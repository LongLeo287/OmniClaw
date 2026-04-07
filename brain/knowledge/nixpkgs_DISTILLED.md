---
id: nixpkgs
type: knowledge
owner: OA_Triage
---
# nixpkgs
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
<p align="center">
  <a href="https://nixos.org">
    <picture>
      <source media="(prefers-color-scheme: light)" srcset="https://brand.nixos.org/logos/nixos-logo-default-gradient-black-regular-horizontal-minimal.svg">
      <source media="(prefers-color-scheme: dark)" srcset="https://brand.nixos.org/logos/nixos-logo-default-gradient-white-regular-horizontal-minimal.svg">
      <img src="https://brand.nixos.org/logos/nixos-logo-default-gradient-black-regular-horizontal-minimal.svg" width="500px" alt="NixOS logo">
    </picture>
  </a>
</p>

<p align="center">
  <a href="CONTRIBUTING.md"><img src="https://img.shields.io/github/contributors-anon/NixOS/nixpkgs" alt="Contributors badge" /></a>
  <a href="https://opencollective.com/nixos"><img src="https://opencollective.com/nixos/tiers/supporter/badge.svg?label=supporters&color=brightgreen" alt="Open Collective supporters" /></a>
</p>

[Nixpkgs](https://github.com/nixos/nixpkgs) is a collection of over 120,000 software packages that can be installed with the [Nix](https://nixos.org/nix/) package manager.
It also implements [NixOS](https://nixos.org/nixos/), a purely-functional Linux distribution.

# Manuals

* [NixOS Manual](https://nixos.org/nixos/manual) - how to install, configure, and maintain a purely-functional Linux distribution
* [Nixpkgs Manual](https://nixos.org/nixpkgs/manual/) - contributing to Nixpkgs and using programming-language-specific Nix expressions
* [Nix Package Manager Manual](https://nixos.org/nix/manual) - how to write Nix expressions (programs), and how to use Nix command line tools

# Community

* [Discourse Forum](https://discourse.nixos.org/)
* [Matrix Chat](https://matrix.to/#/#space:nixos.org)
* [Official wiki](https://wiki.nixos.org/)
* [Community-maintained list of ways to get in touch](https://wiki.nixos.org/wiki/Get_In_Touch#Chat) (Discord, Telegram, IRC, etc.)

# Other Project Repositories

The sources of all official Nix-related projects are in the [NixOS organization on GitHub](https://github.com/NixOS/).
Here are some of the main ones:

* [Nix](https://github.com/NixOS/nix) - the purely functional package manager
* [NixOps](https://github.com/NixOS/nixops) - the tool to remotely deploy NixOS machines
* [nixos-hardware](https://github.com/NixOS/nixos-hardware) - NixOS profiles to optimize settings for different hardware
* [Nix RFCs](https://github.com/NixOS/rfcs) - the formal process for making substantial changes to the community
* [NixOS homepage](https://github.com/NixOS/nixos-homepage) - the [NixOS.org](https://nixos.org) website
* [hydra](https://github.com/NixOS/hydra) - our continuous integration system
* [NixOS Branding](https://github.com/NixOS/branding) - NixOS branding

# Continuous Integration and Distribution

Nixpkgs and NixOS are built and tested by our continuous integration system, [Hydra](https://hydra.nixos.org/).

* [Continuous package builds for unstable/master](https://hydra.nixos.org/jobset/nixos/trunk-combined)
* [Continuous package builds for the NixOS 25.11 release](https://hydra.nixos.org/jobset/nixos/release-25.11)
* [Tests for unstable/master](https://hydra.nixos.org/job/nixos/trunk-combined/tested#tabs-constituents)
* [Tests for the NixOS 25.11 release](https://hydra.nixos.org/job/nixos/release-25.11/tested#tabs-constituents)

Artifacts successfully built with Hydra are published to cache at https://cache.nixos.org/.
When successful build and test criteria are met, the Nixpkgs expressions are distributed via [Nix channels](https://nix.dev/manual/nix/stable/command-ref/nix-channel.html).

# Contributing

Nixpkgs is among the most active projects on GitHub.
While thousands of open issues and pull requests might seem like a lot at first, it helps to consider it in the context of the scope of the project.
Nixpkgs describes how to build tens of thousands of pieces of software and implements a Linux distribution.
The [GitHub Insights](https://github.com/NixOS/nixpkgs/pulse) page gives a sense of the project activity.

Community contributions are always welcome through GitHub Issues and Pull Requests.

For more information about contributing to the project, please visit the [contributing page](CONTRIBUTING.md).

# Donations

The infrastructure for NixOS and related projects is maintained by a nonprofit organization, the [NixOS Foundation](https://nixos.org/nixos/foundation.html).
To ensure the continuity and expansion of the NixOS infrastructure, we are looking for donations to our organization.

You can donate to the NixOS Foundation through [SEPA bank transfers](https://nixos.org/donate.html) or by using Open Collective:

<a href="https://opencollective.com/nixos#support"><img src="https://opencollective.com/nixos/tiers/supporter.svg?width=890" /></a>

# License

Nixpkgs is licensed under the [MIT License](COPYING).

> [!Note]
> MIT license does not apply to the packages built by Nixpkgs, merely to the files in this repository (the Nix expressions, build scripts, NixOS modules, etc.).
It also might not apply to patches included in Nixpkgs, which may be derivative works of the packages to which they apply.
The aforementioned artifacts are all covered by the licenses of the respective packages.

```

### File: ci\README.md
```md
# CI support files

This directory contains files to support CI, such as [GitHub Actions](https://github.com/NixOS/nixpkgs/tree/master/.github/workflows) and [Ofborg](https://github.com/nixos/ofborg).
This is in contrast with [`maintainers/scripts`](../maintainers/scripts) which is for human use instead.

## Pinned Nixpkgs

CI may need certain packages from Nixpkgs.
In order to ensure that the needed packages are generally available without building, [`pinned.json`](./pinned.json) contains a pinned Nixpkgs version tested by Hydra.

Run [`update-pinned.sh`](./update-pinned.sh) to update it.

## GitHub specific code

Some of the code is specific to GitHub.
This code is currently spread out over multiple places and written in both Bash and JavaScript.
The goal is to eventually have all GitHub specific code in `ci/github-script` and written in JavaScript via `actions/github-script`.
A lot of code has already been migrated, but some Bash code still remains.
New CI features need to be introduced in JavaScript, not Bash.

## Nixpkgs merge bot

The Nixpkgs merge bot empowers package maintainers by enabling them to merge PRs related to their own packages.
It serves as a bridge for maintainers to quickly respond to user feedback, facilitating a more self-reliant approach.
Especially when considering there are roughly 20 maintainers for every committer, this bot is a game-changer.

Following [RFC 172], the merge bot was originally implemented as a [python webapp](https://github.com/NixOS/nixpkgs-merge-bot), which has now been integrated into [`ci/github-script/bot.js`](./github-script/bot.js) and [`ci/github-script/merge.js`](./github-script/merge.js).

### Using the merge bot

To merge a PR, maintainers can simply comment:
```gfm
@NixOS/nixpkgs-merge-bot merge
```

The next time the bot runs it will verify the below constraints, then (if satisfied) merge the PR.

The merge bot will reference [#306934](https://github.com/NixOS/nixpkgs/issues/306934) on PRs it merges successfully, [#305350](https://github.com/NixOS/nixpkgs/issues/305350) for unsuccessful attempts, or [#371492](https://github.com/NixOS/nixpkgs/issues/371492) if an error occurs.
These issues effectively list PRs the merge bot has interacted with.

### Merge bot constraints

To ensure security and a focused utility, the bot adheres to specific limitations:

- The PR targets one of the [development branches](#branch-classification).
- The PR only touches files of packages located under `pkgs/by-name/*`.
- The PR is either:
  - approved by a [committer][@NixOS/nixpkgs-committers].
  - backported via label.
  - opened by a [committer][@NixOS/nixpkgs-committers].
  - opened by [@r-ryantm](https://nix-community.github.io/nixpkgs-update/r-ryantm/).
- The user attempting to merge is a member of [@NixOS/nixpkgs-maintainers].
- The user attempting to merge is a maintainer of all packages touched by the PR.

### Approving merge bot changes

Changes to the bot can usually be approved by the [@NixOS/nixpkgs-ci] team, as with other CI changes.
However, additional acknowledgement from the [@NixOS/nixpkgs-core] team is required for changes to what the merge bot will merge, who is eligible to use the merge bot, or similar changes in scope.

## `ci/nixpkgs-vet.sh BASE_BRANCH [REPOSITORY]`

Runs the [`nixpkgs-vet` tool](https://github.com/NixOS/nixpkgs-vet) on the HEAD commit, closely matching what CI does.
This can't do exactly the same as CI, because CI needs to rely on GitHub's server-side Git history to compute the mergeability of PRs before the check can be started.
In turn, when contributors are running this tool locally, we don't want to have to push commits to test them, and we can also rely on the local Git history to do the mergeability check.

Arguments:

- `BASE_BRANCH`: The base branch to use, e.g. master or release-24.05
- `REPOSITORY`: The repository from which to fetch the base branch.
  Defaults to <https://github.com/NixOS/nixpkgs.git>.

# Branch classification

For the purposes of CI, branches in the NixOS/nixpkgs repository are classified as follows:

- **Channel** branches
  - `nixos-` or `nixpkgs-` prefix
  - Are only updated from `master` or `release-` branches, when hydra passes.
  - Otherwise not worked on, Pull Requests are not allowed.
  - Long-lived, no deletion, no force push.
- **Primary development** branches
  - `release-` prefix and `master`
  - Pull Requests required.
  - Long-lived, no deletion, no force push.
- **Secondary development** branches
  - `staging-` prefix and `haskell-updates`
  - Pull Requests normally required, except when merging development branches into each other.
  - Long-lived, no deletion, no force push.
- **Work-In-Progress** branches
  - `backport-`, `revert-` and `wip-` prefixes.
  - Deprecated: All other branches, not matched by channel/development.
  - Pull Requests are optional.
  - Short-lived, force push allowed, deleted after merge.

Some branches also have a version component, which is either `unstable` or `YY.MM`.

`ci/supportedBranches.js` is a script imported by CI to classify the base and head branches of a Pull Request.
This classification will then be used to skip certain jobs.
This script can also be run locally to print basic test cases.


[@NixOS/nixpkgs-maintainers]: https://github.com/orgs/NixOS/teams/nixpkgs-maintainers
[@NixOS/nixpkgs-committers]: https://github.com/orgs/NixOS/teams/nixpkgs-committers
[@NixOS/nixpkgs-ci]: https://github.com/orgs/NixOS/teams/nixpkgs-ci
[@NixOS/nixpkgs-core]: https://github.com/orgs/NixOS/teams/nixpkgs-core
[RFC 172]: https://github.com/NixOS/rfcs/pull/172

```

### File: doc\README.md
```md
# Contributing to the Nixpkgs reference manual

This directory houses the source files for the Nixpkgs reference manual.

> [!IMPORTANT]
> We are actively restructuring our documentation to follow the [Diátaxis framework](https://diataxis.fr/)
>
> Going forward, this directory should **only** contain [reference documentation](https://nix.dev/contributing/documentation/diataxis#reference).
> For tutorials, guides and explanations, contribute to <https://nix.dev/> instead.
>
> We are actively working to generate **all** reference documentation from the [doc-comments](https://github.com/NixOS/rfcs/blob/master/rfcs/0145-doc-strings.md) present in code.
> This also provides the benefit of using `:doc` in the `nix repl` to view reference documentation locally on the fly.

For documentation only relevant for contributors, use Markdown files next to the source and regular code comments.

> [!TIP]
> Feedback for improving support for parsing and rendering doc-comments is highly appreciated.
> [Open an issue](https://github.com/NixOS/nixpkgs/issues/new?labels=6.topic%3A+documentation&title=Doc%3A+) to request bugfixes or new features.

Rendered documentation:
- [Unstable (from master)](https://nixos.org/manual/nixpkgs/unstable/)
- [Stable (from latest release)](https://nixos.org/manual/nixpkgs/stable/)

The rendering tool is [nixos-render-docs](../pkgs/by-name/ni/nixos-render-docs), sometimes abbreviated `nrd`.

## Contributing to this documentation

You can quickly check your edits with `nix-build`:

```ShellSession
$ cd /path/to/nixpkgs
$ nix-build doc
```

If the build succeeds, the manual will be in `./result/share/doc/nixpkgs/manual.html`.

### Development environment

In order to reduce repetition, consider using tools from the provided development environment:

Load it from the Nixpkgs documentation directory with

```ShellSession
$ cd /path/to/nixpkgs/doc
$ nix-shell
```

To load the development utilities automatically when entering that directory, [set up `nix-direnv`](https://nix.dev/guides/recipes/direnv).

Make sure that your local files aren't added to Git history by adding the following lines to `.git/info/exclude` at the root of the Nixpkgs repository:

```
/**/.envrc
/**/.direnv
```

#### `devmode`

Use [`devmode`](../pkgs/by-name/de/devmode/README.md) for a live preview when editing the manual.

### Testing redirects

Once you have a successful build, you can open the relevant HTML (path mentioned above) in a browser along with the anchor, and observe the redirection.

Note that if you already loaded the page and *then* input the anchor, you will need to perform a reload.
This is because browsers do not re-run client JS code when only the anchor has changed.

## Syntax

As per [RFC 0072](https://github.com/NixOS/rfcs/pull/72), all new documentation content should be written in [CommonMark](https://commonmark.org/) Markdown dialect.

Additional syntax extensions are available, all of which can be used in NixOS option documentation.
The following extensions are currently used:

#### Tables

Tables, using the [GitHub-flavored Markdown syntax](https://github.github.com/gfm/#tables-extension-).

#### Anchors

Explicitly defined **anchors** on headings, to allow linking to sections.
These should be always used, to ensure the anchors can be linked even when the heading text changes, and to prevent conflicts between [automatically assigned identifiers](https://github.com/jgm/commonmark-hs/blob/master/commonmark-extensions/test/auto_identifiers.md).

It uses the widely compatible [header attributes](https://github.com/jgm/commonmark-hs/blob/master/commonmark-extensions/test/attributes.md) syntax:

```markdown
## Syntax {#sec-contributing-markup}
```

> [!Note]
> NixOS option documentation does not support headings in general.

#### Inline Anchors

Allow linking to an arbitrary place in the text (e.g. individual list items, sentences…).

They are defined using a hybrid of the link syntax with the attributes syntax known from headings, called [bracketed spans](https://github.com/jgm/commonmark-hs/blob/master/commonmark-extensions/test/bracketed_spans.md):

```markdown
- []{#ssec-gnome-hooks-glib} `glib` setup hook will populate `GSETTINGS_SCHEMAS_PATH` and then `wrapGApps*` hook will prepend it to `XDG_DATA_DIRS`.
```

#### Automatic links

If you **omit a link text** for a link pointing to a section, the text will be substituted automatically.
For example `[](#chap-contributing)`.

This syntax is taken from [MyST](https://myst-parser.readthedocs.io/en/latest/using/syntax.html#targets-and-cross-referencing).


#### HTML

Inlining HTML is not allowed.
Parts of the documentation get rendered to various non-HTML formats, such as man pages in the case of NixOS manual.

#### Roles

If you want to link to a man page, you can use `` {manpage}`nix.conf(5)` ``.
The references will turn into links when a mapping exists in [`doc/manpage-urls.json`](./manpage-urls.json).
Please keep the `manpage-urls.json` file alphabetically sorted.

A few markups for other kinds of literals are also available:

- `` {command}`rm -rfi` ``
- `` {env}`XDG_DATA_DIRS` ``
- `` {file}`/etc/passwd` ``
- `` {option}`networking.useDHCP` ``
- `` {var}`/etc/passwd` ``

These literal kinds are used mostly in NixOS option documentation.

This syntax is taken from [MyST](https://myst-parser.readthedocs.io/en/latest/syntax/syntax.html#roles-an-in-line-extension-point).
Though, the feature originates from [reStructuredText](https://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html#role-manpage) with slightly different syntax.
They are handled by `myst_role` defined per renderer. <!-- reverse references in code -->

#### Admonitions

Set off from the text to bring attention to something.

It uses pandoc’s [fenced `div`s syntax](https://github.com/jgm/commonmark-hs/blob/master/commonmark-extensions/test/fenced_divs.md):

```markdown
::: {.warning}
This is a warning
:::
```

The following are supported:

- `caution`
- `important`
- `note`
- `tip`
- `warning`
- `example`

Example admonitions require a title to work.
If you don't provide one, the manual won't be built.

```markdown
::: {.example #ex-showing-an-example}

# Title for this example

Text for the example.
:::
```

#### [Definition lists](https://github.com/jgm/commonmark-hs/blob/master/commonmark-extensions/test/definition_lists.md)

For defining a group of terms:

```markdown
pear
:   green or yellow bulbous fruit

watermelon
:   green fruit with red flesh
```

## Commit conventions

- Make sure you read about the [commit conventions](../CONTRIBUTING.md#commit-conventions) common to Nixpkgs as a whole.

- If creating a commit purely for documentation changes, format the commit message in the following way:

  ```
  doc: (documentation summary)

  (Motivation for change, relevant links, additional information.)
  ```

  Examples:

  * doc: update the kernel config documentation to use `nix-shell`
  * doc: add information about `nix-update-script`

    Closes #216321.

- If the commit contains more than just documentation changes, follow the commit message format relevant for the rest of the changes.

## Documentation conventions

In an effort to keep the Nixpkgs manual in a consistent style, please follow the conventions below, unless they prevent you from properly documenting something.
In that case, please open an issue about the particular documentation convention and tag it with a "needs: documentation" label.
When needed, each convention explains why it exists, so you can make a decision whether to follow it or not based on your particular case.
Note that these conventions are about the **structure** of the manual (and its source files), not about the content that goes in it.
You, as the writer of documentation, are still in charge of its content.

### One sentence per line

Put each sentence in its own line.
This makes reviews and suggestions much easier, since GitHub's review system is based on lines.
It also helps identifying long sentences at a glance.

Not everything has been migrated to this format yet.
Please always use it for new content.
When changing existing content, update formatting if possible, but avoid excessive diffs.

### Writing Function Documentation

Function documentation is *reference documentation*, for which
[diataxis Reference documentation](https://diataxis.fr/reference/) (8 minutes) is **mandatory reading**.

On top of the diataxis framework, which provides a balanced perspective on what reference documentation should contain, we apply a specific style rule to function documentation:
the first sentence is in present tense, active voice, and the subject is omitted, referring implicitly to the name of the function.
For example:

```nix
/**
  Subtracts value `b` from value `a`.

  Returns the difference as a number.
*/
subtractValues # ...elided code
```

Renders as:

```md
## `subtractValues`

Subtracts value `b` from value `a`.

Returns the difference as a number.
```

### Callouts and examples

Use the [admonition syntax](#admonitions) for callouts and examples.

### Provide self-contained examples

Provide at least one example per function, and make examples self-contained.
This is easier to understand for beginners.
It also helps with testing that it actually works – especially once we introduce automation.

Example code should be such that it can be passed to `pkgs.callPackage`.
Instead of something like:

```nix
pkgs.dockerTools.buildLayeredImage {
  name = "hello";
  contents = [ pkgs.hello ];
}
```

Write something like:

```nix
{ dockerTools, hello }:
dockerTools.buildLayeredImage {
  name = "hello";
  contents = [ hello ];
}
```

### REPLs

When showing inputs/outputs of any [REPL](https://en.wikipedia.org/wiki/Read%E2%80%93eval%E2%80%93print_loop), such as a shell or the Nix REPL, use a format as you'd see in the REPL, while trying to visually separate inputs from outputs.
This means that for a shell, you should use a format like the following:
```shell
$ nix-build -A hello '<nixpkgs>' \
  --option require-sigs false \
  --option trusted-substituters file:///tmp/hello-cache \
  --option substituters file:///tmp/hello-cache
/nix/store/zhl06z4lrfrkw5rp0hnjjfrgsclzvxpm-hello-2.12.1
```
Note how the input is preceded by `$` on the first line and indented on subsequent lines, and how the output is provided as you'd see on the shell.

For the Nix REPL, you should use a format like the following:
```shell
nix-repl> builtins.attrNames { a = 1; b = 2; }
[ "a" "b" ]
```
Note how the input is preceded by `nix-repl>` and the output is provided as you'd see on the Nix REPL.

### Headings for inputs, outputs and examples

When documenting functions or anything that has inputs/outputs and example usage, use nested headings to clearly separate inputs, outputs, and examples.
Keep examples as the last nested heading, and link to the examples wherever applicable in the documentation.

The purpose of this convention is to provide a familiar structure for navigating the manual, so any reader can expect to find content related to inputs in an "inputs" heading, examples in an "examples" heading, and so on.
An example:
```
## buildImage

Some explanation about the function here.
Describe a particular scenario, and point to [](#ex-dockerTools-buildImage), which is an example demonstrating it.

### Inputs

Documentation for the inputs of `buildImage`.
Perhaps even point to [](#ex-dockerTools-buildImage) again when talking about something specifically linked to it.

### Passthru outputs

Documentation for any passthru outputs of `buildImage`.

### Examples

Note that this is the last nested heading in the `buildImage` section.

:::{.example #ex-dockerTools-buildImage}

# Using `buildImage`

Example of how to use `buildImage` goes here.

:::
```

### Function arguments

Use [definition lists](#definition-lists) to document function arguments, and the attributes of such arguments as well as their [types](https://nixos.org/manual/nix/stable/language/values).
For example:

```markdown
# pkgs.coolFunction {#pkgs.coolFunction}

`pkgs.coolFunction` *`name`* *`config`*

Description of what `callPackage` does.


## Inputs {#pkgs-coolFunction-inputs}

If something's special about `coolFunction`'s general argument handling, you can say so here.
Otherwise, just describe the single argument or start the arguments' definition list without introduction.

*`name`* (String)

: The name of the resulting image.

*`config`* (Attribute set)

: Introduce the parameter. Maybe you have a test to make sure `{ }` is a sensible default; then you can say: these attributes are optional; `{ }` is a valid argument.

  `outputHash` (String; _optional_)

  : A brief explanation including when and when not to pass this attribute.

  : _Default:_ the output path's hash.
```

Checklist:
- Start with a synopsis, to show the order of positional arguments.
- Metavariables are in emphasized code spans: ``` *`arg1`* ```.
  Metavariables are placeholders where users may write arbitrary expressions.
  This includes positional arguments.
- Attribute names are regular code spans: ``` `attr1` ```.
  These identifiers can _not_ be picked freely by users, so they are _not_ metavariables.
- _optional_ attributes have a _`Default:`_ if it's easily described as a value.
- _optional_ attributes have a _`Default behavior:`_ if it's not easily described using a value.
- Nix types aren't in code spans, because they are not code
- Nix types are capitalized, to distinguish them from the camelCase Module System types, which _are_ code and behave like functions.

#### Examples

To define a referenceable figure use the following fencing:

```markdown
:::{.example #an-attribute-set-example}
# An attribute set example

You can add text before

    ```nix
    { a = 1; b = 2;}
    ```

and after code fencing
:::
```

Defining examples through the `example` fencing class adds them to a "List of Examples" section after the Table of Contents.
Though this is not shown in the rendered documentation on nixos.org.

#### Figures

To define a referenceable figure use the following fencing:

```markdown
::: {.figure #nixos-logo}
# NixOS Logo
![NixOS logo](./nixos_logo.png)
:::
```

Defining figures through the `figure` fencing class adds them to a `List of Figures` after the `Table of Contents`.
Though this is not shown in the rendered documentation on nixos.org.

#### Footnotes

To add a footnote explanation, use the following syntax:

```markdown
Sometimes it's better to add context [^context] in a footnote.

[^context]: This explanation will be rendered at the end of the chapter.
```

#### Inline comments

Inline comments are supported with following syntax:

```markdown
<!-- This is an inline comment -->
```

The comments will not be rendered in the rendered HTML.

#### Link reference definitions

Links can reference a label, for example, to make the link target reusable:

```markdown
::: {.note}
Reference links can also be used to [shorten U
... [TRUNCATED]
```

### File: lib\README.md
```md
# Nixpkgs lib

This directory contains the implementation, documentation and tests for the Nixpkgs `lib` library.

## Overview

The evaluation entry point for `lib` is [`default.nix`](default.nix).
This file evaluates to an attribute set containing two separate kinds of attributes:
- Sub-libraries:
  Attribute sets grouping together similar functionality.
  Each sub-library is defined in a separate file usually matching its attribute name.

  Example: `lib.lists` is a sub-library containing list-related functionality such as `lib.lists.take` and `lib.lists.imap0`.
  These are defined in the file [`lists.nix`](lists.nix).

- Aliases:
  Attributes that point to an attribute of the same name in some sub-library.

  Example: `lib.take` is an alias for `lib.lists.take`.

Most files in this directory are definitions of sub-libraries, but there are a few others:
- [`minfeatures.nix`](minfeatures.nix): A list of conditions for the used Nix version to match that are required to evaluate Nixpkgs.
- [`tests`](tests): Tests, see [Running tests](#running-tests)
  - [`release.nix`](tests/release.nix): A derivation aggregating all tests
  - [`misc.nix`](tests/misc.nix): Evaluation unit tests for most sub-libraries
  - `*.sh`: Bash scripts that run tests for specific sub-libraries
  - All other files in this directory exist to support the tests
- [`systems`](systems): The `lib.systems` sub-library, structured into a directory instead of a file due to its complexity
- [`path`](path): The `lib.path` sub-library, which includes tests as well as a document describing the design goals of `lib.path`
- All other files in this directory are sub-libraries

### Module system

The [module system](https://nixos.org/manual/nixpkgs/#module-system) spans multiple sub-libraries:
- [`modules.nix`](modules.nix): `lib.modules` for the core functions and anything not relating to option definitions
- [`options.nix`](options.nix): `lib.options` for anything relating to option definitions
- [`types.nix`](types.nix): `lib.types` for module system types

## PR Guidelines

Follow these guidelines for proposing a change to the interface of `lib`.

### Provide a Motivation

Clearly describe why the change is necessary and its use cases.

Make sure that the change benefits the user more than the added mental effort of looking it up and keeping track of its definition.
If the same can reasonably be done with the existing interface,
consider just updating the documentation with more examples and links.
This is also known as the [Fairbairn Threshold](https://wiki.haskell.org/Fairbairn_threshold).

Through this principle we avoid the human cost of duplicated functionality in an overly large library.

### Make one PR for each change

Don't have multiple changes in one PR, instead split it up into multiple ones.

This keeps the conversation focused and has a higher chance of getting merged.

### Name the interface appropriately

When introducing new names to the interface, such as new function, or new function attributes,
make sure to name it appropriately.

Names should be self-explanatory and consistent with the rest of `lib`.
If there's no obvious best name, include the alternatives you considered.

### Write documentation

Update the [reference documentation](#reference-documentation) to reflect the change.

Be generous with links to related functionality.

### Write tests

Add good test coverage for the change, including:

- Tests for edge cases, such as empty values or lists.
- Tests for tricky inputs, such as a string with string context or a path that doesn't exist.
- Test all code paths, such as `if-then-else` branches and returned attributes.
- If the tests for the sub-library are written in bash,
  test messages of custom errors, such as `throw` or `abortMsg`,

  At the time this is only not necessary for sub-libraries tested with [`tests/misc.nix`](./tests/misc.nix).

See [running tests](#running-tests) for more details on the test suites.

### Write tidy code

Name variables well, even if they're internal.
The code should be as self-explanatory as possible.
Be generous with code comments when appropriate.

As a baseline, follow the [Nixpkgs code conventions](https://github.com/NixOS/nixpkgs/blob/master/CONTRIBUTING.md#code-conventions).

### Write efficient code

Nix generally does not have free abstractions.
Be aware that seemingly straightforward changes can cause more allocations and a decrease in performance.
That said, don't optimise prematurely, especially in new code.

## Reference documentation

Reference documentation for library functions is written above each function as a multi-line comment.
These comments are processed using [nixdoc](https://github.com/nix-community/nixdoc) and [rendered in the Nixpkgs manual](https://nixos.org/manual/nixpkgs/stable/#chap-functions).
The nixdoc README describes the [comment format](https://github.com/nix-community/nixdoc#comment-format).

See [doc/README.md](../doc/README.md) for how to build the manual.

## Running tests

All library tests can be run by building the derivation in [`tests/release.nix`](tests/release.nix):

```bash
nix-build tests/release.nix
```

Some commands for quicker iteration over parts of the test suite are also available:

```bash
# Run all evaluation unit tests in tests/misc.nix
# if the resulting list is empty, all tests passed
nix-instantiate --eval --strict tests/misc.nix

# Run the module system tests
tests/modules.sh

# Run the lib.sources tests
tests/sources.sh

# Run the lib.filesystem tests
tests/filesystem.sh

# Run the lib.path property tests
path/tests/prop.sh

# Run the lib.fileset tests
fileset/tests.sh
```

## Commit conventions

- Make sure you read about the [commit conventions](../CONTRIBUTING.md#commit-conventions) common to Nixpkgs as a whole.

- Format the commit messages in the following way:

  ```
  lib.(section): (init | add additional argument | refactor | etc)

  (Motivation for change. Additional information.)
  ```

  Examples:

  * lib.getExe': check arguments
  * lib.fileset: Add an additional argument in the design docs

    Closes #264537


```

### File: modules\README.md
```md
# `<nixpkgs>/modules`

This directory hosts subdirectories representing each module [class](https://nixos.org/manual/nixpkgs/stable/#module-system-lib-evalModules-param-class) for which the `nixpkgs` repository has user-importable modules.

Exceptions:
- `_class = "nixos";` modules go in the `<nixpkgs>/nixos/modules` tree
- modules whose only purpose is to test code in this repository

The emphasis is on _importable_ modules, i.e. ones that aren't inherent to and built into the Module System application.

```

### File: .github\workflows\README.md
```md
# GitHub Actions Workflows

Some architectural notes about key decisions and concepts in our workflows:

- Instead of `pull_request` we use [`pull_request_target`](https://docs.github.com/actions/writing-workflows/choosing-when-your-workflow-runs/events-that-trigger-workflows#pull_request_target) for all PR-related workflows.
  This has the advantage that those workflows will run without prior approval for external contributors.

- Running on `pull_request_target` also optionally provides us with a GH_TOKEN with elevated privileges (write access), which we need to do things like adding labels, requesting reviewers or pushing branches.
  **Note about security:** We need to be careful to limit the scope of elevated privileges as much as possible.
  Thus they should be lowered to the minimum with `permissions: {}` in every workflow by default.

- By definition `pull_request_target` runs in the context of the **base** of the pull request.
  This means that the workflow files to run will be taken from the base branch, not the PR, and actions/checkout will not checkout the PR, but the base branch, by default.
  To protect our secrets, we need to make sure to **never execute code** from the pull request and always evaluate or build nix code from the pull request with the **sandbox enabled**.

- To test the pull request's contents, we checkout the "test merge commit".
  This is a temporary commit that GitHub creates automatically as "what would happen if this PR was merged into the base branch now?".
  The checkout could be done via the virtual branch `refs/pull/<pr-number>/merge`, but doing so would cause failures when this virtual branch doesn't exist (anymore).
  This can happen when the PR has conflicts, in which case the virtual branch is not created, or when the PR is getting merged while workflows are still running, in which case the branch won't exist anymore at the time of checkout.
  Thus, we use the `prepare` job to check whether the PR is mergeable and the test merge commit exists and only then run the relevant jobs.

- Various workflows need to make comparisons against the base branch.
  In this case, we checkout the parent of the "test merge commit" for best results.
  Note that this is not necessarily the same as the default commit that actions/checkout would use, which is also a commit from the base branch (see above), but might be older.

## Terminology

- **base commit**: The pull_request_target event's context commit, i.e. the base commit given by GitHub Actions.
  Same as `github.event.pull_request.base.sha`.
- **head commit**: The HEAD commit in the pull request's branch.
  Same as `github.event.pull_request.head.sha`.
- **merge commit**: The temporary "test merge commit" that GitHub Actions creates and updates for the pull request.
  Same as `refs/pull/${{ github.event.pull_request.number }}/merge`.
- **target commit**: The base branch's parent of the "test merge commit" to compare against.

## Concurrency Groups

We use [GitHub's Concurrency Groups](https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/control-the-concurrency-of-workflows-and-jobs) to cancel older jobs on pushes to Pull Requests.
When two workflows are in the same group, a newer workflow cancels an older workflow.
Thus, it is important how to construct the group keys:

- Because we want to run jobs for different events at same time, we add `github.event_name` to the key.
  This is the case for the `pull_request` which runs on changes to the workflow files to test the new files and the same workflow from the base branch run via `pull_request_event`.

- We don't want workflows of different Pull Requests to cancel each other, so we include `github.event.pull_request.number`.
  The [GitHub docs](https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/control-the-concurrency-of-workflows-and-jobs#example-using-a-fallback-value) show using `github.head_ref` for this purpose, but this doesn't work well with forks: Different users could have the same head branch name in their forks and run CI for their PRs at the same time.

- Sometimes, there is no `pull_request.number`.
  To ensure non-PR runs are never cancelled, we add a fallback of `github.run_id`.
  This is a unique value for each workflow run.

- Of course, we run multiple workflows at the same time, so we add `github.workflow` to the key.
  Otherwise workflows would cancel each other.

- There is a special case for reusable workflows called via `workflow_call` - they will have `github.workflow` set to their parent workflow's name.
  Thus, they would cancel each other.
  That's why we additionally hardcode the name of the workflow as well.

This results in a key with the following semantics:

```
<running-workflow>-<triggering-workflow>-<triggered-event>-<pull-request/fallback>
```

## Required Status Checks

The "Required Status Checks" branch ruleset is implemented in two top-level workflows: `pull-request-target.yml` and `merge-group.yml`.

The PR workflow defines all checks that need to succeed to add a Pull Request to the Merge Queue.
If no Merge Queue is set up for a branch, the PR workflow defines the checks required to merge into the target branch.

The Merge Group workflow defines all checks that are run as part of the Merge Queue.
Only when these pass, a Pull Request is finally merged into the target branch.
They don't apply when no Merge Queue is set up.

Both workflows work with the same `no PR failures` status check.
This name can never be changed, because it's used in the branch ruleset for these rules.

```

### File: ci\eval\README.md
```md
# Nixpkgs CI evaluation

The code in this directory is used by the [eval.yml](../../.github/workflows/eval.yml) GitHub Actions workflow to evaluate the majority of Nixpkgs for all PRs, effectively making sure that when the development branches are processed by Hydra, no evaluation failures are encountered.

Furthermore it also allows local evaluation using:

```
nix-build ci -A eval.baseline
```

The two most important arguments are:
- `--arg evalSystems`: The set of systems for which `nixpkgs` should be evaluated.
  Defaults to the [supported systems](../../pkgs/top-level/release-supported-systems.json) for the branch.
  Example: `--arg evalSystems '["x86_64-linux" "aarch64-darwin"]'`
- `--arg quickTest`: Enables testing a single chunk of the current system only for quick iteration.
  Example: `--arg quickTest true`

The following arguments can be used to fine-tune performance:
- `--max-jobs`: The maximum number of derivations to run at the same time.
  Only each supported system gets a separate derivation, so it doesn't make sense to set this higher than that number.
- `--cores`: The number of cores to use for each job.
  Recommended to set this to the number of cores on your system divided by `--max-jobs`.
- `--arg chunkSize`: The number of attributes that are evaluated simultaneously on a single core.
  Lowering this decreases memory usage at the cost of increased evaluation time.
  If this is too high, there won't be enough chunks to process them in parallel, and will also increase evaluation time.
  The default is 5000.
  Example: `--arg chunkSize 10000`

Note that 16GB memory is the recommended minimum, while with less than 8GB memory evaluation time suffers greatly.

## Local eval with rebuilds / comparison

To compare two commits locally, first run the following on the baseline commit:

```
nix-build ci -A eval.baseline --out-link baseline
```

Then, on the commit with your changes:

```
nix-build ci -A eval.full --arg baseline ./baseline
```

Keep in mind to otherwise pass the same set of arguments for both commands (`evalSystems`, `quickTest`, `chunkSize`).
Running this command will evaluate the difference between the baseline statistics and the ones at the time of running the command.
From that difference, it will produce a human-readable report in `$out/step-summary.md`.
If no packages were added or removed, then performance statistics will also be generated as part of this report.

```

### File: CONTRIBUTING.md
```md
# Contributing to Nixpkgs

This document is for people wanting to contribute to Nixpkgs.
This involves changes that are proposed using [GitHub](https://github.com) [pull requests](https://docs.github.com/pull-requests) to the [Nixpkgs repository](https://github.com/nixos/nixpkgs).

A GitHub account is recommended, which you can sign up for [here](https://github.com/signup).
See [here](https://discourse.nixos.org/t/about-the-patches-category/477) for how to contribute without a GitHub account.

This document assumes that you already know how to use GitHub and Git.
If that's not the case, we recommend learning about it [here](https://docs.github.com/en/get-started/quickstart/hello-world).

## Overview
[overview]: #overview

This file contains general contributing information.
More specific information about individual parts of Nixpkgs can be found here:
- [`doc`](./doc/README.md): Sources and infrastructure for the [Nixpkgs manual](https://nixos.org/manual/nixpkgs/stable/)
- [`lib`](./lib/README.md): Sources and documentation of the [library functions](https://nixos.org/manual/nixpkgs/stable/#chap-functions)
- [`maintainers`](./maintainers/README.md): Nixpkgs maintainer and team listings, maintainer scripts
- [`nixos`](./nixos/README.md): Implementation of [NixOS](https://nixos.org/manual/nixos/stable/)
- [`pkgs`](./pkgs/README.md): Package and [builder](https://nixos.org/manual/nixpkgs/stable/#part-builders) definitions

# How to's

## How to create pull requests
[pr-create]: #how-to-create-pull-requests

This section describes how changes can be proposed with a pull request (PR).

> [!Note]
> Be aware that contributing implies licensing those contributions under the terms of [COPYING](./COPYING), an MIT-like license.

0. Set up a local version of Nixpkgs to work with:
   1. [Fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo#forking-a-repository) the [Nixpkgs repository](https://github.com/nixos/nixpkgs).
   1. [Clone the forked repository](https://docs.github.com/en/get-started/quickstart/fork-a-repo#cloning-your-forked-repository) into a local `nixpkgs` directory.
   1. [Configure the upstream Nixpkgs repository](https://docs.github.com/en/get-started/quickstart/fork-a-repo#configuring-git-to-sync-your-fork-with-the-upstream-repository).

1. Select the appropriate [base branch](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-branches#working-with-branches) for the change, as [described here][branch].
   If in doubt, use `master`.
   This can be changed later by [rebasing][rebase].

2. Create a new Git branch, ideally such that:
   - The name of the branch hints at your change, e.g. `update-hello`.
   - The branch contains the most recent base branch.

   We'll assume the base branch `master` here.

   ```bash
   # Make sure you have the latest changes from upstream Nixpkgs
   git fetch upstream

   # Create and switch to a new branch, based on the base branch in Nixpkgs
   git switch --create update-hello upstream/master
   ```

   To avoid potentially having to download and build many derivations, you can base on a specific [Git commit](https://www.git-scm.com/docs/gitglossary#def_commit) instead:
   - The commit of the latest `nixpkgs-unstable` channel, available [here](https://channels.nixos.org/nixpkgs-unstable/git-revision).
   - The commit of a local Nixpkgs downloaded using [nix-channel](https://nixos.org/manual/nix/stable/command-ref/nix-channel), available using `nix-instantiate --eval --expr '(import <nixpkgs/lib>).trivial.revisionWithDefault null'`
   - If you're using NixOS, the commit of your NixOS installation, available with `nixos-version --revision`.

   You can use this commit instead of `upstream/master` in the above command:
   ```bash
   # Here, b9c03fbb is an example commit from nixpkgs-unstable
   git switch --create update-hello b9c03fbb
   ```

3. Make your changes in the local Nixpkgs repository and:
   - Adhere to both the [general code conventions][code-conventions], and the relevant [specific code conventions][overview].
   - Test the changes.
   - If necessary, document the changes.

   See the [overview section][overview] for more specific information.

4. Commit your changes using `git commit`.
   Make sure to adhere to the [commit conventions](#commit-conventions).

   Repeat the steps 3-4 as many times as necessary.
   Advance to the next step once all the commits make sense together.
   You can view your commits with `git log`.

5. Push your commits to your fork of Nixpkgs:
   ```
   git push --set-upstream origin HEAD
   ```

   The above command will output a link to directly do the next step:
   ```
   remote: Create a pull request for 'update-hello' on GitHub by visiting:
   remote:      https://github.com/myUser/nixpkgs/pull/new/update-hello
   ```

6. [Create a pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request#creating-the-pull-request) from the new branch in your Nixpkgs fork to the upstream Nixpkgs repository.
   Use the branch from step 1 as the PR's base branch.
   Go through the [pull request template][pr-template].

7. Respond to review comments and potentially to CI failures and merge conflicts by updating the PR.
   Always keep it in a mergeable state.

   The non-technical side of this process is covered in [I opened a PR, how do I get it merged?](#i-opened-a-pr-how-do-i-get-it-merged).

   The [ofborg](https://github.com/NixOS/ofborg) CI system will perform checks to ensure code quality.
   You can see the results at the bottom of the PR.
   See [the ofborg Readme](https://github.com/NixOS/ofborg#readme) for more details.

   - To add new commits, repeat steps 3-4 and push the result:
     ```
     git push
     ```

   - To change existing commits, [rewrite the Git history](https://git-scm.com/book/en/v2/Git-Tools-Rewriting-History).
     Useful Git commands for this are `git commit --patch --amend` and `git rebase --interactive`.
     With a rewritten history you need to force-push the commits:
     ```
     git push --force-with-lease
     ```

   - If there are merge conflicts, you will have to [rebase the branch](https://git-scm.com/book/en/v2/Git-Branching-Rebasing) onto the current **base branch**.
     Sometimes this can be done [on GitHub directly](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/keeping-your-pull-request-in-sync-with-the-base-branch#updating-your-pull-request-branch).
     To rebase locally:
     ```
     git fetch upstream
     git rebase upstream/master
     git push --force-with-lease
     ```

     Use the base branch from step 1 instead of `upstream/master`.

   - If you need to change the base branch, [rebase][rebase].

8. If your PR is merged and [acceptable for releases][release-acceptable], you may [backport][pr-backport] it.

### Pull request template
[pr-template]: #pull-request-template

The pull request template helps to determine which steps have been taken so far.
Details not covered by the title and links to existing related issues should go at the top.

When a PR is created, it will be pre-populated with some checkboxes.

#### Tested using sandboxing

When sandbox builds are enabled, Nix will set up an isolated environment for each build process.
It is used to remove further hidden dependencies set by the build environment, to improve reproducibility.
This includes access to the network during the build outside of `fetch*` functions and files outside the Nix store.
Depending on the operating system, access to other resources is blocked as well; see [sandbox](https://nixos.org/manual/nix/stable/command-ref/conf-file#conf-sandbox) in the Nix manual for details.

Please test builds with sandboxing enabled, because it is also used in [Hydra](https://nixos.org/hydra).

If you are on Linux, sandboxing is enabled by default.
On other platforms, sandboxing is disabled by default due to a small performance hit on each build.

Please enable sandboxing **before** building the package by adding the following to `/etc/nix/nix.conf`:

  ```ini
  sandbox = true
  ```

#### Built on platform(s)

Many Nix packages are designed to run on multiple platforms.
As such, it’s important to let the maintainer know which platforms you have tested on.
It’s not always practical to test all platforms, and it’s not required for a pull request to be merged.
Only check the platforms you tested the build on in this section.

#### Tested via one or more NixOS test(s) if existing and applicable for the change (look inside nixos/tests)

Packages with automated tests are likely merged quicker, because they don’t require as much manual testing.
If there are existing tests for the package, they should be run.
NixOS tests can only be run on linux.
For more details on writing and running tests, see the [section in the NixOS manual](https://nixos.org/nixos/manual/index.html#sec-nixos-tests).

#### Tested compilation of all pkgs that depend on this change using `nixpkgs-review`

If you are modifying a package, you can use `nixpkgs-review` to make sure all packages that depend on the updated package still build.
It can work on uncommitted changes with the `wip` option or on a specific pull request.

Review changes from pull request number 12345:

```ShellSession
nix-shell -p nixpkgs-review --run "nixpkgs-review pr 12345"
```

Alternatively, with flakes (and analogously for the other commands below):

```ShellSession
nix run nixpkgs#nixpkgs-review -- pr 12345
```

Review uncommitted changes:

```ShellSession
nix-shell -p nixpkgs-review --run "nixpkgs-review wip"
```

Review changes from the last commit:

```ShellSession
nix-shell -p nixpkgs-review --run "nixpkgs-review rev HEAD"
```

#### Tested execution of all binary files (usually in `./result/bin/`)

It's important to test a modified package's executables.
Look into `./result/bin` and run all files in there, or at a minimum, the main executable.
For example, if you make a change to `texlive`, you probably would only check the binaries associated with the change you made, rather than testing all of them.

#### Meets Nixpkgs contribution standards

The last checkbox is about whether it fits the guidelines in this `CONTRIBUTING.md` file.
This document details our standards for commit messages, reviews, licensing of contributions, etc...
Everyone should read and understand these standards before submitting a pull request.

### Rebasing between branches (i.e. from `master` to `staging`)
[rebase]: #rebasing-between-branches-ie-from-master-to-staging

Sometimes, changes must be rebased between branches.
One example is, if the number of rebuilds caused is too large for the original target branch.

In the following example, the current `feature` branch is based on `master`, and we rebase it to have the PR target `staging`.
We rebase on the _merge base_ between `master` and `staging` to avoid too many local rebuilds.


```console
# Rebase your commits onto the common merge base
git rebase --onto upstream/staging... upstream/master
# Force push your changes
git push origin feature --force-with-lease
```

The syntax `upstream/staging...` is equivalent to `upstream/staging...HEAD` and stands for the merge base between `upstream/staging` and `HEAD` (hence between `upstream/staging` and `upstream/master`).

Then use the *Edit* button in the upper right corner of the GitHub PR, and switch the base branch from `master` to `staging`.
*After* the PR has been retargeted, a final rebase onto the target branch might be needed to resolve merge conflicts.

```console
# Rebase onto target branch
git rebase upstream/staging
# Review and fixup possible conflicts
git status
# Force push your changes
git push origin feature --force-with-lease
```

## How to backport pull requests
[pr-backport]: #how-to-backport-pull-requests

Once a PR has been merged, a backport to the corresponding `release-YY.MM` branch can be created.

### Automatically backporting changes

> [!Note]
> You have to be a [Nixpkgs maintainer](./maintainers) to automatically create a backport pull request.

Add the [`backport release-YY.MM` label](https://github.com/NixOS/nixpkgs/labels?q=backport) to the PR on the `master` branch.
This will cause [a GitHub Action](.github/workflows/backport.yml) to open a new PR to the `release-YY.MM` branch a few minutes later.
This can be done on both open or already merged pull requests.

### Manually backporting changes

To manually create a backport, follow [the standard pull request process][pr-create], but:

- Use `release-YY.MM` for the base branch, both for the local branch and the pull request.

> [!Warning]
> Do not use the `nixos-YY.MM` branch.
> It points to the latest _tested_ release channel commit.

- Instead of manually making and committing the changes, use [`git cherry-pick -x`](https://git-scm.com/docs/git-cherry-pick) for each commit.
  Use `git cherry-pick -x <commit>` when the reason is obvious, for example for minor version bumps and fixes.
  Otherwise, use `git cherry-pick -xe <commit>` to add a reason for the backport.
  Here is [an example](https://github.com/nixos/nixpkgs/commit/5688c39af5a6c5f3d646343443683da880eaefb8).

> [!Warning]
> Ensure the commits exist on the `master` branch.
> In the case of squashed or rebased merges, the commit hash will change and the new commits can be found in the merge message at the bottom of the `master` pull request.

- In the pull request description, link to the original pull request to `master`.
  The pull request title should include `[YY.MM]` matching the release you're backporting to.

## How to review pull requests
[pr-review]: #how-to-review-pull-requests

The Nixpkgs project receives a high number of pull requests.
Anyone may review and approve PRs and it is an important contribution to the project.

The high change rate makes any PR that remains open for too long subject to merge conflicts.
To avoid extra work, reviewing PRs timely and being responsive is key.
GitHub provides sort filters to see the [most recently updated](https://github.com/NixOS/nixpkgs/pulls?q=is%3Apr+is%3Aopen+sort%3Aupdated-desc) pull requests.
We highly encourage looking at [this list of ready to merge, unreviewed pull requests](https://github.com/NixOS/nixpkgs/pulls?q=is%3Apr+is%3Aopen+review%3Anone+status%3Asuccess+no%3Aproject+no%3Aassignee+no%3Amilestone).

Controversial changes can lead to controversial opinions, but it is important to respect every community member and their work.
Always be nice and polite.

GitHub provides reactions for quick feedback to pull requests or comments.
The thumb-down reaction should be used with care and, if possible, accompanied with explanation for the submitter to improve their contribution.

When doing a review:
- Aim to drive the proposal to a timely conclusion.
- Foc
... [TRUNCATED]
```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.

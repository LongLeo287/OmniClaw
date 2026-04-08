---
id: repo-fetched-angular-120216
type: knowledge
owner: OA
registered_at: 2026-04-05T03:10:20.643344
tags: ["auto-cloned", "oa-assimilated"]
---

# FETCHED_angular_120216

## Assimilation Report
Auto-cloned repository: FETCHED_angular_120216

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
<h1 align="center">Angular - The modern web developer's platform</h1>

<p align="center">
  <img src="adev/src/assets/images/press-kit/angular_icon_gradient.gif" alt="angular-logo" width="120px" height="120px"/>
  <br>
  <em>Angular is a development platform for building mobile and desktop web applications
    <br> using TypeScript/JavaScript and other languages.</em>
  <br>
</p>

<p align="center">
  <a href="https://angular.dev/"><strong>angular.dev</strong></a>
  <br>
</p>

<p align="center">
  <a href="CONTRIBUTING.md">Contributing Guidelines</a>
  ·
  <a href="https://github.com/angular/angular/issues">Submit an Issue</a>
  ·
  <a href="https://blog.angular.dev/">Blog</a>
  <br>
  <br>
</p>

<p align="center">
  <a href="https://www.npmjs.com/@angular/core">
    <img src="https://img.shields.io/npm/v/@angular/core.svg?logo=npm&logoColor=fff&label=NPM+package&color=limegreen" alt="Angular on npm" />
  </a>
</p>

<hr>

## Documentation

Get started with Angular, learn the fundamentals and explore advanced topics on our documentation website.

- [Getting Started][quickstart]
- [Architecture][architecture]
- [Components and Templates][componentstemplates]
- [Forms][forms]
- [API][api]

### Advanced

- [Angular Elements][angularelements]
- [Server Side Rendering][ssr]
- [Schematics][schematics]
- [Lazy Loading][lazyloading]
- [Animations][animations]

### Local Development

To contribute to the Angular Docs, check out the [Angular.dev README](adev/README.md)

## Development Setup

### Prerequisites

- Install [Node.js] which includes [Node Package Manager][npm]

### Setting Up a Project

Install the Angular CLI globally:

```
npm install -g @angular/cli
```

Create workspace:

```
ng new [PROJECT NAME]
```

Run the application:

```
cd [PROJECT NAME]
ng serve
```

Angular is cross-platform, fast, scalable, has incredible tooling, and is loved by millions.

## Quickstart

[Get started in 5 minutes][quickstart].

## Ecosystem

<p>
  <img src="/contributing-docs/images/angular-ecosystem-logos.png" alt="angular ecosystem logos" width="500px" height="auto">
</p>

- [Angular Command Line (CLI)][cli]
- [Angular Material][angularmaterial]

## Changelog

[Learn about the latest improvements][changelog].

## Upgrading

Check out our [upgrade guide](https://angular.dev/update-guide/) to find out the best way to upgrade your project.

## Contributing

### Contributing Guidelines

Read through our [contributing guidelines][contributing] to learn about our submission process, coding rules, and more.

### Want to Help?

Want to report a bug, contribute some code, or improve the documentation? Excellent! Read up on our guidelines for [contributing][contributing] and then check out one of our issues labeled as <kbd>[help wanted](https://github.com/angular/angular/labels/help%20wanted)</kbd> or <kbd>[good first issue](https://github.com/angular/angular/labels/good%20first%20issue)</kbd>.

### Code of Conduct

Help us keep Angular open and inclusive. Please read and follow our [Code of Conduct][codeofconduct].

## Community

Join the conversation and help the community.

- [X (formerly Twitter)][X (formerly Twitter)]
- [Bluesky][bluesky]
- [Discord][discord]
- [YouTube][youtube]
- [StackOverflow][stackoverflow]
- Find a Local [Meetup][meetup]

[![Love Angular badge](https://img.shields.io/badge/angular-love-blue?logo=angular&angular=love)](https://www.github.com/angular/angular)

**Love Angular? Give our repo a star :star: :arrow_up:.**

[contributing]: CONTRIBUTING.md
[quickstart]: https://angular.dev/tutorials/learn-angular
[changelog]: CHANGELOG.md
[ng]: https://angular.dev
[documentation]: https://angular.dev/overview
[angularmaterial]: https://material.angular.dev/
[cli]: https://angular.dev/tools/cli
[architecture]: https://angular.dev/essentials
[componentstemplates]: https://angular.dev/tutorials/learn-angular/1-components-in-angular
[forms]: https://angular.dev/tutorials/learn-angular/15-forms
[api]: https://angular.dev/api
[angularelements]: https://angular.dev/guide/elements
[ssr]: https://angular.dev/guide/ssr
[schematics]: https://angular.dev/tools/cli/schematics
[lazyloading]: https://angular.dev/guide/routing/define-routes#lazily-loaded-components
[node.js]: https://nodejs.org/
[npm]: https://www.npmjs.com/get-npm
[codeofconduct]: CODE_OF_CONDUCT.md
[X (formerly Twitter)]: https://www.x.com/angular
[bluesky]: https://bsky.app/profile/angular.dev
[discord]: https://discord.gg/angular
[stackoverflow]: https://stackoverflow.com/questions/tagged/angular
[youtube]: https://youtube.com/angular
[meetup]: https://www.meetup.com/find/?keywords=angular
[animations]: https://angular.dev/guide/animations

```

### File: .devcontainer\README.md
```md
# VSCode Remote Development - Developing inside a Container

This folder contains configuration files that can be used to opt into working on this repository in a [Docker container](https://www.docker.com/resources/what-container) via [VSCode](https://code.visualstudio.com/)'s Remote Development feature (see below).

Info on remote development and developing inside a container with VSCode:

- [VSCode: Remote Development](https://code.visualstudio.com/docs/remote/remote-overview)
- [VSCode: Developing inside a Container](https://code.visualstudio.com/docs/remote/containers)
- [VSCode: Remote Development FAQ](https://code.visualstudio.com/docs/remote/faq)

## Usage

_Prerequisite: [Install Docker](https://docs.docker.com/install) on your local environment._

To get started, read and follow the instructions in [Developing inside a Container](https://code.visualstudio.com/docs/remote/containers). The [.devcontainer/](.) directory contains pre-configured `devcontainer.json` and `Dockerfile` files, which you can use to set up remote development with a docker container.

In a nutshell, you need to:

- Install the [Remote - Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) extension.
- Copy [recommended-Dockerfile](./recommended-Dockerfile) to `Dockerfile` (and optionally tweak to suit your needs).
- Copy [recommended-devcontainer.json](./recommended-devcontainer.json) to `devcontainer.json` (and optionally tweak to suit your needs).
- Open VSCode and bring up the [Command Palette](https://code.visualstudio.com/docs/getstarted/userinterface#_command-palette).
- Type `Remote-Containers: Open Folder in Container` and choose your local clone of [angular/angular](https://github.com/angular/angular).

The `.devcontainer/devcontainer.json` and `.devcontainer/Dockerfile` files are ignored by git, so you can have your own local versions. We may occasionally update the template files ([recommended-devcontainer.json](./recommended-devcontainer.json), [recommended-Dockerfile](./recommended-Dockerfile)), in which case you will need to manually update your local copies (if desired).

## Updating `recommended-devcontainer.json` and `recommended-Dockerfile`

You can update and commit the recommended config files (which people use as basis for their local configs), if you find that something is broken, out-of-date or can be improved.

Please, keep in mind that any changes you make will potentially be used by many people on different environments. Try to keep these config files cross-platform compatible and free of personal preferences.

```

### File: .vscode\README.md
```md
# VSCode Configuration

This folder contains opt-in [Workspace Settings](https://code.visualstudio.com/docs/getstarted/settings), [Tasks](https://code.visualstudio.com/docs/editor/tasks), [Launch Configurations](https://code.visualstudio.com/Docs/editor/debugging#_launch-configurations) and [Extension Recommendations](https://code.visualstudio.com/docs/editor/extension-gallery#_workspace-recommended-extensions) that the Angular team recommends using when working on this repository.

## Usage

To use the recommended configurations follow the steps below:

- install the recommended extensions in `.vscode/extensions.json`
- copy (or link) `.vscode/recommended-settings.json` to `.vscode/settings.json`
- restart the editor

If you already have your custom workspace settings, you should instead manually merge the file contents.

This isn't an automatic process, so you will need to repeat it when settings are updated.

To see the recommended extensions select "Extensions: Show Recommended Extensions" in the [Command Palette](https://code.visualstudio.com/docs/getstarted/userinterface#_command-palette).

## Editing `.vscode/recommended-*.json` files

If you wish to add extra configuration items please keep in mind any modifications you make here will be used by many users.

Try to keep these settings/configurations to things that help facilitate the development process and avoid altering the user workflow whenever possible.

```

### File: packages\README.md
```md
# Angular

The sources for this package are in the main [Angular](https://github.com/angular/angular) repo. Please file issues and pull requests against that repo.

Usage information and reference details can be found in [Angular documentation](https://angular.dev/overview).

License: MIT

```

### File: packages\examples\README.md
```md
# API Examples

This folder contains small example apps that get in-lined into our API docs.
Each example contains tests for application behavior (as opposed to testing Angular's
behavior) just like an Angular application developer would write.

# Running the examples

```
# Serving individual examples (e.g. common)
pnpm bazel run //packages/examples/common:devserver

# "core" examples
pnpm bazel run //packages/examples/core:devserver
```

# Running the tests

```
pnpm bazel test //packages/examples/...
```

```

### File: AGENTS.md
```md
---
trigger: always_on
---

This is the source code for the Angular framework. This guide outlines standard practices for AI agents working in this repository.

## Environment

- Use `pnpm` for package management.
- Use `pnpm bazel test //target` to run tests.

## Key Documentation

- [Building and Testing](contributing-docs/building-and-testing-angular.md): definitive guide for running targets.
- [Coding Standards](contributing-docs/coding-standards.md): style guide for TypeScript and other files.
- [Commit Guidelines](contributing-docs/commit-message-guidelines.md): format for commit messages and PR titles.

## Testing

- **Zoneless & Async-First:** Assume a zoneless environment where state changes schedule updates asynchronously.
  - **Do NOT** use `fixture.detectChanges()` to manually trigger updates.
  - **ALWAYS** use the "Act, Wait, Assert" pattern:
    1. **Act:** Update state or perform an action.
    2. **Wait:** `await fixture.whenStable()` to allow the framework to process the scheduled update.
    3. **Assert:** Verify the output.
- To keep tests fast, minimize the need for waiting:
  - Use `useAutoTick()` (from `packages/private/testing/src/utils.ts`) to fast-forward time via the mock clock.
- When waiting is necessary, use real async tests (`it('...', async () => { ... })`) along with:
  - `await timeout(ms)` (from `packages/private/testing/src/utils.ts`) to wait a specific number of milliseconds.
  - `await fixture.whenStable()` to wait for framework stability.

## Pull Requests

- Use the `gh` CLI (GitHub CLI) for creating and managing pull requests.

```

### File: CODE_OF_CONDUCT.md
```md
# Contributor Covenant Code of Conduct

## Our Pledge

In the interest of fostering a safe and welcoming environment, we as
the Angular team pledge to make participation in our project and
our community a harassment-free experience for everyone, regardless of age, body
size, disability, ethnicity, sex characteristics, gender identity, gender expression,
level of experience, education, socio-economic status, nationality, personal
appearance, race, religion, or sexual identity and orientation.

## Our Standards

Examples of behavior that contributes to creating a positive environment
include:

- Use welcoming and inclusive language
- Respect each other
- Provide and gracefully accept constructive criticism
- Show empathy towards other community members

Examples of unacceptable behavior by participants include:

- Trolling, insulting/derogatory comments, and personal or political attacks
- Public or private harassment
- Publishing others' private information, such as a physical or electronic
  address, without explicit permission
- The use of sexualized language or imagery
- Unwelcome sexual attention or advances
- Other conduct which could reasonably be considered inappropriate in a
  professional setting

## Our Responsibilities

Angular team are responsible for clarifying the standards of acceptable
behavior and are expected to take appropriate and fair corrective action in
response to any instances of unacceptable behavior.

Angular team have the right and responsibility to remove, edit, or
reject comments, commits, code, wiki edits, issues, and other contributions
that are not aligned to this Code of Conduct, and to ban temporarily or
permanently any contributor for other behaviors that they deem inappropriate,
threatening, offensive, or harmful.

## Scope

This Code of Conduct applies to all Angular communication channels - online or in person,
and it also applies when an individual is representing the project or its community in
public spaces. Examples of representing a project or community include using an official
project e-mail address, posting via an official social media account, or acting
as an appointed representative at an online or offline event. Representation of
a project may be further defined and clarified by project maintainers.

## Enforcement

Instances of abusive, harassing, or otherwise unacceptable behavior may be
reported by contacting the Angular team at conduct@angular.io. All
complaints will be reviewed and investigated and will result in a response that
is deemed necessary and appropriate to the circumstances. The Angular team
will maintain confidentiality with regard to the reporter of an incident.
Enforcement may result in an indefinite ban from all official Angular communication
channels, or other actions as deemed appropriate by the Angular team.

Angular maintainers who do not follow or enforce the Code of Conduct in good
faith may face temporary or permanent repercussions as determined by other
members of the project's leadership.

### Appeal

If you are banned you may contest the decision. To do so email conduct@angular.io with the subject line "Repeal Ban for {{your name here}}" and body with the responses to the following:

- Why do you believe you did not violate the Code of Conduct?
- Were other factors involved in this situation the leadership team may have been unaware of?
- Why do you wish to be a part of the Angular community?

## Attribution

This Code of Conduct is adapted from the [Contributor Covenant](https://www.contributor-covenant.org), version 1.4,
available at https://www.contributor-covenant.org/version/1/4/code-of-conduct.html

```

### File: CONTRIBUTING.md
```md
# Contributing to Angular

We would love for you to contribute to Angular and help make it even better than it is today!
As a contributor, here are the guidelines we would like you to follow:

- [Code of Conduct](#coc)
- [Question or Problem?](#question)
- [Issues and Bugs](#issue)
- [Feature Requests](#feature)
- [Submission Guidelines](#submit)
- [Coding Rules](#rules)
- [Commit Message Guidelines](#commit)
- [Signing the CLA](#cla)

## <a name="coc"></a> Code of Conduct

Help us keep Angular open and inclusive.
Please read and follow our [Code of Conduct][coc].

## <a name="question"></a> Got a Question or Problem?

Do not open issues for general support questions as we want to keep GitHub issues for bug reports and feature requests.
Instead, we recommend using [Stack Overflow](https://stackoverflow.com/questions/tagged/angular) to ask support-related questions. When creating a new question on Stack Overflow, make sure to add the `angular` tag.

Stack Overflow is a much better place to ask questions since:

- there are thousands of people willing to help on Stack Overflow
- questions and answers stay available for public viewing so your question/answer might help someone else
- Stack Overflow's voting system assures that the best answers are prominently visible.

To save your and our time, we will systematically close all issues that are requests for general support and redirect people to Stack Overflow.

If you would like to chat about the question in real-time, you can reach out via [the Angular community Discord server][discord].

## <a name="issue"></a> Found a Bug?

If you find a bug in the source code, you can help us by [submitting an issue](#submit-issue) to our [GitHub Repository][github].
Even better, you can [submit a Pull Request](#submit-pr) with a fix.

## <a name="feature"></a> Missing a Feature?

You can _request_ a new feature by [submitting an issue](#submit-issue) to our GitHub Repository.
If you would like to _implement_ a new feature, please consider the size of the change in order to determine the right steps to proceed:

- For a **Major Feature**, first open an issue and outline your proposal so that it can be discussed.
  This process allows us to better coordinate our efforts, prevent duplication of work, and help you to craft the change so that it is successfully accepted into the project.

  **Note**: Adding a new topic to the documentation, or significantly re-writing a topic, counts as a major feature.

- **Small Features** can be crafted and directly [submitted as a Pull Request](#submit-pr).

## <a name="submit"></a> Submission Guidelines

### <a name="submit-issue"></a> Submitting an Issue

Before you submit an issue, please search the issue tracker. An issue for your problem might already exist and the discussion might inform you of workarounds readily available.

We want to fix all the issues as soon as possible, but before fixing a bug, we need to reproduce and confirm it.
In order to reproduce bugs, we require that you provide a minimal reproduction.
Having a minimal reproducible scenario gives us a wealth of important information without going back and forth to you with additional questions.

A minimal reproduction allows us to quickly confirm a bug (or point out a coding problem) as well as confirm that we are fixing the right problem.

We require a minimal reproduction to save maintainers' time and ultimately be able to fix more bugs.
Often, developers find coding problems themselves while preparing a minimal reproduction.
We understand that sometimes it might be hard to extract essential bits of code from a larger codebase, but we really need to isolate the problem before we can fix it.

Unfortunately, we are not able to investigate / fix bugs without a minimal reproduction, so if we don't hear back from you, we are going to close an issue that doesn't have enough info to be reproduced.

You can file new issues by selecting from our [new issue templates](https://github.com/angular/angular/issues/new/choose) and filling out the issue template.

### <a name="pr-quality"></a> Contribution Quality

We strongly value open source contribution and pull requests from community contributors. Please note that every pull request is reviewed and merged by an actual person on the team, which does take time and effort. That is time and effort that does take away from other valuable work. With that in mind we have an minimum set of expectations that are required of any community contribution pull request that is opened.

1. Search [GitHub](https://github.com/angular/angular/pulls) for an open or closed PR that relates to your submission.
   - You don't want to duplicate existing efforts.
2. Be sure that an issue or pull request clearly describes the problem you're fixing, or documents the design for the feature you'd like to add. Issues require a _minimal_ reproduction.

3. Discussing the design in an issue upfront helps to ensure that we're ready to accept your work. Pull requests are not the right place to do design work.
   - When in doubt, open an issue first before doing any sort of speculative implementation work

4. Ideally the PR should be tied to an issue, but this is not required

5. The change should improve code quality (i.e. addressing a TODO) or should impact / improve a feature

6. Micro optimizations will only be accepted if they are validated by an actual benchmark

7. Do not open pull requests that are addressing feature requests that are not labeled as "help wanted" as they usually need additional design work before we could accept pull requests

8. The change should be well tested

If your pull request does not meet these minimum expectations, we may close your PR. Also, if your PR introduces a breaking change, it's possible the level of churn this breaking change causes may block our ability to move forward with it. We may close your PR in that situation, as well. Otherwise, we're excited to see your contributions and enthusiasm for Angular!

### <a name="submit-pr"></a> Submitting a Pull Request (PR)

Before you submit your Pull Request (PR) consider the following guidelines:

1. Please sign our [Contributor License Agreement (CLA)](#cla) before sending PRs.
   We cannot accept code without a signed CLA.
   Make sure you author all contributed Git commits with email address associated with your CLA signature.

2. [Fork](https://docs.github.com/en/github/getting-started-with-github/fork-a-repo) the [angular/angular](https://github.com/angular/angular/fork) repo.

3. In your forked repository, make your changes in a new git branch:

   ```shell
   git checkout -b my-fix-branch main
   ```

4. Create your patch, **including appropriate test cases**.

5. Follow our [Coding Rules](#rules).

6. Run the full Angular test suite, as described in the [developer documentation][dev-doc], and ensure that all tests pass.

7. Commit your changes using a descriptive commit message that follows our [commit message conventions][commit-message-guidelines].
   Adherence to these conventions is necessary because release notes are automatically generated from these messages.

   ```shell
   git commit --all
   ```

   Note: the optional commit `--all` command line option will automatically "add" and "rm" edited files.

8. Push your branch to GitHub:

   ```shell
   git push origin my-fix-branch
   ```

9. In GitHub, send a pull request to `angular:main`.

### Reviewing a Pull Request

The Angular team reserves the right not to accept pull requests from community members who haven't been good citizens of the community. Such behavior includes not following the [Angular code of conduct](https://github.com/angular/code-of-conduct) and applies within or outside of Angular managed channels.

#### Addressing review feedback

If we ask for changes via code reviews then:

1. Make the required updates to the code.

2. Re-run the Angular test suites to ensure tests are still passing.

3. Create a fixup commit and push to your GitHub repository (this will update your Pull Request):

   ```shell
   git commit --all --fixup HEAD
   git push
   ```

   For more info on working with fixup commits see [here](./contributing-docs/using-fixup-commits.md).

That's it! Thank you for your contribution!

##### Updating the commit message

A reviewer might often suggest changes to a commit message (for example, to add more context for a change or adhere to our [commit message guidelines][commit-message-guidelines]).
In order to update the commit message of the last commit on your branch:

1. Check out your branch:

   ```shell
   git checkout my-fix-branch
   ```

2. Amend the last commit and modify the commit message:

   ```shell
   git commit --amend
   ```

3. Push to your GitHub repository:

   ```shell
   git push --force-with-lease
   ```

> NOTE:<br />
> If you need to update the commit message of an earlier commit, you can use `git rebase` in interactive mode.
> See the [git docs](https://git-scm.com/docs/git-rebase#_interactive_mode) for more details.

#### After your pull request is merged

After your pull request is merged, you can safely delete your branch and pull the changes from the main (upstream) repository:

- Delete the remote branch on GitHub either through the GitHub web UI or your local shell as follows:

  ```shell
  git push origin --delete my-fix-branch
  ```

- Check out the main branch:

  ```shell
  git checkout main -f
  ```

- Delete the local branch:

  ```shell
  git branch -D my-fix-branch
  ```

- Update your local `main` with the latest upstream version:

  ```shell
  git pull --ff upstream main
  ```

## <a name="rules"></a> Coding Rules

To ensure consistency throughout the source code, keep these rules in mind as you are working:

- All features or bug fixes **must be tested** by one or more specs (unit-tests).
- All public API methods **must be documented**.
- We follow [Google's TypeScript Style Guide][ts-style-guide], but wrap all code at **100 characters**.

  An automated formatter is available, see [building-and-testing-angular.md](./contributing-docs/building-and-testing-angular.md#formatting-your-source-code).

## <a name="commit"></a> Commit Message Guidelines

We have very precise rules over how our Git commit messages must be formatted:

```
<type>(<scope>): <short summary>
```

See [Commit Message Guidelines][commit-message-guidelines] for details.

## <a name="cla"></a> Signing the CLA

Please sign our Contributor License Agreement (CLA) before sending pull requests. For any code
changes to be accepted, the CLA must be signed. It's a quick process, we promise!

- For individuals, we have a [simple click-through form][individual-cla].
- For corporations, we'll need you to
  [print, sign and one of scan+email, fax or mail the form][corporate-cla].

If you have more than one GitHub accounts, or multiple email addresses associated with a single GitHub account, you must sign the CLA using the primary email address of the GitHub account used to author Git commits and send pull requests.

The following documents can help you sort out issues with GitHub accounts and multiple email addresses:

- https://help.github.com/articles/setting-your-commit-email-address-in-git/
- https://stackoverflow.com/questions/37245303/what-does-usera-committed-with-userb-13-days-ago-on-github-mean
- https://help.github.com/articles/about-commit-email-addresses/
- https://help.github.com/articles/blocking-command-line-pushes-that-expose-your-personal-email-address/

[coc]: https://github.com/angular/code-of-conduct/blob/main/CODE_OF_CONDUCT.md
[corporate-cla]: https://cla.developers.google.com/about/google-corporate
[dev-doc]: ./contributing-docs/building-and-testing-angular.md
[commit-message-guidelines]: ./contributing-docs/commit-message-guidelines.md
[github]: https://github.com/angular/angular
[discord]: https://discord.gg/angular
[individual-cla]: https://cla.developers.google.com/about/google-individual
[ts-style-guide]: https://google.github.io/styleguide/tsguide.html

```

### File: SECURITY.md
```md
Angular is part of Google [Open Source Software Vulnerability Reward Program](https://bughunters.google.com/about/rules/6521337925468160/google-open-source-software-vulnerability-reward-program-rules). For vulnerabilities in Angular, please submit your report [here](https://bughunters.google.com/report).

For more information, check out [Angular's security policy](https://angular.dev/best-practices/security).

```

### File: VETTING_REPORT.md
```md
---
title: Auto Vetting Report for angular
date: 2026-04-05
analyst: civ_vetting_pipeline
status: AUTO_VETTED
---

# Auto-Vetted Repository
This repository was automatically swept and vetted by the batch processor. Only documentation remains.

```

### File: .github\ISSUE_TEMPLATE.md
```md
Please help us process issues more efficiently by filing an
issue using one of the following templates:

https://github.com/angular/angular/issues/new/choose

Thank you!

```

### File: .github\PULL_REQUEST_TEMPLATE.md
```md
## PR Checklist

Please check if your PR fulfills the following requirements:

- [ ] The commit message follows our guidelines: https://github.com/angular/angular/blob/main/contributing-docs/commit-message-guidelines.md
- [ ] Tests for the changes have been added (for bug fixes / features)
- [ ] Docs have been added / updated (for bug fixes / features)

## PR Type

What kind of change does this PR introduce?

<!-- Please check the one that applies to this PR using "x". -->

- [ ] Bugfix
- [ ] Feature
- [ ] Code style update (formatting, local variables)
- [ ] Refactoring (no functional changes, no api changes)
- [ ] Build related changes
- [ ] CI related changes
- [ ] Documentation content changes
- [ ] angular.dev application / infrastructure changes
- [ ] Other... Please describe:

## What is the current behavior?

<!-- Please describe the current behavior that you are modifying, or link to a relevant issue. -->

Issue Number: N/A

## What is the new behavior?

## Does this PR introduce a breaking change?

- [ ] Yes
- [ ] No

<!-- If this PR contains a breaking change, please describe the impact and migration path for existing applications below. -->

## Other information

```

### File: packages\license-banner.txt
```txt
/**
 * @license Angular v0.0.0-PLACEHOLDER
 * (c) 2010-2026 Google LLC. https://angular.dev/
 * License: MIT
 */

```

### File: .agent\rules\agents.md
```md
../../AGENTS.md
```

### File: .agent\skills\adev-writing-guide\SKILL.md
```md
---
name: adev-writing-guide
description: Comprehensive writing guide for Angular documentation (adev). Covers Google Technical Writing standards, Angular-specific markdown extensions, code blocks, and components. Use when authoring or reviewing content in adev/src/content.
---

# Angular Documentation (adev) Writing Guide

This skill provides comprehensive guidelines for authoring content in `adev/src/content`. It combines Google's technical writing standards with Angular-specific markdown conventions, components, and best practices.

## I. Google Technical Writing Guidelines

### Tone and Content

- **Be conversational and friendly:** Maintain a helpful yet professional tone. Avoid being overly casual.
- **Write accessibly:** Ensure documentation is understandable to a diverse global audience, including non-native English speakers.
- **Audience-first:** Focus on what the user needs to do, not just what the system does.
- **Avoid pre-announcing:** Do not mention unreleased features or make unsupported claims.
- **Use descriptive link text:** Link text should clearly indicate the destination (e.g., avoid "click here").

### Language and Grammar

- **Use second person ("you"):** Address the reader directly.
- **Prefer active voice:** Clearly state who or what is performing the action (e.g., "The system generates a token" vs "A token is generated").
- **Standard American English:** Use standard American spelling and punctuation.
- **Conditional clauses first:** Place "if" or "when" clauses before the instruction (e.g., "If you encounter an error, check the logs").
- **Define terms:** Introduce new or unfamiliar terms/acronyms upon first use.
- **Consistent terminology:** Use the same term for the same concept throughout the document.
- **Conciseness:** Aim for one idea per sentence. Keep sentences short.

### Formatting and Organization

- **Sentence case for headings:** Capitalize only the first word and proper nouns in titles and headings.
- **Lists:**
  - **Numbered lists:** Use for sequential steps or prioritized items.
  - **Bulleted lists:** Use for unordered collections of items.
  - **Description lists:** Use for term-definition pairs.
- **Serial commas:** Use the Oxford comma (comma before the last item in a list of three or more).
- **Code formatting:** Use code font for code-related text (filenames, variables, commands).
- **UI Elements:** formatting user interface elements in **bold**.
- **Date formatting:** Use unambiguous formats (e.g., "September 4, 2024" rather than "9/4/2024").
- **Structure:** Use logical hierarchy with clear introductions and navigation. Headings should be task-based where possible.

### Images and Code Samples

- **Images:** Use simple, clear illustrations to enhance understanding.
- **Captions:** Write captions that support the image.
- **Code Samples:**
  - Ensure code is correct and builds without errors.
  - Follow language-specific conventions.
  - **Comments:** Focus on _why_, not _what_. Avoid commenting on obvious code.

### Reference Hierarchy

1.  Project-specific style guidelines (if any exist in `CONTRIBUTING.md` or similar).
2.  Google Developer Documentation Style Guide.
3.  Merriam-Webster (spelling).
4.  Chicago Manual of Style (non-technical).
5.  Microsoft Writing Style Guide (technical).

---

## II. Angular Documentation Specifics

### Code Blocks

Use the appropriate language identifier for syntax highlighting:

- **TypeScript (Angular):** Use `angular-ts` when TypeScript code examples contain inline templates.
- **HTML (Angular):** Use `angular-html` for Angular templates.
- **TypeScript (Generic):** Use `ts` for plain TypeScript.
- **HTML (Generic):** Use `html` for plain HTML.
- **Shell/Terminal:** Use `shell` or `bash`.
- **Mermaid Diagrams:** Use `mermaid`.

#### Attributes

You can enhance code blocks with attributes in curly braces `{}` after the language identifier:

- `header="Title"`: Adds a title to the code block.
- `linenums`: Enables line numbering.
- `highlight="[1, 3-5]"`: Highlights specific lines.
- `hideCopy`: Hides the copy button.
- `prefer`: Marks code as a preferred example (green border/check).
- `avoid`: Marks code as an example to avoid (red border/cross).

**Example:**

````markdown
```angular-ts {header:"My Component", linenums, highlight="[2]"}
@Component({
  selector: 'my-app',
  template: '<h1>Hello</h1>',
})
export class App {}
```
````

#### `<docs-code>` Component

For more advanced code block features, use the `<docs-code>` component:

- `path`: Path to a source file (e.g., `adev/src/content/examples/...`).
- `header`: Custom header text.
- `language`: Language identifier (e.g., `angular-ts`).
- `linenums`: Boolean attribute.
- `highlight`: Array of line numbers/ranges (e.g., `[[3,7], 9]`).
- `diff`: Path to diff file.
- `visibleLines`: Range of lines to show initially (collapsible).
- `region`: Region to extract from source file.
- `preview`: Boolean. Renders a live preview (StackBlitz). _Only works with standalone examples._
- `hideCode`: Boolean. Collapses code by default.

**Multifile Example:**

```html
<docs-code-multifile path="..." preview>
  <docs-code path="..." />
  <docs-code path="..." />
</docs-code-multifile>
```

### Alerts / Admonitions

Use specific keywords followed by a colon for alerts. These render as styled blocks.

- `NOTE:` For ancillary information.
- `TIP:` For helpful hints or shortcuts.
- `IMPORTANT:` For crucial information.
- `CRITICAL:` For warnings about potential data loss or severe issues.
- `TODO`: For incomplete documentation.
- `QUESTION:` To pose a question to the reader.
- `SUMMARY:` For section summaries.
- `TLDR:` For concise summaries.
- `HELPFUL:` For best practices.

**Example:**

```markdown
TIP: Use `ng serve` to run your application locally.
```

### Custom Components

- **Cards (`<docs-card>`):**
  - Must be inside `<docs-card-container>`.
  - Attributes: `title`, `link`, `href`.
- **Callouts (`<docs-callout>`):**
  - Attributes: `title`, `important`, `critical`.
- **Pills (`<docs-pill>`):**
  - Must be inside `<docs-pill-row>`.
  - Attributes: `title`, `href`.
- **Steps / Workflow (`<docs-step>`):**
  - Must be inside `<docs-workflow>`.
  - Attributes: `title`.
- **Tabs (`<docs-tab>`):**
  - Must be inside `<docs-tab-group>`.
  - Attributes: `label`.
- **Videos (`<docs-video>`):**
  - Attributes: `src` (YouTube embed URL), `alt`.

### Images

Use standard markdown syntax with optional attributes for sizing and loading behavior.

- `#small`, `#medium`: Append to image URL for sizing.
- `{loading: 'lazy'}`: Add attribute for lazy loading.

**Example:**

```markdown
![Alt Text](path/to/image.png#medium {loading: 'lazy'})
```

### Headers

- Use markdown headers (`#`, `##`, `###`).
- Ensure a logical hierarchy (don't skip levels).
- `h2` and `h3` are most common for content structure.

```

### File: .agent\skills\pr_review\SKILL.md
```md
---
name: PR Review
description: Guidelines and tools for reviewing pull requests in the Angular repository.
---

# PR Review Guidelines

When reviewing a pull request for the `angular` repository, follow these essential guidelines to ensure high-quality contributions:

1. **Context & Ecosystem**:
   - Keep in mind that this is the core Angular framework. Changes here can impact millions of developers.
   - Be mindful of backwards compatibility. Breaking changes require strict approval processes and deprecation periods.

2. **Key Focus Areas**:
   - **Comprehensive Reviews**: You **MUST always** perform a deep, comprehensive review of the _entire_ pull request. If the user asks you to look into a specific issue, file, or area of concern, you must investigate that specific area _in addition to_ reviewing the rest of the PR's substantive changes. Do not terminate your review after addressing only the user's focal point.
   - **Package-Specific Guidelines**: Check if there are specific guidelines for the package being modified in the `reference/` directory (e.g., `reference/router.md`). Always prioritize these rules for their respective packages.
   - **Commit Messages**: Evaluate the quality of commit messages. They should explain the _why_ behind the change, not just the _what_. Someone should be able to look at the commit history years from now and clearly understand the context and reasoning for the change.
   - **Code Cleanliness**: Ensure the code is readable, maintainable, and follows Angular's project standards.
   - **Performance**: Look out for code that might negatively impact runtime performance or bundle size, particularly in hot paths like change detection or rendering.
   - **Testing**: Ensure all new logic has comprehensive tests, including edge cases. **Do NOT run tests locally** as part of your review process. CI handles this automatically, and running tests locally is redundant and inefficient.
   - **API Design**: Ensure new public APIs are well-designed, consistent with existing APIs, and properly documented.
   - **Payload Size**: Pay attention to the impact of changes on the final client payload size.

3. **Execution Workflow**:
   Determine the appropriate review method. If the user explicitly asks for a `remote` or `local` review in their request, that takes precedence (e.g. "leave comments on the PR" implies `remote`). Otherwise, use the GitHub MCP or available scripts to determine if the review should be `local` or `remote`.

   **Common Review Practices (Applies to both Local and Remote)**
   - **Preparation & Checklist**:
     - First, create a task list (e.g., in `task.md`) that you can easily reference containing **all** the review requirements from the "Key Focus Areas" section (Commit Messages, Performance, Testing, etc.), along with any specific review notes or requests from the user.
     - Before doing an in-depth review, expand this list into more detailed items of what you plan to explore and verify in the PR.
     - As you conduct the review, check off items in this list, adding your assessment or findings underneath each item.
     - At the end of your review, refer back to the checklist to ensure every single requirement was completely verified.
   - **Fetch PR Metadata Safely**: When you need to read the PR description or context, do NOT use `gh pr view <PR_NUMBER>` by itself, as its default GraphQL query may fail due to lack of `read:org` and `read:discussion` token scopes. Instead, use `read_url_content` on the PR URL or use `gh pr view <PR_NUMBER> --json title,body,state,author`.
   - **Check Existing Comments First**: Before formulating feedback, use the GitHub MCP or available scripts to fetch existing comments on the PR. Review this feedback to avoid duplicate comments, and incorporate its insights into your own review process.
   - **Constructive Feedback**: Provide clear, actionable, and polite feedback. Explain the _why_ behind your suggestions or edits. Do **NOT** leave inline comments purely to praise, agree with, or acknowledge a correct implementation detail, as this clutters the review. If you want to praise the PR, do so in the single general PR comment.

   **A. Local Code Review (If the PR is owned by the author requesting the review)**
   - **Checkout**: Check out the PR branch locally (if it doesn't already exist, fetch it). If checking out the branch fails due to a worktree claim (e.g. "fatal: '<branch>' is already used by worktree at '<path>'"), do the review in that directory.
   - **Review & Edit**: Execute the review directly on the code. Instead of adding inline PR comments for suggestions, format the codebase or apply the edits directly to the files.
   - **Feedback**: Summarize the review findings and the concrete changes you made in a message to the user, referencing the completed items from your checklist.
   - **Do NOT Commit or Push**: Leave the changes uncommitted in the working directory so the user can easily review the pending edits locally. Let the user know the changes are ready for their review, but do not ask for approval to push.
   - **Resolve Comments**: Once the user confirms the changes are good and should be committed/pushed, respond to the existing comments as 'resolved' using the GitHub MCP or available scripts.

   **B. Remote Code Review (For all other PRs)**
   - **Batching Comments (MCP Server - Preferred)**: If you have the GitHub MCP Server configured, you **MUST** follow this workflow to avoid spamming the author with multiple notifications:
     1. Create a pending review using `mcp_github-mcp-server_pull_request_review_write` (method `create`).
     2. Add your inline comments to the pending review using `mcp_github-mcp-server_add_comment_to_pending_review`.
     3. Submit the review using `mcp_github-mcp-server_pull_request_review_write` (method `submit_pending`).
   - **Batching Comments (Scripts - Fallback)**: If you do **NOT** have access to the GitHub MCP Server (e.g., specific MCP tools are missing from your context), fallback to using the provided scripts. Use `post_inline_comment.sh` to stage your comments locally. Once all comments are staged, you **MUST** call `submit_pr_review.sh` to publish them as a single batched review (and send a single notification). Try to keep comments minimal or use a general comment if you have many suggestions.
   - **Use Suggested Changes**: Whenever appropriate (e.g., for simple code fixes, refactoring suggestions, or typo corrections), prefer using GitHub's **Suggested Changes** syntax (`suggestion ... `) in your inline comments. This allows the author to apply your suggested code improvements with a single click in the GitHub UI.
   - **Review Type**: Never mark an external PR review as an "approval" unless explicitly instructed by a repo maintainer. Always use "Request Changes" or "Comment". Note that some tools might only support commenting.
   - **Require User Approval Before Posting**: Prepare your review comments and present them to the user, alongside a summary of your completed checklist. Do NOT post comments to the PR without explicitly asking the user for permission first. Only post the review after the user approves.
   - **Prefix Agent Comments**: To make it clear when comments are generated and posted by an AI agent rather than a human user, **always** prefix your review comments with `AGENT: `.

## Available Tools

The following tools are available for remote interactions. We prefer using standard **GitHub MCP Server** tools when available. If you do not have the MCP server set up, you **MUST** fallback to using the custom bash scripts.

### GitHub MCP Tools (Preferred)

- `mcp_github-mcp-server_pull_request_review_write`
- `mcp_github-mcp-server_add_comment_to_pending_review`

### Custom Bash Scripts (Fallback)

The following scripts are provided as fallbacks if the MCP server is not available. Note that they rely on the `gh` CLI being correctly installed and authenticated in the local environment.

### `determine_review_type.sh`

Determines whether to use the Local or Remote review workflow by checking if the currently authenticated GitHub user via the `gh` CLI matches the author of the pull request.

**Usage:**

```bash
.agent/skills/pr_review/scripts/determine_review_type.sh <PR_NUMBER>
```

### `get_pr_comments.sh`

Fetches all existing inline comments on a PR using the GitHub API. This is crucial for reviewing other contributors' feedback and avoiding duplicate comments. It outputs JSON containing the `id`, `path`, `line`, `body`, and `user` for each comment.

**Usage:**

```bash
.agent/skills/pr_review/scripts/get_pr_comments.sh <PR_NUMBER>
```

### `reply_pr_comment.sh`

Replies to an existing PR comment thread. This is useful for marking comments as resolved after addressing them in a local code review. Note that the `COMMENT_ID` must be the ID of the top-level comment in the thread.

**Usage:**

```bash
.agent/skills/pr_review/scripts/reply_pr_comment.sh <PR_NUMBER> <COMMENT_ID> <REPLY_BODY>
```

### `post_inline_comment.sh`

The GitHub CLI `gh pr review` command does not natively support adding inline comments to specific lines of code via its standard flags. This script wraps the GitHub API to stage comments locally. They will not be published until you call `submit_pr_review.sh`.

**Usage:**

```bash
.agent/skills/pr_review/scripts/post_inline_comment.sh <PR_NUMBER> <FILE_PATH> <LINE_NUMBER> <COMMENT_BODY>
```

**Example:**

```bash
.agent/skills/pr_review/scripts/post_inline_comment.sh 12345 "packages/core/src/render3/instructions/element.ts" 42 "AGENT: Consider the performance implications here."
```

### `submit_pr_review.sh`

Submits all locally staged inline comments as a single batched review via the GitHub Pull Request Reviews API.

**Usage:**

```bash
.agent/skills/pr_review/scripts/submit_pr_review.sh <PR_NUMBER> <EVENT_TYPE> [BODY]
```

**Options:**

- `EVENT_TYPE`: Must be `COMMENT`, `APPROVE`, or `REQUEST_CHANGES`. Never use `APPROVE` for external PRs.
- `BODY`: (Optional) A general summary comment for the review.

**Example:**

```bash
.agent/skills/pr_review/scripts/submit_pr_review.sh 12345 COMMENT "AGENT: I have left a few inline suggestions for your consideration."
```

```

### File: .agent\skills\reference-compiler-cli\SKILL.md
```md
---
name: reference-compiler-cli
description: Explains the mental model and architecture of the code under `packages/compiler-cli`. You MUST use this skill any time you plan to work with code in `packages/compiler-cli`
---

# Angular Compiler CLI (`ngtsc`) Architecture

## Overview

The `packages/compiler-cli` package contains the Angular Compiler (Ivy), often referred to as `ngtsc`. It is a wrapper around the TypeScript compiler (`tsc`) that extends it with Angular-specific capabilities.

The core goal of `ngtsc` is to compile Angular decorators (like `@Component`, `@Directive`, `@Pipe`) into static properties on the class (Ivy instructions, e.g., `static ɵcmp = ...`). It also performs template type checking and ahead-of-time (AOT) compilation.

## Mental Model

The compiler is designed as a **lazy, incremental, and partial** compilation pipeline.

1.  **Wrapper Pattern**: `NgtscProgram` wraps the standard `ts.Program`. It intercepts calls to act as a drop-in replacement for standard tooling.
2.  **Traits System**: Every class with an Angular decorator is considered a "Trait". The compiler manages the state of these traits through a state machine:
    - **Pending**: Detected but not processed.
    - **Analyzed**: Metadata extracted, template parsed (but dependencies not yet linked).
    - **Resolved**: Dependencies (directives/pipes in template) resolved, import cycles handled.
    - **Skipped**: Not an Angular class.
3.  **Lazy Analysis**: Analysis only happens when necessary (e.g., when diagnostics are requested or emit is prepared).
4.  **Output AST**: The compiler generates an intermediate "Output AST" (`o.Expression`) for the generated code, which is then translated into TypeScript AST nodes during the emit phase.

## Key Subsystems

### 1. Core Orchestration (`ngtsc/core`)

- **`NgtscProgram`**: The public API implementing `api.Program`. It manages the `ts.Program` and the `NgCompiler`.
- **`NgCompiler`**: The brain of the compiler. It orchestrates the compilation phases (Analysis, Resolution, Type Checking, Emit). It holds the `TraitCompiler`.

### 2. Trait Compilation (`ngtsc/transform`)

- **`TraitCompiler`**: Manages the lifecycle of "Traits". It iterates over source files, identifies decorated classes, and delegates to the appropriate `DecoratorHandler`.
- **`Trait`**: A state container for a class, holding its handler, analysis results, and resolution results.

### 3. Decorator Handlers (`ngtsc/annotations`)

- **`DecoratorHandler`**: An interface for handling specific decorators.
- **`ComponentDecoratorHandler`**: The most complex handler. It:
  - Extracts metadata (selector, inputs, outputs).
  - Parses the template.
  - Resolves used directives and pipes (`R3TargetBinder`).
  - Generates the `ɵcmp` instruction.
- **`DirectiveDecoratorHandler`**, **`PipeDecoratorHandler`**, **`NgModuleDecoratorHandler`**: Handle their respective decorators.

### 4. Template Type Checking (`ngtsc/typecheck`)

- **`TemplateTypeChecker`**: Generates "Type Check Blocks" (TCBs). A TCB is a block of TypeScript code that represents the template's logic in a way `tsc` can understand and check for errors.
- **`TypeCheckBlock`**: The actual generated code that validates bindings, events, and structural directives.

### 5. Metadata & Scope (`ngtsc/metadata`, `ngtsc/scope`)

- **`MetadataReader`**: Reads Angular metadata from source files (using `LocalMetadataRegistry`) and `.d.ts` files (using `DtsMetadataReader`).
- **`ScopeRegistry`**: Determines the "compilation scope" of a component (which directives/pipes are available to it), handling `NgModule` transitive exports and Standalone Component imports.

### 6. Emit & Transformation (`ngtsc/transform`)

- **`ivyTransformFactory`**: A TypeScript transformer factory.
- **`IvyCompilationVisitor`**: Visits classes, triggers compilation via `TraitCompiler`, and collects the Output AST.
- **`IvyTransformationVisitor`**: Translates the Output AST into TypeScript AST, injects the `static ɵ...` fields, and removes the original decorators.

## Compilation Phases

1.  **Construction**: `NgtscProgram` creates `NgCompiler`, which sets up all registries and the `TraitCompiler`.
2.  **Analysis** (`analyzeSync`):
    - The `TraitCompiler` scans files.
    - `DecoratorHandler`s extract metadata and parse templates.
    - No cross-file resolution happens here (allowing for parallelism and caching).
3.  **Resolution** (`resolve`):
    - `TraitCompiler` resolves traits.
    - Components link their templates to specific Directives and Pipes (found via `ScopeRegistry`).
    - Import cycles are detected and handled (e.g., via "remote scoping").
4.  **Type Checking**:
    - `TemplateTypeChecker` creates TCBs for all components.
    - TypeScript diagnostics are retrieved for these TCBs.
5.  **Emit** (`prepareEmit`):
    - `ivyTransformFactory` is created.
    - TS `emit` is called.
    - The transformers run, injecting the compiled Ivy instructions into the JS/DTS output.

## Important File Locations

- `packages/compiler-cli/src/ngtsc/program.ts`: Entry point (`NgtscProgram`).
- `packages/compiler-cli/src/ngtsc/core/src/compiler.ts`: Core logic (`NgCompiler`).
- `packages/compiler-cli/src/ngtsc/transform/src/trait.ts`: Trait state machine.
- `packages/compiler-cli/src/ngtsc/annotations/component/src/handler.ts`: Component compilation logic.
- `packages/compiler-cli/src/ngtsc/typecheck/src/template_type_checker.ts`: Type checking logic.
- `packages/compiler-cli/src/ngtsc/transform/src/transform.ts`: AST transformation logic.

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.

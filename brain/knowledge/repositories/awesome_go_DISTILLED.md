---
id: repo-fetched-awesome-go-133747
type: knowledge
owner: OA
registered_at: 2026-04-05T03:43:49.194832
tags: ["auto-cloned", "oa-assimilated"]
---

# FETCHED_awesome-go_133747

## Assimilation Report
Auto-cloned repository: FETCHED_awesome-go_133747

## Application for OmniClaw
No structural integration blueprint provided.

## SWALLOW ENGINE DISTILLATION

### File: AGENTS.md
```md
# awesome-go · LLM Contribution Guide

This document summarizes the project context and the conventions that language models must follow when helping on this repository.

## Project Snapshot

- Purpose: maintain the curated `README.md` list of Go resources and generate the static site via `go run .`.
- Primary language: Go 1.23 (see `go.mod`). Supporting JavaScript exists only for the GitHub Action in `.github/scripts`.
- Key entry points:
  - `main.go`: reads `README.md`, builds category pages, and writes artifacts to `out/` using templates in `tmpl/`.
  - `pkg/markdown` and `pkg/slug`: helper packages used by the generator.
  - `.github/workflows/`: CI pipelines for PR quality validation, stale checks, site deployment, and Go tests.

## When Modifying the Awesome List

- Read and respect `CONTRIBUTING.md` (alphabetical order, one item per PR, descriptions end with a period, etc.).
- Keep categories with at least three entries and verify surrounding entries still meet quality standards.
- Avoid promotional copy; descriptions must stay concise and neutral.
- Do not drop existing content unless removal is requested and justified.

## Coding Guidelines

- Go:
  - Use standard formatting (`gofmt`) and idiomatic Go style.
  - Favor small, testable functions; keep exported APIs documented with Go-style comments.
  - Maintain ≥80% coverage for non-data packages and ≥90% for data packages when adding new testable code.
- JavaScript (GitHub Action script):
  - Keep Node 20 compatibility.
  - Uphold strict mode and existing patterns (async helpers, early returns, descriptive errors).
- Generated site output is not committed; do not add files under `out/`.

## Testing & Validation

- Preferred commands before submitting Go changes:
  - `go test ./...`
  - `go test -run ^TestStaleRepository$` (mirrors the scheduled workflow focus).
- For list-only modifications, run linting/formatting on touched files if tools are configured locally.
- The `PR Quality Checks` workflow will run `.github/scripts/check-quality.js`; ensure referenced links in PR bodies are reachable.

## CI Overview

- `tests.yaml`: runs `go test main_test.go main.go` on pushes/PRs.
- `pr-quality-check.yaml`: validates PR metadata (forge link, pkg.go.dev, Go Report Card, coverage).
- `run-check.yaml`: scheduled stale repository audit via `go test -run ^TestStaleRepository$`.
- `site-deploy.yaml`: builds and deploys the static site to Netlify on `main` pushes.

## Documentation & Housekeeping

- Update this `AGENTS.md` whenever repository conventions change.
- Keep documentation in English; follow American English spelling for code and comments.
- Remove unused files/modules when confirmed obsolete.
- Align rendered documentation (`README.md`, `COVERAGE.md`, etc.) with any behavior changes made to `main.go` or helper packages.

```

### File: CODE_OF_CONDUCT.md
```md
# Code of Conduct

## 1. Purpose

A primary goal of Awesome Go is to be inclusive to the largest number of contributors, with the most varied and diverse backgrounds possible. As such, we are committed to providing a friendly, safe and welcoming environment for all, regardless of gender, sexual orientation, ability, ethnicity, socioeconomic status, and religion (or lack thereof).

This code of conduct outlines our expectations for all those who participate in our community, as well as the consequences for unacceptable behavior.

We invite all those who participate in Awesome Go to help us create safe and positive experiences for everyone.

## 2. Open Source Citizenship

A supplemental goal of this Code of Conduct is to increase open source citizenship by encouraging participants to recognize and strengthen the relationships between our actions and their effects on our community.

Communities mirror the societies in which they exist, and positive action is essential to counteract the many forms of inequality and abuses of power that exist in society.

If you see someone who is making an extra effort to ensure our community is welcoming, friendly, and encourages all participants to contribute to the fullest extent, we want to know.

## 3. Expected Behavior

The following behaviors are expected and requested of all community members:

* Participate in an authentic and active way. In doing so, you contribute to the health and longevity of this community.
* Exercise consideration and respect in your speech and actions.
* Attempt collaboration before conflict.
* Refrain from demeaning, discriminatory, or harassing behavior and speech.
* Be mindful of your surroundings and of your fellow participants. Alert community leaders if you notice a dangerous situation, someone distressed, or violations of this Code of Conduct, even if they seem inconsequential.
* Remember that community event venues may be shared with members of the public; please be respectful to all patrons of these locations.

## 4. Unacceptable Behavior

The following behaviors are considered harassment and are unacceptable within our community:

* Violence, threats of violence or violent language directed against another person.
* Sexist, racist, homophobic, transphobic, ableist or otherwise discriminatory jokes and language.
* Posting or displaying sexually explicit or violent material.
* Posting or threatening to post other people’s personally identifying information ("doxing").
* Personal insults, particularly those related to gender, sexual orientation, race, religion, or disability.
* Inappropriate photography or recording.
* Inappropriate physical contact. You should have someone’s consent before touching them.
* Unwelcome sexual attention. This includes, sexualized comments or jokes; inappropriate touching, groping, and unwelcomed sexual advances.
* Deliberate intimidation, stalking or following (online or in person).
* Advocating for, or encouraging, any of the above behavior.
* Sustained disruption of community events, including talks and presentations.

## 5. Consequences of Unacceptable Behavior

Unacceptable behavior from any community member, including sponsors and those with decision-making authority, will not be tolerated.

Anyone asked to stop unacceptable behavior is expected to comply immediately.

If a community member engages in unacceptable behavior, the community organizers may take any action they deem appropriate, up to and including a temporary ban or permanent expulsion from the community unexpected (and without refund in the case of a paid event).

## 6. Reporting Guidelines

If you are subject to or witness unacceptable behavior, or have any other concerns, please notify a community organizer as soon as possible.

[Reporting Guidelines](https://github.com/avelino/awesome-go/blob/main/CONTRIBUTING.md#contribution-guidelines)

Additionally, community organizers are available to help community members engage with local law enforcement or to otherwise help those experiencing unacceptable behavior feel safe. In the context of in-person events, organizers will also provide escorts as desired by the person experiencing distress.

## 7. Addressing Grievances

If you feel you have been falsely or unfairly accused of violating this Code of Conduct, you should notify Avelino with a concise description of your grievance. Your grievance will be handled in accordance with our existing governing policies.

[Policy](https://github.com/avelino/awesome-go/blob/main/CONTRIBUTING.md)

## 8. Scope

We expect all community participants (contributors, paid or otherwise; sponsors; and other guests) to abide by this Code of Conduct in all community venues–online and in-person–as well as in all one-on-one communications pertaining to community business.

This code of conduct and its related procedures also applies to unacceptable behavior occurring outside the scope of community activities when such behavior has the potential to adversely affect the safety and well-being of community members.

## 9. Contact info

avelinorun AT gmail DOT com

## 10. License and attribution

This Code of Conduct is distributed under a [Creative Commons Attribution-ShareAlike license](http://creativecommons.org/licenses/by-sa/3.0/).

Portions of text derived from the [Django Code of Conduct](https://www.djangoproject.com/conduct/) and the [Geek Feminism Anti-Harassment Policy](http://geekfeminism.wikia.com/wiki/Conference_anti-harassment/Policy).

Retrieved on November 22, 2016

```

### File: CONTRIBUTING.md
```md
# Contribution Guidelines

This resource was made by the Go community and wouldn't be possible without you!
We appreciate and recognize [all contributors](https://github.com/avelino/awesome-go/graphs/contributors).

> Please be aware that we want to accept your contribution, but we have **some rules to keep the minimum quality** of the packages listed here. All reviews are **not personal feedback**, even if you are a _developer reviewing your contribution_. **Sorry, if we can't meet your expectations; we do our best**.

- **To add, remove, or change things on the list:** Submit a pull request

## Table of Contents

- [Quick checklist](#quick-checklist)
- [Quality standards](#quality-standards)
- [What is checked automatically](#what-is-checked-automatically)
- [Preparing for review](#preparing-for-review)
- [How to add an item to the list](#how-to-add-an-item-to-the-list)
  - [Entry formatting rules](#entry-formatting-rules)
  - [PR body example](#pr-body-example)
- [Congrats, your project got accepted - what now](#congrats-your-project-got-accepted---what-now)
- [Maintenance expectations for projects listed here](#maintenance-expectations-for-projects-listed-here)
- [How to remove an item from the list](#how-to-remove-an-item-from-the-list)
- [Maintainers](#maintainers)
- [Reporting issues](#reporting-issues)
- [How decisions are made](#how-decisions-are-made)
- [How to become a contributor](#how-to-become-a-contributor)
- [How to become an ~~"official maintainer"~~](#how-to-become-an-official-maintainer)

## Quick checklist

Before opening a pull request, ensure the following:

- [ ] One PR adds, removes, or changes **only one item**.
- [ ] The item is in the **correct category** and in **alphabetical order**.
- [ ] The link text is the **exact project/package name**.
- [ ] The description is **concise, non-promotional, and ends with a period**.
- [ ] The repository has: at least **5 months of history**, an **open source license**, a `go.mod`, and at least one **SemVer release** (`vX.Y.Z`).
- [ ] Documentation in English: **README** and **pkg.go.dev doc comments** for public APIs.
- [ ] Tests meet the coverage guideline (**≥80%** for non-data packages, **≥90%** for data packages) when applicable.
- [ ] Include links in the PR body to **pkg.go.dev**, **Go Report Card**, and a **coverage report**.
- [ ] For ongoing development: issues and PRs are responded to within ~2 weeks; or, if the project is mature/stable, there are no bug reports older than 6 months.

To set this list apart from and complement the excellent [Go wiki Projects page](https://go.dev/wiki/Projects),
and other lists, awesome-go is a specially curated list of high-quality, actively maintained Go packages and resources.

Please contribute links to packages/projects you have used or are familiar with. This will help ensure high-quality entries.

> the maintainers do not work full-time on the project, meaning that we do not have a set periodicity for reviewing contributions - rest assured that we will do our best to review and eventually accept contributions

## Quality standards

To be on the list, project repositories should adhere to the following quality standards.
(<https://goreportcard.com/report/github.com/> **github_user** / **github_repo**):

- have at least 5 months of history since the first commit.
- have an **open source license**, [see list of allowed licenses](https://opensource.org/licenses/alphabetical);
- function as documented and expected;
- be generally useful to the wider community of Go programmers;
- be actively maintained with:
  - regular, recent commits;
  - or, for finished projects, issues and pull requests are responded to generally within 2 weeks;
- be stable or progressing toward stable;
- be thoroughly documented (README, pkg.go.dev doc comments, etc.) in the English language, so everyone is able to understand the project's intention and how it works. All public functions and types should have a Go-style documentation header;
- if the library/program is testable, then coverage should be >= 80% for non-data-related packages and >=90% for data-related packages. (**Note**: the tests will be reviewed too. We will check your coverage manually if your package's coverage is just a benchmark result);
- have at least one official version-numbered release that allows go.mod files to list the file by version number of the form vX.X.X.

Categories must have at least 3 items.

## What is checked automatically

When you open a PR, the following checks run automatically via CI. Fixing these before submitting saves review time.

### Blocking checks (PR cannot be merged if these fail)

| Check | What it validates |
|-------|-------------------|
| **Repo accessible** | Repository URL responds and is not archived |
| **go.mod present** | `go.mod` exists at the repository root |
| **SemVer release** | At least one tag matching `vX.Y.Z` exists |
| **pkg.go.dev reachable** | The provided pkg.go.dev link loads |
| **Go Report Card grade** | Grade is A-, A, or A+ |
| **PR body links present** | Forge link, pkg.go.dev, and Go Report Card are provided |
| **Single item per PR** | Only one package added or removed per PR |
| **Link consistency** | URL added to README matches the forge link in the PR body |
| **Description format** | Entry ends with a period |
| **Alphabetical order** | Entry is in the correct alphabetical position |
| **No duplicate links** | URL is not already in the list |
| **Entry format** | Matches `- [name](url) - Description.` pattern |
| **Category minimum** | Category has at least 3 items |

### Non-blocking checks (reported as warnings)

| Check | What it validates |
|-------|-------------------|
| **Open source license** | GitHub detects a recognized OSS license |
| **Repository maturity** | First commit is at least 5 months old |
| **CI/CD configured** | GitHub Actions workflows are present |
| **README present** | Repository has a README file |
| **Coverage link** | A Codecov or Coveralls link is provided and reachable |
| **Link text** | Link text matches the repository name |
| **Non-promotional** | Description avoids superlative/marketing language |
| **Extra files** | Only README.md is modified (for package additions) |

### Still reviewed manually by maintainers

- Package is in the **correct category** for its functionality
- Package is **generally useful** to the Go community
- Description is **accurate and clear**
- Test coverage is **real** (not just benchmarks)
- Documentation quality (README detail, pkg.go.dev comments)
- Package **functions as documented**
- For surrounding packages: still meet quality standards

## Preparing for review

Projects listed must have the following in their documentation. When submitting, you will be asked
to provide them.

- A link to the project's pkg.go.dev page
- A link to the project's Go Report Card report
- A link to a code coverage report

One way to accomplish the above is to add badges to your project's README file.

- Use <https://pkg.go.dev/badge/> to create the pkg.go.dev link.
- Go to <https://goreportcard.com/> to generate a Go Report Card report, then click on the report badge in the upper-right corner to see details on how to add the badge to your README.
- Codecov, coveralls, and gocover all offer ways to create badges for code coverage reports. Another option is to generate a badge as part of a continuous integration process. See [Code Coverage](COVERAGE.md) for an example.

## How to add an item to the list

Open a pull request against the README.md document that adds the repository to the list.

- The pull request should add one and only one item to the list.
- The added item should be in alphabetical order within its category.
- The link should be the name of the package or project.
- Descriptions should be clear, concise, and non-promotional.
- Descriptions should follow the link on the same line and end with a punctuation mark.
- Remember to put a period `.` at the end of the project description.

If you are creating a new category, move the projects that apply to the new category, ensuring
that the resulting list has at least 3 projects in every category, and that the categories are alphabetized.

Fill out the template in your PR with the links asked for. If you accidentally remove the PR template from the submission, you can find it [here](https://github.com/avelino/awesome-go/blob/main/.github/PULL_REQUEST_TEMPLATE.md).

### Entry formatting rules

Good:

```md
- [project-name](https://github.com/org/project) - Short, clear description.
```

Bad (not alphabetical):

```md
- [zeta](https://github.com/org/zeta) - ...
- [alpha](https://github.com/org/alpha) - ...
```

Bad (promotional, missing period, or mismatched link text):

```md
- [Awesome Best Project Ever!!!](https://github.com/org/project) - The ultimate, world-class solution
```

### PR body example

Provide these links in the PR body to speed up review:

```md
Forge link: https://github.com/org/project
pkg.go.dev: https://pkg.go.dev/github.com/org/project
goreportcard.com: https://goreportcard.com/report/github.com/org/project
Coverage: https://app.codecov.io/gh/org/project
```

## Congrats, your project got accepted - what now

You are an outstanding project now! Feel encouraged to tell others about it by adding one of these badges:
[![Mentioned in Awesome Go](https://awesome.re/mentioned-badge.svg)](https://github.com/avelino/awesome-go)
[![Mentioned in Awesome Go](https://awesome.re/mentioned-badge-flat.svg)](https://github.com/avelino/awesome-go)

```md
[![Mentioned in Awesome Go](https://awesome.re/mentioned-badge.svg)](https://github.com/avelino/awesome-go)
[![Mentioned in Awesome Go](https://awesome.re/mentioned-badge-flat.svg)](https://github.com/avelino/awesome-go)
```

## Maintenance expectations for projects listed here

To prevent removal from awesome-go, your project must maintain the following quality standards.

- Development should be ongoing and maintain code quality. Official releases should be at least once a year if the project is ongoing.
- Or, if development has halted because the project is mature and stable, that can be demonstrated by having no bug reports in the Issues list that are older than 6 months.
- All links to quality reports should be to the most recent official release or current ongoing development.

Highly recommended but not required:

- A continuous integration process to be part of the ongoing development process
- That the project uses a pull-request process, and the owners do not commit directly to the repository
- That the pull-request process requires the continuous-integration tests to pass before a pull request can be merged

## How to remove an item from the list

- Open a pull request that deletes the line of the project in question.
- Delete the submission template and substitute a description of which criteria the project is not meeting. It should be a combination of the following.
  - The project has not made an official release within the last year and has open issues.
  - The project is not responding to bug reports issued within 6 months of submission.
  - The project is not meeting quality standards as indicated by the Go Report Card or Code Coverage tests.
  - The quality standard links have been removed from the documentation.
  - The project is no longer open-sourced.
  - The project is incompatible with any Go version issued within the last year (there is hopefully an open PR about this at the project).

If the project is hosted on GitHub, include a link to the project's submitter and/or author so
that they will be notified of the desire to remove the project and have an opportunity to respond.
The link should be of the form @githubID.

If the project is not hosted on GitHub, open an issue at the project in question's repository linking to the PR
and stating the following:

>This project is currently listed at awesome-go at <https://github.com/avelino/awesome-go>.
However, it appears that the project is not maintaining the quality standards required to continue to be listed at the awesome-go project.
This project is scheduled to be removed within 2 weeks of this posting. To continue to be listed at awesome-go, please respond at:
  -- link to above PR --

Then, comment on your PR at awesome-go with a link to the removal issue at the project.

## Maintainers

To make sure every PR is checked, we have [team maintainers](MAINTAINERS). Every PR MUST be reviewed by at least one maintainer before it can get merged.

The maintainers will review your PR and notify you and tag it in case any
information is still missing. They will wait 15 days for your interaction, after
that the PR will be closed.

## Reporting issues

Please open an issue if you would like to discuss anything that could be improved or have suggestions for making the list a more valuable resource. We realize sometimes packages fall into abandonment or have breaking builds for extended periods of time, so if you see that, feel free to change its listing, or please let us know. We also realize that sometimes projects are just going through transitions or are more experimental in nature. These can still be cool, but we can indicate them as transitory or experimental.

Removal changes will not be applied until they have been pending for a minimum of 1 week (7 days). This grace window benefits projects that may be going through a temporary transition, but are otherwise worthy of being on the list.

Thanks, everyone!

## How decisions are made

The official group of maintainers has the final decision on what PRs are accepted. Discussions are made openly in issues. Decisions are made by consensus.

## How to become a contributor

awesome-go is an open source project (created and maintained by the community), we are always open to new people to help us review the contributions (pull requests), **you don't need permission** or _name on the maintainers list_ to review a contribution and mark it as **LGTM**.

> Before you do anything, please read [this topic](https://github.com/avelino/awesome-go/blob/main/CONTRIBUTING.md#quality-standards) very carefully.

Now that you've read it, let's go!

Go into the pull requests (PR) and look at the following aspects:

- **shared links in the body of the PR:** they need to be valid and follow the quality specified above
- **check that the link added to `README.md`** is the same as the link to the repository mentioned in the body of the PR.
- **is it in the correct category?**

If everything is OK, mark the PR as approved, [read this documentation](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/reviewing-proposed-changes-in-a-pull-request#starting-a-review) on how to do it.

**Welcome to awesome-go!**

## How to become an ~~"official maintainer"~~

We don't give this name to people who are allowed to accept the PR.

If you are a person who is constantly active in reviewing PR and con
... [TRUNCATED]
```

### File: COVERAGE.md
```md
# Code Coverage

While we recommend using one of the free websites available for monitoring code coverage during your continuous integration process, below is an example of how you can incorporate code coverage during the continuous integration process provided by GitHub actions and generate a code coverage report without one of those services.

This `yaml` file will run tests on multiple system configurations, but will produce a code coverage report on only one of those. It will then create a code coverage badge and add it to the README file.

This file should be put in the `.github/workflows` directory of your repo:

```yaml
name: Go  # The name of the workflow that will appear on Github

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]
  # Allows you to run this workflow manually from the Actions tab
  workflow_dispatch:

jobs:

  build:
    runs-on: ${{ matrix.os }}
    strategy:
      matrix:
        os: [ubuntu-latest, windows-latest]
        go: [1.16, 1.17]
    steps:
    - uses: actions/checkout@v2

    - name: Set up Go
      uses: actions/setup-go@v2
      with:
        go-version: ${{ matrix.go }}

    - name: Build
      run: go install

    - name: Test
      run: |
        go test -v -cover ./... -coverprofile coverage.out -coverpkg ./...
        go tool cover -func coverage.out -o coverage.out  # Replaces coverage.out with the analysis of coverage.out

    - name: Go Coverage Badge
      uses: tj-actions/coverage-badge-go@v1
      if: ${{ runner.os == 'Linux' && matrix.go == '1.17' }} # Runs this on only one of the ci builds.
      with:
        green: 80
        filename: coverage.out

    - uses: stefanzweifel/git-auto-commit-action@v4
      id: auto-commit-action
      with:
        commit_message: Apply Code Coverage Badge
        skip_fetch: true
        skip_checkout: true
        file_pattern: ./README.md

    - name: Push Changes
      if: steps.auto-commit-action.outputs.changes_detected == 'true'
      uses: ad-m/github-push-action@master
      with:
        github_token: ${{ github.token }}
        branch: ${{ github.ref }}

```

```

### File: SECURITY.md
```md
# Security Policy

## Scope

This policy covers the **awesome-go repository itself** — including the curated list, the static site generator, CI/CD workflows, and any associated tooling.

If you find an issue with a **listed project** (a Go library or tool linked from the list), please report it directly to that project's maintainers, not here.

## Supported Versions

This is a community-maintained open source project provided as-is. There are no formal support commitments or versioned releases. The maintainers will do their best to address reports promptly and responsibly.

## Reporting a Vulnerability

If you discover a security vulnerability in this repository, please [open an issue](https://github.com/avelino/awesome-go/issues/new).

When reporting, please include:

- A clear description of the vulnerability
- Steps to reproduce (if applicable)
- The potential impact
- A suggested fix (if you have one)

The maintainers will review and respond as quickly as possible.

## Past Incidents

We believe in transparency. Security issues that have been identified and fixed are tracked in the public issue history of this repository.

```

### File: VETTING_REPORT.md
```md
---
title: Auto Vetting Report for awesome_go
date: 2026-04-05
analyst: civ_vetting_pipeline
status: AUTO_VETTED
---

# Auto-Vetted Repository
This repository was automatically swept and vetted by the batch processor. Only documentation remains.

```

### File: .github\PULL_REQUEST_TEMPLATE.md
```md
## Required links

_Provide the links below. Our CI will automatically validate them._

- [ ] Forge link (github.com, gitlab.com, etc): <!-- https://github.com/org/project -->
- [ ] pkg.go.dev: <!-- https://pkg.go.dev/github.com/org/project -->
- [ ] goreportcard.com: <!-- https://goreportcard.com/report/github.com/org/project -->
- [ ] Coverage service link ([codecov](https://codecov.io/), [coveralls](https://coveralls.io/), etc.): <!-- https://app.codecov.io/gh/org/project -->

## Pre-submission checklist

- [ ] I have read the [Contribution Guidelines](https://github.com/avelino/awesome-go/blob/main/CONTRIBUTING.md#contribution-guidelines)
- [ ] I have read the [Quality Standards](https://github.com/avelino/awesome-go/blob/main/CONTRIBUTING.md#quality-standards)

## Repository requirements

_These are validated automatically by CI:_

- [ ] The repo has a `go.mod` file and at least one SemVer release (`vX.Y.Z`).
- [ ] The repo has an open source license.
- [ ] The repo documentation has a pkg.go.dev link.
- [ ] The repo documentation has a goreportcard link (grade A- or better).
- [ ] The repo documentation has a coverage service link.

_These are recommended and reported as warnings:_

- [ ] The repo has a continuous integration process (GitHub Actions, etc.).
- [ ] CI runs tests that must pass before merging.

## Pull Request content

_These are validated automatically by CI:_

- [ ] This PR adds/removes/changes **only one** package.
- [ ] The package has been added in **alphabetical order**.
- [ ] The link text is the **exact project name**.
- [ ] The description is clear, concise, non-promotional, and **ends with a period**.
- [ ] The link in README.md matches the forge link above.

## Category quality

_Note: new categories require a minimum of 3 packages._

Packages added a long time ago might not meet the current guidelines anymore. It would be very helpful if you could check 3-5 packages above and below your submission to ensure they still meet the Quality Standards.

Please delete one of the following lines:

- [ ] The packages around my addition still meet the Quality Standards.
- [ ] I removed the following packages around my addition: (please give a short reason for each removal)

Thanks for your PR, you're awesome! :sunglasses:

```


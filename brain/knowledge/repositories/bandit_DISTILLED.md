---
id: repo-fetched-bandit-084509
type: knowledge
owner: OA
registered_at: 2026-04-05T03:48:14.353484
tags: ["auto-cloned", "oa-assimilated"]
---

# FETCHED_bandit_084509

## Assimilation Report
Auto-cloned repository: FETCHED_bandit_084509

## Application for OmniClaw
No structural integration blueprint provided.

## SWALLOW ENGINE DISTILLATION

### File: requirements.txt
```txt
# The order of packages is significant, because pip processes them in the order
# of appearance. Changing the order has an impact on the overall integration
# process, which may cause wedges in the gate later.
PyYAML>=5.3.1 # MIT
stevedore>=1.20.0 # Apache-2.0
colorama>=0.3.9;platform_system=="Windows" # BSD License (3 clause)
rich # MIT

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
reported to the community leaders responsible for enforcement at Ian
Stapleton Cordasco <graffatcolmingov@gmail.com>, Ian Lee <IanLee1521@gmail.com>
or Florian Bruhin <me@the-compiler.org>. All complaints will be reviewed and
investigated promptly and fairly.

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

### File: CONTRIBUTING.md
```md
# Contributing to Bandit
Thanks for considering to take part in the improvement of the Bandit project. Contributions are always welcome!
Here are guidelines and rules that can be helpful if you plan to want to get involved in the project.

#### Table Of Contents
[Code of Conduct](#code-of-conduct)

[How Can I Contribute?](#how-can-i-contribute)
  * [Reporting Bugs](#reporting-bugs)
  * [Suggesting Enhancements](#suggesting-enhancements)
  * [Your First Code Contribution](#your-first-code-contribution)
  * [Pull Requests](#pull-requests)
    * [Commit Message Guidelines](#commit-message-guidelines)
    * [Squash Commits](#squash-commits)
  * [Things You Should Know Before Getting Started](#things-you-should-know-before-getting-started)
    * [Vulnerability Tests](#vulnerability-tests)
    * [Writing Tests](#writing-tests)
    * [Extending Bandit](#extending-bandit)

## Code of Conduct
Everyone who participates in this project is governed by the PyCQA [Code of Conduct](https://github.com/PyCQA/bandit/blob/main/CODE_OF_CONDUCT.md#contributor-covenant-code-of-conduct).

## Reporting Bugs
If you encounter a bug, please let us know about it. See the guide here [GitHub issues](https://guides.github.com/features/issues/).

**Before submitting a new issue** you might want to check for an [existing issue](https://github.com/PyCQA/bandit/issues) to know if there is already a reported issue. If an issue is already open please feel free
to add a comment to the existing issue instead of creating a new one.

### Submitting your first issue
We encourage using the issue template to improve quality of reported issues.
Navigate to the issues tab and select `New issue`, then select the **Bug report** template and fill out the form.
To submit a good bug report keep in mind to:
* Use a descriptive title so other people can understand what the issue is about.
* Be specific about the details, for example, what command did you use, what version of Bandit did you use, and in what environment you observed the bug (CI or development).

## Suggesting Enhancements
If you want to suggest an enhancement, open a new issue and use the **Feature request** template.

**Before submitting an enhancement** please check for existing [feature requests](https://github.com/PyCQA/bandit/issues?q=is%3Aopen+is%3Aissue+label%3Aenhancement).

Useful things to point out in your feature request:
* Explain your feature request in a way that everyone can understand
* Please try to explain how this feature will improve the Bandit project

## Your First Code Contribution
You can start contributing to Bandit project by picking [bug issues](https://github.com/PyCQA/bandit/issues?q=is%3Aopen+is%3Aissue+label%3Abug)
These issues can be easier to resolve rather than a feature request and can get you up and running with the code base.

## Pull Requests
The best way to get started with Bandit is to grab the source:

Fork the repository into one with your username
```shell script
git clone https://github.com/<your username>/bandit.git
```

Create you own branch to start writing code:
```shell script
git switch -c mybranch
<create local changes>
git add <changed files>
git commit -S
<create a good commit message>
git push origin mybranch
```
You can test any changes with tox:

```shell script
pip install tox
tox run -e pep8
tox run -e format
tox run -e py310
tox run -e docs
tox run -e cover
```
If everything is done, proceed with [opening a new pull request](https://help.github.com/en/desktop/contributing-to-projects/creating-a-pull-request)

### Commit Message Guidelines

We follow the commit formatting recommendations found on [Chris Beams' How to Write a Git Commit Message article](https://chris.beams.io/posts/git-commit/).

Well formed commit messages not only help reviewers understand the nature of
the Pull Request, but also assists the release process where commit messages
are used to generate release notes.

A good example of a commit message would be as follows:

```
Summarize changes in around 50 characters or less

More detailed explanatory text, if necessary. Wrap it to about 72
characters or so. In some contexts, the first line is treated as the
subject of the commit and the rest of the text as the body. The
blank line separating the summary from the body is critical (unless
you omit the body entirely); various tools like `log`, `shortlog`
and `rebase` can get confused if you run the two together.

Explain the problem that this commit is solving. Focus on why you
are making this change as opposed to how (the code explains that).
Are there side effects or other unintuitive consequences of this
change? Here's the place to explain them.

Further paragraphs come after blank lines.

 - Bullet points are okay, too

 - Typically a hyphen or asterisk is used for the bullet, preceded
   by a single space, with blank lines in between, but conventions
   vary here

If you use an issue tracker, put references to them at the bottom,
like this:

Resolves: #123
See also: #456, #789
```

Note the `Resolves #123` tag, this references the issue raised and allows us to
ensure issues are associated and closed when a pull request is merged.

Please refer to [the github help page on message types](https://help.github.com/articles/closing-issues-using-keywords/)
for a complete list of issue references.

### Squash Commits

Should your pull request consist of more than one commit (perhaps due to
a change being requested during the review cycle), please perform a git squash
once a reviewer has approved your pull request.

A squash can be performed as follows. Let's say you have the following commits:

    initial commit
    second commit
    final commit

Run the command below with the number set to the total commits you wish to
squash (in our case 3 commits):

    git rebase -i HEAD~3

You default text editor will then open up and you will see the following::

    pick eb36612 initial commit
    pick 9ac8968 second commit
    pick a760569 final commit

    # Rebase eb1429f..a760569 onto eb1429f (3 commands)

We want to rebase on top of our first commit, so we change the other two commits
to `squash`:

    pick eb36612 initial commit
    squash 9ac8968 second commit
    squash a760569 final commit

After this, should you wish to update your commit message to better summarise
all of your pull request, run:

    git commit --amend

You will then need to force push (assuming your initial commit(s) were posted
to github):

    git push origin your-branch --force

## Things You Should Know Before Getting Started

### Vulnerability Tests
Vulnerability tests or "plugins" are defined in files in the plugins directory.

Tests are written in Python and are autodiscovered from the plugins directory.
Each test can examine one or more type of Python statements. Tests are marked
with the types of Python statements they examine (for example: function call,
string, import, etc).

Tests are executed by the ``BanditNodeVisitor`` object as it visits each node
in the AST.

Test results are managed in the ``Manager`` and aggregated for
output at the completion of a test run through the method `output_result` from ``Manager`` instance.

### Writing Tests
To write a test:
 - Identify a vulnerability to build a test for, and create a new file in
   examples/ that contains one or more cases of that vulnerability.
 - Consider the vulnerability you're testing for, mark the function with one
   or more of the appropriate decorators:
   - @checks('Call')
   - @checks('Import', 'ImportFrom')
   - @checks('Str')
 - Create a new Python source file to contain your test, you can reference
   existing tests for examples.
 - The function that you create should take a parameter "context" which is
   an instance of the context class you can query for information about the
   current element being examined.  You can also get the raw AST node for
   more advanced use cases.  Please see the context.py file for more.
 - Extend your Bandit configuration file as needed to support your new test.
 - Execute Bandit against the test file you defined in examples/ and ensure
   that it detects the vulnerability.  Consider variations on how this
   vulnerability might present itself and extend the example file and the test
   function accordingly.


### Extending Bandit

Bandit allows users to write and register extensions for checks and formatters.
Bandit will load plugins from two entry-points:

- `bandit.formatters`
- `bandit.plugins`

Formatters need to accept 5 things:

- `manager`: an instance of `bandit manager`
- `fileobj`: the output file object, which may be sys.stdout
- `sev_level` : Filtering severity level
- `conf_level`: Filtering confidence level
- `lines=-1`: number of lines to report

Plugins tend to take advantage of the `bandit.checks` decorator which allows
the author to register a check for a particular type of AST node. For example

::

    @bandit.checks('Call')
    def prohibit_unsafe_deserialization(context):
        if 'unsafe_load' in context.call_function_name_qual:
            return bandit.Issue(
                severity=bandit.HIGH,
                confidence=bandit.HIGH,
                text="Unsafe deserialization detected."
            )

To register your plugin, you have two options:

1. If you're using setuptools directly, add something like the following to
   your ``setup`` call::

        # If you have an imaginary bson formatter in the bandit_bson module
        # and a function called `formatter`.
        entry_points={'bandit.formatters': ['bson = bandit_bson:formatter']}
        # Or a check for using mako templates in bandit_mako that
        entry_points={'bandit.plugins': ['mako = bandit_mako']}

2. If you're using pbr, add something like the following to your `setup.cfg`
   file::

        [entry_points]
        bandit.formatters =
            bson = bandit_bson:formatter
        bandit.plugins =
            mako = bandit_mako

## Creating and Publishing a Release (Maintainers)

### Create the GitHub Release

1. Navigate to the [Releases](https://github.com/PyCQA/bandit/releases) page
2. Click on `Draft a new release`
3. Under `Choose a tag` enter a new release version (typically increment the patch number) and select `Create new tag: <version> on publish`
4. Click on `Generate release notes`
5. Click on `Publish release`

### Publish the Release to Test PyPI

1. Go to `Actions` tab
2. Click on the `Publish to Test PyPI` action
3. Click on `Run workflow`
4. Select `Use workflow from`, then `Tags` tab, and select `<version>`
5. Click on `Run workflow`

### Publish the Release to PyPI

1. Go to `Actions` tab
2. Click on the `Publish to PyPI` action
3. Click on `Run workflow`
4. Select `Use workflow from`, then `Tags` tab, and select `<version>`
5. Click on `Run workflow`

```

### File: SECURITY.md
```md
# Security Policy

Bandit is a tool designed to find security issues, so every effort is made that Bandit itself is also
free of those issues. However, if you believe you have found a security vulnerability in this repository
please open it privately via the [Report a security vulnerability](https://github.com/PyCQA/bandit/security/advisories/new) link in the Issues tab.

**Please do not report security vulnerabilities through public issues, discussions, or pull requests.**

Please also inform the [Tidelift security](https://tidelift.com/security). Tidelift will help coordinate the fix and disclosure.

```

### File: test-requirements.txt
```txt
# The order of packages is significant, because pip processes them in the order
# of appearance. Changing the order has an impact on the overall integration
# process, which may cause wedges in the gate later.
coverage>=4.5.4 # Apache-2.0
fixtures>=3.0.0 # Apache-2.0/BSD
flake8>=4.0.0 # Apache-2.0
stestr>=2.5.0 # Apache-2.0
testscenarios>=0.5.0 # Apache-2.0/BSD
testtools>=2.3.0 # MIT
beautifulsoup4>=4.8.0 # MIT
pylint==1.9.4 # GPLv2

```

### File: VETTING_REPORT.md
```md
---
title: Auto Vetting Report for bandit
date: 2026-04-05
analyst: civ_vetting_pipeline
status: AUTO_VETTED
---

# Auto-Vetted Repository
This repository was automatically swept and vetted by the batch processor. Only documentation remains.

```

### File: .github\ISSUE_TEMPLATE\Feature_request.md
```md
---
name: "\U0001F680 Feature request"
about: Suggest an idea for this project
title: ''
labels: enhancement
assignees: ''

---

**Is your feature request related to a problem? Please describe.**
A clear and concise description of what the problem is. Ex. I'm always frustrated when [...]

**Describe the solution you'd like**
A clear and concise description of what you want to happen.

**Describe alternatives you've considered**
A clear and concise description of any alternative solutions or features you've considered.

**Additional context**
Add any other context or screenshots about the feature request here.

Love this idea? Give it a 👍. We prioritize fulfilling features with the most 👍.

```


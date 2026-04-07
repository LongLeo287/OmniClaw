---
id: vale
type: knowledge
owner: OA_Triage
---
# vale
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
# Vale: Your style, our editor [![Build status](https://ci.appveyor.com/api/projects/status/snk0oo6ih1nwuf6r?svg=true)](https://ci.appveyor.com/project/jdkato/vale) [![GitHub All Releases](https://img.shields.io/github/downloads/errata-ai/vale/total?logo=GitHub&color=ff69b4)](https://github.com/errata-ai/vale/releases) [![Docker Pulls](https://img.shields.io/docker/pulls/jdkato/vale?color=orange&logo=docker&logoColor=white)](https://hub.docker.com/r/jdkato/vale) [![Chocolatey](https://img.shields.io/chocolatey/dt/vale?color=white&label=chocolatey&logo=chocolatey)](https://community.chocolatey.org/packages/vale) [![Homebrew](https://img.shields.io/homebrew/installs/dy/vale?color=yellow&label=homebrew&logo=homebrew)](https://formulae.brew.sh/formula/vale) [![Gurubase](https://img.shields.io/badge/Gurubase-Ask%20Vale%20Guru-006BFF)](https://gurubase.io/g/vale)

<p align="center">
  <b>Vale</b> is a command-line tool that brings code-like linting to prose. It's <b><a href="#mag-at-a-glance-vale-vs-">fast</a></b>, <b>cross-platform</b> (Windows, macOS, and Linux), and <b>highly customizable</b>.
</p>

<p align="center">
  <img width="75%" alt="A demo screenshot." src="https://vale.sh/media/mac.png">
</p>

<div align="center">
<table>
<thead>
<tr>
<th><a href="https://vale.sh/docs/vale-cli/installation/">Docs</a></th>
<th><a href="https://studio.vale.sh/">Vale Studio</a></th>
<th><a href="https://vale.sh/hub/">Package Hub</a></th>
<th><a href="https://vale.sh/explorer/">Rule Explorer</a></th>
<th><a href="https://vale.sh/generator/">Config Generator</a></th>
</tr>
</thead>
</table>
</div>

## :heart: Sponsors

> Hi there! I'm [@jdkato](https://github.com/jdkato), the sole developer of Vale. If you'd like to help me dedicate more time to _developing_, _documenting_, and _supporting_ Vale, feel free to donate through [GitHub Sponsors](https://github.com/sponsors/jdkato) or [Open Collective](https://opencollective.com/vale). Any donation&mdash;big, small, one-time, or recurring&mdash;is greatly appreciated!

### Organizations

<a href="https://opencollective.com/vale"><img src="https://opencollective.com/vale/organizations.svg?width=890"></a>

### Other

> Thanks to [DigitalOcean][1] for providing hosting credits for [Vale Studio][2].

<p>
  <a href="https://www.digitalocean.com/?refcode=dc0864bb87fd&utm_campaign=Referral_Invite&utm_medium=Referral_Program&utm_source=badge"><img src="https://web-platforms.sfo2.cdn.digitaloceanspaces.com/WWW/Badge%202.svg" alt="DigitalOcean Referral Badge" /></a>
</p>

[Deploy now on DigitalOcean](https://m.do.co/c/dc0864bb87fd) and get $200 in free credits!

### Individuals

<a href="https://opencollective.com/vale"><img src="https://opencollective.com/vale/individuals.svg?width=890"></a>

## :boom: Key Features

- [x] **Support for markup**: Vale has a rich understanding of many [markup formats](https://vale.sh/docs/topics/scoping/#formats), allowing it to avoid syntax-related false positives and intelligently exclude code snippets from prose-related rules.

- [x] A **highly customizable** [extension system](https://vale.sh/docs/topics/styles/): Vale is capable of enforcing _your style_&mdash;be it a standard [editorial style guide](https://github.com/errata-ai/styles#available-styles) or a custom in-house set of rules (see [examples][6]).

- [x] **Easy-to-install**, stand-alone binaries: Unlike other tools, Vale doesn't require you to install and configure a particular programming language and its related tooling (such as Python/pip or Node.js/npm).

See the [documentation](https://vale.sh) for more information.

## :mag: At a Glance: Vale vs. `<...>`

> **NOTE**: While all of the options listed below are open-source (CLI-based) linters for prose, their implementations and features vary significantly. And so, the "best" option will depends on your specific needs and preferences.

### Functionality

| Tool       | Extensible           | Checks          | Supports Markup                                                         | Built With | License      |
| ---------- | -------------------- | --------------- | ----------------------------------------------------------------------- | ---------- | ------------ |
| Vale       | Yes (via YAML)       | spelling, style | Yes (Markdown, AsciiDoc, reStructuredText, HTML, XML, Org)              | Go         | MIT          |
| textlint   | Yes (via JavaScript) | spelling, style | Yes (Markdown, AsciiDoc, reStructuredText, HTML, Re:VIEW)               | JavaScript | MIT          |
| RedPen     | Yes (via Java)       | spelling, style | Yes (Markdown, AsciiDoc, reStructuredText, Textile, Re:VIEW, and LaTeX) | Java       | Apache-2.0   |
| write-good | Yes (via JavaScript) | style           | No                                                                      | JavaScript | MIT          |
| proselint  | No                   | style           | No                                                                      | Python     | BSD 3-Clause |
| Joblint    | No                   | style           | No                                                                      | JavaScript | MIT          |
| alex       | No                   | style           | Yes (Markdown)                                                          | JavaScript | MIT          |

The exact definition of "Supports Markup" varies by tool but, in general, it means that the format is understood at a higher level than a regular plain-text file (for example, features like excluding code blocks from spell check).

Extensibility means that there's a built-in means of creating your own rules without modifying the original source code.

### Benchmarks

<table>
    <tr>
        <td width="50%">
            <a href="https://user-images.githubusercontent.com/8785025/97052257-809aa300-1535-11eb-83cd-65a52b29d6de.png">
                <img src="https://user-images.githubusercontent.com/8785025/97052257-809aa300-1535-11eb-83cd-65a52b29d6de.png" width="100%">
            </a>
        </td>
        <td width="50%">
            <a href="https://user-images.githubusercontent.com/8785025/97051175-91e2b000-1533-11eb-9a57-9d44d6def4c3.png">
                <img src="https://user-images.githubusercontent.com/8785025/97051175-91e2b000-1533-11eb-9a57-9d44d6def4c3.png" width="100%">
            </a>
        </td>
    </tr>
    <tr>
        <td width="50%">
          This benchmark has all three tools configured to use their implementations of the <code>write-good</code> rule set and Unix-style output.
        </td>
        <td width="50%">This benchmark runs Vale's implementation of <code>proselint</code>'s rule set against the original. Both tools are configured to use JSON output.</td>
    </tr>
    <tr>
        <td width="50%">
            <a href="https://user-images.githubusercontent.com/8785025/97053402-c5bfd480-1537-11eb-815b-a33ab13a59cf.png">
                <img src="https://user-images.githubusercontent.com/8785025/97053402-c5bfd480-1537-11eb-815b-a33ab13a59cf.png" width="100%">
            </a>
        </td>
        <td width="50%">
            <a href="https://user-images.githubusercontent.com/8785025/97055850-7b8d2200-153c-11eb-86fa-d882ce6babf8.png">
                <img src="https://user-images.githubusercontent.com/8785025/97055850-7b8d2200-153c-11eb-86fa-d882ce6babf8.png" width="100%">
            </a>
        </td>
    </tr>
    <tr>
        <td width="50%">
          This benchmark runs Vale's implementation of Joblint's rule set against the original. Both tools are configured to use JSON output.
        </td>
        <td width="50%">This benchmark has all three tools configured to perform only English spell checking using their default output styles.</td>
    </tr>
</table>

All benchmarking was performed using the open-source [hyperfine](https://github.com/sharkdp/hyperfine) tool on a MacBook Pro (2.9 GHz Intel Core i7):

```
hyperfine --warmup 3 '<command>'
```

The corpus IDs in the above plots&mdash;`gitlab` and `ydkjs`&mdash;correspond to the following files:

- A [snapshot][7] of GitLab's open-source documentation (1,500 Markdown files).

- A [chapter][8] from the open-source book _You Don't Know JS_.

[1]: https://www.digitalocean.com/open-source/credits-for-projects
[2]: https://studio.vale.sh/
[3]: https://appwrite.io/oss-fund
[4]: https://appwrite.io/
[5]: https://page.famewall.io/vale
[6]: https://vale.sh/#users
[7]: https://gitlab.com/gitlab-org/gitlab/-/tree/7d6a4025a0346f1f50d2825c85742e5a27b39a8b/doc
[8]: https://raw.githubusercontent.com/getify/You-Dont-Know-JS/1st-ed/es6%20%26%20beyond/ch2.md

```

### File: .pre-commit-hooks.yaml
```yaml
- id: vale
  name: vale
  description: Run vale on your text
  entry: vale
  language: golang
  types: [text]

```

### File: .github\CODE_OF_CONDUCT.md
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
jdkato@vale.sh.
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

### File: .github\CONTRIBUTING.md
```md
# Contributing to Vale

Interested in contributing to Vale? Great&mdash;we welcome contributions of any kind including documentation improvements, bug reports, feature requests, and pull requests.

## Table of Contents

- [Contributing to Vale](#contributing-to-vale)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Testing](#testing)
  - [Setting up a Development Environment](#setting-up-a-development-environment)
  - [Code Contribution Guidelines](#code-contribution-guidelines)
  - [Git Commit Message Guidelines](#git-commit-message-guidelines)
  - [Terminology](#terminology)

## Introduction

Vale is a natural language linter that supports plain text, markup (Markdown, reStructuredText, AsciiDoc, and HTML), and source code comments. However, unlike many similar projects, Vale's primary focus isn't on providing a collection of rules everyone must follow&mdash;instead, Vale aims to be flexible enough to support many different styles (see [Styles](https://errata-ai.github.io/vale/styles/) for more information).

More specifically, Vale is written in Go and split into packages that are tasked with implementing specific functionality:

- `check` handles the loading and validating of external rules (YAML files).
- `core`: includes the main structures used throughout the application (e.g., `File` and `Alert`) and manages configuration files.
- `lint` handles the actual linting, which includes knowing when to apply rules and how to handle specific file formats.
- `rule` implements Vale's built-in style.
- `ui` manages displaying information to users.

If you're looking to improve Vale's documentation, check out the [`docs/`](https://github.com/errata-ai/vale/tree/master/docs) directory.

## Testing

Vale is tested using both integration and unit tests.

Integration tests are the most plentiful at the moment. They're implemented using the behavior-driven development framework [Cucumber](https://cucumber.io/). You'll find the relevant files for these tests in the `fixtures` and `features` directories. Unit tests are found in the `*_test.go` files inside the actual Go packages.

We also track Vale's performance on a per-commit basis through benchmarks. On every commit, you'll see comparison against the last tagged release (over 5 runs) on CI builds:

```text
LintRST-2   1.63s ± 2%   1.65s ± 2%  +0.95%  (p=0.031 n=10+10)
LintMD-2    1.54s ± 1%   1.54s ± 1%    ~     (p=0.604 n=10+10)
```


To run the tests, you'll want to invoke either `make bench` or `make ci` (see [Setting up a Development Environment]() for more information).

## Setting up a Development Environment

Prerequisites:

* [Ruby](https://www.ruby-lang.org/en/downloads/) (v2.3+)
* [Go](https://golang.org/) (v1.7+) installed.
* [Asciidoctor](http://asciidoctor.org/) available on your `$PATH`.
* [rst2html](http://docutils.sourceforge.net/docs/user/tools.html#rst2html-py) available on your `$PATH`. The latter is installed with both [Sphinx](http://www.sphinx-doc.org/en/stable/) and [docutils](https://pypi.python.org/pypi/docutils).
* [xsltproc](http://xmlsoft.org/xslt/xsltproc.html) available on your `$PATH`.
* [dita](https://www.dita-ot.org/download) available on your `$PATH` (v3.6+).

```bash
$ gem install bundler:2.2.31 # if necessary
$ make setup
$ make test
```

## Code Contribution Guidelines

To make the contribution process as seamless as possible, we ask for the following:

* Fork the project and make your changes.
* When you’re ready to create a pull request, be sure to:
    * Run `make lint` to check your Go code style.
    * Squash your commits into a single commit. `git rebase -i`. It’s okay to force update your pull request with `git push -f`.
    * Follow the **Git Commit Message Guidelines** below.

## Git Commit Message Guidelines

Vale follows a modified version of the [AngularJS Commit Guidelines](https://github.com/angular/angular.js/blob/master/CONTRIBUTING.md#-git-commit-guidelines). A commit message should take the following form:

```
<type>: <subject>
<BLANK LINE>
<body>
<BLANK LINE>
<footer>
```

with `<body>` and `<footer>` being optional. `<type>` should be one of the following:

- `feat`: A new feature
- `fix`: A bug fix
- `docs`: Documentation only changes (e.g., this document, the README, or source comments)
- `style`: Changes that do not affect the meaning of the code (e.g., code formatting)
- refactor: A code change that neither fixes a bug nor adds a feature
- `perf`: A code change that improves performance (in this case, please include relevant benchmark(s))
- `test`: Adding missing or correcting existing tests
- `chore`: Changes to the build process or auxiliary tools

An example would be something like:

```text
refactor: make "warning" the default lint level

Also demotes `Annotations` and `PassiveVoice` to "suggestions."

Related to #30.
```

## Terminology

| Term  | Definition                                                                                                                                                                        |
|:-----:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| check | A "check" is one of Vale's extension points (e.g., `existence` and `substitution`) that performs a single task such as looking for the existence of a word.                       |
| rule  | A "rule" is an actual implementation of a check. For example, [`Hedging`](https://github.com/errata-ai/vale/blob/master/rule/vale/Hedging.yml) is one of Vale's built-in rules.         |
| style | A "style" is a collection of rules. For example, [`Joblint`](https://github.com/errata-ai/vale/tree/master/rule/Joblint) is a style that consists of rules such as `LegacyTech`. |

```

### File: internal\core\alert.go
```go
package core

// AlertLevels holds the possible values for "level" in an external rule.
var AlertLevels = []string{"suggestion", "warning", "error"}

// LevelToInt allows us to easily compare levels in lint.go.
var LevelToInt = map[string]int{
	"suggestion": 0,
	"warning":    1,
	"error":      2,
}

// An Action represents a possible solution to an Alert.
type Action struct {
	Name   string   // the name of the action -- e.g, 'replace'
	Params []string // a slice of parameters for the given action
}

// An Alert represents a potential error in prose.
type Alert struct {
	Action         Action   // a possible solution
	Span           []int    // the [begin, end] location within a line
	Offset         []string `json:"-"` // tokens to ignore before this match
	Check          string   // the name of the check
	Description    string   // why `Message` is meaningful
	Link           string   // reference material
	Message        string   // the output message
	Severity       string   // 'suggestion', 'warning', or 'error'
	Match          string   // the actual matched text
	Line           int      // the source line
	Limit          int      `json:"-"` // the max times to report
	Hide           bool     `json:"-"` // should we hide this alert?
	HasByteOffsets bool     `json:"-"` // Span holds byte offsets into the raw document
}

// FormatAlert ensures that all required fields have data.
func FormatAlert(a *Alert, limit int, level, name string) {
	if a.Severity == "" {
		a.Severity = level
	}
	if a.Check == "" {
		a.Check = name
	}
	a.Limit = limit
	a.Message = WhitespaceToSpace(a.Message)
}

// ByPosition sorts Alerts by line and column.
type ByPosition []Alert

func (a ByPosition) Len() int      { return len(a) }
func (a ByPosition) Swap(i, j int) { a[i], a[j] = a[j], a[i] }
func (a ByPosition) Less(i, j int) bool {
	ai, aj := a[i], a[j]

	if ai.Line != aj.Line {
		return ai.Line < aj.Line
	}
	return ai.Span[0] < aj.Span[0]
}

// ByName sorts Files by their path.
type ByName []*File

func (a ByName) Len() int      { return len(a) }
func (a ByName) Swap(i, j int) { a[i], a[j] = a[j], a[i] }
func (a ByName) Less(i, j int) bool {
	ai, aj := a[i], a[j]
	return ai.Path < aj.Path
}

```

### File: internal\core\config.go
```go
package core

import (
	"bufio"
	"encoding/json"
	"fmt"
	"io"
	"os"
	"path/filepath"
	"strings"

	"github.com/adrg/xdg"
	"github.com/bmatcuk/doublestar/v4"
	"github.com/errata-ai/ini"

	"github.com/errata-ai/vale/v3/internal/glob"
	"github.com/errata-ai/vale/v3/internal/system"
)

var (
	// ConfigDir is the default location for Vale's configuration files.
	//
	// This was introduced in v3.0.0 as a means of standardizing the location
	// of Vale's configuration files.
	//
	// This directory is relative to the user's specified `StylesPath`, which
	// can be set via the `--config` flag, the `VALE_CONFIG_PATH` environment
	// variable, or the default search process.
	//
	// NOTE: The config pipeline is stored in the top-level `.vale-config`
	// directory. See `cmd/vale/sync.go`.
	ConfigDir = "config"

	// PipeDir is the default location for Vale's configuration pipeline.
	PipeDir = ".vale-config"

	VocabDir  = filepath.Join(ConfigDir, "vocabularies")
	DictDir   = filepath.Join(ConfigDir, "dictionaries")
	TmplDir   = filepath.Join(ConfigDir, "templates")
	IgnoreDir = filepath.Join(ConfigDir, "ignore")
	ActionDir = filepath.Join(ConfigDir, "actions")
	FilterDir = filepath.Join(ConfigDir, "filters")
	ScriptDir = filepath.Join(ConfigDir, "scripts")
	ViewDir   = filepath.Join(ConfigDir, "views")
)

// ConfigDirs is a list of all directories that contain user-defined, non-style
// configuration files.
var ConfigDirs = []string{
	VocabDir,
	DictDir,
	TmplDir,
	IgnoreDir,
	ActionDir,
	ScriptDir,
	FilterDir,
	ViewDir,
}

// ConfigVars is a list of all supported environment variables.
var ConfigVars = map[string]string{
	"VALE_CONFIG_PATH": "Override the default search process by specifying a .vale.ini file.",
	"VALE_STYLES_PATH": "Specify the location of the default StylesPath.",
}

// ConfigNames is a list of all possible configuration file names.
//
// NOTE: This is leftover from the early days of Vale; we have now standardized
// on `.vale.ini` for documentation purposes.
var configNames = []string{
	".vale",
	"_vale",
	"vale.ini",
	".vale.ini",
	"_vale.ini",
}

// FindConfigAsset tries to locate a Vale-related resource by looking in the
// user-defined StylesPath(s).
func FindConfigAsset(cfg *Config, name, dir string) string {
	return getConfigAsset(name, cfg.SearchPaths(), []string{dir})
}

// FindAsset tries to locate a Vale-related resource by looking in the
// user-defined StylesPath.
func FindAsset(cfg *Config, path string) string {
	if path == "" {
		return ""
	}

	for _, p := range cfg.SearchPaths() {
		inPath := filepath.Join(p, path)
		if system.FileExists(inPath) {
			return inPath
		}
	}

	if p := getConfigAsset(path, cfg.SearchPaths(), ConfigDirs); p != "" {
		return p
	}

	p := system.DeterminePath(cfg.Flags.Path, path)
	if system.FileExists(p) {
		return p
	}

	return ""
}

// IgnoreFiles returns a list of all user-defined ignore files.
func IgnoreFiles(stylesPath string) ([]string, error) {
	ignore := filepath.Join(stylesPath, IgnoreDir)
	return doublestar.FilepathGlob(filepath.Join(ignore, "**", "*.txt"))
}

// getConfigAsset returns the path to a given asset if it exists.
// Otherwise, it returns an empty string.
func getConfigAsset(target string, paths, dirs []string) string {
	for _, p := range paths {
		for _, dir := range dirs {
			path := filepath.Join(p, dir, target)
			if system.FileExists(path) {
				return path
			}
		}
	}
	return ""
}

// DefaultConfig returns the path to the default configuration file.
//
// We don't create this file automatically because there's no actual notion of
// a "default" configuration -- it's just a file loation.
//
// NOTE: if this file does not exist *and* the user has not specified a
// project-specific configuration file, Vale raises an error.
func DefaultConfig() (string, error) {
	root, err := xdg.ConfigFile("vale/.vale.ini")
	if err != nil {
		return "", fmt.Errorf("failed to find default config: %w", err)
	}
	return root, nil
}

// DefaultStylesPath returns the path to the default styles directory.
//
// NOTE: the default styles directory is only used if neither the
// project-specific nor the global configuration file specify a `StylesPath`.
func DefaultStylesPath() (string, error) {
	if fromEnv, hasEnv := os.LookupEnv("VALE_STYLES_PATH"); hasEnv {
		return fromEnv, nil
	}

	styles, err := xdg.DataFile("vale/styles/config.yml")
	if err != nil {
		return "", fmt.Errorf("failed to find default styles: %w", err)
	}

	return filepath.Dir(styles), nil
}

// CLIFlags holds the values that are defined at runtime by the user.
//
// For example, `vale --minAlertLevel=error`.
type CLIFlags struct {
	AlertLevel   string
	Built        string
	Glob         string
	InExt        string
	InPath       string
	Output       string
	Path         string
	Sources      string
	Filter       string
	Local        bool
	NoExit       bool
	Normalize    bool
	Relative     bool
	Remote       bool
	Simple       bool
	Sorted       bool
	Wrap         bool
	Version      bool
	Help         bool
	IgnoreGlobal bool
}

// Config holds the configuration values from both the CLI and `.vale.ini`.
type Config struct {
	// General configuration
	BlockIgnores      map[string][]string        // A list of blocks to ignore
	Checks            []string                   // All checks to load
	Formats           map[string]string          // A map of unknown -> known formats
	Asciidoctor       map[string]string          // A map of asciidoctor attributes
	FormatToLang      map[string]string          // A map of format to lang ID
	GBaseStyles       []string                   // Global base style
	GChecks           map[string]bool            // Global checks
	IgnoredClasses    []string                   // A list of HTML classes to ignore
	IgnoredScopes     []string                   // A list of HTML tags to ignore
	MinAlertLevel     int                        // Lowest alert level to display
	Vocab             []string                   // The active project
	RuleToLevel       map[string]string          // Single-rule level changes
	SBaseStyles       map[string][]string        // Syntax-specific base styles
	SChecks           map[string]map[string]bool // Syntax-specific checks
	SkippedScopes     []string                   // A list of HTML blocks to ignore
	Stylesheets       map[string]string          // XSLT stylesheet
	TokenIgnores      map[string][]string        // A list of tokens to ignore
	CommentDelimiters map[string][2]string       // Strings to treat as comment delimiters. Indicates the start and end delimiters.
	WordTemplate      string                     // The template used in YAML -> regexp list conversions
	RootINI           string                     // the path to the project's .vale.ini file
	Paths             []string                   // A list of paths to search for styles
	ConfigFiles       []string                   // A list of configuration files to load

	AcceptedTokens []string `json:"-"` // Project-specific vocabulary (okay)
	RejectedTokens []string `json:"-"` // Project-specific vocabulary (avoid)

	FallbackPath string               `json:"-"`
	SecToPat     map[string]glob.Glob `json:"-"`
	Styles       []string             `json:"-"`
	Views        map[string]*View     `json:"-"`

	NLPEndpoint string // An external API to call for NLP-related work.

	// Command-line configuration
	Flags *CLIFlags `json:"-"`

	StyleKeys []string `json:"-"`
	RuleKeys  []string `json:"-"`
}

// NewConfig initializes a Config with its default values.
func NewConfig(flags *CLIFlags) (*Config, error) {
	var cfg Config

	cfg.BlockIgnores = make(map[string][]string)
	cfg.Flags = flags
	cfg.Formats = make(map[string]string)
	cfg.Asciidoctor = make(map[string]string)
	cfg.GChecks = make(map[string]bool)
	cfg.MinAlertLevel = 0
	cfg.RuleToLevel = make(map[string]string)
	cfg.SBaseStyles = make(map[string][]string)
	cfg.SChecks = make(map[string]map[string]bool)
	cfg.SecToPat = make(map[string]glob.Glob)
	cfg.Stylesheets = make(map[string]string)
	cfg.TokenIgnores = make(map[string][]string)
	cfg.CommentDelimiters = make(map[string][2]string)
	cfg.FormatToLang = make(map[string]string)
	cfg.Views = make(map[string]*View)
	cfg.Paths = []string{}
	cfg.ConfigFiles = []string{}

	found, _ := DefaultStylesPath()
	if !flags.IgnoreGlobal && system.IsDir(found) {
		cfg.AddStylesPath(found)
	}

	return &cfg, nil
}

// AddConfigFile adds a new configuration file to the current list.
func (c *Config) AddConfigFile(name string) {
	if !StringInSlice(name, c.ConfigFiles) {
		c.ConfigFiles = append(c.ConfigFiles, name)
	}
}

// AddStylesPath adds a new path to the current list.
func (c *Config) AddStylesPath(path string) {
	if !StringInSlice(path, c.Paths) && path != "" {
		c.Paths = append(c.Paths, path)
	}
}

// ConfigFile returns the last configuration file in the list.
//
// This represents the user's project-agnostic configuration file -- i.e., the
// last one that was added.
func (c *Config) ConfigFile() string {
	if len(c.ConfigFiles) > 0 {
		return c.ConfigFiles[len(c.ConfigFiles)-1]
	}
	return ""
}

// Root returns the first configuration file in the list.
func (c *Config) Root() (string, error) {
	if len(c.ConfigFiles) > 0 {
		return c.ConfigFiles[0], nil
	}

	root, err := DefaultConfig()
	if err != nil {
		return "", err
	}

	if !system.FileExists(root) {
		return "", fmt.Errorf("no .vale.ini file found")
	}

	return root, nil
}

// GetStylesPath returns the last path in the list.
//
// This represents the user's project-specific styles directory -- i.e., the
// last one that was added.
func (c *Config) StylesPath() string {
	if len(c.Paths) > 0 {
		return c.Paths[len(c.Paths)-1]
	}
	return ""
}

func (c *Config) SearchPaths() []string {
	if len(c.Paths) == 0 {
		// This represents the 'no value set' case.
		return []string{""}
	}
	return c.Paths
}

// AddWordListFile adds vocab terms from a provided file.
func (c *Config) AddWordListFile(name string, accept bool) error {
	fd, err := os.Open(name)
	if err != nil {
		return err
	}
	defer fd.Close()
	return c.addWordList(fd, accept)
}

func (c *Config) addWordList(r io.Reader, accept bool) error {
	scanner := bufio.NewScanner(r)
	for scanner.Scan() {
		word := strings.TrimSpace(scanner.Text())
		if len(word) == 0 || strings.HasPrefix(word, "# ") { //nolint:gocritic
			continue
		} else if accept {
			c.AcceptedTokens = append(c.AcceptedTokens, word)
		} else {
			c.RejectedTokens = append(c.RejectedTokens, word)
		}
	}
	return scanner.Err()
}

func (c *Config) String() string {
	b, _ := json.MarshalIndent(c, "", "  ")
	return string(b)
}

// Get the user-defined packages from a `.vale.ini` file.
func GetPackages(src string) ([]string, error) {
	packages := []string{}

	uCfg, err := ini.Load(src)
	if err != nil {
		return packages, err
	}

	core := uCfg.Section("")
	return core.Key("Packages").Strings(","), nil
}

func pipeConfig(cfg *Config) ([]string, error) {
	var sources []string

	pipeline := filepath.Join(cfg.StylesPath(), ".vale-config")
	if system.IsDir(pipeline) && len(cfg.Flags.Sources) == 0 {
		configs, err := os.ReadDir(pipeline)
		if err != nil {
			return sources, err
		}

		for _, config := range configs {
			if config.IsDir() {
				continue
			}
			sources = append(sources, filepath.Join(pipeline, config.Name()))
		}
		sources = append(sources, cfg.ConfigFiles...)
	}

	return sources, nil
}

// MockLoad returns the would-be configuration after loading two files, one
// from the project and one from the user's local directory.
func MockLoad(project, local string, cfg *Config) error {
	uCfg, err := ini.LoadSources(ini.LoadOptions{
		AllowShadows:             true,
		SpaceBeforeInlineComment: true}, project, local)

	if err != nil {
		return err
	}

	_, err = processConfig(uCfg, cfg, true)
	return err
}

```

### File: internal\core\config_test.go
```go
package core

import (
	"os"
	"path/filepath"
	"testing"

	"github.com/errata-ai/vale/v3/internal/system"
)

var testData = filepath.Join("..", "..", "testdata")

func TestInitCfg(t *testing.T) {
	cfg, err := NewConfig(&CLIFlags{})
	if err != nil {
		t.Fatal(err)
	}
	path := cfg.StylesPath()

	// In v3.0, these should have defaults.
	if path == "" {
		t.Fatal("StylesPath is empty")
	} else if !system.IsDir(path) {
		t.Fatalf("%s is not a directory", path)
	}
}

func TestGetIgnores(t *testing.T) {
	found, err := IgnoreFiles(filepath.Join(testData, "styles"))
	if err != nil {
		t.Fatal(err)
	} else if len(found) != 2 {
		t.Fatalf("Expected 2 ignore files, found %d", len(found))
	}
}

// TestFindAsset tests that we find an asset on the user-specified StylesPath.
//
// This was the standard behavior in v2.0.
func TestFindAsset(t *testing.T) {
	cfg, err := NewConfig(&CLIFlags{})
	if err != nil {
		t.Fatal(err)
	}
	cfg.AddStylesPath(filepath.Join(testData, "styles"))

	found := FindAsset(cfg, "line.tmpl")
	if found == "" {
		t.Fatal("Expected to find line.tmpl")
	}

	found = FindAsset(cfg, "notfound")
	if found != "" {
		t.Fatal("Expected to not find notfound")
	}
}

// TestFindAssetDefault tests that we find an asset on the default StylesPath
// when there's no user-specified StylesPath.
func TestFindAssetDefault(t *testing.T) {
	cfg, err := NewConfig(&CLIFlags{})
	if err != nil {
		t.Fatal(err)
	}

	expected, err := DefaultStylesPath()
	if err != nil {
		t.Fatal(err)
	}
	target := filepath.Join(expected, "tmp.tmpl")

	err = os.WriteFile(target, []byte{}, 0600)
	if err != nil {
		t.Fatal("Failed to create file", err)
	}

	found := FindAsset(cfg, "tmp.tmpl")
	if found == "" {
		t.Fatal("Expected to find 'tmp.tmpl', got empty")
	}

	found = FindAsset(cfg, "notfound")
	if found != "" {
		t.Fatal("Expected to not find 'notfound', got", found)
	}

	err = os.Remove(target)
	if err != nil {
		t.Fatal(err)
	}
}

// TestFallbackToDefault tests that we find an asset on the default StylesPath
// when there's a user-specified StylesPath, but the asset isn't there.
func TestFallbackToDefault(t *testing.T) {
	cfg, err := NewConfig(&CLIFlags{})
	if err != nil {
		t.Fatal(err)
	}

	local := filepath.Join(testData, "styles")
	cfg.AddStylesPath(local)

	expected, err := DefaultStylesPath()
	if err != nil {
		t.Fatal(err)
	}
	target := filepath.Join(expected, "tmp.tmpl")

	err = os.WriteFile(target, []byte{}, 0600)
	if err != nil {
		t.Fatal("Failed to create file", err)
	}

	found := FindAsset(cfg, "tmp.tmpl")
	if found == "" {
		t.Fatal("Expected to find 'tmp.tmpl', got empty", cfg.Paths)
	}

	err = os.Remove(target)
	if err != nil {
		t.Fatal(err)
	}
}

```

### File: internal\core\doc.go
```go
// Package core contains configuration and utility internals.
package core

```

### File: internal\core\error.go
```go
package core

import (
	"bufio"
	"bytes"
	"errors"
	"fmt"
	"os"
	"path/filepath"
	"strings"

	"github.com/pterm/pterm"
)

type lineError struct {
	content string
	line    int
	span    []int
}

type errorCondition func(position int, line, target string) bool

func annotate(file []byte, target string, finder errorCondition) (lineError, error) {
	var sb strings.Builder

	scanner := bufio.NewScanner(bytes.NewBuffer(file))
	context := lineError{span: []int{1, 1}}

	idx := 1
	for scanner.Scan() {
		markup := scanner.Text()
		plain := StripANSI(markup)
		if idx-context.line > 2 && context.line != 0 { //nolint:gocritic
			break
		} else if finder(idx, plain, target) && context.line == 0 {
			context.line = idx

			s := strings.Index(plain, target) + 1
			context.span = []int{s, s + len(target)}

			sb.WriteString(
				fmt.Sprintf("\033[1;32m%4d\033[0m* %s\n", idx, markup))
		} else {
			sb.WriteString(
				fmt.Sprintf("\033[1;32m%4d\033[0m  %s\n", idx, markup))
		}
		idx++
	}

	if err := scanner.Err(); err != nil {
		return lineError{}, err
	}

	lines := []string{}
	for i, l := range strings.Split(sb.String(), "\n") {
		if context.line-i < 3 {
			lines = append(lines, l)
		}
	}

	context.content = strings.Join(lines, "\n")
	return context, nil
}

// NewError creates a colored error from the given information.
//
// # The standard format is
//
// ```
// <code> [<context>] <title>
//
// <msg>
// ```
func NewError(code, title, msg string) error {
	return fmt.Errorf(
		"%s %s\n\n%s\n\n%s",
		pterm.BgRed.Sprint(code),
		title,
		msg,
		pterm.Fuzzy.Sprint(pterm.Italic.Sprintf("Execution stopped with code 1.")),
	)
}

// NewE100 creates a new, formatted "unexpected" error.
//
// Since E100 errors can occur anywhere, we include a "context" that makes it
// clear where exactly the error was generated.
func NewE100(context string, err error) error {
	title := fmt.Sprintf("[%s] %s", context, "Runtime error")
	return NewError("E100", title, err.Error())
}

// NewE201 creates a formatted user-generated error.
//
// 201 errors involve a specific configuration asset and should contain
// parsable location information on their last line of the form:
//
// <path>:<line>:<start>:<end>
func NewE201(msg, value, path string, finder errorCondition) error {
	f, err := os.ReadFile(path)
	if err != nil {
		return NewE100("NewE201", errors.New(msg))
	}

	ctx, err := annotate(f, value, finder)
	if err != nil {
		return NewE100("NewE201/annotate", err)
	}

	title := fmt.Sprintf(
		"Invalid value [%s:%d:%d]:",
		filepath.ToSlash(path),
		ctx.line,
		ctx.span[0])

	return NewError(
		"E201",
		title,
		fmt.Sprintf("%s\n%s", ctx.content, msg))
}

// NewE201FromTarget creates a new E201 error from a target string.
func NewE201FromTarget(msg, value, file string) error {
	return NewE201(
		msg,
		value,
		file,
		func(_ int, line, target string) bool {
			return strings.Contains(line, target)
		})
}

// NewE201FromPosition creates a new E201 error from an in-file location.
func NewE201FromPosition(msg, file string, goal int) error {
	return NewE201(
		msg,
		"",
		file,
		func(position int, _, _ string) bool {
			return position == goal
		})
}

```

### File: internal\core\file.go
```go
package core

import (
	"bytes"
	"encoding/json"
	"os"
	"path/filepath"
	"regexp"
	"sort"
	"strconv"
	"strings"

	"github.com/jdkato/twine/summarize"

	"github.com/errata-ai/vale/v3/internal/glob"
	"github.com/errata-ai/vale/v3/internal/nlp"
	"github.com/errata-ai/vale/v3/internal/system"
)

var commentControlRE = regexp.MustCompile(`^vale (.+\..+|[^.]+) = (YES|NO|on|off)$`)

var commentStyleRE = regexp.MustCompile(`^vale styles? = (.*)$`)

var commentControlMatchesRE = regexp.MustCompile(`^vale (.+\..+)(\[.+\]) = (YES|NO)$`)

// A File represents a linted text file.
type File struct {
	NLP        nlp.Info          // -
	Summary    bytes.Buffer      // holds content to be included in summarization checks
	Alerts     []Alert           // all alerts associated with this file
	BaseStyles []string          // base style assigned in .vale
	Lines      []string          // the File's Content split into lines
	Sequences  []string          // tracks various info (e.g., defined abbreviations)
	Content    string            // the raw file contents
	Format     string            // 'code', 'markup' or 'prose'
	NormedExt  string            // the normalized extension (see util/format.go)
	Path       string            // the full path
	NormedPath string            // the normalized path
	Transform  string            // XLST transform
	RealExt    string            // actual file extension
	Checks     map[string]bool   // syntax-specific checks assigned in .vale
	ChkToCtx   map[string]string // maps a temporary context to a particular check
	Comments   map[string]bool   // comment control statements
	Metrics    map[string]int    // count-based metrics
	history    map[string]int    // -
	limits     map[string]int    // -
	simple     bool              // -
	Lookup     bool              // -
}

// NewFile initializes a File.
func NewFile(src string, config *Config) (*File, error) {
	var format, ext string
	var fbytes []byte
	var lookup bool
	path := src

	if system.FileExists(src) {
		fbytes, _ = os.ReadFile(src)
		if config.Flags.InExt != ".txt" {
			ext, format = FormatFromExt(config.Flags.InExt, config.Formats)
		} else {
			ext, format = FormatFromExt(src, config.Formats)
		}
	} else {
		fbytes = []byte(src)
		lookup = true
		// For stdin, allow an explicit path override to drive path-based config.
		if config.Flags.InPath != "" {
			path = config.Flags.InPath
		} else {
			path = "stdin" + config.Flags.InExt
		}
		// If --ext was explicitly set, respect it; otherwise infer from the path.
		if config.Flags.InExt != ".txt" {
			ext, format = FormatFromExt(config.Flags.InExt, config.Formats)
		} else {
			ext, format = FormatFromExt(path, config.Formats)
		}
	}

	filepaths := []string{path}
	normed := system.ReplaceFileExt(path, config.Formats)

	baseStyles := config.GBaseStyles
	checks := make(map[string]bool)

	for _, fp := range filepaths {
		for _, sec := range config.StyleKeys {
			if pat, found := config.SecToPat[sec]; found && pat.Match(fp) {
				baseStyles = config.SBaseStyles[sec]
			}
		}

		for _, sec := range config.RuleKeys {
			if pat, found := config.SecToPat[sec]; found && pat.Match(fp) {
				for k, v := range config.SChecks[sec] {
					checks[k] = v
				}
			}
		}
	}

	lang := "en"
	for syntax, code := range config.FormatToLang {
		sec, err := glob.Compile(syntax)
		if err != nil {
			return &File{}, err
		} else if sec.Match(path) {
			lang = code
			break
		}
	}

	transform := ""
	for sec, p := range config.Stylesheets {
		pat, err := glob.Compile(sec)
		if err != nil {
			return &File{}, NewE100(path, err)
		} else if pat.Match(path) {
			transform = p
			break
		}
	}
	content := Sanitize(string(fbytes))

	// NOTE: We need to perform a clone here because we perform inplace editing
	// of the files contents that we don't want reflected in `lines`.
	//
	// See lint/walk.go.
	lines := strings.SplitAfter(strings.Clone(content), "\n")

	file := File{
		NormedExt: ext, Format: format, RealExt: filepath.Ext(path),
		BaseStyles: baseStyles, Checks: checks, Lines: lines, Content: content,
		Comments: make(map[string]bool), history: make(map[string]int),
		simple: config.Flags.Simple, Transform: transform,
		limits: make(map[string]int), Path: path, Metrics: make(map[string]int),
		NLP:    nlp.Info{Endpoint: config.NLPEndpoint, Lang: lang},
		Lookup: lookup, NormedPath: normed,
	}

	return &file, nil
}

// SortedAlerts returns all of f's alerts sorted by line and column.
func (f *File) SortedAlerts() []Alert {
	sort.Sort(ByPosition(f.Alerts))
	return f.Alerts
}

// ComputeMetrics returns all of f's metrics.
func (f *File) ComputeMetrics() (map[string]interface{}, error) {
	params := map[string]interface{}{}

	doc := summarize.NewDocument(f.Summary.String())
	if doc.NumWords == 0 {
		return params, nil
	}

	for k, v := range f.Metrics {
		if strings.HasPrefix(k, "table") {
			continue
		}
		k = strings.ReplaceAll(k, ".", "_")
		params[k] = float64(v)
	}

	params["complex_words"] = doc.NumComplexWords
	params["long_words"] = doc.NumLongWords
	params["paragraphs"] = doc.NumParagraphs - 1
	params["sentences"] = doc.NumSentences
	params["characters"] = doc.NumCharacters
	params["words"] = doc.NumWords
	params["polysyllabic_words"] = doc.NumPolysylWords
	params["syllables"] = doc.NumSyllables

	return params, nil
}

// FindLoc calculates the line and span of an Alert.
func (f *File) FindLoc(ctx, s string, pad, count int, a Alert) (int, []int) {
	var length int
	var lines []string

	for _, s := range a.Offset {
		ctx, _ = Substitute(ctx, s, '@')
	}

	pos, substring := initialPosition(ctx, s, a)
	if pos < 0 {
		// Shouldn't happen ...
		return pos, []int{0, 0}
	}

	loc := a.Span
	if f.Format == "markup" && !f.simple || f.Format == "fragment" {
		lines = f.Lines
	} else {
		lines = strings.SplitAfter(ctx, "\n")
	}

	counter := 0
	for idx, l := range lines {
		length = nlp.StrLen(l)
		if (counter + length) >= pos {
			loc[0] = (pos - counter) + pad
			loc[1] = loc[0] + nlp.StrLen(substring) - 1
			extent := length + pad
			if loc[1] > extent {
				loc[1] = extent
			} else if loc[1] <= 0 {
				loc[1] = 1
			}
			return count - (len(lines) - (idx + 1)), loc
		}
		counter += length
	}

	return count, loc
}

func (f *File) assignLoc(ctx string, blk nlp.Block, pad int, a Alert) (int, []int) {
	loc := a.Span
	for idx, l := range strings.SplitAfter(ctx, "\n") {
		if loc[0] < 0 || loc[1] < 0 {
			continue
		}
		// NOTE: This fixes #473, but the real issue is that `blk.Line` is
		// wrong. This seems related to `location.go#41`, but I'm not sure.
		//
		// At the very least, this change includes a representative test case
		// and a temporary fix.
		exact := len(l) > loc[1] && l[loc[0]:loc[1]] == a.Match
		if exact || idx == blk.Line {
			length := nlp.StrLen(l)
			pos, substring := initialPosition(l, blk.Text, a)

			loc[0] = pos + pad
			loc[1] = pos + nlp.StrLen(substring) - 1

			extent := length + pad
			if loc[1] > extent {
				loc[1] = extent
			} else if loc[1] <= 0 {
				loc[1] = 1
			}

			return idx + 1, loc
		}
	}
	return blk.Line + 1, a.Span
}

// locFromByteOffset computes a 1-based line number and a [col, col+len] span
// from absolute byte offsets into the raw document text. This avoids the
// text-search approach used by FindLoc/initialPosition, which can report the
// wrong location when the matched text appears more than once.
func locFromByteOffset(ctx string, begin, end, pad int) (int, []int) {
	line := 1
	lineStart := 0

	for i := 0; i < begin && i < len(ctx); i++ {
		if ctx[i] == '\n' {
			line++
			lineStart = i + 1
		}
	}

	col := nlp.StrLen(ctx[lineStart:begin]) + 1 + pad
	matchLen := nlp.StrLen(ctx[begin:end])

	span := []int{col, col + matchLen - 1}
	if span[1] <= 0 {
		span[1] = 1
	}

	return line, span
}

// SetText updates the file's content, lines, and history.
func (f *File) SetText(s string) {
	f.Content = s
	f.Lines = strings.SplitAfter(s, "\n")
	f.history = map[string]int{}
}

// SetNormedExt sets the normalized extension of a File.
func (f *File) SetNormedExt(ext string) {
	f.NormedExt = "." + ext
}

// AddAlert calculates the in-text location of an Alert and adds it to a File.
func (f *File) AddAlert(a Alert, blk nlp.Block, lines, pad int, lookup bool) {
	ctx := blk.Context
	if old, ok := f.ChkToCtx[a.Check]; ok {
		ctx = old
	}

	// When the alert carries byte offsets from a script rule and falls within
	// the document, compute line:column directly from those offsets instead of
	// performing a text search. This fixes incorrect position reporting for
	// script rules with `scope: raw` when the matched text appears more than
	// once.
	//
	// We use blk.Context (the original document) rather than ctx, which may
	// have been modified by ChkToCtx substitutions from earlier alerts.
	if a.HasByteOffsets && a.Span[0] >= 0 && a.Span[1] <= len(blk.Context) {
		a.Line, a.Span = locFromByteOffset(blk.Context, a.Span[0], a.Span[1], pad)
	} else {
		// NOTE: If the `ctx` document is large (as could be the case with
		// `scope: raw`) this is *slow*. Thus, the cap at 1k.
		//
		// TODO: Actually fix this.
		if len(a.Offset) == 0 && strings.Count(ctx, a.Match) > 1 && len(ctx) < 1000 {
			a.Offset = append(a.Offset, strings.Fields(ctx[0:a.Span[0]])...)
		}

		if !lookup {
			a.Line, a.Span = f.assignLoc(ctx, blk, pad, a)
		}
		if (!lookup && a.Span[0] < 0) || lookup {
			a.Line, a.Span = f.FindLoc(ctx, blk.Text, pad, lines, a)
		}
	}

	if a.Span[0] > 0 {
		f.ChkToCtx[a.Check], _ = Substitute(ctx, a.Match, '#')
		if !a.Hide {
			// Ensure that we're not double-reporting an Alert:
			entry := strings.Join([]string{
				strconv.Itoa(a.Line),
				strconv.Itoa(a.Span[0]),
				a.Check}, "-")

			if _, found := f.history[entry]; !found {
				// Check rule-assigned limits for reporting:
				count, occur := f.limits[a.Check]
				if (!occur || a.Limit == 0) || count < a.Limit {
					f.Alerts = append(f.Alerts, a)

					f.history[entry] = 1
					if a.Limit > 0 {
						f.limits[a.Check]++
					}
				}
			}
		}
	}
}

// UpdateComments sets a new status based on comment.
func (f *File) UpdateComments(comment string) {
	if comment == "vale off" { //nolint:gocritic
		f.Comments["off"] = true
	} else if comment == "vale on" {
		f.Comments["off"] = false
	} else if commentControlMatchesRE.MatchString(comment) {
		check := commentControlMatchesRE.FindStringSubmatch(comment)
		if len(check) == 4 {
			var parts []string
			if err := json.Unmarshal([]byte(check[2]), &parts); err == nil {
				for i := range parts {
					f.Comments[check[1]+"["+parts[i]+"]"] = check[3] == "NO"
				}
			}
		}
	} else if commentControlRE.MatchString(comment) {
		check := commentControlRE.FindStringSubmatch(comment)
		if len(check) == 3 {
			f.Comments[check[1]] = (check[2] == "NO" || check[2] == "off")
		}
	} else if commentStyleRE.MatchString(comment) {
		for _, style := range f.BaseStyles {
			f.Comments[style] = true
		}
		check := commentStyleRE.FindStringSubmatch(comment)
		for _, style := range strings.Split(check[1], ", ") {
			f.Comments[style] = false
		}
	}
}

// QueryComments checks if there has been an in-text comment for this check.
func (f *File) QueryComments(check string) bool {
	if f.Comments["off"] {
		return true
	}
	if style, _, ok := strings.Cut(check, "."); ok {
		if status := f.Comments[style]; status {
			return true
		}
	}
	if status := f.Comments[check]; status {
		return true
	}
	return false
}

// ResetComments resets the state of all checks back to active.
func (f *File) ResetComments() {
	for check := range f.Comments {
		if check != "off" {
			f.Comments[check] = false
		}
	}
}

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.

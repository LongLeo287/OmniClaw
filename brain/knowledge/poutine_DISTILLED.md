---
id: poutine
type: knowledge
owner: OA_Triage
---
# poutine
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
[![OpenSSF Best Practices](https://www.bestpractices.dev/projects/8787/badge)](https://www.bestpractices.dev/projects/8787)
[![OpenSSF Scorecard](https://api.securityscorecards.dev/projects/github.com/boostsecurityio/poutine/badge)](https://securityscorecards.dev/viewer/?uri=github.com/boostsecurityio/poutine)
![build](https://github.com/boostsecurityio/poutine/actions/workflows/build_test.yml/badge.svg)
![CodeQL](https://github.com/boostsecurityio/poutine/actions/workflows/codeql.yml/badge.svg)
[![Go Reference](https://pkg.go.dev/badge/github.com/boostsecurityio/poutine/v4.svg)](https://pkg.go.dev/github.com/boostsecurityio/poutine)
[![Go Report Card](https://goreportcard.com/badge/github.com/boostsecurityio/poutine)](https://goreportcard.com/report/github.com/boostsecurityio/poutine)
[![SLSA 3](https://slsa.dev/images/gh-badge-level3.svg)](https://slsa.dev)

[![View site - GH Pages](https://img.shields.io/badge/View_site-GH_Pages-2ea44f?style=for-the-badge)](https://boostsecurityio.github.io/poutine/)

# `poutine`

Created by [BoostSecurity.io](https://boostsecurity.io), `poutine` is a security scanner that detects misconfigurations and vulnerabilities in the build pipelines of a repository. It supports parsing CI workflows from GitHub Actions and Gitlab CI/CD. When given an access token with read-level access, `poutine` can analyze all the repositories of an organization to quickly gain insights into the security posture of the organization's software supply chain.

<table>
<td>

![Finding raised by poutine about "Arbitrary Code Execution from Untrusted Code Changes"](https://github.com/boostsecurityio/poutine/assets/172889/ca031a4f-afd8-4e3f-9e66-a2502bd0379b)

</td>
</table>

See the [documentation](docs/content/en/rules) for a list of rules currently supported by `poutine`.

## Why `poutine`?

In French, the word "poutine", when not referring to the [dish](https://en.wikipedia.org/wiki/Poutine), can be used to mean "messy". Inspired by the complexity and intertwined dependencies of modern open-source projects, `poutine` reflects both a nod to our Montreal roots and the often messy, complex nature of securing software supply chains.

## Supported Platforms

- GitHub Actions
- Gitlab Pipelines
- Azure DevOps
- Pipelines As Code Tekton

## Getting Started

### Installation

To install `poutine`, download the latest release from the [releases page](https://github.com/boostsecurityio/poutine/releases) and add the binary to your $PATH. 

<!-- TODO: cosign verify instructions? -->

#### Homebrew
``` bash
brew install poutine
```

#### Docker
``` bash
docker run -e GH_TOKEN ghcr.io/boostsecurityio/poutine:latest
```

#### GitHub Actions
```yaml
...
jobs:
  poutine:
    runs-on: ubuntu-latest
    permissions:
      security-events: write
      contents: read
    steps:
    - uses: actions/checkout@b4ffde65f46336ab88eb53be808477a3936bae11 # v4.1.1
#################################################################################################
    - name: poutine - GitHub Actions SAST
      uses: boostsecurityio/poutine-action@main # We recommend to use a tagged version and pin it
#################################################################################################
    - name: Upload poutine SARIF file
      uses: github/codeql-action/upload-sarif@4355270be187e1b672a7a1c7c7bae5afdc1ab94a # v3.24.10
      with:
        sarif_file: results.sarif
```

### Usage
``` bash
poutine [command] [arguments] [options]
```

#### Analyze a local repository

``` bash
poutine analyze_local .
```

#### Analyze a remote GitHub repository

```bash
poutine analyze_repo org/repo --token "$GH_TOKEN"
```

#### Analyze all repositories in a GitHub organization

```bash
poutine analyze_org org --token "$GH_TOKEN"
```


#### Analyze all projects in a self-hosted Gitlab instance

``` bash
poutine analyze_org my-org/project --token "$GL_TOKEN" --scm gitlab --scm-base-url https://gitlab.example.com
```

### Configuration Options

```
--token              SCM access token (required for the commands analyze_repo, analyze_org) (env: GH_TOKEN)
--format             Output format (default: pretty, json, sarif)
--ignore-forks       Ignore forked repositories in the organization (analyze_org)
--scm                SCM platform (default: github, gitlab)
--scm-base-url       Base URI of the self-hosted SCM instance
--threads            Number of threads to use (default: 2)
--config             Path to the configuration file (default: .poutine.yml)
--skip               Add rules to the skip list for the current run (can be specified multiple times)
--verbose            Enable debug logging
--fail-on-violation  Exit with a non-zero code (10) when violations are found
```

See [.poutine.sample.yml](.poutine.sample.yml) for an example configuration file.

### Custom Rules

`poutine` supports custom Rego rules to extend its security scanning capabilities. You can write your own rules and include them at runtime.

#### Configuration

Create a `.poutine.yml` configuration file in your current working directory, or use a custom path with the `--config` flag:

```bash
poutine analyze_local . --config my-config.yml
```

In your configuration file, specify the path(s) to your custom rules using the `include` directive:

```yaml
include:
  - path: ./custom_rules
  - path: ./github_actions
```

#### Writing Custom Rules

Custom Rego rules must:
1. Be saved as `*.rego` files in the included directory
2. Follow the package naming convention: `package rules.<rule_name>`
3. Define a `rule` variable with metadata
4. Define a `results` set containing findings

**Example custom rule:**

```rego
package rules.custom_injection

import data.poutine
import rego.v1

# METADATA
# title: Custom Injection Detection
# description: Detects potential injection vulnerabilities in workflows
# custom:
#   level: warning

rule := poutine.rule(rego.metadata.chain())

# Define pattern to detect (properly escaped for Rego)
patterns.github contains `\\$\\{\\{[^\\}]+\\}\\}`

results contains poutine.finding(rule, pkg.purl, {
  "path": workflow.path,
  "line": step.lines.run,
  "job": job.id,
  "step": i,
  "details": "Potential injection found in step",
}) if {
  pkg := input.packages[_]
  workflow := pkg.github_actions_workflows[_]
  job := workflow.jobs[_]
  step := job.steps[i]
  step.run  # Ensure step has a run command
  regex.match(patterns.github[_], step.run)
}
```

**Key points:**
- Use `import data.poutine` and `import rego.v1` for modern Rego syntax and poutine utilities
- Use `rule := poutine.rule(rego.metadata.chain())` to extract metadata from METADATA comments
- The `package` name determines the rule identifier (e.g., `package rules.custom_injection` → rule ID: `custom_injection`)
- Add METADATA comments to describe the rule with `title`, `description`, and `level`
- Set the severity `level` to `note`, `warning`, or `error`
- Use `poutine.finding(rule, pkg.purl, {...})` to create findings that match the poutine schema
- The `results` set should contain findings with fields like `path`, `line`, `job`, `step`, `details`

For more examples, see:
- [poutine-rules repository](https://github.com/boost-rnd/poutine-rules) - External rule examples
- Built-in rules in [opa/rego/rules/](./opa/rego/rules/) directory
- [.poutine.sample.yml](.poutine.sample.yml) - Configuration examples

### Acknowledging Findings

`poutine` supports skipping (acknowledging) specific findings that are not relevant in your context. This can be useful when:
- A finding is a false positive
- The security concern has been addressed through other means (e.g., hardened self-hosted runners)
- You've accepted the risk for a particular finding

To acknowledge findings, you can either:
1. Add a `skip` section to your `.poutine.yml` configuration file
2. Use the `--skip` command-line flag (e.g., `--skip rule_name`) for one-time skipping

#### Configuration File

Add a `skip` section to your `.poutine.yml` configuration file. Each skip rule can filter findings by:
- `job`: Filter by job name
- `level`: Filter by severity level (note, warning, error)
- `path`: Filter by workflow file path
- `rule`: Filter by rule name
- `purl`: Filter by package URL
- `osv_id`: Filter by OSV ID

Example configuration:

```yaml
skip:
  # Skip all note-level findings
  - level: note

  # Skip findings in a specific workflow
  - path: .github/workflows/safe.yml

  # Skip a specific rule everywhere
  - rule: unpinnable_action

  # Skip a rule for specific workflows
  - rule: pr_runs_on_self_hosted
    path:
      - .github/workflows/pr.yml
      - .github/workflows/deploy.yml

  # Skip findings for specific packages
  - rule: github_action_from_unverified_creator_used
    purl:
      - pkg:githubactions/dorny/paths-filter
```

For more examples, see [.poutine.sample.yml](.poutine.sample.yml).

#### Command Line

You can also skip rules on the command line using the `--skip` flag. Note that the command-line flag only supports skipping rules by name globally and does not support the granular filtering options (job, path, level, etc.) available in the configuration file.

```bash
# Skip a single rule globally
poutine analyze_repo org/repo --skip unpinnable_action

# Skip multiple rules globally
poutine analyze_repo org/repo --skip unpinnable_action --skip pr_runs_on_self_hosted
```

This is useful for one-time analysis or when you want to temporarily ignore specific rules without modifying your configuration file. For more granular control (e.g., skipping a rule only in specific workflows), use the configuration file instead.

## AI Coding Assistant Integration (MCP)

`poutine` can be integrated with AI coding assistants like Claude Code, Gemini, etc. through the Model Context Protocol (MCP). This allows AI assistants to analyze repositories and validate CI/CD pipelines directly from your development environment.

For detailed setup instructions for your specific AI coding tool, see the [MCP Integration Guide](MCP_INTEGRATION.md).

## Building from source

Building `poutine` requires Go 1.26+.

```bash
git clone https://github.com/boostsecurityio/poutine.git
cd poutine
make build
```

## Development
### Updating Build Platform CVE Database
```bash
go test -tags build_platform_vuln_database ./...
opa fmt -w opa/rego/external/build_platform.rego
```

## See Also 

For examples of vulnerabilities in GitHub Actions workflows, you can explore the [Messy poutine GitHub organization](https://github.com/messypoutine). It showcases real-world vulnerabilities from open-source projects readily exploitable for educational purposes. 

To get started with some hints, try using `poutine` to analyze the `messypoutine` organization:
``` bash
poutine analyze_org messypoutine --token `gh auth token`
```

You may submit the flags you find in a [private vulnerability disclosure](https://github.com/messypoutine/.github/security/advisories/new).

## License

This project is licensed under the Apache License 2.0 - see the LICENSE file for details.

```

### File: .goreleaser.yaml
```yaml
version: 2
project_name: poutine

before:
  hooks:
    - go mod verify

builds:
  - env:
      - CGO_ENABLED=0
    goos:
      - linux
      - darwin
    goarch:
      - amd64
      - arm64
      - arm
    flags:
      - -trimpath
    ldflags:
      - -s -w -X main.version={{.Version}} -X main.commit={{.Commit}} -X main.date={{.Date}} -X main.builtBy=goreleaser
    goarm:
      - '7'

kos:
  - repository: ghcr.io/boostsecurityio/poutine
    base_image: 'cgr.dev/chainguard/git:latest@sha256:06119871a608d163eac2daddd0745582e457a29ee8402bd351c13f294ede30e1'
    tags:
      - '{{.Version}}'
      - latest
    bare: true
    preserve_import_paths: false
    platforms:
      - linux/amd64
      - linux/arm64

docker_signs:
  - artifacts: manifests
    args:
      - "sign"
      - "${artifact}"
      - "--yes" # skip user interaction

signs:
  - cmd: cosign
    certificate: '${artifact}.pem'
    args:
      - "sign-blob"
      - "--output-certificate=${certificate}"
      - "--output-signature=${signature}"
      - "${artifact}"
      - "--yes" # skip user interaction
    artifacts: all
    output: true

archives:
  - format: tar.gz
    # this name template makes the OS and Arch compatible with the results of `uname`.
    name_template: >-
      {{ .ProjectName }}_
      {{- title .Os }}_
      {{- if eq .Arch "amd64" }}x86_64
      {{- else if eq .Arch "386" }}i386
      {{- else }}{{ .Arch }}{{ end }}
      {{- if .Arm }}v{{ .Arm }}{{ end }}
    # use zip for windows archives
    format_overrides:
      - goos: windows
        format: zip

changelog:
  use: github-native
  sort: asc
  filters:
    exclude:
      - "^docs:"
      - "^test:"

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
conduct@openssf.org.
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

### File: CONTRIBUTING.md
```md
# Contributing to Poutine

Thank you for your interest in contributing to `poutine`! We value the contributions of our community members and look forward to your input.

## Code of Conduct

Before you start contributing, please make sure to read and abide by our [Code of Conduct](./CODE_OF_CONDUCT.md). Additionally, we follow the Linux Foundation's guidelines for commit sign-offs. Please sign off your commits using the `-s` or `--signoff` flag.

## Getting Started

### Environment Setup

To contribute to Poutine, you'll need the following:

- [Go toolchain v1.24](https://golang.org/dl/) or higher.

### Contributing Process

1. **Find an Issue or Feature**: Check our [Roadmap](https://github.com/orgs/boostsecurityio/projects/2) or open [GitHub Issues](https://github.com/boostsecurityio/poutine/issues). Pick an existing issue or propose your feature request there.

2. **Get Approval**: For new features, wait for the issue to be labeled `Approved` by the maintainers.

3. **Fork and Code**: Fork the repository, make your changes, and ensure your code adheres to the provided coding conventions and quality standards.

4. **Submit a Pull Request (PR)**: Once you've completed your changes, submit a PR. Make sure your PR title and description clearly describe the changes. Include the issue number your PR addresses.

### Testing and Linting

- Run `gofmt` to ensure your code is properly formatted.
- Include any tests relevant to the bug or feature you are addressing.

### Documentation

- Update the `README.md` if you introduce or modify any commands.
- If your changes involve adding or altering rules, update the corresponding markdown file in `docs/content/en/rules/[RULE_ID].md`.

## Community and Questions

Currently, we handle all communications through GitHub issues and pull requests. If you have questions or need help with the setup, please open an issue and tag it as a question.

```

### File: dagger.json
```json
{
  "name": "poutine",
  "sdk": "go",
  "source": "dagger",
  "engineVersion": "v0.11.6"
}

```

### File: MAINTAINERS.md
```md
# Maintainers

## `poutine-maintainers`

In alphabetical order:
- Alexis-Maurer Fortin ([@SUSTAPLE117](https://github.com/SUSTAPLE117)), BoostSecurity.io
- François Proulx ([@fproulx-boostsecurity](https://github.com/fproulx-boostsecurity)), BoostSecurity.io

```

### File: MCP_INTEGRATION.md
```md
# Poutine MCP Server Integration Guide

The Poutine MCP (Model Context Protocol) server allows AI coding assistants to analyze repositories and CI/CD pipelines for security vulnerabilities directly from your development environment.

## Prerequisites

1. **Install Poutine**: Follow the [installation guide](README.md) to install Poutine
2. **GitHub Authentication**: Set up GitHub CLI authentication
   ```bash
   gh auth login
   ```
3. **Set GitHub Token Environment Variable**: Before launching your AI coding assistant, export the GitHub token:
   ```bash
   export GH_TOKEN=$(gh auth token)
   ```

   The Poutine MCP server will automatically pick up the `GH_TOKEN` environment variable from your shell session.

## Setup

### Claude Code

```bash
claude mcp add poutine poutine mcp-server
```

### Gemini CLI

```bash
gemini mcp add poutine poutine mcp-server
```

### Other MCP-Compatible Clients

Add the following configuration to your MCP-compatible AI coding assistant:

```json
"mcpServers": {
  "poutine": {
    "type": "stdio",
    "command": "poutine",
    "args": [
      "mcp-server"
    ],
  }
}
```

**Note**: The Poutine MCP server will automatically pick up the `GH_TOKEN` environment variable from your shell session. Make sure you've set it (see Prerequisites) before launching your AI coding assistant.

## Available MCP Tools

Once configured, the following tools are available to your AI assistant:

### `analyze_org`
Scan all repositories in a GitHub/GitLab organization.

**Parameters:**
- `org` (required): Organization name
- `scm_provider` (optional): "github" or "gitlab" (default: "github")
- `scm_base_url` (optional): Base URL for self-hosted instances
- `threads` (optional): Number of parallel threads (default: 2)
- `ignore_forks` (optional): Skip forked repositories (default: false)

### `analyze_repo`
Scan a specific repository.

**Parameters:**
- `repo` (required): Repository name in format "org/repo"
- `scm_provider` (optional): "github" or "gitlab" (default: "github")
- `scm_base_url` (optional): Base URL for self-hosted instances
- `ref` (optional): Git branch or commit to analyze (default: "HEAD")

### `analyze_local`
Scan a local repository by file path.

**Parameters:**
- `path` (required): Local file system path to the repository

### `analyze_repo_stale_branches`
Scan repository branches for `pull_request_target` vulnerabilities.

**Parameters:**
- `repo` (required): Repository name in format "org/repo"
- `scm_provider` (optional): "github" or "gitlab" (default: "github")
- `scm_base_url` (optional): Base URL for self-hosted instances
- `threads` (optional): Number of parallel threads (default: 5)
- `expand` (optional): Expand output to full format (default: false)
- `regex` (optional): Regex pattern for workflow matching (default: "pull_request_target")

### `analyze_manifest`
Analyze CI/CD pipeline manifest content for security issues.

**Parameters:**
- `content` (required): The complete YAML manifest content
- `manifest_type` (required): Type of manifest - "github-actions", "gitlab-ci", "azure-pipelines", or "tekton"

**Note**: This tool is automatically called when AI assistants generate or modify CI/CD workflows to ensure security best practices.

## Example AI Assistant Prompts

Here are some example prompts you can use with your AI coding assistant:

**Organization-wide scan:**
```
Use Poutine to scan all repositories in the <your_org> organization
```

**Single repository analysis:**
```
Analyze the security of the repository actions/checkout
```

**Local repository scan:**
```
Scan the repository at /Users/me/projects/myapp for supply chain vulnerabilities
```

**Stale branch analysis:**
```
Check the myorg/myrepo repository for pull_request_target vulnerabilities in stale branches
```

**Workflow generation with automatic security validation:**
```
Create a GitHub Actions workflow that runs tests on pull requests
```
*(The AI will automatically use `analyze_manifest` to validate the generated workflow)*

## Additional Resources

- [Model Context Protocol Specification](https://spec.modelcontextprotocol.io/)
- [Poutine Documentation](README.md)
- [Claude Code MCP Guide](https://docs.claude.com/en/docs/claude-code/mcp)
- [Gemini CLI MCP Guide](https://github.com/google-gemini/gemini-cli/blob/main/docs/tools/mcp-server.md)

```

### File: poutine.go
```go
package main

import (
	"github.com/boostsecurityio/poutine/cmd"
)

var (
	version = "development"
	commit  = "none"
	date    = "unknown"
)

func main() {
	cmd.Commit = commit
	cmd.Version = version
	cmd.Date = date
	cmd.Execute()
}

```

### File: analyze\analyze.go
```go
// Package analyze can analyze things.
package analyze

import (
	"context"
	"errors"
	"fmt"
	"io"
	"os"
	"path/filepath"
	"regexp"
	"strings"
	"sync"
	"time"

	"github.com/boostsecurityio/poutine/models"
	"github.com/boostsecurityio/poutine/results"
	"golang.org/x/sync/semaphore"

	"github.com/boostsecurityio/poutine/opa"
	"github.com/boostsecurityio/poutine/providers/pkgsupply"
	scm_domain "github.com/boostsecurityio/poutine/providers/scm/domain"
	"github.com/boostsecurityio/poutine/scanner"
	"github.com/rs/zerolog/log"
	"github.com/schollz/progressbar/v3"
)

const TEMP_DIR_PREFIX = "poutine-*"

type Repository interface {
	GetProviderName() string
	GetRepoIdentifier() string
	GetIsFork() bool
	BuildGitURL(baseURL string) string
	GetHasIssues() bool
	GetHasWiki() bool
	GetHasDiscussion() bool
	GetOpenIssuesCount() int
	GetForksCount() int
	GetStarsCount() int
	GetPrimaryLanguage() string
	GetSize() int
	GetDefaultBranch() string
	GetLicense() string
	GetIsTemplate() bool
	GetOrganizationID() int
	GetRepositoryID() int
	GetIsEmpty() bool
}

type RepoBatch struct {
	TotalCount   int
	Repositories []Repository
	Err          error
}

type ScmClient interface {
	GetOrgRepos(ctx context.Context, org string) <-chan RepoBatch
	GetRepo(ctx context.Context, org string, name string) (Repository, error)
	GetToken() string
	GetProviderName() string
	GetProviderVersion(ctx context.Context) (string, error)
	GetProviderBaseURL() string
	ParseRepoAndOrg(string) (string, string, error)
}

type GitClient interface {
	Clone(ctx context.Context, clonePath string, url string, token string, ref string) error
	FetchCone(ctx context.Context, clonePath string, url string, token string, ref string, cone string) error
	CommitSHA(clonePath string) (string, error)
	LastCommitDate(ctx context.Context, clonePath string) (time.Time, error)
	GetRemoteOriginURL(ctx context.Context, repoPath string) (string, error)
	GetRepoHeadBranchName(ctx context.Context, repoPath string) (string, error)
	GetUniqWorkflowsBranches(ctx context.Context, clonePath string) (map[string][]models.BranchInfo, error)
	BlobMatches(ctx context.Context, clonePath string, blobsha string, regex *regexp.Regexp) (bool, []byte, error)
	ListFiles(clonePath string, extensions []string) (map[string][]byte, error)
	Cleanup(clonePath string)
}

func NewAnalyzer(scmClient ScmClient, gitClient GitClient, formatter Formatter, config *models.Config, opaClient *opa.Opa) *Analyzer {
	if config == nil {
		config = &models.Config{}
	}
	return &Analyzer{
		ScmClient: scmClient,
		GitClient: gitClient,
		Formatter: formatter,
		Config:    config,
		Opa:       opaClient,
	}
}

type Analyzer struct {
	ScmClient ScmClient
	GitClient GitClient
	Formatter Formatter
	Config    *models.Config
	Opa       *opa.Opa
}

func (a *Analyzer) AnalyzeOrg(ctx context.Context, org string, numberOfGoroutines *int) ([]*models.PackageInsights, error) {
	provider := a.ScmClient.GetProviderName()

	providerVersion, err := a.ScmClient.GetProviderVersion(ctx)
	if err != nil {
		log.Debug().Err(err).Msgf("Failed to get provider version for %s", provider)
	}

	log.Debug().Msgf("Provider: %s, Version: %s, BaseURL: %s", provider, providerVersion, a.ScmClient.GetProviderBaseURL())

	log.Debug().Msgf("Fetching list of repositories for organization: %s on %s", org, provider)
	orgReposBatches := a.ScmClient.GetOrgRepos(ctx, org)

	pkgsupplyClient := pkgsupply.NewStaticClient()
	inventory := scanner.NewInventory(a.Opa, pkgsupplyClient, provider, providerVersion)

	log.Debug().Msgf("Starting repository analysis for organization: %s on %s", org, provider)
	bar := a.ProgressBar(0, "Analyzing repositories")

	var reposWg sync.WaitGroup
	errChan := make(chan error, 1)
	maxGoroutines := 2
	if numberOfGoroutines != nil {
		maxGoroutines = *numberOfGoroutines
	}
	goRoutineLimitSem := semaphore.NewWeighted(int64(maxGoroutines))

	scannedPackages := make([]*models.PackageInsights, 0)

	pkgChan := make(chan *models.PackageInsights)
	pkgWg := sync.WaitGroup{}
	pkgWg.Add(1)
	go func() {
		defer pkgWg.Done()
		for pkg := range pkgChan {
			scannedPackages = append(scannedPackages, pkg)
		}
	}()

	for repoBatch := range orgReposBatches {
		if repoBatch.Err != nil {
			log.Error().Err(repoBatch.Err).Msg("failed to fetch batch of repos, skipping batch")
			continue
		}
		if repoBatch.TotalCount != 0 {
			bar.ChangeMax(repoBatch.TotalCount)
		}

		for _, repo := range repoBatch.Repositories {
			if a.Config.IgnoreForks && repo.GetIsFork() {
				bar.ChangeMax(repoBatch.TotalCount - 1)
				continue
			}
			if repo.GetSize() == 0 {
				bar.ChangeMax(repoBatch.TotalCount - 1)
				log.Info().Str("repo", repo.GetRepoIdentifier()).Msg("Skipping empty repository")
				continue
			}
			if err := goRoutineLimitSem.Acquire(ctx, 1); err != nil {
				close(errChan)
				return scannedPackages, fmt.Errorf("failed to acquire semaphore: %w", err)
			}

			reposWg.Add(1)
			go func(repo Repository) {
				defer goRoutineLimitSem.Release(1)
				defer reposWg.Done()
				repoNameWithOwner := repo.GetRepoIdentifier()
				repoKey, err := a.cloneRepo(ctx, repo.BuildGitURL(a.ScmClient.GetProviderBaseURL()), a.ScmClient.GetToken(), "HEAD")
				if err != nil {
					log.Error().Err(err).Str("repo", repoNameWithOwner).Msg("failed to clone repo")
					return
				}
				defer a.GitClient.Cleanup(repoKey)

				pkg, err := a.GeneratePackageInsights(ctx, repoKey, repo, "HEAD")
				if err != nil {
					log.Error().Err(err).Str("repo", repoNameWithOwner).Msg("failed to generate package insights")
					return
				}

				files, err := a.GitClient.ListFiles(repoKey, []string{".yml", ".yaml"})
				if err != nil {
					log.Error().Err(err).Str("repo", repoNameWithOwner).Msg("failed to list files")
					return
				}

				memScanner := &scanner.InventoryScannerMem{
					Files: files,
					Parsers: []scanner.MemParser{
						scanner.NewGithubActionsMetadataParser(),
						scanner.NewGithubActionWorkflowParser(),
						scanner.NewAzurePipelinesParser(),
						scanner.NewGitlabCiParser(),
						scanner.NewPipelineAsCodeTektonParser(),
					},
				}

				scannedPkg, err := inventory.ScanPackageScanner(ctx, *pkg, memScanner)
				if err != nil {
					log.Error().Err(err).Str("repo", repoNameWithOwner).Msg("failed to scan package")
					return
				}

				select {
				case pkgChan <- scannedPkg:
				case <-ctx.Done():
					log.Error().Msg("Context canceled while sending package to channel")
					return
				}
				_ = bar.Add(1)
			}(repo)
		}
	}

	go func() {
		reposWg.Wait()
		close(pkgChan)
		close(errChan)
	}()

	pkgWg.Wait()

	for err := range errChan {
		if err != nil {
			return scannedPackages, err
		}
	}

	_ = bar.Finish()

	err = a.finalizeAnalysis(ctx, scannedPackages)
	if err != nil {
		return scannedPackages, err
	}

	return scannedPackages, nil
}

func (a *Analyzer) AnalyzeStaleBranches(ctx context.Context, repoString string, numberOfGoroutines *int, expand *bool, regex *regexp.Regexp) (*models.PackageInsights, error) {
	org, repoName, err := a.ScmClient.ParseRepoAndOrg(repoString)
	if err != nil {
		return nil, fmt.Errorf("failed to parse repository: %w", err)
	}
	repo, err := a.ScmClient.GetRepo(ctx, org, repoName)
	if err != nil {
		return nil, fmt.Errorf("failed to get repo: %w", err)
	}
	provider := repo.GetProviderName()

	providerVersion, err := a.ScmClient.GetProviderVersion(ctx)
	if err != nil {
		log.Debug().Err(err).Msgf("Failed to get provider version for %s", provider)
	}

	log.Debug().Msgf("Provider: %s, Version: %s, BaseURL: %s", provider, providerVersion, a.ScmClient.GetProviderBaseURL())

	pkgsupplyClient := pkgsupply.NewStaticClient()

	inventory := scanner.NewInventory(a.Opa, pkgsupplyClient, provider, providerVersion)

	log.Debug().Msgf("Starting repository analysis for: %s/%s on %s", org, repoName, provider)
	bar := a.ProgressBar(3, "Cloning repository")
	_ = bar.RenderBlank()

	repoUrl := repo.BuildGitURL(a.ScmClient.GetProviderBaseURL())
	repoKey, err := a.fetchCone(ctx, repoUrl, a.ScmClient.GetToken(), "refs/heads/*:refs/remotes/origin/*", ".github/workflows")
	if err != nil {
		return nil, fmt.Errorf("failed to fetch cone: %w", err)
	}
	defer a.GitClient.Cleanup(repoKey)

	bar.Describe("Listing unique workflows")
	_ = bar.Add(1)

	workflows, err := a.GitClient.GetUniqWorkflowsBranches(ctx, repoKey)
	if err != nil {
		return nil, fmt.Errorf("failed to get unique workflow: %w", err)
	}

	bar.Describe("Check which workflows match regex: " + regex.String())
	_ = bar.Add(1)

	errChan := make(chan error, 1)
	maxGoroutines := 5
	if numberOfGoroutines != nil {
		maxGoroutines = *numberOfGoroutines
	}
	sem := semaphore.NewWeighted(int64(maxGoroutines))
	m := sync.Mutex{}
	type file struct {
		path string
		data []byte
	}
	filesChan := make(chan *file)
	files := make(map[string][]byte)

	wgConsumer := sync.WaitGroup{}
	wgProducer := sync.WaitGroup{}

	wgConsumer.Add(1)
	go func() {
		defer wgConsumer.Done()
		for v := range filesChan {
			files[v.path] = v.data
		}
	}()
	blobShas := make([]string, 0, len(workflows))
	for sha := range workflows {
		blobShas = append(blobShas, sha)
	}
	for _, blobSha := range blobShas {
		if err := sem.Acquire(ctx, 1); err != nil {
			errChan <- fmt.Errorf("failed to acquire semaphore: %w", err)
			break
		}
		wgProducer.Add(1)
		go func(blobSha string) {
			defer wgProducer.Done()
			defer sem.Release(1)
			match, content, err := a.GitClient.BlobMatches(ctx, repoKey, blobSha, regex)
			if err != nil {
				errChan <- fmt.Errorf("failed to blob match %s: %w", blobSha, err)
				return
			}
			if match {
				filesChan <- &file{
					path: ".github/workflows/" + blobSha + ".yaml",
					data: content,
				}
			} else {
				m.Lock()
				delete(workflows, blobSha)
				m.Unlock()
			}
		}(blobSha)
	}
	wgProducer.Wait()
	close(errChan)
	close(filesChan)
	wgConsumer.Wait()
	for err := range errChan {
		return nil, err
	}

	bar.Describe("Scanning package")
	_ = bar.Add(1)
	pkg, err := a.GeneratePackageInsights(ctx, repoKey, repo, "HEAD")
	if err != nil {
		return nil, fmt.Errorf("failed to generate package insight: %w", err)
	}

	inventoryScanner := scanner.InventoryScannerMem{
		Files: files,
		Parsers: []scanner.MemParser{
			scanner.NewGithubActionWorkflowParser(),
		},
	}

	scannedPackage, err := inventory.ScanPackageScanner(ctx, *pkg, &inventoryScanner)
	if err != nil {
		return nil, fmt.Errorf("failed to scan package: %w", err)
	}

	_ = bar.Finish()
	if *expand {
		expanded := []results.Finding{}
		for _, finding := range scannedPackage.FindingsResults.Findings {
			filename := filepath.Base(finding.Meta.Path)
			blobsha := strings.TrimSuffix(filename, filepath.Ext(filename))
			purl, err := models.NewPurl(finding.Purl)
			if err != nil {
				log.Warn().Err(err).Str("purl", finding.Purl).Msg("failed to evaluate PURL, skipping")
				continue
			}
			for _, branchInfo := range workflows[blobsha] {
				for _, path := range branchInfo.FilePath {
					finding.Meta.Path = path
					purl.Version = branchInfo.BranchName
					finding.Purl = purl.String()
					expanded = append(expanded, finding)
				}
			}
		}
		scannedPackage.FindingsResults.Findings = expanded

		if err := a.Formatter.Format(ctx, []*models.PackageInsights{scannedPackage}); err != nil {
			return nil, fmt.Errorf("failed to finalize analysis of package: %w", err)
		}
	} else {
		results := make(map[string][]*models.RepoInfo, len(workflows))
		for blobsha, branchinfos := range workflows {
			results[blobsha] = []*models.RepoInfo{{
				RepoName:    repoName,
				Purl:        pkg.Purl,
				BranchInfos: branchinfos,
			}}
		}

		if err := a.Formatter.FormatWithPath(ctx, []*models.PackageInsights{scannedPackage}, results); err != nil {
			return nil, fmt.Errorf("failed to finalize analysis of package: %w", err)
		}

	}

	return scannedPackage, nil
}

func (a *Analyzer) AnalyzeRepo(ctx context.Context, repoString string, ref string) (*models.PackageInsights, error) {
	org, repoName, err := a.ScmClient.ParseRepoAndOrg(repoString)
	if err != nil {
		return nil, fmt.Errorf("failed to parse repository: %w", err)
	}
	repo, err := a.ScmClient.GetRepo(ctx, org, repoName)
	if err != nil {
		return nil, fmt.Errorf("failed to get repo: %w", err)
	}
	provider := repo.GetProviderName()

	providerVersion, err := a.ScmClient.GetProviderVersion(ctx)
	if err != nil {
		log.Debug().Err(err).Msgf("Failed to get provider version for %s", provider)
	}

	log.Debug().Msgf("Provider: %s, Version: %s, BaseURL: %s", provider, providerVersion, a.ScmClient.GetProviderBaseURL())

	pkgsupplyClient := pkgsupply.NewStaticClient()
	inventory := scanner.NewInventory(a.Opa, pkgsupplyClient, provider, providerVersion)

	log.Debug().Msgf("Starting repository analysis for: %s/%s on %s", org, repoName, provider)
	bar := a.ProgressBar(2, "Cloning repository")
	_ = bar.RenderBlank()

	repoKey, err := a.cloneRepo(ctx, repo.BuildGitURL(a.ScmClient.GetProviderBaseURL()), a.ScmClient.GetToken(), ref)
	if err != nil {
		return nil, err
	}
	defer a.GitClient.Cleanup(repoKey)

	bar.Describe("Analyzing repository")
	_ = bar.Add(1)

	pkg, err := a.GeneratePackageInsights(ctx, repoKey, repo, ref)
	if err != nil {
		return nil, err
	}

	files, err := a.GitClient.ListFiles(repoKey, []string{".yml", ".yaml"})
	if err != nil {
		return nil, fmt.Errorf("failed to list files: %w", err)
	}

	memScanner := &scanner.InventoryScannerMem{
		Files: files,
		Parsers: []scanner.MemParser{
			scanner.NewGithubActionsMetadataParser(),
			scanner.NewGithubActionWorkflowParser(),
			scanner.NewAzurePipelinesParser(),
			scanner.NewGitlabCiParser(),
			scanner.NewPipelineAsCodeTektonParser(),
		},
	}

	scannedPackage, err := inventory.ScanPackageScanner(ctx, *pkg, memScanner)
	if err != nil {
		return nil, err
	}
	_ = bar.Finish()

	err = a.finalizeAnalysis(ctx, []*models.PackageInsights{scannedPackage})
	if err != nil {
		return nil, err
	}

	return scannedPackage, nil
}

func (a *Analyzer) AnalyzeLocalRepo(ctx context.Context, repoPath string) (*models.PackageInsights, error) {
	org, repoName, err := a.ScmClient.ParseRepoAndOrg(repoPath)
	if err != nil {
		return nil, fmt.Errorf("failed to parse repository: %w", err)
	}
	repo, err := a.ScmClient.GetRepo(ctx, org, repoName)
	if err != nil {
		return nil, fmt.Errorf("failed to get repo: %w", err)
	}
	provider := repo.GetProviderName()

	providerVersion, err := a.ScmClient.GetProviderVersion(ctx)
	if err != nil {
		log.Debug().Err(err).Msgf("Failed to get provider version for %s", provider)
	}

	log.Debug().Msgf("Provider: %s, Version: %s, BaseURL: %s", provider, providerVersion, a.ScmClient.GetProviderBaseURL())

	pkgsupplyClient := pkgsupply.NewStaticClient()
	inventory := scanner.NewInventory(a.Opa, pkgsupplyClient, provider, providerVersion)

	log.Debug().Msgf("Starting repository analysis for: %s/%s on %s", org, repoName, provider)

	pkg, err := a.GeneratePackageInsights(ctx, repoPath, repo, "")
	if err != nil {
		return nil, err
	}

	scannedPackage, err := inventory.ScanPackage(ctx, *pkg, repoPath)
	if
... [TRUNCATED]
```

### File: analyze\analyze_test.go
```go
package analyze

import (
	"context"
	"fmt"
	"strings"
	"testing"

	"github.com/boostsecurityio/poutine/formatters/noop"
	"github.com/boostsecurityio/poutine/models"
	"github.com/boostsecurityio/poutine/opa"
	"github.com/stretchr/testify/assert"
	"github.com/stretchr/testify/require"
)

// newTestOpa creates an OPA client for testing
func newTestOpa(ctx context.Context) (*opa.Opa, error) {
	config := models.DefaultConfig()
	opaClient, err := opa.NewOpa(ctx, config)
	if err != nil {
		return nil, fmt.Errorf("failed to create opa client: %w", err)
	}
	return opaClient, nil
}

func TestAnalyzeManifestDirectly(t *testing.T) {
	ctx := context.Background()

	tests := []struct {
		name           string
		content        string
		manifestType   string
		expectedType   string
		validateResult func(t *testing.T, insights *models.PackageInsights)
	}{
		{
			name: "valid github actions workflow",
			content: `name: Test Workflow
on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Run tests
        run: echo "Running tests"`,
			manifestType: "github-actions",
			expectedType: "github-actions",
			validateResult: func(t *testing.T, insights *models.PackageInsights) {
				assert.Equal(t, "manifest", insights.SourceScmType)
				assert.Contains(t, insights.Purl, "pkg:generic/github-actions-workflow")
				assert.Equal(t, "YAML", insights.PrimaryLanguage)
				assert.Len(t, insights.GithubActionsWorkflows, 1, "Should detect GitHub Actions workflow")
			},
		},
		{
			name: "valid gitlab ci config",
			content: `stages:
  - build
  - test

variables:
  DOCKER_DRIVER: overlay2

build_job:
  stage: build
  script:
    - echo "Building application"

test_job:
  stage: test
  script:
    - echo "Running tests"`,
			manifestType: "gitlab-ci",
			expectedType: "gitlab-ci",
			validateResult: func(t *testing.T, insights *models.PackageInsights) {
				assert.Equal(t, "manifest", insights.SourceScmType)
				assert.Contains(t, insights.Purl, "pkg:generic/gitlab-ci-config")
				assert.Len(t, insights.GitlabciConfigs, 1, "Should detect GitLab CI config")
			},
		},
		{
			name: "vulnerable github actions workflow",
			content: `name: Vulnerable Workflow
on: pull_request_target

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@main
      - name: Vulnerable command
        run: |
          curl -fsSL https://example.com/script.sh | bash
          echo "${{ github.event.pull_request.title }}" | bash`,
			manifestType: "github-actions",
			expectedType: "github-actions",
			validateResult: func(t *testing.T, insights *models.PackageInsights) {
				assert.Contains(t, insights.Purl, "pkg:generic/github-actions-workflow")
				assert.Len(t, insights.GithubActionsWorkflows, 1, "Should detect workflow")

				workflow := insights.GithubActionsWorkflows[0]
				assert.Equal(t, "Vulnerable Workflow", workflow.Name)

				assert.Len(t, insights.FindingsResults.Findings, 3, "May have security findings for vulnerable workflow")
			},
		},
		{
			name: "azure pipelines config",
			content: `trigger:
  - main

pool:
  vmImage: ubuntu-latest

steps:
  - task: UseDotNet@2
    displayName: 'Install .NET'
    inputs:
      version: '6.0.x'

  - script: dotnet build
    displayName: 'Build application'`,
			manifestType: "azure-pipelines",
			expectedType: "azure-pipelines",
			validateResult: func(t *testing.T, insights *models.PackageInsights) {
				assert.Contains(t, insights.Purl, "pkg:generic/azure-pipelines-config")
				assert.Len(t, insights.AzurePipelines, 1, "Should detect Azure Pipeline")
			},
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			opaClient, err := newTestOpa(ctx)
			require.NoError(t, err, "Failed to create OPA client")

			formatter := &noop.Format{}
			analyzer := NewAnalyzer(nil, nil, formatter, models.DefaultConfig(), opaClient)

			manifestReader := strings.NewReader(tt.content)
			result, err := analyzer.AnalyzeManifest(ctx, manifestReader, tt.manifestType)

			require.NoError(t, err, "AnalyzeManifest should not return an error")
			require.NotNil(t, result, "Result should not be nil")

			if tt.validateResult != nil {
				tt.validateResult(t, result)
			}
		})
	}
}

func TestAnalyzeManifestErrorHandling(t *testing.T) {
	ctx := context.Background()

	opaClient, err := newTestOpa(ctx)
	require.NoError(t, err)

	formatter := &noop.Format{}
	analyzer := NewAnalyzer(nil, nil, formatter, models.DefaultConfig(), opaClient)

	t.Run("empty content", func(t *testing.T) {
		manifestReader := strings.NewReader("")
		result, err := analyzer.AnalyzeManifest(ctx, manifestReader, "github-actions")

		require.NoError(t, err)
		require.NotNil(t, result)
		assert.Equal(t, "manifest", result.SourceScmType)
	})

	t.Run("invalid yaml", func(t *testing.T) {
		invalidYaml := `name: Test
on: push
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: "Unclosed quote
        run: echo "test"`

		manifestReader := strings.NewReader(invalidYaml)
		result, err := analyzer.AnalyzeManifest(ctx, manifestReader, "github-actions")

		require.NoError(t, err)
		require.NotNil(t, result)
	})
}

```

### File: cmd\analyzeLocal.go
```go
package cmd

import (
	"fmt"

	"github.com/boostsecurityio/poutine/analyze"
	"github.com/boostsecurityio/poutine/providers/gitops"
	"github.com/boostsecurityio/poutine/providers/local"

	"github.com/spf13/cobra"
)

// analyzeLocalCmd represents the analyzeLocal command
var analyzeLocalCmd = &cobra.Command{
	Use:   "analyze_local",
	Short: "Analyzes a local repository for supply chain vulnerabilities",
	Long: `Analyzes a local repository for supply chain vulnerabilities
Example: poutine analyze_local /path/to/repo`,
	Args: cobra.ExactArgs(1),
	RunE: func(cmd *cobra.Command, args []string) error {
		ctx := cmd.Context()
		repoPath := args[0]

		opaClient, err := newOpa(ctx)
		if err != nil {
			return err
		}

		formatter := GetFormatter(opaClient)

		localScmClient, err := local.NewGitSCMClient(ctx, repoPath, nil)
		if err != nil {
			return fmt.Errorf("failed to create local SCM client: %w", err)
		}

		localGitClient := gitops.NewLocalGitClient(nil)

		analyzer := analyze.NewAnalyzer(localScmClient, localGitClient, formatter, config, opaClient)

		result, err := analyzer.AnalyzeLocalRepo(ctx, repoPath)
		if err != nil {
			return fmt.Errorf("failed to analyze repoPath %s: %w", repoPath, err)
		}

		if err := checkViolations(result); err != nil {
			return err
		}

		return nil
	},
}

func init() {
	RootCmd.AddCommand(analyzeLocalCmd)
}

```

### File: cmd\analyzeOrg.go
```go
package cmd

import (
	"fmt"

	"github.com/spf13/cobra"
	"github.com/spf13/viper"
)

var threads int

// analyzeOrgCmd represents the analyzeOrg command
var analyzeOrgCmd = &cobra.Command{
	Use:   "analyze_org",
	Short: "Analyzes an organization's repositories for supply chain vulnerabilities",
	Long: `Analyzes an organization's repositories for supply chain vulnerabilities
Example: poutine analyze_org org --token "$GH_TOKEN"

Analyze All Projects in a Self-Hosted Gitlab Organization: 
poutine analyze_org my-org/project --token "$GL_TOKEN" --scm gitlab --scm-base-uri https://gitlab.example.com
		
Note: This command will scan all repositories in the organization except those that are Archived.
`,
	Args: cobra.ExactArgs(1),
	RunE: func(cmd *cobra.Command, args []string) error {
		Token = viper.GetString("token")
		ctx := cmd.Context()
		analyzer, err := GetAnalyzer(ctx, "analyze_org")
		if err != nil {
			return err
		}

		org := args[0]

		results, err := analyzer.AnalyzeOrg(ctx, org, &threads)
		if err != nil {
			return fmt.Errorf("failed to analyze org %s: %w", org, err)
		}

		if err := checkViolations(results...); err != nil {
			return err
		}

		return nil
	},
}

func init() {
	RootCmd.AddCommand(analyzeOrgCmd)

	analyzeOrgCmd.Flags().StringVarP(&Token, "token", "t", "", "SCM access token (env: GH_TOKEN)")

	analyzeOrgCmd.Flags().IntVarP(&threads, "threads", "j", 2, "Parallelization factor for scanning organizations")
	analyzeOrgCmd.Flags().BoolVarP(&config.IgnoreForks, "ignore-forks", "i", false, "Ignore forked repositories in the organization")

	viper.BindPFlag("token", analyzeOrgCmd.Flags().Lookup("token"))
	viper.BindPFlag("ignoreForks", analyzeOrgCmd.Flags().Lookup("ignore-forks"))
	viper.BindEnv("token", "GH_TOKEN")
}

```

### File: cmd\analyzeRepo.go
```go
package cmd

import (
	"fmt"

	"github.com/spf13/cobra"
	"github.com/spf13/viper"
)

var ref string

// analyzeRepoCmd represents the analyzeRepo command
var analyzeRepoCmd = &cobra.Command{
	Use:   "analyze_repo",
	Short: "Analyzes a remote repository for supply chain vulnerabilities",
	Long: `Analyzes a remote repository for supply chain vulnerabilities
Example Scanning a remote Github Repository: poutine analyze_repo org/repo --token "$GH_TOKEN"`,
	Args: cobra.ExactArgs(1),
	RunE: func(cmd *cobra.Command, args []string) error {
		Token = viper.GetString("token")
		ctx := cmd.Context()
		analyzer, err := GetAnalyzer(ctx, "analyze_repo")
		if err != nil {
			return err
		}

		repo := args[0]

		result, err := analyzer.AnalyzeRepo(ctx, repo, ref)
		if err != nil {
			return fmt.Errorf("failed to analyze repo %s: %w", repo, err)
		}

		if err := checkViolations(result); err != nil {
			return err
		}

		return nil
	},
}

func init() {
	RootCmd.AddCommand(analyzeRepoCmd)

	analyzeRepoCmd.Flags().StringVarP(&Token, "token", "t", "", "SCM access token (env: GH_TOKEN)")
	analyzeRepoCmd.Flags().StringVarP(&ref, "ref", "r", "HEAD", "Commit or branch to analyze (defaults to HEAD)")

	viper.BindPFlag("token", analyzeOrgCmd.Flags().Lookup("token"))
	viper.BindEnv("token", "GH_TOKEN")
}

```

### File: cmd\analyzeRepoStaleBranches.go
```go
package cmd

import (
	"errors"
	"fmt"
	"regexp"

	"github.com/spf13/cobra"
	"github.com/spf13/viper"
)

var expand bool
var regex string

var analyzeRepoStaleBranches = &cobra.Command{
	Use:   "analyze_repo_stale_branches",
	Short: "Analyzes a remote repository for pull_request_target vulnerabilities in stale branches",
	Long: `Analyzes a remote repository, looping through all remote branches to find unique GitHub Actions workflows with old pull_request_target vulnerabilities, even though the default branch does not have that vulnerability anymore.
Example Scanning a remote Github Repository: poutine analyze_repo_stale_branches org/repo --token "$GH_TOKEN"`,
	Args: cobra.ExactArgs(1),
	RunE: func(cmd *cobra.Command, args []string) error {
		Token = viper.GetString("token")
		ctx := cmd.Context()
		analyzer, err := GetAnalyzer(ctx, "analyze_repo_stale_branches")
		if err != nil {
			return fmt.Errorf("error getting analyzer analyze_repo_stale_branches: %w", err)
		}

		if Format == "sarif" {
			return errors.New("sarif formatter not supported for analyze_repo_stale_branches")
		}

		repo := args[0]

		reg, err := regexp.Compile(regex)
		if err != nil {
			return fmt.Errorf("error compiling regex: %w", err)
		}

		result, err := analyzer.AnalyzeStaleBranches(ctx, repo, &threads, &expand, reg)
		if err != nil {
			return fmt.Errorf("failed to analyze repo %s: %w", repo, err)
		}

		if err := checkViolations(result); err != nil {
			return err
		}

		return nil
	},
}

func init() {
	RootCmd.AddCommand(analyzeRepoStaleBranches)

	analyzeRepoStaleBranches.Flags().StringVarP(&Token, "token", "t", "", "SCM access token (env: GH_TOKEN)")
	analyzeRepoStaleBranches.Flags().IntVarP(&threads, "threads", "j", 5, "Parallelization factor for scanning stale branches")
	analyzeRepoStaleBranches.Flags().BoolVarP(&expand, "expand", "e", false, "Expand the output to the classic representation from analyze_repo")
	analyzeRepoStaleBranches.Flags().StringVarP(&regex, "regex", "r", "pull_request_target", "Regex to check if the workflow is accessible in stale branches")

	_ = viper.BindPFlag("token", analyzeRepoStaleBranches.Flags().Lookup("token"))
	_ = viper.BindEnv("token", "GH_TOKEN")
}

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.

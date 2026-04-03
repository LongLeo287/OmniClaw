---
id: sigstore-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:31:13.722862
---

# KNOWLEDGE EXTRACT: sigstore
> **Extracted on:** 2026-03-30 17:53:21
> **Source:** sigstore

---

## File: `cosign-installer.md`
```markdown
# 📦 sigstore/cosign-installer [🔖 PENDING/APPROVE]
🔗 https://github.com/sigstore/cosign-installer
🌐 https://sigstore.dev

## Meta
- **Stars:** ⭐ 193 | **Forks:** 🍴 55
- **Language:** N/A | **License:** Apache-2.0
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Cosign Github Action

## README (trích đầu)
```
# cosign-installer GitHub Action

This action enables you to sign and verify container images using `cosign`.
`cosign-installer` verifies the integrity of the `cosign` release during installation.

For a quick start guide on the usage of `cosign`, please refer to https://github.com/sigstore/cosign#quick-start.
For available `cosign` releases, see https://github.com/sigstore/cosign/releases.

## Usage

This action currently supports GitHub-provided Linux, macOS and Windows runners (self-hosted runners may not work).

Add the following entry to your Github workflow YAML file:

```yaml
uses: sigstore/cosign-installer@v4.1.0
```

Full example:

```yaml
jobs:
  example:
    runs-on: ubuntu-latest

    permissions: {}

    name: Install Cosign
    steps:
      - name: Install Cosign
        uses: sigstore/cosign-installer@v4.1.0
      - name: Check install!
        run: cosign version
```

The used Cosign version only changes when cosign-installer is upgraded. If you need to select a specific Cosign version, use `cosign-release` but note that you are now responsible for maintaining the Cosign version (in addition to maintaining the cosign-installer version).

Example pinning Cosign version with `cosign-release`:

```yaml
jobs:
  example:
    runs-on: ubuntu-latest

    permissions: {}

    name: Install Cosign
    steps:
      - name: Install Cosign
        uses: sigstore/cosign-installer@v4.1.0
        with:
          cosign-release: 'v3.0.5'
      - name: Check install!
        run: cosign version
```

If you want to install cosign from its main version by using 'go install' under the hood, you can set 'cosign-release' as 'main'. Once you did that, cosign will be installed via 'go install' which means that please ensure that go is installed.

Example of installing cosign via go install:

```yaml
jobs:
  example:
    runs-on: ubuntu-latest

    permissions: {}

    name: Install Cosign via go install
    steps:
      - name: Install go
        uses: actions/setup-go@v6.0.0
        with:
          go-version: '1.24'
          check-latest: true
      - name: Install Cosign
        uses: sigstore/cosign-installer@v4.1.0
        with:
          cosign-release: main
      - name: Check install!
        run: cosign version
```

This action does not need any GitHub permission to run, however, if your workflow needs to update, create or perform any
action against your repository, then you should change the scope of the permission appropriately.

For example, if you are using the `ghcr.io` as your registry to push the images you will need to give the `write` permission
to the `packages` scope.

Example of a simple workflow:

```yaml
jobs:
  build-image:
    runs-on: ubuntu-latest

    permissions:
      contents: read
      packages: write
      id-token: write # needed for signing the images with GitHub OIDC Token

    name: build-image
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 1

      - name: Install Cosign
        u
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `cosign.md`
```markdown
# 📦 sigstore/cosign [🔖 PENDING/APPROVE]
🔗 https://github.com/sigstore/cosign


## Meta
- **Stars:** ⭐ 5760 | **Forks:** 🍴 711
- **Language:** Go | **License:** Apache-2.0
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Code signing and transparency for containers and binaries

## README (trích đầu)
```
<p align="center">
  <img style="max-width: 100%;width: 300px;" src="https://raw.githubusercontent.com/sigstore/community/main/artwork/cosign/horizontal/color/sigstore_cosign-horizontal-color.svg" alt="Cosign logo"/>
</p>

# cosign

Signing OCI containers (and other artifacts) using [Sigstore](https://sigstore.dev/)!

[![Go Report Card](https://goreportcard.com/badge/github.com/sigstore/cosign)](https://goreportcard.com/report/github.com/sigstore/cosign)
[![e2e-tests](https://github.com/sigstore/cosign/actions/workflows/e2e-tests.yml/badge.svg)](https://github.com/sigstore/cosign/actions/workflows/e2e-tests.yml)
[![CII Best Practices](https://bestpractices.coreinfrastructure.org/projects/5715/badge)](https://bestpractices.coreinfrastructure.org/projects/5715)
[![OpenSSF Scorecard](https://api.securityscorecards.dev/projects/github.com/sigstore/cosign/badge)](https://securityscorecards.dev/viewer/?uri=github.com/sigstore/cosign)

Cosign aims to make signatures **invisible infrastructure**.

Cosign supports:

* "Keyless signing" with the Sigstore public good Fulcio certificate authority and Rekor transparency log (default)
* Hardware and KMS signing
* Signing with a cosign generated encrypted private/public keypair
* Container Signing, Verification and Storage in an OCI registry.
* Bring-your-own PKI

## Info

`Cosign` is developed as part of the [`sigstore`](https://sigstore.dev) project.
We also use a [slack channel](https://sigstore.slack.com)!
Click [here](https://join.slack.com/t/sigstore/shared_invite/zt-2ub0ztl5z-PkWb_Ldwef5d6nb~oryaTA) for the invite link.

## Installation

For Homebrew, Arch, Nix, GitHub Action, and Kubernetes installs see the [installation docs](https://docs.sigstore.dev/cosign/system_config/installation/).

For Linux and macOS binaries see the [GitHub release assets](https://github.com/sigstore/cosign/releases/latest).

:rotating_light: If you are downloading releases of cosign from our GCS bucket - please see more information on the July 31, 2023 [deprecation notice](https://blog.sigstore.dev/cosign-releases-bucket-deprecation/) :rotating_light:

## Developer Installation

If you have Go 1.22+, you can setup a development environment:

```shell
$ git clone https://github.com/sigstore/cosign
$ cd cosign
$ go install ./cmd/cosign
$ $(go env GOPATH)/bin/cosign
```

## Contributing

If you are interested in contributing to `cosign`, please read the [contributing documentation](./CONTRIBUTING.md).

Future Cosign development will be focused the next major release which will be based on
[sigstore-go](https://github.com/sigstore/sigstore-go). Maintainers will be focused on feature development within
sigstore-go. Contributions to sigstore-go, particularly around bring-your-own keys and signing, are appreciated.
Please see the [issue tracker](https://github.com/sigstore/sigstore-go/issues) for good first issues.

Cosign 2.x is a stable release and will continue to receive periodic feature updates and bug fixes. PRs
that are small
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```


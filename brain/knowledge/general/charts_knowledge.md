# Knowledge Dump for charts

## File: .markdownlint.yaml
```
MD013: false # Line length
MD026: false # Trailing punctuation in header
MD029: false # Ordered list item prefix
MD033: false # Inline HTML

```

## File: .pre-commit-config.yaml
```
default_language_version:
  python: python3.11

repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.4.0
    hooks:
      - id: no-commit-to-branch
        args: ["--branch", "main", "--branch", "dev"]
      - id: mixed-line-ending
      - id: end-of-file-fixer
      - id: trailing-whitespace
      - id: check-added-large-files
      - id: check-merge-conflict
      - id: check-case-conflict
      - id: check-docstring-first
      - id: check-symlinks
      - id: check-yaml
        exclude: "charts/paradedb/" # Exclude all files in the charts/paradedb/ directory, which aren't standard YAML
      - id: check-json
      - id: check-xml
      - id: check-ast
      - id: check-toml
      - id: check-executables-have-shebangs
      - id: check-shebang-scripts-are-executable
      - id: check-vcs-permalinks
      - id: detect-private-key
      - id: detect-aws-credentials
      - id: debug-statements
      - id: destroyed-symlinks
      - id: fix-encoding-pragma
      - id: fix-byte-order-marker
      - id: requirements-txt-fixer

  - repo: https://github.com/igorshubovych/markdownlint-cli
    rev: v0.37.0
    hooks:
      - id: markdownlint

  - repo: https://github.com/pre-commit/mirrors-prettier
    rev: v3.0.3
    hooks:
      - id: prettier
        exclude: "charts/paradedb/" # Exclude all files in the charts/paradedb/ directory, which aren't standard YAML

```

## File: artifacthub-repo.yml
```
# Artifact Hub repository metadata file
#
# Some settings like the verified publisher flag or the ignored packages won't
# be applied until the next time the repository is processed. Please keep in
# mind that the repository won't be processed if it has not changed since the
# last time it was processed. Depending on the repository kind, this is checked
# in a different way. For Helm http based repositories, we consider it has
# changed if the `index.yaml` file changes. For git based repositories, it does
# when the hash of the last commit in the branch you set up changes. This does
# NOT apply to ownership claim operations, which are processed immediately.
#
repositoryID: d7b5cc3f-1710-47b5-af0f-14855f44f77d
owners:
  - name: ParadeDB Support
    email: support@paradedb.com

```

## File: code_of_conduct.md
```
# Contributor Covenant Code of Conduct

## Our Pledge

We as members, contributors, and leaders pledge to make participation in our
community a harassment-free experience for everyone, regardless of age, body
size, visible or invisible disability, ethnicity, sex characteristics, gender
identity and expression, level of experience, education, socioeconomic status,
nationality, personal appearance, race, caste, color, religion, or sexual identity
and orientation.

We pledge to act and interact in ways that contribute to an open, welcoming,
diverse, inclusive, and healthy community.

## Our Standards

Examples of behavior that contributes to a positive environment for our
community include:

- Demonstrating empathy and kindness toward other people
- Being respectful of differing opinions, viewpoints, and experiences
- Giving and gracefully accepting constructive feedback
- Accepting responsibility and apologizing to those affected by our mistakes,
  and learning from the experience
- Focusing on what is best not just for us as individuals, but for the
  overall community

Examples of unacceptable behavior include:

- The use of sexualized language or imagery, and sexual attention or
  advances of any kind
- Trolling, insulting or derogatory comments, and personal or political attacks
- Public or private harassment
- Publishing others' private information, such as a physical or email
  address, without their explicit permission
- Other conduct which could reasonably be considered inappropriate in a
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
[community@paradedb.com](mailto:community@paradedb.com).
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
standards, including sustained inappropriate behavior, harassment of an
individual, or aggression toward or disparagement of classes of individuals.

**Consequence**: A permanent ban from any sort of public interaction within
the community.

## Attribution

This Code of Conduct is adapted from the [Contributor Covenant][homepage],
version 2.0, available [here](https://www.contributor-covenant.org/version/2/0/code_of_conduct.html).

Community Impact Guidelines were inspired by [Mozilla's code of conduct
enforcement ladder](https://github.com/mozilla/diversity).

[homepage]: https://www.contributor-covenant.org

For answers to common questions about this code of conduct, see the
[FAQ](https://www.contributor-covenant.org/faq). Translations are available
[here](https://www.contributor-covenant.org/translations).

```

## File: contributing.md
```
# Contributing to CloudNativePG

Thank you for your interest in contributing! 💖

To ensure consistency across the project, all CloudNativePG repositories follow
a common set of guidelines regarding code of conduct, AI usage, and
contribution workflows.

Please review the [CloudNativePG Project contributing guidelines](https://github.com/cloudnative-pg/governance/blob/main/CONTRIBUTING.md)
before searching for issues, reporting bugs, or submitting a pull request.

```

## File: README.md
```
<h1 align="center">
  <a href="https://paradedb.com"><img src="https://raw.githubusercontent.com/paradedb/paradedb/dev/docs/logo/readme.svg" alt="ParadeDB"></a>
<br>
</h1>

<p align="center">
    <b>Postgres for Search and Analytics</b> <br />
</p>

<h3 align="center">
  <a href="https://paradedb.com">Website</a> &bull;
  <a href="https://docs.paradedb.com">Docs</a> &bull;
  <a href="https://join.slack.com/t/paradedbcommunity/shared_invite/zt-32abtyjg4-yoYoi~RPh9MSW8tDbl0BQw">Community</a> &bull;
  <a href="https://paradedb.com/blog/">Blog</a> &bull;
  <a href="https://docs.paradedb.com/changelog/">Changelog</a>
</h3>

---

[![Publish Helm Chart](https://github.com/paradedb/charts/actions/workflows/paradedb-publish-chart.yml/badge.svg)](https://github.com/paradedb/charts/actions/workflows/paradedb-publish-chart.yml)
[![Artifact Hub](https://img.shields.io/endpoint?url=https://artifacthub.io/badge/repository/paradedb)](https://artifacthub.io/packages/search?repo=paradedb)
[![Docker Pulls](https://img.shields.io/docker/pulls/paradedb/paradedb)](https://hub.docker.com/r/paradedb/paradedb)
[![License](https://img.shields.io/github/license/paradedb/charts?color=blue)](https://github.com/paradedb/charts/blob/main/LICENSE)
[![Slack URL](https://img.shields.io/badge/Join%20Slack-purple?logo=slack&link=https%3A%2F%2Fjoin.slack.com%2Ft%2Fparadedbcommunity%2Fshared_invite%2Fzt-32abtyjg4-yoYoi~RPh9MSW8tDbl0BQw)](https://join.slack.com/t/paradedbcommunity/shared_invite/zt-32abtyjg4-yoYoi~RPh9MSW8tDbl0BQw)
[![X URL](https://img.shields.io/twitter/url?url=https%3A%2F%2Ftwitter.com%2Fparadedb&label=Follow%20%40paradedb)](https://x.com/paradedb)

# ParadeDB Helm Chart

The [ParadeDB](https://github.com/paradedb/paradedb) Helm Chart is based on the official [CloudNativePG Helm Chart](https://cloudnative-pg.io/). CloudNativePG is a Kubernetes operator that manages the full lifecycle of a highly available PostgreSQL database cluster with a primary/standby architecture using Postgres streaming (physical) replication.

Kubernetes, and specifically the CloudNativePG operator, is the recommended approach for deploying ParadeDB in production, with high availability. ParadeDB also provides a [Docker image](https://hub.docker.com/r/paradedb/paradedb) and [prebuilt binaries](https://github.com/paradedb/paradedb/releases) for Debian, Ubuntu, Red Hat Enterprise Linux, and macOS.

The ParadeDB Helm Chart supports Postgres 15+ and ships with Postgres 18 by default.

The chart is also available on [Artifact Hub](https://artifacthub.io/packages/helm/paradedb/paradedb).

## Usage

First, install [Helm](https://helm.sh/docs/intro/install/). The following steps assume you have a Kubernetes cluster running v1.29+. If you are testing locally, we recommend using [Minikube](https://minikube.sigs.k8s.io/docs/start/).

#### Monitoring

The ParadeDB Helm chart supports monitoring via Prometheus and Grafana. To enable monitoring, you need to have the Prometheus CRDs installed before installing the CloudNativePG operator. The Prometheus CRDs can be found [here](https://prometheus-community.github.io/helm-charts).

#### Installing the CloudNativePG Operator

Skip this step if the CloudNativePG operator is already installed in your cluster. For advanced CloudNativePG configuration and monitoring, please refer to the [CloudNativePG Cluster Chart documentation](https://github.com/paradedb/charts/blob/main/charts/cloudnative-pg/README.md#values).

```bash
helm repo add cnpg https://cloudnative-pg.github.io/charts
helm upgrade --atomic --install cnpg \
--create-namespace \
--namespace cnpg-system \
cnpg/cloudnative-pg
```

#### Setting up a ParadeDB CNPG Cluster

> [!IMPORTANT]
> When deploying a cluster with more than one instance, you must use `type: paradedb-enterprise` to enable replication of BM25 indexes across instances.
> Using ParadeDB Enterprise requires an access token. To request one, please [contact sales](mailto:sales@paradedb.com).

Create a `values.yaml` and configure it to your requirements. Here is a basic example:

```yaml
type: paradedb
mode: standalone

version:
  # -- PostgreSQL major version to use
  postgresql: "18"
  # -- ParadeDB version to use
  paradedb: "0.22.3"

cluster:
  instances: 1
  storage:
    size: 256Mi
```

Then, launch the ParadeDB cluster.

```bash
helm repo add paradedb https://paradedb.github.io/charts
helm upgrade --atomic --install paradedb \
--namespace paradedb \
--create-namespace \
--values values.yaml \
paradedb/paradedb
```

If `--values values.yaml` is omitted, the default values will be used. For advanced ParadeDB configuration and monitoring, please refer to the [ParadeDB Chart documentation](https://github.com/paradedb/charts/tree/dev/charts/paradedb#values).

#### Connecting to a ParadeDB CNPG Cluster

You can launch a Bash shell inside a specific pod via:

```bash
kubectl exec --stdin --tty <pod-name> -n paradedb -- bash
```

The primary is called `paradedb-1`. The replicas are called `paradedb-2` onwards depending on the number of replicas you configured. You can connect to the ParadeDB database with `psql` via:

```bash
psql -d paradedb
```

## Development

To test changes to the Chart on a local Minikube cluster, follow the instructions from [Self Hosted](#self-hosted) replacing the `helm upgrade` step by the path to the directory of the modified `Chart.yaml`.

```bash
helm upgrade --atomic --install paradedb --namespace paradedb --create-namespace ./charts/paradedb
```

## License

Apache-2.0 License - see [LICENSE](LICENSE) for details.

```

## File: security.md
```
# Security Policy

## Supported Versions

We release patches for security vulnerabilities on a regular cadence. Which versions
are eligible for receiving such patches can be found below:

| Version | Supported          |
| ------- | ------------------ |
| latest  | :white_check_mark: |

## Reporting a Vulnerability

Please do NOT raise a GitHub Issue to report a security vulnerability. Please report
(suspected) security vulnerabilities to **[security@paradedb.com](mailto:security@paradedb.com)**,
preferably with a proof of concept. You will receive a response from us within 24
hours. If the issue is confirmed, we will release a patch as quickly as
possible depending on complexity but historically within a few days.

Non-vulnerability-related security issues such as new ideas for security features
are welcome on GitHub Issues.

```

## File: _GIT_INGEST.md
```
# OmniClaw Repo Plow: CIV_FETCHED_charts_182209



================================================
FILE: CODE_OF_CONDUCT.md
================================================
# Contributor Covenant Code of Conduct

## Our Pledge

We as members, contributors, and leaders pledge to make participation in our
community a harassment-free experience for everyone, regardless of age, body
size, visible or invisible disability, ethnicity, sex characteristics, gender
identity and expression, level of experience, education, socioeconomic status,
nationality, personal appearance, race, caste, color, religion, or sexual identity
and orientation.

We pledge to act and interact in ways that contribute to an open, welcoming,
diverse, inclusive, and healthy community.

## Our Standards

Examples of behavior that contributes to a positive environment for our
community include:

- Demonstrating empathy and kindness toward other people
- Being respectful of differing opinions, viewpoints, and experiences
- Giving and gracefully accepting constructive feedback
- Accepting responsibility and apologizing to those affected by our mistakes,
  and learning from the experience
- Focusing on what is best not just for us as individuals, but for the
  overall community

Examples of unacceptable behavior include:

- The use of sexualized language or imagery, and sexual attention or
  advances of any kind
- Trolling, insulting or derogatory comments, and personal or political attacks
- Public or private harassment
- Publishing others' private information, such as a physical or email
  address, without their explicit permission
- Other conduct which could reasonably be considered inappropriate in a
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
[community@paradedb.com](mailto:community@paradedb.com).
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
standards, including sustained inappropriate behavior, harassment of an
individual, or aggression toward or disparagement of classes of individuals.

**Consequence**: A permanent ban from any sort of public interaction within
the community.

## Attribution

This Code of Conduct is adapted from the [Contributor Covenant][homepage],
version 2.0, available [here](https://www.contributor-covenant.org/version/2/0/code_of_conduct.html).

Community Impact Guidelines were inspired by [Mozilla's code of conduct
enforcement ladder](https://github

================================================
FILE: CONTRIBUTING.md
================================================
# Contributing to CloudNativePG

Thank you for your interest in contributing! 💖

To ensure consistency across the project, all CloudNativePG repositories follow
a common set of guidelines regarding code of conduct, AI usage, and
contribution workflows.

Please review the [CloudNativePG Project contributing guidelines](https://github.com/cloudnative-pg/governance/blob/main/CONTRIBUTING.md)
before searching for issues, reporting bugs, or submitting a pull request.


================================================
FILE: README.md
================================================
<h1 align="center">
  <a href="https://paradedb.com"><img src="https://raw.githubusercontent.com/paradedb/paradedb/dev/docs/logo/readme.svg" alt="ParadeDB"></a>
<br>
</h1>

<p align="center">
    <b>Postgres for Search and Analytics</b> <br />
</p>

<h3 align="center">
  <a href="https://paradedb.com">Website</a> &bull;
  <a href="https://docs.paradedb.com">Docs</a> &bull;
  <a href="https://join.slack.com/t/paradedbcommunity/shared_invite/zt-32abtyjg4-yoYoi~RPh9MSW8tDbl0BQw">Community</a> &bull;
  <a href="https://paradedb.com/blog/">Blog</a> &bull;
  <a href="https://docs.paradedb.com/changelog/">Changelog</a>
</h3>

---

[![Publish Helm Chart](https://github.com/paradedb/charts/actions/workflows/paradedb-publish-chart.yml/badge.svg)](https://github.com/paradedb/charts/actions/workflows/paradedb-publish-chart.yml)
[![Artifact Hub](https://img.shields.io/endpoint?url=https://artifacthub.io/badge/repository/paradedb)](https://artifacthub.io/packages/search?repo=paradedb)
[![Docker Pulls](https://img.shields.io/docker/pulls/paradedb/paradedb)](https://hub.docker.com/r/paradedb/paradedb)
[![License](https://img.shields.io/github/license/paradedb/charts?color=blue)](https://github.com/paradedb/charts/blob/main/LICENSE)
[![Slack URL](https://img.shields.io/badge/Join%20Slack-purple?logo=slack&link=https%3A%2F%2Fjoin.slack.com%2Ft%2Fparadedbcommunity%2Fshared_invite%2Fzt-32abtyjg4-yoYoi~RPh9MSW8tDbl0BQw)](https://join.slack.com/t/paradedbcommunity/shared_invite/zt-32abtyjg4-yoYoi~RPh9MSW8tDbl0BQw)
[![X URL](https://img.shields.io/twitter/url?url=https%3A%2F%2Ftwitter.com%2Fparadedb&label=Follow%20%40paradedb)](https://x.com/paradedb)

# ParadeDB Helm Chart

The [ParadeDB](https://github.com/paradedb/paradedb) Helm Chart is based on the official [CloudNativePG Helm Chart](https://cloudnative-pg.io/). CloudNativePG is a Kubernetes operator that manages the full lifecycle of a highly available PostgreSQL database cluster with a primary/standby architecture using Postgres streaming (physical) replication.

Kubernetes, and specifically the CloudNativePG operator, is the recommended approach for deploying ParadeDB in production, with high availability. ParadeDB also provides a [Docker image](https://hub.docker.com/r/paradedb/paradedb) and [prebuilt binaries](https://github.com/paradedb/paradedb/releases) for Debian, Ubuntu, Red Hat Enterprise Linux, and macOS.

The ParadeDB Helm Chart supports Postgres 15+ and ships with Postgres 18 by default.

The chart is also available on [Artifact Hub](https://artifacthub.io/packages/helm/paradedb/paradedb).

## Usage

First, install [Helm](https://helm.sh/docs/intro/install/). The following steps assume you have a Kubernetes cluster running v1.29+. If you are testing locally, we recommend using [Minikube](https://minikube.sigs.k8s.io/docs/start/).

#### Monitoring

The ParadeDB Helm chart supports monitoring via Prometheus and Grafana. To enable monitoring, you need to have the Prometheus CRDs installed before installing the CloudNativePG operator. The Prometheus CRDs can be found [here](https://prometheus-community.github.io/helm-charts).

#### Installing the CloudNativePG Operator

Skip this step if the CloudNativePG operator is already installed in your cluster. For advanced CloudNativePG configuration and monitoring, please refer to the [CloudNativePG Cluster Chart documentation](https://github.com/paradedb/charts/blob/main/charts/cloudnative-pg/README.md#values).

```bash
helm repo add cnpg https://cloudnative-pg.github.io/charts
helm upgrade --atomic --install cnpg \
--create-namespace \
--namespace cnpg-system \
cnpg/cloudnative-pg
```

#### Setting up a ParadeDB CNPG Cluster

> [!IMPORTANT]
> When deploying a cluster with more than one instance, you must use `type: paradedb-enterprise` to enable replication of BM25 indexes across instances.
> Using ParadeDB Enterprise requires an access token. To request one, please [contact sales](mailto:sales@paradedb.com).

Create a `values.yaml` and configure it to your requirements. Here is a basic example:

```yaml
type: paradedb
mode: standalone

version:
  # -- PostgreSQL major version to use
  postgresql: "18"
  # -- ParadeDB version to use
  paradedb: "0.22.3"

cluster:
  instances: 1
  storage:
    size: 256Mi
```

Then, launch the ParadeDB cluster.

```bash
helm repo add paradedb https://paradedb.github.io/charts
helm upgrade --atomic --install paradedb \
--namespace paradedb \
--create-namespace \
--values values.yaml \
paradedb/paradedb
```

If `--values values.yaml` is omitted, the default values will be used. For advanced ParadeDB configuration and monitoring, please refer to the [ParadeDB Chart documentation](https://github.com/paradedb/charts/tree/dev/charts/paradedb#values).

#### Connecting to a ParadeDB CNPG Cluster

You can launch a Bash shell inside a specific pod via:

```bash
kubectl exec --stdin --tty <pod-name> -n paradedb -- bash
```

The primary is called `paradedb-1`. The replicas are called `paradedb-2` onw

================================================
FILE: SECURITY.md
================================================
# Security Policy

## Supported Versions

We release patches for security vulnerabilities on a regular cadence. Which versions
are eligible for receiving such patches can be found below:

| Version | Supported          |
| ------- | ------------------ |
| latest  | :white_check_mark: |

## Reporting a Vulnerability

Please do NOT raise a GitHub Issue to report a security vulnerability. Please report
(suspected) security vulnerabilities to **[security@paradedb.com](mailto:security@paradedb.com)**,
preferably with a proof of concept. You will receive a response from us within 24
hours. If the issue is confirmed, we will release a patch as quickly as
possible depending on complexity but historically within a few days.

Non-vulnerability-related security issues such as new ideas for security features
are welcome on GitHub Issues.


================================================
FILE: charts\paradedb\README.md
================================================
# ParadeDB Helm Chart

The [ParadeDB](https://github.com/paradedb/paradedb) Helm Chart is based on the official [CloudNativePG Helm Chart](https://cloudnative-pg.io/). CloudNativePG is a Kubernetes operator that manages the full lifecycle of a highly available PostgreSQL database cluster with a primary/standby architecture using Postgres streaming (physical) replication.

Kubernetes, and specifically the CloudNativePG operator, is the recommended approach for deploying ParadeDB in production, with high availability. ParadeDB also provides a [Docker image](https://hub.docker.com/r/paradedb/paradedb) and [prebuilt binaries](https://github.com/paradedb/paradedb/releases) for Debian, Ubuntu, Red Hat Enterprise Linux, and macOS.

The ParadeDB Helm Chart supports Postgres 15+ and ships with Postgres 18 by default.

The chart is also available on [Artifact Hub](https://artifacthub.io/packages/helm/paradedb/paradedb).

## Usage

First, install [Helm](https://helm.sh/docs/intro/install/). The following steps assume you have a Kubernetes cluster running v1.29+. If you are testing locally, we recommend using [Minikube](https://minikube.sigs.k8s.io/docs/start/).

#### Monitoring

The ParadeDB Helm chart supports monitoring via Prometheus and Grafana. To enable monitoring, you need to have the Prometheus CRDs installed before installing the CloudNativePG operator. The Prometheus CRDs can be found [here](https://prometheus-community.github.io/helm-charts).

#### Installing the CloudNativePG Operator

Skip this step if the CloudNativePG operator is already installed in your cluster. For advanced CloudNativePG configuration and monitoring, please refer to the [CloudNativePG Cluster Chart documentation](https://github.com/paradedb/charts/blob/main/charts/cloudnative-pg/README.md#values).

```bash
helm repo add cnpg https://cloudnative-pg.github.io/charts
helm upgrade --atomic --install cnpg \
--create-namespace \
--namespace cnpg-system \
cnpg/cloudnative-pg
```

#### Setting up a ParadeDB CNPG Cluster

> [!IMPORTANT]
> When deploying a cluster with more than one instance, you must use `type: paradedb-enterprise` to enable replication of BM25 indexes across instances.
> Using ParadeDB Enterprise requires an access token. To request one, please [contact sales](mailto:sales@paradedb.com).

Create a `values.yaml` and configure it to your requirements. Here is a basic example:

```yaml
type: paradedb
mode: standalone

version:
  # -- PostgreSQL major version to use
  postgresql: "18"
  # -- ParadeDB version to use
  paradedb: "0.22.3"

cluster:
  instances: 1
  storage:
    size: 256Mi
```

Then, launch the ParadeDB cluster.

```bash
helm repo add paradedb https://paradedb.github.io/charts
helm upgrade --atomic --install paradedb \
--namespace paradedb \
--create-namespace \
--values values.yaml \
paradedb/paradedb
```

If `--values values.yaml` is omitted, the default values will be used. For advanced ParadeDB configuration and monitoring, please refer to the [ParadeDB Chart documentation](https://github.com/paradedb/charts/tree/dev/charts/paradedb#values).

#### Connecting to a ParadeDB CNPG Cluster

You can launch a Bash shell inside a specific pod via:

```bash
kubectl exec --stdin --tty <pod-name> -n paradedb -- bash
```

The primary is called `paradedb-1`. The replicas are called `paradedb-2` onwards depending on the number of replicas you configured. You can connect to the ParadeDB database with `psql` via:

```bash
psql -d paradedb
```

## Development

To test changes to the Chart on a local Minikube cluster, follow the instructions from [Self Hosted](#self-hosted) replacing the `helm upgrade` step by the path to the directory of the modified `Chart.yaml`.

```bash
helm upgrade --atomic --install paradedb --namespace paradedb --create-namespace ./charts/paradedb
```

## Advanced Cluster Configuration

### Database Types

To create a ParadeDB cluster, you must specify either `paradedb` or `paradedb-enterprise` via the `type` parameter.

> [!IMPORTANT]
> When using `paradedb-enterprise` you must also specify the `cluster.imagePullSecrets` containing the Docker registry credentials. You can create one with:
>
> ```bash
> kubectl -n NAMESPACE create secret docker-registry paradedb-enterprise-registry-cred --docker-server="https://index.docker.io/v1/" --docker-username="USERNAME" --docker-password="ACCESS_TOKEN"
> ```
>
> You then need to set the name of the secret in the `values.yaml` file with:
>
> ```yaml
> type: paradedb-enterprise
> cluster:
>   imagePullSecrets:
>    - name: paradedb-enterprise-registry-cred
> ```

### Modes of Operation

The chart has three modes of operation. These are configured via the `mode` parameter:

* `standalone` - Creates new or updates an existing CNPG cluster. This is the default mode.
* `replica` - Creates a replica cluster from an existing CNPG cluster.
* `recovery` - Recovers a CNPG cluster from a backup, object store or via pg_basebackup.

### Backup Configuration

CNPG implements disa

================================================
FILE: charts\paradedb\values.schema.json
================================================
{
    "$schema": "http://json-schema.org/schema#",
    "type": "object",
    "properties": {
        "backups": {
            "type": "object",
            "properties": {
                "azure": {
                    "type": "object",
                    "properties": {
                        "connectionString": {
                            "type": "string"
                        },
                        "containerName": {
                            "type": "string"
                        },
                        "inheritFromAzureAD": {
                            "type": "boolean"
                        },
                        "path": {
                            "type": "string"
                        },
                        "serviceName": {
                            "type": "string"
                        },
                        "storageAccount": {
                            "type": "string"
                        },
                        "storageKey": {
                            "type": "string"
                        },
                        "storageSasToken": {
                            "type": "string"
                        }
                    }
                },
                "data": {
                    "type": "object",
                    "properties": {
                        "compression": {
                            "type": "string"
                        },
                        "encryption": {
                            "type": "string"
                        },
                        "jobs": {
                            "type": "integer"
                        }
                    }
                },
                "destinationPath": {
                    "type": "string"
                },
                "enabled": {
                    "type": "boolean"
                },
                "endpointCA": {
                    "type": "object",
                    "properties": {
                        "create": {
                            "type": "boolean"
                        },
                        "key": {
                            "type": "string"
                        },
                        "name": {
                            "type": "string"
                        },
                        "value": {
                            "type": "string"
                        }
                    }
                },
                "endpointURL": {
                    "type": "string"
                },
                "google": {
                    "type": "object",
                    "properties": {
                        "applicationCredentials": {
                            "type": "string"
                        },
                        "bucket": {
                            "type": "string"
                        },
                        "gkeEnvironment": {
                            "type": "boolean"
                        },
                        "path": {
                            "type": "string"
                        }
                    }
                },
                "provider": {
                    "type": "string"
                },
                "retentionPolicy": {
                    "type": "string"
                },
                "s3": {
                    "type": "object",
                    "properties": {
                        "accessKey": {
                            "type": "string"
                        },
                        "bucket": {
                            "type": "string"
                        },
                        "inheritFromIAMRole": {
                            "type": "boolean"
                        },
                        "path": {
                            "type": "string"
                        },
                        "region": {
                            "type": "string"
                        },
                        "secretKey": {
                            "type": "string"
                        }
                    }
                },
                "scheduledBackups": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "backupOwnerReference": {
                                "type": "string"
                            },
                            "method": {
                                "type": "string"
                            },
                            "name": {
                                "type": "string"
                            },
                            "schedule": {
                                "type": "string"
                            }
                        }
                    }
                },
                "secret": {
                    "type": "object",
                    "properties": {
                        "cr

================================================
FILE: charts\paradedb\docs\getting-started.md
================================================
# Getting Started

The CNPG cluster chart follows a convention over configuration approach. This means that the chart will create a reasonable
CNPG setup with sensible defaults. However, you can override these defaults to create a more customized setup. Note that
you still need to configure backups and monitoring separately. The chart will not install a Prometheus stack for you.

_**Note**_ that this is an opinionated chart. It does not support all configuration options that CNPG supports. If you
need a highly customized setup, you should manage your cluster via a Kubernetes CNPG cluster manifest instead of this chart.
Refer to the [CNPG documentation](https://cloudnative-pg.io/documentation/current/) in that case.

## Installing the operator

To begin, make sure you install the CNPG operator in your cluster. It can be installed via a Helm chart as shown below or
it can be installed via a Kubernetes manifest. For more information see the [CNPG documentation](https://cloudnative-pg.io/documentation/current/installation_upgrade/).

```console
helm repo add cnpg https://cloudnative-pg.github.io/charts
helm upgrade --install cnpg \
  --namespace cnpg-system \
  --create-namespace \
  cnpg/cloudnative-pg
```

## Creating a cluster configuration

Once you have the operator installed, the next step is to prepare the cluster configuration. Whether this will be managed
via a GitOps solution or directly via Helm is up to you. The following sections outline the important steps in both cases.

### Choosing the database type

Currently the chart supports two database types. These are configured via the `type` parameter. These are:
* `postgresql` - A standard PostgreSQL database.
* `paradedb` - Postgres for Search and Analytics.

Depending on the type the chart will use a different Docker image and fill in some initial setup, like extension installation.

### Choosing the mode of operation

The chart has three modes of operation. These are configured via the `mode` parameter. If this is your first cluster, you
are likely looking for the `standalone` option.
* `standalone` - Creates new or updates an existing CNPG cluster. This is the default mode.
* `replica` - Creates a replica cluster from an existing CNPG cluster.
* `recovery` - Recovers a CNPG cluster from a backup, object store or via pg_basebackup.

### Backup configuration

Most importantly you should configure your backup storage.

CNPG implements disaster recovery via [Barman](https://pgbarman.org/). The following section configures the barman object
store where backups will be stored. Barman performs backups of the cluster filesystem base backup and WALs. Both are
stored in the specified location. The backup provider is configured via the `backups.provider` parameter. The following
providers are supported:

* S3 or S3-compatible stores, like MinIO
* Microsoft Azure Blob Storage
* Google Cloud Storage

Additionally you can specify the following parameters:
* `backups.retentionPolicy` - The retention policy for backups. Defaults to `30d`.
* `backups.scheduledBackups` - An array of scheduled backups containing a name and a crontab schedule. Example:
  ```yaml
  backups:
    scheduledBackups:
      - name: daily-backup
        schedule: "0 0 0 * * *" # Daily at midnight
        backupOwnerReference: self
  ```

Each backup adapter takes its own set of parameters, listed in the [Configuration options](../README.md#Configuration-options)
section. Refer to the table for the full list of parameters and place the configuration under the appropriate key: `backups.s3`,
`backups.azure`, or `backups.google`.

### Cluster configuration

There are several important cluster options. Here are the most important ones:

`cluster.instances` - The number of instances in the cluster. Defaults to `1`, but you should set this to `3` for production.
`cluster.imageName` - This allows you to override the Docker image used for the cluster. The chart will choose a default
  for you based on the setting you chose for `type`. If you need to run a configuration that is not supported, you can
  create your own Docker image. You can use the [postgres-containers](https://github.com/cloudnative-pg/postgres-containers)
  repository for a starting point.
  You will likely need to set your own repository access credentials via: `cluster.imagePullPolicy` and `cluster.imagePullSecrets`.
`cluster.storage.size` - The size of the persistent volume claim for the cluster. Defaults to `8Gi`. Every instance will
  have its own persistent volume claim.
`cluster.storage.storageClass` - The storage class to use for the persistent volume claim.
`cluster.resources` - The resource limits and requests for the cluster. You are strongly advised to use the same values
  for both limits and requests to ensure a [Guaranteed QoS](https://kubernetes.io/docs/concepts/workloads/pods/pod-qos/#guaranteed).
`cluster.affinity.topologyKey` - The chart sets it to `topology.kubernetes.io/zone` by default which is useful if you are

================================================
FILE: charts\paradedb\docs\long-running-tasks.md
================================================
# Executing Long-running Tasks

By setting `cluster.console.enabled=true`, the chart deploys a StatefulSet with a console pod for executing long-running tasks. This is useful for tasks that need to run in the background or for batch processing, such as `CREATE INDEX`. The intent is to use this console pod to run commands in the background without maintaining a persistent client connection. Because the console pod is on the cluster, it is less susceptible to network issues.

> [!NOTE]
> We don't provision a PodDisruption Budget (PDB) for the console StatefulSet. Node maintenance or other disruptions may cause the console pod to be evicted, killing your session.
>
> The console pod has `root` access so that you can use `apt install` to install any additional tools you may need. Keep in mind that while the root user home folder (`/root`) is persisted, any tools you install will not be persisted if the pod restarts.
>
> All the utilities in the pod are installed during the pod startup, so it may take a few seconds before they become available, after the pod has restarted.

## Connecting to the Console Pod

To use the console pod, you can run the following command:

```bash
kubectl --namespace <namespace> exec --stdin --tty statefulset/<cluster-name>-console -- bash
```

## Database credentials

We provide the database credentials as environment variables in the console pod. You can access them using:

* `$DB_APP_URI` - Connection URI for the default application user.
* `$DB_SUPERUSER_URI` - Connection URI for the `postgres` superuser.

## Executing queries

To run a command in the background you can use the `nohup` command. For example, to create an index in the background:

```bash
nohup psql "$DB_SUPERUSER_URI/<db-name>" -c "CREATE INDEX orders_idx ON orders USING bm25 (order_id, customer_name) WITH (key_field='order_id');" 2>&1 > command.log &
```

To check on the status of the command, you can use the `tail` command:

```bash
tail -f command.log
```

## Advanced usage with `screen`

You can also use the `screen` utility to run commands in the background and keep them running even if you disconnect from the console pod. Here are some basic commands to get you started:

* Start a new screen session

```bash
screen -S mysession
```

* List all screen sessions

```bash
screen -list
```

* To detach from a screen session without stopping it, press `Ctrl + A`, then `D`.
* You can reattach to a screen session with:

```bash
screen -r mysession
```


================================================
FILE: charts\paradedb\docs\recovery.md
================================================
# Recovery

This chart can be used to initiate a recovery operation of a CNPG cluster no matter if it was created with the chart or not.

CNPG does not support recovery in-place. Instead you need to create a new cluster that will be bootstrapped from the existing one or from a backup.

You can find more information about the recovery process in the [CNPG documentation](https://cloudnative-pg.io/documentation/current/backup_recovery).

There are 3 types of recovery possible with CNPG:

* Recovery from a backup object in the same Kubernetes namespace.
* Recovery from a Barman Object Store, that could be located anywhere.
* Streaming replication from an operating cluster using `pg_basebackup`.

When performing a recovery you are strongly advised to use the same configuration and PostgreSQL version as the original cluster.

To begin, create a `values.yaml` that contains the following:

1. Set `mode: recovery` to indicate that you want to bootstrap the new cluster from an existing one.
2. Set the `recovery.method` to the type of recovery you want to perform.
3. Set either the `recovery.backupName` or the Barman Object Store configuration - i.e. `recovery.provider` and appropriate S3, Azure or GCS configuration. In case of `pg_basebackup` complete the `recovery.pgBaseBackup` section.
4. Optionally set the `recovery.pitrTarget.time` in RFC3339 format to perform a point-in-time recovery (not applicable for `pgBaseBackup`).
5. Retain the identical PostgreSQL version and configuration as the original cluster.
6. Make sure you don't use the same backup section name as the original cluster. We advise you change the `path` within the storage location if you want to reuse the same storage location/bucket.
    One pattern is adding a version number at the end of the path, e.g. `/v1` or `/v2` after each recovery procedure.

Example recovery configurations can be found in the [examples](../examples) directory.


================================================
FILE: charts\paradedb\docs\runbooks\CNPGClusterHACritical.md
================================================
# CNPGClusterHACritical

## Description

The `CNPGClusterHACritical` alert is triggered when the CloudNativePG cluster has no ready standby replicas.

This alert may occur during a regular failover or a planned automated version upgrade on two-instance clusters, as there is a brief period when only the primary remains active while a failover completes.

On single-instance clusters, this alert will remain active at all times. If running with a single instance is intentional, consider silencing the alert.

## Impact

Without standby replicas, the cluster will incur downtime if the primary fails. While the primary instance remains online and able to serve queries, connections through the `-ro` endpoint will fail.

## Diagnosis

Identify the current primary instance using the [CloudNativePG Grafana Dashboard](https://grafana.com/grafana/dashboards/20417-cloudnativepg/) or by running:

```bash
kubectl get cluster paradedb -o 'jsonpath={"Current Primary: "}{.status.currentPrimary}{"; Target Primary: "}{.status.targetPrimary}{"\n"}' --namespace <namespace>
```

Since the primary is the only instance serving queries, avoid making any changes that could disrupt it.

To inspect cluster health and instance status:

- Get the status of the CloudNativePG cluster instances:

```bash
kubectl get pods -A -l "cnpg.io/podRole=instance" -o wide
```

- If any pods are Pending, describe them to identify the cause:

```bash
kubectl describe --namespace <namespace> pod/<pod-name>
```

- Inspect the cluster phase and reason:

```bash
kubectl get cluster paradedb -o 'jsonpath={.status.phase}{"\n"}{.status.phaseReason}{"\n"}' --namespace <namespace>
```

- Inspect the logs of the affected CloudNativePG instances:

```bash
kubectl logs --namespace <namespace> pod/<instance-pod-name>
```

- Inspect the CloudNativePG operator logs:

```bash
kubectl logs --namespace cnpg-system -l "app.kubernetes.io/name=cloudnative-pg"
```

## Mitigation

### Instance Failure

First, consult the [CloudNativePG Failure Modes](https://cloudnative-pg.io/documentation/current/failure_modes/) and [CloudNativePG Troubleshooting](https://cloudnative-pg.io/documentation/current/troubleshooting/) documentation for more information on the conditions when CloudNativePG is unable to heal instances and standard troubleshooting steps.

### Insufficient Storage

If the above diagnosis commands indicate that an instance’s storage or WAL disk is full, increase the cluster storage size. Refer to the CloudNativePG documentation for more information on how to [Resize the CloudNativePG Cluster Storage](https://cloudnative-pg.io/documentation/current/troubleshooting/#storage-is-full).

### Unknown

If the root cause remains unclear, recreating the affected pods can sometimes resolve the issue. Recreating a pod involves deleting the pod, its storage PVC, and its WAL storage PVC. This will trigger a full rebuild of the node from a base backup and can take several hours, depending on the size of the database. Note that pods should **always** be recreated one at a time to avoid increasing the load on the primary instance.

Before doing so, carefully verify that:

- You are connected to the correct cluster.
- You are deleting the correct pod.
- You are not deleting the active primary instance.

```bash
kubectl delete --namespace <namespace> pod/<pod-name> pvc/<pod-name> pvc/<pod-name>-wal
```


================================================
FILE: charts\paradedb\docs\runbooks\CNPGClusterHAWarning.md
================================================
# CNPGClusterHAWarning

## Description

The `CNPGClusterHAWarning` alert is triggered when the CloudNativePG cluster has fewer than two ready standby replicas.

This alert may occur during a regular failover or a planned automated version upgrade, as there is a brief period when only the primary remains active while a failover completes.

On single-instance or two-instance clusters, this alert will remain active at all times. If this is intentional, consider silencing the alert.

## Impact

With fewer than two standby replicas, the `-ro` endpoint is at risk of downtime if the last replica fails. The cluster will continue to function, but both the `-ro` and `-r` endpoints will operate with reduced capacity.

## Diagnosis

Identify the current primary instance using the [CloudNativePG Grafana Dashboard](https://grafana.com/grafana/dashboards/20417-cloudnativepg/) or by running:

```bash
kubectl get cluster paradedb -o 'jsonpath={"Current Primary: "}{.status.currentPrimary}{"; Target Primary: "}{.status.targetPrimary}{"\n"}' --namespace <namespace>
```

Since the primary is the only instance serving queries, avoid making any changes that could disrupt it.

To inspect cluster health and instance status:

- Get the status of the CloudNativePG cluster instances:

```bash
kubectl get pods -A -l "cnpg.io/podRole=instance" -o wide
```

- If any pods are Pending, describe them to identify the cause:

```bash
kubectl describe --namespace <namespace> pod/<pod-name>
```

- Inspect the cluster phase and reason:

```bash
kubectl get cluster paradedb -o 'jsonpath={.status.phase}{"\n"}{.status.phaseReason}{"\n"}' --namespace <namespace>
```

- Inspect the logs of the affected CloudNativePG instances:

```bash
kubectl logs --namespace <namespace> pod/<instance-pod-name>
```

- Inspect the CloudNativePG operator logs:

```bash
kubectl logs --namespace cnpg-system -l "app.kubernetes.io/name=cloudnative-pg"
```

## Mitigation

### Instance Failure

First, consult the [CloudNativePG Failure Modes](https://cloudnative-pg.io/documentation/current/failure_modes/) and [CloudNativePG Troubleshooting](https://cloudnative-pg.io/documentation/current/troubleshooting/) documentation for more information on the conditions when CloudNativePG is unable to heal instances and standard troubleshooting steps.

### Insufficient Storage

If the above diagnosis commands indicate that an instance’s storage or WAL disk is full, increase the cluster storage size. Refer to the CloudNativePG documentation for more information on how to [Resize the CloudNativePG Cluster Storage](https://cloudnative-pg.io/documentation/current/troubleshooting/#storage-is-full).

### Unknown

If the root cause remains unclear, recreating the affected pods can sometimes resolve the issue. Recreating a pod involves deleting the pod, its storage PVC, and its WAL storage PVC. This will trigger a full rebuild of the node from a base backup and can take several hours, depending on the size of the database. Note that pods should **always** be recreated one at a time to avoid increasing the load on the primary instance.

Before doing so, carefully verify that:

- You are connected to the correct cluster.
- You are deleting the correct pod.
- You are not deleting the active primary instance.

```bash
kubectl delete --namespace <namespace> pod/<pod-name> pvc/<pod-name> pvc/<pod-name>-wal
```


================================================
FILE: charts\paradedb\docs\runbooks\CNPGClusterHighConnectionsCritical.md
================================================
# CNPGClusterHighConnectionsCritical

## Description

The `CNPGClusterHighConnectionsCritical` alert is triggered when the number of connections on the CloudNativePG cluster instance exceeds 95% of its configured capacity.

## Impact

At 100% capacity, the instance will reject new connections, resulting in a service disruption.

## Diagnosis

Use the [CloudNativePG Grafana Dashboard](https://grafana.com/grafana/dashboards/20417-cloudnativepg/) to inspect the number of connections to the CloudNativePG cluster instances. Identify which instance is over capacity, and determine whether it is the primary or a standby replica.

You can check the current primary instance using the following command:

```bash
kubectl get cluster paradedb -o 'jsonpath={"Current Primary: "}{.status.currentPrimary}{"; Target Primary: "}{.status.targetPrimary}{"\n"}' --namespace <namespace>
```

## Mitigation

> [!IMPORTANT]
> Changing the `max_connections` parameter requires a restart of the CloudNativePG cluster instances. This will cause a restart of a standby instance and a switchover of the primary instance, causing a brief service disruption.

- Increase the maximum number of connections by setting the `max_connections` PostgreSQL parameter:
  - Helm: `cluster.postgresql.parameters.max_connections`

- Use connection pooling by enabling PgBouncer to reduce the number of connections to the database. PgBouncer itself requires connections, so temporarily increase `max_connections` while enabling it to avoid service disruption.

> [!NOTE]
> PostgreSQL sizes certain resources directly based on the value of `max_connections`. Each connection uses a portion of the `shared_buffers` memory as well as additional non-shared memory. As a result, increasing the `max_connections` parameter will increase the memory usage of the CloudNativePG cluster instances.


================================================
FILE: charts\paradedb\docs\runbooks\CNPGClusterHighConnectionsWarning.md
================================================
# CNPGClusterHighConnectionsWarning

## Description

The `CNPGClusterHighConnectionsWarning` alert is triggered when the number of connections on the CloudNativePG cluster instance exceeds 85% of its configured capacity.

## Impact

At 100% capacity, the instance will reject new connections, resulting in a service disruption.

## Diagnosis

Use the [CloudNativePG Grafana Dashboard](https://grafana.com/grafana/dashboards/20417-cloudnativepg/) to check the number of connections to the CloudNativePG cluster instances. Identify which instance is over capacity, and determine whether it is the primary or a standby replica.

You can check the current primary instance using the following command:

```bash
kubectl get cluster paradedb -o 'jsonpath={"Current Primary: "}{.status.currentPrimary}{"; Target Primary: "}{.status.targetPrimary}{"\n"}' --namespace <namespace>
```

## Mitigation

> [!IMPORTANT]
> Changing the `max_connections` parameter requires a restart of the CloudNativePG cluster instances. This will cause a restart of a standby instance and a switchover of the primary instance, causing a brief service disruption.

- Increase the maximum number of connections by setting the `max_connections` PostgreSQL parameter:
  - Helm: `cluster.postgresql.parameters.max_connections`

- Use connection pooling by enabling PgBouncer to reduce the number of connections to the database. PgBouncer itself requires connections, so temporarily increase `max_connections` while enabling it to avoid service disruption.

> [!NOTE]
> PostgreSQL sizes certain resources directly based on the value of `max_connections`. Each connection uses a portion of the `shared_buffers` memory as well as additional non-shared memory. As a result, increasing the `max_connections` parameter will increase the memory usage of the CloudNativePG cluster instances.


================================================
FILE: charts\paradedb\docs\runbooks\CNPGClusterHighPhysicalReplicationLagWarning.md
================================================
# CNPGClusterHighPhysicalReplicationLagWarning

## Description

The `CNPGClusterHighPhysicalReplicationLagWarning` alert is triggered when physical replication lag in the CloudNativePG cluster exceeds 1 second.

## Impact

High physical replication lag can cause the cluster replicas to become out of sync. Queries to the `-r` and `-ro` endpoints may return stale data. In the event of a failover, the data that has not yet been replicated from the primary to the replicas may be lost during failover.

## Diagnosis

Check replication status in the [CloudNativePG Grafana Dashboard](https://grafana.com/grafana/dashboards/20417-cloudnativepg/) or by running:

```bash
kubectl exec --namespace <namespace> --stdin --tty services/<cluster_name>-rw -- psql -c "SELECT * FROM pg_stat_replication;"
```

High physical replication lag can be caused by a number of factors, including:

- Network congestion on the node interface

Inspect the network interface statistics using the `Kubernetes Cluster` section of the [CloudNativePG Grafana Dashboard](https://grafana.com/grafana/dashboards/20417-cloudnativepg/).

- High CPU or memory load on primary or replicas

Inspect the CPU and Memory usage of the CloudNativePG cluster instances using the [CloudNativePG Grafana Dashboard](https://grafana.com/grafana/dashboards/20417-cloudnativepg/).

- Disk I/O bottlenecks on replicas

Inspect the disk IO statistics using the [CloudNativePG Grafana Dashboard](https://grafana.com/grafana/dashboards/20417-cloudnativepg/).

- Long-running queries

Inspect the `Stat Activity` section of the [CloudNativePG Grafana Dashboard](https://grafana.com/grafana/dashboards/20417-cloudnativepg/).

- Suboptimal PostgreSQL configuration, e.g. too few `max_wal_senders`. Set this to at least the number of cluster instances (default 10 is usually sufficient).

Inspect the `PostgreSQL Parameters` section of the [CloudNativePG Grafana Dashboard](https://grafana.com/grafana/dashboards/20417-cloudnativepg/).

## Mitigation

- Terminate long-running transactions that generate excessive changes.

```bash
kubectl exec -it services/cluster-rw --namespace <namespace> -- psql
```

- Increase the Memory and CPU resources of the instances under heavy load. This can be done by setting `cluster.resources.requests` and `cluster.resources.limits` in your Helm values. Set both `requests` and `limits` to the same value to achieve QoS Guaranteed. This will require a restart of the CloudNativePG cluster instances and a primary switchover, which will cause a brief service disruption.

- Enable `wal_compression` by setting the `cluster.postgresql.parameters.wal_compression` parameter to `on`. Doing so will reduce the size of the WAL files and can help reduce replication lag in a congested network. Changing `wal_compression` does not require a restart of the CloudNativePG cluster.

- Increase IOPS or throughput of the storage used by the cluster to alleviate disk I/O bottlenecks. This requires creating a new storage class with higher IOPS/throughput and rebuilding cluster instances and their PVCs one by one using the new storage class. This is a slow process that will also affect the cluster's availability.

If you decide to go this route:

1. Start by creating a new storage class. Storage classes are immutable, so you cannot change the storage class of existing Persistent Volume Claims (PVCs).

2. Make sure to only replace one instance at a time to avoid service disruption.

3. Double check you are deleting the correct pod.

4. Don't start with the active primary instance. Delete one of the standby replicas first.

```bash
kubectl delete --namespace <namespace> pod/<pod-name> pvc/<pod-name> pvc/<pod-name>-wal
```

- In the event that the cluster has 9+ instances, ensure that the `max_wal_senders` parameter is set to a value greater than or equal to the total number of instances in your cluster.


================================================
FILE: charts\paradedb\docs\runbooks\CNPGClusterInstancesOnSameNode.md
================================================
# CNPGClusterInstancesOnSameNode

## Description

The `CNPGClusterInstancesOnSameNode` alert is triggered when two or more database pods are scheduled on the same node. This is unexpected for CloudNativePG clusters, as each instance should run on a separate node to ensure high availability and fault tolerance.

This can be caused by insufficient nodes in the cluster or misconfigured scheduling rules, such as pod affinity/anti-affinity rules or tolerations.

## Impact

This configuration reduces high availability, as a node failure hosting multiple database pods will cause all of them to go down simultaneously.

## Diagnosis

To investigate node placement of database pods:

- List all database pods and their node assignments:

```bash
kubectl get pods -A -l "cnpg.io/podRole=instance" -o json | jq -r '["Namespace", "Pod", "Node"], ( .items[] | [.metadata.namespace, .metadata.name, .spec.nodeName]) | @tsv' | column -t
```

- Describe the cluster and check the affinity and tolerations configuration:

```bash
kubectl describe --namespace <namespace> clusters.postgresql.cnpg.io/paradedb
```

- Describe the pods:

```bash
kubectl describe pods -A -l "cnpg.io/podRole=instance"
```

## Mitigation

- Verify that you have more than a single node with no taint preventing pods from being scheduled on these nodes.

- Verify your [affinity](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/), taints, and tolerations configuration.

- Increase the instance CPU and Memory resources so that no node can host more than one instance.

For more information, please refer to the ["Scheduling"](https://cloudnative-pg.io/documentation/current/scheduling/) section of the documentation.


================================================
FILE: charts\paradedb\docs\runbooks\CNPGClusterLogicalReplicationErrors.md
================================================
# CNPGClusterLogicalReplicationErrors

## Description

The `CNPGClusterLogicalReplicationErrors` alert indicates that a logical replication subscription is experiencing errors during data replication. This includes:

1. **Apply Errors**: Errors that occur when applying received changes from the publisher
2. **Sync Errors**: Errors that occur during the initial table synchronization phase

- **Warning level**: Any error detected in the last 5 minutes
- **Critical level**: 5 or more errors in the last 5 minutes

## Impact

- **Data Inconsistency**: The subscriber may have missing or incorrect data
- **Replication Paused**: Depending on configuration, replication might stop on errors
- **Growing Lag**: Errors can cause replication to fall behind
- **Critical**: Persistent errors may lead to complete replication failure

## Diagnosis

### Step 1: Check Error Details

```bash
# Connect to the subscriber and check subscription status
kubectl exec -it svc/SUBSCRIBER-CLUSTER-rw -n NAMESPACE -- psql -c "
SELECT
    s.subname,
    s.subenabled,
    COALESCE(sss.apply_error_count, 0) AS apply_error_count,
    COALESCE(sss.sync_error_count, 0) AS sync_error_count,
    sss.stats_reset
FROM pg_subscription s
LEFT JOIN pg_stat_subscription_stats sss ON s.oid = sss.subid
WHERE COALESCE(sss.apply_error_count, 0) > 0 OR COALESCE(sss.sync_error_count, 0) > 0;
"

# Check the last error message
kubectl exec -it svc/SUBSCRIBER-CLUSTER-rw -n NAMESPACE -- psql -c "
SELECT
    s.subname,
    ss.last_msg_receipt_time,
    ss.latest_end_time,
    CASE
        WHEN COALESCE(sss.apply_error_count, 0) > 0 THEN 'Apply errors detected'
        WHEN COALESCE(sss.sync_error_count, 0) > 0 THEN 'Sync errors detected'
        ELSE 'No errors detected'
    END as error_type
FROM pg_subscription s
LEFT JOIN pg_stat_subscription ss ON s.oid = ss.subid
LEFT JOIN pg_stat_subscription_stats sss ON s.oid = sss.subid;
"
```

### Step 2: Check PostgreSQL Logs

```bash
# Get the pod name
POD=$(kubectl get pods -n NAMESPACE -l app=postgresql -o name | head -1 | cut -d/ -f2)

# Check recent logs for errors
kubectl logs -n NAMESPACE $POD --tail=100 | grep -i "replication\|subscription\|error"

# Stream logs for real-time monitoring
kubectl logs -n NAMESPACE $POD -f | grep -i "replication\|subscription\|error"
```

### Step 3: Identify Common Error Patterns

1. **Constraint Violations**:
   ```bash
   kubectl logs -n NAMESPACE $POD | grep "violates.*constraint"
   ```

2. **Permission Issues**:
   ```bash
   kubectl logs -n NAMESPACE $POD | grep "permission denied\|role"
   ```

3. **Data Type Mismatches**:
   ```bash
   kubectl logs -n NAMESPACE $POD | grep "invalid input syntax\|datatype"
   ```

4. **Connection Issues**:
   ```bash
   kubectl logs -n NAMESPACE $POD | grep "connection\|timeout"
   ```

### Step 4: Verify Publication/Subscription Configuration

```bash
# On publisher - check publication tables
kubectl exec -it svc/PUBLISHER-CLUSTER-rw -n NAMESPACE -- psql -c "
SELECT pubname, puballtables, pubinsert, pubupdate, pubdelete
FROM pg_publication;
"

# On subscriber - check subscription details
kubectl exec -it svc/SUBSCRIBER-CLUSTER-rw -n NAMESPACE -- psql -c "
SELECT
    subname,
    subconninfo,
    subslotname,
    subsynccommit,
    subpublications
FROM pg_subscription;
"

# Check which tables are being replicated
kubectl exec -it svc/SUBSCRIBER-CLUSTER-rw -n NAMESPACE -- psql -c "
SELECT
    sr.srrelid::regclass as table_name,
    sr.srsubstate as state
FROM pg_subscription_rel sr
JOIN pg_class c ON sr.srrelid = c.oid
WHERE sr.srsubstate NOT IN ('r', 's');  -- Not ready or synchronizing
"
```

### Step 5: Check for Data Conflicts

```bash
# Check for conflicting primary keys
kubectl exec -it svc/SUBSCRIBER-CLUSTER-rw -n NAMESPACE -- psql -c "
SELECT schemaname, tablename, attname, n_distinct, correlation
FROM pg_stats
WHERE schemaname NOT IN ('pg_catalog', 'information_schema')
ORDER BY schemaname, tablename;
"
```

## Resolution

### For Constraint Violations

1. **Identify the Constraint**:
   ```sql
   -- Find the violated constraint
   SELECT conname, contype, pg_get_constraintdef(oid)
   FROM pg_constraint
   WHERE conrelid = 'table_name'::regclass;
   ```

2. **Resolve Data Conflicts**:
   ```sql
   -- Option 1: Remove conflicting data on subscriber
   DELETE FROM table_name WHERE id = conflicting_id;

   -- Option 2: Update conflicting data
   UPDATE table_name
   SET conflicting_column = new_value
   WHERE id = conflicting_id;

   -- Option 3: Temporarily disable constraint (use with caution)
   ALTER TABLE table_name DISABLE TRIGGER ALL;
   -- After sync, re-enable
   ALTER TABLE table_name ENABLE TRIGGER ALL;
   ```

### For Permission Issues

1. **Check Subscription Owner**:
   ```sql
   SELECT usename, usesuper, usecreatedb
   FROM pg_user
   WHERE usename = current_user;
   ```

2. **Grant Necessary Permissions**:
   ```sql
   -- On subscriber, ensure subscription owner has rights
   GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEM

================================================
FILE: charts\paradedb\docs\runbooks\CNPGClusterLogicalReplicationLagging.md
================================================
# CNPGClusterLogicalReplicationLagging

## Description

The `CNPGClusterLogicalReplicationLagging` alert indicates that a CloudNativePG cluster with a logical replication subscription is falling behind its publisher. This alert aggregates three types of lag:

1. **Receipt Lag** (`cnpg_pg_stat_subscription_receipt_lag_seconds`): Time since the last WAL message was received from the publisher
2. **Apply Lag** (`cnpg_pg_stat_subscription_apply_lag_seconds`): Time delay between receiving and actually applying changes
3. **LSN Distance** (`cnpg_pg_stat_subscription_buffered_lag_bytes`): Amount of WAL data buffered but not yet applied (measured in bytes)

- **Warning level**: Any lag metric exceeds 60s or 1GB
- **Critical level**: Any lag metric exceeds 300s or 4GB

## Impact

The cluster remains operational, but:
- Queries to the subscriber will return stale data
- Data inconsistency between publisher and subscriber
- In critical cases, disk space on the publisher may fill up with unapplied WAL
- Recovery time increases with lag duration

## Diagnosis

### Step 1: Identify the Lag Type

Connect to the subscriber and check the current state:

```bash
kubectl exec -it svc/SUBSCRIBER-CLUSTER-rw -n NAMESPACE -- psql -c "
SELECT
    s.subname,
    s.subenabled AS enabled,
    EXTRACT(EPOCH FROM (NOW() - ss.last_msg_receipt_time)) AS receipt_lag_seconds,
    EXTRACT(EPOCH FROM (NOW() - ss.latest_end_time)) AS apply_lag_seconds,
    COALESCE(pg_wal_lsn_diff(ss.received_lsn, ss.latest_end_lsn), 0) AS pending_bytes,
    CASE
        WHEN EXTRACT(EPOCH FROM (NOW() - ss.last_msg_receipt_time)) > 60 THEN 'High receipt lag'
        WHEN EXTRACT(EPOCH FROM (NOW() - ss.latest_end_time)) > 60 THEN 'High apply lag'
        WHEN COALESCE(pg_wal_lsn_diff(ss.received_lsn, ss.latest_end_lsn), 0) > 1024^3 THEN 'High LSN distance'
        ELSE 'Healthy'
    END as primary_issue
FROM pg_subscription s
LEFT JOIN pg_stat_subscription ss ON s.oid = ss.subid;
"
```

### Step 2: Check Network Connectivity

For **receipt lag** issues:

```bash
# Check network latency between publisher and subscriber
kubectl exec -it svc/SUBSCRIBER-CLUSTER-rw -n NAMESPACE -- \
  ping -c 10 PUBLISHER-HOSTNAME

# Check bandwidth (if tools are available)
kubectl exec -it svc/SUBSCRIBER-CLUSTER-rw -n NAMESPACE -- \
  nc -zv PUBLISHER-HOSTNAME 5432
```

### Step 3: Check Resource Utilization

For **apply lag** issues:

```bash
# Check CPU/Memory usage on subscriber
kubectl top pod -n NAMESPACE -l app=postgresql

# Check disk I/O
kubectl exec -it svc/SUBSCRIBER-CLUSTER-rw -n NAMESPACE -- \
  iostat -x 1 5

# Check for long-running queries
kubectl exec -it svc/SUBSCRIBER-CLUSTER-rw -n NAMESPACE -- psql -c "
SELECT pid, now() - pg_stat_activity.query_start AS duration, query
FROM pg_stat_activity
WHERE state = 'active' AND now() - query_start > interval '5 minutes'
ORDER BY duration DESC;
"
```

### Step 4: Check Configuration

```bash
# Verify replication worker settings
kubectl exec -it svc/SUBSCRIBER-CLUSTER-rw -n NAMESPACE -- psql -c "
SHOW max_worker_processes;
SHOW max_logical_replication_workers;
SHOW max_parallel_workers;
"

# Ensure adequate worker processes:
# max_worker_processes >= max_parallel_workers + max_logical_replication_workers
```

### Step 5: Monitor Trends

Use the CloudNativePG Grafana Dashboard:
- Navigate to the Logical Replication section
- Examine all lag graphs over time
- Check if lag is stable, increasing, or fluctuating
- Correlate with workload spikes

## Resolution

### For Receipt Lag (Network Issues)

1. **Check Network Latency**:
   - Verify network connectivity between clusters
   - Consider placing clusters in the same region/availability zone
   - Check for network congestion or throttling

2. **Optimize Network Configuration**:
   ```yaml
   # In the subscriber's postgresql configuration
   postgresql:
     parameters:
       wal_sender_timeout: '60s'
       wal_receiver_status_interval: '10s'
   ```

### For Apply Lag (Resource Issues)

1. **Scale Up Resources**:
   ```yaml
   # Increase CPU/memory for the subscriber
   resources:
     requests:
       cpu: 2
       memory: 8Gi
     limits:
       cpu: 4
       memory: 16Gi
   ```

2. **Optimize Disk I/O**:
   - Use faster storage (SSD if not already)
   - Consider increasing storage IOPS
   - Check for disk bottlenecks

3. **Tune PostgreSQL Settings**:
   ```yaml
   postgresql:
     parameters:
       # Increase for better write performance
       wal_buffers: '16MB'
       checkpoint_completion_target: 0.9
       # Reduce checkpoint frequency
       max_wal_size: '4GB'
       min_wal_size: '1GB'
   ```

### For High Transaction Volume

1. **Batch Large Transactions**:
   - Break large transactions into smaller ones
   - Use `COPY` instead of many INSERT statements

2. **Consider Row Filtering**:
   ```sql
   -- Only replicate needed data
   ALTER PUBLICATION publication_name SET (publish = 'insert, update, delete');
   ALTER PUBLICATION publication_name ADD TABLE table_name

================================================
FILE: charts\paradedb\docs\runbooks\CNPGClusterLogicalReplicationStopped.md
================================================
# CNPGClusterLogicalReplicationStopped

## Description

The `CNPGClusterLogicalReplicationStopped` alert indicates that a logical replication subscription is not actively replicating data. This can occur in two scenarios:

1. **Disabled Subscription**: The subscription has been explicitly disabled (`enabled = false`)
2. **Stuck Subscription**: The subscription is enabled but has no active worker process (no PID) with pending data

- **Warning level**: Subscription stopped for 5 minutes
- **Critical level**: Subscription stopped for 15 minutes

## Impact

- **No Data Replication**: The subscriber will not receive any updates from the publisher
- **Data Divergence**: The subscriber data becomes increasingly stale
- **Disk Space**: WAL files may accumulate on the publisher
- **Critical**: Extended downtime may require full resynchronization

## Diagnosis

### Step 1: Check Subscription Status

```bash
# Check all subscriptions and their status
kubectl exec -it svc/SUBSCRIBER-CLUSTER-rw -n NAMESPACE -- psql -c "
SELECT
    s.subname,
    s.subenabled AS enabled,
    CASE
        WHEN NOT s.subenabled THEN 'Explicitly disabled'
        WHEN ss.pid IS NULL AND COALESCE(pg_wal_lsn_diff(ss.received_lsn, ss.latest_end_lsn), 0) > 0 THEN 'Stuck (no worker)'
        WHEN ss.pid IS NOT NULL THEN 'Active'
        ELSE 'Unknown'
    END as status,
    COALESCE(pg_wal_lsn_diff(ss.received_lsn, ss.latest_end_lsn), 0) AS pending_bytes,
    ss.pid IS NOT NULL AS has_worker
FROM pg_subscription s
LEFT JOIN pg_stat_subscription ss ON s.oid = ss.subid;
"
```

### Step 2: Check Worker Process

```bash
# Check if replication worker is running
kubectl exec -it svc/SUBSCRIBER-CLUSTER-rw -n NAMESPACE -- psql -c "
SELECT
    pid,
    application_name,
    state,
    backend_type,
    query_start
FROM pg_stat_activity
WHERE application_name LIKE '%subscription%' OR backend_type = 'logical replication worker';
"
```

### Step 3: Verify Subscription Details

```bash
# Get subscription configuration
kubectl exec -it svc/SUBSCRIBER-CLUSTER-rw -n NAMESPACE -- psql -c "
SELECT
    subname,
    subconninfo,
    subsynccommit,
    subslotname,
    subpublications
FROM pg_subscription;
"
```

### Step 4: Check PostgreSQL Logs

```bash
# Get the pod name
POD=$(kubectl get pods -n NAMESPACE -l app=postgresql -o name | head -1 | cut -d/ -f2)

# Check for subscription-related errors
kubectl logs -n NAMESPACE $POD --tail=200 | grep -i "subscription\|replication\|worker"
```

### Step 5: Test Connectivity to Publisher

```bash
# Extract connection info from subscription
kubectl exec -it svc/SUBSCRIBER-CLUSTER-rw -n NAMESPACE -- psql -c "
SELECT subconninfo FROM pg_subscription WHERE subname = 'your_subscription_name';
" | grep -o "host=[^ ]*" | cut -d= -f2

# Test connection
kubectl exec -it svc/SUBSCRIBER-CLUSTER-rw -n NAMESPACE -- \
  psql "host=PUBLISHER-HOST port=5432 dbname=DATABASE user=USER" -c "SELECT version();"
```

## Resolution

### If Subscription is Disabled

1. **Check if Disable Was Intentional**:
   ```bash
   # Check recent activity
   kubectl get events -n NAMESPACE --field-selector reason=SubscriptionDisabled

   # Check audit logs if RBAC is enabled
   kubectl auth can-i create subscriptions
   ```

2. **Enable the Subscription**:
   ```sql
   -- Enable the subscription
   ALTER SUBSCRIPTION subscription_name ENABLE;
   ```

   Or using kubectl:
   ```bash
   kubectl cnpg subscription enable subscription_name -n NAMESPACE
   ```

### If Subscription is Stuck

1. **Check for Worker Resource Limits**:
   ```bash
   # Check max_logical_replication_workers
   kubectl exec -it svc/SUBSCRIBER-CLUSTER-rw -n NAMESPACE -- psql -c "
   SHOW max_logical_replication_workers;
   SHOW max_worker_processes;
   "

   # Count active replication workers
   kubectl exec -it svc/SUBSCRIBER-CLUSTER-rw -n NAMESPACE -- psql -c "
   SELECT COUNT(*) FROM pg_stat_activity WHERE backend_type = 'logical replication worker';
   "
   ```

2. **Increase Worker Limits if Needed**:
   ```yaml
   # In the CNPG cluster configuration
   postgresql:
     parameters:
       max_logical_replication_workers: 10
       max_worker_processes: 20
       max_replication_slots: 10
   ```

3. **Restart the Subscription**:
   ```bash
   # First try to restart just the subscription
   kubectl cnpg subscription restart subscription_name -n NAMESPACE

   # If that doesn't work, restart the entire cluster
   kubectl cnpg restart subscriber-cluster -n NAMESPACE
   ```

4. **Check for Stuck Transactions**:
   ```sql
   -- Check for long-running transactions that might block replication
   SELECT pid, now() - pg_stat_activity.query_start AS duration, query
   FROM pg_stat_activity
   WHERE state = 'active'
     AND now() - query_start > interval '10 minutes'
     AND pid NOT IN (SELECT pid FROM pg_stat_activity WHERE application_name LIKE '%subscription%');

   -- Terminate blocking transactions if necessary
   SELECT pg_terminate_backend(pid);
   ```

### If Connection Issues

1. **

================================================
FILE: charts\paradedb\docs\runbooks\CNPGClusterLowDiskSpaceCritical.md
================================================
# CNPGClusterLowDiskSpaceCritical

## Description

The `CNPGClusterLowDiskSpaceCritical` alert is triggered when disk usage on any CloudNativePG cluster volume exceeds 90%. It may occur on the following volumes:

- The PVC hosting `PGDATA` (`storage` section)
- The PVC hosting WAL files (`walStorage` section)
- Any PVC hosting a tablespace (`tablespaces` section)

## Impact

At 100% disk usage, the cluster will experience downtime and potential data loss.

High disk usage can also cause fragmentation, where files are split due to insufficient contiguous free space, significantly increasing random I/O and degrading performance. Disk fragmentation can start happening at ~80% disk space usage.

## Diagnosis

Check disk usage metrics in the [CloudNativePG Grafana Dashboard](https://grafana.com/grafana/dashboards/20417-cloudnativepg/) to identify which volume is nearing capacity.

## Mitigation

If the WAL (Write-Ahead Logging) volume is filling and you have continuous archiving enabled, verify that WAL archiving is functioning correctly. A buildup of WAL files in `pg_wal` indicates an issue. Monitor the `cnpg_collector_pg_wal_archive_status` metric and ensure the number of `ready` files is not steadily increasing.

For more details, see the [CloudNativePG documentation on resizing storage](https://cloudnative-pg.io/documentation/current/troubleshooting/#storage-is-full).


================================================
FILE: charts\paradedb\docs\runbooks\CNPGClusterLowDiskSpaceWarning.md
================================================
# CNPGClusterLowDiskSpaceWarning

## Description

The `CNPGClusterLowDiskSpaceWarning` alert is triggered when disk usage on any CloudNativePG cluster volume exceeds 80%. It may occur on the following volumes:

- The PVC hosting `PGDATA` (`storage` section)
- The PVC hosting WAL files (`walStorage` section)
- Any PVC hosting a tablespace (`tablespaces` section)

## Impact

At 100% disk usage, the cluster will experience downtime and potential data loss.

High disk usage can also cause fragmentation, where files are split due to insufficient contiguous free space, significantly increasing random I/O and degrading performance. Disk fragmentation can start happening at ~80% disk space usage.

## Diagnosis

Check disk usage metrics in the [CloudNativePG Grafana Dashboard](https://grafana.com/grafana/dashboards/20417-cloudnativepg/) to identify which volume is nearing capacity.

## Mitigation

If the WAL (Write-Ahead Logging) volume is filling and you have continuous archiving enabled, verify that WAL archiving is functioning correctly. A buildup of WAL files in `pg_wal` indicates an issue. Monitor the `cnpg_collector_pg_wal_archive_status` metric and ensure the number of `ready` files is not steadily increasing.

For more details, see the [CloudNativePG documentation on resizing storage](https://cloudnative-pg.io/documentation/current/troubleshooting/#storage-is-full).


================================================
FILE: charts\paradedb\docs\runbooks\CNPGClusterOffline.md
================================================
# CNPGClusterOffline

## Description

The `CNPGClusterOffline` alert is triggered when no CloudNativePG instances are ready.

## Impact

When the cluster is offline, applications cannot access the database, resulting in a full service disruption.

## Diagnosis

To investigate why the cluster is offline:

- Get the status of the CloudNativePG cluster instances:

```bash
kubectl get pods -A -l "cnpg.io/podRole=instance" -o wide
```

- Inspect the logs of the affected CloudNativePG instances:

```bash
kubectl logs --namespace <namespace> pod/<instance-pod-name>
```

- Inspect the CloudNativePG operator logs:

```bash
kubectl logs --namespace cnpg-system -l "app.kubernetes.io/name=cloudnative-pg"
```

## Mitigation

Refer to the [CloudNativePG Failure Modes](https://cloudnative-pg.io/documentation/current/failure_modes/) and [CloudNativePG Troubleshooting](https://cloudnative-pg.io/documentation/current/troubleshooting/) documentation for guidance on troubleshooting and recovery.


================================================
FILE: charts\paradedb\docs\runbooks\CNPGClusterPhysicalReplicationLag.md
================================================
# CNPGClusterPhysicalReplicationLag

## Description

The `CNPGClusterPhysicalReplicationLag` alerts indicate that physical replication lag in the CloudNativePG cluster is exceeding acceptable thresholds. Physical replication lag measures how far behind the standby replicas are from the primary instance.

- **Warning level**: Replication lag exceeds 1 second
- **Critical level**: Replication lag exceeds 15 seconds

## Impact

Physical replication lag can cause the cluster replicas to become out of sync. Queries to the `-r` and `-ro` endpoints may return stale data. In the event of a failover, the data that has not yet been replicated from the primary to the replicas may be lost during failover.

- **Warning**: Minor data staleness, acceptable for read-heavy workloads with some tolerance for outdated data
- **Critical**: Significant data loss risk during failover, stale data affecting business operations

## Diagnosis

### Step 1: Check Replication Status

Check replication status in the [CloudNativePG Grafana Dashboard](https://grafana.com/grafana/dashboards/20417-cloudnativepg/) or by running:

```bash
kubectl exec --namespace <namespace> --stdin --tty services/<cluster_name>-rw -- psql -c "SELECT * FROM pg_stat_replication;"
```

### Step 2: Identify Common Causes

High physical replication lag can be caused by a number of factors:

**Network Issues:**
- Network congestion on the node interface
- Insufficient bandwidth between primary and replicas

```bash
# Inspect network interface statistics
kubectl exec -it <pod-name> -- ss -i
```

**Resource Contention:**
- High CPU or memory load on primary or replicas
- Disk I/O bottlenecks on replicas

```bash
# Check resource usage
kubectl top pods -n <namespace> -l cnpg.io/podRole=instance

# Check disk I/O
kubectl exec -it <pod-name> -- iostat -x 1 5
```

**Database Issues:**
- Long-running queries blocking replication
- Suboptimal PostgreSQL configuration

```bash
# Check for long-running queries
kubectl exec -it services/<cluster_name>-rw -- psql -c "
SELECT pid, now() - pg_stat_activity.query_start AS duration, query
FROM pg_stat_activity
WHERE state = 'active'
  AND now() - query_start > interval '5 minutes'
ORDER BY duration DESC;
"
```

### Step 3: Check PostgreSQL Configuration

Inspect the `PostgreSQL Parameters` section of the [CloudNativePG Grafana Dashboard](https://grafana.com/grafana/dashboards/20417-cloudnativepg/) or check directly:

```bash
kubectl exec -it services/<cluster_name>-rw -- psql -c "
SHOW max_wal_senders;
SHOW wal_compression;
SHOW max_replication_slots;
"
```

## Resolution

### For Warning Level Alerts (1-15 seconds lag)

1. **Monitor Resource Usage:**
   - Check CPU and Memory usage of the CloudNativePG cluster instances
   - Monitor network traffic between primary and replicas
   - Review disk I/O statistics

2. **Identify and Address Minor Issues:**
   - Look for and optimize long-running queries
   - Check for temporary resource spikes
   - Ensure adequate network bandwidth

### For Critical Level Alerts (>15 seconds lag)

1. **Immediate Actions:**
   ```bash
   # Terminate long-running transactions that generate excessive changes
   kubectl exec -it services/<cluster_name>-rw -- psql -c "
   SELECT pg_terminate_backend(pid)
   FROM pg_stat_activity
   WHERE state = 'active'
     AND now() - query_start > interval '30 minutes'
     AND query NOT LIKE '%autovacuum%';
   "
   ```

2. **Scale Up Resources:**
   Increase the Memory and CPU resources of the instances under heavy load. This can be done by setting `cluster.resources.requests` and `cluster.resources.limits` in your Helm values. Set both `requests` and `limits` to the same value to achieve QoS Guaranteed.

   ```yaml
   cluster:
     resources:
       requests:
         cpu: 4
         memory: 16Gi
       limits:
         cpu: 4
         memory: 16Gi
   ```

3. **Enable WAL Compression:**
   ```yaml
   cluster:
     postgresql:
       parameters:
         wal_compression: "on"
   ```
   This will reduce the size of the WAL files and can help reduce replication lag in congested networks. Changing `wal_compression` does not require a restart.

4. **Upgrade Storage Performance:**
   Increase IOPS or throughput of the storage used by the cluster to alleviate disk I/O bottlenecks.

   **Process:**
   1. Create a new storage class with higher IOPS/throughput
   2. Replace cluster instances one by one using the new storage class
   3. Start with standby replicas, not the primary
   4. Delete and recreate each instance with new storage:

   ```bash
   kubectl delete --namespace <namespace> pod/<pod-name> pvc/<pod-name> pvc/<pod-name>-wal
   ```

5. **Increase WAL Senders:**
   For clusters with 9+ instances, ensure `max_wal_senders` is adequate:
   ```yaml
   cluster:
     postgresql:
       parameters:
         max_wal_senders: 15  # Should be >= number of instances
   ```

## Prevention

1. **Resource Planning:**
   - Allocate adequate CPU, memory, and storage IOPS
   - Monit

================================================
FILE: charts\paradedb\docs\runbooks\CNPGClusterZoneSpreadWarning.md
================================================
# CNPGClusterZoneSpreadWarning

## Description

The `CNPGClusterZoneSpreadWarning` alert is triggered when pods are not evenly distributed across availability zones. To be more precise, the alert is raised when the number of pods exceeds the number of zones and the cluster runs in fewer than three zones.

This can be caused by insufficient nodes in the cluster or by misconfigured scheduling rules, such as pod affinity/anti-affinity rules or tolerations.

## Impact

The uneven distribution of pods across availability zones increases the risk of a single point of failure if a zone becomes unavailable.

## Diagnosis

To investigate pod distribution across zones:

- Get the status of the CloudNativePG cluster instances:

```bash
kubectl get pods -A -l "cnpg.io/podRole=instance" -o wide
```

- Get the nodes and their respective zones:

```bash
kubectl get nodes --label-columns topology.kubernetes.io/zone
```

- Identify the current primary instance with the following command:

```bash
kubectl get cluster paradedb -o 'jsonpath={"Current Primary: "}{.status.currentPrimary}{"; Target Primary: "}{.status.targetPrimary}{"\n"}' --namespace <namespace>
```

## Mitigation

1. Verify that there are more than one schedulable node per availability zone, with no taints preventing pod placement.

2. Verify your [affinity](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/), taints, and tolerations configuration.

3. Delete pods and PVCs that are not in the desired availability zone. The CloudNativePG operator will automatically create replacement pods. Always delete pods one at a time to avoid placing excess load on the primary instance.

Before doing so, carefully verify that:

- You are deleting the correct pod.
- You are not deleting the active primary instance.

```bash
kubectl delete --namespace <namespace> pod/<pod-name> pvc/<pod-name> pvc/<pod-name>-wal
```


================================================
FILE: charts\paradedb\monitoring\paradedb-dashboard.json
================================================
{
  "annotations": {
    "list": [
      {
        "builtIn": 1,
        "datasource": {
          "type": "datasource",
          "uid": "grafana"
        },
        "enable": true,
        "hide": true,
        "iconColor": "rgba(0, 211, 255, 1)",
        "name": "Annotations & Alerts",
        "target": {
          "limit": 100,
          "matchAny": false,
          "tags": [],
          "type": "dashboard"
        },
        "type": "dashboard"
      }
    ]
  },
  "editable": true,
  "fiscalYearStartMonth": 0,
  "graphTooltip": 1,
  "id": 89,
  "links": [
    {
      "asDropdown": false,
      "icon": "external link",
      "includeVars": false,
      "keepTime": false,
      "tags": [
        "cloudnativepg"
      ],
      "targetBlank": false,
      "title": "Related Dashboards",
      "tooltip": "",
      "type": "dashboards",
      "url": ""
    }
  ],
  "panels": [
    {
      "fieldConfig": {
        "defaults": {},
        "overrides": []
      },
      "gridPos": {
        "h": 12,
        "w": 5,
        "x": 0,
        "y": 0
      },
      "id": 676,
      "options": {
        "alertInstanceLabelFilter": "{namespace=~\"$namespace\"}",
        "alertName": "",
        "dashboardAlerts": false,
        "folder": "",
        "groupBy": [],
        "groupMode": "default",
        "maxItems": 20,
        "showInactiveAlerts": false,
        "sortOrder": 1,
        "stateFilter": {
          "error": true,
          "firing": true,
          "noData": false,
          "normal": true,
          "pending": true
        },
        "viewMode": "list"
      },
      "pluginVersion": "11.5.1",
      "title": "Alerts",
      "type": "alertlist"
    },
    {
      "fieldConfig": {
        "defaults": {},
        "overrides": []
      },
      "gridPos": {
        "h": 1,
        "w": 4,
        "x": 5,
        "y": 0
      },
      "id": 586,
      "options": {
        "code": {
          "language": "plaintext",
          "showLineNumbers": false,
          "showMiniMap": false
        },
        "content": "",
        "mode": "markdown"
      },
      "pluginVersion": "11.5.1",
      "title": "Health",
      "type": "text"
    },
    {
      "fieldConfig": {
        "defaults": {},
        "overrides": []
      },
      "gridPos": {
        "h": 1,
        "w": 9,
        "x": 9,
        "y": 0
      },
      "id": 336,
      "options": {
        "code": {
          "language": "plaintext",
          "showLineNumbers": false,
          "showMiniMap": false
        },
        "content": "",
        "mode": "markdown"
      },
      "pluginVersion": "11.5.1",
      "title": "Overview",
      "type": "text"
    },
    {
      "fieldConfig": {
        "defaults": {},
        "overrides": []
      },
      "gridPos": {
        "h": 1,
        "w": 3,
        "x": 18,
        "y": 0
      },
      "id": 352,
      "options": {
        "code": {
          "language": "plaintext",
          "showLineNumbers": false,
          "showMiniMap": false
        },
        "content": "",
        "mode": "markdown"
      },
      "pluginVersion": "11.5.1",
      "title": "Storage",
      "type": "text"
    },
    {
      "fieldConfig": {
        "defaults": {},
        "overrides": []
      },
      "gridPos": {
        "h": 1,
        "w": 3,
        "x": 21,
        "y": 0
      },
      "id": 354,
      "options": {
        "code": {
          "language": "plaintext",
          "showLineNumbers": false,
          "showMiniMap": false
        },
        "content": "",
        "mode": "markdown"
      },
      "pluginVersion": "11.5.1",
      "title": "Backups",
      "type": "text"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "description": "Cluster Replication Health represents the availability of replica servers available to replace the primary in case of a failure.",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "mappings": [
            {
              "options": {
                "0": {
                  "color": "green",
                  "index": 1,
                  "text": "Healthy"
                },
                "-1": {
                  "color": "red",
                  "index": 0,
                  "text": "None"
                }
              },
              "type": "value"
            },
            {
              "options": {
                "from": 1,
                "result": {
                  "color": "orange",
                  "index": 2,
                  "text": "Degraded"
                },
                "to": 999
              },
              "type": "range"
            }
          ],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": null
              }
            ]
          }
        },
        "overrides": []
      },
      "gridP

================================================
FILE: charts\paradedb\templates\NOTES.txt
================================================
{{- if .Values.pooler -}}
  {{ fail ".Values.pooler has been deprecated. Use .Values.poolers instead." }}
{{- end -}}

{{- if gt (omit .Values.cluster.postgresql "parameters" "synchronous" "pg_hba" "pg_ident" "syncReplicaElectionConstraint" "shared_preload_libraries" "ldap" "promotionTimeout" "enableAlterSystem" | keys | len) 0 -}}
  {{ fail ".Values.cluster.postgresql has been deprecated. Use .Values.cluster.postgresql.parameters instead." }}
{{- end -}}


{{ if .Release.IsInstall }}
The {{ include "cluster.color-info" (include "cluster.fullname" .) }} cluster has been installed successfully.
{{ else if .Release.IsUpgrade }}
The {{ include "cluster.color-info" (include "cluster.fullname" .) }} cluster has been upgraded successfully.
{{ end }}

   ██████   ██                       ██ ████     ██             ██   ██                  ███████    ████████
  ██░░░░██ ░██                      ░██░██░██   ░██            ░██  ░░                  ░██░░░░██  ██░░░░░░██
 ██    ░░  ░██  ██████  ██   ██     ░██░██░░██  ░██  ██████   ██████ ██ ██    ██  █████ ░██   ░██ ██      ░░
░██        ░██ ██░░░░██░██  ░██  ██████░██ ░░██ ░██ ░░░░░░██ ░░░██░ ░██░██   ░██ ██░░░██░███████ ░██
░██        ░██░██   ░██░██  ░██ ██░░░██░██  ░░██░██  ███████   ░██  ░██░░██ ░██ ░███████░██░░░░  ░██    █████
░░██    ██ ░██░██   ░██░██  ░██░██  ░██░██   ░░████ ██░░░░██   ░██  ░██ ░░████  ░██░░░░ ░██      ░░██  ░░░░██
 ░░██████  ███░░██████ ░░██████░░██████░██    ░░███░░████████  ░░██ ░██  ░░██   ░░██████░██       ░░████████
  ░░░░░░  ░░░  ░░░░░░   ░░░░░░  ░░░░░░ ░░      ░░░  ░░░░░░░░    ░░  ░░    ░░     ░░░░░░ ░░         ░░░░░░░░

Cheatsheet
----------

Run Helm Tests:
{{ include "cluster.color-info" (printf "helm test --namespace %s %s" .Release.Namespace .Release.Name) }}

Get a list of all base backups:
{{ include "cluster.color-info" (printf "kubectl --namespace %s get backups --selector cnpg.io/cluster=%s" .Release.Namespace (include "cluster.fullname" .)) }}

Connect to the cluster's primary instance:
{{ include "cluster.color-info" (printf "kubectl --namespace %s exec --stdin --tty services/%s-rw -- bash" .Release.Namespace (include "cluster.fullname" .)) }}

{{ if .Values.cluster.console.enabled -}}
Connect to the console pod for executing long-running tasks (e.g. `CREATE INDEX`):
{{ include "cluster.color-info" (printf "kubectl --namespace %s exec --stdin --tty statefulsets/%s-console -- bash" .Release.Namespace (include "cluster.fullname" .)) }}
{{- end }}

Configuration
-------------

{{- $redundancyColor := "" -}}
{{- if lt (int .Values.cluster.instances) 2 }}
  {{- $redundancyColor = "error" -}}
{{- else if lt (int .Values.cluster.instances) 3 -}}
  {{- $redundancyColor = "warning" -}}
{{- else -}}
  {{- $redundancyColor = "ok" -}}
{{- end }}

{{- $scheduledBackups := (first .Values.backups.scheduledBackups).name -}}
{{- range (rest .Values.backups.scheduledBackups) -}}
  {{ $scheduledBackups = printf "%s, %s" $scheduledBackups .name }}
{{- end -}}
{{- if eq (len .Values.backups.scheduledBackups) 0 }}
  {{- $scheduledBackups = "None" -}}
{{- end -}}

{{- $mode := .Values.mode -}}
{{- $source := "" -}}
{{- if eq .Values.mode "recovery" }}
{{- $mode = printf "%s (%s)" .Values.mode .Values.recovery.method -}}
  {{- if eq .Values.recovery.method "pg_basebackup" }}
    {{- $source = printf "postgresql://%s@%s:%.0f/%s" .Values.recovery.pgBaseBackup.source.username .Values.recovery.pgBaseBackup.source.host .Values.recovery.pgBaseBackup.source.port .Values.recovery.pgBaseBackup.source.database -}}
  {{- end -}}
{{- end -}}

{{- $image := (include "cluster.image" .) | fromYaml -}}
{{- if $image.imageCatalogRef -}}
  {{- $image = printf "%s: %s(%s)" $image.imageCatalogRef.kind $image.imageCatalogRef.name (include "cluster.postgresqlMajor" .) -}}
{{- else if $image.imageName -}}
  {{- $image = $image.imageName -}}
{{- end }}

╭───────────────────┬──────────────────────────────────────────────────────────╮
│ Configuration     │ Value                                                    │
┝━━━━━━━━━━━━━━━━━━━┿━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┥
│ Cluster mode      │ {{ printf "%-56s" $mode }} │
│ Type              │ {{ printf "%-56s" .Values.type }} │
│ Image             │ {{ include "cluster.color-info" (printf "%-56s" $image) }} │
{{- if eq .Values.mode "recovery" }}
│ Source            │ {{ printf "%-56s" $source }} │
{{- end }}
│ Instances         │ {{ include (printf "%s%s" "cluster.color-" $redundancyColor) (printf "%-56s" (toString .Values.cluster.instances)) }} │
│ Backups           │ {{ include (printf "%s%s" "cluster.color-" (ternary "ok" "error" .Values.backups.enabled)) (printf "%-56s" (ternary "Enabled" "Disabled" .Values.backups.enabled)) }} │
{{- if .Values.backups.enabled }}
│ Backup Provider   │ {{ printf "%-56s" (title .Values.backups.provider) }} │
│ Scheduled Backups │ {{ printf "%-56s" $scheduledBackups }} │
{{- end }}
│ Storage           │ {{ printf "%-56s" .Values.cluster.storage.size }} │
│ Storage
```

## File: .github\dependabot.yml
```
version: 2

updates:
  - package-ecosystem: "github-actions"
    directory: "/"
    schedule:
      interval: "monthly"
    ignore:
      - dependency-name: "*"
        update-types: ["version-update:semver-patch"]
    groups:
      github-actions-dependencies:
        patterns:
          - "*"

```

## File: .github\FUNDING.yml
```
# These are supported funding model platforms

github: [paradedb] # Replace with up to 4 GitHub Sponsors-enabled usernames e.g., [user1, user2]
patreon: # Replace with a single Patreon username
open_collective: # Replace with a single Open Collective username
ko_fi: # Replace with a single Ko-fi username
tidelift: # Replace with a single Tidelift platform-name/package-name e.g., npm/babel
community_bridge: # Replace with a single Community Bridge project-name e.g., cloud-foundry
liberapay: # Replace with a single Liberapay username
issuehunt: # Replace with a single IssueHunt username
otechie: # Replace with a single Otechie username
custom: # Replace with up to 4 custom sponsorship URLs e.g., ['link1', 'link2']

```

## File: .github\minio.yaml
```
tenant:
  pools:
    - servers: 1
      name: pool0
      volumesPerServer: 1
      size: 1Gi
  buckets:
    - name: mybucket
      region: local

```

## File: .github\pull_request_template.md
```
# Ticket(s) Closed

- Closes #

## What

## Why

## How

## Tests

```

## File: .github\actions\deploy-cert-manager\action.yml
```
name: Deploys cert-manager
description: Deploys the cert-manager operator using Helm.
inputs:
  namespace:
    description: 'The name of the namespace where cert-manager will be installed.'
    required: false
    default: 'cert-manager'
runs:
  using: composite
  steps:
    - name: Deploy the operator
      shell: bash
      env:
        NAMESPACE: ${{ inputs.namespace }}
      run: |
        helm repo add jetstack https://charts.jetstack.io

        helm install \
          cert-manager jetstack/cert-manager \
          --namespace $NAMESPACE \
          --create-namespace \
          --version v1.18.2 \
          --set crds.enabled=true

```

## File: .github\actions\deploy-cluster\action.yml
```
name: Deploy a CNPG Cluster
description: Deploys a CNPG Cluster
inputs:
  namespace:
    description: 'The name of the namespace where the Cluster will be deployed'
    required: false
    default: 'default'
runs:
  using: composite
  steps:
    - name: Deploy a cluster
      shell: bash
      env:
        NAMESPACE: ${{ inputs.namespace }}
      run: |
        cat <<EOF | kubectl apply --server-side --validate=strict -f -
        # Example of PostgreSQL cluster
        apiVersion: postgresql.cnpg.io/v1
        kind: Cluster
        metadata:
          name: cluster-example
          namespace: $NAMESPACE
        spec:
          instances: 3
          storage:
            size: 1Gi
        EOF

```

## File: .github\actions\deploy-operator\action.yml
```
name: Deploy the CNPG Operator
description: Deploys the CNPG Operator to a Kubernetes cluster
inputs:
  namespace:
    description: 'The name of the namespace where the operator will be deployed'
    required: false
    default: 'cnpg-system'
  cluster-wide:
    description: 'If the operator should be deployed cluster-wide or in single-namespace mode'
    required: false
    default: 'true'
runs:
  using: composite
  steps:
    - name: Deploy the operator
      shell: bash
      env:
        NAMESPACE: ${{ inputs.namespace }}
        CLUSTER_WIDE: ${{ inputs.cluster-wide }}
      run: |
        helm repo add cnpg https://cloudnative-pg.github.io/charts
        helm upgrade \
          --install \
          --namespace $NAMESPACE \
          --create-namespace \
          --set config.clusterWide=$CLUSTER_WIDE \
          --wait \
          cnpg cnpg/cloudnative-pg

```

## File: .github\actions\setup-kind\action.yml
```
name: Setup Kind
description: Sets up a kind cluster and installs Helm and kubectl
outputs:
  helm-path:
    description: The path to the Helm binary
    value: ${{ steps.helm.outputs.helm-path }}
  kubectl-path:
    description: The path to the kubectl binary
    value: ${{ steps.kubectl.outputs.kubectl-path }}
runs:
  using: composite
  steps:
    - id: helm
      name: Set up Helm
      uses: azure/setup-helm@1a275c3b69536ee54be43f2070a358922e12c8d4 # v4.3.1
      with:
        version: v3.16.2

    - id: kubectl
      name: Install kubectl
      uses: azure/setup-kubectl@901a10e89ea615cf61f57ac05cecdf23e7de06d8 # v3.2

    - name: Create kind cluster
      uses: helm/kind-action@92086f6be054225fa813e0a4b13787fc9088faab # v1.13.0

```

## File: .github\actions\verify-cluster-ready\action.yaml
```
name: Verifies that a CNPG cluster has a certain amount of ready instances
description: Verifies that a CNPG cluster has a certain amount of ready instances
inputs:
  cluster-name:
    description: The name of the cluster to verify
    required: true
    default: database-cluster
  namespace:
    description: 'The name of the namespace where the Cluster is deployed'
    required: false
    default: 'default'
  ready-instances:
    description: The amount of ready instances to wait for
    required: true
    default: "3"

runs:
  using: composite
  steps:
    - name: Wait for the cluster to become ready
      shell: bash
      env:
        CLUSTER_NAME: ${{ inputs.cluster-name }}
        NAMESPACE: ${{ inputs.namespace }}
        EXPECTED_READY_INSTANCES: ${{ inputs.ready-instances }}
      run: |
        ITER=0
        while true; do
          if [[ $ITER -ge 300 ]]; then
            echo "Cluster not ready"
            exit 1
          fi
          READY_INSTANCES=$(kubectl get clusters.postgresql.cnpg.io $CLUSTER_NAME -n $NAMESPACE -o jsonpath='{.status.readyInstances}')
          if [[ "$READY_INSTANCES" == "$EXPECTED_READY_INSTANCES" ]]; then
            echo "Cluster up and running"
            break
          fi
          sleep 1
          (( ++ITER ))
        done

```

## File: .github\config\cr.yaml
```
## Reference: https://github.com/helm/chart-releaser
index-path: "./index.yaml"

# PGP signing
sign: true
key: ParadeDB
# keyring:          # Set via env variable CR_KEYRING
# passphrase-file:  # Set via env variable CR_PASSPHRASE_FILE

# Enable automatic generation of release notes using GitHub's release notes generator.
# see: https://docs.github.com/en/repositories/releasing-projects-on-github/automatically-generated-release-notes
generate-release-notes: true

```

## File: .github\ISSUE_TEMPLATE\bug_report.md
```
---
name: Bug report
about: Create a report to help us improve
title: ""
labels: ""
assignees: ""
---

**Bug Description**
Please describe the bug.

**How To Reproduce**
Please describe how to reproduce the bug.

**Proposed Fix**
Please describe how you think this bug could be fixed.

```

## File: .github\ISSUE_TEMPLATE\config.yml
```
blank_issues_enabled: false

```

## File: .github\ISSUE_TEMPLATE\feature_request.md
```
---
name: Feature request
about: Suggest an idea for this project
title: ""
labels: ""
assignees: ""
---

**What**
Please describe the feature.

**Why**
Please describe why this feature is important.

**How**
Please describe how you'd implement this feature.

```

## File: .github\workflows\check-typo.yml
```
# workflows/check-typo.yml
#
# Check Typo
# Check Typo using codespell.

name: Check Typo

on:
  pull_request:
    types: [opened, synchronize, reopened, ready_for_review]
  workflow_dispatch:

concurrency:
  group: check-typo-${{ github.head_ref || github.ref }}
  cancel-in-progress: true

jobs:
  check-typo:
    name: Check Typo using codespell
    runs-on: ubuntu-latest
    if: github.event.pull_request.draft == false

    steps:
      - name: Checkout Git Repository
        uses: actions/checkout@v4

      - name: Check Typo using codespell
        uses: codespell-project/actions-codespell@v2
        with:
          check_filenames: true

```

## File: .github\workflows\paradedb-publish-chart.yml
```
# workflows/paradedb-publish-chart.yml
#
# ParadeDB Publish Chart
# Publish the ParadeDB Helm chart to paradedb.github.io via GitHub Pages. This workflow also
# triggers the creation of a GitHub Release. It only runs on pushes to `main` or when we trigger
# a workflow_dispatch event, either manually or via creating a release in `paradedb/paradedb`.

name: ParadeDB Publish Chart

on:
  push:
    branches:
      - main
  workflow_dispatch:
    inputs:
      appVersion:
        description: "The ParadeDB version to publish in the Helm Chart (e.g. 0.1.0)"
        required: true
        default: ""

concurrency:
  group: paradedb-publish-chart-${{ github.head_ref || github.ref }}
  cancel-in-progress: true

jobs:
  paradedb-publish-chart:
    name: Publish ParadeDB Helm Charts to GitHub Pages
    runs-on: ubuntu-latest
    permissions:
      contents: write

    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Configure Git
        run: |
          git config user.name "$GITHUB_ACTOR"
          git config user.email "$GITHUB_ACTOR@users.noreply.github.com"

      - name: Set Helm Chart Release Versions
        id: set_versions
        working-directory: charts/paradedb/
        env:
          GH_TOKEN: ${{ secrets.PARADEDB_BOT_GITHUB_TOKEN }}
        run: |
          # If no appVersion is provided, we use the latest ParadeDB version
          if [ -z "${{ github.event.inputs.appVersion }}" ]; then
            LATEST_TAG=$(gh api repos/paradedb/paradedb/tags --jq '.[0].name')
            APP_VERSION=${LATEST_TAG#v}
          else
            APP_VERSION=${{ github.event.inputs.appVersion }}
          fi
          # Update appVersion to the GitHub Release version and version to the Helm Chart version
          sed -i "s/^[[:space:]]*paradedb: .*/  paradedb: \"$APP_VERSION\"/" values.yaml
          sed -i "s/^appVersion: .*/appVersion: \"$APP_VERSION\"/" Chart.yaml
          sed -i "s/^version: .*/version: ${{ vars.CHART_VERSION_MAJOR }}.${{ vars.CHART_VERSION_MINOR }}.${{ vars.CHART_VERSION_PATCH }}/" Chart.yaml
          echo "values.yaml:"
          cat values.yaml
          echo "----------------------------------------"
          echo "Chart.yaml:"
          cat Chart.yaml

          # Set output to update post-release, increasing the Helm Chart version patch number by one to update in GitHub Actions Variables
          echo "new_chart_version_patch=$(( ${{ vars.CHART_VERSION_PATCH }} + 1 ))" >> $GITHUB_OUTPUT

      # The GitHub repository secret `PARADEDB_PGP_PRIVATE_KEY` contains the private key
      # in ASCII-armored format. To export a (new) key, run this command:
      # `gpg --armor --export-secret-key <my key>`
      - name: Prepare ParadeDB PGP Key
        env:
          PGP_PRIVATE_KEY: "${{ secrets.PARADEDB_PGP_PRIVATE_KEY }}"
          PGP_PASSPHRASE: "${{ secrets.PARADEDB_PGP_PASSPHRASE }}"
        run: |
          IFS=""
          echo "$PGP_PRIVATE_KEY" | gpg --dearmor --verbose > /tmp/secring.gpg
          echo "$PGP_PASSPHRASE" > /tmp/passphrase.txt

          # Tell chart-releaser-action where to find the key and its passphrase
          echo "CR_KEYRING=/tmp/secring.gpg" >> "$GITHUB_ENV"
          echo "CR_PASSPHRASE_FILE=/tmp/passphrase.txt" >> "$GITHUB_ENV"

      - name: Add Grafana Chart Dependencies
        run: helm repo add cnpg-grafana-dashboard https://cloudnative-pg.github.io/grafana-dashboards

      - name: Run chart-releaser
        uses: helm/chart-releaser-action@v1.6.0
        with:
          config: "./.github/config/cr.yaml"
        env:
          CR_TOKEN: "${{ secrets.PARADEDB_BOT_GITHUB_TOKEN }}"

      # We have a separate version for our Helm Chart, since it needs to always increment by
      # one for every production release, independently of the ParadeDB version. Any non-patch
      # version increment should be done manually in GitHub Actions Variables.
      - name: Increment Helm Chart Version Number in GitHub Actions Variables
        env:
          GH_TOKEN: ${{ secrets.PARADEDB_BOT_GITHUB_TOKEN }}
        run: |
          gh api \
            --method PATCH \
            -H "Accept: application/vnd.github+json" \
            -H "X-GitHub-Api-Version: 2022-11-28" \
            /repos/paradedb/charts/actions/variables/CHART_VERSION_PATCH \
            -f name='CHART_VERSION_PATCH' \
            -f value='${{ steps.set_versions.outputs.new_chart_version_patch }}'

      - name: Securely Delete the PGP Key and Passphrase
        if: always()
        run: shred --remove=wipesync /tmp/secring.gpg /tmp/passphrase.txt

```

## File: .github\workflows\paradedb-test-chainsaw.yaml
```
name: Test ParadeDB Helm Chart

on:
  pull_request:
    branches-ignore:
      - "gh-pages"

permissions: read-all

jobs:
  test-list:
    runs-on: ubuntu-latest
    outputs:
      tests: ${{ steps.listTests.outputs.tests }}
    steps:
      - name: Checkout
        uses: actions/checkout@v4
        with:
          fetch-depth: 1
      - id: listTests
        run: |
          echo "tests=$(ls charts/paradedb/test -1 | jq -cRn '{ include: [inputs | { test: "\(.)" }]}')" >> $GITHUB_OUTPUT

  test:
    needs: test-list
    runs-on: ubuntu-latest
    strategy:
      fail-fast: false
      matrix: ${{ fromJson(needs.test-list.outputs.tests) }}
    name: ${{ matrix.test }}
    steps:
      - name: Checkout
        uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Install Cosign
        uses: sigstore/cosign-installer@v3

      # Added by ParadeDB: Authenticate to Docker Hub to avoid rate limits
      - name: Login to Docker Hub
        uses: docker/login-action@v3
        with:
          username: ${{ vars.DOCKERHUB_USERNAME }}
          password: ${{ secrets.DOCKERHUB_ACCESS_TOKEN }}

      # Added by ParadeDB: Always pull the latest version of paradedb/paradedb
      - name: Set ParadeDB Version to Latest
        working-directory: charts/paradedb/
        env:
          GH_TOKEN: ${{ secrets.PARADEDB_BOT_GITHUB_TOKEN }}
        run: |
          LATEST_TAG=$(gh api repos/paradedb/paradedb/tags --jq '.[0].name')
          APP_VERSION=${LATEST_TAG#v}
          sed -i "s/^[[:space:]]*paradedb: .*/  paradedb: \"$APP_VERSION\"/" values.yaml
          sed -i "s/^version: .*/version: ${{ vars.CHART_VERSION_MAJOR }}.${{ vars.CHART_VERSION_MINOR }}.${{ vars.CHART_VERSION_PATCH }}/" Chart.yaml
          echo "values.yaml:"
          cat values.yaml
          echo "----------------------------------------"
          echo "Chart.yaml:"
          cat Chart.yaml

      - name: Setup kind
        uses: ./.github/actions/setup-kind

      - name: Deploy the operator
        uses: ./.github/actions/deploy-operator

      - name: Install Prometheus CRDs
        run: |
          helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
          helm install prometheus-crds prometheus-community/prometheus-operator-crds

      - name: Install Chainsaw
        uses: kyverno/action-install-chainsaw@v0.2.12
        with:
          verify: true

      - name: Setup MinIO
        run: |
          helm repo add minio-operator https://operator.min.io
          helm upgrade \
            --install \
            --namespace minio-system \
            --create-namespace \
            --wait \
            operator minio-operator/operator
          helm upgrade \
            --install \
            --namespace minio \
            --create-namespace \
            --wait \
            --values ./.github/minio.yaml \
            tenant minio-operator/tenant

      # The Docker Hub tokens are required for the ParadeDB Enterprise tests
      - name: Run Kyverno/Chainsaw
        run: chainsaw test charts/paradedb/test/${{ matrix.test }}
        env:
          PARADEDB_ENTERPRISE_DOCKER_USERNAME: ${{ vars.DOCKERHUB_USERNAME }}
          PARADEDB_ENTERPRISE_DOCKER_PAT: ${{ secrets.DOCKERHUB_ACCESS_TOKEN }}

```

## File: .github\workflows\release-pr.yml
```
##
# Create a PR for a release when a commit is pushed on a release/*-v* branch to support the releases of both the
# operator and cluster charts
name: release-pr

on:
  push:
    branches:
      - release/*-v*

permissions: read-all

jobs:
  create-pull-request:
    runs-on: ubuntu-24.04
    permissions:
      pull-requests: write
    steps:
      - name: Checkout
        uses: actions/checkout@8e8c483db84b4bee98b60c0593521ed34d9990e8 # v6.0.1
      - name: Create Pull Request
        id: create-pr
        env:
          GH_TOKEN: ${{ secrets.REPO_GHA_PAT }}
          ACTOR: ${{ github.actor }}
        run: |
          TAG="${GITHUB_REF##*/}"
          TITLE="Release ${TAG}"
          BODY="Automated PR. Will trigger the ${TAG} release when approved."
          LABEL=release
          ASSIGNEE="${ACTOR}"
          gh pr create --title "${TITLE}" --body "${BODY}" --label "${LABEL}" --assignee "${ASSIGNEE}" ||
          gh pr edit --title "${TITLE}" --body "${BODY}" --add-label "${LABEL}"

```

## File: .github\workflows\tests-cluster-chainsaw.yaml
```
name: test( cluster )

on:
  pull_request:
    branches-ignore:
      - 'gh-pages'

permissions: read-all

jobs:
  test-list:
    runs-on: ubuntu-24.04
    outputs:
      tests: ${{ steps.listTests.outputs.tests }}
    steps:
      - name: Checkout
        uses: actions/checkout@8e8c483db84b4bee98b60c0593521ed34d9990e8 # v6.0.1
        with:
          fetch-depth: 1
      - id: listTests
        run: |
          echo "tests=$(ls charts/cluster/test -1 | jq -cRn '{ include: [inputs | { test: "\(.)" }]}')" >> $GITHUB_OUTPUT
  test:
    needs: test-list
    runs-on: ubuntu-24.04
    strategy:
      fail-fast: false
      matrix: ${{ fromJson(needs.test-list.outputs.tests) }}
    name: ${{matrix.test}}
    steps:
      - name: Checkout
        uses: actions/checkout@8e8c483db84b4bee98b60c0593521ed34d9990e8 # v6.0.1
        with:
          fetch-depth: 0

      - name: Install Cosign
        uses: sigstore/cosign-installer@faadad0cce49287aee09b3a48701e75088a2c6ad # v4.0.0

      - name: Setup kind
        uses: ./.github/actions/setup-kind

      - name: Deploy the operator
        uses: ./.github/actions/deploy-operator

      - name: Install Prometheus CRDs
        run: |
          helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
          helm install prometheus-crds prometheus-community/prometheus-operator-crds

      - name: Install Chainsaw
        uses: kyverno/action-install-chainsaw@06560d18422209e9c1e08e931d477d04bf2674c1 # v0.2.14
        with:
          verify: true

      - name: Setup MinIO
        run: |
          helm repo add minio-operator https://operator.min.io
          helm upgrade \
            --install \
            --namespace minio-system \
            --create-namespace \
            --wait \
            operator minio-operator/operator
          helm upgrade \
            --install \
            --namespace minio \
            --create-namespace \
            --wait \
            --values ./.github/minio.yaml \
            tenant minio-operator/tenant

      - name: Run Kyverno/Chainsaw
        env:
          MATRIX_TEST: ${{ matrix.test }}
        run: chainsaw test "charts/cluster/test/${MATRIX_TEST}"

```

## File: .github\workflows\tests-plugin-barman-cloud.yaml
```
name: test( cluster )

on:
  pull_request:
    branches-ignore:
      - 'gh-pages'

permissions: read-all

jobs:
  test-list:
    runs-on: ubuntu-24.04
    outputs:
      tests: ${{ steps.listTests.outputs.tests }}
    steps:
      - name: Checkout
        uses: actions/checkout@8e8c483db84b4bee98b60c0593521ed34d9990e8 # v6.0.1
        with:
          fetch-depth: 1
      - id: listTests
        run: |
          echo "tests=$(ls charts/plugin-barman-cloud/test -1 | jq -cRn '{ include: [inputs | { test: "\(.)" }]}')" >> $GITHUB_OUTPUT
  test:
    needs: test-list
    runs-on: ubuntu-24.04
    strategy:
      fail-fast: false
      matrix: ${{ fromJson(needs.test-list.outputs.tests) }}
    env:
      MATRIX_TEST: ${{ matrix.test }}
    name: ${{ env.MATRIX_TEST }}
    steps:
      - name: Checkout
        uses: actions/checkout@8e8c483db84b4bee98b60c0593521ed34d9990e8 # v6.0.1
        with:
          fetch-depth: 0

      - name: Install Cosign
        uses: sigstore/cosign-installer@faadad0cce49287aee09b3a48701e75088a2c6ad # v4.0.0

      - name: Setup kind
        uses: ./.github/actions/setup-kind

      - name: Deploy the operator
        uses: ./.github/actions/deploy-operator

      - name: Install cert-manager
        uses: ./.github/actions/deploy-cert-manager

      - name: Install Prometheus CRDs
        run: |
          helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
          helm install prometheus-crds prometheus-community/prometheus-operator-crds

      - name: Install Chainsaw
        uses: kyverno/action-install-chainsaw@06560d18422209e9c1e08e931d477d04bf2674c1 # v0.2.14
        with:
          verify: true

      - name: Setup MinIO
        run: |
          helm repo add minio-operator https://operator.min.io
          helm upgrade \
            --install \
            --namespace minio-system \
            --create-namespace \
            --wait \
            operator minio-operator/operator
          helm upgrade \
            --install \
            --namespace minio \
            --create-namespace \
            --wait \
            --values ./.github/minio.yaml \
            tenant minio-operator/tenant

      - name: Run Kyverno/Chainsaw
        run: chainsaw test "charts/plugin-barman-cloud/test/${MATRIX_TEST}"

```

## File: charts\paradedb\Chart.yaml
```
#
# Copyright © contributors to CloudNativePG, established as
# CloudNativePG a Series of LF Projects, LLC.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# SPDX-License-Identifier: Apache-2.0
#
apiVersion: v2
name: paradedb
description: Deploys and manages a ParadeDB CloudNativePG cluster and its associated resources.
icon: https://raw.githubusercontent.com/paradedb/paradedb/main/docs/logo/light.svg
type: application

# The Chart version, set in the publish CI workflow from GitHub Actions Variables
version: 0.0.0-generated-in-ci

# The ParadeDB version, set in the publish CI workflow from the latest paradedb/paradedb GitHub tag
# We default to v0.22.3 for testing and local development
appVersion: 0.22.3

sources:
  - https://github.com/paradedb/charts
keywords:
  - paradedb
  - pg_search
  - postgresql
  - postgres
  - database
  - full-text
  - analytics
  - vector
  - zero-etl
home: https://paradedb.com
maintainers:
  - name: ParadeDB
    email: support@paradedb.com
    url: https://paradedb.com

```

## File: charts\paradedb\README.md
```
# ParadeDB Helm Chart

The [ParadeDB](https://github.com/paradedb/paradedb) Helm Chart is based on the official [CloudNativePG Helm Chart](https://cloudnative-pg.io/). CloudNativePG is a Kubernetes operator that manages the full lifecycle of a highly available PostgreSQL database cluster with a primary/standby architecture using Postgres streaming (physical) replication.

Kubernetes, and specifically the CloudNativePG operator, is the recommended approach for deploying ParadeDB in production, with high availability. ParadeDB also provides a [Docker image](https://hub.docker.com/r/paradedb/paradedb) and [prebuilt binaries](https://github.com/paradedb/paradedb/releases) for Debian, Ubuntu, Red Hat Enterprise Linux, and macOS.

The ParadeDB Helm Chart supports Postgres 15+ and ships with Postgres 18 by default.

The chart is also available on [Artifact Hub](https://artifacthub.io/packages/helm/paradedb/paradedb).

## Usage

First, install [Helm](https://helm.sh/docs/intro/install/). The following steps assume you have a Kubernetes cluster running v1.29+. If you are testing locally, we recommend using [Minikube](https://minikube.sigs.k8s.io/docs/start/).

#### Monitoring

The ParadeDB Helm chart supports monitoring via Prometheus and Grafana. To enable monitoring, you need to have the Prometheus CRDs installed before installing the CloudNativePG operator. The Prometheus CRDs can be found [here](https://prometheus-community.github.io/helm-charts).

#### Installing the CloudNativePG Operator

Skip this step if the CloudNativePG operator is already installed in your cluster. For advanced CloudNativePG configuration and monitoring, please refer to the [CloudNativePG Cluster Chart documentation](https://github.com/paradedb/charts/blob/main/charts/cloudnative-pg/README.md#values).

```bash
helm repo add cnpg https://cloudnative-pg.github.io/charts
helm upgrade --atomic --install cnpg \
--create-namespace \
--namespace cnpg-system \
cnpg/cloudnative-pg
```

#### Setting up a ParadeDB CNPG Cluster

> [!IMPORTANT]
> When deploying a cluster with more than one instance, you must use `type: paradedb-enterprise` to enable replication of BM25 indexes across instances.
> Using ParadeDB Enterprise requires an access token. To request one, please [contact sales](mailto:sales@paradedb.com).

Create a `values.yaml` and configure it to your requirements. Here is a basic example:

```yaml
type: paradedb
mode: standalone

version:
  # -- PostgreSQL major version to use
  postgresql: "18"
  # -- ParadeDB version to use
  paradedb: "0.22.3"

cluster:
  instances: 1
  storage:
    size: 256Mi
```

Then, launch the ParadeDB cluster.

```bash
helm repo add paradedb https://paradedb.github.io/charts
helm upgrade --atomic --install paradedb \
--namespace paradedb \
--create-namespace \
--values values.yaml \
paradedb/paradedb
```

If `--values values.yaml` is omitted, the default values will be used. For advanced ParadeDB configuration and monitoring, please refer to the [ParadeDB Chart documentation](https://github.com/paradedb/charts/tree/dev/charts/paradedb#values).

#### Connecting to a ParadeDB CNPG Cluster

You can launch a Bash shell inside a specific pod via:

```bash
kubectl exec --stdin --tty <pod-name> -n paradedb -- bash
```

The primary is called `paradedb-1`. The replicas are called `paradedb-2` onwards depending on the number of replicas you configured. You can connect to the ParadeDB database with `psql` via:

```bash
psql -d paradedb
```

## Development

To test changes to the Chart on a local Minikube cluster, follow the instructions from [Self Hosted](#self-hosted) replacing the `helm upgrade` step by the path to the directory of the modified `Chart.yaml`.

```bash
helm upgrade --atomic --install paradedb --namespace paradedb --create-namespace ./charts/paradedb
```

## Advanced Cluster Configuration

### Database Types

To create a ParadeDB cluster, you must specify either `paradedb` or `paradedb-enterprise` via the `type` parameter.

> [!IMPORTANT]
> When using `paradedb-enterprise` you must also specify the `cluster.imagePullSecrets` containing the Docker registry credentials. You can create one with:
>
> ```bash
> kubectl -n NAMESPACE create secret docker-registry paradedb-enterprise-registry-cred --docker-server="https://index.docker.io/v1/" --docker-username="USERNAME" --docker-password="ACCESS_TOKEN"
> ```
>
> You then need to set the name of the secret in the `values.yaml` file with:
>
> ```yaml
> type: paradedb-enterprise
> cluster:
>   imagePullSecrets:
>    - name: paradedb-enterprise-registry-cred
> ```

### Modes of Operation

The chart has three modes of operation. These are configured via the `mode` parameter:

* `standalone` - Creates new or updates an existing CNPG cluster. This is the default mode.
* `replica` - Creates a replica cluster from an existing CNPG cluster.
* `recovery` - Recovers a CNPG cluster from a backup, object store or via pg_basebackup.

### Backup Configuration

CNPG implements disaster recovery via [Barman](https://pgbarman.org/). The following section configures the barman object
store where backups will be stored. Barman performs backups of the cluster filesystem base backup and WALs. Both are
stored in the specified location. The backup provider is configured via the `backups.provider` parameter. The following
providers are supported:

* S3 or S3-compatible stores, like MinIO
* Microsoft Azure Blob Storage
* Google Cloud Storage

Additionally you can specify the following parameters:

* `backups.retentionPolicy` - The retention policy for backups. Defaults to `30d`.
* `backups.scheduledBackups` - An array of scheduled backups containing a name and a crontab schedule. Example:

```yaml
backups:
  scheduledBackups:
    - name: daily-backup
      schedule: "0 0 0 * * *" # Daily at midnight
      backupOwnerReference: self
```

Each backup adapter takes its own set of parameters, listed in the [Configuration options](#Configuration-options) section.
Refer to the table for the full list of parameters and place the configuration under the appropriate key: `backups.s3`,
`backups.azure`, or `backups.google`.

## Recovery

There is a separate document outlining the recovery procedure here: **[Recovery](docs/recovery.md)**

## Monitoring

The ParadeDB Helm chart supports monitoring with Prometheus and Grafana. The chart includes a comprehensive Grafana dashboard that provides complete monitoring for both PostgreSQL/cluster operations and ParadeDB-specific search and analytics features. The dashboard is provisioned as a ConfigMap that works with the Grafana sidecar to automatically import dashboards. You can enable this by setting `monitoring.grafanaDashboard.create`.

**Note:** This is a complete, all-in-one dashboard that includes both standard CloudNativePG monitoring (replication, backups, storage, WAL, connections) and ParadeDB-specific metrics (pg_search, BM25 search, index segments). You do not need to install any additional dashboards.

### Dashboard Features

The comprehensive dashboard includes monitoring for:

**PostgreSQL & Cluster Management:**
- Physical Replication (lag, write/flush/replay lag)
- Backups & WAL archiving status
- Storage usage and disk I/O
- Server health (CPU, memory, TPS)
- Connection states and transactions
- Logical replication metrics

**ParadeDB Search & Analytics:**
- BM25 index segments and sizes
- `pg_search` performance metrics
- Search-specific analytics
- Index layer monitoring

Alternatively, you can manually import the dashboard from the `monitoring` directory.

### Metrics Configuration

Additionally, we recommend enabling the `kube-state-metrics` CRD monitoring and adding the CNPG metrics. The configuration can be found in `monitoring/metrics-clusters_postgresql_cnpg_io.yaml`.

## Examples

There are several configuration examples in the [examples](examples) directory. Refer to them for a basic setup and
refer to the [CloudNativePG Documentation](https://cloudnative-pg.io/documentation/current/) for more advanced configurations.

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| backups.azure.connectionString | string | `""` |  |
| backups.azure.containerName | string | `""` |  |
| backups.azure.inheritFromAzureAD | bool | `false` |  |
| backups.azure.path | string | `"/"` |  |
| backups.azure.serviceName | string | `"blob"` |  |
| backups.azure.storageAccount | string | `""` |  |
| backups.azure.storageKey | string | `""` |  |
| backups.azure.storageSasToken | string | `""` |  |
| backups.data.compression | string | `"gzip"` | Data compression method. One of `` (for no compression), `gzip`, `bzip2` or `snappy`. |
| backups.data.encryption | string | `"AES256"` | Whether to instruct the storage provider to encrypt data files. One of `` (use the storage container default), `AES256` or `aws:kms`. |
| backups.data.jobs | int | `2` | Number of data files to be archived or restored in parallel. |
| backups.destinationPath | string | `""` | Overrides the provider specific default path. Defaults to: S3: s3://<bucket><path> Azure: https://<storageAccount>.<serviceName>.core.windows.net/<containerName><path> Google: gs://<bucket><path> |
| backups.enabled | bool | `false` | You need to configure backups manually, so backups are disabled by default. |
| backups.endpointCA | object | `{"create":false,"key":"","name":"","value":""}` | Specifies a CA bundle to validate a privately signed certificate. |
| backups.endpointCA.create | bool | `false` | Creates a secret with the given value if true, otherwise uses an existing secret. |
| backups.endpointURL | string | `""` | Overrides the provider specific default endpoint. Defaults to: S3: https://s3.<region>.amazonaws.com |
| backups.google.applicationCredentials | string | `""` |  |
| backups.google.bucket | string | `""` |  |
| backups.google.gkeEnvironment | bool | `false` |  |
| backups.google.path | string | `"/"` |  |
| backups.provider | string | `"s3"` | One of `s3`, `azure` or `google` |
| backups.retentionPolicy | string | `"30d"` | Retention policy for backups |
| backups.s3.accessKey | string | `""` |  |
| backups.s3.bucket | string | `""` |  |
| backups.s3.inheritFromIAMRole | bool | `false` | Use the role based authentication without providing explicitly the keys |
| backups.s3.path | string | `"/"` |  |
| backups.s3.region | string | `""` |  |
| backups.s3.secretKey | string | `""` |  |
| backups.scheduledBackups[0].backupOwnerReference | string | `"self"` | Backup owner reference |
| backups.scheduledBackups[0].method | string | `"barmanObjectStore"` | Backup method, can be `barmanObjectStore` (default) or `volumeSnapshot` |
| backups.scheduledBackups[0].name | string | `"daily-backup"` | Scheduled backup name |
| backups.scheduledBackups[0].schedule | string | `"0 0 0 * * *"` | Schedule in cron format |
| backups.secret.create | bool | `true` | Whether to create a secret for the backup credentials |
| backups.secret.name | string | `""` | Name of the backup credentials secret |
| backups.wal.compression | string | `"gzip"` | WAL compression method. One of `` (for no compression), `gzip`, `bzip2` or `snappy`. |
| backups.wal.encryption | string | `"AES256"` | Whether to instruct the storage provider to encrypt WAL files. One of `` (use the storage container default), `AES256` or `aws:kms`. |
| backups.wal.maxParallel | int | `1` | Number of WAL files to be archived or restored in parallel. |
| cluster.additionalLabels | object | `{}` |  |
| cluster.affinity | object | `{"topologyKey":"topology.kubernetes.io/zone"}` | Affinity/Anti-affinity rules for Pods. See: https://cloudnative-pg.io/documentation/current/cloudnative-pg.v1/#postgresql-cnpg-io-v1-AffinityConfiguration |
| cluster.annotations | object | `{}` |  |
| cluster.certificates | object | `{}` | The configuration for the CA and related certificates. See: https://cloudnative-pg.io/documentation/current/cloudnative-pg.v1/#postgresql-cnpg-io-v1-CertificatesConfiguration |
| cluster.console.enabled | bool | `false` | Deploys a console StatefulSet to run long-running commands against the cluster (e.g. `CREATE INDEX`). |
| cluster.enablePDB | bool | `true` | Allows disabling PDB, mainly useful for upgrade of single-instance clusters or development purposes See: https://cloudnative-pg.io/documentation/current/kubernetes_upgrade/#pod-disruption-budgets |
| cluster.enableSuperuserAccess | bool | `true` | When this option is enabled, the operator will use the SuperuserSecret to update the postgres user password. If the secret is not present, the operator will automatically create one. When this option is disabled, the operator will ignore the SuperuserSecret content, delete it when automatically created, and then blank the password of the postgres user by setting it to NULL. |
| cluster.env | list | `[]` | Env follows the Env format to pass environment variables to the pods created in the cluster |
| cluster.envFrom | list | `[]` | EnvFrom follows the EnvFrom format to pass environment variables sources to the pods to be used by Env |
| cluster.imageCatalogRef | object | `{}` | Reference to `ImageCatalog` of `ClusterImageCatalog`, if specified takes precedence over `cluster.imageName` |
| cluster.imageName | string | `""` | Name of the container image, supporting both tags (<image>:<tag>) and digests for deterministic and repeatable deployments: <image>:<tag>@sha256:<digestValue> |
| cluster.imagePullPolicy | string | `"IfNotPresent"` | Image pull policy. One of Always, Never or IfNotPresent. If not defined, it defaults to IfNotPresent. Cannot be updated. More info: https://kubernetes.io/docs/concepts/containers/images#updating-images |
| cluster.imagePullSecrets | list | `[]` | The list of pull secrets to be used to pull the images. See: https://cloudnative-pg.io/documentation/current/cloudnative-pg.v1/#postgresql-cnpg-io-v1-LocalObjectReference |
| cluster.initdb | object | `{"database":"paradedb"}` | BootstrapInitDB is the configuration of the bootstrap process when initdb is used. See: https://cloudnative-pg.io/documentation/current/bootstrap/ See: https://cloudnative-pg.io/documentation/current/cloudnative-pg.v1/#postgresql-cnpg-io-v1-bootstrapinitdb |
| cluster.instances | int | `3` | Number of instances |
| cluster.logLevel | string | `"info"` | The instances' log level, one of the following values: error, warning, info (default), debug, trace |
| cluster.monitoring.customQueries | list | `[]` | Custom Prometheus metrics Will be stored in the ConfigMap |
| cluster.monitoring.customQueriesSecret | list | `[]` | The list of secrets containing the custom queries |
| cluster.monitoring.disableDefaultQueries | bool | `false` | Whether the default queries should be injected. Set it to true if you don't want to inject default queries into the cluster. |
| cluster.monitoring.enabled | bool | `false` | Whether to enable monitoring |
| cluster.monitoring.instrumentation.logicalReplication | bool | `true` | Enable logical replication metrics |
| cluster.monitoring.instrumentation.paradedbIndex | bool | `true` | Enable ParadeDB index metrics |
| cluster.monitoring.podMonitor.enabled | bool | `true` | Whether to enable the PodMonitor |
| cluster.monitoring.podMonitor.labels | object | `{}` | Additional labels to set on the generated PodMonitor resource. Add labels your monitoring stack requires (for example `team-name`). |
| cluster.monitoring.podMonitor.metricRelabelings | list | `[]` | The list of metric relabelings for the PodMonitor. Applied to samples before ingestion. |
| cluster.monitoring.podMonitor.relabelings | list | `[]` | The list of relabelings for the PodMonitor. Applied to samples before scraping. |
| cluster.monitoring.prometheusRule.enabled | bool | `true` | Whether to enable the PrometheusRule automated alerts |
| cluster.monitoring.prometheusRule.excludeRules | list | `[]` | Exclude specified rules |
| cluster.podSecurityContext | object | `{}` | Configure the Pod Security Context. See: https://cloudnative-pg.io/documentation/preview/security/ |
| cluster.postgresGID | int | `-1` | The GID of the postgres user inside the image, defaults to 999 for ParadeDB and 26 for PostgreSQL |
| cluster.postgresUID | int | `-1` | The UID of the postgres user inside the image, defaults to 999 for ParadeDB and 26 for PostgreSQL |
| cluster.postgresql.ldap | object | `{}` | PostgreSQL LDAP configuration (see https://cloudnative-pg.io/documentation/current/postgresql_conf/#ldap-configuration) |
| cluster.postgresql.parameters | object | `{}` | PostgreSQL configuration options (postgresql.conf) |
| cluster.postgresql.pg_hba | list | `[]` | PostgreSQL Host Based Authentication rules (lines to be appended to the pg_hba.conf file) |
| cluster.postgresql.pg_ident | list | `[]` | PostgreSQL User Name Maps rules (lines to be appended to the pg_ident.conf file) |
| cluster.postgresql.shared_preload_libraries | list | `[]` | Lists of shared preload libraries to add to the default ones |
| cluster.postgresql.synchronous | object | `{}` | Quorum-based Synchronous Replication |
| cluster.primaryUpdateMethod | string | `"switchover"` | Method to follow to upgrade the primary server during a rolling update procedure, after all replicas have been successfully updated. It can be switchover (default) or restart. |
| cluster.primaryUpdateStrategy | string | `"unsupervised"` | Strategy to follow to upgrade the primary server during a rolling update procedure, after all replicas have been successfully updated: it can be automated (unsupervised - default) or manual (supervised) |
| cluster.priorityClassName | string | `""` |  |
| cluster.resources | object | `{}` | Resources requirements of every generated Pod. Please refer to https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/ for more information. We strongly advise you use the same setting for limits and requests so that your cluster pods are given a Guaranteed QoS. See: https://kubernetes.io/docs/concepts/workloads/pods/pod-qos/ |
| cluster.roles | list | `[]` | This feature enables declarative management of existing roles, as well as the creation of new roles if they are not already present in the database. See: https://cloudnative-pg.io/documentation/current/declarative_role_management/ |
| cluster.securityContext | object | `{}` | Configure Container Security Context. See: https://cloudnative-pg.io/documentation/preview/security/ |
| cluster.serviceAccountTemplate | object | `{}` | Configure the metadata of the generated service account |
| cluster.services | object | `{}` | Customization of service definitions. Please refer to https://cloudnative-pg.io/documentation/current/service_management/ |
| cluster.storage.size | string | `"8Gi"` |  |
| cluster.storage.storageClass | string | `""` |  |
| cluster.superuserSecret | string | `""` |  |
| cluster.walStorage.enabled | bool | `false` |  |
| cluster.walStorage.size | string | `"1Gi"` |  |
| cluster.walStorage.storageClass | string | `""` |  |
| databases | list | `[]` |  |
| fullnameOverride | string | `""` | Override the full name of the chart |
| imageCatalog.create | bool | `true` | Whether to provision an image catalog. If imageCatalog.images is empty this option will be ignored. |
| imageCatalog.images | list | `[]` | List of images to be provisioned in an image catalog. |
| mode | string | `"standalone"` | Cluster mode of operation. Available modes: * `standalone` - default mode. Creates new or updates an existing CNPG cluster. * `replica` - Creates a replica cluster from an existing CNPG cluster. * `recovery` - Same as standalone but creates a cluster from a backup, object store or via pg_basebackup. |
| monitoring.grafanaDashboard.annotations | object | `{}` | Annotations that ConfigMaps can have to get configured in Grafana. |
| monitoring.grafanaDashboard.configMapName | string | `"paradedb-grafana-dashboard"` | The name of the ConfigMap containing the dashboard. |
| monitoring.grafanaDashboard.create | bool | `true` |  |
| monitoring.grafanaDashboard.labels | object | `{"grafana_dashboard":"1"}` | Labels that ConfigMaps should have to get configured in Grafana. |
| monitoring.grafanaDashboard.namespace | string | `"monitoring"` | Allows overriding the namespace where the ConfigMap will be created, defaulting to the same one as the Release. |
| nameOverride | string | `""` | Override the name of the chart |
| namespaceOverride | string | `""` | Override the namespace of the chart |
| poolers | list | `[]` | List of PgBouncer poolers |
| recovery.azure.connectionString | string | `""` |  |
| recovery.azure.containerName | string | `""` |  |
| recovery.azure.inheritFromAzureAD | bool | `false` |  |
| recovery.azure.path | string | `"/"` |  |
| recovery.azure.serviceName | string | `"blob"` |  |
| recovery.azure.storageAccount | string | `""` |  |
| recovery.azure.storageKey | string | `""` |  |
| recovery.azure.storageSasToken | string | `""` |  |
| recovery.backupName | string | `""` | Backup Recovery Method |
| recovery.clusterName | string | `""` | The original cluster name when used in backups. Also known as serverName. |
| recovery.database | string | `"paradedb"` | Name of the database used by the application. Default: `paradedb`. |
| recovery.destinationPath | string | `""` | Overrides the provider specific default path. Defaults to: S3: s3://<bucket><path> Azure: https://<storageAccount>.<serviceName>.core.windows.net/<containerName><path> Google: gs://<bucket><path> |
| recovery.endpointCA | object | `{"create":false,"key":"","name":"","value":""}` | Specifies a CA bundle to validate a privately signed certificate. |
| recovery.endpointCA.create | bool | `false` | Creates a secret with the given value if true, otherwise uses an existing secret. |
| recovery.endpointURL | string | `""` | Overrides the provider specific default endpoint. Defaults to: S3: https://s3.<region>.amazonaws.com |
| recovery.google.applicationCredentials | string | `""` |  |
| recovery.google.bucket | string | `""` |  |
| recovery.google.gkeEnvironment | bool | `false` |  |
| recovery.google.path | string | `"/"` |  |
| recovery.import.databases | list | `[]` | Databases to import |
| recovery.import.pgDumpExtraOptions | list | `[]` | List of custom options to pass to the `pg_dump` command. IMPORTANT: Use these options with caution and at your own risk, as the operator does not validate their content. Be aware that certain options may conflict with the operator's intended functionality or design. |
| recovery.import.pgRestoreExtraOptions | list | `[]` | List of custom options to pass to the `pg_restore` command. IMPORTANT: Use these options with caution and at your own risk, as the operator does not validate their content. Be aware that certain options may conflict with the operator's intended functionality or design. |
| recovery.import.postImportApplicationSQL | list | `[]` | List of SQL queries to be executed as a superuser in the application database right after is imported. To be used with extreme care. Only available in microservice type. |
| recovery.import.roles | list | `[]` | Roles to import |
| recovery.import.schemaOnly | bool | `false` | When set to true, only the pre-data and post-data sections of pg_restore are invoked, avoiding data import. |
| recovery.import.source.database | string | `"paradedb"` |  |
| recovery.import.source.host | string | `""` |  |
| recovery.import.source.passwordSecret.create | bool | `false` | Whether to create a secret for the password |
| recovery.import.source.passwordSecret.key | string | `"password"` | The key in the secret containing the password |
| recovery.import.source.passwordSecret.name | string | `""` | Name of the secret containing the password |
| recovery.import.source.passwordSecret.value | string | `""` | The password value to use when creating the secret |
| recovery.import.source.port | int | `5432` |  |
| recovery.import.source.sslCertSecret.key | string | `""` |  |
| recovery.import.source.sslCertSecret.name | string | `""` |  |
| recovery.import.source.sslKeySecret.key | string | `""` |  |
| recovery.import.source.sslKeySecret.name | string | `""` |  |
| recovery.import.source.sslMode | string | `"verify-full"` |  |
| recovery.import.source.sslRootCertSecret.key | string | `""` |  |
| recovery.import.source.sslRootCertSecret.name | string | `""` |  |
| recovery.import.source.username | string | `""` |  |
| recovery.import.type | string | `"microservice"` | One of `microservice` or `monolith`. See: https://cloudnative-pg.io/documentation/current/database_import/#how-it-works |
| recovery.method | string | `"backup"` | Available recovery methods: * `backup` - Recovers a CNPG cluster from a CNPG backup (PITR supported) Needs to be on the same cluster in the same namespace. * `object_store` - Recovers a CNPG cluster from a barman object store (PITR supported). * `pg_basebackup` - Recovers a CNPG cluster via a streaming replication protocol. Useful if you want to migrate databases to CloudNativePG, even from outside Kubernetes. * `import` - Import one or more databases from an existing Postgres cluster. |
| recovery.owner | string | `""` | Name of the owner of the database in the instance to be used by applications. Defaults to the value of the `database` key. |
| recovery.pgBaseBackup.database | string | `"paradedb"` | Name of the database used by the application. Default: `paradedb`. |
| recovery.pgBaseBackup.owner | string | `""` | Name of the owner of the database in the instance to be used by applications. Defaults to the value of the `database` key. |
| recovery.pgBaseBackup.secretName | string | `""` | Name of the kubernetes.io/basic-auth secret containing the initial credentials for the owner of the user database. If empty a new secret will be created from scratch. |
| recovery.pgBaseBackup.source.database | string | `"paradedb"` |  |
| recovery.pgBaseBackup.source.host | string | `""` |  |
| recovery.pgBaseBackup.source.passwordSecret.create | bool | `false` | Whether to create a secret for the password |
| recovery.pgBaseBackup.source.passwordSecret.key | string | `"password"` | The key in the secret containing the password |
| recovery.pgBaseBackup.source.passwordSecret.name | string | `""` | Name of the secret containing the password |
| recovery.pgBaseBackup.source.passwordSecret.value | string | `""` | The password value to use when creating the secret |
| recovery.pgBaseBackup.source.port | int | `5432` |  |
| recovery.pgBaseBackup.source.sslCertSecret.key | string | `""` |  |
| recovery.pgBaseBackup.source.sslCertSecret.name | string | `""` |  |
| recovery.pgBaseBackup.source.sslKeySecret.key | string | `""` |  |
| recovery.pgBaseBackup.source.sslKeySecret.name | string | `""` |  |
| recovery.pgBaseBackup.source.sslMode | string | `"verify-full"` |  |
| recovery.pgBaseBackup.source.sslRootCertSecret.key | string | `""` |  |
| recovery.pgBaseBackup.source.sslRootCertSecret.name | string | `""` |  |
| recovery.pgBaseBackup.source.username | string | `""` |  |
| recovery.pitrTarget.time | string | `""` | Time in RFC3339 format |
| recovery.provider | string | `"s3"` | One of `s3`, `azure` or `google` |
| recovery.s3.accessKey | string | `""` |  |
| recovery.s3.bucket | string | `""` |  |
| recovery.s3.inheritFromIAMRole | bool | `false` | Use the role based authentication without providing explicitly the keys |
| recovery.s3.path | string | `"/"` |  |
| recovery.s3.region | string | `""` |  |
| recovery.s3.secretKey | string | `""` |  |
| recovery.secret.create | bool | `true` | Whether to create a secret for the backup credentials |
| recovery.secret.name | string | `""` | Name of the backup credentials secret |
| replica.bootstrap.database | string | `""` | Name of the database used by the application |
| replica.bootstrap.owner | string | `""` | Name of the owner of the database in the instance to be used by applications. Defaults to the value of the `database` key. |
| replica.bootstrap.secret | string | `""` | Name of the secret containing the initial credentials for the owner of the user database. If empty a new secret will be created from scratch |
| replica.bootstrap.source | string | `""` | One of `object_store` or `pg_basebackup`. Method to use for bootstrap. |
| replica.minApplyDelay | string | `""` | When replica mode is enabled, this parameter allows you to replay transactions only when the system time is at least the configured time past the commit time. This provides an opportunity to correct data loss errors. Note that when this parameter is set, a promotion token cannot be used. |
| replica.origin.objectStore.azure.connectionString | string | `""` |  |
| replica.origin.objectStore.azure.containerName | string | `""` |  |
| replica.origin.objectStore.azure.inheritFromAzureAD | bool | `false` |  |
| replica.origin.objectStore.azure.path | string | `"/"` |  |
| replica.origin.objectStore.azure.serviceName | string | `"blob"` |  |
| replica.origin.objectStore.azure.storageAccount | string | `""` |  |
| replica.origin.objectStore.azure.storageKey | string | `""` |  |
| replica.origin.objectStore.azure.storageSasToken | string | `""` |  |
| replica.origin.objectStore.clusterName | string | `""` | The original cluster name when used in backups. Also known as serverName. |
| replica.origin.objectStore.destinationPath | string | `""` | Overrides the provider specific default path. Defaults to: S3: s3://<bucket><path> Azure: https://<storageAccount>.<serviceName>.core.windows.net/<containerName><path> Google: gs://<bucket><path> |
| replica.origin.objectStore.endpointCA | object | `{"create":false,"key":"","name":"","value":""}` | Specifies a CA bundle to validate a privately signed certificate. |
| replica.origin.objectStore.endpointCA.create | bool | `false` | Creates a secret with the given value if true, otherwise uses an existing secret. |
| replica.origin.objectStore.google.applicationCredentials | string | `""` |  |
| replica.origin.objectStore.google.bucket | string | `""` |  |
| replica.origin.objectStore.google.gkeEnvironment | bool | `false` |  |
| replica.origin.objectStore.google.path | string | `"/"` |  |
| replica.origin.objectStore.provider | string | `""` | One of `s3`, `azure` or `google` |
| replica.origin.objectStore.s3.accessKey | string | `""` |  |
| replica.origin.objectStore.s3.bucket | string | `""` |  |
| replica.origin.objectStore.s3.inheritFromIAMRole | bool | `false` | Use the role based authentication without providing explicitly the keys |
| replica.origin.objectStore.s3.path | string | `"/"` |  |
| replica.origin.objectStore.s3.region | string | `""` |  |
| replica.origin.objectStore.s3.secretKey | string | `""` |  |
| replica.origin.objectStore.secret.create | bool | `true` | Whether to create a secret for the backup credentials |
| replica.origin.objectStore.secret.name | string | `""` | Name of the backup credentials secret |
| replica.origin.pg_basebackup.database | string | `""` |  |
| replica.origin.pg_basebackup.host | string | `""` |  |
| replica.origin.pg_basebackup.passwordSecret.key | string | `""` |  |
| replica.origin.pg_basebackup.passwordSecret.name | string | `""` |  |
| replica.origin.pg_basebackup.port | int | `5432` |  |
| replica.origin.pg_basebackup.sslCertSecret.key | string | `""` |  |
| replica.origin.pg_basebackup.sslCertSecret.name | string | `""` |  |
| replica.origin.pg_basebackup.sslKeySecret.key | string | `""` |  |
| replica.origin.pg_basebackup.sslKeySecret.name | string | `""` |  |
| replica.origin.pg_basebackup.sslMode | string | `"verify-full"` |  |
| replica.origin.pg_basebackup.sslRootCertSecret.key | string | `""` |  |
| replica.origin.pg_basebackup.sslRootCertSecret.name | string | `""` |  |
| replica.origin.pg_basebackup.username | string | `""` |  |
| replica.primary | string | `""` | Primary defines which Cluster is defined to be the primary in the distributed PostgreSQL cluster, based on the topology specified in externalClusters |
| replica.promotionToken | string | `""` | A demotion token generated by an external cluster used to check if the promotion requirements are met. |
| replica.self | string | `""` | Defines the name of this cluster. It is used to determine if this is a primary or a replica cluster, comparing it with primary. Leave empty by default. |
| type | string | `"paradedb"` | Type of the CNPG database. Available types: * `paradedb` * `paradedb-enterprise` |
| version.paradedb | string | `"0.22.3"` | We default to v0.22.3 for testing and local development |
| version.postgresql | string | `"18"` | PostgreSQL major version to use |
| poolers[].name | string | `` | Name of the pooler resource |
| poolers[].instances | number | `1` | The number of replicas we want |
| poolers[].type | [PoolerType][PoolerType] | `rw` | Type of service to forward traffic to. Default: `rw`. |
| poolers[].poolMode | [PgBouncerPoolMode][PgBouncerPoolMode] | `session` | The pool mode. Default: `session`. |
| poolers[].authQuerySecret | [LocalObjectReference][LocalObjectReference] | `{}` | The credentials of the user that need to be used for the authentication query. |
| poolers[].authQuery | string | `{}` | The credentials of the user that need to be used for the authentication query. |
| poolers[].parameters | map[string]string | `{}` | Additional parameters to be passed to PgBouncer - please check the CNPG documentation for a list of options you can configure |
| poolers[].template | [PodTemplateSpec][PodTemplateSpec] | `{}` | The template of the Pod to be created |
| poolers[].template | [ServiceTemplateSpec][ServiceTemplateSpec] | `{}` | Template for the Service to be created |
| poolers[].pg_hba | []string | `{}` | PostgreSQL Host Based Authentication rules (lines to be appended to the pg_hba.conf file) |
| poolers[].monitoring.enabled | bool | `false` | Whether to enable monitoring for the Pooler. |
| poolers[].monitoring.podMonitor.enabled | bool | `true` | Create a podMonitor for the Pooler. |

## Maintainers

| Name | Email | Url |
| ---- | ------ | --- |
| ParadeDB | <support@paradedb.com> | <https://paradedb.com> |

## License

Apache-2.0 License - see [LICENSE](LICENSE) for details.

```

## File: charts\paradedb\values.schema.json
```
{
    "$schema": "http://json-schema.org/schema#",
    "type": "object",
    "properties": {
        "backups": {
            "type": "object",
            "properties": {
                "azure": {
                    "type": "object",
                    "properties": {
                        "connectionString": {
                            "type": "string"
                        },
                        "containerName": {
                            "type": "string"
                        },
                        "inheritFromAzureAD": {
                            "type": "boolean"
                        },
                        "path": {
                            "type": "string"
                        },
                        "serviceName": {
                            "type": "string"
                        },
                        "storageAccount": {
                            "type": "string"
                        },
                        "storageKey": {
                            "type": "string"
                        },
                        "storageSasToken": {
                            "type": "string"
                        }
                    }
                },
                "data": {
                    "type": "object",
                    "properties": {
                        "compression": {
                            "type": "string"
                        },
                        "encryption": {
                            "type": "string"
                        },
                        "jobs": {
                            "type": "integer"
                        }
                    }
                },
                "destinationPath": {
                    "type": "string"
                },
                "enabled": {
                    "type": "boolean"
                },
                "endpointCA": {
                    "type": "object",
                    "properties": {
                        "create": {
                            "type": "boolean"
                        },
                        "key": {
                            "type": "string"
                        },
                        "name": {
                            "type": "string"
                        },
                        "value": {
                            "type": "string"
                        }
                    }
                },
                "endpointURL": {
                    "type": "string"
                },
                "google": {
                    "type": "object",
                    "properties": {
                        "applicationCredentials": {
                            "type": "string"
                        },
                        "bucket": {
                            "type": "string"
                        },
                        "gkeEnvironment": {
                            "type": "boolean"
                        },
                        "path": {
                            "type": "string"
                        }
                    }
                },
                "provider": {
                    "type": "string"
                },
                "retentionPolicy": {
                    "type": "string"
                },
                "s3": {
                    "type": "object",
                    "properties": {
                        "accessKey": {
                            "type": "string"
                        },
                        "bucket": {
                            "type": "string"
                        },
                        "inheritFromIAMRole": {
                            "type": "boolean"
                        },
                        "path": {
                            "type": "string"
                        },
                        "region": {
                            "type": "string"
                        },
                        "secretKey": {
                            "type": "string"
                        }
                    }
                },
                "scheduledBackups": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "backupOwnerReference": {
                                "type": "string"
                            },
                            "method": {
                                "type": "string"
                            },
                            "name": {
                                "type": "string"
                            },
                            "schedule": {
                                "type": "string"
                            }
                        }
                    }
                },
                "secret": {
                    "type": "object",
                    "properties": {
                        "create": {
                            "type": "boolean"
                        },
                        "name": {
                            "type": "string"
                        }
                    }
                },
                "wal": {
                    "type": "object",
                    "properties": {
                        "compression": {
                            "type": "string"
                        },
                        "encryption": {
                            "type": "string"
                        },
                        "maxParallel": {
                            "type": "integer"
                        }
                    }
                }
            }
        },
        "cluster": {
            "type": "object",
            "properties": {
                "additionalLabels": {
                    "type": "object"
                },
                "affinity": {
                    "type": "object",
                    "properties": {
                        "topologyKey": {
                            "type": "string"
                        }
                    }
                },
                "annotations": {
                    "type": "object"
                },
                "certificates": {
                    "type": "object"
                },
                "console": {
                    "type": "object",
                    "properties": {
                        "enabled": {
                            "type": "boolean"
                        }
                    }
                },
                "enablePDB": {
                    "type": "boolean"
                },
                "enableSuperuserAccess": {
                    "type": "boolean"
                },
                "env": {
                    "type": "array"
                },
                "envFrom": {
                    "type": "array"
                },
                "imageCatalogRef": {
                    "type": "object"
                },
                "imageName": {
                    "type": "string"
                },
                "imagePullPolicy": {
                    "type": "string"
                },
                "imagePullSecrets": {
                    "type": "array"
                },
                "initdb": {
                    "type": "object",
                    "properties": {
                        "database": {
                            "type": "string"
                        }
                    }
                },
                "instances": {
                    "type": "integer"
                },
                "logLevel": {
                    "type": "string"
                },
                "monitoring": {
                    "type": "object",
                    "properties": {
                        "customQueries": {
                            "type": "array"
                        },
                        "customQueriesSecret": {
                            "type": "array"
                        },
                        "disableDefaultQueries": {
                            "type": "boolean"
                        },
                        "enabled": {
                            "type": "boolean"
                        },
                        "instrumentation": {
                            "type": "object",
                            "properties": {
                                "logicalReplication": {
                                    "type": "boolean"
                                },
                                "paradedbIndex": {
                                    "type": "boolean"
                                }
                            }
                        },
                        "podMonitor": {
                            "type": "object",
                            "properties": {
                                "enabled": {
                                    "type": "boolean"
                                },
                                "labels": {
                                    "type": "object"
                                },
                                "metricRelabelings": {
                                    "type": "array"
                                },
                                "relabelings": {
                                    "type": "array"
                                }
                            }
                        },
                        "prometheusRule": {
                            "type": "object",
                            "properties": {
                                "enabled": {
                                    "type": "boolean"
                                },
                                "excludeRules": {
                                    "type": "array"
                                }
                            }
                        }
                    }
                },
                "podSecurityContext": {
                    "type": "object"
                },
                "postgresGID": {
                    "type": "integer"
                },
                "postgresUID": {
                    "type": "integer"
                },
                "postgresql": {
                    "type": "object",
                    "properties": {
                        "ldap": {
                            "type": "object"
                        },
                        "parameters": {
                            "type": "object"
                        },
                        "pg_hba": {
                            "type": "array"
                        },
                        "pg_ident": {
                            "type": "array"
                        },
                        "shared_preload_libraries": {
                            "type": "array"
                        },
                        "synchronous": {
                            "type": "object"
                        }
                    }
                },
                "primaryUpdateMethod": {
                    "type": "string"
                },
                "primaryUpdateStrategy": {
                    "type": "string"
                },
                "priorityClassName": {
                    "type": "string"
                },
                "resources": {
                    "type": "object"
                },
                "roles": {
                    "type": "array"
                },
                "securityContext": {
                    "type": "object"
                },
                "serviceAccountTemplate": {
                    "type": "object"
                },
                "services": {
                    "type": "object"
                },
                "storage": {
                    "type": "object",
                    "properties": {
                        "size": {
                            "type": "string"
                        },
                        "storageClass": {
                            "type": "string"
                        }
                    }
                },
                "superuserSecret": {
                    "type": "string"
                },
                "walStorage": {
                    "type": "object",
                    "properties": {
                        "enabled": {
                            "type": "boolean"
                        },
                        "size": {
                            "type": "string"
                        },
                        "storageClass": {
                            "type": "string"
                        }
                    }
                }
            }
        },
        "databases": {
            "type": "array"
        },
        "fullnameOverride": {
            "type": "string"
        },
        "imageCatalog": {
            "type": "object",
            "properties": {
                "create": {
                    "type": "boolean"
                },
                "images": {
                    "type": "array"
                }
            }
        },
        "mode": {
            "type": "string"
        },
        "monitoring": {
            "type": "object",
            "properties": {
                "grafanaDashboard": {
                    "type": "object",
                    "properties": {
                        "annotations": {
                            "type": "object"
                        },
                        "configMapName": {
                            "type": "string"
                        },
                        "create": {
                            "type": "boolean"
                        },
                        "labels": {
                            "type": "object",
                            "properties": {
                                "grafana_dashboard": {
                                    "type": "string"
                                }
                            }
                        },
                        "namespace": {
                            "type": "string"
                        }
                    }
                }
            }
        },
        "nameOverride": {
            "type": "string"
        },
        "namespaceOverride": {
            "type": "string"
        },
        "poolers": {
            "type": "array"
        },
        "recovery": {
            "type": "object",
            "properties": {
                "azure": {
                    "type": "object",
                    "properties": {
                        "connectionString": {
                            "type": "string"
                        },
                        "containerName": {
                            "type": "string"
                        },
                        "inheritFromAzureAD": {
                            "type": "boolean"
                        },
                        "path": {
                            "type": "string"
                        },
                        "serviceName": {
                            "type": "string"
                        },
                        "storageAccount": {
                            "type": "string"
                        },
                        "storageKey": {
                            "type": "string"
                        },
                        "storageSasToken": {
                            "type": "string"
                        }
                    }
                },
                "backupName": {
                    "type": "string"
                },
                "clusterName": {
                    "type": "string"
                },
                "database": {
                    "type": "string"
                },
                "destinationPath": {
                    "type": "string"
                },
                "endpointCA": {
                    "type": "object",
                    "properties": {
                        "create": {
                            "type": "boolean"
                        },
                        "key": {
                            "type": "string"
                        },
                        "name": {
                            "type": "string"
                        },
                        "value": {
                            "type": "string"
                        }
                    }
                },
                "endpointURL": {
                    "type": "string"
                },
                "google": {
                    "type": "object",
                    "properties": {
                        "applicationCredentials": {
                            "type": "string"
                        },
                        "bucket": {
                            "type": "string"
                        },
                        "gkeEnvironment": {
                            "type": "boolean"
                        },
                        "path": {
                            "type": "string"
                        }
                    }
                },
                "import": {
                    "type": "object",
                    "properties": {
                        "databases": {
                            "type": "array"
                        },
                        "pgDumpExtraOptions": {
                            "type": "array"
                        },
                        "pgRestoreExtraOptions": {
                            "type": "array"
                        },
                        "postImportApplicationSQL": {
                            "type": "array"
                        },
                        "roles": {
                            "type": "array"
                        },
                        "schemaOnly": {
                            "type": "boolean"
                        },
                        "source": {
                            "type": "object",
                            "properties": {
                                "database": {
                                    "type": "string"
                                },
                                "host": {
                                    "type": "string"
                                },
                                "passwordSecret": {
                                    "type": "object",
                                    "properties": {
                                        "create": {
                                            "type": "boolean"
                                        },
                                        "key": {
                                            "type": "string"
                                        },
                                        "name": {
                                            "type": "string"
                                        },
                                        "value": {
                                            "type": "string"
                                        }
                                    }
                                },
                                "port": {
                                    "type": "integer"
                                },
                                "sslCertSecret": {
                                    "type": "object",
                                    "properties": {
                                        "key": {
                                            "type": "string"
                                        },
                                        "name": {
                                            "type": "string"
                                        }
                                    }
                                },
                                "sslKeySecret": {
                                    "type": "object",
                                    "properties": {
                                        "key": {
                                            "type": "string"
                                        },
                                        "name": {
                                            "type": "string"
                                        }
                                    }
                                },
                                "sslMode": {
                                    "type": "string"
                                },
                                "sslRootCertSecret": {
                                    "type": "object",
                                    "properties": {
                                        "key": {
                                            "type": "string"
                                        },
                                        "name": {
                                            "type": "string"
                                        }
                                    }
                                },
                                "username": {
                                    "type": "string"
                                }
                            }
                        },
                        "type": {
                            "type": "string"
                        }
                    }
                },
                "method": {
                    "type": "string"
                },
                "owner": {
                    "type": "string"
                },
                "pgBaseBackup": {
                    "type": "object",
                    "properties": {
                        "database": {
                            "type": "string"
                        },
                        "owner": {
                            "type": "string"
                        },
                        "secretName": {
                            "type": "string"
                        },
                        "source": {
                            "type": "object",
                            "properties": {
                                "database": {
                                    "type": "string"
                                },
                                "host": {
                                    "type": "string"
                                },
                                "passwordSecret": {
                                    "type": "object",
                                    "properties": {
                                        "create": {
                                            "type": "boolean"
                                        },
                                        "key": {
                                            "type": "string"
                                        },
                                        "name": {
                                            "type": "string"
                                        },
                                        "value": {
                                            "type": "string"
                                        }
                                    }
                                },
                                "port": {
                                    "type": "integer"
                                },
                                "sslCertSecret": {
                                    "type": "object",
                                    "properties": {
                                        "key": {
                                            "type": "string"
                                        },
                                        "name": {
                                            "type": "string"
                                        }
                                    }
                                },
                                "sslKeySecret": {
                                    "type": "object",
                                    "properties": {
                                        "key": {
                                            "type": "string"
                                        },
                                        "name": {
                                            "type": "string"
                                        }
                                    }
                                },
                                "sslMode": {
                                    "type": "string"
                                },
                                "sslRootCertSecret": {
                                    "type": "object",
                                    "properties": {
                                        "key": {
                                            "type": "string"
                                        },
                                        "name": {
                                            "type": "string"
                                        }
                                    }
                                },
                                "username": {
                                    "type": "string"
                                }
                            }
                        }
                    }
                },
                "pitrTarget": {
                    "type": "object",
                    "properties": {
                        "time": {
                            "type": "string"
                        }
                    }
                },
                "provider": {
                    "type": "string"
                },
                "s3": {
                    "type": "object",
                    "properties": {
                        "accessKey": {
                            "type": "string"
                        },
                        "bucket": {
                            "type": "string"
                        },
                        "inheritFromIAMRole": {
                            "type": "boolean"
                        },
                        "path": {
                            "type": "string"
                        },
                        "region": {
                            "type": "string"
                        },
                        "secretKey": {
                            "type": "string"
                        }
                    }
                },
                "secret": {
                    "type": "object",
                    "properties": {
                        "create": {
                            "type": "boolean"
                        },
                        "name": {
                            "type": "string"
                        }
                    }
                }
            }
        },
        "replica": {
            "type": "object",
            "properties": {
                "bootstrap": {
                    "type": "object",
                    "properties": {
                        "database": {
                            "type": "string"
                        },
                        "owner": {
                            "type": "string"
                        },
                        "secret": {
                            "type": "string"
                        },
                        "source": {
                            "type": "string"
                        }
                    }
                },
                "minApplyDelay": {
                    "type": "string"
                },
                "origin": {
                    "type": "object",
                    "properties": {
                        "objectStore": {
                            "type": "object",
                            "properties": {
                                "azure": {
                                    "type": "object",
                                    "properties": {
                                        "connectionString": {
                                            "type": "string"
                                        },
                                        "containerName": {
                                            "type": "string"
                                        },
                                        "inheritFromAzureAD": {
                                            "type": "boolean"
                                        },
                                        "path": {
                                            "type": "string"
                                        },
                                        "serviceName": {
                                            "type": "string"
                                        },
                                        "storageAccount": {
                                            "type": "string"
                                        },
                                        "storageKey": {
                                            "type": "string"
                                        },
                                        "storageSasToken": {
                                            "type": "string"
                                        }
                                    }
                                },
                                "clusterName": {
                                    "type": "string"
                                },
                                "destinationPath": {
                                    "type": "string"
                                },
                                "endpointCA": {
                                    "type": "object",
                                    "properties": {
                                        "create": {
                                            "type": "boolean"
                                        },
                                        "key": {
                                            "type": "string"
                                        },
                                        "name": {
                                            "type": "string"
                                        },
                                        "value": {
                                            "type": "string"
                                        }
                                    }
                                },
                                "google": {
                                    "type": "object",
                                    "properties": {
                                        "applicationCredentials": {
                                            "type": "string"
                                        },
                                        "bucket": {
                                            "type": "string"
                                        },
                                        "gkeEnvironment": {
                                            "type": "boolean"
                                        },
                                        "path": {
                                            "type": "string"
                                        }
                                    }
                                },
                                "provider": {
                                    "type": "string"
                                },
                                "s3": {
                                    "type": "object",
                                    "properties": {
                                        "accessKey": {
                                            "type": "string"
                                        },
                                        "bucket": {
                                            "type": "string"
                                        },
                                        "inheritFromIAMRole": {
                                            "type": "boolean"
                                        },
                                        "path": {
                                            "type": "string"
                                        },
                                        "region": {
                                            "type": "string"
                                        },
                                        "secretKey": {
                                            "type": "string"
                                        }
                                    }
                                },
                                "secret": {
                                    "type": "object",
                                    "properties": {
                                        "create": {
                                            "type": "boolean"
                                        },
                                        "name": {
                                            "type": "string"
                                        }
                                    }
                                }
                            }
                        },
                        "pg_basebackup": {
                            "type": "object",
                            "properties": {
                                "database": {
                                    "type": "string"
                                },
                                "host": {
                                    "type": "string"
                                },
                                "passwordSecret": {
                                    "type": "object",
                                    "properties": {
                                        "create": {
                                            "type": "boolean"
                                        },
                                        "key": {
                                            "type": "string"
                                        },
                                        "name": {
                                            "type": "string"
                                        },
                                        "value": {
                                            "type": "string"
                                        }
                                    }
                                },
                                "port": {
                                    "type": "integer"
                                },
                                "sslCertSecret": {
                                    "type": "object",
                                    "properties": {
                                        "key": {
                                            "type": "string"
                                        },
                                        "name": {
                                            "type": "string"
                                        }
                                    }
                                },
                                "sslKeySecret": {
                                    "type": "object",
                                    "properties": {
                                        "key": {
                                            "type": "string"
                                        },
                                        "name": {
                                            "type": "string"
                                        }
                                    }
                                },
                                "sslMode": {
                                    "type": "string"
                                },
                                "sslRootCertSecret": {
                                    "type": "object",
                                    "properties": {
                                        "key": {
                                            "type": "string"
                                        },
                                        "name": {
                                            "type": "string"
                                        }
                                    }
                                },
                                "username": {
                                    "type": "string"
                                }
                            }
                        }
                    }
                },
                "primary": {
                    "type": "string"
                },
                "promotionToken": {
                    "type": "string"
                },
                "self": {
                    "type": "string"
                }
            }
        },
        "type": {
            "type": "string"
        },
        "version": {
            "type": "object",
            "properties": {
                "postgresql": {
                    "type": "string"
                },
                "paradedb": {
                    "type": "string"
                }
            }
        }
    }
}

```

## File: charts\paradedb\values.yaml
```
# -- Override the name of the chart
nameOverride: ""
# -- Override the full name of the chart
fullnameOverride: ""
# -- Override the namespace of the chart
namespaceOverride: ""

###
# -- Type of the CNPG database. Available types:
# * `paradedb`
# * `paradedb-enterprise`
type: paradedb

version:
  # -- PostgreSQL major version to use
  postgresql: "18"
  # -- ParadeDB version to use
  paradedb: "0.22.3"

###
# -- Cluster mode of operation. Available modes:
# * `standalone` - default mode. Creates new or updates an existing CNPG cluster.
# * `replica` - Creates a replica cluster from an existing CNPG cluster.
# * `recovery` - Same as standalone but creates a cluster from a backup, object store or via pg_basebackup.
mode: standalone

recovery:
  ##
  # -- Available recovery methods:
  # * `backup` - Recovers a CNPG cluster from a CNPG backup (PITR supported) Needs to be on the same cluster in the same namespace.
  # * `object_store` - Recovers a CNPG cluster from a barman object store (PITR supported).
  # * `pg_basebackup` - Recovers a CNPG cluster via a streaming replication protocol. Useful if you want to
  #        migrate databases to CloudNativePG, even from outside Kubernetes.
  # * `import` - Import one or more databases from an existing Postgres cluster.
  method: backup

  ## -- Point in time recovery target. Specify one of the following:
  pitrTarget:
    # -- Time in RFC3339 format
    time: ""

  ##
  # -- Backup Recovery Method
  backupName: ""  # Name of the backup to recover from. Required if method is `backup`.

  ##
  # -- The original cluster name when used in backups. Also known as serverName.
  clusterName: ""
  # -- Name of the database used by the application. Default: `paradedb`.
  database: paradedb
  # -- Name of the owner of the database in the instance to be used by applications. Defaults to the value of the `database` key.
  owner: ""
  # -- Overrides the provider specific default endpoint. Defaults to:
  # S3: https://s3.<region>.amazonaws.com
  # Leave empty if using the default S3 endpoint
  endpointURL: ""
  # -- Specifies a CA bundle to validate a privately signed certificate.
  endpointCA:
    # -- Creates a secret with the given value if true, otherwise uses an existing secret.
    create: false
    name: ""
    key: ""
    value: ""
  # -- Overrides the provider specific default path. Defaults to:
  # S3: s3://<bucket><path>
  # Azure: https://<storageAccount>.<serviceName>.core.windows.net/<containerName><path>
  # Google: gs://<bucket><path>
  destinationPath: ""
  # -- One of `s3`, `azure` or `google`
  provider: s3
  s3:
    region: ""
    bucket: ""
    path: "/"
    accessKey: ""
    secretKey: ""
    # -- Use the role based authentication without providing explicitly the keys
    inheritFromIAMRole: false
  azure:
    path: "/"
    connectionString: ""
    storageAccount: ""
    storageKey: ""
    storageSasToken: ""
    containerName: ""
    serviceName: blob
    inheritFromAzureAD: false
  google:
    path: "/"
    bucket: ""
    gkeEnvironment: false
    applicationCredentials: ""
  secret:
    # -- Whether to create a secret for the backup credentials
    create: true
    # -- Name of the backup credentials secret
    name: ""

  # See https://cloudnative-pg.io/documentation/current/bootstrap/#bootstrap-from-a-live-cluster-pg_basebackup
  pgBaseBackup:
    # -- Name of the database used by the application. Default: `paradedb`.
    database: paradedb
    # -- Name of the kubernetes.io/basic-auth secret containing the initial credentials for the owner of the user database. If empty a new secret will be created from scratch.
    secretName: ""
    # -- Name of the owner of the database in the instance to be used by applications. Defaults to the value of the `database` key.
    owner: ""
    source:
      host: ""
      port: 5432
      username: ""
      database: "paradedb"
      sslMode: "verify-full"
      passwordSecret:
        # -- Whether to create a secret for the password
        create: false
        # -- Name of the secret containing the password
        name: ""
        # -- The key in the secret containing the password
        key: "password"
        # -- The password value to use when creating the secret
        value: ""
      sslKeySecret:
        name: ""
        key: ""
      sslCertSecret:
        name: ""
        key: ""
      sslRootCertSecret:
        name: ""
        key: ""

  # See: https://cloudnative-pg.io/documentation/current/cloudnative-pg.v1/#postgresql-cnpg-io-v1-Import
  import:
    # -- One of `microservice` or `monolith`
    # See: https://cloudnative-pg.io/documentation/current/database_import/#how-it-works
    type: "microservice"
    # -- Databases to import
    databases: []
    # -- Roles to import
    roles: []
    # -- List of SQL queries to be executed as a superuser in the application database right after is imported.
    # To be used with extreme care. Only available in microservice type.
    postImportApplicationSQL: []
    # -- When set to true, only the pre-data and post-data sections of pg_restore are invoked, avoiding data import.
    schemaOnly: false
    # -- List of custom options to pass to the `pg_dump` command. IMPORTANT: Use these options with caution and at your
    # own risk, as the operator does not validate their content. Be aware that certain options may conflict with the
    # operator's intended functionality or design.
    pgDumpExtraOptions: []
    # -- List of custom options to pass to the `pg_restore` command. IMPORTANT: Use these options with caution and at
    # your own risk, as the operator does not validate their content. Be aware that certain options may conflict with the
    # operator's intended functionality or design.
    pgRestoreExtraOptions: []
    source:
      host: ""
      port: 5432
      username: ""
      database: "paradedb"
      sslMode: "verify-full"
      passwordSecret:
        # -- Whether to create a secret for the password
        create: false
        # -- Name of the secret containing the password
        name: ""
        # -- The key in the secret containing the password
        key: "password"
        # -- The password value to use when creating the secret
        value: ""
      sslKeySecret:
        name: ""
        key: ""
      sslCertSecret:
        name: ""
        key: ""
      sslRootCertSecret:
        name: ""
        key: ""

cluster:
  # -- Number of instances
  instances: 1

  # -- Name of the container image, supporting both tags (<image>:<tag>) and digests for deterministic and repeatable deployments:
  # <image>:<tag>@sha256:<digestValue>
  imageName: ""  # Default value depends on type (postgresql/paradedb)

  # -- Reference to `ImageCatalog` of `ClusterImageCatalog`, if specified takes precedence over `cluster.imageName`
  imageCatalogRef: {}
    # kind: ImageCatalog
    # name: postgresql

  # -- Image pull policy. One of Always, Never or IfNotPresent. If not defined, it defaults to IfNotPresent. Cannot be updated.
  # More info: https://kubernetes.io/docs/concepts/containers/images#updating-images
  imagePullPolicy: IfNotPresent

  # -- The list of pull secrets to be used to pull the images.
  # See: https://cloudnative-pg.io/documentation/current/cloudnative-pg.v1/#postgresql-cnpg-io-v1-LocalObjectReference
  imagePullSecrets: []

  storage:
    size: 8Gi
    storageClass: ""

  walStorage:
    enabled: false
    size: 1Gi
    storageClass: ""

  # -- The UID of the postgres user inside the image, defaults to 999 for ParadeDB and 26 for PostgreSQL
  postgresUID: -1

  # -- The GID of the postgres user inside the image, defaults to 999 for ParadeDB and 26 for PostgreSQL
  postgresGID: -1

  # -- Customization of service definitions. Please refer to https://cloudnative-pg.io/documentation/current/service_management/
  services: {}

  # -- Resources requirements of every generated Pod.
  # Please refer to https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/ for more information.
  # We strongly advise you use the same setting for limits and requests so that your cluster pods are given a Guaranteed QoS.
  # See: https://kubernetes.io/docs/concepts/workloads/pods/pod-qos/
  resources: {}
    # limits:
    #   cpu: 2000m
    #   memory: 8Gi
    # requests:
    #   cpu: 2000m
    #   memory: 8Gi

  priorityClassName: ""

  # -- Method to follow to upgrade the primary server during a rolling update procedure, after all replicas have been
  # successfully updated. It can be switchover (default) or restart.
  primaryUpdateMethod: switchover

  # -- Strategy to follow to upgrade the primary server during a rolling update procedure, after all replicas have been
  # successfully updated: it can be automated (unsupervised - default) or manual (supervised)
  primaryUpdateStrategy: unsupervised

  # -- The instances' log level, one of the following values: error, warning, info (default), debug, trace
  logLevel: "info"

  # -- Affinity/Anti-affinity rules for Pods.
  # See: https://cloudnative-pg.io/documentation/current/cloudnative-pg.v1/#postgresql-cnpg-io-v1-AffinityConfiguration
  affinity:
    topologyKey: topology.kubernetes.io/zone

  # -- Env follows the Env format to pass environment variables to the pods created in the cluster
  env: []
    # - name: MY_CUSTOM_FLAG
    #   value: "enabled"
    # - name: MY_CUSTOM_ENV
    #   valueFrom:
    #     configMapKeyRef:
    #       name: my-custom-env
    #       key: env
    #       optional: true
    # - name: MY_CUSTOM_SECRET_ENV
    #   valueFrom:
    #     secretKeyRef:
    #       name: my-custom-secret
    #       key: secret
    #       optional: true

  # -- EnvFrom follows the EnvFrom format to pass environment variables sources to the pods to be used by Env
  envFrom: []
    # - configMapRef:
    #     name: global-envs
    #     optional: true
    # - secretRef:
    #     name: db-credentials
    #     optional: true

  # -- The configuration for the CA and related certificates.
  # See: https://cloudnative-pg.io/documentation/current/cloudnative-pg.v1/#postgresql-cnpg-io-v1-CertificatesConfiguration
  certificates: {}

  # -- When this option is enabled, the operator will use the SuperuserSecret to update the postgres user password.
  # If the secret is not present, the operator will automatically create one.
  # When this option is disabled, the operator will ignore the SuperuserSecret content, delete it when automatically created,
  # and then blank the password of the postgres user by setting it to NULL.
  enableSuperuserAccess: true
  superuserSecret: ""

  # -- Allows disabling PDB, mainly useful for upgrade of single-instance clusters or development purposes
  # See: https://cloudnative-pg.io/documentation/current/kubernetes_upgrade/#pod-disruption-budgets
  enablePDB: true

  # -- This feature enables declarative management of existing roles, as well as the creation of new roles if they are not
  # already present in the database.
  # See: https://cloudnative-pg.io/documentation/current/declarative_role_management/
  roles: []
    # - name: dante
    #   ensure: present
    #   comment: Dante Alighieri
    #   login: true
    #   superuser: false
    #   inRoles:
    #     - pg_monitor
    #     - pg_signal_backend

  monitoring:
    # -- Whether to enable monitoring
    enabled: false
    instrumentation:
      # -- Enable ParadeDB index metrics
      paradedbIndex: true
      # -- Enable logical replication metrics
      logicalReplication: true
      # -- Enable pg_stat_statements metrics
      pgStatStatements: true
    podMonitor:
      # -- Whether to enable the PodMonitor
      enabled: true
      # -- Additional labels to set on the generated PodMonitor resource.
      # Add labels your monitoring stack requires (for example `team-name`).
      labels: {}
      # -- The list of relabelings for the PodMonitor.
      # Applied to samples before scraping.
      relabelings: []
      # -- The list of metric relabelings for the PodMonitor.
      # Applied to samples before ingestion.
      metricRelabelings: []
    prometheusRule:
      # -- Whether to enable the PrometheusRule automated alerts
      enabled: true
      # -- Exclude specified rules
      excludeRules: []
        # - CNPGClusterZoneSpreadWarning
    # -- Whether the default queries should be injected.
    # Set it to true if you don't want to inject default queries into the cluster.
    disableDefaultQueries: false
    # -- Custom Prometheus metrics
    # Will be stored in the ConfigMap
    customQueries: []
    #  - name: "pg_cache_hit_ratio"
    #    query: "SELECT current_database() as datname, sum(heap_blks_hit) / (sum(heap_blks_hit) + sum(heap_blks_read)) as ratio FROM pg_statio_user_tables;"
    #    target_databases: ["*"]
    #    predicate_query: "SELECT '{{ .Values.version.postgresql }}';"
    #    metrics:
    #      - datname:
    #          usage: "LABEL"
    #          description: "Name of the database"
    #      - ratio:
    #          usage: GAUGE
    #          description: "Cache hit ratio"
    # -- The list of secrets containing the custom queries
    customQueriesSecret: []
    #  - name: custom-queries-secret
    #    key: custom-queries

  postgresql:
    # -- PostgreSQL configuration options (postgresql.conf)
    parameters: {}
      # max_connections: 300
    # -- Quorum-based Synchronous Replication
    synchronous: {}
     # method: any
     # number: 1
    # -- PostgreSQL Host Based Authentication rules (lines to be appended to the pg_hba.conf file)
    pg_hba: []
      # - host all all 10.244.0.0/16 md5
    # -- PostgreSQL User Name Maps rules (lines to be appended to the pg_ident.conf file)
    pg_ident: []
      # - mymap   /^(.*)@mydomain\.com$      \1
    # -- Lists of shared preload libraries to add to the default ones
    shared_preload_libraries: []
      # - pgaudit
    # -- PostgreSQL LDAP configuration (see https://cloudnative-pg.io/documentation/current/postgresql_conf/#ldap-configuration)
    ldap: {}
      # https://cloudnative-pg.io/documentation/current/postgresql_conf/#ldap-configuration
      # server: 'openldap.default.svc.cluster.local'
      # bindSearchAuth:
        # baseDN: 'ou=org,dc=example,dc=com'
        # bindDN: 'cn=admin,dc=example,dc=com'
        # bindPassword:
          # name: 'ldapBindPassword'
          # key: 'data'
        # searchAttribute: 'uid'


  # -- BootstrapInitDB is the configuration of the bootstrap process when initdb is used.
  # See: https://cloudnative-pg.io/documentation/current/bootstrap/
  # See: https://cloudnative-pg.io/documentation/current/cloudnative-pg.v1/#postgresql-cnpg-io-v1-bootstrapinitdb
  initdb:
    database: paradedb
    # owner: "" # Defaults to the database name
    # secret:
    #   name: "" # Name of the secret containing the initial credentials for the owner of the user database. If empty a new secret will be created from scratch
    # options: []
    # encoding: UTF8
    # postInitSQL: []
    # postInitApplicationSQL: []
    # postInitTemplateSQL: []

  # -- Configure the metadata of the generated service account
  serviceAccountTemplate: {}

  # -- Configure the Pod Security Context.
  # See: https://cloudnative-pg.io/documentation/preview/security/
  podSecurityContext: {}

  # -- Configure Container Security Context.
  # See: https://cloudnative-pg.io/documentation/preview/security/
  securityContext: {}

  additionalLabels: {}
  annotations: {}

  console:
    # -- Deploys a console StatefulSet to run long-running commands against the cluster (e.g. `CREATE INDEX`).
    enabled: false

backups:
  # -- You need to configure backups manually, so backups are disabled by default.
  enabled: false

  # -- Overrides the provider specific default endpoint. Defaults to:
  # S3: https://s3.<region>.amazonaws.com
  endpointURL: ""  # Leave empty if using the default S3 endpoint
  # -- Specifies a CA bundle to validate a privately signed certificate.
  endpointCA:
    # -- Creates a secret with the given value if true, otherwise uses an existing secret.
    create: false
    name: ""
    key: ""
    value: ""

  # -- Overrides the provider specific default path. Defaults to:
  # S3: s3://<bucket><path>
  # Azure: https://<storageAccount>.<serviceName>.core.windows.net/<containerName><path>
  # Google: gs://<bucket><path>
  destinationPath: ""
  # -- One of `s3`, `azure` or `google`
  provider: s3
  s3:
    region: ""
    bucket: ""
    path: "/"
    accessKey: ""
    secretKey: ""
    # -- Use the role based authentication without providing explicitly the keys
    inheritFromIAMRole: false
  azure:
    path: "/"
    connectionString: ""
    storageAccount: ""
    storageKey: ""
    storageSasToken: ""
    containerName: ""
    serviceName: blob
    inheritFromAzureAD: false
  google:
    path: "/"
    bucket: ""
    gkeEnvironment: false
    applicationCredentials: ""
  secret:
    # -- Whether to create a secret for the backup credentials
    create: true
    # -- Name of the backup credentials secret
    name: ""

  wal:
    # -- WAL compression method. One of `` (for no compression), `gzip`, `bzip2` or `snappy`.
    compression: gzip
    # -- Whether to instruct the storage provider to encrypt WAL files. One of `` (use the storage container default), `AES256` or `aws:kms`.
    encryption: AES256
    # -- Number of WAL files to be archived or restored in parallel.
    maxParallel: 1
  data:
    # -- Data compression method. One of `` (for no compression), `gzip`, `bzip2` or `snappy`.
    compression: gzip
    # -- Whether to instruct the storage provider to encrypt data files. One of `` (use the storage container default), `AES256` or `aws:kms`.
    encryption: AES256
    # -- Number of data files to be archived or restored in parallel.
    jobs: 2

  scheduledBackups:
    -
      # -- Scheduled backup name
      name: daily-backup
      # -- Schedule in cron format
      schedule: "0 0 0 * * *"
      # -- Backup owner reference
      backupOwnerReference: self
      # -- Backup method, can be `barmanObjectStore` (default) or `volumeSnapshot`
      method: barmanObjectStore

  # -- Retention policy for backups
  retentionPolicy: "30d"

replica:
  # -- Defines the name of this cluster. It is used to determine if this is a primary or a replica cluster, comparing it with primary. Leave empty by default.
  self: ""
  # -- Primary defines which Cluster is defined to be the primary in the distributed PostgreSQL cluster, based on the topology specified in externalClusters
  primary: ""
  # -- A demotion token generated by an external cluster used to check if the promotion requirements are met.
  promotionToken: ""
  # -- When replica mode is enabled, this parameter allows you to replay transactions only when the system time is at least the configured time past the commit time. This provides an opportunity to correct data loss errors. Note that when this parameter is set, a promotion token cannot be used.
  minApplyDelay: ""
  bootstrap:
    # -- One of `object_store` or `pg_basebackup`. Method to use for bootstrap.
    source: ""
    # -- Name of the database used by the application
    database: ""
    # -- Name of the secret containing the initial credentials for the owner of the user database. If empty a new secret will be created from scratch
    secret: ""
    # -- Name of the owner of the database in the instance to be used by applications. Defaults to the value of the `database` key.
    owner: ""
  origin:
    objectStore:
      # -- The original cluster name when used in backups. Also known as serverName.
      clusterName: ""
      # -- Overrides the provider specific default path. Defaults to:
      # S3: s3://<bucket><path>
      # Azure: https://<storageAccount>.<serviceName>.core.windows.net/<containerName><path>
      # Google: gs://<bucket><path>
      destinationPath: ""
      # -- Specifies a CA bundle to validate a privately signed certificate.
      endpointCA:
        # -- Creates a secret with the given value if true, otherwise uses an existing secret.
        create: false
        name: ""
        key: ""
        value: ""
      # -- One of `s3`, `azure` or `google`
      provider: ""
      s3:
        region: ""
        bucket: ""
        path: "/"
        accessKey: ""
        secretKey: ""
        # -- Use the role based authentication without providing explicitly the keys
        inheritFromIAMRole: false
      azure:
        path: "/"
        connectionString: ""
        storageAccount: ""
        storageKey: ""
        storageSasToken: ""
        containerName: ""
        serviceName: blob
        inheritFromAzureAD: false
      google:
        path: "/"
        bucket: ""
        gkeEnvironment: false
        applicationCredentials: ""
      secret:
        # -- Whether to create a secret for the backup credentials
        create: true
        # -- Name of the backup credentials secret
        name: ""
    pg_basebackup:
      host: ""
      port: 5432
      username: ""
      sslMode: verify-full
      database: ""
      sslKeySecret:
        name: ""
        key: ""
      sslCertSecret:
        name: ""
        key: ""
      sslRootCertSecret:
        name: ""
        key: ""
      passwordSecret:
        # -- Whether to create a secret for the password
        create: false
        name: ""
        key: ""
        # -- The password value to use when creating the secret
        value: ""
##
# Database management configuration
databases: []
 # - name: paradedb                 # -- Name of the database to be created.
 #   ensure: present                # -- Ensure the PostgreSQL database is present or absent - defaults to "present".
 #   owner: paradedb                # -- Owner of the database, defaults to the value of the `name` key.
 #   template: template1            # -- Maps to the TEMPLATE parameter.
 #   encoding: UTF8                 # -- Maps to the ENCODING parameter.
 #   connectionLimit: -1            # -- Maps to the CONNECTION LIMIT parameter. -1 (the default) means no limit.
 #   tablespace: ""                 # -- Maps to the TABLESPACE parameter and ALTER DATABASE.
 #   databaseReclaimPolicy: retain  # -- One of: retain / delete (retain by default).
 #   schemas: []                    # -- List of schemas to be created in the database.
 #    # - name: myschema
 #    #   owner: paradedb           # -- Owner of the schema, defaults to the database owner.
 #    #   ensure: present           # -- Ensure the PostgreSQL schema is present or absent - defaults to "present".
 #   extensions: []                 # -- List of extensions to be created in the database.
 #    # - name: pg_search
 #    #   ensure: present           # -- Ensure the PostgreSQL extension is present or absent - defaults to "present".
 #    #   version: "0.22.3"         # -- Version of the extension to be installed, if not specified the latest version will be used.
 #    #   schema: ""                # -- Schema where the extension will be installed, if not specified the extensions or current default object creation schema will be used.
 #   isTemplate: false              # -- Maps to the IS_TEMPLATE parameter. If true, the database is considered a template for new databases.
 #   locale: ""                     # -- Maps to the LC_COLLATE and LC_CTYPE parameters
 #   localeProvider: ""             # -- Maps to the LOCALE_PROVIDER parameter. Available from PostgreSQL 16.
 #   localeCollate: ""              # -- Maps to the LC_COLLATE parameter
 #   localeCType: ""                # -- Maps to the LC_CTYPE parameter
 #   icuLocale: ""                  # -- Maps to the ICU_LOCALE parameter. Available from PostgreSQL 15.
 #   icuRules: ""                   # -- Maps to the ICU_RULES parameter. Available from PostgreSQL 16.
 #   builtinLocale: ""              # -- Maps to the BUILTIN_LOCALE parameter. Available from PostgreSQL 17.
 #   collationVersion: ""           # -- Maps to the COLLATION_VERSION parameter.

imageCatalog:
  # -- Whether to provision an image catalog. If imageCatalog.images is empty this option will be ignored.
  create: true
  # -- List of images to be provisioned in an image catalog.
  images: []
    # - image: ghcr.io/your_repo/your_image:your_tag
    #   major: 18

# -- List of PgBouncer poolers
poolers: []
  # -
  #   # -- Pooler name
  #   name: rw
  #   # -- PgBouncer type of service to forward traffic to.
  #   type: rw
  #   # -- PgBouncer pooling mode
  #   poolMode: transaction
  #   # -- Number of PgBouncer instances
  #   instances: 3
  #   # -- PgBouncer configuration parameters
  #   parameters:
  #     max_client_conn: "1000"
  #     default_pool_size: "25"
  #   monitoring:
  #     # -- Whether to enable monitoring
  #     enabled: false
  #     podMonitor:
  #         # -- Whether to enable the PodMonitor
  #       enabled: true
  #       # -- Additional labels to set on the generated PodMonitor resource.
  #       # Add labels your monitoring stack requires (for example `team-name`).
  #       labels: {}
  #       # --The list of relabelings for the PodMonitor.
  #       # Applied to samples before scraping.
  #       relabelings: []
  #       # -- The list of metric relabelings for the PodMonitor.
  #       # Applied to samples before ingestion.
  #       metricRelabelings: []
  #   # -- Custom PgBouncer deployment template.
  #   # Use to override image, specify resources, etc.
  #   template: {}
  # -
  #   # -- Pooler name
  #   name: ro
  #   # -- PgBouncer type of service to forward traffic to.
  #   type: ro
  #   # -- PgBouncer pooling mode
  #   poolMode: transaction
  #   # -- Number of PgBouncer instances
  #   instances: 3
  #   # -- PgBouncer configuration parameters
  #   parameters:
  #     max_client_conn: "1000"
  #     default_pool_size: "25"
  #   monitoring:
  #     # -- Whether to enable monitoring
  #     enabled: false
  #     podMonitor:
  #         # -- Whether to enable the PodMonitor
  #       enabled: true
  #       # -- Additional labels to set on the generated PodMonitor resource.
  #       # Add labels your monitoring stack requires (for example `team-name`).
  #       labels: {}
  #       # --The list of relabelings for the PodMonitor.
  #       # Applied to samples before scraping.
  #       relabelings: []
  #       # -- The list of metric relabelings for the PodMonitor.
  #       # Applied to samples before ingestion.
  #       metricRelabelings: []
  #   # -- Custom PgBouncer deployment template.
  #   # Use to override image, specify resources, etc.
  #   template: {}

monitoring:
  grafanaDashboard:
    create: false
    # -- Allows overriding the namespace where the ConfigMap will be created, defaulting to the same one as the Release.
    namespace: ""
    # -- The name of the ConfigMap containing the dashboard.
    configMapName: "paradedb-grafana-dashboard"
    # -- Labels that ConfigMaps should have to get configured in Grafana.
    labels:
      grafana_dashboard: "1"
    # -- Annotations that ConfigMaps can have to get configured in Grafana.
    annotations: {}

```

## File: charts\paradedb\docs\getting_started.md
```
# Getting Started

The CNPG cluster chart follows a convention over configuration approach. This means that the chart will create a reasonable
CNPG setup with sensible defaults. However, you can override these defaults to create a more customized setup. Note that
you still need to configure backups and monitoring separately. The chart will not install a Prometheus stack for you.

_**Note**_ that this is an opinionated chart. It does not support all configuration options that CNPG supports. If you
need a highly customized setup, you should manage your cluster via a Kubernetes CNPG cluster manifest instead of this chart.
Refer to the [CNPG documentation](https://cloudnative-pg.io/documentation/current/) in that case.

## Installing the operator

To begin, make sure you install the CNPG operator in your cluster. It can be installed via a Helm chart as shown below or
it can be installed via a Kubernetes manifest. For more information see the [CNPG documentation](https://cloudnative-pg.io/documentation/current/installation_upgrade/).

```console
helm repo add cnpg https://cloudnative-pg.github.io/charts
helm upgrade --install cnpg \
  --namespace cnpg-system \
  --create-namespace \
  cnpg/cloudnative-pg
```

## Creating a cluster configuration

Once you have the operator installed, the next step is to prepare the cluster configuration. Whether this will be managed
via a GitOps solution or directly via Helm is up to you. The following sections outline the important steps in both cases.

### Choosing the database type

Currently the chart supports two database types. These are configured via the `type` parameter. These are:
* `postgresql` - A standard PostgreSQL database.
* `paradedb` - Postgres for Search and Analytics.

Depending on the type the chart will use a different Docker image and fill in some initial setup, like extension installation.

### Choosing the mode of operation

The chart has three modes of operation. These are configured via the `mode` parameter. If this is your first cluster, you
are likely looking for the `standalone` option.
* `standalone` - Creates new or updates an existing CNPG cluster. This is the default mode.
* `replica` - Creates a replica cluster from an existing CNPG cluster.
* `recovery` - Recovers a CNPG cluster from a backup, object store or via pg_basebackup.

### Backup configuration

Most importantly you should configure your backup storage.

CNPG implements disaster recovery via [Barman](https://pgbarman.org/). The following section configures the barman object
store where backups will be stored. Barman performs backups of the cluster filesystem base backup and WALs. Both are
stored in the specified location. The backup provider is configured via the `backups.provider` parameter. The following
providers are supported:

* S3 or S3-compatible stores, like MinIO
* Microsoft Azure Blob Storage
* Google Cloud Storage

Additionally you can specify the following parameters:
* `backups.retentionPolicy` - The retention policy for backups. Defaults to `30d`.
* `backups.scheduledBackups` - An array of scheduled backups containing a name and a crontab schedule. Example:
  ```yaml
  backups:
    scheduledBackups:
      - name: daily-backup
        schedule: "0 0 0 * * *" # Daily at midnight
        backupOwnerReference: self
  ```

Each backup adapter takes its own set of parameters, listed in the [Configuration options](../README.md#Configuration-options)
section. Refer to the table for the full list of parameters and place the configuration under the appropriate key: `backups.s3`,
`backups.azure`, or `backups.google`.

### Cluster configuration

There are several important cluster options. Here are the most important ones:

`cluster.instances` - The number of instances in the cluster. Defaults to `1`, but you should set this to `3` for production.
`cluster.imageName` - This allows you to override the Docker image used for the cluster. The chart will choose a default
  for you based on the setting you chose for `type`. If you need to run a configuration that is not supported, you can
  create your own Docker image. You can use the [postgres-containers](https://github.com/cloudnative-pg/postgres-containers)
  repository for a starting point.
  You will likely need to set your own repository access credentials via: `cluster.imagePullPolicy` and `cluster.imagePullSecrets`.
`cluster.storage.size` - The size of the persistent volume claim for the cluster. Defaults to `8Gi`. Every instance will
  have its own persistent volume claim.
`cluster.storage.storageClass` - The storage class to use for the persistent volume claim.
`cluster.resources` - The resource limits and requests for the cluster. You are strongly advised to use the same values
  for both limits and requests to ensure a [Guaranteed QoS](https://kubernetes.io/docs/concepts/workloads/pods/pod-qos/#guaranteed).
`cluster.affinity.topologyKey` - The chart sets it to `topology.kubernetes.io/zone` by default which is useful if you are
  running a production cluster in a multi AZ cluster (highly recommended). If you are running a single AZ cluster, you may
  want to change that to `kubernetes.io/hostname` to ensure that cluster instances are not provisioned on the same node.
`cluster.postgresql.parameters` - Allows you to override PostgreSQL configuration parameters, for example:
  ```yaml
  cluster:
    postgresql:
      parameters:
        max_connections: "200"
        shared_buffers: "2GB"
  ```
`cluster.initdb.postInitSQL` - Allows you to run custom SQL queries during cluster initialization. This is useful for creating
extensions, schemas, and databases. Use `cluster.initdb.postInitApplicationSQL` and `cluster.initdb.postInitTemplateSQL` when
you need application-database or template-database specific initialization.

For a full list - refer to the Helm chart [configuration options](../README.md#Configuration-options).

## Examples

There are several configuration examples in the [examples](../examples) directory. Refer to them for a basic setup and
refer to the [CloudNativePG Documentation](https://cloudnative-pg.io/documentation/current/) for more advanced configurations.

```

## File: charts\paradedb\docs\long_running_tasks.md
```
# Executing Long-running Tasks

By setting `cluster.console.enabled=true`, the chart deploys a StatefulSet with a console pod for executing long-running tasks. This is useful for tasks that need to run in the background or for batch processing, such as `CREATE INDEX`. The intent is to use this console pod to run commands in the background without maintaining a persistent client connection. Because the console pod is on the cluster, it is less susceptible to network issues.

> [!NOTE]
> We don't provision a PodDisruption Budget (PDB) for the console StatefulSet. Node maintenance or other disruptions may cause the console pod to be evicted, killing your session.
>
> The console pod has `root` access so that you can use `apt install` to install any additional tools you may need. Keep in mind that while the root user home folder (`/root`) is persisted, any tools you install will not be persisted if the pod restarts.
>
> All the utilities in the pod are installed during the pod startup, so it may take a few seconds before they become available, after the pod has restarted.

## Connecting to the Console Pod

To use the console pod, you can run the following command:

```bash
kubectl --namespace <namespace> exec --stdin --tty statefulset/<cluster-name>-console -- bash
```

## Database credentials

We provide the database credentials as environment variables in the console pod. You can access them using:

* `$DB_APP_URI` - Connection URI for the default application user.
* `$DB_SUPERUSER_URI` - Connection URI for the `postgres` superuser.

## Executing queries

To run a command in the background you can use the `nohup` command. For example, to create an index in the background:

```bash
nohup psql "$DB_SUPERUSER_URI/<db-name>" -c "CREATE INDEX orders_idx ON orders USING bm25 (order_id, customer_name) WITH (key_field='order_id');" 2>&1 > command.log &
```

To check on the status of the command, you can use the `tail` command:

```bash
tail -f command.log
```

## Advanced usage with `screen`

You can also use the `screen` utility to run commands in the background and keep them running even if you disconnect from the console pod. Here are some basic commands to get you started:

* Start a new screen session

```bash
screen -S mysession
```

* List all screen sessions

```bash
screen -list
```

* To detach from a screen session without stopping it, press `Ctrl + A`, then `D`.
* You can reattach to a screen session with:

```bash
screen -r mysession
```

```

## File: charts\paradedb\docs\recovery.md
```
# Recovery

This chart can be used to initiate a recovery operation of a CNPG cluster no matter if it was created with the chart or not.

CNPG does not support recovery in-place. Instead you need to create a new cluster that will be bootstrapped from the existing one or from a backup.

You can find more information about the recovery process in the [CNPG documentation](https://cloudnative-pg.io/documentation/current/backup_recovery).

There are 3 types of recovery possible with CNPG:

* Recovery from a backup object in the same Kubernetes namespace.
* Recovery from a Barman Object Store, that could be located anywhere.
* Streaming replication from an operating cluster using `pg_basebackup`.

When performing a recovery you are strongly advised to use the same configuration and PostgreSQL version as the original cluster.

To begin, create a `values.yaml` that contains the following:

1. Set `mode: recovery` to indicate that you want to bootstrap the new cluster from an existing one.
2. Set the `recovery.method` to the type of recovery you want to perform.
3. Set either the `recovery.backupName` or the Barman Object Store configuration - i.e. `recovery.provider` and appropriate S3, Azure or GCS configuration. In case of `pg_basebackup` complete the `recovery.pgBaseBackup` section.
4. Optionally set the `recovery.pitrTarget.time` in RFC3339 format to perform a point-in-time recovery (not applicable for `pgBaseBackup`).
5. Retain the identical PostgreSQL version and configuration as the original cluster.
6. Make sure you don't use the same backup section name as the original cluster. We advise you change the `path` within the storage location if you want to reuse the same storage location/bucket.
    One pattern is adding a version number at the end of the path, e.g. `/v1` or `/v2` after each recovery procedure.

Example recovery configurations can be found in the [examples](../examples) directory.

```

## File: charts\paradedb\docs\runbooks\cnpgclusterhacritical.md
```
# CNPGClusterHACritical

## Description

The `CNPGClusterHACritical` alert is triggered when the CloudNativePG cluster has no ready standby replicas.

This alert may occur during a regular failover or a planned automated version upgrade on two-instance clusters, as there is a brief period when only the primary remains active while a failover completes.

On single-instance clusters, this alert will remain active at all times. If running with a single instance is intentional, consider silencing the alert.

## Impact

Without standby replicas, the cluster will incur downtime if the primary fails. While the primary instance remains online and able to serve queries, connections through the `-ro` endpoint will fail.

## Diagnosis

Identify the current primary instance using the [CloudNativePG Grafana Dashboard](https://grafana.com/grafana/dashboards/20417-cloudnativepg/) or by running:

```bash
kubectl get cluster paradedb -o 'jsonpath={"Current Primary: "}{.status.currentPrimary}{"; Target Primary: "}{.status.targetPrimary}{"\n"}' --namespace <namespace>
```

Since the primary is the only instance serving queries, avoid making any changes that could disrupt it.

To inspect cluster health and instance status:

- Get the status of the CloudNativePG cluster instances:

```bash
kubectl get pods -A -l "cnpg.io/podRole=instance" -o wide
```

- If any pods are Pending, describe them to identify the cause:

```bash
kubectl describe --namespace <namespace> pod/<pod-name>
```

- Inspect the cluster phase and reason:

```bash
kubectl get cluster paradedb -o 'jsonpath={.status.phase}{"\n"}{.status.phaseReason}{"\n"}' --namespace <namespace>
```

- Inspect the logs of the affected CloudNativePG instances:

```bash
kubectl logs --namespace <namespace> pod/<instance-pod-name>
```

- Inspect the CloudNativePG operator logs:

```bash
kubectl logs --namespace cnpg-system -l "app.kubernetes.io/name=cloudnative-pg"
```

## Mitigation

### Instance Failure

First, consult the [CloudNativePG Failure Modes](https://cloudnative-pg.io/documentation/current/failure_modes/) and [CloudNativePG Troubleshooting](https://cloudnative-pg.io/documentation/current/troubleshooting/) documentation for more information on the conditions when CloudNativePG is unable to heal instances and standard troubleshooting steps.

### Insufficient Storage

If the above diagnosis commands indicate that an instance’s storage or WAL disk is full, increase the cluster storage size. Refer to the CloudNativePG documentation for more information on how to [Resize the CloudNativePG Cluster Storage](https://cloudnative-pg.io/documentation/current/troubleshooting/#storage-is-full).

### Unknown

If the root cause remains unclear, recreating the affected pods can sometimes resolve the issue. Recreating a pod involves deleting the pod, its storage PVC, and its WAL storage PVC. This will trigger a full rebuild of the node from a base backup and can take several hours, depending on the size of the database. Note that pods should **always** be recreated one at a time to avoid increasing the load on the primary instance.

Before doing so, carefully verify that:

- You are connected to the correct cluster.
- You are deleting the correct pod.
- You are not deleting the active primary instance.

```bash
kubectl delete --namespace <namespace> pod/<pod-name> pvc/<pod-name> pvc/<pod-name>-wal
```

```

## File: charts\paradedb\docs\runbooks\cnpgclusterhawarning.md
```
# CNPGClusterHAWarning

## Description

The `CNPGClusterHAWarning` alert is triggered when the CloudNativePG cluster has fewer than two ready standby replicas.

This alert may occur during a regular failover or a planned automated version upgrade, as there is a brief period when only the primary remains active while a failover completes.

On single-instance or two-instance clusters, this alert will remain active at all times. If this is intentional, consider silencing the alert.

## Impact

With fewer than two standby replicas, the `-ro` endpoint is at risk of downtime if the last replica fails. The cluster will continue to function, but both the `-ro` and `-r` endpoints will operate with reduced capacity.

## Diagnosis

Identify the current primary instance using the [CloudNativePG Grafana Dashboard](https://grafana.com/grafana/dashboards/20417-cloudnativepg/) or by running:

```bash
kubectl get cluster paradedb -o 'jsonpath={"Current Primary: "}{.status.currentPrimary}{"; Target Primary: "}{.status.targetPrimary}{"\n"}' --namespace <namespace>
```

Since the primary is the only instance serving queries, avoid making any changes that could disrupt it.

To inspect cluster health and instance status:

- Get the status of the CloudNativePG cluster instances:

```bash
kubectl get pods -A -l "cnpg.io/podRole=instance" -o wide
```

- If any pods are Pending, describe them to identify the cause:

```bash
kubectl describe --namespace <namespace> pod/<pod-name>
```

- Inspect the cluster phase and reason:

```bash
kubectl get cluster paradedb -o 'jsonpath={.status.phase}{"\n"}{.status.phaseReason}{"\n"}' --namespace <namespace>
```

- Inspect the logs of the affected CloudNativePG instances:

```bash
kubectl logs --namespace <namespace> pod/<instance-pod-name>
```

- Inspect the CloudNativePG operator logs:

```bash
kubectl logs --namespace cnpg-system -l "app.kubernetes.io/name=cloudnative-pg"
```

## Mitigation

### Instance Failure

First, consult the [CloudNativePG Failure Modes](https://cloudnative-pg.io/documentation/current/failure_modes/) and [CloudNativePG Troubleshooting](https://cloudnative-pg.io/documentation/current/troubleshooting/) documentation for more information on the conditions when CloudNativePG is unable to heal instances and standard troubleshooting steps.

### Insufficient Storage

If the above diagnosis commands indicate that an instance’s storage or WAL disk is full, increase the cluster storage size. Refer to the CloudNativePG documentation for more information on how to [Resize the CloudNativePG Cluster Storage](https://cloudnative-pg.io/documentation/current/troubleshooting/#storage-is-full).

### Unknown

If the root cause remains unclear, recreating the affected pods can sometimes resolve the issue. Recreating a pod involves deleting the pod, its storage PVC, and its WAL storage PVC. This will trigger a full rebuild of the node from a base backup and can take several hours, depending on the size of the database. Note that pods should **always** be recreated one at a time to avoid increasing the load on the primary instance.

Before doing so, carefully verify that:

- You are connected to the correct cluster.
- You are deleting the correct pod.
- You are not deleting the active primary instance.

```bash
kubectl delete --namespace <namespace> pod/<pod-name> pvc/<pod-name> pvc/<pod-name>-wal
```

```

## File: charts\paradedb\docs\runbooks\cnpgclusterhighconnectionscritical.md
```
# CNPGClusterHighConnectionsCritical

## Description

The `CNPGClusterHighConnectionsCritical` alert is triggered when the number of connections on the CloudNativePG cluster instance exceeds 95% of its configured capacity.

## Impact

At 100% capacity, the instance will reject new connections, resulting in a service disruption.

## Diagnosis

Use the [CloudNativePG Grafana Dashboard](https://grafana.com/grafana/dashboards/20417-cloudnativepg/) to inspect the number of connections to the CloudNativePG cluster instances. Identify which instance is over capacity, and determine whether it is the primary or a standby replica.

You can check the current primary instance using the following command:

```bash
kubectl get cluster paradedb -o 'jsonpath={"Current Primary: "}{.status.currentPrimary}{"; Target Primary: "}{.status.targetPrimary}{"\n"}' --namespace <namespace>
```

## Mitigation

> [!IMPORTANT]
> Changing the `max_connections` parameter requires a restart of the CloudNativePG cluster instances. This will cause a restart of a standby instance and a switchover of the primary instance, causing a brief service disruption.

- Increase the maximum number of connections by setting the `max_connections` PostgreSQL parameter:
  - Helm: `cluster.postgresql.parameters.max_connections`

- Use connection pooling by enabling PgBouncer to reduce the number of connections to the database. PgBouncer itself requires connections, so temporarily increase `max_connections` while enabling it to avoid service disruption.

> [!NOTE]
> PostgreSQL sizes certain resources directly based on the value of `max_connections`. Each connection uses a portion of the `shared_buffers` memory as well as additional non-shared memory. As a result, increasing the `max_connections` parameter will increase the memory usage of the CloudNativePG cluster instances.

```

## File: charts\paradedb\docs\runbooks\cnpgclusterhighconnectionswarning.md
```
# CNPGClusterHighConnectionsWarning

## Description

The `CNPGClusterHighConnectionsWarning` alert is triggered when the number of connections on the CloudNativePG cluster instance exceeds 85% of its configured capacity.

## Impact

At 100% capacity, the instance will reject new connections, resulting in a service disruption.

## Diagnosis

Use the [CloudNativePG Grafana Dashboard](https://grafana.com/grafana/dashboards/20417-cloudnativepg/) to check the number of connections to the CloudNativePG cluster instances. Identify which instance is over capacity, and determine whether it is the primary or a standby replica.

You can check the current primary instance using the following command:

```bash
kubectl get cluster paradedb -o 'jsonpath={"Current Primary: "}{.status.currentPrimary}{"; Target Primary: "}{.status.targetPrimary}{"\n"}' --namespace <namespace>
```

## Mitigation

> [!IMPORTANT]
> Changing the `max_connections` parameter requires a restart of the CloudNativePG cluster instances. This will cause a restart of a standby instance and a switchover of the primary instance, causing a brief service disruption.

- Increase the maximum number of connections by setting the `max_connections` PostgreSQL parameter:
  - Helm: `cluster.postgresql.parameters.max_connections`

- Use connection pooling by enabling PgBouncer to reduce the number of connections to the database. PgBouncer itself requires connections, so temporarily increase `max_connections` while enabling it to avoid service disruption.

> [!NOTE]
> PostgreSQL sizes certain resources directly based on the value of `max_connections`. Each connection uses a portion of the `shared_buffers` memory as well as additional non-shared memory. As a result, increasing the `max_connections` parameter will increase the memory usage of the CloudNativePG cluster instances.

```

## File: charts\paradedb\docs\runbooks\cnpgclusterhighphysicalreplicationlagwarning.md
```
# CNPGClusterHighPhysicalReplicationLagWarning

## Description

The `CNPGClusterHighPhysicalReplicationLagWarning` alert is triggered when physical replication lag in the CloudNativePG cluster exceeds 1 second.

## Impact

High physical replication lag can cause the cluster replicas to become out of sync. Queries to the `-r` and `-ro` endpoints may return stale data. In the event of a failover, the data that has not yet been replicated from the primary to the replicas may be lost during failover.

## Diagnosis

Check replication status in the [CloudNativePG Grafana Dashboard](https://grafana.com/grafana/dashboards/20417-cloudnativepg/) or by running:

```bash
kubectl exec --namespace <namespace> --stdin --tty services/<cluster_name>-rw -- psql -c "SELECT * FROM pg_stat_replication;"
```

High physical replication lag can be caused by a number of factors, including:

- Network congestion on the node interface

Inspect the network interface statistics using the `Kubernetes Cluster` section of the [CloudNativePG Grafana Dashboard](https://grafana.com/grafana/dashboards/20417-cloudnativepg/).

- High CPU or memory load on primary or replicas

Inspect the CPU and Memory usage of the CloudNativePG cluster instances using the [CloudNativePG Grafana Dashboard](https://grafana.com/grafana/dashboards/20417-cloudnativepg/).

- Disk I/O bottlenecks on replicas

Inspect the disk IO statistics using the [CloudNativePG Grafana Dashboard](https://grafana.com/grafana/dashboards/20417-cloudnativepg/).

- Long-running queries

Inspect the `Stat Activity` section of the [CloudNativePG Grafana Dashboard](https://grafana.com/grafana/dashboards/20417-cloudnativepg/).

- Suboptimal PostgreSQL configuration, e.g. too few `max_wal_senders`. Set this to at least the number of cluster instances (default 10 is usually sufficient).

Inspect the `PostgreSQL Parameters` section of the [CloudNativePG Grafana Dashboard](https://grafana.com/grafana/dashboards/20417-cloudnativepg/).

## Mitigation

- Terminate long-running transactions that generate excessive changes.

```bash
kubectl exec -it services/cluster-rw --namespace <namespace> -- psql
```

- Increase the Memory and CPU resources of the instances under heavy load. This can be done by setting `cluster.resources.requests` and `cluster.resources.limits` in your Helm values. Set both `requests` and `limits` to the same value to achieve QoS Guaranteed. This will require a restart of the CloudNativePG cluster instances and a primary switchover, which will cause a brief service disruption.

- Enable `wal_compression` by setting the `cluster.postgresql.parameters.wal_compression` parameter to `on`. Doing so will reduce the size of the WAL files and can help reduce replication lag in a congested network. Changing `wal_compression` does not require a restart of the CloudNativePG cluster.

- Increase IOPS or throughput of the storage used by the cluster to alleviate disk I/O bottlenecks. This requires creating a new storage class with higher IOPS/throughput and rebuilding cluster instances and their PVCs one by one using the new storage class. This is a slow process that will also affect the cluster's availability.

If you decide to go this route:

1. Start by creating a new storage class. Storage classes are immutable, so you cannot change the storage class of existing Persistent Volume Claims (PVCs).

2. Make sure to only replace one instance at a time to avoid service disruption.

3. Double check you are deleting the correct pod.

4. Don't start with the active primary instance. Delete one of the standby replicas first.

```bash
kubectl delete --namespace <namespace> pod/<pod-name> pvc/<pod-name> pvc/<pod-name>-wal
```

- In the event that the cluster has 9+ instances, ensure that the `max_wal_senders` parameter is set to a value greater than or equal to the total number of instances in your cluster.

```

## File: charts\paradedb\docs\runbooks\cnpgclusterinstancesonsamenode.md
```
# CNPGClusterInstancesOnSameNode

## Description

The `CNPGClusterInstancesOnSameNode` alert is triggered when two or more database pods are scheduled on the same node. This is unexpected for CloudNativePG clusters, as each instance should run on a separate node to ensure high availability and fault tolerance.

This can be caused by insufficient nodes in the cluster or misconfigured scheduling rules, such as pod affinity/anti-affinity rules or tolerations.

## Impact

This configuration reduces high availability, as a node failure hosting multiple database pods will cause all of them to go down simultaneously.

## Diagnosis

To investigate node placement of database pods:

- List all database pods and their node assignments:

```bash
kubectl get pods -A -l "cnpg.io/podRole=instance" -o json | jq -r '["Namespace", "Pod", "Node"], ( .items[] | [.metadata.namespace, .metadata.name, .spec.nodeName]) | @tsv' | column -t
```

- Describe the cluster and check the affinity and tolerations configuration:

```bash
kubectl describe --namespace <namespace> clusters.postgresql.cnpg.io/paradedb
```

- Describe the pods:

```bash
kubectl describe pods -A -l "cnpg.io/podRole=instance"
```

## Mitigation

- Verify that you have more than a single node with no taint preventing pods from being scheduled on these nodes.

- Verify your [affinity](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/), taints, and tolerations configuration.

- Increase the instance CPU and Memory resources so that no node can host more than one instance.

For more information, please refer to the ["Scheduling"](https://cloudnative-pg.io/documentation/current/scheduling/) section of the documentation.

```

## File: charts\paradedb\docs\runbooks\cnpgclusterlogicalreplicationerrors.md
```
# CNPGClusterLogicalReplicationErrors

## Description

The `CNPGClusterLogicalReplicationErrors` alert indicates that a logical replication subscription is experiencing errors during data replication. This includes:

1. **Apply Errors**: Errors that occur when applying received changes from the publisher
2. **Sync Errors**: Errors that occur during the initial table synchronization phase

- **Warning level**: Any error detected in the last 5 minutes
- **Critical level**: 5 or more errors in the last 5 minutes

## Impact

- **Data Inconsistency**: The subscriber may have missing or incorrect data
- **Replication Paused**: Depending on configuration, replication might stop on errors
- **Growing Lag**: Errors can cause replication to fall behind
- **Critical**: Persistent errors may lead to complete replication failure

## Diagnosis

### Step 1: Check Error Details

```bash
# Connect to the subscriber and check subscription status
kubectl exec -it svc/SUBSCRIBER-CLUSTER-rw -n NAMESPACE -- psql -c "
SELECT
    s.subname,
    s.subenabled,
    COALESCE(sss.apply_error_count, 0) AS apply_error_count,
    COALESCE(sss.sync_error_count, 0) AS sync_error_count,
    sss.stats_reset
FROM pg_subscription s
LEFT JOIN pg_stat_subscription_stats sss ON s.oid = sss.subid
WHERE COALESCE(sss.apply_error_count, 0) > 0 OR COALESCE(sss.sync_error_count, 0) > 0;
"

# Check the last error message
kubectl exec -it svc/SUBSCRIBER-CLUSTER-rw -n NAMESPACE -- psql -c "
SELECT
    s.subname,
    ss.last_msg_receipt_time,
    ss.latest_end_time,
    CASE
        WHEN COALESCE(sss.apply_error_count, 0) > 0 THEN 'Apply errors detected'
        WHEN COALESCE(sss.sync_error_count, 0) > 0 THEN 'Sync errors detected'
        ELSE 'No errors detected'
    END as error_type
FROM pg_subscription s
LEFT JOIN pg_stat_subscription ss ON s.oid = ss.subid
LEFT JOIN pg_stat_subscription_stats sss ON s.oid = sss.subid;
"
```

### Step 2: Check PostgreSQL Logs

```bash
# Get the pod name
POD=$(kubectl get pods -n NAMESPACE -l app=postgresql -o name | head -1 | cut -d/ -f2)

# Check recent logs for errors
kubectl logs -n NAMESPACE $POD --tail=100 | grep -i "replication\|subscription\|error"

# Stream logs for real-time monitoring
kubectl logs -n NAMESPACE $POD -f | grep -i "replication\|subscription\|error"
```

### Step 3: Identify Common Error Patterns

1. **Constraint Violations**:
   ```bash
   kubectl logs -n NAMESPACE $POD | grep "violates.*constraint"
   ```

2. **Permission Issues**:
   ```bash
   kubectl logs -n NAMESPACE $POD | grep "permission denied\|role"
   ```

3. **Data Type Mismatches**:
   ```bash
   kubectl logs -n NAMESPACE $POD | grep "invalid input syntax\|datatype"
   ```

4. **Connection Issues**:
   ```bash
   kubectl logs -n NAMESPACE $POD | grep "connection\|timeout"
   ```

### Step 4: Verify Publication/Subscription Configuration

```bash
# On publisher - check publication tables
kubectl exec -it svc/PUBLISHER-CLUSTER-rw -n NAMESPACE -- psql -c "
SELECT pubname, puballtables, pubinsert, pubupdate, pubdelete
FROM pg_publication;
"

# On subscriber - check subscription details
kubectl exec -it svc/SUBSCRIBER-CLUSTER-rw -n NAMESPACE -- psql -c "
SELECT
    subname,
    subconninfo,
    subslotname,
    subsynccommit,
    subpublications
FROM pg_subscription;
"

# Check which tables are being replicated
kubectl exec -it svc/SUBSCRIBER-CLUSTER-rw -n NAMESPACE -- psql -c "
SELECT
    sr.srrelid::regclass as table_name,
    sr.srsubstate as state
FROM pg_subscription_rel sr
JOIN pg_class c ON sr.srrelid = c.oid
WHERE sr.srsubstate NOT IN ('r', 's');  -- Not ready or synchronizing
"
```

### Step 5: Check for Data Conflicts

```bash
# Check for conflicting primary keys
kubectl exec -it svc/SUBSCRIBER-CLUSTER-rw -n NAMESPACE -- psql -c "
SELECT schemaname, tablename, attname, n_distinct, correlation
FROM pg_stats
WHERE schemaname NOT IN ('pg_catalog', 'information_schema')
ORDER BY schemaname, tablename;
"
```

## Resolution

### For Constraint Violations

1. **Identify the Constraint**:
   ```sql
   -- Find the violated constraint
   SELECT conname, contype, pg_get_constraintdef(oid)
   FROM pg_constraint
   WHERE conrelid = 'table_name'::regclass;
   ```

2. **Resolve Data Conflicts**:
   ```sql
   -- Option 1: Remove conflicting data on subscriber
   DELETE FROM table_name WHERE id = conflicting_id;

   -- Option 2: Update conflicting data
   UPDATE table_name
   SET conflicting_column = new_value
   WHERE id = conflicting_id;

   -- Option 3: Temporarily disable constraint (use with caution)
   ALTER TABLE table_name DISABLE TRIGGER ALL;
   -- After sync, re-enable
   ALTER TABLE table_name ENABLE TRIGGER ALL;
   ```

### For Permission Issues

1. **Check Subscription Owner**:
   ```sql
   SELECT usename, usesuper, usecreatedb
   FROM pg_user
   WHERE usename = current_user;
   ```

2. **Grant Necessary Permissions**:
   ```sql
   -- On subscriber, ensure subscription owner has rights
   GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO subscription_user;
   GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO subscription_user;
   ```

### For Data Type Mismatches

1. **Verify Schema Consistency**:
   ```sql
   -- On publisher
   \d+ table_name

   -- On subscriber
   \d+ table_name

   -- Compare columns and types
   SELECT column_name, data_type, is_nullable
   FROM information_schema.columns
   WHERE table_name = 'table_name';
   ```

2. **Fix Schema Issues**:
   ```sql
   -- Alter table to match publisher schema
   ALTER TABLE table_name ALTER COLUMN column_name TYPE new_type;
   ```

### For Initial Sync Errors

1. **Check if Tables Exist**:
   ```sql
   -- On subscriber, ensure tables exist
   SELECT tablename FROM pg_tables WHERE schemaname = 'public';
   ```

2. **Create Missing Tables**:
   ```sql
   -- Export schema from publisher
   pg_dump -h PUBLISHER-HOST -U postgres -s -t table_name database_name

   -- Import into subscriber
   psql -h SUBSCRIBER-HOST -U postgres -d database_name < schema_dump.sql
   ```

3. **Reset Subscription**:
   ```bash
   # WARNING: This will resync all data
   kubectl cnpg subscription restart SUBSCRIPTION-NAME -n NAMESPACE

   # Or completely recreate
   kubectl cnpg subscription delete SUBSCRIPTION-NAME -n NAMESPACE
   # Recreate with proper configuration
   ```

### For Connection/Timeout Issues

1. **Check Connectivity**:
   ```bash
   # Test connection from subscriber to publisher
   kubectl exec -it svc/SUBSCRIBER-CLUSTER-rw -n NAMESPACE -- \
     psql -h PUBLISHER-HOST -U postgres -d database_name -c "SELECT 1;"
   ```

2. **Increase Timeout Values**:
   ```yaml
   # In subscription configuration
   spec:
     parameters:
       application_name: "my_subscription"
       synchronous_commit: "off"
       # Increase timeout for slow networks
   ```

## Recovery Procedures

Choose one of the following approaches based on your situation:

### Option 1: Resolve Data Conflict (Recommended - Lets Replication Retry Automatically)

**When to use**: When you have a specific constraint violation (e.g., duplicate key) and want to let the publisher's data replicate correctly.

The most common cause of replication errors is conflicting data between publisher and subscriber. PostgreSQL's logical replication **stops** when it encounters a conflict and requires manual intervention.

#### Step 1: Identify the conflicting data

Check the PostgreSQL logs for the conflict details:

```bash
kubectl logs -n NAMESPACE $POD | grep "conflict detected\|duplicate key"
```

You'll see something like:
```
ERROR: duplicate key value violates unique constraint "test_pkey"
DETAIL: Key (c)=(1) already exists.
CONTEXT: processing remote data for replication origin "pg_16395" during "INSERT" 
for replication target relation "public.test" in transaction 725 finished at 0/14C0378
```

This tells you which table and key is causing the conflict.

#### Step 2: Remove or fix the conflicting row on the subscriber

```sql
-- For INSERT conflicts: Delete the conflicting row to let publisher's data replicate
DELETE FROM table_name WHERE id = conflicting_id;
```

**That's it!** Once you remove the conflicting row, logical replication will **automatically retry** the transaction and apply the publisher's data. You do NOT need to manually skip the transaction.

**Important**: Only delete the subscriber's data if you're certain the publisher's version should win.

### Option 2: Skip Transaction Without Applying Publisher's Data (Use With Caution)

**When to use**: When you want to keep the subscriber's version of the data and permanently ignore what the publisher tried to send. This causes data divergence.

If you've decided that the subscriber's conflicting data is correct and you want to ignore the publisher's transaction:

```sql
-- Using ALTER SUBSCRIPTION SKIP
-- The subscription must be enabled for this to work
ALTER SUBSCRIPTION your_subscription SKIP (lsn = '0/14C0378');
```

**WARNING**: This permanently skips the transaction and causes the subscriber to differ from the publisher. Document what was skipped.

### Option 3: Full Resynchronization (For Multiple Conflicts or Unknown State)

**When to use**: When you have many conflicts, corrupted data, or prefer to start fresh rather than manually fixing individual rows.

**WARNING**: This will re-copy all table data and may take a long time for large tables.

```bash
# Mark subscription for full refresh
kubectl exec -it svc/SUBSCRIBER-CLUSTER-rw -n NAMESPACE -- psql -c "
ALTER SUBSCRIPTION your_subscription REFRESH PUBLICATION WITH (copy_data = true);
"

# Or restart the subscription
kubectl cnpg subscription restart your_subscription -n NAMESPACE
```

## Important Notes

- **PostgreSQL logical replication automatically retries after you fix the conflict** - Just delete or fix the conflicting row, and replication will resume on its own
- **Only use SKIP if you want to ignore the publisher's data** - Skipping means you're choosing to keep the subscriber's version and create data divergence
- **For typical constraint violations** - Delete the subscriber's conflicting row (Option 1), don't skip the transaction

## Prevention

1. **Schema Changes**:
   - Always test schema changes in staging first
   - Use DDL replication tools or manually sync schemas
   - Coordinate schema changes between publisher and subscriber

2. **Data Validation**:
   ```sql
   -- Regular data consistency checks
   SELECT COUNT(*) FROM table_name;
   -- Compare counts between publisher and subscriber
   ```

3. **Monitoring**:
   - Set up alerts for error rates
   - Monitor pg_stat_subscription regularly
   - Log error details for faster troubleshooting

4. **Best Practices**:
   - Don't modify subscriber data directly (unless bidirectional replication)
   - Use consistent character sets and collations
   - Ensure sufficient disk space for WAL retention

## Common Error Scenarios

### Primary Key Conflicts
```sql
-- Find duplicates
SELECT id, COUNT(*)
FROM table_name
GROUP BY id
HAVING COUNT(*) > 1;

-- Resolve by updating or removing duplicates
```

### Missing Sequences
```sql
-- Check sequence ownership
SELECT relname, seqrelid::regclass
FROM pg_depend
WHERE refobjid = 'table_name'::regclass
  AND deptype = 'a';

-- Sync sequence values
SELECT setval('sequence_name', (SELECT max(id) FROM table_name));
```

### Trigger Conflicts
```sql
-- Disable problematic triggers during sync
ALTER TABLE table_name DISABLE TRIGGER trigger_name;

-- Re-enable after sync
ALTER TABLE table_name ENABLE TRIGGER trigger_name;
```

## When to Escalate

- Contact support if:
  - Errors persist after all troubleshooting steps
  - You encounter frequent constraint violations
  - The schema cannot be synchronized
  - You need to skip transactions repeatedly
  - Error rate is increasing despite fixes

```

## File: charts\paradedb\docs\runbooks\cnpgclusterlogicalreplicationlagging.md
```
# CNPGClusterLogicalReplicationLagging

## Description

The `CNPGClusterLogicalReplicationLagging` alert indicates that a CloudNativePG cluster with a logical replication subscription is falling behind its publisher. This alert aggregates three types of lag:

1. **Receipt Lag** (`cnpg_pg_stat_subscription_receipt_lag_seconds`): Time since the last WAL message was received from the publisher
2. **Apply Lag** (`cnpg_pg_stat_subscription_apply_lag_seconds`): Time delay between receiving and actually applying changes
3. **LSN Distance** (`cnpg_pg_stat_subscription_buffered_lag_bytes`): Amount of WAL data buffered but not yet applied (measured in bytes)

- **Warning level**: Any lag metric exceeds 60s or 1GB
- **Critical level**: Any lag metric exceeds 300s or 4GB

## Impact

The cluster remains operational, but:
- Queries to the subscriber will return stale data
- Data inconsistency between publisher and subscriber
- In critical cases, disk space on the publisher may fill up with unapplied WAL
- Recovery time increases with lag duration

## Diagnosis

### Step 1: Identify the Lag Type

Connect to the subscriber and check the current state:

```bash
kubectl exec -it svc/SUBSCRIBER-CLUSTER-rw -n NAMESPACE -- psql -c "
SELECT
    s.subname,
    s.subenabled AS enabled,
    EXTRACT(EPOCH FROM (NOW() - ss.last_msg_receipt_time)) AS receipt_lag_seconds,
    EXTRACT(EPOCH FROM (NOW() - ss.latest_end_time)) AS apply_lag_seconds,
    COALESCE(pg_wal_lsn_diff(ss.received_lsn, ss.latest_end_lsn), 0) AS pending_bytes,
    CASE
        WHEN EXTRACT(EPOCH FROM (NOW() - ss.last_msg_receipt_time)) > 60 THEN 'High receipt lag'
        WHEN EXTRACT(EPOCH FROM (NOW() - ss.latest_end_time)) > 60 THEN 'High apply lag'
        WHEN COALESCE(pg_wal_lsn_diff(ss.received_lsn, ss.latest_end_lsn), 0) > 1024^3 THEN 'High LSN distance'
        ELSE 'Healthy'
    END as primary_issue
FROM pg_subscription s
LEFT JOIN pg_stat_subscription ss ON s.oid = ss.subid;
"
```

### Step 2: Check Network Connectivity

For **receipt lag** issues:

```bash
# Check network latency between publisher and subscriber
kubectl exec -it svc/SUBSCRIBER-CLUSTER-rw -n NAMESPACE -- \
  ping -c 10 PUBLISHER-HOSTNAME

# Check bandwidth (if tools are available)
kubectl exec -it svc/SUBSCRIBER-CLUSTER-rw -n NAMESPACE -- \
  nc -zv PUBLISHER-HOSTNAME 5432
```

### Step 3: Check Resource Utilization

For **apply lag** issues:

```bash
# Check CPU/Memory usage on subscriber
kubectl top pod -n NAMESPACE -l app=postgresql

# Check disk I/O
kubectl exec -it svc/SUBSCRIBER-CLUSTER-rw -n NAMESPACE -- \
  iostat -x 1 5

# Check for long-running queries
kubectl exec -it svc/SUBSCRIBER-CLUSTER-rw -n NAMESPACE -- psql -c "
SELECT pid, now() - pg_stat_activity.query_start AS duration, query
FROM pg_stat_activity
WHERE state = 'active' AND now() - query_start > interval '5 minutes'
ORDER BY duration DESC;
"
```

### Step 4: Check Configuration

```bash
# Verify replication worker settings
kubectl exec -it svc/SUBSCRIBER-CLUSTER-rw -n NAMESPACE -- psql -c "
SHOW max_worker_processes;
SHOW max_logical_replication_workers;
SHOW max_parallel_workers;
"

# Ensure adequate worker processes:
# max_worker_processes >= max_parallel_workers + max_logical_replication_workers
```

### Step 5: Monitor Trends

Use the CloudNativePG Grafana Dashboard:
- Navigate to the Logical Replication section
- Examine all lag graphs over time
- Check if lag is stable, increasing, or fluctuating
- Correlate with workload spikes

## Resolution

### For Receipt Lag (Network Issues)

1. **Check Network Latency**:
   - Verify network connectivity between clusters
   - Consider placing clusters in the same region/availability zone
   - Check for network congestion or throttling

2. **Optimize Network Configuration**:
   ```yaml
   # In the subscriber's postgresql configuration
   postgresql:
     parameters:
       wal_sender_timeout: '60s'
       wal_receiver_status_interval: '10s'
   ```

### For Apply Lag (Resource Issues)

1. **Scale Up Resources**:
   ```yaml
   # Increase CPU/memory for the subscriber
   resources:
     requests:
       cpu: 2
       memory: 8Gi
     limits:
       cpu: 4
       memory: 16Gi
   ```

2. **Optimize Disk I/O**:
   - Use faster storage (SSD if not already)
   - Consider increasing storage IOPS
   - Check for disk bottlenecks

3. **Tune PostgreSQL Settings**:
   ```yaml
   postgresql:
     parameters:
       # Increase for better write performance
       wal_buffers: '16MB'
       checkpoint_completion_target: 0.9
       # Reduce checkpoint frequency
       max_wal_size: '4GB'
       min_wal_size: '1GB'
   ```

### For High Transaction Volume

1. **Batch Large Transactions**:
   - Break large transactions into smaller ones
   - Use `COPY` instead of many INSERT statements

2. **Consider Row Filtering**:
   ```sql
   -- Only replicate needed data
   ALTER PUBLICATION publication_name SET (publish = 'insert, update, delete');
   ALTER PUBLICATION publication_name ADD TABLE table_name WHERE (condition);
   ```

3. **Temporarily Disable Triggers**:
   ```sql
   -- On subscriber for performance-critical periods
   ALTER TABLE table_name DISABLE TRIGGER ALL;
   -- Remember to re-enable after
   ```

### General Tuning

1. **Increase Replication Slots**:
   ```yaml
   # If multiple publications
   postgresql:
     parameters:
       max_replication_slots: 10
       max_wal_senders: 10
   ```

2. **Monitor and Restart**:
   ```bash
   # If subscriber is stuck
   kubectl cnpg subscription restart SUBSCRIPTION-NAME -n NAMESPACE

   # Or restart the entire cluster
   kubectl cnpg restart SUBSCRIBER-CLUSTER -n NAMESPACE
   ```

## Prevention

1. **Right-size Resources**:
   - Allocate adequate CPU, memory, and storage IOPS
   - Monitor resource utilization regularly

2. **Network Optimization**:
   - Place publisher and subscriber close to each other
   - Use dedicated network connections if possible

3. **Regular Monitoring**:
   - Set up proactive monitoring before issues become critical
   - Review lag trends regularly
   - Set up automated scaling based on metrics

4. **Maintenance Windows**:
   - Schedule large data operations during low-traffic periods
   - Consider pausing replication during major maintenance

## Additional Commands

```bash
# Check replication slot status
kubectl exec -it svc/PUBLISHER-CLUSTER-rw -n NAMESPACE -- psql -c "
SELECT slot_name, active, pg_size_pretty(pg_wal_lsn_diff(pg_current_wal_lsn(), restart_lsn)) as lag_bytes
FROM pg_replication_slots
WHERE slot_type = 'logical';
"

# Force sync (if needed)
kubectl cnpg subscription enable SUBSCRIPTION-NAME -n NAMESPACE

# Check subscription details
kubectl exec -it svc/SUBSCRIBER-CLUSTER-rw -n NAMESPACE -- psql -c "\dRs+"
```

## When to Escalate

- Contact support if:
  - Lag continues to increase despite optimization
  - Network issues persist between clusters
  - Resource utilization is at maximum but lag continues
  - You experience frequent replication failures

```

## File: charts\paradedb\docs\runbooks\cnpgclusterlogicalreplicationstopped.md
```
# CNPGClusterLogicalReplicationStopped

## Description

The `CNPGClusterLogicalReplicationStopped` alert indicates that a logical replication subscription is not actively replicating data. This can occur in two scenarios:

1. **Disabled Subscription**: The subscription has been explicitly disabled (`enabled = false`)
2. **Stuck Subscription**: The subscription is enabled but has no active worker process (no PID) with pending data

- **Warning level**: Subscription stopped for 5 minutes
- **Critical level**: Subscription stopped for 15 minutes

## Impact

- **No Data Replication**: The subscriber will not receive any updates from the publisher
- **Data Divergence**: The subscriber data becomes increasingly stale
- **Disk Space**: WAL files may accumulate on the publisher
- **Critical**: Extended downtime may require full resynchronization

## Diagnosis

### Step 1: Check Subscription Status

```bash
# Check all subscriptions and their status
kubectl exec -it svc/SUBSCRIBER-CLUSTER-rw -n NAMESPACE -- psql -c "
SELECT
    s.subname,
    s.subenabled AS enabled,
    CASE
        WHEN NOT s.subenabled THEN 'Explicitly disabled'
        WHEN ss.pid IS NULL AND COALESCE(pg_wal_lsn_diff(ss.received_lsn, ss.latest_end_lsn), 0) > 0 THEN 'Stuck (no worker)'
        WHEN ss.pid IS NOT NULL THEN 'Active'
        ELSE 'Unknown'
    END as status,
    COALESCE(pg_wal_lsn_diff(ss.received_lsn, ss.latest_end_lsn), 0) AS pending_bytes,
    ss.pid IS NOT NULL AS has_worker
FROM pg_subscription s
LEFT JOIN pg_stat_subscription ss ON s.oid = ss.subid;
"
```

### Step 2: Check Worker Process

```bash
# Check if replication worker is running
kubectl exec -it svc/SUBSCRIBER-CLUSTER-rw -n NAMESPACE -- psql -c "
SELECT
    pid,
    application_name,
    state,
    backend_type,
    query_start
FROM pg_stat_activity
WHERE application_name LIKE '%subscription%' OR backend_type = 'logical replication worker';
"
```

### Step 3: Verify Subscription Details

```bash
# Get subscription configuration
kubectl exec -it svc/SUBSCRIBER-CLUSTER-rw -n NAMESPACE -- psql -c "
SELECT
    subname,
    subconninfo,
    subsynccommit,
    subslotname,
    subpublications
FROM pg_subscription;
"
```

### Step 4: Check PostgreSQL Logs

```bash
# Get the pod name
POD=$(kubectl get pods -n NAMESPACE -l app=postgresql -o name | head -1 | cut -d/ -f2)

# Check for subscription-related errors
kubectl logs -n NAMESPACE $POD --tail=200 | grep -i "subscription\|replication\|worker"
```

### Step 5: Test Connectivity to Publisher

```bash
# Extract connection info from subscription
kubectl exec -it svc/SUBSCRIBER-CLUSTER-rw -n NAMESPACE -- psql -c "
SELECT subconninfo FROM pg_subscription WHERE subname = 'your_subscription_name';
" | grep -o "host=[^ ]*" | cut -d= -f2

# Test connection
kubectl exec -it svc/SUBSCRIBER-CLUSTER-rw -n NAMESPACE -- \
  psql "host=PUBLISHER-HOST port=5432 dbname=DATABASE user=USER" -c "SELECT version();"
```

## Resolution

### If Subscription is Disabled

1. **Check if Disable Was Intentional**:
   ```bash
   # Check recent activity
   kubectl get events -n NAMESPACE --field-selector reason=SubscriptionDisabled

   # Check audit logs if RBAC is enabled
   kubectl auth can-i create subscriptions
   ```

2. **Enable the Subscription**:
   ```sql
   -- Enable the subscription
   ALTER SUBSCRIPTION subscription_name ENABLE;
   ```

   Or using kubectl:
   ```bash
   kubectl cnpg subscription enable subscription_name -n NAMESPACE
   ```

### If Subscription is Stuck

1. **Check for Worker Resource Limits**:
   ```bash
   # Check max_logical_replication_workers
   kubectl exec -it svc/SUBSCRIBER-CLUSTER-rw -n NAMESPACE -- psql -c "
   SHOW max_logical_replication_workers;
   SHOW max_worker_processes;
   "

   # Count active replication workers
   kubectl exec -it svc/SUBSCRIBER-CLUSTER-rw -n NAMESPACE -- psql -c "
   SELECT COUNT(*) FROM pg_stat_activity WHERE backend_type = 'logical replication worker';
   "
   ```

2. **Increase Worker Limits if Needed**:
   ```yaml
   # In the CNPG cluster configuration
   postgresql:
     parameters:
       max_logical_replication_workers: 10
       max_worker_processes: 20
       max_replication_slots: 10
   ```

3. **Restart the Subscription**:
   ```bash
   # First try to restart just the subscription
   kubectl cnpg subscription restart subscription_name -n NAMESPACE

   # If that doesn't work, restart the entire cluster
   kubectl cnpg restart subscriber-cluster -n NAMESPACE
   ```

4. **Check for Stuck Transactions**:
   ```sql
   -- Check for long-running transactions that might block replication
   SELECT pid, now() - pg_stat_activity.query_start AS duration, query
   FROM pg_stat_activity
   WHERE state = 'active'
     AND now() - query_start > interval '10 minutes'
     AND pid NOT IN (SELECT pid FROM pg_stat_activity WHERE application_name LIKE '%subscription%');

   -- Terminate blocking transactions if necessary
   SELECT pg_terminate_backend(pid);
   ```

### If Connection Issues

1. **Verify Publication Exists**:
   ```bash
   # On publisher
   kubectl exec -it svc/PUBLISHER-CLUSTER-rw -n NAMESPACE -- psql -c "
   SELECT pubname FROM pg_publication;
   "
   ```

2. **Check Replication Slot Status**:
   ```bash
   # On publisher
   kubectl exec -it svc/PUBLISHER-CLUSTER-rw -n NAMESPACE -- psql -c "
   SELECT slot_name, active, pg_size_pretty(pg_wal_lsn_diff(pg_current_wal_lsn(), restart_lsn)) as lag
   FROM pg_replication_slots
   WHERE slot_type = 'logical';
   "
   ```

3. **Recreate Subscription**:
   ```sql
   -- Drop and recreate the subscription
   DROP SUBSCRIPTION IF EXISTS subscription_name;

   CREATE SUBSCRIPTION subscription_name
   CONNECTION 'host=publisher-host port=5432 dbname=database_name user=replication_user password=xxx'
   PUBLICATION publication_name
   WITH (
     copy_data = true,
     synchronized_commit = 'off',
     create_slot = true
   );
   ```

### If WAL Retention Issues

1. **Check WAL Retention**:
   ```bash
   # On publisher, check wal_keep_size
   kubectl exec -it svc/PUBLISHER-CLUSTER-rw -n NAMESPACE -- psql -c "SHOW wal_keep_size;"

   # Check if WAL was removed before subscription could catch up
   kubectl exec -it svc/PUBLISHER-CLUSTER-rw -n NAMESPACE -- psql -c "
   SELECT slot_name, restart_lsn, pg_current_wal_lsn()
   FROM pg_replication_slots;
   "
   ```

2. **Increase WAL Retention**:
   ```yaml
   # In publisher configuration
   postgresql:
     parameters:
       wal_keep_size: '2GB'
       max_slot_wal_keep_size: '4GB'
   ```

## Advanced Troubleshooting

### Manual Worker Creation

```sql
-- If workers aren't starting automatically
SELECT pg_reload_conf();

-- Force subscription to start worker
ALTER SUBSCRIPTION subscription_name ENABLE;
ALTER SUBSCRIPTION subscription_name REFRESH PUBLICATION;
```

### Check System Resources

```bash
# Check for OOM kills or resource constraints
kubectl describe pod -n NAMESPACE POD-NAME

# Check if the pod was restarted
kubectl get pods -n NAMESPACE -l app=postgresql

# Check node resources
kubectl top nodes
```

### Full Resync Procedure

```bash
# Step 1: Mark all tables for resync
kubectl exec -it svc/SUBSCRIBER-CLUSTER-rw -n NAMESPACE -- psql -c "
SELECT schemaname, tablename
FROM pg_tables
WHERE schemaname NOT IN ('pg_catalog', 'information_schema');
"

# Step 2: Disable subscription
kubectl exec -it svc/SUBSCRIBER-CLUSTER-rw -n NAMESPACE -- psql -c "
ALTER SUBSCRIPTION subscription_name DISABLE;
"

# Step 3: Truncate subscriber tables (if safe)
kubectl exec -it svc/SUBSCRIBER-CLUSTER-rw -n NAMESPACE -- psql -c "
TRUNCATE TABLE table_name CASCADE;  -- Repeat for each table
"

# Step 4: Re-enable with full copy
kubectl exec -it svc/SUBSCRIBER-CLUSTER-rw -n NAMESPACE -- psql -c "
ALTER SUBSCRIPTION subscription_name ENABLE;
ALTER SUBSCRIPTION subscription_name REFRESH PUBLICATION WITH (copy_data = true);
"
```

## Prevention

1. **Monitoring**:
   - Set up alerts for disabled subscriptions
   - Monitor worker process counts
   - Track subscription state changes

2. **Resource Planning**:
   - Ensure adequate worker processes
   - Monitor disk space for WAL retention
   - Set appropriate timeouts

3. **High Availability**:
   ```yaml
   # Configure subscription retry parameters
   postgresql:
     parameters:
       wal_receiver_timeout: '60s'
       wal_receiver_status_interval: '10s'
       wal_retrieve_retry_interval: '5s'
   ```

4. **Backup Strategy**:
   - Regular backups of both publisher and subscriber
   - Document subscription configurations
   - Test recovery procedures

## Quick Reference Commands

```bash
# Check subscription status
kubectl exec -it svc/CLUSTER-rw -n NS -- psql -c "SELECT * FROM pg_stat_subscription;"

# Enable subscription
kubectl exec -it svc/CLUSTER-rw -n NS -- psql -c "ALTER SUBSCRIPTION sub_name ENABLE;"

# Restart subscription
kubectl cnpg subscription restart sub_name -n NS

# Restart cluster
kubectl cnpg restart CLUSTER -n NS

# Check replication slots
kubectl exec -it svc/PUBLISHER-rw -n NS -- psql -c "SELECT * FROM pg_replication_slots;"

# Check workers
kubectl exec -it svc/CLUSTER-rw -n NS -- psql -c "SELECT * FROM pg_stat_activity WHERE backend_type = 'logical replication worker';"
```

## When to Escalate

- Contact support if:
  - Subscription remains stuck after multiple restarts
  - Workers fail to start despite adequate resources
  - WAL retention issues prevent catch-up
  - Frequent disconnections occur
  - Data cannot be resynchronized successfully

```

## File: charts\paradedb\docs\runbooks\cnpgclusterlowdiskspacecritical.md
```
# CNPGClusterLowDiskSpaceCritical

## Description

The `CNPGClusterLowDiskSpaceCritical` alert is triggered when disk usage on any CloudNativePG cluster volume exceeds 90%. It may occur on the following volumes:

- The PVC hosting `PGDATA` (`storage` section)
- The PVC hosting WAL files (`walStorage` section)
- Any PVC hosting a tablespace (`tablespaces` section)

## Impact

At 100% disk usage, the cluster will experience downtime and potential data loss.

High disk usage can also cause fragmentation, where files are split due to insufficient contiguous free space, significantly increasing random I/O and degrading performance. Disk fragmentation can start happening at ~80% disk space usage.

## Diagnosis

Check disk usage metrics in the [CloudNativePG Grafana Dashboard](https://grafana.com/grafana/dashboards/20417-cloudnativepg/) to identify which volume is nearing capacity.

## Mitigation

If the WAL (Write-Ahead Logging) volume is filling and you have continuous archiving enabled, verify that WAL archiving is functioning correctly. A buildup of WAL files in `pg_wal` indicates an issue. Monitor the `cnpg_collector_pg_wal_archive_status` metric and ensure the number of `ready` files is not steadily increasing.

For more details, see the [CloudNativePG documentation on resizing storage](https://cloudnative-pg.io/documentation/current/troubleshooting/#storage-is-full).

```

## File: charts\paradedb\docs\runbooks\cnpgclusterlowdiskspacewarning.md
```
# CNPGClusterLowDiskSpaceWarning

## Description

The `CNPGClusterLowDiskSpaceWarning` alert is triggered when disk usage on any CloudNativePG cluster volume exceeds 80%. It may occur on the following volumes:

- The PVC hosting `PGDATA` (`storage` section)
- The PVC hosting WAL files (`walStorage` section)
- Any PVC hosting a tablespace (`tablespaces` section)

## Impact

At 100% disk usage, the cluster will experience downtime and potential data loss.

High disk usage can also cause fragmentation, where files are split due to insufficient contiguous free space, significantly increasing random I/O and degrading performance. Disk fragmentation can start happening at ~80% disk space usage.

## Diagnosis

Check disk usage metrics in the [CloudNativePG Grafana Dashboard](https://grafana.com/grafana/dashboards/20417-cloudnativepg/) to identify which volume is nearing capacity.

## Mitigation

If the WAL (Write-Ahead Logging) volume is filling and you have continuous archiving enabled, verify that WAL archiving is functioning correctly. A buildup of WAL files in `pg_wal` indicates an issue. Monitor the `cnpg_collector_pg_wal_archive_status` metric and ensure the number of `ready` files is not steadily increasing.

For more details, see the [CloudNativePG documentation on resizing storage](https://cloudnative-pg.io/documentation/current/troubleshooting/#storage-is-full).

```

## File: charts\paradedb\docs\runbooks\cnpgclusteroffline.md
```
# CNPGClusterOffline

## Description

The `CNPGClusterOffline` alert is triggered when no CloudNativePG instances are ready.

## Impact

When the cluster is offline, applications cannot access the database, resulting in a full service disruption.

## Diagnosis

To investigate why the cluster is offline:

- Get the status of the CloudNativePG cluster instances:

```bash
kubectl get pods -A -l "cnpg.io/podRole=instance" -o wide
```

- Inspect the logs of the affected CloudNativePG instances:

```bash
kubectl logs --namespace <namespace> pod/<instance-pod-name>
```

- Inspect the CloudNativePG operator logs:

```bash
kubectl logs --namespace cnpg-system -l "app.kubernetes.io/name=cloudnative-pg"
```

## Mitigation

Refer to the [CloudNativePG Failure Modes](https://cloudnative-pg.io/documentation/current/failure_modes/) and [CloudNativePG Troubleshooting](https://cloudnative-pg.io/documentation/current/troubleshooting/) documentation for guidance on troubleshooting and recovery.

```

## File: charts\paradedb\docs\runbooks\cnpgclusterphysicalreplicationlag.md
```
# CNPGClusterPhysicalReplicationLag

## Description

The `CNPGClusterPhysicalReplicationLag` alerts indicate that physical replication lag in the CloudNativePG cluster is exceeding acceptable thresholds. Physical replication lag measures how far behind the standby replicas are from the primary instance.

- **Warning level**: Replication lag exceeds 1 second
- **Critical level**: Replication lag exceeds 15 seconds

## Impact

Physical replication lag can cause the cluster replicas to become out of sync. Queries to the `-r` and `-ro` endpoints may return stale data. In the event of a failover, the data that has not yet been replicated from the primary to the replicas may be lost during failover.

- **Warning**: Minor data staleness, acceptable for read-heavy workloads with some tolerance for outdated data
- **Critical**: Significant data loss risk during failover, stale data affecting business operations

## Diagnosis

### Step 1: Check Replication Status

Check replication status in the [CloudNativePG Grafana Dashboard](https://grafana.com/grafana/dashboards/20417-cloudnativepg/) or by running:

```bash
kubectl exec --namespace <namespace> --stdin --tty services/<cluster_name>-rw -- psql -c "SELECT * FROM pg_stat_replication;"
```

### Step 2: Identify Common Causes

High physical replication lag can be caused by a number of factors:

**Network Issues:**
- Network congestion on the node interface
- Insufficient bandwidth between primary and replicas

```bash
# Inspect network interface statistics
kubectl exec -it <pod-name> -- ss -i
```

**Resource Contention:**
- High CPU or memory load on primary or replicas
- Disk I/O bottlenecks on replicas

```bash
# Check resource usage
kubectl top pods -n <namespace> -l cnpg.io/podRole=instance

# Check disk I/O
kubectl exec -it <pod-name> -- iostat -x 1 5
```

**Database Issues:**
- Long-running queries blocking replication
- Suboptimal PostgreSQL configuration

```bash
# Check for long-running queries
kubectl exec -it services/<cluster_name>-rw -- psql -c "
SELECT pid, now() - pg_stat_activity.query_start AS duration, query
FROM pg_stat_activity
WHERE state = 'active'
  AND now() - query_start > interval '5 minutes'
ORDER BY duration DESC;
"
```

### Step 3: Check PostgreSQL Configuration

Inspect the `PostgreSQL Parameters` section of the [CloudNativePG Grafana Dashboard](https://grafana.com/grafana/dashboards/20417-cloudnativepg/) or check directly:

```bash
kubectl exec -it services/<cluster_name>-rw -- psql -c "
SHOW max_wal_senders;
SHOW wal_compression;
SHOW max_replication_slots;
"
```

## Resolution

### For Warning Level Alerts (1-15 seconds lag)

1. **Monitor Resource Usage:**
   - Check CPU and Memory usage of the CloudNativePG cluster instances
   - Monitor network traffic between primary and replicas
   - Review disk I/O statistics

2. **Identify and Address Minor Issues:**
   - Look for and optimize long-running queries
   - Check for temporary resource spikes
   - Ensure adequate network bandwidth

### For Critical Level Alerts (>15 seconds lag)

1. **Immediate Actions:**
   ```bash
   # Terminate long-running transactions that generate excessive changes
   kubectl exec -it services/<cluster_name>-rw -- psql -c "
   SELECT pg_terminate_backend(pid)
   FROM pg_stat_activity
   WHERE state = 'active'
     AND now() - query_start > interval '30 minutes'
     AND query NOT LIKE '%autovacuum%';
   "
   ```

2. **Scale Up Resources:**
   Increase the Memory and CPU resources of the instances under heavy load. This can be done by setting `cluster.resources.requests` and `cluster.resources.limits` in your Helm values. Set both `requests` and `limits` to the same value to achieve QoS Guaranteed.

   ```yaml
   cluster:
     resources:
       requests:
         cpu: 4
         memory: 16Gi
       limits:
         cpu: 4
         memory: 16Gi
   ```

3. **Enable WAL Compression:**
   ```yaml
   cluster:
     postgresql:
       parameters:
         wal_compression: "on"
   ```
   This will reduce the size of the WAL files and can help reduce replication lag in congested networks. Changing `wal_compression` does not require a restart.

4. **Upgrade Storage Performance:**
   Increase IOPS or throughput of the storage used by the cluster to alleviate disk I/O bottlenecks.

   **Process:**
   1. Create a new storage class with higher IOPS/throughput
   2. Replace cluster instances one by one using the new storage class
   3. Start with standby replicas, not the primary
   4. Delete and recreate each instance with new storage:

   ```bash
   kubectl delete --namespace <namespace> pod/<pod-name> pvc/<pod-name> pvc/<pod-name>-wal
   ```

5. **Increase WAL Senders:**
   For clusters with 9+ instances, ensure `max_wal_senders` is adequate:
   ```yaml
   cluster:
     postgresql:
       parameters:
         max_wal_senders: 15  # Should be >= number of instances
   ```

## Prevention

1. **Resource Planning:**
   - Allocate adequate CPU, memory, and storage IOPS
   - Monitor resource utilization regularly
   - Set appropriate resource limits and requests

2. **Network Optimization:**
   - Ensure sufficient network bandwidth between replicas
   - Consider placing replicas in the same availability zone
   - Monitor network latency and throughput

3. **Configuration Tuning:**
   - Enable WAL compression to reduce replication bandwidth
   - Ensure adequate `max_wal_senders` for cluster size
   - Monitor and tune checkpoint settings

4. **Regular Maintenance:**
   - Monitor replication lag trends
   - Review long-running query patterns
   - Plan capacity upgrades before reaching limits

## Quick Reference Commands

```bash
# Check replication status
kubectl exec -n <namespace> services/<cluster_name>-rw -- psql -c "SELECT * FROM pg_stat_replication;"

# Check resource usage
kubectl top pods -n <namespace> -l cnpg.io/podRole=instance

# Check long-running queries
kubectl exec -it services/<cluster_name>-rw -- psql -c "
SELECT pid, now() - pg_stat_activity.query_start AS duration, query
FROM pg_stat_activity
WHERE state = 'active'
  AND now() - query_start > interval '5 minutes'
ORDER BY duration DESC;
"

# Restart a replica (if needed)
kubectl delete pod <replica-pod-name> -n <namespace>

# Check PostgreSQL parameters
kubectl exec -it services/<cluster_name>-rw -- psql -c "SHOW max_wal_senders; SHOW wal_compression;"
```

## When to Escalate

- Contact support if:
  - Replication lag continues to increase despite optimization
  - Network issues persist between cluster instances
  - Resource utilization is at maximum but lag continues
  - You experience frequent replication failures
  - Lag remains critical for more than 30 minutes
```

## File: charts\paradedb\docs\runbooks\cnpgclusterzonespreadwarning.md
```
# CNPGClusterZoneSpreadWarning

## Description

The `CNPGClusterZoneSpreadWarning` alert is triggered when pods are not evenly distributed across availability zones. To be more precise, the alert is raised when the number of pods exceeds the number of zones and the cluster runs in fewer than three zones.

This can be caused by insufficient nodes in the cluster or by misconfigured scheduling rules, such as pod affinity/anti-affinity rules or tolerations.

## Impact

The uneven distribution of pods across availability zones increases the risk of a single point of failure if a zone becomes unavailable.

## Diagnosis

To investigate pod distribution across zones:

- Get the status of the CloudNativePG cluster instances:

```bash
kubectl get pods -A -l "cnpg.io/podRole=instance" -o wide
```

- Get the nodes and their respective zones:

```bash
kubectl get nodes --label-columns topology.kubernetes.io/zone
```

- Identify the current primary instance with the following command:

```bash
kubectl get cluster paradedb -o 'jsonpath={"Current Primary: "}{.status.currentPrimary}{"; Target Primary: "}{.status.targetPrimary}{"\n"}' --namespace <namespace>
```

## Mitigation

1. Verify that there are more than one schedulable node per availability zone, with no taints preventing pod placement.

2. Verify your [affinity](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/), taints, and tolerations configuration.

3. Delete pods and PVCs that are not in the desired availability zone. The CloudNativePG operator will automatically create replacement pods. Always delete pods one at a time to avoid placing excess load on the primary instance.

Before doing so, carefully verify that:

- You are deleting the correct pod.
- You are not deleting the active primary instance.

```bash
kubectl delete --namespace <namespace> pod/<pod-name> pvc/<pod-name> pvc/<pod-name>-wal
```

```

## File: charts\paradedb\examples\basic.yaml
```
type: paradedb
mode: standalone
version:
  postgresql: "18"
cluster:
  instances: 1
backups:
  enabled: false

```

## File: charts\paradedb\examples\custom-queries.yaml
```
type: paradedb
mode: standalone

cluster:
  instances: 1
  monitoring:
    enabled: true
    customQueries:
      - name: "pg_cache_hit"
        query: |
          SELECT
            current_database() as datname,
            sum(heap_blks_hit) / (sum(heap_blks_hit) + sum(heap_blks_read)) as ratio
          FROM pg_statio_user_tables;
        metrics:
          - datname:
              usage: "LABEL"
              description: "Name of the database"
          - ratio:
              usage: GAUGE
              description: "Cache hit ratio"

backups:
  enabled: false

```

## File: charts\paradedb\examples\image-catalog-ref.yaml
```
type: paradedb
mode: standalone
version:
  major: "18"
  paradedb: "0.22.3"
cluster:
  instances: 1
  imageCatalogRef:
    kind: ImageCatalog
    name: my-image-catalog
backups:
  enabled: false

```

## File: charts\paradedb\examples\image-catalog.yaml
```
type: paradedb
mode: standalone
version:
  major: "18"
  paradedb: "0.22.3"
cluster:
  instances: 1
backups:
  enabled: false
imageCatalog:
  create: true
  images:
    - major: 18
      image: my-custom-postgres-image:mytag

```

## File: charts\paradedb\examples\paradedb.yaml
```
type: paradedb
mode: standalone
version:
  postgresql: "18"
  paradedb: "0.22.3"
cluster:
  instances: 1
backups:
  enabled: false

```

## File: charts\paradedb\examples\pgbouncer.yaml
```
type: paradedb
mode: standalone

cluster:
  instances: 1
  monitoring:
    enabled: true
    podMonitor:
      enabled: true
      labels: {}
      #   team-name: my-team

backups:
  enabled: false

poolers:
  - name: rw
    type: rw
    instances: 1
    monitoring:
      enabled: true
      podMonitor:
        enabled: true
        relabelings:
          - targetLabel: type
            replacement: rw
  - name: ro
    type: ro
    instances: 1
    monitoring:
      enabled: true
      podMonitor:
        enabled: true
        relabelings:
          - targetLabel: type
            replacement: ro

```

## File: charts\paradedb\examples\recovery-backup.yaml
```
type: paradedb
mode: recovery

recovery:
  method: backup
  backupName: "database-clustermarket-database-daily-backup-1683244800"

cluster:
  instances: 1

backups:
  provider: s3
  s3:
    region: "eu-west-1"
    bucket: "db-backups"
    path: "/v1-restore"
    accessKey: "AWS_S3_ACCESS_KEY"
    secretKey: "AWS_S3_SECRET_KEY"
  scheduledBackups:
    - name: daily-backup # Daily at midnight
      schedule: "0 0 0 * * *" # Daily at midnight
      backupOwnerReference: self
  retentionPolicy: "30d"
```

## File: charts\paradedb\examples\recovery-object_store.yaml
```
type: paradedb
mode: recovery

recovery:
  method: object_store
  clusterName: "cluster-name-to-recover-from"
  provider: s3
  s3:
    region: "eu-west-1"
    bucket: "db-backups"
    path: "/v1-restore"
    accessKey: "AWS_S3_ACCESS_KEY"
    secretKey: "AWS_S3_SECRET_KEY"

cluster:
  instances: 1

backups:
  endpointURL: "https://cm-db-chart-test.ams3.digitaloceanspaces.com"
  provider: s3
  s3:
    region: "eu-west-1"
    bucket: "db-backups"
    path: "/v1-restore"
    accessKey: "AWS_S3_ACCESS_KEY"
    secretKey: "AWS_S3_SECRET_KEY"
  scheduledBackups:
    - name: daily-backup # Daily at midnight
      schedule: "0 0 0 * * *" # Daily at midnight
      backupOwnerReference: self
  retentionPolicy: "30d"

```

## File: charts\paradedb\examples\recovery-pg_basebackup.yaml
```
type: paradedb
mode: "recovery"

recovery:
  method: "pg_basebackup"
  pgBaseBackup:
    sourceHost: "source-db.foo.com"
    sourceUsername: "streaming_replica"
    existingPasswordSecret: "source-db-replica-password"

cluster:
  instances: 1

backups:
  enabled: false
```

## File: charts\paradedb\examples\standalone-s3.yaml
```
type: paradedb
mode: standalone

cluster:
  instances: 1

backups:
  enabled: true
  provider: s3
  s3:
    region: "eu-west-1"
    bucket: "db-backups"
    path: "/v1"
    accessKey: "AWS_S3_ACCESS_KEY"
    secretKey: "AWS_S3_SECRET_KEY"
  scheduledBackups:
    - name: daily-backup # Daily at midnight
      schedule: "0 0 0 * * *" # Daily at midnight
      backupOwnerReference: self
  retentionPolicy: "30d"

```

## File: charts\paradedb\monitoring\metrics-clusters_postgresql_cnpg_io.yaml
```
kind: CustomResourceStateMetrics
spec:
  resources:
    - groupVersionKind:
        group: postgresql.cnpg.io
        version: "v1"
        kind: "Cluster"
      labelsFromPath:
        cluster: [metadata, name]
        namespace: [metadata, namespace]
      metrics:
        - name: "image_info"
          help: "Image used by the cluster pods"
          each:
            type: Info
            info:
              labelsFromPath:
                image: [status, image]

        - name: "phase_info"
          help: "Current phase of the cluster"
          each:
            type: Info
            info:
              labelsFromPath:
                phase: [status, phase]
                phase_reason: [status, phaseReason]

        - name: "instances_total"
          help: "Total number of PVC Groups detected in the cluster"
          each:
            type: Gauge
            gauge:
              path: [status, instances]

        - name: "instances_ready"
          help: "Total number of ready instances in the cluster"
          each:
            type: Gauge
            gauge:
              path: [status, readyInstances]

        - name: "instances_status_healthy_info"
          help: "Cluster instances that are healthy"
          each:
            type: Info
            info:
              path: [status, instancesStatus, "healthy"]
              labelsFromPath:
                instance: []

        - name: "instances_status_replicating_info"
          help: "Cluster instances that are replicating"
          each:
            type: Info
            info:
              path: [status, instancesStatus, "replicating"]
              labelsFromPath:
                instance: []

        - name: "instances_status_failed_info"
          help: "Cluster instances that are failed"
          each:
            type: Info
            info:
              path: [status, instancesStatus, "failed"]
              labelsFromPath:
                instance: []

        - name: "primary_info"
          help: "Information about the current primary instance"
          each:
            type: Info
            info:
              labelsFromPath:
                current_primary: [status, currentPrimary]
                target_primary: [status, targetPrimary]

        - name: "primary_promotion_time"
          help: "The timestamp when the last actual promotion to primary has occurred"
          each:
            type: Gauge
            gauge:
              path: [status, currentPrimaryTimestamp]
              labelsFromPath:
                primary: [status, currentPrimary]

        - name: "primary_failing_since_time"
          help: "The timestamp when the primary was detected to be unhealthy. This field is reported when .spec.failoverDelay is populated or during online upgrades"
          each:
            type: Gauge
            gauge:
              path: [status, currentPrimaryFailingSinceTimestamp]
              labelsFromPath:
                primary: [status, currentPrimary]

        - name: "first_recoverability_point"
          help: "First recoverability point timestamp by backup method"
          each:
            type: Gauge
            gauge:
              path: [status, firstRecoverabilityPointByMethod]
              labelFromKey: method

        - name: "last_successful_backup"
          help: "Last successful backup timestamp by method"
          each:
            type: Gauge
            gauge:
              path: [status, lastSuccessfulBackupByMethod]
              labelFromKey: method

        - name: "last_failed_backup"
          help: "Last failed backup timestamp"
          each:
            type: Gauge
            gauge:
              path: [status, lastFailedBackup]

        - name: "dangling_pvc_info"
          help: "List of all the PVCs created by this cluster and still available which are not attached to a Pod"
          each:
            type: Info
            info:
              path: [status, danglingPVC]
              labelsFromPath:
                pvc: []

        - name: "resizing_pvc_info"
          help: "List of all the PVCs that have ResizingPVC condition"
          each:
            type: Info
            info:
              path: [status, resizingPVC]
              labelsFromPath:
                pvc: []

        - name: "initializing_pvc_info"
          help: "List of all the PVCs that are being initialized by this cluster"
          each:
            type: Info
            info:
              path: [status, initializingPVC]
              labelsFromPath:
                pvc: []

        - name: "healthy_pvc_info"
          help: "List of all the PVCs not dangling nor initializing"
          each:
            type: Info
            info:
              path: [status, healthyPVC]
              labelsFromPath:
                pvc: []

        - name: "unusable_pvc_info"
          help: "List of all the PVCs that are unusable because another PVC is missing"
          each:
            type: Info
            info:
              path: [status, unusablePVC]
              labelsFromPath:
                pvc: []

        - name: "conditions"
          help: "Cluster conditions"
          each:
            type: Gauge
            gauge:
              path: [status, conditions]
              labelsFromPath:
                type: [type]
                reason: [reason]
                status: [status]
                message: [message]
                observed_generation: [observedGeneration]
              valueFrom: [lastTransitionTime]

        - name: "plugin_status_info"
          help: "Status of loaded plugins"
          each:
            type: Info
            info:
              path: [status, pluginStatus]
              labelsFromPath:
                name: [name]
                version: [version]
                capabilities: [capabilities]
                operator_capabilities: [operatorCapabilities]
                wal_capabilities: [walCapabilities]
                backup_capabilities: [backupCapabilities]
                restore_job_hook_capabilities: [restoreJobHookCapabilities]
                status: [status]

```

## File: charts\paradedb\monitoring\paradedb-dashboard.json
```
{
  "annotations": {
    "list": [
      {
        "builtIn": 1,
        "datasource": {
          "type": "datasource",
          "uid": "grafana"
        },
        "enable": true,
        "hide": true,
        "iconColor": "rgba(0, 211, 255, 1)",
        "name": "Annotations & Alerts",
        "target": {
          "limit": 100,
          "matchAny": false,
          "tags": [],
          "type": "dashboard"
        },
        "type": "dashboard"
      }
    ]
  },
  "editable": true,
  "fiscalYearStartMonth": 0,
  "graphTooltip": 1,
  "id": 89,
  "links": [
    {
      "asDropdown": false,
      "icon": "external link",
      "includeVars": false,
      "keepTime": false,
      "tags": [
        "cloudnativepg"
      ],
      "targetBlank": false,
      "title": "Related Dashboards",
      "tooltip": "",
      "type": "dashboards",
      "url": ""
    }
  ],
  "panels": [
    {
      "fieldConfig": {
        "defaults": {},
        "overrides": []
      },
      "gridPos": {
        "h": 12,
        "w": 5,
        "x": 0,
        "y": 0
      },
      "id": 676,
      "options": {
        "alertInstanceLabelFilter": "{namespace=~\"$namespace\"}",
        "alertName": "",
        "dashboardAlerts": false,
        "folder": "",
        "groupBy": [],
        "groupMode": "default",
        "maxItems": 20,
        "showInactiveAlerts": false,
        "sortOrder": 1,
        "stateFilter": {
          "error": true,
          "firing": true,
          "noData": false,
          "normal": true,
          "pending": true
        },
        "viewMode": "list"
      },
      "pluginVersion": "11.5.1",
      "title": "Alerts",
      "type": "alertlist"
    },
    {
      "fieldConfig": {
        "defaults": {},
        "overrides": []
      },
      "gridPos": {
        "h": 1,
        "w": 4,
        "x": 5,
        "y": 0
      },
      "id": 586,
      "options": {
        "code": {
          "language": "plaintext",
          "showLineNumbers": false,
          "showMiniMap": false
        },
        "content": "",
        "mode": "markdown"
      },
      "pluginVersion": "11.5.1",
      "title": "Health",
      "type": "text"
    },
    {
      "fieldConfig": {
        "defaults": {},
        "overrides": []
      },
      "gridPos": {
        "h": 1,
        "w": 9,
        "x": 9,
        "y": 0
      },
      "id": 336,
      "options": {
        "code": {
          "language": "plaintext",
          "showLineNumbers": false,
          "showMiniMap": false
        },
        "content": "",
        "mode": "markdown"
      },
      "pluginVersion": "11.5.1",
      "title": "Overview",
      "type": "text"
    },
    {
      "fieldConfig": {
        "defaults": {},
        "overrides": []
      },
      "gridPos": {
        "h": 1,
        "w": 3,
        "x": 18,
        "y": 0
      },
      "id": 352,
      "options": {
        "code": {
          "language": "plaintext",
          "showLineNumbers": false,
          "showMiniMap": false
        },
        "content": "",
        "mode": "markdown"
      },
      "pluginVersion": "11.5.1",
      "title": "Storage",
      "type": "text"
    },
    {
      "fieldConfig": {
        "defaults": {},
        "overrides": []
      },
      "gridPos": {
        "h": 1,
        "w": 3,
        "x": 21,
        "y": 0
      },
      "id": 354,
      "options": {
        "code": {
          "language": "plaintext",
          "showLineNumbers": false,
          "showMiniMap": false
        },
        "content": "",
        "mode": "markdown"
      },
      "pluginVersion": "11.5.1",
      "title": "Backups",
      "type": "text"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "description": "Cluster Replication Health represents the availability of replica servers available to replace the primary in case of a failure.",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "mappings": [
            {
              "options": {
                "0": {
                  "color": "green",
                  "index": 1,
                  "text": "Healthy"
                },
                "-1": {
                  "color": "red",
                  "index": 0,
                  "text": "None"
                }
              },
              "type": "value"
            },
            {
              "options": {
                "from": 1,
                "result": {
                  "color": "orange",
                  "index": 2,
                  "text": "Degraded"
                },
                "to": 999
              },
              "type": "range"
            }
          ],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": null
              }
            ]
          }
        },
        "overrides": []
      },
      "gridPos": {
        "h": 2,
        "w": 2,
        "x": 5,
        "y": 1
      },
      "id": 585,
      "options": {
        "colorMode": "background",
        "graphMode": "none",
        "justifyMode": "auto",
        "orientation": "auto",
        "percentChangeColorMode": "standard",
        "reduceOptions": {
          "calcs": [
            "lastNotNull"
          ],
          "fields": "",
          "values": false
        },
        "showPercentChange": false,
        "textMode": "auto",
        "wideLayout": true
      },
      "pluginVersion": "11.5.1",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "editorMode": "code",
          "expr": "(max(count by (pod) (cnpg_pg_stat_replication_backend_start{namespace=\"$namespace\", job=\"$namespace/$cluster\",application_name=~\"$instances\"})) - sum(cnpg_pg_replication_is_wal_receiver_up{namespace=~\"$namespace\", pod=~\"$instances\"})) + (clamp_max(max(cnpg_pg_replication_streaming_replicas{namespace=~\"$namespace\", pod=~\"$instances\"}), 1) - 1)",
          "legendFormat": "Replication",
          "range": true,
          "refId": "A"
        }
      ],
      "title": "",
      "type": "stat"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "description": "High lag indicates issue with replication. Network or storage interfaces may not have enough bandwidth to handle incoming traffic and replication at the same time.",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "mappings": [
            {
              "options": {
                "match": "null",
                "result": {
                  "color": "text",
                  "index": 0,
                  "text": "No data"
                }
              },
              "type": "special"
            },
            {
              "options": {
                "from": 0,
                "result": {
                  "color": "green",
                  "index": 1,
                  "text": "Healthy"
                },
                "to": 0.1
              },
              "type": "range"
            },
            {
              "options": {
                "from": 0.1,
                "result": {
                  "color": "yellow",
                  "index": 2,
                  "text": "Sub-second"
                },
                "to": 1
              },
              "type": "range"
            },
            {
              "options": {
                "from": 1,
                "result": {
                  "color": "orange",
                  "index": 3,
                  "text": "Delayed"
                },
                "to": 5
              },
              "type": "range"
            },
            {
              "options": {
                "from": 5,
                "result": {
                  "color": "red",
                  "index": 4,
                  "text": "High"
                },
                "to": 4294967295
              },
              "type": "range"
            }
          ],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": null
              }
            ]
          }
        },
        "overrides": []
      },
      "gridPos": {
        "h": 2,
        "w": 1,
        "x": 7,
        "y": 1
      },
      "id": 590,
      "options": {
        "colorMode": "background",
        "graphMode": "none",
        "justifyMode": "auto",
        "orientation": "auto",
        "percentChangeColorMode": "standard",
        "reduceOptions": {
          "calcs": [
            "lastNotNull"
          ],
          "fields": "",
          "values": false
        },
        "showPercentChange": false,
        "textMode": "value_and_name",
        "wideLayout": true
      },
      "pluginVersion": "11.5.1",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "editorMode": "code",
          "expr": "max(cnpg_pg_replication_lag{namespace=~\"$namespace\",pod=~\"$instances\"}) + max(cnpg_pg_stat_replication_write_lag_seconds{namespace=~\"$namespace\",pod=~\"$instances\"}) + max(cnpg_pg_stat_replication_flush_lag_seconds{namespace=~\"$namespace\",pod=~\"$instances\"}) + max(cnpg_pg_stat_replication_replay_lag_seconds{namespace=~\"$namespace\",pod=~\"$instances\"})",
          "hide": false,
          "instant": false,
          "legendFormat": "Lag",
          "range": true,
          "refId": "LAG"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "expr": "",
          "hide": false,
          "instant": false,
          "range": true,
          "refId": "A"
        }
      ],
      "title": "",
      "type": "stat"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "description": "Low disk space or low inode count will result in data loss.",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "mappings": [
            {
              "options": {
                "match": "null",
                "result": {
                  "color": "text",
                  "index": 0,
                  "text": "No data"
                }
              },
              "type": "special"
            },
            {
              "options": {
                "from": 0,
                "result": {
                  "color": "green",
                  "index": 1,
                  "text": "Healthy"
                },
                "to": 0.8
              },
              "type": "range"
            },
            {
              "options": {
                "from": 0.8,
                "result": {
                  "color": "orange",
                  "index": 2,
                  "text": "Warning"
                },
                "to": 0.9
              },
              "type": "range"
            },
            {
              "options": {
                "from": 0.9,
                "result": {
                  "color": "red",
                  "index": 3,
                  "text": "Critical"
                },
                "to": 0.98
              },
              "type": "range"
            },
            {
              "options": {
                "from": 0.98,
                "result": {
                  "color": "red",
                  "index": 4,
                  "text": "Data Loss"
                },
                "to": 1
              },
              "type": "range"
            },
            {
              "options": {
                "from": 1,
                "result": {
                  "color": "red",
                  "index": 5,
                  "text": "Full"
                },
                "to": 4294967295
              },
              "type": "range"
            }
          ],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": null
              }
            ]
          }
        },
        "overrides": []
      },
      "gridPos": {
        "h": 2,
        "w": 1,
        "x": 8,
        "y": 1
      },
      "id": 613,
      "options": {
        "colorMode": "background",
        "graphMode": "none",
        "justifyMode": "auto",
        "orientation": "auto",
        "percentChangeColorMode": "standard",
        "reduceOptions": {
          "calcs": [
            "lastNotNull"
          ],
          "fields": "",
          "values": false
        },
        "showPercentChange": false,
        "textMode": "value_and_name",
        "wideLayout": true
      },
      "pluginVersion": "11.5.1",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "editorMode": "code",
          "expr": "max((max(max by(persistentvolumeclaim) (1 - kubelet_volume_stats_available_bytes{namespace=\"$namespace\", persistentvolumeclaim=~\"$instances\"} / kubelet_volume_stats_capacity_bytes{namespace=\"$namespace\", persistentvolumeclaim=~\"$instances\"}))) OR (max by(persistentvolumeclaim) (kubelet_volume_stats_inodes_used{namespace=\"$namespace\", persistentvolumeclaim=~\"$instances\"} / kubelet_volume_stats_inodes{namespace=\"$namespace\", persistentvolumeclaim=~\"$instances\"})))",
          "hide": false,
          "legendFormat": "Storage",
          "range": true,
          "refId": "STORAGE"
        }
      ],
      "title": "",
      "type": "stat"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "description": "",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "dark-blue",
                "value": null
              }
            ]
          },
          "unit": "dateTimeFromNow"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 3,
        "w": 2,
        "x": 9,
        "y": 1
      },
      "id": 338,
      "options": {
        "colorMode": "background",
        "graphMode": "none",
        "justifyMode": "auto",
        "orientation": "horizontal",
        "percentChangeColorMode": "standard",
        "reduceOptions": {
          "calcs": [
            "lastNotNull"
          ],
          "fields": "",
          "values": false
        },
        "showPercentChange": false,
        "text": {},
        "textMode": "value",
        "wideLayout": true
      },
      "pluginVersion": "11.5.1",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "editorMode": "code",
          "exemplar": false,
          "expr": "max(cnpg_pg_postmaster_start_time{namespace=~\"$namespace\",pod=~\"$instances\"})*1000",
          "format": "time_series",
          "hide": false,
          "instant": true,
          "interval": "",
          "intervalFactor": 1,
          "legendFormat": "",
          "refId": "A"
        }
      ],
      "title": "Last failover",
      "type": "stat"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "blue",
                "value": null
              }
            ]
          }
        },
        "overrides": []
      },
      "gridPos": {
        "h": 6,
        "w": 3,
        "x": 11,
        "y": 1
      },
      "id": 342,
      "interval": "1m",
      "options": {
        "colorMode": "value",
        "graphMode": "area",
        "justifyMode": "auto",
        "orientation": "auto",
        "percentChangeColorMode": "standard",
        "reduceOptions": {
          "calcs": [
            "lastNotNull"
          ],
          "fields": "",
          "values": false
        },
        "showPercentChange": false,
        "textMode": "auto",
        "wideLayout": true
      },
      "pluginVersion": "11.5.1",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "editorMode": "code",
          "exemplar": true,
          "expr": "sum(rate(cnpg_pg_stat_database_xact_commit{namespace=~\"$namespace\",pod=~\"$instances\"}[$__interval])) + sum(rate(cnpg_pg_stat_database_xact_rollback{namespace=~\"$namespace\",pod=~\"$instances\"}[$__interval]))",
          "interval": "",
          "legendFormat": "TPS",
          "range": true,
          "refId": "TPS"
        }
      ],
      "title": "TPS",
      "type": "stat"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "description": "CPU Utilisation from Requests",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "mappings": [
            {
              "options": {
                "match": "null",
                "result": {
                  "color": "text",
                  "index": 0,
                  "text": "Missing request"
                }
              },
              "type": "special"
            }
          ],
          "max": 1,
          "min": 0,
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": null
              },
              {
                "color": "orange",
                "value": 0.8
              },
              {
                "color": "red",
                "value": 0.9
              }
            ]
          },
          "unit": "percentunit"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 4,
        "w": 2,
        "x": 14,
        "y": 1
      },
      "id": 344,
      "interval": "1m",
      "options": {
        "minVizHeight": 75,
        "minVizWidth": 75,
        "orientation": "horizontal",
        "reduceOptions": {
          "calcs": [
            "mean"
          ],
          "fields": "",
          "values": false
        },
        "showThresholdLabels": false,
        "showThresholdMarkers": true,
        "sizing": "auto"
      },
      "pluginVersion": "11.5.1",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "editorMode": "code",
          "expr": "sum(node_namespace_pod_container:container_cpu_usage_seconds_total:sum_irate{namespace=\"$namespace\", pod=~\"$instances\"}) / sum(kube_pod_container_resource_requests{job=\"kube-state-metrics\",  namespace=\"$namespace\", resource=\"cpu\", pod=~\"$instances\"})",
          "format": "time_series",
          "instant": true,
          "intervalFactor": 2,
          "refId": "A"
        }
      ],
      "title": "CPU Utilisation",
      "type": "gauge"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "description": "Memory Utilisation from Requests",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "mappings": [
            {
              "options": {
                "match": "null",
                "result": {
                  "color": "text",
                  "index": 0,
                  "text": "Missing request"
                }
              },
              "type": "special"
            }
          ],
          "max": 1,
          "min": 0,
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": null
              },
              {
                "color": "orange",
                "value": 0.8
              },
              {
                "color": "red",
                "value": 0.9
              }
            ]
          },
          "unit": "percentunit"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 4,
        "w": 2,
        "x": 16,
        "y": 1
      },
      "id": 348,
      "interval": "1m",
      "options": {
        "minVizHeight": 75,
        "minVizWidth": 75,
        "orientation": "horizontal",
        "reduceOptions": {
          "calcs": [
            "mean"
          ],
          "fields": "",
          "values": false
        },
        "showThresholdLabels": false,
        "showThresholdMarkers": true,
        "sizing": "auto"
      },
      "pluginVersion": "11.5.1",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "editorMode": "code",
          "expr": "sum(container_memory_working_set_bytes{job=\"kubelet\", metrics_path=\"/metrics/cadvisor\", namespace=\"$namespace\",container!=\"\", image!=\"\", pod=~\"$instances\"}) / sum(max by(pod) (kube_pod_container_resource_requests{job=\"kube-state-metrics\", namespace=\"$namespace\", resource=\"memory\", pod=~\"$instances\"}))",
          "format": "time_series",
          "instant": true,
          "intervalFactor": 2,
          "refId": "A"
        }
      ],
      "title": "Memory Utilisation",
      "type": "gauge"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "mappings": [],
          "max": 1,
          "min": 0,
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": null
              },
              {
                "color": "orange",
                "value": 0.8
              },
              {
                "color": "red",
                "value": 0.9
              }
            ]
          },
          "unit": "percentunit"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 4,
        "w": 3,
        "x": 18,
        "y": 1
      },
      "id": 356,
      "options": {
        "minVizHeight": 75,
        "minVizWidth": 75,
        "orientation": "auto",
        "reduceOptions": {
          "calcs": [
            "lastNotNull"
          ],
          "fields": "",
          "values": false
        },
        "showThresholdLabels": false,
        "showThresholdMarkers": true,
        "sizing": "auto"
      },
      "pluginVersion": "11.5.1",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "editorMode": "code",
          "exemplar": false,
          "expr": "max(max by(persistentvolumeclaim) (1 - kubelet_volume_stats_available_bytes{namespace=\"$namespace\", persistentvolumeclaim=~\"$instances\"} / kubelet_volume_stats_capacity_bytes{namespace=\"$namespace\", persistentvolumeclaim=~\"$instances\"}))",
          "format": "time_series",
          "instant": true,
          "interval": "",
          "legendFormat": "DATA",
          "range": false,
          "refId": "DATA"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "editorMode": "code",
          "exemplar": false,
          "expr": "max(max by(persistentvolumeclaim) (1 - kubelet_volume_stats_available_bytes{namespace=\"$namespace\", persistentvolumeclaim=~\"(${instances})-wal\"} / kubelet_volume_stats_capacity_bytes{namespace=\"$namespace\", persistentvolumeclaim=~\"(${instances})-wal\"}))",
          "format": "time_series",
          "instant": true,
          "interval": "",
          "legendFormat": "WAL",
          "range": false,
          "refId": "WAL"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "editorMode": "code",
          "exemplar": false,
          "expr": "max(\n    sum by (namespace,persistentvolumeclaim) (kubelet_volume_stats_used_bytes{namespace=\"$namespace\", persistentvolumeclaim=~\"(${instances})-tbs.*\"}) \n    /\n    sum by (namespace,persistentvolumeclaim) (kubelet_volume_stats_capacity_bytes{namespace=\"$namespace\", persistentvolumeclaim=~\"(${instances})-tbs.*\"}) \n    *\n    on(namespace, persistentvolumeclaim) group_left(volume)\n    kube_pod_spec_volumes_persistentvolumeclaims_info{pod=~\"$instances\"}\n)",
          "hide": false,
          "instant": true,
          "legendFormat": "Tablespaces (max)",
          "range": false,
          "refId": "Max Tablespace"
        }
      ],
      "title": "Volume Space Usage",
      "type": "gauge"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "description": "Elapsed time since the last successful base backup.",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "mappings": [
            {
              "options": {
                "from": 1,
                "result": {
                  "color": "semi-dark-orange",
                  "index": 0,
                  "text": "Invalid date"
                },
                "to": 1e+42
              },
              "type": "range"
            },
            {
              "options": {
                "from": -2147483648,
                "result": {
                  "color": "red",
                  "index": 1,
                  "text": "N/A"
                },
                "to": -1577847600
              },
              "type": "range"
            }
          ],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": null
              },
              {
                "color": "semi-dark-red",
                "value": -108000
              },
              {
                "color": "semi-dark-orange",
                "value": -107999
              },
              {
                "color": "#EAB839",
                "value": -89999
              },
              {
                "color": "green",
                "value": -86399
              }
            ]
          },
          "unit": "dtdurations"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 2,
        "w": 3,
        "x": 21,
        "y": 1
      },
      "id": 360,
      "options": {
        "colorMode": "value",
        "graphMode": "none",
        "justifyMode": "auto",
        "orientation": "auto",
        "percentChangeColorMode": "standard",
        "reduceOptions": {
          "calcs": [
            "lastNotNull"
          ],
          "fields": "",
          "values": false
        },
        "showPercentChange": false,
        "textMode": "auto",
        "wideLayout": true
      },
      "pluginVersion": "11.5.1",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "editorMode": "code",
          "exemplar": false,
          "expr": "-(time() - max(cnpg_collector_last_available_backup_timestamp{namespace=\"$namespace\",pod=~\"$instances\"}))",
          "instant": true,
          "legendFormat": "__auto",
          "range": false,
          "refId": "A"
        }
      ],
      "title": "Last Base Backup",
      "type": "stat"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "description": "High resource usage (CPU, Memory, DB Connections)",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "mappings": [
            {
              "options": {
                "match": "null",
                "result": {
                  "color": "text",
                  "index": 0,
                  "text": "No data"
                }
              },
              "type": "special"
            },
            {
              "options": {
                "from": 0,
                "result": {
                  "color": "green",
                  "index": 1,
                  "text": "Healthy"
                },
                "to": 0.8
              },
              "type": "range"
            },
            {
              "options": {
                "from": 0.8,
                "result": {
                  "color": "orange",
                  "index": 2,
                  "text": "Warning"
                },
                "to": 0.9
              },
              "type": "range"
            },
            {
              "options": {
                "from": 0.9,
                "result": {
                  "color": "red",
                  "index": 3,
                  "text": "Critical"
                },
                "to": 0.98
              },
              "type": "range"
            },
            {
              "options": {
                "from": 0.98,
                "result": {
                  "color": "red",
                  "index": 4,
                  "text": "Data Loss"
                },
                "to": 999
              },
              "type": "range"
            }
          ],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": null
              }
            ]
          }
        },
        "overrides": []
      },
      "gridPos": {
        "h": 2,
        "w": 4,
        "x": 5,
        "y": 3
      },
      "id": 591,
      "options": {
        "colorMode": "background",
        "graphMode": "none",
        "justifyMode": "auto",
        "orientation": "auto",
        "percentChangeColorMode": "standard",
        "reduceOptions": {
          "calcs": [
            "lastNotNull"
          ],
          "fields": "",
          "values": false
        },
        "showPercentChange": false,
        "textMode": "value_and_name",
        "wideLayout": true
      },
      "pluginVersion": "11.5.1",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "editorMode": "code",
          "expr": "(sum(node_namespace_pod_container:container_cpu_usage_seconds_total:sum_irate{ namespace=\"$namespace\", pod=~\"$instances\"}) / sum(kube_pod_container_resource_requests{job=\"kube-state-metrics\", namespace=\"$namespace\", resource=\"cpu\", pod=~\"$instances\"}))",
          "hide": false,
          "legendFormat": "CPU",
          "range": true,
          "refId": "CPU"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "editorMode": "code",
          "expr": "(sum(container_memory_working_set_bytes{job=\"kubelet\", metrics_path=\"/metrics/cadvisor\", namespace=\"$namespace\",container!=\"\", image!=\"\", pod=~\"$instances\"}) / sum(max by(pod) (kube_pod_container_resource_requests{job=\"kube-state-metrics\", namespace=\"$namespace\", resource=\"memory\", pod=~\"$instances\"})))",
          "hide": false,
          "instant": false,
          "legendFormat": "Memory",
          "range": true,
          "refId": "MEM"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "editorMode": "code",
          "expr": " (max(sum by (pod) (cnpg_backends_total{namespace=~\"$namespace\", pod=~\"$instances\"}) / sum by (pod) (cnpg_pg_settings_setting{name=\"max_connections\", namespace=~\"$namespace\", pod=~\"$instances\"})))",
          "hide": false,
          "instant": false,
          "legendFormat": "Connections",
          "range": true,
          "refId": "CONNS"
        }
      ],
      "title": "",
      "type": "stat"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "description": "Computes the time since the last known WAL archival in the primary.\nWe ensure to ignore the metric in the replicas by using (1 - cnpg_pg_replication_in_recovery ) as a multiplicative factor. It will be 0 for replicas, 1 for the primary.",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "mappings": [
            {
              "options": {
                "match": "null",
                "result": {
                  "color": "red",
                  "index": 0,
                  "text": "No backups"
                }
              },
              "type": "special"
            },
            {
              "options": {
                "from": -1e+22,
                "result": {
                  "color": "text",
                  "index": 1,
                  "text": "No data"
                },
                "to": 0
              },
              "type": "range"
            }
          ],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": null
              }
            ]
          },
          "unit": "dtdurations"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 2,
        "w": 3,
        "x": 21,
        "y": 3
      },
      "id": 362,
      "options": {
        "colorMode": "value",
        "graphMode": "none",
        "justifyMode": "auto",
        "orientation": "auto",
        "percentChangeColorMode": "standard",
        "reduceOptions": {
          "calcs": [
            "lastNotNull"
          ],
          "fields": "",
          "values": false
        },
        "showPercentChange": false,
        "textMode": "auto",
        "wideLayout": true
      },
      "pluginVersion": "11.5.1",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "editorMode": "code",
          "exemplar": false,
          "expr": "max((1 - cnpg_pg_replication_in_recovery{namespace=~\"$namespace\",pod=~\"$instances\"}) * (time() - timestamp(cnpg_pg_stat_archiver_seconds_since_last_archival{namespace=~\"$namespace\",pod=~\"$instances\"}) +\ncnpg_pg_stat_archiver_seconds_since_last_archival{namespace=~\"$namespace\",pod=~\"$instances\"}))",
          "format": "time_series",
          "instant": true,
          "interval": "",
          "legendFormat": "__auto",
          "range": false,
          "refId": "A"
        }
      ],
      "title": "Last archived WAL",
      "type": "stat"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "description": "",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "dark-blue",
                "value": null
              }
            ]
          },
          "unit": "string"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 3,
        "w": 2,
        "x": 9,
        "y": 4
      },
      "id": 340,
      "options": {
        "colorMode": "background",
        "graphMode": "none",
        "justifyMode": "auto",
        "orientation": "horizontal",
        "percentChangeColorMode": "standard",
        "reduceOptions": {
          "calcs": [
            "lastNotNull"
          ],
          "fields": "/^full$/",
          "values": false
        },
        "showPercentChange": false,
        "text": {},
        "textMode": "value",
        "wideLayout": true
      },
      "pluginVersion": "11.5.1",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "editorMode": "builder",
          "exemplar": false,
          "expr": "cnpg_collector_postgres_version{namespace=~\"$namespace\",pod=~\"$instances\"}",
          "format": "table",
          "hide": false,
          "instant": true,
          "interval": "",
          "intervalFactor": 1,
          "legendFormat": "{{pod}}",
          "range": false,
          "refId": "A"
        }
      ],
      "title": "Version",
      "type": "stat"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "description": "Base Backups are considered healthy when there has been at least one base backup in the last 24 hours.",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "mappings": [
            {
              "options": {
                "match": "null",
                "result": {
                  "color": "orange",
                  "index": 0,
                  "text": "None"
                }
              },
              "type": "special"
            },
            {
              "options": {
                "from": 0,
                "result": {
                  "color": "green",
                  "index": 1,
                  "text": "Healthy"
                },
                "to": 90000
              },
              "type": "range"
            },
            {
              "options": {
                "from": 90000,
                "result": {
                  "color": "orange",
                  "index": 2,
                  "text": "Degraded"
                },
                "to": 108000
              },
              "type": "range"
            },
            {
              "options": {
                "from": 108000,
                "result": {
                  "color": "red",
                  "index": 3,
                  "text": "None recent"
                },
                "to": 4294967295
              },
              "type": "range"
            }
          ],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": null
              }
            ]
          }
        },
        "overrides": [
          {
            "matcher": {
              "id": "byName",
              "options": "WAL"
            },
            "properties": [
              {
                "id": "mappings",
                "value": [
                  {
                    "options": {
                      "match": "null",
                      "result": {
                        "color": "orange",
                        "index": 0,
                        "text": "None"
                      }
                    },
                    "type": "special"
                  },
                  {
                    "options": {
                      "from": 0,
                      "result": {
                        "color": "green",
                        "index": 1,
                        "text": "Healthy"
                      },
                      "to": 360
                    },
                    "type": "range"
                  },
                  {
                    "options": {
                      "from": 360,
                      "result": {
                        "color": "orange",
                        "index": 2,
                        "text": "Delayed"
                      },
                      "to": 900
                    },
                    "type": "range"
                  },
                  {
                    "options": {
                      "from": 900,
                      "result": {
                        "color": "red",
                        "index": 3,
                        "text": "Unsynced"
                      },
                      "to": 4294967295
                    },
                    "type": "range"
                  }
                ]
              }
            ]
          }
        ]
      },
      "gridPos": {
        "h": 2,
        "w": 1,
        "x": 5,
        "y": 5
      },
      "id": 588,
      "options": {
        "colorMode": "background",
        "graphMode": "none",
        "justifyMode": "auto",
        "orientation": "auto",
        "percentChangeColorMode": "standard",
        "reduceOptions": {
          "calcs": [
            "lastNotNull"
          ],
          "fields": "",
          "values": false
        },
        "showPercentChange": false,
        "textMode": "value_and_name",
        "wideLayout": true
      },
      "pluginVersion": "11.5.1",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "editorMode": "code",
          "expr": "time() - max(cnpg_collector_last_available_backup_timestamp{namespace=\"$namespace\", pod=~\"$instances\"})",
          "legendFormat": "Backups",
          "range": true,
          "refId": "BACKUPS"
        }
      ],
      "title": "",
      "type": "stat"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "description": "Base Backups are considered healthy when there has been at least one base backup in the last 24 hours.",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "mappings": [
            {
              "options": {
                "match": "null",
                "result": {
                  "color": "orange",
                  "index": 0,
                  "text": "None"
                }
              },
              "type": "special"
            },
            {
              "options": {
                "from": 0,
                "result": {
                  "color": "green",
                  "index": 1,
                  "text": "Healthy"
                },
                "to": 360
              },
              "type": "range"
            },
            {
              "options": {
                "from": 360,
                "result": {
                  "color": "orange",
                  "index": 2,
                  "text": "Delayed"
                },
                "to": 900
              },
              "type": "range"
            },
            {
              "options": {
                "from": 900,
                "result": {
                  "color": "red",
                  "index": 3,
                  "text": "Unsynced"
                },
                "to": 4294967295
              },
              "type": "range"
            }
          ],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": null
              }
            ]
          }
        },
        "overrides": [
          {
            "matcher": {
              "id": "byName",
              "options": "WAL"
            },
            "properties": [
              {
                "id": "mappings",
                "value": [
                  {
                    "options": {
                      "match": "null",
                      "result": {
                        "color": "orange",
                        "index": 0,
                        "text": "None"
                      }
                    },
                    "type": "special"
                  },
                  {
                    "options": {
                      "from": 0,
                      "result": {
                        "color": "green",
                        "index": 1,
                        "text": "Healthy"
                      },
                      "to": 360
                    },
                    "type": "range"
                  },
                  {
                    "options": {
                      "from": 360,
                      "result": {
                        "color": "orange",
                        "index": 2,
                        "text": "Delayed"
                      },
                      "to": 900
                    },
                    "type": "range"
                  },
                  {
                    "options": {
                      "from": 900,
                      "result": {
                        "color": "red",
                        "index": 3,
                        "text": "Unsynced"
                      },
                      "to": 4294967295
                    },
                    "type": "range"
                  }
                ]
              }
            ]
          }
        ]
      },
      "gridPos": {
        "h": 2,
        "w": 1,
        "x": 6,
        "y": 5
      },
      "id": 612,
      "options": {
        "colorMode": "background",
        "graphMode": "none",
        "justifyMode": "auto",
        "orientation": "auto",
        "percentChangeColorMode": "standard",
        "reduceOptions": {
          "calcs": [
            "lastNotNull"
          ],
          "fields": "",
          "values": false
        },
        "showPercentChange": false,
        "textMode": "value_and_name",
        "wideLayout": true
      },
      "pluginVersion": "11.5.1",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "editorMode": "code",
          "expr": "max((1 - cnpg_pg_replication_in_recovery{namespace=~\"$namespace\", pod=~\"$instances\"}) * (time() - timestamp(cnpg_pg_stat_archiver_seconds_since_last_archival{namespace=~\"$namespace\", pod=~\"$instances\"}) +\ncnpg_pg_stat_archiver_seconds_since_last_archival{namespace=~\"$namespace\", pod=~\"$instances\"}))",
          "hide": false,
          "instant": false,
          "legendFormat": "WAL",
          "range": true,
          "refId": "WAL"
        }
      ],
      "title": "",
      "type": "stat"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "description": "Online if there is at least one ready operator pod",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "mappings": [
            {
              "options": {
                "0": {
                  "color": "red",
                  "index": 0,
                  "text": "Failure"
                }
              },
              "type": "value"
            },
            {
              "options": {
                "from": 1,
                "result": {
                  "color": "green",
                  "index": 1,
                  "text": "Online"
                },
                "to": 99
              },
              "type": "range"
            }
          ],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": null
              }
            ]
          }
        },
        "overrides": [
          {
            "matcher": {
              "id": "byName",
              "options": "A"
            },
            "properties": [
              {
                "id": "displayName",
                "value": "Reconcile errors"
              }
            ]
          }
        ]
      },
      "gridPos": {
        "h": 2,
        "w": 1,
        "x": 7,
        "y": 5
      },
      "id": 589,
      "options": {
        "colorMode": "background",
        "graphMode": "none",
        "justifyMode": "auto",
        "orientation": "auto",
        "percentChangeColorMode": "standard",
        "reduceOptions": {
          "calcs": [
            "lastNotNull"
          ],
          "fields": "",
          "values": false
        },
        "showPercentChange": false,
        "textMode": "value_and_name",
        "wideLayout": true
      },
      "pluginVersion": "11.5.1",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "editorMode": "code",
          "expr": "sum(kube_pod_status_ready{namespace=\"$operatorNamespace\", pod=~\"cloudnative-pg-operator.+\", condition=\"true\"})",
          "hide": false,
          "instant": true,
          "legendFormat": "Operator Status",
          "range": false,
          "refId": "A"
        }
      ],
      "title": "",
      "type": "stat"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "description": "The operator reconcile errors don't distinguish between database cluster or namespaces.",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "mappings": [
            {
              "options": {
                "0": {
                  "color": "green",
                  "index": 0,
                  "text": "None"
                }
              },
              "type": "value"
            },
            {
              "options": {
                "from": 1,
                "result": {
                  "color": "red",
                  "index": 1,
                  "text": "Backup"
                },
                "to": 9
              },
              "type": "range"
            },
            {
              "options": {
                "from": 10,
                "result": {
                  "color": "red",
                  "index": 2,
                  "text": "Cluster"
                },
                "to": 99
              },
              "type": "range"
            },
            {
              "options": {
                "from": 100,
                "result": {
                  "color": "red",
                  "index": 3,
                  "text": "Pooler"
                },
                "to": 999
              },
              "type": "range"
            },
            {
              "options": {
                "from": 1000,
                "result": {
                  "color": "red",
                  "index": 4,
                  "text": "Scheduled Backup"
                },
                "to": 9999
              },
              "type": "range"
            }
          ],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": null
              }
            ]
          }
        },
        "overrides": [
          {
            "matcher": {
              "id": "byName",
              "options": "A"
            },
            "properties": [
              {
                "id": "displayName",
                "value": "Reconcile errors"
              }
            ]
          }
        ]
      },
      "gridPos": {
        "h": 2,
        "w": 1,
        "x": 8,
        "y": 5
      },
      "id": 655,
      "options": {
        "colorMode": "background",
        "graphMode": "none",
        "justifyMode": "auto",
        "orientation": "auto",
        "percentChangeColorMode": "standard",
        "reduceOptions": {
          "calcs": [
            "lastNotNull"
          ],
          "fields": "",
          "values": false
        },
        "showPercentChange": false,
        "textMode": "value_and_name",
        "wideLayout": true
      },
      "pluginVersion": "11.5.1",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "editorMode": "code",
          "expr": "clamp_max(max(controller_runtime_reconcile_total{namespace=~\"$operatorNamespace\", result=\"error\", controller=\"backup\"}), 1)",
          "hide": true,
          "legendFormat": "__auto",
          "range": true,
          "refId": "RECONCILE_ERRORS_BACKUP"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "editorMode": "code",
          "expr": "clamp_max(max(controller_runtime_reconcile_total{namespace=~\"$operatorNamespace\", result=\"error\", controller=\"cluster\"}), 1)",
          "hide": true,
          "legendFormat": "__auto",
          "range": true,
          "refId": "RECONCILE_ERRORS_CLUSTER"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "editorMode": "code",
          "expr": "clamp_max(max(controller_runtime_reconcile_total{namespace=~\"$operatorNamespace\", result=\"error\", controller=\"pooler\"}), 1)",
          "hide": true,
          "legendFormat": "__auto",
          "range": true,
          "refId": "RECONCILE_ERRORS_POOLER"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "editorMode": "code",
          "expr": "clamp_max(max(controller_runtime_reconcile_total{namespace=~\"$operatorNamespace\", result=\"error\", controller=~\"scheduledbackup|scheduled-backup\"}), 1)",
          "hide": true,
          "legendFormat": "__auto",
          "range": true,
          "refId": "RECONCILE_ERRORS_SCHEDULED_BACKUP"
        },
        {
          "datasource": {
            "type": "__expr__",
            "uid": "${DS_EXPRESSION}"
          },
          "expression": "$RECONCILE_ERRORS_BACKUP + $RECONCILE_ERRORS_CLUSTER * 10 + $RECONCILE_ERRORS_POOLER * 100 + $RECONCILE_ERRORS_SCHEDULED_BACKUP * 1000",
          "hide": false,
          "refId": "A",
          "type": "math"
        }
      ],
      "title": "",
      "type": "stat"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "description": "",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "decimals": 2,
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "blue",
                "value": null
              }
            ]
          },
          "unit": "none"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 2,
        "w": 2,
        "x": 14,
        "y": 5
      },
      "id": 346,
      "options": {
        "colorMode": "value",
        "graphMode": "area",
        "justifyMode": "center",
        "orientation": "horizontal",
        "percentChangeColorMode": "same_as_value",
        "reduceOptions": {
          "calcs": [
            "lastNotNull"
          ],
          "fields": "",
          "values": false
        },
        "showPercentChange": true,
        "textMode": "value",
        "wideLayout": true
      },
      "pluginVersion": "11.5.1",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "editorMode": "code",
          "exemplar": true,
          "expr": "sum(node_namespace_pod_container:container_cpu_usage_seconds_total:sum_irate{namespace=\"$namespace\", pod=~\"$instances\"})",
          "hide": false,
          "interval": "",
          "legendFormat": "__auto",
          "range": true,
          "refId": "B"
        }
      ],
      "title": "",
      "type": "stat"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "description": "Container memory working set",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "blue",
                "value": null
              }
            ]
          },
          "unit": "bytes"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 2,
        "w": 2,
        "x": 16,
        "y": 5
      },
      "id": 350,
      "options": {
        "colorMode": "value",
        "graphMode": "area",
        "justifyMode": "center",
        "orientation": "horizontal",
        "percentChangeColorMode": "same_as_value",
        "reduceOptions": {
          "calcs": [
            "lastNotNull"
          ],
          "fields": "",
          "values": false
        },
        "showPercentChange": true,
        "textMode": "value",
        "wideLayout": true
      },
      "pluginVersion": "11.5.1",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "editorMode": "code",
          "exemplar": true,
          "expr": "sum(container_memory_working_set_bytes{pod=~\"$instances\", namespace=\"$namespace\", container!=\"\", image!=\"\"})",
          "hide": false,
          "interval": "",
          "legendFormat": "__auto",
          "range": true,
          "refId": "B"
        }
      ],
      "title": "",
      "type": "stat"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "description": "",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "decimals": 2,
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "blue",
                "value": null
              }
            ]
          },
          "unit": "decbytes"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 2,
        "w": 3,
        "x": 18,
        "y": 5
      },
      "id": 358,
      "options": {
        "colorMode": "value",
        "graphMode": "none",
        "justifyMode": "auto",
        "orientation": "auto",
        "percentChangeColorMode": "standard",
        "reduceOptions": {
          "calcs": [
            "sum"
          ],
          "fields": "",
          "values": false
        },
        "showPercentChange": false,
        "textMode": "value",
        "wideLayout": true
      },
      "pluginVersion": "11.5.1",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "editorMode": "code",
          "exemplar": false,
          "expr": "cnpg_pg_database_size_bytes{namespace=\"$namespace\", pod=~\"$instances\"}",
          "format": "table",
          "instant": false,
          "legendFormat": "__auto",
          "range": true,
          "refId": "A"
        }
      ],
      "title": "Database Size",
      "transformations": [
        {
          "id": "groupBy",
          "options": {
            "fields": {
              "Value": {
                "aggregations": [
                  "max"
                ],
                "operation": "aggregate"
              },
              "datname": {
                "aggregations": [],
                "operation": "groupby"
              }
            }
          }
        }
      ],
      "type": "stat"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "mappings": [
            {
              "options": {
                "0": {
                  "color": "red",
                  "index": 1,
                  "text": "N/A"
                }
              },
              "type": "value"
            },
            {
              "options": {
                "match": "null",
                "result": {
                  "color": "red",
                  "index": 0,
                  "text": "No backups"
                }
              },
              "type": "special"
            }
          ],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "blue",
                "value": null
              }
            ]
          },
          "unit": "dateTimeAsIso"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 2,
        "w": 3,
        "x": 21,
        "y": 5
      },
      "id": 364,
      "options": {
        "colorMode": "value",
        "graphMode": "none",
        "justifyMode": "auto",
        "orientation": "auto",
        "percentChangeColorMode": "standard",
        "reduceOptions": {
          "calcs": [
            "lastNotNull"
          ],
          "fields": "",
          "values": false
        },
        "showPercentChange": false,
        "textMode": "auto",
        "wideLayout": true
      },
      "pluginVersion": "11.5.1",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "editorMode": "code",
          "exemplar": false,
          "expr": "max(cnpg_collector_first_recoverability_point{namespace=~\"$namespace\",pod=~\"$instances\"})*1000",
          "format": "time_series",
          "instant": true,
          "interval": "",
          "legendFormat": "{{pod}}",
          "range": false,
          "refId": "A"
        }
      ],
      "title": "First Recoverability Point",
      "type": "stat"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "blue",
                "value": null
              }
            ]
          }
        },
        "overrides": []
      },
      "gridPos": {
        "h": 1,
        "w": 6,
        "x": 5,
        "y": 7
      },
      "id": 810,
      "options": {
        "colorMode": "background",
        "graphMode": "none",
        "justifyMode": "auto",
        "orientation": "horizontal",
        "percentChangeColorMode": "standard",
        "reduceOptions": {
          "calcs": [
            "lastNotNull"
          ],
          "fields": "/^Primary$/",
          "values": false
        },
        "showPercentChange": false,
        "text": {
          "titleSize": 15,
          "valueSize": 18
        },
        "textMode": "auto",
        "wideLayout": true
      },
      "pluginVersion": "11.5.1",
      "targets": [
        {
          "editorMode": "code",
          "exemplar": false,
          "expr": "label_join(kube_customresource_primary_info{customresource_group=\"postgresql.cnpg.io\", customresource_kind=\"Cluster\", namespace=\"$namespace\",cluster=\"$cluster\"}, \"Primary\", \" ➔ \", \"current_primary\", \"target_primary\") or label_replace(kube_customresource_primary_info{customresource_group=\"postgresql.cnpg.io\", customresource_kind=\"Cluster\", namespace=\"$namespace\",cluster=\"$cluster\"}, \"Primary\", \"$1\", \"current_primary\", \"(.*)\") == label_replace(kube_customresource_primary_info{customresource_group=\"postgresql.cnpg.io\", customresource_kind=\"Cluster\", namespace=\"$namespace\",cluster=\"$cluster\"}, \"Primary\", \"$1\", \"target_primary\", \"(.*)\")",
          "format": "table",
          "instant": true,
          "legendFormat": "__auto",
          "range": false,
          "refId": "A"
        }
      ],
      "title": "",
      "type": "stat"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "mappings": [
            {
              "options": {
                "Cluster in healthy state": {
                  "color": "green",
                  "index": 0
                }
              },
              "type": "value"
            }
          ],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "orange",
                "value": null
              }
            ]
          }
        },
        "overrides": []
      },
      "gridPos": {
        "h": 1,
        "w": 5,
        "x": 11,
        "y": 7
      },
      "id": 812,
      "options": {
        "colorMode": "background",
        "graphMode": "none",
        "justifyMode": "auto",
        "orientation": "horizontal",
        "percentChangeColorMode": "standard",
        "reduceOptions": {
          "calcs": [
            "lastNotNull"
          ],
          "fields": "/^Phase$/",
          "values": false
        },
        "showPercentChange": false,
        "text": {
          "titleSize": 12,
          "valueSize": 12
        },
        "textMode": "auto",
        "wideLayout": true
      },
      "pluginVersion": "11.5.1",
      "targets": [
        {
          "editorMode": "code",
          "exemplar": false,
          "expr": "kube_customresource_phase_info{customresource_group=\"postgresql.cnpg.io\", customresource_kind=\"Cluster\", namespace=\"$namespace\"}",
          "format": "table",
          "instant": true,
          "legendFormat": "__auto",
          "range": false,
          "refId": "A"
        }
      ],
      "title": "",
      "transformations": [
        {
          "id": "organize",
          "options": {
            "excludeByName": {},
            "includeByName": {},
            "indexByName": {},
            "renameByName": {
              "phase": "Phase"
            }
          }
        }
      ],
      "type": "stat"
    },
    {
      "fieldConfig": {
        "defaults": {},
        "overrides": []
      },
      "gridPos": {
        "h": 1,
        "w": 4,
        "x": 16,
        "y": 7
      },
      "id": 800,
      "options": {
        "code": {
          "language": "plaintext",
          "showLineNumbers": false,
          "showMiniMap": false
        },
        "content": "",
        "mode": "markdown"
      },
      "pluginVersion": "11.5.1",
      "title": "Physical Replication",
      "type": "text"
    },
    {
      "fieldConfig": {
        "defaults": {},
        "overrides": []
      },
      "gridPos": {
        "h": 1,
        "w": 4,
        "x": 20,
        "y": 7
      },
      "id": 801,
      "options": {
        "code": {
          "language": "plaintext",
          "showLineNumbers": false,
          "showMiniMap": false
        },
        "content": "",
        "mode": "markdown"
      },
      "pluginVersion": "11.5.1",
      "title": "Logical Replication",
      "type": "text"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "blue",
                "value": null
              }
            ]
          }
        },
        "overrides": []
      },
      "gridPos": {
        "h": 1,
        "w": 6,
        "x": 5,
        "y": 8
      },
      "id": 811,
      "options": {
        "colorMode": "background",
        "graphMode": "none",
        "justifyMode": "auto",
        "orientation": "horizontal",
        "percentChangeColorMode": "standard",
        "reduceOptions": {
          "calcs": [
            "lastNotNull"
          ],
          "fields": "/^Image$/",
          "values": false
        },
        "showPercentChange": false,
        "text": {
          "titleSize": 15,
          "valueSize": 16
        },
        "textMode": "auto",
        "wideLayout": true
      },
      "pluginVersion": "11.5.1",
      "targets": [
        {
          "editorMode": "code",
          "exemplar": false,
          "expr": "kube_customresource_image_info{customresource_group=\"postgresql.cnpg.io\", customresource_kind=\"Cluster\", namespace=\"$namespace\"}",
          "format": "table",
          "instant": true,
          "legendFormat": "__auto",
          "range": false,
          "refId": "A"
        }
      ],
      "title": "",
      "transformations": [
        {
          "id": "organize",
          "options": {
            "excludeByName": {},
            "includeByName": {},
            "indexByName": {},
            "renameByName": {
              "image": "Image"
            }
          }
        }
      ],
      "type": "stat"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "orange",
                "value": null
              }
            ]
          }
        },
        "overrides": []
      },
      "gridPos": {
        "h": 1,
        "w": 5,
        "x": 11,
        "y": 8
      },
      "id": 813,
      "options": {
        "colorMode": "value",
        "graphMode": "none",
        "justifyMode": "auto",
        "orientation": "horizontal",
        "percentChangeColorMode": "standard",
        "reduceOptions": {
          "calcs": [
            "lastNotNull"
          ],
          "fields": "/^phase_reason$/",
          "values": false
        },
        "showPercentChange": false,
        "text": {
          "titleSize": 12,
          "valueSize": 12
        },
        "textMode": "value",
        "wideLayout": true
      },
      "pluginVersion": "11.5.1",
      "targets": [
        {
          "editorMode": "code",
          "exemplar": false,
          "expr": "kube_customresource_phase_info{customresource_group=\"postgresql.cnpg.io\", customresource_kind=\"Cluster\", namespace=\"$namespace\"}",
          "format": "table",
          "instant": true,
          "legendFormat": "__auto",
          "range": false,
          "refId": "A"
        }
      ],
      "title": "",
      "transparent": true,
      "type": "stat"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "mappings": [],
          "max": 30,
          "min": 0,
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": null
              },
              {
                "color": "yellow",
                "value": 1
              },
              {
                "color": "orange",
                "value": 10
              },
              {
                "color": "red",
                "value": 20
              }
            ]
          },
          "unit": "s"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 2,
        "w": 2,
        "x": 16,
        "y": 8
      },
      "id": 465,
      "options": {
        "colorMode": "value",
        "graphMode": "area",
        "justifyMode": "auto",
        "orientation": "auto",
        "percentChangeColorMode": "inverted",
        "reduceOptions": {
          "calcs": [
            "lastNotNull"
          ],
          "fields": "",
          "values": false
        },
        "showPercentChange": true,
        "textMode": "auto",
        "wideLayout": true
      },
      "pluginVersion": "11.5.1",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "editorMode": "code",
          "exemplar": false,
          "expr": "max(cnpg_pg_replication_lag{namespace=~\"$namespace\",pod=~\"$instances\"})",
          "instant": false,
          "legendFormat": "__auto",
          "range": true,
          "refId": "A"
        }
      ],
      "title": "Replication Lag",
      "type": "stat"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "description": "Data sent but not written to the standby's disk",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": null
              },
              {
                "color": "yellow",
                "value": 1
              },
              {
                "color": "orange",
                "value": 10
              },
              {
                "color": "red",
                "value": 20
              }
            ]
          },
          "unit": "s"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 2,
        "w": 2,
        "x": 18,
        "y": 8
      },
      "id": 467,
      "options": {
        "colorMode": "value",
        "graphMode": "area",
        "justifyMode": "auto",
        "orientation": "auto",
        "percentChangeColorMode": "inverted",
        "reduceOptions": {
          "calcs": [
            "lastNotNull"
          ],
          "fields": "",
          "values": false
        },
        "showPercentChange": true,
        "textMode": "auto",
        "wideLayout": true
      },
      "pluginVersion": "11.5.1",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "editorMode": "code",
          "expr": "max(cnpg_pg_stat_replication_write_lag_seconds{namespace=~\"$namespace\",pod=~\"$instances\"})",
          "legendFormat": "__auto",
          "range": true,
          "refId": "A"
        }
      ],
      "title": "Write Lag",
      "type": "stat"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "mappings": [],
          "max": 30,
          "min": 0,
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": null
              },
              {
                "color": "yellow",
                "value": 1
              },
              {
                "color": "orange",
                "value": 10
              },
              {
                "color": "red",
                "value": 20
              }
            ]
          },
          "unit": "s"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 2,
        "w": 2,
        "x": 20,
        "y": 8
      },
      "id": 802,
      "options": {
        "colorMode": "value",
        "graphMode": "area",
        "justifyMode": "auto",
        "orientation": "auto",
        "percentChangeColorMode": "inverted",
        "reduceOptions": {
          "calcs": [
            "lastNotNull"
          ],
          "fields": "",
          "values": false
        },
        "showPercentChange": true,
        "textMode": "auto",
        "wideLayout": true
      },
      "pluginVersion": "11.5.1",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "editorMode": "code",
          "exemplar": false,
          "expr": "max(clamp_min(timestamp(cnpg_pg_stat_subscription_last_msg_receipt_time{namespace=\"$namespace\"}) - cnpg_pg_stat_subscription_last_msg_receipt_time{namespace=\"$namespace\"},0))",
          "instant": false,
          "legendFormat": "Replication Lag",
          "range": true,
          "refId": "A"
        }
      ],
      "title": "",
      "type": "stat"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "mappings": [],
          "max": 30,
          "min": 0,
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": null
              },
              {
                "color": "yellow",
                "value": 1
              },
              {
                "color": "orange",
                "value": 10
              },
              {
                "color": "red",
                "value": 20
              }
            ]
          },
          "unit": "bytes"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 2,
        "w": 2,
        "x": 22,
        "y": 8
      },
      "id": 803,
      "options": {
        "colorMode": "value",
        "graphMode": "area",
        "justifyMode": "auto",
        "orientation": "auto",
        "percentChangeColorMode": "inverted",
        "reduceOptions": {
          "calcs": [
            "lastNotNull"
          ],
          "fields": "",
          "values": false
        },
        "showPercentChange": true,
        "textMode": "auto",
        "wideLayout": true
      },
      "pluginVersion": "11.5.1",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "editorMode": "code",
          "exemplar": false,
          "expr": "max(abs(cnpg_pg_stat_subscription_received_lsn{namespace=\"$namespace\"} - cnpg_pg_stat_subscription_latest_end_lsn{namespace=\"$namespace\"}))",
          "instant": false,
          "legendFormat": "LSN Distance",
          "range": true,
          "refId": "A"
        }
      ],
      "title": "",
      "type": "stat"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "mappings": [
            {
              "options": {
                "1": {
                  "color": "green",
                  "index": 0,
                  "text": "READY"
                },
                "2": {
                  "color": "orange",
                  "index": 1,
                  "text": "REPLICATING"
                },
                "3": {
                  "color": "red",
                  "index": 2,
                  "text": "FAILED"
                }
              },
              "type": "value"
            }
          ],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": null
              }
            ]
          }
        },
        "overrides": []
      },
      "gridPos": {
        "h": 3,
        "w": 11,
        "x": 5,
        "y": 9
      },
      "id": 814,
      "options": {
        "colorMode": "background",
        "graphMode": "area",
        "justifyMode": "auto",
        "orientation": "auto",
        "percentChangeColorMode": "standard",
        "reduceOptions": {
          "calcs": [
            "lastNotNull"
          ],
          "fields": "",
          "values": false
        },
        "showPercentChange": false,
        "textMode": "auto",
        "wideLayout": true
      },
      "pluginVersion": "11.5.1",
      "targets": [
        {
          "editorMode": "code",
          "exemplar": false,
          "expr": "max by (instance)(kube_customresource_instances_status_healthy_info{namespace=\"$namespace\"} or \nkube_customresource_instances_status_replicating_info{namespace=\"$namespace\"}+1 or \nkube_customresource_instances_status_failed_info{namespace=\"$namespace\"}+2)",
          "instant": true,
          "legendFormat": "{{instance}}",
          "range": false,
          "refId": "A"
        }
      ],
      "title": "",
      "type": "stat"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "description": "Data flushed, but not replayed into the standby database",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": null
              },
              {
                "color": "yellow",
                "value": 1
              },
              {
                "color": "orange",
                "value": 10
              },
              {
                "color": "red",
                "value": 20
              }
            ]
          },
          "unit": "s"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 2,
        "w": 2,
        "x": 16,
        "y": 10
      },
      "id": 468,
      "options": {
        "colorMode": "value",
        "graphMode": "area",
        "justifyMode": "auto",
        "orientation": "auto",
        "percentChangeColorMode": "inverted",
        "reduceOptions": {
          "calcs": [
            "lastNotNull"
          ],
          "fields": "",
          "values": false
        },
        "showPercentChange": true,
        "textMode": "auto",
        "wideLayout": true
      },
      "pluginVersion": "11.5.1",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "editorMode": "code",
          "expr": "max(cnpg_pg_stat_replication_replay_lag_seconds{namespace=~\"$namespace\",pod=~\"$instances\"})",
          "legendFormat": "__auto",
          "range": true,
          "refId": "A"
        }
      ],
      "title": "Replay Lag",
      "type": "stat"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "description": "Data written but not flushed to the standby's disk",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": null
              },
              {
                "color": "yellow",
                "value": 1
              },
              {
                "color": "orange",
                "value": 10
              },
              {
                "color": "red",
                "value": 20
              }
            ]
          },
          "unit": "s"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 2,
        "w": 2,
        "x": 18,
        "y": 10
      },
      "id": 804,
      "options": {
        "colorMode": "value",
        "graphMode": "area",
        "justifyMode": "auto",
        "orientation": "auto",
        "percentChangeColorMode": "inverted",
        "reduceOptions": {
          "calcs": [
            "lastNotNull"
          ],
          "fields": "",
          "values": false
        },
        "showPercentChange": true,
        "textMode": "auto",
        "wideLayout": true
      },
      "pluginVersion": "11.5.1",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "editorMode": "code",
          "expr": "max(cnpg_pg_stat_replication_flush_lag_seconds{namespace=~\"$namespace\",pod=~\"$instances\"})",
          "legendFormat": "__auto",
          "range": true,
          "refId": "A"
        }
      ],
      "title": "Flush Lag",
      "type": "stat"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "description": "Evaluation of an SLO objective for logical replication LSN distance to stay below 500MB 99.9% of the time every 7 day rolling period.",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "mappings": [
            {
              "options": {
                "match": "null+nan",
                "result": {
                  "color": "text",
                  "index": 0
                }
              },
              "type": "special"
            }
          ],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "red",
                "value": null
              },
              {
                "color": "orange",
                "value": 0.999
              },
              {
                "color": "green",
                "value": 0.9995
              }
            ]
          },
          "unit": "percentunit"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 2,
        "w": 4,
        "x": 20,
        "y": 10
      },
      "hideTimeOverride": true,
      "id": 820,
      "options": {
        "colorMode": "value",
        "graphMode": "area",
        "justifyMode": "auto",
        "orientation": "auto",
        "percentChangeColorMode": "standard",
        "reduceOptions": {
          "calcs": [
            "lastNotNull"
          ],
          "fields": "",
          "values": false
        },
        "showPercentChange": false,
        "textMode": "value_and_name",
        "wideLayout": false
      },
      "pluginVersion": "11.5.1",
      "targets": [
        {
          "editorMode": "code",
          "expr": "min(avg by (subname) (avg_over_time(((abs(cnpg_pg_stat_subscription_received_lsn{namespace=\"$namespace\",worker_type=\"apply\"} - cnpg_pg_stat_subscription_latest_end_lsn{namespace=\"$namespace\"})) < BOOL 500*1024*1024)[$__range:])) * avg by (subname) (avg_over_time((time() - cnpg_pg_stat_subscription_last_msg_receipt_time{namespace=\"$namespace\",worker_type=\"apply\"} < BOOL 120))))",
          "legendFormat": "Logical Replication SLO 99.9% < 500MB",
          "range": true,
          "refId": "SLO"
        }
      ],
      "timeFrom": "7d",
      "title": "",
      "type": "stat"
    },
    {
      "collapsed": false,
      "gridPos": {
        "h": 1,
        "w": 24,
        "x": 0,
        "y": 12
      },
      "id": 12,
      "panels": [],
      "title": "Server Health",
      "type": "row"
    },
    {
      "fieldConfig": {
        "defaults": {},
        "overrides": []
      },
      "gridPos": {
        "h": 1,
        "w": 3,
        "x": 0,
        "y": 13
      },
      "id": 191,
      "options": {
        "code": {
          "language": "plaintext",
          "showLineNumbers": false,
          "showMiniMap": false
        },
        "content": "",
        "mode": "html"
      },
      "pluginVersion": "11.5.1",
      "title": "Instance",
      "transparent": true,
      "type": "text"
    },
    {
      "fieldConfig": {
        "defaults": {},
        "overrides": []
      },
      "gridPos": {
        "h": 1,
        "w": 2,
        "x": 3,
        "y": 13
      },
      "id": 192,
      "options": {
        "code": {
          "language": "plaintext",
          "showLineNumbers": false,
          "showMiniMap": false
        },
        "content": "",
        "mode": "html"
      },
      "pluginVersion": "11.5.1",
      "title": "Status",
      "type": "text"
    },
    {
      "fieldConfig": {
        "defaults": {},
        "overrides": []
      },
      "gridPos": {
        "h": 1,
        "w": 3,
        "x": 5,
        "y": 13
      },
      "id": 193,
      "options": {
        "code": {
          "language": "plaintext",
          "showLineNumbers": false,
          "showMiniMap": false
        },
        "content": "",
        "mode": "html"
      },
      "pluginVersion": "11.5.1",
      "title": "Clustering / replicas",
      "type": "text"
    },
    {
      "fieldConfig": {
        "defaults": {},
        "overrides": []
      },
      "gridPos": {
        "h": 1,
        "w": 2,
        "x": 8,
        "y": 13
      },
      "id": 384,
      "options": {
        "code": {
          "language": "plaintext",
          "showLineNumbers": false,
          "showMiniMap": false
        },
        "content": "",
        "mode": "html"
      },
      "pluginVersion": "11.5.1",
      "title": "Zone",
      "type": "text"
    },
    {
      "fieldConfig": {
        "defaults": {},
        "overrides": []
      },
      "gridPos": {
        "h": 1,
        "w": 4,
        "x": 10,
        "y": 13
      },
      "id": 195,
      "options": {
        "code": {
          "language": "plaintext",
          "showLineNumbers": false,
          "showMiniMap": false
        },
        "content": "",
        "mode": "html"
      },
      "pluginVersion": "11.5.1",
      "title": "Connections",
      "type": "text"
    },
    {
      "fieldConfig": {
        "defaults": {},
        "overrides": []
      },
      "gridPos": {
        "h": 1,
        "w": 3,
        "x": 14,
        "y": 13
      },
      "id": 196,
      "options": {
        "code": {
          "language": "plaintext",
          "showLineNumbers": false,
          "showMiniMap": false
        },
        "content": "",
        "mode": "html"
      },
      "pluginVersion": "11.5.1",
      "title": "Max Connections",
      "type": "text"
    },
    {
      "description": "",
      "fieldConfig": {
        "defaults": {},
        "overrides": []
      },
      "gridPos": {
        "h": 1,
        "w": 3,
        "x": 17,
        "y": 13
      },
      "id": 197,
      "options": {
        "code": {
          "language": "plaintext",
          "showLineNumbers": false,
          "showMiniMap": false
        },
        "content": "",
        "mode": "html"
      },
      "pluginVersion": "11.5.1",
      "title": "Wraparound",
      "type": "text"
    },
    {
      "fieldConfig": {
        "defaults": {},
        "overrides": []
      },
      "gridPos": {
        "h": 1,
        "w": 2,
        "x": 20,
        "y": 13
      },
      "id": 313,
      "options": {
        "code": {
          "language": "plaintext",
          "showLineNumbers": false,
          "showMiniMap": false
        },
        "content": "",
        "mode": "html"
      },
      "pluginVersion": "11.5.1",
      "title": "Started",
      "type": "text"
    },
    {
      "fieldConfig": {
        "defaults": {},
        "overrides": []
      },
      "gridPos": {
        "h": 1,
        "w": 2,
        "x": 22,
        "y": 13
      },
      "id": 198,
      "options": {
        "code": {
          "language": "plaintext",
          "showLineNumbers": false,
          "showMiniMap": false
        },
        "content": "",
        "mode": "html"
      },
      "pluginVersion": "11.5.1",
      "title": "Version",
      "type": "text"
    },
    {
      "fieldConfig": {
        "defaults": {},
        "overrides": []
      },
      "gridPos": {
        "h": 3,
        "w": 3,
        "x": 0,
        "y": 14
      },
      "id": 61,
      "options": {
        "code": {
          "language": "plaintext",
          "showLineNumbers": false,
          "showMiniMap": false
        },
        "content": "<table style=\"width:100%; height:100%;border:0px solid black;\">\n  <td style=\"text-align: center;vertical-align: middle;border:0px solid black; \"><p style=\"font-weight: bold;\">$instances</p>\n  </td>\n</table>",
        "mode": "html"
      },
      "pluginVersion": "11.5.1",
      "repeat": "instances",
      "repeatDirection": "v",
      "title": "",
      "type": "text"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "mappings": [
            {
              "options": {
                "0": {
                  "index": 0,
                  "text": "Down"
                },
                "1": {
                  "index": 1,
                  "text": "Up"
                }
              },
              "type": "value"
            }
          ],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "dark-red",
                "value": null
              },
              {
                "color": "green",
                "value": 1
              }
            ]
          },
          "unitScale": true
        },
        "overrides": []
      },
      "gridPos": {
        "h": 3,
        "w": 2,
        "x": 3,
        "y": 14
      },
      "id": 33,
      "options": {
        "colorMode": "background",
        "graphMode": "area",
        "justifyMode": "auto",
        "orientation": "auto",
        "reduceOptions": {
          "calcs": [
            "lastNotNull"
          ],
          "fields": "",
          "values": false
        },
        "showPercentChange": false,
        "text": {},
        "textMode": "value",
        "wideLayout": true
      },
      "pluginVersion": "10.3.3",
      "repeat": "instances",
      "repeatDirection": "v",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "editorMode": "code",
          "exemplar": true,
          "expr": "min(kube_pod_container_status_ready{container=\"postgres\",namespace=~\"$namespace\",pod=~\"$instances\"})",
          "instant": true,
          "interval": "",
          "legendFormat": "",
          "refId": "A"
        }
      ],
      "title": "",
      "type": "stat"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "description": "",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "mappings": [
            {
              "options": {
                "0": {
                  "color": "red",
                  "index": 1,
                  "text": "No"
                },
                "1": {
                  "color": "green",
                  "index": 0,
                  "text": "Yes"
                }
              },
              "type": "value"
            }
          ],
          "noValue": "-",
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": null
              },
              {
                "color": "red",
                "value": 80
              }
            ]
          },
          "unitScale": true
        },
        "overrides": []
      },
      "gridPos": {
        "h": 3,
        "w": 2,
        "x": 5,
        "y": 14
      },
      "id": 60,
      "options": {
        "colorMode": "background",
        "graphMode": "area",
        "justifyMode": "auto",
        "orientation": "auto",
        "reduceOptions": {
          "calcs": [
            "lastNotNull"
          ],
          "fields": "",
          "values": false
        },
        "showPercentChange": false,
        "text": {},
        "textMode": "value",
        "wideLayout": true
      },
      "pluginVersion": "10.3.3",
      "repeat": "instances",
      "repeatDirection": "v",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "1 - cnpg_pg_replication_in_recovery{namespace=~\"$namespace\",pod=~\"$instances\"} + cnpg_pg_replication_is_wal_receiver_up{namespace=~\"$namespace\",pod=~\"$instances\"}",
          "instant": true,
          "interval": "",
          "legendFormat": "{{pod}}",
          "refId": "A"
        }
      ],
      "title": "",
      "type": "stat"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "description": "",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "mappings": [],
          "noValue": "-",
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": null
              },
              {
                "color": "red",
                "value": 80
              }
            ]
          },
          "unitScale": true
        },
        "overrides": []
      },
      "gridPos": {
        "h": 3,
        "w": 1,
        "x": 7,
        "y": 14
      },
      "id": 229,
      "options": {
        "colorMode": "value",
        "graphMode": "none",
        "justifyMode": "auto",
        "orientation": "auto",
        "reduceOptions": {
          "calcs": [
            "lastNotNull"
          ],
          "fields": "",
          "values": false
        },
        "showPercentChange": false,
        "text": {},
        "textMode": "value",
        "wideLayout": true
      },
      "pluginVersion": "10.3.3",
      "repeat": "instances",
      "repeatDirection": "v",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "editorMode": "code",
          "exemplar": true,
          "expr": "cnpg_pg_replication_streaming_replicas{namespace=~\"$namespace\", pod=~\"$instances\"}",
          "instant": true,
          "interval": "",
          "legendFormat": "{{pod}}",
          "refId": "A"
        }
      ],
      "title": "",
      "type": "stat"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "description": "This metric depends on exporting the: `topology.kubernetes.io/zone` label through kube-state-metrics (not enabled by default). Can be added by changing its configuration with:\n\n```yaml\nmetricLabelsAllowlist:\n  - nodes=[topology.kubernetes.io/zone]\n```",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "blue",
                "value": null
              }
            ]
          }
        },
        "overrides": []
      },
      "gridPos": {
        "h": 3,
        "w": 2,
        "x": 8,
        "y": 14
      },
      "id": 386,
      "options": {
        "colorMode": "value",
        "graphMode": "none",
        "justifyMode": "auto",
        "orientation": "auto",
        "percentChangeColorMode": "standard",
        "reduceOptions": {
          "calcs": [
            "lastNotNull"
          ],
          "fields": "/^label_topology_kubernetes_io_zone$/",
          "values": false
        },
        "showPercentChange": false,
        "text": {
          "valueSize": 18
        },
        "textMode": "value",
        "wideLayout": true
      },
      "pluginVersion": "11.5.1",
      "repeat": "instances",
      "repeatDirection": "v",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "editorMode": "code",
          "exemplar": true,
          "expr": "kube_pod_info{namespace=~\"$namespace\", pod=~\"$instances\"} * on(node,instance) group_left(label_topology_kubernetes_io_zone) kube_node_labels",
          "format": "table",
          "instant": true,
          "interval": "",
          "legendFormat": "{{pod}}",
          "refId": "A"
        }
      ],
      "title": "",
      "type": "stat"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "palette-classic"
          },
          "custom": {
            "axisBorderShow": false,
            "axisCenteredZero": false,
            "axisColorMode": "text",
            "axisLabel": "",
            "axisPlacement": "auto",
            "barAlignment": 0,
            "drawStyle": "line",
            "fillOpacity": 10,
            "gradientMode": "none",
            "hideFrom": {
              "legend": false,
              "tooltip": false,
              "viz": false
            },
            "insertNulls": false,
            "lineInterpolation": "linear",
            "lineWidth": 1,
            "pointSize": 5,
            "scaleDistribution": {
              "type": "linear"
            },
            "showPoints": "never",
            "spanNulls": true,
            "stacking": {
              "group": "A",
              "mode": "none"
            },
            "thresholdsStyle": {
              "mode": "off"
            }
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": null
              }
            ]
          },
          "unit": "short",
          "unitScale": true
        },
        "overrides": []
      },
      "gridPos": {
        "h": 3,
        "w": 4,
        "x": 10,
        "y": 14
      },
      "id": 58,
      "options": {
        "legend": {
          "calcs": [
            "last",
            "mean"
          ],
          "displayMode": "list",
          "placement": "bottom",
          "showLegend": true
        },
        "tooltip": {
          "mode": "multi",
          "sort": "none"
        }
      },
      "pluginVersion": "8.2.1",
      "repeat": "instances",
      "repeatDirection": "v",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "editorMode": "code",
          "exemplar": true,
          "expr": "sum by (pod) (cnpg_backends_total{namespace=~\"$namespace\", pod=~\"$instances\"})",
          "instant": false,
          "interval": "",
          "legendFormat": "-",
          "refId": "A"
        }
      ],
      "title": "",
      "type": "timeseries"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "description": "",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "decimals": 0,
          "mappings": [],
          "max": 100,
          "min": 0,
          "noValue": "<1%",
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": null
              },
              {
                "color": "#EAB839",
                "value": 75
              },
              {
                "color": "red",
                "value": 90
              }
            ]
          },
          "unit": "percent",
          "unitScale": true
        },
        "overrides": []
      },
      "gridPos": {
        "h": 3,
        "w": 3,
        "x": 14,
        "y": 14
      },
      "id": 32,
      "options": {
        "minVizHeight": 75,
        "minVizWidth": 75,
        "orientation": "horizontal",
        "reduceOptions": {
          "calcs": [
            "last"
          ],
          "fields": "",
          "values": false
        },
        "showThresholdLabels": false,
        "showThresholdMarkers": true,
        "sizing": "auto",
        "text": {}
      },
      "pluginVersion": "10.3.3",
      "repeat": "instances",
      "repeatDirection": "v",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "editorMode": "code",
          "exemplar": true,
          "expr": "100 * sum by (pod) (cnpg_backends_total{namespace=~\"$namespace\", pod=~\"$instances\"}) / sum by (pod) (cnpg_pg_settings_setting{name=\"max_connections\", namespace=~\"$namespace\", pod=~\"$instances\"})",
          "instant": true,
          "interval": "",
          "legendFormat": "{{pod}}",
          "refId": "A"
        }
      ],
      "title": "",
      "type": "gauge"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "mappings": [],
          "max": 2147483647,
          "min": 0,
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": null
              },
              {
                "color": "#EAB839",
                "value": 200000000
              },
              {
                "color": "red",
                "value": 1000000000
              }
            ]
          },
          "unit": "none",
          "unitScale": true
        },
        "overrides": []
      },
      "gridPos": {
        "h": 3,
        "w": 3,
        "x": 17,
        "y": 14
      },
      "id": 8,
      "options": {
        "displayMode": "lcd",
        "maxVizHeight": 300,
        "minVizHeight": 10,
        "minVizWidth": 0,
        "namePlacement": "auto",
        "orientation": "horizontal",
        "reduceOptions": {
          "calcs": [
            "lastNotNull"
          ],
          "fields": "",
          "values": false
        },
        "showUnfilled": true,
        "sizing": "auto",
        "text": {},
        "valueMode": "color"
      },
      "pluginVersion": "10.3.3",
      "repeat": "instances",
      "repeatDirection": "v",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "editorMode": "code",
          "exemplar": true,
          "expr": "max by (pod) (cnpg_pg_database_xid_age{namespace=~\"$namespace\", pod=~\"$instances\"})",
          "instant": true,
          "interval": "",
          "legendFormat": "{{pod}}",
          "refId": "A"
        }
      ],
      "title": "",
      "type": "bargauge"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "description": "",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "dark-blue",
                "value": null
              }
            ]
          },
          "unit": "dateTimeFromNow",
          "unitScale": true
        },
        "overrides": []
      },
      "gridPos": {
        "h": 3,
        "w": 2,
        "x": 20,
        "y": 14
      },
      "id": 314,
      "options": {
        "colorMode": "background",
        "graphMode": "none",
        "justifyMode": "auto",
        "orientation": "horizontal",
        "reduceOptions": {
          "calcs": [
            "lastNotNull"
          ],
          "fields": "",
          "values": false
        },
        "showPercentChange": false,
        "text": {},
        "textMode": "value",
        "wideLayout": true
      },
      "pluginVersion": "10.3.3",
      "repeat": "instances",
      "repeatDirection": "v",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "editorMode": "code",
          "exemplar": false,
          "expr": "cnpg_pg_postmaster_start_time{namespace=~\"$namespace\", pod=~\"$instances\"}*1000",
          "format": "time_series",
          "hide": false,
          "instant": true,
          "interval": "",
          "intervalFactor": 1,
          "legendFormat": "",
          "refId": "A"
        }
      ],
      "title": "",
      "type": "stat"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "description": "",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "dark-blue",
                "value": null
              }
            ]
          },
          "unit": "string",
          "unitScale": true
        },
        "overrides": []
      },
      "gridPos": {
        "h": 3,
        "w": 2,
        "x": 22,
        "y": 14
      },
      "id": 42,
      "options": {
        "colorMode": "background",
        "graphMode": "none",
        "justifyMode": "auto",
        "orientation": "horizontal",
        "reduceOptions": {
          "calcs": [
            "lastNotNull"
          ],
          "fields": "/^full$/",
          "values": false
        },
        "showPercentChange": false,
        "text": {},
        "textMode": "value",
        "wideLayout": true
      },
      "pluginVersion": "10.3.3",
      "repeat": "instances",
      "repeatDirection": "v",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "editorMode": "code",
          "exemplar": false,
          "expr": "cnpg_collector_postgres_version{namespace=~\"$namespace\", pod=~\"$instances\"}",
          "format": "table",
          "hide": false,
          "instant": true,
          "interval": "",
          "intervalFactor": 1,
          "legendFormat": "{{pod}}",
          "refId": "A"
        }
      ],
      "title": "",
      "type": "stat"
    },
    {
      "collapsed": false,
      "gridPos": {
        "h": 1,
        "w": 24,
        "x": 0,
        "y": 17
      },
      "id": 796,
      "panels": [],
      "title": "Logical Replication",
      "type": "row"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "description": "",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "custom": {
            "align": "auto",
            "cellOptions": {
              "type": "auto"
            },
            "inspect": false
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "red",
                "value": null
              }
            ]
          },
          "unit": "bytes"
        },
        "overrides": [
          {
            "matcher": {
              "id": "byName",
              "options": "Value #MESSAGE_RECEIPT_AGE (lastNotNull)"
            },
            "properties": [
              {
                "id": "unit",
                "value": "s"
              },
              {
                "id": "custom.cellOptions",
                "value": {
                  "type": "color-background"
                }
              },
              {
                "id": "custom.cellOptions",
                "value": {
                  "type": "color-background"
                }
              },
              {
                "id": "thresholds",
                "value": {
                  "mode": "absolute",
                  "steps": [
                    {
                      "color": "green",
                      "value": null
                    },
                    {
                      "color": "yellow",
                      "value": 60
                    },
                    {
                      "color": "orange",
                      "value": 120
                    },
                    {
                      "color": "red",
                      "value": 300
                    }
                  ]
                }
              },
              {
                "id": "custom.width",
                "value": 210
              }
            ]
          },
          {
            "matcher": {
              "id": "byName",
              "options": "Value #LSN_DISTANCE (lastNotNull)"
            },
            "properties": [
              {
                "id": "unit",
                "value": "bytes"
              },
              {
                "id": "custom.cellOptions",
                "value": {
                  "type": "color-background"
                }
              },
              {
                "id": "thresholds",
                "value": {
                  "mode": "absolute",
                  "steps": [
                    {
                      "color": "green",
                      "value": null
                    },
                    {
                      "color": "yellow",
                      "value": 104857600
                    },
                    {
                      "color": "orange",
                      "value": 524288000
                    },
                    {
                      "color": "dark-orange",
                      "value": 1073741824
                    },
                    {
                      "color": "red",
                      "value": 10737418340
                    }
                  ]
                }
              },
              {
                "id": "custom.width",
                "value": 119
              }
            ]
          },
          {
            "matcher": {
              "id": "byName",
              "options": "Value #SLO (lastNotNull)"
            },
            "properties": [
              {
                "id": "unit",
                "value": "percentunit"
              },
              {
                "id": "custom.cellOptions",
                "value": {
                  "type": "color-background"
                }
              },
              {
                "id": "thresholds",
                "value": {
                  "mode": "absolute",
                  "steps": [
                    {
                      "color": "red",
                      "value": null
                    },
                    {
                      "color": "orange",
                      "value": 0.995
                    },
                    {
                      "color": "#EAB839",
                      "value": 0.999
                    },
                    {
                      "color": "green",
                      "value": 0.9995
                    }
                  ]
                }
              },
              {
                "id": "custom.width",
                "value": 70
              }
            ]
          }
        ]
      },
      "gridPos": {
        "h": 9,
        "w": 10,
        "x": 0,
        "y": 18
      },
      "id": 831,
      "options": {
        "cellHeight": "sm",
        "footer": {
          "countRows": false,
          "fields": "",
          "reducer": [
            "sum"
          ],
          "show": false
        },
        "showHeader": true
      },
      "pluginVersion": "11.5.1",
      "targets": [
        {
          "editorMode": "code",
          "exemplar": false,
          "expr": "clamp_min(timestamp(cnpg_pg_stat_subscription_last_msg_receipt_time) - cnpg_pg_stat_subscription_last_msg_receipt_time{namespace=\"$namespace\",job=\"$namespace/$cluster\",worker_type=\"apply\"},0)",
          "format": "table",
          "instant": true,
          "legendFormat": "__auto",
          "range": false,
          "refId": "MESSAGE_RECEIPT_AGE"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "editorMode": "code",
          "exemplar": false,
          "expr": "cnpg_pg_stat_subscription_received_lsn{namespace=\"$namespace\",job=\"$namespace/$cluster\",worker_type=\"apply\"} - cnpg_pg_stat_subscription_latest_end_lsn",
          "format": "table",
          "hide": false,
          "instant": true,
          "legendFormat": "__auto",
          "range": false,
          "refId": "LSN_DISTANCE"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "editorMode": "code",
          "exemplar": false,
          "expr": "avg by (subname) \n(\n    avg by (subname, pod) (\n        last_over_time(\n            avg_over_time(\n                (cnpg_pg_stat_subscription_received_lsn{namespace=\"$namespace\",job=\"$namespace/$cluster\",worker_type=\"apply\"} - cnpg_pg_stat_subscription_latest_end_lsn < bool 500 * 1024 * 1024)[$__range]\n            )[$__interval]\n        )\n    )\n    *\n    avg by (subname, pod) (\n        last_over_time(\n            avg_over_time(\n                (time() - cnpg_pg_stat_subscription_last_msg_receipt_time {namespace=\"$namespace\",job=\"$namespace/$cluster\",worker_type=\"apply\"} < bool 120)[$__range]\n            )[$__interval]\n        )\n    )\n    * \n    on (pod) group_left() (label_replace(kube_customresource_primary_info{customresource_group=\"postgresql.cnpg.io\", customresource_kind=\"Cluster\", namespace=\"$namespace\",cluster=\"$cluster\"}, \"pod\", \"$1\", \"current_primary\", \"(.*)\"))\n)[7d]",
          "format": "table",
          "hide": false,
          "instant": true,
          "legendFormat": "__auto",
          "range": false,
          "refId": "SLO"
        }
      ],
      "timeFrom": "7d",
      "title": "Subscriptions",
      "transformations": [
        {
          "id": "groupBy",
          "options": {
            "fields": {
              "Value #A": {
                "aggregations": [
                  "lastNotNull"
                ],
                "operation": "aggregate"
              },
              "Value #B": {
                "aggregations": [
                  "lastNotNull"
                ],
                "operation": "aggregate"
              },
              "Value #C": {
                "aggregations": [
                  "lastNotNull"
                ],
                "operation": "aggregate"
              },
              "Value #LSN_DISTANCE": {
                "aggregations": [
                  "lastNotNull"
                ],
                "operation": "aggregate"
              },
              "Value #MESSAGE_RECEIPT_AGE": {
                "aggregations": [
                  "lastNotNull"
                ],
                "operation": "aggregate"
              },
              "Value #SLO": {
                "aggregations": [
                  "lastNotNull"
                ],
                "operation": "aggregate"
              },
              "subname": {
                "aggregations": [],
                "operation": "groupby"
              }
            }
          }
        },
        {
          "id": "merge",
          "options": {}
        },
        {
          "id": "organize",
          "options": {
            "excludeByName": {
              "Time": true
            },
            "includeByName": {},
            "indexByName": {},
            "renameByName": {
              "Value #LSN_DISTANCE": "LSN Distance",
              "Value #LSN_DISTANCE (lastNotNull)": "LSN Distance",
              "Value #MESSAGE_RECEIPT_AGE": "Last Message Receipt Age",
              "Value #MESSAGE_RECEIPT_AGE (lastNotNull)": "Last Message Receipt Age",
              "Value #SLO": "SLO",
              "Value #SLO (lastNotNull)": "SLO",
              "subname": "Subscription"
            }
          }
        }
      ],
      "type": "table"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "description": "This shows the LSN distance for each Logical Replication Subscription based on data from `pg_stat_subscription`. Note that in case of replication lag, this value can show LSN distance as 0 when the subscription has not received any new data in a while. Check Last Message Receipt Age to account for that.",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "palette-classic"
          },
          "custom": {
            "axisBorderShow": false,
            "axisCenteredZero": false,
            "axisColorMode": "text",
            "axisLabel": "",
            "axisPlacement": "auto",
            "barAlignment": 0,
            "barWidthFactor": 0.6,
            "drawStyle": "line",
            "fillOpacity": 50,
            "gradientMode": "opacity",
            "hideFrom": {
              "legend": false,
              "tooltip": false,
              "viz": false
            },
            "insertNulls": false,
            "lineInterpolation": "linear",
            "lineWidth": 1,
            "pointSize": 5,
            "scaleDistribution": {
              "type": "linear"
            },
            "showPoints": "auto",
            "spanNulls": false,
            "stacking": {
              "group": "A",
              "mode": "none"
            },
            "thresholdsStyle": {
              "mode": "off"
            }
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "red",
                "value": null
              }
            ]
          },
          "unit": "bytes"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 9,
        "w": 14,
        "x": 10,
        "y": 18
      },
      "id": 799,
      "options": {
        "legend": {
          "calcs": [],
          "displayMode": "list",
          "placement": "right",
          "showLegend": true
        },
        "tooltip": {
          "hideZeros": false,
          "mode": "multi",
          "sort": "none"
        }
      },
      "pluginVersion": "11.5.1",
      "targets": [
        {
          "editorMode": "code",
          "expr": "max by (subname,worker_type)(max_over_time(cnpg_pg_stat_subscription_received_lsn{namespace=\"$namespace\"} - cnpg_pg_stat_subscription_latest_end_lsn{namespace=\"$namespace\"}))",
          "legendFormat": "{{subname}}",
          "range": true,
          "refId": "A"
        }
      ],
      "title": "LSN Distance",
      "type": "timeseries"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "description": "This shows the LSN rate of change for each Logical Replication Subscription based on data from `pg_stat_subscription`. Note that in case of replication lag, this value can show LSN distance as 0 when the subscription has not received any new data in a while. Check Last Message Receipt Age to account for that.",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "palette-classic"
          },
          "custom": {
            "axisBorderShow": false,
            "axisCenteredZero": false,
            "axisColorMode": "text",
            "axisLabel": "",
            "axisPlacement": "auto",
            "barAlignment": 0,
            "barWidthFactor": 0.6,
            "drawStyle": "line",
            "fillOpacity": 25,
            "gradientMode": "none",
            "hideFrom": {
              "legend": false,
              "tooltip": false,
              "viz": false
            },
            "insertNulls": false,
            "lineInterpolation": "linear",
            "lineWidth": 1,
            "pointSize": 5,
            "scaleDistribution": {
              "type": "linear"
            },
            "showPoints": "auto",
            "spanNulls": false,
            "stacking": {
              "group": "A",
              "mode": "none"
            },
            "thresholdsStyle": {
              "mode": "off"
            }
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "red",
                "value": null
              }
            ]
          },
          "unit": "binBps"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 9,
        "w": 10,
        "x": 0,
        "y": 27
      },
      "id": 832,
      "options": {
        "legend": {
          "calcs": [],
          "displayMode": "list",
          "placement": "bottom",
          "showLegend": true
        },
        "tooltip": {
          "hideZeros": false,
          "mode": "multi",
          "sort": "none"
        }
      },
      "pluginVersion": "11.5.1",
      "targets": [
        {
          "editorMode": "code",
          "expr": "avg by (subname,worker_type)(deriv(cnpg_pg_stat_subscription_received_lsn{namespace=\"$namespace\",job=\"$namespace/$cluster\"} - cnpg_pg_stat_subscription_latest_end_lsn))",
          "legendFormat": "{{subname}} ({{type}})",
          "range": true,
          "refId": "A"
        }
      ],
      "title": "LSN Distance Growth Rate",
      "type": "timeseries"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "description": "",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "palette-classic"
          },
          "custom": {
            "axisBorderShow": false,
            "axisCenteredZero": false,
            "axisColorMode": "text",
            "axisLabel": "",
            "axisPlacement": "auto",
            "barAlignment": 0,
            "barWidthFactor": 0.6,
            "drawStyle": "line",
            "fillOpacity": 30,
            "gradientMode": "opacity",
            "hideFrom": {
              "legend": false,
              "tooltip": false,
              "viz": false
            },
            "insertNulls": false,
            "lineInterpolation": "linear",
            "lineWidth": 1,
            "pointSize": 5,
            "scaleDistribution": {
              "type": "linear"
            },
            "showPoints": "auto",
            "spanNulls": false,
            "stacking": {
              "group": "A",
              "mode": "none"
            },
            "thresholdsStyle": {
              "mode": "off"
            }
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "red",
                "value": null
              },
              {
                "color": "orange",
                "value": 0.999
              },
              {
                "color": "green",
                "value": 0.9995
              }
            ]
          },
          "unit": "ms"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 9,
        "w": 14,
        "x": 10,
        "y": 27
      },
      "id": 797,
      "options": {
        "legend": {
          "calcs": [],
          "displayMode": "list",
          "placement": "bottom",
          "showLegend": true
        },
        "tooltip": {
          "hideZeros": false,
          "mode": "multi",
          "sort": "none"
        }
      },
      "pluginVersion": "11.5.1",
      "targets": [
        {
          "editorMode": "code",
          "expr": "max by(subname, worker_type) (max_over_time(clamp_min(timestamp(cnpg_pg_stat_subscription_last_msg_receipt_time) - cnpg_pg_stat_subscription_last_msg_receipt_time{namespace=\"$namespace\",job=\"$namespace/$cluster\",worker_type=\"apply\"},0)[$__rate_interval]))*1000",
          "legendFormat": "{{subname}} ({{type}})",
          "range": true,
          "refId": "A"
        }
      ],
      "title": "Last Message Receipt Age",
      "type": "timeseries"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "description": "Evaluation of an SLO objective for logical replication LSN distance to stay below 500MB 99.9% of the time every 7 day rolling period.",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "palette-classic"
          },
          "custom": {
            "axisBorderShow": false,
            "axisCenteredZero": false,
            "axisColorMode": "text",
            "axisLabel": "",
            "axisPlacement": "auto",
            "barAlignment": 0,
            "barWidthFactor": 0.6,
            "drawStyle": "line",
            "fillOpacity": 30,
            "gradientMode": "opacity",
            "hideFrom": {
              "legend": false,
              "tooltip": false,
              "viz": false
            },
            "insertNulls": false,
            "lineInterpolation": "linear",
            "lineWidth": 1,
            "pointSize": 5,
            "scaleDistribution": {
              "type": "linear"
            },
            "showPoints": "auto",
            "spanNulls": false,
            "stacking": {
              "group": "A",
              "mode": "none"
            },
            "thresholdsStyle": {
              "mode": "off"
            }
          },
          "mappings": [
            {
              "options": {
                "match": "null+nan",
                "result": {
                  "color": "text",
                  "index": 0
                }
              },
              "type": "special"
            }
          ],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "red",
                "value": null
              },
              {
                "color": "orange",
                "value": 0.999
              },
              {
                "color": "green",
                "value": 0.9995
              }
            ]
          },
          "unit": "percentunit"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 9,
        "w": 24,
        "x": 0,
        "y": 36
      },
      "id": 798,
      "options": {
        "legend": {
          "calcs": [],
          "displayMode": "list",
          "placement": "bottom",
          "showLegend": true
        },
        "tooltip": {
          "hideZeros": false,
          "mode": "single",
          "sort": "none"
        }
      },
      "pluginVersion": "11.5.1",
      "targets": [
        {
          "editorMode": "code",
          "expr": "avg by (subname) (avg_over_time(((abs(cnpg_pg_stat_subscription_received_lsn{namespace=\"$namespace\",worker_type=\"apply\"} - cnpg_pg_stat_subscription_latest_end_lsn{namespace=\"$namespace\"})) < BOOL 500*1024*1024)[$__range:])) * avg by (subname) (avg_over_time((time() - cnpg_pg_stat_subscription_last_msg_receipt_time{namespace=\"$namespace\",worker_type=\"apply\"} < BOOL 120)))",
          "legendFormat": "{{subname}}",
          "range": true,
          "refId": "SLO"
        }
      ],
      "timeFrom": "7d",
      "title": "Logical Replication SLO 99.9% < 500MB",
      "type": "timeseries"
    },
    {
      "collapsed": false,
      "gridPos": {
        "h": 1,
        "w": 24,
        "x": 0,
        "y": 45
      },
      "id": 806,
      "panels": [],
      "title": "ParadeDB",
      "type": "row"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "palette-classic"
          },
          "custom": {
            "axisBorderShow": false,
            "axisCenteredZero": false,
            "axisColorMode": "text",
            "axisLabel": "",
            "axisPlacement": "auto",
            "barAlignment": 0,
            "barWidthFactor": 0.6,
            "drawStyle": "line",
            "fillOpacity": 50,
            "gradientMode": "opacity",
            "hideFrom": {
              "legend": false,
              "tooltip": false,
              "viz": false
            },
            "insertNulls": false,
            "lineInterpolation": "linear",
            "lineWidth": 1,
            "pointSize": 5,
            "scaleDistribution": {
              "type": "linear"
            },
            "showPoints": "auto",
            "spanNulls": false,
            "stacking": {
              "group": "A",
              "mode": "none"
            },
            "thresholdsStyle": {
              "mode": "off"
            }
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": null
              },
              {
                "color": "red",
                "value": 80
              }
            ]
          }
        },
        "overrides": []
      },
      "gridPos": {
        "h": 8,
        "w": 12,
        "x": 0,
        "y": 46
      },
      "id": 807,
      "options": {
        "legend": {
          "calcs": [
            "min",
            "mean",
            "max"
          ],
          "displayMode": "table",
          "placement": "right",
          "showLegend": true
        },
        "tooltip": {
          "hideZeros": false,
          "mode": "multi",
          "sort": "none"
        }
      },
      "pluginVersion": "11.5.1",
      "targets": [
        {
          "editorMode": "code",
          "expr": "cnpg_paradedb_index_segments_count * on (pod) group_left() (label_replace(kube_customresource_primary_info{customresource_group=\"postgresql.cnpg.io\", customresource_kind=\"Cluster\", namespace=\"$namespace\"}, \"pod\", \"$1\", \"current_primary\", \"(.*)\"))",
          "legendFormat": "{{relname}}",
          "range": true,
          "refId": "A"
        }
      ],
      "title": "Segment count",
      "type": "timeseries"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "palette-classic"
          },
          "custom": {
            "axisBorderShow": false,
            "axisCenteredZero": false,
            "axisColorMode": "text",
            "axisLabel": "",
            "axisPlacement": "auto",
            "barAlignment": 0,
            "barWidthFactor": 0.6,
            "drawStyle": "line",
            "fillOpacity": 50,
            "gradientMode": "opacity",
            "hideFrom": {
              "legend": false,
              "tooltip": false,
              "viz": false
            },
            "insertNulls": false,
            "lineInterpolation": "linear",
            "lineWidth": 1,
            "pointSize": 5,
            "scaleDistribution": {
              "type": "linear"
            },
            "showPoints": "auto",
            "spanNulls": false,
            "stacking": {
              "group": "A",
              "mode": "none"
            },
            "thresholdsStyle": {
              "mode": "off"
            }
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": null
              }
            ]
          },
          "unit": "bytes"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 8,
        "w": 12,
        "x": 12,
        "y": 46
      },
      "id": 808,
      "options": {
        "legend": {
          "calcs": [
            "min",
            "mean",
            "max"
          ],
          "displayMode": "table",
          "placement": "right",
          "showLegend": true
        },
        "tooltip": {
          "hideZeros": false,
          "mode": "multi",
          "sort": "none"
        }
      },
      "pluginVersion": "11.5.1",
      "targets": [
        {
          "editorMode": "code",
          "expr": "cnpg_paradedb_index_segments_max_size * on (pod) group_left() (label_replace(kube_customresource_primary_info{customresource_group=\"postgresql.cnpg.io\", customresource_kind=\"Cluster\", namespace=\"$namespace\"}, \"pod\", \"$1\", \"current_primary\", \"(.*)\"))",
          "legendFormat": "max {{relname}}",
          "range": true,
          "refId": "A"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "editorMode": "code",
          "expr": "cnpg_paradedb_index_segments_avg_size * on (pod) group_left() (label_replace(kube_customresource_primary_info{customresource_group=\"postgresql.cnpg.io\", customresource_kind=\"Cluster\", namespace=\"$namespace\"}, \"pod\", \"$1\", \"current_primary\", \"(.*)\"))",
          "hide": false,
          "legendFormat": "avg {{relname}}",
          "range": true,
          "refId": "B"
        }
      ],
      "title": "Segment size",
      "type": "timeseries"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "fieldConfig": {
        "defaults": {
          "custom": {
            "hideFrom": {
              "legend": false,
              "tooltip": false,
              "viz": false
            },
            "scaleDistribution": {
              "type": "linear"
            }
          }
        },
        "overrides": []
      },
      "gridPos": {
        "h": 8,
        "w": 24,
        "x": 0,
        "y": 54
      },
      "id": 809,
      "maxDataPoints": 80,
      "maxPerRow": 2,
      "options": {
        "calculate": false,
        "cellGap": 1,
        "color": {
          "exponent": 0.5,
          "fill": "dark-orange",
          "mode": "scheme",
          "reverse": false,
          "scale": "exponential",
          "scheme": "RdYlBu",
          "steps": 64
        },
        "exemplars": {
          "color": "rgba(255,0,255,0.7)"
        },
        "filterValues": {
          "le": 1e-9
        },
        "legend": {
          "show": true
        },
        "rowsFrame": {
          "layout": "auto"
        },
        "tooltip": {
          "mode": "multi",
          "showColorScale": false,
          "yHistogram": false
        },
        "yAxis": {
          "axisPlacement": "left",
          "reverse": false,
          "unit": "bytes"
        }
      },
      "pluginVersion": "11.5.1",
      "repeat": "bm25_indicies",
      "repeatDirection": "h",
      "targets": [
        {
          "editorMode": "code",
          "expr": "avg(cnpg_paradedb_index_layer_segments_bucket{namespace=\"$namespace\",relname=\"$bm25_indicies\"}) by (le)",
          "format": "heatmap",
          "legendFormat": "{{relname}}",
          "range": true,
          "refId": "A"
        }
      ],
      "title": "$bm25_indicies segments",
      "type": "heatmap"
    },
    {
      "collapsed": false,
      "gridPos": {
        "h": 1,
        "w": 24,
        "x": 0,
        "y": 62
      },
      "id": 41,
      "panels": [],
      "title": "Configuration",
      "type": "row"
    },
    {
      "fieldConfig": {
        "defaults": {},
        "overrides": []
      },
      "gridPos": {
        "h": 1,
        "w": 3,
        "x": 0,
        "y": 63
      },
      "id": 187,
      "options": {
        "code": {
          "language": "plaintext",
          "showLineNumbers": false,
          "showMiniMap": false
        },
        "content": "",
        "mode": "html"
      },
      "pluginVersion": "11.5.1",
      "title": "Instance",
      "transparent": true,
      "type": "text"
    },
    {
      "fieldConfig": {
        "defaults": {},
        "overrides": []
      },
      "gridPos": {
        "h": 1,
        "w": 3,
        "x": 3,
        "y": 63
      },
      "id": 183,
      "options": {
        "code": {
          "language": "plaintext",
          "showLineNumbers": false,
          "showMiniMap": false
        },
        "content": "",
        "mode": "html"
      },
      "pluginVersion": "11.5.1",
      "title": "Max Connections",
      "type": "text"
    },
    {
      "fieldConfig": {
        "defaults": {},
        "overrides": []
      },
      "gridPos": {
        "h": 1,
        "w": 3,
        "x": 6,
        "y": 63
      },
      "id": 184,
      "options": {
        "code": {
          "language": "plaintext",
          "showLineNumbers": false,
          "showMiniMap": false
        },
        "content": "",
        "mode": "html"
      },
      "pluginVersion": "11.5.1",
      "title": "Shared Buffers",
      "type": "text"
    },
    {
      "fieldConfig": {
        "defaults": {},
        "overrides": []
      },
      "gridPos": {
        "h": 1,
        "w": 3,
        "x": 9,
        "y": 63
      },
      "id": 185,
      "options": {
        "code": {
          "language": "plaintext",
          "showLineNumbers": false,
          "showMiniMap": false
        },
        "content": "",
        "mode": "html"
      },
      "pluginVersion": "11.5.1",
      "title": "Effective Cache Size",
      "type": "text"
    },
    {
      "fieldConfig": {
        "defaults": {},
        "overrides": []
      },
      "gridPos": {
        "h": 1,
        "w": 3,
        "x": 12,
        "y": 63
      },
      "id": 186,
      "options": {
        "code": {
          "language": "plaintext",
          "showLineNumbers": false,
          "showMiniMap": false
        },
        "content": "",
        "mode": "html"
      },
      "pluginVersion": "11.5.1",
      "title": "Work Mem",
      "type": "text"
    },
    {
      "fieldConfig": {
        "defaults": {},
        "overrides": []
      },
      "gridPos": {
        "h": 1,
        "w": 3,
        "x": 15,
        "y": 63
      },
      "id": 188,
      "options": {
        "code": {
          "language": "plaintext",
          "showLineNumbers": false,
          "showMiniMap": false
        },
        "content": "",
        "mode": "html"
      },
      "pluginVersion": "11.5.1",
      "title": "Maintenance Work Mem",
      "type": "text"
    },
    {
      "fieldConfig": {
        "defaults": {},
        "overrides": []
      },
      "gridPos": {
        "h": 1,
        "w": 3,
        "x": 18,
        "y": 63
      },
      "id": 189,
      "options": {
        "code": {
          "language": "plaintext",
          "showLineNumbers": false,
          "showMiniMap": false
        },
        "content": "",
        "mode": "html"
      },
      "pluginVersion": "11.5.1",
      "title": "Random Page Cost",
      "type": "text"
    },
    {
      "fieldConfig": {
        "defaults": {},
        "overrides": []
      },
      "gridPos": {
        "h": 1,
        "w": 3,
        "x": 21,
        "y": 63
      },
      "id": 190,
      "options": {
        "code": {
          "language": "plaintext",
          "showLineNumbers": false,
          "showMiniMap": false
        },
        "content": "",
        "mode": "html"
      },
      "pluginVersion": "11.5.1",
      "title": "Sequential Page Cost",
      "type": "text"
    },
    {
      "fieldConfig": {
        "defaults": {},
        "overrides": []
      },
      "gridPos": {
        "h": 3,
        "w": 3,
        "x": 0,
        "y": 64
      },
      "id": 86,
      "options": {
        "code": {
          "language": "plaintext",
          "showLineNumbers": false,
          "showMiniMap": false
        },
        "content": "<table style=\"width:100%; height:100%;border:0px solid black;\">\n  <td style=\"text-align: center;vertical-align: middle;border:0px solid black; \"><p style=\"font-weight: bold;\">$instances</p>\n  </td>\n</table>",
        "mode": "html"
      },
      "pluginVersion": "10.3.1",
      "repeat": "instances",
      "repeatDirection": "v",
      "title": "",
      "type": "text"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "dark-purple",
                "value": null
              }
            ]
          },
          "unitScale": true
        },
        "overrides": []
      },
      "gridPos": {
        "h": 3,
        "w": 3,
        "x": 3,
        "y": 64
      },
      "id": 30,
      "options": {
        "colorMode": "background",
        "graphMode": "none",
        "justifyMode": "auto",
        "orientation": "horizontal",
        "reduceOptions": {
          "calcs": [
            "lastNotNull"
          ],
          "fields": "",
          "values": false
        },
        "showPercentChange": false,
        "text": {},
        "textMode": "value",
        "wideLayout": true
      },
      "pluginVersion": "10.3.1",
      "repeat": "instances",
      "repeatDirection": "v",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "cnpg_pg_settings_setting{name=\"max_connections\",namespace=~\"$namespace\",pod=~\"$instances\"}",
          "instant": true,
          "interval": "",
          "legendFormat": "{{pod}}",
          "refId": "A"
        }
      ],
      "title": "",
      "type": "stat"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "description": "",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "dark-purple",
                "value": null
              }
            ]
          },
          "unit": "bytes",
          "unitScale": true
        },
        "overrides": []
      },
      "gridPos": {
        "h": 3,
        "w": 3,
        "x": 6,
        "y": 64
      },
      "id": 24,
      "options": {
        "colorMode": "background",
        "graphMode": "none",
        "justifyMode": "auto",
        "orientation": "horizontal",
        "reduceOptions": {
          "calcs": [
            "lastNotNull"
          ],
          "fields": "",
          "values": false
        },
        "showPercentChange": false,
        "text": {},
        "textMode": "value",
        "wideLayout": true
      },
      "pluginVersion": "10.3.1",
      "repeat": "instances",
      "repeatDirection": "v",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "max by (pod) (cnpg_pg_settings_setting{name=\"shared_buffers\",namespace=~\"$namespace\",pod=~\"$instances\"}) * max by (pod) (cnpg_pg_settings_setting{name=\"block_size\",namespace=~\"$namespace\",pod=~\"$instances\"})",
          "instant": true,
          "interval": "",
          "legendFormat": "{{pod}}",
          "refId": "A"
        }
      ],
      "title": "",
      "type": "stat"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "description": "",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "dark-purple",
                "value": null
              }
            ]
          },
          "unit": "bytes",
          "unitScale": true
        },
        "overrides": []
      },
      "gridPos": {
        "h": 3,
        "w": 3,
        "x": 9,
        "y": 64
      },
      "id": 57,
      "options": {
        "colorMode": "background",
        "graphMode": "none",
        "justifyMode": "auto",
        "orientation": "horizontal",
        "reduceOptions": {
          "calcs": [
            "lastNotNull"
          ],
          "fields": "",
          "values": false
        },
        "showPercentChange": false,
        "text": {},
        "textMode": "value",
        "wideLayout": true
      },
      "pluginVersion": "10.3.1",
      "repeat": "instances",
      "repeatDirection": "v",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "max by (pod) (cnpg_pg_settings_setting{name=\"effective_cache_size\",namespace=~\"$namespace\",pod=~\"$instances\"}) * max by (pod) (cnpg_pg_settings_setting{name=\"block_size\",namespace=~\"$namespace\",pod=~\"$instances\"})",
          "instant": true,
          "interval": "",
          "legendFormat": "{{pod}}",
          "refId": "A"
        }
      ],
      "title": "",
      "type": "stat"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "description": "",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "dark-purple",
                "value": null
              }
            ]
          },
          "unit": "bytes",
          "unitScale": true
        },
        "overrides": []
      },
      "gridPos": {
        "h": 3,
        "w": 3,
        "x": 12,
        "y": 64
      },
      "id": 26,
      "options": {
        "colorMode": "background",
        "graphMode": "none",
        "justifyMode": "auto",
        "orientation": "horizontal",
        "reduceOptions": {
          "calcs": [
            "lastNotNull"
          ],
          "fields": "",
          "values": false
        },
        "showPercentChange": false,
        "text": {},
        "textMode": "value",
        "wideLayout": true
      },
      "pluginVersion": "10.3.1",
      "repeat": "instances",
      "repeatDirection": "v",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "cnpg_pg_settings_setting{name=\"work_mem\",namespace=~\"$namespace\",pod=~\"$instances\"} * 1024",
          "instant": true,
          "interval": "",
          "legendFormat": "{{pod}}",
          "refId": "A"
        }
      ],
      "title": "",
      "type": "stat"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "dark-purple",
                "value": null
              }
            ]
          },
          "unit": "bytes",
          "unitScale": true
        },
        "overrides": []
      },
      "gridPos": {
        "h": 3,
        "w": 3,
        "x": 15,
        "y": 64
      },
      "id": 47,
      "options": {
        "colorMode": "background",
        "graphMode": "none",
        "justifyMode": "auto",
        "orientation": "horizontal",
        "reduceOptions": {
          "calcs": [
            "lastNotNull"
          ],
          "fields": "",
          "values": false
        },
        "showPercentChange": false,
        "text": {},
        "textMode": "value",
        "wideLayout": true
      },
      "pluginVersion": "10.3.1",
      "repeat": "instances",
      "repeatDirection": "v",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "cnpg_pg_settings_setting{name=\"maintenance_work_mem\",namespace=~\"$namespace\",pod=~\"$instances\"}",
          "instant": true,
          "interval": "",
          "legendFormat": "{{pod}}",
          "refId": "A"
        }
      ],
      "title": "",
      "type": "stat"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "dark-purple",
                "value": null
              }
            ]
          },
          "unit": "none",
          "unitScale": true
        },
        "overrides": []
      },
      "gridPos": {
        "h": 3,
        "w": 3,
        "x": 18,
        "y": 64
      },
      "id": 48,
      "options": {
        "colorMode": "background",
        "graphMode": "none",
        "justifyMode": "auto",
        "orientation": "horizontal",
        "reduceOptions": {
          "calcs": [
            "lastNotNull"
          ],
          "fields": "",
          "values": false
        },
        "showPercentChange": false,
        "text": {},
        "textMode": "value",
        "wideLayout": true
      },
      "pluginVersion": "10.3.1",
      "repeat": "instances",
      "repeatDirection": "v",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "cnpg_pg_settings_setting{name=\"random_page_cost\",namespace=~\"$namespace\",pod=~\"$instances\"}",
          "instant": true,
          "interval": "",
          "legendFormat": "{{pod}}",
          "refId": "A"
        }
      ],
      "title": "",
      "type": "stat"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "dark-purple",
                "value": null
              }
            ]
          },
          "unit": "none",
          "unitScale": true
        },
        "overrides": []
      },
      "gridPos": {
        "h": 3,
        "w": 3,
        "x": 21,
        "y": 64
      },
      "id": 56,
      "options": {
        "colorMode": "background",
        "graphMode": "none",
        "justifyMode": "auto",
        "orientation": "horizontal",
        "reduceOptions": {
          "calcs": [
            "lastNotNull"
          ],
          "fields": "",
          "values": false
        },
        "showPercentChange": false,
        "text": {},
        "textMode": "value",
        "wideLayout": true
      },
      "pluginVersion": "10.3.1",
      "repeat": "instances",
      "repeatDirection": "v",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "cnpg_pg_settings_setting{name=\"seq_page_cost\",namespace=~\"$namespace\",pod=~\"$instances\"}",
          "instant": true,
          "interval": "",
          "legendFormat": "{{pod}}",
          "refId": "A"
        }
      ],
      "title": "",
      "type": "stat"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "custom": {
            "align": "auto",
            "cellOptions": {
              "type": "auto"
            },
            "filterable": true,
            "inspect": false
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "dark-purple",
                "value": null
              }
            ]
          }
        },
        "overrides": []
      },
      "gridPos": {
        "h": 9,
        "w": 24,
        "x": 0,
        "y": 67
      },
      "id": 150,
      "options": {
        "cellHeight": "sm",
        "footer": {
          "countRows": false,
          "fields": "",
          "reducer": [
            "sum"
          ],
          "show": false
        },
        "showHeader": true,
        "sortBy": []
      },
      "pluginVersion": "11.5.1",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "cnpg_pg_settings_setting{namespace=~\"$namespace\",pod=~\"$instances\"}",
          "format": "table",
          "instant": true,
          "interval": "",
          "legendFormat": "{{pod}}",
          "refId": "A"
        }
      ],
      "title": "Configurations",
      "transformations": [
        {
          "id": "organize",
          "options": {
            "excludeByName": {
              "Time": true,
              "__name__": true,
              "container": true,
              "endpoint": true,
              "instance": true,
              "job": true,
              "name": false,
              "namespace": true,
              "pod": false
            },
            "indexByName": {
              "Time": 0,
              "Value": 9,
              "__name__": 1,
              "container": 2,
              "endpoint": 3,
              "instance": 4,
              "job": 5,
              "name": 7,
              "namespace": 8,
              "pod": 6
            },
            "renameByName": {
              "__name__": "",
              "name": "parameter"
            }
          }
        },
        {
          "id": "groupingToMatrix",
          "options": {
            "columnField": "pod",
            "rowField": "parameter",
            "valueField": "Value"
          }
        },
        {
          "id": "organize",
          "options": {
            "excludeByName": {},
            "indexByName": {},
            "renameByName": {
              "parameter\\pod": "parameter"
            }
          }
        }
      ],
      "type": "table"
    },
    {
      "collapsed": false,
      "gridPos": {
        "h": 1,
        "w": 24,
        "x": 0,
        "y": 76
      },
      "id": 10,
      "panels": [],
      "title": "Operational Stats",
      "type": "row"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "palette-classic"
          },
          "custom": {
            "axisBorderShow": false,
            "axisCenteredZero": false,
            "axisColorMode": "text",
            "axisLabel": "",
            "axisPlacement": "auto",
            "barAlignment": 0,
            "barWidthFactor": 0.6,
            "drawStyle": "line",
            "fillOpacity": 30,
            "gradientMode": "opacity",
            "hideFrom": {
              "legend": false,
              "tooltip": false,
              "viz": false
            },
            "insertNulls": false,
            "lineInterpolation": "linear",
            "lineWidth": 2,
            "pointSize": 5,
            "scaleDistribution": {
              "type": "linear"
            },
            "showPoints": "never",
            "spanNulls": false,
            "stacking": {
              "group": "A",
              "mode": "normal"
            },
            "thresholdsStyle": {
              "mode": "off"
            }
          },
          "mappings": [],
          "min": 0,
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": null
              },
              {
                "color": "red",
                "value": 80
              }
            ]
          },
          "unit": "short"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 7,
        "w": 12,
        "x": 0,
        "y": 77
      },
      "id": 273,
      "options": {
        "legend": {
          "calcs": [],
          "displayMode": "list",
          "placement": "bottom",
          "showLegend": true
        },
        "tooltip": {
          "hideZeros": false,
          "mode": "multi",
          "sort": "desc"
        }
      },
      "pluginVersion": "11.5.1",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "sum(node_namespace_pod_container:container_cpu_usage_seconds_total:sum_irate{pod=~\"$instances\", namespace=~\"$namespace\"}) by (pod)",
          "format": "time_series",
          "interval": "",
          "intervalFactor": 2,
          "legendFormat": "{{pod}}",
          "refId": "A",
          "step": 10
        }
      ],
      "title": "CPU Usage",
      "type": "timeseries"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "palette-classic"
          },
          "custom": {
            "axisBorderShow": false,
            "axisCenteredZero": false,
            "axisColorMode": "text",
            "axisLabel": "",
            "axisPlacement": "auto",
            "barAlignment": 0,
            "barWidthFactor": 0.6,
            "drawStyle": "line",
            "fillOpacity": 30,
            "gradientMode": "opacity",
            "hideFrom": {
              "legend": false,
              "tooltip": false,
              "viz": false
            },
            "insertNulls": false,
            "lineInterpolation": "linear",
            "lineWidth": 2,
            "pointSize": 5,
            "scaleDistribution": {
              "type": "linear"
            },
            "showPoints": "never",
            "spanNulls": false,
            "stacking": {
              "group": "A",
              "mode": "none"
            },
            "thresholdsStyle": {
              "mode": "off"
            }
          },
          "mappings": [],
          "min": 0,
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": null
              },
              {
                "color": "red",
                "value": 80
              }
            ]
          },
          "unit": "bytes"
        },
        "overrides": [
          {
            "matcher": {
              "id": "byName",
              "options": "quota - requests"
            },
            "properties": [
              {
                "id": "color",
                "value": {
                  "fixedColor": "#F2495C",
                  "mode": "fixed"
                }
              },
              {
                "id": "custom.fillOpacity",
                "value": 0
              },
              {
                "id": "custom.lineWidth",
                "value": 2
              },
              {
                "id": "custom.stacking",
                "value": {
                  "group": "A",
                  "mode": "none"
                }
              },
              {
                "id": "custom.lineStyle",
                "value": {
                  "dash": [
                    10,
                    10
                  ],
                  "fill": "dash"
                }
              }
            ]
          },
          {
            "matcher": {
              "id": "byName",
              "options": "quota - limits"
            },
            "properties": [
              {
                "id": "color",
                "value": {
                  "fixedColor": "#FF9830",
                  "mode": "fixed"
                }
              },
              {
                "id": "custom.fillOpacity",
                "value": 0
              },
              {
                "id": "custom.lineWidth",
                "value": 2
              },
              {
                "id": "custom.stacking",
                "value": {
                  "group": "A",
                  "mode": "none"
                }
              },
              {
                "id": "custom.lineStyle",
                "value": {
                  "dash": [
                    10,
                    10
                  ],
                  "fill": "dash"
                }
              }
            ]
          }
        ]
      },
      "gridPos": {
        "h": 7,
        "w": 12,
        "x": 12,
        "y": 77
      },
      "id": 275,
      "options": {
        "legend": {
          "calcs": [],
          "displayMode": "list",
          "placement": "bottom",
          "showLegend": true
        },
        "tooltip": {
          "hideZeros": false,
          "mode": "multi",
          "sort": "desc"
        }
      },
      "pluginVersion": "11.5.1",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "sum(container_memory_working_set_bytes{pod=~\"$instances\", namespace=\"$namespace\", container!=\"\", image!=\"\"}) by (pod)",
          "format": "time_series",
          "interval": "",
          "intervalFactor": 2,
          "legendFormat": "{{pod}}",
          "refId": "A",
          "step": 10
        }
      ],
      "title": "Memory Usage (container memory working set)",
      "type": "timeseries"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "description": "",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "palette-classic"
          },
          "custom": {
            "axisBorderShow": false,
            "axisCenteredZero": false,
            "axisColorMode": "text",
            "axisLabel": "",
            "axisPlacement": "auto",
            "barAlignment": 0,
            "barWidthFactor": 0.6,
            "drawStyle": "line",
            "fillOpacity": 30,
            "gradientMode": "opacity",
            "hideFrom": {
              "legend": false,
              "tooltip": false,
              "viz": false
            },
            "insertNulls": false,
            "lineInterpolation": "linear",
            "lineWidth": 1,
            "pointSize": 5,
            "scaleDistribution": {
              "type": "linear"
            },
            "showPoints": "never",
            "spanNulls": true,
            "stacking": {
              "group": "A",
              "mode": "none"
            },
            "thresholdsStyle": {
              "mode": "off"
            }
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green"
              }
            ]
          }
        },
        "overrides": []
      },
      "gridPos": {
        "h": 8,
        "w": 24,
        "x": 0,
        "y": 84
      },
      "id": 39,
      "options": {
        "legend": {
          "calcs": [],
          "displayMode": "list",
          "placement": "bottom",
          "showLegend": true
        },
        "tooltip": {
          "hideZeros": false,
          "mode": "multi",
          "sort": "none"
        }
      },
      "pluginVersion": "11.5.1",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "sum(cnpg_backends_total{namespace=~\"$namespace\",pod=~\"$instances\"}) by (pod)",
          "hide": false,
          "interval": "",
          "legendFormat": "total ({{pod}})",
          "refId": "B"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "sum(cnpg_backends_total{namespace=~\"$namespace\",pod=~\"$instances\"}) by (state, pod)",
          "interval": "",
          "legendFormat": "{{state}} ({{pod}})",
          "refId": "A"
        }
      ],
      "title": "Session States",
      "type": "timeseries"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "palette-classic"
          },
          "custom": {
            "axisBorderShow": false,
            "axisCenteredZero": false,
            "axisColorMode": "text",
            "axisLabel": "",
            "axisPlacement": "auto",
            "barAlignment": 0,
            "barWidthFactor": 0.6,
            "drawStyle": "line",
            "fillOpacity": 30,
            "gradientMode": "opacity",
            "hideFrom": {
              "legend": false,
              "tooltip": false,
              "viz": false
            },
            "insertNulls": false,
            "lineInterpolation": "linear",
            "lineWidth": 1,
            "pointSize": 5,
            "scaleDistribution": {
              "type": "linear"
            },
            "showPoints": "never",
            "spanNulls": true,
            "stacking": {
              "group": "A",
              "mode": "none"
            },
            "thresholdsStyle": {
              "mode": "off"
            }
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green"
              },
              {
                "color": "red",
                "value": 80
              }
            ]
          }
        },
        "overrides": []
      },
      "gridPos": {
        "h": 8,
        "w": 12,
        "x": 0,
        "y": 92
      },
      "id": 50,
      "options": {
        "legend": {
          "calcs": [],
          "displayMode": "list",
          "placement": "bottom",
          "showLegend": true
        },
        "tooltip": {
          "hideZeros": false,
          "mode": "multi",
          "sort": "none"
        }
      },
      "pluginVersion": "11.5.1",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "editorMode": "code",
          "exemplar": true,
          "expr": "sum(rate(cnpg_pg_stat_database_xact_commit{namespace=~\"$namespace\",pod=~\"$instances\"}[5m])) by (pod)",
          "interval": "",
          "legendFormat": "committed ({{pod}})",
          "range": true,
          "refId": "A"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "sum(rate(cnpg_pg_stat_database_xact_rollback{namespace=~\"$namespace\",pod=~\"$instances\"}[5m])) by (pod)",
          "hide": false,
          "interval": "",
          "legendFormat": "rolled back ({{pod}})",
          "refId": "B"
        }
      ],
      "title": "Transactions [5m]",
      "type": "timeseries"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "description": "",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "palette-classic"
          },
          "custom": {
            "axisBorderShow": false,
            "axisCenteredZero": false,
            "axisColorMode": "text",
            "axisLabel": "",
            "axisPlacement": "auto",
            "barAlignment": 0,
            "barWidthFactor": 0.6,
            "drawStyle": "line",
            "fillOpacity": 30,
            "gradientMode": "opacity",
            "hideFrom": {
              "legend": false,
              "tooltip": false,
              "viz": false
            },
            "insertNulls": false,
            "lineInterpolation": "linear",
            "lineWidth": 1,
            "pointSize": 5,
            "scaleDistribution": {
              "type": "linear"
            },
            "showPoints": "never",
            "spanNulls": true,
            "stacking": {
              "group": "A",
              "mode": "none"
            },
            "thresholdsStyle": {
              "mode": "off"
            }
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green"
              },
              {
                "color": "red",
                "value": 80
              }
            ]
          },
          "unit": "s"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 8,
        "w": 12,
        "x": 12,
        "y": 92
      },
      "id": 4,
      "options": {
        "legend": {
          "calcs": [],
          "displayMode": "list",
          "placement": "bottom",
          "showLegend": true
        },
        "tooltip": {
          "hideZeros": false,
          "mode": "multi",
          "sort": "none"
        }
      },
      "pluginVersion": "11.5.1",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "max by (pod) (cnpg_backends_max_tx_duration_seconds{namespace=~\"$namespace\",pod=~\"$instances\"})",
          "interval": "",
          "legendFormat": "{{pod}}",
          "refId": "A"
        }
      ],
      "title": "Longest Transaction",
      "type": "timeseries"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "description": "",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "palette-classic"
          },
          "custom": {
            "axisBorderShow": false,
            "axisCenteredZero": false,
            "axisColorMode": "text",
            "axisLabel": "",
            "axisPlacement": "auto",
            "barAlignment": 0,
            "barWidthFactor": 0.6,
            "drawStyle": "line",
            "fillOpacity": 30,
            "gradientMode": "opacity",
            "hideFrom": {
              "legend": false,
              "tooltip": false,
              "viz": false
            },
            "insertNulls": false,
            "lineInterpolation": "linear",
            "lineWidth": 1,
            "pointSize": 5,
            "scaleDistribution": {
              "type": "linear"
            },
            "showPoints": "never",
            "spanNulls": true,
            "stacking": {
              "group": "A",
              "mode": "none"
            },
            "thresholdsStyle": {
              "mode": "off"
            }
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green"
              },
              {
                "color": "red",
                "value": 80
              }
            ]
          }
        },
        "overrides": []
      },
      "gridPos": {
        "h": 8,
        "w": 12,
        "x": 0,
        "y": 100
      },
      "id": 55,
      "options": {
        "legend": {
          "calcs": [],
          "displayMode": "list",
          "placement": "bottom",
          "showLegend": true
        },
        "tooltip": {
          "hideZeros": false,
          "mode": "multi",
          "sort": "none"
        }
      },
      "pluginVersion": "11.5.1",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "rate(cnpg_pg_stat_database_deadlocks{datname=\"\",namespace=~\"$namespace\",pod=~\"$instances\"}[5m])",
          "hide": false,
          "instant": false,
          "interval": "",
          "legendFormat": "count ({{pod}})",
          "refId": "B"
        }
      ],
      "title": "Deadlocks [5m]",
      "type": "timeseries"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "description": "",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "palette-classic"
          },
          "custom": {
            "axisBorderShow": false,
            "axisCenteredZero": false,
            "axisColorMode": "text",
            "axisLabel": "",
            "axisPlacement": "auto",
            "barAlignment": 0,
            "barWidthFactor": 0.6,
            "drawStyle": "line",
            "fillOpacity": 30,
            "gradientMode": "opacity",
            "hideFrom": {
              "legend": false,
              "tooltip": false,
              "viz": false
            },
            "insertNulls": false,
            "lineInterpolation": "linear",
            "lineWidth": 1,
            "pointSize": 5,
            "scaleDistribution": {
              "type": "linear"
            },
            "showPoints": "never",
            "spanNulls": true,
            "stacking": {
              "group": "A",
              "mode": "none"
            },
            "thresholdsStyle": {
              "mode": "off"
            }
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green"
              },
              {
                "color": "red",
                "value": 80
              }
            ]
          }
        },
        "overrides": []
      },
      "gridPos": {
        "h": 8,
        "w": 12,
        "x": 12,
        "y": 100
      },
      "id": 54,
      "options": {
        "legend": {
          "calcs": [],
          "displayMode": "list",
          "placement": "bottom",
          "showLegend": true
        },
        "tooltip": {
          "hideZeros": false,
          "mode": "multi",
          "sort": "none"
        }
      },
      "pluginVersion": "11.5.1",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "cnpg_backends_waiting_total{namespace=~\"$namespace\",pod=~\"$instances\"}",
          "interval": "",
          "legendFormat": "{{pod}}",
          "refId": "A"
        }
      ],
      "title": "Blocked Queries",
      "type": "timeseries"
    },
    {
      "collapsed": false,
      "gridPos": {
        "h": 1,
        "w": 24,
        "x": 0,
        "y": 108
      },
      "id": 822,
      "panels": [],
      "title": "PG Stat Activity Statistics",
      "type": "row"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "description": "Number of queries running for longer than 30s",
      "fieldConfig": {
        "defaults": {
          "custom": {
            "hideFrom": {
              "legend": false,
              "tooltip": false,
              "viz": false
            },
            "scaleDistribution": {
              "type": "linear"
            }
          }
        },
        "overrides": []
      },
      "gridPos": {
        "h": 8,
        "w": 12,
        "x": 0,
        "y": 109
      },
      "id": 825,
      "maxDataPoints": 80,
      "options": {
        "calculate": false,
        "cellGap": 1,
        "color": {
          "exponent": 0.5,
          "fill": "dark-orange",
          "mode": "scheme",
          "reverse": false,
          "scale": "exponential",
          "scheme": "RdYlBu",
          "steps": 64
        },
        "exemplars": {
          "color": "rgba(255,0,255,0.7)"
        },
        "filterValues": {
          "le": 1e-9
        },
        "legend": {
          "show": true
        },
        "rowsFrame": {
          "layout": "auto"
        },
        "tooltip": {
          "mode": "single",
          "showColorScale": false,
          "yHistogram": false
        },
        "yAxis": {
          "axisPlacement": "left",
          "reverse": false
        }
      },
      "pluginVersion": "11.5.1",
      "targets": [
        {
          "editorMode": "code",
          "expr": "avg(cnpg_pg_stat_activity_long_running_queries_bucket{namespace=\"$namespace\"}) by (le)",
          "format": "heatmap",
          "legendFormat": "Count",
          "range": true,
          "refId": "A"
        }
      ],
      "title": "Long running queries",
      "type": "heatmap"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "description": "Number of queries running for longer than 30s",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "palette-classic"
          },
          "custom": {
            "axisBorderShow": false,
            "axisCenteredZero": false,
            "axisColorMode": "text",
            "axisLabel": "",
            "axisPlacement": "auto",
            "barAlignment": 0,
            "barWidthFactor": 0.6,
            "drawStyle": "line",
            "fillOpacity": 30,
            "gradientMode": "opacity",
            "hideFrom": {
              "legend": false,
              "tooltip": false,
              "viz": false
            },
            "insertNulls": false,
            "lineInterpolation": "linear",
            "lineWidth": 1,
            "pointSize": 5,
            "scaleDistribution": {
              "type": "linear"
            },
            "showPoints": "auto",
            "spanNulls": false,
            "stacking": {
              "group": "A",
              "mode": "none"
            },
            "thresholdsStyle": {
              "mode": "off"
            }
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green"
              },
              {
                "color": "red",
                "value": 80
              }
            ]
          }
        },
        "overrides": []
      },
      "gridPos": {
        "h": 8,
        "w": 6,
        "x": 12,
        "y": 109
      },
      "id": 823,
      "options": {
        "legend": {
          "calcs": [],
          "displayMode": "list",
          "placement": "bottom",
          "showLegend": true
        },
        "tooltip": {
          "hideZeros": false,
          "mode": "multi",
          "sort": "none"
        }
      },
      "pluginVersion": "11.5.1",
      "targets": [
        {
          "editorMode": "code",
          "expr": "max(cnpg_pg_stat_activity_long_running_count * on (pod) group_left() (label_replace(kube_customresource_primary_info{customresource_group=\"postgresql.cnpg.io\", customresource_kind=\"Cluster\", namespace=\"$namespace\"}, \"pod\", \"$1\", \"current_primary\", \"(.*)\")))",
          "legendFormat": "Count",
          "range": true,
          "refId": "A"
        }
      ],
      "title": "Long running queries",
      "type": "timeseries"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "description": "Age of queries running for longer than 30s",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "palette-classic"
          },
          "custom": {
            "axisBorderShow": false,
            "axisCenteredZero": false,
            "axisColorMode": "text",
            "axisLabel": "",
            "axisPlacement": "auto",
            "barAlignment": 0,
            "barWidthFactor": 0.6,
            "drawStyle": "line",
            "fillOpacity": 30,
            "gradientMode": "opacity",
            "hideFrom": {
              "legend": false,
              "tooltip": false,
              "viz": false
            },
            "insertNulls": false,
            "lineInterpolation": "linear",
            "lineWidth": 1,
            "pointSize": 5,
            "scaleDistribution": {
              "type": "linear"
            },
            "showPoints": "auto",
            "spanNulls": false,
            "stacking": {
              "group": "A",
              "mode": "none"
            },
            "thresholdsStyle": {
              "mode": "off"
            }
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green"
              },
              {
                "color": "red",
                "value": 80
              }
            ]
          },
          "unit": "s"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 8,
        "w": 6,
        "x": 18,
        "y": 109
      },
      "id": 824,
      "options": {
        "legend": {
          "calcs": [],
          "displayMode": "list",
          "placement": "bottom",
          "showLegend": true
        },
        "tooltip": {
          "hideZeros": false,
          "mode": "multi",
          "sort": "none"
        }
      },
      "pluginVersion": "11.5.1",
      "targets": [
        {
          "editorMode": "code",
          "expr": "max(cnpg_pg_stat_activity_long_running_max_duration * on (pod) group_left() (label_replace(kube_customresource_primary_info{customresource_group=\"postgresql.cnpg.io\", customresource_kind=\"Cluster\", namespace=\"$namespace\"}, \"pod\", \"$1\", \"current_primary\", \"(.*)\")))",
          "legendFormat": "Maximum",
          "range": true,
          "refId": "A"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "editorMode": "code",
          "expr": "max(cnpg_pg_stat_activity_long_running_avg_duration * on (pod) group_left() (label_replace(kube_customresource_primary_info{customresource_group=\"postgresql.cnpg.io\", customresource_kind=\"Cluster\", namespace=\"$namespace\"}, \"pod\", \"$1\", \"current_primary\", \"(.*)\")))",
          "hide": false,
          "instant": false,
          "legendFormat": "Average",
          "range": true,
          "refId": "B"
        }
      ],
      "title": "Long running queries duration",
      "type": "timeseries"
    },
    {
      "collapsed": false,
      "gridPos": {
        "h": 1,
        "w": 24,
        "x": 0,
        "y": 117
      },
      "id": 35,
      "panels": [],
      "title": "Storage I/O",
      "type": "row"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "description": "",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "palette-classic"
          },
          "custom": {
            "axisBorderShow": false,
            "axisCenteredZero": false,
            "axisColorMode": "text",
            "axisLabel": "",
            "axisPlacement": "auto",
            "barAlignment": 0,
            "barWidthFactor": 0.6,
            "drawStyle": "line",
            "fillOpacity": 100,
            "gradientMode": "opacity",
            "hideFrom": {
              "legend": false,
              "tooltip": false,
              "viz": false
            },
            "insertNulls": false,
            "lineInterpolation": "linear",
            "lineWidth": 1,
            "pointSize": 5,
            "scaleDistribution": {
              "type": "linear"
            },
            "showPoints": "auto",
            "spanNulls": false,
            "stacking": {
              "group": "A",
              "mode": "none"
            },
            "thresholdsStyle": {
              "mode": "off"
            }
          },
          "decimals": 2,
          "mappings": [],
          "min": 0,
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green"
              }
            ]
          },
          "unit": "decbytes"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 8,
        "w": 7,
        "x": 0,
        "y": 118
      },
      "id": 816,
      "options": {
        "legend": {
          "calcs": [],
          "displayMode": "list",
          "placement": "bottom",
          "showLegend": true
        },
        "tooltip": {
          "hideZeros": false,
          "mode": "multi",
          "sort": "none"
        }
      },
      "pluginVersion": "11.5.1",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "editorMode": "code",
          "exemplar": false,
          "expr": "max by (datname) (cnpg_pg_database_size_bytes{namespace=\"$namespace\", pod=~\"$instances\"})",
          "format": "time_series",
          "instant": false,
          "legendFormat": "__auto",
          "range": true,
          "refId": "A"
        }
      ],
      "title": "Database Size",
      "type": "timeseries"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "description": "Based on the data from the last 24h",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "decimals": 2,
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "blue"
              }
            ]
          },
          "unit": "decbytes"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 4,
        "w": 5,
        "x": 7,
        "y": 118
      },
      "id": 817,
      "options": {
        "colorMode": "value",
        "graphMode": "area",
        "justifyMode": "auto",
        "orientation": "auto",
        "percentChangeColorMode": "standard",
        "reduceOptions": {
          "calcs": [
            "lastNotNull"
          ],
          "fields": "",
          "values": false
        },
        "showPercentChange": false,
        "textMode": "auto",
        "wideLayout": true
      },
      "pluginVersion": "11.5.1",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "editorMode": "code",
          "exemplar": false,
          "expr": "max by (datname) (delta( cnpg_pg_database_size_bytes{datname!~\"template.*\", datname!=\"postgres\", namespace=\"$namespace\",job=\"$namespace/$cluster\"}[$__range]))",
          "format": "time_series",
          "instant": true,
          "legendFormat": "__auto",
          "range": false,
          "refId": "A"
        }
      ],
      "timeFrom": "24h",
      "title": "Δsize / month",
      "type": "stat"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "palette-classic"
          },
          "custom": {
            "axisBorderShow": false,
            "axisCenteredZero": false,
            "axisColorMode": "text",
            "axisLabel": "",
            "axisPlacement": "auto",
            "barAlignment": 0,
            "barWidthFactor": 0.6,
            "drawStyle": "line",
            "fillOpacity": 30,
            "gradientMode": "opacity",
            "hideFrom": {
              "legend": false,
              "tooltip": false,
              "viz": false
            },
            "insertNulls": false,
            "lineInterpolation": "linear",
            "lineWidth": 1,
            "pointSize": 5,
            "scaleDistribution": {
              "type": "linear"
            },
            "showPoints": "auto",
            "spanNulls": false,
            "stacking": {
              "group": "A",
              "mode": "none"
            },
            "thresholdsStyle": {
              "mode": "off"
            }
          },
          "mappings": [],
          "max": 1,
          "min": 0,
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green"
              },
              {
                "color": "#EAB839",
                "value": 0.7
              },
              {
                "color": "red",
                "value": 0.8
              }
            ]
          },
          "unit": "percentunit"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 8,
        "w": 12,
        "x": 12,
        "y": 118
      },
      "id": 424,
      "options": {
        "legend": {
          "calcs": [],
          "displayMode": "list",
          "placement": "bottom",
          "showLegend": true
        },
        "tooltip": {
          "hideZeros": false,
          "mode": "multi",
          "sort": "none"
        }
      },
      "pluginVersion": "11.5.1",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "editorMode": "code",
          "expr": "max by(persistentvolumeclaim, volume) (1 - kubelet_volume_stats_available_bytes{namespace=\"$namespace\", persistentvolumeclaim=~\"$instances.*\"} / kubelet_volume_stats_capacity_bytes * on(namespace, persistentvolumeclaim) group_left(volume,pod) kube_pod_spec_volumes_persistentvolumeclaims_info)",
          "format": "time_series",
          "interval": "",
          "legendFormat": "{{persistentvolumeclaim}} ({{volume}})",
          "range": true,
          "refId": "FREE_SPACE"
        }
      ],
      "title": "Volume Space Usage",
      "type": "timeseries"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "description": "Based on the data from the last 7d",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "decimals": 2,
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "blue"
              }
            ]
          },
          "unit": "decbytes"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 4,
        "w": 5,
        "x": 7,
        "y": 122
      },
      "id": 818,
      "options": {
        "colorMode": "value",
        "graphMode": "area",
        "justifyMode": "auto",
        "orientation": "auto",
        "percentChangeColorMode": "standard",
        "reduceOptions": {
          "calcs": [
            "lastNotNull"
          ],
          "fields": "",
          "values": false
        },
        "showPercentChange": false,
        "textMode": "auto",
        "wideLayout": true
      },
      "pluginVersion": "11.5.1",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "editorMode": "code",
          "exemplar": false,
          "expr": "max by (datname) (delta( cnpg_pg_database_size_bytes{datname!~\"template.*\", datname!=\"postgres\", namespace=\"$namespace\",job=\"$namespace/$cluster\"}[$__range]))",
          "format": "time_series",
          "instant": true,
          "legendFormat": "__auto",
          "range": false,
          "refId": "A"
        }
      ],
      "timeFrom": "7d",
      "title": "Δsize / month",
      "type": "stat"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "custom": {
            "align": "auto",
            "cellOptions": {
              "type": "auto"
            },
            "inspect": false
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green"
              },
              {
                "color": "red",
                "value": 80
              }
            ]
          }
        },
        "overrides": [
          {
            "matcher": {
              "id": "byName",
              "options": "persistentvolumeclaim"
            },
            "properties": [
              {
                "id": "custom.width",
                "value": 300
              }
            ]
          },
          {
            "matcher": {
              "id": "byName",
              "options": ""
            },
            "properties": []
          },
          {
            "matcher": {
              "id": "byName",
              "options": "Provisioner"
            },
            "properties": [
              {
                "id": "custom.width",
                "value": 214
              }
            ]
          },
          {
            "matcher": {
              "id": "byName",
              "options": "Reclaim Policy"
            },
            "properties": [
              {
                "id": "custom.width",
                "value": 119
              },
              {
                "id": "custom.cellOptions",
                "value": {
                  "type": "color-text"
                }
              },
              {
                "id": "mappings",
                "value": [
                  {
                    "options": {
                      "Delete": {
                        "color": "red",
                        "index": 1
                      },
                      "Retain": {
                        "color": "green",
                        "index": 0
                      }
                    },
                    "type": "value"
                  }
                ]
              }
            ]
          },
          {
            "matcher": {
              "id": "byName",
              "options": "PVC Name"
            },
            "properties": [
              {
                "id": "custom.width",
                "value": 276
              }
            ]
          }
        ]
      },
      "gridPos": {
        "h": 8,
        "w": 12,
        "x": 0,
        "y": 126
      },
      "id": 819,
      "options": {
        "cellHeight": "sm",
        "footer": {
          "countRows": false,
          "fields": "",
          "reducer": [
            "sum"
          ],
          "show": false
        },
        "showHeader": true,
        "sortBy": []
      },
      "pluginVersion": "11.5.1",
      "targets": [
        {
          "editorMode": "code",
          "exemplar": false,
          "expr": "kube_persistentvolumeclaim_info{namespace=\"$namespace\"} * on (storageclass) group_left(reclaim_policy, provisioner, volume_binding_mode) kube_storageclass_info",
          "format": "table",
          "instant": true,
          "legendFormat": "__auto",
          "range": false,
          "refId": "A"
        }
      ],
      "title": "Storage Classes",
      "transformations": [
        {
          "id": "organize",
          "options": {
            "excludeByName": {
              "Time": true,
              "Value": true,
              "container": true,
              "endpoint": true,
              "instance": true,
              "job": true,
              "namespace": true,
              "persistentvolumeclaim": false,
              "pod": true,
              "prometheus": true,
              "provisioner": false,
              "reclaim_policy": false,
              "service": true,
              "storageclass": false,
              "volume_binding_mode": false,
              "volumemode": true,
              "volumename": true
            },
            "includeByName": {},
            "indexByName": {},
            "renameByName": {
              "persistentvolumeclaim": "PVC Name",
              "provisioner": "Provisioner",
              "reclaim_policy": "Reclaim Policy",
              "storageclass": "Storage Class",
              "volume_binding_mode": "Volume Binding mode"
            }
          }
        }
      ],
      "type": "table"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "description": "Represents that Inode usage of your filesystem. Reaching the limit will result in data loss and downtime. This number may be shown as 0.00% even with terrabytes of data on disk which is normal.",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "palette-classic"
          },
          "custom": {
            "axisBorderShow": false,
            "axisCenteredZero": false,
            "axisColorMode": "text",
            "axisLabel": "",
            "axisPlacement": "auto",
            "barAlignment": 0,
            "barWidthFactor": 0.6,
            "drawStyle": "line",
            "fillOpacity": 30,
            "gradientMode": "opacity",
            "hideFrom": {
              "legend": false,
              "tooltip": false,
              "viz": false
            },
            "insertNulls": false,
            "lineInterpolation": "linear",
            "lineWidth": 1,
            "pointSize": 5,
            "scaleDistribution": {
              "type": "linear"
            },
            "showPoints": "auto",
            "spanNulls": false,
            "stacking": {
              "group": "A",
              "mode": "none"
            },
            "thresholdsStyle": {
              "mode": "off"
            }
          },
          "decimals": 2,
          "mappings": [],
          "max": 1,
          "min": 0,
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green"
              },
              {
                "color": "#EAB839",
                "value": 0.8
              },
              {
                "color": "red",
                "value": 0.9
              }
            ]
          },
          "unit": "percentunit"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 8,
        "w": 12,
        "x": 12,
        "y": 126
      },
      "id": 426,
      "options": {
        "legend": {
          "calcs": [],
          "displayMode": "list",
          "placement": "bottom",
          "showLegend": true
        },
        "tooltip": {
          "hideZeros": false,
          "mode": "multi",
          "sort": "none"
        }
      },
      "pluginVersion": "11.5.1",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "editorMode": "code",
          "expr": "max by(persistentvolumeclaim) (kubelet_volume_stats_inodes_used{namespace=\"$namespace\", persistentvolumeclaim=~\"$instances.*\"} / kubelet_volume_stats_inodes * on(namespace, persistentvolumeclaim) group_left(volume,pod) kube_pod_spec_volumes_persistentvolumeclaims_info)",
          "format": "time_series",
          "interval": "",
          "legendFormat": "{{persistentvolumeclaim}}",
          "range": true,
          "refId": "FREE_INODES"
        }
      ],
      "title": "Volume Inode Usage",
      "type": "timeseries"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "description": "",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "palette-classic"
          },
          "custom": {
            "axisBorderShow": false,
            "axisCenteredZero": false,
            "axisColorMode": "text",
            "axisLabel": "",
            "axisPlacement": "auto",
            "barAlignment": 0,
            "barWidthFactor": 0.6,
            "drawStyle": "line",
            "fillOpacity": 30,
            "gradientMode": "opacity",
            "hideFrom": {
              "legend": false,
              "tooltip": false,
              "viz": false
            },
            "insertNulls": false,
            "lineInterpolation": "linear",
            "lineWidth": 1,
            "pointSize": 5,
            "scaleDistribution": {
              "type": "linear"
            },
            "showPoints": "never",
            "spanNulls": false,
            "stacking": {
              "group": "A",
              "mode": "normal"
            },
            "thresholdsStyle": {
              "mode": "off"
            }
          },
          "decimals": 2,
          "mappings": [],
          "min": 0,
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green"
              }
            ]
          },
          "unit": "bytes"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 8,
        "w": 12,
        "x": 0,
        "y": 134
      },
      "id": 829,
      "options": {
        "legend": {
          "calcs": [],
          "displayMode": "list",
          "placement": "bottom",
          "showLegend": true
        },
        "tooltip": {
          "hideZeros": false,
          "mode": "multi",
          "sort": "none"
        }
      },
      "pluginVersion": "11.5.1",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "editorMode": "code",
          "exemplar": false,
          "expr": "rate(sum by (instance) (node_disk_read_bytes_total) * on(instance) group_left(nodename) node_uname_info) * on(nodename) group_left(pod) label_replace(kube_pod_info{pod=~\"$instances\", namespace=\"$namespace\"}, \"nodename\", \"$1\", \"node\", \"(.*)\")",
          "format": "time_series",
          "interval": "",
          "legendFormat": "{{pod}}",
          "range": true,
          "refId": "A"
        }
      ],
      "title": "Disk IO (Read)",
      "type": "timeseries"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "description": "",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "palette-classic"
          },
          "custom": {
            "axisBorderShow": false,
            "axisCenteredZero": false,
            "axisColorMode": "text",
            "axisLabel": "",
            "axisPlacement": "auto",
            "barAlignment": 0,
            "barWidthFactor": 0.6,
            "drawStyle": "line",
            "fillOpacity": 30,
            "gradientMode": "opacity",
            "hideFrom": {
              "legend": false,
              "tooltip": false,
              "viz": false
            },
            "insertNulls": false,
            "lineInterpolation": "linear",
            "lineWidth": 1,
            "pointSize": 5,
            "scaleDistribution": {
              "type": "linear"
            },
            "showPoints": "never",
            "spanNulls": false,
            "stacking": {
              "group": "A",
              "mode": "normal"
            },
            "thresholdsStyle": {
              "mode": "off"
            }
          },
          "decimals": 2,
          "mappings": [],
          "min": 0,
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green"
              }
            ]
          },
          "unit": "bytes"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 8,
        "w": 12,
        "x": 12,
        "y": 134
      },
      "id": 830,
      "options": {
        "legend": {
          "calcs": [],
          "displayMode": "list",
          "placement": "bottom",
          "showLegend": true
        },
        "tooltip": {
          "hideZeros": false,
          "mode": "multi",
          "sort": "none"
        }
      },
      "pluginVersion": "11.5.1",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "editorMode": "code",
          "exemplar": false,
          "expr": "rate(sum by (instance) (node_disk_written_bytes_total) * on(instance) group_left(nodename) node_uname_info) * on(nodename) group_left(pod) label_replace(kube_pod_info{pod=~\"$instances\", namespace=\"$namespace\"}, \"nodename\", \"$1\", \"node\", \"(.*)\")",
          "format": "time_series",
          "interval": "",
          "legendFormat": "{{pod}}",
          "range": true,
          "refId": "A"
        }
      ],
      "title": "Disk IO (Write)",
      "type": "timeseries"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "description": "Aggregation over large periods of time introduces inaccuracies. Zoom in to periods you are interested in for accurate results.",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "palette-classic"
          },
          "custom": {
            "axisBorderShow": false,
            "axisCenteredZero": false,
            "axisColorMode": "text",
            "axisLabel": "",
            "axisPlacement": "auto",
            "barAlignment": 0,
            "barWidthFactor": 0.6,
            "drawStyle": "line",
            "fillOpacity": 30,
            "gradientMode": "opacity",
            "hideFrom": {
              "legend": false,
              "tooltip": false,
              "viz": false
            },
            "insertNulls": false,
            "lineInterpolation": "linear",
            "lineWidth": 1,
            "pointSize": 5,
            "scaleDistribution": {
              "type": "linear"
            },
            "showPoints": "never",
            "spanNulls": false,
            "stacking": {
              "group": "A",
              "mode": "normal"
            },
            "thresholdsStyle": {
              "mode": "off"
            }
          },
          "decimals": 2,
          "mappings": [],
          "min": 0,
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green"
              }
            ]
          },
          "unit": "none"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 8,
        "w": 12,
        "x": 0,
        "y": 142
      },
      "id": 833,
      "options": {
        "legend": {
          "calcs": [],
          "displayMode": "list",
          "placement": "bottom",
          "showLegend": true
        },
        "tooltip": {
          "hideZeros": false,
          "mode": "multi",
          "sort": "none"
        }
      },
      "pluginVersion": "11.5.1",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "editorMode": "code",
          "exemplar": false,
          "expr": "max by (customer,instance) (max_over_time(rate(node_disk_reads_completed_total+node_disk_writes_completed_total)[$__rate_interval])[$__interval]) * on(instance,customer) group_left(nodename) node_uname_info{} * on(customer,nodename) group_left(pod) label_replace(kube_pod_info{pod=~\"$cluster-([1-9][0-9]*)$\", namespace=\"$namespace\"}, \"nodename\", \"$1\", \"node\", \"(.*)\")",
          "format": "time_series",
          "interval": "",
          "legendFormat": "{{pod}}",
          "range": true,
          "refId": "A"
        }
      ],
      "title": "Disk IOPS",
      "type": "timeseries"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "palette-classic"
          },
          "custom": {
            "axisBorderShow": false,
            "axisCenteredZero": false,
            "axisColorMode": "text",
            "axisLabel": "",
            "axisPlacement": "auto",
            "barAlignment": 0,
            "barWidthFactor": 0.6,
            "drawStyle": "line",
            "fillOpacity": 30,
            "gradientMode": "opacity",
            "hideFrom": {
              "legend": false,
              "tooltip": false,
              "viz": false
            },
            "insertNulls": false,
            "lineInterpolation": "linear",
            "lineWidth": 1,
            "pointSize": 5,
            "scaleDistribution": {
              "type": "linear"
            },
            "showPoints": "never",
            "spanNulls": true,
            "stacking": {
              "group": "A",
              "mode": "none"
            },
            "thresholdsStyle": {
              "mode": "off"
            }
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green"
              },
              {
                "color": "red",
                "value": 80
              }
            ]
          }
        },
        "overrides": []
      },
      "gridPos": {
        "h": 8,
        "w": 12,
        "x": 12,
        "y": 142
      },
      "id": 46,
      "options": {
        "legend": {
          "calcs": [],
          "displayMode": "list",
          "placement": "bottom",
          "showLegend": true
        },
        "tooltip": {
          "hideZeros": false,
          "mode": "multi",
          "sort": "none"
        }
      },
      "pluginVersion": "11.5.1",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "editorMode": "code",
          "exemplar": true,
          "expr": "rate(cnpg_pg_stat_database_blks_hit{datname=\"\",namespace=~\"$namespace\",pod=~\"$instances\"}[5m])",
          "interval": "",
          "legendFormat": "hit ({{pod}})",
          "range": true,
          "refId": "A"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "editorMode": "code",
          "exemplar": true,
          "expr": "rate(cnpg_pg_stat_database_blks_read{datname=\"\",namespace=~\"$namespace\",pod=~\"$instances\"}[5m])",
          "hide": false,
          "interval": "",
          "legendFormat": "read ({{pod}})",
          "range": true,
          "refId": "B"
        }
      ],
      "title": "Block I/O [5m]",
      "type": "timeseries"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "palette-classic"
          },
          "custom": {
            "axisBorderShow": false,
            "axisCenteredZero": false,
            "axisColorMode": "text",
            "axisLabel": "",
            "axisPlacement": "auto",
            "barAlignment": 0,
            "barWidthFactor": 0.6,
            "drawStyle": "line",
            "fillOpacity": 30,
            "gradientMode": "opacity",
            "hideFrom": {
              "legend": false,
              "tooltip": false,
              "viz": false
            },
            "insertNulls": false,
            "lineInterpolation": "linear",
            "lineWidth": 1,
            "pointSize": 5,
            "scaleDistribution": {
              "type": "linear"
            },
            "showPoints": "never",
            "spanNulls": true,
            "stacking": {
              "group": "A",
              "mode": "none"
            },
            "thresholdsStyle": {
              "mode": "off"
            }
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green"
              },
              {
                "color": "red",
                "value": 80
              }
            ]
          }
        },
        "overrides": []
      },
      "gridPos": {
        "h": 8,
        "w": 12,
        "x": 0,
        "y": 150
      },
      "id": 44,
      "options": {
        "legend": {
          "calcs": [],
          "displayMode": "list",
          "placement": "bottom",
          "showLegend": true
        },
        "tooltip": {
          "hideZeros": false,
          "mode": "multi",
          "sort": "none"
        }
      },
      "pluginVersion": "11.5.1",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "editorMode": "code",
          "exemplar": true,
          "expr": "sum(rate(cnpg_pg_stat_database_tup_deleted{datname=\"\",namespace=~\"$namespace\",pod=~\"$instances\"}[5m]))",
          "interval": "",
          "legendFormat": "deleted",
          "range": true,
          "refId": "A"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "editorMode": "code",
          "exemplar": true,
          "expr": "sum(rate(cnpg_pg_stat_database_tup_inserted{datname=\"\",namespace=~\"$namespace\",pod=~\"$instances\"}[5m]))",
          "hide": false,
          "interval": "",
          "legendFormat": "inserted",
          "range": true,
          "refId": "B"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "editorMode": "code",
          "exemplar": true,
          "expr": "sum(rate(cnpg_pg_stat_database_tup_fetched{datname=\"\",namespace=~\"$namespace\",pod=~\"$instances\"}[5m]))",
          "hide": false,
          "interval": "",
          "legendFormat": "fetched",
          "range": true,
          "refId": "C"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "editorMode": "code",
          "exemplar": true,
          "expr": "sum(rate(cnpg_pg_stat_database_tup_returned{datname=\"\",namespace=~\"$namespace\",pod=~\"$instances\"}[5m]))",
          "hide": false,
          "interval": "",
          "legendFormat": "returned",
          "range": true,
          "refId": "D"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "editorMode": "code",
          "exemplar": true,
          "expr": "sum(rate(cnpg_pg_stat_database_tup_updated{datname=\"\",namespace=~\"$namespace\",pod=~\"$instances\"}[5m]))",
          "hide": false,
          "interval": "",
          "legendFormat": "updated",
          "range": true,
          "refId": "E"
        }
      ],
      "title": "Tuple I/O [5m]",
      "type": "timeseries"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "palette-classic"
          },
          "custom": {
            "axisBorderShow": false,
            "axisCenteredZero": false,
            "axisColorMode": "text",
            "axisLabel": "",
            "axisPlacement": "auto",
            "barAlignment": 0,
            "barWidthFactor": 0.6,
            "drawStyle": "line",
            "fillOpacity": 30,
            "gradientMode": "opacity",
            "hideFrom": {
              "legend": false,
              "tooltip": false,
              "viz": false
            },
            "insertNulls": false,
            "lineInterpolation": "linear",
            "lineWidth": 1,
            "pointSize": 5,
            "scaleDistribution": {
              "type": "linear"
            },
            "showPoints": "never",
            "spanNulls": true,
            "stacking": {
              "group": "A",
              "mode": "none"
            },
            "thresholdsStyle": {
              "mode": "off"
            }
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green"
              },
              {
                "color": "red",
                "value": 80
              }
            ]
          },
          "unit": "decbytes"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 8,
        "w": 12,
        "x": 12,
        "y": 150
      },
      "id": 2,
      "options": {
        "legend": {
          "calcs": [],
          "displayMode": "list",
          "placement": "bottom",
          "showLegend": true
        },
        "tooltip": {
          "hideZeros": false,
          "mode": "multi",
          "sort": "none"
        }
      },
      "pluginVersion": "11.5.1",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "rate(cnpg_pg_stat_database_temp_bytes{datname=\"\",namespace=~\"$namespace\",pod=~\"$instances\"}[5m])",
          "instant": false,
          "interval": "",
          "legendFormat": "{{pod}}",
          "refId": "A"
        }
      ],
      "title": "Temp Bytes [5m]",
      "type": "timeseries"
    },
    {
      "collapsed": false,
      "gridPos": {
        "h": 1,
        "w": 24,
        "x": 0,
        "y": 158
      },
      "id": 827,
      "panels": [],
      "title": "Network I/O",
      "type": "row"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "palette-classic"
          },
          "custom": {
            "axisBorderShow": false,
            "axisCenteredZero": false,
            "axisColorMode": "text",
            "axisLabel": "",
            "axisPlacement": "auto",
            "barAlignment": 0,
            "barWidthFactor": 0.6,
            "drawStyle": "line",
            "fillOpacity": 30,
            "gradientMode": "opacity",
            "hideFrom": {
              "legend": false,
              "tooltip": false,
              "viz": false
            },
            "insertNulls": false,
            "lineInterpolation": "linear",
            "lineWidth": 2,
            "pointSize": 5,
            "scaleDistribution": {
              "type": "linear"
            },
            "showPoints": "auto",
            "spanNulls": false,
            "stacking": {
              "group": "A",
              "mode": "none"
            },
            "thresholdsStyle": {
              "mode": "off"
            }
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green"
              }
            ]
          },
          "unit": "bytes"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 10,
        "w": 24,
        "x": 0,
        "y": 159
      },
      "id": 828,
      "options": {
        "legend": {
          "calcs": [],
          "displayMode": "list",
          "placement": "bottom",
          "showLegend": true
        },
        "tooltip": {
          "hideZeros": false,
          "mode": "multi",
          "sort": "none"
        }
      },
      "pluginVersion": "11.5.1",
      "repeat": "nodes",
      "repeatDirection": "h",
      "targets": [
        {
          "editorMode": "code",
          "expr": "sum by (node) (rate(container_network_receive_bytes_total{}[$__rate_interval])) * on(node) group_left(pod) kube_pod_info{namespace=~\"$namespace\", pod=~\"$instances\", node=\"$nodes\"}",
          "legendFormat": "{{node}} ({{pod}}) (RX)",
          "range": true,
          "refId": "RX"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "editorMode": "code",
          "expr": "- sum by (node) (rate(container_network_transmit_bytes_total{}[$__rate_interval])) * on(node) group_left(pod) kube_pod_info{namespace=~\"$namespace\", pod=~\"$instances\", node=\"$nodes\"}",
          "hide": false,
          "instant": false,
          "legendFormat": "{{node}} ({{pod}}) (TX)",
          "range": true,
          "refId": "TX"
        }
      ],
      "title": "Network Throughout: $nodes",
      "type": "timeseries"
    },
    {
      "collapsed": false,
      "gridPos": {
        "h": 1,
        "w": 24,
        "x": 0,
        "y": 169
      },
      "id": 37,
      "panels": [],
      "title": "Write Ahead Logs",
      "type": "row"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "palette-classic"
          },
          "custom": {
            "axisBorderShow": false,
            "axisCenteredZero": false,
            "axisColorMode": "text",
            "axisLabel": "",
            "axisPlacement": "auto",
            "barAlignment": 0,
            "barWidthFactor": 0.6,
            "drawStyle": "line",
            "fillOpacity": 30,
            "gradientMode": "opacity",
            "hideFrom": {
              "legend": false,
              "tooltip": false,
              "viz": false
            },
            "insertNulls": false,
            "lineInterpolation": "linear",
            "lineWidth": 1,
            "pointSize": 5,
            "scaleDistribution": {
              "type": "linear"
            },
            "showPoints": "never",
            "spanNulls": true,
            "stacking": {
              "group": "A",
              "mode": "none"
            },
            "thresholdsStyle": {
              "mode": "off"
            }
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green"
              },
              {
                "color": "red",
                "value": 80
              }
            ]
          }
        },
        "overrides": []
      },
      "gridPos": {
        "h": 8,
        "w": 8,
        "x": 0,
        "y": 170
      },
      "id": 6,
      "options": {
        "legend": {
          "calcs": [],
          "displayMode": "list",
          "placement": "bottom",
          "showLegend": true
        },
        "tooltip": {
          "hideZeros": false,
          "mode": "multi",
          "sort": "none"
        }
      },
      "pluginVersion": "11.5.1",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "cnpg_collector_pg_wal_archive_status{value=\"ready\",namespace=~\"$namespace\",pod=~\"$instances\"}",
          "interval": "",
          "legendFormat": "ready ({{pod}})",
          "refId": "A"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "cnpg_collector_pg_wal_archive_status{value=\"done\",namespace=~\"$namespace\",pod=~\"$instances\"}",
          "hide": false,
          "interval": "",
          "legendFormat": "done ({{pod}})",
          "refId": "B"
        }
      ],
      "title": "WAL Segment Archive Status",
      "type": "timeseries"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "palette-classic"
          },
          "custom": {
            "axisBorderShow": false,
            "axisCenteredZero": false,
            "axisColorMode": "text",
            "axisLabel": "",
            "axisPlacement": "auto",
            "barAlignment": 0,
            "barWidthFactor": 0.6,
            "drawStyle": "line",
            "fillOpacity": 30,
            "gradientMode": "opacity",
            "hideFrom": {
              "legend": false,
              "tooltip": false,
              "viz": false
            },
            "insertNulls": false,
            "lineInterpolation": "linear",
            "lineWidth": 1,
            "pointSize": 5,
            "scaleDistribution": {
              "type": "linear"
            },
            "showPoints": "never",
            "spanNulls": true,
            "stacking": {
              "group": "A",
              "mode": "none"
            },
            "thresholdsStyle": {
              "mode": "off"
            }
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green"
              },
              {
                "color": "red",
                "value": 80
              }
            ]
          }
        },
        "overrides": []
      },
      "gridPos": {
        "h": 8,
        "w": 8,
        "x": 8,
        "y": 170
      },
      "id": 52,
      "options": {
        "legend": {
          "calcs": [],
          "displayMode": "list",
          "placement": "bottom",
          "showLegend": true
        },
        "tooltip": {
          "hideZeros": false,
          "mode": "multi",
          "sort": "none"
        }
      },
      "pluginVersion": "11.5.1",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "rate(cnpg_pg_stat_archiver_archived_count{namespace=~\"$namespace\",pod=~\"$instances\"}[5m])",
          "interval": "",
          "legendFormat": "archived ({{pod}})",
          "refId": "A"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "rate(cnpg_pg_stat_archiver_failed_count{namespace=~\"$namespace\",pod=~\"$instances\"}[5m])",
          "hide": false,
          "interval": "",
          "legendFormat": "failed ({{pod}})",
          "refId": "B"
        }
      ],
      "title": "Archiver Status [5m]",
      "type": "timeseries"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "description": "",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "palette-classic"
          },
          "custom": {
            "axisBorderShow": false,
            "axisCenteredZero": false,
            "axisColorMode": "text",
            "axisLabel": "",
            "axisPlacement": "auto",
            "barAlignment": 0,
            "barWidthFactor": 0.6,
            "drawStyle": "line",
            "fillOpacity": 30,
            "gradientMode": "opacity",
            "hideFrom": {
              "legend": false,
              "tooltip": false,
              "viz": false
            },
            "insertNulls": false,
            "lineInterpolation": "linear",
            "lineWidth": 1,
            "pointSize": 5,
            "scaleDistribution": {
              "type": "linear"
            },
            "showPoints": "never",
            "spanNulls": true,
            "stacking": {
              "group": "A",
              "mode": "none"
            },
            "thresholdsStyle": {
              "mode": "off"
            }
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green"
              },
              {
                "color": "red",
                "value": 80
              }
            ]
          },
          "unit": "s"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 8,
        "w": 8,
        "x": 16,
        "y": 170
      },
      "id": 53,
      "options": {
        "legend": {
          "calcs": [],
          "displayMode": "list",
          "placement": "bottom",
          "showLegend": true
        },
        "tooltip": {
          "hideZeros": false,
          "mode": "multi",
          "sort": "none"
        }
      },
      "pluginVersion": "11.5.1",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "cnpg_pg_stat_archiver_seconds_since_last_archival{namespace=~\"$namespace\",pod=~\"$instances\"}",
          "interval": "",
          "legendFormat": "age ({{pod}})",
          "refId": "A"
        }
      ],
      "title": "Last Archive Age",
      "type": "timeseries"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "palette-classic"
          },
          "custom": {
            "axisBorderShow": false,
            "axisCenteredZero": false,
            "axisColorMode": "text",
            "axisLabel": "",
            "axisPlacement": "auto",
            "barAlignment": 0,
            "barWidthFactor": 0.6,
            "drawStyle": "line",
            "fillOpacity": 30,
            "gradientMode": "opacity",
            "hideFrom": {
              "legend": false,
              "tooltip": false,
              "viz": false
            },
            "insertNulls": false,
            "lineInterpolation": "linear",
            "lineWidth": 1,
            "pointSize": 5,
            "scaleDistribution": {
              "type": "linear"
            },
            "showPoints": "auto",
            "spanNulls": false,
            "stacking": {
              "group": "A",
              "mode": "none"
            },
            "thresholdsStyle": {
              "mode": "off"
            }
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green"
              },
              {
                "color": "red",
                "value": 80
              }
            ]
          }
        },
        "overrides": []
      },
      "gridPos": {
        "h": 8,
        "w": 8,
        "x": 0,
        "y": 178
      },
      "id": 725,
      "options": {
        "legend": {
          "calcs": [],
          "displayMode": "list",
          "placement": "bottom",
          "showLegend": true
        },
        "tooltip": {
          "hideZeros": false,
          "mode": "single",
          "sort": "none"
        }
      },
      "pluginVersion": "11.5.1",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "editorMode": "code",
          "expr": "cnpg_collector_pg_wal{pod=~\"$instances\", namespace=~\"$namespace\", value=\"count\"}",
          "instant": false,
          "legendFormat": "{{pod}}",
          "range": true,
          "refId": "A"
        }
      ],
      "title": "WAL Count",
      "type": "timeseries"
    },
    {
      "collapsed": false,
      "gridPos": {
        "h": 1,
        "w": 24,
        "x": 0,
        "y": 186
      },
      "id": 18,
      "panels": [],
      "title": "Physical Replication",
      "type": "row"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "palette-classic"
          },
          "custom": {
            "axisBorderShow": false,
            "axisCenteredZero": false,
            "axisColorMode": "text",
            "axisLabel": "",
            "axisPlacement": "auto",
            "barAlignment": 0,
            "barWidthFactor": 0.6,
            "drawStyle": "line",
            "fillOpacity": 30,
            "gradientMode": "opacity",
            "hideFrom": {
              "legend": false,
              "tooltip": false,
              "viz": false
            },
            "insertNulls": false,
            "lineInterpolation": "linear",
            "lineWidth": 1,
            "pointSize": 5,
            "scaleDistribution": {
              "type": "linear"
            },
            "showPoints": "never",
            "spanNulls": true,
            "stacking": {
              "group": "A",
              "mode": "none"
            },
            "thresholdsStyle": {
              "mode": "line"
            }
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green"
              },
              {
                "color": "#EAB839",
                "value": 600
              },
              {
                "color": "dark-red",
                "value": 3600
              }
            ]
          },
          "unit": "s"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 8,
        "w": 6,
        "x": 0,
        "y": 187
      },
      "id": 16,
      "options": {
        "legend": {
          "calcs": [],
          "displayMode": "list",
          "placement": "bottom",
          "showLegend": true
        },
        "tooltip": {
          "hideZeros": false,
          "mode": "multi",
          "sort": "none"
        }
      },
      "pluginVersion": "11.5.1",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "cnpg_pg_replication_lag{namespace=~\"$namespace\",pod=~\"$instances\"}",
          "instant": false,
          "interval": "",
          "legendFormat": "{{pod}}",
          "refId": "A"
        }
      ],
      "title": "Replication Lag",
      "type": "timeseries"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "palette-classic"
          },
          "custom": {
            "axisBorderShow": false,
            "axisCenteredZero": false,
            "axisColorMode": "text",
            "axisLabel": "",
            "axisPlacement": "auto",
            "barAlignment": 0,
            "barWidthFactor": 0.6,
            "drawStyle": "line",
            "fillOpacity": 30,
            "gradientMode": "opacity",
            "hideFrom": {
              "legend": false,
              "tooltip": false,
              "viz": false
            },
            "insertNulls": false,
            "lineInterpolation": "linear",
            "lineWidth": 1,
            "pointSize": 5,
            "scaleDistribution": {
              "type": "linear"
            },
            "showPoints": "never",
            "spanNulls": true,
            "stacking": {
              "group": "A",
              "mode": "none"
            },
            "thresholdsStyle": {
              "mode": "off"
            }
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green"
              },
              {
                "color": "red",
                "value": 80
              }
            ]
          },
          "unit": "s"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 8,
        "w": 6,
        "x": 6,
        "y": 187
      },
      "id": 14,
      "options": {
        "legend": {
          "calcs": [],
          "displayMode": "list",
          "placement": "bottom",
          "showLegend": true
        },
        "tooltip": {
          "hideZeros": false,
          "mode": "multi",
          "sort": "none"
        }
      },
      "pluginVersion": "11.5.1",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "editorMode": "code",
          "exemplar": true,
          "expr": "cnpg_pg_stat_replication_write_lag_seconds{namespace=~\"$namespace\",pod=~\"$instances\"}",
          "instant": false,
          "interval": "",
          "legendFormat": "{{pod}} -> {{application_name}}",
          "refId": "A"
        }
      ],
      "title": "Write Lag",
      "type": "timeseries"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "palette-classic"
          },
          "custom": {
            "axisBorderShow": false,
            "axisCenteredZero": false,
            "axisColorMode": "text",
            "axisLabel": "",
            "axisPlacement": "auto",
            "barAlignment": 0,
            "barWidthFactor": 0.6,
            "drawStyle": "line",
            "fillOpacity": 30,
            "gradientMode": "opacity",
            "hideFrom": {
              "legend": false,
              "tooltip": false,
              "viz": false
            },
            "insertNulls": false,
            "lineInterpolation": "linear",
            "lineWidth": 1,
            "pointSize": 5,
            "scaleDistribution": {
              "type": "linear"
            },
            "showPoints": "never",
            "spanNulls": true,
            "stacking": {
              "group": "A",
              "mode": "none"
            },
            "thresholdsStyle": {
              "mode": "off"
            }
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green"
              },
              {
                "color": "red",
                "value": 80
              }
            ]
          },
          "unit": "s"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 8,
        "w": 6,
        "x": 12,
        "y": 187
      },
      "id": 59,
      "options": {
        "legend": {
          "calcs": [],
          "displayMode": "list",
          "placement": "bottom",
          "showLegend": true
        },
        "tooltip": {
          "hideZeros": false,
          "mode": "multi",
          "sort": "none"
        }
      },
      "pluginVersion": "11.5.1",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "editorMode": "code",
          "exemplar": true,
          "expr": "cnpg_pg_stat_replication_flush_lag_seconds{namespace=~\"$namespace\",pod=~\"$instances\"}",
          "instant": false,
          "interval": "",
          "legendFormat": "{{pod}} -> {{application_name}}",
          "refId": "A"
        }
      ],
      "title": "Flush Lag",
      "type": "timeseries"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "description": "",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "palette-classic"
          },
          "custom": {
            "axisBorderShow": false,
            "axisCenteredZero": false,
            "axisColorMode": "text",
            "axisLabel": "",
            "axisPlacement": "auto",
            "barAlignment": 0,
            "barWidthFactor": 0.6,
            "drawStyle": "line",
            "fillOpacity": 30,
            "gradientMode": "opacity",
            "hideFrom": {
              "legend": false,
              "tooltip": false,
              "viz": false
            },
            "insertNulls": false,
            "lineInterpolation": "linear",
            "lineWidth": 1,
            "pointSize": 5,
            "scaleDistribution": {
              "type": "linear"
            },
            "showPoints": "never",
            "spanNulls": true,
            "stacking": {
              "group": "A",
              "mode": "none"
            },
            "thresholdsStyle": {
              "mode": "off"
            }
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green"
              },
              {
                "color": "red",
                "value": 80
              }
            ]
          },
          "unit": "s"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 8,
        "w": 6,
        "x": 18,
        "y": 187
      },
      "id": 20,
      "options": {
        "legend": {
          "calcs": [],
          "displayMode": "list",
          "placement": "bottom",
          "showLegend": true
        },
        "tooltip": {
          "hideZeros": false,
          "mode": "multi",
          "sort": "none"
        }
      },
      "pluginVersion": "11.5.1",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "editorMode": "code",
          "exemplar": true,
          "expr": "cnpg_pg_stat_replication_replay_lag_seconds{namespace=~\"$namespace\",pod=~\"$instances\"}",
          "interval": "",
          "legendFormat": "{{pod}} -> {{application_name}}",
          "range": true,
          "refId": "A"
        }
      ],
      "title": "Replay Lag",
      "type": "timeseries"
    },
    {
      "collapsed": false,
      "gridPos": {
        "h": 1,
        "w": 24,
        "x": 0,
        "y": 195
      },
      "id": 231,
      "panels": [],
      "title": "Collector Stats",
      "type": "row"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "fieldConfig": {
        "defaults": {
          "custom": {
            "hideFrom": {
              "legend": false,
              "tooltip": false,
              "viz": false
            },
            "scaleDistribution": {
              "type": "linear"
            }
          }
        },
        "overrides": []
      },
      "gridPos": {
        "h": 8,
        "w": 12,
        "x": 0,
        "y": 196
      },
      "id": 233,
      "options": {
        "calculate": true,
        "calculation": {},
        "cellGap": 2,
        "cellValues": {},
        "color": {
          "exponent": 0.5,
          "fill": "#b4ff00",
          "mode": "scheme",
          "reverse": false,
          "scale": "exponential",
          "scheme": "Oranges",
          "steps": 128
        },
        "exemplars": {
          "color": "rgba(255,0,255,0.7)"
        },
        "filterValues": {
          "le": 1e-9
        },
        "legend": {
          "show": false
        },
        "rowsFrame": {
          "layout": "auto"
        },
        "showValue": "never",
        "tooltip": {
          "mode": "single",
          "showColorScale": false,
          "yHistogram": false
        },
        "yAxis": {
          "axisPlacement": "left",
          "reverse": false,
          "unit": "s"
        }
      },
      "pluginVersion": "11.5.1",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "cnpg_collector_collection_duration_seconds{namespace=~\"$namespace\",pod=~\"$instances\"}",
          "interval": "",
          "legendFormat": "",
          "refId": "A"
        }
      ],
      "title": "Collection Duration",
      "type": "heatmap"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "palette-classic"
          },
          "custom": {
            "axisBorderShow": false,
            "axisCenteredZero": false,
            "axisColorMode": "text",
            "axisLabel": "",
            "axisPlacement": "auto",
            "barAlignment": 0,
            "barWidthFactor": 0.6,
            "drawStyle": "line",
            "fillOpacity": 30,
            "gradientMode": "opacity",
            "hideFrom": {
              "legend": false,
              "tooltip": false,
              "viz": false
            },
            "insertNulls": false,
            "lineInterpolation": "linear",
            "lineWidth": 1,
            "pointSize": 5,
            "scaleDistribution": {
              "type": "linear"
            },
            "showPoints": "auto",
            "spanNulls": false,
            "stacking": {
              "group": "A",
              "mode": "none"
            },
            "thresholdsStyle": {
              "mode": "off"
            }
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green"
              },
              {
                "color": "red",
                "value": 80
              }
            ]
          }
        },
        "overrides": []
      },
      "gridPos": {
        "h": 8,
        "w": 12,
        "x": 12,
        "y": 196
      },
      "id": 235,
      "options": {
        "legend": {
          "calcs": [],
          "displayMode": "list",
          "placement": "bottom",
          "showLegend": true
        },
        "tooltip": {
          "hideZeros": false,
          "mode": "multi",
          "sort": "none"
        }
      },
      "pluginVersion": "11.5.1",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "cnpg_collector_last_collection_error{namespace=~\"$namespace\",pod=~\"$instances\"}",
          "interval": "",
          "legendFormat": "{{pod}}",
          "refId": "A"
        }
      ],
      "title": "Errors",
      "type": "timeseries"
    },
    {
      "collapsed": false,
      "gridPos": {
        "h": 1,
        "w": 24,
        "x": 0,
        "y": 204
      },
      "id": 239,
      "panels": [],
      "title": "Backups",
      "type": "row"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "palette-classic"
          },
          "custom": {
            "axisBorderShow": false,
            "axisCenteredZero": false,
            "axisColorMode": "text",
            "axisLabel": "",
            "axisPlacement": "auto",
            "barAlignment": 0,
            "barWidthFactor": 0.6,
            "drawStyle": "line",
            "fillOpacity": 30,
            "gradientMode": "opacity",
            "hideFrom": {
              "legend": false,
              "tooltip": false,
              "viz": false
            },
            "insertNulls": false,
            "lineInterpolation": "linear",
            "lineWidth": 1,
            "pointSize": 5,
            "scaleDistribution": {
              "type": "linear"
            },
            "showPoints": "auto",
            "spanNulls": false,
            "stacking": {
              "group": "A",
              "mode": "none"
            },
            "thresholdsStyle": {
              "mode": "off"
            }
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green"
              },
              {
                "color": "red",
                "value": 80
              }
            ]
          },
          "unit": "dateTimeAsIso"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 6,
        "w": 8,
        "x": 0,
        "y": 205
      },
      "id": 237,
      "options": {
        "legend": {
          "calcs": [],
          "displayMode": "list",
          "placement": "bottom",
          "showLegend": true
        },
        "tooltip": {
          "hideZeros": false,
          "mode": "multi",
          "sort": "none"
        }
      },
      "pluginVersion": "11.5.1",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "cnpg_collector_first_recoverability_point{namespace=~\"$namespace\",pod=~\"$instances\"}*1000 > 0",
          "format": "time_series",
          "interval": "",
          "legendFormat": "{{pod}}",
          "refId": "A"
        }
      ],
      "title": "First Recoverability Point",
      "type": "timeseries"
    },
    {
      "collapsed": false,
      "gridPos": {
        "h": 1,
        "w": 24,
        "x": 0,
        "y": 211
      },
      "id": 293,
      "panels": [],
      "title": "Checkpoints",
      "type": "row"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "description": "",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "palette-classic"
          },
          "custom": {
            "axisBorderShow": false,
            "axisCenteredZero": false,
            "axisColorMode": "text",
            "axisLabel": "",
            "axisPlacement": "auto",
            "barAlignment": -1,
            "barWidthFactor": 0.6,
            "drawStyle": "line",
            "fillOpacity": 30,
            "gradientMode": "opacity",
            "hideFrom": {
              "legend": false,
              "tooltip": false,
              "viz": false
            },
            "insertNulls": false,
            "lineInterpolation": "linear",
            "lineWidth": 1,
            "pointSize": 5,
            "scaleDistribution": {
              "type": "linear"
            },
            "showPoints": "never",
            "spanNulls": true,
            "stacking": {
              "group": "A",
              "mode": "none"
            },
            "thresholdsStyle": {
              "mode": "off"
            }
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green"
              },
              {
                "color": "red",
                "value": 80
              }
            ]
          },
          "unit": "none"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 6,
        "w": 5,
        "x": 0,
        "y": 212
      },
      "id": 295,
      "options": {
        "legend": {
          "calcs": [],
          "displayMode": "list",
          "placement": "bottom",
          "showLegend": true
        },
        "tooltip": {
          "hideZeros": false,
          "mode": "multi",
          "sort": "none"
        }
      },
      "pluginVersion": "11.5.1",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "{__name__=~\"cnpg_pg_stat_(bgwriter|checkpointer)_checkpoints_req\",namespace=~\"$namespace\",pod=~\"$instances\"}",
          "format": "time_series",
          "hide": false,
          "instant": false,
          "interval": "",
          "intervalFactor": 1,
          "legendFormat": "req/{{pod}}",
          "refId": "B"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "{__name__=~\"cnpg_pg_stat_(bgwriter|checkpointer)_checkpoints_timed\",namespace=~\"$namespace\",pod=~\"$instances\"}",
          "format": "time_series",
          "interval": "",
          "intervalFactor": 1,
          "legendFormat": "timed/{{pod}}",
          "refId": "A"
        }
      ],
      "title": "Requested/Timed",
      "type": "timeseries"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "description": "",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "palette-classic"
          },
          "custom": {
            "axisBorderShow": false,
            "axisCenteredZero": false,
            "axisColorMode": "text",
            "axisLabel": "",
            "axisPlacement": "auto",
            "barAlignment": -1,
            "barWidthFactor": 0.6,
            "drawStyle": "line",
            "fillOpacity": 30,
            "gradientMode": "opacity",
            "hideFrom": {
              "legend": false,
              "tooltip": false,
              "viz": false
            },
            "insertNulls": false,
            "lineInterpolation": "linear",
            "lineWidth": 1,
            "pointSize": 5,
            "scaleDistribution": {
              "type": "linear"
            },
            "showPoints": "never",
            "spanNulls": true,
            "stacking": {
              "group": "A",
              "mode": "none"
            },
            "thresholdsStyle": {
              "mode": "off"
            }
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green"
              },
              {
                "color": "red",
                "value": 80
              }
            ]
          },
          "unit": "ms"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 6,
        "w": 5,
        "x": 5,
        "y": 212
      },
      "id": 296,
      "options": {
        "legend": {
          "calcs": [],
          "displayMode": "list",
          "placement": "bottom",
          "showLegend": true
        },
        "tooltip": {
          "hideZeros": false,
          "mode": "multi",
          "sort": "none"
        }
      },
      "pluginVersion": "11.5.1",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "{__name__=~\"cnpg_pg_stat_(bgwriter_checkpoint|checkpointer)_write_time\",namespace=~\"$namespace\",pod=~\"$instances\"}",
          "format": "time_series",
          "hide": false,
          "instant": false,
          "interval": "",
          "intervalFactor": 1,
          "legendFormat": "write/{{pod}}",
          "refId": "B"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "{__name__=~\"cnpg_pg_stat_(bgwriter_checkpoint|checkpointer)_sync_time\",namespace=~\"$namespace\",pod=~\"$instances\"}",
          "format": "time_series",
          "interval": "",
          "intervalFactor": 1,
          "legendFormat": "sync/{{pod}}",
          "refId": "A"
        }
      ],
      "title": "Write/Sync time",
      "type": "timeseries"
    },
    {
      "collapsed": false,
      "gridPos": {
        "h": 1,
        "w": 24,
        "x": 0,
        "y": 218
      },
      "id": 794,
      "panels": [],
      "title": "Extensions",
      "type": "row"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "description": "Show the installed extensions and their versions",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "custom": {
            "align": "auto",
            "cellOptions": {
              "type": "auto",
              "wrapText": false
            },
            "filterable": false,
            "inspect": false
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green"
              }
            ]
          }
        },
        "overrides": [
          {
            "matcher": {
              "id": "byName",
              "options": "Update Available"
            },
            "properties": [
              {
                "id": "unit",
                "value": "bool_yes_no"
              },
              {
                "id": "mappings",
                "value": [
                  {
                    "options": {
                      "0": {
                        "color": "green",
                        "index": 1
                      },
                      "1": {
                        "color": "red",
                        "index": 0
                      }
                    },
                    "type": "value"
                  }
                ]
              },
              {
                "id": "custom.cellOptions",
                "value": {
                  "type": "color-background"
                }
              },
              {
                "id": "custom.width",
                "value": 135
              }
            ]
          }
        ]
      },
      "gridPos": {
        "h": 8,
        "w": 24,
        "x": 0,
        "y": 219
      },
      "id": 792,
      "options": {
        "cellHeight": "sm",
        "footer": {
          "countRows": false,
          "fields": "",
          "reducer": [
            "sum"
          ],
          "show": false
        },
        "showHeader": true,
        "sortBy": [
          {
            "desc": false,
            "displayName": "Value"
          }
        ]
      },
      "pluginVersion": "11.5.1",
      "targets": [
        {
          "disableTextWrap": false,
          "editorMode": "code",
          "exemplar": false,
          "expr": "max(cnpg_pg_extensions_update_available{pod=~\"$instances\", namespace=~\"$namespace\"}) by (datname, extname, default_version, installed_version)",
          "format": "table",
          "fullMetaSearch": false,
          "includeNullMetadata": true,
          "instant": true,
          "interval": "",
          "legendFormat": "__auto",
          "range": false,
          "refId": "A",
          "useBackend": false
        }
      ],
      "title": "Installed extensions",
      "transformations": [
        {
          "id": "sortBy",
          "options": {
            "fields": {},
            "sort": [
              {
                "field": "extname"
              }
            ]
          }
        },
        {
          "id": "organize",
          "options": {
            "excludeByName": {
              "Time": true
            },
            "includeByName": {},
            "indexByName": {
              "Time": 0,
              "Value": 5,
              "datname": 2,
              "default_version": 3,
              "extname": 1,
              "installed_version": 4
            },
            "renameByName": {
              "Value": "Update Available",
              "datname": "Database",
              "default_version": "Default Version",
              "extname": "Extension",
              "installed_version": "Installed Version"
            }
          }
        }
      ],
      "type": "table"
    },
    {
      "collapsed": false,
      "gridPos": {
        "h": 1,
        "w": 24,
        "x": 0,
        "y": 227
      },
      "id": 696,
      "panels": [],
      "title": "Operator",
      "type": "row"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "description": "",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "mappings": [
            {
              "options": {
                "0": {
                  "color": "red",
                  "index": 0,
                  "text": "No Ready pods"
                }
              },
              "type": "value"
            }
          ],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green"
              }
            ]
          }
        },
        "overrides": [
          {
            "matcher": {
              "id": "byName",
              "options": "A"
            },
            "properties": [
              {
                "id": "displayName",
                "value": "Reconcile errors"
              }
            ]
          }
        ]
      },
      "gridPos": {
        "h": 2,
        "w": 4,
        "x": 0,
        "y": 228
      },
      "id": 697,
      "options": {
        "colorMode": "background",
        "graphMode": "none",
        "justifyMode": "auto",
        "orientation": "auto",
        "percentChangeColorMode": "standard",
        "reduceOptions": {
          "calcs": [
            "lastNotNull"
          ],
          "fields": "",
          "values": false
        },
        "showPercentChange": false,
        "textMode": "value_and_name",
        "wideLayout": true
      },
      "pluginVersion": "11.5.1",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "editorMode": "code",
          "exemplar": false,
          "expr": "sum(kube_pod_status_ready{namespace=\"$operatorNamespace\", pod=~\"cloudnative-pg-operator.+\", condition=\"true\"})",
          "hide": false,
          "instant": true,
          "legendFormat": "Ready Operator Pods",
          "range": false,
          "refId": "A"
        }
      ],
      "title": "",
      "type": "stat"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "description": "The operator reconcile errors don't distinguish between database cluster or namespaces.",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "mappings": [
            {
              "options": {
                "0": {
                  "color": "green",
                  "index": 0,
                  "text": "None"
                }
              },
              "type": "value"
            },
            {
              "options": {
                "from": 1,
                "result": {
                  "color": "red",
                  "index": 1
                },
                "to": 4294967295
              },
              "type": "range"
            }
          ],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green"
              }
            ]
          }
        },
        "overrides": [
          {
            "matcher": {
              "id": "byName",
              "options": "A"
            },
            "properties": [
              {
                "id": "displayName",
                "value": "Reconcile errors"
              }
            ]
          }
        ]
      },
      "gridPos": {
        "h": 2,
        "w": 4,
        "x": 4,
        "y": 228
      },
      "id": 702,
      "options": {
        "colorMode": "background",
        "graphMode": "none",
        "justifyMode": "auto",
        "orientation": "auto",
        "percentChangeColorMode": "standard",
        "reduceOptions": {
          "calcs": [
            "lastNotNull"
          ],
          "fields": "",
          "values": false
        },
        "showPercentChange": false,
        "textMode": "value_and_name",
        "wideLayout": true
      },
      "pluginVersion": "11.5.1",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "editorMode": "code",
          "exemplar": false,
          "expr": "max(controller_runtime_reconcile_total{namespace=~\"$operatorNamespace\", result=\"error\", controller=\"cluster\"})",
          "hide": false,
          "instant": true,
          "legendFormat": "Cluster Reconcile Errors",
          "range": false,
          "refId": "RECONCILE_ERRORS_BACKUP"
        }
      ],
      "title": "",
      "type": "stat"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "description": "The operator reconcile errors don't distinguish between database cluster or namespaces.",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "mappings": [
            {
              "options": {
                "0": {
                  "color": "green",
                  "index": 0,
                  "text": "None"
                }
              },
              "type": "value"
            },
            {
              "options": {
                "from": 1,
                "result": {
                  "color": "red",
                  "index": 1
                },
                "to": 4294967295
              },
              "type": "range"
            }
          ],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green"
              }
            ]
          }
        },
        "overrides": [
          {
            "matcher": {
              "id": "byName",
              "options": "A"
            },
            "properties": [
              {
                "id": "displayName",
                "value": "Reconcile errors"
              }
            ]
          }
        ]
      },
      "gridPos": {
        "h": 2,
        "w": 4,
        "x": 8,
        "y": 228
      },
      "id": 698,
      "options": {
        "colorMode": "background",
        "graphMode": "none",
        "justifyMode": "auto",
        "orientation": "auto",
        "percentChangeColorMode": "standard",
        "reduceOptions": {
          "calcs": [
            "lastNotNull"
          ],
          "fields": "",
          "values": false
        },
        "showPercentChange": false,
        "textMode": "value_and_name",
        "wideLayout": true
      },
      "pluginVersion": "11.5.1",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "editorMode": "code",
          "exemplar": false,
          "expr": "max(controller_runtime_reconcile_total{namespace=~\"$operatorNamespace\", result=\"error\", controller=\"backup\"})",
          "hide": false,
          "instant": true,
          "legendFormat": "Backup Reconcile Errors",
          "range": false,
          "refId": "RECONCILE_ERRORS_BACKUP"
        }
      ],
      "title": "",
      "type": "stat"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "description": "The operator reconcile errors don't distinguish between database cluster or namespaces.",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "mappings": [
            {
              "options": {
                "0": {
                  "color": "green",
                  "index": 0,
                  "text": "None"
                }
              },
              "type": "value"
            },
            {
              "options": {
                "from": 1,
                "result": {
                  "color": "red",
                  "index": 1
                },
                "to": 4294967295
              },
              "type": "range"
            }
          ],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green"
              }
            ]
          }
        },
        "overrides": [
          {
            "matcher": {
              "id": "byName",
              "options": "A"
            },
            "properties": [
              {
                "id": "displayName",
                "value": "Reconcile errors"
              }
            ]
          }
        ]
      },
      "gridPos": {
        "h": 2,
        "w": 4,
        "x": 12,
        "y": 228
      },
      "id": 704,
      "options": {
        "colorMode": "background",
        "graphMode": "none",
        "justifyMode": "auto",
        "orientation": "auto",
        "percentChangeColorMode": "standard",
        "reduceOptions": {
          "calcs": [
            "lastNotNull"
          ],
          "fields": "",
          "values": false
        },
        "showPercentChange": false,
        "textMode": "value_and_name",
        "wideLayout": true
      },
      "pluginVersion": "11.5.1",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "editorMode": "code",
          "exemplar": false,
          "expr": "max(controller_runtime_reconcile_total{namespace=~\"$operatorNamespace\", result=\"error\", controller=~\"scheduledbackup|scheduled-backup\"})",
          "hide": false,
          "instant": true,
          "legendFormat": "Scheduled Backup Reconcile Errors",
          "range": false,
          "refId": "RECONCILE_ERRORS_BACKUP"
        }
      ],
      "title": "",
      "type": "stat"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "description": "The operator reconcile errors don't distinguish between database cluster or namespaces.",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "mappings": [
            {
              "options": {
                "0": {
                  "color": "green",
                  "index": 0,
                  "text": "None"
                }
              },
              "type": "value"
            },
            {
              "options": {
                "from": 1,
                "result": {
                  "color": "red",
                  "index": 1
                },
                "to": 4294967295
              },
              "type": "range"
            }
          ],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green"
              }
            ]
          }
        },
        "overrides": [
          {
            "matcher": {
              "id": "byName",
              "options": "A"
            },
            "properties": [
              {
                "id": "displayName",
                "value": "Reconcile errors"
              }
            ]
          }
        ]
      },
      "gridPos": {
        "h": 2,
        "w": 4,
        "x": 16,
        "y": 228
      },
      "id": 703,
      "options": {
        "colorMode": "background",
        "graphMode": "none",
        "justifyMode": "auto",
        "orientation": "auto",
        "percentChangeColorMode": "standard",
        "reduceOptions": {
          "calcs": [
            "lastNotNull"
          ],
          "fields": "",
          "values": false
        },
        "showPercentChange": false,
        "textMode": "value_and_name",
        "wideLayout": true
      },
      "pluginVersion": "11.5.1",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "editorMode": "code",
          "exemplar": false,
          "expr": "max(controller_runtime_reconcile_total{namespace=~\"$operatorNamespace\", result=\"error\", controller=\"pooler\"})",
          "hide": false,
          "instant": true,
          "legendFormat": "Pooler Reconcile Errors",
          "range": false,
          "refId": "RECONCILE_ERRORS_BACKUP"
        }
      ],
      "title": "",
      "type": "stat"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "description": "",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "palette-classic"
          },
          "custom": {
            "axisBorderShow": false,
            "axisCenteredZero": false,
            "axisColorMode": "text",
            "axisLabel": "",
            "axisPlacement": "auto",
            "barAlignment": 0,
            "barWidthFactor": 0.6,
            "drawStyle": "line",
            "fillOpacity": 30,
            "gradientMode": "opacity",
            "hideFrom": {
              "legend": false,
              "tooltip": false,
              "viz": false
            },
            "insertNulls": false,
            "lineInterpolation": "linear",
            "lineWidth": 1,
            "pointSize": 5,
            "scaleDistribution": {
              "type": "linear"
            },
            "showPoints": "auto",
            "spanNulls": false,
            "stacking": {
              "group": "A",
              "mode": "none"
            },
            "thresholdsStyle": {
              "mode": "off"
            }
          },
          "mappings": [
            {
              "options": {
                "0": {
                  "color": "red",
                  "index": 0,
                  "text": "No Ready pods"
                }
              },
              "type": "value"
            }
          ],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green"
              }
            ]
          }
        },
        "overrides": [
          {
            "matcher": {
              "id": "byName",
              "options": "A"
            },
            "properties": [
              {
                "id": "displayName",
                "value": "Reconcile errors"
              }
            ]
          }
        ]
      },
      "gridPos": {
        "h": 8,
        "w": 4,
        "x": 0,
        "y": 230
      },
      "id": 746,
      "options": {
        "legend": {
          "calcs": [],
          "displayMode": "list",
          "placement": "bottom",
          "showLegend": true
        },
        "tooltip": {
          "hideZeros": false,
          "mode": "single",
          "sort": "none"
        }
      },
      "pluginVersion": "11.5.1",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "editorMode": "code",
          "expr": "sum(kube_pod_status_ready{namespace=\"$operatorNamespace\", pod=~\"cloudnative-pg-operator.+\", condition=\"true\"})",
          "hide": false,
          "instant": false,
          "legendFormat": "Ready Operator Pods",
          "range": true,
          "refId": "A"
        }
      ],
      "title": "Ready Operator Pods",
      "type": "timeseries"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "description": "The operator reconcile errors don't distinguish between database cluster or namespaces.",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "palette-classic"
          },
          "custom": {
            "axisBorderShow": false,
            "axisCenteredZero": false,
            "axisColorMode": "text",
            "axisLabel": "",
            "axisPlacement": "auto",
            "barAlignment": 0,
            "barWidthFactor": 0.6,
            "drawStyle": "line",
            "fillOpacity": 30,
            "gradientMode": "opacity",
            "hideFrom": {
              "legend": false,
              "tooltip": false,
              "viz": false
            },
            "insertNulls": false,
            "lineInterpolation": "linear",
            "lineWidth": 1,
            "pointSize": 5,
            "scaleDistribution": {
              "type": "linear"
            },
            "showPoints": "auto",
            "spanNulls": false,
            "stacking": {
              "group": "A",
              "mode": "none"
            },
            "thresholdsStyle": {
              "mode": "off"
            }
          },
          "mappings": [
            {
              "options": {
                "0": {
                  "color": "green",
                  "index": 0,
                  "text": "None"
                }
              },
              "type": "value"
            },
            {
              "options": {
                "from": 1,
                "result": {
                  "color": "red",
                  "index": 1
                },
                "to": 4294967295
              },
              "type": "range"
            }
          ],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green"
              }
            ]
          }
        },
        "overrides": [
          {
            "matcher": {
              "id": "byName",
              "options": "A"
            },
            "properties": [
              {
                "id": "displayName",
                "value": "Reconcile errors"
              }
            ]
          }
        ]
      },
      "gridPos": {
        "h": 8,
        "w": 4,
        "x": 4,
        "y": 230
      },
      "id": 767,
      "options": {
        "legend": {
          "calcs": [],
          "displayMode": "list",
          "placement": "bottom",
          "showLegend": true
        },
        "tooltip": {
          "hideZeros": false,
          "mode": "single",
          "sort": "none"
        }
      },
      "pluginVersion": "11.5.1",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "editorMode": "code",
          "expr": "max(controller_runtime_reconcile_total{namespace=~\"$operatorNamespace\", result=\"error\", controller=\"cluster\"})",
          "hide": false,
          "legendFormat": "Cluster Reconcile Errors",
          "range": true,
          "refId": "RECONCILE_ERRORS_BACKUP"
        }
      ],
      "title": "Cluster Reconcile Errors",
      "type": "timeseries"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "description": "The operator reconcile errors don't distinguish between database cluster or namespaces.",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "palette-classic"
          },
          "custom": {
            "axisBorderShow": false,
            "axisCenteredZero": false,
            "axisColorMode": "text",
            "axisLabel": "",
            "axisPlacement": "auto",
            "barAlignment": 0,
            "barWidthFactor": 0.6,
            "drawStyle": "line",
            "fillOpacity": 30,
            "gradientMode": "opacity",
            "hideFrom": {
              "legend": false,
              "tooltip": false,
              "viz": false
            },
            "insertNulls": false,
            "lineInterpolation": "linear",
            "lineWidth": 1,
            "pointSize": 5,
            "scaleDistribution": {
              "type": "linear"
            },
            "showPoints": "auto",
            "spanNulls": false,
            "stacking": {
              "group": "A",
              "mode": "none"
            },
            "thresholdsStyle": {
              "mode": "off"
            }
          },
          "mappings": [
            {
              "options": {
                "0": {
                  "color": "green",
                  "index": 0,
                  "text": "None"
                }
              },
              "type": "value"
            },
            {
              "options": {
                "from": 1,
                "result": {
                  "color": "red",
                  "index": 1
                },
                "to": 4294967295
              },
              "type": "range"
            }
          ],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green"
              }
            ]
          }
        },
        "overrides": [
          {
            "matcher": {
              "id": "byName",
              "options": "A"
            },
            "properties": [
              {
                "id": "displayName",
                "value": "Reconcile errors"
              }
            ]
          }
        ]
      },
      "gridPos": {
        "h": 8,
        "w": 4,
        "x": 8,
        "y": 230
      },
      "id": 768,
      "options": {
        "legend": {
          "calcs": [],
          "displayMode": "list",
          "placement": "bottom",
          "showLegend": true
        },
        "tooltip": {
          "hideZeros": false,
          "mode": "single",
          "sort": "none"
        }
      },
      "pluginVersion": "11.5.1",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "editorMode": "code",
          "expr": "max(controller_runtime_reconcile_total{namespace=~\"$operatorNamespace\", result=\"error\", controller=\"backup\"})",
          "hide": false,
          "legendFormat": "Backup Reconcile Errors",
          "range": true,
          "refId": "RECONCILE_ERRORS_BACKUP"
        }
      ],
      "title": "Backup Reconcile Errors",
      "type": "timeseries"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "description": "The operator reconcile errors don't distinguish between database cluster or namespaces.",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "palette-classic"
          },
          "custom": {
            "axisBorderShow": false,
            "axisCenteredZero": false,
            "axisColorMode": "text",
            "axisLabel": "",
            "axisPlacement": "auto",
            "barAlignment": 0,
            "barWidthFactor": 0.6,
            "drawStyle": "line",
            "fillOpacity": 30,
            "gradientMode": "opacity",
            "hideFrom": {
              "legend": false,
              "tooltip": false,
              "viz": false
            },
            "insertNulls": false,
            "lineInterpolation": "linear",
            "lineWidth": 1,
            "pointSize": 5,
            "scaleDistribution": {
              "type": "linear"
            },
            "showPoints": "auto",
            "spanNulls": false,
            "stacking": {
              "group": "A",
              "mode": "none"
            },
            "thresholdsStyle": {
              "mode": "off"
            }
          },
          "mappings": [
            {
              "options": {
                "0": {
                  "color": "green",
                  "index": 0,
                  "text": "None"
                }
              },
              "type": "value"
            },
            {
              "options": {
                "from": 1,
                "result": {
                  "color": "red",
                  "index": 1
                },
                "to": 4294967295
              },
              "type": "range"
            }
          ],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green"
              }
            ]
          }
        },
        "overrides": [
          {
            "matcher": {
              "id": "byName",
              "options": "A"
            },
            "properties": [
              {
                "id": "displayName",
                "value": "Reconcile errors"
              }
            ]
          }
        ]
      },
      "gridPos": {
        "h": 8,
        "w": 4,
        "x": 12,
        "y": 230
      },
      "id": 790,
      "options": {
        "legend": {
          "calcs": [],
          "displayMode": "list",
          "placement": "bottom",
          "showLegend": true
        },
        "tooltip": {
          "hideZeros": false,
          "mode": "single",
          "sort": "none"
        }
      },
      "pluginVersion": "11.5.1",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "editorMode": "code",
          "exemplar": false,
          "expr": "max(controller_runtime_reconcile_total{namespace=~\"$operatorNamespace\", result=\"error\", controller=~\"scheduledbackup|scheduled-backup\"})",
          "hide": false,
          "instant": false,
          "legendFormat": "Scheduled Backup Reconcile Errors",
          "range": true,
          "refId": "RECONCILE_ERRORS_BACKUP"
        }
      ],
      "title": "Scheduled Backup Reconcile Errors",
      "type": "timeseries"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "description": "The operator reconcile errors don't distinguish between database cluster or namespaces.",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "palette-classic"
          },
          "custom": {
            "axisBorderShow": false,
            "axisCenteredZero": false,
            "axisColorMode": "text",
            "axisLabel": "",
            "axisPlacement": "auto",
            "barAlignment": 0,
            "barWidthFactor": 0.6,
            "drawStyle": "line",
            "fillOpacity": 30,
            "gradientMode": "opacity",
            "hideFrom": {
              "legend": false,
              "tooltip": false,
              "viz": false
            },
            "insertNulls": false,
            "lineInterpolation": "linear",
            "lineWidth": 1,
            "pointSize": 5,
            "scaleDistribution": {
              "type": "linear"
            },
            "showPoints": "auto",
            "spanNulls": false,
            "stacking": {
              "group": "A",
              "mode": "none"
            },
            "thresholdsStyle": {
              "mode": "off"
            }
          },
          "mappings": [
            {
              "options": {
                "0": {
                  "color": "green",
                  "index": 0,
                  "text": "None"
                }
              },
              "type": "value"
            },
            {
              "options": {
                "from": 1,
                "result": {
                  "color": "red",
                  "index": 1
                },
                "to": 4294967295
              },
              "type": "range"
            }
          ],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green"
              }
            ]
          }
        },
        "overrides": [
          {
            "matcher": {
              "id": "byName",
              "options": "A"
            },
            "properties": [
              {
                "id": "displayName",
                "value": "Reconcile errors"
              }
            ]
          }
        ]
      },
      "gridPos": {
        "h": 8,
        "w": 4,
        "x": 16,
        "y": 230
      },
      "id": 769,
      "options": {
        "legend": {
          "calcs": [],
          "displayMode": "list",
          "placement": "bottom",
          "showLegend": true
        },
        "tooltip": {
          "hideZeros": false,
          "mode": "single",
          "sort": "none"
        }
      },
      "pluginVersion": "11.5.1",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "editorMode": "code",
          "expr": "max(controller_runtime_reconcile_total{namespace=~\"$operatorNamespace\", result=\"error\", controller=\"pooler\"})",
          "hide": false,
          "legendFormat": "Pooler Reconcile Errors",
          "range": true,
          "refId": "RECONCILE_ERRORS_BACKUP"
        }
      ],
      "title": "Pooler Reconcile Errors",
      "type": "timeseries"
    }
  ],
  "preload": false,
  "refresh": "30s",
  "schemaVersion": 40,
  "tags": [],
  "templating": {
    "list": [
      {
        "current": {},
        "includeAll": false,
        "label": "Datasource",
        "name": "DS_PROMETHEUS",
        "options": [],
        "query": "prometheus",
        "refresh": 1,
        "regex": "",
        "type": "datasource"
      },
      {
        "current": {
          "text": "cnpg-system",
          "value": "cnpg-system"
        },
        "datasource": {
          "type": "prometheus",
          "uid": "${DS_PROMETHEUS}"
        },
        "definition": "label_values(controller_runtime_webhook_requests_total{webhook=\"/mutate-postgresql-cnpg-io-v1-cluster\"},namespace)",
        "description": "Namespace where the CNPG operator is located",
        "includeAll": false,
        "label": "Operator Namespace",
        "name": "operatorNamespace",
        "options": [],
        "query": {
          "qryType": 1,
          "query": "label_values(controller_runtime_webhook_requests_total{webhook=\"/mutate-postgresql-cnpg-io-v1-cluster\"},namespace)",
          "refId": "PrometheusVariableQueryEditor-VariableQuery"
        },
        "refresh": 2,
        "regex": "",
        "type": "query"
      },
      {
        "current": {
          "text": "paradedb",
          "value": "paradedb"
        },
        "datasource": {
          "type": "prometheus",
          "uid": "${DS_PROMETHEUS}"
        },
        "definition": "cnpg_collector_up",
        "description": "Namespace where the database cluster is located",
        "includeAll": false,
        "label": "Database Namespace",
        "name": "namespace",
        "options": [],
        "query": {
          "query": "cnpg_collector_up",
          "refId": "StandardVariableQuery"
        },
        "refresh": 2,
        "regex": "/namespace=\"(?<text>[^\"]+)/g",
        "type": "query"
      },
      {
        "current": {
          "text": "paradedb-replica",
          "value": "paradedb-replica"
        },
        "datasource": {
          "type": "prometheus",
          "uid": "${DS_PROMETHEUS}"
        },
        "definition": "cnpg_collector_up{namespace=~\"$namespace\"}",
        "description": "CNPG Cluster",
        "includeAll": false,
        "label": "Cluster",
        "name": "cluster",
        "options": [],
        "query": {
          "query": "cnpg_collector_up{namespace=~\"$namespace\"}",
          "refId": "PrometheusVariableQueryEditor-VariableQuery"
        },
        "refresh": 2,
        "regex": "/\\bcluster\\b=\"(?<text>[^\"]+)/g",
        "sort": 1,
        "type": "query"
      },
      {
        "allValue": "$cluster-([1-9][0-9]*)",
        "current": {
          "text": "All",
          "value": [
            "$__all"
          ]
        },
        "datasource": {
          "type": "prometheus",
          "uid": "${DS_PROMETHEUS}"
        },
        "definition": "cnpg_collector_up{namespace=~\"$namespace\",pod=~\"$cluster-([1-9][0-9]*)$\"}",
        "description": "Database cluster instances",
        "includeAll": true,
        "label": "Instances",
        "multi": true,
        "name": "instances",
        "options": [],
        "query": {
          "qryType": 4,
          "query": "cnpg_collector_up{namespace=~\"$namespace\",pod=~\"$cluster-([1-9][0-9]*)$\"}",
          "refId": "PrometheusVariableQueryEditor-VariableQuery"
        },
        "refresh": 2,
        "regex": "/pod=\"(?<text>[^\"]+)/g",
        "sort": 1,
        "type": "query"
      },
      {
        "allowCustomValue": false,
        "current": {
          "text": "All",
          "value": "$__all"
        },
        "definition": "label_values(cnpg_paradedb_index_layer_segments_bucket{namespace=\"$namespace\"},relname)",
        "hide": 2,
        "includeAll": true,
        "name": "bm25_indicies",
        "options": [],
        "query": {
          "qryType": 1,
          "query": "label_values(cnpg_paradedb_index_layer_segments_bucket{namespace=\"$namespace\"},relname)",
          "refId": "PrometheusVariableQueryEditor-VariableQuery"
        },
        "refresh": 2,
        "regex": "",
        "type": "query"
      },
      {
        "allValue": ".+",
        "current": {
          "text": "All",
          "value": "$__all"
        },
        "definition": "label_values(kube_node_info,node)",
        "description": "\tlabel_values(kube_node_info{customer=\"$customer\"},node)",
        "hide": 2,
        "includeAll": true,
        "multi": true,
        "name": "nodes",
        "options": [],
        "query": {
          "qryType": 1,
          "query": "label_values(kube_node_info,node)",
          "refId": "PrometheusVariableQueryEditor-VariableQuery"
        },
        "refresh": 1,
        "regex": "",
        "type": "query"
      }
    ]
  },
  "time": {
    "from": "now-6h",
    "to": "now"
  },
  "timepicker": {
    "nowDelay": ""
  },
  "timezone": "",
  "title": "ParadeDB",
  "uid": "paradedb",
  "version": 4,
  "weekStart": ""
}

```

## File: charts\paradedb\prometheus_rules\cluster-ha-critical.yaml
```
{{- $alert := "CNPGClusterHACritical" -}}
{{- if not (has $alert .excludeRules) -}}
alert: {{ $alert }}
annotations:
  summary: ParadeDB CNPG Cluster has no standby replicas!
  description: |-
    ParadeDB CloudNativePG Cluster "{{ .labels.job }}" has no ready standby replicas. The cluster is at a severe risk of data loss and downtime if the primary instance fails.

    The primary instance is still online and able to serve queries, although connections to the `-ro` endpoint will fail. The `-r` endpoint is operating at reduced capacity and all traffic is being served by the primary.

    This can happen during a normal fail-over or automated minor version upgrades in a cluster with 2 or less instances. The replaced instance may need some time to catch-up with the cluster primary instance.

    This alarm will be constantly triggered if your cluster is configured to run with only 1 instance. If this is intentional, you may want to silence it.
  runbook_url: https://github.com/paradedb/charts/blob/main/charts/paradedb/docs/runbooks/{{ $alert }}.md
expr: |
  max by (job) (cnpg_pg_replication_streaming_replicas{namespace="{{ .namespace }}"} - cnpg_pg_replication_is_wal_receiver_up{namespace="{{ .namespace }}"}) < 1
for: 5m
labels:
  severity: critical
  namespace: {{ .namespace }}
  cnpg_cluster: {{ .cluster }}
{{- end -}}

```

## File: charts\paradedb\prometheus_rules\cluster-ha-warning.yaml
```
{{- $alert := "CNPGClusterHAWarning" -}}
{{- if not (has $alert .excludeRules) -}}
alert: {{ $alert }}
annotations:
  summary: ParadeDB CNPG Cluster less than 2 standby replicas.
  description: |-
    ParadeDB CloudNativePG Cluster "{{ .labels.job }}" has only {{ .value }} standby replicas, putting your cluster at risk if another instance fails. The cluster is still able to operate normally, although the `-ro` and `-r` endpoints are operating at reduced capacity.

    This can happen during a normal fail-over or automated minor version upgrades. The replaced instance may need some time to catch-up with the cluster primary instance.

    This alarm will be constantly triggered if your cluster is configured to run with less than 3 instances. If this is intentional, you may want to silence it.
  runbook_url: https://github.com/paradedb/charts/blob/main/charts/paradedb/docs/runbooks/{{ $alert }}.md
expr: |
  max by (job) (cnpg_pg_replication_streaming_replicas{namespace="{{ .namespace }}"} - cnpg_pg_replication_is_wal_receiver_up{namespace="{{ .namespace }}"}) < 2
for: 5m
labels:
  severity: warning
  namespace: {{ .namespace }}
  cnpg_cluster: {{ .cluster }}
{{- end -}}

```

## File: charts\paradedb\prometheus_rules\cluster-high_connection-critical.yaml
```
{{- $alert := "CNPGClusterHighConnectionsCritical" -}}
{{- if not (has $alert .excludeRules) -}}
alert: {{ $alert }}
annotations:
  summary: ParadeDB Instance maximum number of connections critical!
  description: |-
    ParadeDB CloudNativePG Cluster "{{ .namespace }}/{{ .cluster }}" instance {{ .labels.pod }} is using {{ .value }}% of the maximum number of connections.
  runbook_url: https://github.com/paradedb/charts/blob/main/charts/paradedb/docs/runbooks/{{ $alert }}.md
expr: |
  sum by (pod) (cnpg_backends_total{namespace="{{ .namespace }}", pod=~"{{ .podSelector }}"}) / max by (pod) (cnpg_pg_settings_setting{name="max_connections", namespace="{{ .namespace }}", pod=~"{{ .podSelector }}"}) * 100 > 95
for: 5m
labels:
  severity: critical
  namespace: {{ .namespace }}
  cnpg_cluster: {{ .cluster }}
{{- end -}}

```

## File: charts\paradedb\prometheus_rules\cluster-high_connection-warning.yaml
```
{{- $alert := "CNPGClusterHighConnectionsWarning" -}}
{{- if not (has $alert .excludeRules) -}}
alert: {{ $alert }}
annotations:
  summary: ParadeDB Instance is approaching the maximum number of connections.
  description: |-
    ParadeDB CloudNativePG Cluster "{{ .namespace }}/{{ .cluster }}" instance {{ .labels.pod }} is using {{ .value }}% of the maximum number of connections.
  runbook_url: https://github.com/paradedb/charts/blob/main/charts/paradedb/docs/runbooks/{{ $alert }}.md
expr: |
  sum by (pod) (cnpg_backends_total{namespace="{{ .namespace }}", pod=~"{{ .podSelector }}"}) / max by (pod) (cnpg_pg_settings_setting{name="max_connections", namespace="{{ .namespace }}", pod=~"{{ .podSelector }}"}) * 100 > 80
for: 5m
labels:
  severity: warning
  namespace: {{ .namespace }}
  cnpg_cluster: {{ .cluster }}
{{- end -}}

```

## File: charts\paradedb\prometheus_rules\cluster-instances_on_same_node.yaml
```
{{- $alert := "CNPGClusterInstancesOnSameNode" -}}
{{- if not (has $alert .excludeRules) -}}
alert: {{ $alert }}
annotations:
  summary: Multiple ParadeDB CNPG Cluster instances are located on the same node.
  description: |-
    ParadeDB CloudNativePG Cluster "{{ .namespace }}/{{ .cluster }}" has {{ .value }} instances on the same node {{ .labels.node }}.

    A failure or scheduled downtime of a single node will lead to a potential service disruption and/or data loss.
  runbook_url: https://github.com/paradedb/charts/blob/main/charts/paradedb/docs/runbooks/{{ $alert }}.md
expr: |
  count by (node) (kube_pod_info{namespace="{{ .namespace }}", pod=~"{{ .podSelector }}"}) > 1
for: 5m
labels:
  severity: warning
  namespace: {{ .namespace }}
  cnpg_cluster: {{ .cluster }}
{{- end -}}

```

## File: charts\paradedb\prometheus_rules\cluster-logical_replication_errors-critical.yaml
```
{{- $alert := "CNPGClusterLogicalReplicationErrorsCritical" -}}
{{- if not (has $alert .excludeRules) -}}
alert: {{ $alert }}
annotations:
  summary: CNPG Cluster critical logical replication errors
  description: |-
    CloudNativePG Cluster's "{{ .namespace }}/{{ .cluster }}" "{{ .labels.subname }}" subscription has experienced {{ .value }} errors in the last 5 minutes.

    CRITICAL: High error rate indicates persistent replication issues requiring immediate attention. This could lead to significant data inconsistency or complete replication failure. Errors include both apply errors and sync errors. The subscription may stop working if errors continue.
  runbook_url: https://github.com/paradedb/charts/blob/main/charts/paradedb/docs/runbooks/CNPGClusterLogicalReplicationErrors.md
expr: |
  label_replace(increase(max by (namespace, job, subname) (cnpg_pg_stat_subscription_apply_error_count + cnpg_pg_stat_subscription_sync_error_count)[5m]), "cluster", "$1", "job", ".+/(.+)") >= 5
for: 0m
labels:
  severity: critical
  namespace: {{ .namespace }}
  cnpg_cluster: {{ .cluster }}
{{- end -}}

```

## File: charts\paradedb\prometheus_rules\cluster-logical_replication_errors.yaml
```
{{- $alert := "CNPGClusterLogicalReplicationErrors" -}}
{{- if not (has $alert .excludeRules) -}}
alert: {{ $alert }}
annotations:
  summary: CNPG Cluster logical replication errors detected
  description: |-
    CloudNativePG Cluster's "{{ .namespace }}/{{ .cluster }}" "{{ .labels.subname }}" subscription has experienced {{ .value }} errors.

    This includes both apply errors (during normal replication) and sync errors (during initial table sync). Errors indicate data consistency issues that need immediate attention to prevent data divergence.
  runbook_url: https://github.com/paradedb/charts/blob/main/charts/paradedb/docs/runbooks/{{ $alert }}.md
expr: |
  label_replace(increase(max by (namespace, job, subname) (cnpg_pg_stat_subscription_apply_error_count + cnpg_pg_stat_subscription_sync_error_count)[5m]), "cluster", "$1", "job", ".+/(.+)") > 0
for: 1m
labels:
  severity: warning
  namespace: {{ .namespace }}
  cnpg_cluster: {{ .cluster }}
{{- end -}}

```

## File: charts\paradedb\prometheus_rules\cluster-logical_replication_lagging-critical.yaml
```
{{- $alert := "CNPGClusterLogicalReplicationLaggingCritical" -}}
{{- if not (has $alert .excludeRules) -}}
alert: {{ $alert }}
annotations:
  summary: CNPG Cluster critical logical replication lag
  description: |-
    CloudNativePG Cluster's "{{ .namespace }}/{{ .cluster }}" "{{ .labels.subname }}" subscription is experiencing critical replication lag!

    {{- if .labels.lag_type }}
    Lag type: {{ .labels.lag_type }}
    {{- end }}
    Current lag: {{ .value }}s

    CRITICAL: The subscriber is significantly behind the publisher. Immediate action required. This could lead to significant data inconsistency, disk space exhaustion on publisher, or extended recovery time.
  runbook_url: https://github.com/paradedb/charts/blob/main/charts/paradedb/docs/runbooks/CNPGClusterLogicalReplicationLagging.md
expr: |
  (
    # Receipt lag - not receiving WAL data
    label_replace(max by (namespace, job, subname) (cnpg_pg_stat_subscription_receipt_lag_seconds), "cluster", "$1", "job", ".+/(.+)") > 300
  ) or (
    # Apply lag - not applying received data
    label_replace(max by (namespace, job, subname) (cnpg_pg_stat_subscription_apply_lag_seconds), "cluster", "$1", "job", ".+/(.+)") > 300
  ) or (
    # LSN distance - large amount of pending data
    label_replace(max by (namespace, job, subname) (cnpg_pg_stat_subscription_buffered_lag_bytes), "cluster", "$1", "job", ".+/(.+)") / 1024^3 > 4
  )
for: 2m
labels:
  severity: critical
  namespace: {{ .namespace }}
  cnpg_cluster: {{ .cluster }}
{{- end -}}

```

## File: charts\paradedb\prometheus_rules\cluster-logical_replication_lagging.yaml
```
{{- $alert := "CNPGClusterLogicalReplicationLagging" -}}
{{- if not (has $alert .excludeRules) -}}
alert: {{ $alert }}
annotations:
  summary: CNPG Cluster logical replication lagging
  description: |-
    CloudNativePG Cluster's "{{ .namespace }}/{{ .cluster }}" "{{ .labels.subname }}" subscription is experiencing replication lag.

    {{- if .labels.lag_type }}
    Lag type: {{ .labels.lag_type }}
    {{- end }}
    Current lag: {{ .value }}s

    This alert indicates the subscriber is falling behind the publisher. The lag could be receipt lag (not receiving WAL data fast enough due to network issues), apply lag (receiving data but not applying it fast enough due to resource contention), or LSN distance (large amount of pending data to be applied).
  runbook_url: https://github.com/paradedb/charts/blob/main/charts/paradedb/docs/runbooks/{{ $alert }}.md
expr: |
  (
    # Receipt lag - time since last message received
    label_replace(max by (namespace, job, subname) (cnpg_pg_stat_subscription_receipt_lag_seconds), "cluster", "$1", "job", ".+/(.+)") > 60
  ) or (
    # Apply lag - time delay in applying changes
    label_replace(max by (namespace, job, subname) (cnpg_pg_stat_subscription_apply_lag_seconds), "cluster", "$1", "job", ".+/(.+)") > 60
  ) or (
    # LSN distance - bytes pending to be applied
    label_replace(max by (namespace, job, subname) (cnpg_pg_stat_subscription_buffered_lag_bytes), "cluster", "$1", "job", ".+/(.+)") / 1024^3 > 1
  )
for: 5m
labels:
  severity: warning
  namespace: {{ .namespace }}
  cnpg_cluster: {{ .cluster }}
{{- end -}}

```

## File: charts\paradedb\prometheus_rules\cluster-logical_replication_stopped-critical.yaml
```
{{- $alert := "CNPGClusterLogicalReplicationStoppedCritical" -}}
{{- if not (has $alert .excludeRules) -}}
alert: {{ $alert }}
annotations:
  summary: CNPG Cluster logical replication subscription CRITICAL
  description: |-
    CloudNativePG Cluster's "{{ .namespace }}/{{ .cluster }}" "{{ .labels.subname }}" subscription is in a critical state.

    CRITICAL: The subscription has been stopped for more than 15 minutes. This will lead to significant data divergence and requires immediate intervention.

    Status: {{ .labels.stop_reason }}
    Duration: {{ .value }}s
  runbook_url: https://github.com/paradedb/charts/blob/main/charts/paradedb/docs/runbooks/CNPGClusterLogicalReplicationStopped.md
expr: |
  (
    # Subscription is explicitly disabled
    label_replace(max by (namespace, job, subname) (cnpg_pg_stat_subscription_enabled), "cluster", "$1", "job", ".+/(.+)") == 0
  ) or (
    # Subscription is enabled but stuck (no worker process with significant lag)
    label_replace(max by (namespace, job, subname) (cnpg_pg_stat_subscription_enabled), "cluster", "$1", "job", ".+/(.+)") == 1
    and label_replace(max by (namespace, job, subname) (cnpg_pg_stat_subscription_pid), "cluster", "$1", "job", ".+/(.+)") <= 0
    and label_replace(max by (namespace, job, subname) (cnpg_pg_stat_subscription_buffered_lag_bytes), "cluster", "$1", "job", ".+/(.+)") / 1024^3 > 0.1
  )
for: 15m
labels:
  severity: critical
  namespace: {{ .namespace }}
  cnpg_cluster: {{ .cluster }}
{{- end -}}

```

## File: charts\paradedb\prometheus_rules\cluster-logical_replication_stopped.yaml
```
{{- $alert := "CNPGClusterLogicalReplicationStopped" -}}
{{- if not (has $alert .excludeRules) -}}
alert: {{ $alert }}
annotations:
  summary: CNPG Cluster logical replication subscription stopped
  description: |-
    CloudNativePG Cluster's "{{ .namespace }}/{{ .cluster }}" "{{ .labels.subname }}" subscription is stopped.

    Status: {{ .labels.stop_reason }}

    The subscription is not actively replicating data. This could be intentional (disabled) or due to an issue preventing the subscription from working.
  runbook_url: https://github.com/paradedb/charts/blob/main/charts/paradedb/docs/runbooks/{{ $alert }}.md
expr: |
  (
    # Subscription is explicitly disabled
    label_replace(max by (namespace, job, subname) (cnpg_pg_stat_subscription_enabled), "cluster", "$1", "job", ".+/(.+)") == 0
  ) or (
    # Subscription is enabled but stuck (no worker process with significant lag)
    label_replace(max by (namespace, job, subname) (cnpg_pg_stat_subscription_enabled), "cluster", "$1", "job", ".+/(.+)") == 1
    and label_replace(max by (namespace, job, subname) (cnpg_pg_stat_subscription_pid), "cluster", "$1", "job", ".+/(.+)") <= 0
    and label_replace(max by (namespace, job, subname) (cnpg_pg_stat_subscription_buffered_lag_bytes), "cluster", "$1", "job", ".+/(.+)") / 1024^3 > 0.1
  )
for: 5m
labels:
  severity: warning
  namespace: {{ .namespace }}
  cnpg_cluster: {{ .cluster }}
{{- end -}}

```

## File: charts\paradedb\prometheus_rules\cluster-low_disk_space-critical.yaml
```
{{- $alert := "CNPGClusterLowDiskSpaceCritical" -}}
{{- if not (has $alert .excludeRules) -}}
alert: {{ $alert }}
annotations:
  summary: ParadeDB Instance is running out of disk space!
  description: |-
    ParadeDB CloudNativePG Cluster "{{ .namespace }}/{{ .cluster }}" is running extremely low on disk space. Check attached PVCs! Current disk space usage is {{ .value }}% of the total capacity.
  runbook_url: https://github.com/paradedb/charts/blob/main/charts/paradedb/docs/runbooks/{{ $alert }}.md
expr: |
  max(max by(persistentvolumeclaim) (1 - kubelet_volume_stats_available_bytes{namespace="{{ .namespace }}", persistentvolumeclaim=~"{{ .podSelector }}"} / kubelet_volume_stats_capacity_bytes{namespace="{{ .namespace }}", persistentvolumeclaim=~"{{ .podSelector }}"})) * 100 > 90 OR
  max(max by(persistentvolumeclaim) (1 - kubelet_volume_stats_available_bytes{namespace="{{ .namespace }}", persistentvolumeclaim=~"{{ .podSelector }}-wal"} / kubelet_volume_stats_capacity_bytes{namespace="{{ .namespace }}", persistentvolumeclaim=~"{{ .podSelector }}-wal"})) * 100 > 90 OR
  max(sum by (namespace,persistentvolumeclaim) (kubelet_volume_stats_used_bytes{namespace="{{ .namespace }}", persistentvolumeclaim=~"{{ .podSelector }}-tbs.*"})
      /
      sum by (namespace,persistentvolumeclaim) (kubelet_volume_stats_capacity_bytes{namespace="{{ .namespace }}", persistentvolumeclaim=~"{{ .podSelector }}-tbs.*"})
      *
      on(namespace, persistentvolumeclaim) group_left(volume)
      kube_pod_spec_volumes_persistentvolumeclaims_info{pod=~"{{ .podSelector }}"}
  ) * 100 > 90
for: 5m
labels:
  severity: critical
  namespace: {{ .namespace }}
  cnpg_cluster: {{ .cluster }}
{{- end -}}

```

## File: charts\paradedb\prometheus_rules\cluster-low_disk_space-warning.yaml
```
{{- $alert := "CNPGClusterLowDiskSpaceWarning" -}}
{{- if not (has $alert .excludeRules) -}}
alert: {{ $alert }}
annotations:
  summary: ParadeDB Instance is running out of disk space.
  description: |-
    ParadeDB CloudNativePG Cluster "{{ .namespace }}/{{ .cluster }}" is running low on disk space. Check attached PVCs. Current disk space usage is {{ .value }}% of the total capacity.
  runbook_url: https://github.com/paradedb/charts/blob/main/charts/paradedb/docs/runbooks/{{ $alert }}.md
expr: |
  max(max by(persistentvolumeclaim) (1 - kubelet_volume_stats_available_bytes{namespace="{{ .namespace }}", persistentvolumeclaim=~"{{ .podSelector }}"} / kubelet_volume_stats_capacity_bytes{namespace="{{ .namespace }}", persistentvolumeclaim=~"{{ .podSelector }}"})) * 100 > 80 OR
  max(max by(persistentvolumeclaim) (1 - kubelet_volume_stats_available_bytes{namespace="{{ .namespace }}", persistentvolumeclaim=~"{{ .podSelector }}-wal"} / kubelet_volume_stats_capacity_bytes{namespace="{{ .namespace }}", persistentvolumeclaim=~"{{ .podSelector }}-wal"})) * 100 > 80 OR
  max(sum by (namespace,persistentvolumeclaim) (kubelet_volume_stats_used_bytes{namespace="{{ .namespace }}", persistentvolumeclaim=~"{{ .podSelector }}-tbs.*"})
      /
      sum by (namespace,persistentvolumeclaim) (kubelet_volume_stats_capacity_bytes{namespace="{{ .namespace }}", persistentvolumeclaim=~"{{ .podSelector }}-tbs.*"})
      *
      on(namespace, persistentvolumeclaim) group_left(volume)
      kube_pod_spec_volumes_persistentvolumeclaims_info{pod=~"{{ .podSelector }}"}
  ) * 100 > 80
for: 5m
labels:
  severity: warning
  namespace: {{ .namespace }}
  cnpg_cluster: {{ .cluster }}
{{- end -}}

```

## File: charts\paradedb\prometheus_rules\cluster-offline.yaml
```
{{- $alert := "CNPGClusterOffline" -}}
{{- if not (has $alert .excludeRules) -}}
alert: {{ $alert }}
annotations:
  summary: ParadeDB CNPG Cluster has no running instances!
  description: |-
    ParadeDB CloudNativePG Cluster "{{ .namespace }}/{{ .cluster }}" has no ready instances.

    Having an offline cluster means your applications will not be able to access the database, leading to potential service disruption and/or data loss.
  runbook_url: https://github.com/paradedb/charts/blob/main/charts/paradedb/docs/runbooks/{{ $alert }}.md
expr: |
  (count(cnpg_collector_up{namespace="{{ .namespace }}",pod=~"{{ .podSelector }}"}) OR on() vector(0)) == 0
for: 5m
labels:
  severity: critical
  namespace: {{ .namespace }}
  cnpg_cluster: {{ .cluster }}
{{- end -}}

```

## File: charts\paradedb\prometheus_rules\cluster-physical_replication_lag-critical.yaml
```
{{- $alert := "CNPGClusterPhysicalReplicationLagCritical" -}}
{{- if not (has $alert .excludeRules) -}}
alert: {{ $alert }}
annotations:
  summary: CNPG Cluster very high physical replication lag
  description: |-
    CloudNativePG Cluster "{{ .namespace }}/{{ .cluster }}" is experiencing a very high physical replication lag of {{ .value }}ms.

    High replication lag indicates network issues, busy instances, slow queries or suboptimal configuration.
  runbook_url: https://github.com/paradedb/charts/blob/main/charts/paradedb/docs/runbooks/CNPGClusterPhysicalReplicationLag.md
expr: |
  max(cnpg_pg_replication_lag{namespace="{{ .namespace }}",pod=~"{{ .podSelector }}"}) > 15
for: 5m
labels:
  severity: critical
  namespace: {{ .namespace }}
  cnpg_cluster: {{ .cluster }}
{{- end -}}

```

## File: charts\paradedb\prometheus_rules\cluster-physical_replication_lag-warning.yaml
```
{{- $alert := "CNPGClusterPhysicalReplicationLagWarning" -}}
{{- if not (has $alert .excludeRules) -}}
alert: {{ $alert }}
annotations:
  summary: CNPG Cluster high physical replication lag
  description: |-
    CloudNativePG Cluster "{{ .namespace }}/{{ .cluster }}" is experiencing a high physical replication lag of {{ .value }}ms.

    High replication lag indicates network issues, busy instances, slow queries or suboptimal configuration.
  runbook_url: https://github.com/paradedb/charts/blob/main/charts/paradedb/docs/runbooks/CNPGClusterPhysicalReplicationLag.md
expr: |
  max(cnpg_pg_replication_lag{namespace="{{ .namespace }}",pod=~"{{ .podSelector }}"}) > 1
for: 5m
labels:
  severity: warning
  namespace: {{ .namespace }}
  cnpg_cluster: {{ .cluster }}
{{- end -}}

```

## File: charts\paradedb\prometheus_rules\cluster-zone_spread-warning.yaml
```
{{- $alert := "CNPGClusterZoneSpreadWarning" -}}
{{- if not (has $alert .excludeRules) -}}
alert: {{ $alert }}
annotations:
  summary: Multiple ParadeDB CNPG Cluster instances are in the same availability zone.
  description: |-
    ParadeDB CloudNativePG Cluster "{{ .namespace }}/{{ .cluster }}" has instances in the same availability zone.

    A disaster in one availability zone will lead to a potential service disruption and/or data loss.
  runbook_url: https://github.com/paradedb/charts/blob/main/charts/paradedb/docs/runbooks/{{ $alert }}.md
expr: |
  {{ .Values.cluster.instances }} > count(count by (label_topology_kubernetes_io_zone) (kube_pod_info{namespace="{{ .namespace }}", pod=~"{{ .podSelector }}"} * on(node,instance) group_left(label_topology_kubernetes_io_zone) kube_node_labels)) < 3
for: 5m
labels:
  severity: warning
  namespace: {{ .namespace }}
  cnpg_cluster: {{ .cluster }}
{{- end -}}

```

## File: charts\paradedb\templates\backup-azure-creds.yaml
```
{{- if and .Values.backups.enabled (eq .Values.backups.provider "azure") .Values.backups.secret.create }}
apiVersion: v1
kind: Secret
metadata:
  name: {{ default (printf "%s-backup-azure-creds" (include "cluster.fullname" .)) .Values.backups.secret.name }}
  namespace: {{ include "cluster.namespace" . }}
data:
  AZURE_CONNECTION_STRING: {{ .Values.backups.azure.connectionString | b64enc | quote }}
  AZURE_STORAGE_ACCOUNT: {{ .Values.backups.azure.storageAccount | b64enc | quote }}
  AZURE_STORAGE_KEY: {{ .Values.backups.azure.storageKey | b64enc | quote }}
  AZURE_STORAGE_SAS_TOKEN: {{ .Values.backups.azure.storageSasToken | b64enc | quote }}
{{- end }}

```

## File: charts\paradedb\templates\backup-google-creds.yaml
```
{{- if and .Values.backups.enabled (eq .Values.backups.provider "google") .Values.backups.secret.create }}
apiVersion: v1
kind: Secret
metadata:
  name: {{ default (printf "%s-backup-google-creds" (include "cluster.fullname" .)) .Values.backups.secret.name }}
  namespace: {{ include "cluster.namespace" . }}
data:
  APPLICATION_CREDENTIALS: {{ .Values.backups.google.applicationCredentials | b64enc | quote }}
{{- end }}

```

## File: charts\paradedb\templates\backup-s3-creds.yaml
```
{{- if and .Values.backups.enabled (eq .Values.backups.provider "s3") (not .Values.backups.s3.inheritFromIAMRole) .Values.backups.secret.create }}
apiVersion: v1
kind: Secret
metadata:
  name: {{ default (printf "%s-backup-s3-creds" (include "cluster.fullname" .)) .Values.backups.secret.name }}
  namespace: {{ include "cluster.namespace" . }}
data:
  ACCESS_KEY_ID: {{ required ".Values.backups.s3.accessKey is required, but not specified." .Values.backups.s3.accessKey | b64enc | quote }}
  ACCESS_SECRET_KEY: {{ required ".Values.backups.s3.secretKey is required, but not specified." .Values.backups.s3.secretKey | b64enc | quote }}
{{- end }}

```

## File: charts\paradedb\templates\ca-bundle.yaml
```
{{- if .Values.backups.endpointCA.create }}
apiVersion: v1
kind: Secret
metadata:
  name: {{ .Values.backups.endpointCA.name | default (printf "%s-ca-bundle" (include "cluster.fullname" .)) | quote }}
  namespace: {{ include "cluster.namespace" . }}
data:
  {{ .Values.backups.endpointCA.key | default "ca-bundle.crt" | quote }}: {{ .Values.backups.endpointCA.value }}
{{- end }}

```

## File: charts\paradedb\templates\cluster.yaml
```
apiVersion: postgresql.cnpg.io/v1
kind: Cluster
metadata:
  name: {{ include "cluster.fullname" . }}
  namespace: {{ include "cluster.namespace" . }}
  {{- with .Values.cluster.annotations }}
  annotations:
    {{- toYaml . | nindent 4 }}
  {{- end }}
  labels:
  {{- include "cluster.labels" . | nindent 4 }}
  {{- with .Values.cluster.additionalLabels }}
    {{ toYaml . | nindent 4 }}
  {{- end }}
spec:
  instances: {{ .Values.cluster.instances }}
  {{- include "cluster.image" . | nindent 2 }}
  imagePullPolicy: {{ .Values.cluster.imagePullPolicy }}
  {{- with .Values.cluster.imagePullSecrets }}
  imagePullSecrets:
    {{- . | toYaml | nindent 4 }}
  {{- end }}
  postgresUID: {{ include "cluster.postgresUID" . }}
  postgresGID: {{ include "cluster.postgresGID" . }}
  storage:
    size: {{ .Values.cluster.storage.size }}
    {{- if not (empty .Values.cluster.storage.storageClass) }}
    storageClass: {{ .Values.cluster.storage.storageClass }}
    {{- end }}
  {{- if .Values.cluster.walStorage.enabled }}
  walStorage:
    size: {{ .Values.cluster.walStorage.size }}
    {{- if not (empty .Values.cluster.walStorage.storageClass) }}
    storageClass: {{ .Values.cluster.walStorage.storageClass }}
    {{- end }}
  {{- end }}
  {{- with .Values.cluster.resources }}
  resources:
    {{- toYaml . | nindent 4 }}
  {{ end }}
  {{- with .Values.cluster.affinity }}
  affinity:
    {{- toYaml . | nindent 4 }}
  {{- end }}
  {{- with .Values.cluster.env }}
  env:
    {{- toYaml . | nindent 4 }}
  {{- end }}
  {{- with .Values.cluster.envFrom }}
  envFrom:
    {{- toYaml . | nindent 4 }}
  {{- end }}
  {{- if .Values.cluster.priorityClassName }}
  priorityClassName: {{ .Values.cluster.priorityClassName }}
  {{- end }}

  primaryUpdateMethod: {{ .Values.cluster.primaryUpdateMethod }}
  primaryUpdateStrategy: {{ .Values.cluster.primaryUpdateStrategy }}
  logLevel: {{ .Values.cluster.logLevel }}
  {{- with .Values.cluster.certificates }}
  certificates:
    {{- toYaml . | nindent 4 }}
  {{ end }}
  enableSuperuserAccess: {{ .Values.cluster.enableSuperuserAccess }}
  {{- with .Values.cluster.superuserSecret }}
  superuserSecret:
    name: {{ . }}
  {{ end }}
  enablePDB: {{ .Values.cluster.enablePDB }}
  postgresql:
    {{- if or (eq .Values.type "paradedb") (eq .Values.type "paradedb-enterprise") (not (empty .Values.cluster.postgresql.shared_preload_libraries)) }}
    shared_preload_libraries:
      {{- if or (eq .Values.type "paradedb") (eq .Values.type "paradedb-enterprise") }}
      - pg_search
      - pg_cron
      - pg_stat_statements
      {{- end }}
      {{- with .Values.cluster.postgresql.shared_preload_libraries }}
      {{- toYaml . | nindent 6 }}
      {{- end }}
    {{- end }}
    {{- with .Values.cluster.postgresql.pg_hba }}
    pg_hba:
      {{- toYaml . | nindent 6 }}
    {{- end }}
    {{- with .Values.cluster.postgresql.pg_ident }}
    pg_ident:
      {{- toYaml . | nindent 6 }}
    {{- end }}
    {{- with .Values.cluster.postgresql.ldap  }}
    ldap:
      {{- toYaml . | nindent 6 }}
    {{- end }}
    {{- with .Values.cluster.postgresql.synchronous }}
    synchronous:
      {{- toYaml . | nindent 6 }}
    {{ end }}
    parameters:
      {{ if eq .Values.type "paradedb-enterprise" }}
      hot_standby_feedback: "1"
      {{ end }}
      {{- with .Values.cluster.postgresql.parameters }}
      {{ toYaml . | nindent 6 }}
      {{ end }}
      cron.database_name: postgres

  {{- if not (and (empty .Values.cluster.roles) (empty .Values.cluster.services)) }}
  managed:
    {{- with .Values.cluster.services }}
    services:
      {{- toYaml . | nindent 6 }}
    {{ end }}
    {{- with .Values.cluster.roles }}
    roles:
      {{- toYaml . | nindent 6 }}
    {{ end }}
  {{- end }}

  {{- with .Values.cluster.serviceAccountTemplate }}
  serviceAccountTemplate:
    {{- toYaml . | nindent 4 }}
  {{- end }}

  {{- with .Values.cluster.podSecurityContext }}
  podSecurityContext:
    {{- toYaml . | nindent 4 }}
  {{ end }}

  {{- with .Values.cluster.securityContext }}
  securityContext:
    {{- toYaml . | nindent 4 }}
  {{ end }}

  monitoring:
    disableDefaultQueries: {{ .Values.cluster.monitoring.disableDefaultQueries }}
    {{- if or .Values.cluster.monitoring.instrumentation.paradedbIndex .Values.cluster.monitoring.instrumentation.logicalReplication .Values.cluster.monitoring.instrumentation.pgStatStatements (not (empty .Values.cluster.monitoring.customQueries)) }}
    customQueriesConfigMap:
    {{- if .Values.cluster.monitoring.instrumentation.paradedbIndex }}
      - name: {{ include "cluster.fullname" . }}-monitoring-paradedb-index
        key: custom-queries
    {{- end }}
    {{- if .Values.cluster.monitoring.instrumentation.logicalReplication }}
      - name: {{ include "cluster.fullname" . }}-monitoring-logical-replication
        key: custom-queries
    {{- end }}
    {{- if .Values.cluster.monitoring.instrumentation.pgStatStatements }}
      - name: {{ include "cluster.fullname" . }}-monitoring-pg-stat-statements
        key: custom-queries
    {{- end }}
    {{- if not (empty .Values.cluster.monitoring.customQueries) }}
      - name: {{ include "cluster.fullname" . }}-monitoring-user-metrics
        key: custom-queries
    {{- end }}
    {{- end }}
    {{- if not (empty .Values.cluster.monitoring.customQueriesSecret) }}
    {{- with .Values.cluster.monitoring.customQueriesSecret }}
    customQueriesSecret:
      {{- toYaml . | nindent 6 }}
    {{ end }}
    {{- end }}
  {{ include "cluster.bootstrap" . | nindent 2 }}
  {{ include "cluster.externalClusters" . | nindent 2 }}
  {{ include "cluster.backup" . | nindent 2 }}

```

## File: charts\paradedb\templates\console-statefulset.yaml
```
{{- if .Values.cluster.console.enabled }}
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: {{ include "cluster.fullname" $ }}-console
  namespace: {{ include "cluster.namespace" $ }}
  {{- with .Values.cluster.annotations }}
  annotations:
    {{- toYaml . | nindent 8 }}
  {{- end }}
  labels:
    {{- include "cluster.labels" . | nindent 4 }}
    {{- with .Values.cluster.additionalLabels }}
      {{- toYaml . | nindent 4 }}
    {{- end }}
    app.kubernetes.io/component: console
spec:
  replicas: 1
  selector:
    matchLabels:
      {{- include "cluster.selectorLabels" . | nindent 6 }}
      app.kubernetes.io/component: console
  serviceName: console
  volumeClaimTemplates:
    - metadata:
        name: console-home
      spec:
        accessModes: [ "ReadWriteOnce" ]
        resources:
          requests:
            storage: 1Gi
  template:
    metadata:
      {{- with .Values.cluster.annotations }}
      annotations:
        {{- toYaml . | nindent 8 }}
      {{- end }}
      labels:
        {{- include "cluster.labels" . | nindent 8 }}
        {{- with .Values.cluster.additionalLabels }}
          {{- toYaml . | nindent 8 }}
        {{- end }}
        app.kubernetes.io/component: console
    spec:
      terminationGracePeriodSeconds: 2
      containers:
        - name: console
          image: ubuntu:latest
          command: [ "sh" ]
          args:
            - "-c"
            - |
              apt update
              apt install -y postgresql-client
              apt install -y screen curl wget jq unzip gzip nano vim util-linux less htop
              cat <<EOF > /root/.bashrc
              echo -e "\nHere are some examples for connecting and running queries on the cluster:"
              echo '  nohup psql "$DB_SUPERUSER_URI/<db-name>" -c "SELECT 1;" > command.log 2>&1 &'
              echo -e "\nTo check up on the command, use:"
              echo "  tail -f command.log"
              echo -e "\nYou can also use 'screen' for an interactive session. See https://github.com/paradedb/charts/blob/main/charts/paradedb/docs/long-running-tasks.md for examples."
              echo -e "\n"
              EOF
              sleep infinity
          env:
            - name: DB_APP_URI
              valueFrom:
                secretKeyRef:
                  name: {{ include "cluster.fullname" $ }}-app
                  key: uri
            - name: DB_SUPERUSER_HOST
              valueFrom:
                secretKeyRef:
                  name: {{ include "cluster.fullname" $ }}-superuser
                  key: host
            - name: DB_SUPERUSER_PORT
              valueFrom:
                  secretKeyRef:
                    name: {{ include "cluster.fullname" $ }}-superuser
                    key: port
            - name: DB_SUPERUSER_USER
              valueFrom:
                secretKeyRef:
                  name: {{ include "cluster.fullname" $ }}-superuser
                  key: user
            - name: DB_SUPERUSER_PASSWORD
              valueFrom:
                secretKeyRef:
                  name: {{ include "cluster.fullname" $ }}-superuser
                  key: password
            - name: DB_SUPERUSER_URI
              value: "postgresql://$(DB_SUPERUSER_USER):$(DB_SUPERUSER_PASSWORD)@$(DB_SUPERUSER_HOST):$(DB_SUPERUSER_PORT)"
          volumeMounts:
            - name: console-home
              mountPath: /root
{{- end }}

```

## File: charts\paradedb\templates\databases.yaml
```
{{- range .Values.databases }}
{{- $dbOwner := default .name .owner }}
---
apiVersion: postgresql.cnpg.io/v1
kind: Database
metadata:
  name: {{ include "cluster.fullname" $ }}-{{ .name | replace "_" "-" }}
  namespace: {{ include "cluster.namespace" $ }}
  {{- with $.Values.cluster.annotations }}
  annotations:
    {{- toYaml . | nindent 4 }}
  {{- end }}
  labels:
  {{- include "cluster.labels" $ | nindent 4 }}
  {{- with $.Values.cluster.additionalLabels }}
    {{ toYaml . | nindent 4 }}
  {{- end }}
spec:
  name: {{ .name }}
  cluster:
    name: {{ include "cluster.fullname" $ }}
  ensure: {{ .ensure | default "present" }}
  owner: {{ $dbOwner }}
  template: {{ .template | default "template1" }}
  encoding: {{ .encoding | default "UTF8" }}
  databaseReclaimPolicy: {{ .databaseReclaimPolicy | default "retain" }}
  {{- if hasKey . "isTemplate" }}
  isTemplate: {{ .isTemplate }}
  {{- end }}
  {{- if hasKey . "allowConnections" }}
  allowConnections: {{ .allowConnections }}
  {{- end }}
  {{- if hasKey . "connectionLimit" }}
  connectionLimit: {{ .connectionLimit }}
  {{- end }}
  {{- with .tablespace }}
  tablespace: {{ . }}
  {{- end }}
  {{- with .locale }}
  locale: {{ . }}
  {{- end }}
  {{- with .localeProvider }}
  localeProvider: {{ . }}
  {{- end }}
  {{- with .localeCollate }}
  localeCollate: {{ . }}
  {{- end }}
  {{- with .localeCType }}
  localeCType: {{ . }}
  {{- end }}
  {{- with .icuLocale }}
  icuLocale: {{ . }}
  {{- end }}
  {{- with .icuRules }}
  icuRules: {{ . }}
  {{- end }}
  {{- with .builtinLocale }}
  builtinLocale: {{ . }}
  {{- end }}
  {{- with .collationVersion }}
  collationVersion: {{ . | quote }}
  {{- end }}
  {{- with .schemas }}
  schemas:
  {{- range . }}
    - name: {{ .name }}
      owner: {{ default $dbOwner .owner }}
      ensure: {{ .ensure | default "present" }}
  {{- end }}
  {{- end }}
  {{- with .extensions }}
  extensions:
  {{- range . }}
    {{- $extname := .name }}
    - name: {{ .name }}
      {{- if eq $extname "pg_search" }}
      version: {{ $.Values.version.paradedb | quote }}
      {{- else if not (empty .version) }}
      version: {{ .version | quote }}
      {{- end }}
      {{- with .schema }}
      schema: {{ . }}
      {{- end }}
      ensure: {{ .ensure | default "present" }}
  {{- end }}
  {{- end }}
{{- end }}

```

## File: charts\paradedb\templates\image-catalog.yaml
```
{{ if and .Values.imageCatalog.create (not (empty .Values.imageCatalog.images )) }}
apiVersion: postgresql.cnpg.io/v1
kind: ImageCatalog
metadata:
  name: {{ include "cluster.fullname" . }}
  namespace: {{ include "cluster.namespace" . }}
spec:
  images:
    {{- range $image := .Values.imageCatalog.images }}
    - image: {{ $image.image }}
      major: {{ $image.major }}
    {{- end }}
{{- end }}

```

## File: charts\paradedb\templates\monitoring-logical-replication.yaml
```
{{- if .Values.cluster.monitoring.instrumentation.logicalReplication }}
apiVersion: v1
kind: ConfigMap
metadata:
  name: {{ include "cluster.fullname" . }}-monitoring-logical-replication
  namespace: {{ include "cluster.namespace" . }}
  labels:
    cnpg.io/reload: ""
    {{- include "cluster.labels" . | nindent 4 }}
data:
  custom-queries: |
    pg_stat_subscription:
      query: |
        SELECT current_database() AS datname
             , s.oid AS subid
             , s.subname AS subname
             , subenabled AS enabled
             , worker_type
             , relid
             , pg_wal_lsn_diff(received_lsn, '0/0') AS received_lsn
             , last_msg_send_time
             , last_msg_receipt_time
             , pg_wal_lsn_diff(latest_end_lsn, '0/0') AS latest_end_lsn
             , latest_end_time
             , apply_error_count
             , sync_error_count
             , stats_reset
             , ss.pid
             , CASE
                 WHEN received_lsn IS NOT NULL AND latest_end_lsn IS NOT NULL
                 THEN GREATEST(0, pg_wal_lsn_diff(received_lsn, latest_end_lsn))
                 ELSE NULL
               END AS buffered_lag_bytes
             , CASE
                 WHEN last_msg_receipt_time IS NOT NULL
                 THEN EXTRACT(EPOCH FROM (NOW() - last_msg_receipt_time))
                 ELSE NULL
               END AS receipt_lag_seconds
             , CASE
                 WHEN latest_end_time IS NOT NULL
                 THEN EXTRACT(EPOCH FROM (NOW() - latest_end_time))
                 ELSE NULL
               END AS apply_lag_seconds
        FROM pg_subscription s
        LEFT JOIN pg_stat_subscription ss ON s.oid = ss.subid
        LEFT JOIN pg_stat_subscription_stats sss ON s.oid = sss.subid;
      target_databases: ["*"]
      metrics:
        - datname:
            description: Name of the database
            usage: LABEL
        - subid:
            description: ID of the subscription
            usage: LABEL
        - subname:
            description: Name of the subscription
            usage: LABEL
        - worker_type:
            description: Type of the worker
            usage: LABEL
        - relid:
            description: OID of the relation
            usage: LABEL
        - received_lsn:
            description: Last written LSN received from the publisher
            usage: GAUGE
        - last_msg_send_time:
            description: Timestamp of the last message sent
            usage: GAUGE
        - last_msg_receipt_time:
            description: Timestamp of the last message receipt
            usage: GAUGE
        - latest_end_lsn:
            description: Latest end LSN received
            usage: GAUGE
        - latest_end_time:
            description: Timestamp of the latest end LSN processed
            usage: GAUGE
        - enabled:
            description: Subscription status (enabled/disabled)
            usage: GAUGE
        - apply_error_count:
            description: Number of times an error occurred while applying changes
            usage: GAUGE
        - sync_error_count:
            description: Number of times an error occurred during the initial table synchronization
            usage: GAUGE
        - stats_reset:
            description: Time at which these statistics were last reset
            usage: GAUGE
        - pid:
            description: Process ID of the subscription worker process
            usage: GAUGE
        - buffered_lag_bytes:
            description: Bytes buffered but not yet applied (received_lsn - latest_end_lsn)
            usage: GAUGE
        - receipt_lag_seconds:
            description: Seconds since last message receipt
            usage: GAUGE
        - apply_lag_seconds:
            description: Seconds since last apply operation
            usage: GAUGE
{{- end }}

```

## File: charts\paradedb\templates\monitoring-paradedb-index.yaml
```
{{- if .Values.cluster.monitoring.instrumentation.paradedbIndex }}
apiVersion: v1
kind: ConfigMap
metadata:
  name: {{ include "cluster.fullname" . }}-monitoring-paradedb-index
  namespace: {{ include "cluster.namespace" . }}
  labels:
    cnpg.io/reload: ""
    {{- include "cluster.labels" . | nindent 4 }}
data:
  custom-queries: |
    paradedb_index:
      query: |
        SELECT current_database() as datname
             , n.nspname AS schema
             , c.relname AS relname
             , pg_relation_size(c.oid) AS relation_size
             , COUNT(info.byte_size) AS segments_count
             , MIN(info.byte_size) AS segments_min_size
             , MAX(info.byte_size) AS segments_max_size
             , AVG(info.byte_size) AS segments_avg_size
        FROM pg_class c
        JOIN pg_namespace n ON n.oid = c.relnamespace
        JOIN pg_index i ON i.indexrelid = c.oid
        JOIN pg_am am ON am.oid = c.relam
        JOIN LATERAL paradedb.index_info(c.oid) AS info ON true
        WHERE n.nspname NOT IN ('pg_catalog', 'information_schema')
          AND am.amname = 'bm25'
        GROUP BY n.nspname, c.relname, c.oid;
      target_databases: ["*"]
      predicate_query: "SELECT 1 FROM pg_extension WHERE extname = 'pg_search' AND extversion = '{{ .Values.version.paradedb }}';"
      metrics:
        - datname:
            description: Name of the database
            usage: LABEL
        - schema:
            description: Schema within the database
            usage: LABEL
        - relname:
            description: Index name
            usage: LABEL
        - relation_size:
            description: Full Relation size
            usage: GAUGE
        - segments_count:
            description: Segment count
            usage: GAUGE
        - segments_min_size:
            description: Minimum segment size in bytes
            usage: GAUGE
        - segments_max_size:
            description: Maximum segment size in bytes
            usage: GAUGE
        - segments_avg_size:
            description: Average segment size in bytes
            usage: GAUGE
    paradedb_index_layer:
      query: |
        WITH index_layer_histogram AS (
          SELECT t.relname
               , t.high
               , SUM(i.count) AS count
          FROM paradedb.index_layer_info t
          LEFT JOIN paradedb.index_layer_info i
          ON i.relname = t.relname AND i.high <= t.high
          GROUP BY t.relname, t.high, t.relname
        )
        SELECT current_database() as datname
             , t.relname
             , SUM(t.byte_size)   AS segments_sum
             , SUM(t.count)       AS segments_count
             , ARRAY_AGG(t.high)  AS segments
             , ARRAY_AGG(i.count) AS segments_bucket
        FROM paradedb.index_layer_info t
        LEFT JOIN index_layer_histogram i ON i.relname = t.relname AND i.high = t.high
        GROUP BY datname, t.relname;
      target_databases: ["*"]
      predicate_query: "SELECT 1 FROM pg_extension WHERE extname = 'pg_search' AND extversion = '{{ .Values.version.paradedb }}';"
      metrics:
        - datname:
            description: Name of the database
            usage: LABEL
        - relname:
            description: Index name
            usage: LABEL
        - segments:
            description: Layer segments size distribution
            usage: HISTOGRAM
{{- end }}

```

## File: charts\paradedb\templates\monitoring-pg-stat-statements.yaml
```
{{- if .Values.cluster.monitoring.instrumentation.pgStatStatements }}
apiVersion: v1
kind: ConfigMap
metadata:
  name: {{ include "cluster.fullname" . }}-monitoring-pg-stat-statements
  namespace: {{ include "cluster.namespace" . }}
  labels:
    cnpg.io/reload: ""
    {{- include "cluster.labels" . | nindent 4 }}
data:
  custom-queries: |
    pg_stat_statements:
      query: |
        SELECT d.datname
             , sum(s.calls) AS calls
             , sum(s.total_exec_time) / 1000 AS total_exec_time_seconds
             , sum(s.rows) AS rows
             , sum(s.shared_blks_hit) AS shared_blks_hit
             , sum(s.shared_blks_read) AS shared_blks_read
             , sum(s.blk_read_time) / 1000 AS blk_read_time_seconds
             , sum(s.blk_write_time) / 1000 AS blk_write_time_seconds
        FROM pg_stat_statements s
        JOIN pg_database d ON s.dbid = d.oid
        GROUP BY d.datname;
      target_databases: ["*"]
      predicate_query: "SELECT 1 FROM pg_extension WHERE extname = 'pg_stat_statements';"
      metrics:
        - datname:
            description: Name of the database
            usage: LABEL
        - calls:
            description: Total number of query executions
            usage: COUNTER
        - total_exec_time_seconds:
            description: Total execution time in seconds
            usage: COUNTER
        - rows:
            description: Total number of rows returned or affected
            usage: COUNTER
        - shared_blks_hit:
            description: Total number of shared block cache hits
            usage: COUNTER
        - shared_blks_read:
            description: Total number of shared blocks read from disk
            usage: COUNTER
        - blk_read_time_seconds:
            description: Total block read time in seconds
            usage: COUNTER
        - blk_write_time_seconds:
            description: Total block write time in seconds
            usage: COUNTER
{{- end }}

```

## File: charts\paradedb\templates\monitoring-user-metrics.yaml
```
{{- if not (empty .Values.cluster.monitoring.customQueries) }}
apiVersion: v1
kind: ConfigMap
metadata:
  name: {{ include "cluster.fullname" . }}-monitoring-user-metrics
  namespace: {{ include "cluster.namespace" . }}
  labels:
    cnpg.io/reload: ""
    {{- include "cluster.labels" . | nindent 4 }}
data:
  custom-queries: |
    {{- range .Values.cluster.monitoring.customQueries }}
    {{ .name }}:
      query: {{ .query | quote }}
      {{- with .target_databases }}
      target_databases: {{ . | toJson }}
      {{- end }}
      {{- with .predicate_query }}
      predicate_query: {{ tpl . $ | quote }}
      {{- end }}
      metrics:
        {{- .metrics | toYaml | nindent 8 }}
    {{- end }}
{{- end }}

```

## File: charts\paradedb\templates\NOTES.txt
```
{{- if .Values.pooler -}}
  {{ fail ".Values.pooler has been deprecated. Use .Values.poolers instead." }}
{{- end -}}

{{- if gt (omit .Values.cluster.postgresql "parameters" "synchronous" "pg_hba" "pg_ident" "syncReplicaElectionConstraint" "shared_preload_libraries" "ldap" "promotionTimeout" "enableAlterSystem" | keys | len) 0 -}}
  {{ fail ".Values.cluster.postgresql has been deprecated. Use .Values.cluster.postgresql.parameters instead." }}
{{- end -}}


{{ if .Release.IsInstall }}
The {{ include "cluster.color-info" (include "cluster.fullname" .) }} cluster has been installed successfully.
{{ else if .Release.IsUpgrade }}
The {{ include "cluster.color-info" (include "cluster.fullname" .) }} cluster has been upgraded successfully.
{{ end }}

   ██████   ██                       ██ ████     ██             ██   ██                  ███████    ████████
  ██░░░░██ ░██                      ░██░██░██   ░██            ░██  ░░                  ░██░░░░██  ██░░░░░░██
 ██    ░░  ░██  ██████  ██   ██     ░██░██░░██  ░██  ██████   ██████ ██ ██    ██  █████ ░██   ░██ ██      ░░
░██        ░██ ██░░░░██░██  ░██  ██████░██ ░░██ ░██ ░░░░░░██ ░░░██░ ░██░██   ░██ ██░░░██░███████ ░██
░██        ░██░██   ░██░██  ░██ ██░░░██░██  ░░██░██  ███████   ░██  ░██░░██ ░██ ░███████░██░░░░  ░██    █████
░░██    ██ ░██░██   ░██░██  ░██░██  ░██░██   ░░████ ██░░░░██   ░██  ░██ ░░████  ░██░░░░ ░██      ░░██  ░░░░██
 ░░██████  ███░░██████ ░░██████░░██████░██    ░░███░░████████  ░░██ ░██  ░░██   ░░██████░██       ░░████████
  ░░░░░░  ░░░  ░░░░░░   ░░░░░░  ░░░░░░ ░░      ░░░  ░░░░░░░░    ░░  ░░    ░░     ░░░░░░ ░░         ░░░░░░░░

Cheatsheet
----------

Run Helm Tests:
{{ include "cluster.color-info" (printf "helm test --namespace %s %s" .Release.Namespace .Release.Name) }}

Get a list of all base backups:
{{ include "cluster.color-info" (printf "kubectl --namespace %s get backups --selector cnpg.io/cluster=%s" .Release.Namespace (include "cluster.fullname" .)) }}

Connect to the cluster's primary instance:
{{ include "cluster.color-info" (printf "kubectl --namespace %s exec --stdin --tty services/%s-rw -- bash" .Release.Namespace (include "cluster.fullname" .)) }}

{{ if .Values.cluster.console.enabled -}}
Connect to the console pod for executing long-running tasks (e.g. `CREATE INDEX`):
{{ include "cluster.color-info" (printf "kubectl --namespace %s exec --stdin --tty statefulsets/%s-console -- bash" .Release.Namespace (include "cluster.fullname" .)) }}
{{- end }}

Configuration
-------------

{{- $redundancyColor := "" -}}
{{- if lt (int .Values.cluster.instances) 2 }}
  {{- $redundancyColor = "error" -}}
{{- else if lt (int .Values.cluster.instances) 3 -}}
  {{- $redundancyColor = "warning" -}}
{{- else -}}
  {{- $redundancyColor = "ok" -}}
{{- end }}

{{- $scheduledBackups := (first .Values.backups.scheduledBackups).name -}}
{{- range (rest .Values.backups.scheduledBackups) -}}
  {{ $scheduledBackups = printf "%s, %s" $scheduledBackups .name }}
{{- end -}}
{{- if eq (len .Values.backups.scheduledBackups) 0 }}
  {{- $scheduledBackups = "None" -}}
{{- end -}}

{{- $mode := .Values.mode -}}
{{- $source := "" -}}
{{- if eq .Values.mode "recovery" }}
{{- $mode = printf "%s (%s)" .Values.mode .Values.recovery.method -}}
  {{- if eq .Values.recovery.method "pg_basebackup" }}
    {{- $source = printf "postgresql://%s@%s:%.0f/%s" .Values.recovery.pgBaseBackup.source.username .Values.recovery.pgBaseBackup.source.host .Values.recovery.pgBaseBackup.source.port .Values.recovery.pgBaseBackup.source.database -}}
  {{- end -}}
{{- end -}}

{{- $image := (include "cluster.image" .) | fromYaml -}}
{{- if $image.imageCatalogRef -}}
  {{- $image = printf "%s: %s(%s)" $image.imageCatalogRef.kind $image.imageCatalogRef.name (include "cluster.postgresqlMajor" .) -}}
{{- else if $image.imageName -}}
  {{- $image = $image.imageName -}}
{{- end }}

╭───────────────────┬──────────────────────────────────────────────────────────╮
│ Configuration     │ Value                                                    │
┝━━━━━━━━━━━━━━━━━━━┿━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┥
│ Cluster mode      │ {{ printf "%-56s" $mode }} │
│ Type              │ {{ printf "%-56s" .Values.type }} │
│ Image             │ {{ include "cluster.color-info" (printf "%-56s" $image) }} │
{{- if eq .Values.mode "recovery" }}
│ Source            │ {{ printf "%-56s" $source }} │
{{- end }}
│ Instances         │ {{ include (printf "%s%s" "cluster.color-" $redundancyColor) (printf "%-56s" (toString .Values.cluster.instances)) }} │
│ Backups           │ {{ include (printf "%s%s" "cluster.color-" (ternary "ok" "error" .Values.backups.enabled)) (printf "%-56s" (ternary "Enabled" "Disabled" .Values.backups.enabled)) }} │
{{- if .Values.backups.enabled }}
│ Backup Provider   │ {{ printf "%-56s" (title .Values.backups.provider) }} │
│ Scheduled Backups │ {{ printf "%-56s" $scheduledBackups }} │
{{- end }}
│ Storage           │ {{ printf "%-56s" .Values.cluster.storage.size }} │
│ Storage Class     │ {{ printf "%-56s" (default "Default" .Values.cluster.storage.storageClass) }} │
│ PGBouncer         │ {{ printf "%-56s" (ternary "Enabled" "Disabled" (gt (len .Values.poolers) 0)) }} │
│ Monitoring        │ {{ include (printf "%s%s" "cluster.color-" (ternary "ok" "error" .Values.cluster.monitoring.enabled)) (printf "%-56s" (ternary "Enabled" "Disabled" .Values.cluster.monitoring.enabled)) }} │
╰───────────────────┴──────────────────────────────────────────────────────────╯

{{ if not .Values.backups.enabled }}
  {{- include "cluster.color-error" "Warning! Backups not enabled. Recovery will not be possible! Do not use this configuration in production.\n" }}
{{ end -}}

{{ if lt (int .Values.cluster.instances) 2 }}
  {{- include "cluster.color-error" "Warning! Instance failure will lead to downtime and/or data loss!\n" }}
{{- else if lt (int .Values.cluster.instances) 3 -}}
  {{- include "cluster.color-warning" "Warning! Single instance redundancy available only. Instance failure will put the cluster at risk.\n" }}
{{ end -}}

```

## File: charts\paradedb\templates\origin-azure-creds.yaml
```
{{- if and (eq .Values.mode "replica" ) (eq .Values.replica.origin.objectStore.provider "azure") .Values.replica.origin.objectStore.secret.create }}
apiVersion: v1
kind: Secret
metadata:
  name: {{ default (printf "%s-origin-azure-creds" (include "cluster.fullname" .)) .Values.replica.origin.objectStore.secret.name }}
  namespace: {{ include "cluster.namespace" . }}
data:
  AZURE_CONNECTION_STRING: {{ .Values.replica.origin.objectStore.azure.connectionString | b64enc | quote }}
  AZURE_STORAGE_ACCOUNT: {{ .Values.replica.origin.objectStore.azure.storageAccount | b64enc | quote }}
  AZURE_STORAGE_KEY: {{ .Values.replica.origin.objectStore.azure.storageKey | b64enc | quote }}
  AZURE_STORAGE_SAS_TOKEN: {{ .Values.replica.origin.objectStore.azure.storageSasToken | b64enc | quote }}
{{- end }}

```

## File: charts\paradedb\templates\origin-google-creds.yaml
```
{{- if and (eq .Values.mode "replica" ) (eq .Values.replica.origin.objectStore.provider "google") .Values.replica.origin.objectStore.secret.create }}
apiVersion: v1
kind: Secret
metadata:
  name: {{ default (printf "%s-origin-google-creds" (include "cluster.fullname" .)) .Values.replica.origin.objectStore.secret.name }}
  namespace: {{ include "cluster.namespace" . }}
data:
  APPLICATION_CREDENTIALS: {{ .Values.replica.origin.objectStore.google.applicationCredentials | b64enc | quote }}
{{- end }}

```

## File: charts\paradedb\templates\origin-pg_basebackup-password.yaml
```
{{- if and (eq .Values.mode "replica" ) (not (empty .Values.replica.origin.pg_basebackup.host)) .Values.replica.origin.pg_basebackup.passwordSecret.create }}
apiVersion: v1
kind: Secret
metadata:
  name: {{ default (printf "%s-origin-pg-basebackup-password" (include "cluster.fullname" .)) .Values.replica.origin.pg_basebackup.passwordSecret.name }}
  namespace: {{ include "cluster.namespace" . }}
data:
  {{ .Values.replica.origin.pg_basebackup.passwordSecret.key }}: {{ required ".Values.replica.origin.pg_basebackup.passwordSecret.value required when creating a password secret." .Values.replica.origin.pg_basebackup.passwordSecret.value | b64enc | quote }}
{{- end }}

```

## File: charts\paradedb\templates\origin-s3-creds.yaml
```
{{- if and (eq .Values.mode "replica" ) (eq .Values.replica.origin.objectStore.provider "s3") (not .Values.replica.origin.objectStore.s3.inheritFromIAMRole) .Values.replica.origin.objectStore.secret.create }}
apiVersion: v1
kind: Secret
metadata:
  name: {{ default (printf "%s-origin-s3-creds" (include "cluster.fullname" .)) .Values.replica.origin.objectStore.secret.name }}
  namespace: {{ include "cluster.namespace" . }}
data:
  ACCESS_KEY_ID: {{ required ".Values.replica.origin.objectStore.s3.accessKey is required, but not specified." .Values.replica.origin.objectStore.s3.accessKey | b64enc | quote }}
  ACCESS_SECRET_KEY: {{ required ".Values.replica.origin.objectStore.s3.secretKey is required, but not specified." .Values.replica.origin.objectStore.s3.secretKey | b64enc | quote }}
{{- end }}

```

## File: charts\paradedb\templates\paradedb-dashboard.yaml
```
{{- if .Values.monitoring.grafanaDashboard.create -}}
apiVersion: v1
kind: ConfigMap
metadata:
  name: {{ .Values.monitoring.grafanaDashboard.configMapName }}
  namespace: {{ default .Release.Namespace .Values.monitoring.grafanaDashboard.namespace }}
  {{- with .Values.monitoring.grafanaDashboard.labels }}
  labels:
    {{- toYaml . | nindent 4 }}
  {{- end }}
  {{- with .Values.monitoring.grafanaDashboard.annotations }}
  annotations:
    {{- toYaml . | nindent 4 }}
  {{- end }}
data:
    paradedb.json: |-
{{ .Files.Get "monitoring/paradedb-dashboard.json" | indent 6 }}
{{- end -}}

```

## File: charts\paradedb\templates\podmonitor-cluster.yaml
```
{{- if and .Values.cluster.monitoring.enabled .Values.cluster.monitoring.podMonitor.enabled }}
apiVersion: monitoring.coreos.com/v1
kind: PodMonitor
metadata:
  name: {{ include "cluster.fullname" . }}-cluster-podmonitor
  namespace: {{ include "cluster.namespace" . }}
  labels:
    cnpg.io/cluster: {{ include "cluster.fullname" . }}
    {{- include "cluster.labels" . | nindent 4 }}
    {{- with .Values.cluster.monitoring.podMonitor.labels }}
    {{- toYaml . | nindent 4 }}
    {{- end }}
  {{- with .Values.cluster.annotations }}
  annotations:
    {{- toYaml . | nindent 4 }}
  {{- end }}
spec:
  selector:
    matchLabels:
      cnpg.io/cluster: {{ include "cluster.fullname" . }}
      cnpg.io/podRole: instance
  podMetricsEndpoints:
    - port: metrics
      {{- with .Values.cluster.monitoring.podMonitor.relabelings }}
      relabelings:
        {{- toYaml . | nindent 8 }}
      {{- end }}
      {{- with .Values.cluster.monitoring.podMonitor.metricRelabelings }}
      metricRelabelings:
        {{- toYaml . | nindent 8 }}
      {{- end }}
{{- end }}

```

## File: charts\paradedb\templates\podmonitor-pooler.yaml
```
{{- range .Values.poolers }}
{{- if .monitoring }}
{{- if .monitoring.enabled }}
{{- if .monitoring.podMonitor }}
{{- if .monitoring.podMonitor.enabled }}
---
apiVersion: monitoring.coreos.com/v1
kind: PodMonitor
metadata:
  name: {{ include "cluster.fullname" $ }}-pooler-{{ .name }}-podmonitor
  namespace: {{ include "cluster.namespace" $ }}
  labels:
    cnpg.io/cluster: {{ include "cluster.fullname" $ }}
    cnpg.io/poolerName: {{ include "cluster.fullname" $  }}-pooler-{{ .name }}
    {{- include "cluster.labels" $ | nindent 4 }}
    {{- with $.Values.cluster.monitoring.podMonitor.labels }}
    {{- toYaml . | nindent 4 }}
    {{- end }}
  {{- with $.Values.cluster.annotations }}
  annotations:
    {{- toYaml . | nindent 4 }}
  {{- end }}
spec:
  selector:
    matchLabels:
      cnpg.io/cluster: {{ include "cluster.fullname" $ }}
      cnpg.io/podRole: pooler
      cnpg.io/poolerName: {{ include "cluster.fullname" $  }}-pooler-{{ .name }}
  podMetricsEndpoints:
    - port: metrics
      {{- with .monitoring.podMonitor.relabelings }}
      relabelings:
        {{- toYaml . | nindent 8 }}
      {{- end }}
      {{- with .monitoring.podMonitor.metricRelabelings }}
      metricRelabelings:
        {{- toYaml . | nindent 8 }}
      {{- end }}
{{- end }}
{{- end }}
{{- end }}
{{- end }}
{{- end }}

```

## File: charts\paradedb\templates\pooler.yaml
```
{{- range .Values.poolers }}
---
apiVersion: postgresql.cnpg.io/v1
kind: Pooler
metadata:
  name: {{ include "cluster.fullname" $  }}-pooler-{{ .name }}
  namespace: {{ include "cluster.namespace" $ }}
spec:
  cluster:
    name: {{ include "cluster.fullname" $ }}
  instances: {{ .instances }}
  type: {{ default "rw" .type }}
  pgbouncer:
    poolMode: {{ default "session" .poolMode }}
    {{- with .authQuerySecret }}
    authQuerySecret:
      {{- toYaml . | nindent 6 }}
    {{- end }}
    {{- with .authQuery }}
    authQuery:
      {{- toYaml . | nindent 6 }}
    {{- end }}
    {{- with .parameters }}
    parameters:
      {{- toYaml . | nindent 6 }}
    {{- end }}
    {{- with .pg_hba }}
    pg_hba:
      {{- toYaml . | nindent 6 }}
    {{- end }}
  {{- with .template }}
  template:
    {{- . | toYaml | nindent 4 }}
  {{- end }}
{{- end }}

```

## File: charts\paradedb\templates\prometheus-rule.yaml
```
{{- if and .Values.cluster.monitoring.enabled .Values.cluster.monitoring.prometheusRule.enabled -}}
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  labels:
    {{- include "cluster.labels" . | nindent 4 }}
    {{- with .Values.cluster.additionalLabels }}
      {{ toYaml . | nindent 4 }}
    {{- end }}
  name: {{ include "cluster.fullname" . }}-alert-rules
  namespace: {{ include "cluster.namespace" . }}
spec:
  groups:
    - name: cloudnative-pg/{{ include "cluster.fullname" . }}
      rules:
        {{- $dict := dict "excludeRules" .Values.cluster.monitoring.prometheusRule.excludeRules -}}
        {{- $_ := set $dict "value"       "{{ $value }}" -}}
        {{- $_ := set $dict "namespace"   .Release.Namespace -}}
        {{- $_ := set $dict "cluster"     (include "cluster.fullname" .) -}}
        {{- $_ := set $dict "labels"      (dict "job" "{{ $labels.job }}" "node" "{{ $labels.node }}" "pod" "{{ $labels.pod }}" "subname" "{{ $labels.subname }}" "lag_type" "{{ $labels.lag_type }}" "stop_reason" "{{ $labels.stop_reason }}") -}}
        {{- $_ := set $dict "podSelector" (printf "%s-([1-9][0-9]*)$" (include "cluster.fullname" .)) -}}
        {{- $_ := set $dict "Values"      .Values -}}
        {{- $_ := set $dict "Template"    .Template -}}
        {{- range $path, $_ := .Files.Glob  "prometheus_rules/**.yaml" }}
        {{- $tpl := tpl ($.Files.Get $path) $dict | nindent 10 | trim -}}
        {{- with $tpl }}
        - {{ $tpl }}
        {{- end -}}
        {{- end -}}
{{ end }}

```

## File: charts\paradedb\templates\recovery-azure-creds.yaml
```
{{- if and (eq .Values.mode "recovery" ) (eq .Values.recovery.method "object_store") (eq .Values.recovery.provider "azure") .Values.recovery.secret.create }}
apiVersion: v1
kind: Secret
metadata:
  name: {{ default (printf "%s-recovery-azure-creds" (include "cluster.fullname" .)) .Values.recovery.secret.name }}
  namespace: {{ include "cluster.namespace" . }}
data:
  AZURE_CONNECTION_STRING: {{ .Values.recovery.azure.connectionString | b64enc | quote }}
  AZURE_STORAGE_ACCOUNT: {{ .Values.recovery.azure.storageAccount | b64enc | quote }}
  AZURE_STORAGE_KEY: {{ .Values.recovery.azure.storageKey | b64enc | quote }}
  AZURE_STORAGE_SAS_TOKEN: {{ .Values.recovery.azure.storageSasToken | b64enc | quote }}
{{- end }}

```

## File: charts\paradedb\templates\recovery-google-creds.yaml
```
{{- if and (eq .Values.mode "recovery" ) (eq .Values.recovery.method "object_store") (eq .Values.recovery.provider "google") .Values.recovery.secret.create }}
apiVersion: v1
kind: Secret
metadata:
  name: {{ default (printf "%s-recovery-google-creds" (include "cluster.fullname" .)) .Values.recovery.secret.name }}
  namespace: {{ include "cluster.namespace" . }}
data:
  APPLICATION_CREDENTIALS: {{ .Values.recovery.google.applicationCredentials | b64enc | quote }}
{{- end }}

```

## File: charts\paradedb\templates\recovery-pg_basebackup-password.yaml
```
{{- if and (eq .Values.mode "recovery") (eq .Values.recovery.method "pg_basebackup") .Values.recovery.pgBaseBackup.source.passwordSecret.create }}
apiVersion: v1
kind: Secret
metadata:
  name: {{ default (printf "%s-pg-basebackup-password" (include "cluster.fullname" .)) .Values.recovery.pgBaseBackup.source.passwordSecret.name }}
  namespace: {{ include "cluster.namespace" . }}
data:
  {{ .Values.recovery.pgBaseBackup.source.passwordSecret.key }}: {{ required ".Values.recovery.pgBaseBackup.source.passwordSecret.value required when creating a password secret." .Values.recovery.pgBaseBackup.source.passwordSecret.value | b64enc | quote }}
{{- end }}

```

## File: charts\paradedb\templates\recovery-s3-creds.yaml
```
{{- if and (eq .Values.mode "recovery" ) (eq .Values.recovery.method "object_store") (eq .Values.recovery.provider "s3") (not .Values.recovery.s3.inheritFromIAMRole) .Values.recovery.secret.create }}
apiVersion: v1
kind: Secret
metadata:
  name: {{ default (printf "%s-recovery-s3-creds" (include "cluster.fullname" .)) .Values.recovery.secret.name }}
  namespace: {{ include "cluster.namespace" . }}
data:
  ACCESS_KEY_ID: {{ required ".Values.recovery.s3.accessKey is required, but not specified." .Values.recovery.s3.accessKey | b64enc | quote }}
  ACCESS_SECRET_KEY: {{ required ".Values.recovery.s3.secretKey is required, but not specified." .Values.recovery.s3.secretKey | b64enc | quote }}
{{- end }}

```

## File: charts\paradedb\templates\scheduled-backups.yaml
```
{{ if .Values.backups.enabled }}
{{ $context := . -}}
{{ range .Values.backups.scheduledBackups -}}
---
apiVersion: postgresql.cnpg.io/v1
kind: ScheduledBackup
metadata:
  name: {{ include "cluster.fullname" $context }}-{{ .name }}
  namespace: {{ include "cluster.namespace" $context }}
  labels:
    {{- include "cluster.labels" $context | nindent 4 }}
spec:
  immediate: true
  schedule: {{ .schedule | quote }}
  method: {{ .method }}
  backupOwnerReference: {{ .backupOwnerReference }}
  cluster:
    name: {{ include "cluster.fullname" $context }}
{{ end -}}
{{ end }}

```

## File: charts\paradedb\templates\tests\ping.yaml
```
apiVersion: batch/v1
kind: Job
metadata:
  name: {{ include "cluster.fullname" . }}-ping-test
  namespace: {{ include "cluster.namespace" . }}
  labels:
    app.kubernetes.io/component: database-ping-test
  annotations:
    "helm.sh/hook": test
    "helm.sh/hook-delete-policy": before-hook-creation,hook-succeeded
spec:
  template:
    metadata:
      name: {{ include "cluster.fullname" . }}-ping-test
      labels:
        app.kubernetes.io/component: database-ping-test
    spec:
      restartPolicy: Never
      containers:
        - name: alpine
          image: alpine:3.17
          command: [ 'sh' ]
          env:
            - name: PGUSER
              valueFrom:
                secretKeyRef:
                  name: {{ include "cluster.fullname" . }}-app
                  key: username
            - name: PGPASS
              valueFrom:
                secretKeyRef:
                  name: {{ include "cluster.fullname" . }}-app
                  key: password
            - name: PGDBNAME
              valueFrom:
                secretKeyRef:
                  name: {{ include "cluster.fullname" . }}-app
                  key: dbname
                  optional: true
          args:
            - "-c"
            - >-
              apk add postgresql-client &&
              psql "postgresql://$PGUSER:$PGPASS@{{ include "cluster.fullname" . }}-rw.{{ include "cluster.namespace" . }}.svc.cluster.local:5432/${PGDBNAME:-$PGUSER}" -c 'SELECT 1'

```

## File: charts\paradedb\test\console-statefulset\01-console_test_cluster-assert.yaml
```
apiVersion: postgresql.cnpg.io/v1
kind: Cluster
metadata:
  name: console-test-paradedb
---
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: console-test-paradedb-console

```

## File: charts\paradedb\test\console-statefulset\01-console_test_cluster.yaml
```
type: paradedb
mode: standalone
version:
  postgresql: "18"
  paradedb: "0.22.3"
cluster:
  instances: 1
  console:
    enabled: true
backups:
  enabled: false

```

## File: charts\paradedb\test\console-statefulset\chainsaw-test.yaml
```
##
# Tests the correct deployment of the console StatefulSet
apiVersion: chainsaw.kyverno.io/v1alpha1
kind: Test
metadata:
  name: console-statefulset
spec:
  timeouts:
    apply: 1s
    assert: 10s
    cleanup: 1m
    exec: 5m
  steps:
    - name: Install a cluster with a console enabled
      try:
        - script:
            content: |
              helm upgrade \
                --install \
                --namespace $NAMESPACE \
                --values ./01-console_test_cluster.yaml \
                --wait \
                console-test ../../
        - assert:
            file: ./01-console_test_cluster-assert.yaml
        - script:
            content: |
              kubectl --namespace $NAMESPACE wait --for=condition=ready clusters.postgresql.cnpg.io/console-test-paradedb --timeout=60s
              kubectl --namespace $NAMESPACE wait --for=condition=ready pod/console-test-paradedb-console-0 --timeout=60s
              kubectl --namespace $NAMESPACE exec pod/console-test-paradedb-console-0 -- bash -c 'while true; do command -v psql && break || sleep 2; done'
              echo 'nohup psql $DB_SUPERUSER_URI -c "SELECT PG_SLEEP(120);" 2>&1 > command.log &' | kubectl --namespace $NAMESPACE exec --stdin pod/console-test-paradedb-console-0 -- bash &
              sleep 60
              PSQL_RUNNING=$(kubectl --namespace $NAMESPACE exec statefulsets/console-test-paradedb-console -- bash -c 'ps -ef | grep psql | wc -l')
              echo "PSQL_RUNNING: $PSQL_RUNNING"
              [ $PSQL_RUNNING -gt 3 ] || exit 1
    - name: Cleanup
      try:
        - script:
            content: |
              helm uninstall --namespace $NAMESPACE console-test

```

## File: charts\paradedb\test\database-management\01-database-parameters-assert.yaml
```
apiVersion: postgresql.cnpg.io/v1
kind: Database
metadata:
  name: database-parameters-paradedb-default-db
spec:
  name: default_db
  cluster:
    name: database-parameters-paradedb
  ensure: present
  owner: test-owner
  template: template1
  encoding: UTF8
  databaseReclaimPolicy: retain
---
apiVersion: postgresql.cnpg.io/v1
kind: Database
metadata:
  name: database-parameters-paradedb-test-db-icu
spec:
  name: test-db-icu
  cluster:
    name: database-parameters-paradedb
  ensure: present
  owner: test-owner
  template: template0
  encoding: UTF16
  connectionLimit: 100
  tablespace: test-space
  databaseReclaimPolicy: delete
  isTemplate: true
  locale: "en_GB.utf8"
  localeProvider: icu
  localeCollate: "en_GB.utf8"
  localeCType: "en_GB.utf8"
  icuLocale: "en_GB"
  icuRules: "en_GB"
  collationVersion: "1"
  schemas:
    - name: test-schema
      owner: test-owner
      ensure: absent
  extensions:
    - name: pg_search
      ensure: absent
      version: "0.19.11"
      schema: test-schema

---
apiVersion: postgresql.cnpg.io/v1
kind: Database
metadata:
  name: database-parameters-paradedb-test-db-builtin
spec:
  name: test-db-builtin
  cluster:
    name: database-parameters-paradedb
  ensure: present
  owner: test-owner
  template: template0
  encoding: UTF16
  connectionLimit: 100
  tablespace: test-space
  databaseReclaimPolicy: delete
  isTemplate: true
  locale: "en_GB.utf8"
  localeProvider: builtin
  localeCollate: "en_GB.utf8"
  localeCType: "en_GB.utf8"
  builtinLocale: "en_GB.utf8"
  collationVersion: "1"
  schemas:
    - name: test-schema
      owner: test-owner
      ensure: absent
  extensions:
    - name: pg_search
      ensure: absent
      version: "0.19.11"
      schema: test-schema

```

## File: charts\paradedb\test\database-management\01-database-parameters.yaml
```
type: paradedb
version:
  postgresql: "17"
  paradedb: "0.19.11"

cluster:
  instances: 1

databases:
  - name: default_db
    ensure: present
    owner: test-owner

  - name: test-db-icu
    ensure: present
    owner: test-owner
    template: template0
    encoding: UTF16
    connectionLimit: 100
    tablespace: test-space
    databaseReclaimPolicy: delete
    isTemplate: true
    locale: "en_GB.utf8"
    localeProvider: icu
    localeCollate: "en_GB.utf8"
    localeCType: "en_GB.utf8"
    icuLocale: "en_GB"
    icuRules: "en_GB"
    collationVersion: "1"
    schemas:
      - name: test-schema
        owner: test-owner
        ensure: absent
    extensions:
      - name: pg_search
        ensure: absent
        version: "0.19.11"
        schema: test-schema

  - name: test-db-builtin
    ensure: present
    owner: test-owner
    template: template0
    encoding: UTF16
    connectionLimit: 100
    tablespace: test-space
    databaseReclaimPolicy: delete
    isTemplate: true
    locale: "en_GB.utf8"
    localeProvider: builtin
    localeCollate: "en_GB.utf8"
    localeCType: "en_GB.utf8"
    builtinLocale: "en_GB.utf8"
    collationVersion: "1"
    schemas:
      - name: test-schema
        owner: test-owner
        ensure: absent
    extensions:
      - name: pg_search
        ensure: absent
        version: "0.19.11"
        schema: test-schema

```

## File: charts\paradedb\test\database-management\02-extension-upgrade-init-assert.yaml
```
apiVersion: postgresql.cnpg.io/v1
kind: Cluster
metadata:
  name: extension-upgrade-paradedb
status:
  readyInstances: 2
  phase: Cluster in healthy state
---
apiVersion: postgresql.cnpg.io/v1
kind: Database
metadata:
  name: extension-upgrade-paradedb-paradedb
spec:
  name: paradedb
  cluster:
    name: extension-upgrade-paradedb
  ensure: present
  owner: paradedb
  template: template1
  encoding: UTF8
  databaseReclaimPolicy: retain
  extensions:
    - name: pg_search
      ensure: present
      version: "0.19.10"

```

## File: charts\paradedb\test\database-management\02-extension-upgrade-init.yaml
```
type: paradedb
version:
  postgresql: "17"
  paradedb: "0.19.10"

cluster:
  instances: 2

databases:
  - name: paradedb
    ensure: present
    owner: paradedb
    encoding: UTF8
    extensions:
      - name: pg_search
        ensure: present

```

## File: charts\paradedb\test\database-management\03-paradedb_extension_check-assert.yaml
```
apiVersion: batch/v1
kind: Job
metadata:
  name: paradedb-version-check-before
status:
  succeeded: 1

```

## File: charts\paradedb\test\database-management\03-paradedb_extension_check.yaml
```
apiVersion: batch/v1
kind: Job
metadata:
  name: paradedb-version-check-before
spec:
  template:
    spec:
      restartPolicy: OnFailure
      containers:
      - name: data-test
        env:
          - name: DB_URI
            valueFrom:
              secretKeyRef:
                name: extension-upgrade-paradedb-app
                key: uri
        image: alpine:3.19
        command: ['sh', '-c']
        args:
          - |
            apk --no-cache add postgresql-client
            PG_SEARCH_VERSION=$(psql "$DB_URI" -t) <<-EOSQL
              SELECT version FROM paradedb.version_info();
            EOSQL
            echo $PG_SEARCH_VERSION
            test "$PG_SEARCH_VERSION" = " 0.19.10"

            EXTVERSION=$(psql "$DB_URI" -t) <<-EOSQL
              SELECT extversion FROM pg_extension WHERE extname = 'pg_search';
            EOSQL
            echo $EXTVERSION
            test "$EXTVERSION" = " 0.19.10"

```

## File: charts\paradedb\test\database-management\04-extension-upgrade-post-assert.yaml
```
apiVersion: postgresql.cnpg.io/v1
kind: Cluster
metadata:
  name: extension-upgrade-paradedb
status:
  readyInstances: 2
  phase: Cluster in healthy state
---
apiVersion: postgresql.cnpg.io/v1
kind: Database
metadata:
  name: extension-upgrade-paradedb-paradedb
spec:
  name: paradedb
  cluster:
    name: extension-upgrade-paradedb
  ensure: present
  owner: paradedb
  template: template1
  encoding: UTF8
  databaseReclaimPolicy: retain
  extensions:
    - name: pg_search
      ensure: present
      version: "0.19.11"

```

## File: charts\paradedb\test\database-management\04-extension-upgrade-post.yaml
```
type: paradedb
version:
  postgresql: "17"
  paradedb: "0.19.11"

cluster:
  instances: 2

databases:
  - name: paradedb
    ensure: present
    owner: paradedb
    encoding: UTF8
    extensions:
      - name: pg_search
        ensure: present

```

## File: charts\paradedb\test\database-management\05-paradedb_extension_check-assert.yaml
```
apiVersion: batch/v1
kind: Job
metadata:
  name: paradedb-version-check-after
status:
  succeeded: 1

```

## File: charts\paradedb\test\database-management\05-paradedb_extension_check.yaml
```
apiVersion: batch/v1
kind: Job
metadata:
  name: paradedb-version-check-after
spec:
  template:
    spec:
      restartPolicy: OnFailure
      containers:
      - name: data-test
        env:
          - name: DB_URI
            valueFrom:
              secretKeyRef:
                name: extension-upgrade-paradedb-app
                key: uri
        image: alpine:3.19
        command: ['sh', '-c']
        args:
          - |
            apk --no-cache add postgresql-client
            PG_SEARCH_VERSION=$(psql "$DB_URI" -t) <<-EOSQL
              SELECT version FROM paradedb.version_info();
            EOSQL
            echo $PG_SEARCH_VERSION
            test "$PG_SEARCH_VERSION" = " 0.19.11"

            EXTVERSION=$(psql "$DB_URI" -t) <<-EOSQL
              SELECT extversion FROM pg_extension WHERE extname = 'pg_search';
            EOSQL
            echo $EXTVERSION
            test "$EXTVERSION" = " 0.19.11"

```

## File: charts\paradedb\test\database-management\chainsaw-test.yaml
```
apiVersion: chainsaw.kyverno.io/v1alpha1
kind: Test
metadata:
  name: database-management
spec:
  timeouts:
    apply: 1s
    assert: 300s
    cleanup: 60s
  steps:
    - name: database-parameters
      timeouts:
        apply: 1s
        assert: 5s
        cleanup: 30s
      try:
        - script:
            content: |
              helm upgrade \
                --install \
                --namespace $NAMESPACE \
                --values ./01-database-parameters.yaml \
                --wait \
                database-parameters ../../
        - assert:
            file: ./01-database-parameters-assert.yaml

    - name: Provision a cluster with a database with the ParadeDB extension
      try:
        - script:
            content: |
              helm upgrade \
                --install \
                --namespace $NAMESPACE \
                --values ./02-extension-upgrade-init.yaml \
                --wait \
                extension-upgrade ../../
        - assert:
            file: ./02-extension-upgrade-init-assert.yaml
      catch:
        - describe:
            apiVersion: postgresql.cnpg.io/v1
            kind: Cluster
            name: extension-upgrade-paradedb
        - podLogs:
            selector: cnpg.io/cluster=extension-upgrade-paradedb
        - script:
            content: |
              echo "=== Cluster Status ==="
              kubectl get cluster extension-upgrade-paradedb -n $NAMESPACE -o yaml | grep -A 50 "status:"
              echo "=== Pod Status ==="
              kubectl get pods -n $NAMESPACE -l cnpg.io/cluster=extension-upgrade-paradedb -o wide
              echo "=== Pod Events ==="
              kubectl get events -n $NAMESPACE --sort-by='.lastTimestamp' | tail -30

    - name: Verify the ParadeDB extension version before upgrade
      try:
        - apply:
            file: ./03-paradedb_extension_check.yaml
        - assert:
            file: ./03-paradedb_extension_check-assert.yaml

    - name: Upgrade the ParadeDB cluster and the extension
      try:
        - script:
            content: |
              helm upgrade \
                --install \
                --namespace $NAMESPACE \
                --values ./04-extension-upgrade-post.yaml \
                --wait \
                extension-upgrade ../../
        - assert:
            file: ./04-extension-upgrade-post-assert.yaml

    - name: Verify the ParadeDB extension version after upgrade
      try:
        - apply:
            file: ./05-paradedb_extension_check.yaml
        - assert:
            file: ./05-paradedb_extension_check-assert.yaml

    - name: Cleanup
      try:
        - script:
            content: |
              helm uninstall --namespace $NAMESPACE database-parameters
              helm uninstall --namespace $NAMESPACE extension-upgrade

```

## File: charts\paradedb\test\monitoring\01-monitoring_cluster-assert.yaml
```
apiVersion: postgresql.cnpg.io/v1
kind: Cluster
metadata:
  name: monitoring-paradedb
  labels:
    foo: bar
  annotations:
    foo: bar
spec:
  instances: 1
  storage:
    size: 256Mi
    storageClass: standard
  monitoring:
      disableDefaultQueries: true
      customQueriesConfigMap:
        - name: monitoring-paradedb-monitoring-paradedb-index
          key: custom-queries
        - name: monitoring-paradedb-monitoring-logical-replication
          key: custom-queries
        - name: monitoring-paradedb-monitoring-pg-stat-statements
          key: custom-queries
        - name: monitoring-paradedb-monitoring-user-metrics
          key: custom-queries
      enablePodMonitor: false
status:
  readyInstances: 1
---
apiVersion: monitoring.coreos.com/v1
kind: PodMonitor
metadata:
  labels:
    cnpg.io/cluster: monitoring-paradedb
    team-name: test-team
    environment: test
spec:
  selector:
    matchLabels:
      cnpg.io/cluster: monitoring-paradedb
      cnpg.io/podRole: instance
  podMetricsEndpoints:
    - relabelings:
        - targetLabel: environment
          replacement: test
        - targetLabel: team
          replacement: alpha
      metricRelabelings:
        - action: replace
          sourceLabels:
            - cluster
          targetLabel: cnpg_cluster
        - action: labeldrop
          regex: cluster
---
apiVersion: monitoring.coreos.com/v1
kind: PodMonitor
spec:
  selector:
    matchLabels:
      cnpg.io/cluster: monitoring-paradedb
      cnpg.io/poolerName: monitoring-paradedb-pooler-rw
      cnpg.io/podRole: pooler
  podMetricsEndpoints:
    - relabelings:
        - targetLabel: type
          replacement: rw
          action: replace
        - targetLabel: team
          replacement: alpha
          action: replace
      metricRelabelings:
        - action: replace
          sourceLabels:
            - cluster
          targetLabel: cnpg_cluster
        - action: labeldrop
          regex: cluster
---
apiVersion: monitoring.coreos.com/v1
kind: PodMonitor
spec:
  selector:
    matchLabels:
      cnpg.io/cluster: monitoring-paradedb
      cnpg.io/poolerName: monitoring-paradedb-pooler-ro
      cnpg.io/podRole: pooler
  podMetricsEndpoints:
    - relabelings:
        - targetLabel: type
          replacement: ro
          action: replace
        - targetLabel: team
          replacement: alpha
          action: replace
      metricRelabelings:
        - action: replace
          sourceLabels:
            - cluster
          targetLabel: cnpg_cluster
        - action: labeldrop
          regex: cluster
---
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: monitoring-paradedb-alert-rules
---
apiVersion: v1
kind: ConfigMap
metadata:
  name: monitoring-paradedb-monitoring-user-metrics
data:
  custom-queries: |
    pg_cache_hit_ratio:
      query: "SELECT current_database() as datname, sum(heap_blks_hit) / (sum(heap_blks_hit) + sum(heap_blks_read)) as ratio FROM pg_statio_user_tables;"
      target_databases: ["*"]
      predicate_query: "SELECT 'paradedb';"
      metrics:
        - datname:
            description: Name of the database
            usage: LABEL
        - ratio:
            description: Cache hit ratio
            usage: GAUGE
---
apiVersion: v1
kind: ConfigMap
metadata:
  name: monitoring-paradedb-monitoring-paradedb-index
---
apiVersion: v1
kind: ConfigMap
metadata:
  name: monitoring-paradedb-monitoring-logical-replication
---
apiVersion: v1
kind: ConfigMap
metadata:
  name: monitoring-paradedb-monitoring-pg-stat-statements
---
apiVersion: v1
kind: ConfigMap
metadata:
  name: paradedb-grafana-dashboard
  labels:
    grafana_dashboard: "1"

```

## File: charts\paradedb\test\monitoring\01-monitoring_cluster.yaml
```
type: paradedb
mode: standalone
cluster:
  instances: 1
  postgresql:
    parameters:
      wal_level: "logical"
      max_worker_processes: "20"
      max_parallel_workers: "15"
      max_wal_senders: "10"
      max_replication_slots: "10"
    pg_hba:
      - host   publisher  postgres  all     md5
  storage:
    size: 256Mi
    storageClass: standard
  monitoring:
    enabled: true
    disableDefaultQueries: true
    instrumentation:
      paradedbIndex: true
      logicalReplication: true
      pgStatStatements: true
    customQueries:
      - name: "pg_cache_hit_ratio"
        query: "SELECT current_database() as datname, sum(heap_blks_hit) / (sum(heap_blks_hit) + sum(heap_blks_read)) as ratio FROM pg_statio_user_tables;"
        target_databases: ["*"]
        predicate_query: "SELECT '{{ .Values.type }}';"
        metrics:
          - datname:
              usage: "LABEL"
              description: "Name of the database"
          - ratio:
              usage: GAUGE
              description: "Cache hit ratio"
    podMonitor:
      labels:
        team-name: test-team
        environment: test
      relabelings:
        - targetLabel: environment
          replacement: test
        - targetLabel: team
          replacement: alpha
      metricRelabelings:
        - action: replace
          sourceLabels:
            - cluster
          targetLabel: cnpg_cluster
        - action: labeldrop
          regex: cluster
  additionalLabels:
    foo: bar
  annotations:
    foo: bar
backups:
  enabled: false
poolers:
  - name: rw
    type: rw
    instances: 1
    monitoring:
      enabled: true
      podMonitor:
        enabled: true
        relabelings:
          - targetLabel: type
            replacement: rw
          - targetLabel: team
            replacement: alpha
        metricRelabelings:
          - action: replace
            sourceLabels:
              - cluster
            targetLabel: cnpg_cluster
          - action: labeldrop
            regex: cluster
  - name: ro
    type: ro
    instances: 1
    monitoring:
      enabled: true
      podMonitor:
        enabled: true
        relabelings:
          - targetLabel: type
            replacement: ro
          - targetLabel: team
            replacement: alpha
        metricRelabelings:
          - action: replace
            sourceLabels:
              - cluster
            targetLabel: cnpg_cluster
          - action: labeldrop
            regex: cluster
monitoring:
  grafanaDashboard:
    create: true
    configMapName: "paradedb-grafana-dashboard"
    labels:
      grafana_dashboard: "1"

```

## File: charts\paradedb\test\monitoring\02-logical-replication-assert.yaml
```
apiVersion: batch/v1
kind: Job
metadata:
  name: logical-replication
status:
  succeeded: 1

```

## File: charts\paradedb\test\monitoring\02-logical-replication.yaml
```
apiVersion: batch/v1
kind: Job
metadata:
  name: logical-replication
spec:
  template:
    spec:
      restartPolicy: OnFailure
      containers:
      - name: logical-replication
        image: alpine:3.19
        command: ['sh', '-c']
        env:
          - name: DB_URI
            valueFrom:
              secretKeyRef:
                name: monitoring-paradedb-superuser
                key: uri
          - name: DB_USER
            valueFrom:
              secretKeyRef:
                name: monitoring-paradedb-superuser
                key: user
          - name: DB_PASS
            valueFrom:
              secretKeyRef:
                name: monitoring-paradedb-superuser
                key: password
          - name: DB_HOST
            valueFrom:
              secretKeyRef:
                name: monitoring-paradedb-superuser
                key: host
        args:
          - |
            apk --no-cache add postgresql-client
            set -e
            DB_URI=$(echo $DB_URI | sed "s|/\*|/|" )
            DB_URI_PUBLISHER=$(echo $DB_URI | sed "s|:5432\/*|:5432/publisher|" )
            DB_URI_SUBSCRIBER=$(echo $DB_URI | sed "s|:5432\/*|:5432/subscriber|" )
            echo "DB_URI: $DB_URI"
            echo "DB_URI_PUBLISHER: $DB_URI_PUBLISHER"
            echo "DB_URI_SUBSCRIBER: $DB_URI_SUBSCRIBER"
            echo "Creating publisher and subscriber databases..."
            # Connect to ParadeDB and create the databases
            psql $DB_URI -c "CREATE DATABASE publisher;"
            psql $DB_URI -c "CREATE DATABASE subscriber;"

            # Configure publisher
            psql $DB_URI_PUBLISHER -c "CREATE TABLE test_table (id SERIAL PRIMARY KEY, data TEXT);"
            psql $DB_URI_PUBLISHER -c "CREATE PUBLICATION test_pub FOR TABLE test_table;"
            psql $DB_URI_PUBLISHER -c "SELECT pg_create_logical_replication_slot('test_sub_slot', 'pgoutput');"

            # Configure subscriber
            psql $DB_URI_SUBSCRIBER -c "CREATE TABLE test_table (id SERIAL PRIMARY KEY, data TEXT);"
            psql $DB_URI_SUBSCRIBER -c "CREATE SUBSCRIPTION test_sub CONNECTION 'host=monitoring-paradedb-rw user=$DB_USER password=$DB_PASS dbname=publisher' PUBLICATION test_pub WITH (slot_name = 'test_sub_slot', create_slot = false);"

            # Insert test data
            psql $DB_URI_PUBLISHER -c "INSERT INTO test_table (data) VALUES ('test data');"

            echo "Logical replication setup complete."

```

## File: charts\paradedb\test\monitoring\02-paradedb-assert.yaml
```
apiVersion: batch/v1
kind: Job
metadata:
  name: paradedb
status:
  succeeded: 1

```

## File: charts\paradedb\test\monitoring\02-paradedb.yaml
```
apiVersion: batch/v1
kind: Job
metadata:
  name: paradedb
spec:
  template:
    spec:
      restartPolicy: OnFailure
      containers:
      - name: paradedb
        image: alpine:3.19
        command: ['sh', '-c']
        env:
          - name: DB_URI
            valueFrom:
              secretKeyRef:
                name: monitoring-paradedb-app
                key: uri
        args:
          - |
            apk --no-cache add postgresql-client
            set -e
            psql $DB_URI -c "CALL paradedb.create_bm25_test_table(schema_name => 'public', table_name => 'mock_items');"
            psql $DB_URI -c "CREATE INDEX search_idx ON mock_items USING bm25 (id, description, category, rating, in_stock, created_at, metadata, weight_range) WITH (key_field='id');"

```

## File: charts\paradedb\test\monitoring\03-metrics-test-assert.yaml
```
apiVersion: batch/v1
kind: Job
metadata:
  name: metrics-test
status:
  succeeded: 1

```

## File: charts\paradedb\test\monitoring\03-metrics-test.yaml
```
---
apiVersion: v1
kind: ServiceAccount
metadata:
  name: pod-reader
---
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: pod-reader
rules:
  - apiGroups: [""]
    resources: ["pods"]
    verbs: ["get","list","watch"]
---
kind: RoleBinding
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  name: pod-reader-binding
subjects:
  - kind: ServiceAccount
    name: pod-reader
roleRef:
  kind: Role
  name: pod-reader
  apiGroup: rbac.authorization.k8s.io
---
apiVersion: batch/v1
kind: Job
metadata:
  name: metrics-test
spec:
  template:
    spec:
      serviceAccountName: pod-reader
      restartPolicy: OnFailure
      containers:
      - name: metrics-test
        image: alpine:3.19
        command: ['sh', '-c']
        env:
          - name: NAMESPACE
            valueFrom:
              fieldRef:
                fieldPath: metadata.namespace
        args:
          - |
            apk --no-cache add curl kubectl
            set -e
            POD_URL="http://$(kubectl -n $NAMESPACE get pods -l cnpg.io/podRole=instance -o jsonpath="{.items[0].status.podIP}"):9187/metrics"
            echo "POD_URL: $POD_URL"

            echo "pg_stat_subscription_received_lsn"
            curl $POD_URL | grep pg_stat_subscription_received_lsn
            echo "pg_stat_subscription_last_msg_send_time"
            curl $POD_URL | grep pg_stat_subscription_last_msg_send_time
            echo "pg_stat_subscription_last_msg_receipt_time"
            curl $POD_URL | grep pg_stat_subscription_last_msg_receipt_time
            echo "pg_stat_subscription_latest_end_lsn"
            curl $POD_URL | grep pg_stat_subscription_latest_end_lsn
            echo "pg_stat_subscription_latest_end_time"
            curl $POD_URL | grep pg_stat_subscription_latest_end_time
            echo "pg_stat_subscription_enabled"
            curl $POD_URL | grep pg_stat_subscription_enabled
            echo "pg_stat_subscription_apply_error_count"
            curl $POD_URL | grep pg_stat_subscription_apply_error_count
            echo "pg_stat_subscription_sync_error_count"
            curl $POD_URL | grep pg_stat_subscription_sync_error_count
            echo "pg_stat_subscription_stats_reset"
            curl $POD_URL | grep pg_stat_subscription_stats_reset
            echo "pg_stat_subscription_pid"
            curl $POD_URL | grep pg_stat_subscription_pid

            echo "paradedb_index_relation_size"
            curl $POD_URL | grep paradedb_index_relation_size
            echo "paradedb_index_segments_count"
            curl $POD_URL | grep paradedb_index_segments_count
            echo "paradedb_index_segments_min_size"
            curl $POD_URL | grep paradedb_index_segments_min_size
            echo "paradedb_index_segments_max_size"
            curl $POD_URL | grep paradedb_index_segments_max_size
            echo "paradedb_index_segments_avg_size"
            curl $POD_URL | grep paradedb_index_segments_avg_size

            echo "paradedb_index_layer_segments_bucket"
            curl $POD_URL | grep paradedb_index_layer_segments_bucket
            echo "paradedb_index_layer_segments_count"
            curl $POD_URL | grep paradedb_index_layer_segments_count
            echo "paradedb_index_layer_segments_sum"
            curl $POD_URL | grep paradedb_index_layer_segments_sum

```

## File: charts\paradedb\test\monitoring\chainsaw-test.yaml
```
##
# This is a test that checks if PodMonitors, ConfigMaps and PrometheusRules are correctly provisioned when requested.
apiVersion: chainsaw.kyverno.io/v1alpha1
kind: Test
metadata:
  name: monitoring
spec:
  timeouts:
    apply: 1s
    assert: 60s
    cleanup: 30s
  steps:
    - name: Install the monitoring cluster
      try:
        - script:
            content: |
              helm upgrade \
                --install \
                --namespace $NAMESPACE \
                --values ./01-monitoring_cluster.yaml \
                --wait \
                --debug \
                monitoring ../../
        - assert:
            file: ./01-monitoring_cluster-assert.yaml
        - apply:
            file: ./02-logical-replication.yaml
        - assert:
            file: ./02-logical-replication-assert.yaml
        - apply:
            file: ./02-paradedb.yaml
        - assert:
            file: ./02-paradedb-assert.yaml
        - apply:
            file: ./03-metrics-test.yaml
        - assert:
            file: ./03-metrics-test-assert.yaml
      catch:
        - describe:
            apiVersion: postgresql.cnpg.io/v1
            kind: Cluster
        - describe:
            apiVersion: batch/v1
            kind: Job
        - podLogs:
            selector: batch.kubernetes.io/job-name=logical-replication
        - podLogs:
            selector: batch.kubernetes.io/job-name=paradedb
        - podLogs:
            selector: batch.kubernetes.io/job-name=metrics-test
    - name: Cleanup
      try:
        - script:
            content: |
              helm uninstall --namespace $NAMESPACE monitoring

```

## File: charts\paradedb\test\paradedb-cluster-configuration\01-non_default_configuration_cluster-assert.yaml
```
apiVersion: postgresql.cnpg.io/v1
kind: Cluster
metadata:
  name: non-default-configuration-paradedb
  labels:
    foo: bar
  annotations:
      foo: bar
spec:
  imageName: ghcr.io/cloudnative-pg/crazycustomimage:99.99
  imagePullPolicy: Always
  postgresUID: 1001
  postgresGID: 1002
  instances: 2
  postgresql:
    ldap:
      server: 'openldap.default.svc.cluster.local'
      bindSearchAuth:
        baseDN: 'ou=org,dc=example,dc=com'
        bindDN: 'cn=admin,dc=example,dc=com'
        bindPassword:
          name: 'ldapBindPassword'
          key: 'data'
        searchAttribute: 'uid'
    parameters:
      max_connections: "42"
      cron.database_name: "postgres"
    pg_hba:
      - host all 1.2.3.4/32 trust
    pg_ident:
      - mymap   /^(.*)@mydomain\.com$      \1
    shared_preload_libraries:
      - pg_search
      - pg_cron
      - pg_stat_statements
      - pgaudit
    synchronous:
      method: any
      number: 1
  bootstrap:
    initdb:
      database: mydb
      owner: dante
      secret:
        name: mydb-secret
      postInitApplicationSQL:
        - CREATE EXTENSION IF NOT EXISTS pg_search;
        - CREATE EXTENSION IF NOT EXISTS pg_ivm;
        - CREATE EXTENSION IF NOT EXISTS vector;
        - CREATE EXTENSION IF NOT EXISTS postgis;
        - CREATE EXTENSION IF NOT EXISTS postgis_topology;
        - CREATE EXTENSION IF NOT EXISTS fuzzystrmatch;
        - CREATE EXTENSION IF NOT EXISTS postgis_tiger_geocoder;
        - CREATE EXTENSION IF NOT EXISTS pg_stat_statements;
        - ALTER DATABASE "mydb" SET search_path TO public,paradedb;
        - CREATE TABLE mytable (id serial PRIMARY KEY, name VARCHAR(255));
      postInitTemplateSQL:
        - CREATE EXTENSION IF NOT EXISTS pg_search;
        - CREATE EXTENSION IF NOT EXISTS pg_ivm;
        - CREATE EXTENSION IF NOT EXISTS vector;
        - CREATE EXTENSION IF NOT EXISTS postgis;
        - CREATE EXTENSION IF NOT EXISTS postgis_topology;
        - CREATE EXTENSION IF NOT EXISTS fuzzystrmatch;
        - CREATE EXTENSION IF NOT EXISTS postgis_tiger_geocoder;
        - CREATE EXTENSION IF NOT EXISTS pg_stat_statements;
        - ALTER DATABASE template1 SET search_path TO public,paradedb;
        - CREATE TABLE mytable (id serial PRIMARY KEY, name VARCHAR(255));
      postInitSQL:
        - CREATE EXTENSION IF NOT EXISTS pg_cron;
        - CREATE TABLE mytable (id serial PRIMARY KEY, name VARCHAR(255));
  superuserSecret:
    name: supersecret-secret
  enableSuperuserAccess: true
  enablePDB: false
  certificates:
    serverCASecret: ca-secret
    serverTLSSecret: tls-secret
    replicationTLSSecret: replication-tls-secret
    clientCASecret: client-ca-secret
  imagePullSecrets:
    - name: image-pull-secret
  storage:
    size: 256Mi
    storageClass: standard
  walStorage:
    size: 256Mi
    storageClass: standard
  affinity:
    topologyKey: kubernetes.io/hostname
    nodeAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
        nodeSelectorTerms:
        - matchExpressions:
          - key: kubernetes.io/hostname
            operator: In
            values:
            - node1
            - node2
  env:
    - name: MY_CUSTOM_FLAG
      value: enabled
    - name: MY_CUSTOM_ENV
      valueFrom:
        configMapKeyRef:
          name: my-custom-env
          key: env
          optional: true
    - name: MY_CUSTOM_SECRET_ENV
      valueFrom:
        secretKeyRef:
          name: my-custom-secret
          key: secret
          optional: true
  envFrom:
    - configMapRef:
        name: global-envs
        optional: true
    - secretRef:
        name: db-credentials
        optional: true
  resources:
    requests:
      cpu: 100m
      memory: 256Mi
    limits:
      cpu: 100m
      memory: 256Mi
  priorityClassName: mega-high
  primaryUpdateStrategy: supervised
  primaryUpdateMethod: restart
  logLevel: warning
  managed:
    roles:
      - name: dante
        ensure: present
        comment: Dante Alighieri
        login: true
        inherit: true
        inRoles:
          - pg_monitor
          - pg_signal_backend
        connectionLimit: -1
    services:
      additional:
        - selectorType: rw
          serviceTemplate:
            metadata:
              name: "test-lb"
              labels:
                test-label: "true"
              annotations:
                test-annotation: "true"
            spec:
              type: LoadBalancer
          updateStrategy: patch
  serviceAccountTemplate:
    metadata:
      annotations:
        my-annotation: my-service-account
  podSecurityContext:
    runAsUser: 26
    runAsGroup: 26
    fsGroup: 26
    supplementalGroups: [2000, 3000]
    fsGroupChangePolicy: "OnRootMismatch"
  securityContext:
    allowPrivilegeEscalation: false
    capabilities:
      drop:
        - ALL
      add:
        - NET_BIND_SERVICE
    readOnlyRootFilesystem: true
    runAsNonRoot: true

```

## File: charts\paradedb\test\paradedb-cluster-configuration\01-non_default_configuration_cluster.yaml
```
type: paradedb
mode: standalone
cluster:
  instances: 2
  imageName: ghcr.io/cloudnative-pg/crazycustomimage:99.99
  imagePullPolicy: Always
  imagePullSecrets:
   - name: "image-pull-secret"
  storage:
    size: 256Mi
    storageClass: standard
  walStorage:
    enabled: true
    size: 256Mi
    storageClass: standard
  postgresUID: 1001
  postgresGID: 1002
  resources:
    requests:
      cpu: 100m
      memory: 256Mi
    limits:
      cpu: 100m
      memory: 256Mi
  priorityClassName: mega-high
  primaryUpdateMethod: restart
  primaryUpdateStrategy: supervised
  logLevel: warning
  affinity:
    topologyKey: kubernetes.io/hostname
    nodeAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
        nodeSelectorTerms:
        - matchExpressions:
          - key: kubernetes.io/hostname
            operator: In
            values:
            - node1
            - node2
  env:
    - name: MY_CUSTOM_FLAG
      value: enabled
    - name: MY_CUSTOM_ENV
      valueFrom:
        configMapKeyRef:
          name: my-custom-env
          key: env
          optional: true
    - name: MY_CUSTOM_SECRET_ENV
      valueFrom:
        secretKeyRef:
          name: my-custom-secret
          key: secret
          optional: true
  envFrom:
    - configMapRef:
        name: global-envs
        optional: true
    - secretRef:
        name: db-credentials
        optional: true
  certificates:
    serverCASecret: ca-secret
    serverTLSSecret: tls-secret
    replicationTLSSecret: replication-tls-secret
    clientCASecret: client-ca-secret
  enableSuperuserAccess: true
  superuserSecret: supersecret-secret
  enablePDB: false
  services:
    additional:
      - selectorType: rw
        serviceTemplate:
          metadata:
            name: "test-lb"
            labels:
              test-label: "true"
            annotations:
              test-annotation: "true"
          spec:
            type: LoadBalancer
        updateStrategy: patch
  roles:
     - name: dante
       ensure: present
       comment: Dante Alighieri
       login: true
       inRoles:
         - pg_monitor
         - pg_signal_backend
  postgresql:
    ldap:
      server: 'openldap.default.svc.cluster.local'
      bindSearchAuth:
        baseDN: 'ou=org,dc=example,dc=com'
        bindDN: 'cn=admin,dc=example,dc=com'
        bindPassword:
          name: 'ldapBindPassword'
          key: 'data'
        searchAttribute: 'uid'
    parameters:
      max_connections: "42"
      cron.database_name: "postgres"
    pg_hba:
      - host all 1.2.3.4/32 trust
    pg_ident:
      - mymap   /^(.*)@mydomain\.com$      \1
    shared_preload_libraries:
      - pgaudit
    synchronous:
      method: any
      number: 1
  initdb:
    database: mydb
    owner: dante
    secret:
      name: mydb-secret
    postInitApplicationSQL:
      - CREATE TABLE mytable (id serial PRIMARY KEY, name VARCHAR(255));
    postInitTemplateSQL:
      - CREATE TABLE mytable (id serial PRIMARY KEY, name VARCHAR(255));
    postInitSQL:
      - CREATE TABLE mytable (id serial PRIMARY KEY, name VARCHAR(255));
  additionalLabels:
    foo: bar
  annotations:
    foo: bar
  serviceAccountTemplate:
    metadata:
      annotations:
        my-annotation: my-service-account
  podSecurityContext:
    runAsUser: 26
    runAsGroup: 26
    fsGroup: 26
    supplementalGroups: [2000, 3000]
    fsGroupChangePolicy: "OnRootMismatch"
  securityContext:
    allowPrivilegeEscalation: false
    capabilities:
      drop:
        - ALL
      add:
        - NET_BIND_SERVICE
    readOnlyRootFilesystem: true
    runAsNonRoot: true

backups:
  enabled: false

```

## File: charts\paradedb\test\paradedb-cluster-configuration\02-recovery_object_store_database_owner-assert.yaml
```
apiVersion: postgresql.cnpg.io/v1
kind: Cluster
metadata:
  name: recovery-object-store-database-owner-paradedb
spec:
  bootstrap:
    recovery:
      source: objectStoreRecoveryCluster
      database: my-special-database
      owner: me

```

## File: charts\paradedb\test\paradedb-cluster-configuration\02-recovery_object_store_database_owner.yaml
```
type: paradedb
mode: recovery

recovery:
  method: object_store
  database: my-special-database
  owner: me
  s3:
    bucket: "mybucket"
    accessKey: "minio"
    secretKey: "minio123"
    region: "local"

backups:
  enabled: false

```

## File: charts\paradedb\test\paradedb-cluster-configuration\03-recovery_backup_database_owner-assert.yaml
```
apiVersion: postgresql.cnpg.io/v1
kind: Cluster
metadata:
  name: recovery-backup-database-owner-paradedb
spec:
  bootstrap:
    recovery:
      backup:
        name: post-init-backup
      database: my-special-database
      owner: me

```

## File: charts\paradedb\test\paradedb-cluster-configuration\03-recovery_backup_database_owner.yaml
```
type: paradedb
mode: recovery

recovery:
  method: backup
  backupName: "post-init-backup"
  database: my-special-database
  owner: me
  s3:
    bucket: "mybucket"
    accessKey: "minio"
    secretKey: "minio123"
    region: "local"

backups:
  enabled: false

```

## File: charts\paradedb\test\paradedb-cluster-configuration\04-replica_origin_azure_creds-assert.yaml
```
apiVersion: v1
kind: Secret
metadata:
  name: replica-origin-azure-creds-paradedb-origin-azure-creds
data:
  AZURE_CONNECTION_STRING: "bXljb25uc3RyaW5n"
  AZURE_STORAGE_ACCOUNT: "bXlhY2NvdW50"
  AZURE_STORAGE_KEY: "bXlzdG9yYWdla2V5"
  AZURE_STORAGE_SAS_TOKEN: "bXlzYXN0b2tlbg=="

```

## File: charts\paradedb\test\paradedb-cluster-configuration\04-replica_origin_azure_creds.yaml
```
type: paradedb
mode: replica

cluster:
  instances: 1
  storage:
    size: 256Mi

replica:
  self: "replica-cluster"
  primary: "source-cluster"
  bootstrap:
    source: object_store
  origin:
    objectStore:
      clusterName: source-paradedb
      provider: azure
      destinationPath: "https://myaccount.blob.core.windows.net/mycontainer"
      azure:
        connectionString: "myconnstring"
        storageAccount: "myaccount"
        storageKey: "mystoragekey"
        storageSasToken: "mysastoken"
        containerName: "mycontainer"

backups:
  enabled: false

```

## File: charts\paradedb\test\paradedb-cluster-configuration\chainsaw-test.yaml
```
##
# This is a test that verifies that non-default configuration options are correctly propagated to the ParadeDB CNPG cluster.
# P.S. This test is not designed to have a good running configuration, it is designed to test the configuration propagation!
apiVersion: chainsaw.kyverno.io/v1alpha1
kind: Test
metadata:
  name: postgresql-cluster-configuration
spec:
  timeouts:
    apply: 1s
    assert: 5s
    cleanup: 30s
  steps:
    - name: Install the non-default configuration cluster
      try:
        - script:
            content: |
              helm upgrade \
                --install \
                --namespace $NAMESPACE \
                --values ./01-non_default_configuration_cluster.yaml \
                --wait \
                non-default-configuration ../../
        - assert:
            file: ./01-non_default_configuration_cluster-assert.yaml
    - name: Install object-store recovery-cluster for specific database and owner
      try:
        - script:
            content: |
              helm upgrade \
                --install \
                --namespace $NAMESPACE \
                --values ./02-recovery_object_store_database_owner.yaml \
                --wait \
                recovery-object-store-database-owner ../../
        - assert:
            file: ./02-recovery_object_store_database_owner-assert.yaml
    - name: Install backup recovery-cluster for specific database and owner
      try:
        - script:
            content: |
              helm upgrade \
                --install \
                --namespace $NAMESPACE \
                --values ./03-recovery_backup_database_owner.yaml \
                --wait \
                recovery-backup-database-owner ../../
        - assert:
            file: ./03-recovery_backup_database_owner-assert.yaml
    - name: Verify replica origin Azure credentials are rendered correctly
      try:
        - script:
            content: |
              helm template \
                --namespace $NAMESPACE \
                --values ./04-replica_origin_azure_creds.yaml \
                --show-only templates/origin-azure-creds.yaml \
                replica-origin-azure-creds ../../ \
                | kubectl apply --namespace $NAMESPACE -f -
        - assert:
            file: ./04-replica_origin_azure_creds-assert.yaml
    - name: Cleanup
      try:
        - script:
            content: |
              helm uninstall --namespace $NAMESPACE non-default-configuration
              helm uninstall --namespace $NAMESPACE recovery-object-store-database-owner
              helm uninstall --namespace $NAMESPACE recovery-backup-database-owner

```

## File: charts\paradedb\test\paradedb-enterprise\01-paradedb-NCC-1701-D_cluster-assert.yaml
```
apiVersion: postgresql.cnpg.io/v1
kind: Cluster
metadata:
  name: paradedb-ncc-1701-d
spec:
  postgresql:
    parameters:
      cron.database_name: postgres
      hot_standby_feedback: "1"
status:
  readyInstances: 2

```

## File: charts\paradedb\test\paradedb-enterprise\01-paradedb-NCC-1701-D_cluster.yaml
```
type: paradedb-enterprise
mode: standalone
version:
  major: "18"
  paradedb: "0.22.3"
cluster:
  instances: 2
  storage:
    size: 256Mi
  imagePullSecrets:
    - name: paradedb-enterprise-registry-cred
  postgresql:
    parameters:
      cron.database_name: postgres
      hot_standby_feedback: "1"

backups:
  enabled: false

```

## File: charts\paradedb\test\paradedb-enterprise\02-paradedb_test-assert.yaml
```
apiVersion: batch/v1
kind: Job
metadata:
  name: paradedb-enterprise-test
status:
  succeeded: 1

```

## File: charts\paradedb\test\paradedb-enterprise\02-paradedb_test.yaml
```
apiVersion: batch/v1
kind: Job
metadata:
  name: paradedb-enterprise-test
spec:
  template:
    spec:
      restartPolicy: OnFailure
      containers:
      - name: data-test
        env:
          - name: DB_URI
            valueFrom:
              secretKeyRef:
                name: paradedb-ncc-1701-d-app
                key: uri
        image: alpine:3.19
        command: ['sh', '-c']
        args:
          - |
            apk --no-cache add postgresql-client
            psql "$DB_URI" <<-EOSQL
              CALL paradedb.create_bm25_test_table(
                schema_name => 'public',
                table_name => 'mock_items_paradedb_enterprise'
              );
              CREATE INDEX search_idx_paradedb_enterprise ON mock_items_paradedb_enterprise
              USING bm25 (id, description, category, rating, in_stock, created_at, metadata, weight_range)
              WITH (key_field='id');
            EOSQL
            RESULT=$(psql "$DB_URI" -t) <<-EOSQL
              SELECT description
              FROM mock_items_paradedb_enterprise
              WHERE description @@@ '"bluetooth speaker"~1'
              LIMIT 1;
            EOSQL
            echo -$RESULT-
            if [ "$RESULT" = " Bluetooth-enabled speaker" ]; then
              echo "Test for description search passed."
            else
              echo "Test for description search failed."
              exit 1
            fi

```

## File: charts\paradedb\test\paradedb-enterprise\03-paradedb_replication_test-assert.yaml
```
apiVersion: batch/v1
kind: Job
metadata:
  name: paradedb-enterprise-index-test
status:
  succeeded: 1

```

## File: charts\paradedb\test\paradedb-enterprise\03-paradedb_replication_test.yaml
```
apiVersion: batch/v1
kind: Job
metadata:
  name: paradedb-enterprise-index-test
spec:
  template:
    spec:
      restartPolicy: OnFailure
      containers:
      - name: data-test
        env:
          - name: DB_URI
            valueFrom:
              secretKeyRef:
                name: paradedb-ncc-1701-d-app
                key: uri
        image: alpine:3.19
        command: ['sh', '-c']
        args:
          - |
            apk --no-cache add postgresql-client
            DB_URI="${DB_URI/paradedb-ncc-1701-d-rw/paradedb-ncc-1701-d-ro}"
            RESULT=$(psql "$DB_URI" -t) <<-EOSQL
              SELECT description
              FROM mock_items_paradedb_enterprise
              WHERE description @@@ '"bluetooth speaker"~1'
              LIMIT 1;
            EOSQL
            echo -$RESULT-
            if [ "$RESULT" = " Bluetooth-enabled speaker" ]; then
              echo "Test for description search on replicas passed."
            else
              echo "Test for description search on replicas failed."
              exit 1
            fi

            SIZE_RESULT=$(psql "$DB_URI" -t) <<-EOSQL
              SELECT pg_size_pretty(pg_relation_size('search_idx_paradedb_enterprise'));
            EOSQL
            echo -$SIZE_RESULT-
            if [ "$SIZE_RESULT" != " 0 bytes" ]; then
              echo "Test for index size on replicas passed."
            else
              echo "Test for index size on replicas failed."
              exit 1
            fi

```

## File: charts\paradedb\test\paradedb-enterprise\chainsaw-test.yaml
```
##
# This test sets up a ParadeDB Enterprise Cluster and ensures that ParadeDB extensions are available.
apiVersion: chainsaw.kyverno.io/v1alpha1
kind: Test
metadata:
  name: paradedb-enterprise
spec:
  timeouts:
    apply: 1s
    assert: 2m
    cleanup: 1m
  steps:
    - name: Install a standalone ParadeDB Enterprise CNPG Cluster
      try:
        - script:
            content: |
              kubectl -n $NAMESPACE create secret docker-registry paradedb-enterprise-registry-cred --docker-server="https://index.docker.io/v1/" --docker-username="$PARADEDB_ENTERPRISE_DOCKER_USERNAME" --docker-password="$PARADEDB_ENTERPRISE_DOCKER_PAT"
              helm upgrade \
                --install \
                --namespace $NAMESPACE \
                --values ./01-paradedb-NCC-1701-D_cluster.yaml \
                --wait \
                paradedb-ncc-1701-d ../../
        - assert:
            file: ./01-paradedb-NCC-1701-D_cluster-assert.yaml
      catch:
        - describe:
            apiVersion: v1
            kind: Pod
        - describe:
            apiVersion: batch/v1
            kind: Job
        - podLogs:
            selector: cnpg.io/cluster=paradedb-ncc-1701-d
    - name: Verify ParadeDB Enterprise extensions are installed
      timeouts:
        apply: 1s
        assert: 30s
      try:
        - apply:
            file: 02-paradedb_test.yaml
        - assert:
            file: 02-paradedb_test-assert.yaml
      catch:
        - describe:
            apiVersion: v1
            kind: Pod
        - describe:
            apiVersion: batch/v1
            kind: Job
        - podLogs:
            selector: cnpg.io/cluster=paradedb-ncc-1701-d
        - podLogs:
            selector: batch.kubernetes.io/job-name=paradedb-enterprise-test
    - name: Verify index replication
      timeouts:
        apply: 1s
        assert: 30s
      try:
        - apply:
            file: 03-paradedb_replication_test.yaml
        - assert:
            file: 03-paradedb_replication_test-assert.yaml
      catch:
        - describe:
            apiVersion: batch/v1
            kind: Job
        - podLogs:
            selector: cnpg.io/cluster=paradedb-ncc-1701-d
        - podLogs:
            selector: batch.kubernetes.io/job-name=paradedb-enterprise-index-test
    - name: Cleanup
      try:
        - script:
            content: |
              helm uninstall --namespace $NAMESPACE paradedb-ncc-1701-d
      catch:
        - describe:
            apiVersion: v1
            kind: Pod
        - podLogs:
            selector: cnpg.io/cluster=paradedb-ncc-1701-d

```

## File: charts\paradedb\test\paradedb-import\00-source-cluster-assert.yaml
```
apiVersion: postgresql.cnpg.io/v1
kind: Cluster
metadata:
  name: source-paradedb
status:
  readyInstances: 1

```

## File: charts\paradedb\test\paradedb-import\00-source-cluster.yaml
```
type: paradedb
mode: standalone
cluster:
  instances: 1
  superuserSecret: source-paradedb-superuser
  storage:
    size: 256Mi
backups:
  enabled: false

```

## File: charts\paradedb\test\paradedb-import\00-source-superuser-password.yaml
```
apiVersion: v1
kind: Secret
metadata:
  name: source-paradedb-superuser
type: Opaque
data:
  username: "cG9zdGdyZXM="
  password: "cG9zdGdyZXM="

```

## File: charts\paradedb\test\paradedb-import\01-data_write-assert.yaml
```
apiVersion: batch/v1
kind: Job
metadata:
  name: data-write
status:
  succeeded: 1

```

## File: charts\paradedb\test\paradedb-import\01-data_write.yaml
```
apiVersion: batch/v1
kind: Job
metadata:
  name: data-write
spec:
  template:
    spec:
      restartPolicy: OnFailure
      containers:
      - name: data-write
        env:
          - name: DB_USER
            valueFrom:
              secretKeyRef:
                name: source-paradedb-superuser
                key: username
          - name: DB_PASS
            valueFrom:
              secretKeyRef:
                name: source-paradedb-superuser
                key: password
          - name: DB_URI
            value: postgres://$(DB_USER):$(DB_PASS)@source-paradedb-rw:5432
        image: alpine:3.19
        command: ['sh', '-c']
        args:
         - |
           set -e
           apk --no-cache add postgresql-client
           psql "$DB_URI" -c "CREATE DATABASE mygooddb;"
           psql "$DB_URI/mygooddb" -c "CREATE TABLE mygoodtable (id serial PRIMARY KEY);"
           psql "$DB_URI/mygooddb" -c "INSERT INTO mygoodtable VALUES (314159265);"
           psql "$DB_URI/mygooddb" -c "CREATE TABLE mybadtable (id serial PRIMARY KEY);"

```

## File: charts\paradedb\test\paradedb-import\02-import-cluster-assert.yaml
```
apiVersion: postgresql.cnpg.io/v1
kind: Cluster
metadata:
  name: import-paradedb
status:
  readyInstances: 1

```

## File: charts\paradedb\test\paradedb-import\02-import-cluster.yaml
```
type: paradedb
mode: "recovery"
recovery:
  method: "import"
  import:
    type: "microservice"
    databases: [ "mygooddb" ]
    pgDumpExtraOptions:
      - --table=mygood*
    source:
      host: "source-paradedb-rw"
      username: "postgres"
      passwordSecret:
        name: source-paradedb-superuser
        key: password
      sslMode: "require"
      sslKeySecret:
        name: source-paradedb-replication
        key: tls.key
      sslCertSecret:
        name: source-paradedb-replication
        key: tls.crt

cluster:
  instances: 1
  storage:
    size: 256Mi
  initdb:
    database: mygooddb

backups:
  enabled: false

```

## File: charts\paradedb\test\paradedb-import\03-data_test-assert.yaml
```
apiVersion: batch/v1
kind: Job
metadata:
  name: data-test
status:
  succeeded: 1

```

## File: charts\paradedb\test\paradedb-import\03-data_test.yaml
```
apiVersion: batch/v1
kind: Job
metadata:
  name: data-test
spec:
  template:
    spec:
      restartPolicy: OnFailure
      containers:
      - name: data-test
        env:
          - name: DB_URI
            valueFrom:
              secretKeyRef:
                name: import-paradedb-superuser
                key: uri
        image: alpine:3.19
        command: ['sh', '-c']
        args:
         - |
           set -e
           apk --no-cache add postgresql-client
           DB_URI=$(echo $DB_URI | sed "s|/\*|/|" )
           test "$(psql "${DB_URI}mygooddb" -t -c 'SELECT EXISTS (SELECT FROM information_schema.tables WHERE table_name = $$mygoodtable$$)' --csv -q 2>/dev/null)" = "t"
           echo "mygoodtable exist"
           test "$(psql "${DB_URI}mygooddb" -t -c 'SELECT EXISTS (SELECT FROM information_schema.tables WHERE table_name = $$mybadtable$$)' --csv -q 2>/dev/null)" = "f"
           echo "mybadtable doesn't exist"
           test "$(psql "${DB_URI}mygooddb" -t -c 'SELECT EXISTS (SELECT FROM mygoodtable WHERE id = 314159265)' --csv -q 2>/dev/null)" = "t"
           echo "mygoodtable contains the desired value"

```

## File: charts\paradedb\test\paradedb-import\04-import-cluster-schema_only-assert.yaml
```
apiVersion: postgresql.cnpg.io/v1
kind: Cluster
metadata:
  name: import-schemaonly-paradedb
status:
  readyInstances: 1

```

## File: charts\paradedb\test\paradedb-import\04-import-cluster-schema_only.yaml
```
type: paradedb
mode: "recovery"
recovery:
  method: "import"
  import:
    type: "microservice"
    databases: [ "mygooddb" ]
    pgRestoreExtraOptions:
      - --table=mygoodtable
    schemaOnly: true
    source:
      host: "source-paradedb-rw"
      username: "postgres"
      passwordSecret:
        name: source-paradedb-superuser
        key: password
      sslMode: "require"
      sslKeySecret:
        name: source-paradedb-replication
        key: tls.key
      sslCertSecret:
        name: source-paradedb-replication
        key: tls.crt

cluster:
  instances: 1
  storage:
    size: 256Mi
  initdb:
    database: mygooddb

backups:
  enabled: false

```

## File: charts\paradedb\test\paradedb-import\05-data_test-assert.yaml
```
apiVersion: batch/v1
kind: Job
metadata:
  name: data-test-schemaonly
status:
  succeeded: 1

```

## File: charts\paradedb\test\paradedb-import\05-data_test.yaml
```
apiVersion: batch/v1
kind: Job
metadata:
  name: data-test-schemaonly
spec:
  template:
    spec:
      restartPolicy: OnFailure
      containers:
      - name: data-test
        env:
          - name: DB_URI
            valueFrom:
              secretKeyRef:
                name: import-schemaonly-paradedb-superuser
                key: uri
        image: alpine:3.19
        command: ['sh', '-c']
        args:
         - |
           set -e
           apk --no-cache add postgresql-client
           DB_URI=$(echo $DB_URI | sed "s|/\*|/|" )
           test "$(psql "${DB_URI}mygooddb" -t -c 'SELECT EXISTS (SELECT FROM information_schema.tables WHERE table_name = $$mygoodtable$$)' --csv -q 2>/dev/null)" = "t"
           echo "mygoodtable exist"
           test "$(psql "${DB_URI}mygooddb" -t -c 'SELECT EXISTS (SELECT FROM information_schema.tables WHERE table_name = $$mybadtable$$)' --csv -q 2>/dev/null)" = "f"
           echo "mybadtable doesn't exist"
           test "$(psql "${DB_URI}mygooddb" -t -c 'SELECT COUNT(*) FROM mygoodtable' --csv -q 2>/dev/null)" = "0"
           echo "mygoodtable is empty"
           test "$(psql "${DB_URI}mygooddb" -t -c 'SELECT EXISTS (SELECT FROM pg_extension WHERE extname = $$pg_search$$)' --csv -q 2>/dev/null)" = "t"
           echo "pg_search extension is installed"

```

## File: charts\paradedb\test\paradedb-import\chainsaw-test.yaml
```
##
# This is a test that provisions a regular (non CNPG) PostgreSQL cluster and attempts to perform a
# pg_basebackup recovery into a ParadeDB cluster.
apiVersion: chainsaw.kyverno.io/v1alpha1
kind: Test
metadata:
  name: paradedb-import
spec:
  timeouts:
    apply: 1s
    assert: 2m
    cleanup: 1m
  steps:
    - name: Install the external PostgreSQL cluster
      try:
        - apply:
            file: ./00-source-superuser-password.yaml
        - script:
            content: |
              helm upgrade \
                --install \
                --namespace $NAMESPACE \
                --values ./00-source-cluster.yaml \
                --wait \
                source ../../
        - assert:
            file: ./00-source-cluster-assert.yaml
        - apply:
            file: ./01-data_write.yaml
        - assert:
            file: ./01-data_write-assert.yaml
    - name: Install the import cluster
      timeouts:
        assert: 5m
      try:
        - script:
            content: |
              helm upgrade \
                --install \
                --namespace $NAMESPACE \
                --values ./02-import-cluster.yaml \
                --wait \
                import ../../
        - assert:
            file: ./02-import-cluster-assert.yaml
      catch:
        - describe:
            apiVersion: postgresql.cnpg.io/v1
            kind: Cluster
    - name: Verify the data exists
      try:
        - apply:
            file: ./03-data_test.yaml
        - assert:
            file: ./03-data_test-assert.yaml
      catch:
        - describe:
            apiVersion: batch/v1
            kind: Job
        - podLogs:
            selector: batch.kubernetes.io/job-name=data-test
    - name: Install the schema-only import cluster
      timeouts:
        assert: 5m
      try:
        - script:
            content: |
              helm upgrade \
                --install \
                --namespace $NAMESPACE \
                --values ./04-import-cluster-schema_only.yaml \
                --wait \
                import-schemaonly ../../
        - assert:
            file: ./04-import-cluster-schema_only-assert.yaml
      catch:
        - describe:
            apiVersion: postgresql.cnpg.io/v1
            kind: Cluster
    - name: Verify only the schema exists
      try:
        - apply:
            file: ./05-data_test.yaml
        - assert:
            file: ./05-data_test-assert.yaml
      catch:
        - describe:
            apiVersion: batch/v1
            kind: Job
        - podLogs:
            selector: batch.kubernetes.io/job-name=data-test-schemaonly
    - name: Cleanup
      try:
        - script:
            content: |
              helm uninstall --namespace $NAMESPACE source
              helm uninstall --namespace $NAMESPACE import
              helm uninstall --namespace $NAMESPACE import-schemaonly

```

## File: charts\paradedb\test\paradedb-minio-backup-restore\00-minio_cleanup-assert.yaml
```
apiVersion: batch/v1
kind: Job
metadata:
  name: minio-cleanup
status:
  succeeded: 1

```

## File: charts\paradedb\test\paradedb-minio-backup-restore\00-minio_cleanup.yaml
```
apiVersion: batch/v1
kind: Job
metadata:
  name: minio-cleanup
spec:
  template:
    spec:
      restartPolicy: OnFailure
      containers:
      - name: minio-cleanup
        image: minio/mc
        command: ['sh', '-c']
        args:
         - |
           mc alias set myminio https://minio.minio.svc.cluster.local minio minio123
           mc rm --recursive --force myminio/mybucket/paradedb

```

## File: charts\paradedb\test\paradedb-minio-backup-restore\01-paradedb_cluster-assert.yaml
```
apiVersion: postgresql.cnpg.io/v1
kind: Cluster
metadata:
  name: paradedb
status:
  readyInstances: 2

```

## File: charts\paradedb\test\paradedb-minio-backup-restore\01-paradedb_cluster.yaml
```
type: paradedb
mode: standalone
version:
  major: "18"
  paradedb: "0.22.3"
cluster:
  instances: 2
  storage:
    size: 256Mi

backups:
  enabled: true
  provider: s3
  endpointURL: "https://minio.minio.svc.cluster.local"
  endpointCA:
    name: kube-root-ca.crt
    key: ca.crt
  wal:
    encryption: ""
  data:
    encryption: ""
  s3:
    bucket: "mybucket"
    path: "/paradedb/v1"
    accessKey: "minio"
    secretKey: "minio123"
    region: "local"
  scheduledBackups: []
  retentionPolicy: "30d"

```

## File: charts\paradedb\test\paradedb-minio-backup-restore\02-paradedb_write-assert.yaml
```
apiVersion: batch/v1
kind: Job
metadata:
  name: paradedb-write
status:
  succeeded: 1

```

## File: charts\paradedb\test\paradedb-minio-backup-restore\02-paradedb_write.yaml
```
apiVersion: batch/v1
kind: Job
metadata:
  name: paradedb-write
spec:
  template:
    spec:
      restartPolicy: OnFailure
      containers:
      - name: data-write
        env:
          - name: DB_URI
            valueFrom:
              secretKeyRef:
                name: paradedb-app
                key: uri
        image: alpine:3.19
        command: ['sh', '-c']
        args:
          - |
            apk --no-cache add postgresql-client
            psql "$DB_URI" <<-EOSQL
              CALL paradedb.create_bm25_test_table(
                schema_name => 'public',
                table_name => 'mock_items_paradedb_minio_backup_restore'
              );
              CREATE INDEX search_idx_paradedb_minio_backup_restore ON mock_items_paradedb_minio_backup_restore
              USING bm25 (id, description, category, rating, in_stock, created_at, metadata, weight_range)
              WITH (key_field='id');
            EOSQL

```

## File: charts\paradedb\test\paradedb-minio-backup-restore\03-paradedb_test-assert.yaml
```
apiVersion: batch/v1
kind: Job
metadata:
  name: paradedb-test
status:
  succeeded: 1

```

## File: charts\paradedb\test\paradedb-minio-backup-restore\03-paradedb_test.yaml
```
apiVersion: batch/v1
kind: Job
metadata:
  name: paradedb-test
spec:
  template:
    spec:
      restartPolicy: OnFailure
      containers:
      - name: data-test
        env:
          - name: DB_URI
            valueFrom:
              secretKeyRef:
                name: paradedb-app
                key: uri
        image: alpine:3.19
        command: ['sh', '-c']
        args:
          - |
            apk --no-cache add postgresql-client
            RESULT=$(psql "$DB_URI" -t) <<-EOSQL
              SELECT description
              FROM mock_items_paradedb_minio_backup_restore
              WHERE description @@@ '"bluetooth speaker"~1'
              LIMIT 1;
            EOSQL
            echo -$RESULT-
            test "$RESULT" = " Bluetooth-enabled speaker"

```

## File: charts\paradedb\test\paradedb-minio-backup-restore\04-data_write-assert.yaml
```
apiVersion: batch/v1
kind: Job
metadata:
  name: data-write
status:
  succeeded: 1

```

## File: charts\paradedb\test\paradedb-minio-backup-restore\04-data_write.yaml
```
apiVersion: v1
kind: ServiceAccount
metadata:
  name: configmap-creator-sa
---
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: configmap-creator
rules:
- apiGroups: [""]
  resources: ["configmaps"]
  verbs: ["create"]
---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: configmap-creator-binding
subjects:
- kind: ServiceAccount
  name: configmap-creator-sa
roleRef:
  kind: Role
  name: configmap-creator
  apiGroup: rbac.authorization.k8s.io
---
apiVersion: batch/v1
kind: Job
metadata:
  name: data-write
spec:
  template:
    spec:
      serviceAccountName: configmap-creator-sa
      restartPolicy: OnFailure
      containers:
      - name: data-write
        env:
          - name: DB_URI
            valueFrom:
              secretKeyRef:
                name: paradedb-superuser
                key: uri
        image: alpine:3.19
        command: ['sh', '-c']
        args:
         - |
           apk --no-cache add postgresql-client kubectl coreutils
           DB_URI=$(echo $DB_URI | sed "s|/\*|/|" )
           psql "$DB_URI" -c "CREATE TABLE mygoodtable (id serial PRIMARY KEY);"
           sleep 5
           DATE_NO_BAD_TABLE=$(date --rfc-3339=ns)
           kubectl create configmap date-no-bad-table --from-literal=date="$DATE_NO_BAD_TABLE"
           sleep 5

```

## File: charts\paradedb\test\paradedb-minio-backup-restore\05-backup.yaml
```
apiVersion: postgresql.cnpg.io/v1
kind: Backup
metadata:
  name: post-init-backup
spec:
  method: barmanObjectStore
  cluster:
    name: paradedb

```

## File: charts\paradedb\test\paradedb-minio-backup-restore\05-backup_completed-assert.yaml
```
apiVersion: postgresql.cnpg.io/v1
kind: Backup
metadata:
  name: post-init-backup
spec:
  cluster:
    name: paradedb
  method: barmanObjectStore
status:
  phase: completed

```

## File: charts\paradedb\test\paradedb-minio-backup-restore\05-backup_running-assert.yaml
```
apiVersion: postgresql.cnpg.io/v1
kind: Backup
metadata:
  name: post-init-backup
spec:
  cluster:
    name: paradedb
  method: barmanObjectStore
status:
  phase: running

```

## File: charts\paradedb\test\paradedb-minio-backup-restore\05-checkpoint.yaml
```
apiVersion: batch/v1
kind: Job
metadata:
  name: backup-checkpoint
spec:
  template:
    spec:
      restartPolicy: OnFailure
      containers:
      - name: create-checkpoint
        env:
          - name: DB_URI
            valueFrom:
              secretKeyRef:
                name: paradedb-superuser
                key: uri
        image: alpine:3.19
        command: ['sh', '-c']
        args:
         - |
           apk --no-cache add postgresql-client
           DB_URI=$(echo $DB_URI | sed "s|/\*|/|" )
           END_TIME=$(( $(date +%s) + 30 ))
           while [ $(date +%s) -lt $END_TIME ]; do
             psql "$DB_URI" -c "SELECT pg_switch_wal();CHECKPOINT;"
             sleep 5
           done

```

## File: charts\paradedb\test\paradedb-minio-backup-restore\06-post_backup_data_write-assert.yaml
```
apiVersion: batch/v1
kind: Job
metadata:
  name: data-write-post-backup
status:
  succeeded: 1

```

## File: charts\paradedb\test\paradedb-minio-backup-restore\06-post_backup_data_write.yaml
```
apiVersion: batch/v1
kind: Job
metadata:
  name: data-write-post-backup
spec:
  template:
    spec:
      restartPolicy: OnFailure
      containers:
      - name: data-write
        env:
          - name: DB_URI
            valueFrom:
              secretKeyRef:
                name: paradedb-superuser
                key: uri
          - name: NAMESPACE
            valueFrom:
              fieldRef:
                fieldPath: metadata.namespace
        image: alpine:3.19
        command: ['sh', '-c']
        args:
         - |
           apk --no-cache add postgresql-client
           DB_URI=$(echo $DB_URI | sed "s|/\*|/|" )
           psql "$DB_URI" -c "CREATE TABLE mybadtable (id serial PRIMARY KEY);"

```

## File: charts\paradedb\test\paradedb-minio-backup-restore\07-recovery_backup_pitr_cluster-assert.yaml
```
apiVersion: postgresql.cnpg.io/v1
kind: Cluster
metadata:
  name: recovery-backup-pitr-paradedb
status:
  readyInstances: 2

```

## File: charts\paradedb\test\paradedb-minio-backup-restore\07-recovery_backup_pitr_cluster.yaml
```
type: paradedb
mode: recovery
cluster:
  instances: 2
  storage:
    size: 256Mi

recovery:
  method: backup
  backupName: "post-init-backup"
  provider: s3
  endpointURL: "https://minio.minio.svc.cluster.local"
  endpointCA:
    name: kube-root-ca.crt
    key: ca.crt
  wal:
    encryption: ""
  data:
    encryption: ""
  s3:
    bucket: "mybucket"
    path: "/paradedb/v1"
    accessKey: "minio"
    secretKey: "minio123"
    region: "local"
  scheduledBackups: []
  retentionPolicy: "30d"

backups:
  enabled: true
  provider: s3
  endpointURL: "https://minio.minio.svc.cluster.local"
  endpointCA:
    name: kube-root-ca.crt
    key: ca.crt
  wal:
    encryption: ""
  data:
    encryption: ""
  s3:
    bucket: "mybucket"
    path: "/paradedb/v2"
    accessKey: "minio"
    secretKey: "minio123"
    region: "local"
  scheduledBackups: []
  retentionPolicy: "30d"

```

## File: charts\paradedb\test\paradedb-minio-backup-restore\08-data_test-assert.yaml
```
apiVersion: batch/v1
kind: Job
metadata:
  name: data-test-backup-pitr
status:
  succeeded: 1

```

## File: charts\paradedb\test\paradedb-minio-backup-restore\08-data_test.yaml
```
apiVersion: batch/v1
kind: Job
metadata:
  name: data-test-backup-pitr
spec:
  template:
    spec:
      restartPolicy: OnFailure
      containers:
      - name: data-test
        env:
          - name: DB_URI
            valueFrom:
              secretKeyRef:
                name: recovery-backup-pitr-paradedb-superuser
                key: uri
        image: alpine:3.19
        command: ['sh', '-c']
        args:
         - |
           apk --no-cache add postgresql-client
           DB_URI=$(echo $DB_URI | sed "s|/\*|/|" )
           set -e
           test "$(psql $DB_URI -t -c 'SELECT EXISTS (SELECT FROM information_schema.tables WHERE table_name = $$mygoodtable$$)' --csv -q 2>/dev/null)" = "t"
           echo "Good table exists"
           test "$(psql $DB_URI -t -c 'SELECT EXISTS (SELECT FROM information_schema.tables WHERE table_name = $$mybadtable$$)' --csv -q 2>/dev/null)" = "f"
           echo "Bad table does not exist"

```

## File: charts\paradedb\test\paradedb-minio-backup-restore\chainsaw-test.yaml
```
##
# This test sets up a ParadeDB CNPG Cluster with MinIO backups and ensures that ParadeDB extensions are installed and
# PITR recovery is enabled and working.
apiVersion: chainsaw.kyverno.io/v1alpha1
kind: Test
metadata:
  name: paradedb
spec:
  timeouts:
    apply: 1s
    assert: 8m
    cleanup: 1m
  steps:
    - name: Clear the MinIO bucket
      try:
        - apply:
            file: ./00-minio_cleanup.yaml
        - assert:
            file: ./00-minio_cleanup-assert.yaml
    - name: Install a standalone ParadeDB CNPG Cluster
      try:
        - script:
            content: |
              kubectl -n $NAMESPACE create secret generic kube-root-ca.crt --from-literal=ca.crt="$(kubectl -n kube-system get configmaps kube-root-ca.crt -o jsonpath='{.data.ca\.crt}')" --dry-run=client -o yaml | kubectl apply -f -
              helm upgrade \
                --install \
                --namespace $NAMESPACE \
                --values ./01-paradedb_cluster.yaml \
                --wait \
                paradedb ../../
        - assert:
            file: ./01-paradedb_cluster-assert.yaml
      catch:
        - describe:
            apiVersion: postgresql.cnpg.io/v1
            kind: Cluster
        - podLogs:
            selector: cnpg.io/cluster=paradedb-paradedb
    - name: Initialize with ParadeDB sample data
      timeouts:
        apply: 1s
        assert: 10s
      try:
        - apply:
            file: ./02-paradedb_write.yaml
        - assert:
            file: ./02-paradedb_write-assert.yaml
      catch:
        - describe:
            apiVersion: batch/v1
            kind: Job
        - podLogs:
            selector: batch.kubernetes.io/job-name=data-write
    - name: Verify ParadeDB extensions are installed
      timeouts:
        apply: 1s
        assert: 30s
      try:
        - apply:
            file: 03-paradedb_test.yaml
        - assert:
            file: 03-paradedb_test-assert.yaml
      catch:
        - describe:
            apiVersion: batch/v1
            kind: Job
        - podLogs:
            selector: batch.kubernetes.io/job-name=paradedb-test
    - name: Write some data to the cluster
      timeouts:
        apply: 1s
        assert: 30s
      try:
        - apply:
            file: 04-data_write.yaml
        - assert:
            file: 04-data_write-assert.yaml
      catch:
        - describe:
            apiVersion: batch/v1
            kind: Job
        - podLogs:
            selector: batch.kubernetes.io/job-name=data-write
    - name: Start a backup
      try:
        - apply:
            file: ./05-backup.yaml
        - assert:
            file: ./05-backup_running-assert.yaml
      catch:
        - describe:
            apiVersion: postgresql.cnpg.io/v1
            kind: Backup
        - podLogs:
            selector: cnpg.io/cluster=paradedb
        - describe:
            apiVersion: postgresql.cnpg.io/v1
            kind: Cluster
        - podLogs:
            selector: cnpg.io/cluster=paradedb-paradedb
    - name: Complete a backup
      try:
        - apply:
            file: ./05-checkpoint.yaml
        - assert:
            file: ./05-backup_completed-assert.yaml
      catch:
        - describe:
            apiVersion: postgresql.cnpg.io/v1
            kind: Backup
        - podLogs:
            selector: cnpg.io/cluster=paradedb
        - describe:
            apiVersion: postgresql.cnpg.io/v1
            kind: Cluster
        - podLogs:
            selector: cnpg.io/cluster=paradedb-paradedb
    - name: Write more data to the database after the backup
      try:
        - apply:
            file: ./06-post_backup_data_write.yaml
        - assert:
            file: ./06-post_backup_data_write-assert.yaml
      timeouts:
        apply: 1s
        assert: 10m
      catch:
        - describe:
            apiVersion: postgresql.cnpg.io/v1
            kind: Backup
    - name: Create a recovery cluster from backup with a PITR target
      try:
        - script:
            content: |
              DATE_NO_BAD_TABLE=$(kubectl -n $NAMESPACE get configmap date-no-bad-table -o 'jsonpath={.data.date}')
              helm upgrade \
                --install \
                --namespace $NAMESPACE \
                --values ./07-recovery_backup_pitr_cluster.yaml \
                --set recovery.pitrTarget.time="$DATE_NO_BAD_TABLE" \
                --wait \
                recovery-backup-pitr ../../
        - assert:
            file: ./07-recovery_backup_pitr_cluster-assert.yaml
      catch:
        - describe:
            apiVersion: postgresql.cnpg.io/v1
            kind: Cluster
        - podLogs:
            selector: cnpg.io/cluster=recovery-backup-pitr-paradedb
    - name: Verify the pre-backup data on the recovery cluster exists but not the post-backup data
      try:
        - apply:
            file: 08-data_test.yaml
        - assert:
            file: 08-data_test-assert.yaml
      catch:
        - describe:
            apiVersion: batch/v1
            kind: Job
            name: data-test-backup-pitr
        - podLogs:
            selector: batch.kubernetes.io/job-name=data-test-backup-pitr
    - name: Cleanup
      try:
        - script:
            content: |
              helm uninstall --namespace $NAMESPACE paradedb

```

## File: charts\paradedb\test\paradedb-pg_basebackup\00-source-cluster-assert.yaml
```
apiVersion: postgresql.cnpg.io/v1
kind: Cluster
metadata:
  name: source-paradedb
status:
  readyInstances: 1

```

## File: charts\paradedb\test\paradedb-pg_basebackup\00-source-cluster.yaml
```
type: paradedb
mode: "standalone"
cluster:
  instances: 1
  storage:
    size: 256Mi
backups:
  enabled: false

```

## File: charts\paradedb\test\paradedb-pg_basebackup\01-data_write-assert.yaml
```
apiVersion: batch/v1
kind: Job
metadata:
  name: data-write
status:
  succeeded: 1

```

## File: charts\paradedb\test\paradedb-pg_basebackup\01-data_write.yaml
```
apiVersion: batch/v1
kind: Job
metadata:
  name: data-write
spec:
  template:
    spec:
      restartPolicy: OnFailure
      containers:
      - name: data-write
        env:
          - name: DB_USER
            valueFrom:
              secretKeyRef:
                name: source-paradedb-superuser
                key: username
          - name: DB_PASS
            valueFrom:
              secretKeyRef:
                name: source-paradedb-superuser
                key: password
          - name: DB_URI
            value: postgres://$(DB_USER):$(DB_PASS)@source-paradedb-rw:5432
        image: alpine:3.19
        command: ['sh', '-c']
        args:
         - |
           apk --no-cache add postgresql-client
           psql "$DB_URI" -c "CREATE DATABASE mygooddb;"
           psql "$DB_URI/mygooddb" -c "CREATE TABLE mygoodtable (id serial PRIMARY KEY);"

```

## File: charts\paradedb\test\paradedb-pg_basebackup\02-pg_basebackup-cluster-assert.yaml
```
apiVersion: postgresql.cnpg.io/v1
kind: Cluster
metadata:
  name: pg-basebackup-paradedb
status:
  readyInstances: 2

```

## File: charts\paradedb\test\paradedb-pg_basebackup\02-pg_basebackup-cluster.yaml
```
type: paradedb
mode: "recovery"
recovery:
  method: "pg_basebackup"
  pgBaseBackup:
    source:
      host: "source-paradedb-rw"
      database: "mygooddb"
      username: "streaming_replica"
      sslMode: "require"
      sslKeySecret:
        name: source-paradedb-replication
        key: tls.key
      sslCertSecret:
        name: source-paradedb-replication
        key: tls.crt
    secretName: "mysecret"

cluster:
  instances: 2
  storage:
    size: 256Mi

backups:
  enabled: false

```

## File: charts\paradedb\test\paradedb-pg_basebackup\02-secret.yaml
```
apiVersion: v1
kind: Secret
metadata:
  name: mysecret
type: kubernetes.io/basic-auth
data:
  username: YXBw
  password: cGFzc3dvcmQ=

```

## File: charts\paradedb\test\paradedb-pg_basebackup\03-data_test-assert.yaml
```
apiVersion: batch/v1
kind: Job
metadata:
  name: data-test
status:
  succeeded: 1

```

## File: charts\paradedb\test\paradedb-pg_basebackup\03-data_test.yaml
```
apiVersion: batch/v1
kind: Job
metadata:
  name: data-test
spec:
  template:
    spec:
      restartPolicy: OnFailure
      containers:
      - name: data-test
        env:
          - name: DB_URI
            valueFrom:
              secretKeyRef:
                name: pg-basebackup-paradedb-superuser
                key: uri
        image: alpine:3.19
        command: ['sh', '-c']
        args:
         - |
           apk --no-cache add postgresql-client
           DB_URI=$(echo $DB_URI | sed "s|/\*|/|" )
           test "$(psql "${DB_URI}mygooddb" -t -c 'SELECT EXISTS (SELECT FROM information_schema.tables WHERE table_name = $$mygoodtable$$)' --csv -q 2>/dev/null)" = "t"

```

## File: charts\paradedb\test\paradedb-pg_basebackup\chainsaw-test.yaml
```
##
# This is a test that provisions a regular (non CNPG) PostgreSQL cluster and attempts to perform a pg_basebackup recovery.
apiVersion: chainsaw.kyverno.io/v1alpha1
kind: Test
metadata:
  name: postgresql-pg-basebackup
spec:
  timeouts:
    apply: 1s
    assert: 2m
    cleanup: 1m
  steps:
    - name: Install the external PostgreSQL cluster
      try:
        - script:
            content: |
              helm upgrade \
                --install \
                --namespace $NAMESPACE \
                --values ./00-source-cluster.yaml \
                --wait \
                source ../../
        - assert:
            file: ./00-source-cluster-assert.yaml
        - apply:
            file: ./01-data_write.yaml
        - assert:
            file: ./01-data_write-assert.yaml
    - name: Install the pg_basebackup cluster
      timeouts:
        assert: 8m
      try:
        - script:
            content: |
              helm upgrade \
                --install \
                --namespace $NAMESPACE \
                --values ./02-pg_basebackup-cluster.yaml \
                --wait \
                pg-basebackup ../../
        - apply:
            file: ./02-secret.yaml
        - assert:
            file: ./02-pg_basebackup-cluster-assert.yaml
      catch:
        - describe:
            apiVersion: postgresql.cnpg.io/v1
            kind: Cluster
    - name: Verify the data from step 1 exists
      try:
        - apply:
            file: ./03-data_test.yaml
        - assert:
            file: ./03-data_test-assert.yaml
      catch:
        - describe:
            apiVersion: batch/v1
            kind: Job
        - podLogs:
            selector: batch.kubernetes.io/job-name=data-test
    - name: Cleanup
      try:
        - script:
            content: |
              helm uninstall --namespace $NAMESPACE source
              helm uninstall --namespace $NAMESPACE pg-basebackup

```

## File: charts\paradedb\test\pooler\01-pooler_cluster-assert.yaml
```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: pooler-paradedb-pooler-rw
status:
  readyReplicas: 2
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: pooler-paradedb-pooler-ro
status:
  readyReplicas: 2
---
apiVersion: postgresql.cnpg.io/v1
kind: Pooler
metadata:
  name: pooler-paradedb-pooler-rw
spec:
  cluster:
    name: pooler-paradedb
  instances: 2
  pgbouncer:
    poolMode: transaction
  type: rw
---
apiVersion: postgresql.cnpg.io/v1
kind: Pooler
metadata:
  name: pooler-paradedb-pooler-ro
spec:
  cluster:
    name: pooler-paradedb
  instances: 2
  pgbouncer:
    poolMode: session
  type: ro

```

## File: charts\paradedb\test\pooler\01-pooler_cluster.yaml
```
type: paradedb
mode: standalone
cluster:
  instances: 2
  storage:
    size: 256Mi
    storageClass: standard
backups:
  enabled: false
poolers:
  - name: rw
    type: rw
    instances: 2
    poolMode: transaction
  - name: ro
    type: ro
    instances: 2

```

## File: charts\paradedb\test\pooler\chainsaw-test.yaml
```
##
# This test verifies that PgBouncer poolers are correctly provisioned when configured via Helm values.
apiVersion: chainsaw.kyverno.io/v1alpha1
kind: Test
metadata:
  name: pooler
spec:
  timeouts:
    apply: 1s
    assert: 20s
    cleanup: 30s
  steps:
    - name: Install the non-default configuration cluster
      try:
        - script:
            content: |
              helm upgrade \
                --install \
                --namespace $NAMESPACE \
                --values ./01-pooler_cluster.yaml \
                --wait \
                pooler ../../
        - assert:
            file: ./01-pooler_cluster-assert.yaml
    - name: Cleanup
      try:
        - script:
            content: |
              helm uninstall --namespace $NAMESPACE pooler

```

## File: charts\paradedb\test\replica\00-minio_cleanup-assert.yaml
```
apiVersion: batch/v1
kind: Job
metadata:
  name: minio-cleanup
status:
  succeeded: 1

```

## File: charts\paradedb\test\replica\00-minio_cleanup.yaml
```
apiVersion: batch/v1
kind: Job
metadata:
  name: minio-cleanup
spec:
  template:
    spec:
      restartPolicy: OnFailure
      containers:
      - name: minio-cleanup
        image: minio/mc
        command: ['sh', '-c']
        args:
         - |
           mc alias set myminio https://minio.minio.svc.cluster.local minio minio123
           mc rm --recursive --force myminio/mybucket/replica

```

## File: charts\paradedb\test\replica\01-source_cluster-assert.yaml
```
apiVersion: postgresql.cnpg.io/v1
kind: Cluster
metadata:
  name: source-paradedb
status:
  readyInstances: 1

```

## File: charts\paradedb\test\replica\01-source_cluster_enterprise.yaml
```
type: paradedb-enterprise
mode: standalone
version:
  major: "18"
  paradedb: "0.22.3"
cluster:
  instances: 1
  storage:
    size: 256Mi
  imagePullSecrets:
    - name: paradedb-enterprise-registry-cred

backups:
  enabled: true
  provider: s3
  endpointURL: "https://minio.minio.svc.cluster.local"
  endpointCA:
    name: kube-root-ca.crt
    key: ca.crt
  wal:
    encryption: ""
  data:
    encryption: ""
  s3:
    bucket: "mybucket"
    path: "/replica/v1"
    accessKey: "minio"
    secretKey: "minio123"
    region: "local"
  scheduledBackups: []
  retentionPolicy: "30d"

```

## File: charts\paradedb\test\replica\02-data_write-assert.yaml
```
apiVersion: batch/v1
kind: Job
metadata:
  name: data-write
status:
  succeeded: 1

```

## File: charts\paradedb\test\replica\02-data_write.yaml
```
apiVersion: batch/v1
kind: Job
metadata:
  name: data-write
spec:
  template:
    spec:
      restartPolicy: OnFailure
      containers:
      - name: data-write
        env:
          - name: DB_USER
            valueFrom:
              secretKeyRef:
                name: source-paradedb-superuser
                key: username
          - name: DB_PASS
            valueFrom:
              secretKeyRef:
                name: source-paradedb-superuser
                key: password
          - name: DB_URI
            value: postgres://$(DB_USER):$(DB_PASS)@source-paradedb-rw:5432
        image: alpine:3.19
        command: ['sh', '-c']
        args:
         - |
           set -e
           apk --no-cache add postgresql-client
           psql "$DB_URI" -c "CREATE DATABASE mygooddb;"
           psql "$DB_URI/mygooddb" -c "CREATE TABLE mygoodtable (id serial PRIMARY KEY);"
           psql "$DB_URI/paradedb" <<-EOSQL
             CALL paradedb.create_bm25_test_table(
               schema_name => 'public',
               table_name => 'mock_items_paradedb_enterprise'
             );
             CREATE INDEX search_idx_paradedb_enterprise ON mock_items_paradedb_enterprise
             USING bm25 (id, description, category, rating, in_stock, created_at, metadata, weight_range)
             WITH (key_field='id');
           EOSQL
           RESULT=$(psql "$DB_URI/paradedb" -t) <<-EOSQL
             SELECT description
             FROM mock_items_paradedb_enterprise
             WHERE description @@@ '"bluetooth speaker"~1'
             LIMIT 1;
           EOSQL
           echo -$RESULT-
           if [ "$RESULT" = " Bluetooth-enabled speaker" ]; then
             echo "Test for description search passed."
           else
             echo "Test for description search failed."
             exit 1
           fi

```

## File: charts\paradedb\test\replica\03-backup.yaml
```
apiVersion: postgresql.cnpg.io/v1
kind: Backup
metadata:
  name: post-init-backup
spec:
  method: barmanObjectStore
  cluster:
    name: source-paradedb

```

## File: charts\paradedb\test\replica\03-backup_completed-assert.yaml
```
apiVersion: postgresql.cnpg.io/v1
kind: Backup
metadata:
  name: post-init-backup
spec:
  cluster:
    name: source-paradedb
  method: barmanObjectStore
status:
  phase: completed

```

## File: charts\paradedb\test\replica\03-backup_running-assert.yaml
```
apiVersion: postgresql.cnpg.io/v1
kind: Backup
metadata:
  name: post-init-backup
spec:
  cluster:
    name: source-paradedb
  method: barmanObjectStore
status:
  phase: running

```

## File: charts\paradedb\test\replica\03-checkpoint.yaml
```
apiVersion: batch/v1
kind: Job
metadata:
  name: backup-checkpoint
spec:
  template:
    spec:
      restartPolicy: OnFailure
      containers:
      - name: create-checkpoint
        env:
          - name: DB_URI
            valueFrom:
              secretKeyRef:
                name: source-paradedb-superuser
                key: uri
        image: alpine:3.19
        command: ['sh', '-c']
        args:
         - |
           apk --no-cache add postgresql-client
           DB_URI=$(echo $DB_URI | sed "s|/\*|/|" )
           END_TIME=$(( $(date +%s) + 30 ))
           while [ $(date +%s) -lt $END_TIME ]; do
             psql "$DB_URI" -c "SELECT pg_switch_wal();CHECKPOINT;"
             sleep 5
           done

```

## File: charts\paradedb\test\replica\04-replica_cluster-assert.yaml
```
apiVersion: postgresql.cnpg.io/v1
kind: Cluster
metadata:
  name: replica-paradedb
spec:
  replica:
    enabled: true
    source: originCluster
status:
  readyInstances: 1

```

## File: charts\paradedb\test\replica\04-replica_cluster_enterprise.yaml
```
type: paradedb-enterprise
mode: replica
cluster:
  instances: 1
  storage:
    size: 256Mi
  imagePullSecrets:
    - name: paradedb-enterprise-registry-cred

replica:
  bootstrap:
    source: pg_basebackup
  origin:
    pg_basebackup:
      host: "source-paradedb-rw"
      username: "streaming_replica"
      sslMode: "require"
      sslKeySecret:
        name: source-paradedb-replication
        key: tls.key
      sslCertSecret:
        name: source-paradedb-replication
        key: tls.crt

```

## File: charts\paradedb\test\replica\05-data_test-assert.yaml
```
apiVersion: batch/v1
kind: Job
metadata:
  name: data-test-replica
status:
  succeeded: 1

```

## File: charts\paradedb\test\replica\05-data_test.yaml
```
apiVersion: batch/v1
kind: Job
metadata:
  name: data-test-replica
spec:
  template:
    spec:
      restartPolicy: OnFailure
      containers:
      - name: data-test
        env:
          - name: DB_URI
            valueFrom:
              secretKeyRef:
                name: replica-paradedb-superuser
                key: uri
          - name: REPLICA_PASSWORD
            valueFrom:
              secretKeyRef:
                name: replica-paradedb-superuser
                key: password
          - name: SOURCE_PASSWORD
            valueFrom:
              secretKeyRef:
                name: source-paradedb-superuser
                key: password
        image: alpine:3.19
        command: ['sh', '-c']
        args:
         - |
           set -e
           apk --no-cache add postgresql-client
           DB_URI=$(echo $DB_URI | sed "s|/\*|/|" )
           DB_URI=$(echo $DB_URI | sed "s|$REPLICA_PASSWORD|$SOURCE_PASSWORD|" )
           echo "DB_URI: $DB_URI"
           test "$(psql "${DB_URI}mygooddb" -t -c 'SELECT EXISTS (SELECT FROM information_schema.tables WHERE table_name = $$mygoodtable$$)' --csv -q)" = "t"
           RESULT=$(psql "${DB_URI}paradedb" -t) <<-EOSQL
             SELECT description
             FROM mock_items_paradedb_enterprise
             WHERE description @@@ '"bluetooth speaker"~1'
             LIMIT 1;
           EOSQL
           echo -$RESULT-
           if [ "$RESULT" = " Bluetooth-enabled speaker" ]; then
             echo "Test for description search on replicas passed."
           else
             echo "Test for description search on replicas failed."
             exit 1
           fi

           SIZE_RESULT=$(psql "${DB_URI}paradedb" -t) <<-EOSQL
             SELECT pg_size_pretty(pg_relation_size('search_idx_paradedb_enterprise'));
           EOSQL
           echo -$SIZE_RESULT-
           if [ "$SIZE_RESULT" != " 0 bytes" ]; then
             echo "Test for index size on replicas passed."
           else
             echo "Test for index size on replicas failed."
             exit 1
           fi

```

## File: charts\paradedb\test\replica\06-replica_object_store_cluster-assert.yaml
```
apiVersion: postgresql.cnpg.io/v1
kind: Cluster
metadata:
  name: replica-object-store-paradedb
spec:
  replica:
    enabled: true
    source: originCluster
status:
  readyInstances: 1

```

## File: charts\paradedb\test\replica\06-replica_object_store_cluster.yaml
```
type: paradedb-enterprise
mode: replica
cluster:
  instances: 1
  storage:
    size: 256Mi
  imagePullSecrets:
    - name: paradedb-enterprise-registry-cred

replica:
  name: "off-site-backup1"
  bootstrap:
    source: object_store
  origin:
    objectStore:
      clusterName: source-paradedb
      provider: s3
      endpointURL: "https://minio.minio.svc.cluster.local"
      endpointCA:
        name: kube-root-ca.crt
        key: ca.crt
      wal:
        encryption: ""
      data:
        encryption: ""
      s3:
        bucket: "mybucket"
        path: "/replica/v1"
        accessKey: "minio"
        secretKey: "minio123"
        region: "local"
      scheduledBackups: []
      retentionPolicy: "30d"

```

## File: charts\paradedb\test\replica\07-data_test-assert.yaml
```
apiVersion: batch/v1
kind: Job
metadata:
  name: data-test-replica-object-store
status:
  succeeded: 1

```

## File: charts\paradedb\test\replica\07-data_test.yaml
```
apiVersion: batch/v1
kind: Job
metadata:
  name: data-test-replica-object-store
spec:
  template:
    spec:
      restartPolicy: OnFailure
      containers:
      - name: data-test
        env:
          - name: DB_URI
            valueFrom:
              secretKeyRef:
                name: replica-object-store-paradedb-superuser
                key: uri
          - name: REPLICA_PASSWORD
            valueFrom:
              secretKeyRef:
                name: replica-object-store-paradedb-superuser
                key: password
          - name: SOURCE_PASSWORD
            valueFrom:
              secretKeyRef:
                name: source-paradedb-superuser
                key: password
        image: alpine:3.19
        command: ['sh', '-c']
        args:
         - |
           set -e
           apk --no-cache add postgresql-client
           DB_URI=$(echo $DB_URI | sed "s|/\*|/|" )
           DB_URI=$(echo $DB_URI | sed "s|$REPLICA_PASSWORD|$SOURCE_PASSWORD|" )
           echo "DB_URI: $DB_URI"
           test "$(psql "${DB_URI}mygooddb" -t -c 'SELECT EXISTS (SELECT FROM information_schema.tables WHERE table_name = $$mygoodtable$$)' --csv -q)" = "t"
           RESULT=$(psql "${DB_URI}paradedb" -t) <<-EOSQL
             SELECT description
             FROM mock_items_paradedb_enterprise
             WHERE description @@@ '"bluetooth speaker"~1'
             LIMIT 1;
           EOSQL
           echo -$RESULT-
           if [ "$RESULT" = " Bluetooth-enabled speaker" ]; then
             echo "Test for description search on replicas passed."
           else
             echo "Test for description search on replicas failed."
             exit 1
           fi

           SIZE_RESULT=$(psql "${DB_URI}paradedb" -t) <<-EOSQL
             SELECT pg_size_pretty(pg_relation_size('search_idx_paradedb_enterprise'));
           EOSQL
           echo -$SIZE_RESULT-
           if [ "$SIZE_RESULT" != " 0 bytes" ]; then
             echo "Test for index size on replicas passed."
           else
             echo "Test for index size on replicas failed."
             exit 1
           fi

```

## File: charts\paradedb\test\replica\08-replica_hybrid_cluster-assert.yaml
```
apiVersion: postgresql.cnpg.io/v1
kind: Cluster
metadata:
  name: replica-hybrid-paradedb
spec:
  bootstrap:
    recovery:
      source: originCluster
  replica:
    enabled: true
    source: originCluster
status:
  readyInstances: 1

```

## File: charts\paradedb\test\replica\08-replica_hybrid_cluster.yaml
```
type: paradedb-enterprise
mode: replica
cluster:
  instances: 1
  storage:
    size: 256Mi
  imagePullSecrets:
    - name: paradedb-enterprise-registry-cred

replica:
  bootstrap:
    source: object_store
  origin:
    pg_basebackup:
      host: "source-paradedb-rw"
      username: "streaming_replica"
      sslMode: "require"
      sslKeySecret:
        name: source-paradedb-replication
        key: tls.key
      sslCertSecret:
        name: source-paradedb-replication
        key: tls.crt
    objectStore:
      clusterName: source-paradedb
      provider: s3
      endpointURL: "https://minio.minio.svc.cluster.local"
      endpointCA:
        name: kube-root-ca.crt
        key: ca.crt
      wal:
        encryption: ""
      data:
        encryption: ""
      s3:
        bucket: "mybucket"
        path: "/replica/v1"
        accessKey: "minio"
        secretKey: "minio123"
        region: "local"
      scheduledBackups: []
      retentionPolicy: "30d"

```

## File: charts\paradedb\test\replica\09-data_test-assert.yaml
```
apiVersion: batch/v1
kind: Job
metadata:
  name: data-test-replica-hybrid
status:
  succeeded: 1

```

## File: charts\paradedb\test\replica\09-data_test.yaml
```
apiVersion: batch/v1
kind: Job
metadata:
  name: data-test-replica-hybrid
spec:
  template:
    spec:
      restartPolicy: OnFailure
      containers:
      - name: data-test
        env:
          - name: DB_URI
            valueFrom:
              secretKeyRef:
                name: replica-hybrid-paradedb-superuser
                key: uri
          - name: REPLICA_PASSWORD
            valueFrom:
              secretKeyRef:
                name: replica-hybrid-paradedb-superuser
                key: password
          - name: SOURCE_PASSWORD
            valueFrom:
              secretKeyRef:
                name: source-paradedb-superuser
                key: password
        image: alpine:3.19
        command: ['sh', '-c']
        args:
         - |
           set -e
           apk --no-cache add postgresql-client
           DB_URI=$(echo $DB_URI | sed "s|/\*|/|" )
           DB_URI=$(echo $DB_URI | sed "s|$REPLICA_PASSWORD|$SOURCE_PASSWORD|" )
           echo "DB_URI: $DB_URI"
           test "$(psql "${DB_URI}mygooddb" -t -c 'SELECT EXISTS (SELECT FROM information_schema.tables WHERE table_name = $$mygoodtable$$)' --csv -q)" = "t"
           RESULT=$(psql "${DB_URI}paradedb" -t) <<-EOSQL
             SELECT description
             FROM mock_items_paradedb_enterprise
             WHERE description @@@ '"bluetooth speaker"~1'
             LIMIT 1;
           EOSQL
           echo -$RESULT-
           if [ "$RESULT" = " Bluetooth-enabled speaker" ]; then
             echo "Test for description search on replicas passed."
           else
             echo "Test for description search on replicas failed."
             exit 1
           fi

           SIZE_RESULT=$(psql "${DB_URI}paradedb" -t) <<-EOSQL
             SELECT pg_size_pretty(pg_relation_size('search_idx_paradedb_enterprise'));
           EOSQL
           echo -$SIZE_RESULT-
           if [ "$SIZE_RESULT" != " 0 bytes" ]; then
             echo "Test for index size on replicas passed."
           else
             echo "Test for index size on replicas failed."
             exit 1
           fi

```

## File: charts\paradedb\test\replica\chainsaw-test.yaml
```
##
# This test creates a source CNPG cluster with ParadeDB Enterprise (required for WALs) and with MinIO backups
# and then creates a replica cluster bootstrapped with pg_basebackup, object store, and a hybrid one, using both.
apiVersion: chainsaw.kyverno.io/v1alpha1
kind: Test
metadata:
  name: replica
spec:
  timeouts:
    apply: 1s
    assert: 3m
    cleanup: 1m
  steps:
    - name: Clear the MinIO bucket
      try:
        - apply:
            file: ./00-minio_cleanup.yaml
        - assert:
            file: ./00-minio_cleanup-assert.yaml
      catch:
        - describe:
            apiVersion: batch/v1
            kind: Job
        - podLogs:
            selector: batch.kubernetes.io/job-name=minio-cleanup
    - name: Install a source cluster with Enterprise
      try:
        - script:
            content: |
              # Create Docker registry secret for ParadeDB Enterprise
              kubectl -n $NAMESPACE create secret docker-registry paradedb-enterprise-registry-cred --docker-server="https://index.docker.io/v1/" --docker-username="$PARADEDB_ENTERPRISE_DOCKER_USERNAME" --docker-password="$PARADEDB_ENTERPRISE_DOCKER_PAT"

              kubectl -n $NAMESPACE create secret generic kube-root-ca.crt --from-literal=ca.crt="$(kubectl -n kube-system get configmaps kube-root-ca.crt -o jsonpath='{.data.ca\.crt}')" --dry-run=client -o yaml | kubectl apply -f -
              helm upgrade \
                --install \
                --namespace $NAMESPACE \
                --values ./01-source_cluster_enterprise.yaml \
                --wait \
                source ../../
        - assert:
            file: 01-source_cluster-assert.yaml
      catch:
        - describe:
            apiVersion: postgresql.cnpg.io/v1
            kind: Cluster
    - name: Write some data to the cluster
      try:
        - apply:
            file: ./02-data_write.yaml
        - assert:
            file: ./02-data_write-assert.yaml
      catch:
        - describe:
            apiVersion: batch/v1
            kind: Job
        - podLogs:
            selector: batch.kubernetes.io/job-name=data-write
    - name: Create a backup
      try:
        - apply:
            file: ./03-backup.yaml
        - assert:
            file: ./03-backup_running-assert.yaml
        - apply:
            file: ./03-checkpoint.yaml
        - assert:
            file: ./03-backup_completed-assert.yaml
    - name: Create a replica cluster from pg_basebackup
      try:
        - script:
            content: |
              helm upgrade \
                --install \
                --namespace $NAMESPACE \
                --values ./04-replica_cluster_enterprise.yaml \
                --wait \
                replica ../../
        - assert:
            file: ./04-replica_cluster-assert.yaml
    - name: Verify the data on the replica cluster exists
      timeouts:
        apply: 1s
        assert: 4m
      try:
        - script:
            content: |
              # Wait for replica cluster to be ready and verify it's streaming
              echo "Waiting for replica cluster to be ready..."
              kubectl wait --for=condition=ready cluster/replica-paradedb -n $NAMESPACE --timeout=5m || true
              echo "Checking replica cluster status..."
              kubectl get cluster replica-paradedb -n $NAMESPACE -o yaml
              echo "Checking replica pods..."
              kubectl get pods -n $NAMESPACE -l cnpg.io/cluster=replica-paradedb
        - apply:
            file: 05-data_test.yaml
        - assert:
            file: 05-data_test-assert.yaml
      catch:
        - describe:
            apiVersion: postgresql.cnpg.io/v1
            kind: Cluster
            name: replica-paradedb
        - describe:
            apiVersion: batch/v1
            kind: Job
            name: data-test-replica
        - podLogs:
            selector: batch.kubernetes.io/job-name=data-test-replica
        - podLogs:
            selector: cnpg.io/cluster=replica-paradedb
        - script:
            content: |
              echo "=== Replica Cluster Conditions ==="
              kubectl get cluster replica-paradedb -n $NAMESPACE -o jsonpath='{.status.conditions}' | jq '.' || kubectl get cluster replica-paradedb -n $NAMESPACE -o yaml | grep -A 20 "conditions:"

              echo "=== Replica Cluster Status ==="
              kubectl get cluster replica-paradedb -n $NAMESPACE -o jsonpath='{.status}' | jq '.' || kubectl get cluster replica-paradedb -n $NAMESPACE -o yaml | grep -A 30 "status:"

              echo "=== Replica Pod Status ==="
              REPLICA_POD=$(kubectl get pods -n $NAMESPACE -l cnpg.io/cluster=replica-paradedb -o jsonpath='{.items[0].metadata.name}' 2>/dev/null)
              if [ -n "$REPLICA_POD" ]; then
                echo "Replica pod: $REPLICA_POD"
                kubectl get pod $REPLICA_POD -n $NAMESPACE -o jsonpath='{.status.conditions}' | jq '.' || kubectl get pod $REPLICA_POD -n $NAMESPACE -o yaml | grep -A 15 "conditions:"
                echo "=== Replica Pod Events ==="
                kubectl get events -n $NAMESPACE --field-selector involvedObject.name=$REPLICA_POD --sort-by='.lastTimestamp' | tail -20
              fi

              echo "=== Cluster Events (last 30) ==="
              kubectl get events -n $NAMESPACE --field-selector involvedObject.kind=Cluster --sort-by='.lastTimestamp' | tail -30
    - name: Create a replica cluster from object store
      try:
        - script:
            content: |
              helm upgrade \
                --install \
                --namespace $NAMESPACE \
                --values ./06-replica_object_store_cluster.yaml \
                --wait \
                replica-object-store ../../
        - assert:
            file: ./06-replica_object_store_cluster-assert.yaml
    - name: Verify the data on the object store replica cluster exists
      try:
        - apply:
            file: 07-data_test.yaml
        - assert:
            file: 07-data_test-assert.yaml
    - name: Create a hybrid replica cluster
      try:
        - script:
            content: |
              helm upgrade \
                --install \
                --namespace $NAMESPACE \
                --values ./08-replica_hybrid_cluster.yaml \
                --wait \
                replica-hybrid ../../
        - assert:
            file: ./08-replica_hybrid_cluster-assert.yaml
    - name: Verify the data on the hybrid replica cluster exists
      try:
        - apply:
            file: 09-data_test.yaml
        - assert:
            file: 09-data_test-assert.yaml
    - name: Cleanup
      try:
        - script:
            content: |
              helm uninstall --namespace $NAMESPACE source
              helm uninstall --namespace $NAMESPACE replica
              helm uninstall --namespace $NAMESPACE replica-object-store
              helm uninstall --namespace $NAMESPACE replica-hybrid

```

## File: charts\paradedb\test\scheduledbackups\00-minio_cleanup-assert.yaml
```
apiVersion: batch/v1
kind: Job
metadata:
  name: minio-cleanup
status:
  succeeded: 1

```

## File: charts\paradedb\test\scheduledbackups\00-minio_cleanup.yaml
```
apiVersion: batch/v1
kind: Job
metadata:
  name: minio-cleanup
spec:
  template:
    spec:
      restartPolicy: OnFailure
      containers:
      - name: minio-cleanup
        image: minio/mc
        command: ['sh', '-c']
        args:
         - |
           mc alias set myminio https://minio.minio.svc.cluster.local minio minio123
           mc rm --recursive --force myminio/mybucket/scheduledbackups

```

## File: charts\paradedb\test\scheduledbackups\01-scheduledbackups_cluster-assert.yaml
```
apiVersion: postgresql.cnpg.io/v1
kind: Cluster
metadata:
  name: scheduledbackups-paradedb
status:
  readyInstances: 1
---
apiVersion: postgresql.cnpg.io/v1
kind: ScheduledBackup
metadata:
  name: scheduledbackups-paradedb-daily-backup
spec:
  immediate: true
  schedule: "0 0 0 * * *"
  method: barmanObjectStore
  backupOwnerReference: self
  cluster:
    name: scheduledbackups-paradedb
---
apiVersion: postgresql.cnpg.io/v1
kind: ScheduledBackup
metadata:
  name: scheduledbackups-paradedb-weekly-backup
spec:
  immediate: true
  schedule: "0 0 0 * * 1"
  method: barmanObjectStore
  backupOwnerReference: self
  cluster:
    name: scheduledbackups-paradedb
---
apiVersion: postgresql.cnpg.io/v1
kind: Backup
spec:
  method: barmanObjectStore
  cluster:
    name: scheduledbackups-paradedb

```

## File: charts\paradedb\test\scheduledbackups\01-scheduledbackups_cluster.yaml
```
type: paradedb
mode: standalone
version:
  major: "18"
  paradedb: "0.22.3"
cluster:
  instances: 1
  storage:
    size: 256Mi

backups:
  enabled: true
  provider: s3
  endpointURL: "https://minio.minio.svc.cluster.local"
  endpointCA:
    name: kube-root-ca.crt
    key: ca.crt
  wal:
    encryption: ""
  data:
    encryption: ""
  s3:
    bucket: "mybucket"
    path: "/scheduledbackups/v1"
    accessKey: "minio"
    secretKey: "minio123"
    region: "local"
  retentionPolicy: "30d"
  scheduledBackups:
    - name: daily-backup
      schedule: "0 0 0 * * *"
      backupOwnerReference: self
      method: barmanObjectStore
    - name: weekly-backup
      schedule: "0 0 0 * * 1"
      backupOwnerReference: self
      method: barmanObjectStore

```

## File: charts\paradedb\test\scheduledbackups\chainsaw-test.yaml
```
apiVersion: chainsaw.kyverno.io/v1alpha1
kind: Test
metadata:
  name: scheduledbackups
spec:
  timeouts:
    apply: 1s
    assert: 1m
    cleanup: 5m
  steps:
    - name: Install the ParadeDB cluster with ScheduledBackups
      try:
        - script:
            content: |
              helm upgrade \
                --install \
                --namespace $NAMESPACE \
                --values ./01-scheduledbackups_cluster.yaml \
                --wait \
                scheduledbackups ../../
        - assert:
            file: ./01-scheduledbackups_cluster-assert.yaml
    - name: Cleanup
      try:
        - script:
            content: |
              helm uninstall --namespace $NAMESPACE scheduledbackups

```


---
id: codacy-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:07.247225
---

# KNOWLEDGE EXTRACT: codacy
> **Extracted on:** 2026-03-30 17:34:26
> **Source:** codacy

---

## File: `codacy-analysis-cli-action.md`
```markdown
# 📦 codacy/codacy-analysis-cli-action [🔖 PENDING/APPROVE]
🔗 https://github.com/codacy/codacy-analysis-cli-action
🌐 https://github.com/codacy/codacy-analysis-cli

## Meta
- **Stars:** ⭐ 65 | **Forks:** 🍴 17
- **Language:** N/A | **License:** Apache-2.0
- **Last updated:** 2026-03-25
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
GitHub Action for the codacy-analysis-cli

## README (trích đầu)
```
# Codacy Analysis CLI GitHub Action

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/946b78614f154f81b1c9c0514fd9f35c)](https://www.codacy.com/gh/codacy/codacy-analysis-cli-action/dashboard?utm_source=github.com&utm_medium=referral&utm_content=codacy/codacy-analysis-cli-action&utm_campaign=Badge_Grade)

GitHub Action for running Codacy static analysis on [over 40 supported languages](https://docs.codacy.com/getting-started/supported-languages-and-tools/) and returning identified issues in the code.

<br/>

<a href="https://www.codacy.com" target="_blank"><img src="images/codacy-logo.svg" alt="Codacy" width="400"/></a>

<br/>

[Codacy](https://www.codacy.com/) is an automated code review tool that makes it easy to ensure your team is writing high-quality code by analyzing more than 40 programming languages such as PHP, JavaScript, Python, Java, and Ruby. Codacy allows you to define your own quality rules, code patterns and quality settings you'd like to enforce to prevent issues on your codebase.

The Codacy GitHub Action supports the following scenarios:

-   **[Analysis with default settings](#analysis-with-default-settings):** Analyzes each commit and pull request and fails the workflow if it finds issues in your code.
-   **[Integration with GitHub code scanning](#integration-with-github-code-scanning):** Analyzes each commit and pull request and uploads the results to GitHub, which displays the identified issues under your repository's tab **Security**.
-   **[Integration with Codacy for client-side tools](#integration-with-codacy-for-client-side-tools):** Analyzes each commit and pull request using one of Codacy's client-side tools and uploads the results to Codacy, which displays the identified issues in UI dashboards and can also report the status of the analysis on your pull requests.

## Analysis with default settings

By default, the Codacy GitHub Action:

-   Analyzes each commit or pull request by running all supported static code analysis tools for the languages found in your repository.
-   Prints the analysis results on the console, which is visible on the GitHub Action's workflow panel.  
-   Fails the workflow if it finds at least one issue in your code.

![Failed Codacy analysis workflow](images/failed-workflow.png)

To use the GitHub Action with default settings, add the following to a file `.github/workflows/codacy-analysis.yaml` in your repository:

```yaml
name: Codacy Analysis CLI

on: ["push"]

jobs:
  codacy-analysis-cli:
    name: Codacy Analysis CLI
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@main

      - name: Run Codacy Analysis CLI
        uses: codacy/codacy-analysis-cli-action@master
```

## Integration with GitHub code scanning

Integrate the Codacy GitHub Action with [GitHub code scanning](https://docs.github.com/github/finding-security-vulnerabilities-and-errors-in-your-code/about-code-scanning) to display the analysis results on your repository u
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `codacy-analysis-cli.md`
```markdown
# 📦 codacy/codacy-analysis-cli [🔖 PENDING/APPROVE]
🔗 https://github.com/codacy/codacy-analysis-cli
🌐 https://www.codacy.com

## Meta
- **Stars:** ⭐ 113 | **Forks:** 🍴 29
- **Language:** Scala | **License:** AGPL-3.0
- **Last updated:** 2026-03-25
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
The Codacy Analysis CLI is a command line interface that enables you to execute Codacy code analysis locally.

## README (trích đầu)
```
> ⚠️ **Legacy Component Warning**  
> This component is part of our **classic/legacy** implementation is no longer actively maintained for local analysis; please use the [new Codacy CLI v2 instead](https://github.com/codacy/codacy-cli-v2/).
> For uploading results to Codacy, use this CLI.


# Codacy Analysis CLI

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/2aa6927599ba4d9db6c9cfcb38e397e4)](https://www.codacy.com/gh/codacy/codacy-analysis-cli?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=codacy/codacy-analysis-cli&amp;utm_campaign=Badge_Grade)
[![Codacy Badge](https://api.codacy.com/project/badge/Coverage/2aa6927599ba4d9db6c9cfcb38e397e4)](https://www.codacy.com/gh/codacy/codacy-analysis-cli?utm_source=github.com&utm_medium=referral&utm_content=codacy/codacy-analysis-cli&utm_campaign=Badge_Coverage)
[![CircleCI](https://circleci.com/gh/codacy/codacy-analysis-cli.svg?style=svg)](https://circleci.com/gh/codacy/codacy-analysis-cli)
[![Docker Version](https://images.microbadger.com/badges/version/codacy/codacy-analysis-cli.svg)](https://microbadger.com/images/codacy/codacy-analysis-cli "Get your own version badge on microbadger.com")
[![Maven Central](https://maven-badges.herokuapp.com/maven-central/com.codacy/codacy-analysis-core_2.12/badge.svg)](https://maven-badges.herokuapp.com/maven-central/com.codacy/codacy-analysis-core_2.12)

Command line interface to execute Codacy code analysis locally.

With a single command you can:
  - Get static code analysis issues, complexity, duplication and other code metrics
  - Run a tool or the whole suite of supported tools by Codacy
  - Use the tools' default patterns, your configuration files or your settings saved on Codacy

## Prerequisites

### Usage

* Java 8+
* Docker 17.09+

### Development

* Java 8+
* SBT 1.1.x
* Scala 2.12.x
* Docker 17.09+

## Install

```bash
curl -L https://github.com/codacy/codacy-analysis-cli/archive/master.tar.gz | tar xvz
cd codacy-analysis-cli-* && sudo make install
```

### Windows

#### Pre-Requisites
- Have Docker installed on Windows (https://hub.docker.com/editions/community/docker-ce-desktop-windows)
- Have WSL enabled with Ubuntu bash installed (https://docs.microsoft.com/en-us/windows/wsl/install-win10)

#### Docker Configuration
Once the pre-requisites are met, it’s time to enable the connectivity between bash and docker.

It’s mandatory that the daemon is exposed without TLS. In order to do that go to Docker Settings -> General. Just click on the checkbox with the label 'Expose daemon on tcp://localhost:2375 without TLS' and docker will reload.

#### Preparing docker client on bash
Now it’s time to go to the bash and install and configure the docker client.

If you are using Windows 10 (build above 1803) the following command will make the docker client available from the bash
```sudo ln -s "/mnt/c/Program Files/Docker/Docker/resources/bin/docker.exe" /usr/local/bin/docker```

If you are using a previous version of Windows 10, [here](h
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```


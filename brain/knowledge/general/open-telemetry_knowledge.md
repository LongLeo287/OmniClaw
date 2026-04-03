---
id: open-telemetry-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:29:15.610352
---

# KNOWLEDGE EXTRACT: open-telemetry
> **Extracted on:** 2026-03-30 17:50:05
> **Source:** open-telemetry

---

## File: `opentelemetry-collector.md`
```markdown
# 📦 open-telemetry/opentelemetry-collector [🔖 PENDING/APPROVE]
🔗 https://github.com/open-telemetry/opentelemetry-collector
🌐 https://opentelemetry.io

## Meta
- **Stars:** ⭐ 6760 | **Forks:** 🍴 1952
- **Language:** Go | **License:** Apache-2.0
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
OpenTelemetry Collector

## README (trích đầu)
```
---

<p align="center">
  <strong>
    <a href="https://opentelemetry.io/docs/collector/getting-started/">Getting Started</a>
    &nbsp;&nbsp;&bull;&nbsp;&nbsp;
    <a href="CONTRIBUTING.md">Getting Involved</a>
    &nbsp;&nbsp;&bull;&nbsp;&nbsp;
    <a href="https://cloud-native.slack.com/archives/C01N6P7KR6W">Getting In Touch</a>
  </strong>
</p>

<p align="center">
  <a href="https://github.com/open-telemetry/opentelemetry-collector/actions/workflows/build-and-test.yml?query=branch%3Amain">
    <img alt="Build Status" src="https://img.shields.io/github/actions/workflow/status/open-telemetry/opentelemetry-collector/build-and-test.yml?branch=main&style=for-the-badge">
  </a>
  <a href="https://goreportcard.com/report/github.com/open-telemetry/opentelemetry-collector">
    <img alt="Go Report Card" src="https://goreportcard.com/badge/github.com/open-telemetry/opentelemetry-collector?style=for-the-badge">
  </a>
  <a href="https://codecov.io/gh/open-telemetry/opentelemetry-collector/branch/main/">
    <img alt="Codecov Status" src="https://img.shields.io/codecov/c/github/open-telemetry/opentelemetry-collector?style=for-the-badge">
  </a>
  <a href="https://github.com/open-telemetry/opentelemetry-collector/releases">
    <img alt="GitHub release (latest by date including pre-releases)" src="https://img.shields.io/github/v/release/open-telemetry/opentelemetry-collector?include_prereleases&style=for-the-badge">
  </a>
  </br>
  <a href="https://www.bestpractices.dev/projects/8404"><img src="https://www.bestpractices.dev/projects/8404/badge">
  </a>
  <a href="https://bugs.chromium.org/p/oss-fuzz/issues/list?sort=-opened&can=1&q=proj:opentelemetry">
    <img alt="Fuzzing Status" src="https://oss-fuzz-build-logs.storage.googleapis.com/badges/opentelemetry.svg">
  </a>
</p>

<p align="center">
  <strong>
    <a href="docs/vision.md">Vision</a>
    &nbsp;&nbsp;&bull;&nbsp;&nbsp;
    <a href="https://opentelemetry.io/docs/collector/configuration/">Configuration</a>
    &nbsp;&nbsp;&bull;&nbsp;&nbsp;
    <a href="https://opentelemetry.io/docs/collector/internal-telemetry/#use-internal-telemetry-to-monitor-the-collector">Monitoring</a>
    &nbsp;&nbsp;&bull;&nbsp;&nbsp;
    <a href="docs/security-best-practices.md">Security</a>
    &nbsp;&nbsp;&bull;&nbsp;&nbsp;
    <a href="https://pkg.go.dev/go.opentelemetry.io/collector">Package</a>
  </strong>
</p>

---

# <img src="https://opentelemetry.io/img/logos/opentelemetry-logo-nav.png" alt="OpenTelemetry Icon" width="45" height=""> OpenTelemetry Collector

The OpenTelemetry Collector offers a vendor-agnostic implementation on how to
receive, process and export telemetry data. In addition, it removes the need
to run, operate and maintain multiple agents/collectors in order to support
open-source telemetry data formats (e.g. Jaeger, Prometheus, etc.) to
multiple open-source or commercial back-ends.

Objectives:

- Usable: Reasonable default configuration, supports popular protocols, runs and collects out of the b
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `opentelemetry-dotnet.md`
```markdown
# 📦 open-telemetry/opentelemetry-dotnet [🔖 PENDING/APPROVE]
🔗 https://github.com/open-telemetry/opentelemetry-dotnet
🌐 https://opentelemetry.io

## Meta
- **Stars:** ⭐ 3680 | **Forks:** 🍴 880
- **Language:** C# | **License:** Apache-2.0
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
The OpenTelemetry .NET Client

## README (trích đầu)
```
# OpenTelemetry .NET

[![Slack](https://img.shields.io/badge/slack-@cncf/otel/dotnet-brightgreen.svg?logo=slack)](https://cloud-native.slack.com/archives/C01N3BC2W7Q)
[![codecov.io](https://codecov.io/gh/open-telemetry/opentelemetry-dotnet/branch/main/graphs/badge.svg?)](https://codecov.io/gh/open-telemetry/opentelemetry-dotnet/)
[![Nuget](https://img.shields.io/nuget/v/OpenTelemetry.svg)](https://www.nuget.org/profiles/OpenTelemetry)
[![NuGet](https://img.shields.io/nuget/dt/OpenTelemetry.svg)](https://www.nuget.org/profiles/OpenTelemetry)
[![Build](https://github.com/open-telemetry/opentelemetry-dotnet/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/open-telemetry/opentelemetry-dotnet/actions/workflows/ci.yml)

[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/open-telemetry/opentelemetry-dotnet/badge)](https://scorecard.dev/viewer/?uri=github.com/open-telemetry/opentelemetry-dotnet)
[![OpenSSF Best Practices](https://www.bestpractices.dev/projects/10017/badge)](https://www.bestpractices.dev/projects/10017)
[![FOSSA License Status](https://app.fossa.com/api/projects/custom%2B162%2Fgithub.com%2Fopen-telemetry%2Fopentelemetry-dotnet.svg?type=shield&issueType=license)](https://app.fossa.com/projects/custom%2B162%2Fgithub.com%2Fopen-telemetry%2Fopentelemetry-dotnet?ref=badge_shield&issueType=license)
[![FOSSA Security Status](https://app.fossa.com/api/projects/custom%2B162%2Fgithub.com%2Fopen-telemetry%2Fopentelemetry-dotnet.svg?type=shield&issueType=security)](https://app.fossa.com/projects/custom%2B162%2Fgithub.com%2Fopen-telemetry%2Fopentelemetry-dotnet?ref=badge_shield&issueType=security)

The .NET [OpenTelemetry](https://opentelemetry.io/) implementation.

<details>
<summary>Table of Contents</summary>

* [Supported .NET versions](#supported-net-versions)
* [Project status](#project-status)
* [Getting started](#getting-started)
  * [Getting started with Logging](#getting-started-with-logging)
  * [Getting started with Metrics](#getting-started-with-metrics)
  * [Getting started with Tracing](#getting-started-with-tracing)
* [Repository structure](#repository-structure)
* [Troubleshooting](#troubleshooting)
* [Extensibility](#extensibility)
* [Releases](#releases)
* [Contributing](#contributing)
* [References](#references)

</details>

## Supported .NET versions

Packages shipped from this repository generally support all the officially
supported versions of [.NET](https://dotnet.microsoft.com/download/dotnet) and
[.NET Framework](https://dotnet.microsoft.com/download/dotnet-framework) (an
older Windows-based .NET implementation), except `.NET Framework 3.5`.
Any exceptions to this are noted in the individual `README.md`
files.

## Project status

**Stable** across all 3 signals (`Logs`, `Metrics`, and `Traces`).

> [!CAUTION]
> Certain components, marked as
[pre-release](https://github.com/open-telemetry/opentelemetry-dotnet/blob/main/VERSIONING.md#pre-releases),
are still work in progress and can undergo 
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `opentelemetry-ebpf-profiler.md`
```markdown
# 📦 open-telemetry/opentelemetry-ebpf-profiler [🔖 PENDING/APPROVE]
🔗 https://github.com/open-telemetry/opentelemetry-ebpf-profiler


## Meta
- **Stars:** ⭐ 3049 | **Forks:** 🍴 387
- **Language:** Go | **License:** Apache-2.0
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
The production-scale datacenter profiler (C/C++, Go, Rust, Python, Java, NodeJS, .NET, PHP, Ruby, Perl, ...)

## README (trích đầu)
```
# Introduction

This repository implements a whole-system, cross-language profiler for Linux via
eBPF.

## Core features and strengths

- Implements the [Alpha OTel Profiles signal](https://github.com/open-telemetry/opentelemetry-proto/pull/775)
- Very low CPU and memory overhead (1% CPU and 250MB memory are our upper limits
  in testing and the agent typically manages to stay way below that)
- Support for native C/C++ executables without the need for DWARF debug
  information (by leveraging `.eh_frame` data as described in
  [US11604718B1](https://patents.google.com/patent/US11604718B1/en?inventor=thomas+dullien&oq=thomas+dullien))
- Support profiling of system libraries **without frame pointers** and **without
  debug symbols on the host**.
- Support for mixed stacktraces between runtimes - stacktraces go from Kernel
  space through unmodified system libraries all the way into high-level
  languages.
- Support for native code (C/C++, Rust, Zig, Go, etc. without debug symbols on
  host)
- Support for a broad set of HLLs, like Hotspot JVM, Python, Ruby, PHP, Node.JS,
  V8, Perl, Erlang and .NET.
- 100% non-intrusive: there's no need to load agents or libraries into the
  processes that are being profiled.
- No need for any reconfiguration, instrumentation or restarts of HLL
  interpreters and VMs: the agent supports unwinding each of the supported
  languages in the default configuration.
- ARM64 support for all unwinders except .NET.
- Support for native `inline frames`, which provide insights into compiler
  optimizations and offer a higher precision of function call chains.

## Building

We have integrated the profiler into the [OTel Collector](https://opentelemetry.io/docs/collector/) as a receiver,
and this is the [supported configuration](https://github.com/open-telemetry/opentelemetry-collector-releases/tree/main/distributions/otelcol-ebpf-profiler) going forward.

To aid with development, testing and debugging, we also offer a standalone profiling agent binary named `ebpf-profiler`,
and a local build of an OTel Collector profiling receiver binary (`otelcol-ebpf-profiler`). These binaries are not
supported in any way, can be dropped in the future and should not be deployed in production.

## Platform Requirements
The agent can be built with the provided make targets. Docker is required for containerized builds, and both amd64 and arm64 architectures are supported.

 For **Linux**, the following steps apply:
  1. Build the agent for your current machine's architecture:
     ```sh
     make agent
     ```
     Or `make debug-agent` for debug build.
  2. To cross-compile for a different architecture (e.g. arm64):
     ```sh
     make agent TARGET_ARCH=arm64
     ```
The resulting binary will be named `ebpf-profiler` in the current directory.

## Other OSes
Since the profiler is Linux-only, macOS and Windows users need to set up a Linux VM to build and run the agent. Ensure the appropriate architecture is specified if using cross-compilation. 
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `opentelemetry-java-instrumentation.md`
```markdown
# 📦 open-telemetry/opentelemetry-java-instrumentation [🔖 PENDING/APPROVE]
🔗 https://github.com/open-telemetry/opentelemetry-java-instrumentation
🌐 https://opentelemetry.io

## Meta
- **Stars:** ⭐ 2488 | **Forks:** 🍴 1075
- **Language:** Java | **License:** Apache-2.0
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
OpenTelemetry auto-instrumentation and instrumentation libraries for Java

## README (trích đầu)
```
# OpenTelemetry Instrumentation for Java

[![Release](https://img.shields.io/github/v/release/open-telemetry/opentelemetry-java-instrumentation?include_prereleases&style=)](https://github.com/open-telemetry/opentelemetry-java-instrumentation/releases/)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/open-telemetry/opentelemetry-java-instrumentation/badge)](https://scorecard.dev/viewer/?uri=github.com/open-telemetry/opentelemetry-java-instrumentation)
[![Slack](https://img.shields.io/badge/slack-@cncf/otel--java-blue.svg?logo=slack)](https://cloud-native.slack.com/archives/C014L2KCTE3)

* [About](#about)
* [Getting Started](#getting-started)
* [Configuring the Agent](#configuring-the-agent)
* [Supported libraries, frameworks, and application servers](#supported-libraries-frameworks-and-application-servers)
* [Creating agent extensions](#creating-agent-extensions)
* [Manually instrumenting](#manually-instrumenting)
* [Logger MDC auto-instrumentation](#logger-mdc-mapped-diagnostic-context-auto-instrumentation)
* [Troubleshooting](#troubleshooting)
* [Contributing](#contributing)

## About

This project provides a Java agent JAR that can be attached to any Java 8+
application and dynamically injects bytecode to capture telemetry from a
number of popular libraries and frameworks.
You can export the telemetry data in a variety of formats.
You can also configure the agent and exporter via command line arguments
or environment variables. The net result is the ability to gather telemetry
data from a Java application without code changes.

This repository also publishes standalone instrumentation for several libraries (and growing)
that can be used if you prefer that over using the Java agent.
Please see the standalone library instrumentation column
on [Supported Libraries](docs/supported-libraries.md#libraries--frameworks).
If you are looking for documentation on using those.

## Getting Started

Download
the [latest version](https://github.com/open-telemetry/opentelemetry-java-instrumentation/releases/latest/download/opentelemetry-javaagent.jar).

This package includes the instrumentation agent as well as
instrumentations for all supported libraries and all available data exporters.
The package provides a completely automatic, out-of-the-box experience.

Enable the instrumentation agent using the `-javaagent` flag to the JVM.

```
java -javaagent:path/to/opentelemetry-javaagent.jar \
     -jar myapp.jar
```

By default, the OpenTelemetry Java agent uses the
[OTLP exporter](https://github.com/open-telemetry/opentelemetry-java/tree/main/exporters/otlp)
configured to send data to an
[OpenTelemetry collector](https://github.com/open-telemetry/opentelemetry-collector/blob/main/receiver/otlpreceiver/README.md)
at `http://localhost:4318`.

Configuration parameters are passed as Java system properties (`-D` flags) or
as environment variables. See [the configuration documentation][config-agent]
for the full list of configuration items. For exa
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `opentelemetry-proto.md`
```markdown
# 📦 open-telemetry/opentelemetry-proto [🔖 PENDING/APPROVE]
🔗 https://github.com/open-telemetry/opentelemetry-proto
🌐 https://opentelemetry.io/docs/specs/otlp/

## Meta
- **Stars:** ⭐ 768 | **Forks:** 🍴 305
- **Language:** Makefile | **License:** Apache-2.0
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
OpenTelemetry protocol (OTLP) specification and Protobuf definitions

## README (trích đầu)
```
# OpenTelemetry Protocol (OTLP) Specification

[![Build Check](https://github.com/open-telemetry/opentelemetry-proto/workflows/Build%20Check/badge.svg?branch=main)](https://github.com/open-telemetry/opentelemetry-proto/actions?query=workflow%3A%22Build+Check%22+branch%3Amain)

This repository contains the [OTLP protocol specification](../../../core/security/QUARANTINE/vetted/repos/claude_code_templates/cli_tool/components/agents/expert_advisors/specification.md)
and the corresponding Language Independent Interface Types ([.proto files](opentelemetry/proto)).

## Language Independent Interface Types

The proto files can be consumed as GIT submodules or copied and built directly in the consumer project.

The compiled files are published to central repositories (Maven, ...) from OpenTelemetry client libraries.

See [contribution guidelines](CONTRIBUTING.md) if you would like to make any changes.

## OTLP/JSON

See additional requirements for [OTLP/JSON wire representation here](https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/protocol/otlp.md#json-protobuf-encoding).

## Generate gRPC Client Libraries

To generate the raw gRPC client libraries, use `make gen-${LANGUAGE}`. Currently supported languages are:

* cpp
* csharp
* go
* java
* objc
* openapi (swagger)
* php
* python
* ruby

## Maturity Level

1.0.0 and newer releases from this repository may contain unstable (alpha or beta)
components as indicated by the Maturity table below.

| Component | Binary Protobuf Maturity | JSON Maturity |
| --------- | --------------- | ------------- |
| common/* | Stable | [Stable](../../../core/security/QUARANTINE/vetted/repos/claude_code_templates/cli_tool/components/agents/expert_advisors/specification.md#json-protobuf-encoding) |
| resource/* | Stable | [Stable](../../../core/security/QUARANTINE/vetted/repos/claude_code_templates/cli_tool/components/agents/expert_advisors/specification.md#json-protobuf-encoding) |
| metrics/\*<br>collector/metrics/* | Stable | [Stable](../../../core/security/QUARANTINE/vetted/repos/claude_code_templates/cli_tool/components/agents/expert_advisors/specification.md#json-protobuf-encoding) |
| trace/\*<br>collector/trace/* | Stable | [Stable](../../../core/security/QUARANTINE/vetted/repos/claude_code_templates/cli_tool/components/agents/expert_advisors/specification.md#json-protobuf-encoding) |
| logs/\*<br>collector/logs/* | Stable | [Stable](../../../core/security/QUARANTINE/vetted/repos/claude_code_templates/cli_tool/components/agents/expert_advisors/specification.md#json-protobuf-encoding) |
| profiles/\*<br>collector/profiles/* | Development | [Development](../../../core/security/QUARANTINE/vetted/repos/claude_code_templates/cli_tool/components/agents/expert_advisors/specification.md#json-protobuf-encoding) |

(See [Versioning and Stability](https://github.com/open-telemetry/opentelemetry-specification/blob/a08d1f92f62acd4aafe4dfaa04ae7bf28600d49e/specification/versioning-and-stability.md)
for definition of maturity levels).

## Stability Definition

Components marked `Stable` provide the following guarantees:

- Field types, numbers and names will not change.
- Service names and `service` package names will not change.
- Service method names will not change. [from 1.0.0]
- Service method parameter names will not change. [from 1.0.0]
- Service method parameter types and return types will not change. [from 1.0.0]
- Service method kind (unary vs streaming) will not change.
- Names of `message`s and `enum`s will not change. [from 1.0.0]
- Numbers assigned to `enum` choices will not change.
- Names of `enum` choices will not change. [from 1.0.0]
- The location of `message`s and `enum`s, i.e. whether they are declared at the t
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `opentelemetry-python.md`
```markdown
# 📦 open-telemetry/opentelemetry-python [🔖 PENDING/APPROVE]
🔗 https://github.com/open-telemetry/opentelemetry-python
🌐 https://opentelemetry.io

## Meta
- **Stars:** ⭐ 2369 | **Forks:** 🍴 826
- **Language:** Python | **License:** Apache-2.0
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
OpenTelemetry Python API and SDK 

## README (trích đầu)
```
# OpenTelemetry Python
[![Slack](https://img.shields.io/badge/slack-@cncf/otel/python-brightgreen.svg?logo=slack)](https://cloud-native.slack.com/archives/C01PD4HUVBL)
[![Build Status 0](https://github.com/open-telemetry/opentelemetry-python/actions/workflows/test_0.yml/badge.svg?branch=main)](https://github.com/open-telemetry/opentelemetry-python/actions/workflows/test_0.yml)
[![Build Status 1](https://github.com/open-telemetry/opentelemetry-python/actions/workflows/test_1.yml/badge.svg?branch=main)](https://github.com/open-telemetry/opentelemetry-python/actions/workflows/test_1.yml)
[![Minimum Python Version](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Release](https://img.shields.io/github/v/release/open-telemetry/opentelemetry-python?include_prereleases&style=)](https://github.com/open-telemetry/opentelemetry-python/releases/)
[![Read the Docs](https://readthedocs.org/projects/opentelemetry-python/badge/?version=latest)](https://opentelemetry-python.readthedocs.io/en/latest/)
[![OpenSSF Best Practices](https://www.bestpractices.dev/projects/11060/badge)](https://www.bestpractices.dev/projects/11060)

## Project Status

See the [OpenTelemetry Instrumentation for Python](https://opentelemetry.io/docs/instrumentation/python/#status-and-releases).

| Signal  | Status       | Project |
| ------- | ------------ | ------- |
| Traces  | Stable       | N/A     |
| Metrics | Stable       | N/A     |
| Logs    | Development* | N/A     |

Project versioning information and stability guarantees can be found [here](./rationale.md#versioning-and-releasing).

***Breaking Changes**

> [!IMPORTANT]
> We are working on stabilizing the Log signal which would require making deprecations and breaking changes. We will try to reduce the releases that may require an update to your code, especially for instrumentations or for SDK developers.

## Getting started

You can find the getting started guide for OpenTelemetry Python [here](https://opentelemetry.io/docs/instrumentation/python/getting-started/).

If you are looking for **examples** on how to use the OpenTelemetry API to
instrument your code manually, or how to set up the OpenTelemetry
Python SDK, see https://opentelemetry.io/docs/instrumentation/python/manual/.

## Python Version Support

This project ensures compatibility with the current supported versions of the Python. As new Python versions are released, support for them is added and
as old Python versions reach their end of life, support for them is removed.

We add support for new Python versions no later than 3 months after they become stable.

We remove support for old Python versions 6 months after they reach their [end of life](https://devguide.python.org/devcycle/#end-of-life-branches).


## Documentation

The online documentation is available at https://opentelemetry-python.readthedocs.io/.
To access the latest version of the documentation, see
https://opentelemetry-python.readthedocs.io/en/latest/.

##
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `opentelemetry-ruby.md`
```markdown
# 📦 open-telemetry/opentelemetry-ruby [🔖 PENDING/APPROVE]
🔗 https://github.com/open-telemetry/opentelemetry-ruby
🌐 https://opentelemetry.io/

## Meta
- **Stars:** ⭐ 566 | **Forks:** 🍴 283
- **Language:** Ruby | **License:** Apache-2.0
- **Last updated:** 2026-03-23
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
OpenTelemetry Ruby API & SDK, and related gems

## README (trích đầu)
```
# OpenTelemetry Ruby

[![Slack channel][slack-image]][slack-url]
[![CI][ci-image]][ci-image]
[![Apache License][license-image]][license-image]

The Ruby [OpenTelemetry](https://opentelemetry.io/) client.

- [Getting Started][getting-started]
- [Contributing](#contributing)
- [Contrib Repository](#contrib-repository)
- [Instrumentation Libraries][contrib-instrumentations]
- [Versioning](#versioning)
- [Useful links](#useful-links)
- [License](#license)

## Contributing

We'd love your help! Use tags [good first issue][issues-good-first-issue] and
[help wanted][issues-help-wanted] to get started with the project.

Please review the [contribution instructions](CONTRIBUTING.md) for important
information on setting up your environment, running the tests, and opening pull
requests.

The Ruby special interest group (SIG) meets regularly. See the OpenTelemetry
[community page][ruby-sig] repo for information on this and other language SIGs.

### Maintainers

- [Daniel Azuma](https://github.com/dazuma), Google
- [Francis Bogsanyi](https://github.com/fbogsany), Shopify
- [Kayla Reopelle](https://github.com/kaylareopelle), New Relic
- [Matthew Wear](https://github.com/mwear), Lightstep
- [Robert Laurin](https://github.com/robertlaurin), Shopify

For more information about the maintainer role, see the [community repository](https://github.com/open-telemetry/community/blob/main/guides/contributor/membership.md#maintainer).

### Approvers

- [Andrew Hayworth](https://github.com/ahayworth), Shopify
- [Ariel Valentin](https://github.com/arielvalentin), GitHub
- [Eric Mustin](https://github.com/ericmustin)
- [Robb Kidd](https://github.com/robbkidd), Honeycomb
- [Sam Handler](https://github.com/plantfansam), Shopify

For more information about the approver role, see the [community repository](https://github.com/open-telemetry/community/blob/main/guides/contributor/membership.md#approver).

## Contrib Repository

The [opentelemetry-ruby-contrib repository][contrib-repo] contains instrumentation libraries for many popular Ruby gems, including Rails, Rack, Sinatra, and others, so you can start using OpenTelemetry with minimal changes to your application. See the [contrib README][contrib-repo] for more details.

## Versioning

OpenTelemetry Ruby follows the [versioning and stability document][otel-versioning] in the OpenTelemetry specification. Notably, we adhere to the outlined version numbering exception, which states that experimental signals may have a `0.x` version number.

## Compatibility

OpenTelemetry Ruby ensures compatibility with the current supported versions of
the [Ruby language](https://www.ruby-lang.org/en/downloads/branches/).

## Useful links

- For more information on OpenTelemetry, visit: <https://opentelemetry.io/>
- For help or feedback on this project, join us in [GitHub Discussions][discussions-url].
- For more examples, check [SDK example][examples-github].

## License

Apache 2.0 - See [LICENSE][license-url] for more information.

[ci-image]:
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```


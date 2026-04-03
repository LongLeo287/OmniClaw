---
id: grafana-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:49.423399
---

# KNOWLEDGE EXTRACT: grafana
> **Extracted on:** 2026-03-30 17:38:02
> **Source:** grafana

---

## File: `alloy.md`
```markdown
# 📦 grafana/alloy [🔖 PENDING/APPROVE]
🔗 https://github.com/grafana/alloy
🌐 https://grafana.com/oss/alloy

## Meta
- **Stars:** ⭐ 3009 | **Forks:** 🍴 560
- **Language:** Go | **License:** Apache-2.0
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
OpenTelemetry Collector distribution with programmable pipelines

## README (trích đầu)
```
<p align="center">
    <img src="docs/sources/assets/logo_alloy_light.svg#gh-dark-mode-only" alt="Grafana Alloy logo" height="100px">
    <img src="docs/sources/assets/logo_alloy_dark.svg#gh-light-mode-only" alt="Grafana Alloy logo" height="100px">
</p>

<p align="center">
  <a href="https://github.com/grafana/alloy/releases"><img src="https://img.shields.io/github/release/grafana/alloy.svg" alt="Latest Release"></a>
  <a href="https://grafana.com/docs/alloy/latest"><img src="https://img.shields.io/badge/Documentation-link-blue?logo=gitbook" alt="Documentation link"></a>
</p>

Grafana Alloy is an open source OpenTelemetry Collector distribution with
built-in Prometheus pipelines and support for metrics, logs, traces, and
profiles.

<p>
<img src="docs/sources/assets/alloy_screenshot.png">
</p>

## What can Alloy do?

* **Programmable pipelines**: Use a rich [expression-based syntax][syntax] for
  configuring powerful observability pipelines.

* **OpenTelemetry Collector Distribution**: Alloy is a [distribution][] of
  OpenTelemetry Collector and supports dozens of its components, alongside new
  components that make use of Alloy's programmable pipelines.

* **Big tent**: Alloy embraces Grafana's "big tent" philosophy, where Alloy
  can be used with other vendors or open source databases. It has components
  to perfectly integrate with multiple telemetry ecosystems:

  * [OpenTelemetry Collector][]
  * [Prometheus][]
  * [Grafana Loki][]
  * [Grafana Pyroscope][]

* **Kubernetes-native**: Use components to interact with native and custom
  Kubernetes resources; no need to learn how to use a separate Kubernetes
  operator.

* **Shareable pipelines**: Use [modules][] to share your pipelines with the
  world.

* **Automatic workload distribution**: Configure Alloy instances to form a
  [cluster][] for automatic workload distribution.

* **Centralized configuration support**: Alloy supports retrieving its
  configuration from a [server][remotecfg] for centralized configuration
  management.

* **Debugging utilities**: Use the [built-in UI][ui] for visualizing and
  debugging pipelines.

[syntax]: https://grafana.com/docs/alloy/latest/concepts/configuration-syntax/
[distribution]: https://opentelemetry.io/docs/collector/distributions/
[OpenTelemetry Collector]: https://opentelemetry.io
[Prometheus]: https://prometheus.io
[Grafana Loki]: https://github.com/grafana/loki
[Grafana Pyroscope]: https://github.com/grafana/pyroscope
[modules]: https://grafana.com/docs/alloy/latest/concepts/modules/
[cluster]: https://grafana.com/docs/alloy/latest/concepts/clustering/
[remotecfg]: https://grafana.com/docs/alloy/latest/reference/config-blocks/remotecfg/
[ui]: https://grafana.com/docs/alloy/latest/tasks/debug/

## Example

```alloy
otelcol.receiver.otlp "example" {
  grpc {
    endpoint = "127.0.0.1:4317"
  }

  output {
    metrics = [otelcol.processor.batch.example.input]
    logs    = [otelcol.processor.batch.example.input]
    traces  = [otelcol.processor.batc
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `async-profiler.md`
```markdown
# 📦 grafana/async-profiler [🔖 PENDING/APPROVE]
🔗 https://github.com/grafana/async-profiler
🌐 https://github.com/jvm-profiling-tools/async-profiler/releases

## Meta
- **Stars:** ⭐ 5 | **Forks:** 🍴 2
- **Language:** C++ | **License:** Apache-2.0
- **Last updated:** 2026-02-20
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Sampling CPU and HEAP profiler for Java featuring AsyncGetCallTrace + perf_events

## README (trích đầu)
```
# Async-profiler

This project is a low overhead sampling profiler for Java
that does not suffer from the [Safepoint bias problem](http://psy-lob-saw.blogspot.ru/2016/02/why-most-sampling-java-profilers-are.html).
It features HotSpot-specific API to collect stack traces
and to track memory allocations. The profiler works with
OpenJDK and other Java runtimes based on the HotSpot JVM.

Unlike traditional Java profilers, async-profiler monitors non-Java threads
(e.g., GC and JIT compiler threads) and shows native and kernel frames in stack traces.

What can be profiled:

- CPU time
- Allocations in Java Heap
- Native memory allocations and leaks
- Contended locks
- Hardware and software performance counters like cache misses, page faults, context switches
- and [more](docs/ProfilingModes.md).

See our [3 hours playlist](https://www.youtube.com/playlist?list=PLNCLTEx3B8h4Yo_WvKWdLvI9mj1XpTKBr)
to learn about more features.

# Download

### Stable release: [4.2.1](https://github.com/async-profiler/async-profiler/releases/tag/v4.2.1)

- Linux x64: [async-profiler-4.2.1-linux-x64.tar.gz](https://github.com/async-profiler/async-profiler/releases/download/v4.2.1/async-profiler-4.2.1-linux-x64.tar.gz)
- Linux arm64: [async-profiler-4.2.1-linux-arm64.tar.gz](https://github.com/async-profiler/async-profiler/releases/download/v4.2.1/async-profiler-4.2.1-linux-arm64.tar.gz)
- macOS arm64/x64: [async-profiler-4.2.1-macos.zip](https://github.com/async-profiler/async-profiler/releases/download/v4.2.1/async-profiler-4.2.1-macos.zip)
- Profile converters: [jfr-converter.jar](https://github.com/async-profiler/async-profiler/releases/download/v4.2.1/jfr-converter.jar)

### Nightly builds

[The most recent binaries](https://github.com/async-profiler/async-profiler/releases/tag/nightly) corresponding
to the latest successful commit in `master`.

For a build corresponding to one of the previous commits, go to
[Nightly Builds](https://github.com/async-profiler/async-profiler/actions/workflows/test-and-publish-nightly.yml),
click the desired build and scroll down to the artifacts section. These binaries are kept for 30 days.

# Quick start

In a typical use case, profiling a Java application is just a matter of a running `asprof` with a PID of a
running Java process.

```
$ asprof -d 30 -f flamegraph.html <PID>
```

The above command translates to: run profiler for 30 seconds and save results to `flamegraph.html`
as an interactive [Flame Graph](docs/FlamegraphInterpretation.md) that can be viewed in a browser.

[![FlameGraph](/.assets/images/flamegraph.png)](https://htmlpreview.github.io/?https://github.com/async-profiler/async-profiler/blob/master/.assets/html/flamegraph.html)

Find more details in the [Getting started guide](docs/GettingStarted.md).

# Building

### Build status

[![Build Status](https://github.com/async-profiler/async-profiler/actions/workflows/test-and-publish-nightly.yml/badge.svg?branch=master)](https://github.com/async-profiler/async-profiler/actio
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `docker-otel-lgtm.md`
```markdown
# 📦 grafana/docker-otel-lgtm [🔖 PENDING/APPROVE]
🔗 https://github.com/grafana/docker-otel-lgtm


## Meta
- **Stars:** ⭐ 1709 | **Forks:** 🍴 188
- **Language:** Shell | **License:** Apache-2.0
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
OpenTelemetry backend in a Docker image

## README (trích đầu)
```
# docker-otel-lgtm

[![Docker latest][docker-latest]][docker-hub]
[![Docker pulls][docker-pulls]][docker-hub]

An OpenTelemetry backend in a Docker image. It bundles the **OpenTelemetry Collector**,
**Prometheus** (metrics), **Tempo** (traces), **Loki** (logs), **Pyroscope** (profiles),
and **Grafana** into a single container — with optional **OBI** (eBPF auto-instrumentation).

<!-- markdownlint-disable-next-line MD013 -->
![Overview of telemetry flow: applications, optionally auto-instrumented with OBI for traces and metrics, send telemetry to the OpenTelemetry Collector, which routes metrics to Prometheus, traces to Tempo, logs to Loki, and profiles to Pyroscope, with all signals visualized in Grafana](img/overview.png) <!-- editorconfig-checker-disable-line -->

The `grafana/otel-lgtm` Docker image is an open source backend for OpenTelemetry
that's intended for development, demo, and testing environments.

> [!IMPORTANT]
> If you are looking for a **production-ready**, out-of-the box solution to monitor applications
> and minimize MTTR (mean time to resolution) with OpenTelemetry and Prometheus,
> you should try [Grafana Cloud Application Observability][app-o11y].

## Documentation

- Blog posts:
  - [_An OpenTelemetry backend in a Docker image: Introducing grafana/otel-lgtm_][otel-lgtm]
  - [_Observability in under 5 seconds: Reflecting on a year of grafana/otel-lgtm_][otel-lgtm-one-year]

## Get the Docker image

The Docker image is available on [Docker Hub][docker-hub].

```sh
docker pull grafana/otel-lgtm:latest
```

## Run the Docker image

### Linux/Unix

```sh
./run-lgtm.sh
```

### Windows (PowerShell)

```powershell
./run-lgtm
```

### Linux/Unix Using mise

You can also use [mise][mise] to run the Docker image:

```sh
mise run lgtm
```

## Configuration

### Enable logging

You can enable logging in the .env file for troubleshooting:

| Environment Variable     | Enables Logging in:     |
|--------------------------|-------------------------|
| `ENABLE_LOGS_GRAFANA`    | Grafana                 |
| `ENABLE_LOGS_LOKI`       | Loki                    |
| `ENABLE_LOGS_PROMETHEUS` | Prometheus              |
| `ENABLE_LOGS_TEMPO`      | Tempo                   |
| `ENABLE_LOGS_PYROSCOPE`  | Pyroscope               |
| `ENABLE_LOGS_OTELCOL`    | OpenTelemetry Collector |
| `ENABLE_LOGS_OBI`        | OBI                     |
| `ENABLE_LOGS_ALL`        | All of the above        |

This has nothing to do with any application logs, which are collected by OpenTelemetry.

### Enable OBI (eBPF auto-instrumentation)

[OpenTelemetry eBPF Instrumentation (OBI)][obi] uses eBPF to automatically generate traces and
[RED][red-method] metrics for HTTP/gRPC services — with zero code changes.

To enable OBI, add `ENABLE_OBI=true` to your `.env` file or pass it as an
environment variable:

```sh
ENABLE_OBI=true ./run-lgtm.sh

# Using mise
mise run lgtm-obi
```

**Requirements:** Linux kernel 5.8+ with BTF support. The `run-lgtm.sh` and
`run-lgtm.ps1` scr
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `dskit.md`
```markdown
# 📦 grafana/dskit [🔖 PENDING/APPROVE]
🔗 https://github.com/grafana/dskit


## Meta
- **Stars:** ⭐ 562 | **Forks:** 🍴 77
- **Language:** Go | **License:** Apache-2.0
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Distributed systems kit

## README (trích đầu)
```
# Grafana Dskit

This library contains utilities that are useful for building distributed
services, including:
 - Exponential [backoff](https://github.com/grafana/dskit/tree/main/backoff) for retries.
 - A common [cache](https://github.com/grafana/dskit/tree/main/cache) API and Memcached implementation.
 - [Hedging](https://github.com/grafana/dskit/tree/main/hedging), sending extra duplicate requests to improve the chance that one succeeds.
 - A common [key-value](https://github.com/grafana/dskit/tree/main/kv) API, implemented for Consul, Etcd and Memberlist.
 - RPC [middlewares](https://github.com/grafana/dskit/tree/main/middleware), for metrics, logging, etc.
 - A [services model](https://github.com/grafana/dskit/tree/main/services), to manage start-up and shut-down.

## Current state

This library is used at scale in production at Grafana Labs.
A number of packages were collected here from database-related projects:

- [Mimir]
- [Loki]
- [Tempo]
- [Pyroscope]

[Mimir]: https://github.com/grafana/mimir
[Loki]: https://github.com/grafana/loki
[Tempo]: https://github.com/grafana/tempo
[Pyroscope]: https://github.com/grafana/pyroscope

## Go version compatibility

This library aims to support at least the two latest Go minor releases.

## Contributing

If you're interested in contributing to this project:

- Start by reading the [Contributing guide](../bmad_repo/CONTRIBUTING.md).
- Pull request titles must follow [Conventional Commits](https://www.conventionalcommits.org/) format.

## Release History

This project uses conventional commit messages to maintain a clear history of changes. No separate changelog is maintained - please refer to the [commit history](https://github.com/grafana/dskit/commits/main) for information about releases and changes.

## License

[Apache 2.0 License](https://github.com/grafana/dskit/blob/main/LICENSE)

```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `grafana-github-actions.md`
```markdown
# 📦 grafana/grafana-github-actions [🔖 PENDING/APPROVE]
🔗 https://github.com/grafana/grafana-github-actions


## Meta
- **Stars:** ⭐ 30 | **Forks:** 🍴 8
- **Language:** TypeScript | **License:** NOASSERTION
- **Last updated:** 2026-03-25
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Github automation 

## README (trích đầu)
```
Github action commands for automating issue management.

Based on work from: https://github.com/microsoft/vscode-github-triage-actions


## Commands

Type: `label`

- `action`: defines what action to perform (`close` or `addToProject`)
- `name`: defines which label to match on
- `addToProject`: an object that is required when the `action` is `addToProject`, but is otherwise optional.
- `addToProject.url`: Absolute url of the project where the project `id` will be parsed.
- `addToProject.column`: Column name to add the issues to. Required for old types of projects
- `removeFromProject`: an object that is required when the `action` is `removeFromProject`, but is otherwise optional.
- `removeFromProject.url`: Absolute url of the project where the project `id` will be parsed.

Note: When removed, the issue will irreversibly lose the project-specific metadata assigned to it. removeFromProject does not currently work for old project types.

**Syntax**:
```json
{
  "type": "label",
  "name": "plugins",
  "action": "addToProject",
  "addToProject": {
    "url": "https://github.com/orgs/grafana/projects/76",
    "column": "To Do"
  }
}
```

## PR Checks

Mark commits with an error, failure, pending, or success state, which is then reflected in pull requests involving those commits.

**Syntax**:
```json
[
  {
    "type": "<check>"
    // check specific properties
  }
]
```

### Milestone Check

This will check if a milestone is set on a pull request or not. All properties below except `type` are optional.

**Syntax**:
```json
{
  "type": "check-milestone",
  "title": "Milestone Check",
  "targetUrl": "https://something",
  "success": "Milestone set",
  "failure": "Milestone not set"
}
```

### Label Check

This will check if `labels.matches` matches any labels on a pull request.
- If it matches, it will create a success status with a `labels.exists` message.
- If it does not match it will create a failure status with a `labels.notExists` message.

If `skip.matches` is specified, it will check if any of the labels exist on a pull request and if so, it will create a success status with a `skip.message` message. This will happen before returning a failure status according to the documentation above.

All properties below except `type` and `labels.matches` are optional. The `labels.matches` and `skip.matches` support providing a `*` (star) at the end to denote only matching the beginning of a label.

```json
{
  "type": "check-label",
  "title": "New Label Backport Check",
  "labels": {
    "exists": "Backport enabled",
    "notExists": "Backport decision needed",
    "matches": [
      "backport v*"
    ]
  },
  "skip": {
    "message": "Backport skipped",
    "matches": [
      "backport",
      "no-backport"
    ]
  },
  "targetUrl": "https://github.com/grafana/grafana/blob/main/contribute/merge-pull-request.md#should-the-pull-request-be-backported"
}
```

### Changelog Check

This check will enforce that an active decision of including a change in changelo
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `jfr-parser.md`
```markdown
# 📦 grafana/jfr-parser [🔖 PENDING/APPROVE]
🔗 https://github.com/grafana/jfr-parser


## Meta
- **Stars:** ⭐ 47 | **Forks:** 🍴 18
- **Language:** Go | **License:** Apache-2.0
- **Last updated:** 2026-03-07
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Java Flight Recorder parser library written in Go.

## README (trích đầu)
```
# Java Flight Recorder parser library written in Go.

The parser design is generic, and it should be able to support any kind of type and event.

Current implementation is incomplete, with a focus in supporting the types and events generated
by [async-profiler](https://github.com/jvm-profiling-tools/async-profiler).

## References

- [JEP 328](https://openjdk.java.net/jeps/328) introduces Java Flight Recorder.
- [async-profiler](https://github.com/jvm-profiling-tools/async-profiler) supports includes
  a [JFR writer](https://github.com/jvm-profiling-tools/async-profiler/blob/master/src/flightRecorder.cpp)
  and [reader](https://github.com/jvm-profiling-tools/async-profiler/tree/master/src/converter/one/jfr).
- [JMC](https://github.com/openjdk/jmc) project includes its
  own [JFR parser](https://github.com/openjdk/jmc/tree/master/core/org.openjdk.jmc.flightrecorder/src/main/java/org/openjdk/jmc/flightrecorder/parser) (
  in Java).
- [The JDK Flight Recorder File Format](https://www.morling.dev/blog/jdk-flight-recorder-file-format/)
  by [@gunnarmorling](https://github.com/gunnarmorling) has a great overview of the JFR format.

```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `jsonnet-libs.md`
```markdown
# 📦 grafana/jsonnet-libs [🔖 PENDING/APPROVE]
🔗 https://github.com/grafana/jsonnet-libs


## Meta
- **Stars:** ⭐ 725 | **Forks:** 🍴 181
- **Language:** Jsonnet | **License:** NOASSERTION
- **Last updated:** 2026-03-25
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Grafana Labs' Jsonnet libraries

## README (trích đầu)
```
# Grafana Labs' Jsonnet libraries

This repository contains various Jsonnet libraries we use at Grafana Labs:

* [`prometheus-ksonnet`](prometheus-ksonnet/): A set of extensible configurations
  for running Prometheus on Kubernetes.
* [`grafana-builder`](grafana-builder/): A library for building Grafana dashboards
  with jsonnet, following the builder pattern.
* [`ksonnet-util`](ksonnet-util/): An overlay and set of utilities aiming at making working with Kubernetes easier.
* [`oauth2-proxy`](oauth2-proxy/): A jsonnet configuration for deploying bitly's
  OAuth proxy to Kubernetes.

## Monitoring mixins

Based on format described [here](https://monitoring.mixins.dev/):

* [`consul-mixin`](consul-mixin/): A set of reuseable and extensible dashboards
  and alerts for running Hashicorp's Consul.

* [`memcached-mixin`](memcached-mixin/): A set of reuseable and extensible dashboards
  for Memcached.

* [`nodejs-mixin`](nodejs-mixin/): A set of reuseable and extensible dashboards
  for Node.js.

* [`caddy-mixin`](caddy-mixin/): A set of reusable and extensible dashboards
  for Caddy.

* [`jira-mixin`](jira-mixin/): A set of reusable and extensible dashboards and alerts for JIRA.

You can find more in directories with `-mixin` suffix.

### Linting

The monitoring mixins in this repository use two linting tools to ensure quality and consistency:

* [mixtool](https://github.com/monitoring-mixins/mixtool): Validates the structure and syntax of monitoring mixins, ensuring they follow the standard mixin format.
* [pint](https://github.com/cloudflare/pint): Lints Prometheus rules and alerts to catch common mistakes and enforce best practices.

## Observability libraries

Observability library is a flexible format to describe dashboards and alerts in a modular way so libraries can be imported into one another or into monitoring-mixins. Observability libraries can be found in folders with `-observ-lib` suffix. [Common library](https://github.com/grafana/jsonnet-libs/tree/master/common-lib) is also used to apply consistent style options.

### Observability libraries signal extention

[Signal](https://github.com/grafana/jsonnet-libs/tree/master/common-lib/common/signal#signal) is the experimental extension to observability libraries format to declare metrics (signals) and then render them as different grafana panel types (timeseries, stat, table, etc), or alert rules.

Examples:
 - [docker-mixin](docker-mixin/)
 - [kafka-observ-lib](kafka-observ-lib/)
 - [jvm-observ-lib](jvm-observ-lib/)
 - [snmp-observ-lib](snmp-observ-lib/)
 - [process-observ-lib](process-observ-lib/)
 - [golang-observ-lib](golang-observ-lib/)
 - [csp-mixin](csp-mixin/)
 - [windows-observ-lib](windows-observ-lib/)

## Prometheus rules testing for monitoring mixins and observability libraries

It is highly recommended to test prometheus alerts with [promtool test rules](https://prometheus.io/docs/prometheus/latest/configuration/unit_testing_rules) command when complex PromQL queries are used or 
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `k8s-monitoring-helm.md`
```markdown
# 📦 grafana/k8s-monitoring-helm [🔖 PENDING/APPROVE]
🔗 https://github.com/grafana/k8s-monitoring-helm


## Meta
- **Stars:** ⭐ 620 | **Forks:** 🍴 207
- **Language:** Go Template | **License:** Apache-2.0
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
(No description)

## README (trích đầu)
```
# Kubernetes Monitoring Helm Charts

<div align="center">

[![Grafana](https://img.shields.io/badge/grafana-%23F46800.svg?logo=grafana&logoColor=white)](https://grafana.com)
[![Artifact Hub](https://img.shields.io/endpoint?url=https://artifacthub.io/badge/repository/grafana)](https://artifacthub.io/packages/search?org=grafana)
[![Helm Chart](https://img.shields.io/badge/helm-k8s--monitoring-blue?logo=helm)](https://img.shields.io/endpoint?url=https://artifacthub.io/packages/helm/grafana/k8s-monitoring)
![GitHub Release](https://img.shields.io/github/v/release/grafana/k8s-monitoring-helm)
![GitHub Release Date](https://img.shields.io/github/release-date/grafana/k8s-monitoring-helm)

[![Unit Tests](https://github.com/grafana/k8s-monitoring-helm/actions/workflows/unit-test.yml/badge.svg?branch=main)](https://github.com/grafana/k8s-monitoring-helm/actions/workflows/unit-test.yml?query=branch%3Amain)
[![Integration Tests](https://github.com/grafana/k8s-monitoring-helm/actions/workflows/integration-test.yml/badge.svg?branch=main)](https://github.com/grafana/k8s-monitoring-helm/actions/workflows/integration-test.yml?query=branch%3Amain)
[![Platform Tests](https://github.com/grafana/k8s-monitoring-helm/actions/workflows/platform-test.yml/badge.svg?branch=main)](https://github.com/grafana/k8s-monitoring-helm/actions/workflows/platform-test.yml?query=branch%3Amain)
![GitHub License](https://img.shields.io/github/license/grafana/k8s-monitoring-helm)

</div>

## Maintainers

| Name     | Email                         | URL |
|----------|-------------------------------|-----|
| petewall | <pete.wall@grafana.com>       |     |
| rlankfo  | <robert.lankford@grafana.com> |     |

## Usage

[Helm](https://helm.sh/) must be installed to use the chart. Please refer to
Helm's [documentation](https://helm.sh/docs/) to get started.

After Helm is set up properly, add the repository as follows:

```console
helm repo add grafana https://grafana.github.io/helm-charts
```

Refer to the [Chart Documentation](https://grafana.com/docs/grafana-cloud/monitor-infrastructure/kubernetes-monitoring/configuration/helm-chart-config/helm-chart/)
to learn more, including about chart installation instructions.

## Office Hours

We hold office hours on the 4th Friday of the month. Meeting times and recordings will be posted here:

| Date       | Topic                                         | Link                                          |
|------------|-----------------------------------------------|-----------------------------------------------|
| 2026-03-27 | TBD                                           | [Zoom](https://grafana.zoom.us/j/96633896206) |
| 2026-02-27 | 3.8 Release and 4.0 preview                   | [Recording](https://youtu.be/OquS3vMaGNE)     |
| 2026-01-23 | 3.7 Release                                   | [Recording](https://youtu.be/VyqreBQuVtM)     |
| 2025-12-12 | 3.6 Release                                   | [Recording](https://youtu.be/T-EaHzJ1Qbs)     |
| 
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `otel-profiling-go.md`
```markdown
# 📦 grafana/otel-profiling-go [🔖 PENDING/APPROVE]
🔗 https://github.com/grafana/otel-profiling-go
🌐 https://pyroscope.io

## Meta
- **Stars:** ⭐ 100 | **Forks:** 🍴 4
- **Language:** Go | **License:** Apache-2.0
- **Last updated:** 2025-12-15
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Open Telemetry integration for Grafana Pyroscope and tracing solutions such as Grafana Tempo, Honeycomb, or Jaeger

## README (trích đầu)
```
# Profiling Instrumentation for OpenTelemetry Go SDK

**NOTE**: This is an experimental package -- and will be officially supported in future versions of Pyroscope

The package provides means to integrate tracing with profiling. More specifically, a `TracerProvider` implementation,
that annotates profiling data with span IDs: when a new trace span emerges, the tracer adds a `span_id` [pprof tag](https://github.com/google/pprof/blob/master/doc/README.md#tag-filtering)
that points to the span. This makes it possible to filter out a profile of a particular trace span in [Pyroscope](https://pyroscope.io).

Note that the module does not control `pprof` profiler itself – it still needs to be started for profiles to be
collected. This can be done either via `runtime/pprof` package, or using the [Pyroscope client](https://github.com/grafana/pyroscope-go).

By default, only the root span gets labeled (the first span created locally): such spans are marked with the
`pyroscope.profile.id` attribute set to the span ID. Please note that presence of the attribute does not necessarily
indicate that the span has a profile: stack trace samples might not be collected, if the utilized CPU time is
less than the sample interval (10ms).

Limitations:
- Only CPU profiling is fully supported at the moment.

### Trace spans profiles

To start profiling trace spans, you need to include our go module in your app:

```
go get github.com/grafana/otel-profiling-go
```

Then add the pyroscope tracer provider:

```go
package main

import (
	otelpyroscope "github.com/grafana/otel-profiling-go"
	"github.com/grafana/pyroscope-go"
)

func main() {
	// Initialize your tracer provider as usual.
	tp := initTracer()

	// Wrap it with otelpyroscope tracer provider.
	otel.SetTracerProvider(otelpyroscope.NewTracerProvider(tp))

	// If you're using Pyroscope Go SDK, initialize pyroscope profiler.
	_, _ = pyroscope.Start(pyroscope.Config{
		ApplicationName: "my-service",
		ServerAddress:   "http://localhost:4040",
	})

	// Your code goes here.
}
```

Tracing integration is supported in pull mode as well: if you scrape profiles using Grafana Agent, you should
make sure that the pyroscope `service_name` label matches `service.name` attribute specified in the OTel SDK configuration.
Please refer to the [Grafana Agent](https://grafana.com/docs/pyroscope/latest/configure-client/grafana-agent/go_pull/)
documentation to learn more.

## Example

You can find a complete example setup with Grafana Tempo in the [Pyroscope repository](https://github.com/grafana/pyroscope/tree/main/examples/tracing/golang-push).

![image](https://github.com/grafana/otel-profiling-go/assets/12090599/31e33cd1-818b-4116-b952-c9ec7b1fb593)

```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `otel-profiling-java.md`
```markdown
# 📦 grafana/otel-profiling-java [🔖 PENDING/APPROVE]
🔗 https://github.com/grafana/otel-profiling-java


## Meta
- **Stars:** ⭐ 47 | **Forks:** 🍴 10
- **Language:** Go | **License:** Apache-2.0
- **Last updated:** 2026-03-25
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
otel profling integration for java

## README (trích đầu)
```
## Java OpenTelemetry tracing integration

Pyroscope can integrate with distributed tracing systems supporting [**OpenTelemetry**](https://opentelemetry.io/docs/instrumentation/java/getting-started/) standard which allows you to
link traces with the profiling data, and find specific lines of code related to a performance issue.


* Because of how sampling profilers work, spans shorter than the sample interval may not be captured. By default pyroscope CPU profiler probes stack traces 100 times per second, meaning that spans shorter than 10ms may not be captured.


Java code can be easily instrumented with otel-profiling-java package -
a `OpenTelemetry` implementation, that annotates profiling data with span IDs which makes it possible to filter
out profile of a particular trace span in Pyroscope.

Visit [docs](https://grafana.com/docs/pyroscope/latest/configure-client/trace-span-profiles/java-span-profiles/) page for usage and configuration documentation.

## Examples

Check out the [examples](https://github.com/grafana/pyroscope/tree/main/examples/tracing/tempo) directory in our repository to
find a complete example application that demonstrates tracing integration features and learn more 🔥

```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `otel-profiling-ruby.md`
```markdown
# 📦 grafana/otel-profiling-ruby [🔖 PENDING/APPROVE]
🔗 https://github.com/grafana/otel-profiling-ruby


## Meta
- **Stars:** ⭐ 9 | **Forks:** 🍴 4
- **Language:** Ruby | **License:** MIT
- **Last updated:** 2025-09-10
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
repo for otel profiling ruby integrations 

## README (trích đầu)
```
# Pyroscope::Otel

Pyroscope can integrate with distributed tracing systems supporting OpenTelemetry standard which allows you to link traces with the profiling data, and find specific lines of code related to a performance issue.

For full documentation, refer to our [docs](https://grafana.com/docs/pyroscope/latest/configure-client/trace-span-profiles/ruby-span-profiles/).

## Installation

Add this line to your application's Gemfile:

```ruby
gem 'pyroscope-otel'
```

And then execute:

    $ bundle install

Or install it yourself as:

    $ gem install pyroscope-otel

## Usage

```ruby
Pyroscope.configure do |config|
  # Configure pyroscope as described https://pyroscope.io/docs/ruby/
end

OpenTelemetry::SDK.configure do |config|
  config.add_span_processor Pyroscope::Otel::SpanProcessor.new(
    "#{app_name}.cpu", # your app name with ".cpu" suffix, for example rideshare-ruby.cpu
    pyroscope_endpoint # link to your pyroscope server, for example "http://localhost:4040"
  )
  # Configure the rest of opentelemetry as described  https://github.com/open-telemetry/opentelemetry-ruby
end
```

## License

The gem is available as open source under the terms of the [MIT License](https://opensource.org/licenses/MIT).

```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `pyroscope-dotnet.md`
```markdown
# 📦 grafana/pyroscope-dotnet [🔖 PENDING/APPROVE]
🔗 https://github.com/grafana/pyroscope-dotnet


## Meta
- **Stars:** ⭐ 35 | **Forks:** 🍴 11
- **Language:** C++ | **License:** Apache-2.0
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Dotnet profiler

## README (trích đầu)
```
(Không lấy được README)
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `pyroscope-go.md`
```markdown
# 📦 grafana/pyroscope-go [🔖 PENDING/APPROVE]
🔗 https://github.com/grafana/pyroscope-go


## Meta
- **Stars:** ⭐ 162 | **Forks:** 🍴 27
- **Language:** Go | **License:** Apache-2.0
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
This is the golang client integration for Pyroscope

## README (trích đầu)
```
# Pyroscope Golang Client

This is a golang integration for Pyroscope — open source continuous profiling platform.

For more information, please visit our [golang integration documentation](https://grafana.com/docs/pyroscope/latest/configure-client/language-sdks/go_push/).

## Profiling Go applications

To start profiling a Go application, you need to include our Go module in your app:

```
go get github.com/grafana/pyroscope-go
```

Then add the following code to your application:

```go
package main

import "github.com/grafana/pyroscope-go"

func main() {
  pyroscope.Start(pyroscope.Config{
    ApplicationName: "simple.golang.app",

    // replace this with the address of pyroscope server
    ServerAddress:   "http://pyroscope-server:4040",

    // you can disable logging by setting this to nil
    Logger:          pyroscope.StandardLogger,

    // Optional HTTP Basic authentication (Grafana Cloud)
    BasicAuthUser:     "<User>",
    BasicAuthPASSWORD='[REDACTED_PASSWORD]',
    // Optional Pyroscope tenant ID (only needed if using multi-tenancy). Not needed for Grafana Cloud.
    // TenantID:          "<TenantID>",

    // by default all profilers are enabled,
    // but you can select the ones you want to use:
    ProfileTypes: []pyroscope.ProfileType{
      pyroscope.ProfileCPU,
      pyroscope.ProfileAllocObjects,
      pyroscope.ProfileAllocSpace,
      pyroscope.ProfileInuseObjects,
      pyroscope.ProfileInuseSpace,
    },
  })

  // your code goes here
}
```

### Tags

It is possible to add tags (labels) to the profiling data. These tags can be used to filter the data in the UI.

```go
// these two ways of adding tags are equivalent:
pyroscope.TagWrapper(context.Background(), pyroscope.Labels("controller", "slow_controller"), func(c context.Context) {
  slowCode()
})

pprof.Do(context.Background(), pprof.Labels("controller", "slow_controller"), func(c context.Context) {
  slowCode()
})
```

### Pull Mode

Go integration supports pull mode, which means that you can profile applications without adding any extra code. For that to work you will need to make sure you have profiling routes (`/debug/pprof`) enabled in your http server. Generally, that means that you need to add `net/http/pprof` package:

```go
import _ "net/http/pprof"
```

## Examples

Check out the [examples](https://github.com/grafana/pyroscope-go/tree/main/example) directory in our repository to learn more. 🔥

## Maintainers

This package is maintained by [@grafana/pyroscope-go](https://github.com/orgs/grafana/teams/pyroscope-go). Mention this team on issues or PRs for feedback.

```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `pyroscope-java.md`
```markdown
# 📦 grafana/pyroscope-java [🔖 PENDING/APPROVE]
🔗 https://github.com/grafana/pyroscope-java


## Meta
- **Stars:** ⭐ 115 | **Forks:** 🍴 43
- **Language:** Java | **License:** Apache-2.0
- **Last updated:** 2026-03-24
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
pyroscope java integration

## README (trích đầu)
```
# Pyroscope Java agent

The Java profiling agent for Pyroscope.io. Based
on [async-profiler](https://github.com/jvm-profiling-tools/async-profiler).

## Distribution

The agent is distributed as a single JAR file `pyroscope.jar`. It contains native async-profiler libraries for:

- Linux on x64;
- Linux on ARM64;
- MacOS on x64.
- MacOS on ARM64.

## Windows OS support

It also contains support for Windows OS, through JFR profiler. In order to use JFR as profiler in place of
async-profiler,
you need to configure profiler type, either through configuration file or environment variable.

By setting `PYROSCOPE_PROFILER_TYPE` configuration variable to `JFR`, agent will use JVM built-in profiler.

## Downloads

Visit [releases](https://github.com/pyroscope-io/pyroscope-java/releases) page to download the latest version
of `pyroscope.jar`

## Usage

Visit [docs](https://pyroscope.io/docs/java/) page for usage and configuration documentation.

## Building

If you want to build the agent JAR yourself, from this repo run:

```shell
./gradlew shadowJar
```

The file will be in `agent/build/libs/pyroscope.jar`.

## Maintainers

This package is maintained by [@grafana/pyroscope-java](https://github.com/orgs/grafana/teams/pyroscope-java).
Mention this team on issues or PRs for feedback.

```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `pyroscope-lambda-extension.md`
```markdown
# 📦 grafana/pyroscope-lambda-extension [🔖 PENDING/APPROVE]
🔗 https://github.com/grafana/pyroscope-lambda-extension
🌐 https://grafana.com/docs/pyroscope/latest/configure-client/aws-lambda

## Meta
- **Stars:** ⭐ 8 | **Forks:** 🍴 4
- **Language:** Go | **License:** Apache-2.0
- **Last updated:** 2025-10-27
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Pyroscope AWS Lambda Extension

## README (trích đầu)
```
# pyroscope-lambda-extension

# Usage
Add `pyroscope-lambda-extension` to your lambda
In your lambda, add the pyroscope client. For example, the go one

```go
func main() {
	pyroscope.Start(pyroscope.Config{
		ApplicationName: "simple.golang.lambda",
		ServerAddress:   "http://localhost:4040",
	})

	lambda.Start(HandleRequest)
}
```
Keep in mind it needs to be setup BEFORE the handler setup.
Also the `ServerAddress` **MUST** be `http://localhost:4040`, which is the address of the relay server.

Then set up the `PYROSCOPE_REMOTE_ADDRESS` environment variable.
If needed, the `PYROSCOPE_AUTH_TOKEN` can be supplied.

For a complete list of variables check the section below.

## Configuration
| env var                         | default                          | description                                                                                  |
|---------------------------------|----------------------------------|----------------------------------------------------------------------------------------------|
| `PYROSCOPE_REMOTE_ADDRESS`      | `https://ingest.pyroscope.cloud` | the pyroscope instance data will be relayed to                                               |
| `PYROSCOPE_AUTH_TOKEN`          | `""`                             | authorization key (token authentication)                                                     |
| `PYROSCOPE_SELF_PROFILING`      | `false`                          | whether to profile the extension itself or not                                               |
| `PYROSCOPE_LOG_LEVEL`           | `info`                           | `error` or `info` or `debug` or `trace`                                                      |
| `PYROSCOPE_TIMEOUT`             | `10s`                            | http client timeout ([go duration format](https://pkg.go.dev/time#Duration))                 |
| `PYROSCOPE_NUM_WORKERS`         | `5`                              | num of relay workers, pick based on the number of profile types                              |
| `PYROSCOPE_FLUSH_ON_INVOKE`     | `false`                          | wait for all relay requests to be finished/flushed before next `Invocation` event is allowed |
| `PYROSCOPE_HTTP_HEADERS`        | `{}`                             | extra http headers in json format, for example: {"X-Header": "Value"}                        |
| `PYROSCOPE_TENANT_ID`           | `""`                             | phlare tenant ID, passed as X-Scope-OrgID http header                                      |
| `PYROSCOPE_BASIC_AUTH_USER`     | `""` | HTTP basic auth user |
| `PYROSCOPE_BASIC_AUTH_PASSWORD` | `""`  | HTTP basic auth password  |
| `PYROSCOPE_LOG_FORMAT`                  | `"text"`         | format to choose from from `"text"` and `"json"`                                        |
| `PYROSCOPE_LOG_TIMESTAMP_FORMAT`        | `time.RFC3339`   | logging timestamp format ([go time format](https://golang.org/pkg/time/#pkg-constants)) |
| `PYROSCOPE_LOG_TIMESTAMP_DISABLE`
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `pyroscope-rs.md`
```markdown
# 📦 grafana/pyroscope-rs [🔖 PENDING/APPROVE]
🔗 https://github.com/grafana/pyroscope-rs


## Meta
- **Stars:** ⭐ 209 | **Forks:** 🍴 47
- **Language:** Rust | **License:** Apache-2.0
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Pyroscope Profiler for Rust. Profile your Rust applications.

## README (trích đầu)
```
## Pyroscope Profiler

**Pyroscope Profiler for Rust. Profile your Rust applications.**

[![license](https://img.shields.io/badge/license-Apache2.0-blue.svg)](LICENSE) 
[![Crate](https://img.shields.io/crates/v/pyroscope.svg)](https://crates.io/crates/pyroscope)


### Major Contributors

We'd like to give a big thank you to the following contributors who have made significant contributions to this project:

* [Abid Omar](https://github.com/omarabid)
* [Anatoly Korniltsev](https://github.com/korniltsev)
* [Bernhard Schuster](https://github.com/drahnr)


### License

Pyroscope is distributed under the Apache License (Version 2.0).

See [LICENSE](LICENSE) for details.

```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `pyroscope.md`
```markdown
# 📦 grafana/pyroscope [🔖 PENDING/APPROVE]
🔗 https://github.com/grafana/pyroscope
🌐 https://grafana.com/oss/pyroscope/

## Meta
- **Stars:** ⭐ 11314 | **Forks:** 🍴 735
- **Language:** Go | **License:** AGPL-3.0
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Continuous Profiling Platform. Debug performance issues down to a single line of code

## README (trích đầu)
```
<p align="center"><img alt="Pyroscope" src="https://github.com/grafana/pyroscope/assets/662636/c1fc4055-b33d-4e69-a450-9e7a7b2317bb" width="100%"/></p>


[![ci](https://github.com/grafana/pyroscope/actions/workflows/test.yml/badge.svg)](https://github.com/grafana/pyroscope/actions/workflows/test.yml)
[![JS Tests Status](https://github.com/grafana/pyroscope/workflows/JS%20Tests/badge.svg)](https://github.com/grafana/pyroscope/actions?query=workflow%3AJS%20Tests)
[![Go Report](https://goreportcard.com/badge/github.com/grafana/pyroscope)](https://goreportcard.com/report/github.com/grafana/pyroscope)
[![License: AGPLv3](https://img.shields.io/badge/License-AGPL%20v3-blue.svg)](LICENSE)
[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2Fgrafana%2Fpyroscope.svg?type=shield)](https://app.fossa.com/projects/git%2Bgithub.com%2Fgrafana%2Fpyroscope?ref=badge_shield)
[![Latest release](https://img.shields.io/github/release/grafana/pyroscope.svg)](https://github.com/grafana/pyroscope/releases)
[![DockerHub](https://img.shields.io/docker/pulls/grafana/pyroscope.svg)](https://hub.docker.com/r/grafana/pyroscope)
[![GoDoc](https://godoc.org/github.com/grafana/pyroscope?status.svg)](https://godoc.org/github.com/grafana/pyroscope)

## 🎉 **Announcement: The new Explore Profiles UI is here!**

We are thrilled to announce the launch of the **Explore Profiles UI**, a brand-new way to explore and analyze your profiling data—now available as part of the Grafana Explore Apps suite! This new app brings you a **queryless**, **intuitive** experience for visualizing your profiling data, simplifying the entire process without the need to write complex queries.

https://github.com/user-attachments/assets/4db19ec7-86f3-4701-8f5f-9b7ffcebd49c

## What is Grafana Pyroscope?

Grafana Pyroscope is a continuous profiling platform designed to surface performance insights from your applications, helping you optimize resource usage such as CPU, memory, and I/O operations. With Pyroscope, you can both **proactively** and **reactively** address performance bottlenecks across your system.

The typical use cases are:

- **Proactive:** Reducing resource consumption, improving application performance, or preventing latency issues.
- **Reactive:** Quickly resolving incidents with line-level detail and debugging active CPU, memory, or I/O bottlenecks.

Pyroscope provides powerful tools to give you a comprehensive view of your application's behavior while allowing you to drill down into specific services for more targeted root cause analysis.

## How Does Pyroscope Work?

![deployment_diagram](https://grafana.com/media/docs/pyroscope/pyroscope_client_server_diagram_09_18_2024.png)

Pyroscope consists of three main components:
- **Pyroscope Server:** The server component that stores and processes profiling data.
- **Pyroscope SDKs(push) or Grafana alloy(pull) :** The client-side part of Pyroscope that collects profiling data from your applications and sends it to the server.
-
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `shared-workflows.md`
```markdown
# 📦 grafana/shared-workflows [🔖 PENDING/APPROVE]
🔗 https://github.com/grafana/shared-workflows


## Meta
- **Stars:** ⭐ 22 | **Forks:** 🍴 34
- **Language:** Go | **License:** AGPL-3.0
- **Last updated:** 2026-03-24
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
A public-facing, centralized place to store reusable workflows used by Grafana Labs.

## README (trích đầu)
```
# shared-workflows

[![OpenSSF Scorecard][scorecard image]][scorecard]

A public-facing, centralized place to store reusable GitHub workflows and action
used by Grafana Labs. See the `actions/` directory for the individual actions
themselves.

[scorecard]: https://scorecard.dev/viewer/?uri=github.com/grafana/shared-workflows
[scorecard image]: https://api.scorecard.dev/projects/github.com/grafana/shared-workflows/badge

## Custom Renovate config

This is a monorepo containing several Actions. When we release a workflow, we create a tag `<workflow name>/v<workflow version>`.

While Dependabot can update references to these actions, Renovate can't do it out of the box. It can, however, be configured to do so:

```json
{
  "packageRules": [
    {
      "matchPackageNames": ["grafana/shared-workflows"],
      "versioning": "regex:^(?<compatibility>.*)[-/]v?(?<major>\\d+)\\.(?<minor>\\d+)\\.(?<patch>\\d+)?$",
      "additionalBranchPrefix": "{{ lookup (split newVersion \"/\") 0 }}-",
      "commitMessagePrefix": "chore(deps):",
      "commitMessageAction": "update",
      "commitMessageTopic": "{{depName}}/{{ lookup (split newVersion \"/\") 0 }} action",
      "commitMessageExtra": "to {{ lookup (split newVersion \"/\") 1 }}"
    }
  ]
}
```

## Notes

### Configure your IDE to run Prettier

[Prettier] will run in CI to ensure that files are formatted correctly. To ensure
that your code is formatted correctly before you commit, set up your IDE to run
Prettier on save.

Or from the commandline, you can run Prettier using [`npx`][npx]:

```sh
npx prettier --check .
```

Or, of course, install it in any other way you want.

[npx]: https://www.npmjs.com/package/npx
[prettier]: https://prettier.io/

### Pin versions

When referencing third-party actions, [always pin the version to a specific
commit hash][hardening]. This ensures that the workflow will always use the same
version of the action, even if the action's maintainers release a new version or
if the tag itself is updated.

Dependabot can update these SHA references when there are new versions. If you
include a tag in a commend after the SHA, it can update the comment too. For
example:

```yaml
- uses: action/foo@abcdef0123456789abcdef0123456789 # foo-action/v1.2.3
```

[hardening]: https://docs.github.com/en/actions/security-guides/security-hardening-for-github-actions#using-third-party-actions

### Refer to other `shared-workflows` actions using relative paths

When referencing other actions in this repository, use a relative path. This
will ensure actions in this repo are always used at the same commit. To do this:

```yaml
- name: Checkout
  env:
    # In a composite action, these two need to be indirected via the
    # environment, as per the GitHub actions documentation:
    # https://docs.github.com/en/actions/learn-github-actions/contexts
    action_repo: ${{ github.action_repository }}
    action_ref: ${{ github.action_ref }}
  uses: actions/checkout@b4ffde65f46336ab88eb53be808477a3936bae11
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```


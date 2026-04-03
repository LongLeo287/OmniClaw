---
id: github.com-grafana-docker-otel-lgtm-7295f18d-knowl
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:20:04.218066
---

# KNOWLEDGE EXTRACT: github.com_grafana_docker-otel-lgtm_7295f18d
> **Extracted on:** 2026-04-01 16:41:15
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007525230/github.com_grafana_docker-otel-lgtm_7295f18d

---

## File: `.codespellrc`
```
[codespell]
ignore-words-list = atMost,equest
```

## File: `.editorconfig`
```
root = true

[*]
max_line_length = 100
indent_size = 2

[*Dockerfile*]
end_of_line = lf
max_line_length = 200

[*.cs]
indent_size = 4
insert_final_newline = true
end_of_line = crlf
max_line_length = 180

[*.md]
max_line_length = 120

[renovate.json5]
max_line_length = 400

[{*.sh,.gitignore,go.work.sum,mise.toml,*.yml,*.yaml,pom.xml,*.cmd,maven-wrapper.properties,go.sum,package-lock.json,README.md}]
max_line_length = 150

[{grafana-dashboard-jvm-metrics.json,grafana-dashboard-red-metrics-classic.json,grafana-dashboard-red-metrics-native.json,.editorconfig,custom-dashboard.json}]
max_line_length = 3000

[*.py]
# checked by black
indent_size = 4
```

## File: `.gitattributes`
```
* text=auto
mvnw eol=lf
*.sh eol=lf
*.cs eol=crlf
Dockerfile eol=lf
```

## File: `.gitignore`
```
.idea/
venv/
.venv
/container/grafana/*
/container/loki/*
/container/prometheus/*
.lycheecache
*.iml
.env
opentelemetry-javaagent*.jar
grafana-opentelemetry*.jar
build/
obj/
examples/go/dice
```

## File: `.golangci.yaml`
```yaml
#linters:
#  disable: metalinter

run:
  timeout: 1m
```

## File: `.markdownlint.yaml`
```yaml
# Default state for all rules
default: true

# allow long lines for tables and code blocks
MD013:
  code_blocks: false
  tables: false
  line_length: 120

MD024:
  siblings_only: true
```

## File: `.prettierignore`
```
**/*.md
```

## File: `.yaml-lint.yml`
```yaml
---
extends: relaxed
```

## File: `AGENTS.md`
```markdown
# AGENTS.md

This file provides guidance to AI coding agents when working with code in this repository.

## Project Overview

docker-otel-lgtm is an all-in-one OpenTelemetry backend Docker image for
development, demo, and testing. It bundles Grafana, Prometheus, Tempo, Loki,
Pyroscope, and OpenTelemetry Collector into a single container.

## Build & Run Commands

All development tasks use [mise](https://github.com/jdx/mise) as the task
runner. Tool versions (Go, Java, Rust, lychee) are pinned in `mise.toml`.

```bash
# Build Docker image (tag defaults to "latest")
mise run build-lgtm dev1

# Run Docker image
mise run lgtm dev1

# Run locally built image
mise run local-lgtm
```

The build script (`build-lgtm.sh`) auto-detects Docker or Podman.

## Testing

Acceptance tests use [OATS](https://github.com/grafana/oats) (OpenTelemetry
Acceptance Tests). Most examples have an `oats.yaml` that validates traces
(TraceQL), metrics (PromQL), and logs (LogQL).

```bash
# Run all acceptance tests
mise run acceptance-tests

# Run a single example's tests (build first)
mise run build-lgtm dev1
oats -timeout 2h -lgtm-version dev1 examples/nodejs
```

## Linting

```bash
# Auto-fix and verify (recommended dev workflow)
mise run fix

# Verify only (same command used in CI)
mise run lint
```

After running `fix`, always review the changed files before committing —
auto-fixes may produce unexpected results.

Go code uses `.golangci.yaml` config. Markdown uses `.markdownlint.yaml`.
EditorConfig rules in `.editorconfig`.

### Renovate Tracked Deps Linter

`mise run lint` verifies that `.github/renovate-tracked-deps.json` stays in
sync with what Renovate actually tracks. If the snapshot is stale, run
`mise run fix` and commit the result. The lint tasks are provided by
[flint](https://github.com/grafana/flint).

## Architecture

### Docker Image (docker/)

The Dockerfile is a multi-stage build on `redhat/ubi9`. The builder stage
downloads each component via individual `download-*.sh` scripts, using cosign
verification for the OpenTelemetry Collector and SHA256 checksum verification
for other components. Each component has a `run-*.sh` startup script.
`run-all.sh` is the container entrypoint that starts all services.

### Example Applications (examples/)

Language-specific demo apps that emit OpenTelemetry data:
- `examples/java` (port 8080) - Maven + OTel Java Agent
- `examples/go` (port 8081) - Go workspace (`go.work` at repository root)
- `examples/python` (port 8082) - Python + auto-instrumentation
- `examples/dotnet` (port 8083) - .NET/C#
- `examples/nodejs` (port 8084) - Node.js

Most examples have a `docker-compose.oats.yml`, a `run.sh` script, and an
`oats.yaml` for acceptance tests.

### Key Ports

| Service    | Port |
|------------|------|
| Grafana    | 3000 |
| OTLP gRPC  | 4317 |
| OTLP HTTP  | 4318 |
| Pyroscope  | 4040 |
| Prometheus | 9090 |

### OTel Collector Configuration

The collector config is split across `docker/otelcol-config.yaml` (base) and
`docker/otelcol-config-export-http.yaml` (external export). To test the merged
config (run inside the container where the binary is at
`/otel-lgtm/otelcol-contrib/otelcol-contrib`):

```bash
/otel-lgtm/otelcol-contrib/otelcol-contrib \
  --config docker/otelcol-config.yaml \
  --config docker/otelcol-config-export-http.yaml \
  print-initial-config \
  --feature-gates otelcol.printInitialConfig > merged.yaml
```

## Component Versions

All component versions are declared as `ARG` directives in `docker/Dockerfile`
with Renovate annotations for automated dependency updates. Version bumps are
made there, not elsewhere.

## Release Process

Releases are automated weekly (Friday 09:00 UTC) via GitHub Actions if
`docker/` has changed. Version auto-increments based on component changes.
Releases are immutable once published.
```

## File: `CLAUDE.md`
```markdown
<!-- markdownlint-disable-file -->

@AGENTS.md
```

## File: `CODEOWNERS`
```
# https://help.github.com/articles/about-codeowners/
# https://git-scm.com/docs/gitignore#_pattern_format

* @grafana/otel-sdk
```

## File: `CONTRIBUTING.md`
```markdown
# Contributing

It's recommended to use the [mise][mise] for development.

## Building locally

`dev1` is an example of a tag to test locally.

- `mise run build-lgtm dev1` will build the Docker image locally.
- `mise run lgtm dev1` will run the Docker image locally.

## Linting

This repository uses [flint][flint] for linting.
See the flint readme for detailed documentation on each linter.

```bash
mise run fix   # Auto-fix all issues (recommended before committing)
mise run lint  # Check only (same command used in CI)
```

Always run `mise run fix` before committing — review the changed files as auto-fixes may produce unexpected results.

## Acceptance Tests

Acceptance test cases are defined in `oats.yaml` files in the examples directory.
The test cases are run by [oats].

If a test case fails (let's say `examples/nodejs`), follow these steps:

1. Build a new image: `mise run build-lgtm dev1`
2. `oats -timeout 2h -lgtm-version dev1 examples/nodejs` (automatically installed by `mise`)
3. go to <http://127.0.0.1:3000>

You can run all everything together using `mise run test`.

## Architecture diagram

> [!NOTE]
> The architecture diagram is only accessible to Grafana employees.

The source code for the architecture diagram is a [Google slide][architecture].
Take a screenshot of the slide and save it as `img/overview.png`.

## OTel Collector

### Testing the combined configuration

```shell
./otelcol-contrib --config docker/otelcol-config.yaml --config docker/otelcol-export-http.yaml \
print-initial-config --feature-gates otelcol.printInitialConfig > merged.yaml
```

<!-- editorconfig-checker-disable -->
<!-- markdownlint-disable MD013 -->

[architecture]: https://docs.google.com/presentation/d/1txMBBitezscvtJIXRHNSXnCekjMRM29GmHufUSI0NRw/edit?slide=id.g26040f0db78_0_0#slide=id.g26040f0db78_0_0
[flint]: https://github.com/grafana/flint
[mise]: https://github.com/jdx/mise
[oats]: https://github.com/grafana/oats
```

## File: `LICENSE`
```
                                 Apache License
                           Version 2.0, January 2004
                        http://www.apache.org/licenses/

   TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

   1. Definitions.

      "License" shall mean the terms and conditions for use, reproduction,
      and distribution as defined by Sections 1 through 9 of this document.

      "Licensor" shall mean the copyright owner or entity authorized by
      the copyright owner that is granting the License.

      "Legal Entity" shall mean the union of the acting entity and all
      other entities that control, are controlled by, or are under common
      control with that entity. For the purposes of this definition,
      "control" means (i) the power, direct or indirect, to cause the
      direction or management of such entity, whether by contract or
      otherwise, or (ii) ownership of fifty percent (50%) or more of the
      outstanding shares, or (iii) beneficial ownership of such entity.

      "You" (or "Your") shall mean an individual or Legal Entity
      exercising permissions granted by this License.

      "Source" form shall mean the preferred form for making modifications,
      including but not limited to software source code, documentation
      source, and configuration files.

      "Object" form shall mean any form resulting from mechanical
      transformation or translation of a Source form, including but
      not limited to compiled object code, generated documentation,
      and conversions to other media types.

      "Work" shall mean the work of authorship, whether in Source or
      Object form, made available under the License, as indicated by a
      copyright notice that is included in or attached to the work
      (an example is provided in the Appendix below).

      "Derivative Works" shall mean any work, whether in Source or Object
      form, that is based on (or derived from) the Work and for which the
      editorial revisions, annotations, elaborations, or other modifications
      represent, as a whole, an original work of authorship. For the purposes
      of this License, Derivative Works shall not include works that remain
      separable from, or merely link (or bind by name) to the interfaces of,
      the Work and Derivative Works thereof.

      "Contribution" shall mean any work of authorship, including
      the original version of the Work and any modifications or additions
      to that Work or Derivative Works thereof, that is intentionally
      submitted to Licensor for inclusion in the Work by the copyright owner
      or by an individual or Legal Entity authorized to submit on behalf of
      the copyright owner. For the purposes of this definition, "submitted"
      means any form of electronic, verbal, or written communication sent
      to the Licensor or its representatives, including but not limited to
      communication on electronic mailing lists, source code control systems,
      and issue tracking systems that are managed by, or on behalf of, the
      Licensor for the purpose of discussing and improving the Work, but
      excluding communication that is conspicuously marked or otherwise
      designated in writing by the copyright owner as "Not a Contribution."

      "Contributor" shall mean Licensor and any individual or Legal Entity
      on behalf of whom a Contribution has been received by Licensor and
      subsequently incorporated within the Work.

   2. Grant of Copyright License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      copyright license to reproduce, prepare Derivative Works of,
      publicly display, publicly perform, sublicense, and distribute the
      Work and such Derivative Works in Source or Object form.

   3. Grant of Patent License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      (except as stated in this section) patent license to make, have made,
      use, offer to sell, sell, import, and otherwise transfer the Work,
      where such license applies only to those patent claims licensable
      by such Contributor that are necessarily infringed by their
      Contribution(s) alone or by combination of their Contribution(s)
      with the Work to which such Contribution(s) was submitted. If You
      institute patent litigation against any entity (including a
      cross-claim or counterclaim in a lawsuit) alleging that the Work
      or a Contribution incorporated within the Work constitutes direct
      or contributory patent infringement, then any patent licenses
      granted to You under this License for that Work shall terminate
      as of the date such litigation is filed.

   4. Redistribution. You may reproduce and distribute copies of the
      Work or Derivative Works thereof in any medium, with or without
      modifications, and in Source or Object form, provided that You
      meet the following conditions:

      (a) You must give any other recipients of the Work or
          Derivative Works a copy of this License; and

      (b) You must cause any modified files to carry prominent notices
          stating that You changed the files; and

      (c) You must retain, in the Source form of any Derivative Works
          that You distribute, all copyright, patent, trademark, and
          attribution notices from the Source form of the Work,
          excluding those notices that do not pertain to any part of
          the Derivative Works; and

      (d) If the Work includes a "NOTICE" text file as part of its
          distribution, then any Derivative Works that You distribute must
          include a readable copy of the attribution notices contained
          within such NOTICE file, excluding those notices that do not
          pertain to any part of the Derivative Works, in at least one
          of the following places: within a NOTICE text file distributed
          as part of the Derivative Works; within the Source form or
          documentation, if provided along with the Derivative Works; or,
          within a display generated by the Derivative Works, if and
          wherever such third-party notices normally appear. The contents
          of the NOTICE file are for informational purposes only and
          do not modify the License. You may add Your own attribution
          notices within Derivative Works that You distribute, alongside
          or as an addendum to the NOTICE text from the Work, provided
          that such additional attribution notices cannot be construed
          as modifying the License.

      You may add Your own copyright statement to Your modifications and
      may provide additional or different license terms and conditions
      for use, reproduction, or distribution of Your modifications, or
      for any such Derivative Works as a whole, provided Your use,
      reproduction, and distribution of the Work otherwise complies with
      the conditions stated in this License.

   5. Submission of Contributions. Unless You explicitly state otherwise,
      any Contribution intentionally submitted for inclusion in the Work
      by You to the Licensor shall be under the terms and conditions of
      this License, without any additional terms or conditions.
      Notwithstanding the above, nothing herein shall supersede or modify
      the terms of any separate license agreement you may have executed
      with Licensor regarding such Contributions.

   6. Trademarks. This License does not grant permission to use the trade
      names, trademarks, service marks, or product names of the Licensor,
      except as required for reasonable and customary use in describing the
      origin of the Work and reproducing the content of the NOTICE file.

   7. Disclaimer of Warranty. Unless required by applicable law or
      agreed to in writing, Licensor provides the Work (and each
      Contributor provides its Contributions) on an "AS IS" BASIS,
      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
      implied, including, without limitation, any warranties or conditions
      of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
      PARTICULAR PURPOSE. You are solely responsible for determining the
      appropriateness of using or redistributing the Work and assume any
      risks associated with Your exercise of permissions under this License.

   8. Limitation of Liability. In no event and under no legal theory,
      whether in tort (including negligence), contract, or otherwise,
      unless required by applicable law (such as deliberate and grossly
      negligent acts) or agreed to in writing, shall any Contributor be
      liable to You for damages, including any direct, indirect, special,
      incidental, or consequential damages of any character arising as a
      result of this License or out of the use or inability to use the
      Work (including but not limited to damages for loss of goodwill,
      work stoppage, computer failure or malfunction, or any and all
      other commercial damages or losses), even if such Contributor
      has been advised of the possibility of such damages.

   9. Accepting Warranty or Additional Liability. While redistributing
      the Work or Derivative Works thereof, You may choose to offer,
      and charge a fee for, acceptance of support, warranty, indemnity,
      or other liability obligations and/or rights consistent with this
      License. However, in accepting such obligations, You may act only
      on Your own behalf and on Your sole responsibility, not on behalf
      of any other Contributor, and only if You agree to indemnify,
      defend, and hold each Contributor harmless for any liability
      incurred by, or claims asserted against, such Contributor by reason
      of your accepting any such warranty or additional liability.

   END OF TERMS AND CONDITIONS

   APPENDIX: How to apply the Apache License to your work.

      To apply the Apache License to your work, attach the following
      boilerplate notice, with the fields enclosed by brackets "[]"
      replaced with your own identifying information. (Don't include
      the brackets!)  The text should be enclosed in the appropriate
      comment syntax for the file format. We also recommend that a
      file or class name and description of purpose be included on the
      same "printed page" as the copyright notice for easier
      identification within third-party archives.

   Copyright [yyyy] [name of copyright owner]

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
```

## File: `README.md`
```markdown
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
`run-lgtm.ps1` scripts automatically add the required `--pid=host` and
`--privileged` Docker flags when OBI is enabled. If you run `docker run`
directly, you must add these flags manually.

> [!NOTE]
> The `--pid=host` flag shares the host's PID namespace with the container,
> so OBI can discover and instrument processes running on the host — not just
> inside the container. For example, `OBI_TARGET=java` will instrument Java
> processes running on the host as well.

#### Target specific applications

By default, OBI discovers services on common ports (80, 443, 8080-8099,
3000-3999, 5000-5999). You can target specific applications:

```sh
# Monitor all Java processes
ENABLE_OBI=true OBI_TARGET=java ./run-lgtm.sh

# Monitor all Python processes
ENABLE_OBI=true OBI_TARGET=python ./run-lgtm.sh

# Monitor a specific executable by name
ENABLE_OBI=true OBI_TARGET=myapp ./run-lgtm.sh

# Monitor specific ports
ENABLE_OBI=true OTEL_EBPF_OPEN_PORT=8080,9090 ./run-lgtm.sh
```

<!-- editorconfig-checker-disable -->

| Variable                    | Purpose                                                                                         |
|-----------------------------|-------------------------------------------------------------------------------------------------|
| `OBI_TARGET`                | Friendly language target: `java`, `python`, `node`, `dotnet`, `ruby`, or any regular expression |
| `OTEL_EBPF_OPEN_PORT`       | Override ports to monitor (native OBI environment variable)                                     |
| `OTEL_EBPF_AUTO_TARGET_EXE` | Executable name pattern (native OBI environment variable, set automatically by `OBI_TARGET`)    |

<!-- editorconfig-checker-enable -->

### Send data to vendors

In addition to the built-in observability tools, you can also send data to vendors.
That way, you can easily try and switch between different backends.

If the [`OTEL_EXPORTER_OTLP_ENDPOINT`][otlp-endpoint]
variable is set, the OpenTelemetry Collector will send data (logs, metrics, and traces)
to the specified endpoint using "OTLP/HTTP".

You can also configure per-signal endpoints:

* `OTEL_EXPORTER_OTLP_LOGS_ENDPOINT`
* `OTEL_EXPORTER_OTLP_METRICS_ENDPOINT`
* `OTEL_EXPORTER_OTLP_TRACES_ENDPOINT`

If both global and per-signal endpoints are set, per-signal values take precedence.
Endpoints must include the scheme (for example, `http://jaeger:4318`).

In addition, you can provide [`OTEL_EXPORTER_OTLP_HEADERS`][otlp-headers],
for example, to authenticate with the backend.

#### Send data to Grafana Cloud

You can find the values for the environment variables in your [Grafana Cloud account][otel-setup].

### Persist data across container instantiation

The various components in the repository are configured to write their data to the `/data`
directory. If you need to persist data across containers being created and destroyed,
you can mount a volume to the `/data` directory. Note that this image is intended for
development, demo, and testing environments and persisting data to an external volume
doesn't change that. However, this feature could be useful in certain cases for
some users even in testing situations.

### Customize backend configuration

Each backend supports a `*_EXTRA_ARGS` environment variable for passing additional
CLI flags without modifying any files:

| Backend                 | Env var                 | Example                              |
|-------------------------|-------------------------|--------------------------------------|
| Prometheus              | `PROMETHEUS_EXTRA_ARGS` | `--storage.tsdb.retention.time=90d`  |
| Loki                    | `LOKI_EXTRA_ARGS`       | `--limits.retention-period=90d`      |
| Tempo                   | `TEMPO_EXTRA_ARGS`      |                                      |
| Pyroscope               | `PYROSCOPE_EXTRA_ARGS`  |                                      |
| OpenTelemetry Collector | `OTELCOL_EXTRA_ARGS`    |                                      |

For example, to set a 90-day retention period for Prometheus:

```sh
docker run -e PROMETHEUS_EXTRA_ARGS="--storage.tsdb.retention.time=90d" grafana/otel-lgtm
```

> [!NOTE]
> The value is split on whitespace into separate arguments. For options that
> require values with spaces, mount a custom configuration file instead (see below).

For deeper customization, you can mount custom configuration files into the container:

| Backend                 | Config file path                            |
|-------------------------|---------------------------------------------|
| Prometheus              | `/otel-lgtm/prometheus.yaml`                |
| Loki                    | `/otel-lgtm/loki-config.yaml`               |
| Tempo                   | `/otel-lgtm/tempo-config.yaml`              |
| Pyroscope               | `/otel-lgtm/pyroscope-config.yaml`          |
| OpenTelemetry Collector | `/otel-lgtm/otelcol-config.yaml`            |

```sh
docker run -v ./my-loki-config.yaml:/otel-lgtm/loki-config.yaml:ro grafana/otel-lgtm
```

Grafana is configured via `GF_*` environment variables — see the
[Grafana documentation][grafana-env-overrides] for details.

### Pre-install Grafana plugins

You can pre-install Grafana plugins by adding them to the `GF_PLUGINS_PREINSTALL` environment variable.
See the [Grafana documentation][grafana-preinstall-plugins] for more information.

### Add custom dashboards

You can add custom Grafana dashboards by mounting them into the container with a provisioning configuration.

Create a dashboard JSON file and a provisioning YAML file:

**dashboards-provisioning.yaml:**

```yaml
apiVersion: 1

providers:
  - name: "Custom Dashboards"
    type: file
    options:
      path: /otel-lgtm/grafana/conf/provisioning/dashboards/custom
      foldersFromFilesStructure: false
```

Mount both files in your `docker-compose.yml`:

```yaml
services:
  lgtm:
    image: grafana/otel-lgtm
    volumes:
      - ./custom-dashboard.json:/otel-lgtm/grafana/conf/provisioning/dashboards/custom/custom-dashboard.json:ro
      - ./dashboards-provisioning.yaml:/otel-lgtm/grafana/conf/provisioning/dashboards/custom.yaml:ro
```

See the [Java example][java-example] for a complete working example.

To set a custom dashboard as the home dashboard, add the `GF_DASHBOARDS_DEFAULT_HOME_DASHBOARD_PATH`
environment variable:

```yaml
services:
  lgtm:
    image: grafana/otel-lgtm
    environment:
      GF_DASHBOARDS_DEFAULT_HOME_DASHBOARD_PATH: /otel-lgtm/grafana/conf/provisioning/dashboards/custom/custom-dashboard.json
```

## Run lgtm in Kubernetes

```sh
# Create k8s resources
kubectl apply -f k8s/lgtm.yaml

# Configure port forwarding
kubectl port-forward service/lgtm 3000:3000 4040:4040 4317:4317 4318:4318 9090:9090

# Using mise
mise k8s-apply
mise k8s-port-forward
```

## Send OpenTelemetry Data

There's no need to configure anything: the Docker image works with OpenTelemetry's defaults.

```sh
# Not needed, but these are the defaults in OpenTelemetry
export OTEL_EXPORTER_OTLP_PROTOCOL=http/protobuf
export OTEL_EXPORTER_OTLP_ENDPOINT=http://127.0.0.1:4318
```

## View Grafana

Navigate to <http://127.0.0.1:3000> and log in with the default built-in user `admin` and password `admin`.

## Build the Docker image from scratch

```sh
cd docker/
docker build . -t grafana/otel-lgtm

# Using mise
mise build-lgtm
```

> [!TIP]
> If you built your image locally, you can use the `run-lgtm` scripts with
> the parameters `latest true` to run your local image (or `mise run local-lgtm`).

## Build and run the example app

> [!TIP]
> You can run everything together using [mise][mise] with `mise run all`.

### Run

Run the example REST service:

#### Unix/Linux

```sh
./run-example.sh
```

#### Windows (PowerShell)

```powershell
./run-example
```

#### Unix/Linux Using mise

```sh
mise run example
```

### Generate traffic

#### Unix/Linux

```sh
./generate-traffic.sh
```

#### Windows (PowerShell)

```powershell
./generate-traffic
```

#### Unix/Linux Using mise

```sh
mise run generate-traffic
```

> [!TIP]
> You can use [OTel Checker][otel-checker] to check if the instrumentation is correct.

## Run example apps in different languages

The example apps are in the [`examples/`][examples] directory.
Each example has a `run.sh` or `run.cmd` script to start the app.

Every example implements a rolldice service, which returns a random number between 1 and 6.

Each example uses a different application port
(to be able to run all applications at the same time).

| Example | Service URL                           |
|---------|---------------------------------------|
| Java    | `curl http://127.0.0.1:8080/rolldice` |
| Go      | `curl http://127.0.0.1:8081/rolldice` |
| Python  | `curl http://127.0.0.1:8082/rolldice` |
| .NET    | `curl http://127.0.0.1:8083/rolldice` |
| Node.js | `curl http://127.0.0.1:8084/rolldice` |

## Verifying Container Image Signatures

The container images that are published are signed using [cosign][cosign]. You
can verify the signatures using a command similar to the following example:

```sh
VERSION="0.11.16"
IMAGE="docker.io/grafana/otel-lgtm:${VERSION}"
IDENTITY="https://github.com/grafana/docker-otel-lgtm/.github/workflows/release.yml@refs/tags/v${VERSION}"
OIDC_ISSUER="https://token.actions.githubusercontent.com"

cosign verify ${IMAGE} --certificate-identity ${IDENTITY} --certificate-oidc-issuer ${OIDC_ISSUER}
```

It is also possible to verify the signatures of images from our continuous integration
that are published to the [GitHub Container Registry][ghcr]. For example for the `main` branch:

```sh
VERSION="main"
IMAGE="ghcr.io/grafana/docker-otel-lgtm:${VERSION}"
WORKFLOW="ghcr-image-build-and-publish.yml"
IDENTITY="https://github.com/grafana/docker-otel-lgtm/.github/workflows/${WORKFLOW}@refs/heads/${VERSION}"
OIDC_ISSUER="https://token.actions.githubusercontent.com"

cosign verify ${IMAGE} --certificate-identity ${IDENTITY} --certificate-oidc-issuer ${OIDC_ISSUER}
```

## Related Work

- [Metrics, Logs, Traces and Profiles in Grafana][mltp]
- [OpenTelemetry Acceptance Tests (OATs)][oats]

<!-- editorconfig-checker-disable -->
<!-- markdownlint-disable MD013 -->

[app-o11y]: https://grafana.com/products/cloud/application-observability/
[obi]: https://opentelemetry.io/docs/zero-code/obi/ "OpenTelemetry eBPF Instrumentation"
[cosign]: https://github.com/sigstore/cosign "Cosign on GitHub"
[docker-hub]: https://hub.docker.com/r/grafana/otel-lgtm
[docker-latest]: https://img.shields.io/docker/v/grafana/otel-lgtm?logo=docker&label=latest&color=blue
[docker-pulls]: https://img.shields.io/docker/pulls/grafana/otel-lgtm?logo=docker&label=pulls
[examples]: examples/
[ghcr]: https://github.com/grafana/docker-otel-lgtm/pkgs/container/docker-otel-lgtm
[grafana-env-overrides]: https://grafana.com/docs/grafana/latest/setup-grafana/configure-grafana/#override-configuration-with-environment-variables
[grafana-preinstall-plugins]: https://grafana.com/docs/grafana/latest/setup-grafana/configure-docker/#install-plugins-in-the-docker-container
[java-example]: examples/java/
[mise]: https://github.com/jdx/mise
[mltp]: https://github.com/grafana/intro-to-mltp
[otel-checker]: https://github.com/grafana/otel-checker/
[otel-lgtm]: https://grafana.com/blog/2024/03/13/an-opentelemetry-backend-in-a-docker-image-introducing-grafana-otel-lgtm
[otel-lgtm-one-year]: https://grafana.com/blog/2025/07/08/observability-in-under-5-seconds-reflecting-on-a-year-of-grafana-otel-lgtm/
[otel-setup]: https://grafana.com/docs/grafana-cloud/send-data/otlp/send-data-otlp/#manual-opentelemetry-setup-for-advanced-users
[otlp-endpoint]: https://opentelemetry.io/docs/languages/sdk-configuration/otlp-exporter/#otel_exporter_otlp_endpoint
[otlp-headers]: https://opentelemetry.io/docs/languages/sdk-configuration/otlp-exporter/#otel_exporter_otlp_headers
[oats]: https://github.com/grafana/oats
[red-method]: https://grafana.com/blog/the-red-method-how-to-instrument-your-services/ "The RED Method"
```

## File: `RELEASING.md`
```markdown
# Releasing

> [!IMPORTANT]
> Releases are [immutable][immutable-releases] and cannot be changed or their associated tag
> deleted once published.
>
> However, the description can still be edited to fix any mistakes or omissions after publishing.

## Scheduled Releases

Releases are automatically published on a weekly basis via a
[scheduled GitHub Actions workflow][scheduled-release]. The workflow runs every Friday at 09:00 UTC
and will publish a new release if any changes have been made in the [`docker/` directory][docker]
since the [latest release][latest-release].

The version will be auto-incremented to the next minor or patch version based on the changes to
the installed components in the container image, if any.

## Manual Releases

1. Open the [Publish Release workflow][publish-release]
2. Click on the **Run workflow** button
3. If required, enter a specific version number (e.g. `x.y.z`) in the version field. If left
   blank, the version will be auto-incremented to the next minor or patch version based on the
   changes to the installed components in the container image since the [latest release][latest-release].
4. Wait for the workflow to complete successfully.
5. Click the link in the workflow run summary to the untagged release created by the workflow.
6. Click the edit button (pencil icon) at the top right of the release notes.
7. Verify that the release notes are correct. Make any manual adjustments if necessary.
8. Click on **Publish release**.

<!-- editorconfig-checker-disable -->
<!-- markdownlint-disable MD013 -->

[docker]: ./docker
[immutable-releases]: https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/immutable-releases
[latest-release]: https://github.com/grafana/docker-otel-lgtm/releases/latest
[publish-release]: https://github.com/grafana/docker-otel-lgtm/actions/workflows/publish-release.yml
[scheduled-release]: .github/workflows/scheduled-release.yml
```

## File: `build-lgtm.cmd`
```
@echo off

SET release_tag=latest
if not "%~1"=="" (
	SET release_tag=%1
)

echo Building the Grafana OTEL-LGTM image with release %release_tag%...

WHERE /Q podman
if not ERRORLEVEL 1 (
	goto use_podman
)

WHERE /Q docker
if not ERRORLEVEL 1 (
	goto use_docker
)

:no_executable_found
echo Please install Podman or docker
goto:EOF

:use_podman
podman buildx build -f docker/Dockerfile docker --tag grafana/otel-lgtm:%release_tag% --build-arg LGTM_VERSION=%release_tag%
goto:EOF

:use_docker
docker buildx build -f docker/Dockerfile docker --tag grafana/otel-lgtm:%release_tag% --build-arg LGTM_VERSION=%release_tag%
goto:EOF
```

## File: `build-lgtm.sh`
```bash
#!/bin/bash

set -euo pipefail

RELEASE=${1:-latest}
CONTAINER_RUNTIME_OVERRIDE=${2:-}

echo "Building the Grafana OTEL-LGTM image with release ${RELEASE}..."

if [ -n "$CONTAINER_RUNTIME_OVERRIDE" ]; then
	case "$CONTAINER_RUNTIME_OVERRIDE" in
	docker | podman) RUNTIME="$CONTAINER_RUNTIME_OVERRIDE" ;;
	*)
		echo "Invalid runtime: $CONTAINER_RUNTIME_OVERRIDE (must be docker or podman)"
		exit 1
		;;
	esac
elif command -v podman >/dev/null 2>&1; then
	RUNTIME=podman
elif command -v docker >/dev/null 2>&1; then
	RUNTIME=docker
else
	echo "Unable to find a suitable container runtime such as Docker or Podman. Exiting."
	exit 1
fi

if [ "$RUNTIME" = "podman" ]; then
	TAG="localhost/grafana/otel-lgtm:${RELEASE}"
else
	TAG="grafana/otel-lgtm:${RELEASE}"
fi

"$RUNTIME" buildx build -f docker/Dockerfile docker --tag "${TAG}" --build-arg LGTM_VERSION="${RELEASE}"

# Ensure the image is also available without localhost/ prefix (for tools like oats)
if [ "$RUNTIME" = "podman" ]; then
	"$RUNTIME" tag "${TAG}" "grafana/otel-lgtm:${RELEASE}"
fi
```

## File: `generate-traffic.cmd`
```
@ECHO OFF
:loop
	cls
	curl -s http://127.0.0.1:8080/rolldice
	curl -s http://127.0.0.1:8081/rolldice
	curl -s http://127.0.0.1:8082/rolldice
	curl -s http://127.0.0.1:8083/rolldice
	curl -s http://127.0.0.1:8084/rolldice
	timeout /t 2
goto loop
```

## File: `generate-traffic.sh`
```bash
#!/bin/bash

watch 'curl -s http://127.0.0.1:8080/rolldice; \
  curl -s http://127.0.0.1:8081/rolldice; \
  curl -s http://127.0.0.1:8082/rolldice; \
  curl -s http://127.0.0.1:8083/rolldice; \
  curl -s http://127.0.0.1:8084/rolldice?rolls=5'
```

## File: `go.work`
```
go 1.25.0

use (
	./examples/go
	./examples/obi/go
)
```

## File: `go.work.sum`
```
cel.dev/expr v0.16.2 h1:RwRhoH17VhAu9U5CMvMhH1PDVgf0tuz9FT+24AfMLfU=
cel.dev/expr v0.16.2/go.mod h1:gXngZQMkWJoSbE8mOzehJlXQyubn/Vg0vR9/F3W7iw8=
cel.dev/expr v0.19.1 h1:NciYrtDRIR0lNCnH1LFJegdjspNx9fI59O7TWcua/W4=
cel.dev/expr v0.19.1/go.mod h1:MrpN08Q+lEBs+bGYdLxxHkZoUSsCp0nSKTs0nTymJgw=
cel.dev/expr v0.20.0 h1:OunBvVCfvpWlt4dN7zg3FM6TDkzOePe1+foGJ9AXeeI=
cel.dev/expr v0.20.0/go.mod h1:MrpN08Q+lEBs+bGYdLxxHkZoUSsCp0nSKTs0nTymJgw=
cel.dev/expr v0.24.0 h1:56OvJKSH3hDGL0ml5uSxZmz3/3Pq4tJ+fb1unVLAFcY=
cel.dev/expr v0.24.0/go.mod h1:hLPLo1W4QUmuYdA72RBX06QTs6MXw941piREPl3Yfiw=
cloud.google.com/go/compute v1.25.1 h1:ZRpHJedLtTpKgr3RV1Fx23NuaAEN1Zfx9hw1u4aJdjU=
cloud.google.com/go/compute v1.25.1/go.mod h1:oopOIR53ly6viBYxaDhBfJwzUAxf1zE//uf3IB011ls=
cloud.google.com/go/compute/metadata v0.2.3 h1:mg4jlk7mCAj6xXp9UJ4fjI9VUI5rubuGBW5aJ7UnBMY=
cloud.google.com/go/compute/metadata v0.2.3/go.mod h1:VAV5nSsACxMJvgaAuX6Pk2AawlZn8kiOGuCv6gTkwuA=
cloud.google.com/go/compute/metadata v0.5.2 h1:UxK4uu/Tn+I3p2dYWTfiX4wva7aYlKixAHn3fyqngqo=
cloud.google.com/go/compute/metadata v0.5.2/go.mod h1:C66sj2AluDcIqakBq/M8lw8/ybHgOZqin2obFxa/E5k=
cloud.google.com/go/compute/metadata v0.6.0 h1:A6hENjEsCDtC1k8byVsgwvVcioamEHvZ4j01OwKxG9I=
cloud.google.com/go/compute/metadata v0.6.0/go.mod h1:FjyFAW1MW0C203CEOMDTu3Dk1FlqW3Rga40jzHL4hfg=
cloud.google.com/go/compute/metadata v0.7.0/go.mod h1:j5MvL9PprKL39t166CoB1uVHfQMs4tFQZZcKwksXUjo=
cloud.google.com/go/compute/metadata v0.9.0 h1:pDUj4QMoPejqq20dK0Pg2N4yG9zIkYGdBtwLoEkH9Zs=
cloud.google.com/go/compute/metadata v0.9.0/go.mod h1:E0bWwX5wTnLPedCKqk3pJmVgCBSM6qQI1yTBdEb3C10=
github.com/GoogleCloudPlatform/opentelemetry-operations-go/detectors/gcp v1.24.2 h1:cZpsGsWTIFKymTA0je7IIvi1O7Es7apb9CF3EQlOcfE=
github.com/GoogleCloudPlatform/opentelemetry-operations-go/detectors/gcp v1.24.2/go.mod h1:itPGVDKf9cC/ov4MdvJ2QZ0khw4bfoo9jzwTJlaxy2k=
github.com/GoogleCloudPlatform/opentelemetry-operations-go/detectors/gcp v1.25.0 h1:3c8yed4lgqTt+oTQ+JNMDo+F4xprBf+O/il4ZC0nRLw=
github.com/GoogleCloudPlatform/opentelemetry-operations-go/detectors/gcp v1.25.0/go.mod h1:obipzmGjfSjam60XLwGfqUkJsfiheAl+TUjG+4yzyPM=
github.com/GoogleCloudPlatform/opentelemetry-operations-go/detectors/gcp v1.26.0 h1:f2Qw/Ehhimh5uO1fayV0QIW7DShEQqhtUfhYc+cBPlw=
github.com/GoogleCloudPlatform/opentelemetry-operations-go/detectors/gcp v1.26.0/go.mod h1:2bIszWvQRlJVmJLiuLhukLImRjKPcYdzzsx6darK02A=
github.com/GoogleCloudPlatform/opentelemetry-operations-go/detectors/gcp v1.29.0/go.mod h1:Cz6ft6Dkn3Et6l2v2a9/RpN7epQ1GtDlO6lj8bEcOvw=
github.com/GoogleCloudPlatform/opentelemetry-operations-go/detectors/gcp v1.30.0 h1:sBEjpZlNHzK1voKq9695PJSX2o5NEXl7/OL3coiIY0c=
github.com/GoogleCloudPlatform/opentelemetry-operations-go/detectors/gcp v1.30.0/go.mod h1:P4WPRUkOhJC13W//jWpyfJNDAIpvRbAUIYLX/4jtlE0=
github.com/antihax/optional v1.0.0 h1:xK2lYat7ZLaVVcIuj82J8kIro4V6kDe0AUDFboUCwcg=
github.com/antihax/optional v1.0.0/go.mod h1:uupD/76wgC+ih3iEmQUL+0Ugr19nfwCT1kdvxnR2qWY=
github.com/census-instrumentation/opencensus-proto v0.4.1 h1:iKLQ0xPNFxR/2hzXZMrBo8f1j86j5WHzznCCQxV/b8g=
github.com/census-instrumentation/opencensus-proto v0.4.1/go.mod h1:4T9NM4+4Vw91VeyqjLS6ao50K5bOcLKN6Q42XnYaRYw=
github.com/cespare/xxhash/v2 v2.2.0 h1:DC2CZ1Ep5Y4k3ZQ899DldepgrayRUGE6BBZ/cd9Cj44=
github.com/cespare/xxhash/v2 v2.2.0/go.mod h1:VGX0DQ3Q6kWi7AoAeZDth3/j3BFtOZR5XLFGgcrjCOs=
github.com/cncf/xds/go v0.0.0-20240318125728-8a4994d93e50 h1:DBmgJDC9dTfkVyGgipamEh2BpGYxScCH1TOF1LL1cXc=
github.com/cncf/xds/go v0.0.0-20240318125728-8a4994d93e50/go.mod h1:5e1+Vvlzido69INQaVO6d87Qn543Xr6nooe9Kz7oBFM=
github.com/cncf/xds/go v0.0.0-20240905190251-b4127c9b8d78 h1:QVw89YDxXxEe+l8gU8ETbOasdwEV+avkR75ZzsVV9WI=
github.com/cncf/xds/go v0.0.0-20240905190251-b4127c9b8d78/go.mod h1:W+zGtBO5Y1IgJhy4+A9GOqVhqLpfZi+vwmdNXUehLA8=
github.com/cncf/xds/go v0.0.0-20241223141626-cff3c89139a3 h1:boJj011Hh+874zpIySeApCX4GeOjPl9qhRF3QuIZq+Q=
github.com/cncf/xds/go v0.0.0-20241223141626-cff3c89139a3/go.mod h1:W+zGtBO5Y1IgJhy4+A9GOqVhqLpfZi+vwmdNXUehLA8=
github.com/cncf/xds/go v0.0.0-20250121191232-2f005788dc42 h1:Om6kYQYDUk5wWbT0t0q6pvyM49i9XZAv9dDrkDA7gjk=
github.com/cncf/xds/go v0.0.0-20250121191232-2f005788dc42/go.mod h1:W+zGtBO5Y1IgJhy4+A9GOqVhqLpfZi+vwmdNXUehLA8=
github.com/cncf/xds/go v0.0.0-20250501225837-2ac532fd4443/go.mod h1:W+zGtBO5Y1IgJhy4+A9GOqVhqLpfZi+vwmdNXUehLA8=
github.com/cncf/xds/go v0.0.0-20251022180443-0feb69152e9f h1:Y8xYupdHxryycyPlc9Y+bSQAYZnetRJ70VMVKm5CKI0=
github.com/cncf/xds/go v0.0.0-20251022180443-0feb69152e9f/go.mod h1:HlzOvOjVBOfTGSRXRyY0OiCS/3J1akRGQQpRO/7zyF4=
github.com/envoyproxy/go-control-plane v0.12.0 h1:4X+VP1GHd1Mhj6IB5mMeGbLCleqxjletLK6K0rbxyZI=
github.com/envoyproxy/go-control-plane v0.12.0/go.mod h1:ZBTaoJ23lqITozF0M6G4/IragXCQKCnYbmlmtHvwRG0=
github.com/envoyproxy/go-control-plane v0.13.1 h1:vPfJZCkob6yTMEgS+0TwfTUfbHjfy/6vOJ8hUWX/uXE=
github.com/envoyproxy/go-control-plane v0.13.1/go.mod h1:X45hY0mufo6Fd0KW3rqsGvQMw58jvjymeCzBU3mWyHw=
github.com/envoyproxy/go-control-plane v0.13.4 h1:zEqyPVyku6IvWCFwux4x9RxkLOMUL+1vC9xUFv5l2/M=
github.com/envoyproxy/go-control-plane v0.13.4/go.mod h1:kDfuBlDVsSj2MjrLEtRWtHlsWIFcGyB2RMO44Dc5GZA=
github.com/envoyproxy/go-control-plane v0.13.5-0.20251024222203-75eaa193e329 h1:K+fnvUM0VZ7ZFJf0n4L/BRlnsb9pL/GuDG6FqaH+PwM=
github.com/envoyproxy/go-control-plane v0.13.5-0.20251024222203-75eaa193e329/go.mod h1:Alz8LEClvR7xKsrq3qzoc4N0guvVNSS8KmSChGYr9hs=
github.com/envoyproxy/go-control-plane/envoy v1.32.4 h1:jb83lalDRZSpPWW2Z7Mck/8kXZ5CQAFYVjQcdVIr83A=
github.com/envoyproxy/go-control-plane/envoy v1.32.4/go.mod h1:Gzjc5k8JcJswLjAx1Zm+wSYE20UrLtt7JZMWiWQXQEw=
github.com/envoyproxy/go-control-plane/envoy v1.35.0 h1:ixjkELDE+ru6idPxcHLj8LBVc2bFP7iBytj353BoHUo=
github.com/envoyproxy/go-control-plane/envoy v1.35.0/go.mod h1:09qwbGVuSWWAyN5t/b3iyVfz5+z8QWGrzkoqm/8SbEs=
github.com/envoyproxy/go-control-plane/ratelimit v0.1.0 h1:/G9QYbddjL25KvtKTv3an9lx6VBE2cnb8wp1vEGNYGI=
github.com/envoyproxy/go-control-plane/ratelimit v0.1.0/go.mod h1:Wk+tMFAFbCXaJPzVVHnPgRKdUdwW/KdbRt94AzgRee4=
github.com/envoyproxy/protoc-gen-validate v1.0.4 h1:gVPz/FMfvh57HdSJQyvBtF00j8JU4zdyUgIUNhlgg0A=
github.com/envoyproxy/protoc-gen-validate v1.0.4/go.mod h1:qys6tmnRsYrQqIhm2bvKZH4Blx/1gTIZ2UKVY1M+Yew=
github.com/envoyproxy/protoc-gen-validate v1.1.0 h1:tntQDh69XqOCOZsDz0lVJQez/2L6Uu2PdjCQwWCJ3bM=
github.com/envoyproxy/protoc-gen-validate v1.1.0/go.mod h1:sXRDRVmzEbkM7CVcM06s9shE/m23dg3wzjl0UWqJ2q4=
github.com/envoyproxy/protoc-gen-validate v1.2.1 h1:DEo3O99U8j4hBFwbJfrz9VtgcDfUKS7KJ7spH3d86P8=
github.com/envoyproxy/protoc-gen-validate v1.2.1/go.mod h1:d/C80l/jxXLdfEIhX1W2TmLfsJ31lvEjwamM4DxlWXU=
github.com/go-jose/go-jose/v4 v4.0.4 h1:VsjPI33J0SB9vQM6PLmNjoHqMQNGPiZ0rHL7Ni7Q6/E=
github.com/go-jose/go-jose/v4 v4.0.4/go.mod h1:NKb5HO1EZccyMpiZNbdUw/14tiXNyUJh188dfnMCAfc=
github.com/go-jose/go-jose/v4 v4.1.1/go.mod h1:BdsZGqgdO3b6tTc6LSE56wcDbMMLuPsw5d4ZD5f94kA=
github.com/go-jose/go-jose/v4 v4.1.3 h1:CVLmWDhDVRa6Mi/IgCgaopNosCaHz7zrMeF9MlZRkrs=
github.com/go-jose/go-jose/v4 v4.1.3/go.mod h1:x4oUasVrzR7071A4TnHLGSPpNOm2a21K9Kf04k1rs08=
github.com/golang/glog v1.2.0 h1:uCdmnmatrKCgMBlM4rMuJZWOkPDqdbZPnrMXDY4gI68=
github.com/golang/glog v1.2.0/go.mod h1:6AhwSGph0fcJtXVM/PEHPqZlFeoLxhs7/t5UDAwmO+w=
github.com/golang/glog v1.2.2 h1:1+mZ9upx1Dh6FmUTFR1naJ77miKiXgALjWOZ3NVFPmY=
github.com/golang/glog v1.2.2/go.mod h1:6AhwSGph0fcJtXVM/PEHPqZlFeoLxhs7/t5UDAwmO+w=
github.com/golang/glog v1.2.4 h1:CNNw5U8lSiiBk7druxtSHHTsRWcxKoac6kZKm2peBBc=
github.com/golang/glog v1.2.4/go.mod h1:6AhwSGph0fcJtXVM/PEHPqZlFeoLxhs7/t5UDAwmO+w=
github.com/golang/glog v1.2.5 h1:DrW6hGnjIhtvhOIiAKT6Psh/Kd/ldepEa81DKeiRJ5I=
github.com/golang/glog v1.2.5/go.mod h1:6AhwSGph0fcJtXVM/PEHPqZlFeoLxhs7/t5UDAwmO+w=
github.com/kr/pretty v0.3.1 h1:flRD4NNwYAUpkphVc1HcthR4KEIFJ65n8Mw5qdRn3LE=
github.com/kr/pretty v0.3.1/go.mod h1:hoEshYVHaxMs3cyo3Yncou5ZscifuDolrwPKZanG3xk=
github.com/kr/text v0.2.0 h1:5Nx0Ya0ZqY2ygV366QzturHI13Jq95ApcVaJBhpS+AY=
github.com/kr/text v0.2.0/go.mod h1:eLer722TekiGuMkidMxC/pM04lWEeraHUUmBw8l2grE=
github.com/planetscale/vtprotobuf v0.6.1-0.20240319094008-0393e58bdf10 h1:GFCKgmp0tecUJ0sJuv4pzYCqS9+RGSn52M3FUwPs+uo=
github.com/planetscale/vtprotobuf v0.6.1-0.20240319094008-0393e58bdf10/go.mod h1:t/avpk3KcrXxUnYOhZhMXJlSEyie6gQbtLq5NM3loB8=
github.com/rogpeppe/fastuuid v1.2.0 h1:Ppwyp6VYCF1nvBTXL3trRso7mXMlRrw9ooo375wvi2s=
github.com/rogpeppe/fastuuid v1.2.0/go.mod h1:jVj6XXZzXRy/MSR5jhDC/2q6DgLz+nrA6LYCDYWNEvQ=
github.com/rogpeppe/go-internal v1.12.0 h1:exVL4IDcn6na9z1rAb56Vxr+CgyK3nn3O+epU5NdKM8=
github.com/rogpeppe/go-internal v1.12.0/go.mod h1:E+RYuTGaKKdloAfM02xzb0FW3Paa99yedzYV+kq4uf4=
github.com/rogpeppe/go-internal v1.13.1 h1:KvO1DLK/DRN07sQ1LQKScxyZJuNnedQ5/wKSR38lUII=
github.com/rogpeppe/go-internal v1.13.1/go.mod h1:uMEvuHeurkdAXX61udpOXGD/AzZDWNMNyH2VO9fmH0o=
github.com/rogpeppe/go-internal v1.14.1 h1:UQB4HGPB6osV0SQTLymcB4TgvyWu6ZyliaW0tI/otEQ=
github.com/rogpeppe/go-internal v1.14.1/go.mod h1:MaRKkUm5W0goXpeCfT7UZI6fk/L7L7so1lCWt35ZSgc=
github.com/spiffe/go-spiffe/v2 v2.5.0 h1:N2I01KCUkv1FAjZXJMwh95KK1ZIQLYbPfhaxw8WS0hE=
github.com/spiffe/go-spiffe/v2 v2.5.0/go.mod h1:P+NxobPc6wXhVtINNtFjNWGBTreew1GBUCwT2wPmb7g=
github.com/spiffe/go-spiffe/v2 v2.6.0 h1:l+DolpxNWYgruGQVV0xsfeya3CsC7m8iBzDnMpsbLuo=
github.com/spiffe/go-spiffe/v2 v2.6.0/go.mod h1:gm2SeUoMZEtpnzPNs2Csc0D/gX33k1xIx7lEzqblHEs=
github.com/zeebo/errs v1.4.0 h1:XNdoD/RRMKP7HD0UhJnIzUy74ISdGGxURlYG8HSWSfM=
github.com/zeebo/errs v1.4.0/go.mod h1:sgbWHsvVuTPHcqJJGQ1WhI5KbWlHYz+2+2C/LSEtCw4=
go.opentelemetry.io/contrib/detectors/gcp v1.31.0 h1:G1JQOreVrfhRkner+l4mrGxmfqYCAuy76asTDAo0xsA=
go.opentelemetry.io/contrib/detectors/gcp v1.31.0/go.mod h1:tzQL6E1l+iV44YFTkcAeNQqzXUiekSYP9jjJjXwEd00=
go.opentelemetry.io/contrib/detectors/gcp v1.34.0 h1:JRxssobiPg23otYU5SbWtQC//snGVIM3Tx6QRzlQBao=
go.opentelemetry.io/contrib/detectors/gcp v1.34.0/go.mod h1:cV4BMFcscUR/ckqLkbfQmF0PRsq8w/lMGzdbCSveBHo=
go.opentelemetry.io/contrib/detectors/gcp v1.36.0/go.mod h1:IbBN8uAIIx734PTonTPxAxnjc2pQTxWNkwfstZ+6H2k=
go.opentelemetry.io/contrib/detectors/gcp v1.38.0 h1:ZoYbqX7OaA/TAikspPl3ozPI6iY6LiIY9I8cUfm+pJs=
go.opentelemetry.io/contrib/detectors/gcp v1.38.0/go.mod h1:SU+iU7nu5ud4oCb3LQOhIZ3nRLj6FNVrKgtflbaf2ts=
go.opentelemetry.io/otel/sdk/log/logtest v0.0.0-20250521073539-a85ae98dcedc h1:uqxdywfHqqCl6LmZzI3pUnXT1RGFYyUgxj0AkWPFxi0=
go.opentelemetry.io/otel/sdk/log/logtest v0.0.0-20250521073539-a85ae98dcedc/go.mod h1:TY/N/FT7dmFrP/r5ym3g0yysP1DefqGpAZr4f82P0dE=
go.yaml.in/yaml/v3 v3.0.4 h1:tfq32ie2Jv2UxXFdLJdh3jXuOzWiL1fo0bu/FbuKpbc=
go.yaml.in/yaml/v3 v3.0.4/go.mod h1:DhzuOOF2ATzADvBadXxruRBLzYTpT36CKvDb3+aBEFg=
golang.org/x/crypto v0.24.0 h1:mnl8DM0o513X8fdIkmyFE/5hTYxbwYOjDS/+rK6qpRI=
golang.org/x/crypto v0.24.0/go.mod h1:Z1PMYSOR5nyMcyAVAIQSKCDwalqy85Aqn1x3Ws4L5DM=
golang.org/x/crypto v0.31.0 h1:ihbySMvVjLAeSH1IbfcRTkD/iNscyz8rGzjF/E5hV6U=
golang.org/x/crypto v0.31.0/go.mod h1:kDsLvtWBEx7MV9tJOj9bnXsPbxwJQ6csT/x4KIN4Ssk=
golang.org/x/crypto v0.32.0 h1:euUpcYgM8WcP71gNpTqQCn6rC2t6ULUPiOzfWaXVVfc=
golang.org/x/crypto v0.32.0/go.mod h1:ZnnJkOaASj8g0AjIduWNlq2NRxL0PlBrbKVyZ6V/Ugc=
golang.org/x/crypto v0.33.0 h1:IOBPskki6Lysi0lo9qQvbxiQ+FvsCC/YWOecCHAixus=
golang.org/x/crypto v0.33.0/go.mod h1:bVdXmD7IV/4GdElGPozy6U7lWdRXA4qyRVGJV57uQ5M=
golang.org/x/crypto v0.36.0 h1:AnAEvhDddvBdpY+uR+MyHmuZzzNqXSe/GvuDeob5L34=
golang.org/x/crypto v0.36.0/go.mod h1:Y4J0ReaxCR1IMaabaSMugxJES1EpwhBHhv2bDHklZvc=
golang.org/x/crypto v0.38.0 h1:jt+WWG8IZlBnVbomuhg2Mdq0+BBQaHbtqHEFEigjUV8=
golang.org/x/crypto v0.38.0/go.mod h1:MvrbAqul58NNYPKnOra203SB9vpuZW0e+RRZV+Ggqjw=
golang.org/x/crypto v0.41.0/go.mod h1:pO5AFd7FA68rFak7rOAGVuygIISepHftHnr8dr6+sUc=
golang.org/x/crypto v0.44.0 h1:A97SsFvM3AIwEEmTBiaxPPTYpDC47w720rdiiUvgoAU=
golang.org/x/crypto v0.44.0/go.mod h1:013i+Nw79BMiQiMsOPcVCB5ZIJbYkerPrGnOa00tvmc=
golang.org/x/crypto v0.47.0 h1:V6e3FRj+n4dbpw86FJ8Fv7XVOql7TEwpHapKoMJ/GO8=
golang.org/x/crypto v0.47.0/go.mod h1:ff3Y9VzzKbwSSEzWqJsJVBnWmRwRSHt/6Op5n9bQc4A=
golang.org/x/mod v0.17.0 h1:zY54UmvipHiNd+pm+m0x9KhZ9hl1/7QNMyxXbc6ICqA=
golang.org/x/mod v0.17.0/go.mod h1:hTbmBsO62+eylJbnUtE2MGJUyE7QWk4xUqPFrRgJ+7c=
golang.org/x/mod v0.26.0/go.mod h1:/j6NAhSk8iQ723BGAUyoAcn7SlD7s15Dp9Nd/SfeaFQ=
golang.org/x/mod v0.29.0 h1:HV8lRxZC4l2cr3Zq1LvtOsi/ThTgWnUk/y64QSs8GwA=
golang.org/x/mod v0.29.0/go.mod h1:NyhrlYXJ2H4eJiRy/WDBO6HMqZQ6q9nk4JzS3NuCK+w=
golang.org/x/mod v0.31.0 h1:HaW9xtz0+kOcWKwli0ZXy79Ix+UW/vOfmWI5QVd2tgI=
golang.org/x/mod v0.31.0/go.mod h1:43JraMp9cGx1Rx3AqioxrbrhNsLl2l/iNAvuBkrezpg=
golang.org/x/oauth2 v0.20.0 h1:4mQdhULixXKP1rwYBW0vAijoXnkTG0BLCDRzfe1idMo=
golang.org/x/oauth2 v0.20.0/go.mod h1:XYTD2NtWslqkgxebSiOHnXEap4TF09sJSc7H1sXbhtI=
golang.org/x/oauth2 v0.24.0 h1:KTBBxWqUa0ykRPLtV69rRto9TLXcqYkeswu48x/gvNE=
golang.org/x/oauth2 v0.24.0/go.mod h1:XYTD2NtWslqkgxebSiOHnXEap4TF09sJSc7H1sXbhtI=
golang.org/x/oauth2 v0.26.0 h1:afQXWNNaeC4nvZ0Ed9XvCCzXM6UHJG7iCg0W4fPqSBE=
golang.org/x/oauth2 v0.26.0/go.mod h1:XYTD2NtWslqkgxebSiOHnXEap4TF09sJSc7H1sXbhtI=
golang.org/x/oauth2 v0.27.0 h1:da9Vo7/tDv5RH/7nZDz1eMGS/q1Vv1N/7FCrBhI9I3M=
golang.org/x/oauth2 v0.27.0/go.mod h1:onh5ek6nERTohokkhCD/y2cV4Do3fxFHFuAejCkRWT8=
golang.org/x/oauth2 v0.30.0/go.mod h1:B++QgG3ZKulg6sRPGD/mqlHQs5rB3Ml9erfeDY7xKlU=
golang.org/x/oauth2 v0.32.0 h1:jsCblLleRMDrxMN29H3z/k1KliIvpLgCkE6R8FXXNgY=
golang.org/x/oauth2 v0.32.0/go.mod h1:lzm5WQJQwKZ3nwavOZ3IS5Aulzxi68dUSgRHujetwEA=
golang.org/x/oauth2 v0.34.0 h1:hqK/t4AKgbqWkdkcAeI8XLmbK+4m4G5YeQRrmiotGlw=
golang.org/x/oauth2 v0.34.0/go.mod h1:lzm5WQJQwKZ3nwavOZ3IS5Aulzxi68dUSgRHujetwEA=
golang.org/x/sync v0.7.0 h1:YsImfSBoP9QPYL0xyKJPq0gcaJdG3rInoqxTWbfQu9M=
golang.org/x/sync v0.7.0/go.mod h1:Czt+wKu1gCyEFDUtn0jG5QVvpJ6rzVqr5aXyt9drQfk=
golang.org/x/sync v0.10.0 h1:3NQrjDixjgGwUOCaF8w2+VYHv0Ve/vGYSbdkTa98gmQ=
golang.org/x/sync v0.10.0/go.mod h1:Czt+wKu1gCyEFDUtn0jG5QVvpJ6rzVqr5aXyt9drQfk=
golang.org/x/sync v0.11.0 h1:GGz8+XQP4FvTTrjZPzNKTMFtSXH80RAzG+5ghFPgK9w=
golang.org/x/sync v0.11.0/go.mod h1:Czt+wKu1gCyEFDUtn0jG5QVvpJ6rzVqr5aXyt9drQfk=
golang.org/x/sync v0.12.0 h1:MHc5BpPuC30uJk597Ri8TV3CNZcTLu6B6z4lJy+g6Jw=
golang.org/x/sync v0.12.0/go.mod h1:1dzgHSNfp02xaA81J2MS99Qcpr2w7fw1gpm99rleRqA=
golang.org/x/sync v0.14.0 h1:woo0S4Yywslg6hp4eUFjTVOyKt0RookbpAHG4c1HmhQ=
golang.org/x/sync v0.14.0/go.mod h1:1dzgHSNfp02xaA81J2MS99Qcpr2w7fw1gpm99rleRqA=
golang.org/x/sync v0.16.0/go.mod h1:1dzgHSNfp02xaA81J2MS99Qcpr2w7fw1gpm99rleRqA=
golang.org/x/sync v0.18.0 h1:kr88TuHDroi+UVf+0hZnirlk8o8T+4MrK6mr60WkH/I=
golang.org/x/sync v0.18.0/go.mod h1:9KTHXmSnoGruLpwFjVSX0lNNA75CykiMECbovNTZqGI=
golang.org/x/sync v0.19.0 h1:vV+1eWNmZ5geRlYjzm2adRgW2/mcpevXNg50YZtPCE4=
golang.org/x/sync v0.19.0/go.mod h1:9KTHXmSnoGruLpwFjVSX0lNNA75CykiMECbovNTZqGI=
golang.org/x/term v0.21.0 h1:WVXCp+/EBEHOj53Rvu+7KiT/iElMrO8ACK16SMZ3jaA=
golang.org/x/term v0.21.0/go.mod h1:ooXLefLobQVslOqselCNF4SxFAaoS6KujMbsGzSDmX0=
golang.org/x/term v0.27.0 h1:WP60Sv1nlK1T6SupCHbXzSaN0b9wUmsPoRS9b61A23Q=
golang.org/x/term v0.27.0/go.mod h1:iMsnZpn0cago0GOrHO2+Y7u7JPn5AylBrcoWkElMTSM=
golang.org/x/term v0.28.0 h1:/Ts8HFuMR2E6IP/jlo7QVLZHggjKQbhu/7H0LJFr3Gg=
golang.org/x/term v0.28.0/go.mod h1:Sw/lC2IAUZ92udQNf3WodGtn4k/XoLyZoh8v/8uiwek=
golang.org/x/term v0.29.0 h1:L6pJp37ocefwRRtYPKSWOWzOtWSxVajvz2ldH/xi3iU=
golang.org/x/term v0.29.0/go.mod h1:6bl4lRlvVuDgSf3179VpIxBF0o10JUpXWOnI7nErv7s=
golang.org/x/term v0.30.0 h1:PQ39fJZ+mfadBm0y5WlL4vlM7Sx1Hgf13sMIY2+QS9Y=
golang.org/x/term v0.30.0/go.mod h1:NYYFdzHoI5wRh/h5tDMdMqCqPJZEuNqVR5xJLd/n67g=
golang.org/x/term v0.32.0 h1:DR4lr0TjUs3epypdhTOkMmuF5CDFJ/8pOnbzMZPQ7bg=
golang.org/x/term v0.32.0/go.mod h1:uZG1FhGx848Sqfsq4/DlJr3xGGsYMu/L5GW4abiaEPQ=
golang.org/x/term v0.34.0/go.mod h1:5jC53AEywhIVebHgPVeg0mj8OD3VO9OzclacVrqpaAw=
golang.org/x/term v0.37.0 h1:8EGAD0qCmHYZg6J17DvsMy9/wJ7/D/4pV/wfnld5lTU=
golang.org/x/term v0.37.0/go.mod h1:5pB4lxRNYYVZuTLmy8oR2BH8dflOR+IbTYFD8fi3254=
golang.org/x/term v0.39.0 h1:RclSuaJf32jOqZz74CkPA9qFuVTX7vhLlpfj/IGWlqY=
golang.org/x/term v0.39.0/go.mod h1:yxzUCTP/U+FzoxfdKmLaA0RV1WgE0VY7hXBwKtY/4ww=
golang.org/x/tools v0.21.1-0.20240508182429-e35e4ccd0d2d h1:vU5i/LfpvrRCpgM/VPfJLg5KjxD3E+hfT1SH+d9zLwg=
golang.org/x/tools v0.21.1-0.20240508182429-e35e4ccd0d2d/go.mod h1:aiJjzUbINMkxbQROHiO6hDPo2LHcIPhhQsa9DLh0yGk=
golang.org/x/tools v0.35.0/go.mod h1:NKdj5HkL/73byiZSJjqJgKn3ep7KjFkBOkR/Hps3VPw=
golang.org/x/tools v0.38.0 h1:Hx2Xv8hISq8Lm16jvBZ2VQf+RLmbd7wVUsALibYI/IQ=
golang.org/x/tools v0.38.0/go.mod h1:yEsQ/d/YK8cjh0L6rZlY8tgtlKiBNTL14pGDJPJpYQs=
golang.org/x/tools v0.40.0 h1:yLkxfA+Qnul4cs9QA3KnlFu0lVmd8JJfoq+E41uSutA=
golang.org/x/tools v0.40.0/go.mod h1:Ik/tzLRlbscWpqqMRjyWYDisX8bG13FrdXp3o4Sr9lc=
golang.org/x/xerrors v0.0.0-20191204190536-9bdfabe68543 h1:E7g+9GITq07hpfrRu66IVDexMakfv52eLZ2CXBWiKr4=
golang.org/x/xerrors v0.0.0-20191204190536-9bdfabe68543/go.mod h1:I/5z698sn9Ka8TeJc9MKroUUfqBBauWjQqLJ2OPfmY0=
google.golang.org/appengine v1.6.8 h1:IhEN5q69dyKagZPYMSdIjS2HqprW324FRQZJcGqPAsM=
google.golang.org/appengine v1.6.8/go.mod h1:1jJ3jBArFh5pcgW8gCtRJnepW8FzD1V44FJffLiz/Ds=
gopkg.in/check.v1 v1.0.0-20201130134442-10cb98267c6c h1:Hei/4ADfdWqJk1ZMxUNpqntNwaWcugrBjAiHlqqRiVk=
gopkg.in/check.v1 v1.0.0-20201130134442-10cb98267c6c/go.mod h1:JHkPIbrfpd72SG/EVd6muEfDQjcINNoR0C8j2r3qZ4Q=
```

## File: `mise.toml`
```
# pin all versions to avoid GitHub rate limit
[tools]
go = "1.26.1"
"go:github.com/grafana/oats" = "0.6.1"
java = "temurin-25.0.2+10.0.LTS"
lychee = "0.22.0"
node = "24.14.1"
"npm:renovate" = "43.66.3"
rust = "1.94.1"

[env]
RENOVATE_TRACKED_DEPS_EXCLUDE="github-actions,github-runners"
# renovate: datasource=docker depName=ghcr.io/super-linter/super-linter
SUPER_LINTER_VERSION="v8.4.0@sha256:c5e3307932203ff9e1e8acfe7e92e894add6266605b5d7fb525fb371a59a26f4"

# Shared lint tasks from flint (https://github.com/grafana/flint)
[tasks."lint:super-linter"]
description = "Run Super-Linter on the repository"
file = "https://raw.githubusercontent.com/grafana/flint/8a39d96e17327c54974623b252eb5260d67ed68a/tasks/lint/super-linter.sh" # v0.9.1
[tasks."lint:links"]
description = "Check for broken links in changed files + all local links"
file = "https://raw.githubusercontent.com/grafana/flint/8a39d96e17327c54974623b252eb5260d67ed68a/tasks/lint/links.sh" # v0.9.1
[tasks."lint:renovate-deps"]
description = "Verify renovate-tracked-deps.json is up to date"
file = "https://raw.githubusercontent.com/grafana/flint/8a39d96e17327c54974623b252eb5260d67ed68a/tasks/lint/renovate-deps.py" # v0.9.1

[tasks."setup:native-lint-tools"]
description = "Install native lint tools matching the pinned super-linter version"
file = "https://raw.githubusercontent.com/grafana/flint/8a39d96e17327c54974623b252eb5260d67ed68a/tasks/setup/native-lint-tools.sh" # v0.9.1
[tasks."lint:fast"]
description = "Run fast lints (no Renovate)"
depends = ["lint:super-linter", "lint:links"]

[tasks.native-lint]
description = "Run lints natively (no container)"
run = "NATIVE=true mise run lint:fast"

[tasks.pre-commit]
description = "Pre-commit hook: native lint"
depends = ["setup:native-lint-tools"]
run = "NATIVE=true mise run lint:fast"
[tasks."setup:pre-commit-hook"]
description = "Install git pre-commit hook that runs native linting"
run = "mise generate git-pre-commit --write --task=pre-commit"

[tasks."lint"]
description = "Run all lints"
depends = ["lint:fast", "lint:renovate-deps"]

[tasks.fix]
description = "Auto-fix lint issues and regenerate tracked deps"
run = "AUTOFIX=true mise run lint"

[tasks.lgtm]
description = "Run LGTM image"
usage = 'arg "<tag>" default="latest"'
run = './run-lgtm.sh ${usage_tag}'

[tasks.lgtm-obi]
description = "Run LGTM with OBI eBPF auto-instrumentation"
usage = '''
flag "--local" help="Use locally built image"
arg "<tag>" default="latest"
'''
env = { ENABLE_OBI = "true" }
run = 'if [ "$usage_local" = "true" ]; then ./run-lgtm.sh ${usage_tag} true; else ./run-lgtm.sh ${usage_tag}; fi'

[tasks.local-lgtm]
description = "Run locally built LGTM image"
run = './run-lgtm.sh latest true'

[tasks.example]
description = "Run Java example"
alias = "example-java"
run = "./run-example.sh"

[tasks.example-nodejs]
description = "Run Node.js example"
dir = "examples/nodejs"
run = "./run.sh"

[tasks.example-python]
description = "Run Python example"
dir = "examples/python"
run = "./run.sh"

[tasks.example-go]
description = "Run Go example"
dir = "examples/go"
run = "./run.sh"

[tasks.example-dotnet]
description = "Run .NET example"
dir = "examples/dotnet"
run = "./run.sh"

[tasks.generate-traffic]
description = "Generate traffic for the running example"
run = "./generate-traffic.sh"

[tasks.all]
description = "Run LGTM, example, and generate traffic"
depends = ["lgtm", "example", "generate-traffic"]

[tasks.k8s-apply]
description = "Apply LGTM Kubernetes manifest"
run = "kubectl apply -f k8s/lgtm.yaml"

[tasks.k8s-port-forward]
description = "Port-forward LGTM Kubernetes service"
run = "kubectl port-forward service/lgtm 3000:3000 4040:4040 4317:4317 4318:4318 9090:9090"

[tasks.build-lgtm]
description = "Build LGTM image"
usage = 'arg "<tag>" default="latest"'
run = './build-lgtm.sh ${usage_tag}'

[settings]
# for go backend
experimental = true
```

## File: `run-example.cmd`
```
@echo off

cd examples/java
run
```

## File: `run-example.sh`
```bash
#!/bin/bash

set -euo pipefail

cd examples/java
./run.sh
```

## File: `run-lgtm.cmd`
```
@echo off

set "releasetag=%~1"
set "local=%~2"

if "%releasetag%"=="" set "releasetag=latest"
if "%localimg%"=="" set "localimg=0"
if "%localimg%"=="false" set "localimg=0"
if "%localimg%"=="true" set "localimg=1"

powershell -ExecutionPolicy ByPass -NoProfile -Command "& '%~dp0\run-lgtm.ps1' -ReleaseTag '%releasetag%' -UseLocalImage %localimg%"
exit /b %ERRORLEVEL%
```

## File: `run-lgtm.ps1`
```powershell
param (
    [Parameter(Mandatory = $false, Position = 0)] [string]  $ReleaseTag = "latest",
    [Parameter(Mandatory = $false, Position = 1)] [boolean] $UseLocalImage = $false
)

$supportedContainerRuntime = 'podman', 'docker'
$containers = 'grafana', 'prometheus', 'loki'
$image = "docker.io/grafana/otel-lgtm:${ReleaseTag}"

# prefilled pwd var to avoid repeated calls in build string.moved to top init section or logic
$path = (Get-Location).Path

$containerCommand = $supportedContainerRuntime | ForEach-Object {
    (Get-Command $_ -ErrorAction SilentlyContinue).Source
} | Select-Object -first 1

if ($null -eq $containerCommand) {
    Write-Error "Unable to find a suitable container runtime such as Docker or Podman. Exiting."
    return
}

$containers | ForEach-Object {
    $null = New-Item -ItemType Directory -Path "$path/container/$_" -Force
}

if (-Not (Test-Path -Path ".env")) {
    New-Item -ItemType File -Path ".env" -Force | Out-Null
}

if ($UseLocalImage) {
    if ($containerCommand -eq 'podman') {
        $image = "localhost/grafana/otel-lgtm:${ReleaseTag}"
    }
    else {
        $image = "grafana/otel-lgtm:${ReleaseTag}"
    }
}
else {
    $image = "docker.io/grafana/otel-lgtm:${ReleaseTag}"
    & $containerCommand image pull $image
}

# Check if OBI is enabled (from environment or .env file)
$obiFlags = @()
$obiEnabled = $env:ENABLE_OBI -eq 'true'
if (-Not $obiEnabled -and (Test-Path -Path ".env")) {
    $obiEnabled = (Get-Content ".env" | Select-String -Pattern '^ENABLE_OBI=true$' -Quiet)
}
if ($obiEnabled) {
    Write-Output "OBI eBPF auto-instrumentation enabled. Adding --pid=host --privileged flags."
    $obiFlags = @('--pid=host', '--privileged')
    # Forward OBI-specific env vars into the container (they are not in .env by default).
    # General OTLP vars (OTEL_EXPORTER_OTLP_ENDPOINT, etc.) are forwarded via --env-file .env.
    $obiFlags += '-e', 'ENABLE_OBI=true'
    Get-ChildItem env: |
        Where-Object { $_.Name -match '^(OBI_TARGET|OTEL_EBPF_|ENABLE_LOGS_OBI)' } |
        ForEach-Object {
            $obiFlags += '-e', "$($_.Name)=$($_.Value)"
        }
}

# Allocate TTY only if stdin is interactive
$ttyFlag = @()
if ([Environment]::UserInteractive -and -not [Console]::IsInputRedirected) {
    $ttyFlag = @('-t', '-i')
}

$runCommand = @(
    'container', 'run'
    '--name', 'lgtm'
)

# Append OBI-related flags (if any) so each flag is a separate argument
if ($obiFlags.Count -gt 0) {
    $runCommand += $obiFlags
}

# Append the remaining fixed arguments
$runCommand += @(
    '-p', '3000:3000'
    '-p', '4040:4040'
    '-p', '4317:4317'
    '-p', '4318:4318'
    '-p', '9090:9090'
    '--rm'
)

$runCommand += $ttyFlag

$runCommand += @(
    '-v', "${path}/container/grafana:/data/grafana"
    '-v', "${path}/container/prometheus:/data/prometheus"
    '-v', "${path}/container/loki:/data/loki"
    '-e', "GF_PATHS_DATA=/data/grafana"
    '--env-file', '.env'
    ${image}
)

& $containerCommand @runCommand
```

## File: `run-lgtm.sh`
```bash
#!/bin/bash

set -euo pipefail

RELEASE=${1:-latest}
LOCAL_VOLUME=${PWD}/container
# Only set this to "true" if you built the image with the 'build-lgtm.sh' script
USE_LOCAL_IMAGE=${2:-false}

for dir in grafana prometheus loki; do
	test -d "${LOCAL_VOLUME}"/${dir} || mkdir -p "${LOCAL_VOLUME}"/${dir}
done

test -f .env || touch .env

# Check if OBI is enabled (from environment or .env file)
OBI_FLAGS=()
OBI_ENV_FLAGS=()
if [[ ${ENABLE_OBI:-} == "true" ]] || grep -qE '^ENABLE_OBI=true$' .env 2>/dev/null; then
	echo "OBI eBPF auto-instrumentation enabled. Adding --pid=host --privileged flags."
	OBI_FLAGS=(--pid=host --privileged)
	# Forward OBI-specific env vars into the container (they are not in .env by default).
	# General OTLP vars (OTEL_EXPORTER_OTLP_ENDPOINT, etc.) are forwarded via --env-file .env.
	OBI_ENV_FLAGS=(-e ENABLE_OBI=true)
	for var in $(compgen -v | grep -E '^(OBI_TARGET|OTEL_EBPF_|ENABLE_LOGS_OBI)' | grep -vE '^(OBI_FLAGS|OBI_ENV_FLAGS)$'); do
		OBI_ENV_FLAGS+=(-e "$var=${!var}")
	done
fi

# Allocate TTY only if stdin is a terminal
TTY_FLAGS=()
if test -t 0; then
	TTY_FLAGS=(-t -i)
fi

if command -v podman >/dev/null 2>&1; then
	RUNTIME=podman
	# Fedora, by default, runs with SELinux on. We require the "z" option for bind mounts.
	# See: https://docs.docker.com/engine/storage/bind-mounts/#configure-the-selinux-label
	# See: https://docs.podman.io/en/stable/markdown/podman-run.1.html section "Labeling Volume Mounts"
	MOUNT_OPTS="rw,z"
elif command -v docker >/dev/null 2>&1; then
	RUNTIME=docker
	MOUNT_OPTS=rw
else
	echo "Unable to find a suitable container runtime such as Podman or Docker. Exiting."
	exit 1
fi

if [ "$USE_LOCAL_IMAGE" = true ]; then
	if [ "$RUNTIME" = "podman" ]; then
		# Default address when building with Podman.
		IMAGE="localhost/grafana/otel-lgtm:latest"
	else
		IMAGE="grafana/otel-lgtm:latest"
	fi
else
	IMAGE="docker.io/grafana/otel-lgtm:${RELEASE}"
	$RUNTIME image pull "$IMAGE"
fi

$RUNTIME container run \
	--name lgtm \
	"${OBI_FLAGS[@]}" \
	"${OBI_ENV_FLAGS[@]}" \
	-p 3000:3000 \
	-p 4040:4040 \
	-p 4317:4317 \
	-p 4318:4318 \
	-p 9090:9090 \
	--rm \
	"${TTY_FLAGS[@]}" \
	-v "${LOCAL_VOLUME}"/grafana:/data/grafana:"${MOUNT_OPTS}" \
	-v "${LOCAL_VOLUME}"/prometheus:/data/prometheus:"${MOUNT_OPTS}" \
	-v "${LOCAL_VOLUME}"/loki:/data/loki:"${MOUNT_OPTS}" \
	-e GF_PATHS_DATA=/data/grafana \
	--env-file .env \
	"$IMAGE"
```

## File: `docker/Dockerfile`
```
ARG LGTM_VERSION=development
# renovate: datasource=github-releases depName=grafana packageName=grafana/grafana
ARG GRAFANA_VERSION=v12.4.2
# renovate: datasource=github-releases depName=prometheus packageName=prometheus/prometheus
ARG PROMETHEUS_VERSION=v3.10.0
# renovate: datasource=github-releases depName=tempo packageName=grafana/tempo
ARG TEMPO_VERSION=v2.10.3
# renovate: datasource=github-releases depName=loki packageName=grafana/loki
ARG LOKI_VERSION=v3.7.1
# renovate: datasource=github-releases depName=pyroscope packageName=grafana/pyroscope
ARG PYROSCOPE_VERSION=v1.19.1
# renovate: datasource=github-releases depName=opentelemetry-collector packageName=open-telemetry/opentelemetry-collector-releases
ARG OPENTELEMETRY_COLLECTOR_VERSION=v0.147.0
# renovate: datasource=github-releases depName=obi packageName=open-telemetry/opentelemetry-ebpf-instrumentation
ARG OBI_VERSION=v0.6.0

# hadolint global ignore=DL3059
FROM docker.io/otel/ebpf-instrument:${OBI_VERSION} AS obi-source

# Download and extract components on the build platform (no QEMU) to avoid tar/rpm
# failures that occur under QEMU emulation with overlayfs. The download scripts use
# TARGETARCH to fetch the correct platform-specific archives.
# hadolint ignore=DL3033
FROM --platform=$BUILDPLATFORM docker.io/redhat/ubi9:9.7@sha256:9e6e193bfc3596a84d2a32f42d6b1552398ec9735b9a4e893a0fc3c6fbccb381 AS downloader

RUN mkdir /otel-lgtm

RUN yum install -y unzip jq

COPY detect-arch.sh \
 download-grafana.sh \
 download-prometheus.sh \
 download-tempo.sh \
 download-loki.sh \
 download-pyroscope.sh \
 download-otelcol.sh \
 install-cosign.sh \
 ./

# TARGETARCH is automatically detected and set by the Docker daemon during the build process. If the build starts
# on an amd64 architecture, then the TARGETARCH will be set to `amd64`.
# More details on the variables can be found here: https://docs.docker.com/desktop/extensions-sdk/extensions/multi-arch/
ARG TARGETARCH
ENV TARGETARCH=${TARGETARCH}

# renovate: datasource=github-releases depName=cosign packageName=sigstore/cosign
ARG COSIGN_VERSION=v3.0.5

RUN ./install-cosign.sh $COSIGN_VERSION

ARG GRAFANA_VERSION
ARG PROMETHEUS_VERSION
ARG TEMPO_VERSION
ARG LOKI_VERSION
ARG PYROSCOPE_VERSION
ARG OPENTELEMETRY_COLLECTOR_VERSION

RUN ./download-grafana.sh $GRAFANA_VERSION
RUN ./download-prometheus.sh $PROMETHEUS_VERSION
RUN ./download-tempo.sh $TEMPO_VERSION
RUN ./download-loki.sh $LOKI_VERSION
RUN ./download-pyroscope.sh $PYROSCOPE_VERSION
RUN ./download-otelcol.sh $OPENTELEMETRY_COLLECTOR_VERSION

FROM docker.io/redhat/ubi9:9.7@sha256:9e6e193bfc3596a84d2a32f42d6b1552398ec9735b9a4e893a0fc3c6fbccb381 AS builder

RUN mkdir /otel-lgtm

COPY prometheus.yaml \
 run-prometheus.sh \
 grafana-dashboard-red-metrics-classic.json \
 grafana-dashboard-red-metrics-native.json \
 grafana-dashboard-jvm-metrics.json \
 logging.sh \
 run-grafana.sh \
 loki-config.yaml \
 run-loki.sh \
 tempo-config.yaml \
 run-tempo.sh \
 pyroscope-config.yaml \
 run-pyroscope.sh \
 obi-config.yaml \
 run-obi.sh \
 otelcol-config*.yaml \
 run-otelcol.sh \
 run-all.sh \
 /otel-lgtm/

# hadolint ignore=DL3033
RUN yum install -y dos2unix

# installs for the final image
# see https://github.com/thomasdarimont/keycloak/blob/main/docs/guides/server/containers.adoc#installing-additional-rpm-packages
# Use tsflags=noscripts to skip RPM scriptlets that need /bin/sh inside the installroot,
# which fails under QEMU emulation (arm64 cross-build). CA certs come from the builder image.
RUN mkdir -p /mnt/rootfs
RUN dnf install --installroot /mnt/rootfs curl-minimal --releasever 9 --setopt install_weak_deps=false --setopt tsflags=noscripts --nodocs -y && \
    dnf --installroot /mnt/rootfs clean all && \
    rpm --root /mnt/rootfs -e --nodeps setup

# hadolint ignore=SC2038,DL4006
RUN find /otel-lgtm/ -maxdepth 1 -type f | xargs dos2unix

COPY --from=downloader /otel-lgtm/ /otel-lgtm/
COPY --from=obi-source /obi /otel-lgtm/obi/obi

COPY grafana-datasources.yaml /otel-lgtm/grafana/conf/provisioning/datasources/
COPY grafana-dashboards.yaml /otel-lgtm/grafana/conf/provisioning/dashboards/

FROM docker.io/redhat/ubi9-micro:9.7@sha256:2173487b3b72b1a7b11edc908e9bbf1726f9df46a4f78fd6d19a2bab0a701f38

RUN mkdir /otel-lgtm
WORKDIR /otel-lgtm

# Make the healthcheck script executable.
COPY healthcheck.sh /otel-lgtm/docker/healthcheck.sh
RUN chmod +x /otel-lgtm/docker/healthcheck.sh
HEALTHCHECK --interval=30s --timeout=5s --retries=3 CMD [ "/otel-lgtm/docker/healthcheck.sh" ]

COPY --from=builder /mnt/rootfs /
# to send telemetry to an external server
COPY --from=builder /etc/pki /etc/pki

COPY --from=builder /otel-lgtm /otel-lgtm

# just for displaying the version in the startup message
ARG LGTM_VERSION
ARG GRAFANA_VERSION
ARG PROMETHEUS_VERSION
ARG TEMPO_VERSION
ARG LOKI_VERSION
ARG PYROSCOPE_VERSION
ARG OBI_VERSION
ARG OPENTELEMETRY_COLLECTOR_VERSION
ENV LGTM_VERSION=${LGTM_VERSION}
ENV GRAFANA_VERSION=${GRAFANA_VERSION}
ENV PROMETHEUS_VERSION=${PROMETHEUS_VERSION}
ENV TEMPO_VERSION=${TEMPO_VERSION}
ENV LOKI_VERSION=${LOKI_VERSION}
ENV PYROSCOPE_VERSION=${PYROSCOPE_VERSION}
ENV OBI_VERSION=${OBI_VERSION}
ENV OPENTELEMETRY_COLLECTOR_VERSION=${OPENTELEMETRY_COLLECTOR_VERSION}

# Re-label the final image, overriding any existing labels from the base image
LABEL description="An open source backend for OpenTelemetry that's intended for development, demo, and testing environments."
LABEL io.k8s.description="An open source backend for OpenTelemetry that's intended for development, demo, and testing environments."
LABEL io.k8s.display-name="Grafana LGTM"
LABEL maintainer="Grafana Labs"
LABEL name="grafana/otel-lgtm"
LABEL org.opencontainers.image.authors="Grafana Labs"
LABEL org.opencontainers.image.documentation="https://github.com/grafana/docker-otel-lgtm/blob/main/README.md"
LABEL org.opencontainers.image.vendor="Grafana Labs"
LABEL org.opencontainers.image.title="Grafana OpenTelemetry LGTM"
LABEL org.opencontainers.image.source="https://github.com/grafana/docker-otel-lgtm"
LABEL summary="An OpenTelemetry backend in a Docker image"
LABEL url="https://github.com/grafana/docker-otel-lgtm"
LABEL vendor="Grafana Labs"

# Blank out labels inherited from the base image that we don't want
LABEL build-date=""
LABEL cpe=""
LABEL io.buildah.version=""
LABEL release=""

CMD ["/otel-lgtm/run-all.sh"]
```

## File: `docker/detect-arch.sh`
```bash
#!/bin/bash
# Detect TARGETARCH when not set by buildx (e.g. plain `docker build`)

if [[ -z "${TARGETARCH:-}" ]]; then
	case "$(uname -m)" in
	x86_64) TARGETARCH="amd64" ;;
	aarch64 | arm64) TARGETARCH="arm64" ;;
	*)
		echo "Unsupported architecture: $(uname -m)"
		exit 1
		;;
	esac
	export TARGETARCH
fi
```

## File: `docker/download-grafana.sh`
```bash
#!/bin/bash

set -euo pipefail

VERSION=${1:-}
if [[ -z "${VERSION}" ]]; then
	echo "Usage: $0 <version>"
	exit 1
fi

source ./detect-arch.sh

API_URL="https://grafana.com/api/downloads/grafana/versions/${VERSION:1}/packages/${TARGETARCH}/linux"
API_RESPONSE=$(curl -fsL "${API_URL}" -H 'accept: application/json')
DOWNLOAD_URL=$(echo "${API_RESPONSE}" | jq -r '.url')
CHECKSUM=$(echo "${API_RESPONSE}" | jq -r '.sha256')
ARCHIVE=$(basename "${DOWNLOAD_URL}")

curl -fsOL "${DOWNLOAD_URL}"
echo "${CHECKSUM} ${ARCHIVE}" | sha256sum -c
tar xfz "${ARCHIVE}"
EXTRACTED_DIR=$(tar -tzf "${ARCHIVE}" | head -1 | cut -f1 -d"/" || true)
mv "${EXTRACTED_DIR}" /otel-lgtm/grafana/
```

## File: `docker/download-loki.sh`
```bash
#!/bin/bash

set -euo pipefail

VERSION=${1:-}
if [[ -z "${VERSION}" ]]; then
	echo "Usage: $0 <version>"
	exit 1
fi

source ./detect-arch.sh

ARCHIVE=loki-linux-"${TARGETARCH}".zip
curl -sOL https://github.com/grafana/loki/releases/download/"${VERSION}"/SHA256SUMS
curl -sOL https://github.com/grafana/loki/releases/download/"${VERSION}"/"${ARCHIVE}"
sha256sum -c SHA256SUMS --ignore-missing
mkdir /otel-lgtm/loki
unzip "${ARCHIVE}" -d /loki/
mv loki/loki-linux-"${TARGETARCH}" /otel-lgtm/loki/loki
```

## File: `docker/download-otelcol.sh`
```bash
#!/bin/bash

set -euo pipefail

VERSION=${1:-}
if [[ -z "${VERSION}" ]]; then
	echo "Usage: $0 <version>"
	exit 1
fi

source ./detect-arch.sh

ARCHIVE=otelcol-contrib_"${VERSION:1}"_linux_"${TARGETARCH}".tar.gz
URL=https://github.com/open-telemetry/opentelemetry-collector-releases/releases/download/"${VERSION}"/"${ARCHIVE}"
curl -sOL "${URL}".sig
curl -sOL "${URL}".pem
curl -sOL "${URL}"
cosign verify-blob \
	--certificate-identity-regexp github.com/open-telemetry/opentelemetry-collector-releases \
	--certificate-oidc-issuer https://token.actions.githubusercontent.com \
	--certificate "${ARCHIVE}".pem \
	--signature "${ARCHIVE}".sig \
	"${ARCHIVE}"
mkdir /otel-lgtm/otelcol-contrib
tar xfz "${ARCHIVE}" -C /otel-lgtm/otelcol-contrib/
```

## File: `docker/download-prometheus.sh`
```bash
#!/bin/bash

set -euo pipefail

VERSION=${1:-}
if [[ -z "${VERSION}" ]]; then
	echo "Usage: $0 <version>"
	exit 1
fi

source ./detect-arch.sh

ARCHIVE=prometheus-"${VERSION:1}".linux-"${TARGETARCH}"
curl -sOL https://github.com/prometheus/prometheus/releases/download/"${VERSION}"/sha256sums.txt
curl -sOL https://github.com/prometheus/prometheus/releases/download/"${VERSION}"/"${ARCHIVE}".tar.gz
sha256sum -c sha256sums.txt --ignore-missing
tar xfz "${ARCHIVE}".tar.gz
mv "${ARCHIVE}" /otel-lgtm/prometheus
```

## File: `docker/download-pyroscope.sh`
```bash
#!/bin/bash

set -euo pipefail

VERSION=${1:-}
if [[ -z "${VERSION}" ]]; then
	echo "Usage: $0 <version>"
	exit 1
fi

source ./detect-arch.sh

ARCHIVE=pyroscope_"${VERSION:1}"_linux_"${TARGETARCH}".tar.gz
curl -sOL https://github.com/grafana/pyroscope/releases/download/"${VERSION}"/checksums.txt
curl -sOL https://github.com/grafana/pyroscope/releases/download/"${VERSION}"/"${ARCHIVE}"
sha256sum -c checksums.txt --ignore-missing
mkdir /otel-lgtm/pyroscope
tar xfz "${ARCHIVE}" -C /otel-lgtm/pyroscope/
```

## File: `docker/download-tempo.sh`
```bash
#!/bin/bash

set -euo pipefail

VERSION=${1:-}
if [[ -z "${VERSION}" ]]; then
	echo "Usage: $0 <version>"
	exit 1
fi

source ./detect-arch.sh

ARCHIVE=tempo_"${VERSION:1}"_linux_"${TARGETARCH}".tar.gz
curl -sOL https://github.com/grafana/tempo/releases/download/"${VERSION}"/SHA256SUMS
curl -sOL https://github.com/grafana/tempo/releases/download/"${VERSION}"/"${ARCHIVE}"
sha256sum -c SHA256SUMS --ignore-missing
mkdir /otel-lgtm/tempo
tar xfz "${ARCHIVE}" -C /otel-lgtm/tempo/
```

## File: `docker/grafana-dashboard-jvm-metrics.json`
```json
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
  "description": "Dashboard for JVM metrics with OpenTelemetry instrumentation",
  "editable": true,
  "fiscalYearStartMonth": 0,
  "gnetId": 18812,
  "graphTooltip": 0,
  "links": [
    {
      "asDropdown": false,
      "icon": "info",
      "includeVars": false,
      "keepTime": false,
      "tags": [],
      "targetBlank": false,
      "title": "Semantic Conventions: 1.20.0 - 1.22.0",
      "tooltip": "multiple versions of the semantic conventions are supported using 'or' and regex queries",
      "type": "link",
      "url": "https://github.com/open-telemetry/semantic-conventions/blob/main/schemas/1.20.0"
    }
  ],
  "liveNow": false,
  "panels": [
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${datasource}"
      },
      "description": "HTTP server request rate",
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
                "color": "green",
                "value": null
              },
              {
                "color": "red",
                "value": 80
              }
            ]
          },
          "unit": "reqps"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 8,
        "w": 4,
        "x": 0,
        "y": 0
      },
      "id": 51,
      "options": {
        "legend": {
          "calcs": [],
          "displayMode": "list",
          "placement": "bottom",
          "showLegend": true
        },
        "tooltip": {
          "mode": "single",
          "sort": "none"
        }
      },
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${datasource}"
          },
          "editorMode": "code",
          "expr": "sum by (instance) (rate({__name__=~\"http_server_request_duration_seconds_count|http_server_request_duration_count|http_server_duration_seconds_count|http_server_duration_count|http_server_duration_milliseconds_count|http_server_requests_milliseconds_count|http_server_requests_count|http_server_requests_seconds_count\", job=~\"$job\", instance=~\"$instance\"}[$__rate_interval]))",
          "instant": false,
          "legendFormat": "__auto",
          "range": true,
          "refId": "A"
        }
      ],
      "title": "Rate",
      "type": "timeseries"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${datasource}"
      },
      "description": "HTTP server error ratio - ratio of requests that return 5xx",
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
                "color": "green",
                "value": null
              },
              {
                "color": "red",
                "value": 80
              }
            ]
          },
          "unit": "percentunit"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 8,
        "w": 5,
        "x": 4,
        "y": 0
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
          "mode": "single",
          "sort": "none"
        }
      },
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${datasource}"
          },
          "editorMode": "code",
          "expr": "(sum by (instance)(rate({__name__=~\"http_server_request_duration_seconds_count|http_server_request_duration_count\", job=~\"$job\", instance=~\"$instance\", http_response_status_code=~\"5.*\"}[$__rate_interval]))) / on (instance) (sum by (instance)(rate({__name__=~\"http_server_request_duration_seconds_count|http_server_request_duration_count\", job=~\"$job\", instance=~\"$instance\"}[$__rate_interval])))\nor\n(sum by (instance)(rate({__name__=~\"http_server_duration_milliseconds_count|http_server_duration_seconds_count|http_server_duration_count\", job=~\"$job\", instance=~\"$instance\", http_status_code=~\"5.*\"}[$__rate_interval]))) / on (instance) (sum by (instance)(rate({__name__=~\"http_server_duration_milliseconds_count|http_server_duration_seconds_count|http_server_duration_count\", job=~\"$job\", instance=~\"$instance\"}[$__rate_interval])))\nor\n(sum by (instance)(rate({__name__=~\"http_server_requests_milliseconds_count|http_server_requests_count|http_server_requests_seconds_count\", job=~\"$job\", instance=~\"$instance\", outcome=\"SERVER_ERROR\"}[$__rate_interval]))) / on (instance) (sum by (instance)(rate({__name__=~\"http_server_requests_milliseconds_count|http_server_requests_count|http_server_requests_seconds_count\", job=~\"$job\", instance=~\"$instance\"}[$__rate_interval])))\n",
          "instant": false,
          "legendFormat": "__auto",
          "range": true,
          "refId": "A"
        }
      ],
      "title": "Error %",
      "type": "timeseries"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${datasource}"
      },
      "description": "95th percentile of HTTP server request duration in seconds",
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
                "color": "green",
                "value": null
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
        "w": 5,
        "x": 9,
        "y": 0
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
          "mode": "single",
          "sort": "none"
        }
      },
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${datasource}"
          },
          "editorMode": "code",
          "expr": "(histogram_quantile(0.95, sum by(le, instance) (rate({__name__=~\"http_server_request_duration_seconds_bucket|http_server_request_duration_bucket|http_server_duration_seconds_bucket|http_server_duration_bucket|http_server_requests_seconds_bucket\", job=~\"$job\", instance=~\"$instance\"}[$__rate_interval]))))\nor\n(histogram_quantile(0.95, sum by(le, instance) (rate({__name__=~\"http_server_duration_milliseconds_bucket|http_server_requests_milliseconds_bucket|http_server_requests_bucket\", job=~\"$job\", instance=~\"$instance\"}[$__rate_interval]))) / 1000)\n",
          "instant": false,
          "legendFormat": "{{instance}}",
          "range": true,
          "refId": "A"
        }
      ],
      "title": "Duration (95%)",
      "type": "timeseries"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${datasource}"
      },
      "description": "CPU utilization for the whole system",
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
                "color": "green",
                "value": null
              },
              {
                "color": "red",
                "value": 80
              }
            ]
          },
          "unit": "percentunit"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 7,
        "w": 7,
        "x": 0,
        "y": 8
      },
      "id": 38,
      "options": {
        "legend": {
          "calcs": [],
          "displayMode": "list",
          "placement": "bottom",
          "showLegend": true
        },
        "tooltip": {
          "mode": "multi",
          "sort": "desc"
        }
      },
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${datasource}"
          },
          "editorMode": "code",
          "expr": "{__name__=~\"jvm_cpu_recent_utilization|jvm_cpu_recent_utilization_ratio|process_runtime_jvm_system_cpu_utilization|process_runtime_jvm_system_cpu_utilization_ratio|system_cpu_usage\", job=~\"$job\", instance=~\"$instance\"}",
          "legendFormat": "{{instance}}",
          "range": true,
          "refId": "A"
        }
      ],
      "title": "CPU utilization",
      "type": "timeseries"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${datasource}"
      },
      "description": "Used heap memory / heap memory limit ",
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
                "color": "green",
                "value": null
              },
              {
                "color": "red",
                "value": 80
              }
            ]
          },
          "unit": "percentunit"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 7,
        "w": 7,
        "x": 7,
        "y": 8
      },
      "id": 30,
      "options": {
        "legend": {
          "calcs": [],
          "displayMode": "list",
          "placement": "bottom",
          "showLegend": true
        },
        "tooltip": {
          "mode": "multi",
          "sort": "none"
        }
      },
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${datasource}"
          },
          "editorMode": "code",
          "expr": "(sum by (instance) ({__name__=~\"jvm_memory_used|jvm_memory_used_bytes\",job=~\"$job\",jvm_memory_type=\"heap\", instance=~\"$instance\"}) / on(instance) sum by (instance) ({__name__=~\"jvm_memory_limit|jvm_memory_limit_bytes\",job=~\"$job\",jvm_memory_type=\"heap\", instance=~\"$instance\"}))\nor\n(sum by (instance) ({__name__=~\"process_runtime_jvm_memory_usage|process_runtime_jvm_memory_usage_bytes\",job=~\"$job\",type=\"heap\", instance=~\"$instance\"}) / on(instance) sum by (instance) ({__name__=~\"process_runtime_jvm_memory_limit|process_runtime_jvm_memory_limit_bytes\",job=~\"$job\",type=\"heap\", instance=~\"$instance\"}))\nor\n(sum by (instance) ({__name__=~\"jvm_memory_used|jvm_memory_used_bytes\",job=~\"$job\",area=\"heap\", instance=~\"$instance\"}) / on(instance) sum by (instance) ({__name__=~\"jvm_memory_max|jvm_memory_max_bytes\",job=~\"$job\",area=\"heap\", instance=~\"$instance\"}))",
          "legendFormat": "{{instance}}",
          "range": true,
          "refId": "A"
        }
      ],
      "title": "Heap Memory utilization",
      "type": "timeseries"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${datasource}"
      },
      "description": "Percentage of time spend for garbage collection pauses",
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
                "color": "green",
                "value": null
              }
            ]
          },
          "unit": "percentunit"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 7,
        "w": 4,
        "x": 0,
        "y": 15
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
          "mode": "single",
          "sort": "none"
        }
      },
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${datasource}"
          },
          "editorMode": "code",
          "expr": "(sum by(instance) (rate({__name__=~\"jvm_gc_duration_sum|jvm_gc_duration_seconds_sum|process_runtime_jvm_gc_duration_sum|process_runtime_jvm_gc_duration_seconds_sum|jvm_gc_pause_sum|jvm_gc_pause_seconds_sum\",job=~\"$job\", instance=~\"$instance\"}[$__rate_interval])))\nor\n(sum by(instance) (rate(jvm_gc_pause_milliseconds_sum{job=~\"$job\", instance=~\"$instance\"}[$__rate_interval])) / 1000)",
          "hide": false,
          "legendFormat": "__auto",
          "range": true,
          "refId": "B"
        }
      ],
      "title": "Garbage Collection",
      "type": "timeseries"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${datasource}"
      },
      "description": "Number of currently loaded classes",
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
                "color": "green",
                "value": null
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
        "h": 7,
        "w": 5,
        "x": 4,
        "y": 15
      },
      "id": 33,
      "options": {
        "legend": {
          "calcs": [],
          "displayMode": "list",
          "placement": "bottom",
          "showLegend": true
        },
        "tooltip": {
          "mode": "multi",
          "sort": "none"
        }
      },
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${datasource}"
          },
          "editorMode": "code",
          "expr": "{__name__=~\"jvm_class_count|process_runtime_jvm_classes_current_loaded|jvm_classes_loaded\",job=~\"$job\", instance=~\"$instance\"}",
          "legendFormat": "{{instance}}",
          "range": true,
          "refId": "A"
        }
      ],
      "title": "Classes",
      "type": "timeseries"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${datasource}"
      },
      "description": "Number of currently executing (also called \"live\") threads",
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
                "color": "green",
                "value": null
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
        "h": 7,
        "w": 5,
        "x": 9,
        "y": 15
      },
      "id": 42,
      "options": {
        "legend": {
          "calcs": [],
          "displayMode": "list",
          "placement": "bottom",
          "showLegend": true
        },
        "tooltip": {
          "mode": "single",
          "sort": "none"
        }
      },
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${datasource}"
          },
          "editorMode": "code",
          "expr": "sum({__name__=~\"jvm_thread_count|process_runtime_jvm_threads_count|jvm_threads_live\",job=~\"$job\", instance=~\"$instance\"}) by (instance)",
          "legendFormat": "{{instance}}",
          "range": true,
          "refId": "A"
        }
      ],
      "title": "Threads",
      "type": "timeseries"
    }
  ],
  "refresh": "",
  "schemaVersion": 38,
  "tags": ["JVM", "open-telemetry", "Java", "otel", "opentelemetry", "otlp"],
  "templating": {
    "list": [
      {
        "current": {
          "selected": false,
          "text": "Prometheus",
          "value": "prometheus"
        },
        "description": "Choose a Prometheus data source",
        "hide": 0,
        "includeAll": false,
        "label": "Data source",
        "multi": false,
        "name": "datasource",
        "options": [],
        "query": "prometheus",
        "queryValue": "",
        "refresh": 1,
        "regex": "",
        "skipUrlSync": false,
        "type": "datasource"
      },
      {
        "allValue": ".+",
        "current": {
          "selected": false,
          "text": "All",
          "value": "$__all"
        },
        "datasource": {
          "type": "prometheus",
          "uid": "${datasource}"
        },
        "definition": "label_values({__name__=~\"jvm_class_count|process_runtime_jvm_classes_current_loaded|jvm_classes_loaded\"},job)",
        "hide": 0,
        "includeAll": true,
        "label": "Job",
        "multi": true,
        "name": "job",
        "options": [],
        "query": {
          "query": "label_values({__name__=~\"jvm_class_count|process_runtime_jvm_classes_current_loaded|jvm_classes_loaded\"},job)",
          "refId": "PrometheusVariableQueryEditor-VariableQuery"
        },
        "refresh": 2,
        "regex": "",
        "skipUrlSync": false,
        "sort": 1,
        "tagValuesQuery": "",
        "tagsQuery": "",
        "type": "query",
        "useTags": false
      },
      {
        "allValue": ".+",
        "current": {
          "selected": false,
          "text": "All",
          "value": "$__all"
        },
        "datasource": {
          "type": "prometheus",
          "uid": "${datasource}"
        },
        "definition": "label_values({__name__=~\"(jvm_class_count|process_runtime_jvm_classes_current_loaded|jvm_classes_loaded)\", job=~\"$job\"},instance)",
        "description": "The instance of the application, e.g. pod1",
        "hide": 0,
        "includeAll": true,
        "label": "Instance",
        "multi": true,
        "name": "instance",
        "options": [],
        "query": {
          "query": "label_values({__name__=~\"(jvm_class_count|process_runtime_jvm_classes_current_loaded|jvm_classes_loaded)\", job=~\"$job\"},instance)",
          "refId": "PrometheusVariableQueryEditor-VariableQuery"
        },
        "refresh": 2,
        "regex": "",
        "skipUrlSync": false,
        "sort": 1,
        "tagValuesQuery": "",
        "tagsQuery": "",
        "type": "query",
        "useTags": false
      }
    ]
  },
  "time": {
    "from": "now-1h",
    "to": "now"
  },
  "timepicker": {
    "refresh_intervals": ["5s", "10s", "30s", "1m", "5m", "15m", "30m", "1h", "2h", "1d"],
    "time_options": ["5m", "15m", "1h", "6h", "12h", "24h", "2d", "7d", "30d"]
  },
  "timezone": "",
  "title": "JVM Overview (OpenTelemetry)",
  "uid": "b91844d7-121e-4d0a-93b8-a9c1a05703b3",
  "version": 1,
  "weekStart": ""
}
```

## File: `docker/grafana-dashboard-red-metrics-classic.json`
```json
{
  "annotations": {
    "list": [
      {
        "builtIn": 1,
        "datasource": {
          "type": "grafana",
          "uid": "-- Grafana --"
        },
        "enable": true,
        "hide": true,
        "iconColor": "rgba(0, 211, 255, 1)",
        "name": "Annotations & Alerts",
        "type": "dashboard"
      }
    ]
  },
  "description": "request rate, error rate, duration",
  "editable": true,
  "fiscalYearStartMonth": 0,
  "graphTooltip": 0,
  "id": 4,
  "links": [],
  "liveNow": false,
  "panels": [
    {
      "datasource": {
        "type": "datasource",
        "uid": "grafana"
      },
      "description": "",
      "gridPos": {
        "h": 5,
        "w": 12,
        "x": 0,
        "y": 0
      },
      "id": 6,
      "options": {
        "code": {
          "language": "plaintext",
          "showLineNumbers": false,
          "showMiniMap": false
        },
        "content": "# RED Metrics: (r)equest rate, (e)rror rate, (d)uration\n\nThis dashboard uses explicit bucket histograms and the stable [OpenTelemetry metrics semantic conventions](https://opentelemetry.io/docs/specs/semconv/general/metrics/).\nTo enable this for the [OpenTelemetry Java instrumentation agent](https://github.com/open-telemetry/opentelemetry-java-instrumentation/), set the following environment variables:\n\n```\nexport OTEL_EXPORTER_OTLP_METRICS_DEFAULT_HISTOGRAM_AGGREGATION=explicit_bucket_histogram\n```",
        "mode": "markdown"
      },
      "pluginVersion": "10.3.3",
      "type": "text"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "prometheus"
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
            "fillOpacity": 0,
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
          "unit": "reqps",
          "unitScale": true
        },
        "overrides": []
      },
      "gridPos": {
        "h": 8,
        "w": 12,
        "x": 0,
        "y": 5
      },
      "id": 1,
      "options": {
        "legend": {
          "calcs": [],
          "displayMode": "list",
          "placement": "bottom",
          "showLegend": true
        },
        "tooltip": {
          "mode": "single",
          "sort": "none"
        }
      },
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "prometheus"
          },
          "editorMode": "code",
          "expr": "sum(rate({__name__=~\"http_server_request_duration_seconds_count|http_server_request_duration_count|http_server_duration_milliseconds_count|http_server_duration_seconds_count|http_server_duration_count\", job=~\"$job\", instance=~\"$instance\"}[5m]))",
          "legendFormat": "__auto",
          "range": true,
          "refId": "A"
        }
      ],
      "title": "Request Rate",
      "type": "timeseries"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "prometheus"
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
            "fillOpacity": 0,
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
          "unit": "percentunit",
          "unitScale": true
        },
        "overrides": []
      },
      "gridPos": {
        "h": 8,
        "w": 12,
        "x": 0,
        "y": 13
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
          "mode": "single",
          "sort": "none"
        }
      },
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "prometheus"
          },
          "editorMode": "code",
          "expr": "sum(rate({__name__=~\"http_server_request_duration_seconds_count|http_server_request_duration_count|http_server_duration_milliseconds_count|http_server_duration_seconds_count|http_server_duration_count\", job=~\"$job\", instance=~\"$instance\", http_response_status_code=~\"5..\"}[5m])) / sum(rate({__name__=~\"http_server_request_duration_seconds_count|http_server_request_duration_count|http_server_duration_milliseconds_count|http_server_duration_seconds_count|http_server_duration_count\", job=~\"$job\", instance=~\"$instance\"}[5m]))",
          "legendFormat": "__auto",
          "range": true,
          "refId": "A"
        }
      ],
      "title": "Error Rate",
      "type": "timeseries"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "prometheus"
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
                "color": "green",
                "value": null
              },
              {
                "color": "red",
                "value": 80
              }
            ]
          },
          "unit": "reqps",
          "unitScale": true
        },
        "overrides": []
      },
      "gridPos": {
        "h": 8,
        "w": 12,
        "x": 0,
        "y": 21
      },
      "id": 3,
      "options": {
        "displayMode": "gradient",
        "maxVizHeight": 300,
        "minVizHeight": 10,
        "minVizWidth": 0,
        "namePlacement": "auto",
        "orientation": "auto",
        "reduceOptions": {
          "calcs": ["lastNotNull"],
          "fields": "",
          "values": false
        },
        "showUnfilled": true,
        "sizing": "auto",
        "valueMode": "color"
      },
      "pluginVersion": "10.3.3",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "prometheus"
          },
          "editorMode": "code",
          "exemplar": true,
          "expr": "sum by (le) (rate({__name__=~\"http_server_request_duration_seconds_bucket|http_server_request_duration_bucket|http_server_duration_milliseconds_bucket|http_server_duration_seconds_bucket|http_server_duration_bucket\", job=~\"$job\", instance=~\"$instance\"}[5m]))",
          "format": "heatmap",
          "instant": false,
          "legendFormat": "{{le}}",
          "range": true,
          "refId": "A"
        }
      ],
      "title": "Duration histogram (s)",
      "type": "bargauge"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "prometheus"
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
        "y": 29
      },
      "id": 5,
      "options": {
        "calculate": false,
        "cellGap": 1,
        "color": {
          "exponent": 0.5,
          "fill": "dark-orange",
          "mode": "scheme",
          "reverse": false,
          "scale": "exponential",
          "scheme": "Oranges",
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
          "show": true,
          "yHistogram": false
        },
        "yAxis": {
          "axisPlacement": "left",
          "reverse": false,
          "unit": "s"
        }
      },
      "pluginVersion": "10.2.0",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "prometheus"
          },
          "editorMode": "code",
          "exemplar": false,
          "expr": "sum by (le) (rate({__name__=~\"http_server_request_duration_seconds_bucket|http_server_request_duration_bucket|http_server_duration_milliseconds_bucket|http_server_duration_seconds_bucket|http_server_duration_bucket\", job=~\"$job\", instance=~\"$instance\"}[5m]))",
          "format": "heatmap",
          "instant": false,
          "range": true,
          "refId": "A"
        }
      ],
      "title": "Duration Heatmap",
      "type": "heatmap"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "prometheus"
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
            "fillOpacity": 0,
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
          "min": 0,
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
        "x": 0,
        "y": 37
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
          "mode": "single",
          "sort": "none"
        }
      },
      "pluginVersion": "9.5.1",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "prometheus"
          },
          "editorMode": "code",
          "exemplar": true,
          "expr": "histogram_quantile(0.95, sum by (le) (rate({__name__=~\"http_server_request_duration_seconds_bucket|http_server_request_duration_bucket|http_server_duration_milliseconds_bucket|http_server_duration_seconds_bucket|http_server_duration_bucket\", job=~\"$job\", instance=~\"$instance\"}[5m])))",
          "format": "time_series",
          "instant": false,
          "legendFormat": "95th",
          "range": true,
          "refId": "A"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "prometheus"
          },
          "editorMode": "code",
          "exemplar": true,
          "expr": "histogram_quantile(0.5, sum by (le) (rate({__name__=~\"http_server_request_duration_seconds_bucket|http_server_request_duration_bucket|http_server_duration_milliseconds_bucket|http_server_duration_seconds_bucket|http_server_duration_bucket\", job=~\"$job\", instance=~\"$instance\"}[5m])))",
          "hide": false,
          "legendFormat": "50th",
          "range": true,
          "refId": "B"
        }
      ],
      "title": "Duration percentiles",
      "type": "timeseries"
    }
  ],
  "refresh": "",
  "schemaVersion": 39,
  "tags": [],
  "templating": {
    "list": [
      {
        "allValue": ".+",
        "current": {
          "selected": true,
          "text": ["All"],
          "value": ["$__all"]
        },
        "datasource": {
          "type": "prometheus",
          "uid": "prometheus"
        },
        "definition": "label_values(job)",
        "hide": 0,
        "includeAll": true,
        "label": "",
        "multi": true,
        "name": "job",
        "options": [],
        "query": {
          "query": "label_values(job)",
          "refId": "PrometheusVariableQueryEditor-VariableQuery"
        },
        "refresh": 1,
        "regex": "",
        "skipUrlSync": false,
        "sort": 0,
        "type": "query"
      },
      {
        "allValue": ".+",
        "current": {
          "selected": true,
          "text": ["All"],
          "value": ["$__all"]
        },
        "datasource": {
          "type": "prometheus",
          "uid": "prometheus"
        },
        "definition": "label_values({job=~\"$job\"},instance)",
        "hide": 0,
        "includeAll": true,
        "label": "instance",
        "multi": true,
        "name": "instance",
        "options": [],
        "query": {
          "query": "label_values({job=~\"$job\"},instance)",
          "refId": "PrometheusVariableQueryEditor-VariableQuery"
        },
        "refresh": 1,
        "regex": "",
        "skipUrlSync": false,
        "sort": 0,
        "type": "query"
      }
    ]
  },
  "time": {
    "from": "now-30m",
    "to": "now"
  },
  "timepicker": {},
  "timezone": "",
  "title": "RED Metrics (classic histogram)",
  "uid": "f543a537-cb96-470d-a349-660ad1513136",
  "version": 1,
  "weekStart": ""
}
```

## File: `docker/grafana-dashboard-red-metrics-native.json`
```json
{
  "annotations": {
    "list": [
      {
        "builtIn": 1,
        "datasource": {
          "type": "grafana",
          "uid": "-- Grafana --"
        },
        "enable": true,
        "hide": true,
        "iconColor": "rgba(0, 211, 255, 1)",
        "name": "Annotations & Alerts",
        "type": "dashboard"
      }
    ]
  },
  "description": "request rate, error rate, duration",
  "editable": true,
  "fiscalYearStartMonth": 0,
  "graphTooltip": 0,
  "links": [],
  "liveNow": false,
  "panels": [
    {
      "datasource": {
        "type": "datasource",
        "uid": "grafana"
      },
      "description": "",
      "gridPos": {
        "h": 5,
        "w": 12,
        "x": 0,
        "y": 0
      },
      "id": 6,
      "options": {
        "code": {
          "language": "plaintext",
          "showLineNumbers": false,
          "showMiniMap": false
        },
        "content": "# RED Metrics: (r)equest rate, (e)rror rate, (d)uration\n\nThis dashboard uses exponential histograms and the stable [OpenTelemetry metrics semantic conventions](https://opentelemetry.io/docs/specs/semconv/general/metrics/).\nTo enable this for the [OpenTelemetry Java instrumentation agent](https://github.com/open-telemetry/opentelemetry-java-instrumentation/), set the following environment variables:\n\n```\nexport OTEL_EXPORTER_OTLP_METRICS_DEFAULT_HISTOGRAM_AGGREGATION=base2_exponential_bucket_histogram\n```",
        "mode": "markdown"
      },
      "pluginVersion": "10.3.3",
      "type": "text"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "prometheus"
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
            "fillOpacity": 0,
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
          "unit": "reqps",
          "unitScale": true
        },
        "overrides": []
      },
      "gridPos": {
        "h": 8,
        "w": 12,
        "x": 0,
        "y": 5
      },
      "id": 1,
      "options": {
        "legend": {
          "calcs": [],
          "displayMode": "list",
          "placement": "bottom",
          "showLegend": true
        },
        "tooltip": {
          "mode": "single",
          "sort": "none"
        }
      },
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "prometheus"
          },
          "editorMode": "code",
          "expr": "sum(histogram_count(rate({__name__=~\"http_server_request_duration_seconds|http_server_request_duration|http_server_duration_milliseconds|http_server_duration_seconds|http_server_duration\", job=~\"$job\", instance=~\"$instance\"}[5m])))",
          "legendFormat": "__auto",
          "range": true,
          "refId": "A"
        }
      ],
      "title": "Request Rate",
      "type": "timeseries"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "prometheus"
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
            "fillOpacity": 0,
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
          "unit": "percentunit",
          "unitScale": true
        },
        "overrides": []
      },
      "gridPos": {
        "h": 8,
        "w": 12,
        "x": 0,
        "y": 13
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
          "mode": "single",
          "sort": "none"
        }
      },
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "prometheus"
          },
          "editorMode": "code",
          "expr": "sum(histogram_count(rate({__name__=~\"http_server_request_duration_seconds|http_server_request_duration|http_server_duration_milliseconds|http_server_duration_seconds|http_server_duration\", job=~\"$job\", instance=~\"$instance\", http_response_status_code=~\"5..\"}[5m]))) / sum(histogram_count(rate({__name__=~\"http_server_request_duration_seconds|http_server_request_duration|http_server_duration_milliseconds|http_server_duration_seconds|http_server_duration\", job=~\"$job\", instance=~\"$instance\"}[5m])))\n\n",
          "legendFormat": "__auto",
          "range": true,
          "refId": "A"
        }
      ],
      "title": "Error Rate",
      "type": "timeseries"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "prometheus"
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
          },
          "unitScale": true
        },
        "overrides": []
      },
      "gridPos": {
        "h": 8,
        "w": 12,
        "x": 0,
        "y": 21
      },
      "id": 5,
      "options": {
        "calculate": false,
        "cellGap": 1,
        "color": {
          "exponent": 0.5,
          "fill": "dark-orange",
          "mode": "scheme",
          "reverse": false,
          "scale": "exponential",
          "scheme": "Oranges",
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
          "reverse": false,
          "unit": "s"
        }
      },
      "pluginVersion": "10.3.3",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "prometheus"
          },
          "editorMode": "code",
          "exemplar": true,
          "expr": "sum(rate({__name__=~\"http_server_request_duration_seconds|http_server_request_duration|http_server_duration_milliseconds|http_server_duration_seconds|http_server_duration\",job=~\"$job\", instance=~\"$instance\"}[5m]))",
          "format": "time_series",
          "instant": false,
          "range": true,
          "refId": "A"
        }
      ],
      "title": "Duration Heatmap",
      "type": "heatmap"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "prometheus"
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
            "fillOpacity": 0,
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
          "unit": "s",
          "unitScale": true
        },
        "overrides": []
      },
      "gridPos": {
        "h": 8,
        "w": 12,
        "x": 0,
        "y": 29
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
          "mode": "single",
          "sort": "none"
        }
      },
      "pluginVersion": "9.5.1",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "prometheus"
          },
          "editorMode": "code",
          "exemplar": true,
          "expr": "histogram_quantile(0.95, sum(rate({__name__=~\"http_server_request_duration_seconds|http_server_request_duration|http_server_duration_milliseconds|http_server_duration_seconds|http_server_duration\",job=~\"$job\", instance=~\"$instance\"}[5m])))",
          "format": "time_series",
          "instant": false,
          "legendFormat": "95th",
          "range": true,
          "refId": "A"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "prometheus"
          },
          "editorMode": "code",
          "exemplar": true,
          "expr": "histogram_quantile(0.5, sum(rate({__name__=~\"http_server_request_duration_seconds|http_server_request_duration|http_server_duration_milliseconds|http_server_duration_seconds|http_server_duration\",job=~\"$job\", instance=~\"$instance\"}[5m])))",
          "hide": false,
          "legendFormat": "50th",
          "range": true,
          "refId": "B"
        }
      ],
      "title": "Duration percentiles",
      "type": "timeseries"
    }
  ],
  "refresh": "",
  "schemaVersion": 39,
  "tags": [],
  "templating": {
    "list": [
      {
        "allValue": ".+",
        "current": {
          "selected": true,
          "text": ["All"],
          "value": ["$__all"]
        },
        "datasource": {
          "type": "prometheus",
          "uid": "prometheus"
        },
        "definition": "label_values(job)",
        "hide": 0,
        "includeAll": true,
        "label": "",
        "multi": true,
        "name": "job",
        "options": [],
        "query": {
          "query": "label_values(job)",
          "refId": "PrometheusVariableQueryEditor-VariableQuery"
        },
        "refresh": 1,
        "regex": "",
        "skipUrlSync": false,
        "sort": 0,
        "type": "query"
      },
      {
        "allValue": ".+",
        "current": {
          "selected": true,
          "text": ["All"],
          "value": ["$__all"]
        },
        "datasource": {
          "type": "prometheus",
          "uid": "prometheus"
        },
        "definition": "label_values({job=~\"$job\"},instance)",
        "hide": 0,
        "includeAll": true,
        "label": "instance",
        "multi": true,
        "name": "instance",
        "options": [],
        "query": {
          "query": "label_values({job=~\"$job\"},instance)",
          "refId": "PrometheusVariableQueryEditor-VariableQuery"
        },
        "refresh": 1,
        "regex": "",
        "skipUrlSync": false,
        "sort": 0,
        "type": "query"
      }
    ]
  },
  "time": {
    "from": "now-30m",
    "to": "now"
  },
  "timepicker": {},
  "timezone": "",
  "title": "RED Metrics (native histogram)",
  "uid": "f543a537-cb96-470d-a349-660ad1513135",
  "version": 1,
  "weekStart": ""
}
```

## File: `docker/grafana-dashboards.yaml`
```yaml
apiVersion: 1

providers:
  - name: "RED Metrics (classic histogram)"
    type: file
    options:
      path: /otel-lgtm/grafana-dashboard-red-metrics-classic.json
      foldersFromFilesStructure: false
  - name: "RED Metrics (exponential/native histogram)"
    type: file
    options:
      path: /otel-lgtm/grafana-dashboard-red-metrics-native.json
      foldersFromFilesStructure: false
  - name: "JVM Metrics"
    type: file
    options:
      path: /otel-lgtm/grafana-dashboard-jvm-metrics.json
      foldersFromFilesStructure: false
```

## File: `docker/grafana-datasources.yaml`
```yaml
apiVersion: 1

datasources:
  - name: Prometheus
    type: prometheus
    uid: prometheus
    url: http://127.0.0.1:9090
    editable: true
    jsonData:
      timeInterval: 60s
      exemplarTraceIdDestinations:
        - name: trace_id
          datasourceUid: tempo
          urlDisplayLabel: "Trace: $${__value.raw}"

  - name: Tempo
    type: tempo
    uid: tempo
    url: http://127.0.0.1:3200
    editable: true
    jsonData:
      tracesToLogsV2:
        customQuery: true
        datasourceUid: "loki"
        query: '{$${__tags}} | trace_id = "$${__trace.traceId}"'
        tags:
          - key: "service.name"
            value: "service_name"

      serviceMap:
        datasourceUid: "prometheus"
      search:
        hide: false
      nodeGraph:
        enabled: true
      lokiSearch:
        datasourceUid: "loki"

  - name: Loki
    type: loki
    uid: loki
    url: http://127.0.0.1:3100
    editable: true
    jsonData:
      derivedFields:
        - name: "trace_id"
          matcherType: "label"
          matcherRegex: "trace_id"
          url: "$${__value.raw}"
          datasourceUid: "tempo"
          urlDisplayLabel: "Trace: $${__value.raw}"

  - name: Pyroscope
    type: grafana-pyroscope-datasource
    uid: pyroscope
    url: http://127.0.0.1:4040
```

## File: `docker/healthcheck.sh`
```bash
#!/usr/bin/env sh

set -eu

check_service() {
	name=$1
	url=$2

	echo "Checking $name"

	set +e
	# check if port is listening
	curl -s "$url" >/dev/null 2>&1
	code=$?
	set -e

	if [ "$code" -eq 7 ]; then
		echo "$name not running (skipping)"
	elif [ "$code" -eq 0 ]; then
		echo "$name healthy"
	else
		echo "$name unhealthy"
		exit 1
	fi
}

check_service "Grafana" http://localhost:3000/api/health
check_service "Loki" http://localhost:3100/ready
check_service "Tempo" http://localhost:3200/ready
check_service "Mimir" http://localhost:9090/-/ready
check_service "OTel Collector" http://localhost:13133/ready

echo "All running services healthy"
exit 0
```

## File: `docker/install-cosign.sh`
```bash
#!/bin/bash

set -euo pipefail

VERSION=${1:-}
if [[ -z "${VERSION}" ]]; then
	echo "Usage: $0 <version>"
	exit 1
fi
VERSION="${VERSION:1}"

ARCH=$(uname -m)
if [[ "${ARCH}" == "x86_64" ]]; then
	ARCH="x86_64"
elif [[ "${ARCH}" == "aarch64" ]]; then
	ARCH="aarch64"
elif [[ "${ARCH}" == "arm64" ]]; then
	ARCH="aarch64"
else
	echo "Unsupported architecture: ${ARCH}"
	exit 1
fi
ARCHIVE=cosign-"${VERSION}"-1."${ARCH}".rpm

cd /tmp
curl -O -L https://github.com/sigstore/cosign/releases/download/v"${VERSION}"/"${ARCHIVE}"
curl -O -L https://github.com/sigstore/cosign/releases/download/v"${VERSION}"/cosign_checksums.txt
sha256sum -c cosign_checksums.txt --ignore-missing
yum install -y "${ARCHIVE}"
```

## File: `docker/logging.sh`
```bash
#!/bin/bash

set -euo pipefail

function run_with_logging() {
	name=$1
	shift
	envvar=$1
	shift
	if [[ ${envvar} == "true" || ${ENABLE_LOGS_ALL:-false} == "true" ]]; then
		echo "Running ${name} logging=true"
		exec "$@"
	else
		echo "Running ${name} logging=false"
		exec "$@" >/dev/null 2>&1
	fi
}
```

## File: `docker/loki-config.yaml`
```yaml
auth_enabled: false

server:
  http_listen_port: 3100

common:
  instance_addr: 127.0.0.1
  path_prefix: /data/loki
  storage:
    filesystem:
      chunks_directory: /data/loki/chunks
      rules_directory: /data/loki/rules
  replication_factor: 1
  ring:
    kvstore:
      store: inmemory

schema_config:
  configs:
    - from: 2020-10-24
      store: tsdb
      object_store: filesystem
      schema: v13
      index:
        prefix: index_
        period: 24h

ruler:
  alertmanager_url: http://127.0.0.1:9093

pattern_ingester:
  lifecycler:
    min_ready_duration: 1s

ingester:
  lifecycler:
    min_ready_duration: 1s

frontend:
  scheduler_dns_lookup_period: 1s
  address: 127.0.0.1

query_scheduler:
  use_scheduler_ring: false
```

## File: `docker/obi-config.yaml`
```yaml
ebpf:
  context_propagation: all

otel_traces_export:
  endpoint: http://127.0.0.1:4318

otel_metrics_export:
  endpoint: http://127.0.0.1:4318

prometheus_export:
  port: 6060
  path: /metrics
```

## File: `docker/otelcol-config.yaml`
```yaml
receivers:
  otlp:
    protocols:
      grpc:
        endpoint: 0.0.0.0:4317
      http:
        endpoint: 0.0.0.0:4318
        cors:
          allowed_origins:
            - http://*
  prometheus/collector:
    config:
      scrape_configs:
        - job_name: "opentelemetry-collector"
          scrape_interval: 1s
          static_configs:
            - targets: ["127.0.0.1:8888"]

extensions:
  health_check:
    endpoint: 0.0.0.0:13133
    path: "/ready"

processors:
  batch:

exporters:
  otlphttp/metrics:
    endpoint: http://127.0.0.1:9090/api/v1/otlp
    tls:
      insecure: true
  otlphttp/traces:
    endpoint: http://127.0.0.1:4418
    tls:
      insecure: true
  otlphttp/logs:
    endpoint: http://127.0.0.1:3100/otlp
    tls:
      insecure: true
  otlp/profiles:
    endpoint: http://127.0.0.1:4040
    tls:
      insecure: true
  debug/metrics:
    verbosity: detailed
  debug/traces:
    verbosity: detailed
  debug/logs:
    verbosity: detailed

service:
  extensions: [health_check]
  pipelines:
    traces:
      receivers: [otlp]
      processors: [batch]
      exporters: [otlphttp/traces]
      #exporters: [otlphttp/traces,debug/traces]
    metrics:
      receivers: [otlp, prometheus/collector]
      processors: [batch]
      exporters: [otlphttp/metrics]
      #exporters: [otlphttp/metrics,debug/metrics]
    logs:
      receivers: [otlp]
      processors: [batch]
      exporters: [otlphttp/logs]
      #exporters: [otlphttp/logs,debug/logs]
    profiles:
      receivers: [otlp]
      exporters: [otlp/profiles]
```

## File: `docker/prometheus.yaml`
```yaml
---
global:
  scrape_native_histograms: true
otlp:
  keep_identifying_resource_attributes: true
  # Recommended attributes to be promoted to labels.
  promote_resource_attributes:
    - service.instance.id
    - service.name
    - service.namespace
    - service.version
    - cloud.availability_zone
    - cloud.region
    - container.name
    - deployment.environment # backward compatibility
    - deployment.environment.name
    - k8s.cluster.name
    - k8s.container.name
    - k8s.cronjob.name
    - k8s.daemonset.name
    - k8s.deployment.name
    - k8s.job.name
    - k8s.namespace.name
    - k8s.node.name
    - k8s.pod.name
    - k8s.replicaset.name
    - k8s.statefulset.name
    - host.name
    - postgresql.database.name
    - postgresql.schema.name
    - postgresql.table.name
    - postgresql.index.name
    - database # used by otelcol/receiver/mongodb
    - kafka.cluster.alias
storage:
  tsdb:
    # A 10min time window is enough because it can easily absorb retries and network delays.
    out_of_order_time_window: 10m
```

## File: `docker/pyroscope-config.yaml`
```yaml
server:
  grpc_listen_port: 9097 # to avoid conflict with tempo

metastore:
  address: 127.0.0.1
  min_ready_duration: 1s

distributor:
  ring:
    kvstore:
      store: inmemory

ingester:
  lifecycler:
    address: 127.0.0.1
    ring:
      kvstore:
        store: inmemory
      replication_factor: 1
    min_ready_duration: 1s

pyroscopedb:
  data_path: "/data/pyroscope"
```

## File: `docker/run-all.sh`
```bash
#!/bin/bash

echo "Starting grafana/otel-lgtm ${LGTM_VERSION}"

# Graceful shutdown: forward SIGTERM/SIGINT to all background jobs
shutdown() {
	echo "Shutting down..."
	# Send SIGTERM to all background jobs (the wrapper scripts exec the
	# server process, so these PIDs are the actual server processes)
	jobs -p | xargs -r kill 2>/dev/null
	wait
	exit 0
}
trap shutdown SIGTERM SIGINT

# Record global start time
start_time_global=$(date +%s)

# Function to record start time for a component
start_component() {
	local component=$1
	local start_time
	start_time=$(date +%s)
	# Store start time in an associative array
	eval "start_time_${component}=${start_time}"
}

# Start all components and record their start times
start_component "grafana"
./run-grafana.sh &

start_component "loki"
./run-loki.sh &

start_component "otelcol"
./run-otelcol.sh &

start_component "prometheus"
./run-prometheus.sh &

start_component "tempo"
./run-tempo.sh &

start_component "pyroscope"
./run-pyroscope.sh &

if [[ ${ENABLE_OBI:-false} == "true" ]]; then
	start_component "obi"
	./run-obi.sh &
fi

echo "Waiting for the OpenTelemetry collector and the Grafana LGTM stack to start up..."

# Declare arrays to store service status and elapsed times
declare -A service_ready elapsed_times

# Define services and their health check URLs
declare -A services
services["grafana"]="http://127.0.0.1:3000/api/health"
services["loki"]="http://127.0.0.1:3100/ready"
services["prometheus"]="http://127.0.0.1:9090/api/v1/status/runtimeinfo"
services["tempo"]="http://127.0.0.1:3200/ready"
services["pyroscope"]="http://127.0.0.1:4040/ready"
services["otelcol"]="http://127.0.0.1:13133/ready"

# Initialize service_ready status to false for all services
for service in "${!services[@]}"; do
	service_ready[$service]=false
done

# Function to check if a service is ready
check_service_ready() {
	local service=$1
	local url=$2

	# Skip if service is already marked as ready
	if [[ ${service_ready[$service]} == true ]]; then
		return 0
	fi

	# Check if service is ready
	if [[ $(curl -o /dev/null -sg "${url}" -w "%{response_code}" 2>/dev/null) == "200" ]]; then
		# Calculate and display startup time
		end_time=$(date +%s)
		start_var="start_time_${service}"
		# shellcheck disable=SC1083,SC2086
		start_time=$(eval echo \${$start_var})
		elapsed=$((end_time - start_time))
		# Store the elapsed time in the array
		elapsed_times[$service]=$elapsed
		service_ready[$service]=true
		echo "${service^} is up and running. Startup time: ${elapsed} seconds"
		return 0
	fi

	return 1
}

# Wait for all services to be ready
all_ready=false
while [[ $all_ready == false ]]; do
	# Check each service
	for service in "${!services[@]}"; do
		check_service_ready "$service" "${services[$service]}"
	done

	# Check if all services are ready
	all_ready=true
	for service in "${!service_ready[@]}"; do
		if [[ ${service_ready[$service]} == false ]]; then
			all_ready=false
			break
		fi
	done

	# If not all ready, wait a second before trying again
	if [[ $all_ready == false ]]; then
		sleep 1
	fi
done

# Calculate total startup time
end_time_global=$(date +%s)
total_elapsed=$((end_time_global - start_time_global))

echo "Total startup time: ${total_elapsed} seconds"

# Print startup time summary
echo -e "\nStartup Time Summary:"
echo "---------------------"
echo "Grafana: ${elapsed_times[grafana]} seconds"
echo "Loki: ${elapsed_times[loki]} seconds"
echo "Prometheus: ${elapsed_times[prometheus]} seconds"
echo "Tempo: ${elapsed_times[tempo]} seconds"
echo "Pyroscope: ${elapsed_times[pyroscope]} seconds"
echo "OpenTelemetry collector: ${elapsed_times[otelcol]} seconds"
if [[ ${ENABLE_OBI:-false} == "true" ]]; then
	echo "OBI: (opt-in, not in health check)"
fi
echo "Total: ${total_elapsed} seconds"

touch /tmp/ready
echo "The OpenTelemetry collector and the Grafana LGTM stack are up and running. (created /tmp/ready)"

if [[ ${ENABLE_OBI:-false} == "true" ]]; then
	# Non-blocking check — don't delay readiness if OBI fails (e.g. missing capabilities)
	if curl -o /dev/null -sg "http://127.0.0.1:6060/metrics" -w "%{response_code}" 2>/dev/null | grep -q "200"; then
		echo "OBI is up and running."
	else
		echo "Warning: OBI internal metrics endpoint is not responding. This may indicate missing eBPF capabilities (--pid=host --privileged)."
	fi
	if [[ -n ${OBI_TARGET:-} ]]; then
		echo "OBI: monitoring '${OBI_TARGET}' processes"
	elif [[ -n ${OTEL_EBPF_AUTO_TARGET_EXE:-} ]]; then
		echo "OBI: monitoring processes matching executable name '${OTEL_EBPF_AUTO_TARGET_EXE}'"
	elif [[ -n ${OTEL_EBPF_OPEN_PORT:-} ]]; then
		echo "OBI: monitoring processes on ports ${OTEL_EBPF_OPEN_PORT}"
	else
		echo "OBI: monitoring processes on default open ports (80, 443, 8080-8099, 3000-3999, 5000-5999)"
	fi
fi

echo "Open ports:"
echo " - 4317: OpenTelemetry GRPC endpoint"
echo " - 4318: OpenTelemetry HTTP endpoint"
echo " - 3000: Grafana (http://localhost:3000). User: admin, password: admin"
echo " - 4040: Pyroscope endpoint"
echo " - 9090: Prometheus endpoint"

# Wait for signal; backgrounded sleep allows the trap to fire
sleep infinity &
wait $!
```

## File: `docker/run-grafana.sh`
```bash
#!/bin/bash

source ./logging.sh

# Respect user-provided environment variables and apply defaults only if unset
export GF_AUTH_ANONYMOUS_ENABLED="${GF_AUTH_ANONYMOUS_ENABLED:-true}"

# Only set anonymous org role when anonymous auth is enabled
if [ "${GF_AUTH_ANONYMOUS_ENABLED}" != "false" ]; then
	export GF_AUTH_ANONYMOUS_ORG_ROLE="${GF_AUTH_ANONYMOUS_ORG_ROLE:-Admin}"
fi

export GF_PATHS_HOME=/data/grafana
export GF_PATHS_DATA=/data/grafana/data
export GF_PATHS_PLUGINS=/data/grafana/plugins

# pyroscope settings:
# profiles drilldown connects to this plugin automatically - so we install it (even though it does nothing)
if [ -n "${GF_PLUGINS_PREINSTALL:-}" ]; then
	export GF_PLUGINS_PREINSTALL="${GF_PLUGINS_PREINSTALL},grafana-llm-app"
else
	export GF_PLUGINS_PREINSTALL=grafana-llm-app
fi

cd /otel-lgtm/grafana || exit 1
run_with_logging "Grafana ${GRAFANA_VERSION}" "${ENABLE_LOGS_GRAFANA:-false}" ./bin/grafana server
```

## File: `docker/run-loki.sh`
```bash
#!/bin/bash

source ./logging.sh

mkdir -p /data/loki

extra_args=()
if [[ -n "${LOKI_EXTRA_ARGS:-}" ]]; then
	read -ra extra_args <<<"${LOKI_EXTRA_ARGS}"
fi
run_with_logging "Loki ${LOKI_VERSION}" "${ENABLE_LOGS_LOKI:-false}" \
	./loki/loki --config.file=./loki-config.yaml "${extra_args[@]}"
```

## File: `docker/run-obi.sh`
```bash
#!/bin/bash

source ./logging.sh

# Map friendly language names to OBI's OTEL_EBPF_AUTO_TARGET_EXE
case "${OBI_TARGET:-}" in
java) export OTEL_EBPF_AUTO_TARGET_EXE="java" ;;
python) export OTEL_EBPF_AUTO_TARGET_EXE="python|python3" ;;
node) export OTEL_EBPF_AUTO_TARGET_EXE="node" ;;
dotnet) export OTEL_EBPF_AUTO_TARGET_EXE="dotnet" ;;
ruby) export OTEL_EBPF_AUTO_TARGET_EXE="ruby" ;;
go) echo "Note: Go binaries have no common executable name. Use OTEL_EBPF_OPEN_PORT or OTEL_EBPF_AUTO_TARGET_EXE with your binary name." ;;
"") ;;                                                 # use default port-based discovery (see below)
*) export OTEL_EBPF_AUTO_TARGET_EXE="${OBI_TARGET}" ;; # pass through as regex
esac

# Default to port-based discovery when no specific target or port is configured
if [[ -z ${OTEL_EBPF_AUTO_TARGET_EXE:-} && -z ${OTEL_EBPF_OPEN_PORT:-} ]]; then
	export OTEL_EBPF_OPEN_PORT="80,443,8080-8099,3000-3999,5000-5999"
fi

run_with_logging "OBI ${OBI_VERSION}" "${ENABLE_LOGS_OBI:-false}" ./obi/obi --config=./obi-config.yaml
```

## File: `docker/run-otelcol.sh`
```bash
#!/bin/bash

source ./logging.sh

secondary_config_file=""

render_external_otlp_export_config() {
	cat <<'EOF' >otelcol-config-export-http.yaml
service:
  pipelines:
EOF

	for signal in traces metrics logs; do
		local signal_var="OTEL_EXPORTER_OTLP_${signal^^}_ENDPOINT"
		if [[ -n ${!signal_var:-} ]]; then
			printf '    %s:\n      exporters: [otlphttp/%s, otlphttp/external-%s]\n' "${signal}" "${signal}" "${signal}" >>otelcol-config-export-http.yaml
		fi
	done

	cat <<'EOF' >>otelcol-config-export-http.yaml

exporters:
EOF

	for signal in traces metrics logs; do
		local signal_var="OTEL_EXPORTER_OTLP_${signal^^}_ENDPOINT"
		if [[ -n ${!signal_var:-} ]]; then
			# shellcheck disable=SC2016 # otelcol config template, not bash variables
			printf '  otlphttp/external-%s:\n    endpoint: ${env:%s}\n' \
				"${signal}" "${signal_var}" >>otelcol-config-export-http.yaml
		fi
	done
}

if [[ -n ${OTEL_EXPORTER_OTLP_ENDPOINT:-} ||
	-n ${OTEL_EXPORTER_OTLP_TRACES_ENDPOINT:-} ||
	-n ${OTEL_EXPORTER_OTLP_METRICS_ENDPOINT:-} ||
	-n ${OTEL_EXPORTER_OTLP_LOGS_ENDPOINT:-} ]]; then
	if [[ -n ${OTEL_EXPORTER_OTLP_ENDPOINT:-} ]]; then
		echo "Also enabling OTLP/HTTP export to ${OTEL_EXPORTER_OTLP_ENDPOINT}"
	fi

	# Keep backward compatibility: if only OTEL_EXPORTER_OTLP_ENDPOINT is set,
	# use it as the per-signal endpoint fallback.
	export OTEL_EXPORTER_OTLP_LOGS_ENDPOINT="${OTEL_EXPORTER_OTLP_LOGS_ENDPOINT:-${OTEL_EXPORTER_OTLP_ENDPOINT:-}}"
	export OTEL_EXPORTER_OTLP_METRICS_ENDPOINT="${OTEL_EXPORTER_OTLP_METRICS_ENDPOINT:-${OTEL_EXPORTER_OTLP_ENDPOINT:-}}"
	export OTEL_EXPORTER_OTLP_TRACES_ENDPOINT="${OTEL_EXPORTER_OTLP_TRACES_ENDPOINT:-${OTEL_EXPORTER_OTLP_ENDPOINT:-}}"

	render_external_otlp_export_config
	secondary_config_file="--config=file:./otelcol-config-export-http.yaml"

	if [[ -v OTEL_EXPORTER_OTLP_HEADERS && -n ${OTEL_EXPORTER_OTLP_HEADERS} ]]; then
		echo "Adding headers from OTEL_EXPORTER_OTLP_HEADERS"

		yaml_headers="{"
		# split the headers into an array on , - and then each element using =
		IFS=',' read -r -a headers <<<"$OTEL_EXPORTER_OTLP_HEADERS"
		for header in "${headers[@]}"; do
			IFS='=' read -r -a header_parts <<<"$header"
			if [[ ${#header_parts[@]} -eq 2 ]]; then
				if [[ $yaml_headers != "{" ]]; then
					yaml_headers+=", "
				fi
				yaml_headers+="'${header_parts[0]}': '${header_parts[1]}'"
			else
				echo "Invalid header: $header"
			fi
		done
		yaml_headers+="}"

		# add the contents of OTEL_EXPORTER_OTLP_HEADERS to all external exporters in otelcol-config-export-http.yaml
		awk -v headers="${yaml_headers}" '
			{ print }
			/endpoint: \$\{env:OTEL_EXPORTER_OTLP_(LOGS|METRICS|TRACES)_ENDPOINT\}/ {
				print "    headers: " headers
			}
		' otelcol-config-export-http.yaml >otelcol-config-export-http.yaml.tmp && mv otelcol-config-export-http.yaml.tmp otelcol-config-export-http.yaml
	fi
fi

otelcol_args=(--feature-gates service.profilesSupport --config=file:./otelcol-config.yaml)
[[ -n "${secondary_config_file}" ]] && otelcol_args+=("${secondary_config_file}")
extra_args=()
if [[ -n "${OTELCOL_EXTRA_ARGS:-}" ]]; then
	read -ra extra_args <<<"${OTELCOL_EXTRA_ARGS}"
fi
run_with_logging "OpenTelemetry Collector ${OPENTELEMETRY_COLLECTOR_VERSION}" "${ENABLE_LOGS_OTELCOL:-false}" \
	./otelcol-contrib/otelcol-contrib "${otelcol_args[@]}" "${extra_args[@]}"
```

## File: `docker/run-prometheus.sh`
```bash
#!/bin/bash

source ./logging.sh

extra_args=()
if [[ -n "${PROMETHEUS_EXTRA_ARGS:-}" ]]; then
	read -ra extra_args <<<"${PROMETHEUS_EXTRA_ARGS}"
fi
run_with_logging "Prometheus ${PROMETHEUS_VERSION}" "${ENABLE_LOGS_PROMETHEUS:-false}" ./prometheus/prometheus \
	--web.enable-remote-write-receiver \
	--web.enable-otlp-receiver \
	--enable-feature=exemplar-storage \
	--storage.tsdb.path=/data/prometheus \
	--config.file=./prometheus.yaml \
	"${extra_args[@]}"
```

## File: `docker/run-pyroscope.sh`
```bash
#!/bin/bash

source ./logging.sh

mkdir -p /data/pyroscope

extra_args=()
if [[ -n "${PYROSCOPE_EXTRA_ARGS:-}" ]]; then
	read -ra extra_args <<<"${PYROSCOPE_EXTRA_ARGS}"
fi
run_with_logging "Pyroscope ${PYROSCOPE_VERSION}" "${ENABLE_LOGS_PYROSCOPE:-false}" \
	./pyroscope/pyroscope --config.file=./pyroscope-config.yaml "${extra_args[@]}"
```

## File: `docker/run-tempo.sh`
```bash
#!/bin/bash

source ./logging.sh

extra_args=()
if [[ -n "${TEMPO_EXTRA_ARGS:-}" ]]; then
	read -ra extra_args <<<"${TEMPO_EXTRA_ARGS}"
fi
run_with_logging "Tempo ${TEMPO_VERSION}" "${ENABLE_LOGS_TEMPO:-false}" \
	./tempo/tempo --config.file=./tempo-config.yaml "${extra_args[@]}"
```

## File: `docker/tempo-config.yaml`
```yaml
server:
  http_listen_port: 3200
  grpc_listen_port: 9096

distributor:
  receivers:
    otlp:
      protocols:
        grpc:
          endpoint: "127.0.0.1:4417"
        http:
          endpoint: "127.0.0.1:4418"

ingester:
  trace_idle_period: 1s
  max_block_duration: 1s
  flush_check_period: 1s
  lifecycler:
    address: 127.0.0.1
    ring:
      kvstore:
        store: inmemory
      replication_factor: 1
    min_ready_duration: 1s

memberlist:
  bind_addr: [127.0.0.1]
  bind_port: 7947

querier:
  frontend_worker:
    frontend_address: 127.0.0.1:9096

storage:
  trace:
    backend: local
    wal:
      path: /data/tempo/wal
    local:
      path: /data/tempo/blocks

metrics_generator:
  processor:
    local_blocks:
      filter_server_spans: false
    span_metrics:
      dimensions:
        - service_name
        - operation
        - status_code
  traces_storage:
    path: /data/tempo/generator/traces
  storage:
    path: /data/tempo/generator/wal
    remote_write:
      - url: http://127.0.0.1:9090/api/v1/write
        send_exemplars: true

overrides:
  metrics_generator_processors: [service-graphs, local-blocks, span-metrics]
```

## File: `examples/dotnet/.dockerignore`
```
# directories
**/bin/
**/obj/
**/out/

# files
Dockerfile*
**/*.trx
**/*.md
**/*.ps1
**/*.cmd
**/*.sh
```

## File: `examples/dotnet/.gitignore`
```
## Ignore Visual Studio temporary files, build results, and
## files generated by popular Visual Studio add-ons.
##
## Get latest from `dotnet new gitignore`

# dotenv files
.env

# User-specific files
*.rsuser
*.suo
*.user
*.userosscache
*.sln.docstates

# User-specific files (MonoDevelop/Xamarin Studio)
*.userprefs

# Mono auto generated files
mono_crash.*

# Build results
[Dd]ebug/
[Dd]ebugPublic/
[Rr]elease/
[Rr]eleases/
x64/
x86/
[Ww][Ii][Nn]32/
[Aa][Rr][Mm]/
[Aa][Rr][Mm]64/
bld/
[Bb]in/
[Oo]bj/
[Ll]og/
[Ll]ogs/

# Visual Studio 2015/2017 cache/options directory
.vs/
# Uncomment if you have tasks that create the project's static files in wwwroot
#wwwroot/

# Visual Studio 2017 auto generated files
Generated\ Files/

# MSTest test Results
[Tt]est[Rr]esult*/
[Bb]uild[Ll]og.*

# NUnit
*.VisualState.xml
TestResult.xml
nunit-*.xml

# Build Results of an ATL Project
[Dd]ebugPS/
[Rr]eleasePS/
dlldata.c

# Benchmark Results
BenchmarkDotNet.Artifacts/

# .NET
project.lock.json
project.fragment.lock.json
artifacts/

# Tye
.tye/

# ASP.NET Scaffolding
ScaffoldingReadMe.txt

# StyleCop
StyleCopReport.xml

# Files built by Visual Studio
*_i.c
*_p.c
*_h.h
*.ilk
*.meta
*.obj
*.iobj
*.pch
*.pdb
*.ipdb
*.pgc
*.pgd
*.rsp
*.sbr
*.tlb
*.tli
*.tlh
*.tmp
*.tmp_proj
*_wpftmp.csproj
*.log
*.tlog
*.vspscc
*.vssscc
.builds
*.pidb
*.svclog
*.scc

# Chutzpah Test files
_Chutzpah*

# Visual C++ cache files
ipch/
*.aps
*.ncb
*.opendb
*.opensdf
*.sdf
*.cachefile
*.VC.db
*.VC.VC.opendb

# Visual Studio profiler
*.psess
*.vsp
*.vspx
*.sap

# Visual Studio Trace Files
*.e2e

# TFS 2012 Local Workspace
$tf/

# Guidance Automation Toolkit
*.gpState

# ReSharper is a .NET coding add-in
_ReSharper*/
*.[Rr]e[Ss]harper
*.DotSettings.user

# TeamCity is a build add-in
_TeamCity*

# DotCover is a Code Coverage Tool
*.dotCover

# AxoCover is a Code Coverage Tool
.axoCover/*
!.axoCover/settings.json

# Coverlet is a free, cross platform Code Coverage Tool
coverage*.json
coverage*.xml
coverage*.info

# Visual Studio code coverage results
*.coverage
*.coveragexml

# NCrunch
_NCrunch_*
.*crunch*.local.xml
nCrunchTemp_*

# MightyMoose
*.mm.*
AutoTest.Net/

# Web workbench (sass)
.sass-cache/

# Installshield output folder
[Ee]xpress/

# DocProject is a documentation generator add-in
DocProject/buildhelp/
DocProject/Help/*.HxT
DocProject/Help/*.HxC
DocProject/Help/*.hhc
DocProject/Help/*.hhk
DocProject/Help/*.hhp
DocProject/Help/Html2
DocProject/Help/html

# Click-Once directory
publish/

# Publish Web Output
*.[Pp]ublish.xml
*.azurePubxml
# Note: Comment the next line if you want to checkin your web deploy settings,
# but database connection strings (with potential passwords) will be unencrypted
*.pubxml
*.publishproj

# Microsoft Azure Web App publish settings. Comment the next line if you want to
# checkin your Azure Web App publish settings, but sensitive information contained
# in these scripts will be unencrypted
PublishScripts/

# NuGet Packages
*.nupkg
# NuGet Symbol Packages
*.snupkg
# The packages folder can be ignored because of Package Restore
**/[Pp]ackages/*
# except build/, which is used as an MSBuild target.
!**/[Pp]ackages/build/
# Uncomment if necessary however generally it will be regenerated when needed
#!**/[Pp]ackages/repositories.config
# NuGet v3's project.json files produces more ignorable files
*.nuget.props
*.nuget.targets

# Microsoft Azure Build Output
csx/
*.build.csdef

# Microsoft Azure Emulator
ecf/
rcf/

# Windows Store app package directories and files
AppPackages/
BundleArtifacts/
Package.StoreAssociation.xml
_pkginfo.txt
*.appx
*.appxbundle
*.appxupload

# Visual Studio cache files
# files ending in .cache can be ignored
*.[Cc]ache
# but keep track of directories ending in .cache
!?*.[Cc]ache/

# Others
ClientBin/
~$*
*~
*.dbmdl
*.dbproj.schemaview
*.jfm
*.pfx
*.publishsettings
orleans.codegen.cs

# Including strong name files can present a security risk
# (https://github.com/github/gitignore/pull/2483#issue-259490424)
#*.snk

# Since there are multiple workflows, uncomment next line to ignore bower_components
# (https://github.com/github/gitignore/pull/1529#issuecomment-104372622)
#bower_components/

# RIA/Silverlight projects
Generated_Code/

# Backup & report files from converting an old project file
# to a newer Visual Studio version. Backup files are not needed,
# because we have git ;-)
_UpgradeReport_Files/
Backup*/
UpgradeLog*.XML
UpgradeLog*.htm
ServiceFabricBackup/
*.rptproj.bak

# SQL Server files
*.mdf
*.ldf
*.ndf

# Business Intelligence projects
*.rdl.data
*.bim.layout
*.bim_*.settings
*.rptproj.rsuser
*- [Bb]ackup.rdl
*- [Bb]ackup ([0-9]).rdl
*- [Bb]ackup ([0-9][0-9]).rdl

# Microsoft Fakes
FakesAssemblies/

# GhostDoc plugin setting file
*.GhostDoc.xml

# Node.js Tools for Visual Studio
.ntvs_analysis.dat
node_modules/

# Visual Studio 6 build log
*.plg

# Visual Studio 6 workspace options file
*.opt

# Visual Studio 6 auto-generated workspace file (contains which files were open etc.)
*.vbw

# Visual Studio 6 auto-generated project file (contains which files were open etc.)
*.vbp

# Visual Studio 6 workspace and project file (working project files containing files to include in project)
*.dsw
*.dsp

# Visual Studio 6 technical files
*.ncb
*.aps

# Visual Studio LightSwitch build output
**/*.HTMLClient/GeneratedArtifacts
**/*.DesktopClient/GeneratedArtifacts
**/*.DesktopClient/ModelManifest.xml
**/*.Server/GeneratedArtifacts
**/*.Server/ModelManifest.xml
_Pvt_Extensions

# Paket dependency manager
.paket/paket.exe
paket-files/

# FAKE - F# Make
.fake/

# CodeRush personal settings
.cr/personal

# Python Tools for Visual Studio (PTVS)
__pycache__/
*.pyc

# Cake - Uncomment if you are using it
# tools/**
# !tools/packages.config

# Tabs Studio
*.tss

# Telerik's JustMock configuration file
*.jmconfig

# BizTalk build output
*.btp.cs
*.btm.cs
*.odx.cs
*.xsd.cs

# OpenCover UI analysis results
OpenCover/

# Azure Stream Analytics local run output
ASALocalRun/

# MSBuild Binary and Structured Log
*.binlog

# NVidia Nsight GPU debugger configuration file
*.nvuser

# MFractors (Xamarin productivity tool) working folder
.mfractor/

# Local History for Visual Studio
.localhistory/

# Visual Studio History (VSHistory) files
.vshistory/

# BeatPulse healthcheck temp database
healthchecksdb

# Backup folder for Package Reference Convert tool in Visual Studio 2017
MigrationBackup/

# Ionide (cross platform F# VS Code tools) working folder
.ionide/

# Fody - auto-generated XML schema
FodyWeavers.xsd

# VS Code files for those working on multiple tools
.vscode/*
!.vscode/settings.json
!.vscode/tasks.json
!.vscode/launch.json
!.vscode/extensions.json
*.code-workspace

# Local History for Visual Studio Code
.history/

# Windows Installer files from build outputs
*.cab
*.msi
*.msix
*.msm
*.msp

# JetBrains Rider
*.sln.iml
.idea

##
## Visual studio for Mac
##


# globs
Makefile.in
*.userprefs
*.usertasks
config.make
config.status
aclocal.m4
install-sh
autom4te.cache/
*.tar.gz
tarballs/
test-results/

# Mac bundle stuff
*.dmg
*.app

# content below from: https://github.com/github/gitignore/blob/master/Global/macOS.gitignore
# General
.DS_Store
.AppleDouble
.LSOverride

# Icon must end with two \r
Icon


# Thumbnails
._*

# Files that might appear in the root of a volume
.DocumentRevisions-V100
.fseventsd
.Spotlight-V100
.TemporaryItems
.Trashes
.VolumeIcon.icns
.com.apple.timemachine.donotpresent

# Directories potentially created on remote AFP share
.AppleDB
.AppleDesktop
Network Trash Folder
Temporary Items
.apdisk

# content below from: https://github.com/github/gitignore/blob/master/Global/Windows.gitignore
# Windows thumbnail cache files
Thumbs.db
ehthumbs.db
ehthumbs_vista.db

# Dump file
*.stackdump

# Folder config file
[Dd]esktop.ini

# Recycle Bin used on file shares
$RECYCLE.BIN/

# Windows Installer files
*.cab
*.msi
*.msix
*.msm
*.msp

# Windows shortcuts
*.lnk

# Vim temporary swap files
*.swp
```

## File: `examples/dotnet/Dockerfile`
```
FROM --platform=$BUILDPLATFORM mcr.microsoft.com/dotnet/sdk:10.0 AS build
ARG TARGETARCH
ARG CONFIGURATION=Release

COPY . /source
WORKDIR /source

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

RUN --mount=type=cache,id=nuget,target=/root/.nuget/packages \
    dotnet publish "rolldice.csproj" --arch "${TARGETARCH}" --configuration "${CONFIGURATION}" --output /app /p:UseAppHost=false

FROM mcr.microsoft.com/dotnet/aspnet:10.0 AS final
WORKDIR /app
EXPOSE 8083

ENV ASPNETCORE_HTTP_PORTS=8083

COPY --from=build /app .
ENTRYPOINT ["dotnet", "rolldice.dll"]
```

## File: `examples/dotnet/Program.cs`
```csharp
using OpenTelemetry;
using OpenTelemetry.Instrumentation.AspNetCore;
using OpenTelemetry.Metrics;
using OpenTelemetry.Resources;
using OpenTelemetry.Trace;
using System.Globalization;

var appBuilder = WebApplication.CreateBuilder(args);

// Build a resource configuration action to set service information.
Action<ResourceBuilder> configureResource = r => r.AddService(
    serviceName: appBuilder.Configuration.GetValue("ServiceName", defaultValue: "otel-test")!,
    serviceVersion: typeof(Program).Assembly.GetName().Version?.ToString() ?? "unknown",
    serviceInstanceId: Environment.MachineName);

// Configure OpenTelemetry tracing and metrics with auto-start using the
// AddOpenTelemetry() extension method from the OpenTelemetry.Extensions.Hosting package.
appBuilder.Services.AddOpenTelemetry()
    .ConfigureResource(configureResource)
    .UseOtlpExporter()
    .WithTracing(builder =>
    {
        builder
            .AddHttpClientInstrumentation()
            .AddAspNetCoreInstrumentation();

        // Use IConfiguration binding for AspNetCore instrumentation options.
        appBuilder.Services.Configure<AspNetCoreTraceInstrumentationOptions>(
            appBuilder.Configuration.GetSection("AspNetCoreInstrumentation"));
    })
    .WithMetrics(builder =>
    {
        builder
            .AddHttpClientInstrumentation()
            .AddAspNetCoreInstrumentation();
    });

// Clear default logging providers used by WebApplication host.
appBuilder.Logging.ClearProviders();

// Configure OpenTelemetry Logging.
appBuilder.Logging.AddOpenTelemetry(options =>
{
    // See appsettings.json "Logging:OpenTelemetry" section for configuration.
    var resourceBuilder = ResourceBuilder.CreateDefault();
    configureResource(resourceBuilder);
    options.SetResourceBuilder(resourceBuilder);
});

var app = appBuilder.Build();

static string HandleRollDice(string? player, ILogger<Program> logger)
{
    var result = RollDice();

    if (string.IsNullOrEmpty(player))
    {
        logger.LogInformation("Anonymous player is rolling the dice: {result}", result);
    }
    else
    {
        logger.LogInformation("{player} is rolling the dice: {result}", player, result);
    }

    return result.ToString(CultureInfo.InvariantCulture);
}

static int RollDice() => Random.Shared.Next(1, 7);

app.MapGet("/rolldice/{player?}", HandleRollDice);

app.Run();
```

## File: `examples/dotnet/appsettings.json`
```json
{
  "Logging": {
    "LogLevel": {
      "Default": "Information"
    },
    "OpenTelemetry": {
      "IncludeFormattedMessage": true,
      "IncludeScopes": true,
      "ParseStateValues": true
    }
  },
  "ServiceName": "rolldice",
  "AllowedHosts": "*",
  "HistogramAggregation": "explicit",
  "AspNetCoreInstrumentation": {
    "RecordException": "true"
  },
  "Kestrel": {
    "Endpoints": {
      "Http": {
        "Url": "http://+:8083"
      }
    }
  }
}
```

## File: `examples/dotnet/docker-compose.oats.yml`
```yaml
---
services:
  rolldice:
    image: rolldice
    build:
      context: .
      dockerfile: Dockerfile
    ports:
      - 8080:8083
    environment:
      - OTEL_EXPORTER_OTLP_ENDPOINT=http://lgtm:4318
      - OTEL_EXPORTER_OTLP_PROTOCOL=http/protobuf
      - OTEL_METRIC_EXPORT_INTERVAL=5000 # so we don't have to wait 60s for metrics
```

## File: `examples/dotnet/docker-compose.yml`
```yaml
---
services:
  rolldice:
    image: rolldice
    build:
      context: .
      dockerfile: Dockerfile
    ports:
      - 8083:8083
    environment:
      - OTEL_EXPORTER_OTLP_ENDPOINT=http://otel-lgtm:4318
      - OTEL_EXPORTER_OTLP_PROTOCOL=http/protobuf
      - OTEL_METRIC_EXPORT_INTERVAL=5000 # so we don't have to wait 60s for metrics
    depends_on:
      - otel-lgtm

  otel-lgtm:
    image: grafana/otel-lgtm

    ports:
      - 3000:3000
      - 4040:4040
      - 4317:4317
      - 4318:4318
      - 9090:9090
```

## File: `examples/dotnet/global.json`
```json
{
  "sdk": {
    "allowPrerelease": false
  }
}
```

## File: `examples/dotnet/oats.yaml`
```yaml
# OATS is an acceptance testing framework for OpenTelemetry
# https://github.com/grafana/oats/tree/main/yaml
oats-schema-version: 2
docker-compose:
  files:
    - ./docker-compose.oats.yml
input:
  - path: /rolldice
expected:
  traces:
    - traceql: '{ span.http.route = "/rolldice/{player?}" }'
      equals: "GET /rolldice/{player?}" # should be "GET /rolldice"
      attributes:
        otel.library.name: Microsoft.AspNetCore
  # https://opentelemetry.io/docs/specs/semconv/dotnet/dotnet-http-metrics/#metric-httpclientactive_requests
  metrics:
    - promql: 'http_server_active_requests{http_request_method="GET"}'
      value: ">= 0"
  logs:
    - logql: '{service_name="rolldice"} |~ `Anonymous player is rolling the dice.*`'
      regexp: "Anonymous player is rolling the dice"
```

## File: `examples/dotnet/rolldice.csproj`
```
<Project Sdk="Microsoft.NET.Sdk.Web">

  <PropertyGroup>
    <TargetFramework>net10.0</TargetFramework>
    <Nullable>enable</Nullable>
    <ImplicitUsings>enable</ImplicitUsings>
  </PropertyGroup>

  <ItemGroup>
    <PackageReference Include="OpenTelemetry.Exporter.Console" Version="1.15.1" />
    <PackageReference Include="OpenTelemetry.Exporter.OpenTelemetryProtocol" Version="1.15.1" />
    <PackageReference Include="OpenTelemetry.Extensions.Hosting" Version="1.15.1" />
    <PackageReference Include="OpenTelemetry.Instrumentation.AspNetCore" Version="1.15.1" />
    <PackageReference Include="OpenTelemetry.Instrumentation.Http" Version="1.15.0" />
  </ItemGroup>

</Project>
```

## File: `examples/dotnet/run.sh`
```bash
#!/bin/bash

set -euo pipefail

export OTEL_METRIC_EXPORT_INTERVAL="5000" # so we don't have to wait 60s for metrics
dotnet run
```

## File: `examples/dotnet/Properties/launchSettings.json`
```json
﻿{
  "$schema": "http://json.schemastore.org/launchsettings.json",
  "profiles": {
    "http": {
      "commandName": "Project",
      "dotnetRunMessages": true,
      "launchBrowser": true,
      "applicationUrl": "http://127.0.0.1:8083/rolldice"
    }
  }
}
```

## File: `examples/ebpf-profiler/Dockerfile`
```
FROM otel/opentelemetry-ebpf-profiler-dev:202601021410@sha256:1d78b71cfc84beafdb321a11375628c2cb8c2d5ca544e34ddf50e3478eff8e6f AS builder

# renovate: datasource=github-tags depName=opentelemetry-ebpf-profiler packageName=open-telemetry/opentelemetry-ebpf-profiler
ARG OPENTELEMETRY_EBPF_PROFILER_VERSION=v0.0.202610
RUN wget https://github.com/open-telemetry/opentelemetry-ebpf-profiler/archive/$OPENTELEMETRY_EBPF_PROFILER_VERSION.tar.gz
RUN mkdir /profiler
RUN tar --strip-components=1 -C /profiler -xzf $OPENTELEMETRY_EBPF_PROFILER_VERSION.tar.gz
WORKDIR /profiler
RUN /bin/bash -euo pipefail -c "source /etc/profile && make ebpf-profiler"

FROM ubuntu:24.04@sha256:186072bba1b2f436cbb91ef2567abca677337cfc786c86e107d25b7072feef0c

COPY --from=builder /profiler/ebpf-profiler /usr/local/bin/

ENTRYPOINT ["/usr/local/bin/ebpf-profiler"]
```

## File: `examples/ebpf-profiler/README.md`
```markdown
# OpenTelemetry eBPF profiler examples

**⚠️ Important: Early access**
The OpenTelemetry eBPF profiler is under active development and may change in the future.
This example is based on the latest Git commit - releases no not yet exist.

**⚠️ Important: Linux-only Support**
This example can only be run on Linux systems (amd64/arm64) as it relies on eBPF technology which is
specific to the Linux kernel.
The profiler requires privileged access to system resources.
For more details refer to the OpenTelemetry ebpf profiler
[docs](https://github.com/open-telemetry/opentelemetry-ebpf-profiler).

These examples demonstrate:

1. OpenTelemetry eBPF profiler collecting system-wide profiles
2. OpenTelemetry Collector receiving and processing the data from the profiler
3. Pyroscope receiving and visualizing the profiles via Grafana

## Docker example

1. Start the environment:

```bash
# Start all services
docker compose up --remove-orphans --build

# To clean up
docker compose down
```

2. Access the UI:

Navigate to the [Pyroscope UI][Pyroscope UI] to visualize the profiles.

## Example output

![Image](https://github.com/user-attachments/assets/15ff58d4-218a-43dd-9835-df12e13ced3f)

<!-- editorconfig-checker-disable -->
<!-- markdownlint-disable MD013 -->

[Pyroscope UI]: http://127.0.0.1:3000/a/grafana-pyroscope-app/explore?searchText=&panelType=time-series&layout=grid&hideNoData=off&explorationType=flame-graph&var-serviceName=unknown&var-profileMetricId=process_cpu:cpu:nanoseconds:cpu:nanoseconds&var-spanSelector=undefined&var-dataSource=pyroscope&var-filters=&var-filtersBaseline=&var-filtersComparison=&var-groupBy=all&maxNodes=16384
```

## File: `examples/ebpf-profiler/docker-compose.oats.yml`
```yaml
services:
  otel-ebpf-profiler:
    build:
      context: .
      dockerfile: Dockerfile
    command: ["-collection-agent", "lgtm:4317", "-no-kernel-version-check", "-disable-tls"]
    hostname: ebpf-profiler
    privileged: true
    pid: "host"
    volumes:
      - /sys/kernel/debug:/sys/kernel/debug
      - /sys/fs/cgroup:/sys/fs/cgroup
      - /proc:/proc
    depends_on:
      - lgtm

  # instrumented applications - sorted alphabetically by language
  go:
    build:
      context: ../go
      dockerfile: ../go/Dockerfile
    environment:
      OTEL_SERVICE_NAME: "rolldice"
      OTEL_EXPORTER_OTLP_ENDPOINT: http://lgtm:4318
      OTEL_METRIC_EXPORT_INTERVAL: "5000" # so we don't have to wait 60s for metrics
    ports:
      - "8080:8081"
    depends_on:
      - lgtm
#
#  java:
#    build:
#      context: ../java
#      dockerfile: ../java/json-logging-otlp/Dockerfile
#    environment:
#      OTEL_SERVICE_NAME: "rolldice"
#      OTEL_EXPORTER_OTLP_ENDPOINT: http://lgtm:4318
#      OTEL_METRIC_EXPORT_INTERVAL: "5000" # so we don't have to wait 60s for metrics
#    ports:
#      - "8080:8080"
#    depends_on:
#      - lgtm
#
#  python:
#    build:
#      context: ../python
#      dockerfile: ../python/Dockerfile
#    environment:
#      OTEL_SERVICE_NAME: "rolldice"
#      OTEL_EXPORTER_OTLP_ENDPOINT: http://lgtm:4317
#      OTEL_METRIC_EXPORT_INTERVAL: "5000" # so we don't have to wait 60s for metrics
#    ports:
#      - "8082:8082"
#    depends_on:
#      - lgtm
```

## File: `examples/ebpf-profiler/docker-compose.yml`
```yaml
services:
  lgtm:
    image: grafana/otel-lgtm
    environment:
      ENABLE_LOGS_OTELCOL: true
      ENABLE_LOGS_PYROSCOPE: true
    networks:
      - otel-net
    ports:
      - "3000:3000"
      - "4040:4040"
      - "4317:4317"
      - "4318:4318"
      - "9090:9090"

  generate-traffic:
    build:
      dockerfile: generate-traffic.Dockerfile
    networks:
      - otel-net
    depends_on:
      - java
      - python
      - dotnet
      - go
      - nodejs

  otel-ebpf-profiler:
    build:
      context: .
      dockerfile: Dockerfile
    command: ["-collection-agent", "lgtm:4317", "-no-kernel-version-check", "-disable-tls"]
    hostname: ebpf-profiler
    privileged: true
    pid: "host"
    volumes:
      - /sys/kernel/debug:/sys/kernel/debug
      - /sys/fs/cgroup:/sys/fs/cgroup
      - /proc:/proc
    networks:
      - otel-net
    depends_on:
      - lgtm

  # instrumented applications - sorted alphabetically by language

  dotnet:
    build:
      context: ../dotnet
      dockerfile: ../dotnet/Dockerfile
    environment:
      OTEL_SERVICE_NAME: "rolldice"
      OTEL_EXPORTER_OTLP_ENDPOINT: http://lgtm:4317
    ports:
      - "8083:8083"
    networks:
      - otel-net
    depends_on:
      - lgtm

  go:
    build:
      context: ../go
      dockerfile: ../go/Dockerfile
    environment:
      OTEL_SERVICE_NAME: "rolldice"
      OTEL_EXPORTER_OTLP_ENDPOINT: http://lgtm:4318
      OTEL_METRIC_EXPORT_INTERVAL: "5000" # so we don't have to wait 60s for metrics
    ports:
      - "8081:8081"
    networks:
      - otel-net
    depends_on:
      - lgtm

  java:
    build:
      context: ../java
      dockerfile: ../java/Dockerfile
    environment:
      OTEL_SERVICE_NAME: "rolldice"
      OTEL_EXPORTER_OTLP_ENDPOINT: http://lgtm:4318
      GRAFANA_ROLL_WAIT: "2000" # 2 seconds
    ports:
      - "8080:8080"
    networks:
      - otel-net
    depends_on:
      - lgtm

  nodejs:
    build:
      context: ../nodejs
      dockerfile: ../nodejs/Dockerfile
    environment:
      OTEL_SERVICE_NAME: "rolldice"
      OTEL_EXPORTER_OTLP_ENDPOINT: http://lgtm:4318
      OTEL_METRIC_EXPORT_INTERVAL: "5000" # so we don't have to wait 60s for metrics
    ports:
      - "8084:8084"
    networks:
      - otel-net
    depends_on:
      - lgtm

  python:
    build:
      context: ../python
      dockerfile: ../python/Dockerfile
    environment:
      OTEL_SERVICE_NAME: "rolldice"
      OTEL_EXPORTER_OTLP_ENDPOINT: http://lgtm:4317
      OTEL_METRIC_EXPORT_INTERVAL: "5000" # so we don't have to wait 60s for metrics
    ports:
      - "8082:8082"
    networks:
      - otel-net
    depends_on:
      - lgtm

networks:
  otel-net:
    driver: bridge
```

## File: `examples/ebpf-profiler/generate-traffic.Dockerfile`
```
FROM ubuntu:24.04

COPY generate-traffic.sh /usr/local/bin/

RUN apt-get update && apt-get -y install curl

ENTRYPOINT ["/usr/local/bin/generate-traffic.sh"]
```

## File: `examples/ebpf-profiler/generate-traffic.sh`
```bash
#!/bin/bash

while true; do
	curl -s http://java:8080/rolldice || echo "error reaching java service"
	curl -s http://go:8081/rolldice || echo "error reaching go service"
	curl -s http://python:8082/rolldice || echo "error reaching python service"
	curl -s http://dotnet:8083/rolldice || echo "error reaching dotnet service"
	curl -s http://nodejs:8084/rolldice?rolls=5 || echo "error reaching nodejs service"
	sleep 1
done
```

## File: `examples/ebpf-profiler/oats.yaml`
```yaml
# OATS is an acceptance testing framework for OpenTelemetry
# https://github.com/grafana/oats/tree/main/yaml
oats-schema-version: 2
docker-compose:
  files:
    - ./docker-compose.oats.yml
input:
  - path: /rolldice
expected:
  profiles:
    # go
    - query: 'process_cpu:cpu:nanoseconds:cpu:nanoseconds{process_executable_name=~"rolldice"}'
      flamebearers:
        equals: "main.rolldice"
    # python and java are flaky
#    - query: 'process_cpu:cpu:nanoseconds:cpu:nanoseconds{process_executable_name=~"python.*"}'
#      flamebearers:
#        # not very useful, because the python function names are not in the flamegraph
#        contains: "python"
#    - query: 'process_cpu:cpu:nanoseconds:cpu:nanoseconds{process_executable_name="java"}'
#      flamebearers:
#        contains: "void org.springframework.boot.SpringApplication.refreshContext(org.springframework.context.ConfigurableApplicationContext)"
```

## File: `examples/go/Dockerfile`
```
FROM golang:1.26@sha256:595c7847cff97c9a9e76f015083c481d26078f961c9c8dca3923132f51fe12f1

WORKDIR /app

COPY go.mod go.sum ./
RUN go mod download

COPY *.go ./

# Build
RUN CGO_ENABLED=0 GOOS=linux go build -o /rolldice

EXPOSE 8081

# Run
CMD ["/rolldice"]
```

## File: `examples/go/docker-compose.oats.yml`
```yaml
---
# OATS is an acceptance testing framework for OpenTelemetry
# https://github.com/grafana/oats/tree/main/yaml
services:
  go:
    build:
      context: .
      dockerfile: Dockerfile
    environment:
      OTEL_EXPORTER_OTLP_ENDPOINT: http://lgtm:4318
      OTEL_METRIC_EXPORT_INTERVAL: "5000" # so we don't have to wait 60s for metrics
    ports:
      - "8080:8081"
```

## File: `examples/go/go.mod`
```
module dice

go 1.25.0

require (
	go.opentelemetry.io/contrib/instrumentation/net/http/otelhttp v0.67.0
	go.opentelemetry.io/contrib/instrumentation/runtime v0.67.0
	go.opentelemetry.io/otel v1.42.0
	go.opentelemetry.io/otel/exporters/otlp/otlplog/otlploghttp v0.18.0
	go.opentelemetry.io/otel/exporters/otlp/otlpmetric/otlpmetrichttp v1.42.0
	go.opentelemetry.io/otel/exporters/otlp/otlptrace v1.42.0
	go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracehttp v1.42.0
	go.opentelemetry.io/otel/log v0.18.0
	go.opentelemetry.io/otel/sdk v1.42.0
	go.opentelemetry.io/otel/sdk/log v0.18.0
	go.opentelemetry.io/otel/sdk/metric v1.42.0
)

require (
	github.com/cenkalti/backoff/v5 v5.0.3 // indirect
	github.com/cespare/xxhash/v2 v2.3.0 // indirect
	go.opentelemetry.io/auto/sdk v1.2.1 // indirect
)

require (
	github.com/felixge/httpsnoop v1.0.4 // indirect
	github.com/go-logr/logr v1.4.3 // indirect
	github.com/go-logr/stdr v1.2.2 // indirect
	github.com/google/uuid v1.6.0 // indirect
	github.com/grpc-ecosystem/grpc-gateway/v2 v2.28.0 // indirect
	go.opentelemetry.io/contrib/bridges/otelslog v0.17.0
	go.opentelemetry.io/otel/metric v1.42.0
	go.opentelemetry.io/otel/trace v1.42.0 // indirect
	go.opentelemetry.io/proto/otlp v1.9.0 // indirect
	golang.org/x/net v0.51.0 // indirect
	golang.org/x/sys v0.41.0 // indirect
	golang.org/x/text v0.34.0 // indirect
	google.golang.org/genproto/googleapis/api v0.0.0-20260209200024-4cfbd4190f57 // indirect
	google.golang.org/genproto/googleapis/rpc v0.0.0-20260209200024-4cfbd4190f57 // indirect
	google.golang.org/grpc v1.79.3 // indirect
	google.golang.org/protobuf v1.36.11 // indirect
)
```

## File: `examples/go/go.sum`
```
github.com/cenkalti/backoff/v5 v5.0.3 h1:ZN+IMa753KfX5hd8vVaMixjnqRZ3y8CuJKRKj1xcsSM=
github.com/cenkalti/backoff/v5 v5.0.3/go.mod h1:rkhZdG3JZukswDf7f0cwqPNk4K0sa+F97BxZthm/crw=
github.com/cespare/xxhash/v2 v2.3.0 h1:UL815xU9SqsFlibzuggzjXhog7bL6oX9BbNZnL2UFvs=
github.com/cespare/xxhash/v2 v2.3.0/go.mod h1:VGX0DQ3Q6kWi7AoAeZDth3/j3BFtOZR5XLFGgcrjCOs=
github.com/davecgh/go-spew v1.1.1 h1:vj9j/u1bqnvCEfJOwUhtlOARqs3+rkHYY13jYWTU97c=
github.com/davecgh/go-spew v1.1.1/go.mod h1:J7Y8YcW2NihsgmVo/mv3lAwl/skON4iLHjSsI+c5H38=
github.com/felixge/httpsnoop v1.0.4 h1:NFTV2Zj1bL4mc9sqWACXbQFVBBg2W3GPvqp8/ESS2Wg=
github.com/felixge/httpsnoop v1.0.4/go.mod h1:m8KPJKqk1gH5J9DgRY2ASl2lWCfGKXixSwevea8zH2U=
github.com/go-logr/logr v1.2.2/go.mod h1:jdQByPbusPIv2/zmleS9BjJVeZ6kBagPoEUsqbVz/1A=
github.com/go-logr/logr v1.4.3 h1:CjnDlHq8ikf6E492q6eKboGOC0T8CDaOvkHCIg8idEI=
github.com/go-logr/logr v1.4.3/go.mod h1:9T104GzyrTigFIr8wt5mBrctHMim0Nb2HLGrmQ40KvY=
github.com/go-logr/stdr v1.2.2 h1:hSWxHoqTgW2S2qGc0LTAI563KZ5YKYRhT3MFKZMbjag=
github.com/go-logr/stdr v1.2.2/go.mod h1:mMo/vtBO5dYbehREoey6XUKy/eSumjCCveDpRre4VKE=
github.com/golang/protobuf v1.5.4 h1:i7eJL8qZTpSEXOPTxNKhASYpMn+8e5Q6AdndVa1dWek=
github.com/golang/protobuf v1.5.4/go.mod h1:lnTiLA8Wa4RWRcIUkrtSVa5nRhsEGBg48fD6rSs7xps=
github.com/google/go-cmp v0.7.0 h1:wk8382ETsv4JYUZwIsn6YpYiWiBsYLSJiTsyBybVuN8=
github.com/google/go-cmp v0.7.0/go.mod h1:pXiqmnSA92OHEEa9HXL2W4E7lf9JzCmGVUdgjX3N/iU=
github.com/google/uuid v1.6.0 h1:NIvaJDMOsjHA8n1jAhLSgzrAzy1Hgr+hNrb57e+94F0=
github.com/google/uuid v1.6.0/go.mod h1:TIyPZe4MgqvfeYDBFedMoGGpEw/LqOeaOT+nhxU+yHo=
github.com/grpc-ecosystem/grpc-gateway/v2 v2.28.0 h1:HWRh5R2+9EifMyIHV7ZV+MIZqgz+PMpZ14Jynv3O2Zs=
github.com/grpc-ecosystem/grpc-gateway/v2 v2.28.0/go.mod h1:JfhWUomR1baixubs02l85lZYYOm7LV6om4ceouMv45c=
github.com/pmezard/go-difflib v1.0.0 h1:4DBwDE0NGyQoBHbLQYPwSUPoCMWR5BEzIk/f1lZbAQM=
github.com/pmezard/go-difflib v1.0.0/go.mod h1:iKH77koFhYxTK1pcRnkKkqfTogsbg7gZNVY4sRDYZ/4=
github.com/stretchr/testify v1.11.1 h1:7s2iGBzp5EwR7/aIZr8ao5+dra3wiQyKjjFuvgVKu7U=
github.com/stretchr/testify v1.11.1/go.mod h1:wZwfW3scLgRK+23gO65QZefKpKQRnfz6sD981Nm4B6U=
go.opentelemetry.io/auto/sdk v1.2.1 h1:jXsnJ4Lmnqd11kwkBV2LgLoFMZKizbCi5fNZ/ipaZ64=
go.opentelemetry.io/auto/sdk v1.2.1/go.mod h1:KRTj+aOaElaLi+wW1kO/DZRXwkF4C5xPbEe3ZiIhN7Y=
go.opentelemetry.io/contrib/bridges/otelslog v0.17.0 h1:NFIS6x7wyObQ7cR84x7bt1sr8nYBx89s3x3GwRjw40k=
go.opentelemetry.io/contrib/bridges/otelslog v0.17.0/go.mod h1:39SaByOyDMRMe872AE7uelMuQZidIw7LLFAnQi0FWTE=
go.opentelemetry.io/contrib/instrumentation/net/http/otelhttp v0.67.0 h1:OyrsyzuttWTSur2qN/Lm0m2a8yqyIjUVBZcxFPuXq2o=
go.opentelemetry.io/contrib/instrumentation/net/http/otelhttp v0.67.0/go.mod h1:C2NGBr+kAB4bk3xtMXfZ94gqFDtg/GkI7e9zqGh5Beg=
go.opentelemetry.io/contrib/instrumentation/runtime v0.67.0 h1:fM78cKITJ2r08cl+nw5i+hI9zWAu3iak8o1Os/ca2Ck=
go.opentelemetry.io/contrib/instrumentation/runtime v0.67.0/go.mod h1:ybmlzIqGcQzwt5lAfi8TpSnHo/CI3yv1Czodmm+OJa8=
go.opentelemetry.io/otel v1.42.0 h1:lSQGzTgVR3+sgJDAU/7/ZMjN9Z+vUip7leaqBKy4sho=
go.opentelemetry.io/otel v1.42.0/go.mod h1:lJNsdRMxCUIWuMlVJWzecSMuNjE7dOYyWlqOXWkdqCc=
go.opentelemetry.io/otel/exporters/otlp/otlplog/otlploghttp v0.18.0 h1:icqq3Z34UrEFk2u+HMhTtRsvo7Ues+eiJVjaJt62njs=
go.opentelemetry.io/otel/exporters/otlp/otlplog/otlploghttp v0.18.0/go.mod h1:W2m8P+d5Wn5kipj4/xmbt9uMqezEKfBjzVJadfABSBE=
go.opentelemetry.io/otel/exporters/otlp/otlpmetric/otlpmetrichttp v1.42.0 h1:H7O6RlGOMTizyl3R08Kn5pdM06bnH8oscSj7o11tmLA=
go.opentelemetry.io/otel/exporters/otlp/otlpmetric/otlpmetrichttp v1.42.0/go.mod h1:mBFWu/WOVDkWWsR7Tx7h6EpQB8wsv7P0Yrh0Pb7othc=
go.opentelemetry.io/otel/exporters/otlp/otlptrace v1.42.0 h1:THuZiwpQZuHPul65w4WcwEnkX2QIuMT+UFoOrygtoJw=
go.opentelemetry.io/otel/exporters/otlp/otlptrace v1.42.0/go.mod h1:J2pvYM5NGHofZ2/Ru6zw/TNWnEQp5crgyDeSrYpXkAw=
go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracehttp v1.42.0 h1:uLXP+3mghfMf7XmV4PkGfFhFKuNWoCvvx5wP/wOXo0o=
go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracehttp v1.42.0/go.mod h1:v0Tj04armyT59mnURNUJf7RCKcKzq+lgJs6QSjHjaTc=
go.opentelemetry.io/otel/log v0.18.0 h1:XgeQIIBjZZrliksMEbcwMZefoOSMI1hdjiLEiiB0bAg=
go.opentelemetry.io/otel/log v0.18.0/go.mod h1:KEV1kad0NofR3ycsiDH4Yjcoj0+8206I6Ox2QYFSNgI=
go.opentelemetry.io/otel/metric v1.42.0 h1:2jXG+3oZLNXEPfNmnpxKDeZsFI5o4J+nz6xUlaFdF/4=
go.opentelemetry.io/otel/metric v1.42.0/go.mod h1:RlUN/7vTU7Ao/diDkEpQpnz3/92J9ko05BIwxYa2SSI=
go.opentelemetry.io/otel/sdk v1.42.0 h1:LyC8+jqk6UJwdrI/8VydAq/hvkFKNHZVIWuslJXYsDo=
go.opentelemetry.io/otel/sdk v1.42.0/go.mod h1:rGHCAxd9DAph0joO4W6OPwxjNTYWghRWmkHuGbayMts=
go.opentelemetry.io/otel/sdk/log v0.18.0 h1:n8OyZr7t7otkeTnPTbDNom6rW16TBYGtvyy2Gk6buQw=
go.opentelemetry.io/otel/sdk/log v0.18.0/go.mod h1:C0+wxkTwKpOCZLrlJ3pewPiiQwpzycPI/u6W0Z9fuYk=
go.opentelemetry.io/otel/sdk/log/logtest v0.18.0 h1:l3mYuPsuBx6UKE47BVcPrZoZ0q/KER57vbj2qkgDLXA=
go.opentelemetry.io/otel/sdk/log/logtest v0.18.0/go.mod h1:7cHtiVJpZebB3wybTa4NG+FUo5NPe3PROz1FqB0+qdw=
go.opentelemetry.io/otel/sdk/metric v1.42.0 h1:D/1QR46Clz6ajyZ3G8SgNlTJKBdGp84q9RKCAZ3YGuA=
go.opentelemetry.io/otel/sdk/metric v1.42.0/go.mod h1:Ua6AAlDKdZ7tdvaQKfSmnFTdHx37+J4ba8MwVCYM5hc=
go.opentelemetry.io/otel/trace v1.42.0 h1:OUCgIPt+mzOnaUTpOQcBiM/PLQ/Op7oq6g4LenLmOYY=
go.opentelemetry.io/otel/trace v1.42.0/go.mod h1:f3K9S+IFqnumBkKhRJMeaZeNk9epyhnCmQh/EysQCdc=
go.opentelemetry.io/proto/otlp v1.9.0 h1:l706jCMITVouPOqEnii2fIAuO3IVGBRPV5ICjceRb/A=
go.opentelemetry.io/proto/otlp v1.9.0/go.mod h1:xE+Cx5E/eEHw+ISFkwPLwCZefwVjY+pqKg1qcK03+/4=
go.uber.org/goleak v1.3.0 h1:2K3zAYmnTNqV73imy9J1T3WC+gmCePx2hEGkimedGto=
go.uber.org/goleak v1.3.0/go.mod h1:CoHD4mav9JJNrW/WLlf7HGZPjdw8EucARQHekz1X6bE=
golang.org/x/net v0.51.0 h1:94R/GTO7mt3/4wIKpcR5gkGmRLOuE/2hNGeWq/GBIFo=
golang.org/x/net v0.51.0/go.mod h1:aamm+2QF5ogm02fjy5Bb7CQ0WMt1/WVM7FtyaTLlA9Y=
golang.org/x/sys v0.41.0 h1:Ivj+2Cp/ylzLiEU89QhWblYnOE9zerudt9Ftecq2C6k=
golang.org/x/sys v0.41.0/go.mod h1:OgkHotnGiDImocRcuBABYBEXf8A9a87e/uXjp9XT3ks=
golang.org/x/text v0.34.0 h1:oL/Qq0Kdaqxa1KbNeMKwQq0reLCCaFtqu2eNuSeNHbk=
golang.org/x/text v0.34.0/go.mod h1:homfLqTYRFyVYemLBFl5GgL/DWEiH5wcsQ5gSh1yziA=
gonum.org/v1/gonum v0.16.0 h1:5+ul4Swaf3ESvrOnidPp4GZbzf0mxVQpDCYUQE7OJfk=
gonum.org/v1/gonum v0.16.0/go.mod h1:fef3am4MQ93R2HHpKnLk4/Tbh/s0+wqD5nfa6Pnwy4E=
google.golang.org/genproto/googleapis/api v0.0.0-20260209200024-4cfbd4190f57 h1:JLQynH/LBHfCTSbDWl+py8C+Rg/k1OVH3xfcaiANuF0=
google.golang.org/genproto/googleapis/api v0.0.0-20260209200024-4cfbd4190f57/go.mod h1:kSJwQxqmFXeo79zOmbrALdflXQeAYcUbgS7PbpMknCY=
google.golang.org/genproto/googleapis/rpc v0.0.0-20260209200024-4cfbd4190f57 h1:mWPCjDEyshlQYzBpMNHaEof6UX1PmHcaUODUywQ0uac=
google.golang.org/genproto/googleapis/rpc v0.0.0-20260209200024-4cfbd4190f57/go.mod h1:j9x/tPzZkyxcgEFkiKEEGxfvyumM01BEtsW8xzOahRQ=
google.golang.org/grpc v1.79.3 h1:sybAEdRIEtvcD68Gx7dmnwjZKlyfuc61Dyo9pGXXkKE=
google.golang.org/grpc v1.79.3/go.mod h1:KmT0Kjez+0dde/v2j9vzwoAScgEPx/Bw1CYChhHLrHQ=
google.golang.org/protobuf v1.36.11 h1:fV6ZwhNocDyBLK0dj+fg8ektcVegBBuEolpbTQyBNVE=
google.golang.org/protobuf v1.36.11/go.mod h1:HTf+CrKn2C3g5S8VImy6tdcUvCska2kB7j23XfzDpco=
gopkg.in/yaml.v3 v3.0.1 h1:fxVm/GzAzEWqLHuvctI91KS9hhNmmWOoWu0XTYJS7CA=
gopkg.in/yaml.v3 v3.0.1/go.mod h1:K4uyk7z7BCEPqu6E+C64Yfv1cQ7kz7rIZviUmN+EgEM=
```

## File: `examples/go/main.go`
```go
package main

import (
	"context"
	"errors"
	"log"
	"net"
	"net/http"
	"os"
	"os/signal"
	"time"

	"go.opentelemetry.io/contrib/instrumentation/net/http/otelhttp"
)

func main() {
	if err := run(); err != nil {
		log.Fatalln(err)
	}
}

func run() (err error) {
	// Handle SIGINT (CTRL+C) gracefully.
	ctx, stop := signal.NotifyContext(context.Background(), os.Interrupt)
	defer stop()

	// Set up OpenTelemetry.
	otelShutdown, err := setupOTelSDK(ctx)
	if err != nil {
		return
	}
	// Handle shutdown properly so nothing leaks.
	defer func() {
		err = errors.Join(err, otelShutdown(context.Background()))
	}()

	// Start HTTP server.
	srv := &http.Server{
		Addr:         ":8081",
		BaseContext:  func(_ net.Listener) context.Context { return ctx },
		ReadTimeout:  time.Second,
		WriteTimeout: 10 * time.Second,
		Handler:      newHTTPHandler(),
	}
	srvErr := make(chan error, 1)
	go func() {
		srvErr <- srv.ListenAndServe()
	}()

	// Wait for interruption.
	select {
	case err = <-srvErr:
		// Error when starting HTTP server.
		return
	case <-ctx.Done():
		// Wait for first CTRL+C.
		// Stop receiving signal notifications as soon as possible.
		stop()
	}

	// When Shutdown is called, ListenAndServe immediately returns ErrServerClosed.
	err = srv.Shutdown(context.Background())
	return
}

func newHTTPHandler() http.Handler {
	mux := http.NewServeMux()

	// Register handlers.
	// Wrap each handler with otelhttp.NewHandler so that the http.route
	// attribute is set correctly from r.Pattern (populated by ServeMux).
	mux.Handle("/rolldice", otelhttp.NewHandler(http.HandlerFunc(rolldice), "/rolldice"))

	return mux
}
```

## File: `examples/go/oats.yaml`
```yaml
---
# OATS is an acceptance testing framework for OpenTelemetry
# https://github.com/grafana/oats/tree/main/yaml
oats-schema-version: 2
docker-compose:
  files:
    - ./docker-compose.oats.yml
input:
  - path: /rolldice
expected:
  traces:
    - traceql: '{ span.http.route = "/rolldice" }'
      equals: "/rolldice"
      attributes:
        otel.library.name: go.opentelemetry.io/contrib/instrumentation/net/http/otelhttp
  metrics:
    - promql: "go_goroutine_count{}"
      value: "> 0"
```

## File: `examples/go/otel.go`
```go
package main

import (
	"context"
	"errors"
	"log/slog"
	"time"

	"go.opentelemetry.io/contrib/bridges/otelslog"
	"go.opentelemetry.io/contrib/instrumentation/runtime"
	"go.opentelemetry.io/otel"
	"go.opentelemetry.io/otel/exporters/otlp/otlplog/otlploghttp"
	"go.opentelemetry.io/otel/exporters/otlp/otlpmetric/otlpmetrichttp"
	"go.opentelemetry.io/otel/exporters/otlp/otlptrace"
	"go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracehttp"
	"go.opentelemetry.io/otel/log/global"
	"go.opentelemetry.io/otel/propagation"
	"go.opentelemetry.io/otel/sdk/log"
	"go.opentelemetry.io/otel/sdk/metric"
	"go.opentelemetry.io/otel/sdk/trace"
)

const schemaName = "https://github.com/grafana/docker-otel-lgtm"

var (
	tracer = otel.Tracer(schemaName)
	logger = otelslog.NewLogger(schemaName)
	meter  = otel.Meter(schemaName)
)

// setupOTelSDK bootstraps the OpenTelemetry pipeline.
// If it does not return an error, make sure to call shutdown for proper cleanup.
func setupOTelSDK(ctx context.Context) (shutdown func(context.Context) error, err error) {
	var shutdownFuncs []func(context.Context) error

	// shutdown calls cleanup functions registered via shutdownFuncs.
	// The errors from the calls are joined.
	// Each registered cleanup will be invoked once.
	shutdown = func(ctx context.Context) error {
		var errs error
		for _, fn := range shutdownFuncs {
			errs = errors.Join(errs, fn(ctx))
		}
		shutdownFuncs = nil
		return errs
	}

	// handleErr calls shutdown for cleanup and makes sure that all errors are returned.
	handleErr := func(inErr error) {
		err = errors.Join(inErr, shutdown(ctx))
	}

	prop := propagation.NewCompositeTextMapPropagator(
		propagation.TraceContext{},
		propagation.Baggage{},
	)
	otel.SetTextMapPropagator(prop)

	traceExporter, err := otlptrace.New(ctx, otlptracehttp.NewClient())
	if err != nil {
		return nil, err
	}

	tracerProvider := trace.NewTracerProvider(trace.WithBatcher(traceExporter))
	if err != nil {
		handleErr(err)
		return
	}
	shutdownFuncs = append(shutdownFuncs, tracerProvider.Shutdown)
	otel.SetTracerProvider(tracerProvider)

	metricExporter, err := otlpmetrichttp.New(ctx)
	if err != nil {
		return nil, err
	}

	meterProvider :=
		metric.NewMeterProvider(metric.WithReader(metric.NewPeriodicReader(metricExporter)))
	if err != nil {
		handleErr(err)
		return
	}
	shutdownFuncs = append(shutdownFuncs, meterProvider.Shutdown)
	otel.SetMeterProvider(meterProvider)

	logExporter, err := otlploghttp.New(ctx, otlploghttp.WithInsecure())
	if err != nil {
		return nil, err
	}

	loggerProvider := log.NewLoggerProvider(log.WithProcessor(log.NewBatchProcessor(logExporter)))
	if err != nil {
		handleErr(err)
		return
	}
	shutdownFuncs = append(shutdownFuncs, loggerProvider.Shutdown)
	global.SetLoggerProvider(loggerProvider)

	err = runtime.Start(runtime.WithMinimumReadMemStatsInterval(time.Second))
	if err != nil {
		logger.ErrorContext(ctx, "otel runtime instrumentation failed:", slog.Any("error", err))
	}

	return
}
```

## File: `examples/go/rolldice.go`
```go
package main

import (
	"fmt"
	"io"
	"log/slog"
	"math/rand"
	"net/http"
	"strconv"
	"time"

	"go.opentelemetry.io/otel/attribute"
	"go.opentelemetry.io/otel/metric"
)

func rolldice(w http.ResponseWriter, r *http.Request) {
	ctx, span := tracer.Start(r.Context(), "roll")
	defer span.End()

	roll := 1 + roll()

	msg := fmt.Sprintf("Rolled a dice: %d\n", roll)
	logger.InfoContext(ctx, msg, slog.Int("result", roll))

	resp := strconv.Itoa(roll) + "\n"
	if _, err := io.WriteString(w, resp); err != nil {
		logger.ErrorContext(ctx, "Write failed: %v\n", slog.Any("error", err))
	}

	h, err := meter.Int64Histogram("dice.roll", metric.WithDescription("The result of the dice roll"))
	success := (err == nil)
	if !success {
		logger.ErrorContext(ctx, "Histogram instantiation failed: %v\n", slog.Any("error", err))
	}
	h.Record(ctx, int64(roll), metric.WithAttributes(attribute.Bool("result.success", success)))
}

func roll() int {
	// simulate a long operation
	// busy wait to make sure it's shown in the flame graph
	start := time.Now()
	//nolint:revive // intentional busy wait for flame graph demo
	for time.Since(start) < 1*time.Second {
	}

	//nolint:gosec
	return rand.Intn(6)
}
```

## File: `examples/go/run.sh`
```bash
#!/bin/bash

set -euo pipefail

export OTEL_METRIC_EXPORT_INTERVAL="5000" # so we don't have to wait 60s for metrics
export OTEL_RESOURCE_ATTRIBUTES="service.name=rolldice,service.instance.id=127.0.0.1:8081"

# Run the application
# use http instead of https (needed because of https://github.com/open-telemetry/opentelemetry-go/issues/4834)
export OTEL_EXPORTER_OTLP_INSECURE="true"
go run .
```

## File: `examples/java/.gitignore`
```
target/
.idea/
```

## File: `examples/java/Dockerfile`
```
FROM ghcr.io/open-telemetry/opentelemetry-operator/autoinstrumentation-java:2.26.1@sha256:dc0c94818e271f4d24ffe44b6894989c5d9c9d7302289bb8559f17dac7b1b159 AS agent

FROM eclipse-temurin:25.0.2_10-jdk@sha256:bee2e23ab444ed60daf8123e36478bc4a286ba7835bec6f9daf9eba1d50a86a2 AS builder

WORKDIR /usr/src/app/

COPY ./mvnw pom.xml ./
COPY ./.mvn ./.mvn
COPY ./src ./src
RUN --mount=type=cache,target=/root/.m2 ./mvnw install -DskipTests

FROM eclipse-temurin:25.0.2_10-jre@sha256:a9980cb3777d2b7b0d513800c3debc034c101530b96db4aadccb845f867fca9e

WORKDIR /usr/src/app/

COPY --from=agent --chown=cnb /javaagent.jar /app/javaagent.jar
ENV JAVA_TOOL_OPTIONS=-javaagent:/app/javaagent.jar
COPY --from=builder /usr/src/app/target/rolldice.jar ./app.jar

EXPOSE 8080
ENTRYPOINT [ "java", "-jar", "./app.jar" ]
```

## File: `examples/java/README.md`
```markdown
# Java Example

Spring Boot application instrumented with OpenTelemetry Java Agent.

## Run with Docker Compose

This example includes a custom Grafana dashboard and sets it as the home dashboard.

```bash
docker compose up -d
```

Generate traffic:

```bash
curl http://127.0.0.1:8080/rolldice
```

Access services:

- Grafana: <http://127.0.0.1:3000> (`admin`/`admin`)
- Application: <http://127.0.0.1:8080/rolldice>

The custom dashboard loads automatically as the home dashboard.

## Run with Standalone Dockerfile

```bash
docker build -t java-rolldice .

# macOS / Windows (Docker Desktop)
docker run -p 8080:8080 \
  -e OTEL_SERVICE_NAME=rolldice \
  -e OTEL_EXPORTER_OTLP_ENDPOINT=http://host.docker.internal:4318 \
  java-rolldice

# Linux (add host.docker.internal manually)
docker run -p 8080:8080 \
  --add-host=host.docker.internal:host-gateway \
  -e OTEL_SERVICE_NAME=rolldice \
  -e OTEL_EXPORTER_OTLP_ENDPOINT=http://host.docker.internal:4318 \
  java-rolldice
```

## Custom Dashboard

The custom dashboard (`custom-dashboard.json`) displays:

- Request rate for the `/rolldice` endpoint
- Response time percentiles (p50, p95)

To modify the dashboard, edit `custom-dashboard.json` and restart the lgtm container:

```bash
docker compose restart lgtm
```
```

## File: `examples/java/custom-dashboard.json`
```json
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
        "type": "dashboard"
      }
    ]
  },
  "description": "Custom dashboard for Java rolldice application",
  "editable": true,
  "fiscalYearStartMonth": 0,
  "graphTooltip": 0,
  "links": [],
  "liveNow": false,
  "panels": [
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${datasource}"
      },
      "description": "Request rate for rolldice endpoint",
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
          "unit": "reqps"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 8,
        "w": 12,
        "x": 0,
        "y": 0
      },
      "id": 1,
      "options": {
        "legend": {
          "calcs": [],
          "displayMode": "list",
          "placement": "bottom",
          "showLegend": true
        },
        "tooltip": {
          "mode": "single",
          "sort": "none"
        }
      },
      "pluginVersion": "11.0.0",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${datasource}"
          },
          "expr": "rate(http_server_request_duration_seconds_count{service_name=\"rolldice\"}[5m])",
          "legendFormat": "{{http_route}}",
          "refId": "A"
        }
      ],
      "title": "Rolldice Request Rate",
      "type": "timeseries"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${datasource}"
      },
      "description": "Response time for rolldice endpoint",
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
          "unit": "s"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 8,
        "w": 12,
        "x": 12,
        "y": 0
      },
      "id": 2,
      "options": {
        "legend": {
          "calcs": ["mean", "max"],
          "displayMode": "table",
          "placement": "bottom",
          "showLegend": true
        },
        "tooltip": {
          "mode": "single",
          "sort": "none"
        }
      },
      "pluginVersion": "11.0.0",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${datasource}"
          },
          "expr": "histogram_quantile(0.95, sum(rate(http_server_request_duration_seconds_bucket{service_name=\"rolldice\"}[5m])) by (le, http_route))",
          "legendFormat": "p95 - {{http_route}}",
          "refId": "A"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${datasource}"
          },
          "expr": "histogram_quantile(0.50, sum(rate(http_server_request_duration_seconds_bucket{service_name=\"rolldice\"}[5m])) by (le, http_route))",
          "legendFormat": "p50 - {{http_route}}",
          "refId": "B"
        }
      ],
      "title": "Rolldice Response Time",
      "type": "timeseries"
    }
  ],
  "schemaVersion": 39,
  "tags": ["custom", "java", "rolldice"],
  "templating": {
    "list": [
      {
        "current": {
          "selected": false,
          "text": "Prometheus",
          "value": "prometheus"
        },
        "hide": 0,
        "includeAll": false,
        "label": "Datasource",
        "multi": false,
        "name": "datasource",
        "options": [],
        "query": "prometheus",
        "refresh": 1,
        "regex": "",
        "skipUrlSync": false,
        "type": "datasource"
      }
    ]
  },
  "time": {
    "from": "now-5m",
    "to": "now"
  },
  "timezone": "",
  "title": "Rolldice Application",
  "uid": "custom-rolldice",
  "version": 1
}
```

## File: `examples/java/dashboards-provisioning.yaml`
```yaml
apiVersion: 1

providers:
  - name: "Custom Dashboards"
    type: file
    options:
      path: /otel-lgtm/grafana/conf/provisioning/dashboards/custom
      foldersFromFilesStructure: false
```

## File: `examples/java/docker-compose.yml`
```yaml
services:
  lgtm:
    image: grafana/otel-lgtm
    ports:
      - "3000:3000"
      - "4317:4317"
      - "4318:4318"
    environment:
      GF_DASHBOARDS_DEFAULT_HOME_DASHBOARD_PATH: /otel-lgtm/grafana/conf/provisioning/dashboards/custom/custom-dashboard.json
    volumes:
      - ./custom-dashboard.json:/otel-lgtm/grafana/conf/provisioning/dashboards/custom/custom-dashboard.json:ro
      - ./dashboards-provisioning.yaml:/otel-lgtm/grafana/conf/provisioning/dashboards/custom.yaml:ro
    networks:
      - java-demo

  java:
    build:
      context: .
      dockerfile: Dockerfile
    environment:
      OTEL_SERVICE_NAME: "rolldice"
      OTEL_EXPORTER_OTLP_ENDPOINT: http://lgtm:4318
    ports:
      - "8080:8080"
    networks:
      - java-demo
    depends_on:
      - lgtm

networks:
  java-demo:
    driver: bridge
```

## File: `examples/java/mvnw`
```
#!/bin/sh
# ----------------------------------------------------------------------------
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
# ----------------------------------------------------------------------------

# ----------------------------------------------------------------------------
# Apache Maven Wrapper startup batch script, version 3.3.4
#
# Optional ENV vars
# -----------------
#   JAVA_HOME - location of a JDK home dir, required when download maven via java source
#   MVNW_REPOURL - repo url base for downloading maven distribution
#   MVNW_USERNAME/MVNW_PASSWORD - user and password for downloading maven
#   MVNW_VERBOSE - true: enable verbose log; debug: trace the mvnw script; others: silence the output
# ----------------------------------------------------------------------------

set -euf
[ "${MVNW_VERBOSE-}" != debug ] || set -x

# OS specific support.
native_path() { printf %s\\n "$1"; }
case "$(uname)" in
CYGWIN* | MINGW*)
  [ -z "${JAVA_HOME-}" ] || JAVA_HOME="$(cygpath --unix "$JAVA_HOME")"
  native_path() { cygpath --path --windows "$1"; }
  ;;
esac

# set JAVACMD and JAVACCMD
set_java_home() {
  # For Cygwin and MinGW, ensure paths are in Unix format before anything is touched
  if [ -n "${JAVA_HOME-}" ]; then
    if [ -x "$JAVA_HOME/jre/sh/java" ]; then
      # IBM's JDK on AIX uses strange locations for the executables
      JAVACMD="$JAVA_HOME/jre/sh/java"
      JAVACCMD="$JAVA_HOME/jre/sh/javac"
    else
      JAVACMD="$JAVA_HOME/bin/java"
      JAVACCMD="$JAVA_HOME/bin/javac"

      if [ ! -x "$JAVACMD" ] || [ ! -x "$JAVACCMD" ]; then
        echo "The JAVA_HOME environment variable is not defined correctly, so mvnw cannot run." >&2
        echo "JAVA_HOME is set to \"$JAVA_HOME\", but \"\$JAVA_HOME/bin/java\" or \"\$JAVA_HOME/bin/javac\" does not exist." >&2
        return 1
      fi
    fi
  else
    JAVACMD="$(
      'set' +e
      'unset' -f command 2>/dev/null
      'command' -v java
    )" || :
    JAVACCMD="$(
      'set' +e
      'unset' -f command 2>/dev/null
      'command' -v javac
    )" || :

    if [ ! -x "${JAVACMD-}" ] || [ ! -x "${JAVACCMD-}" ]; then
      echo "The java/javac command does not exist in PATH nor is JAVA_HOME set, so mvnw cannot run." >&2
      return 1
    fi
  fi
}

# hash string like Java String::hashCode
hash_string() {
  str="${1:-}" h=0
  while [ -n "$str" ]; do
    char="${str%"${str#?}"}"
    h=$(((h * 31 + $(LC_CTYPE=C printf %d "'$char")) % 4294967296))
    str="${str#?}"
  done
  printf %x\\n $h
}

verbose() { :; }
[ "${MVNW_VERBOSE-}" != true ] || verbose() { printf %s\\n "${1-}"; }

die() {
  printf %s\\n "$1" >&2
  exit 1
}

trim() {
  # MWRAPPER-139:
  #   Trims trailing and leading whitespace, carriage returns, tabs, and linefeeds.
  #   Needed for removing poorly interpreted newline sequences when running in more
  #   exotic environments such as mingw bash on Windows.
  printf "%s" "${1}" | tr -d '[:space:]'
}

scriptDir="$(dirname "$0")"
scriptName="$(basename "$0")"

# parse distributionUrl and optional distributionSha256Sum, requires .mvn/wrapper/maven-wrapper.properties
while IFS="=" read -r key value; do
  case "${key-}" in
  distributionUrl) distributionUrl=$(trim "${value-}") ;;
  distributionSha256Sum) distributionSha256Sum=$(trim "${value-}") ;;
  esac
done <"$scriptDir/.mvn/wrapper/maven-wrapper.properties"
[ -n "${distributionUrl-}" ] || die "cannot read distributionUrl property in $scriptDir/.mvn/wrapper/maven-wrapper.properties"

case "${distributionUrl##*/}" in
maven-mvnd-*bin.*)
  MVN_CMD=mvnd.sh _MVNW_REPO_PATTERN=/maven/mvnd/
  case "${PROCESSOR_ARCHITECTURE-}${PROCESSOR_ARCHITEW6432-}:$(uname -a)" in
  *AMD64:CYGWIN* | *AMD64:MINGW*) distributionPlatform=windows-amd64 ;;
  :Darwin*x86_64) distributionPlatform=darwin-amd64 ;;
  :Darwin*arm64) distributionPlatform=darwin-aarch64 ;;
  :Linux*x86_64*) distributionPlatform=linux-amd64 ;;
  *)
    echo "Cannot detect native platform for mvnd on $(uname)-$(uname -m), use pure java version" >&2
    distributionPlatform=linux-amd64
    ;;
  esac
  distributionUrl="${distributionUrl%-bin.*}-$distributionPlatform.zip"
  ;;
maven-mvnd-*) MVN_CMD=mvnd.sh _MVNW_REPO_PATTERN=/maven/mvnd/ ;;
*) MVN_CMD="mvn${scriptName#mvnw}" _MVNW_REPO_PATTERN=/org/apache/maven/ ;;
esac

# apply MVNW_REPOURL and calculate MAVEN_HOME
# maven home pattern: ~/.m2/wrapper/dists/{apache-maven-<version>,maven-mvnd-<version>-<platform>}/<hash>
[ -z "${MVNW_REPOURL-}" ] || distributionUrl="$MVNW_REPOURL$_MVNW_REPO_PATTERN${distributionUrl#*"$_MVNW_REPO_PATTERN"}"
distributionUrlName="${distributionUrl##*/}"
distributionUrlNameMain="${distributionUrlName%.*}"
distributionUrlNameMain="${distributionUrlNameMain%-bin}"
MAVEN_USER_HOME="${MAVEN_USER_HOME:-${HOME}/.m2}"
MAVEN_HOME="${MAVEN_USER_HOME}/wrapper/dists/${distributionUrlNameMain-}/$(hash_string "$distributionUrl")"

exec_maven() {
  unset MVNW_VERBOSE MVNW_USERNAME MVNW_PASSWORD MVNW_REPOURL || :
  exec "$MAVEN_HOME/bin/$MVN_CMD" "$@" || die "cannot exec $MAVEN_HOME/bin/$MVN_CMD"
}

if [ -d "$MAVEN_HOME" ]; then
  verbose "found existing MAVEN_HOME at $MAVEN_HOME"
  exec_maven "$@"
fi

case "${distributionUrl-}" in
*?-bin.zip | *?maven-mvnd-?*-?*.zip) ;;
*) die "distributionUrl is not valid, must match *-bin.zip or maven-mvnd-*.zip, but found '${distributionUrl-}'" ;;
esac

# prepare tmp dir
if TMP_DOWNLOAD_DIR="$(mktemp -d)" && [ -d "$TMP_DOWNLOAD_DIR" ]; then
  clean() { rm -rf -- "$TMP_DOWNLOAD_DIR"; }
  trap clean HUP INT TERM EXIT
else
  die "cannot create temp dir"
fi

mkdir -p -- "${MAVEN_HOME%/*}"

# Download and Install Apache Maven
verbose "Couldn't find MAVEN_HOME, downloading and installing it ..."
verbose "Downloading from: $distributionUrl"
verbose "Downloading to: $TMP_DOWNLOAD_DIR/$distributionUrlName"

# select .zip or .tar.gz
if ! command -v unzip >/dev/null; then
  distributionUrl="${distributionUrl%.zip}.tar.gz"
  distributionUrlName="${distributionUrl##*/}"
fi

# verbose opt
__MVNW_QUIET_WGET=--quiet __MVNW_QUIET_CURL=--silent __MVNW_QUIET_UNZIP=-q __MVNW_QUIET_TAR=''
[ "${MVNW_VERBOSE-}" != true ] || __MVNW_QUIET_WGET='' __MVNW_QUIET_CURL='' __MVNW_QUIET_UNZIP='' __MVNW_QUIET_TAR=v

# normalize http auth
case "${MVNW_PASSWORD:+has-password}" in
'') MVNW_USERNAME='' MVNW_PASSWORD='' ;;
has-password) [ -n "${MVNW_USERNAME-}" ] || MVNW_USERNAME='' MVNW_PASSWORD='' ;;
esac

if [ -z "${MVNW_USERNAME-}" ] && command -v wget >/dev/null; then
  verbose "Found wget ... using wget"
  wget ${__MVNW_QUIET_WGET:+"$__MVNW_QUIET_WGET"} "$distributionUrl" -O "$TMP_DOWNLOAD_DIR/$distributionUrlName" || die "wget: Failed to fetch $distributionUrl"
elif [ -z "${MVNW_USERNAME-}" ] && command -v curl >/dev/null; then
  verbose "Found curl ... using curl"
  curl ${__MVNW_QUIET_CURL:+"$__MVNW_QUIET_CURL"} -f -L -o "$TMP_DOWNLOAD_DIR/$distributionUrlName" "$distributionUrl" || die "curl: Failed to fetch $distributionUrl"
elif set_java_home; then
  verbose "Falling back to use Java to download"
  javaSource="$TMP_DOWNLOAD_DIR/Downloader.java"
  targetZip="$TMP_DOWNLOAD_DIR/$distributionUrlName"
  cat >"$javaSource" <<-END
	public class Downloader extends java.net.Authenticator
	{
	  protected java.net.PasswordAuthentication getPasswordAuthentication()
	  {
	    return new java.net.PasswordAuthentication( System.getenv( "MVNW_USERNAME" ), System.getenv( "MVNW_PASSWORD" ).toCharArray() );
	  }
	  public static void main( String[] args ) throws Exception
	  {
	    setDefault( new Downloader() );
	    java.nio.file.Files.copy( java.net.URI.create( args[0] ).toURL().openStream(), java.nio.file.Paths.get( args[1] ).toAbsolutePath().normalize() );
	  }
	}
	END
  # For Cygwin/MinGW, switch paths to Windows format before running javac and java
  verbose " - Compiling Downloader.java ..."
  "$(native_path "$JAVACCMD")" "$(native_path "$javaSource")" || die "Failed to compile Downloader.java"
  verbose " - Running Downloader.java ..."
  "$(native_path "$JAVACMD")" -cp "$(native_path "$TMP_DOWNLOAD_DIR")" Downloader "$distributionUrl" "$(native_path "$targetZip")"
fi

# If specified, validate the SHA-256 sum of the Maven distribution zip file
if [ -n "${distributionSha256Sum-}" ]; then
  distributionSha256Result=false
  if [ "$MVN_CMD" = mvnd.sh ]; then
    echo "Checksum validation is not supported for maven-mvnd." >&2
    echo "Please disable validation by removing 'distributionSha256Sum' from your maven-wrapper.properties." >&2
    exit 1
  elif command -v sha256sum >/dev/null; then
    if echo "$distributionSha256Sum  $TMP_DOWNLOAD_DIR/$distributionUrlName" | sha256sum -c - >/dev/null 2>&1; then
      distributionSha256Result=true
    fi
  elif command -v shasum >/dev/null; then
    if echo "$distributionSha256Sum  $TMP_DOWNLOAD_DIR/$distributionUrlName" | shasum -a 256 -c >/dev/null 2>&1; then
      distributionSha256Result=true
    fi
  else
    echo "Checksum validation was requested but neither 'sha256sum' or 'shasum' are available." >&2
    echo "Please install either command, or disable validation by removing 'distributionSha256Sum' from your maven-wrapper.properties." >&2
    exit 1
  fi
  if [ $distributionSha256Result = false ]; then
    echo "Error: Failed to validate Maven distribution SHA-256, your Maven distribution might be compromised." >&2
    echo "If you updated your Maven version, you need to update the specified distributionSha256Sum property." >&2
    exit 1
  fi
fi

# unzip and move
if command -v unzip >/dev/null; then
  unzip ${__MVNW_QUIET_UNZIP:+"$__MVNW_QUIET_UNZIP"} "$TMP_DOWNLOAD_DIR/$distributionUrlName" -d "$TMP_DOWNLOAD_DIR" || die "failed to unzip"
else
  tar xzf${__MVNW_QUIET_TAR:+"$__MVNW_QUIET_TAR"} "$TMP_DOWNLOAD_DIR/$distributionUrlName" -C "$TMP_DOWNLOAD_DIR" || die "failed to untar"
fi

# Find the actual extracted directory name (handles snapshots where filename != directory name)
actualDistributionDir=""

# First try the expected directory name (for regular distributions)
if [ -d "$TMP_DOWNLOAD_DIR/$distributionUrlNameMain" ]; then
  if [ -f "$TMP_DOWNLOAD_DIR/$distributionUrlNameMain/bin/$MVN_CMD" ]; then
    actualDistributionDir="$distributionUrlNameMain"
  fi
fi

# If not found, search for any directory with the Maven executable (for snapshots)
if [ -z "$actualDistributionDir" ]; then
  # enable globbing to iterate over items
  set +f
  for dir in "$TMP_DOWNLOAD_DIR"/*; do
    if [ -d "$dir" ]; then
      if [ -f "$dir/bin/$MVN_CMD" ]; then
        actualDistributionDir="$(basename "$dir")"
        break
      fi
    fi
  done
  set -f
fi

if [ -z "$actualDistributionDir" ]; then
  verbose "Contents of $TMP_DOWNLOAD_DIR:"
  verbose "$(ls -la "$TMP_DOWNLOAD_DIR")"
  die "Could not find Maven distribution directory in extracted archive"
fi

verbose "Found extracted Maven distribution directory: $actualDistributionDir"
printf %s\\n "$distributionUrl" >"$TMP_DOWNLOAD_DIR/$actualDistributionDir/mvnw.url"
mv -- "$TMP_DOWNLOAD_DIR/$actualDistributionDir" "$MAVEN_HOME" || [ -d "$MAVEN_HOME" ] || die "fail to move MAVEN_HOME"

clean || :
exec_maven "$@"
```

## File: `examples/java/mvnw.cmd`
```
<# : batch portion
@REM ----------------------------------------------------------------------------
@REM Licensed to the Apache Software Foundation (ASF) under one
@REM or more contributor license agreements.  See the NOTICE file
@REM distributed with this work for additional information
@REM regarding copyright ownership.  The ASF licenses this file
@REM to you under the Apache License, Version 2.0 (the
@REM "License"); you may not use this file except in compliance
@REM with the License.  You may obtain a copy of the License at
@REM
@REM    http://www.apache.org/licenses/LICENSE-2.0
@REM
@REM Unless required by applicable law or agreed to in writing,
@REM software distributed under the License is distributed on an
@REM "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
@REM KIND, either express or implied.  See the License for the
@REM specific language governing permissions and limitations
@REM under the License.
@REM ----------------------------------------------------------------------------

@REM ----------------------------------------------------------------------------
@REM Apache Maven Wrapper startup batch script, version 3.3.4
@REM
@REM Optional ENV vars
@REM   MVNW_REPOURL - repo url base for downloading maven distribution
@REM   MVNW_USERNAME/MVNW_PASSWORD - user and password for downloading maven
@REM   MVNW_VERBOSE - true: enable verbose log; others: silence the output
@REM ----------------------------------------------------------------------------

@IF "%__MVNW_ARG0_NAME__%"=="" (SET __MVNW_ARG0_NAME__=%~nx0)
@SET __MVNW_CMD__=
@SET __MVNW_ERROR__=
@SET __MVNW_PSMODULEP_SAVE=%PSModulePath%
@SET PSModulePath=
@FOR /F "usebackq tokens=1* delims==" %%A IN (`powershell -noprofile "& {$scriptDir='%~dp0'; $script='%__MVNW_ARG0_NAME__%'; icm -ScriptBlock ([Scriptblock]::Create((Get-Content -Raw '%~f0'))) -NoNewScope}"`) DO @(
  IF "%%A"=="MVN_CMD" (set __MVNW_CMD__=%%B) ELSE IF "%%B"=="" (echo %%A) ELSE (echo %%A=%%B)
)
@SET PSModulePath=%__MVNW_PSMODULEP_SAVE%
@SET __MVNW_PSMODULEP_SAVE=
@SET __MVNW_ARG0_NAME__=
@SET MVNW_USERNAME=
@SET MVNW_PASSWORD=
@IF NOT "%__MVNW_CMD__%"=="" ("%__MVNW_CMD__%" %*)
@echo Cannot start maven from wrapper >&2 && exit /b 1
@GOTO :EOF
: end batch / begin powershell #>

$ErrorActionPreference = "Stop"
if ($env:MVNW_VERBOSE -eq "true") {
  $VerbosePreference = "Continue"
}

# calculate distributionUrl, requires .mvn/wrapper/maven-wrapper.properties
$distributionUrl = (Get-Content -Raw "$scriptDir/.mvn/wrapper/maven-wrapper.properties" | ConvertFrom-StringData).distributionUrl
if (!$distributionUrl) {
  Write-Error "cannot read distributionUrl property in $scriptDir/.mvn/wrapper/maven-wrapper.properties"
}

switch -wildcard -casesensitive ( $($distributionUrl -replace '^.*/','') ) {
  "maven-mvnd-*" {
    $USE_MVND = $true
    $distributionUrl = $distributionUrl -replace '-bin\.[^.]*$',"-windows-amd64.zip"
    $MVN_CMD = "mvnd.cmd"
    break
  }
  default {
    $USE_MVND = $false
    $MVN_CMD = $script -replace '^mvnw','mvn'
    break
  }
}

# apply MVNW_REPOURL and calculate MAVEN_HOME
# maven home pattern: ~/.m2/wrapper/dists/{apache-maven-<version>,maven-mvnd-<version>-<platform>}/<hash>
if ($env:MVNW_REPOURL) {
  $MVNW_REPO_PATTERN = if ($USE_MVND -eq $False) { "/org/apache/maven/" } else { "/maven/mvnd/" }
  $distributionUrl = "$env:MVNW_REPOURL$MVNW_REPO_PATTERN$($distributionUrl -replace "^.*$MVNW_REPO_PATTERN",'')"
}
$distributionUrlName = $distributionUrl -replace '^.*/',''
$distributionUrlNameMain = $distributionUrlName -replace '\.[^.]*$','' -replace '-bin$',''

$MAVEN_M2_PATH = "$HOME/.m2"
if ($env:MAVEN_USER_HOME) {
  $MAVEN_M2_PATH = "$env:MAVEN_USER_HOME"
}

if (-not (Test-Path -Path $MAVEN_M2_PATH)) {
    New-Item -Path $MAVEN_M2_PATH -ItemType Directory | Out-Null
}

$MAVEN_WRAPPER_DISTS = $null
if ((Get-Item $MAVEN_M2_PATH).Target[0] -eq $null) {
  $MAVEN_WRAPPER_DISTS = "$MAVEN_M2_PATH/wrapper/dists"
} else {
  $MAVEN_WRAPPER_DISTS = (Get-Item $MAVEN_M2_PATH).Target[0] + "/wrapper/dists"
}

$MAVEN_HOME_PARENT = "$MAVEN_WRAPPER_DISTS/$distributionUrlNameMain"
$MAVEN_HOME_NAME = ([System.Security.Cryptography.SHA256]::Create().ComputeHash([byte[]][char[]]$distributionUrl) | ForEach-Object {$_.ToString("x2")}) -join ''
$MAVEN_HOME = "$MAVEN_HOME_PARENT/$MAVEN_HOME_NAME"

if (Test-Path -Path "$MAVEN_HOME" -PathType Container) {
  Write-Verbose "found existing MAVEN_HOME at $MAVEN_HOME"
  Write-Output "MVN_CMD=$MAVEN_HOME/bin/$MVN_CMD"
  exit $?
}

if (! $distributionUrlNameMain -or ($distributionUrlName -eq $distributionUrlNameMain)) {
  Write-Error "distributionUrl is not valid, must end with *-bin.zip, but found $distributionUrl"
}

# prepare tmp dir
$TMP_DOWNLOAD_DIR_HOLDER = New-TemporaryFile
$TMP_DOWNLOAD_DIR = New-Item -Itemtype Directory -Path "$TMP_DOWNLOAD_DIR_HOLDER.dir"
$TMP_DOWNLOAD_DIR_HOLDER.Delete() | Out-Null
trap {
  if ($TMP_DOWNLOAD_DIR.Exists) {
    try { Remove-Item $TMP_DOWNLOAD_DIR -Recurse -Force | Out-Null }
    catch { Write-Warning "Cannot remove $TMP_DOWNLOAD_DIR" }
  }
}

New-Item -Itemtype Directory -Path "$MAVEN_HOME_PARENT" -Force | Out-Null

# Download and Install Apache Maven
Write-Verbose "Couldn't find MAVEN_HOME, downloading and installing it ..."
Write-Verbose "Downloading from: $distributionUrl"
Write-Verbose "Downloading to: $TMP_DOWNLOAD_DIR/$distributionUrlName"

$webclient = New-Object System.Net.WebClient
if ($env:MVNW_USERNAME -and $env:MVNW_PASSWORD) {
  $webclient.Credentials = New-Object System.Net.NetworkCredential($env:MVNW_USERNAME, $env:MVNW_PASSWORD)
}
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
$webclient.DownloadFile($distributionUrl, "$TMP_DOWNLOAD_DIR/$distributionUrlName") | Out-Null

# If specified, validate the SHA-256 sum of the Maven distribution zip file
$distributionSha256Sum = (Get-Content -Raw "$scriptDir/.mvn/wrapper/maven-wrapper.properties" | ConvertFrom-StringData).distributionSha256Sum
if ($distributionSha256Sum) {
  if ($USE_MVND) {
    Write-Error "Checksum validation is not supported for maven-mvnd. `nPlease disable validation by removing 'distributionSha256Sum' from your maven-wrapper.properties."
  }
  Import-Module $PSHOME\Modules\Microsoft.PowerShell.Utility -Function Get-FileHash
  if ((Get-FileHash "$TMP_DOWNLOAD_DIR/$distributionUrlName" -Algorithm SHA256).Hash.ToLower() -ne $distributionSha256Sum) {
    Write-Error "Error: Failed to validate Maven distribution SHA-256, your Maven distribution might be compromised. If you updated your Maven version, you need to update the specified distributionSha256Sum property."
  }
}

# unzip and move
Expand-Archive "$TMP_DOWNLOAD_DIR/$distributionUrlName" -DestinationPath "$TMP_DOWNLOAD_DIR" | Out-Null

# Find the actual extracted directory name (handles snapshots where filename != directory name)
$actualDistributionDir = ""

# First try the expected directory name (for regular distributions)
$expectedPath = Join-Path "$TMP_DOWNLOAD_DIR" "$distributionUrlNameMain"
$expectedMvnPath = Join-Path "$expectedPath" "bin/$MVN_CMD"
if ((Test-Path -Path $expectedPath -PathType Container) -and (Test-Path -Path $expectedMvnPath -PathType Leaf)) {
  $actualDistributionDir = $distributionUrlNameMain
}

# If not found, search for any directory with the Maven executable (for snapshots)
if (!$actualDistributionDir) {
  Get-ChildItem -Path "$TMP_DOWNLOAD_DIR" -Directory | ForEach-Object {
    $testPath = Join-Path $_.FullName "bin/$MVN_CMD"
    if (Test-Path -Path $testPath -PathType Leaf) {
      $actualDistributionDir = $_.Name
    }
  }
}

if (!$actualDistributionDir) {
  Write-Error "Could not find Maven distribution directory in extracted archive"
}

Write-Verbose "Found extracted Maven distribution directory: $actualDistributionDir"
Rename-Item -Path "$TMP_DOWNLOAD_DIR/$actualDistributionDir" -NewName $MAVEN_HOME_NAME | Out-Null
try {
  Move-Item -Path "$TMP_DOWNLOAD_DIR/$MAVEN_HOME_NAME" -Destination $MAVEN_HOME_PARENT | Out-Null
} catch {
  if (! (Test-Path -Path "$MAVEN_HOME" -PathType Container)) {
    Write-Error "fail to move MAVEN_HOME"
  }
} finally {
  try { Remove-Item $TMP_DOWNLOAD_DIR -Recurse -Force | Out-Null }
  catch { Write-Warning "Cannot remove $TMP_DOWNLOAD_DIR" }
}

Write-Output "MVN_CMD=$MAVEN_HOME/bin/$MVN_CMD"
```

## File: `examples/java/pom.xml`
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>com.grafana.example</groupId>
    <artifactId>rolldice</artifactId>
    <version>1.0.0-SNAPSHOT</version>

    <name>Hello World REST Service</name>

    <properties>
        <spring.version>4.0.5</spring.version>
        <maven.compiler.source>17</maven.compiler.source>
        <maven.compiler.target>17</maven.compiler.target>
    </properties>

    <dependencyManagement>
        <dependencies>
            <dependency>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-dependencies</artifactId>
                <version>${spring.version}</version>
                <type>pom</type>
                <scope>import</scope>
            </dependency>
        </dependencies>
    </dependencyManagement>

    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>
    </dependencies>

    <build>
        <finalName>${project.artifactId}</finalName>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
                <executions>
                    <execution>
                        <goals>
                            <goal>repackage</goal>
                        </goals>
                    </execution>
                </executions>
            </plugin>
        </plugins>
    </build>
</project>
```

## File: `examples/java/run.cmd`
```
@REM @echo off

if not exist ./target/rolldice.jar (
    mvnw clean package
)

set version=v2.1.0
set jar=opentelemetry-javaagent-%version%.jar
if not exist ./%jar% (
    curl -sL https://github.com/open-telemetry/opentelemetry-java-instrumentation/releases/download/%version%/opentelemetry-javaagent.jar -o %jar%
)

set OTEL_RESOURCE_ATTRIBUTES=service.name=rolldice,service.instance.id=127.0.0.1:8080
@REM uncomment the next line to switch to Prometheus native histograms.
@REM set OTEL_EXPORTER_OTLP_METRICS_DEFAULT_HISTOGRAM_AGGREGATION=base2_exponential_bucket_histogram
java -Dotel.metric.export.interval=500 -Dotel.bsp.schedule.delay=500 -javaagent:%jar% -jar ./target/rolldice.jar
```

## File: `examples/java/run.sh`
```bash
#!/bin/bash

set -euox pipefail

if [[ ! -f ./target/rolldice.jar ]]; then
	./mvnw clean package
fi

# renovate: datasource=github-releases depName=opentelemetry-java-instrumentation packageName=open-telemetry/opentelemetry-java-instrumentation
opentelemetry_javaagent_version=2.26.1
jar=opentelemetry-javaagent-${opentelemetry_javaagent_version}.jar
if [[ ! -f ./${jar} ]]; then
	curl -vL https://github.com/open-telemetry/opentelemetry-java-instrumentation/releases/download/v${opentelemetry_javaagent_version}/opentelemetry-javaagent.jar -o ${jar} # editorconfig-checker-disable-line

fi
export OTEL_RESOURCE_ATTRIBUTES="service.name=rolldice,service.instance.id=127.0.0.1:8080"
# uncomment the next line to switch to Prometheus native histograms.
# export OTEL_EXPORTER_OTLP_METRICS_DEFAULT_HISTOGRAM_AGGREGATION=base2_exponential_bucket_histogram
java -Dotel.metric.export.interval=500 -Dotel.bsp.schedule.delay=500 -javaagent:${jar} -jar ./target/rolldice.jar
```

## File: `examples/java/json-logging-ecs/Dockerfile`
```
FROM eclipse-temurin:25.0.2_10-jdk@sha256:bee2e23ab444ed60daf8123e36478bc4a286ba7835bec6f9daf9eba1d50a86a2 AS builder

WORKDIR /usr/src/app/

COPY ./mvnw pom.xml ./
COPY ./.mvn ./.mvn
COPY ./src ./src
COPY json-logging-ecs/logback-spring.xml ./src/main/resources/logback-spring.xml
RUN sed -i '/<dependencies>/a <dependency><groupId>co.elastic.logging</groupId><artifactId>logback-ecs-encoder</artifactId><version>1.6.0</version></dependency>' pom.xml
RUN --mount=type=cache,target=/root/.m2 ./mvnw install -DskipTests

FROM eclipse-temurin:25.0.2_10-jre@sha256:a9980cb3777d2b7b0d513800c3debc034c101530b96db4aadccb845f867fca9e

WORKDIR /usr/src/app/

COPY --from=builder /usr/src/app/target/rolldice.jar ./app.jar
# we ignore the version (which is from upstream) and use the latest version of the grafana distribution
ADD --chmod=644 https://github.com/open-telemetry/opentelemetry-java-instrumentation/releases/latest/download/opentelemetry-javaagent.jar /usr/src/app/opentelemetry-javaagent.jar
ENV JAVA_TOOL_OPTIONS=-javaagent:/usr/src/app/opentelemetry-javaagent.jar

EXPOSE 8080
ENTRYPOINT [ "java", "-jar", "./app.jar" ]
```

## File: `examples/java/json-logging-ecs/README.md`
```markdown
# Exporting Application logs using Elastic Common Schema (ECS) logging in Kubernetes

## Running the example

1. Build the Docker image using using `build.sh`
2. Deploy the manifest using `kubectl apply -f k8s/` (e.g.
   using [k3d.sh](k3d.sh))
3. Generate traffic
   using [generate-traffic.sh](../../../generate-traffic.sh)
4. Log in to [http://127.0.0.1:3000](http://127.0.0.1:3000) with user _admin_ and password _admin_.
5. Go to "Explore"
6. Select "Loki" as data source
```

## File: `examples/java/json-logging-ecs/build.sh`
```bash
#!/bin/bash

set -euo pipefail

docker build -f Dockerfile -t "dice:1.1-SNAPSHOT" ..
```

## File: `examples/java/json-logging-ecs/k3d.sh`
```bash
#!/bin/bash

set -euo pipefail

./build.sh
k3d cluster create jsonlogging || k3d cluster start jsonlogging
k3d image import -c jsonlogging dice:1.1-SNAPSHOT

kubectl apply -f k8s/

kubectl wait --for=condition=ready pod -l app=dice
kubectl wait --for=condition=ready --timeout=5m pod -l app=lgtm

kubectl port-forward service/dice 8080:8080 &
kubectl port-forward service/lgtm 3000:3000 &
```

## File: `examples/java/json-logging-ecs/logback-spring.xml`
```xml
<configuration>
    <include resource="co/elastic/logging/logback/boot/ecs-console-appender.xml" />

    <root level="info">
        <appender-ref ref="ECS_JSON_CONSOLE"/>
    </root>
</configuration>
```

## File: `examples/java/json-logging-ecs/k8s/collector-configmap.yaml`
```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: otel-collector-config
data:
  otel-collector-config.yaml: |-
    receivers:
      otlp:
        protocols:
          grpc:
            endpoint: 0.0.0.0:4317
          http:
            endpoint: 0.0.0.0:4318
      prometheus/collector: # needed if you use the docker-lgtm image
        config:
          scrape_configs:
            - job_name: 'opentelemetry-collector'
              static_configs:
                - targets: [ '127.0.0.1:8888' ]
      filelog/json-ecs:
        include:
          - /var/log/pods/*/*/*.log
        include_file_path: true
        operators:
          - id: container-parser
            type: container
          - id: router
            type: router
            routes:
              - output: json_parser
                expr: 'body matches "\\{[^{}]*\\}" == true'
          - id: json_parser
            type: json_parser
            on_error: drop_quiet
            body: attributes.message
            timestamp:
              parse_from: attributes["@timestamp"]
              layout: '%Y-%m-%dT%H:%M:%S.%LZ'
            severity:
              parse_from: attributes["log.level"]
            trace:
              trace_id:
                parse_from: attributes.trace_id
              span_id:
                parse_from: attributes.span_id
            scope_name:
              parse_from: attributes["log.logger"]
          - id: move_service_namespace
            type: move
            if: 'attributes["service.namespace"] != nil'
            from: attributes["service.namespace"]
            to: resource["service.namespace"]
          - id: move_service_name
            type: move
            from: attributes["service.name"]
            to: resource["service.name"]
          - id: move_service_instance_id
            type: move
            if: 'attributes["service.instance.id"] != nil'
            from: attributes["service.instance.id"]
            to: resource["service.instance.id"]
          - id: move_deployment_environment
            type: move
            if: 'attributes["deployment.environment"] != nil'
            from: attributes["deployment.environment"]
            to: resource["deployment.environment"]
          - id: move_thread_name
            type: move
            from: attributes["process.thread.name"]
            to: attributes["thread.name"]
          - id: move_error_message
            type: move
            if: 'attributes["error.message"] != nil'
            from: attributes["error.message"]
            to: attributes["exception.message"]
          - id: move_error_type
            type: move
            if: 'attributes["error.type"] != nil'
            from: attributes["error.type"]
            to: attributes["exception.type"]
          - id: move_throwable_stacktrace
            type: move
            if: 'len(attributes["error.stack_trace"]) > 0'
            from: attributes["error.stack_trace"]
            to: attributes["exception.stacktrace"]
          - id: remove_logger_name
            type: remove
            field: attributes["log.logger"]
          - id: remove_timestamp
            type: remove
            field: attributes["@timestamp"]
          - id: remove_level
            type: remove
            field: attributes["log.level"]
          - id: remove_span_id
            if: 'attributes["span_id"] != nil'
            type: remove
            field: attributes.span_id
          - id: remove_trace_id
            if: 'attributes["trace_id"] != nil'
            type: remove
            field: attributes.trace_id
          - id: remove_message
            type: remove
            field: attributes.message
          - id: remove_ecs_version
            type: remove
            field: attributes["ecs.version"]
          - id: remove_ecs_event_dataset
            type: remove
            field: attributes["event.dataset"]
          - id: remove_trace_flags
            type: remove
            field: attributes["trace_flags"]
          - id: remove_logtag
            type: remove
            field: attributes.logtag
          - id: remove_file
            type: remove
            field: attributes["log.file.path"]
          - id: remove_filename
            type: remove
            field: attributes["log.file.name"]
          - id: remove_stream
            type: remove
            field: attributes["log.iostream"]
          - id: remove_time
            type: remove
            field: attributes.time

    processors:
      batch:
      resourcedetection:
        detectors: [ "env", "system" ]
        override: false

    exporters:
      otlphttp/metrics:
        endpoint: http://127.0.0.1:9090/api/v1/otlp
      otlphttp/traces:
        endpoint: http://127.0.0.1:4418
      otlphttp/logs:
        endpoint: http://127.0.0.1:3100/otlp
      debug/metrics:
        verbosity: detailed
      debug/traces:
        verbosity: detailed
      debug/logs:
        verbosity: detailed
      nop:

    service:
      pipelines:
        traces:
          receivers: [ otlp ]
          processors: [ batch ]
          exporters: [ otlphttp/traces ]
        metrics:
          receivers: [ otlp, prometheus/collector ]
          processors: [ batch ]
          exporters: [ otlphttp/metrics ]
        logs/otlp:
          receivers: [ otlp ]
          processors: [ batch ]
          exporters: [ otlphttp/logs ]
        logs/json-ecs:
          receivers: [ filelog/json-ecs ]
          processors: [ batch ]
          exporters: [ otlphttp/logs ]
          # exporters: [ otlphttp/logs, debug/logs ]  # Uncomment this line to enable debug logging
```

## File: `examples/java/json-logging-ecs/k8s/dice.yaml`
```yaml
---
apiVersion: v1
kind: Service
metadata:
  name: dice
spec:
  selector:
    app: dice
  ports:
    - protocol: TCP
      port: 8080
      targetPort: 8080
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: dice
spec:
  replicas: 1
  selector:
    matchLabels:
      app: dice
  template:
    metadata:
      labels:
        app: dice
    spec:
      containers:
        - name: dice
          image: dice:1.1-SNAPSHOT
          imagePullPolicy: Never
          ports:
            - containerPort: 8080
          env:
            - name: OTEL_EXPORTER_OTLP_ENDPOINT
              value: "http://lgtm:4318"
            - name: OTEL_LOGS_EXPORTER
              value: "none" # to avoid duplicate logs
            - name: OTEL_RESOURCE_ATTRIBUTES
              value: service.name=dice,service.namespace=shop,service.version=1.1,deployment.environment=staging
            - name: OTEL_INSTRUMENTATION_COMMON_MDC_RESOURCE_ATTRIBUTES
              value: "service.namespace,service.instance.id,deployment.environment"
            - name: SERVICE_NAME
              value: dice
```

## File: `examples/java/json-logging-ecs/k8s/lgtm.yaml`
```yaml
---
apiVersion: v1
kind: Service
metadata:
  name: lgtm
spec:
  selector:
    app: lgtm
  ports:
    - name: grafana
      protocol: TCP
      port: 3000
      targetPort: 3000
    - name: pyroscope
      protocol: TCP
      port: 4040
      targetPort: 4040
    - name: otel-grpc
      protocol: TCP
      port: 4317
      targetPort: 4317
    - name: otel-http
      protocol: TCP
      port: 4318
      targetPort: 4318
    - name: prometheus # needed for automated tests
      protocol: TCP
      port: 9090
      targetPort: 9090
    - name: loki # needed for automated tests
      protocol: TCP
      port: 3100
      targetPort: 3100
    - name: tempo # needed for automated tests
      protocol: TCP
      port: 3200
      targetPort: 3200
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: lgtm
spec:
  replicas: 1
  selector:
    matchLabels:
      app: lgtm
  template:
    metadata:
      labels:
        app: lgtm
    spec:
      containers:
        - name: lgtm
          image: grafana/otel-lgtm:latest
          ports:
            - containerPort: 3000
            - containerPort: 4040
            - containerPort: 4317
            - containerPort: 4318
            - containerPort: 9090 # needed for automated tests
            - containerPort: 3100 # needed for automated tests
            - containerPort: 3200 # needed for automated tests
          readinessProbe:
            exec:
              command:
                - cat
                - /tmp/ready
          volumeMounts:
            - mountPath: /otel-lgtm/otelcol-config.yaml
              name: otel-collector-config
              subPath: otel-collector-config.yaml
              readOnly: true
            - mountPath: /var/log
              name: varlog
              readOnly: true
            - mountPath: /var/lib/docker/containers
              name: varlibdockercontainers
              readOnly: true
          env:
            - name: ENABLE_LOGS_OTELCOL
              value: "true"
      volumes:
        - name: otel-collector-config
          configMap:
            name: otel-collector-config
        - name: varlog
          hostPath:
            path: /var/log
        - name: varlibdockercontainers
          hostPath:
            path: /var/lib/docker/containers
```

## File: `examples/java/json-logging-logback/Dockerfile`
```
FROM eclipse-temurin:25.0.2_10-jdk@sha256:bee2e23ab444ed60daf8123e36478bc4a286ba7835bec6f9daf9eba1d50a86a2 AS builder

WORKDIR /usr/src/app/

COPY ./mvnw pom.xml ./
COPY ./.mvn ./.mvn
COPY ./src ./src
COPY json-logging-logback/logback-spring.xml ./src/main/resources/logback-spring.xml
RUN --mount=type=cache,target=/root/.m2 ./mvnw install -DskipTests

FROM eclipse-temurin:25.0.2_10-jre@sha256:a9980cb3777d2b7b0d513800c3debc034c101530b96db4aadccb845f867fca9e

WORKDIR /usr/src/app/

COPY --from=builder /usr/src/app/target/rolldice.jar ./app.jar
# we ignore the version (which is from upstream) and use the latest version of the grafana distribution
ADD --chmod=644 https://github.com/open-telemetry/opentelemetry-java-instrumentation/releases/latest/download/opentelemetry-javaagent.jar /usr/src/app/opentelemetry-javaagent.jar
ENV JAVA_TOOL_OPTIONS=-javaagent:/usr/src/app/opentelemetry-javaagent.jar

EXPOSE 8080
ENTRYPOINT [ "java", "-jar", "./app.jar" ]
```

## File: `examples/java/json-logging-logback/README.md`
```markdown
# Exporting Application logs using JSON logging in Kubernetes

## Running the example

1. Build the Docker image using using `build.sh`
2. Deploy the manifest using `kubectl apply -f k8s/` (e.g.
   using [k3d.sh](k3d.sh))
3. Generate traffic
   using [generate-traffic.sh](../../../generate-traffic.sh)
4. Log in to [http://127.0.0.1:3000](http://127.0.0.1:3000) with user _admin_ and password _admin_.
5. Go to "Explore"
6. Select "Loki" as data source
```

## File: `examples/java/json-logging-logback/build.sh`
```bash
#!/bin/bash

set -euo pipefail

docker build -f Dockerfile -t "dice:1.1-SNAPSHOT" ..
```

## File: `examples/java/json-logging-logback/k3d.sh`
```bash
#!/bin/bash

set -euo pipefail

./build.sh
k3d cluster create jsonlogging || k3d cluster start jsonlogging
k3d image import -c jsonlogging dice:1.1-SNAPSHOT

kubectl apply -f k8s/

kubectl wait --for=condition=ready pod -l app=dice
kubectl wait --for=condition=ready --timeout=5m pod -l app=lgtm

kubectl port-forward service/dice 8080:8080 &
kubectl port-forward service/lgtm 3000:3000 &
```

## File: `examples/java/json-logging-logback/logback-spring.xml`
```xml
<?xml version="1.0" encoding="UTF-8"?>
<configuration>
    <include resource="org/springframework/boot/logging/logback/defaults.xml"/>
    <include resource="org/springframework/boot/logging/logback/console-appender.xml"/>

    <root level="INFO">
        <appender-ref ref="CONSOLE_JSON"/>
    </root>

    <appender name="CONSOLE_JSON" class="ch.qos.logback.core.ConsoleAppender">
        <encoder class="ch.qos.logback.classic.encoder.JsonEncoder">
            <withFormattedMessage>true</withFormattedMessage>
            <withMessage>false</withMessage>
            <withArguments>false</withArguments>
            <withSequenceNumber>false</withSequenceNumber>
            <withNanoseconds>false</withNanoseconds>
        </encoder>
    </appender>
</configuration>
```

## File: `examples/java/json-logging-logback/k8s/collector-configmap.yaml`
```yaml
---
apiVersion: v1
kind: ConfigMap
metadata:
  name: otel-collector-config
data:
  otel-collector-config.yaml: |-
    receivers:
      otlp:
        protocols:
          grpc:
            endpoint: 0.0.0.0:4317
          http:
            endpoint: 0.0.0.0:4318
      prometheus/collector: # needed if you use the docker-lgtm image
        config:
          scrape_configs:
            - job_name: 'opentelemetry-collector'
              static_configs:
                - targets: [ '127.0.0.1:8888' ]
      filelog/json-logback:
        include:
          - /var/log/pods/*/*/*.log
        include_file_path: true
        operators:
          - id: container-parser
            type: container
          - id: router
            type: router
            routes:
              - output: json_parser
                expr: 'body matches "\\{[^{}]*\\}" == true'
          - id: json_parser
            type: json_parser
            on_error: drop_quiet
            body: attributes.formattedMessage
            timestamp:
              parse_from: attributes.timestamp
              layout_type: 'epoch'
              layout: 'ms'
            severity:
              parse_from: attributes.level
            trace:
              trace_id:
                parse_from: attributes.mdc.trace_id
              span_id:
                parse_from: attributes.mdc.span_id
              trace_flags:
                parse_from: attributes.mdc.trace_flags
            scope_name:
              parse_from: attributes.loggerName
          - id: move_service_namespace
            type: move
            if: 'attributes.mdc["service.namespace"] != nil'
            from: attributes.mdc["service.namespace"]
            to: resource["service.namespace"]
          - id: move_service_name
            type: move
            from: attributes.mdc["service.name"]
            to: resource["service.name"]
          - id: move_service_version
            type: move
            from: attributes.mdc["service.version"]
            to: resource["service.version"]
          - id: move_service_instance_id
            type: move
            if: 'attributes.mdc["service.instance.id"] != nil'
            from: attributes.mdc["service.instance.id"]
            to: resource["service.instance.id"]
          - id: move_deployment_environment
            type: move
            if: 'attributes.mdc["deployment.environment"] != nil'
            from: attributes.mdc["deployment.environment"]
            to: resource["deployment.environment"]
          - id: move_thread_name
            type: move
            from: attributes.threadName
            to: attributes["thread.name"]
          - id: move_throwable_class_name
            type: move
            if: "attributes.throwable?.className != nil"
            from: attributes.throwable.className
            to: attributes["exception.type"]
          - id: move_throwable_message
            type: move
            if: "attributes.throwable?.message != nil"
            from: attributes.throwable.message
            to: attributes["exception.message"]
          # FIXME "stepArray" is a json array eroding the visualization in Loki
          # [{ "className": "a.b.C", "methodName": "do", "fileName": "C.java", "lineNumber": 123},...]
          # It would help if logBack had a raw toString of the stack trace
          - id: move_throwable_stack_trace
            type: move
            if: "attributes.throwable?.stepArray != nil"
            from: attributes.throwable.stepArray
            to: attributes["exception.stacktrace"]
          - id: remove_throwable
            type: remove
            field: attributes.throwable
          - id: remove_logger_name
            type: remove
            field: attributes.loggerName
          - id: remove_timestamp
            type: remove
            field: attributes.timestamp
          - id: remove_observed_timestamp
            type: remove
            field: attributes["observed.timestamp"]
          - id: remove_level
            type: remove
            field: attributes.level
          - id: remove_detected_level
            type: remove
            field: attributes["detected.level"]
          - id: remove_mdc
            type: remove
            field: attributes.mdc
          - id: remove_context
            type: remove
            field: attributes.context
          - id: remove_formattedMessage
            type: remove
            field: attributes.formattedMessage
          - id: remove_logtag
            type: remove
            field: attributes.logtag
          - id: remove_file
            type: remove
            field: attributes["log.file.path"]
          - id: remove_filename
            type: remove
            field: attributes["log.file.name"]
          - id: remove_stream
            type: remove
            field: attributes["log.iostream"]
          - id: remove_time
            type: remove
            field: attributes.time

    processors:
      batch:
      resourcedetection:
        detectors: [ "env", "system" ]
        override: false

    exporters:
      otlphttp/metrics:
        endpoint: http://127.0.0.1:9090/api/v1/otlp
      otlphttp/traces:
        endpoint: http://127.0.0.1:4418
      otlphttp/logs:
        endpoint: http://127.0.0.1:3100/otlp
      debug/metrics:
        verbosity: detailed
      debug/traces:
        verbosity: detailed
      debug/logs:
        verbosity: detailed
      nop:

    service:
      pipelines:
        traces:
          receivers: [ otlp ]
          processors: [ batch ]
          exporters: [ otlphttp/traces ]
        metrics:
          receivers: [ otlp, prometheus/collector ]
          processors: [ batch ]
          exporters: [ otlphttp/metrics ]
        logs/otlp:
          receivers: [ otlp ]
          processors: [ batch ]
          exporters: [ otlphttp/logs ]
        logs/json-elastic:
          receivers: [ filelog/json-logback ]
          processors: [ batch ]
          exporters: [ otlphttp/logs ]
          # exporters: [ otlphttp/logs, debug/logs ]  # Uncomment this line to enable debug logging
```

## File: `examples/java/json-logging-logback/k8s/dice.yaml`
```yaml
---
apiVersion: v1
kind: Service
metadata:
  name: dice
spec:
  selector:
    app: dice
  ports:
    - protocol: TCP
      port: 8080
      targetPort: 8080
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: dice
spec:
  replicas: 1
  selector:
    matchLabels:
      app: dice
  template:
    metadata:
      labels:
        app: dice
    spec:
      containers:
        - name: dice
          image: dice:1.1-SNAPSHOT
          imagePullPolicy: Never
          ports:
            - containerPort: 8080
          env:
            - name: OTEL_EXPORTER_OTLP_ENDPOINT
              value: "http://lgtm:4318"
            - name: OTEL_LOGS_EXPORTER
              value: "none" # to avoid duplicate logs
            - name: OTEL_RESOURCE_ATTRIBUTES
              value: service.name=dice,service.namespace=shop,service.version=1.1,deployment.environment=staging
            - name: OTEL_INSTRUMENTATION_COMMON_MDC_RESOURCE_ATTRIBUTES
              value: "service.namespace,service.name,service.instance.id,service.version,deployment.environment"
            - name: SERVICE_NAME
              value: dice
```

## File: `examples/java/json-logging-logback/k8s/lgtm.yaml`
```yaml
---
apiVersion: v1
kind: Service
metadata:
  name: lgtm
spec:
  selector:
    app: lgtm
  ports:
    - name: grafana
      protocol: TCP
      port: 3000
      targetPort: 3000
    - name: otel-grpc
      protocol: TCP
      port: 4317
      targetPort: 4317
    - name: otel-http
      protocol: TCP
      port: 4318
      targetPort: 4318
    - name: prometheus # needed for automated tests
      protocol: TCP
      port: 9090
      targetPort: 9090
    - name: loki # needed for automated tests
      protocol: TCP
      port: 3100
      targetPort: 3100
    - name: tempo # needed for automated tests
      protocol: TCP
      port: 3200
      targetPort: 3200
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: lgtm
spec:
  replicas: 1
  selector:
    matchLabels:
      app: lgtm
  template:
    metadata:
      labels:
        app: lgtm
    spec:
      containers:
        - name: lgtm
          image: grafana/otel-lgtm:latest
          ports:
            - containerPort: 3000
            - containerPort: 4317
            - containerPort: 4318
            - containerPort: 9090 # needed for automated tests
            - containerPort: 3100 # needed for automated tests
            - containerPort: 3200 # needed for automated tests
          readinessProbe:
            exec:
              command:
                - cat
                - /tmp/ready
          volumeMounts:
            - mountPath: /otel-lgtm/otelcol-config.yaml
              name: otel-collector-config
              subPath: otel-collector-config.yaml
              readOnly: true
            - mountPath: /var/log
              name: varlog
              readOnly: true
            - mountPath: /var/lib/docker/containers
              name: varlibdockercontainers
              readOnly: true
          env:
            - name: ENABLE_LOGS_OTELCOL
              value: "true"
      volumes:
        - name: otel-collector-config
          configMap:
            name: otel-collector-config
        - name: varlog
          hostPath:
            path: /var/log
        - name: varlibdockercontainers
          hostPath:
            path: /var/lib/docker/containers
```

## File: `examples/java/json-logging-otlp/Dockerfile`
```
FROM ghcr.io/open-telemetry/opentelemetry-operator/autoinstrumentation-java:2.26.1@sha256:dc0c94818e271f4d24ffe44b6894989c5d9c9d7302289bb8559f17dac7b1b159 AS agent

FROM eclipse-temurin:25.0.2_10-jdk@sha256:bee2e23ab444ed60daf8123e36478bc4a286ba7835bec6f9daf9eba1d50a86a2 AS builder

WORKDIR /usr/src/app/

COPY ./mvnw pom.xml ./
COPY ./.mvn ./.mvn
COPY ./src ./src
COPY json-logging-otlp/logback-spring.xml ./src/main/resources/logback-spring.xml
RUN --mount=type=cache,target=/root/.m2 ./mvnw install -DskipTests

FROM eclipse-temurin:25.0.2_10-jre@sha256:a9980cb3777d2b7b0d513800c3debc034c101530b96db4aadccb845f867fca9e

WORKDIR /usr/src/app/

COPY --from=agent --chown=cnb /javaagent.jar /app/javaagent.jar
ENV JAVA_TOOL_OPTIONS=-javaagent:/app/javaagent.jar
COPY --from=builder /usr/src/app/target/rolldice.jar ./app.jar

EXPOSE 8080
ENTRYPOINT [ "java", "-jar", "./app.jar" ]
```

## File: `examples/java/json-logging-otlp/README.md`
```markdown
# Exporting Application logs using OTLP logging in Kubernetes

## Running the example

1. Build the Docker image using using `build.sh`
2. Deploy the manifest using `kubectl apply -f k8s/` (e.g.
   using [k3d.sh](k3d.sh))
3. Generate traffic
   using [generate-traffic.sh](../../../generate-traffic.sh)
4. Log in to [http://127.0.0.1:3000](http://127.0.0.1:3000) with user _admin_ and password _admin_.
5. Go to "Explore"
6. Select "Loki" as data source
```

## File: `examples/java/json-logging-otlp/build.sh`
```bash
#!/bin/bash

set -euo pipefail

docker build -f Dockerfile -t "dice:1.1-SNAPSHOT" ..
```

## File: `examples/java/json-logging-otlp/k3d.sh`
```bash
#!/bin/bash

set -euo pipefail

./build.sh
k3d cluster create jsonlogging || k3d cluster start jsonlogging
k3d image import -c jsonlogging dice:1.1-SNAPSHOT

kubectl apply -f k8s/

kubectl wait --for=condition=ready pod -l app=dice
kubectl wait --for=condition=ready --timeout=5m pod -l app=lgtm

kubectl port-forward service/dice 8080:8080 &
kubectl port-forward service/lgtm 3000:3000 &
```

## File: `examples/java/json-logging-otlp/logback-spring.xml`
```xml
<?xml version="1.0" encoding="UTF-8"?>
<configuration>
    <root level="INFO">
    </root>
</configuration>
```

## File: `examples/java/json-logging-otlp/k8s/collector-configmap.yaml`
```yaml
---
apiVersion: v1
kind: ConfigMap
metadata:
  name: otel-collector-config
data:
  otel-collector-config.yaml: |-
    receivers:
      otlp:
        protocols:
          grpc:
            endpoint: 0.0.0.0:4317
          http:
            endpoint: 0.0.0.0:4318
      prometheus/collector: # needed if you use the docker-lgtm image
        config:
          scrape_configs:
            - job_name: 'opentelemetry-collector'
              static_configs:
                - targets: [ 'localhost:8888' ]
      filelog/otlp-json-logs:
        include:
          - /var/log/pods/*/*/*.log
        include_file_path: true
        operators:
          - id: container-parser
            type: container

    processors:
      batch:
      resourcedetection:
        detectors: [ "env", "system" ]
        override: false

    connectors:
      otlpjson:

    exporters:
      otlphttp/metrics:
        endpoint: http://127.0.0.1:9090/api/v1/otlp
      otlphttp/traces:
        endpoint: http://127.0.0.1:4418
      otlphttp/logs:
        endpoint: http://127.0.0.1:3100/otlp
      debug/metrics:
        verbosity: detailed
      debug/traces:
        verbosity: detailed
      debug/logs:
        verbosity: detailed
      nop:

    service:
      pipelines:
        traces:
          receivers: [ otlp ]
          processors: [ batch ]
          exporters: [ otlphttp/traces ]
        metrics:
          receivers: [ otlp, prometheus/collector ]
          processors: [ batch ]
          exporters: [ otlphttp/metrics ]
        logs/raw_otlpjson:
          receivers: [ filelog/otlp-json-logs ]
          # No need for processors before the otlpjson connector
          # Declare processors in the shared "logs" pipeline below
          processors: [ ]
          exporters: [ otlpjson ]
        logs/otlp:
          receivers: [ otlp, otlpjson ]
          processors: [ resourcedetection, batch ]
          exporters: [ otlphttp/logs ]
          # exporters: [ otlphttp/logs, debug/logs ]  # Uncomment this line to enable debug logging
```

## File: `examples/java/json-logging-otlp/k8s/dice.yaml`
```yaml
---
apiVersion: v1
kind: Service
metadata:
  name: dice
spec:
  selector:
    app: dice
  ports:
    - protocol: TCP
      port: 8080
      targetPort: 8080
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: dice
spec:
  replicas: 1
  selector:
    matchLabels:
      app: dice
  template:
    metadata:
      labels:
        app: dice
    spec:
      containers:
        - name: dice
          image: dice:1.1-SNAPSHOT
          imagePullPolicy: Never
          ports:
            - containerPort: 8080
          env:
            - name: OTEL_EXPORTER_OTLP_ENDPOINT
              value: "http://lgtm:4318"
            - name: OTEL_LOGS_EXPORTER
              value: "experimental-otlp/stdout"
            - name: OTEL_RESOURCE_ATTRIBUTES
              value: service.name=dice,service.namespace=shop,service.version=1.1,deployment.environment=staging
            - name: OTEL_INSTRUMENTATION_LOGBACK_APPENDER_EXPERIMENTAL_LOG_ATTRIBUTES
              value: "true"
            - name: OTEL_INSTRUMENTATION_LOGBACK_APPENDER_EXPERIMENTAL_CAPTURE_KEY_VALUE_PAIR_ATTRIBUTES
              value: "true"
            - name: OTEL_INSTRUMENTATION_LOGBACK_APPENDER_EXPERIMENTAL_CAPTURE_MDC_ATTRIBUTES
              value: "true"
            - name: SERVICE_NAME
              value: dice
```

## File: `examples/java/json-logging-otlp/k8s/lgtm.yaml`
```yaml
---
apiVersion: v1
kind: Service
metadata:
  name: lgtm
spec:
  selector:
    app: lgtm
  ports:
    - name: grafana
      protocol: TCP
      port: 3000
      targetPort: 3000
    - name: otel-grpc
      protocol: TCP
      port: 4317
      targetPort: 4317
    - name: otel-http
      protocol: TCP
      port: 4318
      targetPort: 4318
    - name: prometheus # needed for automated tests
      protocol: TCP
      port: 9090
      targetPort: 9090
    - name: loki # needed for automated tests
      protocol: TCP
      port: 3100
      targetPort: 3100
    - name: tempo # needed for automated tests
      protocol: TCP
      port: 3200
      targetPort: 3200
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: lgtm
spec:
  replicas: 1
  selector:
    matchLabels:
      app: lgtm
  template:
    metadata:
      labels:
        app: lgtm
    spec:
      containers:
        - name: lgtm
          image: grafana/otel-lgtm:latest
          ports:
            - containerPort: 3000
            - containerPort: 4317
            - containerPort: 4318
            - containerPort: 9090 # needed for automated tests
            - containerPort: 3100 # needed for automated tests
            - containerPort: 3200 # needed for automated tests
          readinessProbe:
            exec:
              command:
                - cat
                - /tmp/ready
          volumeMounts:
            - mountPath: /otel-lgtm/otelcol-config.yaml
              name: otel-collector-config
              subPath: otel-collector-config.yaml
              readOnly: true
            - mountPath: /var/log
              name: varlog
              readOnly: true
            - mountPath: /var/lib/docker/containers
              name: varlibdockercontainers
              readOnly: true
          env:
            - name: ENABLE_LOGS_OTELCOL
              value: "true"
      volumes:
        - name: otel-collector-config
          configMap:
            name: otel-collector-config
        - name: varlog
          hostPath:
            path: /var/log
        - name: varlibdockercontainers
          hostPath:
            path: /var/lib/docker/containers
```

## File: `examples/java/src/main/java/com/grafana/example/RollController.java`
```java
package com.grafana.example;

import java.util.Optional;
import java.util.Random;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

/** A simple controller that simulates rolling a dice. */
@RestController
public class RollController {

  private static final Logger logger = LoggerFactory.getLogger(RollController.class);
  private final Random random = new Random(0);
  private final float wait;

  public RollController(@Value("${grafana.roll.wait:200}") float wait) {
    logger.info("Wait time is set to {} ms", wait);
    this.wait = wait;
  }

  /** Simulates rolling a dice. */
  @GetMapping("/rolldice")
  public String index(@RequestParam("player") Optional<String> player) throws InterruptedException {
    veryLongCalculation();
    if (random.nextInt(10) < 3) {
      throw new RuntimeException("simulating an error");
    }
    int result = this.getRandomNumber(1, 6);
    if (player.isPresent()) {
      logger.info("{} is rolling the dice: {}", player.get(), result);
    } else {
      logger.info("Anonymous player is rolling the dice: {}", result);
    }
    return Integer.toString(result);
  }

  private void veryLongCalculation() throws InterruptedException {
    Thread.sleep((long) (Math.abs((random.nextGaussian() + 1.0) * wait)));
  }

  private int getRandomNumber(int min, int max) {
    return random.nextInt(min, max + 1);
  }
}
```

## File: `examples/java/src/main/java/com/grafana/example/SpringBootApp.java`
```java
package com.grafana.example;

import jakarta.servlet.http.HttpServletResponse;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

/** A simple Spring Boot application that redirects to {@link RollController}. */
@SpringBootApplication
@RestController
public class SpringBootApp {

  /** Redirect to {@link RollController}. */
  @GetMapping("/")
  public void redirect(HttpServletResponse httpServletResponse) {
    httpServletResponse.setHeader("Location", "/rolldice");
    httpServletResponse.setStatus(302);
  }

  /** Main method to start the Spring Boot application. */
  public static void main(String[] args) {
    SpringApplication.run(SpringBootApp.class, args);
  }
}
```

## File: `examples/java/testcontainer/README.md`
```markdown
# Using Testcontainers

The provided code demonstrates how to use **Testcontainers** with **Grafana's LGTM stack** to
test OpenTelemetry metrics in a Java application. Here's a step-by-step explanation:

1. **Set Up the Testcontainers Environment**:

- The `@Testcontainers` annotation enables the Testcontainers extension for JUnit 5.
- The `@Container` annotation is used to define a `LgtmStackContainer` that
  runs the Grafana LGTM stack in a Docker container.

2. **Configure OpenTelemetry**:

- In the `@BeforeEach` method, system properties are set to configure the OpenTelemetry
  exporter to send metrics to the LGTM stack running in the container.

3. **Run the Application**:

- The `OtelApp` class initializes OpenTelemetry and generates a custom metric (`sold_items`)
  with attributes (e.g., `tenant`), a span representing the block of code, and emits a log.

4. **Test Exporting Metrics and Traces**:

- The test method `testExportSignals` runs the application and queries the Prometheus, Loki, and
  Tempo endpoints in the LGTM stack to verify that the metric (`sold_items`), span, and log have
  been exported successfully.
- The `Awaitility` library is used to poll the endpoints until the telemetry is found or a timeout
  occurs.

5. **Debugging with Grafana**:

- The test outputs the Grafana URL (`lgtm.getGrafanaHttpUrl()`) to the console, allowing you to
  manually inspect the
  telemetry in the Grafana UI if needed.

## Example Usage

1. Start the test using `mvn test`.
2. Check the console output for the Grafana URL.
3. Open the Grafana UI, navigate to the Explore tab, and query the metrics, traces or logs.
4. The test will pass if the metric, log, and span are successfully exported and found in Prometheus,
   Loki, and Tempo.

This setup is useful for validating OpenTelemetry instrumentation and ensuring metrics are correctly
exported to a monitoring system.

## Alternative Approach

If you prefer declarative tests, you can use [OpenTelemetry Acceptance Tests (OATs)](https://github.com/grafana/oats),
where the test would look like this:

```yaml
docker-compose:
  files:
    - ./docker-compose.yaml
expected:
  metrics:
    - promql: 'uptime_seconds_total{}'
      value: '>= 0'
```

OATs provides support for traces, logs, profiles, and metrics.

```

## File: `examples/java/testcontainer/pom.xml`
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>com.grafana.example</groupId>
    <artifactId>testcontainer</artifactId>
    <version>1.0.0-SNAPSHOT</version>

    <name>Java Testcontainer Demo</name>

    <properties>
        <spring.version>3.4.4</spring.version>
        <maven.compiler.source>17</maven.compiler.source>
        <maven.compiler.target>17</maven.compiler.target>
    </properties>

    <dependencyManagement>
        <dependencies>
            <dependency>
                <groupId>io.opentelemetry</groupId>
                <artifactId>opentelemetry-bom-alpha</artifactId>
                <version>1.49.0-alpha</version>
                <type>pom</type>
                <scope>import</scope>
            </dependency>
            <dependency>
                <groupId>org.testcontainers</groupId>
                <artifactId>testcontainers-bom</artifactId>
                <version>2.0.4</version>
                <type>pom</type>
                <scope>import</scope>
            </dependency>
        </dependencies>
    </dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>io.opentelemetry</groupId>
            <artifactId>opentelemetry-api-incubator</artifactId>
        </dependency>
        <dependency>
            <groupId>io.opentelemetry</groupId>
            <artifactId>opentelemetry-exporter-otlp</artifactId>
        </dependency>
        <dependency>
            <groupId>io.opentelemetry</groupId>
            <artifactId>opentelemetry-sdk-extension-autoconfigure</artifactId>
        </dependency>

        <dependency>
            <groupId>org.junit.jupiter</groupId>
            <artifactId>junit-jupiter</artifactId>
            <version>6.0.3</version>
            <scope>test</scope>
        </dependency>
        <dependency>
            <groupId>org.testcontainers</groupId>
            <artifactId>junit-jupiter</artifactId>
            <scope>test</scope>
        </dependency>
        <dependency>
            <groupId>org.testcontainers</groupId>
            <artifactId>grafana</artifactId>
            <scope>test</scope>
        </dependency>
        <dependency>
            <groupId>org.awaitility</groupId>
            <artifactId>awaitility</artifactId>
            <version>4.3.0</version>
            <scope>test</scope>
        </dependency>
        <dependency>
            <groupId>org.assertj</groupId>
            <artifactId>assertj-core</artifactId>
            <version>3.27.7</version>
            <scope>test</scope>
        </dependency>
    </dependencies>

</project>
```

## File: `examples/java/testcontainer/src/main/java/com/grafana/example/OtelApp.java`
```java
package com.grafana.example;

import io.opentelemetry.api.common.AttributeKey;
import io.opentelemetry.api.common.Attributes;
import io.opentelemetry.api.incubator.trace.ExtendedTracer;
import io.opentelemetry.api.logs.Logger;
import io.opentelemetry.api.metrics.LongCounter;
import io.opentelemetry.sdk.autoconfigure.AutoConfiguredOpenTelemetrySdk;

public class OtelApp {

  private final ExtendedTracer tracer;
  private final LongCounter counter;
  private final Logger logger;

  public static void main(String[] args) {
    new OtelApp().run();
  }

  public OtelApp() {
    var openTelemetry = AutoConfiguredOpenTelemetrySdk.initialize().getOpenTelemetrySdk();
    var meter = openTelemetry.getMeter("my-app");
    tracer = (ExtendedTracer) openTelemetry.tracerBuilder("my-app").build();
    counter = meter.counterBuilder("sold_items").build();
    logger = openTelemetry.getSdkLoggerProvider().loggerBuilder("my-app").build();
  }

  public void run() {
    Attributes attributes = Attributes.of(AttributeKey.stringKey("tenant"), "tenant1");
    tracer
        .spanBuilder("sell_item")
        .setAllAttributes(attributes)
        .startAndRun(() -> counter.add(42, attributes));

    logger
        .logRecordBuilder()
        .setBody("Test log!")
        .setAttribute(AttributeKey.stringKey("job"), "test-job")
        .emit();
  }
}
```

## File: `examples/java/testcontainer/src/test/java/com/grafana/example/TestcontainerTest.java`
```java
package com.grafana.example;

import static org.awaitility.Awaitility.await;

import java.net.URI;
import java.net.URLEncoder;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.nio.charset.StandardCharsets;
import java.time.Duration;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.testcontainers.grafana.LgtmStackContainer;
import org.testcontainers.junit.jupiter.Container;
import org.testcontainers.junit.jupiter.Testcontainers;

@Testcontainers
public class TestcontainerTest {

  @Container private final LgtmStackContainer lgtm = new LgtmStackContainer("grafana/otel-lgtm");

  @BeforeEach
  void setUp() {
    System.setProperty("otel.exporter.otlp.endpoint", lgtm.getOtlpHttpUrl());
    System.setProperty("otel.exporter.otlp.protocol", "http/protobuf");
    System.setProperty("otel.resource.attributes", "service.name=otel-java-test");
    System.setProperty("otel.metric.export.interval", "1s");
    System.setProperty("otel.bsp.schedule.delay", "500ms");
  }

  @Test
  void testExportSignals() {
    // How to debug:
    // 1. Run the test with a really long timeout (update the awaitility argument)
    // 2. Go to the Grafana UI
    // 3. Open the Explore tab
    // 4. Select the Prometheus data source
    // 5. Find your metric by name or attribute (e.g. "tenant1")
    // 6. Click on the metric to see the details
    // 7. Copy the query and paste it into the test
    System.out.println("Grafana URL to debug telemetry: " + lgtm.getGrafanaHttpUrl());
    var app = new OtelApp();
    app.run();

    HttpClient client = HttpClient.newHttpClient();

    String prometheusQuery =
        "sold_items_total{job=\"otel-java-test\","
            + "service_name=\"otel-java-test\",tenant=\"tenant1\"}";

    var requestConfigs =
        new RequestConfig[] {
          new RequestConfig(
              lgtm.getPrometheusHttpUrl() + "/api/v1/query", prometheusQuery, "sold_items"),
          new RequestConfig(lgtm.getTempoUrl() + "/api/search", null, "otel-java-test"),
          new RequestConfig(
              lgtm.getLokiUrl() + "/loki/api/v1/query_range",
              "{service_name=\"otel-java-test\"}",
              "Test log!")
        };

    await()
        .atMost(Duration.ofSeconds(10))
        .untilAsserted(
            () -> {
              for (RequestConfig config : requestConfigs) {
                HttpResponse<String> response = executeRequest(client, config);
                assert response.statusCode() == 200
                    && response.body().contains(config.expectedContent);
              }
            });
  }

  private HttpResponse<String> executeRequest(HttpClient client, RequestConfig config)
      throws Exception {
    URI uri;
    if (config.queryValue != null) {
      uri =
          URI.create(
              String.format(
                  "%s?query=%s",
                  config.baseUrl, URLEncoder.encode(config.queryValue, StandardCharsets.UTF_8)));
    } else {
      uri = URI.create(config.baseUrl);
    }

    HttpRequest request = HttpRequest.newBuilder().uri(uri).build();
    return client.send(request, HttpResponse.BodyHandlers.ofString());
  }

  private record RequestConfig(String baseUrl, String queryValue, String expectedContent) {}
}
```

## File: `examples/nodejs/.gitignore`
```
node_modules
```

## File: `examples/nodejs/.prettierrc`
```
{
  "singleQuote": true,
  "semi": false,
  "trailingComma": "none"
}
```

## File: `examples/nodejs/Dockerfile`
```
# syntax=docker/dockerfile:1.22@sha256:4a43a54dd1fedceb30ba47e76cfcf2b47304f4161c0caeac2db1c61804ea3c91

FROM node:24.14.1-alpine@sha256:01743339035a5c3c11a373cd7c83aeab6ed1457b55da6a69e014a95ac4e4700b

ENV NODE_ENV production

WORKDIR /usr/src/app

RUN --mount=type=bind,source=package.json,target=package.json \
    --mount=type=bind,source=package-lock.json,target=package-lock.json \
    --mount=type=cache,target=/root/.npm \
    npm ci --omit=dev

USER node

COPY . .

EXPOSE 8084

CMD ["node", "--require", "./instrumentation.js", "app.js"]
```

## File: `examples/nodejs/app.js`
```javascript
const { trace, SpanStatusCode } = require('@opentelemetry/api')
const express = require('express')
const { rollTheDice } = require('./dice.js')
const { Logger } = require('./logger.js')

const tracer = trace.getTracer('dice-server', '0.1.0')

const logger = new Logger('dice-server')

const PORT = parseInt(process.env.PORT || '8084')
const app = express()

app.get('/rolldice', (req, res) => {
  return tracer.startActiveSpan('rollDice', (span) => {
    logger.log('Received request to roll dice')
    const rolls = req.query.rolls ? parseInt(req.query.rolls.toString()) : NaN
    if (isNaN(rolls)) {
      const errorMessage = "Request parameter 'rolls' is missing or not a number."
      span.setStatus({
        code: SpanStatusCode.ERROR,
        message: errorMessage
      })
      logger.error(errorMessage)
      res.status(400).send(errorMessage)
      span.end()
      return
    }
    const result = JSON.stringify(rollTheDice(rolls, 1, 6))
    span.end()
    res.send(result)
  })
})

app.listen(PORT, () => {
  console.log(`Listening for requests on http://127.0.0.1:${PORT}`)
})
```

## File: `examples/nodejs/dice.js`
```javascript
const { trace, metrics } = require('@opentelemetry/api')
const { Logger } = require('./logger')

const tracer = trace.getTracer('dice-lib')
const meter = metrics.getMeter('dice-lib')

const counter = meter.createCounter('dice-lib.rolls.counter')

const logger = new Logger('dice-lib')

function rollOnce(i, min, max) {
  return tracer.startActiveSpan(`rollOnce:${i}`, (span) => {
    counter.add(1)
    logger.log(`Rolling a single die between ${min} and ${max}`)
    const result = Math.floor(Math.random() * (max - min + 1) + min)

    // Add an attribute to the span
    span.setAttribute('dicelib.rolled', result.toString())

    span.end()
    return result
  })
}

function rollTheDice(rolls, min, max) {
  // Create a span. A span must be closed.
  return tracer.startActiveSpan(
    'rollTheDice',
    { attributes: { 'dicelib.rolls': rolls.toString() } },
    (parentSpan) => {
      logger.log(`Rolling ${rolls} dice(s) between ${min} and ${max}`)
      const result = []
      for (let i = 0; i < rolls; i++) {
        result.push(rollOnce(i, min, max))
      }
      // Be sure to end the span!
      parentSpan.end()
      return result
    }
  )
}

module.exports = { rollTheDice }
```

## File: `examples/nodejs/docker-compose.oats.yml`
```yaml
---
# OATS is an acceptance testing framework for OpenTelemetry
# https://github.com/grafana/oats/tree/main/yaml
version: '3.4'

services:
  nodejs:
    build:
      context: .
      dockerfile: Dockerfile
    environment:
      OTEL_SERVICE_NAME: 'dice-server'
      OTEL_SERVICE_VERSION: '0.1.0'
      OTEL_EXPORTER_OTLP_ENDPOINT: http://lgtm:4318
      OTEL_METRIC_EXPORT_INTERVAL: '5000' # so we don't have to wait 60s for metrics
    ports:
      - '8080:8084'
```

## File: `examples/nodejs/instrumentation.js`
```javascript
const { NodeSDK } = require('@opentelemetry/sdk-node')
const { getNodeAutoInstrumentations } = require('@opentelemetry/auto-instrumentations-node')
const { PeriodicExportingMetricReader } = require('@opentelemetry/sdk-metrics')
const { OTLPTraceExporter } = require('@opentelemetry/exporter-trace-otlp-proto')
const { OTLPMetricExporter } = require('@opentelemetry/exporter-metrics-otlp-proto')

const sdk = new NodeSDK({
  traceExporter: new OTLPTraceExporter(),
  metricReader: new PeriodicExportingMetricReader({
    exporter: new OTLPMetricExporter()
  }),
  instrumentations: [
    getNodeAutoInstrumentations({
      '@opentelemetry/instrumentation-http': {
        ignoreIncomingRequestHook: (request) => {
          if (request.url === '/favicon.ico') {
            return true
          }
          return false
        }
      }
    })
  ]
})

sdk.start()
```

## File: `examples/nodejs/logger.js`
```javascript
const { SeverityNumber } = require('@opentelemetry/api-logs')
const { LoggerProvider, BatchLogRecordProcessor } = require('@opentelemetry/sdk-logs')
const { OTLPLogExporter } = require('@opentelemetry/exporter-logs-otlp-proto')
const { resourceFromAttributes } = require('@opentelemetry/resources')
const { ATTR_SERVICE_NAME, ATTR_SERVICE_VERSION } = require('@opentelemetry/semantic-conventions')

class Logger {
  context

  constructor(context) {
    this.context = context

    // To start a logger, you first need to initialize the Logger provider.
    const loggerProvider = new LoggerProvider({
      resource: resourceFromAttributes({
        [ATTR_SERVICE_NAME]: process.env.OTEL_SERVICE_NAME,
        [ATTR_SERVICE_VERSION]: process.env.OTEL_SERVICE_VERSION
      }),
      processors: [
        // Add a processor to export log record
        new BatchLogRecordProcessor(new OTLPLogExporter())
      ]
    })
    this.logger = loggerProvider.getLogger('default')
  }

  log(message) {
    this.logger.emit({
      severityNumber: SeverityNumber.INFO,
      severityText: 'INFO',
      body: message,
      attributes: {
        context: this.context
      }
    })

    console.log(`[${this.context}] - ${message}`)
  }

  warn(message) {
    this.logger.emit({
      severityNumber: SeverityNumber.WARN,
      severityText: 'WARN',
      body: message,
      attributes: {
        context: this.context
      }
    })

    console.warn(`[${this.context}] - ${message}`)
  }

  error(message) {
    this.logger.emit({
      severityNumber: SeverityNumber.ERROR,
      severityText: 'ERROR',
      body: message,
      attributes: {
        context: this.context
      }
    })

    console.error(`[${this.context}] - ${message}`)
  }
}

module.exports = { Logger }
```

## File: `examples/nodejs/oats.yaml`
```yaml
# OATS is an acceptance testing framework for OpenTelemetry
# https://github.com/grafana/oats/tree/main/yaml
oats-schema-version: 2
docker-compose:
  files:
    - ./docker-compose.oats.yml
input:
  - path: /rolldice?rolls=5
expected:
  traces:
    - traceql: '{ span.http.route = "/rolldice" }'
      equals: 'GET /rolldice'
      attributes:
        otel.library.name: '@opentelemetry/instrumentation-http'
  metrics:
    - promql: 'dice_lib_rolls_counter_total{service_name="dice-server"}'
      value: '>= 0'
  logs:
    - logql: '{service_name="dice-server"} |~ `Received request to roll dice`'
      equals: 'Received request to roll dice'
```

## File: `examples/nodejs/package.json`
```json
{
  "name": "dice-server",
  "version": "0.1.0",
  "description": "Simple Express app that rolls a dice.",
  "main": "app.js",
  "scripts": {
    "start": "node --require ./instrumentation.js app.js",
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "repository": {
    "type": "git",
    "url": "git+https://github.com/grafana/docker-otel-lgtm.git"
  },
  "keywords": [
    "grafana",
    "opentelemetry",
    "lgtm"
  ],
  "author": "",
  "license": "Apache-2.0",
  "bugs": {
    "url": "https://github.com/grafana/docker-otel-lgtm/issues"
  },
  "homepage": "https://github.com/grafana/docker-otel-lgtm#readme",
  "dependencies": {
    "@opentelemetry/api": "^1.9.0",
    "@opentelemetry/api-logs": "0.214.0",
    "@opentelemetry/auto-instrumentations-node": "^0.72.0",
    "@opentelemetry/exporter-logs-otlp-proto": "0.214.0",
    "@opentelemetry/exporter-metrics-otlp-proto": "^0.214.0",
    "@opentelemetry/exporter-trace-otlp-proto": "^0.214.0",
    "@opentelemetry/resources": "^2.0.0",
    "@opentelemetry/sdk-logs": "0.214.0",
    "@opentelemetry/sdk-metrics": "^2.0.0",
    "@opentelemetry/sdk-node": "^0.214.0",
    "@opentelemetry/sdk-trace-node": "^2.0.0",
    "@opentelemetry/semantic-conventions": "^1.30.0",
    "express": "^5.0.0"
  }
}
```

## File: `examples/nodejs/run.sh`
```bash
#!/bin/bash

set -euo pipefail

export OTEL_METRIC_EXPORT_INTERVAL="5000" # so we don't have to wait 60s for metrics
export OTEL_SERVICE_NAME="dice-server"
export OTEL_SERVICE_VERSION="0.1.0"

npm install

npm start
```

## File: `examples/obi/README.md`
```markdown
# OBI (OpenTelemetry eBPF Instrumentation) Example

This example demonstrates [OBI](https://github.com/open-telemetry/opentelemetry-go-instrumentation)
(OpenTelemetry eBPF Instrumentation, formerly Grafana Beyla) automatically instrumenting
5 applications written in different languages — **without any code changes or OpenTelemetry SDKs**.

## What is OBI?

OBI uses Linux eBPF to hook into kernel-level events (network I/O, function calls) to
automatically generate OpenTelemetry traces and metrics for HTTP/gRPC services. Unlike
traditional instrumentation that requires SDK integration, agents, or code changes, OBI
works at the kernel level and can instrument any application regardless of language.

## How it works

<!-- editorconfig-checker-disable -->

```text
+--------------------------------------------------------------------+
|  lgtm container (privileged, pid: host)                            |
|                                                                    |
|  +-----------+  +------------+  +-------+  +------+  +----------+  |
|  | OBI (eBPF)|->| OTel       |->| Tempo |  | Loki |  |Prometheus|  |
|  |           |  | Collector  |  +-------+  +------+  +----------+  |
|  +-----+-----+  +------------+       ^                     ^       |
|        |              |               +---------------------+      |
|        | eBPF hooks   |                    Grafana :3000           |
+--------+--------------+--------------------------------------------+
         | observes     |
    +----+--------------+------------------------------------------+
    |              Host kernel (shared via pid: host)              |
    +--------+------+--------+---------+-----------+               |
    |  Java  |  Go  | Python | Node.js |  .NET     |               |
    |  :8080 |:8081 | :8082  |  :8084  |  :8083    |               |
    |        |      |        |         |           |               |
    |  (no OTel SDK, agent, or distro in any app)  |               |
    +--------+------+--------+---------+-----------+               |
    +--------------------------------------------------------------+
```

<!-- editorconfig-checker-enable -->

1. The `lgtm` container runs with `privileged: true` and `pid: "host"`, giving OBI access
   to the host kernel and all container processes.
2. OBI attaches eBPF probes to the kernel to observe HTTP traffic patterns.
3. It automatically generates traces and metrics and sends them to the OpenTelemetry Collector.
4. The Collector forwards data to Tempo (traces) and Prometheus (metrics).
5. Grafana provides a UI to explore all telemetry data.

## Prerequisites

- **Linux host** (eBPF is a Linux kernel feature)
- **Kernel 5.8+** (required for eBPF ring buffer support)
- **Docker** with support for `privileged` containers and `pid: "host"`
- Note: This example does **not** work on Docker Desktop for macOS/Windows due to eBPF
  limitations in the Linux VM.

## Quick start

```bash
docker compose up --build
```

Wait for all services to start (the traffic generator will begin sending requests
to all 5 apps automatically).

## What you'll see in Grafana

Open <http://127.0.0.1:3000> (no login required).

### Traces (Tempo)

1. Go to **Explore** → select **Tempo** data source
2. Use the **Search** tab to find traces
3. You should see HTTP traces for `/rolldice` from all 5 services

### Metrics (Prometheus)

1. Go to **Explore** → select **Prometheus** data source
2. Query HTTP metrics, e.g.:
   - `http_server_request_duration_seconds_bucket` — request duration histogram
   - `http_server_request_duration_seconds_count` — request count

## Applications

All 5 applications implement the same `/rolldice` endpoint returning a random number 1–6.
**None** of them include any OpenTelemetry instrumentation:

| Language | Port | Source                        | What's different from `../` version   |
|----------|------|-------------------------------|---------------------------------------|
| Java     | 8080 | Reuses `../java` source       | No OTel Java agent                    |
| Go       | 8081 | `./go/` (new minimal source)  | No `otelhttp`, no OTel SDK            |
| Python   | 8082 | Reuses `../python` source     | No `opentelemetry-distro`             |
| .NET     | 8083 | `./dotnet/` (new minimal)     | No OTel NuGet packages                |
| Node.js  | 8084 | `./nodejs/` (new minimal)     | No `@opentelemetry/*` packages        |

## Comparison: OBI vs traditional instrumentation

| Aspect                | Traditional (SDK/Agent)       | OBI (eBPF)                  |
|-----------------------|-------------------------------|-----------------------------|
| Code changes required | Yes (SDK) or agent config     | None                        |
| Language support      | Per-language SDK              | Language-agnostic           |
| Trace detail          | Full custom spans, attributes | HTTP/gRPC-level spans       |
| Metrics               | Custom + auto                 | HTTP request metrics        |
| Deployment            | Per-app configuration         | Single privileged container |
| Kernel requirement    | None                          | Linux 5.8+                  |
| Overhead              | In-process                    | Kernel-level (minimal)      |

## Configuration

OBI is configured via environment variables on the `lgtm` container:

- `ENABLE_OBI: "true"` — enables OBI inside the LGTM container
- `OTEL_EXPORTER_OTLP_ENDPOINT` — where OBI sends telemetry (defaults to local collector)

See the [OBI documentation](https://opentelemetry.io/docs/zero-code/obi/)
for additional configuration options like route decoration, service name mapping, and filtering.

## Limitations

- **Linux only** — eBPF is a Linux kernel feature; does not work on macOS/Windows hosts
- **Privileged mode required** — the container needs elevated permissions for eBPF
- **HTTP/gRPC only** — OBI instruments network protocols, not application-internal logic
- **No custom spans** — unlike SDK instrumentation, you cannot add custom spans or attributes
- **No logs** — OBI generates traces and metrics, not logs
```

## File: `examples/obi/docker-compose.oats.yml`
```yaml
---
# OATS is an acceptance testing framework for OpenTelemetry
# https://github.com/grafana/oats/tree/main/yaml
services:
  # Override the OATS-provided lgtm service to enable OBI
  lgtm:
    environment:
      ENABLE_OBI: "true"
      ENABLE_LOGS_OBI: "true"
    privileged: true
    pid: "host"

  generate-traffic:
    build:
      dockerfile: generate-traffic.Dockerfile
    depends_on:
      - java
      - python
      - dotnet
      - go
      - nodejs

  # Uninstrumented applications — no OTel SDK, agent, or distro.
  # OBI discovers and instruments them automatically via eBPF.

  dotnet:
    build:
      context: ./dotnet
    depends_on:
      - lgtm

  go:
    build:
      context: ./go
    depends_on:
      - lgtm

  java:
    build:
      context: ../java
      dockerfile: ../obi/java.Dockerfile
    depends_on:
      - lgtm

  nodejs:
    build:
      context: ./nodejs
    depends_on:
      - lgtm

  python:
    build:
      context: ../python
      dockerfile: ../obi/python.Dockerfile
    depends_on:
      - lgtm
```

## File: `examples/obi/docker-compose.yaml`
```yaml
services:
  lgtm:
    image: grafana/otel-lgtm
    environment:
      ENABLE_OBI: "true"
    privileged: true
    pid: "host"
    networks:
      - otel-net
    ports:
      - "3000:3000"
      - "4040:4040"
      - "4317:4317"
      - "4318:4318"
      - "9090:9090"

  generate-traffic:
    build:
      dockerfile: generate-traffic.Dockerfile
    networks:
      - otel-net
    depends_on:
      - java
      - python
      - dotnet
      - go
      - nodejs

  # Uninstrumented applications - sorted alphabetically by language.
  # None of these have any OpenTelemetry SDK, agent, or distro.
  # OBI (eBPF Instrumentation) running inside the lgtm container
  # automatically discovers and instruments them via eBPF.

  dotnet:
    build:
      context: ./dotnet
    ports:
      - "8083:8083"
    networks:
      - otel-net
    depends_on:
      - lgtm

  go:
    build:
      context: ./go
    ports:
      - "8081:8081"
    networks:
      - otel-net
    depends_on:
      - lgtm

  java:
    build:
      context: ../java
      dockerfile: ../obi/java.Dockerfile
    ports:
      - "8080:8080"
    networks:
      - otel-net
    depends_on:
      - lgtm

  nodejs:
    build:
      context: ./nodejs
    ports:
      - "8084:8084"
    networks:
      - otel-net
    depends_on:
      - lgtm

  python:
    build:
      context: ../python
      dockerfile: ../obi/python.Dockerfile
    ports:
      - "8082:8082"
    networks:
      - otel-net
    depends_on:
      - lgtm

networks:
  otel-net:
    driver: bridge
```

## File: `examples/obi/generate-traffic.Dockerfile`
```
FROM ubuntu:24.04

COPY generate-traffic.sh /usr/local/bin/

RUN apt-get update \
    && apt-get install -y --no-install-recommends curl \
    && rm -rf /var/lib/apt/lists/*

ENTRYPOINT ["/usr/local/bin/generate-traffic.sh"]
```

## File: `examples/obi/generate-traffic.sh`
```bash
#!/bin/bash

while true; do
	curl -s http://java:8080/rolldice || echo "error reaching java service"
	curl -s http://go:8081/rolldice || echo "error reaching go service"
	curl -s http://python:8082/rolldice || echo "error reaching python service"
	curl -s http://dotnet:8083/rolldice || echo "error reaching dotnet service"
	curl -s http://nodejs:8084/rolldice || echo "error reaching nodejs service"
	sleep 1
done
```

## File: `examples/obi/java.Dockerfile`
```
# Same Spring Boot app as ../java but WITHOUT the OpenTelemetry Java agent.
# OBI (eBPF Instrumentation) provides observability at the kernel level instead.

FROM eclipse-temurin:25.0.2_10-jdk@sha256:bee2e23ab444ed60daf8123e36478bc4a286ba7835bec6f9daf9eba1d50a86a2 AS builder

WORKDIR /usr/src/app/

COPY ./mvnw pom.xml ./
COPY ./.mvn ./.mvn
COPY ./src ./src
RUN --mount=type=cache,target=/root/.m2 ./mvnw install -DskipTests

FROM eclipse-temurin:25.0.2_10-jre@sha256:a9980cb3777d2b7b0d513800c3debc034c101530b96db4aadccb845f867fca9e

WORKDIR /usr/src/app/

COPY --from=builder /usr/src/app/target/rolldice.jar ./app.jar

EXPOSE 8080
ENTRYPOINT [ "java", "-jar", "./app.jar" ]
```

## File: `examples/obi/oats.yaml`
```yaml
---
# OATS is an acceptance testing framework for OpenTelemetry
# https://github.com/grafana/oats/tree/main/yaml
oats-schema-version: 2
docker-compose:
  files:
    - ./docker-compose.oats.yml
# No input: section — OATS only supports a single application port, but this
# test exercises 5 services on different ports. The generate-traffic sidecar
# sends requests to all services instead.
expected:
  traces:
    # Java (port 8080) - reuses ../java source, no OTel agent
    - traceql: '{ span.url.path = "/rolldice" && span.server.port = 8080 }'
      equals: "GET /rolldice"
    # Go (port 8081) - minimal source, no OTel SDK
    - traceql: '{ span.url.path = "/rolldice" && span.server.port = 8081 }'
      equals: "GET /rolldice"
    # Python (port 8082) - reuses ../python source, no opentelemetry-distro
    - traceql: '{ span.url.path = "/rolldice" && span.server.port = 8082 }'
      equals: "GET /rolldice"
    # .NET (port 8083) - minimal source, no OTel NuGet packages
    - traceql: '{ span.url.path = "/rolldice" && span.server.port = 8083 }'
      equals: "GET /rolldice"
    # Node.js (port 8084) - minimal source, no @opentelemetry/* packages
    - traceql: '{ span.url.path = "/rolldice" && span.server.port = 8084 }'
      equals: "GET /rolldice"
  metrics:
    - promql: 'http_server_request_duration_seconds_count{http_route="/rolldice"}'
      value: "> 0"
```

## File: `examples/obi/python.Dockerfile`
```
# Same Flask app as ../python but WITHOUT the OpenTelemetry Python distro.
# OBI (eBPF Instrumentation) provides observability at the kernel level instead.

# hadolint global ignore=DL3059
FROM python:alpine3.19

WORKDIR /app

COPY requirements.txt .

RUN apk add --no-cache build-base
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

EXPOSE 8082

CMD ["flask", "run", "--host", "0.0.0.0", "--port", "8082"]
```

## File: `examples/obi/dotnet/Dockerfile`
```
FROM --platform=$BUILDPLATFORM mcr.microsoft.com/dotnet/sdk:10.0 AS build
ARG TARGETARCH
ARG CONFIGURATION=Release

COPY . /source
WORKDIR /source

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

RUN --mount=type=cache,id=nuget,target=/root/.nuget/packages \
    dotnet publish "rolldice.csproj" --arch "${TARGETARCH}" --configuration "${CONFIGURATION}" --output /app /p:UseAppHost=false

FROM mcr.microsoft.com/dotnet/aspnet:10.0 AS final
WORKDIR /app
EXPOSE 8083

ENV ASPNETCORE_HTTP_PORTS=8083

COPY --from=build /app .
ENTRYPOINT ["dotnet", "rolldice.dll"]
```

## File: `examples/obi/dotnet/Program.cs`
```csharp
using System.Globalization;

var app = WebApplication.CreateBuilder(args).Build();

string HandleRollDice(string? player, ILogger<Program> logger)
{
    var result = Random.Shared.Next(1, 7);

    if (string.IsNullOrEmpty(player))
    {
        logger.LogInformation("Anonymous player is rolling the dice: {result}", result);
    }
    else
    {
        logger.LogInformation("{player} is rolling the dice: {result}", player, result);
    }

    return result.ToString(CultureInfo.InvariantCulture);
}

app.MapGet("/rolldice/{player?}", HandleRollDice);

app.Run();
```

## File: `examples/obi/dotnet/rolldice.csproj`
```
<Project Sdk="Microsoft.NET.Sdk.Web">

  <PropertyGroup>
    <TargetFramework>net10.0</TargetFramework>
    <Nullable>enable</Nullable>
    <ImplicitUsings>enable</ImplicitUsings>
  </PropertyGroup>

</Project>
```

## File: `examples/obi/go/Dockerfile`
```
FROM golang:1.26@sha256:595c7847cff97c9a9e76f015083c481d26078f961c9c8dca3923132f51fe12f1

WORKDIR /app

COPY go.mod ./

COPY *.go ./

# Build
RUN CGO_ENABLED=0 GOOS=linux go build -o /rolldice

EXPOSE 8081

# Run
CMD ["/rolldice"]
```

## File: `examples/obi/go/go.mod`
```
module github.com/grafana/docker-otel-lgtm/examples/obi/go

go 1.24.0
```

## File: `examples/obi/go/main.go`
```go
package main

import (
	"fmt"
	"log"
	"math/rand/v2"
	"net/http"
)

func main() {
	http.HandleFunc("/rolldice", func(w http.ResponseWriter, _ *http.Request) {
		result := rand.IntN(6) + 1 //nolint:gosec // dice roll, no crypto needed
		log.Printf("Anonymous player is rolling the dice: %d", result)
		fmt.Fprint(w, result)
	})

	log.Println("Starting server on :8081")
	log.Fatal(http.ListenAndServe(":8081", nil)) //nolint:gosec // simple demo server
}
```

## File: `examples/obi/nodejs/Dockerfile`
```
FROM node:24-alpine@sha256:01743339035a5c3c11a373cd7c83aeab6ed1457b55da6a69e014a95ac4e4700b

ENV NODE_ENV=production

WORKDIR /usr/src/app

COPY package*.json ./
RUN npm ci --omit=dev

COPY --chown=node:node app.js .

USER node

EXPOSE 8084

CMD ["node", "app.js"]
```

## File: `examples/obi/nodejs/app.js`
```javascript
const express = require("express");

const PORT = parseInt(process.env.PORT || "8084");
const app = express();

app.get("/rolldice", (req, res) => {
  const result = Math.floor(Math.random() * 6) + 1;
  console.log(`Anonymous player is rolling the dice: ${result}`);
  res.send(result.toString());
});

app.listen(PORT, () => {
  console.log(`Listening for requests on http://127.0.0.1:${PORT}`);
});
```

## File: `examples/obi/nodejs/package.json`
```json
{
  "name": "dice-server",
  "version": "0.1.0",
  "description": "Simple Express app that rolls a dice (no OpenTelemetry instrumentation).",
  "main": "app.js",
  "scripts": {
    "start": "node app.js"
  },
  "license": "Apache-2.0",
  "dependencies": {
    "express": "^5.0.0"
  }
}
```

## File: `examples/python/Dockerfile`
```
# hadolint global ignore=DL3059
FROM python:alpine3.19

WORKDIR /app

COPY requirements.txt .

# How to get the requirements.txt file?
# 1. Follow https://opentelemetry.io/docs/languages/python/getting-started/
# 2. Run `pip freeze > requirements.txt` in the same directory as your app.py file
RUN apk add --no-cache build-base
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# renovate: datasource=pypi depName=opentelemetry-distro
ENV OPENTELEMETRY_DISTRO_VERSION=0.61b0
RUN pip install --no-cache-dir "opentelemetry-distro[otlp]==$OPENTELEMETRY_DISTRO_VERSION"
RUN opentelemetry-bootstrap -a install

COPY app.py .

# Logging support is still in alpha, so we need to enable it explicitly
ENV OTEL_PYTHON_LOGGING_AUTO_INSTRUMENTATION_ENABLED=true
ENV OTEL_LOGS_EXPORTER=otlp

EXPOSE 8082

CMD ["opentelemetry-instrument", "flask", "run", "--host", "0.0.0.0", "--port", "8082"]
```

## File: `examples/python/app.py`
```python
"""Simple Flask app that rolls a dice."""

import logging
from random import randint

from flask import Flask, request

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@app.route("/rolldice")
def roll_dice():
    """Rolls a dice and returns the result."""
    player = request.args.get("player", default=None, type=str)
    result = str(roll())
    if player:
        logger.warning("%s is rolling the dice: %s", player, result)
    else:
        logger.warning("Anonymous player is rolling the dice: %s", result)
    return result


def roll():
    """Rolls a dice and returns the result."""
    return randint(1, 6)
```

## File: `examples/python/docker-compose.oats.yml`
```yaml
---
# OATS is an acceptance testing framework for OpenTelemetry
# https://github.com/grafana/oats/tree/main/yaml
version: "3.4"

services:
  python:
    build:
      context: .
      dockerfile: Dockerfile
    environment:
      OTEL_SERVICE_NAME: "rolldice"
      OTEL_EXPORTER_OTLP_ENDPOINT: http://lgtm:4317
      OTEL_METRIC_EXPORT_INTERVAL: "5000" # so we don't have to wait 60s for metrics
    ports:
      - "8080:8082"
```

## File: `examples/python/oats.yaml`
```yaml
# OATS is an acceptance testing framework for OpenTelemetry
# https://github.com/grafana/oats/tree/main/yaml
oats-schema-version: 2
docker-compose:
  files:
    - ./docker-compose.oats.yml
input:
  - path: /rolldice
expected:
  # this is checking that the health check is working
  # this is usually not needed - because we check the functionality of the app
  # but some cases are missing, e.g. that grafana is up and running
  # We also check that this exact log line is present in the logs, which some users rely on
  compose-logs:
    - "The OpenTelemetry collector and the Grafana LGTM stack are up and running. (created /tmp/ready)"
  traces:
    - traceql: '{ span.http.route = "/rolldice" }'
      equals: "GET /rolldice"
      attributes:
        otel.library.name: opentelemetry.instrumentation.flask
  metrics:
    - promql: 'http_server_active_requests{http_method="GET"}'
      value: ">= 0"
  logs:
    - logql: '{service_name="rolldice"} |~ `Anonymous player is rolling the dice.*`'
      regexp: "Anonymous player is rolling the dice"
```

## File: `examples/python/requirements.txt`
```
blinker==1.9.0
click==8.3.1
Flask==3.1.3
itsdangerous==2.2.0
Jinja2==3.1.6
MarkupSafe==3.0.3
Werkzeug==3.1.7
```

## File: `examples/python/run.sh`
```bash
#!/bin/bash

set -euo pipefail

export OTEL_METRIC_EXPORT_INTERVAL="5000" # so we don't have to wait 60s for metrics
export OTEL_RESOURCE_ATTRIBUTES="service.name=rolldice,service.instance.id=127.0.0.1:8082"

python3 -m venv venv
# shellcheck disable=SC1091
source ./venv/bin/activate

# How to get the requirements.txt file?
# 1. Follow https://opentelemetry.io/docs/languages/python/getting-started/
# 2. Run `pip freeze > requirements.txt` in the same directory as your app.py file
pip install --upgrade pip
pip install -r requirements.txt

# Step 1: Install the OpenTelemetry SDK
# renovate: datasource=pypi depName=opentelemetry-distro
opentelemetry_distro_version=0.61b0
pip install "opentelemetry-distro[otlp]==${opentelemetry_distro_version}"
opentelemetry-bootstrap -a install

# Step 2: Run the application
export OTEL_PYTHON_LOGGING_AUTO_INSTRUMENTATION_ENABLED=true
export OTEL_LOGS_EXPORTER=otlp
opentelemetry-instrument flask run -p 8082
```

## File: `k8s/lgtm.yaml`
```yaml
# this is intended for demo / testing purposes only, not for production usage
apiVersion: v1
kind: Service
metadata:
  name: lgtm
spec:
  selector:
    app: lgtm
  ports:
    - name: grafana
      protocol: TCP
      port: 3000
      targetPort: 3000
    - name: pyroscope
      protocol: TCP
      port: 4040
      targetPort: 4040
    - name: otel-grpc
      protocol: TCP
      port: 4317
      targetPort: 4317
    - name: otel-http
      protocol: TCP
      port: 4318
      targetPort: 4318
    - name: prometheus
      protocol: TCP
      port: 9090
      targetPort: 9090
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: lgtm
spec:
  replicas: 1
  selector:
    matchLabels:
      app: lgtm
  template:
    metadata:
      labels:
        app: lgtm
    spec:
      containers:
        - name: lgtm
          image: grafana/otel-lgtm:latest
          ports:
            - containerPort: 3000
            - containerPort: 4040
            - containerPort: 4317
            - containerPort: 4318
            - containerPort: 9090
          readinessProbe:
            exec:
              command:
                - cat
                - /tmp/ready
          # NOTE: By default OpenShift does not allow writing the root directory.
          # That's why the data dirs for grafana, prometheus and loki can not be
          # created and the pod never becomes ready.
          # See: https://github.com/grafana/docker-otel-lgtm/issues/132
          volumeMounts:
            - name: tempo-data
              mountPath: /data/tempo
            - name: grafana-data
              mountPath: /data/grafana
            - name: loki-data
              mountPath: /data/loki
            - name: loki-storage
              mountPath: /loki
            - name: p8s-storage
              mountPath: /data/prometheus
            - name: pyroscope-storage
              mountPath: /data/pyroscope
      volumes:
        - name: tempo-data
          emptyDir: {}
        - name: loki-data
          emptyDir: {}
        - name: grafana-data
          emptyDir: {}
        - name: loki-storage
          emptyDir: {}
        - name: p8s-storage
          emptyDir: {}
        - name: pyroscope-storage
          emptyDir: {}
```


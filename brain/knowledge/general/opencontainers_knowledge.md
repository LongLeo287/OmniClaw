---
id: opencontainers-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:29:16.450420
---

# KNOWLEDGE EXTRACT: opencontainers
> **Extracted on:** 2026-03-30 17:50:21
> **Source:** opencontainers

---

## File: `runtime-spec.md`
```markdown
# 📦 opencontainers/runtime-spec [🔖 PENDING/APPROVE]
🔗 https://github.com/opencontainers/runtime-spec
🌐 http://www.opencontainers.org

## Meta
- **Stars:** ⭐ 3579 | **Forks:** 🍴 607
- **Language:** Go | **License:** Apache-2.0
- **Last updated:** 2026-03-24
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
OCI Runtime Specification

## README (trích đầu)
```
# Open Container Initiative Runtime Specification

[![GitHub Actions status](https://github.com/opencontainers/runtime-spec/workflows/build/badge.svg)](https://github.com/opencontainers/runtime-spec/actions?query=workflow%3Abuild)

The [Open Container Initiative][oci] develops specifications for standards on Operating System process and application containers.

The specification can be found [here](spec.md).

## Table of Contents

Additional documentation about how this group operates:

- [Code of Conduct][code-of-conduct]
- [Style and Conventions](../../../core/security/QUARANTINE/vetted/repos/openclaw/apps/android/style.md)
- [Implementations](implementations.md)
- [Releases](../../../core/security/QUARANTINE/incoming/repos/alasql/RELEASES.md)
- [charter][charter]

## Use Cases

To provide context for users the following section gives example use cases for each part of the spec.

### Application Bundle Builders

Application bundle builders can create a [bundle](bundle.md) directory that includes all of the files required for launching an application as a container.
The bundle contains an OCI [configuration file](config.md) where the builder can specify host-independent details such as [which executable to launch](config.md#process) and host-specific settings such as [mount](config.md#mounts) locations, [hook](config.md#posix-platform-hooks) paths, Linux [namespaces](config-linux.md#namespaces) and [cgroups](config-linux.md#control-groups).
Because the configuration includes host-specific settings, application bundle directories copied between two hosts may require configuration adjustments.

### Hook Developers

[Hook](config.md#posix-platform-hooks) developers can extend the functionality of an OCI-compliant runtime by hooking into a container's lifecycle with an external application.
Example use cases include sophisticated network configuration, volume garbage collection, etc.

### Runtime Developers

Runtime developers can build runtime implementations that run OCI-compliant bundles and container configuration, containing low-level OS and host-specific details, on a particular platform.

## Contributing

Development happens on GitHub for the spec.
Issues are used for bugs and actionable items and longer discussions can happen on the [mailing list](#mailing-list).

The specification and code is licensed under the Apache 2.0 license found in the [LICENSE](./LICENSE) file.

### Discuss your design

The project welcomes submissions, but please let everyone know what you are working on.

Before undertaking a nontrivial change to this specification, send mail to the [mailing list](#mailing-list) to discuss what you plan to do.
This gives everyone a chance to validate the design, helps prevent duplication of effort, and ensures that the idea fits.
It also guarantees that the design is sound before code is written; a GitHub pull-request is not the place for high-level discussions.

Typos and grammatical errors can go straight to a pull-request.
When in doubt, start on the [mailing-list](#mailing-list).

### Meetings

Please see the [OCI org repository README](https://gith
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```


---
id: kubernetes-sigs-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:29:02.113103
---

# KNOWLEDGE EXTRACT: kubernetes-sigs
> **Extracted on:** 2026-03-30 17:38:56
> **Source:** kubernetes-sigs

---

## File: `agent-sandbox.md`
```markdown
# 📦 kubernetes-sigs/agent-sandbox [🔖 PENDING/APPROVE]
🔗 https://github.com/kubernetes-sigs/agent-sandbox
🌐 https://agent-sandbox.sigs.k8s.io

## Meta
- **Stars:** ⭐ 1543 | **Forks:** 🍴 167
- **Language:** Go | **License:** Apache-2.0
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
agent-sandbox enables easy management of isolated, stateful, singleton workloads, ideal for use cases like AI agent runtimes.

## README (trích đầu)
```
<div align="center">
  <img src="site/assets/icons/color_logo.svg" alt="Agent Sandbox logo" width="150" />

  <h1>Agent Sandbox</h1>
</div>


<p>
  <a href="https://github.com/kubernetes-sigs/agent-sandbox/releases"><img src="https://img.shields.io/github/v/release/kubernetes-sigs/agent-sandbox" alt="GitHub release"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/Apache-2-blue.svg" alt="Apache-2.0 license"></a>
</p>

[Website](https://agent-sandbox.sigs.k8s.io) · [Docs](https://agent-sandbox.sigs.k8s.io/docs/) · [DeepWiki](https://deepwiki.com/kubernetes-sigs/agent-sandbox) · [Getting Started](https://agent-sandbox.sigs.k8s.io/docs/getting_started/) · [Examples](examples/) · [Roadmap](roadmap.md)

**agent-sandbox enables easy management of isolated, stateful, singleton workloads, ideal for use cases like AI agent runtimes.**

This project is developing a `Sandbox` Custom Resource Definition (CRD) and controller for Kubernetes, under the umbrella of [SIG Apps](https://github.com/kubernetes/community/tree/master/sig-apps). The goal is to provide a declarative, standardized API for managing workloads that require the characteristics of a long-running, stateful, singleton container with a stable identity, much like a lightweight, single-container VM experience built on Kubernetes primitives.

## Overview

### Core: Sandbox

The `Sandbox` CRD is the core of agent-sandbox. It provides a declarative API for managing a single, stateful pod with a stable identity and persistent storage. This is useful for workloads that don't fit well into the stateless, replicated model of Deployments or the numbered, stable model of StatefulSets.

Key features of the `Sandbox` CRD include:

*   **Stable Identity:** Each Sandbox has a stable hostname and network identity.
*   **Persistent Storage:** Sandboxes can be configured with persistent storage that survives restarts.
*   **Lifecycle Management:** The Sandbox controller manages the lifecycle of the pod, including creation, scheduled deletion, pausing and resuming.

### Extensions

The `extensions` module provides additional CRDs and controllers that build on the core `Sandbox` API to provide more advanced features.

*   `SandboxTemplate`: Provides a way to define reusable templates for creating Sandboxes, making it easier to manage large numbers of similar Sandboxes.
*   `SandboxClaim`: Allows users to create Sandboxes from a template, abstracting away the details of the underlying Sandbox configuration.
*   `SandboxWarmPool`: Manages a pool of pre-warmed Sandbox Pods that can be quickly allocated to users, reducing the time it takes to get a new Sandbox up and running.

## Architecture

agent-sandbox follows the Kubernetes controller pattern. Users create a Sandbox custom resource, and the controller manages the underlying runtime resources.

### Architecture Diagram

```mermaid
flowchart TB

    User[User]

    Claim[SandboxClaim]
    Template[SandboxTemplate]
    Sandbox[Sandbox]

    ClaimContro
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `windows-gmsa.md`
```markdown
# 📦 kubernetes-sigs/windows-gmsa [🔖 PENDING/APPROVE]
🔗 https://github.com/kubernetes-sigs/windows-gmsa


## Meta
- **Stars:** ⭐ 34 | **Forks:** 🍴 61
- **Language:** Go | **License:** Apache-2.0
- **Last updated:** 2025-10-09
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
External components to support Windows GMSA in Kubernetes

## README (trích đầu)
```
![Build Status](https://github.com/kubernetes-sigs/windows-gmsa/actions/workflows/build.yaml/badge.svg)

# Kubernetes Windows GMSA

External components to support [Windows' GMSA](https://docs.microsoft.com/en-us/windows-server/security/group-managed-service-accounts/group-managed-service-accounts-overview) in Kubernetes.

## Community, discussion, contribution, and support

Learn how to engage with the Kubernetes community on the [community page](http://kubernetes.io/community/).

You can reach the maintainers of this project at:

- [Slack](http://slack.k8s.io/)
- [Mailing List](https://groups.google.com/forum/#!forum/kubernetes-dev)

### Code of conduct

Participation in the Kubernetes community is governed by the [Kubernetes Code of Conduct](../../../vault/archives/archive_legacy/AutoGPT/docs/content/code-of-conduct.md).

[owners]: https://git.k8s.io/community/contributors/guide/owners.md
[Creative Commons 4.0]: https://git.k8s.io/website/LICENSE

```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```


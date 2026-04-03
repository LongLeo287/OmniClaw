---
id: prometheus-operator-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:31:02.207967
---

# KNOWLEDGE EXTRACT: prometheus-operator
> **Extracted on:** 2026-03-30 17:51:10
> **Source:** prometheus-operator

---

## File: `prometheus-operator.md`
```markdown
# 📦 prometheus-operator/prometheus-operator [🔖 PENDING/APPROVE]
🔗 https://github.com/prometheus-operator/prometheus-operator
🌐 https://prometheus-operator.dev

## Meta
- **Stars:** ⭐ 9866 | **Forks:** 🍴 3846
- **Language:** Go | **License:** Apache-2.0
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Prometheus Operator creates/configures/manages Prometheus clusters atop Kubernetes

## README (trích đầu)
```
# Prometheus Operator

[![Build Status](https://github.com/prometheus-operator/prometheus-operator/actions/workflows/checks.yaml/badge.svg)](https://github.com/prometheus-operator/prometheus-operator/actions)
[![Go Report Card](https://goreportcard.com/badge/prometheus-operator/prometheus-operator "Go Report Card")](https://goreportcard.com/report/prometheus-operator/prometheus-operator)
[![Slack](https://img.shields.io/badge/join%20slack-%23prometheus--operator-brightgreen.svg)](https://kubernetes.slack.com)

## Overview

The Prometheus Operator provides [Kubernetes](https://kubernetes.io/) native deployment and management of
[Prometheus](https://prometheus.io/) and related monitoring components. The purpose of this project is to
simplify and automate the configuration of a Prometheus based monitoring stack for Kubernetes clusters.

The Prometheus operator includes, but is not limited to, the following features:

* **Kubernetes Custom Resources**: Use Kubernetes custom resources to deploy and manage Prometheus, Alertmanager,
  and related components.

* **Simplified Deployment Configuration**: Configure the fundamentals of Prometheus like versions, persistence,
  retention policies, and replicas from a native Kubernetes resource.

* **Prometheus Target Configuration**: Automatically generate monitoring target configurations based
  on familiar Kubernetes label queries; no need to learn a Prometheus specific configuration language.

For an introduction to the Prometheus Operator, see the [getting started](https://github.com/prometheus-operator/prometheus-operator/blob/main/Documentation/developer/getting-started.md) guide.

## Project Status

The operator in itself is considered to be production ready. Please refer to the Custom Resource Definition (CRD) versions for the status of each CRD:

* `monitoring.coreos.com/v1`: **stable** CRDs and API, changes are made in a backward-compatible way.
* `monitoring.coreos.com/v1beta1`: **unstable** CRDs and API, changes can happen but the team is focused on avoiding them. We encourage usage in production for users that accept the risk of breaking changes.
* `monitoring.coreos.com/v1alpha1`: **unstable** CRDs and API, changes can happen frequently, and we suggest avoiding its usage on mission-critical environments.

## Prometheus Operator vs. kube-prometheus vs. community Helm chart

### Prometheus Operator

The Prometheus Operator uses Kubernetes [custom resources](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/) to simplify the deployment and configuration of Prometheus, Alertmanager, and related monitoring components.

### kube-prometheus

[kube-prometheus](https://github.com/prometheus-operator/kube-prometheus) provides example configurations for a complete cluster monitoring
stack based on Prometheus and the Prometheus Operator. This includes deployment of multiple Prometheus and Alertmanager instances,
metrics exporters such as the node_exporter for gathering node
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```


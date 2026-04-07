---
id: sympozium
type: knowledge
owner: OA_Triage
---
# sympozium
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
  "dependencies": {
    "opencode-lmstudio": "^0.3.0"
  }
}

```

### File: README.md
```md
<p align="center">
  <img src="logo.png" alt="sympozium.ai logo" width="600px;">
</p>

<p align="center">

  <em>
  Every agent is an ephemeral Pod.<br>Every policy is a CRD. Every execution is a Job.<br>
  Orchestrate multi-agent workflows <b>and</b> let agents diagnose, scale, and remediate your infrastructure.<br>
  Multi-tenant. Horizontally scalable. Safe by design.</em><br><br>
  From the creator of <a href="https://github.com/k8sgpt-ai/k8sgpt">k8sgpt</a> and <a href="https://github.com/AlexsJones/llmfit">llmfit</a>
</p>

<p align="center">
  <b>
  This project is under active development. API's will change, things will be break. Be brave.
  <b />
</p>
<p align="center">
  <a href="https://github.com/sympozium-ai/sympozium/actions"><img src="https://github.com/sympozium-ai/sympozium/actions/workflows/build.yaml/badge.svg" alt="Build"></a>
  <a href="https://github.com/sympozium-ai/sympozium/releases/latest"><img src="https://img.shields.io/github/v/release/sympozium-ai/sympozium" alt="Release"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-Apache%202.0-blue" alt="License"></a>
</p>

<p align="center">
  <img src="demo.gif" alt="Sympozium TUI demo" width="800px;">
</p>

---

> **Full documentation:** [deploy.sympozium.ai/docs](https://deploy.sympozium.ai/docs/)

---

### Quick Install (macOS / Linux)

**Homebrew:**
```bash
brew tap sympozium-ai/sympozium
brew install sympozium
```

**Shell installer:**
```bash
curl -fsSL https://deploy.sympozium.ai/install.sh | sh
```

Then deploy to your cluster and activate your first agents:

```bash
sympozium install          # deploys CRDs, controllers, and built-in PersonaPacks
sympozium                  # launch the TUI — go to Personas tab, press Enter to onboard
sympozium serve            # open the web dashboard (port-forwards to the in-cluster UI)
```

### Advanced: Helm Chart

**Prerequisites:** [cert-manager](https://cert-manager.io/) (for webhook TLS):
```bash
kubectl apply -f https://github.com/cert-manager/cert-manager/releases/download/v1.17.1/cert-manager.yaml
```

Deploy the Sympozium control plane:
```bash
helm repo add sympozium https://deploy.sympozium.ai/charts
helm repo update
helm install sympozium sympozium/sympozium
```

See [`charts/sympozium/values.yaml`](charts/sympozium/values.yaml) for configuration options.

---

## Why Sympozium?

Sympozium serves **two powerful use cases** on one Kubernetes-native platform:

1. **Orchestrate fleets of AI agents** — customer support, code review, data pipelines, or any domain-specific workflow. Each agent gets its own pod, RBAC, and network policy with proper tenant isolation.
2. **Administer the cluster itself agentically** — point agents inward to diagnose failures, scale deployments, triage alerts, and remediate issues, all with Kubernetes-native isolation, RBAC, and audit trails.

### Key Features

| | |
|---|---|
| **PersonaPacks** | Helm-like bundles for AI agents — activate a pack and the controller stamps out a full agent team |
| **Skill Sidecars** | Every skill runs in its own sidecar with ephemeral least-privilege RBAC, garbage-collected on completion |
| **Multi-Channel** | Telegram, Slack, Discord, WhatsApp — each channel is a dedicated Deployment backed by NATS JetStream |
| **Persistent Memory** | SQLite + FTS5 on a PersistentVolume — memories survive across ephemeral pod runs |
| **Scheduled Heartbeats** | Cron-based recurring agent runs for health checks, alert triage, and resource right-sizing |
| **Agent Sandbox** | Kernel-level isolation via [kubernetes-sigs/agent-sandbox](https://deploy.sympozium.ai/docs/concepts/agent-sandbox/) — gVisor or Kata with warm pools for instant starts |
| **MCP Servers** | External tool providers via Model Context Protocol with auto-discovery and allow/deny filtering |
| **TUI & Web UI** | Terminal and browser dashboards, or skip the UI entirely with Helm and kubectl |
| **Any AI Provider** | OpenAI, Anthropic, Azure, Ollama, or any compatible endpoint — no vendor lock-in |

---

## Documentation

| Topic | Link |
|-------|------|
| Getting Started | [deploy.sympozium.ai/docs/getting-started](https://deploy.sympozium.ai/docs/getting-started/) |
| Architecture | [deploy.sympozium.ai/docs/architecture](https://deploy.sympozium.ai/docs/architecture/) |
| Custom Resources | [deploy.sympozium.ai/docs/concepts/custom-resources](https://deploy.sympozium.ai/docs/concepts/custom-resources/) |
| PersonaPacks | [deploy.sympozium.ai/docs/concepts/personapacks](https://deploy.sympozium.ai/docs/concepts/personapacks/) |
| Skills & Sidecars | [deploy.sympozium.ai/docs/concepts/skills](https://deploy.sympozium.ai/docs/concepts/skills/) |
| Persistent Memory | [deploy.sympozium.ai/docs/concepts/persistent-memory](https://deploy.sympozium.ai/docs/concepts/persistent-memory/) |
| Channels | [deploy.sympozium.ai/docs/concepts/channels](https://deploy.sympozium.ai/docs/concepts/channels/) |
| Agent Sandboxing | [deploy.sympozium.ai/docs/concepts/agent-sandbox](https://deploy.sympozium.ai/docs/concepts/agent-sandbox/) |
| Security | [deploy.sympozium.ai/docs/concepts/security](https://deploy.sympozium.ai/docs/concepts/security/) |
| CLI & TUI Reference | [deploy.sympozium.ai/docs/reference/cli](https://deploy.sympozium.ai/docs/reference/cli/) |
| Helm Chart | [deploy.sympozium.ai/docs/reference/helm](https://deploy.sympozium.ai/docs/reference/helm/) |
| Ollama & Local Inference | [deploy.sympozium.ai/docs/guides/ollama](https://deploy.sympozium.ai/docs/guides/ollama/) |
| Writing Skills | [deploy.sympozium.ai/docs/guides/writing-skills](https://deploy.sympozium.ai/docs/guides/writing-skills/) |
| Writing Tools | [deploy.sympozium.ai/docs/guides/writing-tools](https://deploy.sympozium.ai/docs/guides/writing-tools/) |
| LM Studio & Local Inference | [deploy.sympozium.ai/docs/guides/lm-studio](https://deploy.sympozium.ai/docs/guides/lm-studio/) |
| Writing PersonaPacks | [deploy.sympozium.ai/docs/guides/writing-personapacks](https://deploy.sympozium.ai/docs/guides/writing-personapacks/) |
| Your First AgentRun | [deploy.sympozium.ai/docs/guides/first-agentrun](https://deploy.sympozium.ai/docs/guides/first-agentrun/) |

---

## Development

```bash
make test        # run tests
make lint        # run linter
make manifests   # generate CRD manifests
make run         # run controller locally (needs kubeconfig)
```

## License

Apache License 2.0

```

### File: examples\README.md
```md
# Examples

This directory contains standalone YAML manifests for Sympozium CRDs. Each file includes instructions at the top.

## Quick Start (Copy-Paste)

```bash
# 1. Create OpenAI secret
kubectl create secret generic my-openai-key --from-literal=key=sk-...

# 2. Apply quickstart example
kubectl apply -f yaml/quickstart.yaml

# 3. Watch it run
kubectl get agentrun quickstart-run -w
```

## Directory Structure

```
examples/
├── README.md              # This file (quick reference)
├── SETUP.md               # Detailed setup guide (secrets, prerequisites)
└── yaml/                  # YAML manifests (copy-paste ready)
    ├── quickstart.yaml               # All-in-one quick start
    ├── personapack-example.yaml      # Team of agents
    ├── sympoziuminstance-example.yaml  # Single agent
    ├── agentrun-example.yaml         # One-off task
    ├── sympoziumschedule-example.yaml  # Recurring task
    ├── personapack-activate.yaml     # Activation examples
    ├── agentrun-trigger.yaml         # Multiple trigger methods
    ├── skillpack-example.yaml        # Custom skills
    └── sympoziumpolicy-example.yaml  # Tool access rules
```

## Examples Reference

| Resource | Purpose | When to Use |
|----------|---------|-------------|
| **PersonaPack** | Bundle multiple personas with skills & schedules | Setting up teams of agents |
| **SympoziumInstance** | Single agent with channels & auth | Custom single-agent setups |
| **AgentRun** | One-off task execution | Ad-hoc requests, testing |
| **SympoziumSchedule** | Recurring heartbeat/cron tasks | Monitoring, periodic checks |
| **SkillPack** | Custom skill definitions | Extend agent capabilities |
| **SympoziumPolicy** | Tool access control rules | Security, compliance |

## Common Workflows

### Deploy a Team of Agents

```bash
kubectl apply -f yaml/personapack-example.yaml
sympozium  # Select Personas tab, press Enter on pack name
```

### Run a One-Off Task

```bash
kubectl apply -f yaml/agentrun-example.yaml
```

### Set Up Monitoring

```bash
kubectl apply -f yaml/sympoziuminstance-example.yaml
kubectl apply -f yaml/sympoziumschedule-example.yaml
```

## See Also

- [Setup Guide](./SETUP.md) - Detailed prerequisites and secrets setup
- [Getting Started Guide](../docs/getting-started.md)
- [Sample CRs in config/samples/](../config/samples/)

```

### File: FETCHED_sympozium_033816\package.json
```json
{
  "dependencies": {
    "opencode-lmstudio": "^0.3.0"
  }
}

```

### File: FETCHED_sympozium_033816\README.md
```md
<p align="center">
  <img src="logo.png" alt="sympozium.ai logo" width="600px;">
</p>

<p align="center">

  <em>
  Every agent is an ephemeral Pod.<br>Every policy is a CRD. Every execution is a Job.<br>
  Orchestrate multi-agent workflows <b>and</b> let agents diagnose, scale, and remediate your infrastructure.<br>
  Multi-tenant. Horizontally scalable. Safe by design.</em><br><br>
  From the creator of <a href="https://github.com/k8sgpt-ai/k8sgpt">k8sgpt</a> and <a href="https://github.com/AlexsJones/llmfit">llmfit</a>
</p>

<p align="center">
  <b>
  This project is under active development. API's will change, things will be break. Be brave.
  <b />
</p>
<p align="center">
  <a href="https://github.com/sympozium-ai/sympozium/actions"><img src="https://github.com/sympozium-ai/sympozium/actions/workflows/build.yaml/badge.svg" alt="Build"></a>
  <a href="https://github.com/sympozium-ai/sympozium/releases/latest"><img src="https://img.shields.io/github/v/release/sympozium-ai/sympozium" alt="Release"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-Apache%202.0-blue" alt="License"></a>
</p>

<p align="center">
  <img src="demo.gif" alt="Sympozium TUI demo" width="800px;">
</p>

---

> **Full documentation:** [deploy.sympozium.ai/docs](https://deploy.sympozium.ai/docs/)

---

### Quick Install (macOS / Linux)

**Homebrew:**
```bash
brew tap sympozium-ai/sympozium
brew install sympozium
```

**Shell installer:**
```bash
curl -fsSL https://deploy.sympozium.ai/install.sh | sh
```

Then deploy to your cluster and activate your first agents:

```bash
sympozium install          # deploys CRDs, controllers, and built-in PersonaPacks
sympozium                  # launch the TUI — go to Personas tab, press Enter to onboard
sympozium serve            # open the web dashboard (port-forwards to the in-cluster UI)
```

### Advanced: Helm Chart

**Prerequisites:** [cert-manager](https://cert-manager.io/) (for webhook TLS):
```bash
kubectl apply -f https://github.com/cert-manager/cert-manager/releases/download/v1.17.1/cert-manager.yaml
```

Deploy the Sympozium control plane:
```bash
helm repo add sympozium https://deploy.sympozium.ai/charts
helm repo update
helm install sympozium sympozium/sympozium
```

See [`charts/sympozium/values.yaml`](charts/sympozium/values.yaml) for configuration options.

---

## Why Sympozium?

Sympozium serves **two powerful use cases** on one Kubernetes-native platform:

1. **Orchestrate fleets of AI agents** — customer support, code review, data pipelines, or any domain-specific workflow. Each agent gets its own pod, RBAC, and network policy with proper tenant isolation.
2. **Administer the cluster itself agentically** — point agents inward to diagnose failures, scale deployments, triage alerts, and remediate issues, all with Kubernetes-native isolation, RBAC, and audit trails.

### Key Features

| | |
|---|---|
| **PersonaPacks** | Helm-like bundles for AI agents — activate a pack and the controller stamps out a full agent team |
| **Skill Sidecars** | Every skill runs in its own sidecar with ephemeral least-privilege RBAC, garbage-collected on completion |
| **Multi-Channel** | Telegram, Slack, Discord, WhatsApp — each channel is a dedicated Deployment backed by NATS JetStream |
| **Persistent Memory** | SQLite + FTS5 on a PersistentVolume — memories survive across ephemeral pod runs |
| **Scheduled Heartbeats** | Cron-based recurring agent runs for health checks, alert triage, and resource right-sizing |
| **Agent Sandbox** | Kernel-level isolation via [kubernetes-sigs/agent-sandbox](https://deploy.sympozium.ai/docs/concepts/agent-sandbox/) — gVisor or Kata with warm pools for instant starts |
| **MCP Servers** | External tool providers via Model Context Protocol with auto-discovery and allow/deny filtering |
| **TUI & Web UI** | Terminal and browser dashboards, or skip the UI entirely with Helm and kubectl |
| **Any AI Provider** | OpenAI, Anthropic, Azure, Ollama, or any compatible endpoint — no vendor lock-in |

---

## Documentation

| Topic | Link |
|-------|------|
| Getting Started | [deploy.sympozium.ai/docs/getting-started](https://deploy.sympozium.ai/docs/getting-started/) |
| Architecture | [deploy.sympozium.ai/docs/architecture](https://deploy.sympozium.ai/docs/architecture/) |
| Custom Resources | [deploy.sympozium.ai/docs/concepts/custom-resources](https://deploy.sympozium.ai/docs/concepts/custom-resources/) |
| PersonaPacks | [deploy.sympozium.ai/docs/concepts/personapacks](https://deploy.sympozium.ai/docs/concepts/personapacks/) |
| Skills & Sidecars | [deploy.sympozium.ai/docs/concepts/skills](https://deploy.sympozium.ai/docs/concepts/skills/) |
| Persistent Memory | [deploy.sympozium.ai/docs/concepts/persistent-memory](https://deploy.sympozium.ai/docs/concepts/persistent-memory/) |
| Channels | [deploy.sympozium.ai/docs/concepts/channels](https://deploy.sympozium.ai/docs/concepts/channels/) |
| Agent Sandboxing | [deploy.sympozium.ai/docs/concepts/agent-sandbox](https://deploy.sympozium.ai/docs/concepts/agent-sandbox/) |
| Security | [deploy.sympozium.ai/docs/concepts/security](https://deploy.sympozium.ai/docs/concepts/security/) |
| CLI & TUI Reference | [deploy.sympozium.ai/docs/reference/cli](https://deploy.sympozium.ai/docs/reference/cli/) |
| Helm Chart | [deploy.sympozium.ai/docs/reference/helm](https://deploy.sympozium.ai/docs/reference/helm/) |
| Ollama & Local Inference | [deploy.sympozium.ai/docs/guides/ollama](https://deploy.sympozium.ai/docs/guides/ollama/) |
| Writing Skills | [deploy.sympozium.ai/docs/guides/writing-skills](https://deploy.sympozium.ai/docs/guides/writing-skills/) |
| Writing Tools | [deploy.sympozium.ai/docs/guides/writing-tools](https://deploy.sympozium.ai/docs/guides/writing-tools/) |
| LM Studio & Local Inference | [deploy.sympozium.ai/docs/guides/lm-studio](https://deploy.sympozium.ai/docs/guides/lm-studio/) |
| Writing PersonaPacks | [deploy.sympozium.ai/docs/guides/writing-personapacks](https://deploy.sympozium.ai/docs/guides/writing-personapacks/) |
| Your First AgentRun | [deploy.sympozium.ai/docs/guides/first-agentrun](https://deploy.sympozium.ai/docs/guides/first-agentrun/) |

---

## Development

```bash
make test        # run tests
make lint        # run linter
make manifests   # generate CRD manifests
make run         # run controller locally (needs kubeconfig)
```

## License

Apache License 2.0

```

### File: web\package.json
```json
{
  "name": "sympozium-web",
  "private": true,
  "version": "0.1.0",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "tsc -b && vite build",
    "preview": "vite preview"
  },
  "dependencies": {
    "@radix-ui/react-dialog": "^1.1.4",
    "@radix-ui/react-dropdown-menu": "^2.1.4",
    "@radix-ui/react-label": "^2.1.1",
    "@radix-ui/react-scroll-area": "^1.2.2",
    "@radix-ui/react-select": "^2.1.4",
    "@radix-ui/react-separator": "^1.1.1",
    "@radix-ui/react-slot": "^1.1.1",
    "@radix-ui/react-tabs": "^1.1.2",
    "@tailwindcss/typography": "^0.5.19",
    "@tanstack/react-query": "^5.62.0",
    "class-variance-authority": "^0.7.1",
    "clsx": "^2.1.1",
    "date-fns": "^4.1.0",
    "lucide-react": "^0.468.0",
    "react": "^19.0.0",
    "react-dom": "^19.0.0",
    "react-grid-layout": "^2.2.2",
    "react-markdown": "^10.1.0",
    "react-router-dom": "^7.1.0",
    "remark-gfm": "^4.0.1",
    "sonner": "^1.7.1",
    "tailwind-merge": "^2.6.0"
  },
  "devDependencies": {
    "@types/node": "^25.3.2",
    "@types/react": "^19.0.0",
    "@types/react-dom": "^19.0.0",
    "@types/react-grid-layout": "^1.3.6",
    "@vitejs/plugin-react": "^4.3.4",
    "autoprefixer": "^10.4.20",
    "postcss": "^8.4.49",
    "tailwindcss": "^3.4.17",
    "typescript": "^5.7.2",
    "vite": "^6.4.1"
  }
}

```

### File: FETCHED_sympozium_033816\examples\README.md
```md
# Examples

This directory contains standalone YAML manifests for Sympozium CRDs. Each file includes instructions at the top.

## Quick Start (Copy-Paste)

```bash
# 1. Create OpenAI secret
kubectl create secret generic my-openai-key --from-literal=key=sk-...

# 2. Apply quickstart example
kubectl apply -f yaml/quickstart.yaml

# 3. Watch it run
kubectl get agentrun quickstart-run -w
```

## Directory Structure

```
examples/
├── README.md              # This file (quick reference)
├── SETUP.md               # Detailed setup guide (secrets, prerequisites)
└── yaml/                  # YAML manifests (copy-paste ready)
    ├── quickstart.yaml               # All-in-one quick start
    ├── personapack-example.yaml      # Team of agents
    ├── sympoziuminstance-example.yaml  # Single agent
    ├── agentrun-example.yaml         # One-off task
    ├── sympoziumschedule-example.yaml  # Recurring task
    ├── personapack-activate.yaml     # Activation examples
    ├── agentrun-trigger.yaml         # Multiple trigger methods
    ├── skillpack-example.yaml        # Custom skills
    └── sympoziumpolicy-example.yaml  # Tool access rules
```

## Examples Reference

| Resource | Purpose | When to Use |
|----------|---------|-------------|
| **PersonaPack** | Bundle multiple personas with skills & schedules | Setting up teams of agents |
| **SympoziumInstance** | Single agent with channels & auth | Custom single-agent setups |
| **AgentRun** | One-off task execution | Ad-hoc requests, testing |
| **SympoziumSchedule** | Recurring heartbeat/cron tasks | Monitoring, periodic checks |
| **SkillPack** | Custom skill definitions | Extend agent capabilities |
| **SympoziumPolicy** | Tool access control rules | Security, compliance |

## Common Workflows

### Deploy a Team of Agents

```bash
kubectl apply -f yaml/personapack-example.yaml
sympozium  # Select Personas tab, press Enter on pack name
```

### Run a One-Off Task

```bash
kubectl apply -f yaml/agentrun-example.yaml
```

### Set Up Monitoring

```bash
kubectl apply -f yaml/sympoziuminstance-example.yaml
kubectl apply -f yaml/sympoziumschedule-example.yaml
```

## See Also

- [Setup Guide](./SETUP.md) - Detailed prerequisites and secrets setup
- [Getting Started Guide](../docs/getting-started.md)
- [Sample CRs in config/samples/](../config/samples/)

```

### File: FETCHED_sympozium_033816\web\package.json
```json
{
  "name": "sympozium-web",
  "private": true,
  "version": "0.1.0",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "tsc -b && vite build",
    "preview": "vite preview"
  },
  "dependencies": {
    "@radix-ui/react-dialog": "^1.1.4",
    "@radix-ui/react-dropdown-menu": "^2.1.4",
    "@radix-ui/react-label": "^2.1.1",
    "@radix-ui/react-scroll-area": "^1.2.2",
    "@radix-ui/react-select": "^2.1.4",
    "@radix-ui/react-separator": "^1.1.1",
    "@radix-ui/react-slot": "^1.1.1",
    "@radix-ui/react-tabs": "^1.1.2",
    "@tailwindcss/typography": "^0.5.19",
    "@tanstack/react-query": "^5.62.0",
    "class-variance-authority": "^0.7.1",
    "clsx": "^2.1.1",
    "date-fns": "^4.1.0",
    "lucide-react": "^0.468.0",
    "react": "^19.0.0",
    "react-dom": "^19.0.0",
    "react-grid-layout": "^2.2.2",
    "react-markdown": "^10.1.0",
    "react-router-dom": "^7.1.0",
    "remark-gfm": "^4.0.1",
    "sonner": "^1.7.1",
    "tailwind-merge": "^2.6.0"
  },
  "devDependencies": {
    "@types/node": "^25.3.2",
    "@types/react": "^19.0.0",
    "@types/react-dom": "^19.0.0",
    "@types/react-grid-layout": "^1.3.6",
    "@vitejs/plugin-react": "^4.3.4",
    "autoprefixer": "^10.4.20",
    "postcss": "^8.4.49",
    "tailwindcss": "^3.4.17",
    "typescript": "^5.7.2",
    "vite": "^6.4.1"
  }
}

```

### File: .release-please-manifest.json
```json
{
  ".": "0.8.9"
}

```

### File: AGENTS.md
```md
# AGENTS.md — Contributor Guide for AI Agents

This file helps AI coding agents (Copilot, Cursor, Cline, etc.) understand the Sympozium project structure and development workflow.

---

## Project Overview

Sympozium is a **Kubernetes-native agent orchestration platform** written in Go. Every AI agent runs as an ephemeral Kubernetes pod (Job), with policy enforcement via CRDs, admission webhooks, and RBAC. Communication flows through NATS JetStream and a filesystem-based IPC bridge.

- **Language:** Go 1.25+
- **Module:** `github.com/sympozium-ai/sympozium`
- **K8s API version:** `sympozium.ai/v1alpha1`

---

## Repository Layout

```
api/v1alpha1/           # CRD type definitions (SympoziumInstance, AgentRun, SympoziumPolicy, SkillPack, SympoziumSchedule, PersonaPack)
cmd/
  agent-runner/         # Agent container — LLM loop + tool execution
  apiserver/            # HTTP + WebSocket API server
  controller/           # Controller manager (all reconcilers + routers)
  ipc-bridge/           # IPC bridge sidecar (fsnotify → NATS)
  web-proxy/            # Web proxy (OpenAI-compat API + MCP gateway)
  node-probe/           # Node probe DaemonSet (discovers inference providers on nodes)
  sympozium/             # CLI + TUI (Bubble Tea)
  webhook/              # Admission webhook server
channels/
  telegram/             # Channel pod — Telegram bot
  slack/                # Channel pod — Slack (Socket Mode + Events API)
  discord/              # Channel pod — Discord bot
  whatsapp/             # Channel pod — WhatsApp
config/
  crd/bases/            # Generated CRD YAML manifests
  manager/              # Controller manager deployment
  personas/             # Built-in PersonaPack YAML definitions
  rbac/                 # RBAC roles
  samples/              # Sample CR YAML files
  skills/               # Built-in SkillPack YAML definitions
  policies/             # Built-in SympoziumPolicy presets
  webhook/              # Webhook configuration
images/                 # Dockerfiles for all components
internal/
  apiserver/            # API server implementation
  channel/              # Channel types
  controller/           # Reconcilers (AgentRun, SympoziumInstance, SympoziumPolicy, SympoziumSchedule, SkillPack, PersonaPack) + routers (Channel, Schedule)
  eventbus/             # NATS JetStream client + topic constants
  ipc/                  # IPC bridge (fsnotify watcher, protocol, file handlers)
  orchestrator/         # Pod builder + spawner for agent Jobs
  session/              # Session store
  webhook/              # Policy enforcer
  webproxy/             # Web proxy handlers (OpenAI, MCP, rate limiting)
migrations/             # PostgreSQL schema migrations
test/integration/       # Integration test scripts (shell)
docs/                   # Design & contributor documentation
```

---

## Key CRDs

| CRD | Purpose |
|-----|---------|
| `SympoziumInstance` | An agent identity — provider config, model, enabled skills, channel bindings |
| `AgentRun` | A single agent invocation — task, result, phase lifecycle |
| `SympoziumPolicy` | Policy rules enforced by the admission webhook |
| `SkillPack` | Bundled skills (Markdown instructions) + optional sidecar container + RBAC |
| `SympoziumSchedule` | Cron-based recurring AgentRun creation (heartbeat, scheduled, sweep) |
| `PersonaPack` | Pre-configured agent bundles — stamps out Instances, Schedules, and memory automatically |

Type definitions live in `api/v1alpha1/`. After modifying types, regenerate with:

```bash
make generate    # deepcopy + CRD manifests
make manifests   # CRD YAML only
```

---

## Development Environment Setup

### Prerequisites

- Go 1.25+
- Docker
- [Kind](https://kind.sigs.k8s.io/) (Kubernetes in Docker)
- kubectl
- An LLM API key (e.g. `OPENAI_API_KEY`)

### Create a Kind Cluster & Install Sympozium

```bash
# Create cluster
kind create cluster --name kind

# Install CRDs
make install

# Build all images
make docker-build TAG=v0.1.0

# Load images into Kind (all components)
for img in controller apiserver ipc-bridge webhook agent-runner web-proxy \
           channel-telegram channel-slack channel-discord channel-whatsapp \
           skill-k8s-ops skill-sre-observability skill-llmfit; do
  kind load docker-image ghcr.io/sympozium-ai/sympozium/$img:v0.1.0 --name kind
done

# Deploy the control plane
kubectl apply -k config/
```

### Build & Test Cycle

After code changes:

```bash
# Build everything
make build

# Run unit tests
make test

# Build specific image + reload into Kind
make docker-build-agent-runner TAG=v0.1.0
kind load docker-image ghcr.io/sympozium-ai/sympozium/agent-runner:v0.1.0 --name kind

# Restart the controller to pick up new images
kubectl rollout restart deployment sympozium-controller-manager -n sympozium-system
```

### Common Build Targets

```bash
make build              # Build all binaries
make test               # Run unit tests with race detector
make test-short         # Run short tests only
make test-integration   # Run all integration tests (requires Kind + API key)
make vet                # go vet
make fmt                # gofmt
make tidy               # go mod tidy
make docker-build       # Build all Docker images
make docker-build-<name> TAG=v0.1.0   # Build a specific image
make generate           # Regenerate deepcopy + CRD manifests
make manifests          # Regenerate CRD YAML only
make clean              # Remove build artifacts
```

---

## Integration Tests

Integration tests live in `test/integration/` and run against a real Kind cluster with a real LLM.

### Running Tests

```bash
# All integration tests
make test-integration

# Single test
./test/integration/test-write-file.sh

# Override model or timeout
TEST_MODEL=gpt-5.2 TEST_TIMEOUT=180 ./test/integration/test-write-file.sh
```

### Existing Tests

| Test | What it validates |
|------|-------------------|
| `test-write-file.sh` | `write_file` tool — agent writes a file, script verifies content |
| `test-anthropic-write-file.sh` | `write_file` tool using Anthropic provider — validates provider parity |
| `test-k8s-ops-nodes.sh` | `k8s-ops` skill — agent runs kubectl via sidecar |
| `test-llmfit-cluster-fit.sh` | `llmfit` skill — agent runs node-level llmfit placement probe workflow |
| `test-telegram-channel.sh` | Telegram channel deployment + message flow |
| `test-slack-channel.sh` | Slack channel deployment (Socket Mode) |
| `test-web-proxy-api.sh` | Web proxy API — healthz, auth, models, chat completions (blocking + streaming), MCP SSE |

### Writing New Tests

See `docs/writing-integration-tests.md` for the full guide and template. Tests follow this pattern:

1. Create a `SympoziumInstance` + `AgentRun` with a deterministic task
2. Poll `status.phase` until `Succeeded` or `Failed`
3. Validate results (pod logs, status, filesystem)
4. Clean up all test resources

Add new tests to the `test-integration` target in the `Makefile`.

---

## Agent Tools

The agent-runner has 7 built-in tools defined in `cmd/agent-runner/tools.go`:

| Tool | Category | Description |
|------|----------|-------------|
| `execute_command` | IPC (sidecar) | Run shell commands in the skill sidecar |
| `read_file` | Native | Read file contents |
| `write_file` | Native | Write/create files |
| `list_directory` | Native | List directory contents |
| `send_channel_message` | IPC (bridge) | Send messages to Telegram/Slack/Discord/WhatsApp |
| `fetch_url` | Native | HTTP GET a URL and return the body |
| `schedule_task` | IPC (bridge) | Create/update/suspend/resume/delete SympoziumSchedule CRDs |

See `docs/writing-tools.md` for the full guide on adding new tools.

---

## Key Architecture Patterns

### IPC Flow (Agent ↔ Control Plane)

```
Agent tool writes JSON → /ipc/<dir>/*.json → fsnotify watcher → NATS publish → Controller handles
```

Directories: `/ipc/tools/` (sidecar exec), `/ipc/messages/` (channel messages), `/ipc/schedules/` (schedule requests).

### Event Bus (NATS Topics)

Key topics in `internal/eventbus/types.go`:

- `agent.run.requested/started/completed/failed` — AgentRun lifecycle
- `channel.message.received/send` — Channel message flow
- `schedule.upsert` — Agent self-scheduling requests
- `tool.exec.request/result` — Sidecar tool execution

### Memory

Each SympoziumInstance has a ConfigMap (`<name>-memory`) mounted at `/memory/MEMORY.md`. The controller extracts memory markers (`__SYMPOZIUM_MEMORY__...__SYMPOZIUM_MEMORY_END__`) from agent output and patches the ConfigMap.

### Skills

SkillPacks are CRDs containing Markdown instructions + optional sidecar definitions. When enabled on a SympoziumInstance, skills are mounted at `/skills/` and sidecars are injected into agent pods. See `docs/writing-skills.md`.

---

## Documentation Index

| Document | Location | Content |
|----------|----------|---------|
| Design document | `docs/sympozium-design.md` | Full architecture, CRD schemas, data flow, security model |
| Writing tools | `docs/writing-tools.md` | How to add new agent tools |
| Writing skills | `docs/writing-skills.md` | How to create SkillPack CRDs |
| Writing integration tests | `docs/writing-integration-tests.md` | Test patterns and templates |
| Web endpoint skill | `docs/skill-web-endpoint.md` | How to expose agents as HTTP APIs (OpenAI-compat + MCP) |
| Serving mode | `docs/serving-mode.md` | How serving mode works for long-lived agent deployments |
| Sample CRs | `config/samples/` | Example SympoziumInstance, AgentRun, SympoziumPolicy, SympoziumSchedule, SkillPack |
| CRD definitions | `api/v1alpha1/` | Go type definitions for all CRDs |
| Built-in PersonaPacks | `config/personas/` | Pre-configured agent bundles (platform-team, devops-essentials) |

---

## Common Tasks for Agents

### Adding a new tool
1. Add constant + definition + handler in `cmd/agent-runner/tools.go`
2. If IPC-based, add watcher in `internal/ipc/bridge.go` and topic in `internal/eventbus/types.go`
3. If it needs a controller handler, add a router in `internal/controller/`
4. Rebuild `agent-runner` (and `ipc-bridge`/`controller` if changed)
5. Write an integration test in `test/integration/`
6. Document in `docs/writing-tools.md`

### Adding a new channel
1. Create `channels/<name>/main.go`
2. Create `images/channel-<name>/Dockerfile`
3. Add to `CHANNELS` list in `Makefile`
4. The controller's `buildChannelDeployment` in `internal/controller/sympoziuminstance_controller.go` handles deployment

### Modifying a CRD
1. Edit type in `api/v1alpha1/<name>_types.go`
2. Run `make generate` to regenerate deepcopy and CRD YAML
3. Run `make install` to apply updated CRDs to cluster
4. Update the reconciler in `internal/controller/`

### Adding a PersonaPack
1. Create a YAML file in `config/personas/<name>.yaml`
2. Define personas with system prompts, skills, schedules, and memory seeds
3. Apply: `kubectl apply -f config/personas/<name>.yaml`
4. Activate via the TUI Personas tab or by patching `spec.authRefs` with kubectl

### Rebuilding after changes
```bash
# Compile check
go build ./...

# Rebuild affected images
make docker-build-<component> TAG=v0.1.0

# Load into Kind
kind load docker-image ghcr.io/sympozium-ai/sympozium/<component>:v0.1.0 --name kind

# Restart controller if controller/ipc-bridge/agent-runner changed
kubectl rollout restart deployment sympozium-controller-manager -n sympozium-system
```

```

### File: CHANGELOG.md
```md
# Changelog

## [0.8.9](https://github.com/sympozium-ai/sympozium/compare/v0.8.8...v0.8.9) (2026-04-02)


### Bug Fixes

* auto-store task/response in memory server after each agent run ([8f475fb](https://github.com/sympozium-ai/sympozium/commit/8f475fbc2bf600ca7fad12394e7c417dd63e2509))
* guard stale Job-not-found reconcile during postRun transition ([8d2ff41](https://github.com/sympozium-ai/sympozium/commit/8d2ff41972acb551a9aabc13cc02c1807ca50560))

## [0.8.8](https://github.com/sympozium-ai/sympozium/compare/v0.8.7...v0.8.8) (2026-04-01)


### Features

* reworked memory implementation ([81fdd0c](https://github.com/sympozium-ai/sympozium/commit/81fdd0c83725dc068bc869f01b5d1af5c421c282))


### Bug Fixes

* add missing observability-mcp-team persona pack to Helm chart ([fc0105c](https://github.com/sympozium-ai/sympozium/commit/fc0105c0d243bb0adc58680e29a4827b7aad88bd))

## [0.8.7](https://github.com/sympozium-ai/sympozium/compare/v0.8.6...v0.8.7) (2026-03-31)


### Bug Fixes

* stop Helm template from overriding node-probe host auto-detection ([4f0e5f4](https://github.com/sympozium-ai/sympozium/commit/4f0e5f41217d5ec9bf165dda7796be0df3fd307d))

## [0.8.6](https://github.com/sympozium-ai/sympozium/compare/v0.8.5...v0.8.6) (2026-03-31)


### Bug Fixes

* create namespace before Helm config init to fix fresh installs ([e49fa50](https://github.com/sympozium-ai/sympozium/commit/e49fa50f26604688a1dcbba6a3d06543b0442ea8))

## [0.8.5](https://github.com/sympozium-ai/sympozium/compare/v0.8.4...v0.8.5) (2026-03-31)


### Bug Fixes

* remove explicit host from node-probe targets to restore auto-detection ([f91229a](https://github.com/sympozium-ai/sympozium/commit/f91229afa5ba5ad0674ba6c9b202932b2a869f3f))

## [0.8.4](https://github.com/sympozium-ai/sympozium/compare/v0.8.3...v0.8.4) (2026-03-31)


### Bug Fixes

* strip directory prefix from CRD names when writing to temp dir ([1906327](https://github.com/sympozium-ai/sympozium/commit/1906327b3abd32dc887f5a09c98eada9e0fb09b6))

## [0.8.3](https://github.com/sympozium-ai/sympozium/compare/v0.8.2...v0.8.3) (2026-03-31)


### Bug Fixes

* add metrics.k8s.io RBAC to config/rbac/role.yaml for sympozium install ([0c1a51c](https://github.com/sympozium-ai/sympozium/commit/0c1a51c8d11354aa5e2df694e8557c120b474857))

## [0.8.2](https://github.com/sympozium-ai/sympozium/compare/v0.8.1...v0.8.2) (2026-03-31)


### Bug Fixes

* resolve remaining TypeScript index signature errors in yaml-panel ([8cea011](https://github.com/sympozium-ai/sympozium/commit/8cea0119064536a30ba8a1a15d119af73c9380a9))

## [0.8.1](https://github.com/sympozium-ai/sympozium/compare/v0.8.0...v0.8.1) (2026-03-31)


### Bug Fixes

* fail AgentRun when skill RBAC creation fails instead of silently continuing ([99ddb4d](https://github.com/sympozium-ai/sympozium/commit/99ddb4d698bedd758c7d5512e6da354dad5db754))
* resolve TypeScript index signature errors in yaml-panel ([4a576a1](https://github.com/sympozium-ai/sympozium/commit/4a576a1b8db3f77c7ee6cb610b08f212b3ab9cd0))

## [0.8.0](https://github.com/sympozium-ai/sympozium/compare/v0.7.0...v0.8.0) (2026-03-30)


### Features

* lifecycle hooks — preRun and postRun containers for agent runs ([a29a8c9](https://github.com/sympozium-ai/sympozium/commit/a29a8c99a67287f063f2b1398b9e499b57e51d35))
* lifecycle hooks — preRun and postRun containers for agent runs ([#67](https://github.com/sympozium-ai/sympozium/issues/67)) ([46250af](https://github.com/sympozium-ai/sympozium/commit/46250afb1e379378e0a82d1d450a811f0a2181dc))


### Bug Fixes

* update API key retrieval to use header instead of query parameter ([e320e8d](https://github.com/sympozium-ai/sympozium/commit/e320e8d8361107acf30af4d35b9df2cd866c0cda))
* update API key retrieval to use header instead of query parameter ([ba6281a](https://github.com/sympozium-ai/sympozium/commit/ba6281a546a18f2b42193c5203049b08eb4eb983))
* update RBAC rules to include metrics.k8s.io permissions for skill sidecars ([cad5b4a](https://github.com/sympozium-ai/sympozium/commit/cad5b4a7eef051efd239604e472be905b4d28d21))
* update RBAC rules to include metrics.k8s.io permissions for skill sidecars ([3f90317](https://github.com/sympozium-ai/sympozium/commit/3f90317d172cc8d43a0d37b952196f48b3f73fe5))

## [0.7.0](https://github.com/sympozium-ai/sympozium/compare/v0.6.1...v0.7.0) (2026-03-29)


### Features

* add apiKey support for provider models fetching ([369fab3](https://github.com/sympozium-ai/sympozium/commit/369fab35e02dd9a5effadb9ce68ccd39d14f6b0e))
* add apiKey support for provider models fetching ([fb4bb53](https://github.com/sympozium-ai/sympozium/commit/fb4bb53b302ff0e11b176e9dba2e19a8856d2295))


### Bug Fixes

* AgentRun status concurrency update ([87dbb22](https://github.com/sympozium-ai/sympozium/commit/87dbb2226b22de4106d7c7c90fb77101c4217f38))
* prevent apiserver image build timeout on multi-arch builds ([830329d](https://github.com/sympozium-ai/sympozium/commit/830329d94295f04a496594ff494100a9e48fd1e1)), closes [#60](https://github.com/sympozium-ai/sympozium/issues/60)

## [0.6.1](https://github.com/sympozium-ai/sympozium/compare/v0.6.0...v0.6.1) (2026-03-28)


### Bug Fixes

* chain release workflow from release-please via workflow_call ([22c9e1e](https://github.com/sympozium-ai/sympozium/commit/22c9e1e9a17a52907e6c3424855bc82ce1cfb5b1))

## [0.6.0](https://github.com/sympozium-ai/sympozium/compare/v0.5.8...v0.6.0) (2026-03-28)


### Features

* Add image pull secret propagation for agent run container ([51858a3](https://github.com/sympozium-ai/sympozium/commit/51858a3686d9a7593eaf20def93e77ad726825b6))
* Add image pull secret propagation for agentrun sidecar container ([d5f4852](https://github.com/sympozium-ai/sympozium/commit/d5f4852515320378b2a36a31a7ff3e6e083f0f9f))
* add RBAC permissions for metrics access on pods and nodes ([013b02e](https://github.com/sympozium-ai/sympozium/commit/013b02eede3918664eed3f0018d93e8d66782be8))
* add RBAC permissions for metrics access on pods and nodes ([d94ed79](https://github.com/sympozium-ai/sympozium/commit/d94ed79da573375e22186ebc8e6d5c264e56549d))

```

### File: CONTRIBUTING.md
```md
# Contributing to Sympozium

Thanks for your interest in contributing! This document covers how we work, what we expect from PRs, and how to get started.

---

## Where to Start

1. **Issues** — Check [GitHub Issues](https://github.com/sympozium-ai/sympozium/issues) for open bugs, feature requests, and `good first issue` labels.
2. **Roadmap** — The project roadmap lives in [GitHub Projects](https://github.com/sympozium-ai/sympozium/projects). Pick items from the current milestone.
3. **AGENTS.md** — If you're an AI coding agent (Copilot, Cursor, etc.), read [`AGENTS.md`](AGENTS.md) for repo layout, build instructions, and common task recipes.
4. **Documentation** — Architecture and guides live in [`docs/`](docs/):
   - [`sympozium-design.md`](docs/sympozium-design.md) — Full architecture and CRD schemas
   - [`writing-tools.md`](docs/writing-tools.md) — How to add agent tools
   - [`writing-skills.md`](docs/writing-skills.md) — How to create SkillPack CRDs
   - [`writing-integration-tests.md`](docs/writing-integration-tests.md) — Integration test patterns

---

## Development Setup

See [`AGENTS.md`](AGENTS.md) for the full setup guide. The short version:

```bash
# Prerequisites: Go 1.25+, Docker, Kind, kubectl
kind create cluster --name kind
make install                          # Install CRDs
make docker-build TAG=v0.1.0         # Build all images
# Load images into Kind (see AGENTS.md for the full loop)
kubectl apply -k config/             # Deploy control plane
```

---

## Local Development (no Docker build/push cycle)

For day-to-day development you can run the controller and API server as local processes against a remote (or local) cluster. This skips the Docker build → image load → rollout cycle entirely, which is especially helpful on low-bandwidth connections or when iterating quickly on controller logic.

All you need is a running cluster with CRDs installed and a valid kubeconfig.

### Run everything locally

```bash
make dev-all
```

This starts four services in parallel:

| Service | Address | What it does |
|---------|---------|-------------|
| Controller | `:9090` (metrics), `:9091` (health) | All CRD reconcilers running locally |
| API server | `:8080` | REST API for the UI |
| Vite dev server | `:5173` | Frontend with hot-reload |
| NATS port-forward | `:4222` | Forwards cluster NATS to localhost |

The in-cluster controller deployment is automatically scaled to zero so there's no conflict. When you Ctrl+C, the in-cluster controller is restored to 1 replica.

Open `http://localhost:5173` in your browser. The API token is `dev-token` (override with `SYMPOZIUM_TOKEN`).

### Run just the controller locally

If you're only working on controller logic and already have `make dev` running for the UI:

```bash
make run-controller
```

This builds and runs the controller manager locally, scaling down the in-cluster one. On exit it restores the in-cluster deployment.

### Run just the API server + UI

If you're only working on the API or frontend and want the in-cluster controller to keep running:

```bash
make dev
```

### Undeploy cluster workloads (keep CRDs)

To stop all in-cluster Sympozium deployments while keeping CRDs and their instances intact:

```bash
kubectl scale deploy -n sympozium-system --replicas=0 --all
```

This is useful when you want the local processes to be the only thing running, or when switching between local and cluster-based development.

---

## GitHub Checks

Every push and PR runs the following checks via GitHub Actions (`.github/workflows/build.yaml`):

| Check | What it does |
|-------|-------------|
| **go vet** | Static analysis for common Go mistakes |
| **go test -race -short** | Unit tests with the race detector enabled |
| **Docker build** | All 10 component images build successfully |

PRs must pass all checks before merging. On merge to `main`, images are automatically built and pushed to `ghcr.io/sympozium-ai/sympozium/`.

Run checks locally before pushing:

```bash
make vet        # go vet ./...
make test       # go test -race ./...
make build      # compile all binaries
go build ./...  # quick compile check
```

---

## Multi-Architecture Builds

Sympozium supports `linux/amd64` and `linux/arm64` (darwin for the CLI).

- **Docker images** are built with Docker Buildx + `docker/build-push-action@v6` with GitHub Actions cache (`type=gha`).
- **CLI releases** are cross-compiled for `linux/amd64`, `linux/arm64`, `darwin/amd64`, and `darwin/arm64` via the release workflow (`.github/workflows/release.yaml`).
- All Go binaries are built with `CGO_ENABLED=0` for static linking.

When adding a new image, ensure its Dockerfile works on both `amd64` and `arm64`. Use multi-stage builds from the existing Dockerfiles as a template.

---

## Conventional Commits

We use [Conventional Commits](https://www.conventionalcommits.org/) for all commit messages. This keeps the history readable and enables automated changelog generation.

### Format

```
<type>(<scope>): <description>

[optional body]

[optional footer(s)]
```

### Types

| Type | When to use |
|------|-------------|
| `feat` | A new feature (`feat: add schedule_task tool`) |
| `fix` | A bug fix (`fix: deduplicate fsnotify events in IPC bridge`) |
| `docs` | Documentation only (`docs: add Telegram setup instructions`) |
| `chore` | Maintenance, deps, CI (`chore: bump controller-gen to v0.17.2`) |
| `refactor` | Code change that neither fixes a bug nor adds a feature |
| `test` | Adding or updating tests (`test: add write-file integration test`) |
| `ci` | CI/CD changes (`ci: add multi-arch Docker build`) |

### Scopes (optional)

Use the component name: `agent-runner`, `controller`, `ipc-bridge`, `webhook`, `tui`, `slack`, `telegram`, `crd`, etc.

### Examples

```
feat(agent-runner): add fetch_url tool
fix(ipc-bridge): deduplicate fsnotify Create+Write events
docs: add CONTRIBUTING.md
test(integration): add k8s-ops-nodes test
ci: add arm64 to Docker build matrix
chore(deps): bump gorilla/websocket to v1.5.1
```

---

## Semantic Versioning

Sympozium follows [Semantic Versioning](https://semver.org/) (`vMAJOR.MINOR.PATCH`):

- **PATCH** (`v0.1.0` → `v0.1.1`) — Bug fixes, docs, minor improvements
- **MINOR** (`v0.1.0` → `v0.2.0`) — New features, new CRD fields (backward-compatible)
- **MAJOR** (`v1.0.0`) — Breaking API/CRD changes

### Releasing

1. Ensure all changes are committed and pushed to `main`.
2. Create and push a tag:
   ```bash
   git tag v0.1.1
   git push origin v0.1.1
   ```
3. The release workflow automatically:
   - Builds CLI binaries for all platforms
   - Packages install manifests
   - Builds and pushes all Docker images tagged with the version
   - Creates a GitHub Release with assets

While in `v0.x.x`, the API is not yet stable and breaking changes may occur in minor versions.

---

## Pull Request Guidelines

1. **One concern per PR** — Don't mix a feature, a bug fix, and a refactor in one PR.
2. **Conventional commit title** — The PR title becomes the merge commit message.
3. **Tests required** — Add or update unit tests. For new tools or major features, add an integration test in `test/integration/`.
4. **CRD changes** — If you modify types in `api/v1alpha1/`, run `make generate` and commit the generated files.
5. **Docs** — Update relevant docs in `docs/` if behavior changes.
6. **Compile check** — Run `go build ./...` before pushing.

---

## Code Standards

- **Go** — Follow standard Go conventions. Run `make fmt` and `make vet`.
- **Error handling** — Return errors, don't panic. Use `fmt.Errorf("context: %w", err)` for wrapping.
- **Logging** — Use the structured logger (`log.Info`, `log.Error`) with key-value pairs, not `fmt.Printf`.
- **Naming** — CRD types use PascalCase (`SympoziumInstance`). Tool names use snake_case (`execute_command`). NATS topics use dot-separated (`agent.run.completed`).
- **IPC protocol** — New IPC-based tools must follow the JSON file drop pattern: write to `/ipc/<dir>/`, bridge watches with fsnotify, publishes to NATS.

---

## Project Structure Conventions

| Pattern | Convention |
|---------|-----------|
| CRD types | `api/v1alpha1/<name>_types.go` |
| Reconcilers | `internal/controller/<name>_controller.go` |
| Routers (NATS → K8s) | `internal/controller/<name>_router.go` |
| Agent tools | All in `cmd/agent-runner/tools.go` |
| Channel pods | `channels/<name>/main.go` |
| Dockerfiles | `images/<name>/Dockerfile` |
| Integration tests | `test/integration/test-<name>.sh` |
| Sample CRs | `config/samples/<name>_sample.yaml` |

---

## Need Help?

- Open an issue for questions or discussion
- Check existing docs in `docs/` before asking
- Look at recent PRs for examples of good contributions

```

### File: index.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>sympozium</title>
  <style>
    body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif; max-width: 640px; margin: 80px auto; padding: 0 20px; color: #1e293b; }
    h1 { display: flex; align-items: center; gap: 12px; }
    h1 img { width: 48px; height: 48px; }
    pre { background: #0f172a; color: #e2e8f0; padding: 16px 20px; border-radius: 8px; overflow-x: auto; font-size: 14px; }
    a { color: #3b82f6; text-decoration: none; }
    a:hover { text-decoration: underline; }
    .subtitle { color: #64748b; margin-top: -12px; }
  </style>
</head>
<body>
  <h1>sympozium</h1>
  <p class="subtitle">Kubernetes-native AI Agent Management Platform</p>
  <h2>Install</h2>
  <pre>curl -fsSL https://deploy.sympozium.ai/install.sh | sh</pre>
  <h2>Deploy to your cluster</h2>
  <pre>sympozium install</pre>
  <p><a href="/docs/">Documentation</a> · <a href="https://github.com/sympozium-ai/sympozium">GitHub</a></p>
</body>
</html>

```

### File: install.sh
```sh
#!/bin/sh
# sympozium installer
# Usage: curl -fsSL https://deploy.sympozium.ai/install.sh | sh
#        curl -fsSL https://deploy.sympozium.ai/install.sh | sh -s -- --local   # Install to ~/.local/bin (no sudo)
#
# Downloads the latest sympozium CLI release from GitHub and installs
# the binary to /usr/local/bin (or ~/.local/bin with --local or if no sudo).

set -e

REPO="sympozium-ai/sympozium"
BINARY="sympozium"
LOCAL_INSTALL=""

# --- helpers ---

info() { printf '  \033[1;34m>\033[0m %s\n' "$*"; }
warn() { printf '  \033[1;33m>\033[0m %s\n' "$*"; }
err()  { printf '  \033[1;31m!\033[0m %s\n' "$*" >&2; exit 1; }

need() {
    command -v "$1" >/dev/null 2>&1 \
        || err "Required tool '$1' not found. Please install it and try again."
}

# --- parse arguments ---

parse_args() {
    while [ $# -gt 0 ]; do
        case "$1" in
            --local|-l)
                LOCAL_INSTALL="1"
                ;;
            --help|-h)
                echo "Usage: install.sh [OPTIONS]"
                echo ""
                echo "Options:"
                echo "  --local, -l    Install to ~/.local/bin (no sudo required)"
                echo "  --help, -h     Show this help message"
                exit 0
                ;;
            *)
                warn "Unknown option: $1"
                ;;
        esac
        shift
    done
}

# --- detect platform ---

detect_platform() {
    OS="$(uname -s)"
    ARCH="$(uname -m)"

    case "$OS" in
        Linux)  OS="linux" ;;
        Darwin) OS="darwin" ;;
        *)      err "Unsupported OS: $OS" ;;
    esac

    case "$ARCH" in
        x86_64|amd64)   ARCH="amd64" ;;
        aarch64|arm64)  ARCH="arm64" ;;
        *)              err "Unsupported architecture: $ARCH" ;;
    esac

    PLATFORM="${OS}-${ARCH}"
}

# --- fetch latest release ---

fetch_latest_tag() {
    need curl
    need tar

    # Use the releases redirect instead of the API to avoid
    # GitHub's 60-request/hour rate limit on unauthenticated API calls.
    TAG="$(curl -fsSI "https://github.com/${REPO}/releases/latest" 2>/dev/null \
        | grep -i '^location:' \
        | head -1 \
        | sed 's|.*/tag/||' \
        | tr -d '\r\n')"

    [ -n "$TAG" ] || err "Could not determine latest release. Check https://github.com/${REPO}/releases"
}

# --- download and install ---

install() {
    ASSET="${BINARY}-${PLATFORM}.tar.gz"
    URL="https://github.com/${REPO}/releases/download/${TAG}/${ASSET}"

    TMPDIR="$(mktemp -d)"
    trap 'rm -rf "$TMPDIR"' EXIT

    info "Downloading ${BINARY} ${TAG} for ${PLATFORM}..."
    curl -fsSL "$URL" -o "${TMPDIR}/${ASSET}" \
        || err "Download failed. Asset '${ASSET}' may not exist for your platform.\n  Check: https://github.com/${REPO}/releases/tag/${TAG}"

    info "Extracting..."
    tar -xzf "${TMPDIR}/${ASSET}" -C "$TMPDIR"

    BIN="$(find "$TMPDIR" -name "$BINARY" -type f | head -1)"
    [ -n "$BIN" ] || err "Binary not found in archive. Release asset may have an unexpected layout."

    chmod +x "$BIN"

    # Determine install directory
    if [ -n "$LOCAL_INSTALL" ]; then
        # User explicitly requested local install
        INSTALL_DIR="${HOME}/.local/bin"
        mkdir -p "$INSTALL_DIR"
        info "Installing to ${INSTALL_DIR} (--local mode)..."
    elif [ -w /usr/local/bin ]; then
        # /usr/local/bin is writable without sudo
        INSTALL_DIR="/usr/local/bin"
    elif command -v sudo >/dev/null 2>&1 && [ -t 0 ]; then
        # sudo is available and we're in an interactive terminal
        info "Installing to /usr/local/bin (requires sudo)..."
        if sudo mv "$BIN" "/usr/local/bin/${BINARY}"; then
            info "Installed ${BINARY} to /usr/local/bin/${BINARY}"
            return
        else
            warn "sudo failed, falling back to ~/.local/bin"
            INSTALL_DIR="${HOME}/.local/bin"
            mkdir -p "$INSTALL_DIR"
        fi
    else
        # No write access and no interactive sudo, use local install
        INSTALL_DIR="${HOME}/.local/bin"
        mkdir -p "$INSTALL_DIR"
        info "Installing to ${INSTALL_DIR} (no sudo available)..."
    fi

    mv "$BIN" "${INSTALL_DIR}/${BINARY}"
    info "Installed ${BINARY} to ${INSTALL_DIR}/${BINARY}"

    # Check if install dir is in PATH
    case ":$PATH:" in
        *":${INSTALL_DIR}:"*) ;;
        *)
            warn "Add ${INSTALL_DIR} to your PATH to use '${BINARY}' directly:"
            echo ""
            echo "    export PATH=\"\$HOME/.local/bin:\$PATH\""
            echo ""
            ;;
    esac
}

# --- main ---

main() {
    parse_args "$@"
    info "sympozium installer"
    detect_platform
    fetch_latest_tag
    install
    info "Done! Run 'sympozium install' to deploy Sympozium to your cluster."
}

main "$@"

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.

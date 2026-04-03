---
id: n8n-io-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:29:10.537471
---

# KNOWLEDGE EXTRACT: n8n-io
> **Extracted on:** 2026-03-30 17:49:01
> **Source:** n8n-io

---

## File: `n8n-docs.md`
```markdown
# 📦 n8n-io/n8n-docs [🔖 PENDING/APPROVE]
🔗 https://github.com/n8n-io/n8n-docs
🌐 https://docs.n8n.io

## Meta
- **Stars:** ⭐ 1532 | **Forks:** 🍴 3932
- **Language:** HTML | **License:** NOASSERTION
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Documentation for n8n, a fair-code licensed automation tool with a free community edition and powerful enterprise options. Build AI functionality into your workflows.

## README (trích đầu)
```
![Banner image](https://user-images.githubusercontent.com/10284570/173569848-c624317f-42b1-45a6-ab09-f0ea3c247648.png)

# n8n Docs

This repository hosts the documentation for [n8n](https://n8n.io/), an extendable workflow automation tool which enables you to connect anything to everything. The documentation is live at [docs.n8n.io](https://docs.n8n.io/).


## Previewing and building the documentation locally

### Prerequisites

* Python 3.8 or above
* Pip
* Follow the [recommended configuration and auto-complete](https://squidfunk.github.io/mkdocs-material/creating-your-site/#minimal-configuration) guidance for the theme. This will help when working with the `mkdocs.yml` file.
* The repo includes a `.editorconfig` file. Make sure your local editor settings **do not override** these settings. In particular:
	- Don't allow your editor to replace tabs with spaces. This can affect our code samples (which must retain tabs for people building nodes).
	- One tab must be equivalent to four spaces.
* n8n recommends using a virtual environment when working with Python, such as [venv](https://docs.python.org/3/tutorial/venv.html).

### Steps

#### For members of the n8n GitHub organization:

n8n members have access to the full Insiders version of the site theme.

1. Set up an SSH token and add it to your GitHub account. Refer to [GitHub | About SSH](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/about-ssh) for guidance.
2. Then run these commands:

	```bash
	git clone --recurse-submodules git@github.com:n8n-io/n8n-docs.git
	cd n8n-docs
 	# Set up a virtual environment (steps depend on your system) and activate it
 	# Install dependencies
	pip install -r requirements.txt
	pip install _submodules/insiders
	```

#### For external contributors:

External contributors don't have access to the full Insiders version of the site theme. You can rely on the preview builds on pull requests, or use the free version of Material for MkDocs.

Fork the repository, then:

```bash
git clone https://github.com/<your-username>/n8n-docs.git
cd n8n-docs
# Set up a virtual environment (steps depend on your system) and activate it
# Install dependencies
pip install -r requirements.txt
pip install mkdocs-material
```

#### To serve a local preview:

```
mkdocs serve --strict
```

## Troubleshooting

### Errors due to missing extensions or features

n8n's docs use the Insiders version of the Material theme. This is not available to external contributors. The standard (free) version has most of the features, but you may get errors if the site is relying on features currently in Insiders. The feature set is constantly changing, as the theme creator gradually moves features out of Insiders to general availability. You can view the currently restricted feautres here: [Material Insiders Benefits](https://squidfunk.github.io/mkdocs-material/insiders/benefits/).

To work around this, you can either:

- Rely on the preview builds when you open a PR.
- Temporarily c
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `n8n-hosting.md`
```markdown
# 📦 n8n-io/n8n-hosting [🔖 PENDING/APPROVE]
🔗 https://github.com/n8n-io/n8n-hosting


## Meta
- **Stars:** ⭐ 1534 | **Forks:** 🍴 763
- **Language:** Go Template | **License:** Unknown
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Example of self-hosting n8n in various environments like docker, kubernetes, etc.

## README (trích đầu)
```
# n8n Hosting

Official hosting configurations for [n8n](https://n8n.io) -- the workflow automation platform.

## Kubernetes (Helm Chart)

The official n8n Helm chart for production Kubernetes deployments.

```bash
helm install n8n oci://ghcr.io/n8n-io/n8n-helm-chart/n8n --version 1.0.0 -f my-values.yaml
```

See the [chart README](../../../README.md) for full documentation and the [examples](./charts/n8n/examples/) directory for common configurations.

## Docker Compose

| Directory | Description |
|---|---|
| [docker-compose/withPostgres](./docker-compose/withPostgres/) | n8n + PostgreSQL |
| [docker-compose/withPostgresAndWorker](./docker-compose/withPostgresAndWorker/) | n8n + PostgreSQL + Redis + worker (queue mode) |
| [docker-compose/subfolderWithSSL](./docker-compose/subfolderWithSSL/) | n8n behind SSL reverse proxy in subfolder |
| [docker-caddy](./docker-caddy/) | n8n with Caddy reverse proxy |

## Kubernetes (Raw Manifests)

See [`kubernetes/`](./kubernetes/) for raw Kubernetes manifest examples used in cloud provider tutorials (AWS, Azure, GCP).

## Documentation

- [n8n docs](https://docs.n8n.io/)
- [Self-hosting guides](https://docs.n8n.io/hosting/)
- [Community forum](https://community.n8n.io/)

```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `n8n.md`
```markdown
# 📦 n8n-io/n8n [🔖 PENDING]
🔗 https://github.com/n8n-io/n8n
🌐 https://n8n.io

## Meta
- **Stars:** ⭐ 181211 | **Forks:** 🍴 56204
- **Language:** TypeScript | **License:** NOASSERTION
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING

## Description:
Fair-code workflow automation platform with native AI capabilities. Combine visual building with custom code, self-host or cloud, 400+ integrations.

## README (trích đầu)
```
![Banner image](https://user-images.githubusercontent.com/10284570/173569848-c624317f-42b1-45a6-ab09-f0ea3c247648.png)

# n8n - Secure Workflow Automation for Technical Teams

n8n is a workflow automation platform that gives technical teams the flexibility of code with the speed of no-code. With 400+ integrations, native AI capabilities, and a fair-code license, n8n lets you build powerful automations while maintaining full control over your data and deployments.

![n8n.io - Screenshot](https://raw.githubusercontent.com/n8n-io/n8n/master/assets/n8n-screenshot-readme.png)

## Key Capabilities

- **Code When You Need It**: Write JavaScript/Python, add npm packages, or use the visual interface
- **AI-Native Platform**: Build AI agent workflows based on LangChain with your own data and models
- **Full Control**: Self-host with our fair-code license or use our [cloud offering](https://app.n8n.cloud/login)
- **Enterprise-Ready**: Advanced permissions, SSO, and air-gapped deployments
- **Active Community**: 400+ integrations and 900+ ready-to-use [templates](https://n8n.io/workflows)

## Quick Start

Try n8n instantly with [npx](https://docs.n8n.io/hosting/installation/npm/) (requires [Node.js](https://nodejs.org/en/)):

```
npx n8n
```

Or deploy with [Docker](https://docs.n8n.io/hosting/installation/docker/):

```
docker volume create n8n_data
docker run -it --rm --name n8n -p 5678:5678 -v n8n_data:/home/node/.n8n docker.n8n.io/n8nio/n8n
```

Access the editor at http://localhost:5678

## Resources

- 📚 [Documentation](https://docs.n8n.io)
- 🔧 [400+ Integrations](https://n8n.io/integrations)
- 💡 [Example Workflows](https://n8n.io/workflows)
- 🤖 [AI & LangChain Guide](https://docs.n8n.io/advanced-ai/)
- 👥 [Community Forum](https://community.n8n.io)
- 📖 [Community Tutorials](https://community.n8n.io/c/tutorials/28)

## Support

Need help? Our community forum is the place to get support and connect with other users:
[community.n8n.io](https://community.n8n.io)

## License

n8n is [fair-code](https://faircode.io) distributed under the [Sustainable Use License](https://github.com/n8n-io/n8n/blob/master/LICENSE.md) and [n8n Enterprise License](https://github.com/n8n-io/n8n/blob/master/LICENSE_EE.md).

- **Source Available**: Always visible source code
- **Self-Hostable**: Deploy anywhere
- **Extensible**: Add your own nodes and functionality

[Enterprise licenses](mailto:license@n8n.io) available for additional features and support.

Additional information about the license model can be found in the [docs](https://docs.n8n.io/sustainable-use-license/).

## Contributing

Found a bug 🐛 or have a feature idea ✨? Check our [Contributing Guide](https://github.com/n8n-io/n8n/blob/master/CONTRIBUTING.md) for a setup guide & best practices.

## Join the Team

Want to shape the future of automation? Check out our [job posts](https://n8n.io/careers) and join our team!

## What does n8n mean?

**Short answer:** It means "nodemation" and is pronounced as n-eight-n.

**
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `task-runner-launcher.md`
```markdown
# 📦 n8n-io/task-runner-launcher [🔖 PENDING/APPROVE]
🔗 https://github.com/n8n-io/task-runner-launcher


## Meta
- **Stars:** ⭐ 47 | **Forks:** 🍴 44
- **Language:** Go | **License:** NOASSERTION
- **Last updated:** 2026-03-25
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
CLI utility to launch an n8n task runner in external mode

## README (trích đầu)
```
# task-runner-launcher

[![codecov](https://codecov.io/gh/n8n-io/task-runner-launcher/graph/badge.svg?token=NW1BW05Q5P)](https://codecov.io/gh/n8n-io/task-runner-launcher)

CLI utility to launch an [n8n task runner](https://docs.n8n.io/hosting/configuration/task-runners/) in `external` mode. The launcher's purpose is to minimize resource use by launching a runner on demand, i.e. only when no runner is available and when a task is ready for pickup. It also makes sure the runner stays responsive and recovers from crashes.

```
./task-runner-launcher javascript
2024/11/29 13:37:46 INFO  [launcher:js] Starting launcher goroutine...
2024/11/29 13:37:46 DEBUG [launcher:js] Changed into working directory
2024/11/29 13:37:46 DEBUG [launcher:js] Prepared env vars for runner
2024/11/29 13:37:46 INFO  [launcher:js] Waiting for task broker to be ready...
2024/11/29 13:37:46 DEBUG [launcher:js] Task broker is ready
2024/11/29 13:37:46 DEBUG [launcher:js] Fetched grant token for launcher
2024/11/29 13:37:46 DEBUG [launcher:js] Launcher ID: fc6c24b9f764ae55
2024/11/29 13:37:46 DEBUG [launcher:js] Connected: ws://127.0.0.1:5679/runners/_ws?id=fc6c24b9f764ae55
2024/11/29 13:37:46 DEBUG [launcher:js] <- Received message `broker:inforequest`
2024/11/29 13:37:46 DEBUG [launcher:js] -> Sent message `runner:info`
2024/11/29 13:37:46 DEBUG [launcher:js] <- Received message `broker:runnerregistered`
2024/11/29 13:37:46 DEBUG [launcher:js] -> Sent message `runner:taskoffer` for offer ID `5990b980a04945bd`
2024/11/29 13:37:46 INFO  [launcher:js] Waiting for launcher's task offer to be accepted...
```

## Sections

- [Setup](../../../core/security/QUARANTINE/vetted/repos/claude_code_templates/cli_tool/components/skills/scientific/qiskit/references/setup.md) - how to set up the launcher in a production environment
- [Development](../../../core/security/QUARANTINE/vetted/repos/llm_lean_log/docs/development.md) - how to set up a development environment to work on the launcher
- [Release](../../../core/security/QUARANTINE/vetted/repos/claude_code_templates/cli_tool/components/commands/git/release.md) - how to release a new version of the launcher
- [Lifecycle](lifecycle.md) - how the launcher works

```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```


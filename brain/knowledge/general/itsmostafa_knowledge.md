---
id: itsmostafa-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:55.728074
---

# KNOWLEDGE EXTRACT: itsmostafa
> **Extracted on:** 2026-03-30 17:38:10
> **Source:** itsmostafa

---

## File: `aws-agent-skills.md`
```markdown
# 📦 itsmostafa/aws-agent-skills [🔖 PENDING/APPROVE]
🔗 https://github.com/itsmostafa/aws-agent-skills


## Meta
- **Stars:** ⭐ 1052 | **Forks:** 🍴 437
- **Language:** Python | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
AWS Skills for Agents

## README (trích đầu)
```
# AWS Agent Skills

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Claude Code](https://img.shields.io/badge/Claude-Code-blueviolet)](https://claude.ai/code)
![Last Commit](https://img.shields.io/github/last-commit/itsmostafa/aws-agent-skills)
![GitHub Stars](https://img.shields.io/github/stars/itsmostafa/aws-agent-skills)

Supercharge Claude Code with AWS cloud engineering skills across 18 core AWS services.

## 🚀 Why AWS Agent Skills?

Developing AWS solutions is complex spanning IAM, compute, storage, security, serverless, networking, and more.

AWS Agent Skills equips Claude Code (and Codex) with deep expertise across 18 AWS domains, enabling automated cloud engineering support from IaC templates to debugging guidance and security best practices.

Automatically checks AWS documentation for updates on a weekly basis to ensure skills stay current with AWS service changes.

### Why not just use an MCP?

AWS MCP is great for live docs and API calls, but AWS Agent Skills is designed for reasoning first.
It gives AI Agents a curated, LLM-optimized AWS knowledge base with real-world patterns, edge cases, and best practices, without streaming large docs or schemas.
Because the skills are local and pre compressed, it is far more token efficient, keeps the context window small and predictable, and avoids MCP infrastructure, latency, and expanded credential exposure.

## Installation

### Claude Code

#### From Marketplace

```bash
# Add the marketplace
/plugin marketplace add itsmostafa/aws-agent-skills

# Install the plugin
/plugin install aws-agent-skills
```

#### From GitHub

```bash
/plugin install https://github.com/itsmostafa/aws-agent-skills
```

#### Local Development

```bash
/plugin install ./path/to/aws-agent-skills
```

### Codex CLI

```bash
$skill-installer install https://github.com/itsmostafa/aws-agent-skills/<skill-name>
```

For example, to install the `rlhf` skill:

```bash
$skill-installer install https://github.com/itsmostafa/aws-agent-skills/rlhf
```

## Available Skills

| Skill | Description |
|-------|-------------|
| **iam** | Identity and Access Management - users, roles, policies, permissions |
| **lambda** | Serverless functions - deployment, triggers, debugging |
| **dynamodb** | NoSQL database - table design, queries, indexes |
| **s3** | Object storage - buckets, objects, security, lifecycle |
| **api-gateway** | REST and HTTP APIs - integrations, authorization |
| **ec2** | Virtual machines - instances, AMIs, networking |
| **ecs** | Container orchestration - clusters, services, tasks |
| **eks** | Kubernetes - clusters, node groups, IRSA |
| **cloudformation** | Infrastructure as Code - templates, stacks, drift |
| **cloudwatch** | Monitoring - logs, metrics, alarms, dashboards |
| **rds** | Relational databases - instances, backups, replication |
| **sqs** | Message queues - standard, FIFO, dead-letter queues |
| **sns** | Notifications - topics, subscri
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```


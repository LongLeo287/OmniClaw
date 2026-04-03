---
id: zxkane-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:32:48.018930
---

# KNOWLEDGE EXTRACT: zxkane
> **Extracted on:** 2026-03-30 18:01:32
> **Source:** zxkane

---

## File: `aws-skills.md`
```markdown
# 📦 zxkane/aws-skills [🔖 PENDING/APPROVE]
🔗 https://github.com/zxkane/aws-skills


## Meta
- **Stars:** ⭐ 219 | **Forks:** 🍴 24
- **Language:** Shell | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Claude Agent Skills for AWS

## README (trích đầu)
```
# AWS Skills for Claude Code

Claude Code plugins for AWS development with specialized knowledge and MCP server integrations, including CDK, serverless architecture, cost optimization, and Bedrock AgentCore for AI agent deployment.

## Plugins

### 0. AWS Common Plugin (Dependency)

Shared AWS agent skills including AWS Documentation MCP configuration for querying up-to-date AWS knowledge.

**Features**:
- AWS MCP server configuration guide
- Documentation MCP setup for querying AWS knowledge
- Shared by all other AWS plugins as a dependency

**Note**: This plugin is automatically loaded as a dependency by other plugins. Install it first if installing plugins individually.

### 1. AWS CDK Plugin

AWS CDK development skill with integrated MCP server for infrastructure as code.

**Features**:
- AWS CDK best practices and patterns
- Pre-deployment validation script
- Comprehensive CDK patterns reference

**Integrated MCP Server**:
- AWS CDK MCP (stdio)

### 2. AWS Cost & Operations Plugin

Cost optimization, monitoring, and operational excellence with 3 integrated MCP servers.

**Features**:
- Cost estimation and optimization
- Monitoring and observability patterns
- Operational best practices

**Integrated MCP Servers**:
- AWS Pricing
- AWS Cost Explorer
- Amazon CloudWatch

### 3. AWS Serverless & Event-Driven Architecture Plugin

Serverless and event-driven architecture patterns based on Well-Architected Framework.

**Features**:
- Well-Architected serverless design principles
- Event-driven architecture patterns
- Orchestration with Step Functions
- Saga patterns for distributed transactions
- Event sourcing patterns

### 4. AWS Agentic AI Plugin

AWS Bedrock AgentCore comprehensive expert for deploying and managing AI agents.

**Features**:
- Gateway service for converting REST APIs to MCP tools
- Runtime service for deploying and scaling agents
- Memory service for managing conversation state
- Identity service for credential and access management
- Code Interpreter for secure code execution
- Browser service for web automation
- Observability for tracing and monitoring

## Installation

Add the marketplace to Claude Code:

```bash
/plugin marketplace add zxkane/aws-skills
```

Install plugins individually:

```bash
# Install the common dependency first
/plugin install aws-common@aws-skills

# Then install the plugins you need
/plugin install aws-cdk@aws-skills
/plugin install aws-cost-ops@aws-skills
/plugin install serverless-eda@aws-skills
/plugin install aws-agentic-ai@aws-skills
```

## Core CDK Principles

### Resource Naming

**Do NOT explicitly specify resource names** when they are optional in CDK constructs.

```typescript
// ✅ GOOD - Let CDK generate unique names
new lambda.Function(this, 'MyFunction', {
  // No functionName specified
});

// ❌ BAD - Prevents multiple deployments
new lambda.Function(this, 'MyFunction', {
  functionName: 'my-lambda',
});
```

### Lambda Functions

Use appropriate constructs for automatic bundling:

- 
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```


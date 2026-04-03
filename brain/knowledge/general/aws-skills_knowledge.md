---
id: aws-skills-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:18:55.865674
---

# KNOWLEDGE EXTRACT: aws-skills
> **Extracted on:** 2026-03-30 13:24:05
> **Source:** aws-skills

---

## File: `.gitignore`
```
# Dependencies
node_modules/
.pnp
.pnp.js

# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
pip-wheel-metadata/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST
venv/
ENV/
env/

# CDK
cdk.out/
cdk.context.json
.cdk.staging/

# AWS
.aws/
*.pem
*.key

# Environment variables
.env
.env.local
.env.development.local
.env.test.local
.env.production.local

# IDE
.vscode/
.idea/
*.swp
*.swo
*~
.DS_Store

# Logs
logs/
*.log
npm-debug.log*
yarn-debug.log*
yarn-error.log*
lerna-debug.log*

# Testing
coverage/
.nyc_output
.pytest_cache/

# Build artifacts
*.zip
*.tar.gz
dist/
build/

# Temporary files
tmp/
temp/
*.tmp

# OS files
Thumbs.db
ehthumbs.db
Desktop.ini

# AWS credentials (NEVER commit)
*credentials*
*secrets*
.aws-sam/

# MCP cache
.aws-docs-cache/

# Package manager lock files (optional - you may want to commit these)
# package-lock.json
# yarn.lock
# poetry.lock

# Claude Code
.claude/settings.local.json
CLAUDE.local.md
```

## File: `CLAUDE.md`
```markdown
# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is an AWS skills plugin marketplace for Claude Code. It contains 5 plugins that provide AWS development expertise through skills and MCP server integrations.

## Architecture

```
.claude-plugin/marketplace.json    # Plugin marketplace definition (versions, MCP servers)
plugins/
├── aws-common/                    # Shared skills (aws-mcp-setup) - dependency for all others
├── aws-cdk/                       # CDK infrastructure as code
├── aws-cost-ops/                  # Cost optimization & monitoring
├── serverless-eda/                # Serverless & event-driven patterns
└── aws-agentic-ai/                # Bedrock AgentCore for AI agents
```

Each plugin contains:
- `skills/<skill-name>/SKILL.md` - Main skill file with frontmatter config
- `skills/<skill-name>/references/` - Detailed reference documentation
- Optional: `scripts/`, `services/`, `cross-service/` directories

## Testing Skills Locally

Skills are symlinked from `.claude/skills/` for local development:

```bash
# Start Claude Code in this directory - skills auto-load
cd /data/git/agentic/aws-skills
claude

# Verify skills loaded
/skills
/context
```

**Non-interactive testing:**
```bash
claude -p "List all available skills in this project"
claude -p "Read the frontmatter of aws-cdk-development skill"
```

**If symlinks break, recreate them:**
```bash
cd .claude && rm -rf skills && mkdir skills
ln -s ../../plugins/aws-common/skills/aws-mcp-setup skills/
ln -s ../../plugins/aws-cdk/skills/aws-cdk-development skills/
ln -s ../../plugins/serverless-eda/skills/aws-serverless-eda skills/
ln -s ../../plugins/aws-agentic-ai/skills/aws-agentic-ai skills/
ln -s ../../plugins/aws-cost-ops/skills/aws-cost-operations skills/
```

## Skill Frontmatter (Claude Code 2.1 Features)

Skills use these frontmatter fields for Claude Code 2.1:

```yaml
---
name: skill-name
description: ...
context: fork                    # Run in forked sub-agent context
model: sonnet                    # Specify model for skill execution
skills:
  - other-skill                  # Auto-load sub-skills
allowed-tools:
  - mcp__server__*               # Wildcard MCP tool permissions
  - Bash(aws *)                  # Wildcard bash permissions
hooks:
  PreToolUse:
    - matcher: Bash(cdk deploy*)
      command: aws sts get-caller-identity --query Account --output text
      once: true                 # Run hook only once per session
---
```

## MCP Server Naming

MCP servers use short names due to Bedrock's 64-char tool name limit:
- `cdk` - AWS CDK MCP
- `pricing` - AWS Pricing MCP
- `costexp` - Cost Explorer MCP
- `cw` - CloudWatch MCP

Tool names follow pattern: `mcp__plugin_{plugin}_{server}__{tool}`

## Version Management

Versions are in `.claude-plugin/marketplace.json`:
- `metadata.version` - Overall marketplace version
- `plugins[].version` - Individual plugin versions

### Version Bump Rules

| Change Type | Version Bump | Examples |
|-------------|--------------|----------|
| **Minor** (x.Y.0) | New features, new skills, new dependencies | Add new skill, add `skills:` dependency, add MCP server |
| **Patch** (x.y.Z) | Bug fixes, doc updates, config tweaks | Fix broken links, update descriptions, fix typos |

**When to bump:**
- Adding/modifying `skills:` frontmatter dependencies → Minor bump for affected plugins
- Adding new plugin → Minor bump for marketplace version
- Updating skill content without structural changes → Patch bump
- Fixing configuration issues → Patch bump

**Always bump versions** when modifying plugin content before committing.

## Key Files to Modify

| Task | Files |
|------|-------|
| Add/update skill content | `plugins/<plugin>/skills/<skill>/SKILL.md` |
| Add reference docs | `plugins/<plugin>/skills/<skill>/references/*.md` |
| Add MCP servers to plugin | `.claude-plugin/marketplace.json` → `plugins[].mcpServers` |
| Change plugin metadata | `.claude-plugin/marketplace.json` |
```

## File: `LICENSE`
```
MIT License

Copyright (c) 2025 Mengxin Zhu

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## File: `README.md`
```markdown
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

- **TypeScript/JavaScript**: `NodejsFunction` from `aws-cdk-lib/aws-lambda-nodejs`
- **Python**: `PythonFunction` from `@aws-cdk/aws-lambda-python-alpha`

### Pre-Deployment Validation

Before committing CDK code:

```bash
npm run build
npm test
npm run lint
cdk synth
./scripts/validate-stack.sh
```

## Usage Examples

### CDK Development

Ask Claude to help with CDK:

```
Create a CDK stack with a Lambda function that processes S3 events
```

Claude will:
- Follow CDK best practices
- Use NodejsFunction for automatic bundling
- Avoid explicit resource naming
- Grant proper IAM permissions
- Use MCP servers for latest AWS information

### Cost Optimization

Estimate costs before deployment:

```
Estimate the monthly cost of running 10 Lambda functions with 1M invocations each
```

Analyze current spending:

```
Show me my AWS costs for the last 30 days broken down by service
```

### Monitoring and Observability

Set up monitoring:

```
Create CloudWatch alarms for my Lambda functions to alert on errors and high duration
```

Investigate issues:

```
Show me CloudWatch logs for my API Gateway errors in the last hour
```

### Security and Audit

Audit activity:

```
Show me all IAM changes made in the last 7 days
```

Assess security:

```
Run a Well-Architected security assessment on my infrastructure
```

### Serverless Development

Build serverless applications:

```
Create a serverless API with Lambda and API Gateway for user management
```

Implement event-driven workflow:

```
Create an event-driven order processing system with EventBridge and Step Functions
```

Orchestrate complex workflows:

```
Implement a saga pattern for booking flights, hotels, and car rentals with compensation logic
```

### AI Agent Development

Deploy AI agents with Bedrock AgentCore:

```
Deploy a REST API as an MCP tool using AgentCore Gateway
```

Manage agent memory:

```
Set up conversation memory for my AI agent with DynamoDB backend
```

Monitor agent performance:

```
Configure observability for my AgentCore runtime with CloudWatch dashboards
```

## Structure

```
.
├── .claude-plugin/
│   └── marketplace.json              # Plugin marketplace configuration
├── plugins/                          # Each plugin has isolated skills
│   ├── aws-common/
│   │   └── skills/
│   │       └── aws-mcp-setup/        # Shared MCP configuration skill
│   │           └── SKILL.md
│   ├── aws-cdk/
│   │   └── skills/
│   │       └── aws-cdk-development/  # CDK development skill
│   │           ├── SKILL.md
│   │           ├── references/
│   │           │   └── cdk-patterns.md
│   │           └── scripts/
│   │               └── validate-stack.sh
│   ├── aws-cost-ops/
│   │   └── skills/
│   │       └── aws-cost-operations/  # Cost & operations skill
│   │           ├── SKILL.md
│   │           └── references/
│   │               ├── operations-patterns.md
│   │               └── cloudwatch-alarms.md
│   ├── serverless-eda/
│   │   └── skills/
│   │       └── aws-serverless-eda/   # Serverless & EDA skill
│   │           ├── SKILL.md
│   │           └── references/
│   │               ├── serverless-patterns.md
│   │               └── eda-patterns.md
│   └── aws-agentic-ai/
│       └── skills/
│           └── aws-agentic-ai/       # Bedrock AgentCore skill
│               ├── SKILL.md
│               ├── services/         # Service-specific docs
│               └── cross-service/    # Cross-service patterns
└── README.md
```

## MCP Server Names

MCP server names use short identifiers to comply with Bedrock's 64-character tool name limit. The naming pattern is: `mcp__plugin_{plugin}_{server}__{tool}`

Examples: `awsdocs` (AWS docs), `cdk` (CDK), `cw` (CloudWatch), `sfn` (Step Functions), `sam` (Serverless), etc.

## Resources

- [Claude Agent Skills](https://docs.claude.com/en/brain/knowledge/docs_legacy/claude-code/skills)
- [AWS MCP Servers](https://awslabs.github.io/mcp/)
- [AWS CDK](https://aws.amazon.com/cdk/)
- [Amazon Bedrock AgentCore](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html)
- [MCP Protocol](https://modelcontextprotocol.io/)

## License

MIT License - see [LICENSE](LICENSE)
```

## File: `brain/knowledge/docs_legacy/aws-mcp-setup.md`
```markdown
# AWS MCP Server Configuration Guide

## Overview

This guide helps you configure AWS MCP tools for Claude Code. Two options are available:

| Option | Requirements | Capabilities |
|--------|--------------|--------------|
| **Full AWS MCP Server** | Python 3.10+, uvx, AWS credentials | Execute AWS API calls + documentation search |
| **AWS Documentation MCP** | None | Documentation search only |

## Step 1: Check Existing Configuration

Before configuring, check if AWS MCP tools are already available using either method:

### Method A: Check Available Tools (Recommended)

Look for these tool name patterns in Claude Code's available tools:
- `mcp__aws-mcp__*` or `mcp__aws__*` → Full AWS MCP Server configured
- `mcp__*awsdocs*__aws___*` → AWS Documentation MCP configured

**How to check**: Run `/mcp` command in Claude Code to list all active MCP servers.

### Method B: Check Configuration Files

Claude Code uses hierarchical configuration (precedence: local → project → user → enterprise):

| Scope | File Location | Use Case |
|-------|---------------|----------|
| Local | `.claude.json` (in project) | Personal/experimental |
| Project | `.mcp.json` (project root) | Team-shared |
| User | `~/.claude.json` | Cross-project personal |
| Enterprise | System managed directories | Organization-wide |

Check these files for `mcpServers` containing `aws-mcp`, `aws`, or `awsdocs` keys:

```bash
# Check project config
cat .mcp.json 2>/dev/null | grep -E '"(aws-mcp|aws|awsdocs)"'

# Check user config
cat ~/.claude.json 2>/dev/null | grep -E '"(aws-mcp|aws|awsdocs)"'

# Or use Claude CLI
claude mcp list
```

If AWS MCP is already configured, no further setup needed.

## Step 2: Choose Configuration Method

### Automatic Detection

Run these commands to determine which option to use:

```bash
# Check for uvx (requires Python 3.10+)
which uvx || echo "uvx not available"

# Check for valid AWS credentials
aws sts get-caller-identity || echo "AWS credentials not configured"
```

### Option A: Full AWS MCP Server (Recommended)

**Use when**: uvx available AND AWS credentials valid

**Prerequisites**:
- Python 3.10+ with `uv` package manager
- AWS credentials configured (via profile, environment variables, or IAM role)

**Required IAM Permissions**:
```json
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow",
    "Action": [
      "aws-mcp:InvokeMCP",
      "aws-mcp:CallReadOnlyTool",
      "aws-mcp:CallReadWriteTool"
    ],
    "Resource": "*"
  }]
}
```

**Configuration** (add to your MCP settings):
```json
{
  "mcpServers": {
    "aws-mcp": {
      "command": "uvx",
      "args": [
        "mcp-proxy-for-aws@latest",
        "https://aws-mcp.us-east-1.api.aws/mcp",
        "--metadata", "AWS_REGION=us-west-2"
      ]
    }
  }
}
```

**Credential Configuration Options**:

1. **AWS Profile** (recommended for development):
   ```json
   "args": [
     "mcp-proxy-for-aws@latest",
     "https://aws-mcp.us-east-1.api.aws/mcp",
     "--profile", "my-profile",
     "--metadata", "AWS_REGION=us-west-2"
   ]
   ```

2. **Environment Variables**:
   ```json
   "env": {
     "AWS_ACCESS_KEY_ID": "...",
     "AWS_SECRET_ACCESS_KEY": "...",
     "AWS_REGION": "us-west-2"
   }
   ```

3. **IAM Role** (for EC2/ECS/Lambda): No additional config needed - uses instance credentials

**Additional Options**:
- `--region <region>`: Override AWS region
- `--read-only`: Restrict to read-only tools
- `--log-level <level>`: Set logging level (debug, info, warning, error)

**Reference**: https://github.com/aws/mcp-proxy-for-aws

### Option B: AWS Documentation MCP Server (No Auth)

**Use when**:
- No Python/uvx environment
- No AWS credentials
- Only need documentation search (no API execution)

**Configuration**:
```json
{
  "mcpServers": {
    "awsdocs": {
      "type": "http",
      "url": "https://knowledge-mcp.global.api.aws"
    }
  }
}
```

## Step 3: Verification

After configuration, verify tools are available:

**For Full AWS MCP**:
- Look for tools: `mcp__aws-mcp__aws___search_documentation`, `mcp__aws-mcp__aws___call_aws`

**For Documentation MCP**:
- Look for tools: `mcp__awsdocs__aws___search_documentation`, `mcp__awsdocs__aws___read_documentation`

## Troubleshooting

| Issue | Cause | Solution |
|-------|-------|----------|
| `uvx: command not found` | uv not installed | Install with `pip install uv` or use Option B |
| `AccessDenied` error | Missing IAM permissions | Add aws-mcp:* permissions to IAM policy |
| `InvalidSignatureException` | Credential issue | Check `aws sts get-caller-identity` |
| Tools not appearing | MCP not started | Restart Claude Code after config change |
```

## File: `plugins/aws-agentic-ai/skills/aws-agentic-ai/SKILL.md`
```markdown
---
name: aws-agentic-ai
aliases:
  - bedrock-agentcore
description: AWS Bedrock AgentCore comprehensive expert for deploying and managing all AgentCore services. Use when working with Gateway, Runtime, Memory, Identity, or any AgentCore component. Covers MCP target deployment, credential management, schema optimization, runtime configuration, memory management, and identity services.
context: fork
model: sonnet
skills:
  - aws-mcp-setup
allowed-tools:
  - mcp__aws-mcp__*
  - mcp__awsdocs__*
  - Bash(aws bedrock-agentcore-control *)
  - Bash(aws bedrock-agentcore-runtime *)
  - Bash(aws bedrock *)
  - Bash(aws s3 cp *)
  - Bash(aws s3 ls *)
  - Bash(aws secretsmanager *)
  - Bash(aws sts get-caller-identity)
hooks:
  PreToolUse:
    - matcher: Bash(aws bedrock-agentcore-control create-*)
      command: aws sts get-caller-identity --query Account --output text
      once: true
---

# AWS Bedrock AgentCore

AWS Bedrock AgentCore provides a complete platform for deploying and scaling AI agents with seven core services. This skill guides you through service selection, deployment patterns, and integration workflows using AWS CLI.

## AWS Documentation Requirement

Always verify AWS facts using MCP tools (`mcp__aws-mcp__*` or `mcp__*awsdocs*__*`) before answering. The `aws-mcp-setup` dependency is auto-loaded — if MCP tools are unavailable, guide the user through that skill's setup flow.

## When to Use This Skill

Use this skill when you need to:
- Deploy REST APIs as MCP tools for AI agents (Gateway)
- Execute agents in serverless runtime (Runtime)
- Add conversation memory to agents (Memory)
- Manage API credentials and authentication (Identity)
- Enable agents to execute code securely (Code Interpreter)
- Allow agents to interact with websites (Browser)
- Monitor and trace agent performance (Observability)

## Available Services

| Service | Use For | Documentation |
|---------|---------|---------------|
| **Gateway** | Converting REST APIs to MCP tools | [`services/gateway/README.md`](../../../README.md) |
| **Runtime** | Deploying and scaling agents | [`services/runtime/README.md`](../../../README.md) |
| **Memory** | Managing conversation state | [`services/memory/README.md`](../../../README.md) |
| **Identity** | Credential and access management | [`services/identity/README.md`](../../../README.md) |
| **Code Interpreter** | Secure code execution in sandboxes | [`services/code-interpreter/README.md`](../../../README.md) |
| **Browser** | Web automation and scraping | [`services/browser/README.md`](../../../README.md) |
| **Observability** | Tracing and monitoring | [`services/observability/README.md`](../../../README.md) |

## Common Workflows

### Deploying a Gateway Target

**MANDATORY - READ DETAILED DOCUMENTATION**: See [`services/gateway/README.md`](../../../README.md) for complete Gateway setup guide including deployment strategies, troubleshooting, and IAM configuration.

**Quick Workflow**:
1. Upload OpenAPI schema to S3
2. *(API Key auth only)* Create credential provider and store API key
3. Create gateway target linking schema (and credentials if using API key)
4. Verify target status and test connectivity

> **Note**: Credential provider is only needed for API key authentication. Lambda targets use IAM roles, and MCP servers use OAuth.

### Managing Credentials

**MANDATORY - READ DETAILED DOCUMENTATION**: See [`cross-service/credential-management.md`](cross-service/credential-management.md) for unified credential management patterns across all services.

**Quick Workflow**:
1. Use Identity service credential providers for all API keys
2. Link providers to gateway targets via ARN references
3. Rotate credentials quarterly through credential provider updates
4. Monitor usage with CloudWatch metrics

### Monitoring Agents

**MANDATORY - READ DETAILED DOCUMENTATION**: See [`services/observability/README.md`](../../../README.md) for comprehensive monitoring setup.

**Quick Workflow**:
1. Enable observability for agents
2. Configure CloudWatch dashboards for metrics
3. Set up alarms for error rates and latency
4. Use X-Ray for distributed tracing

## Service-Specific Documentation

For detailed documentation on each AgentCore service, see the following resources:

### Gateway Service
- **Overview**: [`services/gateway/README.md`](../../../README.md)
- **Deployment Strategies**: [`services/gateway/deployment-strategies.md`](services/gateway/deployment-strategies.md)
- **Troubleshooting**: [`services/gateway/troubleshooting-guide.md`](../../../vault/archives/archive_legacy/claude-code-templates/cli-tool/components/commands/documentation/troubleshooting-guide.md)

### Runtime, Memory, Identity, Code Interpreter, Browser, Observability
Each service has comprehensive documentation in its respective directory:
- [`services/runtime/README.md`](../../../README.md)
- [`services/memory/README.md`](../../../README.md)
- [`services/identity/README.md`](../../../README.md)
- [`services/code-interpreter/README.md`](../../../README.md)
- [`services/browser/README.md`](../../../README.md)
- [`services/observability/README.md`](../../../README.md)

## Cross-Service Resources

For patterns and best practices that span multiple AgentCore services:

- **Credential Management**: [`cross-service/credential-management.md`](cross-service/credential-management.md) - Unified credential patterns, security practices, rotation procedures

## Additional Resources

- **AWS Documentation**: [Amazon Bedrock AgentCore](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html)
- **API Reference**: [Bedrock AgentCore Control Plane API](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/)
- **AWS CLI Reference**: [bedrock-agentcore-control commands](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/bedrock-agentcore-control/index.html)

```

## File: `plugins/aws-agentic-ai/skills/aws-agentic-ai/cross-service/credential-management.md`
```markdown
# Cross-Service Credential Management

**Applies to**: Gateway, Runtime, Memory, Identity

## Overview

Credential management is a cross-cutting concern across all AgentCore services. This guide provides unified patterns for managing API keys, tokens, and authentication credentials across the AgentCore platform.

## Authentication Overview

| Service | Direction | Supported Methods | Use Case |
|---------|-----------|-------------------|----------|
| **Gateway** | Inbound | IAM, JWT, No Auth | Who can invoke MCP tools |
| **Gateway** | Outbound | IAM, OAuth (2LO/3LO), API Key | Accessing external APIs |
| **Runtime** | Inbound | IAM (SigV4), JWT | Who can invoke agents |
| **Runtime** | Outbound | OAuth, API Key | Accessing third-party services |
| **Memory** | - | IAM Role | Data access permissions |
| **Identity** | - | AWS KMS | Secret encryption |

### Inbound Authorization (Who Can Access Your Services)

**Gateway Options** ([docs](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-inbound-auth.html)):
- **IAM Identity**: Uses AWS IAM credentials for authorization
- **JWT**: Tokens from identity providers (Cognito, Microsoft Entra ID, etc.)
- **No Authorization**: Open access - only for production with proper security controls

**Runtime Options** ([docs](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-oauth.html)):
- **IAM (SigV4)**: Default authentication (works automatically)
- **JWT Bearer Token**: Token-based auth with discovery URL and audience validation

> **Note**: A Runtime can only use one inbound auth type (IAM or JWT), not both simultaneously.

### Outbound Authorization (Accessing External Services)

**Gateway Options** ([docs](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-outbound-auth.html)):

| Target Type | IAM (Service Role) | OAuth 2LO | OAuth 3LO | API Key |
|-------------|-------------------|-----------|-----------|---------|
| Lambda function | ✅ | ❌ | ❌ | ❌ |
| API Gateway | ✅ | ❌ | ❌ | ✅ |
| OpenAPI schema | ❌ | ✅ | ✅ | ✅ |
| Smithy schema | ✅ | ✅ | ✅ | ❌ |
| MCP server | ❌ | ✅ | ❌ | ❌ |

- **OAuth 2LO**: Client credentials grant (machine-to-machine)
- **OAuth 3LO**: Authorization code grant (user-delegated access)

**Runtime Options**:
- **OAuth**: Tokens on behalf of users via Identity Service
- **API Key**: Key-based authentication via Identity Service

## Best Practices

### ✅ DO's

1. **Use Identity Service**: Always manage credentials through the Identity service
   ```bash
   # ✅ Correct - Use Identity API
   aws bedrock-agentcore-control create-api-key-credential-provider \
     --name MyCredentialProvider \
     --api-key "YOUR_API_KEY_VALUE"
   ```

2. **Separate by Environment**: Use different providers for different environments
   ```bash
   - dev-api-key-provider      # Development
   - staging-api-key-provider  # Staging
   - prod-api-key-provider     # Production
   ```

3. **Rotate Regularly**: Implement quarterly credential rotation
   ```bash
   aws bedrock-agentcore-control update-api-key-credential-provider \
     --name MyCredentialProvider \
     --api-key "NEW_API_KEY"
   ```

4. **Least Privilege**: Grant minimal required permissions to each credential
   ```bash
   # API key should only have necessary API permissions
   # IAM roles should have scoped-down policies
   ```

5. **Monitor Usage**: Track credential usage and set up alerts
   ```json
   {
     "CloudWatch Alarms": {
       "HighErrorRate": "Alert if > 10% failed requests",
       "UnusualActivity": "Alert on usage spikes"
     }
   }
   ```

### ❌ DON'Ts

1. **Never Hardcode**: Don't embed credentials in code or configuration files
   ```bash
   # ❌ Bad - Hardcoded API key
   const apiKey = "sk-1234567890abcdef"

   # ✅ Good - Reference credential provider
   const credentialProvider = "MyCredentialProvider"
   ```

2. **Don't Share Across Environments**: Avoid using production keys in development
   ```bash
   # ❌ Bad - Same key everywhere
   dev:  third-party-api-key: prod-key
   prod: third-party-api-key: prod-key

   # ✅ Good - Separate keys
   dev:  third-party-api-key: dev-key
   prod: third-party-api-key: prod-key
   ```

3. **Don't Commit to Git**: Exclude credential files from version control
   ```bash
   # .gitignore
   *.env
   *.secret
   credential-*.json
   ```

4. **Don't Use Long-Lived Tokens**: Implement token refresh for OAuth
   ```bash
   # OAuth tokens should auto-refresh
   # Don't use tokens with > 30 day expiration
   ```

## Multi-Service Credential Patterns

### Pattern 1: Centralized Identity, Distributed Usage

```
┌─────────────────────────────────────┐
│  Identity Service                   │
│  - Stores ALL credentials           │
│  - Manages rotation                 │
│  - Provides audit logs              │
└──────────┬──────────────────────────┘
           │
           ├────────────┬────────────┬────────────┐
           ▼            ▼            ▼            ▼
    ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐
    │ Gateway  │ │ Runtime  │ │  Memory  │ │  Other   │
    │  Uses    │ │  Uses    │ │  Uses    │ │  Uses    │
    └──────────┘ └──────────┘ └──────────┘ └──────────┘
```

**Benefits**:
- Single source of truth for all credentials
- Unified rotation and audit
- Consistent access patterns

**Setup**:
```bash
# 1. Create master credential in Identity
aws bedrock-agentcore-control create-api-key-credential-provider \
  --name MasterAPICredentials \
  --api-key "YOUR_MASTER_API_KEY"

# 2. Grant access to each service
# - Gateway: can read MasterAPICredentials
# - Runtime: can read MasterAPICredentials
# - Memory: can read MasterAPICredentials
```

### Pattern 2: Service-Specific Credentials

```
┌─────────────────────────────────────┐
│  Identity Service                   │
│  - Stores credentials per service   │
└──────────┬──────────────────────────┘
           │
    ┌──────┴──────┬────────┬─────────┐
    ▼             ▼        ▼         ▼
┌─────────┐ ┌─────────┐ ┌──────┐ ┌─────┐
│ Gateway │ │ Runtime │ │Memory││Other│
│  Cred   │ │  Cred   │ │ Cred ││Cred │
└─────────┘ └─────────┘ └──────┘ └─────┘
```

**Benefits**:
- Isolation between services
- Independent rotation per service
- Service-specific permissions

**Setup**:
```bash
# Create separate providers
aws bedrock-agentcore-control create-api-key-credential-provider \
  --name GatewayAPICredentials \
  --api-key "YOUR_GATEWAY_API_KEY"

aws bedrock-agentcore-control create-api-key-credential-provider \
  --name RuntimeCredentials \
  --api-key "YOUR_RUNTIME_API_KEY"
```

### Pattern 3: Tiered (Master + Service)

```
┌─────────────────────────────────────┐
│  Identity Service                   │
│  - Master credential                │
│  - Per-service credentials          │
└──────────┬──────────────────────────┘
           │
    ┌──────┴──────┐
    ▼             ▼
┌─────────┐ ┌─────────────┐
│ Master  │ │   Services  │
│  Cred   │ │   - Gateway │ │
└────┬────┘ │   - Runtime │
     │      │   - Memory  │
     └──────┤   (each has │
            │ own creds)  │
            └─────────────┘
```

**Use Cases**:
- Production: Master credential for critical APIs
- Development: Service-specific credentials for testing
- Emergency: Master credential as backup

## Security Best Practices

### Encryption

```bash
# Use KMS for secret encryption
aws secretsmanager create-secret \
  --name MySecret \
  --kms-key-id arn:aws:kms:us-west-2:123456789012:key/12345678-abcd-ef12-3456-7890abcdef12 \
  --secret-string "my-secret-value"
```

### Access Control

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "bedrock-agentcore:GetResourceApiKey"
      ],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "aws:PrincipalTag/Service": "gateway"
        }
      }
    }
  ]
}
```

### Audit Logging

```bash
# Enable CloudTrail for Bedrock AgentCore
aws cloudtrail create-trail \
  --name agentcore-audit \
  --s3-bucket-name agentcore-audit-logs \
  --include-global-service-events true
```

## Rotation Strategy

### Automated Rotation

```bash
# Enable automatic rotation (when supported)
aws secretsmanager rotate-secret \
  --secret-id MySecret \
  --lambda-arn arn:aws:lambda:us-west-2:123456789012:function:MyRotationFunction

# Rotation schedule (every 30 days)
aws secretsmanager rotate-secret \
  --secret-id MySecret \
  --rotation-rules AutomaticAfterDays=30
```

### Manual Rotation Process

```bash
#!/bin/bash
# rotate-credentials.sh

echo "Step 1: Generate new credential"
NEW_KEY=$(generate-new-api-key)

echo "Step 2: Update in Identity service"
aws bedrock-agentcore-control update-api-key-credential-provider \
  --name MyCredentialProvider \
  --api-key "$NEW_KEY"

echo "Step 3: Verify all services work"
./test-all-services.sh

echo "Step 4: Delete old credential"
# Old credential is automatically deprecated
```

## Common Patterns

### Pattern: Credential Fallback

```typescript
// Try primary credential, fallback to backup
async function callWithFallback(provider: string) {
  try {
    return await callAPI(provider);
  } catch (error) {
    if (error.code === 'InvalidAPICredentials') {
      // Fallback to backup provider
      return await callAPI(`${provider}-backup`);
    }
    throw error;
  }
}
```

### Pattern: Rate Limiting with Credential Pool

```typescript
// Rotate through multiple credentials to avoid rate limits
const credentialPool = [
  'cred-1',
  'cred-2',
  'cred-3'
];

let currentIndex = 0;

function getNextCredential(): string {
  const credential = credentialPool[currentIndex];
  currentIndex = (currentIndex + 1) % credentialPool.length;
  return credential;
}
```

## Troubleshooting Credential Issues

### Issue: "Credential not found"

**Diagnosis**:
```bash
# Check if provider exists
aws bedrock-agentcore-control get-api-key-credential-provider \
  --name MyCredentialProvider

# Check IAM permissions
aws iam simulate-principal-policy \
  --policy-source-arn arn:aws:iam::123456789012:role/MyRole \
  --action-names bedrock-agentcore:GetResourceApiKey \
  --resource-arns arn:aws:bedrock-agentcore:us-west-2:123456789012:*
```

**Solution**: Create provider or grant IAM permissions

---

### Issue: "Invalid credentials" after rotation

**Diagnosis**:
```bash
# Check secret value format
aws secretsmanager get-secret-value \
  --secret-id arn:aws:secretsmanager:us-west-2:123456789012:secret:MySecret

# Should be: {"apiKey": "valid-key"}
```

**Solution**: Use correct update API
```bash
aws bedrock-agentcore-control update-api-key-credential-provider \
  --name MyCredentialProvider \
  --api-key "VALID_KEY"
```

---

### Issue: Cross-service access denied

**Diagnosis**:
```bash
# Check which services can access the credential
aws bedrock-agentcore-control get-api-key-credential-provider \
  --name MyCredentialProvider

# Review service IAM policies
```

**Solution**: Add cross-service access policy
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "bedrock-agentcore:GetResourceApiKey",
      "Resource": "*",
      "Condition": {
        "ArnLike": {
          "aws:PrincipalArn": [
            "arn:aws:iam::*:role/*gateway*",
            "arn:aws:iam::*:role/*runtime*"
          ]
        }
      }
    }
  ]
}
```

## Cost Considerations

### Secrets Manager Costs

- **Per secret**: ~$0.40/month
- **Per 10,000 API calls**: ~$0.05
- **Cross-region replication**: Additional costs

**Optimization**:
- Share credentials across services when possible
- Use regional replication only when necessary
- Cache credential retrieval (respect security requirements)

### Identity Service Costs

- **Credential provider storage**: Included in Secrets Manager
- **API calls**: Same as Secrets Manager pricing
- **Cross-account access**: No additional cost

## References

- **[Identity Service](../../../README.md)**: Credential provider management
- **[Gateway Service](../../../README.md)**: Uses credentials for API authentication
- **AWS Secrets Manager**: [Pricing](https://aws.amazon.com/secrets-manager/pricing/)
- **AWS Documentation**: [Managing AWS Secrets Manager secrets](https://docs.aws.amazon.com/secretsmanager/latest/userguide/manage_create-basic-secret.html)

---

**Related Guides**:
- [Observability Service](../../../README.md)
- [AWS AgentCore Identity Documentation](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity.html)
```

## File: `plugins/aws-agentic-ai/skills/aws-agentic-ai/services/browser/README.md`
```markdown
# AgentCore Browser Service

> **Status**: ✅ Available

## Overview

Amazon Bedrock AgentCore Browser provides a fast, secure, cloud-based browser runtime enabling AI agents to interact with websites at scale without infrastructure management.

## Core Capabilities

### Cloud-Based Runtime
- **Fast Execution**: High-performance browser instances with minimal latency
- **Auto Scaling**: Automatic scaling based on demand without configuration
- **Zero Infrastructure**: No servers or containers to manage
- **Multi-Region**: Deploy browser instances across AWS regions globally

### Security and Compliance
- **Enterprise Security**: Industry-standard security controls and encryption
- **Isolated Sessions**: Each browsing session runs in complete isolation
- **Data Protection**: Secure data handling and privacy controls
- **Compliance Ready**: Meets enterprise compliance requirements (SOC, HIPAA, GDPR)

### Web Interaction Capabilities
- **Full Automation**: Complete browser automation capabilities
- **JavaScript Support**: Execute JavaScript in browser context
- **Form Interaction**: Fill forms, click buttons, navigate pages
- **Content Extraction**: Extract text, data, and media from pages
- **Session Management**: Handle cookies, local storage, and sessions
- **Screenshot Capture**: Take screenshots of pages and elements

### Observability
- **Execution Logging**: Comprehensive logs of browser actions
- **Performance Metrics**: Track page load times and operation latency
- **Error Tracking**: Detailed error capture and debugging information
- **Request Monitoring**: Monitor network requests and responses

## Use Cases

### Web Scraping and Data Extraction
Enable agents to:
- Extract data from websites at scale
- Scrape content from dynamic pages
- Collect structured data from multiple sources
- Monitor website changes over time

### Automated Testing and QA
Support scenarios like:
- Automated UI testing of web applications
- Regression testing for web features
- Cross-browser compatibility testing
- Performance testing and monitoring

### Form Filling and Workflow Automation
Allow agents to:
- Automate form submissions
- Complete multi-step workflows
- Handle authentication and logins
- Process batch operations on web interfaces

### Real-Time Monitoring
Enable agents to:
- Monitor website availability and uptime
- Track content changes and updates
- Verify website functionality
- Gather competitive intelligence

### Content Verification
Support tasks like:
- Validate web content accuracy
- Check link integrity
- Verify page rendering
- Test responsive designs

## Architecture

### Browser Execution Flow

```
Agent Request
    ↓
┌─────────────────────────────────────────┐
│  Browser Service API                    │
│  - Parse browser action request         │
│  - Validate parameters                  │
│  - Allocate browser instance            │
└─────────────────────────────────────────┘
    ↓
┌─────────────────────────────────────────┐
│  Browser Instance                       │
│  - Navigate to URL                      │
│  - Execute JavaScript                   │
│  - Interact with page elements          │
│  - Extract content and data             │
└─────────────────────────────────────────┘
    ↓
┌─────────────────────────────────────────┐
│  Result Processing                      │
│  - Package extracted data               │
│  - Capture screenshots (if requested)   │
│  - Log execution details                │
│  - Return results to agent              │
└─────────────────────────────────────────┘
```

### Security Architecture

1. **Session Isolation**: Each browser session runs in isolated environment
2. **Network Security**: Controlled outbound internet access
3. **Data Encryption**: All data encrypted in transit and at rest
4. **Resource Limits**: CPU, memory, and time limits per session
5. **Access Control**: IAM-based authentication and authorization

## Configuration

### Basic Browser Session

```bash
# Configure browser service for agent
aws bedrock-agentcore-control configure-browser \
  --agent-id <AGENT_ID> \
  --session-timeout 600 \
  --viewport-width 1920 \
  --viewport-height 1080 \
  --region <REGION>
```

### Advanced Configuration

```bash
# Set browser preferences and capabilities
aws bedrock-agentcore-control update-browser-config \
  --agent-id <AGENT_ID> \
  --browser-config '{
    "headless": true,
    "javascript": true,
    "images": true,
    "cookies": true,
    "userAgent": "CustomUserAgent/1.0",
    "timeout": 30000
  }' \
  --region <REGION>
```

## Browser Actions

### Navigation
```javascript
// Navigate to URL
{
  "action": "navigate",
  "url": "https://example.com"
}

// Go back
{
  "action": "goBack"
}

// Refresh page
{
  "action": "reload"
}
```

### Element Interaction
```javascript
// Click element
{
  "action": "click",
  "selector": "#submit-button"
}

// Fill input field
{
  "action": "type",
  "selector": "#username",
  "text": "user@example.com"
}

// Select option
{
  "action": "select",
  "selector": "#country",
  "value": "US"
}
```

### Content Extraction
```javascript
// Extract text
{
  "action": "getText",
  "selector": ".article-content"
}

// Get element attribute
{
  "action": "getAttribute",
  "selector": "img.logo",
  "attribute": "src"
}

// Evaluate JavaScript
{
  "action": "evaluate",
  "script": "return document.title;"
}
```

### Screenshots
```javascript
// Full page screenshot
{
  "action": "screenshot",
  "fullPage": true
}

// Element screenshot
{
  "action": "screenshot",
  "selector": "#chart-container"
}
```

## Best Practices

### Performance Optimization
- Use headless mode for non-visual operations
- Disable unnecessary resources (images, stylesheets)
- Set appropriate timeouts for page loads
- Reuse browser sessions when possible
- Implement exponential backoff for retries

### Reliability
- Handle network failures gracefully
- Implement proper error handling
- Use explicit waits for dynamic content
- Verify element existence before interaction
- Set reasonable timeout values

### Security
- Validate all URLs before navigation
- Sanitize extracted data
- Use secure credential storage
- Implement rate limiting
- Monitor for suspicious patterns

### Cost Optimization
- Close browser sessions when done
- Use session pooling for frequent operations
- Set appropriate resource limits
- Monitor usage patterns
- Implement caching where appropriate

## Integration Patterns

### With Memory Service
```
Browser ←→ Memory Service
- Store extracted data in memory
- Cache frequently accessed pages
- Share session state across agents
```

### With Identity Service
```
Browser ←→ Identity Service
- Authenticate browser sessions
- Access credentials for protected sites
- Manage authentication tokens
```

### With Code Interpreter
```
Browser ←→ Code Interpreter
- Process scraped data with code
- Transform extracted content
- Analyze website data
```

## Troubleshooting

### Common Issues

**Page Load Timeout**
- Symptom: Page takes too long to load
- Solution: Increase timeout or optimize target page

**Element Not Found**
- Symptom: Cannot locate page element
- Solution: Use explicit waits or verify selector

**JavaScript Errors**
- Symptom: Page JavaScript fails
- Solution: Check console logs, handle errors

**Session Terminated**
- Symptom: Browser session unexpectedly ends
- Solution: Check resource limits and session timeout

**Authentication Required**
- Symptom: Cannot access protected pages
- Solution: Configure credentials via Identity service

## Monitoring

### Key Metrics
- **Session Count**: Number of active browser sessions
- **Success Rate**: Percentage of successful operations
- **Page Load Time**: Average time to load pages
- **Error Rate**: Percentage of failed operations
- **Resource Usage**: CPU and memory utilization

### CloudWatch Integration
```bash
# Query browser metrics
aws cloudwatch get-metric-statistics \
  --namespace AWS/BedrockAgentCore/Browser \
  --metric-name SessionCount \
  --dimensions Name=AgentId,Value=<AGENT_ID> \
  --start-time <START> \
  --end-time <END> \
  --period 3600 \
  --statistics Average
```

### Logging
```bash
# View browser execution logs
aws logs tail /aws/bedrock-agentcore/browser/<AGENT_ID> \
  --follow \
  --format short
```

## Performance Considerations

### Optimization Techniques
1. **Disable Unnecessary Resources**: Turn off images/stylesheets when not needed
2. **Use Headless Mode**: Faster execution without rendering overhead
3. **Implement Caching**: Cache static resources and repeated queries
4. **Parallel Execution**: Run multiple browser sessions concurrently
5. **Smart Waiting**: Use explicit waits instead of fixed delays

### Scaling Patterns
- **Horizontal Scaling**: Launch multiple browser instances
- **Session Pooling**: Reuse browser sessions for efficiency
- **Request Queuing**: Queue browser operations during high load
- **Regional Distribution**: Distribute load across AWS regions

## Additional Resources

- **AWS Documentation**: [Bedrock AgentCore Browser](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/browser.html)
- **Best Practices**: [Browser Automation Guide](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/browser-best-practices.html)
- **API Reference**: [Browser API](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/)
- **Selector Reference**: [CSS Selectors](https://developer.mozilla.org/en-US/brain/knowledge/docs_legacy/Web/CSS/CSS_Selectors)

---

**Related Services**:
- [Runtime Service](../../../README.md) - Agent execution
- [Code Interpreter](../../../README.md) - Data processing
- [Memory Service](../../../README.md) - State management
- [Observability Service](../../../README.md) - Monitoring
```

## File: `plugins/aws-agentic-ai/skills/aws-agentic-ai/services/code-interpreter/README.md`
```markdown
# AgentCore Code Interpreter Service

> **Status**: ✅ Available

## Overview

Amazon Bedrock AgentCore Code Interpreter enables agents to securely execute code in isolated sandbox environments, supporting complex data analysis workflows and computational tasks.

## Core Capabilities

### Secure Execution
- **Isolated Sandboxes**: Each code execution runs in a completely isolated environment
- **No Cross-Contamination**: Sessions are independent with no shared state
- **Enterprise Security**: Meets enterprise security and compliance requirements
- **Resource Controls**: Configurable limits and timeout controls for execution

### Framework Integration
- **Popular Frameworks**: Seamless integration with LangGraph, CrewAI, Strands, and other agent frameworks
- **Multi-Language Support**: Execute code in Python, JavaScript, and other languages
- **Advanced Configuration**: Extensive customization options for runtime environments
- **Custom Runtimes**: Support for specialized runtime configurations

### Data Processing
- **File Operations**: Upload and download files for processing
- **Multi-Modal Data**: Handle structured and unstructured data
- **Result Formatting**: Format and visualize execution results
- **Error Handling**: Comprehensive error reporting and debugging support

## Use Cases

### Data Analysis and Transformation
Enable agents to:
- Process and analyze datasets
- Transform data formats
- Perform statistical calculations
- Generate data insights

### Complex Computational Workflows
Support scenarios like:
- Running scientific computations
- Executing business logic calculations
- Processing batch operations
- Performing iterative algorithms

### Visualization and Reporting
Allow agents to:
- Generate charts and graphs
- Create formatted reports
- Build visualizations from data
- Export results in various formats

### Dynamic Code Testing
Enable agents to:
- Test code snippets dynamically
- Validate logic and algorithms
- Debug code execution issues
- Prototype solutions quickly

## Architecture

### Execution Flow

```
Agent Request
    ↓
┌─────────────────────────────────────────┐
│  Code Interpreter Service               │
│  - Parse code execution request         │
│  - Validate code and parameters         │
│  - Allocate isolated sandbox            │
└─────────────────────────────────────────┘
    ↓
┌─────────────────────────────────────────┐
│  Sandbox Environment                    │
│  - Execute code in isolation            │
│  - Process data and files               │
│  - Generate outputs                     │
│  - Capture errors and logs              │
└─────────────────────────────────────────┘
    ↓
┌─────────────────────────────────────────┐
│  Result Processing                      │
│  - Format execution results             │
│  - Package outputs and artifacts        │
│  - Return to agent                      │
└─────────────────────────────────────────┘
```

### Security Model

1. **Sandbox Isolation**: Each execution runs in a completely isolated environment
2. **Resource Limits**: CPU, memory, and time limits prevent resource exhaustion
3. **Network Restrictions**: Controlled network access from sandbox environments
4. **Data Encryption**: Data at rest and in transit is encrypted
5. **Audit Logging**: All code executions are logged for compliance

## Configuration

### Basic Setup

```bash
# Configure code interpreter for agent
aws bedrock-agentcore-control configure-code-interpreter \
  --agent-id <AGENT_ID> \
  --execution-timeout 300 \
  --memory-limit 2048 \
  --region <REGION>
```

### Custom Runtime Configuration

```bash
# Set custom runtime environment
aws bedrock-agentcore-control update-code-interpreter-runtime \
  --agent-id <AGENT_ID> \
  --runtime-config '{
    "language": "python3.11",
    "packages": ["pandas", "numpy", "matplotlib"],
    "environment": {
      "CUSTOM_VAR": "value"
    }
  }' \
  --region <REGION>
```

## Best Practices

### Code Security
- Validate all code inputs before execution
- Implement input sanitization for user-provided code
- Use resource limits to prevent denial of service
- Monitor code execution patterns for anomalies

### Performance Optimization
- Cache common dependencies in runtime images
- Use appropriate timeout values for expected workload
- Optimize code for execution within timeout limits
- Batch similar operations when possible

### Error Handling
- Implement comprehensive error catching in code
- Provide clear error messages for debugging
- Log execution details for troubleshooting
- Use structured output formats for results

### Data Management
- Minimize data transfer in and out of sandboxes
- Use streaming for large data processing
- Clean up temporary files after execution
- Implement data validation before processing

## Integration Patterns

### With Memory Service
```
Code Interpreter ←→ Memory Service
- Store execution results in memory
- Retrieve past computation results
- Share data across agent sessions
```

### With Identity Service
```
Code Interpreter ←→ Identity Service
- Authenticate code execution requests
- Access credentials for external APIs
- Manage permissions for data access
```

### With Observability Service
```
Code Interpreter ←→ Observability Service
- Trace code execution workflows
- Monitor performance metrics
- Log execution events
- Alert on execution failures
```

## Troubleshooting

### Common Issues

**Execution Timeout**
- Symptom: Code execution exceeds timeout limit
- Solution: Increase timeout or optimize code performance

**Memory Limit Exceeded**
- Symptom: Code runs out of memory
- Solution: Increase memory limit or process data in chunks

**Package Import Errors**
- Symptom: Required packages not found
- Solution: Configure custom runtime with needed packages

**Permission Denied**
- Symptom: Cannot access required resources
- Solution: Configure IAM permissions for code interpreter

## Monitoring

### Key Metrics
- **Execution Count**: Number of code executions
- **Success Rate**: Percentage of successful executions
- **Average Duration**: Mean execution time
- **Error Rate**: Percentage of failed executions
- **Resource Utilization**: CPU and memory usage

### CloudWatch Integration
```bash
# Query execution metrics
aws cloudwatch get-metric-statistics \
  --namespace AWS/BedrockAgentCore/CodeInterpreter \
  --metric-name ExecutionCount \
  --dimensions Name=AgentId,Value=<AGENT_ID> \
  --start-time <START> \
  --end-time <END> \
  --period 3600 \
  --statistics Sum
```

## Additional Resources

- **AWS Documentation**: [Bedrock AgentCore Code Interpreter](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/code-interpreter.html)
- **Security Best Practices**: [Secure Code Execution](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/code-interpreter-security.html)
- **API Reference**: [Code Interpreter API](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/)

---

**Related Services**:
- [Runtime Service](../../../README.md) - Agent execution environment
- [Memory Service](../../../README.md) - State management
- [Observability Service](../../../README.md) - Monitoring and tracing
```

## File: `plugins/aws-agentic-ai/skills/aws-agentic-ai/services/gateway/deploy-template.sh`
```bash
#!/bin/bash
# AgentCore Gateway Multi-Environment Deployment Script
# Template for deploying targets to multiple gateways

set -euo pipefail

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Function to print colored output
print_info() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARN]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Check if environment file is provided
if [ $# -eq 0 ]; then
    print_error "Environment file not provided!"
    echo "Usage: $0 <environment-file>"
    echo "Example: $0 .env.production"
    exit 1
fi

ENV_FILE="$1"

# Check if environment file exists
if [ ! -f "$ENV_FILE" ]; then
    print_error "Environment file not found: $ENV_FILE"
    exit 1
fi

print_info "Loading environment from: $ENV_FILE"

# Load environment variables safely (skip comments and blank lines, validate keys)
while IFS='=' read -r key value; do
    # Skip comments and blank lines
    [[ -z "$key" || "$key" =~ ^[[:space:]]*# ]] && continue
    # Strip leading/trailing whitespace
    key="$(echo "$key" | xargs)"
    value="$(echo "$value" | xargs)"
    # Validate key is a safe variable name
    if [[ ! "$key" =~ ^[a-zA-Z_][a-zA-Z0-9_]*$ ]]; then
        print_warning "Skipping invalid variable name: $key"
        continue
    fi
    export "$key=$value"
done < "$ENV_FILE"

# Validate required environment variables
REQUIRED_VARS=("GATEWAY_IDENTIFIER" "CREDENTIAL_PROVIDER_NAME" "AWS_REGION")
for var in "${REQUIRED_VARS[@]}"; do
    if [ -z "${!var}" ]; then
        print_error "Required environment variable not set: $var"
        exit 1
    fi
done

# Validate identifiers contain only safe characters
for var in GATEWAY_IDENTIFIER CREDENTIAL_PROVIDER_NAME AWS_REGION; do
    if [[ ! "${!var}" =~ ^[a-zA-Z0-9._:/-]+$ ]]; then
        print_error "Invalid characters in $var: ${!var}"
        exit 1
    fi
done

# Get AWS account ID
print_info "Getting AWS account ID..."
CDK_DEFAULT_ACCOUNT="$(aws sts get-caller-identity \
  --query Account --output text \
  --profile "${AWS_PROFILE:-default}")"
export CDK_DEFAULT_ACCOUNT

if [ -z "$CDK_DEFAULT_ACCOUNT" ]; then
    print_error "Failed to get AWS account ID"
    exit 1
fi

print_info "Account ID: $CDK_DEFAULT_ACCOUNT"
print_info "Gateway: $GATEWAY_IDENTIFIER"
print_info "Credential Provider: $CREDENTIAL_PROVIDER_NAME"
print_info "Region: $AWS_REGION"

# Extract gateway name from identifier if not provided
if [ -z "${GATEWAY_NAME:-}" ]; then
    # Extract prefix before first hyphen
    GATEWAY_NAME="$(echo "$GATEWAY_IDENTIFIER" | cut -d'-' -f1)"
    export GATEWAY_NAME
    print_info "Auto-extracted gateway name: $GATEWAY_NAME"
fi

# Build project
print_info "Building project..."
if ! npm run build; then
    print_error "Build failed!"
    exit 1
fi

print_info "Build successful!"

# Deploy to AWS
print_info "Deploying to AWS..."
if cdk deploy --profile "${AWS_PROFILE:-default}" --require-approval never; then
    print_info "Deployment successful!"

    # Display deployment information
    echo ""
    print_info "Deployment Details:"
    echo "  Gateway ID: $GATEWAY_IDENTIFIER"
    echo "  Stack Name: ${GATEWAY_NAME}FootballAPITarget"
    echo "  Region: $AWS_REGION"
    echo "  Credential Provider: $CREDENTIAL_PROVIDER_NAME"
    echo ""

    # Get and display target information
    print_info "Fetching target details..."
    aws bedrock-agentcore-control list-gateway-targets \
      --gateway-identifier "$GATEWAY_IDENTIFIER" \
      --profile "${AWS_PROFILE:-default}" \
      --region "$AWS_REGION"

else
    print_error "Deployment failed!"
    exit 1
fi
```

## File: `plugins/aws-agentic-ai/skills/aws-agentic-ai/services/gateway/deployment-strategies.md`
```markdown
# AgentCore Gateway Deployment Strategies

## Overview

This reference guide covers different deployment strategies for AWS Bedrock AgentCore Gateway targets, including credential management approaches, multi-environment patterns, and rollback procedures.

## Credential Provider Strategies

### Strategy 1: Shared Provider (Recommended for Most Cases)

**Concept**: Create ONE credential provider and share across all gateway targets

**Setup**:
```bash
# Create shared provider with API key (run once)
aws bedrock-agentcore-control create-api-key-credential-provider \
  --name SharedAPICredentialProvider \
  --api-key "YOUR_API_KEY" \
  --profile default --region us-west-2
```

**Environment Configuration**:
```bash
# .env.gateway-a
GATEWAY_IDENTIFIER=gateway-a-abc123xyz
CREDENTIAL_PROVIDER_NAME=SharedAPICredentialProvider  # Same for all

# .env.gateway-b
GATEWAY_IDENTIFIER=gateway-b-def456uvw
CREDENTIAL_PROVIDER_NAME=SharedAPICredentialProvider  # Same for all
```

**Benefits**:
- ✅ Simplified key management - single key to rotate
- ✅ Reduced operational overhead
- ✅ Consistent authentication across all gateways
- ✅ Easier compliance and auditing

**Use Cases**:
- Same API, multiple gateway deployments
- Development/Testing/Production gateways
- Regional deployments (us-west-2, eu-west-1)

**Trade-offs**:
- Less isolation between gateways (all or nothing key rotation)

### Strategy 2: Isolated Provider (Per-Gateway)

**Concept**: Create UNIQUE credential provider for each gateway

**Setup**:
```bash
# Create provider for Gateway A
aws bedrock-agentcore-control create-api-key-credential-provider \
  --name GatewayAAPICredentialProvider \
  --api-key "API_KEY_A" \
  --profile default --region us-west-2

# Create provider for Gateway B
aws bedrock-agentcore-control create-api-key-credential-provider \
  --name GatewayBAPICredentialProvider \
  --api-key "API_KEY_B" \
  --profile default --region us-west-2
```

**Environment Configuration**:
```bash
# .env.gateway-a
GATEWAY_IDENTIFIER=gateway-a-abc123xyz
CREDENTIAL_PROVIDER_NAME=GatewayAAPICredentialProvider  # Unique

# .env.gateway-b
GATEWAY_IDENTIFIER=gateway-b-def456uvw
CREDENTIAL_PROVIDER_NAME=GatewayBAPICredentialProvider  # Unique
```

**Benefits**:
- ✅ Complete isolation between gateways
- ✅ Independent key rotation per environment
- ✅ Different API keys for different use cases
- ✅ Better security boundaries

**Use Cases**:
- Production vs Development with different API keys
- Different APIs for different gateways
- Compliance requiring environment separation
- Testing new API versions in isolation

**Trade-offs**:
- More complex key management
- Multiple keys to rotate and maintain

### Strategy 3: Tiered (Shared + Isolated)

**Concept**: Hybrid approach with shared provider for non-prod, isolated for production

**Setup**:
```bash
# Shared provider for dev/test
aws bedrock-agentcore-control create-api-key-credential-provider \
  --name DevTestAPICredentialProvider \
  --api-key "DEV_TEST_API_KEY" \
  --profile default --region us-west-2

# Isolated provider for production
aws bedrock-agentcore-control create-api-key-credential-provider \
  --name ProdAPICredentialProvider \
  --api-key "PROD_API_KEY" \
  --profile default --region us-west-2
```

**Environment Configuration**:
```bash
# .env.development
GATEWAY_IDENTIFIER=dev-gateway-abc123xyz
CREDENTIAL_PROVIDER_NAME=DevTestAPICredentialProvider

# .env.staging
GATEWAY_IDENTIFIER=staging-gateway-def456uvw
CREDENTIAL_PROVIDER_NAME=DevTestAPICredentialProvider

# .env.production
GATEWAY_IDENTIFIER=prod-gateway-ghi789rst
CREDENTIAL_PROVIDER_NAME=ProdAPICredentialProvider
```

**Benefits**:
- ✅ Balance of simplicity and security
- ✅ Production isolation with dev/test convenience
- ✅ Easier testing in non-prod environments
- ✅ Production key remains protected

**Use Cases**:
- Most common enterprise pattern
- Clear separation between environments
- Controlled production access

## Multi-Account Deployment

When deploying across multiple AWS accounts:

### Setup

1. **Credential Provider per Account**:
   ```bash
   # Account 1 (Dev)
   aws bedrock-agentcore-control create-api-key-credential-provider \
     --name APICredentialProvider \
     --api-key "DEV_API_KEY" \
     --profile dev-account

   # Account 2 (Prod)
   aws bedrock-agentcore-control create-api-key-credential-provider \
     --name APICredentialProvider \
     --api-key "PROD_API_KEY" \
     --profile prod-account
   ```

2. **Centralized Configuration**:
   ```bash
   # .env.dev
   ACCOUNT_ID=123456789012
   GATEWAY_IDENTIFIER=dev-gateway-abc123xyz
   AWS_PROFILE=dev-account

   # .env.prod
   ACCOUNT_ID=987654321098
   GATEWAY_IDENTIFIER=prod-gateway-abc123xyz
   AWS_PROFILE=prod-account
   ```

3. **Cross-Account Deployment Script**:
   ```bash
   #!/bin/bash
   ENV_FILE=$1

   # Load environment
   export $(cat $ENV_FILE | xargs)

   # Get AWS account ID
   export CDK_DEFAULT_ACCOUNT=$(aws sts get-caller-identity \
     --profile $AWS_PROFILE \
     --query Account --output text)

   # Deploy
   npm run build && cdk deploy --profile $AWS_PROFILE --require-approval never
   ```

## Key Rotation Procedures

### Shared Provider Strategy

**Manual Rotation**:
```bash
# 1. Update key in provider
aws bedrock-agentcore-control update-api-key-credential-provider \
  --name SharedAPICredentialProvider \
  --api-key "NEW_API_KEY" \
  --profile default --region us-west-2

# 2. Restart gateway targets (if needed) to pick up new key
```

**Automated Rotation**:
- Use AWS Secrets Manager rotation (if supported by credential provider)
- Triggered by CloudWatch Events schedule
- Lambda function handles key generation/update

### Isolated Provider Strategy

**Per-Gateway Rotation**:
```bash
# Rotate dev environment only
aws bedrock-agentcore-control update-api-key-credential-provider \
  --name DevAPICredentialProvider \
  --api-key "NEW_DEV_KEY"

# Production remains unchanged
aws bedrock-agentcore-control update-api-key-credential-provider \
  --name ProdAPICredentialProvider \
  --api-key "EXISTING_PROD_KEY"
```

## Rollback Procedures

### Rollback Failed Deployment

```bash
# List CloudFormation stacks
aws cloudformation list-stacks --stack-status-filter UPDATE_ROLLBACK_FAILED

# Get previous stack configuration
aws cloudformation describe-stack-resources --stack-name StackName

# Rollback to previous version
aws cloudformation continue-update-rollback --stack-name StackName
```

### Rollback Credential Changes

```bash
# If new API key is causing issues, restore previous key
aws bedrock-agentcore-control update-api-key-credential-provider \
  --name APICredentialProvider \
  --api-key "PREVIOUS_WORKING_KEY"
```

## Monitoring and Alerting

### CloudWatch Metrics to Monitor

- **Gateway Target Status**: Monitor target health
- **API Request Count**: Track usage per gateway
- **Error Rates**: 4xx and 5xx errors
- **Latency**: P95, P99 response times
- **Credential Provider Errors**: Secret access failures

### CloudWatch Alarms

```typescript
// CDK Example: Create alarm for high error rate
new cloudwatch.Alarm(this, 'HighErrorRate', {
  metric: new cloudwatch.Metric({
    namespace: 'AWS/BedrockAgentCore',
    metricName: 'TargetErrorRate',
    dimensionsMap: {
      GatewayId: gatewayId,
      TargetId: targetId,
    },
    statistic: 'avg',
    period: Duration.minutes(5),
  }),
  threshold: 10,
  evaluationPeriods: 2,
  datapointsToAlarm: 2,
  comparisonOperator: cloudwatch.ComparisonOperator.GREATER_THAN_THRESHOLD,
  alarmDescription: 'Error rate exceeds 10%',
  actionsEnabled: true,
});
```

## Cost Optimization

### Cost Considerations

1. **AgentCore Gateway**: Pay per tool invocation
   - Optimize schema to reduce unnecessary API calls
   - Cache frequently accessed data in schema descriptions
   - Use batch operations where available

2. **S3 Asset Storage**: Negligible (<$0.01/month)
   - Schema files are small
   - CDK automatically cleans up old versions

3. **Lambda (GatewayRoleUpdater)**: ~$0.01 per deployment
   - Covered by AWS Lambda free tier (1M requests/month)
   - Only runs during deployment/update

4. **Secrets Manager**: ~$0.40/month per secret
   - Use shared provider to minimize secret count
   - Rotate secrets on schedule to maintain security

5. **API Calls (RapidAPI Example)**:
   - Free tier: 100 requests/day
   - Paid tiers: From $10/month
   - Optimize by embedding IDs in schema

### Optimization Strategies

**Schema Optimization**:
```yaml
# Embed common IDs to reduce API calls by 50%
info:
  description: |
    COMMON LEAGUE IDs:
    - Premier League: 39
    - Champions League: 2
    - World Cup: 1
```

**Credential Provider Sharing**:
- Single provider for all gateways = 1 secret = $0.40/month
- Separate providers = N secrets = $0.40N/month

## Security Best Practices

### Credential Management
- Never commit API keys to source control
- Use AWS Secrets Manager via credential providers
- Rotate keys regularly (quarterly minimum)
- Use different keys for different environments

### IAM Permissions
- Custom Resource Lambda has scoped permissions
- Only allows access to Gateway service roles
- Follows principle of least privilege
- Audit policy versions regularly

### Network Security
- Ensure Gateway is in VPC if required
- Use AWS PrivateLink for on-premises integrations
- Enable encryption in transit (TLS 1.2+)
- Verify API endpoints use HTTPS

## Common Patterns

### Pattern 1: Development Pipeline

```bash
# Branch-based deployment
if [ "$BRANCH" = "main" ]; then
  ./deploy.sh .env.production
elif [ "$BRANCH" = "develop" ]; then
  ./deploy.sh .env.staging
else
  ./deploy.sh .env.development
fi
```

### Pattern 2: Regional Deployment

```bash
# Deploy to multiple regions
for region in us-west-2 eu-west-1 ap-southeast-1; do
  export AWS_REGION=$region
  export GATEWAY_IDENTIFIER="my-gateway-${region}"
  npm run build && cdk deploy --require-approval never
done
```

### Pattern 3: Blue-Green Deployment

```bash
# Deploy to blue environment
./deploy.sh .env.blue

# Test blue environment
./test-target.sh blue

# Switch to green if blue is healthy
./deploy.sh .env.green
```

## Migration Strategies

### Migrating from Manual to CDK Management

1. **Discovery Phase**:
   ```bash
   # Document existing targets
   aws bedrock-agentcore-control list-gateway-targets \
     --gateway-identifier existing-gateway \
     --profile default --region us-west-2
   ```

2. **Schema Extraction**:
   - Export existing OpenAPI schemas
   - Audit and optimize schema descriptions
   - Embed common IDs for performance

3. **CDK Implementation**:
   - Create stack with existing target configuration
   - Import existing credential provider
   - Add GatewayRoleUpdater for IAM automation

4. **Cutover**:
   - Deploy to new gateway first (test)
   - Update AI agents to use new target
   - Decommission old target after verification

## Additional References

- **Main Skill Documentation**: [`../../SKILL.md`](../../../.claude/skills/supabase-postgres-best-practices/SKILL.md)
- **Troubleshooting Guide**: [`./troubleshooting-guide.md`](../../../vault/archives/archive_legacy/claude-code-templates/cli-tool/components/commands/documentation/troubleshooting-guide.md)
- **Deployment Template Script**: [`./deploy-template.sh`](./deploy-template.sh)
- **Credential Management**: [`../../cross-service/credential-management.md`](../../cross-service/credential-management.md)
```

## File: `plugins/aws-agentic-ai/skills/aws-agentic-ai/services/gateway/README.md`
```markdown
# Gateway Service

The Gateway service converts REST APIs into MCP tools that AI agents can use. It handles authentication, schema validation, and request routing.

## Quick Start

### Prerequisites
- AWS CLI configured with appropriate permissions
- An existing Gateway (created via AWS Console or CLI)
- OpenAPI schema for your target API

### Deploy a Gateway Target

**Step 1: Upload OpenAPI schema to S3**
```bash
aws s3 cp my-api-openapi.yaml s3://<BUCKET_NAME>/schemas/
```

**Step 2: Create credential provider (API Key auth only)**
```bash
aws bedrock-agentcore-control create-api-key-credential-provider \
  --name MyAPICredentialProvider \
  --api-key "YOUR_API_KEY" \
  --region us-west-2
```

**Step 3: Create gateway target**
```bash
aws bedrock-agentcore-control create-gateway-target \
  --gateway-identifier <GATEWAY_ID> \
  --name MyAPITarget \
  --endpoint-configuration '{"openApiSchema": {"s3": {"uri": "s3://<BUCKET_NAME>/schemas/my-api-openapi.yaml"}}}' \
  --credential-provider-configurations '[{"credentialProviderType": "GATEWAY_API_KEY_CREDENTIAL_PROVIDER", "apiKeyCredentialProvider": {"providerArn": "arn:aws:bedrock-agentcore:us-west-2:<ACCOUNT_ID>:api-key-credential-provider/MyAPICredentialProvider"}}]' \
  --region us-west-2
```

**Step 4: Verify deployment**
```bash
aws bedrock-agentcore-control get-gateway-target \
  --gateway-identifier <GATEWAY_ID> \
  --target-identifier <TARGET_ID> \
  --region us-west-2
```

## Authentication Options

### Outbound (Accessing External APIs)

| Target Type | IAM | OAuth 2LO | OAuth 3LO | API Key |
|-------------|-----|-----------|-----------|---------|
| Lambda function | Yes | No | No | No |
| API Gateway | Yes | No | No | Yes |
| OpenAPI schema | No | Yes | Yes | Yes |
| Smithy schema | Yes | Yes | Yes | No |
| MCP server | No | Yes | No | No |

### Inbound (Who Can Invoke Tools)
- **IAM**: AWS IAM credentials
- **JWT**: Tokens from identity providers (Cognito, Entra ID)
- **No Auth**: Open access (use with caution)

## Documentation

| Document | Description |
|----------|-------------|
| [Deployment Strategies](deployment-strategies.md) | Credential provider patterns, multi-environment setup, key rotation |
| [Troubleshooting Guide](../../../vault/archives/archive_legacy/claude-code-templates/cli-tool/components/commands/documentation/troubleshooting-guide.md) | Common errors, diagnosis steps, solutions |
| [Deploy Template Script](deploy-template.sh) | Automated deployment script |
| [Validate Deployment Script](validate-deployment.sh) | Post-deployment verification |

## Common Operations

### List Gateway Targets
```bash
aws bedrock-agentcore-control list-gateway-targets \
  --gateway-identifier <GATEWAY_ID> \
  --region us-west-2
```

### Update Credential Provider
```bash
aws bedrock-agentcore-control update-api-key-credential-provider \
  --name MyAPICredentialProvider \
  --api-key "NEW_API_KEY" \
  --region us-west-2
```

### Delete Gateway Target
```bash
aws bedrock-agentcore-control delete-gateway-target \
  --gateway-identifier <GATEWAY_ID> \
  --target-identifier <TARGET_ID> \
  --region us-west-2
```

## Related Resources

- [Cross-Service Credential Management](../../cross-service/credential-management.md)
- [AWS Gateway Documentation](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html)
- [Bedrock AgentCore CLI Reference](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/bedrock-agentcore-control/index.html)
```

## File: `plugins/aws-agentic-ai/skills/aws-agentic-ai/services/gateway/troubleshooting-guide.md`
```markdown
# AgentCore Gateway Troubleshooting Guide

## Quick Diagnosis

### Symptom: Target Creation Fails

**Error Message**: `"Gateway target creation failed"`

**Diagnosis Steps**:
1. Verify gateway exists
   ```bash
   aws bedrock-agentcore-control get-gateway \
     --gateway-identifier <GATEWAY_ID> \
     --profile default --region us-west-2
   ```

2. Check credential provider exists (if using API key auth)
   ```bash
   aws bedrock-agentcore-control get-api-key-credential-provider \
     --name <PROVIDER_NAME> \
     --profile default --region us-west-2
   ```

3. List existing targets
   ```bash
   aws bedrock-agentcore-control list-gateway-targets \
     --gateway-identifier <GATEWAY_ID> \
     --profile default --region us-west-2
   ```

**Common Causes**:
- Gateway ID incorrect or gateway doesn't exist
- Credential provider name misspelled (for API key auth)
- OpenAPI schema syntax error
- S3 bucket permissions issue for schema

---

## Permission Errors

### Error: "User is not authorized to perform: bedrock-agentcore:GetResourceApiKey"

**Full Error**:
```
User: arn:aws:sts::<ACCOUNT_ID>:assumed-role/GatewayServiceRole is not
authorized to perform: bedrock-agentcore:GetResourceApiKey on resource: *
```

**Root Cause**: Gateway service role missing credential provider access permissions

**Diagnosis**:
```bash
# Get gateway role ARN
GATEWAY_ROLE=$(aws bedrock-agentcore-control get-gateway \
  --gateway-identifier <GATEWAY_ID> \
  --query 'roleArn' --output text \
  --profile default --region us-west-2)

echo $GATEWAY_ROLE

# Extract role name
ROLE_NAME=$(echo $GATEWAY_ROLE | cut -d'/' -f2)

# Check attached policies
aws iam list-attached-role-policies \
  --role-name $ROLE_NAME \
  --profile default --region us-west-2
```

**Solution**: Add required permissions to gateway role:
```bash
cat > /tmp/gateway-policy.json <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "GetResourceApiKey",
      "Effect": "Allow",
      "Action": ["bedrock-agentcore:GetResourceApiKey"],
      "Resource": "*"
    },
    {
      "Sid": "GetWorkloadAccessToken",
      "Effect": "Allow",
      "Action": ["bedrock-agentcore:GetWorkloadAccessToken"],
      "Resource": "*"
    },
    {
      "Sid": "GetCredentials",
      "Effect": "Allow",
      "Action": ["secretsmanager:GetSecretValue"],
      "Resource": ["arn:aws:secretsmanager:us-west-2:<ACCOUNT_ID>:secret:bedrock-agentcore-identity!*"]
    }
  ]
}
EOF

# Get policy ARN from role
POLICY_ARN=$(aws iam list-attached-role-policies \
  --role-name $ROLE_NAME \
  --query 'AttachedPolicies[0].PolicyArn' \
  --output text \
  --profile default --region us-west-2)

# Create new policy version
aws iam create-policy-version \
  --policy-arn $POLICY_ARN \
  --policy-document file:///tmp/gateway-policy.json \
  --set-as-default \
  --profile default --region us-west-2
```

---

### Error: "AccessDeniedException: Secrets Manager"

**Full Error**:
```
AccessDeniedException: User: arn:aws:sts::<ACCOUNT_ID>:assumed-role/GatewayServiceRole
is not authorized to perform: secretsmanager:GetSecretValue on resource: ...
```

**Root Cause**: Gateway cannot access Secrets Manager for credential provider

**Solution**: Add `secretsmanager:GetSecretValue` permission to gateway role (see above)

---

## Credential Provider Issues

### Error: "Credential provider not found"

**Diagnosis**:
```bash
# Check if provider exists
aws bedrock-agentcore-control get-api-key-credential-provider \
  --name <PROVIDER_NAME> \
  --profile default --region us-west-2

# List all providers
aws bedrock-agentcore-control list-api-key-credential-providers \
  --profile default --region us-west-2
```

**Solution**:
```bash
# Create provider if missing
aws bedrock-agentcore-control create-api-key-credential-provider \
  --name <PROVIDER_NAME> \
  --api-key "YOUR_API_KEY" \
  --profile default --region us-west-2
```

---

### Error: "Invalid API key"

**Symptom**: API calls return 403 or authentication errors

**Diagnosis**:
```bash
# Check API key format in secret
SECRET=$(aws secretsmanager get-secret-value \
  --secret-id "arn:aws:secretsmanager:us-west-2:<ACCOUNT_ID>:secret:bedrock-agentcore-identity/default/apikeycredentialprovider/<PROVIDER_NAME>-AbCdEf" \
  --query 'SecretString' --output text \
  --profile default --region us-west-2)

echo $SECRET | jq '.'
# Should be: {"apiKey": "your-key-here"}
```

**Solution**:
```bash
# Use the correct update command (not secretsmanager put-secret-value)
aws bedrock-agentcore-control update-api-key-credential-provider \
  --name <PROVIDER_NAME> \
  --api-key "YOUR_VALID_API_KEY" \
  --profile default --region us-west-2
```

**Common Mistake**: Using `secretsmanager put-secret-value` directly bypasses credential provider validation

---

## OpenAPI Schema Issues

### Error: "Invalid OpenAPI schema"

**Diagnosis**:
```bash
# Validate OpenAPI schema locally
npm install -g @apidevtools/swagger-cli
swagger-cli validate schemas/my-api-openapi.yaml

# Check for unsupported constructs
grep -n "oneOf\|anyOf\|allOf" schemas/my-api-openapi.yaml
# These constructs are not supported in Gateway
```

**Common Issues**:
1. **oneOf/anyOf/allOf**: Not supported, use simple types
2. **Missing operationId**: All operations must have operationId
3. **Invalid $ref references**: Must point to valid components
4. **YAML syntax errors**: Use online YAML validator

**Solution**: Use OpenAPI 3.0 simple types only:
```yaml
# ❌ Bad - unsupported
schema:
  oneOf:
    - type: string
    - type: number

# ✅ Good - simple type
schema:
  type: string
```

---

### Error: "Schema size exceeds limit"

**Root Cause**: OpenAPI schema too large for Gateway

**Solutions**:
1. Remove unused endpoints from schema
2. Simplify descriptions (keep essential info only)
3. Remove redundant component definitions
4. Split into multiple targets if necessary

---

## API Call Issues

### Error: "Rate limit exceeded"

**Symptom**: API calls return 429 Too Many Requests

**Root Cause**: Gateway or upstream API rate limits

**Diagnosis**:
```bash
# Check gateway target status
aws bedrock-agentcore-control get-gateway-target \
  --gateway-identifier <GATEWAY_ID> \
  --target-identifier <TARGET_ID> \
  --profile default --region us-west-2
```

**Solutions**:
1. **Check Gateway limits**: Verify gateway quota in AWS Console
2. **Upstream API limits**: Check your API provider dashboard for limits
3. **Optimize calls**: Use embedded IDs in schema to reduce API queries
4. **Implement caching**: Cache responses when possible
5. **Request limit increase**: Contact AWS support if needed

---

### Error: "Invalid API host header"

**Root Cause**: API endpoint or host header configuration mismatch

**Diagnosis**:
```bash
# Check schema for correct server URL
grep -A5 "servers:" schemas/my-api-openapi.yaml

# Verify host header in security scheme
grep -A10 "securitySchemes:" schemas/my-api-openapi.yaml
```

**Solution**: Update OpenAPI schema with correct server URL and host header

---

### Error: "Connection timeout"

**Symptom**: Gateway target calls fail with timeout errors

**Root Cause**: Upstream API not responding within timeout limit

**Solutions**:
1. Verify upstream API is accessible
2. Check network connectivity from Gateway
3. Increase timeout in target configuration (if supported)
4. Check if upstream API requires VPC configuration

---

## Target Status Issues

### Target Status: "FAILED"

**Diagnosis**:
```bash
# Get target details including status reason
aws bedrock-agentcore-control get-gateway-target \
  --gateway-identifier <GATEWAY_ID> \
  --target-identifier <TARGET_ID> \
  --query '{status: status, statusReason: statusReason}' \
  --profile default --region us-west-2
```

**Common Status Reasons**:
- `SCHEMA_VALIDATION_FAILED`: OpenAPI schema has errors
- `CREDENTIAL_PROVIDER_NOT_FOUND`: API key provider doesn't exist
- `PERMISSION_DENIED`: IAM permissions missing

---

### Target Status: "PENDING" for too long

**Root Cause**: Target creation stuck

**Solutions**:
1. Check if all dependencies exist (gateway, credential provider)
2. Delete and recreate target
3. Check AWS service health dashboard

---

## Testing and Verification

### How to Test Target Deployment

```bash
#!/bin/bash
# test-target.sh

GATEWAY_ID=$1
TARGET_ID=$2

# Test 1: List targets
echo "Listing gateway targets..."
aws bedrock-agentcore-control list-gateway-targets \
  --gateway-identifier $GATEWAY_ID \
  --profile default --region us-west-2

# Test 2: Get target details
echo "Getting target details..."
aws bedrock-agentcore-control get-gateway-target \
  --gateway-identifier $GATEWAY_ID \
  --target-identifier $TARGET_ID \
  --profile default --region us-west-2

# Test 3: Get tools from target
echo "Getting tools..."
aws bedrock-agentcore-control get-gateway-target \
  --gateway-identifier $GATEWAY_ID \
  --target-identifier $TARGET_ID \
  --query 'tools' \
  --profile default --region us-west-2
```

---

## Common Error Summary Table

| Error | Likely Cause | Solution |
|-------|-------------|----------|
| "not authorized to perform: bedrock-agentcore:GetResourceApiKey" | Missing IAM permissions | Add permissions to gateway role |
| "Credential provider not found" | Provider doesn't exist or name typo | Create provider with `create-api-key-credential-provider` |
| "Invalid API key" | Key format wrong or key invalid | Use `update-api-key-credential-provider` to update |
| "Invalid OpenAPI schema" | Unsupported constructs (oneOf/anyOf/allOf) | Remove unsupported constructs, use simple types |
| "Invalid API host header" | Host header doesn't match endpoint | Update OpenAPI schema with correct host |
| "Rate limit exceeded" | Too many API calls | Check limits, implement caching |
| "Connection timeout" | Upstream API not responding | Verify API accessibility |
| "Target status FAILED" | Schema or credential issues | Check statusReason in get-gateway-target |

---

## Escalation Path

If issues persist after troubleshooting:

1. **Check AWS Documentation**: https://docs.aws.amazon.com/bedrock-agentcore/
2. **AWS Support**: Open case with Bedrock AgentCore service
3. **Community**: AWS Developer Forums

**Information to gather for AWS Support**:
- Gateway ID and target ID
- Error messages and timestamps
- OpenAPI schema (sanitized)
- IAM role and policy configuration
```

## File: `plugins/aws-agentic-ai/skills/aws-agentic-ai/services/gateway/validate-deployment.sh`
```bash
#!/bin/bash
# AgentCore Gateway Target Validation Script
# Validates gateway target deployment and functionality

set -euo pipefail

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Configuration
AWS_REGION="${AWS_REGION:-us-west-2}"
AWS_PROFILE="${AWS_PROFILE:-default}"

# Function to print colored output
print_info() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARN]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

print_section() {
    echo ""
    echo -e "${BLUE}==== $1 ====${NC}"
}

# Check if gateway ID is provided
if [ $# -eq 0 ]; then
    print_error "Gateway ID not provided!"
    echo "Usage: $0 <gateway-identifier>"
    echo "Example: $0 xiaozhi-mfyvjzuqpk"
    exit 1
fi

GATEWAY_ID="$1"

# Validate gateway ID contains only safe characters
if [[ ! "$GATEWAY_ID" =~ ^[a-zA-Z0-9._-]+$ ]]; then
    print_error "Invalid gateway identifier format: $GATEWAY_ID"
    exit 1
fi

print_info "Validating gateway: $GATEWAY_ID"

# Test 1: Gateway exists
print_section "Test 1: Gateway Existence"
print_info "Checking if gateway exists..."

if aws bedrock-agentcore-control get-gateway \
  --gateway-identifier "$GATEWAY_ID" \
  --profile "$AWS_PROFILE" \
  --region "$AWS_REGION" > /dev/null 2>&1; then
    print_info "✓ Gateway exists"
else
    print_error "✗ Gateway not found: $GATEWAY_ID"
    exit 1
fi

# Test 2: List gateway targets
print_section "Test 2: Gateway Targets"
print_info "Listing targets on gateway..."

TARGETS_JSON="$(aws bedrock-agentcore-control list-gateway-targets \
  --gateway-identifier "$GATEWAY_ID" \
  --profile "$AWS_PROFILE" \
  --region "$AWS_REGION" 2>/dev/null)" || {
    print_error "✗ Failed to list targets"
    exit 1
}

TARGET_COUNT="$(echo "$TARGETS_JSON" | jq -r '.targets | length')"
print_info "✓ Found $TARGET_COUNT target(s)"

if [ "$TARGET_COUNT" -gt 0 ]; then
    echo ""
    echo "Target Details:"
    echo "$TARGETS_JSON" | jq -r '.targets[] | "  - Target ID: \(.targetId)"'
    echo "$TARGETS_JSON" | jq -r '.targets[] | "    Status: \(.status)"'
fi

# Test 3: Check target details (if targets exist)
if [ "$TARGET_COUNT" -gt 0 ]; then
    print_section "Test 3: Target Details"

    while IFS= read -r TARGET_ID; do
        print_info "Checking target: $TARGET_ID"

        TARGET_DETAIL="$(aws bedrock-agentcore-control get-gateway-target \
          --gateway-identifier "$GATEWAY_ID" \
          --target-identifier "$TARGET_ID" \
          --profile "$AWS_PROFILE" \
          --region "$AWS_REGION" 2>/dev/null)" || {
            print_error "✗ Failed to get target details: $TARGET_ID"
            echo ""
            continue
        }

        STATUS="$(echo "$TARGET_DETAIL" | jq -r '.status')"
        echo "|----------------------------------------|"
        echo "| Target ID    | $TARGET_ID"
        echo "| Status       | $STATUS"
        echo "$TARGET_DETAIL" | jq -r '"| Gateway ARN  | \(.gatewayArn)"' | cut -c1-60
        echo "$TARGET_DETAIL" | jq -r '"| Schema URI   | \(.schemaS3Uri)"' | head -1
        echo "|----------------------------------------|"

        if [ "$STATUS" = "READY" ]; then
            print_info "✓ Target is READY"
        else
            print_warning "⚠ Target status: $STATUS"
        fi

        # Check for common issues
        TARGET_NAME="$(echo "$TARGET_DETAIL" | jq -r '.targetName')"
        if [ "$TARGET_NAME" = "null" ] || [ "$TARGET_NAME" = "None" ] || [ -z "$TARGET_NAME" ]; then
            print_warning "? Target name not set"
        fi
        echo ""
    done < <(echo "$TARGETS_JSON" | jq -r '.targets[].targetId')
fi

# Test 4: Check credential provider access
print_section "Test 4: Credential Provider Access"
print_info "Checking if Gateway service role has credential access..."

# Get gateway details
GATEWAY_DETAIL="$(aws bedrock-agentcore-control get-gateway \
  --gateway-identifier "$GATEWAY_ID" \
  --profile "$AWS_PROFILE" \
  --region "$AWS_REGION" 2>/dev/null)" || {
    print_error "✗ Failed to get gateway details"
    GATEWAY_DETAIL=""
}

if [ -n "$GATEWAY_DETAIL" ]; then
    ROLE_ARN="$(echo "$GATEWAY_DETAIL" | jq -r '.roleArn')"
    print_info "Gateway Role: $ROLE_ARN"

    # Extract role name from ARN
    ROLE_NAME="$(echo "$ROLE_ARN" | cut -d'/' -f2)"

    # Check attached policies
    POLICIES="$(aws iam list-attached-role-policies \
      --role-name "$ROLE_NAME" \
      --profile "$AWS_PROFILE" \
      --region "$AWS_REGION" 2>/dev/null)" || POLICIES=""

    if [ -n "$POLICIES" ]; then
        print_info "✓ Role has attached policies"
        echo "$POLICIES" | jq -r '.AttachedPolicies[] | "  - \(.PolicyName): \(.PolicyArn)"'

        # Note: This is a simplified check - full verification requires policy inspection
        print_info "✓ IAM permissions appear to be configured"
    else
        print_warning "⚠ Could not verify role policies"
    fi
fi

# Test 5: Check CloudFormation stack (optional)
print_section "Test 5: CloudFormation Stack"

# Extract stack name from gateway ID (prefix before first hyphen)
STACK_PREFIX="$(echo "$GATEWAY_ID" | cut -d'-' -f1)"
STACK_NAME="${STACK_PREFIX}FootballAPITarget"

print_info "Checking CloudFormation stack: $STACK_NAME"

STACK_STATUS="$(aws cloudformation describe-stacks \
  --stack-name "$STACK_NAME" \
  --profile "$AWS_PROFILE" \
  --region "$AWS_REGION" \
  --query 'Stacks[0].StackStatus' \
  --output text 2>/dev/null)" || STACK_STATUS=""

if [ -n "$STACK_STATUS" ]; then
    print_info "✓ Stack exists with status: $STACK_STATUS"

    if [ "$STACK_STATUS" = "UPDATE_COMPLETE" ] || [ "$STACK_STATUS" = "CREATE_COMPLETE" ]; then
        print_info "✓ Stack is healthy"
    else
        print_warning "⚠ Stack status: $STACK_STATUS"
    fi
else
    print_warning "⚠ Stack not found (this is OK if using different naming)"
fi
```

## File: `plugins/aws-agentic-ai/skills/aws-agentic-ai/services/identity/README.md`
```markdown
# AgentCore Identity Service

> **Status**: ✅ Available

## Overview

Amazon Bedrock AgentCore Identity is an identity and credential management service designed specifically for AI agents and automated workloads. It provides secure authentication, authorization, and credential management capabilities that enable agents and tools to access AWS resources and third-party services on behalf of users while maintaining strict security controls and audit trails.

## Core Capabilities

### Centralized Agent Identity Management
- **Workload Identities**: Agent identities implemented as workload identities with specialized attributes
- **Unified Directory**: Create, manage, and organize agent identities through unified directory service
- **Hierarchical Organization**: Group-based access controls and hierarchical organization
- **Cross-Environment**: Consistent identity management regardless of deployment location

### Secure Credential Storage
- **Token Vault**: Securely store OAuth 2.0 tokens, client credentials, and API keys
- **Encryption**: Comprehensive encryption at rest and in transit
- **Access Controls**: Strict access controls with independent request validation
- **Defense-in-Depth**: Protects end-user data from malicious or misbehaving agent code

### OAuth 2.0 Flow Support
- **Client Credentials Grant**: Machine-to-machine authentication (2LO)
- **Authorization Code Grant**: User-delegated access (3LO)
- **Built-in Providers**: Pre-configured providers for Google, GitHub, Slack, Salesforce
- **Custom Providers**: Configurable OAuth 2.0 credential providers for custom integrations

### Credential Provider Management
- **API Key Providers**: Securely store and manage API keys
- **OAuth Credential Providers**: Handle OAuth flow and token management
- **Token Lifecycle**: Automatic token refresh and expiration handling
- **Provider Discovery**: Automatically discover available credential providers

### Agent Identity and Access Controls
- **Impersonation Flow**: Agents access resources using provided credentials
- **Audit Trails**: Maintain audit trails for all actions performed on behalf of users
- **Request Verification**: Token signature verification, expiration checks, scope validation
- **Identity-Aware Authorization**: Pass user context to agent code for dynamic decisions

## Use Cases

### Securing AI Agent Access
Enable agents to:
- Authenticate with external services securely
- Access resources on behalf of users
- Maintain proper audit trails
- Implement least-privilege access patterns

### Multi-Provider Authentication
Support scenarios like:
- Different authentication methods for different APIs
- Unified credential management across services
- OAuth flows for user-delegated access
- API key management for service accounts

### Zero-Trust Security Models
Allow implementation of:
- No long-lived credentials in application code
- Centralized, audited credential vault
- Automated rotation to reduce attack window
- Comprehensive access logging

### Compliance and Auditing
Enable teams to:
- Generate reports for compliance audits (SOC2, ISO27001)
- Implement periodic access reviews
- Maintain secrets inventory
- Enforce credential policies

## Quick Start

### Create API Key Credential Provider

```bash
aws bedrock-agentcore-control create-api-key-credential-provider \
  --name MyAPICredentialProvider \
  --api-key "YOUR_API_KEY" \
  --region us-west-2
```

### Create OAuth Credential Provider

```bash
aws bedrock-agentcore-control create-oauth2-credential-provider \
  --name MyOAuthProvider \
  --client-id "YOUR_CLIENT_ID" \
  --client-secret "YOUR_CLIENT_SECRET" \
  --authorization-url "https://provider.com/oauth/authorize" \
  --token-url "https://provider.com/oauth/token" \
  --scopes '["read", "write"]' \
  --region us-west-2
```

### Using Credentials with SDK

```python
from bedrock_agentcore.identity import CredentialProvider

# Get credentials for external API
provider = CredentialProvider("MyAPICredentialProvider")
api_key = provider.get_api_key()

# Get OAuth token
oauth_provider = CredentialProvider("MyOAuthProvider")
token = oauth_provider.get_access_token()
```

## Common Operations

### List Credential Providers

```bash
aws bedrock-agentcore-control list-api-key-credential-providers \
  --region us-west-2
```

### Update Credential Provider

```bash
aws bedrock-agentcore-control update-api-key-credential-provider \
  --name MyAPICredentialProvider \
  --api-key "NEW_API_KEY" \
  --region us-west-2
```

### Delete Credential Provider

```bash
aws bedrock-agentcore-control delete-api-key-credential-provider \
  --name MyAPICredentialProvider \
  --region us-west-2
```

## Built-in OAuth Providers

AgentCore Identity includes built-in providers for popular services:

| Provider | Use Case |
|----------|----------|
| **Google** | Google Workspace, Gmail, Drive |
| **GitHub** | Repository access, Actions |
| **Slack** | Messaging, channel access |
| **Salesforce** | CRM data access |

## Best Practices

### Security
- Use credential providers instead of hardcoded credentials
- Implement least-privilege access for each credential
- Rotate credentials regularly (quarterly minimum)
- Monitor credential usage with CloudWatch

### Development
- Use separate credential providers per environment
- Implement proper error handling for credential access
- Test credential flows in non-production first
- Use SDK annotations for cleaner code

### Operations
- Set up alerts for credential access failures
- Audit credential usage periodically
- Implement automated rotation where possible
- Document credential ownership and purpose

## Troubleshooting

| Issue | Cause | Solution |
|-------|-------|----------|
| Credential not found | Provider doesn't exist or name typo | Verify provider name with list command |
| Invalid API key | Key expired or incorrect | Update credential provider with new key |
| OAuth token expired | Token refresh failed | Check OAuth provider configuration |
| Access denied | Insufficient permissions | Verify IAM policy for credential access |

## Related Services

- **[Gateway Service](../../../README.md)**: Uses Identity for MCP target authentication
- **[Runtime Service](../../../README.md)**: Uses Identity for agent authentication
- **[Memory Service](../../../README.md)**: May use Identity for data encryption

## References

- [AWS Identity Documentation](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity.html)
- [Credential Provider Setup](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity-outbound-credential-provider.html)
- [Identity Features](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/key-features-and-benefits.html)
- [Securing AI Agents Blog](https://aws.amazon.com/blogs/security/securing-ai-agents-with-amazon-bedrock-agentcore-identity/)
```

## File: `plugins/aws-agentic-ai/skills/aws-agentic-ai/services/memory/README.md`
```markdown
# AgentCore Memory Service

> **Status**: ✅ Available

## Overview

Amazon Bedrock AgentCore Memory is a fully managed service that gives AI agents the ability to remember past interactions, enabling more intelligent, context-aware, and personalized conversations. It addresses a fundamental challenge in agentic AI: statelessness. Without memory capabilities, AI agents treat each interaction as a new instance with no knowledge of previous conversations.

## Memory Types

AgentCore Memory offers two types of memory that work together:

### Short-Term Memory
Captures turn-by-turn interactions within a single session, allowing agents to maintain immediate context without requiring users to repeat information.

**Example**: When a user asks "What's the weather like in Seattle?" and follows up with "What about tomorrow?", the agent relies on recent conversation history to understand that "tomorrow" refers to Seattle weather.

### Long-Term Memory
Automatically extracts and stores key insights from conversations across multiple sessions, including user preferences, important facts, and session summaries for persistent knowledge retention.

**Example**: If a customer mentions they prefer window seats during flight booking, the agent stores this preference and proactively offers window seats in future interactions.

## Core Capabilities

### Memory Resource Management
- **Logical Containers**: Encapsulate both raw events and processed long-term memories
- **Retention Policies**: Define how long data is retained
- **Security Configuration**: Control access and encryption
- **Data Transformation**: Transform raw interactions into meaningful insights

### Short-Term Memory Features
- **Event Storage**: Store conversations, system events, and state changes as immutable events
- **Session Organization**: Organize by actor and session
- **Context Preservation**: Maintain immediate context within sessions
- **Structured Storage**: Support structured storage of interaction data

### Long-Term Memory Features
- **Insight Extraction**: Automatically extract insights, preferences, and knowledge
- **Asynchronous Processing**: Extract memories asynchronously using memory strategies
- **Cross-Session Persistence**: Retain information across multiple sessions
- **Semantic Search**: Search memories by meaning and context

### Memory Strategies
Define the intelligence layer that transforms raw events into meaningful memories:

| Strategy | Description |
|----------|-------------|
| **Semantic** | Extract meaningful facts and information |
| **Summary** | Generate conversation summaries |
| **User Preference** | Extract and store user preferences |
| **Custom** | Define custom extraction logic |

### Advanced Features
- **Branching**: Create alternative conversation paths from specific points
- **Checkpointing**: Save and mark specific states for later reference
- **Memory Consolidation**: Merge related memories without duplicates
- **Audit Trail**: Immutable audit trail for all memory operations

## Use Cases

### Conversational Agents
Enable chatbots to:
- Remember previous issues and preferences
- Provide relevant assistance based on history
- Create personalized customer experiences
- Maintain context across session breaks

### Task-Oriented Agents
Support workflows like:
- Track multi-step business process status
- Maintain workflow progress across sessions
- Remember task context for resumption
- Store intermediate results

### Multi-Agent Systems
Allow agent teams to:
- Share memory for synchronized operations
- Coordinate inventory levels and logistics
- Maintain shared context
- Optimize collaborative workflows

### Autonomous Agents
Enable agents to:
- Plan routes based on past experiences
- Learn from previous interactions
- Improve decision-making over time
- Build persistent knowledge bases

## Quick Start

### Create Memory Resource

```bash
aws bedrock-agentcore-control create-memory \
  --memory-name my-agent-memory \
  --memory-strategies '[{"strategyName": "SEMANTIC", "configuration": {}}]' \
  --region us-west-2
```

### Using Memory with SDK

```python
from bedrock_agentcore.memory import MemoryClient

# Initialize memory client
memory = MemoryClient(memory_id="my-agent-memory")

# Add short-term memory event
memory.add_event(
    session_id="session-123",
    actor_id="user-456",
    event_type="message",
    content={"role": "user", "message": "Book a flight to Seattle"}
)

# Retrieve conversation history
history = memory.get_session_events(session_id="session-123")

# Search long-term memories
memories = memory.search_memories(
    query="user flight preferences",
    limit=5
)
```

### Store and Retrieve Memories

```python
# Store long-term memory
memory.store_memory(
    memory_type="user_preference",
    content={"preference": "window_seat", "context": "flights"}
)

# Retrieve relevant memories
relevant = memory.search_memories(
    query="seating preferences for flights",
    actor_id="user-456"
)
```

## Common Operations

### List Memories

```bash
aws bedrock-agentcore-control list-memories \
  --region us-west-2
```

### Get Memory Details

```bash
aws bedrock-agentcore-control get-memory \
  --memory-id <MEMORY_ID> \
  --region us-west-2
```

### Update Memory Configuration

```bash
aws bedrock-agentcore-control update-memory \
  --memory-id <MEMORY_ID> \
  --memory-strategies '[{"strategyName": "SEMANTIC"}, {"strategyName": "USER_PREFERENCE"}]' \
  --region us-west-2
```

### Delete Memory

```bash
aws bedrock-agentcore-control delete-memory \
  --memory-id <MEMORY_ID> \
  --region us-west-2
```

## Memory Strategies Configuration

### Built-in Strategies

```bash
# Use semantic strategy
aws bedrock-agentcore-control create-memory \
  --memory-name semantic-memory \
  --memory-strategies '[{
    "strategyName": "SEMANTIC",
    "configuration": {}
  }]'
```

### Custom Strategies

```bash
# Create custom strategy with specific model
aws bedrock-agentcore-control create-memory \
  --memory-name custom-memory \
  --memory-strategies '[{
    "strategyName": "CUSTOM",
    "configuration": {
      "modelId": "anthropic.claude-3-sonnet",
      "extractionPrompt": "Extract key user preferences from this conversation"
    }
  }]'
```

## Best Practices

### Memory Architecture
- Design memory architecture intentionally
- Choose appropriate strategies for use case
- Implement proper retention policies
- Consider memory costs and storage

### Performance
- Use appropriate time-to-live settings
- Extract only relevant information
- Implement rhythm of memory operations
- Monitor memory search latency

### Security
- Implement proper access controls
- Encrypt sensitive memories
- Audit memory access
- Follow data privacy regulations (GDPR, HIPAA)

### Operations
- Monitor memory usage and costs
- Set up alerts for memory failures
- Implement backup strategies
- Test memory operations regularly

## Troubleshooting

| Issue | Cause | Solution |
|-------|-------|----------|
| Memory not found | Incorrect memory ID | Verify memory ID with list command |
| Search returns empty | No matching memories | Check query and memory content |
| Slow memory retrieval | Large memory size | Implement pagination and filters |
| Strategy extraction fails | Invalid configuration | Check strategy configuration |

## Related Services

- **[Gateway Service](../../../README.md)**: Expose APIs as tools for agents
- **[Runtime Service](../../../README.md)**: Execute agents that generate conversation data
- **[Identity Service](../../../README.md)**: Secure access to conversation data
- **[Observability Service](../../../README.md)**: Monitor memory operations

## References

- [AWS Memory Documentation](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html)
- [Memory Types](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory-types.html)
- [Memory Strategies](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory-strategies.html)
- [Building Context-Aware Agents Blog](https://aws.amazon.com/blogs/machine-learning/amazon-bedrock-agentcore-memory-building-context-aware-agents/)
- [Long-Term Memory Deep Dive](https://aws.amazon.com/blogs/machine-learning/building-smarter-ai-agents-agentcore-long-term-memory-deep-dive/)
```

## File: `plugins/aws-agentic-ai/skills/aws-agentic-ai/services/observability/README.md`
```markdown
# AgentCore Observability Service

> **Status**: ✅ Available

## Overview

Amazon Bedrock AgentCore Observability helps developers trace, debug, and monitor agent performance in production through unified operational dashboards and OpenTelemetry-compatible telemetry.

## Core Capabilities

### Distributed Tracing
- **End-to-End Tracing**: Complete request tracing across all AgentCore services
- **Workflow Visualization**: Detailed step-by-step workflow execution views
- **Service Dependencies**: Automatic mapping of service interactions
- **Bottleneck Detection**: Identify performance bottlenecks in agent workflows
- **Error Attribution**: Pinpoint exact failure points in complex workflows

### Metrics and Monitoring
- **Real-Time Metrics**: Live operational metrics for all agent activities
- **Token Tracking**: Monitor token consumption and costs
- **Latency Measurements**: Track P50, P95, P99 response times
- **Session Monitoring**: Track session duration and status
- **Error Rates**: Monitor error rates by service and operation
- **Throughput**: Measure requests per second and operation counts

### Logging
- **Centralized Aggregation**: All service logs in one place
- **Structured Logging**: Consistent log format with correlation IDs
- **Search and Filter**: Query logs by service, operation, or time
- **Real-Time Streaming**: Live log tailing for debugging
- **Log Retention**: Configurable retention policies

### Dashboards and Alerting
- **Unified Dashboards**: Pre-built operational dashboards
- **Custom Metrics**: Define and visualize custom metrics
- **CloudWatch Integration**: Native AWS CloudWatch support
- **Configurable Alerts**: Set up alerts for critical conditions
- **Multi-Service Views**: Consolidated view across all services

### OpenTelemetry Support
- **Industry Standard**: Compatible with OpenTelemetry specification
- **Tool Integration**: Works with existing observability tools
- **Custom Instrumentation**: Add custom traces and metrics
- **External Export**: Export telemetry to external systems

## Use Cases

### Production Debugging
Enable teams to:
- Debug agent execution issues in real-time
- Identify root causes of failures quickly
- Trace request flows across services
- Analyze error patterns and trends

### Performance Monitoring
Support scenarios like:
- Monitor agent response times
- Track token usage and costs
- Identify slow operations
- Optimize agent workflows

### Behavior Analysis
Allow teams to:
- Analyze agent behavior patterns
- Understand user interaction flows
- Identify usage trends
- Detect anomalies

### Quality Assurance
Enable teams to:
- Ensure SLA compliance
- Monitor service reliability
- Track quality metrics
- Validate performance standards

### Capacity Planning
Support activities like:
- Forecast resource needs
- Identify scaling requirements
- Optimize resource allocation
- Plan for growth

## Architecture

### Observability Data Flow

```
┌─────────────────────────────────────────┐
│  AgentCore Services                     │
│  - Gateway, Runtime, Memory, etc.       │
│  - Emit traces, logs, metrics           │
└─────────────────────────────────────────┘
           ↓
┌─────────────────────────────────────────┐
│  OpenTelemetry Collector                │
│  - Receive telemetry data               │
│  - Process and enrich                   │
│  - Route to destinations                │
└─────────────────────────────────────────┘
           ↓
    ┌──────┴──────┐
    ↓             ↓
┌─────────┐  ┌─────────────┐
│CloudWatch│  │  X-Ray      │
│ Logs    │  │  Traces     │
│ Metrics │  │  Service Map│
└─────────┘  └─────────────┘
    ↓             ↓
┌─────────────────────────────────────────┐
│  Unified Dashboards                     │
│  - Service health                       │
│  - Performance metrics                  │
│  - Error analysis                       │
│  - Cost tracking                        │
└─────────────────────────────────────────┘
```

### Data Collection Model

1. **Automatic Instrumentation**: Built-in instrumentation for all services
2. **Context Propagation**: Correlation IDs passed across service boundaries
3. **Sampling**: Intelligent sampling for high-volume operations
4. **Buffering**: Local buffering for reliability
5. **Batch Export**: Efficient batch transmission to backends

## Configuration

### Enable Observability

```bash
# Enable observability for agent
aws bedrock-agentcore-control update-observability-config \
  --agent-id <AGENT_ID> \
  --config '{
    "tracing": {
      "enabled": true,
      "samplingRate": 1.0
    },
    "metrics": {
      "enabled": true,
      "interval": 60
    },
    "logging": {
      "enabled": true,
      "level": "INFO"
    }
  }' \
  --region <REGION>
```

### Configure Sampling

```bash
# Set trace sampling rate
aws bedrock-agentcore-control update-tracing-config \
  --agent-id <AGENT_ID> \
  --sampling-rate 0.1 \
  --region <REGION>
```

### Custom Metrics

```bash
# Define custom metric
aws bedrock-agentcore-control create-custom-metric \
  --agent-id <AGENT_ID> \
  --metric-name "CustomOperationCount" \
  --metric-type "Counter" \
  --description "Count of custom operations" \
  --region <REGION>
```

## Traces

### View Traces

```bash
# Query recent traces
aws xray get-trace-summaries \
  --start-time <START_TIMESTAMP> \
  --end-time <END_TIMESTAMP> \
  --filter-expression 'service(id(name: "AgentCore", type: "AWS::Service"))'
```

### Trace Details

```bash
# Get specific trace
aws xray batch-get-traces \
  --trace-ids <TRACE_ID_1> <TRACE_ID_2>
```

### Service Map

```bash
# Get service map
aws xray get-service-graph \
  --start-time <START_TIMESTAMP> \
  --end-time <END_TIMESTAMP>
```

## Metrics

### Common Metrics

**Gateway Metrics**:
- `TargetInvocations`: Number of target invocations
- `TargetErrors`: Number of target errors
- `TargetLatency`: Target response latency

**Runtime Metrics**:
- `AgentExecutions`: Number of agent executions
- `ExecutionDuration`: Agent execution duration
- `ExecutionErrors`: Number of execution failures

**Memory Metrics**:
- `MemoryReads`: Number of memory read operations
- `MemoryWrites`: Number of memory write operations
- `MemorySize`: Total memory storage size

**Token Metrics**:
- `TokensConsumed`: Total tokens used
- `TokenCost`: Estimated cost in dollars

### Query Metrics

```bash
# Get metric statistics
aws cloudwatch get-metric-statistics \
  --namespace AWS/BedrockAgentCore \
  --metric-name TargetInvocations \
  --dimensions Name=AgentId,Value=<AGENT_ID> \
  --start-time <START> \
  --end-time <END> \
  --period 300 \
  --statistics Sum Average
```

### Custom Metrics

```bash
# Put custom metric data
aws cloudwatch put-metric-data \
  --namespace AgentCore/Custom \
  --metric-name CustomMetric \
  --value 1.0 \
  --dimensions AgentId=<AGENT_ID>
```

## Logs

### Query Logs

```bash
# Tail agent logs
aws logs tail /aws/bedrock-agentcore/<AGENT_ID> \
  --follow \
  --format short

# Query logs with filter
aws logs filter-log-events \
  --log-group-name /aws/bedrock-agentcore/<AGENT_ID> \
  --filter-pattern "ERROR" \
  --start-time <TIMESTAMP>
```

### Log Insights

```bash
# Run Insights query
aws logs start-query \
  --log-group-name /aws/bedrock-agentcore/<AGENT_ID> \
  --start-time <START_TIMESTAMP> \
  --end-time <END_TIMESTAMP> \
  --query-string 'fields @timestamp, @message
    | filter @message like /ERROR/
    | sort @timestamp desc
    | limit 20'
```

## Dashboards

### Create Dashboard

```bash
# Create CloudWatch dashboard
aws cloudwatch put-dashboard \
  --dashboard-name AgentCore-<AGENT_ID> \
  --dashboard-body file://dashboard-definition.json
```

### Dashboard Definition Example

```json
{
  "widgets": [
    {
      "type": "metric",
      "properties": {
        "metrics": [
          ["AWS/BedrockAgentCore", "TargetInvocations", {"stat": "Sum"}]
        ],
        "period": 300,
        "stat": "Sum",
        "region": "us-west-2",
        "title": "Target Invocations"
      }
    },
    {
      "type": "metric",
      "properties": {
        "metrics": [
          ["AWS/BedrockAgentCore", "TargetErrors", {"stat": "Sum"}]
        ],
        "period": 300,
        "stat": "Sum",
        "region": "us-west-2",
        "title": "Target Errors"
      }
    }
  ]
}
```

## Alerting

### Create Alarm

```bash
# Create CloudWatch alarm
aws cloudwatch put-metric-alarm \
  --alarm-name high-error-rate-<AGENT_ID> \
  --alarm-description "Alert when error rate exceeds threshold" \
  --metric-name TargetErrors \
  --namespace AWS/BedrockAgentCore \
  --statistic Sum \
  --period 300 \
  --evaluation-periods 2 \
  --threshold 10 \
  --comparison-operator GreaterThanThreshold \
  --dimensions Name=AgentId,Value=<AGENT_ID> \
  --alarm-actions <SNS_TOPIC_ARN>
```

### Alarm Templates

**High Error Rate**:
```bash
# Alert on >5% error rate
aws cloudwatch put-metric-alarm \
  --alarm-name error-rate-high \
  --metric-name ErrorRate \
  --threshold 5 \
  --comparison-operator GreaterThanThreshold
```

**High Latency**:
```bash
# Alert on P95 latency >2s
aws cloudwatch put-metric-alarm \
  --alarm-name latency-high \
  --metric-name TargetLatency \
  --statistic p95 \
  --threshold 2000 \
  --comparison-operator GreaterThanThreshold
```

**High Token Usage**:
```bash
# Alert on excessive token usage
aws cloudwatch put-metric-alarm \
  --alarm-name tokens-high \
  --metric-name TokensConsumed \
  --statistic Sum \
  --threshold 1000000 \
  --comparison-operator GreaterThanThreshold
```

## Best Practices

### Instrumentation
- Enable observability for all production agents
- Use appropriate sampling rates (1.0 for dev, 0.1 for prod)
- Add custom metrics for business-critical operations
- Include context in log messages
- Use structured logging formats

### Performance
- Use appropriate metric aggregation periods
- Implement metric sampling for high-volume operations
- Set reasonable log retention periods
- Use log filtering to reduce noise
- Archive old traces and logs

### Cost Optimization
- Adjust sampling rates based on traffic
- Use metric filters to create custom metrics
- Set appropriate log retention (7-30 days)
- Archive infrequently accessed data to S3
- Use CloudWatch Insights for complex queries

### Alerting
- Define clear SLOs and SLIs
- Set meaningful alert thresholds
- Avoid alert fatigue with proper tuning
- Use composite alarms for complex conditions
- Implement escalation policies

### Security
- Encrypt logs and metrics at rest
- Use IAM for access control
- Implement least privilege access
- Audit observability data access
- Protect sensitive data in logs

## Integration Patterns

### With All Services

Observability is automatically integrated with all AgentCore services:

```
Gateway ──→ Observability
Runtime ──→ Observability
Memory ──→ Observability
Identity ──→ Observability
Code Interpreter ──→ Observability
Browser ──→ Observability
```

### With External Tools

Export telemetry to external observability platforms:

```
AgentCore Observability
    ↓
OpenTelemetry Collector
    ↓
┌────────┬────────┬────────┐
│Datadog │New Relic│Grafana│
└────────┴────────┴────────┘
```

## Troubleshooting

### No Traces Appearing

**Diagnosis**:
```bash
# Check if tracing is enabled
aws bedrock-agentcore-control get-observability-config \
  --agent-id <AGENT_ID>
```

**Solution**: Enable tracing in observability configuration

### High Cardinality Metrics

**Symptom**: Too many unique metric combinations
**Solution**: Reduce dimension cardinality, use metric filters

### Missing Logs

**Diagnosis**:
```bash
# Check log group exists
aws logs describe-log-groups \
  --log-group-name-prefix /aws/bedrock-agentcore
```

**Solution**: Verify IAM permissions for CloudWatch Logs

### High Costs

**Symptom**: Excessive CloudWatch costs
**Solution**: Adjust sampling rates, reduce log retention, archive old data

## Performance Monitoring

### Key Performance Indicators

**Availability**:
- Service uptime percentage
- Error rate by service
- Failed request percentage

**Performance**:
- P50, P95, P99 latency
- Request throughput
- Operation duration

**Efficiency**:
- Token consumption rate
- Cost per operation
- Resource utilization

**Quality**:
- Agent success rate
- User satisfaction metrics
- Workflow completion rate

## Additional Resources

- **AWS Documentation**: [Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html)
- **CloudWatch Guide**: [CloudWatch User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/)
- **X-Ray Guide**: [AWS X-Ray Developer Guide](https://docs.aws.amazon.com/xray/latest/devguide/)
- **OpenTelemetry**: [OpenTelemetry Documentation](https://opentelemetry.io/brain/knowledge/docs_legacy/)
- **Best Practices**: [Observability Best Practices](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability-best-practices.html)

---

**Related Services**:
- [Gateway Service](../../../README.md) - Gateway monitoring
- [Runtime Service](../../../README.md) - Runtime tracing
- [Memory Service](../../../README.md) - Memory metrics
- [Credential Management](../../cross-service/credential-management.md) - Cross-service credential patterns
```

## File: `plugins/aws-agentic-ai/skills/aws-agentic-ai/services/runtime/README.md`
```markdown
# Runtime Service

The Runtime service provides a secure, serverless hosting environment for deploying and running AI agents or tools. It handles scaling, session management, security isolation, and infrastructure management.

## Key Features

| Feature | Description |
|---------|-------------|
| **Framework Agnostic** | Works with LangGraph, Strands, CrewAI, or custom agents |
| **Model Flexibility** | Supports any LLM (Bedrock, Claude, Gemini, OpenAI) |
| **Protocol Support** | MCP (Model Context Protocol) and A2A (Agent to Agent) |
| **Session Isolation** | Dedicated microVM per session with isolated CPU, memory, filesystem |
| **Extended Execution** | Up to 8 hours for long-running workloads |
| **100MB Payloads** | Handle multimodal content (text, images, audio, video) |
| **Bidirectional Streaming** | HTTP API and WebSocket for real-time interactions |

## Quick Start

### Prerequisites
- AWS CLI configured with appropriate permissions
- Docker installed for container builds
- Python 3.9+ for SDK usage

### Deploy an Agent

**Step 1: Install AgentCore SDK**
```bash
pip install bedrock-agentcore
```

**Step 2: Create agent code**
```python
from bedrock_agentcore.runtime import BedrockAgentCoreApp

app = BedrockAgentCoreApp()

@app.handler()
async def handle_request(request, context):
    user_input = request.get("input", "")
    # Your agent logic here
    return {"response": f"Processed: {user_input}"}
```

**Step 3: Create AgentCore Runtime**
```bash
aws bedrock-agentcore-control create-agent-runtime \
  --agent-runtime-name my-agent \
  --runtime-artifact '{"containerConfiguration": {"containerUri": "<ACCOUNT_ID>.dkr.ecr.<REGION>.amazonaws.com/my-agent:latest"}}' \
  --role-arn arn:aws:iam::<ACCOUNT_ID>:role/AgentRuntimeExecutionRole \
  --network-configuration '{"networkMode": "PUBLIC"}' \
  --region us-west-2
```

**Step 4: Invoke agent**
```bash
aws bedrock-agentcore-runtime invoke-agent-runtime \
  --agent-runtime-endpoint-arn arn:aws:bedrock-agentcore:us-west-2:<ACCOUNT_ID>:runtime/my-agent/endpoint/DEFAULT \
  --payload '{"input": "Hello, agent!"}' \
  --region us-west-2
```

## Core Components

### AgentCore Runtime
Containerized application hosting your AI agent or tool code. Each runtime:
- Has a unique identity
- Is versioned for controlled deployment and updates
- Can use popular frameworks or custom implementations

### Versions
Immutable snapshots of configuration:
- Version 1 (V1) created automatically with new runtime
- Each update creates a new version
- Enables rollback capabilities

### Endpoints
Addressable access points to runtime versions:
- **DEFAULT**: Automatically created, points to latest version
- Custom endpoints for different environments (dev, test, prod)
- Unique ARN for invocation

Endpoint states: `CREATING` → `READY` (or `CREATE_FAILED`) → `UPDATING` → `READY`

### Sessions
Individual interaction contexts with complete isolation:
- Dedicated microVM per session
- Preserves context across interactions
- Persists up to 8 hours
- Auto-terminates after 15 minutes idle

Session states: `Active` → `Idle` → `Terminated`

## Authentication

### Inbound (Who Can Access Your Agent)

| Method | Description |
|--------|-------------|
| **IAM (SigV4)** | AWS credentials for identity verification |
| **OAuth 2.0** | External identity providers (Cognito, Okta, Entra ID) |

**OAuth Flow**:
1. User authenticates with identity provider
2. Client receives bearer token
3. Token passed in authorization header
4. Runtime validates token
5. Request processed or rejected

### Outbound (Accessing External Services)

| Method | Use Case |
|--------|----------|
| **OAuth** | Services supporting OAuth flows |
| **API Keys** | Key-based authentication |

**Modes**:
- **User-delegated**: Acting on behalf of end user
- **Autonomous**: Acting with service-level credentials

## Common Operations

### List Agent Runtimes
```bash
aws bedrock-agentcore-control list-agent-runtimes \
  --region us-west-2
```

### Get Runtime Details
```bash
aws bedrock-agentcore-control get-agent-runtime \
  --agent-runtime-id <RUNTIME_ID> \
  --region us-west-2
```

### Update Runtime
```bash
aws bedrock-agentcore-control update-agent-runtime \
  --agent-runtime-id <RUNTIME_ID> \
  --runtime-artifact '{"containerConfiguration": {"containerUri": "<NEW_IMAGE_URI>"}}' \
  --region us-west-2
```

### Delete Runtime
```bash
aws bedrock-agentcore-control delete-agent-runtime \
  --agent-runtime-id <RUNTIME_ID> \
  --region us-west-2
```

## Long-Running Agents

For workloads exceeding request/response cycles (up to 8 hours):

```python
from bedrock_agentcore.runtime import BedrockAgentCoreApp

app = BedrockAgentCoreApp()

@app.handler()
async def handle_request(request, context):
    # Add async task
    task_id = context.add_async_task("background-processing")

    # Start background work
    # ... long-running operation ...

    # Complete task when done
    context.complete_async_task(task_id)

    return {"status": "Task started", "task_id": task_id}
```

## Streaming Responses

Enable real-time partial results:

```python
@app.handler()
async def handle_request(request, context):
    async for chunk in generate_response(request):
        yield {"partial": chunk}
    yield {"complete": True}
```

## Supported Frameworks

| Framework | Description |
|-----------|-------------|
| **LangGraph** | Graph-based agent workflows |
| **Strands** | AWS-native agent framework |
| **CrewAI** | Multi-agent collaboration |
| **Custom** | Any Python-based agent |

## Troubleshooting

| Error | Cause | Solution |
|-------|-------|----------|
| 504 Gateway Timeout | Container issues, ARM64 compatibility | Ensure container exposes port 8080, use ARM64 image |
| 403 AccessDeniedException | Missing permissions | Verify IAM role and policies |
| exec format error | Wrong architecture | Build ARM64 containers with buildx |
| Session terminated after 15min | Idle timeout | Implement ping handler with HEALTHY_BUSY status |

## Related Services

- **[Gateway Service](../../../README.md)**: Expose APIs as tools for agents
- **[Memory Service](../../../README.md)**: Store agent conversation history
- **[Identity Service](../../../README.md)**: Manage agent credentials
- **[Observability Service](../../../README.md)**: Monitor agent performance

## References

- [AWS Runtime Documentation](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html)
- [How Runtime Works](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-how-it-works.html)
- [Runtime Troubleshooting](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-troubleshooting.html)
- [Runtime API Reference](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/)
```

## File: `plugins/aws-cdk/skills/aws-cdk-development/SKILL.md`
```markdown
---
name: aws-cdk-development
description: AWS Cloud Development Kit (CDK) expert for building cloud infrastructure with TypeScript/Python. Use when creating CDK stacks, defining CDK constructs, implementing infrastructure as code, or when the user mentions CDK, CloudFormation, IaC, cdk synth, cdk deploy, or wants to define AWS infrastructure programmatically. Covers CDK app structure, construct patterns, stack composition, and deployment workflows.
context: fork
skills:
  - aws-mcp-setup
allowed-tools:
  - mcp__cdk__*
  - mcp__aws-mcp__*
  - mcp__awsdocs__*
  - Bash(cdk *)
  - Bash(npm *)
  - Bash(npx *)
  - Bash(aws cloudformation *)
  - Bash(aws sts get-caller-identity)
hooks:
  PreToolUse:
    - matcher: Bash(cdk deploy*)
      command: aws sts get-caller-identity --query Account --output text
      once: true
---

# AWS CDK Development

This skill provides comprehensive guidance for developing AWS infrastructure using the Cloud Development Kit (CDK), with integrated MCP servers for accessing latest AWS knowledge and CDK utilities.

## AWS Documentation Requirement

Always verify AWS facts using MCP tools (`mcp__aws-mcp__*` or `mcp__*awsdocs*__*`) before answering. The `aws-mcp-setup` dependency is auto-loaded — if MCP tools are unavailable, guide the user through that skill's setup flow.

## Integrated MCP Servers

This skill includes the CDK MCP server automatically configured with the plugin:

### AWS CDK MCP Server
**When to use**: For CDK-specific guidance and utilities
- Get CDK construct recommendations
- Retrieve CDK best practices
- Access CDK pattern suggestions
- Validate CDK configurations
- Get help with CDK-specific APIs

**Important**: Leverage this server for CDK construct guidance and advanced CDK operations.

## When to Use This Skill

Use this skill when:
- Creating new CDK stacks or constructs
- Refactoring existing CDK infrastructure
- Implementing Lambda functions within CDK
- Following AWS CDK best practices
- Validating CDK stack configurations before deployment
- Verifying AWS service capabilities and regional availability

## Core CDK Principles

### Resource Naming

**CRITICAL**: Do NOT explicitly specify resource names when they are optional in CDK constructs.

**Why**: CDK-generated names enable:
- **Reusable patterns**: Deploy the same construct/pattern multiple times without conflicts
- **Parallel deployments**: Multiple stacks can deploy simultaneously in the same region
- **Cleaner shared logic**: Patterns and shared code can be initialized multiple times without name collision
- **Stack isolation**: Each stack gets uniquely identified resources automatically

**Pattern**: Let CDK generate unique names automatically using CloudFormation's naming mechanism.

```typescript
// ❌ BAD - Explicit naming prevents reusability and parallel deployments
new lambda.Function(this, 'MyFunction', {
  functionName: 'my-lambda',  // Avoid this
  // ...
});

// ✅ GOOD - Let CDK generate unique names
new lambda.Function(this, 'MyFunction', {
  // No functionName specified - CDK generates: StackName-MyFunctionXXXXXX
  // ...
});
```

**Security Note**: For different environments (dev, staging, prod), follow AWS Security Pillar best practices by using separate AWS accounts rather than relying on resource naming within a single account. Account-level isolation provides stronger security boundaries.

### Lambda Function Development

Use the appropriate Lambda construct based on runtime:

**TypeScript/JavaScript**: Use `@aws-cdk/aws-lambda-nodejs`
```typescript
import { NodejsFunction } from 'aws-cdk-lib/aws-lambda-nodejs';

new NodejsFunction(this, 'MyFunction', {
  entry: 'lambda/handler.ts',
  handler: 'handler',
  // Automatically handles bundling, dependencies, and transpilation
});
```

**Python**: Use `@aws-cdk/aws-lambda-python`
```typescript
import { PythonFunction } from '@aws-cdk/aws-lambda-python-alpha';

new PythonFunction(this, 'MyFunction', {
  entry: 'lambda',
  index: 'handler.py',
  handler: 'handler',
  // Automatically handles dependencies and packaging
});
```

**Benefits**:
- Automatic bundling and dependency management
- Transpilation handled automatically
- No manual packaging required
- Consistent deployment patterns

### Pre-Deployment Validation

Use a **multi-layer validation strategy** for comprehensive CDK quality checks:

#### Layer 1: Real-Time IDE Feedback (Recommended)

**For TypeScript/JavaScript projects**:

Install [cdk-nag](https://github.com/cdklabs/cdk-nag) for synthesis-time validation:
```bash
npm install --save-dev cdk-nag
```

Add to your CDK app:
```typescript
import { Aspects } from 'aws-cdk-lib';
import { AwsSolutionsChecks } from 'cdk-nag';

const app = new App();
Aspects.of(app).add(new AwsSolutionsChecks());
```

**Optional - VS Code users**: Install [CDK NAG Validator extension](https://marketplace.visualstudio.com/items?itemName=alphacrack.cdk-nag-validator) for faster feedback on file save.

**For Python/Java/C#/Go projects**: cdk-nag is available in all CDK languages and provides the same synthesis-time validation.

#### Layer 2: Synthesis-Time Validation (Required)

1. **Synthesis with cdk-nag**: Validate stack with comprehensive rules
   ```bash
   cdk synth  # cdk-nag runs automatically via Aspects
   ```

2. **Suppress legitimate exceptions** with documented reasons:
   ```typescript
   import { NagSuppressions } from 'cdk-nag';

   // Document WHY the exception is needed
   NagSuppressions.addResourceSuppressions(resource, [
     {
       id: 'AwsSolutions-L1',
       reason: 'Lambda@Edge requires specific runtime for CloudFront compatibility'
     }
   ]);
   ```

#### Layer 3: Pre-Commit Safety Net

1. **Build**: Ensure compilation succeeds
   ```bash
   npm run build  # or language-specific build command
   ```

2. **Tests**: Run unit and integration tests
   ```bash
   npm test  # or pytest, mvn test, etc.
   ```

3. **Validation Script**: Meta-level checks
   ```bash
   ./scripts/validate-stack.sh
   ```

The validation script now focuses on:
- Language detection
- Template size and resource count analysis
- Synthesis success verification
- (Note: Detailed anti-pattern checks are handled by cdk-nag)

## Workflow Guidelines

### Development Workflow

1. **Design**: Plan infrastructure resources and relationships
2. **Verify AWS Services**: Use AWS Documentation MCP to confirm service availability and features
   - Check regional availability for all required services
   - Verify service limits and quotas
   - Confirm latest API specifications
3. **Implement**: Write CDK constructs following best practices
   - Use CDK MCP server for construct recommendations
   - Reference CDK best practices via MCP tools
4. **Validate**: Run pre-deployment checks (see above)
5. **Synthesize**: Generate CloudFormation templates
6. **Review**: Examine synthesized templates for correctness
7. **Deploy**: Deploy to target environment
8. **Verify**: Confirm resources are created correctly

### Stack Organization

- Use nested stacks for complex applications
- Separate concerns into logical construct boundaries
- Export values that other stacks may need
- Use CDK context for environment-specific configuration

### Testing Strategy

- Unit test individual constructs
- Integration test stack synthesis
- Snapshot test CloudFormation templates
- Validate resource properties and relationships

## Using MCP Servers Effectively

### When to Use AWS Documentation MCP

**Always verify before implementing**:
- New AWS service features or configurations
- Service availability in target regions
- API parameter specifications
- Service limits and quotas
- Security best practices for AWS services

**Example scenarios**:
- "Check if Lambda supports Python 3.13 runtime"
- "Verify DynamoDB is available in eu-south-2"
- "What are the current Lambda timeout limits?"
- "Get latest S3 encryption options"

### When to Use CDK MCP Server

**Leverage for CDK-specific guidance**:
- CDK construct selection and usage
- CDK API parameter options
- CDK best practice patterns
- Construct property configurations
- CDK-specific optimizations

**Example scenarios**:
- "What's the recommended CDK construct for API Gateway REST API?"
- "How to configure NodejsFunction bundling options?"
- "Best practices for CDK stack organization"
- "CDK construct for DynamoDB with auto-scaling"

### MCP Usage Best Practices

1. **Verify First**: Always check AWS Documentation MCP before implementing new features
2. **Regional Validation**: Check service availability in target deployment regions
3. **CDK Guidance**: Use CDK MCP for construct-specific recommendations
4. **Stay Current**: MCP servers provide latest information beyond knowledge cutoff
5. **Combine Sources**: Use both skill patterns and MCP servers for comprehensive guidance

## CDK Patterns Reference

For detailed CDK patterns, anti-patterns, and architectural guidance, refer to the comprehensive reference:

**File**: `references/cdk-patterns.md`

This reference includes:
- Common CDK patterns and their use cases
- Anti-patterns to avoid
- Security best practices
- Cost optimization strategies
- Performance considerations

## Additional Resources

- **Validation Script**: `scripts/validate-stack.sh` - Pre-deployment validation
- **CDK Patterns**: `references/cdk-patterns.md` - Detailed pattern library
- **AWS Documentation MCP**: Integrated for latest AWS information
- **CDK MCP Server**: Integrated for CDK-specific guidance

## GitHub Actions Integration

When GitHub Actions workflow files exist in the repository, ensure all checks defined in `.github/workflows/` pass before committing. This prevents CI/CD failures and maintains code quality standards.
```

## File: `plugins/aws-cdk/skills/aws-cdk-development/references/cdk-patterns.md`
```markdown
# AWS CDK Patterns and Best Practices

This reference provides detailed patterns, anti-patterns, and best practices for AWS CDK development.

## Table of Contents

- [Naming Conventions](#naming-conventions)
- [Construct Patterns](#construct-patterns)
- [Security Patterns](#security-patterns)
- [Lambda Integration](#lambda-integration)
- [Testing Patterns](#testing-patterns)
- [Cost Optimization](#cost-optimization)
- [Anti-Patterns](#anti-patterns)

## Naming Conventions

### Automatic Resource Naming (Recommended)

Let CDK and CloudFormation generate unique resource names automatically:

**Benefits**:
- Enables multiple deployments in the same region/account
- Supports parallel environments (dev, staging, prod)
- Prevents naming conflicts
- Allows stack cloning and testing

**Example**:
```typescript
// ✅ GOOD - Automatic naming
const bucket = new s3.Bucket(this, 'DataBucket', {
  // No bucketName specified
  encryption: s3.BucketEncryption.S3_MANAGED,
});
```

### When Explicit Naming is Required

Some scenarios require explicit names:
- Resources referenced by external systems
- Resources that must maintain consistent names across deployments
- Cross-stack references requiring stable names

**Pattern**: Use logical prefixes and environment suffixes
```typescript
// Only when absolutely necessary
const bucket = new s3.Bucket(this, 'DataBucket', {
  bucketName: `${props.projectName}-data-${props.environment}`,
});
```

## Construct Patterns

### L3 Constructs (Patterns)

Prefer high-level patterns that encapsulate best practices:

```typescript
import * as patterns from 'aws-cdk-lib/aws-apigateway';

new patterns.LambdaRestApi(this, 'MyApi', {
  handler: myFunction,
  // Includes CloudWatch Logs, IAM roles, and API Gateway configuration
});
```

### Custom Constructs

Create reusable constructs for repeated patterns:

```typescript
export class ApiWithDatabase extends Construct {
  public readonly api: apigateway.RestApi;
  public readonly table: dynamodb.Table;

  constructor(scope: Construct, id: string, props: ApiWithDatabaseProps) {
    super(scope, id);

    this.table = new dynamodb.Table(this, 'Table', {
      partitionKey: { name: 'id', type: dynamodb.AttributeType.STRING },
      billingMode: dynamodb.BillingMode.PAY_PER_REQUEST,
    });

    const handler = new NodejsFunction(this, 'Handler', {
      entry: props.handlerEntry,
      environment: {
        TABLE_NAME: this.table.tableName,
      },
    });

    this.table.grantReadWriteData(handler);

    this.api = new apigateway.LambdaRestApi(this, 'Api', {
      handler,
    });
  }
}
```

## Security Patterns

### IAM Least Privilege

Use grant methods instead of broad policies:

```typescript
// ✅ GOOD - Specific grants
const table = new dynamodb.Table(this, 'Table', { /* ... */ });
const lambda = new lambda.Function(this, 'Function', { /* ... */ });

table.grantReadWriteData(lambda);

// ❌ BAD - Overly broad permissions
lambda.addToRolePolicy(new iam.PolicyStatement({
  actions: ['dynamodb:*'],
  resources: ['*'],
}));
```

### Secrets Management

Use Secrets Manager for sensitive data:

```typescript
import * as secretsmanager from 'aws-cdk-lib/aws-secretsmanager';

const secret = new secretsmanager.Secret(this, 'DbPassword', {
  generateSecretString: {
    secretStringTemplate: JSON.stringify({ username: 'admin' }),
    generateStringKey: 'password',
    excludePunctuation: true,
  },
});

// Grant read access to Lambda
secret.grantRead(myFunction);
```

### VPC Configuration

Follow VPC best practices:

```typescript
const vpc = new ec2.Vpc(this, 'Vpc', {
  maxAzs: 2,
  natGateways: 1, // Cost optimization: use 1 for dev, 2+ for prod
  subnetConfiguration: [
    {
      name: 'Public',
      subnetType: ec2.SubnetType.PUBLIC,
      cidrMask: 24,
    },
    {
      name: 'Private',
      subnetType: ec2.SubnetType.PRIVATE_WITH_EGRESS,
      cidrMask: 24,
    },
    {
      name: 'Isolated',
      subnetType: ec2.SubnetType.PRIVATE_ISOLATED,
      cidrMask: 24,
    },
  ],
});
```

## Lambda Integration

### NodejsFunction (TypeScript/JavaScript)

```typescript
import { NodejsFunction } from 'aws-cdk-lib/aws-lambda-nodejs';

const fn = new NodejsFunction(this, 'Function', {
  entry: 'src/handlers/process.ts',
  handler: 'handler',
  runtime: lambda.Runtime.NODEJS_20_X,
  timeout: Duration.seconds(30),
  memorySize: 512,
  environment: {
    TABLE_NAME: table.tableName,
  },
  bundling: {
    minify: true,
    sourceMap: true,
    externalModules: ['@aws-sdk/*'], // Use AWS SDK from Lambda runtime
  },
});
```

### PythonFunction

```typescript
import { PythonFunction } from '@aws-cdk/aws-lambda-python-alpha';

const fn = new PythonFunction(this, 'Function', {
  entry: 'src/handlers',
  index: 'process.py',
  handler: 'handler',
  runtime: lambda.Runtime.PYTHON_3_12,
  timeout: Duration.seconds(30),
  memorySize: 512,
});
```

### Lambda Layers

Share code across functions:

```typescript
const layer = new lambda.LayerVersion(this, 'CommonLayer', {
  code: lambda.Code.fromAsset('layers/common'),
  compatibleRuntimes: [lambda.Runtime.NODEJS_20_X],
  description: 'Common utilities',
});

new NodejsFunction(this, 'Function', {
  entry: 'src/handler.ts',
  layers: [layer],
});
```

## Testing Patterns

### Snapshot Testing

```typescript
import { Template } from 'aws-cdk-lib/assertions';

test('Stack creates expected resources', () => {
  const app = new cdk.App();
  const stack = new MyStack(app, 'TestStack');

  const template = Template.fromStack(stack);
  expect(template.toJSON()).toMatchSnapshot();
});
```

### Fine-Grained Assertions

```typescript
test('Lambda has correct environment', () => {
  const app = new cdk.App();
  const stack = new MyStack(app, 'TestStack');

  const template = Template.fromStack(stack);

  template.hasResourceProperties('AWS::Lambda::Function', {
    Runtime: 'nodejs20.x',
    Timeout: 30,
    Environment: {
      Variables: {
        TABLE_NAME: { Ref: Match.anyValue() },
      },
    },
  });
});
```

### Resource Count Validation

```typescript
test('Stack has correct number of functions', () => {
  const app = new cdk.App();
  const stack = new MyStack(app, 'TestStack');

  const template = Template.fromStack(stack);
  template.resourceCountIs('AWS::Lambda::Function', 3);
});
```

## Cost Optimization

### Right-Sizing Lambda

```typescript
// Development
const devFunction = new NodejsFunction(this, 'DevFunction', {
  memorySize: 256, // Lower for dev
  timeout: Duration.seconds(30),
});

// Production
const prodFunction = new NodejsFunction(this, 'ProdFunction', {
  memorySize: 1024, // Higher for prod performance
  timeout: Duration.seconds(10),
  reservedConcurrentExecutions: 10, // Prevent runaway costs
});
```

### DynamoDB Billing Modes

```typescript
// Development/Low Traffic
const devTable = new dynamodb.Table(this, 'DevTable', {
  billingMode: dynamodb.BillingMode.PAY_PER_REQUEST,
});

// Production/Predictable Load
const prodTable = new dynamodb.Table(this, 'ProdTable', {
  billingMode: dynamodb.BillingMode.PROVISIONED,
  readCapacity: 5,
  writeCapacity: 5,
  autoScaling: { /* ... */ },
});
```

### S3 Lifecycle Policies

```typescript
const bucket = new s3.Bucket(this, 'DataBucket', {
  lifecycleRules: [
    {
      id: 'MoveToIA',
      transitions: [
        {
          storageClass: s3.StorageClass.INFREQUENT_ACCESS,
          transitionAfter: Duration.days(30),
        },
        {
          storageClass: s3.StorageClass.GLACIER,
          transitionAfter: Duration.days(90),
        },
      ],
    },
    {
      id: 'CleanupOldVersions',
      noncurrentVersionExpiration: Duration.days(30),
    },
  ],
});
```

## Anti-Patterns

### ❌ Hardcoded Values

```typescript
// BAD
new lambda.Function(this, 'Function', {
  functionName: 'my-function', // Prevents multiple deployments
  code: lambda.Code.fromAsset('lambda'),
  handler: 'index.handler',
  runtime: lambda.Runtime.NODEJS_20_X,
});

// GOOD
new NodejsFunction(this, 'Function', {
  entry: 'src/handler.ts',
  // Let CDK generate the name
});
```

### ❌ Overly Broad IAM Permissions

```typescript
// BAD
function.addToRolePolicy(new iam.PolicyStatement({
  actions: ['*'],
  resources: ['*'],
}));

// GOOD
table.grantReadWriteData(function);
```

### ❌ Manual Dependency Management

```typescript
// BAD - Manual bundling
new lambda.Function(this, 'Function', {
  code: lambda.Code.fromAsset('lambda.zip'), // Pre-bundled manually
  // ...
});

// GOOD - Let CDK handle it
new NodejsFunction(this, 'Function', {
  entry: 'src/handler.ts',
  // CDK handles bundling automatically
});
```

### ❌ Missing Environment Variables

```typescript
// BAD
new NodejsFunction(this, 'Function', {
  entry: 'src/handler.ts',
  // Table name hardcoded in Lambda code
});

// GOOD
new NodejsFunction(this, 'Function', {
  entry: 'src/handler.ts',
  environment: {
    TABLE_NAME: table.tableName,
  },
});
```

### ❌ Ignoring Stack Outputs

```typescript
// BAD - No way to reference resources
new MyStack(app, 'Stack', {});

// GOOD - Export important values
class MyStack extends Stack {
  constructor(scope: Construct, id: string) {
    super(scope, id);

    const api = new apigateway.RestApi(this, 'Api', {});

    new CfnOutput(this, 'ApiUrl', {
      value: api.url,
      description: 'API Gateway URL',
      exportName: 'MyApiUrl',
    });
  }
}
```

## Summary

- **Always** let CDK generate resource names unless explicitly required
- **Use** high-level constructs (L2/L3) over low-level (L1)
- **Prefer** grant methods for IAM permissions
- **Leverage** `NodejsFunction` and `PythonFunction` for automatic bundling
- **Test** stacks with assertions and snapshots
- **Optimize** costs based on environment (dev vs prod)
- **Validate** infrastructure before deployment
- **Document** custom constructs and patterns
```

## File: `plugins/aws-cdk/skills/aws-cdk-development/scripts/validate-stack.sh`
```bash
#!/bin/bash

# AWS CDK Stack Validation Script
#
# This script performs meta-level validation of CDK stacks before deployment.
# Run this as part of pre-commit checks to ensure infrastructure quality.
#
# Focus areas:
# - CDK synthesis success validation
# - CloudFormation template size and resource count checks
# - Language detection and dependency verification
# - Integration with cdk-nag (recommended for comprehensive best practice checks)
#
# Supports CDK projects in multiple languages:
# - TypeScript/JavaScript (detects via package.json)
# - Python (detects via requirements.txt or setup.py)
# - Java (detects via pom.xml)
# - C# (detects via .csproj files)
# - Go (detects via go.mod)
#
# For comprehensive CDK best practice validation (IAM policies, security,
# naming conventions, etc.), use cdk-nag: https://github.com/cdklabs/cdk-nag
# cdk-nag provides suppression mechanisms and supports all CDK languages.

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "${SCRIPT_DIR}/../../.." && pwd)"

echo "🔍 AWS CDK Stack Validation"
echo "============================"
echo ""

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Track validation status
VALIDATION_PASSED=true

# Function to print success
success() {
    echo -e "${GREEN}✓${NC} $1"
}

# Function to print error
error() {
    echo -e "${RED}✗${NC} $1"
    VALIDATION_PASSED=false
}

# Function to print warning
warning() {
    echo -e "${YELLOW}⚠${NC} $1"
}

# Function to print info
info() {
    echo "ℹ $1"
}

# Check if cdk is installed
if ! command -v cdk &> /dev/null; then
    error "AWS CDK CLI not found. Install with: npm install -g aws-cdk"
    exit 1
fi

success "AWS CDK CLI found"

# Detect CDK project language
detect_language() {
    if [ -f "${PROJECT_ROOT}/package.json" ]; then
        echo "typescript"
    elif [ -f "${PROJECT_ROOT}/requirements.txt" ] || [ -f "${PROJECT_ROOT}/setup.py" ]; then
        echo "python"
    elif [ -f "${PROJECT_ROOT}/pom.xml" ]; then
        echo "java"
    elif [ -f "${PROJECT_ROOT}/cdk.csproj" ] || find "${PROJECT_ROOT}" -maxdepth 2 -name "*.csproj" -print -quit 2>/dev/null | grep -q .; then
        echo "csharp"
    elif [ -f "${PROJECT_ROOT}/go.mod" ]; then
        echo "go"
    else
        echo "unknown"
    fi
}

CDK_LANGUAGE=$(detect_language)

case "$CDK_LANGUAGE" in
    typescript)
        info "Detected TypeScript/JavaScript CDK project"
        success "package.json found"
        ;;
    python)
        info "Detected Python CDK project"
        success "requirements.txt or setup.py found"
        ;;
    java)
        info "Detected Java CDK project"
        success "pom.xml found"
        ;;
    csharp)
        info "Detected C# CDK project"
        success ".csproj file found"
        ;;
    go)
        info "Detected Go CDK project"
        success "go.mod found"
        ;;
    unknown)
        warning "Could not detect CDK project language"
        warning "Proceeding with generic validation only"
        ;;
esac

echo ""
info "Running CDK synthesis..."

# Synthesize stacks
if cdk synth --quiet > /dev/null 2>&1; then
    success "CDK synthesis successful"
else
    error "CDK synthesis failed"
    echo ""
    echo "Run 'cdk synth' for detailed error information"
    exit 1
fi

echo ""
info "Checking for cdk-nag integration..."

# Check if cdk-nag is being used for comprehensive validation
case "$CDK_LANGUAGE" in
    typescript)
        if grep -r "cdk-nag" "${PROJECT_ROOT}/package.json" 2>/dev/null | grep -q "."; then
            success "cdk-nag found in package.json"
        else
            warning "cdk-nag not found - recommended for comprehensive CDK validation"
            warning "Install with: npm install --save-dev cdk-nag"
            warning "See: https://github.com/cdklabs/cdk-nag"
        fi
        ;;
    python)
        if grep -r "cdk-nag" "${PROJECT_ROOT}/requirements.txt" 2>/dev/null | grep -q "."; then
            success "cdk-nag found in requirements.txt"
        elif grep -r "cdk-nag" "${PROJECT_ROOT}/setup.py" 2>/dev/null | grep -q "."; then
            success "cdk-nag found in setup.py"
        else
            warning "cdk-nag not found - recommended for comprehensive CDK validation"
            warning "Install with: pip install cdk-nag"
            warning "See: https://github.com/cdklabs/cdk-nag"
        fi
        ;;
    java)
        if grep -r "cdk-nag" "${PROJECT_ROOT}/pom.xml" 2>/dev/null | grep -q "."; then
            success "cdk-nag found in pom.xml"
        else
            warning "cdk-nag not found - recommended for comprehensive CDK validation"
            warning "See: https://github.com/cdklabs/cdk-nag"
        fi
        ;;
    csharp)
        if find "${PROJECT_ROOT}" -maxdepth 2 -name "*.csproj" -exec grep -l "CdkNag" {} \; 2>/dev/null | grep -q "."; then
            success "cdk-nag found in .csproj"
        else
            warning "cdk-nag not found - recommended for comprehensive CDK validation"
            warning "See: https://github.com/cdklabs/cdk-nag"
        fi
        ;;
    go)
        if grep -r "cdk-nag-go" "${PROJECT_ROOT}/go.mod" 2>/dev/null | grep -q "."; then
            success "cdk-nag-go found in go.mod"
        else
            warning "cdk-nag-go not found - recommended for comprehensive CDK validation"
            warning "See: https://github.com/cdklabs/cdk-nag-go"
        fi
        ;;
esac

success "Integration checks completed"

echo ""
info "💡 Note: This script focuses on template and meta-level validation."
info "For comprehensive CDK best practice checks (IAM, security, naming, etc.),"
info "use cdk-nag: https://github.com/cdklabs/cdk-nag"

echo ""
info "Checking synthesized templates..."

# Get list of synthesized templates
TEMPLATES=()
while IFS= read -r -d '' file; do
    TEMPLATES+=("$file")
done < <(find "${PROJECT_ROOT}/cdk.out" -name "*.template.json" -print0 2>/dev/null)

if [ ${#TEMPLATES[@]} -eq 0 ]; then
    error "No CloudFormation templates found in cdk.out/"
    exit 1
fi

success "Found ${#TEMPLATES[@]} CloudFormation template(s)"

# Validate each template
for template in "${TEMPLATES[@]}"; do
    STACK_NAME="$(basename "$template" .template.json)"

    # Check template size
    TEMPLATE_SIZE="$(wc -c < "$template")"
    MAX_SIZE=51200 # 50KB warning threshold

    if [ "$TEMPLATE_SIZE" -gt "$MAX_SIZE" ]; then
        warning "${STACK_NAME}: Template size (${TEMPLATE_SIZE} bytes) is large"
        warning "Consider using nested stacks to reduce size"
    fi

    # Count resources
    RESOURCE_COUNT="$(jq '.Resources | length' "$template" 2>/dev/null || echo 0)"

    if [ "$RESOURCE_COUNT" -gt 200 ]; then
        warning "${STACK_NAME}: High resource count (${RESOURCE_COUNT})"
        warning "Consider splitting into multiple stacks"
    else
        success "${STACK_NAME}: ${RESOURCE_COUNT} resources"
    fi
done

echo ""
echo "============================"

if [ "$VALIDATION_PASSED" = true ]; then
    echo -e "${GREEN}✓ Validation passed${NC}"
    echo ""
    info "Stack is ready for deployment"
    exit 0
else
    echo -e "${RED}✗ Validation failed${NC}"
    echo ""
    error "Please fix the errors above before deploying"
    exit 1
fi
```

## File: `plugins/aws-common/skills/aws-mcp-setup/SKILL.md`
```markdown
---
name: aws-mcp-setup
description: Configure AWS MCP servers for documentation search and API access. Use when setting up AWS MCP, configuring AWS documentation tools, troubleshooting MCP connectivity, or when user mentions aws-mcp, awsdocs, uvx setup, or MCP server configuration. Covers both Full AWS MCP Server (with uvx + credentials) and lightweight Documentation MCP (no auth required).
allowed-tools:
  - Bash(which *)
  - Bash(aws sts get-caller-identity*)
  - Bash(claude mcp *)
  - Bash(cat *mcp.json*)
  - Bash(cat *claude.json*)
---

# AWS MCP Server Configuration Guide

## Overview

This guide helps you configure AWS MCP tools for AI agents. Two options are available:

| Option | Requirements | Capabilities |
|--------|--------------|--------------|
| **Full AWS MCP Server** | Python 3.10+, uvx, AWS credentials | Execute AWS API calls + documentation search |
| **AWS Documentation MCP** | None | Documentation search only |

## Step 1: Check Existing Configuration

Before configuring, check if AWS MCP tools are already available using either method:

### Method A: Check Available Tools (Recommended)

Look for these tool name patterns in your agent's available tools:
- `mcp__aws-mcp__*` or `mcp__aws__*` → Full AWS MCP Server configured
- `mcp__*awsdocs*__aws___*` → AWS Documentation MCP configured

**How to check**: Run `/mcp` command to list all active MCP servers.

### Method B: Check Configuration Files

Agent tools use hierarchical configuration (precedence: local → project → user → enterprise):

| Scope | File Location | Use Case |
|-------|---------------|----------|
| Local | `.claude.json` (in project) | Personal/experimental |
| Project | `.mcp.json` (project root) | Team-shared |
| User | `~/.claude.json` | Cross-project personal |
| Enterprise | System managed directories | Organization-wide |

Check these files for `mcpServers` containing `aws-mcp`, `aws`, or `awsdocs` keys:

```bash
# Check project config
cat .mcp.json 2>/dev/null | grep -E '"(aws-mcp|aws|awsdocs)"'

# Check user config
cat ~/.claude.json 2>/dev/null | grep -E '"(aws-mcp|aws|awsdocs)"'

# Or use Claude CLI
claude mcp list
```

If AWS MCP is already configured, no further setup needed.

## Step 2: Choose Configuration Method

### Automatic Detection

Run these commands to determine which option to use:

```bash
# Check for uvx (requires Python 3.10+)
which uvx || echo "uvx not available"

# Check for valid AWS credentials
aws sts get-caller-identity || echo "AWS credentials not configured"
```

### Option A: Full AWS MCP Server (Recommended)

**Use when**: uvx available AND AWS credentials valid

**Prerequisites**:
- Python 3.10+ with `uv` package manager
- AWS credentials configured (via profile, environment variables, or IAM role)

**Required IAM Permissions**:
```json
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow",
    "Action": [
      "aws-mcp:InvokeMCP",
      "aws-mcp:CallReadOnlyTool",
      "aws-mcp:CallReadWriteTool"
    ],
    "Resource": "*"
  }]
}
```

**Configuration** (add to your MCP settings):
```json
{
  "mcpServers": {
    "aws-mcp": {
      "command": "uvx",
      "args": [
        "mcp-proxy-for-aws@latest",
        "https://aws-mcp.us-east-1.api.aws/mcp",
        "--metadata", "AWS_REGION=us-west-2"
      ]
    }
  }
}
```

**Credential Configuration Options**:

1. **AWS Profile** (recommended for development):
   ```json
   "args": [
     "mcp-proxy-for-aws@latest",
     "https://aws-mcp.us-east-1.api.aws/mcp",
     "--profile", "my-profile",
     "--metadata", "AWS_REGION=us-west-2"
   ]
   ```

2. **Environment Variables**:
   ```json
   "env": {
     "AWS_ACCESS_KEY_ID": "...",
     "AWS_SECRET_ACCESS_KEY": "...",
     "AWS_REGION": "us-west-2"
   }
   ```

3. **IAM Role** (for EC2/ECS/Lambda): No additional config needed - uses instance credentials

**Additional Options**:
- `--region <region>`: Override AWS region
- `--read-only`: Restrict to read-only tools
- `--log-level <level>`: Set logging level (debug, info, warning, error)

**Reference**: https://github.com/aws/mcp-proxy-for-aws

### Option B: AWS Documentation MCP Server (No Auth)

**Use when**:
- No Python/uvx environment
- No AWS credentials
- Only need documentation search (no API execution)

**Configuration**:
```json
{
  "mcpServers": {
    "awsdocs": {
      "type": "http",
      "url": "https://knowledge-mcp.global.api.aws"
    }
  }
}
```

## Step 3: Verification

After configuration, verify tools are available:

**For Full AWS MCP**:
- Look for tools: `mcp__aws-mcp__aws___search_documentation`, `mcp__aws-mcp__aws___call_aws`

**For Documentation MCP**:
- Look for tools: `mcp__awsdocs__aws___search_documentation`, `mcp__awsdocs__aws___read_documentation`

## Troubleshooting

| Issue | Cause | Solution |
|-------|-------|----------|
| `uvx: command not found` | uv not installed | Install with `pip install uv` or use Option B |
| `AccessDenied` error | Missing IAM permissions | Add aws-mcp:* permissions to IAM policy |
| `InvalidSignatureException` | Credential issue | Check `aws sts get-caller-identity` |
| Tools not appearing | MCP not started | Restart your agent after config change |
```

## File: `plugins/aws-cost-ops/skills/aws-cost-operations/SKILL.md`
```markdown
---
name: aws-cost-operations
description: AWS cost optimization, monitoring, and operational excellence expert. Use when analyzing AWS bills, estimating costs, setting up CloudWatch alarms, querying logs, auditing CloudTrail activity, or assessing security posture. Essential when user mentions AWS costs, spending, billing, budget, pricing, CloudWatch, observability, monitoring, alerting, CloudTrail, audit, or wants to optimize AWS infrastructure costs and operational efficiency.
context: fork
skills:
  - aws-mcp-setup
allowed-tools:
  - mcp__pricing__*
  - mcp__costexp__*
  - mcp__cw__*
  - mcp__aws-mcp__*
  - mcp__awsdocs__*
  - Bash(aws ce *)
  - Bash(aws cloudwatch *)
  - Bash(aws logs *)
  - Bash(aws budgets *)
  - Bash(aws cloudtrail *)
  - Bash(aws sts get-caller-identity)
hooks:
  PreToolUse:
    - matcher: Bash(aws ce *)
      command: aws sts get-caller-identity --query Account --output text
      once: true
---

# AWS Cost & Operations

This skill provides comprehensive guidance for AWS cost optimization, monitoring, observability, and operational excellence with integrated MCP servers.

## AWS Documentation Requirement

Always verify AWS facts using MCP tools (`mcp__aws-mcp__*` or `mcp__*awsdocs*__*`) before answering. The `aws-mcp-setup` dependency is auto-loaded — if MCP tools are unavailable, guide the user through that skill's setup flow.

## Integrated MCP Servers

This plugin provides 3 MCP servers:

### Bundled Servers

#### 1. AWS Pricing MCP Server (`pricing`)
**Purpose**: Pre-deployment cost estimation and optimization
- Estimate costs before deploying resources
- Compare pricing across regions
- Calculate Total Cost of Ownership (TCO)
- Evaluate different service options for cost efficiency

#### 2. AWS Cost Explorer MCP Server (`costexp`)
**Purpose**: Detailed cost analysis and reporting
- Analyze historical spending patterns
- Identify cost anomalies and trends
- Forecast future costs
- Analyze cost by service, region, or tag

#### 3. Amazon CloudWatch MCP Server (`cw`)
**Purpose**: Metrics, alarms, and logs analysis
- Query CloudWatch metrics and logs
- Create and manage CloudWatch alarms
- Troubleshoot operational issues
- Monitor resource utilization

> **Note**: The following servers are available separately via the Full AWS MCP Server (see `aws-mcp-setup` skill) and are not bundled with this plugin:
> - AWS Billing and Cost Management MCP — Real-time billing details
> - CloudWatch Application Signals MCP — APM and SLOs
> - AWS Managed Prometheus MCP — PromQL queries for containers
> - AWS CloudTrail MCP — API activity audit
> - AWS Well-Architected Security Assessment MCP — Security posture assessment

## When to Use This Skill

Use this skill when:
- Optimizing AWS costs and reducing spending
- Estimating costs before deployment
- Monitoring application and infrastructure performance
- Setting up observability and alerting
- Analyzing spending patterns and trends
- Investigating operational issues
- Auditing AWS activity and changes
- Assessing security posture
- Implementing operational excellence

## Cost Optimization Best Practices

### Pre-Deployment Cost Estimation

**Always estimate costs before deploying**:
1. Use **AWS Pricing MCP** to estimate resource costs
2. Compare pricing across different regions
3. Evaluate alternative service options
4. Calculate expected monthly costs
5. Plan for scaling and growth

**Example workflow**:
```
"Estimate the monthly cost of running a Lambda function with
1 million invocations, 512MB memory, 3-second duration in us-east-1"
```

### Cost Analysis and Optimization

**Regular cost reviews**:
1. Use **Cost Explorer MCP** to analyze spending trends
2. Identify cost anomalies and unexpected charges
3. Review costs by service, region, and environment
4. Compare actual vs. budgeted costs
5. Generate cost optimization recommendations

**Cost optimization strategies**:
- Right-size over-provisioned resources
- Use appropriate storage classes (S3, EBS)
- Implement auto-scaling for dynamic workloads
- Leverage Savings Plans and Reserved Instances
- Delete unused resources and snapshots
- Use cost allocation tags effectively

### Budget Monitoring

**Track spending against budgets**:
1. Use **Billing and Cost Management MCP** to monitor budgets
2. Set up budget alerts for threshold breaches
3. Review budget utilization regularly
4. Adjust budgets based on trends
5. Implement cost controls and governance

## Monitoring and Observability Best Practices

### CloudWatch Metrics and Alarms

**Implement comprehensive monitoring**:
1. Use **CloudWatch MCP** to query metrics and logs
2. Set up alarms for critical metrics:
   - CPU and memory utilization
   - Error rates and latency
   - Queue depths and processing times
   - API gateway throttling
   - Lambda errors and timeouts
3. Create CloudWatch dashboards for visualization
4. Use log insights for troubleshooting

**Example alarm scenarios**:
- Lambda error rate > 1%
- EC2 CPU utilization > 80%
- API Gateway 4xx/5xx error spike
- DynamoDB throttled requests
- ECS task failures

### Application Performance Monitoring

**Monitor application health**:
1. Use **CloudWatch Application Signals MCP** for APM
2. Track service-level objectives (SLOs)
3. Monitor application dependencies
4. Identify performance bottlenecks
5. Set up distributed tracing

### Container and Kubernetes Monitoring

**For containerized workloads**:
1. Use **AWS Managed Prometheus MCP** for metrics
2. Monitor container resource utilization
3. Track pod and node health
4. Create PromQL queries for custom metrics
5. Set up alerts for container anomalies

## Audit and Security Best Practices

### CloudTrail Activity Analysis

**Audit AWS activity**:
1. Use **CloudTrail MCP** to analyze API activity
2. Track who made changes to resources
3. Investigate security incidents
4. Monitor for suspicious activity patterns
5. Audit compliance with policies

**Common audit scenarios**:
- "Who deleted this S3 bucket?"
- "Show all IAM role changes in the last 24 hours"
- "List failed login attempts"
- "Find all actions by a specific user"
- "Track modifications to security groups"

### Security Assessment

**Regular security reviews**:
1. Use **Well-Architected Security Assessment MCP**
2. Assess security posture against best practices
3. Identify security gaps and vulnerabilities
4. Implement recommended security improvements
5. Document security compliance

**Security assessment areas**:
- Identity and Access Management (IAM)
- Detective controls and monitoring
- Infrastructure protection
- Data protection and encryption
- Incident response preparedness

## Using MCP Servers Effectively

### Cost Analysis Workflow

1. **Pre-deployment**: Use Pricing MCP to estimate costs
2. **Post-deployment**: Use Billing MCP to track actual spending
3. **Analysis**: Use Cost Explorer MCP for detailed cost analysis
4. **Optimization**: Implement recommendations from Cost Explorer

### Monitoring Workflow

1. **Setup**: Configure CloudWatch metrics and alarms
2. **Monitor**: Use CloudWatch MCP to track key metrics
3. **Analyze**: Use Application Signals for APM insights
4. **Troubleshoot**: Query CloudWatch Logs for issue resolution

### Security Workflow

1. **Audit**: Use CloudTrail MCP to review activity
2. **Assess**: Use Well-Architected Security Assessment
3. **Remediate**: Implement security recommendations
4. **Monitor**: Track security events via CloudWatch

### MCP Usage Best Practices

1. **Cost Awareness**: Check pricing before deploying resources
2. **Proactive Monitoring**: Set up alarms for critical metrics
3. **Regular Reviews**: Analyze costs and performance weekly
4. **Audit Trails**: Review CloudTrail logs for compliance
5. **Security First**: Run security assessments regularly
6. **Optimize Continuously**: Act on cost and performance recommendations

## Operational Excellence Guidelines

### Cost Optimization

- **Tag Everything**: Use consistent cost allocation tags
- **Review Monthly**: Analyze spending trends and anomalies
- **Right-size**: Match resources to actual usage
- **Automate**: Use auto-scaling and scheduling
- **Monitor Budgets**: Set alerts for cost overruns

### Monitoring and Alerting

- **Critical Metrics**: Alert on business-critical metrics
- **Noise Reduction**: Fine-tune thresholds to reduce false positives
- **Actionable Alerts**: Ensure alerts have clear remediation steps
- **Dashboard Visibility**: Create dashboards for key stakeholders
- **Log Retention**: Balance cost and compliance needs

### Security and Compliance

- **Least Privilege**: Grant minimum required permissions
- **Audit Regularly**: Review CloudTrail logs for anomalies
- **Encrypt Data**: Use encryption at rest and in transit
- **Assess Continuously**: Run security assessments frequently
- **Incident Response**: Have procedures for security events

## Additional Resources

For detailed operational patterns and best practices, refer to the comprehensive reference:

**File**: `references/operations-patterns.md`

This reference includes:
- Cost optimization strategies
- Monitoring and alerting patterns
- Observability best practices
- Security and compliance guidelines
- Troubleshooting workflows

## CloudWatch Alarms Reference

**File**: `references/cloudwatch-alarms.md`

Common alarm configurations for:
- Lambda functions
- EC2 instances
- RDS databases
- DynamoDB tables
- API Gateway
- ECS services
- Application Load Balancers
```

## File: `plugins/aws-cost-ops/skills/aws-cost-operations/references/cloudwatch-alarms.md`
```markdown
# CloudWatch Alarms Reference

Common CloudWatch alarm configurations for AWS services.

## Lambda Functions

### Error Rate Alarm
```typescript
new cloudwatch.Alarm(this, 'LambdaErrorAlarm', {
  metric: lambdaFunction.metricErrors({
    statistic: 'Sum',
    period: Duration.minutes(5),
  }),
  threshold: 10,
  evaluationPeriods: 1,
  treatMissingData: cloudwatch.TreatMissingData.NOT_BREACHING,
  alarmDescription: 'Lambda error count exceeded threshold',
});
```

### Duration Alarm (Approaching Timeout)
```typescript
new cloudwatch.Alarm(this, 'LambdaDurationAlarm', {
  metric: lambdaFunction.metricDuration({
    statistic: 'Maximum',
    period: Duration.minutes(5),
  }),
  threshold: lambdaFunction.timeout.toMilliseconds() * 0.8, // 80% of timeout
  evaluationPeriods: 2,
  alarmDescription: 'Lambda duration approaching timeout',
});
```

### Throttle Alarm
```typescript
new cloudwatch.Alarm(this, 'LambdaThrottleAlarm', {
  metric: lambdaFunction.metricThrottles({
    statistic: 'Sum',
    period: Duration.minutes(5),
  }),
  threshold: 5,
  evaluationPeriods: 1,
  alarmDescription: 'Lambda function is being throttled',
});
```

### Concurrent Executions Alarm
```typescript
new cloudwatch.Alarm(this, 'LambdaConcurrencyAlarm', {
  metric: new cloudwatch.Metric({
    namespace: 'AWS/Lambda',
    metricName: 'ConcurrentExecutions',
    dimensionsMap: {
      FunctionName: lambdaFunction.functionName,
    },
    statistic: 'Maximum',
    period: Duration.minutes(1),
  }),
  threshold: 100, // Adjust based on reserved concurrency
  evaluationPeriods: 2,
  alarmDescription: 'Lambda concurrent executions high',
});
```

## API Gateway

### 5XX Error Rate Alarm
```typescript
new cloudwatch.Alarm(this, 'Api5xxAlarm', {
  metric: api.metricServerError({
    statistic: 'Sum',
    period: Duration.minutes(5),
  }),
  threshold: 10,
  evaluationPeriods: 1,
  alarmDescription: 'API Gateway 5XX errors exceeded threshold',
});
```

### 4XX Error Rate Alarm
```typescript
new cloudwatch.Alarm(this, 'Api4xxAlarm', {
  metric: api.metricClientError({
    statistic: 'Sum',
    period: Duration.minutes(5),
  }),
  threshold: 50,
  evaluationPeriods: 2,
  alarmDescription: 'API Gateway 4XX errors exceeded threshold',
});
```

### Latency Alarm
```typescript
new cloudwatch.Alarm(this, 'ApiLatencyAlarm', {
  metric: api.metricLatency({
    statistic: 'p99',
    period: Duration.minutes(5),
  }),
  threshold: 2000, // 2 seconds
  evaluationPeriods: 2,
  alarmDescription: 'API Gateway p99 latency exceeded threshold',
});
```

## DynamoDB

### Read Throttle Alarm
```typescript
new cloudwatch.Alarm(this, 'DynamoDBReadThrottleAlarm', {
  metric: table.metricUserErrors({
    dimensions: {
      Operation: 'GetItem',
    },
    statistic: 'Sum',
    period: Duration.minutes(5),
  }),
  threshold: 5,
  evaluationPeriods: 1,
  alarmDescription: 'DynamoDB read operations being throttled',
});
```

### Write Throttle Alarm
```typescript
new cloudwatch.Alarm(this, 'DynamoDBWriteThrottleAlarm', {
  metric: table.metricUserErrors({
    dimensions: {
      Operation: 'PutItem',
    },
    statistic: 'Sum',
    period: Duration.minutes(5),
  }),
  threshold: 5,
  evaluationPeriods: 1,
  alarmDescription: 'DynamoDB write operations being throttled',
});
```

### Consumed Capacity Alarm
```typescript
new cloudwatch.Alarm(this, 'DynamoDBCapacityAlarm', {
  metric: table.metricConsumedReadCapacityUnits({
    statistic: 'Sum',
    period: Duration.minutes(5),
  }),
  threshold: provisionedCapacity * 0.8, // 80% of provisioned
  evaluationPeriods: 2,
  alarmDescription: 'DynamoDB consumed capacity approaching limit',
});
```

## EC2 Instances

### CPU Utilization Alarm
```typescript
new cloudwatch.Alarm(this, 'EC2CpuAlarm', {
  metric: new cloudwatch.Metric({
    namespace: 'AWS/EC2',
    metricName: 'CPUUtilization',
    dimensionsMap: {
      InstanceId: instance.instanceId,
    },
    statistic: 'Average',
    period: Duration.minutes(5),
  }),
  threshold: 80,
  evaluationPeriods: 3,
  alarmDescription: 'EC2 CPU utilization high',
});
```

### Status Check Failed Alarm
```typescript
new cloudwatch.Alarm(this, 'EC2StatusCheckAlarm', {
  metric: new cloudwatch.Metric({
    namespace: 'AWS/EC2',
    metricName: 'StatusCheckFailed',
    dimensionsMap: {
      InstanceId: instance.instanceId,
    },
    statistic: 'Maximum',
    period: Duration.minutes(1),
  }),
  threshold: 1,
  evaluationPeriods: 2,
  alarmDescription: 'EC2 status check failed',
});
```

### Disk Space Alarm (Requires CloudWatch Agent)
```typescript
new cloudwatch.Alarm(this, 'EC2DiskAlarm', {
  metric: new cloudwatch.Metric({
    namespace: 'CWAgent',
    metricName: 'disk_used_percent',
    dimensionsMap: {
      InstanceId: instance.instanceId,
      path: '/',
    },
    statistic: 'Average',
    period: Duration.minutes(5),
  }),
  threshold: 85,
  evaluationPeriods: 2,
  alarmDescription: 'EC2 disk space usage high',
});
```

## RDS Databases

### CPU Alarm
```typescript
new cloudwatch.Alarm(this, 'RDSCpuAlarm', {
  metric: new cloudwatch.Metric({
    namespace: 'AWS/RDS',
    metricName: 'CPUUtilization',
    dimensionsMap: {
      DBInstanceIdentifier: dbInstance.instanceIdentifier,
    },
    statistic: 'Average',
    period: Duration.minutes(5),
  }),
  threshold: 80,
  evaluationPeriods: 3,
  alarmDescription: 'RDS CPU utilization high',
});
```

### Connection Count Alarm
```typescript
new cloudwatch.Alarm(this, 'RDSConnectionAlarm', {
  metric: new cloudwatch.Metric({
    namespace: 'AWS/RDS',
    metricName: 'DatabaseConnections',
    dimensionsMap: {
      DBInstanceIdentifier: dbInstance.instanceIdentifier,
    },
    statistic: 'Average',
    period: Duration.minutes(5),
  }),
  threshold: maxConnections * 0.8, // 80% of max connections
  evaluationPeriods: 2,
  alarmDescription: 'RDS connection count approaching limit',
});
```

### Free Storage Space Alarm
```typescript
new cloudwatch.Alarm(this, 'RDSStorageAlarm', {
  metric: new cloudwatch.Metric({
    namespace: 'AWS/RDS',
    metricName: 'FreeStorageSpace',
    dimensionsMap: {
      DBInstanceIdentifier: dbInstance.instanceIdentifier,
    },
    statistic: 'Average',
    period: Duration.minutes(5),
  }),
  threshold: 10 * 1024 * 1024 * 1024, // 10 GB in bytes
  comparisonOperator: cloudwatch.ComparisonOperator.LESS_THAN_THRESHOLD,
  evaluationPeriods: 1,
  alarmDescription: 'RDS free storage space low',
});
```

## ECS Services

### Task Count Alarm
```typescript
new cloudwatch.Alarm(this, 'ECSTaskCountAlarm', {
  metric: new cloudwatch.Metric({
    namespace: 'ECS/ContainerInsights',
    metricName: 'RunningTaskCount',
    dimensionsMap: {
      ServiceName: service.serviceName,
      ClusterName: cluster.clusterName,
    },
    statistic: 'Average',
    period: Duration.minutes(5),
  }),
  threshold: 1,
  comparisonOperator: cloudwatch.ComparisonOperator.LESS_THAN_THRESHOLD,
  evaluationPeriods: 2,
  alarmDescription: 'ECS service has no running tasks',
});
```

### CPU Utilization Alarm
```typescript
new cloudwatch.Alarm(this, 'ECSCpuAlarm', {
  metric: new cloudwatch.Metric({
    namespace: 'AWS/ECS',
    metricName: 'CPUUtilization',
    dimensionsMap: {
      ServiceName: service.serviceName,
      ClusterName: cluster.clusterName,
    },
    statistic: 'Average',
    period: Duration.minutes(5),
  }),
  threshold: 80,
  evaluationPeriods: 3,
  alarmDescription: 'ECS service CPU utilization high',
});
```

### Memory Utilization Alarm
```typescript
new cloudwatch.Alarm(this, 'ECSMemoryAlarm', {
  metric: new cloudwatch.Metric({
    namespace: 'AWS/ECS',
    metricName: 'MemoryUtilization',
    dimensionsMap: {
      ServiceName: service.serviceName,
      ClusterName: cluster.clusterName,
    },
    statistic: 'Average',
    period: Duration.minutes(5),
  }),
  threshold: 85,
  evaluationPeriods: 2,
  alarmDescription: 'ECS service memory utilization high',
});
```

## SQS Queues

### Queue Depth Alarm
```typescript
new cloudwatch.Alarm(this, 'SQSDepthAlarm', {
  metric: queue.metricApproximateNumberOfMessagesVisible({
    statistic: 'Maximum',
    period: Duration.minutes(5),
  }),
  threshold: 1000,
  evaluationPeriods: 2,
  alarmDescription: 'SQS queue depth exceeded threshold',
});
```

### Age of Oldest Message Alarm
```typescript
new cloudwatch.Alarm(this, 'SQSAgeAlarm', {
  metric: queue.metricApproximateAgeOfOldestMessage({
    statistic: 'Maximum',
    period: Duration.minutes(5),
  }),
  threshold: 300, // 5 minutes in seconds
  evaluationPeriods: 1,
  alarmDescription: 'SQS messages not being processed timely',
});
```

## Application Load Balancer

### Target Health Alarm
```typescript
new cloudwatch.Alarm(this, 'ALBUnhealthyTargetAlarm', {
  metric: new cloudwatch.Metric({
    namespace: 'AWS/ApplicationELB',
    metricName: 'UnHealthyHostCount',
    dimensionsMap: {
      LoadBalancer: loadBalancer.loadBalancerFullName,
      TargetGroup: targetGroup.targetGroupFullName,
    },
    statistic: 'Average',
    period: Duration.minutes(5),
  }),
  threshold: 1,
  evaluationPeriods: 2,
  alarmDescription: 'ALB has unhealthy targets',
});
```

### HTTP 5XX Alarm
```typescript
new cloudwatch.Alarm(this, 'ALB5xxAlarm', {
  metric: new cloudwatch.Metric({
    namespace: 'AWS/ApplicationELB',
    metricName: 'HTTPCode_Target_5XX_Count',
    dimensionsMap: {
      LoadBalancer: loadBalancer.loadBalancerFullName,
    },
    statistic: 'Sum',
    period: Duration.minutes(5),
  }),
  threshold: 10,
  evaluationPeriods: 1,
  alarmDescription: 'ALB target 5XX errors exceeded threshold',
});
```

### Response Time Alarm
```typescript
new cloudwatch.Alarm(this, 'ALBLatencyAlarm', {
  metric: new cloudwatch.Metric({
    namespace: 'AWS/ApplicationELB',
    metricName: 'TargetResponseTime',
    dimensionsMap: {
      LoadBalancer: loadBalancer.loadBalancerFullName,
    },
    statistic: 'p99',
    period: Duration.minutes(5),
  }),
  threshold: 1, // 1 second
  evaluationPeriods: 2,
  alarmDescription: 'ALB p99 response time exceeded threshold',
});
```

## Composite Alarms

### Service Health Composite Alarm
```typescript
const errorAlarm = new cloudwatch.Alarm(this, 'ErrorAlarm', { /* ... */ });
const latencyAlarm = new cloudwatch.Alarm(this, 'LatencyAlarm', { /* ... */ });
const throttleAlarm = new cloudwatch.Alarm(this, 'ThrottleAlarm', { /* ... */ });

new cloudwatch.CompositeAlarm(this, 'ServiceHealthAlarm', {
  compositeAlarmName: 'service-health',
  alarmRule: cloudwatch.AlarmRule.anyOf(
    errorAlarm,
    latencyAlarm,
    throttleAlarm
  ),
  alarmDescription: 'Overall service health degraded',
});
```

## Alarm Actions

### SNS Topic Integration
```typescript
const topic = new sns.Topic(this, 'AlarmTopic', {
  displayName: 'CloudWatch Alarms',
});

// Email subscription
topic.addSubscription(new subscriptions.EmailSubscription('ops@example.com'));

// Add action to alarm
alarm.addAlarmAction(new actions.SnsAction(topic));
alarm.addOkAction(new actions.SnsAction(topic));
```

### Auto Scaling Action
```typescript
const scalingAction = targetGroup.scaleOnMetric('ScaleUp', {
  metric: targetGroup.metricTargetResponseTime(),
  scalingSteps: [
    { upper: 1, change: 0 },
    { lower: 1, change: +1 },
    { lower: 2, change: +2 },
  ],
});
```

## Alarm Best Practices

### Threshold Selection

**CPU/Memory Alarms**:
- Warning: 70-80%
- Critical: 80-90%
- Consider burst patterns and normal usage

**Error Rate Alarms**:
- Threshold based on SLA (e.g., 99.9% = 0.1% error rate)
- Account for normal error rates
- Different thresholds for different error types

**Latency Alarms**:
- p99 latency for user-facing APIs
- Warning: 80% of SLA target
- Critical: 100% of SLA target

### Evaluation Periods

**Fast-changing metrics** (1-2 periods):
- Error counts
- Failed health checks
- Critical application errors

**Slow-changing metrics** (3-5 periods):
- CPU utilization
- Memory usage
- Disk usage

**Cost-related metrics** (longer periods):
- Daily spending
- Resource count changes
- Usage patterns

### Missing Data Handling

```typescript
// For intermittent workloads
alarm.treatMissingData(cloudwatch.TreatMissingData.NOT_BREACHING);

// For always-on services
alarm.treatMissingData(cloudwatch.TreatMissingData.BREACHING);

// To distinguish from data issues
alarm.treatMissingData(cloudwatch.TreatMissingData.MISSING);
```

### Alarm Naming Conventions

```typescript
// Pattern: <service>-<metric>-<severity>
'lambda-errors-critical'
'api-latency-warning'
'rds-cpu-warning'
'ecs-tasks-critical'
```

### Alarm Actions Best Practices

1. **Separate topics by severity**:
   - Critical alarms → PagerDuty/on-call
   - Warning alarms → Slack/email
   - Info alarms → Metrics dashboard

2. **Include context in alarm description**:
   - Service name
   - Expected threshold
   - Troubleshooting runbook link

3. **Auto-remediation where possible**:
   - Lambda errors → automatic retry
   - CPU high → auto-scaling trigger
   - Disk full → automated cleanup

4. **Alarm fatigue prevention**:
   - Tune thresholds based on actual patterns
   - Use composite alarms to reduce noise
   - Implement proper evaluation periods
   - Regularly review and adjust alarms

## Monitoring Dashboard

### Recommended Dashboard Layout

**Service Overview**:
- Request count and rate
- Error count and percentage
- Latency (p50, p95, p99)
- Availability percentage

**Resource Utilization**:
- CPU utilization by service
- Memory utilization by service
- Network throughput
- Disk I/O

**Cost Metrics**:
- Daily spending by service
- Month-to-date costs
- Budget utilization
- Cost anomalies

**Security Metrics**:
- Failed login attempts
- IAM policy changes
- Security group modifications
- GuardDuty findings
```

## File: `plugins/aws-cost-ops/skills/aws-cost-operations/references/operations-patterns.md`
```markdown
# AWS Cost & Operations Patterns

Comprehensive patterns and best practices for AWS cost optimization, monitoring, and operational excellence.

## Table of Contents

- [Cost Optimization Patterns](#cost-optimization-patterns)
- [Monitoring Patterns](#monitoring-patterns)
- [Observability Patterns](#observability-patterns)
- [Security and Audit Patterns](#security-and-audit-patterns)
- [Troubleshooting Workflows](#troubleshooting-workflows)

## Cost Optimization Patterns

### Pattern 1: Cost Estimation Before Deployment

**When**: Before deploying any new infrastructure

**MCP Server**: AWS Pricing MCP

**Steps**:
1. List all resources to be deployed
2. Query pricing for each resource type
3. Calculate monthly costs based on expected usage
4. Compare pricing across regions
5. Document cost estimates in architecture docs

**Example**:
```
Resource: Lambda Function
- Invocations: 1,000,000/month
- Duration: 3 seconds avg
- Memory: 512 MB
- Region: us-east-1
Estimated cost: $X/month
```

### Pattern 2: Monthly Cost Review

**When**: First week of every month

**MCP Servers**: Cost Explorer MCP, Billing and Cost Management MCP

**Steps**:
1. Review total spending vs. budget
2. Analyze cost by service (top 5 services)
3. Identify cost anomalies (>20% increase)
4. Review cost by environment (dev/staging/prod)
5. Check cost allocation tag coverage
6. Generate cost optimization recommendations

**Key Metrics**:
- Month-over-month cost change
- Cost per environment
- Cost per application/project
- Untagged resource costs

### Pattern 3: Right-Sizing Resources

**When**: Quarterly or when utilization alerts trigger

**MCP Servers**: CloudWatch MCP, Cost Explorer MCP

**Steps**:
1. Query CloudWatch for resource utilization metrics
2. Identify over-provisioned resources (< 40% utilization)
3. Identify under-provisioned resources (> 80% utilization)
4. Calculate potential savings from right-sizing
5. Plan and execute right-sizing changes
6. Monitor post-change performance

**Common Right-Sizing Scenarios**:
- EC2 instances with low CPU utilization
- RDS instances with excess capacity
- DynamoDB tables with low read/write usage
- Lambda functions with excessive memory allocation

### Pattern 4: Unused Resource Cleanup

**When**: Monthly or triggered by cost anomalies

**MCP Servers**: Cost Explorer MCP, CloudTrail MCP

**Steps**:
1. Identify resources with zero usage
2. Query CloudTrail for last access time
3. Tag resources for deletion review
4. Notify resource owners
5. Delete confirmed unused resources
6. Track cost savings

**Common Unused Resources**:
- Unattached EBS volumes
- Old EBS snapshots
- Idle Load Balancers
- Unused Elastic IPs
- Old AMIs and snapshots
- Stopped EC2 instances (long-term)

## Monitoring Patterns

### Pattern 1: Critical Service Monitoring

**When**: All production services

**MCP Server**: CloudWatch MCP

**Metrics to Monitor**:
- **Availability**: Service uptime, health checks
- **Performance**: Latency, response time
- **Errors**: Error rate, failed requests
- **Saturation**: CPU, memory, disk, network utilization

**Alarm Thresholds** (adjust based on SLAs):
- Error rate: > 1% for 2 consecutive periods
- Latency: p99 > 1 second for 5 minutes
- CPU: > 80% for 10 minutes
- Memory: > 85% for 5 minutes

### Pattern 2: Lambda Function Monitoring

**MCP Server**: CloudWatch MCP

**Key Metrics**:
```
- Invocations (Count)
- Errors (Count, %)
- Duration (Average, p99)
- Throttles (Count)
- ConcurrentExecutions (Max)
- IteratorAge (for stream processing)
```

**Recommended Alarms**:
- Error rate > 1%
- Duration > 80% of timeout
- Throttles > 0
- ConcurrentExecutions > 80% of reserved

### Pattern 3: API Gateway Monitoring

**MCP Server**: CloudWatch MCP

**Key Metrics**:
```
- Count (Total requests)
- 4XXError, 5XXError
- Latency (p50, p95, p99)
- IntegrationLatency
- CacheHitCount, CacheMissCount
```

**Recommended Alarms**:
- 5XX error rate > 0.5%
- 4XX error rate > 5%
- Latency p99 > 2 seconds
- Integration latency spike

### Pattern 4: Database Monitoring

**MCP Server**: CloudWatch MCP

**RDS Metrics**:
```
- CPUUtilization
- DatabaseConnections
- FreeableMemory
- ReadLatency, WriteLatency
- ReadIOPS, WriteIOPS
- FreeStorageSpace
```

**DynamoDB Metrics**:
```
- ConsumedReadCapacityUnits
- ConsumedWriteCapacityUnits
- UserErrors
- SystemErrors
- ThrottledRequests
```

**Recommended Alarms**:
- RDS CPU > 80% for 10 minutes
- RDS connections > 80% of max
- RDS free storage < 10 GB
- DynamoDB throttled requests > 0
- DynamoDB user errors spike

## Observability Patterns

### Pattern 1: Distributed Tracing Setup

**MCP Server**: CloudWatch Application Signals MCP

**Components**:
1. **Service Map**: Visualize service dependencies
2. **Traces**: Track requests across services
3. **Metrics**: Monitor latency and errors per service
4. **SLOs**: Define and track service level objectives

**Implementation**:
- Enable X-Ray tracing on Lambda functions
- Add X-Ray SDK to application code
- Configure sampling rules
- Create service lens dashboards

### Pattern 2: Log Aggregation and Analysis

**MCP Server**: CloudWatch MCP

**Log Strategy**:
1. **Centralize Logs**: Send all application logs to CloudWatch Logs
2. **Structure Logs**: Use JSON format for structured logging
3. **Log Insights**: Use CloudWatch Logs Insights for queries
4. **Retention**: Set appropriate retention periods

**Example Log Insights Queries**:
```
# Find errors in last hour
fields @timestamp, @message
| filter @message like /ERROR/
| sort @timestamp desc
| limit 100

# Count errors by type
stats count() by error_type
| sort count desc

# Calculate p99 latency
stats percentile(duration, 99) by service_name
```

### Pattern 3: Custom Metrics

**MCP Server**: CloudWatch MCP

**When to Use Custom Metrics**:
- Business-specific KPIs (orders/minute, revenue/hour)
- Application-specific metrics (cache hit rate, queue depth)
- Performance metrics not provided by AWS

**Best Practices**:
- Use consistent namespace: `CompanyName/ApplicationName`
- Include relevant dimensions (environment, region, version)
- Publish metrics at appropriate intervals
- Use metric filters for log-derived metrics

## Security and Audit Patterns

### Pattern 1: API Activity Auditing

**MCP Server**: CloudTrail MCP

**Regular Audit Queries**:
```
# Find all IAM changes
eventName: CreateUser, DeleteUser, AttachUserPolicy, etc.
Time: Last 24 hours

# Track S3 bucket deletions
eventName: DeleteBucket
Time: Last 7 days

# Find failed login attempts
eventName: ConsoleLogin
errorCode: Failure

# Monitor privileged actions
userIdentity.arn: *admin* OR *root*
```

**Audit Schedule**:
- Daily: Review privileged user actions
- Weekly: Audit IAM changes and security group modifications
- Monthly: Comprehensive security review

### Pattern 2: Security Posture Assessment

**MCP Server**: Well-Architected Security Assessment Tool MCP

**Assessment Areas**:
1. **Identity and Access Management**
   - Least privilege implementation
   - MFA enforcement
   - Role-based access control
   - Service control policies

2. **Detective Controls**
   - CloudTrail enabled in all regions
   - GuardDuty findings review
   - Config rule compliance
   - Security Hub findings

3. **Infrastructure Protection**
   - VPC security groups review
   - Network ACLs configuration
   - AWS WAF rules
   - Security group ingress rules

4. **Data Protection**
   - Encryption at rest (S3, EBS, RDS)
   - Encryption in transit (TLS/SSL)
   - KMS key usage and rotation
   - Secrets Manager utilization

5. **Incident Response**
   - IR playbooks documented
   - Automated response procedures
   - Contact information current
   - Regular IR drills

**Assessment Frequency**:
- Quarterly: Full Well-Architected review
- Monthly: High-priority findings review
- Weekly: Critical security findings

### Pattern 3: Compliance Monitoring

**MCP Servers**: CloudTrail MCP, CloudWatch MCP

**Compliance Requirements**:
- Data residency (ensure data stays in approved regions)
- Access logging (all access logged and retained)
- Encryption requirements (data encrypted at rest and in transit)
- Change management (all changes tracked in CloudTrail)

**Compliance Dashboards**:
- Encryption coverage by service
- CloudTrail logging status
- Failed login attempts
- Privileged access usage
- Non-compliant resources

## Troubleshooting Workflows

### Workflow 1: High Lambda Error Rate

**MCP Servers**: CloudWatch MCP, CloudWatch Application Signals MCP

**Steps**:
1. Query CloudWatch for Lambda error metrics
2. Check error logs in CloudWatch Logs
3. Identify error patterns (timeout, memory, permission)
4. Check Lambda configuration (memory, timeout, permissions)
5. Review recent code deployments
6. Check downstream service health
7. Implement fix and monitor

### Workflow 2: Increased Latency

**MCP Servers**: CloudWatch MCP, CloudWatch Application Signals MCP

**Steps**:
1. Identify latency spike in CloudWatch metrics
2. Check service map for slow dependencies
3. Query distributed traces for slow requests
4. Check database query performance
5. Review API Gateway integration latency
6. Check Lambda cold starts
7. Identify bottleneck and optimize

### Workflow 3: Cost Spike Investigation

**MCP Servers**: Cost Explorer MCP, CloudWatch MCP, CloudTrail MCP

**Steps**:
1. Use Cost Explorer to identify service causing spike
2. Check CloudWatch metrics for usage increase
3. Review CloudTrail for recent resource creation
4. Identify root cause (misconfiguration, runaway process, attack)
5. Implement cost controls (budgets, alarms, service quotas)
6. Clean up unnecessary resources

### Workflow 4: Security Incident Response

**MCP Servers**: CloudTrail MCP, GuardDuty (via CloudWatch), Well-Architected Assessment MCP

**Steps**:
1. Identify security event in GuardDuty or CloudWatch
2. Query CloudTrail for related API activity
3. Determine scope and impact
4. Isolate affected resources
5. Revoke compromised credentials
6. Implement remediation
7. Conduct post-incident review
8. Update security controls

## Summary

- **Cost Optimization**: Use Pricing, Cost Explorer, and Billing MCPs for proactive cost management
- **Monitoring**: Set up comprehensive CloudWatch alarms for all critical services
- **Observability**: Implement distributed tracing and structured logging
- **Security**: Regular CloudTrail audits and Well-Architected assessments
- **Proactive**: Don't wait for incidents - monitor and optimize continuously
```

## File: `plugins/serverless-eda/skills/aws-serverless-eda/SKILL.md`
```markdown
---
name: aws-serverless-eda
description: AWS serverless and event-driven architecture expert based on Well-Architected Framework. Use when building serverless APIs, Lambda functions, REST APIs, microservices, or async workflows. Covers Lambda with TypeScript/Python, API Gateway (REST/HTTP), DynamoDB, Step Functions, EventBridge, SQS, SNS, and serverless patterns. Essential when user mentions serverless, Lambda, API Gateway, event-driven, async processing, queues, pub/sub, or wants to build scalable serverless applications with AWS best practices.
context: fork
skills:
  - aws-mcp-setup
  - aws-cdk-development
allowed-tools:
  - mcp__aws-mcp__*
  - mcp__awsdocs__*
  - mcp__cdk__*
  - Bash(sam *)
  - Bash(aws lambda *)
  - Bash(aws apigateway *)
  - Bash(aws apigatewayv2 *)
  - Bash(aws dynamodb *)
  - Bash(aws stepfunctions *)
  - Bash(aws events *)
  - Bash(aws sqs *)
  - Bash(aws sns *)
  - Bash(aws sts get-caller-identity)
hooks:
  PreToolUse:
    - matcher: Bash(sam deploy*)
      command: aws sts get-caller-identity --query Account --output text
      once: true
---

# AWS Serverless & Event-Driven Architecture

This skill provides comprehensive guidance for building serverless applications and event-driven architectures on AWS based on Well-Architected Framework principles.

## AWS Documentation Requirement

Always verify AWS facts using MCP tools (`mcp__aws-mcp__*` or `mcp__*awsdocs*__*`) before answering. The `aws-mcp-setup` dependency is auto-loaded — if MCP tools are unavailable, guide the user through that skill's setup flow.

## Serverless MCP Servers

This skill leverages the CDK MCP server (provided via `aws-cdk-development` dependency) and AWS Documentation MCP for serverless guidance.

> **Note**: The following AWS MCP servers are available separately via the Full AWS MCP Server (see `aws-mcp-setup` skill) and are not bundled with this plugin:
> - AWS Serverless MCP — SAM CLI lifecycle (init, deploy, local test)
> - AWS Lambda Tool MCP — Direct Lambda invocation
> - AWS Step Functions MCP — Workflow orchestration
> - Amazon SNS/SQS MCP — Messaging and queue management

## When to Use This Skill

Use this skill when:
- Building serverless applications with Lambda
- Designing event-driven architectures
- Implementing microservices patterns
- Creating asynchronous processing workflows
- Orchestrating multi-service transactions
- Building real-time data processing pipelines
- Implementing saga patterns for distributed transactions
- Designing for scale and resilience

## AWS Well-Architected Serverless Design Principles

### 1. Speedy, Simple, Singular

**Functions should be concise and single-purpose**

```typescript
// ✅ GOOD - Single purpose, focused function
export const processOrder = async (event: OrderEvent) => {
  // Only handles order processing
  const order = await validateOrder(event);
  await saveOrder(order);
  await publishOrderCreatedEvent(order);
  return { statusCode: 200, body: JSON.stringify({ orderId: order.id }) };
};

// ❌ BAD - Function does too much
export const handleEverything = async (event: any) => {
  // Handles orders, inventory, payments, shipping...
  // Too many responsibilities
};
```

**Keep functions environmentally efficient and cost-aware**:
- Minimize cold start times
- Optimize memory allocation
- Use provisioned concurrency only when needed
- Leverage connection reuse

### 2. Think Concurrent Requests, Not Total Requests

**Design for concurrency, not volume**

Lambda scales horizontally - design considerations should focus on:
- Concurrent execution limits
- Downstream service throttling
- Shared resource contention
- Connection pool sizing

```typescript
// Consider concurrent Lambda executions accessing DynamoDB
const table = new dynamodb.Table(this, 'Table', {
  billingMode: dynamodb.BillingMode.PAY_PER_REQUEST, // Auto-scales with load
});

// Or with provisioned capacity + auto-scaling
const table = new dynamodb.Table(this, 'Table', {
  billingMode: dynamodb.BillingMode.PROVISIONED,
  readCapacity: 5,
  writeCapacity: 5,
});

// Enable auto-scaling for concurrent load
table.autoScaleReadCapacity({ minCapacity: 5, maxCapacity: 100 });
table.autoScaleWriteCapacity({ minCapacity: 5, maxCapacity: 100 });
```

### 3. Share Nothing

**Function runtime environments are short-lived**

```typescript
// ❌ BAD - Relying on local file system
export const handler = async (event: any) => {
  fs.writeFileSync('/tmp/data.json', JSON.stringify(data)); // Lost after execution
};

// ✅ GOOD - Use persistent storage
export const handler = async (event: any) => {
  await s3.putObject({
    Bucket: process.env.BUCKET_NAME,
    Key: 'data.json',
    Body: JSON.stringify(data),
  });
};
```

**State management**:
- Use DynamoDB for persistent state
- Use Step Functions for workflow state
- Use ElastiCache for session state
- Use S3 for file storage

### 4. Assume No Hardware Affinity

**Applications must be hardware-agnostic**

Infrastructure can change without notice:
- Lambda functions can run on different hardware
- Container instances can be replaced
- No assumption about underlying infrastructure

**Design for portability**:
- Use environment variables for configuration
- Avoid hardware-specific optimizations
- Test across different environments

### 5. Orchestrate with State Machines, Not Function Chaining

**Use Step Functions for orchestration**

```typescript
// ❌ BAD - Lambda function chaining
export const handler1 = async (event: any) => {
  const result = await processStep1(event);
  await lambda.invoke({
    FunctionName: 'handler2',
    Payload: JSON.stringify(result),
  });
};

// ✅ GOOD - Step Functions orchestration
const stateMachine = new stepfunctions.StateMachine(this, 'OrderWorkflow', {
  definition: stepfunctions.Chain
    .start(validateOrder)
    .next(processPayment)
    .next(shipOrder)
    .next(sendConfirmation),
});
```

**Benefits of Step Functions**:
- Visual workflow representation
- Built-in error handling and retries
- Execution history and debugging
- Parallel and sequential execution
- Service integrations without code

### 6. Use Events to Trigger Transactions

**Event-driven over synchronous request/response**

```typescript
// Pattern: Event-driven processing
const bucket = new s3.Bucket(this, 'DataBucket');

bucket.addEventNotification(
  s3.EventType.OBJECT_CREATED,
  new s3n.LambdaDestination(processFunction),
  { prefix: 'uploads/' }
);

// Pattern: EventBridge integration
const rule = new events.Rule(this, 'OrderRule', {
  eventPattern: {
    source: ['orders'],
    detailType: ['OrderPlaced'],
  },
});

rule.addTarget(new targets.LambdaFunction(processOrderFunction));
```

**Benefits**:
- Loose coupling between services
- Asynchronous processing
- Better fault tolerance
- Independent scaling

### 7. Design for Failures and Duplicates

**Operations must be idempotent**

```typescript
// ✅ GOOD - Idempotent operation
export const handler = async (event: SQSEvent) => {
  for (const record of event.Records) {
    const orderId = JSON.parse(record.body).orderId;

    // Check if already processed (idempotency)
    const existing = await dynamodb.getItem({
      TableName: process.env.TABLE_NAME,
      Key: { orderId },
    });

    if (existing.Item) {
      console.log('Order already processed:', orderId);
      continue; // Skip duplicate
    }

    // Process order
    await processOrder(orderId);

    // Mark as processed
    await dynamodb.putItem({
      TableName: process.env.TABLE_NAME,
      Item: { orderId, processedAt: Date.now() },
    });
  }
};
```

**Implement retry logic with exponential backoff**:
```typescript
async function withRetry<T>(fn: () => Promise<T>, maxRetries = 3): Promise<T> {
  for (let i = 0; i < maxRetries; i++) {
    try {
      return await fn();
    } catch (error) {
      if (i === maxRetries - 1) throw error;
      await new Promise(resolve => setTimeout(resolve, Math.pow(2, i) * 1000));
    }
  }
  throw new Error('Max retries exceeded');
}
```

## Architecture Patterns

For detailed implementation patterns with full code examples, see the reference documentation:

### Event-Driven Architecture Patterns
**File**: `references/eda-patterns.md`
- Event Router with EventBridge (custom event bus, schema registry, rule-based routing)
- Queue-Based Processing with SQS (standard/FIFO, DLQ, Lambda consumers)
- Pub/Sub Fan-Out with SNS + SQS (multi-consumer, filtering)
- Saga Pattern with Step Functions (distributed transactions, compensating actions)
- Event Sourcing with DynamoDB Streams (append-only event store, projections)

### Serverless Architecture Patterns
**File**: `references/serverless-patterns.md`
- API-Driven Microservices (REST API + Lambda backend)
- Stream Processing with Kinesis (real-time, batch windowing, bisect on error)
- Async Task Processing with SQS (background jobs, concurrency control)
- Scheduled Jobs with EventBridge (cron/rate schedules)
- Webhook Processing (signature validation, async queue forwarding)

> **Important**: When using CDK code examples from references, avoid hardcoding resource names (e.g., `restApiName`, `eventBusName`). Let CDK generate unique names automatically to enable reusability and parallel deployments. See `aws-cdk-development` skill for details.

## Best Practices

### Error Handling

**Implement comprehensive error handling**:

```typescript
export const handler = async (event: SQSEvent) => {
  const failures: SQSBatchItemFailure[] = [];

  for (const record of event.Records) {
    try {
      await processRecord(record);
    } catch (error) {
      console.error('Failed to process record:', record.messageId, error);
      failures.push({ itemIdentifier: record.messageId });
    }
  }

  // Return partial batch failures for retry
  return { batchItemFailures: failures };
};
```

### Dead Letter Queues

**Always configure DLQs for error handling**:

```typescript
const dlq = new sqs.Queue(this, 'DLQ', {
  retentionPeriod: Duration.days(14),
});

const queue = new sqs.Queue(this, 'Queue', {
  deadLetterQueue: {
    queue: dlq,
    maxReceiveCount: 3,
  },
});

// Monitor DLQ depth
new cloudwatch.Alarm(this, 'DLQAlarm', {
  metric: dlq.metricApproximateNumberOfMessagesVisible(),
  threshold: 1,
  evaluationPeriods: 1,
  alarmDescription: 'Messages in DLQ require attention',
});
```

### Observability

**Enable tracing and monitoring**:

```typescript
new NodejsFunction(this, 'Function', {
  entry: 'src/handler.ts',
  tracing: lambda.Tracing.ACTIVE, // X-Ray tracing
  environment: {
    POWERTOOLS_SERVICE_NAME: 'order-service',
    POWERTOOLS_METRICS_NAMESPACE: 'MyApp',
    LOG_LEVEL: 'INFO',
  },
});
```

## Using MCP Servers Effectively

Use the CDK MCP server (via `aws-cdk-development` dependency) for construct recommendations and CDK-specific guidance when building serverless infrastructure.

Use AWS Documentation MCP to verify service features, regional availability, and API specifications before implementing.

## Additional Resources

This skill includes comprehensive reference documentation based on AWS best practices:

- **Serverless Patterns**: `references/serverless-patterns.md`
  - Core serverless architectures and API patterns
  - Data processing and integration patterns
  - Orchestration with Step Functions
  - Anti-patterns to avoid

- **Event-Driven Architecture Patterns**: `references/eda-patterns.md`
  - Event routing and processing patterns
  - Event sourcing and saga patterns
  - Idempotency and error handling
  - Message ordering and deduplication

- **Security Best Practices**: `references/security-best-practices.md`
  - Shared responsibility model
  - IAM least privilege patterns
  - Data protection and encryption
  - Network security with VPC

- **Observability Best Practices**: `references/observability-best-practices.md`
  - Three pillars: metrics, logs, traces
  - Structured logging with Lambda Powertools
  - X-Ray distributed tracing
  - CloudWatch alarms and dashboards

- **Performance Optimization**: `references/performance-optimization.md`
  - Cold start optimization techniques
  - Memory and CPU optimization
  - Package size reduction
  - Provisioned concurrency patterns

- **Deployment Best Practices**: `references/deployment-best-practices.md`
  - CI/CD pipeline design
  - Testing strategies (unit, integration, load)
  - Deployment strategies (canary, blue/green)
  - Rollback and safety mechanisms

**External Resources**:
- **AWS Well-Architected Serverless Lens**: https://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/
- **ServerlessLand.com**: Pre-built serverless patterns
- **AWS Serverless Workshops**: https://serverlessland.com/learn?type=Workshops

For detailed implementation patterns, anti-patterns, and code examples, refer to the comprehensive references in the skill directory.
```

## File: `plugins/serverless-eda/skills/aws-serverless-eda/references/deployment-best-practices.md`
```markdown
# Serverless Deployment Best Practices

Deployment best practices for serverless applications including CI/CD, testing, and deployment strategies.

## Table of Contents

- [Software Release Process](#software-release-process)
- [Infrastructure as Code](#infrastructure-as-code)
- [CI/CD Pipeline Design](#cicd-pipeline-design)
- [Testing Strategies](#testing-strategies)
- [Deployment Strategies](#deployment-strategies)
- [Rollback and Safety](#rollback-and-safety)

## Software Release Process

### Four Stages of Release

**1. Source Phase**:
- Developers commit code changes
- Code review (peer review)
- Version control (Git)

**2. Build Phase**:
- Compile code
- Run unit tests
- Style checking and linting
- Create deployment packages
- Build container images

**3. Test Phase**:
- Integration tests with other systems
- Load testing
- UI testing
- Security testing (penetration testing)
- Acceptance testing

**4. Production Phase**:
- Deploy to production environment
- Monitor for errors
- Validate deployment success
- Rollback if needed

### CI/CD Maturity Levels

**Continuous Integration (CI)**:
- Automated build on code commit
- Automated unit testing
- Manual deployment to test/production

**Continuous Delivery (CD)**:
- Automated deployment to test environments
- Manual approval for production
- Automated testing in non-prod

**Continuous Deployment**:
- Fully automated pipeline
- Automated deployment to production
- No manual intervention after code commit

## Infrastructure as Code

### Framework Selection

**AWS SAM (Serverless Application Model)**:

```yaml
# template.yaml
AWSTemplateFormatVersion: '2010-09-09'
Transform: AWS::Serverless-2016-10-31

Resources:
  OrderFunction:
    Type: AWS::Serverless::Function
    Properties:
      Handler: app.handler
      Runtime: nodejs20.x
      CodeUri: src/
      Events:
        Api:
          Type: Api
          Properties:
            Path: /orders
            Method: post
```

**Benefits**:
- Simple, serverless-focused syntax
- Built-in best practices
- SAM CLI for local testing
- Integrates with CodeDeploy

**AWS CDK**:

```typescript
new NodejsFunction(this, 'OrderFunction', {
  entry: 'src/orders/handler.ts',
  environment: {
    TABLE_NAME: ordersTable.tableName,
  },
});

ordersTable.grantReadWriteData(orderFunction);
```

**Benefits**:
- Type-safe, programmatic
- Reusable constructs
- Rich AWS service support
- Better for complex infrastructure

**When to use**:
- **SAM**: Serverless-only applications, simpler projects
- **CDK**: Complex infrastructure, multiple services, reusable patterns

### Environment Management

**Separate environments**:

```typescript
// CDK App
const app = new cdk.App();

new ServerlessStack(app, 'DevStack', {
  env: { account: '111111111111', region: 'us-east-1' },
  environment: 'dev',
  logLevel: 'DEBUG',
});

new ServerlessStack(app, 'ProdStack', {
  env: { account: '222222222222', region: 'us-east-1' },
  environment: 'prod',
  logLevel: 'INFO',
});
```

**SAM with parameters**:

```yaml
Parameters:
  Environment:
    Type: String
    Default: dev
    AllowedValues:
      - dev
      - staging
      - prod

Resources:
  Function:
    Type: AWS::Serverless::Function
    Properties:
      Environment:
        Variables:
          ENVIRONMENT: !Ref Environment
          LOG_LEVEL: !If [IsProd, INFO, DEBUG]
```

## CI/CD Pipeline Design

### AWS CodePipeline

**Comprehensive pipeline**:

```typescript
import * as codepipeline from 'aws-cdk-lib/aws-codepipeline';
import * as codepipeline_actions from 'aws-cdk-lib/aws-codepipeline-actions';

const sourceOutput = new codepipeline.Artifact();
const buildOutput = new codepipeline.Artifact();

const pipeline = new codepipeline.Pipeline(this, 'Pipeline', {
  pipelineName: 'serverless-pipeline',
});

// Source stage
pipeline.addStage({
  stageName: 'Source',
  actions: [
    new codepipeline_actions.CodeStarConnectionsSourceAction({
      actionName: 'GitHub_Source',
      owner: 'myorg',
      repo: 'myrepo',
      branch: 'main',
      output: sourceOutput,
      connectionArn: githubConnection.connectionArn,
    }),
  ],
});

// Build stage
pipeline.addStage({
  stageName: 'Build',
  actions: [
    new codepipeline_actions.CodeBuildAction({
      actionName: 'Build',
      project: buildProject,
      input: sourceOutput,
      outputs: [buildOutput],
    }),
  ],
});

// Test stage
pipeline.addStage({
  stageName: 'Test',
  actions: [
    new codepipeline_actions.CloudFormationCreateUpdateStackAction({
      actionName: 'Deploy_Test',
      templatePath: buildOutput.atPath('packaged.yaml'),
      stackName: 'test-stack',
      adminPermissions: true,
    }),
    new codepipeline_actions.CodeBuildAction({
      actionName: 'Integration_Tests',
      project: testProject,
      input: buildOutput,
      runOrder: 2,
    }),
  ],
});

// Production stage (with manual approval)
pipeline.addStage({
  stageName: 'Production',
  actions: [
    new codepipeline_actions.ManualApprovalAction({
      actionName: 'Approve',
    }),
    new codepipeline_actions.CloudFormationCreateUpdateStackAction({
      actionName: 'Deploy_Prod',
      templatePath: buildOutput.atPath('packaged.yaml'),
      stackName: 'prod-stack',
      adminPermissions: true,
      runOrder: 2,
    }),
  ],
});
```

### GitHub Actions

**Serverless deployment workflow**:

```yaml
# .github/workflows/deploy.yml
name: Deploy Serverless Application

on:
  push:
    branches: [main]

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Setup Node.js
        uses: actions/setup-node@v3
        with:
          node-version: '20'

      - name: Install dependencies
        run: npm ci

      - name: Run tests
        run: npm test

      - name: Setup SAM CLI
        uses: aws-actions/setup-sam@v2

      - name: Build SAM application
        run: sam build

      - name: Deploy to Dev
        if: github.ref != 'refs/heads/main'
        run: |
          sam deploy \
            --no-confirm-changeset \
            --no-fail-on-empty-changeset \
            --stack-name dev-stack \
            --parameter-overrides Environment=dev

      - name: Run integration tests
        run: npm run test:integration

      - name: Deploy to Prod
        if: github.ref == 'refs/heads/main'
        run: |
          sam deploy \
            --no-confirm-changeset \
            --no-fail-on-empty-changeset \
            --stack-name prod-stack \
            --parameter-overrides Environment=prod
```

## Testing Strategies

### Unit Testing

**Test business logic independently**:

```typescript
// handler.ts
export const processOrder = (order: Order): ProcessedOrder => {
  // Pure business logic (easily testable)
  validateOrder(order);
  calculateTotal(order);
  return transformOrder(order);
};

export const handler = async (event: any) => {
  const order = parseEvent(event);
  const processed = processOrder(order); // Testable function
  await saveToDatabase(processed);
  return formatResponse(processed);
};

// handler.test.ts
import { processOrder } from './handler';

describe('processOrder', () => {
  it('calculates total correctly', () => {
    const order = {
      items: [
        { price: 10, quantity: 2 },
        { price: 5, quantity: 3 },
      ],
    };

    const result = processOrder(order);

    expect(result.total).toBe(35);
  });

  it('throws on invalid order', () => {
    const invalid = { items: [] };
    expect(() => processOrder(invalid)).toThrow();
  });
});
```

### Integration Testing

**Test in actual AWS environment**:

```typescript
// integration.test.ts
import { LambdaClient, InvokeCommand } from '@aws-sdk/client-lambda';
import { DynamoDBClient, GetItemCommand } from '@aws-sdk/client-dynamodb';

describe('Order Processing Integration', () => {
  const lambda = new LambdaClient({});
  const dynamodb = new DynamoDBClient({});

  it('processes order end-to-end', async () => {
    // Invoke Lambda
    const response = await lambda.send(new InvokeCommand({
      FunctionName: process.env.FUNCTION_NAME,
      Payload: JSON.stringify({
        orderId: 'test-123',
        items: [{ productId: 'prod-1', quantity: 2 }],
      }),
    }));

    const result = JSON.parse(Buffer.from(response.Payload!).toString());

    expect(result.statusCode).toBe(200);

    // Verify database write
    const dbResult = await dynamodb.send(new GetItemCommand({
      TableName: process.env.TABLE_NAME,
      Key: { orderId: { S: 'test-123' } },
    }));

    expect(dbResult.Item).toBeDefined();
    expect(dbResult.Item?.status.S).toBe('PROCESSED');
  });
});
```

### Local Testing with SAM

**Test locally before deployment**:

```bash
# Start local API
sam local start-api

# Invoke function locally
sam local invoke OrderFunction -e events/create-order.json

# Generate sample events
sam local generate-event apigateway aws-proxy > event.json

# Debug locally
sam local invoke OrderFunction -d 5858

# Test with Docker
sam local start-api --docker-network my-network
```

### Load Testing

**Test under production load**:

```bash
# Install Artillery
npm install -g artillery

# Create load test
cat > load-test.yml <<EOF
config:
  target: https://api.example.com
  phases:
    - duration: 300 # 5 minutes
      arrivalRate: 50 # 50 requests/second
      rampTo: 200 # Ramp to 200 req/sec
scenarios:
  - flow:
      - post:
          url: /orders
          json:
            orderId: "{{ $randomString() }}"
EOF

# Run load test
artillery run load-test.yml --output report.json

# Generate HTML report
artillery report report.json
```

## Deployment Strategies

### All-at-Once Deployment

**Simple, fast, risky**:

```yaml
# SAM template
Resources:
  OrderFunction:
    Type: AWS::Serverless::Function
    Properties:
      DeploymentPreference:
        Type: AllAtOnce # Deploy immediately
```

**Use for**:
- Development environments
- Non-critical applications
- Quick hotfixes (with caution)

### Blue/Green Deployment

**Zero-downtime deployment**:

```yaml
Resources:
  OrderFunction:
    Type: AWS::Serverless::Function
    Properties:
      AutoPublishAlias: live
      DeploymentPreference:
        Type: Linear10PercentEvery1Minute
        Alarms:
          - !Ref ErrorAlarm
          - !Ref LatencyAlarm
```

**Deployment types**:
- **Linear10PercentEvery1Minute**: 10% traffic shift every minute
- **Linear10PercentEvery2Minutes**: Slower, more conservative
- **Linear10PercentEvery3Minutes**: Even slower
- **Linear10PercentEvery10Minutes**: Very gradual
- **Canary10Percent5Minutes**: 10% for 5 min, then 100%
- **Canary10Percent10Minutes**: 10% for 10 min, then 100%
- **Canary10Percent30Minutes**: 10% for 30 min, then 100%

### Canary Deployment

**Test with subset of traffic**:

```yaml
Resources:
  OrderFunction:
    Type: AWS::Serverless::Function
    Properties:
      AutoPublishAlias: live
      DeploymentPreference:
        Type: Canary10Percent10Minutes
        Alarms:
          - !Ref ErrorAlarm
          - !Ref LatencyAlarm
        Hooks:
          PreTraffic: !Ref PreTrafficHook
          PostTraffic: !Ref PostTrafficHook

  PreTrafficHook:
    Type: AWS::Serverless::Function
    Properties:
      Handler: hooks.pre_traffic
      Runtime: python3.12
      # Runs before traffic shift
      # Validates new version

  PostTrafficHook:
    Type: AWS::Serverless::Function
    Properties:
      Handler: hooks.post_traffic
      Runtime: python3.12
      # Runs after traffic shift
      # Validates deployment success
```

**CDK with CodeDeploy**:

```typescript
import * as codedeploy from 'aws-cdk-lib/aws-codedeploy';

const alias = fn.currentVersion.addAlias('live');

new codedeploy.LambdaDeploymentGroup(this, 'DeploymentGroup', {
  alias,
  deploymentConfig: codedeploy.LambdaDeploymentConfig.CANARY_10PERCENT_10MINUTES,
  alarms: [errorAlarm, latencyAlarm],
  autoRollback: {
    failedDeployment: true,
    stoppedDeployment: true,
    deploymentInAlarm: true,
  },
});
```

### Deployment Hooks

**Pre-traffic hook (validation)**:

```python
# hooks.py
import boto3

lambda_client = boto3.client('lambda')
codedeploy = boto3.client('codedeploy')

def pre_traffic(event, context):
    """
    Validate new version before traffic shift
    """
    function_name = event['DeploymentId']
    version = event['NewVersion']

    try:
        # Invoke new version with test payload
        response = lambda_client.invoke(
            FunctionName=f"{function_name}:{version}",
            InvocationType='RequestResponse',
            Payload=json.dumps({'test': True})
        )

        # Validate response
        if response['StatusCode'] == 200:
            codedeploy.put_lifecycle_event_hook_execution_status(
                deploymentId=event['DeploymentId'],
                lifecycleEventHookExecutionId=event['LifecycleEventHookExecutionId'],
                status='Succeeded'
            )
        else:
            raise Exception('Validation failed')

    except Exception as e:
        print(f'Pre-traffic validation failed: {e}')
        codedeploy.put_lifecycle_event_hook_execution_status(
            deploymentId=event['DeploymentId'],
            lifecycleEventHookExecutionId=event['LifecycleEventHookExecutionId'],
            status='Failed'
        )
```

**Post-traffic hook (verification)**:

```python
def post_traffic(event, context):
    """
    Verify deployment success after traffic shift
    """
    try:
        # Check CloudWatch metrics
        cloudwatch = boto3.client('cloudwatch')

        metrics = cloudwatch.get_metric_statistics(
            Namespace='AWS/Lambda',
            MetricName='Errors',
            Dimensions=[{'Name': 'FunctionName', 'Value': function_name}],
            StartTime=deployment_start_time,
            EndTime=datetime.utcnow(),
            Period=300,
            Statistics=['Sum']
        )

        # Validate no errors
        total_errors = sum(point['Sum'] for point in metrics['Datapoints'])

        if total_errors == 0:
            codedeploy.put_lifecycle_event_hook_execution_status(
                deploymentId=event['DeploymentId'],
                lifecycleEventHookExecutionId=event['LifecycleEventHookExecutionId'],
                status='Succeeded'
            )
        else:
            raise Exception(f'{total_errors} errors detected')

    except Exception as e:
        print(f'Post-traffic verification failed: {e}')
        codedeploy.put_lifecycle_event_hook_execution_status(
            deploymentId=event['DeploymentId'],
            lifecycleEventHookExecutionId=event['LifecycleEventHookExecutionId'],
            status='Failed'
        )
```

## Rollback and Safety

### Automatic Rollback

**Configure rollback triggers**:

```yaml
DeploymentPreference:
  Type: Canary10Percent10Minutes
  Alarms:
    - !Ref ErrorAlarm
    - !Ref LatencyAlarm
  # Automatically rolls back if alarms trigger
```

**Rollback scenarios**:
- CloudWatch alarm triggers during deployment
- Pre-traffic hook fails
- Post-traffic hook fails
- Deployment manually stopped

### CloudWatch Alarms for Deployment

**Critical alarms during deployment**:

```typescript
// Error rate alarm
const errorAlarm = new cloudwatch.Alarm(this, 'ErrorAlarm', {
  metric: fn.metricErrors({
    statistic: 'Sum',
    period: Duration.minutes(1),
  }),
  threshold: 5,
  evaluationPeriods: 2,
  treatMissingData: cloudwatch.TreatMissingData.NOT_BREACHING,
});

// Duration alarm (regression)
const durationAlarm = new cloudwatch.Alarm(this, 'DurationAlarm', {
  metric: fn.metricDuration({
    statistic: 'Average',
    period: Duration.minutes(1),
  }),
  threshold: previousAvgDuration * 1.2, // 20% increase
  evaluationPeriods: 2,
  comparisonOperator: cloudwatch.ComparisonOperator.GREATER_THAN_THRESHOLD,
});

// Throttle alarm
const throttleAlarm = new cloudwatch.Alarm(this, 'ThrottleAlarm', {
  metric: fn.metricThrottles({
    statistic: 'Sum',
    period: Duration.minutes(1),
  }),
  threshold: 1,
  evaluationPeriods: 1,
});
```

### Version Management

**Use Lambda versions and aliases**:

```typescript
const version = fn.currentVersion;

const prodAlias = version.addAlias('prod');
const devAlias = version.addAlias('dev');

// Gradual rollout with weighted aliases
new lambda.Alias(this, 'LiveAlias', {
  aliasName: 'live',
  version: newVersion,
  additionalVersions: [
    { version: oldVersion, weight: 0.9 }, // 90% old
    // 10% automatically goes to main version (new)
  ],
});
```

## Best Practices Checklist

### Pre-Deployment

- [ ] Code review completed
- [ ] Unit tests passing
- [ ] Integration tests passing
- [ ] Security scan completed
- [ ] Dependencies updated
- [ ] Infrastructure validated (CDK synth, SAM validate)
- [ ] Environment variables configured

### Deployment

- [ ] Use IaC (SAM, CDK, Terraform)
- [ ] Separate environments (dev, staging, prod)
- [ ] Automate deployments via CI/CD
- [ ] Use gradual deployment (canary or linear)
- [ ] Configure CloudWatch alarms
- [ ] Enable automatic rollback
- [ ] Use deployment hooks for validation

### Post-Deployment

- [ ] Monitor CloudWatch metrics
- [ ] Check CloudWatch Logs for errors
- [ ] Verify X-Ray traces
- [ ] Validate business metrics
- [ ] Check alarm status
- [ ] Review deployment logs
- [ ] Document any issues

### Rollback Preparation

- [ ] Keep previous version available
- [ ] Document rollback procedure
- [ ] Test rollback in non-prod
- [ ] Configure automatic rollback
- [ ] Monitor during rollback
- [ ] Communication plan for rollback

## Deployment Patterns

### Multi-Region Deployment

**Active-Passive**:

```typescript
// Primary region
new ServerlessStack(app, 'PrimaryStack', {
  env: { region: 'us-east-1' },
  isPrimary: true,
});

// Secondary region (standby)
new ServerlessStack(app, 'SecondaryStack', {
  env: { region: 'us-west-2' },
  isPrimary: false,
});

// Route 53 health check and failover
const healthCheck = new route53.CfnHealthCheck(this, 'HealthCheck', {
  type: 'HTTPS',
  resourcePath: '/health',
  fullyQualifiedDomainName: 'api.example.com',
});
```

**Active-Active**:

```typescript
// Deploy to multiple regions
const regions = ['us-east-1', 'us-west-2', 'eu-west-1'];

for (const region of regions) {
  new ServerlessStack(app, `Stack-${region}`, {
    env: { region },
  });
}

// Route 53 geolocation routing
new route53.ARecord(this, 'GeoRecord', {
  zone: hostedZone,
  recordName: 'api',
  target: route53.RecordTarget.fromAlias(
    new targets.ApiGatewayDomain(domain)
  ),
  geoLocation: route53.GeoLocation.country('US'),
});
```

### Feature Flags with AppConfig

**Safe feature rollout**:

```typescript
import { AppConfigData } from '@aws-sdk/client-appconfigdata';

const appconfig = new AppConfigData({});

export const handler = async (event: any) => {
  // Fetch feature flags
  const config = await appconfig.getLatestConfiguration({
    ConfigurationToken: token,
  });

  const features = JSON.parse(config.Configuration.toString());

  if (features.newFeatureEnabled) {
    return newFeatureHandler(event);
  }

  return legacyHandler(event);
};
```

## Summary

- **IaC**: Use SAM or CDK for all deployments
- **Environments**: Separate dev, staging, production
- **CI/CD**: Automate build, test, and deployment
- **Testing**: Unit, integration, and load testing
- **Gradual Deployment**: Use canary or linear for production
- **Alarms**: Configure and monitor during deployment
- **Rollback**: Enable automatic rollback on failures
- **Hooks**: Validate before and after traffic shifts
- **Versioning**: Use Lambda versions and aliases
- **Multi-Region**: Plan for disaster recovery
```

## File: `plugins/serverless-eda/skills/aws-serverless-eda/references/eda-patterns.md`
```markdown
# Event-Driven Architecture Patterns

Comprehensive patterns for building event-driven systems on AWS with serverless technologies.

## Table of Contents

- [Core EDA Concepts](#core-eda-concepts)
- [Event Routing Patterns](#event-routing-patterns)
- [Event Processing Patterns](#event-processing-patterns)
- [Event Sourcing Patterns](#event-sourcing-patterns)
- [Saga Patterns](#saga-patterns)
- [Best Practices](#best-practices)

## Core EDA Concepts

### Event Types

**Domain Events**: Represent business facts
```json
{
  "source": "orders",
  "detailType": "OrderPlaced",
  "detail": {
    "orderId": "12345",
    "customerId": "customer-1",
    "amount": 100.00,
    "timestamp": "2025-01-15T10:30:00Z"
  }
}
```

**System Events**: Technical occurrences
```json
{
  "source": "aws.s3",
  "detailType": "Object Created",
  "detail": {
    "bucket": "my-bucket",
    "key": "data/file.json"
  }
}
```

### Event Contracts

Define clear contracts between producers and consumers:

```typescript
// schemas/order-events.ts
export interface OrderPlacedEvent {
  orderId: string;
  customerId: string;
  items: Array<{
    productId: string;
    quantity: number;
    price: number;
  }>;
  totalAmount: number;
  timestamp: string;
}

// Register schema with EventBridge
const registry = new events.EventBusSchemaRegistry(this, 'SchemaRegistry');

const schema = new events.Schema(this, 'OrderPlacedSchema', {
  schemaName: 'OrderPlaced',
  definition: events.SchemaDefinition.fromInline(/* JSON Schema */),
});
```

## Event Routing Patterns

### Pattern 1: Content-Based Routing

Route events based on content:

```typescript
// Route by order amount
new events.Rule(this, 'HighValueOrders', {
  eventPattern: {
    source: ['orders'],
    detailType: ['OrderPlaced'],
    detail: {
      totalAmount: [{ numeric: ['>', 1000] }],
    },
  },
  targets: [new targets.LambdaFunction(highValueOrderFunction)],
});

new events.Rule(this, 'StandardOrders', {
  eventPattern: {
    source: ['orders'],
    detailType: ['OrderPlaced'],
    detail: {
      totalAmount: [{ numeric: ['<=', 1000] }],
    },
  },
  targets: [new targets.LambdaFunction(standardOrderFunction)],
});
```

### Pattern 2: Event Filtering

Filter events before processing:

```typescript
// Filter by multiple criteria
new events.Rule(this, 'FilteredRule', {
  eventPattern: {
    source: ['inventory'],
    detailType: ['StockUpdate'],
    detail: {
      warehouseId: ['WH-1', 'WH-2'], // Specific warehouses
      quantity: [{ numeric: ['<', 10] }], // Low stock only
      productCategory: ['electronics'], // Specific category
    },
  },
  targets: [new targets.LambdaFunction(reorderFunction)],
});
```

### Pattern 3: Event Replay and Archive

Store events for replay and audit:

```typescript
// Archive all events
const archive = new events.Archive(this, 'EventArchive', {
  eventPattern: {
    account: [this.account],
  },
  retention: Duration.days(365),
});

// Replay events when needed
// Use AWS Console or CLI to replay from archive
```

### Pattern 4: Cross-Account Event Routing

Route events to other AWS accounts:

```typescript
// Event bus in Account A
const eventBus = new events.EventBus(this, 'SharedBus');

// Grant permission to Account B
eventBus.addToResourcePolicy(new iam.PolicyStatement({
  effect: iam.Effect.ALLOW,
  principals: [new iam.AccountPrincipal('ACCOUNT-B-ID')],
  actions: ['events:PutEvents'],
  resources: [eventBus.eventBusArn],
}));

// Rule forwards to Account B event bus
new events.Rule(this, 'ForwardToAccountB', {
  eventBus,
  eventPattern: {
    source: ['shared-service'],
  },
  targets: [new targets.EventBus(
    events.EventBus.fromEventBusArn(
      this,
      'AccountBBus',
      'arn:aws:events:us-east-1:ACCOUNT-B-ID:event-bus/default'
    )
  )],
});
```

## Event Processing Patterns

### Pattern 1: Event Transformation

Transform events before routing:

```typescript
// EventBridge input transformer
new events.Rule(this, 'TransformRule', {
  eventPattern: {
    source: ['orders'],
  },
  targets: [new targets.LambdaFunction(processFunction, {
    event: events.RuleTargetInput.fromObject({
      orderId: events.EventField.fromPath('$.detail.orderId'),
      customerEmail: events.EventField.fromPath('$.detail.customer.email'),
      amount: events.EventField.fromPath('$.detail.totalAmount'),
      // Transformed structure
    }),
  })],
});
```

### Pattern 2: Event Aggregation

Aggregate multiple events:

```typescript
// DynamoDB stores partial results
export const handler = async (event: any) => {
  const { transactionId, step, data } = event;

  // Store step result
  await dynamodb.updateItem({
    TableName: process.env.TABLE_NAME,
    Key: { transactionId },
    UpdateExpression: 'SET #step = :data',
    ExpressionAttributeNames: { '#step': step },
    ExpressionAttributeValues: { ':data': data },
  });

  // Check if all steps complete
  const item = await dynamodb.getItem({
    TableName: process.env.TABLE_NAME,
    Key: { transactionId },
  });

  if (allStepsComplete(item)) {
    // Trigger final processing
    await eventBridge.putEvents({
      Entries: [{
        Source: 'aggregator',
        DetailType: 'AllStepsComplete',
        Detail: JSON.stringify(item),
      }],
    });
  }
};
```

### Pattern 3: Event Enrichment

Enrich events with additional data:

```typescript
export const enrichEvent = async (event: any) => {
  const { customerId } = event.detail;

  // Fetch additional customer data
  const customer = await dynamodb.getItem({
    TableName: process.env.CUSTOMER_TABLE,
    Key: { customerId },
  });

  // Publish enriched event
  await eventBridge.putEvents({
    Entries: [{
      Source: 'orders',
      DetailType: 'OrderEnriched',
      Detail: JSON.stringify({
        ...event.detail,
        customerName: customer.Item?.name,
        customerTier: customer.Item?.tier,
        customerEmail: customer.Item?.email,
      }),
    }],
  });
};
```

### Pattern 4: Event Fork and Join

Process event multiple ways then aggregate:

```typescript
// Step Functions parallel + aggregation
const parallel = new stepfunctions.Parallel(this, 'ForkProcessing');

parallel.branch(new tasks.LambdaInvoke(this, 'ValidateInventory', {
  lambdaFunction: inventoryFunction,
  resultPath: '$.inventory',
}));

parallel.branch(new tasks.LambdaInvoke(this, 'CheckCredit', {
  lambdaFunction: creditFunction,
  resultPath: '$.credit',
}));

parallel.branch(new tasks.LambdaInvoke(this, 'CalculateShipping', {
  lambdaFunction: shippingFunction,
  resultPath: '$.shipping',
}));

const definition = parallel.next(
  new tasks.LambdaInvoke(this, 'AggregateResults', {
    lambdaFunction: aggregateFunction,
  })
);
```

## Event Sourcing Patterns

### Pattern: Event Store with DynamoDB

Store all events as source of truth:

```typescript
const eventStore = new dynamodb.Table(this, 'EventStore', {
  partitionKey: { name: 'aggregateId', type: dynamodb.AttributeType.STRING },
  sortKey: { name: 'version', type: dynamodb.AttributeType.NUMBER },
  stream: dynamodb.StreamViewType.NEW_IMAGE,
  pointInTimeRecovery: true, // Important for audit
});

// Append events
export const appendEvent = async (aggregateId: string, event: any) => {
  const version = await getNextVersion(aggregateId);

  await dynamodb.putItem({
    TableName: process.env.EVENT_STORE,
    Item: {
      aggregateId,
      version,
      eventType: event.type,
      eventData: event.data,
      timestamp: Date.now(),
      userId: event.userId,
    },
    ConditionExpression: 'attribute_not_exists(version)', // Optimistic locking
  });
};

// Rebuild state from events
export const rebuildState = async (aggregateId: string) => {
  const events = await dynamodb.query({
    TableName: process.env.EVENT_STORE,
    KeyConditionExpression: 'aggregateId = :id',
    ExpressionAttributeValues: { ':id': aggregateId },
    ScanIndexForward: true, // Chronological order
  });

  let state = initialState();
  for (const event of events.Items) {
    state = applyEvent(state, event);
  }

  return state;
};
```

### Pattern: Materialized Views

Create read-optimized projections:

```typescript
// Event store stream triggers projection
eventStore.grantStreamRead(projectionFunction);

new lambda.EventSourceMapping(this, 'Projection', {
  target: projectionFunction,
  eventSourceArn: eventStore.tableStreamArn,
  startingPosition: lambda.StartingPosition.LATEST,
});

// Projection function updates read model
export const updateProjection = async (event: DynamoDBStreamEvent) => {
  for (const record of event.Records) {
    if (record.eventName !== 'INSERT') continue;

    const eventData = record.dynamodb?.NewImage;
    const aggregateId = eventData?.aggregateId.S;

    // Rebuild current state
    const currentState = await rebuildState(aggregateId);

    // Update read model
    await readModelTable.putItem({
      TableName: process.env.READ_MODEL_TABLE,
      Item: currentState,
    });
  }
};
```

### Pattern: Snapshots

Optimize event replay with snapshots:

```typescript
export const createSnapshot = async (aggregateId: string) => {
  // Rebuild state from all events
  const state = await rebuildState(aggregateId);
  const version = await getLatestVersion(aggregateId);

  // Store snapshot
  await snapshotTable.putItem({
    TableName: process.env.SNAPSHOT_TABLE,
    Item: {
      aggregateId,
      version,
      state: JSON.stringify(state),
      createdAt: Date.now(),
    },
  });
};

// Rebuild from snapshot + newer events
export const rebuildFromSnapshot = async (aggregateId: string) => {
  // Get latest snapshot
  const snapshot = await getLatestSnapshot(aggregateId);

  let state = JSON.parse(snapshot.state);
  const snapshotVersion = snapshot.version;

  // Apply only events after snapshot
  const events = await getEventsSinceVersion(aggregateId, snapshotVersion);

  for (const event of events) {
    state = applyEvent(state, event);
  }

  return state;
};
```

## Saga Patterns

### Pattern: Choreography-Based Saga

Services coordinate through events:

```typescript
// Order Service publishes event
export const placeOrder = async (order: Order) => {
  await saveOrder(order);

  await eventBridge.putEvents({
    Entries: [{
      Source: 'orders',
      DetailType: 'OrderPlaced',
      Detail: JSON.stringify({ orderId: order.id }),
    }],
  });
};

// Inventory Service reacts to event
new events.Rule(this, 'ReserveInventory', {
  eventPattern: {
    source: ['orders'],
    detailType: ['OrderPlaced'],
  },
  targets: [new targets.LambdaFunction(reserveInventoryFunction)],
});

// Inventory Service publishes result
export const reserveInventory = async (event: any) => {
  const { orderId } = event.detail;

  try {
    await reserve(orderId);

    await eventBridge.putEvents({
      Entries: [{
        Source: 'inventory',
        DetailType: 'InventoryReserved',
        Detail: JSON.stringify({ orderId }),
      }],
    });
  } catch (error) {
    await eventBridge.putEvents({
      Entries: [{
        Source: 'inventory',
        DetailType: 'InventoryReservationFailed',
        Detail: JSON.stringify({ orderId, error: error.message }),
      }],
    });
  }
};

// Payment Service reacts to inventory event
new events.Rule(this, 'ProcessPayment', {
  eventPattern: {
    source: ['inventory'],
    detailType: ['InventoryReserved'],
  },
  targets: [new targets.LambdaFunction(processPaymentFunction)],
});
```

### Pattern: Orchestration-Based Saga

Central coordinator manages saga:

```typescript
// Step Functions orchestrates saga
const definition = new tasks.LambdaInvoke(this, 'ReserveInventory', {
  lambdaFunction: reserveInventoryFunction,
  resultPath: '$.inventory',
})
  .next(new tasks.LambdaInvoke(this, 'ProcessPayment', {
    lambdaFunction: processPaymentFunction,
    resultPath: '$.payment',
  }))
  .next(new tasks.LambdaInvoke(this, 'ShipOrder', {
    lambdaFunction: shipOrderFunction,
    resultPath: '$.shipment',
  }))
  .addCatch(
    // Compensation flow
    new tasks.LambdaInvoke(this, 'RefundPayment', {
      lambdaFunction: refundFunction,
    })
      .next(new tasks.LambdaInvoke(this, 'ReleaseInventory', {
        lambdaFunction: releaseFunction,
      })),
    {
      errors: ['States.TaskFailed'],
      resultPath: '$.error',
    }
  );

new stepfunctions.StateMachine(this, 'OrderSaga', {
  definition,
  tracingEnabled: true,
});
```

**Comparison**:

| Aspect | Choreography | Orchestration |
|--------|--------------|---------------|
| Coordination | Decentralized | Centralized |
| Coupling | Loose | Tighter |
| Visibility | Distributed logs | Single execution history |
| Debugging | Harder (trace across services) | Easier (single workflow) |
| Best for | Simple flows | Complex flows |

## Best Practices

### Idempotency

**Always make event handlers idempotent**:

```typescript
// Use idempotency keys
export const handler = async (event: any) => {
  const idempotencyKey = event.requestId || event.messageId;

  // Check if already processed
  try {
    const existing = await dynamodb.getItem({
      TableName: process.env.IDEMPOTENCY_TABLE,
      Key: { idempotencyKey },
    });

    if (existing.Item) {
      console.log('Already processed:', idempotencyKey);
      return existing.Item.result; // Return cached result
    }
  } catch (error) {
    // First time processing
  }

  // Process event
  const result = await processEvent(event);

  // Store result
  await dynamodb.putItem({
    TableName: process.env.IDEMPOTENCY_TABLE,
    Item: {
      idempotencyKey,
      result,
      processedAt: Date.now(),
    },
    // Optional: Set TTL for cleanup
    ExpirationTime: Math.floor(Date.now() / 1000) + 86400, // 24 hours
  });

  return result;
};
```

### Event Versioning

**Handle event schema evolution**:

```typescript
// Version events
interface OrderPlacedEventV1 {
  version: '1.0';
  orderId: string;
  amount: number;
}

interface OrderPlacedEventV2 {
  version: '2.0';
  orderId: string;
  amount: number;
  currency: string; // New field
}

// Handler supports multiple versions
export const handler = async (event: any) => {
  const eventVersion = event.detail.version || '1.0';

  switch (eventVersion) {
    case '1.0':
      return processV1(event.detail as OrderPlacedEventV1);
    case '2.0':
      return processV2(event.detail as OrderPlacedEventV2);
    default:
      throw new Error(`Unsupported event version: ${eventVersion}`);
  }
};

const processV1 = async (event: OrderPlacedEventV1) => {
  // Upgrade to V2 internally
  const v2Event: OrderPlacedEventV2 = {
    ...event,
    version: '2.0',
    currency: 'USD', // Default value
  };
  return processV2(v2Event);
};
```

### Eventual Consistency

**Design for eventual consistency**:

```typescript
// Service A writes to its database
export const createOrder = async (order: Order) => {
  // Write to Order database
  await orderTable.putItem({ Item: order });

  // Publish event
  await eventBridge.putEvents({
    Entries: [{
      Source: 'orders',
      DetailType: 'OrderCreated',
      Detail: JSON.stringify({ orderId: order.id }),
    }],
  });
};

// Service B eventually updates its database
export const onOrderCreated = async (event: any) => {
  const { orderId } = event.detail;

  // Fetch additional data
  const orderDetails = await getOrderDetails(orderId);

  // Update inventory database (eventual consistency)
  await inventoryTable.updateItem({
    Key: { productId: orderDetails.productId },
    UpdateExpression: 'SET reserved = reserved + :qty',
    ExpressionAttributeValues: { ':qty': orderDetails.quantity },
  });
};
```

### Error Handling in EDA

**Comprehensive error handling strategy**:

```typescript
// Dead Letter Queue for failed events
const dlq = new sqs.Queue(this, 'EventDLQ', {
  retentionPeriod: Duration.days(14),
});

// EventBridge rule with DLQ
new events.Rule(this, 'ProcessRule', {
  eventPattern: { /* ... */ },
  targets: [
    new targets.LambdaFunction(processFunction, {
      deadLetterQueue: dlq,
      maxEventAge: Duration.hours(2),
      retryAttempts: 2,
    }),
  ],
});

// Monitor DLQ
new cloudwatch.Alarm(this, 'DLQAlarm', {
  metric: dlq.metricApproximateNumberOfMessagesVisible(),
  threshold: 1,
  evaluationPeriods: 1,
});

// DLQ processor for manual review
new lambda.EventSourceMapping(this, 'DLQProcessor', {
  target: dlqProcessorFunction,
  eventSourceArn: dlq.queueArn,
  enabled: false, // Enable manually when reviewing
});
```

### Message Ordering

**When order matters**:

```typescript
// SQS FIFO for strict ordering
const fifoQueue = new sqs.Queue(this, 'OrderedQueue', {
  fifo: true,
  contentBasedDeduplication: true,
  deduplicationScope: sqs.DeduplicationScope.MESSAGE_GROUP,
  fifoThroughputLimit: sqs.FifoThroughputLimit.PER_MESSAGE_GROUP_ID,
});

// Publish with message group ID
await sqs.sendMessage({
  QueueUrl: process.env.QUEUE_URL,
  MessageBody: JSON.stringify(event),
  MessageGroupId: customerId, // All messages for same customer in order
  MessageDeduplicationId: eventId, // Prevent duplicates
});

// Kinesis for ordered streams
const stream = new kinesis.Stream(this, 'Stream', {
  shardCount: 1, // Single shard = strict ordering
});

// Partition key ensures same partition
await kinesis.putRecord({
  StreamName: process.env.STREAM_NAME,
  Data: Buffer.from(JSON.stringify(event)),
  PartitionKey: customerId, // Same key = same shard
});
```

### Deduplication

**Prevent duplicate event processing**:

```typescript
// Content-based deduplication with SQS FIFO
const queue = new sqs.Queue(this, 'Queue', {
  fifo: true,
  contentBasedDeduplication: true, // Hash of message body
});

// Manual deduplication with DynamoDB
export const handler = async (event: any) => {
  const eventId = event.id || event.messageId;

  try {
    // Conditional write (fails if exists)
    await dynamodb.putItem({
      TableName: process.env.DEDUP_TABLE,
      Item: {
        eventId,
        processedAt: Date.now(),
        ttl: Math.floor(Date.now() / 1000) + 86400, // 24h TTL
      },
      ConditionExpression: 'attribute_not_exists(eventId)',
    });

    // Event is unique, process it
    await processEvent(event);
  } catch (error) {
    if (error.code === 'ConditionalCheckFailedException') {
      console.log('Duplicate event ignored:', eventId);
      return; // Already processed
    }
    throw error; // Other error
  }
};
```

### Backpressure Handling

**Prevent overwhelming downstream systems**:

```typescript
// Control Lambda concurrency
const consumerFunction = new lambda.Function(this, 'Consumer', {
  reservedConcurrentExecutions: 10, // Max 10 concurrent
});

// SQS visibility timeout + retry logic
const queue = new sqs.Queue(this, 'Queue', {
  visibilityTimeout: Duration.seconds(300), // 5 minutes
  receiveMessageWaitTime: Duration.seconds(20), // Long polling
});

new lambda.EventSourceMapping(this, 'Consumer', {
  target: consumerFunction,
  eventSourceArn: queue.queueArn,
  batchSize: 10,
  maxConcurrency: 5, // Process 5 batches concurrently
  reportBatchItemFailures: true,
});

// Circuit breaker pattern
let consecutiveFailures = 0;
const FAILURE_THRESHOLD = 5;

export const handler = async (event: any) => {
  // Check circuit breaker
  if (consecutiveFailures >= FAILURE_THRESHOLD) {
    console.error('Circuit breaker open, skipping processing');
    throw new Error('Circuit breaker open');
  }

  try {
    await processEvent(event);
    consecutiveFailures = 0; // Reset on success
  } catch (error) {
    consecutiveFailures++;
    throw error;
  }
};
```

## Advanced Patterns

### Pattern: Event Replay

Replay events for recovery or testing:

```typescript
// Archive events for replay
const archive = new events.Archive(this, 'Archive', {
  sourceEventBus: eventBus,
  eventPattern: {
    account: [this.account],
  },
  retention: Duration.days(365),
});

// Replay programmatically
export const replayEvents = async (startTime: Date, endTime: Date) => {
  // Use AWS SDK to start replay
  await eventBridge.startReplay({
    ReplayName: `replay-${Date.now()}`,
    EventSourceArn: archive.archiveArn,
    EventStartTime: startTime,
    EventEndTime: endTime,
    Destination: {
      Arn: eventBus.eventBusArn,
    },
  });
};
```

### Pattern: Event Time vs Processing Time

Handle late-arriving events:

```typescript
// Include event timestamp
interface Event {
  eventId: string;
  eventTime: string; // When event occurred
  processingTime?: string; // When event processed
  data: any;
}

// Windowed aggregation
export const aggregateWindow = async (events: Event[]) => {
  // Group by event time window (not processing time)
  const windows = new Map<string, Event[]>();

  for (const event of events) {
    const window = getWindowForTime(new Date(event.eventTime), Duration.minutes(5));
    const key = window.toISOString();

    if (!windows.has(key)) {
      windows.set(key, []);
    }
    windows.get(key)!.push(event);
  }

  // Process each window
  for (const [window, eventsInWindow] of windows) {
    await processWindow(window, eventsInWindow);
  }
};
```

### Pattern: Transactional Outbox

Ensure event publishing with database writes:

```typescript
// Single DynamoDB transaction
export const createOrderWithEvent = async (order: Order) => {
  await dynamodb.transactWriteItems({
    TransactItems: [
      {
        // Write order
        Put: {
          TableName: process.env.ORDERS_TABLE,
          Item: marshall(order),
        },
      },
      {
        // Write outbox event
        Put: {
          TableName: process.env.OUTBOX_TABLE,
          Item: marshall({
            eventId: uuid(),
            eventType: 'OrderPlaced',
            eventData: order,
            status: 'PENDING',
            createdAt: Date.now(),
          }),
        },
      },
    ],
  });
};

// Separate Lambda processes outbox
new lambda.EventSourceMapping(this, 'OutboxProcessor', {
  target: outboxFunction,
  eventSourceArn: outboxTable.tableStreamArn,
  startingPosition: lambda.StartingPosition.LATEST,
});

export const processOutbox = async (event: DynamoDBStreamEvent) => {
  for (const record of event.Records) {
    if (record.eventName !== 'INSERT') continue;

    const outboxEvent = unmarshall(record.dynamodb?.NewImage);

    // Publish to EventBridge
    await eventBridge.putEvents({
      Entries: [{
        Source: 'orders',
        DetailType: outboxEvent.eventType,
        Detail: JSON.stringify(outboxEvent.eventData),
      }],
    });

    // Mark as processed
    await dynamodb.updateItem({
      TableName: process.env.OUTBOX_TABLE,
      Key: { eventId: outboxEvent.eventId },
      UpdateExpression: 'SET #status = :status',
      ExpressionAttributeNames: { '#status': 'status' },
      ExpressionAttributeValues: { ':status': 'PUBLISHED' },
    });
  }
};
```

## Testing Event-Driven Systems

### Pattern: Event Replay for Testing

```typescript
// Publish test events
export const publishTestEvents = async () => {
  const testEvents = [
    { source: 'orders', detailType: 'OrderPlaced', detail: { orderId: '1' } },
    { source: 'orders', detailType: 'OrderPlaced', detail: { orderId: '2' } },
  ];

  for (const event of testEvents) {
    await eventBridge.putEvents({ Entries: [event] });
  }
};

// Monitor processing
export const verifyProcessing = async () => {
  // Check downstream databases
  const order1 = await orderTable.getItem({ Key: { orderId: '1' } });
  const order2 = await orderTable.getItem({ Key: { orderId: '2' } });

  expect(order1.Item).toBeDefined();
  expect(order2.Item).toBeDefined();
};
```

### Pattern: Event Mocking

```typescript
// Mock EventBridge in tests
const mockEventBridge = {
  putEvents: jest.fn().mockResolvedValue({}),
};

// Test event publishing
test('publishes event on order creation', async () => {
  await createOrder(mockEventBridge, order);

  expect(mockEventBridge.putEvents).toHaveBeenCalledWith({
    Entries: [
      expect.objectContaining({
        Source: 'orders',
        DetailType: 'OrderPlaced',
      }),
    ],
  });
});
```

## Summary

- **Loose Coupling**: Services communicate via events, not direct calls
- **Async Processing**: Use queues and event buses for asynchronous workflows
- **Idempotency**: Always handle duplicate events gracefully
- **Dead Letter Queues**: Configure DLQs for error handling
- **Event Contracts**: Define clear schemas for events
- **Observability**: Enable tracing and monitoring across services
- **Eventual Consistency**: Design for it, don't fight it
- **Saga Patterns**: Use for distributed transactions
- **Event Sourcing**: Store events as source of truth when needed
```

## File: `plugins/serverless-eda/skills/aws-serverless-eda/references/observability-best-practices.md`
```markdown
# Serverless Observability Best Practices

Comprehensive observability patterns for serverless applications based on AWS best practices.

## Table of Contents

- [Three Pillars of Observability](#three-pillars-of-observability)
- [Metrics](#metrics)
- [Logging](#logging)
- [Tracing](#tracing)
- [Unified Observability](#unified-observability)
- [Alerting](#alerting)

## Three Pillars of Observability

### Metrics
**Numeric data measured at intervals (time series)**
- Request rate, error rate, duration
- CPU%, memory%, disk%
- Custom business metrics
- Service Level Indicators (SLIs)

### Logs
**Timestamped records of discrete events**
- Application events and errors
- State transformations
- Debugging information
- Audit trails

### Traces
**Single user's journey across services**
- Request flow through distributed system
- Service dependencies
- Latency breakdown
- Error propagation

## Metrics

### CloudWatch Metrics for Lambda

**Out-of-the-box metrics** (automatically available):
```
- Invocations
- Errors
- Throttles
- Duration
- ConcurrentExecutions
- IteratorAge (for streams)
```

**CDK Configuration**:
```typescript
const fn = new NodejsFunction(this, 'Function', {
  entry: 'src/handler.ts',
});

// Create alarms on metrics
new cloudwatch.Alarm(this, 'ErrorAlarm', {
  metric: fn.metricErrors({
    statistic: 'Sum',
    period: Duration.minutes(5),
  }),
  threshold: 10,
  evaluationPeriods: 1,
});

new cloudwatch.Alarm(this, 'DurationAlarm', {
  metric: fn.metricDuration({
    statistic: 'p99',
    period: Duration.minutes(5),
  }),
  threshold: 1000, // 1 second
  evaluationPeriods: 2,
});
```

### Custom Metrics

**Use CloudWatch Embedded Metric Format (EMF)**:

```typescript
export const handler = async (event: any) => {
  const startTime = Date.now();

  try {
    const result = await processOrder(event);

    // Emit custom metrics
    console.log(JSON.stringify({
      _aws: {
        Timestamp: Date.now(),
        CloudWatchMetrics: [{
          Namespace: 'MyApp/Orders',
          Dimensions: [['ServiceName', 'Operation']],
          Metrics: [
            { Name: 'ProcessingTime', Unit: 'Milliseconds' },
            { Name: 'OrderValue', Unit: 'None' },
          ],
        }],
      },
      ServiceName: 'OrderService',
      Operation: 'ProcessOrder',
      ProcessingTime: Date.now() - startTime,
      OrderValue: result.amount,
    }));

    return result;
  } catch (error) {
    // Emit error metric
    console.log(JSON.stringify({
      _aws: {
        CloudWatchMetrics: [{
          Namespace: 'MyApp/Orders',
          Dimensions: [['ServiceName']],
          Metrics: [{ Name: 'Errors', Unit: 'Count' }],
        }],
      },
      ServiceName: 'OrderService',
      Errors: 1,
    }));

    throw error;
  }
};
```

**Using Lambda Powertools**:

```typescript
import { Metrics, MetricUnits } from '@aws-lambda-powertools/metrics';

const metrics = new Metrics({
  namespace: 'MyApp',
  serviceName: 'OrderService',
});

export const handler = async (event: any) => {
  metrics.addMetric('Invocation', MetricUnits.Count, 1);

  const startTime = Date.now();

  try {
    const result = await processOrder(event);

    metrics.addMetric('Success', MetricUnits.Count, 1);
    metrics.addMetric('ProcessingTime', MetricUnits.Milliseconds, Date.now() - startTime);
    metrics.addMetric('OrderValue', MetricUnits.None, result.amount);

    return result;
  } catch (error) {
    metrics.addMetric('Error', MetricUnits.Count, 1);
    throw error;
  } finally {
    metrics.publishStoredMetrics();
  }
};
```

## Logging

### Structured Logging

**Use JSON format for logs**:

```typescript
// ✅ GOOD - Structured JSON logging
export const handler = async (event: any) => {
  console.log(JSON.stringify({
    level: 'INFO',
    message: 'Processing order',
    orderId: event.orderId,
    customerId: event.customerId,
    timestamp: new Date().toISOString(),
    requestId: context.requestId,
  }));

  try {
    const result = await processOrder(event);

    console.log(JSON.stringify({
      level: 'INFO',
      message: 'Order processed successfully',
      orderId: event.orderId,
      duration: Date.now() - startTime,
      timestamp: new Date().toISOString(),
    }));

    return result;
  } catch (error) {
    console.error(JSON.stringify({
      level: 'ERROR',
      message: 'Order processing failed',
      orderId: event.orderId,
      error: {
        name: error.name,
        message: error.message,
        stack: error.stack,
      },
      timestamp: new Date().toISOString(),
    }));

    throw error;
  }
};

// ❌ BAD - Unstructured logging
console.log('Processing order ' + orderId + ' for customer ' + customerId);
```

**Using Lambda Powertools Logger**:

```typescript
import { Logger } from '@aws-lambda-powertools/logger';

const logger = new Logger({
  serviceName: 'OrderService',
  logLevel: 'INFO',
});

export const handler = async (event: any, context: Context) => {
  logger.addContext(context);

  logger.info('Processing order', {
    orderId: event.orderId,
    customerId: event.customerId,
  });

  try {
    const result = await processOrder(event);

    logger.info('Order processed', {
      orderId: event.orderId,
      amount: result.amount,
    });

    return result;
  } catch (error) {
    logger.error('Order processing failed', {
      orderId: event.orderId,
      error,
    });

    throw error;
  }
};
```

### Log Levels

**Use appropriate log levels**:
- **ERROR**: Errors requiring immediate attention
- **WARN**: Warnings or recoverable errors
- **INFO**: Important business events
- **DEBUG**: Detailed debugging information (disable in production)

```typescript
const logger = new Logger({
  serviceName: 'OrderService',
  logLevel: process.env.LOG_LEVEL || 'INFO',
});

logger.debug('Detailed processing info', { data });
logger.info('Business event occurred', { event });
logger.warn('Recoverable error', { error });
logger.error('Critical failure', { error });
```

### Log Insights Queries

**Common CloudWatch Logs Insights queries**:

```
# Find errors in last hour
fields @timestamp, @message, level, error.message
| filter level = "ERROR"
| sort @timestamp desc
| limit 100

# Count errors by type
stats count() by error.name as ErrorType
| sort count desc

# Calculate p99 latency
stats percentile(duration, 99) by serviceName

# Find slow requests
fields @timestamp, orderId, duration
| filter duration > 1000
| sort duration desc
| limit 50

# Track specific customer requests
fields @timestamp, @message, orderId
| filter customerId = "customer-123"
| sort @timestamp desc
```

## Tracing

### Enable X-Ray Tracing

**Configure X-Ray for Lambda**:

```typescript
const fn = new NodejsFunction(this, 'Function', {
  entry: 'src/handler.ts',
  tracing: lambda.Tracing.ACTIVE, // Enable X-Ray
});

// API Gateway tracing
const api = new apigateway.RestApi(this, 'Api', {
  deployOptions: {
    tracingEnabled: true,
  },
});

// Step Functions tracing
new stepfunctions.StateMachine(this, 'StateMachine', {
  definition,
  tracingEnabled: true,
});
```

**Instrument application code**:

```typescript
import { captureAWSv3Client } from 'aws-xray-sdk-core';
import { DynamoDBClient } from '@aws-sdk/client-dynamodb';

// Wrap AWS SDK clients
const client = captureAWSv3Client(new DynamoDBClient({}));

// Custom segments
import AWSXRay from 'aws-xray-sdk-core';

export const handler = async (event: any) => {
  const segment = AWSXRay.getSegment();

  // Custom subsegment
  const subsegment = segment.addNewSubsegment('ProcessOrder');

  try {
    // Add annotations (indexed for filtering)
    subsegment.addAnnotation('orderId', event.orderId);
    subsegment.addAnnotation('customerId', event.customerId);

    // Add metadata (not indexed, detailed info)
    subsegment.addMetadata('orderDetails', event);

    const result = await processOrder(event);

    subsegment.addAnnotation('status', 'success');
    subsegment.close();

    return result;
  } catch (error) {
    subsegment.addError(error);
    subsegment.close();
    throw error;
  }
};
```

**Using Lambda Powertools Tracer**:

```typescript
import { Tracer } from '@aws-lambda-powertools/tracer';

const tracer = new Tracer({ serviceName: 'OrderService' });

export const handler = async (event: any) => {
  const segment = tracer.getSegment();

  // Automatically captures and traces
  const result = await tracer.captureAWSv3Client(dynamodb).getItem({
    TableName: process.env.TABLE_NAME,
    Key: { orderId: event.orderId },
  });

  // Custom annotation
  tracer.putAnnotation('orderId', event.orderId);
  tracer.putMetadata('orderDetails', event);

  return result;
};
```

### Service Map

**Visualize service dependencies** with X-Ray:
- Shows service-to-service communication
- Identifies latency bottlenecks
- Highlights error rates between services
- Tracks downstream dependencies

### Distributed Tracing Best Practices

1. **Enable tracing everywhere**: Lambda, API Gateway, Step Functions
2. **Use annotations for filtering**: Indexed fields for queries
3. **Use metadata for details**: Non-indexed detailed information
4. **Sample appropriately**: 100% for low traffic, sampled for high traffic
5. **Correlate with logs**: Include trace ID in log entries

## Unified Observability

### Correlation Between Pillars

**Include trace ID in logs**:

```typescript
export const handler = async (event: any, context: Context) => {
  const traceId = process.env._X_AMZN_TRACE_ID;

  console.log(JSON.stringify({
    level: 'INFO',
    message: 'Processing order',
    traceId,
    requestId: context.requestId,
    orderId: event.orderId,
  }));
};
```

### CloudWatch ServiceLens

**Unified view of traces and metrics**:
- Automatically correlates X-Ray traces with CloudWatch metrics
- Shows service map with metrics overlay
- Identifies performance and availability issues
- Provides end-to-end request view

### Lambda Powertools Integration

**All three pillars in one**:

```typescript
import { Logger } from '@aws-lambda-powertools/logger';
import { Tracer } from '@aws-lambda-powertools/tracer';
import { Metrics, MetricUnits } from '@aws-lambda-powertools/metrics';

const logger = new Logger({ serviceName: 'OrderService' });
const tracer = new Tracer({ serviceName: 'OrderService' });
const metrics = new Metrics({ namespace: 'MyApp', serviceName: 'OrderService' });

export const handler = async (event: any, context: Context) => {
  // Automatically adds trace context to logs
  logger.addContext(context);

  logger.info('Processing order', { orderId: event.orderId });

  // Add trace annotations
  tracer.putAnnotation('orderId', event.orderId);

  // Add metrics
  metrics.addMetric('Invocation', MetricUnits.Count, 1);

  const startTime = Date.now();

  try {
    const result = await processOrder(event);

    metrics.addMetric('Success', MetricUnits.Count, 1);
    metrics.addMetric('Duration', MetricUnits.Milliseconds, Date.now() - startTime);

    logger.info('Order processed', { orderId: event.orderId });

    return result;
  } catch (error) {
    metrics.addMetric('Error', MetricUnits.Count, 1);
    logger.error('Processing failed', { orderId: event.orderId, error });
    throw error;
  } finally {
    metrics.publishStoredMetrics();
  }
};
```

## Alerting

### Effective Alerting Strategy

**Alert on what matters**:
- **Critical**: Customer-impacting issues (errors, high latency)
- **Warning**: Approaching thresholds (80% capacity)
- **Info**: Trends and anomalies (cost spikes)

**Alarm fatigue prevention**:
- Tune thresholds based on actual patterns
- Use composite alarms to reduce noise
- Set appropriate evaluation periods
- Include clear remediation steps

### CloudWatch Alarms

**Common alarm patterns**:

```typescript
// Error rate alarm
new cloudwatch.Alarm(this, 'ErrorRateAlarm', {
  metric: new cloudwatch.MathExpression({
    expression: 'errors / invocations * 100',
    usingMetrics: {
      errors: fn.metricErrors({ statistic: 'Sum' }),
      invocations: fn.metricInvocations({ statistic: 'Sum' }),
    },
  }),
  threshold: 1, // 1% error rate
  evaluationPeriods: 2,
  alarmDescription: 'Error rate exceeded 1%',
});

// Latency alarm (p99)
new cloudwatch.Alarm(this, 'LatencyAlarm', {
  metric: fn.metricDuration({
    statistic: 'p99',
    period: Duration.minutes(5),
  }),
  threshold: 1000, // 1 second
  evaluationPeriods: 2,
  alarmDescription: 'p99 latency exceeded 1 second',
});

// Concurrent executions approaching limit
new cloudwatch.Alarm(this, 'ConcurrencyAlarm', {
  metric: fn.metricConcurrentExecutions({
    statistic: 'Maximum',
  }),
  threshold: 800, // 80% of 1000 default limit
  evaluationPeriods: 1,
  alarmDescription: 'Approaching concurrency limit',
});
```

### Composite Alarms

**Reduce alert noise**:

```typescript
const errorAlarm = new cloudwatch.Alarm(this, 'Errors', {
  metric: fn.metricErrors(),
  threshold: 10,
  evaluationPeriods: 1,
});

const throttleAlarm = new cloudwatch.Alarm(this, 'Throttles', {
  metric: fn.metricThrottles(),
  threshold: 5,
  evaluationPeriods: 1,
});

const latencyAlarm = new cloudwatch.Alarm(this, 'Latency', {
  metric: fn.metricDuration({ statistic: 'p99' }),
  threshold: 2000,
  evaluationPeriods: 2,
});

// Composite alarm (any of the above)
new cloudwatch.CompositeAlarm(this, 'ServiceHealthAlarm', {
  compositeAlarmName: 'order-service-health',
  alarmRule: cloudwatch.AlarmRule.anyOf(
    errorAlarm,
    throttleAlarm,
    latencyAlarm
  ),
  alarmDescription: 'Overall service health degraded',
});
```

## Dashboard Best Practices

### Service Dashboard Layout

**Recommended sections**:

1. **Overview**:
   - Total invocations
   - Error rate percentage
   - P50, P95, P99 latency
   - Availability percentage

2. **Resource Utilization**:
   - Concurrent executions
   - Memory utilization
   - Duration distribution
   - Throttles

3. **Business Metrics**:
   - Orders processed
   - Revenue per minute
   - Customer activity
   - Feature usage

4. **Errors and Alerts**:
   - Error count by type
   - Active alarms
   - DLQ message count
   - Failed transactions

### CloudWatch Dashboard CDK

```typescript
const dashboard = new cloudwatch.Dashboard(this, 'ServiceDashboard', {
  dashboardName: 'order-service',
});

dashboard.addWidgets(
  // Row 1: Overview
  new cloudwatch.GraphWidget({
    title: 'Invocations',
    left: [fn.metricInvocations()],
  }),
  new cloudwatch.SingleValueWidget({
    title: 'Error Rate',
    metrics: [
      new cloudwatch.MathExpression({
        expression: 'errors / invocations * 100',
        usingMetrics: {
          errors: fn.metricErrors({ statistic: 'Sum' }),
          invocations: fn.metricInvocations({ statistic: 'Sum' }),
        },
      }),
    ],
  }),
  new cloudwatch.GraphWidget({
    title: 'Latency (p50, p95, p99)',
    left: [
      fn.metricDuration({ statistic: 'p50', label: 'p50' }),
      fn.metricDuration({ statistic: 'p95', label: 'p95' }),
      fn.metricDuration({ statistic: 'p99', label: 'p99' }),
    ],
  })
);

// Row 2: Errors
dashboard.addWidgets(
  new cloudwatch.LogQueryWidget({
    title: 'Recent Errors',
    logGroupNames: [fn.logGroup.logGroupName],
    queryLines: [
      'fields @timestamp, @message',
      'filter level = "ERROR"',
      'sort @timestamp desc',
      'limit 20',
    ],
  })
);
```

## Monitoring Serverless Architectures

### End-to-End Monitoring

**Monitor the entire flow**:

```
API Gateway → Lambda → DynamoDB → EventBridge → Lambda
     ↓           ↓          ↓            ↓           ↓
  Metrics    Traces     Metrics      Metrics     Logs
```

**Key metrics per service**:

| Service | Key Metrics |
|---------|-------------|
| API Gateway | Count, 4XXError, 5XXError, Latency, CacheHitCount |
| Lambda | Invocations, Errors, Duration, Throttles, ConcurrentExecutions |
| DynamoDB | ConsumedReadCapacity, ConsumedWriteCapacity, UserErrors, SystemErrors |
| SQS | NumberOfMessagesSent, NumberOfMessagesReceived, ApproximateAgeOfOldestMessage |
| EventBridge | Invocations, FailedInvocations, TriggeredRules |
| Step Functions | ExecutionsStarted, ExecutionsFailed, ExecutionTime |

### Synthetic Monitoring

**Use CloudWatch Synthetics for API monitoring**:

```typescript
import { Canary, Test, Code, Schedule } from '@aws-cdk/aws-synthetics-alpha';

new Canary(this, 'ApiCanary', {
  canaryName: 'api-health-check',
  schedule: Schedule.rate(Duration.minutes(5)),
  test: Test.custom({
    code: Code.fromInline(`
      const synthetics = require('Synthetics');

      const apiCanaryBlueprint = async function () {
        const response = await synthetics.executeHttpStep('Verify API', {
          url: 'https://api.example.com/health',
          method: 'GET',
        });

        return response.statusCode === 200 ? 'success' : 'failure';
      };

      exports.handler = async () => {
        return await apiCanaryBlueprint();
      };
    `),
    handler: 'index.handler',
  }),
  runtime: synthetics.Runtime.SYNTHETICS_NODEJS_PUPPETEER_6_2,
});
```

## OpenTelemetry Integration

### Amazon Distro for OpenTelemetry (ADOT)

**Use ADOT for vendor-neutral observability**:

```typescript
// Lambda Layer with ADOT
const adotLayer = lambda.LayerVersion.fromLayerVersionArn(
  this,
  'AdotLayer',
  `arn:aws:lambda:${this.region}:901920570463:layer:aws-otel-nodejs-amd64-ver-1-18-1:4`
);

new NodejsFunction(this, 'Function', {
  entry: 'src/handler.ts',
  layers: [adotLayer],
  tracing: lambda.Tracing.ACTIVE,
  environment: {
    AWS_LAMBDA_EXEC_WRAPPER: '/opt/otel-handler',
    OPENTELEMETRY_COLLECTOR_CONFIG_FILE: '/var/task/collector.yaml',
  },
});
```

**Benefits of ADOT**:
- Vendor-neutral (works with Datadog, New Relic, Honeycomb, etc.)
- Automatic instrumentation
- Consistent format across services
- Export to multiple backends

## Best Practices Summary

### Metrics
- ✅ Use CloudWatch Embedded Metric Format (EMF)
- ✅ Track business metrics, not just technical metrics
- ✅ Set alarms on error rate, latency, and throughput
- ✅ Use p99 for latency, not average
- ✅ Create dashboards for key services

### Logging
- ✅ Use structured JSON logging
- ✅ Include correlation IDs (request ID, trace ID)
- ✅ Use appropriate log levels
- ✅ Never log sensitive data (PII, secrets)
- ✅ Use CloudWatch Logs Insights for analysis

### Tracing
- ✅ Enable X-Ray tracing on all services
- ✅ Instrument AWS SDK calls
- ✅ Add custom annotations for business context
- ✅ Use service map to understand dependencies
- ✅ Correlate traces with logs and metrics

### Alerting
- ✅ Alert on customer-impacting issues
- ✅ Tune thresholds to reduce false positives
- ✅ Use composite alarms to reduce noise
- ✅ Include clear remediation steps
- ✅ Escalate critical alarms appropriately

### Tools
- ✅ Use Lambda Powertools for unified observability
- ✅ Use CloudWatch ServiceLens for service view
- ✅ Use Synthetics for proactive monitoring
- ✅ Consider ADOT for vendor-neutral observability
```

## File: `plugins/serverless-eda/skills/aws-serverless-eda/references/performance-optimization.md`
```markdown
# Serverless Performance Optimization

Performance optimization best practices for AWS Lambda and serverless architectures.

## Table of Contents

- [Lambda Execution Lifecycle](#lambda-execution-lifecycle)
- [Cold Start Optimization](#cold-start-optimization)
- [Memory and CPU Optimization](#memory-and-cpu-optimization)
- [Package Size Optimization](#package-size-optimization)
- [Initialization Optimization](#initialization-optimization)
- [Runtime Performance](#runtime-performance)

## Lambda Execution Lifecycle

### Execution Environment Phases

**Three phases of Lambda execution**:

1. **Init Phase** (Cold Start):
   - Download and unpack function package
   - Create execution environment
   - Initialize runtime
   - Execute initialization code (outside handler)

2. **Invoke Phase**:
   - Execute handler code
   - Return response
   - Freeze execution environment

3. **Shutdown Phase**:
   - Runtime shutdown (after period of inactivity)
   - Execution environment destroyed

### Concurrency and Scaling

**Key concepts**:
- **Concurrency**: Number of execution environments serving requests simultaneously
- **One event per environment**: Each environment processes one event at a time
- **Automatic scaling**: Lambda creates new environments as needed
- **Environment reuse**: Warm starts reuse existing environments

**Example**:
- Function takes 100ms to execute
- Single environment can handle 10 requests/second
- 100 concurrent requests = 10 environments needed
- Default account limit: 1,000 concurrent executions (can be raised)

## Cold Start Optimization

### Understanding Cold Starts

**Cold start components**:
```
Total Cold Start = Download Package + Init Environment + Init Code + Handler
```

**Cold start frequency**:
- Development: Every code change creates new environments (frequent)
- Production: Typically < 1% of invocations
- Optimize for p95/p99 latency, not average

### Package Size Optimization

**Minimize deployment package**:

```typescript
new NodejsFunction(this, 'Function', {
  entry: 'src/handler.ts',
  bundling: {
    minify: true, // Minify production code
    sourceMap: false, // Disable in production
    externalModules: [
      '@aws-sdk/*', // Use AWS SDK from runtime
    ],
    // Tree-shaking removes unused code
  },
});
```

**Tools for optimization**:
- **esbuild**: Automatic tree-shaking and minification
- **Webpack**: Bundle optimization
- **Maven**: Dependency analysis
- **Gradle**: Unused dependency detection

**Best practices**:
1. Avoid monolithic functions
2. Bundle only required dependencies
3. Use tree-shaking to remove unused code
4. Minify production code
5. Exclude AWS SDK (provided by runtime)

### Provisioned Concurrency

**Pre-initialize environments for predictable latency**:

```typescript
const fn = new NodejsFunction(this, 'Function', {
  entry: 'src/handler.ts',
});

// Static provisioned concurrency
fn.currentVersion.addAlias('live', {
  provisionedConcurrentExecutions: 10,
});

// Auto-scaling provisioned concurrency
const alias = fn.currentVersion.addAlias('prod');

const target = new applicationautoscaling.ScalableTarget(this, 'ScalableTarget', {
  serviceNamespace: applicationautoscaling.ServiceNamespace.LAMBDA,
  maxCapacity: 100,
  minCapacity: 10,
  resourceId: `function:${fn.functionName}:${alias.aliasName}`,
  scalableDimension: 'lambda:function:ProvisionedConcurrentExecutions',
});

target.scaleOnUtilization({
  utilizationTarget: 0.7, // 70% utilization
});
```

**When to use**:
- **Consistent traffic patterns**: Predictable load
- **Latency-sensitive APIs**: Sub-100ms requirements
- **Cost consideration**: Compare cold start frequency vs. provisioned cost

**Cost comparison**:
- **On-demand**: Pay only for actual usage
- **Provisioned**: Pay for provisioned capacity + invocations
- **Breakeven**: When cold starts > ~20% of invocations

### Lambda SnapStart (Java)

**Instant cold starts for Java**:

```typescript
new lambda.Function(this, 'JavaFunction', {
  runtime: lambda.Runtime.JAVA_17,
  code: lambda.Code.fromAsset('target/function.jar'),
  handler: 'com.example.Handler::handleRequest',
  snapStart: lambda.SnapStartConf.ON_PUBLISHED_VERSIONS,
});
```

**Benefits**:
- Up to 10x faster cold starts for Java
- No code changes required
- Works with published versions
- No additional cost

## Memory and CPU Optimization

### Memory = CPU Allocation

**Key principle**: Memory and CPU are proportionally allocated

| Memory | vCPU |
|--------|------|
| 128 MB | 0.07 vCPU |
| 512 MB | 0.28 vCPU |
| 1,024 MB | 0.57 vCPU |
| 1,769 MB | 1.00 vCPU |
| 3,538 MB | 2.00 vCPU |
| 10,240 MB | 6.00 vCPU |

### Cost vs. Performance Balancing

**Example - Compute-intensive function**:

| Memory | Duration | Cost |
|--------|----------|------|
| 128 MB | 11.72s | $0.0246 |
| 256 MB | 6.68s | $0.0280 |
| 512 MB | 3.19s | $0.0268 |
| 1024 MB | 1.46s | $0.0246 |

**Key insight**: More memory = faster execution = similar or lower cost

**Formula**:
```
Duration = Allocated Memory (GB) × Execution Time (seconds)
Cost = Duration × Number of Invocations × Price per GB-second
```

### Finding Optimal Memory

**Use Lambda Power Tuning**:

```bash
# Deploy power tuning state machine
sam deploy --template-file template.yml --stack-name lambda-power-tuning

# Run power tuning
aws lambda invoke \
  --function-name powerTuningFunction \
  --payload '{"lambdaARN": "arn:aws:lambda:...", "powerValues": [128, 256, 512, 1024, 1536, 3008]}' \
  response.json
```

**Manual testing approach**:
1. Test function at different memory levels
2. Measure execution time at each level
3. Calculate cost for each configuration
4. Choose optimal balance for your use case

### Multi-Core Optimization

**Leverage multiple vCPUs** (at 1,769 MB+):

```typescript
// Use Worker Threads for parallel processing
import { Worker } from 'worker_threads';

export const handler = async (event: any) => {
  const items = event.items;

  // Process in parallel using multiple cores
  const workers = items.map(item =>
    new Promise((resolve, reject) => {
      const worker = new Worker('./worker.js', {
        workerData: item,
      });

      worker.on('message', resolve);
      worker.on('error', reject);
    })
  );

  const results = await Promise.all(workers);
  return results;
};
```

**Python multiprocessing**:

```python
import multiprocessing as mp

def handler(event, context):
    items = event['items']

    # Use multiple cores for CPU-bound work
    with mp.Pool(mp.cpu_count()) as pool:
        results = pool.map(process_item, items)

    return {'results': results}
```

## Initialization Optimization

### Code Outside Handler

**Initialize once, reuse across invocations**:

```typescript
// ✅ GOOD - Initialize outside handler
import { DynamoDBClient } from '@aws-sdk/client-dynamodb';
import { S3Client } from '@aws-sdk/client-s3';

// Initialized once per execution environment
const dynamodb = new DynamoDBClient({});
const s3 = new S3Client({});

// Connection pool initialized once
const pool = createConnectionPool({
  host: process.env.DB_HOST,
  max: 1, // One connection per execution environment
});

export const handler = async (event: any) => {
  // Reuse connections across invocations
  const data = await dynamodb.getItem({ /* ... */ });
  const file = await s3.getObject({ /* ... */ });
  return processData(data, file);
};

// ❌ BAD - Initialize in handler
export const handler = async (event: any) => {
  const dynamodb = new DynamoDBClient({}); // Created every invocation
  const s3 = new S3Client({}); // Created every invocation
  // ...
};
```

### Lazy Loading

**Load dependencies only when needed**:

```typescript
// ✅ GOOD - Conditional loading
export const handler = async (event: any) => {
  if (event.operation === 'generatePDF') {
    // Load heavy PDF library only when needed
    const pdfLib = await import('./pdf-generator');
    return pdfLib.generatePDF(event.data);
  }

  if (event.operation === 'processImage') {
    const sharp = await import('sharp');
    return processImage(sharp, event.data);
  }

  // Default operation (no heavy dependencies)
  return processDefault(event);
};

// ❌ BAD - Load everything upfront
import pdfLib from './pdf-generator'; // 50MB
import sharp from 'sharp'; // 20MB
// Even if not used!

export const handler = async (event: any) => {
  if (event.operation === 'generatePDF') {
    return pdfLib.generatePDF(event.data);
  }
};
```

### Connection Reuse

**Enable connection reuse**:

```typescript
import { DynamoDBClient } from '@aws-sdk/client-dynamodb';

const client = new DynamoDBClient({
  // Enable keep-alive for connection reuse
  requestHandler: {
    connectionTimeout: 3000,
    socketTimeout: 3000,
  },
});

// For Node.js AWS SDK
process.env.AWS_NODEJS_CONNECTION_REUSE_ENABLED = '1';
```

## Runtime Performance

### Choose the Right Runtime

**Runtime comparison**:

| Runtime | Cold Start | Execution Speed | Ecosystem | Best For |
|---------|------------|-----------------|-----------|----------|
| Node.js 20 | Fast | Fast | Excellent | APIs, I/O-bound |
| Python 3.12 | Fast | Medium | Excellent | Data processing |
| Java 17 + SnapStart | Fast (w/SnapStart) | Fast | Good | Enterprise apps |
| .NET 8 | Medium | Fast | Good | Enterprise apps |
| Go | Very Fast | Very Fast | Good | High performance |
| Rust | Very Fast | Very Fast | Growing | High performance |

### Optimize Handler Code

**Efficient code patterns**:

```typescript
// ✅ GOOD - Batch operations
const items = ['item1', 'item2', 'item3'];

// Single batch write
await dynamodb.batchWriteItem({
  RequestItems: {
    [tableName]: items.map(item => ({
      PutRequest: { Item: item },
    })),
  },
});

// ❌ BAD - Multiple single operations
for (const item of items) {
  await dynamodb.putItem({
    TableName: tableName,
    Item: item,
  }); // Slow, multiple round trips
}
```

### Async Processing

**Use async/await effectively**:

```typescript
// ✅ GOOD - Parallel async operations
const [userData, orderData, inventoryData] = await Promise.all([
  getUserData(userId),
  getOrderData(orderId),
  getInventoryData(productId),
]);

// ❌ BAD - Sequential async operations
const userData = await getUserData(userId);
const orderData = await getOrderData(orderId); // Waits unnecessarily
const inventoryData = await getInventoryData(productId); // Waits unnecessarily
```

### Caching Strategies

**Cache frequently accessed data**:

```typescript
// In-memory cache (persists in warm environments)
const cache = new Map<string, any>();

export const handler = async (event: any) => {
  const key = event.key;

  // Check cache first
  if (cache.has(key)) {
    console.log('Cache hit');
    return cache.get(key);
  }

  // Fetch from database
  const data = await fetchFromDatabase(key);

  // Store in cache
  cache.set(key, data);

  return data;
};
```

**ElastiCache for shared cache**:

```typescript
import Redis from 'ioredis';

// Initialize once
const redis = new Redis({
  host: process.env.REDIS_HOST,
  port: 6379,
  lazyConnect: true,
  enableOfflineQueue: false,
});

export const handler = async (event: any) => {
  const key = `order:${event.orderId}`;

  // Try cache
  const cached = await redis.get(key);
  if (cached) {
    return JSON.parse(cached);
  }

  // Fetch and cache
  const data = await fetchOrder(event.orderId);
  await redis.setex(key, 300, JSON.stringify(data)); // 5 min TTL

  return data;
};
```

## Performance Testing

### Load Testing

**Use Artillery for load testing**:

```yaml
# load-test.yml
config:
  target: https://api.example.com
  phases:
    - duration: 60
      arrivalRate: 10
      rampTo: 100 # Ramp from 10 to 100 req/sec
scenarios:
  - flow:
      - post:
          url: /orders
          json:
            orderId: "{{ $randomString() }}"
            amount: "{{ $randomNumber(10, 1000) }}"
```

```bash
artillery run load-test.yml
```

### Benchmarking

**Test different configurations**:

```typescript
// benchmark.ts
import { Lambda } from '@aws-sdk/client-lambda';

const lambda = new Lambda({});

const testConfigurations = [
  { memory: 128, name: 'Function-128' },
  { memory: 256, name: 'Function-256' },
  { memory: 512, name: 'Function-512' },
  { memory: 1024, name: 'Function-1024' },
];

for (const config of testConfigurations) {
  const times: number[] = [];

  // Warm up
  for (let i = 0; i < 5; i++) {
    await lambda.invoke({ FunctionName: config.name });
  }

  // Measure
  for (let i = 0; i < 100; i++) {
    const start = Date.now();
    await lambda.invoke({ FunctionName: config.name });
    times.push(Date.now() - start);
  }

  const p99 = times.sort()[99];
  const avg = times.reduce((a, b) => a + b) / times.length;

  console.log(`${config.memory}MB - Avg: ${avg}ms, p99: ${p99}ms`);
}
```

## Cost Optimization

### Right-Sizing Memory

**Balance cost and performance**:

**CPU-bound workloads**:
- More memory = more CPU = faster execution
- Often results in lower cost overall
- Test at 1769MB (1 vCPU) and above

**I/O-bound workloads**:
- Less sensitive to memory allocation
- May not benefit from higher memory
- Test at lower memory levels (256-512MB)

**Simple operations**:
- Minimal CPU required
- Use minimum memory (128-256MB)
- Fast execution despite low resources

### Billing Granularity

**Lambda bills in 1ms increments**:
- Precise billing (7ms execution = 7ms cost)
- Optimize even small improvements
- Consider trade-offs carefully

**Cost calculation**:
```
Cost = (Memory GB) × (Duration seconds) × (Invocations) × ($0.0000166667/GB-second)
     + (Invocations) × ($0.20/1M requests)
```

### Cost Reduction Strategies

1. **Optimize execution time**: Faster = cheaper
2. **Right-size memory**: Balance CPU needs with cost
3. **Reduce invocations**: Batch processing, caching
4. **Use Graviton2**: 20% better price/performance
5. **Reserved Concurrency**: Only when needed
6. **Compression**: Reduce data transfer costs

## Advanced Optimization

### Lambda Extensions

**Use extensions for cross-cutting concerns**:

```typescript
// Lambda layer with extension
const extensionLayer = lambda.LayerVersion.fromLayerVersionArn(
  this,
  'Extension',
  'arn:aws:lambda:us-east-1:123456789:layer:my-extension:1'
);

new NodejsFunction(this, 'Function', {
  entry: 'src/handler.ts',
  layers: [extensionLayer],
});
```

**Common extensions**:
- Secrets caching
- Configuration caching
- Custom logging
- Security scanning
- Performance monitoring

### Graviton2 Architecture

**20% better price/performance**:

```typescript
new NodejsFunction(this, 'Function', {
  entry: 'src/handler.ts',
  architecture: lambda.Architecture.ARM_64, // Graviton2
});
```

**Considerations**:
- Most runtimes support ARM64
- Test thoroughly before migrating
- Dependencies must support ARM64
- Native extensions may need recompilation

### VPC Optimization

**Hyperplane ENIs** (automatic since 2019):
- No ENI per function
- Faster cold starts in VPC
- Scales instantly

```typescript
// Modern VPC configuration (fast)
new NodejsFunction(this, 'VpcFunction', {
  entry: 'src/handler.ts',
  vpc,
  vpcSubnets: { subnetType: ec2.SubnetType.PRIVATE_WITH_EGRESS },
  // Fast scaling, no ENI limitations
});
```

## Performance Monitoring

### Key Metrics

**Monitor these metrics**:
- **Duration**: p50, p95, p99, max
- **Cold Start %**: ColdStartDuration / TotalDuration
- **Error Rate**: Errors / Invocations
- **Throttles**: Indicates concurrency limit reached
- **Iterator Age**: For stream processing lag

### Performance Dashboards

```typescript
const dashboard = new cloudwatch.Dashboard(this, 'PerformanceDashboard');

dashboard.addWidgets(
  new cloudwatch.GraphWidget({
    title: 'Latency Distribution',
    left: [
      fn.metricDuration({ statistic: 'p50', label: 'p50' }),
      fn.metricDuration({ statistic: 'p95', label: 'p95' }),
      fn.metricDuration({ statistic: 'p99', label: 'p99' }),
      fn.metricDuration({ statistic: 'Maximum', label: 'max' }),
    ],
  }),
  new cloudwatch.GraphWidget({
    title: 'Memory Utilization',
    left: [fn.metricDuration()],
    right: [fn.metricErrors()],
  })
);
```

## Summary

- **Cold Starts**: Optimize package size, use provisioned concurrency for critical paths
- **Memory**: More memory often = faster execution = lower cost
- **Initialization**: Initialize connections outside handler
- **Lazy Loading**: Load dependencies only when needed
- **Connection Reuse**: Enable for AWS SDK clients
- **Testing**: Test at different memory levels to find optimal configuration
- **Monitoring**: Track p99 latency, not average
- **Graviton2**: Consider ARM64 for better price/performance
- **Batch Operations**: Reduce round trips to services
- **Caching**: Cache frequently accessed data
```

## File: `plugins/serverless-eda/skills/aws-serverless-eda/references/security-best-practices.md`
```markdown
# Serverless Security Best Practices

Security best practices for serverless applications based on AWS Well-Architected Framework.

## Table of Contents

- [Shared Responsibility Model](#shared-responsibility-model)
- [Identity and Access Management](#identity-and-access-management)
- [Function Security](#function-security)
- [API Security](#api-security)
- [Data Protection](#data-protection)
- [Network Security](#network-security)

## Shared Responsibility Model

### Serverless Shifts Responsibility to AWS

With serverless, AWS takes on more security responsibilities:

**AWS Responsibilities**:
- Compute infrastructure
- Execution environment
- Runtime language and patches
- Networking infrastructure
- Server software and OS
- Physical hardware and facilities
- Automatic security patches (like Log4Shell mitigation)

**Customer Responsibilities**:
- Function code and dependencies
- Resource configuration
- Identity and Access Management (IAM)
- Data encryption (at rest and in transit)
- Application-level security
- Secure coding practices

### Benefits of Shifted Responsibility

- **Automatic Patching**: AWS applies security patches automatically (e.g., Log4Shell fixed within 3 days)
- **Infrastructure Security**: No OS patching, server hardening, or vulnerability scanning
- **Operational Agility**: Quick security response at scale
- **Focus on Code**: Spend time on business logic, not infrastructure security

## Identity and Access Management

### Least Privilege Principle

**Always use least privilege IAM policies**:

```typescript
// ✅ GOOD - Specific grant
const table = new dynamodb.Table(this, 'Table', {});
const function = new lambda.Function(this, 'Function', {});

table.grantReadData(function); // Only read access

// ❌ BAD - Overly broad
function.addToRolePolicy(new iam.PolicyStatement({
  actions: ['dynamodb:*'],
  resources: ['*'],
}));
```

### Function Execution Role

**Separate roles per function**:

```typescript
// ✅ GOOD - Each function has its own role
const readFunction = new NodejsFunction(this, 'ReadFunction', {
  entry: 'src/read.ts',
  // Gets its own execution role
});

const writeFunction = new NodejsFunction(this, 'WriteFunction', {
  entry: 'src/write.ts',
  // Gets its own execution role
});

table.grantReadData(readFunction);
table.grantReadWriteData(writeFunction);

// ❌ BAD - Shared role with excessive permissions
const sharedRole = new iam.Role(this, 'SharedRole', {
  assumedBy: new iam.ServicePrincipal('lambda.amazonaws.com'),
  managedPolicies: [
    iam.ManagedPolicy.fromAwsManagedPolicyName('AdministratorAccess'), // Too broad!
  ],
});
```

### Resource-Based Policies

Control who can invoke functions:

```typescript
// Allow API Gateway to invoke function
myFunction.grantInvoke(new iam.ServicePrincipal('apigateway.amazonaws.com'));

// Allow specific account
myFunction.addPermission('AllowAccountInvoke', {
  principal: new iam.AccountPrincipal('123456789012'),
  action: 'lambda:InvokeFunction',
});

// Conditional invoke (only from specific VPC endpoint)
myFunction.addPermission('AllowVPCInvoke', {
  principal: new iam.ServicePrincipal('lambda.amazonaws.com'),
  action: 'lambda:InvokeFunction',
  sourceArn: vpcEndpoint.vpcEndpointId,
});
```

### IAM Policies Best Practices

1. **Use grant methods**: Prefer `.grantXxx()` over manual policies
2. **Condition keys**: Use IAM conditions for fine-grained control
3. **Resource ARNs**: Always specify resource ARNs, avoid wildcards
4. **Session policies**: Use for temporary elevated permissions
5. **Service Control Policies (SCPs)**: Enforce organization-wide guardrails

## Function Security

### Lambda Isolation Model

**Each function runs in isolated sandbox**:
- Built on Firecracker microVMs
- Dedicated execution environment per function
- No shared memory between functions
- Isolated file system and network namespace
- Strong workload isolation

**Execution Environment Security**:
- One concurrent invocation per environment
- Environment may be reused (warm starts)
- `/tmp` storage persists between invocations
- Sensitive data in memory may persist

### Secure Coding Practices

**Handle sensitive data securely**:

```typescript
// ✅ GOOD - Clean up sensitive data
export const handler = async (event: any) => {
  const apiKey = process.env.API_KEY;

  try {
    const result = await callApi(apiKey);
    return result;
  } finally {
    // Clear sensitive data from memory
    delete process.env.API_KEY;
  }
};

// ✅ GOOD - Use Secrets Manager
import { SecretsManagerClient, GetSecretValueCommand } from '@aws-sdk/client-secrets-manager';

const secretsClient = new SecretsManagerClient({});

export const handler = async (event: any) => {
  const secret = await secretsClient.send(
    new GetSecretValueCommand({ SecretId: process.env.SECRET_ARN })
  );

  const apiKey = secret.SecretString;
  // Use apiKey
};
```

### Dependency Management

**Scan dependencies for vulnerabilities**:

```json
// package.json
{
  "scripts": {
    "audit": "npm audit",
    "audit:fix": "npm audit fix"
  },
  "devDependencies": {
    "snyk": "^1.0.0"
  }
}
```

**Keep dependencies updated**:
- Run `npm audit` or `pip-audit` regularly
- Use Dependabot or Snyk for automated scanning
- Update dependencies promptly when vulnerabilities found
- Use minimal dependency sets

### Environment Variable Security

**Never store secrets in environment variables**:

```typescript
// ❌ BAD - Secret in environment variable
new NodejsFunction(this, 'Function', {
  environment: {
    API_KEY: 'sk-1234567890abcdef', // Never do this!
  },
});

// ✅ GOOD - Reference to secret
new NodejsFunction(this, 'Function', {
  environment: {
    SECRET_ARN: secret.secretArn,
  },
});

secret.grantRead(myFunction);
```

## API Security

### API Gateway Security

**Authentication and Authorization**:

```typescript
// Cognito User Pool authorizer
const authorizer = new apigateway.CognitoUserPoolsAuthorizer(this, 'Authorizer', {
  cognitoUserPools: [userPool],
});

api.root.addMethod('GET', integration, {
  authorizer,
  authorizationType: apigateway.AuthorizationType.COGNITO,
});

// Lambda authorizer for custom auth
const customAuthorizer = new apigateway.TokenAuthorizer(this, 'CustomAuth', {
  handler: authorizerFunction,
  resultsCacheTtl: Duration.minutes(5),
});

// IAM authorization for service-to-service
api.root.addMethod('POST', integration, {
  authorizationType: apigateway.AuthorizationType.IAM,
});
```

### Request Validation

**Validate requests at API Gateway**:

```typescript
const validator = new apigateway.RequestValidator(this, 'Validator', {
  api,
  validateRequestBody: true,
  validateRequestParameters: true,
});

const model = api.addModel('Model', {
  schema: {
    type: apigateway.JsonSchemaType.OBJECT,
    required: ['email', 'name'],
    properties: {
      email: {
        type: apigateway.JsonSchemaType.STRING,
        format: 'email',
      },
      name: {
        type: apigateway.JsonSchemaType.STRING,
        minLength: 1,
        maxLength: 100,
      },
    },
  },
});

resource.addMethod('POST', integration, {
  requestValidator: validator,
  requestModels: {
    'application/json': model,
  },
});
```

### Rate Limiting and Throttling

```typescript
const api = new apigateway.RestApi(this, 'Api', {
  deployOptions: {
    throttlingRateLimit: 1000, // requests per second
    throttlingBurstLimit: 2000, // burst capacity
  },
});

// Per-method throttling
resource.addMethod('POST', integration, {
  methodResponses: [{ statusCode: '200' }],
  requestParameters: {
    'method.request.header.Authorization': true,
  },
  throttling: {
    rateLimit: 100,
    burstLimit: 200,
  },
});
```

### API Keys and Usage Plans

```typescript
const apiKey = api.addApiKey('ApiKey', {
  apiKeyName: 'customer-key',
});

const plan = api.addUsagePlan('UsagePlan', {
  name: 'Standard',
  throttle: {
    rateLimit: 100,
    burstLimit: 200,
  },
  quota: {
    limit: 10000,
    period: apigateway.Period.MONTH,
  },
});

plan.addApiKey(apiKey);
plan.addApiStage({
  stage: api.deploymentStage,
});
```

## Data Protection

### Encryption at Rest

**DynamoDB encryption**:

```typescript
// Default: AWS-owned CMK (no additional cost)
const table = new dynamodb.Table(this, 'Table', {
  encryption: dynamodb.TableEncryption.AWS_MANAGED, // AWS managed CMK
});

// Customer-managed CMK (for compliance)
const kmsKey = new kms.Key(this, 'Key', {
  enableKeyRotation: true,
});

const table = new dynamodb.Table(this, 'Table', {
  encryption: dynamodb.TableEncryption.CUSTOMER_MANAGED,
  encryptionKey: kmsKey,
});
```

**S3 encryption**:

```typescript
// SSE-S3 (default, no additional cost)
const bucket = new s3.Bucket(this, 'Bucket', {
  encryption: s3.BucketEncryption.S3_MANAGED,
});

// SSE-KMS (for fine-grained access control)
const bucket = new s3.Bucket(this, 'Bucket', {
  encryption: s3.BucketEncryption.KMS,
  encryptionKey: kmsKey,
});
```

**SQS/SNS encryption**:

```typescript
const queue = new sqs.Queue(this, 'Queue', {
  encryption: sqs.QueueEncryption.KMS,
  encryptionMasterKey: kmsKey,
});

const topic = new sns.Topic(this, 'Topic', {
  masterKey: kmsKey,
});
```

### Encryption in Transit

**All AWS service APIs use TLS**:
- API Gateway endpoints use HTTPS by default
- Lambda to AWS service communication encrypted
- EventBridge, SQS, SNS use TLS
- Custom domains can use ACM certificates

```typescript
// API Gateway with custom domain
const certificate = new acm.Certificate(this, 'Certificate', {
  domainName: 'api.example.com',
  validation: acm.CertificateValidation.fromDns(hostedZone),
});

const api = new apigateway.RestApi(this, 'Api', {
  domainName: {
    domainName: 'api.example.com',
    certificate,
  },
});
```

### Data Sanitization

**Validate and sanitize inputs**:

```typescript
import DOMPurify from 'isomorphic-dompurify';
import { z } from 'zod';

// Schema validation
const OrderSchema = z.object({
  orderId: z.string().uuid(),
  amount: z.number().positive(),
  email: z.string().email(),
});

export const handler = async (event: any) => {
  const body = JSON.parse(event.body);

  // Validate schema
  const result = OrderSchema.safeParse(body);
  if (!result.success) {
    return {
      statusCode: 400,
      body: JSON.stringify({ error: result.error }),
    };
  }

  // Sanitize HTML inputs
  const sanitized = {
    ...result.data,
    description: DOMPurify.sanitize(result.data.description),
  };

  await processOrder(sanitized);
};
```

## Network Security

### VPC Configuration

**Lambda in VPC for private resources**:

```typescript
const vpc = new ec2.Vpc(this, 'Vpc', {
  maxAzs: 2,
  natGateways: 1,
});

// Lambda in private subnet
const vpcFunction = new NodejsFunction(this, 'VpcFunction', {
  entry: 'src/handler.ts',
  vpc,
  vpcSubnets: {
    subnetType: ec2.SubnetType.PRIVATE_WITH_EGRESS,
  },
  securityGroups: [securityGroup],
});

// Security group for Lambda
const securityGroup = new ec2.SecurityGroup(this, 'LambdaSG', {
  vpc,
  description: 'Security group for Lambda function',
  allowAllOutbound: false, // Restrict outbound
});

// Only allow access to RDS
securityGroup.addEgressRule(
  ec2.Peer.securityGroupId(rdsSecurityGroup.securityGroupId),
  ec2.Port.tcp(3306),
  'Allow MySQL access'
);
```

### VPC Endpoints

**Use VPC endpoints for AWS services**:

```typescript
// S3 VPC endpoint (gateway endpoint, no cost)
vpc.addGatewayEndpoint('S3Endpoint', {
  service: ec2.GatewayVpcEndpointAwsService.S3,
});

// DynamoDB VPC endpoint (gateway endpoint, no cost)
vpc.addGatewayEndpoint('DynamoDBEndpoint', {
  service: ec2.GatewayVpcEndpointAwsService.DYNAMODB,
});

// Secrets Manager VPC endpoint (interface endpoint, cost applies)
vpc.addInterfaceEndpoint('SecretsManagerEndpoint', {
  service: ec2.InterfaceVpcEndpointAwsService.SECRETS_MANAGER,
  privateDnsEnabled: true,
});
```

### Security Groups

**Principle of least privilege for network access**:

```typescript
// Lambda security group
const lambdaSG = new ec2.SecurityGroup(this, 'LambdaSG', {
  vpc,
  allowAllOutbound: false,
});

// RDS security group
const rdsSG = new ec2.SecurityGroup(this, 'RDSSG', {
  vpc,
  allowAllOutbound: false,
});

// Allow Lambda to access RDS only
rdsSG.addIngressRule(
  ec2.Peer.securityGroupId(lambdaSG.securityGroupId),
  ec2.Port.tcp(3306),
  'Allow Lambda access'
);

lambdaSG.addEgressRule(
  ec2.Peer.securityGroupId(rdsSG.securityGroupId),
  ec2.Port.tcp(3306),
  'Allow RDS access'
);
```

## Security Monitoring

### CloudWatch Logs

**Enable and encrypt logs**:

```typescript
new NodejsFunction(this, 'Function', {
  entry: 'src/handler.ts',
  logRetention: logs.RetentionDays.ONE_WEEK,
  logGroup: new logs.LogGroup(this, 'LogGroup', {
    encryptionKey: kmsKey, // Encrypt logs
    retention: logs.RetentionDays.ONE_WEEK,
  }),
});
```

### CloudTrail

**Enable CloudTrail for audit**:

```typescript
const trail = new cloudtrail.Trail(this, 'Trail', {
  isMultiRegionTrail: true,
  includeGlobalServiceEvents: true,
  managementEvents: cloudtrail.ReadWriteType.ALL,
});

// Log Lambda invocations
trail.addLambdaEventSelector([{
  includeManagementEvents: true,
  readWriteType: cloudtrail.ReadWriteType.ALL,
}]);
```

### GuardDuty

**Enable GuardDuty for threat detection**:
- Analyzes VPC Flow Logs, DNS logs, CloudTrail events
- Detects unusual API activity
- Identifies compromised credentials
- Monitors for cryptocurrency mining

## Security Best Practices Checklist

### Development

- [ ] Validate and sanitize all inputs
- [ ] Scan dependencies for vulnerabilities
- [ ] Use least privilege IAM permissions
- [ ] Store secrets in Secrets Manager or Parameter Store
- [ ] Never log sensitive data
- [ ] Enable encryption for all data stores
- [ ] Use environment variables for configuration, not secrets

### Deployment

- [ ] Enable CloudTrail in all regions
- [ ] Configure VPC for sensitive workloads
- [ ] Use VPC endpoints for AWS service access
- [ ] Enable GuardDuty for threat detection
- [ ] Implement resource-based policies
- [ ] Use AWS WAF for API protection
- [ ] Enable access logging for API Gateway

### Operations

- [ ] Monitor CloudTrail for unusual activity
- [ ] Set up alarms for security events
- [ ] Rotate secrets regularly
- [ ] Review IAM policies periodically
- [ ] Audit function permissions
- [ ] Monitor GuardDuty findings
- [ ] Implement automated security responses

### Testing

- [ ] Test with least privilege policies
- [ ] Validate error handling for security failures
- [ ] Test input validation and sanitization
- [ ] Verify encryption configurations
- [ ] Test with malicious payloads
- [ ] Audit logs for security events

## Summary

- **Shared Responsibility**: AWS handles infrastructure, you handle application security
- **Least Privilege**: Use IAM grant methods, avoid wildcards
- **Encryption**: Enable encryption at rest and in transit
- **Input Validation**: Validate and sanitize all inputs
- **Dependency Security**: Scan and update dependencies regularly
- **Monitoring**: Enable CloudTrail, GuardDuty, and CloudWatch
- **Secrets Management**: Use Secrets Manager, never environment variables
- **Network Security**: Use VPC, security groups, and VPC endpoints appropriately
```

## File: `plugins/serverless-eda/skills/aws-serverless-eda/references/serverless-patterns.md`
```markdown
# Serverless Architecture Patterns

Comprehensive patterns for building serverless applications on AWS based on Well-Architected Framework principles.

## Table of Contents

- [Core Serverless Patterns](#core-serverless-patterns)
- [API Patterns](#api-patterns)
- [Data Processing Patterns](#data-processing-patterns)
- [Integration Patterns](#integration-patterns)
- [Orchestration Patterns](#orchestration-patterns)
- [Anti-Patterns](#anti-patterns)

## Core Serverless Patterns

### Pattern: Serverless Microservices

**Use case**: Independent, scalable services with separate databases

**Architecture**:
```
API Gateway → Lambda Functions → DynamoDB/RDS
              ↓ (events)
         EventBridge → Other Services
```

**CDK Implementation**:
```typescript
// User Service
const userTable = new dynamodb.Table(this, 'Users', {
  partitionKey: { name: 'userId', type: dynamodb.AttributeType.STRING },
  billingMode: dynamodb.BillingMode.PAY_PER_REQUEST,
});

const userFunction = new NodejsFunction(this, 'UserHandler', {
  entry: 'src/services/users/handler.ts',
  environment: {
    TABLE_NAME: userTable.tableName,
  },
});

userTable.grantReadWriteData(userFunction);

// Order Service (separate database)
const orderTable = new dynamodb.Table(this, 'Orders', {
  partitionKey: { name: 'orderId', type: dynamodb.AttributeType.STRING },
  billingMode: dynamodb.BillingMode.PAY_PER_REQUEST,
});

const orderFunction = new NodejsFunction(this, 'OrderHandler', {
  entry: 'src/services/orders/handler.ts',
  environment: {
    TABLE_NAME: orderTable.tableName,
    EVENT_BUS: eventBus.eventBusName,
  },
});

orderTable.grantReadWriteData(orderFunction);
eventBus.grantPutEventsTo(orderFunction);
```

**Benefits**:
- Independent deployment and scaling
- Database per service (data isolation)
- Technology diversity
- Fault isolation

### Pattern: Serverless API Backend

**Use case**: REST or GraphQL API with serverless compute

**REST API with API Gateway**:
```typescript
const api = new apigateway.RestApi(this, 'Api', {
  restApiName: 'serverless-api',
  deployOptions: {
    stageName: 'prod',
    tracingEnabled: true,
    loggingLevel: apigateway.MethodLoggingLevel.INFO,
    dataTraceEnabled: true,
    metricsEnabled: true,
  },
  defaultCorsPreflightOptions: {
    allowOrigins: apigateway.Cors.ALL_ORIGINS,
    allowMethods: apigateway.Cors.ALL_METHODS,
  },
});

// Resource-based routing
const items = api.root.addResource('items');
items.addMethod('GET', new apigateway.LambdaIntegration(listFunction));
items.addMethod('POST', new apigateway.LambdaIntegration(createFunction));

const item = items.addResource('{id}');
item.addMethod('GET', new apigateway.LambdaIntegration(getFunction));
item.addMethod('PUT', new apigateway.LambdaIntegration(updateFunction));
item.addMethod('DELETE', new apigateway.LambdaIntegration(deleteFunction));
```

**GraphQL API with AppSync**:
```typescript
const api = new appsync.GraphqlApi(this, 'Api', {
  name: 'serverless-graphql-api',
  schema: appsync.SchemaFile.fromAsset('schema.graphql'),
  authorizationConfig: {
    defaultAuthorization: {
      authorizationType: appsync.AuthorizationType.API_KEY,
    },
  },
  xrayEnabled: true,
});

// Lambda resolver
const dataSource = api.addLambdaDataSource('lambda-ds', resolverFunction);

dataSource.createResolver('QueryGetItem', {
  typeName: 'Query',
  fieldName: 'getItem',
});
```

### Pattern: Serverless Data Lake

**Use case**: Ingest, process, and analyze large-scale data

**Architecture**:
```
S3 (raw data) → Lambda (transform) → S3 (processed)
                  ↓ (catalog)
               AWS Glue → Athena (query)
```

**Implementation**:
```typescript
const rawBucket = new s3.Bucket(this, 'RawData');
const processedBucket = new s3.Bucket(this, 'ProcessedData');

// Trigger Lambda on file upload
rawBucket.addEventNotification(
  s3.EventType.OBJECT_CREATED,
  new s3n.LambdaDestination(transformFunction),
  { prefix: 'incoming/' }
);

// Transform function
export const transform = async (event: S3Event) => {
  for (const record of event.Records) {
    const key = record.s3.object.key;

    // Get raw data
    const raw = await s3.getObject({
      Bucket: record.s3.bucket.name,
      Key: key,
    });

    // Transform data
    const transformed = await transformData(raw.Body);

    // Write to processed bucket
    await s3.putObject({
      Bucket: process.env.PROCESSED_BUCKET,
      Key: `processed/${key}`,
      Body: JSON.stringify(transformed),
    });
  }
};
```

## API Patterns

### Pattern: Authorizer Pattern

**Use case**: Custom authentication and authorization

```typescript
// Lambda authorizer
const authorizer = new apigateway.TokenAuthorizer(this, 'Authorizer', {
  handler: authorizerFunction,
  identitySource: 'method.request.header.Authorization',
  resultsCacheTtl: Duration.minutes(5),
});

// Apply to API methods
const resource = api.root.addResource('protected');
resource.addMethod('GET', new apigateway.LambdaIntegration(protectedFunction), {
  authorizer,
});
```

### Pattern: Request Validation

**Use case**: Validate requests before Lambda invocation

```typescript
const requestModel = api.addModel('RequestModel', {
  contentType: 'application/json',
  schema: {
    type: apigateway.JsonSchemaType.OBJECT,
    required: ['name', 'email'],
    properties: {
      name: { type: apigateway.JsonSchemaType.STRING, minLength: 1 },
      email: { type: apigateway.JsonSchemaType.STRING, format: 'email' },
    },
  },
});

resource.addMethod('POST', integration, {
  requestValidator: new apigateway.RequestValidator(this, 'Validator', {
    api,
    validateRequestBody: true,
    validateRequestParameters: true,
  }),
  requestModels: {
    'application/json': requestModel,
  },
});
```

### Pattern: Response Caching

**Use case**: Reduce backend load and improve latency

```typescript
const api = new apigateway.RestApi(this, 'Api', {
  deployOptions: {
    cachingEnabled: true,
    cacheTtl: Duration.minutes(5),
    cacheClusterEnabled: true,
    cacheClusterSize: '0.5', // GB
  },
});

// Enable caching per method
resource.addMethod('GET', integration, {
  methodResponses: [{
    statusCode: '200',
    responseParameters: {
      'method.response.header.Cache-Control': true,
    },
  }],
});
```

## Data Processing Patterns

### Pattern: S3 Event Processing

**Use case**: Process files uploaded to S3

```typescript
const bucket = new s3.Bucket(this, 'DataBucket');

// Process images
bucket.addEventNotification(
  s3.EventType.OBJECT_CREATED,
  new s3n.LambdaDestination(imageProcessingFunction),
  { suffix: '.jpg' }
);

// Process CSV files
bucket.addEventNotification(
  s3.EventType.OBJECT_CREATED,
  new s3n.LambdaDestination(csvProcessingFunction),
  { suffix: '.csv' }
);

// Large file processing with Step Functions
bucket.addEventNotification(
  s3.EventType.OBJECT_CREATED,
  new s3n.SfnDestination(processingStateMachine),
  { prefix: 'large-files/' }
);
```

### Pattern: DynamoDB Streams Processing

**Use case**: React to database changes

```typescript
const table = new dynamodb.Table(this, 'Table', {
  partitionKey: { name: 'id', type: dynamodb.AttributeType.STRING },
  stream: dynamodb.StreamViewType.NEW_AND_OLD_IMAGES,
});

// Process stream changes
new lambda.EventSourceMapping(this, 'StreamConsumer', {
  target: streamProcessorFunction,
  eventSourceArn: table.tableStreamArn,
  startingPosition: lambda.StartingPosition.LATEST,
  batchSize: 100,
  maxBatchingWindow: Duration.seconds(5),
  bisectBatchOnError: true,
  retryAttempts: 3,
});

// Example: Sync to search index
export const processStream = async (event: DynamoDBStreamEvent) => {
  for (const record of event.Records) {
    if (record.eventName === 'INSERT' || record.eventName === 'MODIFY') {
      const newImage = record.dynamodb?.NewImage;
      await elasticSearch.index({
        index: 'items',
        id: newImage?.id.S,
        body: unmarshall(newImage),
      });
    } else if (record.eventName === 'REMOVE') {
      await elasticSearch.delete({
        index: 'items',
        id: record.dynamodb?.Keys?.id.S,
      });
    }
  }
};
```

### Pattern: Kinesis Stream Processing

**Use case**: Real-time data streaming and analytics

```typescript
const stream = new kinesis.Stream(this, 'EventStream', {
  shardCount: 2,
  streamMode: kinesis.StreamMode.PROVISIONED,
});

// Fan-out with multiple consumers
const consumer1 = new lambda.EventSourceMapping(this, 'Analytics', {
  target: analyticsFunction,
  eventSourceArn: stream.streamArn,
  startingPosition: lambda.StartingPosition.LATEST,
  batchSize: 100,
  parallelizationFactor: 10, // Process 10 batches per shard in parallel
});

const consumer2 = new lambda.EventSourceMapping(this, 'Alerting', {
  target: alertingFunction,
  eventSourceArn: stream.streamArn,
  startingPosition: lambda.StartingPosition.LATEST,
  filters: [
    lambda.FilterCriteria.filter({
      eventName: lambda.FilterRule.isEqual('CRITICAL_EVENT'),
    }),
  ],
});
```

## Integration Patterns

### Pattern: Service Integration with EventBridge

**Use case**: Decouple services with events

```typescript
const eventBus = new events.EventBus(this, 'AppBus');

// Service A publishes events
const serviceA = new NodejsFunction(this, 'ServiceA', {
  entry: 'src/services/a/handler.ts',
  environment: {
    EVENT_BUS: eventBus.eventBusName,
  },
});

eventBus.grantPutEventsTo(serviceA);

// Service B subscribes to events
new events.Rule(this, 'ServiceBRule', {
  eventBus,
  eventPattern: {
    source: ['service.a'],
    detailType: ['EntityCreated'],
  },
  targets: [new targets.LambdaFunction(serviceBFunction)],
});

// Service C subscribes to same events
new events.Rule(this, 'ServiceCRule', {
  eventBus,
  eventPattern: {
    source: ['service.a'],
    detailType: ['EntityCreated'],
  },
  targets: [new targets.LambdaFunction(serviceCFunction)],
});
```

### Pattern: API Gateway + SQS Integration

**Use case**: Async API requests without Lambda

```typescript
const queue = new sqs.Queue(this, 'RequestQueue');

const api = new apigateway.RestApi(this, 'Api');

// Direct SQS integration (no Lambda)
const sqsIntegration = new apigateway.AwsIntegration({
  service: 'sqs',
  path: `${process.env.AWS_ACCOUNT_ID}/${queue.queueName}`,
  integrationHttpMethod: 'POST',
  options: {
    credentialsRole: sqsRole,
    requestParameters: {
      'integration.request.header.Content-Type': "'application/x-www-form-urlencoded'",
    },
    requestTemplates: {
      'application/json': 'Action=SendMessage&MessageBody=$input.body',
    },
    integrationResponses: [{
      statusCode: '200',
    }],
  },
});

api.root.addMethod('POST', sqsIntegration, {
  methodResponses: [{ statusCode: '200' }],
});
```

### Pattern: EventBridge + Step Functions

**Use case**: Event-triggered workflow orchestration

```typescript
// State machine for order processing
const orderStateMachine = new stepfunctions.StateMachine(this, 'OrderFlow', {
  definition: /* ... */,
});

// EventBridge triggers state machine
new events.Rule(this, 'OrderPlacedRule', {
  eventPattern: {
    source: ['orders'],
    detailType: ['OrderPlaced'],
  },
  targets: [new targets.SfnStateMachine(orderStateMachine)],
});
```

## Orchestration Patterns

### Pattern: Sequential Workflow

**Use case**: Multi-step process with dependencies

```typescript
const definition = new tasks.LambdaInvoke(this, 'Step1', {
  lambdaFunction: step1Function,
  outputPath: '$.Payload',
})
  .next(new tasks.LambdaInvoke(this, 'Step2', {
    lambdaFunction: step2Function,
    outputPath: '$.Payload',
  }))
  .next(new tasks.LambdaInvoke(this, 'Step3', {
    lambdaFunction: step3Function,
    outputPath: '$.Payload',
  }));

new stepfunctions.StateMachine(this, 'Sequential', {
  definition,
});
```

### Pattern: Parallel Execution

**Use case**: Execute independent tasks concurrently

```typescript
const parallel = new stepfunctions.Parallel(this, 'ParallelProcessing');

parallel.branch(new tasks.LambdaInvoke(this, 'ProcessA', {
  lambdaFunction: functionA,
}));

parallel.branch(new tasks.LambdaInvoke(this, 'ProcessB', {
  lambdaFunction: functionB,
}));

parallel.branch(new tasks.LambdaInvoke(this, 'ProcessC', {
  lambdaFunction: functionC,
}));

const definition = parallel.next(new tasks.LambdaInvoke(this, 'Aggregate', {
  lambdaFunction: aggregateFunction,
}));

new stepfunctions.StateMachine(this, 'Parallel', { definition });
```

### Pattern: Map State (Dynamic Parallelism)

**Use case**: Process array of items in parallel

```typescript
const mapState = new stepfunctions.Map(this, 'ProcessItems', {
  maxConcurrency: 10,
  itemsPath: '$.items',
});

mapState.iterator(new tasks.LambdaInvoke(this, 'ProcessItem', {
  lambdaFunction: processItemFunction,
}));

const definition = mapState.next(new tasks.LambdaInvoke(this, 'Finalize', {
  lambdaFunction: finalizeFunction,
}));
```

### Pattern: Choice State (Conditional Logic)

**Use case**: Branching logic based on input

```typescript
const choice = new stepfunctions.Choice(this, 'OrderType');

choice.when(
  stepfunctions.Condition.stringEquals('$.orderType', 'STANDARD'),
  standardProcessing
);

choice.when(
  stepfunctions.Condition.stringEquals('$.orderType', 'EXPRESS'),
  expressProcessing
);

choice.otherwise(defaultProcessing);
```

### Pattern: Wait State

**Use case**: Delay between steps or wait for callbacks

```typescript
// Fixed delay
const wait = new stepfunctions.Wait(this, 'Wait30Seconds', {
  time: stepfunctions.WaitTime.duration(Duration.seconds(30)),
});

// Wait until timestamp
const waitUntil = new stepfunctions.Wait(this, 'WaitUntil', {
  time: stepfunctions.WaitTime.timestampPath('$.expiryTime'),
});

// Wait for callback (.waitForTaskToken)
const waitForCallback = new tasks.LambdaInvoke(this, 'WaitForApproval', {
  lambdaFunction: approvalFunction,
  integrationPattern: stepfunctions.IntegrationPattern.WAIT_FOR_TASK_TOKEN,
  payload: stepfunctions.TaskInput.fromObject({
    token: stepfunctions.JsonPath.taskToken,
    data: stepfunctions.JsonPath.entirePayload,
  }),
});
```

## Anti-Patterns

### ❌ Lambda Monolith

**Problem**: Single Lambda handling all operations

```typescript
// BAD
export const handler = async (event: any) => {
  switch (event.operation) {
    case 'createUser': return createUser(event);
    case 'getUser': return getUser(event);
    case 'updateUser': return updateUser(event);
    case 'deleteUser': return deleteUser(event);
    case 'createOrder': return createOrder(event);
    // ... 20 more operations
  }
};
```

**Solution**: Separate Lambda functions per operation

```typescript
// GOOD - Separate functions
export const createUser = async (event: any) => { /* ... */ };
export const getUser = async (event: any) => { /* ... */ };
export const updateUser = async (event: any) => { /* ... */ };
```

### ❌ Recursive Lambda Pattern

**Problem**: Lambda invoking itself (runaway costs)

```typescript
// BAD
export const handler = async (event: any) => {
  await processItem(event);

  if (hasMoreItems()) {
    await lambda.invoke({
      FunctionName: process.env.AWS_LAMBDA_FUNCTION_NAME,
      InvocationType: 'Event',
      Payload: JSON.stringify({ /* next batch */ }),
    });
  }
};
```

**Solution**: Use SQS or Step Functions

```typescript
// GOOD - Use SQS for iteration
export const handler = async (event: SQSEvent) => {
  for (const record of event.Records) {
    await processItem(record);
  }
  // SQS handles iteration automatically
};
```

### ❌ Lambda Chaining

**Problem**: Lambda directly invoking another Lambda

```typescript
// BAD
export const handler1 = async (event: any) => {
  const result = await processStep1(event);

  // Directly invoking next Lambda
  await lambda.invoke({
    FunctionName: 'handler2',
    Payload: JSON.stringify(result),
  });
};
```

**Solution**: Use EventBridge, SQS, or Step Functions

```typescript
// GOOD - Publish to EventBridge
export const handler1 = async (event: any) => {
  const result = await processStep1(event);

  await eventBridge.putEvents({
    Entries: [{
      Source: 'service.step1',
      DetailType: 'Step1Completed',
      Detail: JSON.stringify(result),
    }],
  });
};
```

### ❌ Synchronous Waiting in Lambda

**Problem**: Lambda waiting for slow operations

```typescript
// BAD - Blocking on slow operation
export const handler = async (event: any) => {
  await startBatchJob(); // Returns immediately

  // Wait for job to complete (wastes Lambda time)
  while (true) {
    const status = await checkJobStatus();
    if (status === 'COMPLETE') break;
    await sleep(1000);
  }
};
```

**Solution**: Use Step Functions with callback pattern

```typescript
// GOOD - Step Functions waits, not Lambda
const waitForJob = new tasks.LambdaInvoke(this, 'StartJob', {
  lambdaFunction: startJobFunction,
  integrationPattern: stepfunctions.IntegrationPattern.WAIT_FOR_TASK_TOKEN,
  payload: stepfunctions.TaskInput.fromObject({
    token: stepfunctions.JsonPath.taskToken,
  }),
});
```

### ❌ Large Deployment Packages

**Problem**: Large Lambda packages increase cold start time

**Solution**:
- Use layers for shared dependencies
- Externalize AWS SDK
- Minimize bundle size

```typescript
new NodejsFunction(this, 'Function', {
  entry: 'src/handler.ts',
  bundling: {
    minify: true,
    externalModules: ['@aws-sdk/*'], // Provided by runtime
    nodeModules: ['only-needed-deps'], // Selective bundling
  },
});
```

## Performance Optimization

### Cold Start Optimization

**Techniques**:
1. Minimize package size
2. Use provisioned concurrency for critical paths
3. Lazy load dependencies
4. Reuse connections outside handler
5. Use Lambda SnapStart (Java)

```typescript
// For latency-sensitive APIs
const apiFunction = new NodejsFunction(this, 'ApiFunction', {
  entry: 'src/api.ts',
  memorySize: 1769, // 1 vCPU for faster initialization
});

const alias = apiFunction.currentVersion.addAlias('live');
alias.addAutoScaling({
  minCapacity: 2,
  maxCapacity: 10,
}).scaleOnUtilization({
  utilizationTarget: 0.7,
});
```

### Right-Sizing Memory

**Test different memory configurations**:

```typescript
// CPU-bound workload
new NodejsFunction(this, 'ComputeFunction', {
  memorySize: 1769, // 1 vCPU
  timeout: Duration.seconds(30),
});

// I/O-bound workload
new NodejsFunction(this, 'IOFunction', {
  memorySize: 512, // Less CPU needed
  timeout: Duration.seconds(60),
});

// Simple operations
new NodejsFunction(this, 'SimpleFunction', {
  memorySize: 256,
  timeout: Duration.seconds(10),
});
```

### Concurrent Execution Control

```typescript
// Protect downstream services
new NodejsFunction(this, 'Function', {
  reservedConcurrentExecutions: 10, // Max 10 concurrent
});

// Unreserved concurrency (shared pool)
new NodejsFunction(this, 'Function', {
  // Uses unreserved account concurrency
});
```

## Testing Strategies

### Unit Testing

Test business logic separate from AWS services:

```typescript
// handler.ts
export const processOrder = async (order: Order): Promise<Result> => {
  // Business logic (easily testable)
  const validated = validateOrder(order);
  const priced = calculatePrice(validated);
  return transformResult(priced);
};

export const handler = async (event: any): Promise<any> => {
  const order = parseEvent(event);
  const result = await processOrder(order);
  await saveToDatabase(result);
  return formatResponse(result);
};

// handler.test.ts
test('processOrder calculates price correctly', () => {
  const order = { items: [{ price: 10, quantity: 2 }] };
  const result = processOrder(order);
  expect(result.total).toBe(20);
});
```

### Integration Testing

Test with actual AWS services:

```typescript
// integration.test.ts
import { LambdaClient, InvokeCommand } from '@aws-sdk/client-lambda';

test('Lambda processes order correctly', async () => {
  const lambda = new LambdaClient({});

  const response = await lambda.send(new InvokeCommand({
    FunctionName: process.env.FUNCTION_NAME,
    Payload: JSON.stringify({ orderId: '123' }),
  }));

  const result = JSON.parse(Buffer.from(response.Payload!).toString());
  expect(result.statusCode).toBe(200);
});
```

### Local Testing with SAM

```bash
# Test API locally
sam local start-api

# Invoke function locally
sam local invoke MyFunction -e events/test-event.json

# Generate sample event
sam local generate-event apigateway aws-proxy > event.json
```

## Summary

- **Single Purpose**: One function, one responsibility
- **Concurrent Design**: Think concurrency, not volume
- **Stateless**: Use external storage for state
- **State Machines**: Orchestrate with Step Functions
- **Event-Driven**: Use events over direct calls
- **Idempotent**: Handle failures and duplicates gracefully
- **Observability**: Enable tracing and structured logging
```


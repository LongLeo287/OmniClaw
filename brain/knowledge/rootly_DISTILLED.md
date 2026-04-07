---
id: rootly
type: knowledge
owner: OA_Triage
---
# rootly
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
<!-- mcp-name: com.rootly/mcp-server -->
# Rootly MCP Server

[![PyPI version](https://badge.fury.io/py/rootly-mcp-server.svg)](https://pypi.org/project/rootly-mcp-server/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/rootly-mcp-server)](https://pypi.org/project/rootly-mcp-server/)
[![Python Version](https://img.shields.io/pypi/pyversions/rootly-mcp-server.svg)](https://pypi.org/project/rootly-mcp-server/)
[![Install MCP Server](https://cursor.com/deeplink/mcp-install-dark.svg)](https://cursor.com/install-mcp?name=rootly&config=eyJ1cmwiOiJodHRwczovL21jcC5yb290bHkuY29tL3NzZSIsImhlYWRlcnMiOnsiQXV0aG9yaXphdGlvbiI6IkJlYXJlciA8WU9VUl9ST09UTFlfQVBJX1RPS0VOPiJ9fQ==)

An MCP server for the [Rootly API](https://docs.rootly.com/api-reference/overview) for Cursor, Windsurf, Claude, and other MCP clients.

![Demo GIF](https://raw.githubusercontent.com/Rootly-AI-Labs/Rootly-MCP-server/refs/heads/main/rootly-mcp-server-demo.gif)

## Quick Start

Use the hosted MCP server. No local installation required.

### Hosted Transport Options

- **Streamable HTTP (recommended):** `https://mcp.rootly.com/mcp`
- **SSE (fallback):** `https://mcp.rootly.com/sse`
- **Code Mode:** `https://mcp.rootly.com/mcp-codemode`

### General Remote Setup

Default remote config (HTTP streamable):

```json
{
  "mcpServers": {
    "rootly": {
      "url": "https://mcp.rootly.com/mcp",
      "headers": {
        "Authorization": "Bearer YOUR_ROOTLY_API_TOKEN"
      }
    }
  }
}
```

SSE fallback:

```json
{
  "mcpServers": {
    "rootly": {
      "url": "https://mcp.rootly.com/sse",
      "headers": {
        "Authorization": "Bearer YOUR_ROOTLY_API_TOKEN"
      }
    }
  }
}
```

Code Mode:

```json
{
  "mcpServers": {
    "rootly": {
      "url": "https://mcp.rootly.com/mcp-codemode",
      "headers": {
        "Authorization": "Bearer YOUR_ROOTLY_API_TOKEN"
      }
    }
  }
}
```

### Agent Setup

<details>
<summary><strong>Claude Code</strong></summary>

<br>

**Streamable HTTP**

```bash
claude mcp add --transport http rootly https://mcp.rootly.com/mcp \
  --header "Authorization: Bearer YOUR_ROOTLY_API_TOKEN"
```

Code Mode:

```bash
claude mcp add rootly-codemode --transport http https://mcp.rootly.com/mcp-codemode \
  --header "Authorization: Bearer YOUR_ROOTLY_API_TOKEN"
```

SSE fallback:

```bash
claude mcp add --transport sse rootly-sse https://mcp.rootly.com/sse \
  --header "Authorization: Bearer YOUR_ROOTLY_API_TOKEN"
```

**Manual Configuration**

Create `.mcp.json` in your project root:

```json
{
  "mcpServers": {
    "rootly": {
      "type": "sse",
      "url": "https://mcp.rootly.com/sse",
      "headers": {
        "Authorization": "Bearer YOUR_ROOTLY_API_TOKEN"
      }
    }
  }
}
```

Restart Claude Code after updating the config.

</details>

<details>
<summary><strong>Gemini CLI</strong></summary>

<br>

Install the extension:

```bash
gemini extensions install https://github.com/Rootly-AI-Labs/Rootly-MCP-server
```

Or configure manually in `~/.gemini/settings.json`:

```json
{
  "mcpServers": {
    "rootly": {
      "command": "uvx",
      "args": ["--from", "rootly-mcp-server", "rootly-mcp-server"],
      "env": {
        "ROOTLY_API_TOKEN": "<YOUR_ROOTLY_API_TOKEN>"
      }
    }
  }
}
```

</details>

<details>
<summary><strong>Cursor</strong></summary>

<br>

Add to `.cursor/mcp.json` or `~/.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "rootly": {
      "url": "https://mcp.rootly.com/mcp",
      "headers": {
        "Authorization": "Bearer <YOUR_ROOTLY_API_TOKEN>"
      }
    }
  }
}
```

</details>

<details>
<summary><strong>Windsurf</strong></summary>

<br>

Add to `~/.codeium/windsurf/mcp_config.json`:

```json
{
  "mcpServers": {
    "rootly": {
      "serverUrl": "https://mcp.rootly.com/mcp",
      "headers": {
        "Authorization": "Bearer <YOUR_ROOTLY_API_TOKEN>"
      }
    }
  }
}
```

</details>

<details>
<summary><strong>Codex</strong></summary>

<br>

Add to `~/.codex/config.toml`:

```toml
[mcp_servers.rootly]
url = "https://mcp.rootly.com/mcp"
bearer_token_env_var = "ROOTLY_API_TOKEN"
```

</details>

<details>
<summary><strong>Claude Desktop</strong></summary>

<br>

Add to `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "rootly": {
      "command": "npx",
      "args": [
        "-y",
        "mcp-remote",
        "https://mcp.rootly.com/mcp",
        "--header",
        "Authorization: Bearer <YOUR_ROOTLY_API_TOKEN>"
      ]
    }
  }
}
```

</details>

## Rootly CLI

Standalone CLI for incidents, alerts, services, and on-call operations.

Install via Homebrew:

```bash
brew install rootlyhq/tap/rootly-cli
```

Or via Go:

```bash
go install github.com/rootlyhq/rootly-cli/cmd/rootly@latest
```

For more details, see the [Rootly CLI repository](https://github.com/rootlyhq/rootly-cli).

## Alternative Installation (Local)

Run the MCP server locally if you do not want to use the hosted service.

### Prerequisites

- Python 3.12 or higher
- `uv` package manager
  ```bash
  curl -LsSf https://astral.sh/uv/install.sh | sh
  ```
- [Rootly API token](https://docs.rootly.com/api-reference/overview#how-to-generate-an-api-key%3F)

### API Token Types

Choose the token type based on the access you need:

- **Global API Key**: Full access across the Rootly instance. Best for organization-wide visibility.
- **Team API Key**: Access limited to entities owned by that team.
- **Personal API Key**: Access matches the user who created it.

A **Global API Key** is recommended for tools like `get_oncall_handoff_summary`, `get_oncall_shift_metrics`, and org-wide incident search.

### With uv

```json
{
  "mcpServers": {
    "rootly": {
      "command": "uv",
      "args": [
        "tool",
        "run",
        "--from",
        "rootly-mcp-server",
        "rootly-mcp-server"
      ],
      "env": {
        "ROOTLY_API_TOKEN": "<YOUR_ROOTLY_API_TOKEN>"
      }
    }
  }
}
```

## Self-Hosted Transport Options

Choose one transport per server process:

- **Streamable HTTP** endpoint path: `/mcp`
- **SSE** endpoint path: `/sse`
- **Code Mode (experimental)** endpoint path: `/mcp-codemode` in hosted dual-transport mode

Example Docker run (Streamable HTTP):

```bash
docker run -p 8000:8000 \
  -e ROOTLY_TRANSPORT=streamable-http \
  -e ROOTLY_API_TOKEN=<YOUR_ROOTLY_API_TOKEN> \
  rootly-mcp-server
```

Example Docker run (SSE):

```bash
docker run -p 8000:8000 \
  -e ROOTLY_TRANSPORT=sse \
  -e ROOTLY_API_TOKEN=<YOUR_ROOTLY_API_TOKEN> \
  rootly-mcp-server
```

Example Docker run (Dual transport + Code Mode):

```bash
docker run -p 8000:8000 \
  -e ROOTLY_TRANSPORT=both \
  -e ROOTLY_API_TOKEN=<YOUR_ROOTLY_API_TOKEN> \
  rootly-mcp-server
```

### With uvx

```json
{
  "mcpServers": {
    "rootly": {
      "command": "uvx",
      "args": [
        "--from",
        "rootly-mcp-server",
        "rootly-mcp-server"
      ],
      "env": {
        "ROOTLY_API_TOKEN": "<YOUR_ROOTLY_API_TOKEN>"
      }
    }
  }
}
```

## Features

- **Dynamic Tool Generation**: Automatically creates MCP resources from Rootly's OpenAPI (Swagger) specification
- **Smart Pagination**: Defaults to 10 items per request for incident endpoints to prevent context window overflow
- **API Filtering**: Limits exposed API endpoints for security and performance
- **Intelligent Incident Analysis**: Smart tools that analyze historical incident data
  - **`find_related_incidents`**: Uses TF-IDF similarity analysis to find historically similar incidents
  - **`suggest_solutions`**: Mines past incident resolutions to recommend actionable solutions
- **MCP Resources**: Exposes incident and team data as structured resources for easy AI reference
- **Intelligent Pattern Recognition**: Automatically identifies services, error types, and resolution patterns
- **On-Call Health Integration**: Detects workload health risk in scheduled responders

## Supported Tools

The default server configuration exposes **101 tools**.

### Custom Agentic Tools

- `check_oncall_health_risk`
- `check_responder_availability`
- `create_override_recommendation`
- `find_related_incidents`
- `getIncident` - retrieve a single incident for direct verification, including PIR-related fields
- `get_alert_by_short_id`
- `get_oncall_handoff_summary`
- `get_oncall_schedule_summary`
- `get_oncall_shift_metrics`
- `get_server_version`
- `get_shift_incidents`
- `list_endpoints`
- `list_shifts`
- `search_incidents`
- `suggest_solutions`
- `updateIncident` - scoped incident update tool for `summary` and `retrospective_progress_status`

### OpenAPI-Generated Tools

```text
attachAlert
createAlert
createEnvironment
createEscalationLevel
createEscalationLevelPaths
createEscalationPath
createEscalationPolicy
createFunctionality
createIncidentActionItem
createIncidentType
createOnCallRole
createOnCallShadow
createOverrideShift
createSchedule
createScheduleRotation
createScheduleRotationActiveDay
createScheduleRotationUser
createService
createSeverity
createTeam
createWorkflow
deleteEscalationLevel
deleteEscalationPath
deleteEscalationPolicy
deleteSchedule
deleteScheduleRotation
getAlert
getCurrentUser
getEnvironment
getEscalationLevel
getEscalationPath
getEscalationPolicy
getFunctionality
getIncidentType
getOnCallRole
getOnCallShadow
getOverrideShift
getSchedule
getScheduleRotation
getScheduleShifts
getService
getSeverity
getTeam
getUser
getWorkflow
listAlerts
listEnvironments
listEscalationLevels
listEscalationLevelsPaths
listEscalationPaths
listEscalationPolicies
listFunctionalities
listIncidentActionItems
listIncidentAlerts
listIncident_Types
listOnCallRoles
listOnCallShadows
listOverrideShifts
listScheduleRotationActiveDays
listScheduleRotationUsers
listScheduleRotations
listSchedules
listServices
listSeverities
listShifts
listTeams
listUsers
listWorkflows
updateAlert
updateEnvironment
updateEscalationLevel
updateEscalationPath
updateEscalationPolicy
updateFunctionality
updateIncidentType
updateOnCallRole
updateOnCallShadow
updateOverrideShift
updateSchedule
updateScheduleRotation
updateService
updateSeverity
updateTeam
updateUser
updateWorkflow
```

Delete operations are intentionally scoped to screenshot coverage paths:
`deleteSchedule`, `deleteScheduleRotation`, `deleteEscalationPolicy`, `deleteEscalationPath`, `deleteEscalationLevel`.

## On-Call Health Integration

Integrates with [On-Call Health](https://oncallhealth.ai) to detect workload health risk in scheduled responders.

### Setup

Set the `ONCALLHEALTH_API_KEY` environment variable:

```json
{
  "mcpServers": {
    "rootly": {
      "command": "uvx",
      "args": ["rootly-mcp-server"],
      "env": {
        "ROOTLY_API_TOKEN": "your_rootly_token",
        "ONCALLHEALTH_API_KEY": "och_live_your_key"
      }
    }
  }
}
```

### Usage

```
check_oncall_health_risk(
    start_date="2026-02-09",
    end_date="2026-02-15"
)
```

Returns at-risk users who are scheduled, recommended safe replacements, and action summaries.

## Example Skills

Pre-built Claude Code skills:

### 🚨 [Rootly Incident Responder](examples/skills/rootly-incident-responder.md)

This skill:
- Analyzes production incidents with full context
- Finds similar historical incidents using ML-based similarity matching
- Suggests solutions based on past successful resolutions
- Coordinates with on-call teams across timezones
- Correlates incidents with recent code changes and deployments
- Creates action items and remediation plans
- Provides confidence scores and time estimates

**Quick Start:**
```bash
# Copy the skill to your project
mkdir -p .claude/skills
cp examples/skills/rootly-incident-responder.md .claude/skills/

# Then in Claude Code, invoke it:
# @rootly-incident-responder analyze incident #12345
```

It demonstrates a full incident response workflow using Rootly tools and GitHub context.

### On-Call Shift Metrics

Get on-call shift metrics for any time period, grouped by user, team, or schedule. Includes primary/secondary role tracking, shift counts, hours, and days on-call.

```
get_oncall_shift_metrics(
    start_date="2025-10-01",
    end_date="2025-10-31",
    group_by="user"
)
```

### On-Call Handoff Summary

Complete handoff: current/next on-call + incidents during shifts.

```python
# All on-call (any timezone)
get_oncall_handoff_summary(
    team_ids="team-1,team-2",
    timezone="America/Los_Angeles"
)

# Regional filter - only show APAC on-call during APAC business hours
get_oncall_handoff_summary(
    timezone="Asia/Tokyo",
    filter_by_region=True
)
```

Regional filtering shows only people on-call during business hours (9am-5pm) in the specified timezone.

Returns: `schedules` with `current_oncall`, `next_oncall`, and `shift_incidents`

### Shift Incidents

Incidents during a time period, with filtering by severity/status/tags.

```python
get_shift_incidents(
    start_time="2025-10-20T09:00:00Z",
    end_time="2025-10-20T17:00:00Z",
    severity="critical",  # optional
    status="resolved",    # optional
    tags="database,api"   # optional
)
```

Returns: `incidents` list + `summary` (counts, avg resolution time, grouping)


## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for developer setup and guidelines.

## Play with it on Postman
[<img src="https://run.pstmn.io/button.svg" alt="Run In Postman" style="width: 128px; height: 32px;">](https://god.gw.postman.com/run-collection/45004446-1074ba3c-44fe-40e3-a932-af7c071b96eb?action=collection%2Ffork&source=rip_markdown&collection-url=entityId%3D45004446-1074ba3c-44fe-40e3-a932-af7c071b96eb%26entityType%3Dcollection%26workspaceId%3D4bec6e3c-50a0-4746-85f1-00a703c32f24)


## About Rootly AI Labs

This project was developed by [Rootly AI Labs](https://labs.rootly.ai/), where we're building the future of system reliability and operational excellence. As an open-source incubator, we share ideas, experiment, and rapidly prototype solutions that benefit the entire community.
![Rootly AI logo](https://github.com/Rootly-AI-Labs/EventOrOutage/raw/main/rootly-ai.png)

```

### File: tests\README.md
```md
# Rootly MCP Server Testing Guide

This directory contains comprehensive testing tools for the Rootly MCP Server, including unit tests, integration tests, and development utilities.

## Quick Start

**1. Install dependencies:**
```bash
uv sync --dev
```

**2. Set API token:**
```bash
export ROOTLY_API_TOKEN="your_rootly_api_token_here"
```

**3. Run tests:**
```bash
# All tests
uv run pytest

# Unit tests only (fast)
uv run pytest tests/unit/

# Integration tests
uv run pytest tests/integration/

# Remote server tests (requires token)
uv run pytest tests/integration/remote/ -m remote
```

## Test Structure

```
tests/
├── conftest.py                 # Shared fixtures and configuration
├── unit/                       # Unit tests (fast, no external dependencies)
│   ├── test_server.py         # Server creation, configuration
│   ├── test_authentication.py # Auth logic (hosted vs local)
│   └── test_tools.py          # Tool integration
├── integration/               # Integration tests
│   ├── local/                 # Local server testing
│   │   └── test_basic.py      # Basic functionality
│   └── remote/                # Remote server testing  
│       └── test_essential.py  # 5 critical remote tests
└── test_client.py             # Manual testing utility
```

## Token Setup

### Getting a Token
1. Go to [Rootly API Documentation](https://docs.rootly.com/api-reference/overview#how-to-generate-an-api-key%3F)
2. Create account and generate API token
3. Token should start with `rootly_` and be ~71 characters

### Setting Token

**For current session (temporary):**
```bash
export ROOTLY_API_TOKEN="rootly_your_token_here"
```

**For permanent setup:**
```bash
# Bash
echo 'export ROOTLY_API_TOKEN="rootly_your_token_here"' >> ~/.bashrc
source ~/.bashrc

# Zsh
echo 'export ROOTLY_API_TOKEN="rootly_your_token_here"' >> ~/.zshrc
source ~/.zshrc
```

**Verify token:**
```bash
echo "Token length: ${#ROOTLY_API_TOKEN}"  # Should be ~71
echo "Token prefix: ${ROOTLY_API_TOKEN:0:7}"  # Should be "rootly_"
```

## Test Categories

### Unit Tests (31 tests)
**Fast, no external dependencies**
- Server creation and configuration
- Authentication logic (hosted vs local modes)
- HTTP client functionality
- Tool integration

```bash
# Run unit tests
uv run pytest tests/unit/ -v

# With coverage
uv run pytest tests/unit/ --cov=src/rootly_mcp_server
```

### Local Integration Tests (13 tests)
**Test local server functionality**
- Server creation with real configuration
- Authentication with environment tokens
- Basic API integration

```bash
# Run local integration tests
uv run pytest tests/integration/local/ -v
```

### Remote Integration Tests (13 tests)
**Test remote server functionality (uses mocks)**
- Remote server connectivity
- Bearer token authentication
- Tool listing and execution
- Response time validation
- Error handling

```bash
# Run remote tests
uv run pytest tests/integration/remote/ -v
```

## Test Markers

Use pytest markers to run specific test categories:

```bash
# Run only unit tests
uv run pytest -m unit

# Run only integration tests  
uv run pytest -m integration

# Run only remote tests
uv run pytest -m remote

# Run tests that require API token
uv run pytest -m "not remote"  # Skip remote tests
```

## Development Workflow

### Before Making Changes
```bash
# Run full test suite to establish baseline
uv run pytest
```

### After Making Changes
```bash
# Quick feedback loop
uv run pytest tests/unit/ -x  # Stop on first failure

# If unit tests pass, run integration
uv run pytest tests/integration/local/ -x

# Check code quality
uv run ruff check .
uv run pyright
```

### Before Committing
```bash
# Full test suite with coverage
uv run pytest --cov=src/rootly_mcp_server --cov-report=term-missing
```

## Manual Testing Tool

### `test_client.py`
Interactive test client for manual verification:

```bash
python test_client.py
```

**What it tests:**
- ✅ Server initialization (24+ tools expected)
- ✅ Authentication modes (hosted vs local)
- ✅ Tool functionality (search_incidents with limits)
- ✅ API connectivity and error handling

**Use when:**
- Debugging authentication issues
- Verifying new functionality manually
- Troubleshooting API connectivity
- Testing against live remote server

## GitHub Actions CI/CD

Tests run automatically on push/PR via `.github/workflows/test.yml`:

**Pull Request Testing:**
- Code quality checks (ruff, pyright)
- Unit tests with coverage
- Local integration tests

**Main Branch Testing (after 7min deployment wait):**
- All PR tests PLUS
- Remote server essential tests

## Troubleshooting

### Common Issues

**"ROOTLY_API_TOKEN not set"**
```bash
# Check if token is set
env | grep ROOTLY_API_TOKEN

# Set token temporarily
export ROOTLY_API_TOKEN="your_token_here"
```

**"401 Unauthorized" errors**
```bash
# Test token directly
curl -H "Authorization: Bearer $ROOTLY_API_TOKEN" \
     -H "Content-Type: application/vnd.api+json" \
     "https://api.rootly.com/v1/incidents" | head -20
```

**Tests timeout or hang**
```bash
# Run with timeout
uv run pytest --timeout=60

# Check for async issues
uv run pytest -v --tb=short
```

**Import errors**
```bash
# Reinstall dependencies
uv sync --dev

# Check Python path
uv run python -c "import rootly_mcp_server; print('OK')"
```

### Test Debugging

**Verbose output:**
```bash
uv run pytest tests/unit/test_server.py::TestServerCreation::test_create_server_with_defaults -v -s
```

**Debug specific test:**
```bash
uv run pytest tests/unit/test_authentication.py -k "test_local_mode" --pdb
```

**Check fixtures:**
```bash
uv run pytest --fixtures test_specific_file.py
```

## Adding New Tests

### For New Features
1. **Unit tests first** - Test logic in isolation
2. **Integration tests** - Test with real dependencies
3. **Update markers** - Add appropriate `@pytest.mark.*`
4. **Update documentation** - Document new test behavior

### Test Writing Guidelines
- Use descriptive test names
- One assertion per concept tested
- Use appropriate fixtures from `conftest.py`
- Mock external dependencies appropriately
- Add docstrings explaining test purpose

### Example Test Structure
```python
@pytest.mark.unit
class TestNewFeature:
    """Test new feature functionality."""
    
    def test_feature_basic_case(self, mock_dependency):
        """Test basic functionality works."""
        # Given
        setup_conditions()
        
        # When  
        result = new_feature()
        
        # Then
        assert result.is_expected()
```

## Performance

Current test performance targets:
- **Unit tests:** <30 seconds
- **Local integration:** <30 seconds  
- **Remote integration:** <60 seconds (including mocks)
- **Full suite:** <2 minutes locally

Monitor test performance and optimize slow tests.
```

### File: examples\skills\README.md
```md
# Rootly MCP Skills

This directory contains pre-built Claude Code skills that demonstrate how to effectively use the Rootly MCP server for incident management workflows.

## What are Skills?

Skills are specialized AI agents that combine multiple tools and follow specific workflows. They provide Claude Code with domain expertise and structured approaches to complex tasks.

## Available Skills

### 🚨 Rootly Incident Responder

**File:** `rootly-incident-responder.md`

An experienced SRE specialist that handles production incidents from detection to resolution.

**Capabilities:**
- Analyzes incidents with full Rootly context
- Leverages ML-based similarity to find related historical incidents
- Provides AI-powered solution recommendations from past resolutions
- Coordinates with on-call teams (timezone-aware)
- Correlates incidents with code deployments via GitHub
- Creates structured action items and remediation plans
- Tracks confidence levels and resolution time estimates

**Best for:**
- Production incident response
- Post-incident analysis
- On-call handoffs
- Learning from historical incident patterns

## Installation

### Option 1: Project-Specific Installation

Copy the skill to your project's `.claude/skills/` directory:

```bash
mkdir -p .claude/skills
cp rootly-incident-responder.md .claude/skills/
```

The skill will be available for use in that project.

### Option 2: Global Installation

Install the skill globally for use across all projects:

```bash
mkdir -p ~/.claude/skills
cp rootly-incident-responder.md ~/.claude/skills/
```

## Usage

Once installed, you can invoke skills in Claude Code using the `@` symbol:

```
@rootly-incident-responder analyze incident #12345
```

Or let Claude automatically use the skill when appropriate:

```
Can you help me respond to the current production incident?
```

Claude will recognize the context and automatically engage the Rootly Incident Responder skill.

## Prerequisites

These skills require the Rootly MCP server to be configured in your Claude Code settings:

```json
{
  "mcpServers": {
    "rootly": {
      "command": "uvx",
      "args": ["--from", "rootly-mcp-server", "rootly-mcp-server"],
      "env": {
        "ROOTLY_API_TOKEN": "<YOUR_ROOTLY_API_TOKEN>"
      }
    }
  }
}
```

For GitHub integration (code correlation), also add:

```json
{
  "mcpServers": {
    "github": {
      "command": "uvx",
      "args": ["--from", "mcp-server-github", "mcp-server-github"],
      "env": {
        "GITHUB_TOKEN": "<YOUR_GITHUB_TOKEN>"
      }
    }
  }
}
```

## Contributing Skills

Have an idea for a new Rootly skill? We welcome contributions!

**Potential skill ideas:**
- **Post-Incident Reviewer**: Analyzes resolved incidents and generates comprehensive post-mortems
- **On-Call Optimizer**: Analyzes on-call metrics and suggests schedule improvements
- **Incident Pattern Detector**: Identifies recurring incident patterns and suggests preventive measures
- **Severity Calibrator**: Helps teams maintain consistent severity classifications
- **Runbook Generator**: Creates runbooks from resolved incident patterns

To contribute:
1. Create your skill following the format in `rootly-incident-responder.md`
2. Test it thoroughly with real Rootly incidents
3. Submit a pull request with documentation and examples

## Learn More

- [Rootly MCP Server Documentation](../../README.md)
- [Claude Code Skills Guide](https://docs.anthropic.com/claude/docs/skills)
- [Contributing Guidelines](../../CONTRIBUTING.md)

## Support

- **Issues**: [GitHub Issues](https://github.com/Rootly-AI-Labs/Rootly-MCP-server/issues)
- **Discussions**: [GitHub Discussions](https://github.com/Rootly-AI-Labs/Rootly-MCP-server/discussions)
- **Rootly Support**: [docs.rootly.com](https://docs.rootly.com)

```

### File: CHANGELOG.md
```md
# Changelog

All notable changes to the Rootly MCP Server will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [2.2.14] - Released 2026-04-02

### Highlights
- Refreshed FastMCP and related runtime dependencies to address newly disclosed security advisories

### Fixes
- Updated Code Mode imports and test fixtures for FastMCP 3.2.0 compatibility

### Docs / Dependencies
- Added a Dependabot cooldown for package ecosystem updates
- Upgraded `fastmcp[code-mode]` to `3.2.0`
- Upgraded transitive `cryptography` to `46.0.6`
- Upgraded transitive `Pygments` to `2.20.0`

## [2.2.13] - Released 2026-03-26

### Highlights
- Improved hosted auth validation and Code Mode `execute` error handling
- Patched vulnerable `authlib` and `requests` dependencies

### Fixes
- Validate hosted `Authorization` headers earlier and log auth header state to make malformed token issues easier to diagnose
- Hardened Code Mode `execute` by normalizing common client-prefixed tool names and returning clearer parser, import, and runtime errors

### Docs / Dependencies
- Simplified the README quick start and added clearer hosted remote configuration examples for HTTP streamable, SSE, and Code Mode
- Upgraded `fastmcp[code-mode]` to `3.1.1` and refreshed CI dependencies

## [2.2.12] - Released 2026-03-18

### Highlights
- Reduced oversized shift and collection payloads and added pagination to `list_shifts`

### Features
- Added MCP-level pagination to `list_shifts`, including pagination metadata and validation for invalid page numbers

### Fixes
- Trimmed `get_shift_incidents` results to avoid oversized responses
- Preserved incidents that started before a shift but were resolved during it

### Docs / Dependencies
- Slimmed heavy collection payloads for generated tools such as `listUsers`, `listServices`, and `listShifts`
- Clarified Code Mode tool discovery and pagination guidance for paginated calls
- Added and simplified Claude Code setup examples in the documentation

## [2.2.11] - Released 2026-03-16

### Highlights
- Added incident update and readback support for PIR workflows

### Features
- Added `updateIncident` for scoped incident updates in the PIR lifecycle
- Added `getIncident` and incident readback support for PIR verification

### Fixes
- Updated `search_incidents` to include retrospective progress status in readback results
- Made Code Mode `execute` compatible with older Monty runtimes
- Patched vulnerable `black` and `PyJWT` dependencies
- Fixed CI usage of `actions/upload-artifact`

### Docs / Dependencies
- Scoped GitHub Actions workflow permissions more tightly

## [2.2.10] - Released 2026-03-12

### Highlights
- Rolled out hosted dual transport, Code Mode, and richer observability support

### Features
- Added a hosted Code Mode endpoint and enabled Code Mode by default in hosted dual-mode deployments
- Added streamable HTTP and SSE dual-transport support in a single hosted process
- Added screenshot coverage, escalation APIs, and tighter allowlist path matching
- Added structured tool-usage telemetry for Datadog, including transport-aware metrics and hashed identity context
- Added Gemini CLI extension support and editor-specific setup documentation
- Added branch-based staging deployment pipeline support

### Fixes
- Restored legacy server parity while preserving compatibility with FastMCP 3.x `list_tools()` and `send()` behavior
- Forwarded auth tokens correctly in hosted SSE and streamable HTTP paths
- Reduced hosted auth noise, improved graceful shutdown behavior, and preserved error context across multi-call tools
- Fixed non-string incident severity handling in `shift_incidents`

### Docs / Dependencies
- Reorganized Quick Start documentation by editor and added Rootly CLI guidance
- Refreshed vulnerable runtime dependencies and normalized log severity handling

## [2.2.9] - Released 2026-02-24

### Fixes
- Added an auth header event hook for hosted mode so downstream API requests consistently carry the caller's bearer token

## [2.2.8] - Released 2026-02-24

### Features
- Added filter parameters to `listAlerts`
- Added transport and hosting mode to the Rootly `User-Agent`

### Docs / Dependencies
- Hardened the Dockerfile and added `.dockerignore`

## [2.2.6] - Released 2026-02-19

### Highlights
- Added alert lookup by short ID and reduced alert payload size

### Features
- Added `get_alert_by_short_id` so alerts can be fetched by short ID or full alert URL

### Fixes
- Included alert `url` and `created_at` in alert field selection
- Removed the `timeout` parameter from `FastMCP.from_openapi()` for FastMCP 3.0 compatibility

### Docs / Dependencies
- Reduced alert API response payload size significantly and added User-Agent tracking

## [2.2.4] - Released 2026-02-18

### Features
- Added MCP registry metadata

### Fixes
- Enforced JSON:API headers through an `httpx` event hook to resolve hosted `415` errors more reliably

## [2.2.3] - Released 2026-02-05

### Features
- Added debug logging for HTTP requests and headers

## [2.2.2] - Released 2026-02-05

### Fixes
- Removed existing content-type headers case-insensitively before setting JSON:API headers

## [2.2.1] - Released 2026-02-05

### Fixes
- Always set JSON:API headers regardless of request kwargs to prevent hosted `415` failures

## [2.2.0] - Released 2026-02-05

### Highlights
- Renamed On-Call Health terminology from `burnout` to `health risk`

## [2.1.4] - Released 2026-02-05

### Fixes
- Resolved hosted MCP `415 Unsupported Media Type` errors

## [2.1.3] - Released 2026-02-05

### Highlights
- Added the first On-Call Health integration

### Features
- Added the On-Call Health integration for burnout-risk detection
- Added unit tests for the On-Call Health integration

### Fixes
- Added proper type hints to `och_client.py`

### Docs / Dependencies
- Streamlined the README and moved development setup details into `CONTRIBUTING.md`

## [2.1.2] - Released 2026-02-05

### Features
- Added on-call AI workflow tools

## [2.1.1] - 2026-02-04

### Fixed
- Fixed parameter transformation bug where filter parameters (e.g., `filter_status`, `filter_services`) were not being transformed back to their API format (`filter[status]`, `filter[services]`) when making requests to the Rootly API
- Root cause: The inner httpx client was being passed to FastMCP instead of the AuthenticatedHTTPXClient wrapper, bypassing the `_transform_params` method
- Thanks to @smoya for reporting this issue in PR #29

## [2.1.0] - 2026-01-27

### Added

#### Security Improvements
- Comprehensive security module (`security.py`) with:
  - API token validation (prevents invalid/short tokens)
  - HTTPS enforcement for all API calls (rejects HTTP URLs)
  - Input sanitization (SQL injection and XSS prevention)
  - Rate limiting using token bucket algorithm (default: 100 req/min)
  - Error message sanitization (removes stack traces and file paths)
  - Sensitive data masking for logs (tokens, passwords, secrets)
  - URL validation with allowed domain checking

#### Exception Handling
- Custom exception hierarchy (`exceptions.py`) with 11 specific exception types:
  - `RootlyAuthenticationError` - 401 authentication failures
  - `RootlyAuthorizationError` - 403 access denied
  - `RootlyNetworkError` - Network/connection issues
  - `RootlyTimeoutError` - Request timeouts
  - `RootlyValidationError` - Input validation failures
  - `RootlyRateLimitError` - Rate limit exceeded (with retry_after)
  - `RootlyAPIError` - Generic API errors
  - `RootlyServerError` - 5xx server errors
  - `RootlyClientError` - 4xx client errors
  - `RootlyConfigurationError` - Missing/invalid configuration
  - `RootlyResourceNotFoundError` - 404 not found
- Automatic exception categorization with `categorize_exception()`

#### Input Validation
- Input validation utilities (`validators.py`) with:
  - Positive integer validation
  - String validation with length and pattern checks
  - Dictionary validation with required keys
  - Enum value validation
  - Pagination parameter validation

#### Monitoring & Observability
- Structured JSON logging with correlation IDs (`monitoring.py`)
- Request metrics tracking:
  - Request counts by endpoint and status code
  - Response latency percentiles (p50, p95, p99)
  - Error rate tracking by type
  - Active connection monitoring
- Health check support with `get_health_status()`
- Request/response logging decorator (automatically sanitizes sensitive data)
- Context manager for tracking request metrics

#### Helper Utilities
- Pagination helpers (`pagination.py`):
  - Async pagination across multiple pages
  - Pagination parameter building for Rootly API
  - Pagination metadata extraction

#### Testing Infrastructure
- 66 comprehensive unit tests (100% passing)
- Test coverage >90% for all new modules
- Security-focused tests:
  - SQL injection prevention
  - XSS prevention
  - Rate limiting behavior
  - Token validation
  - HTTPS enforcement
  - Error message sanitization

#### CI/CD Pipeline
- GitHub Actions workflow (`.github/workflows/ci.yml`) with:
  - Automated testing on Python 3.10, 3.11, 3.12
  - Code coverage reporting (Codecov integration)
  - Automated linting (ruff, black, isort, mypy)
  - Security scanning (bandit, safety)
  - Automated package building
  - Runs on every push and pull request

### Changed

#### Security Enhancements
- **BREAKING SECURITY FIX**: Removed all API token logging from `__main__.py` (line 100, 116)
  - Changed from: `logger.debug(f"Token starts with: {api_token[:5]}...")`
  - Changed to: `logger.info("ROOTLY_API_TOKEN is configured")`
- **SECURITY**: Updated `client.py` to use structured logging without exposing tokens
- **SECURITY**: All error messages now sanitized to remove stack traces
- Replaced generic `except Exception` with specific exception types in:
  - `__main__.py` - Now catches `RootlyConfigurationError`, `RootlyMCPError`
  - `client.py` - Now catches specific HTTP errors and categorizes them

#### API Client Improvements
- `RootlyClient.make_request()` now raises specific exceptions instead of returning JSON errors
- Added HTTPS enforcement to base URL validation
- Added 30-second timeout to all requests (already existed, now enforced everywhere)
- Better error categorization for HTTP status codes (401, 403, 404, 429, 4xx, 5xx)

#### Configuration Validation
- API token now validated on startup with `validate_api_token()`
- Better error messages for missing or invalid configuration

### Fixed

- Security vulnerability: API tokens no longer logged (even partially)
- Security vulnerability: Stack traces no longer exposed in error responses
- Security vulnerability: HTTP URLs now rejected (HTTPS enforced)
- Generic exception handling replaced with specific exception types
- Error messages now user-friendly (sanitized of internal details)

### Documentation

- Added `IMPLEMENTATION_REPORT.md` - Detailed implementation summary
- Added `GPT4O_REVIEW.md` - External review of improvements
- Added `IMPLEMENTATION_CHECKLIST.md` - Implementation progress tracking
- Updated `IMPROVEMENT_PLAN.md` with GPT-4o recommendations
- All new modules have comprehensive docstrings
- Updated package docstring with new features

### Technical Details

- **Lines of Code Added**: ~1,500 lines production code, ~500 lines test code
- **Test Coverage**: >90% for new modules
- **Tests Passing**: 66/66 (100%)
- **Security Issues Fixed**: 6 critical vulnerabilities
- **Breaking Changes**: 0 (fully backward compatible)

### Backward Compatibility

All changes are backward compatible:
- Existing API unchanged
- New modules are additive
- Exception hierarchy maintains base `Exception` compatibility
- Client behavior unchanged from external perspective
- No migration required for existing users

## [2.0.15] - Previous Release

(Previous changelog entries would go here)

```

### File: CONTRIBUTING.md
```md
# Contributing to Rootly MCP Server

## Submitting Changes

1. Fork the repository and create a feature branch
2. Make your changes with clear, atomic commits
3. Open a Pull Request with a description that clearly explains:
   - What the change does
   - Why it's needed
   - Any breaking changes or migration steps

## Developer Setup

### Prerequisites
- Python 3.12 or higher
- [`uv`](https://github.com/astral-sh/uv) for dependency management

### 1. Set Up Virtual Environment

Create and activate a virtual environment:

```bash
uv venv .venv
source .venv/bin/activate  # Always activate before running scripts
```

### 2. Install Dependencies

Install all project dependencies:

```bash
uv pip install .
```

To add new dependencies during development:
```bash
uv pip install <package>
```

### 3. Set Up Git Hooks (Recommended)

Install pre-commit hooks to automatically run linting and tests before commits:

```bash
./scripts/setup-hooks.sh
```

This ensures code quality by running:
- Ruff linting
- Pyright type checking
- Unit tests

### 4. Verify Installation

The server should now be ready to use with your MCP-compatible editor.

Additional testing tools are available in the `tests/` directory.

```

### File: gemini-extension.json
```json
{
  "name": "rootly",
  "version": "0.1.0",
  "description": "Manage incidents, alerts, services, and on-call schedules with Rootly through Gemini CLI",
  "mcpServers": {
    "rootly": {
      "command": "uvx",
      "args": [
        "--from",
        "rootly-mcp-server",
        "rootly-mcp-server"
      ]
    }
  },
  "settings": [
    {
      "name": "Rootly API Token",
      "description": "Your Rootly API token (generate at Organization Settings > API Keys)",
      "envVar": "ROOTLY_API_TOKEN",
      "sensitive": true
    }
  ]
}

```

### File: server.json
```json
{
  "$schema": "https://static.modelcontextprotocol.io/schemas/2025-12-11/server.schema.json",
  "name": "com.rootly/mcp-server",
  "title": "Rootly",
  "description": "Incident management, on-call scheduling, and intelligent analysis powered by Rootly.",
  "version": "2.2.9",
  "repository": {
    "url": "https://github.com/Rootly-AI-Labs/Rootly-MCP-server",
    "source": "github"
  },
  "remotes": [
    {
      "type": "streamable-http",
      "url": "https://mcp.rootly.com/mcp",
      "headers": [
        {
          "name": "Authorization",
          "description": "Bearer token for Rootly API (format: Bearer <YOUR_ROOTLY_API_TOKEN>)",
          "isRequired": true,
          "isSecret": true
        }
      ]
    },
    {
      "type": "sse",
      "url": "https://mcp.rootly.com/sse",
      "headers": [
        {
          "name": "Authorization",
          "description": "Bearer token for Rootly API (format: Bearer <YOUR_ROOTLY_API_TOKEN>)",
          "isRequired": true,
          "isSecret": true
        }
      ]
    }
  ],
  "packages": [
    {
      "registryType": "pypi",
      "identifier": "rootly-mcp-server",
      "version": "2.2.9",
      "transport": {
        "type": "stdio"
      },
      "environmentVariables": [
        {
          "name": "ROOTLY_API_TOKEN",
          "description": "Your Rootly API token",
          "isRequired": true,
          "isSecret": true
        }
      ]
    }
  ]
}

```

### File: .semaphore\update-task-definition.sh
```sh
#!/bin/bash

set -e

# Updates a task definition with a new container image
# Returns the new task definition ARN
#
# Required environment variables:
# TASK_FAMILY - Task definition family
# CONTAINER_NAME - Container name to update
# IMAGE - New container image to deploy

if [ -z "$TASK_FAMILY" ] || [ -z "$CONTAINER_NAME" ] || [ -z "$IMAGE" ]; then
  echo "Error: TASK_FAMILY, CONTAINER_NAME, and IMAGE environment variables are required"
  exit 1
fi

TASK_DEFINITION="$(aws ecs describe-task-definition --task-definition=$TASK_FAMILY | jq '.taskDefinition')"

# Remove fields that can't be used in register-task-definition
TASK_DEFINITION="$(jq 'del(.taskDefinitionArn, .revision, .status, .requiresAttributes, .compatibilities, .registeredAt, .registeredBy)' <<< "$TASK_DEFINITION")"

# Find the index of the specified container
CONTAINER_INDEX="$(jq --arg NAME "$CONTAINER_NAME" '.containerDefinitions | map(.name) | index($NAME)' <<< "$TASK_DEFINITION")"

if [ "$CONTAINER_INDEX" = "null" ]; then
  echo "Error: Container '$CONTAINER_NAME' not found in task definition"
  exit 1
fi

# Update the container image
NEW_TASK_DEFINITION="$(jq --arg INDEX "$CONTAINER_INDEX" --arg IMAGE "$IMAGE" '.containerDefinitions[$INDEX | tonumber].image = $IMAGE' <<< "$TASK_DEFINITION")"

# Register the new task definition
NEW_TASK_DEFINITION_ARN="$(aws ecs register-task-definition --cli-input-json "$NEW_TASK_DEFINITION" --output text --query 'taskDefinition.taskDefinitionArn')"

echo "$TASK_DEFINITION" > task-definition.json
echo "$NEW_TASK_DEFINITION" > new-task-definition.json

echo "Applying update:" >&2
diff -u task-definition.json new-task-definition.json >&2 || :

echo "$NEW_TASK_DEFINITION_ARN"

```

### File: scripts\setup-hooks.sh
```sh
#!/bin/bash
# Setup git hooks for this repository
# Run this script after cloning: ./scripts/setup-hooks.sh

set -e

REPO_ROOT="$(git rev-parse --show-toplevel)"
HOOKS_DIR="$REPO_ROOT/.git/hooks"

echo "🔧 Setting up git hooks..."

# Create pre-commit hook
cat > "$HOOKS_DIR/pre-commit" << 'EOF'
#!/bin/bash
# Pre-commit hook to run linting and type checking
# This ensures code quality before committing

set -e

echo "🔍 Running pre-commit checks..."
echo ""

# 1. Ruff linting
echo "📝 Checking code style with ruff..."
if ! uv run ruff check .; then
    echo "❌ Ruff linting failed!"
    echo "💡 Try running: uv run ruff check . --fix"
    exit 1
fi
echo "✅ Ruff passed!"
echo ""

# 2. Pyright type checking
echo "🔍 Running type checks with pyright..."
if ! uv run pyright; then
    echo "❌ Type checking failed!"
    echo "💡 Fix type errors or add type: ignore comments"
    exit 1
fi
echo "✅ Pyright passed!"
echo ""

# 3. Run unit tests (quick check)
echo "🧪 Running unit tests..."
if ! uv run pytest tests/unit/ -q --tb=line; then
    echo "❌ Tests failed!"
    echo "💡 Fix failing tests before committing"
    exit 1
fi
echo "✅ Tests passed!"
echo ""

echo "✅ All pre-commit checks passed! Proceeding with commit..."
exit 0
EOF

chmod +x "$HOOKS_DIR/pre-commit"

echo "✅ Git hooks installed successfully!"
echo ""
echo "The following checks will run before every commit:"
echo "  1. Ruff linting"
echo "  2. Pyright type checking"
echo "  3. Unit tests"
echo ""
echo "To skip hooks (not recommended): git commit --no-verify"

```

### File: tests\conftest.py
```py
"""
Shared pytest fixtures and configuration for Rootly MCP Server tests.

This module provides fixtures for:
- Token management (secure API token access)
- Test environment detection
- Common test utilities
- Mock configurations
"""

import os
from typing import Any
from unittest.mock import Mock, patch

import pytest


@pytest.fixture(scope="session")
def api_token() -> str:
    """
    Provide API token for testing.

    Skips tests if token is not available to prevent failures
    in environments without proper token configuration.
    """
    token = os.getenv("ROOTLY_API_TOKEN")
    if not token:
        pytest.skip("ROOTLY_API_TOKEN not set - skipping API tests")
    return token  # pytest.skip() never returns, so this is always a string


@pytest.fixture(scope="session")
def test_environment() -> dict[str, Any]:
    """
    Provide information about the current test environment.

    Returns:
        Dict with environment details:
        - has_token: Whether API token is available
        - is_ci: Whether running in CI environment
        - github_ref: Git reference (for CI)
    """
    return {
        "has_token": bool(os.getenv("ROOTLY_API_TOKEN")),
        "is_ci": os.getenv("CI") == "true",
        "github_ref": os.getenv("GITHUB_REF", ""),
        "github_actor": os.getenv("GITHUB_ACTOR", ""),
    }


@pytest.fixture
def mock_api_response():
    """
    Provide a mock API response for testing without real API calls.

    Returns a function that creates mock responses with common structure.
    """

    def create_response(
        data: list | None = None, meta: dict | None = None, status_code: int = 200
    ) -> dict[str, Any]:
        if data is None:
            data = []
        if meta is None:
            meta = {"total": len(data), "page": 1}

        return {"data": data, "meta": meta, "status_code": status_code}

    return create_response


@pytest.fixture
def mock_incident_data():
    """
    Provide sample incident data for testing.

    Returns realistic incident data structure matching Rootly API format.
    """
    return [
        {
            "id": "1",
            "type": "incidents",
            "attributes": {
                "title": "Database connection timeout",
                "summary": "Users experiencing slow response times",
                "status": "investigating",
                "severity": "high",
                "created_at": "2025-08-21T10:00:00Z",
            },
        },
        {
            "id": "2",
            "type": "incidents",
            "attributes": {
                "title": "API rate limiting activated",
                "summary": "High traffic causing rate limits",
                "status": "resolved",
                "severity": "medium",
                "created_at": "2025-08-21T09:30:00Z",
            },
        },
    ]


@pytest.fixture
def mock_server_config():
    """
    Provide mock server configuration for testing.

    Returns configuration that doesn't require external dependencies.
    """
    return {
        "name": "TestServer",
        "hosted": False,
        "swagger_path": None,
        "api_base": "https://api.rootly.com/v1",
    }


@pytest.fixture
def mock_httpx_client():
    """
    Provide a mock httpx client for testing HTTP interactions.
    """
    with patch("httpx.AsyncClient") as mock_client:
        mock_instance = Mock()
        mock_client.return_value = mock_instance

        # Configure default responses
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"data": [], "meta": {"total": 0}}
        mock_instance.get.return_value = mock_response
        mock_instance.post.return_value = mock_response

        yield mock_instance


@pytest.fixture
def mock_environment_token():
    """
    Temporarily set environment token for testing.

    Use this fixture when you need to test token loading behavior.
    """
    test_token = "rootly_test_token_123456789"
    with patch.dict(os.environ, {"ROOTLY_API_TOKEN": test_token}):
        yield test_token


@pytest.fixture
def skip_if_no_token():
    """
    Skip test if no API token is available.

    Use as a fixture in tests that absolutely require an API token.
    """
    if not os.getenv("ROOTLY_API_TOKEN"):
        pytest.skip("API token required for this test")

```

### File: tests\test_client.py
```py
#!/usr/bin/env python3
"""
Functional test client for Rootly MCP Server

Tests the actual functionality including:
- search_incidents with new max_results limits
- Authentication in both hosted and local modes
- Custom tools execution
"""

import asyncio
import os
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from rootly_mcp_server.server import create_rootly_mcp_server


async def test_search_incidents_limits():
    """Test the new search_incidents max_results limits."""
    print("\n🔍 Testing search_incidents limits...")

    server = create_rootly_mcp_server(name="TestServer")

    # Get the search_incidents tool
    tools_list = await server.list_tools()
    search_tool = next((t for t in tools_list if t.name == "search_incidents"), None)

    if not search_tool:
        print("❌ search_incidents tool not found")
        return

    print("✅ Found search_incidents tool")

    # Check the parameter schema for max_results
    if hasattr(search_tool, "fn"):
        # Get function signature info
        import inspect

        sig = inspect.signature(search_tool.fn)  # type: ignore
        max_results_param = sig.parameters.get("max_results")

        if max_results_param and hasattr(max_results_param.annotation, "__metadata__"):
            # Extract the Field constraints
            field_info = max_results_param.annotation.__metadata__[0]
            print(f"  Max allowed: {field_info.le if hasattr(field_info, 'le') else 'Unknown'}")
            print(f"  Default value: {max_results_param.default}")

    # Test actual execution with different limits
    try:
        print("\n  Testing with empty query (should get recent incidents)...")
        result = await search_tool.fn(query="", max_results=5)  # type: ignore
        result_count = len(result.get("data", []))
        print(f"  ✅ Empty query test - got {result_count} results")

        if result_count == 0:
            print("    ℹ️  No incidents found - this may be normal for a test/empty environment")
        else:
            # Show first incident title if available
            first_incident = result.get("data", [{}])[0]
            title = first_incident.get("attributes", {}).get("title", "No title")
            print(f"    📋 First incident: {title[:50]}...")

        print("\n  Testing with max limit (10)...")
        result = await search_tool.fn(query="", max_results=10)  # type: ignore
        result_count = len(result.get("data", []))
        print(f"  ✅ Max limit test - got {result_count} results")

        # Also test pagination
        print("\n  Testing pagination (page_number=1)...")
        result = await search_tool.fn(query="", page_number=1, page_size=3)  # type: ignore
        result_count = len(result.get("data", []))
        print(f"  ✅ Pagination test - got {result_count} results (max 3 per page)")

        print("\n  Testing invalid limit (15 - should be rejected)...")
        try:
            # Try to use the tool through the MCP framework validation
            if hasattr(search_tool, "validate_call"):
                result = await search_tool.validate_call(query="test", max_results=15)  # type: ignore
            else:
                # Fallback to direct call - validation might not trigger here
                result = await search_tool.fn(query="test", max_results=15)  # type: ignore
                print("  ⚠️  Function accepted max_results=15 (validation may be bypassed)")
                print(f"      Result count: {len(result.get('data', []))}")
                return
        except Exception as e:
            print(f"  ✅ Correctly rejected max_results=15: {type(e).__name__}: {e}")

    except Exception as e:
        print(f"  ❌ API call failed: {e}")
        if "401" in str(e) or "authentication" in str(e).lower():
            print("    (This is expected if API token is invalid/expired)")


async def test_authentication_modes():
    """Test authentication in different modes."""
    print("\n🔐 Testing authentication modes...")

    # Test local mode (default)
    print("\n  Testing local mode (hosted=False)...")
    try:
        server_local = create_rootly_mcp_server(name="LocalTest", hosted=False)
        print("  ✅ Local mode server created successfully")

        # Check if API token was loaded
        tools_list = await server_local.list_tools()
        search_tool = next((t for t in tools_list if t.name == "search_incidents"), None)
        if search_tool:
            print("  ✅ search_incidents tool available in local mode")

    except Exception as e:
        print(f"  ❌ Local mode failed: {e}")

    # Test hosted mode
    print("\n  Testing hosted mode (hosted=True)...")
    try:
        server_hosted = create_rootly_mcp_server(name="HostedTest", hosted=True)
        print("  ✅ Hosted mode server created successfully")

        tools_list = await server_hosted.list_tools()
        search_tool = next((t for t in tools_list if t.name == "search_incidents"), None)
        if search_tool:
            print("  ✅ search_incidents tool available in hosted mode")

    except Exception as e:
        print(f"  ❌ Hosted mode failed: {e}")


async def test_tool_availability():
    """Test that all expected tools are available."""
    print("\n🛠️  Testing tool availability...")

    server = create_rootly_mcp_server(name="ToolTest")
    tools_list = await server.list_tools()

    expected_custom_tools = ["search_incidents", "list_endpoints"]
    tool_names = [t.name for t in tools_list]

    print(f"  Total tools found: {len(tools_list)}")

    # Check custom tools
    for tool_name in expected_custom_tools:
        if tool_name in tool_names:
            print(f"  ✅ Custom tool '{tool_name}' found")
        else:
            print(f"  ❌ Custom tool '{tool_name}' missing")

    # List all available OpenAPI tools to see actual naming
    openapi_tools = [name for name in tool_names if name not in expected_custom_tools]
    print(f"  📋 Available OpenAPI tools ({len(openapi_tools)}):")
    for tool_name in sorted(openapi_tools)[:10]:  # Show first 10
        print(f"    • {tool_name}")
    if len(openapi_tools) > 10:
        print(f"    ... and {len(openapi_tools) - 10} more")

    # Check for incident-related tools specifically
    incident_tools = [name for name in tool_names if "incident" in name.lower()]
    if incident_tools:
        print(f"  🔍 Incident-related tools: {', '.join(incident_tools)}")


async def main():
    """Run all tests."""
    print("Rootly MCP Server Functional Tests")
    print("=" * 50)

    # Check environment
    token = os.getenv("ROOTLY_API_TOKEN")
    if token:
        print(f"✅ API token found: {token[:10]}...")
    else:
        print("⚠️  No ROOTLY_API_TOKEN found - API calls may fail")

    try:
        await test_tool_availability()
        await test_authentication_modes()
        await test_search_incidents_limits()

        print("\n" + "=" * 50)
        print("🎉 All tests completed!")

    except Exception as e:
        print(f"\n❌ Test suite failed: {e}")
        import traceback

        traceback.print_exc()


if __name__ == "__main__":
    asyncio.run(main())

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.

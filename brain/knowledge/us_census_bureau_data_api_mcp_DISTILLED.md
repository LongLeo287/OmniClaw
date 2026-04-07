---
id: us-census-bureau-data-api-mcp
type: knowledge
owner: OA_Triage
---
# us-census-bureau-data-api-mcp
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
# U.S. Census Bureau Data API MCP
[![License: CC0-1.0](https://img.shields.io/badge/License-CC0%201.0-lightgrey.svg)](https://github.com/uscensusbureau/us-census-bureau-data-api-mcp/blob/main/LICENSE)
[![MCP Project Build](https://github.com/uscensusbureau/us-census-bureau-data-api-mcp/actions/workflows/build.yml/badge.svg)](https://github.com/uscensusbureau/us-census-bureau-data-api-mcp/actions/workflows/build.yml)
[![MCP Project - Lint](https://github.com/uscensusbureau/us-census-bureau-data-api-mcp/actions/workflows/lint.yml/badge.svg)](https://github.com/uscensusbureau/us-census-bureau-data-api-mcp/actions/workflows/lint.yml)
[![MCP Server - Tests](https://github.com/uscensusbureau/us-census-bureau-data-api-mcp/actions/workflows/test.yml/badge.svg)](https://github.com/uscensusbureau/us-census-bureau-data-api-mcp/actions/workflows/test.yml)
[![MCP Database - Tests](https://github.com/uscensusbureau/us-census-bureau-data-api-mcp/actions/workflows/test-db.yml/badge.svg)](https://github.com/uscensusbureau/us-census-bureau-data-api-mcp/actions/workflows/test-db.yml)
![MCP Server - Test Coverage](https://raw.githubusercontent.com/gist/luke-keller-census/0589e2c69696f077eef7d6af818a108b/raw/badge.svg)
![MCP Database - Test Coverage](https://raw.githubusercontent.com/gist/luke-keller-census/ae50d82d94893c2e674f7f742aea958e/raw/badge.svg)

Bringing _official_ Census Bureau statistics to AI assistants everywhere.

The *U.S. Census Bureau Data API MCP* is a [Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction) server that connects AI assistants with data from the Census Data API and other official Census Bureau sources. This project is built using the [MCP Typescript SDK](https://github.com/modelcontextprotocol/typescript-sdk).

## Contents
* [Getting Started](#getting-started)
* [Using the MCP Server](#using-the-mcp-server)
* [How the MCP Server Works](#how-the-mcp-server-works)
* [Development](#development)
* [MCP Server Architecture](#mcp-server-architecture)
* [Available Methods](#available-methods)
* [Available Tools](#available-tools)
* [Available Prompts](#available-prompts)
* [Helper Scripts](#helper-scripts)
* [Additional Information](#additional-information)

## Getting Started
To get started, you will need:

* A valid Census Bureau [Data API key](https://api.census.gov/data/key_signup.html)
* Docker (i.e. Docker Desktop)
* Node 18+

## Using the MCP Server
To use the U.S. Census Bureau Data API MCP server:
1. Clone or download the project locally.
2. In a terminal window, navigate to the project’s root directory and run `docker compose --profile prod run --rm census-mcp-db-init sh -c "npm run migrate:up && npm run seed"` to pull data from the Census Data API into the local database. *This is only required on first-time setup.*
3. Configure your AI Assistant to use the MCP Server (see below).
4. Start your AI Assistant.

Here is an example configuration file that includes the appropriate scripts for launching the MCP Server:

```
{
  "mcpServers": {
    "mcp-census-api": {
      "command": "bash",
      "args": [
        "/Path/To/Server/us-census-bureau-data-api-mcp/scripts/mcp-connect.sh"
      ],
      "env": {
        "CENSUS_API_KEY": "YOUR_CENSUS_API_KEY"
      }
    }
  }
}
```

Note that the `CENSUS_API_KEY` variable is required. This defines the `env` variable in the MCP Client and passes it to the MCP server via the `mcp-connect` script.

Be sure to update the path to the `us-census-bureau-data-api-mcp` directory in `args` and provide a valid `CENSUS_API_KEY`.

### Updating the MCP Server
When a new version of this project is released, you will need to rebuild the production environment for the latest features. From the `mcp-db/` directory, run the following:

```
npm run prod:down
npm run prod:build
```

After that, you can relaunch your MCP Client and it should connect to the server again.

## How the MCP Server Works

The U.S. Census Bureau Data API MCP server uses data from the Census Data API and other official sources to construct contextually rich data and statistics for use with AI Assistants. The Census Data API is the primary source of data but some of the API's data is pulled down to a local postgres container to enable more robust and performant search functionality. Below is an illustration of how user prompts are processed by AI Assistants and the MCP Server.

![Illustration of how the MCP Server works, starting with a user prompt, processing by an AI Assistant, tool or resource calls to the U.S. Census Bureau Data API MCP server, and finally queries to the local postgres database or the Census Data API.](/us-census-burea-mcp-server-flow.jpg)

## Development

Run `docker compose --profile dev up` from the root of the project to build the containers. This starts the MCP Database containers that runs migrations and seeds a local `postgres` database to supplement information from the Census Bureau API. It also starts the MCP Server itself.

By default, all logging functions are disabled in the `mcp-server` to prevent `json` validation errors when interacting with the MCP server through MCP clients. To enable logging for development purposes, set `DEBUG_LOGS=true` when interacting with the server directly using the examples below, e.g. `echo '{CALL_ARGUMENTS}' docker exec -e DEBUG_LOGS=true -i -e CENSUS_API_KEY=YOUR_CENSUS_API_KEY mcp-server node dist/index.js`. 

### Testing

This project uses [Vitest](https://vitest.dev/) to test the MCP Server and MCP Database.

#### MCP Server Testing

Prior to running the MCP Server tests, a valid Census Bureau [API key](https://api.census.gov/data/key_signup.html) is required. This key should be defined in the `.env` file of the `mcp-server` directory. The `sample.env` offers an example of how this `.env` file should look.

To run tests, navigate to the `mcp-server/` directory and run `npm run test`. To run ESLint, run `npm run lint` from the same directory.

#### MCP Database Testing

A `.env` file needs to be created in the `mcp-db/` directory with a valid `DATABASE_URL` variable defined. The `sample.env` in the same directory includes the default value.

To run tests, navigate to the `mcp-db/` directory and run `npm run test`.

## MCP Server Architecture

* `mcp-server/src/` - Source code for the MCP Server.
* `mcp-server/src/index.ts` - Starts the MCP Server and registers tools.
* `mcp-server/src/server.ts` - Defines the `McpServer` class that handles calls to the server, e.g. how `tools/list` and `tools/calls` respond to requests
* `mcp-server/src/tools/` - Includes tool definitions and shared classes, e.g. `BaseTool` and `ToolRegistry`, to reduce repetition and exposes the tools list to the server
* `mcp-server/src/schema/` - Houses each tool’s schema and is used to validate schemas in tests

## Available Methods

The MCP server exposes several methods: `tools/list`, `tools/call`, `prompts/list`, and `prompts/get`.

## Available Tools
This section covers tools that can be called.

### List Datasets
The `list-datasets` tool is used for fetching a subset of metadata for all datasets that are available in the Census Bureau's API. \
It requires no arguments.

### Fetch Dataset Geography
The `fetch-dataset-geography` tool is used for fetching available geography levels for filtering a given dataset. It accepts the following arguments:
* Dataset (Required) - The identifier of the dataset, e.g. `'acs/acs1'`
* Year (Optional) - The vintage of the dataset, e.g. `1987`

### Fetch Aggregate Data
The `fetch-aggregate-data` tool is used for fetching  aggregate data from the Census Bureau's API. It accepts the following arguments:
* Dataset (Required) - The identifier of the dataset, e.g. `'acs/acs1'`
* Year (Required) - The vintage of the dataset, e.g. `1987`
* Get (Required) - An object that is required that accepts 2 optional arguments:
	* Variables (optional) - An array of variables for filtering responses by attributes and rows, e.g. `'NAME'`, `'B01001_001E'`
	* Group (Optional) - A string that returns a larger collection of variables, e.g. `S0101`
* For (Optional) - A string that restricts geography to various levels and is required in most datasets
* In (Optional) - A string that restricts geography to smaller areas than state level
* UCGID (Optional) - A string that restricts geography by Uniform Census Geography Identifier (UCGID), e.g. `0400000US41`
* Predicates (Optional) - Filter options for the dataset, e.g. `'for': 'state*'`
* Descriptive (Optional) - Adds variable labels to API response (default: `false`), e.g. `true`

### Resolve Geography FIPS Tool
The `resolve-geography-fips` tool is used to search across all Census Bureau geographies to return a list of potential matches and the correct FIPS codes and parameters used to query data in them. This tool accepts the following arguments:
* Geography Name (Required) - The name of the geography to search, e.g. `Philadelphia`
* Summary Level (Optional) - The summary level to search. Accepts name or summary level code, e.g. `Place`, `160`

## Available Prompts
This section covers prompts that can be called. According to the [Model Context Protocol docs](https://modelcontextprotocol.io/docs/learn/server-concepts#:~:text=Pre%2Dbuilt%20instruction%20templates%20that%20tell%20the%20model%20to%20work%20with%20specific%20tools%20and%20resources.), prompts are "pre-built instruction templates that tell the model to work with specific tools and resources". This means that prompts override the default model behavior. Prompts are **not** a menu of allowed questions. They are instructions, not constraints on server capability.

### Population
This `get_population_data` prompt retrieves population statistics for US states, counties, cities, and other geographic areas. It resolves geographic names to their corresponding FIPS codes before fetching data. This prompt accepts the following argument:
- `geography_name` (required): Name of the geographic area (state, county, city, etc.)

## Helper Scripts

For easier command-line usage, this project includes bash helper scripts in the `scripts/dev` directory that wrap the complex Docker commands and handle the `CENSUS_API_KEY` parameter automatically.

## Additional Information
For more information about the parameters above and all available predicates, review the Census Bureau's [API documentation](https://www.census.gov/data/developers/guidance/api-user-guide.Core_Concepts.html#list-tab-559651575).


```

### File: scripts\dev\README.md
```md
# Development Helper Scripts

**Note: These scripts are for development and testing purposes only.** They are not the intended primary interface for interacting with the MCP server. For production use, connect your AI assistant client to the MCP server as described in the main [README.md](../../README.md).

The Model Context Protocol (MCP) is designed for client-server interactions through MCP clients (like Claude Desktop, IDEs with MCP support, etc.). These bash helper scripts are provided to facilitate development, debugging, and testing workflows.

## Contents
* [Available Scripts](#available-scripts)
* [Helper Scripts Usage](#helper-scripts-usage)
  * [Main Helper Script](#main-helper-script)
  * [Individual Helper Scripts](#individual-helper-scripts)
  * [Script Features](#script-features)
* [CLI Examples](#cli-examples)
* [Listing Tools](#listing-tools)
* [Listing Prompts](#listing-prompts)
* [Available Tools](#available-tools)
  * [List Datasets](#list-datasets)
  * [Fetch Dataset Geography](#fetch-dataset-geography)
  * [Fetch Aggregate Data](#fetch-aggregate-data)
  * [Resolve Geography FIPS Tool](#resolve-geography-fips-tool)
* [Available Prompts](#available-prompts)
  * [Population](#population)

## Available Scripts

* `census-mcp.sh` - Unified interface to all Census MCP tools
* `list-tools.sh` - List available MCP tools
* `list-prompts.sh` - List available MCP prompts
* `list-datasets.sh` - List available Census datasets
* `fetch-dataset-geography.sh` - Fetch geography levels for a dataset
* `fetch-aggregate-data.sh` - Fetch aggregate Census data
* `resolve-geography-fips.sh` - Resolve geography names to FIPS codes
* `get-population-data.sh` - Get population data prompt for a geography


## Helper Scripts Usage

All helper scripts require the `CENSUS_API_KEY` environment variable to be set:

```bash
export CENSUS_API_KEY='your_api_key_here'
```

### Main Helper Script

The `census-mcp.sh` script provides a unified interface to all Census MCP tools:

```bash
# Usage
./census-mcp.sh <command> [arguments...] [--json]

# Available commands:
#   list-tools              List available MCP tools
#   list-prompts            List available MCP prompts
#   list-datasets           List available Census datasets
#   fetch-dataset-geography <dataset> [year]
#                           Fetch geography levels for a dataset
#   fetch-aggregate-data    <dataset> <year> <variables> [for] [in] [ucgid] [predicates] [--descriptive]
#                           Fetch aggregate Census data
#   resolve-geography-fips  <geography_name> [summary_level]
#                           Resolve geography name to FIPS codes
#   get-population-data     <geography_name>
#                           Get population data prompt
```

### Script Features

All helper scripts:
- Automatically handle the `CENSUS_API_KEY` environment variable
- Start Docker services if needed
- Provide usage help with `-h` or `--help`
- Include input validation and error handling
- Support `--json` flag for clean JSON output suitable for piping to tools like `jq`

## CLI Examples

The following sections show both raw CLI commands (for understanding the underlying MCP protocol) and helper script examples for each tool and prompt.

## Listing Tools

To list available tools, use the `tools/list` method with no arguments. `tools/list` is a standard method that is often called by LLMs when the client is initialized.

#### How to Run via CLI (Raw)
```
echo '{"jsonrpc":"2.0","id":1,"method":"tools/list"}' | docker exec -i \
mcp-server node dist/index.js
```

#### How to Run via Helper Script
```bash
export CENSUS_API_KEY='your_api_key'

# List all available tools
./scripts/dev/list-tools.sh

# Using unified wrapper  
./scripts/dev/census-mcp.sh list-tools

# JSON output for processing (count tools)
./scripts/dev/list-tools.sh --json | jq '.result.tools | length'

# Extract tool names
./scripts/dev/list-tools.sh --json | jq '.result.tools[].name'
```

## Listing Prompts
To list available prompts, use the `prompts/list` method with no arguments. 

#### How to Run via CLI (Raw)
```
echo '{"jsonrpc":"2.0","id":1,"method":"prompts/list"}' | docker exec -i \
mcp-server node dist/index.js
```

#### How to Run via Helper Script
```bash
export CENSUS_API_KEY='your_api_key'

# List all available prompts
./scripts/dev/list-prompts.sh

# Using unified wrapper
./scripts/dev/census-mcp.sh list-prompts

# JSON output for processing (extract prompt name)
./scripts/dev/list-prompts.sh --json | jq '.result.prompts[0].name'
```

## Available Tools
This section covers tools that can be called.

### List Datasets
For detailed information about the `list-datasets` tool, see the [Available Tools](../../README.md#available-tools) section in the main README.

#### How to Run via CLI (Raw)
```
echo '{"jsonrpc":"2.0","id":1,"method":"tools/call", "params":{"name":"list-datasets","arguments":{}}}' \
| docker exec -i -e CENSUS_API_KEY=YOUR_CENSUS_API_KEY mcp-server node dist/index.js
```

#### How to Run via Helper Script
```bash
export CENSUS_API_KEY='your_api_key'

# List all available datasets
./scripts/dev/list-datasets.sh

# Using unified wrapper
./scripts/dev/census-mcp.sh list-datasets

# JSON output for processing (count datasets)
./scripts/dev/list-datasets.sh --json | jq '.result.content[0].text | fromjson | length'

# Extract specific dataset info
./scripts/dev/list-datasets.sh --json | jq '.result.content[0].text | fromjson | .[] | select(.dataset=="acs/acs5")'
```

### Fetch Dataset Geography
For detailed information about the `fetch-dataset-geography` tool, see the [Available Tools](../../README.md#available-tools) section in the main README.

#### How to Run via CLI (Raw)
```
echo '{"jsonrpc":"2.0","id":1,"method":"tools/call", "params":{"name":"fetch-dataset-geography", "arguments":{"dataset":"cbp","year":2022}}}' \
| docker exec -i -e CENSUS_API_KEY=YOUR_CENSUS_API_KEY mcp-server node dist/index.js
```

#### How to Run via Helper Script
```bash
export CENSUS_API_KEY='your_api_key'

# Get geography levels for CBP data
./scripts/dev/fetch-dataset-geography.sh cbp 2022

# Using unified wrapper
./scripts/dev/census-mcp.sh fetch-dataset-geography cbp 2022

# Using unified wrapper with JSON output
./scripts/dev/census-mcp.sh fetch-dataset-geography cbp 2022 --json | jq -r '.result.content[0].text' | tail -n +3 | jq 'length'

# JSON output for processing (count geography levels)
./scripts/dev/fetch-dataset-geography.sh cbp 2022 --json | jq -r '.result.content[0].text' | tail -n +3 | jq 'length'

# Extract specific geography query example
./scripts/dev/fetch-dataset-geography.sh cbp 2022 --json | jq -r '.result.content[0].text' | tail -n +3 | jq '.[] | select(.name == "state") | .queryExample'
```

### Fetch Aggregate Data
For detailed information about the `fetch-aggregate-data` tool, see the [Available Tools](../../README.md#available-tools) section in the main README.

#### How to Run via CLI (Raw)
```
echo '{"jsonrpc":"2.0","id":1,"method":"tools/call", "params":{"name":"fetch-aggregate-data", "arguments":{"dataset":"acs/acs1","year":2022, "get": { "variables":["NAME","B01001_001E"] }, "for":"state:01,13"}}}' \
| docker exec -i -e CENSUS_API_KEY=YOUR_CENSUS_API_KEY mcp-server node dist/index.js
```

#### How to Run via Helper Script
```bash
export CENSUS_API_KEY='your_api_key'

# Using variables (comma-separated) - requires geography for ACS
./scripts/dev/fetch-aggregate-data.sh acs/acs1 2022 'NAME,B01001_001E' 'state:01'
./scripts/dev/fetch-aggregate-data.sh acs/acs1 2022 'NAME,B01001_001E' 'state:01,13'

# Using a group (single identifier) - example with CBP dataset  
./scripts/dev/fetch-aggregate-data.sh cbp 2022 'NAME,EMP' 'state:01'
./scripts/dev/fetch-aggregate-data.sh cbp 2022 'NAME,EMP' 'state:*'

# With descriptive labels enabled
./scripts/dev/fetch-aggregate-data.sh acs/acs1 2022 'NAME,B01001_001E' 'state:01' --descriptive

# With predicates
./scripts/dev/fetch-aggregate-data.sh acs/acs1 2022 'NAME,B01001_001E' --predicates 'NAICS2017:31-33'

# Using unified wrapper
./scripts/dev/census-mcp.sh fetch-aggregate-data acs/acs1 2022 'NAME,B01001_001E' 'state:01'

# JSON output for processing
./scripts/dev/fetch-aggregate-data.sh acs/acs1 2022 'NAME,B01001_001E' 'state:01' --json | jq '.result.content[0].text'
```

### Resolve Geography FIPS Tool
For detailed information about the `resolve-geography-fips` tool, see the [Available Tools](../../README.md#available-tools) section in the main README.

#### How to Run via CLI (Raw)
```
echo '{"jsonrpc":"2.0","id":1,"method":"tools/call","params":{"name":"resolve-geography-fips", "arguments":{"geography_name":"Philadelphia, Pennsylvania"}}}' \
| docker exec -i -e CENSUS_API_KEY=YOUR_CENSUS_API_KEY mcp-server node dist/index.js
```

#### How to Run via Helper Script
```bash
export CENSUS_API_KEY='your_api_key'

# Basic geography search
./scripts/dev/resolve-geography-fips.sh 'Philadelphia, Pennsylvania'

# With summary level filter
./scripts/dev/resolve-geography-fips.sh 'Philadelphia' 'Place'
./scripts/dev/resolve-geography-fips.sh 'Cook County' '050'

# Using unified wrapper
./scripts/dev/census-mcp.sh resolve-geography-fips 'Philadelphia, Pennsylvania'

# JSON output for processing  
./scripts/dev/resolve-geography-fips.sh 'Cook County' '050' --json | jq -r '.result.content[0].text' | tail -n +3 | jq '.[0].for_param'
```

## Available Prompts
This section covers prompts that can be called. Please note that prompts do not return data. Prompts produce instructions that cause the model to generate or request data.

### Population

For detailed information about the `get_population_data` prompt, see the [Available Prompts](../../README.md#available-prompts) section in the main README.

#### How to Run via CLI (Raw)
```
echo '{"jsonrpc":"2.0","id":1,"method":"prompts/get", "params":{"name":"get_population_data","arguments":{"geography_name":"San Francisco, CA"}}}' \
| docker exec -i -e CENSUS_API_KEY=YOUR_CENSUS_API_KEY mcp-server node dist/index.js
```

#### How to Run via Helper Script
```bash
export CENSUS_API_KEY='your_api_key'

# Basic usage
./scripts/dev/get-population-data.sh 'San Francisco, CA'
./scripts/dev/get-population-data.sh 'California'

# Using unified wrapper
./scripts/dev/census-mcp.sh get-population-data 'San Francisco, CA'

# JSON output for processing
./scripts/dev/get-population-data.sh 'Cook County, Illinois' --json | jq '.result.description'
```
```

### File: CONTRIBUTING.md
```md
# Contributing

Before you consider contributing, please: 

- Read this contributing guide  
- Check the [README](https://github.com/uscensusbureau/mcp-server-census-api/blob/main/README.md) for project overview and setup instructions 
- Review existing [issues](https://github.com/uscensusbureau/mcp-server-census-api/issues) and [pull requests](https://github.com/uscensusbureau/mcp-server-census-api/pulls)
- For major changes, open an issue first to discuss the approach

## Criteria for Contributions and Feedback
This is a moderated platform. The U.S. Census Bureau will only accept contributions that are contributed per the terms of the license file. Contributors may submit links or materials for hosting in the repository. Upon submission, materials will be public and considered publicly available information, unless noted in the license file.

The U.S. Census Bureau reserves the right to reject, remove, or edit any contribution or feedback, including anything that:
* states or implies endorsement of any entities, services, or products;
* is inaccurate;
* contains abusive or vulgar content, spam, hate speech, personal attacks, or similar content;
* is clearly "off topic";
* makes unsupported accusations;
* includes personally identifiable or business identifiable information according to Department of Commerce Office of Privacy and Open Government guidelines; or,
* contains .exe or .jar file types.

## How to Contribute 

There are two ways to contribute: 1) reporting issues or feature requests and 2) contributing code.  

### Issue Reports and Feature Requests 

When reporting issues and feature requests, please use our Github issue templates. 

### Code Contributions 

All new code contributions must include appropriate tests and require code review. The code review process is simple: open a Pull Request on GitHub and ensure all CI checks pass. One of the code owners will review your contribution. 

### Generative AI
We neither encourage nor prohibit AI code generation tools when contributing to this codebase. Please indicate in the Pull Request (PR) whether you used generative AI to create any part of the code. Generated code requires extra diligence. The time saved in generation is often offset by verification and review effort. Don't shift the burden of catching errors and understanding implementation details to maintainers; do this work before submitting.

## Public domain
This project is in the public domain within the United States, and copyright and related rights in the work worldwide are waived through the [CC0 1.0 Universal public domain dedication](https://github.com/uscensusbureau/us-census-bureau-data-api-mcp/?tab=CC0-1.0-1-ov-file/).

All contributions to this project will be released under the CC0 dedication. By submitting a pull request, you are agreeing to comply with this waiver of copyright interest.

```

### File: .github\copilot-instructions.md
```md
<Goals>
- Provide expert-level review of the repository's structure, technology stack, and critical patterns, with a focus on Model Context Protocol (MCP) best practices
- Highlight any non-obvious dependencies or architectural decisions that may impact code changes
- Ensure best practices are followed in terms of code organization, validation, and error handling
- Ensure architectural consistency across the codebase, especially in how MCP tools are implemented and how Census API interactions are handled
</Goals>

<HighLevelDetails>
This repository is a Model Context Protocol (MCP) server that provides AI-ready U.S. Census Bureau data.

**Technology Stack:**
- Language: TypeScript (Node.js runtime)
- API: U.S. Census Bureau API
- Database: PostgreSQL (for caching dataset metadata)
- Validation: Zod schemas
- Testing: Vitest
- Build: TypeScript compiler (tsc)
- Package Manager: npm
- Containerization: Docker & Docker Compose

**Repository Size:** Medium-sized TypeScript project with:
- MCP server application (mcp-server/)
- Database ETL service (mcp-db/)
- Multi-profile Docker Compose setup (dev/test/prod)
- Comprehensive test suite with unit and integration tests

**Project Purpose:** To enable use of official Census Bureau statistics with AI assistants, leveraging the Model Context Protocol to provide token-optimized data that reduces hallucinations.
</HighLevelDetails>

<BuildInstructions>
**Prerequisites:**
- Docker and Docker Compose installed
- Node.js 18+ (for local development outside Docker)

**Local Development Setup:**

The project uses Docker Compose with multiple profiles (dev, test, prod).

**Start Development Environment:**
```bash
docker compose --profile dev up
```
This starts:
- PostgreSQL database on port 5433
- Runs migrations automatically
- Leaves the dev container running for interactive commands

**Run Tests in Development:**
```bash
docker compose --profile dev exec census-mcp-db-dev-init npm run test
```

**Run Linter in Development:**
```bash
docker compose --profile dev exec census-mcp-db-dev-init npm run lint
```

**Run Tests (Standalone):**
```bash
docker compose --profile test up census-mcp-db-test-init
```
Starts test database and runs the test suite, then exits.

**Production Deployment:**
```bash
docker compose --profile prod up
```
Starts production services with MCP server on standard PostgreSQL port 5432.

**Validation:**
All validation (build, lint, tests) is handled by CI/GitHub Actions on pull requests.

**Important Notes:**
- The project is containerized - all services run in Docker
- Development uses port 5433, test uses 5434, prod uses 5432
- Database migrations run automatically on container startup
- The MCP server runs as a containerized service, not standalone
- Focus on writing correct code - let CI handle validation
- If modifying database schema, migrations will auto-run on next startup
</BuildInstructions>

<ProjectLayout>
**Directory Structure:**
```
/
├── mcp-db/                       # Database ETL service (CRITICAL - runs first)
│   ├── src/
│   │   ├── seeds                 # Orchestrates seeding process
│   │   │   ├── configs           # Configs for seeding different data types
│   │   │   ├── scripts           # Generic seeding utilities
│   │   │   │   ├── seed-runner   # Orchestrates seeding process
│   │   │   │   └── seed-database # Executes ETL pipeline
│   ├── migrations/               # Database schema migrations
│   ├── tests/                    # Test suite (mirrors src/)
│   ├── Dockerfile
│   ├── package.json
│   ├── tsconfig.json
│   ├── vitest.config.ts
│   └── eslint.config.js
├── mcp-server/                  # Main MCP server application
│   ├── src/
│   │   ├── tools/               # MCP tool implementations
│   │   │   ├── base.tool.ts
│   │   │   ├── fetch-aggregate-data.tool.ts
│   │   │   ├── fetch-dataset-geography.tool.ts
│   │   │   ├── list-datasets.tool.ts
│   │   │   └── resolve-geography-fips.tool.ts
│   │   ├── types/               # TypeScript definitions
│   │   ├── schema/              # Zod validation schemas
│   │   ├── prompts/             # MCP prompts
│   │   ├── services/            # Database service
│   │   ├── index.js             # Entry point
│   │   └── server.js
│   ├── tests/                   # Test suite (mirrors src/)
│   ├── Dockerfile
│   ├── package.json
│   ├── tsconfig.json
│   ├── vitest.config.ts
│   └── eslint.config.js
├── docker-compose.yml           # Multi-profile orchestration
```

**Configuration Files:**
- `mcp-server/tsconfig.json` - TypeScript strict mode, local development
- `mcp-server/tsconfig.docker.json` - TypeScript config for Docker builds
- `mcp-server/vitest.config.ts` - Test configuration with coverage
- `mcp-server/eslint.config.js` - Linting rules
- `mcp-server/.prettierrc` - Code formatting rules
- `mcp-db/Dockerfile` - Multi-stage build (dev/prod targets) for ETL service
- `mcp-db/tsconfig.json` - TypeScript config for database ETL
- `mcp-db/package.json` - Dependencies for migration and seeding
- `docker-compose.yml` - Multi-profile service orchestration (dev/test/prod)

**Key Architectural Elements:**

1. **MCP Database Service** (`mcp-db/`)
   - **CRITICAL:** Extracts, transforms, and loads (ETL) all Census metadata into PostgreSQL
   - Runs migrations and seeds database on container startup
   - Provides metadata used by all tools EXCEPT `fetch-aggregate-data` tool
   - Tools like `list-datasets`, `resolve-geography-fips`, and `fetch-dataset-geography` query this database
   - Must complete successfully before MCP server can start
   - Multi-stage Dockerfile (dev/prod targets)

2. **MCP Tools** (`mcp-server/src/tools/`)
   - `base.tool.ts` - Abstract base class for all tools
   - Each tool file implements one MCP tool following Model Context Protocol
   - Tools use Zod schemas for validation
   - **Data sources:**
     - `fetch-aggregate-data.tool.ts` - Queries Census API directly
     - All other tools - Query PostgreSQL database populated by mcp-db service

3. **Schemas** (`mcp-server/src/schema/`)
   - Zod validation schemas for all Census API responses
   - `validators.js` - Shared validation utilities
   - Each tool has a corresponding schema file

4. **Prompts** (`mcp-server/src/prompts/`)
   - MCP prompt implementations
   - `base.prompt.js` - Base prompt functionality
   - Example: `population.prompt.js` for population-related queries

5. **Services** (`mcp-server/src/services/`)
   - `database.service.js` - PostgreSQL connection and query handling
   - Used by most tools to retrieve metadata from database

6. **Testing Structure** (`mcp-server/tests/`)
   - Unit tests: `*.test.ts`
   - Integration tests: `*.integration.test.ts`
   - Test helpers in `tests/helpers/`
   - Mocks in `tests/mocks/`

**CI/CD Checks:**
- GitHub Actions workflows (not visible in tree, assumed present)
- Local validation via Docker Compose test profile
- All PRs must pass: build + lint + test suite

**Critical Patterns:**
- **Tool Naming:** All tools extend `base.tool.ts`
- **Schema Validation:** Every tool has a corresponding `.schema.js` file
- **Test Organization:** Tests mirror `src/` structure with unit + integration
- **FIPS Geography Codes:** Handled in `resolve-geography-fips.tool.ts`
- **Database Service:** Centralized in `database.service.js`

**Dependencies Not Obvious from Structure:**
- **mcp-db service MUST run successfully before mcp-server starts** - it populates the metadata database
- Most tools (`list-datasets`, `resolve-geography-fips`, `fetch-dataset-geography`) depend on database populated by mcp-db
- Only `fetch-aggregate-data` queries Census API directly - all other tools query PostgreSQL
- All tools depend on `base.tool.ts`
- Tools use schemas from `schema/` directory for validation
- Database connection managed by `database.service.js`
- Test utilities centralized in `tests/helpers/`

**Important Files:**
- `mcp-server/src/index.js` - MCP server entry point
- `mcp-server/src/server.js` - Server initialization and configuration
- `mcp-server/sample.env` - Required environment variables template
- `mcp-db/src/seeds/configs/*` - Config files for seeding different data types (datasets, geographies, variables)
- `mcp-db/src/seeds/scripts/seed-runner` - Orchestrates database seeding process
- `mcp-db/src/seeds/scripts/seed-database` - Executes ETL pipeline to populate metadata
- `docker-compose.yml` - Service orchestration with dev/test/prod profiles

**Trust These Instructions:**
The information above reflects the actual repository structure. Only search for additional information if these instructions are incomplete or incorrect for your specific task.
</ProjectLayout>
```

### File: scripts\mcp-connect.sh
```sh
#!/bin/bash

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

PROJECT_DIR="$(dirname "$SCRIPT_DIR")"

cd "$PROJECT_DIR" || exit

# Start production services (won't restart if already running)
docker compose --profile prod up -d >/dev/null 2>&1

# Wait a moment for services to be ready
sleep 3

# Check if the existing container can be used
if docker exec mcp-server test -f /app/dist/index.js 2>/dev/null; then
    # Container exists and is ready, use it
    exec docker exec -i -e CENSUS_API_KEY="$CENSUS_API_KEY" mcp-server node dist/index.js
else
    # Fall back to run command
    exec docker compose --profile prod run --rm -T -e CENSUS_API_KEY="$CENSUS_API_KEY" mcp-server node dist/index.js
fi

```

### File: .github\ISSUE_TEMPLATE\bug_report.md
```md
---
name: Bug report
about: Create a report to help us improve
title: ''
labels: ''
assignees: ''

---

**Describe the bug**
A clear and concise description of what the bug is.

**To Reproduce**
Steps to reproduce the behavior:
1. Go to '...'
2. Click on '....'
3. Scroll down to '....'
4. See error

**Expected behavior**
A clear and concise description of what you expected to happen.

**Conversation:**
Please provide details about the conversation that led to this response. Examples include:
- User Input [e.g. "What’s the population of Maryland?"]
- Model Response [include any tools invoked, source data cited, and text responses]
- MCP Tools Invoked [e.g. 'fetch-summary-table']

**Model Details**
 - The Name of the Model [e.g. Claude]
 - The Version of the Model [e.g. Claude Sonnet 4.0]
 - Where the Conversation Occured [e.g. Claude Desktop]

**Screenshots**
If applicable, add screenshots to help explain your problem.

**Additional context**
Add any other context about the problem here.

```

### File: .github\ISSUE_TEMPLATE\feature_request.md
```md
---
name: Feature request
about: Suggest an idea for this project
title: ''
labels: ''
assignees: ''

---

**Is your feature request related to a problem? Please describe.**
A clear and concise description of what the problem is. Ex. I'm always frustrated when [...]

**Describe the solution you'd like**
A clear and concise description of what you want to happen.

**Describe alternatives you've considered**
A clear and concise description of any alternative solutions or features you've considered.

**Additional context**
Add any other context or screenshots about the feature request here.

```

### File: .github\PULL_REQUEST_TEMPLATE\pull_request_template.md
```md
# Pull Request

## Description

Please provide a brief description of the changes introduced by this pull request.

## Changes Made

- List the changes made in bullet points.

## Related Issue

- Link to the related issue (if applicable).

## Generative AI
- Was generative AI used to create any part of the code submitted in this PR? [Yes/No]

## Additional Notes

Provide any additional information or context that might be helpful for reviewers.

## Screenshots (if applicable)

Include screenshots or GIFs that demonstrate the changes, if relevant.

## Checklist

- [ ] I have read the CONTRIBUTING.md document.
- [ ] My code follows the project's coding standards.
- [ ] I have added tests that prove my fix is effective or that my feature works.
- [ ] All new and existing tests passed.
- [ ] I have updated the documentation accordingly.
- [ ] The title of my pull request is a short description of the changes.
- [ ] My pull request is assigned to the appropriate milestone.


```

### File: scripts\dev\census-mcp.sh
```sh
#!/bin/bash

# Census MCP Helper - Main wrapper script for all Census MCP tools
# This script provides a unified interface to all Census MCP tools and commands

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Function to show usage
show_usage() {
    echo "Census MCP Helper - Unified interface for Census Bureau Data API MCP tools"
    echo ""
    echo "Usage: $0 <command> [arguments...] [--json]"
    echo ""
    echo "Available commands:"
    echo "  list-tools              List available MCP tools"
    echo "  list-prompts            List available MCP prompts" 
    echo "  list-datasets           List available Census datasets"
    echo "  fetch-dataset-geography <dataset> [year]"
    echo "                          Fetch geography levels for a dataset"
    echo "  fetch-aggregate-data <dataset> <year> <variables> [for] [in] [ucgid] [predicates] [--descriptive]"
    echo "                          Fetch aggregate Census data"
    echo "  resolve-geography-fips <geography> [summary_level]"
    echo "                          Resolve geography name to FIPS codes"
    echo "  get-population-data <geography>"
    echo "                          Get population data prompt"
    echo ""
    echo "Global Options:"
    echo "  --json                  Output only JSON (suitable for piping to jq)"
    echo "  -h, --help              Show this help message"
    echo ""
    echo "Environment Setup:"
    echo "  Set CENSUS_API_KEY environment variable before running:"
    echo "    export CENSUS_API_KEY='your_api_key_here'"
    echo "    $0 <command> [arguments...]"
    echo ""
    echo "  Or provide it inline:"
    echo "    CENSUS_API_KEY='your_api_key' $0 <command> [arguments...]"
    echo ""
    echo "Examples:"
    echo "  $0 list-tools"
    echo "  $0 list-datasets --json | jq '.result'"
    echo "  $0 fetch-dataset-geography acs/acs1 2022"
    echo "  $0 fetch-aggregate-data acs/acs1 2022 'NAME,B01001_001E' 'state:01,13' --descriptive"
    echo "  $0 resolve-geography-fips 'Philadelphia, Pennsylvania'"
    echo "  $0 get-population-data 'San Francisco, CA'"
}

# Check if CENSUS_API_KEY is provided
if [ -z "$CENSUS_API_KEY" ]; then
    echo "Error: CENSUS_API_KEY environment variable is required" >&2
    echo "" >&2
    show_usage >&2
    exit 1
fi

# Parse arguments to extract --json flag and command
JSON_FLAG=""
COMMAND=""
COMMAND_ARGS=()

while [[ $# -gt 0 ]]; do
    case $1 in
        --json)
            JSON_FLAG="--json"
            shift
            ;;
        -h|--help|help)
            show_usage
            exit 0
            ;;
        *)
            if [ -z "$COMMAND" ]; then
                COMMAND="$1"
            else
                COMMAND_ARGS+=("$1")
            fi
            shift
            ;;
    esac
done

# Check for command argument
if [ -z "$COMMAND" ]; then
    echo "Error: Command argument is required" >&2
    echo "" >&2
    show_usage >&2
    exit 1
fi

# Route to appropriate script
case "$COMMAND" in
    "list-tools")
        exec "$SCRIPT_DIR/list-tools.sh" "${COMMAND_ARGS[@]}" $JSON_FLAG
        ;;
    "list-prompts")
        exec "$SCRIPT_DIR/list-prompts.sh" "${COMMAND_ARGS[@]}" $JSON_FLAG
        ;;
    "list-datasets")
        exec "$SCRIPT_DIR/list-datasets.sh" "${COMMAND_ARGS[@]}" $JSON_FLAG
        ;;
    "fetch-dataset-geography")
        exec "$SCRIPT_DIR/fetch-dataset-geography.sh" "${COMMAND_ARGS[@]}" $JSON_FLAG
        ;;
    "fetch-aggregate-data")
        exec "$SCRIPT_DIR/fetch-aggregate-data.sh" "${COMMAND_ARGS[@]}" $JSON_FLAG
        ;;
    "resolve-geography-fips")
        exec "$SCRIPT_DIR/resolve-geography-fips.sh" "${COMMAND_ARGS[@]}" $JSON_FLAG
        ;;
    "get-population-data")
        exec "$SCRIPT_DIR/get-population-data.sh" "${COMMAND_ARGS[@]}" $JSON_FLAG
        ;;
    *)
        echo "Error: Unknown command '$COMMAND'" >&2
        echo "" >&2
        show_usage >&2
        exit 1
        ;;
esac
```

### File: scripts\dev\fetch-aggregate-data.sh
```sh
#!/bin/bash

# Fetch Aggregate Data Helper Script
# This script wraps the fetch-aggregate-data tool with a simplified interface

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"

# Parse arguments
JSON_ONLY=false
DESCRIPTIVE=false
PREDICATES_ARGS=()
POSITIONAL_ARGS=()

while [[ $# -gt 0 ]]; do
    case $1 in
        --json)
            JSON_ONLY=true
            shift
            ;;
        -h|--help)
            echo "Usage: $0 <dataset> <year> <variables|group> [for] [in] [ucgid] [predicates] [--descriptive] [--json]"
            echo ""
            echo "Arguments:"
            echo "  dataset     (Required) Dataset identifier, e.g., 'acs/acs1'"
            echo "  year        (Required) Dataset vintage, e.g., 2022"
            echo "  get         (Required) Data to retrieve - specify either:"
            echo "    variables (Optional) Comma-separated variables, e.g., 'NAME,B01001_001E'"
            echo "    group     (Optional) Variable group identifier, e.g., 'S0101'"
            echo "  for         (Optional) Geography restriction, e.g., 'state:01,13'"
            echo "  in          (Optional) Constrains the 'for' geography to a parent geography"
            echo "  ucgid       (Optional) Uniform Census Geography Identifier"
            echo "  predicates  (Optional) Additional dataset specific filters (format: key:value,key2:value2)"
            echo ""
            echo "Options:"
            echo "  --descriptive           Add variable labels to results"
            echo "  --json                  Output only JSON (suitable for piping to jq)"
            echo "  -h, --help              Show this help message"
            echo ""
            echo "Examples:"
            echo "  # Using variables (comma-separated)"
            echo "  CENSUS_API_KEY=your_key $0 acs/acs1 2022 'NAME,B01001_001E'"
            echo "  CENSUS_API_KEY=your_key $0 acs/acs1 2022 'NAME,B01001_001E' 'state:01,13'"
            echo "  CENSUS_API_KEY=your_key $0 acs/acs1 2022 'NAME,B01001_001E' --descriptive"
            echo ""
            echo "  # Using a group (single identifier)"
            echo "  CENSUS_API_KEY=your_key $0 acs/acs1 2022 'S0101'"
            echo "  CENSUS_API_KEY=your_key $0 acs/acs1 2022 'S0101' 'state:*'"
            echo ""
            echo "  # JSON output (pipe to jq)"
            echo "  CENSUS_API_KEY=your_key $0 acs/acs1 2022 'NAME,B01001_001E' --json | jq '.result'"
            echo ""
            echo "Environment:"
            echo "  CENSUS_API_KEY must be set"
            exit 0
            ;;
        --descriptive)
            DESCRIPTIVE=true
            shift
            ;;
        -*)
            echo "Unknown option: $1" >&2
            exit 1
            ;;
        *)
            POSITIONAL_ARGS+=("$1")
            shift
            ;;
    esac
done

# Restore positional parameters
set -- "${POSITIONAL_ARGS[@]}"

# Check if CENSUS_API_KEY is provided
if [ -z "$CENSUS_API_KEY" ]; then
    echo "Error: CENSUS_API_KEY environment variable is required" >&2
    echo "Usage: CENSUS_API_KEY=your_key $0 <dataset> <year> <variables|group> [for] [in] [ucgid] [predicates] [--descriptive] [--json]" >&2
    exit 1
fi

# Check for required arguments
if [ $# -lt 3 ]; then
    echo "Error: Dataset, year, and variables/group arguments are required" >&2
    echo "Usage: $0 <dataset> <year> <variables|group> [for] [in] [ucgid] [predicates] [--descriptive] [--json]" >&2
    exit 1
fi

DATASET="$1"
YEAR="$2"
GET_PARAM="$3"
FOR_PARAM="$4"
IN_PARAM="$5"
UCGID_PARAM="$6"
PREDICATES_PARAM="$7"

# Parse predicates if provided (format: key:value,key2:value2)
if [ -n "$PREDICATES_PARAM" ]; then
    IFS=',' read -ra PREDICATES_ARGS <<< "$PREDICATES_PARAM"
fi

# Determine if GET_PARAM is variables (comma-separated) or group (single value)
# If it contains a comma, treat it as variables; otherwise, treat as group
if [[ "$GET_PARAM" == *","* ]]; then
    # Convert comma-separated variables to JSON array
    IFS=',' read -ra VAR_ARRAY <<< "$GET_PARAM"
    VARS_JSON="["
    for i in "${!VAR_ARRAY[@]}"; do
        if [ "$i" -gt 0 ]; then
            VARS_JSON+=","
        fi
        VARS_JSON+="\"${VAR_ARRAY[i]}\""
    done
    VARS_JSON+="]"
    GET_JSON="\"variables\":$VARS_JSON"
    GET_TYPE="variables"
    GET_DISPLAY="$GET_PARAM"
else
    # Treat as group
    GET_JSON="\"group\":\"$GET_PARAM\""
    GET_TYPE="group"
    GET_DISPLAY="$GET_PARAM"
fi

# Build arguments JSON
ARGS_JSON="{\"dataset\":\"$DATASET\",\"year\":$YEAR,\"get\":{$GET_JSON}"

# Add optional parameters
if [ -n "$FOR_PARAM" ]; then
    ARGS_JSON+=",\"for\":\"$FOR_PARAM\""
fi

if [ -n "$IN_PARAM" ]; then
    ARGS_JSON+=",\"in\":\"$IN_PARAM\""
fi

if [ -n "$UCGID_PARAM" ]; then
    ARGS_JSON+=",\"ucgid\":\"$UCGID_PARAM\""
fi

if [ "$DESCRIPTIVE" = true ]; then
    ARGS_JSON+=",\"descriptive\":true"
fi

# Add predicates if provided
if [ ${#PREDICATES_ARGS[@]} -gt 0 ]; then
    PREDICATES_JSON="{"
    for i in "${!PREDICATES_ARGS[@]}"; do
        if [ $i -gt 0 ]; then
            PREDICATES_JSON+=","
        fi
        # Split key:value pair
        KEY="${PREDICATES_ARGS[i]%%:*}"
        VALUE="${PREDICATES_ARGS[i]#*:}"
        PREDICATES_JSON+="\"$KEY\":\"$VALUE\""
    done
    PREDICATES_JSON+="}"
    ARGS_JSON+=",\"predicates\":$PREDICATES_JSON"
fi

ARGS_JSON+="}"

# Build complete JSON payload
JSON_PAYLOAD="{\"jsonrpc\":\"2.0\",\"id\":1,\"method\":\"tools/call\",\"params\":{\"name\":\"fetch-aggregate-data\",\"arguments\":$ARGS_JSON}}"

# Change to project directory
cd "$PROJECT_DIR" || exit

# Ensure services are running
docker compose --profile prod up -d >/dev/null 2>&1
sleep 3

if [ "$JSON_ONLY" = false ]; then
    echo "Fetching aggregate data for dataset: $DATASET (year: $YEAR)"
    if [ "$GET_TYPE" = "variables" ]; then
        echo "Variables: $GET_DISPLAY"
    else
        echo "Group: $GET_DISPLAY"
    fi
    [ -n "$FOR_PARAM" ] && echo "For: $FOR_PARAM"
    [ -n "$IN_PARAM" ] && echo "In: $IN_PARAM"
    [ -n "$UCGID_PARAM" ] && echo "UCGID: $UCGID_PARAM"
    [ "$DESCRIPTIVE" = true ] && echo "Descriptive labels: enabled"
    [ ${#PREDICATES_ARGS[@]} -gt 0 ] && echo "Predicates: ${PREDICATES_ARGS[*]}"
    echo ""
fi

echo "$JSON_PAYLOAD" | \
docker exec -i -e CENSUS_API_KEY="$CENSUS_API_KEY" mcp-server node dist/index.js
```

### File: scripts\dev\fetch-dataset-geography.sh
```sh
#!/bin/bash

# Fetch Dataset Geography Helper Script
# This script wraps the fetch-dataset-geography tool

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"

# Parse arguments
JSON_ONLY=false
POSITIONAL_ARGS=()

while [[ $# -gt 0 ]]; do
    case $1 in
        --json)
            JSON_ONLY=true
            shift
            ;;
        -h|--help)
            echo "Usage: $0 <dataset> [year] [--json]"
            echo ""
            echo "Arguments:"
            echo "  dataset   (Required) Dataset identifier, e.g., 'cbp'"
            echo "  year      (Optional) Dataset vintage, e.g., 2022"
            echo ""
            echo "Options:"
            echo "  --json    Output only JSON (suitable for piping to jq)"
            echo "  -h, --help Show this help message"
            echo ""
            echo "Examples:"
            echo "  CENSUS_API_KEY=your_key $0 cbp"
            echo "  CENSUS_API_KEY=your_key $0 cbp 2022"
            echo "  CENSUS_API_KEY=your_key $0 cbp 2022 --json | jq '.result'"
            echo ""
            echo "Environment:"
            echo "  CENSUS_API_KEY must be set"
            exit 0
            ;;
        -*)
            echo "Unknown option: $1" >&2
            exit 1
            ;;
        *)
            POSITIONAL_ARGS+=("$1")
            shift
            ;;
    esac
done

# Restore positional parameters
set -- "${POSITIONAL_ARGS[@]}"

# Check if CENSUS_API_KEY is provided
if [ -z "$CENSUS_API_KEY" ]; then
    echo "Error: CENSUS_API_KEY environment variable is required" >&2
    echo "Usage: CENSUS_API_KEY=your_key $0 <dataset> [year] [--json]" >&2
    exit 1
fi

# Check for required arguments
if [ $# -lt 1 ]; then
    echo "Error: Dataset argument is required" >&2
    echo "Usage: $0 <dataset> [year] [--json]" >&2
    exit 1
fi

DATASET="$1"
YEAR="$2"

# Build JSON payload
if [ -n "$YEAR" ]; then
    JSON_PAYLOAD="{\"jsonrpc\":\"2.0\",\"id\":1,\"method\":\"tools/call\",\"params\":{\"name\":\"fetch-dataset-geography\",\"arguments\":{\"dataset\":\"$DATASET\",\"year\":$YEAR}}}"
else
    JSON_PAYLOAD="{\"jsonrpc\":\"2.0\",\"id\":1,\"method\":\"tools/call\",\"params\":{\"name\":\"fetch-dataset-geography\",\"arguments\":{\"dataset\":\"$DATASET\"}}}"
fi

# Change to project directory
cd "$PROJECT_DIR" || exit

# Ensure services are running
docker compose --profile prod up -d >/dev/null 2>&1
sleep 3

if [ "$JSON_ONLY" = false ]; then
    echo "Fetching geography levels for dataset: $DATASET$([ -n "$YEAR" ] && echo " (year: $YEAR)")"
fi

echo "$JSON_PAYLOAD" | \
docker exec -i -e CENSUS_API_KEY="$CENSUS_API_KEY" mcp-server node dist/index.js
```

### File: scripts\dev\get-population-data.sh
```sh
#!/bin/bash

# Get Population Data Helper Script
# This script wraps the get_population_data prompt to format a prompt for retrieving population statistics

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"

# Parse arguments
JSON_ONLY=false
POSITIONAL_ARGS=()

while [[ $# -gt 0 ]]; do
    case $1 in
        --json)
            JSON_ONLY=true
            shift
            ;;
        -h|--help)
            echo "Usage: $0 <geography_name> [--json]"
            echo ""
            echo "Arguments:"
            echo "  geography_name   (Required) Name of the geographic area (state, county, city, etc.)"
            echo ""
            echo "Options:"
            echo "  --json          Output only JSON (suitable for piping to jq)"
            echo "  -h, --help      Show this help message"
            echo ""
            echo "Examples:"
            echo "  CENSUS_API_KEY=your_key $0 'San Francisco, CA'"
            echo "  CENSUS_API_KEY=your_key $0 'California'"
            echo "  CENSUS_API_KEY=your_key $0 'Cook County, Illinois' --json | jq '.result'"
            echo ""
            echo "Environment:"
            echo "  CENSUS_API_KEY must be set"
            exit 0
            ;;
        -*)
            echo "Unknown option: $1" >&2
            exit 1
            ;;
        *)
            POSITIONAL_ARGS+=("$1")
            shift
            ;;
    esac
done

# Restore positional parameters
set -- "${POSITIONAL_ARGS[@]}"

# Check if CENSUS_API_KEY is provided
if [ -z "$CENSUS_API_KEY" ]; then
    echo "Error: CENSUS_API_KEY environment variable is required" >&2
    echo "Usage: CENSUS_API_KEY=your_key $0 <geography_name> [--json]" >&2
    exit 1
fi

# Check for required arguments
if [ $# -lt 1 ]; then
    echo "Error: Geography name argument is required" >&2
    echo "Usage: $0 <geography_name> [--json]" >&2
    exit 1
fi

GEOGRAPHY_NAME="$1"

# Build JSON payload
JSON_PAYLOAD="{\"jsonrpc\":\"2.0\",\"id\":1,\"method\":\"prompts/get\",\"params\":{\"name\":\"get_population_data\",\"arguments\":{\"geography_name\":\"$GEOGRAPHY_NAME\"}}}"

# Change to project directory
cd "$PROJECT_DIR" || exit

# Ensure services are running
docker compose --profile prod up -d >/dev/null 2>&1
sleep 3

if [ "$JSON_ONLY" = false ]; then
    echo "Getting population data for: $GEOGRAPHY_NAME"
    echo ""
fi

echo "$JSON_PAYLOAD" | \
docker exec -i -e CENSUS_API_KEY="$CENSUS_API_KEY" mcp-server node dist/index.js
```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.

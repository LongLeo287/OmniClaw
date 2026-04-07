---
id: ORPHAN
type: knowledge
owner: OA_Triage
---
# ORPHAN
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: index.js
```js
import { AppRegistry } from 'react-native';
import App from './src/App';
import { name as appName } from './app.json';

AppRegistry.registerComponent(appName, () => App);

```

### File: main.py
```py
def main():
    print("Hello from xda!")


if __name__ == "__main__":
    main()

```

### File: package.json
```json
{
  "name": "@kilocode/upstream-merge",
  "version": "7.1.20",
  "private": true,
  "type": "module",
  "description": "Scripts for automating upstream opencode merges into Kilo",
  "scripts": {
    "merge": "bun run merge.ts",
    "merge:dry-run": "bun run merge.ts --dry-run",
    "merge:report": "bun run merge.ts --report-only",
    "transform:names": "bun run transforms/package-names.ts",
    "transform:imports": "bun run codemods/transform-imports.ts",
    "transform:strings": "bun run codemods/transform-strings.ts",
    "transform:all": "bun run transforms/package-names.ts && bun run codemods/transform-imports.ts && bun run codemods/transform-strings.ts",
    "versions": "bun run transforms/preserve-versions.ts",
    "keep-ours": "bun run transforms/keep-ours.ts"
  },
  "dependencies": {
    "ts-morph": "^24.0.0"
  },
  "devDependencies": {
    "@types/bun": "catalog:"
  }
}

```

### File: README.md
```md
# Zone.js

[![CDNJS](https://img.shields.io/cdnjs/v/zone.js.svg)](https://cdnjs.com/libraries/zone.js)

Implements _Zones_ for JavaScript, inspired by [Dart](https://dart.dev/articles/archive/zones).

> If you're using zone.js via unpkg (i.e. using `https://unpkg.com/zone.js`)
> and you're using any of the following libraries, make sure you import them first

> - 'newrelic' as it patches global.Promise before zone.js does
> - 'async-listener' as it patches global.setTimeout, global.setInterval before zone.js does
> - 'continuation-local-storage' as it uses async-listener

## Development Status of Zone.js

As Angular moves towards a zoneless application development model, Zone.js is no longer accepting new features, including additional patches for native platform APIs. The team will also not be accepting any low priority bug fixes. Any critical bug fixes that relate to Angular's direct use of Zone.js will still be accepted.

While still a supported part of Angular, the Angular team strongly discourages using Zone.js outside of Angular application contexts.

## NEW Zone.js POST-v0.6.0

See the new API [here](./lib/zone.ts).

Read up on [Zone Primer](https://docs.google.com/document/d/1F5Ug0jcrm031vhSMJEOgp1l-Is-Vf0UCNDY-LsQtAIY).

## BREAKING CHANGES since Zone.js v0.11.1

Prior to `v0.11.1`, Zone.js provided two distribution bundle formats in the `dist` folder.
They were (1) `ES5` bundle distributed as `zone.js` and (2) `ES2015` bundle distributed as `zone-evergreen.js`.
Both of these bundles were in `UMD` format, and are used for Angular's differential-loading mechanism.

Starting with `v0.11.1`, Zone.js follows the [Angular Package Format](https://docs.google.com/document/d/1CZC2rcpxffTDfRDs6p1cfbmKNLA6x5O-NtkJglDaBVs). Therefor the new Zone.js file layout is:

- `bundles`: `ES5` bundle in `UMD` format.
- `fesm2015`: `ES5` bundle in `ESM` format.
- `dist`: `ES5` bundle in `UMD` format. This directory is present to keep backward compatibility.

If you are using `Angular CLI`, the `polyfills.ts` file will contain:

```
import 'zone.js/dist/zone';
```

Starting with Zone.js `v0.11.1+` the import changes to:

```
import 'zone.js';
```

Prior to `v0.11.1` the import would load the `ES5` bundle in `UMD` format from `dist/zone.js`.
Starting with `v0.11.1` the import loads the `ES2015` bundle in `ESM` format instead.

This is a breaking change for legacy browsers such as `IE11`.

For backwards compatibility `zone.js` continues to distribute the same bundles under `dist`.
To restore the old behavior import from the `dist` directory instead like so:

```
import 'zone.js/dist/zone';
```

For details, please refer the [changelog](./CHANGELOG.md) and the [PR](https://github.com/angular/angular/pull/36540).

## What's a Zone?

A Zone is an execution context that persists across async tasks.
You can think of it as [thread-local storage](https://en.wikipedia.org/wiki/Thread-local_storage) for JavaScript VMs.

See this video from ng-conf 2014 for a detailed explanation:

[![screenshot of the zone.js presentation and ng-conf 2014](./presentation.png)](//www.youtube.com/watch?v=3IqtmUscE_U&t=150)

## See also

- [async-listener](https://github.com/othiym23/async-listener) - a similar library for node
- [Async stack traces in Chrome](https://www.html5rocks.com/en/tutorials/developertools/async-call-stack/)
- [strongloop/zone](https://github.com/strongloop/zone) (Deprecated)
- [vizone](https://github.com/gilbox/vizone) - control flow visualizer that uses zone.js

## Standard API support

zone.js patched most standard web APIs (such as DOM events, `XMLHttpRequest`, ...) and nodejs APIs
(`EventEmitter`, `fs`, ...), for more details, please see [STANDARD-APIS.md](STANDARD-APIS.md).

## Nonstandard API support

We are adding support to some nonstandard APIs, such as MediaQuery and
Notification. Please see [NON-STANDARD-APIS.md](NON-STANDARD-APIS.md) for more details.

## Examples

You can find some samples to describe how to use zone.js in [SAMPLE.md](SAMPLE.md).

## Modules

zone.js patches the async APIs described above, but those patches will have some overhead.
Starting from zone.js v0.8.9, you can choose which web API module you want to patch.
For more details, please
see [MODULE.md](MODULE.md).

## Bundles

Starting with `v0.11.0`, `zone.js` uses `Angular Package Format` for bundle distribution.
(For backwards compatibility, all bundles can still be accessed from `dist` folder.)

| Bundle            | Summary                                                                                                                                                                                                                                                                                           |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `zone.js`         | The default bundle. Contains the most used APIs such as `setTimeout/Promise/EventTarget...`, it also supports differential loading by importing this bundle using `import zone.js`. In legacy browsers it includes some additional patches such as `registerElement` and `EventTarget` like APIs. |
| `zone-testing.js` | The bundle for zone testing support of `jasmine` / `mocha` / `jest`. Also includes test utility functions `async` / `fakeAsync` / `sync`.                                                                                                                                                         |
| `zone-node.js`    | The NodeJS support bundle.                                                                                                                                                                                                                                                                        |
| `zone-mix.js`     | A mixed bundle which supports both browser and NodeJS. Useful for mixed environment such as Electron.                                                                                                                                                                                             |
| `zone-externs.js` | the API definitions for `closure compiler`.                                                                                                                                                                                                                                                       |

Additional optional patches not included in the `zone.js` bundles which extend functionality.
The additional bundles can be found under `zone.js/plugins` folder.
To use these bundles, add the following code after importing zone.js bundle.

```
import 'zone.js';
// For example, import canvas patch
import 'zone.js/plugins/zone-patch-canvas';
```

| Patch                            | Summary                                                                                                                                              |
| -------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| `webapis-media-query.js`         | patch for `MediaQuery APIs`                                                                                                                          |
| `webapis-notification.js`        | patch for `Notification APIs`                                                                                                                        |
| `webapis-rtc-peer-connection.js` | patch for `RTCPeerConnection APIs`                                                                                                                   |
| `webapis-shadydom.js`            | patch for `Shady DOM APIs`                                                                                                                           |
| `zone-bluebird.js`               | patch for `Bluebird APIs`                                                                                                                            |
| `zone-error.js`                  | patch for `Error Global Object`, supports adding zone information to stack frame, and also removing unrelated stack frames from `zone.js` internally |
| `zone-patch-canvas.js`           | patch for `Canvas API`                                                                                                                               |
| `zone-patch-cordova.js`          | patch for `Cordova API`                                                                                                                              |
| `zone-patch-electron.js`         | patch for `Electron API`                                                                                                                             |
| `zone-patch-fetch.js`            | patch for `Fetch API`                                                                                                                                |
| `zone-patch-jsonp.js`            | helper utility for `jsonp API`                                                                                                                       |
| `zone-patch-resize-observer.js`  | patch for `ResizeObserver API`                                                                                                                       |
| `zone-patch-rxjs.js`             | patch for `rxjs API`                                                                                                                                 |
| `zone-patch-rxjs-fake-async.js`  | patch for `rxjs fakeasync test`                                                                                                                      |
| `zone-patch-socket-io.js`        | patch for `socket-io`                                                                                                                                |
| `zone-patch-user-media.js`       | patch for `UserMedia API`                                                                                                                            |
| `zone-patch-message-port.js`     | patch for `MessagePort API`                                                                                                                          |

## License

MIT

```

### File: requirements.txt
```txt
pandas>=2.0.0
pyarrow>=10.0.0
fastmcp>=0.1.0
langchain-mcp-adapters>=0.1.0
langchain-openai>=0.1.0
python-dotenv>=1.0.0
langchain>=0.1.0
boxlite[sync]>=0.6.0
e2b-code-interpreter>=1.0.0

```

### File: .changeset\README.md
```md
# Changesets

This folder stores release notes for version bumps managed by Changesets.

Create a new changeset before merging a user-facing change:

```bash
bunx changeset
```

After the changeset lands on `main`, GitHub Actions will open or update the release PR automatically. Merging that release PR publishes the next npm version.

```

### File: .todo\README.md
```md
# v4 API Implementation Tasks

This directory contains tasks for implementing the v4 API endpoints that query Clickhouse data as part of the transition to OpenTelemetry.

## Overview

The v4 API will replace the existing v2 API endpoints that query data from Supabase. The new endpoints will query data from Clickhouse, which stores OpenTelemetry trace, log, and metric data.

## Task Structure

Each task is defined in a separate Markdown file with the following structure:

1. Task name and description
2. Requirements
3. Implementation details
4. Testing requirements
5. Dependencies
6. Estimated time

## Task Dependencies

The tasks are ordered by dependency, with earlier tasks being dependencies for later tasks:

1. **Clickhouse Client**: Implement a client for connecting to Clickhouse
2. **Authentication Middleware**: Implement middleware for authenticating requests
3. **Trace Endpoints**: Implement endpoints for querying trace data
4. **Log Endpoints**: Implement endpoints for querying log data
5. **Metric Endpoints**: Implement endpoints for querying metric data
6. **Session Endpoints**: Implement endpoints for querying session data
7. **Computed Fields Migration**: Migrate computed fields from v2 to v4
8. **API Documentation**: Create documentation for the v4 API
9. **Testing and Validation**: Create tests for the v4 API
10. **Deployment and Monitoring**: Create a deployment and monitoring strategy

## Implementation Strategy

The implementation strategy is to create a new set of v4 endpoints that query data from Clickhouse, while maintaining backward compatibility with the existing v2 endpoints. This will allow for a gradual migration from v2 to v4.

## Computed Fields Migration

A key challenge in this implementation is migrating the computed fields from v2 to v4. In v2, these fields were computed by "meters", but in v4, they need to be computed from OpenTelemetry data in Clickhouse. Task 7 focuses on this migration.

## Authentication

The v4 endpoints will use the same authentication mechanism as the v3 endpoints, which exchange an API key for a JWT token. The token is then used to authenticate requests to the v4 endpoints.

## Testing

Each task includes testing requirements to ensure that the implementation is correct and performs well. Task 9 focuses on comprehensive testing of the entire v4 API.

## Deployment

Task 10 focuses on creating a deployment and monitoring strategy for the v4 API, including procedures for deploying, monitoring, and alerting.

```

### File: ai_defense\README.md
```md
# Cisco AI Defense Configuration Example

This example contains configuration files for using Cisco AI Defense in your NeMo Guardrails project.

## Files

- **`config.yml`**:  AI Defense configuration with optional settings

## Configuration Options

The AI Defense integration supports configurable timeout and error handling behavior:

- **`timeout`**: API request timeout in seconds (default: 30.0)
- **`fail_open`**: Behavior when API calls fail (default: false for fail closed)

For more details on the Cisco AI Defense integration, see [Cisco AI Defense Integration User Guide](../../../docs/user-guides/community/ai-defense.md).

```

### File: ai_defense_v2\README.md
```md
# Cisco AI Defense Configuration Example (Colang 2.x)

This example contains configuration files for using Cisco AI Defense with Colang 2.x in your NeMo Guardrails project.

## Files

- **`config.yaml`**: AI Defense configuration with optional settings
- **`main.co`**: Main flow definition
- **`rails.co`**: Input and output rails definitions for AI Defense

## Configuration Options

The AI Defense integration supports configurable timeout and error handling behavior:

- **`timeout`**: API request timeout in seconds (default: 30.0)
- **`fail_open`**: Behavior when API calls fail (default: false for fail closed)
  - `false`: Fail closed - blocks content when API errors occur
  - `true`: Fail open - allows content when API errors occur


## Environment Variables

Before running this example, set the required environment variables:

```bash
export AI_DEFENSE_API_KEY="your-api-key"
export AI_DEFENSE_API_ENDPOINT="us.api.inspect.aidefense.security.cisco.com/api/v1/inspect/chat"
```

For more details on the Cisco AI Defense integration, see [Cisco AI Defense Integration User Guide](../../../docs/user-guides/community/ai-defense.md).

```

### File: animations\README.md
```md
# CoreAnimationsE2E

This project was generated with [Angular CLI](https://github.com/angular/angular-cli) version 9.0.0-next.9.

## Development server

Run `ng serve` for a dev server. Navigate to `http://localhost:4200/`. The app will automatically reload if you change any of the source files.

## Code scaffolding

Run `ng generate component component-name` to generate a new component. You can also use `ng generate directive|pipe|service|class|guard|interface|enum|module`.

## Build

Run `ng build` to build the project. The build artifacts will be stored in the `dist/` directory. Use the `--prod` flag for a production build.

## Running unit tests

Run `ng test` to execute the unit tests via [Karma](https://karma-runner.github.io).

## Running end-to-end tests

Run `ng e2e` to execute the end-to-end tests via [Protractor](https://www.protractortest.org/).

## Further help

To get more help on the Angular CLI use `ng help` or go check out the [Angular CLI README](https://github.com/angular/angular-cli/blob/main/README.md).

```

### File: api\README.md
```md
# LightRAG Server and WebUI

The LightRAG Server is designed to provide a Web UI and API support. The Web UI facilitates document indexing, knowledge graph exploration, and a simple RAG query interface. LightRAG Server also provides an Ollama-compatible interface, aiming to emulate LightRAG as an Ollama chat model. This allows AI chat bots, such as Open WebUI, to access LightRAG easily.

![image-20250323122538997](./README.assets/image-20250323122538997.png)

![image-20250323122754387](./README.assets/image-20250323122754387.png)

![image-20250323123011220](./README.assets/image-20250323123011220.png)

## Getting Started

### Installation

* Install from PyPI

```bash
### Install LightRAG Server as tool using uv (recommended)
uv tool install "lightrag-hku[api]"

### Or using pip
# python -m venv .venv
# source .venv/bin/activate  # Windows: .venv\Scripts\activate
# pip install "lightrag-hku[api]"
```

* Installation from Source

```bash
# Clone the repository
git clone https://github.com/HKUDS/lightrag.git

# Change to the repository directory
cd lightrag

# Bootstrap the development environment (recommended)
make dev
source .venv/bin/activate  # Activate the virtual environment (Linux/macOS)
# Or on Windows: .venv\Scripts\activate

# make dev installs the test toolchain plus the full offline stack
# (API, storage backends, and provider integrations), then builds the frontend.
# Run make env-base or copy env.example to .env before starting the server.

# Equivalent manual steps with uv
# Note: uv sync automatically creates a virtual environment in .venv/
uv sync --extra test --extra offline
source .venv/bin/activate  # Activate the virtual environment (Linux/macOS)
# Or on Windows: .venv\Scripts\activate

# Or using pip with virtual environment
# python -m venv .venv
# source .venv/bin/activate  # Windows: .venv\Scripts\activate
# pip install -e ".[test,offline]"

# Build front-end artifacts
cd lightrag_webui
bun install --frozen-lockfile
bun run build
cd ..
```

### Before Starting LightRAG Server

LightRAG necessitates the integration of both an LLM (Large Language Model) and an Embedding Model to effectively execute document indexing and querying operations. Prior to the initial deployment of the LightRAG server, it is essential to configure the settings for both the LLM and the Embedding Model. LightRAG supports binding to various LLM/Embedding backends:

* ollama
* lollms
* openai or openai compatible
* azure_openai
* aws_bedrock
* gemini

It is recommended to use environment variables to configure the LightRAG Server. There is an example environment variable file named `env.example` in the root directory of the project. Please copy this file to the startup directory and rename it to `.env`. After that, you can modify the parameters related to the LLM and Embedding models in the `.env` file. It is important to note that the LightRAG Server will load the environment variables from `.env` into the system environment variables each time it starts. **LightRAG Server will prioritize the settings in the system environment variables to .env file**.

> Since VS Code with the Python extension may automatically load the .env file in the integrated terminal, please open a new terminal session after each modification to the .env file.

Here are some examples of common settings for LLM and Embedding models:

* OpenAI LLM + Ollama Embedding:

```
LLM_BINDING=openai
LLM_MODEL=gpt-4o
LLM_BINDING_HOST=https://api.openai.com/v1
LLM_BINDING_API_KEY=your_api_key

EMBEDDING_BINDING=ollama
EMBEDDING_BINDING_HOST=http://localhost:11434
EMBEDDING_MODEL=bge-m3:latest
EMBEDDING_DIM=1024
# EMBEDDING_BINDING_API_KEY=your_api_key
```

> When targeting Google Gemini, set `LLM_BINDING=gemini`, choose a model such as `LLM_MODEL=gemini-flash-latest`, and provide your Gemini key via `LLM_BINDING_API_KEY` (or `GEMINI_API_KEY`).

* Ollama LLM + Ollama Embedding:

```
LLM_BINDING=ollama
LLM_MODEL=mistral-nemo:latest
LLM_BINDING_HOST=http://localhost:11434
# LLM_BINDING_API_KEY=your_api_key
###  Ollama Server context length (Must be larger than MAX_TOTAL_TOKENS+2000)
OLLAMA_LLM_NUM_CTX=16384

EMBEDDING_BINDING=ollama
EMBEDDING_BINDING_HOST=http://localhost:11434
EMBEDDING_MODEL=bge-m3:latest
EMBEDDING_DIM=1024
# EMBEDDING_BINDING_API_KEY=your_api_key
```

> **Important Note**: The Embedding model must be determined before document indexing, and the same model must be used during the document query phase. For certain storage solutions (e.g., PostgreSQL), the vector dimension must be defined upon initial table creation. Therefore, when changing embedding models, it is necessary to delete the existing vector-related tables and allow LightRAG to recreate them with the new dimensions.

### Create .env File With Setup Tool

Instead of editing `env.example` by hand, you can use the interactive setup wizard to generate a configured `.env` and, when needed, `docker-compose.final.yml`:

```bash
make env-base           # Required first step: LLM, embedding, reranker
make env-storage        # Optional: storage backends and database services
make env-server         # Optional: server port, auth, and SSL
make env-security-check # Optional: audit the current .env for security risks
```

For a full description of every target and what each flow does, see [docs/InteractiveSetup.md](../../docs/InteractiveSetup.md).
The setup wizards update configuration only; run `make env-security-check` separately to audit the
current `.env` for security risks before deployment.

### Starting LightRAG Server

The LightRAG Server supports two operational modes:
* The simple and efficient Uvicorn mode:

```
lightrag-server
```
* The multiprocess Gunicorn + Uvicorn mode (production mode, not supported on Windows environments):

```
lightrag-gunicorn --workers 4
```

When starting LightRAG, the current working directory must contain the `.env` configuration file. **It is intentionally designed that the `.env` file must be placed in the startup directory**. The purpose of this is to allow users to launch multiple LightRAG instances simultaneously and configure different `.env` files for different instances. **After modifying the `.env` file, you need to reopen the terminal for the new settings to take effect.** This is because each time LightRAG Server starts, it loads the environment variables from the `.env` file into the system environment variables, and system environment variables have higher precedence.

During startup, configurations in the `.env` file can be overridden by command-line parameters. Common command-line parameters include:

- `--host`: Server listening address (default: 0.0.0.0)
- `--port`: Server listening port (default: 9621)
- `--timeout`: LLM request timeout (default: 150 seconds)
- `--log-level`: Log level (default: INFO)
- `--working-dir`: Database persistence directory (default: ./rag_storage)
- `--input-dir`: Directory for uploaded files (default: ./inputs)
- `--workspace`: Workspace name, used to logically isolate data between multiple LightRAG instances (default: empty)

### Launching LightRAG Server with Docker

Using Docker Compose is the most convenient way to deploy and run the LightRAG Server.

- Create a project directory.
- Copy the `docker-compose.yml` file from the LightRAG repository into your project directory.
- Prepare the `.env` file: Duplicate the sample file [`env.example`](https://ai.znipower.com:5013/c/env.example)to create a customized `.env` file, and configure the LLM and embedding parameters according to your specific requirements.
- Start the LightRAG Server with the following command:

```shell
docker compose up
# If you want the program to run in the background after startup, add the -d parameter at the end of the command.
```

You can get the official docker compose file from here: [docker-compose.yml](https://raw.githubusercontent.com/HKUDS/LightRAG/refs/heads/main/docker-compose.yml). For historical versions of LightRAG docker images, visit this link: [LightRAG Docker Images](https://github.com/HKUDS/LightRAG/pkgs/container/lightrag). For more details about docker deployment, please refer to [DockerDeployment.md](./../../docs/DockerDeployment.md).

### Nginx Reverse Proxy Configuration

When using Nginx as a reverse proxy in front of LightRAG Server, you need to configure `client_max_body_size` for the `/documents/upload` endpoint to handle large file uploads. Without this configuration, Nginx will reject files larger than 1MB (the default limit) with a `413 Request Entity Too Large` error before the request reaches LightRAG.

**Recommended Configuration:**

```nginx
server {
    listen 80;
    server_name your-domain.com;

    # Global default: 8MB for LLM queries with long context
    client_max_body_size 8M;

    # Upload endpoint: 100MB for large file uploads
    location /documents/upload {
        client_max_body_size 100M;

        proxy_pass http://localhost:9621;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;

        # Increase timeouts for large file uploads
        proxy_read_timeout 300s;
        proxy_send_timeout 300s;
    }

    # Streaming endpoints: LLM response streaming
    location ~ ^/(query/stream|api/chat|api/generate) {
        gzip off;  # Disable compression for streaming responses

        proxy_pass http://localhost:9621;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;

        # Long timeout for LLM generation
        proxy_read_timeout 300s;
    }

    # Other endpoints
    location / {
        proxy_pass http://localhost:9621;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

**Key Points:**

1. **Global Limit (8MB)**: Sufficient for LLM queries with long conversation history and context (128K tokens ≈ 512KB + JSON overhead).
2. **Upload Endpoint (100MB)**: Must match or exceed `MAX_UPLOAD_SIZE` in your `.env` file. The default `MAX_UPLOAD_SIZE` is 100MB.
3. **Streaming Endpoints**: Disable gzip compression (`gzip off`) for streaming endpoints to ensure real-time response delivery. LightRAG automatically sets `X-Accel-Buffering: no` header to disable response buffering.
4. **Timeout Settings**: Large file uploads and LLM generation require longer timeouts; adjust `proxy_read_timeout` and `proxy_send_timeout` accordingly.
5. **Size Validation Layers**:
   - Nginx validates the `Content-Length` header first
   - LightRAG performs streaming validation during upload
   - Setting appropriate limits at both layers ensures better error messages and security

### Offline Deployment

Official LightRAG Docker images are fully compatible with offline or air-gapped environments. If you want to build up you own  offline enviroment, please refer to [Offline Deployment Guide](./../../docs/OfflineDeployment.md).

### Starting Multiple LightRAG Instances

There are two ways to start multiple LightRAG instances. The first way is to configure a completely independent working environment for each instance. This requires creating a separate working directory for each instance and placing a dedicated `.env` configuration file in that directory. The server listening ports in the configuration files of different instances cannot be the same. Then, you can start the service by running `lightrag-server` in the working directory.

The second way is for all instances to share the same set of `.env` configuration files, and then use command-line arguments to specify different server listening ports and workspaces for each instance. You can start multiple LightRAG instances in the same working directory with different command-line arguments. For example:

```
# Start instance 1
lightrag-server --port 9621 --workspace space1

# Start instance 2
lightrag-server --port 9622 --workspace space2
```

The purpose of a workspace is to achieve data isolation between different instances. Therefore, the `workspace` parameter must be different for different instances; otherwise, it will lead to data confusion and corruption.

When launching multiple LightRAG instances via Docker Compose, simply specify unique `WORKSPACE` and `PORT` environment variables for each container within your `docker-compose.yml`. Even if all instances share a common `.env` file, the container-specific environment variables defined in Compose will take precedence, ensuring independent configurations for each instance.

### Data Isolation Between LightRAG Instances

Configuring an independent working directory and a dedicated `.env` configuration file for each instance can generally ensure that locally persisted files in the in-memory database are saved in their respective working directories, achieving data isolation. By default, LightRAG uses all in-memory databases, and this method of data isolation is sufficient. However, if you are using an external database, and different instances access the same database instance, you need to use workspaces to achieve data isolation; otherwise, the data of different instances will conflict and be destroyed.

The command-line `workspace` argument and the `WORKSPACE` environment variable in the `.env` file can both be used to specify the workspace name for the current instance, with the command-line argument having higher priority. Here is how workspaces are implemented for different types of storage:

- **For local file-based databases, data isolation is achieved through workspace subdirectories:** `JsonKVStorage`, `JsonDocStatusStorage`, `NetworkXStorage`, `NanoVectorDBStorage`, `FaissVectorDBStorage`.
- **For databases that store data in collections, it's done by adding a workspace prefix to the collection name:** `RedisKVStorage`, `RedisDocStatusStorage`, `MilvusVectorDBStorage`, `MongoKVStorage`, `MongoDocStatusStorage`, `MongoVectorDBStorage`, `MongoGraphStorage`, `PGGraphStorage`.
- **For Qdrant vector database, data isolation is achieved through payload-based partitioning (Qdrant's recommended multitenancy approach):** `QdrantVectorDBStorage` uses shared collections with payload filtering for unlimited workspace scalability.
- **For relational databases, data isolation is achieved by adding a `workspace` field to the tables for logical data separation:** `PGKVStorage`, `PGVectorStorage`, `PGDocStatusStorage`.
- **For graph databases, logical data isolation is achieved through labels:** `Neo4JStorage`, `MemgraphStorage`
- **For OpenSearch, data isolation is achieved through index name prefixes:** `OpenSearchKVStorage`, `OpenSearchDocStatusStorage`, `OpenSearchGraphStorage`, `OpenSearchVectorDBStorage`

To maintain compatibility with 
... [TRUNCATED]
```

### File: app\README.md
```md
# Tauri + React + Typescript

This template should help get you started developing with Tauri, React and Typescript in Vite.

## Recommended IDE Setup

- [VS Code](https://code.visualstudio.com/) + [Tauri](https://marketplace.visualstudio.com/items?itemName=tauri-apps.tauri-vscode) + [rust-analyzer](https://marketplace.visualstudio.com/items?itemName=rust-lang.rust-analyzer)

```

### File: autoalign\README.md
```md
# AutoAlign

This example showcases the use of AutoAlign guardrails.

The structure of the config folders is the following:
- `autoalign_config` - example configuration folder for all guardrails (except factcheck)
  - `config.yml` - The config file holding all the configuration options.
- `autoalign_groundness_config` - example configuration folder for AutoAlign's groundness check
  - `kb` - The folder containing documents that form the knowledge base.
  - `config.yml` - The config file holding all the configuration options.
- `autoalign_factcheck_config` - example configuration folder for AutoAlign's factcheck
  - `config.yml` - The config file holding all the configuration options.

```

### File: backend\README.md
```md
[Getting Started (Released)](https://docs.agpt.co/platform/getting-started/#autogpt_agent_server)
```

### File: backend\requirements.txt
```txt
fastapi>=0.109.0
uvicorn[standard]>=0.27.0
sqlalchemy>=2.0.25
psycopg2-binary>=2.9.9
asyncpg>=0.29.0
greenlet>=3.0.0
pydantic>=2.10.0
pydantic-settings>=2.1.0
python-dotenv>=1.0.1
httpx>=0.26.0
mcp>=1.0.0
structlog>=24.1.0
python-json-logger>=2.0.7
cvss>=2.6

```

### File: benchmark\readme.md
```md
<h1 align="center">
        LLM-Bench
    </h1>
    <p align="center">
        <p align="center">Benchmark LLMs response, cost and response time</p>
        <p>LLM vs Cost per input + output token ($)</p>
        <img width="806" alt="Screenshot 2023-11-13 at 2 51 06 PM" src="https://github.com/BerriAI/litellm/assets/29436595/6d1bed71-d062-40b8-a113-28359672636a">
    </p>
        <a href="https://docs.google.com/spreadsheets/d/1mvPbP02OLFgc-5-Ubn1KxGuQQdbMyG1jhMSWxAldWy4/edit?usp=sharing">
               Bar Graph Excel Sheet here
        </a>

| Model | Provider | Cost per input + output token ($)|
| --- | --- | --- |
| openrouter/mistralai/mistral-7b-instruct | openrouter | 0.0 |
| ollama/llama2 | ollama | 0.0 |
| ollama/llama2:13b | ollama | 0.0 |
| ollama/llama2:70b | ollama | 0.0 |
| ollama/llama2-uncensored | ollama | 0.0 |
| ollama/mistral | ollama | 0.0 |
| ollama/codellama | ollama | 0.0 |
| ollama/orca-mini | ollama | 0.0 |
| ollama/vicuna | ollama | 0.0 |
| perplexity/codellama-34b-instruct | perplexity | 0.0 |
| perplexity/llama-2-13b-chat | perplexity | 0.0 |
| perplexity/llama-2-70b-chat | perplexity | 0.0 |
| perplexity/mistral-7b-instruct | perplexity | 0.0 |
| perplexity/replit-code-v1.5-3b | perplexity | 0.0 |
| text-bison | vertex_ai-text-models | 0.00000025 |
| text-bison@001 | vertex_ai-text-models | 0.00000025 |
| chat-bison | vertex_ai-chat-models | 0.00000025 |
| chat-bison@001 | vertex_ai-chat-models | 0.00000025 |
| chat-bison-32k | vertex_ai-chat-models | 0.00000025 |
| code-bison | vertex_ai-code-text-models | 0.00000025 |
| code-bison@001 | vertex_ai-code-text-models | 0.00000025 |
| code-gecko@001 | vertex_ai-chat-models | 0.00000025 |
| code-gecko@latest | vertex_ai-chat-models | 0.00000025 |
| codechat-bison | vertex_ai-code-chat-models | 0.00000025 |
| codechat-bison@001 | vertex_ai-code-chat-models | 0.00000025 |
| codechat-bison-32k | vertex_ai-code-chat-models | 0.00000025 |
| palm/chat-bison | palm | 0.00000025 |
| palm/chat-bison-001 | palm | 0.00000025 |
| palm/text-bison | palm | 0.00000025 |
| palm/text-bison-001 | palm | 0.00000025 |
| palm/text-bison-safety-off | palm | 0.00000025 |
| palm/text-bison-safety-recitation-off | palm | 0.00000025 |
| anyscale/meta-llama/Llama-2-7b-chat-hf | anyscale | 0.0000003 |
| anyscale/mistralai/Mistral-7B-Instruct-v0.1 | anyscale | 0.0000003 |
| openrouter/meta-llama/llama-2-13b-chat | openrouter | 0.0000004 |
| openrouter/nousresearch/nous-hermes-llama2-13b | openrouter | 0.0000004 |
| deepinfra/meta-llama/Llama-2-7b-chat-hf | deepinfra | 0.0000004 |
| deepinfra/mistralai/Mistral-7B-Instruct-v0.1 | deepinfra | 0.0000004 |
| anyscale/meta-llama/Llama-2-13b-chat-hf | anyscale | 0.0000005 |
| amazon.titan-text-lite-v1 | bedrock | 0.0000007 |
| deepinfra/meta-llama/Llama-2-13b-chat-hf | deepinfra | 0.0000007 |
| text-babbage-001 | text-completion-openai | 0.0000008 |
| text-ada-001 | text-completion-openai | 0.0000008 |
| babbage-002 | text-completion-openai | 0.0000008 |
| openrouter/google/palm-2-chat-bison | openrouter | 0.000001 |
| openrouter/google/palm-2-codechat-bison | openrouter | 0.000001 |
| openrouter/meta-llama/codellama-34b-instruct | openrouter | 0.000001 |
| deepinfra/codellama/CodeLlama-34b-Instruct-hf | deepinfra | 0.0000012 |
| deepinfra/meta-llama/Llama-2-70b-chat-hf | deepinfra | 0.0000016499999999999999 |
| deepinfra/jondurbin/airoboros-l2-70b-gpt4-1.4.1 | deepinfra | 0.0000016499999999999999 |
| anyscale/meta-llama/Llama-2-70b-chat-hf | anyscale | 0.000002 |
| anyscale/codellama/CodeLlama-34b-Instruct-hf | anyscale | 0.000002 |
| gpt-3.5-turbo-1106 | openai | 0.000003 |
| openrouter/meta-llama/llama-2-70b-chat | openrouter | 0.000003 |
| amazon.titan-text-express-v1 | bedrock | 0.000003 |
| gpt-3.5-turbo | openai | 0.0000035 |
| gpt-3.5-turbo-0301 | openai | 0.0000035 |
| gpt-3.5-turbo-0613 | openai | 0.0000035 |
| gpt-3.5-turbo-instruct | text-completion-openai | 0.0000035 |
| openrouter/openai/gpt-3.5-turbo | openrouter | 0.0000035 |
| cohere.command-text-v14 | bedrock | 0.0000035 |
| gpt-3.5-turbo-0613 | openai | 0.0000035 |
| claude-instant-1 | anthropic | 0.00000714 |
| claude-instant-1.2 | anthropic | 0.00000714 |
| openrouter/anthropic/claude-instant-v1 | openrouter | 0.00000714 |
| anthropic.claude-instant-v1 | bedrock | 0.00000714 |
| openrouter/mancer/weaver | openrouter | 0.00001125 |
| j2-mid | ai21 | 0.00002 |
| ai21.j2-mid-v1 | bedrock | 0.000025 |
| openrouter/jondurbin/airoboros-l2-70b-2.1 | openrouter | 0.00002775 |
| command-nightly | cohere | 0.00003 |
| command | cohere | 0.00003 |
| command-light | cohere | 0.00003 |
| command-medium-beta | cohere | 0.00003 |
| command-xlarge-beta | cohere | 0.00003 |
| command-r-plus| cohere | 0.000018 |
| j2-ultra | ai21 | 0.00003 |
| ai21.j2-ultra-v1 | bedrock | 0.0000376 |
| gpt-4-1106-preview | openai | 0.00004 |
| gpt-4-vision-preview | openai | 0.00004 |
| claude-2 | anthropic | 0.0000437 |
| openrouter/anthropic/claude-2 | openrouter | 0.0000437 |
| anthropic.claude-v1 | bedrock | 0.0000437 |
| anthropic.claude-v2 | bedrock | 0.0000437 |
| gpt-4 | openai | 0.00009 |
| gpt-4-0314 | openai | 0.00009 |
| gpt-4-0613 | openai | 0.00009 |
| openrouter/openai/gpt-4 | openrouter | 0.00009 |
| gpt-4-32k | openai | 0.00018 |
| gpt-4-32k-0314 | openai | 0.00018 |
| gpt-4-32k-0613 | openai | 0.00018 |



## Setup:
```
git clone https://github.com/BerriAI/litellm
```
cd to `benchmark` dir
```
cd litellm/cookbook/benchmark
```

### Install Dependencies
```
pip install litellm click tqdm tabulate termcolor
```

### Configuration
In `benchmark/benchmark.py` select your LLMs, LLM API Key and questions

Supported LLMs: https://docs.litellm.ai/docs/providers

```python
# Define the list of models to benchmark
models = ['gpt-3.5-turbo', 'togethercomputer/llama-2-70b-chat', 'claude-2']

# Enter LLM API keys
os.environ['OPENAI_API_KEY'] = ""
os.environ['ANTHROPIC_API_KEY'] = ""
os.environ['TOGETHERAI_API_KEY'] = ""

# List of questions to benchmark (replace with your questions)
questions = [
    "When will BerriAI IPO?",
    "When will LiteLLM hit $100M ARR?"
]

```

## Run LLM-Bench
```
python3 benchmark.py
```

## Expected Output
```
Running question: When will BerriAI IPO? for model: claude-2: 100%|████████████████████████████████████████████████████████████████████████████████████| 3/3 [00:13<00:00,  4.41s/it]

Benchmark Results for 'When will BerriAI IPO?':
+-----------------+----------------------------------------------------------------------------------+---------------------------+------------+
| Model           | Response                                                                         | Response Time (seconds)   | Cost ($)   |
+=================+==================================================================================+===========================+============+
| gpt-3.5-turbo   | As an AI language model, I cannot provide up-to-date information or predict      | 1.55 seconds              | $0.000122  |
|                 | future events. It is best to consult a reliable financial source or contact      |                           |            |
|                 | BerriAI directly for information regarding their IPO plans.                      |                           |            |
+-----------------+----------------------------------------------------------------------------------+---------------------------+------------+
| togethercompute | I'm not able to provide information about future IPO plans or dates for BerriAI  | 8.52 seconds              | $0.000531  |
| r/llama-2-70b-c | or any other company. IPO (Initial Public Offering) plans and timelines are      |                           |            |
| hat             | typically kept private by companies until they are ready to make a public        |                           |            |
|                 | announcement.  It's important to note that IPO plans can change and are subject  |                           |            |
|                 | to various factors, such as market conditions, financial performance, and        |                           |            |
|                 | regulatory approvals. Therefore, it's difficult to predict with certainty when   |                           |            |
|                 | BerriAI or any other company will go public.  If you're interested in staying    |                           |            |
|                 | up-to-date with BerriAI's latest news and developments, you may want to follow   |                           |            |
|                 | their official social media accounts, subscribe to their newsletter, or visit    |                           |            |
|                 | their website periodically for updates.                                          |                           |            |
+-----------------+----------------------------------------------------------------------------------+---------------------------+------------+
| claude-2        | I do not have any information about when or if BerriAI will have an initial      | 3.17 seconds              | $0.002084  |
|                 | public offering (IPO). As an AI assistant created by Anthropic to be helpful,    |                           |            |
|                 | harmless, and honest, I do not have insider knowledge about Anthropic's business |                           |            |
|                 | plans or strategies.                                                             |                           |            |
+-----------------+----------------------------------------------------------------------------------+---------------------------+------------+
```

## Support 
**🤝 Schedule a 1-on-1 Session:** Book a [1-on-1 session](https://enterprise.litellm.ai/demo) with Krrish and Ishaan, the founders, to discuss any issues, provide feedback, or explore how we can improve LiteLLM for you.

```

### File: benchmarks\README.md
```md
# HyperspaceDB Benchmarks

> **⚠️ ATTENTION:** Don't take anyone's word for it, verify all numbers yourself! We provide the exact scripts used to generate our results so you can reproduce them on your own hardware.

## 1. Project Overview

This directory contains reproducible benchmark tooling for HyperspaceDB and other vector databases.
The main goal is to measure throughput, latency, and retrieval quality on the same datasets and query sets.

The project now includes:
- a **modular plugin-based runner** (`run_benchmark.py`) for scalable adapter growth (add you DB or custom metrics, if you want);

## 2. Core Functionalities

- Run benchmark against all supported databases at once.
- Run benchmark for only one database adapter.
- Add new database by creating one plugin file in `db_plugins/adapters/`.
- Reuse the same data preparation and metric logic across adapters.
- Compare legacy and modular reports to track metric parity.
- Run durability benchmark (`run_durability_benchmark.py`) independently.

## 3. Docs and Libraries

### Main references
- HuggingFace `datasets` for dataset loading.
- `vectordb-bench` for standardized benchmark cases.
- DB SDKs: `pymilvus`, `qdrant-client`, `chromadb`, Hyperspace Python SDK.
- `torch`, `transformers`, `peft` for embedding generation.

### Install
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install -e ../sdks/python
```

### Start DB stack
```bash
docker-compose up -d
```

## 4. Current File Structure (Snapshot)

```text
benchmarks/
├── README.md
├── requirements.txt
├── docker-compose.yml
├── download_dataset.py
├── run_benchmark.py
├── run_durability_benchmark.py
├── plugin_runtime.py
├── db_plugins/
    ├── __init__.py
    ├── base.py
    ├── registry.py
    └── adapters/
        ├── __init__.py
        ├── chroma_plugin.py
        ├── hyperspace_plugin.py
        ├── milvus_plugin.py
        └── qdrant_plugin.py

```

## 5. Run Commands

### Benchmark runner
```bash
python3 run_benchmark.py hyper --case=Performance1024D1M
python3 run_benchmark.py --case=Performance1024D1M
python3 run_benchmark.py hyper
```

## 6. Benchmark Metrics

- Throughput (Insert/Search QPS)
- Latency (P50/P95/P99)
- Recall@10, MRR@10, NDCG@10
- System Recall@10 (vs exact brute-force)
- Concurrency profile (C1/C10/C30)
- **LSM-Tree Flush Latency**: Impact of WAL rotation on active search performance.
- **S3 Tiering Cold Latency**: First-access latency for chunks retrieved from cloud storage.
- **Cache Hit Ratio**: Effectiveness of the local `moka` LRU cache.
- Disk usage (Local vs Cloud breakdown).

```

### File: benchmarks\requirements.txt
```txt
pydantic<2.0.0
numpy>=1.26.0,<2.0.0
tqdm>=4.64.0
datasets>=2.8.0
vectordb-bench>=0.1.0
torch>=1.13.0
transformers>=4.25.0
peft>=0.2.0
sentence-transformers>=2.2.0
pymilvus>=2.3.0
qdrant-client>=1.7.0,<1.8.0
weaviate-client>=3.25.0,<4.0.0
chromadb>=0.4.0,<0.5.0
requests>=2.28.0
grpcio>=1.64.0
grpcio-tools>=1.64.0
protobuf>=5.29.0
h5py>=3.7.0
pandas>=2.0.0
pytest>=8.0.0
psycopg2-binary>=2.9.9
pgvector>=0.2.4

```

### File: caching\Readme.md
```md
# Caching on LiteLLM

LiteLLM supports multiple caching mechanisms. This allows users to choose the most suitable caching solution for their use case.

The following caching mechanisms are supported:

1. **RedisCache**
2. **RedisSemanticCache**
3. **QdrantSemanticCache**
4. **InMemoryCache**
5. **DiskCache**
6. **S3Cache**
7. **AzureBlobCache**
8. **DualCache** (updates both Redis and an in-memory cache simultaneously)

## Folder Structure

```
litellm/caching/
├── base_cache.py
├── caching.py
├── caching_handler.py
├── disk_cache.py
├── dual_cache.py
├── in_memory_cache.py
├── qdrant_semantic_cache.py
├── redis_cache.py
├── redis_semantic_cache.py
├── s3_cache.py
```

## Documentation
- [Caching on LiteLLM Gateway](https://docs.litellm.ai/docs/proxy/caching)
- [Caching on LiteLLM Python](https://docs.litellm.ai/docs/caching/all_caches)








```

### File: claude\README.md
```md
# Claude Inspired Design System

[DESIGN.md](https://github.com/VoltAgent/awesome-design-md/blob/main/design-md/claude/DESIGN.md) extracted from the public [claude](https://claude.ai/) website. This is not the official design system. Colors, fonts, and spacing may not be 100% accurate. But it's a good starting point for building something similar.

## Files

| File | Description |
|------|-------------|
| `DESIGN.md` | Complete design system documentation (9 sections) |
| `preview.html` | Interactive design token catalog (light) |
| `preview-dark.html` | Interactive design token catalog (dark) |


Use [DESIGN.md](https://github.com/VoltAgent/awesome-design-md/blob/main/design-md/claude/DESIGN.md) to use as a reference for AI agents (Claude, Cursor, Stitch) to generate UI that looks like the Claude design language.

## Preview

A sample landing page built with DESIGN.md. It shows the actual colors, typography, buttons, cards, spacing, and elevation, all in one page.

### Dark Mode
![Claude Design System — Dark Mode](https://pub-2e4ecbcbc9b24e7b93f1a6ab5b2bc71f.r2.dev/designs/claude/preview-dark-screenshot.png)

### Light Mode
![Claude Design System — Light Mode](https://pub-2e4ecbcbc9b24e7b93f1a6ab5b2bc71f.r2.dev/designs/claude/preview-screenshot.png)

```

### File: clavata\README.md
```md
# Clavata Example

This example demonstrates how to integrate with the [Clavata](https://clavata.ai) API for content moderation.

To test this configuration you can use the CLI Chat by running the following command from the `examples/configs/clavata` directory:

```bash
nemoguardrails chat
```

The structure of the config folder is the following:

- `config.yml` - The config file holding all the configuration options for Clavata integration.

Please see the docs for more details about:

- [Full Clavata integration guide](../../../docs/user-guides/community/clavata.md)
- [Configuration options and setup instructions](../../../docs/user-guides/community/clavata.md#setup)
- [Error handling and best practices](../../../docs/user-guides/community/clavata.md#error-handling)

```

### File: clavata_v2\README.md
```md
# Clavata Example

This example demonstrates how to integrate with the [Clavata](https://clavata.ai) API for content moderation.

To test this configuration you can use the CLI Chat by running the following command from the `examples/configs/clavata` directory:

```bash
nemoguardrails chat
```

The structure of the config folder is the following:

- `config.yml` - The config file holding all the configuration options for Clavata integration.
- `rails.co` - This file shows how to use Clavata's rails if you're using `colang v2.x`. In version `2.x` configuration of rails via the `config.yml` file is deprecated and the new approach shown in `rails.co` is something you would include in your flows.

Please see the docs for more details about:

- [Full Clavata integration guide](../../../docs/user-guides/community/clavata.md)
- [Configuration options and setup instructions](../../../docs/user-guides/community/clavata.md#setup)
- [Error handling and best practices](../../../docs/user-guides/community/clavata.md#error-handling)

## Policy Matching vs Label Matching

If you take a peek at the example [config.yml](config.yml), you'll notice that the integration no longer specifies `input` or `output` keys. Instead, the input and output rails are specified in a `rails.co` file as shown [here](./rails.co).

Additionally, because the `$input_text` or `$output_text` is passed directly to the rail, both input and output rails use the same Clavata action flow `clavata check for`. Just pass the text to be evaluated, the policy to use, and, optionally, the specific labels to look for, and the flow will take care of the rest.

Whether specific label matches are necessary will depend on both the policy being used, and what you're trying to accomplish. For most use cases, matching on the policy will likely be sufficient.

**As an example of when you might want to specify labels:**

Suppose you are using the same policy for input and output rails. In this case, the policy might include many labels, with some relevant to input, some relevant to output, and some relevant to both. You can specify the labels for input and output rails to ensure each rail only triggers when appropriate.

> Note: When setting specific labels to match, you can also control whether the logic is `ALL` (meaning all specified labels must be found), or `ANY`, meaning any of the specific labels being found will trigger the rail. The default is `ANY`, but you can control this by setting the `label_match_logic` key in your [rails config](./config.yml).

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.

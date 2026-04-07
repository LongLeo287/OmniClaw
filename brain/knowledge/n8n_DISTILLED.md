---
id: n8n
type: knowledge
owner: OA_Triage
---
# n8n
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
World's first n8n client that manage workflow collections inside VSCode/Cursor/Antigravity
- Walkthrough video: <a href="https://www.youtube.com/watch?v=1KgItvryNdA" target="_blank">n8n atom + Antigravity: vibe building workflow (feel like vibe coding)</a>
- Website: <a href="https://atom8n.com/" target="_blank">www.atom8n.com</a>
- Download the client extension: <a href="https://open-vsx.org/extension/atom8n/n8n-atom-v3" target="_blank">n8n Atom 3.0</a>
- Join Our Community: <a href="https://discord.gg/9MmAhtJFWW" target="_blank">Discord</a>, <a href="https://web.facebook.com/groups/atom8n" target="_blank">Facebook</a>
- Nodejs installation:
```
npx -y @atom8n/n8n@latest
```
Or docker:
```
docker volume create n8n_data

docker run --pull=always -it --rm --name n8n-atom -p 5888:5888 -v n8n_data:/home/node/.n8n atom8n/n8n:fork
```


<img width="2718" height="1618" alt="image" src="https://github.com/user-attachments/assets/8cc10306-e349-4cac-b5b7-e04cc9695ca0" />
<img width="2100" height="1358" alt="image" src="https://github.com/user-attachments/assets/6f53d124-27e8-45e2-935f-3933ad42ff12" />
<img width="2114" height="1496" alt="image" src="https://github.com/user-attachments/assets/c48534d1-742f-4981-b5eb-557f610015d2" />

## n8n Atom
n8n Atom is the world's first n8n client that manages workflow collections directly inside VSCode, Cursor, and Antigravity.

**Key Features:**
- File-Based Workflows: Convert n8n workflows into file format (.n8n) that can be committed to GitHub, enabling proper version control and collaboration
- Native Editor Integration: Full drag-and-drop n8n UI embedded directly in your editor, forked from the official n8n front-end
- AI-Powered Workflow Building: Leverage AI coding agents (like Antigravity) to iteratively build and improve workflows by editing the workflow JSON files directly
- Seamless Workflow Management: Create, edit, execute, and manage n8n workflows without leaving your development environment
- Local Development: Works with local n8n server instances, perfect for development and testing workflows before deploying to production

**Why n8n Atom?**
The main motivation behind this project was to make workflows file-based, so they can be committed to GitHub and version controlled like regular code. This also allows developers to leverage AI coding assistants to efficiently build and iterate on workflows, transforming the manual UI-based workflow creation process into a code-driven, version-controlled development experience.

**Perfect For:**
- Developers who want to version control their n8n workflows
Teams looking to integrate workflow development into their existing development workflow
- Users of Antigravity, Cursor, or VSCode who want a unified development environment
- Anyone who wants to leverage AI coding agents to build and improve workflows programmatically

## Story behind
As a developer working frequently with n8n workflows, I realized a core problem: **workflows couldn't be managed like code**.

**The problems I faced:**
- Workflows were stored in n8n's database, making version control impossible
- Every change required manual UI work, which was time-consuming and error-prone
- No way to review changes before deploying
- Couldn't leverage AI coding agents to build workflows automatically
- Had to switch between multiple tools, breaking my development flow

**The inspiration:**
I wanted to bring workflows into the file-based world so they could be committed to GitHub and version controlled like regular code. This would also allow developers to leverage AI coding assistants to efficiently build and iterate on workflows.

**The journey:**
I spent 2 days "vibe coding" with Antigravity to build the MVP. The experience was incredible, I could input 100% in natural language and build workflows seamlessly, just like coding. In those 2 days, I:
- Forked the front-end from the official n8n repository
- Integrated n8n UI into a VSCode extension
- Implemented a file-based workflow system (.n8n format)
- Created the world's first extension to manage n8n workflows in an editor

## Killing feature
<img alt="image" src="https://github.com/user-attachments/assets/8692fa68-c290-42f5-83ca-64c7b01f85b8" />


## Testimonials (for reference)
- "I've been waiting a long time for an extension like this, I think it's awesome"
- "Being able to version control workflows like regular code changes everything"
- "The workflow is incredibly powerful when used with other tools like Kanban and Thor Client"
- "This feels like you materialized the vision of turning VS Code into a true AI cockpit"
<img alt="image" src="https://github.com/user-attachments/assets/5ca3bb39-248f-407a-b5c5-6a09a261bc24" />
<img alt="image" src="https://github.com/user-attachments/assets/ee9d5d1c-8c62-475b-bf72-f677c061e25c" />
<img alt="image" src="https://github.com/user-attachments/assets/6f334782-ed50-40d6-9a78-43724dba0e85" />
<img alt="image" src="https://github.com/user-attachments/assets/c6d82899-9f05-4d56-9e5e-52f01aa58ef7" />


  


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
docker run -it --rm --name n8n -p 5888:5888 -v n8n_data:/home/node/.n8n docker.n8n.io/n8nio/n8n
```

Access the editor at http://localhost:5888

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

Found a bug 🐛 or have a feature idea ✨? Check our [Contributing Guide](https://github.com/n8n-io/n8n/blob/master/CONTRIBUTING.md) to get started.

## Join the Team

Want to shape the future of automation? Check out our [job posts](https://n8n.io/careers) and join our team!

## What does n8n mean?

**Short answer:** It means "nodemation" and is pronounced as n-eight-n.

**Long answer:** "I get that question quite often (more often than I expected) so I decided it is probably best to answer it here. While looking for a good name for the project with a free domain I realized very quickly that all the good ones I could think of were already taken. So, in the end, I chose nodemation. 'node-' in the sense that it uses a Node-View and that it uses Node.js and '-mation' for 'automation' which is what the project is supposed to help with. However, I did not like how long the name was and I could not imagine writing something that long every time in the CLI. That is when I then ended up on 'n8n'." - **Jan Oberhauser, Founder and CEO, n8n.io**

<img width="1038" height="1252" alt="image" src="https://github.com/user-attachments/assets/40399657-a371-4ed9-a232-4d100dccac5a" />


```

### File: packages\core\README.md
```md
![n8n.io - Workflow Automation](https://user-images.githubusercontent.com/65276001/173571060-9f2f6d7b-bac0-43b6-bdb2-001da9694058.png)

# n8n-core

Core components for n8n

```
npm install n8n-core
```

## License

You can find the license information [here](https://github.com/n8n-io/n8n/blob/master/README.md#license)

```

### File: packages\testing\playwright\README.md
```md
# Playwright E2E Test Guide

## Development setup
```bash
pnpm install-browsers:local # in playwright directory
pnpm build:docker # from root first to test against local changes
```

## Quick Start
```bash
pnpm test:all                 									# Run all tests (fresh containers, pnpm build:docker from root first to ensure local containers)
pnpm test:local           											# Starts a local server and runs the E2E tests
N8N_BASE_URL=localhost:5068 pnpm test:local			# Runs the E2E tests against the instance running
```

## Separate Backend and Frontend URLs

When developing with separate backend and frontend servers (e.g., backend on port 5680, frontend on port 8080), you can use the following environment variables:

- **`N8N_BASE_URL`**: Backend server URL (also used as frontend URL if `N8N_EDITOR_URL` is not set)
- **`N8N_EDITOR_URL`**: Frontend server URL (when set, overrides frontend URL while backend uses `N8N_BASE_URL`)

**How it works:**
- **Backend URL** (for API calls): Always uses `N8N_BASE_URL`
- **Frontend URL** (for browser navigation): Uses `N8N_EDITOR_URL` if set, otherwise falls back to `N8N_BASE_URL`

This allows you to:
- Test against a backend on port 5680 while the frontend dev server runs on port 8080
- Use different URLs for API calls vs browser navigation
- Maintain backward compatibility with single-URL setups

## Test Commands

```bash
# By Mode
pnpm test:container:sqlite      # SQLite (default)
pnpm test:container:postgres    # PostgreSQL
pnpm test:container:queue       # Queue mode
pnpm test:container:multi-main  # HA setup

pnpm test:performance						# Runs the performance tests against Sqlite container
pnpm test:chaos									# Runs the chaos tests


# Development
pnpm test:all --grep "workflow"           # Pattern match, can run across all test types E2E/cli-workflow/performance
pnpm test:local --ui            # To enable UI debugging and test running mode
```

## Test Tags
```typescript
test('basic test', ...)                              // All modes, fully parallel
test('postgres only @mode:postgres', ...)            // Mode-specific
test('needs clean db @db:reset', ...)                // Sequential per worker
test('chaos test @mode:multi-main @chaostest', ...) // Isolated per worker
test('cloud resource test @cloud:trial', ...)       // Cloud resource constraints
test('proxy test @capability:proxy', ...)           // Requires proxy server capability
```

## Fixture Selection
- **`base.ts`**: Standard testing with worker-scoped containers (default choice)
- **`cloud-only.ts`**: Cloud resource testing with guaranteed isolation
  - Use for performance testing under resource constraints
  - Requires `@cloud:*` tags (`@cloud:trial`, `@cloud:enterprise`, etc.)
  - Creates only cloud containers, no worker containers

```typescript
// Standard testing
import { test, expect } from '../fixtures/base';

// Cloud resource testing
import { test, expect } from '../fixtures/cloud-only';
test('Performance under constraints @cloud:trial', async ({ n8n, api }) => {
  // Test runs with 384MB RAM, 250 millicore CPU
});
```

## Tips
- `test:*` commands use fresh containers (for testing)
- VS Code: Set `N8N_BASE_URL` in Playwright settings to run tests directly from VS Code
- Pass custom env vars via `N8N_TEST_ENV='{"KEY":"value"}'`

## Project Layout
- **composables**: Multi-page interactions (e.g., `WorkflowComposer.executeWorkflowAndWaitForNotification()`)
- **config**: Test setup and configuration (constants, test users, etc.)
- **fixtures**: Custom test fixtures extending Playwright's base test
  - `base.ts`: Standard fixtures with worker-scoped containers
  - `cloud-only.ts`: Cloud resource testing with test-scoped containers only
- **pages**: Page Object Models for UI interactions
- **services**: API helpers for E2E controller, REST calls, workflow management, etc.
- **utils**: Utility functions (string manipulation, helpers, etc.)
- **workflows**: Test workflow JSON files for import/reuse

## Writing Tests with Proxy

You can use ProxyServer to mock API requests.

```typescript
import { test, expect } from '../fixtures/base';

// The `@capability:proxy` tag ensures tests only run when proxy infrastructure is available.
test.describe('Proxy tests @capability:proxy', () => {
  test('should mock HTTP requests', async ({ proxyServer, n8n }) => {
    // Create mock expectations
    await proxyServer.createGetExpectation('/api/data', { result: 'mocked' });

    // Execute workflow that makes HTTP requests
    await n8n.canvas.openNewWorkflow();
    // ... test implementation

    // Verify requests were proxied
    expect(await proxyServer.wasGetRequestMade('/api/data')).toBe(true);
  });
});
```

### Recording and replaying requests

The ProxyServer service supports recording HTTP requests for test mocking and replay. All proxied requests are automatically recorded by the mock server as described in the [Mock Server documentation](https://www.mock-server.com/proxy/record_and_replay.html).

#### Recording Expectations

```typescript
// Record all requests (the request is simplified/cleansed to method/path/body/query)
await proxyServer.recordExpectations('test-folder');

// Record with filtering and options
await proxyServer.recordExpectations('test-folder', {
  host: 'googleapis.com',           // Filter by host (partial match)
  dedupe: true,                     // Remove duplicate requests
  raw: false                        // Save cleaned requests (default)
});

// Record raw requests with all headers and metadata
await proxyServer.recordExpectations('test-folder', {
  raw: true                         // Save complete original requests
});

// Record requests matching specific criteria
await proxyServer.recordExpectations('test-folder', {
  pathOrRequestDefinition: {
    method: 'POST',
    path: '/api/workflows'
  }
});
```

#### Loading and Using Recorded Expectations

Recorded expectations are saved as JSON files in the `expectations/` directory. To use them in tests, you must explicitly load them:

```typescript
test('should use recorded expectations', async ({ proxyServer }) => {
  // Load expectations from a specific folder
  await proxyServer.loadExpectations('test-folder');

  // Your test code here - requests will be mocked using loaded expectations
});
```

#### Important: Cleanup Expectations

**Remember to clean up expectations before or after test runs:**

```typescript
test.beforeEach(async ({ proxyServer }) => {
  // Clear any existing expectations before test
  await proxyServer.clearAllExpectations();
});

test.afterEach(async ({ proxyServer }) => {
  // Or clear expectations after test
  await proxyServer.clearAllExpectations();
});
```

This prevents expectations from one test affecting others and ensures test isolation.

## Writing Tests
For guidelines on writing new tests, see [CONTRIBUTING.md](./CONTRIBUTING.md).

```

### File: packages\frontend\@n8n\i18n\README.md
```md
# @n8n/i18n

A package for managing internationalization (i18n) in n8n's Frontend codebase. It provides a structured way to handle translations and localization, ensuring that the application can be easily adapted to different languages and regions.

## Table of Contents

- [Features](#features)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Translation Management**: Simplifies the process of managing translations for different languages.
- **Localization Support**: Provides tools to adapt the application for different regions and cultures.
- **Easy Integration**: Seamlessly integrates with n8n's Frontend codebase, making it easy to implement and use.
- **Reusable Base Text**: Allows for the definition of reusable base text strings, reducing redundancy in translations.
- **Pluralization and Interpolation**: Supports pluralization and interpolation in base text strings, making it flexible for various use cases.
- **Versioned Nodes Support**: Facilitates the management of translations for nodes in versioned directories, ensuring consistency across different versions.
- **Documentation**: Comprehensive documentation to help developers understand and utilize the package effectively.

## Contributing

For more details, please read our [CONTRIBUTING.md](CONTRIBUTING.md).

## License

For more details, please read our [LICENSE.md](LICENSE.md).

```

### File: packages\frontend\@n8n\stores\README.md
```md
# @n8n/stores

A collection of Pinia stores that provide common data-related functionality across n8n's Front-End packages.

## Table of Contents

- [Features](#features)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Composable State Management**: Share and reuse stateful logic across multiple Vue components using Pinia stores.
- **Consistent Patterns**: Promote uniform state handling and best practices throughout the front-end codebase.
- **Easy Extensibility**: Add or modify stores as project requirements evolve, supporting scalable development.
- **Composition API Support**: Designed to work seamlessly with Vue's Composition API for modern, maintainable code.

## Contributing

For more details, please read our [CONTRIBUTING.md](CONTRIBUTING.md).

## License

For more details, please read our [LICENSE.md](LICENSE.md).

```

### File: packages\frontend\@n8n\i18n\docs\README.md
```md
# i18n in n8n

## Scope

n8n allows for internalization of the majority of UI text:

- base text, e.g. menu display items in the left-hand sidebar menu,
- node text, e.g. parameter display names and placeholders in the node view,
- credential text, e.g. parameter display names and placeholders in the credential modal,
- header text, e.g. node display names and descriptions at various spots.

Currently, n8n does _not_ allow for internalization of:

- messages from outside the `editor-ui` package, e.g. `No active database connection`,
- strings in certain Vue components, e.g. date time picker
- node subtitles, e.g. `create: user` or `getAll: post` below the node name on the canvas,
- new version notification contents in the updates panel, e.g. `Includes node enhancements`, and
- options that rely on `loadOptionsMethod`.

Pending functionality:

- Search in nodes panel by translated node name
- UI responsiveness to differently sized strings
- Locale-aware number formatting

## Locale identifiers

A **locale identifier** is a language code compatible with the [`Accept-Language` header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Accept-Language), e.g. `de` (German), `es` (Spanish), `ja` (Japanese). Regional variants of locale identifiers, such as `-AT` in `de-AT`, are _not_ supported. For a list of all locale identifiers, see [column 639-1 in this table](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes).

By default, n8n runs in the `en` (English) locale. To have run it in a different locale, set the `N8N_DEFAULT_LOCALE` environment variable to a locale identifier. When running in a non-`en` locale, n8n will display UI strings for the selected locale and fall back to `en` for any untranslated strings.

```
export N8N_DEFAULT_LOCALE=de
pnpm start
```

Output:

```
Initializing n8n process
n8n ready on 0.0.0.0, port 5678
Version: 0.156.0
Locale: de

Editor is now accessible via:
http://localhost:5678/

Press "o" to open in Browser.
```

## Base text

Base text is rendered with no dependencies, i.e. base text is fixed and does not change in any circumstances. Base text is supplied by the user in one file per locale in the `/frontend/@n8n/i18n` package.

### Locating base text

The base text file for each locale is located at `/packages/frontend/@n8n/i18n/src/locales/` and is named `{localeIdentifier}.json`. Keys in the base text file can be Vue component dirs, Vue component names, and references to symbols in those Vue components. These keys are added by the team as the UI is modified or expanded.

```json
{
	"nodeCreator.categoryNames.analytics": "🇩🇪 Analytics",
	"nodeCreator.categoryNames.communication": "🇩🇪 Communication",
	"nodeCreator.categoryNames.coreNodes": "🇩🇪 Core Nodes"
}
```

### Translating base text

1. Select a new locale identifier, e.g. `de`, copy the `en` JSON base text file with a new name:

```
cp ./packages/frontend/@n8n/i18n/src/locales/en.json ./packages/frontend/@n8n/i18n/src/locales/de.json
```

2. Find in the UI a string to translate, and search for it in the newly created base text file. Alternatively, find in `/frontend/editor-ui` a call to `i18n.baseText(key)`, e.g. `i18n.baseText('workflowActivator.deactivateWorkflow')`, and take note of the key and find it in the newly created base text file.

> **Note**: If you cannot find a string in the new base text file, either it does not belong to base text (i.e., the string might be part of header text, credential text, or node text), or the string might belong to the backend, where i18n is currently unsupported.

3. Translate the string value - do not change the key. In the examples below, a string starting with 🇩🇪 stands for a string translated from English into German.

As an optional final step, remove any untranslated strings from the new base text file. Untranslated strings in the new base text file will trigger a fallback to the `en` base text file.

> For information about **interpolation** and **reusable base text**, refer to the [Addendum](./ADDENDUM.md).

## Dynamic text

Dynamic text relies on data specific to each node and credential:

- `headerText` and `nodeText` in the **node translation file**
- `credText` in the **credential translation file**

### Locating dynamic text

#### Locating the credential translation file

A credential translation file is placed at `/nodes-base/credentials/translations/{localeIdentifier}`

```
credentials
	└── translations
		└── de
			├── githubApi.json
			└── githubOAuth2Api.json
```

Every credential must have its own credential translation file.

The name of the credential translation file must be sourced from the credential's `description.name` property:

```ts
export class GithubApi implements ICredentialType {
	name = 'githubApi'; // to use for credential translation file
	displayName = 'Github API';
	documentationUrl = 'github';
	properties: INodeProperties[] = [
```

#### Locating the node translation file

A node translation file is placed at `/nodes-base/nodes/{node}/translations/{localeIdentifier}`

```
GitHub
	├── GitHub.node.ts
	├── GitHubTrigger.node.ts
	└── translations
		└── de
			├── github.json
			└── githubTrigger.json
```

Every node must have its own node translation file.

> For information about nodes in **versioned dirs** and **grouping dirs**, refer to the [Addendum](./ADDENDUM.md).

The name of the node translation file must be sourced from the node's `description.name` property:

```ts
export class Github implements INodeType {
	description: INodeTypeDescription = {
		displayName: 'GitHub',
		name: 'github', // to use for node translation file name
		icon: 'file:github.svg',
		group: ['input'],
```

### Translating dynamic text

#### Translating the credential translation file

> **Note**: All translation keys are optional. Missing translation values trigger a fallback to the `en` locale strings.

A credential translation file, e.g. `githubApi.json` is an object containing keys that match the credential parameter names:

```ts
export class GithubApi implements ICredentialType {
	name = 'githubApi';
	displayName = 'Github API';
	documentationUrl = 'github';
	properties: INodeProperties[] = [
		{
			displayName: 'Github Server',
			name: 'server', // key to use in translation
			type: 'string',
			default: 'https://api.github.com',
			description: 'The server to connect to. Only has to be set if Github Enterprise is used.',
		},
		{
			displayName: 'User',
			name: 'user', // key to use in translation
			type: 'string',
			default: '',
		},
		{
			displayName: 'Access Token',
			name: 'accessToken', // key to use in translation
			type: 'string',
			default: '',
		},
	];
}
```

The object for each node credential parameter allows for the keys `displayName`, `description`, and `placeholder`.

```json
{
	"server.displayName": "🇩🇪 Github Server",
	"server.description": "🇩🇪 The server to connect to. Only has to be set if Github Enterprise is used.",
	"user.placeholder": "🇩🇪 Hans",
	"accessToken.placeholder": "🇩🇪 123"
}
```

<p align="center">
	<img src="img/cred.png">
</p>

Only existing parameters are translatable. If a credential parameter does not have a description in the English original, adding a translation for that non-existing parameter will not result in the translation being displayed - the parameter will need to be added in the English original first.

#### Translating the node translation file

> **Note**: All keys are optional. Missing translations trigger a fallback to the `en` locale strings.

Each node translation file is an object that allows for two keys, `header` and `nodeView`, which are the _sections_ of each node translation.

The `header` section points to an object that may contain only two keys, `displayName` and `description`, matching the node's `description.displayName` and `description.description`.

```ts
export class Github implements INodeType {
	description: INodeTypeDescription = {
		displayName: 'GitHub', // key to use in translation
		description: 'Consume GitHub API', // key to use in translation
		name: 'github',
		icon: 'file:github.svg',
		group: ['input'],
		version: 1,
```

```json
{
	"header": {
		"displayName": "🇩🇪 GitHub",
		"description": "🇩🇪 Consume GitHub API"
	}
}
```

Header text is used wherever the node's display name and description are needed:

<p align="center">
		<img src="img/header1.png" width="400">
		<img src="img/header2.png" width="200">
		<img src="img/header3.png" width="400">
</p>

<p align="center">
		<img src="img/header4.png" width="400">
		<img src="img/header5.png" width="500">
</p>

In turn, the `nodeView` section points to an object containing translation keys that match the node's operational parameters, found in the `*.node.ts` and also found in `*Description.ts` files in the same dir.

```ts
export class Github implements INodeType {
	description: INodeTypeDescription = {
		displayName: 'GitHub',
		name: 'github',
		properties: [
			{
				displayName: 'Resource',
				name: 'resource', // key to use in translation
				type: 'options',
				options: [],
				default: 'issue',
				description: 'The resource to operate on.',
			},
```

```json
{
	"nodeView.resource.displayName": "🇩🇪 Resource"
}
```

A node parameter allows for different translation keys depending on parameter type.

#### `string`, `number` and `boolean` parameters

Allowed keys: `displayName`, `description`, `placeholder`

```ts
{
	displayName: 'Repository Owner',
	name: 'owner', // key to use in translation
	type: 'string',
	required: true,
	placeholder: 'n8n-io',
	description: 'Owner of the repository.',
},
```

```json
{
	"nodeView.owner.displayName": "🇩🇪 Repository Owner",
	"nodeView.owner.placeholder": "🇩🇪 n8n-io",
	"nodeView.owner.description": "🇩🇪 Owner of the repository"
}
```

<p align="center">
	<img src="img/node1.png" width="400">
</p>

#### `options` parameter

Allowed keys: `displayName`, `description`, `placeholder`

Allowed subkeys: `options.{optionName}.displayName` and `options.{optionName}.description`.

```js
{
	displayName: 'Resource',
	name: 'resource',
	type: 'options',
	options: [
		{
			name: 'File',
			value: 'file', // key to use in translation
		},
		{
			name: 'Issue',
			value: 'issue', // key to use in translation
		},
	],
	default: 'issue',
	description: 'Resource to operate on',
},
```

```json
{
	"nodeView.resource.displayName": "🇩🇪 Resource",
	"nodeView.resource.description": "🇩🇪 Resource to operate on",
	"nodeView.resource.options.file.name": "🇩🇪 File",
	"nodeView.resource.options.issue.name": "🇩🇪 Issue"
}
```

<p align="center">
	<img src="img/node2.png" width="400">
</p>

For nodes whose credentials may be used in the HTTP Request node, an additional option `Custom API Call` is injected into the `Resource` and `Operation` parameters. Use the `__CUSTOM_API_CALL__` key to translate this additional option.

```json
{
	"nodeView.resource.options.file.name": "🇩🇪 File",
	"nodeView.resource.options.issue.name": "🇩🇪 Issue",
	"nodeView.resource.options.__CUSTOM_API_CALL__.name": "🇩🇪 Custom API Call"
}
```

#### `collection` and `fixedCollection` parameters

Allowed keys: `displayName`, `description`, `placeholder`, `multipleValueButtonText`

Example of `collection` parameter:

```js
{
	displayName: 'Labels',
	name: 'labels', // key to use in translation
	type: 'collection',
	typeOptions: {
		multipleValues: true,
		multipleValueButtonText: 'Add Label',
	},
	displayOptions: {
		show: {
			operation: [
				'create',
			],
			resource: [
				'issue',
			],
		},
	},
	default: { 'label': '' },
	options: [
		{
			displayName: 'Label',
			name: 'label', // key to use in translation
			type: 'string',
			default: '',
			description: 'Label to add to issue',
		},
	],
},
```

```json
{
	"nodeView.labels.displayName": "🇩🇪 Labels",
	"nodeView.labels.multipleValueButtonText": "🇩🇪 Add Label",
	"nodeView.labels.options.label.displayName": "🇩🇪 Label",
	"nodeView.labels.options.label.description": "🇩🇪 Label to add to issue",
	"nodeView.labels.options.label.placeholder": "🇩🇪 Some placeholder"
}
```

Example of `fixedCollection` parameter:

```js
{
	displayName: 'Additional Parameters',
	name: 'additionalParameters',
	placeholder: 'Add Parameter',
	description: 'Additional fields to add.',
	type: 'fixedCollection',
	default: {},
	displayOptions: {
		show: {
			operation: [
				'create',
				'delete',
				'edit',
			],
			resource: [
				'file',
			],
		},
	},
	options: [
		{
			name: 'author',
			displayName: 'Author',
			values: [
				{
					displayName: 'Name',
					name: 'name',
					type: 'string',
					default: '',
					description: 'Name of the author of the commit',
					placeholder: 'John',
				},
				{
					displayName: 'Email',
					name: 'email',
					type: 'string',
					default: '',
					description: 'Email of the author of the commit',
					placeholder: 'john@email.com',
				},
			],
		},
	],
}
```

```json
{
	"nodeView.additionalParameters.displayName": "🇩🇪 Additional Parameters",
	"nodeView.additionalParameters.placeholder": "🇩🇪 Add Field",
	"nodeView.additionalParameters.options.author.displayName": "🇩🇪 Author",
	"nodeView.additionalParameters.options.author.values.name.displayName": "🇩🇪 Name",
	"nodeView.additionalParameters.options.author.values.name.description": "🇩🇪 Name of the author of the commit",
	"nodeView.additionalParameters.options.author.values.name.placeholder": "🇩🇪 Jan",
	"nodeView.additionalParameters.options.author.values.email.displayName": "🇩🇪 Email",
	"nodeView.additionalParameters.options.author.values.email.description": "🇩🇪 Email of the author of the commit",
	"nodeView.additionalParameters.options.author.values.email.placeholder": "🇩🇪 jan@n8n.io"
}
```

<p align="center">
		<img src="img/node4.png" width="400">
</p>

> For information on **reusable dynamic text**, refer to the [Addendum](./ADDENDUM.md).

# Building translations

## Base text

When translating a base text file at `/packages/frontend/@n8n/i18n/src/locales/{localeIdentifier}.json`:

1. Open a terminal:

```sh
export N8N_DEFAULT_LOCALE=de
pnpm start
```

2. Open another terminal:

```sh
export N8N_DEFAULT_LOCALE=de
cd packages/frontend/editor-ui
pnpm dev
```

Changing the base text file will trigger a rebuild of the client at `http://localhost:8080`.

## Dynamic text

When translating a dynamic text file at `/packages/nodes-base/nodes/{node}/translations/{localeIdentifier}/{node}.json`,

1. Open a terminal:

```sh
export N8N_DEFAULT_LOCALE=de
pnpm start
```

2. Open another terminal:

```sh
export N8N_DEFAULT_LOCALE=de
cd packages/nodes-base
pnpm n8n-generate-translations
pnpm watch
```

After changing the dynamic text file:

1. Stop and restart the first terminal.
2. Refresh the browser at `http://localhost:5678`

If a `headerText` section was changed, re-run `pnpm n8n-generate-translations` in `/nodes-base`.

> **Note**: To translate base and dynamic text simultaneously, run three terminals following the steps from both sections (first terminal running only once) and browse `http://localhost:8080`.

```

### File: AGENTS.md
```md
# AGENTS.md

This file provides guidance on how to work with the n8n repository.

## Project Overview

n8n is a workflow automation platform written in TypeScript, using a monorepo
structure managed by pnpm workspaces. It consists of a Node.js backend, Vue.js
frontend, and extensible node-based workflow engine.

## General Guidelines

- Always use pnpm
- We use Linear as a ticket tracking system
- We use Posthog for feature flags
- When starting to work on a new ticket – create a new branch from fresh
  master with the name specified in Linear ticket
- When creating a new branch for a ticket in Linear - use the branch name
  suggested by linear
- Use mermaid diagrams in MD files when you need to visualise something

## Essential Commands

### Building
Use `pnpm build` to build all packages. ALWAYS redirect the output of the
build command to a file:

```bash
pnpm build > build.log 2>&1
```

You can inspect the last few lines of the build log file to check for errors:
```bash
tail -n 20 build.log
```

### Testing
- `pnpm test` - Run all tests
- `pnpm test:affected` - Runs tests based on what has changed since the last
  commit

Running a particular test file requires going to the directory of that test
and running: `pnpm test <test-file>`.

When changing directories, use `pushd` to navigate into the directory and
`popd` to return to the previous directory. When in doubt, use `pwd` to check
your current directory.

### Code Quality
- `pnpm lint` - Lint code
- `pnpm typecheck` - Run type checks

Always run lint and typecheck before committing code to ensure quality.
Execute these commands from within the specific package directory you're
working on (e.g., `cd packages/cli && pnpm lint`). Run the full repository
check only when preparing the final PR. When your changes affect type
definitions, interfaces in `@n8n/api-types`, or cross-package dependencies,
build the system before running lint and typecheck.

## Architecture Overview

**Monorepo Structure:** pnpm workspaces with Turbo build orchestration

### Package Structure

The monorepo is organized into these key packages:

- **`packages/@n8n/api-types`**: Shared TypeScript interfaces between frontend and backend
- **`packages/workflow`**: Core workflow interfaces and types
- **`packages/core`**: Workflow execution engine
- **`packages/cli`**: Express server, REST API, and CLI commands
- **`packages/editor-ui`**: Vue 3 frontend application
- **`packages/@n8n/i18n`**: Internationalization for UI text
- **`packages/nodes-base`**: Built-in nodes for integrations
- **`packages/@n8n/nodes-langchain`**: AI/LangChain nodes
- **`@n8n/design-system`**: Vue component library for UI consistency
- **`@n8n/config`**: Centralized configuration management

## Technology Stack

- **Frontend:** Vue 3 + TypeScript + Vite + Pinia + Storybook UI Library
- **Backend:** Node.js + TypeScript + Express + TypeORM
- **Testing:** Jest (unit) + Playwright (E2E)
- **Database:** TypeORM with SQLite/PostgreSQL/MySQL support
- **Code Quality:** Biome (for formatting) + ESLint + lefthook git hooks

### Key Architectural Patterns

1. **Dependency Injection**: Uses `@n8n/di` for IoC container
2. **Controller-Service-Repository**: Backend follows MVC-like pattern
3. **Event-Driven**: Internal event bus for decoupled communication
4. **Context-Based Execution**: Different contexts for different node types
5. **State Management**: Frontend uses Pinia stores
6. **Design System**: Reusable components and design tokens are centralized in
   `@n8n/design-system`, where all pure Vue components should be placed to
   ensure consistency and reusability

## Key Development Patterns

- Each package has isolated build configuration and can be developed independently
- Hot reload works across the full stack during development
- Node development uses dedicated `node-dev` CLI tool
- Workflow tests are JSON-based for integration testing
- AI features have dedicated development workflow (`pnpm dev:ai`)

### TypeScript Best Practices
- **NEVER use `any` type** - use proper types or `unknown`
- **Avoid type casting with `as`** - use type guards or type predicates instead
- **Define shared interfaces in `@n8n/api-types`** package for FE/BE communication

### Error Handling
- Don't use `ApplicationError` class in CLI and nodes for throwing errors,
  because it's deprecated. Use `UnexpectedError`, `OperationalError` or
  `UserError` instead.
- Import from appropriate error classes in each package

### Frontend Development
- **All UI text must use i18n** - add translations to `@n8n/i18n` package
- **Use CSS variables directly** - never hardcode spacing as px values
- **data-test-id must be a single value** (no spaces or multiple values)

When implementing CSS, refer to @packages/frontend/CLAUDE.md for guidelines on
CSS variables and styling conventions.

### Testing Guidelines
- **Always work from within the package directory** when running tests
- **Mock all external dependencies** in unit tests
- **Confirm test cases with user** before writing unit tests
- **Typecheck is critical before committing** - always run `pnpm typecheck`
- **When modifying pinia stores**, check for unused computed properties

What we use for testing and writing tests:
- For testing nodes and other backend components, we use Jest for unit tests. Examples can be found in `packages/nodes-base/nodes/**/*test*`.
- We use `nock` for server mocking
- For frontend we use `vitest`
- For E2E tests we use Playwright. Run with `pnpm --filter=n8n-playwright test:local`.
  See `packages/testing/playwright/README.md` for details.

### Common Development Tasks

When implementing features:
1. Define API types in `packages/@n8n/api-types`
2. Implement backend logic in `packages/cli` module, follow
   `@packages/cli/scripts/backend-module/backend-module-guide.md`
3. Add API endpoints via controllers
4. Update frontend in `packages/editor-ui` with i18n support
5. Write tests with proper mocks
6. Run `pnpm typecheck` to verify types

## Github Guidelines
- When creating a PR, use the conventions in
  `.github/pull_request_template.md` and
  `.github/pull_request_title_conventions.md`.
- Use `gh pr create --draft` to create draft PRs.
- Always reference the Linear ticket in the PR description,
  use `https://linear.app/n8n/issue/[TICKET-ID]`
- always link to the github issue if mentioned in the linear ticket.

```

### File: CLAUDE.md
```md
@AGENTS.md

```

### File: CODE_OF_CONDUCT.md
```md
# Contributor Covenant Code of Conduct

## Our Pledge

In the interest of fostering an open and welcoming environment, we as
contributors and maintainers pledge to making participation in our project and
our community a harassment-free experience for everyone, regardless of age, body
size, disability, ethnicity, sex characteristics, gender identity and expression,
level of experience, education, socio-economic status, nationality, personal
appearance, race, religion, or sexual identity and orientation.

## Our Standards

Examples of behavior that contributes to creating a positive environment
include:

- Using welcoming and inclusive language
- Being respectful of differing viewpoints and experiences
- Gracefully accepting constructive criticism
- Focusing on what is best for the community
- Showing empathy towards other community members

Examples of unacceptable behavior by participants include:

- The use of sexualized language or imagery and unwelcome sexual attention or
  advances
- Trolling, insulting/derogatory comments, and personal or political attacks
- Public or private harassment
- Publishing others' private information, such as a physical or electronic
  address, without explicit permission
- Other conduct which could reasonably be considered inappropriate in a
  professional setting

## Our Responsibilities

Project maintainers are responsible for clarifying the standards of acceptable
behavior and are expected to take appropriate and fair corrective action in
response to any instances of unacceptable behavior.

Project maintainers have the right and responsibility to remove, edit, or
reject comments, commits, code, wiki edits, issues, and other contributions
that are not aligned to this Code of Conduct, or to ban temporarily or
permanently any contributor for other behaviors that they deem inappropriate,
threatening, offensive, or harmful.

## Scope

This Code of Conduct applies both within project spaces and in public spaces
when an individual is representing the project or its community. Examples of
representing a project or community include using an official project e-mail
address, posting via an official social media account, or acting as an appointed
representative at an online or offline event. Representation of a project may be
further defined and clarified by project maintainers.

## Enforcement

Instances of abusive, harassing, or otherwise unacceptable behavior may be
reported by contacting the project team at jan@n8n.io. All
complaints will be reviewed and investigated and will result in a response that
is deemed necessary and appropriate to the circumstances. The project team is
obligated to maintain confidentiality with regard to the reporter of an incident.
Further details of specific enforcement policies may be posted separately.

Project maintainers who do not follow or enforce the Code of Conduct in good
faith may face temporary or permanent repercussions as determined by other
members of the project's leadership.

## Attribution

This Code of Conduct is adapted from the [Contributor Covenant][homepage], version 1.4,
available at https://www.contributor-covenant.org/version/1/4/code-of-conduct.html

[homepage]: https://www.contributor-covenant.org

For answers to common questions about this code of conduct, see
https://www.contributor-covenant.org/faq

```

### File: CONTRIBUTING.md
```md
# Contributing to n8n

Great that you are here and you want to contribute to n8n

## Contents

- [Contributing to n8n](#contributing-to-n8n)
	- [Contents](#contents)
	- [Code of conduct](#code-of-conduct)
	- [Directory structure](#directory-structure)
	- [Development setup](#development-setup)
		- [Dev Container](#dev-container)
		- [Requirements](#requirements)
			- [Node.js](#nodejs)
			- [pnpm](#pnpm)
				- [pnpm workspaces](#pnpm-workspaces)
			- [corepack](#corepack)
			- [Build tools](#build-tools)
		- [Actual n8n setup](#actual-n8n-setup)
		- [Start](#start)
	- [Development cycle](#development-cycle)
		- [Community PR Guidelines](#community-pr-guidelines)
			- [**1. Change Request/Comment**](#1-change-requestcomment)
			- [**2. General Requirements**](#2-general-requirements)
			- [**3. PR Specific Requirements**](#3-pr-specific-requirements)
			- [**4. Workflow Summary for Non-Compliant PRs**](#4-workflow-summary-for-non-compliant-prs)
		- [Test suite](#test-suite)
			- [Unit tests](#unit-tests)
			- [Code Coverage](#code-coverage)
			- [E2E tests](#e2e-tests)
	- [Releasing](#releasing)
	- [Create custom nodes](#create-custom-nodes)
	- [Extend documentation](#extend-documentation)
	- [Contribute workflow templates](#contribute-workflow-templates)
	- [Contributor License Agreement](#contributor-license-agreement)

## Code of conduct

This project and everyone participating in it are governed by the Code of
Conduct which can be found in the file [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).
By participating, you are expected to uphold this code. Please report
unacceptable behavior to jan@n8n.io.

## Directory structure

n8n is split up in different modules which are all in a single mono repository.

The most important directories:

- [/docker/images](/docker/images) - Dockerfiles to create n8n containers
- [/packages](/packages) - The different n8n modules
- [/packages/cli](/packages/cli) - CLI code to run front- & backend
- [/packages/core](/packages/core) - Core code which handles workflow
  execution, active webhooks and
  workflows. **Contact n8n before
  starting on any changes here**
- [/packages/frontend/@n8n/design-system](/packages/design-system) - Vue frontend components
- [/packages/frontend/editor-ui](/packages/editor-ui) - Vue frontend workflow editor
- [/packages/node-dev](/packages/node-dev) - CLI to create new n8n-nodes
- [/packages/nodes-base](/packages/nodes-base) - Base n8n nodes
- [/packages/workflow](/packages/workflow) - Workflow code with interfaces which
  get used by front- & backend

## Development setup

If you want to change or extend n8n you have to make sure that all the needed
dependencies are installed and the packages get linked correctly. Here's a short guide on how that can be done:

### Dev Container

If you already have VS Code and Docker installed, you can click [here](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/n8n-io/n8n) to get started. Clicking these links will cause VS Code to automatically install the Dev Containers extension if needed, clone the source code into a container volume, and spin up a dev container for use.

### Requirements

#### Node.js

[Node.js](https://nodejs.org/en/) version 22.16 or newer is required for development purposes.

#### pnpm

[pnpm](https://pnpm.io/) version 10.2 or newer is required for development purposes. We recommend installing it with [corepack](#corepack).

##### pnpm workspaces

n8n is split up into different modules which are all in a single mono repository.
To facilitate the module management, [pnpm workspaces](https://pnpm.io/workspaces) are used.
This automatically sets up file-links between modules which depend on each other.

#### corepack

We recommend enabling [Node.js corepack](https://nodejs.org/docs/latest-v16.x/api/corepack.html) with `corepack enable`.

You can install the correct version of pnpm using `corepack prepare --activate`.

**IMPORTANT**: If you have installed Node.js via homebrew, you'll need to run `brew install corepack`, since homebrew explicitly removes `npm` and `corepack` from [the `node` formula](https://github.com/Homebrew/homebrew-core/blob/master/Formula/node.rb#L66).

**IMPORTANT**: If you are on windows, you'd need to run `corepack enable` and `corepack prepare --activate` in a terminal as an administrator.

#### Build tools

The packages which n8n uses depend on a few build tools:

Debian/Ubuntu:

```
apt-get install -y build-essential python
```

CentOS:

```
yum install gcc gcc-c++ make
```

Windows:

```
npm add -g windows-build-tools
```

MacOS:

No additional packages required.

#### actionlint (for GitHub Actions workflow development)

If you plan to modify GitHub Actions workflow files (`.github/workflows/*.yml`), you'll need [actionlint](https://github.com/rhysd/actionlint) for workflow validation:

**macOS (Homebrew):**
```
brew install actionlint
```
> **Note:** actionlint is only required if you're modifying workflow files. It runs automatically via git hooks when workflow files are changed.

### Actual n8n setup

> **IMPORTANT**: All the steps below have to get executed at least once to get the development setup up and running!

Now that everything n8n requires to run is installed, the actual n8n code can be
checked out and set up:

1. [Fork](https://guides.github.com/activities/forking/#fork) the n8n repository.

2. Clone your forked repository:

   ```
   git clone https://github.com/<your_github_username>/n8n.git
   ```

3. Go into repository folder:

   ```
   cd n8n
   ```

4. Add the original n8n repository as `upstream` to your forked repository:

   ```
   git remote add upstream https://github.com/n8n-io/n8n.git
   ```

5. Install all dependencies of all modules and link them together:

   ```
   pnpm install
   ```

6. Build all the code:
   ```
   pnpm build
   ```

### Start

To start n8n execute:

```
pnpm start
```

## Development cycle

While iterating on n8n modules code, you can run `pnpm dev`. It will then
automatically build your code, restart the backend and refresh the frontend
(editor-ui) on every change you make.

### Basic Development Workflow

1. Start n8n in development mode:
   ```
   pnpm dev
   ```
2. Hack, hack, hack
3. Check if everything still runs in production mode:
   ```
   pnpm build
   pnpm start
   ```
4. Create tests
5. Run all [tests](#test-suite):
   ```
   pnpm test
   ```
6. Commit code and [create a pull request](https://docs.github.com/en/github/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork)

### Hot Reload for Nodes (N8N_DEV_RELOAD)

When developing custom nodes or credentials, you can enable hot reload to automatically detect changes without restarting the server:

```bash
N8N_DEV_RELOAD=true pnpm dev
```

**Performance considerations:**
- File watching adds overhead to your system, especially on slower machines
- The watcher monitors potentially thousands of files, which can impact CPU and memory usage
- On resource-constrained systems, consider developing without hot reload and manually restarting when needed

### Selective Package Development

Running all packages in development mode can be resource-intensive. For better performance, run only the packages relevant to your work:

#### Available Filtered Commands

- **Backend-only development:**
  ```bash
  pnpm dev:be
  ```
  Excludes frontend packages like editor-ui and design-system

- **Frontend-only development:**
  ```bash
  pnpm dev:fe
  ```
  Runs the backend server and editor-ui development server

- **AI/LangChain nodes development:**
  ```bash
  pnpm dev:ai
  ```
  Runs only essential packages for AI node development

#### Custom Selective Development

For even more focused development, you can run packages individually:

**Example 1: Working on custom nodes**
```bash
# Terminal 1: Build and watch nodes package
cd packages/nodes-base
pnpm dev

# Terminal 2: Run the CLI with hot reload
cd packages/cli
N8N_DEV_RELOAD=true pnpm dev
```

**Example 2: Pure frontend development**
```bash
# Terminal 1: Start the backend server (no watching)
pnpm start

# Terminal 2: Run frontend dev server
cd packages/editor-ui
pnpm dev
```

**Example 3: Working on a specific node package**
```bash
# Terminal 1: Watch your node package
cd packages/nodes-base  # or your custom node package
pnpm watch

# Terminal 2: Run CLI with hot reload
cd packages/cli
N8N_DEV_RELOAD=true pnpm dev
```

### Performance Considerations

The full development mode (`pnpm dev`) runs multiple processes in parallel:

1. **TypeScript compilation** for each package
2. **File watchers** monitoring source files
3. **Nodemon** restarting the backend on changes
4. **Vite dev server** for the frontend with HMR
5. **Multiple build processes** for various packages

**Performance impact:**
- Can consume significant CPU and memory resources
- File system watching creates overhead, especially on:
  - Networked file systems
  - Virtual machines with shared folders
  - Systems with slower I/O performance
- The more packages you run in dev mode, the more system resources are consumed

**Recommendations for resource-constrained environments:**
1. Use selective development commands based on your task
2. Close unnecessary applications to free up resources
3. Monitor system performance and adjust your development approach accordingly

---

### Community PR Guidelines

#### **1. Change Request/Comment**

Please address the requested changes or provide feedback within 14 days. If there is no response or updates to the pull request during this time, it will be automatically closed. The PR can be reopened once the requested changes are applied.

#### **2. General Requirements**

- **Follow the Style Guide:**
  - Ensure your code adheres to n8n's coding standards and conventions (e.g., formatting, naming, indentation). Use linting tools where applicable.
- **TypeScript Compliance:**
  - Do not use `ts-ignore` .
  - Ensure code adheres to TypeScript rules.
- **Avoid Repetitive Code:**
  - Reuse existing components, parameters, and logic wherever possible instead of redefining or duplicating them.
  - For nodes: Use the same parameter across multiple operations rather than defining a new parameter for each operation (if applicable).
- **Testing Requirements:**
  - PRs **must include tests**:
    - Unit tests
    - Workflow tests for nodes (example [here](https://github.com/n8n-io/n8n/tree/master/packages/nodes-base/nodes/Switch/V3/test))
    - UI tests (if applicable)
- **Typos:**
  - Use a spell-checking tool, such as [**Code Spell Checker**](https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.code-spell-checker), to avoid typos.

#### **3. PR Specific Requirements**

- **Small PRs Only:**
  - Focus on a single feature or fix per PR.
- **Naming Convention:**
  - Follow [n8n's PR Title Conventions](https://github.com/n8n-io/n8n/blob/master/.github/pull_request_title_conventions.md#L36).
- **New Nodes:**
  - PRs that introduce new nodes will be **auto-closed** unless they are explicitly requested by the n8n team and aligned with an agreed project scope. However, you can still explore [building your own nodes](https://docs.n8n.io/integrations/creating-nodes/overview/), as n8n offers the flexibility to create your own custom nodes.
- **Typo-Only PRs:**
  - Typos are not sufficient justification for a PR and will be rejected.

#### **4. Workflow Summary for Non-Compliant PRs**

- **No Tests:** If tests are not provided, the PR will be auto-closed after **14 days**.
- **Non-Small PRs:** Large or multifaceted PRs will be returned for segmentation.
- **New Nodes/Typo PRs:** Automatically rejected if not aligned with project scope or guidelines.

---

### Test suite

#### Unit tests

Unit tests can be started via:

```
pnpm test
```

If that gets executed in one of the package folders it will only run the tests
of this package. If it gets executed in the n8n-root folder it will run all
tests of all packages.

If you made a change which requires an update on a `.test.ts.snap` file, pass `-u` to the command to run tests or press `u` in watch mode.

#### Code Coverage
We track coverage for all our code on [Codecov](https://app.codecov.io/gh/n8n-io/n8n).
But when you are working on tests locally, we recommend running your tests with env variable `COVERAGE_ENABLED` set to `true`. You can then view the code coverage in the `coverage` folder, or you can use [this VSCode extension](https://marketplace.visualstudio.com/items?itemName=ryanluker.vscode-coverage-gutters) to visualize the coverage directly in VSCode.

#### E2E tests

n8n uses [Playwright](https://playwright.dev) for E2E testing.

E2E tests can be started via one of the following commands:

- `pnpm --filter=n8n-playwright test:local` - Run tests locally (starts local server on port 5680 and runs UI tests)
- `pnpm --filter=n8n-playwright test:local --ui` - Run tests in interactive UI mode (useful for debugging)
- `pnpm --filter=n8n-playwright test:local --grep="test-name"` - Run specific tests matching pattern

See `packages/testing/playwright/README.md` for more test commands and `packages/testing/playwright/CONTRIBUTING.md` for writing guidelines.

## Releasing

To start a release, trigger [this workflow](https://github.com/n8n-io/n8n/actions/workflows/release-create-pr.yml) with the SemVer release type, and select a branch to cut this release from. This workflow will then:

1. Bump versions of packages that have changed or have dependencies that have changed
2. Update the Changelog
3. Create a new branch called `release/${VERSION}`, and
4. Create a new pull-request to track any further changes that need to be included in this release

Once ready to release, simply merge the pull-request.
This triggers [another workflow](https://github.com/n8n-io/n8n/actions/workflows/release-publish.yml), that will:

1. Build and publish the packages that have a new version in this release
2. Create a new tag, and GitHub release from squashed release commit
3. Merge the squashed release commit back into `master`

## Create custom nodes

Learn about [building nodes](https://docs.n8n.io/integrations/creating-nodes/overview/) to create custom nodes for n8n. You can create community nodes and make them available using [npm](https://www.npmjs.com/).

## Extend documentation

The repository for the n8n documentation on [docs.n8n.io](https://docs.n8n.io) can be found [here](https://github.com/n8n-io/n8n-docs).

## Contribute workflow templates

You can submit your workflows to n8n's template library.

n8n is working on a creator program, and developing a marketplace of templates. This is an ongoing project, and details are likely to change.

Refer to [n8n Creator hub](https://www.notion.so/n8n/n8n-Creator-hub-7bd2cbe0fce0449198ecb23ff4a2f76f) for information on how to submit templates and become a creator.

## Contributor License Agreement

That we do not have a
... [TRUNCATED]
```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.

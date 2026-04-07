---
id: mcp-server-guide
type: knowledge
owner: OA_Triage
---
# mcp-server-guide
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
# Figma MCP Server Guide

The Figma MCP server brings Figma directly into your workflow by providing important design information and context to AI agents generating code from Figma design files.

> [!NOTE]
> Rate limits apply to Figma MCP server tools that read data from Figma. Some tools, such as those that write to Figma files, are exempt from the rate limits.
> <br><br>
> Users on the Starter plan or with View or Collab seats on paid plans will be limited to up to 6 tool calls per month.
> <br><br>
> Users with a [Dev or Full seat](https://help.figma.com/hc/en-us/articles/27468498501527-Updates-to-Figma-s-pricing-seats-and-billing-experience#h_01JCPBM8X2MBEXTABDM92HWZG4) on the [Professional, Organization, or Enterprise plans](https://help.figma.com/hc/en-us/articles/360040328273-Figma-plans-and-features) have per minute rate limits, which follow the same limits as the Tier 1 [Figma REST API](https://developers.figma.com/docs/rest-api/rate-limits/). As with Figma’s REST API, Figma reserves the right to change rate limits.

For the complete set of Figma MCP server docs, see our [developer documentation](https://developers.figma.com/docs/figma-mcp-server/). By using the Figma MCP server and the related resources (including these skills), you agree to the [Figma Developer Terms](https://www.figma.com/legal/developer-terms/). These skills are currently available as a Beta feature.

## Features

- **Write to the canvas** (remote server only): Create and modify native Figma content directly from your MCP client. With the right skills, agents can build and update frames, components, variables, and auto layout in your Figma files using your design system as the source of truth.

    **Note:** We're quickly improving how Figma supports AI agents. The write to canvas feature will eventually be a usage-based paid feature, but is currently available for free during the beta period.

- **Generate code from selected frames**

  Select a Figma frame and turn it into code. Great for product teams building new flows or iterating on app features.

- **Extract design context**

  Pull in variables, components, and layout data directly into your IDE. This is especially useful for design systems and component-based workflows.

- **Code smarter with Code Connect**

  Boost output quality by reusing your actual components. Code Connect keeps your generated code consistent with your codebase.

  [Learn more about Code Connect →](https://help.figma.com/hc/en-us/articles/23920389749655-Code-Connect)

- **Generate Figma designs from web pages** *(rolling out)*

  Capture, import, or convert a web page into a Figma design directly from your AI coding agent.

## Installation & Setup

### Connect to the Figma MCP server

Different MCP clients require slightly different setups. Follow the instructions below for your specific client to connect to the Figma MCP server.

#### VS Code

1. Use the shortcut `⌘ Shift P` to search for `MCP:Add Server`.
2. Select `HTTP`.
3. Paste the server url `https://mcp.figma.com/mcp` in the search bar. Then hit `Enter`.
4. When you're prompted for a server ID, enter `figma`.
5. Select whether you want to add this server globally or only for the current workspace. Once confirmed, you'll see a configuration like this in your `mcp.json` file:

```json
{
  "servers": {
    "figma": {
      "type": "http",
      "url": "https://mcp.figma.com/mcp"
    }
  }
}
```

6. Open the chat toolbar using `⌥⌘B` or `⌃⌘I` and switch to **Agent** mode.
7. With the chat open, type in `#get_design_context` to confirm that the Figma MCP server tools are available. If no tools are listed, restart VS Code.

> [!NOTE]
> You must have [GitHub Copilot](https://github.com/features/copilot) enabled on your account to use MCP in VS Code.
>
> For more information, see [VS Code's official documentation](https://code.visualstudio.com/docs/copilot/chat/mcp-servers).

#### Cursor

The recommended way to set up the Figma MCP server in Cursor is by installing the Figma Plugin, which includes MCP server settings as well as Agent Skills for common workflows.

Install the plugin by typing the following command in Cursor's agent chat:

```
/add-plugin figma
```

The plugin includes:

- MCP server configuration for the Figma MCP server
- Skills for implementing designs, connecting components via Code Connect, and creating design system rules
- Rules for proper asset handling from the Figma MCP server

<details>
<summary>Manual setup</summary>

1. Open **Cursor → Settings → Cursor Settings**.
2. Go to the **MCP** tab.
3. Click **+ Add new global MCP server**.
4. Enter the following configuration and save:

```json
{
  "mcpServers": {
    "figma": {
      "url": "https://mcp.figma.com/mcp"
    }
  }
}
```

For more information, see [Cursor's official documentation](https://docs.cursor.com/context/model-context-protocol).

</details>

#### Claude Code

The recommended way to set up the Figma MCP server in Claude Code is by installing the Figma Plugin, which includes MCP server settings as well as Agent Skills for common workflows.

Run the following command to install the plugin from Anthropic's official plugin marketplace.

```bash
claude plugin install figma@claude-plugins-official
```

Learn more about Anthropic's [Claude Code Plugins](https://claude.com/blog/claude-code-plugins) and [Agent Skills](https://claude.com/blog/skills).

<details>
<summary>Manual setup</summary>

1. Open your terminal and run:

```bash
claude mcp add --transport http figma https://mcp.figma.com/mcp
```

2. Use the following commands to check MCP settings and manage servers:

- List all configured servers
  ```bash
  claude mcp list
  ```
- Get details for a specific server
  ```bash
  claude mcp get my-server
  ```
- Remove a server
  ```bash
  claude mcp remove my-server
  ```

For more information, see [Anthropic's official documentation](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/tutorials#set-up-model-context-protocol-mcp).

</details>

#### Gemini CLI

Install the Figma extension for Gemini CLI by running the following command:

```bash
gemini extensions install https://github.com/figma/mcp-server-guide
```

Once installed, authenticate with Figma by running `gemini` and then executing the following command within the CLI:

```
/mcp auth figma
```

To uninstall the extension:

```bash
gemini extensions uninstall figma
```

#### Other editors

Other code editors and tools that support Streamable HTTP can also connect to the Figma MCP server.

If you're using a different editor or tool, check its documentation to confirm it supports Streamable HTTP based communication. If it does, you can manually add the Figma MCP server using this configuration:

```json
{
  "mcpServers": {
    "figma": {
      "url": "https://mcp.figma.com/mcp"
    }
  }
}
```

## Prompting your MCP client

The Figma MCP server introduces a set of tools that help LLMs translate designs in Figma. Once connected, you can prompt your MCP client to access a specific design node.

To provide Figma design context to your AI client:

1. Copy the link to a frame or layer in Figma.
2. Prompt your client to help you implement the design at the selected URL.

<img src="https://help.figma.com/hc/article_attachments/34049303807895" width="300" />

> [!NOTE]
> Your client won't be able to navigate to the selected URL, but it will extract the node-id that is required for the MCP server to identify which object to return information about.

## Tools and usage suggestions

### `get_design_context`

**Supported file types:** Figma Design, Figma Make

Use this to get design context for your Figma selection using the MCP server. The default output is **React + Tailwind**, but you can customize this through your prompts:

- Change the framework

  - "Generate my Figma selection in Vue."
  - "Generate my Figma selection in plain HTML + CSS."
  - "Generate my Figma selection in iOS."

- Use your components

  - "Generate my Figma selection using components from src/components/ui"
  - "Generate my Figma selection using components from src/ui and style with Tailwind"

  You can paste links to the frame or component in Figma before prompting.

[Learn how to set up Code Connect for better component reuse →](https://help.figma.com/hc/en-us/articles/23920389749655-Code-Connect)

### `generate_figma_design` (specific clients only, remote only)

**Supported file types:** Figma Design

Captures, imports, or converts a web page into a Figma design. You can send live UI interfaces as design layers to new or existing Figma files, or to your clipboard.

- "Start a local server for my app and capture the UI in a new Figma file"
- "Capture the login page to [Figma file URL]"

### `get_variable_defs`

**Supported file types:** Figma Design

Returns variables and styles used in your selection—like colors, spacing, and typography.

- List all tokens used
  - "Get the variables used in my Figma selection."
- Focus on a specific type
  - "What color and spacing variables are used in my Figma selection?"
- Get both names and values
  - "List the variable names and their values used in my Figma selection."

### `get_code_connect_map`

**Supported file types:** Figma Design

Retrieves a mapping between Figma node IDs and their corresponding code components in your codebase. Specifically, it returns an object where each key is a Figma node ID, and the value contains:

- `codeConnectSrc`: The location of the component in your codebase (e.g., a file path or URL).
- `codeConnectName`: The name of the component in your codebase.

This mapping is used to connect Figma design elements directly to their React (or other framework) implementations, enabling seamless design-to-code workflows and ensuring that the correct components are used for each part of the design. If a Figma node is connected to a code component, this function helps you identify and use the exact component in your project.

### `add_code_connect_map`

**Supported file types:** Figma Design

Creates mappings between Figma node IDs and corresponding code components in your codebase. This improves design-to-code workflow quality by linking specific design elements to their code implementations.

### `get_code_connect_suggestions`

**Supported file types:** Figma Design

Detects and suggests Code Connect mappings between Figma components and code components in your codebase. Works in conjunction with `send_code_connect_mappings` to confirm suggestions.

### `send_code_connect_mappings`

**Supported file types:** Figma Design

Confirms and finalizes Code Connect mappings after suggestions are reviewed through `get_code_connect_suggestions`.

### `get_screenshot`

**Supported file types:** Figma Design, FigJam

This takes a screenshot of your selection to preserve layout fidelity. Keep this on unless you're managing token limits.

### `create_design_system_rules`

**Supported file types:** No file context required

Use this tool to create a rule file that gives agents the context they need to generate high-quality front end code. Rule files help align output with your design system and tech stack, improving accuracy and ensuring code is tailored to your needs.

After running the tool, save the output to the appropriate `rules/` or `instructions/` directory so your agent can access it during code generation.

### `get_metadata`

**Supported file types:** Figma Design

Returns an XML representation of your selection containing basic properties such as layer IDs, names, types, position and sizes. You can use `get_design_context` on the resulting outline to retrieve only the styling information of the design you need.

This is useful for very large designs where `get_design_context` produces output with a large context size. It also works with multiple selections or the whole page if nothing is selected.

### `get_figjam`

**Supported file types:** FigJam

This tool returns metadata for FigJam diagrams in XML format, similar to `get_metadata`. In addition to returning basic properties like layer IDs, names, types, positions, and sizes, it also includes screenshots of the nodes.

### `generate_diagram`

**Supported file types:** No file context required

Generates FigJam diagrams from Mermaid syntax. The agent can generate diagrams from natural language descriptions without requiring you to write Mermaid syntax. Supports flowcharts, Gantt charts, state diagrams, and sequence diagrams.

- "Create a flowchart for the user authentication flow using the Figma MCP generate_diagram tool"
- "Generate a sequence diagram for the payment processing system"

### `whoami` (remote only)

**Supported file types:** No file context required

This tool returns the identity of the user that's authenticated to Figma, including:

- The user's email address
- All of the plans the user belongs to
- The seat type the user has on each plan

### `use_figma` (remote only)

**Note:** We're quickly improving how Figma supports AI agents. This will eventually be a usage-based paid feature, but is currently available for free during the beta period.

**Supported file types:** Figma Design, FigJam

The general-purpose tool for writing to Figma. Use it to create, edit, delete, or inspect any object in a Figma file: pages, frames, components, variants, variables, styles, text, images, and more.

When relevant, the agent will first check your design system for existing components to reuse before creating anything from scratch.

The `use_figma` tool is best invoked with the `figma-use` skill.

**You can ask it to:**

- **Create or modify designs**
  - `add a new frame to my Figma file`
  - `update the button component to use the correct fill color`
- **Set up design tokens, variables, or styles**
  - `create a color variable collection from my design tokens`
  - `set up spacing tokens in my Figma file`
- **Build or update component and variant systems**
  - `generate variants for the card component`
  - `sync my Figma components with my latest code changes`
- **Fix layout or visual issues**
  - `fix the auto-layout spacing on the nav component`
  - `update the typography styles to match the design spec`

### `search_design_system`

**Supported file types:** Figma Design

Searches across all connected design libraries to find components, variables, and styles matching a text query. Returns matching assets so the agent can reuse existing design system elements rather than creating new ones from scratch.

**You can ask it to:**

- **Find components**
  - `search for a button component in my design system`
  - `find a card component I can use for this layout`
- **Look up tokens**
  - `search for the primary color variable in my design system`
  - `find spacing tokens in my design libraries`
- **Narrow by type**
  - `search for icon styles in my design system`

### `create_new_file`

**Supported file types:** No file context required

Creates a new blank Figma Design or FigJam file in your drafts folder. If you be
... [TRUNCATED]
```

### File: .mcp.json
```json
{
  "mcpServers": {
    "figma": {
      "type": "http",
      "url": "https://mcp.figma.com/mcp"
    }
  }
}

```

### File: gemini-extension.json
```json
{
  "name": "Figma",
  "version": "2.0.7",
  "description": "Integrate Figma into your workflow: Generate code from frames, extract design context, retrieve resources, and ensure design system consistency with your codebase",
  "mcpServers": {
    "figma": {
      "httpUrl": "https://mcp.figma.com/mcp",
      "oauth": {
        "enabled": true
      }
    }
  }
}

```

### File: server.json
```json
{
  "$schema": "https://static.modelcontextprotocol.io/schemas/2025-09-29/server.schema.json",
  "name": "com.figma.mcp/mcp",
  "title": "Figma MCP Server",
  "description": "The Figma MCP server brings Figma design context directly into your AI workflow.",
  "repository": {
    "url": "https://github.com/figma/mcp-server-guide",
    "source": "github"
  },
  "version": "2.0.7",
  "remotes": [
    {
      "type": "streamable-http",
      "url": "https://mcp.figma.com/mcp"
    }
  ]
}

```

### File: .claude-plugin\plugin.json
```json
{
  "name": "figma",
  "description": "Plugin that includes the Figma MCP server and Skills for common workflows",
  "version": "2.0.7",
  "author": {
    "name": "Figma"
  }
}

```

### File: .cursor-plugin\plugin.json
```json
{
  "name": "figma",
  "displayName": "Figma",
  "version": "2.0.7",
  "description": "Plugin that includes the Figma MCP server and Skills for common workflows",
  "author": {
    "name": "Figma"
  },
  "logo": "./Figma Icon (Full-color).svg",
  "homepage": "https://github.com/figma/mcp-server-guide",
  "repository": "https://github.com/figma/mcp-server-guide",
  "keywords": ["figma", "design", "mcp", "ui", "code-connect"],
  "skills": "./skills/",
  "mcpServers": "./.mcp.json"
}

```

### File: .github\plugin\plugin.json
```json
{
  "name": "figma",
  "description": "Plugin that includes the Figma MCP server and Skills for common workflows.",
  "version": "2.0.7",
  "author": {
    "name": "Figma",
    "url": "https://www.figma.com"
  },
  "homepage": "https://github.com/figma/mcp-server-guide",
  "keywords": ["figma", "design", "mcp", "ui", "code-connect"]
}

```


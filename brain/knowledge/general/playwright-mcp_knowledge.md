---
id: playwright-mcp-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:31:00.183377
---

# KNOWLEDGE EXTRACT: playwright-mcp
> **Extracted on:** 2026-03-30 13:17:24
> **Source:** playwright-mcp

---

## File: `.gitignore`
```
node_modules/
test-results/
playwright-report/
.vscode/mcp.json
.idea
.DS_Store
.env
sessions/
```

## File: `CLAUDE.md`
```markdown
## Commit Convention

Semantic commit messages: `label(scope): description`

Labels: `fix`, `feat`, `chore`, `docs`, `test`, `devops`

```bash
git checkout -b fix-39562
# ... make changes ...
git add <changed-files>
git commit -m "$(cat <<'EOF'
fix(proxy): handle SOCKS proxy authentication

Fixes: https://github.com/microsoft/playwright/issues/39562
EOF
)"
git push origin fix-39562
gh pr create --repo microsoft/playwright --head username:fix-39562 \
  --title "fix(proxy): handle SOCKS proxy authentication" \
  --body "$(cat <<'EOF'
## Summary
- <describe the change very! briefly>

Fixes https://github.com/microsoft/playwright/issues/39562
EOF
)"
```

Never add Co-Authored-By agents in commit message.
Branch naming for issue fixes: `fix-<issue-number>`

```

## File: `CONTRIBUTING.md`
```markdown
# Contributing

## Choose an issue

Playwright MCP **requires an issue** for every contribution, except for minor documentation updates.

If you are passionate about a bug/feature, but cannot find an issue describing it, **file an issue first**. This will
facilitate the discussion, and you might get some early feedback from project maintainers before spending your time on
creating a pull request.

## Make a change

> [!WARNING]
> The core of the Playwright MCP was moved to the [Playwright monorepo](https://github.com/microsoft/playwright).

Clone the Playwright repository. If you plan to send a pull request, it might be better to [fork the repository](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo) first.


```bash
git clone https://github.com/microsoft/playwright
cd playwright
```

Install dependencies and run the build in watch mode.
```bash
# install deps and run watch
npm ci
npm run watch
npx playwright install
```

Source code for Playwright MCP is located at [packages/playwright/src/mcp](https://github.com/microsoft/playwright/blob/main/packages/playwright/src/mcp).

```bash
# list source files
ls -la packages/playwright/src/mcp
```

Coding style is fully defined in [eslint.config.mjs](https://github.com/microsoft/playwright/blob/main/eslint.config.mjs). Before creating a pull request, or at any moment during development, run linter to check all kinds of things:
```bash
# lint the source base before sending PR
npm run flint
```

Comments should have an explicit purpose and should improve readability rather than hinder it. If the code would not be understood without comments, consider re-writing the code to make it self-explanatory.

## Add a test

Playwright requires a test for the new or modified functionality. An exception would be a pure refactoring, but chances are you are doing more than that.

There are multiple [test suites](https://github.com/microsoft/playwright/blob/main/tests) in Playwright that will be executed on the CI. Tests for Playwright MCP are located at [tests/mcp](https://github.com/microsoft/playwright/blob/main/tests/mcp).

```bash
# list test files
ls -la tests/mcp
```

To run the mcp tests, use

```bash
# fast path runs all MCP tests in Chromium
npm run mcp-ctest
```

```bash
# slow path runs all tests in three browsers
npm run mcp-test
```

Since Playwright tests are using Playwright under the hood, everything from our documentation applies, for example [this guide on running and debugging tests](https://playwright.dev/docs/running-tests#running-tests).

Note that tests should be *hermetic*, and not depend on external services. Tests should work on all three platforms: macOS, Linux and Windows.

## Write a commit message

Commit messages should follow the [Semantic Commit Messages](https://www.conventionalcommits.org/en/v1.0.0/) format:

```
label(namespace): title

description

footer
```

1. *label* is one of the following:
    - `fix` - bug fixes
    - `feat` - new features
    - `docs` - documentation-only changes
    - `test` - test-only changes
    - `devops` - changes to the CI or build
    - `chore` - everything that doesn't fall under previous categories
2. *namespace* is put in parentheses after label and is optional. Must be lowercase.
3. *title* is a brief summary of changes.
4. *description* is **optional**, new-line separated from title and is in present tense.
5. *footer* is **optional**, new-line separated from *description* and contains "fixes" / "references" attribution to GitHub issues.

Example:

```
feat(trace viewer): network panel filtering

This patch adds a filtering toolbar to the network panel.
<link to a screenshot>

Fixes #123, references #234.
```

## Send a pull request

All submissions, including submissions by project members, require review. We use GitHub pull requests for this purpose.
Make sure to keep your PR (diff) small and readable. If necessary, split your contribution into multiple PRs.
Consult [GitHub Help](https://help.github.com/articles/about-pull-requests/) for more information on using pull requests.

After a successful code review, one of the maintainers will merge your pull request. Congratulations!

## More details

**No new dependencies**

There is a very high bar for new dependencies, including updating to a new version of an existing dependency. We recommend to explicitly discuss this in an issue and get a green light from a maintainer, before creating a pull request that updates dependencies.

## Contributor License Agreement

This project welcomes contributions and suggestions.  Most contributions require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us
the rights to use your contribution. For details, visit https://cla.opensource.microsoft.com.

When you submit a pull request, a CLA bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., status check, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repos using our CLA.

### Code of Conduct

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.
```

## File: `Dockerfile`
```
ARG PLAYWRIGHT_BROWSERS_PATH=/ms-playwright

# ------------------------------
# Base
# ------------------------------
# Base stage: Contains only the minimal dependencies required for runtime
# (node_modules and Playwright system dependencies)
FROM node:22-bookworm-slim AS base

ARG PLAYWRIGHT_BROWSERS_PATH
ENV PLAYWRIGHT_BROWSERS_PATH=${PLAYWRIGHT_BROWSERS_PATH}

# Set the working directory
WORKDIR /app

RUN --mount=type=cache,target=/root/.npm,sharing=locked,id=npm-cache \
    --mount=type=bind,source=package.json,target=package.json \
    --mount=type=bind,source=package-lock.json,target=package-lock.json \
    --mount=type=bind,source=packages/playwright-mcp/package.json,target=packages/playwright-mcp/package.json \
  npm ci --omit=dev && \
  # Install system dependencies for playwright
  npx -y playwright-core install-deps chromium

# ------------------------------
# Builder
# ------------------------------
FROM base AS builder

RUN --mount=type=cache,target=/root/.npm,sharing=locked,id=npm-cache \
    --mount=type=bind,source=package.json,target=package.json \
    --mount=type=bind,source=package-lock.json,target=package-lock.json \
    --mount=type=bind,source=packages/playwright-mcp/package.json,target=packages/playwright-mcp/package.json \
  npm ci

# Copy the rest of the app
COPY packages/playwright-mcp/*.json packages/playwright-mcp/*.js packages/playwright-mcp/*.ts .

# ------------------------------
# Browser
# ------------------------------
# Cache optimization:
# - Browser is downloaded only when node_modules or Playwright system dependencies change
# - Cache is reused when only source code changes
FROM base AS browser

RUN npx -y playwright-core install --no-shell chromium

# ------------------------------
# Runtime
# ------------------------------
FROM base

ARG PLAYWRIGHT_BROWSERS_PATH
ARG USERNAME=node
ENV NODE_ENV=production
ENV PLAYWRIGHT_MCP_OUTPUT_DIR=/tmp/playwright-output

# Set the correct ownership for the runtime user on production `node_modules`
RUN chown -R ${USERNAME}:${USERNAME} node_modules

USER ${USERNAME}

COPY --from=browser --chown=${USERNAME}:${USERNAME} ${PLAYWRIGHT_BROWSERS_PATH} ${PLAYWRIGHT_BROWSERS_PATH}
COPY --chown=${USERNAME}:${USERNAME} packages/playwright-mcp/cli.js packages/playwright-mcp/package.json ./

# Run in headless and only with chromium (other browsers need more dependencies not included in this image)
ENTRYPOINT ["node", "cli.js", "--headless", "--browser", "chromium", "--no-sandbox"]
```

## File: `LICENSE`
```
                                 Apache License
                           Version 2.0, January 2004
                        http://www.apache.org/licenses/

   TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

   1. Definitions.

      "License" shall mean the terms and conditions for use, reproduction,
      and distribution as defined by Sections 1 through 9 of this document.

      "Licensor" shall mean the copyright owner or entity authorized by
      the copyright owner that is granting the License.

      "Legal Entity" shall mean the union of the acting entity and all
      other entities that control, are controlled by, or are under common
      control with that entity. For the purposes of this definition,
      "control" means (i) the power, direct or indirect, to cause the
      direction or management of such entity, whether by contract or
      otherwise, or (ii) ownership of fifty percent (50%) or more of the
      outstanding shares, or (iii) beneficial ownership of such entity.

      "You" (or "Your") shall mean an individual or Legal Entity
      exercising permissions granted by this License.

      "Source" form shall mean the preferred form for making modifications,
      including but not limited to software source code, documentation
      source, and configuration files.

      "Object" form shall mean any form resulting from mechanical
      transformation or translation of a Source form, including but
      not limited to compiled object code, generated documentation,
      and conversions to other media types.

      "Work" shall mean the work of authorship, whether in Source or
      Object form, made available under the License, as indicated by a
      copyright notice that is included in or attached to the work
      (an example is provided in the Appendix below).

      "Derivative Works" shall mean any work, whether in Source or Object
      form, that is based on (or derived from) the Work and for which the
      editorial revisions, annotations, elaborations, or other modifications
      represent, as a whole, an original work of authorship. For the purposes
      of this License, Derivative Works shall not include works that remain
      separable from, or merely link (or bind by name) to the interfaces of,
      the Work and Derivative Works thereof.

      "Contribution" shall mean any work of authorship, including
      the original version of the Work and any modifications or additions
      to that Work or Derivative Works thereof, that is intentionally
      submitted to Licensor for inclusion in the Work by the copyright owner
      or by an individual or Legal Entity authorized to submit on behalf of
      the copyright owner. For the purposes of this definition, "submitted"
      means any form of electronic, verbal, or written communication sent
      to the Licensor or its representatives, including but not limited to
      communication on electronic mailing lists, source code control systems,
      and issue tracking systems that are managed by, or on behalf of, the
      Licensor for the purpose of discussing and improving the Work, but
      excluding communication that is conspicuously marked or otherwise
      designated in writing by the copyright owner as "Not a Contribution."

      "Contributor" shall mean Licensor and any individual or Legal Entity
      on behalf of whom a Contribution has been received by Licensor and
      subsequently incorporated within the Work.

   2. Grant of Copyright License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      copyright license to reproduce, prepare Derivative Works of,
      publicly display, publicly perform, sublicense, and distribute the
      Work and such Derivative Works in Source or Object form.

   3. Grant of Patent License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      (except as stated in this section) patent license to make, have made,
      use, offer to sell, sell, import, and otherwise transfer the Work,
      where such license applies only to those patent claims licensable
      by such Contributor that are necessarily infringed by their
      Contribution(s) alone or by combination of their Contribution(s)
      with the Work to which such Contribution(s) was submitted. If You
      institute patent litigation against any entity (including a
      cross-claim or counterclaim in a lawsuit) alleging that the Work
      or a Contribution incorporated within the Work constitutes direct
      or contributory patent infringement, then any patent licenses
      granted to You under this License for that Work shall terminate
      as of the date such litigation is filed.

   4. Redistribution. You may reproduce and distribute copies of the
      Work or Derivative Works thereof in any medium, with or without
      modifications, and in Source or Object form, provided that You
      meet the following conditions:

      (a) You must give any other recipients of the Work or
          Derivative Works a copy of this License; and

      (b) You must cause any modified files to carry prominent notices
          stating that You changed the files; and

      (c) You must retain, in the Source form of any Derivative Works
          that You distribute, all copyright, patent, trademark, and
          attribution notices from the Source form of the Work,
          excluding those notices that do not pertain to any part of
          the Derivative Works; and

      (d) If the Work includes a "NOTICE" text file as part of its
          distribution, then any Derivative Works that You distribute must
          include a readable copy of the attribution notices contained
          within such NOTICE file, excluding those notices that do not
          pertain to any part of the Derivative Works, in at least one
          of the following places: within a NOTICE text file distributed
          as part of the Derivative Works; within the Source form or
          documentation, if provided along with the Derivative Works; or,
          within a display generated by the Derivative Works, if and
          wherever such third-party notices normally appear. The contents
          of the NOTICE file are for informational purposes only and
          do not modify the License. You may add Your own attribution
          notices within Derivative Works that You distribute, alongside
          or as an addendum to the NOTICE text from the Work, provided
          that such additional attribution notices cannot be construed
          as modifying the License.

      You may add Your own copyright statement to Your modifications and
      may provide additional or different license terms and conditions
      for use, reproduction, or distribution of Your modifications, or
      for any such Derivative Works as a whole, provided Your use,
      reproduction, and distribution of the Work otherwise complies with
      the conditions stated in this License.

   5. Submission of Contributions. Unless You explicitly state otherwise,
      any Contribution intentionally submitted for inclusion in the Work
      by You to the Licensor shall be under the terms and conditions of
      this License, without any additional terms or conditions.
      Notwithstanding the above, nothing herein shall supersede or modify
      the terms of any separate license agreement you may have executed
      with Licensor regarding such Contributions.

   6. Trademarks. This License does not grant permission to use the trade
      names, trademarks, service marks, or product names of the Licensor,
      except as required for reasonable and customary use in describing the
      origin of the Work and reproducing the content of the NOTICE file.

   7. Disclaimer of Warranty. Unless required by applicable law or
      agreed to in writing, Licensor provides the Work (and each
      Contributor provides its Contributions) on an "AS IS" BASIS,
      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
      implied, including, without limitation, any warranties or conditions
      of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
      PARTICULAR PURPOSE. You are solely responsible for determining the
      appropriateness of using or redistributing the Work and assume any
      risks associated with Your exercise of permissions under this License.

   8. Limitation of Liability. In no event and under no legal theory,
      whether in tort (including negligence), contract, or otherwise,
      unless required by applicable law (such as deliberate and grossly
      negligent acts) or agreed to in writing, shall any Contributor be
      liable to You for damages, including any direct, indirect, special,
      incidental, or consequential damages of any character arising as a
      result of this License or out of the use or inability to use the
      Work (including but not limited to damages for loss of goodwill,
      work stoppage, computer failure or malfunction, or any and all
      other commercial damages or losses), even if such Contributor
      has been advised of the possibility of such damages.

   9. Accepting Warranty or Additional Liability. While redistributing
      the Work or Derivative Works thereof, You may choose to offer,
      and charge a fee for, acceptance of support, warranty, indemnity,
      or other liability obligations and/or rights consistent with this
      License. However, in accepting such obligations, You may act only
      on Your own behalf and on Your sole responsibility, not on behalf
      of any other Contributor, and only if You agree to indemnify,
      defend, and hold each Contributor harmless for any liability
      incurred by, or claims asserted against, such Contributor by reason
      of your accepting any such warranty or additional liability.

   END OF TERMS AND CONDITIONS

   APPENDIX: How to apply the Apache License to your work.

      To apply the Apache License to your work, attach the following
      boilerplate notice, with the fields enclosed by brackets "[]"
      replaced with your own identifying information. (Don't include
      the brackets!)  The text should be enclosed in the appropriate
      comment syntax for the file format. We also recommend that a
      file or class name and description of purpose be included on the
      same "printed page" as the copyright notice for easier
      identification within third-party archives.

   Copyright (c) Microsoft Corporation.

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
```

## File: `package.json`
```json
{
  "name": "playwright-mcp-internal",
  "version": "0.0.68",
  "private": true,
  "repository": {
    "type": "git",
    "url": "git+https://github.com/microsoft/playwright-mcp.git"
  },
  "homepage": "https://playwright.dev",
  "author": {
    "name": "Microsoft Corporation"
  },
  "license": "Apache-2.0",
  "scripts": {
    "docker-build": "docker build --no-cache -t playwright-mcp-dev:latest .",
    "docker-rm": "docker rm playwright-mcp-dev",
    "docker-run": "docker run -it -p 8080:8080 --name playwright-mcp-dev playwright-mcp-dev:latest",
    "lint": "npm run lint --workspaces",
    "test": "npm run test --workspaces",
    "build": "npm run build --workspaces",
    "bump": "npm version --workspaces --no-git-tag-version",
    "roll": "node roll.js"
  },
  "workspaces": [
    "packages/*"
  ],
  "devDependencies": {
    "@modelcontextprotocol/sdk": "^1.25.2",
    "@playwright/test": "1.59.0-alpha-1773608981000",
    "@types/node": "^24.3.0"
  }
}
```

## File: `README.md`
```markdown
## Playwright MCP

A Model Context Protocol (MCP) server that provides browser automation capabilities using [Playwright](https://playwright.dev). This server enables LLMs to interact with web pages through structured accessibility snapshots, bypassing the need for screenshots or visually-tuned models.

### Playwright MCP vs Playwright CLI

This package provides MCP interface into Playwright. If you are using a **coding agent**, you might benefit from using the [CLI+SKILLS](https://github.com/microsoft/playwright-cli) instead.

- **CLI**: Modern **coding agents** increasingly favor CLI–based workflows exposed as SKILLs over MCP because CLI invocations are more token-efficient: they avoid loading large tool schemas and verbose accessibility trees into the model context, allowing agents to act through concise, purpose-built commands. This makes CLI + SKILLs better suited for high-throughput coding agents that must balance browser automation with large codebases, tests, and reasoning within limited context windows.<br>**Learn more about [Playwright CLI with SKILLS](https://github.com/microsoft/playwright-cli)**.

- **MCP**: MCP remains relevant for specialized agentic loops that benefit from persistent state, rich introspection, and iterative reasoning over page structure, such as exploratory automation, self-healing tests, or long-running autonomous workflows where maintaining continuous browser context outweighs token cost concerns.

### Key Features

- **Fast and lightweight**. Uses Playwright's accessibility tree, not pixel-based input.
- **LLM-friendly**. No vision models needed, operates purely on structured data.
- **Deterministic tool application**. Avoids ambiguity common with screenshot-based approaches.

### Requirements
- Node.js 18 or newer
- VS Code, Cursor, Windsurf, Claude Desktop, Goose or any other MCP client

<!--
// Generate using:
node utils/generate-links.js
-->

### Getting started

First, install the Playwright MCP server with your client.

**Standard config** works in most of the tools:

```js
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": [
        "@playwright/mcp@latest"
      ]
    }
  }
}
```

[<img src="https://img.shields.io/badge/VS_Code-VS_Code?style=flat-square&label=Install%20Server&color=0098FF" alt="Install in VS Code">](https://insiders.vscode.dev/redirect?url=vscode%3Amcp%2Finstall%3F%257B%2522name%2522%253A%2522playwright%2522%252C%2522command%2522%253A%2522npx%2522%252C%2522args%2522%253A%255B%2522%2540playwright%252Fmcp%2540latest%2522%255D%257D) [<img alt="Install in VS Code Insiders" src="https://img.shields.io/badge/VS_Code_Insiders-VS_Code_Insiders?style=flat-square&label=Install%20Server&color=24bfa5">](https://insiders.vscode.dev/redirect?url=vscode-insiders%3Amcp%2Finstall%3F%257B%2522name%2522%253A%2522playwright%2522%252C%2522command%2522%253A%2522npx%2522%252C%2522args%2522%253A%255B%2522%2540playwright%252Fmcp%2540latest%2522%255D%257D)

<details>
<summary>Amp</summary>

Add via the Amp VS Code extension settings screen or by updating your settings.json file:

```json
"amp.mcpServers": {
  "playwright": {
    "command": "npx",
    "args": [
      "@playwright/mcp@latest"
    ]
  }
}
```

**Amp CLI Setup:**

Add via the `amp mcp add`command below

```bash
amp mcp add playwright -- npx @playwright/mcp@latest
```

</details>

<details>
<summary>Antigravity</summary>

Add via the Antigravity settings or by updating your configuration file:

```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": [
        "@playwright/mcp@latest"
      ]
    }
  }
}
```

</details>

<details>
<summary>Claude Code</summary>

Use the Claude Code CLI to add the Playwright MCP server:

```bash
claude mcp add playwright npx @playwright/mcp@latest
```
</details>

<details>
<summary>Claude Desktop</summary>

Follow the MCP install [guide](https://modelcontextprotocol.io/quickstart/user), use the standard config above.

</details>

<details>
<summary>Cline</summary>

Follow the instruction in the section [Configuring MCP Servers](https://docs.cline.bot/mcp/configuring-mcp-servers)

**Example: Local Setup**

Add the following to your [`cline_mcp_settings.json`](https://docs.cline.bot/mcp/configuring-mcp-servers#editing-mcp-settings-files) file:

```json
{
  "mcpServers": {
    "playwright": {
      "type": "stdio",
      "command": "npx",
      "timeout": 30,
      "args": [
        "-y",
        "@playwright/mcp@latest"
      ],
      "disabled": false
    }
  }
}
```

</details>

<details>
<summary>Codex</summary>

Use the Codex CLI to add the Playwright MCP server:

```bash
codex mcp add playwright npx "@playwright/mcp@latest"
```

Alternatively, create or edit the configuration file `~/.codex/config.toml` and add:

```toml
[mcp_servers.playwright]
command = "npx"
args = ["@playwright/mcp@latest"]
```

For more information, see the [Codex MCP documentation](https://github.com/openai/codex/blob/main/codex-rs/config.md#mcp_servers).

</details>

<details>
<summary>Copilot</summary>

Use the Copilot CLI to interactively add the Playwright MCP server:

```bash
/mcp add
```

Alternatively, create or edit the configuration file `~/.copilot/mcp-config.json` and add:

```json
{
  "mcpServers": {
    "playwright": {
      "type": "local",
      "command": "npx",
      "tools": [
        "*"
      ],
      "args": [
        "@playwright/mcp@latest"
      ]
    }
  }
}
```

For more information, see the [Copilot CLI documentation](https://docs.github.com/en/copilot/concepts/agents/about-copilot-cli).

</details>

<details>
<summary>Cursor</summary>

#### Click the button to install:

[<img src="https://cursor.com/deeplink/mcp-install-dark.svg" alt="Install in Cursor">](https://cursor.com/en/install-mcp?name=Playwright&config=eyJjb21tYW5kIjoibnB4IEBwbGF5d3JpZ2h0L21jcEBsYXRlc3QifQ%3D%3D)

#### Or install manually:

Go to `Cursor Settings` -> `MCP` -> `Add new MCP Server`. Name to your liking, use `command` type with the command `npx @playwright/mcp@latest`. You can also verify config or add command like arguments via clicking `Edit`.

</details>

<details>
<summary>Factory</summary>

Use the Factory CLI to add the Playwright MCP server:

```bash
droid mcp add playwright "npx @playwright/mcp@latest"
```

Alternatively, type `/mcp` within Factory droid to open an interactive UI for managing MCP servers.

For more information, see the [Factory MCP documentation](https://docs.factory.ai/cli/configuration/mcp).

</details>

<details>
<summary>Gemini CLI</summary>

Follow the MCP install [guide](https://github.com/google-gemini/gemini-cli/blob/main/docs/tools/mcp-server.md#configure-the-mcp-server-in-settingsjson), use the standard config above.

</details>

<details>
<summary>Goose</summary>

#### Click the button to install:

[![Install in Goose](https://block.github.io/goose/img/extension-install-dark.svg)](https://block.github.io/goose/extension?cmd=npx&arg=%40playwright%2Fmcp%40latest&id=playwright&name=Playwright&description=Interact%20with%20web%20pages%20through%20structured%20accessibility%20snapshots%20using%20Playwright)

#### Or install manually:

Go to `Advanced settings` -> `Extensions` -> `Add custom extension`. Name to your liking, use type `STDIO`, and set the `command` to `npx @playwright/mcp`. Click "Add Extension".
</details>

<details>
<summary>Kiro</summary>

[![Add to Kiro](https://kiro.dev/images/add-to-kiro.svg)](https://kiro.dev/launch/mcp/add?name=playwright&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22%40playwright%2Fmcp%40latest%22%5D%7D)

Follow the MCP Servers [documentation](https://kiro.dev/docs/mcp/). For example in `.kiro/settings/mcp.json`:

```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": [
        "@playwright/mcp@latest"
      ]
    }
  }
}
```
</details>

<details>
<summary>LM Studio</summary>

#### Click the button to install:

[![Add MCP Server playwright to LM Studio](https://files.lmstudio.ai/deeplink/mcp-install-light.svg)](https://lmstudio.ai/install-mcp?name=playwright&config=eyJjb21tYW5kIjoibnB4IiwiYXJncyI6WyJAcGxheXdyaWdodC9tY3BAbGF0ZXN0Il19)

#### Or install manually:

Go to `Program` in the right sidebar -> `Install` -> `Edit mcp.json`. Use the standard config above.
</details>

<details>
<summary>opencode</summary>

Follow the MCP Servers [documentation](https://opencode.ai/docs/mcp-servers/). For example in `~/.config/opencode/opencode.json`:

```json
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "playwright": {
      "type": "local",
      "command": [
        "npx",
        "@playwright/mcp@latest"
      ],
      "enabled": true
    }
  }
}

```
</details>

<details>
<summary>Qodo Gen</summary>

Open [Qodo Gen](https://docs.qodo.ai/qodo-documentation/qodo-gen) chat panel in VSCode or IntelliJ → Connect more tools → + Add new MCP → Paste the standard config above.

Click <code>Save</code>.
</details>

<details>
<summary>VS Code</summary>

#### Click the button to install:

[<img src="https://img.shields.io/badge/VS_Code-VS_Code?style=flat-square&label=Install%20Server&color=0098FF" alt="Install in VS Code">](https://insiders.vscode.dev/redirect?url=vscode%3Amcp%2Finstall%3F%257B%2522name%2522%253A%2522playwright%2522%252C%2522command%2522%253A%2522npx%2522%252C%2522args%2522%253A%255B%2522%2540playwright%252Fmcp%2540latest%2522%255D%257D) [<img alt="Install in VS Code Insiders" src="https://img.shields.io/badge/VS_Code_Insiders-VS_Code_Insiders?style=flat-square&label=Install%20Server&color=24bfa5">](https://insiders.vscode.dev/redirect?url=vscode-insiders%3Amcp%2Finstall%3F%257B%2522name%2522%253A%2522playwright%2522%252C%2522command%2522%253A%2522npx%2522%252C%2522args%2522%253A%255B%2522%2540playwright%252Fmcp%2540latest%2522%255D%257D)

#### Or install manually:

Follow the MCP install [guide](https://code.visualstudio.com/docs/copilot/chat/mcp-servers#_add-an-mcp-server), use the standard config above. You can also install the Playwright MCP server using the VS Code CLI:

```bash
# For VS Code
code --add-mcp '{"name":"playwright","command":"npx","args":["@playwright/mcp@latest"]}'
```

After installation, the Playwright MCP server will be available for use with your GitHub Copilot agent in VS Code.
</details>

<details>
<summary>Warp</summary>

Go to `Settings` -> `AI` -> `Manage MCP Servers` -> `+ Add` to [add an MCP Server](https://docs.warp.dev/knowledge-and-collaboration/mcp#adding-an-mcp-server). Use the standard config above.

Alternatively, use the slash command `/add-mcp` in the Warp prompt and paste the standard config from above:
```js
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": [
        "@playwright/mcp@latest"
      ]
    }
  }
}
```

</details>

<details>
<summary>Windsurf</summary>

Follow Windsurf MCP [documentation](https://docs.windsurf.com/windsurf/cascade/mcp). Use the standard config above.

</details>

### Configuration

Playwright MCP server supports following arguments. They can be provided in the JSON configuration above, as a part of the `"args"` list:

<!--- Options generated by update-readme.js -->

| Option | Description |
|--------|-------------|
| --allowed-hosts <hosts...> | comma-separated list of hosts this server is allowed to serve from. Defaults to the host the server is bound to. Pass '*' to disable the host check.<br>*env* `PLAYWRIGHT_MCP_ALLOWED_HOSTS` |
| --allowed-origins <origins> | semicolon-separated list of TRUSTED origins to allow the browser to request. Default is to allow all. Important: *does not* serve as a security boundary and *does not* affect redirects.<br>*env* `PLAYWRIGHT_MCP_ALLOWED_ORIGINS` |
| --allow-unrestricted-file-access | allow access to files outside of the workspace roots. Also allows unrestricted access to file:// URLs. By default access to file system is restricted to workspace root directories (or cwd if no roots are configured) only, and navigation to file:// URLs is blocked.<br>*env* `PLAYWRIGHT_MCP_ALLOW_UNRESTRICTED_FILE_ACCESS` |
| --blocked-origins <origins> | semicolon-separated list of origins to block the browser from requesting. Blocklist is evaluated before allowlist. If used without the allowlist, requests not matching the blocklist are still allowed. Important: *does not* serve as a security boundary and *does not* affect redirects.<br>*env* `PLAYWRIGHT_MCP_BLOCKED_ORIGINS` |
| --block-service-workers | block service workers<br>*env* `PLAYWRIGHT_MCP_BLOCK_SERVICE_WORKERS` |
| --browser <browser> | browser or chrome channel to use, possible values: chrome, firefox, webkit, msedge.<br>*env* `PLAYWRIGHT_MCP_BROWSER` |
| --caps <caps> | comma-separated list of additional capabilities to enable, possible values: vision, pdf, devtools.<br>*env* `PLAYWRIGHT_MCP_CAPS` |
| --cdp-endpoint <endpoint> | CDP endpoint to connect to.<br>*env* `PLAYWRIGHT_MCP_CDP_ENDPOINT` |
| --cdp-header <headers...> | CDP headers to send with the connect request, multiple can be specified.<br>*env* `PLAYWRIGHT_MCP_CDP_HEADER` |
| --cdp-timeout <timeout> | timeout in milliseconds for connecting to CDP endpoint, defaults to 30000ms<br>*env* `PLAYWRIGHT_MCP_CDP_TIMEOUT` |
| --codegen <lang> | specify the language to use for code generation, possible values: "typescript", "none". Default is "typescript".<br>*env* `PLAYWRIGHT_MCP_CODEGEN` |
| --config <path> | path to the configuration file.<br>*env* `PLAYWRIGHT_MCP_CONFIG` |
| --console-level <level> | level of console messages to return: "error", "warning", "info", "debug". Each level includes the messages of more severe levels.<br>*env* `PLAYWRIGHT_MCP_CONSOLE_LEVEL` |
| --device <device> | device to emulate, for example: "iPhone 15"<br>*env* `PLAYWRIGHT_MCP_DEVICE` |
| --executable-path <path> | path to the browser executable.<br>*env* `PLAYWRIGHT_MCP_EXECUTABLE_PATH` |
| --extension | Connect to a running browser instance (Edge/Chrome only). Requires the "Playwright MCP Bridge" browser extension to be installed.<br>*env* `PLAYWRIGHT_MCP_EXTENSION` |
| --grant-permissions <permissions...> | List of permissions to grant to the browser context, for example "geolocation", "clipboard-read", "clipboard-write".<br>*env* `PLAYWRIGHT_MCP_GRANT_PERMISSIONS` |
| --headless | run browser in headless mode, headed by default<br>*env* `PLAYWRIGHT_MCP_HEADLESS` |
| --host <host> | host to bind server to. Default is localhost. Use 0.0.0.0 to bind to all interfaces.<br>*env* `PLAYWRIGHT_MCP_HOST` |
| --ignore-https-errors | ignore https errors<br>*env* `PLAYWRIGHT_MCP_IGNORE_HTTPS_ERRORS` |
| --init-page <path...> | path to TypeScript file to evaluate on Playwright page object<br>*env* `PLAYWRIGHT_MCP_INIT_PAGE` |
| --init-script <path...> | path to JavaScript file to add as an initialization script. The script will be evaluated in every page before any of the page's scripts. Can be specified multiple times.<br>*env* `PLAYWRIGHT_MCP_INIT_SCRIPT` |
| --isolated | keep the browser profile in memory, do not save it to disk.<br>*env* `PLAYWRIGHT_MCP_ISOLATED` |
| --image-responses <mode> | whether to send image responses to the client. Can be "allow" or "omit", Defaults to "allow".<br>*env* `PLAYWRIGHT_MCP_IMAGE_RESPONSES` |
| --no-sandbox | disable the sandbox for all process types that are normally sandboxed.<br>*env* `PLAYWRIGHT_MCP_NO_SANDBOX` |
| --output-dir <path> | path to the directory for output files.<br>*env* `PLAYWRIGHT_MCP_OUTPUT_DIR` |
| --output-mode <mode> | whether to save snapshots, console messages, network logs to a file or to the standard output. Can be "file" or "stdout". Default is "stdout".<br>*env* `PLAYWRIGHT_MCP_OUTPUT_MODE` |
| --port <port> | port to listen on for SSE transport.<br>*env* `PLAYWRIGHT_MCP_PORT` |
| --proxy-bypass <bypass> | comma-separated domains to bypass proxy, for example ".com,chromium.org,.domain.com"<br>*env* `PLAYWRIGHT_MCP_PROXY_BYPASS` |
| --proxy-server <proxy> | specify proxy server, for example "http://myproxy:3128" or "socks5://myproxy:8080"<br>*env* `PLAYWRIGHT_MCP_PROXY_SERVER` |
| --sandbox | enable the sandbox for all process types that are normally not sandboxed.<br>*env* `PLAYWRIGHT_MCP_SANDBOX` |
| --save-session | Whether to save the Playwright MCP session into the output directory.<br>*env* `PLAYWRIGHT_MCP_SAVE_SESSION` |
| --secrets <path> | path to a file containing secrets in the dotenv format<br>*env* `PLAYWRIGHT_MCP_SECRETS` |
| --shared-browser-context | reuse the same browser context between all connected HTTP clients.<br>*env* `PLAYWRIGHT_MCP_SHARED_BROWSER_CONTEXT` |
| --snapshot-mode <mode> | when taking snapshots for responses, specifies the mode to use. Can be "incremental", "full", or "none". Default is incremental.<br>*env* `PLAYWRIGHT_MCP_SNAPSHOT_MODE` |
| --storage-state <path> | path to the storage state file for isolated sessions.<br>*env* `PLAYWRIGHT_MCP_STORAGE_STATE` |
| --test-id-attribute <attribute> | specify the attribute to use for test ids, defaults to "data-testid"<br>*env* `PLAYWRIGHT_MCP_TEST_ID_ATTRIBUTE` |
| --timeout-action <timeout> | specify action timeout in milliseconds, defaults to 5000ms<br>*env* `PLAYWRIGHT_MCP_TIMEOUT_ACTION` |
| --timeout-navigation <timeout> | specify navigation timeout in milliseconds, defaults to 60000ms<br>*env* `PLAYWRIGHT_MCP_TIMEOUT_NAVIGATION` |
| --user-agent <ua string> | specify user agent string<br>*env* `PLAYWRIGHT_MCP_USER_AGENT` |
| --user-data-dir <path> | path to the user data directory. If not specified, a temporary directory will be created.<br>*env* `PLAYWRIGHT_MCP_USER_DATA_DIR` |
| --viewport-size <size> | specify browser viewport size in pixels, for example "1280x720"<br>*env* `PLAYWRIGHT_MCP_VIEWPORT_SIZE` |

<!--- End of options generated section -->

### User profile

You can run Playwright MCP with persistent profile like a regular browser (default), in isolated contexts for testing sessions, or connect to your existing browser using the browser extension.

**Persistent profile**

All the logged in information will be stored in the persistent profile, you can delete it between sessions if you'd like to clear the offline state.
Persistent profile is located at the following locations and you can override it with the `--user-data-dir` argument.

```bash
# Windows
%USERPROFILE%\AppData\Local\ms-playwright\mcp-{channel}-profile

# macOS
- ~/Library/Caches/ms-playwright/mcp-{channel}-profile

# Linux
- ~/.cache/ms-playwright/mcp-{channel}-profile
```

**Isolated**

In the isolated mode, each session is started in the isolated profile. Every time you ask MCP to close the browser,
the session is closed and all the storage state for this session is lost. You can provide initial storage state
to the browser via the config's `contextOptions` or via the `--storage-state` argument. Learn more about the storage
state [here](https://playwright.dev/docs/auth).

```js
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": [
        "@playwright/mcp@latest",
        "--isolated",
        "--storage-state={path/to/storage.json}"
      ]
    }
  }
}
```

**Browser Extension**

The Playwright MCP Chrome Extension allows you to connect to existing browser tabs and leverage your logged-in sessions and browser state. See [packages/extension/README.md](packages/extension/README.md) for installation and setup instructions.

### Initial state

There are multiple ways to provide the initial state to the browser context or a page.

For the storage state, you can either:
- Start with a user data directory using the `--user-data-dir` argument. This will persist all browser data between the sessions.
- Start with a storage state file using the `--storage-state` argument. This will load cookies and local storage from the file into an isolated browser context.

For the page state, you can use:

- `--init-page` to point to a TypeScript file that will be evaluated on the Playwright page object. This allows you to run arbitrary code to set up the page.

```ts
// init-page.ts
export default async ({ page }) => {
  await page.context().grantPermissions(['geolocation']);
  await page.context().setGeolocation({ latitude: 37.7749, longitude: -122.4194 });
  await page.setViewportSize({ width: 1280, height: 720 });
};
```

- `--init-script` to point to a JavaScript file that will be added as an initialization script. The script will be evaluated in every page before any of the page's scripts.
This is useful for overriding browser APIs or setting up the environment.

```js
// init-script.js
window.isPlaywrightMCP = true;
```

### Configuration file

The Playwright MCP server can be configured using a JSON configuration file. You can specify the configuration file
using the `--config` command line option:

```bash
npx @playwright/mcp@latest --config path/to/config.json
```

<details>
<summary>Configuration file schema</summary>

<!--- Config generated by update-readme.js -->

```typescript
{
  /**
   * The browser to use.
   */
  browser?: {
    /**
     * The type of browser to use.
     */
    browserName?: 'chromium' | 'firefox' | 'webkit';

    /**
     * Keep the browser profile in memory, do not save it to disk.
     */
    isolated?: boolean;

    /**
     * Path to a user data directory for browser profile persistence.
     * Temporary directory is created by default.
     */
    userDataDir?: string;

    /**
     * Launch options passed to
     * @see https://playwright.dev/docs/api/class-browsertype#browser-type-launch-persistent-context
     *
     * This is useful for settings options like `channel`, `headless`, `executablePath`, etc.
     */
    launchOptions?: playwright.LaunchOptions;

    /**
     * Context options for the browser context.
     *
     * This is useful for settings options like `viewport`.
     */
    contextOptions?: playwright.BrowserContextOptions;

    /**
     * Chrome DevTools Protocol endpoint to connect to an existing browser instance in case of Chromium family browsers.
     */
    cdpEndpoint?: string;

    /**
     * CDP headers to send with the connect request.
     */
    cdpHeaders?: Record<string, string>;

    /**
     * Timeout in milliseconds for connecting to CDP endpoint. Defaults to 30000 (30 seconds). Pass 0 to disable timeout.
     */
    cdpTimeout?: number;

    /**
     * Remote endpoint to connect to an existing Playwright server.
     */
    remoteEndpoint?: string;

    /**
     * Paths to TypeScript files to add as initialization scripts for Playwright page.
     */
    initPage?: string[];

    /**
     * Paths to JavaScript files to add as initialization scripts.
     * The scripts will be evaluated in every page before any of the page's scripts.
     */
    initScript?: string[];
  },

  /**
   * Connect to a running browser instance (Edge/Chrome only). If specified, `browser`
   * config is ignored.
   * Requires the "Playwright MCP Bridge" browser extension to be installed.
   */
  extension?: boolean;

  server?: {
    /**
     * The port to listen on for SSE or MCP transport.
     */
    port?: number;

    /**
     * The host to bind the server to. Default is localhost. Use 0.0.0.0 to bind to all interfaces.
     */
    host?: string;

    /**
     * The hosts this server is allowed to serve from. Defaults to the host server is bound to.
     * This is not for CORS, but rather for the DNS rebinding protection.
     */
    allowedHosts?: string[];
  },

  /**
   * List of enabled tool capabilities. Possible values:
   *   - 'core': Core browser automation features.
   *   - 'pdf': PDF generation and manipulation.
   *   - 'vision': Coordinate-based interactions.
   *   - 'devtools': Developer tools features.
   */
  capabilities?: ToolCapability[];

  /**
   * Whether to save the Playwright session into the output directory.
   */
  saveSession?: boolean;

  /**
   * Reuse the same browser context between all connected HTTP clients.
   */
  sharedBrowserContext?: boolean;

  /**
   * Secrets are used to prevent LLM from getting sensitive data while
   * automating scenarios such as authentication.
   * Prefer the browser.contextOptions.storageState over secrets file as a more secure alternative.
   */
  secrets?: Record<string, string>;

  /**
   * The directory to save output files.
   */
  outputDir?: string;

  /**
   * Whether to save snapshots, console messages, network logs and other session logs to a file or to the standard output. Defaults to "stdout".
   */
  outputMode?: 'file' | 'stdout';

  console?: {
    /**
     * The level of console messages to return. Each level includes the messages of more severe levels. Defaults to "info".
     */
    level?: 'error' | 'warning' | 'info' | 'debug';
  },

  network?: {
    /**
     * List of origins to allow the browser to request. Default is to allow all. Origins matching both `allowedOrigins` and `blockedOrigins` will be blocked.
     *
     * Supported formats:
     * - Full origin: `https://example.com:8080` - matches only that origin
     * - Wildcard port: `http://localhost:*` - matches any port on localhost with http protocol
     */
    allowedOrigins?: string[];

    /**
     * List of origins to block the browser to request. Origins matching both `allowedOrigins` and `blockedOrigins` will be blocked.
     *
     * Supported formats:
     * - Full origin: `https://example.com:8080` - matches only that origin
     * - Wildcard port: `http://localhost:*` - matches any port on localhost with http protocol
     */
    blockedOrigins?: string[];
  };

  /**
   * Specify the attribute to use for test ids, defaults to "data-testid".
   */
  testIdAttribute?: string;

  timeouts?: {
    /*
     * Configures default action timeout: https://playwright.dev/docs/api/class-page#page-set-default-timeout. Defaults to 5000ms.
     */
    action?: number;

    /*
     * Configures default navigation timeout: https://playwright.dev/docs/api/class-page#page-set-default-navigation-timeout. Defaults to 60000ms.
     */
    navigation?: number;

    /**
     * Configures default expect timeout: https://playwright.dev/docs/test-timeouts#expect-timeout. Defaults to 5000ms.
     */
    expect?: number;
  };

  /**
   * Whether to send image responses to the client. Can be "allow", "omit", or "auto". Defaults to "auto", which sends images if the client can display them.
   */
  imageResponses?: 'allow' | 'omit';

  snapshot?: {
    /**
     * When taking snapshots for responses, specifies the mode to use.
     */
    mode?: 'incremental' | 'full' | 'none';
  };

  /**
   * Whether to allow file uploads from anywhere on the file system.
   * By default (false), file uploads are restricted to paths within the MCP roots only.
   */
  allowUnrestrictedFileAccess?: boolean;

  /**
   * Specify the language to use for code generation.
   */
  codegen?: 'typescript' | 'none';
}
```

<!--- End of config generated section -->

</details>

### Standalone MCP server

When running headed browser on system w/o display or from worker processes of the IDEs,
run the MCP server from environment with the DISPLAY and pass the `--port` flag to enable HTTP transport.

```bash
npx @playwright/mcp@latest --port 8931
```

And then in MCP client config, set the `url` to the HTTP endpoint:

```js
{
  "mcpServers": {
    "playwright": {
      "url": "http://localhost:8931/mcp"
    }
  }
}
```

## Security

Playwright MCP is **not** a security boundary. See [MCP Security Best Practices](https://modelcontextprotocol.io/docs/tutorials/security/security_best_practices) for guidance on securing your deployment.

<details>
<summary><b>Docker</b></summary>

**NOTE:** The Docker implementation only supports headless chromium at the moment.

```js
{
  "mcpServers": {
    "playwright": {
      "command": "docker",
      "args": ["run", "-i", "--rm", "--init", "--pull=always", "mcr.microsoft.com/playwright/mcp"]
    }
  }
}
```

Or If you prefer to run the container as a long-lived service instead of letting the MCP client spawn it, use:

```
docker run -d -i --rm --init --pull=always \
  --entrypoint node \
  --name playwright \
  -p 8931:8931 \
  mcr.microsoft.com/playwright/mcp \
  cli.js --headless --browser chromium --no-sandbox --port 8931 --host 0.0.0.0
```

The server will listen on host port **8931** and can be reached by any MCP client.  

You can build the Docker image yourself.

```
docker build -t mcr.microsoft.com/playwright/mcp .
```
</details>

<details>
<summary><b>Programmatic usage</b></summary>

```js
import http from 'http';

import { createConnection } from '@playwright/mcp';
import { SSEServerTransport } from '@modelcontextprotocol/sdk/server/sse.js';

http.createServer(async (req, res) => {
  // ...

  // Creates a headless Playwright MCP server with SSE transport
  const connection = await createConnection({ browser: { launchOptions: { headless: true } } });
  const transport = new SSEServerTransport('/messages', res);
  await connection.connect(transport);

  // ...
});
```
</details>

### Tools

<!--- Tools generated by update-readme.js -->

<details>
<summary><b>Core automation</b></summary>

<!-- NOTE: This has been generated via update-readme.js -->

- **browser_click**
  - Title: Click
  - Description: Perform click on a web page
  - Parameters:
    - `element` (string, optional): Human-readable element description used to obtain permission to interact with the element
    - `ref` (string): Exact target element reference from the page snapshot
    - `selector` (string, optional): CSS or role selector for the target element, when "ref" is not available
    - `doubleClick` (boolean, optional): Whether to perform a double click instead of a single click
    - `button` (string, optional): Button to click, defaults to left
    - `modifiers` (array, optional): Modifier keys to press
  - Read-only: **false**

<!-- NOTE: This has been generated via update-readme.js -->

- **browser_close**
  - Title: Close browser
  - Description: Close the page
  - Parameters: None
  - Read-only: **false**

<!-- NOTE: This has been generated via update-readme.js -->

- **browser_console_messages**
  - Title: Get console messages
  - Description: Returns all console messages
  - Parameters:
    - `level` (string): Level of the console messages to return. Each level includes the messages of more severe levels. Defaults to "info".
    - `all` (boolean, optional): Return all console messages since the beginning of the session, not just since the last navigation. Defaults to false.
    - `filename` (string, optional): Filename to save the console messages to. If not provided, messages are returned as text.
  - Read-only: **true**

<!-- NOTE: This has been generated via update-readme.js -->

- **browser_drag**
  - Title: Drag mouse
  - Description: Perform drag and drop between two elements
  - Parameters:
    - `startElement` (string): Human-readable source element description used to obtain the permission to interact with the element
    - `startRef` (string): Exact source element reference from the page snapshot
    - `startSelector` (string, optional): CSS or role selector for the source element, when ref is not available
    - `endElement` (string): Human-readable target element description used to obtain the permission to interact with the element
    - `endRef` (string): Exact target element reference from the page snapshot
    - `endSelector` (string, optional): CSS or role selector for the target element, when ref is not available
  - Read-only: **false**

<!-- NOTE: This has been generated via update-readme.js -->

- **browser_evaluate**
  - Title: Evaluate JavaScript
  - Description: Evaluate JavaScript expression on page or element
  - Parameters:
    - `function` (string): () => { /* code */ } or (element) => { /* code */ } when element is provided
    - `element` (string, optional): Human-readable element description used to obtain permission to interact with the element
    - `ref` (string, optional): Exact target element reference from the page snapshot
    - `selector` (string, optional): CSS or role selector for the target element, when "ref" is not available.
  - Read-only: **false**

<!-- NOTE: This has been generated via update-readme.js -->

- **browser_file_upload**
  - Title: Upload files
  - Description: Upload one or multiple files
  - Parameters:
    - `paths` (array, optional): The absolute paths to the files to upload. Can be single file or multiple files. If omitted, file chooser is cancelled.
  - Read-only: **false**

<!-- NOTE: This has been generated via update-readme.js -->

- **browser_fill_form**
  - Title: Fill form
  - Description: Fill multiple form fields
  - Parameters:
    - `fields` (array): Fields to fill in
  - Read-only: **false**

<!-- NOTE: This has been generated via update-readme.js -->

- **browser_handle_dialog**
  - Title: Handle a dialog
  - Description: Handle a dialog
  - Parameters:
    - `accept` (boolean): Whether to accept the dialog.
    - `promptText` (string, optional): The text of the prompt in case of a prompt dialog.
  - Read-only: **false**

<!-- NOTE: This has been generated via update-readme.js -->

- **browser_hover**
  - Title: Hover mouse
  - Description: Hover over element on page
  - Parameters:
    - `element` (string, optional): Human-readable element description used to obtain permission to interact with the element
    - `ref` (string): Exact target element reference from the page snapshot
    - `selector` (string, optional): CSS or role selector for the target element, when "ref" is not available
  - Read-only: **false**

<!-- NOTE: This has been generated via update-readme.js -->

- **browser_navigate**
  - Title: Navigate to a URL
  - Description: Navigate to a URL
  - Parameters:
    - `url` (string): The URL to navigate to
  - Read-only: **false**

<!-- NOTE: This has been generated via update-readme.js -->

- **browser_navigate_back**
  - Title: Go back
  - Description: Go back to the previous page in the history
  - Parameters: None
  - Read-only: **false**

<!-- NOTE: This has been generated via update-readme.js -->

- **browser_network_requests**
  - Title: List network requests
  - Description: Returns all network requests since loading the page
  - Parameters:
    - `includeStatic` (boolean): Whether to include successful static resources like images, fonts, scripts, etc. Defaults to false.
    - `filename` (string, optional): Filename to save the network requests to. If not provided, requests are returned as text.
  - Read-only: **true**

<!-- NOTE: This has been generated via update-readme.js -->

- **browser_press_key**
  - Title: Press a key
  - Description: Press a key on the keyboard
  - Parameters:
    - `key` (string): Name of the key to press or a character to generate, such as `ArrowLeft` or `a`
  - Read-only: **false**

<!-- NOTE: This has been generated via update-readme.js -->

- **browser_resize**
  - Title: Resize browser window
  - Description: Resize the browser window
  - Parameters:
    - `width` (number): Width of the browser window
    - `height` (number): Height of the browser window
  - Read-only: **false**

<!-- NOTE: This has been generated via update-readme.js -->

- **browser_run_code**
  - Title: Run Playwright code
  - Description: Run Playwright code snippet
  - Parameters:
    - `code` (string): A JavaScript function containing Playwright code to execute. It will be invoked with a single argument, page, which you can use for any page interaction. For example: `async (page) => { await page.getByRole('button', { name: 'Submit' }).click(); return await page.title(); }`
  - Read-only: **false**

<!-- NOTE: This has been generated via update-readme.js -->

- **browser_select_option**
  - Title: Select option
  - Description: Select an option in a dropdown
  - Parameters:
    - `element` (string, optional): Human-readable element description used to obtain permission to interact with the element
    - `ref` (string): Exact target element reference from the page snapshot
    - `selector` (string, optional): CSS or role selector for the target element, when "ref" is not available
    - `values` (array): Array of values to select in the dropdown. This can be a single value or multiple values.
  - Read-only: **false**

<!-- NOTE: This has been generated via update-readme.js -->

- **browser_snapshot**
  - Title: Page snapshot
  - Description: Capture accessibility snapshot of the current page, this is better than screenshot
  - Parameters:
    - `filename` (string, optional): Save snapshot to markdown file instead of returning it in the response.
    - `selector` (string, optional): Element selector of the root element to capture a partial snapshot instead of the whole page
  - Read-only: **true**

<!-- NOTE: This has been generated via update-readme.js -->

- **browser_take_screenshot**
  - Title: Take a screenshot
  - Description: Take a screenshot of the current page. You can't perform actions based on the screenshot, use browser_snapshot for actions.
  - Parameters:
    - `type` (string): Image format for the screenshot. Default is png.
    - `filename` (string, optional): File name to save the screenshot to. Defaults to `page-{timestamp}.{png|jpeg}` if not specified. Prefer relative file names to stay within the output directory.
    - `element` (string, optional): Human-readable element description used to obtain permission to screenshot the element. If not provided, the screenshot will be taken of viewport. If element is provided, ref must be provided too.
    - `ref` (string, optional): Exact target element reference from the page snapshot. If not provided, the screenshot will be taken of viewport. If ref is provided, element must be provided too.
    - `selector` (string, optional): CSS or role selector for the target element, when "ref" is not available.
    - `fullPage` (boolean, optional): When true, takes a screenshot of the full scrollable page, instead of the currently visible viewport. Cannot be used with element screenshots.
  - Read-only: **true**

<!-- NOTE: This has been generated via update-readme.js -->

- **browser_type**
  - Title: Type text
  - Description: Type text into editable element
  - Parameters:
    - `element` (string, optional): Human-readable element description used to obtain permission to interact with the element
    - `ref` (string): Exact target element reference from the page snapshot
    - `selector` (string, optional): CSS or role selector for the target element, when "ref" is not available
    - `text` (string): Text to type into the element
    - `submit` (boolean, optional): Whether to submit entered text (press Enter after)
    - `slowly` (boolean, optional): Whether to type one character at a time. Useful for triggering key handlers in the page. By default entire text is filled in at once.
  - Read-only: **false**

<!-- NOTE: This has been generated via update-readme.js -->

- **browser_wait_for**
  - Title: Wait for
  - Description: Wait for text to appear or disappear or a specified time to pass
  - Parameters:
    - `time` (number, optional): The time to wait in seconds
    - `text` (string, optional): The text to wait for
    - `textGone` (string, optional): The text to wait for to disappear
  - Read-only: **false**

</details>

<details>
<summary><b>Tab management</b></summary>

<!-- NOTE: This has been generated via update-readme.js -->

- **browser_tabs**
  - Title: Manage tabs
  - Description: List, create, close, or select a browser tab.
  - Parameters:
    - `action` (string): Operation to perform
    - `index` (number, optional): Tab index, used for close/select. If omitted for close, current tab is closed.
  - Read-only: **false**

</details>

<details>
<summary><b>Browser installation</b></summary>

</details>

<details>
<summary><b>Configuration (opt-in via --caps=config)</b></summary>

<!-- NOTE: This has been generated via update-readme.js -->

- **browser_get_config**
  - Title: Get config
  - Description: Get the final resolved config after merging CLI options, environment variables and config file.
  - Parameters: None
  - Read-only: **true**

</details>

<details>
<summary><b>Network (opt-in via --caps=network)</b></summary>

<!-- NOTE: This has been generated via update-readme.js -->

- **browser_network_state_set**
  - Title: Set network state
  - Description: Sets the browser network state to online or offline. When offline, all network requests will fail.
  - Parameters:
    - `state` (string): Set to "offline" to simulate offline mode, "online" to restore network connectivity
  - Read-only: **false**

<!-- NOTE: This has been generated via update-readme.js -->

- **browser_route**
  - Title: Mock network requests
  - Description: Set up a route to mock network requests matching a URL pattern
  - Parameters:
    - `pattern` (string): URL pattern to match (e.g., "**/api/users", "**/*.{png,jpg}")
    - `status` (number, optional): HTTP status code to return (default: 200)
    - `body` (string, optional): Response body (text or JSON string)
    - `contentType` (string, optional): Content-Type header (e.g., "application/json", "text/html")
    - `headers` (array, optional): Headers to add in "Name: Value" format
    - `removeHeaders` (string, optional): Comma-separated list of header names to remove from request
  - Read-only: **false**

<!-- NOTE: This has been generated via update-readme.js -->

- **browser_route_list**
  - Title: List network routes
  - Description: List all active network routes
  - Parameters: None
  - Read-only: **true**

<!-- NOTE: This has been generated via update-readme.js -->

- **browser_unroute**
  - Title: Remove network routes
  - Description: Remove network routes matching a pattern (or all routes if no pattern specified)
  - Parameters:
    - `pattern` (string, optional): URL pattern to unroute (omit to remove all routes)
  - Read-only: **false**

</details>

<details>
<summary><b>Storage (opt-in via --caps=storage)</b></summary>

<!-- NOTE: This has been generated via update-readme.js -->

- **browser_cookie_clear**
  - Title: Clear cookies
  - Description: Clear all cookies
  - Parameters: None
  - Read-only: **false**

<!-- NOTE: This has been generated via update-readme.js -->

- **browser_cookie_delete**
  - Title: Delete cookie
  - Description: Delete a specific cookie
  - Parameters:
    - `name` (string): Cookie name to delete
  - Read-only: **false**

<!-- NOTE: This has been generated via update-readme.js -->

- **browser_cookie_get**
  - Title: Get cookie
  - Description: Get a specific cookie by name
  - Parameters:
    - `name` (string): Cookie name to get
  - Read-only: **true**

<!-- NOTE: This has been generated via update-readme.js -->

- **browser_cookie_list**
  - Title: List cookies
  - Description: List all cookies (optionally filtered by domain/path)
  - Parameters:
    - `domain` (string, optional): Filter cookies by domain
    - `path` (string, optional): Filter cookies by path
  - Read-only: **true**

<!-- NOTE: This has been generated via update-readme.js -->

- **browser_cookie_set**
  - Title: Set cookie
  - Description: Set a cookie with optional flags (domain, path, expires, httpOnly, secure, sameSite)
  - Parameters:
    - `name` (string): Cookie name
    - `value` (string): Cookie value
    - `domain` (string, optional): Cookie domain
    - `path` (string, optional): Cookie path
    - `expires` (number, optional): Cookie expiration as Unix timestamp
    - `httpOnly` (boolean, optional): Whether the cookie is HTTP only
    - `secure` (boolean, optional): Whether the cookie is secure
    - `sameSite` (string, optional): Cookie SameSite attribute
  - Read-only: **false**

<!-- NOTE: This has been generated via update-readme.js -->

- **browser_localstorage_clear**
  - Title: Clear localStorage
  - Description: Clear all localStorage
  - Parameters: None
  - Read-only: **false**

<!-- NOTE: This has been generated via update-readme.js -->

- **browser_localstorage_delete**
  - Title: Delete localStorage item
  - Description: Delete a localStorage item
  - Parameters:
    - `key` (string): Key to delete
  - Read-only: **false**

<!-- NOTE: This has been generated via update-readme.js -->

- **browser_localstorage_get**
  - Title: Get localStorage item
  - Description: Get a localStorage item by key
  - Parameters:
    - `key` (string): Key to get
  - Read-only: **true**

<!-- NOTE: This has been generated via update-readme.js -->

- **browser_localstorage_list**
  - Title: List localStorage
  - Description: List all localStorage key-value pairs
  - Parameters: None
  - Read-only: **true**

<!-- NOTE: This has been generated via update-readme.js -->

- **browser_localstorage_set**
  - Title: Set localStorage item
  - Description: Set a localStorage item
  - Parameters:
    - `key` (string): Key to set
    - `value` (string): Value to set
  - Read-only: **false**

<!-- NOTE: This has been generated via update-readme.js -->

- **browser_sessionstorage_clear**
  - Title: Clear sessionStorage
  - Description: Clear all sessionStorage
  - Parameters: None
  - Read-only: **false**

<!-- NOTE: This has been generated via update-readme.js -->

- **browser_sessionstorage_delete**
  - Title: Delete sessionStorage item
  - Description: Delete a sessionStorage item
  - Parameters:
    - `key` (string): Key to delete
  - Read-only: **false**

<!-- NOTE: This has been generated via update-readme.js -->

- **browser_sessionstorage_get**
  - Title: Get sessionStorage item
  - Description: Get a sessionStorage item by key
  - Parameters:
    - `key` (string): Key to get
  - Read-only: **true**

<!-- NOTE: This has been generated via update-readme.js -->

- **browser_sessionstorage_list**
  - Title: List sessionStorage
  - Description: List all sessionStorage key-value pairs
  - Parameters: None
  - Read-only: **true**

<!-- NOTE: This has been generated via update-readme.js -->

- **browser_sessionstorage_set**
  - Title: Set sessionStorage item
  - Description: Set a sessionStorage item
  - Parameters:
    - `key` (string): Key to set
    - `value` (string): Value to set
  - Read-only: **false**

<!-- NOTE: This has been generated via update-readme.js -->

- **browser_set_storage_state**
  - Title: Restore storage state
  - Description: Restore storage state (cookies, local storage) from a file. This clears existing cookies and local storage before restoring.
  - Parameters:
    - `filename` (string): Path to the storage state file to restore from
  - Read-only: **false**

<!-- NOTE: This has been generated via update-readme.js -->

- **browser_storage_state**
  - Title: Save storage state
  - Description: Save storage state (cookies, local storage) to a file for later reuse
  - Parameters:
    - `filename` (string, optional): File name to save the storage state to. Defaults to `storage-state-{timestamp}.json` if not specified.
  - Read-only: **true**

</details>

<details>
<summary><b>DevTools (opt-in via --caps=devtools)</b></summary>

<!-- NOTE: This has been generated via update-readme.js -->

- **browser_start_tracing**
  - Title: Start tracing
  - Description: Start trace recording
  - Parameters: None
  - Read-only: **true**

<!-- NOTE: This has been generated via update-readme.js -->

- **browser_start_video**
  - Title: Start video
  - Description: Start video recording
  - Parameters:
    - `size` (object, optional): Video size
  - Read-only: **true**

<!-- NOTE: This has been generated via update-readme.js -->

- **browser_stop_tracing**
  - Title: Stop tracing
  - Description: Stop trace recording
  - Parameters: None
  - Read-only: **true**

<!-- NOTE: This has been generated via update-readme.js -->

- **browser_stop_video**
  - Title: Stop video
  - Description: Stop video recording
  - Parameters:
    - `filename` (string, optional): Filename to save the video
  - Read-only: **true**

</details>

<details>
<summary><b>Coordinate-based (opt-in via --caps=vision)</b></summary>

<!-- NOTE: This has been generated via update-readme.js -->

- **browser_mouse_click_xy**
  - Title: Click
  - Description: Click mouse button at a given position
  - Parameters:
    - `x` (number): X coordinate
    - `y` (number): Y coordinate
    - `button` (string, optional): Button to click, defaults to left
    - `clickCount` (number, optional): Number of clicks, defaults to 1
    - `delay` (number, optional): Time to wait between mouse down and mouse up in milliseconds, defaults to 0
  - Read-only: **false**

<!-- NOTE: This has been generated via update-readme.js -->

- **browser_mouse_down**
  - Title: Press mouse down
  - Description: Press mouse down
  - Parameters:
    - `button` (string, optional): Button to press, defaults to left
  - Read-only: **false**

<!-- NOTE: This has been generated via update-readme.js -->

- **browser_mouse_drag_xy**
  - Title: Drag mouse
  - Description: Drag left mouse button to a given position
  - Parameters:
    - `startX` (number): Start X coordinate
    - `startY` (number): Start Y coordinate
    - `endX` (number): End X coordinate
    - `endY` (number): End Y coordinate
  - Read-only: **false**

<!-- NOTE: This has been generated via update-readme.js -->

- **browser_mouse_move_xy**
  - Title: Move mouse
  - Description: Move mouse to a given position
  - Parameters:
    - `x` (number): X coordinate
    - `y` (number): Y coordinate
  - Read-only: **false**

<!-- NOTE: This has been generated via update-readme.js -->

- **browser_mouse_up**
  - Title: Press mouse up
  - Description: Press mouse up
  - Parameters:
    - `button` (string, optional): Button to press, defaults to left
  - Read-only: **false**

<!-- NOTE: This has been generated via update-readme.js -->

- **browser_mouse_wheel**
  - Title: Scroll mouse wheel
  - Description: Scroll mouse wheel
  - Parameters:
    - `deltaX` (number): X delta
    - `deltaY` (number): Y delta
  - Read-only: **false**

</details>

<details>
<summary><b>PDF generation (opt-in via --caps=pdf)</b></summary>

<!-- NOTE: This has been generated via update-readme.js -->

- **browser_pdf_save**
  - Title: Save as PDF
  - Description: Save page as PDF
  - Parameters:
    - `filename` (string, optional): File name to save the pdf to. Defaults to `page-{timestamp}.pdf` if not specified. Prefer relative file names to stay within the output directory.
  - Read-only: **true**

</details>

<details>
<summary><b>Test assertions (opt-in via --caps=testing)</b></summary>

<!-- NOTE: This has been generated via update-readme.js -->

- **browser_generate_locator**
  - Title: Create locator for element
  - Description: Generate locator for the given element to use in tests
  - Parameters:
    - `element` (string, optional): Human-readable element description used to obtain permission to interact with the element
    - `ref` (string): Exact target element reference from the page snapshot
    - `selector` (string, optional): CSS or role selector for the target element, when "ref" is not available
  - Read-only: **true**

<!-- NOTE: This has been generated via update-readme.js -->

- **browser_verify_element_visible**
  - Title: Verify element visible
  - Description: Verify element is visible on the page
  - Parameters:
    - `role` (string): ROLE of the element. Can be found in the snapshot like this: `- {ROLE} "Accessible Name":`
    - `accessibleName` (string): ACCESSIBLE_NAME of the element. Can be found in the snapshot like this: `- role "{ACCESSIBLE_NAME}"`
  - Read-only: **false**

<!-- NOTE: This has been generated via update-readme.js -->

- **browser_verify_list_visible**
  - Title: Verify list visible
  - Description: Verify list is visible on the page
  - Parameters:
    - `element` (string): Human-readable list description
    - `ref` (string): Exact target element reference that points to the list
    - `selector` (string, optional): CSS or role selector for the target list, when "ref" is not available.
    - `items` (array): Items to verify
  - Read-only: **false**

<!-- NOTE: This has been generated via update-readme.js -->

- **browser_verify_text_visible**
  - Title: Verify text visible
  - Description: Verify text is visible on the page. Prefer browser_verify_element_visible if possible.
  - Parameters:
    - `text` (string): TEXT to verify. Can be found in the snapshot like this: `- role "Accessible Name": {TEXT}` or like this: `- text: {TEXT}`
  - Read-only: **false**

<!-- NOTE: This has been generated via update-readme.js -->

- **browser_verify_value**
  - Title: Verify value
  - Description: Verify element value
  - Parameters:
    - `type` (string): Type of the element
    - `element` (string): Human-readable element description
    - `ref` (string): Exact target element reference from the page snapshot
    - `selector` (string, optional): CSS or role selector for the target element, when "ref" is not available
    - `value` (string): Value to verify. For checkbox, use "true" or "false".
  - Read-only: **false**

</details>


<!--- End of tools generated section -->
```

## File: `roll.js`
```javascript
const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

function copyConfig() {
  const src = path.join(__dirname, '..', 'playwright', 'packages', 'playwright-core', 'src', 'tools', 'mcp', 'config.d.ts');
  const dst = path.join(__dirname, 'packages', 'playwright-mcp', 'config.d.ts');
  let content = fs.readFileSync(src, 'utf-8');
  content = content.replace(
    "import type * as playwright from 'playwright-core';",
    "import type * as playwright from 'playwright';"
  );
  fs.writeFileSync(dst, content);
  console.log(`Copied config.d.ts from ${src} to ${dst}`);
}

function updatePlaywrightVersion(version) {
  const packagesDir = path.join(__dirname, 'packages');
  const files = [path.join(__dirname, 'package.json')];
  for (const entry of fs.readdirSync(packagesDir, { withFileTypes: true })) {
    const pkgJson = path.join(packagesDir, entry.name, 'package.json');
    if (fs.existsSync(pkgJson))
      files.push(pkgJson);
  }

  for (const file of files) {
    const json = JSON.parse(fs.readFileSync(file, 'utf-8'));
    let updated = false;
    for (const section of ['dependencies', 'devDependencies']) {
      for (const pkg of ['@playwright/test', 'playwright', 'playwright-core']) {
        if (json[section]?.[pkg]) {
          json[section][pkg] = version;
          updated = true;
        }
      }
    }
    if (updated) {
      fs.writeFileSync(file, JSON.stringify(json, null, 2) + '\n');
      console.log(`Updated ${file}`);
    }
  }

  execSync('npm install', { cwd: __dirname, stdio: 'inherit' });
}

function doRoll(version) {
  updatePlaywrightVersion(version);
  copyConfig();
  // update readme
  execSync('npm run lint', { cwd: __dirname, stdio: 'inherit' });
}

let version = process.argv[2];
if (!version) {
  version = execSync('npm info playwright@next version', { encoding: 'utf-8' }).trim();
  console.log(`Using next playwright version: ${version}`);
}
doRoll(version);
```

## File: `SECURITY.md`
```markdown
<!-- BEGIN MICROSOFT SECURITY.MD V0.0.9 BLOCK -->

## Security

Microsoft takes the security of our software products and services seriously, which includes all source code repositories managed through our GitHub organizations, which include [Microsoft](https://github.com/Microsoft), [Azure](https://github.com/Azure), [DotNet](https://github.com/dotnet), [AspNet](https://github.com/aspnet) and [Xamarin](https://github.com/xamarin).

If you believe you have found a security vulnerability in any Microsoft-owned repository that meets [Microsoft's definition of a security vulnerability](https://aka.ms/security.md/definition), please report it to us as described below.

## Reporting Security Issues

**Please do not report security vulnerabilities through public GitHub issues.**

Instead, please report them to the Microsoft Security Response Center (MSRC) at [https://msrc.microsoft.com/create-report](https://aka.ms/security.md/msrc/create-report).

If you prefer to submit without logging in, send email to [secure@microsoft.com](mailto:secure@microsoft.com).  If possible, encrypt your message with our PGP key; please download it from the [Microsoft Security Response Center PGP Key page](https://aka.ms/security.md/msrc/pgp).

You should receive a response within 24 hours. If for some reason you do not, please follow up via email to ensure we received your original message. Additional information can be found at [microsoft.com/msrc](https://www.microsoft.com/msrc). 

Please include the requested information listed below (as much as you can provide) to help us better understand the nature and scope of the possible issue:

  * Type of issue (e.g. buffer overflow, SQL injection, cross-site scripting, etc.)
  * Full paths of source file(s) related to the manifestation of the issue
  * The location of the affected source code (tag/branch/commit or direct URL)
  * Any special configuration required to reproduce the issue
  * Step-by-step instructions to reproduce the issue
  * Proof-of-concept or exploit code (if possible)
  * Impact of the issue, including how an attacker might exploit the issue

This information will help us triage your report more quickly.

If you are reporting for a bug bounty, more complete reports can contribute to a higher bounty award. Please visit our [Microsoft Bug Bounty Program](https://aka.ms/security.md/msrc/bounty) page for more details about our active programs.

## Preferred Languages

We prefer all communications to be in English.

## Policy

Microsoft follows the principle of [Coordinated Vulnerability Disclosure](https://aka.ms/security.md/cvd).

<!-- END MICROSOFT SECURITY.MD BLOCK -->
```

## File: `packages/extension/.gitignore`
```
dist/
```

## File: `packages/extension/manifest.json`
```json
{
  "manifest_version": 3,
  "name": "Playwright MCP Bridge",
  "version": "0.0.68",
  "description": "Share browser tabs with Playwright MCP server",
  "permissions": [
    "debugger",
    "activeTab",
    "tabs"
  ],
  "host_permissions": [
    "<all_urls>"
  ],
  "background": {
    "service_worker": "lib/background.mjs",
    "type": "module"
  },
  "action": {
    "default_title": "Playwright MCP Bridge",
    "default_icon": {
      "16": "icons/icon-16.png",
      "32": "icons/icon-32.png",
      "48": "icons/icon-48.png",
      "128": "icons/icon-128.png"
    }
  },
  "icons": {
    "16": "icons/icon-16.png",
    "32": "icons/icon-32.png",
    "48": "icons/icon-48.png",
    "128": "icons/icon-128.png"
  }
}
```

## File: `packages/extension/package.json`
```json
{
  "name": "@playwright/mcp-extension",
  "version": "0.0.68",
  "description": "Playwright MCP Browser Extension",
  "private": true,
  "repository": {
    "type": "git",
    "url": "git+https://github.com/microsoft/playwright-mcp.git"
  },
  "homepage": "https://playwright.dev",
  "engines": {
    "node": ">=18"
  },
  "author": {
    "name": "Microsoft Corporation"
  },
  "license": "Apache-2.0",
  "scripts": {
    "build": "tsc --project . && tsc --project tsconfig.ui.json && vite build && vite build --config vite.sw.config.mts",
    "watch": "tsc --watch --project . & tsc --watch --project tsconfig.ui.json & vite build --watch & vite build --watch --config vite.sw.config.mts",
    "test": "playwright test",
    "lint": "tsc --project .",
    "clean": "rm -rf dist"
  },
  "devDependencies": {
    "@types/chrome": "^0.0.315",
    "@types/react": "^18.2.66",
    "@types/react-dom": "^18.2.22",
    "@vitejs/plugin-react": "^4.0.0",
    "minimist": "^1.2.5",
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "typescript": "^5.8.2",
    "vite": "^7.3.1",
    "vite-plugin-static-copy": "^3.1.1"
  }
}
```

## File: `packages/extension/playwright.config.ts`
```typescript
/**
 * Copyright (c) Microsoft Corporation.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

import { defineConfig } from '@playwright/test';

import type { TestOptions } from '../playwright-mcp/tests/fixtures';

export default defineConfig<TestOptions>({
  testDir: './tests',
  fullyParallel: true,
  forbidOnly: !!process.env.CI,
  retries: process.env.CI ? 2 : 0,
  workers: process.env.CI ? 1 : undefined,
  reporter: 'list',
  projects: [
    { name: 'chromium', use: { mcpBrowser: 'chromium' } },
  ],
});
```

## File: `packages/extension/README.md`
```markdown
# Playwright MCP Chrome Extension

## Introduction

The Playwright MCP Chrome Extension allows you to connect to pages in your existing browser and leverage the state of your default user profile. This means the AI assistant can interact with websites where you're already logged in, using your existing cookies, sessions, and browser state, providing a seamless experience without requiring separate authentication or setup.

## Prerequisites

- Chrome/Edge/Chromium browser

## Installation Steps

### Install the Extension

Install [Playwright MCP Bridge](https://chromewebstore.google.com/detail/playwright-mcp-bridge/mmlmfjhmonkocbjadbfplnigmagldckm) from the Chrome Web Store.

### Configure Playwright MCP server

Configure Playwright MCP server to connect to the browser using the extension by passing the `--extension` option when running the MCP server:

```json
{
  "mcpServers": {
    "playwright-extension": {
      "command": "npx",
      "args": [
        "@playwright/mcp@latest",
        "--extension"
      ]
    }
  }
}
```

## Usage

### Browser Tab Selection

When the LLM interacts with the browser for the first time, it will load a page where you can select which browser tab the LLM will connect to. This allows you to control which specific page the AI assistant will interact with during the session.

### Bypassing the Connection Approval Dialog

By default, you'll need to approve each connection when the MCP server tries to connect to your browser. To bypass this approval dialog and allow automatic connections, you can use an authentication token.

#### Using Your Unique Authentication Token

1. After installing the extension, click on the extension icon or navigate to the extension's status page
2. Copy the `PLAYWRIGHT_MCP_EXTENSION_TOKEN` value displayed in the extension UI
3. Add it to your MCP server configuration:

```json
{
  "mcpServers": {
    "playwright-extension": {
      "command": "npx",
      "args": [
        "@playwright/mcp@latest",
        "--extension"
      ],
      "env": {
        "PLAYWRIGHT_MCP_EXTENSION_TOKEN": "your-token-here"
      }
    }
  }
}
```

This token is unique to your browser profile and provides secure authentication between the MCP server and the extension. Once configured, you won't need to manually approve connections each time.


```

## File: `packages/extension/tsconfig.json`
```json
{
  "compilerOptions": {
    "target": "ESNext",
    "esModuleInterop": true,
    "moduleResolution": "node",
    "strict": true,
    "module": "ESNext",
    "rootDir": "src",
    "outDir": "./dist/lib",
    "resolveJsonModule": true,
    "types": ["chrome"],
    "jsx": "react-jsx",
    "jsxImportSource": "react",
    "noEmit": true
  },
  "include": [
    "src",
  ],
  "exclude": [
    "src/ui",
  ]
}
```

## File: `packages/extension/tsconfig.ui.json`
```json
{
  "compilerOptions": {
    "target": "ESNext",
    "esModuleInterop": true,
    "moduleResolution": "node",
    "strict": true,
    "module": "ESNext",
    "rootDir": "src",
    "outDir": "./lib",
    "resolveJsonModule": true,
    "types": ["chrome"],
    "jsx": "react-jsx",
    "jsxImportSource": "react",
    "noEmit": true,
  },
  "include": [
    "src/ui",
  ],
}
```

## File: `packages/extension/vite.config.mts`
```
/**
 * Copyright (c) Microsoft Corporation.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

import { resolve } from 'path';
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import { viteStaticCopy } from 'vite-plugin-static-copy';

// Public key matching the Chrome Web Store listing — used to fix the extension ID across installs.
// Set SET_EXTENSION_PUBLIC_KEY_IN_MANIFEST=1 in release builds to inject it into the manifest.
const extensionPublicKey = 'MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAwRsUUO4mmbCi4JpmrIoIw31iVW9+xUJRZ6nSzya17PQkaUPDxe1IpgM+vpd/xB6mJWlJSyE1Lj95c0sbomGfVY1M0zUeKbaRVcAb+/a6m59gNR+ubFlmTX0nK9/8fE2FpRB9D+4N5jyeIPQuASW/0oswI2/ijK7hH5NTRX8gWc/ROMSgUj7rKhTAgBrICt/NsStgDPsxRTPPJnhJ/ViJtM1P5KsSYswE987DPoFnpmkFpq8g1ae0eYbQfXy55ieaacC4QWyJPj3daU2kMfBQw7MXnnk0H/WDxouMOIHnd8MlQxpEMqAihj7KpuONH+MUhuj9HEQo4df6bSaIuQ0b4QIDAQAB';

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    react(),
    viteStaticCopy({
      targets: [
        {
          src: '../../icons/*',
          dest: 'icons'
        },
        {
          src: '../../manifest.json',
          dest: '.',
          ...(!!process.env.SET_EXTENSION_PUBLIC_KEY_IN_MANIFEST ? {
            transform: (content: string) => {
              const manifest = JSON.parse(content);
              manifest.key = extensionPublicKey;
              return JSON.stringify(manifest, null, 2);
            }
          } : {})
        }
      ]
    })
  ],
  root: resolve(__dirname, 'src/ui'),
  build: {
    outDir: resolve(__dirname, 'dist/'),
    emptyOutDir: false,
    minify: false,
    rollupOptions: {
      input: ['src/ui/connect.html', 'src/ui/status.html'],
      output: {
        manualChunks: undefined,
        entryFileNames: 'lib/ui/[name].js',
        chunkFileNames: 'lib/ui/[name].js',
        assetFileNames: 'lib/ui/[name].[ext]'
      }
    }
  }
});
```

## File: `packages/extension/vite.sw.config.mts`
```
/**
 * Copyright (c) Microsoft Corporation.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

import { resolve } from 'path';
import { defineConfig } from 'vite';

export default defineConfig({
  build: {
    lib: {
      entry: resolve(__dirname, 'src/background.ts'),
      fileName: 'lib/background',
      formats: ['es']
    },
    outDir: 'dist',
    emptyOutDir: false,
    minify: false
  }
});
```

## File: `packages/extension/src/background.ts`
```typescript
/**
 * Copyright (c) Microsoft Corporation.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

import { RelayConnection, debugLog } from './relayConnection';

type PageMessage = {
  type: 'connectToMCPRelay';
  mcpRelayUrl: string;
} | {
  type: 'getTabs';
} | {
  type: 'connectToTab';
  tabId?: number;
  windowId?: number;
  mcpRelayUrl: string;
} | {
  type: 'getConnectionStatus';
} | {
  type: 'disconnect';
};

class TabShareExtension {
  private _activeConnection: RelayConnection | undefined;
  private _connectedTabId: number | null = null;
  private _pendingTabSelection = new Map<number, { connection: RelayConnection, timerId?: number }>();

  constructor() {
    chrome.tabs.onRemoved.addListener(this._onTabRemoved.bind(this));
    chrome.tabs.onUpdated.addListener(this._onTabUpdated.bind(this));
    chrome.tabs.onActivated.addListener(this._onTabActivated.bind(this));
    chrome.runtime.onMessage.addListener(this._onMessage.bind(this));
    chrome.action.onClicked.addListener(this._onActionClicked.bind(this));
  }

  // Promise-based message handling is not supported in Chrome: https://issues.chromium.org/issues/40753031
  private _onMessage(message: PageMessage, sender: chrome.runtime.MessageSender, sendResponse: (response: any) => void) {
    switch (message.type) {
      case 'connectToMCPRelay':
        this._connectToRelay(sender.tab!.id!, message.mcpRelayUrl).then(
            () => sendResponse({ success: true }),
            (error: any) => sendResponse({ success: false, error: error.message }));
        return true;
      case 'getTabs':
        this._getTabs().then(
            tabs => sendResponse({ success: true, tabs, currentTabId: sender.tab?.id }),
            (error: any) => sendResponse({ success: false, error: error.message }));
        return true;
      case 'connectToTab':
        const tabId = message.tabId || sender.tab?.id!;
        const windowId = message.windowId || sender.tab?.windowId!;
        this._connectTab(sender.tab!.id!, tabId, windowId, message.mcpRelayUrl!).then(
            () => sendResponse({ success: true }),
            (error: any) => sendResponse({ success: false, error: error.message }));
        return true; // Return true to indicate that the response will be sent asynchronously
      case 'getConnectionStatus':
        sendResponse({
          connectedTabId: this._connectedTabId
        });
        return false;
      case 'disconnect':
        this._disconnect().then(
            () => sendResponse({ success: true }),
            (error: any) => sendResponse({ success: false, error: error.message }));
        return true;
    }
    return false;
  }

  private async _connectToRelay(selectorTabId: number, mcpRelayUrl: string): Promise<void> {
    try {
      debugLog(`Connecting to relay at ${mcpRelayUrl}`);
      const socket = new WebSocket(mcpRelayUrl);
      await new Promise<void>((resolve, reject) => {
        socket.onopen = () => resolve();
        socket.onerror = () => reject(new Error('WebSocket error'));
        setTimeout(() => reject(new Error('Connection timeout')), 5000);
      });

      const connection = new RelayConnection(socket);
      connection.onclose = () => {
        debugLog('Connection closed');
        this._pendingTabSelection.delete(selectorTabId);
        // TODO: show error in the selector tab?
      };
      this._pendingTabSelection.set(selectorTabId, { connection });
      debugLog(`Connected to MCP relay`);
    } catch (error: any) {
      const message = `Failed to connect to MCP relay: ${error.message}`;
      debugLog(message);
      throw new Error(message);
    }
  }

  private async _connectTab(selectorTabId: number, tabId: number, windowId: number, mcpRelayUrl: string): Promise<void> {
    try {
      debugLog(`Connecting tab ${tabId} to relay at ${mcpRelayUrl}`);
      try {
        this._activeConnection?.close('Another connection is requested');
      } catch (error: any) {
        debugLog(`Error closing active connection:`, error);
      }
      await this._setConnectedTabId(null);

      this._activeConnection = this._pendingTabSelection.get(selectorTabId)?.connection;
      if (!this._activeConnection)
        throw new Error('No active MCP relay connection');
      this._pendingTabSelection.delete(selectorTabId);

      this._activeConnection.setTabId(tabId);
      this._activeConnection.onclose = () => {
        debugLog('MCP connection closed');
        this._activeConnection = undefined;
        void this._setConnectedTabId(null);
      };

      await Promise.all([
        this._setConnectedTabId(tabId),
        chrome.tabs.update(tabId, { active: true }),
        chrome.windows.update(windowId, { focused: true }),
      ]);
      debugLog(`Connected to MCP bridge`);
    } catch (error: any) {
      await this._setConnectedTabId(null);
      debugLog(`Failed to connect tab ${tabId}:`, error.message);
      throw error;
    }
  }

  private async _setConnectedTabId(tabId: number | null): Promise<void> {
    const oldTabId = this._connectedTabId;
    this._connectedTabId = tabId;
    if (oldTabId && oldTabId !== tabId)
      await this._updateBadge(oldTabId, { text: '' });
    if (tabId)
      await this._updateBadge(tabId, { text: '✓', color: '#4CAF50', title: 'Connected to MCP client' });
  }

  private async _updateBadge(tabId: number, { text, color, title }: { text: string; color?: string, title?: string }): Promise<void> {
    try {
      await chrome.action.setBadgeText({ tabId, text });
      await chrome.action.setTitle({ tabId, title: title || '' });
      if (color)
        await chrome.action.setBadgeBackgroundColor({ tabId, color });
    } catch (error: any) {
      // Ignore errors as the tab may be closed already.
    }
  }

  private async _onTabRemoved(tabId: number): Promise<void> {
    const pendingConnection = this._pendingTabSelection.get(tabId)?.connection;
    if (pendingConnection) {
      this._pendingTabSelection.delete(tabId);
      pendingConnection.close('Browser tab closed');
      return;
    }
    if (this._connectedTabId !== tabId)
      return;
    this._activeConnection?.close('Browser tab closed');
    this._activeConnection = undefined;
    this._connectedTabId = null;
  }

  private _onTabActivated(activeInfo: chrome.tabs.TabActiveInfo) {
    for (const [tabId, pending] of this._pendingTabSelection) {
      if (tabId === activeInfo.tabId) {
        if (pending.timerId) {
          clearTimeout(pending.timerId);
          pending.timerId = undefined;
        }
        continue;
      }
      if (!pending.timerId) {
        pending.timerId = setTimeout(() => {
          const existed = this._pendingTabSelection.delete(tabId);
          if (existed) {
            pending.connection.close('Tab has been inactive for 5 seconds');
            chrome.tabs.sendMessage(tabId, { type: 'connectionTimeout' });
          }
        }, 5000);
      }
    }
  }

  private _onTabUpdated(tabId: number, changeInfo: chrome.tabs.TabChangeInfo, tab: chrome.tabs.Tab) {
    if (this._connectedTabId === tabId)
      void this._setConnectedTabId(tabId);
  }

  private async _getTabs(): Promise<chrome.tabs.Tab[]> {
    const tabs = await chrome.tabs.query({});
    return tabs.filter(tab => tab.url && !['chrome:', 'edge:', 'devtools:'].some(scheme => tab.url!.startsWith(scheme)));
  }

  private async _onActionClicked(): Promise<void> {
    await chrome.tabs.create({
      url: chrome.runtime.getURL('status.html'),
      active: true
    });
  }

  private async _disconnect(): Promise<void> {
    this._activeConnection?.close('User disconnected');
    this._activeConnection = undefined;
    await this._setConnectedTabId(null);
  }
}

new TabShareExtension();
```

## File: `packages/extension/src/relayConnection.ts`
```typescript
/**
 * Copyright (c) Microsoft Corporation.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

export function debugLog(...args: unknown[]): void {
  const enabled = true;
  if (enabled) {
    // eslint-disable-next-line no-console
    console.log('[Extension]', ...args);
  }
}

type ProtocolCommand = {
  id: number;
  method: string;
  params?: any;
};

type ProtocolResponse = {
  id?: number;
  method?: string;
  params?: any;
  result?: any;
  error?: string;
};

export class RelayConnection {
  private _debuggee: chrome.debugger.Debuggee;
  private _ws: WebSocket;
  private _eventListener: (source: chrome.debugger.DebuggerSession, method: string, params: any) => void;
  private _detachListener: (source: chrome.debugger.Debuggee, reason: string) => void;
  private _tabPromise: Promise<void>;
  private _tabPromiseResolve!: () => void;
  private _closed = false;

  onclose?: () => void;

  constructor(ws: WebSocket) {
    this._debuggee = { };
    this._tabPromise = new Promise(resolve => this._tabPromiseResolve = resolve);
    this._ws = ws;
    this._ws.onmessage = this._onMessage.bind(this);
    this._ws.onclose = () => this._onClose();
    // Store listeners for cleanup
    this._eventListener = this._onDebuggerEvent.bind(this);
    this._detachListener = this._onDebuggerDetach.bind(this);
    chrome.debugger.onEvent.addListener(this._eventListener);
    chrome.debugger.onDetach.addListener(this._detachListener);
  }

  // Either setTabId or close is called after creating the connection.
  setTabId(tabId: number): void {
    this._debuggee = { tabId };
    this._tabPromiseResolve();
  }

  close(message: string): void {
    this._ws.close(1000, message);
    // ws.onclose is called asynchronously, so we call it here to avoid forwarding
    // CDP events to the closed connection.
    this._onClose();
  }

  private _onClose() {
    if (this._closed)
      return;
    this._closed = true;
    chrome.debugger.onEvent.removeListener(this._eventListener);
    chrome.debugger.onDetach.removeListener(this._detachListener);
    chrome.debugger.detach(this._debuggee).catch(() => {});
    this.onclose?.();
  }

  private _onDebuggerEvent(source: chrome.debugger.DebuggerSession, method: string, params: any): void {
    if (source.tabId !== this._debuggee.tabId)
      return;
    debugLog('Forwarding CDP event:', method, params);
    const sessionId = source.sessionId;
    this._sendMessage({
      method: 'forwardCDPEvent',
      params: {
        sessionId,
        method,
        params,
      },
    });
  }

  private _onDebuggerDetach(source: chrome.debugger.Debuggee, reason: string): void {
    if (source.tabId !== this._debuggee.tabId)
      return;
    this.close(`Debugger detached: ${reason}`);
    this._debuggee = { };
  }

  private _onMessage(event: MessageEvent): void {
    this._onMessageAsync(event).catch(e => debugLog('Error handling message:', e));
  }

  private async _onMessageAsync(event: MessageEvent): Promise<void> {
    let message: ProtocolCommand;
    try {
      message = JSON.parse(event.data);
    } catch (error: any) {
      debugLog('Error parsing message:', error);
      this._sendError(-32700, `Error parsing message: ${error.message}`);
      return;
    }

    debugLog('Received message:', message);

    const response: ProtocolResponse = {
      id: message.id,
    };
    try {
      response.result = await this._handleCommand(message);
    } catch (error: any) {
      debugLog('Error handling command:', error);
      response.error = error.message;
    }
    debugLog('Sending response:', response);
    this._sendMessage(response);
  }

  private async _handleCommand(message: ProtocolCommand): Promise<any> {
    if (message.method === 'attachToTab') {
      await this._tabPromise;
      debugLog('Attaching debugger to tab:', this._debuggee);
      await chrome.debugger.attach(this._debuggee, '1.3');
      const result: any = await chrome.debugger.sendCommand(this._debuggee, 'Target.getTargetInfo');
      return {
        targetInfo: result?.targetInfo,
      };
    }
    if (!this._debuggee.tabId)
      throw new Error('No tab is connected. Please go to the Playwright MCP extension and select the tab you want to connect to.');
    if (message.method === 'forwardCDPCommand') {
      const { sessionId, method, params } = message.params;
      debugLog('CDP command:', method, params);
      const debuggerSession: chrome.debugger.DebuggerSession = {
        ...this._debuggee,
        sessionId,
      };
      // Forward CDP command to chrome.debugger
      return await chrome.debugger.sendCommand(
          debuggerSession,
          method,
          params
      );
    }
  }

  private _sendError(code: number, message: string): void {
    this._sendMessage({
      error: {
        code,
        message,
      },
    });
  }

  private _sendMessage(message: any): void {
    if (this._ws.readyState === WebSocket.OPEN)
      this._ws.send(JSON.stringify(message));
  }
}
```

## File: `packages/extension/src/ui/authToken.css`
```css
/*
  Copyright (c) Microsoft Corporation.

  Licensed under the Apache License, Version 2.0 (the "License");
  you may not use this file except in compliance with the License.
  You may obtain a copy of the License at

      http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.
*/

.auth-token-section {
  margin: 16px 0;
  padding: 16px;
  background-color: #f6f8fa;
  border-radius: 6px;
}

.auth-token-description {
  font-size: 12px;
  color: #656d76;
  margin-bottom: 12px;
}

.auth-token-container {
  display: flex;
  align-items: center;
  gap: 8px;
  background-color: #ffffff;
  padding: 8px;
}

.auth-token-code {
  font-family: 'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, monospace;
  font-size: 12px;
  color: #1f2328;
  border: none;
  flex: 1;
  padding: 0;
  word-break: break-all;
}

.auth-token-refresh {
  flex: none;
  height: 24px;
  width: 24px;
  border: none;
  outline: none;
  color: var(--color-fg-muted);
  background: transparent;
  padding: 4px;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  border-radius: 4px;
}

.auth-token-refresh svg {
  margin: 0;
}

.auth-token-refresh:not(:disabled):hover {
  background-color: var(--color-btn-selected-bg);
}

.auth-token-example-section {
  margin-top: 16px;
}

.auth-token-example-toggle {
  display: flex;
  align-items: center;
  gap: 8px;
  background: none;
  border: none;
  padding: 8px 0;
  font-size: 12px;
  color: #656d76;
  cursor: pointer;
  outline: none;
  text-align: left;
  width: 100%;
}

.auth-token-example-toggle:hover {
  color: #1f2328;
}

.auth-token-chevron {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  transform: rotate(-90deg);
  flex-shrink: 0;
}

.auth-token-chevron.expanded {
  transform: rotate(0deg);
}

.auth-token-chevron svg {
  width: 12px;
  height: 12px;
}

.auth-token-chevron .octicon {
  margin: 0px;
}

.auth-token-example-content {
  margin-top: 12px;
  padding: 12px 0;
}

.auth-token-example-description {
  font-size: 12px;
  color: #656d76;
  margin-bottom: 12px;
}

.auth-token-example-config {
  display: flex;
  align-items: flex-start;
  gap: 8px;
  background-color: #ffffff;
  padding: 12px;
}

.auth-token-example-code {
  font-family: 'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, monospace;
  font-size: 11px;
  color: #1f2328;
  white-space: pre;
  flex: 1;
  line-height: 1.4;
}
```

## File: `packages/extension/src/ui/authToken.tsx`
```tsx
/**
 * Copyright (c) Microsoft Corporation.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

import React, { useCallback, useState } from 'react';
import { CopyToClipboard } from './copyToClipboard';
import * as icons from './icons';
import './authToken.css';

export const AuthTokenSection: React.FC<{}> = ({}) => {
  const [authToken, setAuthToken] = useState<string>(getOrCreateAuthToken);
  const [isExampleExpanded, setIsExampleExpanded] = useState<boolean>(false);

  const onRegenerateToken = useCallback(() => {
    const newToken = generateAuthToken();
    localStorage.setItem('auth-token', newToken);
    setAuthToken(newToken);
  }, []);

  const toggleExample = useCallback(() => {
    setIsExampleExpanded(!isExampleExpanded);
  }, [isExampleExpanded]);

  return (
    <div className='auth-token-section'>
      <div className='auth-token-description'>
        Set this environment variable to bypass the connection dialog:
      </div>
      <div className='auth-token-container'>
        <code className='auth-token-code'>{authTokenCode(authToken)}</code>
        <button className='auth-token-refresh' title='Generate new token' aria-label='Generate new token'onClick={onRegenerateToken}>{icons.refresh()}</button>
        <CopyToClipboard value={authTokenCode(authToken)} />
      </div>

      <div className='auth-token-example-section'>
        <button
          className='auth-token-example-toggle'
          onClick={toggleExample}
          aria-expanded={isExampleExpanded}
          title={isExampleExpanded ? 'Hide example config' : 'Show example config'}
        >
          <span className={`auth-token-chevron ${isExampleExpanded ? 'expanded' : ''}`}>
            {icons.chevronDown()}
          </span>
          Example MCP server configuration
        </button>

        {isExampleExpanded && (
          <div className='auth-token-example-content'>
            <div className='auth-token-example-description'>
              Add this configuration to your MCP client (e.g., VS Code) to connect to the Playwright MCP Bridge:
            </div>
            <div className='auth-token-example-config'>
              <code className='auth-token-example-code'>{exampleConfig(authToken)}</code>
              <CopyToClipboard value={exampleConfig(authToken)} />
            </div>
          </div>
        )}
      </div>
    </div>
  );
};

function authTokenCode(authToken: string) {
  return `PLAYWRIGHT_MCP_EXTENSION_TOKEN=${authToken}`;
}

function exampleConfig(authToken: string) {
  return `{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": ["@playwright/mcp@latest", "--extension"],
      "env": {
        "PLAYWRIGHT_MCP_EXTENSION_TOKEN":
          "${authToken}"
      }
    }
  }
}`;
}

function generateAuthToken(): string {
  // Generate a cryptographically secure random token
  const array = new Uint8Array(32);
  crypto.getRandomValues(array);
  // Convert to base64 and make it URL-safe
  return btoa(String.fromCharCode.apply(null, Array.from(array)))
      .replace(/[+/=]/g, match => {
        switch (match) {
          case '+': return '-';
          case '/': return '_';
          case '=': return '';
          default: return match;
        }
      });
}

export const getOrCreateAuthToken = (): string => {
  let token = localStorage.getItem('auth-token');
  if (!token) {
    token = generateAuthToken();
    localStorage.setItem('auth-token', token);
  }
  return token;
}
```

## File: `packages/extension/src/ui/colors.css`
```css
/* The MIT License (MIT)

Copyright (c) 2021 GitHub Inc.

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
SOFTWARE. */

:root {
  --color-canvas-default-transparent: rgba(255,255,255,0);
  --color-marketing-icon-primary: #218bff;
  --color-marketing-icon-secondary: #54aeff;
  --color-diff-blob-addition-num-text: #24292f;
  --color-diff-blob-addition-fg: #24292f;
  --color-diff-blob-addition-num-bg: #CCFFD8;
  --color-diff-blob-addition-line-bg: #E6FFEC;
  --color-diff-blob-addition-word-bg: #ABF2BC;
  --color-diff-blob-deletion-num-text: #24292f;
  --color-diff-blob-deletion-fg: #24292f;
  --color-diff-blob-deletion-num-bg: #FFD7D5;
  --color-diff-blob-deletion-line-bg: #FFEBE9;
  --color-diff-blob-deletion-word-bg: rgba(255,129,130,0.4);
  --color-diff-blob-hunk-num-bg: rgba(84,174,255,0.4);
  --color-diff-blob-expander-icon: #57606a;
  --color-diff-blob-selected-line-highlight-mix-blend-mode: multiply;
  --color-diffstat-deletion-border: rgba(27,31,36,0.15);
  --color-diffstat-addition-border: rgba(27,31,36,0.15);
  --color-diffstat-addition-bg: #2da44e;
  --color-search-keyword-hl: #fff8c5;
  --color-prettylights-syntax-comment: #6e7781;
  --color-prettylights-syntax-constant: #0550ae;
  --color-prettylights-syntax-entity: #8250df;
  --color-prettylights-syntax-storage-modifier-import: #24292f;
  --color-prettylights-syntax-entity-tag: #116329;
  --color-prettylights-syntax-keyword: #cf222e;
  --color-prettylights-syntax-string: #0a3069;
  --color-prettylights-syntax-variable: #953800;
  --color-prettylights-syntax-brackethighlighter-unmatched: #82071e;
  --color-prettylights-syntax-invalid-illegal-text: #f6f8fa;
  --color-prettylights-syntax-invalid-illegal-bg: #82071e;
  --color-prettylights-syntax-carriage-return-text: #f6f8fa;
  --color-prettylights-syntax-carriage-return-bg: #cf222e;
  --color-prettylights-syntax-string-regexp: #116329;
  --color-prettylights-syntax-markup-list: #3b2300;
  --color-prettylights-syntax-markup-heading: #0550ae;
  --color-prettylights-syntax-markup-italic: #24292f;
  --color-prettylights-syntax-markup-bold: #24292f;
  --color-prettylights-syntax-markup-deleted-text: #82071e;
  --color-prettylights-syntax-markup-deleted-bg: #FFEBE9;
  --color-prettylights-syntax-markup-inserted-text: #116329;
  --color-prettylights-syntax-markup-inserted-bg: #dafbe1;
  --color-prettylights-syntax-markup-changed-text: #953800;
  --color-prettylights-syntax-markup-changed-bg: #ffd8b5;
  --color-prettylights-syntax-markup-ignored-text: #eaeef2;
  --color-prettylights-syntax-markup-ignored-bg: #0550ae;
  --color-prettylights-syntax-meta-diff-range: #8250df;
  --color-prettylights-syntax-brackethighlighter-angle: #57606a;
  --color-prettylights-syntax-sublimelinter-gutter-mark: #8c959f;
  --color-prettylights-syntax-constant-other-reference-link: #0a3069;
  --color-codemirror-text: #24292f;
  --color-codemirror-bg: #ffffff;
  --color-codemirror-gutters-bg: #ffffff;
  --color-codemirror-guttermarker-text: #ffffff;
  --color-codemirror-guttermarker-subtle-text: #6e7781;
  --color-codemirror-linenumber-text: #57606a;
  --color-codemirror-cursor: #24292f;
  --color-codemirror-selection-bg: rgba(84,174,255,0.4);
  --color-codemirror-activeline-bg: rgba(234,238,242,0.5);
  --color-codemirror-matchingbracket-text: #24292f;
  --color-codemirror-lines-bg: #ffffff;
  --color-codemirror-syntax-comment: #24292f;
  --color-codemirror-syntax-constant: #0550ae;
  --color-codemirror-syntax-entity: #8250df;
  --color-codemirror-syntax-keyword: #cf222e;
  --color-codemirror-syntax-storage: #cf222e;
  --color-codemirror-syntax-string: #0a3069;
  --color-codemirror-syntax-support: #0550ae;
  --color-codemirror-syntax-variable: #953800;
  --color-checks-bg: #24292f;
  --color-checks-run-border-width: 0px;
  --color-checks-container-border-width: 0px;
  --color-checks-text-primary: #f6f8fa;
  --color-checks-text-secondary: #8c959f;
  --color-checks-text-link: #54aeff;
  --color-checks-btn-icon: #afb8c1;
  --color-checks-btn-hover-icon: #f6f8fa;
  --color-checks-btn-hover-bg: rgba(255,255,255,0.125);
  --color-checks-input-text: #eaeef2;
  --color-checks-input-placeholder-text: #8c959f;
  --color-checks-input-focus-text: #8c959f;
  --color-checks-input-bg: #32383f;
  --color-checks-input-shadow: none;
  --color-checks-donut-error: #fa4549;
  --color-checks-donut-pending: #bf8700;
  --color-checks-donut-success: #2da44e;
  --color-checks-donut-neutral: #afb8c1;
  --color-checks-dropdown-text: #afb8c1;
  --color-checks-dropdown-bg: #32383f;
  --color-checks-dropdown-border: #424a53;
  --color-checks-dropdown-shadow: rgba(27,31,36,0.3);
  --color-checks-dropdown-hover-text: #f6f8fa;
  --color-checks-dropdown-hover-bg: #424a53;
  --color-checks-dropdown-btn-hover-text: #f6f8fa;
  --color-checks-dropdown-btn-hover-bg: #32383f;
  --color-checks-scrollbar-thumb-bg: #57606a;
  --color-checks-header-label-text: #d0d7de;
  --color-checks-header-label-open-text: #f6f8fa;
  --color-checks-header-border: #32383f;
  --color-checks-header-icon: #8c959f;
  --color-checks-line-text: #d0d7de;
  --color-checks-line-num-text: rgba(140,149,159,0.75);
  --color-checks-line-timestamp-text: #8c959f;
  --color-checks-line-hover-bg: #32383f;
  --color-checks-line-selected-bg: rgba(33,139,255,0.15);
  --color-checks-line-selected-num-text: #54aeff;
  --color-checks-line-dt-fm-text: #24292f;
  --color-checks-line-dt-fm-bg: #9a6700;
  --color-checks-gate-bg: rgba(125,78,0,0.15);
  --color-checks-gate-text: #d0d7de;
  --color-checks-gate-waiting-text: #afb8c1;
  --color-checks-step-header-open-bg: #32383f;
  --color-checks-step-error-text: #ff8182;
  --color-checks-step-warning-text: #d4a72c;
  --color-checks-logline-text: #8c959f;
  --color-checks-logline-num-text: rgba(140,149,159,0.75);
  --color-checks-logline-debug-text: #c297ff;
  --color-checks-logline-error-text: #d0d7de;
  --color-checks-logline-error-num-text: #ff8182;
  --color-checks-logline-error-bg: rgba(164,14,38,0.15);
  --color-checks-logline-warning-text: #d0d7de;
  --color-checks-logline-warning-num-text: #d4a72c;
  --color-checks-logline-warning-bg: rgba(125,78,0,0.15);
  --color-checks-logline-command-text: #54aeff;
  --color-checks-logline-section-text: #4ac26b;
  --color-checks-ansi-black: #24292f;
  --color-checks-ansi-black-bright: #32383f;
  --color-checks-ansi-white: #d0d7de;
  --color-checks-ansi-white-bright: #d0d7de;
  --color-checks-ansi-gray: #8c959f;
  --color-checks-ansi-red: #ff8182;
  --color-checks-ansi-red-bright: #ffaba8;
  --color-checks-ansi-green: #4ac26b;
  --color-checks-ansi-green-bright: #6fdd8b;
  --color-checks-ansi-yellow: #d4a72c;
  --color-checks-ansi-yellow-bright: #eac54f;
  --color-checks-ansi-blue: #54aeff;
  --color-checks-ansi-blue-bright: #80ccff;
  --color-checks-ansi-magenta: #c297ff;
  --color-checks-ansi-magenta-bright: #d8b9ff;
  --color-checks-ansi-cyan: #76e3ea;
  --color-checks-ansi-cyan-bright: #b3f0ff;
  --color-project-header-bg: #24292f;
  --color-project-sidebar-bg: #ffffff;
  --color-project-gradient-in: #ffffff;
  --color-project-gradient-out: rgba(255,255,255,0);
  --color-mktg-success: rgba(36,146,67,1);
  --color-mktg-info: rgba(19,119,234,1);
  --color-mktg-bg-shade-gradient-top: rgba(27,31,36,0.065);
  --color-mktg-bg-shade-gradient-bottom: rgba(27,31,36,0);
  --color-mktg-btn-bg-top: hsla(228,82%,66%,1);
  --color-mktg-btn-bg-bottom: #4969ed;
  --color-mktg-btn-bg-overlay-top: hsla(228,74%,59%,1);
  --color-mktg-btn-bg-overlay-bottom: #3355e0;
  --color-mktg-btn-text: #ffffff;
  --color-mktg-btn-primary-bg-top: hsla(137,56%,46%,1);
  --color-mktg-btn-primary-bg-bottom: #2ea44f;
  --color-mktg-btn-primary-bg-overlay-top: hsla(134,60%,38%,1);
  --color-mktg-btn-primary-bg-overlay-bottom: #22863a;
  --color-mktg-btn-primary-text: #ffffff;
  --color-mktg-btn-enterprise-bg-top: hsla(249,100%,72%,1);
  --color-mktg-btn-enterprise-bg-bottom: #6f57ff;
  --color-mktg-btn-enterprise-bg-overlay-top: hsla(248,65%,63%,1);
  --color-mktg-btn-enterprise-bg-overlay-bottom: #614eda;
  --color-mktg-btn-enterprise-text: #ffffff;
  --color-mktg-btn-outline-text: #4969ed;
  --color-mktg-btn-outline-border: rgba(73,105,237,0.3);
  --color-mktg-btn-outline-hover-text: #3355e0;
  --color-mktg-btn-outline-hover-border: rgba(51,85,224,0.5);
  --color-mktg-btn-outline-focus-border: #4969ed;
  --color-mktg-btn-outline-focus-border-inset: rgba(73,105,237,0.5);
  --color-mktg-btn-dark-text: #ffffff;
  --color-mktg-btn-dark-border: rgba(255,255,255,0.3);
  --color-mktg-btn-dark-hover-text: #ffffff;
  --color-mktg-btn-dark-hover-border: rgba(255,255,255,0.5);
  --color-mktg-btn-dark-focus-border: #ffffff;
  --color-mktg-btn-dark-focus-border-inset: rgba(255,255,255,0.5);
  --color-avatar-bg: #ffffff;
  --color-avatar-border: rgba(27,31,36,0.15);
  --color-avatar-stack-fade: #afb8c1;
  --color-avatar-stack-fade-more: #d0d7de;
  --color-avatar-child-shadow: -2px -2px 0 rgba(255,255,255,0.8);
  --color-topic-tag-border: rgba(0,0,0,0);
  --color-select-menu-backdrop-border: rgba(0,0,0,0);
  --color-select-menu-tap-highlight: rgba(175,184,193,0.5);
  --color-select-menu-tap-focus-bg: #b6e3ff;
  --color-overlay-shadow: 0 1px 3px rgba(27,31,36,0.12), 0 8px 24px rgba(66,74,83,0.12);
  --color-header-text: rgba(255,255,255,0.7);
  --color-header-bg: #24292f;
  --color-header-logo: #ffffff;
  --color-header-search-bg: #24292f;
  --color-header-search-border: #57606a;
  --color-sidenav-selected-bg: #ffffff;
  --color-menu-bg-active: rgba(0,0,0,0);
  --color-control-transparent-bg-hover: #818b981a;
  --color-input-disabled-bg: rgba(175,184,193,0.2);
  --color-timeline-badge-bg: #eaeef2;
  --color-ansi-black: #24292f;
  --color-ansi-black-bright: #57606a;
  --color-ansi-white: #6e7781;
  --color-ansi-white-bright: #8c959f;
  --color-ansi-gray: #6e7781;
  --color-ansi-red: #cf222e;
  --color-ansi-red-bright: #a40e26;
  --color-ansi-green: #116329;
  --color-ansi-green-bright: #1a7f37;
  --color-ansi-yellow: #4d2d00;
  --color-ansi-yellow-bright: #633c01;
  --color-ansi-blue: #0969da;
  --color-ansi-blue-bright: #218bff;
  --color-ansi-magenta: #8250df;
  --color-ansi-magenta-bright: #a475f9;
  --color-ansi-cyan: #1b7c83;
  --color-ansi-cyan-bright: #3192aa;
  --color-btn-text: #24292f;
  --color-btn-bg: #f6f8fa;
  --color-btn-border: rgba(27,31,36,0.15);
  --color-btn-shadow: 0 1px 0 rgba(27,31,36,0.04);
  --color-btn-inset-shadow: inset 0 1px 0 rgba(255,255,255,0.25);
  --color-btn-hover-bg: #f3f4f6;
  --color-btn-hover-border: rgba(27,31,36,0.15);
  --color-btn-active-bg: hsla(220,14%,93%,1);
  --color-btn-active-border: rgba(27,31,36,0.15);
  --color-btn-selected-bg: hsla(220,14%,94%,1);
  --color-btn-focus-bg: #f6f8fa;
  --color-btn-focus-border: rgba(27,31,36,0.15);
  --color-btn-focus-shadow: 0 0 0 3px rgba(9,105,218,0.3);
  --color-btn-shadow-active: inset 0 0.15em 0.3em rgba(27,31,36,0.15);
  --color-btn-shadow-input-focus: 0 0 0 0.2em rgba(9,105,218,0.3);
  --color-btn-counter-bg: rgba(27,31,36,0.08);
  --color-btn-primary-text: #ffffff;
  --color-btn-primary-bg: #2da44e;
  --color-btn-primary-border: rgba(27,31,36,0.15);
  --color-btn-primary-shadow: 0 1px 0 rgba(27,31,36,0.1);
  --color-btn-primary-inset-shadow: inset 0 1px 0 rgba(255,255,255,0.03);
  --color-btn-primary-hover-bg: #2c974b;
  --color-btn-primary-hover-border: rgba(27,31,36,0.15);
  --color-btn-primary-selected-bg: hsla(137,55%,36%,1);
  --color-btn-primary-selected-shadow: inset 0 1px 0 rgba(0,45,17,0.2);
  --color-btn-primary-disabled-text: rgba(255,255,255,0.8);
  --color-btn-primary-disabled-bg: #94d3a2;
  --color-btn-primary-disabled-border: rgba(27,31,36,0.15);
  --color-btn-primary-focus-bg: #2da44e;
  --color-btn-primary-focus-border: rgba(27,31,36,0.15);
  --color-btn-primary-focus-shadow: 0 0 0 3px rgba(45,164,78,0.4);
  --color-btn-primary-icon: rgba(255,255,255,0.8);
  --color-btn-primary-counter-bg: rgba(255,255,255,0.2);
  --color-btn-outline-text: #0969da;
  --color-btn-outline-hover-text: #ffffff;
  --color-btn-outline-hover-bg: #0969da;
  --color-btn-outline-hover-border: rgba(27,31,36,0.15);
  --color-btn-outline-hover-shadow: 0 1px 0 rgba(27,31,36,0.1);
  --color-btn-outline-hover-inset-shadow: inset 0 1px 0 rgba(255,255,255,0.03);
  --color-btn-outline-hover-counter-bg: rgba(255,255,255,0.2);
  --color-btn-outline-selected-text: #ffffff;
  --color-btn-outline-selected-bg: hsla(212,92%,42%,1);
  --color-btn-outline-selected-border: rgba(27,31,36,0.15);
  --color-btn-outline-selected-shadow: inset 0 1px 0 rgba(0,33,85,0.2);
  --color-btn-outline-disabled-text: rgba(9,105,218,0.5);
  --color-btn-outline-disabled-bg: #f6f8fa;
  --color-btn-outline-disabled-counter-bg: rgba(9,105,218,0.05);
  --color-btn-outline-focus-border: rgba(27,31,36,0.15);
  --color-btn-outline-focus-shadow: 0 0 0 3px rgba(5,80,174,0.4);
  --color-btn-outline-counter-bg: rgba(9,105,218,0.1);
  --color-btn-danger-text: #cf222e;
  --color-btn-danger-hover-text: #ffffff;
  --color-btn-danger-hover-bg: #a40e26;
  --color-btn-danger-hover-border: rgba(27,31,36,0.15);
  --color-btn-danger-hover-shadow: 0 1px 0 rgba(27,31,36,0.1);
  --color-btn-danger-hover-inset-shadow: inset 0 1px 0 rgba(255,255,255,0.03);
  --color-btn-danger-hover-counter-bg: rgba(255,255,255,0.2);
  --color-btn-danger-selected-text: #ffffff;
  --color-btn-danger-selected-bg: hsla(356,72%,44%,1);
  --color-btn-danger-selected-border: rgba(27,31,36,0.15);
  --color-btn-danger-selected-shadow: inset 0 1px 0 rgba(76,0,20,0.2);
  --color-btn-danger-disabled-text: rgba(207,34,46,0.5);
  --color-btn-danger-disabled-bg: #f6f8fa;
  --color-btn-danger-disabled-counter-bg: rgba(207,34,46,0.05);
  --color-btn-danger-focus-border: rgba(27,31,36,0.15);
  --color-btn-danger-focus-shadow: 0 0 0 3px rgba(164,14,38,0.4);
  --color-btn-danger-counter-bg: rgba(207,34,46,0.1);
  --color-btn-danger-icon: #cf222e;
  --color-btn-danger-hover-icon: #ffffff;
  --color-underlinenav-icon: #6e7781;
  --color-underlinenav-border-hover: rgba(175,184,193,0.2);
  --color-fg-default: #24292f;
  --color-fg-muted: #57606a;
  --color-fg-subtle: #6e7781;
  --color-fg-on-emphasis: #ffffff;
  --color-canvas-default: #ffffff;
  --color-canvas-overlay: #ffffff;
  --color-canvas-inset: #f6f8fa;
  --color-canvas-subtle: #f6f8fa;
  --color-border-default: #d0d7de;
  --color-border-muted: hsla(210,18%,87%,1);
  --color-border-subtle: rgba(27,31,36,0.15);
  --color-shadow-small: 0 1px 0 rgba(27,31,36,0.04);
  --color-shadow-medium: 0 3px 6px rgba(140,149,159,0.15);
  --color-shadow-large: 0 8px 24px rgba(140,149,159,0.2);
  --color-shadow-extra-large: 0 12px 28px rgba(140,149,159,0.3);
  --color-neutral-emphasis-plus: #24292f;
  --color-neutral-emphasis: #6e7781;
  --color-neutral-muted: rgba(175,184,193,0.2);
  --color-neutral-subtle: rgba(234,238,242,0.5);
  --color-accent-fg: #0969da;
  --color-accent-emphasis: #0969da;
  --color-accent-muted: rgba(84,174,255,0.4);
  --color-accent-subtle: #ddf4ff;
  --color-success-fg: #1a7f37;
  --color-success-emphasis: #2da44e;
  --color-success-muted: rgba(74,194,107,0.4);
  --color-success-subtle: #dafbe1;
  --color-attention-fg: #9a6700;
  --color-attention-emphasis: #bf8700;
  --color-attention-muted: rgba(212,167,44,0.4);
  --color-attention-subtle: #fff8c5;
  --color-severe-fg: #bc4c00;
  --color-severe-emphasis: #bc4c00;
  --color-severe-muted: rgba(251,143,68,0.4);
  --color-severe-subtle: #fff1e5;
  --color-danger-fg: #cf222e;
  --color-danger-emphasis: #cf222e;
  --color-danger-muted: rgba(255,129,130,0.4);
  --color-danger-subtle: #FFEBE9;
  --color-done-fg: #8250df;
  --color-done-emphasis: #8250df;
  --color-done-muted: rgba(194,151,255,0.4);
  --color-done-subtle: #fbefff;
  --color-sponsors-fg: #bf3989;
  --color-sponsors-emphasis: #bf3989;
  --color-sponsors-muted: rgba(255,128,200,0.4);
  --color-sponsors-subtle: #ffeff7;
  --color-primer-canvas-backdrop: rgba(27,31,36,0.5);
  --color-primer-canvas-sticky: rgba(255,255,255,0.95);
  --color-primer-border-active: #FD8C73;
  --color-primer-border-contrast: rgba(27,31,36,0.1);
  --color-primer-shadow-highlight: inset 0 1px 0 rgba(255,255,255,0.25);
  --color-primer-shadow-inset: inset 0 1px 0 rgba(208,215,222,0.2);
  --color-primer-shadow-focus: 0 0 0 3px rgba(9,105,218,0.3);
  --color-scale-black: #1b1f24;
  --color-scale-white: #ffffff;
  --color-scale-gray-0: #f6f8fa;
  --color-scale-gray-1: #eaeef2;
  --color-scale-gray-2: #d0d7de;
  --color-scale-gray-3: #afb8c1;
  --color-scale-gray-4: #8c959f;
  --color-scale-gray-5: #6e7781;
  --color-scale-gray-6: #57606a;
  --color-scale-gray-7: #424a53;
  --color-scale-gray-8: #32383f;
  --color-scale-gray-9: #24292f;
  --color-scale-blue-0: #ddf4ff;
  --color-scale-blue-1: #b6e3ff;
  --color-scale-blue-2: #80ccff;
  --color-scale-blue-3: #54aeff;
  --color-scale-blue-4: #218bff;
  --color-scale-blue-5: #0969da;
  --color-scale-blue-6: #0550ae;
  --color-scale-blue-7: #033d8b;
  --color-scale-blue-8: #0a3069;
  --color-scale-blue-9: #002155;
  --color-scale-green-0: #dafbe1;
  --color-scale-green-1: #aceebb;
  --color-scale-green-2: #6fdd8b;
  --color-scale-green-3: #4ac26b;
  --color-scale-green-4: #2da44e;
  --color-scale-green-5: #1a7f37;
  --color-scale-green-6: #116329;
  --color-scale-green-7: #044f1e;
  --color-scale-green-8: #003d16;
  --color-scale-green-9: #002d11;
  --color-scale-yellow-0: #fff8c5;
  --color-scale-yellow-1: #fae17d;
  --color-scale-yellow-2: #eac54f;
  --color-scale-yellow-3: #d4a72c;
  --color-scale-yellow-4: #bf8700;
  --color-scale-yellow-5: #9a6700;
  --color-scale-yellow-6: #7d4e00;
  --color-scale-yellow-7: #633c01;
  --color-scale-yellow-8: #4d2d00;
  --color-scale-yellow-9: #3b2300;
  --color-scale-orange-0: #fff1e5;
  --color-scale-orange-1: #ffd8b5;
  --color-scale-orange-2: #ffb77c;
  --color-scale-orange-3: #fb8f44;
  --color-scale-orange-4: #e16f24;
  --color-scale-orange-5: #bc4c00;
  --color-scale-orange-6: #953800;
  --color-scale-orange-7: #762c00;
  --color-scale-orange-8: #5c2200;
  --color-scale-orange-9: #471700;
  --color-scale-red-0: #FFEBE9;
  --color-scale-red-1: #ffcecb;
  --color-scale-red-2: #ffaba8;
  --color-scale-red-3: #ff8182;
  --color-scale-red-4: #fa4549;
  --color-scale-red-5: #cf222e;
  --color-scale-red-6: #a40e26;
  --color-scale-red-7: #82071e;
  --color-scale-red-8: #660018;
  --color-scale-red-9: #4c0014;
  --color-scale-purple-0: #fbefff;
  --color-scale-purple-1: #ecd8ff;
  --color-scale-purple-2: #d8b9ff;
  --color-scale-purple-3: #c297ff;
  --color-scale-purple-4: #a475f9;
  --color-scale-purple-5: #8250df;
  --color-scale-purple-6: #6639ba;
  --color-scale-purple-7: #512a97;
  --color-scale-purple-8: #3e1f79;
  --color-scale-purple-9: #2e1461;
  --color-scale-pink-0: #ffeff7;
  --color-scale-pink-1: #ffd3eb;
  --color-scale-pink-2: #ffadda;
  --color-scale-pink-3: #ff80c8;
  --color-scale-pink-4: #e85aad;
  --color-scale-pink-5: #bf3989;
  --color-scale-pink-6: #99286e;
  --color-scale-pink-7: #772057;
  --color-scale-pink-8: #611347;
  --color-scale-pink-9: #4d0336;
  --color-scale-coral-0: #FFF0EB;
  --color-scale-coral-1: #FFD6CC;
  --color-scale-coral-2: #FFB4A1;
  --color-scale-coral-3: #FD8C73;
  --color-scale-coral-4: #EC6547;
  --color-scale-coral-5: #C4432B;
  --color-scale-coral-6: #9E2F1C;
  --color-scale-coral-7: #801F0F;
  --color-scale-coral-8: #691105;
  --color-scale-coral-9: #510901
}

@media(prefers-color-scheme: dark) {
  :root {
    --color-canvas-default-transparent: rgba(13,17,23,0);
    --color-marketing-icon-primary: #79c0ff;
    --color-marketing-icon-secondary: #1f6feb;
    --color-diff-blob-addition-num-text: #c9d1d9;
    --color-diff-blob-addition-fg: #c9d1d9;
    --color-diff-blob-addition-num-bg: rgba(63,185,80,0.3);
    --color-diff-blob-addition-line-bg: rgba(46,160,67,0.15);
    --color-diff-blob-addition-word-bg: rgba(46,160,67,0.4);
    --color-diff-blob-deletion-num-text: #c9d1d9;
    --color-diff-blob-deletion-fg: #c9d1d9;
    --color-diff-blob-deletion-num-bg: rgba(248,81,73,0.3);
    --color-diff-blob-deletion-line-bg: rgba(248,81,73,0.15);
    --color-diff-blob-deletion-word-bg: rgba(248,81,73,0.4);
    --color-diff-blob-hunk-num-bg: rgba(56,139,253,0.4);
    --color-diff-blob-expander-icon: #8b949e;
    --color-diff-blob-selected-line-highlight-mix-blend-mode: screen;
    --color-diffstat-deletion-border: rgba(240,246,252,0.1);
    --color-diffstat-addition-border: rgba(240,246,252,0.1);
    --color-diffstat-addition-bg: #3fb950;
    --color-search-keyword-hl: rgba(210,153,34,0.4);
    --color-prettylights-syntax-comment: #8b949e;
    --color-prettylights-syntax-constant: #79c0ff;
    --color-prettylights-syntax-entity: #d2a8ff;
    --color-prettylights-syntax-storage-modifier-import: #c9d1d9;
    --color-prettylights-syntax-entity-tag: #7ee787;
    --color-prettylights-syntax-keyword: #ff7b72;
    --color-prettylights-syntax-string: #a5d6ff;
    --color-prettylights-syntax-variable: #ffa657;
    --color-prettylights-syntax-brackethighlighter-unmatched: #f85149;
    --color-prettylights-syntax-invalid-illegal-text: #f0f6fc;
    --color-prettylights-syntax-invalid-illegal-bg: #8e1519;
    --color-prettylights-syntax-carriage-return-text: #f0f6fc;
    --color-prettylights-syntax-carriage-return-bg: #b62324;
    --color-prettylights-syntax-string-regexp: #7ee787;
    --color-prettylights-syntax-markup-list: #f2cc60;
    --color-prettylights-syntax-markup-heading: #1f6feb;
    --color-prettylights-syntax-markup-italic: #c9d1d9;
    --color-prettylights-syntax-markup-bold: #c9d1d9;
    --color-prettylights-syntax-markup-deleted-text: #ffdcd7;
    --color-prettylights-syntax-markup-deleted-bg: #67060c;
    --color-prettylights-syntax-markup-inserted-text: #aff5b4;
    --color-prettylights-syntax-markup-inserted-bg: #033a16;
    --color-prettylights-syntax-markup-changed-text: #ffdfb6;
    --color-prettylights-syntax-markup-changed-bg: #5a1e02;
    --color-prettylights-syntax-markup-ignored-text: #c9d1d9;
    --color-prettylights-syntax-markup-ignored-bg: #1158c7;
    --color-prettylights-syntax-meta-diff-range: #d2a8ff;
    --color-prettylights-syntax-brackethighlighter-angle: #8b949e;
    --color-prettylights-syntax-sublimelinter-gutter-mark: #484f58;
    --color-prettylights-syntax-constant-other-reference-link: #a5d6ff;
    --color-codemirror-text: #c9d1d9;
    --color-codemirror-bg: #0d1117;
    --color-codemirror-gutters-bg: #0d1117;
    --color-codemirror-guttermarker-text: #0d1117;
    --color-codemirror-guttermarker-subtle-text: #484f58;
    --color-codemirror-linenumber-text: #8b949e;
    --color-codemirror-cursor: #c9d1d9;
    --color-codemirror-selection-bg: rgba(56,139,253,0.4);
    --color-codemirror-activeline-bg: rgba(110,118,129,0.1);
    --color-codemirror-matchingbracket-text: #c9d1d9;
    --color-codemirror-lines-bg: #0d1117;
    --color-codemirror-syntax-comment: #8b949e;
    --color-codemirror-syntax-constant: #79c0ff;
    --color-codemirror-syntax-entity: #d2a8ff;
    --color-codemirror-syntax-keyword: #ff7b72;
    --color-codemirror-syntax-storage: #ff7b72;
    --color-codemirror-syntax-string: #a5d6ff;
    --color-codemirror-syntax-support: #79c0ff;
    --color-codemirror-syntax-variable: #ffa657;
    --color-checks-bg: #010409;
    --color-checks-run-border-width: 1px;
    --color-checks-container-border-width: 1px;
    --color-checks-text-primary: #c9d1d9;
    --color-checks-text-secondary: #8b949e;
    --color-checks-text-link: #58a6ff;
    --color-checks-btn-icon: #8b949e;
    --color-checks-btn-hover-icon: #c9d1d9;
    --color-checks-btn-hover-bg: rgba(110,118,129,0.1);
    --color-checks-input-text: #8b949e;
    --color-checks-input-placeholder-text: #484f58;
    --color-checks-input-focus-text: #c9d1d9;
    --color-checks-input-bg: #161b22;
    --color-checks-input-shadow: none;
    --color-checks-donut-error: #f85149;
    --color-checks-donut-pending: #d29922;
    --color-checks-donut-success: #2ea043;
    --color-checks-donut-neutral: #8b949e;
    --color-checks-dropdown-text: #c9d1d9;
    --color-checks-dropdown-bg: #161b22;
    --color-checks-dropdown-border: #30363d;
    --color-checks-dropdown-shadow: rgba(1,4,9,0.3);
    --color-checks-dropdown-hover-text: #c9d1d9;
    --color-checks-dropdown-hover-bg: rgba(110,118,129,0.1);
    --color-checks-dropdown-btn-hover-text: #c9d1d9;
    --color-checks-dropdown-btn-hover-bg: rgba(110,118,129,0.1);
    --color-checks-scrollbar-thumb-bg: rgba(110,118,129,0.4);
    --color-checks-header-label-text: #8b949e;
    --color-checks-header-label-open-text: #c9d1d9;
    --color-checks-header-border: #21262d;
    --color-checks-header-icon: #8b949e;
    --color-checks-line-text: #8b949e;
    --color-checks-line-num-text: #484f58;
    --color-checks-line-timestamp-text: #484f58;
    --color-checks-line-hover-bg: rgba(110,118,129,0.1);
    --color-checks-line-selected-bg: rgba(56,139,253,0.15);
    --color-checks-line-selected-num-text: #58a6ff;
    --color-checks-line-dt-fm-text: #f0f6fc;
    --color-checks-line-dt-fm-bg: #9e6a03;
    --color-checks-gate-bg: rgba(187,128,9,0.15);
    --color-checks-gate-text: #8b949e;
    --color-checks-gate-waiting-text: #d29922;
    --color-checks-step-header-open-bg: #161b22;
    --color-checks-step-error-text: #f85149;
    --color-checks-step-warning-text: #d29922;
    --color-checks-logline-text: #8b949e;
    --color-checks-logline-num-text: #484f58;
    --color-checks-logline-debug-text: #a371f7;
    --color-checks-logline-error-text: #8b949e;
    --color-checks-logline-error-num-text: #484f58;
    --color-checks-logline-error-bg: rgba(248,81,73,0.15);
    --color-checks-logline-warning-text: #8b949e;
    --color-checks-logline-warning-num-text: #d29922;
    --color-checks-logline-warning-bg: rgba(187,128,9,0.15);
    --color-checks-logline-command-text: #58a6ff;
    --color-checks-logline-section-text: #3fb950;
    --color-checks-ansi-black: #0d1117;
    --color-checks-ansi-black-bright: #161b22;
    --color-checks-ansi-white: #b1bac4;
    --color-checks-ansi-white-bright: #b1bac4;
    --color-checks-ansi-gray: #6e7681;
    --color-checks-ansi-red: #ff7b72;
    --color-checks-ansi-red-bright: #ffa198;
    --color-checks-ansi-green: #3fb950;
    --color-checks-ansi-green-bright: #56d364;
    --color-checks-ansi-yellow: #d29922;
    --color-checks-ansi-yellow-bright: #e3b341;
    --color-checks-ansi-blue: #58a6ff;
    --color-checks-ansi-blue-bright: #79c0ff;
    --color-checks-ansi-magenta: #bc8cff;
    --color-checks-ansi-magenta-bright: #d2a8ff;
    --color-checks-ansi-cyan: #76e3ea;
    --color-checks-ansi-cyan-bright: #b3f0ff;
    --color-project-header-bg: #0d1117;
    --color-project-sidebar-bg: #161b22;
    --color-project-gradient-in: #161b22;
    --color-project-gradient-out: rgba(22,27,34,0);
    --color-mktg-success: rgba(41,147,61,1);
    --color-mktg-info: rgba(42,123,243,1);
    --color-mktg-bg-shade-gradient-top: rgba(1,4,9,0.065);
    --color-mktg-bg-shade-gradient-bottom: rgba(1,4,9,0);
    --color-mktg-btn-bg-top: hsla(228,82%,66%,1);
    --color-mktg-btn-bg-bottom: #4969ed;
    --color-mktg-btn-bg-overlay-top: hsla(228,74%,59%,1);
    --color-mktg-btn-bg-overlay-bottom: #3355e0;
    --color-mktg-btn-text: #f0f6fc;
    --color-mktg-btn-primary-bg-top: hsla(137,56%,46%,1);
    --color-mktg-btn-primary-bg-bottom: #2ea44f;
    --color-mktg-btn-primary-bg-overlay-top: hsla(134,60%,38%,1);
    --color-mktg-btn-primary-bg-overlay-bottom: #22863a;
    --color-mktg-btn-primary-text: #f0f6fc;
    --color-mktg-btn-enterprise-bg-top: hsla(249,100%,72%,1);
    --color-mktg-btn-enterprise-bg-bottom: #6f57ff;
    --color-mktg-btn-enterprise-bg-overlay-top: hsla(248,65%,63%,1);
    --color-mktg-btn-enterprise-bg-overlay-bottom: #614eda;
    --color-mktg-btn-enterprise-text: #f0f6fc;
    --color-mktg-btn-outline-text: #f0f6fc;
    --color-mktg-btn-outline-border: rgba(240,246,252,0.3);
    --color-mktg-btn-outline-hover-text: #f0f6fc;
    --color-mktg-btn-outline-hover-border: rgba(240,246,252,0.5);
    --color-mktg-btn-outline-focus-border: #f0f6fc;
    --color-mktg-btn-outline-focus-border-inset: rgba(240,246,252,0.5);
    --color-mktg-btn-dark-text: #f0f6fc;
    --color-mktg-btn-dark-border: rgba(240,246,252,0.3);
    --color-mktg-btn-dark-hover-text: #f0f6fc;
    --color-mktg-btn-dark-hover-border: rgba(240,246,252,0.5);
    --color-mktg-btn-dark-focus-border: #f0f6fc;
    --color-mktg-btn-dark-focus-border-inset: rgba(240,246,252,0.5);
    --color-avatar-bg: rgba(240,246,252,0.1);
    --color-avatar-border: rgba(240,246,252,0.1);
    --color-avatar-stack-fade: #30363d;
    --color-avatar-stack-fade-more: #21262d;
    --color-avatar-child-shadow: -2px -2px 0 #0d1117;
    --color-topic-tag-border: rgba(0,0,0,0);
    --color-select-menu-backdrop-border: #484f58;
    --color-select-menu-tap-highlight: rgba(48,54,61,0.5);
    --color-select-menu-tap-focus-bg: #0c2d6b;
    --color-overlay-shadow: 0 0 0 1px #30363d, 0 16px 32px rgba(1,4,9,0.85);
    --color-header-text: rgba(240,246,252,0.7);
    --color-header-bg: #161b22;
    --color-header-logo: #f0f6fc;
    --color-header-search-bg: #0d1117;
    --color-header-search-border: #30363d;
    --color-sidenav-selected-bg: #21262d;
    --color-menu-bg-active: #161b22;
    --color-control-transparent-bg-hover: #656c7633;
    --color-input-disabled-bg: rgba(110,118,129,0);
    --color-timeline-badge-bg: #21262d;
    --color-ansi-black: #484f58;
    --color-ansi-black-bright: #6e7681;
    --color-ansi-white: #b1bac4;
    --color-ansi-white-bright: #f0f6fc;
    --color-ansi-gray: #6e7681;
    --color-ansi-red: #ff7b72;
    --color-ansi-red-bright: #ffa198;
    --color-ansi-green: #3fb950;
    --color-ansi-green-bright: #56d364;
    --color-ansi-yellow: #d29922;
    --color-ansi-yellow-bright: #e3b341;
    --color-ansi-blue: #58a6ff;
    --color-ansi-blue-bright: #79c0ff;
    --color-ansi-magenta: #bc8cff;
    --color-ansi-magenta-bright: #d2a8ff;
    --color-ansi-cyan: #39c5cf;
    --color-ansi-cyan-bright: #56d4dd;
    --color-btn-text: #c9d1d9;
    --color-btn-bg: #21262d;
    --color-btn-border: rgba(240,246,252,0.1);
    --color-btn-shadow: 0 0 transparent;
    --color-btn-inset-shadow: 0 0 transparent;
    --color-btn-hover-bg: #30363d;
    --color-btn-hover-border: #8b949e;
    --color-btn-active-bg: hsla(212,12%,18%,1);
    --color-btn-active-border: #6e7681;
    --color-btn-selected-bg: #161b22;
    --color-btn-focus-bg: #21262d;
    --color-btn-focus-border: #8b949e;
    --color-btn-focus-shadow: 0 0 0 3px rgba(139,148,158,0.3);
    --color-btn-shadow-active: inset 0 0.15em 0.3em rgba(1,4,9,0.15);
    --color-btn-shadow-input-focus: 0 0 0 0.2em rgba(31,111,235,0.3);
    --color-btn-counter-bg: #30363d;
    --color-btn-primary-text: #ffffff;
    --color-btn-primary-bg: #238636;
    --color-btn-primary-border: rgba(240,246,252,0.1);
    --color-btn-primary-shadow: 0 0 transparent;
    --color-btn-primary-inset-shadow: 0 0 transparent;
    --color-btn-primary-hover-bg: #2ea043;
    --color-btn-primary-hover-border: rgba(240,246,252,0.1);
    --color-btn-primary-selected-bg: #238636;
    --color-btn-primary-selected-shadow: 0 0 transparent;
    --color-btn-primary-disabled-text: rgba(240,246,252,0.5);
    --color-btn-primary-disabled-bg: rgba(35,134,54,0.6);
    --color-btn-primary-disabled-border: rgba(240,246,252,0.1);
    --color-btn-primary-focus-bg: #238636;
    --color-btn-primary-focus-border: rgba(240,246,252,0.1);
    --color-btn-primary-focus-shadow: 0 0 0 3px rgba(46,164,79,0.4);
    --color-btn-primary-icon: #f0f6fc;
    --color-btn-primary-counter-bg: rgba(240,246,252,0.2);
    --color-btn-outline-text: #58a6ff;
    --color-btn-outline-hover-text: #58a6ff;
    --color-btn-outline-hover-bg: #30363d;
    --color-btn-outline-hover-border: rgba(240,246,252,0.1);
    --color-btn-outline-hover-shadow: 0 1px 0 rgba(1,4,9,0.1);
    --color-btn-outline-hover-inset-shadow: inset 0 1px 0 rgba(240,246,252,0.03);
    --color-btn-outline-hover-counter-bg: rgba(240,246,252,0.2);
    --color-btn-outline-selected-text: #f0f6fc;
    --color-btn-outline-selected-bg: #0d419d;
    --color-btn-outline-selected-border: rgba(240,246,252,0.1);
    --color-btn-outline-selected-shadow: 0 0 transparent;
    --color-btn-outline-disabled-text: rgba(88,166,255,0.5);
    --color-btn-outline-disabled-bg: #0d1117;
    --color-btn-outline-disabled-counter-bg: rgba(31,111,235,0.05);
    --color-btn-outline-focus-border: rgba(240,246,252,0.1);
    --color-btn-outline-focus-shadow: 0 0 0 3px rgba(17,88,199,0.4);
    --color-btn-outline-counter-bg: rgba(31,111,235,0.1);
    --color-btn-danger-text: #f85149;
    --color-btn-danger-hover-text: #f0f6fc;
    --color-btn-danger-hover-bg: #da3633;
    --color-btn-danger-hover-border: #f85149;
    --color-btn-danger-hover-shadow: 0 0 transparent;
    --color-btn-danger-hover-inset-shadow: 0 0 transparent;
    --color-btn-danger-hover-icon: #f0f6fc;
    --color-btn-danger-hover-counter-bg: rgba(255,255,255,0.2);
    --color-btn-danger-selected-text: #ffffff;
    --color-btn-danger-selected-bg: #b62324;
    --color-btn-danger-selected-border: #ff7b72;
    --color-btn-danger-selected-shadow: 0 0 transparent;
    --color-btn-danger-disabled-text: rgba(248,81,73,0.5);
    --color-btn-danger-disabled-bg: #0d1117;
    --color-btn-danger-disabled-counter-bg: rgba(218,54,51,0.05);
    --color-btn-danger-focus-border: #f85149;
    --color-btn-danger-focus-shadow: 0 0 0 3px rgba(248,81,73,0.4);
    --color-btn-danger-counter-bg: rgba(218,54,51,0.1);
    --color-btn-danger-icon: #f85149;
    --color-underlinenav-icon: #484f58;
    --color-underlinenav-border-hover: rgba(110,118,129,0.4);
    --color-fg-default: #c9d1d9;
    --color-fg-muted: #8b949e;
    --color-fg-subtle: #484f58;
    --color-fg-on-emphasis: #f0f6fc;
    --color-canvas-default: #0d1117;
    --color-canvas-overlay: #161b22;
    --color-canvas-inset: #010409;
    --color-canvas-subtle: #161b22;
    --color-border-default: #30363d;
    --color-border-muted: #21262d;
    --color-border-subtle: rgba(240,246,252,0.1);
    --color-shadow-small: 0 0 transparent;
    --color-shadow-medium: 0 3px 6px #010409;
    --color-shadow-large: 0 8px 24px #010409;
    --color-shadow-extra-large: 0 12px 48px #010409;
    --color-neutral-emphasis-plus: #6e7681;
    --color-neutral-emphasis: #6e7681;
    --color-neutral-muted: rgba(110,118,129,0.4);
    --color-neutral-subtle: rgba(110,118,129,0.1);
    --color-accent-fg: #58a6ff;
    --color-accent-emphasis: #1f6feb;
    --color-accent-muted: rgba(56,139,253,0.4);
    --color-accent-subtle: rgba(56,139,253,0.15);
    --color-success-fg: #3fb950;
    --color-success-emphasis: #238636;
    --color-success-muted: rgba(46,160,67,0.4);
    --color-success-subtle: rgba(46,160,67,0.15);
    --color-attention-fg: #d29922;
    --color-attention-emphasis: #9e6a03;
    --color-attention-muted: rgba(187,128,9,0.4);
    --color-attention-subtle: rgba(187,128,9,0.15);
    --color-severe-fg: #db6d28;
    --color-severe-emphasis: #bd561d;
    --color-severe-muted: rgba(219,109,40,0.4);
    --color-severe-subtle: rgba(219,109,40,0.15);
    --color-danger-fg: #f85149;
    --color-danger-emphasis: #da3633;
    --color-danger-muted: rgba(248,81,73,0.4);
    --color-danger-subtle: rgba(248,81,73,0.15);
    --color-done-fg: #a371f7;
    --color-done-emphasis: #8957e5;
    --color-done-muted: rgba(163,113,247,0.4);
    --color-done-subtle: rgba(163,113,247,0.15);
    --color-sponsors-fg: #db61a2;
    --color-sponsors-emphasis: #bf4b8a;
    --color-sponsors-muted: rgba(219,97,162,0.4);
    --color-sponsors-subtle: rgba(219,97,162,0.15);
    --color-primer-canvas-backdrop: rgba(1,4,9,0.8);
    --color-primer-canvas-sticky: rgba(13,17,23,0.95);
    --color-primer-border-active: #F78166;
    --color-primer-border-contrast: rgba(240,246,252,0.2);
    --color-primer-shadow-highlight: 0 0 transparent;
    --color-primer-shadow-inset: 0 0 transparent;
    --color-primer-shadow-focus: 0 0 0 3px #0c2d6b;
    --color-scale-black: #010409;
    --color-scale-white: #f0f6fc;
    --color-scale-gray-0: #f0f6fc;
    --color-scale-gray-1: #c9d1d9;
    --color-scale-gray-2: #b1bac4;
    --color-scale-gray-3: #8b949e;
    --color-scale-gray-4: #6e7681;
    --color-scale-gray-5: #484f58;
    --color-scale-gray-6: #30363d;
    --color-scale-gray-7: #21262d;
    --color-scale-gray-8: #161b22;
    --color-scale-gray-9: #0d1117;
    --color-scale-blue-0: #cae8ff;
    --color-scale-blue-1: #a5d6ff;
    --color-scale-blue-2: #79c0ff;
    --color-scale-blue-3: #58a6ff;
    --color-scale-blue-4: #388bfd;
    --color-scale-blue-5: #1f6feb;
    --color-scale-blue-6: #1158c7;
    --color-scale-blue-7: #0d419d;
    --color-scale-blue-8: #0c2d6b;
    --color-scale-blue-9: #051d4d;
    --color-scale-green-0: #aff5b4;
    --color-scale-green-1: #7ee787;
    --color-scale-green-2: #56d364;
    --color-scale-green-3: #3fb950;
    --color-scale-green-4: #2ea043;
    --color-scale-green-5: #238636;
    --color-scale-green-6: #196c2e;
    --color-scale-green-7: #0f5323;
    --color-scale-green-8: #033a16;
    --color-scale-green-9: #04260f;
    --color-scale-yellow-0: #f8e3a1;
    --color-scale-yellow-1: #f2cc60;
    --color-scale-yellow-2: #e3b341;
    --color-scale-yellow-3: #d29922;
    --color-scale-yellow-4: #bb8009;
    --color-scale-yellow-5: #9e6a03;
    --color-scale-yellow-6: #845306;
    --color-scale-yellow-7: #693e00;
    --color-scale-yellow-8: #4b2900;
    --color-scale-yellow-9: #341a00;
    --color-scale-orange-0: #ffdfb6;
    --color-scale-orange-1: #ffc680;
    --color-scale-orange-2: #ffa657;
    --color-scale-orange-3: #f0883e;
    --color-scale-orange-4: #db6d28;
    --color-scale-orange-5: #bd561d;
    --color-scale-orange-6: #9b4215;
    --color-scale-orange-7: #762d0a;
    --color-scale-orange-8: #5a1e02;
    --color-scale-orange-9: #3d1300;
    --color-scale-red-0: #ffdcd7;
    --color-scale-red-1: #ffc1ba;
    --color-scale-red-2: #ffa198;
    --color-scale-red-3: #ff7b72;
    --color-scale-red-4: #f85149;
    --color-scale-red-5: #da3633;
    --color-scale-red-6: #b62324;
    --color-scale-red-7: #8e1519;
    --color-scale-red-8: #67060c;
    --color-scale-red-9: #490202;
    --color-scale-purple-0: #eddeff;
    --color-scale-purple-1: #e2c5ff;
    --color-scale-purple-2: #d2a8ff;
    --color-scale-purple-3: #bc8cff;
    --color-scale-purple-4: #a371f7;
    --color-scale-purple-5: #8957e5;
    --color-scale-purple-6: #6e40c9;
    --color-scale-purple-7: #553098;
    --color-scale-purple-8: #3c1e70;
    --color-scale-purple-9: #271052;
    --color-scale-pink-0: #ffdaec;
    --color-scale-pink-1: #ffbedd;
    --color-scale-pink-2: #ff9bce;
    --color-scale-pink-3: #f778ba;
    --color-scale-pink-4: #db61a2;
    --color-scale-pink-5: #bf4b8a;
    --color-scale-pink-6: #9e3670;
    --color-scale-pink-7: #7d2457;
    --color-scale-pink-8: #5e103e;
    --color-scale-pink-9: #42062a;
    --color-scale-coral-0: #FFDDD2;
    --color-scale-coral-1: #FFC2B2;
    --color-scale-coral-2: #FFA28B;
    --color-scale-coral-3: #F78166;
    --color-scale-coral-4: #EA6045;
    --color-scale-coral-5: #CF462D;
    --color-scale-coral-6: #AC3220;
    --color-scale-coral-7: #872012;
    --color-scale-coral-8: #640D04;
    --color-scale-coral-9: #460701
  }
}
```

## File: `packages/extension/src/ui/connect.css`
```css
/*
  Copyright (c) Microsoft Corporation.

  Licensed under the Apache License, Version 2.0 (the "License");
  you may not use this file except in compliance with the License.
  You may obtain a copy of the License at

      http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.
*/

body {
  margin: 0;
  padding: 0;
}

/* Base styles */
.app-container {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Noto Sans", Helvetica, Arial, sans-serif;
  background-color: #ffffff;
  color: #1f2328;
  margin: 0;
  padding: 16px;
  min-height: 100vh;
  font-size: 14px;
}

.content-wrapper {
  max-width: 600px;
  margin: 0 auto;
}

/* Status Banner */
.status-container {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 16px;
  padding-right: 12px;
}

.status-banner {
  padding: 12px;
  font-size: 14px;
  font-weight: 500;
  display: flex;
  align-items: center;
  gap: 8px;
  flex: 1;
}

.status-banner.connected {
  color: #1f2328;
}

.status-banner.connected::before {
  content: "\2705";
  margin-right: 8px;
}

.status-banner.error {
  color: #1f2328;
}

.status-banner.error::before {
  content: "\274C";
  margin-right: 8px;
}

/* Buttons */
.button-container {
  margin-bottom: 16px;
  display: flex;
  justify-content: flex-end;
  padding-right: 12px;
}

.button {
  padding: 8px 16px;
  border-radius: 6px;
  border: none;
  font-size: 14px;
  font-weight: 500;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  text-decoration: none;
  margin-right: 8px;
  min-width: 90px;
}

.button.primary {
  background-color: #f8f9fa;
  color: #3c4043;
  border: 1px solid #dadce0;
}

.button.primary:hover {
  background-color: #f1f3f4;
  border-color: #dadce0;
  box-shadow: 0 1px 2px 0 rgba(60,64,67,.1);
}

.button.default {
  background-color: #f6f8fa;
  color: #24292f;
}

.button.default:hover {
  background-color: #f3f4f6;
}

.button.reject {
  background-color: #da3633;
  color: #ffffff;
  border: 1px solid #da3633;
}

.button.reject:hover {
  background-color: #c73836;
  border-color: #c73836;
}

/* Tab selection */
.tab-section-title {
  padding-left: 12px;
  font-size: 12px;
  font-weight: 400;
  margin-bottom: 12px;
  color: #656d76;
}

.tab-item {
  display: flex;
  align-items: center;
  padding: 12px;
  margin-bottom: 8px;
  background-color: #ffffff;
  cursor: pointer;
  border-radius: 6px;
  transition: background-color 0.2s ease;
}

.tab-item:hover {
  background-color: #f8f9fa;
}

.tab-item.selected {
  background-color: #f6f8fa;
}

.tab-item.disabled {
  cursor: not-allowed;
  opacity: 0.5;
}

.tab-radio {
  margin-right: 12px;
  flex-shrink: 0;
}

.tab-favicon {
  width: 16px;
  height: 16px;
  margin-right: 8px;
  flex-shrink: 0;
}

.tab-content {
  flex: 1;
  min-width: 0;
}

.tab-title {
  font-weight: 500;
  color: #1f2328;
  margin-bottom: 2px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.tab-url {
  font-size: 12px;
  color: #656d76;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

/* Link-style button */
.link-button {
  background: none;
  border: none;
  color: #0066cc;
  text-decoration: underline;
  cursor: pointer;
  padding: 0;
  font: inherit;
}

/* Auth token section */
.auth-token-section {
  margin: 16px 0;
  padding: 16px;
  background-color: #f6f8fa;
  border-radius: 6px;
}

.auth-token-description {
  font-size: 12px;
  color: #656d76;
  margin-bottom: 12px;
}

.auth-token-container {
  display: flex;
  align-items: center;
  gap: 8px;
  background-color: #ffffff;
  padding: 8px;
}

.auth-token-code {
  font-family: 'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, monospace;
  font-size: 12px;
  color: #1f2328;
  border: none;
  flex: 1;
  padding: 0;
  word-break: break-all;
}

.auth-token-refresh {
  flex: none;
  height: 24px;
  width: 24px;
  border: none;
  outline: none;
  color: var(--color-fg-muted);
  background: transparent;
  padding: 4px;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  border-radius: 4px;
}

.auth-token-refresh svg {
  margin: 0;
}

.auth-token-refresh:not(:disabled):hover {
  background-color: var(--color-btn-selected-bg);
}
```

## File: `packages/extension/src/ui/connect.html`
```html
<!--
  Copyright (c) Microsoft Corporation.

  Licensed under the Apache License, Version 2.0 (the "License");
  you may not use this file except in compliance with the License.
  You may obtain a copy of the License at

      http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.
-->
<!DOCTYPE html>
<html>
<head>
  <title>Playwright MCP extension</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="icon" type="image/png" sizes="32x32" href="../../icons/icon-32.png">
  <link rel="icon" type="image/png" sizes="16x16" href="../../icons/icon-16.png">
  <link rel="stylesheet" href="connect.css">
</head>
<body>
  <div id="root"></div>
  <script type="module" src="connect.tsx"></script>
</body>
</html> 
```

## File: `packages/extension/src/ui/connect.tsx`
```tsx
/**
 * Copyright (c) Microsoft Corporation.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

import React, { useCallback, useEffect, useState } from 'react';
import { createRoot } from 'react-dom/client';
import { Button, TabItem } from './tabItem';
import { AuthTokenSection, getOrCreateAuthToken } from './authToken';

import type { TabInfo } from './tabItem';

type Status =
  | { type: 'connecting'; message: string }
  | { type: 'connected'; message: string }
  | { type: 'error'; message: string }
  | { type: 'error'; versionMismatch: { extensionVersion: string; } };

const SUPPORTED_PROTOCOL_VERSION = 1;

const ConnectApp: React.FC = () => {
  const [tabs, setTabs] = useState<TabInfo[]>([]);
  const [status, setStatus] = useState<Status | null>(null);
  const [showButtons, setShowButtons] = useState(true);
  const [showTabList, setShowTabList] = useState(true);
  const [clientInfo, setClientInfo] = useState('unknown');
  const [mcpRelayUrl, setMcpRelayUrl] = useState('');
  const [newTab, setNewTab] = useState<boolean>(false);

  useEffect(() => {
    const runAsync = async () => {
      const params = new URLSearchParams(window.location.search);
      const relayUrl = params.get('mcpRelayUrl');

      if (!relayUrl) {
        handleReject('Missing mcpRelayUrl parameter in URL.');
        return;
      }

      try {
        const host = new URL(relayUrl).hostname;
        if (host !== '127.0.0.1' && host !== '[::1]') {
          handleReject(`MCP extension only allows loopback connections (127.0.0.1 or [::1]). Received host: ${host}`);
          return;
        }
      } catch (e) {
        handleReject(`Invalid mcpRelayUrl parameter in URL: ${relayUrl}. ${e}`);
        return;
      }

      setMcpRelayUrl(relayUrl);

      try {
        const client = JSON.parse(params.get('client') || '{}');
        const info = `${client.name}/${client.version}`;
        setClientInfo(info);
        setStatus({
          type: 'connecting',
          message: `🎭 Playwright MCP started from  "${info}" is trying to connect. Do you want to continue?`
        });
      } catch (e) {
        setStatus({ type: 'error', message: 'Failed to parse client version.' });
        return;
      }

      const parsedVersion = parseInt(params.get('protocolVersion') ?? '', 10);
      const requiredVersion = isNaN(parsedVersion) ? 1 : parsedVersion;
      if (requiredVersion > SUPPORTED_PROTOCOL_VERSION) {
        const extensionVersion = chrome.runtime.getManifest().version;
        setShowButtons(false);
        setShowTabList(false);
        setStatus({
          type: 'error',
          versionMismatch: {
            extensionVersion,
          }
        });
        return;
      }

      const expectedToken = getOrCreateAuthToken();
      const token = params.get('token');
      if (token === expectedToken) {
        await connectToMCPRelay(relayUrl);
        await handleConnectToTab();
        return;
      }
      if (token) {
        handleReject('Invalid token provided.');
        return;
      }

      await connectToMCPRelay(relayUrl);

      // If this is a browser_navigate command, hide the tab list and show simple allow/reject
      if (params.get('newTab') === 'true') {
        setNewTab(true);
        setShowTabList(false);
      } else {
        await loadTabs();
      }
    };
    void runAsync();
  }, []);

  const handleReject = useCallback((message: string) => {
    setShowButtons(false);
    setShowTabList(false);
    setStatus({ type: 'error', message });
  }, []);

  const connectToMCPRelay = useCallback(async (mcpRelayUrl: string) => {
    const response = await chrome.runtime.sendMessage({ type: 'connectToMCPRelay', mcpRelayUrl  });
    if (!response.success)
      handleReject(response.error);
  }, [handleReject]);

  const loadTabs = useCallback(async () => {
    const response = await chrome.runtime.sendMessage({ type: 'getTabs' });
    if (response.success)
      setTabs(response.tabs);
    else
      setStatus({ type: 'error', message: 'Failed to load tabs: ' + response.error });
  }, []);

  const handleConnectToTab = useCallback(async (tab?: TabInfo) => {
    setShowButtons(false);
    setShowTabList(false);

    try {
      const response = await chrome.runtime.sendMessage({
        type: 'connectToTab',
        mcpRelayUrl,
        tabId: tab?.id,
        windowId: tab?.windowId,
      });

      if (response?.success) {
        setStatus({ type: 'connected', message: `MCP client "${clientInfo}" connected.` });
      } else {
        setStatus({
          type: 'error',
          message: response?.error || `MCP client "${clientInfo}" failed to connect.`
        });
      }
    } catch (e) {
      setStatus({
        type: 'error',
        message: `MCP client "${clientInfo}" failed to connect: ${e}`
      });
    }
  }, [clientInfo, mcpRelayUrl]);

  useEffect(() => {
    const listener = (message: any) => {
      if (message.type === 'connectionTimeout')
        handleReject('Connection timed out.');
    };
    chrome.runtime.onMessage.addListener(listener);
    return () => {
      chrome.runtime.onMessage.removeListener(listener);
    };
  }, [handleReject]);

  return (
    <div className='app-container'>
      <div className='content-wrapper'>
        {status && (
          <div className='status-container'>
            <StatusBanner status={status} />
            {showButtons && (
              <div className='button-container'>
                {newTab ? (
                  <>
                    <Button variant='primary' onClick={() => handleConnectToTab()}>
                      Allow
                    </Button>
                    <Button variant='reject' onClick={() => handleReject('Connection rejected. This tab can be closed.')}>
                      Reject
                    </Button>
                  </>
                ) : (
                  <Button variant='reject' onClick={() => handleReject('Connection rejected. This tab can be closed.')}>
                    Reject
                  </Button>
                )}
              </div>
            )}
          </div>
        )}

        {status?.type === 'connecting' && (
          <AuthTokenSection />
        )}

        {showTabList && (
          <div>
            <div className='tab-section-title'>
              Select page to expose to MCP server:
            </div>
            <div>
              {tabs.map(tab => (
                <TabItem
                  key={tab.id}
                  tab={tab}
                  button={
                    <Button variant='primary' onClick={() => handleConnectToTab(tab)}>
                      Connect
                    </Button>
                  }
                />
              ))}
            </div>
          </div>
        )}
      </div>
    </div>
  );
};

const VersionMismatchError: React.FC<{ extensionVersion: string }> = ({ extensionVersion }) => {
  const readmeUrl = 'https://github.com/microsoft/playwright-mcp/blob/main/extension/README.md';
  const latestReleaseUrl = 'https://github.com/microsoft/playwright-mcp/releases/latest';
  return (
    <div>
      Playwright MCP version trying to connect requires newer extension version (current version: {extensionVersion}).{' '}
      <a href={latestReleaseUrl}>Click here</a> to download latest version of the extension, then drag and drop it into the Chrome Extensions page.{' '}
      See <a href={readmeUrl} target='_blank' rel='noopener noreferrer'>installation instructions</a> for more details.
    </div>
  );
};

const StatusBanner: React.FC<{ status: Status }> = ({ status }) => {
  return (
    <div className={`status-banner ${status.type}`}>
      {'versionMismatch' in status ? (
        <VersionMismatchError
          extensionVersion={status.versionMismatch.extensionVersion}
        />
      ) : (
        status.message
      )}
    </div>
  );
};

// Initialize the React app
const container = document.getElementById('root');
if (container) {
  const root = createRoot(container);
  root.render(<ConnectApp />);
}
```

## File: `packages/extension/src/ui/copyToClipboard.css`
```css
/*
  Copyright (c) Microsoft Corporation.

  Licensed under the Apache License, Version 2.0 (the "License");
  you may not use this file except in compliance with the License.
  You may obtain a copy of the License at

      http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.
*/

.copy-icon {
  flex: none;
  height: 24px;
  width: 24px;
  border: none;
  outline: none;
  color: var(--color-fg-muted);
  background: transparent;
  padding: 4px;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  border-radius: 4px;
}

.copy-icon svg {
  margin: 0;
}

.copy-icon:not(:disabled):hover {
  background-color: var(--color-btn-selected-bg);
}
```

## File: `packages/extension/src/ui/copyToClipboard.tsx`
```tsx
/**
 * Copyright (c) Microsoft Corporation.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

import * as React from 'react';
import * as icons from './icons';
import './copyToClipboard.css';

type CopyToClipboardProps = {
  value: string;
};

/**
 * A copy to clipboard button.
 */
export const CopyToClipboard: React.FunctionComponent<CopyToClipboardProps> = ({ value }) => {
  type IconType = 'copy' | 'check' | 'cross';
  const [icon, setIcon] = React.useState<IconType>('copy');

  React.useEffect(() => {
    setIcon('copy');
  }, [value]);

  React.useEffect(() => {
    if (icon === 'check') {
      const timeout = setTimeout(() => {
        setIcon('copy');
      }, 3000);
      return () => clearTimeout(timeout);
    }
  }, [icon]);

  const handleCopy = React.useCallback(() => {
    navigator.clipboard.writeText(value).then(() => {
      setIcon('check');
    }, () => {
      setIcon('cross');
    });
  }, [value]);
  const iconElement = icon === 'check' ? icons.check() : icon === 'cross' ? icons.cross() : icons.copy();
  return <button className='copy-icon' title='Copy to clipboard' aria-label='Copy to clipboard' onClick={handleCopy}>{iconElement}</button>;
};
```

## File: `packages/extension/src/ui/icons.css`
```css
/*
  Copyright (c) Microsoft Corporation.

  Licensed under the Apache License, Version 2.0 (the "License");
  you may not use this file except in compliance with the License.
  You may obtain a copy of the License at

      http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.
*/

.octicon {
  display: inline-block;
  overflow: visible !important;
  vertical-align: text-bottom;
  fill: currentColor;
  margin-right: 7px;
  flex: none;
}

.color-icon-success {
  color: var(--color-success-fg) !important;
}

.color-text-danger {
  color: var(--color-danger-fg) !important;
}
```

## File: `packages/extension/src/ui/icons.tsx`
```tsx
/*
  Copyright (c) Microsoft Corporation.

  Licensed under the Apache License, Version 2.0 (the "License");
  you may not use this file except in compliance with the License.
  You may obtain a copy of the License at

      http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.
*/

import './icons.css';
import './colors.css';

export const cross = () => {
  return <svg className='octicon color-text-danger' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true'>
    <path fillRule='evenodd' d='M3.72 3.72a.75.75 0 011.06 0L8 6.94l3.22-3.22a.75.75 0 111.06 1.06L9.06 8l3.22 3.22a.75.75 0 11-1.06 1.06L8 9.06l-3.22 3.22a.75.75 0 01-1.06-1.06L6.94 8 3.72 4.78a.75.75 0 010-1.06z'></path>
  </svg>;
};

export const check = () => {
  return <svg aria-hidden='true' height='16' viewBox='0 0 16 16' version='1.1' width='16' data-view-component='true' className='octicon color-icon-success'>
    <path fillRule='evenodd' d='M13.78 4.22a.75.75 0 010 1.06l-7.25 7.25a.75.75 0 01-1.06 0L2.22 9.28a.75.75 0 011.06-1.06L6 10.94l6.72-6.72a.75.75 0 011.06 0z'></path>
  </svg>;
};

export const copy = () => {
  return <svg className='octicon' viewBox='0 0 16 16' width='16' height='16' aria-hidden='true'>
    <path d='M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z'></path>
    <path d='M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z'></path>
  </svg>;
};

export const refresh = () => {
  return <svg className='octicon' viewBox="0 0 16 16" width="16" height="16" aria-hidden='true'>
    <path d="M1.705 8.005a.75.75 0 0 1 .834.656 5.5 5.5 0 0 0 9.592 2.97l-1.204-1.204a.25.25 0 0 1 .177-.427h3.646a.25.25 0 0 1 .25.25v3.646a.25.25 0 0 1-.427.177l-1.38-1.38A7.002 7.002 0 0 1 1.05 8.84a.75.75 0 0 1 .656-.834ZM8 2.5a5.487 5.487 0 0 0-4.131 1.869l1.204 1.204A.25.25 0 0 1 4.896 6H1.25A.25.25 0 0 1 1 5.75V2.104a.25.25 0 0 1 .427-.177l1.38 1.38A7.002 7.002 0 0 1 14.95 7.16a.75.75 0 0 1-1.49.178A5.5 5.5 0 0 0 8 2.5Z"></path>
  </svg>;
};

export const chevronDown = () => {
  return <svg className='octicon' viewBox="0 0 16 16" width="16" height="16" aria-hidden='true'>
    <path d="M12.78 5.22a.749.749 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.06 0L3.22 6.28a.749.749 0 1 1 1.06-1.06L8 8.939l3.72-3.719a.749.749 0 0 1 1.06 0Z"></path>
  </svg>;
};
```

## File: `packages/extension/src/ui/status.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Playwright MCP Bridge Status</title>
  <link rel="stylesheet" href="connect.css">
</head>
<body>
  <div id="root"></div>
  <script src="status.tsx" type="module"></script>
</body>
</html>
```

## File: `packages/extension/src/ui/status.tsx`
```tsx
/**
 * Copyright (c) Microsoft Corporation.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

import React, { useState, useEffect } from 'react';
import { createRoot } from 'react-dom/client';
import { Button, TabItem  } from './tabItem';

import type { TabInfo } from './tabItem';
import { AuthTokenSection } from './authToken';

interface ConnectionStatus {
  isConnected: boolean;
  connectedTabId: number | null;
  connectedTab?: TabInfo;
}

const StatusApp: React.FC = () => {
  const [status, setStatus] = useState<ConnectionStatus>({
    isConnected: false,
    connectedTabId: null
  });

  useEffect(() => {
    void loadStatus();
  }, []);

  const loadStatus = async () => {
    // Get current connection status from background script
    const { connectedTabId } = await chrome.runtime.sendMessage({ type: 'getConnectionStatus' });
    if (connectedTabId) {
      const tab = await chrome.tabs.get(connectedTabId);
      setStatus({
        isConnected: true,
        connectedTabId,
        connectedTab: {
          id: tab.id!,
          windowId: tab.windowId!,
          title: tab.title!,
          url: tab.url!,
          favIconUrl: tab.favIconUrl
        }
      });
    } else {
      setStatus({
        isConnected: false,
        connectedTabId: null
      });
    }
  };

  const openConnectedTab = async () => {
    if (!status.connectedTabId)
      return;
    await chrome.tabs.update(status.connectedTabId, { active: true });
    window.close();
  };

  const disconnect = async () => {
    await chrome.runtime.sendMessage({ type: 'disconnect' });
    window.close();
  };

  return (
    <div className='app-container'>
      <div className='content-wrapper'>
        {status.isConnected && status.connectedTab ? (
          <div>
            <div className='tab-section-title'>
              Page with connected MCP client:
            </div>
            <div>
              <TabItem
                tab={status.connectedTab}
                button={
                  <Button variant='primary' onClick={disconnect}>
                    Disconnect
                  </Button>
                }
                onClick={openConnectedTab}
              />
            </div>
          </div>
        ) : (
          <div className='status-banner'>
            No MCP clients are currently connected.
          </div>
        )}
        <AuthTokenSection />
      </div>
    </div>
  );
};

// Initialize the React app
const container = document.getElementById('root');
if (container) {
  const root = createRoot(container);
  root.render(<StatusApp />);
}
```

## File: `packages/extension/src/ui/tabItem.tsx`
```tsx
/**
 * Copyright (c) Microsoft Corporation.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

import React from 'react';

export interface TabInfo {
  id: number;
  windowId: number;
  title: string;
  url: string;
  favIconUrl?: string;
}

export const Button: React.FC<{ variant: 'primary' | 'default' | 'reject'; onClick: () => void; children: React.ReactNode }> = ({
  variant,
  onClick,
  children
}) => {
  return (
    <button className={`button ${variant}`} onClick={onClick}>
      {children}
    </button>
  );
};


export interface TabItemProps {
  tab: TabInfo;
  onClick?: () => void;
  button?: React.ReactNode;
}

export const TabItem: React.FC<TabItemProps> = ({
  tab,
  onClick,
  button
}) => {
  return (
    <div className='tab-item' onClick={onClick} style={onClick ? { cursor: 'pointer' } : undefined}>
      <img
        src={tab.favIconUrl || 'data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16"><rect width="16" height="16" fill="%23f6f8fa"/></svg>'}
        alt=''
        className='tab-favicon'
      />
      <div className='tab-content'>
        <div className='tab-title'>
          {tab.title || 'Untitled'}
        </div>
        <div className='tab-url'>{tab.url}</div>
      </div>
      {button}
    </div>
  );
};
```

## File: `packages/extension/src/ui/tsconfig.json`
```json
// Help VSCode to find right tsconfig file.
{
    "extends": "../../tsconfig.ui.json"
}
```

## File: `packages/extension/tests/extension.spec.ts`
```typescript
/**
 * Copyright (c) Microsoft Corporation.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

import fs from 'fs/promises';
import path from 'path';
import { chromium } from 'playwright';
import { spawn } from 'child_process';
import { test as base, expect } from '../../playwright-mcp/tests/fixtures';

import type { Client } from '@modelcontextprotocol/sdk/client/index.js';
import type { BrowserContext } from 'playwright';
import type { StartClient } from '../../playwright-mcp/tests/fixtures';

type BrowserWithExtension = {
  userDataDir: string;
  launch: (mode?: 'disable-extension') => Promise<BrowserContext>;
};

type CliResult = {
  output: string;
  error: string;
};

type TestFixtures = {
  browserWithExtension: BrowserWithExtension,
  pathToExtension: string,
  useShortConnectionTimeout: (timeoutMs: number) => void
  overrideProtocolVersion: (version: number) => void
  cli: (...args: string[]) => Promise<CliResult>;
};

const extensionPublicKey = 'MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAwRsUUO4mmbCi4JpmrIoIw31iVW9+xUJRZ6nSzya17PQkaUPDxe1IpgM+vpd/xB6mJWlJSyE1Lj95c0sbomGfVY1M0zUeKbaRVcAb+/a6m59gNR+ubFlmTX0nK9/8fE2FpRB9D+4N5jyeIPQuASW/0oswI2/ijK7hH5NTRX8gWc/ROMSgUj7rKhTAgBrICt/NsStgDPsxRTPPJnhJ/ViJtM1P5KsSYswE987DPoFnpmkFpq8g1ae0eYbQfXy55ieaacC4QWyJPj3daU2kMfBQw7MXnnk0H/WDxouMOIHnd8MlQxpEMqAihj7KpuONH+MUhuj9HEQo4df6bSaIuQ0b4QIDAQAB';
const extensionId = 'mmlmfjhmonkocbjadbfplnigmagldckm';

const test = base.extend<TestFixtures>({
  pathToExtension: async ({}, use, testInfo) => {
    const extensionDir = testInfo.outputPath('extension');
    const srcDir = path.resolve(__dirname, '../dist');
    await fs.cp(srcDir, extensionDir, { recursive: true });
    const manifestPath = path.join(extensionDir, 'manifest.json');
    const manifest = JSON.parse(await fs.readFile(manifestPath, 'utf8'));
    // We don't hardcode the key in manifest, but for the tests we set the key field
    // to ensure that locally installed extension has the same id as the one published
    // in the store.
    manifest.key = extensionPublicKey;
    await fs.writeFile(manifestPath, JSON.stringify(manifest, null, 2));
    await use(extensionDir);
  },

  browserWithExtension: async ({ mcpBrowser, pathToExtension }, use, testInfo) => {
    // The flags no longer work in Chrome since
    // https://chromium.googlesource.com/chromium/src/+/290ed8046692651ce76088914750cb659b65fb17%5E%21/chrome/browser/extensions/extension_service.cc?pli=1#
    test.skip('chromium' !== mcpBrowser, '--load-extension is not supported for official builds of Chromium');

    let browserContext: BrowserContext | undefined;
    const userDataDir = testInfo.outputPath('extension-user-data-dir');
    await use({
      userDataDir,
      launch: async (mode?: 'disable-extension') => {
        browserContext = await chromium.launchPersistentContext(userDataDir, {
          channel: mcpBrowser,
          // Opening the browser singleton only works in headed.
          headless: false,
          // Automation disables singleton browser process behavior, which is necessary for the extension.
          ignoreDefaultArgs: ['--enable-automation'],
          args: mode === 'disable-extension' ? [] : [
            `--disable-extensions-except=${pathToExtension}`,
            `--load-extension=${pathToExtension}`,
          ],
        });

        // for manifest v3:
        let [serviceWorker] = browserContext.serviceWorkers();
        if (!serviceWorker)
          serviceWorker = await browserContext.waitForEvent('serviceworker');

        return browserContext;
      }
    });
    await browserContext?.close();

    // Free up disk space.
    await fs.rm(userDataDir, { recursive: true, force: true }).catch(() => {});
  },

  useShortConnectionTimeout: async ({}, use) => {
    await use((timeoutMs: number) => {
      process.env.PWMCP_TEST_CONNECTION_TIMEOUT = timeoutMs.toString();
    });
    process.env.PWMCP_TEST_CONNECTION_TIMEOUT = undefined;
  },

  overrideProtocolVersion: async ({}, use) => {
    await use((version: number) => {
      process.env.PWMCP_TEST_PROTOCOL_VERSION = version.toString();
    });
    process.env.PWMCP_TEST_PROTOCOL_VERSION = undefined;
  },

  cli: async ({ mcpBrowser }, use, testInfo) => {
    await use(async (...args: string[]) => {
      return await runCli(args, { mcpBrowser, testInfo });
    });

    // Cleanup sessions
    await runCli(['close-all'], { mcpBrowser, testInfo }).catch(() => {});

    const daemonDir = path.join(testInfo.outputDir, 'daemon');
    await fs.rm(daemonDir, { recursive: true, force: true }).catch(() => {});
  },
});

async function runCli(
  args: string[],
  options: { mcpBrowser?: string, testInfo: any },
): Promise<CliResult> {
  const stepTitle = `cli ${args.join(' ')}`;

  return await test.step(stepTitle, async () => {
    const testInfo = options.testInfo;

    // Path to the terminal CLI
    const cliPath = path.join(__dirname, '../../../node_modules/playwright/lib/cli/client/program.js');

    return new Promise<CliResult>((resolve, reject) => {
      let stdout = '';
      let stderr = '';

      const childProcess = spawn(process.execPath, [cliPath, ...args], {
        cwd: testInfo.outputPath(),
        env: {
          ...process.env,
          PLAYWRIGHT_DAEMON_INSTALL_DIR: testInfo.outputPath(),
          PLAYWRIGHT_DAEMON_SESSION_DIR: testInfo.outputPath('daemon'),
          PLAYWRIGHT_DAEMON_SOCKETS_DIR: path.join(testInfo.project.outputDir, 'daemon-sockets'),
          PLAYWRIGHT_MCP_BROWSER: options.mcpBrowser,
          PLAYWRIGHT_MCP_HEADLESS: 'false',
        },
        detached: true,
      });

      childProcess.stdout?.on('data', (data) => {
        stdout += data.toString();
      });

      childProcess.stderr?.on('data', (data) => {
        if (process.env.PWMCP_DEBUG)
          process.stderr.write(data);
        stderr += data.toString();
      });

      childProcess.on('close', async (code) => {
        await testInfo.attach(stepTitle, { body: stdout, contentType: 'text/plain' });
        resolve({
          output: stdout.trim(),
          error: stderr.trim(),
        });
      });

      childProcess.on('error', reject);
    });
  });
}

async function startWithExtensionFlag(browserWithExtension: BrowserWithExtension, startClient: StartClient): Promise<Client> {
  const { client } = await startClient({
    args: [`--extension`],
    config: {
      browser: {
        userDataDir: browserWithExtension.userDataDir,
      }
    },
  });
  return client;
}

const testWithOldExtensionVersion = test.extend({
  pathToExtension: async ({ pathToExtension }, use, testInfo) => {
    const manifestPath = path.join(pathToExtension, 'manifest.json');
    const manifest = JSON.parse(await fs.readFile(manifestPath, 'utf8'));
    manifest.key = extensionPublicKey;
    manifest.version = '0.0.1';
    await fs.writeFile(manifestPath, JSON.stringify(manifest, null, 2));
    await use(pathToExtension);
  },
});

test(`navigate with extension`, async ({ browserWithExtension, startClient, server }) => {
  const browserContext = await browserWithExtension.launch();

  const client = await startWithExtensionFlag(browserWithExtension, startClient);

  const confirmationPagePromise = browserContext.waitForEvent('page', page => {
    return page.url().startsWith(`chrome-extension://${extensionId}/connect.html`);
  });

  const navigateResponse = client.callTool({
    name: 'browser_navigate',
    arguments: { url: server.HELLO_WORLD },
  });

  const selectorPage = await confirmationPagePromise;
  // For browser_navigate command, the UI shows Allow/Reject buttons instead of tab selector
  await selectorPage.getByRole('button', { name: 'Allow' }).click();

  expect(await navigateResponse).toHaveResponse({
    snapshot: expect.stringContaining(`- generic [active] [ref=e1]: Hello, world!`),
  });
});

test(`snapshot of an existing page`, async ({ browserWithExtension, startClient, server }) => {
  const browserContext = await browserWithExtension.launch();

  const page = await browserContext.newPage();
  await page.goto(server.HELLO_WORLD);

  // Another empty page.
  await browserContext.newPage();
  expect(browserContext.pages()).toHaveLength(3);

  const client = await startWithExtensionFlag(browserWithExtension, startClient);
  expect(browserContext.pages()).toHaveLength(3);

  const confirmationPagePromise = browserContext.waitForEvent('page', page => {
    return page.url().startsWith(`chrome-extension://${extensionId}/connect.html`);
  });

  const navigateResponse = client.callTool({
    name: 'browser_snapshot',
    arguments: { },
  });

  const selectorPage = await confirmationPagePromise;
  expect(browserContext.pages()).toHaveLength(4);

  await selectorPage.locator('.tab-item', { hasText: 'Title' }).getByRole('button', { name: 'Connect' }).click();

  expect(await navigateResponse).toHaveResponse({
    snapshot: expect.stringContaining(`- generic [active] [ref=e1]: Hello, world!`),
  });

  expect(browserContext.pages()).toHaveLength(4);
});

test(`extension not installed timeout`, async ({ browserWithExtension, startClient, server, useShortConnectionTimeout }) => {
  useShortConnectionTimeout(100);

  const browserContext = await browserWithExtension.launch();

  const client = await startWithExtensionFlag(browserWithExtension, startClient);

  const confirmationPagePromise = browserContext.waitForEvent('page', page => {
    return page.url().startsWith(`chrome-extension://${extensionId}/connect.html`);
  });

  expect(await client.callTool({
    name: 'browser_navigate',
    arguments: { url: server.HELLO_WORLD },
  })).toHaveResponse({
    error: expect.stringContaining('Extension connection timeout. Make sure the "Playwright MCP Bridge" extension is installed.'),
    isError: true,
  });

  await confirmationPagePromise;
});

testWithOldExtensionVersion(`works with old extension version`, async ({ browserWithExtension, startClient, server, useShortConnectionTimeout }) => {
  useShortConnectionTimeout(500);

  // Prelaunch the browser, so that it is properly closed after the test.
  const browserContext = await browserWithExtension.launch();

  const client = await startWithExtensionFlag(browserWithExtension, startClient);

  const confirmationPagePromise = browserContext.waitForEvent('page', page => {
    return page.url().startsWith(`chrome-extension://${extensionId}/connect.html`);
  });

  const navigateResponse = client.callTool({
    name: 'browser_navigate',
    arguments: { url: server.HELLO_WORLD },
  });

  const selectorPage = await confirmationPagePromise;
  // For browser_navigate command, the UI shows Allow/Reject buttons instead of tab selector
  await selectorPage.getByRole('button', { name: 'Allow' }).click();

  expect(await navigateResponse).toHaveResponse({
    snapshot: expect.stringContaining(`- generic [active] [ref=e1]: Hello, world!`),
  });
});

test(`extension needs update`, async ({ browserWithExtension, startClient, server, useShortConnectionTimeout, overrideProtocolVersion }) => {
  useShortConnectionTimeout(500);
  overrideProtocolVersion(1000);

  // Prelaunch the browser, so that it is properly closed after the test.
  const browserContext = await browserWithExtension.launch();

  const client = await startWithExtensionFlag(browserWithExtension, startClient);

  const confirmationPagePromise = browserContext.waitForEvent('page', page => {
    return page.url().startsWith(`chrome-extension://${extensionId}/connect.html`);
  });

  const navigateResponse = client.callTool({
    name: 'browser_navigate',
    arguments: { url: server.HELLO_WORLD },
  });

  const confirmationPage = await confirmationPagePromise;
  await expect(confirmationPage.locator('.status-banner')).toContainText(`Playwright MCP version trying to connect requires newer extension version`);

  expect(await navigateResponse).toHaveResponse({
    error: expect.stringContaining('Extension connection timeout.'),
    isError: true,
  });
});

test(`custom executablePath`, async ({ startClient, server, useShortConnectionTimeout }) => {
  useShortConnectionTimeout(1000);

  const executablePath = test.info().outputPath('echo.sh');
  await fs.writeFile(executablePath, '#!/bin/bash\necho "Custom exec args: $@" > "$(dirname "$0")/output.txt"', { mode: 0o755 });

  const { client } = await startClient({
    args: [`--extension`],
    config: {
      browser: {
        launchOptions: {
          executablePath,
        },
      }
    },
  });

  const navigateResponse = await client.callTool({
    name: 'browser_navigate',
    arguments: { url: server.HELLO_WORLD },
  });
  expect(await navigateResponse).toHaveResponse({
    error: expect.stringContaining('Extension connection timeout.'),
    isError: true,
  });
  expect(await fs.readFile(test.info().outputPath('output.txt'), 'utf8')).toMatch(new RegExp(`Custom exec args.*chrome-extension://${extensionId}/connect\\.html\\?`));
});

test(`bypass connection dialog with token`, async ({ browserWithExtension, startClient, server }) => {
  const browserContext = await browserWithExtension.launch();

  const page = await browserContext.newPage();
  await page.goto(`chrome-extension://${extensionId}/status.html`);
  const token = await page.locator('.auth-token-code').textContent();
  const [name, value] = token?.split('=') || [];

  const { client } = await startClient({
    args: [`--extension`],
    extensionToken: value,
    config: {
      browser: {
        userDataDir: browserWithExtension.userDataDir,
      }
    },
  });

  const navigateResponse = await client.callTool({
    name: 'browser_navigate',
    arguments: { url: server.HELLO_WORLD },
  });

  expect(await navigateResponse).toHaveResponse({
    snapshot: expect.stringContaining(`- generic [active] [ref=e1]: Hello, world!`),
  });
});

test.describe('CLI with extension', () => {
  test('open <url> --extension', async ({ browserWithExtension, cli, server }, testInfo) => {
    const browserContext = await browserWithExtension.launch();

    // Write config file with userDataDir 
    const configPath = testInfo.outputPath('cli-config.json');
    await fs.writeFile(configPath, JSON.stringify({
      browser: {
        userDataDir: browserWithExtension.userDataDir,
      }
    }, null, 2));

    const confirmationPagePromise = browserContext.waitForEvent('page', page => {
      return page.url().startsWith(`chrome-extension://${extensionId}/connect.html`);
    });

    // Start the CLI command in the background
    const cliPromise = cli('open', server.HELLO_WORLD, '--extension', `--config=cli-config.json`);

    // Wait for the confirmation page to appear
    const confirmationPage = await confirmationPagePromise;

    // Click the Connect button
    await confirmationPage.locator('.tab-item', { hasText: 'Playwright MCP extension' }).getByRole('button', { name: 'Connect' }).click();

    // Wait for the CLI command to complete
    const { output } = await cliPromise;

    // Verify the output
    expect(output).toContain(`### Page`);
    expect(output).toContain(`- Page URL: ${server.HELLO_WORLD}`);
    expect(output).toContain(`- Page Title: Title`);
  });
});
```

## File: `packages/playwright-cli-stub/LICENSE`
```
                                 Apache License
                           Version 2.0, January 2004
                        http://www.apache.org/licenses/

   TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

   1. Definitions.

      "License" shall mean the terms and conditions for use, reproduction,
      and distribution as defined by Sections 1 through 9 of this document.

      "Licensor" shall mean the copyright owner or entity authorized by
      the copyright owner that is granting the License.

      "Legal Entity" shall mean the union of the acting entity and all
      other entities that control, are controlled by, or are under common
      control with that entity. For the purposes of this definition,
      "control" means (i) the power, direct or indirect, to cause the
      direction or management of such entity, whether by contract or
      otherwise, or (ii) ownership of fifty percent (50%) or more of the
      outstanding shares, or (iii) beneficial ownership of such entity.

      "You" (or "Your") shall mean an individual or Legal Entity
      exercising permissions granted by this License.

      "Source" form shall mean the preferred form for making modifications,
      including but not limited to software source code, documentation
      source, and configuration files.

      "Object" form shall mean any form resulting from mechanical
      transformation or translation of a Source form, including but
      not limited to compiled object code, generated documentation,
      and conversions to other media types.

      "Work" shall mean the work of authorship, whether in Source or
      Object form, made available under the License, as indicated by a
      copyright notice that is included in or attached to the work
      (an example is provided in the Appendix below).

      "Derivative Works" shall mean any work, whether in Source or Object
      form, that is based on (or derived from) the Work and for which the
      editorial revisions, annotations, elaborations, or other modifications
      represent, as a whole, an original work of authorship. For the purposes
      of this License, Derivative Works shall not include works that remain
      separable from, or merely link (or bind by name) to the interfaces of,
      the Work and Derivative Works thereof.

      "Contribution" shall mean any work of authorship, including
      the original version of the Work and any modifications or additions
      to that Work or Derivative Works thereof, that is intentionally
      submitted to Licensor for inclusion in the Work by the copyright owner
      or by an individual or Legal Entity authorized to submit on behalf of
      the copyright owner. For the purposes of this definition, "submitted"
      means any form of electronic, verbal, or written communication sent
      to the Licensor or its representatives, including but not limited to
      communication on electronic mailing lists, source code control systems,
      and issue tracking systems that are managed by, or on behalf of, the
      Licensor for the purpose of discussing and improving the Work, but
      excluding communication that is conspicuously marked or otherwise
      designated in writing by the copyright owner as "Not a Contribution."

      "Contributor" shall mean Licensor and any individual or Legal Entity
      on behalf of whom a Contribution has been received by Licensor and
      subsequently incorporated within the Work.

   2. Grant of Copyright License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      copyright license to reproduce, prepare Derivative Works of,
      publicly display, publicly perform, sublicense, and distribute the
      Work and such Derivative Works in Source or Object form.

   3. Grant of Patent License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      (except as stated in this section) patent license to make, have made,
      use, offer to sell, sell, import, and otherwise transfer the Work,
      where such license applies only to those patent claims licensable
      by such Contributor that are necessarily infringed by their
      Contribution(s) alone or by combination of their Contribution(s)
      with the Work to which such Contribution(s) was submitted. If You
      institute patent litigation against any entity (including a
      cross-claim or counterclaim in a lawsuit) alleging that the Work
      or a Contribution incorporated within the Work constitutes direct
      or contributory patent infringement, then any patent licenses
      granted to You under this License for that Work shall terminate
      as of the date such litigation is filed.

   4. Redistribution. You may reproduce and distribute copies of the
      Work or Derivative Works thereof in any medium, with or without
      modifications, and in Source or Object form, provided that You
      meet the following conditions:

      (a) You must give any other recipients of the Work or
          Derivative Works a copy of this License; and

      (b) You must cause any modified files to carry prominent notices
          stating that You changed the files; and

      (c) You must retain, in the Source form of any Derivative Works
          that You distribute, all copyright, patent, trademark, and
          attribution notices from the Source form of the Work,
          excluding those notices that do not pertain to any part of
          the Derivative Works; and

      (d) If the Work includes a "NOTICE" text file as part of its
          distribution, then any Derivative Works that You distribute must
          include a readable copy of the attribution notices contained
          within such NOTICE file, excluding those notices that do not
          pertain to any part of the Derivative Works, in at least one
          of the following places: within a NOTICE text file distributed
          as part of the Derivative Works; within the Source form or
          documentation, if provided along with the Derivative Works; or,
          within a display generated by the Derivative Works, if and
          wherever such third-party notices normally appear. The contents
          of the NOTICE file are for informational purposes only and
          do not modify the License. You may add Your own attribution
          notices within Derivative Works that You distribute, alongside
          or as an addendum to the NOTICE text from the Work, provided
          that such additional attribution notices cannot be construed
          as modifying the License.

      You may add Your own copyright statement to Your modifications and
      may provide additional or different license terms and conditions
      for use, reproduction, or distribution of Your modifications, or
      for any such Derivative Works as a whole, provided Your use,
      reproduction, and distribution of the Work otherwise complies with
      the conditions stated in this License.

   5. Submission of Contributions. Unless You explicitly state otherwise,
      any Contribution intentionally submitted for inclusion in the Work
      by You to the Licensor shall be under the terms and conditions of
      this License, without any additional terms or conditions.
      Notwithstanding the above, nothing herein shall supersede or modify
      the terms of any separate license agreement you may have executed
      with Licensor regarding such Contributions.

   6. Trademarks. This License does not grant permission to use the trade
      names, trademarks, service marks, or product names of the Licensor,
      except as required for reasonable and customary use in describing the
      origin of the Work and reproducing the content of the NOTICE file.

   7. Disclaimer of Warranty. Unless required by applicable law or
      agreed to in writing, Licensor provides the Work (and each
      Contributor provides its Contributions) on an "AS IS" BASIS,
      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
      implied, including, without limitation, any warranties or conditions
      of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
      PARTICULAR PURPOSE. You are solely responsible for determining the
      appropriateness of using or redistributing the Work and assume any
      risks associated with Your exercise of permissions under this License.

   8. Limitation of Liability. In no event and under no legal theory,
      whether in tort (including negligence), contract, or otherwise,
      unless required by applicable law (such as deliberate and grossly
      negligent acts) or agreed to in writing, shall any Contributor be
      liable to You for damages, including any direct, indirect, special,
      incidental, or consequential damages of any character arising as a
      result of this License or out of the use or inability to use the
      Work (including but not limited to damages for loss of goodwill,
      work stoppage, computer failure or malfunction, or any and all
      other commercial damages or losses), even if such Contributor
      has been advised of the possibility of such damages.

   9. Accepting Warranty or Additional Liability. While redistributing
      the Work or Derivative Works thereof, You may choose to offer,
      and charge a fee for, acceptance of support, warranty, indemnity,
      or other liability obligations and/or rights consistent with this
      License. However, in accepting such obligations, You may act only
      on Your own behalf and on Your sole responsibility, not on behalf
      of any other Contributor, and only if You agree to indemnify,
      defend, and hold each Contributor harmless for any liability
      incurred by, or claims asserted against, such Contributor by reason
      of your accepting any such warranty or additional liability.

   END OF TERMS AND CONDITIONS

   APPENDIX: How to apply the Apache License to your work.

      To apply the Apache License to your work, attach the following
      boilerplate notice, with the fields enclosed by brackets "[]"
      replaced with your own identifying information. (Don't include
      the brackets!)  The text should be enclosed in the appropriate
      comment syntax for the file format. We also recommend that a
      file or class name and description of purpose be included on the
      same "printed page" as the copyright notice for easier
      identification within third-party archives.

   Copyright (c) Microsoft Corporation.

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
```

## File: `packages/playwright-cli-stub/package.json`
```json
{
  "name": "playwright-cli",
  "version": "0.262.0",
  "description": "Deprecated package, use @playwright/cli instead.",
  "repository": {
    "type": "git",
    "url": "git+https://github.com/microsoft/playwright-cli.git"
  },
  "homepage": "https://playwright.dev",
  "scripts": {
    "lint": "echo OK",
    "build": "echo OK",
    "test": "echo OK"
  },
  "author": {
    "name": "Microsoft Corporation"
  },
  "license": "Apache-2.0"
}
```

## File: `packages/playwright-cli-stub/README.md`
```markdown
# 🎭 Playwright CLI

This package has moved to @playwright/cli.

```sh
$ npm i -g @playwright/cli
```
```

## File: `packages/playwright-mcp/.gitignore`
```
README.md
LICENSE
```

## File: `packages/playwright-mcp/.npmignore`
```
**/*
!README.md
!LICENSE
!cli.js
!index.*
!config.d.ts
```

## File: `packages/playwright-mcp/cli.js`
```javascript
#!/usr/bin/env node
/**
 * Copyright (c) Microsoft Corporation.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

const { program } = require('playwright-core/lib/utilsBundle');
const { decorateMCPCommand } = require('playwright-core/lib/tools/mcp/program');

if (process.argv.includes('install-browser')) {
  const argv = process.argv.map(arg => arg === 'install-browser' ? 'install' : arg);
  const { program: mainProgram } = require('playwright-core/lib/cli/program');
  mainProgram.parse(argv);
  return;
}

const packageJSON = require('./package.json');
const p = program.version('Version ' + packageJSON.version).name('Playwright MCP');
decorateMCPCommand(p, packageJSON.version)

void program.parseAsync(process.argv);
```

## File: `packages/playwright-mcp/config.d.ts`
```typescript
/**
 * Copyright (c) Microsoft Corporation.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

import type * as playwright from 'playwright';

export type ToolCapability =
  'config' |
  'core' |
  'core-navigation' |
  'core-tabs' |
  'core-input' |
  'core-install' |
  'network' |
  'pdf' |
  'storage' |
  'testing' |
  'vision' |
  'devtools';

export type Config = {
  /**
   * The browser to use.
   */
  browser?: {
    /**
     * The type of browser to use.
     */
    browserName?: 'chromium' | 'firefox' | 'webkit';

    /**
     * Keep the browser profile in memory, do not save it to disk.
     */
    isolated?: boolean;

    /**
     * Path to a user data directory for browser profile persistence.
     * Temporary directory is created by default.
     */
    userDataDir?: string;

    /**
     * Launch options passed to
     * @see https://playwright.dev/docs/api/class-browsertype#browser-type-launch-persistent-context
     *
     * This is useful for settings options like `channel`, `headless`, `executablePath`, etc.
     */
    launchOptions?: playwright.LaunchOptions;

    /**
     * Context options for the browser context.
     *
     * This is useful for settings options like `viewport`.
     */
    contextOptions?: playwright.BrowserContextOptions;

    /**
     * Chrome DevTools Protocol endpoint to connect to an existing browser instance in case of Chromium family browsers.
     */
    cdpEndpoint?: string;

    /**
     * CDP headers to send with the connect request.
     */
    cdpHeaders?: Record<string, string>;

    /**
     * Timeout in milliseconds for connecting to CDP endpoint. Defaults to 30000 (30 seconds). Pass 0 to disable timeout.
     */
    cdpTimeout?: number;

    /**
     * Remote endpoint to connect to an existing Playwright server.
     */
    remoteEndpoint?: string;

    /**
     * Paths to TypeScript files to add as initialization scripts for Playwright page.
     */
    initPage?: string[];

    /**
     * Paths to JavaScript files to add as initialization scripts.
     * The scripts will be evaluated in every page before any of the page's scripts.
     */
    initScript?: string[];
  },

  /**
   * Connect to a running browser instance (Edge/Chrome only). If specified, `browser`
   * config is ignored.
   * Requires the "Playwright MCP Bridge" browser extension to be installed.
   */
  extension?: boolean;

  server?: {
    /**
     * The port to listen on for SSE or MCP transport.
     */
    port?: number;

    /**
     * The host to bind the server to. Default is localhost. Use 0.0.0.0 to bind to all interfaces.
     */
    host?: string;

    /**
     * The hosts this server is allowed to serve from. Defaults to the host server is bound to.
     * This is not for CORS, but rather for the DNS rebinding protection.
     */
    allowedHosts?: string[];
  },

  /**
   * List of enabled tool capabilities. Possible values:
   *   - 'core': Core browser automation features.
   *   - 'pdf': PDF generation and manipulation.
   *   - 'vision': Coordinate-based interactions.
   *   - 'devtools': Developer tools features.
   */
  capabilities?: ToolCapability[];

  /**
   * Whether to save the Playwright session into the output directory.
   */
  saveSession?: boolean;

  /**
   * Reuse the same browser context between all connected HTTP clients.
   */
  sharedBrowserContext?: boolean;

  /**
   * Secrets are used to prevent LLM from getting sensitive data while
   * automating scenarios such as authentication.
   * Prefer the browser.contextOptions.storageState over secrets file as a more secure alternative.
   */
  secrets?: Record<string, string>;

  /**
   * The directory to save output files.
   */
  outputDir?: string;

  /**
   * Whether to save snapshots, console messages, network logs and other session logs to a file or to the standard output. Defaults to "stdout".
   */
  outputMode?: 'file' | 'stdout';

  console?: {
    /**
     * The level of console messages to return. Each level includes the messages of more severe levels. Defaults to "info".
     */
    level?: 'error' | 'warning' | 'info' | 'debug';
  },

  network?: {
    /**
     * List of origins to allow the browser to request. Default is to allow all. Origins matching both `allowedOrigins` and `blockedOrigins` will be blocked.
     *
     * Supported formats:
     * - Full origin: `https://example.com:8080` - matches only that origin
     * - Wildcard port: `http://localhost:*` - matches any port on localhost with http protocol
     */
    allowedOrigins?: string[];

    /**
     * List of origins to block the browser to request. Origins matching both `allowedOrigins` and `blockedOrigins` will be blocked.
     *
     * Supported formats:
     * - Full origin: `https://example.com:8080` - matches only that origin
     * - Wildcard port: `http://localhost:*` - matches any port on localhost with http protocol
     */
    blockedOrigins?: string[];
  };

  /**
   * Specify the attribute to use for test ids, defaults to "data-testid".
   */
  testIdAttribute?: string;

  timeouts?: {
    /*
     * Configures default action timeout: https://playwright.dev/docs/api/class-page#page-set-default-timeout. Defaults to 5000ms.
     */
    action?: number;

    /*
     * Configures default navigation timeout: https://playwright.dev/docs/api/class-page#page-set-default-navigation-timeout. Defaults to 60000ms.
     */
    navigation?: number;

    /**
     * Configures default expect timeout: https://playwright.dev/docs/test-timeouts#expect-timeout. Defaults to 5000ms.
     */
    expect?: number;
  };

  /**
   * Whether to send image responses to the client. Can be "allow", "omit", or "auto". Defaults to "auto", which sends images if the client can display them.
   */
  imageResponses?: 'allow' | 'omit';

  snapshot?: {
    /**
     * When taking snapshots for responses, specifies the mode to use.
     */
    mode?: 'incremental' | 'full' | 'none';
  };

  /**
   * Whether to allow file uploads from anywhere on the file system.
   * By default (false), file uploads are restricted to paths within the MCP roots only.
   */
  allowUnrestrictedFileAccess?: boolean;

  /**
   * Specify the language to use for code generation.
   */
  codegen?: 'typescript' | 'none';
};
```

## File: `packages/playwright-mcp/index.d.ts`
```typescript
#!/usr/bin/env node
/**
 * Copyright (c) Microsoft Corporation.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

import type { Server } from '@modelcontextprotocol/sdk/server/index.js';
import type { Config } from './config';
import type { BrowserContext } from 'playwright';

export declare function createConnection(config?: Config, contextGetter?: () => Promise<BrowserContext>): Promise<Server>;
export {};
```

## File: `packages/playwright-mcp/index.js`
```javascript
#!/usr/bin/env node
/**
 * Copyright (c) Microsoft Corporation.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

const { createConnection } = require('playwright-core/lib/tools/exports');
module.exports = { createConnection };
```

## File: `packages/playwright-mcp/package.json`
```json
{
  "name": "@playwright/mcp",
  "version": "0.0.68",
  "description": "Playwright Tools for MCP",
  "repository": {
    "type": "git",
    "url": "git+https://github.com/microsoft/playwright-mcp.git"
  },
  "homepage": "https://playwright.dev",
  "engines": {
    "node": ">=18"
  },
  "author": {
    "name": "Microsoft Corporation"
  },
  "license": "Apache-2.0",
  "mcpName": "io.github.microsoft/playwright-mcp",
  "scripts": {
    "lint": "node update-readme.js",
    "test": "playwright test",
    "ctest": "playwright test --project=chrome",
    "ftest": "playwright test --project=firefox",
    "wtest": "playwright test --project=webkit",
    "dtest": "MCP_IN_DOCKER=1 playwright test --project=chromium-docker",
    "build": "echo OK",
    "npm-publish": "npm run lint && npm run test && npm publish"
  },
  "exports": {
    "./package.json": "./package.json",
    ".": {
      "types": "./index.d.ts",
      "default": "./index.js"
    }
  },
  "dependencies": {
    "playwright": "1.59.0-alpha-1773608981000",
    "playwright-core": "1.59.0-alpha-1773608981000"
  },
  "bin": {
    "playwright-mcp": "cli.js"
  }
}
```

## File: `packages/playwright-mcp/playwright.config.ts`
```typescript
/**
 * Copyright (c) Microsoft Corporation.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

import { defineConfig } from '@playwright/test';

import type { TestOptions } from './tests/fixtures';

export default defineConfig<TestOptions>({
  testDir: './tests',
  fullyParallel: true,
  forbidOnly: !!process.env.CI,
  workers: process.env.CI ? 2 : undefined,
  reporter: 'list',
  projects: [
    { name: 'chrome' },
    ...process.env.MCP_IN_DOCKER ? [{
      name: 'chromium-docker',
      grep: /browser_navigate|browser_click/,
      use: {
        mcpBrowser: 'chromium',
        mcpMode: 'docker' as const
      }
    }] : [],
  ],
});
```

## File: `packages/playwright-mcp/update-readme.js`
```javascript
#!/usr/bin/env node
/**
 * Copyright (c) Microsoft Corporation.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
// @ts-check

const fs = require('fs')
const path = require('path')
const { execSync } = require('child_process');

const { browserTools } = require('playwright-core/lib/tools/exports');

const capabilities = /** @type {Record<string, string>} */ ({
  'core-navigation': 'Core automation',
  'core': 'Core automation',
  'core-tabs': 'Tab management',
  'core-input': 'Core automation',
  'core-install': 'Browser installation',
  'config': 'Configuration',
  'network': 'Network',
  'storage': 'Storage',
  'devtools': 'DevTools',
  'vision': 'Coordinate-based',
  'pdf': 'PDF generation',
  'testing': 'Test assertions',
});

const knownCapabilities = new Set(Object.keys(capabilities));
const unknownCapabilities = [...new Set(browserTools.map(tool => tool.capability))].filter(cap => !knownCapabilities.has(cap));
if (unknownCapabilities.length)
  throw new Error(`Unknown tool capabilities: ${unknownCapabilities.join(', ')}. Please update the capabilities map in ${path.basename(__filename)}.`);

/** @type {Record<string, any[]>} */
const toolsByCapability = {};
for (const capability of Object.keys(capabilities)) {
  const title = capabilityTitle(capability);
  let tools = browserTools.filter(tool => tool.capability === capability && !tool.skillOnly);
  tools = (toolsByCapability[title] || []).concat(tools);
  toolsByCapability[title] = tools;
}
for (const [, tools] of Object.entries(toolsByCapability))
  tools.sort((a, b) => a.schema.name.localeCompare(b.schema.name));

/**
 * @param {string} capability
 * @returns {string}
 */
function capabilityTitle(capability) {
  const title = capabilities[capability];
  return capability.startsWith('core') ? title : `${title} (opt-in via --caps=${capability})`;
}

/**
 * @param {any} tool
 * @returns {string[]}
 */
function formatToolForReadme(tool) {
  const lines = /** @type {string[]} */ ([]);
  lines.push(`<!-- NOTE: This has been generated via ${path.basename(__filename)} -->`);
  lines.push(``);
  lines.push(`- **${tool.name}**`);
  lines.push(`  - Title: ${tool.title}`);
  lines.push(`  - Description: ${tool.description}`);

  const inputSchema = /** @type {any} */ (tool.inputSchema ? tool.inputSchema.toJSONSchema() : {});
  const requiredParams = inputSchema.required || [];
  if (inputSchema.properties && Object.keys(inputSchema.properties).length) {
    lines.push(`  - Parameters:`);
    Object.entries(inputSchema.properties).forEach(([name, param]) => {
      const optional = !requiredParams.includes(name);
      const meta = /** @type {string[]} */ ([]);
      if (param.type)
        meta.push(param.type);
      if (optional)
        meta.push('optional');
      lines.push(`    - \`${name}\` ${meta.length ? `(${meta.join(', ')})` : ''}: ${param.description}`);
    });
  } else {
    lines.push(`  - Parameters: None`);
  }
  lines.push(`  - Read-only: **${tool.type === 'readOnly'}**`);
  lines.push('');
  return lines;
}

/**
 * @param {string} content
 * @param {string} startMarker
 * @param {string} endMarker
 * @param {string[]} generatedLines
 * @returns {Promise<string>}
 */
async function updateSection(content, startMarker, endMarker, generatedLines) {
  const startMarkerIndex = content.indexOf(startMarker);
  const endMarkerIndex = content.indexOf(endMarker);
  if (startMarkerIndex === -1 || endMarkerIndex === -1)
    throw new Error('Markers for generated section not found in README');

  return [
    content.slice(0, startMarkerIndex + startMarker.length),
    '',
    generatedLines.join('\n'),
    '',
    content.slice(endMarkerIndex),
  ].join('\n');
}

/**
 * @param {string} content
 * @returns {Promise<string>}
 */
async function updateTools(content) {
  console.log('Loading tool information from compiled modules...');

  const generatedLines = /** @type {string[]} */ ([]);
  for (const [capability, tools] of Object.entries(toolsByCapability)) {
    console.log('Updating tools for capability:', capability);
    generatedLines.push(`<details>\n<summary><b>${capability}</b></summary>`);
    generatedLines.push('');
    for (const tool of tools)
      generatedLines.push(...formatToolForReadme(tool.schema));
    generatedLines.push(`</details>`);
    generatedLines.push('');
  }

  const startMarker = `<!--- Tools generated by ${path.basename(__filename)} -->`;
  const endMarker = `<!--- End of tools generated section -->`;
  return updateSection(content, startMarker, endMarker, generatedLines);
}

/**
 * @param {string} content
 * @returns {Promise<string>}
 */
async function updateOptions(content) {
  console.log('Listing options...');
  execSync('node cli.js --help > help.txt');
  const output = fs.readFileSync('help.txt');
  fs.unlinkSync('help.txt');
  const lines = output.toString().split('\n');
  const firstLine = lines.findIndex(line => line.includes('--version'));
  lines.splice(0, firstLine + 1);
  const lastLine = lines.findIndex(line => line.includes('--help'));
  lines.splice(lastLine);

  /**
   * @type {{ name: string, value: string }[]}
   */
  const options = [];
  for (let line of lines) {
    if (line.startsWith('  --')) {
      const l = line.substring('  --'.length);
      const gapIndex = l.indexOf('  ');
      const name = l.substring(0, gapIndex).trim();
      const value = l.substring(gapIndex).trim();
      options.push({ name, value });
    } else {
      const value = line.trim();
      options[options.length - 1].value += ' ' + value;
    }
  }

  const table = [];
  table.push(`| Option | Description |`);
  table.push(`|--------|-------------|`);
  for (const option of options) {
    const prefix = option.name.split(' ')[0];
    const envName = `PLAYWRIGHT_MCP_` + prefix.toUpperCase().replace(/-/g, '_');
    table.push(`| --${option.name} | ${option.value}<br>*env* \`${envName}\` |`);
  }

  if (process.env.PRINT_ENV) {
    const envTable = [];
    envTable.push(`| Environment |`);
    envTable.push(`|-------------|`);
    for (const option of options) {
      const prefix = option.name.split(' ')[0];
      const envName = `PLAYWRIGHT_MCP_` + prefix.toUpperCase().replace(/-/g, '_');
      envTable.push(`| \`${envName}\` ${option.value} |`);
    }
    console.log(envTable.join('\n'));
  }

  const startMarker = `<!--- Options generated by ${path.basename(__filename)} -->`;
  const endMarker = `<!--- End of options generated section -->`;
  return updateSection(content, startMarker, endMarker, table);
}

/**
 * @param {string} content
 * @returns {Promise<string>}
 */
async function updateConfig(content) {
  console.log('Updating config schema from config.d.ts...');
  const configPath = path.join(__dirname, 'config.d.ts');
  const configContent = await fs.promises.readFile(configPath, 'utf-8');

  // Extract the Config type definition
  const configTypeMatch = configContent.match(/export type Config = (\{[\s\S]*?\n\});/);
  if (!configTypeMatch)
    throw new Error('Config type not found in config.d.ts');

  const configType = configTypeMatch[1]; // Use capture group to get just the object definition

  const startMarker = `<!--- Config generated by ${path.basename(__filename)} -->`;
  const endMarker = `<!--- End of config generated section -->`;
  return updateSection(content, startMarker, endMarker, [
    '```typescript',
    configType,
    '```',
  ]);
}

/**
 * @param {string} filePath
 */
async function copyToPackage(filePath) {
  await fs.promises.copyFile(path.join(__dirname, '../../', filePath), path.join(__dirname, filePath));
  console.log(`${filePath} copied successfully`);
}

async function updateReadme() {
  const readmePath = path.join(__dirname, '../../README.md');
  const readmeContent = await fs.promises.readFile(readmePath, 'utf-8');
  const withTools = await updateTools(readmeContent);
  const withOptions = await updateOptions(withTools);
  const withConfig = await updateConfig(withOptions);
  await fs.promises.writeFile(readmePath, withConfig, 'utf-8');
  console.log('README updated successfully');

  await copyToPackage('README.md');
  await copyToPackage('LICENSE');
}

updateReadme().catch(err => {
  console.error('Error updating README:', err);
  process.exit(1);
});
```

## File: `packages/playwright-mcp/src/README.md`
```markdown
# Where is the source?

Playwright MCP source code is located in the [Playwright monorepo](https://github.com/microsoft/playwright/blob/main/packages/playwright-core/src/tools/mcp). Please refer to the contributor's guide in [CONTRIBUTING.md](../CONTRIBUTING.md) for more details.
```

## File: `packages/playwright-mcp/tests/capabilities.spec.ts`
```typescript
/**
 * Copyright (c) Microsoft Corporation.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

import { test, expect } from './fixtures';

test('test snapshot tool list', async ({ client }) => {
  const { tools } = await client.listTools();
  expect(new Set(tools.map(t => t.name))).toEqual(new Set([
    'browser_click',
    'browser_console_messages',
    'browser_drag',
    'browser_evaluate',
    'browser_file_upload',
    'browser_fill_form',
    'browser_handle_dialog',
    'browser_hover',
    'browser_select_option',
    'browser_type',
    'browser_close',
    'browser_navigate_back',
    'browser_navigate',
    'browser_network_requests',
    'browser_press_key',
    'browser_resize',
    'browser_run_code',
    'browser_snapshot',
    'browser_tabs',
    'browser_take_screenshot',
    'browser_wait_for',
  ]));
});

test('test capabilities (pdf)', async ({ startClient }) => {
  const { client } = await startClient({
    args: ['--caps=pdf'],
  });
  const { tools } = await client.listTools();
  const toolNames = tools.map(t => t.name);
  expect(toolNames).toContain('browser_pdf_save');
});

test('test capabilities (vision)', async ({ startClient }) => {
  const { client } = await startClient({
    args: ['--caps=vision'],
  });
  const { tools } = await client.listTools();
  const toolNames = tools.map(t => t.name);
  expect(toolNames).toContain('browser_mouse_move_xy');
  expect(toolNames).toContain('browser_mouse_click_xy');
  expect(toolNames).toContain('browser_mouse_drag_xy');
});

test('support for legacy --vision option', async ({ startClient }) => {
  const { client } = await startClient({
    args: ['--vision'],
  });
  const { tools } = await client.listTools();
  const toolNames = tools.map(t => t.name);
  expect(toolNames).toContain('browser_mouse_move_xy');
  expect(toolNames).toContain('browser_mouse_click_xy');
  expect(toolNames).toContain('browser_mouse_drag_xy');
});
```

## File: `packages/playwright-mcp/tests/cli.spec.ts`
```typescript
/**
 * Copyright (c) Microsoft Corporation.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
import child_process from 'child_process';
import path from 'path';
import { test, expect } from './fixtures';

const cliPath = path.resolve(__dirname, '..', 'cli.js');

test('install-browser --help', async () => {
  const output = child_process.execSync(`node ${cliPath} install-browser --help`, { encoding: 'utf-8' });
  expect(output).toContain('install');
});
```

## File: `packages/playwright-mcp/tests/click.spec.ts`
```typescript
/**
 * Copyright (c) Microsoft Corporation.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

import { test, expect } from './fixtures';

test('browser_click', async ({ client, server }) => {
  server.setContent('/', `
    <title>Title</title>
    <button>Submit</button>
    <script>
      const button = document.querySelector('button');
      button.addEventListener('click', () => {
        button.focus(); // without manual focus, webkit focuses body
      });
    </script>
  `, 'text/html');

  expect(await client.callTool({
    name: 'browser_navigate',
    arguments: { url: server.PREFIX },
  })).toHaveResponse({
    code: `await page.goto('${server.PREFIX}');`,
    snapshot: expect.stringContaining(`- button \"Submit\" [ref=e2]`),
  });

  expect(await client.callTool({
    name: 'browser_click',
    arguments: {
      element: 'Submit button',
      ref: 'e2',
    },
  })).toHaveResponse({
    code: `await page.getByRole('button', { name: 'Submit' }).click();`,
    snapshot: expect.stringContaining(`button "Submit" [active] [ref=e2]`),
  });
});
```

## File: `packages/playwright-mcp/tests/core.spec.ts`
```typescript
/**
 * Copyright (c) Microsoft Corporation.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

import { test, expect } from './fixtures';

test('browser_navigate', async ({ client, server }) => {
  expect(await client.callTool({
    name: 'browser_navigate',
    arguments: { url: server.HELLO_WORLD },
  })).toHaveResponse({
    code: `await page.goto('${server.HELLO_WORLD}');`,
    snapshot: expect.stringContaining(`generic [active] [ref=e1]: Hello, world!`),
  });
});
```

## File: `packages/playwright-mcp/tests/fixtures.ts`
```typescript
/**
 * Copyright (c) Microsoft Corporation.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

import fs from 'fs';
import path from 'path';
import { chromium } from 'playwright';

import { test as baseTest, expect as baseExpect } from '@playwright/test';
import { StdioClientTransport } from '@modelcontextprotocol/sdk/client/stdio.js';
import { Client } from '@modelcontextprotocol/sdk/client/index.js';
import { ListRootsRequestSchema } from '@modelcontextprotocol/sdk/types.js';
import { TestServer } from './testserver/index';

import type { Config } from '../config';
import type { BrowserContext } from 'playwright';
import type { Transport } from '@modelcontextprotocol/sdk/shared/transport.js';
import type { Stream } from 'stream';

export type TestOptions = {
  mcpArgs: string[] | undefined;
  mcpBrowser: string | undefined;
  mcpMode: 'docker' | undefined;
};

type CDPServer = {
  endpoint: string;
  start: () => Promise<BrowserContext>;
};

export type StartClient = (options?: {
  clientName?: string,
  args?: string[],
  config?: Config,
  roots?: { name: string, uri: string }[],
  rootsResponseDelay?: number,
  extensionToken?: string,
}) => Promise<{ client: Client, stderr: () => string }>;


type TestFixtures = {
  client: Client;
  startClient: StartClient;
  wsEndpoint: string;
  cdpServer: CDPServer;
  server: TestServer;
  httpsServer: TestServer;
  mcpHeadless: boolean;
};

type WorkerFixtures = {
  _workerServers: { server: TestServer, httpsServer: TestServer };
};

export const test = baseTest.extend<TestFixtures & TestOptions, WorkerFixtures>({

  mcpArgs: [undefined, { option: true }],

  client: async ({ startClient }, use) => {
    const { client } = await startClient();
    await use(client);
  },

  startClient: async ({ mcpHeadless, mcpBrowser, mcpMode, mcpArgs }, use, testInfo) => {
    const configDir = path.dirname(test.info().config.configFile!);
    const clients: Client[] = [];

    await use(async options => {
      const args: string[] = mcpArgs ?? [];
      if (process.env.CI && process.platform === 'linux')
        args.push('--no-sandbox');
      if (mcpHeadless)
        args.push('--headless');
      if (mcpBrowser)
        args.push(`--browser=${mcpBrowser}`);
      if (options?.args)
        args.push(...options.args);
      if (options?.config) {
        const configFile = testInfo.outputPath('config.json');
        await fs.promises.writeFile(configFile, JSON.stringify(options.config, null, 2));
        args.push(`--config=${path.relative(configDir, configFile)}`);
      }

      const client = new Client({ name: options?.clientName ?? 'test', version: '1.0.0' }, options?.roots ? { capabilities: { roots: {} } } : undefined);
      if (options?.roots) {
        client.setRequestHandler(ListRootsRequestSchema, async request => {
          if (options.rootsResponseDelay)
            await new Promise(resolve => setTimeout(resolve, options.rootsResponseDelay));
          return {
            roots: options.roots,
          };
        });
      }
      const { transport, stderr } = await createTransport(args, mcpMode, testInfo.outputPath('ms-playwright'), options?.extensionToken);
      let stderrBuffer = '';
      stderr?.on('data', data => {
        if (process.env.PWMCP_DEBUG)
          process.stderr.write(data);
        stderrBuffer += data.toString();
      });
      clients.push(client);
      await client.connect(transport);
      await client.ping();
      return { client, stderr: () => stderrBuffer };
    });

    await Promise.all(clients.map(client => client.close()));
  },

  wsEndpoint: async ({ }, use) => {
    const browserServer = await chromium.launchServer();
    await use(browserServer.wsEndpoint());
    await browserServer.close();
  },

  cdpServer: async ({ mcpBrowser }, use, testInfo) => {
    test.skip(!['chrome', 'msedge', 'chromium'].includes(mcpBrowser!), 'CDP is not supported for non-Chromium browsers');

    let browserContext: BrowserContext | undefined;
    const port = 3200 + test.info().parallelIndex;
    await use({
      endpoint: `http://localhost:${port}`,
      start: async () => {
        if (browserContext)
          throw new Error('CDP server already exists');
        browserContext = await chromium.launchPersistentContext(testInfo.outputPath('cdp-user-data-dir'), {
          channel: mcpBrowser,
          headless: true,
          args: [
            `--remote-debugging-port=${port}`,
          ],
        });
        return browserContext;
      }
    });
    await browserContext?.close();
  },

  mcpHeadless: async ({ headless }, use) => {
    await use(headless);
  },

  mcpBrowser: ['chrome', { option: true }],

  mcpMode: [undefined, { option: true }],

  _workerServers: [async ({ }, use, workerInfo) => {
    const port = 8907 + workerInfo.workerIndex * 4;
    const server = await TestServer.create(port);

    const httpsPort = port + 1;
    const httpsServer = await TestServer.createHTTPS(httpsPort);

    await use({ server, httpsServer });

    await Promise.all([
      server.stop(),
      httpsServer.stop(),
    ]);
  }, { scope: 'worker' }],

  server: async ({ _workerServers }, use) => {
    _workerServers.server.reset();
    await use(_workerServers.server);
  },

  httpsServer: async ({ _workerServers }, use) => {
    _workerServers.httpsServer.reset();
    await use(_workerServers.httpsServer);
  },
});

async function createTransport(args: string[], mcpMode: TestOptions['mcpMode'], profilesDir: string, extensionToken?: string): Promise<{
  transport: Transport,
  stderr: Stream | null,
}> {
  if (mcpMode === 'docker') {
    const dockerArgs = ['run', '--rm', '-i', '--network=host', '-v', `${test.info().project.outputDir}:/app/test-results`];
    const transport = new StdioClientTransport({
      command: 'docker',
      args: [...dockerArgs, 'playwright-mcp-dev:latest', ...args],
    });
    return {
      transport,
      stderr: transport.stderr,
    };
  }

  const transport = new StdioClientTransport({
    command: 'node',
    args: [path.join(__dirname, '../cli.js'), ...args],
    cwd: path.dirname(test.info().config.configFile!),
    stderr: 'pipe',
    env: {
      ...process.env,
      DEBUG: 'pw:mcp:test',
      DEBUG_COLORS: '0',
      DEBUG_HIDE_DATE: '1',
      PWMCP_PROFILES_DIR_FOR_TEST: profilesDir,
      ...(extensionToken ? { PLAYWRIGHT_MCP_EXTENSION_TOKEN: extensionToken } : {}),
    },
  });
  return {
    transport,
    stderr: transport.stderr!,
  };
}

type Response = Awaited<ReturnType<Client['callTool']>>;

export const expect = baseExpect.extend({
  toHaveResponse(response: Response, object: any) {
    const parsed = parseResponse(response);
    const isNot = this.isNot;
    try {
      if (isNot)
        expect(parsed).not.toEqual(expect.objectContaining(object));
      else
        expect(parsed).toEqual(expect.objectContaining(object));
    } catch (e: any) {
      return {
        pass: isNot,
        message: () => e.message,
      };
    }
    return {
      pass: !isNot,
      message: () => ``,
    };
  },
});

export function formatOutput(output: string): string[] {
  return output.split('\n').map(line => line.replace(/^pw:mcp:test /, '').replace(/user data dir.*/, 'user data dir').trim()).filter(Boolean);
}

function parseResponse(response: any) {
  const text = response.content[0].text;
  const sections = parseSections(text);

  const error = sections.get('Error');
  const result = sections.get('Result');
  const code = sections.get('Ran Playwright code');
  const tabs = sections.get('Open tabs');
  const pageState = sections.get('Page state');
  const snapshot = sections.get('Snapshot');
  const consoleMessages = sections.get('New console messages');
  const modalState = sections.get('Modal state');
  const downloads = sections.get('Downloads');
  const codeNoFrame = code?.replace(/^```js\n/, '').replace(/\n```$/, '');
  const isError = response.isError;
  const attachments = response.content.slice(1);

  return {
    error,
    result,
    code: codeNoFrame,
    tabs,
    pageState,
    snapshot,
    consoleMessages,
    modalState,
    downloads,
    isError,
    attachments,
  };
}

function parseSections(text: string): Map<string, string> {
  const sections = new Map<string, string>();
  const sectionHeaders = text.split(/^### /m).slice(1); // Remove empty first element

  for (const section of sectionHeaders) {
    const firstNewlineIndex = section.indexOf('\n');
    if (firstNewlineIndex === -1)
      continue;

    const sectionName = section.substring(0, firstNewlineIndex);
    const sectionContent = section.substring(firstNewlineIndex + 1).trim();
    sections.set(sectionName, sectionContent);
  }

  return sections;
}
```

## File: `packages/playwright-mcp/tests/library.spec.ts`
```typescript
/**
 * Copyright (c) Microsoft Corporation.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
import child_process from 'child_process';
import fs from 'fs/promises';
import { test, expect } from './fixtures';

test('library can be used from CommonJS', { annotation: { type: 'issue', description: 'https://github.com/microsoft/playwright-mcp/issues/456' } }, async ({}, testInfo) => {
  const file = testInfo.outputPath('main.cjs');
  await fs.writeFile(file, `
    import('@playwright/mcp')
      .then(playwrightMCP => playwrightMCP.createConnection())
      .then(() => console.log('OK'));
 `);
  expect(child_process.execSync(`node ${file}`, { encoding: 'utf-8' })).toContain('OK');
});
```

## File: `packages/playwright-mcp/tests/testserver/cert.pem`
```
-----BEGIN CERTIFICATE-----
MIIFCjCCAvKgAwIBAgIULU/gkDm8IqC7PG8u3RID0AYyP6gwDQYJKoZIhvcNAQEL
BQAwGjEYMBYGA1UEAwwPcGxheXdyaWdodC10ZXN0MB4XDTIzMDgxMDIyNTc1MFoX
DTMzMDgwNzIyNTc1MFowGjEYMBYGA1UEAwwPcGxheXdyaWdodC10ZXN0MIICIjAN
BgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEArbS99qjKcnHr5G0Zc2xhDaOZnjQv
Fbiqxf/nbXt/7WaqryzpVKu7AT1ainBvuPEo7If9DhVnfF//2pGl0gbU31OU4/mr
ymQmczGEyZvOBDsZhtCif54o5OoO0BjhODNT8OWec9RT87n6RkH58MHlOi8xsPxQ
9n5U1CN/h2DyQF3aRKunEFCgtwPKWSjG+J/TAI9i0aSENXPiR8wjTrjg79s8Ehuj
NN8Wk6rKLU3sepG3GIMID5vLsVa2t9xqn562sP95Ee+Xp2YX3z7oYK99QCJdzacw
alhMHob1GCEKjDyxsD2IFRi7Dysiutfyzy3pMo6NALxFrwKVhWX0L4zVFIsI6JlV
dK8dHmDk0MRSqgB9sWXvEfSTXADEe8rncFSFpFz4Z8RNLmn5YSzQJzokNn41DUCP
dZTlTkcGTqvn5NqoY4sOV8rkFbgmTcqyijV/sebPjxCbJNcNmaSWa9FJ5IjRTpzM
38wLmxn+eKGK68n2JB3P7JP6LtsBShQEpXAF3rFfyNsP1bjquvGZVSjV8w/UwPE4
kV5eq3j3D4913Zfxvzjp6PEmhStG0EQtIXvx/TRoYpaNWypIgZdbkZQp1HUIQL15
D2Web4nazP3so1FC3ZgbrJZ2ozoadjLMp49NcSFdh+WRyVKuo0DIqR0zaiAzzf2D
G1q7TLKimM3XBMUCAwEAAaNIMEYwCQYDVR0TBAIwADALBgNVHQ8EBAMCBeAwLAYD
VR0RBCUwI4IJbG9jYWxob3N0hwR/AAABhxAAAAAAAAAAAAAAAAAAAAABMA0GCSqG
SIb3DQEBCwUAA4ICAQAvC5M1JFc21WVSLPvE2iVbt4HmirO3EENdDqs+rTYG5VJG
iE5ZuI6h/LjS5ptTfKovXQKaMr3pwp1pLMd/9q+6ZR1Hs9Z2wF6OZan4sb0uT32Y
1KGlj86QMiiSLdrJ/1Z9JHskHYNCep1ZTsUhGk0qqiNv+G3K2y7ZpvrT/xlnYMth
KLTuSVUwM8BBEPrCRLoXuaEy0LnvMvMVepIfP8tnMIL6zqmj3hXMPe4r4OFV/C5o
XX25bC7GyuPWIRYn2OWP92J1CODZD1rGRoDtmvqrQpHdeX9RYcKH0ZLZoIf5L3Hf
pPUtVkw3QGtjvKeG3b9usxaV9Od2Z08vKKk1PRkXFe8gqaeyicK7YVIOMTSuspAf
JeJEHns6Hg61Exbo7GwdX76xlmQ/Z43E9BPHKgLyZ9WuJ0cysqN4aCyvS9yws9to
ki7iMZqJUsmE2o09n9VaEsX6uQANZtLjI9wf+IgJuueDTNrkzQkhU7pbaPMsSG40
AgGY/y4BR0H8sbhNnhqtZH7RcXV9VCJoPBAe+YiuXRiXyZHWxwBRyBE3e7g4MKHg
hrWtaWUAs7gbavHwjqgU63iVItDSk7t4fCiEyObjK09AaNf2DjjaSGf8YGza4bNy
BjYinYJ6/eX//gp+abqfocFbBP7D9zRDgMIbVmX/Ey6TghKiLkZOdbzcpO4Wgg==
-----END CERTIFICATE-----
```

## File: `packages/playwright-mcp/tests/testserver/index.ts`
```typescript
/**
 * Copyright 2017 Google Inc. All rights reserved.
 * Modifications copyright (c) Microsoft Corporation.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

import fs from 'fs';
import http from 'http';
import https from 'https';
import path from 'path';
import debug from 'debug';

const fulfillSymbol = Symbol('fulfil callback');
const rejectSymbol = Symbol('reject callback');

export class TestServer {
  private _server: http.Server;
  readonly debugServer: any;
  private _routes = new Map<string, (request: http.IncomingMessage, response: http.ServerResponse) => any>();
  private _csp = new Map<string, string>();
  private _extraHeaders = new Map<string, object>();
  private _requestSubscribers = new Map<string, Promise<any>>();
  readonly PORT: number;
  readonly PREFIX: string;
  readonly CROSS_PROCESS_PREFIX: string;
  readonly HELLO_WORLD: string;

  static async create(port: number): Promise<TestServer> {
    const server = new TestServer(port);
    await new Promise(x => server._server.once('listening', x));
    return server;
  }

  static async createHTTPS(port: number): Promise<TestServer> {
    const server = new TestServer(port, {
      key: await fs.promises.readFile(path.join(path.dirname(__filename), 'key.pem')),
      cert: await fs.promises.readFile(path.join(path.dirname(__filename), 'cert.pem')),
      passphrase: 'aaaa',
    });
    await new Promise(x => server._server.once('listening', x));
    return server;
  }

  constructor(port: number, sslOptions?: object) {
    if (sslOptions)
      this._server = https.createServer(sslOptions, this._onRequest.bind(this));
    else
      this._server = http.createServer(this._onRequest.bind(this));
    this._server.listen(port);
    this.debugServer = debug('pw:testserver');

    const cross_origin = '127.0.0.1';
    const same_origin = 'localhost';
    const protocol = sslOptions ? 'https' : 'http';
    this.PORT = port;
    this.PREFIX = `${protocol}://${same_origin}:${port}/`;
    this.CROSS_PROCESS_PREFIX = `${protocol}://${cross_origin}:${port}/`;
    this.HELLO_WORLD = `${this.PREFIX}hello-world`;
  }

  setCSP(path: string, csp: string) {
    this._csp.set(path, csp);
  }

  setExtraHeaders(path: string, object: Record<string, string>) {
    this._extraHeaders.set(path, object);
  }

  async stop() {
    this.reset();
    await new Promise(x => this._server.close(x));
  }

  route(path: string, handler: (request: http.IncomingMessage, response: http.ServerResponse) => any) {
    this._routes.set(path, handler);
  }

  setContent(path: string, content: string, mimeType: string) {
    this.route(path, (req, res) => {
      res.writeHead(200, { 'Content-Type': mimeType });
      res.end(mimeType === 'text/html' ? `<!DOCTYPE html>${content}` : content);
    });
  }

  redirect(from: string, to: string) {
    this.route(from, (req, res) => {
      const headers = this._extraHeaders.get(req.url!) || {};
      res.writeHead(302, { ...headers, location: to });
      res.end();
    });
  }

  waitForRequest(path: string): Promise<http.IncomingMessage> {
    let promise = this._requestSubscribers.get(path);
    if (promise)
      return promise;
    let fulfill, reject;
    promise = new Promise((f, r) => {
      fulfill = f;
      reject = r;
    });
    promise[fulfillSymbol] = fulfill;
    promise[rejectSymbol] = reject;
    this._requestSubscribers.set(path, promise);
    return promise;
  }

  reset() {
    this._routes.clear();
    this._csp.clear();
    this._extraHeaders.clear();
    this._server.closeAllConnections();
    const error = new Error('Static Server has been reset');
    for (const subscriber of this._requestSubscribers.values())
      subscriber[rejectSymbol].call(null, error);
    this._requestSubscribers.clear();

    this.setContent('/favicon.ico', '', 'image/x-icon');

    this.setContent('/', ``, 'text/html');

    this.setContent('/hello-world', `
      <title>Title</title>
      <body>Hello, world!</body>
    `, 'text/html');
  }

  _onRequest(request: http.IncomingMessage, response: http.ServerResponse) {
    request.on('error', error => {
      if ((error as any).code === 'ECONNRESET')
        response.end();
      else
        throw error;
    });
    (request as any).postBody = new Promise(resolve => {
      const chunks: Buffer[] = [];
      request.on('data', chunk => {
        chunks.push(chunk);
      });
      request.on('end', () => resolve(Buffer.concat(chunks)));
    });
    const path = request.url || '/';
    this.debugServer(`request ${request.method} ${path}`);
    // Notify request subscriber.
    if (this._requestSubscribers.has(path)) {
      this._requestSubscribers.get(path)![fulfillSymbol].call(null, request);
      this._requestSubscribers.delete(path);
    }
    const handler = this._routes.get(path);
    if (handler) {
      handler.call(null, request, response);
    } else {
      response.writeHead(404);
      response.end();
    }
  }
}
```

## File: `packages/playwright-mcp/tests/testserver/key.pem`
```
-----BEGIN PRIVATE KEY-----
MIIJQgIBADANBgkqhkiG9w0BAQEFAASCCSwwggkoAgEAAoICAQCttL32qMpycevk
bRlzbGENo5meNC8VuKrF/+dte3/tZqqvLOlUq7sBPVqKcG+48Sjsh/0OFWd8X//a
kaXSBtTfU5Tj+avKZCZzMYTJm84EOxmG0KJ/nijk6g7QGOE4M1Pw5Z5z1FPzufpG
QfnwweU6LzGw/FD2flTUI3+HYPJAXdpEq6cQUKC3A8pZKMb4n9MAj2LRpIQ1c+JH
zCNOuODv2zwSG6M03xaTqsotTex6kbcYgwgPm8uxVra33Gqfnraw/3kR75enZhff
Puhgr31AIl3NpzBqWEwehvUYIQqMPLGwPYgVGLsPKyK61/LPLekyjo0AvEWvApWF
ZfQvjNUUiwjomVV0rx0eYOTQxFKqAH2xZe8R9JNcAMR7yudwVIWkXPhnxE0uaflh
LNAnOiQ2fjUNQI91lOVORwZOq+fk2qhjiw5XyuQVuCZNyrKKNX+x5s+PEJsk1w2Z
pJZr0UnkiNFOnMzfzAubGf54oYrryfYkHc/sk/ou2wFKFASlcAXesV/I2w/VuOq6
8ZlVKNXzD9TA8TiRXl6rePcPj3Xdl/G/OOno8SaFK0bQRC0he/H9NGhilo1bKkiB
l1uRlCnUdQhAvXkPZZ5vidrM/eyjUULdmBuslnajOhp2Msynj01xIV2H5ZHJUq6j
QMipHTNqIDPN/YMbWrtMsqKYzdcExQIDAQABAoICAGqXttpdyZ1g+vg5WpzRrNzJ
v8KtExepMmI+Hq24U1BC6AqG7MfgeejQ1XaOeIBsvEgpSsgRqmdQIZjmN3Mibg59
I6ih1SFlQ5L8mBd/XHSML6Xi8VSOoVmXp29bVRk/pgr1XL6HVN0DCumCIvXyhc+m
lj+dFbGs5DEpd2CDxSRqcz4gd2wzjevAj7MWqsJ2kOyPEHzFD7wdWIXmZuQv3xhQ
2BPkkcon+5qx+07BupOcR1brUU8Cs4QnSgiZYXSB2GnU215+P/mhVJTR7ZcnGRz5
+cXxCmy3sj4pYs1juS1FMWSM3azUeDVeqvks+vrXmXpEr5H79mbmlwo8/hMPwNDO
07HRZwa8T01aT9EYVm0lIOYjMF/2f6j6cu2apJtjXICOksR2HefRBVXQirOxRHma
9XAYfNkZ/2164ZbgFmJv9khFnegPEuth9tLVdFIeGSmsG0aX9tH63zGT2NROyyLc
QXPqsDl2CxCYPRs2oiGkM9dnfP1wAOp96sq42GIuN7ykfqfRnwAIvvnLKvyCq1vR
pIno3CIX6vnzt+1/Hrmv13b0L6pJPitpXwKWHv9zJKBTpN8HEzP3Qmth2Ef60/7/
CBo1PVTd1A6zcU7816flg7SCY+Vk+OxVHV3dGBIIqN9SfrQ8BPcOl6FNV5Anbrnv
CpSw+LzH9n5xympDnk0BAoIBAQDjenvDfCnrNVeqx8+sYaYey4/WPVLXOQhREvRY
oOtX9eqlNSi20+Wl+iuXmyj8wdHrDET7rfjCbpDQ7u105yzLw4gy4qIRDKZ1nE45
YX+tm8mZgBqRnTp0DoGOArqmp3IKXJtUYmpbTz9tOfY7Usb1o1epb4winEB+Pl+8
mgXOEo8xvWBzKeRA7tE73V64Mwbvbo9Ff2EguhXweQP29yBkEjT4iViayuHUmyPt
hOVSMj2oFQuQGPdhAk7nUXojSGK/Zas/AGpH9CHH9De0h4m08vd3oM4vj0HwzgjU
Co9aRa9SAH7EiaocOTcjDRPxWdZPHhxmrVRIYlF0MNmOAkXJAoIBAQDDfEqu4sNi
pq74VXVatQqhzCILZo+o48bdgEjF7mF99mqPj8rwIDrEoEriDK861kenLc3vWKRY
5wh1iX3S896re9kUMoxx6p4heYTcsOJ9BbkcpT8bJPZx9gBJb4jJENeVf1exf6sG
RhFnulpzReRRaUjX2yAkyUPfc8YcUt+Nalrg+2W0fzeLCUpABCAcj2B1Vv7qRZHj
oEtlCV5Nz+iMhrwIa16g9c8wGt5DZb4PI+VIJ6EYkdsjhgqIF0T/wDq9/habGBPo
mHN+/DX3hCJWN2QgoVGJskHGt0zDMgiEgXfLZ2Grl02vQtq+mW2O2vGVeUd9Y5Ew
RUiY4bSRTrUdAoIBAHxL1wiP9c/By+9TUtScXssA681ioLtdPIAgXUd4VmAvzVEM
ZPzRd/BjbCJg89p4hZ1rjN4Ax6ZmB9dCVpnEH6QPaYJ0d53dTa+CAvQzpDJWp6eq
adobEW+M5ZmVQCwD3rpus6k+RWMzQDMMstDjgDeEU0gP3YCj5FGW/3TsrDNXzMqe
8e67ey9Hzyho43K+3xFBViPhYE8jnw1Q8quliRtlH3CWi8W5CgDD7LPCJBPvw+Tt
6u2H1tQ5EKgwyw4wZVSz1wiLz4cVjMfXWADa9pHbGQFS6pbuLlfIHObQBliLLysd
ficiGcNmOAx8/uKn9gQxLc+k8iLDJkLY1mdUMpECggEAJLl87k37ltTpmg2z9k58
qNjIrIugAYKJIaOwCD84YYmhi0bgQSxM3hOe/ciUQuFupKGeRpDIj0sX87zYvoDC
HEUwCvNUHzKMco15wFwasJIarJ7+tALFqbMlaqZhdCSN27AIsXfikVMogewoge9n
bUPyQ1sPNtn4vknptfh7tv18BTg1aytbK+ua31vnDHaDEIg/a5OWTMUYZOrVpJii
f4PwX0SMioCjY84oY1EB26ZKtLt9MDh2ir3rzJVSiRl776WEaa6kTtYVHI4VNWLF
cJ0HWnnz74JliQd2jFUh9IK+FqBdYPcTyREuNxBr3KKVMBeQrqW96OubL913JrU6
oQKCAQEA0yzORUouT0yleWs7RmzBlT9OLD/3cBYJMf/r1F8z8OQjB8fU1jKbO1Cs
q4l+o9FmI+eHkgc3xbEG0hahOFWm/hTTli9vzksxurgdawZELThRkK33uTU9pKla
Okqx3Ru/iMOW2+DQUx9UB+jK+hSAgq4gGqLeJVyaBerIdLQLlvqxrwSxjvvj+wJC
Y66mgRzdCi6VDF1vV0knCrQHK6tRwcPozu/k4zjJzvdbMJnKEy2S7Vh6vO8lEPJm
MQtaHPpmz+F4z14b9unNIiSbHO60Q4O+BwIBCzxApQQbFg63vBLYYwEMRd7hh92s
ZkZVSOEp+sYBf/tmptlKr49nO+dTjQ==
-----END PRIVATE KEY-----
```

## File: `packages/playwright-mcp/tests/testserver/san.cnf`
```
# openssl req -new -x509 -days 3650 -key key.pem -out cert.pem -config san.cnf -extensions v3_req

[req]
distinguished_name = req_distinguished_name
req_extensions = v3_req
prompt = no

[req_distinguished_name]
CN = playwright-test

[v3_req]
basicConstraints = CA:FALSE
keyUsage = nonRepudiation, digitalSignature, keyEncipherment
subjectAltName = @alt_names

[alt_names]
DNS.1 = localhost
IP.1 = 127.0.0.1
IP.2 = ::1
```


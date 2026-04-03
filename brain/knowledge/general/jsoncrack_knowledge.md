---
id: jsoncrack-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:56.619012
---

# KNOWLEDGE EXTRACT: jsoncrack
> **Extracted on:** 2026-03-30 17:38:13
> **Source:** jsoncrack

---

## File: `.gitignore`
```
# Agent tooling
.agents
.claude
.codex

# Package manager
node_modules/
.npm-cache/
.pnpm-store/
.pnp*
npm-debug.log*
pnpm-debug.log*
yarn-debug.log*
yarn-error.log*

# Turborepo
.turbo/

# Build outputs and caches (all workspaces)
**/.next/
**/out/
**/coverage/
**/*.tsbuildinfo

# OS
.DS_Store
```

## File: `.npmrc`
```
engine-strict=true
```

## File: `CODE_OF_CONDUCT.md`
```markdown

# Contributor Covenant Code of Conduct

## Our Pledge

We as members, contributors, and leaders pledge to make participation in our
community a harassment-free experience for everyone, regardless of age, body
size, visible or invisible disability, ethnicity, sex characteristics, gender
identity and expression, level of experience, education, socio-economic status,
nationality, personal appearance, race, caste, color, religion, or sexual
identity and orientation.

We pledge to act and interact in ways that contribute to an open, welcoming,
diverse, inclusive, and healthy community.

## Our Standards

Examples of behavior that contributes to a positive environment for our
community include:

* Demonstrating empathy and kindness toward other people
* Being respectful of differing opinions, viewpoints, and experiences
* Giving and gracefully accepting constructive feedback
* Accepting responsibility and apologizing to those affected by our mistakes,
  and learning from the experience
* Focusing on what is best not just for us as individuals, but for the overall
  community

Examples of unacceptable behavior include:

* The use of sexualized language or imagery, and sexual attention or advances of
  any kind
* Trolling, insulting or derogatory comments, and personal or political attacks
* Public or private harassment
* Publishing others' private information, such as a physical or email address,
  without their explicit permission
* Other conduct which could reasonably be considered inappropriate in a
  professional setting

## Enforcement Responsibilities

Community leaders are responsible for clarifying and enforcing our standards of
acceptable behavior and will take appropriate and fair corrective action in
response to any behavior that they deem inappropriate, threatening, offensive,
or harmful.

Community leaders have the right and responsibility to remove, edit, or reject
comments, commits, code, wiki edits, issues, and other contributions that are
not aligned to this Code of Conduct, and will communicate reasons for moderation
decisions when appropriate.

## Scope

This Code of Conduct applies within all community spaces, and also applies when
an individual is officially representing the community in public spaces.
Examples of representing our community include using an official e-mail address,
posting via an official social media account, or acting as an appointed
representative at an online or offline event.

## Enforcement

Instances of abusive, harassing, or otherwise unacceptable behavior may be
reported to the community leaders responsible for enforcement at
opensource@github.com.
All complaints will be reviewed and investigated promptly and fairly.

All community leaders are obligated to respect the privacy and security of the
reporter of any incident.

## Enforcement Guidelines

Community leaders will follow these Community Impact Guidelines in determining
the consequences for any action they deem in violation of this Code of Conduct:

### 1. Correction

**Community Impact**: Use of inappropriate language or other behavior deemed
unprofessional or unwelcome in the community.

**Consequence**: A private, written warning from community leaders, providing
clarity around the nature of the violation and an explanation of why the
behavior was inappropriate. A public apology may be requested.

### 2. Warning

**Community Impact**: A violation through a single incident or series of
actions.

**Consequence**: A warning with consequences for continued behavior. No
interaction with the people involved, including unsolicited interaction with
those enforcing the Code of Conduct, for a specified period of time. This
includes avoiding interactions in community spaces as well as external channels
like social media. Violating these terms may lead to a temporary or permanent
ban.

### 3. Temporary Ban

**Community Impact**: A serious violation of community standards, including
sustained inappropriate behavior.

**Consequence**: A temporary ban from any sort of interaction or public
communication with the community for a specified period of time. No public or
private interaction with the people involved, including unsolicited interaction
with those enforcing the Code of Conduct, is allowed during this period.
Violating these terms may lead to a permanent ban.

### 4. Permanent Ban

**Community Impact**: Demonstrating a pattern of violation of community
standards, including sustained inappropriate behavior, harassment of an
individual, or aggression toward or disparagement of classes of individuals.

**Consequence**: A permanent ban from any sort of public interaction within the
community.

## Attribution

This Code of Conduct is adapted from the [Contributor Covenant][homepage],
version 2.1, available at
[https://www.contributor-covenant.org/version/2/1/code_of_conduct.html][v2.1].

Community Impact Guidelines were inspired by
[Mozilla's code of conduct enforcement ladder][Mozilla CoC].

For answers to common questions about this code of conduct, see the FAQ at
[https://www.contributor-covenant.org/faq][FAQ]. Translations are available at
[https://www.contributor-covenant.org/translations][translations].

[homepage]: https://www.contributor-covenant.org
[v2.1]: https://www.contributor-covenant.org/version/2/1/code_of_conduct.html
[Mozilla CoC]: https://github.com/mozilla/diversity
[FAQ]: https://www.contributor-covenant.org/faq
[translations]: https://www.contributor-covenant.org/translations
```

## File: `CONTRIBUTING.md`
```markdown
# Contributing to JSON Crack

Thank you for wanting to contribute! This is a community-driven project, and we appreciate your help. Please read this guide carefully to make the review process smooth and fast.

**Read our [Code of Conduct](./CODE_OF_CONDUCT.md) first** — we want to keep this community friendly and welcoming.

---

## Before You Start: The Issue-First Workflow

**Always open or find an issue BEFORE you start coding.** This saves everyone time.

1. **Check existing issues** — Search to see if someone already reported this or is working on it
2. **Open a new issue** if one doesn't exist — Describe what you want to fix or build
3. **Wait for approval** — I'll review and give feedback (usually within a few days)
4. **Once approved**, you can start coding
5. **Link your PR to the issue** — Use `Closes #123` in your PR description

This workflow prevents duplicate work and ensures your contribution aligns with the project's direction.

---

## Quick Setup

### Prerequisites
- Node.js 18+
- pnpm (or npm/yarn)

### Tech Stack
JSON Crack uses:
- **React** — UI library
- **Reaflow** — Graph visualization
- **Mantine UI** — UI components
- **Zustand** — State management

### Get Started
```bash
# Clone the repo
git clone https://github.com/AykutSarac/jsoncrack.com.git
cd jsoncrack.com

# Install dependencies
pnpm install

# Run the dev server
pnpm dev
```

The app will be available at `http://localhost:3000`

---

## How to Submit a Pull Request

### Requirements
Before submitting, make sure your PR includes:

1. **Issue ID** — Reference the issue: `Closes #123`
2. **Clear description** — What does this change do? Why?
3. **Evidence of working changes** — One or both:
   - **Screenshot** — Show the UI before/after
   - **Video** — Screen recording of the feature in action
4. **Test it locally** — Run `pnpm dev` and verify it works
5. **Follow code style** — Use [Google TypeScript Style Guide](https://google.github.io/styleguide/tsguide.html)

### Creating Your Branch
```bash
git checkout -b fix/issue-123-description
# or
git checkout -b feature/issue-123-description
```

Use clear branch names that reference the issue.

---

## Guidelines

### Performance First
- Avoid unnecessary re-renders
- Use React DevTools Profiler to check performance
- Test with large JSON files to ensure no slowdowns

### Code Quality
- Follow the [Google TypeScript Style Guide](https://google.github.io/styleguide/tsguide.html)
- Write descriptive commit messages
- Keep changes focused — one feature/fix per PR

### Testing
- Manually test your changes thoroughly
- Describe exactly how you tested it in the PR
- Make sure existing features still work

---

## Example PR

Here's what a good PR looks like:

**Title:** Add JSON validation tooltip on parse error

**Description:**
```
Closes #234

## What Changed
Added a helpful tooltip that shows validation errors when JSON fails to parse, making it easier for users to fix their JSON.

## How to Test
1. Paste invalid JSON: `{invalid`
2. Look for the red error indicator
3. Hover over it to see the detailed error message

## Evidence
- [Screenshot of tooltip](link-to-image)

## Performance Notes
No performance impact. Tooltip renders conditionally only on errors.
```

---

## Questions?

- Found a bug? Open an issue
- Have an idea? Open an issue
- Confused about something? Comment on the issue

Thank you for contributing to JSON Crack! 🎉
```

## File: `LICENSE.md`
```markdown
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

   Copyright 2025 Aykut Saraç

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
  "name": "jsoncrack-monorepo",
  "private": true,
  "license": "Apache-2.0",
  "homepage": "https://jsoncrack.com",
  "author": {
    "name": "Aykut Saraç",
    "email": "aykutsarac0@gmail.com"
  },
  "bugs": {
    "url": "https://github.com/AykutSarac/jsoncrack.com/issues"
  },
  "scripts": {
    "dev": "turbo run dev",
    "dev:www": "turbo run dev --filter=www",
    "dev:vscode": "turbo run watch-build --filter=vscode",
    "build": "turbo run build",
    "build:www": "turbo run build --filter=www",
    "build:vscode": "turbo run build --filter=vscode",
    "start": "turbo run start",
    "lint": "turbo run lint",
    "lint:vscode": "turbo run lint --filter=vscode",
    "lint:fix": "turbo run lint:fix",
    "lint:fix:vscode": "turbo run lint:fix --filter=vscode",
    "analyze": "turbo run analyze",
    "clean": "turbo run clean"
  },
  "devDependencies": {
    "turbo": "^2.8.8"
  },
  "engines": {
    "node": ">=24",
    "pnpm": ">=10"
  },
  "packageManager": "pnpm@10.20.0",
  "pnpm": {
    "onlyBuiltDependencies": [
      "esbuild",
      "sharp",
      "unrs-resolver"
    ],
    "overrides": {
      "react": "19.2.4",
      "react-dom": "19.2.4",
      "@types/react": "19.2.11",
      "@types/react-dom": "19.2.3",
      "html-to-image": "1.11.11",
      "jq-web": "0.5.1"
    }
  }
}
```

## File: `pnpm-workspace.yaml`
```yaml
packages:
  - apps/*
  - packages/*
```

## File: `README.md`
```markdown
<!-- PROJECT LOGO -->
<p align="center">
  <a href="https://github.com/AykutSarac/jsoncrack.com">
   <img src="./apps/www/public/assets/192.png" height="50" alt="Logo">
  </a>

  <h1 align="center">JSON Crack</h1>

  <p align="center">
    The open-source JSON Editor.
    <br />
    <a href="https://jsoncrack.com"><strong>Learn more »</strong></a>
    <br />
    <br />
    <a href="https://todiagram.com">ToDiagram</a>
    ·
    <a href="https://discord.gg/yVyTtCRueq">Discord</a>
    ·
    <a href="https://jsoncrack.com">Website</a>
    ·
    <a href="https://github.com/AykutSarac/jsoncrack.com/issues">Issues</a>
    ·
    <a href="https://marketplace.visualstudio.com/items?itemName=AykutSarac.jsoncrack-vscode">VS Code</a>
  </p>
</p>

<!-- ABOUT THE PROJECT -->

## About the Project

<img width="100%" alt="booking-screen" src="./apps/www/public/assets/editor.webp">

## Visualize JSON into interactive graphs

JSON Crack is a tool for visualizing JSON data in a structured, interactive graphs, making it easier to explore, format, and validate JSON. It offers features like converting JSON to other formats (CSV, YAML), generating JSON Schema, executing queries, and exporting visualizations as images. Designed for both readability and usability.

* **Visualizer**: Instantly convert JSON, YAML, CSV, and XML into interactive graphs or trees in dark or light mode.
* **Convert**: Seamlessly transform data formats, like JSON to CSV or XML to JSON, for easy sharing.
* **Format & Validate**: Beautify and validate JSON, YAML, and CSV for clear and accurate data.
* **Code Generation**: Generate TypeScript interfaces, Golang structs, and JSON Schema.
* **JSON Schema**: Create JSON Schema, mock data, and validate various data formats.
* **Advanced Tools**: Decode JWT, randomize data, and run jq or JSON path queries.
* **Export Image**: Download your visualization as PNG, JPEG, or SVG.
* **Privacy**: All data processing is local; nothing is stored on our servers.

## Recognition

<a href="https://news.ycombinator.com/item?id=32626873">
  <img
    style="width: 250px; height: 54px;" width="250" height="54"
    alt="Featured on Hacker News"
    src="https://hackernews-badge.vercel.app/api?id=32626873"
  />
</a>

<a href="https://producthunt.com/posts/JSON-Crack?utm_source=badge-featured&utm_medium=badge&utm_souce=badge-jsoncrack" target="_blank"><img src="https://api.producthunt.com/widgets/embed-image/v1/featured.svg?post_id=332281&theme=light" alt="JSON Crack | Product Hunt" style="width: 250px; height: 54px;" width="250" height="54" /></a>

## Integrations

- [VS Code Extension](https://marketplace.visualstudio.com/items?itemName=AykutSarac.jsoncrack-vscode)
- [npm Package (`jsoncrack-react`)](https://www.npmjs.com/package/jsoncrack-react)

## Contributing

- Found a bug or missing feature? Open an issue on [GitHub Issues](https://github.com/AykutSarac/jsoncrack.com/issues).
- Want to contribute code or docs? Start with our [contribution guide](./CONTRIBUTING.md).

## Sponsors & Support

If you find JSON Crack useful, you can support the project by using [ToDiagram](https://todiagram.com).

## Stay Up-to-Date

JSON Crack officially launched as v1.0 on the 17th of February 2022 and we've come a long way so far. Watch **releases** of this repository to be notified of future updates:

<a href="https://github.com/AykutSarac/jsoncrack.com"><img src="https://img.shields.io/github/stars/AykutSarac/jsoncrack.com" alt="Star at GitHub" /></a>

<!-- GETTING STARTED -->

## Getting Started

To get a local copy up and running, please follow these simple steps.

### Prerequisites

Here is what you need to be able to run JSON Crack.

- Node.js (Version: >=24.x)
- pnpm (Version: >=10)


## Development

### Setup

1. Clone the repo into a public GitHub repository (or fork https://github.com/AykutSarac/jsoncrack.com/fork). If you plan to distribute the code, read the [`LICENSE`](LICENSE.md) for additional details.

   ```sh
   git clone https://github.com/AykutSarac/jsoncrack.com.git
   ```

2. Go to the project folder

   ```sh
   cd jsoncrack.com
   ```

3. Install packages

   ```sh
   pnpm install
   ```

4. Run the web app

   ```sh
   pnpm dev:www

   # Running on http://localhost:3000/
   ```

### Useful Commands

From repository root:

```sh
# Web app
pnpm dev:www
pnpm build:www

# VS Code extension
pnpm dev:vscode
pnpm build:vscode
pnpm lint:vscode
pnpm lint:fix:vscode

# All workspaces
pnpm dev
pnpm build
pnpm lint
```

`pnpm build:www` is the production build command used in GitHub Actions deployment.

### Debug VS Code Extension

1. Open repository root in VS Code.
2. Press `F5`.
3. Select `Run VSCode Extension (apps/vscode)` when prompted.
4. In the Extension Development Host window, open a `.json` file and run:
   `JSON Crack: Enable JSON Crack visualization`.

### Docker

🐳 Docker assets are in `apps/www`.
If you want to run JSON Crack locally:

```console
cd apps/www

# Build a Docker image with:
docker compose build

# Run locally with `docker-compose`
docker compose up

# Go to http://localhost:8888
```

## Configuration

The supported node limit can be changed by editing `NEXT_PUBLIC_NODE_LIMIT` in `apps/www/.env`.

<!-- LICENSE -->

## License

See [`LICENSE`](LICENSE.md) for more information.
```

## File: `turbo.json`
```json
{
  "$schema": "https://turborepo.com/schema.json",
  "tasks": {
    "build": {
      "dependsOn": ["^build"],
      "outputs": [".next/**", "!.next/cache/**", "dist/**", "out/**", "build/**"]
    },
    "dev": {
      "dependsOn": ["^build"],
      "cache": false,
      "persistent": true
    },
    "start": {
      "cache": false,
      "persistent": true
    },
    "lint": {
      "dependsOn": ["^build"],
      "outputs": []
    },
    "lint:fix": {
      "cache": false
    },
    "analyze": {
      "dependsOn": ["^build"],
      "outputs": [".next/**", "!.next/cache/**", "out/**", "build/**"]
    },
    "clean": {
      "cache": false
    },
    "watch-build": {
      "cache": false,
      "persistent": true
    }
  }
}
```

## File: `apps/vscode/.env`
```
PUBLIC_URL=./
```

## File: `apps/vscode/.eslintrc.json`
```json
{
  "root": true,
  "parser": "@typescript-eslint/parser",
  "parserOptions": {
    "ecmaVersion": 6,
    "sourceType": "module"
  },
  "plugins": ["@typescript-eslint",
  "unused-imports",
  "prettier"
],
  "extends": [
    "eslint:recommended",
    "prettier",
    "plugin:@typescript-eslint/recommended"
  ],
  
  "rules": {
    "@typescript-eslint/consistent-type-imports": "error",
    "unused-imports/no-unused-imports": "error",
    "@typescript-eslint/no-explicit-any": "off",
    "prettier/prettier": "error",
    "space-in-parens": "error",
    "no-empty": "error",
    "no-multiple-empty-lines": "error",
    "no-irregular-whitespace": "error",
    "strict": ["error", "never"],
    "linebreak-style": ["error", "unix"],
    "quotes": ["error", "double", { "avoidEscape": true }],
    "semi": ["error", "always"],
    "prefer-const": "error",
    "space-before-function-paren": [
      "error",
      {
        "anonymous": "always",
        "named": "never",
        "asyncArrow": "always"
      }
    ]
  },
  "ignorePatterns": ["build", "public", "scripts", "node_modules", "webpack.config.js"]
}
```

## File: `apps/vscode/.gitignore`
```
node_modules/
build/
*.vsix
```

## File: `apps/vscode/.prettierignore`
```
.github
.next
node_modules/
out
public
*-lock.json
tsconfig.json
build
jsoncrack
```

## File: `apps/vscode/.prettierrc`
```
{
  "trailingComma": "es5",
  "singleQuote": false,
  "semi": true,
  "printWidth": 100,
  "arrowParens": "avoid",
  "importOrder": [
    "^(react/(.*)$)|^(react$)",
    "^(next/(.*)$)|^(next$)",
    "^@mantine/core",
    "^@mantine",
    "styled",
    "<THIRD_PARTY_MODULES>",
    "^src/(.*)$",
    "^[./]"
  ],
  "importOrderParserPlugins": ["typescript", "jsx", "decorators-legacy"],
  "plugins": ["@trivago/prettier-plugin-sort-imports"]
}
```

## File: `apps/vscode/.vscodeignore`
```
.vscode/**
.vscode-test/**
.github/**
.turbo/**
node_modules/**
scripts/**
src/**
.gitignore
.env
.prettierignore
.prettierrc
.pnpm-lock.yaml
webpack.config.js
tsconfig.extension.json
vsc-extension-quickstart.md
yarn.lock
**/tsconfig.json
**/.eslintrc.json
**/*.map
**/*.ts
```

## File: `apps/vscode/LICENSE.md`
```markdown
MIT License

Copyright (c) 2025 Aykut Saraç

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```

## File: `apps/vscode/package.json`
```json
{
  "name": "vscode",
  "version": "3.0.0",
  "displayName": "JSON Crack",
  "description": "Seamlessly visualize your JSON data instantly into graphs.",
  "publisher": "AykutSarac",
  "license": "MIT",
  "author": {
    "email": "aykutsarac0@gmail.com",
    "name": "Aykut Saraç"
  },
  "homepage": "https://jsoncrack.com",
  "icon": "assets/jsoncrack.png",
  "galleryBanner": {
    "color": "#202225",
    "theme": "dark"
  },
  "categories": [
    "Visualization"
  ],
  "keywords": [
    "json",
    "visualizer",
    "jsoncrack",
    "data",
    "yaml",
    "livepreview"
  ],
  "activationEvents": [
    "workspaceContains:**/*.{json}"
  ],
  "main": "./build/ext-src/extension.js",
  "contributes": {
    "commands": [
      {
        "command": "jsoncrack-vscode.start",
        "title": "Enable JSON Crack visualization",
        "category": "menubar",
        "icon": {
          "light": "./assets/icon-light.svg",
          "dark": "./assets/icon-dark.svg"
        }
      },
      {
        "command": "jsoncrack-vscode.start.specific",
        "title": "Enable JSON Crack visualization for specific file",
        "category": "menubar"
      },
      {
        "command": "jsoncrack-vscode.start.selected",
        "title": "Open with JSON Crack",
        "category": "Navigation"
      }
    ],
    "menus": {
      "editor/context": [
        {
          "command": "jsoncrack-vscode.start.selected",
          "when": "editorHasSelection",
          "group": "navigation"
        }
      ],
      "commandPalette": [
        {
          "command": "jsoncrack-vscode.start",
          "when": "never"
        }
      ],
      "editor/title": [
        {
          "command": "jsoncrack-vscode.start",
          "when": "resourceExtname == .json || editorLangId == json",
          "group": "navigation"
        }
      ]
    }
  },
  "scripts": {
    "vscode:prepublish": "pnpm run build",
    "dev": "react-scripts start",
    "start": "react-scripts start",
    "compile": "webpack --mode development",
    "watch": "webpack --mode development --watch",
    "package": "webpack --mode production --devtool hidden-source-map",
    "analyze": "ANALYZE=true pnpm run build",
    "lint": "eslint src ext-src && prettier --check src ext-src",
    "lint:fix": "eslint --fix src ext-src && prettier --write src ext-src",
    "build": "node ./scripts/build-non-split.js && tsc -p tsconfig.extension.json",
    "clean": "rm -rf build",
    "watch-build": "nodemon --watch src --watch ext-src --watch scripts --ext js,tsx,ts --exec \"pnpm run build\"",
    "eject": "react-scripts eject"
  },
  "devDependencies": {
    "@babel/plugin-proposal-private-property-in-object": "^7.21.11",
    "@mantine/code-highlight": "^7.16.2",
    "@mantine/core": "^7.16.2",
    "@mantine/hooks": "^7.16.2",
    "@trivago/prettier-plugin-sort-imports": "^4.3.0",
    "@types/node": "16.x",
    "@types/react": "^19.0.0",
    "@types/react-dom": "^19.0.0",
    "@types/vscode": "^1.86.0",
    "@types/webpack-env": "^1.18.5",
    "@typescript-eslint/eslint-plugin": "^5.31.0",
    "@typescript-eslint/parser": "^5.31.0",
    "eslint": "^8.20.0",
    "eslint-config-prettier": "^9.1.0",
    "eslint-plugin-prettier": "^5.2.1",
    "eslint-plugin-unused-imports": "^4.1.4",
    "nodemon": "^2.0.20",
    "prettier": "^3.3.3",
    "react-scripts": "^5.0.1",
    "rewire": "^7.0.0",
    "ts-loader": "^9.5.1",
    "typescript": "^5.6.3",
    "vsce": "^2.15.0",
    "webpack": "^5.95.0",
    "webpack-cli": "^5.1.4"
  },
  "dependencies": {
    "jsoncrack-react": "workspace:*",
    "react": "19.2.4",
    "react-dom": "19.2.4"
  },
  "browserslist": {
    "production": [
      ">0.2%",
      "not dead",
      "not op_mini all"
    ],
    "development": [
      "last 1 chrome version",
      "last 1 firefox version",
      "last 1 safari version"
    ]
  },
  "repository": {
    "type": "git",
    "url": "https://github.com/AykutSarac/jsoncrack.com"
  },
  "bugs": {
    "url": "https://github.com/AykutSarac/jsoncrack.com/issues"
  },
  "engines": {
    "vscode": "^1.86.0"
  },
  "packageManager": "pnpm@10.20.0"
}
```

## File: `apps/vscode/README.md`
```markdown
  <img src="https://github.com/AykutSarac/jsoncrack-vscode/assets/47941171/23b26537-7c4a-4029-af78-456dea0d0b04" width="300" alt="JSON Crack" />

<hr />

[JSON Crack](https://jsoncrack.com?utm_source=jsoncrack-vscode&utm_medium=readme)'s Official Visual Studio Code Extension that visualizes JSON data as an interactive diagram. The extension parses the open JSON file and displays its structure as a connected graph where nodes represent objects, arrays, and values.

## How to use?

1. Install the JSON Crack extension from the [VS Code marketplace](https://marketplace.visualstudio.com/items?itemName=AykutSarac.jsoncrack-vscode).
2. Open a JSON file.
3. Click on the JSON Crack icon in the menubar at top right.

<img width="600" alt="image" src="https://github.com/AykutSarac/jsoncrack-vscode/assets/47941171/06715ac1-2403-402f-b3fa-3d91e1c9196a">

## Privacy

The extension works **fully offline**. No data is sent to any server. All JSON parsing and visualization happens locally in your editor.

## Debugging

This extension lives in `apps/vscode` inside the [jsoncrack.com](https://github.com/AykutSarac/jsoncrack.com) monorepo.

**Prerequisites:** Node.js `>=24`, pnpm `>=10`

```sh
# Install dependencies from repo root
pnpm install

# Watch mode — rebuilds on every change
pnpm dev:vscode
```

Then press **F5** in VS Code to launch the Extension Development Host. Keep the watch process running for live iteration.
```

## File: `apps/vscode/tsconfig.extension.json`
```json
{
  "compilerOptions": {
    "module": "commonjs",
    "target": "es6",
    "outDir": "build",
    "lib": ["es6", "dom"],
    "sourceMap": true,
    "rootDir": ".",
    "strict": true
  },
  "include": ["ext-src"],
  "exclude": ["node_modules", ".vscode-test"]
}
```

## File: `apps/vscode/tsconfig.json`
```json
{
  "compilerOptions": {
    "baseUrl": ".",
    "target": "ES6",
    "lib": ["dom", "dom.iterable", "esnext"],
    "allowJs": true,
    "skipLibCheck": true,
    "strict": true,
    "forceConsistentCasingInFileNames": true,
    "noEmit": false,
    "esModuleInterop": true,
    "module": "esnext",
    "moduleResolution": "node",
    "resolveJsonModule": true,
    "isolatedModules": true,
    "jsx": "preserve",
    "incremental": true,
    "noImplicitAny": false
  },
  "include": ["src"],
  "exclude": ["node_modules"]
}
```

## File: `apps/vscode/webpack.config.js`
```javascript
/** @typedef {import('webpack').Configuration} WebpackConfig **/

const webpack = require("webpack");
const path = require("path");

/** @type WebpackConfig */
const extensionConfig = {
  target: "node",
  mode: "none",
  entry: "./ext-src/extension.ts",
  output: {
    path: path.resolve(__dirname, "build"),
    filename: "extension.js",
    libraryTarget: "commonjs2",
	},
  externals: {
    vscode: "commonjs vscode",
  },
  module: {
		rules: [{
			test: /\.ts$/,
			exclude: [/node_modules/],
			use: [{
				loader: 'ts-loader'
			}]
		}]
	},
  resolve: {
    extensions: [".ts", ".js"],
  },
  plugins: [
    new webpack.optimize.LimitChunkCountPlugin({
      maxChunks: 1, // disable chunks by default since web extensions must be a single bundle
    }),
    new webpack.ProvidePlugin({
      process: "process/browser", // provide a shim for the global `process` variable
    }),
  ],
  devtool: "nosources-source-map",
  performance: {
		hints: false
	},
  infrastructureLogging: {
    level: "log",
  },
};

module.exports = extensionConfig;
```

## File: `apps/vscode/ext-src/extension.ts`
```typescript
import * as path from "path";
import * as vscode from "vscode";
import { createWebviewPanel } from "./webview";

function getPanelTitle(document?: vscode.TextDocument) {
  if (!document) return "JSON Crack";

  const fileName = path.basename(document.fileName);
  return fileName || "JSON Crack";
}

export function activate(context: vscode.ExtensionContext) {
  context.subscriptions.push(
    vscode.commands.registerCommand("jsoncrack-vscode.start", () =>
      createWebviewForActiveEditor(context)
    ),
    vscode.commands.registerCommand("jsoncrack-vscode.start.specific", (content?: string) =>
      createWebviewForContent(context, content)
    ),
    vscode.commands.registerCommand("jsoncrack-vscode.start.selected", () =>
      createWebviewForSelectedText(context)
    )
  );
}

// create webview for selected text
async function createWebviewForSelectedText(context: vscode.ExtensionContext) {
  const editor = vscode.window.activeTextEditor;

  if (editor && editor.selection.isEmpty) {
    vscode.window.showInformationMessage("Please select some text first!");
    return;
  }

  const selectedText = editor?.document.getText(editor.selection);

  // Create the webview panel and send the selected JSON content
  const panel = createWebviewPanel(context, getPanelTitle(editor?.document));
  panel.webview.postMessage({
    json: selectedText,
  });

  const onReceiveMessage = panel.webview.onDidReceiveMessage(e => {
    if (e === "ready") {
      panel.webview.postMessage({
        json: selectedText,
      });
    }
  });

  const onTextChange = vscode.workspace.onDidChangeTextDocument(changeEvent => {
    if (changeEvent.document === editor?.document) {
      panel.webview.postMessage({
        json: changeEvent.document.getText(editor?.selection),
      });
    }
  });

  const disposer = () => {
    onTextChange.dispose();
    onReceiveMessage.dispose();
  };

  panel.onDidDispose(disposer, null, context.subscriptions);
}

async function createWebviewForActiveEditor(context: vscode.ExtensionContext) {
  const editor = vscode.window.activeTextEditor;
  const panel = createWebviewPanel(context, getPanelTitle(editor?.document));

  const onReceiveMessage = panel.webview.onDidReceiveMessage(e => {
    if (e === "ready") {
      panel.webview.postMessage({
        json: editor?.document.getText(),
      });
    }
  });

  const onTextChange = vscode.workspace.onDidChangeTextDocument(changeEvent => {
    if (changeEvent.document === editor?.document) {
      panel.webview.postMessage({
        json: changeEvent.document.getText(),
      });
    }
  });

  const disposer = () => {
    onTextChange.dispose();
    onReceiveMessage.dispose();
  };

  panel.onDidDispose(disposer, null, context.subscriptions);
}

/**
 * Renders a readonly diagram from a string
 * @param context ExtensionContext
 * @param content JSON content as a string
 */
function createWebviewForContent(context?: vscode.ExtensionContext, content?: string): any {
  if (context && content) {
    const panel = createWebviewPanel(
      context,
      getPanelTitle(vscode.window.activeTextEditor?.document)
    );
    panel.webview.postMessage({
      json: content,
    });
  }
}

// This method is called when your extension is deactivated
// eslint-disable-next-line @typescript-eslint/no-empty-function
export function deactivate() {}
```

## File: `apps/vscode/ext-src/webview.ts`
```typescript
import * as fs from "fs";
import * as path from "path";
import * as vscode from "vscode";

export function createWebviewPanel(context: vscode.ExtensionContext, title = "JSON Crack") {
  const extPath = context.extensionPath;

  const panel = vscode.window.createWebviewPanel(
    "liveHTMLPreviewer",
    title,
    vscode.ViewColumn.Beside,
    {
      enableScripts: true,
      retainContextWhenHidden: true,
      localResourceRoots: [
        vscode.Uri.file(path.join(extPath, "build")),
        vscode.Uri.file(path.join(extPath, "build", "static")),
        vscode.Uri.file(path.join(extPath, "build", "static", "js")),
        vscode.Uri.file(path.join(extPath, "build", "static", "css")),
        vscode.Uri.file(path.join(extPath, "assets")),
      ],
    }
  );
  panel.iconPath = vscode.Uri.file(path.join(extPath, "build", "assets", "favicon.ico"));

  const manifest = JSON.parse(
    fs.readFileSync(path.join(extPath, "build", "asset-manifest.json"), "utf-8")
  );

  const mainScript = manifest.files["main.js"];
  const mainStyle = manifest.files["main.css"];

  const scriptPathOnDisk = vscode.Uri.file(path.join(extPath, "build", mainScript));
  const stylePathOnDisk = vscode.Uri.file(path.join(extPath, "build", mainStyle));

  const stylesMainUri = panel.webview.asWebviewUri(stylePathOnDisk);
  const scriptUri = panel.webview.asWebviewUri(scriptPathOnDisk);

  const nonce = getNonce();
  const csp = [
    `default-src 'self' ${panel.webview.cspSource} blob:`,
    `connect-src ${panel.webview.cspSource} blob:`,
    `script-src 'unsafe-eval' 'unsafe-inline' ${panel.webview.cspSource}`,
    `style-src ${panel.webview.cspSource} 'unsafe-inline'`,
    `worker-src ${panel.webview.cspSource} blob: data:`,
  ].join("; ");

  panel.webview.html = `<!DOCTYPE html>
      <html lang="en">
      <head>
        <meta charset="utf-8">
        <base href="${panel.webview.asWebviewUri(vscode.Uri.file(path.join(extPath, "build")))}/">
        <meta http-equiv="Content-Security-Policy" content="${csp}">
        <link href="${stylesMainUri}" rel="stylesheet">
      </head>
      <body>
        <noscript>You need to enable JavaScript to run this app.</noscript>
        <div id="root"></div>
        <script nonce="${nonce}" src="${scriptUri}"></script>
      </body>
      </html>`;

  return panel;
}

function getNonce() {
  let text = "";
  const possible = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
  for (let i = 0; i < 32; i++) {
    text += possible.charAt(Math.floor(Math.random() * possible.length));
  }
  return text;
}
```

## File: `apps/vscode/public/index.html`
```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="theme-color" content="#000000">
  </head>
  <body>
    <noscript>
      You need to enable JavaScript to run this app.
    </noscript>
    <div id="root"></div>
  </body>
</html>
```

## File: `apps/vscode/scripts/build-non-split.js`
```javascript
#!/usr/bin/env node

const path = require("path");
const rewire = require("rewire");
const defaults = rewire("react-scripts/scripts/build.js");
let config = defaults.__get__("config");

// Disable source maps
config.devtool = false;

// Disable code splitting
config.optimization.splitChunks = {
  cacheGroups: {
    default: false
  }
};

config.optimization.runtimeChunk = false;

// Enable tree shaking
config.optimization.usedExports = true;

// Force a single React instance in the bundle. Without this, workspace-linked
// packages can resolve a different React version and break hooks at runtime.
config.resolve.alias = {
  ...(config.resolve.alias || {}),
  react: path.resolve(__dirname, "../node_modules/react"),
  "react-dom": path.resolve(__dirname, "../node_modules/react-dom")
};

config.resolve.plugins = (config.resolve.plugins || []).filter(
  (plugin) => plugin.constructor.name !== "ModuleScopePlugin"
);

// Ensure production optimizations are enabled
config.mode = 'production';
config.optimization.minimize = true;

// Allow extensionless imports from ESM dependencies.
config.module.rules.push({
  test: /\.m?js$/,
  resolve: {
    fullySpecified: false
  }
});
```

## File: `apps/vscode/src/App.tsx`
```tsx
import { useCallback, useEffect, useState } from "react";
import { Anchor, Box, MantineProvider, Text } from "@mantine/core";
import type { NodeData } from "jsoncrack-react";
import { JSONCrack } from "jsoncrack-react";
import { NodeModal } from "./components/NodeModal";

function getTheme() {
  const theme = document.body.getAttribute("data-vscode-theme-kind");
  if (theme?.includes("light")) return "light" as const;
  return "dark";
}

const App: React.FC = () => {
  const [json, setJson] = useState("{}");
  const [selectedNode, setSelectedNode] = useState<NodeData | null>(null);
  const theme = getTheme();

  useEffect(() => {
    const vscode = window?.acquireVsCodeApi?.();
    vscode?.postMessage("ready");

    const onMessage = (event: MessageEvent<{ json?: string }>) => {
      const jsonData = event.data?.json;
      if (typeof jsonData === "string") {
        setJson(jsonData);
      }
    };

    window.addEventListener("message", onMessage);

    return () => {
      window.removeEventListener("message", onMessage);
    };
  }, []);

  const handleNodeClick = useCallback((node: NodeData) => {
    setSelectedNode(node);
  }, []);

  const closeNodeModal = useCallback(() => {
    setSelectedNode(null);
  }, []);

  return (
    <MantineProvider forceColorScheme={theme}>
      <Box h="100vh" w="100vw">
        <JSONCrack json={json} theme={theme} showControls={false} onNodeClick={handleNodeClick} />
        {selectedNode && (
          <NodeModal opened={!!selectedNode} onClose={closeNodeModal} nodeData={selectedNode} />
        )}
        <Anchor
          pos="fixed"
          bottom={0}
          left={0}
          href="https://jsoncrack.com/editor?utm_source=vscode&utm_campaign=attribute"
          target="_blank"
        >
          <Box px="12" py="4" bg="dark">
            <Text fz="sm" c="white">
              Powered by JSON Crack
            </Text>
          </Box>
        </Anchor>
      </Box>
    </MantineProvider>
  );
};

export default App;

declare global {
  interface Window {
    acquireVsCodeApi?: () => any;
  }
}
```

## File: `apps/vscode/src/global.css`
```css
html,
body,
#root {
  margin: 0;
  padding: 0;
  width: 100%;
  height: 100%;
  overflow: hidden;
}

*,
*::before,
*::after {
  box-sizing: border-box;
}

a {
  color: inherit;
  text-decoration: none;
}
```

## File: `apps/vscode/src/index.tsx`
```tsx
import "@mantine/core/styles.css";
import "@mantine/code-highlight/styles.css";
import "jsoncrack-react/style.css";
import { createRoot } from "react-dom/client";
import App from "./App";
import "./global.css";

const container = document.getElementById("root") as HTMLElement;
const root = createRoot(container);
root.render(<App />);
```

## File: `apps/vscode/src/react-app-env.d.ts`
```typescript
/// <reference types="react-scripts" />

declare global {
  interface Window {
    acquireVsCodeApi?: () => any;
  }
}
```

## File: `apps/vscode/src/components/NodeModal.tsx`
```tsx
import React from "react";
import type { ModalProps } from "@mantine/core";
import { Modal, Stack, Text, ScrollArea } from "@mantine/core";
import { CodeHighlight } from "@mantine/code-highlight";
import type { NodeData } from "jsoncrack-react";

interface NodeModalProps extends ModalProps {
  nodeData: NodeData | null;
}

const normalizeNodeData = (nodeRows: NodeData["text"]) => {
  if (!nodeRows || nodeRows.length === 0) return "{}";
  if (nodeRows.length === 1 && !nodeRows[0].key) return `${nodeRows[0].value}`;

  const obj: Record<string, unknown> = {};
  nodeRows.forEach(row => {
    if (row.type !== "array" && row.type !== "object" && row.key) {
      obj[row.key] = row.value;
    }
  });

  return JSON.stringify(obj, null, 2);
};

const jsonPathToString = (path?: NodeData["path"]) => {
  if (!path || path.length === 0) return "$";
  const segments = path.map(seg => (typeof seg === "number" ? seg : `"${seg}"`));
  return `$[${segments.join("][")}]`;
};

export const NodeModal = ({ opened, onClose, nodeData }: NodeModalProps) => {
  const nodeContent = normalizeNodeData(nodeData?.text ?? []);
  const jsonPath = jsonPathToString(nodeData?.path);

  return (
    <Modal title="Node Content" size="auto" opened={opened} onClose={onClose} centered>
      <Stack py="sm" gap="sm">
        <Stack gap="xs">
          <Text fz="xs" fw={500}>
            Content
          </Text>
          <ScrollArea.Autosize mah={250} maw={600}>
            <CodeHighlight code={nodeContent} miw={350} maw={600} language="json" withCopyButton />
          </ScrollArea.Autosize>
        </Stack>
        <Text fz="xs" fw={500}>
          JSON Path
        </Text>
        <ScrollArea.Autosize maw={600}>
          <CodeHighlight
            code={jsonPath}
            miw={350}
            mah={250}
            language="json"
            copyLabel="Copy to clipboard"
            copiedLabel="Copied to clipboard"
            withCopyButton
          />
        </ScrollArea.Autosize>
      </Stack>
    </Modal>
  );
};
```

## File: `apps/www/.dockerignore`
```
Dockerfile
.dockerignore
node_modules
npm-debug.log
README.md
.next
.git
```

## File: `apps/www/.env`
```
NEXT_PUBLIC_NODE_LIMIT=800
NEXT_TELEMETRY_DISABLED=1
```

## File: `apps/www/.env.development`
```
NEXT_PUBLIC_NODE_LIMIT=2000
NEXT_PUBLIC_DISABLE_EXTERNAL_MODE=false
```

## File: `apps/www/.eslintrc.json`
```json
{
  "rules": {
    "@next/next/no-img-element": "off",
    "@typescript-eslint/consistent-type-imports": "error",
    "unused-imports/no-unused-imports": "error",
    "@typescript-eslint/no-explicit-any": "off",
    "prettier/prettier": "error",
    "space-in-parens": "error",
    "no-empty": "error",
    "no-multiple-empty-lines": "error",
    "no-irregular-whitespace": "error",
    "strict": ["error", "never"],
    "linebreak-style": ["error", "unix"],
    "quotes": ["error", "double", { "avoidEscape": true }],
    "semi": ["error", "always"],
    "prefer-const": "error",
    "space-before-function-paren": [
      "error",
      {
        "anonymous": "always",
        "named": "never",
        "asyncArrow": "always"
      }
    ]
  },
  "extends": ["next/core-web-vitals", "prettier", "plugin:@typescript-eslint/recommended"],
  "plugins": ["prettier", "unused-imports"],
  "ignorePatterns": ["src/enums", "next.config.js"]
}
```

## File: `apps/www/.gitignore`
```
# App dependencies
node_modules/

# Next.js
.next/
out/

# Turborepo task cache
.turbo/

# Test/build artifacts
coverage/
build/
*.tsbuildinfo

# Local environment files
.env.local
.env.development.local
.env.test.local
.env.production.local

# Deployment
.vercel

# Workspace migration artifact (root lockfile is authoritative)
pnpm-lock.yaml

# PWA workers
public/workbox-*.js
public/sw.js
public/fallback-*.js
```

## File: `apps/www/.prettierignore`
```
.github
.next
node_modules/
out
public
*-lock.json
tsconfig.json
```

## File: `apps/www/.prettierrc`
```
{
  "trailingComma": "es5",
  "singleQuote": false,
  "semi": true,
  "printWidth": 100,
  "arrowParens": "avoid",
  "importOrder": [
    "^(react/(.*)$)|^(react$)",
    "^(next/(.*)$)|^(next$)",
    "^@mantine/core",
    "^@mantine",
    "styled",
    "<THIRD_PARTY_MODULES>",
    "^src/(.*)$",
    "^[./]"
  ],
  "importOrderParserPlugins": ["typescript", "jsx", "decorators-legacy"],
  "plugins": ["@trivago/prettier-plugin-sort-imports"]
}
```

## File: `apps/www/docker-compose.yml`
```yaml
services:
  jsoncrack:
    image: jsoncrack
    container_name: jsoncrack
    build: 
      context: .
      dockerfile: Dockerfile
    ports:
      - "8888:8080"
    environment:
      - NODE_ENV=production
```

## File: `apps/www/Dockerfile`
```
FROM node:24.10.0-alpine AS base
RUN npm install -g pnpm@10.10.0

# Stage 1: Install dependencies
FROM base AS deps
WORKDIR /app
COPY package.json pnpm-lock.yaml ./
RUN corepack enable pnpm && pnpm install --frozen-lockfile

# Stage 2: Build the application
FROM base AS builder
WORKDIR /app
COPY --from=deps /app/node_modules ./node_modules
COPY . .
RUN corepack enable pnpm && pnpm run build

# Stage 3: Production image
FROM nginxinc/nginx-unprivileged:stable AS production
WORKDIR /app
COPY --from=builder /app/out /app
COPY ./nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 8080
```

## File: `apps/www/eslint.config.mjs`
```
import { FlatCompat } from "@eslint/eslintrc";
import js from "@eslint/js";
import nextCoreWebVitals from "eslint-config-next/core-web-vitals";
import prettier from "eslint-plugin-prettier";
import unusedImports from "eslint-plugin-unused-imports";
import { defineConfig, globalIgnores } from "eslint/config";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const compat = new FlatCompat({
  baseDirectory: __dirname,
  recommendedConfig: js.configs.recommended,
  allConfig: js.configs.all,
});

export default defineConfig([
  globalIgnores(["src/enums", "**/next.config.js"]),
  {
    extends: [
      ...nextCoreWebVitals,
      ...compat.extends("prettier"),
      ...compat.extends("plugin:@typescript-eslint/recommended"),
    ],

    plugins: {
      prettier,
      "unused-imports": unusedImports,
    },

    rules: {
      "@next/next/no-img-element": "off",
      "@typescript-eslint/consistent-type-imports": "error",
      "unused-imports/no-unused-imports": "error",
      "@typescript-eslint/no-explicit-any": "off",
      "prettier/prettier": "error",
      "space-in-parens": "error",
      "no-empty": "error",
      "no-multiple-empty-lines": "error",
      "no-irregular-whitespace": "error",
      strict: ["error", "never"],
      "linebreak-style": ["error", "unix"],

      quotes: [
        "error",
        "double",
        {
          avoidEscape: true,
        },
      ],

      semi: ["error", "always"],
      "prefer-const": "error",

      "space-before-function-paren": [
        "error",
        {
          anonymous: "always",
          named: "never",
          asyncArrow: "always",
        },
      ],
    },
  },
]);
```

## File: `apps/www/LICENSE.md`
```markdown
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

   Copyright 2025 Aykut Saraç

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

## File: `apps/www/next-env.d.ts`
```typescript
/// <reference types="next" />
/// <reference types="next/image-types/global" />
import "./.next/dev/types/routes.d.ts";

// NOTE: This file should not be edited
// see https://nextjs.org/docs/pages/api-reference/config/typescript for more information.
```

## File: `apps/www/next-sitemap.config.js`
```javascript
/** @type {import('next-sitemap').IConfig} */
module.exports = {
  siteUrl: "https://jsoncrack.com",
  exclude: ["/widget"],
  autoLastmod: false,
  changefreq: "never",
};
```

## File: `apps/www/next.config.js`
```javascript
const withBundleAnalyzer = require("@next/bundle-analyzer")({
  enabled: process.env.ANALYZE === "true",
});

/**
 * @type {import('next').NextConfig}
 */
const config = {
  output: "export",
  transpilePackages: ["jsoncrack"],
  reactStrictMode: false,
  productionBrowserSourceMaps: true,
  compiler: {
    styledComponents: true,
  },
  turbopack: {
    resolveAlias: {
      fs: {
        browser: "./shims/empty.ts",
      },
    },
  },
  webpack: (config, { isServer }) => {
    config.resolve.fallback = { fs: false };
    config.output.webassemblyModuleFilename = "static/wasm/[modulehash].wasm";
    config.experiments = { asyncWebAssembly: true, layers: true };

    if (!isServer) {
      config.output.environment = { ...config.output.environment, asyncFunction: true };
    }

    return config;
  },
};

const configExport = () => {
  if (process.env.ANALYZE === "true") return withBundleAnalyzer(config);
  return config;
};

module.exports = configExport();
```

## File: `apps/www/nginx.conf`
```
server {
    listen 8080;
    root  /app;
    include /etc/nginx/mime.types;

    location /editor {
        try_files $uri /editor.html;
    }
    
    location /widget {
        try_files $uri /widget.html;
    }

    location /docs {
        try_files $uri /docs.html;
    }
}
```

## File: `apps/www/package.json`
```json
{
  "name": "www",
  "private": true,
  "version": "0.0.0",
  "license": "Apache-2.0",
  "scripts": {
    "dev": "next dev --webpack",
    "build": "next build --webpack",
    "postbuild": "next-sitemap --config next-sitemap.config.js",
    "start": "next start",
    "lint": "tsc --project tsconfig.json && eslint src && prettier --check src",
    "lint:fix": "eslint --fix src && prettier --write src",
    "analyze": "ANALYZE=true npm run build"
  },
  "dependencies": {
    "jsoncrack-react": "workspace:*",
    "@mantine/code-highlight": "^8.3.14",
    "@mantine/core": "^8.3.14",
    "@mantine/dropzone": "^8.3.14",
    "@mantine/hooks": "^8.3.14",
    "@monaco-editor/react": "^4.7.0",
    "allotment": "^1.20.5",
    "fast-xml-parser": "5.3.4",
    "gofmt.js": "0.0.2",
    "html-to-image": "1.11.11",
    "jq-web": "0.5.1",
    "js-yaml": "4.1.1",
    "json-2-csv": "5.5.10",
    "json-schema-faker": "0.5.9",
    "json_typegen_wasm": "0.7.0",
    "jsonc-parser": "3.3.1",
    "jsonpath-plus": "10.3.0",
    "lodash.debounce": "^4.0.8",
    "next": "16.1.6",
    "next-seo": "^7.1.0",
    "next-sitemap": "^4.2.3",
    "nextjs-google-analytics": "^2.3.7",
    "react": "19.2.4",
    "react-dom": "19.2.4",
    "react-hot-toast": "^2.6.0",
    "react-icons": "^5.5.0",
    "react-json-tree": "^0.20.0",
    "react-linkify-it": "^2.0.0",
    "react-zoomable-ui": "^0.11.0",
    "reaflow": "5.4.1",
    "shiki": "^3.22.0",
    "styled-components": "^6.3.8",
    "use-sync-external-store": "^1.6.0",
    "use-long-press": "^3.3.0",
    "zustand": "^5.0.11"
  },
  "devDependencies": {
    "@eslint/eslintrc": "^3.2.0",
    "@eslint/js": "^9.39.2",
    "@next/bundle-analyzer": "16.1.6",
    "@trivago/prettier-plugin-sort-imports": "^6.0.2",
    "@types/js-yaml": "^4.0.9",
    "@types/node": "^25.2.0",
    "@types/react": "19.2.11",
    "@types/react-dom": "19.2.3",
    "@typescript-eslint/eslint-plugin": "^8.54.0",
    "eslint": "^9.39.2",
    "eslint-config-next": "16.1.6",
    "eslint-config-prettier": "^10.1.8",
    "eslint-plugin-prettier": "^5.5.5",
    "eslint-plugin-unused-imports": "^4.3.0",
    "prettier": "^3.8.1",
    "ts-node": "^10.9.2",
    "typescript": "5.9.3"
  },
  "packageManager": "pnpm@10.20.0"
}
```

## File: `apps/www/tsconfig.json`
```json
{
  "compilerOptions": {
    "target": "ES6",
    "lib": [
      "dom",
      "dom.iterable",
      "esnext"
    ],
    "allowJs": true,
    "skipLibCheck": true,
    "strict": true,
    "forceConsistentCasingInFileNames": true,
    "noEmit": true,
    "esModuleInterop": true,
    "module": "esnext",
    "moduleResolution": "bundler",
    "resolveJsonModule": true,
    "isolatedModules": true,
    "jsx": "react-jsx",
    "incremental": true,
    "noImplicitAny": false,
    "typeRoots": [
      "types"
    ]
  },
  "include": [
    "src",
    "next-env.d.ts"
  ],
  "exclude": [
    "node_modules"
  ]
}
```

## File: `apps/www/public/CNAME`
```
jsoncrack.com
```

## File: `apps/www/public/manifest.json`
```json
{
  "name": "JSON Crack",
  "short_name": "JSON Crack",
  "description": "JSON Crack Editor is a tool for visualizing into graphs, analyzing, editing, formatting, querying, transforming and validating JSON, CSV, YAML, XML, and more.",
  "theme_color": "#36393e",
  "background_color": "#36393e",
  "display": "standalone",
  "orientation": "landscape",
  "scope": "/editor",
  "start_url": "/editor",
  "icons": [
    {
      "src": "assets/192.png",
      "sizes": "192x192",
      "type": "image/png"
    },

    {
      "src": "assets/512.png",
      "sizes": "512x512",
      "type": "image/png"
    }
  ]
}
```

## File: `apps/www/public/robots.txt`
```
User-agent: *

Allow: /

Sitemap: https://jsoncrack.com/sitemap.xml
```

## File: `apps/www/public/sitemap-0.xml`
```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:news="http://www.google.com/schemas/sitemap-news/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml" xmlns:mobile="http://www.google.com/schemas/sitemap-mobile/1.0" xmlns:image="http://www.google.com/schemas/sitemap-image/1.1" xmlns:video="http://www.google.com/schemas/sitemap-video/1.1">
<url><loc>https://jsoncrack.com</loc><changefreq>never</changefreq><priority>0.7</priority></url>
<url><loc>https://jsoncrack.com/converter/csv-to-json</loc><changefreq>never</changefreq><priority>0.7</priority></url>
<url><loc>https://jsoncrack.com/converter/csv-to-xml</loc><changefreq>never</changefreq><priority>0.7</priority></url>
<url><loc>https://jsoncrack.com/converter/csv-to-yaml</loc><changefreq>never</changefreq><priority>0.7</priority></url>
<url><loc>https://jsoncrack.com/converter/json-to-csv</loc><changefreq>never</changefreq><priority>0.7</priority></url>
<url><loc>https://jsoncrack.com/converter/json-to-xml</loc><changefreq>never</changefreq><priority>0.7</priority></url>
<url><loc>https://jsoncrack.com/converter/json-to-yaml</loc><changefreq>never</changefreq><priority>0.7</priority></url>
<url><loc>https://jsoncrack.com/converter/xml-to-csv</loc><changefreq>never</changefreq><priority>0.7</priority></url>
<url><loc>https://jsoncrack.com/converter/xml-to-json</loc><changefreq>never</changefreq><priority>0.7</priority></url>
<url><loc>https://jsoncrack.com/converter/xml-to-yaml</loc><changefreq>never</changefreq><priority>0.7</priority></url>
<url><loc>https://jsoncrack.com/converter/yaml-to-csv</loc><changefreq>never</changefreq><priority>0.7</priority></url>
<url><loc>https://jsoncrack.com/converter/yaml-to-json</loc><changefreq>never</changefreq><priority>0.7</priority></url>
<url><loc>https://jsoncrack.com/converter/yaml-to-xml</loc><changefreq>never</changefreq><priority>0.7</priority></url>
<url><loc>https://jsoncrack.com/docs</loc><changefreq>never</changefreq><priority>0.7</priority></url>
<url><loc>https://jsoncrack.com/editor</loc><changefreq>never</changefreq><priority>0.7</priority></url>
<url><loc>https://jsoncrack.com/legal/privacy</loc><changefreq>never</changefreq><priority>0.7</priority></url>
<url><loc>https://jsoncrack.com/legal/terms</loc><changefreq>never</changefreq><priority>0.7</priority></url>
<url><loc>https://jsoncrack.com/tools/json-schema</loc><changefreq>never</changefreq><priority>0.7</priority></url>
<url><loc>https://jsoncrack.com/type/csv-to-go</loc><changefreq>never</changefreq><priority>0.7</priority></url>
<url><loc>https://jsoncrack.com/type/csv-to-kotlin</loc><changefreq>never</changefreq><priority>0.7</priority></url>
<url><loc>https://jsoncrack.com/type/csv-to-rust</loc><changefreq>never</changefreq><priority>0.7</priority></url>
<url><loc>https://jsoncrack.com/type/csv-to-typescript</loc><changefreq>never</changefreq><priority>0.7</priority></url>
<url><loc>https://jsoncrack.com/type/json-to-go</loc><changefreq>never</changefreq><priority>0.7</priority></url>
<url><loc>https://jsoncrack.com/type/json-to-kotlin</loc><changefreq>never</changefreq><priority>0.7</priority></url>
<url><loc>https://jsoncrack.com/type/json-to-rust</loc><changefreq>never</changefreq><priority>0.7</priority></url>
<url><loc>https://jsoncrack.com/type/json-to-typescript</loc><changefreq>never</changefreq><priority>0.7</priority></url>
<url><loc>https://jsoncrack.com/type/xml-to-go</loc><changefreq>never</changefreq><priority>0.7</priority></url>
<url><loc>https://jsoncrack.com/type/xml-to-kotlin</loc><changefreq>never</changefreq><priority>0.7</priority></url>
<url><loc>https://jsoncrack.com/type/xml-to-rust</loc><changefreq>never</changefreq><priority>0.7</priority></url>
<url><loc>https://jsoncrack.com/type/xml-to-typescript</loc><changefreq>never</changefreq><priority>0.7</priority></url>
<url><loc>https://jsoncrack.com/type/yaml-to-go</loc><changefreq>never</changefreq><priority>0.7</priority></url>
<url><loc>https://jsoncrack.com/type/yaml-to-kotlin</loc><changefreq>never</changefreq><priority>0.7</priority></url>
<url><loc>https://jsoncrack.com/type/yaml-to-rust</loc><changefreq>never</changefreq><priority>0.7</priority></url>
<url><loc>https://jsoncrack.com/type/yaml-to-typescript</loc><changefreq>never</changefreq><priority>0.7</priority></url>
</urlset>
```

## File: `apps/www/public/sitemap.xml`
```xml
<?xml version="1.0" encoding="UTF-8"?>
<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
<sitemap><loc>https://jsoncrack.com/sitemap-0.xml</loc></sitemap>
</sitemapindex>
```

## File: `apps/www/shims/empty.ts`
```typescript
export {};
```

## File: `apps/www/src/constants/globalStyle.ts`
```typescript
import { createGlobalStyle } from "styled-components";

const GlobalStyle = createGlobalStyle`
  html, body {
    background: #ffffff;
    overscroll-behavior: none;
    -webkit-font-smoothing: subpixel-antialiased !important;
  }

  *,
  *::before,
  *::after {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      scroll-behavior: smooth !important;
      -webkit-tap-highlight-color: transparent;
      -webkit-font-smoothing: never;
  }

  .hide {
    display: none;
  }

  svg {
    vertical-align: text-top;
  }

  a {
    color: unset;
    text-decoration: none;
  }

  button {
    border: none;
    outline: none;
    background: transparent;
    width: fit-content;
    margin: 0;
    padding: 0;
    cursor: pointer;
  }
`;

export default GlobalStyle;
```

## File: `apps/www/src/constants/graph.ts`
```typescript
export const NODE_DIMENSIONS = {
  ROW_HEIGHT: 30, // Regular row height
  PARENT_HEIGHT: 36, // Height for parent nodes
} as const;

export const SUPPORTED_LIMIT = +(process.env.NEXT_PUBLIC_NODE_LIMIT as string);
```

## File: `apps/www/src/constants/seo.ts`
```typescript
import type { DefaultSeoProps } from "next-seo/pages";

export const SEO: DefaultSeoProps = {
  title: "JSON Crack | Online JSON Viewer - Transform your data into interactive graphs",
  description:
    "JSON Crack Editor is a tool for visualizing into graphs, analyzing, editing, formatting, querying, transforming and validating JSON, CSV, YAML, XML, and more.",
  themeColor: "#36393E",
  openGraph: {
    type: "website",
    images: [
      {
        url: "https://jsoncrack.com/assets/jsoncrack.png",
        width: 1200,
        height: 627,
      },
    ],
  },
  twitter: {
    handle: "@jsoncrack",
    cardType: "summary_large_image",
  },
  additionalLinkTags: [
    {
      rel: "manifest",
      href: "/manifest.json",
    },
    {
      rel: "icon",
      href: "/favicon.ico",
      sizes: "48x48",
    },
  ],
};
```

## File: `apps/www/src/constants/theme.ts`
```typescript
const fixedColors = {
  CRIMSON: "#DC143C",
  BLURPLE: "#5865F2",
  PURPLE: "#9036AF",
  FULL_WHITE: "#FFFFFF",
  BLACK: "#202225",
  BLACK_DARK: "#2C2F33",
  BLACK_LIGHT: "#2F3136",
  BLACK_PRIMARY: "#36393f",
  DARK_SALMON: "#E9967A",
  DANGER: "hsl(359,calc(var(--saturation-factor, 1)*66.7%),54.1%)",
  LIGHTGREEN: "#90EE90",
  SEAGREEN: "#11883B",
  ORANGE: "#FAA81A",
  SILVER: "#B9BBBE",
  PRIMARY: "#4D4D4D",
  TEXT_DANGER: "#db662e",
};

const nodeColors = {
  dark: {
    NODE_COLORS: {
      TEXT: "#DCE5E7",
      NODE_KEY: "#59b8ff",
      NODE_VALUE: "#DCE5E7",
      INTEGER: "#e8c479",
      NULL: "#939598",
      BOOL: {
        FALSE: "#F85C50",
        TRUE: "#00DC7D",
      },
      PARENT_ARR: "#FC9A40",
      PARENT_OBJ: "#59b8ff",
      CHILD_COUNT: "white",
      DIVIDER: "#383838",
    },
  },
  light: {
    NODE_COLORS: {
      TEXT: "#000",
      NODE_KEY: "#761CEA",
      NODE_VALUE: "#535353",
      INTEGER: "#FD0079",
      NULL: "#afafaf",
      BOOL: {
        FALSE: "#FF0000",
        TRUE: "#748700",
      },
      PARENT_ARR: "#FF6B00",
      PARENT_OBJ: "#761CEA",
      CHILD_COUNT: "#535353",
      DIVIDER: "#e6e6e6",
    },
  },
};

export const darkTheme = {
  ...fixedColors,
  ...nodeColors.dark,
  BLACK_SECONDARY: "#23272A",
  SILVER_DARK: "#4D4D4D",
  NODE_KEY: "#FAA81A",
  OBJECT_KEY: "#59b8ff",
  SIDEBAR_ICONS: "#8B8E90",

  INTERACTIVE_NORMAL: "#b9bbbe",
  INTERACTIVE_HOVER: "#dcddde",
  INTERACTIVE_ACTIVE: "#fff",
  BACKGROUND_NODE: "#2B2C3E",
  BACKGROUND_TERTIARY: "#202225",
  BACKGROUND_SECONDARY: "#2f3136",
  TOOLBAR_BG: "#262626",
  BACKGROUND_PRIMARY: "#36393f",
  BACKGROUND_MODIFIER_ACCENT: "rgba(79,84,92,0.48)",
  MODAL_BACKGROUND: "#36393E",
  TEXT_NORMAL: "#dcddde",
  TEXT_POSITIVE: "hsl(139,calc(var(--saturation-factor, 1)*51.6%),52.2%)",
  GRID_BG_COLOR: "#141414",
  GRID_COLOR_PRIMARY: "#1c1b1b",
  GRID_COLOR_SECONDARY: "#191919",
};

export const lightTheme = {
  ...fixedColors,
  ...nodeColors.light,
  BLACK_SECONDARY: "#F2F2F2",
  SILVER_DARK: "#CCCCCC",
  NODE_KEY: "#DC3790",
  OBJECT_KEY: "#0260E8",
  SIDEBAR_ICONS: "#6D6E70",

  INTERACTIVE_NORMAL: "#4f5660",
  INTERACTIVE_HOVER: "#2e3338",
  INTERACTIVE_ACTIVE: "#060607",
  BACKGROUND_NODE: "#F6F8FA",
  BACKGROUND_TERTIARY: "#e3e5e8",
  BACKGROUND_SECONDARY: "#f2f3f5",
  TOOLBAR_BG: "#ECECEC",
  BACKGROUND_PRIMARY: "#FFFFFF",
  BACKGROUND_MODIFIER_ACCENT: "rgba(106,116,128,0.24)",
  MODAL_BACKGROUND: "#FFFFFF",
  TEXT_NORMAL: "#2e3338",
  TEXT_POSITIVE: "#008736",
  GRID_BG_COLOR: "#f7f7f7",
  GRID_COLOR_PRIMARY: "#ebe8e8",
  GRID_COLOR_SECONDARY: "#f2eeee",
};

const themeDs = {
  ...lightTheme,
  ...darkTheme,
};

export default themeDs;
```

## File: `apps/www/src/data/example.json`
```json
{
  "fruits": [
    {
      "name": "Apple",
      "color": "#FF0000",
      "details": {
        "type": "Pome",
        "season": "Fall"
      },
      "nutrients": {
        "calories": 52,
        "fiber": "2.4g",
        "vitaminC": "4.6mg"
      }
    },
    {
      "name": "Banana",
      "color": "#FFFF00",
      "details": {
        "type": "Berry",
        "season": "Year-round"
      },
      "nutrients": {
        "calories": 89,
        "fiber": "2.6g",
        "potassium": "358mg"
      }
    },
    {
      "name": "Orange",
      "color": "#FFA500",
      "details": {
        "type": "Citrus",
        "season": "Winter"
      },
      "nutrients": {
        "calories": 47,
        "fiber": "2.4g",
        "vitaminC": "53.2mg"
      }
    }
  ]
}
```

## File: `apps/www/src/data/faq.json`
```json
[
  {
    "title": "What is JSON Crack and what does it do?",
    "content": "JSON Crack is an online JSON viewer tool designed to visualize and analyze various data formats, including JSON, YAML, CSV, XML and more. It transforms complex data into intuitive graphs and tree views, making it ideal for developers, data analysts, and anyone working with structured data."
  },
  {
    "title": "How is it different than traditional JSON viewers?",
    "content": "While traditional JSON Viewers and JSON formatters only allow you to work with raw data on text editors, JSON Crack offers a unique visual representation of your data, making it easier to understand and analyze complex data structures. It provides a tree view and graph view to help you visualize your data in different ways."
  },
  {
    "title": "Is JSON Crack free?",
    "content": "Yes, JSON Crack is a free-forever open source online tool. For advanced features you may use ToDiagram.com"
  },
  {
    "title": "Is my data secure?",
    "content": "Yes. When you paste or import your data into the editor, it's processed only on your browser to create the visualization without going into our servers."
  },
  {
    "title": "Can I convert JSON to other formats using JSON Crack?",
    "content": "Yes, JSON Crack offers robust data conversion capabilities. You can easily convert JSON to YAML, XML to JSON, CSV to JSON and other popular formats."
  },
  {
    "title": "What kind of data formats are supported?",
    "content": "A wide range of data formats are supported including JSON, YAML, XML, and CSV."
  },
  {
    "title": "What size of data can I visualize?",
    "content": "It supports approximately 300 KB. It might vary depending on the complexity of the data and your hardware."
  },
  {
    "title": "Can I export the generated graphs?",
    "content": "Yes, you can export the generated graphs as PNG, JPEG, or SVG files."
  },
  {
    "title": "How to use VS Code extension?",
    "content": "You can use the VS Code extension to visualize JSON data directly in your editor. Install the extension from the VS Code marketplace and follow the instructions at extension's page."
  },
  {
    "title": "I've previously subscribed to the premium plan, where did it go?",
    "content": "We have moved the premium features to ToDiagram.com. You can use the same credentials to access the premium features or manage your subscription."
  }
]
```

## File: `apps/www/src/data/privacy.json`
```json
{
  "Introduction": [
    "Welcome to JSON Crack.",
    "JSON Crack (“us”, “we”, or “our”) operates https://jsoncrack.com (hereinafter referred to as “Service”).",
    "Our Privacy Policy governs your visit to https://jsoncrack.com, explaining how we collect, safeguard, and disclose information resulting from your use of our Service.",
    "By using the Service, you agree to the collection and use of information in accordance with this policy. Unless otherwise defined in this Privacy Policy, the terms used have the same meanings as in our Terms and Conditions.",
    "Our Terms and Conditions (“Terms”) govern all use of our Service and together with the Privacy Policy constitute your agreement with us (“agreement”)."
  ],
  "Definitions": [
    "SERVICE means the https://jsoncrack.com website.",
    "PERSONAL DATA means data about a living individual who can be identified from those data.",
    "USAGE DATA is data collected automatically, generated by the use of Service or from Service infrastructure itself (e.g., the duration of a page visit).",
    "COOKIES are small files stored on your device (computer or mobile device)."
  ],
  "Information Collection and Use": [
    "We collect limited information for the purpose of improving our Service. We do not collect or store any Personal Data beyond what is necessary for analytics and security."
  ],
  "Data Collection": [
    "Usage Data",
    "• We may collect information that your browser sends whenever you visit our Service (“Usage Data”).",
    "• This may include your computer's IP address, browser type, browser version, pages visited, time and date of your visit, time spent on pages, and other diagnostic data.",
    "Cookies",
    "• We use cookies and similar tracking technologies to monitor activity on our Service.",
    "• Cookies are files with a small amount of data that may include an anonymous unique identifier."
  ],
  "Use of Data": [
    "JSON Crack uses collected data to:",
    "• Provide and maintain the Service;",
    "• Improve and analyze Service performance."
  ],
  "Security of Data": [
    "The data you paste into the editor for transformation into visualizations is not stored or processed on our servers, ensuring that your information remains private.",
    "Usage Data may be shared with third-party analytics services as outlined below."
  ],
  "Analytics": [
    "We may use Google Analytics to monitor Service usage.",
    "• Google Analytics collects non-personally identifying information such as browser type, referring pages, and time spent on the site.",
    "• We do not collect IP addresses through Google Analytics.",
    "• Learn more about Google's privacy practices: https://support.google.com/analytics/answer/4597324?hl=en"
  ],
  "Changes to This Privacy Policy": [
    "We may update our Privacy Policy from time to time. We will notify you of any changes by posting the new Privacy Policy on this page.",
    "You are advised to review this Privacy Policy periodically for any changes. Changes are effective when posted on this page."
  ],
  "Contact Us": [
    "If you have any questions about this Privacy Policy, please contact us at contact@todiagram.com."
  ]
}
```

## File: `apps/www/src/data/terms.json`
```json
{
  "Introduction": [
    "Subject to these Terms of Service (“Terms”, “Terms of Service”), jsoncrack.com ('JSON Crack', 'we', 'us' and/or 'our') provides access to JSON Crack's application as a service (collectively, the 'Services'). By using or accessing the Services, you acknowledge that you have read, understand, and agree to be bound by this Agreement.",
    "These Terms of Service govern your use of our web pages located at https://jsoncrack.com.",
    "Our Privacy Policy also governs your use of our Service and explains how we collect, safeguard and disclose information that results from your use of our web pages. Please read it here https://jsoncrack.com/legal/privacy.",
    "Your agreement with us includes these Terms and our Privacy Policy (“Agreements”). You acknowledge that you have read and understood Agreements, and agree to be bound of them.",
    "If you do not agree with (or cannot comply with) Agreements, then you may not use the Service, but please let us know by emailing at contact@todiagram.com so we can try to find a solution. These Terms apply to all visitors, users and others who wish to access or use Service.",
    "Thank you for being responsible."
  ],
  "Prohibited Uses": [
    "You may use Service only for lawful purposes and in accordance with Terms. You agree not to use Service:",
    "• In any way that violates any applicable national or international law or regulation.",
    "• For the purpose of exploiting, harming, or attempting to exploit or harm minors in any way by exposing them to inappropriate content or otherwise.",
    "• To transmit, or procure the sending of, any advertising or promotional material, including any “junk mail”, “chain letter,” “spam,” or any other similar solicitation.",
    "• In any way that infringes upon the rights of others, or in any way is illegal, threatening, fraudulent, or harmful, or in connection with any unlawful, illegal, fraudulent, or harmful purpose or activity.",
    "• To engage in any other conduct that restricts or inhibits anyone's use or enjoyment of Service, or which, as determined by us, may harm or offend Company or users of Service or expose them to liability.",
    "Additionally, you agree not to:",
    "• Use Service in any manner that could disable, overburden, damage, or impair Service or interfere with any other party's use of Service, including their ability to engage in real time activities through Service.",
    "• Use any robot, spider, or other automatic device, process, or means to access Service for any purpose, including monitoring or copying any of the material on Service.",
    "• Use any manual process to monitor or copy any of the material on Service or for any other unauthorized purpose without our prior written consent.",
    "• Use any device, software, or routine that interferes with the proper working of Service.",
    "• Introduce any viruses, trojan horses, worms, logic bombs, or other material which is malicious or technologically harmful.",
    "• Attempt to gain unauthorized access to, interfere with, damage, or disrupt any parts of Service, the server on which Service is stored, or any server, computer, or database connected to Service.",
    "• Attack Service via a denial-of-service attack or a distributed denial-of-service attack.",
    "• Take any action that may damage or falsify Company rating.",
    "• Otherwise attempt to interfere with the proper working of Service."
  ],
  "Analytics": [
    "We may use third-party Service Providers to monitor and analyze the use of our Service.",
    "Google Analytics is a web analytics service offered by Google that tracks and reports website traffic. Google uses the data collected to track and monitor the use of our Service. This data is shared with other Google services. Google may use the collected data to contextualise and personalise the ads of its own advertising network.",
    "For more information on the privacy practices of Google, please visit the Google Privacy Terms web page: https://policies.google.com/privacy?hl=en",
    "We also encourage you to review the Google's policy for safeguarding your data: https://support.google.com/analytics/answer/6004245"
  ],
  "Data Security": [
    "As we do not store any user data on our servers, we are not responsible for any data security risks that may occur when users store or process data locally on their devices."
  ],
  "Intellectual Property": [
    "Service and its original content (excluding Content provided by users), features and functionality are and will remain the exclusive property of JSON Crack and its licensors. Service is protected by copyright and other laws of foreign countries. Our trademarks and trade dress may not be used in connection with any product or service without the prior written consent of JSON Crack."
  ],
  "Disclaimer of Warranty": [
    "THESE SERVICES ARE PROVIDED BY COMPANY ON AN “AS IS” AND “AS AVAILABLE” BASIS. COMPANY MAKES NO REPRESENTATIONS OR WARRANTIES OF ANY KIND, EXPRESS OR IMPLIED, AS TO THE OPERATION OF THEIR SERVICES, OR THE INFORMATION, CONTENT OR MATERIALS INCLUDED THEREIN. YOU EXPRESSLY AGREE THAT YOUR USE OF THESE SERVICES, THEIR CONTENT, AND ANY SERVICES OR ITEMS OBTAINED FROM US IS AT YOUR SOLE RISK.",
    "NEITHER COMPANY NOR ANY PERSON ASSOCIATED WITH COMPANY MAKES ANY WARRANTY OR REPRESENTATION WITH RESPECT TO THE COMPLETENESS, SECURITY, RELIABILITY, QUALITY, ACCURACY, OR AVAILABILITY OF THE SERVICES. WITHOUT LIMITING THE FOREGOING, NEITHER COMPANY NOR ANYONE ASSOCIATED WITH COMPANY REPRESENTS OR WARRANTS THAT THE SERVICES, THEIR CONTENT, OR ANY SERVICES OR ITEMS OBTAINED THROUGH THE SERVICES WILL BE ACCURATE, RELIABLE, ERROR-FREE, OR UNINTERRUPTED, THAT DEFECTS WILL BE CORRECTED, THAT THE SERVICES OR THE SERVER THAT MAKES IT AVAILABLE ARE FREE OF VIRUSES OR OTHER HARMFUL COMPONENTS OR THAT THE SERVICES OR ANY SERVICES OR ITEMS OBTAINED THROUGH THE SERVICES WILL OTHERWISE MEET YOUR NEEDS OR EXPECTATIONS.",
    "COMPANY HEREBY DISCLAIMS ALL WARRANTIES OF ANY KIND, WHETHER EXPRESS OR IMPLIED, STATUTORY, OR OTHERWISE, INCLUDING BUT NOT LIMITED TO ANY WARRANTIES OF MERCHANTABILITY, NON-INFRINGEMENT, AND FITNESS FOR PARTICULAR PURPOSE.",
    "THE FOREGOING DOES NOT AFFECT ANY WARRANTIES WHICH CANNOT BE EXCLUDED OR LIMITED UNDER APPLICABLE LAW."
  ],
  "Limitation of Liability": [
    "EXCEPT AS PROHIBITED BY LAW, YOU WILL HOLD US AND OUR OFFICERS, DIRECTORS, EMPLOYEES, AND AGENTS HARMLESS FOR ANY INDIRECT, PUNITIVE, SPECIAL, INCIDENTAL, OR CONSEQUENTIAL DAMAGE, HOWEVER IT ARISES (INCLUDING ATTORNEYS' FEES AND ALL RELATED COSTS AND EXPENSES OF LITIGATION AND ARBITRATION, OR AT TRIAL OR ON APPEAL, IF ANY, WHETHER OR NOT LITIGATION OR ARBITRATION IS INSTITUTED), WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE, OR OTHER TORTIOUS ACTION, OR ARISING OUT OF OR IN CONNECTION WITH THIS AGREEMENT, INCLUDING WITHOUT LIMITATION ANY CLAIM FOR PERSONAL INJURY OR PROPERTY DAMAGE, ARISING FROM THIS AGREEMENT AND ANY VIOLATION BY YOU OF ANY FEDERAL, STATE, OR LOCAL LAWS, STATUTES, RULES, OR REGULATIONS, EVEN IF COMPANY HAS BEEN PREVIOUSLY ADVISED OF THE POSSIBILITY OF SUCH DAMAGE. EXCEPT AS PROHIBITED BY LAW, IF THERE IS LIABILITY FOUND ON THE PART OF COMPANY, IT WILL BE LIMITED TO THE AMOUNT PAID FOR THE PRODUCTS AND/OR SERVICES, AND UNDER NO CIRCUMSTANCES WILL THERE BE CONSEQUENTIAL OR PUNITIVE DAMAGES. SOME STATES DO NOT ALLOW THE EXCLUSION OR LIMITATION OF PUNITIVE, INCIDENTAL OR CONSEQUENTIAL DAMAGES, SO THE PRIOR LIMITATION OR EXCLUSION MAY NOT APPLY TO YOU."
  ],
  "Termination": [
    "We may terminate or suspend your account and bar access to Service immediately, without prior notice or liability, under our sole discretion, for any reason whatsoever and without limitation, including but not limited to a breach of Terms.",
    "If you wish to terminate your account, you may simply discontinue using Service.",
    "All provisions of Terms which by their nature should survive termination shall survive termination, including, without limitation, ownership provisions, warranty disclaimers, indemnity and limitations of liability."
  ],
  "Changes To Service": [
    "We reserve the right to withdraw or amend our Service, and any service or material we provide via Service, in our sole discretion without notice. We will not be liable if for any reason all or any part of Service is unavailable at any time or for any period. From time to time, we may restrict access to some parts of Service, or the entire Service, to users, including registered users."
  ],
  "Amendments To Terms": [
    "We may amend Terms at any time by posting the amended terms on this site. It is your responsibility to review these Terms periodically.",
    "Your continued use of the Platform following the posting of revised Terms means that you accept and agree to the changes. You are expected to check this page frequently so you are aware of any changes, as they are binding on you.",
    "By continuing to access or use our Service after any revisions become effective, you agree to be bound by the revised terms. If you do not agree to the new terms, you are no longer authorized to use Service."
  ],
  "Acknowledgement": [
    "BY USING SERVICE OR OTHER SERVICES PROVIDED BY US, YOU ACKNOWLEDGE THAT YOU HAVE READ THESE TERMS OF SERVICE AND AGREE TO BE BOUND BY THEM."
  ],
  "Contact Us": [
    "If you have any questions about these terms of service, please contact us:",
    "By email: contact@todiagram.com."
  ]
}
```

## File: `apps/www/src/enums/file.enum.ts`
```typescript
export enum FileFormat {
  "JSON" = "json",
  "YAML" = "yaml",
  "XML" = "xml",
  "CSV" = "csv",
}

export const formats = [
  { value: FileFormat.JSON, label: "JSON" },
  { value: FileFormat.YAML, label: "YAML" },
  { value: FileFormat.XML, label: "XML" },
  { value: FileFormat.CSV, label: "CSV" },
];

export enum TypeLanguage {
  TypeScript = "typescript",
  TypeScript_Combined = "typescript/typealias",
  Go = "go",
  JSON_SCHEMA = "json_schema",
  Kotlin = "kotlin",
  Rust = "rust",
}

export const typeOptions = [
  {
    label: "TypeScript",
    value: TypeLanguage.TypeScript,
    lang: "typescript",
  },
  {
    label: "TypeScript (merged)",
    value: TypeLanguage.TypeScript_Combined,
    lang: "typescript",
  },
  {
    label: "Go",
    value: TypeLanguage.Go,
    lang: "go",
  },
  {
    label: "JSON Schema",
    value: TypeLanguage.JSON_SCHEMA,
    lang: "json",
  },
  {
    label: "Kotlin",
    value: TypeLanguage.Kotlin,
    lang: "kotlin",
  },
  {
    label: "Rust",
    value: TypeLanguage.Rust,
    lang: "rust",
  },
];
```

## File: `apps/www/src/enums/viewMode.enum.ts`
```typescript
export enum ViewMode {
  Graph = "graph",
  Tree = "tree",
}
```

## File: `apps/www/src/features/Banner.tsx`
```tsx
import React, { useEffect, useState } from "react";
import { Anchor, Flex, Button, ActionIcon } from "@mantine/core";
import { useSessionStorage } from "@mantine/hooks";
import { MdClose } from "react-icons/md";

export const BANNER_HEIGHT =
  process.env.NEXT_PUBLIC_DISABLE_EXTERNAL_MODE === "true" ? "0px" : "40px";

const BANNER_LIST = [
  "Save and store your diagrams with ToDiagram",
  "Explore the ToDiagram from the creators of JSON Crack",
  "Generate AI diagrams with single prompt",
  "Try ToDiagram for free, no sign-up required",
  "Edit data directly inside diagrams",
  "Explore larger datasets (up to 50 MB) easily",
];

export const Banner = () => {
  const ROTATION_INTERVAL = 6000; // ms between label changes
  const FADE_DURATION = 500; // ms for fade transition

  const [index, setIndex] = useState(0);
  const [visible, setVisible] = useState(true);
  const [dismissed, setDismissed] = useSessionStorage({
    key: "jsoncrack_banner_dismissed",
    defaultValue: false,
  });

  useEffect(() => {
    if (dismissed) return;

    let fadeTimeout: ReturnType<typeof setTimeout> | undefined;
    const intervalId = setInterval(() => {
      setVisible(false);
      fadeTimeout = setTimeout(() => {
        setIndex(i => (i + 1) % BANNER_LIST.length);
        setVisible(true);
      }, FADE_DURATION);
    }, ROTATION_INTERVAL);

    return () => {
      clearInterval(intervalId);
      if (fadeTimeout) clearTimeout(fadeTimeout);
    };
  }, [dismissed]);

  const handleDismiss = (e: React.MouseEvent) => {
    e.preventDefault();
    e.stopPropagation();
    setDismissed(true);
  };

  if (dismissed) return null;

  return (
    <Anchor
      href="https://todiagram.com/editor?utm_source=jsoncrack&utm_medium=top_banner"
      target="_blank"
      rel="noopener"
      underline="never"
      style={{ position: "relative" }}
    >
      <Flex
        h={BANNER_HEIGHT}
        justify="center"
        align="center"
        fw="500"
        gap="xs"
        style={{
          background: "linear-gradient(90deg, #FF75B7 0%, #FED761 100%)",
          color: "black",
        }}
      >
        <span
          style={{
            transition: `opacity ${FADE_DURATION}ms ease`,
            opacity: visible ? 1 : 0,
            willChange: "opacity",
            display: "inline-block",
          }}
        >
          {BANNER_LIST[index]}{" "}
        </span>
        <Button size="xs" color="gray">
          Try now
        </Button>
        <ActionIcon
          onClick={handleDismiss}
          size="sm"
          variant="transparent"
          style={{
            position: "absolute",
            right: "8px",
            color: "black",
          }}
          aria-label="Close banner"
        >
          <MdClose size={18} />
        </ActionIcon>
      </Flex>
    </Anchor>
  );
};
```

## File: `apps/www/src/features/editor/BottomBar.tsx`
```tsx
import React from "react";
import { Flex, Menu, Popover, Text } from "@mantine/core";
import styled from "styled-components";
import { event as gaEvent } from "nextjs-google-analytics";
import { BiSolidDockLeft } from "react-icons/bi";
import { IoMdCheckmark } from "react-icons/io";
import { MdArrowUpward } from "react-icons/md";
import { VscCheck, VscError, VscRunAll, VscSync, VscSyncIgnored } from "react-icons/vsc";
import { formats } from "../../enums/file.enum";
import useConfig from "../../store/useConfig";
import useFile from "../../store/useFile";
import useGraph from "./views/GraphView/stores/useGraph";

const StyledBottomBar = styled.div`
  position: relative;
  display: flex;
  align-items: center;
  justify-content: space-between;
  border-top: 1px solid ${({ theme }) => theme.BACKGROUND_MODIFIER_ACCENT};
  background: ${({ theme }) => theme.TOOLBAR_BG};
  max-height: 27px;
  height: 27px;
  z-index: 35;
  padding-right: 6px;

  @media screen and (max-width: 320px) {
    display: none;
  }
`;

const StyledLeft = styled.div`
  display: flex;
  align-items: center;
  justify-content: left;
  gap: 4px;
  padding-left: 8px;

  @media screen and (max-width: 480px) {
    display: none;
  }
`;

const StyledRight = styled.div`
  display: flex;
  align-items: center;
  justify-content: right;
  gap: 4px;
`;

const StyledBottomBarItem = styled.button<{ $bg?: string }>`
  display: flex;
  align-items: center;
  gap: 4px;
  width: fit-content;
  margin: 0;
  height: 28px;
  padding: 4px;
  font-size: 12px;
  font-weight: 400;
  color: ${({ theme }) => theme.INTERACTIVE_NORMAL};
  background: ${({ $bg }) => $bg};
  white-space: nowrap;
  text-overflow: ellipsis;
  overflow: hidden;

  &:hover:not(&:disabled) {
    background-image: linear-gradient(rgba(0, 0, 0, 0.1) 0 0);
    color: ${({ theme }) => theme.INTERACTIVE_HOVER};
  }

  &:disabled {
    opacity: 0.6;
    cursor: default;
  }
`;

export const BottomBar = () => {
  const data = useFile(state => state.fileData);
  const toggleLiveTransform = useConfig(state => state.toggleLiveTransform);
  const liveTransformEnabled = useConfig(state => state.liveTransformEnabled);
  const error = useFile(state => state.error);
  const setContents = useFile(state => state.setContents);
  const toggleFullscreen = useGraph(state => state.toggleFullscreen);
  const fullscreen = useGraph(state => state.fullscreen);
  const setFormat = useFile(state => state.setFormat);
  const currentFormat = useFile(state => state.format);

  const toggleEditor = () => {
    toggleFullscreen(!fullscreen);
    gaEvent("toggle_fullscreen");
  };

  React.useEffect(() => {
    if (data?.name) window.document.title = `${data.name} | JSON Crack`;
  }, [data]);

  return (
    <StyledBottomBar>
      <StyledLeft>
        <StyledBottomBarItem onClick={toggleEditor}>
          <BiSolidDockLeft />
        </StyledBottomBarItem>
        <StyledBottomBarItem>
          {error ? (
            <Popover width="auto" shadow="md" position="top" withArrow>
              <Popover.Target>
                <Flex align="center" gap={2}>
                  <VscError color="red" />
                  <Text c="red" fw={500} fz="xs">
                    Invalid
                  </Text>
                </Flex>
              </Popover.Target>
              <Popover.Dropdown style={{ pointerEvents: "none" }}>
                <Text size="xs">{error}</Text>
              </Popover.Dropdown>
            </Popover>
          ) : (
            <Flex align="center" gap={2}>
              <VscCheck />
              <Text size="xs">Valid</Text>
            </Flex>
          )}
        </StyledBottomBarItem>
        <StyledBottomBarItem
          onClick={() => {
            toggleLiveTransform(!liveTransformEnabled);
            gaEvent("toggle_live_transform");
          }}
        >
          {liveTransformEnabled ? <VscSync /> : <VscSyncIgnored />}
          <Text fz="xs">Live Transform</Text>
        </StyledBottomBarItem>
        {!liveTransformEnabled && (
          <StyledBottomBarItem onClick={() => setContents({})} disabled={!!error}>
            <VscRunAll />
            Click to Transform
          </StyledBottomBarItem>
        )}
      </StyledLeft>

      <StyledRight>
        <Menu offset={8}>
          <Menu.Target>
            <StyledBottomBarItem>
              <Flex align="center" gap={2}>
                <MdArrowUpward />
                <Text size="xs">{currentFormat?.toUpperCase()}</Text>
              </Flex>
            </StyledBottomBarItem>
          </Menu.Target>
          <Menu.Dropdown>
            {formats.map(format => (
              <Menu.Item
                key={format.value}
                fz={12}
                onClick={() => setFormat(format.value)}
                rightSection={currentFormat === format.value && <IoMdCheckmark />}
              >
                {format.label}
              </Menu.Item>
            ))}
          </Menu.Dropdown>
        </Menu>
      </StyledRight>
    </StyledBottomBar>
  );
};
```

## File: `apps/www/src/features/editor/ExternalMode.tsx`
```tsx
import React from "react";
import { Accordion, Anchor, Code, Flex, FocusTrap, Group, Modal, Text } from "@mantine/core";

const ExternalMode = () => {
  const [isExternal, setExternal] = React.useState(false);

  React.useEffect(() => {
    if (process.env.NEXT_PUBLIC_DISABLE_EXTERNAL_MODE === "false") {
      if (typeof window !== "undefined") {
        if (window.location.pathname.includes("widget")) return setExternal(false);
        if (window.location.host !== "jsoncrack.com") return setExternal(true);
        return setExternal(false);
      }
    }
  }, []);

  if (!isExternal) return null;

  return (
    <Modal
      title="Thanks for using JSON Crack"
      opened={isExternal}
      onClose={() => setExternal(false)}
      centered
      size="lg"
    >
      <FocusTrap.InitialFocus />
      <Group>
        <Accordion variant="separated" w="100%">
          <Accordion.Item value="1">
            <Accordion.Control>How can I change the file size limit?</Accordion.Control>
            <Accordion.Panel>
              The main reason for the file size limit is to prevent performance issues, not to push
              you to upgrade. You can increase the limit by setting{" "}
              <Code>NEXT_PUBLIC_NODE_LIMIT</Code> in your <Code>.env</Code> file.
              <br />
              <br />
              If you&apos;d like to work with even larger files and unlock additional features, you
              can upgrade to the{" "}
              <Anchor
                href="https://todiagram.com?utm_source=jsoncrack&utm_medium=external-mode"
                rel="noopener"
                target="_blank"
              >
                Pro
              </Anchor>{" "}
              version.
            </Accordion.Panel>
          </Accordion.Item>
          <Accordion.Item value="2">
            <Accordion.Control>How can I stop this dialog from appearing?</Accordion.Control>
            <Accordion.Panel>
              You can disable this dialog by setting <Code>NEXT_PUBLIC_DISABLE_EXTERNAL_MODE</Code>{" "}
              to <Code>true</Code> in your <Code>.env.development</Code> file.
              <br />
              <br />
              If you want to re-enable it, simply remove or set the value to <Code>false</Code>.
            </Accordion.Panel>
          </Accordion.Item>
          <Accordion.Item value="3">
            <Accordion.Control>What are the license terms?</Accordion.Control>
            <Accordion.Panel>
              Read the full license terms on{" "}
              <Anchor
                href="https://github.com/AykutSarac/jsoncrack.com/blob/main/LICENSE.md"
                rel="noopener"
                target="_blank"
              >
                GitHub
              </Anchor>
              .
            </Accordion.Panel>
          </Accordion.Item>
          <Accordion.Item value="4">
            <Accordion.Control>How do I report a bug or request a feature?</Accordion.Control>
            <Accordion.Panel>
              You can report bugs or request features by opening an issue on our{" "}
              <Anchor
                href="https://github.com/AykutSarac/jsoncrack.com/issues"
                rel="noopener"
                target="_blank"
              >
                GitHub Issues page
              </Anchor>
              .
              <br />
              <br />
              Please provide as much detail as possible to help us address your feedback quickly.
            </Accordion.Panel>
          </Accordion.Item>
          <Accordion.Item value="5">
            <Accordion.Control>How do I contribute to the project?</Accordion.Control>
            <Accordion.Panel>
              We welcome contributions! Visit our{" "}
              <Anchor
                href="https://github.com/AykutSarac/jsoncrack.com"
                rel="noopener"
                target="_blank"
              >
                GitHub repository
              </Anchor>{" "}
              and read the{" "}
              <Anchor
                href="https://github.com/AykutSarac/jsoncrack.com/blob/main/CONTRIBUTING.md"
                rel="noopener"
                target="_blank"
              >
                contributing guide
              </Anchor>{" "}
              to get started.
            </Accordion.Panel>
          </Accordion.Item>
          <Accordion.Item value="6">
            <Accordion.Control>
              What is the difference between JSON Crack and ToDiagram?
            </Accordion.Control>
            <Accordion.Panel>
              JSON Crack is a free and open-source tool for visualizing JSON data. ToDiagram is the
              professional version that offers advanced features, higher limits, and the ability to
              edit data directly from diagrams. You can learn more or upgrade at{" "}
              <Anchor
                href="https://todiagram.com?utm_source=jsoncrack&utm_medium=external-mode"
                rel="noopener"
                target="_blank"
              >
                todiagram.com
              </Anchor>
              .
            </Accordion.Panel>
          </Accordion.Item>
        </Accordion>
      </Group>
      <Flex justify="center" align="center" gap="sm" mt="md">
        <Anchor
          href="https://github.com/AykutSarac/jsoncrack.com"
          rel="noopener"
          target="_blank"
          fz="sm"
        >
          GitHub
        </Anchor>
        <Text c="dimmed">•</Text>
        <Anchor
          href="https://todiagram.com?utm_source=jsoncrack&utm_medium=external-mode"
          rel="noopener"
          target="_blank"
          fz="sm"
        >
          ToDiagram
        </Anchor>
        <Text c="dimmed">•</Text>
        <Anchor href="https://x.com/aykutsarach" rel="noopener" target="_blank" fz="sm">
          Aykut Saraç (@aykutsarach)
        </Anchor>
      </Flex>
    </Modal>
  );
};

export default ExternalMode;
```

## File: `apps/www/src/features/editor/FullscreenDropzone.tsx`
```tsx
import React from "react";
import { Group, Text } from "@mantine/core";
import { Dropzone } from "@mantine/dropzone";
import toast from "react-hot-toast";
import { VscCircleSlash, VscFiles } from "react-icons/vsc";
import { FileFormat } from "../../enums/file.enum";
import useFile from "../../store/useFile";

export const FullscreenDropzone = () => {
  const setContents = useFile(state => state.setContents);

  return (
    <Dropzone.FullScreen
      maxFiles={1}
      accept={["application/json", "application/x-yaml", "text/csv", "application/xml"]}
      onReject={files => toast.error(`Unable to load file ${files[0].file.name}`)}
      onDrop={async e => {
        try {
          const fileContent = await e[0].text();
          let fileExtension = e[0].name.split(".").pop() as FileFormat | undefined;
          if (!fileExtension) fileExtension = FileFormat.JSON;
          setContents({ contents: fileContent, format: fileExtension, hasChanges: false });
        } catch (err) {
          toast.error("An error occurred while reading the file.");
          console.error(err);
        }
      }}
    >
      <Group
        justify="center"
        ta="center"
        align="center"
        gap="xl"
        h="100vh"
        style={{ pointerEvents: "none" }}
      >
        <Dropzone.Accept>
          <VscFiles size={100} />
          <Text fz="h1" fw={500} mt="lg">
            Upload to JSON Crack
          </Text>
          <Text fz="lg" c="dimmed" mt="sm">
            (Max file size: 300 KB)
          </Text>
        </Dropzone.Accept>
        <Dropzone.Reject>
          <VscCircleSlash size={100} />
          <Text fz="h1" fw={500} mt="lg">
            Invalid file
          </Text>
          <Text fz="lg" c="dimmed" mt="sm">
            Allowed formats are JSON, YAML, CSV, XML
          </Text>
        </Dropzone.Reject>
      </Group>
    </Dropzone.FullScreen>
  );
};
```

## File: `apps/www/src/features/editor/LiveEditor.tsx`
```tsx
import React from "react";
import { useSessionStorage } from "@mantine/hooks";
import styled from "styled-components";
import { ViewMode } from "../../enums/viewMode.enum";
import { GraphView } from "./views/GraphView";
import { TreeView } from "./views/TreeView";

const StyledLiveEditor = styled.div`
  position: relative;
  height: 100%;
  background: ${({ theme }) => theme.GRID_BG_COLOR};
  overflow: auto;

  & > ul {
    margin-top: 0 !important;
    padding: 12px !important;
    font-family: monospace;
    font-size: 14px;
    font-weight: 500;
  }

  .tab-group {
    position: absolute;
    top: 10px;
    left: 10px;
    z-index: 2;
  }
`;

const View = () => {
  const [viewMode] = useSessionStorage({
    key: "viewMode",
    defaultValue: ViewMode.Graph,
  });

  if (viewMode === ViewMode.Graph) return <GraphView />;
  if (viewMode === ViewMode.Tree) return <TreeView />;
  return null;
};

const LiveEditor = () => {
  return (
    <StyledLiveEditor onContextMenuCapture={e => e.preventDefault()}>
      <View />
    </StyledLiveEditor>
  );
};

export default LiveEditor;
```

## File: `apps/www/src/features/editor/TextEditor.tsx`
```tsx
import React, { useCallback } from "react";
import { LoadingOverlay } from "@mantine/core";
import styled from "styled-components";
import Editor, { type EditorProps, loader, type OnMount, useMonaco } from "@monaco-editor/react";
import useConfig from "../../store/useConfig";
import useFile from "../../store/useFile";

loader.config({
  paths: {
    vs: "https://cdnjs.cloudflare.com/ajax/libs/monaco-editor/0.52.2/min/vs",
  },
});

const editorOptions: EditorProps["options"] = {
  tabSize: 2,
  formatOnType: true,
  minimap: { enabled: false },
  stickyScroll: { enabled: false },
  scrollBeyondLastLine: false,
  placeholder: "Start typing...",
};

const TextEditor = () => {
  const monaco = useMonaco();
  const contents = useFile(state => state.contents);
  const setContents = useFile(state => state.setContents);
  const setError = useFile(state => state.setError);
  const jsonSchema = useFile(state => state.jsonSchema);
  const getHasChanges = useFile(state => state.getHasChanges);
  const theme = useConfig(state => (state.darkmodeEnabled ? "vs-dark" : "light"));
  const fileType = useFile(state => state.format);
  const jsonDefaults = (monaco?.languages as any)?.json?.jsonDefaults as
    | { setDiagnosticsOptions: (options: unknown) => void }
    | undefined;

  React.useEffect(() => {
    if (!jsonDefaults) return;

    jsonDefaults.setDiagnosticsOptions({
      validate: true,
      allowComments: true,
      enableSchemaRequest: true,
      ...(jsonSchema && {
        schemas: [
          {
            uri: "http://myserver/foo-schema.json",
            fileMatch: ["*"],
            schema: jsonSchema,
          },
        ],
      }),
    });
  }, [jsonDefaults, jsonSchema]);

  React.useEffect(() => {
    const beforeunload = (e: BeforeUnloadEvent) => {
      if (getHasChanges()) {
        const confirmationMessage =
          "Unsaved changes, if you leave before saving  your changes will be lost";

        (e || window.event).returnValue = confirmationMessage; //Gecko + IE
        return confirmationMessage;
      }
    };

    window.addEventListener("beforeunload", beforeunload);

    return () => {
      window.removeEventListener("beforeunload", beforeunload);
    };
  }, [getHasChanges]);

  const handleMount: OnMount = useCallback(editor => {
    editor.onDidPaste(() => {
      editor.getAction("editor.action.formatDocument")?.run();
    });
  }, []);

  return (
    <StyledEditorWrapper>
      <StyledWrapper>
        <Editor
          height="100%"
          language={fileType}
          theme={theme}
          value={contents}
          options={editorOptions}
          onMount={handleMount}
          onValidate={errors => setError(errors[0]?.message || "")}
          onChange={contents => setContents({ contents, skipUpdate: true })}
          loading={<LoadingOverlay visible />}
        />
      </StyledWrapper>
    </StyledEditorWrapper>
  );
};

export default TextEditor;

const StyledEditorWrapper = styled.div`
  display: flex;
  flex-direction: column;
  height: 100%;
  user-select: none;
`;

const StyledWrapper = styled.div`
  display: grid;
  height: 100%;
  grid-template-columns: 100%;
  grid-template-rows: minmax(0, 1fr);
`;
```

## File: `apps/www/src/features/editor/Toolbar/FileMenu.tsx`
```tsx
import React from "react";
import { Flex, Menu } from "@mantine/core";
import { event as gaEvent } from "nextjs-google-analytics";
import { CgChevronDown } from "react-icons/cg";
import useFile from "../../../store/useFile";
import { useModal } from "../../../store/useModal";
import { StyledToolElement } from "./styles";

export const FileMenu = () => {
  const setVisible = useModal(state => state.setVisible);
  const getContents = useFile(state => state.getContents);
  const getFormat = useFile(state => state.getFormat);

  const handleSave = () => {
    const a = document.createElement("a");
    const file = new Blob([getContents()], { type: "text/plain" });

    a.href = window.URL.createObjectURL(file);
    a.download = `jsoncrack.${getFormat()}`;
    a.click();

    gaEvent("save_file", { label: getFormat() });
  };

  return (
    <Menu shadow="md" withArrow>
      <Menu.Target>
        <StyledToolElement title="File">
          <Flex align="center" gap={3}>
            File
            <CgChevronDown />
          </Flex>
        </StyledToolElement>
      </Menu.Target>
      <Menu.Dropdown>
        <Menu.Item onClick={() => setVisible("ImportModal", true)}>Import</Menu.Item>
        <Menu.Item onClick={handleSave}>Export</Menu.Item>
      </Menu.Dropdown>
    </Menu>
  );
};
```

## File: `apps/www/src/features/editor/Toolbar/index.tsx`
```tsx
import React from "react";
import Link from "next/link";
import { Flex, Group } from "@mantine/core";
import styled from "styled-components";
import toast from "react-hot-toast";
import { AiOutlineFullscreen } from "react-icons/ai";
import { FaGithub } from "react-icons/fa6";
import { JSONCrackLogo } from "../../../layout/JSONCrackBrandLogo";
import { FileMenu } from "./FileMenu";
import { ThemeToggle } from "./ThemeToggle";
import { ToolsMenu } from "./ToolsMenu";
import { ViewMenu } from "./ViewMenu";
import { StyledToolElement } from "./styles";

const StyledTools = styled.div`
  position: relative;
  display: flex;
  width: 100%;
  align-items: center;
  gap: 4px;
  justify-content: space-between;
  height: 45px;
  padding: 6px 12px;
  background: ${({ theme }) => theme.TOOLBAR_BG};
  color: ${({ theme }) => theme.SILVER};
  z-index: 36;
  border-bottom: 1px solid ${({ theme }) => theme.SILVER_DARK};

  @media only screen and (max-width: 320px) {
    display: none;
  }
`;

function fullscreenBrowser() {
  if (!document.fullscreenElement) {
    document.documentElement.requestFullscreen().catch(() => {
      toast.error("Unable to enter fullscreen mode.");
    });
  } else if (document.exitFullscreen) {
    document.exitFullscreen();
  }
}

export const Toolbar = () => {
  return (
    <StyledTools>
      <Group gap="xs" justify="left" w="100%" style={{ flexWrap: "nowrap" }}>
        <StyledToolElement title="JSON Crack">
          <Flex gap="xs" align="center" justify="center">
            <JSONCrackLogo fontSize="14px" hideLogo />
          </Flex>
        </StyledToolElement>
        <FileMenu />
        <ViewMenu />
        <ToolsMenu />
      </Group>
      <Group gap="xs" justify="right" w="100%" style={{ flexWrap: "nowrap" }}>
        <ThemeToggle />
        <Link href="https://github.com/AykutSarac/jsoncrack.com" rel="noopener" target="_blank">
          <StyledToolElement title="GitHub">
            <FaGithub size="20" />
          </StyledToolElement>
        </Link>
        <StyledToolElement title="Fullscreen" onClick={fullscreenBrowser}>
          <AiOutlineFullscreen size="20" />
        </StyledToolElement>
      </Group>
    </StyledTools>
  );
};
```

## File: `apps/www/src/features/editor/Toolbar/SearchInput.tsx`
```tsx
import React from "react";
import { Flex, Text, TextInput } from "@mantine/core";
import { getHotkeyHandler } from "@mantine/hooks";
import { useOs } from "@mantine/hooks";
import { AiOutlineSearch } from "react-icons/ai";
import { useFocusNode } from "../../../hooks/useFocusNode";

export const SearchInput = () => {
  const [searchValue, setValue, skip, nodeCount, currentNode] = useFocusNode();
  const os = useOs();

  const coreKey = os === "macos" ? "⌘" : "Ctrl";

  return (
    <TextInput
      variant="unstyled"
      type="search"
      size="xs"
      id="search-node"
      w={180}
      value={searchValue}
      onChange={e => setValue(e.currentTarget.value)}
      placeholder={`Search Node (${coreKey} + F)`}
      autoComplete="off"
      autoCorrect="off"
      onKeyDown={getHotkeyHandler([["Enter", skip]])}
      leftSection={<AiOutlineSearch />}
      rightSection={
        searchValue && (
          <Flex h={30} align="center">
            <Text size="xs" c="dimmed" pr="md">
              {searchValue && `${nodeCount}/${nodeCount > 0 ? currentNode + 1 : "0"}`}
            </Text>
          </Flex>
        )
      }
      style={{ borderBottom: "1px solid gray" }}
    />
  );
};
```

## File: `apps/www/src/features/editor/Toolbar/styles.ts`
```typescript
import styled from "styled-components";

export const StyledToolElement = styled.button<{ $hide?: boolean; $highlight?: boolean }>`
  display: ${({ $hide }) => ($hide ? "none" : "flex")};
  align-items: center;
  gap: 4px;
  place-content: center;
  font-size: 14px;
  background: ${({ $highlight }) =>
    $highlight ? "linear-gradient(rgba(0, 0, 0, 0.1) 0 0)" : "none"};
  color: ${({ theme }) => theme.INTERACTIVE_NORMAL};
  padding: 6px;
  border-radius: 3px;
  white-space: nowrap;

  &:hover {
    background-image: linear-gradient(rgba(0, 0, 0, 0.1) 0 0);
  }

  &:hover {
    color: ${({ theme }) => theme.INTERACTIVE_HOVER};
    opacity: 1;
    box-shadow: none;
  }
`;
```

## File: `apps/www/src/features/editor/Toolbar/ThemeToggle.tsx`
```tsx
import { FaMoon, FaSun } from "react-icons/fa6";
import useConfig from "../../../store/useConfig";
import { StyledToolElement } from "./styles";

export const ThemeToggle = () => {
  const darkmodeEnabled = useConfig(state => state.darkmodeEnabled);
  const toggleDarkMode = useConfig(state => state.toggleDarkMode);

  return (
    <StyledToolElement title="Fullscreen" onClick={() => toggleDarkMode(!darkmodeEnabled)}>
      {!darkmodeEnabled ? <FaMoon size="18" /> : <FaSun size="18" />}
    </StyledToolElement>
  );
};
```

## File: `apps/www/src/features/editor/Toolbar/ToolsMenu.tsx`
```tsx
import React from "react";
import { Menu, Flex } from "@mantine/core";
import { event as gaEvent } from "nextjs-google-analytics";
import { CgChevronDown } from "react-icons/cg";
import { MdFilterListAlt } from "react-icons/md";
import { VscSearchFuzzy, VscJson, VscGroupByRefType } from "react-icons/vsc";
import { useModal } from "../../../store/useModal";
import { StyledToolElement } from "./styles";

export const ToolsMenu = () => {
  const setVisible = useModal(state => state.setVisible);

  return (
    <Menu shadow="md" withArrow>
      <Menu.Target>
        <StyledToolElement onClick={() => gaEvent("show_tools_menu")}>
          <Flex align="center" gap={3}>
            Tools <CgChevronDown />
          </Flex>
        </StyledToolElement>
      </Menu.Target>
      <Menu.Dropdown>
        <Menu.Item
          leftSection={<VscSearchFuzzy />}
          onClick={() => {
            setVisible("JQModal", true);
            gaEvent("open_jq_modal");
          }}
        >
          JSON Query (jq)
        </Menu.Item>
        <Menu.Item
          leftSection={<MdFilterListAlt />}
          onClick={() => {
            setVisible("JPathModal", true);
            gaEvent("open_json_path_modal");
          }}
        >
          JSON Path
        </Menu.Item>
        <Menu.Item
          leftSection={<VscJson />}
          onClick={() => {
            setVisible("SchemaModal", true);
            gaEvent("open_schema_modal");
          }}
        >
          JSON Schema
        </Menu.Item>
        <Menu.Divider />
        <Menu.Item
          leftSection={<VscGroupByRefType />}
          onClick={() => {
            setVisible("TypeModal", true);
            gaEvent("open_type_modal");
          }}
        >
          Generate Type
        </Menu.Item>
      </Menu.Dropdown>
    </Menu>
  );
};
```

## File: `apps/www/src/features/editor/Toolbar/ViewMenu.tsx`
```tsx
import { Menu, Flex, SegmentedControl } from "@mantine/core";
import { useSessionStorage } from "@mantine/hooks";
import { event as gaEvent } from "nextjs-google-analytics";
import { CgChevronDown } from "react-icons/cg";
import { ViewMode } from "../../../enums/viewMode.enum";
import { StyledToolElement } from "./styles";

export const ViewMenu = () => {
  const [viewMode, setViewMode] = useSessionStorage({
    key: "viewMode",
    defaultValue: ViewMode.Graph,
  });

  return (
    <Menu shadow="md" closeOnItemClick={false} withArrow>
      <Menu.Target>
        <StyledToolElement onClick={() => gaEvent("show_view_menu")}>
          <Flex align="center" gap={3}>
            View <CgChevronDown />
          </Flex>
        </StyledToolElement>
      </Menu.Target>
      <Menu.Dropdown>
        <SegmentedControl
          size="md"
          w="100%"
          value={viewMode}
          onChange={e => {
            setViewMode(e as ViewMode);
            gaEvent("change_view_mode", { label: e });
          }}
          data={[
            { value: ViewMode.Graph, label: "Graph" },
            { value: ViewMode.Tree, label: "Tree" },
          ]}
          fullWidth
          orientation="vertical"
        />
      </Menu.Dropdown>
    </Menu>
  );
};
```

## File: `apps/www/src/features/editor/views/GraphView/index.tsx`
```tsx
import React from "react";
import { Box } from "@mantine/core";
import styled from "styled-components";
import { JSONCrack } from "jsoncrack-react";
import type { NodeData } from "jsoncrack-react";
import { useLongPress } from "use-long-press";
import { SUPPORTED_LIMIT } from "../../../../constants/graph";
import useConfig from "../../../../store/useConfig";
import useJson from "../../../../store/useJson";
import { useModal } from "../../../../store/useModal";
import { NotSupported } from "./NotSupported";
import { OptionsMenu } from "./OptionsMenu";
import { SecureInfo } from "./SecureInfo";
import { ZoomControl } from "./ZoomControl";
import useGraph from "./stores/useGraph";

const StyledEditorWrapper = styled.div<{ $widget: boolean }>`
  width: 100%;
  height: 100%;

  .jsoncrack-space,
  .jsoncrack-space:active {
    cursor: url("/assets/cursor.svg"), auto;
  }
`;

interface GraphProps {
  isWidget?: boolean;
}

export const GraphView = ({ isWidget = false }: GraphProps) => {
  const setViewPort = useGraph(state => state.setViewPort);
  const direction = useGraph(state => state.direction);
  const setSelectedNode = useGraph(state => state.setSelectedNode);
  const gesturesEnabled = useConfig(state => state.gesturesEnabled);
  const rulersEnabled = useConfig(state => state.rulersEnabled);
  const darkmodeEnabled = useConfig(state => state.darkmodeEnabled);
  const json = useJson(state => state.json);
  const setVisible = useModal(state => state.setVisible);

  const callback = React.useCallback(() => {
    const canvas = document.querySelector(".jsoncrack-canvas") as HTMLDivElement | null;
    canvas?.classList.add("dragging");
  }, []);

  const bindLongPress = useLongPress(callback, {
    threshold: 150,
    onFinish: () => {
      const canvas = document.querySelector(".jsoncrack-canvas") as HTMLDivElement | null;
      canvas?.classList.remove("dragging");
    },
  });

  const blurOnClick = React.useCallback(() => {
    if ("activeElement" in document) {
      (document.activeElement as HTMLElement | null)?.blur();
    }
  }, []);

  const handleNodeClick = React.useCallback(
    (node: NodeData) => {
      setSelectedNode(node);
      setVisible("NodeModal", true);
    },
    [setSelectedNode, setVisible]
  );

  const maxVisibleNodes = Number.isFinite(SUPPORTED_LIMIT) ? SUPPORTED_LIMIT : 1500;

  return (
    <Box pos="relative" h="100%" w="100%">
      {!isWidget && <OptionsMenu />}
      {!isWidget && <SecureInfo />}
      <ZoomControl />
      <StyledEditorWrapper
        $widget={isWidget}
        onContextMenu={event => event.preventDefault()}
        onClick={blurOnClick}
        {...bindLongPress()}
      >
        <JSONCrack
          key={[direction, gesturesEnabled, rulersEnabled].join("-")}
          json={json}
          theme={darkmodeEnabled ? "dark" : "light"}
          layoutDirection={direction}
          showControls={false}
          showGrid={rulersEnabled}
          trackpadZoom={gesturesEnabled}
          maxRenderableNodes={maxVisibleNodes}
          centerOnLayout
          onViewportCreate={setViewPort}
          onNodeClick={handleNodeClick}
          renderNodeLimitExceeded={() => <NotSupported />}
        />
      </StyledEditorWrapper>
    </Box>
  );
};
```

## File: `apps/www/src/features/editor/views/GraphView/NotSupported.tsx`
```tsx
import React from "react";
import { Anchor, Button, Image, Overlay, Stack, Text } from "@mantine/core";
import styled, { keyframes } from "styled-components";
import useConfig from "../../../../store/useConfig";

const shineEffect = keyframes`
  0% {
    transform: translateX(-120%) rotate(25deg);
    opacity: 0.5;
  }
  5% {
    opacity: 0.5;
    transform: translateX(-80%) rotate(25deg);
  }
  70% {
    transform: translateX(80%) rotate(25deg);
    opacity: 0.5;
  }
  80% {
    transform: translateX(120%) rotate(25deg);
    opacity: 0;
  }
  100% {
    transform: translateX(120%) rotate(25deg);
    opacity: 0;
  }
`;

const ShiningButton = styled.div`
  position: relative;
  overflow: hidden;
  display: inline-block;
  border-radius: 0.5rem;
  z-index: 10;

  &::before {
    content: "";
    position: absolute;
    top: -50%;
    left: -50%;
    width: 200%;
    height: 200%;
    background: linear-gradient(
      to right,
      rgba(255, 255, 255, 0) 0%,
      rgba(255, 255, 255, 0) 35%,
      rgba(255, 255, 255, 0.5) 50%,
      rgba(255, 255, 255, 0) 65%,
      rgba(255, 255, 255, 0) 100%
    );
    transform: translateX(-120%) rotate(25deg);
    z-index: 20;
    pointer-events: none;
    animation: ${shineEffect} 4s ease-out infinite;
    transition: transform 0.2s ease-out;
  }
`;

export const NotSupported = () => {
  const darkmodeEnabled = useConfig(state => state.darkmodeEnabled);

  return (
    <Overlay
      backgroundOpacity={0.8}
      color={darkmodeEnabled ? "gray" : "rgb(226, 240, 243)"}
      blur="1.5"
      center
    >
      <Stack maw="60%" align="center" justify="center" gap="sm">
        <Image src="https://todiagram.com/logo.svg" alt="Unsupported" w={72} h={72} />
        <Text fz="48" fw={600} c="bright">
          Time to upgrade!
        </Text>
        <Text ta="center" size="lg" fw={500} c="gray" maw="600">
          This diagram is too large and not supported at JSON Crack.
          <br />
          Try{" "}
          <Anchor
            inherit
            c="teal"
            fw="500"
            href="https://todiagram.com/editor?utm_source=jsoncrack&utm_medium=data_limit"
            target="_blank"
            rel="noopener"
          >
            ToDiagram
          </Anchor>{" "}
          for larger diagrams and more features.
        </Text>
        <ShiningButton style={{ marginTop: "16px", position: "relative" }}>
          <Button
            component="a"
            href="https://todiagram.com/editor?utm_source=jsoncrack&utm_medium=data_limit"
            rel="noopener"
            size="lg"
            w="200"
            target="_blank"
            color="teal"
          >
            Try now &rarr;
          </Button>
        </ShiningButton>
      </Stack>
    </Overlay>
  );
};
```

## File: `apps/www/src/features/editor/views/GraphView/OptionsMenu.tsx`
```tsx
import React from "react";
import { ActionIcon, Flex, Menu, Text } from "@mantine/core";
import { useHotkeys } from "@mantine/hooks";
import styled from "styled-components";
import type { LayoutDirection } from "jsoncrack-react";
import { event as gaEvent } from "nextjs-google-analytics";
import { BsCheck2 } from "react-icons/bs";
import { LuImageDown, LuMenu } from "react-icons/lu";
import { TiFlowMerge } from "react-icons/ti";
import useConfig from "../../../../store/useConfig";
import { useModal } from "../../../../store/useModal";
import useGraph from "./stores/useGraph";

const StyledFlowIcon = styled(TiFlowMerge)<{ rotate: number }>`
  transform: rotate(${({ rotate }) => `${rotate}deg`});
`;

const getNextDirection = (direction: LayoutDirection) => {
  if (direction === "RIGHT") return "DOWN";
  if (direction === "DOWN") return "LEFT";
  if (direction === "LEFT") return "UP";
  return "RIGHT";
};

const rotateLayout = (direction: LayoutDirection) => {
  if (direction === "LEFT") return 90;
  if (direction === "UP") return 180;
  if (direction === "RIGHT") return 270;
  return 360;
};

export const OptionsMenu = () => {
  const toggleGestures = useConfig(state => state.toggleGestures);
  const toggleRulers = useConfig(state => state.toggleRulers);
  const gesturesEnabled = useConfig(state => state.gesturesEnabled);
  const rulersEnabled = useConfig(state => state.rulersEnabled);
  const setDirection = useGraph(state => state.setDirection);
  const direction = useGraph(state => state.direction);
  const setVisible = useModal(state => state.setVisible);
  const [coreKey, setCoreKey] = React.useState("CTRL");

  const toggleDirection = () => {
    const nextDirection = getNextDirection(direction || "RIGHT");
    if (setDirection) setDirection(nextDirection);
  };

  useHotkeys(
    [
      ["mod+shift+d", toggleDirection],
      [
        "mod+f",
        () => {
          const input = document.querySelector("#search-node") as HTMLInputElement;
          input.focus();
        },
      ],
    ],
    []
  );

  React.useEffect(() => {
    if (typeof window !== "undefined") {
      setCoreKey(navigator.userAgent.indexOf("Mac OS X") ? "⌘" : "CTRL");
    }
  }, []);

  return (
    <Flex
      gap="xs"
      align="center"
      style={{
        position: "absolute",
        top: "10px",
        left: "10px",
        zIndex: 100,
      }}
    >
      <Menu withArrow>
        <Menu.Target>
          <ActionIcon aria-label="actions" size="lg" color="gray" variant="light">
            <LuMenu size="18" />
          </ActionIcon>
        </Menu.Target>
        <Menu.Dropdown>
          <Menu.Item
            fz="sm"
            leftSection={<LuImageDown color="gray" />}
            onClick={() => setVisible("DownloadModal", true)}
          >
            <Flex justify="space-between" gap="md">
              <Text inherit>Export</Text>
              <Text fz="xs" ml="md" c="dimmed">
                {coreKey} + S
              </Text>
            </Flex>
          </Menu.Item>
          <Menu.Item
            fz="sm"
            onClick={() => {
              toggleDirection();
              gaEvent("rotate_layout", { label: direction });
            }}
            leftSection={
              <StyledFlowIcon color="gray" rotate={rotateLayout(direction || "RIGHT")} />
            }
            rightSection={
              <Text fz="xs" ml="md" c="dimmed">
                {coreKey} Shift D
              </Text>
            }
            closeMenuOnClick={false}
          >
            Rotate Layout
          </Menu.Item>
          <Menu.Divider />
          <Menu.Sub position="right" offset={0}>
            <Menu.Sub.Target>
              <Menu.Sub.Item fz="sm">View Options</Menu.Sub.Item>
            </Menu.Sub.Target>
            <Menu.Sub.Dropdown>
              <Menu.Item
                fz="sm"
                leftSection={<BsCheck2 opacity={rulersEnabled ? 100 : 0} />}
                onClick={() => {
                  toggleRulers(!rulersEnabled);
                  gaEvent("toggle_rulers", { label: rulersEnabled ? "on" : "off" });
                }}
                closeMenuOnClick={false}
              >
                Rulers
              </Menu.Item>
              <Menu.Item
                fz="sm"
                leftSection={<BsCheck2 opacity={gesturesEnabled ? 100 : 0} />}
                onClick={() => {
                  toggleGestures(!gesturesEnabled);
                  gaEvent("toggle_gestures", { label: gesturesEnabled ? "on" : "off" });
                }}
              >
                Zoom on Scroll
              </Menu.Item>
            </Menu.Sub.Dropdown>
          </Menu.Sub>
        </Menu.Dropdown>
      </Menu>
    </Flex>
  );
};
```

## File: `apps/www/src/features/editor/views/GraphView/SecureInfo.tsx`
```tsx
import React from "react";
import { ThemeIcon, Tooltip } from "@mantine/core";
import { LuShieldCheck } from "react-icons/lu";

export const SecureInfo = () => {
  return (
    <Tooltip
      label="Your data is processed locally on your device."
      fz="xs"
      ta="center"
      maw="200"
      multiline
      withArrow
    >
      <ThemeIcon
        variant="light"
        color="teal"
        size="36"
        style={{
          position: "absolute",
          bottom: "10px",
          right: "10px",
          zIndex: 100,
        }}
        radius="xl"
      >
        <LuShieldCheck size="22" />
      </ThemeIcon>
    </Tooltip>
  );
};
```

## File: `apps/www/src/features/editor/views/GraphView/ZoomControl.tsx`
```tsx
import React from "react";
import { ActionIcon, Flex, Tooltip, Text } from "@mantine/core";
import { useHotkeys } from "@mantine/hooks";
import { event as gaEvent } from "nextjs-google-analytics";
import { LuFocus, LuMaximize, LuMinus, LuPlus } from "react-icons/lu";
import { SearchInput } from "../../Toolbar/SearchInput";
import useGraph from "./stores/useGraph";

export const ZoomControl = () => {
  const zoomIn = useGraph(state => state.zoomIn);
  const zoomOut = useGraph(state => state.zoomOut);
  const centerView = useGraph(state => state.centerView);
  const focusFirstNode = useGraph(state => state.focusFirstNode);

  useHotkeys(
    [
      ["mod+[plus]", zoomIn, { usePhysicalKeys: true }],
      ["mod+[minus]", zoomOut, { usePhysicalKeys: true }],
      ["shift+Digit1", focusFirstNode, { usePhysicalKeys: true }],
      ["shift+Digit2", centerView, { usePhysicalKeys: true }],
    ],
    []
  );

  return (
    <Flex
      align="center"
      gap="xs"
      style={{
        position: "absolute",
        bottom: "10px",
        left: "10px",
        alignItems: "start",
        zIndex: 100,
      }}
    >
      <ActionIcon.Group borderWidth={0}>
        <Tooltip
          label={
            <Flex fz="xs" gap="md">
              <Text fz="xs">Center first item</Text>
              <Text fz="xs" c="dimmed">
                ⇧ 1
              </Text>
            </Flex>
          }
          withArrow
        >
          <ActionIcon
            size="lg"
            variant="light"
            color="gray"
            onClick={() => {
              focusFirstNode();
              gaEvent("focus_first_node");
            }}
          >
            <LuFocus />
          </ActionIcon>
        </Tooltip>
        <Tooltip
          label={
            <Flex fz="xs" gap="md">
              <Text fz="xs">Fit to center</Text>
              <Text fz="xs" c="dimmed">
                ⇧ 2
              </Text>
            </Flex>
          }
          withArrow
        >
          <ActionIcon
            size="lg"
            variant="light"
            color="gray"
            onClick={() => {
              centerView();
              gaEvent("center_view");
            }}
          >
            <LuMaximize />
          </ActionIcon>
        </Tooltip>
        <ActionIcon
          size="lg"
          variant="light"
          color="gray"
          onClick={() => {
            zoomOut();
            gaEvent("zoom_out");
          }}
        >
          <LuMinus />
        </ActionIcon>
        <ActionIcon
          size="lg"
          variant="light"
          color="gray"
          onClick={() => {
            zoomIn();
            gaEvent("zoom_in");
          }}
        >
          <LuPlus />
        </ActionIcon>
      </ActionIcon.Group>
      <SearchInput />
    </Flex>
  );
};
```

## File: `apps/www/src/features/editor/views/GraphView/CustomEdge/index.tsx`
```tsx
import React from "react";
import { useComputedColorScheme } from "@mantine/core";
import type { EdgeProps } from "reaflow";
import { Edge } from "reaflow";
import useGraph from "../stores/useGraph";

const CustomEdgeWrapper = (props: EdgeProps) => {
  const colorScheme = useComputedColorScheme();
  const viewPort = useGraph(state => state.viewPort);
  const [hovered, setHovered] = React.useState(false);

  const handeClick = () => {
    const targetNodeId = (props.properties as { to?: string } | undefined)?.to;
    const targetNodeDom = document.querySelector(
      `[data-id$="node-${targetNodeId}"]`
    ) as HTMLElement;
    if (targetNodeDom && targetNodeDom.parentElement) {
      viewPort?.camera.centerFitElementIntoView(targetNodeDom.parentElement, {
        elementExtraMarginForZoom: 150,
      });
    }
  };

  return (
    <Edge
      containerClassName={`edge-${props.id}`}
      onClick={handeClick}
      onEnter={() => setHovered(true)}
      onLeave={() => setHovered(false)}
      style={{
        stroke: colorScheme === "dark" ? "#444444" : "#BCBEC0",
        ...(hovered && { stroke: "#3B82F6" }),
        strokeWidth: 1.5,
      }}
      {...props}
    />
  );
};

export const CustomEdge = React.memo(CustomEdgeWrapper);
```

## File: `apps/www/src/features/editor/views/GraphView/CustomNode/index.tsx`
```tsx
import React from "react";
import { useComputedColorScheme } from "@mantine/core";
import type { NodeData } from "jsoncrack-react";
import type { NodeProps } from "reaflow";
import { Node } from "reaflow";
import { useModal } from "../../../../../store/useModal";
import useGraph from "../stores/useGraph";
import { ObjectNode } from "./ObjectNode";
import { TextNode } from "./TextNode";

export interface CustomNodeProps {
  node: NodeData;
  x: number;
  y: number;
  hasCollapse?: boolean;
}

const CustomNodeWrapper = (nodeProps: NodeProps<NodeData>) => {
  const setSelectedNode = useGraph(state => state.setSelectedNode);
  const setVisible = useModal(state => state.setVisible);
  const colorScheme = useComputedColorScheme();

  const handleNodeClick = React.useCallback(
    (_: React.MouseEvent<SVGGElement, MouseEvent>, data: NodeData) => {
      if (setSelectedNode) setSelectedNode(data);
      setVisible("NodeModal", true);
    },
    [setSelectedNode, setVisible]
  );

  return (
    <Node
      {...nodeProps}
      onClick={handleNodeClick as any}
      animated={false}
      label={null as any}
      onEnter={ev => {
        ev.currentTarget.style.stroke = "#3B82F6";
      }}
      onLeave={ev => {
        ev.currentTarget.style.stroke = colorScheme === "dark" ? "#424242" : "#BCBEC0";
      }}
      style={{
        fill: colorScheme === "dark" ? "#292929" : "#ffffff",
        stroke: colorScheme === "dark" ? "#424242" : "#BCBEC0",
        strokeWidth: 1,
      }}
    >
      {({ node, x, y }) => {
        const hasKey = nodeProps.properties.text[0].key;
        if (!hasKey) return <TextNode node={nodeProps.properties as NodeData} x={x} y={y} />;

        return <ObjectNode node={node as NodeData} x={x} y={y} />;
      }}
    </Node>
  );
};

export const CustomNode = React.memo(CustomNodeWrapper);
```

## File: `apps/www/src/features/editor/views/GraphView/CustomNode/ObjectNode.tsx`
```tsx
import React from "react";
import type { NodeData } from "jsoncrack-react";
import type { CustomNodeProps } from ".";
import { NODE_DIMENSIONS } from "../../../../../constants/graph";
import { TextRenderer } from "./TextRenderer";
import * as Styled from "./styles";

type RowProps = {
  row: NodeData["text"][number];
  x: number;
  y: number;
  index: number;
};

const Row = ({ row, x, y, index }: RowProps) => {
  const rowPosition = index * NODE_DIMENSIONS.ROW_HEIGHT;

  const getRowText = () => {
    if (row.type === "object") return `{${row.childrenCount ?? 0} keys}`;
    if (row.type === "array") return `[${row.childrenCount ?? 0} items]`;
    return row.value;
  };

  return (
    <Styled.StyledRow
      $value={row.value}
      data-key={`${row.key}: ${row.value}`}
      data-x={x}
      data-y={y + rowPosition}
    >
      <Styled.StyledKey $type="object">{row.key}: </Styled.StyledKey>
      <TextRenderer>{getRowText()}</TextRenderer>
    </Styled.StyledRow>
  );
};

const Node = ({ node, x, y }: CustomNodeProps) => (
  <Styled.StyledForeignObject
    data-id={`node-${node.id}`}
    width={node.width}
    height={node.height}
    x={0}
    y={0}
    $isObject
  >
    {node.text.map((row, index) => (
      <Row key={`${node.id}-${index}`} row={row} x={x} y={y} index={index} />
    ))}
  </Styled.StyledForeignObject>
);

function propsAreEqual(prev: CustomNodeProps, next: CustomNodeProps) {
  return (
    JSON.stringify(prev.node.text) === JSON.stringify(next.node.text) &&
    prev.node.width === next.node.width
  );
}

export const ObjectNode = React.memo(Node, propsAreEqual);
```

## File: `apps/www/src/features/editor/views/GraphView/CustomNode/styles.tsx`
```tsx
import type { DefaultTheme } from "styled-components";
import styled from "styled-components";
import { LinkItUrl } from "react-linkify-it";
import { NODE_DIMENSIONS } from "../../../../../constants/graph";

type TextColorFn = {
  theme: DefaultTheme;
  $type?: string;
  $value?: string | number | null | boolean;
};

function getTextColor({ $value, $type, theme }: TextColorFn) {
  if ($value === null) return theme.NODE_COLORS.NULL;
  if ($type === "object") return theme.NODE_COLORS.NODE_KEY;
  if ($type === "number") return theme.NODE_COLORS.INTEGER;
  if ($value === true) return theme.NODE_COLORS.BOOL.TRUE;
  if ($value === false) return theme.NODE_COLORS.BOOL.FALSE;
  return theme.NODE_COLORS.NODE_VALUE;
}

export const StyledLinkItUrl = styled(LinkItUrl)`
  text-decoration: underline;
  pointer-events: all;
`;

export const StyledForeignObject = styled.foreignObject<{ $isObject?: boolean }>`
  text-align: ${({ $isObject }) => !$isObject && "center"};
  color: ${({ theme }) => theme.NODE_COLORS.TEXT};
  font-family: monospace;
  font-size: 12px;
  font-weight: 500;
  overflow: hidden;
  pointer-events: none;

  &.searched {
    background: rgba(27, 255, 0, 0.1);
    border: 1px solid ${({ theme }) => theme.TEXT_POSITIVE};
    border-radius: 2px;
    box-sizing: border-box;
  }

  .highlight {
    background: rgba(255, 214, 0, 0.15);
  }

  .renderVisible {
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 12px;
    width: 100%;
    height: 100%;
    overflow: hidden;
    cursor: pointer;
  }
`;

export const StyledKey = styled.span<{
  $type: TextColorFn["$type"];
  $value?: TextColorFn["$value"];
}>`
  display: inline;
  align-items: center;
  justify-content: center;
  flex: 1;
  min-width: 0;
  height: auto;
  line-height: inherit;
  padding: 0; // Remove padding
  color: ${({ theme, $type, $value = "" }) => getTextColor({ $value, $type, theme })};
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
`;

export const StyledRow = styled.span<{ $value: TextColorFn["$value"] }>`
  padding: 3px 10px;
  height: ${NODE_DIMENSIONS.ROW_HEIGHT}px;
  line-height: 24px;
  color: ${({ theme, $value }) => getTextColor({ $value, theme, $type: typeof $value })};
  display: block;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  border-bottom: 1px solid ${({ theme }) => theme.NODE_COLORS.DIVIDER};
  box-sizing: border-box;

  &:last-of-type {
    border-bottom: none;
  }

  .searched & {
    border-bottom: 1px solid ${({ theme }) => theme.TEXT_POSITIVE};
  }
`;

export const StyledChildrenCount = styled.span`
  color: ${({ theme }) => theme.NODE_COLORS.CHILD_COUNT};
  padding: 10px;
  margin-left: -15px;
`;
```

## File: `apps/www/src/features/editor/views/GraphView/CustomNode/TextNode.tsx`
```tsx
import React from "react";
import styled from "styled-components";
import type { CustomNodeProps } from ".";
import { TextRenderer } from "./TextRenderer";
import * as Styled from "./styles";

const StyledTextNodeWrapper = styled.span<{ $isParent: boolean }>`
  display: flex;
  justify-content: ${({ $isParent }) => ($isParent ? "center" : "flex-start")};
  align-items: center;
  height: 100%;
  width: 100%;
  overflow: hidden;
  padding: 0 10px;
`;

const Node = ({ node, x, y }: CustomNodeProps) => {
  const { text, width, height } = node;
  const value = text[0].value;

  return (
    <Styled.StyledForeignObject
      data-id={`node-${node.id}`}
      width={width}
      height={height}
      x={0}
      y={0}
    >
      <StyledTextNodeWrapper
        data-x={x}
        data-y={y}
        data-key={JSON.stringify(text)}
        $isParent={false}
      >
        <Styled.StyledKey $value={value} $type={typeof text[0].value}>
          <TextRenderer>{value}</TextRenderer>
        </Styled.StyledKey>
      </StyledTextNodeWrapper>
    </Styled.StyledForeignObject>
  );
};

function propsAreEqual(prev: CustomNodeProps, next: CustomNodeProps) {
  return prev.node.text === next.node.text && prev.node.width === next.node.width;
}

export const TextNode = React.memo(Node, propsAreEqual);
```

## File: `apps/www/src/features/editor/views/GraphView/CustomNode/TextRenderer.tsx`
```tsx
import React from "react";
import { ColorSwatch } from "@mantine/core";
import styled from "styled-components";

const StyledRow = styled.span`
  display: inline-flex;
  align-items: center;
  overflow: hidden;
  gap: 4px;
  vertical-align: middle;
`;

const isURL = (word: string) => {
  const urlPattern =
    /^(http:\/\/www\.|https:\/\/www\.|http:\/\/|https:\/\/)?[a-z0-9]+([\-\.]{1}[a-z0-9]+)*\.[a-z]{2,5}(:[0-9]{1,5})?(\/.*)?$/gm;

  return word?.match(urlPattern);
};

const Linkify = (text: string) => {
  const addMarkup = (word: string) => {
    return isURL(word)
      ? `<a onclick="event.stopPropagation()" href="${word}" style="text-decoration: underline; pointer-events: all;" target="_blank" rel="noopener noreferrer">${word}</a>`
      : word;
  };

  const words = text.split(" ");
  const formatedWords = words.map(w => addMarkup(w));
  const html = formatedWords.join(" ");
  return <span dangerouslySetInnerHTML={{ __html: html }} />;
};

export const TextRenderer = ({ children }: React.PropsWithChildren) => {
  if (typeof children === "string" && isURL(children)) return Linkify(children);

  if (typeof children === "string" && isColorFormat(children)) {
    return (
      <StyledRow>
        <ColorSwatch size={12} radius={4} mr={4} color={children} />
        {children}
      </StyledRow>
    );
  }

  return <>{`${children}`}</>;
};

function isColorFormat(colorString: string) {
  const hexCodeRegex = /^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$/;
  const rgbRegex = /^rgb\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*\)$/;
  const rgbaRegex = /^rgba\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*,\s*(0|1|0\.\d+)\s*\)$/;

  return (
    hexCodeRegex.test(colorString) || rgbRegex.test(colorString) || rgbaRegex.test(colorString)
  );
}
```

## File: `apps/www/src/features/editor/views/GraphView/lib/jsonParser.ts`
```typescript
/**
 * Copyright (c) JSON Crack
 * This source code is licensed under the Apache 2.0 license found in the
 * LICENSE file in the root directory of this source tree.
 */
import { parseTree, getNodePath, type Node } from "jsonc-parser";
import type { EdgeData, NodeData, NodeRow } from "jsoncrack-react";
import { calculateNodeSize } from "./utils/calculateNodeSize";

export type Graph = {
  nodes: NodeData[];
  edges: EdgeData[];
};

export const parser = (json: string): Graph => {
  const jsonTree = parseTree(json);
  if (!jsonTree) return { nodes: [], edges: [] };

  const nodes: NodeData[] = [];
  const edges: EdgeData[] = [];
  let nodeId = 1;
  let edgeId = 1;

  function traverse(node: Node, parentId?: string) {
    const id = String(nodeId++);
    const text: NodeRow[] = [];

    // If parentId is provided, create an edge from parentId to the current node id
    if (parentId !== undefined && node.parent?.type === "array") {
      edges.push({
        id: String(edgeId++),
        from: parentId,
        to: id,
        text: "",
      });
    }

    const isArray = node.type === "array";
    const isRootArray = !node.parent || node.parent.type === "array";
    if (isArray && isRootArray) {
      const { width, height } = calculateNodeSize(`[${node.children?.length ?? "0"} items]`);
      nodes.push({
        id,
        text: [
          {
            key: null,
            value: `[${node.children?.length ?? 0} items]`,
            type: "array",
            childrenCount: node.children?.length,
          },
        ],
        width,
        height,
        path: [],
      });

      node.children?.forEach(child => {
        traverse(child, id);
      });

      return id;
    }

    node.children?.forEach(child => {
      if (!child.children || !child.children[1]) return traverse(child, id);

      const key = child.children[0].value ?? null;
      const valueNode = child.children[1];
      const type = valueNode.type;

      if (type === "array") {
        const targetIds: string[] = [];

        valueNode.children?.forEach(arrayChild => {
          const arrayChildId = traverse(arrayChild, undefined);
          if (arrayChildId) targetIds.push(arrayChildId);
        });

        text.push({
          key,
          value: valueNode.value,
          type,
          to: targetIds.length > 0 ? targetIds : undefined,
          childrenCount: valueNode.children?.length,
        });

        targetIds.forEach(targetId => {
          edges.push({
            id: String(edgeId++),
            from: id,
            to: targetId,
            text: key ?? null,
          });
        });
      } else if (type === "object") {
        const objectNodeId = traverse(valueNode, id);
        text.push({
          key,
          value: valueNode.value,
          type,
          childrenCount: Object.keys(valueNode.children ?? {}).length,
          ...(objectNodeId && { to: [objectNodeId] }),
        });

        if (objectNodeId) {
          edges.push({
            id: String(edgeId++),
            from: id,
            to: objectNodeId,
            text: key ?? null,
          });
        }
      } else {
        text.push({
          key,
          value: valueNode.value,
          type,
        });
      }
    });

    // to handle case where empty object inside array [{}]
    if (node.parent?.type === "array" && node.type === "object" && node.children?.length === 0) {
      text.push({
        key: null,
        value: "{0 keys}",
        type: "object",
        childrenCount: 0,
      });
    }

    const appendParentKey = () => {
      const getParentKey = (targetNode: any) => {
        const path = getNodePath(targetNode);
        return path?.pop()?.toString();
      };

      if (!node.parent) {
        return { parentKey: getParentKey(node), parentType: node.type };
      }

      if (node.parent.type === "array") {
        return { parentKey: getParentKey(node.parent), parentType: "array" };
      }

      if (node.parent.type === "property") {
        return { parentKey: getParentKey(node), parentType: "object" };
      }

      return {
        parentKey: getParentKey(node),
        parentType: node.parent.type.replace("property", "object"),
      };
    };

    // its for singular text like string, number, boolean, null
    if (text.length === 0) {
      if (typeof node.value === "undefined") return;
      const { width, height } = calculateNodeSize(node.value);

      nodes.push({
        id,
        text: [
          {
            key: null,
            value: node.value,
            type: node.type,
          },
        ],
        width,
        height,
        path: getNodePath(node),
        ...appendParentKey(),
      });
    } else {
      let t: string | [string, string][] = "";

      if (text.some(t => t.key !== null)) {
        t = text.map(t => {
          const keyStr = t.key === null ? "" : t.key;
          if (t.type === "object") return [keyStr, `{${t.childrenCount ?? 0} keys}`];
          if (t.type === "array") return [keyStr, `[${t.childrenCount ?? 0} items]`];
          if (t.value === null) return [keyStr, "null"];

          return [keyStr, `${t.value}`];
        });
      } else {
        t = `${text[0].value}`;
      }

      const { width, height } = calculateNodeSize(t);
      nodes.push({
        id,
        text,
        width,
        height,
        path: getNodePath(node),
        ...appendParentKey(),
      });
    }

    return id; // Return the current id for referencing in the parent node
  }

  traverse(jsonTree);
  return { nodes, edges };
};
```

## File: `apps/www/src/features/editor/views/GraphView/lib/utils/calculateNodeSize.ts`
```typescript
import { NODE_DIMENSIONS } from "../../../../../../constants/graph";

type Text = number | string | [string, string][];
type Size = { width: number; height: number };

const calculateLines = (text: Text): string => {
  if (Array.isArray(text)) {
    return text.map(([k, v]) => `${k}: ${JSON.stringify(v).slice(0, 80)}`).join("\n");
  }

  return `${text}`;
};

const calculateWidthAndHeight = (str: string, single = false) => {
  if (!str) return { width: 45, height: 45 };

  const dummyElement = document.createElement("div");
  dummyElement.style.whiteSpace = single ? "nowrap" : "pre-wrap";
  dummyElement.innerText = str;
  dummyElement.style.fontSize = "12px";
  dummyElement.style.width = "fit-content";
  dummyElement.style.padding = "0 10px";
  dummyElement.style.fontWeight = "500";
  dummyElement.style.fontFamily = "monospace";
  document.body.appendChild(dummyElement);

  const clientRect = dummyElement.getBoundingClientRect();
  const lines = str.split("\n").length;

  const width = clientRect.width + 4;
  // Use parent height for single line nodes that are parents
  const height = single ? NODE_DIMENSIONS.PARENT_HEIGHT : lines * NODE_DIMENSIONS.ROW_HEIGHT;

  document.body.removeChild(dummyElement);
  return { width, height };
};

const sizeCache = new Map<Text, Size>();

// clear cache every 2 mins
setInterval(() => sizeCache.clear(), 120_000);

export const calculateNodeSize = (text: Text, isParent = false) => {
  const cacheKey = [text, isParent].toString();

  // check cache if data already exists
  if (sizeCache.has(cacheKey)) {
    const size = sizeCache.get(cacheKey);
    if (size) return size;
  }

  const lines = calculateLines(text);
  const sizes = calculateWidthAndHeight(lines, typeof text === "string");

  if (isParent) sizes.width += 80;
  if (sizes.width > 700) sizes.width = 700;

  sizeCache.set(cacheKey, sizes);
  return sizes;
};
```

## File: `apps/www/src/features/editor/views/GraphView/lib/utils/getChildrenEdges.ts`
```typescript
import type { EdgeData, NodeData } from "jsoncrack-react";

export const getChildrenEdges = (nodes: NodeData[], edges: EdgeData[]): EdgeData[] => {
  const nodeIds = nodes.map(node => node.id);

  return edges.filter(
    edge => nodeIds.includes(edge.from as string) || nodeIds.includes(edge.to as string)
  );
};
```

## File: `apps/www/src/features/editor/views/GraphView/lib/utils/getOutgoers.ts`
```typescript
import type { EdgeData, NodeData } from "jsoncrack-react";

type Outgoers = [NodeData[], string[]];

export const getOutgoers = (
  nodeId: string,
  nodes: NodeData[],
  edges: EdgeData[],
  parent: string[] = []
): Outgoers => {
  const outgoerNodes: NodeData[] = [];
  const matchingNodes: string[] = [];

  if (parent.includes(nodeId)) {
    const initialParentNode = nodes.find(n => n.id === nodeId);

    if (initialParentNode) outgoerNodes.push(initialParentNode);
  }

  const findOutgoers = (currentNodeId: string) => {
    const outgoerIds = edges.filter(e => e.from === currentNodeId).map(e => e.to);
    const nodeList = nodes.filter(n => {
      if (parent.includes(n.id) && !matchingNodes.includes(n.id)) matchingNodes.push(n.id);
      return outgoerIds.includes(n.id) && !parent.includes(n.id);
    });

    outgoerNodes.push(...nodeList);
    nodeList.forEach(node => findOutgoers(node.id));
  };

  findOutgoers(nodeId);
  return [outgoerNodes, matchingNodes];
};
```

## File: `apps/www/src/features/editor/views/GraphView/stores/useGraph.ts`
```typescript
import type { LayoutDirection, NodeData } from "jsoncrack-react";
import type { ViewPort } from "react-zoomable-ui";
import { create } from "zustand";

export interface Graph {
  viewPort: ViewPort | null;
  direction: LayoutDirection;
  fullscreen: boolean;
  selectedNode: NodeData | null;
}

const initialStates: Graph = {
  viewPort: null,
  direction: "RIGHT",
  fullscreen: false,
  selectedNode: null,
};

interface GraphActions {
  setDirection: (direction: LayoutDirection) => void;
  setViewPort: (ref: ViewPort) => void;
  setSelectedNode: (nodeData: NodeData | null) => void;
  focusFirstNode: () => void;
  toggleFullscreen: (value: boolean) => void;
  zoomIn: () => void;
  zoomOut: () => void;
  centerView: () => void;
}

const useGraph = create<Graph & GraphActions>((set, get) => ({
  ...initialStates,
  setSelectedNode: nodeData => set({ selectedNode: nodeData }),
  setDirection: (direction = "RIGHT") => {
    set({ direction });
    setTimeout(() => get().centerView(), 200);
  },
  focusFirstNode: () => {
    const rootNode = document.querySelector("g[id$='node-1']");
    get().viewPort?.camera?.centerFitElementIntoView(rootNode as HTMLElement, {
      elementExtraMarginForZoom: 100,
    });
  },
  zoomIn: () => {
    const viewPort = get().viewPort;
    viewPort?.camera?.recenter(viewPort.centerX, viewPort.centerY, viewPort.zoomFactor + 0.1);
  },
  zoomOut: () => {
    const viewPort = get().viewPort;
    viewPort?.camera?.recenter(viewPort.centerX, viewPort.centerY, viewPort.zoomFactor - 0.1);
  },
  centerView: () => {
    const viewPort = get().viewPort;
    viewPort?.updateContainerSize();

    const canvas = document.querySelector(".jsoncrack-canvas") as HTMLElement | null;
    if (canvas) {
      viewPort?.camera?.centerFitElementIntoView(canvas);
    }
  },
  toggleFullscreen: fullscreen => set({ fullscreen }),
  setViewPort: viewPort => set({ viewPort }),
}));

export default useGraph;
```

## File: `apps/www/src/features/editor/views/TreeView/index.tsx`
```tsx
import React from "react";
import { useTheme } from "styled-components";
import { JSONTree } from "react-json-tree";
import useJson from "../../../../store/useJson";
import { Label } from "./Label";
import { Value } from "./Value";

export const TreeView = () => {
  const theme = useTheme();
  const json = useJson(state => state.json);

  return (
    <JSONTree
      hideRoot
      data={JSON.parse(json)}
      valueRenderer={(valueAsString, value) => <Value {...{ valueAsString, value }} />}
      labelRenderer={(keyPath, nodeType) => <Label {...{ keyPath, nodeType }} />}
      theme={{
        extend: {
          overflow: "scroll",
          height: "100%",
          scheme: "monokai",
          author: "wimer hazenberg (http://www.monokai.nl)",
          base00: theme.GRID_BG_COLOR,
        },
      }}
    />
  );
};
```

## File: `apps/www/src/features/editor/views/TreeView/Label.tsx`
```tsx
import React from "react";
import type { DefaultTheme } from "styled-components";
import { styled } from "styled-components";
import type { KeyPath } from "react-json-tree";

interface LabelProps {
  keyPath: KeyPath;
  nodeType: string;
}

function getLabelColor({ $type, theme }: { $type?: string; theme: DefaultTheme }) {
  if ($type === "Object") return theme.NODE_COLORS.PARENT_OBJ;
  if ($type === "Array") return theme.NODE_COLORS.PARENT_ARR;
  return theme.NODE_COLORS.PARENT_OBJ;
}

const StyledLabel = styled.span<{ $nodeType?: string }>`
  color: ${({ theme, $nodeType }) => getLabelColor({ theme, $type: $nodeType })};

  &:hover {
    filter: brightness(1.5);
    transition: filter 0.2s ease-in-out;
  }
`;

export const Label = ({ keyPath, nodeType }: LabelProps) => {
  return <StyledLabel $nodeType={nodeType}>{keyPath[0]}:</StyledLabel>;
};
```

## File: `apps/www/src/features/editor/views/TreeView/Value.tsx`
```tsx
import React from "react";
import type { DefaultTheme } from "styled-components";
import { useTheme } from "styled-components";
import { TextRenderer } from "../GraphView/CustomNode/TextRenderer";

type TextColorFn = {
  theme: DefaultTheme;
  $value?: string | unknown;
};

function getValueColor({ $value, theme }: TextColorFn) {
  if ($value && !Number.isNaN(+$value)) return theme.NODE_COLORS.INTEGER;
  if ($value === "true") return theme.NODE_COLORS.BOOL.TRUE;
  if ($value === "false") return theme.NODE_COLORS.BOOL.FALSE;
  if ($value === "null") return theme.NODE_COLORS.NULL;

  // default
  return theme.NODE_COLORS.NODE_VALUE;
}

interface ValueProps {
  valueAsString: unknown;
  value: unknown;
}

export const Value = (props: ValueProps) => {
  const theme = useTheme();
  const { valueAsString, value } = props;

  return (
    <span
      style={{
        color: getValueColor({
          theme,
          $value: valueAsString,
        }),
      }}
    >
      <TextRenderer>{JSON.stringify(value)}</TextRenderer>
    </span>
  );
};
```

## File: `apps/www/src/features/modals/index.ts`
```typescript
export { DownloadModal } from "./DownloadModal";
export { ImportModal } from "./ImportModal";
export { NodeModal } from "./NodeModal";
export { SchemaModal } from "./SchemaModal";
export { JQModal } from "./JQModal";
export { TypeModal } from "./TypeModal";
export { JPathModal } from "./JPathModal";
```

## File: `apps/www/src/features/modals/ModalController.tsx`
```tsx
import React from "react";
import * as ModalComponents from ".";
import { useModal } from "../../store/useModal";
import { modals, type ModalName } from "./modalTypes";

const Modal = ({ modalKey }: { modalKey: ModalName }) => {
  const opened = useModal(state => state[modalKey]);
  const setVisible = useModal(state => state.setVisible);
  const ModalComponent = ModalComponents[modalKey];

  return <ModalComponent opened={opened} onClose={() => setVisible(modalKey, false)} />;
};

const ModalController = () => {
  return modals.map(modal => <Modal key={modal} modalKey={modal} />);
};

export default ModalController;
```

## File: `apps/www/src/features/modals/modalTypes.ts`
```typescript
import * as ModalComponents from ".";

// Define the modals array separate from the component logic
export const modals = Object.freeze(Object.keys(ModalComponents)) as Extract<
  keyof typeof ModalComponents,
  string
>[];

export type ModalName = (typeof modals)[number];
```

## File: `apps/www/src/features/modals/DownloadModal/index.tsx`
```tsx
import React from "react";
import type { ModalProps } from "@mantine/core";
import {
  ColorPicker,
  TextInput,
  SegmentedControl,
  Group,
  Modal,
  Button,
  Divider,
  ColorInput,
} from "@mantine/core";
import { toBlob, toJpeg, toPng, toSvg } from "html-to-image";
import { event as gaEvent } from "nextjs-google-analytics";
import toast from "react-hot-toast";
import { FiCopy, FiDownload } from "react-icons/fi";

enum Extensions {
  SVG = "svg",
  PNG = "png",
  JPEG = "jpeg",
}

const getDownloadFormat = (format: Extensions) => {
  switch (format) {
    case Extensions.SVG:
      return toSvg;
    case Extensions.PNG:
      return toPng;
    case Extensions.JPEG:
      return toJpeg;
  }
};

const swatches = [
  "#B80000",
  "#DB3E00",
  "#FCCB00",
  "#008B02",
  "#006B76",
  "#1273DE",
  "#004DCF",
  "#5300EB",
  "#EB9694",
  "#FAD0C3",
  "#FEF3BD",
  "#C1E1C5",
  "#BEDADC",
  "#C4DEF6",
  "#BED3F3",
  "#D4C4FB",
  "transparent",
];

function downloadURI(uri: string, name: string) {
  const link = document.createElement("a");

  link.download = name;
  link.href = uri;
  document.body.appendChild(link);
  link.click();
  document.body.removeChild(link);
}

const getExportElement = () =>
  (document.querySelector(".jsoncrack-canvas") as HTMLElement | null) ??
  (document.querySelector("svg[id*='ref']") as HTMLElement | null);

export const DownloadModal = ({ opened, onClose }: ModalProps) => {
  const [extension, setExtension] = React.useState(Extensions.PNG);
  const [fileDetails, setFileDetails] = React.useState({
    filename: "jsoncrack.com",
    backgroundColor: "#FFFFFF",
    quality: 1,
  });

  const clipboardImage = async () => {
    try {
      toast.loading("Copying to clipboard...", { id: "toastClipboard" });

      const imageElement = getExportElement();
      if (!imageElement) {
        toast.error("Canvas not found.");
        return;
      }
      const imageOptions = {
        quality: fileDetails.quality,
        backgroundColor: fileDetails.backgroundColor,
        skipFonts: true,
      };

      const blob = await toBlob(imageElement, imageOptions);

      if (!blob) return;

      await navigator.clipboard?.write([
        new ClipboardItem({
          [blob.type]: blob,
        }),
      ]);

      toast.success("Copied to clipboard");
      gaEvent("clipboard_img");
    } catch (error) {
      if (error instanceof Error && error.name === "NotAllowedError") {
        toast.error(
          "Clipboard write permission denied. Please allow clipboard access in your browser settings."
        );
      } else {
        toast.error("Failed to copy to clipboard");
      }
    } finally {
      toast.dismiss("toastClipboard");
      onClose();
    }
  };

  const exportAsImage = async () => {
    try {
      toast.loading("Downloading...", { id: "toastDownload" });

      const imageElement = getExportElement();
      if (!imageElement) {
        toast.error("Canvas not found.");
        return;
      }
      const imageOptions = {
        quality: fileDetails.quality,
        backgroundColor: fileDetails.backgroundColor,
        skipFonts: true,
      };

      const dataURI = await getDownloadFormat(extension)(imageElement, imageOptions);

      downloadURI(dataURI, `${fileDetails.filename}.${extension}`);
      gaEvent("download_img", { label: extension });
    } catch {
      toast.error("Failed to download image!");
    } finally {
      toast.dismiss("toastDownload");
      onClose();
    }
  };

  const updateDetails = (key: keyof typeof fileDetails, value: string | number) =>
    setFileDetails({ ...fileDetails, [key]: value });

  return (
    <Modal opened={opened} onClose={onClose} title="Download Image" centered>
      <TextInput
        label="File Name"
        value={fileDetails.filename}
        onChange={e => updateDetails("filename", e.target.value)}
        mb="lg"
      />
      <SegmentedControl
        value={extension}
        onChange={e => setExtension(e as Extensions)}
        fullWidth
        data={[
          { label: "PNG", value: Extensions.PNG },
          { label: "JPEG", value: Extensions.JPEG },
          { label: "SVG", value: Extensions.SVG },
        ]}
        mb="lg"
      />
      <ColorInput
        label="Background Color"
        value={fileDetails.backgroundColor}
        onChange={color => updateDetails("backgroundColor", color)}
        withEyeDropper={false}
        mb="lg"
      />
      <ColorPicker
        format="rgba"
        value={fileDetails.backgroundColor}
        onChange={color => updateDetails("backgroundColor", color)}
        swatches={swatches}
        withPicker={false}
        fullWidth
      />
      <Divider my="xs" />
      <Group justify="right">
        <Button leftSection={<FiCopy />} onClick={clipboardImage}>
          Clipboard
        </Button>
        <Button color="green" leftSection={<FiDownload />} onClick={exportAsImage}>
          Download
        </Button>
      </Group>
    </Modal>
  );
};
```

## File: `apps/www/src/features/modals/ImportModal/index.tsx`
```tsx
import React from "react";
import type { ModalProps } from "@mantine/core";
import { Modal, Group, Button, TextInput, Stack, Paper, Text } from "@mantine/core";
import { Dropzone } from "@mantine/dropzone";
import { event as gaEvent } from "nextjs-google-analytics";
import toast from "react-hot-toast";
import { AiOutlineUpload } from "react-icons/ai";
import type { FileFormat } from "../../../enums/file.enum";
import useFile from "../../../store/useFile";

export const ImportModal = ({ opened, onClose }: ModalProps) => {
  const [url, setURL] = React.useState("");
  const [file, setFile] = React.useState<File | null>(null);

  const setContents = useFile(state => state.setContents);
  const setFormat = useFile(state => state.setFormat);

  const handleImportFile = () => {
    if (url) {
      setFile(null);

      toast.loading("Loading...", { id: "toastFetch" });
      gaEvent("fetch_url");

      return fetch(url)
        .then(res => res.json())
        .then(json => {
          setContents({ contents: JSON.stringify(json, null, 2) });
          onClose();
        })
        .catch(() => toast.error("Failed to fetch JSON!"))
        .finally(() => toast.dismiss("toastFetch"));
    } else if (file) {
      const lastIndex = file.name.lastIndexOf(".");
      const format = file.name.substring(lastIndex + 1);
      setFormat(format as FileFormat);

      file.text().then(text => {
        setContents({ contents: text });
        setFile(null);
        setURL("");
        onClose();
      });

      gaEvent("import_file", { label: format });
    }
  };

  return (
    <Modal
      title="Import File"
      opened={opened}
      onClose={() => {
        setFile(null);
        setURL("");
        onClose();
      }}
      centered
    >
      <Stack py="sm">
        <TextInput
          value={url}
          onChange={e => setURL(e.target.value)}
          type="url"
          placeholder="URL of JSON to fetch"
          data-autofocus
        />
        <Paper radius="md" style={{ cursor: "pointer" }}>
          <Dropzone
            onDrop={files => setFile(files[0])}
            onReject={files => toast.error(`Unable to load file ${files[0].file.name}`)}
            maxFiles={1}
            p="md"
            accept={["application/json", "application/x-yaml", "text/csv", "application/xml"]}
          >
            <Stack justify="center" align="center" gap="sm" mih={220}>
              <AiOutlineUpload size={48} />
              <Text fw="bold">Drop here or click to upload files</Text>
              <Text c="dimmed" fz="sm">
                {file?.name ?? "None"}
              </Text>
            </Stack>
          </Dropzone>
        </Paper>
      </Stack>
      <Group justify="right">
        <Button onClick={handleImportFile} disabled={!(file || url)}>
          Import
        </Button>
      </Group>
    </Modal>
  );
};
```

## File: `apps/www/src/features/modals/JPathModal/index.tsx`
```tsx
import React from "react";
import type { ModalProps } from "@mantine/core";
import { Stack, Modal, Button, Text, Anchor, Group, TextInput } from "@mantine/core";
import { JSONPath } from "jsonpath-plus";
import { event as gaEvent } from "nextjs-google-analytics";
import toast from "react-hot-toast";
import { VscLinkExternal } from "react-icons/vsc";
import useFile from "../../../store/useFile";
import useJson from "../../../store/useJson";

export const JPathModal = ({ opened, onClose }: ModalProps) => {
  const getJson = useJson(state => state.getJson);
  const setContents = useFile(state => state.setContents);
  const [query, setQuery] = React.useState("");

  const evaluteJsonPath = () => {
    try {
      const json = getJson();
      const result = JSONPath({ path: query, json: JSON.parse(json) });

      setContents({ contents: JSON.stringify(result, null, 2) });
      gaEvent("run_json_path");
      onClose();
    } catch (error) {
      if (error instanceof Error) toast.error(error.message);
    }
  };

  return (
    <Modal title="JSON Path" size="lg" opened={opened} onClose={onClose} centered>
      <Stack>
        <Text fz="sm">
          JsonPath expressions always refer to a JSON structure in the same way as XPath expression
          are used in combination with an XML document. The &quot;root member object&quot; in
          JsonPath is always referred to as $ regardless if it is an object or array.
          <br />
          <Anchor
            fz="sm"
            target="_blank"
            href="https://docs.oracle.com/cd/E60058_01/PDF/8.0.8.x/8.0.8.0.0/PMF_HTML/JsonPath_Expressions.htm"
            rel="noopener noreferrer"
          >
            Read documentation. <VscLinkExternal />
          </Anchor>
        </Text>
        <TextInput
          value={query}
          onChange={e => setQuery(e.currentTarget.value)}
          placeholder="Enter JSON Path..."
          data-autofocus
        />
        <Group justify="right">
          <Button onClick={evaluteJsonPath} disabled={!query.length}>
            Run
          </Button>
        </Group>
      </Stack>
    </Modal>
  );
};
```

## File: `apps/www/src/features/modals/JQModal/index.tsx`
```tsx
import React from "react";
import type { ModalProps } from "@mantine/core";
import { Stack, Modal, Button, Text, Anchor, Group, TextInput } from "@mantine/core";
import { VscLinkExternal } from "react-icons/vsc";
import useJsonQuery from "../../../hooks/useJsonQuery";

export const JQModal = ({ opened, onClose }: ModalProps) => {
  const { updateJson } = useJsonQuery();
  const [query, setQuery] = React.useState("");

  return (
    <Modal title="JSON Query" size="lg" opened={opened} onClose={onClose} centered>
      <Stack>
        <Text fz="sm">
          jq is a lightweight and flexible command-line JSON processor. JSON Crack uses simplified
          version of jq, not all features are supported.
          <br />
          <Anchor
            fz="sm"
            target="_blank"
            href="https://jqlang.github.io/jq/manual/"
            rel="noopener noreferrer"
          >
            Read documentation. <VscLinkExternal />
          </Anchor>
        </Text>
        <TextInput
          leftSection="jq"
          placeholder="Enter jq query"
          value={query}
          onChange={e => setQuery(e.currentTarget.value)}
        />
        <Group justify="right">
          <Button onClick={() => updateJson(query, onClose)}>Display on Graph</Button>
        </Group>
      </Stack>
    </Modal>
  );
};
```

## File: `apps/www/src/features/modals/NodeModal/index.tsx`
```tsx
import React from "react";
import type { ModalProps } from "@mantine/core";
import { Modal, Stack, Text, ScrollArea, Flex, CloseButton } from "@mantine/core";
import { CodeHighlight } from "@mantine/code-highlight";
import type { NodeData } from "jsoncrack-react";
import useGraph from "../../editor/views/GraphView/stores/useGraph";

// return object from json removing array and object fields
const normalizeNodeData = (nodeRows: NodeData["text"]) => {
  if (!nodeRows || nodeRows.length === 0) return "{}";
  if (nodeRows.length === 1 && !nodeRows[0].key) return `${nodeRows[0].value}`;

  const obj = {};
  nodeRows?.forEach(row => {
    if (row.type !== "array" && row.type !== "object") {
      if (row.key) obj[row.key] = row.value;
    }
  });
  return JSON.stringify(obj, null, 2);
};

// return json path in the format $["customer"]
const jsonPathToString = (path?: NodeData["path"]) => {
  if (!path || path.length === 0) return "$";
  const segments = path.map(seg => (typeof seg === "number" ? seg : `"${seg}"`));
  return `$[${segments.join("][")}]`;
};

export const NodeModal = ({ opened, onClose }: ModalProps) => {
  const nodeData = useGraph(state => state.selectedNode);

  return (
    <Modal size="auto" opened={opened} onClose={onClose} centered withCloseButton={false}>
      <Stack pb="sm" gap="sm">
        <Stack gap="xs">
          <Flex justify="space-between" align="center">
            <Text fz="xs" fw={500}>
              Content
            </Text>
            <CloseButton onClick={onClose} />
          </Flex>
          <ScrollArea.Autosize mah={250} maw={600}>
            <CodeHighlight
              code={normalizeNodeData(nodeData?.text ?? [])}
              miw={350}
              maw={600}
              language="json"
              withCopyButton
            />
          </ScrollArea.Autosize>
        </Stack>
        <Text fz="xs" fw={500}>
          JSON Path
        </Text>
        <ScrollArea.Autosize maw={600}>
          <CodeHighlight
            code={jsonPathToString(nodeData?.path)}
            miw={350}
            mah={250}
            language="json"
            copyLabel="Copy to clipboard"
            copiedLabel="Copied to clipboard"
            withCopyButton
          />
        </ScrollArea.Autosize>
      </Stack>
    </Modal>
  );
};
```

## File: `apps/www/src/features/modals/SchemaModal/index.tsx`
```tsx
import React from "react";
import type { ModalProps } from "@mantine/core";
import { Stack, Modal, Button, Text, Anchor, Group, Paper } from "@mantine/core";
import Editor from "@monaco-editor/react";
import { event as gaEvent } from "nextjs-google-analytics";
import { toast } from "react-hot-toast";
import { VscLinkExternal } from "react-icons/vsc";
import useConfig from "../../../store/useConfig";
import useFile from "../../../store/useFile";

export const SchemaModal = ({ opened, onClose }: ModalProps) => {
  const setJsonSchema = useFile(state => state.setJsonSchema);
  const darkmodeEnabled = useConfig(state => (state.darkmodeEnabled ? "vs-dark" : "light"));
  const [schema, setSchema] = React.useState(
    JSON.stringify(
      {
        $schema: "http://json-schema.org/draft-04/schema#",
        title: "Product",
        description: "A product from catalog",
        type: "object",
        properties: {
          id: {
            description: "The unique identifier for a product",
            type: "integer",
          },
        },
        required: ["id"],
      },
      null,
      2
    )
  );

  const onApply = () => {
    try {
      const parsedSchema = JSON.parse(schema);
      setJsonSchema(parsedSchema);

      gaEvent("apply_json_schema");
      toast.success("Applied schema!");
      onClose();
    } catch {
      toast.error("Invalid Schema");
    }
  };

  const onClear = () => {
    setJsonSchema(null);
    setSchema("");
    toast("Disabled JSON Schema");
    onClose();
  };

  return (
    <Modal title="JSON Schema" size="lg" opened={opened} onClose={onClose} centered>
      <Stack>
        <Text fz="sm">Any validation failures are shown at the bottom toolbar of pane.</Text>
        <Anchor
          fz="sm"
          target="_blank"
          href="https://niem.github.io/json/sample-schema/"
          rel="noopener noreferrer"
        >
          View Examples <VscLinkExternal />
        </Anchor>
        <Paper withBorder radius="sm" style={{ overflow: "hidden" }}>
          <Editor
            value={schema ?? ""}
            theme={darkmodeEnabled}
            onChange={e => setSchema(e!)}
            height={300}
            language="json"
            options={{
              formatOnPaste: true,
              tabSize: 2,
              formatOnType: true,
              scrollBeyondLastLine: false,
              stickyScroll: { enabled: false },
              minimap: { enabled: false },
            }}
          />
        </Paper>
        <Group p="0" justify="right">
          <Button variant="subtle" color="gray" onClick={onClear} disabled={!schema}>
            Clear
          </Button>
          <Button variant="default" onClick={onApply} disabled={!schema}>
            Apply
          </Button>
        </Group>
      </Stack>
    </Modal>
  );
};
```

## File: `apps/www/src/features/modals/TypeModal/index.tsx`
```tsx
import React from "react";
import type { ModalProps } from "@mantine/core";
import { Stack, Modal, Select, ScrollArea } from "@mantine/core";
import { CodeHighlight } from "@mantine/code-highlight";
import { event as gaEvent } from "nextjs-google-analytics";
import useJson from "../../../store/useJson";

enum Language {
  TypeScript = "typescript",
  TypeScript_Combined = "typescript/typealias",
  Go = "go",
  JSON_SCHEMA = "json_schema",
  Kotlin = "kotlin",
  Rust = "rust",
}

const typeOptions = [
  {
    label: "TypeScript",
    value: Language.TypeScript,
    lang: "typescript",
  },
  {
    label: "TypeScript (combined)",
    value: Language.TypeScript_Combined,
    lang: "typescript",
  },
  {
    label: "Go",
    value: Language.Go,
    lang: "go",
  },
  {
    label: "JSON Schema",
    value: Language.JSON_SCHEMA,
    lang: "json",
  },
  {
    label: "Kotlin",
    value: Language.Kotlin,
    lang: "kotlin",
  },
  {
    label: "Rust",
    value: Language.Rust,
    lang: "rust",
  },
];

export const TypeModal = ({ opened, onClose }: ModalProps) => {
  const getJson = useJson(state => state.getJson);
  const [type, setType] = React.useState("");
  const [selectedType, setSelectedType] = React.useState<Language>(Language.TypeScript);

  const editorLanguage = React.useMemo(() => {
    return typeOptions[typeOptions.findIndex(o => o.value === selectedType)]?.lang;
  }, [selectedType]);

  const transformer = React.useCallback(
    async ({ value }) => {
      const { run } = await import("json_typegen_wasm");
      return run(
        "Root",
        value,
        JSON.stringify({
          output_mode: selectedType,
        })
      );
    },
    [selectedType]
  );

  React.useEffect(() => {
    if (opened) {
      try {
        if (selectedType === Language.Go) {
          import("../../../lib/utils/json2go").then(jtg => {
            import("gofmt.js").then(gofmt => {
              const types = jtg.default(getJson());
              setType(gofmt.default(types.go));
            });
          });
        } else {
          transformer({ value: getJson() }).then(setType);
        }
      } catch (error) {
        console.error(error);
      }
    }
  }, [getJson, opened, selectedType, transformer]);

  return (
    <Modal title="Generate Types" size="lg" opened={opened} onClose={onClose} centered>
      <Stack pos="relative">
        <Select
          value={selectedType}
          data={typeOptions}
          onChange={e => {
            setSelectedType(e as Language);
            gaEvent("generate_type", { label: e as Language });
          }}
          allowDeselect={false}
        />
        <ScrollArea.Autosize mah={400} maw={700}>
          <CodeHighlight
            language={editorLanguage}
            copyLabel="Copy to clipboard"
            copiedLabel="Copied to clipboard"
            radius={6}
            code={type}
          />
        </ScrollArea.Autosize>
      </Stack>
    </Modal>
  );
};
```

## File: `apps/www/src/hooks/useFocusNode.ts`
```typescript
import React from "react";
import { useDebouncedValue } from "@mantine/hooks";
import { event as gaEvent } from "nextjs-google-analytics";
import useGraph from "../features/editor/views/GraphView/stores/useGraph";
import { cleanupHighlight, searchQuery, highlightMatchedNodes } from "../lib/utils/search";

export const useFocusNode = () => {
  const viewPort = useGraph(state => state.viewPort);
  const [selectedNode, setSelectedNode] = React.useState(0);
  const [nodeCount, setNodeCount] = React.useState(0);
  const [value, setValue] = React.useState("");
  const [debouncedValue] = useDebouncedValue(value, 600);

  const skip = () => setSelectedNode(current => (current + 1) % nodeCount);

  React.useEffect(() => {
    if (!value) {
      cleanupHighlight();
      setSelectedNode(0);
      setNodeCount(0);
      return;
    }

    if (!viewPort || !debouncedValue) return;
    const matchedNodes: NodeListOf<Element> = searchQuery(`span[data-key*='${debouncedValue}' i]`);
    const matchedNode: Element | null = matchedNodes[selectedNode] || null;

    cleanupHighlight();

    if (matchedNode && matchedNode.parentElement) {
      highlightMatchedNodes(matchedNodes, selectedNode);
      setNodeCount(matchedNodes.length);

      viewPort?.camera.centerFitElementIntoView(matchedNode.parentElement, {
        elementExtraMarginForZoom: 400,
      });
    } else {
      setSelectedNode(0);
      setNodeCount(0);
    }

    gaEvent("search_graph");
  }, [selectedNode, debouncedValue, value, viewPort]);

  return [value, setValue, skip, nodeCount, selectedNode] as const;
};
```

## File: `apps/www/src/hooks/useJsonQuery.ts`
```typescript
import toast from "react-hot-toast";
import useFile from "../store/useFile";
import useJson from "../store/useJson";

const useJsonQuery = () => {
  const getJson = useJson(state => state.getJson);
  const setContents = useFile(state => state.setContents);

  const transformer = async ({ value }) => {
    const { run } = await import("json_typegen_wasm");
    return run("Root", value, JSON.stringify({ output_mode: "typescript/typealias" }));
  };

  const updateJson = async (query: string, cb?: () => void) => {
    try {
      const jq = await import("jq-web");
      const res = await jq.promised.json(JSON.parse(getJson()), query);

      setContents({ contents: JSON.stringify(res, null, 2) });
      cb?.();
    } catch (error) {
      console.error(error);
      toast.error("Unable to process the request.");
    }
  };

  const getJsonType = async () => {
    const types = await transformer({ value: getJson() });
    return types;
  };

  return { updateJson, getJsonType };
};

export default useJsonQuery;
```

## File: `apps/www/src/layout/JSONCrackBrandLogo.tsx`
```tsx
import React from "react";
import localFont from "next/font/local";
import Link from "next/link";
import { Image } from "@mantine/core";
import styled from "styled-components";

const monaSans = localFont({
  src: "../assets/fonts/Mona-Sans.woff2",
  variable: "--mona-sans",
  display: "swap",
  fallback: ["Futura, Helvetica, sans-serif", "Tahoma, Verdana, sans-serif"],
});

const StyledLogoWrapper = styled.div`
  display: flex;
  align-items: center;
  gap: 8px;
`;

const StyledTitle = styled.span<{ fontSize: string }>`
  font-weight: 800;
  margin: 0;
  font-family: ${monaSans.style.fontFamily} !important;
  font-size: ${({ fontSize }) => fontSize};
  white-space: nowrap;
  z-index: 10;
  vertical-align: middle;
  color: white;
  mix-blend-mode: difference;
`;

interface LogoProps extends React.ComponentPropsWithoutRef<"div"> {
  fontSize?: string;
  hideLogo?: boolean;
  hideText?: boolean;
}

export const JSONCrackLogo = ({ fontSize = "1.2rem", hideText, hideLogo, ...props }: LogoProps) => {
  const handleLogoClick = React.useCallback((event: React.MouseEvent<HTMLAnchorElement>) => {
    if (typeof window === "undefined") return;
    if (!window.location.href.includes("widget")) return;

    event.preventDefault();
    window.open("/", "_blank", "noopener,noreferrer");
  }, []);

  return (
    <Link href="/" prefetch={false} target="_self" onClick={handleLogoClick}>
      <StyledLogoWrapper>
        {!hideLogo && (
          <Image
            src="/assets/192.png"
            loading="eager"
            width={parseFloat(fontSize) * 18}
            height={parseFloat(fontSize) * 18}
            alt="logo"
            radius={4}
            mb="2"
          />
        )}
        {!hideText && (
          <StyledTitle fontSize={fontSize} {...props}>
            JSON CRACK
          </StyledTitle>
        )}
      </StyledLogoWrapper>
    </Link>
  );
};
```

## File: `apps/www/src/layout/ConverterLayout/options.ts`
```typescript
import type { EditorProps } from "@monaco-editor/react";

export const editorOptions: EditorProps["options"] = {
  formatOnPaste: true,
  formatOnType: true,
  tabSize: 2,
  stopRenderingLineAfter: -1,
  minimap: { enabled: false },
  stickyScroll: { enabled: false },
  scrollBeyondLastLine: false,
};
```

## File: `apps/www/src/layout/ConverterLayout/PageLinks.tsx`
```tsx
import React from "react";
import Link from "next/link";
import { Anchor, Button, Flex, List, SimpleGrid, Stack } from "@mantine/core";
import { FaArrowRightLong } from "react-icons/fa6";
import { formats } from "../../enums/file.enum";

const languages = formats.map(format => format.label);

function groupCombinations(array: string[]): Record<string, string[]> {
  // Create an object to hold the grouped combinations
  const grouped = {};

  // Iterate over each item in the array
  array.forEach(from => {
    // Filter out the same item for the "to" array
    const targets = array.filter(to => to !== from);

    // Add the "from" item as the key and the "to" items as the value array
    grouped[from] = targets;
  });

  return grouped;
}

const groupedLanguages = groupCombinations(languages);

export const PageLinks = () => {
  return (
    <Flex justify="space-between" align="center">
      <Stack gap="sm" py="md" justify="center">
        <Button
          component={Link}
          prefetch={false}
          href="/editor"
          radius="md"
          size="sm"
          color="dark.5"
          autoContrast
          w="fit-content"
          rightSection={<FaArrowRightLong />}
          style={{
            boxShadow: "rgba(0, 0, 0, 0.12) 0px -3px 0px 0px inset",
            border: "none",
          }}
        >
          Open JSON Crack
        </Button>
      </Stack>
      <SimpleGrid cols={4} w="fit-content">
        {Object.entries(groupedLanguages).map(([from, tos]) => (
          <List key={from} listStyleType="none">
            {tos.map(to => (
              <List.Item key={to} c="black">
                <Anchor
                  component={Link}
                  prefetch={false}
                  c="black"
                  href={`/converter/${from.toLowerCase()}-to-${to.toLowerCase()}`}
                >
                  {from} to {to}
                </Anchor>
              </List.Item>
            ))}
          </List>
        ))}
      </SimpleGrid>
    </Flex>
  );
};
```

## File: `apps/www/src/layout/ConverterLayout/ToolPage.tsx`
```tsx
import React, { useEffect, useRef } from "react";
import Head from "next/head";
import { Box, Container, Flex, Paper, Text, Title } from "@mantine/core";
import { Editor } from "@monaco-editor/react";
import { generateNextSeo } from "next-seo/pages";
import { LuCheck, LuCircleX } from "react-icons/lu";
import { SEO } from "../../constants/seo";
import { type FileFormat, formats } from "../../enums/file.enum";
import { contentToJson, jsonToContent } from "../../lib/utils/jsonAdapter";
import Layout from "../PageLayout";
import { PageLinks } from "./PageLinks";
import { editorOptions } from "./options";

interface ToolPageProps {
  from: FileFormat;
  to: FileFormat;
}

export const ToolPage = ({ from, to }: ToolPageProps) => {
  const editorRef = useRef<any>(null);
  const [contentHasError, setContentHasError] = React.useState(false);
  const [originalContent, setOriginalContent] = React.useState("");
  const [convertedContent, setConvertedContent] = React.useState("");
  const [scrollPosition, setScrollPosition] = React.useState(0);
  const [editorHeight, setEditorHeight] = React.useState(0);

  const fromLabel = formats.find(({ value }) => value === from)?.label;
  const toLabel = formats.find(({ value }) => value === to)?.label;

  useEffect(() => {
    if (!originalContent.length) return;

    (async () => {
      try {
        const json = await contentToJson(originalContent, from);
        const content = await jsonToContent(JSON.stringify(json), to);
        setConvertedContent(content);
        setContentHasError(false);
      } catch {
        setContentHasError(true);
        setConvertedContent("");
      }
    })();
  }, [from, originalContent, to]);

  useEffect(() => {
    const scrollPositionRatio =
      (scrollPosition / editorHeight) * (editorRef.current?.getContentHeight() || 0);

    editorRef.current?.setScrollTop(scrollPositionRatio);
  }, [editorHeight, scrollPosition]);

  return (
    <Layout>
      <Head>
        {generateNextSeo({
          ...SEO,
          title: `${fromLabel} to ${toLabel} | JSON Crack`,
          canonical: `https://jsoncrack.com/converter/${from}-to-${to}`,
          description: `Convert ${fromLabel} to ${toLabel} using this free online tool. Upload your ${fromLabel} file and get the converted ${fromLabel} file instantly.`,
        })}
      </Head>
      <Container mt="xl" size="lg">
        <Title c="black">
          {fromLabel} to {toLabel} Converter
        </Title>
        <PageLinks />
        <Flex pt="lg" gap="40">
          <Paper mah="600px" withBorder flex="1" style={{ overflow: "hidden" }}>
            <Box p="xs" bg="gray">
              <Flex justify="space-between" align="center">
                <Text c="gray.3">{fromLabel}</Text>
                {contentHasError && !!originalContent ? (
                  <LuCircleX color="red" />
                ) : (
                  <LuCheck color="lightgreen" />
                )}
              </Flex>
            </Box>
            <Editor
              value={originalContent}
              onChange={value => setOriginalContent(value || "")}
              language={from}
              height={500}
              options={editorOptions}
              onMount={editor => {
                editor.onDidContentSizeChange(() => {
                  setEditorHeight(editor.getContentHeight());
                });

                editor.onDidScrollChange(e => {
                  setScrollPosition(e.scrollTop);
                });
              }}
            />
          </Paper>
          <Paper mah="600px" withBorder flex="1" style={{ overflow: "hidden" }}>
            <Box p="xs" bg="gray">
              <Text c="gray.3">{toLabel}</Text>
            </Box>
            <Editor
              value={convertedContent}
              language={to}
              height={500}
              options={{
                ...editorOptions,
                readOnly: true,
              }}
              onMount={editor => {
                editorRef.current = editor;
              }}
            />
          </Paper>
        </Flex>
      </Container>
    </Layout>
  );
};
```

## File: `apps/www/src/layout/Landing/FAQ.tsx`
```tsx
import React from "react";
import { Container, Title, Accordion } from "@mantine/core";
import Questions from "../../data/faq.json";

export const FAQ = () => {
  return (
    <Container id="faq" component="section" size="sm" py={80}>
      <Title
        c="black"
        order={2}
        fz={{
          base: 24,
          xs: 30,
          sm: 36,
        }}
        fw={600}
        mb={60}
        ta="center"
      >
        Frequently Asked Questions
      </Title>
      <Accordion
        variant="separated"
        styles={{
          panel: {
            background: "#f9f9f9",
            color: "#1d1d1d",
          },
          label: {
            color: "#1d1d1d",
            fontWeight: 500,
          },
          item: {
            background: "#f9f9f9",
            color: "#1d1d1d",
            overflow: "hidden",
            border: "1px solid #ededed",
            borderRadius: 12,
            fontWeight: 300,
          },
        }}
      >
        {Questions.map(({ title, content }) => (
          <Accordion.Item key={title} value={title}>
            <Accordion.Control>{title}</Accordion.Control>
            <Accordion.Panel>{content}</Accordion.Panel>
          </Accordion.Item>
        ))}
      </Accordion>
    </Container>
  );
};
```

## File: `apps/www/src/layout/Landing/Features.tsx`
```tsx
import React from "react";
import {
  Container,
  Flex,
  Title,
  Text,
  Paper,
  Center,
  Badge,
  ThemeIcon,
  SimpleGrid,
} from "@mantine/core";
import { FaBolt, FaToolbox } from "react-icons/fa";
import { IoImages, IoShieldCheckmark } from "react-icons/io5";
import { MdOutlineFormatIndentIncrease, MdOutlineGeneratingTokens } from "react-icons/md";
import { TbTransformFilled } from "react-icons/tb";
import { VscJson } from "react-icons/vsc";

interface FeatureItem {
  title: string;
  description: string;
  icon: React.ReactNode;
  color: string;
}

const features: FeatureItem[] = [
  {
    title: "JSON Visualizer",
    description:
      "Transform your data into interactive graphs or trees as you type. Supports JSON, YAML, CSV, and XML.",
    icon: <FaBolt size={20} />,
    color: "yellow",
  },
  {
    title: "Convert Data",
    description:
      "Convert JSON to CSV, YAML to JSON, XML to JSON, and more. Our JSON converter supports multiple formats for easy data exchange.",
    icon: <TbTransformFilled size={20} />,
    color: "orange",
  },
  {
    title: "JSON Formatter and JSON Validator",
    description:
      "Format and beautify your JSON data to make it more readable. Validate JSON, YAML, and CSV.",
    icon: <MdOutlineFormatIndentIncrease size={20} />,
    color: "green",
  },
  {
    title: "Generate Code/Types",
    description: "Generate TypeScript interface, Golang structs, Rust serde, JSON Schema and more.",
    icon: <MdOutlineGeneratingTokens size={20} />,
    color: "grape",
  },
  {
    title: "JSON Schema Generator",
    description:
      "Validate JSON Schema, create mock data, and generate JSON Schema from various data formats like JSON, YAML, XML, and CSV.",
    icon: <VscJson size={20} />,
    color: "cyan",
  },
  {
    title: "Advanced JSON Tools",
    description: "Decode JWT, randomize data, execute jq (JSON Query), json path commands.",
    icon: <FaToolbox size={20} />,
    color: "teal.5",
  },
  {
    title: "Export Image",
    description:
      "Export image of the graphs as PNG, JPEG, or SVG. Share your data visualization with others.",
    icon: <IoImages size={20} />,
    color: "blue.4",
  },
  {
    title: "Secure",
    description: "Your data is never stored on our servers. Everything happens on your device.",
    icon: <IoShieldCheckmark size={20} />,
    color: "gray",
  },
];

export const Features = () => {
  return (
    <Container component="section" id="features" fluid py={80}>
      <Container size="xl">
        <Center>
          <Badge
            fw="600"
            tt="none"
            variant="outline"
            c="blue.7"
            color="blue.3"
            bg="blue.0"
            size="lg"
          >
            Features
          </Badge>
        </Center>
        <Title
          c="black"
          order={2}
          px="lg"
          fz={{
            base: 26,
            xs: 32,
            sm: 42,
          }}
          fw={600}
          mb={15}
          style={{ textAlign: "center" }}
        >
          Explore Your Data Visually
        </Title>
        <Title
          order={3}
          fw={500}
          c="gray.7"
          px="lg"
          mx="auto"
          ta="center"
          mb={50}
          fz={{ base: 16, sm: 18 }}
          w={{ base: "100%", xs: "80%", sm: "60%", md: "40%" }}
        >
          All in one tool for JSON, YAML, CSV, and XML.
        </Title>

        <SimpleGrid
          cols={{
            base: 1,
            xs: 2,
            md: 4,
          }}
          spacing="xl"
        >
          {features.map((feature, index) => (
            <Paper key={index} bg="gray.0" p="lg" radius="md">
              <Flex gap="sm" align="center" justify="center" direction="column">
                <ThemeIcon radius="xl" size="xl" variant="light" color={feature.color}>
                  {feature.icon}
                </ThemeIcon>
                <Title fw={500} ta="center" c="gray.9" order={3}>
                  {feature.title}
                </Title>
                <Text fz="sm" c="gray.8">
                  {feature.description}
                </Text>
              </Flex>
            </Paper>
          ))}
        </SimpleGrid>
      </Container>
    </Container>
  );
};
```

## File: `apps/www/src/layout/Landing/HeroPreview.tsx`
```tsx
import React from "react";
import { Container, Image } from "@mantine/core";

export const HeroPreview = () => {
  return (
    <Container component="section" id="preview" fluid py="20" mx="lg">
      <Image
        src="./assets/editor.webp"
        loading="eager"
        maw={1036}
        mx="auto"
        alt="JSON Crack editor preview"
        style={{
          borderRadius: 10,
          overflow: "hidden",
          border: "1px solid #c1c1c1",
          outline: "1px solid #c1c1c1",
          outlineOffset: "6px",
        }}
      />
    </Container>
  );
};
```

## File: `apps/www/src/layout/Landing/HeroSection.tsx`
```tsx
import React from "react";
import { Oxygen } from "next/font/google";
import Link from "next/link";
import { Stack, Flex, Button } from "@mantine/core";
import styled from "styled-components";
import { FaChevronRight, FaGithub, FaStar } from "react-icons/fa6";

const oxygen = Oxygen({
  subsets: ["latin-ext"],
  weight: ["700"],
});

const StyledHeroSection = styled.main`
  position: relative;

  &:before {
    position: absolute;
    content: "";
    width: 100%;
    height: 100%;
    background-size: 40px 40px;
    background-image:
      linear-gradient(to right, #f7f7f7 1px, transparent 1px),
      linear-gradient(to bottom, #f7f7f7 1px, transparent 1px);
    image-rendering: pixelated;
    -webkit-mask-image: linear-gradient(to bottom, transparent, 0%, white, 98%, transparent);
    mask-image: linear-gradient(to bottom, transparent, 0%, white, 98%, transparent);
  }

  @media only screen and (max-width: 1240px) {
    flex-direction: column;
  }
`;

const StyledHeroSectionBody = styled.div`
  position: relative;
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: center;
  padding: 6rem 10% 4rem;
  overflow: hidden;
  text-align: center;
  gap: 60px;
  min-height: 40vh;

  @media only screen and (max-width: 768px) {
    padding: 6em 16px;
    padding-top: 10vh;
  }
`;

const StyledHeroTitle = styled.h1`
  position: relative;
  font-size: 2.3rem;
  font-weight: 700;
  display: inline;
  color: #120f43;
  width: fit-content;
  line-height: 1.15;
  max-width: 30rem;
  font-family: ${oxygen.style.fontFamily};

  @media only screen and (min-width: 576px) {
    font-size: 3.4rem;
    max-width: 34rem;
  }

  @media only screen and (min-width: 992px) {
    font-size: 3.8rem;
    max-width: 40rem;
  }

  @media only screen and (min-width: 1400px) {
    font-size: 4.2rem;
    max-width: 50rem;
  }
`;

const StyledHeroText = styled.h2`
  font-size: 14px;
  color: #4a5568;
  font-weight: 400;
  max-width: 75%;
  margin-top: 1rem;
  text-align: center;

  strong {
    font-weight: 400;
    color: #115fe6;
  }

  @media only screen and (min-width: 576px) {
    font-size: 18px;
    max-width: 80%;
  }

  @media only screen and (min-width: 1400px) {
    font-size: 18px;
    max-width: 60%;
  }
`;

export const HeroSection = ({ stars = 0 }) => {
  return (
    <StyledHeroSection>
      <StyledHeroSectionBody>
        <Stack flex="1" miw={250} mx="auto" align="center">
          <Link href="https://github.com/AykutSarac/jsoncrack.com" target="_blank" rel="noopener">
            <Button
              variant="default"
              radius="xl"
              ta="left"
              leftSection={<FaGithub size="18" />}
              rightSection={
                <Flex ml="sm" c="dimmed" align="center" gap="4">
                  <FaStar />
                  {stars.toLocaleString("en-US")}
                </Flex>
              }
            >
              GitHub
            </Button>
          </Link>

          <StyledHeroTitle>Visualize JSON into interactive graphs</StyledHeroTitle>
          <StyledHeroText>
            The best online JSON viewer to <strong>visualize</strong>, <strong>format</strong> and{" "}
            <strong>explore</strong>.
          </StyledHeroText>

          <Flex gap="xs" wrap="wrap" justify="center" hiddenFrom="xs">
            <Button
              component="a"
              color="#202842"
              href="/editor"
              size="md"
              radius="md"
              rightSection={<FaChevronRight />}
              fw="500"
              mt="sm"
            >
              Go to Editor
            </Button>
          </Flex>
          <Flex gap="lg" wrap="wrap" justify="center" visibleFrom="xs">
            <Button
              component="a"
              color="#202842"
              href="/editor"
              size="xl"
              radius="md"
              rightSection={<FaChevronRight />}
              mt="sm"
            >
              Go to Editor
            </Button>
          </Flex>
        </Stack>
      </StyledHeroSectionBody>
    </StyledHeroSection>
  );
};
```

## File: `apps/www/src/layout/Landing/Section1.tsx`
```tsx
import React from "react";
import { Container, Image, SimpleGrid, Stack, Text, Title } from "@mantine/core";
import styled from "styled-components";

const StyledImageWrapper = styled.div`
  position: relative;

  &::after {
    content: "";
    position: absolute;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
    padding: 12px;
    border-radius: 15px;
    border: 1px solid #e0e0e0;
    background: #f3f3f3;
    --line-color-1: #e3e3e3;
    --line-color-2: #e5e5e5;
    background-image:
      linear-gradient(var(--line-color-1) 1.5px, transparent 1.5px),
      linear-gradient(90deg, var(--line-color-1) 1.5px, transparent 1.5px),
      linear-gradient(var(--line-color-2) 1px, transparent 1px),
      linear-gradient(90deg, var(--line-color-2) 1px, transparent 1px);
    background-position:
      -1.5px -1.5px,
      -1.5px -1.5px,
      -1px -1px,
      -1px -1px;
    background-size:
      100px 100px,
      100px 100px,
      20px 20px,
      20px 20px;
  }

  img {
    z-index: 1;
  }
`;

export const Section1 = () => {
  return (
    <Container size="xl" py="80">
      <Title
        lh="1.1"
        fz={{
          base: 26,
          xs: 46,
          sm: 52,
        }}
        maw="16ch"
        ta="center"
        order={2}
        c="gray.9"
        mx="auto"
        mb="15"
      >
        Make working with JSON easy
      </Title>
      <Title
        order={3}
        fw={400}
        c="gray.7"
        px="lg"
        mx="auto"
        ta="center"
        mb={50}
        fz={{ base: 16, sm: 18 }}
        w={{ base: "100%", md: "600" }}
      >
        JSON Crack eliminates the chaos of raw, messy data, making the complex appear simple and
        easy to understand.
      </Title>
      <SimpleGrid
        cols={{
          base: 1,
          sm: 3,
        }}
      >
        <Stack
          p="lg"
          m="lg"
          maw="360"
          mx="auto"
          style={{
            borderRadius: "17px",
            border: "1px solid #e0e0e0",
          }}
        >
          <StyledImageWrapper>
            <Image src="/assets/step1-visual.png" pos="relative" w="100%" alt="upload" />
          </StyledImageWrapper>
          <Title ta="center" c="black" order={3}>
            Upload your data
          </Title>
          <Text ta="center" c="gray.7">
            Upload your JSON file, URL, or type your data directly into our easy-to-use text editor.
          </Text>
        </Stack>
        <Stack
          p="lg"
          m="lg"
          maw="360"
          mx="auto"
          style={{
            borderRadius: "17px",
            border: "1px solid #e0e0e0",
          }}
        >
          <StyledImageWrapper>
            <Image src="/assets/step2-visual.png" pos="relative" w="100%" alt="visualize" />
          </StyledImageWrapper>
          <Title ta="center" c="black" order={3}>
            Visualize your JSON
          </Title>
          <Text ta="center" c="gray.7">
            Your data will automatically be turned into a visual tree graph so you can quickly
            understand your data at a glance.
          </Text>
        </Stack>
        <Stack
          p="lg"
          m="lg"
          maw="360"
          mx="auto"
          style={{
            borderRadius: "17px",
            border: "1px solid #e0e0e0",
          }}
        >
          <StyledImageWrapper>
            <Image src="/assets/step3-visual.png" pos="relative" w="100%" alt="export image" />
          </StyledImageWrapper>
          <Title ta="center" c="black" order={3}>
            Export to image
          </Title>
          <Text ta="center" c="gray.7">
            Once you&apos;re satisfied, you can export an image of your graph as PNG, JPEG, or SVG
            and share with others.
          </Text>
        </Stack>
      </SimpleGrid>
    </Container>
  );
};
```

## File: `apps/www/src/layout/Landing/Section2.tsx`
```tsx
import React from "react";
import {
  Button,
  Container,
  Flex,
  Image,
  JsonInput,
  List,
  SimpleGrid,
  Stack,
  Text,
  Title,
} from "@mantine/core";
import styled from "styled-components";
import { LuBadgeCheck } from "react-icons/lu";

const StyledDottedContainer = styled.div`
  position: relative;
  background-color: #f3f3f3;
  background-image: radial-gradient(#e0e0e0 3px, transparent 0);
  background-size: 40px 40px;
  border: 1px solid #e0e0e0;

  width: 100%;
  min-width: 300px;
  max-width: 500px;
  border-radius: 15px;
  height: 460px;

  .jc {
    position: absolute;
    top: 0;
    left: 0;
    padding: 12px;
    border-radius: 15px;
    transform: translate(-80px, 10%);
    border: 1px solid #000;
    box-shadow: 0px 4px 0px 0px #000;
    background: #f3f3f3;
    --line-color-1: #e3e3e3;
    --line-color-2: #e5e5e5;
    background-image:
      linear-gradient(var(--line-color-1) 1.5px, transparent 1.5px),
      linear-gradient(90deg, var(--line-color-1) 1.5px, transparent 1.5px),
      linear-gradient(var(--line-color-2) 1px, transparent 1px),
      linear-gradient(90deg, var(--line-color-2) 1px, transparent 1px);
    background-position:
      -1.5px -1.5px,
      -1.5px -1.5px,
      -1px -1px,
      -1px -1px;
    background-size:
      100px 100px,
      100px 100px,
      20px 20px,
      20px 20px;
  }

  .jcode {
    position: absolute;
    top: 0;
    left: 0;
    transform: translate(80%, 80%);
    width: 273px;
    border-radius: 15px;
    border: 1px solid #000;
    box-shadow: 0px 4px 0px 0px #000;
    overflow: hidden;
  }

  @media only screen and (max-width: 1085px) {
    display: none;
  }
`;

export const Section2 = () => {
  return (
    <Container size="xl" py="80">
      <Flex justify="center" gap="80" align="center">
        <Stack maw={634}>
          <Title
            lh="1.1"
            fz={{
              base: 26,
              xs: 32,
              sm: 42,
            }}
            maw={500}
            order={2}
            c="gray.9"
          >
            Don&apos;t waste time with JSON formatters
          </Title>
          <Text my="md" c="gray.7" fz={16} maw={510}>
            Format JSON and transform into a readable graph in seconds. JSON Crack is an open-source
            online tool that helps you visualize and understand data.
          </Text>
          <List
            fz={{
              base: 16,
              xs: 18,
            }}
            fw={500}
            component={SimpleGrid}
            c="gray.8"
            icon={<LuBadgeCheck size="20" />}
          >
            <SimpleGrid w="fit-content" cols={2}>
              <List.Item>VS Code Extension</List.Item>
              <List.Item>Open-source</List.Item>
              <List.Item>JSON Validator/Formatter</List.Item>
              <List.Item>Export Image</List.Item>
            </SimpleGrid>
          </List>
          <Button
            component="a"
            href="/editor"
            color="#202842"
            size="lg"
            radius="md"
            w="fit-content"
            mt="sm"
          >
            Open JSON Editor
          </Button>
        </Stack>
        <StyledDottedContainer>
          <Image className="jc" src="/assets/diagram.svg" alt="diagram" loading="lazy" />
          <JsonInput
            w={273}
            rows={12}
            className="jcode"
            styles={{
              input: {
                border: "none",
                fontSize: 12,
              },
            }}
            value={JSON.stringify(
              {
                squadName: "Super hero squad",
                homeTown: "Metro City",
                formed: 2016,
                secretBase: "Super tower",
                active: true,
                members: [
                  {
                    name: "Molecule Man",
                    age: 29,
                    secretIdentity: "Dan Jukes",
                  },
                  {
                    name: "Madame Uppercut",
                    age: 39,
                    secretIdentity: "Jane Wilson",
                  },
                  {
                    name: "Eternal Flame",
                    age: 1000000,
                    secretIdentity: "Unknown",
                  },
                ],
              },
              null,
              2
            )}
          />
        </StyledDottedContainer>
      </Flex>
    </Container>
  );
};
```

## File: `apps/www/src/layout/Landing/Section3.tsx`
```tsx
import React from "react";
import {
  Button,
  Container,
  Flex,
  Image,
  List,
  SimpleGrid,
  Stack,
  Text,
  Title,
} from "@mantine/core";
import styled from "styled-components";
import { LuBadgeCheck } from "react-icons/lu";

const StyledDottedContainer = styled.div`
  position: relative;
  width: 100%;
  min-width: 300px;
  max-width: 500px;
  border-radius: 15px;
  height: 460px;

  .jc {
    position: absolute;
    top: 0;
    left: 0;
    padding: 12px;
    border-radius: 15px;
    border: 1px solid #e0e0e0;
    background: #f3f3f3;
    --line-color-1: #e3e3e3;
    --line-color-2: #e5e5e5;
    background-image:
      linear-gradient(var(--line-color-1) 1.5px, transparent 1.5px),
      linear-gradient(90deg, var(--line-color-1) 1.5px, transparent 1.5px),
      linear-gradient(var(--line-color-2) 1px, transparent 1px),
      linear-gradient(90deg, var(--line-color-2) 1px, transparent 1px);
    background-position:
      -1.5px -1.5px,
      -1.5px -1.5px,
      -1px -1px,
      -1px -1px;
    background-size:
      100px 100px,
      100px 100px,
      20px 20px,
      20px 20px;
  }

  @media only screen and (max-width: 1085px) {
    display: none;
  }
`;

export const Section3 = () => {
  return (
    <Container size="xl" py="80">
      <Flex justify="center" gap="80" align="center">
        <StyledDottedContainer>
          <Image
            className="jc"
            src="/assets/bf2-image.png"
            alt="json, csv, yaml, xml"
            loading="lazy"
          />
        </StyledDottedContainer>
        <Stack maw={634}>
          <Title
            lh="1.1"
            fz={{
              base: 26,
              xs: 32,
              sm: 42,
            }}
            maw={500}
            order={2}
            c="gray.9"
          >
            Visualize and convert to multiple formats
          </Title>
          <Text my="md" c="gray.7" fz={16} maw={510}>
            JSON Crack supports formats like CSV, YAML, and XML, making it easier to visualize your
            data, no matter the type.
          </Text>
          <List
            fz={{
              base: 16,
              xs: 18,
            }}
            fw={500}
            component={SimpleGrid}
            c="gray.8"
            icon={<LuBadgeCheck size="20" />}
          >
            <SimpleGrid w="fit-content" cols={2}>
              <List.Item>JSON to CSV</List.Item>
              <List.Item>YAML to JSON</List.Item>
              <List.Item>XML to JSON</List.Item>
              <List.Item>and more...</List.Item>
            </SimpleGrid>
          </List>
          <Button
            component="a"
            href="/converter/json-to-yaml"
            color="#202842"
            size="lg"
            radius="md"
            w="fit-content"
            mt="sm"
          >
            Open Converter
          </Button>
        </Stack>
      </Flex>
    </Container>
  );
};
```

## File: `apps/www/src/layout/PageLayout/Footer.tsx`
```tsx
import React from "react";
import Link from "next/link";
import { Anchor, Container, Divider, Flex, Stack, Text, ThemeIcon } from "@mantine/core";
import { FaDiscord, FaGithub, FaLinkedin } from "react-icons/fa";
import { FaXTwitter } from "react-icons/fa6";
import { JSONCrackLogo } from "../JSONCrackBrandLogo";

export const Footer = () => {
  return (
    <Container w="100%" mt={60} px={60} pb="xl" bg="black" fluid>
      <Divider color="gray.3" mb="xl" mx={-60} />
      <Flex justify="space-between">
        <Stack gap={4} visibleFrom="sm">
          <JSONCrackLogo />
          <Anchor href="mailto:contact@todiagram.com" fz="xs" c="dimmed">
            contact@todiagram.com
          </Anchor>
        </Stack>
        <Flex gap={60} visibleFrom="sm">
          <Stack gap="xs">
            <Text fz="sm" c="white">
              Product
            </Text>
            <Anchor
              fz="sm"
              c="gray.5"
              href="https://marketplace.visualstudio.com/items?itemName=AykutSarac.jsoncrack-vscode"
              rel="noopener"
            >
              VS Code
            </Anchor>
            <Anchor
              href="https://github.com/AykutSarac/jsoncrack.com"
              fz="sm"
              c="gray.5"
              target="_blank"
              rel="noopener"
            >
              Open Source
            </Anchor>
            <Anchor
              href="https://todiagram.com?utm_source=jsoncrack&utm_medium=footer"
              fz="sm"
              c="gray.5"
              rel="noopener"
            >
              ToDiagram
            </Anchor>
          </Stack>
          <Stack gap="xs">
            <Text fz="sm" c="white">
              Resources
            </Text>
            <Anchor component={Link} prefetch={false} fz="sm" c="gray.5" href="/#faq">
              FAQ
            </Anchor>
            <Anchor component={Link} prefetch={false} fz="sm" c="gray.5" href="/docs">
              Docs
            </Anchor>
          </Stack>
          <Stack gap="xs">
            <Text fz="sm" c="white">
              Social
            </Text>
            <Flex gap="xs">
              <Anchor
                aria-label="LinkedIn"
                href="https://www.linkedin.com/company/jsoncrack"
                fz="sm"
                rel="noopener"
              >
                <ThemeIcon variant="transparent" color="gray.5">
                  <FaLinkedin size={20} />
                </ThemeIcon>
              </Anchor>
              <Anchor aria-label="X" fz="sm" href="https://x.com/jsoncrack" rel="noopener">
                <ThemeIcon variant="transparent" color="gray.5">
                  <FaXTwitter size={20} />
                </ThemeIcon>
              </Anchor>
              <Anchor
                aria-label="GitHub"
                href="https://github.com/AykutSarac/jsoncrack.com"
                fz="sm"
                rel="noopener"
              >
                <ThemeIcon variant="transparent" color="gray.5">
                  <FaGithub size={20} />
                </ThemeIcon>
              </Anchor>
              <Anchor
                aria-label="Discord"
                fz="sm"
                href="https://discord.com/invite/yVyTtCRueq"
                rel="noopener"
              >
                <ThemeIcon variant="transparent" color="gray.5">
                  <FaDiscord size={20} />
                </ThemeIcon>
              </Anchor>
            </Flex>
          </Stack>
        </Flex>
      </Flex>
      <Flex gap="xl">
        <Text fz="sm" c="dimmed">
          © {new Date().getFullYear()} JSON Crack
        </Text>
        <Anchor component={Link} prefetch={false} fz="sm" c="dimmed" href="/legal/terms">
          <Text fz="sm" c="dimmed">
            Terms
          </Text>
        </Anchor>
        <Anchor component={Link} prefetch={false} fz="sm" c="dimmed" href="/legal/privacy">
          <Text fz="sm" c="dimmed">
            Privacy
          </Text>
        </Anchor>
      </Flex>
    </Container>
  );
};
```

## File: `apps/www/src/layout/PageLayout/index.tsx`
```tsx
import React from "react";
import { Inter } from "next/font/google";
import styled, { ThemeProvider } from "styled-components";
import { lightTheme } from "../../constants/theme";
import { Footer } from "./Footer";
import { Navbar } from "./Navbar";

const inter = Inter({
  subsets: ["latin-ext"],
});

const StyledLayoutWrapper = styled.div`
  background: #fff;
  font-family: ${inter.style.fontFamily};
  display: flex;
  flex-direction: column;
  min-height: 100vh;
`;

const ContentWrapper = styled.div`
  flex: 1;
`;

const PageLayout = ({ children }: React.PropsWithChildren) => {
  return (
    <ThemeProvider theme={lightTheme}>
      <StyledLayoutWrapper>
        <Navbar />
        <ContentWrapper>{children}</ContentWrapper>
        <Footer />
      </StyledLayoutWrapper>
    </ThemeProvider>
  );
};

export default PageLayout;
```

## File: `apps/www/src/layout/PageLayout/Navbar.tsx`
```tsx
import React from "react";
import Link from "next/link";
import { Button, Menu, type MenuItemProps, Text, Stack } from "@mantine/core";
import styled from "styled-components";
import { LuChevronDown } from "react-icons/lu";
import { JSONCrackLogo } from "../JSONCrackBrandLogo";

const StyledNavbarWrapper = styled.div`
  z-index: 3;
  transition: background 0.2s ease-in-out;
`;

const StyledMenuItem = styled(Menu.Item)<MenuItemProps & any>`
  color: black;

  &[data-hovered] {
    background-color: #f7f7f7;
  }
`;

const StyledNavbar = styled.nav`
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 100%;
  max-width: 1200px;
  margin: 0 auto;
  padding: 16px 24px;
  background: white;
  backdrop-filter: blur(5px);
  -webkit-backdrop-filter: blur(5px);

  @media only screen and (max-width: 768px) {
    padding: 16px 24px;
  }
`;

const Left = styled.div`
  display: flex;
  align-items: center;
`;

const Right = styled.div`
  display: flex;
  gap: 16px;
  align-items: center;
  white-space: nowrap;
`;

const Center = styled.div`
  display: flex;
  gap: 6px;
  align-items: center;
  white-space: nowrap;
  justify-content: center;

  @media only screen and (max-width: 768px) {
    display: none;
  }
`;

export const Navbar = () => {
  return (
    <StyledNavbarWrapper className="navbar">
      <StyledNavbar>
        <Left>
          <JSONCrackLogo fontSize="1.2rem" />
        </Left>
        <Center>
          <Button
            component="a"
            href="https://marketplace.visualstudio.com/items?itemName=AykutSarac.jsoncrack-vscode"
            target="_blank"
            variant="subtle"
            color="black"
            size="md"
            radius="md"
            rel="noopener"
          >
            VS Code
          </Button>
          <Button
            component={Link}
            prefetch={false}
            href="/docs"
            variant="subtle"
            color="black"
            size="md"
            radius="md"
          >
            Embed
          </Button>
          <Button
            component="a"
            href="https://github.com/AykutSarac/jsoncrack.com"
            target="_blank"
            variant="subtle"
            color="black"
            size="md"
            radius="md"
            rel="noopener"
          >
            Open Source
          </Button>
          <Menu withArrow shadow="sm">
            <Menu.Target>
              <Button
                variant="subtle"
                color="black"
                visibleFrom="sm"
                size="md"
                radius="md"
                rightSection={<LuChevronDown />}
              >
                Tools
              </Button>
            </Menu.Target>
            <Menu.Dropdown maw={300} bg="white">
              <StyledMenuItem component={Link} prefetch={false} href="/converter/json-to-yaml">
                <Stack gap="2">
                  <Text c="black" size="sm" fw={600}>
                    Converter
                  </Text>
                  <Text size="xs" c="gray.6" lineClamp={2}>
                    Convert JSON to YAML, CSV to JSON, YAML to XML, and more.
                  </Text>
                </Stack>
              </StyledMenuItem>
              <StyledMenuItem component={Link} prefetch={false} href="/type/json-to-rust">
                <Stack gap="2">
                  <Text c="black" size="sm" fw={600}>
                    Generate Types
                  </Text>
                  <Text size="xs" c="gray.6" lineClamp={2}>
                    Generate TypeScript types, Golang structs, Rust, and more.
                  </Text>
                </Stack>
              </StyledMenuItem>
              <StyledMenuItem component={Link} prefetch={false} href="/tools/json-schema">
                <Stack gap="2">
                  <Text c="black" size="sm" fw={600}>
                    JSON Schema
                  </Text>
                  <Text size="xs" c="gray.6" lineClamp={2}>
                    Generate JSON schema from JSON data.
                  </Text>
                  <Text size="xs" c="gray.6" lineClamp={2}>
                    Generate JSON data from JSON schema.
                  </Text>
                </Stack>
              </StyledMenuItem>
            </Menu.Dropdown>
          </Menu>
        </Center>
        <Right>
          <Button
            component="a"
            href="https://todiagram.com?utm_source=jsoncrack&utm_medium=navbar"
            variant="subtle"
            color="black"
            size="md"
            radius="md"
            rel="noopener"
          >
            Upgrade
          </Button>
          <Button
            radius="md"
            component="a"
            color="#202842"
            href="/editor"
            visibleFrom="sm"
            size="md"
          >
            Editor
          </Button>
        </Right>
      </StyledNavbar>
    </StyledNavbarWrapper>
  );
};
```

## File: `apps/www/src/layout/TypeLayout/PageLinks.tsx`
```tsx
import React from "react";
import Link from "next/link";
import { Anchor, Button, Flex, List, SimpleGrid, Stack } from "@mantine/core";
import { FaArrowRightLong } from "react-icons/fa6";
import { formats, TypeLanguage, typeOptions } from "../../enums/file.enum";

type MappedCombinations = {
  [language: string]: string[]; // Maps each language to an array of programming languages
};

function mapLanguagesToProgramming(
  languages: string[],
  programmingLanguages: string[]
): MappedCombinations {
  const mappedCombinations: MappedCombinations = {};

  // Iterate over each language
  languages.forEach(language => {
    // Assign the array of programming languages to each language key
    mappedCombinations[language] = programmingLanguages;
  });

  return mappedCombinations;
}

const filterProgrammingLanguages = [TypeLanguage.TypeScript_Combined, TypeLanguage.JSON_SCHEMA];

const languages = formats.map(format => format.label);

const programmingLanguages = typeOptions
  .filter(option => !filterProgrammingLanguages.includes(option.value))
  .map(option => option.label);

const groupedLanguages = mapLanguagesToProgramming(languages, programmingLanguages);

export const PageLinks = () => {
  return (
    <Flex justify="space-between" align="center">
      <Stack gap="sm" py="md" justify="center">
        <Button
          component={Link}
          prefetch={false}
          href="/editor"
          radius="md"
          size="sm"
          color="dark.5"
          autoContrast
          w="fit-content"
          rightSection={<FaArrowRightLong />}
          style={{
            boxShadow: "rgba(0, 0, 0, 0.12) 0px -3px 0px 0px inset",
            border: "none",
          }}
        >
          Open JSON Crack
        </Button>
      </Stack>
      <SimpleGrid cols={4} w="fit-content">
        {Object.entries(groupedLanguages).map(([from, tos]) => (
          <List key={from} listStyleType="none">
            {tos.map(to => (
              <List.Item key={to} c="black">
                <Anchor
                  component={Link}
                  prefetch={false}
                  c="black"
                  href={`/type/${from.toLowerCase()}-to-${to.toLowerCase()}`}
                >
                  {from} to {to}
                </Anchor>
              </List.Item>
            ))}
          </List>
        ))}
      </SimpleGrid>
    </Flex>
  );
};
```

## File: `apps/www/src/layout/TypeLayout/TypegenWrapper.tsx`
```tsx
import React, { useEffect, useRef } from "react";
import Head from "next/head";
import { Box, Container, Flex, Paper, Title, Text } from "@mantine/core";
import { Editor } from "@monaco-editor/react";
import { generateNextSeo } from "next-seo/pages";
import { LuCheck, LuCircleX } from "react-icons/lu";
import { SEO } from "../../constants/seo";
import { type FileFormat, formats, type TypeLanguage, typeOptions } from "../../enums/file.enum";
import { generateType } from "../../lib/utils/generateType";
import { editorOptions } from "../ConverterLayout/options";
import Layout from "../PageLayout";
import { PageLinks } from "./PageLinks";

interface ConverterPagesProps {
  from: FileFormat;
  to: TypeLanguage;
}

export const TypegenWrapper = ({ from, to }: ConverterPagesProps) => {
  const editorRef = useRef<any>(null);
  const [contentHasError, setContentHasError] = React.useState(false);
  const [originalContent, setOriginalContent] = React.useState("");
  const [convertedContent, setConvertedContent] = React.useState("");

  const fromLabel = formats.find(({ value }) => value === from)?.label;
  const toLabel = typeOptions.find(({ value }) => value === to)?.label;

  useEffect(() => {
    if (!originalContent.length) return;

    (async () => {
      try {
        const type = await generateType(originalContent, from, to);
        setConvertedContent(type);
        setContentHasError(false);
      } catch {
        setContentHasError(true);
        setConvertedContent("");
      }
    })();
  }, [from, originalContent, to]);

  return (
    <Layout>
      <Head>
        {generateNextSeo({
          ...SEO,
          title: `${fromLabel} to ${toLabel} | JSON Crack`,
          canonical: `https://jsoncrack.com/converter/${from}-to-${to}`,
          description: `Instantly generate ${toLabel} from ${fromLabel} using this free online tool. Paste your ${fromLabel} and get the generated ${toLabel} instantly.`,
        })}
      </Head>
      <Container mt="xl" size="lg">
        <Title c="black">
          {fromLabel} to {toLabel} Converter
        </Title>
        <PageLinks />
        <Flex pt="lg" gap="40">
          <Paper mah="600px" withBorder flex="1" style={{ overflow: "hidden" }}>
            <Box p="xs" bg="gray">
              <Flex justify="space-between" align="center">
                <Text c="gray.3">{fromLabel}</Text>
                {contentHasError && !!originalContent ? (
                  <LuCircleX color="red" />
                ) : (
                  <LuCheck color="lightgreen" />
                )}
              </Flex>
            </Box>
            <Editor
              value={originalContent}
              onChange={value => setOriginalContent(value || "")}
              language={from}
              height={500}
              options={editorOptions}
            />
          </Paper>
          <Paper mah="600px" withBorder flex="1" style={{ overflow: "hidden" }}>
            <Box p="xs" bg="gray">
              <Text c="gray.3">{toLabel}</Text>
            </Box>
            <Editor
              value={convertedContent}
              language={to}
              height={500}
              options={{
                ...editorOptions,
                readOnly: true,
              }}
              onMount={editor => {
                editorRef.current = editor;
              }}
            />
          </Paper>
        </Flex>
      </Container>
    </Layout>
  );
};
```

## File: `apps/www/src/lib/utils/generateType.ts`
```typescript
import { type FileFormat, TypeLanguage } from "../../enums/file.enum";
import { contentToJson } from "./jsonAdapter";

export const generateType = async (input: string, format: FileFormat, output: TypeLanguage) => {
  try {
    const inputToJson = await contentToJson(input, format);
    const jsonString = JSON.stringify(inputToJson);

    if (output === TypeLanguage.Go) {
      const json2go = await import("./json2go.js");
      const gofmt = await import("gofmt.js");
      const types = json2go.default(jsonString);

      return gofmt.default(types.go);
    } else {
      const { run } = await import("json_typegen_wasm");
      return run("Root", jsonString, JSON.stringify({ output_mode: output }));
    }
  } catch (error) {
    console.error(error);
    return "";
  }
};
```

## File: `apps/www/src/lib/utils/helpers.ts`
```typescript
export function isIframe() {
  try {
    return window.self !== window.top;
  } catch {
    return true;
  }
}
```

## File: `apps/www/src/lib/utils/json2go.js`
```javascript
/*
	JSON-to-Go
	by Matt Holt

	https://github.com/mholt/json-to-go

	A simple utility to translate JSON into a Go type definition.
*/

function jsonToGo(json, typename, flatten = true, example = false, allOmitempty = false) {
  let data;
  let scope;
  let go = "";
  let tabs = 0;

  const seen = {};
  const stack = [];
  let accumulator = "";
  const innerTabs = 0;
  let parent = "";

  try {
    data = JSON.parse(json.replace(/(:\s*\[?\s*-?\d*)\.0/g, "$1.1")); // hack that forces floats to stay as floats
    scope = data;
  } catch (e) {
    return {
      go: "",
      error: e.message,
    };
  }

  typename = format(typename || "Root");
  append(`type ${typename} `);

  parseScope(scope);

  return {
    go: flatten ? (go += accumulator) : go,
  };

  function parseScope(scope, depth = 0) {
    if (typeof scope === "object" && scope !== null) {
      if (Array.isArray(scope)) {
        let sliceType;
        const scopeLength = scope.length;

        for (let i = 0; i < scopeLength; i++) {
          const thisType = goType(scope[i]);
          if (!sliceType) sliceType = thisType;
          else if (sliceType != thisType) {
            sliceType = mostSpecificPossibleGoType(thisType, sliceType);
            if (sliceType == "any") break;
          }
        }

        const slice = flatten && ["struct", "slice"].includes(sliceType) ? `[]${parent}` : "[]";

        if (flatten && depth >= 2) appender(slice);
        else append(slice);
        if (sliceType == "struct") {
          const allFields = {};

          // for each field counts how many times appears
          for (let i = 0; i < scopeLength; i++) {
            const keys = Object.keys(scope[i]);
            for (const k in keys) {
              let keyname = keys[k];
              if (!(keyname in allFields)) {
                allFields[keyname] = {
                  value: scope[i][keyname],
                  count: 0,
                };
              } else {
                const existingValue = allFields[keyname].value;
                const currentValue = scope[i][keyname];

                if (compareObjects(existingValue, currentValue)) {
                  const comparisonResult = compareObjectKeys(
                    Object.keys(currentValue),
                    Object.keys(existingValue)
                  );
                  if (!comparisonResult) {
                    keyname = `${keyname}_${uuidv4()}`;
                    allFields[keyname] = {
                      value: currentValue,
                      count: 0,
                    };
                  }
                }
              }
              allFields[keyname].count++;
            }
          }

          // create a common struct with all fields found in the current array
          // omitempty dict indicates if a field is optional
          const keys = Object.keys(allFields),
            struct = {},
            omitempty = {};
          for (const k in keys) {
            const keyname = keys[k],
              elem = allFields[keyname];

            struct[keyname] = elem.value;
            omitempty[keyname] = elem.count != scopeLength;
          }
          parseStruct(depth + 1, innerTabs, struct, omitempty); // finally parse the struct !!
        } else if (sliceType == "slice") {
          parseScope(scope[0], depth);
        } else {
          if (flatten && depth >= 2) {
            appender(sliceType || "any");
          } else {
            append(sliceType || "any");
          }
        }
      } else {
        if (flatten) {
          if (depth >= 2) {
            appender(parent);
          } else {
            append(parent);
          }
        }
        parseStruct(depth + 1, innerTabs, scope);
      }
    } else {
      if (flatten && depth >= 2) {
        appender(goType(scope));
      } else {
        append(goType(scope));
      }
    }
  }

  function parseStruct(depth, innerTabs, scope, omitempty) {
    if (flatten) {
      stack.push(depth >= 2 ? "\n" : "");
    }

    const seenTypeNames = [];

    if (flatten && depth >= 2) {
      const parentType = `type ${parent}`;
      const scopeKeys = formatScopeKeys(Object.keys(scope));

      // this can only handle two duplicate items
      // future improvement will handle the case where there could
      // three or more duplicate keys with different values
      if (parent in seen && compareObjectKeys(scopeKeys, seen[parent])) {
        stack.pop();
        return;
      }
      seen[parent] = scopeKeys;

      appender(`${parentType} struct {\n`);
      ++innerTabs;
      const keys = Object.keys(scope);
      for (const i in keys) {
        const keyname = getOriginalName(keys[i]);
        indenter(innerTabs);
        const typename = uniqueTypeName(format(keyname), seenTypeNames);
        seenTypeNames.push(typename);

        appender(typename + " ");
        parent = typename;
        parseScope(scope[keys[i]], depth);
        appender(' `json:"' + keyname);
        if (allOmitempty || (omitempty && omitempty[keys[i]] === true)) {
          appender(",omitempty");
        }
        appender('"`\n');
      }
      indenter(--innerTabs);
      appender("}");
    } else {
      append("struct {\n");
      ++tabs;
      const keys = Object.keys(scope);
      for (const i in keys) {
        const keyname = getOriginalName(keys[i]);
        indent(tabs);
        const typename = uniqueTypeName(format(keyname), seenTypeNames);
        seenTypeNames.push(typename);
        append(typename + " ");
        parent = typename;
        parseScope(scope[keys[i]], depth);
        append(' `json:"' + keyname);
        if (allOmitempty || (omitempty && omitempty[keys[i]] === true)) {
          append(",omitempty");
        }
        if (example && scope[keys[i]] !== "" && typeof scope[keys[i]] !== "object") {
          append('" example:"' + scope[keys[i]]);
        }
        append('"`\n');
      }
      indent(--tabs);
      append("}");
    }
    if (flatten) accumulator += stack.pop();
  }

  function indent(tabs) {
    for (let i = 0; i < tabs; i++) go += "\t";
  }

  function append(str) {
    go += str;
  }

  function indenter(tabs) {
    for (let i = 0; i < tabs; i++) stack[stack.length - 1] += "\t";
  }

  function appender(str) {
    stack[stack.length - 1] += str;
  }

  // Generate a unique name to avoid duplicate struct field names.
  // This function appends a number at the end of the field name.
  function uniqueTypeName(name, seen) {
    if (seen.indexOf(name) === -1) {
      return name;
    }

    let i = 0;
    while (true) {
      const newName = name + i.toString();
      if (seen.indexOf(newName) === -1) {
        return newName;
      }

      i++;
    }
  }

  // Sanitizes and formats a string to make an appropriate identifier in Go
  function format(str) {
    str = formatNumber(str);

    const sanitized = toProperCase(str).replace(/[^a-z0-9]/gi, "");
    if (!sanitized) {
      return "NAMING_FAILED";
    }

    // After sanitizing the remaining characters can start with a number.
    // Run the sanitized string again trough formatNumber to make sure the identifier is Num[0-9] or Zero_... instead of 1.
    return formatNumber(sanitized);
  }

  // Adds a prefix to a number to make an appropriate identifier in Go
  function formatNumber(str) {
    if (!str) return "";
    else if (str.match(/^\d+$/)) str = "Num" + str;
    else if (str.charAt(0).match(/\d/)) {
      const numbers = {
        0: "Zero_",
        1: "One_",
        2: "Two_",
        3: "Three_",
        4: "Four_",
        5: "Five_",
        6: "Six_",
        7: "Seven_",
        8: "Eight_",
        9: "Nine_",
      };
      str = numbers[str.charAt(0)] + str.substr(1);
    }

    return str;
  }

  // Determines the most appropriate Go type
  function goType(val) {
    if (val === null) return "any";

    switch (typeof val) {
      case "string":
        if (/\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d(\.\d+)?(\+\d\d:\d\d|Z)/.test(val)) return "time.Time";
        else return "string";
      case "number":
        if (val % 1 === 0) {
          if (val > -2147483648 && val < 2147483647) return "int";
          else return "int64";
        } else return "float64";
      case "boolean":
        return "bool";
      case "object":
        if (Array.isArray(val)) return "slice";
        return "struct";
      default:
        return "any";
    }
  }

  // Given two types, returns the more specific of the two
  function mostSpecificPossibleGoType(typ1, typ2) {
    if (typ1.substr(0, 5) == "float" && typ2.substr(0, 3) == "int") return typ1;
    else if (typ1.substr(0, 3) == "int" && typ2.substr(0, 5) == "float") return typ2;
    else return "any";
  }

  // Proper cases a string according to Go conventions
  function toProperCase(str) {
    // ensure that the SCREAMING_SNAKE_CASE is converted to snake_case
    if (str.match(/^[_A-Z0-9]+$/)) {
      str = str.toLowerCase();
    }

    // https://github.com/golang/lint/blob/5614ed5bae6fb75893070bdc0996a68765fdd275/lint.go#L771-L810
    const commonInitialisms = [
      "ACL",
      "API",
      "ASCII",
      "CPU",
      "CSS",
      "DNS",
      "EOF",
      "GUID",
      "HTML",
      "HTTP",
      "HTTPS",
      "ID",
      "IP",
      "JSON",
      "LHS",
      "QPS",
      "RAM",
      "RHS",
      "RPC",
      "SLA",
      "SMTP",
      "SQL",
      "SSH",
      "TCP",
      "TLS",
      "TTL",
      "UDP",
      "UI",
      "UID",
      "UUID",
      "URI",
      "URL",
      "UTF8",
      "VM",
      "XML",
      "XMPP",
      "XSRF",
      "XSS",
    ];

    return str
      .replace(/(^|[^a-zA-Z])([a-z]+)/g, function (unused, sep, frag) {
        if (commonInitialisms.indexOf(frag.toUpperCase()) >= 0) return sep + frag.toUpperCase();
        else return sep + frag[0].toUpperCase() + frag.substr(1).toLowerCase();
      })
      .replace(/([A-Z])([a-z]+)/g, function (unused, sep, frag) {
        if (commonInitialisms.indexOf(sep + frag.toUpperCase()) >= 0)
          return (sep + frag).toUpperCase();
        else return sep + frag;
      });
  }

  function uuidv4() {
    return "xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx".replace(/[xy]/g, function (c) {
      var r = (Math.random() * 16) | 0,
        v = c == "x" ? r : (r & 0x3) | 0x8;
      return v.toString(16);
    });
  }

  function getOriginalName(unique) {
    const reLiteralUUID =
      /^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$/i;
    const uuidLength = 36;

    if (unique.length >= uuidLength) {
      const tail = unique.substr(-uuidLength);
      if (reLiteralUUID.test(tail)) {
        return unique.slice(0, -1 * (uuidLength + 1));
      }
    }
    return unique;
  }

  function compareObjects(objectA, objectB) {
    const object = "[object Object]";
    return (
      Object.prototype.toString.call(objectA) === object &&
      Object.prototype.toString.call(objectB) === object
    );
  }

  function compareObjectKeys(itemAKeys, itemBKeys) {
    const lengthA = itemAKeys.length;
    const lengthB = itemBKeys.length;

    // nothing to compare, probably identical
    if (lengthA == 0 && lengthB == 0) return true;

    // duh
    if (lengthA != lengthB) return false;

    for (const item of itemAKeys) {
      if (!itemBKeys.includes(item)) return false;
    }
    return true;
  }

  function formatScopeKeys(keys) {
    for (const i in keys) {
      keys[i] = format(keys[i]);
    }
    return keys;
  }
}

if (typeof module != "undefined") {
  module.exports = jsonToGo;
}
```

## File: `apps/www/src/lib/utils/jsonAdapter.ts`
```typescript
import type { ParseError } from "jsonc-parser";
import { FileFormat } from "../../enums/file.enum";

export const contentToJson = (value: string, format = FileFormat.JSON): Promise<object> => {
  return new Promise(async (resolve, reject) => {
    try {
      if (!value) return resolve({});

      if (format === FileFormat.JSON) {
        const { parse } = await import("jsonc-parser");
        const errors: ParseError[] = [];
        const result = parse(value, errors);
        if (errors.length > 0) JSON.parse(value);
        return resolve(result);
      }

      if (format === FileFormat.YAML) {
        const { load } = await import("js-yaml");
        return resolve(load(value) as object);
      }

      if (format === FileFormat.XML) {
        const { XMLParser } = await import("fast-xml-parser");
        const parser = new XMLParser({
          attributeNamePrefix: "$",
          ignoreAttributes: false,
          allowBooleanAttributes: true,
          parseAttributeValue: true,
          trimValues: true,
          parseTagValue: true,
        });
        return resolve(parser.parse(value));
      }

      if (format === FileFormat.CSV) {
        const { csv2json } = await import("json-2-csv");
        const result = csv2json(value, {
          trimFieldValues: true,
          trimHeaderFields: true,
          wrapBooleans: true,
          excelBOM: true,
        });
        return resolve(result);
      }

      return resolve({});
    } catch (error) {
      const errorMessage = error instanceof Error ? error.message : "Failed to parse content";
      return reject(errorMessage);
    }
  });
};

export const jsonToContent = async (json: string, format: FileFormat): Promise<string> => {
  return new Promise(async resolve => {
    try {
      if (!json) return resolve("");

      if (format === FileFormat.JSON) {
        const parsedJson = JSON.parse(json);
        return resolve(JSON.stringify(parsedJson, null, 2));
      }

      if (format === FileFormat.YAML) {
        const { dump } = await import("js-yaml");
        const { parse } = await import("jsonc-parser");
        return resolve(dump(parse(json)));
      }

      if (format === FileFormat.XML) {
        const { XMLBuilder } = await import("fast-xml-parser");
        const builder = new XMLBuilder({
          format: true,
          attributeNamePrefix: "$",
          ignoreAttributes: false,
        });

        return resolve(builder.build(JSON.parse(json)));
      }

      if (format === FileFormat.CSV) {
        const { json2csv } = await import("json-2-csv");
        const parsedJson = JSON.parse(json);

        const data = Array.isArray(parsedJson) ? parsedJson : [parsedJson];
        return resolve(
          json2csv(data, {
            expandArrayObjects: true,
            expandNestedObjects: true,
            excelBOM: true,
            wrapBooleans: true,
            trimFieldValues: true,
            trimHeaderFields: true,
          })
        );
      }

      return resolve(json);
    } catch (error) {
      console.error(json, error);
      return resolve(json);
    }
  });
};
```

## File: `apps/www/src/lib/utils/mantineColorScheme.ts`
```typescript
import { type MantineColorScheme, type MantineColorSchemeManager } from "@mantine/core";

export interface SmartColorSchemeManagerOptions {
  /** Local storage key used to retrieve value with `localStorage.getItem(key)` */
  key: string;
  /** Function that returns the current pathname */
  getPathname: () => string;
  /** Optional list of paths that should use the dynamic color scheme */
  dynamicPaths?: string[];
}

/**
 * Creates a smart color scheme manager that handles different behaviors based on the current path
 * - For editor paths: Uses dynamic behavior with localStorage persistence and per-tab independence
 * - For other paths: Forces light theme
 */
export function smartColorSchemeManager({
  key,
  getPathname,
  dynamicPaths = [],
}: SmartColorSchemeManagerOptions): MantineColorSchemeManager {
  // Keep track of theme in memory for dynamic paths
  let currentColorScheme: MantineColorScheme | null = null;

  // Helper function to check if current path should use dynamic behavior
  const shouldUseDynamicBehavior = () => {
    const pathname = getPathname();
    return dynamicPaths.some(path => pathname === path || pathname.startsWith(`${path}/`));
  };

  return {
    get: defaultValue => {
      // If not in a dynamic path (e.g., editor), always return light theme
      if (!shouldUseDynamicBehavior()) return "light";

      // For dynamic paths, use the stored value (memory first, then localStorage)
      if (currentColorScheme) return currentColorScheme;

      // First time initialization - read from localStorage
      if (typeof window === "undefined") return defaultValue;

      try {
        currentColorScheme =
          (window.localStorage.getItem(key) as MantineColorScheme) || defaultValue;
        return currentColorScheme;
      } catch {
        return defaultValue;
      }
    },

    set: value => {
      // Only store theme for dynamic paths
      if (!shouldUseDynamicBehavior()) return;

      // Update our in-memory value
      currentColorScheme = value;

      // Also save to localStorage
      try {
        window.localStorage.setItem(key, value);
      } catch (error) {
        console.warn("Smart color scheme manager was unable to save color scheme.", error);
      }
    },

    // These do nothing regardless of path
    subscribe: () => {},
    unsubscribe: () => {},
    clear: () => {
      currentColorScheme = null;
      if (typeof window !== "undefined") {
        window.localStorage.removeItem(key);
      }
    },
  };
}
```

## File: `apps/www/src/lib/utils/search.ts`
```typescript
export const searchQuery = (param: string) => {
  return document.querySelectorAll(param);
};

export const cleanupHighlight = () => {
  const nodes = document.querySelectorAll("foreignObject.searched, .highlight");
  for (let i = 0; i < nodes.length; i++) {
    const node = nodes[i];
    node.classList.remove("searched", "highlight");
  }
};

export const highlightMatchedNodes = (nodes: NodeListOf<Element>, selectedNode: number) => {
  for (let i = 0; i < nodes.length; i++) {
    const node = nodes[i];
    const foreignObject = node.parentElement?.closest("foreignObject");
    if (foreignObject) foreignObject.classList.add("searched");
  }

  nodes[selectedNode].classList.add("highlight");
};
```

## File: `apps/www/src/pages/404.tsx`
```tsx
import React from "react";
import Head from "next/head";
import Link from "next/link";
import { Button, Stack, Text, Title } from "@mantine/core";
import { generateNextSeo } from "next-seo/pages";
import { SEO } from "../constants/seo";
import Layout from "../layout/PageLayout";

const NotFound = () => {
  return (
    <Layout>
      <Head>{generateNextSeo({ ...SEO, title: "404 | JSON Crack", noindex: true })}</Head>
      <Stack mt={100} justify="center" align="center">
        <Title fz={150} style={{ fontFamily: "monospace" }}>
          404
        </Title>
        <Title order={2}>Nothing to see here</Title>
        <Text c="dimmed" maw={800} style={{ textAlign: "center" }}>
          Page you are trying to open does not exist. You may have mistyped the address, or the page
          has been moved to another URL. If you think this is an error contact support.
        </Text>
        <Link href="/">
          <Button size="lg" color="gray" type="button">
            Go Home
          </Button>
        </Link>
      </Stack>
    </Layout>
  );
};

export default NotFound;
```

## File: `apps/www/src/pages/docs.tsx`
```tsx
import React from "react";
import Head from "next/head";
import { Group, Paper, Stack, Text, Title } from "@mantine/core";
import { CodeHighlight } from "@mantine/code-highlight";
import styled from "styled-components";
import { generateNextSeo } from "next-seo/pages";
import { SEO } from "../constants/seo";
import Layout from "../layout/PageLayout";

const StyledFrame = styled.iframe`
  border: none;
  width: 80%;
  flex: 500px;
  margin: 3% auto;
`;

const StyledContentBody = styled.div`
  display: flex;
  flex-direction: column;
  flex-wrap: wrap;
  gap: 15px;
  line-height: 1.8;
  overflow-x: auto;
`;

const StyledHighlight = styled.span<{ $link?: boolean; $alert?: boolean }>`
  display: inline-block;
  text-align: left;
  color: ${({ theme, $link, $alert }) =>
    $alert ? theme.DANGER : $link ? theme.BLURPLE : theme.TEXT_POSITIVE};
  background: ${({ theme }) => theme.BACKGROUND_TERTIARY};
  border-radius: 4px;
  font-weight: 500;
  padding: 2px 4px;
  font-size: 14px;
  margin: ${({ $alert }) => ($alert ? "8px 0" : "1px")};
`;

const Docs = () => {
  return (
    <Layout>
      <Head>
        {generateNextSeo({
          ...SEO,
          title: "Documentation - JSON Crack",
          description: "Integrate JSON Crack widgets into your website.",
          canonical: "https://jsoncrack.com/docs",
        })}
      </Head>
      <Stack mx="auto" maw="90%">
        <Group mb="lg" mt={40}>
          <Title order={1} c="dark">
            Embed
          </Title>
        </Group>
        <Paper bg="white" c="black" p="md" radius="md" withBorder>
          <Title mb="sm" order={3} c="dark">
            # Fetching from URL
          </Title>
          <StyledContentBody>
            <Text>
              By adding <StyledHighlight>?json=https://catfact.ninja/fact</StyledHighlight> query at
              the end of iframe src you will be able to fetch from URL at widgets without additional
              scripts. This applies to editor page as well, the following link will fetch the url at
              the editor:{" "}
              <StyledHighlight
                as="a"
                href="https://jsoncrack.com/editor?json=https://catfact.ninja/fact"
                $link
              >
                https://jsoncrack.com/editor?json=https://catfact.ninja/fact
              </StyledHighlight>
            </Text>

            <StyledFrame
              title="Untitled"
              src="https://codepen.io/AykutSarac/embed/KKBpWVR?default-tab=html%2Cresult"
              loading="eager"
            >
              See the Pen <a href="https://codepen.io/AykutSarac/pen/KKBpWVR">Untitled</a> by Aykut
              Saraç (<a href="https://codepen.io/AykutSarac">@AykutSarac</a>) on{" "}
              <a href="https://codepen.io">CodePen</a>.
            </StyledFrame>
          </StyledContentBody>
        </Paper>
        <Paper bg="white" c="black" p="md" radius="md" withBorder>
          <Title mb="sm" order={3} c="dark">
            # Communicating with API
          </Title>
          <Title order={4}>◼︎ Post Message to Embed</Title>
          <StyledContentBody>
            <Text>
              Communicating with the embed is possible with{" "}
              <StyledHighlight
                as="a"
                href="https://developer.mozilla.org/en-US/docs/Web/API/MessagePort/postMessage"
                $link
              >
                MessagePort
              </StyledHighlight>
              , you should pass an object consist of &quot;json&quot; and &quot;options&quot; key
              where json is a string and options is an object that may contain the following:
              <CodeHighlight
                w={500}
                language="json"
                code={
                  '{\n  theme: "light" | "dark",\n  direction: "TOP" | "RIGHT" | "DOWN" | "LEFT"\n}'
                }
                withCopyButton={false}
              />
            </Text>

            <StyledFrame
              scrolling="no"
              title="Untitled"
              src="https://codepen.io/AykutSarac/embed/rNrVyWP?default-tab=html%2Cresult"
              loading="lazy"
            >
              See the Pen <a href="https://codepen.io/AykutSarac/pen/rNrVyWP">Untitled</a> by Aykut
              Saraç (<a href="https://codepen.io/AykutSarac">@AykutSarac</a>) on{" "}
              <a href="https://codepen.io">CodePen</a>.
            </StyledFrame>
          </StyledContentBody>
        </Paper>
        <Paper bg="white" c="black" p="md" radius="md" withBorder>
          <Title order={4}>◼︎ On Page Load</Title>
          <StyledContentBody>
            <Text>
              <Text>
                ⚠️ <b>Important!</b> - iframe should be defined before the script tag
              </Text>
              <Text>
                ⚠️ <b>Note</b> - Widget is not loaded immediately with the parent page. The widget
                sends its <b>id</b> attribute so you can listen for it as in the example below to
                ensure its loaded and ready to listen for messages.
              </Text>
            </Text>
            <StyledFrame
              title="Untitled"
              src="https://codepen.io/AykutSarac/embed/QWBbpqx?default-tab=html%2Cresult"
              loading="lazy"
            >
              See the Pen <a href="https://codepen.io/AykutSarac/pen/QWBbpqx">Untitled</a> by Aykut
              Saraç (<a href="https://codepen.io/AykutSarac">@AykutSarac</a>) on{" "}
              <a href="https://codepen.io">CodePen</a>.
            </StyledFrame>
          </StyledContentBody>
        </Paper>
      </Stack>
    </Layout>
  );
};

export default Docs;
```

## File: `apps/www/src/pages/editor.tsx`
```tsx
import { useEffect } from "react";
import dynamic from "next/dynamic";
import Head from "next/head";
import { useRouter } from "next/router";
import { useMantineColorScheme } from "@mantine/core";
import "@mantine/dropzone/styles.css";
import styled, { ThemeProvider } from "styled-components";
import { Allotment } from "allotment";
import "allotment/dist/style.css";
import { generateNextSeo } from "next-seo/pages";
import { SEO } from "../constants/seo";
import { darkTheme, lightTheme } from "../constants/theme";
import { Banner } from "../features/Banner";
import { BottomBar } from "../features/editor/BottomBar";
import { FullscreenDropzone } from "../features/editor/FullscreenDropzone";
import { Toolbar } from "../features/editor/Toolbar";
import useGraph from "../features/editor/views/GraphView/stores/useGraph";
import useConfig from "../store/useConfig";
import useFile from "../store/useFile";

const ModalController = dynamic(() => import("../features/modals/ModalController"));
const ExternalMode = dynamic(() => import("../features/editor/ExternalMode"));

export const StyledPageWrapper = styled.div`
  display: flex;
  flex-direction: column;
  height: 100vh;
  width: 100%;

  @media only screen and (max-width: 320px) {
    height: 100vh;
  }
`;

export const StyledEditorWrapper = styled.div`
  width: 100%;
  height: 100%;
  overflow: hidden;
`;

export const StyledEditor = styled(Allotment)`
  position: relative !important;
  display: flex;
  background: ${({ theme }) => theme.BACKGROUND_SECONDARY};

  @media only screen and (max-width: 320px) {
    height: 100vh;
  }
`;

const StyledTextEditor = styled.div`
  display: flex;
  flex-direction: column;
  width: 100%;
  height: 100%;
`;

const TextEditor = dynamic(() => import("../features/editor/TextEditor"), {
  ssr: false,
});

const LiveEditor = dynamic(() => import("../features/editor/LiveEditor"), {
  ssr: false,
});

const EditorPage = () => {
  const { query, isReady } = useRouter();
  const { setColorScheme } = useMantineColorScheme();
  const checkEditorSession = useFile(state => state.checkEditorSession);
  const darkmodeEnabled = useConfig(state => state.darkmodeEnabled);
  const fullscreen = useGraph(state => state.fullscreen);

  useEffect(() => {
    if (isReady) checkEditorSession(query?.json);
  }, [checkEditorSession, isReady, query]);

  useEffect(() => {
    setColorScheme(darkmodeEnabled ? "dark" : "light");
  }, [darkmodeEnabled, setColorScheme]);

  return (
    <>
      <Head>
        {generateNextSeo({
          ...SEO,
          title: "Editor | JSON Crack",
          description:
            "JSON Crack Editor is a tool for visualizing into graphs, analyzing, editing, formatting, querying, transforming and validating JSON, CSV, YAML, XML, and more.",
          canonical: "https://jsoncrack.com/editor",
        })}
      </Head>
      <ThemeProvider theme={darkmodeEnabled ? darkTheme : lightTheme}>
        <ExternalMode />
        <ModalController />
        <StyledEditorWrapper>
          <StyledPageWrapper>
            {process.env.NEXT_PUBLIC_DISABLE_EXTERNAL_MODE === "true" ? null : <Banner />}
            <Toolbar />
            <StyledEditorWrapper>
              <StyledEditor proportionalLayout={false}>
                <Allotment.Pane
                  preferredSize={450}
                  minSize={fullscreen ? 0 : 300}
                  maxSize={800}
                  visible={!fullscreen}
                >
                  <StyledTextEditor>
                    <TextEditor />
                    <BottomBar />
                  </StyledTextEditor>
                </Allotment.Pane>
                <Allotment.Pane minSize={0}>
                  <LiveEditor />
                </Allotment.Pane>
              </StyledEditor>
              <FullscreenDropzone />
            </StyledEditorWrapper>
          </StyledPageWrapper>
        </StyledEditorWrapper>
      </ThemeProvider>
    </>
  );
};

export default EditorPage;
```

## File: `apps/www/src/pages/index.tsx`
```tsx
import React from "react";
import type { InferGetStaticPropsType, GetStaticProps } from "next";
import Head from "next/head";
import { generateNextSeo } from "next-seo/pages";
import { SEO } from "../constants/seo";
import { FAQ } from "../layout/Landing/FAQ";
import { Features } from "../layout/Landing/Features";
import { HeroPreview } from "../layout/Landing/HeroPreview";
import { HeroSection } from "../layout/Landing/HeroSection";
import { Section1 } from "../layout/Landing/Section1";
import { Section2 } from "../layout/Landing/Section2";
import { Section3 } from "../layout/Landing/Section3";
import Layout from "../layout/PageLayout";

export const HomePage = (props: InferGetStaticPropsType<typeof getStaticProps>) => {
  return (
    <Layout>
      <Head>{generateNextSeo({ ...SEO, canonical: "https://jsoncrack.com" })}</Head>
      <HeroSection stars={props.stars} />
      <HeroPreview />
      <Section1 />
      <Section2 />
      <Section3 />
      <Features />
      <FAQ />
    </Layout>
  );
};

export default HomePage;

export const getStaticProps = (async () => {
  try {
    const res = await fetch("https://api.github.com/repos/AykutSarac/jsoncrack.com");
    const data = await res.json();

    return {
      props: {
        stars: data?.stargazers_count || 0,
      },
    };
  } catch {
    return {
      props: {
        stars: 0,
      },
    };
  }
}) satisfies GetStaticProps<{ stars: number }>;
```

## File: `apps/www/src/pages/widget.tsx`
```tsx
import React from "react";
import dynamic from "next/dynamic";
import Head from "next/head";
import { useRouter } from "next/router";
import { useMantineColorScheme } from "@mantine/core";
import { ThemeProvider } from "styled-components";
import type { LayoutDirection } from "jsoncrack-react";
import { generateNextSeo } from "next-seo/pages";
import toast from "react-hot-toast";
import { darkTheme, lightTheme } from "../constants/theme";
import useGraph from "../features/editor/views/GraphView/stores/useGraph";
import useFile from "../store/useFile";
import useJson from "../store/useJson";

interface EmbedMessage {
  data: {
    json?: string;
    options?: {
      theme?: "light" | "dark";
      direction?: LayoutDirection;
    };
  };
}

const ModalController = dynamic(() => import("../features/modals/ModalController"), {
  ssr: false,
});

const GraphView = dynamic(
  () => import("../features/editor/views/GraphView").then(c => c.GraphView),
  {
    ssr: false,
  }
);

const WidgetPage = () => {
  const { query, push, isReady } = useRouter();
  const { setColorScheme } = useMantineColorScheme();
  const [theme, setTheme] = React.useState<"dark" | "light">("dark");
  const checkEditorSession = useFile(state => state.checkEditorSession);
  const setContents = useFile(state => state.setContents);
  const setDirection = useGraph(state => state.setDirection);
  const clearJson = useJson(state => state.clear);

  React.useEffect(() => {
    if (isReady) {
      if (typeof query?.json === "string") checkEditorSession(query.json, true);
      else clearJson();

      window.parent.postMessage(window.frameElement?.getAttribute("id"), "*");
    }
  }, [checkEditorSession, clearJson, isReady, push, query.json, query.partner]);

  React.useEffect(() => {
    const handler = (event: EmbedMessage) => {
      try {
        if (!event.data?.json) return;
        if (event.data?.options?.theme === "light" || event.data?.options?.theme === "dark") {
          setTheme(event.data.options.theme);
        }

        setContents({ contents: event.data.json, hasChanges: false });
        setDirection(event.data.options?.direction || "RIGHT");
      } catch (error) {
        console.error(error);
        toast.error("Invalid JSON!");
      }
    };

    window.addEventListener("message", handler);
    return () => window.removeEventListener("message", handler);
  }, [setColorScheme, setContents, setDirection, theme]);

  React.useEffect(() => {
    setColorScheme(theme);
  }, [setColorScheme, theme]);

  return (
    <ThemeProvider theme={theme === "dark" ? darkTheme : lightTheme}>
      <Head>{generateNextSeo({ noindex: true, nofollow: true })}</Head>
      <ModalController />
      <GraphView isWidget />
    </ThemeProvider>
  );
};

export default WidgetPage;
```

## File: `apps/www/src/pages/_app.tsx`
```tsx
import React from "react";
import type { AppProps } from "next/app";
import Head from "next/head";
import { useRouter } from "next/router";
import { createTheme, MantineProvider } from "@mantine/core";
import "@mantine/core/styles.css";
import { CodeHighlightAdapterProvider, createShikiAdapter } from "@mantine/code-highlight";
import "@mantine/code-highlight/styles.css";
import { ThemeProvider } from "styled-components";
import "jsoncrack-react/style.css";
import { SoftwareApplicationJsonLd } from "next-seo";
import { generateDefaultSeo } from "next-seo/pages";
import { GoogleAnalytics } from "nextjs-google-analytics";
import { Toaster } from "react-hot-toast";
import GlobalStyle from "../constants/globalStyle";
import { SEO } from "../constants/seo";
import { lightTheme } from "../constants/theme";
import { smartColorSchemeManager } from "../lib/utils/mantineColorScheme";

async function loadShiki() {
  const { createHighlighter } = await import("shiki");
  const shiki = await createHighlighter({
    langs: ["typescript", "json", "go", "kotlin", "rust"],
    themes: [],
  });

  return shiki;
}

const shikiAdapter = createShikiAdapter(loadShiki);

const theme = createTheme({
  autoContrast: true,
  fontSmoothing: false,
  respectReducedMotion: true,
  cursorType: "pointer",
  fontFamily:
    'system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,"Noto Sans",sans-serif,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol","Noto Color Emoji"',
  defaultGradient: {
    from: "#388cdb",
    to: "#0f037f",
    deg: 180,
  },
  primaryShade: 8,
  colors: {
    brightBlue: [
      "#e6f2ff",
      "#cee1ff",
      "#9bc0ff",
      "#649dff",
      "#3980fe",
      "#1d6dfe",
      "#0964ff",
      "#0054e4",
      "#004acc",
      "#003fb5",
    ],
  },
  radius: {
    lg: "12px",
  },
  components: {
    Button: {
      defaultProps: {
        fw: 500,
      },
    },
  },
});

function JSONCrackApp({ Component, pageProps }: AppProps) {
  const { pathname } = useRouter();

  // Create a single smart manager that handles pathname logic internally
  const colorSchemeManager = smartColorSchemeManager({
    key: "editor-color-scheme",
    getPathname: () => pathname,
    dynamicPaths: ["/editor"], // Only editor paths use dynamic theme
  });

  return (
    <>
      <Head>{generateDefaultSeo(SEO)}</Head>
      <SoftwareApplicationJsonLd
        name="JSON Crack"
        type="SoftwareApplication"
        operatingSystem="Browser"
        applicationCategory="DeveloperApplication"
        aggregateRating={{ ratingValue: 4.9, ratingCount: 19 }}
        datePublished="2022-17-02"
      />
      <MantineProvider
        colorSchemeManager={colorSchemeManager}
        defaultColorScheme="light"
        theme={theme}
      >
        <CodeHighlightAdapterProvider adapter={shikiAdapter}>
          <ThemeProvider theme={lightTheme}>
            <Toaster
              position="bottom-right"
              containerStyle={{
                bottom: 34,
                right: 8,
                fontSize: 14,
              }}
              toastOptions={{
                style: {
                  background: "#4D4D4D",
                  color: "#B9BBBE",
                  borderRadius: 4,
                },
              }}
            />
            <GlobalStyle />
            {process.env.NEXT_PUBLIC_GA_MEASUREMENT_ID && <GoogleAnalytics trackPageViews />}
            <Component {...pageProps} />
          </ThemeProvider>
        </CodeHighlightAdapterProvider>
      </MantineProvider>
    </>
  );
}

export default JSONCrackApp;
```

## File: `apps/www/src/pages/_document.tsx`
```tsx
import type { DocumentContext, DocumentInitialProps } from "next/document";
import Document, { Html, Head, Main, NextScript } from "next/document";
import { ColorSchemeScript } from "@mantine/core";
import { ServerStyleSheet } from "styled-components";

class MyDocument extends Document {
  static async getInitialProps(ctx: DocumentContext): Promise<DocumentInitialProps> {
    const sheet = new ServerStyleSheet();
    const originalRenderPage = ctx.renderPage;

    try {
      ctx.renderPage = () =>
        originalRenderPage({
          enhanceApp: App => props => sheet.collectStyles(<App {...props} />),
        });

      const initialProps = await Document.getInitialProps(ctx);

      return {
        ...initialProps,
        styles: (
          <>
            {initialProps.styles}
            {sheet.getStyleElement()}
          </>
        ),
      };
    } finally {
      sheet.seal();
    }
  }

  render() {
    return (
      <Html lang="en">
        <Head>
          <ColorSchemeScript />
        </Head>
        <body>
          <Main />
          <NextScript />
        </body>
      </Html>
    );
  }
}

export default MyDocument;
```

## File: `apps/www/src/pages/_error.tsx`
```tsx
import React from "react";
import Head from "next/head";
import { useRouter } from "next/router";
import { Button, Stack, Text, Title } from "@mantine/core";
import { generateNextSeo } from "next-seo/pages";
import { SEO } from "../constants/seo";
import Layout from "../layout/PageLayout";

const Custom500 = () => {
  const router = useRouter();

  return (
    <Layout>
      <Head>
        {generateNextSeo({
          ...SEO,
          title: "Unexpected Error Occurred | JSON Crack",
        })}
      </Head>
      <Stack mt={100} justify="center" align="center">
        <Title fz={150} style={{ fontFamily: "monospace" }}>
          500
        </Title>
        <Title order={2}>Something bad just happened...</Title>
        <Text c="dimmed" maw={800} style={{ textAlign: "center" }}>
          Our servers could not handle your request. Don&apos;t worry, our development team was
          already notified. Try refreshing the page.
        </Text>
        <Button size="lg" color="gray" type="button" onClick={() => router.reload()}>
          Refresh the page
        </Button>
      </Stack>
    </Layout>
  );
};

export default Custom500;
```

## File: `apps/www/src/pages/converter/csv-to-json.tsx`
```tsx
import React from "react";
import { FileFormat } from "../../enums/file.enum";
import { ToolPage } from "../../layout/ConverterLayout/ToolPage";

const Page = () => {
  return <ToolPage from={FileFormat.CSV} to={FileFormat.JSON} />;
};

export default Page;
```

## File: `apps/www/src/pages/converter/csv-to-xml.tsx`
```tsx
import React from "react";
import { FileFormat } from "../../enums/file.enum";
import { ToolPage } from "../../layout/ConverterLayout/ToolPage";

const Page = () => {
  return <ToolPage from={FileFormat.CSV} to={FileFormat.XML} />;
};

export default Page;
```

## File: `apps/www/src/pages/converter/csv-to-yaml.tsx`
```tsx
import React from "react";
import { FileFormat } from "../../enums/file.enum";
import { ToolPage } from "../../layout/ConverterLayout/ToolPage";

const Page = () => {
  return <ToolPage from={FileFormat.CSV} to={FileFormat.YAML} />;
};

export default Page;
```

## File: `apps/www/src/pages/converter/json-to-csv.tsx`
```tsx
import React from "react";
import { FileFormat } from "../../enums/file.enum";
import { ToolPage } from "../../layout/ConverterLayout/ToolPage";

const Page = () => {
  return <ToolPage from={FileFormat.JSON} to={FileFormat.CSV} />;
};

export default Page;
```

## File: `apps/www/src/pages/converter/json-to-xml.tsx`
```tsx
import React from "react";
import { FileFormat } from "../../enums/file.enum";
import { ToolPage } from "../../layout/ConverterLayout/ToolPage";

const Page = () => {
  return <ToolPage from={FileFormat.JSON} to={FileFormat.XML} />;
};

export default Page;
```

## File: `apps/www/src/pages/converter/json-to-yaml.tsx`
```tsx
import React from "react";
import { FileFormat } from "../../enums/file.enum";
import { ToolPage } from "../../layout/ConverterLayout/ToolPage";

const Page = () => {
  return <ToolPage from={FileFormat.JSON} to={FileFormat.YAML} />;
};

export default Page;
```

## File: `apps/www/src/pages/converter/xml-to-csv.tsx`
```tsx
import React from "react";
import { FileFormat } from "../../enums/file.enum";
import { ToolPage } from "../../layout/ConverterLayout/ToolPage";

const Page = () => {
  return <ToolPage from={FileFormat.XML} to={FileFormat.CSV} />;
};

export default Page;
```

## File: `apps/www/src/pages/converter/xml-to-json.tsx`
```tsx
import React from "react";
import { FileFormat } from "../../enums/file.enum";
import { ToolPage } from "../../layout/ConverterLayout/ToolPage";

const Page = () => {
  return <ToolPage from={FileFormat.XML} to={FileFormat.JSON} />;
};

export default Page;
```

## File: `apps/www/src/pages/converter/xml-to-yaml.tsx`
```tsx
import React from "react";
import { FileFormat } from "../../enums/file.enum";
import { ToolPage } from "../../layout/ConverterLayout/ToolPage";

const Page = () => {
  return <ToolPage from={FileFormat.XML} to={FileFormat.YAML} />;
};

export default Page;
```

## File: `apps/www/src/pages/converter/yaml-to-csv.tsx`
```tsx
import React from "react";
import { FileFormat } from "../../enums/file.enum";
import { ToolPage } from "../../layout/ConverterLayout/ToolPage";

const Page = () => {
  return <ToolPage from={FileFormat.YAML} to={FileFormat.CSV} />;
};

export default Page;
```

## File: `apps/www/src/pages/converter/yaml-to-json.tsx`
```tsx
import React from "react";
import { FileFormat } from "../../enums/file.enum";
import { ToolPage } from "../../layout/ConverterLayout/ToolPage";

const Page = () => {
  return <ToolPage from={FileFormat.YAML} to={FileFormat.JSON} />;
};

export default Page;
```

## File: `apps/www/src/pages/converter/yaml-to-xml.tsx`
```tsx
import React from "react";
import { FileFormat } from "../../enums/file.enum";
import { ToolPage } from "../../layout/ConverterLayout/ToolPage";

const Page = () => {
  return <ToolPage from={FileFormat.YAML} to={FileFormat.XML} />;
};

export default Page;
```

## File: `apps/www/src/pages/legal/privacy.tsx`
```tsx
import React from "react";
import Head from "next/head";
import { Box, Container, Paper, Stack, Text, Title } from "@mantine/core";
import { generateNextSeo } from "next-seo/pages";
import { SEO } from "../../constants/seo";
import privacy from "../../data/privacy.json";
import Layout from "../../layout/PageLayout";

const Privacy = () => {
  return (
    <Layout>
      <Head>
        {generateNextSeo({
          ...SEO,
          title: "Privacy Policy - JSON Crack",
          description: "JSON Crack Privacy Policy",
          canonical: "https://jsoncrack.com/legal/privacy",
        })}
      </Head>
      <Container my={50} size="md" pb="lg">
        <Paper bg="transparent">
          <Title ta="center" c="gray.8">
            Privacy Policy
          </Title>
          <Text c="gray.6" ta="center">
            Last updated: Feb 5, 2025
          </Text>

          <Stack mt={50} my="lg">
            {Object.keys(privacy).map((term, index) => (
              <Box component="section" mt="xl" key={index}>
                <Title order={2} mb="xl" c="gray.8">
                  {term}
                </Title>
                {privacy[term].map(term => (
                  <Text mt="md" c="gray.8" key={term} ml={term.startsWith("•") ? 15 : 0}>
                    {term}
                  </Text>
                ))}
              </Box>
            ))}
          </Stack>
        </Paper>
      </Container>
    </Layout>
  );
};

export default Privacy;
```

## File: `apps/www/src/pages/legal/terms.tsx`
```tsx
import React from "react";
import Head from "next/head";
import { Box, Container, Paper, Stack, Text, Title } from "@mantine/core";
import { generateNextSeo } from "next-seo/pages";
import { SEO } from "../../constants/seo";
import terms from "../../data/terms.json";
import Layout from "../../layout/PageLayout";

const Terms = () => {
  return (
    <Layout>
      <Head>
        {generateNextSeo({
          ...SEO,
          title: "Terms of Service - JSON Crack",
          description: "JSON Crack Terms of Service",
          canonical: "https://jsoncrack.com/legal/terms",
        })}
      </Head>
      <Container my={50} size="md" pb="lg">
        <Paper bg="transparent">
          <Title ta="center" c="gray.8">
            Terms of Service
          </Title>
          <Text c="gray.6" ta="center">
            Last updated: No 30, 2024
          </Text>

          <Stack mt={50} my="lg">
            {Object.keys(terms).map((term, index) => (
              <Box component="section" mt="xl" key={index}>
                <Title order={2} mb="xl" c="gray.8">
                  {term}
                </Title>
                {terms[term].map(term => (
                  <Text mt="md" c="gray.8" key={term} ml={term.startsWith("•") ? 15 : 0}>
                    {term}
                  </Text>
                ))}
              </Box>
            ))}
          </Stack>
        </Paper>
      </Container>
    </Layout>
  );
};

export default Terms;
```

## File: `apps/www/src/pages/tools/json-schema.tsx`
```tsx
import React from "react";
import Head from "next/head";
import { Box, Button, Container, Flex, Paper, Title, Text } from "@mantine/core";
import { Editor, type OnMount } from "@monaco-editor/react";
import { JSONSchemaFaker } from "json-schema-faker";
import { generateNextSeo } from "next-seo/pages";
import { LuCheck, LuCircleX } from "react-icons/lu";
import { SEO } from "../../constants/seo";
import { FileFormat, TypeLanguage } from "../../enums/file.enum";
import { editorOptions } from "../../layout/ConverterLayout/options";
import Layout from "../../layout/PageLayout";
import { generateType } from "../../lib/utils/generateType";
import { jsonToContent } from "../../lib/utils/jsonAdapter";

const JSONSchemaTool = () => {
  const monacoRef = React.useRef<Parameters<OnMount>[1] | null>(null);
  const [jsonError, setJsonError] = React.useState(false);
  const [jsonSchemaError, setJsonSchemaError] = React.useState(false);
  const [json, setJson] = React.useState("");
  const [jsonSchema, setJsonSchema] = React.useState("");

  React.useEffect(() => {
    monacoRef.current?.languages.json.jsonDefaults.setDiagnosticsOptions({
      validate: true,
      allowComments: true,
      enableSchemaRequest: true,
      ...(jsonSchema && {
        schemas: [
          {
            uri: "",
            fileMatch: ["*"],
            schema: jsonSchema,
          },
        ],
      }),
    });
  }, [jsonSchema]);

  const generateJsonSchema = async () => {
    const jsonSchema = await generateType(json, FileFormat.JSON, TypeLanguage.JSON_SCHEMA);
    setJsonSchema(jsonSchema);
  };

  const generateJson = async () => {
    const randomJson = await JSONSchemaFaker.resolve(JSON.parse(jsonSchema));
    const contents = await jsonToContent(JSON.stringify(randomJson, null, 2), FileFormat.JSON);
    setJson(contents);
  };

  return (
    <Layout>
      <Head>
        {generateNextSeo({
          ...SEO,
          title: "JSON Schema Validator & Generator",
          description:
            "Use our JSON Schema Validator & Generator tool to easily validate and generate JSON schemas, and generate data from JSON schemas. Simply input your JSON data, generate the corresponding schema, and validate your data with ease.",
          canonical: "https://jsoncrack.com/tools/json-schema",
        })}
      </Head>
      <Container mt="xl" size="xl">
        <Title c="black">JSON Schema Validator & Generator</Title>
        <Flex pt="lg" gap="lg">
          <Button
            onClick={generateJsonSchema}
            variant="default"
            size="md"
            disabled={!json.length || jsonError}
          >
            Generate JSON Schema
          </Button>
          <Button
            onClick={generateJson}
            variant="default"
            size="md"
            disabled={!jsonSchema.length || jsonSchemaError}
          >
            Generate JSON
          </Button>
        </Flex>
        <Flex pt="lg" gap="40">
          <Paper mah="600px" withBorder flex="1" style={{ overflow: "hidden" }}>
            <Box p="xs" bg="gray">
              <Flex justify="space-between" align="center">
                <Text c="gray.3">JSON</Text>
                {jsonError ? <LuCircleX color="red" /> : <LuCheck color="lightgreen" />}
              </Flex>
            </Box>
            <Editor
              value={json}
              onChange={value => setJson(value || "")}
              onValidate={errors => setJsonError(!!errors.length)}
              language="json"
              height={500}
              options={editorOptions}
              onMount={(_editor, monaco) => (monacoRef.current = monaco)}
            />
          </Paper>
          <Paper mah="600px" withBorder flex="1" style={{ overflow: "hidden" }}>
            <Box p="xs" bg="gray">
              <Flex justify="space-between" align="center">
                <Text c="gray.3">JSON Schema</Text>
                {jsonSchemaError ? <LuCircleX color="red" /> : <LuCheck color="lightgreen" />}
              </Flex>
            </Box>
            <Editor
              value={jsonSchema}
              onChange={value => setJsonSchema(value || "")}
              onValidate={errors => setJsonSchemaError(!!errors.length)}
              language="json"
              height={500}
              options={editorOptions}
            />
          </Paper>
        </Flex>
      </Container>
    </Layout>
  );
};

export default JSONSchemaTool;
```

## File: `apps/www/src/pages/type/csv-to-go.tsx`
```tsx
import React from "react";
import { FileFormat, TypeLanguage } from "../../enums/file.enum";
import { TypegenWrapper } from "../../layout/TypeLayout/TypegenWrapper";

const TypePage = () => {
  return <TypegenWrapper from={FileFormat.CSV} to={TypeLanguage.Go} />;
};

export default TypePage;
```

## File: `apps/www/src/pages/type/csv-to-kotlin.tsx`
```tsx
import React from "react";
import { FileFormat, TypeLanguage } from "../../enums/file.enum";
import { TypegenWrapper } from "../../layout/TypeLayout/TypegenWrapper";

const TypePage = () => {
  return <TypegenWrapper from={FileFormat.CSV} to={TypeLanguage.Kotlin} />;
};

export default TypePage;
```

## File: `apps/www/src/pages/type/csv-to-rust.tsx`
```tsx
import React from "react";
import { FileFormat, TypeLanguage } from "../../enums/file.enum";
import { TypegenWrapper } from "../../layout/TypeLayout/TypegenWrapper";

const TypePage = () => {
  return <TypegenWrapper from={FileFormat.CSV} to={TypeLanguage.Rust} />;
};

export default TypePage;
```

## File: `apps/www/src/pages/type/csv-to-typescript.tsx`
```tsx
import React from "react";
import { FileFormat, TypeLanguage } from "../../enums/file.enum";
import { TypegenWrapper } from "../../layout/TypeLayout/TypegenWrapper";

const TypePage = () => {
  return <TypegenWrapper from={FileFormat.CSV} to={TypeLanguage.TypeScript} />;
};

export default TypePage;
```

## File: `apps/www/src/pages/type/json-to-go.tsx`
```tsx
import React from "react";
import { FileFormat, TypeLanguage } from "../../enums/file.enum";
import { TypegenWrapper } from "../../layout/TypeLayout/TypegenWrapper";

const TypePage = () => {
  return <TypegenWrapper from={FileFormat.JSON} to={TypeLanguage.Go} />;
};

export default TypePage;
```

## File: `apps/www/src/pages/type/json-to-kotlin.tsx`
```tsx
import React from "react";
import { FileFormat, TypeLanguage } from "../../enums/file.enum";
import { TypegenWrapper } from "../../layout/TypeLayout/TypegenWrapper";

const TypePage = () => {
  return <TypegenWrapper from={FileFormat.JSON} to={TypeLanguage.Kotlin} />;
};

export default TypePage;
```

## File: `apps/www/src/pages/type/json-to-rust.tsx`
```tsx
import React from "react";
import { FileFormat, TypeLanguage } from "../../enums/file.enum";
import { TypegenWrapper } from "../../layout/TypeLayout/TypegenWrapper";

const TypePage = () => {
  return <TypegenWrapper from={FileFormat.JSON} to={TypeLanguage.Rust} />;
};

export default TypePage;
```

## File: `apps/www/src/pages/type/json-to-typescript.tsx`
```tsx
import React from "react";
import { FileFormat, TypeLanguage } from "../../enums/file.enum";
import { TypegenWrapper } from "../../layout/TypeLayout/TypegenWrapper";

const TypePage = () => {
  return <TypegenWrapper from={FileFormat.JSON} to={TypeLanguage.TypeScript} />;
};

export default TypePage;
```

## File: `apps/www/src/pages/type/xml-to-go.tsx`
```tsx
import React from "react";
import { FileFormat, TypeLanguage } from "../../enums/file.enum";
import { TypegenWrapper } from "../../layout/TypeLayout/TypegenWrapper";

const TypePage = () => {
  return <TypegenWrapper from={FileFormat.XML} to={TypeLanguage.Go} />;
};

export default TypePage;
```

## File: `apps/www/src/pages/type/xml-to-kotlin.tsx`
```tsx
import React from "react";
import { FileFormat, TypeLanguage } from "../../enums/file.enum";
import { TypegenWrapper } from "../../layout/TypeLayout/TypegenWrapper";

const TypePage = () => {
  return <TypegenWrapper from={FileFormat.XML} to={TypeLanguage.Kotlin} />;
};

export default TypePage;
```

## File: `apps/www/src/pages/type/xml-to-rust.tsx`
```tsx
import React from "react";
import { FileFormat, TypeLanguage } from "../../enums/file.enum";
import { TypegenWrapper } from "../../layout/TypeLayout/TypegenWrapper";

const TypePage = () => {
  return <TypegenWrapper from={FileFormat.XML} to={TypeLanguage.Rust} />;
};

export default TypePage;
```

## File: `apps/www/src/pages/type/xml-to-typescript.tsx`
```tsx
import React from "react";
import { FileFormat, TypeLanguage } from "../../enums/file.enum";
import { TypegenWrapper } from "../../layout/TypeLayout/TypegenWrapper";

const TypePage = () => {
  return <TypegenWrapper from={FileFormat.XML} to={TypeLanguage.TypeScript} />;
};

export default TypePage;
```

## File: `apps/www/src/pages/type/yaml-to-go.tsx`
```tsx
import React from "react";
import { FileFormat, TypeLanguage } from "../../enums/file.enum";
import { TypegenWrapper } from "../../layout/TypeLayout/TypegenWrapper";

const TypePage = () => {
  return <TypegenWrapper from={FileFormat.YAML} to={TypeLanguage.Go} />;
};

export default TypePage;
```

## File: `apps/www/src/pages/type/yaml-to-kotlin.tsx`
```tsx
import React from "react";
import { FileFormat, TypeLanguage } from "../../enums/file.enum";
import { TypegenWrapper } from "../../layout/TypeLayout/TypegenWrapper";

const TypePage = () => {
  return <TypegenWrapper from={FileFormat.YAML} to={TypeLanguage.Kotlin} />;
};

export default TypePage;
```

## File: `apps/www/src/pages/type/yaml-to-rust.tsx`
```tsx
import React from "react";
import { FileFormat, TypeLanguage } from "../../enums/file.enum";
import { TypegenWrapper } from "../../layout/TypeLayout/TypegenWrapper";

const TypePage = () => {
  return <TypegenWrapper from={FileFormat.YAML} to={TypeLanguage.Rust} />;
};

export default TypePage;
```

## File: `apps/www/src/pages/type/yaml-to-typescript.tsx`
```tsx
import React from "react";
import { FileFormat, TypeLanguage } from "../../enums/file.enum";
import { TypegenWrapper } from "../../layout/TypeLayout/TypegenWrapper";

const TypePage = () => {
  return <TypegenWrapper from={FileFormat.YAML} to={TypeLanguage.TypeScript} />;
};

export default TypePage;
```

## File: `apps/www/src/store/useConfig.ts`
```typescript
import { create } from "zustand";
import { persist } from "zustand/middleware";

const initialStates = {
  darkmodeEnabled: true,
  liveTransformEnabled: true,
  gesturesEnabled: false,
  rulersEnabled: true,
};

export interface ConfigActions {
  toggleDarkMode: (value: boolean) => void;
  toggleLiveTransform: (value: boolean) => void;
  toggleGestures: (value: boolean) => void;
  toggleRulers: (value: boolean) => void;
}

const useConfig = create(
  persist<typeof initialStates & ConfigActions>(
    set => ({
      ...initialStates,
      toggleRulers: rulersEnabled => set({ rulersEnabled }),
      toggleGestures: gesturesEnabled => set({ gesturesEnabled }),
      toggleLiveTransform: liveTransformEnabled => set({ liveTransformEnabled }),
      toggleDarkMode: darkmodeEnabled => set({ darkmodeEnabled }),
    }),
    {
      name: "config",
    }
  )
);

export default useConfig;
```

## File: `apps/www/src/store/useFile.ts`
```typescript
import debounce from "lodash.debounce";
import { event as gaEvent } from "nextjs-google-analytics";
import { toast } from "react-hot-toast";
import { create } from "zustand";
import exampleJson from "../data/example.json";
import { FileFormat } from "../enums/file.enum";
import { isIframe } from "../lib/utils/helpers";
import { contentToJson, jsonToContent } from "../lib/utils/jsonAdapter";
import useConfig from "./useConfig";
import useJson from "./useJson";

const defaultJson = JSON.stringify(exampleJson, null, 2);

type SetContents = {
  contents?: string;
  hasChanges?: boolean;
  skipUpdate?: boolean;
  format?: FileFormat;
};

type Query = string | string[] | undefined;

interface JsonActions {
  getContents: () => string;
  getFormat: () => FileFormat;
  getHasChanges: () => boolean;
  setError: (error: string | null) => void;
  setHasChanges: (hasChanges: boolean) => void;
  setContents: (data: SetContents) => void;
  fetchUrl: (url: string) => void;
  setFormat: (format: FileFormat) => void;
  clear: () => void;
  setFile: (fileData: File) => void;
  setJsonSchema: (jsonSchema: object | null) => void;
  checkEditorSession: (url: Query, widget?: boolean) => void;
}

export type File = {
  id: string;
  views: number;
  owner_email: string;
  name: string;
  content: string;
  private: boolean;
  format: FileFormat;
  created_at: string;
  updated_at: string;
};

const initialStates = {
  fileData: null as File | null,
  format: FileFormat.JSON,
  contents: defaultJson,
  error: null as any,
  hasChanges: false,
  jsonSchema: null as object | null,
};

export type FileStates = typeof initialStates;

const isURL = (value: string) => {
  return /(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,})/gi.test(
    value
  );
};

const debouncedUpdateJson = debounce((value: unknown) => {
  useJson.getState().setJson(JSON.stringify(value, null, 2));
}, 400);

const useFile = create<FileStates & JsonActions>()((set, get) => ({
  ...initialStates,
  clear: () => {
    set({ contents: "" });
    useJson.getState().clear();
  },
  setJsonSchema: jsonSchema => set({ jsonSchema }),
  setFile: fileData => {
    set({ fileData, format: fileData.format || FileFormat.JSON });
    get().setContents({ contents: fileData.content, hasChanges: false });
    gaEvent("set_content", { label: fileData.format });
  },
  getContents: () => get().contents,
  getFormat: () => get().format,
  getHasChanges: () => get().hasChanges,
  setFormat: async format => {
    try {
      const prevFormat = get().format;

      set({ format });
      const contentJson = await contentToJson(get().contents, prevFormat);
      const jsonContent = await jsonToContent(JSON.stringify(contentJson, null, 2), format);

      get().setContents({ contents: jsonContent });
    } catch {
      get().clear();
      console.warn("The content was unable to be converted, so it was cleared instead.");
    }
  },
  setContents: async ({ contents, hasChanges = true, skipUpdate = false, format }) => {
    try {
      set({
        ...(contents && { contents }),
        error: null,
        hasChanges,
        format: format ?? get().format,
      });

      const isFetchURL = window.location.href.includes("?");
      const json = await contentToJson(get().contents, get().format);

      if (!useConfig.getState().liveTransformEnabled && skipUpdate) return;

      if (get().hasChanges && contents && contents.length < 80_000 && !isIframe() && !isFetchURL) {
        sessionStorage.setItem("content", contents);
        sessionStorage.setItem("format", get().format);
        set({ hasChanges: true });
      }

      debouncedUpdateJson(json);
    } catch (error: any) {
      if (error?.mark?.snippet) return set({ error: error.mark.snippet });
      if (error?.message) set({ error: error.message });
      useJson.setState({ loading: false });
    }
  },
  setError: error => set({ error }),
  setHasChanges: hasChanges => set({ hasChanges }),
  fetchUrl: async url => {
    try {
      const res = await fetch(url);
      const json = await res.json();
      const jsonStr = JSON.stringify(json, null, 2);

      get().setContents({ contents: jsonStr });
      return useJson.setState({ json: jsonStr, loading: false });
    } catch {
      get().clear();
      toast.error("Failed to fetch document from URL!");
    }
  },
  checkEditorSession: (url, widget) => {
    if (url && typeof url === "string" && isURL(url)) {
      return get().fetchUrl(url);
    }

    let contents = defaultJson;
    const sessionContent = sessionStorage.getItem("content") as string | null;
    const format = sessionStorage.getItem("format") as FileFormat | null;
    if (sessionContent && !widget) contents = sessionContent;

    if (format) set({ format });
    get().setContents({ contents, hasChanges: false });
  },
}));

export default useFile;
```

## File: `apps/www/src/store/useJson.ts`
```typescript
import { create } from "zustand";

interface JsonActions {
  setJson: (json: string) => void;
  getJson: () => string;
  clear: () => void;
}

const initialStates = {
  json: "{}",
  loading: true,
};

export type JsonStates = typeof initialStates;

const useJson = create<JsonStates & JsonActions>()((set, get) => ({
  ...initialStates,
  getJson: () => get().json,
  setJson: json => {
    set({ json, loading: false });
  },
  clear: () => {
    set({ json: "", loading: false });
  },
}));

export default useJson;
```

## File: `apps/www/src/store/useModal.ts`
```typescript
import { createWithEqualityFn as create } from "zustand/traditional";
import { type ModalName, modals } from "../features/modals/modalTypes";

interface ModalActions {
  setVisible: (name: ModalName, open: boolean) => void;
}

type ModalState = Record<ModalName, boolean>;

const initialStates: ModalState = modals.reduce((acc, modal) => {
  acc[modal] = false;
  return acc;
}, {} as ModalState);

export const useModal = create<ModalState & ModalActions>()(set => ({
  ...initialStates,
  setVisible: (name, open) => {
    set({ [name]: open });
  },
}));
```

## File: `apps/www/src/types/styled.d.ts`
```typescript
/* eslint-disable @typescript-eslint/no-empty-object-type */
import "styled-components";
import type theme from "../constants/theme";

type CustomTheme = typeof theme;

declare module "styled-components" {
  export interface DefaultTheme extends CustomTheme {}
}
```

## File: `packages/jsoncrack-react/.gitignore`
```
node_modules
dist/
.turbo/
coverage/
*.tsbuildinfo
```

## File: `packages/jsoncrack-react/.prettierrc`
```
{
  "trailingComma": "es5",
  "singleQuote": false,
  "semi": true,
  "printWidth": 100,
  "arrowParens": "avoid",
  "importOrder": [
    "^(react/(.*)$)|^(react$)",
    "<THIRD_PARTY_MODULES>",
    "^[./]"
  ],
  "importOrderParserPlugins": ["typescript", "jsx", "decorators-legacy"],
  "plugins": ["@trivago/prettier-plugin-sort-imports"]
}
```

## File: `packages/jsoncrack-react/eslint.config.mjs`
```
import { FlatCompat } from "@eslint/eslintrc";
import js from "@eslint/js";
import prettier from "eslint-plugin-prettier";
import unusedImports from "eslint-plugin-unused-imports";
import { defineConfig, globalIgnores } from "eslint/config";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const compat = new FlatCompat({
  baseDirectory: __dirname,
  recommendedConfig: js.configs.recommended,
  allConfig: js.configs.all,
});

export default defineConfig([
  globalIgnores(["dist", "scripts", "node_modules"]),
  {
    extends: [
      ...compat.extends("eslint:recommended"),
      ...compat.extends("prettier"),
      ...compat.extends("plugin:@typescript-eslint/recommended"),
    ],

    plugins: {
      prettier,
      "unused-imports": unusedImports,
    },

    rules: {
      "@typescript-eslint/consistent-type-imports": "error",
      "unused-imports/no-unused-imports": "error",
      "@typescript-eslint/no-explicit-any": "off",
      "prettier/prettier": "error",
      "space-in-parens": "error",
      "no-empty": "error",
      "no-multiple-empty-lines": "error",
      "no-irregular-whitespace": "error",
      strict: ["error", "never"],
      "linebreak-style": ["error", "unix"],

      quotes: [
        "error",
        "double",
        {
          avoidEscape: true,
        },
      ],

      semi: ["error", "always"],
      "prefer-const": "error",

      "space-before-function-paren": [
        "error",
        {
          anonymous: "always",
          named: "never",
          asyncArrow: "always",
        },
      ],
    },
  },
]);
```

## File: `packages/jsoncrack-react/LICENSE.md`
```markdown
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

   Copyright 2025 Aykut Saraç

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

## File: `packages/jsoncrack-react/package.json`
```json
{
  "name": "jsoncrack-react",
  "version": "1.0.0",
  "description": "Reusable JSON Crack canvas as a React component",
  "license": "Apache-2.0",
  "author": "Aykut Saraç",
  "homepage": "https://jsoncrack.com",
  "repository": {
    "type": "git",
    "url": "https://github.com/AykutSarac/jsoncrack.com"
  },
  "keywords": [
    "json",
    "visualizer",
    "graph",
    "canvas",
    "react",
    "json-crack",
    "typescript"
  ],
  "type": "module",
  "main": "./dist/index.js",
  "types": "./dist/index.d.ts",
  "exports": {
    ".": {
      "types": "./dist/index.d.ts",
      "import": "./dist/index.js"
    },
    "./style.css": "./dist/index.css"
  },
  "files": [
    "dist"
  ],
  "sideEffects": [
    "./dist/index.css"
  ],
  "scripts": {
    "build": "vite build && tsc -p tsconfig.build.json",
    "clean": "rm -rf dist",
    "lint": "tsc -p tsconfig.build.json --noEmit && eslint src && prettier --check src",
    "lint:fix": "eslint --fix src && prettier --write src"
  },
  "peerDependencies": {
    "react": ">=18",
    "react-dom": ">=18"
  },
  "dependencies": {
    "jsonc-parser": "^3.3.1",
    "react-zoomable-ui": "^0.11.0",
    "reaflow": "5.4.1"
  },
  "devDependencies": {
    "@eslint/eslintrc": "^3.2.0",
    "@eslint/js": "^9.39.2",
    "@trivago/prettier-plugin-sort-imports": "^4.3.0",
    "@types/react": "^19.2.11",
    "@types/react-dom": "^19.2.3",
    "@typescript-eslint/eslint-plugin": "^8.54.0",
    "@typescript-eslint/parser": "^8.54.0",
    "@vitejs/plugin-react": "^4.3.0",
    "eslint": "^9.39.2",
    "eslint-config-prettier": "^10.1.8",
    "eslint-plugin-prettier": "^5.5.5",
    "eslint-plugin-unused-imports": "^4.3.0",
    "prettier": "^3.8.1",
    "typescript": "^5.9.3",
    "vite": "^6.0.0"
  }
}
```

## File: `packages/jsoncrack-react/README.md`
```markdown
# jsoncrack-react

Reusable JSON graph canvas component from [JSON Crack](https://jsoncrack.com) — visualize JSON as interactive node graphs.

- React component API
- Interactive canvas (pan/zoom + optional controls)
- TypeScript types included

[Live demo](https://jsoncrack.com) · [GitHub](https://github.com/AykutSarac/jsoncrack.com) · [npm](https://www.npmjs.com/package/jsoncrack-react)

## Install

```bash
npm install jsoncrack-react
```

Peer dependencies: `react >= 18`, `react-dom >= 18`

## Setup

Import the stylesheet once in your app entry point:

```ts
import "jsoncrack-react/style.css";
```

## Quick Start

```tsx
import { JSONCrack } from "jsoncrack-react";

export function Example() {
  return (
    <div style={{ height: 700 }}>
      <JSONCrack
        json={{
          user: {
            id: 1,
            name: "Ada",
            tags: ["admin", "staff"],
          },
        }}
      />
    </div>
  );
}
```

The wrapper must have an explicit height.

## Props

| Prop | Type | Default | Description |
| --- | --- | --- | --- |
| `json` | `string \| object \| unknown[]` | - | JSON input data to visualize |
| `theme` | `"dark" \| "light"` | `"dark"` | Canvas theme |
| `layoutDirection` | `"LEFT" \| "RIGHT" \| "DOWN" \| "UP"` | `"RIGHT"` | Layout direction |
| `showControls` | `boolean` | `true` | Show built-in camera controls |
| `showGrid` | `boolean` | `true` | Show grid background |
| `trackpadZoom` | `boolean` | `false` | Enables two-finger trackpad gesture zoom behavior |
| `centerOnLayout` | `boolean` | `true` | Auto-center on first/major layout changes |
| `maxRenderableNodes` | `number` | `1500` | Node rendering safety limit |
| `className` | `string` | - | Wrapper class |
| `style` | `React.CSSProperties` | - | Wrapper inline style |
| `onNodeClick` | `(node: NodeData) => void` | - | Node click callback |
| `onParse` | `(graph: GraphData) => void` | - | Parsed graph callback |
| `onParseError` | `(error: Error) => void` | - | Parse error callback |
| `onViewportCreate` | `(viewPort: ViewPort) => void` | - | Viewport ready callback |
| `renderNodeLimitExceeded` | `(nodeCount: number, maxRenderableNodes: number) => React.ReactNode` | - | Custom fallback when node limit is exceeded |

## Performance

The component renders all nodes as SVG elements. For large inputs, rendering cost grows with the number of nodes.

- **Default limit:** `maxRenderableNodes` is set to `1500`. Graphs exceeding this render a fallback instead of the canvas.
- **Recommended range:** Up to ~300–500 nodes for smooth interaction. Beyond that, panning and zooming may feel sluggish depending on the device.
- **Reduce node count:** Flatten or trim your data before passing it in. Arrays of primitives become individual nodes, so large arrays expand the graph quickly.
- **Custom fallback:** Use `renderNodeLimitExceeded` to show a message or alternative UI when the limit is hit.

```tsx
<JSONCrack
  json={data}
  maxRenderableNodes={300}
  renderNodeLimitExceeded={(count, max) => (
    <p>Too large to render ({count} nodes, limit is {max})</p>
  )}
/>
```

## Imperative API (ref)

```tsx
import { useRef } from "react";
import { JSONCrack, type JSONCrackRef } from "jsoncrack-react";

export function WithRef({ json }: { json: string }) {
  const ref = useRef<JSONCrackRef>(null);

  return (
    <>
      <button onClick={() => ref.current?.centerView()}>Center</button>
      <button onClick={() => ref.current?.zoomIn()}>+</button>
      <button onClick={() => ref.current?.zoomOut()}>-</button>
      <div style={{ height: 600 }}>
        <JSONCrack ref={ref} json={json} />
      </div>
    </>
  );
}
```

`JSONCrackRef` methods:

- `zoomIn()`
- `zoomOut()`
- `setZoom(zoomFactor: number)`
- `centerView()`
- `focusFirstNode()`

## Utility: `parseGraph`

If you only need parser output:

```ts
import { parseGraph } from "jsoncrack-react";

const result = parseGraph('{"a":[1,2,3]}');
// result: { nodes, edges, errors }
```

## Exported Types

- `JSONCrackProps`
- `JSONCrackRef`
- `ParseGraphResult`
- `CanvasThemeMode`
- `LayoutDirection`
- `NodeData`
- `EdgeData`
- `GraphData`
- `NodeRow`

## License

Apache-2.0
```

## File: `packages/jsoncrack-react/tsconfig.build.json`
```json
{
  "compilerOptions": {
    "target": "ES2020",
    "lib": ["DOM", "ES2020"],
    "module": "ESNext",
    "moduleResolution": "Bundler",
    "strict": true,
    "declaration": true,
    "declarationMap": true,
    "emitDeclarationOnly": true,
    "outDir": "dist",
    "rootDir": "src",
    "jsx": "react-jsx",
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true
  },
  "include": ["src"]
}
```

## File: `packages/jsoncrack-react/tsconfig.json`
```json
{
  "extends": "./tsconfig.build.json",
  "compilerOptions": {
    "noEmit": true
  },
  "include": ["src"],
  "exclude": ["dist", "node_modules"]
}
```

## File: `packages/jsoncrack-react/vite.config.ts`
```typescript
import react from "@vitejs/plugin-react";
import { resolve } from "node:path";
import { defineConfig } from "vite";

export default defineConfig({
  plugins: [react()],
  build: {
    lib: {
      entry: resolve(__dirname, "src/index.ts"),
      formats: ["es"],
      fileName: "index",
    },
    rollupOptions: {
      external: [
        "react",
        "react-dom",
        "react/jsx-runtime",
        "reaflow",
        "react-zoomable-ui",
        "jsonc-parser",
      ],
      output: {
        assetFileNames: "index[extname]",
      },
    },
  },
});
```

## File: `packages/jsoncrack-react/src/css-modules.d.ts`
```typescript
declare module "*.module.css" {
  const classes: Record<string, string>;
  export default classes;
}
```

## File: `packages/jsoncrack-react/src/index.ts`
```typescript
export { JSONCrack } from "./JSONCrackComponent";
export { parseGraph } from "./parser";
export type { JSONCrackProps, JSONCrackRef } from "./JSONCrackComponent";
export type { ParseGraphResult } from "./parser";
export type {
  CanvasThemeMode,
  EdgeData,
  GraphData,
  LayoutDirection,
  NodeData,
  NodeRow,
} from "./types";
```

## File: `packages/jsoncrack-react/src/JSONCrackComponent.tsx`
```tsx
"use client";

import React from "react";
import type { ViewPort } from "react-zoomable-ui";
import { Space } from "react-zoomable-ui";
import { Canvas } from "reaflow";
import type { ElkRoot } from "reaflow";
import styles from "./JSONCrackStyles.module.css";
import { Controls } from "./components/Controls";
import { CustomEdge } from "./components/CustomEdge";
import { CustomNode } from "./components/CustomNode";
import { parseGraph } from "./parser";
import { themes } from "./theme";
import type { CanvasThemeMode, GraphData, LayoutDirection, NodeData } from "./types";

const layoutOptions = {
  "elk.layered.compaction.postCompaction.strategy": "EDGE_LENGTH",
  "elk.layered.nodePlacement.strategy": "NETWORK_SIMPLEX",
  "elk.spacing.edgeLabel": "15",
};

const objectJsonCache = new WeakMap<object, string>();

export interface JSONCrackRef {
  zoomIn: () => void;
  zoomOut: () => void;
  setZoom: (zoomFactor: number) => void;
  centerView: () => void;
  focusFirstNode: () => void;
}

export interface JSONCrackProps {
  json: string | object | unknown[];
  theme?: CanvasThemeMode;
  layoutDirection?: LayoutDirection;
  showControls?: boolean;
  showGrid?: boolean;
  trackpadZoom?: boolean;
  centerOnLayout?: boolean;
  maxRenderableNodes?: number;
  className?: string;
  style?: React.CSSProperties;
  onNodeClick?: (node: NodeData) => void;
  onParse?: (graph: GraphData) => void;
  onParseError?: (error: Error) => void;
  onViewportCreate?: (viewPort: ViewPort) => void;
  renderNodeLimitExceeded?: (nodeCount: number, maxRenderableNodes: number) => React.ReactNode;
}

const toJsonText = (json: JSONCrackProps["json"]): string => {
  if (typeof json === "string") return json;

  if (json && typeof json === "object") {
    const cached = objectJsonCache.get(json);
    if (cached) return cached;

    const serialized = JSON.stringify(json, null, 2);
    objectJsonCache.set(json, serialized);
    return serialized;
  }

  return JSON.stringify(json, null, 2);
};

export const JSONCrack = React.forwardRef<JSONCrackRef, JSONCrackProps>(
  (
    {
      json,
      theme = "dark",
      layoutDirection = "RIGHT",
      showControls = true,
      showGrid = true,
      trackpadZoom = false,
      centerOnLayout = true,
      maxRenderableNodes = 1500,
      className,
      style,
      onNodeClick,
      onParse,
      onParseError,
      onViewportCreate,
      renderNodeLimitExceeded,
    },
    ref
  ) => {
    const themeTokens = themes[theme];
    const containerRef = React.useRef<HTMLDivElement | null>(null);
    const [viewPort, setViewPort] = React.useState<ViewPort | null>(null);
    const [nodes, setNodes] = React.useState<GraphData["nodes"]>([]);
    const [edges, setEdges] = React.useState<GraphData["edges"]>([]);
    const [loading, setLoading] = React.useState(true);
    const [aboveSupportedLimit, setAboveSupportedLimit] = React.useState(false);
    const [totalNodes, setTotalNodes] = React.useState(0);
    const [paneWidth, setPaneWidth] = React.useState(2000);
    const [paneHeight, setPaneHeight] = React.useState(2000);
    const hasAutoFittedRef = React.useRef(false);
    const previousLayoutAreaRef = React.useRef<number | null>(null);
    const callbacksRef = React.useRef({ onParse, onParseError });
    const onViewportCreateRef = React.useRef(onViewportCreate);
    const lastParsedInputRef = React.useRef<{
      jsonText: string;
      maxRenderableNodes: number;
    } | null>(null);

    React.useEffect(() => {
      callbacksRef.current = { onParse, onParseError };
    }, [onParse, onParseError]);

    React.useEffect(() => {
      onViewportCreateRef.current = onViewportCreate;
    }, [onViewportCreate]);

    React.useEffect(() => {
      hasAutoFittedRef.current = false;
      previousLayoutAreaRef.current = null;
    }, [layoutDirection]);

    const centerView = React.useCallback(() => {
      const nextViewPort = viewPort;
      nextViewPort?.updateContainerSize();

      const canvas = containerRef.current?.querySelector(".jsoncrack-canvas") as HTMLElement | null;
      if (canvas) {
        nextViewPort?.camera?.centerFitElementIntoView(canvas);
      }
    }, [viewPort]);

    const focusFirstNode = React.useCallback(() => {
      const rootNode = containerRef.current?.querySelector("g[id$='node-1']") as HTMLElement | null;
      if (!rootNode) return;

      viewPort?.camera?.centerFitElementIntoView(rootNode, {
        elementExtraMarginForZoom: 100,
      });
    }, [viewPort]);

    const setZoom = React.useCallback(
      (zoomFactor: number) => {
        if (!viewPort) return;
        viewPort.camera?.recenter(viewPort.centerX, viewPort.centerY, zoomFactor);
      },
      [viewPort]
    );

    const zoomIn = React.useCallback(() => {
      if (!viewPort) return;
      viewPort.camera?.recenter(viewPort.centerX, viewPort.centerY, viewPort.zoomFactor + 0.1);
    }, [viewPort]);

    const zoomOut = React.useCallback(() => {
      if (!viewPort) return;
      viewPort.camera?.recenter(viewPort.centerX, viewPort.centerY, viewPort.zoomFactor - 0.1);
    }, [viewPort]);

    React.useImperativeHandle(
      ref,
      () => ({
        zoomIn,
        zoomOut,
        setZoom,
        centerView,
        focusFirstNode,
      }),
      [centerView, focusFirstNode, setZoom, zoomIn, zoomOut]
    );

    React.useEffect(() => {
      try {
        const jsonText = toJsonText(json);
        const lastParsedInput = lastParsedInputRef.current;

        if (
          lastParsedInput &&
          lastParsedInput.jsonText === jsonText &&
          lastParsedInput.maxRenderableNodes === maxRenderableNodes
        ) {
          return;
        }

        setLoading(true);

        const graph = parseGraph(jsonText);

        if (graph.errors.length > 0) {
          callbacksRef.current.onParseError?.(
            new Error(`Failed to parse data (${graph.errors.length} syntax error(s)).`)
          );
        }

        setTotalNodes(graph.nodes.length);

        if (graph.nodes.length > maxRenderableNodes) {
          setAboveSupportedLimit(true);
          setNodes([]);
          setEdges([]);
          setLoading(false);
          lastParsedInputRef.current = {
            jsonText,
            maxRenderableNodes,
          };
          return;
        }

        setAboveSupportedLimit(false);
        setNodes(graph.nodes);
        setEdges(graph.edges);
        callbacksRef.current.onParse?.({
          nodes: graph.nodes,
          edges: graph.edges,
        });
        lastParsedInputRef.current = {
          jsonText,
          maxRenderableNodes,
        };

        if (graph.nodes.length === 0) {
          setLoading(false);
        }
      } catch (error) {
        setNodes([]);
        setEdges([]);
        setLoading(false);
        callbacksRef.current.onParseError?.(
          error instanceof Error ? error : new Error("Unable to parse data.")
        );
      }
    }, [json, maxRenderableNodes]);

    const edgeTargetById = React.useMemo(() => {
      const targetById = new Map<string, string>();

      for (let i = 0; i < edges.length; i += 1) {
        const edge = edges[i];
        targetById.set(edge.id, edge.to);
      }

      return targetById;
    }, [edges]);

    const onLayoutChange = React.useCallback(
      (layout: ElkRoot) => {
        if (!layout.width || !layout.height) {
          setLoading(false);
          return;
        }

        const currentLayoutArea = layout.width * layout.height;
        const previousLayoutArea = previousLayoutAreaRef.current;
        previousLayoutAreaRef.current = currentLayoutArea;

        setPaneWidth(layout.width + 50);
        setPaneHeight(layout.height + 50);

        setTimeout(() => {
          window.requestAnimationFrame(() => {
            const isFirstAutoFit = !hasAutoFittedRef.current;
            const hasLargeLayoutChange =
              previousLayoutArea !== null &&
              previousLayoutArea > 0 &&
              Math.abs((currentLayoutArea * 100) / previousLayoutArea - 100) > 70;
            const shouldAutoFit = centerOnLayout && (isFirstAutoFit || hasLargeLayoutChange);

            if (shouldAutoFit) {
              centerView();
              hasAutoFittedRef.current = true;
            }

            setLoading(false);
          });
        }, 0);
      },
      [centerView, centerOnLayout]
    );

    const tooLargeContent = renderNodeLimitExceeded?.(totalNodes, maxRenderableNodes);
    const canvasClassName = [styles.canvasWrapper, showGrid ? styles.showGrid : "", className]
      .filter(Boolean)
      .join(" ");
    const canvasStyle = {
      "--bg-color": themeTokens.GRID_BG_COLOR,
      "--line-color-1": themeTokens.GRID_COLOR_PRIMARY,
      "--line-color-2": themeTokens.GRID_COLOR_SECONDARY,
      "--edge-stroke": theme === "dark" ? "#444444" : "#BCBEC0",
      "--node-fill": theme === "dark" ? "#292929" : "#ffffff",
      "--node-stroke": theme === "dark" ? "#424242" : "#BCBEC0",
      "--interactive-normal": themeTokens.INTERACTIVE_NORMAL,
      "--background-node": themeTokens.BACKGROUND_NODE,
      "--node-text": themeTokens.NODE_COLORS.TEXT,
      "--node-key": themeTokens.NODE_COLORS.NODE_KEY,
      "--node-value": themeTokens.NODE_COLORS.NODE_VALUE,
      "--node-integer": themeTokens.NODE_COLORS.INTEGER,
      "--node-null": themeTokens.NODE_COLORS.NULL,
      "--node-bool-true": themeTokens.NODE_COLORS.BOOL.TRUE,
      "--node-bool-false": themeTokens.NODE_COLORS.BOOL.FALSE,
      "--node-child-count": themeTokens.NODE_COLORS.CHILD_COUNT,
      "--node-divider": themeTokens.NODE_COLORS.DIVIDER,
      "--text-positive": themeTokens.TEXT_POSITIVE,
      "--background-modifier-accent": themeTokens.BACKGROUND_MODIFIER_ACCENT,
      "--spinner-track": theme === "dark" ? "rgba(255, 255, 255, 0.3)" : "rgba(17, 24, 39, 0.2)",
      "--spinner-head": theme === "dark" ? "#FFFFFF" : "#111827",
      "--overlay-bg": theme === "dark" ? "rgba(0, 0, 0, 0.2)" : "rgba(255, 255, 255, 0.38)",
      ...style,
    } as React.CSSProperties;

    return (
      <div
        ref={containerRef}
        className={canvasClassName}
        style={canvasStyle}
        onContextMenu={event => event.preventDefault()}
      >
        {showControls && (
          <Controls
            onFocusRoot={focusFirstNode}
            onCenterView={centerView}
            onZoomOut={zoomOut}
            onZoomIn={zoomIn}
          />
        )}

        {aboveSupportedLimit &&
          (tooLargeContent ? (
            tooLargeContent
          ) : (
            <div className={styles.tooLarge}>
              {`This graph has ${totalNodes} nodes and exceeds the maxRenderableNodes limit (${maxRenderableNodes}).`}
            </div>
          ))}

        {loading && (
          <div className={styles.overlay}>
            <div className={styles.spinner} />
          </div>
        )}

        <Space
          onCreate={nextViewPort => {
            setViewPort(nextViewPort);
            onViewportCreateRef.current?.(nextViewPort);
          }}
          onContextMenu={event => event.preventDefault()}
          treatTwoFingerTrackPadGesturesLikeTouch={trackpadZoom}
          pollForElementResizing
          className="jsoncrack-space"
        >
          <Canvas
            className="jsoncrack-canvas"
            onLayoutChange={onLayoutChange}
            node={nodeProps => <CustomNode {...nodeProps} onNodeClick={onNodeClick} />}
            edge={edgeProps => (
              <CustomEdge
                {...edgeProps}
                viewPort={viewPort}
                edgeTargetById={edgeTargetById}
                hostElement={containerRef.current}
              />
            )}
            nodes={nodes}
            edges={edges}
            arrow={null}
            maxHeight={paneHeight}
            maxWidth={paneWidth}
            height={paneHeight}
            width={paneWidth}
            direction={layoutDirection}
            layoutOptions={layoutOptions}
            key={layoutDirection}
            pannable={false}
            zoomable={false}
            animated={false}
            readonly
            dragEdge={null}
            dragNode={null}
            fit
          />
        </Space>
      </div>
    );
  }
);

JSONCrack.displayName = "JSONCrack";
```

## File: `packages/jsoncrack-react/src/JSONCrackStyles.module.css`
```css
.canvasWrapper {
  position: relative;
  width: 100%;
  height: 100%;
  background-color: var(--bg-color);
}

.showGrid {
  background-image:
    linear-gradient(var(--line-color-1) 1.5px, transparent 1.5px),
    linear-gradient(90deg, var(--line-color-1) 1.5px, transparent 1.5px),
    linear-gradient(var(--line-color-2) 1px, transparent 1px),
    linear-gradient(90deg, var(--line-color-2) 1px, transparent 1px);
  background-position:
    -1.5px -1.5px,
    -1.5px -1.5px,
    -1px -1px,
    -1px -1px;
  background-size:
    100px 100px,
    100px 100px,
    20px 20px,
    20px 20px;
}

.canvasWrapper :global(.jsoncrack-space) {
  cursor: grab;
}

.canvasWrapper :global(.jsoncrack-space:active) {
  cursor: grabbing;
}

.canvasWrapper :global(.dragging),
.canvasWrapper :global(.dragging button) {
  pointer-events: none;
}

.canvasWrapper :global(text) {
  fill: var(--interactive-normal) !important;
}

.canvasWrapper :global(rect) {
  fill: var(--node-fill);
}

.overlay {
  position: absolute;
  inset: 0;
  z-index: 30;
  display: flex;
  align-items: center;
  justify-content: center;
  pointer-events: none;
  background: radial-gradient(circle at center, var(--overlay-bg) 0 44px, transparent 96px);
}

.spinner {
  width: 30px;
  height: 30px;
  border-radius: 9999px;
  border: 3px solid var(--spinner-track);
  border-top-color: var(--spinner-head);
  border-right-color: var(--spinner-head);
  animation: spin 0.9s linear infinite;
}

@keyframes spin {
  to {
    transform: rotate(360deg);
  }
}

.tooLarge {
  position: absolute;
  inset: 0;
  z-index: 40;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 24px;
  text-align: center;
  background: rgba(0, 0, 0, 0.62);
  color: #ffffff;
  font-size: 14px;
}
```

## File: `packages/jsoncrack-react/src/parser.ts`
```typescript
import { getNodePath, parseTree, type Node, type ParseError } from "jsonc-parser";
import type { EdgeData, GraphData, NodeData, NodeRow } from "./types";
import { calculateNodeSize } from "./utils/calculateNodeSize";

export interface ParseGraphResult extends GraphData {
  errors: ParseError[];
}

export const parseGraph = (json: string): ParseGraphResult => {
  const parseErrors: ParseError[] = [];
  const jsonTree = parseTree(json, parseErrors);

  if (!jsonTree) {
    return {
      nodes: [],
      edges: [],
      errors: parseErrors,
    };
  }

  const nodes: NodeData[] = [];
  const edges: EdgeData[] = [];
  let nodeId = 1;
  let edgeId = 1;

  function traverse(node: Node, parentId?: string): string | undefined {
    const id = String(nodeId++);
    const text: NodeRow[] = [];

    if (parentId !== undefined && node.parent?.type === "array") {
      edges.push({
        id: String(edgeId++),
        from: parentId,
        to: id,
        text: "",
      });
    }

    const isArray = node.type === "array";
    const isRootArray = !node.parent || node.parent.type === "array";

    if (isArray && isRootArray) {
      const { width, height } = calculateNodeSize(`[${node.children?.length ?? "0"} items]`);

      nodes.push({
        id,
        text: [
          {
            key: null,
            value: `[${node.children?.length ?? 0} items]`,
            type: "array",
            childrenCount: node.children?.length,
          },
        ],
        width,
        height,
        path: [],
      });

      node.children?.forEach(child => {
        traverse(child, id);
      });

      return id;
    }

    node.children?.forEach(child => {
      if (!child.children || !child.children[1]) {
        traverse(child, id);
        return;
      }

      const key = child.children[0].value?.toString() ?? null;
      const valueNode = child.children[1];
      const type = valueNode.type;

      if (type === "array") {
        const targetIds: string[] = [];

        valueNode.children?.forEach(arrayChild => {
          const arrayChildId = traverse(arrayChild, undefined);
          if (arrayChildId) targetIds.push(arrayChildId);
        });

        text.push({
          key,
          value: valueNode.value as NodeRow["value"],
          type,
          to: targetIds.length > 0 ? targetIds : undefined,
          childrenCount: valueNode.children?.length,
        });

        targetIds.forEach(targetId => {
          edges.push({
            id: String(edgeId++),
            from: id,
            to: targetId,
            text: key,
          });
        });
      } else if (type === "object") {
        const objectNodeId = traverse(valueNode, id);

        text.push({
          key,
          value: valueNode.value as NodeRow["value"],
          type,
          childrenCount: Object.keys(valueNode.children ?? {}).length,
          ...(objectNodeId && { to: [objectNodeId] }),
        });

        if (objectNodeId) {
          edges.push({
            id: String(edgeId++),
            from: id,
            to: objectNodeId,
            text: key,
          });
        }
      } else {
        text.push({
          key,
          value: valueNode.value as NodeRow["value"],
          type,
        });
      }
    });

    if (node.parent?.type === "array" && node.type === "object" && node.children?.length === 0) {
      text.push({
        key: null,
        value: "{0 keys}",
        type: "object",
        childrenCount: 0,
      });
    }

    const appendParentKey = () => {
      const getParentKey = (targetNode: Node) => {
        const path = getNodePath(targetNode);
        return path?.pop()?.toString();
      };

      if (!node.parent) {
        return { parentKey: getParentKey(node), parentType: node.type };
      }

      if (node.parent.type === "array") {
        return { parentKey: getParentKey(node.parent), parentType: "array" };
      }

      if (node.parent.type === "property") {
        return { parentKey: getParentKey(node), parentType: "object" };
      }

      return {
        parentKey: getParentKey(node),
        parentType: node.parent.type.replace("property", "object"),
      };
    };

    if (text.length === 0) {
      if (typeof node.value === "undefined") return undefined;

      const { width, height } = calculateNodeSize(node.value as string | number);

      nodes.push({
        id,
        text: [
          {
            key: null,
            value: node.value as NodeRow["value"],
            type: node.type,
          },
        ],
        width,
        height,
        path: getNodePath(node),
        ...appendParentKey(),
      });
    } else {
      let displayText: string | [string, string][] = "";

      if (text.some(row => row.key !== null)) {
        displayText = text.map(row => {
          const keyStr = row.key === null ? "" : row.key;

          if (row.type === "object") return [keyStr, `{${row.childrenCount ?? 0} keys}`];
          if (row.type === "array") return [keyStr, `[${row.childrenCount ?? 0} items]`];
          if (row.value === null) return [keyStr, "null"];

          return [keyStr, `${row.value}`];
        });
      } else {
        displayText = `${text[0].value}`;
      }

      const { width, height } = calculateNodeSize(displayText);

      nodes.push({
        id,
        text,
        width,
        height,
        path: getNodePath(node),
        ...appendParentKey(),
      });
    }

    return id;
  }

  traverse(jsonTree);

  return {
    nodes,
    edges,
    errors: parseErrors,
  };
};
```

## File: `packages/jsoncrack-react/src/theme.ts`
```typescript
import type { CanvasThemeMode } from "./types";

export interface JSONCrackTheme {
  NODE_COLORS: {
    TEXT: string;
    NODE_KEY: string;
    NODE_VALUE: string;
    INTEGER: string;
    NULL: string;
    BOOL: {
      FALSE: string;
      TRUE: string;
    };
    CHILD_COUNT: string;
    DIVIDER: string;
  };
  INTERACTIVE_NORMAL: string;
  BACKGROUND_NODE: string;
  BACKGROUND_MODIFIER_ACCENT: string;
  TEXT_POSITIVE: string;
  GRID_BG_COLOR: string;
  GRID_COLOR_PRIMARY: string;
  GRID_COLOR_SECONDARY: string;
}

export const themes: Record<CanvasThemeMode, JSONCrackTheme> = {
  dark: {
    NODE_COLORS: {
      TEXT: "#DCE5E7",
      NODE_KEY: "#59b8ff",
      NODE_VALUE: "#DCE5E7",
      INTEGER: "#e8c479",
      NULL: "#939598",
      BOOL: {
        FALSE: "#F85C50",
        TRUE: "#00DC7D",
      },
      CHILD_COUNT: "#FFFFFF",
      DIVIDER: "#383838",
    },
    INTERACTIVE_NORMAL: "#b9bbbe",
    BACKGROUND_NODE: "#2B2C3E",
    BACKGROUND_MODIFIER_ACCENT: "rgba(79,84,92,0.48)",
    TEXT_POSITIVE: "hsl(139,calc(var(--saturation-factor, 1)*51.6%),52.2%)",
    GRID_BG_COLOR: "#141414",
    GRID_COLOR_PRIMARY: "#1c1b1b",
    GRID_COLOR_SECONDARY: "#191919",
  },
  light: {
    NODE_COLORS: {
      TEXT: "#000000",
      NODE_KEY: "#761CEA",
      NODE_VALUE: "#535353",
      INTEGER: "#FD0079",
      NULL: "#afafaf",
      BOOL: {
        FALSE: "#FF0000",
        TRUE: "#748700",
      },
      CHILD_COUNT: "#535353",
      DIVIDER: "#e6e6e6",
    },
    INTERACTIVE_NORMAL: "#4f5660",
    BACKGROUND_NODE: "#F6F8FA",
    BACKGROUND_MODIFIER_ACCENT: "rgba(106,116,128,0.24)",
    TEXT_POSITIVE: "#008736",
    GRID_BG_COLOR: "#f7f7f7",
    GRID_COLOR_PRIMARY: "#ebe8e8",
    GRID_COLOR_SECONDARY: "#f2eeee",
  },
};
```

## File: `packages/jsoncrack-react/src/types.ts`
```typescript
import type { JSONPath, Node } from "jsonc-parser";

export interface NodeRow {
  key: string | null;
  value: string | number | null | boolean;
  type: Node["type"];
  childrenCount?: number;
  to?: string[];
}

export interface NodeData {
  id: string;
  text: Array<NodeRow>;
  width: number;
  height: number;
  path?: JSONPath;
  parentKey?: string;
  parentType?: string;
}

export interface EdgeData {
  id: string;
  from: string;
  to: string;
  text: string | null;
}

export interface GraphData {
  nodes: NodeData[];
  edges: EdgeData[];
}

export type LayoutDirection = "LEFT" | "RIGHT" | "DOWN" | "UP";

export type CanvasThemeMode = "light" | "dark";
```

## File: `packages/jsoncrack-react/src/components/Controls.module.css`
```css
.controls {
  position: absolute;
  bottom: 10px;
  left: 10px;
  z-index: 100;
  display: inline-flex;
  align-items: center;
  gap: 6px;
  background: rgba(20, 20, 20, 0.38);
  border: 1px solid rgba(255, 255, 255, 0.18);
  border-radius: 8px;
  padding: 6px;
  backdrop-filter: blur(8px);
}

.button {
  border: none;
  border-radius: 6px;
  cursor: pointer;
  min-width: 30px;
  height: 30px;
  padding: 0 8px;
  font-size: 12px;
  color: #ffffff;
  background: rgba(255, 255, 255, 0.18);
}

.button:hover {
  background: rgba(255, 255, 255, 0.28);
}
```

## File: `packages/jsoncrack-react/src/components/Controls.tsx`
```tsx
import styles from "./Controls.module.css";

interface ControlsProps {
  onFocusRoot: () => void;
  onCenterView: () => void;
  onZoomOut: () => void;
  onZoomIn: () => void;
}

export const Controls = ({ onFocusRoot, onCenterView, onZoomOut, onZoomIn }: ControlsProps) => {
  return (
    <div className={styles.controls}>
      <button
        className={styles.button}
        type="button"
        onClick={onFocusRoot}
        title="Center first node"
      >
        Root
      </button>
      <button className={styles.button} type="button" onClick={onCenterView} title="Fit view">
        Fit
      </button>
      <button className={styles.button} type="button" onClick={onZoomOut} title="Zoom out">
        -
      </button>
      <button className={styles.button} type="button" onClick={onZoomIn} title="Zoom in">
        +
      </button>
    </div>
  );
};
```

## File: `packages/jsoncrack-react/src/components/CustomEdge.tsx`
```tsx
import React from "react";
import type { ViewPort } from "react-zoomable-ui";
import type { EdgeProps } from "reaflow";
import { Edge } from "reaflow";
import type { EdgeData } from "../types";

type QueryRoot = {
  querySelector: (selector: string) => Element | null;
};

type CustomEdgeProps = EdgeProps & {
  viewPort: ViewPort | null;
  edgeTargetById: Map<string, string>;
  hostElement: QueryRoot | null;
};

const isQueryRoot = (value: unknown): value is QueryRoot => {
  return (
    typeof value === "object" &&
    value !== null &&
    "querySelector" in value &&
    typeof (value as QueryRoot).querySelector === "function"
  );
};

const CustomEdgeBase = ({ viewPort, edgeTargetById, hostElement, ...props }: CustomEdgeProps) => {
  const [hovered, setHovered] = React.useState(false);
  const edgeId = (props.properties as EdgeData | undefined)?.id;

  const handleClick = React.useCallback(() => {
    const targetNodeId = edgeId ? edgeTargetById.get(edgeId) : undefined;
    if (!targetNodeId) return;

    const queryRoot = isQueryRoot(hostElement)
      ? hostElement
      : typeof document !== "undefined"
        ? document
        : null;
    if (!queryRoot) return;

    const targetNodeDom = queryRoot.querySelector(
      `[data-id$="node-${targetNodeId}"]`
    ) as HTMLElement | null;

    if (targetNodeDom?.parentElement) {
      viewPort?.camera.centerFitElementIntoView(targetNodeDom.parentElement, {
        elementExtraMarginForZoom: 150,
      });
    }
  }, [hostElement, edgeId, edgeTargetById, viewPort]);

  return (
    <Edge
      containerClassName={`edge-${props.id}`}
      onClick={handleClick}
      onEnter={() => setHovered(true)}
      onLeave={() => setHovered(false)}
      style={{
        stroke: hovered ? "#3B82F6" : "var(--edge-stroke)",
        strokeWidth: 1.5,
      }}
      {...props}
    />
  );
};

export const CustomEdge = React.memo(CustomEdgeBase);
```

## File: `packages/jsoncrack-react/src/components/CustomNode.tsx`
```tsx
import React from "react";
import type { NodeProps } from "reaflow";
import { Node } from "reaflow";
import type { NodeData } from "../types";
import { ObjectNode } from "./ObjectNode";
import { TextNode } from "./TextNode";

type CustomNodeProps = NodeProps<NodeData> & {
  onNodeClick?: (node: NodeData) => void;
};

const CustomNodeBase = ({ onNodeClick, ...nodeProps }: CustomNodeProps) => {
  const handleNodeClick = React.useCallback(
    (_: React.MouseEvent<SVGGElement, MouseEvent>, data: NodeData) => {
      onNodeClick?.(data);
    },
    [onNodeClick]
  );

  return (
    <Node
      {...nodeProps}
      onClick={handleNodeClick as any}
      animated={false}
      label={null as any}
      onEnter={event => {
        event.currentTarget.style.stroke = "#3B82F6";
      }}
      onLeave={event => {
        event.currentTarget.style.stroke = "var(--node-stroke)";
      }}
      style={{
        fill: "var(--node-fill)",
        stroke: "var(--node-stroke)",
        strokeWidth: 1,
      }}
    >
      {({ node, x, y }) => {
        const hasKey = nodeProps.properties.text[0]?.key;
        if (!hasKey) {
          return <TextNode node={nodeProps.properties as NodeData} x={x} y={y} />;
        }

        return <ObjectNode node={node as NodeData} x={x} y={y} />;
      }}
    </Node>
  );
};

export const CustomNode = React.memo(CustomNodeBase);
```

## File: `packages/jsoncrack-react/src/components/Node.module.css`
```css
.foreignObject {
  text-align: center;
  color: var(--node-text);
  font-family:
    ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New",
    monospace;
  font-size: 12px;
  font-weight: 500;
  overflow: hidden;
  pointer-events: none;
}

.objectForeignObject {
  text-align: left;
}

.key {
  display: inline;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.row {
  padding: 3px 10px;
  height: 30px;
  line-height: 24px;
  display: block;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  border-bottom: 1px solid var(--node-divider);
  box-sizing: border-box;
}

.row:last-of-type {
  border-bottom: none;
}

.textNodeWrapper {
  display: flex;
  justify-content: flex-start;
  align-items: center;
  height: 100%;
  width: 100%;
  overflow: hidden;
  padding: 0 10px;
}

.foreignObject:global(.searched) {
  background: rgba(27, 255, 0, 0.1);
  border: 1px solid var(--text-positive);
  border-radius: 2px;
  box-sizing: border-box;
}

.foreignObject :global(.highlight) {
  background: rgba(255, 214, 0, 0.15);
}

.foreignObject:global(.searched) .row {
  border-bottom: 1px solid var(--text-positive);
}
```

## File: `packages/jsoncrack-react/src/components/nodeStyles.ts`
```typescript
type TextColorOptions = {
  type?: string;
  value?: string | number | null | boolean;
};

export const getTextColor = ({ type, value }: TextColorOptions) => {
  if (value === null) return "var(--node-null)";
  if (type === "object") return "var(--node-key)";
  if (type === "number") return "var(--node-integer)";
  if (value === true) return "var(--node-bool-true)";
  if (value === false) return "var(--node-bool-false)";
  return "var(--node-value)";
};
```

## File: `packages/jsoncrack-react/src/components/ObjectNode.tsx`
```tsx
import React from "react";
import type { NodeData } from "../types";
import styles from "./Node.module.css";
import { TextRenderer } from "./TextRenderer";
import { getTextColor } from "./nodeStyles";

type ObjectNodeProps = {
  node: NodeData;
  x: number;
  y: number;
};

type RowProps = {
  row: NodeData["text"][number];
  x: number;
  y: number;
  index: number;
};

const ROW_HEIGHT = 30;

const Row = ({ row, x, y, index }: RowProps) => {
  const rowPosition = index * ROW_HEIGHT;

  const getRowText = () => {
    if (row.type === "object") return `{${row.childrenCount ?? 0} keys}`;
    if (row.type === "array") return `[${row.childrenCount ?? 0} items]`;
    return row.value;
  };

  return (
    <span
      className={styles.row}
      style={{
        color: getTextColor({ value: row.value, type: typeof row.value }),
      }}
      data-key={`${row.key}: ${row.value}`}
      data-x={x}
      data-y={y + rowPosition}
    >
      <span
        className={styles.key}
        style={{ color: getTextColor({ type: "object", value: row.value }) }}
      >
        {row.key}:{" "}
      </span>
      <TextRenderer>{getRowText()}</TextRenderer>
    </span>
  );
};

const ObjectNodeBase = ({ node, x, y }: ObjectNodeProps) => (
  <foreignObject
    className={`${styles.foreignObject} ${styles.objectForeignObject}`}
    data-id={`node-${node.id}`}
    width={node.width}
    height={node.height}
    x={0}
    y={0}
  >
    {node.text.map((row, index) => (
      <Row key={`${node.id}-${index}`} row={row} x={x} y={y} index={index} />
    ))}
  </foreignObject>
);

const areRowTargetsEqual = (prevTargets?: string[], nextTargets?: string[]) => {
  if (prevTargets === nextTargets) return true;
  if (!prevTargets || !nextTargets) return false;
  if (prevTargets.length !== nextTargets.length) return false;

  for (let i = 0; i < prevTargets.length; i += 1) {
    if (prevTargets[i] !== nextTargets[i]) return false;
  }

  return true;
};

const areRowsEqual = (prevRows: NodeData["text"], nextRows: NodeData["text"]) => {
  if (prevRows === nextRows) return true;
  if (prevRows.length !== nextRows.length) return false;

  for (let i = 0; i < prevRows.length; i += 1) {
    const prevRow = prevRows[i];
    const nextRow = nextRows[i];

    if (
      prevRow.key !== nextRow.key ||
      prevRow.value !== nextRow.value ||
      prevRow.type !== nextRow.type ||
      prevRow.childrenCount !== nextRow.childrenCount ||
      !areRowTargetsEqual(prevRow.to, nextRow.to)
    ) {
      return false;
    }
  }

  return true;
};

const propsAreEqual = (prev: ObjectNodeProps, next: ObjectNodeProps) => {
  return (
    prev.node.width === next.node.width &&
    prev.node.height === next.node.height &&
    areRowsEqual(prev.node.text, next.node.text)
  );
};

export const ObjectNode = React.memo(ObjectNodeBase, propsAreEqual);
```

## File: `packages/jsoncrack-react/src/components/TextNode.tsx`
```tsx
import React from "react";
import type { NodeData } from "../types";
import styles from "./Node.module.css";
import { TextRenderer } from "./TextRenderer";
import { getTextColor } from "./nodeStyles";

type TextNodeProps = {
  node: NodeData;
  x: number;
  y: number;
};

const TextNodeBase = ({ node, x, y }: TextNodeProps) => {
  const { text, width, height } = node;
  const firstRow = text[0];

  if (!firstRow) return null;

  const value = firstRow.value;

  return (
    <foreignObject
      className={styles.foreignObject}
      data-id={`node-${node.id}`}
      width={width}
      height={height}
      x={0}
      y={0}
    >
      <span
        className={styles.textNodeWrapper}
        data-x={x}
        data-y={y}
        data-key={JSON.stringify(text)}
      >
        <span className={styles.key} style={{ color: getTextColor({ value, type: typeof value }) }}>
          <TextRenderer>{value}</TextRenderer>
        </span>
      </span>
    </foreignObject>
  );
};

const propsAreEqual = (prev: TextNodeProps, next: TextNodeProps) => {
  return prev.node.text === next.node.text && prev.node.width === next.node.width;
};

export const TextNode = React.memo(TextNodeBase, propsAreEqual);
```

## File: `packages/jsoncrack-react/src/components/TextRenderer.module.css`
```css
.row {
  display: inline-flex;
  align-items: center;
  overflow: hidden;
  gap: 4px;
  vertical-align: middle;
}

.colorPreview {
  width: 12px;
  height: 12px;
  border-radius: 3px;
  display: inline-block;
  border: 1px solid rgba(0, 0, 0, 0.25);
}

.link {
  text-decoration: underline;
  pointer-events: all;
}
```

## File: `packages/jsoncrack-react/src/components/TextRenderer.tsx`
```tsx
import React from "react";
import styles from "./TextRenderer.module.css";

const URL_PATTERN =
  /^(http:\/\/www\.|https:\/\/www\.|http:\/\/|https:\/\/)?[a-z0-9]+([-.]{1}[a-z0-9]+)*\.[a-z]{2,5}(:[0-9]{1,5})?(\/.*)?$/i;
const HEX_CODE_PATTERN = /^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$/;
const RGB_PATTERN = /^rgb\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*\)$/;
const RGBA_PATTERN = /^rgba\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*,\s*(0|1|0\.\d+)\s*\)$/;

const isURL = (word: string) => {
  return URL_PATTERN.test(word);
};

const isColorFormat = (colorString: string) => {
  return (
    HEX_CODE_PATTERN.test(colorString) ||
    RGB_PATTERN.test(colorString) ||
    RGBA_PATTERN.test(colorString)
  );
};

const LinkifiedText = ({ text }: { text: string }) => {
  if (!isURL(text)) return <>{text}</>;

  const href = text.startsWith("http://") || text.startsWith("https://") ? text : `https://${text}`;

  return (
    <a
      className={styles.link}
      onClick={event => event.stopPropagation()}
      href={href}
      target="_blank"
      rel="noopener noreferrer"
    >
      {text}
    </a>
  );
};

export const TextRenderer = ({ children }: React.PropsWithChildren) => {
  if (typeof children === "string" && isColorFormat(children)) {
    return (
      <span className={styles.row}>
        <span className={styles.colorPreview} style={{ backgroundColor: children }} />
        {children}
      </span>
    );
  }

  if (typeof children === "string") {
    return <LinkifiedText text={children} />;
  }

  return <>{`${children}`}</>;
};
```

## File: `packages/jsoncrack-react/src/utils/calculateNodeSize.ts`
```typescript
const NODE_DIMENSIONS = {
  ROW_HEIGHT: 30,
  PARENT_HEIGHT: 36,
} as const;

type Text = number | string | [string, string][];
type Size = { width: number; height: number };

const CACHE_TTL_MS = 120_000;
const sizeCache = new Map<string, Size>();
let lastCacheClearAt = Date.now();

const calculateLines = (text: Text): string => {
  if (Array.isArray(text)) {
    return text.map(([k, v]) => `${k}: ${JSON.stringify(v).slice(0, 80)}`).join("\n");
  }

  return `${text}`;
};

const fallbackSize = (str: string, single: boolean): Size => {
  const lines = str.split("\n");
  const longestLine = lines.reduce((max, line) => Math.max(max, line.length), 0);

  return {
    width: Math.min(700, Math.max(45, longestLine * 8 + 24)),
    height: single ? NODE_DIMENSIONS.PARENT_HEIGHT : lines.length * NODE_DIMENSIONS.ROW_HEIGHT,
  };
};

const calculateWidthAndHeight = (str: string, single = false): Size => {
  if (!str) return { width: 45, height: 45 };

  if (typeof document === "undefined") {
    return fallbackSize(str, single);
  }

  const dummyElement = document.createElement("div");
  dummyElement.style.position = "absolute";
  dummyElement.style.visibility = "hidden";
  dummyElement.style.pointerEvents = "none";
  dummyElement.style.whiteSpace = single ? "nowrap" : "pre-wrap";
  dummyElement.innerText = str;
  dummyElement.style.fontSize = "12px";
  dummyElement.style.width = "fit-content";
  dummyElement.style.padding = "0 10px";
  dummyElement.style.fontWeight = "500";
  dummyElement.style.fontFamily = "monospace";
  document.body.appendChild(dummyElement);

  const clientRect = dummyElement.getBoundingClientRect();
  const lines = str.split("\n").length;

  const width = clientRect.width + 4;
  const height = single ? NODE_DIMENSIONS.PARENT_HEIGHT : lines * NODE_DIMENSIONS.ROW_HEIGHT;

  document.body.removeChild(dummyElement);
  return { width, height };
};

const maybeClearCache = () => {
  if (Date.now() - lastCacheClearAt < CACHE_TTL_MS) return;
  sizeCache.clear();
  lastCacheClearAt = Date.now();
};

export const calculateNodeSize = (text: Text, isParent = false) => {
  maybeClearCache();

  const cacheKey = `${JSON.stringify(text)}-${isParent}`;

  const cached = sizeCache.get(cacheKey);
  if (cached) return cached;

  const lines = calculateLines(text);
  const sizes = calculateWidthAndHeight(lines, typeof text === "string");

  if (isParent) sizes.width += 80;
  if (sizes.width > 700) sizes.width = 700;

  sizeCache.set(cacheKey, sizes);
  return sizes;
};
```


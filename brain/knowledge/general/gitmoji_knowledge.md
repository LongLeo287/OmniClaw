---
id: gitmoji-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:48.368227
---

# KNOWLEDGE EXTRACT: gitmoji
> **Extracted on:** 2026-03-30 22:46:33
> **Source:** gitmoji

---

## File: `.editorconfig`
```
# http://editorconfig.org
root = true

[*]
indent_style = spaces
tab_width = 2
charset = utf-8
trim_trailing_whitespace = true
insert_final_newline = true

[*.md]
trim_trailing_whitespace = false

[*.js]
indent_style = spaces
tab_width = 2
charset = utf-8
trim_trailing_whitespace = true
insert_final_newline = true
```

## File: `.gitignore`
```
.DS_Store
dist/
node_modules/
.publish/
.next
out/
coverage/
.eslintcache
*.log
.pnp.*

# next-pwa
packages/website/public/workbox-*.js
packages/website/public/workbox-*.js
packages/website/public/sw.js
packages/website/public/sw.js
packages/website/public/*.map

# next-sitemap
packages/website/public/robots.txt
packages/website/public/sitemap.xml
packages/website/public/sitemap-*.xml

# gitmojis
packages/website/public/api/

# TS
*.tsbuildinfo

# Turbo
.turbo
```

## File: `.lintstagedrc.json`
```json
{
  "*.json": ["prettier --write"],
  "*.md": ["prettier --write"],
  "*.yml": ["prettier --write"]
}
```

## File: `.node-version`
```
24
```

## File: `AGENTS.md`
```markdown
# Gitmoji Guide for AI Assistants

## Purpose

This guide helps AI assistants understand and use gitmoji convention when creating commits. Using emojis on commit messages provides an easy way of identifying the purpose or intention of a commit with only looking at the emojis used. Gitmoji use emojis to make commit messages more expressive and easier to understand at a glance.

## Official Specification

A gitmoji commit message is composed using the following pieces:

- **intention**: The intention you want to express with the commit, using an emoji from the gitmoji list. Either in the `:shortcode:` or unicode format.
- **scope**: An optional string that adds contextual information for the scope of the change.
- **message**: A brief explanation of the change.

### Format

```
<intention> [scope?][:?] <message>

[optional body]
```

## Gitmoji reference

Fetch all available gitmojis from: https://gitmoji.dev/api/gitmojis.

## Usage Guidelines for AI

### Selecting the correct emoji

1. **Identify the primary purpose** of the commit
2. **Choose the most specific emoji** that matches the change
3. **Use only one emoji** per commit for clarity
4. **Prioritize by impact**: Breaking changes (💥) > Features (✨) > Fixes (🐛) > Refactoring (♻️)

### Examples

```
✨ feat: Add user authentication system

Implement JWT-based authentication with login and registration endpoints.
Closes #123
```

```
🐛 Resolve null pointer exception in user service

Added null check before accessing user properties to prevent crashes.
```

```
📝 docs: Update installation instructions

Added step-by-step guide for setting up the development environment.
```

```
⚡️ Optimize user query with indexing

Reduced query time from 500ms to 50ms by adding composite index.
```

```
💥 Update API response format to REST specification

All API endpoints now return data in a standardized envelope format.
Clients must update their response parsing logic.
```

## Best Practices

1. **Be atomic**: One emoji, one purpose, one commit
2. **Write clear subjects**: Keep under 60 characters, imperative mood
3. **Use the body**: Explain "why" not "what" for complex changes
4. **Reference issues**: Include issue numbers when applicable
5. **Indicate breaking changes**: Use 💥 `:boom:`.

## Resources

- Gitmojis list: https://gitmoji.dev/api/gitmojis
- Gitmoji website: https://gitmoji.dev/
- Gitmoji specification: https://gitmoji.dev/specification
```

## File: `LICENSE`
```
MIT License

Copyright (c) 2016-2022 Carlos Cuesta

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

## File: `package.json`
```json
{
  "name": "gitmoji",
  "private": true,
  "engines": {
    "node": "22",
    "pnpm": ">=8"
  },
  "scripts": {
    "prepare": "husky install",
    "dev": "pnpm turbo --parallel dev"
  },
  "devDependencies": {
    "husky": "^9.1.7",
    "lint-staged": "^16.4.0",
    "prettier": "3.8.1",
    "turbo": "2.8.16"
  },
  "packageManager": "pnpm@8.6.2"
}
```

## File: `pnpm-workspace.yaml`
```yaml
packages:
  - 'packages/*'
```

## File: `README.md`
```markdown
<p align="center">
	<a href="https://gitmoji.dev">
		<img src="https://cloud.githubusercontent.com/assets/7629661/20073135/4e3db2c2-a52b-11e6-85e1-661a8212045a.gif" width="456" alt="gitmoji">
	</a>
</p>
<p align="center">
	<a href="https://github.com/carloscuesta/gitmoji/actions?query=workflow%3ACI+branch%3Amaster">
		<img src="https://img.shields.io/github/actions/workflow/status/carloscuesta/gitmoji/ci.yml?branch=master&style=flat-square"
			 alt="Build Status">
	</a>
	<a href="https://gitmoji.dev">
		<img src="https://img.shields.io/badge/gitmoji-%20😜%20😍-FFDD67.svg?style=flat-square"
			 alt="Gitmoji">
	</a>
</p>

## About

[Gitmoji](https://gitmoji.dev) is an initiative to standardize and explain **the use of emojis on GitHub commit messages**.

**Using emojis** on **commit messages** provides an **easy way** of **identifying the purpose or intention of a commit** with only looking at the emojis used. As there are a lot of different emojis I found the need of creating a guide that can help to use emojis easier.

The gitmojis are published on the [following package](https://www.npmjs.com/package/gitmojis) in order to be used as a dependency 📦.

## Using [gitmoji-cli](https://github.com/carloscuesta/gitmoji-cli)

To use gitmojis from your command line install [gitmoji-cli](https://github.com/carloscuesta/gitmoji-cli). A gitmoji interactive client for using emojis on commit messages.

```bash
npm i -g gitmoji-cli
```

## Example of usage

In case you need some ideas to integrate gitmoji in your project, here's a practical way to use it:

```
<intention> [scope?][:?] <message>
```

- `intention`: An emoji from the list.
- `scope`: An optional string that adds contextual information for the scope of the change.
- `message`: A brief explanation of the change.

## Contributing to gitmoji

Contributing to gitmoji is a piece of :cake:, read the [contributing guidelines](https://github.com/carloscuesta/gitmoji/blob/master/.github/CONTRIBUTING.md). You can discuss emojis using the [issues section](https://github.com/carloscuesta/gitmoji/issues/new). To add a new emoji to the list create an issue and send a pull request, see [how to send a pull request and add a gitmoji](https://github.com/carloscuesta/gitmoji/blob/master/.github/CONTRIBUTING.md#how-to-add-a-gitmoji).

## Spread the word

Are you using Gitmoji on your project? Set the Gitmoji badge on top of your readme using this code:

```html
<a href="https://gitmoji.dev">
  <img
    src="https://img.shields.io/badge/gitmoji-%20😜%20😍-FFDD67.svg?style=flat-square"
    alt="Gitmoji"
  />
</a>
```

## License

The code is available under the [MIT](https://github.com/carloscuesta/gitmoji/blob/master/LICENSE) license.
```

## File: `turbo.json`
```json
{
  "$schema": "https://turbo.build/schema.json",
  "tasks": {
    "dev": {
      "dependsOn": ["^build"],
      "cache": false,
      "persistent": true
    },
    "lint": {
      "dependsOn": ["^build"],
      "outputs": []
    },
    "tscheck": {
      "dependsOn": ["^build"],
      "outputs": []
    },
    "test": {
      "dependsOn": ["^build"],
      "outputs": ["coverage/**"]
    },
    "build": {
      "outputs": [".next/**", "public/**", "dist/**"],
      "dependsOn": ["^build"]
    },
    "publishPackage": {
      "dependsOn": ["^lint"],
      "outputs": []
    }
  }
}
```

## File: `packages/gitmojis/.lintstagedrc.json`
```json
{
  "./src/*.json": ["prettier --write ./src/*.json"],
  "./src/*.ts": ["prettier --write ./src/*.ts"],
  "./src/*.js": ["prettier --write ./src/*.js"]
}
```

## File: `packages/gitmojis/package.json`
```json
{
  "name": "gitmojis",
  "type": "module",
  "version": "3.15.0",
  "description": "An emoji guide for your commit messages.",
  "main": "./dist/index.cjs",
  "types": "./dist/index.d.ts",
  "exports": {
    ".": {
      "import": "./dist/index.mjs",
      "require": "./dist/index.cjs"
    }
  },
  "files": [
    "dist"
  ],
  "scripts": {
    "dev": "nodemon --exec 'pnpm run build' --watch ./src",
    "build": "unbuild",
    "lint:json": "ajv --spec=draft2020 validate -s ./src/schema.json -d ./src/gitmojis.json",
    "lint": "pnpm run lint:json && prettier --check ./src/**/*.{js,json,ts}",
    "publishPackage": "npm publish"
  },
  "devDependencies": {
    "ajv-cli": "^5.0.0",
    "lint-staged": "^16.4.0",
    "nodemon": "^3.1.14",
    "prettier": "3.8.1",
    "unbuild": "^3.6.1"
  },
  "author": {
    "name": "carloscuesta",
    "email": "hi@carloscuesta.me",
    "url": "https://carloscuesta.me"
  },
  "license": "MIT",
  "bugs": {
    "url": "https://github.com/carloscuesta/gitmoji/issues"
  },
  "repository": {
    "type": "git",
    "url": "git+https://github.com/carloscuesta/gitmoji.git"
  },
  "homepage": "https://gitmoji.dev",
  "keywords": [
    "gitmoji",
    "emoji",
    "carloscuesta",
    "commit"
  ],
  "prettier": {
    "semi": false,
    "singleQuote": true,
    "arrowParens": "always"
  }
}
```

## File: `packages/gitmojis/README.md`
```markdown
<p align="center">
	<a href="https://gitmoji.dev">
		<img src="https://cloud.githubusercontent.com/assets/7629661/20073135/4e3db2c2-a52b-11e6-85e1-661a8212045a.gif" width="456" alt="gitmoji">
	</a>
</p>
<p align="center">
	<a href="https://github.com/carloscuesta/gitmoji/actions?query=workflow%3ACI+branch%3Amaster">
		<img src="https://img.shields.io/github/actions/workflow/status/carloscuesta/gitmoji/ci.yml?branch=master&style=flat-square"
			 alt="Build Status">
	</a>
	<a href="https://gitmoji.dev">
		<img src="https://img.shields.io/badge/gitmoji-%20😜%20😍-FFDD67.svg?style=flat-square"
			 alt="Gitmoji">
	</a>
</p>

## About

The emojis from the [gitmoji](https://gitmoji.dev) convention **bundled** into a **node module**.

## Install

```bash
npm i gitmojis
```

## Usage

```js
import { gitmojis } from 'gitmojis'

console.log(gitmojis)

/*
[
  {
    emoji: '🎨',
    entity: '&#x1f3a8;',
    code: ':art:',
    description: 'Improve structure / format of the code.',
    name: 'art',
    semver: null
  },
  {
    emoji: '⚡️',
    entity: '&#x26a1;',
    code: ':zap:',
    description: 'Improve performance.',
    name: 'zap',
    semver: null
  },
  ...
]
*/
```

## API

Alternatively you can also consume this as through HTTP using the API:
  
```bash
curl https://gitmoji.dev/api/gitmojis
```

## Spread the word

Are you using Gitmoji on your project? Set the Gitmoji badge on top of your readme using this code:

```html
<a href="https://gitmoji.dev">
  <img
    src="https://img.shields.io/badge/gitmoji-%20😜%20😍-FFDD67.svg?style=flat-square"
    alt="Gitmoji"
  />
</a>
```
```

## File: `packages/gitmojis/src/gitmojis.json`
```json
{
  "$schema": "https://gitmoji.dev/api/gitmojis/schema",
  "gitmojis": [
    {
      "emoji": "🎨",
      "entity": "&#x1f3a8;",
      "code": ":art:",
      "description": "Improve structure / format of the code.",
      "name": "art",
      "semver": null
    },
    {
      "emoji": "⚡️",
      "entity": "&#x26a1;",
      "code": ":zap:",
      "description": "Improve performance.",
      "name": "zap",
      "semver": "patch"
    },
    {
      "emoji": "🔥",
      "entity": "&#x1f525;",
      "code": ":fire:",
      "description": "Remove code or files.",
      "name": "fire",
      "semver": null
    },
    {
      "emoji": "🐛",
      "entity": "&#x1f41b;",
      "code": ":bug:",
      "description": "Fix a bug.",
      "name": "bug",
      "semver": "patch"
    },
    {
      "emoji": "🚑️",
      "entity": "&#128657;",
      "code": ":ambulance:",
      "description": "Critical hotfix.",
      "name": "ambulance",
      "semver": "patch"
    },
    {
      "emoji": "✨",
      "entity": "&#x2728;",
      "code": ":sparkles:",
      "description": "Introduce new features.",
      "name": "sparkles",
      "semver": "minor"
    },
    {
      "emoji": "📝",
      "entity": "&#x1f4dd;",
      "code": ":memo:",
      "description": "Add or update documentation.",
      "name": "memo",
      "semver": null
    },
    {
      "emoji": "🚀",
      "entity": "&#x1f680;",
      "code": ":rocket:",
      "description": "Deploy stuff.",
      "name": "rocket",
      "semver": null
    },
    {
      "emoji": "💄",
      "entity": "&#ff99cc;",
      "code": ":lipstick:",
      "description": "Add or update the UI and style files.",
      "name": "lipstick",
      "semver": "patch"
    },
    {
      "emoji": "🎉",
      "entity": "&#127881;",
      "code": ":tada:",
      "description": "Begin a project.",
      "name": "tada",
      "semver": null
    },
    {
      "emoji": "✅",
      "entity": "&#x2705;",
      "code": ":white_check_mark:",
      "description": "Add, update, or pass tests.",
      "name": "white-check-mark",
      "semver": null
    },
    {
      "emoji": "🔒️",
      "entity": "&#x1f512;",
      "code": ":lock:",
      "description": "Fix security or privacy issues.",
      "name": "lock",
      "semver": "patch"
    },
    {
      "emoji": "🔐",
      "entity": "&#x1f510;",
      "code": ":closed_lock_with_key:",
      "description": "Add or update secrets.",
      "name": "closed-lock-with-key",
      "semver": null
    },
    {
      "emoji": "🔖",
      "entity": "&#x1f516;",
      "code": ":bookmark:",
      "description": "Release / Version tags.",
      "name": "bookmark",
      "semver": null
    },
    {
      "emoji": "🚨",
      "entity": "&#x1f6a8;",
      "code": ":rotating_light:",
      "description": "Fix compiler / linter warnings.",
      "name": "rotating-light",
      "semver": null
    },
    {
      "emoji": "🚧",
      "entity": "&#x1f6a7;",
      "code": ":construction:",
      "description": "Work in progress.",
      "name": "construction",
      "semver": null
    },
    {
      "emoji": "💚",
      "entity": "&#x1f49a;",
      "code": ":green_heart:",
      "description": "Fix CI Build.",
      "name": "green-heart",
      "semver": null
    },
    {
      "emoji": "⬇️",
      "entity": "⬇️",
      "code": ":arrow_down:",
      "description": "Downgrade dependencies.",
      "name": "arrow-down",
      "semver": "patch"
    },
    {
      "emoji": "⬆️",
      "entity": "⬆️",
      "code": ":arrow_up:",
      "description": "Upgrade dependencies.",
      "name": "arrow-up",
      "semver": "patch"
    },
    {
      "emoji": "📌",
      "entity": "&#x1F4CC;",
      "code": ":pushpin:",
      "description": "Pin dependencies to specific versions.",
      "name": "pushpin",
      "semver": "patch"
    },
    {
      "emoji": "👷",
      "entity": "&#x1f477;",
      "code": ":construction_worker:",
      "description": "Add or update CI build system.",
      "name": "construction-worker",
      "semver": null
    },
    {
      "emoji": "📈",
      "entity": "&#x1F4C8;",
      "code": ":chart_with_upwards_trend:",
      "description": "Add or update analytics or track code.",
      "name": "chart-with-upwards-trend",
      "semver": "patch"
    },
    {
      "emoji": "♻️",
      "entity": "&#x267b;",
      "code": ":recycle:",
      "description": "Refactor code.",
      "name": "recycle",
      "semver": null
    },
    {
      "emoji": "➕",
      "entity": "&#10133;",
      "code": ":heavy_plus_sign:",
      "description": "Add a dependency.",
      "name": "heavy-plus-sign",
      "semver": "patch"
    },
    {
      "emoji": "➖",
      "entity": "&#10134;",
      "code": ":heavy_minus_sign:",
      "description": "Remove a dependency.",
      "name": "heavy-minus-sign",
      "semver": "patch"
    },
    {
      "emoji": "🔧",
      "entity": "&#x1f527;",
      "code": ":wrench:",
      "description": "Add or update configuration files.",
      "name": "wrench",
      "semver": "patch"
    },
    {
      "emoji": "🔨",
      "entity": "&#128296;",
      "code": ":hammer:",
      "description": "Add or update development scripts.",
      "name": "hammer",
      "semver": null
    },
    {
      "emoji": "🌐",
      "entity": "&#127760;",
      "code": ":globe_with_meridians:",
      "description": "Internationalization and localization.",
      "name": "globe-with-meridians",
      "semver": "patch"
    },
    {
      "emoji": "✏️",
      "entity": "&#59161;",
      "code": ":pencil2:",
      "description": "Fix typos.",
      "name": "pencil2",
      "semver": "patch"
    },
    {
      "emoji": "💩",
      "entity": "&#58613;",
      "code": ":poop:",
      "description": "Write bad code that needs to be improved.",
      "name": "poop",
      "semver": null
    },
    {
      "emoji": "⏪️",
      "entity": "&#9194;",
      "code": ":rewind:",
      "description": "Revert changes.",
      "name": "rewind",
      "semver": "patch"
    },
    {
      "emoji": "🔀",
      "entity": "&#128256;",
      "code": ":twisted_rightwards_arrows:",
      "description": "Merge branches.",
      "name": "twisted-rightwards-arrows",
      "semver": null
    },
    {
      "emoji": "📦️",
      "entity": "&#1F4E6;",
      "code": ":package:",
      "description": "Add or update compiled files or packages.",
      "name": "package",
      "semver": "patch"
    },
    {
      "emoji": "👽️",
      "entity": "&#1F47D;",
      "code": ":alien:",
      "description": "Update code due to external API changes.",
      "name": "alien",
      "semver": "patch"
    },
    {
      "emoji": "🚚",
      "entity": "&#1F69A;",
      "code": ":truck:",
      "description": "Move or rename resources (e.g.: files, paths, routes).",
      "name": "truck",
      "semver": null
    },
    {
      "emoji": "📄",
      "entity": "&#1F4C4;",
      "code": ":page_facing_up:",
      "description": "Add or update license.",
      "name": "page-facing-up",
      "semver": null
    },
    {
      "emoji": "💥",
      "entity": "&#x1f4a5;",
      "code": ":boom:",
      "description": "Introduce breaking changes.",
      "name": "boom",
      "semver": "major"
    },
    {
      "emoji": "🍱",
      "entity": "&#1F371",
      "code": ":bento:",
      "description": "Add or update assets.",
      "name": "bento",
      "semver": "patch"
    },
    {
      "emoji": "♿️",
      "entity": "&#9855;",
      "code": ":wheelchair:",
      "description": "Improve accessibility.",
      "name": "wheelchair",
      "semver": "patch"
    },
    {
      "emoji": "💡",
      "entity": "&#128161;",
      "code": ":bulb:",
      "description": "Add or update comments in source code.",
      "name": "bulb",
      "semver": null
    },
    {
      "emoji": "🍻",
      "entity": "&#x1f37b;",
      "code": ":beers:",
      "description": "Write code drunkenly.",
      "name": "beers",
      "semver": null
    },
    {
      "emoji": "💬",
      "entity": "&#128172;",
      "code": ":speech_balloon:",
      "description": "Add or update text and literals.",
      "name": "speech-balloon",
      "semver": "patch"
    },
    {
      "emoji": "🗃️",
      "entity": "&#128451;",
      "code": ":card_file_box:",
      "description": "Perform database related changes.",
      "name": "card-file-box",
      "semver": "patch"
    },
    {
      "emoji": "🔊",
      "entity": "&#128266;",
      "code": ":loud_sound:",
      "description": "Add or update logs.",
      "name": "loud-sound",
      "semver": null
    },
    {
      "emoji": "🔇",
      "entity": "&#128263;",
      "code": ":mute:",
      "description": "Remove logs.",
      "name": "mute",
      "semver": null
    },
    {
      "emoji": "👥",
      "entity": "&#128101;",
      "code": ":busts_in_silhouette:",
      "description": "Add or update contributor(s).",
      "name": "busts-in-silhouette",
      "semver": null
    },
    {
      "emoji": "🚸",
      "entity": "&#128696;",
      "code": ":children_crossing:",
      "description": "Improve user experience / usability.",
      "name": "children-crossing",
      "semver": "patch"
    },
    {
      "emoji": "🏗️",
      "entity": "&#1f3d7;",
      "code": ":building_construction:",
      "description": "Make architectural changes.",
      "name": "building-construction",
      "semver": null
    },
    {
      "emoji": "📱",
      "entity": "&#128241;",
      "code": ":iphone:",
      "description": "Work on responsive design.",
      "name": "iphone",
      "semver": "patch"
    },
    {
      "emoji": "🤡",
      "entity": "&#129313;",
      "code": ":clown_face:",
      "description": "Mock things.",
      "name": "clown-face",
      "semver": null
    },
    {
      "emoji": "🥚",
      "entity": "&#129370;",
      "code": ":egg:",
      "description": "Add or update an easter egg.",
      "name": "egg",
      "semver": "patch"
    },
    {
      "emoji": "🙈",
      "entity": "&#8bdfe7;",
      "code": ":see_no_evil:",
      "description": "Add or update a .gitignore file.",
      "name": "see-no-evil",
      "semver": null
    },
    {
      "emoji": "📸",
      "entity": "&#128248;",
      "code": ":camera_flash:",
      "description": "Add or update snapshots.",
      "name": "camera-flash",
      "semver": null
    },
    {
      "emoji": "⚗️",
      "entity": "&#x2697;",
      "code": ":alembic:",
      "description": "Perform experiments.",
      "name": "alembic",
      "semver": "patch"
    },
    {
      "emoji": "🔍️",
      "entity": "&#128269;",
      "code": ":mag:",
      "description": "Improve SEO.",
      "name": "mag",
      "semver": "patch"
    },
    {
      "emoji": "🏷️",
      "entity": "&#127991;",
      "code": ":label:",
      "description": "Add or update types.",
      "name": "label",
      "semver": "patch"
    },
    {
      "emoji": "🌱",
      "entity": "&#127793;",
      "code": ":seedling:",
      "description": "Add or update seed files.",
      "name": "seedling",
      "semver": null
    },
    {
      "emoji": "🚩",
      "entity": "&#x1F6A9;",
      "code": ":triangular_flag_on_post:",
      "description": "Add, update, or remove feature flags.",
      "name": "triangular-flag-on-post",
      "semver": "patch"
    },
    {
      "emoji": "🥅",
      "entity": "&#x1F945;",
      "code": ":goal_net:",
      "description": "Catch errors.",
      "name": "goal-net",
      "semver": "patch"
    },
    {
      "emoji": "💫",
      "entity": "&#x1f4ab;",
      "code": ":dizzy:",
      "description": "Add or update animations and transitions.",
      "name": "dizzy",
      "semver": "patch"
    },
    {
      "emoji": "🗑️",
      "entity": "&#x1F5D1;",
      "code": ":wastebasket:",
      "description": "Deprecate code that needs to be cleaned up.",
      "name": "wastebasket",
      "semver": "patch"
    },
    {
      "emoji": "🛂",
      "entity": "&#x1F6C2;",
      "code": ":passport_control:",
      "description": "Work on code related to authorization, roles and permissions.",
      "name": "passport-control",
      "semver": "patch"
    },
    {
      "emoji": "🩹",
      "entity": "&#x1FA79;",
      "code": ":adhesive_bandage:",
      "description": "Simple fix for a non-critical issue.",
      "name": "adhesive-bandage",
      "semver": "patch"
    },
    {
      "emoji": "🧐",
      "entity": "&#x1F9D0;",
      "code": ":monocle_face:",
      "description": "Data exploration/inspection.",
      "name": "monocle-face",
      "semver": null
    },
    {
      "emoji": "⚰️",
      "entity": "&#x26B0;",
      "code": ":coffin:",
      "description": "Remove dead code.",
      "name": "coffin",
      "semver": null
    },
    {
      "emoji": "🧪",
      "entity": "&#x1F9EA;",
      "code": ":test_tube:",
      "description": "Add a failing test.",
      "name": "test-tube",
      "semver": null
    },
    {
      "emoji": "👔",
      "entity": "&#128084;",
      "code": ":necktie:",
      "description": "Add or update business logic.",
      "name": "necktie",
      "semver": "patch"
    },
    {
      "emoji": "🩺",
      "entity": "&#x1FA7A;",
      "code": ":stethoscope:",
      "description": "Add or update healthcheck.",
      "name": "stethoscope",
      "semver": null
    },
    {
      "emoji": "🧱",
      "entity": "&#x1f9f1;",
      "code": ":bricks:",
      "description": "Infrastructure related changes.",
      "name": "bricks",
      "semver": null
    },
    {
      "emoji": "🧑‍💻",
      "entity": "&#129489;&#8205;&#128187;",
      "code": ":technologist:",
      "description": "Improve developer experience.",
      "name": "technologist",
      "semver": null
    },
    {
      "emoji": "💸",
      "entity": "&#x1F4B8;",
      "code": ":money_with_wings:",
      "description": "Add sponsorships or money related infrastructure.",
      "name": "money-with-wings",
      "semver": null
    },
    {
      "emoji": "🧵",
      "entity": "&#x1F9F5;",
      "code": ":thread:",
      "description": "Add or update code related to multithreading or concurrency.",
      "name": "thread",
      "semver": null
    },
    {
      "emoji": "🦺",
      "entity": "&#x1F9BA;",
      "code": ":safety_vest:",
      "description": "Add or update code related to validation.",
      "name": "safety-vest",
      "semver": null
    },
    {
      "emoji": "✈️",
      "entity": "&#x2708;",
      "code": ":airplane:",
      "description": "Improve offline support.",
      "name": "airplane",
      "semver": null
    },
    {
      "emoji": "🦖",
      "entity": "&#x2708;",
      "code": ":t-rex:",
      "description": "Code that adds backwards compatibility.",
      "name": "t-rex",
      "semver": null
    }
  ]
}
```

## File: `packages/gitmojis/src/index.d.ts`
```typescript
declare module 'gitmojis' {
  type Gitmoji = {
    /**
     * Gitmoji unicode character
     * @example '🎨', '⚡️', '🔥', '🐛'
     */
    readonly emoji: string
    /**
     * Gitmoji hexadecimal entity.
     * @example '&#x1f3a8;', '&#x26a1;', '&#x1f525;', '&#x1f41b;'
     */
    readonly entity: `&#${string};`
    /**
     * Gitmoji use-case description.
     */
    readonly description: string
    /**
     * Gitmoji name.
     * @example 'art', 'zap', 'fire', 'bug'
     */
    readonly name: string
    /**
     * Gitmoji semver range. Can be `null` if not specified.
     */
    readonly semver: 'patch' | 'minor' | 'major' | null
    /**
     * Gitmoji character formatted as a shortcode.
     * @example ':art:', ':zap:', ':fire:', ':bug:'
     */
    readonly code: `:${string}:`
  }

  export const gitmojis: readonly Gitmoji[]

  export const schema: readonly any
}
```

## File: `packages/gitmojis/src/index.js`
```javascript
import gitmojisJson from './gitmojis.json' assert { type: 'json' }

export { default as schema } from './schema.json' assert { type: 'json' }

export const gitmojis = gitmojisJson.gitmojis
```

## File: `packages/gitmojis/src/schema.json`
```json
{
  "type": "object",
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "required": ["gitmojis"],
  "properties": {
    "gitmojis": {
      "type": "array",
      "minItems": 1,
      "uniqueItems": true,
      "items": {
        "type": "object",
        "required": [
          "emoji",
          "entity",
          "code",
          "description",
          "name",
          "semver"
        ],
        "properties": {
          "code": {
            "type": "string"
          },
          "entity": {
            "type": "string"
          },
          "description": {
            "type": "string"
          },
          "emoji": {
            "type": "string"
          },
          "name": {
            "type": "string"
          },
          "semver": {
            "enum": ["major", "minor", "patch", null]
          }
        }
      }
    }
  }
}
```

## File: `packages/website/.lintstagedrc.json`
```json
{
  "./src/**/*.{ts,tsx,css}": [
    "eslint --cache --fix",
    "prettier --write ./src/**/*.{ts,tsx,css}"
  ]
}
```

## File: `packages/website/eslint.config.mjs`
```
import { FlatCompat } from '@eslint/eslintrc'
import js from '@eslint/js'
import typescriptParser from '@typescript-eslint/parser'
import typescriptPlugin from '@typescript-eslint/eslint-plugin'
import reactPlugin from 'eslint-plugin-react'
import importPlugin from 'eslint-plugin-import'
import nextPlugin from '@next/eslint-plugin-next'
import prettierConfig from 'eslint-config-prettier'
import path from 'path'
import { fileURLToPath } from 'url'

const __filename = fileURLToPath(import.meta.url)
const __dirname = path.dirname(__filename)

const compat = new FlatCompat({
  baseDirectory: __dirname,
})

export default [
  js.configs.recommended,
  ...compat.extends('plugin:@typescript-eslint/recommended'),
  prettierConfig,
  {
    files: ['**/*.{js,mjs,cjs,ts,tsx}'],
    languageOptions: {
      parser: typescriptParser,
      parserOptions: {
        ecmaVersion: 12,
        sourceType: 'module',
        ecmaFeatures: {
          jsx: true,
        },
      },
      globals: {
        React: 'readonly',
        JSX: 'readonly',
        window: 'readonly',
        document: 'readonly',
        navigator: 'readonly',
        console: 'readonly',
        process: 'readonly',
        __dirname: 'readonly',
        __filename: 'readonly',
        module: 'readonly',
        require: 'readonly',
        jest: 'readonly',
        describe: 'readonly',
        it: 'readonly',
        test: 'readonly',
        expect: 'readonly',
        beforeAll: 'readonly',
        beforeEach: 'readonly',
        afterAll: 'readonly',
        afterEach: 'readonly',
      },
    },
    plugins: {
      '@typescript-eslint': typescriptPlugin,
      react: reactPlugin,
      import: importPlugin,
      '@next/next': nextPlugin,
    },
    settings: {
      react: {
        version: 'detect',
      },
      'import/resolver': {
        typescript: true,
        node: true,
        alias: {
          map: [['src', './src']],
        },
      },
    },
    rules: {
      'react/react-in-jsx-scope': 'off',
      '@next/next/no-img-element': 'off',
      'react/no-unknown-property': [
        'error',
        {
          ignore: ['jsx', 'global'],
        },
      ],
      'import/order': [
        'error',
        {
          groups: [
            ['builtin', 'external'],
            ['internal', 'parent', 'sibling', 'index'],
          ],
          'newlines-between': 'always',
        },
      ],
    },
  },
]
```

## File: `packages/website/jest.config.js`
```javascript
const nextJest = require('next/jest')

const createJestConfig = nextJest({ dir: './' })

async function jestConfig() {
  const nextJestConfig = await createJestConfig({
    "collectCoverageFrom": [
      "src/**/*.{ts,tsx}",
    ],
    "testMatch": [
      "**/*.(spec).(ts)",
      "**/*.(spec).(tsx)"
    ],
    "moduleNameMapper": {
      "src/(.*)$": "<rootDir>/src/$1",
      "\\.svg$": "<rootDir>/__mocks__/svg.js"
    },
    "testEnvironment": "jsdom",
    "setupFilesAfterEnv": ["<rootDir>/jest.setup.js"],
    "reporters": [
      "default",
      "github-actions"
    ]
  })()

  // Add ignores for specific ESM packages so they are transformed by Jest
  // See: https://github.com/vercel/next.js/issues/35634
  nextJestConfig.transformIgnorePatterns[0] = '/node_modules/(!@vercel/analytics)/'

  return nextJestConfig
}

module.exports = jestConfig
```

## File: `packages/website/jest.d.ts`
```typescript
/// <reference types="@testing-library/jest-dom" />
```

## File: `packages/website/jest.setup.js`
```javascript
import '@testing-library/jest-dom'
import React from 'react'

// Mock next/dynamic to load components synchronously in tests
jest.mock('next/dynamic', () => ({
  __esModule: true,
  default: (...args) => {
    const dynamicModule = jest.requireActual('next/dynamic')
    const dynamicActualComp = dynamicModule.default
    const RequiredComponent = dynamicActualComp(args[0])
    RequiredComponent.preload ? RequiredComponent.preload() : RequiredComponent.render.preload()
    return RequiredComponent
  },
}))

// Mock matchMedia for components that use it
Object.defineProperty(window, 'matchMedia', {
  writable: true,
  value: jest.fn().mockImplementation((query) => ({
    matches: false,
    media: query,
    onchange: null,
    addListener: jest.fn(),
    removeListener: jest.fn(),
    addEventListener: jest.fn(),
    removeEventListener: jest.fn(),
    dispatchEvent: jest.fn(),
  })),
})

// Silence known React/JSDOM warnings in tests that don't affect functionality
const originalError = console.error
beforeAll(() => {
  console.error = (...args) => {
    // Suppress SVG element warnings - these are JSDOM limitations, not actual errors
    // The SVG elements work fine in real browsers
    if (
      typeof args[0] === 'string' &&
      (args[0].includes('The tag <') && args[0].includes('is unrecognized in this browser'))
    ) {
      return
    }
    originalError.call(console, ...args)
  }
})

afterAll(() => {
  console.error = originalError
})

// Mock SVG namespace attributes for JSDOM
// JSDOM doesn't fully support SVG namespaced attributes like xlink:href
const originalCreateElement = document.createElement.bind(document)
const originalCreateElementNS = document.createElementNS.bind(document)

document.createElement = function (tagName, options) {
  const element = originalCreateElement(tagName, options)
  if (tagName.toLowerCase() === 'svg') {
    element.setAttribute = function (name, value) {
      if (name === 'xlinkHref') {
        this.setAttributeNS('http://www.w3.org/1999/xlink', 'xlink:href', value)
      } else {
        Element.prototype.setAttribute.call(this, name, value)
      }
    }
  }
  return element
}

document.createElementNS = function (namespaceURI, qualifiedName) {
  const element = originalCreateElementNS(namespaceURI, qualifiedName)
  if (namespaceURI === 'http://www.w3.org/2000/svg') {
    element.setAttribute = function (name, value) {
      if (name === 'xlinkHref') {
        this.setAttributeNS('http://www.w3.org/1999/xlink', 'xlink:href', value)
      } else {
        Element.prototype.setAttribute.call(this, name, value)
      }
    }
  }
  return element
}
```

## File: `packages/website/jsconfig.json`
```json
{
  "compilerOptions": {
    "baseUrl": "."
  }
}
```

## File: `packages/website/next-env.d.ts`
```typescript
/// <reference types="next" />
/// <reference types="next/image-types/global" />
import "./.next/types/routes.d.ts";

// NOTE: This file should not be edited
// see https://nextjs.org/docs/app/api-reference/config/typescript for more information.
```

## File: `packages/website/next-sitemap.config.js`
```javascript
/** @type {import('next-sitemap').IConfig} */
module.exports = {
  siteUrl: 'https://gitmoji.dev',
  generateRobotsTxt: true,
}
```

## File: `packages/website/next-sitemap.js`
```javascript
module.exports = {
  siteUrl: 'https://gitmoji.dev',
  generateRobotsTxt: true,
}
```

## File: `packages/website/next.config.js`
```javascript
module.exports = {
  reactStrictMode: true,
  output: 'export',
}
```

## File: `packages/website/package.json`
```json
{
  "name": "website",
  "private": true,
  "version": "1.0.0",
  "engines": {
    "node": "24"
  },
  "scripts": {
    "build": "node scripts/generate-api.js && next build && next-sitemap",
    "tscheck": "pnpm exec tsc --noEmit",
    "dev": "next dev",
    "lint": "eslint ./src && prettier --check ./src/**/*.{ts,tsx,css}",
    "start": "next start",
    "test": "FORCE_COLOR=1 jest --coverage"
  },
  "devDependencies": {
    "@eslint/eslintrc": "3.3.3",
    "@eslint/js": "10.0.1",
    "@next/eslint-plugin-next": "16.1.6",
    "@testing-library/jest-dom": "6.9.1",
    "@testing-library/react": "16.3.2",
    "@testing-library/user-event": "14.6.1",
    "@types/fetch-mock": "^7.3.8",
    "@types/jest": "^29.5.14",
    "@types/react": "^19.2.14",
    "@typescript-eslint/eslint-plugin": "^8.57.2",
    "@typescript-eslint/parser": "^8.57.2",
    "clipboard": "^2.0.11",
    "eslint": "^9.39.2",
    "eslint-config-next": "^16.1.6",
    "eslint-config-prettier": "^10.1.8",
    "eslint-import-resolver-alias": "^1.1.2",
    "eslint-import-resolver-typescript": "^4.4.4",
    "eslint-plugin-import": "^2.32.0",
    "eslint-plugin-jest": "^29.12.1",
    "eslint-plugin-react": "^7.37.5",
    "focus-trap-react": "^12.0.0",
    "gitmojis": "workspace:*",
    "jest": "^29.7.0",
    "jest-environment-jsdom": "^30.2.0",
    "jest-fetch-mock": "^3.0.3",
    "lint-staged": "^16.4.0",
    "next": "^16.1.7",
    "next-sitemap": "^4.2.3",
    "next-themes": "^0.4.6",
    "node-mocks-http": "^1.17.2",
    "prettier": "3.8.1",
    "prop-types": "^15.8.1",
    "react": "^19.2.4",
    "react-dom": "^19.2.4",
    "react-hot-toast": "^2.5.2",
    "typescript": "^5.9.3"
  },
  "author": {
    "name": "carloscuesta",
    "email": "hi@carloscuesta.me",
    "url": "https://carloscuesta.me"
  },
  "license": "MIT",
  "bugs": {
    "url": "https://github.com/carloscuesta/gitmoji/issues"
  },
  "repository": {
    "type": "git",
    "url": "git+https://github.com/carloscuesta/gitmoji.git"
  },
  "homepage": "https://gitmoji.dev",
  "keywords": [
    "gitmoji",
    "emoji",
    "carloscuesta",
    "commit"
  ],
  "prettier": {
    "semi": false,
    "singleQuote": true,
    "arrowParens": "always"
  }
}
```

## File: `packages/website/tsconfig.json`
```json
{
  "compilerOptions": {
    "baseUrl": ".",
    "target": "es6",
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
    "incremental": true,
    "esModuleInterop": true,
    "module": "esnext",
    "moduleResolution": "node",
    "resolveJsonModule": true,
    "isolatedModules": true,
    "jsx": "react-jsx",
    "plugins": [
      {
        "name": "next"
      }
    ]
  },
  "include": [
    "next-env.d.ts",
    "**/*.ts",
    "**/*.tsx",
    ".next/types/**/*.ts",
    ".next/dev/types/**/*.ts"
  ],
  "exclude": [
    "node_modules"
  ]
}
```

## File: `packages/website/public/_redirects`
```
/api/gitmojis  /api/gitmojis/index.json  200
```

## File: `packages/website/public/static/browserconfig.xml`
```xml
<?xml version="1.0" encoding="utf-8"?>
<browserconfig><msapplication><tile><square70x70logo src="/static/ms-icon-70x70.png"/><square150x150logo src="/static/ms-icon-150x150.png"/><square310x310logo src="/static/ms-icon-310x310.png"/><TileColor>#ffffff</TileColor></tile></msapplication></browserconfig>
```

## File: `packages/website/public/static/manifest.json`
```json
{
  "name": "Gitmoji",
  "display": "minimal-ui",
  "start_url": "/",
  "theme_color": "#FFDD67",
  "background_color": "#FFF",
  "icons": [
    {
      "src": "/static/android-icon-36x36.png",
      "sizes": "36x36",
      "type": "image/png",
      "density": "0.75"
    },
    {
      "src": "/static/android-icon-48x48.png",
      "sizes": "48x48",
      "type": "image/png",
      "density": "1.0"
    },
    {
      "src": "/static/android-icon-72x72.png",
      "sizes": "72x72",
      "type": "image/png",
      "density": "1.5"
    },
    {
      "src": "/static/android-icon-96x96.png",
      "sizes": "96x96",
      "type": "image/png",
      "density": "2.0"
    },
    {
      "src": "/static/android-icon-144x144.png",
      "sizes": "144x144",
      "type": "image/png",
      "density": "3.0"
    },
    {
      "src": "/static/android-icon-192x192.png",
      "sizes": "192x192",
      "type": "image/png",
      "density": "4.0"
    },
    {
      "src": "/static/android-icon-512x512.png",
      "sizes": "512x512",
      "type": "image/png",
      "density": "4.0"
    },
    {
      "src": "/static/maskable_icon.png",
      "sizes": "192x192",
      "type": "image/png",
      "purpose": "maskable"
    }
  ]
}
```

## File: `packages/website/public/static/opensearchdescription.xml`
```xml
<?xml version="1.0" encoding="UTF-8"?>
<OpenSearchDescription xmlns="http://a9.com/-/spec/opensearch/1.1/">
  <ShortName>Gitmoji</ShortName>
  <Description>An emoji guide for your commit messages.</Description>
  <Tags>gitmoji emoji git</Tags>
  <Image height="16" width="16" type="image/png">https://gitmoji.dev/static/favicon-16x16.png</Image>
  <Image height="32" width="32" type="image/png">https://gitmoji.dev/static/favicon-32x32.png</Image>
  <Image height="96" width="96" type="image/png">https://gitmoji.dev/static/favicon-96x96.png</Image>
  <Url type="text/html" template="https://gitmoji.dev/?search={searchTerms}"/>
</OpenSearchDescription>
```

## File: `packages/website/scripts/generate-api.js`
```javascript
const { gitmojis } = require('gitmojis')
const fs = require('fs')
const path = require('path')

const outputDir = path.join(__dirname, '../public/api/gitmojis')
fs.mkdirSync(outputDir, { recursive: true })
fs.writeFileSync(
  path.join(outputDir, 'index.json'),
  JSON.stringify({ gitmojis }, null, 2)
)

console.log('Generated static API at public/api/gitmojis/index.json')
```

## File: `packages/website/src/app/layout.tsx`
```tsx
import type { Metadata } from 'next'
import { ThemeProvider } from 'next-themes'

import Layout from 'src/components/Layout'
import 'src/utils/theme/theme.css'

export const metadata: Metadata = {
  title: 'gitmoji | An emoji guide for your commit messages',
  description:
    "Gitmoji is an emoji guide for your commit messages. Aims to be a standarization cheatsheet for using emojis on GitHub's commit messages.",
  authors: [{ name: 'Carlos Cuesta', url: 'https://carloscuesta.me' }],
  keywords: ['gitmoji', 'emoji', 'carloscuesta', 'commit'],
  metadataBase: new URL('https://gitmoji.dev'),
  alternates: {
    canonical: '/',
  },
  robots: 'index, follow',
  openGraph: {
    title: 'gitmoji',
    description: 'An emoji guide for your commit messages.',
    url: 'https://gitmoji.dev',
    images: [
      {
        url: 'https://gitmoji.dev/static/gitmoji.gif',
      },
    ],
  },
  twitter: {
    card: 'summary',
    title: 'gitmoji',
    description: 'An emoji guide for your commit messages.',
    creator: '@crloscuesta',
    images: ['https://gitmoji.dev/static/gitmoji.gif'],
  },
  icons: {
    icon: [
      { url: '/static/favicon-16x16.png', sizes: '16x16', type: 'image/png' },
      { url: '/static/favicon-32x32.png', sizes: '32x32', type: 'image/png' },
      { url: '/static/favicon-96x96.png', sizes: '96x96', type: 'image/png' },
      {
        url: '/static/android-icon-192x192.png',
        sizes: '192x192',
        type: 'image/png',
      },
    ],
    apple: [
      { url: '/static/apple-icon-57x57.png', sizes: '57x57' },
      { url: '/static/apple-icon-60x60.png', sizes: '60x60' },
      { url: '/static/apple-icon-72x72.png', sizes: '72x72' },
      { url: '/static/apple-icon-76x76.png', sizes: '76x76' },
      { url: '/static/apple-icon-114x114.png', sizes: '114x114' },
      { url: '/static/apple-icon-120x120.png', sizes: '120x120' },
      { url: '/static/apple-icon-144x144.png', sizes: '144x144' },
      { url: '/static/apple-icon-152x152.png', sizes: '152x152' },
      { url: '/static/apple-icon-180x180.png', sizes: '180x180' },
    ],
  },
  manifest: '/static/manifest.json',
  other: {
    'msapplication-TileColor': '#FFDD67',
    'msapplication-TileImage': '/ms-icon-144x144.png',
    'google-site-verification': '78vmlhi_erc-UGybxcGwHyiUtf04wzYExTLa-4LoWio',
  },
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en" suppressHydrationWarning>
      <head>
        <meta name="theme-color" content="#FFDD67" />
        <link
          rel="search"
          type="application/opensearchdescription+xml"
          href="/static/opensearchdescription.xml"
        />
        <script
          type="text/javascript"
          dangerouslySetInnerHTML={{
            __html: `(function(a,e,f,g,b,c,d){a.GoogleAnalyticsObject=b;a[b]=a[b]||function(){(a[b].q=a[b].q||[]).push(arguments)};a[b].l=1*new Date;c=e.createElement(f);d=e.getElementsByTagName(f)[0];c.async=1;c.src=g;d.parentNode.insertBefore(c,d)})(window,document,"script","//www.google-analytics.com/analytics.js","ga");ga("create","UA-67824860-7","auto");ga("send","pageview");`,
          }}
        />
      </head>
      <body>
        <ThemeProvider attribute="data-theme" defaultTheme="light">
          <Layout>{children}</Layout>
        </ThemeProvider>
      </body>
    </html>
  )
}
```

## File: `packages/website/src/app/page.tsx`
```tsx
import { Toaster } from 'react-hot-toast'
import { gitmojis } from 'gitmojis'

import GitmojiList from 'src/components/GitmojiList'
import CarbonAd from 'src/components/CarbonAd'

export default function Home() {
  return (
    <main>
      <CarbonAd />
      <GitmojiList gitmojis={gitmojis} />
      <Toaster position="top-left" />
    </main>
  )
}
```

## File: `packages/website/src/app/about/page.tsx`
```tsx
import type { Metadata } from 'next'
import Link from 'next/link'

import CarbonAd from 'src/components/CarbonAd'

export const metadata: Metadata = {
  title: 'gitmoji | About | An emoji guide for your commit messages',
  alternates: {
    canonical: '/about',
  },
}

export default function About() {
  return (
    <main>
      <CarbonAd />
      <section>
        <h1>About</h1>

        <p>
          <strong>Gitmoji is an emoji guide for GitHub commit messages</strong>.
          Aims to be a standarization cheatsheet - guide for using emojis on
          GitHub&#39;s commit messages.
        </p>

        <p>
          <strong>Using emojis</strong> on <strong>commit messages</strong>{' '}
          provides an <strong>easy way</strong> of{' '}
          <strong>identifying the purpose or intention of a commit</strong> with
          only looking at the emojis used. As there are a lot of different
          emojis I found the need of creating a guide that can help to use
          emojis easier.
        </p>

        <p>
          This project is Open Source, that means everyone can participate,
          suggesting, discussing and adding new emojis. Take a look at the{' '}
          <Link href="#contributing-gitmoji">contributing section</Link> and{' '}
          <a href="https://github.com/carloscuesta/gitmoji/blob/master/.github/CONTRIBUTING.md">
            guidelines for contributing
          </a>
          .
        </p>
      </section>

      <section>
        <h1>
          Using gitmoji with{' '}
          <a href="https://github.com/carloscuesta/gitmoji-cli">gitmoji-cli</a>
        </h1>

        <p>
          An easy solution for using gitmoji from your command line, is to
          install{' '}
          <a href="https://github.com/carloscuesta/gitmoji-cli">gitmoji-cli</a>.
          A gitmoji interactive client for using emojis on commit messages.
        </p>

        <pre className="overflow-x-adjust">
          <code>$ npm i -g gitmoji-cli</code>
        </pre>
      </section>

      <section>
        <h1 id="specification">Specification</h1>

        <p>
          To understand how to use gitmoji properly, please check the official
          specification <Link href="/specification">here</Link> 👈.
        </p>
      </section>

      <section>
        <h1 id="contributing-gitmoji">Contributing to gitmoji</h1>

        <p>
          Contributing to gitmoji is a piece of 🍰! This project is a static
          website built with <i>Next.js</i>. All the gitmojis displayed are
          rendered from a JSON file. Before submitting any pull request, please
          follow these steps:
        </p>

        <ol>
          <li>
            <a href="https://github.com/carloscuesta/gitmoji/issues/new">
              Create an issue
            </a>{' '}
            filling the template.
          </li>
          <li>
            After discussing the idea, feature or suggestion,{' '}
            <a href="https://github.com/carloscuesta/gitmoji/blob/master/.github/CONTRIBUTING.md">
              read the contribution docs.
            </a>
          </li>
          <li>
            <a href="https://github.com/carloscuesta/gitmoji/fork">
              Create a fork{' '}
            </a>
            of gitmoji.
          </li>
          <li>
            Create a new branch with the feature name. (Eg: add-emoji-deploy,
            fix-website-header)
          </li>
          <li>
            Make your changes and send a{' '}
            <a href="https://help.github.com/articles/creating-a-pull-request/">
              pull request{' '}
            </a>
            .
          </li>
        </ol>
      </section>
    </main>
  )
}
```

## File: `packages/website/src/app/contributors/page.tsx`
```tsx
import type { Metadata } from 'next'

import ContributorsList from 'src/components/ContributorsList'
import CarbonAd from 'src/components/CarbonAd'

export const metadata: Metadata = {
  title: 'gitmoji | Contributors | An emoji guide for your commit messages',
  alternates: {
    canonical: '/contributors',
  },
}

type Contributor = {
  avatar: string
  id: string
  url: string
}

type GitHubContributor = {
  avatar_url: string
  id: string
  html_url: string
  login: string
}

async function getContributors(): Promise<Contributor[]> {
  const response = await fetch(
    'https://api.github.com/repos/carloscuesta/gitmoji/contributors',
    { next: { revalidate: 3600 * 3 } },
  )
  const contributors: GitHubContributor[] = await response.json()

  return contributors
    .filter((contributor) => !contributor.login.includes('bot'))
    .map((contributor) => ({
      avatar: contributor.avatar_url,
      id: contributor.id,
      url: contributor.html_url,
    }))
}

export default async function Contributors() {
  const contributors = await getContributors()

  return (
    <main>
      <CarbonAd />
      <section>
        <h1>Contributors</h1>

        <ContributorsList contributors={contributors} />
      </section>
    </main>
  )
}
```

## File: `packages/website/src/app/related-tools/page.tsx`
```tsx
import type { Metadata } from 'next'

import CarbonAd from 'src/components/CarbonAd'

export const metadata: Metadata = {
  title: 'gitmoji | Related tools | An emoji guide for your commit messages',
  alternates: {
    canonical: '/related-tools',
  },
}

const tools = [
  {
    name: 'gitmoji-changelog',
    description: 'A changelog generator for gitmoji.',
    link: 'https://github.com/frinyvonnick/gitmoji-changelog/',
  },
  {
    name: 'gitmemoji',
    description: 'A game to learn gitmojis.',
    link: 'https://github.com/ImBIOS/gitmemoji/',
  },
  {
    name: 'gitmoji-browser-extension',
    description: 'The Gitmoji extension to easily search and copy gitmojis.',
    link: 'https://github.com/johannchopin/gitmoji-browser-extension',
  },
  {
    name: 'gitmoji-vscode',
    description: 'Gitmoji tool for git commit messages in VS Code',
    link: 'https://github.com/seatonjiang/gitmoji-vscode',
  },
  {
    name: 'gitmoji-intellij-plugin',
    description:
      'A Jetbrains suite plugin to easily add gitmoji when committing',
    link: 'https://plugins.jetbrains.com/plugin/12383-gitmoji-plus-commit-button',
  },
  {
    name: 'gitmoji-sublimetext',
    description: 'A Sublime Text plugin to add emojis in git commit messages.',
    link: 'https://packagecontrol.io/packages/Gitmoji',
  },
  {
    name: 'gitimoji',
    description: 'A Gitmoji App for macOS.',
    link: 'https://github.com/TimoZacherl/gitimoji',
  },
  {
    name: 'gitmoji-atom',
    description: 'Gitmoji for Atom',
    link: 'https://github.com/ThatXliner/gitmoji-atom',
  },
  {
    name: 'gitmoji-regex',
    description: 'A Gitmoji::Regex for Ruby.',
    link: 'https://github.com/pboling/gitmoji-regex',
  },
  {
    name: 'traymoji',
    description: 'A Electron Tray App for Gitmojis',
    link: 'https://github.com/CoenWarmer/traymoji',
  },
  {
    name: 'alfred-gitmoji',
    description: 'Gitmoji Workflow for Alfred',
    link: 'https://github.com/techouse/alfred-gitmoji',
  },
  {
    name: 'gitmojiapp',
    description: 'A Flutter Gitmoji App for macOS, Linux, and Windows',
    link: 'https://github.com/patrick-fu/GitmojiApp',
  },
  {
    name: 'githubmoji',
    description:
      'A Firefox addon that adds a predictive gitmoji picker to GitHub commit message inputs.',
    link: 'https://github.com/ma1ted/githubmoji',
  },
  {
    name: 'gitmoji-changelog-action',
    description: 'GitHub Action for gitmoji-changelog',
    link: 'https://github.com/sercanuste/gitmoji-changelog-action',
  },
  {
    name: 'raycast-gitmoji-search',
    description: 'Gitmoji extension for Raycast',
    link: 'https://www.raycast.com/ricoberger/gitmoji',
  },
  {
    name: 'gitmoji-fuzzy-hook',
    description:
      'Fuzzy finder git-commit-hook for prepending a gitmoji (cmd & GUI).',
    link: 'https://gitlab.com/raabf/gitmoji-fuzzy-hook',
  },
  {
    name: 'genmoji',
    description: 'Gitmoji commit message generation using AI',
    link: 'https://github.com/segersniels/genmoji',
  },
  {
    name: 'gitmoji-plus-flow-launcher',
    description: 'A flow launcher plugin to search and copy gitmojis',
    link: 'https://github.com/tho-myr/Flow.Launcher.Plugin.Gitmoji_Plus',
  },
]

export default function RelatedTools() {
  return (
    <main>
      <CarbonAd />
      <section>
        <h1>Related tools</h1>

        <p>
          This is a list of tools which are related with the <b>gitmoji</b>{' '}
          convention.
        </p>

        <ul>
          {tools.map((tool) => (
            <li key={tool.name}>
              <a href={tool.link} target="_blank" rel="noopener noreferrer">
                <b>{tool.name}</b>
              </a>
              {`: ${tool.description}`}
            </li>
          ))}
        </ul>
      </section>
    </main>
  )
}
```

## File: `packages/website/src/app/specification/page.tsx`
```tsx
import type { Metadata } from 'next'
import Link from 'next/link'

import CarbonAd from 'src/components/CarbonAd'

export const metadata: Metadata = {
  title: 'gitmoji | Specification | An emoji guide for your commit messages',
  alternates: {
    canonical: '/specification',
  },
}

export default function Specification() {
  return (
    <main>
      <CarbonAd />
      <section>
        <h1 id="specification">Specification</h1>

        <p>
          You can extend Gitmoji and make it your own, but in case you want to
          follow the official specification, please continue reading 👀
        </p>

        <p>
          A gitmoji commit message consists is composed using the following
          pieces:
        </p>

        <ul>
          <li>
            <b>intention</b>: The intention you want to express with the commit,
            using an emoji from the <Link href="/">list</Link>. Either in the
            :shortcode: or unicode format.
          </li>
          <li>
            <b>scope</b>: An optional string that adds contextual information
            for the scope of the change.
          </li>
          <li>
            <b>message</b>: A brief explanation of the change.
          </li>
        </ul>

        <pre className="overflow-x-adjust">
          <code>&lt;intention&gt; [scope?][:?] &lt;message&gt;</code>
        </pre>
      </section>

      <section>
        <h1 id="specification-examples">Examples</h1>

        <ul>
          <li>⚡️ Lazyload home screen images.</li>
          <li>🐛 Fix `onClick` event handler</li>
          <li>🔖 Bump version `1.2.0`</li>
          <li>♻️ (components): Transform classes to hooks</li>
          <li>📈 Add analytics to the dashboard</li>
          <li>🌐 Support Japanese language</li>
          <li>♿️ (account): Improve modals a11y</li>
        </ul>
      </section>

      <section>
        <h1 id="shortcode-vs-unicode-format">Shortcode vs Unicode format</h1>

        <p>
          You&#39;ll notice that when using emojis in commits, it&#39;s possible
          to use either the shortcode or the unicode format.
        </p>

        <p>
          The difference between both is that the unicode represents the emoji
          itself while the shortcode is a text representation of the emoji that
          will be converted to the unicode character when rendered on a Git
          platform, such as GitHub, GitLab etc.
        </p>

        <p>
          Both approaches are completely fine, you can choose the one you&#39;re
          most comfortable and suits you best. Let&#39;s understand the pros and
          cons of each approach so you can decide on it:
        </p>

        <h2>Unicode</h2>

        <h3>Pros ✅</h3>

        <ul>
          <li>
            It represents the actual emoji no external systems are needed.
          </li>
          <li>Better git log.</li>
          <li>Easier to type.</li>
          <li>Takes less characters of the commit title.</li>
        </ul>

        <h3>Cons ❌</h3>
        <ul>
          <li>Might not be supported in all terminals / operating systems.</li>
        </ul>

        <h2>Shortcode</h2>
        <h3>Pros ✅</h3>
        <ul>
          <li>
            Supported everywhere as it&#39;s a text representation of the emoji.
          </li>
        </ul>
        <h3>Cons ❌</h3>
        <ul>
          <li>
            You&#39;ll need a platform / system that knows how to properly
            render the shortcode.
          </li>
          <li>
            Different platforms / systems might use different shortcode namings,
            eg: GitHub and GitLab have some differences.
          </li>
          <li>Takes more characters of the commit title.</li>
        </ul>
      </section>
    </main>
  )
}
```

## File: `packages/website/src/components/Button/index.tsx`
```tsx
import Icon from 'src/components/Icon'
import styles from './styles.module.css'

type Props = { target?: string; icon?: string; text: string; link: string }

const Button = (props: Props) => (
  <a
    className={styles.button}
    target={props.target && props.target}
    href={props.link}
  >
    {props.icon && <Icon name={props.icon} />}
    {props.text}
  </a>
)

export default Button
```

## File: `packages/website/src/components/Button/styles.module.css`
```css
.button {
  border-radius: 4px;
  cursor: pointer;
  display: inline-block;
  font-weight: 600;
  margin: 0.25em 0;
  padding: 0.75em 1em;
  position: relative;
  transition: none;
  background-color: var(--secondary);
  color: var(--textInSecondary);
  box-shadow: 0 4px var(--secondaryShadow);
}

.button:hover {
  top: 2px;
  box-shadow: 0 2px var(--secondaryShadow);
  animation: none;
}

.button:active {
  box-shadow: 0 0 var(--secondary);
  top: 4px;
}
```

## File: `packages/website/src/components/Button/__tests__/button.spec.tsx`
```tsx
import { render, screen } from '@testing-library/react'

import Button from '../index'
import * as stubs from './stubs'

describe('Button', () => {
  it('should render the component with correct attributes', () => {
    render(<Button {...stubs.props} />)

    const link = screen.getByRole('link', { name: /GitHub/i })
    expect(link).toBeInTheDocument()
    expect(link).toHaveAttribute('href', '/')
    expect(link).toHaveAttribute('target', '_blank')
  })

  it('should render without icon when icon prop is not provided', () => {
    // eslint-disable-next-line @typescript-eslint/no-unused-vars
    const { icon, ...propsWithoutIcon } = stubs.props
    const { container } = render(<Button {...propsWithoutIcon} />)

    const link = screen.getByRole('link', { name: /GitHub/i })
    expect(link).toBeInTheDocument()
    expect(container.querySelector('svg')).not.toBeInTheDocument()
  })
})
```

## File: `packages/website/src/components/Button/__tests__/stubs.ts`
```typescript
export const props = {
  target: '_blank',
  icon: 'star',
  text: 'GitHub',
  link: '/',
}
```

## File: `packages/website/src/components/CarbonAd/index.tsx`
```tsx
'use client'

import { useRef, useEffect } from 'react'

import styles from './styles.module.css'

const CarbonAd = () => {
  const adsContainer = useRef<HTMLDivElement>(null)

  useEffect(() => {
    if (!adsContainer.current || typeof window === 'undefined') {
      return
    }

    const existingScript = document.getElementById('_carbonads_js')

    if (existingScript) {
      const existingAd = document.getElementById('carbonads')

      if (existingAd && adsContainer.current) {
        adsContainer.current.appendChild(existingAd)
      }

      return
    }

    const carbonAdsScript = document.createElement('script')
    carbonAdsScript.src =
      '//cdn.carbonads.com/carbon.js' + '?serve=CE7DL5QJ&placement=gitmojidev'
    carbonAdsScript.async = true
    carbonAdsScript.id = '_carbonads_js'

    adsContainer.current.appendChild(carbonAdsScript)

    return () => {}
  }, [])

  return (
    <div className="col-xs-12">
      <div
        ref={adsContainer}
        className={`${styles.carbonContainer} row center-xs`}
      />
    </div>
  )
}

export default CarbonAd
```

## File: `packages/website/src/components/CarbonAd/styles.module.css`
```css
.carbonContainer {
  height: 100px;
}

:global(#carbonads) {
  display: block;
  overflow: hidden;
  max-width: 728px;
  border-radius: 4px;
  position: relative;
  box-shadow: 0 1px 2px 0 var(--cardShadow);
}

:global(#carbonads > span) {
  display: block;
}

:global(#carbonads a) {
  color: inherit;
  text-decoration: none;
}

:global(#carbonads a:hover) {
  color: inherit;
  animation: none;
}

:global(.carbon-wrap) {
  display: flex;
  align-items: center;
}

:global(.carbon-img) {
  display: block;
  margin: 0;
  line-height: 1;
}

:global(.carbon-img img) {
  display: block;
  height: 90px;
  width: auto;
}

:global(.carbon-text) {
  display: block;
  padding: 0 1em;
  line-height: 1.35;
  text-align: center;
  width: 100%;
  font-size: 14px;
}

:global(.carbon-poweredby) {
  display: block;
  position: absolute;
  bottom: 0;
  right: 0;
  padding: 6px 10px;
  background: var(--carbonAdBadgeBackground);
  text-align: center;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  font-weight: 600;
  font-size: 8px;
  border-top-left-radius: 4px;
  line-height: 1;
}
```

## File: `packages/website/src/components/CarbonAd/__tests__/carbonAd.spec.tsx`
```tsx
import { render, waitFor } from '@testing-library/react'

import CarbonAd from '../index'
import styles from '../styles.module.css'

describe('CarbonAd', () => {
  it('should render the component with carbon ads script container', async () => {
    const { container } = render(<CarbonAd />)

    await waitFor(() => {
      const carbonAdContainer = container.querySelector(
        `.${styles.carbonContainer}`,
      )
      expect(carbonAdContainer).toBeInTheDocument()
    })
  })
})
```

## File: `packages/website/src/components/ContributorsList/index.tsx`
```tsx
import Contributor from './Contributor'

type Props = {
  contributors: Array<{
    avatar: string
    id: string
    url: string
  }>
}

const ContributorsList = (props: Props) => (
  <div className="row center-xs">
    {props.contributors.map((contributor) => (
      <Contributor
        key={contributor.id}
        url={contributor.url}
        avatar={contributor.avatar}
      />
    ))}
  </div>
)

export default ContributorsList
```

## File: `packages/website/src/components/ContributorsList/Contributor/index.tsx`
```tsx
import styles from './styles.module.css'

type Props = { avatar: string; url: string }

const Contributor = (props: Props) => (
  <article className="col-xs-3 col-sm-2">
    <a href={props.url} target="_blank" rel="noreferrer">
      <img className={styles.picture} src={props.avatar} />
    </a>
  </article>
)

export default Contributor
```

## File: `packages/website/src/components/ContributorsList/Contributor/styles.module.css`
```css
.picture {
  max-width: 100%;
  border-radius: 50%;
  padding: 0.5em;
}
```

## File: `packages/website/src/components/ContributorsList/__tests__/contributorsList.spec.tsx`
```tsx
import { render } from '@testing-library/react'

import ContributorsList from '../index'
import Contributor from '../Contributor'
import * as stubs from './stubs'

describe('ContributorsList', () => {
  describe('Contributor', () => {
    it('should render the contributor with link and avatar', () => {
      const { container } = render(<Contributor {...stubs.contributor} />)

      const link = container.querySelector('a')
      expect(link).toBeInTheDocument()
      expect(link).toHaveAttribute('href', stubs.contributor.url)
      expect(link).toHaveAttribute('target', '_blank')
      expect(link).toHaveAttribute('rel', 'noreferrer')

      const img = container.querySelector('img')
      expect(img).toBeInTheDocument()
      expect(img).toHaveAttribute('src', stubs.contributor.avatar)
    })
  })

  it('should render the list of contributors', () => {
    const { container } = render(<ContributorsList {...stubs.props} />)

    const links = container.querySelectorAll('a')
    expect(links).toHaveLength(stubs.props.contributors.length)
    expect(links[0]).toHaveAttribute('href', stubs.contributor.url)
  })
})
```

## File: `packages/website/src/components/ContributorsList/__tests__/stubs.ts`
```typescript
export const contributor = {
  url: 'https://github.com/profile',
  avatar: 'https://github.com/avatar',
  id: 'contributor-id-123',
}

export const props = {
  contributors: [contributor],
}
```

## File: `packages/website/src/components/GitmojiList/emojiColorsMap.ts`
```typescript
export default {
  'adhesive-bandage': '#fbcfb7',
  alembic: '#7f39fb',
  alien: '#c5e763',
  ambulance: '#fb584a',
  dizzy: '#ffdb3a',
  'arrow-down': '#ef5350',
  'arrow-up': '#00e676',
  art: '#ff7281',
  beers: '#fbb64b',
  bento: '#ff5864',
  bookmark: '#80deea',
  boom: '#f94f28',
  bug: '#8cd842',
  'building-construction': '#ffe55f',
  bulb: '#ffce49',
  'busts-in-silhouette': '#ffce49',
  'camera-flash': '#00a9f0',
  'card-file-box': '#c5e763',
  'chart-with-upwards-trend': '#cedae6',
  'children-crossing': '#ffce49',
  'clown-face': '#ff7281',
  'construction-worker': '#64b5f6',
  construction: '#ffb74d',
  egg: '#77e856',
  fire: '#ff9d44',
  'globe-with-meridians': '#e7f4ff',
  'goal-net': '#c7cb12',
  'green-heart': '#c5e763',
  hammer: '#ffc400',
  coffin: '#d9e3e8',
  'heavy-minus-sign': '#ef5350',
  'heavy-plus-sign': '#00e676',
  iphone: '#40c4ff',
  label: '#cb63e6',
  lipstick: '#80deea',
  lock: '#ffce49',
  'closed-lock-with-key': '#83beec',
  'loud-sound': '#23b4d2',
  mag: '#ffe55f',
  memo: '#00e676',
  mute: '#e6ebef',
  'ok-hand': '#c5e763',
  package: '#fdd0ae',
  'page-facing-up': '#d9e3e8',
  'passport-control': '#4dc6dc',
  pencil: '#ffce49',
  pencil2: '#ffce49',
  poop: '#a78674',
  pushpin: '#39c2f1',
  recycle: '#77e856',
  rewind: '#56d1d8',
  rocket: '#00a9f0',
  'rotating-light': '#536dfe',
  'safety-vest': '#f2ad52',
  'see-no-evil': '#8bdfe7',
  seedling: '#c5e763',
  sparkles: '#ffe55f',
  'speech-balloon': '#cedae6',
  stethoscope: '#77e856',
  tada: '#f74d5f',
  'test-tube': '#fb584a',
  'triangular-flag-on-post': '#ffce49',
  truck: '#ef584a',
  'twisted-rightwards-arrows': '#56d1d8',
  wastebasket: '#d9e3e8',
  wheelchair: '#00b1fb',
  'white-check-mark': '#77e856',
  wrench: '#ffc400',
  zap: '#40c4ff',
  'monocle-face': '#ffe55f',
  necktie: '#83beec',
  bricks: '#ff6723',
  technologist: '#86B837',
  'money-with-wings': '#b3c0b1',
  thread: '#ffbe7b',
  airplane: '#74d4ec',
  't-rex': '#56d1d8',
} as const
```

## File: `packages/website/src/components/GitmojiList/index.tsx`
```tsx
'use client'

import { Suspense, useEffect, useState } from 'react'
import Clipboard from 'clipboard'
import type { Gitmoji as GitmojiType } from 'gitmojis'
import toast from 'react-hot-toast'

import Gitmoji from './Gitmoji'
import Toolbar from './Toolbar'
import SearchParamsSync from './SearchParamsSync'
import useLocalStorage from './hooks/useLocalStorage'
import styles from './styles.module.css'

type Props = {
  gitmojis: readonly GitmojiType[]
}

const GitmojiList = (props: Props) => {
  const [searchInput, setSearchInput] = useState('')
  const [isListMode, setIsListMode] = useLocalStorage('isListMode', false)

  const gitmojis = searchInput
    ? props.gitmojis.filter(({ emoji, code, description }) => {
        const lowerCasedSearch = searchInput.toLowerCase()

        return (
          code.includes(lowerCasedSearch) ||
          description.toLowerCase().includes(lowerCasedSearch) ||
          emoji == searchInput
        )
      })
    : props.gitmojis

  useEffect(() => {
    const clipboard = new Clipboard(
      '.gitmoji-clipboard-emoji, .gitmoji-clipboard-code',
    )

    clipboard.on('success', function (e) {
      toast(
        (t) => (
          <span className={styles.notification}>
            <p>
              Hey! Gitmoji <span className={styles.gitmojiCode}>{e.text}</span>{' '}
              copied to the clipboard 😜
            </p>
            <span
              className={styles.closeButton}
              onClick={() => toast.dismiss(t.id)}
            />
          </span>
        ),
        {
          id: 'clipboard',
          style: {
            background: '#ff5a79',
            color: '#ffffff',
            fontWeight: 600,
            fontSize: '90%',
          },
        },
      )
    })

    return () => clipboard.destroy()
  }, [])

  return (
    <div className="row" id="gitmoji-list">
      <Suspense fallback={null}>
        <SearchParamsSync
          searchInput={searchInput}
          setSearchInput={setSearchInput}
        />
      </Suspense>
      <div className="col-xs-12">
        <Toolbar
          isListMode={isListMode}
          searchInput={searchInput}
          setIsListMode={setIsListMode}
          setSearchInput={setSearchInput}
        />
      </div>

      {gitmojis.length === 0 ? (
        <h2>No gitmojis found for search: {searchInput}</h2>
      ) : (
        gitmojis.map((gitmoji, index) => (
          <Gitmoji
            code={gitmoji.code}
            description={gitmoji.description}
            emoji={gitmoji.emoji}
            isListMode={isListMode}
            key={index}
            // @ts-expect-error: This should be replaced with something like:
            // typeof gitmojis[number]['name'] but JSON can't be exported `as const`
            name={gitmoji.name}
          />
        ))
      )}
    </div>
  )
}

export default GitmojiList
```

## File: `packages/website/src/components/GitmojiList/SearchParamsSync.tsx`
```tsx
'use client'

import { useEffect } from 'react'
import { useRouter, useSearchParams } from 'next/navigation'

type Props = {
  searchInput: string
  setSearchInput: (value: string) => void
}

/**
 * Small client component that syncs URL search params with the search input state.
 * Wrapped in Suspense to avoid CSR bailout while keeping the main list static.
 */
export default function SearchParamsSync({
  searchInput,
  setSearchInput,
}: Props) {
  const router = useRouter()
  const searchParams = useSearchParams()

  useEffect(() => {
    const search = searchParams.get('search')
    if (search) {
      setSearchInput(search)
    }
  }, [searchParams, setSearchInput])

  useEffect(() => {
    const search = searchParams.get('search')
    if (search && !searchInput) {
      router.push('/')
    }
  }, [searchInput, searchParams, router])

  return null
}
```

## File: `packages/website/src/components/GitmojiList/styles.module.css`
```css
.gitmojiCode {
  padding: 0 4px;
  border-radius: 4px;
  background-color: var(--notificationEmojiCodeColor);
  color: var(--notificationText);
}

.closeButton {
  width: 20px;
  height: 20px;
  position: absolute;
  right: 4px;
  top: 4px;
  overflow: hidden;
  text-indent: 100%;
  cursor: pointer;
  backface-visibility: hidden;
}

.closeButton:hover,
.closeButton:focus {
  outline: none;
}

.closeButton::before,
.closeButton::after {
  content: '';
  position: absolute;
  width: 3px;
  height: 60%;
  top: 50%;
  left: 50%;
  background: var(--notificationText);
}

.closeButton::before {
  transform: translate(-50%, -50%) rotate(45deg);
}

.closeButton::after {
  transform: translate(-50%, -50%) rotate(-45deg);
}
```

## File: `packages/website/src/components/GitmojiList/Gitmoji/index.tsx`
```tsx
import emojiColorsMap from '../emojiColorsMap'
import styles from './styles.module.css'

type Props = {
  code: string
  description: string
  emoji: string
  isListMode: boolean
  name: keyof typeof emojiColorsMap
}

const Gitmoji = (props: Props) => {
  const style = {
    '--emojiColor': emojiColorsMap[props.name],
  } as React.CSSProperties

  return (
    <article
      style={style}
      className={`${styles.emoji} col-xs-12 col-sm-6 ${
        props.isListMode ? 'col-md-4' : 'col-md-3'
      }`}
    >
      <div
        className={`${styles.card} ${props.isListMode ? styles.cardList : ''}`}
      >
        <header className={`${styles.cardHeader}`}>
          <button
            type="button"
            className={`gitmoji-clipboard-emoji ${styles.gitmoji}`}
            data-clipboard-text={props.emoji}
          >
            {props.emoji}
          </button>
        </header>
        <div className={styles.gitmojiInfo}>
          <button
            className={`gitmoji-clipboard-code ${styles.gitmojiCode}`}
            data-clipboard-text={props.code}
            tabIndex={-1}
            type="button"
          >
            <code>
              {replaceWithJSX(
                props.code,
                '_',
                <>
                  _<wbr />
                </>,
              )}
            </code>
          </button>
          <p>{props.description}</p>
        </div>
      </div>
    </article>
  )
}

const replaceWithJSX = (
  text: string,
  find: string,
  replace: React.JSX.Element,
) => {
  const nodes: (string | React.JSX.Element)[] = text.split(find)
  const first = nodes.shift()

  return nodes
    .reduce((newNodes, part) => [...newNodes, replace, part], [first])
    .map((el, index) => <span key={index}>{el}</span>)
}

export default Gitmoji
```

## File: `packages/website/src/components/GitmojiList/Gitmoji/styles.module.css`
```css
.emoji {
  display: flex;
  box-sizing: border-box;
}

.card {
  background-color: var(--cardBackground);
  border-radius: 4px;
  box-shadow: 0 1px 2px 0 var(--cardShadow);
  flex: 1;
  margin: 1em 0;
  transition: all 0.25s ease-out;
  text-align: center;
  overflow: hidden;
}

.cardList {
  display: flex;
}

.cardList .gitmoji {
  font-size: 3.5em;
}

.cardList .cardHeader {
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 0 1rem;
}

.cardList .gitmojiInfo {
  text-align: left;
  padding: 1rem;
}

.cardList .gitmojiCode {
  text-align: left;
}

.cardList .gitmojiInfo p {
  padding: 0;
  margin: 0;
  padding-top: 0.5rem;
}

.card:hover {
  box-shadow: 0 10px 20px 0 var(--cardShadow);
  transform: translateY(-1px);
}

[data-theme='dark'] .card:hover {
  box-shadow: none;
  background-color: #3b3b3b;
}

.cardHeader {
  background-color: var(--emojiColor);
  align-self: flex-start;
  padding-top: 2em;
  padding-bottom: 0.85em;
  border-top-left-radius: 4px;
  border-top-right-radius: 4px;
}

.gitmoji,
.gitmojiCode {
  background-color: transparent;
  border: none;
  color: inherit;
  font: inherit;
  padding: 0;
}

.gitmoji {
  border-radius: none;
  cursor: pointer;
  display: inline-block;
  font-size: 5em;
  font-family:
    'Apple Color Emoji', 'Segoe UI Emoji', 'Noto Color Emoji',
    'Segoe UI Symbol', 'Android Emoji', 'EmojiSymbols';
}

.gitmoji:hover,
.gitmoji:focus {
  animation-name: bounce;
  animation-duration: 0.5s;
}

.gitmojiCode {
  display: inline-block;
  position: relative;
  border-radius: 4px;
  transition-duration: 0.3s;
  cursor: pointer;
  white-space: nowrap;
}

.gitmojiCode::after {
  content: '';
  position: absolute;
  left: 0;
  bottom: 0;
  width: 0;
  height: 0.2em;
  border-radius: 4px;
  transition: width 0.15s;
  background-color: var(--emojiColor);
}

.gitmojiCode:hover::after {
  width: 100%;
}

.gitmojiInfo {
  padding: 1.5em;
  word-break: break-all;
  color: var(--emojiCodeText);
}

.gitmojiInfo p {
  color: var(--cardText);
  word-break: normal;
}

@media (max-width: 768px) {
  .gitmoji,
  .cardList .gitmoji {
    font-size: 50px;
  }

  .cardHeader {
    padding-bottom: 1em;
  }
}

/*
  This code has been obtained from:
  https://github.com/daneden/animate.css/blob/master/source/attention_seekers/bounce.css
*/
@keyframes bounce {
  from,
  20%,
  53%,
  80%,
  to {
    animation-timing-function: cubic-bezier(0.215, 0.61, 0.355, 1);
    transform: translate3d(0, 0, 0);
  }

  40%,
  43% {
    animation-timing-function: cubic-bezier(0.755, 0.05, 0.855, 0.06);
    transform: translate3d(0, -9px, 0);
  }

  70% {
    animation-timing-function: cubic-bezier(0.755, 0.05, 0.855, 0.06);
    transform: translate3d(0, -5px, 0);
  }

  90% {
    transform: translate3d(0, -2px, 0);
  }
}
```

## File: `packages/website/src/components/GitmojiList/hooks/useLocalStorage.tsx`
```tsx
import { useState, useEffect } from 'react'

export default function useLocalStorage<T>(key: string, defaultValue: T) {
  const [state, setState] = useState(defaultValue)

  useEffect(() => {
    try {
      const localValue = window.localStorage.getItem(key)

      if (localValue !== null) {
        setState(JSON.parse(localValue))
      }
    } catch (error) {
      console.error(`ERROR: Loading ${key} from localStorage – ${error}`)
    }
  }, [])

  useEffect(() => {
    window.localStorage.setItem(key, `${state}`)
  }, [state])

  return [state, setState] as const
}
```

## File: `packages/website/src/components/GitmojiList/hooks/__tests__/stubs.ts`
```typescript
export const localStorageMock = {
  key: 'gitmojiTestKey',
  value: 'gitmojiTestValue',
}
```

## File: `packages/website/src/components/GitmojiList/hooks/__tests__/useLocalStorage.spec.tsx`
```tsx
import { render } from '@testing-library/react'

import useLocalStorage from '../useLocalStorage'
import * as stubs from './stubs'

const TestComponent = ({
  storageKey,
  storageValue,
}: {
  storageKey: string
  storageValue: string
}) => {
  useLocalStorage(storageKey, storageValue)

  return null
}

Object.defineProperty(window, 'localStorage', {
  writable: true,
  value: { setItem: jest.fn(), getItem: jest.fn() },
})

const getItem = window.localStorage.getItem as jest.Mock
const setItem = window.localStorage.setItem as jest.Mock

describe('useLocalStorage', () => {
  beforeEach(() => {
    jest.clearAllMocks()
  })

  describe('when value is not persisted', () => {
    beforeEach(() => {
      getItem.mockReturnValue(null)
    })

    it('should call localStorage.setItem', () => {
      const { rerender } = render(
        <TestComponent
          storageKey={stubs.localStorageMock.key}
          storageValue={stubs.localStorageMock.value}
        />,
      )

      rerender(
        <TestComponent
          storageKey={stubs.localStorageMock.key}
          storageValue={stubs.localStorageMock.value}
        />,
      )

      expect(setItem).toHaveBeenCalledWith(
        stubs.localStorageMock.key,
        stubs.localStorageMock.value,
      )
    })
  })

  describe('when there is an error', () => {
    const consoleError = console.error

    beforeEach(() => {
      getItem.mockImplementation(() => {
        throw new Error('Test')
      })

      Object.defineProperty(console, 'error', {
        writable: true,
        value: jest.fn(),
      })
    })

    afterEach(() => {
      Object.defineProperty(console, 'error', {
        writable: true,
        value: consoleError,
      })
    })

    it('should call console.error', () => {
      const { rerender } = render(
        <TestComponent
          storageKey={stubs.localStorageMock.key}
          storageValue={stubs.localStorageMock.value}
        />,
      )

      rerender(
        <TestComponent
          storageKey={stubs.localStorageMock.key}
          storageValue={stubs.localStorageMock.value}
        />,
      )

      expect(console.error).toHaveBeenCalledWith(expect.any(String))
    })
  })
})
```

## File: `packages/website/src/components/GitmojiList/Toolbar/index.tsx`
```tsx
'use client'

import { useEffect, useRef } from 'react'
import dynamic from 'next/dynamic'

import ListModeSelector from './ListModeSelector'
import ThemeSelector from './ThemeSelector'
const Kbd = dynamic(() => import('./Kbd'), { ssr: false })
import styles from './styles.module.css'

type Props = {
  isListMode: boolean
  searchInput?: string
  setIsListMode: (searchInput: boolean) => void
  setSearchInput: (searchInput: string) => void
}

const Toolbar = (props: Props) => {
  const searchInputRef = useRef<HTMLInputElement>(null)

  useEffect(() => {
    const keyboardEventListener = (event: KeyboardEvent) => {
      const searchInput = searchInputRef.current
      if (
        searchInput &&
        (event.ctrlKey || event.metaKey) &&
        event.key === 'k'
      ) {
        event.preventDefault()
        searchInput.focus()
      }
    }

    if (typeof window !== 'undefined') {
      document.addEventListener('keydown', keyboardEventListener, false)
    }

    return () => {
      document.removeEventListener('keydown', keyboardEventListener, false)
    }
  }, [])

  return (
    <div className={styles.container}>
      <div className={styles.inputWrapper}>
        <input
          className={styles.searchInput}
          ref={searchInputRef}
          name="searchInput"
          onChange={(event) => props.setSearchInput(event.target.value)}
          placeholder="Search your gitmoji..."
          type="search"
          value={props.searchInput}
        />

        <Kbd />
      </div>

      <div className={styles.actionsContainer}>
        <ThemeSelector />

        <ListModeSelector
          isListMode={props.isListMode}
          setIsListMode={props.setIsListMode}
        />
      </div>
    </div>
  )
}

export default Toolbar
```

## File: `packages/website/src/components/GitmojiList/Toolbar/styles.module.css`
```css
.container {
  align-items: center;
  display: flex;
  flex-direction: row;
  margin-bottom: 0.5rem;
  margin-top: 1.5rem;
}

.actionsContainer {
  display: flex;
}

.inputWrapper {
  flex: 1;
  display: flex;
  align-items: center;
  border-radius: 4px;
  border: 0;
  box-shadow: 0 2px 4px 0 var(--cardShadow);
  margin-right: 1rem;
  background-color: var(--cardBackground);
}

.inputWrapper:focus-within {
  outline: -webkit-focus-ring-color auto 1px;
}

.searchInput {
  background-color: transparent;
  border: none;
  flex-grow: 1;
  font-size: 1rem;
  padding: 1rem;
}

.searchInput:focus-visible {
  outline: none;
}

.searchInput:focus {
  outline: none;
}

[data-theme='dark'] .searchInput {
  color: var(--text);
}

@media (max-width: 568px) {
  .searchInput {
    margin: 0;
    margin-top: 0.5rem;
  }

  .container {
    flex-direction: column-reverse;
    align-items: stretch;
  }
}
```

## File: `packages/website/src/components/GitmojiList/Toolbar/Kbd/index.tsx`
```tsx
import styles from './styles.module.css'

const isMacOs = () => {
  return (
    typeof window !== 'undefined' &&
    window.navigator.platform.toUpperCase().includes('MAC')
  )
}

const Kbd = () => {
  return <kbd className={styles.kbd}>{isMacOs() ? '⌘' : 'Ctrl'} K</kbd>
}

export default Kbd
```

## File: `packages/website/src/components/GitmojiList/Toolbar/Kbd/styles.module.css`
```css
.kbd {
  right: 0;
  align-items: center;
  border-radius: 3px;
  border: solid 1px #999;
  color: #595959;
  display: flex;
  font-family: system-ui;
  margin-right: 0.5rem;
  padding: 0.25rem 0.5rem;
}

[data-theme='dark'] .kbd {
  color: #b8b8b8;
}

@media (max-width: 568px) {
  .kbd {
    display: none;
  }
}
```

## File: `packages/website/src/components/GitmojiList/Toolbar/ListModeSelector/index.tsx`
```tsx
import Icon from 'src/components/Icon'
import styles from './styles.module.css'

type Props = {
  isListMode: boolean
  setIsListMode: (isListMode: boolean) => void
}

const ListModeSelector = (props: Props) => (
  <div className={styles.container}>
    <button
      className={`${styles.button} ${
        !props.isListMode ? styles.buttonActive : ''
      }`}
      disabled={!props.isListMode}
      onClick={() => props.setIsListMode(false)}
    >
      <Icon name="grid" />
    </button>

    <button
      className={`${styles.button} ${
        props.isListMode ? styles.buttonActive : ''
      }`}
      disabled={props.isListMode}
      onClick={() => props.setIsListMode(true)}
    >
      <Icon name="list" />
    </button>
  </div>
)

export default ListModeSelector
```

## File: `packages/website/src/components/GitmojiList/Toolbar/ListModeSelector/styles.module.css`
```css
.container {
  display: flex;
}

.button {
  align-items: center;
  border-radius: 4px;
  border: none;
  color: var(--text);
  cursor: pointer;
  display: flex;
  background-color: var(--cardBackground);
  box-shadow: 0 2px 4px 0 var(--cardShadow);
  font-size: 16px;
  height: 48px;
  justify-content: center;
  margin: 8px;
  width: 48px;
}

.button svg {
  margin: 0;
}

.buttonActive {
  color: var(--secondary);
}
```

## File: `packages/website/src/components/GitmojiList/Toolbar/ThemeSelector/index.tsx`
```tsx
'use client'

import { useEffect, useState } from 'react'
import { useTheme } from 'next-themes'

import Icon from 'src/components/Icon'
import styles from './styles.module.css'

const ThemeSelector = () => {
  const [isMounted, setIsMounted] = useState(false)
  const { resolvedTheme, setTheme } = useTheme()
  const nextTheme = resolvedTheme === 'light' ? 'dark' : 'light'

  useEffect(() => setIsMounted(true), [])

  if (!isMounted) {
    return (
      <div className={styles.container}>
        <button disabled className={`${styles.button}`} />
      </div>
    )
  }

  return (
    <button className={`${styles.button}`} onClick={() => setTheme(nextTheme)}>
      <Icon name={nextTheme} />
    </button>
  )
}

export default ThemeSelector
```

## File: `packages/website/src/components/GitmojiList/Toolbar/ThemeSelector/styles.module.css`
```css
.button {
  display: flex;
  align-items: center;
  border-radius: 4px;
  border: none;
  color: var(--text);
  cursor: pointer;
  background-color: var(--cardBackground);
  box-shadow: 0 2px 4px 0 var(--cardShadow);
  font-size: 16px;
  height: 48px;
  justify-content: center;
  margin: 8px;
  width: 48px;
}

.button svg {
  margin: 0;
}

@media (max-width: 568px) {
  .button {
    margin-left: 0;
  }
}
```

## File: `packages/website/src/components/GitmojiList/__tests__/gitmojiList.spec.tsx`
```tsx
import { useRouter, useSearchParams } from 'next/navigation'
import { render, screen, fireEvent } from '@testing-library/react'

import GitmojiList from '../index'
import * as stubs from './stubs'

jest.mock('next/navigation', () => ({
  useRouter: jest.fn(),
  useSearchParams: jest.fn(),
  usePathname: jest.fn(() => '/'),
}))

const useRouterMock = useRouter as jest.Mock
const useSearchParamsMock = useSearchParams as jest.Mock

describe('GitmojiList', () => {
  beforeEach(() => {
    useRouterMock.mockReturnValue(stubs.appRouterMock())
    useSearchParamsMock.mockReturnValue(stubs.searchParamsMock())
  })

  describe('when is not list mode', () => {
    it('should render the component in grid mode by default', () => {
      const { container } = render(<GitmojiList {...stubs.props} />)

      const articles = container.querySelectorAll('article')
      expect(articles.length).toBeGreaterThan(0)
    })
  })

  describe('when is list mode', () => {
    it('should switch to list mode when clicking the list button', () => {
      const { container } = render(<GitmojiList {...stubs.props} />)

      const buttons = screen.getAllByRole('button')
      const listModeButton = buttons[1]

      fireEvent.click(listModeButton)

      const articles = container.querySelectorAll('article')
      expect(articles.length).toBeGreaterThan(0)
    })
  })

  describe('when user search the fire gitmoji', () => {
    beforeEach(() => {
      useRouterMock.mockReturnValue(stubs.appRouterMock())
      useSearchParamsMock.mockReturnValue(stubs.searchParamsMock())
    })

    it('should find the fire gitmoji by code', () => {
      const { container } = render(<GitmojiList {...stubs.props} />)
      const input = screen.getByRole('searchbox')
      const query = 'Fire'

      fireEvent.change(input, { target: { value: query } })

      const articles = container.querySelectorAll('article')
      expect(articles.length).toEqual(1)
    })

    it('should find the fire gitmoji by description', () => {
      const { container } = render(<GitmojiList {...stubs.props} />)
      const input = screen.getByRole('searchbox')
      const query = 'remove'

      fireEvent.change(input, { target: { value: query } })

      const articles = container.querySelectorAll('article')
      expect(articles.length).toEqual(1)
    })

    it('should find the fire gitmoji by emoji', () => {
      const { container } = render(<GitmojiList {...stubs.props} />)
      const input = screen.getByRole('searchbox')
      const query = '🔥'

      fireEvent.change(input, { target: { value: query } })

      const articles = container.querySelectorAll('article')
      expect(articles.length).toEqual(1)
    })
  })

  describe('when search is provided by query string', () => {
    beforeEach(() => {
      useRouterMock.mockReturnValue(stubs.appRouterMock())
      useSearchParamsMock.mockReturnValue(stubs.searchParamsMock('fire'))
    })

    it('should set the search input value to query.search', () => {
      render(<GitmojiList {...stubs.props} />)
      const query = 'fire'

      const input = screen.getByRole('searchbox')
      expect(input).toHaveValue(query)
    })

    describe('when the user deletes the search input', () => {
      it('should clear the query string', () => {
        const mockRouter = stubs.appRouterMock()
        useRouterMock.mockReturnValue(mockRouter)
        useSearchParamsMock.mockReturnValue(stubs.searchParamsMock('fire'))

        render(<GitmojiList {...stubs.props} />)
        const input = screen.getByRole('searchbox')

        fireEvent.change(input, { target: { value: '' } })

        expect(mockRouter.push).toHaveBeenCalledWith('/')
      })
    })
  })
})
```

## File: `packages/website/src/components/GitmojiList/__tests__/stubs.ts`
```typescript
import { gitmojis } from 'gitmojis'

export const props = {
  gitmojis: gitmojis.slice(0, 6),
}

export const routerMock = (query = {}) => ({
  query,
  push: jest.fn(),
})

export const appRouterMock = () => ({
  push: jest.fn(),
  replace: jest.fn(),
  prefetch: jest.fn(),
  back: jest.fn(),
  forward: jest.fn(),
  refresh: jest.fn(),
})

export const searchParamsMock = (searchValue?: string) => {
  const params = new URLSearchParams()
  if (searchValue) {
    params.set('search', searchValue)
  }
  return params
}
```

## File: `packages/website/src/components/Icon/definitions.tsx`
```tsx
export const IconDefinitions = () => (
  <svg
    style={{ position: 'absolute', width: 0, height: 0 }}
    width={0}
    height={0}
    version="1.1"
    xmlns="http://www.w3.org/2000/svg"
    xmlnsXlink="http://www.w3.org/1999/xlink"
  >
    <defs>
      <symbol id="icon-heart" viewBox="0 0 64 64">
        <title>heart</title>
        <path
          className="heart"
          d="m61.1 18.2c-6.4-17-27.2-9.4-29.1-.9-2.6-9-22.9-15.7-29.1.9-6.9 18.5 26.7 35.1 29.1 37.8 2.4-2.2 36-19.6 29.1-37.8"
          fill="#ff5a79"
        />
      </symbol>
      <symbol id="icon-star" viewBox="0 0 64 64">
        <title>star</title>
        <path
          className="twitter"
          d="M62,25.2H39.1L32,3l-7.1,22.2H2l18.5,13.7l-7,22.1L32,47.3L50.5,61l-7.1-22.2L62,25.2z"
          fill="#FFDD67"
        />
      </symbol>
      <symbol id="icon-twitter" viewBox="0 0 64 64">
        <title>twitter</title>
        <g fill="#42ade2">
          <path d="m59.8 24.3c0 0 1.1-6.2-3.5-3.4 0 0-.4-6.3-4.3-1.9 0 0-2.1-3.9-4.4-.3-3.1 4.8-5.2 12.4-3.2 25l3.8-2.5c2.7-7.9 12.4-8.8 13.7-13.1.9-3-2.1-3.8-2.1-3.8" />
          <path d="m22.1 17.6l-9.9 3.6c2.2-12 16.6-11.2 16.6-11.2s-6.8 3.2-6.7 7.6" />
          <path d="m23.7 19.8l-10.5 1.4c4.8-11.2 18.7-7.3 18.7-7.3s-7.3 1.6-8.2 5.9" />
        </g>
        <g fill="#ffd93b">
          <path d="m2 29l5.4-1.4v3.6c0-.1-3.3-.6-5.4-2.2" />
          <path d="M7.4,27.5L2,24.8c3.6-2.8,7.7-1.9,7.7-1.9L7.4,27.5z" />
        </g>
        <g fill="#e08828">
          <path d="m33.8 53h-2.1v7.9c-.3.1-2.1-.1-2.9-.1-1.8 0-3.3 1.3-3.3 1.3h8.3v-9.1" />
          <path d="m25 53h-2.1v7.9c-.3.1-2.1-.1-2.9-.1-1.8 0-3.3 1.3-3.3 1.3h8.3v-9.1" />
          <path
            d="m54 36.2c3.9 0-4.1 17.5-23.3 17.5-13 0-23.9-5.2-23.9-21.5 0-10.1 6.4-18.3 19.5-15 13.3 3.5 6.5 19 27.7 19"
            fill="#42ade2"
          />
          <path
            d="m37.6 51.7c-15.6 0-14-12-27.9-11.2 5.1 15.8 27.9 11.2 27.9 11.2"
            fill="#fff"
          />
          <path
            d="m39.1 29.2c-10-9.8-20.2 6.2-7.9 12.6 12.1 6.2 20.4-4.8 20.4-4.8s-6.1-1.5-12.5-7.8"
            fill="#297b9d"
          />
        </g>
        <circle cx="15.1" cy="24.9" r="2.5" fill="#3e4347" />
      </symbol>
      <symbol id="icon-twitter-x" viewBox="0 0 48 35">
        <title>twitter-x</title>
        <path d="M12.91 5.477l14.813 19.882-14.907 16.164h3.356l13.05-14.152 10.544 14.152h11.418l-15.645-21L49.414 5.477H46.06l-12.02 13.035-9.71-13.035zm4.934 2.48h5.242L46.25 39.043h-5.246zm0 0"></path>
      </symbol>
      <symbol id="icon-list" x="0px" y="0px" viewBox="0 0 512 512">
        <title>list</title>
        <path
          fill="currentColor"
          d="M149.333 216v80c0 13.255-10.745 24-24 24H24c-13.255 0-24-10.745-24-24v-80c0-13.255 10.745-24 24-24h101.333c13.255 0 24 10.745 24 24zM0 376v80c0 13.255 10.745 24 24 24h101.333c13.255 0 24-10.745 24-24v-80c0-13.255-10.745-24-24-24H24c-13.255 0-24 10.745-24 24zM125.333 32H24C10.745 32 0 42.745 0 56v80c0 13.255 10.745 24 24 24h101.333c13.255 0 24-10.745 24-24V56c0-13.255-10.745-24-24-24zm80 448H488c13.255 0 24-10.745 24-24v-80c0-13.255-10.745-24-24-24H205.333c-13.255 0-24 10.745-24 24v80c0 13.255 10.745 24 24 24zm-24-424v80c0 13.255 10.745 24 24 24H488c13.255 0 24-10.745 24-24V56c0-13.255-10.745-24-24-24H205.333c-13.255 0-24 10.745-24 24zm24 264H488c13.255 0 24-10.745 24-24v-80c0-13.255-10.745-24-24-24H205.333c-13.255 0-24 10.745-24 24v80c0 13.255 10.745 24 24 24z"
          className=""
        ></path>
      </symbol>
      <symbol id="icon-grid" viewBox="0 0 512 512">
        <title>grid</title>
        <path
          fill="currentColor"
          d="M149.333 56v80c0 13.255-10.745 24-24 24H24c-13.255 0-24-10.745-24-24V56c0-13.255 10.745-24 24-24h101.333c13.255 0 24 10.745 24 24zm181.334 240v-80c0-13.255-10.745-24-24-24H205.333c-13.255 0-24 10.745-24 24v80c0 13.255 10.745 24 24 24h101.333c13.256 0 24.001-10.745 24.001-24zm32-240v80c0 13.255 10.745 24 24 24H488c13.255 0 24-10.745 24-24V56c0-13.255-10.745-24-24-24H386.667c-13.255 0-24 10.745-24 24zm-32 80V56c0-13.255-10.745-24-24-24H205.333c-13.255 0-24 10.745-24 24v80c0 13.255 10.745 24 24 24h101.333c13.256 0 24.001-10.745 24.001-24zm-205.334 56H24c-13.255 0-24 10.745-24 24v80c0 13.255 10.745 24 24 24h101.333c13.255 0 24-10.745 24-24v-80c0-13.255-10.745-24-24-24zM0 376v80c0 13.255 10.745 24 24 24h101.333c13.255 0 24-10.745 24-24v-80c0-13.255-10.745-24-24-24H24c-13.255 0-24 10.745-24 24zm386.667-56H488c13.255 0 24-10.745 24-24v-80c0-13.255-10.745-24-24-24H386.667c-13.255 0-24 10.745-24 24v80c0 13.255 10.745 24 24 24zm0 160H488c13.255 0 24-10.745 24-24v-80c0-13.255-10.745-24-24-24H386.667c-13.255 0-24 10.745-24 24v80c0 13.255 10.745 24 24 24zM181.333 376v80c0 13.255 10.745 24 24 24h101.333c13.255 0 24-10.745 24-24v-80c0-13.255-10.745-24-24-24H205.333c-13.255 0-24 10.745-24 24z"
        ></path>
      </symbol>
      <symbol id="icon-light" viewBox="0 0 24 24">
        <title>light</title>
        <path
          fill="currentColor"
          d="M3.563 18.563l1.781-1.828 1.406 1.406-1.781 1.828zM11.016 22.453v-2.953h1.969v2.953h-1.969zM12 5.484q2.484 0 4.242 1.758t1.758 4.242-1.758 4.242-4.242 1.758-4.242-1.758-1.758-4.242 1.758-4.242 4.242-1.758zM20.016 10.5h3v2.016h-3v-2.016zM17.25 18.141l1.406-1.359 1.781 1.781-1.406 1.406zM20.438 4.453l-1.781 1.781-1.406-1.406 1.781-1.781zM12.984 0.563v2.953h-1.969v-2.953h1.969zM3.984 10.5v2.016h-3v-2.016h3zM6.75 4.828l-1.406 1.406-1.781-1.781 1.406-1.406z"
        ></path>
      </symbol>

      <symbol id="icon-dark" viewBox="0 0 24 24">
        <title>dark</title>
        <path
          fill="currentColor"
          d="M9.984 2.016q4.172 0 7.102 2.93t2.93 7.055-2.93 7.055-7.102 2.93q-2.719 0-4.969-1.313 2.297-1.313 3.633-3.633t1.336-5.039-1.336-5.039-3.633-3.633q2.25-1.313 4.969-1.313z"
        ></path>
      </symbol>
    </defs>
  </svg>
)
```

## File: `packages/website/src/components/Icon/index.tsx`
```tsx
export { IconDefinitions } from './definitions'
import styles from './styles.module.css'

type Props = { name: string }

const Icon = (props: Props) => (
  <svg className={`${styles.icon} icon-${props.name}`}>
    <use xlinkHref={`#icon-${props.name}`} />
  </svg>
)

export default Icon
```

## File: `packages/website/src/components/Icon/styles.module.css`
```css
.icon {
  width: 1em;
  height: 1em;
  margin-right: 0.25em;
}

.icon:global(.icon-heart) {
  margin: 0;
}
```

## File: `packages/website/src/components/Icon/__tests__/icon.spec.tsx`
```tsx
import { render } from '@testing-library/react'

import Icon, { IconDefinitions } from '../index'
import * as stubs from './stubs'

describe('Icon', () => {
  it('should render the component with correct icon reference', () => {
    const { container } = render(<Icon {...stubs.props} />)

    const svg = container.querySelector('svg')
    expect(svg).toBeInTheDocument()
    expect(svg).toHaveClass(`icon-${stubs.props.name}`)

    const use = container.querySelector('use')
    expect(use).toBeInTheDocument()
    expect(use).toHaveAttribute('xlink:href', `#icon-${stubs.props.name}`)
  })

  it('should render IconDefinitions with all symbols', () => {
    const { container } = render(<IconDefinitions />)

    const svg = container.querySelector('svg')
    expect(svg).toBeInTheDocument()

    const defs = container.querySelector('defs')
    expect(defs).toBeInTheDocument()
  })
})
```

## File: `packages/website/src/components/Icon/__tests__/stubs.ts`
```typescript
export const props = {
  name: 'star',
}
```

## File: `packages/website/src/components/Layout/index.tsx`
```tsx
import { IconDefinitions } from 'src/components/Icon'
import Header from './Header'
import Hamburger from './Hamburger'
import Footer from './Footer'

type Props = { children: React.ReactNode }

const Layout = (props: Props) => (
  <>
    <IconDefinitions />
    <Hamburger />
    <Header withHeadline />
    <main className="wrap">{props.children}</main>
    <Footer />
  </>
)

export default Layout
```

## File: `packages/website/src/components/Layout/Footer/index.tsx`
```tsx
import Link from 'next/link'

import Icon from 'src/components/Icon'
import styles from './styles.module.css'

const Footer = () => (
  <footer className={styles.footer}>
    <div className="wrap">
      <div className="row middle-xs">
        <div className={`col-sm-6 ${styles.madeWithLove}`}>
          <h3>
            Made with <Icon name="heart" /> by{' '}
            <a href="https://carloscuesta.me">Carlos Cuesta</a>
          </h3>
        </div>
        <div className={`col-sm-6 ${styles.footerNav}`}>
          <nav>
            <Link href="/about">About</Link>
            <Link href="/contributors">Contributors</Link>
            <a href="https://github.com/carloscuesta/gitmoji">GitHub</a>
          </nav>
        </div>
      </div>
    </div>
  </footer>
)

export default Footer
```

## File: `packages/website/src/components/Layout/Footer/styles.module.css`
```css
.footer {
  padding: 1.5em;
  background-color: var(--footerBackground);
  color: var(--textInSecondary);
}

.footerNav {
  -webkit-box-pack: end;
  -ms-flex-pack: end;
  justify-content: flex-end;
  text-align: end;
}

.footerNav a:after {
  content: '·';
  color: var(--textInSecondary);
  margin: 0 0.75em;
}

.footerNav a:last-child:after {
  content: '';
  margin: 0;
}

@media (max-width: 768px) {
  .footer,
  .footerNav {
    justify-content: center;
    text-align: center;
  }

  .madeWithLove,
  .footerNav {
    flex-basis: 100%;
    max-width: 100%;
  }
}
```

## File: `packages/website/src/components/Layout/Hamburger/index.tsx`
```tsx
'use client'

import { useState, useEffect } from 'react'
import { usePathname } from 'next/navigation'
import FocusTrap from 'focus-trap-react'

import MenuLink from './MenuLink'
import OpenIcon from './OpenIcon'
import CloseIcon from './CloseIcon'
import styles from './styles.module.css'

const Hamburger = () => {
  const pathname = usePathname()
  const [isOpen, setIsOpen] = useState(false)

  useEffect(() => {
    setIsOpen(false)
  }, [pathname])

  useEffect(() => {
    if (isOpen) {
      document.body.classList.add('overflow-hidden')
    } else {
      document.body.classList.remove('overflow-hidden')
    }
  }, [isOpen])

  return (
    <div className={styles.hamburger}>
      <button
        aria-label="Open navigation menu"
        className={styles.button}
        onClick={() => setIsOpen(true)}
      >
        <OpenIcon />
      </button>

      {isOpen && (
        <FocusTrap active={isOpen}>
          <nav className={styles.menu}>
            <div className={styles.closeContainer}>
              <button
                aria-label="Close navigation menu"
                className={styles.button}
                onClick={() => setIsOpen(false)}
              >
                <CloseIcon />
              </button>
            </div>

            <ul className={styles.links}>
              <li>
                <MenuLink href="/" text="Home" />
              </li>
              <li>
                <MenuLink href="/about" text="About" />
              </li>
              <li>
                <MenuLink href="/specification" text="Specification" />
              </li>
              <li>
                <MenuLink href="/contributors" text="Contributors" />
              </li>
              <li>
                <MenuLink href="/related-tools" text="Related tools" />
              </li>
            </ul>
          </nav>
        </FocusTrap>
      )}
    </div>
  )
}

export default Hamburger
```

## File: `packages/website/src/components/Layout/Hamburger/styles.module.css`
```css
.hamburger {
  position: fixed;
  right: 0;
  z-index: 1;
}

.menu {
  background: var(--menuBackground);
  bottom: 0;
  left: 0;
  position: fixed;
  right: 0;
  top: 0;
}

.button {
  background-color: transparent;
  border: none;
  color: inherit;
  color: var(--secondary);
  cursor: pointer;
  display: flex;
  font: inherit;
  margin: 0;
  padding: 0.75em;
}

.closeContainer {
  position: absolute;
  right: 0;
}

.closeContainer .button {
  color: var(--textInSecondary);
}

.links {
  align-items: center;
  color: var(--textInSecondary);
  display: flex;
  flex-direction: column;
  flex: 1;
  font-size: 3em;
  height: 100%;
  justify-content: center;
  list-style-type: none;
  margin: 0;
  padding: 0;
}

.links li {
  padding: 0.5em 0;
}
```

## File: `packages/website/src/components/Layout/Hamburger/CloseIcon/index.tsx`
```tsx
const CloseIcon = () => (
  <svg
    xmlns="http://www.w3.org/2000/svg"
    width="48"
    height="48"
    fill="currentColor"
  >
    <path d="M37.968 12.844L26.812 24L37.968 35.156L35.156 37.968L24 26.812L12.844 37.968L10.032 35.156L21.188 24L10.032 12.844L12.844 10.032L24 21.188L35.156 10.032L37.968 12.844Z" />
  </svg>
)

export default CloseIcon
```

## File: `packages/website/src/components/Layout/Hamburger/MenuLink/index.tsx`
```tsx
'use client'

import Link from 'next/link'
import { usePathname } from 'next/navigation'

import styles from './styles.module.css'

type Props = { href: string; text: string }

const MenuLink = (props: Props) => {
  const pathname = usePathname()
  const isUserOnLinkPage: boolean = props.href === pathname

  if (!props.href.startsWith('/')) {
    return (
      <a
        className={styles.link}
        href={props.href}
        rel="noopener noreferrer"
        target="_blank"
      >
        {props.text}
      </a>
    )
  }

  return (
    <Link
      className={[styles.link, isUserOnLinkPage && styles.linkActive].join(' ')}
      href={props.href}
    >
      {props.text}
    </Link>
  )
}

export default MenuLink
```

## File: `packages/website/src/components/Layout/Hamburger/MenuLink/styles.module.css`
```css
.link {
  color: var(--text);
  text-decoration: none;
  font-weight: bold;
}

.link:hover {
  text-decoration: underline;
}

.linkActive {
  text-decoration: underline;
}
```

## File: `packages/website/src/components/Layout/Hamburger/OpenIcon/index.tsx`
```tsx
const OpenIcon = () => (
  <svg
    xmlns="http://www.w3.org/2000/svg"
    width="48"
    height="48"
    fill="currentColor"
  >
    <path d="M6 12H42V16.032H6V12ZM6 25.968V22.03H42V25.968H6ZM6 36V31.968H42V36H6Z" />
  </svg>
)

export default OpenIcon
```

## File: `packages/website/src/components/Layout/Header/index.tsx`
```tsx
import Button from 'src/components/Button'
import Logo from './Logo'
import styles from './styles.module.css'

type Props = { withHeadline: boolean }

const Header = (props: Props) => (
  <header className={styles.header}>
    <Logo />
    {props.withHeadline && (
      <h2 className={styles.title}>An emoji guide for your commit messages</h2>
    )}
    <div className={styles.buttons}>
      <Button
        icon="star"
        link="https://github.com/carloscuesta/gitmoji"
        text="GitHub"
      />
      <Button
        icon="twitter-x"
        link={
          'https://twitter.com/intent/tweet?text=gitmoji' +
          '%20%E2%80%93%20An%20%23emoji%20guide%20for%20your%20commit' +
          '%20messages%20by%20%40crloscuesta%20%F0%9F%98%8D%F0%9F%98%9C' +
          '&url=https://gitmoji.dev'
        }
        target="_blank"
        text="Share"
      />
    </div>
  </header>
)

export default Header
```

## File: `packages/website/src/components/Layout/Header/styles.module.css`
```css
.header {
  background-color: var(--primary);
  padding: 4.5em 2em;
  text-align: center;
}

.title {
  padding: 0.5em 0;
  margin: 0;
  font-size: 2em;
  color: var(--textInPrimary);
}

.buttons {
  padding: 1em 0;
  text-align: center;
}

.buttons a:first-child {
  margin-right: 1em;
}
```

## File: `packages/website/src/components/Layout/Header/Logo/index.tsx`
```tsx
'use client'

import { useState, useEffect } from 'react'

import Status, { LOGO_STATUSES, type EmojiLogoStatus } from './Status'
import styles from './styles.module.css'

const Logo = () => {
  const statuses = Object.values(LOGO_STATUSES)
  const [status, setStatus] = useState<EmojiLogoStatus>(null)

  useEffect(() => {
    setStatus(statuses[Math.floor(Math.random() * statuses.length)])
  }, [])

  return (
    <svg
      xmlns="http://www.w3.org/2000/svg"
      className={styles.logo}
      height="137px"
      width="457px"
      version="1.1"
      xmlnsXlink="http://www.w3.org/1999/xlink"
      viewBox="0 0 457 137"
    >
      <title>gitmoji</title>
      <g id="gitmoji" fillRule="evenodd" fill="none">
        <g id="Logo" transform="translate(-270 -430)">
          <g id="gitmoji" transform="translate(270 430)">
            <path
              d="m17.5 106c0.6 4 2.4 7 5.3 10 2.9 2 6.6 4 11.2 4 6.1 0 10.7-2 14-5s4.9-8 4.9-15.1v-5.1c-1.5 2.3-3.8 4.4-7.1 6.2-3.2 2-7.5 3-12.6 3-4.7 0-9.1-1-13.1-3-4.1-1.5-7.6-3.9-10.5-7-2.91-3-5.22-6.7-6.9-10.8-1.68-4.2-2.52-8.8-2.52-13.8 0.004-4.7 0.82-9.1 2.45-13.3s3.89-7.9 6.77-11c2.9-3.2 6.3-5.7 10.4-7.5 4-1.8 8.5-2.7 13.4-2.7 5.6 0 10.1 1 13.4 3 3.2 2 5.5 4.2 6.7 6.6v-8.3h18.5v63.2c0 4.6-0.7 9.6-2.1 13.6-1.4 5-3.6 9-6.6 12-3 4-6.8 6-11.5 8s-10.4 4-17 4c-4.9 0-9.3-1-13.3-3-4-1-7.5-3-10.5-5-2.94-3-5.34-5-7.16-8-1.82-4-2.98-7-3.46-10l17.3-5zm19-18.6c4.9 0 8.9-1.6 12-4.9 3.1-3.2 4.7-7.6 4.7-13.1s-1.7-9.8-4.9-13c-3.3-3.2-7.2-4.8-11.8-4.8-2.4 0-4.7 0.4-6.7 1.2-2.1 0.8-3.9 2-5.4 3.6-1.6 1.6-2.8 3.5-3.6 5.7-0.9 2.2-1.3 4.6-1.3 7.3 0 5.6 1.6 10 4.7 13.2 3.2 3.2 7.3 4.8 12.3 4.8zm54.7 19.6v-70.8h18.8v70.8h-18.8zm-2.3-94c0-3.39 1.1-6.22 3.4-8.53 2.3-2.3 5.1-3.45 8.7-3.45 3 0 6 1.15 8 3.45 2 2.31 4 5.14 4 8.53 0 3.1-2 5.9-4 8.2s-5 3.4-8 3.4c-3.6 0-6.4-1.1-8.7-3.4s-3.4-5.1-3.4-8.2zm65.1 23.2h15v16.9h-15v29.7c0 3.1 1 5.2 2 6.4 2 1.2 4 1.8 7 1.8 1 0 2 0 3-0.1s2-0.3 3-0.5v15.6c-1 1-3 1-4 1-2 1-4 1-7 1-7 0-13-2-17-6-4-3.6-6-9-6-15.9v-33h-12v-16.9h3c4 0 7-1.1 8-3.3 2-2.1 3-4.8 3-8v-9.9h17v21.2zm30 70.8v-70.8h18v8.6c1-1.7 2-3.3 4-4.6 1-1.4 3-2.5 5-3.3 2-0.9 4-1.6 6-2 2-0.5 4-0.8 6-0.8 5 0 9 1 13 3.1 3 2 6 4.9 8 8.7 3-4.3 6-7.3 10-9.1s8-2.7 12-2.7 7 0.5 10 1.5c3 1.1 6 2.7 8 4.9 3 2.2 4 5 6 8.4 1 3.4 2 7.5 2 12.2v45.9h-19v-42c0-3.9 0-7.1-2-9.6-2-2.6-6-3.8-10-3.8s-7 1.3-10 4.1c-2 2.7-3 6-3 9.8v41.5h-19v-42c0-3.9-1-7.1-3-9.6-2-2.6-5-3.8-10-3.8-4 0-7 1.3-9 4-3 2.7-4 6-4 9.9v41.5h-19zm159-15.3c3 0 5-0.4 7-1.3 2-0.8 4-2.1 6-3.8 1-1.7 3-3.7 4-6.2s1-5.5 1-8.8c0-3.4 0-6.3-1-8.8s-3-4.6-4-6.3c-2-1.7-4-2.9-6-3.8s-4-1.3-7-1.3c-2 0-4 0.4-6 1.3-3 0.9-5 2.1-6 3.8-2 1.7-3 3.8-4 6.3s-2 5.4-2 8.8c0 3.3 1 6.3 2 8.8s2 4.5 4 6.2c1 1.7 3 3 6 3.8 2 0.9 4 1.3 6 1.3zm0-57.7c6 0 11 0.9 15 2.8 5 1.9 9 4.5 12 7.8s6 7.2 8 11.9c2 4.6 2 9.6 2 15.1 0 5.4 0 10.5-2 15-2 4.6-5 8.5-8 11.9-3 3.5-7 5.5-12 7.5-4 2-9 3-15 3-5 0-10-1-14-3-5-2-9-4-12-7.5-4-3.4-6-7.3-8-11.9-2-4.5-3-9.6-3-15 0-5.5 1-10.5 3-15.1 2-4.7 4-8.6 8-11.9 3-3.3 7-5.9 12-7.8 4-1.9 9-2.8 14-2.8zm53 2.2h19v76.8c0 4-1 7-2 10-1 2-2 5-4 7s-4 4-7 5-6 2-9 2-6-1-8-1c-2-1-3-1-3-1v-16h2c1 1 2 1 4 1 3 0 5-1 6-3 1-1 2-3 2-6v-74.8zm-3-23.4c0-3.34 1-6.17 4-8.47 2-2.31 5-3.46 8-3.46 3 0.002 6 1.15 9 3.46 2 2.3 3 5.13 3 8.47 0 3.3-1 6-3 8.3-3 2.3-6 3.4-9 3.4s-6-1.1-8-3.4c-3-2.3-4-5-4-8.3zm42 94.2v-70.8h19v70.8h-19zm-2-94c0-3.39 1-6.22 3-8.53 3-2.3 5-3.45 9-3.45 3 0 6 1.15 8 3.45 2 2.31 4 5.14 4 8.53 0 3.1-2 5.9-4 8.2s-5 3.4-8 3.4c-4 0-6-1.1-9-3.4-2-2.3-3-5.1-3-8.2z"
              fill="#000"
            />
            <Status status={status} />
          </g>
        </g>
      </g>
    </svg>
  )
}

export default Logo
```

## File: `packages/website/src/components/Layout/Header/Logo/styles.module.css`
```css
.logo {
  width: 100%;
  height: 115px;
}
```

## File: `packages/website/src/components/Layout/Header/Logo/Status/index.tsx`
```tsx
import Joy from './Joy'
import Loved from './Loved'
import Sexy from './Sexy'
import Smiling from './Smiling'
import Sunglasses from './Sunglasses'
import Tongue from './Tongue'

export const LOGO_STATUSES = {
  JOY: 'JOY',
  LOVED: 'LOVED',
  SEXY: 'SEXY',
  SMILING: 'SMILING',
  SUNGLASSES: 'SUNGLASSES',
  TONGUE: 'TONGUE',
} as const

export type EmojiLogoStatus = keyof typeof LOGO_STATUSES | null

type Props = { status: EmojiLogoStatus }

const Status = (props: Props) => {
  switch (props.status) {
    case LOGO_STATUSES.JOY:
      return <Joy />
    case LOGO_STATUSES.LOVED:
      return <Loved />
    case LOGO_STATUSES.SEXY:
      return <Sexy />
    case LOGO_STATUSES.SMILING:
      return <Smiling />
    case LOGO_STATUSES.SUNGLASSES:
      return <Sunglasses />
    case LOGO_STATUSES.TONGUE:
      return <Tongue />
    default:
      return null
  }
}

export default Status
```

## File: `packages/website/src/components/Layout/Header/Logo/Status/Joy/index.tsx`
```tsx
export const Joy = () => (
  <g id="joy" transform="translate(304 32)">
    <g id="Group">
      <circle id="Oval" cy={39} cx={39} r={39} fill="#FFDD67" />
      <path
        id="Shape"
        fill="#664E27"
        d="m62 42.2c-0.5-0.7-1.5-0.6-2.5-0.6h-41c-1 0-2-0.1-2.5 0.6-5.1 6.4 0.9 25.4 23 25.4s28.1-19 23-25.4z"
      />
      <path
        id="Shape"
        fill="#4C3526"
        d="m41.4 51.7c-0.8-0.1-1.9 0.6-1.5 2.5 0.2 0.9 1.6 2.1 1.6 3.6 0 3.1-5 3.1-5 0 0-1.5 1.4-2.7 1.6-3.6 0.4-1.9-0.7-2.6-1.5-2.5-2 0-5.4 2.2-5.4 5.9 0 4.2 3.5 7.6 7.8 7.6s7.8-3.4 7.8-7.6c0-3.7-3.4-5.9-5.4-5.9z"
      />
      <path
        id="Shape"
        fill="#FF717F"
        d="m29 63.3c2.9 1.2 6.2 1.9 10 1.9s7.1-0.7 10-1.9c-2.8-1.4-6.1-2.2-10-2.2s-7.2 0.8-10 2.2z"
      />
      <path
        id="Shape"
        fill="#fff"
        d="m58.4 44.2h-38.8c-2.7 0-2.7 5.2-0.1 5.2h39c2.6 0 2.6-5.2-0.1-5.2z"
      />
      <g id="Shape" fill="#65B1EF" transform="translate(0 37.7)">
        <path d="m74.7 7.64c9.5 9.96-3.4 23.6-12.9 13.6-7-7.3-7.3-21.2-7.3-21.2 0 0.013 13.2 0.347 20.2 7.64zm-58.5 13.6c-9.46 10-22.4-3.6-12.9-13.6 7-7.25 20.2-7.59 20.2-7.59 0 0.003-0.3 13.9-7.3 21.2z" />
      </g>
      <g id="Shape" fill="#664E27" transform="translate(14.3 24.7)">
        <path d="m20.2 9.97c-2.4-6.64-6.1-9.97-9.7-9.97-3.66 0-7.3 3.33-9.71 9.97-0.243 0.63 1 1.83 1.63 1.23 2.34-2.48 5.14-3.47 8.08-3.47 2.9 0 5.7 0.99 8.1 3.47 0.6 0.6 1.8-0.6 1.6-1.23zm28.4 0c-2.4-6.64-6-9.97-9.7-9.97-3.6 0-7.3 3.33-9.7 9.97-0.2 0.63 1 1.83 1.6 1.23 2.4-2.48 5.2-3.47 8.1-3.47s5.7 0.99 8.1 3.47c0.6 0.6 1.9-0.6 1.6-1.23z" />
      </g>
    </g>
  </g>
)

export default Joy
```

## File: `packages/website/src/components/Layout/Header/Logo/Status/Loved/index.tsx`
```tsx
export const Loved = () => (
  <g id="loved" transform="translate(304 32)">
    <g id="Group">
      <path
        id="Shape"
        fill="#FFDD67"
        d="m78 39c0 21.5-17.5 39-39 39s-39-17.5-39-39 17.5-39 39-39 39 17.5 39 39z"
      />
      <path
        id="Shape"
        fill="#F46767"
        d="m77.8 14.6c-0.6-3.5-2.6-6.37-5.8-7.23-3.4-0.95-6.6 0.41-9.7 3.53-1.7-4.74-4.3-8.24-8.4-10-4.3-1.89-8.4-0.645-11 2.64-2.7 3.42-3.8 8.66-0.9 15.6 2.7 6.5 14.9 19.5 15.2 19.9 0.5-0.3 14-8.7 17.3-12.9 3.2-4 3.9-8.1 3.3-11.5zm-42.7-11.1c-2.6-3.28-6.7-4.53-11-2.68-4.1 1.8-6.7 5.3-8.4 10-3.1-3.12-6.25-4.48-9.7-3.53-3.16 0.86-5.2 3.73-5.8 7.23-0.599 3.4 0.072 7.5 3.31 11.5 3.31 4.2 16.8 12.6 17.3 12.9 0.3-0.4 12.5-13.4 15.2-19.9 2.9-6.9 1.8-12.1-0.9-15.6v0.04z"
      />
      <path
        id="Shape"
        fill="#664E27"
        d="m61.1 46.9c0-1.1-0.6-2.4-2.4-2.7-4.5-0.9-11.1-1.8-19.7-1.8s-15.2 0.9-19.7 1.8c-1.8 0.3-2.4 1.6-2.4 2.7 0 9.4 7.3 18.9 22.1 18.9s22.1-9.5 22.1-18.9z"
      />
      <path
        id="Shape"
        fill="#fff"
        d="m55.5 47.2c-2.9-0.5-8.9-1.3-16.5-1.3s-13.6 0.8-16.5 1.3c-1.7 0.3-1.8 0.9-1.7 1.9 0.1 0.6 0.2 1.3 0.4 2 0.2 0.9 0.3 1.2 1.6 1.1 2.5-0.3 29.9-0.3 32.4 0 1.3 0.1 1.4-0.2 1.6-1.1 0.2-0.7 0.3-1.4 0.4-2 0.1-1 0-1.6-1.7-1.9z"
      />
    </g>
  </g>
)

export default Loved
```

## File: `packages/website/src/components/Layout/Header/Logo/Status/Sexy/index.tsx`
```tsx
export const Sexy = () => (
  <g id="sexy" transform="translate(304 32)">
    <g id="Group">
      <ellipse id="Oval" rx={39} ry={39} cy={39} cx={39} fill="#FFDD67" />
      <ellipse
        id="Oval"
        rx="10.4"
        ry="10.4"
        cy="45.7"
        cx="66.1"
        fill="#FF717F"
      />
      <ellipse
        id="Oval"
        rx="10.4"
        ry="10.4"
        cy="45.7"
        cx="11.9"
        fill="#FF717F"
      />
      <path
        id="Shape"
        fill="#917524"
        d="m68.4 24.2c-3.5-4.2-8.7-6.7-14.2-6.6-0.8 0-1-2.9 0-2.9 6.3 0 12.4 2.8 16.4 7.7 0.6 0.7-1.7 2.4-2.2 1.8zm-44.6-6.8c-5.5 0-10.7 2.4-14.2 6.6-0.52 0.6-2.81-1.1-2.23-1.8 4.03-4.9 10.1-7.7 16.4-7.7 1 0 0.8 2.9 0 2.9z"
      />
      <ellipse id="Oval" rx="5.85" ry="5.85" cy="61.7" cx={39} fill="#664E27" />
      <path
        id="Shape"
        fill="#fff"
        d="m35.8 35.3c0 6.4-5.3 11.7-11.8 11.7-6.4 0-11.6-5.3-11.6-11.7 0-6.5 5.2-11.7 11.6-11.7 6.5 0 11.8 5.2 11.8 11.7z"
      />
      <ellipse id="Oval" rx="5.85" ry="5.85" cy="35.3" cx={24} fill="#664E27" />
      <g transform="translate(41.6 23.4)">
        <path
          id="Shape"
          fill="#fff"
          d="m24 11.9c0 6.4-5.2 11.7-11.6 11.7-6.51 0-11.8-5.3-11.8-11.7 0.05-6.48 5.29-11.7 11.8-11.7 6.4-0.022 11.6 5.22 11.6 11.7z"
        />
        <ellipse
          id="Oval"
          rx="5.85"
          ry="5.85"
          cy="11.9"
          cx="12.4"
          fill="#664E27"
        />
      </g>
    </g>
  </g>
)

export default Sexy
```

## File: `packages/website/src/components/Layout/Header/Logo/Status/Smiling/index.tsx`
```tsx
export const Smiling = () => (
  <g id="haha" transform="translate(304 32)">
    <g id="Group">
      <path
        id="Oval"
        fill="#FFDD67"
        d="m39 78c21.5 0 39-17.5 39-39s-17.5-39-39-39-39 17.5-39 39 17.5 39 39 39z"
      />
      <g id="Shape" fill="#664E27" transform="translate(11.7 20.5)">
        <path d="m52.9 2.09c0.3 0.15 0.4 0.47 0.4 0.79-0.1 0.32-0.3 0.57-0.6 0.63-3.5 0.52-7.3 1.12-10.8 3.07 5.2 0.87 9.4 3.52 11.7 6.32 0.5 0.6-0.1 1.4-0.7 1.2-6.2-2.3-12.6-3.5-20.6-2.6-0.6 0-1.2-0.3-1-0.9 2.1-9.39 14.2-12.9 21.6-8.51zm-51.2 0c-0.29 0.15-0.45 0.47-0.4 0.79s0.3 0.57 0.62 0.63c3.5 0.52 7.21 1.12 10.8 3.07-5.35 0.87-9.55 3.52-11.8 6.32-0.538 0.6 0.11 1.4 0.68 1.2 6.2-2.3 12.6-3.5 20.6-2.6 0.6 0 1.2-0.3 1-0.9-2.1-9.39-14.2-12.9-21.6-8.51h0.03z" />
      </g>
      <path
        id="Shape"
        fill="#664E27"
        d="m62 42.2c-0.5-0.7-1.5-0.6-2.5-0.6h-41c-1 0-2-0.1-2.5 0.6-5.1 6.4 0.9 25.4 23 25.4s28.1-19 23-25.4z"
      />
      <path
        id="Shape"
        fill="#4C3526"
        d="m41.4 51.7c-0.8-0.1-1.9 0.6-1.5 2.5 0.2 0.9 1.6 2.1 1.6 3.6 0 3.1-5 3.1-5 0 0-1.5 1.4-2.7 1.6-3.6 0.4-1.9-0.7-2.6-1.5-2.5-2 0-5.4 2.2-5.4 5.9 0 4.2 3.5 7.6 7.8 7.6s7.8-3.4 7.8-7.6c0-3.7-3.4-5.9-5.4-5.9z"
      />
      <path
        id="Shape"
        fill="#FF717F"
        d="m29 63.3c2.9 1.2 6.2 1.9 10 1.9s7.1-0.7 10-1.9c-2.8-1.4-6.1-2.2-10-2.2s-7.2 0.8-10 2.2z"
      />
      <path
        id="Shape"
        fill="#fff"
        d="m58.4 44.2h-38.8c-2.7 0-2.7 5.2-0.1 5.2h39c2.6 0 2.6-5.2-0.1-5.2z"
      />
    </g>
  </g>
)

export default Smiling
```

## File: `packages/website/src/components/Layout/Header/Logo/Status/Sunglasses/index.tsx`
```tsx
export const Sunglasses = () => (
  <g id="sunglasses" transform="translate(304 32)">
    <g id="Group">
      <path
        id="Shape"
        fill="#FFDD67"
        d="m39 0c21.5 0 39 17.5 39 39s-17.5 39-39 39-39-17.5-39-39 17.5-39 39-39"
      />
      <path
        id="Shape"
        fill="#494949"
        d="m44 24c-2.9 1.4-7.1 1.4-10 0-3.1-1.6-6.8-2.6-11.3-2.9-4.3-0.4-13.6-0.4-18.2 1.2-0.52 0.2-1.04 0.4-1.55 0.7-0.28 0.1-0.34 0.2-0.34 0.8v0.7c0 1.3-0.16 0.8 0.76 1.3 1.8 1 2.82 3.8 3.36 7.5 0.78 5.5 3.47 8.9 7.87 10.6 4 1.5 8.5 1.5 12.6-0.2 2.2-0.8 4.1-2.2 5.6-4.5 2.7-3.9 1.9-6.4 3.3-9.8 1.2-2.9 4.6-2.9 5.8 0 1.4 3.4 0.6 5.9 3.3 9.8 1.5 2.3 3.4 3.7 5.6 4.5 4.1 1.7 8.6 1.7 12.6 0.2 4.4-1.7 7.1-5.1 7.9-10.6 0.5-3.7 1.5-6.5 3.3-7.5 0.9-0.5 0.8 0 0.8-1.3v-0.7c0-0.6-0.1-0.7-0.4-0.8-0.5-0.3-1-0.5-1.5-0.7-4.6-1.6-13.9-1.6-18.2-1.2-4.5 0.3-8.2 1.3-11.3 2.9"
      />
      <path
        id="Shape"
        fill="#664E27"
        d="m55.4 52.4c-10.6 7.3-22.3 7.3-32.8 0-1.2-0.9-2.4 0.6-1.5 2 3.2 5.3 9.6 10 17.9 10s14.7-4.7 17.9-10c0.9-1.4-0.3-2.9-1.5-2z"
      />
    </g>
  </g>
)

export default Sunglasses
```

## File: `packages/website/src/components/Layout/Header/Logo/Status/Tongue/index.tsx`
```tsx
export const Tongue = () => (
  <g id="tongue" transform="translate(304 32)">
    <g id="Group">
      <ellipse id="Oval" rx={39} ry={39} cy={39} cx={39} fill="#FFDD67" />
      <path
        id="Shape"
        fill="#fff"
        d="m38 29.4c0 7.1-5.8 13-13 13s-13-5.9-13-13c0-7.2 5.8-13 13-13s13 5.8 13 13z"
      />
      <ellipse id="Oval" rx="5.85" ry="5.85" cy="29.4" cx={25} fill="#664E27" />
      <path
        id="Shape"
        fill="#664E27"
        d="m63.7 35.3c-2.5-5.3-6.1-8-9.7-8-3.7 0-7.3 2.7-9.8 8-0.2 0.5 1 1.5 1.7 0.9 2.3-1.9 5.1-2.7 8.1-2.7 2.9 0 5.7 0.8 8 2.7 0.7 0.6 1.9-0.4 1.7-0.9z"
      />
      <g id="Shape" transform="translate(16.9 46.8)">
        <path
          d="m42.7 0h-41.2c-0.989 0-1.5 0.659-1.5 1.3 0.0013 9.5 7.75 19.5 22.1 19.5s22.1-10 22.1-19.5c0-0.641-0.5-1.3-1.5-1.3z"
          fill="#664E27"
        />
        <path
          d="m34 7.8h-11.9-11.9c-0.95 0-1.1 0.41-1.1 1.1v5.2c0 11.4 5.8 17.1 13 17.1s13-5.7 13-17.1v-5.2c0-0.69-0.1-1.1-1.1-1.1z"
          fill="#FF717F"
        />
        <polygon points="24 7.8 22.1 25.7 20.2 7.8" fill="#E2596C" />
      </g>
    </g>
  </g>
)

export default Tongue
```

## File: `packages/website/src/components/Layout/__tests__/layout.spec.tsx`
```tsx
import { render, screen } from '@testing-library/react'

import Layout from '../index'
import Status, { LOGO_STATUSES } from '../Header/Logo/Status'
import * as stubs from './stubs'

jest.mock('next/navigation', () => ({
  usePathname: jest.fn(() => '/'),
}))

describe('Layout', () => {
  beforeAll(() => {
    Math.random = jest.fn().mockReturnValue(1)
  })

  beforeEach(() => {
    jest.clearAllMocks()
  })

  it('should render the component with children', () => {
    render(
      <Layout {...stubs.props}>
        <p>Some children</p>
      </Layout>,
    )

    expect(screen.getByText('Some children')).toBeInTheDocument()
  })

  describe('Logo', () => {
    Object.values(LOGO_STATUSES)
      .map((status) => status)
      .forEach((status) => {
        it('should render Logo with status ' + status, () => {
          const { container } = render(<Status status={status} />)

          expect(container.firstChild).toBeInTheDocument()
        })
      })
  })
})
```

## File: `packages/website/src/components/Layout/__tests__/stubs.ts`
```typescript
export const props = {
  headerWithSocialButtons: true,
}
```

## File: `packages/website/src/utils/theme/theme.css`
```css
:root {
  --background: #ffffff;
  --primary: #ffdd67;
  --primaryShadow: #ffcc1b;
  --secondary: #ff5a79;
  --secondaryShadow: #f3002e;
  --textInPrimary: #000000;
  --textInSecondary: #ffffff;
  --footerBackground: #00e5ff;
  --cardBackground: #ffffff;
  --cardText: #999999;
  --emojiCodeText: #000000;
  --cardShadow: rgba(168, 182, 191, 0.6);
  --notificationText: #ffffff;
  --notificationShadow: rgba(0, 0, 0, 0.05);
  --notificationEmojiCodeColor: rgba(0, 0, 0, 0.85);
  --menuBackground: #ff5a79;
  --carbonAdBadgeBackground: #f1f1f1;
}

[data-theme='dark'] {
  --background: #121212;
  --primary: #ffdd67;
  --primaryShadow: #ffcc1b;
  --secondary: #ff5a79;
  --secondaryShadow: #f3002e;
  --textInPrimary: #000000;
  --textInSecondary: #ffffff;
  --footerBackground: #00e5ff;
  --cardBackground: #2b2b2b;
  --cardText: #ffffff;
  --emojiCodeText: #ffffff;
  --cardShadow: none;
  --notificationText: #ffffff;
  --notificationShadow: rgba(0, 0, 0, 0.05);
  --notificationEmojiCodeColor: rgba(0, 0, 0, 0.85);
  --menuBackground: #ff5a79;
  --carbonAdBadgeBackground: #2b2b2b;
}

[data-theme='dark'] body {
  color: var(--cardText);
}

html,
body {
  background-color: var(--background);
  margin: 0;
  padding: 0;
  font-size: 16.5px;
  font-family:
    Avenir,
    -apple-system,
    BlinkMacSystemFont,
    'Segoe UI',
    'Roboto',
    'Oxygen',
    'Ubuntu',
    'Cantarell',
    'Fira Sans',
    'Droid Sans',
    'Helvetica Neue',
    sans-serif;
}

h1 {
  font-size: 2em;
}

a {
  text-decoration: none;
  color: var(--secondary);
}

a:hover {
  animation: zomg 0.5s infinite;
}

@media (prefers-reduced-motion: reduce) {
  a:hover {
    animation: none;
    text-decoration: underline;
  }
}

code {
  font-family:
    Avenir,
    -apple-system,
    BlinkMacSystemFont,
    'Segoe UI',
    'Roboto',
    'Oxygen',
    'Ubuntu',
    'Cantarell',
    'Fira Sans',
    'Droid Sans',
    'Helvetica Neue',
    sans-serif;
  font-weight: 700;
  font-size: 1.25em;
  word-break: break-all;
}

section {
  padding: 0.5em;
}

pre {
  background-color: var(--primary);
  border-radius: 4px;
  box-shadow: 0 4px var(--primaryShadow);
  color: var(--textInPrimary);
  padding: 1em;
}

.overflow-hidden {
  overflow: hidden;
}

.overflow-x-adjust {
  overflow-x: auto;
}

.wrap {
  max-width: 1100px;
  margin: 0 auto;
}

main.wrap {
  padding: 2em;
}

@keyframes zomg {
  0%,
  100% {
    color: #7ccdea;
  }

  16% {
    color: #0074d9;
  }

  32% {
    color: #2ecc40;
  }

  48% {
    color: #ffdc00;
  }

  64% {
    color: #b10dc9;
  }

  80% {
    color: #ff4136;
  }
}

@media (min-width: 2048px) {
  html,
  body {
    font-size: 19px;
  }
}

/* Flexboxgrid critical */

.col-sm-2,
.col-xs-12,
.col-xs-3,
.row {
  box-sizing: border-box;
}
.container {
  margin-right: auto;
  margin-left: auto;
}
.row {
  display: -webkit-box;
  display: -webkit-flex;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-flex: 0;
  -webkit-flex: 0 1 auto;
  -ms-flex: 0 1 auto;
  flex: 0 1 auto;
  -webkit-box-orient: horizontal;
  -webkit-box-direction: normal;
  -webkit-flex-direction: row;
  -ms-flex-direction: row;
  flex-direction: row;
  -webkit-flex-wrap: wrap;
  -ms-flex-wrap: wrap;
  flex-wrap: wrap;
  margin-right: -0.5rem;
  margin-left: -0.5rem;
}
.col-xs-12,
.col-xs-3 {
  -webkit-box-flex: 0;
  -webkit-flex: 0 0 auto;
  -ms-flex: 0 0 auto;
  flex: 0 0 auto;
  padding-right: 1.25rem;
  padding-left: 1.25rem;
}
.col-xs-12 {
  -webkit-flex-basis: 100%;
  -ms-flex-preferred-size: 100%;
  flex-basis: 100%;
  max-width: 100%;
}
.col-xs-3 {
  -ms-flex-preferred-size: 25%;
  flex-basis: 25%;
  max-width: 25%;
}
.center-xs {
  -webkit-box-pack: center;
  -webkit-justify-content: center;
  -ms-flex-pack: center;
  justify-content: center;
  text-align: center;
}
.middle-xs {
  -webkit-box-align: center;
  -webkit-align-items: center;
  -ms-flex-align: center;
  align-items: center;
}
@media only screen and (min-width: 48em) {
  .container {
    width: 49rem;
  }
  .col-sm-2,
  .col-sm-6 {
    box-sizing: border-box;
    -webkit-box-flex: 0;
    -webkit-flex: 0 0 auto;
    -ms-flex: 0 0 auto;
    flex: 0 0 auto;
    padding-right: 1.25rem;
    padding-left: 1.25rem;
  }
  .col-sm-6 {
    -webkit-flex-basis: 50%;
    -ms-flex-preferred-size: 50%;
    flex-basis: 50%;
    max-width: 50%;
  }
  .col-sm-2 {
    -ms-flex-preferred-size: 16.66666667%;
    flex-basis: 16.66666667%;
    max-width: 16.66666667%;
  }
}
@media only screen and (min-width: 64em) {
  .container {
    width: 65rem;
  }
  .col-md-3 {
    box-sizing: border-box;
    -webkit-box-flex: 0;
    -webkit-flex: 0 0 auto;
    -ms-flex: 0 0 auto;
    flex: 0 0 auto;
    padding-right: 1.25rem;
    padding-left: 1.25rem;
    -ms-flex-preferred-size: 25%;
    flex-basis: 25%;
    max-width: 25%;
  }
  .col-md-4 {
    -ms-flex-preferred-size: 33.33333333%;
    flex-basis: 33.33333333%;
    max-width: 33.33333333%;
  }
}
```

## File: `packages/website/src/__tests__/pages.spec.tsx`
```tsx
import { render, screen } from '@testing-library/react'

import RootLayout from '../app/layout'
import Home from '../app/page'
import About from '../app/about/page'
import Specification from '../app/specification/page'
import RelatedTools from '../app/related-tools/page'

jest.mock('next/navigation', () => ({
  useRouter: jest.fn(() => ({
    push: jest.fn(),
    replace: jest.fn(),
    prefetch: jest.fn(),
  })),
  useSearchParams: jest.fn(() => new URLSearchParams()),
  usePathname: jest.fn(() => '/'),
}))

jest.mock('next-themes', () => ({
  ThemeProvider: ({ children }: { children: React.ReactNode }) => (
    <div>{children}</div>
  ),
  useTheme: jest.fn(() => ({
    resolvedTheme: 'light',
    setTheme: jest.fn(),
  })),
}))

describe('Pages', () => {
  beforeAll(() => {
    Math.random = jest.fn().mockReturnValue(1)
  })

  describe('RootLayout', () => {
    it('should include theme provider and layout wrapper', () => {
      expect(RootLayout).toBeDefined()
      expect(typeof RootLayout).toBe('function')
    })
  })

  describe('Home', () => {
    it('should render the page', () => {
      const { container } = render(<Home />)
      expect(container.firstChild).toBeInTheDocument()
    })
  })

  describe('About', () => {
    it('should render the page with about content', () => {
      render(<About />)
      expect(screen.getByText(/About/i)).toBeInTheDocument()
    })
  })

  describe('Specification', () => {
    it('should render the page with specification content', () => {
      render(<Specification />)
      const heading = screen.getByRole('heading', {
        name: /Specification/i,
        level: 1,
      })
      expect(heading).toBeInTheDocument()
    })
  })

  describe('Related tools', () => {
    it('should render the page', () => {
      render(<RelatedTools />)
      expect(screen.getByText(/Related Tools/i)).toBeInTheDocument()
    })
  })
})
```

## File: `packages/website/src/__tests__/stubs.tsx`
```tsx
export const appProps = {
  Component: (props: object) => <div {...props}>Component</div>,
  pageProps: { test: '' },
}

export const contributors = [
  {
    url: 'https://github.com/profile',
    avatar: 'https://github.com/avatar',
    id: 'contributor-id-123',
  },
]

export const contributorsMock = [
  {
    html_url: 'https://github.com/profile',
    avatar_url: 'https://github.com/avatar',
    id: 'contributor-id-123',
    login: 'carloscuesta',
  },
]
```

## File: `packages/website/__mocks__/svg.js`
```javascript
module.exports = 'svg-mock'
```


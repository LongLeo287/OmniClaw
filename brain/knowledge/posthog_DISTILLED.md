---
id: posthog
type: knowledge
owner: OA_Triage
---
# posthog
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
    "name": "@posthog/root",
    "version": "0.0.0",
    "description": "",
    "homepage": "https://github.com/posthog/posthog#readme",
    "bugs": {
        "url": "https://github.com/posthog/posthog/issues"
    },
    "license": "MIT",
    "author": "PostHog Inc.",
    "repository": {
        "type": "git",
        "url": "https://github.com/posthog/posthog.git"
    },
    "browser": {
        "path": "path-browserify"
    },
    "scripts": {
        "prepare": "husky install",
        "schema:build": "bin/hogli build:schema",
        "openapi:build": "bin/hogli build:openapi",
        "schema:build:python": "bash bin/build-schema-python.sh",
        "taxonomy:build": "pnpm run taxonomy:build:json",
        "taxonomy:build:json": "python bin/build-taxonomy-json.py",
        "grammar:build": "pnpm grammar:build:python && pnpm grammar:build:cpp",
        "grammar:build:python": "cd posthog/hogql/grammar && cat HogQLLexer.python.g4 > HogQLLexer.g4 && tail -n +2 HogQLLexer.common.g4 |sed s/isOpeningTag/self.isOpeningTag/ >> HogQLLexer.g4 && antlr -Dlanguage=Python3 HogQLLexer.g4 && rm HogQLLexer.g4 && antlr -visitor -no-listener -Dlanguage=Python3 HogQLParser.g4",
        "grammar:build:cpp": "cd posthog/hogql/grammar && cat HogQLLexer.cpp.g4 > HogQLLexer.g4 && tail -n +2 HogQLLexer.common.g4 >> HogQLLexer.g4 && antlr -o ../../../common/hogql_parser -Dlanguage=Cpp HogQLLexer.g4 && rm HogQLLexer.g4 && antlr -o ../../../common/hogql_parser -visitor -no-listener -Dlanguage=Cpp HogQLParser.g4",
        "build:products": "pnpm --filter=@posthog/frontend run build:products",
        "generate:source-configs": "DEBUG=1 python manage.py generate_source_configs",
        "// DEPRECATED - use hogli migrations:run instead": "",
        "dev:migrate:postgres": "export DEBUG=1 && source env/bin/activate && python manage.py migrate",
        "// DEPRECATED - use hogli migrations:run instead ": "",
        "dev:migrate:clickhouse": "export DEBUG=1 && source env/bin/activate && python manage.py migrate_clickhouse",
        "mypy-baseline-sync": "TEST=1 mypy . | mypy-baseline sync",
        "mypy-check": "TEST=1 mypy . | mypy-baseline filter",
        "// DEPRECATED - use hogli format:python instead": "",
        "format:backend": "./bin/ruff.sh format .",
        "// DEPRECATED - use hogli format:js instead": "",
        "format:frontend": "oxfmt --check \"{products,frontend/src,docs}/**/*.{js,mjs,ts,tsx,json,yaml,yml,css,scss}\"",
        "format:frontend:check": "pnpm run format:frontend -- --check",
        "// DEPRECATED - use hogli format instead": "",
        "format": "pnpm format:backend && pnpm format:frontend",
        "cleandep": "rm -rf node_modules && pnpm -r exec rm -rf node_modules",
        "storybook": "pnpm turbo --filter=@posthog/storybook start",
        "// DEPRECATED - use hogli start instead": "",
        "start": "./bin/start",
        "postinstall": "git config --get blame.ignoreRevsFile > /dev/null 2>&1 || git config blame.ignoreRevsFile .git-blame-ignore-revs > /dev/null 2>&1 || true; [ ! -f bin/fix-rdkafka-paths ] || bin/fix-rdkafka-paths",
        "lint": "pnpm lint:js && pnpm lint:css",
        "lint:js": "oxlint --quiet",
        "lint:css": "stylelint \"(frontend|products)/**/*.{css,scss}\"",
        "test:unit": "pnpm --filter=@posthog/frontend test"
    },
    "dependencies": {
        "concurrently": "catalog:",
        "fuse.js": "catalog:",
        "husky": "catalog:",
        "lint-staged": "catalog:",
        "uuid": "^10.0.0"
    },
    "devDependencies": {
        "@parcel/packager-ts": "catalog:",
        "@parcel/transformer-typescript-types": "catalog:",
        "@types/uuid": "^10.0.0",
        "markdownlint-cli2": "^0.18.1",
        "oxfmt": "catalog:",
        "oxlint": "^1.8.0",
        "playwright": "1.45.0",
        "stylelint": "^15.11.0",
        "stylelint-config-recess-order": "^4.6.0",
        "stylelint-config-standard-scss": "^11.1.0",
        "stylelint-order": "^6.0.4",
        "syncpack": "^13.0.4",
        "turbo": "^2.4.2"
    },
    "optionalDependencies": {
        "fsevents": "^2.3.3"
    },
    "lint-staged": {
        ".claude/settings.json": "sh -c 'printf \"\\n\\033[31mDo not commit .claude/settings.json — personal permissions belong in .claude/settings.local.json (gitignored).\\nUnstage with: git restore --staged .claude/settings.json\\033[0m\\n\\n\" >&2 && exit 1'",
        ".claude/hooks/**": "sh -c 'printf \"\\n\\033[33mWarning: hooks in .claude/ are reserved for env bootstrapping (SessionStart only).\\nPrefer skills, AGENTS.md instructions, or lint-staged rules. See Agent automation in AGENTS.md.\\033[0m\\n\\n\"'",
        "products/**/manifest.tsx": [
            "bin/hogli format:js",
            "sh -c 'pnpm build:products && git add frontend/src/products.tsx frontend/src/products.json'"
        ],
        "!(**/.sqlx/**)*.{json,yaml,yml}": "bin/hogli format:yaml",
        "*.{css,scss}": "bin/hogli format:css",
        "{playwright,frontend,products,common,ee,services,docs}/**/*.{js,jsx,mjs,ts,tsx}": "bin/hogli format:js",
        "nodejs/**/*.{js,jsx,mjs,ts,tsx}": "bin/hogli format:nodejs",
        "funnel-udf/**/*.rs": "bin/hogli format:rust",
        "!(posthog/hogql/grammar/*|posthog/personhog_client/proto/generated/*|products/*/skills/*/scripts/*)*.{py,pyi}": [
            "bin/hogli lint:python:fix",
            "bin/hogli format:python"
        ],
        "*.{md,mdx}": "bin/hogli format:markdown"
    },
    "browserslist": {
        "development": [
            "last 2 chrome versions",
            "last 2 firefox versions",
            "last 2 edge versions"
        ],
        "production": [
            "defaults and not op_mini all"
        ]
    },
    "engines": {
        "node": ">=24 <25"
    },
    "packageManager": "pnpm@10.29.3",
    "pnpm": {
        "// Fix React version to a fixed known good version across the monorepo": "",
        "overrides": {
            "@modelcontextprotocol/sdk": "^1.26.0",
            "@types/react": "18.3.27",
            "@types/react-dom": "18.3.7",
            "cipher-base": ">=1.0.5",
            "d3-geo": ">=3.1.0",
            "d3-selection": ">=3.0.0",
            "d3-zoom": ">=3.0.0",
            "form-data": ">=4.0.4",
            "node-forge": "1.3.2",
            "pbkdf2": ">=3.1.3",
            "react": "18.3.1",
            "react-dom": "18.3.1",
            "sha.js": ">=2.4.12",
            "typescript": "5.6.3"
        },
        "patchedDependencies": {
            "heatmap.js@2.0.5": "patches/heatmap.js@2.0.5.patch",
            "dayjs@1.11.11": "patches/dayjs@1.11.11.patch",
            "chartjs-plugin-crosshair@2.0.0": "patches/chartjs-plugin-crosshair@2.0.0.patch"
        },
        "// Known dependencies that we need preinstall scripts for, add new ones with caution": "",
        "onlyBuiltDependencies": [
            "@modelcontextprotocol/ext-apps",
            "@parcel/watcher",
            "chartjs-plugin-stacked100",
            "@swc/core",
            "core-js",
            "core-js-pure",
            "cpu-features",
            "esbuild",
            "lmdb",
            "lz4",
            "msgpackr-extract",
            "msw",
            "node-gyp",
            "node-rdkafka",
            "protobufjs",
            "re2",
            "sharp",
            "ssh2",
            "unrs-resolver",
            "workerd"
        ]
    }
}

```

### File: README.md
```md
<p align="center">
  <img alt="posthoglogo" src="https://user-images.githubusercontent.com/65415371/205059737-c8a4f836-4889-4654-902e-f302b187b6a0.png">
</p>
<p align="center">
  <a href='https://posthog.com/contributors'><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/posthog/posthog"/></a>
  <a href='http://makeapullrequest.com'><img alt='PRs Welcome' src='https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=shields'/></a>
  <img alt="Docker Pulls" src="https://img.shields.io/docker/pulls/posthog/posthog"/>
  <a href="https://github.com/PostHog/posthog/commits/master"><img alt="GitHub commit activity" src="https://img.shields.io/github/commit-activity/m/posthog/posthog"/> </a>
  <a href="https://github.com/PostHog/posthog/issues?q=is%3Aissue%20state%3Aclosed"><img alt="GitHub closed issues" src="https://img.shields.io/github/issues-closed/posthog/posthog"/> </a>
</p>

<p align="center">
  <a href="https://posthog.com/docs">Docs</a> - <a href="https://posthog.com/community">Community</a> - <a href="https://posthog.com/roadmap">Roadmap</a> - <a href="https://posthog.com/why">Why PostHog?</a> - <a href="https://posthog.com/changelog">Changelog</a> - <a href="https://github.com/PostHog/posthog/issues/new?assignees=&labels=bug&template=bug_report.yml">Bug reports</a>
</p>

<p align="center">
  <a href="https://www.youtube.com/watch?v=2jQco8hEvTI">
    <img src="https://res.cloudinary.com/dmukukwp6/image/upload/demo_thumb_68d0d8d56d" alt="PostHog Demonstration">
  </a>
</p>

## PostHog is an all-in-one, open source platform for building successful products

[PostHog](https://posthog.com/) provides every tool you need to build a successful product including:

- [Product Analytics](https://posthog.com/product-analytics): Autocapture or manually instrument event-based analytics to understand user behavior and analyze data with visualization or SQL.
- [Web Analytics](https://posthog.com/web-analytics): Monitor web traffic and user sessions with a GA-like dashboard. Easily monitor conversion, web vitals, and revenue.
- [Session Replays](https://posthog.com/session-replay): Watch real user sessions of interactions with your website or mobile app to diagnose issues and understand user behavior.
- [Feature Flags](https://posthog.com/feature-flags): Safely roll out features to select users or cohorts with feature flags.
- [Experiments](https://posthog.com/experiments): Test changes and measure their statistical impact on goal metrics. Set up experiments with no-code too.
- [Error Tracking](https://posthog.com/error-tracking): Track errors, get alerts, and resolve issues to improve your product.
- [Surveys](https://posthog.com/surveys): Ask anything with our collection of no-code survey templates, or build custom surveys with our survey builder.
- [Data warehouse](https://posthog.com/data-warehouse): Sync data from external tools like Stripe, Hubspot, your data warehouse, and more. Query it alongside your product data.
- [Data pipelines](https://posthog.com/cdp): Run custom filters and transformations on your incoming data. Send it to 25+ tools or any webhook in real time or batch export large amounts to your warehouse.
- [LLM analytics](https://posthog.com/docs/llm-analytics): Capture traces, generations, latency, and cost for your LLM-powered app.
- [Workflows](https://posthog.com/docs/workflows): Create workflows that automate actions or send messages to your users.

Best of all, all of this is free to use with a [generous monthly free tier](https://posthog.com/pricing) for each product. Get started by signing up for [PostHog Cloud US](https://us.posthog.com/signup) or [PostHog Cloud EU](https://eu.posthog.com/signup).

## Table of Contents

- [PostHog is an all-in-one, open source platform for building successful products](#posthog-is-an-all-in-one-open-source-platform-for-building-successful-products)
- [Table of Contents](#table-of-contents)
- [Getting started with PostHog](#getting-started-with-posthog)
  - [PostHog Cloud (Recommended)](#posthog-cloud-recommended)
  - [Self-hosting the open-source hobby deploy (Advanced)](#self-hosting-the-open-source-hobby-deploy-advanced)
- [Setting up PostHog](#setting-up-posthog)
- [Learning more about PostHog](#learning-more-about-posthog)
- [Contributing](#contributing)
- [Open-source vs. paid](#open-source-vs-paid)
- [We’re hiring!](#were-hiring)

## Getting started with PostHog

### PostHog Cloud (Recommended)

The fastest and most reliable way to get started with PostHog is signing up for free to [PostHog Cloud](https://us.posthog.com/signup) or [PostHog Cloud EU](https://eu.posthog.com/signup). Your first 1 million events, 5k recordings, 1M flag requests, 100k exceptions, and 1500 survey responses are free every month, after which you pay based on usage.

### Self-hosting the open-source hobby deploy (Advanced)

If you want to self-host PostHog, you can deploy a hobby instance in one line on Linux with Docker (recommended 4GB memory):

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/posthog/posthog/HEAD/bin/deploy-hobby)"
```

Open source deployments should scale to approximately 100k events per month, after which we recommend [migrating to a PostHog Cloud](https://posthog.com/docs/migrate/migrate-to-cloud).

We _do not_ provide customer support or offer guarantees for open source deployments. See our [self-hosting docs](https://posthog.com/docs/self-host), [troubleshooting guide](https://posthog.com/docs/self-host/deploy/troubleshooting), and [disclaimer](https://posthog.com/docs/self-host/open-source/disclaimer) for more info.

## Setting up PostHog

Once you've got a PostHog instance, you can set it up by installing our [JavaScript web snippet](https://posthog.com/docs/getting-started/install?tab=snippet), one of [our SDKs](https://posthog.com/docs/getting-started/install?tab=sdks), or by [using our API](https://posthog.com/docs/getting-started/install?tab=api).

We have SDKs and libraries for popular languages and frameworks like:

| Frontend                                              | Mobile                                                          | Backend                                             |
| ----------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------- |
| [JavaScript](https://posthog.com/docs/libraries/js)   | [React Native](https://posthog.com/docs/libraries/react-native) | [Python](https://posthog.com/docs/libraries/python) |
| [Next.js](https://posthog.com/docs/libraries/next-js) | [Android](https://posthog.com/docs/libraries/android)           | [Node](https://posthog.com/docs/libraries/node)     |
| [React](https://posthog.com/docs/libraries/react)     | [iOS](https://posthog.com/docs/libraries/ios)                   | [PHP](https://posthog.com/docs/libraries/php)       |
| [Vue](https://posthog.com/docs/libraries/vue-js)      | [Flutter](https://posthog.com/docs/libraries/flutter)           | [Ruby](https://posthog.com/docs/libraries/ruby)     |

Beyond this, we have docs and guides for [Go](https://posthog.com/docs/libraries/go), [.NET/C#](https://posthog.com/docs/libraries/dotnet), [Django](https://posthog.com/docs/libraries/django), [Angular](https://posthog.com/docs/libraries/angular), [WordPress](https://posthog.com/docs/libraries/wordpress), [Webflow](https://posthog.com/docs/libraries/webflow), and more.

Once you've installed PostHog, see our [product docs](https://posthog.com/docs/product-os) for more information on how to set up [product analytics](https://posthog.com/docs/product-analytics/capture-events), [web analytics](https://posthog.com/docs/web-analytics/getting-started), [session replays](https://posthog.com/docs/session-replay/how-to-watch-recordings), [feature flags](https://posthog.com/docs/feature-flags/creating-feature-flags), [experiments](https://posthog.com/docs/experiments/creating-an-experiment), [error tracking](https://posthog.com/docs/error-tracking/installation#setting-up-exception-autocapture), [surveys](https://posthog.com/docs/surveys/installation), [data warehouse](https://posthog.com/docs/cdp/sources), and more.

## Learning more about PostHog

Our code isn't the only thing that's open source 😳. We also open source our [company handbook](https://posthog.com/handbook) which details our [strategy](https://posthog.com/handbook/why-does-posthog-exist), [ways of working](https://posthog.com/handbook/company/culture), and [processes](https://posthog.com/handbook/team-structure).

Curious about how to make the most of PostHog? We wrote a guide to [winning with PostHog](https://posthog.com/docs/new-to-posthog/getting-hogpilled) which walks you through the basics of [measuring activation](https://posthog.com/docs/new-to-posthog/activation), [tracking retention](https://posthog.com/docs/new-to-posthog/retention), and [capturing revenue](https://posthog.com/docs/new-to-posthog/revenue).

## Contributing

We <3 contributions big and small:

- Vote on features or get early access to beta functionality in our [roadmap](https://posthog.com/roadmap)
- Open a PR (see our instructions on [developing PostHog locally](https://posthog.com/handbook/engineering/developing-locally))
- Submit a [feature request](https://github.com/PostHog/posthog/issues/new?assignees=&labels=enhancement%2C+feature&template=feature_request.yml) or [bug report](https://github.com/PostHog/posthog/issues/new?assignees=&labels=bug&template=bug_report.yml)

For an overview of the codebase structure, see [monorepo layout](docs/internal/monorepo-layout.md) and [products](products/README.md).

## Open-source vs. paid

This repo is available under the [MIT expat license](https://github.com/PostHog/posthog/blob/master/LICENSE), except for the `ee` directory (which has its [license here](https://github.com/PostHog/posthog/blob/master/ee/LICENSE)) if applicable.

Need _absolutely 💯% FOSS_? Check out our [posthog-foss](https://github.com/PostHog/posthog-foss) repository, which is purged of all proprietary code and features.

The pricing for our paid plan is completely transparent and available on [our pricing page](https://posthog.com/pricing).

## We're hiring!

<img src="https://res.cloudinary.com/dmukukwp6/image/upload/v1/posthog.com/src/components/Home/images/mission-control-hog" alt="Hedgehog working on a Mission Control Center" width="350px"/>

Hey! If you're reading this, you've proven yourself as a dedicated README reader.

You might also make a great addition to our team. We're growing fast [and would love for you to join us](https://posthog.com/careers).

```

### File: cli\README.md
```md
# The Posthog CLI

```bash
> posthog-cli --help
The command line interface for PostHog 🦔

Usage: posthog-cli [OPTIONS] <COMMAND>

Commands:
  login      Interactively authenticate with PostHog, storing a personal API token locally. You can also use the environment variables `POSTHOG_CLI_API_KEY`, `POSTHOG_CLI_PROJECT_ID` and `POSTHOG_CLI_HOST`
  query      Run a SQL query against any data you have in posthog. This is mostly for fun, and subject to change
  sourcemap  Upload a directory of bundled chunks to PostHog
  exp        Contains a set of experimental commands
  help       Print this message or the help of the given subcommand(s)

Options:
      --host <HOST>  The PostHog host to connect to [default: https://us.posthog.com]
  -h, --help         Print help
  -V, --version      Print version
```

## Env-based Authentication

You can authenticate with PostHog interactively for using the CLI locally, but if you'd like to use it in a CI/CD pipeline, we recommend using these environment variables:

- `POSTHOG_CLI_HOST`: The PostHog host to connect to [default: https://us.posthog.com]
- `POSTHOG_CLI_API_KEY`: [A posthog personal API key.](https://posthog.com/docs/api#private-endpoint-authentication) (also accepts `POSTHOG_CLI_TOKEN` for backward compatibility)
- `POSTHOG_CLI_PROJECT_ID`: The ID number of the project/environment to connect to. E.g. the "2" in `https://us.posthog.com/project/2` (also accepts `POSTHOG_CLI_ENV_ID` for backward compatibility)

### Personal API key scopes

Commands require different API scopes. Make sure to set these scopes on your personal API key:

| Command                       | Required Scopes                            |
| ----------------------------- | ------------------------------------------ |
| `query`                       | `query:read`                               |
| `sourcemap`                   | `error_tracking:write`                     |
| `exp endpoints list/get/pull` | `endpoint:read`                            |
| `exp endpoints push`          | `endpoint:write`, `insight_variable:write` |
| `exp endpoints run`           | `query:read`                               |
| `exp tasks`                   | `task:read`                                |

```

### File: common\README.md
```md
# Common

Shared libraries, tools, and utilities used across the monorepo.

**Transitional bucket** — new code should prefer `platform/`, `tools/`, `products/`, or `services/` depending on what it is. Items here will migrate to more specific locations over time.

- Internal RFC: https://github.com/PostHog/product-internal/pull/703
- Keep folder names `under_score` cased — dashes break Python imports

```

### File: docs\README.md
```md
# PostHog Documentation

Developer-focused documentation alongside code. Update docs in the same PR as your code changes.

## Structure

### `published/` - Published on posthog.com

Documentation published when merged to master. The URL mirrors the directory structure - just strip the `docs/published/` prefix:

```text
docs/published/docs/surveys/...          →  posthog.com/docs/surveys/...
docs/published/handbook/engineering/...  →  posthog.com/handbook/engineering/...
```

**Examples:**

- `published/docs/surveys/sdk-feature-support.md` → `/docs/surveys/sdk-feature-support`
- `published/handbook/engineering/developing-locally.md` → `/handbook/engineering/developing-locally`

### `internal/` - GitHub-only

Documentation that stays in the repository:

- Development workflows
- Migration patterns
- Team processes

**When to use**: Knowledge useful for the team but not for external users. We're open source, so "internal" means GitHub-only rather than truly private.

## Publishing Flow

```text
Engineer creates PR with /docs/published/** changes
  ↓
GitHub Action triggers posthog.com preview build
  ↓
Preview URL posted to PR
  ↓
Merge to master
  ↓
Docs go live on posthog.com
```

The posthog.com Gatsby build uses gatsby-source-git to clone this monorepo and pull files from `/docs/published/` during the build process.

## Guidelines

- All published docs must have YAML frontmatter
- Use relative links between docs: `../contributing/index.md`
- Docs about PostHog internals → here
- User product docs and tutorials → posthog.com repo

## Setup

For posthog.com team setting up the integration, see the PRs in PostHog/posthog.com repo.

```

### File: frontend\package.json
```json
{
    "name": "@posthog/frontend",
    "version": "0.0.0",
    "description": "",
    "homepage": "https://github.com/posthog/posthog#readme",
    "bugs": {
        "url": "https://github.com/posthog/posthog/issues"
    },
    "license": "MIT",
    "author": "PostHog Inc.",
    "repository": {
        "type": "git",
        "url": "https://github.com/posthog/posthog.git"
    },
    "browser": {
        "path": "path-browserify"
    },
    "scripts": {
        "copy-scripts": "mkdir -p dist/ && ./bin/copy-posthog-js",
        "clean": "rm -rf dist && mkdir dist",
        "build": "pnpm copy-scripts && pnpm build:esbuild",
        "build:esbuild": "DEBUG=0 node ./build.mjs",
        "build:products": "DEBUG=0 node build-products.mjs",
        "build:tailwind": "pnpm --filter=@posthog/tailwind build",
        "watch:tailwind": "pnpm --filter=@posthog/tailwind start",
        "start": "concurrently -n ESBUILD,TAILWIND -c yellow,blue \"pnpm start-http\" \"pnpm watch:tailwind\"",
        "start-http": "pnpm clean && pnpm copy-scripts && pnpm build:esbuild --dev",
        "start-docker": "pnpm start-http --host 0.0.0.0",
        "openapi:types": "node ./bin/generate-openapi-types.mjs",
        "typegen:check": "cd .. && NODE_OPTIONS=--max-old-space-size=8192 kea-typegen check",
        "typegen:clean": "cd .. && find frontend/src products common -type f -name '*Type.ts' -delete",
        "typegen:watch": "cd .. && NODE_OPTIONS=--max-old-space-size=8192 kea-typegen watch --delete --show-ts-errors --use-cache",
        "typegen:write": "cd .. && NODE_OPTIONS=--max-old-space-size=8192 kea-typegen write --delete --show-ts-errors --use-cache",
        "typegen:write:no-cache": "cd .. && NODE_OPTIONS=--max-old-space-size=8192 kea-typegen write --delete --show-ts-errors",
        "schema:build:json": "ts-node ./bin/build-schema-json.mjs && oxfmt ./src/queries/schema.json && ts-node ./bin/build-validators.mjs && oxfmt ./src/queries/validators.js",
        "test": "SHARD_IDX=${SHARD_INDEX:-1}; SHARD_TOTAL=${SHARD_COUNT:-1}; echo $SHARD_IDX/$SHARD_TOTAL; pnpm build:products && jest --testPathPattern='(frontend/|products/|common/)' --forceExit --shard=$SHARD_IDX/$SHARD_TOTAL",
        "jest": "pnpm build:products && jest",
        "typescript:check": "tsc --noEmit && echo \"No errors reported by tsc.\"",
        "lint": "cd .. && oxlint --quiet",
        "format": "cd .. && oxlint --fix --fix-suggestions --fix-dangerously --quiet && oxfmt \"./{products,frontend/src,docs}/**/*.{js,mjs,ts,tsx,json,yaml,yml,css,scss}\"",
        "visualize-toolbar-bundle": "pnpm exec esbuild-visualizer --metadata ./toolbar-esbuild-meta.json --filename=toolbar-esbuild-bundle-visualization.html",
        "check-toolbar-csp-eval": "node ./bin/check-toolbar-csp-eval.mjs",
        "start-vite": "pnpm build:products && concurrently -n VITE,TAILWIND,TOOLBAR -c green,yellow,magenta \"vite --host 0.0.0.0\" \"pnpm watch:tailwind\" \"pnpm watch:toolbar\"",
        "watch:toolbar": "node ./bin/build-toolbar.mjs --dev",
        "mobile-replay:web:schema:build:json": "ts-json-schema-generator -f ./tsconfig.json --path 'node_modules/@posthog/rrweb-types/dist/index.d.ts' --type 'eventWithTime' --expose all --no-top-ref --out ./src/scenes/session-recordings/mobile-replay/schema/web/rr-web-schema.json && oxfmt ./src/scenes/session-recordings/mobile-replay/schema/web/rr-web-schema.json",
        "mobile-replay:mobile:schema:build:json": "ts-json-schema-generator -f ./tsconfig.json --path './src/scenes/session-recordings/mobile-replay/mobile.types.ts' --type 'mobileEventWithTime' --expose all --no-top-ref --out ./src/scenes/session-recordings/mobile-replay/schema/mobile/rr-mobile-schema.json && oxfmt ./src/scenes/session-recordings/mobile-replay/schema/mobile/rr-mobile-schema.json",
        "mobile-replay:schema:build:json": "pnpm mobile-replay:web:schema:build:json && pnpm mobile-replay:mobile:schema:build:json",
        "build:survey-sdk-docs": "ts-node -r tsconfig-paths/register --transpile-only ./bin/docs/build-survey-sdk-docs.ts"
    },
    "dependencies": {
        "@babel/runtime": "^7.24.0",
        "@base-ui/react": "^1.3.0",
        "@dagrejs/dagre": "^1.1.5",
        "@dnd-kit/core": "^6.0.8",
        "@dnd-kit/modifiers": "^6.0.1",
        "@dnd-kit/sortable": "^7.0.2",
        "@dnd-kit/utilities": "^3.2.1",
        "@floating-ui/react": "^0.27.19",
        "@lottiefiles/react-lottie-player": "^3.4.7",
        "@marsidev/react-turnstile": "^1.4.2",
        "@medv/finder": "^4.0.2",
        "@microlink/react-json-view": "^1.26.2",
        "@microsoft/fetch-event-source": "^2.0.1",
        "@monaco-editor/react": "4.7.0",
        "@posthog/docs-onboarding": "workspace:*",
        "@posthog/esbuilder": "workspace:*",
        "@posthog/hedgehog-mode": "^0.0.48",
        "@posthog/hogql-parser": "1.3.35",
        "@posthog/hogvm": "workspace:*",
        "@posthog/icons": "^0.36.6",
        "@posthog/mosaic": "workspace:*",
        "@posthog/products-actions": "workspace:*",
        "@posthog/products-cohorts": "workspace:*",
        "@posthog/products-conversations": "workspace:*",
        "@posthog/products-customer-analytics": "workspace:*",
        "@posthog/products-dashboards": "workspace:*",
        "@posthog/products-early-access-features": "workspace:*",
        "@posthog/products-endpoints": "workspace:*",
        "@posthog/products-error-tracking": "workspace:*",
        "@posthog/products-experiments": "workspace:*",
        "@posthog/products-feature-flags": "workspace:*",
        "@posthog/products-games": "workspace:*",
        "@posthog/products-groups": "workspace:*",
        "@posthog/products-links": "workspace:*",
        "@posthog/products-live-debugger": "workspace:*",
        "@posthog/products-llm-analytics": "workspace:*",
        "@posthog/products-logs": "workspace:*",
        "@posthog/products-managed-migrations": "workspace:*",
        "@posthog/products-mcp-analytics": "workspace:*",
        "@posthog/products-mcp-store": "workspace:*",
        "@posthog/products-messaging": "workspace:*",
        "@posthog/products-metrics": "workspace:*",
        "@posthog/products-notebooks": "workspace:*",
        "@posthog/products-persons": "workspace:*",
        "@posthog/products-product-analytics": "workspace:*",
        "@posthog/products-replay": "workspace:*",
        "@posthog/products-revenue-analytics": "workspace:*",
        "@posthog/products-session-summaries": "workspace:*",
        "@posthog/products-surveys": "workspace:*",
        "@posthog/products-tasks": "workspace:*",
        "@posthog/products-tracing": "workspace:*",
        "@posthog/products-user-interviews": "workspace:*",
        "@posthog/products-visual-review": "workspace:*",
        "@posthog/products-web-analytics": "workspace:*",
        "@posthog/products-workflows": "workspace:*",
        "@posthog/replay-shared": "workspace:*",
        "@posthog/rrweb": "0.0.26",
        "@posthog/rrweb-plugin-console-record": "0.0.26",
        "@posthog/rrweb-types": "0.0.26",
        "@posthog/tailwind": "workspace:*",
        "@radix-ui/react-accordion": "^1.2.12",
        "@radix-ui/react-context-menu": "^2.2.16",
        "@radix-ui/react-dismissable-layer": "^1.1.11",
        "@radix-ui/react-dropdown-menu": "^2.1.16",
        "@radix-ui/react-hover-card": "^1.1.15",
        "@radix-ui/react-popover": "^1.1.15",
        "@radix-ui/react-select": "^2.2.6",
        "@radix-ui/react-slot": "^1.2.4",
        "@radix-ui/react-tabs": "^1.1.13",
        "@radix-ui/react-toggle-group": "^1.1.11",
        "@react-hook/size": "^2.1.2",
        "@sgratzl/chartjs-chart-boxplot": "^4.4.5",
        "@simplewebauthn/browser": "^13.2.2",
        "@stripe/react-stripe-js": "^2.8.0",
        "@stripe/stripe-js": "^4.5.0",
        "@tailwindcss/cli": "4.0.11",
        "@testing-library/dom": ">=9.3.4",
        "@tiptap/core": "^3.20.1",
        "@tiptap/extension-code-block-lowlight": "^3.20.1",
        "@tiptap/extension-color": "^3.20.1",
        "@tiptap/extension-document": "^3.20.1",
        "@tiptap/extension-drag-handle-react": "^3.20.1",
        "@tiptap/extension-floating-menu": "^3.20.1",
        "@tiptap/extension-heading": "^3.20.1",
        "@tiptap/extension-image": "^3.20.1",
        "@tiptap/extension-link": "^3.20.1",
        "@tiptap/extension-list": "^3.20.1",
        "@tiptap/extension-placeholder": "^3.20.1",
        "@tiptap/extension-table": "^3.20.1",
        "@tiptap/extension-table-of-contents": "^3.20.1",
        "@tiptap/extension-text-align": "^3.20.1",
        "@tiptap/extension-text-style": "^3.20.1",
        "@tiptap/extension-underline": "^3.20.1",
        "@tiptap/extensions": "^3.20.1",
        "@tiptap/html": "^3.20.1",
        "@tiptap/markdown": "^3.20.1",
        "@tiptap/pm": "^3.20.1",
        "@tiptap/react": "^3.20.1",
        "@tiptap/starter-kit": "^3.20.1",
        "@tiptap/suggestion": "^3.20.1",
        "@vitejs/plugin-react": "^4.7.0",
        "@xyflow/react": "^12.6.0",
        "ajv": "^8.12.0",
        "bintrees": "^1.0.2",
        "bloommx": "^1.0.3",
        "buffer": "^6.0.3",
        "chart.js": "^4.5.1",
        "chartjs-adapter-dayjs-3": "^1.2.3",
        "chartjs-plugin-annotation": "^3.1.0",
        "chartjs-plugin-crosshair": "2.0.0",
        "chartjs-plugin-datalabels": "^2.2.0",
        "chartjs-plugin-stacked100": "1.7.1",
        "chartjs-plugin-trendline": "^3.2.0",
        "chartjs-plugin-zoom": "^2.2.0",
        "chokidar": "^3.5.3",
        "classnames": "^2.5.1",
        "clsx": "^2.1.1",
        "country-flag-emoji-polyfill": "^0.1.8",
        "cron-parser": "^5.5.0",
        "cronstrue": "^3.14.0",
        "crypto-browserify": "^3.12.0",
        "cva": "1.0.0-beta.3",
        "d3": "^7.9.0",
        "d3-array": "^3.2.4",
        "d3-flame-graph": "^5.0.0",
        "dayjs": "1.11.11",
        "dompurify": "^3.2.6",
        "elkjs": "^0.10.0",
        "emoji-regex": "^10.4.0",
        "eventsource-parser": "^3.0.0",
        "fast-deep-equal": "catalog:",
        "fastpriorityqueue": "^0.7.5",
        "fflate": "^0.7.4",
        "frimousse": "^0.3.0",
        "fuse.js": "catalog:",
        "hast-util-to-html": "^9.0.5",
        "he": "^1.2.0",
        "heatmap.js": "^2.0.5",
        "highlight.js": "~11.11.0",
        "hls.js": "^1.5.15",
        "html-to-image": "^1.11.13",
        "husky": "catalog:",
        "image-blob-reduce": "^4.1.0",
        "kea": "catalog:",
        "kea-forms": "catalog:",
        "kea-loaders": "catalog:",
        "kea-localstorage": "catalog:",
        "kea-router": "catalog:",
        "kea-subscriptions": "catalog:",
        "kea-test-utils": "catalog:",
        "kea-waitfor": "catalog:",
        "kea-window-values": "catalog:",
        "liquidjs": "^10.25.2",
        "lodash.debounce": "^4.0.8",
        "lodash.difference": "^4.5.0",
        "lodash.isequal": "^4.5.0",
        "lodash.merge": "^4.6.2",
        "lodash.sortby": "^4.7.0",
        "lodash.throttle": "^4.1.1",
        "lodash.uniqby": "^4.7.0",
        "lowlight": "^3.3.0",
        "maplibre-gl": "^3.5.1",
        "marked": "^17.0.4",
        "mathjax-full": "3.2.2",
        "md5": "^2.3.0",
        "mdast-util-find-and-replace": "^3.0.2",
        "monaco-editor": "^0.55.1",
        "monaco-vim": "^0.4.4",
        "motion": "^12.26.1",
        "natural-orderby": "^3.0.2",
        "oxfmt": "catalog:",
        "papaparse": "^5.4.1",
        "pmtiles": "^2.11.0",
        "posthog-js": "catalog:",
        "protomaps-themes-base": "2.0.0-alpha.1",
        "query-selector-shadow-dom": "^1.0.0",
        "re2js": "^0.4.1",
        "react": "^18.3.1",
        "react-data-grid": "7.0.0-beta.47",
        "react-dom": "^18.3.1",
        "react-draggable": "^4.5.0",
        "react-email-editor": "^1.7.11",
        "react-grid-layout": "^2.2.2",
        "react-intersection-observer": "^9.5.3",
        "react-markdown": "^9.0.0",
        "react-modal": "^3.15.1",
        "react-resizable": "^3.0.5",
        "react-shadow": "^20.3.0",
        "react-simple-maps": "^3.0.0",
        "react-textarea-autosize": "^8.3.3",
        "react-toastify": "^10.0.0",
        "react-transition-group": "^4.4.5",
        "react-virtualized-auto-sizer": "^2.0.2",
        "react-window": "^2.2.5",
        "remark-gfm": "^4.0.0",
        "resize-observer-polyfill": "^1.5.1",
        "rrule": "^2.8.1",
        "sass": "^1.26.2",
        "simple-statistics": "^7.8.8",
        "snappy-wasm": "^0.3.0",
        "tailwind-merge": "^2.2.2",
        "tailwindcss": "4.0.7",
        "torph": "^0.0.5",
        "ts-pattern": "catalog:",
        "typescript": "catalog:",
        "use-debounce": "catalog:",
        "use-resize-observer": "^8.0.0",
        "vite": "^7.1.9",
        "zxcvbn": "^4.4.2"
    },
    "devDependencies": {
        "@babel/parser": "^7.24.0",
        "@babel/traverse": "^7.24.0",
        "@parcel/packager-ts": "catalog:",
        "@parcel/transformer-typescript-types": "catalog:",
        "@posthog/openapi-codegen": "workspace:*",
        "@storybook/addon-actions": "catalog:",
        "@storybook/react": "catalog:",
        "@storybook/testing-library": "catalog:",
        "@storybook/types": "catalog:",
        "@sucrase/jest-plugin": "^3.0.0",
        "@testing-library/dom": ">=9.3.4",
        "@testing-library/jest-dom": "^5.17.0",
        "@testing-library/react": "^14.3.1",
        "@testing-library/user-event": "^14.6.1",
        "@types/bintrees": "^1.0.6",
        "@types/chartjs-plugin-crosshair": "^1.1.1",
        "@types/chartjs-plugin-trendline": "^1.0.4",
        "@types/clone": "^2.1.1",
        "@types/d3": "^7.4.3",
        "@types/dompurify": "^3.0.3",
        "@types/he": "^1.2.3",
        "@types/heatmap.js": "^2.0.41",
        "@types/image-blob-reduce": "^4.1.1",
        "@types/jest": "catalog:",
        "@types/jest-image-snapshot": "^6.1.0",
        "@types/lodash.debounce": "^4.0.9",
        "@types/lodash.difference": "^4.5.9",
        "@types/lodash.isequal": "^4.5.8",
        "@types/lodash.merge": "^4.6.9",
        "@types/lodash.sortby": "^4.7.9",
        "@types/lodash.throttle": "^4.1.1",
        "@types/lodash.uniqby": "^4.7.9",
        "@types/md5": "^2.3.0",
        "@types/node": "catalog:",
        "@types/papaparse": "^5.3.8",
        "@types/query-selector-shadow-dom": "^1.0.0",
        "@types/react": "catalog:",
        "@types/react-dom": "catalog:",
        "@types/react-modal": "^3.13.1",
        "@types/react-resizable": "^3.0.4",
        "@types/react-simple-maps": "^3.0.6",
        "@types/react-transition-group": "^4.4.5",
        "@types/testing-library__jest-dom": "^5.14.5",
        "@types/zxcvbn": "^4.4.0",
        "caniuse-lite": "^1.0.30001689",
        "concurrently": "catalog:",
        "esbuild-visualizer": "^0.6.0",
        "fake-indexeddb": "^6.0.1",
        "fs-extra": "^10.0.0",
        "history": "^5.0.1",
        "jest": "catalog:",
        "jest-canvas-mock": "^2.4.0",
        "jest-envir
... [TRUNCATED]
```

### File: nodejs\package.json
```json
{
    "name": "@posthog/nodejs",
    "version": "1.10.5",
    "description": "PostHog Node.js services",
    "license": "MIT",
    "author": "PostHog <hey@posthog.com>",
    "repository": "https://github.com/PostHog/posthog",
    "main": "dist/index.js",
    "types": "dist/index.d.ts",
    "scripts": {
        "test": "SHARD_IDX=${SHARD_INDEX:-1}; SHARD_TOTAL=${SHARD_COUNT:-1}; echo $SHARD_IDX/$SHARD_TOTAL; jest --runInBand --forceExit --shard=$SHARD_IDX/$SHARD_TOTAL --testPathIgnorePatterns='postgres-parity'",
        "test:postgres-parity": "jest --runInBand --forceExit --testPathPatterns='postgres-parity'",
        "start": "pnpm start:dev",
        "start:dist": "node dist/index.js",
        "start:dev": "NODE_ENV=dev tsx watch src/index.ts",
        "start:devNoWatch": "NODE_ENV=dev tsx src/index.ts",
        "prestart:dev": "pnpm build:cyclotron:dev",
        "prestart:devNoWatch": "pnpm build:cyclotron:dev",
        "build": "pnpm clean && pnpm typescript:compile && pnpm typescript:compile-cleanup",
        "clean": "rm -rf dist/*",
        "typescript:compile": "tsc -b && tsc-alias",
        "typescript:compile-cleanup": "[ -d dist/src ] && mv dist/src/* dist/ || true",
        "typescript:check": "tsc --noEmit -p .",
        "lint": "eslint .",
        "lint:fix": "eslint --fix .",
        "format": "prettier --write .",
        "format:check": "prettier --check .",
        "prepublishOnly": "pnpm build",
        "setup:dev:clickhouse": "cd .. && DEBUG=1 python manage.py migrate_clickhouse",
        "setup:test": "cd .. && TEST=1 python manage.py setup_test_environment && cd nodejs && pnpm run setup:test:rust",
        "setup:test:rust": "CYCLOTRON_DATABASE_NAME=test_cyclotron CYCLOTRON_NODE_DATABASE_NAME=test_cyclotron_node PERSONS_DATABASE_NAME=test_persons BEHAVIORAL_COHORTS_DATABASE_NAME=test_behavioral_cohorts ../rust/bin/migrate-entry all --fresh",
        "setup:test:persons-parity": "PERSONS_DATABASE_NAME=test_persons_parity ../rust/bin/migrate-entry persons --fresh",
        "migrate:persons": "../rust/bin/migrate-persons",
        "migrate:cyclotron": "../rust/bin/migrate-cyclotron",
        "migrate:cyclotron-node": "../rust/bin/migrate-cyclotron-node",
        "migrate:behavioral-cohorts": "../rust/bin/migrate-behavioral-cohorts",
        "migrate:rust": "../rust/bin/migrate-entry all",
        "services:start": "cd .. && docker compose -f docker-compose.dev.yml up",
        "services:stop": "cd .. && docker compose -f docker-compose.dev.yml down",
        "services:clean": "cd .. && docker compose -f docker-compose.dev.yml rm -v",
        "services": "pnpm services:stop && pnpm services:clean && pnpm services:start",
        "build:cyclotron": "pnpm --filter=@posthog/cyclotron package",
        "build:cyclotron:dev": "pnpm --filter=@posthog/cyclotron run build:dev",
        "generate:personhog-proto": "cd ../proto && buf generate --template ../nodejs/buf.gen.yaml --path personhog/service --path personhog/types .",
        "update-ai-costs": "ts-node src/ingestion/ai/costs/scripts/update-ai-costs.ts",
        "sync-segment-icons": "DATABASE_URL=something ts-node src/cdp/segment/sync-segment-icons.ts",
        "start:recording-rasterizer": "node dist/session-replay/recording-rasterizer/index.js"
    },
    "dependencies": {
        "@amplitude/ua-parser-js": "^0.7.33",
        "@aws-sdk/client-dynamodb": "^3.952.0",
        "@aws-sdk/client-kms": "^3.952.0",
        "@aws-sdk/client-s3": "^3.723.0",
        "@aws-sdk/client-sesv2": "^3.980.0",
        "@aws-sdk/client-sts": "^3.975.0",
        "@aws-sdk/lib-storage": "^3.723.0",
        "@babel/core": "^7.22.10",
        "@babel/plugin-transform-react-jsx": "^7.22.5",
        "@babel/preset-env": "^7.22.10",
        "@babel/preset-typescript": "^7.18.6",
        "@babel/standalone": "^7.23.2",
        "@bufbuild/protobuf": "^2.11.0",
        "@clickhouse/client": "^1.12.0",
        "@connectrpc/connect": "^2.1.1",
        "@connectrpc/connect-node": "^2.1.1",
        "@google-cloud/pubsub": "4.11.0",
        "@google-cloud/storage": "^5.8.5",
        "@maxmind/geoip2-node": "^3.4.0",
        "@mongodb-js/zstd": "^1.2.0",
        "@opentelemetry/api": "^1.9.0",
        "@opentelemetry/auto-instrumentations-node": "^0.62.1",
        "@opentelemetry/exporter-trace-otlp-grpc": "^0.203.0",
        "@opentelemetry/exporter-trace-otlp-http": "^0.203.0",
        "@opentelemetry/instrumentation-pg": "^0.56.0",
        "@opentelemetry/resources": "^2.0.1",
        "@opentelemetry/sdk-node": "^0.203.0",
        "@opentelemetry/sdk-trace-node": "^2.0.1",
        "@opentelemetry/semantic-conventions": "^1.36.0",
        "@posthog/cyclotron": "workspace:*",
        "@posthog/hogvm": "workspace:*",
        "@posthog/replay-headless": "workspace:*",
        "@posthog/siphash": "1.1.1",
        "@pyroscope/nodejs": "^0.4.8",
        "@segment/action-destinations": "^3.383.0",
        "@temporalio/activity": "1.15.0",
        "@temporalio/client": "^1.12.0",
        "@temporalio/common": "1.15.0",
        "@temporalio/proto": "1.15.0",
        "@temporalio/worker": "^1.12.0",
        "@types/node": "catalog:",
        "@types/tail": "^2.2.1",
        "avsc": "^5.7.9",
        "aws-sdk": "^2.927.0",
        "cors": "^2.8.5",
        "detect-browser": "^5.3.0",
        "escape-string-regexp": "^4.0.0",
        "fast-deep-equal": "catalog:",
        "fastpriorityqueue": "^0.7.5",
        "fernet-nodejs": "^1.0.6",
        "generic-pool": "^3.7.1",
        "husky": "catalog:",
        "ioredis": "^4.27.6",
        "ipaddr.js": "^2.1.0",
        "js-big-decimal": "^2.2.0",
        "jsonwebtoken": "^9.0.2",
        "libsodium-wrappers": "^0.7.15",
        "liquidjs": "^10.25.2",
        "lodash": "^4.17.21",
        "lru-cache": "^11.0.0",
        "luxon": "^3.4.4",
        "node-fetch": "^2.6.1",
        "node-rdkafka": "^3.6.1",
        "node-schedule": "^2.1.0",
        "nodemailer": "^7.0.5",
        "p-limit": "3.1.0",
        "pg": "^8.6.0",
        "pino": "^8.6.0",
        "posthog-node": "5.25.0",
        "pretty-bytes": "^5.6.0",
        "prom-client": "^14.2.0",
        "puppeteer": "^24.3.0",
        "puppeteer-capture": "^1.43.0",
        "re2": "^1.22.1",
        "snappy": "^7.2.2",
        "tail": "^2.2.6",
        "tldts": "^6.1.57",
        "typescript": "catalog:",
        "ultimate-express": "^2.0.9",
        "undici": "^7.8.0",
        "undici-types": "^7.3.0",
        "uuid": "^10.0.0",
        "xml-js": "^1.6.11",
        "zod": "^3.24.1"
    },
    "devDependencies": {
        "@babel/cli": "^7.22.5",
        "@babel/types": "^7.20.2",
        "@bufbuild/protoc-gen-es": "^2.11.0",
        "@segment/actions-core": "^3.151.0",
        "@trivago/prettier-plugin-sort-imports": "^5.2.2",
        "@types/adm-zip": "^0.4.34",
        "@types/babel__core": "^7.1.19",
        "@types/babel__standalone": "^7.1.4",
        "@types/chance": "^1.1.7",
        "@types/cors": "^2.8.19",
        "@types/faker": "^5.5.7",
        "@types/generic-pool": "^3.1.9",
        "@types/ioredis": "^4.26.4",
        "@types/jest": "^30.0.0",
        "@types/jsonwebtoken": "^9.0.10",
        "@types/libsodium-wrappers": "^0.7.14",
        "@types/lodash": "^4.17.16",
        "@types/long": "4.x.x",
        "@types/luxon": "^3.4.2",
        "@types/node-fetch": "^2.5.10",
        "@types/node-schedule": "^2.1.0",
        "@types/nodemailer": "^6.4.17",
        "@types/pg": "^8.6.0",
        "@types/redlock": "^4.0.1",
        "@types/snowflake-sdk": "^1.5.1",
        "@types/supertest": "^6.0.2",
        "@types/uuid": "^10.0.0",
        "@typescript-eslint/eslint-plugin": "^7.1.1",
        "@typescript-eslint/parser": "^7.1.1",
        "babel-eslint": "^10.1.0",
        "chance": "^1.1.13",
        "eslint": "^8.53.0",
        "eslint-config-prettier": "^9.1.0",
        "eslint-plugin-eslint-comments": "^3.2.0",
        "eslint-plugin-import": "^2.29.0",
        "eslint-plugin-no-only-tests": "^3.1.0",
        "eslint-plugin-node": "^11.1.0",
        "eslint-plugin-promise": "^6.1.1",
        "jest": "^30.0.0",
        "jest-environment-node": "^30.0.0",
        "pino-pretty": "^9.1.0",
        "prettier": "^3.6.2",
        "supertest": "^7.0.0",
        "ts-jest": "^29.1.0",
        "ts-node": "^10.9.1",
        "tsc-alias": "^1.8.16",
        "tsconfig-paths": "^4.2.0",
        "tsx": "^4.7.0"
    },
    "engines": {
        "node": ">=24 <25"
    },
    "cyclotron": {
        "//This is a short term workaround to ensure that cyclotron changes trigger a rebuild": true,
        "version": "0.1.12"
    }
}

```

### File: playwright\package.json
```json
{
    "name": "@posthog/playwright",
    "scripts": {
        "build:products": "pnpm --filter=@posthog/frontend build:products",
        "test": "pnpm build:products && playwright test"
    },
    "dependencies": {
        "@playwright/test": "1.45.0",
        "@posthog/frontend": "workspace:*"
    },
    "peerDependencies": {}
}

```

### File: playwright\README.md
```md
# End-to-End Testing

## Running tests

Spin up a full local E2E environment (backend, frontend, docker services, Playwright UI):

```bash
./bin/e2e-test-runner
```

This uses `bin/phrocs-e2e.yaml` under the hood. If you need to reset the E2E database, trigger the `reset-db` process in the phrocs UI.

To run tests against an already-running PostHog instance:

```bash
LOGIN_USERNAME='my@email.address' LOGIN_PASSWORD="the-password" BASE_URL='http://localhost:8010' pnpm --filter=@posthog/playwright exec playwright test --ui
```

You might need to install Playwright first: `pnpm --filter=@posthog/playwright exec playwright install`

## Writing tests with Claude Code

Use the `/playwright-test` skill to have Claude Code write and validate end-to-end tests for you.
It will explore the UI with Playwright MCP tools, plan the tests, implement them, and run them in a loop until they pass reliably (including a flakiness check with `--repeat-each 10`).

## Writing tests

### Best practices

- Don't use CSS selectors — prefer accessibility roles (`getByRole`) or `getByTestId()` which maps to `data-attr` in our config. Add `data-attr` to components if needed.
- Write fewer, longer tests that do multiple things. Split logical steps with `test.step()`.
- Use page object models for common tasks and accessing common elements (see `page-models/`).
- After UI interactions, assert on UI changes — don't assert on network requests resolving.
- Never put conditional logic (`if`) in a test.

### Gotchas

**Flaky tests are almost always due to not waiting for the right thing.**
Consider adding a better selector, an intermediate step like waiting for URL or page title to change,
or waiting for a critical network request to complete.

**Loose selectors cause strict mode violations.**
If a selector matches multiple elements, Playwright will show all matches — use the output to narrow down:

```text
Error: locator.click: Error: strict mode violation: locator('text=Set a billing limit') resolved to 2 elements:
1) <span class="LemonButton__content">Set a billing limit</span> aka getByTestId('billing-limit-input-wrapper-product_analytics').getByRole('button', { name: 'Set a billing limit' })
2) <span class="LemonButton__content">Set a billing limit</span> aka getByTestId('billing-limit-input-wrapper-session_replay').getByRole('button', { name: 'Set a billing limit' })
```

```

### File: proto\README.md
```md
# Proto Definitions

Language-agnostic protobuf definitions for PostHog services.

## Structure

```text
proto/
├── buf.yaml
├── kafka_assigner/       # Kafka partition assignment
└── personhog/            # Person data service
    ├── types/v1/
    ├── replica/v1/
    └── service/v1/
```

## Consumers

| Proto             | Rust                                         | Python                                                   |
| ----------------- | -------------------------------------------- | -------------------------------------------------------- |
| `personhog/`      | `rust/personhog-proto` (auto via tonic)      | `posthog/personhog_client/proto/generated/` (checked in) |
| `kafka_assigner/` | `rust/kafka-assigner-proto` (auto via tonic) | —                                                        |

## Updating protos

1. Edit `.proto` files in the relevant directory
2. Regenerate language bindings for affected consumers (see table above)
3. Commit generated files — CI rejects stale stubs

### Python stubs (personhog only)

```bash
bin/generate_personhog_proto.sh
```

Only needed when `personhog/` protos change. Requires `grpcio-tools` and `protoletariat` (`uv sync`).

If you added or removed **message types**, update the re-exports in `posthog/personhog_client/proto/__init__.py`.
If you added or removed **RPCs**, update the wrapper methods in `posthog/personhog_client/client.py`.

### Rust

No action needed — Rust bindings regenerate on `cargo build`.

## CI

`.github/workflows/ci-proto.yml` runs on proto changes:

- `buf lint` — style and naming
- `buf breaking` — backwards compatibility against `master`
- Python codegen staleness check

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.

---
id: diginext
type: knowledge
owner: OA_Triage
---
# diginext
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
	"name": "@topgroup/diginext",
	"version": "3.43.5",
	"description": "A BUILD SERVER & CLI to deploy apps to any Kubernetes clusters.",
	"exports": "./index.js",
	"bin": {
		"di": "./dist/index.js",
		"dx": "./dist/index.js"
	},
	"files": [
		"dist/**",
		"CHANGELOG.md",
		"di-banner.png",
		"public/**",
		"templates/**"
	],
	"keywords": [
		"topgroup",
		"dx",
		"digitop",
		"dig-cli",
		"deploy k8s",
		"diginext-cli",
		"diginext",
		"di",
		"di-cli",
		"build-server",
		"cli-deploy",
		"k8s",
		"kubernetes",
		"kubectl",
		"build container",
		"build docker",
		"deploy docker",
		"run k8s"
	],
	"repository": {
		"type": "git",
		"url": "https://github.com/digitopvn/diginext.git"
	},
	"bugs": {
		"url": "https://github.com/digitopvn/diginext/issues"
	},
	"homepage": "https://github.com/digitopvn/diginext",
	"author": {
		"name": "TOP GROUP (a.k.a Digitop)",
		"email": "dev@wearetopgroup.com",
		"url": "https://github.com/digitopvn/diginext"
	},
	"license": "GPL-3.0",
	"engines": {
		"npm": ">=8.0.0",
		"node": ">=16.0.0"
	},
	"scripts": {
		"build": "rimraf dist && tsc -p tsconfig.json && tsc-alias -p tsconfig.json && npm run restruct && rimraf dist/__tests__ && chmod -R +x dist && npm link && pnpm swagger",
		"build:deploy": "git merge origin/main && pnpm build && skaffold run --platform=linux/amd64,linux/arm64",
		"build:run": "pnpm build && skaffold run --platform=linux/amd64,linux/arm64",
		"build:deploy-release": "pnpm build && skaffold run --platform=linux/amd64,linux/arm64 && pnpm release:nobuild",
		"deploy": "skaffold run --tail",
		"startup": "pm2 startup",
		"unstartup": "pm2 unstartup",
		"serve": "CLI_MODE=server pm2 start dist/server.js --name diginext-build-server && pm2 save",
		"stop": "pm2 stop diginext-build-server",
		"restruct": "ncp dist/src dist && rimraf dist/src dist/package.json",
		"dx": "CLI_MODE=client ts-node src/index.ts",
		"dev": "pnpm dev:server",
		"dev:server": "run-script-os",
		"dev:server:win32": "set CLI_MODE=server && rimraf dist && concurrently \"tsup src/**/*.ts src/**/*.tsx --format esm,cjs --legacy-output --watch\"",
		"dev:server:darwin:linux": "CLI_MODE=server ts-node-dev --poll -r tsconfig-paths/register src/server.ts --debug --respawn --exit-child --watch src",
		"dev:server:default": "CLI_MODE=server ts-node-dev --poll -r tsconfig-paths/register src/server.ts --debug --respawn --exit-child --watch src",
		"dev:nodemon": "CLI_MODE=server nodemon --legacy-watch \"src/**/*.ts\" --ext \"ts,json\" --exec \"pnpm swagger && CLI_MODE=server ts-node -r tsconfig-paths/register src/server.ts\"",
		"dev:swagger": "concurrently \"pnpm dev:spec\" \"pnpm dev:server\"",
		"dev:spec": "ts-node-dev --respawn --transpile-only -- node_modules/tsoa/dist/cli.js spec",
		"start:ts": "NODE_ENV=production CLI_MODE=server ts-node -r tsconfig-paths/register src/server.ts",
		"start:js": "NODE_ENV=production CLI_MODE=server node dist/server.js",
		"check-types": "tsc --noEmit --pretty -p tsconfig.json",
		"lint": "eslint \"src/**/*.ts\" --fix && pnpm check-types",
		"clean": "rimraf .yarn/cache node_modules yarn.lock pnpm-lock.yaml dist",
		"test": "run-script-os",
		"test:win32": "set CLI_MODE=server && set NODE_ENV=test && jest --runInBand --detectOpenHandles --watchAll=false --forceExit",
		"test:darwin:linux": "CLI_MODE=server NODE_ENV=test jest --runInBand --detectOpenHandles --watchAll=false --forceExit",
		"test:default": "CLI_MODE=server NODE_ENV=test jest --runInBand --detectOpenHandles --watchAll=false --forceExit",
		"test:build": "pnpm build && CLI_MODE=server NODE_ENV=test jest --runInBand --detectOpenHandles --watchAll=false --forceExit",
		"coverage": "pnpm lint && pnpm build && jest --coverage",
		"format": "prettier 'src/**/*.{js,ts,tsx,json,yaml}' --write && pnpm lint",
		"commit": "git add . && cz && git merge origin/prerelease -m \"chore(PR): Merged from origin/prerelease\" --no-ff && git merge origin/main -m \"chore(PR): Merged from origin/main\" --no-ff && git push origin && exit 0",
		"commit-build": "git add . && git commit --allow-empty -m 'chore(changelog.md): generate changelog [skip ci]' && git push -u origin || true",
		"commit-pkgver": "git add . && git commit --allow-empty -m 'chore(package.json): update version [skip ci]' && git push -u origin || true",
		"pkg-version": "npm pkg set version=$(echo $(git describe --tags $(git rev-list --tags --max-count=1)) | cut -c2-)",
		"npm-publish": "npm publish --access=public",
		"release": "npm run release:nobuild",
		"release:build": "npm run format && npm run build && npm run release:nobuild",
		"release:nobuild": "npm run prerelease && npm run npm-publish",
		"release:deploy": "npm run release && skaffold run --platform=linux/amd64,linux/arm64",
		"release:docker": "npm run release && npm run docker-build",
		"release:all": "npm run release && npm run docker-build && skaffold run --tail",
		"prerelease": "npx semantic-release --no-ci",
		"ci:release": "open-cli https://github.com/digitopvn/diginext/compare/main...$(echo $(git rev-parse --abbrev-ref HEAD))",
		"ci:prerelease": "open-cli https://github.com/digitopvn/diginext/compare/prerelease...$(echo $(git rev-parse --abbrev-ref HEAD))",
		"pull-request": "open-cli https://github.com/digitopvn/diginext/compare/main...$(echo $(git rev-parse --abbrev-ref HEAD))",
		"pr": "pnpm pull-request",
		"husky-hide": "npm pkg delete scripts.prepare && npm pkg delete scripts.postinstall",
		"husky-show": "npm pkg set scripts.prepare='husky install' && npm pkg set scripts.postinstall='husky install'",
		"docker-driver": "docker buildx create --driver docker-container --name diginext-cli-builder",
		"podman-build-beta": "podman build -f Dockerfile -t digitop/diginext:beta --cache-from digitop/diginext .",
		"docker-build-beta": "docker buildx build --platform=linux/amd64,linux/arm64 -f Dockerfile --push -t digitop/diginext:$(echo $(git describe --tags $(git rev-list --tags --max-count=1)) | cut -c2-) -t digitop/diginext:beta --cache-from type=registry,ref=digitop/diginext .",
		"docker-build-beta-amd": "docker buildx build -o docker-cache --platform=linux/amd64 -f Dockerfile -t digitop/diginext:beta --builder=diginext-cli-beta-builder --cache-from type=local,ref=docker-cache .",
		"docker-build-beta-arm": "docker buildx build --platform=linux/amd64 -f Dockerfile --push -t digitop/diginext:beta --builder=diginext-cli-beta-builder --cache-from type=registry,ref=digitop/diginext:beta .",
		"docker-build": "docker buildx build --platform=linux/amd64,linux/arm64 -f Dockerfile --push -t digitop/diginext:$(echo $(git describe --tags $(git rev-list --tags --max-count=1)) | cut -c2-) -t digitop/diginext:latest --cache-from type=registry,ref=digitop/diginext .",
		"docker-build-arm": "docker buildx build -f Dockerfile --load -t digitop/diginext:latest --builder=diginext-cli-builder --cache-from type=registry,ref=digitop/diginext:latest .",
		"docker-release": "pnpm build && pnpm docker-build",
		"swagger": "tsoa spec",
		"prepare": "husky install || true",
		"postinstall": "husky install || true"
	},
	"config": {
		"commitizen": {
			"path": "@commitlint/cz-commitlint"
		}
	},
	"release": {
		"branches": [
			"main",
			{
				"name": "prerelease",
				"prerelease": true
			},
			{
				"name": "beta",
				"prerelease": true
			}
		],
		"plugins": [
			[
				"@semantic-release/commit-analyzer",
				{
					"preset": "angular",
					"releaseRules": [
						{
							"type": "docs",
							"scope": "README",
							"release": "patch"
						},
						{
							"type": "refactor",
							"release": "minor"
						},
						{
							"type": "style",
							"release": "patch"
						}
					],
					"parserOpts": {
						"noteKeywords": [
							"BREAKING CHANGE",
							"BREAKING CHANGES"
						]
					}
				}
			],
			"@semantic-release/release-notes-generator",
			"@semantic-release/changelog",
			"@semantic-release/git",
			[
				"@semantic-release/github",
				{
					"successComment": false,
					"failTitle": false
				}
			],
			"@semantic-release/npm"
		]
	},
	"dependencies": {
		"@aws-sdk/client-s3": "^3.188.0",
		"@aws-sdk/lib-storage": "^3.675.0",
		"@aws-sdk/types": "^3.188.0",
		"@babel/runtime": "^7.15.4",
		"@google-analytics/admin": "^1.2.3",
		"@google-cloud/storage": "^5.5.0",
		"@kubernetes/client-node": "^0.20.0",
		"@socket.io/redis-adapter": "^8.3.0",
		"@supercharge/strings": "^1.16.0",
		"@tsoa/runtime": "^5.0.0",
		"@types/jest": "^26.0.22",
		"agentkeepalive": "^4.2.1",
		"app-root-path": "^3.1.0",
		"axios": "1.4.0",
		"bcrypt": "^5.1.0",
		"bitbucket": "^2.7.0",
		"body-parser": "^1.20.1",
		"chalk": "4.1.2",
		"class-validator": "^0.13.2",
		"cli-highlight": "^2.1.11",
		"cli-html": "^3.0.6",
		"cli-markdown": "^3.0.2",
		"cli-progress": "^3.8.2",
		"cli-table": "^0.3.11",
		"clui": "^0.3.6",
		"compare-versions": "^5.0.1",
		"configstore": "^5.0.1",
		"cookie-parser": "^1.4.6",
		"cookie-session": "^2.0.0",
		"cors": "^2.8.5",
		"cron": "^2.1.0",
		"date-fns": "^2.29.3",
		"dayjs": "^1.10.4",
		"debug": "^4.3.4",
		"diginext-utils": "3.0.6",
		"dotenv": "^8.2.0",
		"envfile": "6.14.0",
		"esm": "^3.2.18",
		"execa": "npm:@esm2cjs/execa@6.1.1-cjs.1",
		"express": "^4.17.1",
		"express-list-endpoints": "^6.0.0",
		"express-query-parser": "^1.3.3",
		"express-session": "^1.17.3",
		"extract-zip": "^2.0.0",
		"form-data": "^4.0.0",
		"generate-password": "^1.7.0",
		"gitignore": "^0.6.0",
		"glob": "^8.1.0",
		"globby": "11.1.0",
		"google-auth-library": "^9.7.0",
		"humanize-duration": "^3.25.1",
		"husky": "^8.0.0",
		"image-size": "^1.0.2",
		"inquirer": "8.2.5",
		"install": "0.13.0",
		"ioredis": "^5.4.1",
		"jest": "^29.5.0",
		"js-yaml": "^4.1.0",
		"json-diff": "^0.5.4",
		"jsonwebtoken": "8.5.1",
		"listr": "^0.14.3",
		"lodash": "^4.17.21",
		"marked": "^4.2.3",
		"marked-terminal": "^5.1.1",
		"mkdirp": "^2.1.3",
		"module-alias": "2.2.2",
		"mongodb": "^4.17.2",
		"mongoose": "^7.0.3",
		"morgan": "^1.10.0",
		"ncp": "^2.0.0",
		"node-cron": "3.0.0",
		"node-emoji": "^1.11.0",
		"node-fetch": "^2.6.0",
		"open": "8.4.0",
		"ora": "^5.1.0",
		"p-queue": "6.6.2",
		"passport": "^0.6.0",
		"passport-google-oauth2": "^0.2.0",
		"passport-http-bearer": "^1.0.1",
		"passport-jwt": "4.0.0",
		"pkg-install": "^0.2.0",
		"pm2": "^5.3.0",
		"puppeteer": "^22.15.0",
		"rate-limiter-flexible": "^2.4.1",
		"recursive-copy": "^2.0.14",
		"redis": "^4.3.1",
		"reflect-metadata": "^0.1.13",
		"remove-markdown": "^0.5.0",
		"sha.js": "^2.4.11",
		"simple-git": "^3.15.0",
		"socket.io": "4.1.3",
		"socket.io-client": "4.1.3",
		"spdx-license-list": "^5.0.0",
		"strip-ansi": "^6.0.1",
		"swagger-ui-express": "^4.6.1",
		"tree-node-cli": "^1.6.0",
		"tslib": "^2.5.0",
		"tsoa": "^5.1.1",
		"tsup": "^7.2.0",
		"uuid": "^9.0.0",
		"xml2js": "^0.4.23",
		"yargs": "^17.6.2",
		"zod": "^3.23.8"
	},
	"devDependencies": {
		"@babel/cli": "^7.19.3",
		"@babel/core": "^7.20.2",
		"@babel/plugin-transform-runtime": "^7.15.8",
		"@babel/preset-env": "^7.23.3",
		"@babel/register": "^7.18.9",
		"@commitlint/cli": "^17.3.0",
		"@commitlint/config-conventional": "^17.3.0",
		"@commitlint/cz-commitlint": "^17.3.0",
		"@jest/globals": "^29.5.0",
		"@jest/types": "^29.5.0",
		"@semantic-release/changelog": "^6.0.2",
		"@semantic-release/commit-analyzer": "^9.0.2",
		"@semantic-release/git": "^10.0.1",
		"@semantic-release/npm": "^9.0.1",
		"@semantic-release/release-notes-generator": "^10.0.3",
		"@types/bcrypt": "^5.0.0",
		"@types/cli-table": "^0.3.1",
		"@types/cookie-session": "^2.0.44",
		"@types/cors": "^2.8.14",
		"@types/express": "^4.17.17",
		"@types/express-list-endpoints": "^6.0.0",
		"@types/express-serve-static-core": "^4.17.33",
		"@types/inquirer": "^9.0.3",
		"@types/jsonwebtoken": "8.5.1",
		"@types/lodash": "^4.14.191",
		"@types/marked": "^4.0.7",
		"@types/mocha": "^10.0.0",
		"@types/morgan": "^1.9.4",
		"@types/node": "^18.8.5",
		"@types/node-cron": "^3.0.7",
		"@types/qs": "^6.9.7",
		"@types/supertest": "^2.0.12",
		"@types/swagger-ui-express": "^4.1.3",
		"@types/yargs": "^17.0.22",
		"@typescript-eslint/eslint-plugin": "^5.45.0",
		"@typescript-eslint/parser": "^5.45.0",
		"babel-core": "^6.26.3",
		"babel-jest": "^29.5.0",
		"babel-loader": "^9.1.3",
		"babel-plugin-module-resolver": "^4.1.0",
		"babel-polyfill": "^6.26.0",
		"chai": "^4.3.7",
		"commitizen": "^4.2.5",
		"concurrently": "^7.6.0",
		"del": "6.1.1",
		"del-cli": "^5.0.0",
		"dependency-cruiser": "^13.1.1",
		"esbuild": "^0.15.15",
		"eslint": "^8.28.0",
		"eslint-config-airbnb-base": "^15.0.0",
		"eslint-config-airbnb-typescript": "^17.0.0",
		"eslint-config-prettier": "^8.5.0",
		"eslint-plugin-import": "^2.29.0",
		"eslint-plugin-prettier": "^5.0.0",
		"eslint-plugin-simple-import-sort": "^8.0.0",
		"eslint-plugin-unused-imports": "^2.0.0",
		"lint-staged": "^13.0.4",
		"mocha": "^10.1.0",
		"nodemon": "^2.0.20",
		"npm-run-all": "^4.1.5",
		"open-cli": "^7.1.0",
		"prettier": "^3.0.0",
		"rimraf": "^6.0.1",
		"run-script-os": "^1.1.6",
		"semantic-release": "^19.0.5",
		"supertest": "^6.3.3",
		"trash-cli": "^5.0.0",
		"ts-jest": "^29.1.1",
		"ts-mocha": "^10.0.0",
		"ts-node": "^10.9.1",
		"ts-node-dev": "^2.0.0",
		"tsc-alias": "^1.7.1",
		"tsconfig-paths": "4.1.0",
		"typescript": "^4.9.5"
	}
}

```

### File: readme.md
```md
# DXUP

### **A developer-focused platform for app deployment & centralized cloud resource management.**

https://dxup.dev

***Developers should not be frustrated by deploying apps to the infrastructure, or bothering the DevOps engineers to help deploying it, they should fully focus on developing apps, they don't need to understand the servers, the domains, or infrastructure related stuffs.***

> *Focus on building your apps, shipping fast, and shinning, and leave your cloud infrastructure to DXUP.*

> `dx` also means **Developer Experience**, and this is my number one goal - create the best experience for developers - let's make coding great again.

<p align="center">
  <img src="dx-banner.png?raw=true" alt="DXUP Build Server & CLI">
</p>

## Features

- **Overcoming Kubernetes complexity by stripping Kubernetes away**
- One-click deploy to any Kubernetes clusters of any cloud providers
    - ✅ GCP
    - ✅ DigitalOcean
    - ✅ Bare Metal K8S cluster
    - 🔜 AWS
    - 🔜 Azure
- Simple deploy of any public or private Docker image
- Application rollback to previously deployed versions
- Start developing new applications with frameworks or boilerplates
- Manage, auto-backup & restore databases:
    - ✅ Postgres
    - ✅ MySQL
    - ✅ MongoDB
- Manage & upload files to:
    - ✅ Google Storage
    - ✅ AWS S3 Block Storage
    - ✅ Digital Ocean Space
- Zero-downtime deploy and health checks
- Cronjobs for automation tasks
- Monitor CPU, RAM, and Network usage per deployment, per node & per cluster
- Marketplace for one click add-ons (e.g. MongoDB, Redis, PostgreSQL)

## Demo Video

[![Watch the video](https://raw.githubusercontent.com/digitopvn/diginext/main/demo.png)](https://www.youtube.com/watch?v=Q2jJ555Mc2k)

## Benefits

### For Developers

- Fully focus on development
- Deploy apps to any Kubernetes cluster (without understanding Kubernetes 🤯 ).
- Enhance your daily basis workflows with additional helpful commands for `k8s`, `git` and `database`
- Start new project quickly with a set of useful Frameworks.

### For DevOps

- If you’re managing multiple cluster, `dx` is definitely for you.
- Enhance your daily basis tasks with helpful commands to manage clusters, namespaces, secrets, deployments, workloads, etc…
- Monitoring your infrastructure with ease!
    - Manage Kubernetes clusters
    - Manage, backup & restore databases: MongoDB, MariaDB, PostgreSQL,…
- Automations, CI/CD, cronjobs, notifications, alerts,…

### Tech Leads, Managers, Company & Startups

- Manage & monitoring your projects easily.
- Overview of your teams & cloud resources.
- Faster diagnose, better logs, fewer stresses.
- Overview of your organization, your teams, your members, your projects, your apps and your investment in cloud resources.
- Better understanding about what your team is doing.
- Especially if you are poor, like us, but still want to adopt the mighty Kubernetes, `dx` is for you.

**Still not convinced?**

- [I turn my company’s PC into my own “Vercel-like” platform](https://dev.to/mrgoonie/i-turn-my-companys-pc-into-my-own-vercel-like-platform-351o)
- [Kubernetes for the poor](https://dev.to/mrgoonie/kubernetes-for-the-poor-2ne)
- [Speed test building Next.js T3 App with Github Actions, Circle CI, Vercel & DXUP](https://dev.to/mrgoonie/speed-test-building-nextjs-t3-app-with-github-actions-circle-ci-vercel-diginext-473i)
- [Developer-First Platforms - Overcoming K8S Complexity](https://dev.to/mrgoonie/developer-first-platforms-overcoming-k8s-complexity-1lf9)
- [“GitDevSecOps”](https://dev.to/mrgoonie/gitdevsecops-49gp)

## Roadmap

- Check out [this link](https://topgroup.notion.site/Roadmap-6a8266c2929c48ad8d4c11c954e9d852?pvs=4).

---

## Getting Started

- [DXUP website](https://dxup.dev/?ref=github)
- [Official Workspace](https://app.dxup.dev/?ref=github)
- [Documentation](https://docs.dxup.dev/?ref=github)

#### CLI Installation

Install the package globally:

```bash
npm i @topgroup/diginext --location=global
```

#### CLI Update

- To update your CLI to the latest version: `dx update` or `npm update @topgroup/diginext --location=global`.

---

Login to your DXUP workspace:

```bash
dx login 
# is similar with:
# $ dx login https://app.dxup.dev
# in case you hosted DXUP server yourself:
# $ dx login https://<your-diginext-workspace-domain>
cd /path/to/your/app
dx init
dx up

# custom deploy
dx up --prod
dx up --prod --rollout
dx up --prod --rollout --replicas=5
dx up --prod --rollout --replicas=5 --port=3000
dx up --prod --rollout --replicas=5 --port=3000 --select-cluster
# deploy to custom environment
dx up --staging
# deploy to other cluster
dx up --cluster=[cluster-name]
# deploy without SSL
dx up --no-ssl
# deploy with custom domain
dx up --domain=[your-domain]
# deploy with custom container size
dx up --size=2x
# deploy with DX API key
dx up --api-key=[your-dx-api-key]
# redirect all other domains to the first domain (for example: no-www -> www)
dx up --redirect
# upload local .env to dxup deployment
dx up --upload-env
# delete old deployments and deploy new
dx up --fresh
```

That's it!

---

Start developing a new app from boilerplate frameworks:

```bash
dx new
```

Available frameworks:
✓ Next.js (Page Router)
✓ Next.js (App Router)
✓ Nest.js
✓ Bun.js Starter
✓ Express.js Starter
✓ Static website with NGINX
✓ More to come!

## Running DXUP platform on your own infrastructure

**Requirements:**
- A server: any computers with Ubuntu, Debian or CentOS

### 1. With installation script

Access into your server (directly or via SSH), then run this script:

```bash
curl -sfL https://dxup.dev/install/microk8s | sh -
```

👉 [Detailed instruction](https://dev.to/mrgoonie/i-turn-my-companys-pc-into-my-own-vercel-like-platform-351o)

### 2. With Docker Engine

-   **DXUP** requires a MongoDB database to run the build server.

For fastest installation, I recommend to use our `docker-compose.yaml`, you will need to fill in some environment variables:

```yaml
...
  # Add your credentials so you can use Google Sign-in to authenticate with your workspace later on:
  - GOOGLE_CLIENT_ID=
  - GOOGLE_CLIENT_SECRET=
```

Then spin up the build server with: `docker compose up`, it will be available at: `http://localhost:6969`

Access the admin (`http://localhost:6969`) to configure your new workspace.

On the client side, use the CLI command `dx login http://your-workspace-domain.com` to login to your workspace and start new app with `dx new` or start deploying with `dx up` (or `dx deploy`).

👉 Read the [docs here](https://docs.dxup.dev/?ref=github).

### Other installation guides

- [Installation guide](https://topgroup.notion.site/Installation-6de7bda045224ed4b4ee5f4cc5681814?pvs=4)

---

## Changelog

- Visit our [changelog here](CHANGELOG.md)

## Admin UI

- Official workspace: https://app.dxup.dev
- Visit our [source code here](https://github.com/digitopvn/diginext-admin)

## Contributing [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](https://makeapullrequest.com)

Read our [contributing guide](CONTRIBUTING.md) and let's build a better build platform together.

We welcome all contributions. Please read our [CONTRIBUTING.md](CONTRIBUTING.md) first. You can submit any ideas as [pull requests](https://github.com/digitopvn/diginext/pulls) or as [GitHub issues](https://github.com/digitopvn/diginext/issues). If you'd like to improve code, check out the [Development Instructions](https://github.com/digitopvn/diginext/wiki/Development) and have a good time! :)

If you are a collaborator, please follow our [Pull Request principle](https://github.com/digitopvn/diginext/wiki/PR-principle) to create a Pull Request with [collaborator template](https://github.com/digitopvn/diginext/compare?expand=1&template=collaborator.md).


## Community and Support:

Join our community on [Discord](https://discord.gg/xMuW5pN2Kn)!

Suggest improvements and report problems.

---

## Credits / Donations

This is a **ONE-MAN** project & I've been spending a lot of time for it, although it's my hobby project, I still need beers to keep the momentum.
If you enjoyed this project — or just feeling generous, consider buying me some beers. Cheers! 🍻

<a href="https://www.buymeacoffee.com/duynguyen" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-green.png" alt="Buy Me A Coffee" height=48 ></a>

<a href="https://paypal.me/mrgoonie/" target="_blank"><img src="https://github.com/andreostrovsky/donate-with-paypal/blob/master/PNG/blue.png" height=48></a>

<a href="https://opencollective.com/diginext/donate" target="_blank">
  <img src="https://opencollective.com/diginext/donate/button@2x.png?color=blue" height=48 />
</a>

<a href="https://me.momo.vn/mrgoonie" target="_blank">
  <img src="https://github.com/digitopvn/diginext/blob/main/docs/momo-button.png?raw=true" height=48 />
</a>

- Author: Duy Nguyen <duynguyen@wearetopgroup.com>
- CTO at [TOP GROUP](https://wearetopgroup.com)

Thank you!

## My other products

- [DigiCord AI](https://digicord.site) - The Most Useful AI Chatbot on Discord
- [IndieBacklink.com](https://indiebacklink.com) - Indie Makers Unite: Feature, Support, Succeed
- [TopRanking.ai](https://topranking.ai) - AI Directory, listing AI products
- [ZII.ONE](https://zii.one) - Personalized Link Shortener
- [VidCap.xyz](https://vidcap.xyz) - Extract Youtube caption, download videos, capture screenshot, summarize,…
- [ReadTube.me](https://readtube.me) - Write blog articles based on Youtube videos
- [BoostTogether.com](https://boosttogether.com) - The Power of WE in Advertising
- [AIVN.Site](https://aivn.site) - Face Swap, Remove BG, Photo Editor,…
- [DxUp.dev](https://dxup.dev) - Developer-focused platform for app deployment & centralized cloud resource management.

```

### File: .babelrc.js
```js
module.exports = {
	presets: ["@babel/preset-env"],
};

```

### File: .dependency-cruiser.js
```js
/** @type {import('dependency-cruiser').IConfiguration} */
module.exports = {
  forbidden: [
    /* rules from the 'recommended' preset: */
    {
      name: 'no-circular',
      severity: 'warn',
      comment:
        'This dependency is part of a circular relationship. You might want to revise ' +
        'your solution (i.e. use dependency inversion, make sure the modules have a single responsibility) ',
      from: {},
      to: {
        circular: true
      }
    },
    {
      name: 'no-orphans',
      comment:
        "This is an orphan module - it's likely not used (anymore?). Either use it or " +
        "remove it. If it's logical this module is an orphan (i.e. it's a config file), " +
        "add an exception for it in your dependency-cruiser configuration. By default " +
        "this rule does not scrutinize dot-files (e.g. .eslintrc.js), TypeScript declaration " +
        "files (.d.ts), tsconfig.json and some of the babel and webpack configs.",
      severity: 'warn',
      from: {
        orphan: true,
        pathNot: [
          '(^|/)\\.[^/]+\\.(js|cjs|mjs|ts|json)$', // dot files
          '\\.d\\.ts$',                            // TypeScript declaration files
          '(^|/)tsconfig\\.json$',                 // TypeScript config
          '(^|/)(babel|webpack)\\.config\\.(js|cjs|mjs|ts|json)$' // other configs
        ]
      },
      to: {},
    },
    {
      name: 'no-deprecated-core',
      comment:
        'A module depends on a node core module that has been deprecated. Find an alternative - these are ' +
        "bound to exist - node doesn't deprecate lightly.",
      severity: 'warn',
      from: {},
      to: {
        dependencyTypes: [
          'core'
        ],
        path: [
          '^(v8\/tools\/codemap)$',
          '^(v8\/tools\/consarray)$',
          '^(v8\/tools\/csvparser)$',
          '^(v8\/tools\/logreader)$',
          '^(v8\/tools\/profile_view)$',
          '^(v8\/tools\/profile)$',
          '^(v8\/tools\/SourceMap)$',
          '^(v8\/tools\/splaytree)$',
          '^(v8\/tools\/tickprocessor-driver)$',
          '^(v8\/tools\/tickprocessor)$',
          '^(node-inspect\/lib\/_inspect)$',
          '^(node-inspect\/lib\/internal\/inspect_client)$',
          '^(node-inspect\/lib\/internal\/inspect_repl)$',
          '^(async_hooks)$',
          '^(punycode)$',
          '^(domain)$',
          '^(constants)$',
          '^(sys)$',
          '^(_linklist)$',
          '^(_stream_wrap)$'
        ],
      }
    },
    {
      name: 'not-to-deprecated',
      comment:
        'This module uses a (version of an) npm module that has been deprecated. Either upgrade to a later ' +
        'version of that module, or find an alternative. Deprecated modules are a security risk.',
      severity: 'warn',
      from: {},
      to: {
        dependencyTypes: [
          'deprecated'
        ]
      }
    },
    {
      name: 'no-non-package-json',
      severity: 'error',
      comment:
        "This module depends on an npm package that isn't in the 'dependencies' section of your package.json. " +
        "That's problematic as the package either (1) won't be available on live (2 - worse) will be " +
        "available on live with an non-guaranteed version. Fix it by adding the package to the dependencies " +
        "in your package.json.",
      from: {},
      to: {
        dependencyTypes: [
          'npm-no-pkg',
          'npm-unknown'
        ]
      }
    },
    {
      name: 'not-to-unresolvable',
      comment:
        "This module depends on a module that cannot be found ('resolved to disk'). If it's an npm " +
        'module: add it to your package.json. In all other cases you likely already know what to do.',
      severity: 'error',
      from: {},
      to: {
        couldNotResolve: true
      }
    },
    {
      name: 'no-duplicate-dep-types',
      comment:
        "Likely this module depends on an external ('npm') package that occurs more than once " +
        "in your package.json i.e. bot as a devDependencies and in dependencies. This will cause " +
        "maintenance problems later on.",
      severity: 'warn',
      from: {},
      to: {
        moreThanOneDependencyType: true,
        // as it's pretty common to have a type import be a type only import 
        // _and_ (e.g.) a devDependency - don't consider type-only dependency
        // types for this rule
        dependencyTypesNot: ["type-only"]
      }
    },

    /* rules you might want to tweak for your specific situation: */
    {
      name: 'not-to-test',
      comment:
        "This module depends on code within a folder that should only contain tests. As tests don't " +
        "implement functionality this is odd. Either you're writing a test outside the test folder " +
        "or there's something in the test folder that isn't a test.",
      severity: 'error',
      from: {
        pathNot: '^(__tests__)'
      },
      to: {
        path: '^(__tests__)'
      }
    },
    {
      name: 'not-to-spec',
      comment:
        'This module depends on a spec (test) file. The sole responsibility of a spec file is to test code. ' +
        "If there's something in a spec that's of use to other modules, it doesn't have that single " +
        'responsibility anymore. Factor it out into (e.g.) a separate utility/ helper or a mock.',
      severity: 'error',
      from: {},
      to: {
        path: '\\.(spec|test)\\.(js|mjs|cjs|ts|ls|coffee|litcoffee|coffee\\.md)$'
      }
    },
    {
      name: 'not-to-dev-dep',
      severity: 'error',
      comment:
        "This module depends on an npm package from the 'devDependencies' section of your " +
        'package.json. It looks like something that ships to production, though. To prevent problems ' +
        "with npm packages that aren't there on production declare it (only!) in the 'dependencies'" +
        'section of your package.json. If this module is development only - add it to the ' +
        'from.pathNot re of the not-to-dev-dep rule in the dependency-cruiser configuration',
      from: {
        path: '^(src)',
        pathNot: '\\.(spec|test)\\.(js|mjs|cjs|ts|ls|coffee|litcoffee|coffee\\.md)$'
      },
      to: {
        dependencyTypes: [
          'npm-dev'
        ]
      }
    },
    {
      name: 'optional-deps-used',
      severity: 'info',
      comment:
        "This module depends on an npm package that is declared as an optional dependency " +
        "in your package.json. As this makes sense in limited situations only, it's flagged here. " +
        "If you're using an optional dependency here by design - add an exception to your" +
        "dependency-cruiser configuration.",
      from: {},
      to: {
        dependencyTypes: [
          'npm-optional'
        ]
      }
    },
    {
      name: 'peer-deps-used',
      comment:
        "This module depends on an npm package that is declared as a peer dependency " +
        "in your package.json. This makes sense if your package is e.g. a plugin, but in " +
        "other cases - maybe not so much. If the use of a peer dependency is intentional " +
        "add an exception to your dependency-cruiser configuration.",
      severity: 'warn',
      from: {},
      to: {
        dependencyTypes: [
          'npm-peer'
        ]
      }
    }
  ],
  options: {

    /* conditions specifying which files not to follow further when encountered:
       - path: a regular expression to match
       - dependencyTypes: see https://github.com/sverweij/dependency-cruiser/blob/main/doc/rules-reference.md#dependencytypes-and-dependencytypesnot
       for a complete list
    */
    doNotFollow: {
      path: 'node_modules'
    },

    /* conditions specifying which dependencies to exclude
       - path: a regular expression to match
       - dynamic: a boolean indicating whether to ignore dynamic (true) or static (false) dependencies.
          leave out if you want to exclude neither (recommended!)
    */
    // exclude : {
    //   path: '',
    //   dynamic: true
    // },

    /* pattern specifying which files to include (regular expression)
       dependency-cruiser will skip everything not matching this pattern
    */
    // includeOnly : '',

    /* dependency-cruiser will include modules matching against the focus
       regular expression in its output, as well as their neighbours (direct
       dependencies and dependents)
    */
    // focus : '',

    /* list of module systems to cruise */
    // moduleSystems: ['amd', 'cjs', 'es6', 'tsd'],

    /* prefix for links in html and svg output (e.g. 'https://github.com/you/yourrepo/blob/develop/'
       to open it on your online repo or `vscode://file/${process.cwd()}/` to 
       open it in visual studio code),
     */
    // prefix: '',

    /* false (the default): ignore dependencies that only exist before typescript-to-javascript compilation
       true: also detect dependencies that only exist before typescript-to-javascript compilation
       "specify": for each dependency identify whether it only exists before compilation or also after
     */
    tsPreCompilationDeps: true,
    
    /* 
       list of extensions to scan that aren't javascript or compile-to-javascript. 
       Empty by default. Only put extensions in here that you want to take into
       account that are _not_ parsable. 
    */
    // extraExtensionsToScan: [".json", ".jpg", ".png", ".svg", ".webp"],

    /* if true combines the package.jsons found from the module up to the base
       folder the cruise is initiated from. Useful for how (some) mono-repos
       manage dependencies & dependency definitions.
     */
    // combinedDependencies: false,

    /* if true leave symlinks untouched, otherwise use the realpath */
    // preserveSymlinks: false,

    /* TypeScript project file ('tsconfig.json') to use for
       (1) compilation and
       (2) resolution (e.g. with the paths property)

       The (optional) fileName attribute specifies which file to take (relative to
       dependency-cruiser's current working directory). When not provided
       defaults to './tsconfig.json'.
     */
    tsConfig: {
      fileName: 'tsconfig.json'
    },

    /* Webpack configuration to use to get resolve options from.

       The (optional) fileName attribute specifies which file to take (relative
       to dependency-cruiser's current working directory. When not provided defaults
       to './webpack.conf.js'.

       The (optional) `env` and `arguments` attributes contain the parameters to be passed if
       your webpack config is a function and takes them (see webpack documentation
       for details)
     */
    // webpackConfig: {
    //  fileName: './webpack.config.js',
    //  env: {},
    //  arguments: {},
    // },

    /* Babel config ('.babelrc', '.babelrc.json', '.babelrc.json5', ...) to use
      for compilation (and whatever other naughty things babel plugins do to
      source code). This feature is well tested and usable, but might change
      behavior a bit over time (e.g. more precise results for used module 
      systems) without dependency-cruiser getting a major version bump.
     */
    // babelConfig: {
    //   fileName: './.babelrc'
    // },

    /* List of strings you have in use in addition to cjs/ es6 requires
       & imports to declare module dependencies. Use this e.g. if you've
       re-declared require, use a require-wrapper or use window.require as
       a hack.
    */
    // exoticRequireStrings: [],
    /* options to pass on to enhanced-resolve, the package dependency-cruiser
       uses to resolve module references to disk. You can set most of these
       options in a webpack.conf.js - this section is here for those
       projects that don't have a separate webpack config file.

       Note: settings in webpack.conf.js override the ones specified here.
     */
    enhancedResolveOptions: {
      /* List of strings to consider as 'exports' fields in package.json. Use
         ['exports'] when you use packages that use such a field and your environment
         supports it (e.g. node ^12.19 || >=14.7 or recent versions of webpack).

         If you have an `exportsFields` attribute in your webpack config, that one
         will have precedence over the one specified here.
      */ 
      exportsFields: ["exports"],
      /* List of conditions to check for in the exports field. e.g. use ['imports']
         if you're only interested in exposed es6 modules, ['require'] for commonjs,
         or all conditions at once `(['import', 'require', 'node', 'default']`)
         if anything goes for you. Only works when the 'exportsFields' array is
         non-empty.

        If you have a 'conditionNames' attribute in your webpack config, that one will
        have precedence over the one specified here.
      */
      conditionNames: ["import", "require", "node", "default"],
      /*
         The extensions, by default are the same as the ones dependency-cruiser
         can access (run `npx depcruise --info` to see which ones that are in
         _your_ environment. If that list is larger than what you need (e.g. 
         it contains .js, .jsx, .ts, .tsx, .cts, .mts - but you don't use 
         TypeScript you can pass just the extensions you actually use (e.g. 
         [".js", ".jsx"]). This can speed up the most expensive step in 
         dependency cruising (module resolution) quite a bit.
       */
      // extensions: [".js", ".jsx", ".ts", ".tsx", ".d.ts"],
      /* 
         If your TypeScript project makes use of types specified in 'types'
         fields in package.jsons of external dependencies, specify "types"
         in addition to "main" in here, so enhanced-resolve (the resolver
         dependency-cruiser uses) knows to also look there. You can also do
         this if you're not sure, but still use TypeScript. In a future version
         of dependency-cruiser this will likely become the default.
       */
      mainFields: ["main", "types"],
    },
    reporterOptions: {
      dot: {
        /* pattern of modules that can be consolidated in the detailed
           graphical dependency graph. The default pattern in this configuration
           collapses everything in node_modules to one folder deep so you see
           the external modules, but not the innards your app depends upon.
         */
        collapsePattern: 'node_modules/(@[^/]+/[^/]+|[^/]+)',

        /* Options to tweak the appearance of your graph.See
           https://github.com/sverweij/dependency-cruiser/blob/main/doc/options-reference.md#reporteroptions
           for details and some examples. If you don't specify a theme
           don't worry - dependency-cruiser will fall back to the default one.
        */
        // theme: {
        //   graph: {
        //     /* use splines: "ortho" for straight lines. Be aware though
        //       graphviz might take a long time calculating ortho(gonal)
        //       rout
... [TRUNCATED]
```

### File: .prettierrc.json
```json
{
	"trailingComma": "es5",
	"tabWidth": 4,
	"useTabs": true,
	"semi": true,
	"singleQuote": false,
	"endOfLine": "lf",
	"printWidth": 150
}

```

### File: 05-podman-fuse-device-plugin.yaml
```yaml
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: fuse-device-plugin-daemonset
  namespace: kube-system
spec:
  selector:
    matchLabels:
      name: fuse-device-plugin-ds
  template:
    metadata:
      labels:
        name: fuse-device-plugin-ds
    spec:
      hostNetwork: true
      containers:
      - image: soolaugust/fuse-device-plugin:v1.0
        name: fuse-device-plugin-ctr
        securityContext:
          allowPrivilegeEscalation: false
          capabilities:
            drop: ["ALL"]
        volumeMounts:
          - name: device-plugin
            mountPath: /var/lib/kubelet/device-plugins
      volumes:
        - name: device-plugin
          hostPath:
            path: /var/lib/kubelet/device-plugins
      imagePullSecrets:
        - name: registry-secret
```

### File: CODE_OF_CONDUCT.md
```md
# Contributor Covenant Code of Conduct

## Our Pledge

In the interest of fostering an open and welcoming environment, we as contributors and maintainers pledge to making participation in our project and our community a harassment-free experience for everyone, regardless of age, body size, disability, ethnicity, gender identity and expression, level of experience, nationality, personal appearance, race, religion, or sexual identity and orientation.

## Our Standards

Examples of behavior that contributes to creating a positive environment include:

- Using welcoming and inclusive language
- Being respectful of differing viewpoints and experiences
- Gracefully accepting constructive criticism
- Focusing on what is best for the community
- Showing empathy towards other community members

Examples of unacceptable behavior by participants include:

- The use of sexualized language or imagery and unwelcome sexual attention or advances
- Trolling, insulting/derogatory comments, and personal or political attacks
- Public or private harassment
- Publishing others' private information, such as a physical or electronic address, without explicit permission
- Other conduct which could reasonably be considered inappropriate in a professional setting

## Our Responsibilities

Project maintainers are responsible for clarifying the standards of acceptable behavior and are expected to take appropriate and fair corrective action in response to any instances of unacceptable behavior.

Project maintainers have the right and responsibility to remove, edit, or reject comments, commits, code, wiki edits, issues, and other contributions that are not aligned to this Code of Conduct, or to ban temporarily or permanently any contributor for other behaviors that they deem inappropriate, threatening, offensive, or harmful.

## Scope

This Code of Conduct applies both within project spaces and in public spaces when an individual is representing the project or its community. Examples of representing a project or community include using an official project e-mail address, posting via an official social media account, or acting as an appointed representative at an online or offline event. Representation of a project may be further defined and clarified by project maintainers.

## Enforcement

Instances of abusive, harassing, or otherwise unacceptable behavior may be reported by contacting the project team at [dev@dxup.dev](mailto:dev@dxup.dev) The project team will review and investigate all complaints, and will respond in a way that it deems appropriate to the circumstances. The project team is obligated to maintain confidentiality with regard to the reporter of an incident. Further details of specific enforcement policies may be posted separately.

Project maintainers who do not follow or enforce the Code of Conduct in good faith may face temporary or permanent repercussions as determined by other members of the project's leadership.

## Attribution

This Code of Conduct is adapted from the [Contributor Covenant][homepage], version 1.4, available at [http://contributor-covenant.org/version/1/4][version].

[homepage]: http://contributor-covenant.org
[version]: http://contributor-covenant.org/version/1/4/
```

### File: commitlint.config.js
```js
module.exports = {
    extends: ["@commitlint/config-conventional"],
    ignores: [(message) => /chore/m.test(message)],
    rules: {
        'body-max-line-length': [0, 'always', 100],
		"subject-case": [0, "never", ["sentence-case", "start-case", "pascal-case", "upper-case"]],
	},
};

```

### File: CONTRIBUTING.md
```md
The following is a set of guidelines for contributing to Diginext. Please spend several minutes reading these guidelines before you create an issue or pull request.

## Code of Conduct

We have adopted a [Code of Conduct](CODE_OF_CONDUCT.md) that we expect project participants to adhere to. Please read the full text so that you can understand what actions will and will not be tolerated.

## Open Development

All work on Diginext happens directly on [GitHub](https://github.com/digitopvn/diginext). Both core team members and external contributors send pull requests which go through the same review process.

Wanna give me a hand? Get started here: [DEVELOPER.md](DEVELOPER.md)

## Branch Organization

According to our [release schedule](changelog#release-schedule), we maintain two branches, `main` and `feature`. If you send a bugfix pull request, please do it against the `main` branch, if it's a feature pull request, please do it against the `feature` branch.

## Bugs

We are using [GitHub Issues](https://github.com/digitopvn/diginext/issues) for bug tracking. The best way to get your bug fixed is by providing reproduction steps with this [template](https://github.com/digitopvn/diginext/issues/new?assignees=&labels=&template=bug_report.md&title=%5BBUG%5D).

Before you report a bug, please make sure you've searched existing issues, and read our [FAQ](FAQ.md).

## Proposing a Change

If you intend to change the public API or introduce new feature, we also recommend you use our [issue helper](https://github.com/digitopvn/diginext/issues/new?assignees=&labels=&template=propose_change.md&title=) to create a proposal issue.

## Your First Pull Request

Working on your first Pull Request? You can learn how from this free video series:

[How to Contribute to an Open Source Project on GitHub](https://egghead.io/courses/how-to-contribute-to-an-open-source-project-on-github)

To help you get your feet wet and get you familiar with our contribution process, we have a list of [good first issues](https://github.com/digitopvn/diginext/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22) that contain bugs or small features that have a relatively limited scope. This is a great place to get started.

If you decide to fix an issue, please be sure to check the comment thread in case somebody is already working on a fix. If nobody is working on it at the moment, please leave a comment stating that you intend to work on it so other people don't accidentally duplicate your effort.

If somebody claims an issue but doesn't follow up for more than two weeks, it's fine to take over it but you should still leave a comment.

## Sending a Pull Request

The core team is monitoring for pull requests. We will review your pull request and either merge it, request changes to it, or close it with an explanation.

**Before submitting a pull request**, please make sure the following is done:

1. Fork the repository and create your branch from the [correct branch](#branch-organization).
1. Run `npm install` in the repository root.
   > For Windows 10 development environment, if you run into error `gyp err! find vs msvs_version not set from command line or npm config`, please install [the latest Python v3](https://www.python.org/downloads/) and **Desktop development with C++** through [Visual Studio Installer](https://docs.microsoft.com/en-us/visualstudio/install/install-visual-studio?view=vs-2019#step-3---install-the-visual-studio-installer) before running `npm install`
1. If you've fixed a bug or added code that should be tested, add tests!
1. Ensure the test suite passes (npm run test). Tip: `npm test -- --watch TestName` is helpful in development.
1. Run `npm test -- -u` to update the [jest snapshots](http://facebook.github.io/jest/docs/en/snapshot-testing.html#snapshot-testing-with-jest) and commit these changes as well (if there are any updates).
1. Ensure the UI change passes `npm run test-image`，Run `npm run test-image -- -u` to update UI snapshots and commit these changes as well (if there are any updates), **UI test base on [Docker](https://docs.docker.com/get-docker/), need download the corresponding installation according to the platform**
1. Make sure your code lints (npm run lint). Tip: Lint runs automatically when you `git commit` (Use [Git Hooks](https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks)).

Sending a Pull Request to [react-component](https://github.com/react-component/):

If it's a bugfix pull request, after it's merged, the core team will release a patch release for that component as soon as possible, then you only need to reinstall Diginext (DX) in your project to get the latest patch release. If it's a feature pull request, after it's merged, the core team will release a minor release, then you need raise another pull request to [Diginext](https://github.com/digitopvn/diginext/) to update dependencies, document and TypeScript interfaces (if needed).

## Development Workflow

After cloning `dx`, run `npm install` to fetch its dependencies. Then, you can run several commands:

1. `npm start` runs Diginext website locally.
1. `npm run lint` checks the code style.
2. `npm test` runs the complete test suite.

## Development Tools

- Docker: https://www.docker.com/

## Being a collaborator

If you are an active contributor and are willing to work with Diginext Team in our opensource workflow, you can [apply to be a outside collaborator](https://github.com/digitopvn/diginext/wiki/Collaborators#how-to-apply-for-being-a-collaborator).

---

**Working on your first Pull Request?** You can learn how from this *free* series [How to Contribute to an Open Source Project on GitHub](https://kcd.im/pull-request)
```

### File: deployment.docker.example.yaml
```yaml
# SERVICE CONFIGURATION
apiVersion: v1
kind: Service
metadata:
  name: diginext-svc
  namespace: diginext
  labels:
    app: diginext
spec:
  # type: NodePort
  ports:
    - port: 6969
  selector:
    app: diginext
---
# POD DEPLOYMENT CONFIGURATION
apiVersion: apps/v1
kind: Deployment
metadata:
  name: diginext
  namespace: diginext
spec:
  replicas: 1
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 0
  selector:
    matchLabels:
      app: diginext
  template:
    metadata:
      labels:
        app: diginext
    spec:
      containers:
        - name: diginext
          image: digitop/diginext:latest
          ports:
            - containerPort: 6969
          securityContext:
            # this is required for Docker but very dangerous !
            privileged: true
            runAsUser: 0
          env:
            - name: TZ
              value: Asia/Ho_Chi_Minh
            - name: PORT
              value: "6969"
            - name: NODE_ENV
              value: production
            - name: CLI_MODE
              value: server
            - name: DEV_MODE
              value: "false"
            - name: BASE_URL
              value: https://api.dxup.dev
            - name: DB_URI
              value: # mongodb://... insert here
            - name: JWT_SECRET
              value: # insert here
            - name: JWT_EXPIRE_TIME
              value: 48h
            - name: GOOGLE_CLIENT_ID
              value: # insert here
            - name: GOOGLE_CLIENT_SECRET
              value: # insert here
            - name: BUILDER
              value: docker
          volumeMounts:
            # this is required for Docker but very dangerous !
            - name: docker-sock
              mountPath: /var/run/docker.sock
            - name: storage
              mountPath: /var/app/storage
            # - name: home
            #   mountPath: /root
      volumes:
        # this is required for Docker but very dangerous !
        - name: docker-sock
          hostPath:
            path: "/var/run/docker.sock"
        - name: storage
          hostPath:
            path: /home/dev/diginext/storage
        - name: home
          hostPath:
            path: /home/dev/diginext/storage/home


```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.

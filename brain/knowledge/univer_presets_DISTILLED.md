---
id: univer-presets
type: knowledge
owner: OA_Triage
---
# univer-presets
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
    "name": "univer-presets",
    "version": "0.20.0",
    "private": true,
    "packageManager": "pnpm@10.27.0",
    "author": "DreamNum Co., Ltd. <developer@univer.ai>",
    "license": "Apache-2.0",
    "engines": {
        "node": ">=20",
        "pnpm": ">=10"
    },
    "scripts": {
        "prepare": "simple-git-hooks",
        "dev": "pnpm --filter examples dev:demo",
        "dev:libs": "pnpm --filter examples dev:demo-libs",
        "build": "turbo build:preset --concurrency=100% && pnpm --filter @univerjs/presets build",
        "build:demo": "pnpm --filter examples build:demo",
        "build:node-demo": "pnpm --filter examples-node build:demo",
        "lint": "eslint .",
        "typecheck": "turbo typecheck",
        "release": "release-it",
        "update:sdk": "tsx scripts/update-dependencies.ts"
    },
    "devDependencies": {
        "@antfu/eslint-config": "^6.7.3",
        "@release-it-plugins/workspaces": "^5.0.3",
        "@release-it/conventional-changelog": "^10.0.6",
        "@types/fs-extra": "^11.0.4",
        "@univerjs/core": "0.20.0",
        "cross-env": "^10.1.0",
        "eslint": "^9.39.2",
        "eslint-plugin-format": "^1.2.0",
        "fs-extra": "^11.3.4",
        "lint-staged": "^16.4.0",
        "release-it": "19.2.4",
        "simple-git-hooks": "^2.13.1",
        "tsx": "^4.21.0",
        "turbo": "^2.8.17"
    },
    "overrides": {
        "vite": "7"
    },
    "simple-git-hooks": {
        "pre-commit": "pnpm lint-staged"
    },
    "lint-staged": {
        "*": "eslint"
    }
}

```

### File: README.md
```md
# Univer Presets

This project provide several collections of Univer plugins for out-of-the-box solutions.

## Presets

...and corresponding examples as follows:

### For Browsers

- Basic Spreadsheet
- Spreadsheet with Advanced Features
- Spreadsheet with Advanced Features and Collaboration Features

### For Node.js

- Headless Spreadsheet
- [ ] Headless Spreadsheet with Advanced Features

## Usage

Please to our [official website](https://univer.ai/guides/quick-start). If these presets do not meet your requirements, you can use code in examples and presets as references.

## Contributing

Please open issues to submit your feature requirements.

```

### File: examples\package.json
```json
{
    "name": "examples",
    "version": "0.0.0",
    "private": true,
    "author": "DreamNum Co., Ltd. <developer@univer.ai>",
    "license": "Apache-2.0",
    "scripts": {
        "dev:demo": "node ./esbuild.config.mjs --watch",
        "dev:demo-libs": "cross-env LINK_PRESET_TO_LIB=true pnpm dev:demo",
        "build:demo": "node ./esbuild.config.mjs"
    },
    "dependencies": {
        "@univerjs/icons": "1.1.1",
        "@univerjs/presets": "workspace:*",
        "@univerjs/sheets-zen-editor": "0.20.0",
        "monaco-editor": "0.55.1",
        "react": "18.3.1",
        "react-dom": "18.3.1",
        "react-mosaic-component": "^6.1.1"
    },
    "devDependencies": {
        "cross-env": "^10.1.0",
        "detect-port": "^2.1.0",
        "dotenv": "^17.3.1",
        "esbuild": "^0.27.4",
        "esbuild-plugin-clean": "^1.0.1",
        "esbuild-plugin-copy": "^2.1.1",
        "esbuild-plugin-vue3": "^0.5.1",
        "esbuild-style-plugin": "^1.6.3",
        "http-proxy": "^1.18.1",
        "minimist": "^1.2.8",
        "typescript": "^5.9.3"
    }
}

```

### File: common\shared\package.json
```json
{
    "name": "@univerjs-infra/shared",
    "version": "0.20.0",
    "private": true,
    "description": "Some infrastructures for univerjs",
    "author": "DreamNum Co., Ltd. <developer@univer.ai>",
    "license": "Apache-2.0",
    "homepage": "https://github.com/dream-num/univer",
    "repository": {
        "type": "git",
        "url": "https://github.com/dream-num/univer.git"
    },
    "keywords": [],
    "exports": {
        "./tsconfigs/*": "./tsconfigs/*.json",
        "./prepare": "./prepare/index.ts",
        "./vite": "./vite/index.ts"
    },
    "dependencies": {
        "fs-extra": "^11.3.4",
        "vite": "7",
        "vite-plugin-dts": "^4.5.4",
        "vite-plugin-external": "^6.2.2"
    },
    "devDependencies": {
        "@types/fs-extra": "^11.0.4"
    }
}

```

### File: .release-it.json
```json
{
    "git": {
        "commitMessage": "chore(release): release v${version}",
        "tagName": "v${version}"
    },
    "npm": false,
    "github": {
        "release": true
    },
    "plugins": {
        "@release-it/conventional-changelog": {
            "preset": "angular",
            "infile": "CHANGELOG.md",
            "ignoreRecommendedBump": true
        },

        "@release-it-plugins/workspaces": {
            "publish": false,
            "skipChecks": true,
            "workspaces": [
                "common/*",
                "packages/*"
            ]
        }
    }
}

```

### File: CHANGELOG.md
```md
# Changelog

# [0.20.0](https://github.com/dream-num/univer-presets/compare/v0.19.0...v0.20.0) (2026-04-03)


### Features

* add pivot.maxLimitItemCount config in UniverSheetsAdvancedPreset ([#119](https://github.com/dream-num/univer-presets/issues/119)) ([75e5ee3](https://github.com/dream-num/univer-presets/commit/75e5ee341d22e8b08c7dbe37dd8a84494caa18f5))
* update sdk to 0.20.0 ([5bc4d1a](https://github.com/dream-num/univer-presets/commit/5bc4d1a76081083d6b428c93839fe82e92ca1352))

# [0.19.0](https://github.com/dream-num/univer-presets/compare/v0.18.0...v0.19.0) (2026-03-28)


### Features

* update sdk to 0.19.0 ([4e00065](https://github.com/dream-num/univer-presets/commit/4e0006591a4d8aebb64dd6cf2083f36a7ad817a0))

# [0.18.0](https://github.com/dream-num/univer-presets/compare/v0.17.0...v0.18.0) (2026-03-18)


### Features

* update sdk to 0.18.0 ([6d7f3e5](https://github.com/dream-num/univer-presets/commit/6d7f3e5653d5fcd654cc2b43e22a4ce026ee7f49))

# [0.17.0](https://github.com/dream-num/univer-presets/compare/v0.16.1...v0.17.0) (2026-03-11)


### Features

* update sdk to 0.17.0 ([74f1616](https://github.com/dream-num/univer-presets/commit/74f1616a6b4a74688e52ae403b18d24f6a9d68dc))

## [0.16.1](https://github.com/dream-num/univer-presets/compare/v0.16.0...v0.16.1) (2026-03-03)


### Features

* update sdk to 0.16.1 ([981ddfc](https://github.com/dream-num/univer-presets/commit/981ddfccb18b17515acc12ec5d50cf0a84b2acc5))

# [0.16.0](https://github.com/dream-num/univer-presets/compare/v0.15.5...v0.16.0) (2026-02-28)


### Features

* advanced preset add shape feature ([#116](https://github.com/dream-num/univer-presets/issues/116)) ([18e6267](https://github.com/dream-num/univer-presets/commit/18e62672df07b4a3af01ecd418a4b4d835fa2ab0))
* update sdk to 0.16.0 ([303e667](https://github.com/dream-num/univer-presets/commit/303e6679360ad51a8d6adfcc5bd07fc656499bf6))

## [0.15.5](https://github.com/dream-num/univer-presets/compare/v0.15.4...v0.15.5) (2026-02-11)


### Features

* update sdk to 0.15.5 ([96ab415](https://github.com/dream-num/univer-presets/commit/96ab4154a496b6d2a18236724b4b6a80fad0f926))

## [0.15.4](https://github.com/dream-num/univer-presets/compare/v0.15.3...v0.15.4) (2026-01-31)


### Features

* add 'sk-SK' locale to LOCLAES_MAP ([#115](https://github.com/dream-num/univer-presets/issues/115)) ([90f0d76](https://github.com/dream-num/univer-presets/commit/90f0d76cc4a309ffbe8c3eb31fab5e7805745713))
* update sdk to 0.15.4 ([9962600](https://github.com/dream-num/univer-presets/commit/996260062fb8aadf9e40a5a7a2c2dc9d66b9cdfe))

## [0.15.3](https://github.com/dream-num/univer-presets/compare/v0.15.2...v0.15.3) (2026-01-24)


### Features

* update sdk to 0.15.3 ([c09c6fa](https://github.com/dream-num/univer-presets/commit/c09c6fafce6006a9709023f4e77185cb1de92a1c))

## [0.15.2](https://github.com/dream-num/univer-presets/compare/v0.15.1...v0.15.2) (2026-01-17)


### Features

* update sdk to 0.15.2 ([b0ea615](https://github.com/dream-num/univer-presets/commit/b0ea6150da0fc62f4f1814f3e9a730491169b6cc))

## [0.15.1](https://github.com/dream-num/univer-presets/compare/v0.15.0...v0.15.1) (2026-01-10)


### Features

* preset-sheets-data-validation add showSearchOnDropdown config ([0025b03](https://github.com/dream-num/univer-presets/commit/0025b0399daeda54bb3d31fb8e27a16fcb9510d4))

# [0.15.0](/compare/v0.14.0...v0.15.0) (2025-12-27)


### Features

* UniverSheetsCollaborationPreset add enableFrontendLog config (#112) f59430f, closes #112
* update sdk to 0.15.0 1217284

# [0.14.0](/compare/v0.13.0...v0.14.0) (2025-12-20)


### Features

* update sdk to 0.14.0 d76c075

# [0.13.0](/compare/v0.12.4...v0.13.0) (2025-12-13)


### Features

* update sdk to 0.13.0 684eb11

## [0.12.4](https://github.com/dream-num/univer-presets/compare/v0.12.3...v0.12.4) (2025-12-06)


### Features

* update sdk to 0.12.4 ([5e3b2b2](https://github.com/dream-num/univer-presets/commit/5e3b2b2050d083cf9c02f5b5723757eb2f5c0117))

## [0.12.3](https://github.com/dream-num/univer-presets/compare/v0.12.2...v0.12.3) (2025-11-29)


### Features

* update sdk to 0.12.3 ([403ed56](https://github.com/dream-num/univer-presets/commit/403ed56e4a436632a322f694452dc297eb2e2747))

## [0.12.2](https://github.com/dream-num/univer-presets/compare/v0.12.1...v0.12.2) (2025-11-22)


### Features

* update sdk to 0.12.2 ([69f170e](https://github.com/dream-num/univer-presets/commit/69f170ef3eb3225e52b6c66ba42367d25f79b6b6))

## [0.12.1](https://github.com/dream-num/univer-presets/compare/v0.12.0...v0.12.1) (2025-11-22)


### Features

* update sdk to 0.12.1 ([659c5ed](https://github.com/dream-num/univer-presets/commit/659c5ed8ccfa9b2dcac90665de4a7f17fcb08e6a))
* update sdk to 0.12.1 ([1f4dea8](https://github.com/dream-num/univer-presets/commit/1f4dea89dfd3c4e01e2e50f13e714be4a652f721))

# [0.12.0](https://github.com/dream-num/univer-presets/compare/v0.11.0...v0.12.0) (2025-11-15)


### Features

* update sdk to 0.12.0 ([c970a96](https://github.com/dream-num/univer-presets/commit/c970a96da191c3d6a717a44023cb1904b3f8337d))

# [0.11.0](https://github.com/dream-num/univer-presets/compare/v0.10.14...v0.11.0) (2025-11-08)


### Bug Fixes

* fix the issue where the import/export feature is broken in UMD bundle ([#106](https://github.com/dream-num/univer-presets/issues/106)) ([9582c46](https://github.com/dream-num/univer-presets/commit/9582c465e9b2cc1566eb13ee54e0e63089c0b650))


### Features

* update sdk to 0.11.0 ([560e78d](https://github.com/dream-num/univer-presets/commit/560e78d89658dd43f9c40b02243d03a8c269f814))

## [0.10.14](https://github.com/dream-num/univer-presets/compare/v0.10.13...v0.10.14) (2025-10-29)


### Features

* update sdk to 0.10.14 ([770130b](https://github.com/dream-num/univer-presets/commit/770130b071534bac84780e1a4ae86686a8ac3b66))

## [0.10.13](https://github.com/dream-num/univer-presets/compare/v0.10.12...v0.10.13) (2025-10-25)


### Features

* update sdk to 0.10.13 ([d5382f6](https://github.com/dream-num/univer-presets/commit/d5382f6a5b54de09dc367080f58c85ac2726573f))

## [0.10.12](https://github.com/dream-num/univer-presets/compare/v0.10.11...v0.10.12) (2025-10-22)


### Features

* update sdk to 0.10.12 ([491b4ff](https://github.com/dream-num/univer-presets/commit/491b4ff66e30d186f5f5eacd10b8708d4592a925))

## [0.10.11](https://github.com/dream-num/univer-presets/compare/v0.10.10...v0.10.11) (2025-10-18)


### Features

* update sdk to 0.10.11 ([d53006d](https://github.com/dream-num/univer-presets/commit/d53006dcbe51199638eaac6732543e38f84e3921))

## [0.10.10](https://github.com/dream-num/univer-presets/compare/v0.10.9...v0.10.10) (2025-09-26)


### Features

* update sdk to 0.10.10 ([06b4b2a](https://github.com/dream-num/univer-presets/commit/06b4b2af3d3641a3f91f989fe52144f226e44e0f))

## [0.10.9](https://github.com/dream-num/univer-presets/compare/v0.10.8...v0.10.9) (2025-09-20)


### Features

* update sdk to 0.10.9 ([fba1c9a](https://github.com/dream-num/univer-presets/commit/fba1c9a4fbaa25af70aa4bd96a698ddb777c504f))

## [0.10.8](https://github.com/dream-num/univer-presets/compare/v0.10.7...v0.10.8) (2025-09-13)


### Features

* update sdk to 0.10.8 ([24d547f](https://github.com/dream-num/univer-presets/commit/24d547f4a5905baa3b380656b109d4a1978ed0a0))

## [0.10.7](https://github.com/dream-num/univer-presets/compare/v0.10.6...v0.10.7) (2025-09-06)


### Features

* update sdk to 0.10.7 ([a4724a7](https://github.com/dream-num/univer-presets/commit/a4724a78b242bd5bdf81b6fdcaae8f13b8f7bb76))

## [0.10.6](https://github.com/dream-num/univer-presets/compare/v0.10.5...v0.10.6) (2025-08-29)


### Features

* update sdk to 0.10.6 ([dfe5dfa](https://github.com/dream-num/univer-presets/commit/dfe5dfa7dc4bb9e223503fbe8bfa72bda63c9fd7))

## [0.10.5](https://github.com/dream-num/univer-presets/compare/v0.10.4...v0.10.5) (2025-08-22)


### Features

* update sdk to 0.10.5 ([ed5c498](https://github.com/dream-num/univer-presets/commit/ed5c4985b65b16c50b0fafcfa92b4d5bd4a8eac7))

## [0.10.4](https://github.com/dream-num/univer-presets/compare/v0.10.3...v0.10.4) (2025-08-15)


### Features

* update sdk to 0.10.4 ([5c675b5](https://github.com/dream-num/univer-presets/commit/5c675b585287b1b8fd79ebd2e47e291548d9f18a))

## [0.10.3](https://github.com/dream-num/univer-presets/compare/v0.10.2...v0.10.3) (2025-08-08)


### Features

* update sdk to 0.10.3 ([38dedeb](https://github.com/dream-num/univer-presets/commit/38dedebc34c0cd25011d5db5e46a383c754f60a0))

## [0.10.2](https://github.com/dream-num/univer-presets/compare/v0.10.1...v0.10.2) (2025-08-02)


### Features

* add umdAdditionalLocales option to build configuration ([#101](https://github.com/dream-num/univer-presets/issues/101)) ([45f4347](https://github.com/dream-num/univer-presets/commit/45f434704db135c3c90cdbe82769149e81098b61))
* update sdk to 0.10.2 ([d418668](https://github.com/dream-num/univer-presets/commit/d418668a685f8ce84d0101686d8e029b1f3c079a))

## [0.10.1](https://github.com/dream-num/univer-presets/compare/v0.10.0...v0.10.1) (2025-07-31)

# [0.10.0](https://github.com/dream-num/univer-presets/compare/v0.9.4...v0.10.0) (2025-07-29)


### Features

* remove customComponents config ([9b519b5](https://github.com/dream-num/univer-presets/commit/9b519b58e93866b0f7abeed2dde3d7c206f1e983))
* update sdk to 0.10.0 ([12bbe7e](https://github.com/dream-num/univer-presets/commit/12bbe7ee69ca28aaf4da63291ca92442595d8a85))

## [0.9.4](https://github.com/dream-num/univer-presets/compare/v0.9.3...v0.9.4) (2025-07-25)


### Features

* export edit-history-viewer from collaboration preset ([#98](https://github.com/dream-num/univer-presets/issues/98)) ([fe11e01](https://github.com/dream-num/univer-presets/commit/fe11e0146d387158b29dcc941cd0bc6c6604a542))
* update sdk to 0.9.4 ([8cf8909](https://github.com/dream-num/univer-presets/commit/8cf89097edf4752bdaf389fd482991bb98d0860a))

## [0.9.3](https://github.com/dream-num/univer-presets/compare/v0.9.2...v0.9.3) (2025-07-19)


### Features

* add locales Spanish (es-ES) and Catalan (ca-ES) ([#96](https://github.com/dream-num/univer-presets/issues/96)) ([dad08a3](https://github.com/dream-num/univer-presets/commit/dad08a3e8742d3b47f2446f0fd813558d9acf765))
* add offline editing and single active instance lock options to collaboration preset config ([#97](https://github.com/dream-num/univer-presets/issues/97)) ([e6e48e9](https://github.com/dream-num/univer-presets/commit/e6e48e90d97d617e6a2b57964471666246d907b7))
* update sdk to 0.9.3 ([4b57f0b](https://github.com/dream-num/univer-presets/commit/4b57f0b42d09ad366c69ddaa347786d610cc1c5b))

## [0.9.2](https://github.com/dream-num/univer-presets/compare/v0.9.1...v0.9.2) (2025-07-11)


### Bug Fixes

* fix redi umd bundle ([#94](https://github.com/dream-num/univer-presets/issues/94)) ([c54cfcf](https://github.com/dream-num/univer-presets/commit/c54cfcfb070008ae5b9890c27e428394f63f821c))


### Features

* update sdk to 0.9.2 ([856525f](https://github.com/dream-num/univer-presets/commit/856525ff685c02335e2d560634a903bc91f804c4))

## [0.9.1](https://github.com/dream-num/univer-presets/compare/v0.9.0...v0.9.1) (2025-07-04)


### Features

* update sdk to 0.9.1 ([ca4d631](https://github.com/dream-num/univer-presets/commit/ca4d631869eee00bfcc9fda73cab28a87e1cdb0e))

# [0.9.0](https://github.com/dream-num/univer-presets/compare/v0.8.3...v0.9.0) (2025-07-04)


### Features

* add @univerjs/preset-docs-node-core ([#90](https://github.com/dream-num/univer-presets/issues/90)) ([7698a53](https://github.com/dream-num/univer-presets/commit/7698a5393318a0eecb7dc8f943d944aaae16e1bc))
* update sdk to 0.9.0 ([4bdcadc](https://github.com/dream-num/univer-presets/commit/4bdcadcf3403e1cb29c02f76c6067c0e55ae80b0))

## [0.8.3](https://github.com/dream-num/univer-presets/compare/v0.8.2...v0.8.3) (2025-06-27)


### Features

* add locale support for Korean(ko-KR) ([#89](https://github.com/dream-num/univer-presets/issues/89)) ([7bd27b1](https://github.com/dream-num/univer-presets/commit/7bd27b1c7663f0c1232ffad7d1e3477dfb94770b))
* **presets:** add export for `@univerjs/themes` ([#88](https://github.com/dream-num/univer-presets/issues/88)) ([dc14ea2](https://github.com/dream-num/univer-presets/commit/dc14ea2fa4225b49da835b31ef956ec21e768cf5))
* update sdk to 0.8.3 ([d58a9ba](https://github.com/dream-num/univer-presets/commit/d58a9bae1a6f8ebe67b2800e59e64e5995b30eab))

## [0.8.2](https://github.com/dream-num/univer-presets/compare/v0.8.1...v0.8.2) (2025-06-20)


### Features

* add '@univerjs/thread-comment' dependency and include in build configuration ([#86](https://github.com/dream-num/univer-presets/issues/86)) ([97f537c](https://github.com/dream-num/univer-presets/commit/97f537cec63e76f5f4a584f5e5295297163d7cd6))
* update sdk to 0.8.2 ([35c50d0](https://github.com/dream-num/univer-presets/commit/35c50d05c51ecfc72db5223f682f6fd6506efdb0))

## [0.8.1](https://github.com/dream-num/univer-presets/compare/v0.8.0...v0.8.1) (2025-06-12)


### Features

* update sdk to 0.8.1 ([a44c978](https://github.com/dream-num/univer-presets/commit/a44c9782ee1fe0490eaf51e2a43b7f3ef503b289))

# [0.8.0](https://github.com/dream-num/univer-presets/compare/v0.8.0-beta.1...v0.8.0) (2025-06-06)


### Bug Fixes

* fix UniverSheetsCorePreset config ([#83](https://github.com/dream-num/univer-presets/issues/83)) ([c4c48c8](https://github.com/dream-num/univer-presets/commit/c4c48c8b56086ac91f1af826a40d70b53834d6a3))


### Features

* add `@univerjs/preset-docs-advanced` ([#79](https://github.com/dream-num/univer-presets/issues/79)) ([c5172ce](https://github.com/dream-num/univer-presets/commit/c5172ce596fee92f0e1671c24b77379a3b78949e))
* add UniverUIPlugin ribbonType config ([#82](https://github.com/dream-num/univer-presets/issues/82)) ([254eaf1](https://github.com/dream-num/univer-presets/commit/254eaf153f451372942b5af57ea3d466c0a9b1e7))
* update sdk to 0.8.0 ([b53a026](https://github.com/dream-num/univer-presets/commit/b53a02633e4849ab72591cb9fc589b82f0822bb4))

# [0.8.0-beta.1](https://github.com/dream-num/univer-presets/compare/v0.8.0-beta.0...v0.8.0-beta.1) (2025-05-29)


### Features

* UniverSheetsCorePreset add config disableForceStringAlert and d… ([#77](https://github.com/dream-num/univer-presets/issues/77)) ([0bb8dd5](https://github.com/dream-num/univer-presets/commit/0bb8dd55fc10921d9cea215ce2d16bdf6ec0c27a))
* update sdk to 0.8.0-beta.1 ([05a153c](https://github.com/dream-num/univer-presets/commit/05a153cb9249d2c212d6bc2313a1e0a06ffd2943))

# [0.8.0-beta.0](https://github.com/dream-num/univer-presets/compare/v0.7.0...v0.8.0-beta.0) (2025-05-26)


### Bug Fixes

* add collaboration option to drawing presets ([e423230](https://github.com/dream-num/univer-presets/commit/e42323015f2e79b7b1f5fd9a77d73565f8ccdcc3))


### Features

* update sdk to 0.8.0-beta.0 ([cef448e](https://github.com/dream-num/univer-presets/commit/cef448e3ae20e93c94300294f6c21a6d1219810c))

# [0.7.0](https://github.com/dream-num/univer-presets/compare/v0.7.0-beta.1...v0.7.0) (2025-
... [TRUNCATED]
```

### File: pnpm-workspace.yaml
```yaml
packages:
    - examples
    - examples-node
    - packages/*
    - common/*

```

### File: turbo.json
```json
{
    "$schema": "https://turbo.build/schema.json",
    "tasks": {
        "build:preset": {
            "cache": false
        },
        "typecheck": {
            "cache": false
        }
    }
}

```

### File: examples\tsconfig.json
```json
{
    "compilerOptions": {
        "target": "ESNext",
        "lib": ["ESNext", "DOM", "DOM.Iterable", "WebWorker"],
        "useDefineForClassFields": true,

        "experimentalDecorators": true,
        "rootDir": "src",
        "module": "ESNext",

        "moduleResolution": "bundler",

        "resolveJsonModule": true,
        "allowImportingTsExtensions": true,

        "strict": true,
        "strictPropertyInitialization": false,
        "noFallthroughCasesInSwitch": true,
        "noImplicitOverride": true,
        "noEmit": true,
        "outDir": "lib/types",
        "isolatedModules": true,
        "skipLibCheck": true
    },
    "include": ["src"]
}

```

### File: scripts\update-dependencies.ts
```ts
/**
 * Dependencies Version Update Script
 *
 * Purpose: Automatically updates the version of all @univerjs and @univerjs-pro
 * related dependencies across all packages.
 *
 * Usage:
 * 1. Basic usage (will use latest version from @univerjs/core latest tag):
 *    pnpm tsx scripts/update-dependencies.ts
 *
 * 2. Specify release channel:
 *    SDK_RELEASE_CHANNEL=nightly pnpm tsx scripts/update-dependencies.ts
 *
 * 3. Specify exact version:
 *    NEW_VERSION=1.0.0 pnpm tsx scripts/update-dependencies.ts
 *
 * Environment Variables:
 * - SDK_RELEASE_CHANNEL: Release channel to use, defaults to 'latest'.
 *                   Can be 'beta', 'alpha', etc.
 * - NEW_VERSION: Target version to update to. If not specified,
 *                will fetch latest version from specified SDK_RELEASE_CHANNEL
 *
 * Notes:
 * - Excluded packages: ${EXCLUDED_PACKAGES}
 * - Excluded versions: ${EXCLUDED_VERSIONS}
 */

import { execSync } from 'node:child_process';
import path from 'node:path';
import process from 'node:process';
import fs from 'fs-extra';

const SDK_RELEASE_CHANNEL = process.env.SDK_RELEASE_CHANNEL || 'latest';
const NEW_VERSION = process.env.NEW_VERSION || getLatestTagVersion('@univerjs/core', SDK_RELEASE_CHANNEL);

if (!NEW_VERSION) {
    console.error('Failed to get version');
    process.exit(1);
}

const EXCLUDED_PACKAGES = ['@univerjs/protocol', '@univerjs/icons'];
const EXCLUDED_VERSIONS = ['workspace:*'];

function getLatestTagVersion(packageName: string, tag: string = 'latest') {
    try {
        const version = execSync(`npm view ${packageName}@${tag} version`, { encoding: 'utf-8' }).trim();
        return version;
    }
    catch (error) {
        console.error(`Failed to get version for ${packageName}@${tag}`);
        throw error;
    }
}

function updateObjVersion(obj: Record<string, string>): string[] {
    const changeLogs: string[] = [];
    Object.entries(obj).forEach(([pkg, version]) => {
        if (
            (pkg.startsWith('@univerjs/') || pkg.startsWith('@univerjs-pro/'))
            && !EXCLUDED_PACKAGES.includes(pkg)
            && !EXCLUDED_VERSIONS.find(rule => version.startsWith(rule))
            && obj[pkg] !== NEW_VERSION
        ) {
            obj[pkg] = NEW_VERSION;
            changeLogs.push(`Updated ${pkg} to ${NEW_VERSION}`);
        }
    });
    return changeLogs;
}

function updateDependency(packageDir: string, dependencyTypes = ['dependencies', 'devDependencies', 'peerDependencies']) {
    const packageJsonPath = path.join(packageDir, 'package.json');

    if (!fs.existsSync(packageJsonPath)) {
        return;
    }

    const packageJson = JSON.parse(fs.readFileSync(packageJsonPath, 'utf8'));
    let hasUpdates = false;

    dependencyTypes.forEach((depType) => {
        if (!packageJson[depType]) {
            return;
        }

        updateObjVersion(packageJson[depType])
            .forEach((log) => {
                console.log(log);
                hasUpdates = true;
            });
    });

    if (hasUpdates) {
        fs.writeJSONSync(packageJsonPath, packageJson, { spaces: 4, EOL: '\n' });
    }
}

const ROOT_DIR = path.resolve(__dirname, '../');
const PACKAGES_DIR = path.resolve(__dirname, '../packages');
function updateDependencies() {
    const packages = fs.readdirSync(PACKAGES_DIR).filter(file =>
        fs.statSync(path.join(PACKAGES_DIR, file)).isDirectory(),
    );
    packages.forEach((packageDir) => {
        updateDependency(path.join(PACKAGES_DIR, packageDir));
    });

    updateDependency(path.join(ROOT_DIR, 'examples'));
    updateDependency(path.join(ROOT_DIR, 'examples-node'));

    console.log('Running pnpm install to update lock file...');
    execSync('pnpm install --no-frozen-lockfile', { stdio: 'inherit' });

    console.log('Dependencies update completed!');
}

updateDependencies();

```

### File: common\shared\vite\auto-detected-external-plugin.ts
```ts
import type { Plugin } from 'vite';
import { convertLibNameFromPackageName } from './utils';

const peerDepsMap = {
    'react': {
        global: 'React',
        name: 'react',
        version: '>=16.9.0 || >=17 || >=18 || >=19',
    },
    'react/jsx-runtime': {
        global: 'React',
        name: 'react',
        version: 'react',
    },
    'react-dom': {
        global: 'ReactDOM',
        name: 'react-dom',
        version: '>=16.9.0 || >=17 || >=18 || >=19',
    },
    'react-dom/client': {
        global: 'ReactDOM',
        name: 'react-dom',
        version: 'react-dom',
    },
    'rxjs': {
        global: 'rxjs',
        name: 'rxjs',
        version: '>=7.0.0',
    },
    'rxjs/operators': {
        global: 'rxjs.operators',
        name: 'rxjs',
        version: 'rxjs',
    },
    '@wendellhu/redi': {
        global: '@wendellhu/redi',
        name: '@wendellhu/redi',
        version: '0.19.2',
    },
    '@wendellhu/redi/react-bindings': {
        global: '@wendellhu/redi/react-bindings',
        name: '@wendellhu/redi',
        version: '@wendellhu/redi',
    },
    'vue': {
        global: 'Vue',
        name: 'vue',
        version: '>=3.0.0',
        optional: true,
    },
};

export function autoDetectedExternalPlugin(): Plugin {
    const globals = {};
    let hasCss = false;

    return {
        name: 'auto-detected-external',
        enforce: 'pre',
        apply: 'build',

        resolveId(source) {
            if (source.endsWith('.css')) {
                hasCss = true;
                return null;
            }

            if (source in peerDepsMap) {
                globals[source] = peerDepsMap[source].global;

                return { id: source, external: true };
            }
            else if (source.startsWith('@univerjs')) {
                if (source === '@univerjs/icons') {
                    return null;
                }
                if (source === '@univerjs/protocol') {
                    return null;
                }

                globals[source] = convertLibNameFromPackageName(source);

                return { id: source, external: true };
            }

            return null;
        },

        outputOptions(opts) {
            opts.globals = globals;

            if (hasCss) {
                opts.assetFileNames = 'index.css';
            }

            return opts;
        },
    };
};

```

### File: common\shared\vite\index.ts
```ts
import type { InlineConfig } from 'vite';
import path from 'node:path';
import process from 'node:process';
import fs from 'fs-extra';
import { mergeConfig, build as viteBuild } from 'vite';
import dts from 'vite-plugin-dts';
import vitePluginExternal from 'vite-plugin-external';

import { autoDetectedExternalPlugin } from './auto-detected-external-plugin';
import prependUMDRaw from './prepend-umd-raw';

import { convertLibNameFromPackageName } from './utils';

type BuildMode = 'bootstrap';

interface IBuildExecuterOptions {
    pkg: Record<string, any>;
    entry: Record<string, string>;
    umdDeps: string[];
    umdAdditionalFiles: string[];
}

const clone = (data: any) => JSON.parse(JSON.stringify(data));

function getSharedConfig(): InlineConfig {
    const sharedConfig: InlineConfig = {
        configFile: false,
        build: {
            target: 'chrome70',
        },
        define: {
            'process.env.NODE_ENV': JSON.stringify('production'),
            'process.env.BUILD_TIMESTAMP': JSON.stringify(Math.floor(Date.now() / 1000)),
        },
        css: {
            modules: {
                localsConvention: 'camelCaseOnly',
                generateScopedName: 'univer-[local]',
            },
        },
        plugins: [
            autoDetectedExternalPlugin(),
            vitePluginExternal({
                nodeBuiltins: true,
            }),
        ],
    };
    return sharedConfig;
}

async function buildESM(sharedConfig: InlineConfig, options: IBuildExecuterOptions) {
    const { entry } = options;

    await Promise.all(Object.keys(entry).map((key) => {
        const config: InlineConfig = mergeConfig(sharedConfig, {
            build: {
                emptyOutDir: false,
                outDir: 'lib',
                lib: {
                    entry: {
                        [key]: entry[key],
                    },
                    fileName: () => `es/${key}.js`,
                    formats: ['es'],
                },
                rollupOptions: {
                    output: {
                        inlineDynamicImports: true,
                    },
                },
            },
            plugins: [
                key === 'index'
                    ? dts({
                            entryRoot: 'src',
                            outDir: 'lib/types',
                            clearPureImport: false,
                        })
                    : null,
            ],
        });

        return viteBuild(config);
    }));

    const __dirname = process.cwd();
    const libDir = path.resolve(__dirname, 'lib');
    const esmDir = path.resolve(__dirname, 'lib/es');

    fs.copySync(esmDir, libDir);
}

async function buildCJS(sharedConfig: InlineConfig, options: IBuildExecuterOptions) {
    const { entry } = options;

    return Promise.all(Object.keys(entry).map((key) => {
        const config: InlineConfig = mergeConfig(sharedConfig, {
            build: {
                emptyOutDir: false,
                outDir: 'lib',
                lib: {
                    entry: {
                        [key]: entry[key],
                    },
                    fileName: () => `cjs/${key}.js`,
                    formats: ['cjs'],
                },
            },
        });

        return viteBuild(config);
    }));
}

async function buildUMD(sharedConfig: InlineConfig, options: IBuildExecuterOptions) {
    const { pkg, entry, umdDeps, umdAdditionalFiles } = options;

    const __dirname = process.cwd();
    entry.index = path.resolve(__dirname, 'src/umd.ts');

    await Promise.all(Object.keys(entry).map((key) => {
        let name = convertLibNameFromPackageName(pkg.name);

        if (key.includes('locales')) {
            const localeKey = key.split('/')[1];
            name = `${name}${convertLibNameFromPackageName(localeKey)}`;
        }

        const config: InlineConfig = mergeConfig(sharedConfig, {
            build: {
                emptyOutDir: false,
                outDir: 'lib',
                lib: {
                    entry: {
                        [key]: entry[key],
                    },
                    name,
                    fileName: () => `umd/${key}.js`,
                    formats: ['umd'],
                },
            },
        });

        return viteBuild(config);
    }));

    prependUMDRaw({
        umdDeps,
        umdAdditionalFiles,
    });

    return Promise.resolve();
}

interface IBuildOptions {
    mode?: BuildMode;
    umdDeps?: string[];
    umdAdditionalFiles?: string[];
}

export async function build(options?: IBuildOptions) {
    const { mode, umdDeps = [], umdAdditionalFiles = [] } = options ?? {};

    const __dirname = process.cwd();

    const pkg = fs.readJsonSync(path.resolve(__dirname, 'package.json'));

    const entry: Record<string, string> = {
        index: path.resolve(__dirname, 'src/index.ts'),
    };

    const hasLocales = fs.existsSync(path.resolve(__dirname, 'src/locales'));
    if (hasLocales) {
        const locales = fs.readdirSync(path.resolve(__dirname, 'src/locales'));
        for (const file of locales) {
            if (fs.statSync(path.resolve(__dirname, 'src/locales', file)).isDirectory() || !file.includes('-')) {
                continue;
            }
            const localeValue = file.replace('.ts', '');
            entry[`locales/${localeValue}`] = path.resolve(__dirname, 'src/locales', file);
        }
    }

    const hasWorker = fs.existsSync(path.resolve(__dirname, 'src/worker.ts'));
    if (hasWorker) {
        entry.worker = path.resolve(__dirname, 'src/worker.ts');
    }

    const buildExecuterOptions: IBuildExecuterOptions = {
        pkg,
        entry,
        umdDeps,
        umdAdditionalFiles,
    };

    buildUMD(getSharedConfig(), clone(buildExecuterOptions));

    if (mode === 'bootstrap') {
        const presets = fs.readdirSync(path.resolve(__dirname, 'src')).filter(dir => dir.startsWith('preset-'));

        for (const preset of presets) {
            const __presetDir = path.resolve(__dirname, 'src', preset);
            entry[`${preset}/index`] = path.resolve(__presetDir, 'index.ts');

            const locales = fs.readdirSync(path.resolve(__presetDir, 'locales'));
            for (const file of locales) {
                const localeValue = file.replace('.ts', '');
                entry[`${preset}/locales/${localeValue}`] = path.resolve(__presetDir, 'locales', file);
            }

            if (fs.existsSync(path.resolve(__presetDir, 'worker.ts'))) {
                entry[`${preset}/worker`] = path.resolve(__presetDir, 'worker.ts');
            }

            const __cssFile = path.resolve(__dirname, 'node_modules', `@univerjs/${preset}`, 'lib/index.css');
            const __cssOutputDir = path.resolve(__dirname, 'lib', 'styles');
            fs.ensureDirSync(__cssOutputDir);
            if (fs.existsSync(__cssFile)) {
                fs.copyFileSync(__cssFile, path.resolve(__cssOutputDir, `${preset}.css`));
            }
        }
    }

    buildESM(getSharedConfig(), clone(buildExecuterOptions));
    buildCJS(getSharedConfig(), clone(buildExecuterOptions));
}

```

### File: common\shared\vite\prepend-umd-raw.ts
```ts
import path from 'node:path';
import process from 'node:process';
import fs from 'fs-extra';

const LOCLAES_MAP = [
    'en-US',
    'fa-IR',
    'fr-FR',
    'ja-JP',
    'ko-KR',
    'ru-RU',
    'vi-VN',
    'zh-CN',
    'zh-TW',
    'es-ES',
    'ca-ES',
    'sk-SK',
];

interface IOptions {
    umdDeps: string[];
    umdAdditionalFiles: string[];
}

export default function prependUMDRaw(options: IOptions) {
    const { umdDeps, umdAdditionalFiles } = options;

    const __nodeModules = path.resolve(process.cwd(), 'node_modules');
    const __umd = path.resolve(process.cwd(), 'lib/umd/index.js');

    const umdContentsMap: Map<string, string> = new Map();

    umdAdditionalFiles.forEach((file) => {
        const content = `// ${file}\n${fs.readFileSync(file, 'utf8')}`;
        umdContentsMap.set(file, content);
    });

    umdDeps.forEach((dep) => {
        const __dep = path.resolve(__nodeModules, dep);
        const __depIndex = path.resolve(__dep, 'lib/umd/index.js');
        const __depFacade = path.resolve(__dep, 'lib/umd/facade.js');

        const key = `${dep}/index`;
        const content = `// ${key}\n${fs.readFileSync(__depIndex, 'utf8')}`;
        if (!umdContentsMap.has(key)) {
            umdContentsMap.set(key, content);
        }

        if (fs.existsSync(__depFacade)) {
            const key = `${dep}/facade`;
            const content = `// ${key}\n${fs.readFileSync(__depFacade, 'utf8')}`;
            if (!umdContentsMap.has(key)) {
                umdContentsMap.set(key, content);
            }
        }
    });

    if (fs.existsSync(__umd)) {
        const key = 'index';
        const content = `// ${key}\n${fs.readFileSync(__umd, 'utf8')}`;
        if (!umdContentsMap.has(key)) {
            umdContentsMap.set(key, content);
        }
    }

    const umdContents = Array.from(umdContentsMap.values()).join('\n\n');
    fs.writeFileSync(__umd, umdContents);

    const __localeDir = path.resolve(process.cwd(), 'lib/umd/locales');

    LOCLAES_MAP.forEach((localeKey) => {
        const localeContentsMap: Map<string, string> = new Map();

        umdDeps.forEach((dep) => {
            const __dep = path.resolve(__nodeModules, dep);
            const __depLocale = path.resolve(__dep, 'lib/umd/locale', `${localeKey}.js`);

            if (fs.existsSync(__depLocale)) {
                const key = `${dep}/locale/${localeKey}`;
                const content = `// ${key}\n${fs.readFileSync(__depLocale, 'utf8')}`;
                if (!localeContentsMap.has(key)) {
                    localeContentsMap.set(key, content);
                }
            }
        });

        const __locale = path.resolve(__localeDir, `${localeKey}.js`);

        if (fs.existsSync(__locale)) {
            const key = `locale/${localeKey}`;
            const content = `// ${key}\n${fs.readFileSync(__locale, 'utf8')}`;

            if (!localeContentsMap.has(key)) {
                localeContentsMap.set(key, content);
            }

            const localeContents = Array.from(localeContentsMap.values()).join('\n\n');
            fs.writeFileSync(__locale, localeContents);
        }
    });
}

```

### File: common\shared\vite\utils.ts
```ts
export function convertLibNameFromPackageName(name: string) {
    return name
        .replace(/^@(univerjs(?:-pro)?)\//, (_, matchedPrefix) => {
            return matchedPrefix === 'univerjs-pro' ? 'univer-pro-' : 'univer-';
        })
        .replace('/lib', '')
        .replace('/locale/', '-')
        .replace('/facade', '-facade')
        .split('-')
        .map(word => word.charAt(0).toUpperCase() + word.slice(1))
        .join('');
};

```


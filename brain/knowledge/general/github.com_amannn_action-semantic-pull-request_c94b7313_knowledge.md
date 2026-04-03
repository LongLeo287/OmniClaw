---
id: github.com-amannn-action-semantic-pull-request-c94
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:30.126739
---

# KNOWLEDGE EXTRACT: github.com_amannn_action-semantic-pull-request_c94b7313
> **Extracted on:** 2026-04-01 11:09:35
> **Source:** D:/LongLeo/AI OS CORP/AI OS/core/security/QUARANTINE/KI-BATCH-20260331205007521270/github.com_amannn_action-semantic-pull-request_c94b7313

---

## File: `.gitignore`
```
node_modules
```

## File: `.releaserc.json`
```json
{
  "preset": "conventionalcommits",
  "branches": ["main"],
  "plugins": [
    "@semantic-release/commit-analyzer",
    "@semantic-release/release-notes-generator",
    ["@semantic-release/changelog", {"changelogTitle": "# Changelog"}],
    "semantic-release-major-tag",
    [
      "@semantic-release/github",
      {
        "failComment": false,
        "failTitle": false,
        "releasedLabels": false
      }
    ],
    [
      "@semantic-release/git",
      {
        "assets": ["dist", "CHANGELOG.md"],
        "message": "chore: Release ${nextRelease.version} [skip ci]"
      }
    ]
  ]
}
```

## File: `CHANGELOG.md`
```markdown
# Changelog

## [6.1.1](https://github.com/amannn/action-semantic-pull-request/compare/v6.1.0...v6.1.1) (2025-08-22)

### Bug Fixes

* Parse `headerPatternCorrespondence` properly ([#295](https://github.com/amannn/action-semantic-pull-request/issues/295)) ([800da4c](https://github.com/amannn/action-semantic-pull-request/commit/800da4c97f618e44f972ff9bc21ab5daecc97773))

## [6.1.0](https://github.com/amannn/action-semantic-pull-request/compare/v6.0.1...v6.1.0) (2025-08-19)

### Features

* Support providing regexps for types ([#292](https://github.com/amannn/action-semantic-pull-request/issues/292)) ([a30288b](https://github.com/amannn/action-semantic-pull-request/commit/a30288bf13b78cca17c3abdc144db5977476fc8b))

### Bug Fixes

* Remove trailing whitespace from "unknown release type" error message ([#291](https://github.com/amannn/action-semantic-pull-request/issues/291)) ([afa4edb](https://github.com/amannn/action-semantic-pull-request/commit/afa4edb1c465fb22230da8ff4776a163ab5facdf))

## [6.0.1](https://github.com/amannn/action-semantic-pull-request/compare/v6.0.0...v6.0.1) (2025-08-13)

### Bug Fixes

* Actually execute action ([#289](https://github.com/amannn/action-semantic-pull-request/issues/289)) ([58e4ab4](https://github.com/amannn/action-semantic-pull-request/commit/58e4ab40f59be79f2c432bf003e34a31174e977a))

## [6.0.0](https://github.com/amannn/action-semantic-pull-request/compare/v5.5.3...v6.0.0) (2025-08-13)

### ⚠ BREAKING CHANGES

* Upgrade action to use Node.js 24 and ESM (#287)

### Features

* Upgrade action to use Node.js 24 and ESM ([#287](https://github.com/amannn/action-semantic-pull-request/issues/287)) ([bc0c9a7](https://github.com/amannn/action-semantic-pull-request/commit/bc0c9a79abfe07c0f08c498dd4a040bd22fe9b79))

## [5.5.3](https://github.com/amannn/action-semantic-pull-request/compare/v5.5.2...v5.5.3) (2024-06-28)


### Bug Fixes

* Bump `braces` dependency ([#269](https://github.com/amannn/action-semantic-pull-request/issues/269). by @EelcoLos) ([2d952a1](https://github.com/amannn/action-semantic-pull-request/commit/2d952a1bf90a6a7ab8f0293dc86f5fdf9acb1915))

## [5.5.2](https://github.com/amannn/action-semantic-pull-request/compare/v5.5.1...v5.5.2) (2024-04-24)


### Bug Fixes

* Bump tar from 6.1.11 to 6.2.1 ([#262](https://github.com/amannn/action-semantic-pull-request/issues/262) by @EelcoLos) ([9a90d5a](https://github.com/amannn/action-semantic-pull-request/commit/9a90d5a5ac979326e3bb9272750cdd4f192ce24a))

## [5.5.1](https://github.com/amannn/action-semantic-pull-request/compare/v5.5.0...v5.5.1) (2024-04-24)


### Bug Fixes

* Bump ip from 2.0.0 to 2.0.1 ([#263](https://github.com/amannn/action-semantic-pull-request/issues/263) by @EelcoLos) ([5e7e9ac](https://github.com/amannn/action-semantic-pull-request/commit/5e7e9acca3ddc6a9d7b640fe1f905c4fff131f4a))

## [5.5.0](https://github.com/amannn/action-semantic-pull-request/compare/v5.4.0...v5.5.0) (2024-04-23)


### Features

* Add outputs for `type`, `scope` and `subject` ([#261](https://github.com/amannn/action-semantic-pull-request/issues/261) by [@bcaurel](https://github.com/bcaurel)) ([b05f5f6](https://github.com/amannn/action-semantic-pull-request/commit/b05f5f6423ef5cdfc7fdff00c4c10dd9a4f54aff))

## [5.4.0](https://github.com/amannn/action-semantic-pull-request/compare/v5.3.0...v5.4.0) (2023-11-03)


### Features

* Use `github.api_url` as default for `githubBaseUrl` ([#243](https://github.com/amannn/action-semantic-pull-request/issues/243) by [@fty4](https://github.com/fty4)) ([4d5734a](https://github.com/amannn/action-semantic-pull-request/commit/4d5734a0a29e548daecc9e7bfeb9bb8b3acdee1e))

## [5.3.0](https://github.com/amannn/action-semantic-pull-request/compare/v5.2.0...v5.3.0) (2023-09-25)


### Features

* Use Node.js 20 in action ([#240](https://github.com/amannn/action-semantic-pull-request/issues/240)) ([4c0d5a2](https://github.com/amannn/action-semantic-pull-request/commit/4c0d5a21fc86635c67cc57ffe89d842c34ade284))

## [5.2.0](https://github.com/amannn/action-semantic-pull-request/compare/v5.1.0...v5.2.0) (2023-03-16)


### Features

* Update dependencies by @EelcoLos ([#229](https://github.com/amannn/action-semantic-pull-request/issues/229)) ([e797448](https://github.com/amannn/action-semantic-pull-request/commit/e797448a07516738bcfdd6f26ad1d1f84c58d0cc))

## [5.1.0](https://github.com/amannn/action-semantic-pull-request/compare/v5.0.2...v5.1.0) (2023-02-10)


### Features

* Add regex support to `scope` and `disallowScopes` configuration ([#226](https://github.com/amannn/action-semantic-pull-request/issues/226)) ([403a6f8](https://github.com/amannn/action-semantic-pull-request/commit/403a6f89242a0d0d3acde94e6141b2e0f4da8838))

### [5.0.2](https://github.com/amannn/action-semantic-pull-request/compare/v5.0.1...v5.0.2) (2022-10-17)


### Bug Fixes

* Upgrade `@actions/core` to avoid deprecation warnings ([#208](https://github.com/amannn/action-semantic-pull-request/issues/208)) ([91f4126](https://github.com/amannn/action-semantic-pull-request/commit/91f4126c9e8625b9cadd64b02a03018fa22fc498))

### [5.0.1](https://github.com/amannn/action-semantic-pull-request/compare/v5.0.0...v5.0.1) (2022-10-14)


### Bug Fixes

* Upgrade GitHub Action to use Node v16 ([#207](https://github.com/amannn/action-semantic-pull-request/issues/207)) ([6282ee3](https://github.com/amannn/action-semantic-pull-request/commit/6282ee339b067cb8eab05026f91153f873ad37fb))

## [5.0.0](https://github.com/amannn/action-semantic-pull-request/compare/v4.6.0...v5.0.0) (2022-10-11)


### ⚠ BREAKING CHANGES

* Enum options need to be newline delimited (to allow whitespace within them) (#205)

### Features

* Enum options need to be newline delimited (to allow whitespace within them) ([#205](https://github.com/amannn/action-semantic-pull-request/issues/205)) ([c906fe1](https://github.com/amannn/action-semantic-pull-request/commit/c906fe1e5a4bcc61624931ca94da9672107bd448))

## [4.6.0](https://github.com/amannn/action-semantic-pull-request/compare/v4.5.0...v4.6.0) (2022-09-26)


### Features

* Provide error messages as `outputs.error_message` ([#194](https://github.com/amannn/action-semantic-pull-request/issues/194)) ([880a3c0](https://github.com/amannn/action-semantic-pull-request/commit/880a3c061c0dea01e977cefe26fb0e0d06b3d1a9))

## [4.5.0](https://github.com/amannn/action-semantic-pull-request/compare/v4.4.0...v4.5.0) (2022-05-04)


### Features

* Add `disallowScopes` option ([#179](https://github.com/amannn/action-semantic-pull-request/issues/179)) ([6a7ed2d](https://github.com/amannn/action-semantic-pull-request/commit/6a7ed2d5046cf8a40c60494c83c962343061874a))

## [4.4.0](https://github.com/amannn/action-semantic-pull-request/compare/v4.3.0...v4.4.0) (2022-04-22)


### Features

* Add options to pass custom regex to conventional-commits-parser ([#177](https://github.com/amannn/action-semantic-pull-request/issues/177)) ([956659a](https://github.com/amannn/action-semantic-pull-request/commit/956659ae00eaa0b00fe5a58dfdf3a3db1efd1d63))

## [4.3.0](https://github.com/amannn/action-semantic-pull-request/compare/v4.2.0...v4.3.0) (2022-04-13)


### Features

* Add `ignoreLabels` option to opt-out of validation for certain PRs ([#174](https://github.com/amannn/action-semantic-pull-request/issues/174)) ([277c230](https://github.com/amannn/action-semantic-pull-request/commit/277c2303f965680aed7613eb512365c58aa92b6b))

## [4.2.0](https://github.com/amannn/action-semantic-pull-request/compare/v4.1.0...v4.2.0) (2022-02-08)


### Features

* Add opt-in validation that PR titles match a single commit ([#160](https://github.com/amannn/action-semantic-pull-request/issues/160)) ([c05e358](https://github.com/amannn/action-semantic-pull-request/commit/c05e3587cb7878ec080300180d31d61ba1cf01ea))

## [4.1.0](https://github.com/amannn/action-semantic-pull-request/compare/v4.0.1...v4.1.0) (2022-02-04)


### Features

* Check if the PR title matches the commit title when single commits are validated to avoid surprises ([#158](https://github.com/amannn/action-semantic-pull-request/issues/158)) ([f1216e9](https://github.com/amannn/action-semantic-pull-request/commit/f1216e9607ae4b476a6584a899c39bbb4f62da6d))

### [4.0.1](https://github.com/amannn/action-semantic-pull-request/compare/v4.0.0...v4.0.1) (2022-02-03)


### Bug Fixes

* Upgrade dependencies ([#156](https://github.com/amannn/action-semantic-pull-request/issues/156)) ([16c6cc6](https://github.com/amannn/action-semantic-pull-request/commit/16c6cc670bd7e91dbcfd9c39de6e6436d2c0fe1b))

## [4.0.0](https://github.com/amannn/action-semantic-pull-request/compare/v3.7.0...v4.0.0) (2022-02-02)


### ⚠ BREAKING CHANGES

* dropped support for node <=15

### Features

* Upgrade semantic-release@19.0.2 ([#155](https://github.com/amannn/action-semantic-pull-request/issues/155)) ([ca264e0](https://github.com/amannn/action-semantic-pull-request/commit/ca264e08ba87f01cd802533512d9787d07a5ba98))

## [3.7.0](https://github.com/amannn/action-semantic-pull-request/compare/v3.6.0...v3.7.0) (2022-02-02)


### Features

* Upgrade @actions/github ([#154](https://github.com/amannn/action-semantic-pull-request/issues/154)) ([c85a868](https://github.com/amannn/action-semantic-pull-request/commit/c85a868a5178060d1a5abcea37546d403b923e6c))

## [3.6.0](https://github.com/amannn/action-semantic-pull-request/compare/v3.5.0...v3.6.0) (2022-01-05)


### Features

* Publish major version tag ([c47e831](https://github.com/amannn/action-semantic-pull-request/commit/c47e8318667a1e17cbe7132cea17eaf5d06cc403))

## [3.5.0](https://github.com/amannn/action-semantic-pull-request/compare/v3.4.6...v3.5.0) (2021-12-15)


### Features

* Add support for Github Enterprise ([#145](https://github.com/amannn/action-semantic-pull-request/issues/145)) ([579fb11](https://github.com/amannn/action-semantic-pull-request/commit/579fb115c050f156ee6d52244a7ff41b685a89fd))

### [3.4.6](https://github.com/amannn/action-semantic-pull-request/compare/v3.4.5...v3.4.6) (2021-10-31)


### Bug Fixes

* Better strategy to detect merge commits ([#132](https://github.com/amannn/action-semantic-pull-request/issues/132)) ([f913d37](https://github.com/amannn/action-semantic-pull-request/commit/f913d374b7bc698a5831a12c8955d1373c439548))

### [3.4.5](https://github.com/amannn/action-semantic-pull-request/compare/v3.4.4...v3.4.5) (2021-10-28)


### Bug Fixes

* Consider merge commits for single commit validation ([#131](https://github.com/amannn/action-semantic-pull-request/issues/131)) ([5265383](https://github.com/amannn/action-semantic-pull-request/commit/526538350f2e4eaaac841e586a197de6b019af1f)), closes [#108](https://github.com/amannn/action-semantic-pull-request/issues/108)

### [3.4.4](https://github.com/amannn/action-semantic-pull-request/compare/v3.4.3...v3.4.4) (2021-10-26)


### Reverts

* Revert "fix: Consider merge commits for single commit validation (#127)" ([d40b0d4](https://github.com/amannn/action-semantic-pull-request/commit/d40b0d425a054807cc5e032a827cc5780f507630)), closes [#127](https://github.com/amannn/action-semantic-pull-request/issues/127)

### [3.4.3](https://github.com/amannn/action-semantic-pull-request/compare/v3.4.2...v3.4.3) (2021-10-26)


### Bug Fixes

* Consider merge commits for single commit validation ([#127](https://github.com/amannn/action-semantic-pull-request/issues/127)) ([1b347f7](https://github.com/amannn/action-semantic-pull-request/commit/1b347f79d6518f5d0190913abf7815286f490f53)), closes [#108](https://github.com/amannn/action-semantic-pull-request/issues/108) [#108](https://github.com/amannn/action-semantic-pull-request/issues/108)

### [3.4.2](https://github.com/amannn/action-semantic-pull-request/compare/v3.4.1...v3.4.2) (2021-08-16)


### Bug Fixes

* Don't require `scopes` when `requireScope` enabled ([#114](https://github.com/amannn/action-semantic-pull-request/issues/114)) ([4c0fe2f](https://github.com/amannn/action-semantic-pull-request/commit/4c0fe2f50d26390ef6a2553a01d9bd13bef2caf2))

### [3.4.1](https://github.com/amannn/action-semantic-pull-request/compare/v3.4.0...v3.4.1) (2021-07-26)


### Bug Fixes

* Make link in error message clickable ([#112](https://github.com/amannn/action-semantic-pull-request/issues/112)) ([2a292a6](https://github.com/amannn/action-semantic-pull-request/commit/2a292a6550224ddc9d79731bcd15732b42344ebf))

## [3.4.0](https://github.com/amannn/action-semantic-pull-request/compare/v3.3.0...v3.4.0) (2021-02-15)


### Features

* Add `validateSingleCommit` flag to validate the commit message if there's only a single commit in the PR (opt-in). This is intended to be used as a workaround for an issue with Github as in this case, the PR title won't be used as the default commit message when merging a PR. ([#87](https://github.com/amannn/action-semantic-pull-request/issues/87)) ([3f20459](https://github.com/amannn/action-semantic-pull-request/commit/3f20459aa1121f2f0093f06f565a95fe7c5cf402))

## [3.3.0](https://github.com/amannn/action-semantic-pull-request/compare/v3.2.6...v3.3.0) (2021-02-10)


### Features

* Add ability to use multiple scopes ([#85](https://github.com/amannn/action-semantic-pull-request/issues/85)) ([d6aabb6](https://github.com/amannn/action-semantic-pull-request/commit/d6aabb6fedc5f57cec60b16db8595a92f1e263ab))

### [3.2.6](https://github.com/amannn/action-semantic-pull-request/compare/v3.2.5...v3.2.6) (2021-01-25)


### Bug Fixes

* Publish changelog ([47ac28b](https://github.com/amannn/action-semantic-pull-request/commit/47ac28b008b9b34b6cda0c1d558f4b8f25a0d3bb))

### [3.2.1](https://github.com/amannn/action-semantic-pull-request/compare/v3.2.0...v3.2.1) (2021-01-19)


### Bug Fixes

* Move configuration docs to a separate section ([dd78147](https://github.com/amannn/action-semantic-pull-request/commit/dd78147b453899371b7406672fb5ebe9dc5e2c5f))

## [3.2.0](https://github.com/amannn/action-semantic-pull-request/compare/v3.1.0...v3.2.0) (2021-01-18)


### Features

* Add `subjectPatternError` option to allow users to override the default error when `subjectPattern` doesn't match ([#76](https://github.com/amannn/action-semantic-pull-request/issues/76)) ([e617d81](https://github.com/amannn/action-semantic-pull-request/commit/e617d811330c87d229d4d7c9a91517f6197869a2))

## [3.1.0](https://github.com/amannn/action-semantic-pull-request/compare/v3.0.0...v3.1.0) (2021-01-11)


### Features

* Add regex validation for subject ([#71](https://github.com/amannn/action-semantic-pull-request/issues/71)) ([04b071e](https://github.com/amannn/action-semantic-pull-request/commit/04b071e606842fe1c6b50fcbc0cab856c7d1cb49))

## [3.0.0](https://github.com/amannn/action-semantic-pull-request/compare/v2.2.0...v3.0.0) (2021-01-08)


### ⚠ BREAKING CHANGES

* Add opt-in for WIP (#73)

### Features

* Add opt-in for WIP ([#73](https://github.com/amannn/action-semantic-pull-request/issues/73)) ([fb077fa](https://github.com/amannn/action-semantic-pull-request/commit/fb077fa571d6e14bc0ba9bc5b971e741ac693399))

## [2.2.0](https://github.com/amannn/action-semantic-pull-request/compare/v2.1.1...v2.2.0) (2020-12-21)


### Features

* Add ability to constrain scopes ([#66](https://github.com/amannn/action-semantic-pull-request/issues/66)) ([95b7031](https://github.com/amannn/action-semantic-pull-request/commit/95b703180f65c7da62280f216fb2a6fcc176dd26))

### [2.1.1](https://github.com/amannn/action-semantic-pull-request/compare/v2.1.0...v2.1.1) (2020-12-03)


### Bug Fixes

* Get rid of deprecation notice ([#63](https://github.com/amannn/action-semantic-pull-request/issues/63)) ([ec157ab](https://github.com/amannn/action-semantic-pull-request/commit/ec157abe0cb1f9c0ec79c022db8a5e6245f53df8))

## [2.1.0](https://github.com/amannn/action-semantic-pull-request/compare/v2.0.0...v2.1.0) (2020-10-21)


### Features

* Allow configuration for custom types ([@alorma](https://github.com/alorma), [@mrchief](https://github.com/mrchief) and [@amannn](https://github.com/amannn) in [#53](https://github.com/amannn/action-semantic-pull-request/issues/53)) ([2fe39e2](https://github.com/amannn/action-semantic-pull-request/commit/2fe39e2ce8ed0337bff045b6b6457e685d0dd51f))

## [2.0.0](https://github.com/amannn/action-semantic-pull-request/compare/v1.2.10...v2.0.0) (2020-09-17)


### ⚠ BREAKING CHANGES

* Remove support for `improvement` prefix (as per commitizen/conventional-commit-types#16).

### Miscellaneous Chores

* Update dependencies. ([b9bc3f1](https://github.com/amannn/action-semantic-pull-request/commit/b9bc3f12d1e30b03273a4077cb7936b091fb1ba2))

### [1.2.10](https://github.com/amannn/action-semantic-pull-request/compare/v1.2.9...v1.2.10) (2020-09-17)


### ⚠ BREAKING CHANGES

* Remove support for `improvement` prefix (as per https://github.com/commitizen/conventional-commit-types/pull/16).

### Miscellaneous Chores

* Update dependencies ([#31](https://github.com/amannn/action-semantic-pull-request/issues/31)) ([2aa2eb7](https://github.com/amannn/action-semantic-pull-request/commit/2aa2eb7e08ff8a6d0eaf3d42df0efec1cdeb1984))

### [1.2.9](https://github.com/amannn/action-semantic-pull-request/compare/v1.2.8...v1.2.9) (2020-09-17)


### Bug Fixes

* Improve reporting for failed checks ([#30](https://github.com/amannn/action-semantic-pull-request/issues/30)) ([1aa9e17](https://github.com/amannn/action-semantic-pull-request/commit/1aa9e172840b7e07c0751e80aa03271b80d27ebe))

### [1.2.8](https://github.com/amannn/action-semantic-pull-request/compare/v1.2.7...v1.2.8) (2020-08-23)

### [1.2.7](https://github.com/amannn/action-semantic-pull-request/compare/v1.2.6...v1.2.7) (2020-08-22)


### Bug Fixes

* update workflow to use pull_request_target ([#25](https://github.com/amannn/action-semantic-pull-request/issues/25)) ([73f02a4](https://github.com/amannn/action-semantic-pull-request/commit/73f02a44b31b2c716caf45cc18e5e12d405ae225)), closes [#24](https://github.com/amannn/action-semantic-pull-request/issues/24)

### [1.2.6](https://github.com/amannn/action-semantic-pull-request/compare/v1.2.5...v1.2.6) (2020-08-14)

### [1.2.5](https://github.com/amannn/action-semantic-pull-request/compare/v1.2.4...v1.2.5) (2020-08-14)

### [1.2.4](https://github.com/amannn/action-semantic-pull-request/compare/v1.2.3...v1.2.4) (2020-08-14)

### [1.2.3](https://github.com/amannn/action-semantic-pull-request/compare/v1.2.2...v1.2.3) (2020-08-14)

### [1.2.2](https://github.com/amannn/action-semantic-pull-request/compare/v1.2.1...v1.2.2) (2020-06-15)


### Bug Fixes

* Bump npm from 6.13.0 to 6.14.5 ([#8](https://github.com/amannn/action-semantic-pull-request/issues/8)) ([9779e20](https://github.com/amannn/action-semantic-pull-request/commit/9779e20f1998f8b97180af283e8f4b29f120d44f))

### [1.2.1](https://github.com/amannn/action-semantic-pull-request/compare/v1.2.0...v1.2.1) (2020-05-13)

## [1.2.0](https://github.com/amannn/action-semantic-pull-request/compare/v1.1.1...v1.2.0) (2019-11-20)


### Features

* Add [WIP] support.  ([#3](https://github.com/amannn/action-semantic-pull-request/issues/3)) ([2b4d25e](https://github.com/amannn/action-semantic-pull-request/commit/2b4d25ed4b55efc389f5e5898b061615ae96a1da))

### 1.1.1 First usable release
```

## File: `CONTRIBUTORS.md`
```markdown
# Contributors

Thank you very much for contributing to this project!

Due to the way event triggers work with GitHub actions it's a bit harder to test your changes.

Simple changes that can be unit tested can be implemented with the regular workflow where you fork the repo and create a pull request. Note however that the new version of the action won't be executed in the workflows of this repository. We have to rely on the unit tests in this case.

If e.g. environment parameters are changed, the action should be tested end-to-end in a workflow.

To do this, please follow this process:

1. Fork the repo.
2. Create a PR in **your own repo**.
3. The "Lint PR title preview (current branch)" workflow will run the new version and will help you validate the change.
4. Create a PR to this repo with the changes. In this case the preview workflow will fail, but we'll know that it works since you've tested it in the fork. Please include a include a link to a workflow where you've tested the current state of this pull request.
5. Don't run `npm run build` to update the `dist` folder as it will be generated on CI during the build
```

## File: `LICENSE`
```
MIT License

Copyright (c) 2020 Contributors

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

## File: `README.md`
```markdown
# action-semantic-pull-request

This is a GitHub Action that ensures that your pull request titles match the [Conventional Commits spec](https://www.conventionalcommits.org/). Typically, this is used in combination with a tool like [semantic-release](https://github.com/semantic-release/semantic-release) to automate releases.

Used by: [Electron](https://github.com/electron/electron) · [Vite](https://github.com/vitejs/vite) · [Excalidraw](https://github.com/excalidraw/excalidraw) · [Apache](https://github.com/apache/pulsar) · [Vercel](https://github.com/vercel/ncc) · [Microsoft](https://github.com/microsoft/SynapseML) · [Firebase](https://github.com/firebase/flutterfire) · [AWS](https://github.com/aws-ia/terraform-aws-eks-blueprints) – and [many more](https://github.com/amannn/action-semantic-pull-request/network/dependents).

## Examples

**Valid pull request titles:**

- fix: Correct typo
- feat: Add support for Node.js 18
- refactor!: Drop support for Node.js 12
- feat(ui): Add `Button` component

> Note that since pull request titles only have a single line, you have to use `!` to indicate breaking changes.

See [Conventional Commits](https://www.conventionalcommits.org/) for more examples.

## Installation

1. If your goal is to create squashed commits that will be used for automated releases, you'll want to configure your GitHub repository to [use the squash & merge strategy](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/configuring-commit-squashing-for-pull-requests) and tick the option "Default to PR title for squash merge commits".
2. [Add the action](https://docs.github.com/en/actions/quickstart) with the following configuration:

```yml
name: 'Lint PR'

on:
  pull_request_target:
    types:
      - opened
      - reopened
      - edited
      # - synchronize (if you use required Actions)

jobs:
  main:
    name: Validate PR title
    runs-on: ubuntu-slim
    permissions:
      pull-requests: read
    steps:
      - uses: amannn/action-semantic-pull-request@v6
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

See the [event triggers documentation](#event-triggers) below to learn more about what `pull_request_target` means.

## Configuration

The action works without configuration, however you can provide options for customization.

The following terminology helps to understand the configuration options:

```
feat(ui): Add `Button` component
^    ^    ^
|    |    |__ Subject
|    |_______ Scope
|____________ Type
```

```yml
        with:
          # Configure which types are allowed (newline-delimited).
          # These are regex patterns auto-wrapped in `^ $`.
          # Default: https://github.com/commitizen/conventional-commit-types
          types: |
            fix
            feat
            JIRA-\d+
          # Configure which scopes are allowed (newline-delimited).
          # These are regex patterns auto-wrapped in `^ $`.
          scopes: |
            core
            ui
            JIRA-\d+
          # Configure that a scope must always be provided.
          requireScope: true
          # Configure which scopes are disallowed in PR titles (newline-delimited).
          # For instance by setting the value below, `chore(release): ...` (lowercase)
          # and `ci(e2e,release): ...` (unknown scope) will be rejected.
          # These are regex patterns auto-wrapped in `^ $`.
          disallowScopes: |
            release
            [A-Z]+
          # Configure additional validation for the subject based on a regex.
          # This example ensures the subject doesn't start with an uppercase character.
          subjectPattern: ^(?![A-Z]).+$
          # If `subjectPattern` is configured, you can use this property to override
          # the default error message that is shown when the pattern doesn't match.
          # The variables `subject` and `title` can be used within the message.
          subjectPatternError: |
            The subject "{subject}" found in the pull request title "{title}"
            didn't match the configured pattern. Please ensure that the subject
            doesn't start with an uppercase character.
          # The GitHub base URL will be automatically set to the correct value from the GitHub context variable.
          # If you want to override this, you can do so here (not recommended).
          githubBaseUrl: https://github.myorg.com/api/v3
          # If the PR contains one of these newline-delimited labels, the
          # validation is skipped. If you want to rerun the validation when
          # labels change, you might want to use the `labeled` and `unlabeled`
          # event triggers in your workflow.
          ignoreLabels: |
            bot
            ignore-semantic-pull-request
          # If you're using a format for the PR title that differs from the traditional Conventional
          # Commits spec, you can use these options to customize the parsing of the type, scope and
          # subject. The `headerPattern` should contain a regex where the capturing groups in parentheses
          # correspond to the parts listed in `headerPatternCorrespondence`.
          # See: https://github.com/conventional-changelog/conventional-changelog/tree/master/packages/conventional-commits-parser#headerpattern
          headerPattern: '^(\w*)(?:\(([\w$.\-*/ ]*)\))?: (.*)$'
          headerPatternCorrespondence: type, scope, subject
```

### Work-in-progress pull requests

For work-in-progress PRs you can typically use [draft pull requests from GitHub](https://github.blog/2019-02-14-introducing-draft-pull-requests/). However, private repositories on the free plan don't have this option and therefore this action allows you to opt-in to using the special "[WIP]" prefix to indicate this state.

**Example:**

```
[WIP] feat: Add support for Node.js 18
```

This will prevent the PR title from being validated, and pull request checks will remain pending.

**Attention**: If you want to use the this feature, you need to grant the `pull-requests: write` permission to the GitHub Action. This is because the action will update the status of the PR to remain in a pending state while `[WIP]` is present in the PR title.

```yml
name: 'Lint PR'

permissions:
  pull-requests: write

jobs:
  main:
    name: Validate PR title
    runs-on: ubuntu-slim
    permissions:
      pull-requests: read
    steps:
      - uses: amannn/action-semantic-pull-request@v6
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        with:
          wip: true
```

### Legacy configuration for validating single commits

When using "Squash and merge" on a PR with only one commit, GitHub will suggest using that commit message instead of the PR title for the merge commit. As it's easy to commit this by mistake this action supports two configuration options to provide additional validation for this case.

```yml
          # If the PR only contains a single commit, the action will validate that
          # it matches the configured pattern.
          validateSingleCommit: true
          # Related to `validateSingleCommit` you can opt-in to validate that the PR
          # title matches a single commit to avoid confusion.
          validateSingleCommitMatchesPrTitle: true
```

However, [GitHub has introduced an option to streamline this behaviour](https://github.blog/changelog/2022-05-11-default-to-pr-titles-for-squash-merge-commit-messages/), so using that instead should be preferred.

## Event triggers

There are two events that can be used as triggers for this action, each with different characteristics:

1. [`pull_request_target`](https://docs.github.com/en/actions/reference/events-that-trigger-workflows#pull_request_target): This allows the action to be used in a fork-based workflow, where e.g. you want to accept pull requests in a public repository. In this case, the configuration from the main branch of your repository will be used for the check. This means that you need to have this configuration in the main branch for the action to run at all (e.g. it won't run within a PR that adds the action initially). Also if you change the configuration in a PR, the changes will not be reflected for the current PR – only subsequent ones after the changes are in the main branch.
2. [`pull_request`](https://docs.github.com/en/actions/reference/events-that-trigger-workflows#pull_request): This configuration uses the latest configuration that is available in the current branch. It will only work if the branch is based in the repository itself. If this configuration is used and a pull request from a fork is opened, you'll encounter an error as the GitHub token environment parameter is not available. This option is viable if all contributors have write access to the repository.

> [!TIP]
> If the workflow is required for merging, you need to ensure that the you add a trigger type for [`synchronize`](https://docs.github.com/en/webhooks/webhook-events-and-payloads?actionType=synchronize#pull_request).
> This will ensure that the check is ran on each new push as required workflows need to run on the lastest change.

## Outputs

- The outputs `type`, `scope` and `subject` are populated, except for if the `wip` option is used.
- The `error_message` output will be populated in case the validation fails.

[An output can be used in other steps](https://docs.github.com/en/actions/using-jobs/defining-outputs-for-jobs), for example to comment the error message onto the pull request.

<details>
<summary>Example</summary>

````yml
name: 'Lint PR'

on:
  pull_request_target:
    types:
      - opened
      - edited

permissions:
  pull-requests: write

jobs:
  main:
    name: Validate PR title
    runs-on: ubuntu-slim
    steps:
      - uses: amannn/action-semantic-pull-request@v6
        id: lint_pr_title
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}

      - uses: marocchino/sticky-pull-request-comment@v2
        # When the previous steps fails, the workflow would stop. By adding this
        # condition you can continue the execution with the populated error message.
        if: always() && (steps.lint_pr_title.outputs.error_message != null)
        with:
          header: pr-title-lint-error
          message: |
            Hey there and thank you for opening this pull request! 👋🏼

            We require pull request titles to follow the [Conventional Commits specification](https://www.conventionalcommits.org/en/v1.0.0/) and it looks like your proposed title needs to be adjusted.

            Details:

            ```
            ${{ steps.lint_pr_title.outputs.error_message }}
            ```

      # Delete a previous comment when the issue has been resolved
      - if: ${{ steps.lint_pr_title.outputs.error_message == null }}
        uses: marocchino/sticky-pull-request-comment@v2
        with:
          header: pr-title-lint-error
          delete: true
````

</details>
```

## File: `action.yml`
```yaml
name: semantic-pull-request
author: Jan Amann <jan@amann.work>
description: Ensure your PR title matches the Conventional Commits spec (https://www.conventionalcommits.org/).
runs:
  using: 'node24'
  main: 'dist/index.js'
branding:
  icon: 'shield'
  color: 'green'
inputs:
  types:
    description: "Provide custom types (newline delimited) if you don't want the default ones from https://www.conventionalcommits.org. These are regex patterns auto-wrapped in `^ $`."
    required: false
  scopes:
    description: 'Configure which scopes are allowed (newline delimited). These are regex patterns auto-wrapped in `^ $`.'
    required: false
  requireScope:
    description: 'Configure that a scope must always be provided.'
    required: false
  disallowScopes:
    description: 'Configure which scopes are disallowed in PR titles (newline delimited). These are regex patterns auto-wrapped in ` ^$`.'
    required: false
  subjectPattern:
    description: "Configure additional validation for the subject based on a regex. E.g. '^(?![A-Z]).+$' ensures the subject doesn't start with an uppercase character."
    required: false
  subjectPatternError:
    description: "If `subjectPattern` is configured, you can use this property to override the default error message that is shown when the pattern doesn't match. The variables `subject` and `title` can be used within the message."
    required: false
  validateSingleCommit:
    description: 'When using "Squash and merge" on a PR with only one commit, GitHub will suggest using that commit message instead of the PR title for the merge commit, and it''s easy to commit this by mistake. Enable this option to also validate the commit message for one commit PRs.'
    required: false
  validateSingleCommitMatchesPrTitle:
    description: 'Related to `validateSingleCommit` you can opt-in to validate that the PR title matches a single commit to avoid confusion.'
    required: false
  githubBaseUrl:
    description: 'The GitHub base URL will be automatically set to the correct value from the GitHub context variable. If you want to override this, you can do so here (not recommended).'
    required: false
    default: '${{ github.api_url }}'
  ignoreLabels:
    description: 'If the PR contains one of these labels (newline delimited), the validation is skipped. If you want to rerun the validation when labels change, you might want to use the `labeled` and `unlabeled` event triggers in your workflow.'
    required: false
  headerPattern:
    description: "If you're using a format for the PR title that differs from the traditional Conventional Commits spec, you can use this to customize the parsing of the type, scope and subject. The `headerPattern` should contain a regex where the capturing groups in parentheses correspond to the parts listed in `headerPatternCorrespondence`. For more details see: https://github.com/conventional-changelog/conventional-changelog/tree/master/packages/conventional-commits-parser#headerpattern"
    required: false
  headerPatternCorrespondence:
    description: 'If `headerPattern` is configured, you can use this to define which capturing groups correspond to the type, scope and subject.'
    required: false
  wip:
    description: "For work-in-progress PRs you can typically use draft pull requests from Github. However, private repositories on the free plan don't have this option and therefore this action allows you to opt-in to using the special '[WIP]' prefix to indicate this state. This will avoid the validation of the PR title and the pull request checks remain pending. Note that a second check will be reported if this is enabled."
    required: false
```

## File: `eslint.config.mjs`
```
import {getPresets} from 'eslint-config-molindo';
import globals from 'globals';

export default [
  ...(await getPresets('javascript', 'vitest')),
  {
    languageOptions: {
      globals: globals.node
    }
  }
];
```

## File: `index.js`
```javascript
const run = require('./src');

run();
```

## File: `package.json`
```json
{
  "name": "action-semantic-pull-request",
  "version": "0.0.0",
  "description": "Ensure your PR title matches the Conventional Commits spec.",
  "main": "dist/index.js",
  "type": "module",
  "scripts": {
    "lint": "eslint src && prettier --check src",
    "test": "vitest src",
    "build": "rollup -c"
  },
  "repository": {
    "type": "git",
    "url": "git+https://github.com/amannn/action-semantic-pull-request.git"
  },
  "keywords": [
    "github-action",
    "conventional-commits"
  ],
  "author": "Jan Amann <jan@amann.work>",
  "license": "MIT",
  "bugs": {
    "url": "https://github.com/amannn/action-semantic-pull-request/issues"
  },
  "homepage": "https://github.com/amannn/action-semantic-pull-request#readme",
  "dependencies": {
    "@actions/core": "^2.0.1",
    "@actions/github": "^6.0.1",
    "conventional-changelog-conventionalcommits": "9.1.0",
    "conventional-commit-types": "^3.0.0",
    "conventional-commits-parser": "^6.2.1"
  },
  "devDependencies": {
    "@rollup/plugin-commonjs": "^29.0.0",
    "@rollup/plugin-json": "^6.1.0",
    "@rollup/plugin-node-resolve": "^16.0.3",
    "@semantic-release/changelog": "6.0.3",
    "@semantic-release/commit-analyzer": "13.0.1",
    "@semantic-release/git": "10.0.1",
    "@semantic-release/github": "12.0.2",
    "@semantic-release/release-notes-generator": "14.1.0",
    "eslint": "9.39.2",
    "eslint-config-molindo": "8.0.0",
    "globals": "^17.0.0",
    "prettier": "^3.7.4",
    "rollup": "^4.54.0",
    "semantic-release": "^25.0.2",
    "semantic-release-major-tag": "0.3.2",
    "vitest": "^4.0.16"
  },
  "engines": {
    "node": "^24.0.0"
  },
  "prettier": "eslint-config-molindo/.prettierrc.json"
}
```

## File: `rollup.config.js`
```javascript
// See: https://rollupjs.org/introduction/

import commonjs from '@rollup/plugin-commonjs';
import json from '@rollup/plugin-json';
import {nodeResolve} from '@rollup/plugin-node-resolve';

const config = {
  input: 'src/index.js',
  output: {
    esModule: true,
    file: 'dist/index.js',
    format: 'es',
    sourcemap: true
  },
  plugins: [commonjs(), nodeResolve({preferBuiltins: true}), json()]
};

export default config;
```

## File: `src/ConfigParser.js`
```javascript
const ENUM_SPLIT_REGEX = /\n/;

export default {
  parseEnum(input) {
    return input
      .split(ENUM_SPLIT_REGEX)
      .map((part) => part.trim())
      .filter((part) => part.length > 0);
  },

  parseBoolean(input) {
    return JSON.parse(input.trim());
  },

  parseString(input) {
    return input;
  }
};
```

## File: `src/ConfigParser.test.js`
```javascript
import {describe, expect, it} from 'vitest';
import ConfigParser from './ConfigParser.js';

describe('parseEnum', () => {
  it('parses newline-delimited lists, trimming whitespace', () => {
    expect(ConfigParser.parseEnum('one   \ntwo   \nthree  \r\nfour')).toEqual([
      'one',
      'two',
      'three',
      'four'
    ]);
  });
  it('parses newline-delimited lists, including regex, trimming whitespace', () => {
    expect(
      ConfigParser.parseEnum('one   \ntwo   \n^[A-Z]+\\n$  \r\nfour')
    ).toEqual(['one', 'two', '^[A-Z]+\\n$', 'four']);
  });
});
```

## File: `src/formatMessage.js`
```javascript
export default function formatMessage(message, values) {
  let formatted = message;
  if (values) {
    Object.entries(values).forEach(([key, value]) => {
      formatted = formatted.replace(new RegExp(`{${key}}`, 'g'), value);
    });
  }
  return formatted;
}
```

## File: `src/formatMessage.test.js`
```javascript
import {expect, it} from 'vitest';
import formatMessage from './formatMessage.js';

it('handles a string without variables', () => {
  const message = 'this is test';
  expect(formatMessage(message)).toEqual(message);
});

it('replaces a variable', () => {
  expect(
    formatMessage('this is {subject} test', {subject: 'my subject'})
  ).toEqual('this is my subject test');
});

it('replaces multiple variables', () => {
  expect(
    formatMessage('this {title} is {subject} test', {
      subject: 'my subject',
      title: 'my title'
    })
  ).toEqual('this my title is my subject test');
});

it('replaces multiple instances of a variable', () => {
  expect(
    formatMessage(
      '99 bottles of {beverage} on the wall, 99 bottles of {beverage}.',
      {beverage: 'beer'}
    )
  ).toEqual('99 bottles of beer on the wall, 99 bottles of beer.');
});
```

## File: `src/index.js`
```javascript
import core from '@actions/core';
import github from '@actions/github';
import parseConfig from './parseConfig.js';
import validatePrTitle from './validatePrTitle.js';

async function run() {
  try {
    const {
      types,
      scopes,
      requireScope,
      disallowScopes,
      wip,
      subjectPattern,
      subjectPatternError,
      headerPattern,
      headerPatternCorrespondence,
      validateSingleCommit,
      validateSingleCommitMatchesPrTitle,
      githubBaseUrl,
      ignoreLabels
    } = parseConfig();

    const client = github.getOctokit(process.env.GITHUB_TOKEN, {
      baseUrl: githubBaseUrl
    });

    const contextPullRequest = github.context.payload.pull_request;
    if (!contextPullRequest) {
      throw new Error(
        "This action can only be invoked in `pull_request_target` or `pull_request` events. Otherwise the pull request can't be inferred."
      );
    }

    const owner = contextPullRequest.base.user.login;
    const repo = contextPullRequest.base.repo.name;

    // The pull request info on the context isn't up to date. When
    // the user updates the title and re-runs the workflow, it would
    // be outdated. Therefore fetch the pull request via the REST API
    // to ensure we use the current title.
    const {data: pullRequest} = await client.rest.pulls.get({
      owner,
      repo,
      pull_number: contextPullRequest.number
    });

    // Ignore errors if specified labels are added.
    if (ignoreLabels) {
      const labelNames = pullRequest.labels.map((label) => label.name);
      for (const labelName of labelNames) {
        if (ignoreLabels.includes(labelName)) {
          core.info(
            `Validation was skipped because the PR label "${labelName}" was found.`
          );
          return;
        }
      }
    }

    // Pull requests that start with "[WIP] " are excluded from the check.
    const isWip = wip && /^\[WIP\]\s/.test(pullRequest.title);

    let validationError;
    if (!isWip) {
      try {
        await validatePrTitle(pullRequest.title, {
          types,
          scopes,
          requireScope,
          disallowScopes,
          subjectPattern,
          subjectPatternError,
          headerPattern,
          headerPatternCorrespondence
        });

        if (validateSingleCommit) {
          const commits = [];
          let nonMergeCommits = [];

          for await (const response of client.paginate.iterator(
            client.rest.pulls.listCommits,
            {
              owner,
              repo,
              pull_number: contextPullRequest.number
            }
          )) {
            commits.push(...response.data);

            // GitHub does not count merge commits when deciding whether to use
            // the PR title or a commit message for the squash commit message.
            nonMergeCommits = commits.filter(
              (commit) => commit.parents.length < 2
            );

            // We only need two non-merge commits to know that the PR
            // title won't be used.
            if (nonMergeCommits.length >= 2) break;
          }

          // If there is only one (non merge) commit present, GitHub will use
          // that commit rather than the PR title for the title of a squash
          // commit. To make sure a semantic title is used for the squash
          // commit, we need to validate the commit title.
          if (nonMergeCommits.length === 1) {
            try {
              await validatePrTitle(nonMergeCommits[0].commit.message, {
                types,
                scopes,
                requireScope,
                disallowScopes,
                subjectPattern,
                subjectPatternError,
                headerPattern,
                headerPatternCorrespondence
              });
              // eslint-disable-next-line unicorn/prefer-optional-catch-binding, no-unused-vars -- Legacy syntax for compatibility
            } catch (error) {
              throw new Error(
                `Pull request has only one commit and it's not semantic; this may lead to a non-semantic commit in the base branch (see https://github.com/community/community/discussions/16271 ). Amend the commit message to match the pull request title, or add another commit.`
              );
            }

            if (validateSingleCommitMatchesPrTitle) {
              const commitTitle =
                nonMergeCommits[0].commit.message.split('\n')[0];
              if (commitTitle !== pullRequest.title) {
                throw new Error(
                  `The pull request has only one (non-merge) commit and in this case Github will use it as the default commit message when merging. The pull request title doesn't match the commit though ("${pullRequest.title}" vs. "${commitTitle}"). Please update the pull request title accordingly to avoid surprises.`
                );
              }
            }
          }
        }
      } catch (error) {
        validationError = error;
      }
    }

    if (wip) {
      const newStatus =
        isWip || validationError != null ? 'pending' : 'success';

      // When setting the status to "pending", the checks don't
      // complete. This can be used for WIP PRs in repositories
      // which don't support draft pull requests.
      // https://developer.github.com/v3/repos/statuses/#create-a-status
      await client.request('POST /repos/:owner/:repo/statuses/:sha', {
        owner,
        repo,
        sha: pullRequest.head.sha,
        state: newStatus,
        target_url: 'https://github.com/amannn/action-semantic-pull-request',
        description: isWip
          ? 'This PR is marked with "[WIP]".'
          : validationError
            ? 'PR title validation failed'
            : 'Ready for review & merge.',
        context: 'action-semantic-pull-request'
      });
    }

    if (!isWip && validationError) {
      throw validationError;
    }
  } catch (error) {
    core.setFailed(error.message);
  }
}

await run();
```

## File: `src/parseConfig.js`
```javascript
import ConfigParser from './ConfigParser.js';

export default function parseConfig() {
  let types;
  if (process.env.INPUT_TYPES) {
    types = ConfigParser.parseEnum(process.env.INPUT_TYPES);
  }

  let scopes;
  if (process.env.INPUT_SCOPES) {
    scopes = ConfigParser.parseEnum(process.env.INPUT_SCOPES);
  }

  let requireScope;
  if (process.env.INPUT_REQUIRESCOPE) {
    requireScope = ConfigParser.parseBoolean(process.env.INPUT_REQUIRESCOPE);
  }

  let disallowScopes;
  if (process.env.INPUT_DISALLOWSCOPES) {
    disallowScopes = ConfigParser.parseEnum(process.env.INPUT_DISALLOWSCOPES);
  }

  let subjectPattern;
  if (process.env.INPUT_SUBJECTPATTERN) {
    subjectPattern = ConfigParser.parseString(process.env.INPUT_SUBJECTPATTERN);
  }

  let subjectPatternError;
  if (process.env.INPUT_SUBJECTPATTERNERROR) {
    subjectPatternError = ConfigParser.parseString(
      process.env.INPUT_SUBJECTPATTERNERROR
    );
  }

  let headerPattern;
  if (process.env.INPUT_HEADERPATTERN) {
    headerPattern = ConfigParser.parseString(process.env.INPUT_HEADERPATTERN);
  }

  let headerPatternCorrespondence;
  if (process.env.INPUT_HEADERPATTERNCORRESPONDENCE) {
    // todo: this should be migrated to an enum w/ ConfigParser.parseEnum
    headerPatternCorrespondence =
      process.env.INPUT_HEADERPATTERNCORRESPONDENCE.split(',')
        .map((part) => part.trim())
        .filter((part) => part.length > 0);
  }

  let wip;
  if (process.env.INPUT_WIP) {
    wip = ConfigParser.parseBoolean(process.env.INPUT_WIP);
  }

  let validateSingleCommit;
  if (process.env.INPUT_VALIDATESINGLECOMMIT) {
    validateSingleCommit = ConfigParser.parseBoolean(
      process.env.INPUT_VALIDATESINGLECOMMIT
    );
  }

  let validateSingleCommitMatchesPrTitle;
  if (process.env.INPUT_VALIDATESINGLECOMMITMATCHESPRTITLE) {
    validateSingleCommitMatchesPrTitle = ConfigParser.parseBoolean(
      process.env.INPUT_VALIDATESINGLECOMMITMATCHESPRTITLE
    );
  }

  let githubBaseUrl;
  if (process.env.INPUT_GITHUBBASEURL) {
    githubBaseUrl = ConfigParser.parseString(process.env.INPUT_GITHUBBASEURL);
  }

  let ignoreLabels;
  if (process.env.INPUT_IGNORELABELS) {
    ignoreLabels = ConfigParser.parseEnum(process.env.INPUT_IGNORELABELS);
  }

  return {
    types,
    scopes,
    requireScope,
    disallowScopes,
    wip,
    subjectPattern,
    subjectPatternError,
    headerPattern,
    headerPatternCorrespondence,
    validateSingleCommit,
    validateSingleCommitMatchesPrTitle,
    githubBaseUrl,
    ignoreLabels
  };
}
```

## File: `src/validatePrTitle.js`
```javascript
import core from '@actions/core';
// eslint-disable-next-line import/no-unresolved -- False positive
import conventionalCommitsConfig from 'conventional-changelog-conventionalcommits';
import conventionalCommitTypes from 'conventional-commit-types';
// eslint-disable-next-line import/no-unresolved -- False positive
import {CommitParser} from 'conventional-commits-parser';
import formatMessage from './formatMessage.js';

const defaultTypes = Object.keys(conventionalCommitTypes.types);

export default async function validatePrTitle(
  prTitle,
  {
    types,
    scopes,
    requireScope,
    disallowScopes,
    subjectPattern,
    subjectPatternError,
    headerPattern,
    headerPatternCorrespondence
  } = {}
) {
  if (!types) types = defaultTypes;

  const {parser: parserOpts} = await conventionalCommitsConfig();
  if (headerPattern) {
    parserOpts.headerPattern = headerPattern;
  }
  if (headerPatternCorrespondence) {
    parserOpts.headerCorrespondence = headerPatternCorrespondence;
  }
  const result = new CommitParser(parserOpts).parse(prTitle);

  core.setOutput('type', result.type);
  core.setOutput('scope', result.scope);
  core.setOutput('subject', result.subject);

  function printAvailableTypes() {
    return `Available types:\n${types
      .map((type) => {
        let bullet = ` - ${type}`;

        if (types === defaultTypes) {
          bullet += `: ${conventionalCommitTypes.types[type].description}`;
        }

        return bullet;
      })
      .join('\n')}`;
  }

  function isUnknownScope(s) {
    return scopes && !scopes.some((scope) => new RegExp(`^${scope}$`).test(s));
  }

  function isDisallowedScope(s) {
    return (
      disallowScopes &&
      disallowScopes.some((scope) => new RegExp(`^${scope}$`).test(s))
    );
  }

  if (!result.type) {
    raiseError(
      `No release type found in pull request title "${prTitle}". Add a prefix to indicate what kind of release this pull request corresponds to. For reference, see https://www.conventionalcommits.org/\n\n${printAvailableTypes()}`
    );
  }

  if (!result.subject) {
    raiseError(`No subject found in pull request title "${prTitle}".`);
  }

  if (!types.some((type) => new RegExp(`^${type}$`).test(result.type))) {
    raiseError(
      `Unknown release type "${
        result.type
      }" found in pull request title "${prTitle}".\n\n${printAvailableTypes()}`
    );
  }

  if (requireScope && !result.scope) {
    let message = `No scope found in pull request title "${prTitle}".`;
    if (scopes) {
      message += ` Scope must match one of: ${scopes.join(', ')}.`;
    }
    raiseError(message);
  }

  const givenScopes = result.scope
    ? result.scope.split(',').map((scope) => scope.trim())
    : undefined;

  const unknownScopes = givenScopes ? givenScopes.filter(isUnknownScope) : [];
  if (scopes && unknownScopes.length > 0) {
    raiseError(
      `Unknown ${
        unknownScopes.length > 1 ? 'scopes' : 'scope'
      } "${unknownScopes.join(
        ','
      )}" found in pull request title "${prTitle}". Scope must match one of: ${scopes.join(
        ', '
      )}.`
    );
  }

  const disallowedScopes = givenScopes
    ? givenScopes.filter(isDisallowedScope)
    : [];
  if (disallowScopes && disallowedScopes.length > 0) {
    raiseError(
      `Disallowed ${
        disallowedScopes.length === 1 ? 'scope was' : 'scopes were'
      } found: ${disallowedScopes.join(', ')}`
    );
  }

  function throwSubjectPatternError(message) {
    if (subjectPatternError) {
      message = formatMessage(subjectPatternError, {
        subject: result.subject,
        title: prTitle
      });
    }
    raiseError(message);
  }

  if (subjectPattern) {
    const match = result.subject.match(new RegExp(subjectPattern));

    if (!match) {
      throwSubjectPatternError(
        `The subject "${result.subject}" found in pull request title "${prTitle}" doesn't match the configured pattern "${subjectPattern}".`
      );
    }

    const matchedPart = match[0];
    if (matchedPart.length !== result.subject.length) {
      throwSubjectPatternError(
        `The subject "${result.subject}" found in pull request title "${prTitle}" isn't an exact match for the configured pattern "${subjectPattern}". Please provide a subject that matches the whole pattern exactly.`
      );
    }
  }

  function raiseError(message) {
    core.setOutput('error_message', message);

    throw new Error(message);
  }
}
```

## File: `src/validatePrTitle.test.js`
```javascript
import {describe, expect, it} from 'vitest';
import validatePrTitle from './validatePrTitle.js';

it('allows valid PR titles that use the default types', async () => {
  const inputs = [
    'fix: Fix bug',
    'fix!: Fix bug',
    'feat: Add feature',
    'feat!: Add feature',
    'refactor: Internal cleanup'
  ];

  for (let index = 0; index < inputs.length; index++) {
    await validatePrTitle(inputs[index]);
  }
});

it('throws for PR titles without a type', async () => {
  await expect(validatePrTitle('Fix bug')).rejects.toThrow(
    'No release type found in pull request title "Fix bug".'
  );
});

it('throws for PR titles with only a type', async () => {
  await expect(validatePrTitle('fix:')).rejects.toThrow(
    'No release type found in pull request title "fix:".'
  );
});

it('throws for PR titles without a subject', async () => {
  await expect(validatePrTitle('fix: ')).rejects.toThrow(
    'No subject found in pull request title "fix: ".'
  );
});

it('throws for PR titles with an unknown type', async () => {
  await expect(validatePrTitle('foo: Bar')).rejects.toThrow(
    'Unknown release type "foo" found in pull request title "foo: Bar".'
  );
});

describe('regex types', () => {
  const headerPattern = /^([\w-]*)(?:\(([\w$.\-*/ ]*)\))?: (.*)$/;

  it('allows a regex matching type', async () => {
    await validatePrTitle('JIRA-123: Bar', {
      types: ['JIRA-\\d+'],
      headerPattern
    });
  });

  it('can be used for dynamic Jira keys', async () => {
    const inputs = ['JIRA-123', 'P-123', 'INT-31', 'CONF-0'];

    for (let index = 0; index < inputs.length; index++) {
      await validatePrTitle(`${inputs[index]}: did the thing`, {
        types: ['[A-Z]+-\\d+'],
        headerPattern
      });
    }
  });

  it('throws for PR titles without a type', async () => {
    await expect(
      validatePrTitle('Fix JIRA-123 bug', {
        types: ['JIRA-\\d+'],
        headerPattern
      })
    ).rejects.toThrow(
      'No release type found in pull request title "Fix JIRA-123 bug".'
    );
  });

  it('throws for PR titles with only a type', async () => {
    await expect(
      validatePrTitle('JIRA-123:', {
        types: ['JIRA-\\d+'],
        headerPattern
      })
    ).rejects.toThrow(
      'No release type found in pull request title "JIRA-123:".'
    );
  });

  it('throws for PR titles without a subject', async () => {
    await expect(
      validatePrTitle('JIRA-123: ', {
        types: ['JIRA-\\d+'],
        headerPattern
      })
    ).rejects.toThrow('No subject found in pull request title "JIRA-123: ".');
  });

  it('throws for PR titles that do not match the regex', async () => {
    await expect(
      validatePrTitle('CONF-123: ', {
        types: ['JIRA-\\d+'],
        headerPattern
      })
    ).rejects.toThrow('No subject found in pull request title "CONF-123: ".');
  });

  it('throws when an unknown type is detected for auto-wrapping regex', async () => {
    await expect(
      validatePrTitle('JIRA-123A: Bar', {
        types: ['JIRA-\\d+'],
        headerPattern
      })
    ).rejects.toThrow(
      'Unknown release type "JIRA-123A" found in pull request title "JIRA-123A: Bar".\n\nAvailable types:\n - JIRA-\\d+'
    );
  });

  it('allows scopes when using a regex for the type', async () => {
    await validatePrTitle('JIRA-123(core): Bar', {
      types: ['JIRA-\\d+'],
      headerPattern
    });
  });
});

describe('defined scopes', () => {
  it('allows a missing scope by default', async () => {
    await validatePrTitle('fix: Bar');
  });

  it('allows all scopes by default', async () => {
    await validatePrTitle('fix(core): Bar');
  });

  it('allows a missing scope when custom scopes are defined', async () => {
    await validatePrTitle('fix: Bar', {scopes: ['foo']});
  });

  it('allows a matching scope', async () => {
    await validatePrTitle('fix(core): Bar', {scopes: ['core']});
  });

  it('allows a regex matching scope', async () => {
    await validatePrTitle('fix(CORE): Bar', {scopes: ['[A-Z]+']});
  });

  it('allows multiple matching scopes', async () => {
    await validatePrTitle('fix(core,e2e): Bar', {
      scopes: ['core', 'e2e', 'web']
    });
  });

  it('allows multiple regex matching scopes', async () => {
    await validatePrTitle('fix(CORE,WEB): Bar', {
      scopes: ['[A-Z]+']
    });
  });

  it('throws when an unknown scope is detected within multiple scopes', async () => {
    await expect(
      validatePrTitle('fix(core,e2e,foo,bar): Bar', {scopes: ['foo', 'core']})
    ).rejects.toThrow(
      'Unknown scopes "e2e,bar" found in pull request title "fix(core,e2e,foo,bar): Bar". Scope must match one of: foo, core.'
    );
  });

  it('throws when an unknown scope is detected within multiple scopes and a regex', async () => {
    await expect(
      validatePrTitle('fix(CORE,e2e,foo,bar): Bar', {
        scopes: ['foo', '[A-Z]+']
      })
    ).rejects.toThrow(
      'Unknown scopes "e2e,bar" found in pull request title "fix(CORE,e2e,foo,bar): Bar". Scope must match one of: foo, [A-Z]+.'
    );
  });

  it('throws when an unknown scope is detected', async () => {
    await expect(
      validatePrTitle('fix(core): Bar', {scopes: ['foo']})
    ).rejects.toThrow(
      'Unknown scope "core" found in pull request title "fix(core): Bar". Scope must match one of: foo.'
    );
  });

  it('throws when an unknown scope is detected for auto-wrapped regex matching', async () => {
    await expect(
      validatePrTitle('fix(score): Bar', {scopes: ['core']})
    ).rejects.toThrow(
      'Unknown scope "score" found in pull request title "fix(score): Bar". Scope must match one of: core.'
    );
  });

  it('throws when an unknown scope is detected for auto-wrapped regex matching when input is already wrapped', async () => {
    await expect(
      validatePrTitle('fix(score): Bar', {scopes: ['^[A-Z]+$']})
    ).rejects.toThrow(
      'Unknown scope "score" found in pull request title "fix(score): Bar". Scope must match one of: ^[A-Z]+$.'
    );
  });

  it('throws when an unknown scope is detected for regex matching', async () => {
    await expect(
      validatePrTitle('fix(core): Bar', {scopes: ['[A-Z]+']})
    ).rejects.toThrow(
      'Unknown scope "core" found in pull request title "fix(core): Bar". Scope must match one of: [A-Z]+.'
    );
  });

  describe('require scope', () => {
    describe('scope allowlist defined', () => {
      it('passes when a scope is provided', async () => {
        await validatePrTitle('fix(core): Bar', {
          scopes: ['core'],
          requireScope: true
        });
      });

      it('throws when a scope is missing', async () => {
        await expect(
          validatePrTitle('fix: Bar', {
            scopes: ['foo', 'bar'],
            requireScope: true
          })
        ).rejects.toThrow(
          'No scope found in pull request title "fix: Bar". Scope must match one of: foo, bar.'
        );
      });
    });

    describe('disallow scopes', () => {
      it('passes when a single scope is provided, but not present in disallowScopes with one item', async () => {
        await validatePrTitle('fix(core): Bar', {disallowScopes: ['release']});
      });

      it('passes when a single scope is provided, but not present in disallowScopes with one regex item', async () => {
        await validatePrTitle('fix(core): Bar', {disallowScopes: ['[A-Z]+']});
      });

      it('passes when multiple scopes are provided, but not present in disallowScopes with one item', async () => {
        await validatePrTitle('fix(core,e2e,bar): Bar', {
          disallowScopes: ['release']
        });
      });

      it('passes when multiple scopes are provided, but not present in disallowScopes with one regex item', async () => {
        await validatePrTitle('fix(core,e2e,bar): Bar', {
          disallowScopes: ['[A-Z]+']
        });
      });

      it('passes when a single scope is provided, but not present in disallowScopes with multiple items', async () => {
        await validatePrTitle('fix(core): Bar', {
          disallowScopes: ['release', 'test', '[A-Z]+']
        });
      });

      it('passes when multiple scopes are provided, but not present in disallowScopes with multiple items', async () => {
        await validatePrTitle('fix(core,e2e,bar): Bar', {
          disallowScopes: ['release', 'test', '[A-Z]+']
        });
      });

      it('throws when a single scope is provided and it is present in disallowScopes with one item', async () => {
        await expect(
          validatePrTitle('fix(release): Bar', {disallowScopes: ['release']})
        ).rejects.toThrow('Disallowed scope was found: release');
      });

      it('throws when a single scope is provided and it is present in disallowScopes with one regex item', async () => {
        await expect(
          validatePrTitle('fix(RELEASE): Bar', {disallowScopes: ['[A-Z]+']})
        ).rejects.toThrow('Disallowed scope was found: RELEASE');
      });

      it('throws when a single scope is provided and it is present in disallowScopes with multiple item', async () => {
        await expect(
          validatePrTitle('fix(release): Bar', {
            disallowScopes: ['release', 'test']
          })
        ).rejects.toThrow('Disallowed scope was found: release');
      });

      it('throws when a single scope is provided and it is present in disallowScopes with multiple regex item', async () => {
        await expect(
          validatePrTitle('fix(RELEASE): Bar', {
            disallowScopes: ['[A-Z]+', '^[A-Z].+$']
          })
        ).rejects.toThrow('Disallowed scope was found: RELEASE');
      });

      it('throws when multiple scopes are provided and one of them is present in disallowScopes with one item ', async () => {
        await expect(
          validatePrTitle('fix(release,e2e): Bar', {
            disallowScopes: ['release']
          })
        ).rejects.toThrow('Disallowed scope was found: release');
      });

      it('throws when multiple scopes are provided and one of them is present in disallowScopes with one regex item ', async () => {
        await expect(
          validatePrTitle('fix(RELEASE,e2e): Bar', {
            disallowScopes: ['[A-Z]+']
          })
        ).rejects.toThrow('Disallowed scope was found: RELEASE');
      });

      it('throws when multiple scopes are provided and one of them is present in disallowScopes with multiple items ', async () => {
        await expect(
          validatePrTitle('fix(release,e2e): Bar', {
            disallowScopes: ['release', 'test']
          })
        ).rejects.toThrow('Disallowed scope was found: release');
      });

      it('throws when multiple scopes are provided and one of them is present in disallowScopes with multiple items and a regex', async () => {
        await expect(
          validatePrTitle('fix(RELEASE,e2e): Bar', {
            disallowScopes: ['[A-Z]+', 'test']
          })
        ).rejects.toThrow('Disallowed scope was found: RELEASE');
      });

      it('throws when multiple scopes are provided and more than one of them are present in disallowScopes', async () => {
        await expect(
          validatePrTitle('fix(release,test,CORE): Bar', {
            disallowScopes: ['release', 'test', '[A-Z]+']
          })
        ).rejects.toThrow('Disallowed scopes were found: release, test, CORE');
      });
    });

    describe('scope allowlist not defined', () => {
      it('passes when a scope is provided', async () => {
        await validatePrTitle('fix(core): Bar', {
          requireScope: true
        });
      });

      it('throws when a scope is missing', async () => {
        await expect(
          validatePrTitle('fix: Bar', {
            requireScope: true
          })
        ).rejects.toThrow(
          // Should make no mention of any available scope
          /^No scope found in pull request title "fix: Bar".$/
        );
      });
    });
  });
});

describe('custom types', () => {
  it('allows PR titles with a supported type', async () => {
    const inputs = ['foo: Foobar', 'bar: Foobar', 'baz: Foobar'];
    const types = ['foo', 'bar', 'baz'];

    for (let index = 0; index < inputs.length; index++) {
      await validatePrTitle(inputs[index], {types});
    }
  });

  it('throws for PR titles with an unknown type', async () => {
    await expect(
      validatePrTitle('fix: Foobar', {types: ['foo', 'bar']})
    ).rejects.toThrow(
      'Unknown release type "fix" found in pull request title "fix: Foobar".'
    );
  });
});

describe('description validation', () => {
  it('does not validate the description by default', async () => {
    await validatePrTitle('fix: sK!"§4123');
  });

  it('can pass the validation when `subjectPatternError` is configured', async () => {
    await validatePrTitle('fix: foobar', {
      subjectPattern: '^(?![A-Z]).+$',
      subjectPatternError:
        'The subject found in the pull request title cannot start with an uppercase character.'
    });
  });

  it('uses the `subjectPatternError` if available when the `subjectPattern` does not match', async () => {
    const customError =
      'The subject found in the pull request title cannot start with an uppercase character.';
    await expect(
      validatePrTitle('fix: Foobar', {
        subjectPattern: '^(?![A-Z]).+$',
        subjectPatternError: customError
      })
    ).rejects.toThrow(customError);
  });

  it('interpolates variables into `subjectPatternError`', async () => {
    await expect(
      validatePrTitle('fix: Foobar', {
        subjectPattern: '^(?![A-Z]).+$',
        subjectPatternError:
          'The subject "{subject}" found in the pull request title "{title}" cannot start with an uppercase character.'
      })
    ).rejects.toThrow(
      'The subject "Foobar" found in the pull request title "fix: Foobar" cannot start with an uppercase character.'
    );
  });

  it('throws for invalid subjects', async () => {
    await expect(
      validatePrTitle('fix: Foobar', {
        subjectPattern: '^(?![A-Z]).+$'
      })
    ).rejects.toThrow(
      'The subject "Foobar" found in pull request title "fix: Foobar" doesn\'t match the configured pattern "^(?![A-Z]).+$".'
    );
  });

  it('throws for only partial matches', async () => {
    await expect(
      validatePrTitle('fix: Foobar', {
        subjectPattern: 'Foo'
      })
    ).rejects.toThrow(
      'The subject "Foobar" found in pull request title "fix: Foobar" isn\'t an exact match for the configured pattern "Foo". Please provide a subject that matches the whole pattern exactly.'
    );
  });

  it('accepts valid subjects', async () => {
    await validatePrTitle('fix: foobar', {
      subjectPattern: '^(?![A-Z]).+$'
    });
  });
});
```


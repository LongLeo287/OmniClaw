---
id: documentation
type: knowledge
owner: OA_Triage
---
# documentation
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
    "name": "@feature-sliced/documentation",
    "version": "2.1.0",
    "private": true,
    "scripts": {
        "dev": "astro dev",
        "linkcheck": "CHECK_LINKS=true pnpm build",
        "docusaurus": "docusaurus",
        "start": "docusaurus start",
        "start:ru": "docusaurus start --locale ru",
        "start:en": "docusaurus start --locale en",
        "start:uz": "docusaurus start --locale uz",
        "start:kr": "docusaurus start --locale kr",
        "start:ja": "docusaurus start --locale ja",
        "start:zh": "docusaurus start --locale zh",
        "start:vi": "docusaurus start --locale vi",
        "build": "astro build",
        "swizzle": "docusaurus swizzle",
        "format": "prettier --cache --experimental-cli --write .",
        "test": "pnpm run test:lint && pnpm run build",
        "test:lint": "eslint --cache \"./**/*.{ts,tsx,js,jsx}\" && stylelint --cache ./**/*.scss && prettier --check --experimental-cli --cache .",
        "test:lint:fix": "eslint --cache --fix \"./**/*.{ts,tsx,js,jsx}\" && stylelint --cache **/*.scss --fix && prettier --write --experimental-cli --cache .",
        "deploy": "docusaurus deploy",
        "clear": "docusaurus clear",
        "serve": "docusaurus serve",
        "write-translations": "docusaurus write-translations",
        "write-heading-ids": "docusaurus write-heading-ids"
    },
    "engines": {
        "node": ">= 22"
    },
    "dependencies": {
        "@ant-design/icons": "^6.0.2",
        "@docusaurus/core": "^3.9.1",
        "@docusaurus/faster": "^3.9.1",
        "@docusaurus/plugin-client-redirects": "^3.9.1",
        "@docusaurus/plugin-content-docs": "^3.9.1",
        "@docusaurus/plugin-ideal-image": "^3.9.1",
        "@docusaurus/preset-classic": "^3.9.1",
        "@fontsource-variable/overpass": "^5.2.8",
        "@mdx-js/react": "^3.1.1",
        "@signalwire/docusaurus-plugin-llms-txt": "^1.2.2",
        "clsx": "^2.1.1",
        "lodash-es": "^4.17.21",
        "plugin-image-zoom": "^1.2.0",
        "prism-react-renderer": "^2.4.1",
        "pushfeedback": "^0.1.76",
        "pushfeedback-react": "^0.1.76",
        "react": "^19.1.1",
        "react-dom": "^19.1.1",
        "react-fast-marquee": "^1.6.5"
    },
    "devDependencies": {
        "@astrojs/starlight": "^0.37.4",
        "@babel/eslint-parser": "^7.28.4",
        "@docusaurus/module-type-aliases": "^3.9.1",
        "@docusaurus/theme-classic": "^3.9.1",
        "@docusaurus/tsconfig": "^3.9.1",
        "@docusaurus/types": "^3.9.1",
        "@eslint-kit/eslint-config-base": "4.1.0",
        "@eslint-kit/eslint-config-patch": "^1.0.0",
        "@eslint-kit/eslint-config-react": "^3.0.0",
        "@types/lodash-es": "^4.17.12",
        "@types/node": "^22.18.6",
        "@types/react": "^19.1.13",
        "@types/react-dom": "^19.1.9",
        "@typescript-eslint/eslint-plugin": "^6.21.0",
        "@typescript-eslint/parser": "^6.21.0",
        "astro": "^5.16.16",
        "docusaurus-plugin-sass": "^0.2.6",
        "eslint": "^7.32.0",
        "eslint-config-prettier": "^9.1.2",
        "eslint-import-resolver-alias": "1.1.2",
        "prettier": "^3.6.2",
        "prettier-plugin-astro": "^0.14.1",
        "remark-heading-id": "^1.0.1",
        "sass": "^1.93.2",
        "sharp": "^0.34.5",
        "starlight-links-validator": "^0.19.2",
        "starlight-llms-txt": "^0.7.0",
        "stylelint": "^16.24.0",
        "stylelint-config-recess-order": "^5.1.1",
        "stylelint-config-recommended": "^14.0.1",
        "stylelint-config-standard-scss": "^13.1.0",
        "typescript": "^5.9.2"
    },
    "packageManager": "pnpm@10.17.1+sha512.17c560fca4867ae9473a3899ad84a88334914f379be46d455cbf92e5cf4b39d34985d452d2583baf19967fa76cb5c17bc9e245529d0b98745721aa7200ecaf7a"
}

```

### File: README.md
```md
<a href="https://discord.gg/S8MzWTUsmp" title="Discord"><img align="right" alt="Discord" src="./.github/assets/README-discord.svg" height="80" /></a><a href="https://t.me/feature_sliced" title="Telegram"><img align="right" alt="Telegram" src="./.github/assets/README-telegram.svg" height="80" /></a><a href="https://feature-sliced.github.io/documentation/"><img align="right" alt="Website" src="./.github/assets/README-website.svg" height="80" /></a><img alt="Feature-Sliced Design, an architectural methodology for frontend projects" src="./.github/assets/README-banner-light.svg#gh-light-mode-only" height="80" /><img alt="Feature-Sliced Design, an architectural methodology for frontend projects" src="./.github/assets/README-banner-dark.svg#gh-dark-mode-only" height="80" />

**Feature-Sliced Design** (FSD) is an architectural methodology for scaffolding front-end applications. Simply put, it's a compilation of rules and conventions on organizing code. The main purpose of this methodology is to make the project more understandable and structured in the face of ever-changing business requirements.

This methodology is not tied to a particular stack — it can be used for web or native applications.

## Advantages

- **Uniformity**  
  The code is organized by scope of influence (layers), by domain (slices), and by technical purpose (segments).  
  This creates a standardized architecture that is easy to comprehend for newcomers.

- **Controlled reuse of logic**  
  Each architectural component has its purpose and predictable dependencies.  
  This keeps a balance between following the **DRY** principle and adaptation possibilities. 

- **Stability in face of changes and refactoring**  
  A module on a particular layer cannot use other modules on the same layer, or the layers above.  
  This enables isolated modifications without unforeseen consequences.

- **Orientation to business and users needs**  
  When the app is split into business domains, you can navigate the code to discover and deeper understand all the project features.

## Show off

To show off that your project uses FSD, you can use the GitHub topic `feature-sliced` and one of the following badges:

[![Feature-Sliced Design][shields-fsd-white]](https://feature-sliced.github.io/documentation/) [![Feature-Sliced Design][shields-fsd-pain]](https://feature-sliced.github.io/documentation/) [![Feature-Sliced Design][shields-fsd-domain]](https://feature-sliced.github.io/documentation/) [![Feature-Sliced Design][shields-fsd-feature]](https://feature-sliced.github.io/documentation/)

[shields-fsd-white]: https://img.shields.io/badge/Feature--Sliced-Design?style=for-the-badge&labelColor=262224&color=F2F2F2&logoWidth=10&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABQAAAAaCAYAAAC3g3x9AAAACXBIWXMAAALFAAACxQGJ1n/vAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAA/SURBVHgB7dKxCgAgCIThs/d/51JoNQIdDrxvqMXlR4FmFs92KDIX/wI7JSdDN+eHtkxIycnQvMNW8hN/crsDc5QgGX9NvT0AAAAASUVORK5CYII=

[shields-fsd-pain]: https://img.shields.io/badge/Feature--Sliced-Design?style=for-the-badge&labelColor=262224&color=F2F2F2&logoWidth=10&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABQAAAAaCAYAAAC3g3x9AAAACXBIWXMAAALFAAACxQGJ1n/vAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAABHSURBVHgB7dKxCQAgDETR08ZNHNBBHNBNrBQFuyCCKQK5V6QMfBJAWVij5zLwKbW6d0VYx2TZyXnBKxvEZJnDx2bylf1kdRM6tiAZsruQ/QAAAABJRU5ErkJggg==

[shields-fsd-domain]: https://img.shields.io/badge/Feature--Sliced-Design?style=for-the-badge&color=F2F2F2&labelColor=262224&logoWidth=10&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABQAAAAaCAYAAAC3g3x9AAAACXBIWXMAAALFAAACxQGJ1n/vAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAABISURBVHgB7dKxCQAgDETR0w2cws0cys2cwhEUBbsggikCuVekDHwSQFlYo7Q+8KnmtHdFWMdk2cl5wSsbxGSZw8dm8pX9ZHUTMBUgGU2F718AAAAASUVORK5CYII=

[shields-fsd-feature]: https://img.shields.io/badge/Feature--Sliced-Design?style=for-the-badge&labelColor=262224&color=F2F2F2&logoWidth=10&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABQAAAAaCAYAAAC3g3x9AAAACXBIWXMAAALFAAACxQGJ1n/vAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAABISURBVHgB7dKxCQAgDETR00EcwYEc0IEcwUUUBbsggikCuVekDHwSQFlYo/Y88KmktndFWMdk2cl5wSsbxGSZw8dm8pX9ZHUTdIYgGbPdU2QAAAAASUVORK5CYII=

<details><summary>Code snippet</summary>

```markdown
White: 
[![Feature-Sliced Design][shields-fsd-white]](https://feature-sliced.github.io/documentation/)

[shields-fsd-white]: https://img.shields.io/badge/Feature--Sliced-Design?style=for-the-badge&labelColor=262224&color=F2F2F2&logoWidth=10&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABQAAAAaCAYAAAC3g3x9AAAACXBIWXMAAALFAAACxQGJ1n/vAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAA/SURBVHgB7dKxCgAgCIThs/d/51JoNQIdDrxvqMXlR4FmFs92KDIX/wI7JSdDN+eHtkxIycnQvMNW8hN/crsDc5QgGX9NvT0AAAAASUVORK5CYII=

----

Pain (red):
[![Feature-Sliced Design][shields-fsd-pain]](https://feature-sliced.github.io/documentation/)

[shields-fsd-pain]: https://img.shields.io/badge/Feature--Sliced-Design?style=for-the-badge&labelColor=262224&color=F2F2F2&logoWidth=10&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABQAAAAaCAYAAAC3g3x9AAAACXBIWXMAAALFAAACxQGJ1n/vAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAABHSURBVHgB7dKxCQAgDETR08ZNHNBBHNBNrBQFuyCCKQK5V6QMfBJAWVij5zLwKbW6d0VYx2TZyXnBKxvEZJnDx2bylf1kdRM6tiAZsruQ/QAAAABJRU5ErkJggg==

----

Domain (blue):
[![Feature-Sliced Design][shields-fsd-domain]](https://feature-sliced.github.io/documentation/)

[shields-fsd-domain]: https://img.shields.io/badge/Feature--Sliced-Design?style=for-the-badge&color=F2F2F2&labelColor=262224&logoWidth=10&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABQAAAAaCAYAAAC3g3x9AAAACXBIWXMAAALFAAACxQGJ1n/vAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAABISURBVHgB7dKxCQAgDETR0w2cws0cys2cwhEUBbsggikCuVekDHwSQFlYo7Q+8KnmtHdFWMdk2cl5wSsbxGSZw8dm8pX9ZHUTMBUgGU2F718AAAAASUVORK5CYII=

----

Feature (green):
[![Feature-Sliced Design][shields-fsd-feature]](https://feature-sliced.github.io/documentation/)

[shields-fsd-feature]: https://img.shields.io/badge/Feature--Sliced-Design?style=for-the-badge&labelColor=262224&color=F2F2F2&logoWidth=10&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABQAAAAaCAYAAAC3g3x9AAAACXBIWXMAAALFAAACxQGJ1n/vAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAABISURBVHgB7dKxCQAgDETR00EcwYEc0IEcwUUUBbsggikCuVekDHwSQFlYo/Y88KmktndFWMdk2cl5wSsbxGSZw8dm8pX9ZHUTdIYgGbPdU2QAAAAASUVORK5CYII=
```

</details>

## How can I help?

- 🍰 Use the methodology in your projects and spread the word
- ⭐ Star us on GitHub
- 💬 Join our [Discord](https://discord.gg/S8MzWTUsmp) or [Telegram](https://t.me/feature_sliced) and share your experience or ask questions
- 📝 Suggest improvements to the documentation through PRs

<div align="center">

[![tg](static/img/social/tg.png)](https://t.me/feature_sliced "Telegram chat")

</div>

```

### File: src\shared\ui\index.js
```js
// NOTE: Prefer specific imports for bundle-size decreasing
export * from "./card";
export * from "./section";
export * from "./table";

```

### File: .eslintrc.js
```js
module.exports = {
    env: {
        node: true,
        browser: true,
        es6: true,
    },
    parser: "@typescript-eslint/parser",
    extends: [
        "@eslint-kit/patch",
        "@eslint-kit/base",
        "@eslint-kit/react",
        "prettier",
    ],
    plugins: ["@typescript-eslint"],
    rules: {
        // Sometime harmful =(
        "react/jsx-props-no-spreading": 0,
        // For external links
        "react/jsx-no-target-blank": 2,
        // For perfomance
        "react/jsx-no-bind": [
            2,
            {
                ignoreDOMComponents: true,
                ignoreRefs: true,
                allowArrowFunctions: false,
                allowFunctions: false,
                allowBind: false,
            },
        ],
        "linebreak-style": [2, "unix"],
        "import/no-unresolved": [
            2,
            {
                ignore: [
                    "^@theme",
                    "^@docusaurus/plugin-content-docs/client",
                    "astro:content",
                ],
            },
        ],
        "import/extensions": 0,
        "import/no-extraneous-dependencies": 0,
    },
    settings: {
        "import/resolver": {
            alias: {
                map: [
                    ["@site", "."],
                    [
                        "@docusaurus",
                        "./node_modules/@docusaurus/core/lib/client/exports",
                    ],
                    [
                        "@theme",
                        "./node_modules/@docusaurus/theme-classic/src/theme",
                    ],
                ],
                extensions: [".js", ".jsx", ".json", ".tsx", ".ts"],
            },
        },
    },
};

```

### File: .stylelintrc.js
```js
module.exports = {
    extends: [
        "stylelint-config-recommended",
        "stylelint-config-standard-scss",
        "stylelint-config-recess-order",
    ],
    rules: {
        "color-hex-length": "long",
        "selector-class-pattern": null,
    },
};

```

### File: CHANGELOG.md
```md
# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

<!-- ## [Since last release][since-last-release] -->

## [2.1.0] - 2024-10-31

The new revision of Feature-Sliced Design is here! The main difference with FSD 2.0 is the new approach to decomposition — “pages first”.

### What's “pages-first”?

You do “pages first” by keeping more code in pages. For example, large blocks of UI, forms and data logic that are not reused on other pages should now stay in the slice of the page that they are used in. The division by segments (`ui`, `api`, `model`, etc.) still applies to all this code, and we encourage you to further split and organize code into folders inside of segments — don't just pile all the code into a single file.

In the same way, widgets are no longer just a compositional layer, instead they should also store code that isn't currently needed outside of that widget, including its own stores, business logic, and API interactions.

When you have a need to reuse code in several widgets or pages, consider putting it in Shared. If that code involves business logic (i. e. managing specific modal dialogs), consider breaking it up into infrastructural code, like the modal manager, and the business code, like the content of the modals. The infrastructure can then go to Shared, and the content can stay in the pages that use this infrastructure.

### How is it different?

In FSD 2.0 we explained how to identify entities and features in your application, and then combine them in widgets and pages. Over time we started disliking this approach, mostly for the following reasons: 

- Code cohesion is much worse in this approach
    - You need to jump around several folders just to make changes to a single user flow
    - Unused code is harder to delete because it's somewhere else
- Finding entities and features is still an advanced skill that needs to be developed over time
    - It requires understanding of the business context, which not all developers want to bother with
    - On the other hand, splitting by pages is natural and requires little training
    - Different developers have different understandings of these concepts, which leads to everyone having their own idea of FSD, which causes conflict and misunderstanding

### Is it hard to migrate from FSD 2.0?

This is a non-breaking change, so you don’t even necessarily need to migrate your current FSD projects to FSD 2.1, but we still think the new way of thinking will lead to a more cohesive and less opinionated structure. We’ve compiled a few steps you can take in [the migration guide](https://feature-sliced.github.io/documentation/docs/guides/migration/from-v2-0).

### What else happened since the last release?

The cross-import notation (`@x`) that was an experimental proposal for a long time has now been standardized! Its official name is **Public API for cross-imports**. You can use it to create explicit connections between entities. There's [a new section in our documentation all about this new notation](https://feature-sliced.github.io/documentation/docs/reference/public-api#public-api-for-cross-imports).

Another exciting new thing in the FSD ecosystem is our architectural linter, [Steiger](https://github.com/feature-sliced/steiger). It's still in active development, but it is production-ready.

A couple more minor clarifications to the docs were made as well:

1. Application-aware things like the route constants, the API calls, or company logo, are now explicitly allowed in Shared. Business logic is still not allowed, but these things are not considered to be business logic.
2. Imports between segments in App and Shared were always allowed, but it's been made explicit too.

And here's what happened to the documentation website:

#### Added

- Slightly rewritten and expanded overview page to give some details about FSD right away (#685).
- New partial translations: Korean (#739, #736, #735, #742, #732, #730, #715), Japanese (#728).
- The tutorial was rewritten. Technical details were stripped out, more FSD theory has been added (#665).
- Guides on how to deal with common frontend issues like page layouts (#708), types (#701), authentication (#693).
- Guides on how to use FSD with Nuxt (#710, #689, #683, #679), SvelteKit (#698), Next.js (#699, #664, #644), and TanStack Query (#673).
- A new feedback widget, powered by PushFeedback! Go give it a try and let us know what you think of the new pages (#695).
- Comparison of FSD with Atomic Design (#671).

#### Changed

- The migration guide from a custom architecture (formerly known as "from legacy") has been actualized (#725).

#### Removed

- The decomposition cheatsheet is now unlisted for an undefined period of time. It proved to be more harmful than useful, but maybe it can be saved later (#649).

## [2.0.0] - 2023-10-01

> **Note**  
> This release note is retrospective, meaning that prior to this release, the Feature-Sliced Design project did not keep a changelog. Below is a summary of the most prominent recent changes, but there is no FSD v1. Prior to FSD, there has been a project called ["Feature Slices"](https://feature-sliced.github.io/featureslices.dev/v1.0.html), and it is considered to be the v1 of FSD.

### Deprecated

- The **Processes** layer is now deprecated. If you're using this layer, consider moving the code to the **Features** layer, with the help of the **App** layer if you need to access pages.

### Added

- The docs are now available in the Uzbek language! The translation is a work in progress, so feel free to contribute (#597, #603, #605).
- Layers, slices, and segments now have strict definitions to avoid ambiguity (#547).
- We now have a multi-lingual Discord community! Feel free to join and ask questions in English, Spanish, German, Ukrainian, Russian, and Japanese.
- The Telegram community is now making use of forum topics to enable conversations in multiple languages: English, Spanish, Ukrainian, Russian, Japanese, Kazakh, Uzbek, and Serbian.

### Changed

- The documentation is now English-first. Other languages are, of course, still supported (#509).
- A new decomposition cheatsheet has been released (#627).
- The FAQ section has been updated, outdated questions have been removed (#628).
- The visual depiction of layers has been updated to reflect their folder-based nature (#583).
- The README has been refreshed, now it features official badges that you can use in your projects (#569).
- The pages about naming and knowledge types have been rewritten for clarity (#550, #551).
- The documentation has been thoroughly reorganised. The old URLs will redirect to the right places (#471, #531).
- The first page of the docs is now a helpful index with a prominent first step (#525).
- The overview page has been rewritten to be more concise and informative (#512, #515, #516).
- FSD has updated its branding, and there are now guidelines to the brand usage. The standard spelling of the name is now "Feature-Sliced Design" (#496, #499, #500, #465).

[since-last-release]: https://github.com/feature-sliced/documentation/compare/v2.1.0...HEAD
[2.1.0]: https://github.com/feature-sliced/documentation/releases/tag/v2.1.0
[2.0.0]: https://github.com/feature-sliced/documentation/releases/tag/v2.0.0

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

* Using welcoming and inclusive language
* Being respectful of differing viewpoints and experiences
* Gracefully accepting constructive criticism
* Focusing on what is best for the community
* Showing empathy towards other community members

Examples of unacceptable behavior by participants include:

* The use of sexualized language or imagery and unwelcome sexual attention or
 advances
* Trolling, insulting/derogatory comments, and personal or political attacks
* Public or private harassment
* Publishing others' private information, such as a physical or electronic
 address, without explicit permission
* Other conduct which could reasonably be considered inappropriate in a
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
reported by contacting the project team at . All
complaints will be reviewed and investigated and will result in a response that
is deemed necessary and appropriate to the circumstances. The project team is
obligated to maintain confidentiality with regard to the reporter of an incident.
Further details of specific enforcement policies may be posted separately.

Project maintainers who do not follow or enforce the Code of Conduct in good
faith may face temporary or permanent repercussions as determined by other
members of the project's leadership.

## Attribution

This Code of Conduct is adapted from the [Contributor Covenant][homepage], version 1.4,
available at <https://www.contributor-covenant.org/version/1/4/code-of-conduct.html>

[homepage]: https://www.contributor-covenant.org

For answers to common questions about this code of conduct, see
<https://www.contributor-covenant.org/faq>

```

### File: CODE_OF_CONDUCT.ru.md
```md
# Кодекс Поведения в рамках Соглашения о Контрибьюторах

## Наше обещание

В интересах создания открытой и гостеприимной среды, мы, как контрибьюторы и разработчики, обещаем сделать участие в нашем проекте и нашем сообществе свободным от притеснений опытом для всех, независимо от возраста, телосложения, ограниченности возможностей, этнической принадлежности, половых признаков, гендерной идентичности и ее выражения, уровня опыта, образования, социально-экономического статуса, национальности, внешности, расы, религии или секуальной индентичности и ориентации.

## Наши стандарты

Примеры поведения, способствующего созданию позитивной среды:

* Использование приветливой и корректной лексики
* Уважительное отношение к различным точкам зрения и опыту
* Достойное принятие конструктивной критики
* Уделение особого внимания тому, что наиболее важно для сообщества
* Выражение сострадания по отношению к другим членам сообщества

Примеры неприемлемого поведения участников:

* Использование сексуализированной лексики или изображений, а также проявление нежелательного сексуального внимания или заигрывания
* Троллинг, оскорбительные/пренебрежительные комментарии, а также нападки в сторону личности или политики
* Открытая или скрытая агрессия
* Публикация чужой персональной информации, такой как физический или электронный адрес, без явного разрешения
* Другое поведение, которое может быть расценено как неподобающее в профессиональной среде

## Наши обязанности

Разработчики проекта несут ответственность за прояснение стандартов приемлемого поведения и принятие должных и честных мер в случае проявления неподобающего поведения.

Разработчики проекта имеют право и обязанность удалять, исправлять или отклонять комментарии, коммиты, код, вики-правки, вопросы и другие материалы, которые не соответствуют данному Кодексу Поведения, или блокировать на время или навсегда любого участника, чье поведение разработчики сочтут неподобающим, угрожающим, оскорбительным или опасным.

## Сфера применения

Данный Кодекс Поведения применим как внутри проектного пространства, так и в рамках общественного, когда участник предствляет проект или сообщество. Примеры презентации проекта или сообщества включают в себя использование официального электронного адреса проекта, публикацию через официальный аккаунт в социальной сети или исполнение обязанностей назначенного представителя на онлайн- или оффлайн-мероприятии. Презентация проекта может быть в дальнейшем уточнена и разъяснена разработчиками проекта.

## Урегулирование конфликтов

О проявлениях жестокого, притесняющего или любого другого неприемлемого поведения можно сообщить команде проекта. Все жалобы будут рассмотрены и изучены, а реакция на них будет соответствовать обстоятельствам. Команда проекта обязуется сохранять конфиденциальность заявителя. Дополнительные детали особых способов урегулирования конфликтов могут быть опубликованы отдельно.

Разработчики проекта, которые не следуют Кодексу Поведения или должным образом не приводят в исполнение меры, прописанные в нем, могут столкнуться с временными или постоянными последствиями, определенными другими членами руководства проекта.

## Атрибуция

Данный Кодекс Поведения составлен на основе [Соглашения о Контрибьюторах][homepage], версия 1.4,
доступного по ссылке: [https://www.contributor-covenant.org/version/1/4/code-of-conduct.html](https://www.contributor-covenant.org/version/1/4/code-of-conduct.html)

[homepage]: https://www.contributor-covenant.org

Ответы на наиболее частые вопросы, касающиеся данного Кодекса Поведения, можно найти по ссылке:
[https://www.contributor-covenant.org/faq](https://www.contributor-covenant.org/faq)

```

### File: CONTRIBUTING.md
```md
# Contributing

First of all, thank you for taking the time to contribute to the project! 👍

## How can I help?

[issues]: https://github.com/feature-sliced/documentation/issues
[issues-new]: https://github.com/feature-sliced/documentation/issues/new
[pr]: https://github.com/feature-sliced/documentation/pulls
[pr-new]: https://github.com/feature-sliced/documentation/compare
[disc]: https://github.com/feature-sliced/documentation/discussions
[fork]: https://github.com/feature-sliced/documentation/fork
[actions]: https://github.com/feature-sliced/documentation/actions

<!-- Other emojis: 👁️ , ✍️ , 🔍 -->

- 📢 [Share feedback, ask and **discuss** anything][disc]
   > We will be glad to receive any feedback from you!
- 💡 [Notify about bugs, suggest improvements][issues-new]
   > If something specific doesn't work quite well for you or could be better - let us know!
- 💬 Rate & discuss [**issues**][issues]
   > Share your opinion, evaluate the problem identified by the author
- 🔩 Reproduce complex [**issues**][issues]
   > Some issues are difficult to reproduce
- 🛡️ Provide a review for [**pull requests**][pr]
   > Share your opinion and help us with the processing of other people's proposals
- ⚒️ Suggest  yur [own **pull-requests**!][pr-new]
   > Enhance the project with your own solutions

## Workflow

[self-review-article]: https://blog.beanbaginc.com/2014/12/01/practicing-effective-self-review/

1. [Fork][fork] the repository
2. Make your changes
   - Make sure that **commits follow** the [Conventional Commits specification](https://www.conventionalcommits.org)
      > All this helps with the changelog formation and keeps the history of the project clean
      >
      > *It would also be useful to indicate in each commit (preferably in the body) the ID of the task in the format `#{ID}' (so that there is linking)*
   - Make sure that **all checks pass**

      ```sh
      $ npm run test
      # > Linting is not broken
      # > The build does not crash
      ```

   - To modify/add markdown tables, it is recommended to use ready-made services (for example [this](https://www.tablesgenerator.com/markdown_tables))
3. [Open your pull-request][pr-new] from *your forked branch* and specify related [issues][issues] (if any)
   - Before creating a PR do at least one [`self-review`][self-review-article] of your changes, to save the reviewers' time
   - Also make sure that you describe the problem being solved as clearly as possible (take care of the reviewer) in your PR
      > The more details you provide in the description, the better
      >
      > *You can get acquainted with [what pull-requests were made before you][pr]*
   - If everything is fine, you can ping someone from the core maintainers to speed things up
      > If you have any problems, you can temporarily convert your PR into a draft (see the panel on the right)
      >
      > Or mark the PR title with the prefix 'WIP:`

   - Make sure that the verification via **[CI][actions]** has passed for your PR
      > Our common goal is to reduce review costs and achieve consistency in the code base 🤙

```

### File: declaration.d.ts
```ts
declare module "*.scss" {
    const content: Record<string, string>;
    export default content;
}

declare module "@site/static/img/*" {
    export default string;
}

declare module "@theme/IdealImage" {
    import type { ReactNode } from "react";

    export interface Props {
        readonly className?: string;
        readonly children?: ReactNode;
        readonly img: string;
        readonly alt: string;
    }
    export default function Image(props: Props): JSX.Element;
}

declare module "@docusaurus/plugin-content-docs/client" {
    export interface Version {
        readonly label: string;
        readonly name: string;
    }
    export function useLatestVersion(): Version;
}

```

### File: DEV.md
```md
# Website

This website is built using [Docusaurus 2](https://docusaurus.io/), a modern static website generator.

## i18n

- [Russian docs version](i18n/ru)
- [English docs version](i18n/en)
- [Uzbek docs version](i18n/uz)
- [Japanese docs version](i18n/ja)

## Installation

```bash
pnpm install
```

## Local Development

```bash
pnpm start       # for default locale
pnpm start:ru    # for RU locale
pnpm start:en    # for EN locale
pnpm start:uz    # for UZ locale
pnpm start:ja    # for JA locale
```

> About [docusaurus/i18n commands](https://docusaurus.io/docs/i18n/git#translate-the-files)

This command starts a local development server and opens up a browser window. Most changes are reflected live without having to restart the server.

## Build

```console
pnpm build
```

This command generates static content into the `build` directory and can be served using any static contents hosting service.

## Deployment

```console
GIT_USER=<Your GitHub username> USE_SSH=true pnpm deploy
```

If you are using GitHub pages for hosting, this command is a convenient way to build the website and push to the `gh-pages` branch.

```

### File: docusaurus.config.js
```js
const { themes: prismThemes } = require("prism-react-renderer");
const cfg = require("./config/docusaurus");

/** @typedef {import('@docusaurus/types').Config} Config */

/**
 * Custom fields (for access on code-level)
 * @see https://docusaurus.io/docs/api/docusaurus-config#customfields
 */
const customFields = {
    legacyRoutes: cfg.LEGACY_ROUTES,
    pushFeedbackProjectId: "5i2vbxcpaz",
};

/** @type {Config} */
module.exports = {
    // General
    title: "Feature-Sliced Design",
    tagline: "Architectural methodology for frontend projects",
    organizationName: "feature-sliced", // Usually your GitHub org/user name.
    projectName: "documentation", // Usually your repo name.
    url: cfg.consts.DOMAIN,
    favicon: "img/favicon/classic.png",
    baseUrl: process.env.BASE_URL || "/",
    // Extensions
    i18n: cfg.i18n,
    presets: cfg.presets,
    plugins: cfg.plugins,
    // Build & Dev
    onBrokenLinks: "throw",
    markdown: {
        hooks: {
            onBrokenMarkdownLinks: "throw",
        },
    },
    onDuplicateRoutes: "warn",
    customFields,
    trailingSlash: false,
    // Theme
    themeConfig: {
        image: "img/preview.png",
        // @see https://docusaurus.io/docs/sidebar#hideable-sidebar
        docs: { sidebar: { hideable: true, autoCollapseCategories: true } },
        colorMode: { respectPrefersColorScheme: true },
        navbar: cfg.navbar,
        footer: cfg.footer,
        algolia: cfg.algolia,
        metadata: cfg.metadata,

        imageZoom: {
            selector: ".markdown :not(a) > img",
            options: {
                background: "rgb(255 255 255 / 0.3)",
            },
        },
        prism: {
            theme: prismThemes.oneLight,
            darkTheme: prismThemes.oneDark,
        },
    },
    future: {
        experimental_faster: true,
        v4: {
            removeLegacyPostBuildHeadAttribute: true,
        },
    },
};

// Remove configs if there are not secrets passed
if (!process.env.ALGOLIA_KEY || !process.env.ALGOLIA_ID) {
    delete module.exports.themeConfig.algolia;
}

```

### File: pnpm-workspace.yaml
```yaml
minimumReleaseAge: 1440

onlyBuiltDependencies:
    - "@parcel/watcher"
    - "@swc/core"
    - core-js
    - core-js-pure
    - sharp

```

### File: sandbox.config.json
```json
{
    "infiniteLoopProtection": true,
    "hardReloadOnChange": true,
    "view": "browser",
    "template": "docusaurus",
    "node": "14",
    "container": {
        "node": "14"
    }
}

```

### File: tsconfig.astro.json
```json
{
    "extends": "astro/tsconfigs/strict",
    "include": [".astro/types.d.ts", "src/content.config.ts"],
    "exclude": ["dist", "build"],
    "compilerOptions": {
        "baseUrl": ".",
        "paths": {
            "@/*": ["./src/*"]
        }
    }
}

```

### File: tsconfig.docusaurus.json
```json
{
    "extends": "@docusaurus/tsconfig",
    "compilerOptions": {
        "baseUrl": ".",
        "lib": ["DOM", "ESNext"]
    },
    "exclude": [
        ".astro/types.d.ts",
        "src/content.config.ts",
        "src/content/**",
        "dist",
        "build"
    ]
}

```

### File: tsconfig.json
```json
{
    "files": [],
    "references": [
        {
            "path": "./tsconfig.astro.json"
        },
        {
            "path": "./tsconfig.docusaurus.json"
        }
    ]
}

```

### File: .github\pull_request_template.md
```md
## Background

<!-- 
  Briefly describe what problem this PR is solving. 
  If these changes were previously discussed in an issue or discussion,
  please, leave a reference to it 🔖.
  
  If there is a issue that your PR closes, just write "Closes #ISSUE_NUMBER" (e.g. Closes #42)
  That will automatically close that issue, once PR is merged.
  Please make sure to address all parts of the issue if you write that!
-->




## Changelog

<!-- 
  Briefly describe the proposed changes below. 
  Numbered lists work best. 
  If you add 📷 screenshots or 🎞️ screencasts, you'll be our hero.
-->




<!-- 
  Hi from the Feature-Sliced Design core team! 👋

  Thank you for taking the time to contribute.
  We have a set of guidelines for contibutors that you might want to read:

    https://github.com/feature-sliced/documentation/blob/master/CONTRIBUTING.md

  We encourage self-reviewing the changes before submitting a PR ✅. 
  Here's a nice article that has some pro-tips:

    https://blog.beanbaginc.com/2014/12/01/practicing-effective-self-review/
    
-->

```

### File: blog\2022-06-04-rebranding.md
```md
---
title: 💥 FSD rebranding!
description: FSD 2.0.0-stable rebranding news 🍰
slug: rebranding-stable
authors:
  - name: Ilya Azin
    title: FSD core-team member
    url: https://github.com/azinit
    image_url: https://github.com/azinit.png
tags: [brand, promo]
image: https://feature-sliced.github.io/documentation/img/blog/rebranding-stable.png
hide_table_of_contents: false
---

import useBaseUrl from "@docusaurus/useBaseUrl";

<div class="container text--center margin-vert--md">
    <img src={useBaseUrl("/img/blog/rebranding-stable.png")} alt="logo-primary" width="100%" />
</div>

TLDR:

We've made whole new identity for FSD website and all related projects, feel free to use [brand assets](/docs/branding)

Мы сделали полностью новую айдентику для сайта FSD и всех связанных проектов, не стесняйтесь пользоваться [фирменными ассетами](/docs/branding)

<!--truncate-->

___

For a long time FSD had [inconsistent legacy identity](https://drive.google.com/drive/folders/11Y-3qZ_C9jOFoW2UbSp11YasOhw4yBdl?usp=sharing). Old design was not representing core-concepts of methodology because it was created as a pure draft. After long time it should have been actualized. So, for long-term use, we carefully reworked FSD signature style.

Let's take a deep dive and decompose ideas behind redesign. The light glow on new logo resembles warm brightness of old CRT monitors, passing the idea of a long history of software architecture. Geometry slightly refers to legacy logo to maintain continuity. It also subtly provides the idea of vertical layers and clear boundaries between them. Effects and colors are neutral and friendly to seamlessly pervade any page like FSD can do with projects. Lot of ideas, but, like it works with every good design, they may be seamless.

Long story short, that's what reworked FSD identity is. Modern yet vintage, simple yet meaningful, strict yet notable.

Get all the assets in [brandbook](/docs/branding)

___

Долгое время у FSD была [неконсистентная устаревшая айдентика](https://drive.google.com/drive/folders/11Y-3qZ_C9jOFoW2UbSp11YasOhw4yBdl?usp=sharing). Старый дизайн не передавал ключевые идеи методологии потому что был сделан исключительно как черновик. Спустя много времени пора бы его актуализировать. Итак, для долгосрочного использования мы тщательно переработали фирменный стиль FSD.

Давайте глубоко погрузимся и разложим идеи, лежащие в основе редизайна. Легкое свечение на новом логотипе напоминает теплую яркость старых электронно-лучевых мониторов, передавая идею долгой истории архитектуры программного обеспечения. Геометрия слегка отсылает к устаревшему логотипу, чтобы сохранить преемственность. Она также тонко намекает на идею вертикальных слоев и четких границ между ними. Эффекты и цвета нейтральны и дружелюбны, чтобы беспрепятственно проникать на любую страницу, как это делает FSD с проектами. Много идей, но, как это должно быть с любым хорошим дизайном, они незаметны.

Кратко говоря, это и есть переработанная айдентика FSD. Современная, но винтажная; простая, но содержательная; строгая, но заметная.

Все ассеты можно скачать в [брендбуке](/docs/branding)

```

### File: blog\2022-07-25-international-community.md
```md
---
title: 🌎 FSD international community
description: FSD international community announcement
slug: international-community
authors:
- name: Anton Medvedev
  title: FSD core-team member
  url: https://github.com/unordinarity
  image_url: https://github.com/unordinarity.png
tags: [community, discord, promo]
image: https://feature-sliced.github.io/documentation/img/blog/international-community.png
hide_table_of_contents: false
---

import useBaseUrl from "@docusaurus/useBaseUrl";

<div class="container text--center margin-vert--md">
    <img src={useBaseUrl("/img/blog/international-community.png")} alt="post-cover" width="100%" />
</div>

TLDR:

FSD goes out into the world, and the beginning of this is the international [Discord-server](https://discord.gg/S8MzWTUsmp)

FSD выходит в мир, и началом послужит международный [Discord-сервер](https://discord.gg/S8MzWTUsmp)

<!--truncate-->

___

FSD methodology has passed a long way from Feature-Driven and Atomic Design to the current state (2.0 version). We, the original authors of FSD, are mostly Russian native speakers, and it was easy for us to gather the same Russian-speaking Frontend developers around methodology. Telegram chat was a hub for our community, also in Russian. Over time, developers from all over the world began to learn about the methodology, and we faced difficulties. A simple chat was no longer enough for many people, it was uncomfortable to communicate in one huge space. We decided that this is the perfect moment to expand the community.

The new Discord server will give everyone the opportunity to speak out, regardless of their experience with FSD, opinions about the software architecture, preferred method of communication and language. Now you can exchange experiences and opinions in our large but cozy community. [You are invited.](https://discord.gg/S8MzWTUsmp)

___

Методология FSD прошла долгий путь от Feature-Driven и Atomic Design до текущего состояния (2.0 версии). Мы, изначальные авторы FSD - по большей части носители русского языка, и нам было проще собирать вокруг методологии таких же русскоговорящих Frontend-разработчиков. Хабом для нашего сообщества был Telegram-чат, тоже русскоязычный. Со временем о методологии стали узнавать разработчики со всего мира, и мы столкнулись со сложностями. Простого чата перестало хватать для множества самых разных людей, многим было некомфортно общаться в одном огромном пространстве. Мы решили, что это и есть идеальный момент расширить сообщество.

Новый Discord-сервер даст каждому возможность высказаться, независимо от опыта работы с FSD, мнения об архитектуре ПО, предпочитаемого способа общения и языка. Теперь обменяться опытом и мнением можно в нашем большом, но уютном сообществе. [Вы приглашены.](https://discord.gg/S8MzWTUsmp)

```

### File: src\content.config.ts
```ts
import { defineCollection } from "astro:content";
import { docsLoader } from "@astrojs/starlight/loaders";
import { docsSchema } from "@astrojs/starlight/schema";

export const collections = {
    docs: defineCollection({ loader: docsLoader(), schema: docsSchema() }),
};

```

### File: static\llms-full.txt
```txt
This file is generated at build time. See /docs/llms for details.


```

### File: static\llms.txt
```txt
This file is generated at build time. See /docs/llms for details.


```

### File: static\robots.txt
```txt
User-agent: *
Disallow:

Sitemap: https://feature-sliced.github.io/documentation/sitemap.xml

```

### File: src\styles\custom.css
```css
:root {
    /* Layout */
    --sl-content-width: 55rem; /* default: 45rem */
    --sl-font: system-ui, sans-serif;
}

:root,
:root[data-theme="dark"] {
    --sl-color-accent-low: #102a4d;
    --sl-color-accent: #3193ff;
    --sl-color-accent-high: #b8dcff;
    --sl-color-white: #ffffff;
    --sl-color-gray-1: #f1f5f9;
    --sl-color-gray-2: #e2e8f0;
    --sl-color-gray-3: #94a3b8;
    --sl-color-gray-4: #64748b;
    --sl-color-gray-5: #1e293b;
    --sl-color-gray-6: #172033;
    --sl-color-black: #0f172a;
}

:root[data-theme="light"] {
    --sl-color-accent-low: #dbeafe;
    --sl-color-accent: #3193ff;
    --sl-color-accent-high: #004080;
    --sl-color-white: #0f172a;
    --sl-color-gray-1: #334155;
    --sl-color-gray-2: #475569;
    --sl-color-gray-3: #64748b;
    --sl-color-gray-4: #94a3b8;
    --sl-color-gray-5: #cbd5e1;
    --sl-color-gray-6: #e2e8f0;
    --sl-color-gray-7: #f1f5f9;
    --sl-color-black: #ffffff;
}

:root[data-theme="dark"] [data-theme-only="light"],
:root[data-theme="light"] [data-theme-only="dark"] {
    display: none;
}

```

### File: src\pages\examples\_config.ts
```ts
import type { Example } from "@site/src/entities/example";

export const VERSIONS = {
    V0: "v0",
    V1: "v1",
    V2: "v2",
};

// Currently not accepting any more examples!
export const examples: Example[] = [
    {
        title: "Cardbox",
        description: "The best solutions from developers in one place",
        source: "https://github.com/cardbox/frontend",
        preview: require("./img/cardbox.png"),
        version: VERSIONS.V2,
        updatedAt: "2021-11-12",
        tech: ["react", "effector"],
    },
    {
        title: "Github Client",
        description: "React & GraphQL powered github web-client",
        source: "https://github.com/ani-team/github-client/tree/workshop/feature-sliced-next",
        preview: require("./img/github-client.png"),
        version: VERSIONS.V2,
        updatedAt: "2023-04-26",
        tech: ["react", "graphql", "antd"],
    },
    {
        title: "Todo App (React+Effector)",
        description:
            "QuickStart todo-app example for React developers (Effector version)",
        website: "https://7b64m.csb.app/",
        source: "https://github.com/feature-sliced/examples/tree/master/todo-app",
        preview: require("./img/todo-app-react-effector.png"),
        version: VERSIONS.V2,
        updatedAt: "2021-07-05",
        tech: ["react", "effector", "antd"],
    },
    {
        title: "Todo App (React+Redux)",
        description:
            "QuickStart todo-app example for React developers (Redux version)",
        source: "https://github.com/EliseyMartynov/fs-rtk",
        preview: require("./img/todo-app-react-redux.png"),
        version: VERSIONS.V2,
        updatedAt: "2022-09-06",
        tech: ["react", "redux", "antd"],
    },
    {
        title: "Todo App (Vue 3)",
        description: "QuickStart todo-app example for Vue developers",
        source: "https://github.com/EliseyMartynov/fs-vue",
        preview: require("./img/todo-app-vue.png"),
        version: VERSIONS.V2,
        updatedAt: "2021-12-27",
        tech: ["vue", "vuex", "antd"],
    },
    {
        title: "Todo App (Angular 13)",
        description: "QuickStart todo-app example for Angular developers",
        website: "https://angular-feature-sliced-architecture.netlify.app/",
        source: "https://github.com/Affiction/angular-feature-sliced",
        preview: require("./img/todo-app-angular.png"),
        version: VERSIONS.V2,
        updatedAt: "2022-01-31",
        tech: ["angular", "rxjs"],
    },
    {
        title: "Sharead (demo)",
        description: "Book Marketplace",
        website: "https://dev-sharead.netlify.app/",
        source: "https://github.com/select-name/sharead-frontend",
        preview: require("./img/sharead.png"),
        version: VERSIONS.V2,
        updatedAt: "2021-11-06",
        tech: ["react", "effector", "antd"],
    },
    {
        title: "Projentry (demo)",
        description: "Assistant for your projects",
        website: "https://projentry.netlify.app/",
        source: "https://github.com/ani-team/projentry",
        preview: require("./img/projentry.png"),
        version: VERSIONS.V2,
        updatedAt: "2021-11-06",
        tech: ["react", "antd"],
    },
    {
        title: "Loripsum generator",
        description: "Simple fish text generator",
        website: "https://loripsum-generator.vercel.app",
        source: "https://github.com/yesnoruly/loripsum-generator",
        preview: require("./img/loripsum-generator.png"),
        version: VERSIONS.V2,
        updatedAt: "2021-11-17",
        tech: ["react", "effector"],
    },
    {
        title: "Cast",
        description: "A podcast listening PWA with automated quality assurance",
        website: "https://cast-iu.pages.dev/",
        source: "https://github.com/aabounegm/cast",
        preview: require("./img/cast.png"),
        version: VERSIONS.V2,
        updatedAt: "2022-05-31",
        tech: ["svelte"],
    },
    {
        title: "Draw, I'll Help",
        description: "A drawing app with shape correction powered by ML",
        website: "https://illright.github.io/draw-ill-help/",
        source: "https://github.com/illright/draw-ill-help",
        preview: require("./img/draw-ill-help.png"),
        version: VERSIONS.V2,
        updatedAt: "2022-06-13",
        tech: ["svelte"],
    },
    {
        title: "Rastrr",
        description: "A simple and free graphic editor for novice artists",
        website: "https://rastrr.ru",
        source: "https://github.com/rastrr-editor/client",
        preview: require("./img/rastrr-editor.png"),
        version: VERSIONS.V2,
        updatedAt: "2023-03-25",
        tech: ["svelte"],
    },
    {
        title: "Todo App (ReactNative+Redux)",
        description:
            "QuickStart todo-app example for ReactNative(Expo) developers",
        source: "https://github.com/berdimyradov/fs-rn-todo-app",
        preview: require("./img/fs-rn-todo-app.png"),
        version: VERSIONS.V2,
        updatedAt: "2023-03-27",
        tech: ["react-native", "expo", "redux"],
    },
    {
        title: "Simple Greenhouse App (React+MobX)",
        description:
            "Simple demonstration of how FSD can be implemented with TypeScript, React.js, MobX and Firebase",
        source: "https://github.com/NIRumiantsev/feature-sliced-design",
        preview: require("./img/greenhouse.png"),
        version: VERSIONS.V2,
        updatedAt: "2023-04-17",
        tech: ["react", "mobx", "typescript", "firebase", "mui", "vite"],
    },
    {
        title: "Nukeapp (React+ReduxToolkit)",
        description: "Shopping app build on React/ReduxToolkit stack",
        website: "https://nukeapp.netlify.app/",
        source: "https://github.com/noveogroup-amorgunov/nukeapp",
        preview: require("./img/nukeapp.png"),
        version: VERSIONS.V2,
        updatedAt: "2023-04-24",
        tech: ["react", "redux-toolkit", "typescript", "vite"],
    },
    {
        title: "Sudoku (React+Effector)",
        description: "A simple crossword of numbers on effector / fsd",
        website: "https://sudoku-effector.pages.dev/",
        source: "https://github.com/Shiyan7/sudoku-effector",
        preview: require("./img/sudoku.png"),
        version: VERSIONS.V2,
        updatedAt: "2023-06-08",
        tech: [
            "react",
            "effector",
            "typescript",
            "vite",
            "tailwind",
            "atomic-router",
        ],
    },
    {
        title: "Kinomore (React+Effector)",
        description: "Large project on the effector/fsd stack",
        website: "https://kinomore.netlify.app/",
        source: "https://github.com/Shiyan7/kinomore-v2",
        preview: require("./img/kinomore.png"),
        version: VERSIONS.V2,
        updatedAt: "2023-07-10",
        tech: [
            "react",
            "effector",
            "typescript",
            "nextjs",
            "react-testing-library",
        ],
    },
    {
        title: "Conduit",
        description:
            "A social blogging site powered by Feature-Sliced Design architectural methodology.",
        website: "https://realworld-fsd.netlify.app/",
        source: "https://github.com/sldk-yuri/realworld-react-fsd",
        preview: require("./img/conduit.png"),
        version: VERSIONS.V2,
        updatedAt: "2023-06-21",
        tech: [
            "react",
            "react-router",
            "react-query",
            "zustand",
            "webpack",
            "typescript",
        ],
    },
    {
        title: "Todo app (Vue 3 + Pinia)",
        description:
            "QuickStart todo-app example for Vue developers with pinia store",
        website: "https://fsd-tasks.netlify.app/",
        source: "https://github.com/hoach-linux/fsd-vue-antd",
        preview: require("./img/todo-vue-pinia.png"),
        version: VERSIONS.V2,
        updatedAt: "2023-010-12",
        tech: ["vue 3", "pinia", "vite", "typescript"],
    },
    {
        title: "E-Commerce",
        description:
            "This project is an online store built using React. It provides the ability to view the product catalog and product pages",
        website: "https://ruslan4432013.github.io/e-commerce-kts/",
        source: "https://github.com/ruslan4432013/e-commerce-kts",
        preview: require("./img/e-commerce.png"),
        version: VERSIONS.V2,
        updatedAt: "2023-09-09",
        tech: ["react", "mobx", "webpack", "typescript", "ssr"],
    },
    {
        title: "Money Flow",
        description:
            "A mobile application for tracking your expenses and incomes.",
        source: "https://github.com/moneyflow-dev/moneyflow",
        preview: require("./img/moneyflow.png"),
        version: VERSIONS.V2,
        updatedAt: "2023-09-07",
        tech: [
            "capacitorjs",
            "react",
            "react-router",
            "zustand",
            "vite",
            "typescript",
            "mobile",
            "android",
            "ios",
        ],
    },
    {
        title: "Сryptolight",
        description:
            "Cryptocurrency review site based on Feature-Sliced Design (Architectural methodology for frontend projects).",
        website: "http://crypto-light.space/",
        source: "https://github.com/Yar56/cryptolight",
        preview: require("./img/cryptolight.png"),
        version: VERSIONS.V2,
        updatedAt: "2023-10-18",
        tech: ["react", "effector", "nextui", "typescript", "vite"],
    },
    {
        title: "VK Audiopad",
        description: "Chrome extension for VK Music",
        website:
            "https://chrome.google.com/webstore/detail/plclpmphdjmdgmdpfkcmdkmohgpfecip",
        source: "https://github.com/vissh/vkui-audiopad",
        preview: require("./img/vkaudiopad.png"),
        version: VERSIONS.V2,
        updatedAt: "2023-11-25",
        tech: ["react", "vkui", "typescript"],
    },
    {
        title: "Fake Cyber Web Store",
        description: "Example web store on Vue3",
        website: "https://akosogorov.github.io/fake-cyber-web-store/",
        source: "https://github.com/AKosogorov/fake-cyber-web-store",
        preview: require("./img/fake-cyber-web-store.jpg"),
        version: VERSIONS.V2,
        updatedAt: "2023-07-26",
        tech: [
            "vue3",
            "pinia",
            "typescript",
            "firebase",
            "vue-router",
            "eslint",
            "prettier",
            "vite",
        ],
    },
    {
        title: "Polka",
        description:
            "The application is a bookshelf where you can add your favorite books. The application works with the Google Books API.",
        website: "https://polka-fsd.netlify.app/",
        source: "https://github.com/lollipopfly/polka",
        preview: require("./img/polka.jpg"),
        version: VERSIONS.V2,
        updatedAt: "2023-12-06",
        tech: [
            "vue3",
            "pinia",
            "typescript",
            "vue-router",
            "eslint",
            "prettier",
            "vite",
            "vuetify",
        ],
    },
    {
        title: "FalkChat",
        description:
            "FalkChat is your go-to destination for seamless and engaging online conversations.",
        website: "https://chat.falkomer.tech",
        version: VERSIONS.V2,
        updatedAt: "2023-12-21",
        source: "https://github.com/falkomerr/falkchat",
        preview: require("./img/falkchat.png"),
        tech: [
            "react",
            "next",
            "prettier",
            "clerk",
            "typescript",
            "tailwind",
            "shadcn/ui",
            "zustand",
        ],
    },
    {
        title: "Posts (React Query example)",
        description:
            "Example of using FSD with React Query (Mutation, Query, Pagination)",
        website: "https://fsd-react-query-example.vercel.app/",
        version: VERSIONS.V2,
        updatedAt: "2024-02-25",
        source: "https://github.com/ruslan4432013/fsd-react-query-example",
        preview: require("./img/react-query-example.png"),
        tech: ["react", "react-query", "typescript", "material ui"],
    },
    {
        title: "Moonlogs (Effector + Forest example)",
        description:
            "Moonlogs is a business-event logging tool with a built-in user-friendly web interface for easy access to events",
        version: VERSIONS.V2,
        updatedAt: "2024-03-06",
        source: "https://github.com/pijng/moonlogs",
        preview: require("./img/moonlogs.png"),
        tech: ["forest", "effector", "tailwind", "typescript", "go"],
    },
    {
        title: "Moke Smoke (React Native example)",
        description:
            "An application that helps you quit smoking, published in the App Store and Google. Developed with React Native",
        version: VERSIONS.V2,
        updatedAt: "2024-03-31",
        website: "https://dontsmoke.vasyl.site",
        source: "https://github.com/penteleichuk/Moke-Smoke",
        preview: require("./img/moke-smoke.jpg"),
        tech: ["react", "rtk", "persist", "typescript", "firebase"],
    },
    {
        title: "IT bookstore",
        description:
            "Catalog for viewing and searching information technology books",
        website: "https://umttikhinadasha.github.io/IT-Bookstore/",
        version: VERSIONS.V2,
        updatedAt: "2024-03-28",
        source: "https://github.com/UmttikhinaDasha/IT-Bookstore",
        preview: require("./img/it-bookstore.png"),
        tech: [
            "react",
            "redux toolkit",
            "typescript",
            "react router",
            "vite",
            "scss",
        ],
    },
    {
        title: "Roke.to dApp",
        description:
            "A crypto streaming service which allows paying people by the second",
        website: "https://app2.roke.to/",
        version: VERSIONS.V2,
        updatedAt: "2024-06-07",
        source: "https://github.com/roke-to/roketo-ui",
        preview: require("./img/roketo.jpg"),
        tech: ["react", "effector", "tailwindcss"],
    },
    {
        title: "Roke.to Business",
        description:
            "Business branch of Roketo, a crypto streaming service which allows paying people by the second",
        version: VERSIONS.V2,
        updatedAt: "2024-06-07",
        source: "https://github.com/roke-to/roketo-business-ui",
        preview: require("./img/roketo-business.jpg"),
        tech: ["react", "effector", "tailwindcss", "turbo"],
    },
    {
        title: "Tiny Bunny Mini Game",
        description:
            'Mini-game "21 points" in the universe of the visual novel "Tiny Bunny".',
        source: "https://github.com/sanua356/tiny-bunny",
        website: "https://sanua356.github.io/tiny-bunny/",
        preview: require("./img/tiny-bunny.png"),
        version: VERSIONS.V2,
        updatedAt: "2024-08-10",
        tech: ["react", "redux-toolkit", "typescript"],
  
... [TRUNCATED]
```


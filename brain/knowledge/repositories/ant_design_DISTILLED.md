---
id: repo-fetched-ant-design-121849
type: knowledge
owner: OA
registered_at: 2026-04-05T03:19:59.238283
tags: ["auto-cloned", "oa-assimilated"]
---

# FETCHED_ant-design_121849

## Assimilation Report
Auto-cloned repository: FETCHED_ant-design_121849

## Application for OmniClaw
No structural integration blueprint provided.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
<div align="center"><a name="readme-top"></a>

<img height="180" src="https://gw.alipayobjects.com/zos/rmsportal/KDpgvguMpGfqaHPjicRK.svg">

<h1>Ant Design</h1>

An enterprise-class UI design language and React UI library.

[![CI status][github-action-image]][github-action-url] [![codecov][codecov-image]][codecov-url] [![NPM version][npm-image]][npm-url] [![NPM downloads][download-image]][download-url] [![][bundlephobia-image]][bundlephobia-url] [![][jsdelivr-image]][jsdelivr-url]

[![Follow Twitter][twitter-image]][twitter-url] [![dumi][dumi-image]][dumi-url] [![FOSSA Status][fossa-image]][fossa-url] [![Issues need help][help-wanted-image]][help-wanted-url] [![LFX Active Contributors][lfx-image]][lfx-url]

[Changelog](./CHANGELOG.en-US.md) · [Report Bug][github-issues-url] · [Request Feature][github-issues-url] · English · [中文](./README-zh_CN.md)

## ❤️ Sponsors [![](https://opencollective.com/ant-design/tiers/sponsors/badge.svg?label=Sponsors&color=brightgreen)](https://opencollective.com/ant-design/contribute/sponsors-218)

<a href="https://tractian.com"><img src="https://images.opencollective.com/tractian/0235da9/logo/256.png" width="128" height="128" alt="TRACTIAN"></a>
<a href="https://lobehub.com"><img src="https://unpkg.com/@lobehub/icons-static-svg@1.79.0/icons/lobehub-color.svg" width="128" height="128" alt="LobeHub"></a>
<a href="https://youmind.com"><img src="https://marketing-assets.youmind.com/logo-512.png" width="128" height="128" alt="YouMind"></a>

[npm-image]: https://img.shields.io/npm/v/antd.svg?style=flat-square
[npm-url]: https://npmjs.org/package/antd
[github-action-image]: https://github.com/ant-design/ant-design/actions/workflows/test.yml/badge.svg
[github-action-url]: https://github.com/ant-design/ant-design/actions/workflows/test.yml
[codecov-image]: https://img.shields.io/codecov/c/github/ant-design/ant-design/master.svg?style=flat-square
[codecov-url]: https://codecov.io/gh/ant-design/ant-design/branch/master
[download-image]: https://img.shields.io/npm/dm/antd.svg?style=flat-square
[download-url]: https://npmjs.org/package/antd
[fossa-image]: https://app.fossa.io/api/projects/git%2Bgithub.com%2Fant-design%2Fant-design.svg?type=shield
[fossa-url]: https://app.fossa.io/projects/git%2Bgithub.com%2Fant-design%2Fant-design?ref=badge_shield
[help-wanted-image]: https://img.shields.io/github/issues/ant-design/ant-design/help%20wanted?color=green&style=flat-square
[help-wanted-url]: https://github.com/ant-design/ant-design/issues?q=is%3Aopen+is%3Aissue+label%3A%22help+wanted%22
[twitter-image]: https://img.shields.io/twitter/follow/AntDesignUI.svg?label=Ant%20Design
[twitter-url]: https://twitter.com/AntDesignUI
[jsdelivr-image]: https://data.jsdelivr.com/v1/package/npm/antd/badge
[jsdelivr-url]: https://www.jsdelivr.com/package/npm/antd
[bundlephobia-image]: https://img.shields.io/bundlephobia/minzip/antd?style=flat-square
[bundlephobia-url]: https://bundlephobia.com/package/antd
[dumi-image]: https://img.shields.io/badge/docs%20by-dumi-blue?style=flat-square
[dumi-url]: https://github.com/umijs/dumi
[github-issues-url]: https://new-issue.ant.design
[lfx-image]: https://insights.linuxfoundation.org/api/badge/active-contributors?project=ant-design-ant-design&repos=https://github.com/ant-design/ant-design
[lfx-url]: https://insights.linuxfoundation.org/project/ant-design-ant-design/repository/ant-design-ant-design

</div>

[![](https://user-images.githubusercontent.com/507615/209472919-6f7e8561-be8c-4b0b-9976-eb3c692aa20a.png)](https://ant.design)

## ✨ Features

- 🌈 Enterprise-class UI designed for web applications.
- 📦 A set of high-quality React components out of the box.
- 🛡 Written in TypeScript with predictable static types.
- ⚙️ Whole package of design resources and development tools.
- 🌍 Internationalization support for dozens of languages.
- 🎨 Powerful theme customization based on CSS-in-JS.

## 🖥 Environment Support

- Modern browsers
- Server-side Rendering
- [Electron](https://www.electronjs.org/)

| [<img src="https://raw.githubusercontent.com/alrra/browser-logos/master/src/edge/edge_48x48.png" alt="Edge" width="24px" height="24px" />](https://godban.github.io/browsers-support-badges/)<br>Edge | [<img src="https://raw.githubusercontent.com/alrra/browser-logos/master/src/firefox/firefox_48x48.png" alt="Firefox" width="24px" height="24px" />](https://godban.github.io/browsers-support-badges/)<br>Firefox | [<img src="https://raw.githubusercontent.com/alrra/browser-logos/master/src/chrome/chrome_48x48.png" alt="Chrome" width="24px" height="24px" />](https://godban.github.io/browsers-support-badges/)<br>Chrome | [<img src="https://raw.githubusercontent.com/alrra/browser-logos/master/src/safari/safari_48x48.png" alt="Safari" width="24px" height="24px" />](https://godban.github.io/browsers-support-badges/)<br>Safari | [<img src="https://raw.githubusercontent.com/alrra/browser-logos/master/src/electron/electron_48x48.png" alt="Electron" width="24px" height="24px" />](https://godban.github.io/browsers-support-badges/)<br>Electron |
| --- | --- | --- | --- | --- |
| Edge | last 2 versions | last 2 versions | last 2 versions | last 2 versions |

## 📦 Install

```bash
npm install antd
```

```bash
yarn add antd
```

```bash
pnpm add antd
```

```bash
bun add antd
```

## 🔨 Usage

```tsx
import { Button, DatePicker } from 'antd';

export default () => (
  <>
    <Button type="primary">PRESS ME</Button>
    <DatePicker placeholder="select date" />
  </>
);
```

## 🔗 Links

- [Home page](https://ant.design/)
- [Components Overview](https://ant.design/components/overview)
- [Sponsor](https://ant.design/docs/react/sponsor)
- [Change Log](CHANGELOG.en-US.md)
- [rc-components](https://react-component.github.io/)
- [🆕 Ant Design X](https://x.ant.design/index-cn)
- [Ant Design Pro](https://pro.ant.design/)
- [Pro Components](https://procomponents.ant.design)
- [Ant Design Mobile](https://mobile.ant.design)
- [Ant Design Mini](https://mini.ant.design)
- [Ant Design Charts](https://charts.ant.design)
- [Ant Design Web3](https://web3.ant.design)
- [Landing Pages](https://landing.ant.design)
- [Ant Motion](https://motion.ant.design)
- [Scaffold Market](https://scaffold.ant.design)
- [Developer Instruction](https://github.com/ant-design/ant-design/wiki/Development)
- [Versioning Release Note](https://github.com/ant-design/ant-design/wiki/%E8%BD%AE%E5%80%BC%E8%A7%84%E5%88%99%E5%92%8C%E7%89%88%E6%9C%AC%E5%8F%91%E5%B8%83%E6%B5%81%E7%A8%8B)
- [FAQ](https://ant.design/docs/react/faq)
- [Online Playground](https://u.ant.design/reproduce) for bug reports
- [Customize Theme](https://ant.design/docs/react/customize-theme)
- [How to Apply for Being A Collaborator](https://github.com/ant-design/ant-design/wiki/Collaborators#how-to-apply-for-being-a-collaborator)

## ⌨️ Development

Use [opensumi.run](https://opensumi.run), a free online pure front-end dev environment.

[![opensumi.run](https://custom-icon-badges.demolab.com/badge/opensumi-run-blue.svg?logo=opensumi)](https://opensumi.run/ide/ant-design/ant-design)

Or clone locally:

```bash
$ git clone git@github.com:ant-design/ant-design.git
$ cd ant-design
$ npm install
$ npm start
```

Open your browser and visit http://127.0.0.1:8001, see more at [Development](https://github.com/ant-design/ant-design/wiki/Development).

## 🤝 Contributing [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](https://makeapullrequest.com)

<table>
<tr>
  <td>
    <a href="https://next.ossinsight.io/widgets/official/compose-recent-top-contributors?repo_id=34526884" target="_blank" style="display: block" align="center">
      <picture>
        <source media="(prefers-color-scheme: dark)" srcset="https://next.ossinsight.io/widgets/official/compose-recent-top-contributors/thumbnail.png?repo_id=34526884&image_size=auto&color_scheme=dark" width="280">
        <img alt="Top Contributors of ant-design/ant-design - Last 28 days" src="https://next.ossinsight.io/widgets/official/compose-recent-top-contributors/thumbnail.png?repo_id=34526884&image_size=auto&color_scheme=light" width="280">
      </picture>
    </a>
  </td>
  <td rowspan="2">
    <a href="https://next.ossinsight.io/widgets/official/compose-last-28-days-stats?repo_id=34526884" target="_blank" style="display: block" align="center">
      <picture>
        <source media="(prefers-color-scheme: dark)" srcset="https://next.ossinsight.io/widgets/official/compose-last-28-days-stats/thumbnail.png?repo_id=34526884&image_size=auto&color_scheme=dark" width="655" height="auto">
        <img alt="Performance Stats of ant-design/ant-design - Last 28 days" src="https://next.ossinsight.io/widgets/official/compose-last-28-days-stats/thumbnail.png?repo_id=34526884&image_size=auto&color_scheme=light" width="655" height="auto">
      </picture>
    </a>
  </td>
</tr>
<tr>
  <td>
    <a href="https://next.ossinsight.io/widgets/official/compose-org-active-contributors?period=past_28_days&activity=new&owner_id=12101536&repo_ids=34526884" target="_blank" style="display: block" align="center">
      <picture>
        <source media="(prefers-color-scheme: dark)" srcset="https://next.ossinsight.io/widgets/official/compose-org-active-contributors/thumbnail.png?period=past_28_days&activity=new&owner_id=12101536&repo_ids=34526884&image_size=2x3&color_scheme=dark" width="273" height="auto">
        <img alt="New participants of ant-design - past 28 days" src="https://next.ossinsight.io/widgets/official/compose-org-active-contributors/thumbnail.png?period=past_28_days&activity=new&owner_id=12101536&repo_ids=34526884&image_size=2x3&color_scheme=light" width="273" height="auto">
      </picture>
    </a>
  </td>
</tr>
</table>

<a href="https://openomy.app/github/ant-design/ant-design" target="_blank" style="display: block; width: 100%;" align="center">
  <img src="https://openomy.app/svg?repo=ant-design/ant-design&chart=bubble&latestMonth=3" target="_blank" alt="Contribution Leaderboard" style="display: block; width: 100%;" />
</a>

Let's build a better antd together.

We warmly invite contributions from everyone. Before you get started, please take a moment to review our [Contribution Guide](https://ant.design/docs/react/contributing). Feel free to share your ideas through [Pull Requests](https://github.com/ant-design/ant-design/pulls) or [GitHub Issues](https://github.com/ant-design/ant-design/issues). If you're interested in enhancing our codebase, explore the [Development Instructions](https://github.com/ant-design/ant-design/wiki/Development) and enjoy your coding journey! :)

For collaborators, adhere to our [Pull Request Principle](https://github.com/ant-design/ant-design/wiki/PR-principle) and utilize our [Pull Request Template](https://github.com/ant-design/ant-design/wiki/PR-principle#pull-request-template) when creating a Pull Request.

## Issue funding

We use [Issuehunt](https://issuehunt.io/repos/3452688) to up-vote and promote specific features that you would like to see and implement. Check our backlog and help us:

[![Let's fund issues in this repository](https://raw.githubusercontent.com/BoostIO/issuehunt-materials/master/v1/issuehunt-button-v1.svg)](https://issuehunt.io/repos/34526884)

## ❤️ Backers [![](https://opencollective.com/ant-design/tiers/backers/badge.svg?label=Backers&color=brightgreen)](https://opencollective.com/ant-design#support)

[![](https://opencollective.com/ant-design/tiers/backers.svg?avatarHeight=72)](https://opencollective.com/ant-design/contribute/backers-217/checkout)

```

### File: AGENTS.md
```md
CLAUDE.md
```

### File: CHANGELOG.en-US.md
```md
---
order: 6
title: Changelog
timeline: true
tag: vVERSION
---

`antd` follows [Semantic Versioning 2.0.0](http://semver.org/).

#### Release Schedule

- Weekly release: patch version at the end of every week for routine bugfixes (anytime for an urgent bugfix).
- Monthly release: minor version at the end of every month for new features.
- Major version release is not included in this schedule for breaking changes and new features.

---

## 6.3.5

`2026-03-30`

- 🐞 Fix Image preview action buttons not resetting native button styles. [#57491](https://github.com/ant-design/ant-design/pull/57491) [@QDyanbing](https://github.com/QDyanbing)
- 🐞 Fix TimePicker column cannot scroll directly on touch devices. [#57468](https://github.com/ant-design/ant-design/pull/57468) [@afc163](https://github.com/afc163)
- 🐞 MISC: Fix Icon not being centered in certain scenarios. [#57460](https://github.com/ant-design/ant-design/pull/57460) [@QDyanbing](https://github.com/QDyanbing)

## 6.3.4

`2026-03-24`

- 🔥 Add [`@ant-design/cli`](https://www.npmjs.com/package/@ant-design/cli) official command-line tool for querying Ant Design component knowledge, analyzing project usage, and guiding migrations offline. [#57413](https://github.com/ant-design/ant-design/pull/57413) [@afc163](https://github.com/afc163)
- 🐞 Fix Form.List losing sibling field values when using `onValuesChange`. [#57399](https://github.com/ant-design/ant-design/pull/57399) [@zombieJ](https://github.com/zombieJ)
- 🐞 Fix missing `screenXXXLMin` in `useToken` causing incorrect antd.css to be generated. [#57372](https://github.com/ant-design/ant-design/pull/57372) [@sealye09](https://github.com/sealye09)
- 🐞 Fix ConfigProvider component config typings to expose semantic `classNames` and `styles` for supported components. [#57396](https://github.com/ant-design/ant-design/pull/57396) [@QDyanbing](https://github.com/QDyanbing)
- 🐞 Fix Image `fetchPriority` prop not being passed through to the `<img>` element. [#57392](https://github.com/ant-design/ant-design/pull/57392) [@aojunhao123](https://github.com/aojunhao123)
- Menu
  - 🐞 Fix Menu SubMenu parent item not applying custom hover color via ConfigProvider. [#57374](https://github.com/ant-design/ant-design/pull/57374) [@EmilyyyLiu](https://github.com/EmilyyyLiu)
  - 🐞 Fix Menu collapsed icons appearing misaligned when customizing `collapsedIconSize`. [#57360](https://github.com/ant-design/ant-design/pull/57360) [@QDyanbing](https://github.com/QDyanbing)
- 🐞 Fix Table controlled popover in column title being rendered twice when scroll is enabled. [#57342](https://github.com/ant-design/ant-design/pull/57342) [@QDyanbing](https://github.com/QDyanbing)
- 🐞 Fix Transfer `render` prop returning JSX elements causing search to fail. [#57133](https://github.com/ant-design/ant-design/pull/57133) [@WustLCQ](https://github.com/WustLCQ)
- 🐞 Fix Tree custom `switcherIcon` missing `switcher-line-icon` className when `showLine` is enabled. [#57303](https://github.com/ant-design/ant-design/pull/57303) [@QDyanbing](https://github.com/QDyanbing)
- 🐞 Fix Watermark TypeScript errors when `onRemove` is omitted. [#57344](https://github.com/ant-design/ant-design/pull/57344) [@QDyanbing](https://github.com/QDyanbing)

## 6.3.3

`2026-03-16`

- Image
  - 💄 Improve Image preview mask blur transition for `backdrop-filter` to reduce flicker perception. [#57299](https://github.com/ant-design/ant-design/pull/57299) [@mango766](https://github.com/mango766)
  - 🐞 Fix Image showing move cursor when `movable={false}`. [#57288](https://github.com/ant-design/ant-design/pull/57288) [@ug-hero](https://github.com/ug-hero)
- ⌨️ Improve App link `:focus-visible` outline to enhance keyboard accessibility. [#57266](https://github.com/ant-design/ant-design/pull/57266) [@ug-hero](https://github.com/ug-hero)
- 🐞 Fix Form required mark using hardcoded `SimSun` font. [#57273](https://github.com/ant-design/ant-design/pull/57273) [@mavericusdev](https://github.com/mavericusdev)
- 🐞 Fix Grid media size mapping issue for `xxxl` breakpoint. [#57246](https://github.com/ant-design/ant-design/pull/57246) [@guoyunhe](https://github.com/guoyunhe)
- 🐞 Fix Tree scrolling to top when clicking node. [#57242](https://github.com/ant-design/ant-design/pull/57242) [@aojunhao123](https://github.com/aojunhao123)

## 6.3.2

`2026-03-09`

- 🐞 Fix Form.Item validation failure caused by a timing issue when using dynamic `rules` and `dependencies` together. [#57147](https://github.com/ant-design/ant-design/pull/57147) [@zombieJ](https://github.com/zombieJ)
- 🐞 Fix InputNumber height in `borderless` variant when using with Input or Select. [#57162](https://github.com/ant-design/ant-design/pull/57162) [@QDyanbing](https://github.com/QDyanbing)
- 🐞 Fix Radio.Group radio button width when options text has different length or breaks. [#57171](https://github.com/ant-design/ant-design/pull/57171) [@QDyanbing](https://github.com/QDyanbing)
- 🐞 Fix Skeleton.Avatar, Skeleton.Button, Skeleton.Input, Rate and Spin cannot take effect when `componentSize` is set globally. [#57093](https://github.com/ant-design/ant-design/pull/57093) [#57106](https://github.com/ant-design/ant-design/pull/57106) [@QDyanbing](https://github.com/QDyanbing)
- 🐞 Fix Splitter may calculate wrong `size` if some panel in controlled mode. [#57142](https://github.com/ant-design/ant-design/pull/57142) [@js0753](https://github.com/js0753)
- 🐞 Fix Tree and TreeSelect line alignment problem when customizing `titleHeight` property. [#56785](https://github.com/ant-design/ant-design/pull/56785) [@QDyanbing](https://github.com/QDyanbing)
- 💄 Fix Checkbox.Group checkbox width when options text has different length or breaks. [#57144](https://github.com/ant-design/ant-design/pull/57144) [@QDyanbing](https://github.com/QDyanbing)
- 💄 Fix ConfigProvider `csp` not taking effect on all the dynamic style. [#57159](https://github.com/ant-design/ant-design/pull/57159) [@zombieJ](https://github.com/zombieJ)
- Select
  - 💄 Fix Select text jumping problem in Firefox browser. [#57030](https://github.com/ant-design/ant-design/pull/57030) [@pierreeurope](https://github.com/pierreeurope)
  - 💄 Fix Select cannot set `visibility: hidden` via `style` property. [#56720](https://github.com/ant-design/ant-design/pull/56720) [@claytonlin1110](https://github.com/claytonlin1110)
- Upload
  - 💄 Fix Upload has invalid blank area in `picture-card` mode with empty data. [#57157](https://github.com/ant-design/ant-design/pull/57157) [@QDyanbing](https://github.com/QDyanbing)
  - ⌨️ Improve Upload to always show item action area on non-hover or coarse-pointer devices. [#57156](https://github.com/ant-design/ant-design/pull/57156) [@Arktomson](https://github.com/Arktomson)
- 🌐 Add `es_US` locale preset. [#57137](https://github.com/ant-design/ant-design/pull/57137) [@yuriidumych-max](https://github.com/yuriidumych-max)
- 🛠 Unify `size` enumeration, replace `default` with `medium` for Badge, Card, Progress, Steps, Switch and Spin, replace `middle` and `default` with `medium` and `large` for Descriptions, replace `middle` with `medium` for Table and Divider. [#57127](https://github.com/ant-design/ant-design/pull/57127) [#57106](https://github.com/ant-design/ant-design/pull/57106) [@QDyanbing](https://github.com/QDyanbing)
- 🛠 Unify `size` className for all components DOM. [#57106](https://github.com/ant-design/ant-design/pull/57106) [@QDyanbing](https://github.com/QDyanbing)
- TypeScript
  - 🤖 Add Upload.Dragger generic type definition support. [#57103](https://github.com/ant-design/ant-design/pull/57103) [@fnoopv](https://github.com/fnoopv)
  - 🤖 Fix Modal `KeyboardEvent` type definition for the arguments of `onCancel` event handler. [#57048](https://github.com/ant-design/ant-design/pull/57048) [@eureka928](https://github.com/eureka928)

## 6.3.1

`2026-02-24`

- Select
  - 🐞 Fix Select incorrect dropdown height when `value` is an empty string. [#56976](https://github.com/ant-design/ant-design/pull/56976) [@zombieJ](https://github.com/zombieJ)
  - 🐞 Fix Select value echo issue when `value` is an empty string. [#56966](https://github.com/ant-design/ant-design/pull/56966) [@luozz1994](https://github.com/luozz1994)
  - 🐞 Fix Select & TreeSelect selected value text still visible when searching. [#56946](https://github.com/ant-design/ant-design/pull/56946)
- 🐞 Fix TreeSelect Checkbox being compressed when multi-line text is present. [#56961](https://github.com/ant-design/ant-design/pull/56961) [@luozz1994](https://github.com/luozz1994)
- 🐞 Fix Typography hovering copy button triggering ellipsis tooltip when both `copyable` and `ellipsis` are enabled; fix ellipsis tooltip not appearing after moving back from copy button. [#56855](https://github.com/ant-design/ant-design/pull/56855) [@claytonlin1110](https://github.com/claytonlin1110)
- 🐞 Fix Progress animation overflow when `status="active"`. [#56972](https://github.com/ant-design/ant-design/pull/56972) [@aibayanyu20](https://github.com/aibayanyu20)
- 🐞 Fix Upload picture-wall mode list overflow and overlap when file count exceeds one row. [#56945](https://github.com/ant-design/ant-design/pull/56945) [@xbsheng](https://github.com/xbsheng)
- 🐞 Fix Image flickering in some browsers when opening preview. [#56937](https://github.com/ant-design/ant-design/pull/56937) [@zombieJ](https://github.com/zombieJ)
- ⌨️ ♿ Add `prefers-reduced-motion` media query support for Button, Checkbox, Radio, Switch, Segmented to disable transitions for improved accessibility. [#56902](https://github.com/ant-design/ant-design/pull/56902) [@li-jia-nan](https://github.com/li-jia-nan)
- 🐞 Fix Input height inconsistency with Select when using `variant="borderless"`. [#57014](https://github.com/ant-design/ant-design/pull/57014) [@njlazzar-su](https://github.com/njlazzar-su)
- 🐞 Fix Modal `confirm` method layout whitespace when `icon` is empty. [#57024](https://github.com/ant-design/ant-design/pull/57024) [@Arktomson](https://github.com/Arktomson)
- 🐞 Add `aria-disabled` attribute for disabled options in Select component.[#57049](https://github.com/ant-design/ant-design/pull/57049) [@meet-student](https://github.com/meet-student)

## 6.3.0

`2026-02-10`

- ConfigProvider
  - 🆕 Support ConfigProvider global configuration of `maskClosable` for Modal and Drawer. [#56739](https://github.com/ant-design/ant-design/pull/56739) [@luozz1994](https://github.com/luozz1994)
  - 🆕 Support ConfigProvider `suffixIcon` global configuration for DatePicker and TimePicker. [#56709](https://github.com/ant-design/ant-design/pull/56709) [@guoyunhe](https://github.com/guoyunhe)
  - 🆕 Support ConfigProvider `expandIcon` and `loadingIcon` global configuration for Cascader. [#56482](https://github.com/ant-design/ant-design/pull/56482) [@guoyunhe](https://github.com/guoyunhe)
  - 🆕 Support ConfigProvider `scroll` global configuration for Table. [#56628](https://github.com/ant-design/ant-design/pull/56628) [@Clayton](https://github.com/Clayton)
  - 🆕 Support ConfigProvider `className` and `style` configuration for App, and `arrow` prop for ColorPicker. [#56573](https://github.com/ant-design/ant-design/pull/56573) [@zombieJ](https://github.com/zombieJ)
  - 🆕 Support ConfigProvider `loadingIcon` global configuration for Button. [#56439](https://github.com/ant-design/ant-design/pull/56439) [@guoyunhe](https://github.com/guoyunhe)
  - 🆕 Support ConfigProvider `rangePicker.separator` global configuration. [#56499](https://github.com/ant-design/ant-design/pull/56499) [@guoyunhe](https://github.com/guoyunhe)
  - 🆕 Support ConfigProvider `tooltipIcon` and `tooltipProps` global configuration for Form. [#56372](https://github.com/ant-design/ant-design/pull/56372) [@guoyunhe](https://github.com/guoyunhe)
- Upload
  - 🆕 Add Upload `classNames.trigger` and `styles.trigger` props. [#56578](https://github.com/ant-design/ant-design/pull/56578) [@QdabuliuQ](https://github.com/QdabuliuQ)
  - 🆕 Support Upload.Dragger `onDoubleClick` event. [#56579](https://github.com/ant-design/ant-design/pull/56579) [@ug-hero](https://github.com/ug-hero)
  - 🐞 Fix Upload missing default height for `picture-card` / `picture-circle` parent nodes. [#56864](https://github.com/ant-design/ant-design/pull/56864) [@wanpan11](https://github.com/wanpan11)
- 🆕 Add Grid `xxxl` (1920px) breakpoint to adapt to FHD screens. [#56825](https://github.com/ant-design/ant-design/pull/56825) [@guoyunhe](https://github.com/guoyunhe)
- 🆕 Support Switch `indicator` customization for semantic structure. [#56710](https://github.com/ant-design/ant-design/pull/56710) [@zombieJ](https://github.com/zombieJ)
- Button
  - 🐞 Fix Button reversed `hover` and `active` colors for `color` in dark theme. [#56872](https://github.com/ant-design/ant-design/pull/56872) [@zombieJ](https://github.com/zombieJ)
  - 🐞 Fix Button border size not following Design Token `lineWidth`. [#56683](https://github.com/ant-design/ant-design/pull/56683) [@zombieJ](https://github.com/zombieJ)
- Select
  - 💄 Remove Select redundant `-content-value` div DOM in single mode to optimize semantic structure, allowing override via `classNames` and `styles`. [#56811](https://github.com/ant-design/ant-design/pull/56811) [@zombieJ](https://github.com/zombieJ)
  - 🐞 Fix Select `notFoundContent` not taking effect. [#56756](https://github.com/ant-design/ant-design/pull/56756) [@QdabuliuQ](https://github.com/QdabuliuQ)
- Radio
  - 🐞 Fix Radio.Group extra right margin for radio items when vertically aligned. [#56909](https://github.com/ant-design/ant-design/pull/56909) [@jany55555](https://github.com/jany55555)
  - 💄 Remove Radio `-inner` DOM node of `icon` sub-element for better semantic structure adaptation. [#56783](https://github.com/ant-design/ant-design/pull/56783) [@zombieJ](https://github.com/zombieJ)
- 💄 Disable Modal & Drawer mask blur effect by default. [#56781](https://github.com/ant-design/ant-design/pull/56781) [@aojunhao123](https://github.com/aojunhao123)
- 🐞 Fix Tooltip & Popover popup animation starting position being shifted to the left. [#56887](https://github.com/ant-design/ant-design/pull/56887) [@zombieJ](https://github.com/zombieJ)
- 🐞 Fix List color-related tokens not working for deprecated component config. [#56913](https://github.com/ant-design/ant-design/pull/56913) [@zombieJ](https://github.com/zombieJ)
- 🛠 Refactor Spin DOM structure to align across different scenarios and support full Semantic Structure. [#56852](https://github.com/ant-design/ant-design/pull/56852) [@zombieJ](https://github.com/zombieJ)
- ⌨️ ♿ Add Icon accessibility names to the search icon SVG to improve screen reader support. [#56521](https://github.com/ant-design/ant-design/pull/56521) [@huangkevin-apr](https://github.com/huangkevin-apr)
- 🐞 Fix Cascader filter list resetting immediately when closing on selection in search mode, affecting UX. [#56764](https://github.com/ant-design/ant-design/pull/56764) [@zombieJ](https://github.com/zombieJ)
- ⌨️ ♿ Improve Tree accessibility support. [#56716](https://github.
... [TRUNCATED]
```

### File: CHANGELOG.zh-CN.md
```md
---
order: 6
title: 更新日志
timeline: true
tag: vVERSION
---

`antd` 遵循 [Semantic Versioning 2.0.0](http://semver.org/lang/zh-CN/) 语义化版本规范。

#### 发布周期

- 修订版本号：每周末会进行日常 bugfix 更新。（如果有紧急的 bugfix，则任何时候都可发布）
- 次版本号：每月发布一个带有新特性的向下兼容的版本。
- 主版本号：含有破坏性更新和新特性，不在发布周期内。

---

## 6.3.5

`2026-03-30`

- 🐞 修复 Image 预览底部操作按钮没有重置原生按钮样式的问题。[#57491](https://github.com/ant-design/ant-design/pull/57491) [@QDyanbing](https://github.com/QDyanbing)
- 🐞 修复 TimePicker 在移动端触摸设备无法直接滚动时间列的问题。[#57468](https://github.com/ant-design/ant-design/pull/57468) [@afc163](https://github.com/afc163)
- 🐞 杂项：修复 Icon 在特定场景没有居中对齐的问题。[#57460](https://github.com/ant-design/ant-design/pull/57460) [@QDyanbing](https://github.com/QDyanbing)

## 6.3.4

`2026-03-24`

- 🔥 新增官方命令行工具 [`@ant-design/cli`](https://www.npmjs.com/package/@ant-design/cli)，支持离线查询 Ant Design 组件知识、分析项目用法及提供迁移指导。[#57413](https://github.com/ant-design/ant-design/pull/57413) [@afc163](https://github.com/afc163)
- 🐞 修复 Form.List 在使用 `onValuesChange` 时丢失同级字段值的问题。[#57399](https://github.com/ant-design/ant-design/pull/57399) [@zombieJ](https://github.com/zombieJ)
- 🐞 修复 `useToken` 缺少 `screenXXXLMin` 导致生成错误的 antd.css 的问题。[#57372](https://github.com/ant-design/ant-design/pull/57372) [@sealye09](https://github.com/sealye09)
- 🐞 修复 ConfigProvider 组件配置的类型定义，为已支持的组件暴露语义化 `classNames` 和 `styles`。[#57396](https://github.com/ant-design/ant-design/pull/57396) [@QDyanbing](https://github.com/QDyanbing)
- 🐞 修复 Image 组件 `fetchPriority` 属性未正确透传到 `<img>` 元素的问题。[#57392](https://github.com/ant-design/ant-design/pull/57392) [@aojunhao123](https://github.com/aojunhao123)
- Menu
  - 🐞 修复通过 ConfigProvider 自定义 Menu 的 `itemHoverColor` 时，SubMenu 父级菜单项 hover 状态颜色不生效的问题。[#57374](https://github.com/ant-design/ant-design/pull/57374) [@EmilyyyLiu](https://github.com/EmilyyyLiu)
  - 🐞 修复 Menu 自定义 `collapsedIconSize` 后折叠图标看起来未居中的问题。[#57360](https://github.com/ant-design/ant-design/pull/57360) [@QDyanbing](https://github.com/QDyanbing)
- 🐞 修复 Table 在开启滚动时列头中受控 Popover 被重复渲染的问题。[#57342](https://github.com/ant-design/ant-design/pull/57342) [@QDyanbing](https://github.com/QDyanbing)
- 🐞 修复 Transfer `render` 属性返回 JSX 元素时搜索功能失效的问题。[#57133](https://github.com/ant-design/ant-design/pull/57133) [@WustLCQ](https://github.com/WustLCQ)
- 🐞 修复 Tree 开启 `showLine` 时自定义 `switcherIcon` 缺少 `switcher-line-icon` 类名导致样式异常的问题。[#57303](https://github.com/ant-design/ant-design/pull/57303) [@QDyanbing](https://github.com/QDyanbing)
- 🐞 修复 Watermark 在未传入 `onRemove` 时的 TypeScript 报错。[#57344](https://github.com/ant-design/ant-design/pull/57344) [@QDyanbing](https://github.com/QDyanbing)

## 6.3.3

`2026-03-16`

- Image
  - 💄 优化 Image 预览蒙层 blur 效果的 `backdrop-filter` 过渡，减少闪烁感。[#57299](https://github.com/ant-design/ant-design/pull/57299) [@mango766](https://github.com/mango766)
  - 🐞 修复 Image 在 `movable={false}` 时仍显示 move 光标的问题。[#57288](https://github.com/ant-design/ant-design/pull/57288) [@ug-hero](https://github.com/ug-hero)
- ⌨️ 优化 App 链接的 `:focus-visible` 外框样式，提升键盘可访问性。[#57266](https://github.com/ant-design/ant-design/pull/57266) [@ug-hero](https://github.com/ug-hero)
- 🐞 修复 Form 必填标记文案中硬编码 `SimSun` 字体的问题。[#57273](https://github.com/ant-design/ant-design/pull/57273) [@mavericusdev](https://github.com/mavericusdev)
- 🐞 修复 Grid `xxxl` 断点在媒体尺寸映射中的错误。[#57246](https://github.com/ant-design/ant-design/pull/57246) [@guoyunhe](https://github.com/guoyunhe)
- 🐞 修复 Tree 点击节点时页面回滚到顶部的问题。[#57242](https://github.com/ant-design/ant-design/pull/57242) [@aojunhao123](https://github.com/aojunhao123)

## 6.3.2

`2026-03-09`

- 🐞 修复 Form.Item 使用动态 `rules` 与 `dependencies` 配合使用时，时序问题导致的校验失败的问题。[#57147](https://github.com/ant-design/ant-design/pull/57147) [@zombieJ](https://github.com/zombieJ)
- 🐞 修复 InputNumber 在 `borderless` 形态下与 Input 或 Select 并排时高度异常的问题。[#57162](https://github.com/ant-design/ant-design/pull/57162) [@QDyanbing](https://github.com/QDyanbing)
- 🐞 修复 Radio.Group 在选项文案长短不一或换行时，勾选框宽度不一致的问题。[#57171](https://github.com/ant-design/ant-design/pull/57171) [@QDyanbing](https://github.com/QDyanbing)
- 🐞 修复 Skeleton.Avatar，Skeleton.Button，Skeleton.Input，Rate 及 Spin 无法响应全局 `componentSize` 设置的问题。[#57093](https://github.com/ant-design/ant-design/pull/57093) [#57106](https://github.com/ant-design/ant-design/pull/57106) [@QDyanbing](https://github.com/QDyanbing)
- 🐞 修复 Splitter 存在 `size` 受控面板时其他面板尺寸可能计算错误的问题。[#57142](https://github.com/ant-design/ant-design/pull/57142) [@js0753](https://github.com/js0753)
- 🐞 修复 Tree 及 TreeSelect 在自定义 `titleHeight` 时会连线错位的问题。[#56785](https://github.com/ant-design/ant-design/pull/56785) [@QDyanbing](https://github.com/QDyanbing)
- 💄 修复 Checkbox.Group 在选项文案长短不一或换行时，勾选框宽度不一致的问题。[#57144](https://github.com/ant-design/ant-design/pull/57144) [@QDyanbing](https://github.com/QDyanbing)
- 💄 修复 ConfigProvider 的 `csp` 配置没有对所有的动态 style 生效的问题。[#57159](https://github.com/ant-design/ant-design/pull/57159) [@zombieJ](https://github.com/zombieJ)
- Select
  - 💄 修复 Select 在 Firefox 浏览器下可能出现文字跳动的问题。[#57030](https://github.com/ant-design/ant-design/pull/57030) [@pierreeurope](https://github.com/pierreeurope)
  - 💄 修复 Select 无法通过 `style` 设置 `visibility: hidden` 的问题。[#56720](https://github.com/ant-design/ant-design/pull/56720) [@claytonlin1110](https://github.com/claytonlin1110)
- Upload
  - 💄 修复 Upload 在 `picture-card` 模式下无数据时仍然存在无效空白区域的问题。[#57157](https://github.com/ant-design/ant-design/pull/57157) [@QDyanbing](https://github.com/QDyanbing)
  - ⌨️ 优化 Upload 在不支持悬停或粗指针的设备上默认显示列表操作按钮。[#57156](https://github.com/ant-design/ant-design/pull/57156) [@Arktomson](https://github.com/Arktomson)
- 🌐 新增 `es_US` 国际化配置。[#57137](https://github.com/ant-design/ant-design/pull/57137) [@yuriidumych-max](https://github.com/yuriidumych-max)
- 🛠 统一 `size` 枚举值定义，针对 Badge、Card、Progress、Steps、Switch 及 Spin 使用 `medium` 替代 `default`，针对 Descriptions 使用 `medium` 和 `large` 替代 `middle` 和 `default`，针对 Table 和 Divider 使用 `medium` 替代 `middle`。[#57127](https://github.com/ant-design/ant-design/pull/57127) [#57106](https://github.com/ant-design/ant-design/pull/57106) [@QDyanbing](https://github.com/QDyanbing)
- 🛠 统一 `size` className 在所有组件元素上的设置值。[#57106](https://github.com/ant-design/ant-design/pull/57106) [@QDyanbing](https://github.com/QDyanbing)
- TypeScript
  - 🤖 新增 Upload.Dragger 的泛型支持。[#57103](https://github.com/ant-design/ant-design/pull/57103) [@fnoopv](https://github.com/fnoopv)
  - 🤖 修复 Modal `onCancel` 入参不支持 `KeyboardEvent` 类型的问题。[#57048](https://github.com/ant-design/ant-design/pull/57048) [@eureka928](https://github.com/eureka928)

## 6.3.1

`2026-02-24`

- Select
  - 🐞 Select 修复 `value` 为空字符串时下拉框高度不正确的问题。[#56976](https://github.com/ant-design/ant-design/pull/56976) [@zombieJ](https://github.com/zombieJ)
  - 🐞 Select 修复 `value` 为空字符串时值回显异常的问题。[#56966](https://github.com/ant-design/ant-design/pull/56966) [@luozz1994](https://github.com/luozz1994)
  - 🐞 Select & TreeSelect 修复搜索时已选中值文本仍然显示的问题。[#56946](https://github.com/ant-design/ant-design/pull/56946)
- 🐞 TreeSelect 修复多行文本时 Checkbox 被压缩变形的问题。[#56961](https://github.com/ant-design/ant-design/pull/56961) [@luozz1994](https://github.com/luozz1994)
- 🐞 Typography 修复同时开启 `copyable` 和 `ellipsis` 时，悬停复制按钮会触发省略号 tooltip 的问题；修复从复制按钮移回文字后省略号 tooltip 不再出现的问题。[#56855](https://github.com/ant-design/ant-design/pull/56855) [@claytonlin1110](https://github.com/claytonlin1110)
- 🐞 Progress 修复 `status="active"` 时动画溢出的问题。[#56972](https://github.com/ant-design/ant-design/pull/56972) [@aibayanyu20](https://github.com/aibayanyu20)
- 🐞 Upload 修复照片墙模式下文件数量超过一行时列表溢出重叠的问题。[#56945](https://github.com/ant-design/ant-design/pull/56945) [@xbsheng](https://github.com/xbsheng)
- 🐞 Image 修复打开预览时，部分浏览器会出现闪烁的问题。[#56937](https://github.com/ant-design/ant-design/pull/56937) [@zombieJ](https://github.com/zombieJ)
- ⌨️ ♿ 为 Button、Checkbox、Radio、Switch、Segmented 等组件添加 `prefers-reduced-motion` 媒体查询支持，禁用过渡动画以改善无障碍体验。[#56902](https://github.com/ant-design/ant-design/pull/56902) [@li-jia-nan](https://github.com/li-jia-nan)
- 🐞 Input 修复 `variant="borderless"` 时高度与 Select 不一致的问题。[#57014](https://github.com/ant-design/ant-design/pull/57014) [@njlazzar-su](https://github.com/njlazzar-su)
- 🐞 Modal 修复 `confirm` 方法在 `icon` 为空时布局出现多余空白的问题。[#57024](https://github.com/ant-design/ant-design/pull/57024) [@Arktomson](https://github.com/Arktomson)
- 🐞 Select 组件中的禁用选项添加 `aria-disabled` 属性。[#57049](https://github.com/ant-design/ant-design/pull/57049) [@meet-student](https://github.com/meet-student)

## 6.3.0

`2026-02-10`

- ConfigProvider
  - 🆕 ConfigProvider 支持 Modal 和 Drawer 的 `maskClosable` 全局配置。[#56739](https://github.com/ant-design/ant-design/pull/56739) [@luozz1994](https://github.com/luozz1994)
  - 🆕 ConfigProvider 支持 DatePicker 和 TimePicker 的 `suffixIcon` 全局配置。[#56709](https://github.com/ant-design/ant-design/pull/56709) [@guoyunhe](https://github.com/guoyunhe)
  - 🆕 ConfigProvider 支持 Cascader 的 `expandIcon` 和 `loadingIcon` 全局配置。[#56482](https://github.com/ant-design/ant-design/pull/56482) [@guoyunhe](https://github.com/guoyunhe)
  - 🆕 ConfigProvider 支持 Table 的 `scroll` 全局配置。[#56628](https://github.com/ant-design/ant-design/pull/56628) [@Clayton](https://github.com/Clayton)
  - 🆕 ConfigProvider 支持配置 App 的 `className` 与 `style`，以及 ColorPicker 的 `arrow` 属性。[#56573](https://github.com/ant-design/ant-design/pull/56573) [@zombieJ](https://github.com/zombieJ)
  - 🆕 ConfigProvider 支持 Button 的 `loadingIcon` 全局配置。[#56439](https://github.com/ant-design/ant-design/pull/56439) [@guoyunhe](https://github.com/guoyunhe)
  - 🆕 ConfigProvider 支持 `rangePicker.separator` 全局配置。[#56499](https://github.com/ant-design/ant-design/pull/56499) [@guoyunhe](https://github.com/guoyunhe)
  - 🆕 ConfigProvider 支持 Form 的 `tooltipIcon` 和 `tooltipProps` 全局配置。[#56372](https://github.com/ant-design/ant-design/pull/56372) [@guoyunhe](https://github.com/guoyunhe)
- Upload
  - 🆕 Upload 新增 `classNames.trigger` 和 `styles.trigger` 属性。[#56578](https://github.com/ant-design/ant-design/pull/56578) [@QdabuliuQ](https://github.com/QdabuliuQ)
  - 🆕 Upload.Dragger 支持 `onDoubleClick` 事件。[#56579](https://github.com/ant-design/ant-design/pull/56579) [@ug-hero](https://github.com/ug-hero)
  - 🐞 Upload 修复 `picture-card` / `picture-circle` 父节点缺少默认高度的问题。[#56864](https://github.com/ant-design/ant-design/pull/56864) [@wanpan11](https://github.com/wanpan11)
- 🆕 Grid 新增 `xxxl`（1920px）断点以适应 FHD 屏幕。[#56825](https://github.com/ant-design/ant-design/pull/56825) [@guoyunhe](https://github.com/guoyunhe)
- 🆕 Switch 语义化结构支持 `indicator` 定制。[#56710](https://github.com/ant-design/ant-design/pull/56710) [@zombieJ](https://github.com/zombieJ)
- Button
  - 🐞 Button 修复暗色主题下 `color` 的 `hover` 与 `active` 状态颜色相反的问题。[#56872](https://github.com/ant-design/ant-design/pull/56872) [@zombieJ](https://github.com/zombieJ)
  - 🐞 Button 修复边框尺寸未跟随 Design Token `lineWidth` 的问题。[#56683](https://github.com/ant-design/ant-design/pull/56683) [@zombieJ](https://github.com/zombieJ)
- Select
  - 💄 Select 移除单选模式下额外的 `-content-value` div DOM，优化语义化结构并支持通过 `classNames` 与 `styles` 覆盖。[#56811](https://github.com/ant-design/ant-design/pull/56811) [@zombieJ](https://github.com/zombieJ)
  - 🐞 Select 修复 `notFoundContent` 不生效的问题。[#56756](https://github.com/ant-design/ant-design/pull/56756) [@QdabuliuQ](https://github.com/QdabuliuQ)
- Radio
  - 🐞 Radio.Group 修复垂直排列时单选项出现多余右边距的问题。[#56909](https://github.com/ant-design/ant-design/pull/56909) [@jany55555](https://github.com/jany55555)
  - 💄 Radio 移除 `icon` 子元素 `-inner` DOM 节点以更好适配语义化结构。[#56783](https://github.com/ant-design/ant-design/pull/56783) [@zombieJ](https://github.com/zombieJ)
- 💄 Modal & Drawer 默认关闭蒙层 blur 效果。[#56781](https://github.com/ant-design/ant-design/pull/56781) [@aojunhao123](https://github.com/aojunhao123)
- 🐞 Tooltip & Popover 修复弹出层动画起始位置偏左的问题。[#56887](https://github.com/ant-design/ant-design/pull/56887) [@zombieJ](https://github.com/zombieJ)
- 🐞 List 修复废弃组件配置的颜色相关 token 不生效的问题。[#56913](https://github.com/ant-design/ant-design/pull/56913) [@zombieJ](https://github.com/zombieJ)
- 🛠 Spin 重构 DOM 结构以对齐不同场景，并支持全量语义化结构（Semantic Structure）。[#56852](https://github.com/ant-design/ant-design/pull/56852) [@zombieJ](https://github.com/zombieJ)
- ⌨️ ♿ Icon 为搜索图标 SVG 添加无障碍名称，改善屏幕阅读器支持。[#56521](https://github.com/ant-design/ant-design/pull/56521) [@huangkevin-apr](https://github.com/huangkevin-apr)
- 🐞 Cascader 修复搜索模式下选择选项并关闭时，过滤列表立即还原影响体验的问题。[#56764](https://github.com/ant-design/ant-design/pull/56764) [@zombieJ](https://github.com/zombieJ)
- ⌨️ ♿ Tree 优化无障碍支持。[#56716](https://github.com/ant-design/ant-design/pull/56716) [@aojunhao123](https://github.com/aojunhao123)
- 🐞 ColorPicker 选择块支持语义化结构，并修复 `root` 语义化错误应用到弹出元素的问题。[#56607](https://github.com/ant-design/ant-design/pull/56607) [@zombieJ](https://github.com/zombieJ)
- 💄 Avatar 将 `size` 默认值从 `default` 改为 `medium` 以保持一致性。[#56440](https://github.com/ant-design/ant-design/pull/56440) [@guoyunhe](https://github.com/guoyunhe)
- 💄 Checkbox 移除 `icon` 子元素 `-inner` DOM 节点以更好适配语义化结构。[#56783](https://github.com/ant-design/ant-design/pull/56783) [@zombieJ](https://github.com/zombieJ)
- MISC
  - 🐞 MISC: 修复 UMD 版本中 React Compiler 兼容性问题，现已默认关闭。[#56830](https://github.com/ant-design/ant-design/pull/56830) [@zombieJ](https://github.com/zombieJ)
  - 🛠 精简 `styles` 和 `classNames` 类型定义，使其更规范。[#56758](https://github.com/ant-design/ant-design/pull/56758) [@crazyair](https://github.com/crazyair)

## 6.2.3

`2026-02-02`

- Button
  - 🐞 修复 Button `defaultBg`、`defaultColor`、`defaultHoverColor` 和 `defaultActiveColor` token 不生效的问题。[#56238](https://github.com/ant-design/ant-design/pull/56238) [@ug-hero](https://github.com/ug-hero)
  - 🐞 修复 Button 默认 token 不生效的问题。[#56719](https://github.com/ant-design/ant-design/pull/56719) [@unknowntocka](https://github.com/unknowntocka)
  - 🐞 修复 Button `variant="solid"` 在 Space.Compact 中边框显示异常的问题。[#56486](https://github.com/ant-design/ant-design/pull/56486) [@Pareder](https://github.com/Pareder)
- 🐞 修复 Input.TextArea ref 缺少 `nativeElement` 属性的问题。[#56803](https://github.com/ant-design/ant-design/pull/56803) [@smith3816](https://github.com/smith3816)
- 🐞 修复 Flex 使用 `orientation` 时默认 `align` 不生效的问题。[#55950](https://github.com/ant-design/ant-design/pull/55950) [@YingtaoMo](https://github.com/YingtaoMo)
- 🐞 修复 Typography 链接选择器特异性过低导致样式被覆盖的问题。[#56759](https://github.com/ant-design/ant-design/pull/56759) [@QDyanbing](https://github.com/QDyanbing)
- 🐞 修复 ColorPicker HEX 输入框可以输入无效字符的问题。[#56752](https://github.com/ant-design/ant-design/pull/56752) [@treephesians](https://github.com/treephesians)

## 6.2.2

`2026-01-26`

- 🐞 修复被 Typography 包裹的带 href 的 Button 显示错误颜色和 hover 时 outline 闪烁的问题。[#56619](https://github.com/ant-design/ant-design/pull/56619) [@QdabuliuQ](https://github.com/QdabuliuQ)
- 🐞 修复 Button `type="text"` 时组件 Token 不生效的问题。[#56291](https://github.com/ant-design/ant-design/pull/56291) [@QDyanbing](https://github.com/QDyanbing)
- 🐞 修复 Popover 内组件被 Form.Item 状态关联影响的问题。[#56728](https://github.com/ant-design/ant-design/pull/56728)
- 🐞 修复 Select 多选时占位符显示异常的问题。[#56675](https://github.com/ant-design/ant-design/pull/56675)
- 💄 修复 Pagination 全局 `fontSize` 变大时各元素上下错位的问题。[#56715](https://gith
... [TRUNCATED]
```

### File: CLAUDE.md
```md
# Ant Design 项目开发指南

> 本文件为 AI 编程助手提供项目上下文和开发规范。

## 项目信息

- React 组件库，发布为 npm 包 `antd`
- 使用 TypeScript 和 React 开发
- 采用 CSS-in-JS 架构（基于 `@ant-design/cssinjs`）
- 支持 Design Token 主题系统、暗色模式、RTL 布局、SSR、国际化（150+ 语言）

### 项目结构

```
ant-design/
├── components/              # 组件源代码（84+ 组件）
│   ├── component-name/      # 单个组件目录
│   │   ├── ComponentName.tsx      # 主组件实现
│   │   ├── demo/                  # 演示代码（*.tsx 和 *.md）
│   │   ├── style/                 # 样式系统（index.ts / token.ts）
│   │   ├── __tests__/            # 单元测试
│   │   ├── index.en-US.md        # 英文文档
│   │   ├── index.zh-CN.md        # 中文文档
│   │   └── index.tsx             # 导出入口
│   ├── _util/                   # 共享工具函数库
│   ├── theme/                   # 主题系统
│   └── locale/                  # 国际化文本
├── tests/                       # 测试工具和共享测试
├── docs/                        # 站点文档
├── CHANGELOG.zh-CN.md           # 中文更新日志
└── CHANGELOG.en-US.md           # 英文更新日志
```

---

## Demo 导入规范

- 本规范同时适用于 `components/**/demo/` 和 `.dumi/` 下的示例、站点、主题相关文件。（`semantic.test.tsx` 文件除外）
- 在这些目录下引入 Ant Design 组件、组件内部模块、工具方法、变量、类型定义时，一律使用绝对路径导入，不使用相对路径导入。
- 允许的导入形式应优先使用项目公开入口或已配置别名，例如：`antd`、`antd/es/*`、`antd/lib/*`、`antd/locale/*`、`.dumi/*`、`@@/*`。
- 禁止使用 `..`、`../xxx`、`../../xxx`、`./xxx` 这类相对路径去引用组件实现、内部模块、方法、变量、类型，包含跨 demo、跨目录复用的场景。
- demo 与 `.dumi` 文件之间不要互相相对引用；如果需要复用少量逻辑，优先内联，或提取到可通过绝对路径访问的公共位置。

## Test 导入规范

- 本规范适用于 `components/**/__tests__/` 下的测试文件。
- 在这些目录下引入 Ant Design 组件，或引入组件内部模块、工具方法、变量、类型定义时，一律使用相对路径导入，不使用绝对路径导入。
- 测试文件应优先从当前组件目录、相邻内部模块或共享测试工具目录通过相对路径引用，例如：`..`、`../index`、`../xxx`、`../../_util/*`、`../../../tests/shared/*`。
- 禁止在 `__tests__` 目录下使用 `antd`、`antd/es/*`、`antd/lib/*`、`antd/locale/*`、`.dumi/*`、`@@/*` 这类绝对路径或别名路径去引用仓库内代码。
- 如需引用仓库外第三方依赖，仍按依赖包名正常导入，例如 `react`、`@testing-library/react`、`dayjs`。

---

## 文档规范

### API 表格格式

| Property | Description | Type                   | Default   | Version |
| -------- | ----------- | ---------------------- | --------- | ------- |
| disabled | 是否禁用    | boolean                | false     | -       |
| type     | 按钮类型    | `primary` \| `default` | `default` | -       |

- 字符串默认值用反引号，布尔/数字直接写，无默认值用 `-`
- API 按字母顺序排列，新增属性需声明版本号

### 文档锚点 ID 规范

- 中文标题必须手动指定英文锚点：`## 中文标题 {#english-anchor-id}`
- 锚点 ID 符合 `^[a-zA-Z][\w-:\.]*$`，长度不超过 32 字符
- FAQ 章节下的锚点必须以 `faq-` 为前缀
- 同一问题的中英文锚点保持一致

### 国际化规范

- 本地化配置文件：`components/locale/`，命名如 `zh_CN.ts`、`en_US.ts`
- 添加或修改本地化配置时，需同时修改所有语言文件
- 类型入口：`components/locale/index.tsx`

---

## PR 规范

### 标题与内容

- PR 标题始终使用英文，格式：`类型: 简短描述`
- PR 内容默认使用英文，可根据用户语言习惯决定使用中文或英文
- 示例：`fix: fix button style issues in Safari browser`

### PR 模板（必须使用）

- 英文模板：`.github/PULL_REQUEST_TEMPLATE.md`
- 中文模板：`.github/PULL_REQUEST_TEMPLATE_CN.md`
- 使用 `gh pr create` 创建 PR 时，必须手动填充模板内容

### 分支策略

- 新特性开发需基于 `feature` 分支，PR 目标分支也需为 `feature`
- 其余提交至 `master` 分支
- 分支命名规范：
  - 功能开发：`feat/description-of-feature`
  - 问题修复：`fix/issue-number-or-description`
  - 文档更新：`docs/what-is-changed`
  - 代码重构：`refactor/what-is-changed`

### PR 改动类型

- 🆕 新特性提交
- 🐞 Bug 修复
- 📝 文档改进
- 📽️ 演示代码改进
- 💄 样式/交互改进
- 🤖 TypeScript 更新
- 📦 包体积优化
- ⚡️ 性能优化
- 🌐 国际化改进

---

## Changelog 规范

### 核心原则

- 文件位置：`CHANGELOG.en-US.md` 和 `CHANGELOG.zh-CN.md`
- 必须同时提供中英文两个版本
- 忽略用户无感知的改动（内部重构、纯测试更新、工具链优化等）
- 描述"对开发者的影响"，而非"具体的实现细节"
- 尽量给出 PR 链接，并统一添加贡献者链接

### 格式规范

#### 条目格式

- **Emoji 置顶**：每条以 Emoji 开头
- **不加冒号**：组件名后不使用英文冒号
- **每条必含组件名**：正文必须出现对应组件名
- **组件名不用反引号**：Modal、Button 等；属性名/API 用反引号
- **中英空格**：中文与英文、数字、链接之间保留一个空格

#### 句式

| 语言 | 格式 | 示例 |
| --- | --- | --- |
| 中文 | `Emoji 动词 组件名 描述`（动词在前） | `🐞 修复 Button 在暗色主题下 \`color\` 的问题。` |
| 英文 | `Emoji 动词 组件名 描述`（动词在前） | `🐞 Fix Button reversed \`hover\` colors in dark theme.` |

#### 分组逻辑

- 同一组件有 2 条以上改动时，使用 `- 组件名` 作为分类标题
- 单项改动直接写单行条目

### Emoji 规范

| Emoji  | 用途                   |
| ------ | ---------------------- |
| 🐞     | 修复 Bug               |
| 💄     | 样式更新或 token 更新  |
| 🆕     | 新增特性 / 新增属性    |
| 🔥     | 极其值得关注的新增特性 |
| 🇺🇸🇨🇳🇬🇧 | 国际化改动             |
| 📖 📝  | 文档或网站改进         |
| ✅     | 新增或更新测试用例     |
| 🛎     | 更新警告/提示信息      |
| ⌨️ ♿  | 可访问性增强           |
| 🗑     | 废弃或移除             |
| 🛠     | 重构或工具链优化       |
| ⚡️     | 性能提升               |

每条 Changelog 仅选择一个 Emoji，不要在同一条目中叠加多个 Emoji。

编写 Changelog 时，请参考 `CHANGELOG.zh-CN.md` 和 `CHANGELOG.en-US.md` 中已有条目的格式。

---

## 参考资源

- [API Naming Rules](https://github.com/ant-design/ant-design/wiki/API-Naming-rules) - API 命名规范
- [轮值规则和版本发布流程](https://github.com/ant-design/ant-design/wiki/%E8%BD%AE%E5%80%BC%E8%A7%84%E5%88%99%E5%92%8C%E7%89%88%E6%9C%AC%E5%8F%91%E5%B8%83%E6%B5%81%E7%A8%8B) - 版本发布流程
- [Unique Panel Component](https://github.com/ant-design/ant-design/wiki/Unique-Panel-Component) - 独立面板组件规范

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

Instances of abusive, harassing, or otherwise unacceptable behavior may be reported by contacting the project team at [xingmin.zhu@alipay.com.](mailto:xingmin.zhu@alipay.com.) The project team will review and investigate all complaints, and will respond in a way that it deems appropriate to the circumstances. The project team is obligated to maintain confidentiality with regard to the reporter of an incident. Further details of specific enforcement policies may be posted separately.

Project maintainers who do not follow or enforce the Code of Conduct in good faith may face temporary or permanent repercussions as determined by other members of the project's leadership.

## Attribution

This Code of Conduct is adapted from the [Contributor Covenant][homepage], version 1.4, available at [http://contributor-covenant.org/version/1/4][version].

[homepage]: http://contributor-covenant.org
[version]: http://contributor-covenant.org/version/1/4/

```

### File: README-zh_CN.md
```md
<div align="center"><a name="readme-top"></a>

<img height="180" src="https://gw.alipayobjects.com/zos/rmsportal/KDpgvguMpGfqaHPjicRK.svg">

<h1>Ant Design</h1>

一套企业级 UI 设计语言和 React 组件库。

[![CI status][github-action-image]][github-action-url] [![codecov][codecov-image]][codecov-url] [![NPM version][npm-image]][npm-url] [![NPM downloads][download-image]][download-url] [![][bundlephobia-image]][bundlephobia-url] [![][jsdelivr-image]][jsdelivr-url]

[![Follow Twitter][twitter-image]][twitter-url] [![dumi][dumi-image]][dumi-url] [![FOSSA Status][fossa-image]][fossa-url] [![Issues need help][help-wanted-image]][help-wanted-url] [![LFX Active Contributors][lfx-image]][lfx-url]

[更新日志](./CHANGELOG.zh-CN.md) · [报告问题][github-issues-url] · [特性需求][github-issues-url] · [English](./README.md) · 中文

## ❤️ 赞助者 [![](https://opencollective.com/ant-design/tiers/sponsors/badge.svg?label=Sponsors&color=brightgreen)](https://opencollective.com/ant-design/contribute/sponsors-218)

<a href="https://tractian.com"><img src="https://images.opencollective.com/tractian/0235da9/logo/256.png" width="128" height="128" alt="TRACTIAN"></a>
<a href="https://lobehub.com"><img src="https://unpkg.com/@lobehub/icons-static-svg@1.79.0/icons/lobehub-color.svg" width="128" height="128" alt="LobeHub"></a>
<a href="https://youmind.com"><img src="https://marketing-assets.youmind.com/logo-512.png" width="128" height="128" alt="YouMind"></a>

[npm-image]: https://img.shields.io/npm/v/antd.svg?style=flat-square
[npm-url]: https://npmjs.org/package/antd
[github-action-image]: https://github.com/ant-design/ant-design/actions/workflows/test.yml/badge.svg
[github-action-url]: https://github.com/ant-design/ant-design/actions/workflows/test.yml
[codecov-image]: https://img.shields.io/codecov/c/github/ant-design/ant-design/master.svg?style=flat-square
[codecov-url]: https://codecov.io/gh/ant-design/ant-design/branch/master
[download-image]: https://img.shields.io/npm/dm/antd.svg?style=flat-square
[download-url]: https://npmjs.org/package/antd
[fossa-image]: https://app.fossa.io/api/projects/git%2Bgithub.com%2Fant-design%2Fant-design.svg?type=shield
[fossa-url]: https://app.fossa.io/projects/git%2Bgithub.com%2Fant-design%2Fant-design?ref=badge_shield
[help-wanted-image]: https://img.shields.io/github/issues/ant-design/ant-design/help%20wanted?color=green&style=flat-square
[help-wanted-url]: https://github.com/ant-design/ant-design/issues?q=is%3Aopen+is%3Aissue+label%3A%22help+wanted%22
[twitter-image]: https://img.shields.io/twitter/follow/AntDesignUI.svg?label=Ant%20Design
[twitter-url]: https://twitter.com/AntDesignUI
[jsdelivr-image]: https://data.jsdelivr.com/v1/package/npm/antd/badge
[jsdelivr-url]: https://www.jsdelivr.com/package/npm/antd
[bundlephobia-image]: https://img.shields.io/bundlephobia/minzip/antd
[bundlephobia-url]: https://bundlephobia.com/package/antd
[dumi-image]: https://img.shields.io/badge/docs%20by-dumi-blue?style=flat-square
[dumi-url]: https://github.com/umijs/dumi
[github-issues-url]: https://new-issue.ant.design
[lfx-image]: https://insights.linuxfoundation.org/api/badge/active-contributors?project=ant-design-ant-design&repos=https://github.com/ant-design/ant-design
[lfx-url]: https://insights.linuxfoundation.org/project/ant-design-ant-design/repository/ant-design-ant-design

</div>

[![](https://user-images.githubusercontent.com/507615/209472919-6f7e8561-be8c-4b0b-9976-eb3c692aa20a.png)](https://ant.design)

## ✨ 特性

- 🌈 提炼自企业级中后台产品的交互语言和视觉风格。
- 📦 开箱即用的高质量 React 组件。
- 🛡 使用 TypeScript 开发，提供完整的类型定义文件。
- ⚙️ 应用开发框架和设计工具配套。
- 🌍 数十个国际化语言支持。
- 🎨 基于 CSS-in-JS 的主题定制能力。

## 🖥 兼容环境

支持范围：https://browsersl.ist/#q=defaults

- 现代浏览器。
- 支持服务端渲染。
- [Electron](https://www.electronjs.org/)

| [<img src="https://raw.githubusercontent.com/alrra/browser-logos/master/src/edge/edge_48x48.png" alt="Edge" width="24px" height="24px" />](https://godban.github.io/browsers-support-badges/)<br>Edge | [<img src="https://raw.githubusercontent.com/alrra/browser-logos/master/src/firefox/firefox_48x48.png" alt="Firefox" width="24px" height="24px" />](https://godban.github.io/browsers-support-badges/)<br>Firefox | [<img src="https://raw.githubusercontent.com/alrra/browser-logos/master/src/chrome/chrome_48x48.png" alt="Chrome" width="24px" height="24px" />](https://godban.github.io/browsers-support-badges/)<br>Chrome | [<img src="https://raw.githubusercontent.com/alrra/browser-logos/master/src/safari/safari_48x48.png" alt="Safari" width="24px" height="24px" />](https://godban.github.io/browsers-support-badges/)<br>Safari | [<img src="https://raw.githubusercontent.com/alrra/browser-logos/master/src/electron/electron_48x48.png" alt="Electron" width="24px" height="24px" />](https://godban.github.io/browsers-support-badges/)<br>Electron |
| --- | --- | --- | --- | --- |
| Edge | last 2 versions | last 2 versions | last 2 versions | last 2 versions |

## 📦 安装

```bash
npm install antd --save
```

```bash
yarn add antd
```

```bash
pnpm add antd
```

```bash
bun add antd
```

## 🔨 示例

```tsx
import React from 'react';
import { Button, DatePicker } from 'antd';

const App = () => (
  <>
    <Button type="primary">PRESS ME</Button>
    <DatePicker />
  </>
);

export default App;
```

### 🌈 定制主题

参考 [定制主题](https://ant.design/docs/react/customize-theme-cn) 文档。

### 🛡 TypeScript

`antd` 使用 TypeScript 编写，具有完整的类型定义，参考 [在 Next.js 中使用](https://ant.design/docs/react/use-with-next-cn)。

## 🌍 国际化

参考 [国际化文档](https://ant.design/docs/react/i18n-cn)。

## 🔗 链接

- [首页](https://ant.design/)
- [所有组件](https://ant.design/components/overview-cn)
- [赞助](https://ant.design/docs/react/sponsor)
- [更新日志](CHANGELOG.zh-CN.md)
- [React 底层基础组件](https://react-component.github.io/)
- [🆕 Ant Design X](https://x.ant.design/index-cn)
- [Ant Design Pro](https://pro.ant.design/)
- [Pro Components](https://procomponents.ant.design)
- [Ant Design Mobile](https://mobile.ant.design)
- [Ant Design Mini](https://mini.ant.design)
- [Ant Design Charts](https://charts.ant.design)
- [Ant Design Web3](https://web3.ant.design)
- [动效](https://motion.ant.design)
- [脚手架市场](https://scaffold.ant.design)
- [设计规范速查手册](https://github.com/ant-design/ant-design/wiki/Ant-Design-%E8%AE%BE%E8%AE%A1%E5%9F%BA%E7%A1%80%E7%AE%80%E7%89%88)
- [开发者说明](https://github.com/ant-design/ant-design/wiki/Development)
- [版本发布规则](https://github.com/ant-design/ant-design/wiki/%E8%BD%AE%E5%80%BC%E8%A7%84%E5%88%99%E5%92%8C%E7%89%88%E6%9C%AC%E5%8F%91%E5%B8%83%E6%B5%81%E7%A8%8B)
- [常见问题](https://ant.design/docs/react/faq-cn)
- [在线演示](https://u.ant.design/reproduce)，用于报告 bug
- [定制主题](https://ant.design/docs/react/customize-theme-cn)
- [国际化](https://ant.design/docs/react/i18n-cn)
- [成为社区协作成员](https://github.com/ant-design/ant-design/wiki/Collaborators#how-to-apply-for-being-a-collaborator)

## ⌨️ 本地开发

推荐使用 [opensumi.run](https://opensumi.run) 进行在线开发：

[![opensumi.run](https://custom-icon-badges.demolab.com/badge/opensumi-run-blue.svg?logo=opensumi)](https://opensumi.run/ide/ant-design/ant-design)

或者克隆到本地开发:

```bash
$ git clone git@github.com:ant-design/ant-design.git
$ cd ant-design
$ npm install
$ npm start
```

打开浏览器访问 http://127.0.0.1:8001 ，更多[本地开发文档](https://github.com/ant-design/ant-design/wiki/Development)。

## 🤝 参与共建 [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](https://makeapullrequest.com)

<table>
<tr>
  <td>
    <a href="https://next.ossinsight.io/widgets/official/compose-recent-top-contributors?repo_id=34526884" target="_blank" style="display: block" align="center">
      <picture>
        <source media="(prefers-color-scheme: dark)" srcset="https://next.ossinsight.io/widgets/official/compose-recent-top-contributors/thumbnail.png?repo_id=34526884&image_size=auto&color_scheme=dark" width="280">
        <img alt="Top Contributors of ant-design/ant-design - Last 28 days" src="https://next.ossinsight.io/widgets/official/compose-recent-top-contributors/thumbnail.png?repo_id=34526884&image_size=auto&color_scheme=light" width="280">
      </picture>
    </a>
  </td>
  <td rowspan="2">
    <a href="https://next.ossinsight.io/widgets/official/compose-last-28-days-stats?repo_id=34526884" target="_blank" style="display: block" align="center">
      <picture>
        <source media="(prefers-color-scheme: dark)" srcset="https://next.ossinsight.io/widgets/official/compose-last-28-days-stats/thumbnail.png?repo_id=34526884&image_size=auto&color_scheme=dark" width="655" height="auto">
        <img alt="Performance Stats of ant-design/ant-design - Last 28 days" src="https://next.ossinsight.io/widgets/official/compose-last-28-days-stats/thumbnail.png?repo_id=34526884&image_size=auto&color_scheme=light" width="655" height="auto">
      </picture>
    </a>
  </td>
</tr>
<tr>
  <td>
    <a href="https://next.ossinsight.io/widgets/official/compose-org-active-contributors?period=past_28_days&activity=new&owner_id=12101536&repo_ids=34526884" target="_blank" style="display: block" align="center">
      <picture>
        <source media="(prefers-color-scheme: dark)" srcset="https://next.ossinsight.io/widgets/official/compose-org-active-contributors/thumbnail.png?period=past_28_days&activity=new&owner_id=12101536&repo_ids=34526884&image_size=2x3&color_scheme=dark" width="273" height="auto">
        <img alt="New participants of ant-design - past 28 days" src="https://next.ossinsight.io/widgets/official/compose-org-active-contributors/thumbnail.png?period=past_28_days&activity=new&owner_id=12101536&repo_ids=34526884&image_size=2x3&color_scheme=light" width="273" height="auto">
      </picture>
    </a>
  </td>
</tr>
</table>

<a href="https://openomy.app/github/ant-design/ant-design" target="_blank" style="display: block; width: 100%;" align="center">
  <img src="https://openomy.app/svg?repo=ant-design/ant-design&chart=bubble&latestMonth=3" alt="Contribution Leaderboard" style="display: block; width: 100%;" />
</a>

请参考[贡献指南](https://ant.design/docs/react/contributing-cn).

> 强烈推荐阅读 [《提问的智慧》](https://github.com/ryanhanwu/How-To-Ask-Questions-The-Smart-Way)、[《如何向开源社区提问题》](https://github.com/seajs/seajs/issues/545) 和 [《如何有效地报告 Bug》](https://www.chiark.greenend.org.uk/%7Esgtatham/bugs-cn.html)、[《如何向开源项目提交无法解答的问题》](https://zhuanlan.zhihu.com/p/25795393)，更好的问题更容易获得帮助。

[![赞助链接](https://raw.githubusercontent.com/BoostIO/issuehunt-materials/master/v1/issuehunt-button-v1.svg)](https://issuehunt.io/repos/34526884)

## 👥 社区互助

如果您在使用的过程中碰到问题，可以通过下面几个途径寻求帮助，同时我们也鼓励资深用户通过下面的途径给新人提供帮助。

通过 GitHub Discussions 提问时，建议使用 `Q&A` 标签。

通过 Stack Overflow 或者 Segment Fault 提问时，建议加上 `antd` 标签。

1. [GitHub Discussions](https://github.com/ant-design/ant-design/discussions)
2. [Stack Overflow](https://stackoverflow.com/questions/tagged/antd)（英文）
3. [Segment Fault](https://segmentfault.com/t/antd)（中文）

## Issue 赞助

我们使用 [Issuehunt](https://issuehunt.io/repos/3452688) 来推动您希望看到的针对 antd 的修复和改进，请查看我们的赞助列表：

[![Let's fund issues in this repository](https://raw.githubusercontent.com/BoostIO/issuehunt-materials/master/v1/issuehunt-button-v1.svg)](https://issuehunt.io/repos/34526884)

## ❤️ Backers [![](https://opencollective.com/ant-design/tiers/backers/badge.svg?label=Backers&color=brightgreen)](https://opencollective.com/ant-design#support)

[![](https://opencollective.com/ant-design/tiers/backers.svg?avatarHeight=72)](https://opencollective.com/ant-design/contribute/backers-217/checkout)

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.

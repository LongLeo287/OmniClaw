---
id: AdguardFilters
type: knowledge
owner: OA_Triage
---
# AdguardFilters
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
    "name": "@adguard/filters",
    "author": "AdGuard Software Ltd.",
    "license": "GPL-3.0-only",
    "type": "module",
    "engines": {
        "node": ">=20.0.0"
    },
    "repository": {
        "type": "git",
        "url": "git+https://github.com/AdguardTeam/AdguardFilters.git"
    },
    "bugs": {
        "url": "https://github.com/AdguardTeam/AdguardFilters/issues"
    },
    "homepage": "https://github.com/AdguardTeam/AdguardFilters#readme",
    "scripts": {
        "aglint": "aglint --cache --cache-location .aglintcache --cache-strategy content \"**/*.txt\"",
        "markdownlint": "markdownlint .",
        "lint": "npm run aglint && npm run markdownlint",
        "prepare": "node .husky/install.js"
    },
    "lint-staged": {
        "*.txt": "aglint",
        "*.md": "markdownlint"
    },
    "devDependencies": {
        "@adguard/aglint": "4.0.0-beta.5",
        "husky": "^9.1.7",
        "lint-staged": "^16.3.2",
        "markdownlint": "^0.40.0",
        "markdownlint-cli": "^0.48.0"
    }
}

```

### File: README.md
```md
<!-- markdownlint-disable -->
&nbsp;

<p align="center">
    <img width="275" alt="AdGuard Filters logo" src="https://cdn.adtidy.org/website/github.com/AdguardFilters/viking.svg" />
</p>

<h1 align="center">AdGuard Filters</h1>
<h3 align="center">The place where ad trackers are actually blocked</h3>

<p align="center">
    <a href="https://github.com/AdguardTeam/AdguardFilters/actions/workflows/aglint.yml" target="_blank"><img src="https://github.com/AdguardTeam/AdguardFilters/actions/workflows/aglint.yml/badge.svg?branch=master" alt="AGLint status"></a>
    <a href="https://github.com/AdguardTeam/AdguardFilters/actions/workflows/pages/pages-build-deployment" target="_blank"><img src="https://github.com/AdguardTeam/AdguardFilters/actions/workflows/pages/pages-build-deployment/badge.svg?branch=master" alt="GitHub Pages deployment"></a>
</p>

<p align="center">
    <a href="https://github.com/AdguardTeam/AdguardFilters/blob/master/LICENSE" target="_blank"><img src="https://img.shields.io/github/license/AdguardTeam/AdguardFilters" alt="License"></a>
    <a href="https://github.com/AdguardTeam/AdguardFilters/graphs/contributors" target="_blank"><img src="https://img.shields.io/github/contributors/AdguardTeam/AdguardFilters" alt="GitHub contributors"></a>
    <a href="https://github.com/AdguardTeam/AdguardFilters/graphs/commit-activity" target="_blank"><img src="https://img.shields.io/github/commit-activity/m/AdguardTeam/AdguardFilters" alt="GitHub commit activity"></a>
    <a href="https://github.com/AdguardTeam/AdguardFilters/issues" target="_blank"><img src="https://img.shields.io/github/issues/AdguardTeam/AdguardFilters" alt="GitHub issues"></a>
    <a href="https://github.com/AdguardTeam/AdguardFilters/issues?q=is%3Aissue+is%3Aclosed" target="_blank"><img src="https://img.shields.io/github/issues-closed/AdguardTeam/AdguardFilters" alt="GitHub closed issues"></a>
</p>
<!-- markdownlint-restore -->

This is the place where we create filters for [AdGuard][adguard] and other
ad-blocking software, such as uBlock Origin. Each filter consists of a set of
text-based rules that AdGuard apps and programs use to filter out advertisements
and privacy-invasive content like banners, pop-ups, and trackers. Rules specific
to a certain region (e.g., German filter, Russian filter) or serving a specific
purpose (e.g., Social Media filter, Tracking Protection filter) are combined
into a single list, or filter, that can be enabled or disabled all at once.

Our filters are constantly updated. This repository allows anyone to bring our
attention to anything from overlooked ads to false positives, helping us refine
our filters, improve them, and keep them current.

We are proud of the fact that AdGuard Filters are among the most actively
developed content-blocking filter lists available, if not the most.

[adguard]: https://adguard.com/

## AdGuard Filters Policy

Our filter policy is available [here][policy].

[policy]: https://adguard.com/kb/general/ad-filtering/filter-policy/

## Contributing to AdGuard

We are blessed to have a community that does not only love AdGuard, but also
gives back. A lot of people volunteer in various ways to make other users'
experience with AdGuard better, and you can join them! We, on our part, can
only be happy to reward the most active members of the community.
So, what can you do?

### Report Issues

To submit a report, please use this [reporting tool][report].

[report]: https://agrd.io/report

### Suggest Filtering Rules

You will find a lot of open issues, each one referencing a problem with some
website — a missed ad, a false positive etc. — choose any one and suggest your
own rules in comments. AdGuard filter engineers will review your suggestions,
and if they find them correct, your rules will be added to AdGuard filters.

Here is the [official documentation][documentation] on AdGuard filtering rules
syntax. You'll need to read it before you'll be able to create your own
filtering rules.

[documentation]: https://adguard.com/kb/general/ad-filtering/create-own-filters/

### Other ways to contribute

Here is [a dedicated page][contribute] for people willing to contribute to
AdGuard.

[contribute]: https://adguard.com/contribute.html

```

### File: FETCHED_AdguardFilters_033323\package.json
```json
{
    "name": "@adguard/filters",
    "author": "AdGuard Software Ltd.",
    "license": "GPL-3.0-only",
    "type": "module",
    "engines": {
        "node": ">=20.0.0"
    },
    "repository": {
        "type": "git",
        "url": "git+https://github.com/AdguardTeam/AdguardFilters.git"
    },
    "bugs": {
        "url": "https://github.com/AdguardTeam/AdguardFilters/issues"
    },
    "homepage": "https://github.com/AdguardTeam/AdguardFilters#readme",
    "scripts": {
        "aglint": "aglint --cache --cache-location .aglintcache --cache-strategy content \"**/*.txt\"",
        "markdownlint": "markdownlint .",
        "lint": "npm run aglint && npm run markdownlint",
        "prepare": "node .husky/install.js"
    },
    "lint-staged": {
        "*.txt": "aglint",
        "*.md": "markdownlint"
    },
    "devDependencies": {
        "@adguard/aglint": "4.0.0-beta.5",
        "husky": "^9.1.7",
        "lint-staged": "^16.3.2",
        "markdownlint": "^0.40.0",
        "markdownlint-cli": "^0.48.0"
    }
}

```

### File: FETCHED_AdguardFilters_033323\README.md
```md
<!-- markdownlint-disable -->
&nbsp;

<p align="center">
    <img width="275" alt="AdGuard Filters logo" src="https://cdn.adtidy.org/website/github.com/AdguardFilters/viking.svg" />
</p>

<h1 align="center">AdGuard Filters</h1>
<h3 align="center">The place where ad trackers are actually blocked</h3>

<p align="center">
    <a href="https://github.com/AdguardTeam/AdguardFilters/actions/workflows/aglint.yml" target="_blank"><img src="https://github.com/AdguardTeam/AdguardFilters/actions/workflows/aglint.yml/badge.svg?branch=master" alt="AGLint status"></a>
    <a href="https://github.com/AdguardTeam/AdguardFilters/actions/workflows/pages/pages-build-deployment" target="_blank"><img src="https://github.com/AdguardTeam/AdguardFilters/actions/workflows/pages/pages-build-deployment/badge.svg?branch=master" alt="GitHub Pages deployment"></a>
</p>

<p align="center">
    <a href="https://github.com/AdguardTeam/AdguardFilters/blob/master/LICENSE" target="_blank"><img src="https://img.shields.io/github/license/AdguardTeam/AdguardFilters" alt="License"></a>
    <a href="https://github.com/AdguardTeam/AdguardFilters/graphs/contributors" target="_blank"><img src="https://img.shields.io/github/contributors/AdguardTeam/AdguardFilters" alt="GitHub contributors"></a>
    <a href="https://github.com/AdguardTeam/AdguardFilters/graphs/commit-activity" target="_blank"><img src="https://img.shields.io/github/commit-activity/m/AdguardTeam/AdguardFilters" alt="GitHub commit activity"></a>
    <a href="https://github.com/AdguardTeam/AdguardFilters/issues" target="_blank"><img src="https://img.shields.io/github/issues/AdguardTeam/AdguardFilters" alt="GitHub issues"></a>
    <a href="https://github.com/AdguardTeam/AdguardFilters/issues?q=is%3Aissue+is%3Aclosed" target="_blank"><img src="https://img.shields.io/github/issues-closed/AdguardTeam/AdguardFilters" alt="GitHub closed issues"></a>
</p>
<!-- markdownlint-restore -->

This is the place where we create filters for [AdGuard][adguard] and other
ad-blocking software, such as uBlock Origin. Each filter consists of a set of
text-based rules that AdGuard apps and programs use to filter out advertisements
and privacy-invasive content like banners, pop-ups, and trackers. Rules specific
to a certain region (e.g., German filter, Russian filter) or serving a specific
purpose (e.g., Social Media filter, Tracking Protection filter) are combined
into a single list, or filter, that can be enabled or disabled all at once.

Our filters are constantly updated. This repository allows anyone to bring our
attention to anything from overlooked ads to false positives, helping us refine
our filters, improve them, and keep them current.

We are proud of the fact that AdGuard Filters are among the most actively
developed content-blocking filter lists available, if not the most.

[adguard]: https://adguard.com/

## AdGuard Filters Policy

Our filter policy is available [here][policy].

[policy]: https://adguard.com/kb/general/ad-filtering/filter-policy/

## Contributing to AdGuard

We are blessed to have a community that does not only love AdGuard, but also
gives back. A lot of people volunteer in various ways to make other users'
experience with AdGuard better, and you can join them! We, on our part, can
only be happy to reward the most active members of the community.
So, what can you do?

### Report Issues

To submit a report, please use this [reporting tool][report].

[report]: https://agrd.io/report

### Suggest Filtering Rules

You will find a lot of open issues, each one referencing a problem with some
website — a missed ad, a false positive etc. — choose any one and suggest your
own rules in comments. AdGuard filter engineers will review your suggestions,
and if they find them correct, your rules will be added to AdGuard filters.

Here is the [official documentation][documentation] on AdGuard filtering rules
syntax. You'll need to read it before you'll be able to create your own
filtering rules.

[documentation]: https://adguard.com/kb/general/ad-filtering/create-own-filters/

### Other ways to contribute

Here is [a dedicated page][contribute] for people willing to contribute to
AdGuard.

[contribute]: https://adguard.com/contribute.html

```

### File: .aglintrc.yaml
```yaml
# AGLint config file
# Documentation: https://github.com/AdguardTeam/AGLint/blob/master/docs/configuration.md
root: true
extends:
  - aglint:recommended
platforms:
  - adg_any
rules:
  no-excluded-rules:
    - error
    - # Exclude rules by their exact text
      # Note: A rule is excluded ONLY if its text matches exactly.
      # For example, adding '||example.com^' will NOT exclude
      # '||example.com^$script'; it will exclude only '||example.com^'.
      excludedRuleTexts:
        # Breaks DuckDuckGo redirect when their Extension is installed - https://github.com/AdguardTeam/AdguardFilters/issues/161751
        - '||duckduckgo.com^$removeparam=atb'
        # Klaviyo onsite tracking - breaks some unsubscribe links
        - '$removeparam=_kx'
        # Completely blocks TikTok search
        # https://github.com/AdguardTeam/AdguardFilters/issues/225737#issuecomment-4003971740
        # https://www.tiktok.com/legal/page/global/tiktok-website-cookies-policy/en
        # For example: https://www.tiktok.com/search?q=test
        - '||tiktok.com^$cookie=ttwid'
        # Blocking pixapi.net causes issues
        - 'pixapi.net^'
        # https://github.com/AdguardTeam/AdguardFilters/issues/221086
        # May break whole mobile page
        - 'u.gg##.media-query_MOBILE_SMALL__MOBILE_LARGE'
        # https://github.com/AdguardTeam/AdguardFilters/issues/221018
        # Breaks Bandlab boost function
        - '||ad.bandlab.io^'
        # Breks shareing and access control in Google Docs
        - 'google.*##div[aria-label="Share"]'
        # Breaks websites that use Intercom chat widget
        - '||api-iam.intercom.io/messenger/web/ping'
        # Breaks adding Yahoo account in email clients
        - '||udc.yahoo.com^'
        # https://github.com/AdguardTeam/AdguardFilters/issues/188783#issuecomment-2359649738
        - '^||bilibili.com^$removeparam=mid'
        # Breaks appconsent.io cookie consents
        - '^||collector.appconsent.io^'

      # Exclude rules using regular expression patterns
      #
      # IMPORTANT:
      # - Patterns are tested against the FULL line text.
      # - Matching applies to ALL lines, including comments (comments start with `!`).
      # - Use this section only when excluding by exact text is not possible.
      # - Be as specific as possible — overly broad patterns may exclude
      #   unrelated rules and cause widespread breakage.
      #
      # NOTE for comments:
      # - Matching applies to comment lines as well, so an unanchored regexp may match them.
      #   Example: the pattern `\|\|foo\^` may exclude both `||foo^` and `! ||foo^`.
      # - If you want to KEEP commented rules, ensure the pattern cannot start with `!`:
      #   * Anchor to the start if you match from the beginning:
      #       ^\|\|foo\^
      #     (matches `||foo^`, but not `! ||foo^`)
      #   * Or, if you want to match “anywhere in the rule”, prefix with:
      #       ^(?!!).*foo
      #     (matches `||foo^` or `||foo.example.com^`,
      #      but not `! ||foo^` nor `! some text foo`)
      #
      # NOTE for regexp-rules (for excluding regexp rules written as /.../):
      # - The escaping trick below is needed ONLY when the excluded rule
      #   itself is a regexp rule (i.e. written as /.../).
      # - In regexp rule text, dots (.) may appear escaped or unescaped.
      #
      # Example:
      #   Excluded rule:
      #     /example.(com|org)\/ads/
      #   Pattern to match both forms:
      #     \/example(\.|\\\.)\(com\|org\)\\\/ads\/
      #
      # This matches BOTH:
      #   /example.(com|org)\/ads/
      #   /example\.(com|org)\/ads/
      #
      # See example: https://regex101.com/r/L7CsOZ/1
      excludedRegExpPatterns:
        # https://github.com/easylist/easylist/commit/c0ba1cec6d0f9b584f9c39f411b09753735d8a00
        - \|\|prodregistryv2\.org\^
        # https://github.com/AdguardTeam/AdGuardSDNSFilter/issues/2021
        - \|\|fd\.cleantalk\.org\^
        # https://github.com/easylist/easylist/pull/22890
        - music\.163\.com\/weapi\/feedback\/weblog
        - music\.163\.com\/weapi\/pl\/count
        - \|\|clientlogusf\.music\.163.com\^
        # https://github.com/AdguardTeam/AdguardFilters/issues/223303
        - \|\|newspicks\.com\^\$removeparam=ref$
        # https://github.com/uBlockOrigin/uAssets/issues/28368#issuecomment-3730694651
        # Broken videos on bloomberg.com
        - (?=.*\|bloomberg\.com)^\/wrapperMessagingWithoutDetection\.js\$script,domain=
        # Broken PerimeterX captcha
        - \|\|collector-.*\.px-cloud\.net\^
        # https://github.com/uBlockOrigin/uAssets/issues/31330
        - \|\|metrics\.streaks\.jp\^(\$third-party)?$
        # https://github.com/AdguardTeam/AdguardFilters/issues/189518#issuecomment-2480190492
        - \@\@\|\|blog\.livedoor\.jp\^\$generichide
        # https://github.com/AdguardTeam/AdguardFilters/issues/220178
        - \|\|uts-front\.line-apps\.com\^
        # https://x.com/aminevsky/status/1999742558281564451
        - bookoffonline\.co\.jp\/files\/.+\/(GoogleAnalytics|clicktag)\.js
        # Dangerous, breaks many sites and apps
        - \|\|tags.tiqcdn.com\^$
        # https://github.com/AdguardTeam/AdguardFilters/issues/219547
        - \|\|adx\.promo\^
        # https://x.com/428rinsuki/status/1994048111082344631
        - \|\|stat\.i3\.dmm\.com
        # https://github.com/DandelionSprout/adfilt/discussions/163#discussioncomment-14989561
        - \|\|nextdns\.io.*\$removeparam=from$
        # https://github.com/easylist/easylist/issues/22562
        - \|\|duplexer\.wix\.com\^
        # https://github.com/AdguardTeam/AdguardFilters/issues/212007#issuecomment-3426074352
        - \|\|lit\.link\/scripts\/geniee-ad-inline\.js
        # https://github.com/AdguardTeam/AdguardFilters/issues/215858
        - \|\|an.gr-wcon.com\^$
        # https://github.com/AdguardTeam/AdguardFilters/issues/215269
        - nhk-ondemand\.jp#%#.+wd\.s_c_il['"]
        # https://github.com/AdguardTeam/AdguardFilters/issues/214686
        - \|\|gmss.use1.prd.api.discomax.com\^$
        # https://github.com/AdguardTeam/AdguardFilters/issues/213803
        - app\.tuta\.com###modal:has.+upgradeReminder
        # https://github.com/easylist/easylist/issues/22306#issuecomment-3303661703
        - airasia\.com\/z\.js$
        # Causes high CPU usage on notion.so
        - \|\|http-inputs-notion.splunkcloud.com\^$
        # https://github.com/hagezi/dns-blocklists/issues/7276
        - datadog.pool.ntp.org\^$
        # https://github.com/AdguardTeam/AdguardFilters/issues/212409
        - \|\|pro-1w-dataaggregator.onelouder.com\^$
        # https://github.com/AdguardTeam/AdguardFilters/commit/3835ef566e40b6374717d39546663a19c2fa7716#r162211924
        - ^##a?\[href[^*]="(https?:\/\/)?lin\.ee\/?"\]\s$
        # It seems this sript also used by anti-bot protection.
        # I can't pay on Taobao when this script is blocked, and applied the scriptlet
        - ^\|\|g\.alicdn\.com\/alilog\/mlog\/aplus_v2\.js
        # Breaks player on Independent sites. It loads config of players
        - ^\|\|pub.pixels.ai\^$
        # Blocks LiveChat chats completely
        - ^\|\|(cdn\.)?livechatinc\.com/tracking\.js(?:$|\$domain=~[^\s]*$)
        # https://github.com/AdguardTeam/AdguardFilters/issues/208130#issuecomment-3012265450
        # Breaks search results
        - ^\|\|links.duckduckgo.com\/d\.js\?q=$
        # https://github.com/AdguardTeam/AdguardFilters/issues/207941
        - ^\|\|sstats\.adobe\.com\^$
        # https://github.com/AdguardTeam/AdguardFilters/issues/208079
        # Related to GDPR consents, may break sites
        - ^\|\|global\.ketchcdn\.com\^$
        # Used by Samsung Internet browser to load config
        - ^\|\|config-api.internet.apps.samsung.com\^$
        # https://github.com/AdguardTeam/AdguardFilters/issues/207250
        # Blocks the order confirmation popup
        - etsy.com##.wt-animated--slide-from-bottom$
        # DataDome bot protection. Visitor may be blocked, if this rule will be applied
        - \$cookie=datadome$
        # https://github.com/AdguardTeam/AdguardFilters/commit/2112d107b92d9dd45c7adfd5819f3f554fa4d132
        - \|\|(www\.)?youtube\.com\^\$removeparam=si$
        - ^\$removeparam=si,domain=(www\.)?youtube\.com
        # https://github.com/AdguardTeam/AdguardFilters/issues/206173#issuecomment-2913361836
        - \|\|oogiri-ads-bucket\.s3\.ap-northeast-3\.amazonaws.com\^$
        - oogiri-chaya.com##\.ads_insert$
        # https://github.com/easylist/easylist/issues/20673#issuecomment-2887148428
        - \|\|prodregistryv2\.org\^$
        # https://github.com/AdguardTeam/AdguardFilters/issues/203956
        - \|\|event\.notifier\.rakuten\.co\.jp\^$
        - \|\|ashiato\.travel\.rakuten\.co\.jp\^$
        # https://github.com/AdguardTeam/AdguardFilters/issues/198683
        - \|\|insights.alibaba.com\^$
        # https://github.com/AdguardTeam/AdguardFilters/issues/203905
        - \|\|roblox.com\^\$cookie=RBXEventTrackerV2
        # dropbox.com
        # Broken "Add account recovery" dialog when setting up 2FA
        # https://www.dropbox.com/account/security?enroll_mfa=1&mfa_checkpoint_token=
        - dropbox\.com##div\.dig-Banner\[role="alert"\]$
        - dropbox\.com##\.dig-Banner$
        # https://github.com/AdguardTeam/AdguardFilters/issues/202560
        - \|\|hotapi\*\.tiktokv\.\w{2,3}\^$
        # plvideo.ru - history will be broken
        - ^\|\|stat\.g2\.plvideo.ru\^
        # https://github.com/AdguardTeam/AdguardFilters/issues/157889#issuecomment-1660195416
        - ^\|\|amazon\.\*\$removeparam=psc$
        # https://github.com/AdguardTeam/AdguardFilters/issues/110571
        - ^\|\|amazon\.\*\$removeparam=ref$
        # https://github.com/AdguardTeam/AdguardFilters/issues/88627
        - ^\|\|amazon\.\*\$removeparam=ref_$
        - ^\|\|amazon\.\*\$removeparam=ie$
        # https://github.com/AdguardTeam/AdguardFilters/issues/89163
        - ^\|\|amazon\.\*\/message-us\$removeparam=origRef$
        # https://github.com/AdguardTeam/AdguardFilters/issues/148958
        # Breaks navigation and removes chosen seller id on the item's page
        - ^\|\|amazon\.\*\$removeparam=smid$
        # https://github.com/AdguardTeam/AdguardFilters/issues/201809
        # May break sites
        - \|\|sdk-v2\.conscent\.in\^(\$third-party)?$
        # https://github.com/AdguardTeam/AdGuardSDNSFilter/issues/1846
        - \|\|c-api-bit.shopeemobile.com\^
        # https://github.com/AdguardTeam/AdguardFilters/issues/201028
        - \|\|tapi.pureapk.com\^
        # https://github.com/AdguardTeam/AdguardFilters/issues/200159#issuecomment-2710664591
        - \|\|market\.yandex\.[a-z]*\$removeparam=do-waremd5
        # https://github.com/easylist/easylist/issues/21268
        - \|\|applicationinsights\.io\^
        # https://github.com/AdguardTeam/AdguardFilters/issues/184034
        - \|\|events.data.microsoft.com\^
        # https://github.com/AdguardTeam/AdguardFilters/issues/127008
        - \|\|bilibili.com\^\$removeparam=from$
        # https://github.com/AdguardTeam/AdguardFilters/issues/198810
        # Don't add any too simple filter for this domain without $path
        - ^ameblo\.jp##div:has\(
        - ameblo\.jp##div(\[class.=.+\])?:empty
        # Causes problems on PlayStation consoles
        - \|\|telemetry\.api\.playstation\.com
        # https://github.com/AdguardTeam/AdguardFilters/issues/197916
        - \|\|mobile\.pipe\.aria\.microsoft.com
        # https://github.com/AdguardTeam/AdguardFilters/issues/146493
        - \|\|log\.suumo\.jp
        # Popular baits. Sync with EasyList
        - ^##\.ad-area$
        - ^##\.sidebar-ad$
        - ^##\.Ad-Container$
        # Cause many false positives
        - ^##\.cookie-modal$
        - ^###cookie-modal$
        # https://github.com/AdguardTeam/AdguardFilters/issues/165972#issuecomment-1815708057
        - ^ameblo\.jp##\.pickCreative_root$
        # https://github.com/AdguardTeam/AdguardFilters/issues/191068#issuecomment-2480464336
        - ^(\/sd)?_ads_updater-$
        - ^\|\|b\.karte\.io
        - ^\|\|static\.karte\.io
        # https://github.com/AdguardTeam/AdguardFilters/commit/a64fb16a9c0ba926f980ca5091ca6d39eeb6ef40
        - ^tuma(douga)?\.jp##\.index_banner_space$
        - static-assets\.bamgrid\.com\/analytics
        - ^staff-start\.com\/js\/track\/
        - minkou.jp\/js\/tracking\.js
        - amazon.com\/1\/batch\/1\/OP\/
        - amazon.com\/1\/batch\/1\/OE\/
        # https://github.com/AdguardTeam/AdguardFilters/pull/189856#issuecomment-2422639077
        - youtube\.com\^\$removeparam=si$
        # https://github.com/AdguardTeam/AdguardFilters/issues/195335
        - syndication\.twitter\.com\^
        # https://github.com/AdguardTeam/AdguardFilters/issues/197918
        - fiverr\.com\^\$removeparam=ref$

```

### File: .markdownlint.json
```json
{
  "ul-indent": { "indent": 2 },
  "line-length": {
    "stern": true,
    "line_length": 120
  },
  "no-multiple-blanks": { "maximum": 2 },
  "no-inline-html": {
    "allowed_elements": ["a", "details", "summary", "img", "pre"]
  },
  "no-duplicate-header": { "siblings_only": true },
  "no-blanks-blockquote": false,
  "no-bare-urls": false,
  "ul-style": { "style": "dash" },
  "blanks-around-fences": { "list_items": false },
  "emphasis-style": { "style": "asterisk" },
  "descriptive-link-text": false
}

```

### File: CONTRIBUTING.md
```md
# Contributing to AdGuard filters

If you want to make AdGuard better by creating new rules, follow the
instructions below to make your ideas come to life faster!

## Pre-requisites

- You need to have a [GitHub account][createaccount] to make contributions.
- You need to have the following tools installed on your machine:
  - [Git][git]
  - [Node.js][nodejs] (we recommend using the latest LTS version)
  - [Visual Studio Code][vscode] (we recommend using this editor)
    - Install the recommended extensions for VSCode (listed in `.vscode/extensions.json`).
      - At first launch, you will be prompted to install them. If not, press `CTRL+SHIFT+P` and type
      `Show Recommended Extensions` and install them.
      - Please note that, by default Comment Anchors does not know adblock-style comments (like `! this is a comment`),
        so you'll need to add `!` as a match prefix in the `commentAnchors.tags.matchPrefix` setting
        (File -> Preferences -> Settings -> Extensions -> Comment Anchors Configuration).

[createaccount]: https://github.com/signup
[git]: https://git-scm.com/downloads
[nodejs]: https://nodejs.org/en/download
[vscode]: https://code.visualstudio.com/download

## Setting up the repository

After you have installed the necessary tools, you need to set up the repository.

1. Fork the original repository on GitHub. This will create a copy of the repository in your account.
1. Clone remote repository from GitHub to your local machine.
1. Install the dependencies by running the following command in the terminal:
   ```bash
   npm install
   ```
   This will install necessary tools like [AGLint][aglint] and initialize [Husky][husky] hooks.

[aglint]: https://github.com/AdguardTeam/AGLint
[husky]: https://typicode.github.io/husky

## Workflow for submitting changes

1. Create a new branch for your changes. Please use the following naming convention:
   `fix/123` where `123` is the issue number you're working on.
1. Make your changes, test them and put them in the proper file or section of the file.
   - You can learn how to write filtering rules in the [How to write filter rules][how-to-write-filters] section.
   - Before creating any rules, please read and understand the current
  [AdGuard filters policy][policy].
  By contributing, you confirm your agreement to follow this policy and
  create rules in accordance with it.
   - One of its most important points is the [quality requirements][qualityrequirements].
   - When you're done with creating rules, please take a look at the similar ones in the filters.
     This may help you to make a better version of the rule.
   - Please read the [Repository structure](#repository-structure) section below
     to learn more about the structure of the repo and where to put your rules.
1. If everything is fine, commit your changes. Please try to separate branches and commits
   for different issues and don't mix them in one. It is easier to manage and review them that way.
   - Note: By default, Husky pre-commit hook will run AGLint on your changes and will prevent you from committing
     if there are any errors in your changes.
1. Push your new branch to your remote repository.
1. Create a pull request from your branch to the `master` branch of the original repository.
   AGLint will run automatically on your PR and will report any errors.
   If there are any errors, fix them and push your changes to your fork.
   If AGLint passes, your PR will be reviewed by a maintainer.
1. If the review is successful, your changes will be merged into the `master` branch.

### Skipping checks

If you need to skip running checks, you can do it in the following ways.
Please note that it is only allowed in special cases and should not be used as a regular practice.

- Skip running Husky pre-commit hook: `git commit --no-verify -m "commit message"`.
- Skip running checks on GitHub: add `[skip ci]` to the commit message as a prefix.

[policy]: https://adguard.com/kb/general/ad-filtering/filter-policy/
[qualityrequirements]: https://adguard.com/kb/general/ad-filtering/filter-policy/#quality-requirements-for-filtering-rules
[how-to-write-filters]: https://adguard.com/kb/general/ad-filtering/create-own-filters/

## Repository structure

AdGuard filters are compiled from files in this repository. This is an automated
process that is periodically run by scripts in the [FiltersRegistry][registry]
repo. In this repository, each filter list is divided into several files, and
each file has its own purpose. If you're adding a new rule, make sure it is
added to the proper file or section of the file.

General requirements for submitting rules: don't add rules to the beginning of
the file, start entering them from line 4, for example. If you add rules with
a task comment or hints, put them next to the same structure in the file.

[registry]: https://github.com/AdguardTeam/FiltersRegistry

### AdGuard Base filter

- Purpose: this filter blocks various kinds of ads mostly on English-language
  and multilingual sites.
- [Base folder](https://github.com/AdguardTeam/AdguardFilters/tree/master/BaseFilter/sections)
- Notes: The AdGuard Base filter includes [Easylist][easylist],
  so there's no need to add rules which are already in `Easylist`.

[easylist]: https://github.com/easylist/easylist

### AdGuard Mobile filter

- Purpose: this filter blocks various kinds of ads on mobile version of sites
  and in mobile apps.
- [Mobile folder](https://github.com/AdguardTeam/AdguardFilters/tree/master/MobileFilter/sections)

### AdGuard Tracking Protection filter

- Purpose: this filter hides your actions online and helps avoid tracking.
- [Tracking Protection folder](https://github.com/AdguardTeam/AdguardFilters/tree/master/SpywareFilter/sections)

### AdGuard URL Tracking filter

- Purpose: this filter removes various kinds of tracking parameters from sites.
- [URL Tracking folder](https://github.com/AdguardTeam/AdguardFilters/tree/master/TrackParamFilter/sections)

### AdGuard Social filter

- Purpose: this filter blocks various kinds of social widgets from sites.
- [Social folder](https://github.com/AdguardTeam/AdguardFilters/tree/master/SocialFilter/sections)

### AdGuard Annoyances filters

- Purpose: this filter blocks irritating elements on web pages including cookie
  notices, third-party widgets and in-page pop-ups.
- [Annoyances folder](https://github.com/AdguardTeam/AdguardFilters/tree/master/AnnoyancesFilter)

  Contains the following AdGuard filters: Cookie Notices, Popups, Mobile
  App Banners, Other Annoyances and Widgets:

  - **Cookie Notices**

     Purpose: this filter blocks cookie notices on web pages.
    - [Cookies folder](https://github.com/AdguardTeam/AdguardFilters/tree/master/AnnoyancesFilter/Cookies/sections)

  - **Mobile App Banners**

    - Purpose: this filter blocks irritating banners that promote mobile apps
      of websites.
    - [MobileApp folder](https://github.com/AdguardTeam/AdguardFilters/tree/master/AnnoyancesFilter/MobileApp/sections)

  - **Popups**

    - Purpose: this filter blocks all kinds of pop-ups that are not necessary
      for websites' operation.
    - [Popups folder](https://github.com/AdguardTeam/AdguardFilters/tree/master/AnnoyancesFilter/Popups/sections)

  - **Widgets**

    - Purpose: this filter blocks annoying third-party widgets: online
      assistants, live support chats, etc.
    - [Widgets folder](https://github.com/AdguardTeam/AdguardFilters/tree/master/AnnoyancesFilter/Widgets/sections)

  - **Other Annoyances**
    - Purpose: this filter blocks irritating elements on web pages that do not
      fall under the popular categories of annoyances.
    - [Other folder](https://github.com/AdguardTeam/AdguardFilters/tree/master/AnnoyancesFilter/Other/sections)

### AdGuard Experimental filter

- Purpose: this filter serves to test some new filtering rules that can
  potentially cause conflicts and mess with websites' work. In case these rules
  perform without any issues, they get added to main filters.
- [Experimental folder](https://github.com/AdguardTeam/AdguardFilters/tree/master/ExperimentalFilter/sections)

### AdGuard Filter unblocking search ads and self-promotions

- Purpose: this filter unblocks search engine result that may be useful to
  users.
- [UsefulAdsFilter folder](https://github.com/AdguardTeam/AdguardFilters/tree/master/UsefulAdsFilter/sections)

### AdGuard Russian filter

- Purpose: this filter blocks various kinds of ads on Russian-language sites.
- [Russian folder](https://github.com/AdguardTeam/AdguardFilters/tree/master/CyrillicFilters/RussianFilter/sections)

### AdGuard Ukrainian filter

- Purpose: this filter blocks various kinds of ads on Ukrainian-language sites.
- [Ukrainian folder](https://github.com/AdguardTeam/AdguardFilters/tree/master/CyrillicFilters/UkrainianFilter/sections)

### AdGuard Chinese filter

- Purpose: this filter blocks various kinds of ads on Chinese-language sites.
- [Chinese folder](https://github.com/AdguardTeam/AdguardFilters/tree/master/ChineseFilter/sections)
- Notes: The AdGuard Chinese filter includes [Easylist China][easylistchina],
  so there's no need to add rules which are already in `Easylist China`.

[easylistchina]: https://github.com/easylist/easylistchina

### AdGuard Dutch filter

- Purpose: this filter blocks various kinds of ads on Dutch-language sites.
- [Dutch folder](https://github.com/AdguardTeam/AdguardFilters/tree/master/DutchFilter/sections)

### AdGuard French filter

- Purpose: this filter blocks various kinds of ads on French-language sites.
- [French folder](https://github.com/AdguardTeam/AdguardFilters/tree/master/FrenchFilter/sections)
- Notes: The AdGuard French filter includes [Liste FR][listefr],
  so there's no need to add rules which are already in `Liste FR`.

[listefr]: https://github.com/easylist/listefr

### AdGuard German filter

- Purpose: this filter blocks various kinds of ads on German-language sites.
- [German folder](https://github.com/AdguardTeam/AdguardFilters/tree/master/GermanFilter/sections)
- Notes: The AdGuard German filter includes [Easylist Germany][easylistgermany],
  so there's no need to add rules which are already in `Easylist Germany`.

[easylistgermany]: https://github.com/easylist/easylistgermany

### AdGuard Japanese filter

- Purpose: this filter blocks various kinds of ads on Japanese-language sites.
- [Japanese folder](https://github.com/AdguardTeam/AdguardFilters/tree/master/JapaneseFilter/sections)

### AdGuard Spanish filter

- Purpose: this filter blocks various kinds of ads on Spanish-language and
  Portuguese-language sites.
- [Spanish folder](https://github.com/AdguardTeam/AdguardFilters/tree/master/SpanishFilter/sections)

### AdGuard Turkish filter

- Purpose: this filter blocks various kinds of ads on Turkish-language sites.
- [Turkish folder](https://github.com/AdguardTeam/AdguardFilters/tree/master/TurkishFilter/sections)

### AdGuard Quick Fixes filter

- Purpose: This filter serves as a quick-response solution, ensuring that AdGuard MV3 extension
  users experience minimal disruption while awaiting updates of the extension with static filters.
- [Quick Fixes folder](https://github.com/AdguardTeam/AdguardFilters/tree/master/QuickFixesFilter/sections)
- Notes: Used in MV3 extension only.

```

### File: ddl_ignore.txt
```txt
! A list of known useful low-traffic sites are mistakenly detected as dead,
! e.g. tools, highly specialized resources.
! Domains must be accompanied by comments
! NOTE: it is not supported by DeadDomainsLinter right now, but can be used during manual checks

```

### File: KNOWN_ISSUES.md
```md
# The list of the filtering related bugs and problems

## Known filtering problems should be added to this list

For each problem there should be opened an issue in the corresponding repository

```

### File: package-lock.json
```json
{
    "name": "@adguard/filters",
    "lockfileVersion": 3,
    "requires": true,
    "packages": {
        "": {
            "name": "@adguard/filters",
            "license": "GPL-3.0-only",
            "devDependencies": {
                "@adguard/aglint": "4.0.0-beta.5",
                "husky": "^9.1.7",
                "lint-staged": "^16.3.2",
                "markdownlint": "^0.40.0",
                "markdownlint-cli": "^0.48.0"
            },
            "engines": {
                "node": ">=20.0.0"
            }
        },
        "node_modules/@adguard/aglint": {
            "version": "4.0.0-beta.5",
            "resolved": "https://registry.npmjs.org/@adguard/aglint/-/aglint-4.0.0-beta.5.tgz",
            "integrity": "sha512-8ceBChpdFC8Vsg+Ud6nnHd3tw19Q40VyJmWuWGuu9/bT4IBTbj9gNc0/gJyKbk3v20vCtheHeGSifVzvt9BObA==",
            "dev": true,
            "license": "MIT",
            "dependencies": {
                "@adguard/agtree": "^3.4.1",
                "@adguard/ecss-tree": "^2.0.1",
                "@inquirer/checkbox": "^4.3.0",
                "@inquirer/confirm": "^6.0.1",
                "@inquirer/select": "^4.4.0",
                "@valibot/to-json-schema": "^1.3.0",
                "chalk": "5.6.2",
                "clone-deep": "^4.0.1",
                "commander": "^14.0.1",
                "deepmerge": "^4.3.1",
                "detect-indent": "^7.0.2",
                "detect-newline": "^4.0.1",
                "esquery": "^1.6.0",
                "fast-fuzzy": "^1.12.0",
                "fast-glob": "^3.3.3",
                "glob-parent": "^6.0.2",
                "ignore": "^5.2.4",
                "inflection": "^2.0.1",
                "is-glob": "^4.0.3",
                "micromustache": "^8.0.3",
                "object-inspect": "^1.13.4",
                "ohash": "^2.0.11",
                "piscina": "^5.1.3",
                "strip-ansi": "6.0.1",
                "terminal-link": "2.1.1",
                "text-table": "^0.2.0",
                "valibot": "^1.1.0",
                "yaml": "^2.8.1"
            },
            "bin": {
                "aglint": "dist/cli/bin.js"
            },
            "engines": {
                "node": ">=20"
            }
        },
        "node_modules/@adguard/agtree": {
            "version": "3.4.3",
            "resolved": "https://registry.npmjs.org/@adguard/agtree/-/agtree-3.4.3.tgz",
            "integrity": "sha512-T838KvYtWu3K6whQ46YLaIXYA7PbszX9QRp4dvNfF8iWdp98tcKHxXWslBwUN1DkcBOqqj4rrkarLmcwT2iAbg==",
            "dev": true,
            "license": "MIT",
            "dependencies": {
                "@adguard/css-tokenizer": "^1.2.0",
                "camelcase-keys": "^7.0.2",
                "clone-deep": "^4.0.1",
                "is-ip": "3.1.0",
                "json5": "^2.2.3",
                "sprintf-js": "^1.1.3",
                "tldts": "^5.7.112",
                "xregexp": "^5.1.1",
                "zod": "3.24.4"
            },
            "engines": {
                "node": ">=22"
            }
        },
        "node_modules/@adguard/css-tokenizer": {
            "version": "1.2.0",
            "resolved": "https://registry.npmjs.org/@adguard/css-tokenizer/-/css-tokenizer-1.2.0.tgz",
            "integrity": "sha512-cUj5j/AU5z/T4//5M6KnIJBpykAY4QbDsoiQ2DaWX/r2XkepMkTb8DhIbUHJD/QLGEyLeQLpi+nlxAgf4NTRRQ==",
            "dev": true,
            "license": "MIT"
        },
        "node_modules/@adguard/ecss-tree": {
            "version": "2.0.1",
            "resolved": "https://registry.npmjs.org/@adguard/ecss-tree/-/ecss-tree-2.0.1.tgz",
            "integrity": "sha512-GvVz3rLQqcZkNVpUbdowimokhPxNL6pODwmZbiWTUfa3bEAT7XI+4ydxVZmtK2WS2u7qu/IISmI69PSFXE0ucw==",
            "dev": true,
            "license": "MIT",
            "dependencies": {
                "@adguard/css-tokenizer": "^1.2.0",
                "@eslint/css-tree": "3.6.6"
            }
        },
        "node_modules/@babel/runtime-corejs3": {
            "version": "7.28.4",
            "resolved": "https://registry.npmjs.org/@babel/runtime-corejs3/-/runtime-corejs3-7.28.4.tgz",
            "integrity": "sha512-h7iEYiW4HebClDEhtvFObtPmIvrd1SSfpI9EhOeKk4CtIK/ngBWFpuhCzhdmRKtg71ylcue+9I6dv54XYO1epQ==",
            "dev": true,
            "license": "MIT",
            "dependencies": {
                "core-js-pure": "^3.43.0"
            },
            "engines": {
                "node": ">=6.9.0"
            }
        },
        "node_modules/@eslint/css-tree": {
            "version": "3.6.6",
            "resolved": "https://registry.npmjs.org/@eslint/css-tree/-/css-tree-3.6.6.tgz",
            "integrity": "sha512-C3YiJMY9OZyZ/3vEMFWJIesdGaRY6DmIYvmtyxMT934CbrOKqRs+Iw7NWSRlJQEaK4dPYy2lZ2y1zkaj8z0p5A==",
            "dev": true,
            "license": "MIT",
            "dependencies": {
                "mdn-data": "2.23.0",
                "source-map-js": "^1.0.1"
            },
            "engines": {
                "node": "^10 || ^12.20.0 || ^14.13.0 || >=15.0.0"
            }
        },
        "node_modules/@inquirer/ansi": {
            "version": "1.0.2",
            "resolved": "https://registry.npmjs.org/@inquirer/ansi/-/ansi-1.0.2.tgz",
            "integrity": "sha512-S8qNSZiYzFd0wAcyG5AXCvUHC5Sr7xpZ9wZ2py9XR88jUz8wooStVx5M6dRzczbBWjic9NP7+rY0Xi7qqK/aMQ==",
            "dev": true,
            "license": "MIT",
            "engines": {
                "node": ">=18"
            }
        },
        "node_modules/@inquirer/checkbox": {
            "version": "4.3.2",
            "resolved": "https://registry.npmjs.org/@inquirer/checkbox/-/checkbox-4.3.2.tgz",
            "integrity": "sha512-VXukHf0RR1doGe6Sm4F0Em7SWYLTHSsbGfJdS9Ja2bX5/D5uwVOEjr07cncLROdBvmnvCATYEWlHqYmXv2IlQA==",
            "dev": true,
            "license": "MIT",
            "dependencies": {
                "@inquirer/ansi": "^1.0.2",
                "@inquirer/core": "^10.3.2",
                "@inquirer/figures": "^1.0.15",
                "@inquirer/type": "^3.0.10",
                "yoctocolors-cjs": "^2.1.3"
            },
            "engines": {
                "node": ">=18"
            },
            "peerDependencies": {
                "@types/node": ">=18"
            },
            "peerDependenciesMeta": {
                "@types/node": {
                    "optional": true
                }
            }
        },
        "node_modules/@inquirer/confirm": {
            "version": "6.0.3",
            "resolved": "https://registry.npmjs.org/@inquirer/confirm/-/confirm-6.0.3.tgz",
            "integrity": "sha512-lyEvibDFL+NA5R4xl8FUmNhmu81B+LDL9L/MpKkZlQDJZXzG8InxiqYxiAlQYa9cqLLhYqKLQwZqXmSTqCLjyw==",
            "dev": true,
            "license": "MIT",
            "dependencies": {
                "@inquirer/core": "^11.1.0",
                "@inquirer/type": "^4.0.2"
            },
            "engines": {
                "node": ">=23.5.0 || ^22.13.0 || ^21.7.0 || ^20.12.0"
            },
            "peerDependencies": {
                "@types/node": ">=18"
            },
            "peerDependenciesMeta": {
                "@types/node": {
                    "optional": true
                }
            }
        },
        "node_modules/@inquirer/confirm/node_modules/@inquirer/ansi": {
            "version": "2.0.2",
            "resolved": "https://registry.npmjs.org/@inquirer/ansi/-/ansi-2.0.2.tgz",
            "integrity": "sha512-SYLX05PwJVnW+WVegZt1T4Ip1qba1ik+pNJPDiqvk6zS5Y/i8PhRzLpGEtVd7sW0G8cMtkD8t4AZYhQwm8vnww==",
            "dev": true,
            "license": "MIT",
            "engines": {
                "node": ">=23.5.0 || ^22.13.0 || ^21.7.0 || ^20.12.0"
            }
        },
        "node_modules/@inquirer/confirm/node_modules/@inquirer/core": {
            "version": "11.1.0",
            "resolved": "https://registry.npmjs.org/@inquirer/core/-/core-11.1.0.tgz",
            "integrity": "sha512-+jD/34T1pK8M5QmZD/ENhOfXdl9Zr+BrQAUc5h2anWgi7gggRq15ZbiBeLoObj0TLbdgW7TAIQRU2boMc9uOKQ==",
            "dev": true,
            "license": "MIT",
            "dependencies": {
                "@inquirer/ansi": "^2.0.2",
                "@inquirer/figures": "^2.0.2",
                "@inquirer/type": "^4.0.2",
                "cli-width": "^4.1.0",
                "mute-stream": "^3.0.0",
                "signal-exit": "^4.1.0",
                "wrap-ansi": "^9.0.2"
            },
            "engines": {
                "node": ">=23.5.0 || ^22.13.0 || ^21.7.0 || ^20.12.0"
            },
            "peerDependencies": {
                "@types/node": ">=18"
            },
            "peerDependenciesMeta": {
                "@types/node": {
                    "optional": true
                }
            }
        },
        "node_modules/@inquirer/confirm/node_modules/@inquirer/figures": {
            "version": "2.0.2",
            "resolved": "https://registry.npmjs.org/@inquirer/figures/-/figures-2.0.2.tgz",
            "integrity": "sha512-qXm6EVvQx/FmnSrCWCIGtMHwqeLgxABP8XgcaAoywsL0NFga9gD5kfG0gXiv80GjK9Hsoz4pgGwF/+CjygyV9A==",
            "dev": true,
            "license": "MIT",
            "engines": {
                "node": ">=23.5.0 || ^22.13.0 || ^21.7.0 || ^20.12.0"
            }
        },
        "node_modules/@inquirer/confirm/node_modules/@inquirer/type": {
            "version": "4.0.2",
            "resolved": "https://registry.npmjs.org/@inquirer/type/-/type-4.0.2.tgz",
            "integrity": "sha512-cae7mzluplsjSdgFA6ACLygb5jC8alO0UUnFPyu0E7tNRPrL+q/f8VcSXp+cjZQ7l5CMpDpi2G1+IQvkOiL1Lw==",
            "dev": true,
            "license": "MIT",
            "engines": {
                "node": ">=23.5.0 || ^22.13.0 || ^21.7.0 || ^20.12.0"
            },
            "peerDependencies": {
                "@types/node": ">=18"
            },
            "peerDependenciesMeta": {
                "@types/node": {
                    "optional": true
                }
            }
        },
        "node_modules/@inquirer/confirm/node_modules/ansi-regex": {
            "version": "6.2.2",
            "resolved": "https://registry.npmjs.org/ansi-regex/-/ansi-regex-6.2.2.tgz",
            "integrity": "sha512-Bq3SmSpyFHaWjPk8If9yc6svM8c56dB5BAtW4Qbw5jHTwwXXcTLoRMkpDJp6VL0XzlWaCHTXrkFURMYmD0sLqg==",
            "dev": true,
            "license": "MIT",
            "engines": {
                "node": ">=12"
            },
            "funding": {
                "url": "https://github.com/chalk/ansi-regex?sponsor=1"
            }
        },
        "node_modules/@inquirer/confirm/node_modules/mute-stream": {
            "version": "3.0.0",
            "resolved": "https://registry.npmjs.org/mute-stream/-/mute-stream-3.0.0.tgz",
            "integrity": "sha512-dkEJPVvun4FryqBmZ5KhDo0K9iDXAwn08tMLDinNdRBNPcYEDiWYysLcc6k3mjTMlbP9KyylvRpd4wFtwrT9rw==",
            "dev": true,
            "license": "ISC",
            "engines": {
                "node": "^20.17.0 || >=22.9.0"
            }
        },
        "node_modules/@inquirer/confirm/node_modules/string-width": {
            "version": "7.2.0",
            "resolved": "https://registry.npmjs.org/string-width/-/string-width-7.2.0.tgz",
            "integrity": "sha512-tsaTIkKW9b4N+AEj+SVA+WhJzV7/zMhcSu78mLKWSk7cXMOSHsBKFWUs0fWwq8QyK3MgJBQRX6Gbi4kYbdvGkQ==",
            "dev": true,
            "license": "MIT",
            "dependencies": {
                "emoji-regex": "^10.3.0",
                "get-east-asian-width": "^1.0.0",
                "strip-ansi": "^7.1.0"
            },
            "engines": {
                "node": ">=18"
            },
            "funding": {
                "url": "https://github.com/sponsors/sindresorhus"
            }
        },
        "node_modules/@inquirer/confirm/node_modules/strip-ansi": {
            "version": "7.1.2",
            "resolved": "https://registry.npmjs.org/strip-ansi/-/strip-ansi-7.1.2.tgz",
            "integrity": "sha512-gmBGslpoQJtgnMAvOVqGZpEz9dyoKTCzy2nfz/n8aIFhN/jCE/rCmcxabB6jOOHV+0WNnylOxaxBQPSvcWklhA==",
            "dev": true,
            "license": "MIT",
            "dependencies": {
                "ansi-regex": "^6.0.1"
            },
            "engines": {
                "node": ">=12"
            },
            "funding": {
                "url": "https://github.com/chalk/strip-ansi?sponsor=1"
            }
        },
        "node_modules/@inquirer/confirm/node_modules/wrap-ansi": {
            "version": "9.0.2",
            "resolved": "https://registry.npmjs.org/wrap-ansi/-/wrap-ansi-9.0.2.tgz",
            "integrity": "sha512-42AtmgqjV+X1VpdOfyTGOYRi0/zsoLqtXQckTmqTeybT+BDIbM/Guxo7x3pE2vtpr1ok6xRqM9OpBe+Jyoqyww==",
            "dev": true,
            "license": "MIT",
            "dependencies": {
                "ansi-styles": "^6.2.1",
                "string-width": "^7.0.0",
                "strip-ansi": "^7.1.0"
            },
            "engines": {
                "node": ">=18"
            },
            "funding": {
                "url": "https://github.com/chalk/wrap-ansi?sponsor=1"
            }
        },
        "node_modules/@inquirer/core": {
            "version": "10.3.2",
            "resolved": "https://registry.npmjs.org/@inquirer/core/-/core-10.3.2.tgz",
            "integrity": "sha512-43RTuEbfP8MbKzedNqBrlhhNKVwoK//vUFNW3Q3vZ88BLcrs4kYpGg+B2mm5p2K/HfygoCxuKwJJiv8PbGmE0A==",
            "dev": true,
            "license": "MIT",
            "dependencies": {
                "@inquirer/ansi": "^1.0.2",
                "@inquirer/figures": "^1.0.15",
                "@inquirer/type": "^3.0.10",
                "cli-width": "^4.1.0",
                "mute-stream": "^2.0.0",
                "signal-exit": "^4.1.0",
                "wrap-ansi": "^6.2.0",
                "yoctocolors-cjs": "^2.1.3"
            },
            "engines": {
                "node": ">=18"
            },
            "peerDependencies": {
                "@types/node": ">=18"
            },
            "peerDependenciesMeta": {
                "@types/node": {
                    "optional": true
                }
            }
        },
        "node_modules/@inquirer/figures": {
            "version": "1.0.15",
            "resolved": "https://registry.npmjs.org/@inquirer/figures/-/figures-1.0.15.tgz",
            "integrity": "sha512-t2IEY+unGHOzAaVM5Xx6DEWKeXlDDcNPeDyUpsRc6CUhBfU3VQOEl+Vssh7VNp1dR8MdUJBWhuObjXCsVpjN5g==",
            "dev": true,
            "license": "MIT",
            "engines": {
                "node": ">=18"
            }
        },
        "node_modules/@inquirer/select": {
            "version": "4.4.2",
            "resolved": "https://registry.npmjs.org/@inquirer/select/-/select-4.4.2.tgz",
            "integrity": "sha512-l4xMuJo55MAe+N7Qr4rX90vypFwCajSakx59qe/tMaC1aEHWLyw68wF4o0A4SLAY4E0nd+Vt+EyskeDIqu1M6w==",
            "dev": true,
            "license": "MIT",
            "dependencies": {
                "@inq
... [TRUNCATED]
```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.

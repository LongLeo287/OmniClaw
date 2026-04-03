---
id: lobsters-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:29:05.795224
---

# KNOWLEDGE EXTRACT: lobsters
> **Extracted on:** 2026-03-30 17:42:03
> **Source:** lobsters

---

## File: `lobsters.md`
```markdown
# 📦 lobsters/lobsters [🔖 PENDING/APPROVE]
🔗 https://github.com/lobsters/lobsters
🌐 https://lobste.rs

## Meta
- **Stars:** ⭐ 4624 | **Forks:** 🍴 942
- **Language:** Ruby | **License:** NOASSERTION
- **Last updated:** 2026-03-24
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Computing-focused community centered around link aggregation and discussion

## README (trích đầu)
```
### Lobsters Rails Project [![build status](https://github.com/lobsters/lobsters/actions/workflows/check.yml/badge.svg)](https://github.com/lobsters/lobsters/actions/workflows/check.yml)

[Lobsters](https://lobste.rs) is a Rails codebase and uses a SQL (MariaDB in production) backend for the database.
The code is open source as part of our [commitment to transparency](https://lobste.rs/about#transparency).
It's been used to run [sister sites](https://github.com/lobsters/lobsters/blob/main/sister_sites.md), but mostly we want people to be able to understand and improve what's happening on Lobsters itself.

Despite the site being an [uber mega cringe](https://bsky.app/profile/anirudh.fi/post/3mdikk6u2w22e) [ghost town](https://xcancel.com/webshitweekly/status/1399935275057389571) running on a [quite sad codebase](https://web.archive.org/web/20230213161624/https://old.reddit.com/r/rails/comments/6jz7tq/source_code_lobsters_a_hacker_news_clone_built/), at least we have [no relation](https://lobste.rs/about#michaelbolton) to the self-help guru.


#### Contributing bugfixes and new features

We'd love to have your help.
Please see the [CONTRIBUTING](https://github.com/lobsters/lobsters/blob/main/CONTRIBUTING.md) file for details and dev environment setup.
If you have questions, there is usually someone in [our chat room](https://lobste.rs/chat) who's familiar with the code.

Lobsters is a volunteer project with limited development time and a long time horizon, we hope to be running for decades.
So our design philosophy is a little different than a typical commercial product:

 * We started with Rails 3.2.2 in 2012, so we have a few dusty corners and places where we don't take advantage of features that were introduced since we started.
 * We lean into using Rails features instead of custom code, and we'll write a couple dozen lines of narrow code for a feature rather than add a dependency that might require maintenance.
 * We are very reluctant to add new production services and almost entirely unwilling to depend on external services.
   We take pride in self-hosting from the VPS up, which necessitates reducing the number of moving parts.
 * We test to ensure functionality, but testing is a lot lighter for moderator and other non-core features.
   We're trying to maximize the return on investment of testing rather than minimize errors.
 * We're willing to take downtime for big code changes rather than try to make them seamless.
 * We have users that are unusually likely to use old, experimental, and even homemade browsers, so we only use CSS in the [widely available baseline](https://web-platform-dx.github.io/web-features/).
 * We don't serve JavaScript to logged-out visitors, we use as little JS as possible for users with a vanilla/jQuery-style of DOM attachment, we are (very slowly) making JS entirely optional for users, and we accept JS for mod features.
   Keeping JS small and optional helps keep the site fast, and an unusually high proportion of 
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```


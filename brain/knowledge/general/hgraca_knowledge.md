---
id: hgraca-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:52.004290
---

# KNOWLEDGE EXTRACT: hgraca
> **Extracted on:** 2026-03-30 17:38:06
> **Source:** hgraca

---

## File: `explicit-architecture-php.md`
```markdown
# 📦 hgraca/explicit-architecture-php [🔖 PENDING/APPROVE]
🔗 https://github.com/hgraca/explicit-architecture-php


## Meta
- **Stars:** ⭐ 730 | **Forks:** 🍴 103
- **Language:** PHP | **License:** MIT
- **Last updated:** 2026-03-24
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
This repository is a demo of Explicit Architecture, using the Symfony Demo Application.

## README (trích đầu)
```
# Explicit Architecture 

[![Author][Author]](https://www.herbertograca.com)
[![Software License][License]](LICENSE)

[![Build Status][Build]](https://scrutinizer-ci.com/g/hgraca/explicit-architecture-php/build-status/master)
[![Scrutinizer Code Quality][Score]](https://scrutinizer-ci.com/g/hgraca/explicit-architecture-php/?branch=master)
[![CodeCov][CodeCov]](https://codecov.io/gh/hgraca/explicit-architecture-php)

[![Code Intelligence Status][CodeInt]](https://scrutinizer-ci.com/code-intelligence)

## Symfony Demo Application

The "Symfony Demo Application" is a reference application created to show how
to develop Symfony applications following the recommended best practices.

This repository is a demo of [Explicit Architecture][1], using the [Symfony Demo Application][2].

There is code in this project that not used and therefore it would be removed in a real project, nevertheless 
it was included here as examples.

### Explicit Architecture

I explained [Explicit Architecture][1] in one of my blog posts, as a result of my understanding of several architectural
 ideas such as (but not limited to) [EBI Architecture][11], [DDD][12], [Ports & Adapters Architecture][13], 
 [Onion Architecture][14] and [Clean Architecture][15].
 
[![Explicit Architecture](https://docs.google.com/drawings/d/e/2PACX-1vQ5ps72uaZcEJzwnJbPhzUfEeBbN6CJ04j7hl2i3K2HHatNcsoyG2tgX2vnrN5xxDKLp5Jm5bzzmZdv/pub?w=960&amp;h=657)][2]

#### Package by component

[![Package by component](https://docs.google.com/drawings/d/e/2PACX-1vQjEj4dKKUaQEUcNDq2UO58oIUu6pehqrE99q4gSRk0DY9KPIuhgG9Yg3qJGgW4ybrL5Ql8_Xo5z3yq/pub?w=960&h=720)][17]

#### Dependencies directions

[![Dependencies](https://docs.google.com/drawings/d/e/2PACX-1vQyv5xAx5hFJPhiK19AGl_2t256M0yKcDSliH8etojltE3tBlEnCndwfsUr1UsXvv5PKGVtrBHkQX3h/pub?w=913&amp;h=129)][16]

#### Folder structure

- **bin** (_application binaries, however the dependencies binaries should go in vendor/bin_)
- **build** (_artifacts needed for building the application prior to running it_)
- **config** (_all the config needed to run the application_)
- **docs** (_application documentation_)
- **lib** (_libraries used by the application, which are specific to this application and/or not distributable_)
    - **php-extension**  (_code to be used as if it was part of the language itself_)
        - _src_
        - _tests_
- **public** (_the entry point to the application, and public frontend artifacts like CSS and JS files_)
- **src**
    - **[Core][10]** (_the application core_)
        - **[Component][5]** (_the application components/bounded contexts_)
        - **[Port][8]** (_the ports, to be implemented by the infrastructure adapters_)
        - **[SharedKernel][6]** (_application and domain code shared among all components/bounded contexts_)
    - **[Infrastructure][9]** (_the port adapters for the infrastructure tools_)
    - **[Presentation][7]** (_the presentation layer with the several user facing applications, controllers, views and related c
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```


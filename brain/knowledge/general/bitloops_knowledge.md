---
id: bitloops-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:18:57.872336
---

# KNOWLEDGE EXTRACT: bitloops
> **Extracted on:** 2026-03-30 17:30:49
> **Source:** bitloops

---

## File: `bitloops-language.md`
```markdown
# 📦 bitloops/bitloops-language [🔖 PENDING/APPROVE]
🔗 https://github.com/bitloops/bitloops-language
🌐 https://bitloops.com/bitloops-language

## Meta
- **Stars:** ⭐ 358 | **Forks:** 🍴 19
- **Language:** TypeScript | **License:** GPL-3.0
- **Last updated:** 2026-02-17
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Open-source transpiled programming language that helps you write clean code, well-designed systems, and build high-quality software that is testable, auditable and maintainable. Like what you see? Don't forget to star! :star: ^^^

## README (trích đầu)
```
![Bitloops](https://storage.googleapis.com/bitloops-github-assets/github-readme-image.png)

<p align="center">
  <a href="https://bitloops.com/brain/knowledge/docs_legacy/bitloops-language/category/quick-start">Quick Start</a> |
  <a href="https://github.com/bitloops/bitloops-language#-what-are-the-benefits-of-using-bitloops-language">Benefits</a> |
  <a href="https://github.com/bitloops/bitloops-language#%EF%B8%8F-why-build-the-bitloops-language">Why?</a> |
  <a href="https://github.com/bitloops/bitloops-language#-language-goals">Goals</a> |
  <a href="https://github.com/bitloops/bitloops-language#-project-status">Project Status</a> |
  <a href="https://discord.gg/vj8EdZx8gK">Discord</a> |
  <a href="https://github.com/bitloops/bitloops-language/discussions">GitHub Discussions</a> |
  <a href="https://github.com/bitloops/bitloops-language/issues">GitHub Issues</a> |
  <a href="https://github.com/bitloops/bitloops-language/blob/main/CONTRIBUTING.md">Contributing</a>
</p>

## 🚀 Build great modular monoliths or microservices faster, much faster

Bitloops Language (BL) is a high-productivity, domain specific language (DSL) that helps you focus on the business logic of your application which is what really matters.

It incorporates software development best practices and design methodologies such as [DDD](https://bitloops.com/brain/knowledge/docs_legacy/bitloops-language/learning/domain-driven-design), [BDD](https://en.wikipedia.org/wiki/Behavior-driven_development) and [Layered/Hexagonal Architecture](https://alistair.cockburn.us/hexagonal-architecture/). 

The Bitloops Language guides and empowers any software developer to write clean code and build high-quality & well designed software. This is particularly relevant for server application software that has complex, and frequently changing business requirements. With BL, developers can build software using principles such as separation of concerns, loose coupling, high cohesion and command query responsibility segregation (CQRS), which ensure systems are easier to understand, maintain and change. 

With Bitloops Language, developers are able to:
1. **Write clean code** in an intuitive and structured approach
2. Follow **best practices** to ensure the code and software can be easily understood by other developers
3. Create objects with **high cohesion and loose coupling** between each other
4. **Separate the busienss logic** from the **technical aspects** which leads to more **robust and flexible systems**
5. **Focus on the core domain** or problem, and not worry about boilerplate code and implementation details

In essence, software developers can focus on what they do best: **solving problems!** With the Bitloops Language developers write code that will allow other developers (and even themselves after 6 months) to easily understand and build on top of that code.  

<!--
Part of the Bitloops Language project, under the GPL-3.0 license
See /LICENSE for license information.
SPDX-License-Identifier: GPL-3.0-only
The GPL-3.0 license does not cove
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `ddd-hexagonal-cqrs-es-eda.md`
```markdown
# 📦 bitloops/ddd-hexagonal-cqrs-es-eda [🔖 PENDING/APPROVE]
🔗 https://github.com/bitloops/ddd-hexagonal-cqrs-es-eda
🌐 https://bitloops.com

## Meta
- **Stars:** ⭐ 1414 | **Forks:** 🍴 122
- **Language:** TypeScript | **License:** MIT
- **Last updated:** 2026-03-24
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Complete working example of using Domain Driven Design (DDD), Hexagonal Architecture, CQRS, Event Sourcing (ES), Event Driven Architecture (EDA), Behaviour Driven Development (BDD) using TypeScript and NestJS. Like what you see? Don't forget to star! ⭐ ^^^

## README (trích đầu)
```
# ddd-hexagonal-cqrs-es-eda

[![Node.js CI](https://github.com/bitloops/ddd-hexagonal-cqrs-es-eda/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/bitloops/ddd-hexagonal-cqrs-es-eda/actions/workflows/main.yml) ![GitHub](https://img.shields.io/github/license/bitloops/ddd-hexagonal-cqrs-es-eda) ![GitHub issues](https://img.shields.io/github/issues/bitloops/ddd-hexagonal-cqrs-es-eda) [![Dependabot](https://badgen.net/badge/Dependabot/enabled/green?icon=dependabot)](https://dependabot.com/)

Complete working example of using Domain Driven Design (DDD), Hexagonal Architecture, CQRS, Event Sourcing (ES), Event Driven Architecture (EDA), Behaviour Driven Development (BDD) using TypeScript and NestJS.

![ddd-hexagonal-cqrs-es-eda](https://storage.googleapis.com/bitloops-github-assets/ddd-hexagonal-cqrs-es-eda-2.gif)

# Table of Contents

- [I. Introduction](#i-introduction)
  - [Overview](#overview)
  - [Todo application business requirements](#todo-application-business-requirements)
- [II. Technologies and Technical Features](#ii-technologies-and-technical-features)
  - [Technical Features](#technical-features)
  - [Technologies Used - Overview](#technologies-used---overview)
- [III. Quick start - running the ToDo App](#iii-quick-start---running-the-todo-app)
  - [Prerequisites](#prerequisites)
  - [Running the app](#running-the-app)
- [IV. Design Process and Decisions](#iv-design-process-and-decisions)
  - [Design Process - Event Storming](#design-process---event-storming)
  - [Design Decisions](#design-decisions)
- [V. Running in development mode](#v-running-in-development-mode)
  - [A. Project Setup](#a-project-setup)
  - [B. Application Validation](#b-application-validation)
  - [C. Understanding the project structure](#c-understanding-the-project-structure)
- [VI. Conclusion](#vi-conclusion)
  - [❓ Questions](#-questions)

# I. Introduction

Building complex software is really hard, and we learnt the hard way how important it is to design your software correctly from the beginning!

There is plenty of information out there on how to build resilient and maintainable software, but the difficulty is actually implementing it. So we went ahead and built a comprehensive example we wish we had when we started learning these concepts and technologies.

Our team has put a lot of effort into creating a clean, and modular code-base that comes as close as possible to production ready code, aiming to provide valuable insights into advanced software architecture concepts.

## Overview

The objective of this project is to provide you a reference implementation on how to design and create maintainable and flexible software applications.

The code is written using Typescript and NodeJS, using the NEST framework, however, the concepts and patterns used are not bound to any specific technologies.

The project includes an over-engineered ToDo app that includes the patterns and principles that are necessary if you want your code to be easy to chang
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```


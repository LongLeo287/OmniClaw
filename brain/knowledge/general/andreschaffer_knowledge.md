---
id: andreschaffer-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:18:46.652868
---

# KNOWLEDGE EXTRACT: andreschaffer
> **Extracted on:** 2026-03-30 17:29:08
> **Source:** andreschaffer

---

## File: `event-sourcing-cqrs-examples.md`
```markdown
# 📦 andreschaffer/event-sourcing-cqrs-examples [🔖 PENDING/APPROVE]
🔗 https://github.com/andreschaffer/event-sourcing-cqrs-examples


## Meta
- **Stars:** ⭐ 592 | **Forks:** 🍴 122
- **Language:** Java | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Event Sourcing and CQRS in practice.

## README (trích đầu)
```
[![Build](https://github.com/andreschaffer/event-sourcing-cqrs-examples/actions/workflows/build.yml/badge.svg)](https://github.com/andreschaffer/event-sourcing-cqrs-examples/actions/workflows/build.yml)
[![Code Coverage](https://qlty.sh/gh/andreschaffer/projects/event-sourcing-cqrs-examples/coverage.svg)](https://qlty.sh/gh/andreschaffer/projects/event-sourcing-cqrs-examples)
[![Maintainability](https://qlty.sh/gh/andreschaffer/projects/event-sourcing-cqrs-examples/maintainability.svg)](https://qlty.sh/gh/andreschaffer/projects/event-sourcing-cqrs-examples)
[![Dependabot](https://img.shields.io/badge/Dependabot-enabled-blue?logo=dependabot)](https://docs.github.com/en/github/administering-a-repository/keeping-your-dependencies-updated-automatically)

# Event Sourcing and CQRS Examples
This project aims to provide examples of how to use Event Sourcing and CQRS applied to a minimalistic bank context.  

We assume the reader has basic knowledge of Event Sourcing and CQRS concepts.  
If you want to brush up on the subject we suggest reading:  
- [https://martinfowler.com/eaaDev/EventSourcing.html](https://martinfowler.com/eaaDev/EventSourcing.html)
- [https://martinfowler.com/bliki/CQRS.html](https://martinfowler.com/bliki/CQRS.html)

## Domain overview
In this minimalistic bank, a _client_ can _open_ one or more _accounts_.  
On each _account_, the _client_ can _deposit_ or _withdraw_ money.  
The history of an _account's transactions_ is available to the _client_ as well as a summary of the _client's accounts_.

## Design choices
### Architecture overview
      Event Store   Projections
        +----+        +----+
        |    |        |    |
        | DB |        | DB |
        +--+-+        +-+--+
          ^             ^
          |             |
    +------------+------------+
    |     |      |      |     |
    |     |    Events   |     |
    |     +------+----+ |     |
    |     |      |    | |     |
    |     +      |    v +     |
    |   Domain   |   Read     |
    |   Model    |   Model    |
    |            |            |
    +------------+------------+
    |                         |
    |           API           |
    |                         |
    +-------------------------+ 

#### Ports and Adapters
For the Domain Model, we chose the Ports and Adapters structure because we wanted to protect the domain logic from
all the technical concerns.

For more information about it read [here](http://www.dossier-andreas.net/software_architecture/ports_and_adapters.html).

#### Package by Feature
For the Read Models, we chose the Package by Feature structure because we would not benefit from isolating the layers
and instead we put all feature related parts close together. 

For more information about it read [here](http://www.javapractices.com/topic/TopicAction.do?Id=205).

### DDD and REST
There has been a myth of DDD and REST being incompatible due to DDD being all about behaviour
whereas REST is all about state.  
In this project we followed
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```


---
id: ddd-by-examples-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:16.768001
---

# KNOWLEDGE EXTRACT: ddd-by-examples
> **Extracted on:** 2026-03-30 17:35:46
> **Source:** ddd-by-examples

---

## File: `event-source-cqrs-sample.md`
```markdown
# 📦 ddd-by-examples/event-source-cqrs-sample [🔖 PENDING/APPROVE]
🔗 https://github.com/ddd-by-examples/event-source-cqrs-sample


## Meta
- **Stars:** ⭐ 476 | **Forks:** 🍴 130
- **Language:** Java | **License:** Unknown
- **Last updated:** 2026-03-08
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Sample ES/CQRS application

## README (trích đầu)
```
[![Conference recommends](https://devternity.com/shields/recommends.svg)](https://devternity.com)


# Sample event sourced application with Command Query Responsibility Segregation

** Event sourcing **

Shop item can be bought, paid, and marked as payment timeout. Aggregate root (ShopItem) emits 3 different types of domain events: ItemBought, ItemPaid, ItemPaymentMissing. All of them are consequences of commands.

Event store is constructed in database as EventStream table with collection of EventDescriptors. EventStream is fetched by unique aggregate root uuid.

** CQRS **

Read model is constructed by listening to domain events mentioned before. This task is performed by ReadModelOnDomainEventUpdater

```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `library.md`
```markdown
# 📦 ddd-by-examples/library [🔖 PENDING/APPROVE]
🔗 https://github.com/ddd-by-examples/library


## Meta
- **Stars:** ⭐ 5711 | **Forks:** 🍴 815
- **Language:** Java | **License:** MIT
- **Last updated:** 2026-03-24
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
A comprehensive Domain-Driven Design example with problem space strategic analysis and various tactical patterns.

## README (trích đầu)
```
[![CircleCI](https://circleci.com/gh/ddd-by-examples/library.svg?style=svg)](https://circleci.com/gh/ddd-by-examples/library)
[![Code Coverage](https://codecov.io/gh/ddd-by-examples/library/branch/master/graph/badge.svg)](https://codecov.io/gh/ddd-by-examples/library)

# Table of contents

1. [About](#about)
2. [Domain description](#domain-description)
3. [General assumptions](#general-assumptions)  
    3.1 [Process discovery](#process-discovery)  
    3.2 [Project structure and architecture](#project-structure-and-architecture)    
    3.3 [Aggregates](#aggregates)  
    3.4 [Events](#events)  
    3.4.1 [Events in Repositories](#events-in-repositories)   
    3.5 [ArchUnit](#archunit)  
    3.6 [Functional thinking](#functional-thinking)  
    3.7 [No ORM](#no-orm)  
    3.8 [Architecture-code gap](#architecture-code-gap)  
    3.9 [Model-code gap](#model-code-gap)   
    3.10 [Spring](#spring)  
    3.11 [Tests](#tests)  
4. [How to contribute](#how-to-contribute)
5. [References](#references)

## About

This is a project of a library, driven by real [business requirements](#domain-description).
We use techniques strongly connected with Domain Driven Design, Behavior-Driven Development,
Event Storming, User Story Mapping. 

## Domain description

A public library allows patrons to place books on hold at its various library branches.
Available books can be placed on hold only by one patron at any given point in time.
Books are either circulating or restricted, and can have retrieval or usage fees.
A restricted book can only be held by a researcher patron. A regular patron is limited
to five holds at any given moment, while a researcher patron is allowed an unlimited number
of holds. An open-ended book hold is active until the patron checks out the book, at which time it
is completed. A closed-ended book hold that is not completed within a fixed number of 
days after it was requested will expire. This check is done at the beginning of a day by 
taking a look at daily sheet with expiring holds. Only a researcher patron can request
an open-ended hold duration. Any patron with more than two overdue checkouts at a library
branch will get a rejection if trying a hold at that same library branch. A book can be
checked out for up to 60 days. Check for overdue checkouts is done by taking a look at
daily sheet with overdue checkouts. Patron interacts with his/her current holds, checkouts, etc.
by taking a look at patron profile. Patron profile looks like a daily sheet, but the
information there is limited to one patron and is not necessarily daily. Currently a
patron can see current holds (not canceled nor expired) and current checkouts (including overdue).
Also, he/she is able to hold a book and cancel a hold.

How actually a patron knows which books are there to lend? Library has its catalogue of
books where books are added together with their specific instances. A specific book
instance of a book can be added only if there is book with matching ISBN a
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```


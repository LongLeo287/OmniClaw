---
id: asc-lab-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:18:50.608569
---

# KNOWLEDGE EXTRACT: asc-lab
> **Extracted on:** 2026-03-30 17:29:11
> **Source:** asc-lab

---

## File: `better-code-with-ddd.md`
```markdown
# 📦 asc-lab/better-code-with-ddd [🔖 PENDING/APPROVE]
🔗 https://github.com/asc-lab/better-code-with-ddd
🌐 https://www.altkomsoftware.com/blog/better-code-using-domain-driven-design/

## Meta
- **Stars:** ⭐ 320 | **Forks:** 🍴 63
- **Language:** C# | **License:** Unknown
- **Last updated:** 2026-02-20
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
This repository contains code that accompanies presentation ASC LAB team gave at meetup about “Creating better code with Domain Driven Design”.

## README (trích đầu)
```
# Better code with DDD building blocks

[![.NET](https://github.com/asc-lab/better-code-with-ddd/actions/workflows/dotnet.yml/badge.svg)](https://github.com/asc-lab/better-code-with-ddd/actions/workflows/dotnet.yml)

This repository contains code that accompanies presentation ASC LAB team gave at meetup about “Creating better code with Domain Driven Design”.

Check out our article on [Altkom Software & Consulting blog](https://www.altkomsoftware.com/blog/better-code-using-domain-driven-design/).

## Business case

Domain Driven Design tactical patterns are presented here using mortgage loan application processing use case.  Business wants to increase efficiency of mortgage loan application processing for individual customers by: automating application score calculation, combining information from online available sources, auto rejecting applications with RED score, having ability to relatively easy add new rules for scoring.

The process: 
* operator submits loan application with property information, customer data, loan information and attached documents provided by customer
* system performs basic validation, required fields, correct formats
* operator commands the system to calculates score based on rules
* if score is RED application is rejected and explanation is provided
* if score is GREEN then operator validates attached documents and accepts application or rejects it due to discrepancies between provided data and documents. System validates operator’s competence level

The rules:
* property value must not exceed requested loan amount
* customer age at the day of last loan installment must not exceed 65 years
* customer must not be registered debtor in national debtors registry system
* loan monthly installment must not exceed 15% of customer monthly income


## Solutions

Repository contains two solutions. First solution presents typical layered application building approach with anemic model and business logic scattered in services that reside in application layer. This solution also presents usage of generic repository and mixing read and write concerns in the same application service class. First solution is located in the LoanApplication.EnterpriseCake folder.

Second solution presents usage of DDD tactical patterns like: value objects, entities, repositories, factories, domain services and application services to achieve better readability and expressiveness of the code. Applying DDD patterns together with ubiquitous language closes the gap between language spoken by experts and the team and language used in the code.
Solution with DDD building blocks applied is located in the LoanApplication.TacticalDdd folder.


## Domain model
Domain model is pretty simple. There are two aggregates LoanApplication and Operator. LoanApplication represenst, as you can guess, a loan application submitted for processsing.
LoadApplication is composed of several value objects, which in turn are also composed from other value object.
Operator represents
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `java-cqrs-intro.md`
```markdown
# 📦 asc-lab/java-cqrs-intro [🔖 PENDING/APPROVE]
🔗 https://github.com/asc-lab/java-cqrs-intro


## Meta
- **Stars:** ⭐ 213 | **Forks:** 🍴 62
- **Language:** Java | **License:** Unknown
- **Last updated:** 2026-03-12
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Examples of implementation CQRS with Event Sourcing - evolutionary approach

## README (trích đầu)
```
# CQRS and Event Sourcing Intro for Developers

We live in a world of dynamically changing technologies. New ways of architecturing our solutions, new frameworks and libraries seem to appear on almost daily basis. 


**But good software engineering is not about fancy frameworks and solutions aggressively promoted by their vendors.** It is not about doing something because Netflix or Google did it. It is about taking well-thought-out decisions based on facts and knowledge. That’s why it is important to be familiar basic architectural concepts like CQRS. It is one of the tools we use in our software house every day. We mentioned CQRS in the article which is part of the series about [Microservices on .NET Core](https://altkomsoftware.pl/en/blog/building-microservices-on-net-core-1/), but it was presented from technical perspective and here we want to focus on basics concepts explanation with visualisation and examples.


[Check our article!](https://altkomsoftware.pl/en/blog/cqrs-event-sourcing/)

## No CQRS

<p align="center">
    <img alt="No CQRS" src="https://raw.githubusercontent.com/asc-lab/java-cqrs-intro/master/readme-images/1_no_cqrs.png" />
</p>

## Separate Commands and Queries

<p align="center">
    <img alt="Separate Commands and Queries" src="https://raw.githubusercontent.com/asc-lab/java-cqrs-intro/master/readme-images/2_separe_commands_queries.png" />
</p>

## Separate Models Commands and Queries

<p align="center">
    <img alt="Separate Models Commands and Queries" src="https://raw.githubusercontent.com/asc-lab/java-cqrs-intro/master/readme-images/3_separate_models_commands_queries.png" />
</p>

## Separate Storage Engines

<p align="center">
    <img alt="Separate Storage Engines" src="https://raw.githubusercontent.com/asc-lab/java-cqrs-intro/master/readme-images/4_separate_storage_engines.png" />
</p>

## Event Sourcing

<p align="center">
    <img alt="Event Sourcing" src="https://raw.githubusercontent.com/asc-lab/java-cqrs-intro/master/readme-images/5_event_sourcing.png" />
</p>

```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```


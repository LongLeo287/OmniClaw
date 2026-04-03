---
id: oskardudycz-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:29:18.330043
---

# KNOWLEDGE EXTRACT: oskardudycz
> **Extracted on:** 2026-03-30 17:50:35
> **Source:** oskardudycz

---

## File: `EventSourcing.NetCore.md`
```markdown
# 📦 oskardudycz/EventSourcing.NetCore [🔖 PENDING/APPROVE]
🔗 https://github.com/oskardudycz/EventSourcing.NetCore
🌐 https://event-driven.io

## Meta
- **Stars:** ⭐ 3670 | **Forks:** 🍴 543
- **Language:** C# | **License:** CC-BY-SA-4.0
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Examples and Tutorials of Event Sourcing in .NET

## README (trích đầu)
```
[<img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" height="20px" />](https://www.linkedin.com/in/oskardudycz/) ![Github Actions](https://github.com/oskardudycz/EventSourcing.NetCore/actions/workflows/build.dotnet.yml/badge.svg?branch=main) [![Github Sponsors](https://img.shields.io/static/v1?label=Sponsor&message=%E2%9D%A4&logo=GitHub&link=https://github.com/sponsors/oskardudycz/)](https://github.com/sponsors/oskardudycz/) [![blog](https://img.shields.io/badge/blog-event--driven.io-brightgreen)](https://event-driven.io/?utm_source=event_sourcing_net) [![blog](https://img.shields.io/badge/%F0%9F%9A%80-Architecture%20Weekly-important)](https://www.architecture-weekly.com/?utm_source=event_sourcing_net)

# EventSourcing .NET

Tutorial, practical samples and other resources about Event Sourcing in .NET. See also my similar repositories for [JVM](https://github.com/oskardudycz/EventSourcing.JVM) and [NodeJS](https://github.com/oskardudycz/EventSourcing.NodeJS).

- [EventSourcing .NET](#eventsourcing-net)
  - [1. Event Sourcing](#1-event-sourcing)
    - [1.1 What is Event Sourcing?](#11-what-is-event-sourcing)
    - [1.2 What is Event?](#12-what-is-event)
    - [1.3 What is Stream?](#13-what-is-stream)
    - [1.4 Event representation](#14-event-representation)
    - [1.5 Event Storage](#15-event-storage)
    - [1.6 Retrieving the current state from events](#16-retrieving-the-current-state-from-events)
    - [1.7 Strongly-Typed ids with Marten](#17-strongly-typed-ids-with-marten)
  - [2. Videos](#2-videos)
    - [2.1. Practical Event Sourcing with Marten](#21-practical-event-sourcing-with-marten)
    - [2.2. Keep your streams short! Or how to model event-sourced systems efficiently](#22-keep-your-streams-short-or-how-to-model-event-sourced-systems-efficiently)
    - [2.3. Let's build event store in one hour!](#23-lets-build-event-store-in-one-hour)
    - [2.4. CQRS is Simpler than you think with C#11 \& NET7](#24-cqrs-is-simpler-than-you-think-with-c11--net7)
    - [2.5. Practical Introduction to Event Sourcing with EventStoreDB](#25-practical-introduction-to-event-sourcing-with-eventstoredb)
    - [2.6. How to deal with privacy and GDPR in Event-Sourced systems](#26-how-to-deal-with-privacy-and-gdpr-in-event-sourced-systems)
    - [2.7 Let's build the worst Event Sourcing system!](#27-lets-build-the-worst-event-sourcing-system)
    - [2.8 The Light and The Dark Side of the Event-Driven Design](#28-the-light-and-the-dark-side-of-the-event-driven-design)
    - [2.9 Implementing Distributed Processes](#29-implementing-distributed-processes)
    - [2.10 Conversation with Yves Lorphelin about CQRS](#210-conversation-with-yves-lorphelin-about-cqrs)
    - [2.11. Never Lose Data Again - Event Sourcing to the Rescue!](#211-never-lose-data-again---event-sourcing-to-the-rescue)
  - [3. Support](#3-support)
  - [4. Prerequisites](#4-prerequisites)
  - [5. Tools used](#5-tools-used)
  - [6. Samples](#6-samples
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```


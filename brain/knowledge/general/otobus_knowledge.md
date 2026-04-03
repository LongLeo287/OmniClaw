---
id: otobus-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:29:18.376149
---

# KNOWLEDGE EXTRACT: otobus
> **Extracted on:** 2026-03-30 17:50:35
> **Source:** otobus

---

## File: `event_bus.md`
```markdown
# 📦 otobus/event_bus [🔖 PENDING/APPROVE]
🔗 https://github.com/otobus/event_bus
🌐 https://hexdocs.pm/event_bus

## Meta
- **Stars:** ⭐ 703 | **Forks:** 🍴 42
- **Language:** Elixir | **License:** MIT
- **Last updated:** 2026-02-11
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
:surfer: Traceable, extendable and minimalist **event bus** implementation for Elixir with built-in **event store** and **event watcher** based on ETS.

## README (trích đầu)
```
# EventBus

[![Build Status](https://travis-ci.org/otobus/event_bus.svg?branch=master)](https://travis-ci.org/otobus/event_bus)
[![Module Version](https://img.shields.io/hexpm/v/event_bus.svg)](https://hex.pm/packages/event_bus)
[![Hex Docs](https://img.shields.io/badge/hex-docs-lightgreen.svg)](https://hexdocs.pm/event_bus/)
[![Total Download](https://img.shields.io/hexpm/dt/event_bus.svg)](https://hex.pm/packages/event_bus)
[![License](https://img.shields.io/hexpm/l/event_bus.svg)](https://github.com/otobus/event_bus/blob/master/LICENSE)
[![Last Updated](https://img.shields.io/github/last-commit/otobus/event_bus.svg)](https://github.com/otobus/event_bus/commits/master)

Traceable, extendable and minimalist event bus implementation for Elixir with built-in event store and event watcher based on ETS.

![Event Bus](https://cdn-images-1.medium.com/max/1600/1*0fcfAiHvNeHCRYhp-a32YA.png)

## Table of Contents

[Features](#features)

[Getting Started](#getting-started)

[Installation](#installation)

[Usage](#usage)

- [Register event topics in `config.exs`](#register-event-topics-in-configexs)

- [Register/unregister event topics on demand](#registerunregister-event-topics-on-demand)

- [Subscribe to the 'event bus' with a subscriber and list of given topics](#subscribe-to-the-event-bus-with-a-subscriber-and-list-of-given-topics-notification-manager-will-match-with-regex)

- [Unsubscribe from the 'event bus'](#unsubscribe-from-the-event-bus)

- [List subscribers](#list-subscribers)

- [List subscribers of a specific event](#list-subscribers-of-a-specific-event)

- [Event data structure](#event-data-structure)

- [Define an event struct](#event-data-structure)

- [Notify all subscribers with `EventBus.Model.Event` data](#notify-all-subscribers-with-eventbusmodelevent-data)

- [Fetch an event from the store](#fetch-an-event-from-the-store)

- [Mark as completed on Event Observation Manager](#mark-as-completed-on-event-observation-manager)

- [Mark as skipped on Event Observation Manager](#mark-as-skipped-on-event-observation-manager)

- [Check if a topic exists?](#check-if-a-topic-exists)

- [Use block builder to build `EventBus.Model.Event` struct](#use-block-builder-to-build-eventbusmodelevent-struct)

- [Use block notifier to notify event data to given topic](#use-block-notifier-to-notify-event-data-to-given-topic)

[Sample Subscriber Implementation](#sample-subscriber-implementation)

[Event Storage Details](#event-storage-details)

[Traceability](#traceability)

[EventBus.Metrics and UI](#eventbusmetrics-library)

[Documentation](#documentation)

[Addons](#addons)

[Wiki](https://github.com/otobus/event_bus/wiki)

[Contributing](./CONTRIBUTING.md)

[License](./LICENSE.md)

[Code of Conduct](./CODE_OF_CONDUCT.md)

[Questions](./QUESTIONS.md)

## Features

- Fast data writes with enabled concurrent writes to ETS.

- Fast data reads with enabled concurrent reads from ETS.

- Fast by design. Almost all implementation data accesses have O(1) complexity
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```


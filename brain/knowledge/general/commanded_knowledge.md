---
id: commanded-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:09.396951
---

# KNOWLEDGE EXTRACT: commanded
> **Extracted on:** 2026-03-30 17:35:36
> **Source:** commanded

---

## File: `commanded.md`
```markdown
# 📦 commanded/commanded [🔖 PENDING/APPROVE]
🔗 https://github.com/commanded/commanded


## Meta
- **Stars:** ⭐ 1998 | **Forks:** 🍴 257
- **Language:** Elixir | **License:** MIT
- **Last updated:** 2026-03-22
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Use Commanded to build Elixir CQRS/ES applications

## README (trích đầu)
```
# Commanded

Use Commanded to build your own Elixir applications following the [CQRS/ES](http://cqrs.nu/Faq) pattern.

Provides support for:

- Command registration and dispatch.
- Hosting and delegation to aggregates.
- Event handling.
- Long running process managers.

Commanded provides a solid technical foundation for you to build on. It allows you to focus on modelling your domain, the most important part of your app, creating a better application at a faster pace.

You can use Commanded with one of the following event stores for persistence:

- [EventStore](https://github.com/commanded/eventstore) - Elixir library using Postgres for persistence.
- [EventStoreDB](https://www.eventstore.com/) - a stream database built for Event Sourcing.
- [In-memory event store](https://github.com/commanded/commanded/wiki/In-memory-event-store) - included for test use only.

Please refer to the [CHANGELOG](CHANGELOG.md) for features, bug fixes, and any upgrade advice included for each release.

Requires Erlang/OTP v21.0 and Elixir v1.11 or later.

---

#### Sponsors

- [View sponsors & backers](BACKERS.md)

[![Alembic](https://user-images.githubusercontent.com/3167/177830256-26a74e82-60ff-4c20-bd84-64ee7c12512c.svg "Alembic")](https://alembic.com.au/)

---

- [Changelog](CHANGELOG.md)
- [Wiki](https://github.com/commanded/commanded/wiki)
- [What is CQRS/ES?](https://kalele.io/blog-posts/really-simple-cqrs/)
- [Frequently asked questions](https://github.com/commanded/commanded/wiki/FAQ)
- [Getting help](https://github.com/commanded/commanded/wiki/Getting-help)
- [Latest published Hex package](https://hex.pm/packages/commanded) & [documentation](https://hexdocs.pm/commanded/)

MIT License

[![Build Status](https://github.com/commanded/commanded/workflows/Test/badge.svg?branch=master)](https://github.com/commanded/commanded/actions) [![Join the chat at https://gitter.im/commanded/Lobby](https://badges.gitter.im/commanded/Lobby.svg)](https://gitter.im/commanded/Lobby?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

---

> This README and the following guides follow the `master` branch which may not be the currently published version.
>
> [Read the documentation for the latest published version of Commanded on Hex](https://hexdocs.pm/commanded/).

### Overview

- [Getting started](guides/Getting%20Started.md)
- [Choosing an event store](guides/Choosing%20an%20Event%20Store.md)
  - [PostgreSQL-based EventStore](guides/Choosing%20an%20Event%20Store.md#postgresql-based-elixir-eventstore)
  - [Greg Young's Event Store](guides/Choosing%20an%20Event%20Store.md#greg-youngs-event-store)
- [Using Commanded](usage.md)
  - [Aggregates](guides/Aggregates.md)
    - [Example aggregate](guides/Aggregates.md#example-aggregate)
    - [`Commanded.Aggregate.Multi`](guides/Aggregates.md#using-commandedaggregatemulti-to-return-multiple-events)
    - [Aggregate state snapshots](guides/Aggregates.md#aggregate-state-snapshots)
  - [Commands](guides/Comma
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `eventstore.md`
```markdown
# 📦 commanded/eventstore [🔖 PENDING/APPROVE]
🔗 https://github.com/commanded/eventstore


## Meta
- **Stars:** ⭐ 1143 | **Forks:** 🍴 154
- **Language:** Elixir | **License:** MIT
- **Last updated:** 2026-03-19
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Event store using PostgreSQL for persistence

## README (trích đầu)
```
# EventStore

Event store implemented in Elixir. Uses [PostgreSQL](http://www.postgresql.org/) as the underlying storage engine.

Requires Elixir v1.10 and PostgreSQL v9.5 or newer.

EventStore supports [running on a cluster of nodes](../../../vault/archives/archive_legacy/node/doc/api/cluster.md).

- [Changelog](CHANGELOG.md)
- [Wiki](https://github.com/commanded/eventstore/wiki)
- [Frequently asked questions](https://github.com/commanded/eventstore/wiki/FAQ)
- [Getting help](https://github.com/commanded/eventstore/wiki/Getting-help)
- [Latest published Hex package](https://hex.pm/packages/eventstore) & [documentation](https://hexdocs.pm/eventstore/)

MIT License

![Build Status](https://github.com/commanded/eventstore/workflows/Test/badge.svg?branch=master)

---

### Overview

> This README and the following guides follow the `master` branch which may not be the currently published version.
> [Read docs for the latest published version of EventStore on Hex](https://hexdocs.pm/eventstore/).

- [Getting started](guides/Getting%20Started.md)
  - [Using an existing database](guides/Getting%20Started.md#using-an-existing-database)
  - [Reset an existing database](guides/Getting%20Started.md#reset-an-existing-database)
  - [Initialize a database using an Elixir release](guides/Getting%20Started.md#initialize-a-database-using-an-elixir-release)
  - [Using Postgres schemas](guides/Getting%20Started.md#using-postgres-schemas)
  - [Event data and metadata data type](guides/Getting%20Started.md#event-data-and-metadata-data-type)
    - [Using the `jsonb` data type](guides/Getting%20Started.md#using-the-jsonb-data-type)
  - [Using with PgBouncer](guides/Getting%20Started.md#using-with-pg-bouncer)
- [Using the EventStore](usage.md)
  - [Writing to a stream](usage.md#writing-to-a-stream)
    - [Appending events to an existing stream](usage.md#appending-events-to-an-existing-stream)
  - [Reading from a stream](usage.md#reading-from-a-stream)
  - [Reading from all streams](usage.md#reading-from-all-streams)
  - [Stream from all streams](usage.md#stream-from-all-streams)
  - [Linking events between streams](usage.md#linking-events-between-streams)
  - [Deleting streams](usage.md#deleting-streams)
- [Subscriptions](guides/Subscriptions.md)
  - [Transient subscriptions](guides/Subscriptions.md#transient-subscriptions)
  - [Persistent subscriptions](guides/Subscriptions.md#persistent-subscriptions)
    - [Acknowledge received events](guides/Subscriptions.md#acknowledge-received-events)
    - [Subscription concurrency](guides/Subscriptions.md#subscription-concurrency)
    - [Example persistent subscriber](guides/Subscriptions.md#example-persistent-subscriber)
    - [Deleting a persistent subscription](guides/Subscriptions.md#deleting-a-persistent-subscription)
- [Running on a cluster](../../../vault/archives/archive_legacy/node/doc/api/cluster.md)
- [Event serialization](guides/Event%20Serialization.md)
- [Upgrading an EventStore](../../../vault/archives/archive_legacy/node/deps/v8/third_party/abseil-cpp/UPGRADES.md)
- [Used in production?](#used-in-production)
- [B
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```


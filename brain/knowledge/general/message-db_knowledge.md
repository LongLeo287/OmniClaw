---
id: message-db-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:29:07.650612
---

# KNOWLEDGE EXTRACT: message-db
> **Extracted on:** 2026-03-30 17:42:47
> **Source:** message-db

---

## File: `message-db.md`
```markdown
# 📦 message-db/message-db [🔖 PENDING/APPROVE]
🔗 https://github.com/message-db/message-db
🌐 http://docs.eventide-project.org/user-guide/message-db/

## Meta
- **Stars:** ⭐ 1651 | **Forks:** 🍴 63
- **Language:** Shell | **License:** MIT
- **Last updated:** 2026-03-21
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Microservice native message and event store for Postgres

## README (trích đầu)
```
![Message DB](http://docs.eventide-project.org/message-db-logo-90x105.png)

# Message DB

**Microservice Native Event Store and Message Store for Postgres**

A fully-featured event store and message store implemented in PostgreSQL for Pub/Sub, Event Sourcing, Messaging, and Evented Microservices applications.

## Features

- Pub/Sub
- JSON message data
- Event streams
- Stream categories
- Metadata
- Message queues
- Message storage
- Consumer groups
- Service host
- Administration tools
- Reports

## Rationale

An event sourcing and Pub/Sub message store built on Postgres for simple cloud or local hosting. A minimalist implementation of the essential features of tools like [Event Store](https://eventstore.org) or [Kafka](https://kafka.apache.org), with built-in support for messaging patterns like Pub/Sub, and consumer patterns like consumer groups.

Message DB was extracted from the [Eventide Project](http://docs.eventide-project.org) to make it easier for users to write clients in the language of their choosing.

## User Guide

A complete user guide is available on the Eventide Project docs site:

[http://docs.eventide-project.org/user-guide/message-db/](http://docs.eventide-project.org/user-guide/message-db/)

## Installation

Message DB can be installed either as a Ruby Gem, an NPM package, or can simply be cloned from this repository.

### Git Clone

``` bash
git clone git@github.com:message-db/message-db.git
```

### As a Ruby Gem

``` bash
gem install message-db
```

### As an NPM Module

``` bash
npm install @eventide/message-db
```

## Create the Postgres Database

Running the database installation script creates the database, schema, table, indexes, functions, views, types, a user role, and limit the user's privileges to the message store's public interface.

### Requirements

Make sure that your default Postgres user has administrative privileges.

### From the Git Clone

The installation script is in the `database` directory of the cloned repo. Change directory to the `message-db` directory where you cloned the repo, and run the script:

``` bash
database/install.sh
```

### From the Ruby Executable

If you installed Message DB via RubyGems, a database installation Ruby executable will be installed with the `message-db` gem.

The executable will be in the gem executable search path and may also be executed through bundler:

``` bash
bundle exec mdb-create-db
```

For more information about Ruby executables installed with the `message-db` Ruby Gem, see the Eventide docs on the administration tools that are bundled with the gem:

[http://docs.eventide-project.org/user-guide/message-db/tools.html](http://docs.eventide-project.org/user-guide/message-db/tools.html)

### From the NPM Module

The `message-db` NPM module doesn't ship with any special tooling other than the bundled scripts.

To execute the installation script, navigate to the directory where the `message-db` module is installed and run the script:

``` bash
install.sh
```

###
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```


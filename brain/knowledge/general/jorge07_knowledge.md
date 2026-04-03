---
id: jorge07-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:56.267830
---

# KNOWLEDGE EXTRACT: jorge07
> **Extracted on:** 2026-03-30 17:38:13
> **Source:** jorge07

---

## File: `ddd-playground.md`
```markdown
# 📦 jorge07/ddd-playground [🔖 PENDING/APPROVE]
🔗 https://github.com/jorge07/ddd-playground


## Meta
- **Stars:** ⭐ 597 | **Forks:** 🍴 86
- **Language:** PHP | **License:** Unknown
- **Last updated:** 2026-01-18
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Domain-Driven Design in a PHP project using Symfony

## README (trích đầu)
```
DDD Playground
==============

> For a more acurated DDD, CQRS and Event Sourcing implementation [see here](https://github.com/jorge07/symfony-4-es-cqrs-boilerplate)

**Wallet API** in Symfony following DDD (Domain Driver Design). 

### Examples in the repo

   - [x] **User authentication** based in JWT 
   - [x] **UUID as binary** to improve the performance and create a nightmare for the dba.
   - [x] Automated tasks with ant.
   - [x] **Dev and CI environments in Docker**. Boosting build speed with docker **cache layers** in pipeline. Orchestrating with **Docker Compose**.
   - [x] An example of **table inheritance and discriminator strategy** 
   - [x] How to deal with **EAV** (Entity-Attribute-Value) with **Json data type**.
   - [x] Code structured in layers as appears in DDD in php book.
   - [x] Test for api in **behat** accessing via web server (*Acceptance tests*). 
   - [x] Integration test with **Lakion api test case** and **Alice** for fixtures and how to integrate it with **behat**. 
   - [x] **Command Bus** implementation
   - [x] DomainEvents
   - [x] Events to RabbitMQ
   - [x] Events stored in ElasticSearch and Kibana for reading in `:5601`
   


### The folder structure 

    src
      \
       |\ Application     `Contains the Use Cases of the domain system and the Data Transfer Objects`
       |
       |\ Domain          `The system business logic layer`
       |
       |\ Infrastructure  `Its the implementation of the system outside the model. I.E: Persistence, serialization, etc`
       |
        \ UI              `User Interface. This use to be inside the Infrastructure layer, but I don't like it.`

### The tests

The tests follow the same structure and the *phpunit* tests are tagged with group tags: *unit* or *functional*.

The *aceptation tests* are inside the test `UI` layer and attack the application from outside using Guzzle.

### The Environment setup

The environment is in PHP7.1 and the development containers are on `etc/infrastructure/dev/docker-compose.yml`

Up environment with: `docker-compose -f etc/infrastructure/dev/docker-compose.yml up -d`

Install dependencies: `docker-compose -f etc/infrastructure/dev/docker-compose.yml exec fpm sh -lc 'composer install'`

Setup database, etc with : `docker-compose -f etc/infrastructure/dev/docker-compose.yml exec fpm sh -lc 'ant build'`

Start **async** listeners: `docker-compose -f etc/infrastructure/dev/docker-compose.yml exec fpm sh -lc 'bin/console rabbitmq:multiple-consumer events'`

- Rabbit Management: `:15672`
![Rabbit](https://i.imgur.com/Wx881tI.png)

- Kibana: `:5601`
![Kibana](https://i.imgur.com/AKsVA0t.png)

### CI/CD

Follow the `Jenkinsfile` or the `gitlab-ci.yml` file, it's clear enough and contains a simply workflow to:

- build the isolated environment
- `docker-compose -p` to avoid parallel jobs conflicts
- provision the environment
- run the test
- extract reports
- Build and store the artifacts (Docker images)
- Clean the environment

```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `symfony-7-es-cqrs-boilerplate.md`
```markdown
# 📦 jorge07/symfony-7-es-cqrs-boilerplate [🔖 PENDING/APPROVE]
🔗 https://github.com/jorge07/symfony-7-es-cqrs-boilerplate


## Meta
- **Stars:** ⭐ 1088 | **Forks:** 🍴 185
- **Language:** PHP | **License:** MIT
- **Last updated:** 2026-02-25
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Symfony 7 DDD ES CQRS backend boilerplate.

## README (trích đầu)
```
# Symfony 7 ES CQRS Boilerplate
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-5-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->

A boilerplate demonstrating **Domain-Driven Design (DDD)**, **Command Query Responsibility Segregation (CQRS)**, and **Event Sourcing** patterns using Symfony 7 and PHP 8.3.

[![push](https://github.com/jorge07/symfony-6-es-cqrs-boilerplate/actions/workflows/push.yml/badge.svg)](https://github.com/jorge07/symfony-6-es-cqrs-boilerplate/actions/workflows/push.yml)

> This is a long living repository that started at v4 and was upgraded to each major version since then. You can find older versions at the following branches:
>
> [symfony-6 branch](https://github.com/jorge07/symfony-6-es-cqrs-boilerplate/tree/symfony-6)
>
> [symfony-5 branch](https://github.com/jorge07/symfony-6-es-cqrs-boilerplate/tree/symfony-5)
>
> [symfony-4 branch](https://github.com/jorge07/symfony-6-es-cqrs-boilerplate/tree/symfony-4)

## Documentation

- [Command and Query Buses](doc/GetStarted/Buses.md)
- [Creating Use Cases](doc/GetStarted/UseCases.md)
- [Adding Projections](doc/GetStarted/Projections.md)
- [Async Processing](../../../vault/archives/archive_legacy/ruff/crates/ty_python_semantic/resources/mdtest/async.md)
- [UI Workflow](../bmad_repo/workflow.md)
- [Xdebug Configuration](doc/GetStarted/Xdebug.md)
- [Kubernetes Deployment](DEPLOYMENT.md)

## Architecture

![Architecture](https://i.imgur.com/SzHgMft.png)

## Implementations

- [x] Environment in Docker
- [x] Symfony Messenger
- [x] Event Store
- [x] Read Model
- [x] Async Event subscribers
- [x] Rest API
- [x] Web UI (A Terrible UX/UI)
- [x] Event Store Rest API 
- [x] Swagger API Doc

## Use Cases

#### User
- [x] Sign up
- [x] Change Email
- [x] Sign in
- [x] Logout

![API Doc](https://i.imgur.com/DBZsPlE.png)

## Stack

- PHP 8.3
- Symfony 7
- MySQL 8.0
- Elasticsearch & Kibana 7.11.0
- RabbitMQ 3

## Project Setup


|    Action           |     Command      |
|---------------------|------------------|
|  Setup              | `make start`     |
|  Run Tests          | `make phpunit`   |
|  Static Analysis    | `make phpstan`   |
|  Code Style         | `make cs`        |
|  PHP Shell          | `make s=php sh`  |
|  Xdebug             | `make xoff/xon`  |
|  Build Artifacts    | `make artifact`  |

## PHPStorm integration

PHPSTORM has native integration with Docker compose. That's nice but will stop your php container after run the test scenario. That's not nice when using fpm. A solution could be use another container just for that purpose but is way slower and I don't want. For that reason I use ssh connection.

### IMPORTANT

> **ssh in the container it's ONLY for that reason and ONLY in the DEV TAG, if you've ssh installed in your production container, you're doing it wrong...***

[Click here for the detailed instructions about how to setup the PHP remote interpreter in PHPStorm.](https://github.com/jorge07/alpine-php/blob/
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```


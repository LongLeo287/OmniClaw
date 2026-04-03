---
id: ferrius-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:24.096651
---

# KNOWLEDGE EXTRACT: ferrius
> **Extracted on:** 2026-03-30 17:37:00
> **Source:** ferrius

---

## File: `ddd-cqrs-example.md`
```markdown
# 📦 ferrius/ddd-cqrs-example [🔖 PENDING/APPROVE]
🔗 https://github.com/ferrius/ddd-cqrs-example


## Meta
- **Stars:** ⭐ 365 | **Forks:** 🍴 54
- **Language:** PHP | **License:** GPL-3.0
- **Last updated:** 2026-03-17
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
DDD CQRS ADR PHP Symfony example

## README (trích đầu)
```
### About
This is an example of implementation and my vision of **practical** CQRS, DDD, ADR, hexagonal architecture and directory structure.
Project has entities `Task` and `User`.
All UI is the REST endpoints.

### What is done
* Hexagonal Architecture (`Ports` directory for external endpoints)
* CQRS (based on symfony messenger component command/query buses with middlewares)
* DDD: directory structure (used sensiolabs-de/deptrac to control layers dependencies)
* DDD: core bounded context
* DDD: domain events implementation
* DDD: example of specification in User entity that requires a db query

### To do
* Add another bounded context
* Add anti-corruption layer for interaction between contexts

### My assumptions
* I placed entities public getters and private setters into the traits with *GS suffix to make entities a little bit clear (phpstorm tracks fine all references to entity classes) anyway you can put getters with setters in the same class
* Unfortunately mysql has a poor performance with primary uuids. Of course prefer application generated uuid if database supports them.

### How to install the project
* `bash setup_env.sh dev` - to setup .env.local docker/.env
* `make dc_up` - docker-compose up 
* `make setup_dev` - composer install, migrations and so on
* `make run php bin/console app:create-user` - create a user
* `http://127.0.0.1:888/api/doc` `https://127.0.0.1:444/api/doc` - api doc

### Some words about docker
In project is used workplace container for code manipulations, CI or building. It was created for preventing of pollution
of working containers (php-fpm) of unused in request, building tools like nodejs, composer, dev libs and so on.
Also was created a local user based on host machine user PUID PGID to resolve conflicts with file permissions.

`make dev` - jump into workplace container

### CI
```
make dev
//in container execute
make analyze
```

### Implementation
Used symfony messenger component to create transactional command bus, query bus and event bus.
Query model represented by DTOs. Domain and Command layers are covered by unit tests. 

```
├── Core (Core bounded context)
│   ├── Application
│   │   ├── Command
│   │   │   ├── AuthToken
│   │   │   ├── Task
│   │   │   └── User
│   │   ├── Query
│   │       └── Task
│   ├── Domain
│   │   └── Model
│   │       ├── Task
│   │       └── User
│   ├── Infrastructure
│   │   └── Repository
│   └── Ports
│       ├── Cli
│       └── Rest
└── Shared
    ├── Domain
    └── Infrastructure

```



```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```


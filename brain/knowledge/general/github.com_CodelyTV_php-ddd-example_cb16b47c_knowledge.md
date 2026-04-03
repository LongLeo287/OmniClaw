---
id: github.com-codelytv-php-ddd-example-cb16b47c-knowl
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:40.905890
---

# KNOWLEDGE EXTRACT: github.com_CodelyTV_php-ddd-example_cb16b47c
> **Extracted on:** 2026-04-01 08:41:28
> **Source:** D:/LongLeo/AI OS CORP/AI OS/core/security/QUARANTINE/KI-BATCH-20260331205007519718/github.com_CodelyTV_php-ddd-example_cb16b47c

---

## File: `.env`
```
### Symfony - framework-bundle
APP_ENV=test
APP_SECRET=29ac4a5187930cd4b689aa0f3ee7cbc0
#TRUSTED_PROXIES=127.0.0.1,127.0.0.2
#TRUSTED_HOSTS='^localhost|example\.com$'

#              MOOC              #
#--------------------------------#
# MySql
MOOC_DATABASE_DRIVER=pdo_mysql
MOOC_DATABASE_HOST=codely-php_ddd_skeleton-mooc-mysql
MOOC_DATABASE_PORT=3306
MOOC_DATABASE_NAME=mooc
MOOC_DATABASE_USER=root
MOOC_DATABASE_PASSWORD=

#           BACKOFFICE           #
#--------------------------------#
# MySql
BACKOFFICE_DATABASE_DRIVER=pdo_mysql
BACKOFFICE_DATABASE_HOST=codely-php_ddd_skeleton-mooc-mysql
BACKOFFICE_DATABASE_PORT=3306
BACKOFFICE_DATABASE_NAME=mooc
BACKOFFICE_DATABASE_USER=root
BACKOFFICE_DATABASE_PASSWORD=

# Elasticsearch
BACKOFFICE_ELASTICSEARCH_HOST=codely-php_ddd_skeleton-backoffice-elastic
BACKOFFICE_ELASTICSEARCH_INDEX_PREFIX=backoffice

#             COMMON             #
#--------------------------------#
# RabbitMQ
RABBITMQ_HOST=codely-php_ddd_skeleton-rabbitmq
RABBITMQ_PORT=5672
RABBITMQ_LOGIN=codely
RABBITMQ_PASSWORD=c0d3ly
RABBITMQ_EXCHANGE=domain_events
RABBITMQ_MAX_RETRIES=5
# RabbitMQ - Application Specific
RABBITMQ_MOOC_VHOST=/
```

## File: `.gitignore`
```
/.env.local
/.env.*.local

/apps/*/*/var/
!/apps/*/*/var/.gitkeep

/apps/*/*/build/
!/apps/*/*/build/supervisor/.gitkeep

/vendor/
.phpunit.result.cache

/build

.php-cs-fixer.cache
```

## File: `Dockerfile`
```
FROM php:8.3-fpm-alpine
WORKDIR /app

RUN apk --update upgrade \
    && apk add --no-cache autoconf automake make gcc g++ git bash icu-dev libzip-dev rabbitmq-c rabbitmq-c-dev linux-headers

RUN pecl install apcu-5.1.23 && pecl install amqp-2.1.1 && pecl install xdebug-3.3.0

RUN docker-php-ext-install -j$(nproc) \
        bcmath \
        opcache \
        intl \
        zip \
        pdo_mysql

RUN docker-php-ext-enable amqp apcu opcache

RUN curl -sS https://get.symfony.com/cli/installer | bash -s - --install-dir /usr/local/bin

COPY etc/infrastructure/php/ /usr/local/etc/php/

# allow non-root users have home
RUN mkdir -p /opt/home
RUN chmod 777 /opt/home
ENV HOME /opt/home
```

## File: `Makefile`
```
current-dir := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))

composer-install:
	@docker run --rm $(INTERACTIVE) --volume $(current-dir):/app --user $(id -u):$(id -g) \
		composer:2.6.4 install \
			--ignore-platform-reqs \
			--no-ansi

test:
	docker exec codely-php_ddd_skeleton-mooc_backend-php ./vendor/bin/phpunit --testsuite mooc
	docker exec codely-php_ddd_skeleton-mooc_backend-php ./vendor/bin/phpunit --testsuite shared
	docker exec codely-php_ddd_skeleton-mooc_backend-php ./vendor/bin/behat -p mooc_backend --format=progress -v
	docker exec codely-php_ddd_skeleton-backoffice_backend-php ./vendor/bin/phpunit --testsuite backoffice

static-analysis:
	docker exec codely-php_ddd_skeleton-mooc_backend-php ./vendor/bin/psalm --output-format=github --shepherd

lint:
	docker exec codely-php_ddd_skeleton-mooc_backend-php ./vendor/bin/ecs check

test-architecture:
	docker exec codely-php_ddd_skeleton-mooc_backend-php php -d memory_limit=4G ./vendor/bin/phpstan analyse --error-format=github

mess-detector:
	docker exec codely-php_ddd_skeleton-mooc_backend-php ./vendor/bin/phpmd apps,src,tests github phpmd.xml

start:
	@if [ ! -f .env.local ]; then echo '' > .env.local; fi
	UID=${shell id -u} GID=${shell id -g} docker compose up --build -d
	make clean-cache

stop:
	UID=${shell id -u} GID=${shell id -g} docker compose stop

destroy:
	UID=${shell id -u} GID=${shell id -g} docker compose down

rebuild:
	docker compose build --pull --force-rm --no-cache
	make install
	make start

ping-mysql:
	@docker exec codely-php_ddd_skeleton-mooc-mysql mysqladmin --user=root --password= --host "127.0.0.1" ping --silent

ping-elasticsearch:
	@curl -I -XHEAD localhost:9200

ping-rabbitmq:
	@docker exec codely-php_ddd_skeleton-rabbitmq rabbitmqctl ping --silent

clean-cache:
	@rm -rf apps/*/*/var
	@docker exec codely-php_ddd_skeleton-mooc_backend-php ./apps/mooc/backend/bin/console cache:warmup
```

## File: `README.md`
```markdown
<p align="center">
  <a href="https://codely.com">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://codely.com/logo/codely_logo-dark.svg">
      <source media="(prefers-color-scheme: light)" srcset="https://codely.com/logo/codely_logo-light.svg">
      <img alt="Codely logo" src="https://codely.com/logo/codely_logo.svg">
    </picture>
  </a>
</p>

<h1 align="center">
  🐘🎯 Hexagonal Architecture, DDD & CQRS in PHP
</h1>

<p align="center">
    <a href="https://github.com/CodelyTV"><img src="https://img.shields.io/badge/Codely-OS-green.svg?style=flat-square" alt="Codely Open Source projects"/></a>
    <a href="http://pro.codely.tv"><img src="https://img.shields.io/badge/CodelyTV-PRO-black.svg?style=flat-square" alt="CodelyTV Courses"/></a>
    <a href="#"><img src="https://img.shields.io/badge/Symfony-7-purple.svg?style=flat-square&logo=symfony" alt="Symfony 7"/></a>
    <a href="https://shepherd.dev/github/CodelyTV/php-ddd-example"><img src="https://shepherd.dev/github/CodelyTV/php-ddd-example/coverage.svg" alt="Type Coverage"/></a>
    <a href="https://github.com/CodelyTV/php-ddd-example/actions"><img src="https://github.com/CodelyTV/php-ddd-example/workflows/CI/badge.svg?branch=master" alt="CI pipeline status" /></a>
</p>

<p align="center">
  Example of a <strong>PHP application using Domain-Driven Design (DDD) and Command Query Responsibility Segregation
  (CQRS) principles</strong> keeping the code as simple as possible.
  <br />
  <br />
  Take a look, play and have fun with this.
  <a href="https://github.com/CodelyTV/php-ddd-example/stargazers">Stars are welcome 😊</a>
  <br />
  <br />
  <a href="https://www.youtube.com/watch?v=1kaP39W80zQ">View Demo</a>
  ·
  <a href="https://github.com/CodelyTV/php-ddd-example/issues">Report a bug</a>
  ·
  <a href="https://github.com/CodelyTV/php-ddd-example/issues">Request a feature</a>
</p>

## 🚀 Environment Setup

### 🐳 Needed tools

1. [Install Docker](https://www.docker.com/get-started)
2. Clone this project: `git clone https://github.com/CodelyTV/php-ddd-example php-ddd-example`
3. Move to the project folder: `cd php-ddd-example`

### 🛠️ Environment configuration

1. Create a local environment file (`cp .env .env.local`) if you want to modify any parameter

### 🔥 Application execution

1. Install all the dependencies and bring up the project with Docker executing: `make build`
2. Then you'll have 3 apps available (2 APIs and 1 Frontend):
   1. [Mooc Backend](apps/mooc/backend): http://localhost:8030/health-check
   2. [Backoffice Backend](apps/backoffice/backend): http://localhost:8040/health-check
   3. [Backoffice Frontend](apps/backoffice/frontend): http://localhost:8041/health-check

### ✅ Tests execution

1. Install the dependencies if you haven't done it previously: `make deps`
2. Execute PHPUnit and Behat tests: `make test`

## 👩‍💻 Project explanation

This project tries to be a MOOC (Massive Open Online Course) platform. It's decoupled from any framework, but it has
some Symfony and Laravel implementations.

### ⛱️ Bounded Contexts

- [Mooc](src/Mooc): Place to look in if you wanna see some code 🙂. Massive Open Online Courses public platform with users, videos, notifications, and so on.
- [Backoffice](src/Backoffice): Here you'll find the use cases needed by the Customer Support department in order to manage users, courses, videos, and so on.

### 🎯 Hexagonal Architecture

This repository follows the Hexagonal Architecture pattern. Also, it's structured using `modules`.
With this, we can see that the current structure of a Bounded Context is:

```scala
$ tree -L 4 src

src
|-- Mooc // Company subdomain / Bounded Context: Features related to one of the company business lines / products
|   `-- Videos // Some Module inside the Mooc context
|       |-- Application
|       |   |-- Create // Inside the application layer all is structured by actions
|       |   |   |-- CreateVideoCommand.php
|       |   |   |-- CreateVideoCommandHandler.php
|       |   |   `-- VideoCreator.php
|       |   |-- Find
|       |   |-- Trim
|       |   `-- Update
|       |-- Domain
|       |   |-- Video.php // The Aggregate of the Module
|       |   |-- VideoCreatedDomainEvent.php // A Domain Event
|       |   |-- VideoFinder.php
|       |   |-- VideoId.php
|       |   |-- VideoNotFound.php
|       |   |-- VideoRepository.php // The `Interface` of the repository is inside Domain
|       |   |-- VideoTitle.php
|       |   |-- VideoType.php
|       |   |-- VideoUrl.php
|       |   `-- Videos.php // A collection of our Aggregate
|       `-- Infrastructure // The infrastructure of our module
|           |-- DependencyInjection
|           `-- Persistence
|               `--MySqlVideoRepository.php // An implementation of the repository
`-- Shared // Shared Kernel: Common infrastructure and domain shared between the different Bounded Contexts
    |-- Domain
    `-- Infrastructure
```

#### Repository pattern

Our repositories try to be as simple as possible usually only containing 2 methods `search` and `save`.
If we need some query with more filters we use the `Specification` pattern also known as `Criteria` pattern. So we add a
`searchByCriteria` method.

You can see an example [here](src/Mooc/Courses/Domain/CourseRepository.php)
and its implementation [here](src/Mooc/Courses/Infrastructure/Persistence/DoctrineCourseRepository.php).

### Aggregates

You can see an example of an aggregate [here](src/Mooc/Courses/Domain/Course.php). All aggregates should
extend the [AggregateRoot](src/Shared/Domain/Aggregate/AggregateRoot.php).

### Command Bus

There is 1 implementations of the [command bus](src/Shared/Domain/Bus/Command/CommandBus.php).
1. [Sync](src/Shared/Infrastructure/Bus/Command/InMemorySymfonyCommandBus.php) using the Symfony Message Bus.


### Query Bus

The [Query Bus](src/Shared/Infrastructure/Bus/Query/InMemorySymfonyQueryBus.php) uses the Symfony Message Bus.

### Event Bus

The [Event Bus](src/Shared/Infrastructure/Bus/Event/InMemory/InMemorySymfonyEventBus.php) uses the Symfony Message Bus.
The [MySql Bus](src/Shared/Infrastructure/Bus/Event/MySql/MySqlDoctrineEventBus.php) uses a MySql+Pulling as a bus.
The [RabbitMQ Bus](src/Shared/Infrastructure/Bus/Event/RabbitMq/RabbitMqEventBus.php) uses RabbitMQ C extension.

## 📱 Monitoring

Every time a domain event is published it's exported to Prometheus. You can access to the Prometheus panel [here](http://localhost:9999/).

## 🤔 Contributing

There are some things missing (add swagger, improve documentation...), feel free to add this if you want! If you want
some guidelines feel free to contact us :)

## 🤩 Extra

This code was shown in the [From framework coupled code to #microservices through #DDD](http://codely.tv/blog/screencasts/codigo-acoplado-framework-microservicios-ddd) talk and doubts where answered in the [DDD y CQRS: Preguntas Frecuentes](https://codely.com/blog/ddd-cqrs-preguntas-frecuentes) video.


🎥 Used in the CodelyTV Pro courses:

- [🇪🇸 DDD in PHP](https://pro.codely.tv/library/ddd-en-php/about/)
- [🇪🇸 Arquitectura Hexagonal](https://pro.codely.tv/library/arquitectura-hexagonal/66748/about/)
- [🇪🇸 CQRS: Command Query Responsibility Segregation](https://pro.codely.tv/library/cqrs-command-query-responsibility-segregation-3719e4aa/62554/about/)
- [🇪🇸 Comunicación entre microservicios: Event-Driven Architecture](https://pro.codely.tv/library/comunicacion-entre-microservicios-event-driven-architecture/74823/about/)

## 🌐 remember to visit our courses

- [Courses codely](https://codely.com/cursos)
```

## File: `behat.yml`
```yaml
imports:
  - apps/mooc/backend/tests/mooc_backend.yml
```

## File: `composer.json`
```json
{
  "name": "codelytv/php-ddd-example",
  "license": "MIT",
  "type": "project",
  "description": "An example project applying Domain-Driven Design, Hexagonal Architecture and CQRS in a Monorepository",
  "require": {
    "php": "^8.3",

    "ext-amqp": "*",
    "ext-apcu": "*",
    "ext-json": "*",
    "ext-zend-opcache": "*",
    "ext-pdo": "*",

    "symfony/framework-bundle": "^7",
    "symfony/messenger": "^7",
    "symfony/dotenv": "^7",
    "symfony/yaml": "^7",
    "symfony/twig-bundle": "^7",
    "symfony/validator": "^7",
    "symfony/cache": "^7",

    "lambdish/phunctional": "^2",

    "ramsey/uuid": "^4",

    "doctrine/dbal": "^3",
    "doctrine/orm": "^2",

    "ocramius/proxy-manager": "^2",
    "laminas/laminas-zendframework-bridge": "^1",

    "elasticsearch/elasticsearch": "^7",
    "monolog/monolog": "^3",

    "promphp/prometheus_client_php": "^2.7.2"
  },
  "require-dev": {
    "ext-xdebug": "*",

    "roave/security-advisories": "dev-master",

    "behat/behat": "^3.13",
    "friends-of-behat/mink-extension": "2.7.5",
    "friends-of-behat/symfony-extension": "2.6.0",
    "behat/mink-browserkit-driver": "2.2.0",

    "phpunit/phpunit": "^9",
    "mockery/mockery": "^1",

    "fakerphp/faker": "^1",

    "symfony/error-handler": "^7",

    "symplify/easy-coding-standard": "^12.0",
    "vimeo/psalm": "^5.15",
    "rector/rector": "^0.18.12",
    "psalm/plugin-mockery": "^1.1",
    "psalm/plugin-symfony": "^5.0",
    "psalm/plugin-phpunit": "^0.18.4",
    "phpstan/phpstan": "^1.10",
    "phpat/phpat": "^0.10.10",
    "phpmd/phpmd": "^2.14",
    "codelytv/coding-style": "^1.1"
  },
  "autoload": {
    "psr-4": {
      "CodelyTv\\Apps\\Mooc\\Backend\\": "apps/mooc/backend/src",
      "CodelyTv\\Apps\\Mooc\\Frontend\\": "apps/mooc/frontend/src",

      "CodelyTv\\Apps\\Backoffice\\Backend\\": "apps/backoffice/backend/src",
      "CodelyTv\\Apps\\Backoffice\\Frontend\\": "apps/backoffice/frontend/src",

      "CodelyTv\\": ["src"]
    }
  },
  "autoload-dev": {
    "psr-4": {
      "CodelyTv\\Tests\\": ["tests"]
    }
  },
  "minimum-stability": "RC",
  "config": {
    "allow-plugins": {
      "ocramius/package-versions": true
    }
  }
}
```

## File: `composer.lock`
```
{
    "_readme": [
        "This file locks the dependencies of your project to a known state",
        "Read more about it at https://getcomposer.org/doc/01-basic-usage.md#installing-dependencies",
        "This file is @generated automatically"
    ],
    "content-hash": "1384ca0a67984f7a0296f15a4373fed1",
    "packages": [
        {
            "name": "brick/math",
            "version": "0.12.1",
            "source": {
                "type": "git",
                "url": "https://github.com/brick/math.git",
                "reference": "f510c0a40911935b77b86859eb5223d58d660df1"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/brick/math/zipball/f510c0a40911935b77b86859eb5223d58d660df1",
                "reference": "f510c0a40911935b77b86859eb5223d58d660df1",
                "shasum": ""
            },
            "require": {
                "php": "^8.1"
            },
            "require-dev": {
                "php-coveralls/php-coveralls": "^2.2",
                "phpunit/phpunit": "^10.1",
                "vimeo/psalm": "5.16.0"
            },
            "type": "library",
            "autoload": {
                "psr-4": {
                    "Brick\\Math\\": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "description": "Arbitrary-precision arithmetic library",
            "keywords": [
                "Arbitrary-precision",
                "BigInteger",
                "BigRational",
                "arithmetic",
                "bigdecimal",
                "bignum",
                "bignumber",
                "brick",
                "decimal",
                "integer",
                "math",
                "mathematics",
                "rational"
            ],
            "support": {
                "issues": "https://github.com/brick/math/issues",
                "source": "https://github.com/brick/math/tree/0.12.1"
            },
            "funding": [
                {
                    "url": "https://github.com/BenMorel",
                    "type": "github"
                }
            ],
            "time": "2023-11-29T23:19:16+00:00"
        },
        {
            "name": "doctrine/cache",
            "version": "2.2.0",
            "source": {
                "type": "git",
                "url": "https://github.com/doctrine/cache.git",
                "reference": "1ca8f21980e770095a31456042471a57bc4c68fb"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/doctrine/cache/zipball/1ca8f21980e770095a31456042471a57bc4c68fb",
                "reference": "1ca8f21980e770095a31456042471a57bc4c68fb",
                "shasum": ""
            },
            "require": {
                "php": "~7.1 || ^8.0"
            },
            "conflict": {
                "doctrine/common": ">2.2,<2.4"
            },
            "require-dev": {
                "cache/integration-tests": "dev-master",
                "doctrine/coding-standard": "^9",
                "phpunit/phpunit": "^7.5 || ^8.5 || ^9.5",
                "psr/cache": "^1.0 || ^2.0 || ^3.0",
                "symfony/cache": "^4.4 || ^5.4 || ^6",
                "symfony/var-exporter": "^4.4 || ^5.4 || ^6"
            },
            "type": "library",
            "autoload": {
                "psr-4": {
                    "Doctrine\\Common\\Cache\\": "lib/Doctrine/Common/Cache"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Guilherme Blanco",
                    "email": "guilhermeblanco@gmail.com"
                },
                {
                    "name": "Roman Borschel",
                    "email": "roman@code-factory.org"
                },
                {
                    "name": "Benjamin Eberlei",
                    "email": "kontakt@beberlei.de"
                },
                {
                    "name": "Jonathan Wage",
                    "email": "jonwage@gmail.com"
                },
                {
                    "name": "Johannes Schmitt",
                    "email": "schmittjoh@gmail.com"
                }
            ],
            "description": "PHP Doctrine Cache library is a popular cache implementation that supports many different drivers such as redis, memcache, apc, mongodb and others.",
            "homepage": "https://www.doctrine-project.org/projects/cache.html",
            "keywords": [
                "abstraction",
                "apcu",
                "cache",
                "caching",
                "couchdb",
                "memcached",
                "php",
                "redis",
                "xcache"
            ],
            "support": {
                "issues": "https://github.com/doctrine/cache/issues",
                "source": "https://github.com/doctrine/cache/tree/2.2.0"
            },
            "funding": [
                {
                    "url": "https://www.doctrine-project.org/sponsorship.html",
                    "type": "custom"
                },
                {
                    "url": "https://www.patreon.com/phpdoctrine",
                    "type": "patreon"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/doctrine%2Fcache",
                    "type": "tidelift"
                }
            ],
            "time": "2022-05-20T20:07:39+00:00"
        },
        {
            "name": "doctrine/collections",
            "version": "2.2.2",
            "source": {
                "type": "git",
                "url": "https://github.com/doctrine/collections.git",
                "reference": "d8af7f248c74f195f7347424600fd9e17b57af59"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/doctrine/collections/zipball/d8af7f248c74f195f7347424600fd9e17b57af59",
                "reference": "d8af7f248c74f195f7347424600fd9e17b57af59",
                "shasum": ""
            },
            "require": {
                "doctrine/deprecations": "^1",
                "php": "^8.1"
            },
            "require-dev": {
                "doctrine/coding-standard": "^12",
                "ext-json": "*",
                "phpstan/phpstan": "^1.8",
                "phpstan/phpstan-phpunit": "^1.0",
                "phpunit/phpunit": "^10.5",
                "vimeo/psalm": "^5.11"
            },
            "type": "library",
            "autoload": {
                "psr-4": {
                    "Doctrine\\Common\\Collections\\": "src"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Guilherme Blanco",
                    "email": "guilhermeblanco@gmail.com"
                },
                {
                    "name": "Roman Borschel",
                    "email": "roman@code-factory.org"
                },
                {
                    "name": "Benjamin Eberlei",
                    "email": "kontakt@beberlei.de"
                },
                {
                    "name": "Jonathan Wage",
                    "email": "jonwage@gmail.com"
                },
                {
                    "name": "Johannes Schmitt",
                    "email": "schmittjoh@gmail.com"
                }
            ],
            "description": "PHP Doctrine Collections library that adds additional functionality on top of PHP arrays.",
            "homepage": "https://www.doctrine-project.org/projects/collections.html",
            "keywords": [
                "array",
                "collections",
                "iterators",
                "php"
            ],
            "support": {
                "issues": "https://github.com/doctrine/collections/issues",
                "source": "https://github.com/doctrine/collections/tree/2.2.2"
            },
            "funding": [
                {
                    "url": "https://www.doctrine-project.org/sponsorship.html",
                    "type": "custom"
                },
                {
                    "url": "https://www.patreon.com/phpdoctrine",
                    "type": "patreon"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/doctrine%2Fcollections",
                    "type": "tidelift"
                }
            ],
            "time": "2024-04-18T06:56:21+00:00"
        },
        {
            "name": "doctrine/common",
            "version": "3.4.4",
            "source": {
                "type": "git",
                "url": "https://github.com/doctrine/common.git",
                "reference": "0aad4b7ab7ce8c6602dfbb1e1a24581275fb9d1a"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/doctrine/common/zipball/0aad4b7ab7ce8c6602dfbb1e1a24581275fb9d1a",
                "reference": "0aad4b7ab7ce8c6602dfbb1e1a24581275fb9d1a",
                "shasum": ""
            },
            "require": {
                "doctrine/persistence": "^2.0 || ^3.0",
                "php": "^7.1 || ^8.0"
            },
            "require-dev": {
                "doctrine/coding-standard": "^9.0 || ^10.0",
                "doctrine/collections": "^1",
                "phpstan/phpstan": "^1.4.1",
                "phpstan/phpstan-phpunit": "^1",
                "phpunit/phpunit": "^7.5.20 || ^8.5 || ^9.0",
                "squizlabs/php_codesniffer": "^3.0",
                "symfony/phpunit-bridge": "^6.1",
                "vimeo/psalm": "^4.4"
            },
            "type": "library",
            "autoload": {
                "psr-4": {
                    "Doctrine\\Common\\": "src"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Guilherme Blanco",
                    "email": "guilhermeblanco@gmail.com"
                },
                {
                    "name": "Roman Borschel",
                    "email": "roman@code-factory.org"
                },
                {
                    "name": "Benjamin Eberlei",
                    "email": "kontakt@beberlei.de"
                },
                {
                    "name": "Jonathan Wage",
                    "email": "jonwage@gmail.com"
                },
                {
                    "name": "Johannes Schmitt",
                    "email": "schmittjoh@gmail.com"
                },
                {
                    "name": "Marco Pivetta",
                    "email": "ocramius@gmail.com"
                }
            ],
            "description": "PHP Doctrine Common project is a library that provides additional functionality that other Doctrine projects depend on such as better reflection support, proxies and much more.",
            "homepage": "https://www.doctrine-project.org/projects/common.html",
            "keywords": [
                "common",
                "doctrine",
                "php"
            ],
            "support": {
                "issues": "https://github.com/doctrine/common/issues",
                "source": "https://github.com/doctrine/common/tree/3.4.4"
            },
            "funding": [
                {
                    "url": "https://www.doctrine-project.org/sponsorship.html",
                    "type": "custom"
                },
                {
                    "url": "https://www.patreon.com/phpdoctrine",
                    "type": "patreon"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/doctrine%2Fcommon",
                    "type": "tidelift"
                }
            ],
            "time": "2024-04-16T13:35:33+00:00"
        },
        {
            "name": "doctrine/dbal",
            "version": "3.8.6",
            "source": {
                "type": "git",
                "url": "https://github.com/doctrine/dbal.git",
                "reference": "b7411825cf7efb7e51f9791dea19d86e43b399a1"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/doctrine/dbal/zipball/b7411825cf7efb7e51f9791dea19d86e43b399a1",
                "reference": "b7411825cf7efb7e51f9791dea19d86e43b399a1",
                "shasum": ""
            },
            "require": {
                "composer-runtime-api": "^2",
                "doctrine/cache": "^1.11|^2.0",
                "doctrine/deprecations": "^0.5.3|^1",
                "doctrine/event-manager": "^1|^2",
                "php": "^7.4 || ^8.0",
                "psr/cache": "^1|^2|^3",
                "psr/log": "^1|^2|^3"
            },
            "require-dev": {
                "doctrine/coding-standard": "12.0.0",
                "fig/log-test": "^1",
                "jetbrains/phpstorm-stubs": "2023.1",
                "phpstan/phpstan": "1.11.5",
                "phpstan/phpstan-strict-rules": "^1.6",
                "phpunit/phpunit": "9.6.19",
                "psalm/plugin-phpunit": "0.18.4",
                "slevomat/coding-standard": "8.13.1",
                "squizlabs/php_codesniffer": "3.10.1",
                "symfony/cache": "^5.4|^6.0|^7.0",
                "symfony/console": "^4.4|^5.4|^6.0|^7.0",
                "vimeo/psalm": "4.30.0"
            },
            "suggest": {
                "symfony/console": "For helpful console commands such as SQL execution and import of files."
            },
            "bin": [
                "bin/doctrine-dbal"
            ],
            "type": "library",
            "autoload": {
                "psr-4": {
                    "Doctrine\\DBAL\\": "src"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Guilherme Blanco",
                    "email": "guilhermeblanco@gmail.com"
                },
                {
                    "name": "Roman Borschel",
                    "email": "roman@code-factory.org"
                },
                {
                    "name": "Benjamin Eberlei",
                    "email": "kontakt@beberlei.de"
                },
                {
                    "name": "Jonathan Wage",
                    "email": "jonwage@gmail.com"
                }
            ],
            "description": "Powerful PHP database abstraction layer (DBAL) with many features for database schema introspection and management.",
            "homepage": "https://www.doctrine-project.org/projects/dbal.html",
            "keywords": [
                "abstraction",
                "database",
                "db2",
                "dbal",
                "mariadb",
                "mssql",
                "mysql",
                "oci8",
                "oracle",
                "pdo",
                "pgsql",
                "postgresql",
                "queryobject",
                "sasql",
                "sql",
                "sqlite",
                "sqlserver",
                "sqlsrv"
            ],
            "support": {
                "issues": "https://github.com/doctrine/dbal/issues",
                "source": "https://github.com/doctrine/dbal/tree/3.8.6"
            },
            "funding": [
                {
                    "url": "https://www.doctrine-project.org/sponsorship.html",
                    "type": "custom"
                },
                {
                    "url": "https://www.patreon.com/phpdoctrine",
                    "type": "patreon"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/doctrine%2Fdbal",
                    "type": "tidelift"
                }
            ],
            "time": "2024-06-19T10:38:17+00:00"
        },
        {
            "name": "doctrine/deprecations",
            "version": "1.1.3",
            "source": {
                "type": "git",
                "url": "https://github.com/doctrine/deprecations.git",
                "reference": "dfbaa3c2d2e9a9df1118213f3b8b0c597bb99fab"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/doctrine/deprecations/zipball/dfbaa3c2d2e9a9df1118213f3b8b0c597bb99fab",
                "reference": "dfbaa3c2d2e9a9df1118213f3b8b0c597bb99fab",
                "shasum": ""
            },
            "require": {
                "php": "^7.1 || ^8.0"
            },
            "require-dev": {
                "doctrine/coding-standard": "^9",
                "phpstan/phpstan": "1.4.10 || 1.10.15",
                "phpstan/phpstan-phpunit": "^1.0",
                "phpunit/phpunit": "^7.5 || ^8.5 || ^9.5",
                "psalm/plugin-phpunit": "0.18.4",
                "psr/log": "^1 || ^2 || ^3",
                "vimeo/psalm": "4.30.0 || 5.12.0"
            },
            "suggest": {
                "psr/log": "Allows logging deprecations via PSR-3 logger implementation"
            },
            "type": "library",
            "autoload": {
                "psr-4": {
                    "Doctrine\\Deprecations\\": "lib/Doctrine/Deprecations"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "description": "A small layer on top of trigger_error(E_USER_DEPRECATED) or PSR-3 logging with options to disable all deprecations or selectively for packages.",
            "homepage": "https://www.doctrine-project.org/",
            "support": {
                "issues": "https://github.com/doctrine/deprecations/issues",
                "source": "https://github.com/doctrine/deprecations/tree/1.1.3"
            },
            "time": "2024-01-30T19:34:25+00:00"
        },
        {
            "name": "doctrine/event-manager",
            "version": "2.0.1",
            "source": {
                "type": "git",
                "url": "https://github.com/doctrine/event-manager.git",
                "reference": "b680156fa328f1dfd874fd48c7026c41570b9c6e"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/doctrine/event-manager/zipball/b680156fa328f1dfd874fd48c7026c41570b9c6e",
                "reference": "b680156fa328f1dfd874fd48c7026c41570b9c6e",
                "shasum": ""
            },
            "require": {
                "php": "^8.1"
            },
            "conflict": {
                "doctrine/common": "<2.9"
            },
            "require-dev": {
                "doctrine/coding-standard": "^12",
                "phpstan/phpstan": "^1.8.8",
                "phpunit/phpunit": "^10.5",
                "vimeo/psalm": "^5.24"
            },
            "type": "library",
            "autoload": {
                "psr-4": {
                    "Doctrine\\Common\\": "src"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Guilherme Blanco",
                    "email": "guilhermeblanco@gmail.com"
                },
                {
                    "name": "Roman Borschel",
                    "email": "roman@code-factory.org"
                },
                {
                    "name": "Benjamin Eberlei",
                    "email": "kontakt@beberlei.de"
                },
                {
                    "name": "Jonathan Wage",
                    "email": "jonwage@gmail.com"
                },
                {
                    "name": "Johannes Schmitt",
                    "email": "schmittjoh@gmail.com"
                },
                {
                    "name": "Marco Pivetta",
                    "email": "ocramius@gmail.com"
                }
            ],
            "description": "The Doctrine Event Manager is a simple PHP event system that was built to be used with the various Doctrine projects.",
            "homepage": "https://www.doctrine-project.org/projects/event-manager.html",
            "keywords": [
                "event",
                "event dispatcher",
                "event manager",
                "event system",
                "events"
            ],
            "support": {
                "issues": "https://github.com/doctrine/event-manager/issues",
                "source": "https://github.com/doctrine/event-manager/tree/2.0.1"
            },
            "funding": [
                {
                    "url": "https://www.doctrine-project.org/sponsorship.html",
                    "type": "custom"
                },
                {
                    "url": "https://www.patreon.com/phpdoctrine",
                    "type": "patreon"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/doctrine%2Fevent-manager",
                    "type": "tidelift"
                }
            ],
            "time": "2024-05-22T20:47:39+00:00"
        },
        {
            "name": "doctrine/inflector",
            "version": "2.0.10",
            "source": {
                "type": "git",
                "url": "https://github.com/doctrine/inflector.git",
                "reference": "5817d0659c5b50c9b950feb9af7b9668e2c436bc"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/doctrine/inflector/zipball/5817d0659c5b50c9b950feb9af7b9668e2c436bc",
                "reference": "5817d0659c5b50c9b950feb9af7b9668e2c436bc",
                "shasum": ""
            },
            "require": {
                "php": "^7.2 || ^8.0"
            },
            "require-dev": {
                "doctrine/coding-standard": "^11.0",
                "phpstan/phpstan": "^1.8",
                "phpstan/phpstan-phpunit": "^1.1",
                "phpstan/phpstan-strict-rules": "^1.3",
                "phpunit/phpunit": "^8.5 || ^9.5",
                "vimeo/psalm": "^4.25 || ^5.4"
            },
            "type": "library",
            "autoload": {
                "psr-4": {
                    "Doctrine\\Inflector\\": "lib/Doctrine/Inflector"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Guilherme Blanco",
                    "email": "guilhermeblanco@gmail.com"
                },
                {
                    "name": "Roman Borschel",
                    "email": "roman@code-factory.org"
                },
                {
                    "name": "Benjamin Eberlei",
                    "email": "kontakt@beberlei.de"
                },
                {
                    "name": "Jonathan Wage",
                    "email": "jonwage@gmail.com"
                },
                {
                    "name": "Johannes Schmitt",
                    "email": "schmittjoh@gmail.com"
                }
            ],
            "description": "PHP Doctrine Inflector is a small library that can perform string manipulations with regard to upper/lowercase and singular/plural forms of words.",
            "homepage": "https://www.doctrine-project.org/projects/inflector.html",
            "keywords": [
                "inflection",
                "inflector",
                "lowercase",
                "manipulation",
                "php",
                "plural",
                "singular",
                "strings",
                "uppercase",
                "words"
            ],
            "support": {
                "issues": "https://github.com/doctrine/inflector/issues",
                "source": "https://github.com/doctrine/inflector/tree/2.0.10"
            },
            "funding": [
                {
                    "url": "https://www.doctrine-project.org/sponsorship.html",
                    "type": "custom"
                },
                {
                    "url": "https://www.patreon.com/phpdoctrine",
                    "type": "patreon"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/doctrine%2Finflector",
                    "type": "tidelift"
                }
            ],
            "time": "2024-02-18T20:23:39+00:00"
        },
        {
            "name": "doctrine/instantiator",
            "version": "2.0.0",
            "source": {
                "type": "git",
                "url": "https://github.com/doctrine/instantiator.git",
                "reference": "c6222283fa3f4ac679f8b9ced9a4e23f163e80d0"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/doctrine/instantiator/zipball/c6222283fa3f4ac679f8b9ced9a4e23f163e80d0",
                "reference": "c6222283fa3f4ac679f8b9ced9a4e23f163e80d0",
                "shasum": ""
            },
            "require": {
                "php": "^8.1"
            },
            "require-dev": {
                "doctrine/coding-standard": "^11",
                "ext-pdo": "*",
                "ext-phar": "*",
                "phpbench/phpbench": "^1.2",
                "phpstan/phpstan": "^1.9.4",
                "phpstan/phpstan-phpunit": "^1.3",
                "phpunit/phpunit": "^9.5.27",
                "vimeo/psalm": "^5.4"
            },
            "type": "library",
            "autoload": {
                "psr-4": {
                    "Doctrine\\Instantiator\\": "src/Doctrine/Instantiator/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Marco Pivetta",
                    "email": "ocramius@gmail.com",
                    "homepage": "https://ocramius.github.io/"
                }
            ],
            "description": "A small, lightweight utility to instantiate objects in PHP without invoking their constructors",
            "homepage": "https://www.doctrine-project.org/projects/instantiator.html",
            "keywords": [
                "constructor",
                "instantiate"
            ],
            "support": {
                "issues": "https://github.com/doctrine/instantiator/issues",
                "source": "https://github.com/doctrine/instantiator/tree/2.0.0"
            },
            "funding": [
                {
                    "url": "https://www.doctrine-project.org/sponsorship.html",
                    "type": "custom"
                },
                {
                    "url": "https://www.patreon.com/phpdoctrine",
                    "type": "patreon"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/doctrine%2Finstantiator",
                    "type": "tidelift"
                }
            ],
            "time": "2022-12-30T00:23:10+00:00"
        },
        {
            "name": "doctrine/lexer",
            "version": "3.0.1",
            "source": {
                "type": "git",
                "url": "https://github.com/doctrine/lexer.git",
                "reference": "31ad66abc0fc9e1a1f2d9bc6a42668d2fbbcd6dd"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/doctrine/lexer/zipball/31ad66abc0fc9e1a1f2d9bc6a42668d2fbbcd6dd",
                "reference": "31ad66abc0fc9e1a1f2d9bc6a42668d2fbbcd6dd",
                "shasum": ""
            },
            "require": {
                "php": "^8.1"
            },
            "require-dev": {
                "doctrine/coding-standard": "^12",
                "phpstan/phpstan": "^1.10",
                "phpunit/phpunit": "^10.5",
                "psalm/plugin-phpunit": "^0.18.3",
                "vimeo/psalm": "^5.21"
            },
            "type": "library",
            "autoload": {
                "psr-4": {
                    "Doctrine\\Common\\Lexer\\": "src"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Guilherme Blanco",
                    "email": "guilhermeblanco@gmail.com"
                },
                {
                    "name": "Roman Borschel",
                    "email": "roman@code-factory.org"
                },
                {
                    "name": "Johannes Schmitt",
                    "email": "schmittjoh@gmail.com"
                }
            ],
            "description": "PHP Doctrine Lexer parser library that can be used in Top-Down, Recursive Descent Parsers.",
            "homepage": "https://www.doctrine-project.org/projects/lexer.html",
            "keywords": [
                "annotations",
                "docblock",
                "lexer",
                "parser",
                "php"
            ],
            "support": {
                "issues": "https://github.com/doctrine/lexer/issues",
                "source": "https://github.com/doctrine/lexer/tree/3.0.1"
            },
            "funding": [
                {
                    "url": "https://www.doctrine-project.org/sponsorship.html",
                    "type": "custom"
                },
                {
                    "url": "https://www.patreon.com/phpdoctrine",
                    "type": "patreon"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/doctrine%2Flexer",
                    "type": "tidelift"
                }
            ],
            "time": "2024-02-05T11:56:58+00:00"
        },
        {
            "name": "doctrine/orm",
            "version": "2.19.6",
            "source": {
                "type": "git",
                "url": "https://github.com/doctrine/orm.git",
                "reference": "c1bb2ccf4b19c845f91ff7c4c01dc7cbba7f4073"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/doctrine/orm/zipball/c1bb2ccf4b19c845f91ff7c4c01dc7cbba7f4073",
                "reference": "c1bb2ccf4b19c845f91ff7c4c01dc7cbba7f4073",
                "shasum": ""
            },
            "require": {
                "composer-runtime-api": "^2",
                "doctrine/cache": "^1.12.1 || ^2.1.1",
                "doctrine/collections": "^1.5 || ^2.1",
                "doctrine/common": "^3.0.3",
                "doctrine/dbal": "^2.13.1 || ^3.2",
                "doctrine/deprecations": "^0.5.3 || ^1",
                "doctrine/event-manager": "^1.2 || ^2",
                "doctrine/inflector": "^1.4 || ^2.0",
                "doctrine/instantiator": "^1.3 || ^2",
                "doctrine/lexer": "^2 || ^3",
                "doctrine/persistence": "^2.4 || ^3",
                "ext-ctype": "*",
                "php": "^7.1 || ^8.0",
                "psr/cache": "^1 || ^2 || ^3",
                "symfony/console": "^4.2 || ^5.0 || ^6.0 || ^7.0",
                "symfony/polyfill-php72": "^1.23",
                "symfony/polyfill-php80": "^1.16"
            },
            "conflict": {
                "doctrine/annotations": "<1.13 || >= 3.0"
            },
            "require-dev": {
                "doctrine/annotations": "^1.13 || ^2",
                "doctrine/coding-standard": "^9.0.2 || ^12.0",
                "phpbench/phpbench": "^0.16.10 || ^1.0",
                "phpstan/phpstan": "~1.4.10 || 1.11.1",
                "phpunit/phpunit": "^7.5 || ^8.5 || ^9.6",
                "psr/log": "^1 || ^2 || ^3",
                "squizlabs/php_codesniffer": "3.7.2",
                "symfony/cache": "^4.4 || ^5.4 || ^6.4 || ^7.0",
                "symfony/var-exporter": "^4.4 || ^5.4 || ^6.2 || ^7.0",
                "symfony/yaml": "^3.4 || ^4.0 || ^5.0 || ^6.0 || ^7.0",
                "vimeo/psalm": "4.30.0 || 5.24.0"
            },
            "suggest": {
                "ext-dom": "Provides support for XSD validation for XML mapping files",
                "symfony/cache": "Provides cache support for Setup Tool with doctrine/cache 2.0",
                "symfony/yaml": "If you want to use YAML Metadata Mapping Driver"
            },
            "bin": [
                "bin/doctrine"
            ],
            "type": "library",
            "autoload": {
                "psr-4": {
                    "Doctrine\\ORM\\": "src"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Guilherme Blanco",
                    "email": "guilhermeblanco@gmail.com"
                },
                {
                    "name": "Roman Borschel",
                    "email": "roman@code-factory.org"
                },
                {
                    "name": "Benjamin Eberlei",
                    "email": "kontakt@beberlei.de"
                },
                {
                    "name": "Jonathan Wage",
                    "email": "jonwage@gmail.com"
                },
                {
                    "name": "Marco Pivetta",
                    "email": "ocramius@gmail.com"
                }
            ],
            "description": "Object-Relational-Mapper for PHP",
            "homepage": "https://www.doctrine-project.org/projects/orm.html",
            "keywords": [
                "database",
                "orm"
            ],
            "support": {
                "issues": "https://github.com/doctrine/orm/issues",
                "source": "https://github.com/doctrine/orm/tree/2.19.6"
            },
            "time": "2024-06-26T17:24:40+00:00"
        },
        {
            "name": "doctrine/persistence",
            "version": "3.3.3",
            "source": {
                "type": "git",
                "url": "https://github.com/doctrine/persistence.git",
                "reference": "b337726451f5d530df338fc7f68dee8781b49779"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/doctrine/persistence/zipball/b337726451f5d530df338fc7f68dee8781b49779",
                "reference": "b337726451f5d530df338fc7f68dee8781b49779",
                "shasum": ""
            },
            "require": {
                "doctrine/event-manager": "^1 || ^2",
                "php": "^7.2 || ^8.0",
                "psr/cache": "^1.0 || ^2.0 || ^3.0"
            },
            "conflict": {
                "doctrine/common": "<2.10"
            },
            "require-dev": {
                "doctrine/coding-standard": "^12",
                "doctrine/common": "^3.0",
                "phpstan/phpstan": "1.11.1",
                "phpstan/phpstan-phpunit": "^1",
                "phpstan/phpstan-strict-rules": "^1.1",
                "phpunit/phpunit": "^8.5 || ^9.5",
                "symfony/cache": "^4.4 || ^5.4 || ^6.0",
                "vimeo/psalm": "4.30.0 || 5.24.0"
            },
            "type": "library",
            "autoload": {
                "psr-4": {
                    "Doctrine\\Persistence\\": "src/Persistence"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Guilherme Blanco",
                    "email": "guilhermeblanco@gmail.com"
                },
                {
                    "name": "Roman Borschel",
                    "email": "roman@code-factory.org"
                },
                {
                    "name": "Benjamin Eberlei",
                    "email": "kontakt@beberlei.de"
                },
                {
                    "name": "Jonathan Wage",
                    "email": "jonwage@gmail.com"
                },
                {
                    "name": "Johannes Schmitt",
                    "email": "schmittjoh@gmail.com"
                },
                {
                    "name": "Marco Pivetta",
                    "email": "ocramius@gmail.com"
                }
            ],
            "description": "The Doctrine Persistence project is a set of shared interfaces and functionality that the different Doctrine object mappers share.",
            "homepage": "https://www.doctrine-project.org/projects/persistence.html",
            "keywords": [
                "mapper",
                "object",
                "odm",
                "orm",
                "persistence"
            ],
            "support": {
                "issues": "https://github.com/doctrine/persistence/issues",
                "source": "https://github.com/doctrine/persistence/tree/3.3.3"
            },
            "funding": [
                {
                    "url": "https://www.doctrine-project.org/sponsorship.html",
                    "type": "custom"
                },
                {
                    "url": "https://www.patreon.com/phpdoctrine",
                    "type": "patreon"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/doctrine%2Fpersistence",
                    "type": "tidelift"
                }
            ],
            "time": "2024-06-20T10:14:30+00:00"
        },
        {
            "name": "elasticsearch/elasticsearch",
            "version": "v7.17.2",
            "source": {
                "type": "git",
                "url": "https://github.com/elastic/elasticsearch-php.git",
                "reference": "2d302233f2bb0926812d82823bb820d405e130fc"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/elastic/elasticsearch-php/zipball/2d302233f2bb0926812d82823bb820d405e130fc",
                "reference": "2d302233f2bb0926812d82823bb820d405e130fc",
                "shasum": ""
            },
            "require": {
                "ext-json": ">=1.3.7",
                "ezimuel/ringphp": "^1.1.2",
                "php": "^7.3 || ^8.0",
                "psr/log": "^1|^2|^3"
            },
            "require-dev": {
                "ext-yaml": "*",
                "ext-zip": "*",
                "mockery/mockery": "^1.2",
                "phpstan/phpstan": "^1.10",
                "phpunit/phpunit": "^9.3",
                "squizlabs/php_codesniffer": "^3.4",
                "symfony/finder": "~4.0"
            },
            "suggest": {
                "ext-curl": "*",
                "monolog/monolog": "Allows for client-level logging and tracing"
            },
            "type": "library",
            "autoload": {
                "files": [
                    "src/autoload.php"
                ],
                "psr-4": {
                    "Elasticsearch\\": "src/Elasticsearch/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "Apache-2.0",
                "LGPL-2.1-only"
            ],
            "authors": [
                {
                    "name": "Zachary Tong"
                },
                {
                    "name": "Enrico Zimuel"
                }
            ],
            "description": "PHP Client for Elasticsearch",
            "keywords": [
                "client",
                "elasticsearch",
                "search"
            ],
            "support": {
                "issues": "https://github.com/elastic/elasticsearch-php/issues",
                "source": "https://github.com/elastic/elasticsearch-php/tree/v7.17.2"
            },
            "time": "2023-04-21T15:31:12+00:00"
        },
        {
            "name": "ezimuel/guzzlestreams",
            "version": "3.1.0",
            "source": {
                "type": "git",
                "url": "https://github.com/ezimuel/guzzlestreams.git",
                "reference": "b4b5a025dfee70d6cd34c780e07330eb93d5b997"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/ezimuel/guzzlestreams/zipball/b4b5a025dfee70d6cd34c780e07330eb93d5b997",
                "reference": "b4b5a025dfee70d6cd34c780e07330eb93d5b997",
                "shasum": ""
            },
            "require": {
                "php": ">=5.4.0"
            },
            "require-dev": {
                "phpunit/phpunit": "~9.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "3.0-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "GuzzleHttp\\Stream\\": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Michael Dowling",
                    "email": "mtdowling@gmail.com",
                    "homepage": "https://github.com/mtdowling"
                }
            ],
            "description": "Fork of guzzle/streams (abandoned) to be used with elasticsearch-php",
            "homepage": "http://guzzlephp.org/",
            "keywords": [
                "Guzzle",
                "stream"
            ],
            "support": {
                "source": "https://github.com/ezimuel/guzzlestreams/tree/3.1.0"
            },
            "time": "2022-10-24T12:58:50+00:00"
        },
        {
            "name": "ezimuel/ringphp",
            "version": "1.2.2",
            "source": {
                "type": "git",
                "url": "https://github.com/ezimuel/ringphp.git",
                "reference": "7887fc8488013065f72f977dcb281994f5fde9f4"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/ezimuel/ringphp/zipball/7887fc8488013065f72f977dcb281994f5fde9f4",
                "reference": "7887fc8488013065f72f977dcb281994f5fde9f4",
                "shasum": ""
            },
            "require": {
                "ezimuel/guzzlestreams": "^3.0.1",
                "php": ">=5.4.0",
                "react/promise": "~2.0"
            },
            "replace": {
                "guzzlehttp/ringphp": "self.version"
            },
            "require-dev": {
                "ext-curl": "*",
                "phpunit/phpunit": "~9.0"
            },
            "suggest": {
                "ext-curl": "Guzzle will use specific adapters if cURL is present"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.1-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "GuzzleHttp\\Ring\\": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Michael Dowling",
                    "email": "mtdowling@gmail.com",
                    "homepage": "https://github.com/mtdowling"
                }
            ],
            "description": "Fork of guzzle/RingPHP (abandoned) to be used with elasticsearch-php",
            "support": {
                "source": "https://github.com/ezimuel/ringphp/tree/1.2.2"
            },
            "time": "2022-12-07T11:28:53+00:00"
        },
        {
            "name": "lambdish/phunctional",
            "version": "v2.1.0",
            "source": {
                "type": "git",
                "url": "https://github.com/Lambdish/phunctional.git",
                "reference": "ed3482e7da134d886789abb33c6df22a5d2f271c"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/Lambdish/phunctional/zipball/ed3482e7da134d886789abb33c6df22a5d2f271c",
                "reference": "ed3482e7da134d886789abb33c6df22a5d2f271c",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2"
            },
            "require-dev": {
                "phpstan/phpstan": "^0.11.16",
                "phpunit/phpunit": "^8.4"
            },
            "type": "library",
            "autoload": {
                "files": [
                    "src/_bootstrap.php"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Eloi Poch"
                },
                {
                    "name": "Jorge Ávila"
                },
                {
                    "name": "Rafa Gómez"
                }
            ],
            "description": "λ PHP functional library",
            "keywords": [
                "functional",
                "generator",
                "lambda",
                "library",
                "php"
            ],
            "support": {
                "issues": "https://github.com/Lambdish/phunctional/issues",
                "source": "https://github.com/Lambdish/phunctional/tree/v2.1.0"
            },
            "time": "2020-09-18T07:22:08+00:00"
        },
        {
            "name": "laminas/laminas-code",
            "version": "4.14.0",
            "source": {
                "type": "git",
                "url": "https://github.com/laminas/laminas-code.git",
                "reference": "562e02b7d85cb9142b5116cc76c4c7c162a11a1c"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/laminas/laminas-code/zipball/562e02b7d85cb9142b5116cc76c4c7c162a11a1c",
                "reference": "562e02b7d85cb9142b5116cc76c4c7c162a11a1c",
                "shasum": ""
            },
            "require": {
                "php": "~8.1.0 || ~8.2.0 || ~8.3.0"
            },
            "require-dev": {
                "doctrine/annotations": "^2.0.1",
                "ext-phar": "*",
                "laminas/laminas-coding-standard": "^2.5.0",
                "laminas/laminas-stdlib": "^3.17.0",
                "phpunit/phpunit": "^10.3.3",
                "psalm/plugin-phpunit": "^0.19.0",
                "vimeo/psalm": "^5.15.0"
            },
            "suggest": {
                "doctrine/annotations": "Doctrine\\Common\\Annotations >=1.0 for annotation features",
                "laminas/laminas-stdlib": "Laminas\\Stdlib component"
            },
            "type": "library",
            "autoload": {
                "psr-4": {
                    "Laminas\\Code\\": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause"
            ],
            "description": "Extensions to the PHP Reflection API, static code scanning, and code generation",
            "homepage": "https://laminas.dev",
            "keywords": [
                "code",
                "laminas",
                "laminasframework"
            ],
            "support": {
                "chat": "https://laminas.dev/chat",
                "docs": "https://docs.laminas.dev/laminas-code/",
                "forum": "https://discourse.laminas.dev",
                "issues": "https://github.com/laminas/laminas-code/issues",
                "rss": "https://github.com/laminas/laminas-code/releases.atom",
                "source": "https://github.com/laminas/laminas-code"
            },
            "funding": [
                {
                    "url": "https://funding.communitybridge.org/projects/laminas-project",
                    "type": "community_bridge"
                }
            ],
            "time": "2024-06-17T08:50:25+00:00"
        },
        {
            "name": "laminas/laminas-zendframework-bridge",
            "version": "1.8.0",
            "source": {
                "type": "git",
                "url": "https://github.com/laminas/laminas-zendframework-bridge.git",
                "reference": "eb0d96c708b92177a92bc2239543d3ed523452c6"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/laminas/laminas-zendframework-bridge/zipball/eb0d96c708b92177a92bc2239543d3ed523452c6",
                "reference": "eb0d96c708b92177a92bc2239543d3ed523452c6",
                "shasum": ""
            },
            "require": {
                "php": "~8.1.0 || ~8.2.0 || ~8.3.0"
            },
            "require-dev": {
                "phpunit/phpunit": "^10.4",
                "psalm/plugin-phpunit": "^0.18.0",
                "squizlabs/php_codesniffer": "^3.7.1",
                "vimeo/psalm": "^5.16.0"
            },
            "type": "library",
            "extra": {
                "laminas": {
                    "module": "Laminas\\ZendFrameworkBridge"
                }
            },
            "autoload": {
                "files": [
                    "src/autoload.php"
                ],
                "psr-4": {
                    "Laminas\\ZendFrameworkBridge\\": "src//"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause"
            ],
            "description": "Alias legacy ZF class names to Laminas Project equivalents.",
            "keywords": [
                "ZendFramework",
                "autoloading",
                "laminas",
                "zf"
            ],
            "support": {
                "forum": "https://discourse.laminas.dev/",
                "issues": "https://github.com/laminas/laminas-zendframework-bridge/issues",
                "rss": "https://github.com/laminas/laminas-zendframework-bridge/releases.atom",
                "source": "https://github.com/laminas/laminas-zendframework-bridge"
            },
            "funding": [
                {
                    "url": "https://funding.communitybridge.org/projects/laminas-project",
                    "type": "community_bridge"
                }
            ],
            "abandoned": true,
            "time": "2023-11-24T13:56:19+00:00"
        },
        {
            "name": "monolog/monolog",
            "version": "3.7.0",
            "source": {
                "type": "git",
                "url": "https://github.com/Seldaek/monolog.git",
                "reference": "f4393b648b78a5408747de94fca38beb5f7e9ef8"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/Seldaek/monolog/zipball/f4393b648b78a5408747de94fca38beb5f7e9ef8",
                "reference": "f4393b648b78a5408747de94fca38beb5f7e9ef8",
                "shasum": ""
            },
            "require": {
                "php": ">=8.1",
                "psr/log": "^2.0 || ^3.0"
            },
            "provide": {
                "psr/log-implementation": "3.0.0"
            },
            "require-dev": {
                "aws/aws-sdk-php": "^3.0",
                "doctrine/couchdb": "~1.0@dev",
                "elasticsearch/elasticsearch": "^7 || ^8",
                "ext-json": "*",
                "graylog2/gelf-php": "^1.4.2 || ^2.0",
                "guzzlehttp/guzzle": "^7.4.5",
                "guzzlehttp/psr7": "^2.2",
                "mongodb/mongodb": "^1.8",
                "php-amqplib/php-amqplib": "~2.4 || ^3",
                "phpstan/phpstan": "^1.9",
                "phpstan/phpstan-deprecation-rules": "^1.0",
                "phpstan/phpstan-strict-rules": "^1.4",
                "phpunit/phpunit": "^10.5.17",
                "predis/predis": "^1.1 || ^2",
                "ruflin/elastica": "^7",
                "symfony/mailer": "^5.4 || ^6",
                "symfony/mime": "^5.4 || ^6"
            },
            "suggest": {
                "aws/aws-sdk-php": "Allow sending log messages to AWS services like DynamoDB",
                "doctrine/couchdb": "Allow sending log messages to a CouchDB server",
                "elasticsearch/elasticsearch": "Allow sending log messages to an Elasticsearch server via official client",
                "ext-amqp": "Allow sending log messages to an AMQP server (1.0+ required)",
                "ext-curl": "Required to send log messages using the IFTTTHandler, the LogglyHandler, the SendGridHandler, the SlackWebhookHandler or the TelegramBotHandler",
                "ext-mbstring": "Allow to work properly with unicode symbols",
                "ext-mongodb": "Allow sending log messages to a MongoDB server (via driver)",
                "ext-openssl": "Required to send log messages using SSL",
                "ext-sockets": "Allow sending log messages to a Syslog server (via UDP driver)",
                "graylog2/gelf-php": "Allow sending log messages to a GrayLog2 server",
                "mongodb/mongodb": "Allow sending log messages to a MongoDB server (via library)",
                "php-amqplib/php-amqplib": "Allow sending log messages to an AMQP server using php-amqplib",
                "rollbar/rollbar": "Allow sending log messages to Rollbar",
                "ruflin/elastica": "Allow sending log messages to an Elastic Search server"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-main": "3.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Monolog\\": "src/Monolog"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Jordi Boggiano",
                    "email": "j.boggiano@seld.be",
                    "homepage": "https://seld.be"
                }
            ],
            "description": "Sends your logs to files, sockets, inboxes, databases and various web services",
            "homepage": "https://github.com/Seldaek/monolog",
            "keywords": [
                "log",
                "logging",
                "psr-3"
            ],
            "support": {
                "issues": "https://github.com/Seldaek/monolog/issues",
                "source": "https://github.com/Seldaek/monolog/tree/3.7.0"
            },
            "funding": [
                {
                    "url": "https://github.com/Seldaek",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/monolog/monolog",
                    "type": "tidelift"
                }
            ],
            "time": "2024-06-28T09:40:51+00:00"
        },
        {
            "name": "ocramius/proxy-manager",
            "version": "2.14.1",
            "source": {
                "type": "git",
                "url": "https://github.com/Ocramius/ProxyManager.git",
                "reference": "3990d60ef79001badbab4927a6a811682274a0d1"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/Ocramius/ProxyManager/zipball/3990d60ef79001badbab4927a6a811682274a0d1",
                "reference": "3990d60ef79001badbab4927a6a811682274a0d1",
                "shasum": ""
            },
            "require": {
                "composer-runtime-api": "^2.1.0",
                "laminas/laminas-code": "^4.4.2",
                "php": "~8.0.0",
                "webimpress/safe-writer": "^2.2.0"
            },
            "conflict": {
                "thecodingmachine/safe": "<1.3.3"
            },
            "require-dev": {
                "codelicia/xulieta": "^0.1.6",
                "doctrine/coding-standard": "^9.0.0",
                "ext-phar": "*",
                "phpbench/phpbench": "^1.0.3",
                "phpunit/phpunit": "^9.5.6",
                "roave/infection-static-analysis-plugin": "^1.8",
                "squizlabs/php_codesniffer": "^3.6.0",
                "vimeo/psalm": "^4.8.1"
            },
            "suggest": {
                "laminas/laminas-json": "To have the JsonRpc adapter (Remote Object feature)",
                "laminas/laminas-soap": "To have the Soap adapter (Remote Object feature)",
                "laminas/laminas-xmlrpc": "To have the XmlRpc adapter (Remote Object feature)",
                "ocramius/generated-hydrator": "To have very fast object to array to object conversion for ghost objects"
            },
            "type": "library",
            "autoload": {
                "psr-4": {
                    "ProxyManager\\": "src/ProxyManager"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Marco Pivetta",
                    "email": "ocramius@gmail.com",
                    "homepage": "https://ocramius.github.io/"
                }
            ],
            "description": "A library providing utilities to generate, instantiate and generally operate with Object Proxies",
            "homepage": "https://github.com/Ocramius/ProxyManager",
            "keywords": [
                "aop",
                "lazy loading",
                "proxy",
                "proxy pattern",
                "service proxies"
            ],
            "support": {
                "issues": "https://github.com/Ocramius/ProxyManager/issues",
                "source": "https://github.com/Ocramius/ProxyManager/tree/2.14.1"
            },
            "funding": [
                {
                    "url": "https://github.com/Ocramius",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/ocramius/proxy-manager",
                    "type": "tidelift"
                }
            ],
            "time": "2022-03-05T18:43:14+00:00"
        },
        {
            "name": "promphp/prometheus_client_php",
            "version": "v2.11.0",
            "source": {
                "type": "git",
                "url": "https://github.com/PromPHP/prometheus_client_php.git",
                "reference": "35d5a68628ea18209938bc1b8796646015ab93cf"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/PromPHP/prometheus_client_php/zipball/35d5a68628ea18209938bc1b8796646015ab93cf",
                "reference": "35d5a68628ea18209938bc1b8796646015ab93cf",
                "shasum": ""
            },
            "require": {
                "ext-json": "*",
                "php": "^7.2|^8.0"
            },
            "replace": {
                "endclothing/prometheus_client_php": "*",
                "jimdo/prometheus_client_php": "*",
                "lkaemmerling/prometheus_client_php": "*"
            },
            "require-dev": {
                "guzzlehttp/guzzle": "^6.3|^7.0",
                "phpstan/extension-installer": "^1.0",
                "phpstan/phpstan": "^1.5.4",
                "phpstan/phpstan-phpunit": "^1.1.0",
                "phpstan/phpstan-strict-rules": "^1.1.0",
                "phpunit/phpunit": "^9.4",
                "squizlabs/php_codesniffer": "^3.6",
                "symfony/polyfill-apcu": "^1.6"
            },
            "suggest": {
                "ext-apc": "Required if using APCu.",
                "ext-pdo": "Required if using PDO.",
                "ext-redis": "Required if using Redis.",
                "promphp/prometheus_push_gateway_php": "An easy client for using Prometheus PushGateway.",
                "symfony/polyfill-apcu": "Required if you use APCu on PHP8.0+"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.0-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Prometheus\\": "src/Prometheus/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "Apache-2.0"
            ],
            "authors": [
                {
                    "name": "Lukas Kämmerling",
                    "email": "kontakt@lukas-kaemmerling.de"
                }
            ],
            "description": "Prometheus instrumentation library for PHP applications.",
            "support": {
                "issues": "https://github.com/PromPHP/prometheus_client_php/issues",
                "source": "https://github.com/PromPHP/prometheus_client_php/tree/v2.11.0"
            },
            "time": "2024-08-05T07:58:08+00:00"
        },
        {
            "name": "psr/cache",
            "version": "3.0.0",
            "source": {
                "type": "git",
                "url": "https://github.com/php-fig/cache.git",
                "reference": "aa5030cfa5405eccfdcb1083ce040c2cb8d253bf"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/php-fig/cache/zipball/aa5030cfa5405eccfdcb1083ce040c2cb8d253bf",
                "reference": "aa5030cfa5405eccfdcb1083ce040c2cb8d253bf",
                "shasum": ""
            },
            "require": {
                "php": ">=8.0.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.0.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Psr\\Cache\\": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "PHP-FIG",
                    "homepage": "https://www.php-fig.org/"
                }
            ],
            "description": "Common interface for caching libraries",
            "keywords": [
                "cache",
                "psr",
                "psr-6"
            ],
            "support": {
                "source": "https://github.com/php-fig/cache/tree/3.0.0"
            },
            "time": "2021-02-03T23:26:27+00:00"
        },
        {
            "name": "psr/clock",
            "version": "1.0.0",
            "source": {
                "type": "git",
                "url": "https://github.com/php-fig/clock.git",
                "reference": "e41a24703d4560fd0acb709162f73b8adfc3aa0d"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/php-fig/clock/zipball/e41a24703d4560fd0acb709162f73b8adfc3aa0d",
                "reference": "e41a24703d4560fd0acb709162f73b8adfc3aa0d",
                "shasum": ""
            },
            "require": {
                "php": "^7.0 || ^8.0"
            },
            "type": "library",
            "autoload": {
                "psr-4": {
                    "Psr\\Clock\\": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "PHP-FIG",
                    "homepage": "https://www.php-fig.org/"
                }
            ],
            "description": "Common interface for reading the clock.",
            "homepage": "https://github.com/php-fig/clock",
            "keywords": [
                "clock",
                "now",
                "psr",
                "psr-20",
                "time"
            ],
            "support": {
                "issues": "https://github.com/php-fig/clock/issues",
                "source": "https://github.com/php-fig/clock/tree/1.0.0"
            },
            "time": "2022-11-25T14:36:26+00:00"
        },
        {
            "name": "psr/container",
            "version": "2.0.2",
            "source": {
                "type": "git",
                "url": "https://github.com/php-fig/container.git",
                "reference": "c71ecc56dfe541dbd90c5360474fbc405f8d5963"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/php-fig/container/zipball/c71ecc56dfe541dbd90c5360474fbc405f8d5963",
                "reference": "c71ecc56dfe541dbd90c5360474fbc405f8d5963",
                "shasum": ""
            },
            "require": {
                "php": ">=7.4.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "2.0.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Psr\\Container\\": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "PHP-FIG",
                    "homepage": "https://www.php-fig.org/"
                }
            ],
            "description": "Common Container Interface (PHP FIG PSR-11)",
            "homepage": "https://github.com/php-fig/container",
            "keywords": [
                "PSR-11",
                "container",
                "container-interface",
                "container-interop",
                "psr"
            ],
            "support": {
                "issues": "https://github.com/php-fig/container/issues",
                "source": "https://github.com/php-fig/container/tree/2.0.2"
            },
            "time": "2021-11-05T16:47:00+00:00"
        },
        {
            "name": "psr/event-dispatcher",
            "version": "1.0.0",
            "source": {
                "type": "git",
                "url": "https://github.com/php-fig/event-dispatcher.git",
                "reference": "dbefd12671e8a14ec7f180cab83036ed26714bb0"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/php-fig/event-dispatcher/zipball/dbefd12671e8a14ec7f180cab83036ed26714bb0",
                "reference": "dbefd12671e8a14ec7f180cab83036ed26714bb0",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.0.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Psr\\EventDispatcher\\": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "PHP-FIG",
                    "homepage": "http://www.php-fig.org/"
                }
            ],
            "description": "Standard interfaces for event handling.",
            "keywords": [
                "events",
                "psr",
                "psr-14"
            ],
            "support": {
                "issues": "https://github.com/php-fig/event-dispatcher/issues",
                "source": "https://github.com/php-fig/event-dispatcher/tree/1.0.0"
            },
            "time": "2019-01-08T18:20:26+00:00"
        },
        {
            "name": "psr/log",
            "version": "3.0.0",
            "source": {
                "type": "git",
                "url": "https://github.com/php-fig/log.git",
                "reference": "fe5ea303b0887d5caefd3d431c3e61ad47037001"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/php-fig/log/zipball/fe5ea303b0887d5caefd3d431c3e61ad47037001",
                "reference": "fe5ea303b0887d5caefd3d431c3e61ad47037001",
                "shasum": ""
            },
            "require": {
                "php": ">=8.0.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "3.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Psr\\Log\\": "src"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "PHP-FIG",
                    "homepage": "https://www.php-fig.org/"
                }
            ],
            "description": "Common interface for logging libraries",
            "homepage": "https://github.com/php-fig/log",
            "keywords": [
                "log",
                "psr",
                "psr-3"
            ],
            "support": {
                "source": "https://github.com/php-fig/log/tree/3.0.0"
            },
            "time": "2021-07-14T16:46:02+00:00"
        },
        {
            "name": "ramsey/collection",
            "version": "2.0.0",
            "source": {
                "type": "git",
                "url": "https://github.com/ramsey/collection.git",
                "reference": "a4b48764bfbb8f3a6a4d1aeb1a35bb5e9ecac4a5"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/ramsey/collection/zipball/a4b48764bfbb8f3a6a4d1aeb1a35bb5e9ecac4a5",
                "reference": "a4b48764bfbb8f3a6a4d1aeb1a35bb5e9ecac4a5",
                "shasum": ""
            },
            "require": {
                "php": "^8.1"
            },
            "require-dev": {
                "captainhook/plugin-composer": "^5.3",
                "ergebnis/composer-normalize": "^2.28.3",
                "fakerphp/faker": "^1.21",
                "hamcrest/hamcrest-php": "^2.0",
                "jangregor/phpstan-prophecy": "^1.0",
                "mockery/mockery": "^1.5",
                "php-parallel-lint/php-console-highlighter": "^1.0",
                "php-parallel-lint/php-parallel-lint": "^1.3",
                "phpcsstandards/phpcsutils": "^1.0.0-rc1",
                "phpspec/prophecy-phpunit": "^2.0",
                "phpstan/extension-installer": "^1.2",
                "phpstan/phpstan": "^1.9",
                "phpstan/phpstan-mockery": "^1.1",
                "phpstan/phpstan-phpunit": "^1.3",
                "phpunit/phpunit": "^9.5",
                "psalm/plugin-mockery": "^1.1",
                "psalm/plugin-phpunit": "^0.18.4",
                "ramsey/coding-standard": "^2.0.3",
                "ramsey/conventional-commits": "^1.3",
                "vimeo/psalm": "^5.4"
            },
            "type": "library",
            "extra": {
                "captainhook": {
                    "force-install": true
                },
                "ramsey/conventional-commits": {
                    "configFile": "conventional-commits.json"
                }
            },
            "autoload": {
                "psr-4": {
                    "Ramsey\\Collection\\": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Ben Ramsey",
                    "email": "ben@benramsey.com",
                    "homepage": "https://benramsey.com"
                }
            ],
            "description": "A PHP library for representing and manipulating collections.",
            "keywords": [
                "array",
                "collection",
                "hash",
                "map",
                "queue",
                "set"
            ],
            "support": {
                "issues": "https://github.com/ramsey/collection/issues",
                "source": "https://github.com/ramsey/collection/tree/2.0.0"
            },
            "funding": [
                {
                    "url": "https://github.com/ramsey",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/ramsey/collection",
                    "type": "tidelift"
                }
            ],
            "time": "2022-12-31T21:50:55+00:00"
        },
        {
            "name": "ramsey/uuid",
            "version": "4.7.6",
            "source": {
                "type": "git",
                "url": "https://github.com/ramsey/uuid.git",
                "reference": "91039bc1faa45ba123c4328958e620d382ec7088"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/ramsey/uuid/zipball/91039bc1faa45ba123c4328958e620d382ec7088",
                "reference": "91039bc1faa45ba123c4328958e620d382ec7088",
                "shasum": ""
            },
            "require": {
                "brick/math": "^0.8.8 || ^0.9 || ^0.10 || ^0.11 || ^0.12",
                "ext-json": "*",
                "php": "^8.0",
                "ramsey/collection": "^1.2 || ^2.0"
            },
            "replace": {
                "rhumsaa/uuid": "self.version"
            },
            "require-dev": {
                "captainhook/captainhook": "^5.10",
                "captainhook/plugin-composer": "^5.3",
                "dealerdirect/phpcodesniffer-composer-installer": "^0.7.0",
                "doctrine/annotations": "^1.8",
                "ergebnis/composer-normalize": "^2.15",
                "mockery/mockery": "^1.3",
                "paragonie/random-lib": "^2",
                "php-mock/php-mock": "^2.2",
                "php-mock/php-mock-mockery": "^1.3",
                "php-parallel-lint/php-parallel-lint": "^1.1",
                "phpbench/phpbench": "^1.0",
                "phpstan/extension-installer": "^1.1",
                "phpstan/phpstan": "^1.8",
                "phpstan/phpstan-mockery": "^1.1",
                "phpstan/phpstan-phpunit": "^1.1",
                "phpunit/phpunit": "^8.5 || ^9",
                "ramsey/composer-repl": "^1.4",
                "slevomat/coding-standard": "^8.4",
                "squizlabs/php_codesniffer": "^3.5",
                "vimeo/psalm": "^4.9"
            },
            "suggest": {
                "ext-bcmath": "Enables faster math with arbitrary-precision integers using BCMath.",
                "ext-gmp": "Enables faster math with arbitrary-precision integers using GMP.",
                "ext-uuid": "Enables the use of PeclUuidTimeGenerator and PeclUuidRandomGenerator.",
                "paragonie/random-lib": "Provides RandomLib for use with the RandomLibAdapter",
                "ramsey/uuid-doctrine": "Allows the use of Ramsey\\Uuid\\Uuid as Doctrine field type."
            },
            "type": "library",
            "extra": {
                "captainhook": {
                    "force-install": true
                }
            },
            "autoload": {
                "files": [
                    "src/functions.php"
                ],
                "psr-4": {
                    "Ramsey\\Uuid\\": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "description": "A PHP library for generating and working with universally unique identifiers (UUIDs).",
            "keywords": [
                "guid",
                "identifier",
                "uuid"
            ],
            "support": {
                "issues": "https://github.com/ramsey/uuid/issues",
                "source": "https://github.com/ramsey/uuid/tree/4.7.6"
            },
            "funding": [
                {
                    "url": "https://github.com/ramsey",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/ramsey/uuid",
                    "type": "tidelift"
                }
            ],
            "time": "2024-04-27T21:32:50+00:00"
        },
        {
            "name": "react/promise",
            "version": "v2.11.0",
            "source": {
                "type": "git",
                "url": "https://github.com/reactphp/promise.git",
                "reference": "1a8460931ea36dc5c76838fec5734d55c88c6831"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/reactphp/promise/zipball/1a8460931ea36dc5c76838fec5734d55c88c6831",
                "reference": "1a8460931ea36dc5c76838fec5734d55c88c6831",
                "shasum": ""
            },
            "require": {
                "php": ">=5.4.0"
            },
            "require-dev": {
                "phpunit/phpunit": "^9.6 || ^5.7 || ^4.8.36"
            },
            "type": "library",
            "autoload": {
                "files": [
                    "src/functions_include.php"
                ],
                "psr-4": {
                    "React\\Promise\\": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Jan Sorgalla",
                    "email": "jsorgalla@gmail.com",
                    "homepage": "https://sorgalla.com/"
                },
                {
                    "name": "Christian Lück",
                    "email": "christian@clue.engineering",
                    "homepage": "https://clue.engineering/"
                },
                {
                    "name": "Cees-Jan Kiewiet",
                    "email": "reactphp@ceesjankiewiet.nl",
                    "homepage": "https://wyrihaximus.net/"
                },
                {
                    "name": "Chris Boden",
                    "email": "cboden@gmail.com",
                    "homepage": "https://cboden.dev/"
                }
            ],
            "description": "A lightweight implementation of CommonJS Promises/A for PHP",
            "keywords": [
                "promise",
                "promises"
            ],
            "support": {
                "issues": "https://github.com/reactphp/promise/issues",
                "source": "https://github.com/reactphp/promise/tree/v2.11.0"
            },
            "funding": [
                {
                    "url": "https://opencollective.com/reactphp",
                    "type": "open_collective"
                }
            ],
            "time": "2023-11-16T16:16:50+00:00"
        },
        {
            "name": "symfony/cache",
            "version": "v7.1.3",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/cache.git",
                "reference": "8ac37acee794372f9732fe8a61a8221f6762148e"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/cache/zipball/8ac37acee794372f9732fe8a61a8221f6762148e",
                "reference": "8ac37acee794372f9732fe8a61a8221f6762148e",
                "shasum": ""
            },
            "require": {
                "php": ">=8.2",
                "psr/cache": "^2.0|^3.0",
                "psr/log": "^1.1|^2|^3",
                "symfony/cache-contracts": "^2.5|^3",
                "symfony/deprecation-contracts": "^2.5|^3.0",
                "symfony/service-contracts": "^2.5|^3",
                "symfony/var-exporter": "^6.4|^7.0"
            },
            "conflict": {
                "doctrine/dbal": "<3.6",
                "symfony/dependency-injection": "<6.4",
                "symfony/http-kernel": "<6.4",
                "symfony/var-dumper": "<6.4"
            },
            "provide": {
                "psr/cache-implementation": "2.0|3.0",
                "psr/simple-cache-implementation": "1.0|2.0|3.0",
                "symfony/cache-implementation": "1.1|2.0|3.0"
            },
            "require-dev": {
                "cache/integration-tests": "dev-master",
                "doctrine/dbal": "^3.6|^4",
                "predis/predis": "^1.1|^2.0",
                "psr/simple-cache": "^1.0|^2.0|^3.0",
                "symfony/config": "^6.4|^7.0",
                "symfony/dependency-injection": "^6.4|^7.0",
                "symfony/filesystem": "^6.4|^7.0",
                "symfony/http-kernel": "^6.4|^7.0",
                "symfony/messenger": "^6.4|^7.0",
                "symfony/var-dumper": "^6.4|^7.0"
            },
            "type": "library",
            "autoload": {
                "psr-4": {
                    "Symfony\\Component\\Cache\\": ""
                },
                "classmap": [
                    "Traits/ValueWrapper.php"
                ],
                "exclude-from-classmap": [
                    "/Tests/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Nicolas Grekas",
                    "email": "p@tchwork.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Provides extended PSR-6, PSR-16 (and tags) implementations",
            "homepage": "https://symfony.com",
            "keywords": [
                "caching",
                "psr6"
            ],
            "support": {
                "source": "https://github.com/symfony/cache/tree/v7.1.3"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2024-07-17T06:10:24+00:00"
        },
        {
            "name": "symfony/cache-contracts",
            "version": "v3.5.0",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/cache-contracts.git",
                "reference": "df6a1a44c890faded49a5fca33c2d5c5fd3c2197"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/cache-contracts/zipball/df6a1a44c890faded49a5fca33c2d5c5fd3c2197",
                "reference": "df6a1a44c890faded49a5fca33c2d5c5fd3c2197",
                "shasum": ""
            },
            "require": {
                "php": ">=8.1",
                "psr/cache": "^3.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-main": "3.5-dev"
                },
                "thanks": {
                    "name": "symfony/contracts",
                    "url": "https://github.com/symfony/contracts"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Contracts\\Cache\\": ""
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Nicolas Grekas",
                    "email": "p@tchwork.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Generic abstractions related to caching",
            "homepage": "https://symfony.com",
            "keywords": [
                "abstractions",
                "contracts",
                "decoupling",
                "interfaces",
                "interoperability",
                "standards"
            ],
            "support": {
                "source": "https://github.com/symfony/cache-contracts/tree/v3.5.0"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2024-04-18T09:32:20+00:00"
        },
        {
            "name": "symfony/clock",
            "version": "v7.1.1",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/clock.git",
                "reference": "3dfc8b084853586de51dd1441c6242c76a28cbe7"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/clock/zipball/3dfc8b084853586de51dd1441c6242c76a28cbe7",
                "reference": "3dfc8b084853586de51dd1441c6242c76a28cbe7",
                "shasum": ""
            },
            "require": {
                "php": ">=8.2",
                "psr/clock": "^1.0",
                "symfony/polyfill-php83": "^1.28"
            },
            "provide": {
                "psr/clock-implementation": "1.0"
            },
            "type": "library",
            "autoload": {
                "files": [
                    "Resources/now.php"
                ],
                "psr-4": {
                    "Symfony\\Component\\Clock\\": ""
                },
                "exclude-from-classmap": [
                    "/Tests/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Nicolas Grekas",
                    "email": "p@tchwork.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Decouples applications from the system clock",
            "homepage": "https://symfony.com",
            "keywords": [
                "clock",
                "psr20",
                "time"
            ],
            "support": {
                "source": "https://github.com/symfony/clock/tree/v7.1.1"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2024-05-31T14:57:53+00:00"
        },
        {
            "name": "symfony/config",
            "version": "v7.1.1",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/config.git",
                "reference": "2210fc99fa42a259eb6c89d1f724ce0c4d62d5d2"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/config/zipball/2210fc99fa42a259eb6c89d1f724ce0c4d62d5d2",
                "reference": "2210fc99fa42a259eb6c89d1f724ce0c4d62d5d2",
                "shasum": ""
            },
            "require": {
                "php": ">=8.2",
                "symfony/deprecation-contracts": "^2.5|^3",
                "symfony/filesystem": "^7.1",
                "symfony/polyfill-ctype": "~1.8"
            },
            "conflict": {
                "symfony/finder": "<6.4",
                "symfony/service-contracts": "<2.5"
            },
            "require-dev": {
                "symfony/event-dispatcher": "^6.4|^7.0",
                "symfony/finder": "^6.4|^7.0",
                "symfony/messenger": "^6.4|^7.0",
                "symfony/service-contracts": "^2.5|^3",
                "symfony/yaml": "^6.4|^7.0"
            },
            "type": "library",
            "autoload": {
                "psr-4": {
                    "Symfony\\Component\\Config\\": ""
                },
                "exclude-from-classmap": [
                    "/Tests/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Fabien Potencier",
                    "email": "fabien@symfony.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Helps you find, load, combine, autofill and validate configuration values of any kind",
            "homepage": "https://symfony.com",
            "support": {
                "source": "https://github.com/symfony/config/tree/v7.1.1"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2024-05-31T14:57:53+00:00"
        },
        {
            "name": "symfony/console",
            "version": "v7.1.3",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/console.git",
                "reference": "cb1dcb30ebc7005c29864ee78adb47b5fb7c3cd9"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/console/zipball/cb1dcb30ebc7005c29864ee78adb47b5fb7c3cd9",
                "reference": "cb1dcb30ebc7005c29864ee78adb47b5fb7c3cd9",
                "shasum": ""
            },
            "require": {
                "php": ">=8.2",
                "symfony/polyfill-mbstring": "~1.0",
                "symfony/service-contracts": "^2.5|^3",
                "symfony/string": "^6.4|^7.0"
            },
            "conflict": {
                "symfony/dependency-injection": "<6.4",
                "symfony/dotenv": "<6.4",
                "symfony/event-dispatcher": "<6.4",
                "symfony/lock": "<6.4",
                "symfony/process": "<6.4"
            },
            "provide": {
                "psr/log-implementation": "1.0|2.0|3.0"
            },
            "require-dev": {
                "psr/log": "^1|^2|^3",
                "symfony/config": "^6.4|^7.0",
                "symfony/dependency-injection": "^6.4|^7.0",
                "symfony/event-dispatcher": "^6.4|^7.0",
                "symfony/http-foundation": "^6.4|^7.0",
                "symfony/http-kernel": "^6.4|^7.0",
                "symfony/lock": "^6.4|^7.0",
                "symfony/messenger": "^6.4|^7.0",
                "symfony/process": "^6.4|^7.0",
                "symfony/stopwatch": "^6.4|^7.0",
                "symfony/var-dumper": "^6.4|^7.0"
            },
            "type": "library",
            "autoload": {
                "psr-4": {
                    "Symfony\\Component\\Console\\": ""
                },
                "exclude-from-classmap": [
                    "/Tests/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Fabien Potencier",
                    "email": "fabien@symfony.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Eases the creation of beautiful and testable command line interfaces",
            "homepage": "https://symfony.com",
            "keywords": [
                "cli",
                "command-line",
                "console",
                "terminal"
            ],
            "support": {
                "source": "https://github.com/symfony/console/tree/v7.1.3"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2024-07-26T12:41:01+00:00"
        },
        {
            "name": "symfony/dependency-injection",
            "version": "v7.1.3",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/dependency-injection.git",
                "reference": "8126f0be4ff984e4db0140e60917900a53facb49"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/dependency-injection/zipball/8126f0be4ff984e4db0140e60917900a53facb49",
                "reference": "8126f0be4ff984e4db0140e60917900a53facb49",
                "shasum": ""
            },
            "require": {
                "php": ">=8.2",
                "psr/container": "^1.1|^2.0",
                "symfony/deprecation-contracts": "^2.5|^3",
                "symfony/service-contracts": "^3.5",
                "symfony/var-exporter": "^6.4|^7.0"
            },
            "conflict": {
                "ext-psr": "<1.1|>=2",
                "symfony/config": "<6.4",
                "symfony/finder": "<6.4",
                "symfony/yaml": "<6.4"
            },
            "provide": {
                "psr/container-implementation": "1.1|2.0",
                "symfony/service-implementation": "1.1|2.0|3.0"
            },
            "require-dev": {
                "symfony/config": "^6.4|^7.0",
                "symfony/expression-language": "^6.4|^7.0",
                "symfony/yaml": "^6.4|^7.0"
            },
            "type": "library",
            "autoload": {
                "psr-4": {
                    "Symfony\\Component\\DependencyInjection\\": ""
                },
                "exclude-from-classmap": [
                    "/Tests/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Fabien Potencier",
                    "email": "fabien@symfony.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Allows you to standardize and centralize the way objects are constructed in your application",
            "homepage": "https://symfony.com",
            "support": {
                "source": "https://github.com/symfony/dependency-injection/tree/v7.1.3"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2024-07-26T07:35:39+00:00"
        },
        {
            "name": "symfony/deprecation-contracts",
            "version": "v3.5.0",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/deprecation-contracts.git",
                "reference": "0e0d29ce1f20deffb4ab1b016a7257c4f1e789a1"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/deprecation-contracts/zipball/0e0d29ce1f20deffb4ab1b016a7257c4f1e789a1",
                "reference": "0e0d29ce1f20deffb4ab1b016a7257c4f1e789a1",
                "shasum": ""
            },
            "require": {
                "php": ">=8.1"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-main": "3.5-dev"
                },
                "thanks": {
                    "name": "symfony/contracts",
                    "url": "https://github.com/symfony/contracts"
                }
            },
            "autoload": {
                "files": [
                    "function.php"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Nicolas Grekas",
                    "email": "p@tchwork.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "A generic function and convention to trigger deprecation notices",
            "homepage": "https://symfony.com",
            "support": {
                "source": "https://github.com/symfony/deprecation-contracts/tree/v3.5.0"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2024-04-18T09:32:20+00:00"
        },
        {
            "name": "symfony/dotenv",
            "version": "v7.1.3",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/dotenv.git",
                "reference": "a26be30fd61678dab694a18a85084cea7673bbf3"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/dotenv/zipball/a26be30fd61678dab694a18a85084cea7673bbf3",
                "reference": "a26be30fd61678dab694a18a85084cea7673bbf3",
                "shasum": ""
            },
            "require": {
                "php": ">=8.2"
            },
            "conflict": {
                "symfony/console": "<6.4",
                "symfony/process": "<6.4"
            },
            "require-dev": {
                "symfony/console": "^6.4|^7.0",
                "symfony/process": "^6.4|^7.0"
            },
            "type": "library",
            "autoload": {
                "psr-4": {
                    "Symfony\\Component\\Dotenv\\": ""
                },
                "exclude-from-classmap": [
                    "/Tests/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Fabien Potencier",
                    "email": "fabien@symfony.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Registers environment variables from a .env file",
            "homepage": "https://symfony.com",
            "keywords": [
                "dotenv",
                "env",
                "environment"
            ],
            "support": {
                "source": "https://github.com/symfony/dotenv/tree/v7.1.3"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2024-07-09T19:36:07+00:00"
        },
        {
            "name": "symfony/error-handler",
            "version": "v7.1.3",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/error-handler.git",
                "reference": "432bb369952795c61ca1def65e078c4a80dad13c"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/error-handler/zipball/432bb369952795c61ca1def65e078c4a80dad13c",
                "reference": "432bb369952795c61ca1def65e078c4a80dad13c",
                "shasum": ""
            },
            "require": {
                "php": ">=8.2",
                "psr/log": "^1|^2|^3",
                "symfony/var-dumper": "^6.4|^7.0"
            },
            "conflict": {
                "symfony/deprecation-contracts": "<2.5",
                "symfony/http-kernel": "<6.4"
            },
            "require-dev": {
                "symfony/deprecation-contracts": "^2.5|^3",
                "symfony/http-kernel": "^6.4|^7.0",
                "symfony/serializer": "^6.4|^7.0"
            },
            "bin": [
                "Resources/bin/patch-type-declarations"
            ],
            "type": "library",
            "autoload": {
                "psr-4": {
                    "Symfony\\Component\\ErrorHandler\\": ""
                },
                "exclude-from-classmap": [
                    "/Tests/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Fabien Potencier",
                    "email": "fabien@symfony.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Provides tools to manage errors and ease debugging PHP code",
            "homepage": "https://symfony.com",
            "support": {
                "source": "https://github.com/symfony/error-handler/tree/v7.1.3"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2024-07-26T13:02:51+00:00"
        },
        {
            "name": "symfony/event-dispatcher",
            "version": "v7.1.1",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/event-dispatcher.git",
                "reference": "9fa7f7a21beb22a39a8f3f28618b29e50d7a55a7"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/event-dispatcher/zipball/9fa7f7a21beb22a39a8f3f28618b29e50d7a55a7",
                "reference": "9fa7f7a21beb22a39a8f3f28618b29e50d7a55a7",
                "shasum": ""
            },
            "require": {
                "php": ">=8.2",
                "symfony/event-dispatcher-contracts": "^2.5|^3"
            },
            "conflict": {
                "symfony/dependency-injection": "<6.4",
                "symfony/service-contracts": "<2.5"
            },
            "provide": {
                "psr/event-dispatcher-implementation": "1.0",
                "symfony/event-dispatcher-implementation": "2.0|3.0"
            },
            "require-dev": {
                "psr/log": "^1|^2|^3",
                "symfony/config": "^6.4|^7.0",
                "symfony/dependency-injection": "^6.4|^7.0",
                "symfony/error-handler": "^6.4|^7.0",
                "symfony/expression-language": "^6.4|^7.0",
                "symfony/http-foundation": "^6.4|^7.0",
                "symfony/service-contracts": "^2.5|^3",
                "symfony/stopwatch": "^6.4|^7.0"
            },
            "type": "library",
            "autoload": {
                "psr-4": {
                    "Symfony\\Component\\EventDispatcher\\": ""
                },
                "exclude-from-classmap": [
                    "/Tests/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Fabien Potencier",
                    "email": "fabien@symfony.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Provides tools that allow your application components to communicate with each other by dispatching events and listening to them",
            "homepage": "https://symfony.com",
            "support": {
                "source": "https://github.com/symfony/event-dispatcher/tree/v7.1.1"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2024-05-31T14:57:53+00:00"
        },
        {
            "name": "symfony/event-dispatcher-contracts",
            "version": "v3.5.0",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/event-dispatcher-contracts.git",
                "reference": "8f93aec25d41b72493c6ddff14e916177c9efc50"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/event-dispatcher-contracts/zipball/8f93aec25d41b72493c6ddff14e916177c9efc50",
                "reference": "8f93aec25d41b72493c6ddff14e916177c9efc50",
                "shasum": ""
            },
            "require": {
                "php": ">=8.1",
                "psr/event-dispatcher": "^1"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-main": "3.5-dev"
                },
                "thanks": {
                    "name": "symfony/contracts",
                    "url": "https://github.com/symfony/contracts"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Contracts\\EventDispatcher\\": ""
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Nicolas Grekas",
                    "email": "p@tchwork.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Generic abstractions related to dispatching event",
            "homepage": "https://symfony.com",
            "keywords": [
                "abstractions",
                "contracts",
                "decoupling",
                "interfaces",
                "interoperability",
                "standards"
            ],
            "support": {
                "source": "https://github.com/symfony/event-dispatcher-contracts/tree/v3.5.0"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2024-04-18T09:32:20+00:00"
        },
        {
            "name": "symfony/filesystem",
            "version": "v7.1.2",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/filesystem.git",
                "reference": "92a91985250c251de9b947a14bb2c9390b1a562c"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/filesystem/zipball/92a91985250c251de9b947a14bb2c9390b1a562c",
                "reference": "92a91985250c251de9b947a14bb2c9390b1a562c",
                "shasum": ""
            },
            "require": {
                "php": ">=8.2",
                "symfony/polyfill-ctype": "~1.8",
                "symfony/polyfill-mbstring": "~1.8"
            },
            "require-dev": {
                "symfony/process": "^6.4|^7.0"
            },
            "type": "library",
            "autoload": {
                "psr-4": {
                    "Symfony\\Component\\Filesystem\\": ""
                },
                "exclude-from-classmap": [
                    "/Tests/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Fabien Potencier",
                    "email": "fabien@symfony.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Provides basic utilities for the filesystem",
            "homepage": "https://symfony.com",
            "support": {
                "source": "https://github.com/symfony/filesystem/tree/v7.1.2"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2024-06-28T10:03:55+00:00"
        },
        {
            "name": "symfony/finder",
            "version": "v7.1.3",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/finder.git",
                "reference": "717c6329886f32dc65e27461f80f2a465412fdca"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/finder/zipball/717c6329886f32dc65e27461f80f2a465412fdca",
                "reference": "717c6329886f32dc65e27461f80f2a465412fdca",
                "shasum": ""
            },
            "require": {
                "php": ">=8.2"
            },
            "require-dev": {
                "symfony/filesystem": "^6.4|^7.0"
            },
            "type": "library",
            "autoload": {
                "psr-4": {
                    "Symfony\\Component\\Finder\\": ""
                },
                "exclude-from-classmap": [
                    "/Tests/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Fabien Potencier",
                    "email": "fabien@symfony.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Finds files and directories via an intuitive fluent interface",
            "homepage": "https://symfony.com",
            "support": {
                "source": "https://github.com/symfony/finder/tree/v7.1.3"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2024-07-24T07:08:44+00:00"
        },
        {
            "name": "symfony/framework-bundle",
            "version": "v7.1.3",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/framework-bundle.git",
                "reference": "a32ec544bd501eb4619eb977860ad3076ee55061"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/framework-bundle/zipball/a32ec544bd501eb4619eb977860ad3076ee55061",
                "reference": "a32ec544bd501eb4619eb977860ad3076ee55061",
                "shasum": ""
            },
            "require": {
                "composer-runtime-api": ">=2.1",
                "ext-xml": "*",
                "php": ">=8.2",
                "symfony/cache": "^6.4|^7.0",
                "symfony/config": "^6.4|^7.0",
                "symfony/dependency-injection": "^7.1",
                "symfony/deprecation-contracts": "^2.5|^3",
                "symfony/error-handler": "^6.4|^7.0",
                "symfony/event-dispatcher": "^6.4|^7.0",
                "symfony/filesystem": "^7.1",
                "symfony/finder": "^6.4|^7.0",
                "symfony/http-foundation": "^6.4|^7.0",
                "symfony/http-kernel": "^6.4|^7.0",
                "symfony/polyfill-mbstring": "~1.0",
                "symfony/routing": "^6.4|^7.0"
            },
            "conflict": {
                "doctrine/persistence": "<1.3",
                "phpdocumentor/reflection-docblock": "<3.2.2",
                "phpdocumentor/type-resolver": "<1.4.0",
                "symfony/asset": "<6.4",
                "symfony/asset-mapper": "<6.4",
                "symfony/clock": "<6.4",
                "symfony/console": "<6.4",
                "symfony/dom-crawler": "<6.4",
                "symfony/dotenv": "<6.4",
                "symfony/form": "<6.4",
                "symfony/http-client": "<6.4",
                "symfony/lock": "<6.4",
                "symfony/mailer": "<6.4",
                "symfony/messenger": "<6.4",
                "symfony/mime": "<6.4",
                "symfony/property-access": "<6.4",
                "symfony/property-info": "<6.4",
                "symfony/scheduler": "<6.4.4|>=7.0.0,<7.0.4",
                "symfony/security-core": "<6.4",
                "symfony/security-csrf": "<6.4",
                "symfony/serializer": "<6.4",
                "symfony/stopwatch": "<6.4",
                "symfony/translation": "<6.4",
                "symfony/twig-bridge": "<6.4",
                "symfony/twig-bundle": "<6.4",
                "symfony/validator": "<6.4",
                "symfony/web-profiler-bundle": "<6.4",
                "symfony/workflow": "<6.4"
            },
            "require-dev": {
                "doctrine/persistence": "^1.3|^2|^3",
                "dragonmantank/cron-expression": "^3.1",
                "phpdocumentor/reflection-docblock": "^3.0|^4.0|^5.0",
                "seld/jsonlint": "^1.10",
                "symfony/asset": "^6.4|^7.0",
                "symfony/asset-mapper": "^6.4|^7.0",
                "symfony/browser-kit": "^6.4|^7.0",
                "symfony/clock": "^6.4|^7.0",
                "symfony/console": "^6.4|^7.0",
                "symfony/css-selector": "^6.4|^7.0",
                "symfony/dom-crawler": "^6.4|^7.0",
                "symfony/dotenv": "^6.4|^7.0",
                "symfony/expression-language": "^6.4|^7.0",
                "symfony/form": "^6.4|^7.0",
                "symfony/html-sanitizer": "^6.4|^7.0",
                "symfony/http-client": "^6.4|^7.0",
                "symfony/lock": "^6.4|^7.0",
                "symfony/mailer": "^6.4|^7.0",
                "symfony/messenger": "^6.4|^7.0",
                "symfony/mime": "^6.4|^7.0",
                "symfony/notifier": "^6.4|^7.0",
                "symfony/polyfill-intl-icu": "~1.0",
                "symfony/process": "^6.4|^7.0",
                "symfony/property-info": "^6.4|^7.0",
                "symfony/rate-limiter": "^6.4|^7.0",
                "symfony/scheduler": "^6.4.4|^7.0.4",
                "symfony/security-bundle": "^6.4|^7.0",
                "symfony/semaphore": "^6.4|^7.0",
                "symfony/serializer": "^6.4|^7.0",
                "symfony/stopwatch": "^6.4|^7.0",
                "symfony/string": "^6.4|^7.0",
                "symfony/translation": "^6.4|^7.0",
                "symfony/twig-bundle": "^6.4|^7.0",
                "symfony/type-info": "^7.1",
                "symfony/uid": "^6.4|^7.0",
                "symfony/validator": "^6.4|^7.0",
                "symfony/web-link": "^6.4|^7.0",
                "symfony/workflow": "^6.4|^7.0",
                "symfony/yaml": "^6.4|^7.0",
                "twig/twig": "^3.0.4"
            },
            "type": "symfony-bundle",
            "autoload": {
                "psr-4": {
                    "Symfony\\Bundle\\FrameworkBundle\\": ""
                },
                "exclude-from-classmap": [
                    "/Tests/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Fabien Potencier",
                    "email": "fabien@symfony.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Provides a tight integration between Symfony components and the Symfony full-stack framework",
            "homepage": "https://symfony.com",
            "support": {
                "source": "https://github.com/symfony/framework-bundle/tree/v7.1.3"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2024-07-26T13:24:34+00:00"
        },
        {
            "name": "symfony/http-foundation",
            "version": "v7.1.3",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/http-foundation.git",
                "reference": "f602d5c17d1fa02f8019ace2687d9d136b7f4a1a"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/http-foundation/zipball/f602d5c17d1fa02f8019ace2687d9d136b7f4a1a",
                "reference": "f602d5c17d1fa02f8019ace2687d9d136b7f4a1a",
                "shasum": ""
            },
            "require": {
                "php": ">=8.2",
                "symfony/polyfill-mbstring": "~1.1",
                "symfony/polyfill-php83": "^1.27"
            },
            "conflict": {
                "doctrine/dbal": "<3.6",
                "symfony/cache": "<6.4"
            },
            "require-dev": {
                "doctrine/dbal": "^3.6|^4",
                "predis/predis": "^1.1|^2.0",
                "symfony/cache": "^6.4|^7.0",
                "symfony/dependency-injection": "^6.4|^7.0",
                "symfony/expression-language": "^6.4|^7.0",
                "symfony/http-kernel": "^6.4|^7.0",
                "symfony/mime": "^6.4|^7.0",
                "symfony/rate-limiter": "^6.4|^7.0"
            },
            "type": "library",
            "autoload": {
                "psr-4": {
                    "Symfony\\Component\\HttpFoundation\\": ""
                },
                "exclude-from-classmap": [
                    "/Tests/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Fabien Potencier",
                    "email": "fabien@symfony.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Defines an object-oriented layer for the HTTP specification",
            "homepage": "https://symfony.com",
            "support": {
                "source": "https://github.com/symfony/http-foundation/tree/v7.1.3"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2024-07-26T12:41:01+00:00"
        },
        {
            "name": "symfony/http-kernel",
            "version": "v7.1.3",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/http-kernel.git",
                "reference": "db9702f3a04cc471ec8c70e881825db26ac5f186"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/http-kernel/zipball/db9702f3a04cc471ec8c70e881825db26ac5f186",
                "reference": "db9702f3a04cc471ec8c70e881825db26ac5f186",
                "shasum": ""
            },
            "require": {
                "php": ">=8.2",
                "psr/log": "^1|^2|^3",
                "symfony/deprecation-contracts": "^2.5|^3",
                "symfony/error-handler": "^6.4|^7.0",
                "symfony/event-dispatcher": "^6.4|^7.0",
                "symfony/http-foundation": "^6.4|^7.0",
                "symfony/polyfill-ctype": "^1.8"
            },
            "conflict": {
                "symfony/browser-kit": "<6.4",
                "symfony/cache": "<6.4",
                "symfony/config": "<6.4",
                "symfony/console": "<6.4",
                "symfony/dependency-injection": "<6.4",
                "symfony/doctrine-bridge": "<6.4",
                "symfony/form": "<6.4",
                "symfony/http-client": "<6.4",
                "symfony/http-client-contracts": "<2.5",
                "symfony/mailer": "<6.4",
                "symfony/messenger": "<6.4",
                "symfony/translation": "<6.4",
                "symfony/translation-contracts": "<2.5",
                "symfony/twig-bridge": "<6.4",
                "symfony/validator": "<6.4",
                "symfony/var-dumper": "<6.4",
                "twig/twig": "<3.0.4"
            },
            "provide": {
                "psr/log-implementation": "1.0|2.0|3.0"
            },
            "require-dev": {
                "psr/cache": "^1.0|^2.0|^3.0",
                "symfony/browser-kit": "^6.4|^7.0",
                "symfony/clock": "^6.4|^7.0",
                "symfony/config": "^6.4|^7.0",
                "symfony/console": "^6.4|^7.0",
                "symfony/css-selector": "^6.4|^7.0",
                "symfony/dependency-injection": "^6.4|^7.0",
                "symfony/dom-crawler": "^6.4|^7.0",
                "symfony/expression-language": "^6.4|^7.0",
                "symfony/finder": "^6.4|^7.0",
                "symfony/http-client-contracts": "^2.5|^3",
                "symfony/process": "^6.4|^7.0",
                "symfony/property-access": "^7.1",
                "symfony/routing": "^6.4|^7.0",
                "symfony/serializer": "^7.1",
                "symfony/stopwatch": "^6.4|^7.0",
                "symfony/translation": "^6.4|^7.0",
                "symfony/translation-contracts": "^2.5|^3",
                "symfony/uid": "^6.4|^7.0",
                "symfony/validator": "^6.4|^7.0",
                "symfony/var-dumper": "^6.4|^7.0",
                "symfony/var-exporter": "^6.4|^7.0",
                "twig/twig": "^3.0.4"
            },
            "type": "library",
            "autoload": {
                "psr-4": {
                    "Symfony\\Component\\HttpKernel\\": ""
                },
                "exclude-from-classmap": [
                    "/Tests/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Fabien Potencier",
                    "email": "fabien@symfony.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Provides a structured process for converting a Request into a Response",
            "homepage": "https://symfony.com",
            "support": {
                "source": "https://github.com/symfony/http-kernel/tree/v7.1.3"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2024-07-26T14:58:15+00:00"
        },
        {
            "name": "symfony/messenger",
            "version": "v7.1.3",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/messenger.git",
                "reference": "604e182a7758ceea35921a8ad5dd492a6e13bae4"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/messenger/zipball/604e182a7758ceea35921a8ad5dd492a6e13bae4",
                "reference": "604e182a7758ceea35921a8ad5dd492a6e13bae4",
                "shasum": ""
            },
            "require": {
                "php": ">=8.2",
                "psr/log": "^1|^2|^3",
                "symfony/clock": "^6.4|^7.0"
            },
            "conflict": {
                "symfony/console": "<6.4",
                "symfony/event-dispatcher": "<6.4",
                "symfony/event-dispatcher-contracts": "<2.5",
                "symfony/framework-bundle": "<6.4",
                "symfony/http-kernel": "<6.4",
                "symfony/serializer": "<6.4"
            },
            "require-dev": {
                "psr/cache": "^1.0|^2.0|^3.0",
                "symfony/console": "^6.4|^7.0",
                "symfony/dependency-injection": "^6.4|^7.0",
                "symfony/event-dispatcher": "^6.4|^7.0",
                "symfony/http-kernel": "^6.4|^7.0",
                "symfony/process": "^6.4|^7.0",
                "symfony/property-access": "^6.4|^7.0",
                "symfony/rate-limiter": "^6.4|^7.0",
                "symfony/routing": "^6.4|^7.0",
                "symfony/serializer": "^6.4|^7.0",
                "symfony/service-contracts": "^2.5|^3",
                "symfony/stopwatch": "^6.4|^7.0",
                "symfony/validator": "^6.4|^7.0"
            },
            "type": "library",
            "autoload": {
                "psr-4": {
                    "Symfony\\Component\\Messenger\\": ""
                },
                "exclude-from-classmap": [
                    "/Tests/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Samuel Roze",
                    "email": "samuel.roze@gmail.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Helps applications send and receive messages to/from other applications or via message queues",
            "homepage": "https://symfony.com",
            "support": {
                "source": "https://github.com/symfony/messenger/tree/v7.1.3"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2024-07-09T19:36:07+00:00"
        },
        {
            "name": "symfony/polyfill-ctype",
            "version": "v1.30.0",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/polyfill-ctype.git",
                "reference": "0424dff1c58f028c451efff2045f5d92410bd540"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/polyfill-ctype/zipball/0424dff1c58f028c451efff2045f5d92410bd540",
                "reference": "0424dff1c58f028c451efff2045f5d92410bd540",
                "shasum": ""
            },
            "require": {
                "php": ">=7.1"
            },
            "provide": {
                "ext-ctype": "*"
            },
            "suggest": {
                "ext-ctype": "For best performance"
            },
            "type": "library",
            "extra": {
                "thanks": {
                    "name": "symfony/polyfill",
                    "url": "https://github.com/symfony/polyfill"
                }
            },
            "autoload": {
                "files": [
                    "bootstrap.php"
                ],
                "psr-4": {
                    "Symfony\\Polyfill\\Ctype\\": ""
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Gert de Pagter",
                    "email": "BackEndTea@gmail.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Symfony polyfill for ctype functions",
            "homepage": "https://symfony.com",
            "keywords": [
                "compatibility",
                "ctype",
                "polyfill",
                "portable"
            ],
            "support": {
                "source": "https://github.com/symfony/polyfill-ctype/tree/v1.30.0"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2024-05-31T15:07:36+00:00"
        },
        {
            "name": "symfony/polyfill-intl-grapheme",
            "version": "v1.30.0",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/polyfill-intl-grapheme.git",
                "reference": "64647a7c30b2283f5d49b874d84a18fc22054b7a"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/polyfill-intl-grapheme/zipball/64647a7c30b2283f5d49b874d84a18fc22054b7a",
                "reference": "64647a7c30b2283f5d49b874d84a18fc22054b7a",
                "shasum": ""
            },
            "require": {
                "php": ">=7.1"
            },
            "suggest": {
                "ext-intl": "For best performance"
            },
            "type": "library",
            "extra": {
                "thanks": {
                    "name": "symfony/polyfill",
                    "url": "https://github.com/symfony/polyfill"
                }
            },
            "autoload": {
                "files": [
                    "bootstrap.php"
                ],
                "psr-4": {
                    "Symfony\\Polyfill\\Intl\\Grapheme\\": ""
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Nicolas Grekas",
                    "email": "p@tchwork.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Symfony polyfill for intl's grapheme_* functions",
            "homepage": "https://symfony.com",
            "keywords": [
                "compatibility",
                "grapheme",
                "intl",
                "polyfill",
                "portable",
                "shim"
            ],
            "support": {
                "source": "https://github.com/symfony/polyfill-intl-grapheme/tree/v1.30.0"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2024-05-31T15:07:36+00:00"
        },
        {
            "name": "symfony/polyfill-intl-normalizer",
            "version": "v1.30.0",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/polyfill-intl-normalizer.git",
                "reference": "a95281b0be0d9ab48050ebd988b967875cdb9fdb"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/polyfill-intl-normalizer/zipball/a95281b0be0d9ab48050ebd988b967875cdb9fdb",
                "reference": "a95281b0be0d9ab48050ebd988b967875cdb9fdb",
                "shasum": ""
            },
            "require": {
                "php": ">=7.1"
            },
            "suggest": {
                "ext-intl": "For best performance"
            },
            "type": "library",
            "extra": {
                "thanks": {
                    "name": "symfony/polyfill",
                    "url": "https://github.com/symfony/polyfill"
                }
            },
            "autoload": {
                "files": [
                    "bootstrap.php"
                ],
                "psr-4": {
                    "Symfony\\Polyfill\\Intl\\Normalizer\\": ""
                },
                "classmap": [
                    "Resources/stubs"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Nicolas Grekas",
                    "email": "p@tchwork.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Symfony polyfill for intl's Normalizer class and related functions",
            "homepage": "https://symfony.com",
            "keywords": [
                "compatibility",
                "intl",
                "normalizer",
                "polyfill",
                "portable",
                "shim"
            ],
            "support": {
                "source": "https://github.com/symfony/polyfill-intl-normalizer/tree/v1.30.0"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2024-05-31T15:07:36+00:00"
        },
        {
            "name": "symfony/polyfill-mbstring",
            "version": "v1.30.0",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/polyfill-mbstring.git",
                "reference": "fd22ab50000ef01661e2a31d850ebaa297f8e03c"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/polyfill-mbstring/zipball/fd22ab50000ef01661e2a31d850ebaa297f8e03c",
                "reference": "fd22ab50000ef01661e2a31d850ebaa297f8e03c",
                "shasum": ""
            },
            "require": {
                "php": ">=7.1"
            },
            "provide": {
                "ext-mbstring": "*"
            },
            "suggest": {
                "ext-mbstring": "For best performance"
            },
            "type": "library",
            "extra": {
                "thanks": {
                    "name": "symfony/polyfill",
                    "url": "https://github.com/symfony/polyfill"
                }
            },
            "autoload": {
                "files": [
                    "bootstrap.php"
                ],
                "psr-4": {
                    "Symfony\\Polyfill\\Mbstring\\": ""
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Nicolas Grekas",
                    "email": "p@tchwork.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Symfony polyfill for the Mbstring extension",
            "homepage": "https://symfony.com",
            "keywords": [
                "compatibility",
                "mbstring",
                "polyfill",
                "portable",
                "shim"
            ],
            "support": {
                "source": "https://github.com/symfony/polyfill-mbstring/tree/v1.30.0"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2024-06-19T12:30:46+00:00"
        },
        {
            "name": "symfony/polyfill-php72",
            "version": "v1.30.0",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/polyfill-php72.git",
                "reference": "10112722600777e02d2745716b70c5db4ca70442"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/polyfill-php72/zipball/10112722600777e02d2745716b70c5db4ca70442",
                "reference": "10112722600777e02d2745716b70c5db4ca70442",
                "shasum": ""
            },
            "require": {
                "php": ">=7.1"
            },
            "type": "library",
            "extra": {
                "thanks": {
                    "name": "symfony/polyfill",
                    "url": "https://github.com/symfony/polyfill"
                }
            },
            "autoload": {
                "files": [
                    "bootstrap.php"
                ],
                "psr-4": {
                    "Symfony\\Polyfill\\Php72\\": ""
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Nicolas Grekas",
                    "email": "p@tchwork.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Symfony polyfill backporting some PHP 7.2+ features to lower PHP versions",
            "homepage": "https://symfony.com",
            "keywords": [
                "compatibility",
                "polyfill",
                "portable",
                "shim"
            ],
            "support": {
                "source": "https://github.com/symfony/polyfill-php72/tree/v1.30.0"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2024-06-19T12:30:46+00:00"
        },
        {
            "name": "symfony/polyfill-php80",
            "version": "v1.30.0",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/polyfill-php80.git",
                "reference": "77fa7995ac1b21ab60769b7323d600a991a90433"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/polyfill-php80/zipball/77fa7995ac1b21ab60769b7323d600a991a90433",
                "reference": "77fa7995ac1b21ab60769b7323d600a991a90433",
                "shasum": ""
            },
            "require": {
                "php": ">=7.1"
            },
            "type": "library",
            "extra": {
                "thanks": {
                    "name": "symfony/polyfill",
                    "url": "https://github.com/symfony/polyfill"
                }
            },
            "autoload": {
                "files": [
                    "bootstrap.php"
                ],
                "psr-4": {
                    "Symfony\\Polyfill\\Php80\\": ""
                },
                "classmap": [
                    "Resources/stubs"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Ion Bazan",
                    "email": "ion.bazan@gmail.com"
                },
                {
                    "name": "Nicolas Grekas",
                    "email": "p@tchwork.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Symfony polyfill backporting some PHP 8.0+ features to lower PHP versions",
            "homepage": "https://symfony.com",
            "keywords": [
                "compatibility",
                "polyfill",
                "portable",
                "shim"
            ],
            "support": {
                "source": "https://github.com/symfony/polyfill-php80/tree/v1.30.0"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2024-05-31T15:07:36+00:00"
        },
        {
            "name": "symfony/polyfill-php83",
            "version": "v1.30.0",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/polyfill-php83.git",
                "reference": "dbdcdf1a4dcc2743591f1079d0c35ab1e2dcbbc9"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/polyfill-php83/zipball/dbdcdf1a4dcc2743591f1079d0c35ab1e2dcbbc9",
                "reference": "dbdcdf1a4dcc2743591f1079d0c35ab1e2dcbbc9",
                "shasum": ""
            },
            "require": {
                "php": ">=7.1"
            },
            "type": "library",
            "extra": {
                "thanks": {
                    "name": "symfony/polyfill",
                    "url": "https://github.com/symfony/polyfill"
                }
            },
            "autoload": {
                "files": [
                    "bootstrap.php"
                ],
                "psr-4": {
                    "Symfony\\Polyfill\\Php83\\": ""
                },
                "classmap": [
                    "Resources/stubs"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Nicolas Grekas",
                    "email": "p@tchwork.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Symfony polyfill backporting some PHP 8.3+ features to lower PHP versions",
            "homepage": "https://symfony.com",
            "keywords": [
                "compatibility",
                "polyfill",
                "portable",
                "shim"
            ],
            "support": {
                "source": "https://github.com/symfony/polyfill-php83/tree/v1.30.0"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2024-06-19T12:35:24+00:00"
        },
        {
            "name": "symfony/routing",
            "version": "v7.1.3",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/routing.git",
                "reference": "8a908a3f22d5a1b5d297578c2ceb41b02fa916d0"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/routing/zipball/8a908a3f22d5a1b5d297578c2ceb41b02fa916d0",
                "reference": "8a908a3f22d5a1b5d297578c2ceb41b02fa916d0",
                "shasum": ""
            },
            "require": {
                "php": ">=8.2",
                "symfony/deprecation-contracts": "^2.5|^3"
            },
            "conflict": {
                "symfony/config": "<6.4",
                "symfony/dependency-injection": "<6.4",
                "symfony/yaml": "<6.4"
            },
            "require-dev": {
                "psr/log": "^1|^2|^3",
                "symfony/config": "^6.4|^7.0",
                "symfony/dependency-injection": "^6.4|^7.0",
                "symfony/expression-language": "^6.4|^7.0",
                "symfony/http-foundation": "^6.4|^7.0",
                "symfony/yaml": "^6.4|^7.0"
            },
            "type": "library",
            "autoload": {
                "psr-4": {
                    "Symfony\\Component\\Routing\\": ""
                },
                "exclude-from-classmap": [
                    "/Tests/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Fabien Potencier",
                    "email": "fabien@symfony.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Maps an HTTP request to a set of configuration variables",
            "homepage": "https://symfony.com",
            "keywords": [
                "router",
                "routing",
                "uri",
                "url"
            ],
            "support": {
                "source": "https://github.com/symfony/routing/tree/v7.1.3"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2024-07-17T06:10:24+00:00"
        },
        {
            "name": "symfony/service-contracts",
            "version": "v3.5.0",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/service-contracts.git",
                "reference": "bd1d9e59a81d8fa4acdcea3f617c581f7475a80f"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/service-contracts/zipball/bd1d9e59a81d8fa4acdcea3f617c581f7475a80f",
                "reference": "bd1d9e59a81d8fa4acdcea3f617c581f7475a80f",
                "shasum": ""
            },
            "require": {
                "php": ">=8.1",
                "psr/container": "^1.1|^2.0",
                "symfony/deprecation-contracts": "^2.5|^3"
            },
            "conflict": {
                "ext-psr": "<1.1|>=2"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-main": "3.5-dev"
                },
                "thanks": {
                    "name": "symfony/contracts",
                    "url": "https://github.com/symfony/contracts"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Contracts\\Service\\": ""
                },
                "exclude-from-classmap": [
                    "/Test/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Nicolas Grekas",
                    "email": "p@tchwork.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Generic abstractions related to writing services",
            "homepage": "https://symfony.com",
            "keywords": [
                "abstractions",
                "contracts",
                "decoupling",
                "interfaces",
                "interoperability",
                "standards"
            ],
            "support": {
                "source": "https://github.com/symfony/service-contracts/tree/v3.5.0"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2024-04-18T09:32:20+00:00"
        },
        {
            "name": "symfony/string",
            "version": "v7.1.3",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/string.git",
                "reference": "ea272a882be7f20cad58d5d78c215001617b7f07"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/string/zipball/ea272a882be7f20cad58d5d78c215001617b7f07",
                "reference": "ea272a882be7f20cad58d5d78c215001617b7f07",
                "shasum": ""
            },
            "require": {
                "php": ">=8.2",
                "symfony/polyfill-ctype": "~1.8",
                "symfony/polyfill-intl-grapheme": "~1.0",
                "symfony/polyfill-intl-normalizer": "~1.0",
                "symfony/polyfill-mbstring": "~1.0"
            },
            "conflict": {
                "symfony/translation-contracts": "<2.5"
            },
            "require-dev": {
                "symfony/emoji": "^7.1",
                "symfony/error-handler": "^6.4|^7.0",
                "symfony/http-client": "^6.4|^7.0",
                "symfony/intl": "^6.4|^7.0",
                "symfony/translation-contracts": "^2.5|^3.0",
                "symfony/var-exporter": "^6.4|^7.0"
            },
            "type": "library",
            "autoload": {
                "files": [
                    "Resources/functions.php"
                ],
                "psr-4": {
                    "Symfony\\Component\\String\\": ""
                },
                "exclude-from-classmap": [
                    "/Tests/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Nicolas Grekas",
                    "email": "p@tchwork.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Provides an object-oriented API to strings and deals with bytes, UTF-8 code points and grapheme clusters in a unified way",
            "homepage": "https://symfony.com",
            "keywords": [
                "grapheme",
                "i18n",
                "string",
                "unicode",
                "utf-8",
                "utf8"
            ],
            "support": {
                "source": "https://github.com/symfony/string/tree/v7.1.3"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2024-07-22T10:25:37+00:00"
        },
        {
            "name": "symfony/translation-contracts",
            "version": "v3.5.0",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/translation-contracts.git",
                "reference": "b9d2189887bb6b2e0367a9fc7136c5239ab9b05a"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/translation-contracts/zipball/b9d2189887bb6b2e0367a9fc7136c5239ab9b05a",
                "reference": "b9d2189887bb6b2e0367a9fc7136c5239ab9b05a",
                "shasum": ""
            },
            "require": {
                "php": ">=8.1"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-main": "3.5-dev"
                },
                "thanks": {
                    "name": "symfony/contracts",
                    "url": "https://github.com/symfony/contracts"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Contracts\\Translation\\": ""
                },
                "exclude-from-classmap": [
                    "/Test/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Nicolas Grekas",
                    "email": "p@tchwork.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Generic abstractions related to translation",
            "homepage": "https://symfony.com",
            "keywords": [
                "abstractions",
                "contracts",
                "decoupling",
                "interfaces",
                "interoperability",
                "standards"
            ],
            "support": {
                "source": "https://github.com/symfony/translation-contracts/tree/v3.5.0"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2024-04-18T09:32:20+00:00"
        },
        {
            "name": "symfony/twig-bridge",
            "version": "v7.1.1",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/twig-bridge.git",
                "reference": "96e6e12a63db80bcedefc012042d2cb2d1a015f8"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/twig-bridge/zipball/96e6e12a63db80bcedefc012042d2cb2d1a015f8",
                "reference": "96e6e12a63db80bcedefc012042d2cb2d1a015f8",
                "shasum": ""
            },
            "require": {
                "php": ">=8.2",
                "symfony/translation-contracts": "^2.5|^3",
                "twig/twig": "^3.9"
            },
            "conflict": {
                "phpdocumentor/reflection-docblock": "<3.2.2",
                "phpdocumentor/type-resolver": "<1.4.0",
                "symfony/console": "<6.4",
                "symfony/form": "<6.4",
                "symfony/http-foundation": "<6.4",
                "symfony/http-kernel": "<6.4",
                "symfony/mime": "<6.4",
                "symfony/serializer": "<6.4",
                "symfony/translation": "<6.4",
                "symfony/workflow": "<6.4"
            },
            "require-dev": {
                "egulias/email-validator": "^2.1.10|^3|^4",
                "league/html-to-markdown": "^5.0",
                "phpdocumentor/reflection-docblock": "^3.0|^4.0|^5.0",
                "symfony/asset": "^6.4|^7.0",
                "symfony/asset-mapper": "^6.4|^7.0",
                "symfony/console": "^6.4|^7.0",
                "symfony/dependency-injection": "^6.4|^7.0",
                "symfony/emoji": "^7.1",
                "symfony/expression-language": "^6.4|^7.0",
                "symfony/finder": "^6.4|^7.0",
                "symfony/form": "^6.4|^7.0",
                "symfony/html-sanitizer": "^6.4|^7.0",
                "symfony/http-foundation": "^6.4|^7.0",
                "symfony/http-kernel": "^6.4|^7.0",
                "symfony/intl": "^6.4|^7.0",
                "symfony/mime": "^6.4|^7.0",
                "symfony/polyfill-intl-icu": "~1.0",
                "symfony/property-info": "^6.4|^7.0",
                "symfony/routing": "^6.4|^7.0",
                "symfony/security-acl": "^2.8|^3.0",
                "symfony/security-core": "^6.4|^7.0",
                "symfony/security-csrf": "^6.4|^7.0",
                "symfony/security-http": "^6.4|^7.0",
                "symfony/serializer": "^6.4.3|^7.0.3",
                "symfony/stopwatch": "^6.4|^7.0",
                "symfony/translation": "^6.4|^7.0",
                "symfony/web-link": "^6.4|^7.0",
                "symfony/workflow": "^6.4|^7.0",
                "symfony/yaml": "^6.4|^7.0",
                "twig/cssinliner-extra": "^2.12|^3",
                "twig/inky-extra": "^2.12|^3",
                "twig/markdown-extra": "^2.12|^3"
            },
            "type": "symfony-bridge",
            "autoload": {
                "psr-4": {
                    "Symfony\\Bridge\\Twig\\": ""
                },
                "exclude-from-classmap": [
                    "/Tests/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Fabien Potencier",
                    "email": "fabien@symfony.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Provides integration for Twig with various Symfony components",
            "homepage": "https://symfony.com",
            "support": {
                "source": "https://github.com/symfony/twig-bridge/tree/v7.1.1"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2024-05-31T14:57:53+00:00"
        },
        {
            "name": "symfony/twig-bundle",
            "version": "v7.1.1",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/twig-bundle.git",
                "reference": "d48c2f08c2f315e749f0e18fc4945b7be8afe1e5"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/twig-bundle/zipball/d48c2f08c2f315e749f0e18fc4945b7be8afe1e5",
                "reference": "d48c2f08c2f315e749f0e18fc4945b7be8afe1e5",
                "shasum": ""
            },
            "require": {
                "composer-runtime-api": ">=2.1",
                "php": ">=8.2",
                "symfony/config": "^6.4|^7.0",
                "symfony/dependency-injection": "^6.4|^7.0",
                "symfony/http-foundation": "^6.4|^7.0",
                "symfony/http-kernel": "^6.4|^7.0",
                "symfony/twig-bridge": "^6.4|^7.0",
                "twig/twig": "^3.0.4"
            },
            "conflict": {
                "symfony/framework-bundle": "<6.4",
                "symfony/translation": "<6.4"
            },
            "require-dev": {
                "symfony/asset": "^6.4|^7.0",
                "symfony/expression-language": "^6.4|^7.0",
                "symfony/finder": "^6.4|^7.0",
                "symfony/form": "^6.4|^7.0",
                "symfony/framework-bundle": "^6.4|^7.0",
                "symfony/routing": "^6.4|^7.0",
                "symfony/stopwatch": "^6.4|^7.0",
                "symfony/translation": "^6.4|^7.0",
                "symfony/web-link": "^6.4|^7.0",
                "symfony/yaml": "^6.4|^7.0"
            },
            "type": "symfony-bundle",
            "autoload": {
                "psr-4": {
                    "Symfony\\Bundle\\TwigBundle\\": ""
                },
                "exclude-from-classmap": [
                    "/Tests/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Fabien Potencier",
                    "email": "fabien@symfony.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Provides a tight integration of Twig into the Symfony full-stack framework",
            "homepage": "https://symfony.com",
            "support": {
                "source": "https://github.com/symfony/twig-bundle/tree/v7.1.1"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2024-05-31T14:57:53+00:00"
        },
        {
            "name": "symfony/validator",
            "version": "v7.1.3",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/validator.git",
                "reference": "ba711a6cfc008544dad059abb3c1d997f1472237"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/validator/zipball/ba711a6cfc008544dad059abb3c1d997f1472237",
                "reference": "ba711a6cfc008544dad059abb3c1d997f1472237",
                "shasum": ""
            },
            "require": {
                "php": ">=8.2",
                "symfony/deprecation-contracts": "^2.5|^3",
                "symfony/polyfill-ctype": "~1.8",
                "symfony/polyfill-mbstring": "~1.0",
                "symfony/polyfill-php83": "^1.27",
                "symfony/translation-contracts": "^2.5|^3"
            },
            "conflict": {
                "doctrine/lexer": "<1.1",
                "symfony/dependency-injection": "<6.4",
                "symfony/doctrine-bridge": "<7.0",
                "symfony/expression-language": "<6.4",
                "symfony/http-kernel": "<6.4",
                "symfony/intl": "<6.4",
                "symfony/property-info": "<6.4",
                "symfony/translation": "<6.4.3|>=7.0,<7.0.3",
                "symfony/yaml": "<6.4"
            },
            "require-dev": {
                "egulias/email-validator": "^2.1.10|^3|^4",
                "symfony/cache": "^6.4|^7.0",
                "symfony/config": "^6.4|^7.0",
                "symfony/console": "^6.4|^7.0",
                "symfony/dependency-injection": "^6.4|^7.0",
                "symfony/expression-language": "^6.4|^7.0",
                "symfony/finder": "^6.4|^7.0",
                "symfony/http-client": "^6.4|^7.0",
                "symfony/http-foundation": "^6.4|^7.0",
                "symfony/http-kernel": "^6.4|^7.0",
                "symfony/intl": "^6.4|^7.0",
                "symfony/mime": "^6.4|^7.0",
                "symfony/property-access": "^6.4|^7.0",
                "symfony/property-info": "^6.4|^7.0",
                "symfony/translation": "^6.4.3|^7.0.3",
                "symfony/type-info": "^7.1",
                "symfony/yaml": "^6.4|^7.0"
            },
            "type": "library",
            "autoload": {
                "psr-4": {
                    "Symfony\\Component\\Validator\\": ""
                },
                "exclude-from-classmap": [
                    "/Tests/",
                    "/Resources/bin/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Fabien Potencier",
                    "email": "fabien@symfony.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Provides tools to validate values",
            "homepage": "https://symfony.com",
            "support": {
                "source": "https://github.com/symfony/validator/tree/v7.1.3"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2024-07-26T12:41:01+00:00"
        },
        {
            "name": "symfony/var-dumper",
            "version": "v7.1.3",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/var-dumper.git",
                "reference": "86af4617cca75a6e28598f49ae0690f3b9d4591f"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/var-dumper/zipball/86af4617cca75a6e28598f49ae0690f3b9d4591f",
                "reference": "86af4617cca75a6e28598f49ae0690f3b9d4591f",
                "shasum": ""
            },
            "require": {
                "php": ">=8.2",
                "symfony/polyfill-mbstring": "~1.0"
            },
            "conflict": {
                "symfony/console": "<6.4"
            },
            "require-dev": {
                "ext-iconv": "*",
                "symfony/console": "^6.4|^7.0",
                "symfony/http-kernel": "^6.4|^7.0",
                "symfony/process": "^6.4|^7.0",
                "symfony/uid": "^6.4|^7.0",
                "twig/twig": "^3.0.4"
            },
            "bin": [
                "Resources/bin/var-dump-server"
            ],
            "type": "library",
            "autoload": {
                "files": [
                    "Resources/functions/dump.php"
                ],
                "psr-4": {
                    "Symfony\\Component\\VarDumper\\": ""
                },
                "exclude-from-classmap": [
                    "/Tests/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Nicolas Grekas",
                    "email": "p@tchwork.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Provides mechanisms for walking through any arbitrary PHP variable",
            "homepage": "https://symfony.com",
            "keywords": [
                "debug",
                "dump"
            ],
            "support": {
                "source": "https://github.com/symfony/var-dumper/tree/v7.1.3"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2024-07-26T12:41:01+00:00"
        },
        {
            "name": "symfony/var-exporter",
            "version": "v7.1.2",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/var-exporter.git",
                "reference": "b80a669a2264609f07f1667f891dbfca25eba44c"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/var-exporter/zipball/b80a669a2264609f07f1667f891dbfca25eba44c",
                "reference": "b80a669a2264609f07f1667f891dbfca25eba44c",
                "shasum": ""
            },
            "require": {
                "php": ">=8.2"
            },
            "require-dev": {
                "symfony/property-access": "^6.4|^7.0",
                "symfony/serializer": "^6.4|^7.0",
                "symfony/var-dumper": "^6.4|^7.0"
            },
            "type": "library",
            "autoload": {
                "psr-4": {
                    "Symfony\\Component\\VarExporter\\": ""
                },
                "exclude-from-classmap": [
                    "/Tests/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Nicolas Grekas",
                    "email": "p@tchwork.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Allows exporting any serializable PHP data structure to plain PHP code",
            "homepage": "https://symfony.com",
            "keywords": [
                "clone",
                "construct",
                "export",
                "hydrate",
                "instantiate",
                "lazy-loading",
                "proxy",
                "serialize"
            ],
            "support": {
                "source": "https://github.com/symfony/var-exporter/tree/v7.1.2"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2024-06-28T08:00:31+00:00"
        },
        {
            "name": "symfony/yaml",
            "version": "v7.1.1",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/yaml.git",
                "reference": "fa34c77015aa6720469db7003567b9f772492bf2"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/yaml/zipball/fa34c77015aa6720469db7003567b9f772492bf2",
                "reference": "fa34c77015aa6720469db7003567b9f772492bf2",
                "shasum": ""
            },
            "require": {
                "php": ">=8.2",
                "symfony/polyfill-ctype": "^1.8"
            },
            "conflict": {
                "symfony/console": "<6.4"
            },
            "require-dev": {
                "symfony/console": "^6.4|^7.0"
            },
            "bin": [
                "Resources/bin/yaml-lint"
            ],
            "type": "library",
            "autoload": {
                "psr-4": {
                    "Symfony\\Component\\Yaml\\": ""
                },
                "exclude-from-classmap": [
                    "/Tests/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Fabien Potencier",
                    "email": "fabien@symfony.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Loads and dumps YAML files",
            "homepage": "https://symfony.com",
            "support": {
                "source": "https://github.com/symfony/yaml/tree/v7.1.1"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2024-05-31T14:57:53+00:00"
        },
        {
            "name": "twig/twig",
            "version": "v3.10.3",
            "source": {
                "type": "git",
                "url": "https://github.com/twigphp/Twig.git",
                "reference": "67f29781ffafa520b0bbfbd8384674b42db04572"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/twigphp/Twig/zipball/67f29781ffafa520b0bbfbd8384674b42db04572",
                "reference": "67f29781ffafa520b0bbfbd8384674b42db04572",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2.5",
                "symfony/deprecation-contracts": "^2.5|^3",
                "symfony/polyfill-ctype": "^1.8",
                "symfony/polyfill-mbstring": "^1.3",
                "symfony/polyfill-php80": "^1.22"
            },
            "require-dev": {
                "psr/container": "^1.0|^2.0",
                "symfony/phpunit-bridge": "^5.4.9|^6.4|^7.0"
            },
            "type": "library",
            "autoload": {
                "files": [
                    "src/Resources/core.php",
                    "src/Resources/debug.php",
                    "src/Resources/escaper.php",
                    "src/Resources/string_loader.php"
                ],
                "psr-4": {
                    "Twig\\": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause"
            ],
            "authors": [
                {
                    "name": "Fabien Potencier",
                    "email": "fabien@symfony.com",
                    "homepage": "http://fabien.potencier.org",
                    "role": "Lead Developer"
                },
                {
                    "name": "Twig Team",
                    "role": "Contributors"
                },
                {
                    "name": "Armin Ronacher",
                    "email": "armin.ronacher@active-4.com",
                    "role": "Project Founder"
                }
            ],
            "description": "Twig, the flexible, fast, and secure template language for PHP",
            "homepage": "https://twig.symfony.com",
            "keywords": [
                "templating"
            ],
            "support": {
                "issues": "https://github.com/twigphp/Twig/issues",
                "source": "https://github.com/twigphp/Twig/tree/v3.10.3"
            },
            "funding": [
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/twig/twig",
                    "type": "tidelift"
                }
            ],
            "time": "2024-05-16T10:04:27+00:00"
        },
        {
            "name": "webimpress/safe-writer",
            "version": "2.2.0",
            "source": {
                "type": "git",
                "url": "https://github.com/webimpress/safe-writer.git",
                "reference": "9d37cc8bee20f7cb2f58f6e23e05097eab5072e6"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/webimpress/safe-writer/zipball/9d37cc8bee20f7cb2f58f6e23e05097eab5072e6",
                "reference": "9d37cc8bee20f7cb2f58f6e23e05097eab5072e6",
                "shasum": ""
            },
            "require": {
                "php": "^7.3 || ^8.0"
            },
            "require-dev": {
                "phpunit/phpunit": "^9.5.4",
                "vimeo/psalm": "^4.7",
                "webimpress/coding-standard": "^1.2.2"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "2.2.x-dev",
                    "dev-develop": "2.3.x-dev",
                    "dev-release-1.0": "1.0.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Webimpress\\SafeWriter\\": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-2-Clause"
            ],
            "description": "Tool to write files safely, to avoid race conditions",
            "keywords": [
                "concurrent write",
                "file writer",
                "race condition",
                "safe writer",
                "webimpress"
            ],
            "support": {
                "issues": "https://github.com/webimpress/safe-writer/issues",
                "source": "https://github.com/webimpress/safe-writer/tree/2.2.0"
            },
            "funding": [
                {
                    "url": "https://github.com/michalbundyra",
                    "type": "github"
                }
            ],
            "time": "2021-04-19T16:34:45+00:00"
        }
    ],
    "packages-dev": [
        {
            "name": "amphp/amp",
            "version": "v2.6.4",
            "source": {
                "type": "git",
                "url": "https://github.com/amphp/amp.git",
                "reference": "ded3d9be08f526089eb7ee8d9f16a9768f9dec2d"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/amphp/amp/zipball/ded3d9be08f526089eb7ee8d9f16a9768f9dec2d",
                "reference": "ded3d9be08f526089eb7ee8d9f16a9768f9dec2d",
                "shasum": ""
            },
            "require": {
                "php": ">=7.1"
            },
            "require-dev": {
                "amphp/php-cs-fixer-config": "dev-master",
                "amphp/phpunit-util": "^1",
                "ext-json": "*",
                "jetbrains/phpstorm-stubs": "^2019.3",
                "phpunit/phpunit": "^7 | ^8 | ^9",
                "react/promise": "^2",
                "vimeo/psalm": "^3.12"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "2.x-dev"
                }
            },
            "autoload": {
                "files": [
                    "lib/functions.php",
                    "lib/Internal/functions.php"
                ],
                "psr-4": {
                    "Amp\\": "lib"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Daniel Lowrey",
                    "email": "rdlowrey@php.net"
                },
                {
                    "name": "Aaron Piotrowski",
                    "email": "aaron@trowski.com"
                },
                {
                    "name": "Bob Weinand",
                    "email": "bobwei9@hotmail.com"
                },
                {
                    "name": "Niklas Keller",
                    "email": "me@kelunik.com"
                }
            ],
            "description": "A non-blocking concurrency framework for PHP applications.",
            "homepage": "https://amphp.org/amp",
            "keywords": [
                "async",
                "asynchronous",
                "awaitable",
                "concurrency",
                "event",
                "event-loop",
                "future",
                "non-blocking",
                "promise"
            ],
            "support": {
                "irc": "irc://irc.freenode.org/amphp",
                "issues": "https://github.com/amphp/amp/issues",
                "source": "https://github.com/amphp/amp/tree/v2.6.4"
            },
            "funding": [
                {
                    "url": "https://github.com/amphp",
                    "type": "github"
                }
            ],
            "time": "2024-03-21T18:52:26+00:00"
        },
        {
            "name": "amphp/byte-stream",
            "version": "v1.8.2",
            "source": {
                "type": "git",
                "url": "https://github.com/amphp/byte-stream.git",
                "reference": "4f0e968ba3798a423730f567b1b50d3441c16ddc"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/amphp/byte-stream/zipball/4f0e968ba3798a423730f567b1b50d3441c16ddc",
                "reference": "4f0e968ba3798a423730f567b1b50d3441c16ddc",
                "shasum": ""
            },
            "require": {
                "amphp/amp": "^2",
                "php": ">=7.1"
            },
            "require-dev": {
                "amphp/php-cs-fixer-config": "dev-master",
                "amphp/phpunit-util": "^1.4",
                "friendsofphp/php-cs-fixer": "^2.3",
                "jetbrains/phpstorm-stubs": "^2019.3",
                "phpunit/phpunit": "^6 || ^7 || ^8",
                "psalm/phar": "^3.11.4"
            },
            "type": "library",
            "autoload": {
                "files": [
                    "lib/functions.php"
                ],
                "psr-4": {
                    "Amp\\ByteStream\\": "lib"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Aaron Piotrowski",
                    "email": "aaron@trowski.com"
                },
                {
                    "name": "Niklas Keller",
                    "email": "me@kelunik.com"
                }
            ],
            "description": "A stream abstraction to make working with non-blocking I/O simple.",
            "homepage": "https://amphp.org/byte-stream",
            "keywords": [
                "amp",
                "amphp",
                "async",
                "io",
                "non-blocking",
                "stream"
            ],
            "support": {
                "issues": "https://github.com/amphp/byte-stream/issues",
                "source": "https://github.com/amphp/byte-stream/tree/v1.8.2"
            },
            "funding": [
                {
                    "url": "https://github.com/amphp",
                    "type": "github"
                }
            ],
            "time": "2024-04-13T18:00:56+00:00"
        },
        {
            "name": "behat/behat",
            "version": "v3.14.0",
            "source": {
                "type": "git",
                "url": "https://github.com/Behat/Behat.git",
                "reference": "2a3832d9cb853a794af3a576f9e524ae460f3340"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/Behat/Behat/zipball/2a3832d9cb853a794af3a576f9e524ae460f3340",
                "reference": "2a3832d9cb853a794af3a576f9e524ae460f3340",
                "shasum": ""
            },
            "require": {
                "behat/gherkin": "^4.9.0",
                "behat/transliterator": "^1.2",
                "ext-mbstring": "*",
                "php": "^7.2 || ^8.0",
                "psr/container": "^1.0 || ^2.0",
                "symfony/config": "^4.4 || ^5.0 || ^6.0 || ^7.0",
                "symfony/console": "^4.4 || ^5.0 || ^6.0 || ^7.0",
                "symfony/dependency-injection": "^4.4 || ^5.0 || ^6.0 || ^7.0",
                "symfony/event-dispatcher": "^4.4 || ^5.0 || ^6.0 || ^7.0",
                "symfony/translation": "^4.4 || ^5.0 || ^6.0 || ^7.0",
                "symfony/yaml": "^4.4 || ^5.0 || ^6.0 || ^7.0"
            },
            "require-dev": {
                "herrera-io/box": "~1.6.1",
                "phpspec/prophecy": "^1.15",
                "phpunit/phpunit": "^8.5 || ^9.0",
                "symfony/process": "^4.4 || ^5.0 || ^6.0 || ^7.0",
                "vimeo/psalm": "^4.8"
            },
            "suggest": {
                "ext-dom": "Needed to output test results in JUnit format."
            },
            "bin": [
                "bin/behat"
            ],
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "3.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Behat\\Hook\\": "src/Behat/Hook/",
                    "Behat\\Step\\": "src/Behat/Step/",
                    "Behat\\Behat\\": "src/Behat/Behat/",
                    "Behat\\Testwork\\": "src/Behat/Testwork/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Konstantin Kudryashov",
                    "email": "ever.zet@gmail.com",
                    "homepage": "http://everzet.com"
                }
            ],
            "description": "Scenario-oriented BDD framework for PHP",
            "homepage": "http://behat.org/",
            "keywords": [
                "Agile",
                "BDD",
                "ScenarioBDD",
                "Scrum",
                "StoryBDD",
                "User story",
                "business",
                "development",
                "documentation",
                "examples",
                "symfony",
                "testing"
            ],
            "support": {
                "issues": "https://github.com/Behat/Behat/issues",
                "source": "https://github.com/Behat/Behat/tree/v3.14.0"
            },
            "time": "2023-12-09T13:55:02+00:00"
        },
        {
            "name": "behat/gherkin",
            "version": "v4.9.0",
            "source": {
                "type": "git",
                "url": "https://github.com/Behat/Gherkin.git",
                "reference": "0bc8d1e30e96183e4f36db9dc79caead300beff4"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/Behat/Gherkin/zipball/0bc8d1e30e96183e4f36db9dc79caead300beff4",
                "reference": "0bc8d1e30e96183e4f36db9dc79caead300beff4",
                "shasum": ""
            },
            "require": {
                "php": "~7.2|~8.0"
            },
            "require-dev": {
                "cucumber/cucumber": "dev-gherkin-22.0.0",
                "phpunit/phpunit": "~8|~9",
                "symfony/yaml": "~3|~4|~5"
            },
            "suggest": {
                "symfony/yaml": "If you want to parse features, represented in YAML files"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "4.x-dev"
                }
            },
            "autoload": {
                "psr-0": {
                    "Behat\\Gherkin": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Konstantin Kudryashov",
                    "email": "ever.zet@gmail.com",
                    "homepage": "http://everzet.com"
                }
            ],
            "description": "Gherkin DSL parser for PHP",
            "homepage": "http://behat.org/",
            "keywords": [
                "BDD",
                "Behat",
                "Cucumber",
                "DSL",
                "gherkin",
                "parser"
            ],
            "support": {
                "issues": "https://github.com/Behat/Gherkin/issues",
                "source": "https://github.com/Behat/Gherkin/tree/v4.9.0"
            },
            "time": "2021-10-12T13:05:09+00:00"
        },
        {
            "name": "behat/mink",
            "version": "v1.11.0",
            "source": {
                "type": "git",
                "url": "https://github.com/minkphp/Mink.git",
                "reference": "d8527fdf8785aad38455fb426af457ab9937aece"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/minkphp/Mink/zipball/d8527fdf8785aad38455fb426af457ab9937aece",
                "reference": "d8527fdf8785aad38455fb426af457ab9937aece",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2",
                "symfony/css-selector": "^4.4 || ^5.0 || ^6.0 || ^7.0"
            },
            "require-dev": {
                "phpstan/phpstan": "^1.10",
                "phpstan/phpstan-phpunit": "^1.3",
                "phpunit/phpunit": "^8.5.22 || ^9.5.11",
                "symfony/error-handler": "^4.4 || ^5.0 || ^6.0 || ^7.0",
                "symfony/phpunit-bridge": "^5.4 || ^6.0 || ^7.0"
            },
            "suggest": {
                "behat/mink-browserkit-driver": "fast headless driver for any app without JS emulation",
                "behat/mink-selenium2-driver": "slow, but JS-enabled driver for any app (requires Selenium2)",
                "behat/mink-zombie-driver": "fast and JS-enabled headless driver for any app (requires node.js)",
                "dmore/chrome-mink-driver": "fast and JS-enabled driver for any app (requires chromium or google chrome)"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Behat\\Mink\\": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Konstantin Kudryashov",
                    "email": "ever.zet@gmail.com",
                    "homepage": "http://everzet.com"
                }
            ],
            "description": "Browser controller/emulator abstraction for PHP",
            "homepage": "https://mink.behat.org/",
            "keywords": [
                "browser",
                "testing",
                "web"
            ],
            "support": {
                "issues": "https://github.com/minkphp/Mink/issues",
                "source": "https://github.com/minkphp/Mink/tree/v1.11.0"
            },
            "time": "2023-12-09T11:23:23+00:00"
        },
        {
            "name": "behat/mink-browserkit-driver",
            "version": "v2.2.0",
            "source": {
                "type": "git",
                "url": "https://github.com/minkphp/MinkBrowserKitDriver.git",
                "reference": "16d53476e42827ed3aafbfa4fde17a1743eafd50"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/minkphp/MinkBrowserKitDriver/zipball/16d53476e42827ed3aafbfa4fde17a1743eafd50",
                "reference": "16d53476e42827ed3aafbfa4fde17a1743eafd50",
                "shasum": ""
            },
            "require": {
                "behat/mink": "^1.11.0@dev",
                "ext-dom": "*",
                "php": ">=7.2",
                "symfony/browser-kit": "^4.4 || ^5.0 || ^6.0 || ^7.0",
                "symfony/dom-crawler": "^4.4 || ^5.0 || ^6.0 || ^7.0"
            },
            "require-dev": {
                "mink/driver-testsuite": "dev-master",
                "phpstan/phpstan": "^1.10",
                "phpstan/phpstan-phpunit": "^1.3",
                "phpunit/phpunit": "^8.5 || ^9.5",
                "symfony/error-handler": "^4.4 || ^5.0 || ^6.0 || ^7.0",
                "symfony/http-client": "^4.4 || ^5.0 || ^6.0 || ^7.0",
                "symfony/http-kernel": "^4.4 || ^5.0 || ^6.0 || ^7.0",
                "symfony/mime": "^4.4 || ^5.0 || ^6.0 || ^7.0",
                "yoast/phpunit-polyfills": "^1.0"
            },
            "type": "mink-driver",
            "extra": {
                "branch-alias": {
                    "dev-master": "2.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Behat\\Mink\\Driver\\": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Konstantin Kudryashov",
                    "email": "ever.zet@gmail.com",
                    "homepage": "http://everzet.com"
                }
            ],
            "description": "Symfony2 BrowserKit driver for Mink framework",
            "homepage": "https://mink.behat.org/",
            "keywords": [
                "Mink",
                "Symfony2",
                "browser",
                "testing"
            ],
            "support": {
                "issues": "https://github.com/minkphp/MinkBrowserKitDriver/issues",
                "source": "https://github.com/minkphp/MinkBrowserKitDriver/tree/v2.2.0"
            },
            "time": "2023-12-09T11:30:50+00:00"
        },
        {
            "name": "behat/transliterator",
            "version": "v1.5.0",
            "source": {
                "type": "git",
                "url": "https://github.com/Behat/Transliterator.git",
                "reference": "baac5873bac3749887d28ab68e2f74db3a4408af"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/Behat/Transliterator/zipball/baac5873bac3749887d28ab68e2f74db3a4408af",
                "reference": "baac5873bac3749887d28ab68e2f74db3a4408af",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2"
            },
            "require-dev": {
                "chuyskywalker/rolling-curl": "^3.1",
                "php-yaoi/php-yaoi": "^1.0",
                "phpunit/phpunit": "^8.5.25 || ^9.5.19"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Behat\\Transliterator\\": "src/Behat/Transliterator"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "Artistic-1.0"
            ],
            "description": "String transliterator",
            "keywords": [
                "i18n",
                "slug",
                "transliterator"
            ],
            "support": {
                "issues": "https://github.com/Behat/Transliterator/issues",
                "source": "https://github.com/Behat/Transliterator/tree/v1.5.0"
            },
            "time": "2022-03-30T09:27:43+00:00"
        },
        {
            "name": "codelytv/coding-style",
            "version": "1.3.0",
            "source": {
                "type": "git",
                "url": "https://github.com/CodelyTV/php-coding_style-codely.git",
                "reference": "41d7e6b651619467b05018666606a1ef0958263e"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/CodelyTV/php-coding_style-codely/zipball/41d7e6b651619467b05018666606a1ef0958263e",
                "reference": "41d7e6b651619467b05018666606a1ef0958263e",
                "shasum": ""
            },
            "require": {
                "symplify/easy-coding-standard": "^12.0"
            },
            "type": "library",
            "autoload": {
                "psr-4": {
                    "CodelyTv\\": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "AGPL-3.0-or-later"
            ],
            "authors": [
                {
                    "name": "Codely",
                    "homepage": "https://codely.com"
                }
            ],
            "description": "PHP Coding Style rules we use in Codely",
            "keywords": [
                "Code style",
                "static analysis"
            ],
            "support": {
                "issues": "https://github.com/CodelyTV/php-coding_style-codely/issues",
                "source": "https://github.com/CodelyTV/php-coding_style-codely/tree/1.3.0"
            },
            "funding": [
                {
                    "url": "https://bit.ly/CodelyTvPro",
                    "type": "custom"
                }
            ],
            "time": "2024-08-05T14:17:14+00:00"
        },
        {
            "name": "composer/package-versions-deprecated",
            "version": "1.11.99.5",
            "source": {
                "type": "git",
                "url": "https://github.com/composer/package-versions-deprecated.git",
                "reference": "b4f54f74ef3453349c24a845d22392cd31e65f1d"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/composer/package-versions-deprecated/zipball/b4f54f74ef3453349c24a845d22392cd31e65f1d",
                "reference": "b4f54f74ef3453349c24a845d22392cd31e65f1d",
                "shasum": ""
            },
            "require": {
                "composer-plugin-api": "^1.1.0 || ^2.0",
                "php": "^7 || ^8"
            },
            "replace": {
                "ocramius/package-versions": "1.11.99"
            },
            "require-dev": {
                "composer/composer": "^1.9.3 || ^2.0@dev",
                "ext-zip": "^1.13",
                "phpunit/phpunit": "^6.5 || ^7"
            },
            "type": "composer-plugin",
            "extra": {
                "class": "PackageVersions\\Installer",
                "branch-alias": {
                    "dev-master": "1.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "PackageVersions\\": "src/PackageVersions"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Marco Pivetta",
                    "email": "ocramius@gmail.com"
                },
                {
                    "name": "Jordi Boggiano",
                    "email": "j.boggiano@seld.be"
                }
            ],
            "description": "Composer plugin that provides efficient querying for installed package versions (no runtime IO)",
            "support": {
                "issues": "https://github.com/composer/package-versions-deprecated/issues",
                "source": "https://github.com/composer/package-versions-deprecated/tree/1.11.99.5"
            },
            "funding": [
                {
                    "url": "https://packagist.com",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/composer",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/composer/composer",
                    "type": "tidelift"
                }
            ],
            "time": "2022-01-17T14:14:24+00:00"
        },
        {
            "name": "composer/pcre",
            "version": "3.2.0",
            "source": {
                "type": "git",
                "url": "https://github.com/composer/pcre.git",
                "reference": "ea4ab6f9580a4fd221e0418f2c357cdd39102a90"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/composer/pcre/zipball/ea4ab6f9580a4fd221e0418f2c357cdd39102a90",
                "reference": "ea4ab6f9580a4fd221e0418f2c357cdd39102a90",
                "shasum": ""
            },
            "require": {
                "php": "^7.4 || ^8.0"
            },
            "conflict": {
                "phpstan/phpstan": "<1.11.8"
            },
            "require-dev": {
                "phpstan/phpstan": "^1.11.8",
                "phpstan/phpstan-strict-rules": "^1.1",
                "phpunit/phpunit": "^8 || ^9"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-main": "3.x-dev"
                },
                "phpstan": {
                    "includes": [
                        "extension.neon"
                    ]
                }
            },
            "autoload": {
                "psr-4": {
                    "Composer\\Pcre\\": "src"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Jordi Boggiano",
                    "email": "j.boggiano@seld.be",
                    "homepage": "http://seld.be"
                }
            ],
            "description": "PCRE wrapping library that offers type-safe preg_* replacements.",
            "keywords": [
                "PCRE",
                "preg",
                "regex",
                "regular expression"
            ],
            "support": {
                "issues": "https://github.com/composer/pcre/issues",
                "source": "https://github.com/composer/pcre/tree/3.2.0"
            },
            "funding": [
                {
                    "url": "https://packagist.com",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/composer",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/composer/composer",
                    "type": "tidelift"
                }
            ],
            "time": "2024-07-25T09:36:02+00:00"
        },
        {
            "name": "composer/semver",
            "version": "3.4.2",
            "source": {
                "type": "git",
                "url": "https://github.com/composer/semver.git",
                "reference": "c51258e759afdb17f1fd1fe83bc12baaef6309d6"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/composer/semver/zipball/c51258e759afdb17f1fd1fe83bc12baaef6309d6",
                "reference": "c51258e759afdb17f1fd1fe83bc12baaef6309d6",
                "shasum": ""
            },
            "require": {
                "php": "^5.3.2 || ^7.0 || ^8.0"
            },
            "require-dev": {
                "phpstan/phpstan": "^1.4",
                "symfony/phpunit-bridge": "^4.2 || ^5"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-main": "3.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Composer\\Semver\\": "src"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Nils Adermann",
                    "email": "naderman@naderman.de",
                    "homepage": "http://www.naderman.de"
                },
                {
                    "name": "Jordi Boggiano",
                    "email": "j.boggiano@seld.be",
                    "homepage": "http://seld.be"
                },
                {
                    "name": "Rob Bast",
                    "email": "rob.bast@gmail.com",
                    "homepage": "http://robbast.nl"
                }
            ],
            "description": "Semver library that offers utilities, version constraint parsing and validation.",
            "keywords": [
                "semantic",
                "semver",
                "validation",
                "versioning"
            ],
            "support": {
                "irc": "ircs://irc.libera.chat:6697/composer",
                "issues": "https://github.com/composer/semver/issues",
                "source": "https://github.com/composer/semver/tree/3.4.2"
            },
            "funding": [
                {
                    "url": "https://packagist.com",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/composer",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/composer/composer",
                    "type": "tidelift"
                }
            ],
            "time": "2024-07-12T11:35:52+00:00"
        },
        {
            "name": "composer/xdebug-handler",
            "version": "3.0.5",
            "source": {
                "type": "git",
                "url": "https://github.com/composer/xdebug-handler.git",
                "reference": "6c1925561632e83d60a44492e0b344cf48ab85ef"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/composer/xdebug-handler/zipball/6c1925561632e83d60a44492e0b344cf48ab85ef",
                "reference": "6c1925561632e83d60a44492e0b344cf48ab85ef",
                "shasum": ""
            },
            "require": {
                "composer/pcre": "^1 || ^2 || ^3",
                "php": "^7.2.5 || ^8.0",
                "psr/log": "^1 || ^2 || ^3"
            },
            "require-dev": {
                "phpstan/phpstan": "^1.0",
                "phpstan/phpstan-strict-rules": "^1.1",
                "phpunit/phpunit": "^8.5 || ^9.6 || ^10.5"
            },
            "type": "library",
            "autoload": {
                "psr-4": {
                    "Composer\\XdebugHandler\\": "src"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "John Stevenson",
                    "email": "john-stevenson@blueyonder.co.uk"
                }
            ],
            "description": "Restarts a process without Xdebug.",
            "keywords": [
                "Xdebug",
                "performance"
            ],
            "support": {
                "irc": "ircs://irc.libera.chat:6697/composer",
                "issues": "https://github.com/composer/xdebug-handler/issues",
                "source": "https://github.com/composer/xdebug-handler/tree/3.0.5"
            },
            "funding": [
                {
                    "url": "https://packagist.com",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/composer",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/composer/composer",
                    "type": "tidelift"
                }
            ],
            "time": "2024-05-06T16:37:16+00:00"
        },
        {
            "name": "dnoegel/php-xdg-base-dir",
            "version": "v0.1.1",
            "source": {
                "type": "git",
                "url": "https://github.com/dnoegel/php-xdg-base-dir.git",
                "reference": "8f8a6e48c5ecb0f991c2fdcf5f154a47d85f9ffd"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/dnoegel/php-xdg-base-dir/zipball/8f8a6e48c5ecb0f991c2fdcf5f154a47d85f9ffd",
                "reference": "8f8a6e48c5ecb0f991c2fdcf5f154a47d85f9ffd",
                "shasum": ""
            },
            "require": {
                "php": ">=5.3.2"
            },
            "require-dev": {
                "phpunit/phpunit": "~7.0|~6.0|~5.0|~4.8.35"
            },
            "type": "library",
            "autoload": {
                "psr-4": {
                    "XdgBaseDir\\": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "description": "implementation of xdg base directory specification for php",
            "support": {
                "issues": "https://github.com/dnoegel/php-xdg-base-dir/issues",
                "source": "https://github.com/dnoegel/php-xdg-base-dir/tree/v0.1.1"
            },
            "time": "2019-12-04T15:06:13+00:00"
        },
        {
            "name": "fakerphp/faker",
            "version": "v1.23.1",
            "source": {
                "type": "git",
                "url": "https://github.com/FakerPHP/Faker.git",
                "reference": "bfb4fe148adbf78eff521199619b93a52ae3554b"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/FakerPHP/Faker/zipball/bfb4fe148adbf78eff521199619b93a52ae3554b",
                "reference": "bfb4fe148adbf78eff521199619b93a52ae3554b",
                "shasum": ""
            },
            "require": {
                "php": "^7.4 || ^8.0",
                "psr/container": "^1.0 || ^2.0",
                "symfony/deprecation-contracts": "^2.2 || ^3.0"
            },
            "conflict": {
                "fzaninotto/faker": "*"
            },
            "require-dev": {
                "bamarni/composer-bin-plugin": "^1.4.1",
                "doctrine/persistence": "^1.3 || ^2.0",
                "ext-intl": "*",
                "phpunit/phpunit": "^9.5.26",
                "symfony/phpunit-bridge": "^5.4.16"
            },
            "suggest": {
                "doctrine/orm": "Required to use Faker\\ORM\\Doctrine",
                "ext-curl": "Required by Faker\\Provider\\Image to download images.",
                "ext-dom": "Required by Faker\\Provider\\HtmlLorem for generating random HTML.",
                "ext-iconv": "Required by Faker\\Provider\\ru_RU\\Text::realText() for generating real Russian text.",
                "ext-mbstring": "Required for multibyte Unicode string functionality."
            },
            "type": "library",
            "autoload": {
                "psr-4": {
                    "Faker\\": "src/Faker/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "François Zaninotto"
                }
            ],
            "description": "Faker is a PHP library that generates fake data for you.",
            "keywords": [
                "data",
                "faker",
                "fixtures"
            ],
            "support": {
                "issues": "https://github.com/FakerPHP/Faker/issues",
                "source": "https://github.com/FakerPHP/Faker/tree/v1.23.1"
            },
            "time": "2024-01-02T13:46:09+00:00"
        },
        {
            "name": "felixfbecker/advanced-json-rpc",
            "version": "v3.2.1",
            "source": {
                "type": "git",
                "url": "https://github.com/felixfbecker/php-advanced-json-rpc.git",
                "reference": "b5f37dbff9a8ad360ca341f3240dc1c168b45447"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/felixfbecker/php-advanced-json-rpc/zipball/b5f37dbff9a8ad360ca341f3240dc1c168b45447",
                "reference": "b5f37dbff9a8ad360ca341f3240dc1c168b45447",
                "shasum": ""
            },
            "require": {
                "netresearch/jsonmapper": "^1.0 || ^2.0 || ^3.0 || ^4.0",
                "php": "^7.1 || ^8.0",
                "phpdocumentor/reflection-docblock": "^4.3.4 || ^5.0.0"
            },
            "require-dev": {
                "phpunit/phpunit": "^7.0 || ^8.0"
            },
            "type": "library",
            "autoload": {
                "psr-4": {
                    "AdvancedJsonRpc\\": "lib/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "ISC"
            ],
            "authors": [
                {
                    "name": "Felix Becker",
                    "email": "felix.b@outlook.com"
                }
            ],
            "description": "A more advanced JSONRPC implementation",
            "support": {
                "issues": "https://github.com/felixfbecker/php-advanced-json-rpc/issues",
                "source": "https://github.com/felixfbecker/php-advanced-json-rpc/tree/v3.2.1"
            },
            "time": "2021-06-11T22:34:44+00:00"
        },
        {
            "name": "felixfbecker/language-server-protocol",
            "version": "v1.5.2",
            "source": {
                "type": "git",
                "url": "https://github.com/felixfbecker/php-language-server-protocol.git",
                "reference": "6e82196ffd7c62f7794d778ca52b69feec9f2842"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/felixfbecker/php-language-server-protocol/zipball/6e82196ffd7c62f7794d778ca52b69feec9f2842",
                "reference": "6e82196ffd7c62f7794d778ca52b69feec9f2842",
                "shasum": ""
            },
            "require": {
                "php": ">=7.1"
            },
            "require-dev": {
                "phpstan/phpstan": "*",
                "squizlabs/php_codesniffer": "^3.1",
                "vimeo/psalm": "^4.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "LanguageServerProtocol\\": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "ISC"
            ],
            "authors": [
                {
                    "name": "Felix Becker",
                    "email": "felix.b@outlook.com"
                }
            ],
            "description": "PHP classes for the Language Server Protocol",
            "keywords": [
                "language",
                "microsoft",
                "php",
                "server"
            ],
            "support": {
                "issues": "https://github.com/felixfbecker/php-language-server-protocol/issues",
                "source": "https://github.com/felixfbecker/php-language-server-protocol/tree/v1.5.2"
            },
            "time": "2022-03-02T22:36:06+00:00"
        },
        {
            "name": "fidry/cpu-core-counter",
            "version": "1.1.0",
            "source": {
                "type": "git",
                "url": "https://github.com/theofidry/cpu-core-counter.git",
                "reference": "f92996c4d5c1a696a6a970e20f7c4216200fcc42"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/theofidry/cpu-core-counter/zipball/f92996c4d5c1a696a6a970e20f7c4216200fcc42",
                "reference": "f92996c4d5c1a696a6a970e20f7c4216200fcc42",
                "shasum": ""
            },
            "require": {
                "php": "^7.2 || ^8.0"
            },
            "require-dev": {
                "fidry/makefile": "^0.2.0",
                "fidry/php-cs-fixer-config": "^1.1.2",
                "phpstan/extension-installer": "^1.2.0",
                "phpstan/phpstan": "^1.9.2",
                "phpstan/phpstan-deprecation-rules": "^1.0.0",
                "phpstan/phpstan-phpunit": "^1.2.2",
                "phpstan/phpstan-strict-rules": "^1.4.4",
                "phpunit/phpunit": "^8.5.31 || ^9.5.26",
                "webmozarts/strict-phpunit": "^7.5"
            },
            "type": "library",
            "autoload": {
                "psr-4": {
                    "Fidry\\CpuCoreCounter\\": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Théo FIDRY",
                    "email": "theo.fidry@gmail.com"
                }
            ],
            "description": "Tiny utility to get the number of CPU cores.",
            "keywords": [
                "CPU",
                "core"
            ],
            "support": {
                "issues": "https://github.com/theofidry/cpu-core-counter/issues",
                "source": "https://github.com/theofidry/cpu-core-counter/tree/1.1.0"
            },
            "funding": [
                {
                    "url": "https://github.com/theofidry",
                    "type": "github"
                }
            ],
            "time": "2024-02-07T09:43:46+00:00"
        },
        {
            "name": "friends-of-behat/mink-extension",
            "version": "v2.7.5",
            "source": {
                "type": "git",
                "url": "https://github.com/FriendsOfBehat/MinkExtension.git",
                "reference": "854336030e11983f580f49faad1b49a1238f9846"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/FriendsOfBehat/MinkExtension/zipball/854336030e11983f580f49faad1b49a1238f9846",
                "reference": "854336030e11983f580f49faad1b49a1238f9846",
                "shasum": ""
            },
            "require": {
                "behat/behat": "^3.0.5",
                "behat/mink": "^1.5",
                "php": ">=7.4",
                "symfony/config": "^4.4 || ^5.0 || ^6.0 || ^7.0"
            },
            "replace": {
                "behat/mink-extension": "self.version"
            },
            "require-dev": {
                "behat/mink-goutte-driver": "^1.1 || ^2.0",
                "phpspec/phpspec": "^6.0 || ^7.0 || 7.1.x-dev"
            },
            "type": "behat-extension",
            "extra": {
                "branch-alias": {
                    "dev-master": "2.1.x-dev"
                }
            },
            "autoload": {
                "psr-0": {
                    "Behat\\MinkExtension": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Konstantin Kudryashov",
                    "email": "ever.zet@gmail.com"
                },
                {
                    "name": "Christophe Coevoet",
                    "email": "stof@notk.org"
                }
            ],
            "description": "Mink extension for Behat",
            "homepage": "http://extensions.behat.org/mink",
            "keywords": [
                "browser",
                "gui",
                "test",
                "web"
            ],
            "support": {
                "issues": "https://github.com/FriendsOfBehat/MinkExtension/issues",
                "source": "https://github.com/FriendsOfBehat/MinkExtension/tree/v2.7.5"
            },
            "time": "2024-01-11T09:12:02+00:00"
        },
        {
            "name": "friends-of-behat/symfony-extension",
            "version": "v2.6.0",
            "source": {
                "type": "git",
                "url": "https://github.com/FriendsOfBehat/SymfonyExtension.git",
                "reference": "dfb1c9c96cc0fb7c8e1caa060695426a12e1efbd"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/FriendsOfBehat/SymfonyExtension/zipball/dfb1c9c96cc0fb7c8e1caa060695426a12e1efbd",
                "reference": "dfb1c9c96cc0fb7c8e1caa060695426a12e1efbd",
                "shasum": ""
            },
            "require": {
                "behat/behat": "^3.6.1",
                "php": "^8.1",
                "symfony/dependency-injection": "^6.2 || ^7.0",
                "symfony/http-kernel": "^6.2 || ^7.0"
            },
            "require-dev": {
                "behat/mink": "^1.9",
                "behat/mink-browserkit-driver": "^2.0",
                "behat/mink-selenium2-driver": "^1.3",
                "friends-of-behat/mink-extension": "^2.5",
                "friends-of-behat/page-object-extension": "^0.3.2",
                "friends-of-behat/service-container-extension": "^1.1",
                "sylius-labs/coding-standard": ">=4.1.1, <=4.2.1",
                "symfony/browser-kit": "^6.2 || ^7.0",
                "symfony/framework-bundle": "^6.2 || ^7.0",
                "symfony/process": "^6.2 || ^7.0",
                "symfony/yaml": "^6.2 || ^7.0",
                "vimeo/psalm": "4.30.0"
            },
            "suggest": {
                "behat/mink": "^1.9",
                "behat/mink-browserkit-driver": "^2.0",
                "friends-of-behat/mink-extension": "^2.5"
            },
            "type": "symfony-bundle",
            "extra": {
                "branch-alias": {
                    "dev-master": "2.2-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "FriendsOfBehat\\SymfonyExtension\\": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Kamil Kokot",
                    "email": "kamil@kokot.me",
                    "homepage": "https://kamilkokot.com"
                }
            ],
            "description": "Integrates Behat with Symfony.",
            "support": {
                "issues": "https://github.com/FriendsOfBehat/SymfonyExtension/issues",
                "source": "https://github.com/FriendsOfBehat/SymfonyExtension/tree/v2.6.0"
            },
            "time": "2024-07-03T15:49:43+00:00"
        },
        {
            "name": "hamcrest/hamcrest-php",
            "version": "v2.0.1",
            "source": {
                "type": "git",
                "url": "https://github.com/hamcrest/hamcrest-php.git",
                "reference": "8c3d0a3f6af734494ad8f6fbbee0ba92422859f3"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/hamcrest/hamcrest-php/zipball/8c3d0a3f6af734494ad8f6fbbee0ba92422859f3",
                "reference": "8c3d0a3f6af734494ad8f6fbbee0ba92422859f3",
                "shasum": ""
            },
            "require": {
                "php": "^5.3|^7.0|^8.0"
            },
            "replace": {
                "cordoval/hamcrest-php": "*",
                "davedevelopment/hamcrest-php": "*",
                "kodova/hamcrest-php": "*"
            },
            "require-dev": {
                "phpunit/php-file-iterator": "^1.4 || ^2.0",
                "phpunit/phpunit": "^4.8.36 || ^5.7 || ^6.5 || ^7.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "2.1-dev"
                }
            },
            "autoload": {
                "classmap": [
                    "hamcrest"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause"
            ],
            "description": "This is the PHP port of Hamcrest Matchers",
            "keywords": [
                "test"
            ],
            "support": {
                "issues": "https://github.com/hamcrest/hamcrest-php/issues",
                "source": "https://github.com/hamcrest/hamcrest-php/tree/v2.0.1"
            },
            "time": "2020-07-09T08:09:16+00:00"
        },
        {
            "name": "masterminds/html5",
            "version": "2.9.0",
            "source": {
                "type": "git",
                "url": "https://github.com/Masterminds/html5-php.git",
                "reference": "f5ac2c0b0a2eefca70b2ce32a5809992227e75a6"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/Masterminds/html5-php/zipball/f5ac2c0b0a2eefca70b2ce32a5809992227e75a6",
                "reference": "f5ac2c0b0a2eefca70b2ce32a5809992227e75a6",
                "shasum": ""
            },
            "require": {
                "ext-dom": "*",
                "php": ">=5.3.0"
            },
            "require-dev": {
                "phpunit/phpunit": "^4.8.35 || ^5.7.21 || ^6 || ^7 || ^8 || ^9"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "2.7-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Masterminds\\": "src"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Matt Butcher",
                    "email": "technosophos@gmail.com"
                },
                {
                    "name": "Matt Farina",
                    "email": "matt@mattfarina.com"
                },
                {
                    "name": "Asmir Mustafic",
                    "email": "goetas@gmail.com"
                }
            ],
            "description": "An HTML5 parser and serializer.",
            "homepage": "http://masterminds.github.io/html5-php",
            "keywords": [
                "HTML5",
                "dom",
                "html",
                "parser",
                "querypath",
                "serializer",
                "xml"
            ],
            "support": {
                "issues": "https://github.com/Masterminds/html5-php/issues",
                "source": "https://github.com/Masterminds/html5-php/tree/2.9.0"
            },
            "time": "2024-03-31T07:05:07+00:00"
        },
        {
            "name": "mockery/mockery",
            "version": "1.6.12",
            "source": {
                "type": "git",
                "url": "https://github.com/mockery/mockery.git",
                "reference": "1f4efdd7d3beafe9807b08156dfcb176d18f1699"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/mockery/mockery/zipball/1f4efdd7d3beafe9807b08156dfcb176d18f1699",
                "reference": "1f4efdd7d3beafe9807b08156dfcb176d18f1699",
                "shasum": ""
            },
            "require": {
                "hamcrest/hamcrest-php": "^2.0.1",
                "lib-pcre": ">=7.0",
                "php": ">=7.3"
            },
            "conflict": {
                "phpunit/phpunit": "<8.0"
            },
            "require-dev": {
                "phpunit/phpunit": "^8.5 || ^9.6.17",
                "symplify/easy-coding-standard": "^12.1.14"
            },
            "type": "library",
            "autoload": {
                "files": [
                    "library/helpers.php",
                    "library/Mockery.php"
                ],
                "psr-4": {
                    "Mockery\\": "library/Mockery"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause"
            ],
            "authors": [
                {
                    "name": "Pádraic Brady",
                    "email": "padraic.brady@gmail.com",
                    "homepage": "https://github.com/padraic",
                    "role": "Author"
                },
                {
                    "name": "Dave Marshall",
                    "email": "dave.marshall@atstsolutions.co.uk",
                    "homepage": "https://davedevelopment.co.uk",
                    "role": "Developer"
                },
                {
                    "name": "Nathanael Esayeas",
                    "email": "nathanael.esayeas@protonmail.com",
                    "homepage": "https://github.com/ghostwriter",
                    "role": "Lead Developer"
                }
            ],
            "description": "Mockery is a simple yet flexible PHP mock object framework",
            "homepage": "https://github.com/mockery/mockery",
            "keywords": [
                "BDD",
                "TDD",
                "library",
                "mock",
                "mock objects",
                "mockery",
                "stub",
                "test",
                "test double",
                "testing"
            ],
            "support": {
                "docs": "https://docs.mockery.io/",
                "issues": "https://github.com/mockery/mockery/issues",
                "rss": "https://github.com/mockery/mockery/releases.atom",
                "security": "https://github.com/mockery/mockery/security/advisories",
                "source": "https://github.com/mockery/mockery"
            },
            "time": "2024-05-16T03:13:13+00:00"
        },
        {
            "name": "myclabs/deep-copy",
            "version": "1.12.0",
            "source": {
                "type": "git",
                "url": "https://github.com/myclabs/DeepCopy.git",
                "reference": "3a6b9a42cd8f8771bd4295d13e1423fa7f3d942c"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/myclabs/DeepCopy/zipball/3a6b9a42cd8f8771bd4295d13e1423fa7f3d942c",
                "reference": "3a6b9a42cd8f8771bd4295d13e1423fa7f3d942c",
                "shasum": ""
            },
            "require": {
                "php": "^7.1 || ^8.0"
            },
            "conflict": {
                "doctrine/collections": "<1.6.8",
                "doctrine/common": "<2.13.3 || >=3 <3.2.2"
            },
            "require-dev": {
                "doctrine/collections": "^1.6.8",
                "doctrine/common": "^2.13.3 || ^3.2.2",
                "phpspec/prophecy": "^1.10",
                "phpunit/phpunit": "^7.5.20 || ^8.5.23 || ^9.5.13"
            },
            "type": "library",
            "autoload": {
                "files": [
                    "src/DeepCopy/deep_copy.php"
                ],
                "psr-4": {
                    "DeepCopy\\": "src/DeepCopy/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "description": "Create deep copies (clones) of your objects",
            "keywords": [
                "clone",
                "copy",
                "duplicate",
                "object",
                "object graph"
            ],
            "support": {
                "issues": "https://github.com/myclabs/DeepCopy/issues",
                "source": "https://github.com/myclabs/DeepCopy/tree/1.12.0"
            },
            "funding": [
                {
                    "url": "https://tidelift.com/funding/github/packagist/myclabs/deep-copy",
                    "type": "tidelift"
                }
            ],
            "time": "2024-06-12T14:39:25+00:00"
        },
        {
            "name": "netresearch/jsonmapper",
            "version": "v4.4.1",
            "source": {
                "type": "git",
                "url": "https://github.com/cweiske/jsonmapper.git",
                "reference": "132c75c7dd83e45353ebb9c6c9f591952995bbf0"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/cweiske/jsonmapper/zipball/132c75c7dd83e45353ebb9c6c9f591952995bbf0",
                "reference": "132c75c7dd83e45353ebb9c6c9f591952995bbf0",
                "shasum": ""
            },
            "require": {
                "ext-json": "*",
                "ext-pcre": "*",
                "ext-reflection": "*",
                "ext-spl": "*",
                "php": ">=7.1"
            },
            "require-dev": {
                "phpunit/phpunit": "~7.5 || ~8.0 || ~9.0 || ~10.0",
                "squizlabs/php_codesniffer": "~3.5"
            },
            "type": "library",
            "autoload": {
                "psr-0": {
                    "JsonMapper": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "OSL-3.0"
            ],
            "authors": [
                {
                    "name": "Christian Weiske",
                    "email": "cweiske@cweiske.de",
                    "homepage": "http://github.com/cweiske/jsonmapper/",
                    "role": "Developer"
                }
            ],
            "description": "Map nested JSON structures onto PHP classes",
            "support": {
                "email": "cweiske@cweiske.de",
                "issues": "https://github.com/cweiske/jsonmapper/issues",
                "source": "https://github.com/cweiske/jsonmapper/tree/v4.4.1"
            },
            "time": "2024-01-31T06:18:54+00:00"
        },
        {
            "name": "nikic/php-parser",
            "version": "v4.19.1",
            "source": {
                "type": "git",
                "url": "https://github.com/nikic/PHP-Parser.git",
                "reference": "4e1b88d21c69391150ace211e9eaf05810858d0b"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/nikic/PHP-Parser/zipball/4e1b88d21c69391150ace211e9eaf05810858d0b",
                "reference": "4e1b88d21c69391150ace211e9eaf05810858d0b",
                "shasum": ""
            },
            "require": {
                "ext-tokenizer": "*",
                "php": ">=7.1"
            },
            "require-dev": {
                "ircmaxell/php-yacc": "^0.0.7",
                "phpunit/phpunit": "^6.5 || ^7.0 || ^8.0 || ^9.0"
            },
            "bin": [
                "bin/php-parse"
            ],
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "4.9-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "PhpParser\\": "lib/PhpParser"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause"
            ],
            "authors": [
                {
                    "name": "Nikita Popov"
                }
            ],
            "description": "A PHP parser written in PHP",
            "keywords": [
                "parser",
                "php"
            ],
            "support": {
                "issues": "https://github.com/nikic/PHP-Parser/issues",
                "source": "https://github.com/nikic/PHP-Parser/tree/v4.19.1"
            },
            "time": "2024-03-17T08:10:35+00:00"
        },
        {
            "name": "pdepend/pdepend",
            "version": "2.16.2",
            "source": {
                "type": "git",
                "url": "https://github.com/pdepend/pdepend.git",
                "reference": "f942b208dc2a0868454d01b29f0c75bbcfc6ed58"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/pdepend/pdepend/zipball/f942b208dc2a0868454d01b29f0c75bbcfc6ed58",
                "reference": "f942b208dc2a0868454d01b29f0c75bbcfc6ed58",
                "shasum": ""
            },
            "require": {
                "php": ">=5.3.7",
                "symfony/config": "^2.3.0|^3|^4|^5|^6.0|^7.0",
                "symfony/dependency-injection": "^2.3.0|^3|^4|^5|^6.0|^7.0",
                "symfony/filesystem": "^2.3.0|^3|^4|^5|^6.0|^7.0",
                "symfony/polyfill-mbstring": "^1.19"
            },
            "require-dev": {
                "easy-doc/easy-doc": "0.0.0|^1.2.3",
                "gregwar/rst": "^1.0",
                "squizlabs/php_codesniffer": "^2.0.0"
            },
            "bin": [
                "src/bin/pdepend"
            ],
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "2.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "PDepend\\": "src/main/php/PDepend"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause"
            ],
            "description": "Official version of pdepend to be handled with Composer",
            "keywords": [
                "PHP Depend",
                "PHP_Depend",
                "dev",
                "pdepend"
            ],
            "support": {
                "issues": "https://github.com/pdepend/pdepend/issues",
                "source": "https://github.com/pdepend/pdepend/tree/2.16.2"
            },
            "funding": [
                {
                    "url": "https://tidelift.com/funding/github/packagist/pdepend/pdepend",
                    "type": "tidelift"
                }
            ],
            "time": "2023-12-17T18:09:59+00:00"
        },
        {
            "name": "phar-io/manifest",
            "version": "2.0.4",
            "source": {
                "type": "git",
                "url": "https://github.com/phar-io/manifest.git",
                "reference": "54750ef60c58e43759730615a392c31c80e23176"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/phar-io/manifest/zipball/54750ef60c58e43759730615a392c31c80e23176",
                "reference": "54750ef60c58e43759730615a392c31c80e23176",
                "shasum": ""
            },
            "require": {
                "ext-dom": "*",
                "ext-libxml": "*",
                "ext-phar": "*",
                "ext-xmlwriter": "*",
                "phar-io/version": "^3.0.1",
                "php": "^7.2 || ^8.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "2.0.x-dev"
                }
            },
            "autoload": {
                "classmap": [
                    "src/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause"
            ],
            "authors": [
                {
                    "name": "Arne Blankerts",
                    "email": "arne@blankerts.de",
                    "role": "Developer"
                },
                {
                    "name": "Sebastian Heuer",
                    "email": "sebastian@phpeople.de",
                    "role": "Developer"
                },
                {
                    "name": "Sebastian Bergmann",
                    "email": "sebastian@phpunit.de",
                    "role": "Developer"
                }
            ],
            "description": "Component for reading phar.io manifest information from a PHP Archive (PHAR)",
            "support": {
                "issues": "https://github.com/phar-io/manifest/issues",
                "source": "https://github.com/phar-io/manifest/tree/2.0.4"
            },
            "funding": [
                {
                    "url": "https://github.com/theseer",
                    "type": "github"
                }
            ],
            "time": "2024-03-03T12:33:53+00:00"
        },
        {
            "name": "phar-io/version",
            "version": "3.2.1",
            "source": {
                "type": "git",
                "url": "https://github.com/phar-io/version.git",
                "reference": "4f7fd7836c6f332bb2933569e566a0d6c4cbed74"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/phar-io/version/zipball/4f7fd7836c6f332bb2933569e566a0d6c4cbed74",
                "reference": "4f7fd7836c6f332bb2933569e566a0d6c4cbed74",
                "shasum": ""
            },
            "require": {
                "php": "^7.2 || ^8.0"
            },
            "type": "library",
            "autoload": {
                "classmap": [
                    "src/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause"
            ],
            "authors": [
                {
                    "name": "Arne Blankerts",
                    "email": "arne@blankerts.de",
                    "role": "Developer"
                },
                {
                    "name": "Sebastian Heuer",
                    "email": "sebastian@phpeople.de",
                    "role": "Developer"
                },
                {
                    "name": "Sebastian Bergmann",
                    "email": "sebastian@phpunit.de",
                    "role": "Developer"
                }
            ],
            "description": "Library for handling version information and constraints",
            "support": {
                "issues": "https://github.com/phar-io/version/issues",
                "source": "https://github.com/phar-io/version/tree/3.2.1"
            },
            "time": "2022-02-21T01:04:05+00:00"
        },
        {
            "name": "phpat/phpat",
            "version": "0.10.18",
            "source": {
                "type": "git",
                "url": "https://github.com/carlosas/phpat.git",
                "reference": "4c29e330fb306876bca3174aa4b097d0d8611964"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/carlosas/phpat/zipball/4c29e330fb306876bca3174aa4b097d0d8611964",
                "reference": "4c29e330fb306876bca3174aa4b097d0d8611964",
                "shasum": ""
            },
            "require": {
                "php": "^7.4 || ^8.0",
                "phpstan/phpstan": "^1.3"
            },
            "require-dev": {
                "friendsofphp/php-cs-fixer": "3.46",
                "kubawerlos/php-cs-fixer-custom-fixers": "3.18",
                "phpunit/phpunit": "^9.0 || ^10.0",
                "vimeo/psalm": "^5.0"
            },
            "type": "phpstan-extension",
            "extra": {
                "phpstan": {
                    "includes": [
                        "extension.neon"
                    ]
                }
            },
            "autoload": {
                "files": [
                    "helpers.php"
                ],
                "psr-4": {
                    "PHPat\\": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Carlos Alandete Sastre",
                    "email": "carlos.alandete@gmail.com"
                }
            ],
            "description": "PHP Architecture Tester",
            "support": {
                "issues": "https://github.com/carlosas/phpat/issues",
                "source": "https://github.com/carlosas/phpat/tree/0.10.18"
            },
            "time": "2024-07-05T14:56:19+00:00"
        },
        {
            "name": "phpdocumentor/reflection-common",
            "version": "2.2.0",
            "source": {
                "type": "git",
                "url": "https://github.com/phpDocumentor/ReflectionCommon.git",
                "reference": "1d01c49d4ed62f25aa84a747ad35d5a16924662b"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/phpDocumentor/ReflectionCommon/zipball/1d01c49d4ed62f25aa84a747ad35d5a16924662b",
                "reference": "1d01c49d4ed62f25aa84a747ad35d5a16924662b",
                "shasum": ""
            },
            "require": {
                "php": "^7.2 || ^8.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-2.x": "2.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "phpDocumentor\\Reflection\\": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Jaap van Otterdijk",
                    "email": "opensource@ijaap.nl"
                }
            ],
            "description": "Common reflection classes used by phpdocumentor to reflect the code structure",
            "homepage": "http://www.phpdoc.org",
            "keywords": [
                "FQSEN",
                "phpDocumentor",
                "phpdoc",
                "reflection",
                "static analysis"
            ],
            "support": {
                "issues": "https://github.com/phpDocumentor/ReflectionCommon/issues",
                "source": "https://github.com/phpDocumentor/ReflectionCommon/tree/2.x"
            },
            "time": "2020-06-27T09:03:43+00:00"
        },
        {
            "name": "phpdocumentor/reflection-docblock",
            "version": "5.4.1",
            "source": {
                "type": "git",
                "url": "https://github.com/phpDocumentor/ReflectionDocBlock.git",
                "reference": "9d07b3f7fdcf5efec5d1609cba3c19c5ea2bdc9c"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/phpDocumentor/ReflectionDocBlock/zipball/9d07b3f7fdcf5efec5d1609cba3c19c5ea2bdc9c",
                "reference": "9d07b3f7fdcf5efec5d1609cba3c19c5ea2bdc9c",
                "shasum": ""
            },
            "require": {
                "doctrine/deprecations": "^1.1",
                "ext-filter": "*",
                "php": "^7.4 || ^8.0",
                "phpdocumentor/reflection-common": "^2.2",
                "phpdocumentor/type-resolver": "^1.7",
                "phpstan/phpdoc-parser": "^1.7",
                "webmozart/assert": "^1.9.1"
            },
            "require-dev": {
                "mockery/mockery": "~1.3.5",
                "phpstan/extension-installer": "^1.1",
                "phpstan/phpstan": "^1.8",
                "phpstan/phpstan-mockery": "^1.1",
                "phpstan/phpstan-webmozart-assert": "^1.2",
                "phpunit/phpunit": "^9.5",
                "vimeo/psalm": "^5.13"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "5.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "phpDocumentor\\Reflection\\": "src"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Mike van Riel",
                    "email": "me@mikevanriel.com"
                },
                {
                    "name": "Jaap van Otterdijk",
                    "email": "opensource@ijaap.nl"
                }
            ],
            "description": "With this component, a library can provide support for annotations via DocBlocks or otherwise retrieve information that is embedded in a DocBlock.",
            "support": {
                "issues": "https://github.com/phpDocumentor/ReflectionDocBlock/issues",
                "source": "https://github.com/phpDocumentor/ReflectionDocBlock/tree/5.4.1"
            },
            "time": "2024-05-21T05:55:05+00:00"
        },
        {
            "name": "phpdocumentor/type-resolver",
            "version": "1.8.2",
            "source": {
                "type": "git",
                "url": "https://github.com/phpDocumentor/TypeResolver.git",
                "reference": "153ae662783729388a584b4361f2545e4d841e3c"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/phpDocumentor/TypeResolver/zipball/153ae662783729388a584b4361f2545e4d841e3c",
                "reference": "153ae662783729388a584b4361f2545e4d841e3c",
                "shasum": ""
            },
            "require": {
                "doctrine/deprecations": "^1.0",
                "php": "^7.3 || ^8.0",
                "phpdocumentor/reflection-common": "^2.0",
                "phpstan/phpdoc-parser": "^1.13"
            },
            "require-dev": {
                "ext-tokenizer": "*",
                "phpbench/phpbench": "^1.2",
                "phpstan/extension-installer": "^1.1",
                "phpstan/phpstan": "^1.8",
                "phpstan/phpstan-phpunit": "^1.1",
                "phpunit/phpunit": "^9.5",
                "rector/rector": "^0.13.9",
                "vimeo/psalm": "^4.25"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-1.x": "1.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "phpDocumentor\\Reflection\\": "src"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Mike van Riel",
                    "email": "me@mikevanriel.com"
                }
            ],
            "description": "A PSR-5 based resolver of Class names, Types and Structural Element Names",
            "support": {
                "issues": "https://github.com/phpDocumentor/TypeResolver/issues",
                "source": "https://github.com/phpDocumentor/TypeResolver/tree/1.8.2"
            },
            "time": "2024-02-23T11:10:43+00:00"
        },
        {
            "name": "phpmd/phpmd",
            "version": "2.15.0",
            "source": {
                "type": "git",
                "url": "https://github.com/phpmd/phpmd.git",
                "reference": "74a1f56e33afad4128b886e334093e98e1b5e7c0"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/phpmd/phpmd/zipball/74a1f56e33afad4128b886e334093e98e1b5e7c0",
                "reference": "74a1f56e33afad4128b886e334093e98e1b5e7c0",
                "shasum": ""
            },
            "require": {
                "composer/xdebug-handler": "^1.0 || ^2.0 || ^3.0",
                "ext-xml": "*",
                "pdepend/pdepend": "^2.16.1",
                "php": ">=5.3.9"
            },
            "require-dev": {
                "easy-doc/easy-doc": "0.0.0 || ^1.3.2",
                "ext-json": "*",
                "ext-simplexml": "*",
                "gregwar/rst": "^1.0",
                "mikey179/vfsstream": "^1.6.8",
                "squizlabs/php_codesniffer": "^2.9.2 || ^3.7.2"
            },
            "bin": [
                "src/bin/phpmd"
            ],
            "type": "library",
            "autoload": {
                "psr-0": {
                    "PHPMD\\": "src/main/php"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause"
            ],
            "authors": [
                {
                    "name": "Manuel Pichler",
                    "email": "github@manuel-pichler.de",
                    "homepage": "https://github.com/manuelpichler",
                    "role": "Project Founder"
                },
                {
                    "name": "Marc Würth",
                    "email": "ravage@bluewin.ch",
                    "homepage": "https://github.com/ravage84",
                    "role": "Project Maintainer"
                },
                {
                    "name": "Other contributors",
                    "homepage": "https://github.com/phpmd/phpmd/graphs/contributors",
                    "role": "Contributors"
                }
            ],
            "description": "PHPMD is a spin-off project of PHP Depend and aims to be a PHP equivalent of the well known Java tool PMD.",
            "homepage": "https://phpmd.org/",
            "keywords": [
                "dev",
                "mess detection",
                "mess detector",
                "pdepend",
                "phpmd",
                "pmd"
            ],
            "support": {
                "irc": "irc://irc.freenode.org/phpmd",
                "issues": "https://github.com/phpmd/phpmd/issues",
                "source": "https://github.com/phpmd/phpmd/tree/2.15.0"
            },
            "funding": [
                {
                    "url": "https://tidelift.com/funding/github/packagist/phpmd/phpmd",
                    "type": "tidelift"
                }
            ],
            "time": "2023-12-11T08:22:20+00:00"
        },
        {
            "name": "phpstan/phpdoc-parser",
            "version": "1.29.1",
            "source": {
                "type": "git",
                "url": "https://github.com/phpstan/phpdoc-parser.git",
                "reference": "fcaefacf2d5c417e928405b71b400d4ce10daaf4"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/phpstan/phpdoc-parser/zipball/fcaefacf2d5c417e928405b71b400d4ce10daaf4",
                "reference": "fcaefacf2d5c417e928405b71b400d4ce10daaf4",
                "shasum": ""
            },
            "require": {
                "php": "^7.2 || ^8.0"
            },
            "require-dev": {
                "doctrine/annotations": "^2.0",
                "nikic/php-parser": "^4.15",
                "php-parallel-lint/php-parallel-lint": "^1.2",
                "phpstan/extension-installer": "^1.0",
                "phpstan/phpstan": "^1.5",
                "phpstan/phpstan-phpunit": "^1.1",
                "phpstan/phpstan-strict-rules": "^1.0",
                "phpunit/phpunit": "^9.5",
                "symfony/process": "^5.2"
            },
            "type": "library",
            "autoload": {
                "psr-4": {
                    "PHPStan\\PhpDocParser\\": [
                        "src/"
                    ]
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "description": "PHPDoc parser with support for nullable, intersection and generic types",
            "support": {
                "issues": "https://github.com/phpstan/phpdoc-parser/issues",
                "source": "https://github.com/phpstan/phpdoc-parser/tree/1.29.1"
            },
            "time": "2024-05-31T08:52:43+00:00"
        },
        {
            "name": "phpstan/phpstan",
            "version": "1.11.9",
            "source": {
                "type": "git",
                "url": "https://github.com/phpstan/phpstan.git",
                "reference": "e370bcddadaede0c1716338b262346f40d296f82"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/phpstan/phpstan/zipball/e370bcddadaede0c1716338b262346f40d296f82",
                "reference": "e370bcddadaede0c1716338b262346f40d296f82",
                "shasum": ""
            },
            "require": {
                "php": "^7.2|^8.0"
            },
            "conflict": {
                "phpstan/phpstan-shim": "*"
            },
            "bin": [
                "phpstan",
                "phpstan.phar"
            ],
            "type": "library",
            "autoload": {
                "files": [
                    "bootstrap.php"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "description": "PHPStan - PHP Static Analysis Tool",
            "keywords": [
                "dev",
                "static analysis"
            ],
            "support": {
                "docs": "https://phpstan.org/user-guide/getting-started",
                "forum": "https://github.com/phpstan/phpstan/discussions",
                "issues": "https://github.com/phpstan/phpstan/issues",
                "security": "https://github.com/phpstan/phpstan/security/policy",
                "source": "https://github.com/phpstan/phpstan-src"
            },
            "funding": [
                {
                    "url": "https://github.com/ondrejmirtes",
                    "type": "github"
                },
                {
                    "url": "https://github.com/phpstan",
                    "type": "github"
                }
            ],
            "time": "2024-08-01T16:25:18+00:00"
        },
        {
            "name": "phpunit/php-code-coverage",
            "version": "9.2.31",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/php-code-coverage.git",
                "reference": "48c34b5d8d983006bd2adc2d0de92963b9155965"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/php-code-coverage/zipball/48c34b5d8d983006bd2adc2d0de92963b9155965",
                "reference": "48c34b5d8d983006bd2adc2d0de92963b9155965",
                "shasum": ""
            },
            "require": {
                "ext-dom": "*",
                "ext-libxml": "*",
                "ext-xmlwriter": "*",
                "nikic/php-parser": "^4.18 || ^5.0",
                "php": ">=7.3",
                "phpunit/php-file-iterator": "^3.0.3",
                "phpunit/php-text-template": "^2.0.2",
                "sebastian/code-unit-reverse-lookup": "^2.0.2",
                "sebastian/complexity": "^2.0",
                "sebastian/environment": "^5.1.2",
                "sebastian/lines-of-code": "^1.0.3",
                "sebastian/version": "^3.0.1",
                "theseer/tokenizer": "^1.2.0"
            },
            "require-dev": {
                "phpunit/phpunit": "^9.3"
            },
            "suggest": {
                "ext-pcov": "PHP extension that provides line coverage",
                "ext-xdebug": "PHP extension that provides line coverage as well as branch and path coverage"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "9.2-dev"
                }
            },
            "autoload": {
                "classmap": [
                    "src/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause"
            ],
            "authors": [
                {
                    "name": "Sebastian Bergmann",
                    "email": "sebastian@phpunit.de",
                    "role": "lead"
                }
            ],
            "description": "Library that provides collection, processing, and rendering functionality for PHP code coverage information.",
            "homepage": "https://github.com/sebastianbergmann/php-code-coverage",
            "keywords": [
                "coverage",
                "testing",
                "xunit"
            ],
            "support": {
                "issues": "https://github.com/sebastianbergmann/php-code-coverage/issues",
                "security": "https://github.com/sebastianbergmann/php-code-coverage/security/policy",
                "source": "https://github.com/sebastianbergmann/php-code-coverage/tree/9.2.31"
            },
            "funding": [
                {
                    "url": "https://github.com/sebastianbergmann",
                    "type": "github"
                }
            ],
            "time": "2024-03-02T06:37:42+00:00"
        },
        {
            "name": "phpunit/php-file-iterator",
            "version": "3.0.6",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/php-file-iterator.git",
                "reference": "cf1c2e7c203ac650e352f4cc675a7021e7d1b3cf"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/php-file-iterator/zipball/cf1c2e7c203ac650e352f4cc675a7021e7d1b3cf",
                "reference": "cf1c2e7c203ac650e352f4cc675a7021e7d1b3cf",
                "shasum": ""
            },
            "require": {
                "php": ">=7.3"
            },
            "require-dev": {
                "phpunit/phpunit": "^9.3"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "3.0-dev"
                }
            },
            "autoload": {
                "classmap": [
                    "src/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause"
            ],
            "authors": [
                {
                    "name": "Sebastian Bergmann",
                    "email": "sebastian@phpunit.de",
                    "role": "lead"
                }
            ],
            "description": "FilterIterator implementation that filters files based on a list of suffixes.",
            "homepage": "https://github.com/sebastianbergmann/php-file-iterator/",
            "keywords": [
                "filesystem",
                "iterator"
            ],
            "support": {
                "issues": "https://github.com/sebastianbergmann/php-file-iterator/issues",
                "source": "https://github.com/sebastianbergmann/php-file-iterator/tree/3.0.6"
            },
            "funding": [
                {
                    "url": "https://github.com/sebastianbergmann",
                    "type": "github"
                }
            ],
            "time": "2021-12-02T12:48:52+00:00"
        },
        {
            "name": "phpunit/php-invoker",
            "version": "3.1.1",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/php-invoker.git",
                "reference": "5a10147d0aaf65b58940a0b72f71c9ac0423cc67"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/php-invoker/zipball/5a10147d0aaf65b58940a0b72f71c9ac0423cc67",
                "reference": "5a10147d0aaf65b58940a0b72f71c9ac0423cc67",
                "shasum": ""
            },
            "require": {
                "php": ">=7.3"
            },
            "require-dev": {
                "ext-pcntl": "*",
                "phpunit/phpunit": "^9.3"
            },
            "suggest": {
                "ext-pcntl": "*"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "3.1-dev"
                }
            },
            "autoload": {
                "classmap": [
                    "src/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause"
            ],
            "authors": [
                {
                    "name": "Sebastian Bergmann",
                    "email": "sebastian@phpunit.de",
                    "role": "lead"
                }
            ],
            "description": "Invoke callables with a timeout",
            "homepage": "https://github.com/sebastianbergmann/php-invoker/",
            "keywords": [
                "process"
            ],
            "support": {
                "issues": "https://github.com/sebastianbergmann/php-invoker/issues",
                "source": "https://github.com/sebastianbergmann/php-invoker/tree/3.1.1"
            },
            "funding": [
                {
                    "url": "https://github.com/sebastianbergmann",
                    "type": "github"
                }
            ],
            "time": "2020-09-28T05:58:55+00:00"
        },
        {
            "name": "phpunit/php-text-template",
            "version": "2.0.4",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/php-text-template.git",
                "reference": "5da5f67fc95621df9ff4c4e5a84d6a8a2acf7c28"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/php-text-template/zipball/5da5f67fc95621df9ff4c4e5a84d6a8a2acf7c28",
                "reference": "5da5f67fc95621df9ff4c4e5a84d6a8a2acf7c28",
                "shasum": ""
            },
            "require": {
                "php": ">=7.3"
            },
            "require-dev": {
                "phpunit/phpunit": "^9.3"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "2.0-dev"
                }
            },
            "autoload": {
                "classmap": [
                    "src/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause"
            ],
            "authors": [
                {
                    "name": "Sebastian Bergmann",
                    "email": "sebastian@phpunit.de",
                    "role": "lead"
                }
            ],
            "description": "Simple template engine.",
            "homepage": "https://github.com/sebastianbergmann/php-text-template/",
            "keywords": [
                "template"
            ],
            "support": {
                "issues": "https://github.com/sebastianbergmann/php-text-template/issues",
                "source": "https://github.com/sebastianbergmann/php-text-template/tree/2.0.4"
            },
            "funding": [
                {
                    "url": "https://github.com/sebastianbergmann",
                    "type": "github"
                }
            ],
            "time": "2020-10-26T05:33:50+00:00"
        },
        {
            "name": "phpunit/php-timer",
            "version": "5.0.3",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/php-timer.git",
                "reference": "5a63ce20ed1b5bf577850e2c4e87f4aa902afbd2"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/php-timer/zipball/5a63ce20ed1b5bf577850e2c4e87f4aa902afbd2",
                "reference": "5a63ce20ed1b5bf577850e2c4e87f4aa902afbd2",
                "shasum": ""
            },
            "require": {
                "php": ">=7.3"
            },
            "require-dev": {
                "phpunit/phpunit": "^9.3"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "5.0-dev"
                }
            },
            "autoload": {
                "classmap": [
                    "src/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause"
            ],
            "authors": [
                {
                    "name": "Sebastian Bergmann",
                    "email": "sebastian@phpunit.de",
                    "role": "lead"
                }
            ],
            "description": "Utility class for timing",
            "homepage": "https://github.com/sebastianbergmann/php-timer/",
            "keywords": [
                "timer"
            ],
            "support": {
                "issues": "https://github.com/sebastianbergmann/php-timer/issues",
                "source": "https://github.com/sebastianbergmann/php-timer/tree/5.0.3"
            },
            "funding": [
                {
                    "url": "https://github.com/sebastianbergmann",
                    "type": "github"
                }
            ],
            "time": "2020-10-26T13:16:10+00:00"
        },
        {
            "name": "phpunit/phpunit",
            "version": "9.6.20",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/phpunit.git",
                "reference": "49d7820565836236411f5dc002d16dd689cde42f"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/phpunit/zipball/49d7820565836236411f5dc002d16dd689cde42f",
                "reference": "49d7820565836236411f5dc002d16dd689cde42f",
                "shasum": ""
            },
            "require": {
                "doctrine/instantiator": "^1.5.0 || ^2",
                "ext-dom": "*",
                "ext-json": "*",
                "ext-libxml": "*",
                "ext-mbstring": "*",
                "ext-xml": "*",
                "ext-xmlwriter": "*",
                "myclabs/deep-copy": "^1.12.0",
                "phar-io/manifest": "^2.0.4",
                "phar-io/version": "^3.2.1",
                "php": ">=7.3",
                "phpunit/php-code-coverage": "^9.2.31",
                "phpunit/php-file-iterator": "^3.0.6",
                "phpunit/php-invoker": "^3.1.1",
                "phpunit/php-text-template": "^2.0.4",
                "phpunit/php-timer": "^5.0.3",
                "sebastian/cli-parser": "^1.0.2",
                "sebastian/code-unit": "^1.0.8",
                "sebastian/comparator": "^4.0.8",
                "sebastian/diff": "^4.0.6",
                "sebastian/environment": "^5.1.5",
                "sebastian/exporter": "^4.0.6",
                "sebastian/global-state": "^5.0.7",
                "sebastian/object-enumerator": "^4.0.4",
                "sebastian/resource-operations": "^3.0.4",
                "sebastian/type": "^3.2.1",
                "sebastian/version": "^3.0.2"
            },
            "suggest": {
                "ext-soap": "To be able to generate mocks based on WSDL files",
                "ext-xdebug": "PHP extension that provides line coverage as well as branch and path coverage"
            },
            "bin": [
                "phpunit"
            ],
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "9.6-dev"
                }
            },
            "autoload": {
                "files": [
                    "src/Framework/Assert/Functions.php"
                ],
                "classmap": [
                    "src/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause"
            ],
            "authors": [
                {
                    "name": "Sebastian Bergmann",
                    "email": "sebastian@phpunit.de",
                    "role": "lead"
                }
            ],
            "description": "The PHP Unit Testing framework.",
            "homepage": "https://phpunit.de/",
            "keywords": [
                "phpunit",
                "testing",
                "xunit"
            ],
            "support": {
                "issues": "https://github.com/sebastianbergmann/phpunit/issues",
                "security": "https://github.com/sebastianbergmann/phpunit/security/policy",
                "source": "https://github.com/sebastianbergmann/phpunit/tree/9.6.20"
            },
            "funding": [
                {
                    "url": "https://phpunit.de/sponsors.html",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/sebastianbergmann",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/phpunit/phpunit",
                    "type": "tidelift"
                }
            ],
            "time": "2024-07-10T11:45:39+00:00"
        },
        {
            "name": "psalm/plugin-mockery",
            "version": "1.1.0",
            "source": {
                "type": "git",
                "url": "https://github.com/psalm/psalm-plugin-mockery.git",
                "reference": "876247d15f91df08240d00dac69c5135b6689283"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/psalm/psalm-plugin-mockery/zipball/876247d15f91df08240d00dac69c5135b6689283",
                "reference": "876247d15f91df08240d00dac69c5135b6689283",
                "shasum": ""
            },
            "require": {
                "composer/package-versions-deprecated": "^1.10",
                "composer/semver": "^1.4 || ^2.0 || ^3.0",
                "mockery/mockery": "^1.0",
                "php": "~7.4 || ~8.0 || ~8.1 || ~8.2",
                "vimeo/psalm": "dev-master || ^5.0@rc || ^5.0"
            },
            "require-dev": {
                "codeception/codeception": "^4.1.9",
                "phpunit/phpunit": "^9.0",
                "squizlabs/php_codesniffer": "^3.3.1",
                "weirdan/codeception-psalm-module": "^0.13.1"
            },
            "type": "psalm-plugin",
            "extra": {
                "psalm": {
                    "pluginClass": "Psalm\\MockeryPlugin\\Plugin"
                }
            },
            "autoload": {
                "psr-4": {
                    "Psalm\\MockeryPlugin\\": [
                        "."
                    ]
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Matt Brown",
                    "email": "github@muglug.com"
                }
            ],
            "description": "Psalm plugin for Mockery",
            "support": {
                "issues": "https://github.com/psalm/psalm-plugin-mockery/issues",
                "source": "https://github.com/psalm/psalm-plugin-mockery/tree/1.1.0"
            },
            "time": "2022-11-25T07:16:18+00:00"
        },
        {
            "name": "psalm/plugin-phpunit",
            "version": "0.18.4",
            "source": {
                "type": "git",
                "url": "https://github.com/psalm/psalm-plugin-phpunit.git",
                "reference": "e4ab3096653d9eb6f6d0ea5f4461898d59ae4dbc"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/psalm/psalm-plugin-phpunit/zipball/e4ab3096653d9eb6f6d0ea5f4461898d59ae4dbc",
                "reference": "e4ab3096653d9eb6f6d0ea5f4461898d59ae4dbc",
                "shasum": ""
            },
            "require": {
                "composer/package-versions-deprecated": "^1.10",
                "composer/semver": "^1.4 || ^2.0 || ^3.0",
                "ext-simplexml": "*",
                "php": "^7.1 || ^8.0",
                "vimeo/psalm": "dev-master || dev-4.x || ^4.7.1 || ^5@beta || ^5.0"
            },
            "conflict": {
                "phpunit/phpunit": "<7.5"
            },
            "require-dev": {
                "codeception/codeception": "^4.0.3",
                "php": "^7.3 || ^8.0",
                "phpunit/phpunit": "^7.5 || ^8.0 || ^9.0",
                "squizlabs/php_codesniffer": "^3.3.1",
                "weirdan/codeception-psalm-module": "^0.11.0",
                "weirdan/prophecy-shim": "^1.0 || ^2.0"
            },
            "type": "psalm-plugin",
            "extra": {
                "psalm": {
                    "pluginClass": "Psalm\\PhpUnitPlugin\\Plugin"
                }
            },
            "autoload": {
                "psr-4": {
                    "Psalm\\PhpUnitPlugin\\": "src"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Matt Brown",
                    "email": "github@muglug.com"
                }
            ],
            "description": "Psalm plugin for PHPUnit",
            "support": {
                "issues": "https://github.com/psalm/psalm-plugin-phpunit/issues",
                "source": "https://github.com/psalm/psalm-plugin-phpunit/tree/0.18.4"
            },
            "time": "2022-12-03T07:47:07+00:00"
        },
        {
            "name": "psalm/plugin-symfony",
            "version": "v5.2.5",
            "source": {
                "type": "git",
                "url": "https://github.com/psalm/psalm-plugin-symfony.git",
                "reference": "fb801a9b3d12ace9fb619febfaa3ae0bc1dbb196"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/psalm/psalm-plugin-symfony/zipball/fb801a9b3d12ace9fb619febfaa3ae0bc1dbb196",
                "reference": "fb801a9b3d12ace9fb619febfaa3ae0bc1dbb196",
                "shasum": ""
            },
            "require": {
                "ext-simplexml": "*",
                "php": "^8.1",
                "symfony/framework-bundle": "^5.0 || ^6.0 || ^7.0",
                "vimeo/psalm": "^5.16"
            },
            "require-dev": {
                "doctrine/annotations": "^1.8|^2",
                "doctrine/orm": "^2.9",
                "phpunit/phpunit": "~7.5 || ~9.5",
                "symfony/cache-contracts": "^1.0 || ^2.0",
                "symfony/console": "*",
                "symfony/form": "^5.0 || ^6.0 || ^7.0",
                "symfony/messenger": "^5.0 || ^6.0 || ^7.0",
                "symfony/security-core": "*",
                "symfony/serializer": "^5.0 || ^6.0 || ^7.0",
                "symfony/validator": "*",
                "twig/twig": "^2.10 || ^3.0",
                "weirdan/codeception-psalm-module": "dev-master"
            },
            "suggest": {
                "weirdan/doctrine-psalm-plugin": "If Doctrine is used, it is recommended install this plugin"
            },
            "type": "psalm-plugin",
            "extra": {
                "psalm": {
                    "pluginClass": "Psalm\\SymfonyPsalmPlugin\\Plugin"
                }
            },
            "autoload": {
                "psr-4": {
                    "Psalm\\SymfonyPsalmPlugin\\": "src"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Farhad Safarov",
                    "email": "farhad.safarov@gmail.com"
                }
            ],
            "description": "Psalm Plugin for Symfony",
            "support": {
                "issues": "https://github.com/psalm/psalm-plugin-symfony/issues",
                "source": "https://github.com/psalm/psalm-plugin-symfony/tree/v5.2.5"
            },
            "time": "2024-07-03T11:57:02+00:00"
        },
        {
            "name": "rector/rector",
            "version": "0.18.13",
            "source": {
                "type": "git",
                "url": "https://github.com/rectorphp/rector.git",
                "reference": "f8011a76d36aa4f839f60f3b4f97707d97176618"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/rectorphp/rector/zipball/f8011a76d36aa4f839f60f3b4f97707d97176618",
                "reference": "f8011a76d36aa4f839f60f3b4f97707d97176618",
                "shasum": ""
            },
            "require": {
                "php": "^7.2|^8.0",
                "phpstan/phpstan": "^1.10.35"
            },
            "conflict": {
                "rector/rector-doctrine": "*",
                "rector/rector-downgrade-php": "*",
                "rector/rector-phpunit": "*",
                "rector/rector-symfony": "*"
            },
            "bin": [
                "bin/rector"
            ],
            "type": "library",
            "autoload": {
                "files": [
                    "bootstrap.php"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "description": "Instant Upgrade and Automated Refactoring of any PHP code",
            "keywords": [
                "automation",
                "dev",
                "migration",
                "refactoring"
            ],
            "support": {
                "issues": "https://github.com/rectorphp/rector/issues",
                "source": "https://github.com/rectorphp/rector/tree/0.18.13"
            },
            "funding": [
                {
                    "url": "https://github.com/tomasvotruba",
                    "type": "github"
                }
            ],
            "time": "2023-12-20T16:08:01+00:00"
        },
        {
            "name": "roave/security-advisories",
            "version": "dev-master",
            "source": {
                "type": "git",
                "url": "https://github.com/Roave/SecurityAdvisories.git",
                "reference": "ff7456939acba6dd515a8a10aad66be6bc1b8dc1"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/Roave/SecurityAdvisories/zipball/ff7456939acba6dd515a8a10aad66be6bc1b8dc1",
                "reference": "ff7456939acba6dd515a8a10aad66be6bc1b8dc1",
                "shasum": ""
            },
            "conflict": {
                "3f/pygmentize": "<1.2",
                "admidio/admidio": "<4.3.10",
                "adodb/adodb-php": "<=5.20.20|>=5.21,<=5.21.3",
                "aheinze/cockpit": "<2.2",
                "aimeos/ai-admin-graphql": ">=2022.04.1,<2022.10.10|>=2023.04.1,<2023.10.6|>=2024.04.1,<2024.04.6",
                "aimeos/ai-admin-jsonadm": "<2020.10.13|>=2021.04.1,<2021.10.6|>=2022.04.1,<2022.10.3|>=2023.04.1,<2023.10.4|==2024.04.1",
                "aimeos/ai-client-html": ">=2020.04.1,<2020.10.27|>=2021.04.1,<2021.10.22|>=2022.04.1,<2022.10.13|>=2023.04.1,<2023.10.15|>=2024.04.1,<2024.04.7",
                "aimeos/ai-controller-frontend": "<2020.10.15|>=2021.04.1,<2021.10.8|>=2022.04.1,<2022.10.8|>=2023.04.1,<2023.10.9",
                "aimeos/aimeos-core": ">=2022.04.1,<2022.10.17|>=2023.04.1,<2023.10.17|>=2024.04.1,<2024.04.7",
                "aimeos/aimeos-typo3": "<19.10.12|>=20,<20.10.5",
                "airesvsg/acf-to-rest-api": "<=3.1",
                "akaunting/akaunting": "<2.1.13",
                "akeneo/pim-community-dev": "<5.0.119|>=6,<6.0.53",
                "alextselegidis/easyappointments": "<1.5",
                "alterphp/easyadmin-extension-bundle": ">=1.2,<1.2.11|>=1.3,<1.3.1",
                "amazing/media2click": ">=1,<1.3.3",
                "amphp/artax": "<1.0.6|>=2,<2.0.6",
                "amphp/http": "<=1.7.2|>=2,<=2.1",
                "amphp/http-client": ">=4,<4.4",
                "anchorcms/anchor-cms": "<=0.12.7",
                "andreapollastri/cipi": "<=3.1.15",
                "andrewhaine/silverstripe-form-capture": ">=0.2,<=0.2.3|>=1,<1.0.2|>=2,<2.2.5",
                "apache-solr-for-typo3/solr": "<2.8.3",
                "apereo/phpcas": "<1.6",
                "api-platform/core": ">=2.2,<2.2.10|>=2.3,<2.3.6|>=2.6,<2.7.10|>=3,<3.0.12|>=3.1,<3.1.3",
                "appwrite/server-ce": "<=1.2.1",
                "arc/web": "<3",
                "area17/twill": "<1.2.5|>=2,<2.5.3",
                "artesaos/seotools": "<0.17.2",
                "asymmetricrypt/asymmetricrypt": "<9.9.99",
                "athlon1600/php-proxy": "<=5.1",
                "athlon1600/php-proxy-app": "<=3",
                "austintoddj/canvas": "<=3.4.2",
                "auth0/wordpress": "<=4.6",
                "automad/automad": "<=2.0.0.0-alpha5",
                "automattic/jetpack": "<9.8",
                "awesome-support/awesome-support": "<=6.0.7",
                "aws/aws-sdk-php": "<3.288.1",
                "azuracast/azuracast": "<0.18.3",
                "backdrop/backdrop": "<1.27.3|>=1.28,<1.28.2",
                "backpack/crud": "<3.4.9",
                "bacula-web/bacula-web": "<8.0.0.0-RC2-dev",
                "badaso/core": "<2.7",
                "bagisto/bagisto": "<2.1",
                "barrelstrength/sprout-base-email": "<1.2.7",
                "barrelstrength/sprout-forms": "<3.9",
                "barryvdh/laravel-translation-manager": "<0.6.2",
                "barzahlen/barzahlen-php": "<2.0.1",
                "baserproject/basercms": "<5.0.9",
                "bassjobsen/bootstrap-3-typeahead": ">4.0.2",
                "bbpress/bbpress": "<2.6.5",
                "bcosca/fatfree": "<3.7.2",
                "bedita/bedita": "<4",
                "bigfork/silverstripe-form-capture": ">=3,<3.1.1",
                "billz/raspap-webgui": "<=3.1.4",
                "bk2k/bootstrap-package": ">=7.1,<7.1.2|>=8,<8.0.8|>=9,<9.0.4|>=9.1,<9.1.3|>=10,<10.0.10|>=11,<11.0.3",
                "blueimp/jquery-file-upload": "==6.4.4",
                "bmarshall511/wordpress_zero_spam": "<5.2.13",
                "bolt/bolt": "<3.7.2",
                "bolt/core": "<=4.2",
                "born05/craft-twofactorauthentication": "<3.3.4",
                "bottelet/flarepoint": "<2.2.1",
                "bref/bref": "<2.1.17",
                "brightlocal/phpwhois": "<=4.2.5",
                "brotkrueml/codehighlight": "<2.7",
                "brotkrueml/schema": "<1.13.1|>=2,<2.5.1",
                "brotkrueml/typo3-matomo-integration": "<1.3.2",
                "buddypress/buddypress": "<7.2.1",
                "bugsnag/bugsnag-laravel": ">=2,<2.0.2",
                "bytefury/crater": "<6.0.2",
                "cachethq/cachet": "<2.5.1",
                "cakephp/cakephp": "<3.10.3|>=4,<4.0.10|>=4.1,<4.1.4|>=4.2,<4.2.12|>=4.3,<4.3.11|>=4.4,<4.4.10",
                "cakephp/database": ">=4.2,<4.2.12|>=4.3,<4.3.11|>=4.4,<4.4.10",
                "cardgate/magento2": "<2.0.33",
                "cardgate/woocommerce": "<=3.1.15",
                "cart2quote/module-quotation": ">=4.1.6,<=4.4.5|>=5,<5.4.4",
                "cart2quote/module-quotation-encoded": ">=4.1.6,<=4.4.5|>=5,<5.4.4",
                "cartalyst/sentry": "<=2.1.6",
                "catfan/medoo": "<1.7.5",
                "causal/oidc": "<2.1",
                "cecil/cecil": "<7.47.1",
                "centreon/centreon": "<22.10.15",
                "cesnet/simplesamlphp-module-proxystatistics": "<3.1",
                "chriskacerguis/codeigniter-restserver": "<=2.7.1",
                "civicrm/civicrm-core": ">=4.2,<4.2.9|>=4.3,<4.3.3",
                "ckeditor/ckeditor": "<4.24",
                "cockpit-hq/cockpit": "<2.7|==2.7",
                "codeception/codeception": "<3.1.3|>=4,<4.1.22",
                "codeigniter/framework": "<3.1.9",
                "codeigniter4/framework": "<4.4.7",
                "codeigniter4/shield": "<1.0.0.0-beta8",
                "codiad/codiad": "<=2.8.4",
                "composer/composer": "<1.10.27|>=2,<2.2.24|>=2.3,<2.7.7",
                "concrete5/concrete5": "<=9.3.2",
                "concrete5/core": "<8.5.8|>=9,<9.1",
                "contao-components/mediaelement": ">=2.14.2,<2.21.1",
                "contao/comments-bundle": ">=2,<4.13.40|>=5.0.0.0-RC1-dev,<5.3.4",
                "contao/contao": ">=3,<3.5.37|>=4,<4.4.56|>=4.5,<4.9.40|>=4.10,<4.11.7|>=4.13,<4.13.21|>=5.1,<5.1.4",
                "contao/core": "<3.5.39",
                "contao/core-bundle": "<4.13.40|>=5,<5.3.4",
                "contao/listing-bundle": ">=3,<=3.5.30|>=4,<4.4.8",
                "contao/managed-edition": "<=1.5",
                "corveda/phpsandbox": "<1.3.5",
                "cosenary/instagram": "<=2.3",
                "craftcms/cms": "<4.6.2|>=5.0.0.0-beta1,<=5.2.2",
                "croogo/croogo": "<4",
                "cuyz/valinor": "<0.12",
                "czproject/git-php": "<4.0.3",
                "dapphp/securimage": "<3.6.6",
                "darylldoyle/safe-svg": "<1.9.10",
                "datadog/dd-trace": ">=0.30,<0.30.2",
                "datatables/datatables": "<1.10.10",
                "david-garcia/phpwhois": "<=4.3.1",
                "dbrisinajumi/d2files": "<1",
                "dcat/laravel-admin": "<=2.1.3.0-beta",
                "derhansen/fe_change_pwd": "<2.0.5|>=3,<3.0.3",
                "derhansen/sf_event_mgt": "<4.3.1|>=5,<5.1.1|>=7,<7.4",
                "desperado/xml-bundle": "<=0.1.7",
                "devgroup/dotplant": "<2020.09.14-dev",
                "directmailteam/direct-mail": "<6.0.3|>=7,<7.0.3|>=8,<9.5.2",
                "doctrine/annotations": "<1.2.7",
                "doctrine/cache": ">=1,<1.3.2|>=1.4,<1.4.2",
                "doctrine/common": "<2.4.3|>=2.5,<2.5.1",
                "doctrine/dbal": ">=2,<2.0.8|>=2.1,<2.1.2|>=3,<3.1.4",
                "doctrine/doctrine-bundle": "<1.5.2",
                "doctrine/doctrine-module": "<0.7.2",
                "doctrine/mongodb-odm": "<1.0.2",
                "doctrine/mongodb-odm-bundle": "<3.0.1",
                "doctrine/orm": ">=1,<1.2.4|>=2,<2.4.8|>=2.5,<2.5.1|>=2.8.3,<2.8.4",
                "dolibarr/dolibarr": "<19.0.2",
                "dompdf/dompdf": "<2.0.4",
                "doublethreedigital/guest-entries": "<3.1.2",
                "drupal/core": ">=6,<6.38|>=7,<7.96|>=8,<10.1.8|>=10.2,<10.2.2",
                "drupal/drupal": ">=5,<5.11|>=6,<6.38|>=7,<7.80|>=8,<8.9.16|>=9,<9.1.12|>=9.2,<9.2.4",
                "duncanmcclean/guest-entries": "<3.1.2",
                "dweeves/magmi": "<=0.7.24",
                "ec-cube/ec-cube": "<2.4.4|>=2.11,<=2.17.1|>=3,<=3.0.18.0-patch4|>=4,<=4.1.2",
                "ecodev/newsletter": "<=4",
                "ectouch/ectouch": "<=2.7.2",
                "egroupware/egroupware": "<23.1.20240624",
                "elefant/cms": "<2.0.7",
                "elgg/elgg": "<3.3.24|>=4,<4.0.5",
                "elijaa/phpmemcacheadmin": "<=1.3",
                "encore/laravel-admin": "<=1.8.19",
                "endroid/qr-code-bundle": "<3.4.2",
                "enhavo/enhavo-app": "<=0.13.1",
                "enshrined/svg-sanitize": "<0.15",
                "erusev/parsedown": "<1.7.2",
                "ether/logs": "<3.0.4",
                "evolutioncms/evolution": "<=3.2.3",
                "exceedone/exment": "<4.4.3|>=5,<5.0.3",
                "exceedone/laravel-admin": "<2.2.3|==3",
                "ezsystems/demobundle": ">=5.4,<5.4.6.1-dev",
                "ezsystems/ez-support-tools": ">=2.2,<2.2.3",
                "ezsystems/ezdemo-ls-extension": ">=5.4,<5.4.2.1-dev",
                "ezsystems/ezfind-ls": ">=5.3,<5.3.6.1-dev|>=5.4,<5.4.11.1-dev|>=2017.12,<2017.12.0.1-dev",
                "ezsystems/ezplatform": "<=1.13.6|>=2,<=2.5.24",
                "ezsystems/ezplatform-admin-ui": ">=1.3,<1.3.5|>=1.4,<1.4.6|>=1.5,<1.5.29|>=2.3,<2.3.26|>=3.3,<3.3.39",
                "ezsystems/ezplatform-admin-ui-assets": ">=4,<4.2.1|>=5,<5.0.1|>=5.1,<5.1.1",
                "ezsystems/ezplatform-graphql": ">=1.0.0.0-RC1-dev,<1.0.13|>=2.0.0.0-beta1,<2.3.12",
                "ezsystems/ezplatform-kernel": "<1.2.5.1-dev|>=1.3,<1.3.35",
                "ezsystems/ezplatform-rest": ">=1.2,<=1.2.2|>=1.3,<1.3.8",
                "ezsystems/ezplatform-richtext": ">=2.3,<2.3.7.1-dev",
                "ezsystems/ezplatform-solr-search-engine": ">=1.7,<1.7.12|>=2,<2.0.2|>=3.3,<3.3.15",
                "ezsystems/ezplatform-user": ">=1,<1.0.1",
                "ezsystems/ezpublish-kernel": "<6.13.8.2-dev|>=7,<7.5.31",
                "ezsystems/ezpublish-legacy": "<=2017.12.7.3|>=2018.6,<=2019.03.5.1",
                "ezsystems/platform-ui-assets-bundle": ">=4.2,<4.2.3",
                "ezsystems/repository-forms": ">=2.3,<2.3.2.1-dev|>=2.5,<2.5.15",
                "ezyang/htmlpurifier": "<4.1.1",
                "facade/ignition": "<1.16.15|>=2,<2.4.2|>=2.5,<2.5.2",
                "facturascripts/facturascripts": "<=2022.08",
                "fastly/magento2": "<1.2.26",
                "feehi/cms": "<=2.1.1",
                "feehi/feehicms": "<=2.1.1",
                "fenom/fenom": "<=2.12.1",
                "filegator/filegator": "<7.8",
                "filp/whoops": "<2.1.13",
                "fineuploader/php-traditional-server": "<=1.2.2",
                "firebase/php-jwt": "<6",
                "fisharebest/webtrees": "<=2.1.18",
                "fixpunkt/fp-masterquiz": "<2.2.1|>=3,<3.5.2",
                "fixpunkt/fp-newsletter": "<1.1.1|>=2,<2.1.2|>=2.2,<3.2.6",
                "flarum/core": "<1.8.5",
                "flarum/flarum": "<0.1.0.0-beta8",
                "flarum/framework": "<1.8.5",
                "flarum/mentions": "<1.6.3",
                "flarum/sticky": ">=0.1.0.0-beta14,<=0.1.0.0-beta15",
                "flarum/tags": "<=0.1.0.0-beta13",
                "floriangaerber/magnesium": "<0.3.1",
                "fluidtypo3/vhs": "<5.1.1",
                "fof/byobu": ">=0.3.0.0-beta2,<1.1.7",
                "fof/upload": "<1.2.3",
                "foodcoopshop/foodcoopshop": ">=3.2,<3.6.1",
                "fooman/tcpdf": "<6.2.22",
                "forkcms/forkcms": "<5.11.1",
                "fossar/tcpdf-parser": "<6.2.22",
                "francoisjacquet/rosariosis": "<=11.5.1",
                "frappant/frp-form-answers": "<3.1.2|>=4,<4.0.2",
                "friendsofsymfony/oauth2-php": "<1.3",
                "friendsofsymfony/rest-bundle": ">=1.2,<1.2.2",
                "friendsofsymfony/user-bundle": ">=1,<1.3.5",
                "friendsofsymfony1/swiftmailer": ">=4,<5.4.13|>=6,<6.2.5",
                "friendsofsymfony1/symfony1": ">=1.1,<1.5.19",
                "friendsoftypo3/mediace": ">=7.6.2,<7.6.5",
                "friendsoftypo3/openid": ">=4.5,<4.5.31|>=4.7,<4.7.16|>=6,<6.0.11|>=6.1,<6.1.6",
                "froala/wysiwyg-editor": "<3.2.7|>=4.0.1,<=4.1.3",
                "froxlor/froxlor": "<2.1.9",
                "frozennode/administrator": "<=5.0.12",
                "fuel/core": "<1.8.1",
                "funadmin/funadmin": "<=3.2|>=3.3.2,<=3.3.3",
                "gaoming13/wechat-php-sdk": "<=1.10.2",
                "genix/cms": "<=1.1.11",
                "getformwork/formwork": "<1.13.1|==2.0.0.0-beta1",
                "getgrav/grav": "<1.7.46",
                "getkirby/cms": "<4.1.1",
                "getkirby/kirby": "<=2.5.12",
                "getkirby/panel": "<2.5.14",
                "getkirby/starterkit": "<=3.7.0.2",
                "gilacms/gila": "<=1.15.4",
                "gleez/cms": "<=1.3|==2",
                "globalpayments/php-sdk": "<2",
                "gogentooss/samlbase": "<1.2.7",
                "google/protobuf": "<3.15",
                "gos/web-socket-bundle": "<1.10.4|>=2,<2.6.1|>=3,<3.3",
                "gree/jose": "<2.2.1",
                "gregwar/rst": "<1.0.3",
                "grumpydictator/firefly-iii": "<6.1.17",
                "gugoan/economizzer": "<=0.9.0.0-beta1",
                "guzzlehttp/guzzle": "<6.5.8|>=7,<7.4.5",
                "guzzlehttp/psr7": "<1.9.1|>=2,<2.4.5",
                "haffner/jh_captcha": "<=2.1.3|>=3,<=3.0.2",
                "harvesthq/chosen": "<1.8.7",
                "helloxz/imgurl": "<=2.31",
                "hhxsv5/laravel-s": "<3.7.36",
                "hillelcoren/invoice-ninja": "<5.3.35",
                "himiklab/yii2-jqgrid-widget": "<1.0.8",
                "hjue/justwriting": "<=1",
                "hov/jobfair": "<1.0.13|>=2,<2.0.2",
                "httpsoft/http-message": "<1.0.12",
                "hyn/multi-tenant": ">=5.6,<5.7.2",
                "ibexa/admin-ui": ">=4.2,<4.2.3|>=4.6.0.0-beta1,<4.6.9",
                "ibexa/core": ">=4,<4.0.7|>=4.1,<4.1.4|>=4.2,<4.2.3|>=4.5,<4.5.6|>=4.6,<4.6.2",
                "ibexa/graphql": ">=2.5,<2.5.31|>=3.3,<3.3.28|>=4.2,<4.2.3",
                "ibexa/post-install": "<=1.0.4",
                "ibexa/solr": ">=4.5,<4.5.4",
                "ibexa/user": ">=4,<4.4.3",
                "icecoder/icecoder": "<=8.1",
                "idno/known": "<=1.3.1",
                "ilicmiljan/secure-props": ">=1.2,<1.2.2",
                "illuminate/auth": "<5.5.10",
                "illuminate/cookie": ">=4,<=4.0.11|>=4.1,<6.18.31|>=7,<7.22.4",
                "illuminate/database": "<6.20.26|>=7,<7.30.5|>=8,<8.40",
                "illuminate/encryption": ">=4,<=4.0.11|>=4.1,<=4.1.31|>=4.2,<=4.2.22|>=5,<=5.0.35|>=5.1,<=5.1.46|>=5.2,<=5.2.45|>=5.3,<=5.3.31|>=5.4,<=5.4.36|>=5.5,<5.5.40|>=5.6,<5.6.15",
                "illuminate/view": "<6.20.42|>=7,<7.30.6|>=8,<8.75",
                "imdbphp/imdbphp": "<=5.1.1",
                "impresscms/impresscms": "<=1.4.5",
                "impresspages/impresspages": "<=1.0.12",
                "in2code/femanager": "<5.5.3|>=6,<6.3.4|>=7,<7.2.3",
                "in2code/ipandlanguageredirect": "<5.1.2",
                "in2code/lux": "<17.6.1|>=18,<24.0.2",
                "innologi/typo3-appointments": "<2.0.6",
                "intelliants/subrion": "<4.2.2",
                "inter-mediator/inter-mediator": "==5.5",
                "ipl/web": "<0.10.1",
                "islandora/islandora": ">=2,<2.4.1",
                "ivankristianto/phpwhois": "<=4.3",
                "jackalope/jackalope-doctrine-dbal": "<1.7.4",
                "james-heinrich/getid3": "<1.9.21",
                "james-heinrich/phpthumb": "<1.7.12",
                "jasig/phpcas": "<1.3.3",
                "jcbrand/converse.js": "<3.3.3",
                "johnbillion/wp-crontrol": "<1.16.2",
                "joomla/application": "<1.0.13",
                "joomla/archive": "<1.1.12|>=2,<2.0.1",
                "joomla/filesystem": "<1.6.2|>=2,<2.0.1",
                "joomla/filter": "<1.4.4|>=2,<2.0.1",
                "joomla/framework": "<1.5.7|>=2.5.4,<=3.8.12",
                "joomla/input": ">=2,<2.0.2",
                "joomla/joomla-cms": ">=2.5,<3.9.12",
                "joomla/session": "<1.3.1",
                "joyqi/hyper-down": "<=2.4.27",
                "jsdecena/laracom": "<2.0.9",
                "jsmitty12/phpwhois": "<5.1",
                "juzaweb/cms": "<=3.4",
                "jweiland/events2": "<8.3.8|>=9,<9.0.6",
                "kazist/phpwhois": "<=4.2.6",
                "kelvinmo/simplexrd": "<3.1.1",
                "kevinpapst/kimai2": "<1.16.7",
                "khodakhah/nodcms": "<=3",
                "kimai/kimai": "<2.16",
                "kitodo/presentation": "<3.2.3|>=3.3,<3.3.4",
                "klaviyo/magento2-extension": ">=1,<3",
                "knplabs/knp-snappy": "<=1.4.2",
                "kohana/core": "<3.3.3",
                "krayin/laravel-crm": "<1.2.2",
                "kreait/firebase-php": ">=3.2,<3.8.1",
                "kumbiaphp/kumbiapp": "<=1.1.1",
                "la-haute-societe/tcpdf": "<6.2.22",
                "laminas/laminas-diactoros": "<2.18.1|==2.19|==2.20|==2.21|==2.22|==2.23|>=2.24,<2.24.2|>=2.25,<2.25.2",
                "laminas/laminas-form": "<2.17.1|>=3,<3.0.2|>=3.1,<3.1.1",
                "laminas/laminas-http": "<2.14.2",
                "laravel/fortify": "<1.11.1",
                "laravel/framework": "<6.20.44|>=7,<7.30.6|>=8,<8.75",
                "laravel/laravel": ">=5.4,<5.4.22",
                "laravel/socialite": ">=1,<2.0.10",
                "latte/latte": "<2.10.8",
                "lavalite/cms": "<=9|==10.1",
                "lcobucci/jwt": ">=3.4,<3.4.6|>=4,<4.0.4|>=4.1,<4.1.5",
                "league/commonmark": "<0.18.3",
                "league/flysystem": "<1.1.4|>=2,<2.1.1",
                "league/oauth2-server": ">=8.3.2,<8.4.2|>=8.5,<8.5.3",
                "lexik/jwt-authentication-bundle": "<2.10.7|>=2.11,<2.11.3",
                "libreform/libreform": ">=2,<=2.0.8",
                "librenms/librenms": "<2017.08.18",
                "liftkit/database": "<2.13.2",
                "lightsaml/lightsaml": "<1.3.5",
                "limesurvey/limesurvey": "<3.27.19",
                "livehelperchat/livehelperchat": "<=3.91",
                "livewire/livewire": ">2.2.4,<2.2.6|>=3.3.5,<3.4.9",
                "lms/routes": "<2.1.1",
                "localizationteam/l10nmgr": "<7.4|>=8,<8.7|>=9,<9.2",
                "luyadev/yii-helpers": "<1.2.1",
                "magento/community-edition": "<2.4.5|==2.4.5|>=2.4.5.0-patch1,<2.4.5.0-patch8|==2.4.6|>=2.4.6.0-patch1,<2.4.6.0-patch6|==2.4.7",
                "magento/core": "<=1.9.4.5",
                "magento/magento1ce": "<1.9.4.3-dev",
                "magento/magento1ee": ">=1,<1.14.4.3-dev",
                "magento/product-community-edition": "<2.4.4.0-patch9|>=2.4.5,<2.4.5.0-patch8|>=2.4.6,<2.4.6.0-patch6|>=2.4.7,<2.4.7.0-patch1",
                "magneto/core": "<1.9.4.4-dev",
                "maikuolan/phpmussel": ">=1,<1.6",
                "mainwp/mainwp": "<=4.4.3.3",
                "mantisbt/mantisbt": "<2.26.2",
                "marcwillmann/turn": "<0.3.3",
                "matyhtf/framework": "<3.0.6",
                "mautic/core": "<4.4.12|>=5.0.0.0-alpha,<5.0.4",
                "mdanter/ecc": "<2",
                "mediawiki/core": "<1.36.2",
                "mediawiki/matomo": "<2.4.3",
                "mediawiki/semantic-media-wiki": "<4.0.2",
                "melisplatform/melis-asset-manager": "<5.0.1",
                "melisplatform/melis-cms": "<5.0.1",
                "melisplatform/melis-front": "<5.0.1",
                "mezzio/mezzio-swoole": "<3.7|>=4,<4.3",
                "mgallegos/laravel-jqgrid": "<=1.3",
                "microsoft/microsoft-graph": ">=1.16,<1.109.1|>=2,<2.0.1",
                "microsoft/microsoft-graph-beta": "<2.0.1",
                "microsoft/microsoft-graph-core": "<2.0.2",
                "microweber/microweber": "<=2.0.4",
                "mikehaertl/php-shellcommand": "<1.6.1",
                "miniorange/miniorange-saml": "<1.4.3",
                "mittwald/typo3_forum": "<1.2.1",
                "mobiledetect/mobiledetectlib": "<2.8.32",
                "modx/revolution": "<=2.8.3.0-patch",
                "mojo42/jirafeau": "<4.4",
                "mongodb/mongodb": ">=1,<1.9.2",
                "monolog/monolog": ">=1.8,<1.12",
                "moodle/moodle": "<4.3.5|>=4.4.0.0-beta,<4.4.1",
                "mos/cimage": "<0.7.19",
                "movim/moxl": ">=0.8,<=0.10",
                "movingbytes/social-network": "<=1.2.1",
                "mpdf/mpdf": "<=7.1.7",
                "munkireport/comment": "<4.1",
                "munkireport/managedinstalls": "<2.6",
                "munkireport/munki_facts": "<1.5",
                "munkireport/munkireport": ">=2.5.3,<5.6.3",
                "munkireport/reportdata": "<3.5",
                "munkireport/softwareupdate": "<1.6",
                "mustache/mustache": ">=2,<2.14.1",
                "namshi/jose": "<2.2",
                "neoan3-apps/template": "<1.1.1",
                "neorazorx/facturascripts": "<2022.04",
                "neos/flow": ">=1,<1.0.4|>=1.1,<1.1.1|>=2,<2.0.1|>=2.3,<2.3.16|>=3,<3.0.12|>=3.1,<3.1.10|>=3.2,<3.2.13|>=3.3,<3.3.13|>=4,<4.0.6",
                "neos/form": ">=1.2,<4.3.3|>=5,<5.0.9|>=5.1,<5.1.3",
                "neos/media-browser": "<7.3.19|>=8,<8.0.16|>=8.1,<8.1.11|>=8.2,<8.2.11|>=8.3,<8.3.9",
                "neos/neos": ">=1.1,<1.1.3|>=1.2,<1.2.13|>=2,<2.0.4|>=2.3,<3.0.20|>=3.1,<3.1.18|>=3.2,<3.2.14|>=3.3,<5.3.10|>=7,<7.0.9|>=7.1,<7.1.7|>=7.2,<7.2.6|>=7.3,<7.3.4|>=8,<8.0.2",
                "neos/swiftmailer": "<5.4.5",
                "netgen/tagsbundle": ">=3.4,<3.4.11|>=4,<4.0.15",
                "nette/application": ">=2,<2.0.19|>=2.1,<2.1.13|>=2.2,<2.2.10|>=2.3,<2.3.14|>=2.4,<2.4.16|>=3,<3.0.6",
                "nette/nette": ">=2,<2.0.19|>=2.1,<2.1.13",
                "nilsteampassnet/teampass": "<3.0.10",
                "nonfiction/nterchange": "<4.1.1",
                "notrinos/notrinos-erp": "<=0.7",
                "noumo/easyii": "<=0.9",
                "novaksolutions/infusionsoft-php-sdk": "<1",
                "nukeviet/nukeviet": "<4.5.02",
                "nyholm/psr7": "<1.6.1",
                "nystudio107/craft-seomatic": "<3.4.12",
                "nzedb/nzedb": "<0.8",
                "nzo/url-encryptor-bundle": ">=4,<4.3.2|>=5,<5.0.1",
                "october/backend": "<1.1.2",
                "october/cms": "<1.0.469|==1.0.469|==1.0.471|==1.1.1",
                "october/october": "<=3.4.4",
                "october/rain": "<1.0.472|>=1.1,<1.1.2",
                "october/system": "<1.0.476|>=1.1,<1.1.12|>=2,<2.2.34|>=3,<3.5.15",
                "omeka/omeka-s": "<4.0.3",
                "onelogin/php-saml": "<2.10.4",
                "oneup/uploader-bundle": ">=1,<1.9.3|>=2,<2.1.5",
                "open-web-analytics/open-web-analytics": "<1.7.4",
                "opencart/opencart": ">=0",
                "openid/php-openid": "<2.3",
                "openmage/magento-lts": "<20.10.1",
                "opensolutions/vimbadmin": "<=3.0.15",
                "opensource-workshop/connect-cms": "<1.7.2|>=2,<2.3.2",
                "orchid/platform": ">=9,<9.4.4|>=14.0.0.0-alpha4,<14.5",
                "oro/calendar-bundle": ">=4.2,<=4.2.6|>=5,<=5.0.6|>=5.1,<5.1.1",
                "oro/commerce": ">=4.1,<5.0.11|>=5.1,<5.1.1",
                "oro/crm": ">=1.7,<1.7.4|>=3.1,<4.1.17|>=4.2,<4.2.7",
                "oro/crm-call-bundle": ">=4.2,<=4.2.5|>=5,<5.0.4|>=5.1,<5.1.1",
                "oro/customer-portal": ">=4.1,<=4.1.13|>=4.2,<=4.2.10|>=5,<=5.0.11|>=5.1,<=5.1.3",
                "oro/platform": ">=1.7,<1.7.4|>=3.1,<3.1.29|>=4.1,<4.1.17|>=4.2,<=4.2.10|>=5,<=5.0.12|>=5.1,<=5.1.3",
                "oveleon/contao-cookiebar": "<1.16.3|>=2,<2.1.3",
                "oxid-esales/oxideshop-ce": "<4.5",
                "oxid-esales/paymorrow-module": ">=1,<1.0.2|>=2,<2.0.1",
                "packbackbooks/lti-1-3-php-library": "<5",
                "padraic/humbug_get_contents": "<1.1.2",
                "pagarme/pagarme-php": "<3",
                "pagekit/pagekit": "<=1.0.18",
                "paragonie/ecc": "<2.0.1",
                "paragonie/random_compat": "<2",
                "passbolt/passbolt_api": "<4.6.2",
                "paypal/adaptivepayments-sdk-php": "<=3.9.2",
                "paypal/invoice-sdk-php": "<=3.9",
                "paypal/merchant-sdk-php": "<3.12",
                "paypal/permissions-sdk-php": "<=3.9.1",
                "pear/archive_tar": "<1.4.14",
                "pear/auth": "<1.2.4",
                "pear/crypt_gpg": "<1.6.7",
                "pear/pear": "<=1.10.1",
                "pegasus/google-for-jobs": "<1.5.1|>=2,<2.1.1",
                "personnummer/personnummer": "<3.0.2",
                "phanan/koel": "<5.1.4",
                "phenx/php-svg-lib": "<0.5.2",
                "php-censor/php-censor": "<2.0.13|>=2.1,<2.1.5",
                "php-mod/curl": "<2.3.2",
                "phpbb/phpbb": "<3.2.10|>=3.3,<3.3.1",
                "phpems/phpems": ">=6,<=6.1.3",
                "phpfastcache/phpfastcache": "<6.1.5|>=7,<7.1.2|>=8,<8.0.7",
                "phpmailer/phpmailer": "<6.5",
                "phpmussel/phpmussel": ">=1,<1.6",
                "phpmyadmin/phpmyadmin": "<5.2.1",
                "phpmyfaq/phpmyfaq": "<3.2.5|==3.2.5",
                "phpoffice/common": "<0.2.9",
                "phpoffice/phpexcel": "<1.8",
                "phpoffice/phpspreadsheet": "<1.16",
                "phpseclib/phpseclib": "<2.0.47|>=3,<3.0.36",
                "phpservermon/phpservermon": "<3.6",
                "phpsysinfo/phpsysinfo": "<3.4.3",
                "phpunit/phpunit": ">=4.8.19,<4.8.28|>=5.0.10,<5.6.3",
                "phpwhois/phpwhois": "<=4.2.5",
                "phpxmlrpc/extras": "<0.6.1",
                "phpxmlrpc/phpxmlrpc": "<4.9.2",
                "pi/pi": "<=2.5",
                "pimcore/admin-ui-classic-bundle": "<=1.5.1",
                "pimcore/customer-management-framework-bundle": "<4.0.6",
                "pimcore/data-hub": "<1.2.4",
                "pimcore/demo": "<10.3",
                "pimcore/ecommerce-framework-bundle": "<1.0.10",
                "pimcore/perspective-editor": "<1.5.1",
                "pimcore/pimcore": "<11.2.4",
                "pixelfed/pixelfed": "<0.11.11",
                "plotly/plotly.js": "<2.25.2",
                "pocketmine/bedrock-protocol": "<8.0.2",
                "pocketmine/pocketmine-mp": "<5.11.2",
                "pocketmine/raklib": ">=0.14,<0.14.6|>=0.15,<0.15.1",
                "pressbooks/pressbooks": "<5.18",
                "prestashop/autoupgrade": ">=4,<4.10.1",
                "prestashop/blockreassurance": "<=5.1.3",
                "prestashop/blockwishlist": ">=2,<2.1.1",
                "prestashop/contactform": ">=1.0.1,<4.3",
                "prestashop/gamification": "<2.3.2",
                "prestashop/prestashop": "<8.1.6",
                "prestashop/productcomments": "<5.0.2",
                "prestashop/ps_emailsubscription": "<2.6.1",
                "prestashop/ps_facetedsearch": "<3.4.1",
                "prestashop/ps_linklist": "<3.1",
                "privatebin/privatebin": "<1.4|>=1.5,<1.7.4",
                "processwire/processwire": "<=3.0.229",
                "propel/propel": ">=2.0.0.0-alpha1,<=2.0.0.0-alpha7",
                "propel/propel1": ">=1,<=1.7.1",
                "pterodactyl/panel": "<1.11.6",
                "ptheofan/yii2-statemachine": ">=2.0.0.0-RC1-dev,<=2",
                "ptrofimov/beanstalk_console": "<1.7.14",
                "pubnub/pubnub": "<6.1",
                "pusher/pusher-php-server": "<2.2.1",
                "pwweb/laravel-core": "<=0.3.6.0-beta",
                "pyrocms/pyrocms": "<=3.9.1",
                "qcubed/qcubed": "<=3.1.1",
                "quickapps/cms": "<=2.0.0.0-beta2",
                "rainlab/blog-plugin": "<1.4.1",
                "rainlab/debugbar-plugin": "<3.1",
                "rainlab/user-plugin": "<=1.4.5",
                "rankmath/seo-by-rank-math": "<=1.0.95",
                "rap2hpoutre/laravel-log-viewer": "<0.13",
                "react/http": ">=0.7,<1.9",
                "really-simple-plugins/complianz-gdpr": "<6.4.2",
                "redaxo/source": "<=5.15.1",
                "remdex/livehelperchat": "<4.29",
                "reportico-web/reportico": "<=8.1",
                "rhukster/dom-sanitizer": "<1.0.7",
                "rmccue/requests": ">=1.6,<1.8",
                "robrichards/xmlseclibs": ">=1,<3.0.4",
                "roots/soil": "<4.1",
                "rudloff/alltube": "<3.0.3",
                "s-cart/core": "<6.9",
                "s-cart/s-cart": "<6.9",
                "sabberworm/php-css-parser": ">=1,<1.0.1|>=2,<2.0.1|>=3,<3.0.1|>=4,<4.0.1|>=5,<5.0.9|>=5.1,<5.1.3|>=5.2,<5.2.1|>=6,<6.0.2|>=7,<7.0.4|>=8,<8.0.1|>=8.1,<8.1.1|>=8.2,<8.2.1|>=8.3,<8.3.1",
                "sabre/dav": ">=1.6,<1.7.11|>=1.8,<1.8.9",
                "scheb/two-factor-bundle": "<3.26|>=4,<4.11",
                "sensiolabs/connect": "<4.2.3",
                "serluck/phpwhois": "<=4.2.6",
                "sfroemken/url_redirect": "<=1.2.1",
                "sheng/yiicms": "<=1.2",
                "shopware/core": "<6.5.8.8-dev|>=6.6.0.0-RC1-dev,<6.6.1",
                "shopware/platform": "<6.5.8.8-dev|>=6.6.0.0-RC1-dev,<6.6.1",
                "shopware/production": "<=6.3.5.2",
                "shopware/shopware": "<=5.7.17",
                "shopware/storefront": "<=6.4.8.1|>=6.5.8,<6.5.8.7-dev",
                "shopxo/shopxo": "<=6.1",
                "showdoc/showdoc": "<2.10.4",
                "silverstripe-australia/advancedreports": ">=1,<=2",
                "silverstripe/admin": "<1.13.19|>=2,<2.1.8",
                "silverstripe/assets": ">=1,<1.11.1",
                "silverstripe/cms": "<4.11.3",
                "silverstripe/comments": ">=1.3,<3.1.1",
                "silverstripe/forum": "<=0.6.1|>=0.7,<=0.7.3",
                "silverstripe/framework": "<5.2.16",
                "silverstripe/graphql": ">=2,<2.0.5|>=3,<3.8.2|>=4,<4.3.7|>=5,<5.1.3",
                "silverstripe/hybridsessions": ">=1,<2.4.1|>=2.5,<2.5.1",
                "silverstripe/recipe-cms": ">=4.5,<4.5.3",
                "silverstripe/registry": ">=2.1,<2.1.2|>=2.2,<2.2.1",
                "silverstripe/reports": "<5.2.3",
                "silverstripe/restfulserver": ">=1,<1.0.9|>=2,<2.0.4|>=2.1,<2.1.2",
                "silverstripe/silverstripe-omnipay": "<2.5.2|>=3,<3.0.2|>=3.1,<3.1.4|>=3.2,<3.2.1",
                "silverstripe/subsites": ">=2,<2.6.1",
                "silverstripe/taxonomy": ">=1.3,<1.3.1|>=2,<2.0.1",
                "silverstripe/userforms": "<3|>=5,<5.4.2",
                "silverstripe/versioned-admin": ">=1,<1.11.1",
                "simple-updates/phpwhois": "<=1",
                "simplesamlphp/saml2": "<1.10.6|>=2,<2.3.8|>=3,<3.1.4|==5.0.0.0-alpha12",
                "simplesamlphp/simplesamlphp": "<1.18.6",
                "simplesamlphp/simplesamlphp-module-infocard": "<1.0.1",
                "simplesamlphp/simplesamlphp-module-openid": "<1",
                "simplesamlphp/simplesamlphp-module-openidprovider": "<0.9",
                "simplesamlphp/xml-security": "==1.6.11",
                "simplito/elliptic-php": "<1.0.6",
                "sitegeist/fluid-components": "<3.5",
                "sjbr/sr-freecap": "<2.4.6|>=2.5,<2.5.3",
                "slim/psr7": "<1.4.1|>=1.5,<1.5.1|>=1.6,<1.6.1",
                "slim/slim": "<2.6",
                "slub/slub-events": "<3.0.3",
                "smarty/smarty": "<4.5.3|>=5,<5.1.1",
                "snipe/snipe-it": "<6.4.2",
                "socalnick/scn-social-auth": "<1.15.2",
                "socialiteproviders/steam": "<1.1",
                "spatie/browsershot": "<3.57.4",
                "spatie/image-optimizer": "<1.7.3",
                "spipu/html2pdf": "<5.2.8",
                "spoon/library": "<1.4.1",
                "spoonity/tcpdf": "<6.2.22",
                "squizlabs/php_codesniffer": ">=1,<2.8.1|>=3,<3.0.1",
                "ssddanbrown/bookstack": "<24.05.1",
                "statamic/cms": "<4.46|>=5.3,<5.6.2",
                "stormpath/sdk": "<9.9.99",
                "studio-42/elfinder": "<=2.1.64",
                "studiomitte/friendlycaptcha": "<0.1.4",
                "subhh/libconnect": "<7.0.8|>=8,<8.1",
                "sukohi/surpass": "<1",
                "sulu/form-bundle": ">=2,<2.5.3",
                "sulu/sulu": "<1.6.44|>=2,<2.4.17|>=2.5,<2.5.13",
                "sumocoders/framework-user-bundle": "<1.4",
                "superbig/craft-audit": "<3.0.2",
                "swag/paypal": "<5.4.4",
                "swiftmailer/swiftmailer": "<6.2.5",
                "swiftyedit/swiftyedit": "<1.2",
                "sylius/admin-bundle": ">=1,<1.0.17|>=1.1,<1.1.9|>=1.2,<1.2.2",
                "sylius/grid": ">=1,<1.1.19|>=1.2,<1.2.18|>=1.3,<1.3.13|>=1.4,<1.4.5|>=1.5,<1.5.1",
                "sylius/grid-bundle": "<1.10.1",
                "sylius/paypal-plugin": ">=1,<1.2.4|>=1.3,<1.3.1",
                "sylius/resource-bundle": ">=1,<1.3.14|>=1.4,<1.4.7|>=1.5,<1.5.2|>=1.6,<1.6.4",
                "sylius/sylius": "<1.12.19|>=1.13.0.0-alpha1,<1.13.4",
                "symbiote/silverstripe-multivaluefield": ">=3,<3.1",
                "symbiote/silverstripe-queuedjobs": ">=3,<3.0.2|>=3.1,<3.1.4|>=4,<4.0.7|>=4.1,<4.1.2|>=4.2,<4.2.4|>=4.3,<4.3.3|>=4.4,<4.4.3|>=4.5,<4.5.1|>=4.6,<4.6.4",
                "symbiote/silverstripe-seed": "<6.0.3",
                "symbiote/silverstripe-versionedfiles": "<=2.0.3",
                "symfont/process": ">=0",
                "symfony/cache": ">=3.1,<3.4.35|>=4,<4.2.12|>=4.3,<4.3.8",
                "symfony/dependency-injection": ">=2,<2.0.17|>=2.7,<2.7.51|>=2.8,<2.8.50|>=3,<3.4.26|>=4,<4.1.12|>=4.2,<4.2.7",
                "symfony/error-handler": ">=4.4,<4.4.4|>=5,<5.0.4",
                "symfony/form": ">=2.3,<2.3.35|>=2.4,<2.6.12|>=2.7,<2.7.50|>=2.8,<2.8.49|>=3,<3.4.20|>=4,<4.0.15|>=4.1,<4.1.9|>=4.2,<4.2.1",
                "symfony/framework-bundle": ">=2,<2.3.18|>=2.4,<2.4.8|>=2.5,<2.5.2|>=2.7,<2.7.51|>=2.8,<2.8.50|>=3,<3.4.26|>=4,<4.1.12|>=4.2,<4.2.7|>=5.3.14,<5.3.15|>=5.4.3,<5.4.4|>=6.0.3,<6.0.4",
                "symfony/http-foundation": ">=2,<2.8.52|>=3,<3.4.35|>=4,<4.2.12|>=4.3,<4.3.8|>=4.4,<4.4.7|>=5,<5.0.7",
                "symfony/http-kernel": ">=2,<4.4.50|>=5,<5.4.20|>=6,<6.0.20|>=6.1,<6.1.12|>=6.2,<6.2.6",
                "symfony/intl": ">=2.7,<2.7.38|>=2.8,<2.8.31|>=3,<3.2.14|>=3.3,<3.3.13",
                "symfony/maker-bundle": ">=1.27,<1.29.2|>=1.30,<1.31.1",
                "symfony/mime": ">=4.3,<4.3.8",
                "symfony/phpunit-bridge": ">=2.8,<2.8.50|>=3,<3.4.26|>=4,<4.1.12|>=4.2,<4.2.7",
                "symfony/polyfill": ">=1,<1.10",
                "symfony/polyfill-php55": ">=1,<1.10",
                "symfony/proxy-manager-bridge": ">=2.7,<2.7.51|>=2.8,<2.8.50|>=3,<3.4.26|>=4,<4.1.12|>=4.2,<4.2.7",
                "symfony/routing": ">=2,<2.0.19",
                "symfony/security": ">=2,<2.7.51|>=2.8,<3.4.49|>=4,<4.4.24|>=5,<5.2.8",
                "symfony/security-bundle": ">=2,<4.4.50|>=5,<5.4.20|>=6,<6.0.20|>=6.1,<6.1.12|>=6.2,<6.2.6",
                "symfony/security-core": ">=2.4,<2.6.13|>=2.7,<2.7.9|>=2.7.30,<2.7.32|>=2.8,<3.4.49|>=4,<4.4.24|>=5,<5.2.9",
                "symfony/security-csrf": ">=2.4,<2.7.48|>=2.8,<2.8.41|>=3,<3.3.17|>=3.4,<3.4.11|>=4,<4.0.11",
                "symfony/security-guard": ">=2.8,<3.4.48|>=4,<4.4.23|>=5,<5.2.8",
                "symfony/security-http": ">=2.3,<2.3.41|>=2.4,<2.7.51|>=2.8,<2.8.50|>=3,<3.4.26|>=4,<4.2.12|>=4.3,<4.3.8|>=4.4,<4.4.7|>=5,<5.0.7|>=5.1,<5.2.8|>=5.3,<5.3.2|>=5.4,<5.4.31|>=6,<6.3.8",
                "symfony/serializer": ">=2,<2.0.11|>=4.1,<4.4.35|>=5,<5.3.12",
                "symfony/symfony": ">=2,<4.4.51|>=5,<5.4.31|>=6,<6.3.8",
                "symfony/translation": ">=2,<2.0.17",
                "symfony/twig-bridge": ">=2,<4.4.51|>=5,<5.4.31|>=6,<6.3.8",
                "symfony/ux-autocomplete": "<2.11.2",
                "symfony/validator": ">=2,<2.0.24|>=2.1,<2.1.12|>=2.2,<2.2.5|>=2.3,<2.3.3",
                "symfony/var-exporter": ">=4.2,<4.2.12|>=4.3,<4.3.8",
                "symfony/web-profiler-bundle": ">=2,<2.3.19|>=2.4,<2.4.9|>=2.5,<2.5.4",
                "symfony/webhook": ">=6.3,<6.3.8",
                "symfony/yaml": ">=2,<2.0.22|>=2.1,<2.1.7|>=2.2.0.0-beta1,<2.2.0.0-beta2",
                "symphonycms/symphony-2": "<2.6.4",
                "t3/dce": "<0.11.5|>=2.2,<2.6.2",
                "t3g/svg-sanitizer": "<1.0.3",
                "t3s/content-consent": "<1.0.3|>=2,<2.0.2",
                "tastyigniter/tastyigniter": "<3.3",
                "tcg/voyager": "<=1.4",
                "tecnickcom/tcpdf": "<=6.7.4",
                "terminal42/contao-tablelookupwizard": "<3.3.5",
                "thelia/backoffice-default-template": ">=2.1,<2.1.2",
                "thelia/thelia": ">=2.1,<2.1.3",
                "theonedemon/phpwhois": "<=4.2.5",
                "thinkcmf/thinkcmf": "<6.0.8",
                "thorsten/phpmyfaq": "<3.2.2",
                "tikiwiki/tiki-manager": "<=17.1",
                "timber/timber": ">=0.16.6,<1.23.1|>=1.24,<1.24.1|>=2,<2.1",
                "tinymce/tinymce": "<7.2",
                "tinymighty/wiki-seo": "<1.2.2",
                "titon/framework": "<9.9.99",
                "tobiasbg/tablepress": "<=2.0.0.0-RC1",
                "topthink/framework": "<6.0.17|>=6.1,<6.1.5|>=8,<8.0.4",
                "topthink/think": "<=6.1.1",
                "topthink/thinkphp": "<=3.2.3",
                "torrentpier/torrentpier": "<=2.4.3",
                "tpwd/ke_search": "<4.0.3|>=4.1,<4.6.6|>=5,<5.0.2",
                "tribalsystems/zenario": "<9.5.60602",
                "truckersmp/phpwhois": "<=4.3.1",
                "ttskch/pagination-service-provider": "<1",
                "twbs/bootstrap": "<=3.4.1|>=4,<=4.6.2",
                "twig/twig": "<1.44.7|>=2,<2.15.3|>=3,<3.4.3",
                "typo3/cms": "<9.5.29|>=10,<10.4.35|>=11,<11.5.23|>=12,<12.2",
                "typo3/cms-backend": "<4.1.14|>=4.2,<4.2.15|>=4.3,<4.3.7|>=4.4,<4.4.4|>=7,<=7.6.50|>=8,<=8.7.39|>=9,<=9.5.24|>=10,<=10.4.13|>=11,<=11.1",
                "typo3/cms-core": "<=8.7.56|>=9,<=9.5.47|>=10,<=10.4.44|>=11,<=11.5.36|>=12,<=12.4.14|>=13,<=13.1",
                "typo3/cms-extbase": "<6.2.24|>=7,<7.6.8|==8.1.1",
                "typo3/cms-fluid": "<4.3.4|>=4.4,<4.4.1",
                "typo3/cms-form": ">=8,<=8.7.39|>=9,<=9.5.24|>=10,<=10.4.13|>=11,<=11.1",
                "typo3/cms-frontend": "<4.3.9|>=4.4,<4.4.5",
                "typo3/cms-install": "<4.1.14|>=4.2,<4.2.16|>=4.3,<4.3.9|>=4.4,<4.4.5|>=12.2,<12.4.8",
                "typo3/cms-rte-ckeditor": ">=9.5,<9.5.42|>=10,<10.4.39|>=11,<11.5.30",
                "typo3/flow": ">=1,<1.0.4|>=1.1,<1.1.1|>=2,<2.0.1|>=2.3,<2.3.16|>=3,<3.0.12|>=3.1,<3.1.10|>=3.2,<3.2.13|>=3.3,<3.3.13|>=4,<4.0.6",
                "typo3/html-sanitizer": ">=1,<=1.5.2|>=2,<=2.1.3",
                "typo3/neos": ">=1.1,<1.1.3|>=1.2,<1.2.13|>=2,<2.0.4|>=2.3,<2.3.99|>=3,<3.0.20|>=3.1,<3.1.18|>=3.2,<3.2.14|>=3.3,<3.3.23|>=4,<4.0.17|>=4.1,<4.1.16|>=4.2,<4.2.12|>=4.3,<4.3.3",
                "typo3/phar-stream-wrapper": ">=1,<2.1.1|>=3,<3.1.1",
                "typo3/swiftmailer": ">=4.1,<4.1.99|>=5.4,<5.4.5",
                "typo3fluid/fluid": ">=2,<2.0.8|>=2.1,<2.1.7|>=2.2,<2.2.4|>=2.3,<2.3.7|>=2.4,<2.4.4|>=2.5,<2.5.11|>=2.6,<2.6.10",
                "ua-parser/uap-php": "<3.8",
                "uasoft-indonesia/badaso": "<=2.9.7",
                "unisharp/laravel-filemanager": "<2.6.4",
                "userfrosting/userfrosting": ">=0.3.1,<4.6.3",
                "usmanhalalit/pixie": "<1.0.3|>=2,<2.0.2",
                "uvdesk/community-skeleton": "<=1.1.1",
                "uvdesk/core-framework": "<=1.1.1",
                "vanilla/safecurl": "<0.9.2",
                "verbb/comments": "<1.5.5",
                "verbb/formie": "<2.1.6",
                "verbb/image-resizer": "<2.0.9",
                "verbb/knock-knock": "<1.2.8",
                "verot/class.upload.php": "<=2.1.6",
                "villagedefrance/opencart-overclocked": "<=1.11.1",
                "vova07/yii2-fileapi-widget": "<0.1.9",
                "vrana/adminer": "<4.8.1",
                "vufind/vufind": ">=2,<9.1.1",
                "waldhacker/hcaptcha": "<2.1.2",
                "wallabag/tcpdf": "<6.2.22",
                "wallabag/wallabag": "<2.6.7",
                "wanglelecc/laracms": "<=1.0.3",
                "web-auth/webauthn-framework": ">=3.3,<3.3.4|>=4.5,<4.9",
                "web-auth/webauthn-lib": ">=4.5,<4.9",
                "web-feet/coastercms": "==5.5",
                "webbuilders-group/silverstripe-kapost-bridge": "<0.4",
                "webcoast/deferred-image-processing": "<1.0.2",
                "webklex/laravel-imap": "<5.3",
                "webklex/php-imap": "<5.3",
                "webpa/webpa": "<3.1.2",
                "wikibase/wikibase": "<=1.39.3",
                "wikimedia/parsoid": "<0.12.2",
                "willdurand/js-translation-bundle": "<2.1.1",
                "winter/wn-backend-module": "<1.2.4",
                "winter/wn-dusk-plugin": "<2.1",
                "winter/wn-system-module": "<1.2.4",
                "wintercms/winter": "<=1.2.3",
                "woocommerce/woocommerce": "<6.6|>=8.8,<8.8.5|>=8.9,<8.9.3",
                "wp-cli/wp-cli": ">=0.12,<2.5",
                "wp-graphql/wp-graphql": "<=1.14.5",
                "wp-premium/gravityforms": "<2.4.21",
                "wpanel/wpanel4-cms": "<=4.3.1",
                "wpcloud/wp-stateless": "<3.2",
                "wpglobus/wpglobus": "<=1.9.6",
                "wwbn/avideo": "<14.3",
                "xataface/xataface": "<3",
                "xpressengine/xpressengine": "<3.0.15",
                "yab/quarx": "<2.4.5",
                "yeswiki/yeswiki": "<4.1",
                "yetiforce/yetiforce-crm": "<=6.4",
                "yidashi/yii2cmf": "<=2",
                "yii2mod/yii2-cms": "<1.9.2",
                "yiisoft/yii": "<1.1.29",
                "yiisoft/yii2": "<2.0.49.4-dev",
                "yiisoft/yii2-authclient": "<2.2.15",
                "yiisoft/yii2-bootstrap": "<2.0.4",
                "yiisoft/yii2-dev": "<2.0.43",
                "yiisoft/yii2-elasticsearch": "<2.0.5",
                "yiisoft/yii2-gii": "<=2.2.4",
                "yiisoft/yii2-jui": "<2.0.4",
                "yiisoft/yii2-redis": "<2.0.8",
                "yikesinc/yikes-inc-easy-mailchimp-extender": "<6.8.6",
                "yoast-seo-for-typo3/yoast_seo": "<7.2.3",
                "yourls/yourls": "<=1.8.2",
                "yuan1994/tpadmin": "<=1.3.12",
                "zencart/zencart": "<=1.5.7.0-beta",
                "zendesk/zendesk_api_client_php": "<2.2.11",
                "zendframework/zend-cache": ">=2.4,<2.4.8|>=2.5,<2.5.3",
                "zendframework/zend-captcha": ">=2,<2.4.9|>=2.5,<2.5.2",
                "zendframework/zend-crypt": ">=2,<2.4.9|>=2.5,<2.5.2",
                "zendframework/zend-db": "<2.2.10|>=2.3,<2.3.5",
                "zendframework/zend-developer-tools": ">=1.2.2,<1.2.3",
                "zendframework/zend-diactoros": "<1.8.4",
                "zendframework/zend-feed": "<2.10.3",
                "zendframework/zend-form": ">=2,<2.2.7|>=2.3,<2.3.1",
                "zendframework/zend-http": "<2.8.1",
                "zendframework/zend-json": ">=2.1,<2.1.6|>=2.2,<2.2.6",
                "zendframework/zend-ldap": ">=2,<2.0.99|>=2.1,<2.1.99|>=2.2,<2.2.8|>=2.3,<2.3.3",
                "zendframework/zend-mail": "<2.4.11|>=2.5,<2.7.2",
                "zendframework/zend-navigation": ">=2,<2.2.7|>=2.3,<2.3.1",
                "zendframework/zend-session": ">=2,<2.2.9|>=2.3,<2.3.4",
                "zendframework/zend-validator": ">=2.3,<2.3.6",
                "zendframework/zend-view": ">=2,<2.2.7|>=2.3,<2.3.1",
                "zendframework/zend-xmlrpc": ">=2.1,<2.1.6|>=2.2,<2.2.6",
                "zendframework/zendframework": "<=3",
                "zendframework/zendframework1": "<1.12.20",
                "zendframework/zendopenid": "<2.0.2",
                "zendframework/zendrest": "<2.0.2",
                "zendframework/zendservice-amazon": "<2.0.3",
                "zendframework/zendservice-api": "<1",
                "zendframework/zendservice-audioscrobbler": "<2.0.2",
                "zendframework/zendservice-nirvanix": "<2.0.2",
                "zendframework/zendservice-slideshare": "<2.0.2",
                "zendframework/zendservice-technorati": "<2.0.2",
                "zendframework/zendservice-windowsazure": "<2.0.2",
                "zendframework/zendxml": ">=1,<1.0.1",
                "zenstruck/collection": "<0.2.1",
                "zetacomponents/mail": "<1.8.2",
                "zf-commons/zfc-user": "<1.2.2",
                "zfcampus/zf-apigility-doctrine": ">=1,<1.0.3",
                "zfr/zfr-oauth2-server-module": "<0.1.2",
                "zoujingli/thinkadmin": "<=6.1.53"
            },
            "type": "metapackage",
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Marco Pivetta",
                    "email": "ocramius@gmail.com",
                    "role": "maintainer"
                },
                {
                    "name": "Ilya Tribusean",
                    "email": "slash3b@gmail.com",
                    "role": "maintainer"
                }
            ],
            "description": "Prevents installation of composer packages with known security vulnerabilities: no API, simply require it",
            "keywords": [
                "dev"
            ],
            "support": {
                "issues": "https://github.com/Roave/SecurityAdvisories/issues",
                "source": "https://github.com/Roave/SecurityAdvisories/tree/latest"
            },
            "funding": [
                {
                    "url": "https://github.com/Ocramius",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/roave/security-advisories",
                    "type": "tidelift"
                }
            ],
            "time": "2024-08-05T15:04:41+00:00"
        },
        {
            "name": "sebastian/cli-parser",
            "version": "1.0.2",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/cli-parser.git",
                "reference": "2b56bea83a09de3ac06bb18b92f068e60cc6f50b"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/cli-parser/zipball/2b56bea83a09de3ac06bb18b92f068e60cc6f50b",
                "reference": "2b56bea83a09de3ac06bb18b92f068e60cc6f50b",
                "shasum": ""
            },
            "require": {
                "php": ">=7.3"
            },
            "require-dev": {
                "phpunit/phpunit": "^9.3"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.0-dev"
                }
            },
            "autoload": {
                "classmap": [
                    "src/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause"
            ],
            "authors": [
                {
                    "name": "Sebastian Bergmann",
                    "email": "sebastian@phpunit.de",
                    "role": "lead"
                }
            ],
            "description": "Library for parsing CLI options",
            "homepage": "https://github.com/sebastianbergmann/cli-parser",
            "support": {
                "issues": "https://github.com/sebastianbergmann/cli-parser/issues",
                "source": "https://github.com/sebastianbergmann/cli-parser/tree/1.0.2"
            },
            "funding": [
                {
                    "url": "https://github.com/sebastianbergmann",
                    "type": "github"
                }
            ],
            "time": "2024-03-02T06:27:43+00:00"
        },
        {
            "name": "sebastian/code-unit",
            "version": "1.0.8",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/code-unit.git",
                "reference": "1fc9f64c0927627ef78ba436c9b17d967e68e120"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/code-unit/zipball/1fc9f64c0927627ef78ba436c9b17d967e68e120",
                "reference": "1fc9f64c0927627ef78ba436c9b17d967e68e120",
                "shasum": ""
            },
            "require": {
                "php": ">=7.3"
            },
            "require-dev": {
                "phpunit/phpunit": "^9.3"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.0-dev"
                }
            },
            "autoload": {
                "classmap": [
                    "src/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause"
            ],
            "authors": [
                {
                    "name": "Sebastian Bergmann",
                    "email": "sebastian@phpunit.de",
                    "role": "lead"
                }
            ],
            "description": "Collection of value objects that represent the PHP code units",
            "homepage": "https://github.com/sebastianbergmann/code-unit",
            "support": {
                "issues": "https://github.com/sebastianbergmann/code-unit/issues",
                "source": "https://github.com/sebastianbergmann/code-unit/tree/1.0.8"
            },
            "funding": [
                {
                    "url": "https://github.com/sebastianbergmann",
                    "type": "github"
                }
            ],
            "time": "2020-10-26T13:08:54+00:00"
        },
        {
            "name": "sebastian/code-unit-reverse-lookup",
            "version": "2.0.3",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/code-unit-reverse-lookup.git",
                "reference": "ac91f01ccec49fb77bdc6fd1e548bc70f7faa3e5"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/code-unit-reverse-lookup/zipball/ac91f01ccec49fb77bdc6fd1e548bc70f7faa3e5",
                "reference": "ac91f01ccec49fb77bdc6fd1e548bc70f7faa3e5",
                "shasum": ""
            },
            "require": {
                "php": ">=7.3"
            },
            "require-dev": {
                "phpunit/phpunit": "^9.3"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "2.0-dev"
                }
            },
            "autoload": {
                "classmap": [
                    "src/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause"
            ],
            "authors": [
                {
                    "name": "Sebastian Bergmann",
                    "email": "sebastian@phpunit.de"
                }
            ],
            "description": "Looks up which function or method a line of code belongs to",
            "homepage": "https://github.com/sebastianbergmann/code-unit-reverse-lookup/",
            "support": {
                "issues": "https://github.com/sebastianbergmann/code-unit-reverse-lookup/issues",
                "source": "https://github.com/sebastianbergmann/code-unit-reverse-lookup/tree/2.0.3"
            },
            "funding": [
                {
                    "url": "https://github.com/sebastianbergmann",
                    "type": "github"
                }
            ],
            "time": "2020-09-28T05:30:19+00:00"
        },
        {
            "name": "sebastian/comparator",
            "version": "4.0.8",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/comparator.git",
                "reference": "fa0f136dd2334583309d32b62544682ee972b51a"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/comparator/zipball/fa0f136dd2334583309d32b62544682ee972b51a",
                "reference": "fa0f136dd2334583309d32b62544682ee972b51a",
                "shasum": ""
            },
            "require": {
                "php": ">=7.3",
                "sebastian/diff": "^4.0",
                "sebastian/exporter": "^4.0"
            },
            "require-dev": {
                "phpunit/phpunit": "^9.3"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "4.0-dev"
                }
            },
            "autoload": {
                "classmap": [
                    "src/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause"
            ],
            "authors": [
                {
                    "name": "Sebastian Bergmann",
                    "email": "sebastian@phpunit.de"
                },
                {
                    "name": "Jeff Welch",
                    "email": "whatthejeff@gmail.com"
                },
                {
                    "name": "Volker Dusch",
                    "email": "github@wallbash.com"
                },
                {
                    "name": "Bernhard Schussek",
                    "email": "bschussek@2bepublished.at"
                }
            ],
            "description": "Provides the functionality to compare PHP values for equality",
            "homepage": "https://github.com/sebastianbergmann/comparator",
            "keywords": [
                "comparator",
                "compare",
                "equality"
            ],
            "support": {
                "issues": "https://github.com/sebastianbergmann/comparator/issues",
                "source": "https://github.com/sebastianbergmann/comparator/tree/4.0.8"
            },
            "funding": [
                {
                    "url": "https://github.com/sebastianbergmann",
                    "type": "github"
                }
            ],
            "time": "2022-09-14T12:41:17+00:00"
        },
        {
            "name": "sebastian/complexity",
            "version": "2.0.3",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/complexity.git",
                "reference": "25f207c40d62b8b7aa32f5ab026c53561964053a"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/complexity/zipball/25f207c40d62b8b7aa32f5ab026c53561964053a",
                "reference": "25f207c40d62b8b7aa32f5ab026c53561964053a",
                "shasum": ""
            },
            "require": {
                "nikic/php-parser": "^4.18 || ^5.0",
                "php": ">=7.3"
            },
            "require-dev": {
                "phpunit/phpunit": "^9.3"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "2.0-dev"
                }
            },
            "autoload": {
                "classmap": [
                    "src/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause"
            ],
            "authors": [
                {
                    "name": "Sebastian Bergmann",
                    "email": "sebastian@phpunit.de",
                    "role": "lead"
                }
            ],
            "description": "Library for calculating the complexity of PHP code units",
            "homepage": "https://github.com/sebastianbergmann/complexity",
            "support": {
                "issues": "https://github.com/sebastianbergmann/complexity/issues",
                "source": "https://github.com/sebastianbergmann/complexity/tree/2.0.3"
            },
            "funding": [
                {
                    "url": "https://github.com/sebastianbergmann",
                    "type": "github"
                }
            ],
            "time": "2023-12-22T06:19:30+00:00"
        },
        {
            "name": "sebastian/diff",
            "version": "4.0.6",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/diff.git",
                "reference": "ba01945089c3a293b01ba9badc29ad55b106b0bc"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/diff/zipball/ba01945089c3a293b01ba9badc29ad55b106b0bc",
                "reference": "ba01945089c3a293b01ba9badc29ad55b106b0bc",
                "shasum": ""
            },
            "require": {
                "php": ">=7.3"
            },
            "require-dev": {
                "phpunit/phpunit": "^9.3",
                "symfony/process": "^4.2 || ^5"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "4.0-dev"
                }
            },
            "autoload": {
                "classmap": [
                    "src/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause"
            ],
            "authors": [
                {
                    "name": "Sebastian Bergmann",
                    "email": "sebastian@phpunit.de"
                },
                {
                    "name": "Kore Nordmann",
                    "email": "mail@kore-nordmann.de"
                }
            ],
            "description": "Diff implementation",
            "homepage": "https://github.com/sebastianbergmann/diff",
            "keywords": [
                "diff",
                "udiff",
                "unidiff",
                "unified diff"
            ],
            "support": {
                "issues": "https://github.com/sebastianbergmann/diff/issues",
                "source": "https://github.com/sebastianbergmann/diff/tree/4.0.6"
            },
            "funding": [
                {
                    "url": "https://github.com/sebastianbergmann",
                    "type": "github"
                }
            ],
            "time": "2024-03-02T06:30:58+00:00"
        },
        {
            "name": "sebastian/environment",
            "version": "5.1.5",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/environment.git",
                "reference": "830c43a844f1f8d5b7a1f6d6076b784454d8b7ed"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/environment/zipball/830c43a844f1f8d5b7a1f6d6076b784454d8b7ed",
                "reference": "830c43a844f1f8d5b7a1f6d6076b784454d8b7ed",
                "shasum": ""
            },
            "require": {
                "php": ">=7.3"
            },
            "require-dev": {
                "phpunit/phpunit": "^9.3"
            },
            "suggest": {
                "ext-posix": "*"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "5.1-dev"
                }
            },
            "autoload": {
                "classmap": [
                    "src/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause"
            ],
            "authors": [
                {
                    "name": "Sebastian Bergmann",
                    "email": "sebastian@phpunit.de"
                }
            ],
            "description": "Provides functionality to handle HHVM/PHP environments",
            "homepage": "http://www.github.com/sebastianbergmann/environment",
            "keywords": [
                "Xdebug",
                "environment",
                "hhvm"
            ],
            "support": {
                "issues": "https://github.com/sebastianbergmann/environment/issues",
                "source": "https://github.com/sebastianbergmann/environment/tree/5.1.5"
            },
            "funding": [
                {
                    "url": "https://github.com/sebastianbergmann",
                    "type": "github"
                }
            ],
            "time": "2023-02-03T06:03:51+00:00"
        },
        {
            "name": "sebastian/exporter",
            "version": "4.0.6",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/exporter.git",
                "reference": "78c00df8f170e02473b682df15bfcdacc3d32d72"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/exporter/zipball/78c00df8f170e02473b682df15bfcdacc3d32d72",
                "reference": "78c00df8f170e02473b682df15bfcdacc3d32d72",
                "shasum": ""
            },
            "require": {
                "php": ">=7.3",
                "sebastian/recursion-context": "^4.0"
            },
            "require-dev": {
                "ext-mbstring": "*",
                "phpunit/phpunit": "^9.3"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "4.0-dev"
                }
            },
            "autoload": {
                "classmap": [
                    "src/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause"
            ],
            "authors": [
                {
                    "name": "Sebastian Bergmann",
                    "email": "sebastian@phpunit.de"
                },
                {
                    "name": "Jeff Welch",
                    "email": "whatthejeff@gmail.com"
                },
                {
                    "name": "Volker Dusch",
                    "email": "github@wallbash.com"
                },
                {
                    "name": "Adam Harvey",
                    "email": "aharvey@php.net"
                },
                {
                    "name": "Bernhard Schussek",
                    "email": "bschussek@gmail.com"
                }
            ],
            "description": "Provides the functionality to export PHP variables for visualization",
            "homepage": "https://www.github.com/sebastianbergmann/exporter",
            "keywords": [
                "export",
                "exporter"
            ],
            "support": {
                "issues": "https://github.com/sebastianbergmann/exporter/issues",
                "source": "https://github.com/sebastianbergmann/exporter/tree/4.0.6"
            },
            "funding": [
                {
                    "url": "https://github.com/sebastianbergmann",
                    "type": "github"
                }
            ],
            "time": "2024-03-02T06:33:00+00:00"
        },
        {
            "name": "sebastian/global-state",
            "version": "5.0.7",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/global-state.git",
                "reference": "bca7df1f32ee6fe93b4d4a9abbf69e13a4ada2c9"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/global-state/zipball/bca7df1f32ee6fe93b4d4a9abbf69e13a4ada2c9",
                "reference": "bca7df1f32ee6fe93b4d4a9abbf69e13a4ada2c9",
                "shasum": ""
            },
            "require": {
                "php": ">=7.3",
                "sebastian/object-reflector": "^2.0",
                "sebastian/recursion-context": "^4.0"
            },
            "require-dev": {
                "ext-dom": "*",
                "phpunit/phpunit": "^9.3"
            },
            "suggest": {
                "ext-uopz": "*"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "5.0-dev"
                }
            },
            "autoload": {
                "classmap": [
                    "src/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause"
            ],
            "authors": [
                {
                    "name": "Sebastian Bergmann",
                    "email": "sebastian@phpunit.de"
                }
            ],
            "description": "Snapshotting of global state",
            "homepage": "http://www.github.com/sebastianbergmann/global-state",
            "keywords": [
                "global state"
            ],
            "support": {
                "issues": "https://github.com/sebastianbergmann/global-state/issues",
                "source": "https://github.com/sebastianbergmann/global-state/tree/5.0.7"
            },
            "funding": [
                {
                    "url": "https://github.com/sebastianbergmann",
                    "type": "github"
                }
            ],
            "time": "2024-03-02T06:35:11+00:00"
        },
        {
            "name": "sebastian/lines-of-code",
            "version": "1.0.4",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/lines-of-code.git",
                "reference": "e1e4a170560925c26d424b6a03aed157e7dcc5c5"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/lines-of-code/zipball/e1e4a170560925c26d424b6a03aed157e7dcc5c5",
                "reference": "e1e4a170560925c26d424b6a03aed157e7dcc5c5",
                "shasum": ""
            },
            "require": {
                "nikic/php-parser": "^4.18 || ^5.0",
                "php": ">=7.3"
            },
            "require-dev": {
                "phpunit/phpunit": "^9.3"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.0-dev"
                }
            },
            "autoload": {
                "classmap": [
                    "src/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause"
            ],
            "authors": [
                {
                    "name": "Sebastian Bergmann",
                    "email": "sebastian@phpunit.de",
                    "role": "lead"
                }
            ],
            "description": "Library for counting the lines of code in PHP source code",
            "homepage": "https://github.com/sebastianbergmann/lines-of-code",
            "support": {
                "issues": "https://github.com/sebastianbergmann/lines-of-code/issues",
                "source": "https://github.com/sebastianbergmann/lines-of-code/tree/1.0.4"
            },
            "funding": [
                {
                    "url": "https://github.com/sebastianbergmann",
                    "type": "github"
                }
            ],
            "time": "2023-12-22T06:20:34+00:00"
        },
        {
            "name": "sebastian/object-enumerator",
            "version": "4.0.4",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/object-enumerator.git",
                "reference": "5c9eeac41b290a3712d88851518825ad78f45c71"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/object-enumerator/zipball/5c9eeac41b290a3712d88851518825ad78f45c71",
                "reference": "5c9eeac41b290a3712d88851518825ad78f45c71",
                "shasum": ""
            },
            "require": {
                "php": ">=7.3",
                "sebastian/object-reflector": "^2.0",
                "sebastian/recursion-context": "^4.0"
            },
            "require-dev": {
                "phpunit/phpunit": "^9.3"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "4.0-dev"
                }
            },
            "autoload": {
                "classmap": [
                    "src/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause"
            ],
            "authors": [
                {
                    "name": "Sebastian Bergmann",
                    "email": "sebastian@phpunit.de"
                }
            ],
            "description": "Traverses array structures and object graphs to enumerate all referenced objects",
            "homepage": "https://github.com/sebastianbergmann/object-enumerator/",
            "support": {
                "issues": "https://github.com/sebastianbergmann/object-enumerator/issues",
                "source": "https://github.com/sebastianbergmann/object-enumerator/tree/4.0.4"
            },
            "funding": [
                {
                    "url": "https://github.com/sebastianbergmann",
                    "type": "github"
                }
            ],
            "time": "2020-10-26T13:12:34+00:00"
        },
        {
            "name": "sebastian/object-reflector",
            "version": "2.0.4",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/object-reflector.git",
                "reference": "b4f479ebdbf63ac605d183ece17d8d7fe49c15c7"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/object-reflector/zipball/b4f479ebdbf63ac605d183ece17d8d7fe49c15c7",
                "reference": "b4f479ebdbf63ac605d183ece17d8d7fe49c15c7",
                "shasum": ""
            },
            "require": {
                "php": ">=7.3"
            },
            "require-dev": {
                "phpunit/phpunit": "^9.3"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "2.0-dev"
                }
            },
            "autoload": {
                "classmap": [
                    "src/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause"
            ],
            "authors": [
                {
                    "name": "Sebastian Bergmann",
                    "email": "sebastian@phpunit.de"
                }
            ],
            "description": "Allows reflection of object attributes, including inherited and non-public ones",
            "homepage": "https://github.com/sebastianbergmann/object-reflector/",
            "support": {
                "issues": "https://github.com/sebastianbergmann/object-reflector/issues",
                "source": "https://github.com/sebastianbergmann/object-reflector/tree/2.0.4"
            },
            "funding": [
                {
                    "url": "https://github.com/sebastianbergmann",
                    "type": "github"
                }
            ],
            "time": "2020-10-26T13:14:26+00:00"
        },
        {
            "name": "sebastian/recursion-context",
            "version": "4.0.5",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/recursion-context.git",
                "reference": "e75bd0f07204fec2a0af9b0f3cfe97d05f92efc1"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/recursion-context/zipball/e75bd0f07204fec2a0af9b0f3cfe97d05f92efc1",
                "reference": "e75bd0f07204fec2a0af9b0f3cfe97d05f92efc1",
                "shasum": ""
            },
            "require": {
                "php": ">=7.3"
            },
            "require-dev": {
                "phpunit/phpunit": "^9.3"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "4.0-dev"
                }
            },
            "autoload": {
                "classmap": [
                    "src/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause"
            ],
            "authors": [
                {
                    "name": "Sebastian Bergmann",
                    "email": "sebastian@phpunit.de"
                },
                {
                    "name": "Jeff Welch",
                    "email": "whatthejeff@gmail.com"
                },
                {
                    "name": "Adam Harvey",
                    "email": "aharvey@php.net"
                }
            ],
            "description": "Provides functionality to recursively process PHP variables",
            "homepage": "https://github.com/sebastianbergmann/recursion-context",
            "support": {
                "issues": "https://github.com/sebastianbergmann/recursion-context/issues",
                "source": "https://github.com/sebastianbergmann/recursion-context/tree/4.0.5"
            },
            "funding": [
                {
                    "url": "https://github.com/sebastianbergmann",
                    "type": "github"
                }
            ],
            "time": "2023-02-03T06:07:39+00:00"
        },
        {
            "name": "sebastian/resource-operations",
            "version": "3.0.4",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/resource-operations.git",
                "reference": "05d5692a7993ecccd56a03e40cd7e5b09b1d404e"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/resource-operations/zipball/05d5692a7993ecccd56a03e40cd7e5b09b1d404e",
                "reference": "05d5692a7993ecccd56a03e40cd7e5b09b1d404e",
                "shasum": ""
            },
            "require": {
                "php": ">=7.3"
            },
            "require-dev": {
                "phpunit/phpunit": "^9.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-main": "3.0-dev"
                }
            },
            "autoload": {
                "classmap": [
                    "src/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause"
            ],
            "authors": [
                {
                    "name": "Sebastian Bergmann",
                    "email": "sebastian@phpunit.de"
                }
            ],
            "description": "Provides a list of PHP built-in functions that operate on resources",
            "homepage": "https://www.github.com/sebastianbergmann/resource-operations",
            "support": {
                "source": "https://github.com/sebastianbergmann/resource-operations/tree/3.0.4"
            },
            "funding": [
                {
                    "url": "https://github.com/sebastianbergmann",
                    "type": "github"
                }
            ],
            "time": "2024-03-14T16:00:52+00:00"
        },
        {
            "name": "sebastian/type",
            "version": "3.2.1",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/type.git",
                "reference": "75e2c2a32f5e0b3aef905b9ed0b179b953b3d7c7"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/type/zipball/75e2c2a32f5e0b3aef905b9ed0b179b953b3d7c7",
                "reference": "75e2c2a32f5e0b3aef905b9ed0b179b953b3d7c7",
                "shasum": ""
            },
            "require": {
                "php": ">=7.3"
            },
            "require-dev": {
                "phpunit/phpunit": "^9.5"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "3.2-dev"
                }
            },
            "autoload": {
                "classmap": [
                    "src/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause"
            ],
            "authors": [
                {
                    "name": "Sebastian Bergmann",
                    "email": "sebastian@phpunit.de",
                    "role": "lead"
                }
            ],
            "description": "Collection of value objects that represent the types of the PHP type system",
            "homepage": "https://github.com/sebastianbergmann/type",
            "support": {
                "issues": "https://github.com/sebastianbergmann/type/issues",
                "source": "https://github.com/sebastianbergmann/type/tree/3.2.1"
            },
            "funding": [
                {
                    "url": "https://github.com/sebastianbergmann",
                    "type": "github"
                }
            ],
            "time": "2023-02-03T06:13:03+00:00"
        },
        {
            "name": "sebastian/version",
            "version": "3.0.2",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/version.git",
                "reference": "c6c1022351a901512170118436c764e473f6de8c"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/version/zipball/c6c1022351a901512170118436c764e473f6de8c",
                "reference": "c6c1022351a901512170118436c764e473f6de8c",
                "shasum": ""
            },
            "require": {
                "php": ">=7.3"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "3.0-dev"
                }
            },
            "autoload": {
                "classmap": [
                    "src/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause"
            ],
            "authors": [
                {
                    "name": "Sebastian Bergmann",
                    "email": "sebastian@phpunit.de",
                    "role": "lead"
                }
            ],
            "description": "Library that helps with managing the version number of Git-hosted PHP projects",
            "homepage": "https://github.com/sebastianbergmann/version",
            "support": {
                "issues": "https://github.com/sebastianbergmann/version/issues",
                "source": "https://github.com/sebastianbergmann/version/tree/3.0.2"
            },
            "funding": [
                {
                    "url": "https://github.com/sebastianbergmann",
                    "type": "github"
                }
            ],
            "time": "2020-09-28T06:39:44+00:00"
        },
        {
            "name": "spatie/array-to-xml",
            "version": "3.3.0",
            "source": {
                "type": "git",
                "url": "https://github.com/spatie/array-to-xml.git",
                "reference": "f56b220fe2db1ade4c88098d83413ebdfc3bf876"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/spatie/array-to-xml/zipball/f56b220fe2db1ade4c88098d83413ebdfc3bf876",
                "reference": "f56b220fe2db1ade4c88098d83413ebdfc3bf876",
                "shasum": ""
            },
            "require": {
                "ext-dom": "*",
                "php": "^8.0"
            },
            "require-dev": {
                "mockery/mockery": "^1.2",
                "pestphp/pest": "^1.21",
                "spatie/pest-plugin-snapshots": "^1.1"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-main": "3.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Spatie\\ArrayToXml\\": "src"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Freek Van der Herten",
                    "email": "freek@spatie.be",
                    "homepage": "https://freek.dev",
                    "role": "Developer"
                }
            ],
            "description": "Convert an array to xml",
            "homepage": "https://github.com/spatie/array-to-xml",
            "keywords": [
                "array",
                "convert",
                "xml"
            ],
            "support": {
                "source": "https://github.com/spatie/array-to-xml/tree/3.3.0"
            },
            "funding": [
                {
                    "url": "https://spatie.be/open-source/support-us",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/spatie",
                    "type": "github"
                }
            ],
            "time": "2024-05-01T10:20:27+00:00"
        },
        {
            "name": "symfony/browser-kit",
            "version": "v7.1.1",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/browser-kit.git",
                "reference": "9c13742e3175b5815e272b981876ae329bec2040"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/browser-kit/zipball/9c13742e3175b5815e272b981876ae329bec2040",
                "reference": "9c13742e3175b5815e272b981876ae329bec2040",
                "shasum": ""
            },
            "require": {
                "php": ">=8.2",
                "symfony/dom-crawler": "^6.4|^7.0"
            },
            "require-dev": {
                "symfony/css-selector": "^6.4|^7.0",
                "symfony/http-client": "^6.4|^7.0",
                "symfony/mime": "^6.4|^7.0",
                "symfony/process": "^6.4|^7.0"
            },
            "type": "library",
            "autoload": {
                "psr-4": {
                    "Symfony\\Component\\BrowserKit\\": ""
                },
                "exclude-from-classmap": [
                    "/Tests/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Fabien Potencier",
                    "email": "fabien@symfony.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Simulates the behavior of a web browser, allowing you to make requests, click on links and submit forms programmatically",
            "homepage": "https://symfony.com",
            "support": {
                "source": "https://github.com/symfony/browser-kit/tree/v7.1.1"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2024-05-31T14:57:53+00:00"
        },
        {
            "name": "symfony/css-selector",
            "version": "v7.1.1",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/css-selector.git",
                "reference": "1c7cee86c6f812896af54434f8ce29c8d94f9ff4"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/css-selector/zipball/1c7cee86c6f812896af54434f8ce29c8d94f9ff4",
                "reference": "1c7cee86c6f812896af54434f8ce29c8d94f9ff4",
                "shasum": ""
            },
            "require": {
                "php": ">=8.2"
            },
            "type": "library",
            "autoload": {
                "psr-4": {
                    "Symfony\\Component\\CssSelector\\": ""
                },
                "exclude-from-classmap": [
                    "/Tests/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Fabien Potencier",
                    "email": "fabien@symfony.com"
                },
                {
                    "name": "Jean-François Simon",
                    "email": "jeanfrancois.simon@sensiolabs.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Converts CSS selectors to XPath expressions",
            "homepage": "https://symfony.com",
            "support": {
                "source": "https://github.com/symfony/css-selector/tree/v7.1.1"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2024-05-31T14:57:53+00:00"
        },
        {
            "name": "symfony/dom-crawler",
            "version": "v7.1.1",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/dom-crawler.git",
                "reference": "01ce8174447f1f1dd33a5854b01beef79061d9fa"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/dom-crawler/zipball/01ce8174447f1f1dd33a5854b01beef79061d9fa",
                "reference": "01ce8174447f1f1dd33a5854b01beef79061d9fa",
                "shasum": ""
            },
            "require": {
                "masterminds/html5": "^2.6",
                "php": ">=8.2",
                "symfony/polyfill-ctype": "~1.8",
                "symfony/polyfill-mbstring": "~1.0"
            },
            "require-dev": {
                "symfony/css-selector": "^6.4|^7.0"
            },
            "type": "library",
            "autoload": {
                "psr-4": {
                    "Symfony\\Component\\DomCrawler\\": ""
                },
                "exclude-from-classmap": [
                    "/Tests/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Fabien Potencier",
                    "email": "fabien@symfony.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Eases DOM navigation for HTML and XML documents",
            "homepage": "https://symfony.com",
            "support": {
                "source": "https://github.com/symfony/dom-crawler/tree/v7.1.1"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2024-05-31T14:57:53+00:00"
        },
        {
            "name": "symfony/translation",
            "version": "v7.1.3",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/translation.git",
                "reference": "8d5e50c813ba2859a6dfc99a0765c550507934a1"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/translation/zipball/8d5e50c813ba2859a6dfc99a0765c550507934a1",
                "reference": "8d5e50c813ba2859a6dfc99a0765c550507934a1",
                "shasum": ""
            },
            "require": {
                "php": ">=8.2",
                "symfony/polyfill-mbstring": "~1.0",
                "symfony/translation-contracts": "^2.5|^3.0"
            },
            "conflict": {
                "symfony/config": "<6.4",
                "symfony/console": "<6.4",
                "symfony/dependency-injection": "<6.4",
                "symfony/http-client-contracts": "<2.5",
                "symfony/http-kernel": "<6.4",
                "symfony/service-contracts": "<2.5",
                "symfony/twig-bundle": "<6.4",
                "symfony/yaml": "<6.4"
            },
            "provide": {
                "symfony/translation-implementation": "2.3|3.0"
            },
            "require-dev": {
                "nikic/php-parser": "^4.18|^5.0",
                "psr/log": "^1|^2|^3",
                "symfony/config": "^6.4|^7.0",
                "symfony/console": "^6.4|^7.0",
                "symfony/dependency-injection": "^6.4|^7.0",
                "symfony/finder": "^6.4|^7.0",
                "symfony/http-client-contracts": "^2.5|^3.0",
                "symfony/http-kernel": "^6.4|^7.0",
                "symfony/intl": "^6.4|^7.0",
                "symfony/polyfill-intl-icu": "^1.21",
                "symfony/routing": "^6.4|^7.0",
                "symfony/service-contracts": "^2.5|^3",
                "symfony/yaml": "^6.4|^7.0"
            },
            "type": "library",
            "autoload": {
                "files": [
                    "Resources/functions.php"
                ],
                "psr-4": {
                    "Symfony\\Component\\Translation\\": ""
                },
                "exclude-from-classmap": [
                    "/Tests/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Fabien Potencier",
                    "email": "fabien@symfony.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Provides tools to internationalize your application",
            "homepage": "https://symfony.com",
            "support": {
                "source": "https://github.com/symfony/translation/tree/v7.1.3"
            },
            "funding": [
                {
                    "url": "https://symfony.com/sponsor",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/fabpot",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2024-07-26T12:41:01+00:00"
        },
        {
            "name": "symplify/easy-coding-standard",
            "version": "12.3.4",
            "source": {
                "type": "git",
                "url": "https://github.com/easy-coding-standard/easy-coding-standard.git",
                "reference": "03cd792d7fa6d9dc59b6e12a5ca73d9873ee9c0e"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/easy-coding-standard/easy-coding-standard/zipball/03cd792d7fa6d9dc59b6e12a5ca73d9873ee9c0e",
                "reference": "03cd792d7fa6d9dc59b6e12a5ca73d9873ee9c0e",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2"
            },
            "conflict": {
                "friendsofphp/php-cs-fixer": "<3.46",
                "phpcsstandards/php_codesniffer": "<3.8",
                "symplify/coding-standard": "<12.1"
            },
            "suggest": {
                "ext-dom": "Needed to support checkstyle output format in class CheckstyleOutputFormatter"
            },
            "bin": [
                "bin/ecs"
            ],
            "type": "library",
            "autoload": {
                "files": [
                    "bootstrap.php"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "description": "Use Coding Standard with 0-knowledge of PHP-CS-Fixer and PHP_CodeSniffer",
            "keywords": [
                "Code style",
                "automation",
                "fixer",
                "static analysis"
            ],
            "support": {
                "issues": "https://github.com/easy-coding-standard/easy-coding-standard/issues",
                "source": "https://github.com/easy-coding-standard/easy-coding-standard/tree/12.3.4"
            },
            "funding": [
                {
                    "url": "https://www.paypal.me/rectorphp",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/tomasvotruba",
                    "type": "github"
                }
            ],
            "time": "2024-08-01T07:55:09+00:00"
        },
        {
            "name": "theseer/tokenizer",
            "version": "1.2.3",
            "source": {
                "type": "git",
                "url": "https://github.com/theseer/tokenizer.git",
                "reference": "737eda637ed5e28c3413cb1ebe8bb52cbf1ca7a2"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/theseer/tokenizer/zipball/737eda637ed5e28c3413cb1ebe8bb52cbf1ca7a2",
                "reference": "737eda637ed5e28c3413cb1ebe8bb52cbf1ca7a2",
                "shasum": ""
            },
            "require": {
                "ext-dom": "*",
                "ext-tokenizer": "*",
                "ext-xmlwriter": "*",
                "php": "^7.2 || ^8.0"
            },
            "type": "library",
            "autoload": {
                "classmap": [
                    "src/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause"
            ],
            "authors": [
                {
                    "name": "Arne Blankerts",
                    "email": "arne@blankerts.de",
                    "role": "Developer"
                }
            ],
            "description": "A small library for converting tokenized PHP source code into XML and potentially other formats",
            "support": {
                "issues": "https://github.com/theseer/tokenizer/issues",
                "source": "https://github.com/theseer/tokenizer/tree/1.2.3"
            },
            "funding": [
                {
                    "url": "https://github.com/theseer",
                    "type": "github"
                }
            ],
            "time": "2024-03-03T12:36:25+00:00"
        },
        {
            "name": "vimeo/psalm",
            "version": "5.25.0",
            "source": {
                "type": "git",
                "url": "https://github.com/vimeo/psalm.git",
                "reference": "01a8eb06b9e9cc6cfb6a320bf9fb14331919d505"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/vimeo/psalm/zipball/01a8eb06b9e9cc6cfb6a320bf9fb14331919d505",
                "reference": "01a8eb06b9e9cc6cfb6a320bf9fb14331919d505",
                "shasum": ""
            },
            "require": {
                "amphp/amp": "^2.4.2",
                "amphp/byte-stream": "^1.5",
                "composer-runtime-api": "^2",
                "composer/semver": "^1.4 || ^2.0 || ^3.0",
                "composer/xdebug-handler": "^2.0 || ^3.0",
                "dnoegel/php-xdg-base-dir": "^0.1.1",
                "ext-ctype": "*",
                "ext-dom": "*",
                "ext-json": "*",
                "ext-libxml": "*",
                "ext-mbstring": "*",
                "ext-simplexml": "*",
                "ext-tokenizer": "*",
                "felixfbecker/advanced-json-rpc": "^3.1",
                "felixfbecker/language-server-protocol": "^1.5.2",
                "fidry/cpu-core-counter": "^0.4.1 || ^0.5.1 || ^1.0.0",
                "netresearch/jsonmapper": "^1.0 || ^2.0 || ^3.0 || ^4.0",
                "nikic/php-parser": "^4.16",
                "php": "^7.4 || ~8.0.0 || ~8.1.0 || ~8.2.0 || ~8.3.0",
                "sebastian/diff": "^4.0 || ^5.0 || ^6.0",
                "spatie/array-to-xml": "^2.17.0 || ^3.0",
                "symfony/console": "^4.1.6 || ^5.0 || ^6.0 || ^7.0",
                "symfony/filesystem": "^5.4 || ^6.0 || ^7.0"
            },
            "conflict": {
                "nikic/php-parser": "4.17.0"
            },
            "provide": {
                "psalm/psalm": "self.version"
            },
            "require-dev": {
                "amphp/phpunit-util": "^2.0",
                "bamarni/composer-bin-plugin": "^1.4",
                "brianium/paratest": "^6.9",
                "ext-curl": "*",
                "mockery/mockery": "^1.5",
                "nunomaduro/mock-final-classes": "^1.1",
                "php-parallel-lint/php-parallel-lint": "^1.2",
                "phpstan/phpdoc-parser": "^1.6",
                "phpunit/phpunit": "^9.6",
                "psalm/plugin-mockery": "^1.1",
                "psalm/plugin-phpunit": "^0.18",
                "slevomat/coding-standard": "^8.4",
                "squizlabs/php_codesniffer": "^3.6",
                "symfony/process": "^4.4 || ^5.0 || ^6.0 || ^7.0"
            },
            "suggest": {
                "ext-curl": "In order to send data to shepherd",
                "ext-igbinary": "^2.0.5 is required, used to serialize caching data"
            },
            "bin": [
                "psalm",
                "psalm-language-server",
                "psalm-plugin",
                "psalm-refactor",
                "psalter"
            ],
            "type": "project",
            "extra": {
                "branch-alias": {
                    "dev-master": "5.x-dev",
                    "dev-4.x": "4.x-dev",
                    "dev-3.x": "3.x-dev",
                    "dev-2.x": "2.x-dev",
                    "dev-1.x": "1.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Psalm\\": "src/Psalm/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Matthew Brown"
                }
            ],
            "description": "A static analysis tool for finding errors in PHP applications",
            "keywords": [
                "code",
                "inspection",
                "php",
                "static analysis"
            ],
            "support": {
                "docs": "https://psalm.dev/docs",
                "issues": "https://github.com/vimeo/psalm/issues",
                "source": "https://github.com/vimeo/psalm"
            },
            "time": "2024-06-16T15:08:35+00:00"
        },
        {
            "name": "webmozart/assert",
            "version": "1.11.0",
            "source": {
                "type": "git",
                "url": "https://github.com/webmozarts/assert.git",
                "reference": "11cb2199493b2f8a3b53e7f19068fc6aac760991"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/webmozarts/assert/zipball/11cb2199493b2f8a3b53e7f19068fc6aac760991",
                "reference": "11cb2199493b2f8a3b53e7f19068fc6aac760991",
                "shasum": ""
            },
            "require": {
                "ext-ctype": "*",
                "php": "^7.2 || ^8.0"
            },
            "conflict": {
                "phpstan/phpstan": "<0.12.20",
                "vimeo/psalm": "<4.6.1 || 4.6.2"
            },
            "require-dev": {
                "phpunit/phpunit": "^8.5.13"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.10-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Webmozart\\Assert\\": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Bernhard Schussek",
                    "email": "bschussek@gmail.com"
                }
            ],
            "description": "Assertions to validate method input/output with nice error messages.",
            "keywords": [
                "assert",
                "check",
                "validate"
            ],
            "support": {
                "issues": "https://github.com/webmozarts/assert/issues",
                "source": "https://github.com/webmozarts/assert/tree/1.11.0"
            },
            "time": "2022-06-03T18:03:27+00:00"
        }
    ],
    "aliases": [],
    "minimum-stability": "RC",
    "stability-flags": {
        "roave/security-advisories": 20
    },
    "prefer-stable": false,
    "prefer-lowest": false,
    "platform": {
        "php": "^8.3",
        "ext-amqp": "*",
        "ext-apcu": "*",
        "ext-json": "*",
        "ext-zend-opcache": "*",
        "ext-pdo": "*"
    },
    "platform-dev": {
        "ext-xdebug": "*"
    },
    "plugin-api-version": "2.6.0"
}
```

## File: `docker-compose.yml`
```yaml
version: '3'

services:
  shared_rabbitmq:
    container_name: codely-php_ddd_skeleton-rabbitmq
    image: 'rabbitmq:3.10.5-management'
    restart: unless-stopped
    ports:
      - "5630:5672"
      - "8090:15672"
    environment:
      - RABBITMQ_DEFAULT_USER=codely
      - RABBITMQ_DEFAULT_PASS=c0d3ly

  shared_prometheus:
    container_name: codely-php_ddd_skeleton-prometheus
    image: prom/prometheus:v2.36.1
    volumes:
      - ./etc/prometheus/:/etc/prometheus/
    command:
      - '--config.file=/etc/prometheus/prometheus.yml'
      - '--storage.tsdb.path=/prometheus'
      - '--web.console.libraries=/usr/share/prometheus/console_libraries'
      - '--web.console.templates=/usr/share/prometheus/consoles'
    ports:
      - "9999:9090"

  mooc_mysql:
    container_name: codely-php_ddd_skeleton-mooc-mysql
    image: mariadb:10.7.4
    ports:
      - "3360:3306"
    environment:
      - MYSQL_ROOT_PASSWORD=
      - MYSQL_ALLOW_EMPTY_PASSWORD=yes
    healthcheck:
      test: ["CMD", "mysqladmin", "--user=root", "--password=", "--host=127.0.0.1", "ping", "--silent"]
      interval: 2s
      timeout: 10s
      retries: 10
    command: ["--default-authentication-plugin=mysql_native_password"]

  backoffice_elasticsearch:
    container_name: codely-php_ddd_skeleton-backoffice-elastic
    image: docker.elastic.co/elasticsearch/elasticsearch:8.2.3
    ports:
      - "9200:9200"
      - "9300:9300"
    environment:
      - discovery.type=single-node
      - xpack.security.enabled=false
      - "ES_JAVA_OPTS=-Xms512m -Xmx512m"

  backoffice_backend_php:
    container_name: codely-php_ddd_skeleton-backoffice_backend-php
    user: "${UID}:${GID}"
    build:
      context: .
      dockerfile: Dockerfile
    restart: unless-stopped
    ports:
      - "8040:8040"
      - "9040:9001"
    volumes:
      - .:/app:delegated
    depends_on:
      - shared_rabbitmq
      - shared_prometheus
      - backoffice_elasticsearch
    command: symfony serve --dir=apps/backoffice/backend/public --port=8040

  backoffice_frontend_php:
    container_name: codely-php_ddd_skeleton-backoffice_frontend-php
    user: "${UID}:${GID}"
    build:
      context: .
      dockerfile: Dockerfile
    restart: unless-stopped
    ports:
      - "8041:8041"
      - "9041:9001"
    volumes:
      - .:/app:delegated
    depends_on:
      - shared_rabbitmq
      - shared_prometheus
      - backoffice_elasticsearch
      - mooc_mysql
    command: symfony serve --dir=apps/backoffice/frontend/public --port=8041

  mooc_backend_php:
    container_name: codely-php_ddd_skeleton-mooc_backend-php
    user: "${UID}:${GID}"
    build:
      context: .
      dockerfile: Dockerfile
    restart: unless-stopped
    ports:
      - "8030:8030"
      - "9030:9001"
    volumes:
      - .:/app:delegated
    depends_on:
      - shared_rabbitmq
      - shared_prometheus
      - mooc_mysql
    command: symfony serve --dir=apps/mooc/backend/public --port=8030
```

## File: `ecs.php`
```php
<?php

declare(strict_types=1);

use CodelyTv\CodingStyle;
use PhpCsFixer\Fixer\ClassNotation\FinalClassFixer;
use Symplify\EasyCodingStandard\Config\ECSConfig;

return function (ECSConfig $ecsConfig): void {
	$ecsConfig->paths([__DIR__ . '/apps', __DIR__ . '/src', __DIR__ . '/tests', ]);

	$ecsConfig->sets([CodingStyle::DEFAULT]);

	$ecsConfig->skip([
		FinalClassFixer::class => [
			__DIR__ . '/apps/backoffice/backend/src/BackofficeBackendKernel.php',
			__DIR__ . '/apps/backoffice/frontend/src/BackofficeFrontendKernel.php',
			__DIR__ . '/apps/mooc/backend/src/MoocBackendKernel.php',
			__DIR__ . '/src/Shared/Infrastructure/Bus/Event/InMemory/InMemorySymfonyEventBus.php',
		],
		__DIR__ . '/apps/backoffice/backend/var',
		__DIR__ . '/apps/backoffice/frontend/var',
		__DIR__ . '/apps/mooc/backend/var',
		__DIR__ . '/apps/mooc/frontend/var',
	]);
};
```

## File: `phpmd.xml`
```xml
<?xml version="1.0"?>
<ruleset xmlns="https://pmd.sf.net/ruleset/1.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:noNamespaceSchemaLocation="https://pmd.sf.net/ruleset_xml_schema.xsd">

    <exclude-pattern>apps/*/*/var/*</exclude-pattern>
    <exclude-pattern>*SimilarComparator*</exclude-pattern>
    <exclude-pattern>*IsSimilar*</exclude-pattern>
    <!-- Fix CyclomaticComplexity -->
    <exclude-pattern>src/Shared/Infrastructure/Symfony/AddJsonBodyToRequestListener.php</exclude-pattern>
    <!-- Fix ExcessiveClassLength -->
    <exclude-pattern>tests/Shared/Infrastructure/Bus/Event/RabbitMq/RabbitMqEventBusTest.php</exclude-pattern>
    <!-- Fix TooManyMethods -->
    <exclude-pattern>tests/Shared/Infrastructure/PhpUnit/UnitTestCase.php</exclude-pattern>

    <rule ref="rulesets/cleancode.xml/BooleanArgumentFlag"/>

    <rule ref="rulesets/codesize.xml/CyclomaticComplexity">
        <properties>
            <property name="reportLevel" value="5"/>
        </properties>
    </rule>
    <rule ref="rulesets/codesize.xml/ExcessiveMethodLength">
        <properties>
            <property name="minimum" value="35"/>
        </properties>
    </rule>
    <rule ref="rulesets/codesize.xml/ExcessiveClassLength">
        <properties>
            <property name="minimum" value="100"/>
        </properties>
    </rule>
    <rule ref="rulesets/codesize.xml/ExcessiveParameterList">
        <properties>
            <property name="minimum" value="10"/>
        </properties>
    </rule>
    <rule ref="rulesets/codesize.xml/TooManyMethods">
        <properties>
            <property name="maxmethods" value="10"/>
        </properties>
    </rule>
    <rule ref="rulesets/codesize.xml/ExcessiveClassComplexity">
        <properties>
            <property name="maximum" value="20"/>
        </properties>
    </rule>
</ruleset>
```

## File: `phpstan.neon`
```
includes:
	- vendor/phpat/phpat/extension.neon

parameters:
	level: 0
	paths:
		- ./apps
		- ./src
		- ./tests
	excludePaths:
		- ./apps/backoffice/backend/var
		- ./apps/backoffice/frontend/var
		- ./apps/mooc/backend/var
		- ./apps/mooc/frontend/var

services:
	-
		class: CodelyTv\Tests\Shared\SharedArchitectureTest
		tags:
			- phpat.test

	-
		class: CodelyTv\Tests\Mooc\MoocArchitectureTest
		tags:
			- phpat.test
```

## File: `phpunit.xml`
```xml
<?xml version="1.0" encoding="UTF-8"?>

<phpunit
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xsi:noNamespaceSchemaLocation="./vendor/phpunit/phpunit/phpunit.xsd"
        backupGlobals="false"
        backupStaticAttributes="false"
        beStrictAboutOutputDuringTests="true"
        beStrictAboutChangesToGlobalState="true"
        beStrictAboutTestsThatDoNotTestAnything="false"
        beStrictAboutTodoAnnotatedTests="true"
        bootstrap="./apps/bootstrap.php"
        colors="true"
        convertErrorsToExceptions="true"
        convertNoticesToExceptions="true"
        convertWarningsToExceptions="true"
        processIsolation="false"
        stopOnError="true"
        stopOnFailure="true"
        stopOnIncomplete="false"
        stopOnSkipped="false"
        stopOnRisky="true"
        verbose="false">

    <php>
        <ini name="error_reporting" value="-1" />
        <env name="SYMFONY_DEPRECATIONS_HELPER" value="weak" />
        <env name="APP_ENV" value="test"/>
    </php>

    <testsuites>
        <testsuite name="backoffice">
            <directory>./tests/Backoffice</directory>
        </testsuite>
        <testsuite name="mooc">
            <directory>./tests/Mooc</directory>
        </testsuite>
        <testsuite name="shared">
            <directory>./tests/Shared</directory>
        </testsuite>
    </testsuites>
</phpunit>
```

## File: `psalm.xml`
```xml
<?xml version="1.0"?>
<psalm
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xmlns="https://getpsalm.org/schema/config"
    xsi:schemaLocation="https://getpsalm.org/schema/config vendor/vimeo/psalm/config.xsd"
    errorLevel="2"
    resolveFromConfigFile="true"
    findUnusedBaselineEntry="false"
    findUnusedCode="false"
    allowStringToStandInForClass="true"
>
    <projectFiles>
        <directory name="apps"/>
        <directory name="src"/>
        <directory name="tests"/>
        <ignoreFiles>
            <directory name="apps/*/*/var"/>
            <directory name="vendor"/>
            <directory name="src/Shared/Infrastructure/Bus/Event/RabbitMq"/>
            <directory name="src/Shared/Infrastructure/Symfony"/>
            <directory name="tests/Shared/Infrastructure/Bus/Event/RabbitMq"/>
            <directory name="tests/Shared/Infrastructure/Mink"/>
            <directory name="tests/Shared/Infrastructure/PhpUnit/Constraint"/>
        </ignoreFiles>
    </projectFiles>

    <issueHandlers>
        <PossiblyUndefinedMethod>
            <errorLevel type="suppress">
                <directory name="tests"/>
            </errorLevel>
        </PossiblyUndefinedMethod>
        <RiskyTruthyFalsyComparison>
            <errorLevel type="suppress">
                <directory name="apps"/>
                <directory name="src"/>
                <directory name="tests"/>
            </errorLevel>
        </RiskyTruthyFalsyComparison>
        <PossiblyUndefinedArrayOffset>
            <errorLevel type="suppress">
                <directory name="apps"/>
                <directory name="src"/>
                <directory name="tests"/>
            </errorLevel>
        </PossiblyUndefinedArrayOffset>
        <PossiblyInvalidArgument>
            <errorLevel type="suppress">
                <directory name="tests"/>
            </errorLevel>
        </PossiblyInvalidArgument>
        <PossiblyNullReference>
            <errorLevel type="suppress">
                <directory name="tests"/>
            </errorLevel>
        </PossiblyNullReference>
        <PossiblyNullArgument>
            <errorLevel type="suppress">
                <directory name="tests"/>
            </errorLevel>
        </PossiblyNullArgument>
        <PropertyNotSetInConstructor>
            <errorLevel type="suppress">
                <directory name="tests"/>
            </errorLevel>
        </PropertyNotSetInConstructor>
        <MoreSpecificReturnType>
            <errorLevel type="suppress">
                <file name="apps/*/*/src/*Kernel.php"/>
            </errorLevel>
        </MoreSpecificReturnType>
        <UnresolvableInclude>
            <errorLevel type="suppress">
                <file name="apps/*/*/src/*Kernel.php"/>
            </errorLevel>
        </UnresolvableInclude>
    </issueHandlers>

    <plugins>
        <pluginClass class="Psalm\MockeryPlugin\Plugin"/>
        <pluginClass class="Psalm\SymfonyPsalmPlugin\Plugin"/>
        <pluginClass class="Psalm\PhpUnitPlugin\Plugin"/>
    </plugins>
</psalm>
```

## File: `rector.php`
```php
<?php

declare(strict_types=1);

use Rector\Config\RectorConfig;
use Rector\Set\ValueObject\LevelSetList;
use Rector\Set\ValueObject\SetList;

return static function (RectorConfig $rectorConfig): void {
    $rectorConfig->paths([
        __DIR__ . '/apps',
        __DIR__ . '/src',
        __DIR__ . '/tests',
    ]);

    $rectorConfig->sets([
        LevelSetList::UP_TO_PHP_82,
        SetList::TYPE_DECLARATION
    ]);

    $rectorConfig->skip([
        __DIR__ . '/apps/backoffice/backend/var',
        __DIR__ . '/apps/backoffice/frontend/var',
        __DIR__ . '/apps/mooc/backend/var',
        __DIR__ . '/apps/mooc/frontend/var',
    ]);
};
```

## File: `apps/bootstrap.php`
```php
<?php

declare(strict_types=1);

use Symfony\Component\Dotenv\Dotenv;

$rootPath = dirname(__DIR__);

require $rootPath . '/vendor/autoload.php';

(new Dotenv())->loadEnv($rootPath . '/.env');

$_SERVER += $_ENV;
$_SERVER['APP_ENV'] = $_ENV['APP_ENV'] = ($_SERVER['APP_ENV'] ?? $_ENV['APP_ENV'] ?? null) ?: 'dev';
$_SERVER['APP_DEBUG'] ??= $_ENV['APP_DEBUG'] ?? $_SERVER['APP_ENV'] !== 'prod';
$_SERVER['APP_DEBUG'] = $_ENV['APP_DEBUG'] =
	(int) $_SERVER['APP_DEBUG'] || filter_var($_SERVER['APP_DEBUG'], FILTER_VALIDATE_BOOLEAN) ? '1' : '0';
```

## File: `apps/backoffice/backend/config/bundles.php`
```php
<?php

declare(strict_types=1);

return [
	Symfony\Bundle\FrameworkBundle\FrameworkBundle::class => ['all' => true],
	FriendsOfBehat\SymfonyExtension\Bundle\FriendsOfBehatSymfonyExtensionBundle::class => ['test' => true],
	//    WouterJ\EloquentBundle\WouterJEloquentBundle::class                                => ['test' => true]
];
```

## File: `apps/backoffice/backend/config/services.yaml`
```yaml
imports:
  - { resource: ../../../../src/Backoffice/Shared/Infrastructure/Symfony/DependencyInjection/backoffice_services.yaml }

services:
  _defaults:
    autoconfigure: true
    autowire: true

  # Configure
  _instanceof:
    CodelyTv\Shared\Domain\Bus\Event\DomainEventSubscriber:
      tags: ['codely.domain_event_subscriber']

    CodelyTv\Shared\Domain\Bus\Command\CommandHandler:
      tags: ['codely.command_handler']

    CodelyTv\Shared\Domain\Bus\Query\QueryHandler:
      tags: ['codely.query_handler']

  CodelyTv\Apps\Backoffice\Backend\Controller\:
    resource: '../src/Controller'
    tags: ['controller.service_arguments']


  # Wire
  CodelyTv\Shared\:
    resource: '../../../../src/Shared'

  CodelyTv\Backoffice\:
    resource: '../../../../src/Backoffice'

  # -- TAGGING --
  CodelyTv\Shared\Infrastructure\Bus\Event\InMemory\InMemorySymfonyEventBus:
    arguments: [!tagged codely.domain_event_subscriber]
    lazy: true

  CodelyTv\Shared\Infrastructure\Bus\Event\DomainEventMapping:
    arguments: [!tagged codely.domain_event_subscriber]

  CodelyTv\Shared\Infrastructure\Bus\Event\DomainEventSubscriberLocator:
    arguments: [!tagged codely.domain_event_subscriber]

  CodelyTv\Shared\Infrastructure\Doctrine\DatabaseConnections:
    arguments: [!tagged codely.database_connection]

  CodelyTv\Shared\Infrastructure\Symfony\AddJsonBodyToRequestListener:
    tags:
      - { name: kernel.event_listener, event: kernel.request, method: onKernelRequest }

  CodelyTv\Shared\Infrastructure\Symfony\ApiExceptionListener:
    tags:
      - { name: kernel.event_listener, event: kernel.exception, method: onException }

  CodelyTv\Shared\Infrastructure\Symfony\BasicHttpAuthMiddleware:
    tags:
      - { name: kernel.event_listener, event: kernel.request, method: onKernelRequest }


  # -- APP DEFINITIONS --
  # Command/Query Handlers
  CodelyTv\Shared\Infrastructure\Bus\Command\InMemorySymfonyCommandBus:
    arguments: [!tagged codely.command_handler]

  CodelyTv\Shared\Infrastructure\Bus\Query\InMemorySymfonyQueryBus:
    arguments: [!tagged codely.query_handler]

  # RabbitMQ
  CodelyTv\Shared\Infrastructure\Bus\Event\RabbitMq\RabbitMqConnection:
    arguments:
      - host: '%env(RABBITMQ_HOST)%'
        port: '%env(RABBITMQ_PORT)%'
        vhost: '%env(RABBITMQ_MOOC_VHOST)%'
        login: '%env(RABBITMQ_LOGIN)%'
        password: '%env(RABBITMQ_PASSWORD)%'
        read_timeout: 2
        write_timeout: 2
        connect_timeout: 5

  CodelyTv\Shared\Infrastructure\Bus\Event\RabbitMq\RabbitMqEventBus:
    arguments: ['@CodelyTv\Shared\Infrastructure\Bus\Event\RabbitMq\RabbitMqConnection', '%env(RABBITMQ_EXCHANGE)%']

  CodelyTv\Shared\Infrastructure\Elasticsearch\ElasticsearchClient:
    factory: '@CodelyTv\Shared\Infrastructure\Elasticsearch\ElasticsearchClientFactory'
    arguments:
      - '%env(BACKOFFICE_ELASTICSEARCH_HOST)%'
      - '%env(BACKOFFICE_ELASTICSEARCH_INDEX_PREFIX)%'
      - '%kernel.project_dir%/../../../etc/databases/backoffice'
      - '%env(APP_ENV)%'
    public: true

  CodelyTv\Shared\Infrastructure\Bus\Event\WithMonitoring\WithPrometheusMonitoringEventBus:
    arguments: ['@CodelyTv\Shared\Infrastructure\Monitoring\PrometheusMonitor', 'backoffice_backend', '@CodelyTv\Shared\Infrastructure\Bus\Event\RabbitMq\RabbitMqEventBus']

  # -- IMPLEMENTATIONS SELECTOR --

  # -- IMPLEMENTATIONS SELECTOR --
  CodelyTv\Shared\Domain\Bus\Event\EventBus: '@CodelyTv\Shared\Infrastructure\Bus\Event\WithMonitoring\WithPrometheusMonitoringEventBus'
  CodelyTv\Backoffice\Courses\Domain\BackofficeCourseRepository: '@CodelyTv\Backoffice\Courses\Infrastructure\Persistence\ElasticsearchBackofficeCourseRepository'
```

## File: `apps/backoffice/backend/config/services_test.yaml`
```yaml
framework:
  test: true

services:
  _defaults:
    autoconfigure: true
    autowire: true

  CodelyTv\Tests\:
    resource: '../../../../tests'

  # -- IMPLEMENTATIONS SELECTOR --
  CodelyTv\Shared\Domain\Bus\Event\EventBus: '@CodelyTv\Shared\Infrastructure\Bus\Event\InMemory\InMemorySymfonyEventBus'
```

## File: `apps/backoffice/backend/config/routes/courses.yaml`
```yaml
courses_get:
  path: /courses
  controller: CodelyTv\Apps\Backoffice\Backend\Controller\Courses\CoursesGetController
  defaults: { auth: false }
  methods:  [GET]
```

## File: `apps/backoffice/backend/config/routes/health-check.yaml`
```yaml
health-check_get:
  path: /health-check
  controller: CodelyTv\Apps\Backoffice\Backend\Controller\HealthCheck\HealthCheckGetController
  methods:  [GET]
```

## File: `apps/backoffice/backend/config/routes/metrics.yaml`
```yaml
metrics_get:
  path: /metrics
  controller: CodelyTv\Apps\Backoffice\Backend\Controller\Metrics\MetricsController
  methods:  [GET]
```

## File: `apps/backoffice/backend/config/services/framework.yaml`
```yaml
framework:
  secret: '%env(APP_SECRET)%'
  #csrf_protection: true
  #http_method_override: true

  # Enables session support. Note that the session will ONLY be started if you read or write from it.
  # Remove or comment this section to explicitly disable session support.
  session:
    handler_id: null
    cookie_secure: auto
    cookie_samesite: lax
    enabled: true

  #esi: true
  #fragments: true
  php_errors:
    log: true
```

## File: `apps/backoffice/backend/public/index.php`
```php
<?php

declare(strict_types=1);

use CodelyTv\Apps\Backoffice\Backend\BackofficeBackendKernel;
use Symfony\Component\ErrorHandler\Debug;
use Symfony\Component\HttpFoundation\Request;

require dirname(__DIR__) . '/../../bootstrap.php';

if ($_SERVER['APP_DEBUG']) {
	umask(0000);

	Debug::enable();
}

if ($trustedProxies = $_SERVER['TRUSTED_PROXIES'] ?? $_ENV['TRUSTED_PROXIES'] ?? false) {
	Request::setTrustedProxies(
		explode(',', $trustedProxies),
		Request::HEADER_X_FORWARDED_FOR | Request::HEADER_X_FORWARDED_PORT | Request::HEADER_X_FORWARDED_PROTO
	);
}

if ($trustedHosts = $_SERVER['TRUSTED_HOSTS'] ?? $_ENV['TRUSTED_HOSTS'] ?? false) {
	Request::setTrustedHosts([$trustedHosts]);
}

$kernel = new BackofficeBackendKernel($_SERVER['APP_ENV'], (bool) $_SERVER['APP_DEBUG']);
$request = Request::createFromGlobals();
$response = $kernel->handle($request);
$response->send();
$kernel->terminate($request, $response);
```

## File: `apps/backoffice/backend/src/BackofficeBackendKernel.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Apps\Backoffice\Backend;

use Symfony\Bundle\FrameworkBundle\Kernel\MicroKernelTrait;
use Symfony\Component\Config\Loader\LoaderInterface;
use Symfony\Component\Config\Resource\FileResource;
use Symfony\Component\DependencyInjection\ContainerBuilder;
use Symfony\Component\HttpKernel\Kernel;

use function dirname;

class BackofficeBackendKernel extends Kernel
{
	use MicroKernelTrait;

	private const string CONFIG_EXTS = '.{xml,yaml}';

	public function registerBundles(): iterable
	{
		$contents = require $this->getProjectDir() . '/config/bundles.php';
		foreach ($contents as $class => $envs) {
			if ($envs[$this->environment] ?? $envs['all'] ?? false) {
				yield new $class();
			}
		}
	}

	public function getProjectDir(): string
	{
		return dirname(__DIR__);
	}

	protected function configureContainer(ContainerBuilder $container, LoaderInterface $loader): void
	{
		$container->addResource(new FileResource($this->getProjectDir() . '/config/bundles.php'));
		$container->setParameter('.container.dumper.inline_class_loader', true);
		$confDir = $this->getProjectDir() . '/config';

		$loader->load($confDir . '/services' . self::CONFIG_EXTS, 'glob');
		$loader->load($confDir . '/services_' . $this->environment . self::CONFIG_EXTS, 'glob');
		$loader->load($confDir . '/services/*' . self::CONFIG_EXTS, 'glob');
	}
}
```

## File: `apps/backoffice/backend/src/Controller/Courses/CoursesGetController.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Apps\Backoffice\Backend\Controller\Courses;

use CodelyTv\Backoffice\Courses\Application\BackofficeCourseResponse;
use CodelyTv\Backoffice\Courses\Application\BackofficeCoursesResponse;
use CodelyTv\Backoffice\Courses\Application\SearchByCriteria\SearchBackofficeCoursesByCriteriaQuery;
use CodelyTv\Shared\Domain\Bus\Query\QueryBus;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\HttpFoundation\Request;

use function Lambdish\Phunctional\map;

final readonly class CoursesGetController
{
	public function __construct(private QueryBus $queryBus) {}

	public function __invoke(Request $request): JsonResponse
	{
		$orderBy = $request->query->get('order_by');
		$order = $request->query->get('order');
		$limit = $request->query->get('limit');
		$offset = $request->query->get('offset');

		/** @var BackofficeCoursesResponse $response */
		$response = $this->queryBus->ask(
			new SearchBackofficeCoursesByCriteriaQuery(
				(array) $request->query->get('filters'),
				$orderBy,
				$order,
				$limit === null ? null : (int) $limit,
				$offset === null ? null : (int) $offset
			)
		);

		return new JsonResponse(
			map(
				fn (BackofficeCourseResponse $course): array => [
					'id' => $course->id(),
					'name' => $course->name(),
					'duration' => $course->duration(),
				],
				$response->courses()
			),
			200,
			['Access-Control-Allow-Origin' => '*']
		);
	}
}
```

## File: `apps/backoffice/backend/src/Controller/HealthCheck/HealthCheckGetController.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Apps\Backoffice\Backend\Controller\HealthCheck;

use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\HttpFoundation\Request;

final class HealthCheckGetController
{
	public function __invoke(Request $request): JsonResponse
	{
		return new JsonResponse(
			[
				'backoffice-backend' => 'ok',
			]
		);
	}
}
```

## File: `apps/backoffice/backend/src/Controller/Metrics/MetricsController.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Apps\Backoffice\Backend\Controller\Metrics;

use CodelyTv\Shared\Infrastructure\Monitoring\PrometheusMonitor;
use Prometheus\RenderTextFormat;
use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\Response;

final readonly class MetricsController
{
	public function __construct(private PrometheusMonitor $monitor) {}

	public function __invoke(Request $request): Response
	{
		$renderer = new RenderTextFormat();
		$result = $renderer->render($this->monitor->registry()->getMetricFamilySamples());

		return new Response($result, 200, ['Content-Type' => RenderTextFormat::MIME_TYPE]);
	}
}
```

## File: `apps/backoffice/frontend/config/bundles.php`
```php
<?php

declare(strict_types=1);

return [
	Symfony\Bundle\FrameworkBundle\FrameworkBundle::class => ['all' => true],
	FriendsOfBehat\SymfonyExtension\Bundle\FriendsOfBehatSymfonyExtensionBundle::class => ['test' => true],
	Symfony\Bundle\TwigBundle\TwigBundle::class => ['all' => true],
	//    WouterJ\EloquentBundle\WouterJEloquentBundle::class                                => ['test' => true]
];
```

## File: `apps/backoffice/frontend/config/services.yaml`
```yaml
imports:
  - { resource: ../../../../src/Backoffice/Shared/Infrastructure/Symfony/DependencyInjection/backoffice_services.yaml }
  - { resource: ../../../../src/Mooc/Shared/Infrastructure/Symfony/DependencyInjection/mooc_services.yaml }

framework:
  session:
    handler_id: null

services:
  _defaults:
    autoconfigure: true
    autowire: true

  # Configure
  _instanceof:
    CodelyTv\Shared\Domain\Bus\Event\DomainEventSubscriber:
      tags: ['codely.domain_event_subscriber']

    CodelyTv\Shared\Domain\Bus\Command\CommandHandler:
      tags: ['codely.command_handler']

    CodelyTv\Shared\Domain\Bus\Query\QueryHandler:
      tags: ['codely.query_handler']

  CodelyTv\Apps\Backoffice\Frontend\Controller\:
    resource: '../src/Controller'
    tags: ['controller.service_arguments']


  # Wire
  CodelyTv\Shared\:
    resource: '../../../../src/Shared'

  CodelyTv\Backoffice\:
    resource: '../../../../src/Backoffice'

  CodelyTv\Mooc\:
    resource: '../../../../src/Mooc'

  # -- TAGGING --
  CodelyTv\Shared\Infrastructure\Bus\Event\InMemory\InMemorySymfonyEventBus:
    arguments: [!tagged codely.domain_event_subscriber]
    lazy: true

  CodelyTv\Shared\Infrastructure\Bus\Event\DomainEventMapping:
    arguments: [!tagged codely.domain_event_subscriber]

  CodelyTv\Shared\Infrastructure\Bus\Event\DomainEventSubscriberLocator:
    arguments: [!tagged codely.domain_event_subscriber]

  CodelyTv\Shared\Infrastructure\Doctrine\DatabaseConnections:
    arguments: [!tagged codely.database_connection]

  CodelyTv\Shared\Infrastructure\Symfony\ApiExceptionListener:
    tags:
      - { name: kernel.event_listener, event: kernel.exception, method: onException }

  CodelyTv\Shared\Infrastructure\Symfony\AddJsonBodyToRequestListener:
    tags:
      - { name: kernel.event_listener, event: kernel.request, method: onKernelRequest }


  # -- APP DEFINITIONS --
  # Command/Query Handlers
  CodelyTv\Shared\Infrastructure\Bus\Command\InMemorySymfonyCommandBus:
    arguments: [!tagged codely.command_handler]

  CodelyTv\Shared\Infrastructure\Bus\Query\InMemorySymfonyQueryBus:
    arguments: [!tagged codely.query_handler]

  # RabbitMQ
  CodelyTv\Shared\Infrastructure\Bus\Event\RabbitMq\RabbitMqConnection:
    arguments:
      - host: '%env(RABBITMQ_HOST)%'
        port: '%env(RABBITMQ_PORT)%'
        vhost: '%env(RABBITMQ_MOOC_VHOST)%'
        login: '%env(RABBITMQ_LOGIN)%'
        password: '%env(RABBITMQ_PASSWORD)%'
        read_timeout: 2
        write_timeout: 2
        connect_timeout: 5

  CodelyTv\Shared\Infrastructure\Bus\Event\RabbitMq\RabbitMqEventBus:
    arguments: ['@CodelyTv\Shared\Infrastructure\Bus\Event\RabbitMq\RabbitMqConnection', '%env(RABBITMQ_EXCHANGE)%']

  CodelyTv\Shared\Infrastructure\Elasticsearch\ElasticsearchClient:
    factory: '@CodelyTv\Shared\Infrastructure\Elasticsearch\ElasticsearchClientFactory'
    arguments:
      - '%env(BACKOFFICE_ELASTICSEARCH_HOST)%'
      - '%env(BACKOFFICE_ELASTICSEARCH_INDEX_PREFIX)%'
      - '%kernel.project_dir%/../../../etc/databases/backoffice'
      - '%env(APP_ENV)%'
    public: true

  CodelyTv\Shared\Infrastructure\Bus\Event\WithMonitoring\WithPrometheusMonitoringEventBus:
    arguments: ['@CodelyTv\Shared\Infrastructure\Monitoring\PrometheusMonitor', 'backoffice_frontend', '@CodelyTv\Shared\Infrastructure\Bus\Event\RabbitMq\RabbitMqEventBus']

  # -- IMPLEMENTATIONS SELECTOR --
  CodelyTv\Shared\Domain\Bus\Event\EventBus: '@CodelyTv\Shared\Infrastructure\Bus\Event\WithMonitoring\WithPrometheusMonitoringEventBus'
  CodelyTv\Backoffice\Courses\Domain\BackofficeCourseRepository: '@CodelyTv\Backoffice\Courses\Infrastructure\Persistence\ElasticsearchBackofficeCourseRepository'

twig:
  default_path: '%kernel.project_dir%/templates'
  strict_variables: true
  globals:
    flash: '@CodelyTv\Shared\Infrastructure\Symfony\FlashSession'
```

## File: `apps/backoffice/frontend/config/services_test.yaml`
```yaml
framework:
  test: true

services:
  _defaults:
    autoconfigure: true
    autowire: true

  CodelyTv\Tests\:
    resource: '../../../../tests'

  # -- IMPLEMENTATIONS SELECTOR --
  CodelyTv\Shared\Domain\Bus\Event\EventBus: '@CodelyTv\Shared\Infrastructure\Bus\Event\InMemory\InMemorySymfonyEventBus'
```

## File: `apps/backoffice/frontend/config/routes/api_courses.yaml`
```yaml
api_courses_get:
  path: /api/courses
  controller: CodelyTv\Apps\Backoffice\Frontend\Controller\Courses\ApiCoursesGetController
  methods:  [GET]
```

## File: `apps/backoffice/frontend/config/routes/courses.yaml`
```yaml
courses_get:
  path: /courses
  controller: CodelyTv\Apps\Backoffice\Frontend\Controller\Courses\CoursesGetWebController
  methods:  [GET]

courses_post:
  path: /courses
  controller: CodelyTv\Apps\Backoffice\Frontend\Controller\Courses\CoursesPostWebController
  methods:  [POST]
```

## File: `apps/backoffice/frontend/config/routes/health-check.yaml`
```yaml
health-check_get:
  path: /health-check
  controller: CodelyTv\Apps\Backoffice\Frontend\Controller\HealthCheck\HealthCheckGetController
  methods:  [GET]
```

## File: `apps/backoffice/frontend/config/routes/home.yaml`
```yaml
home_get:
  path: /
  controller: CodelyTv\Apps\Backoffice\Frontend\Controller\Home\HomeGetWebController
  methods:  [GET]
```

## File: `apps/backoffice/frontend/config/routes/metrics.yaml`
```yaml
metrics_get:
  path: /metrics
  controller: CodelyTv\Apps\Backoffice\Frontend\Controller\Metrics\MetricsController
  methods:  [GET]
```

## File: `apps/backoffice/frontend/config/services/framework.yaml`
```yaml
framework:
  secret: '%env(APP_SECRET)%'
  #csrf_protection: true
  #http_method_override: true

  # Enables session support. Note that the session will ONLY be started if you read or write from it.
  # Remove or comment this section to explicitly disable session support.
  session:
    handler_id: null
    cookie_secure: auto
    cookie_samesite: lax
    enabled: true

  #esi: true
  #fragments: true
  php_errors:
    log: true
```

## File: `apps/backoffice/frontend/public/index.php`
```php
<?php

declare(strict_types=1);

use CodelyTv\Apps\Backoffice\Frontend\BackofficeFrontendKernel;
use Symfony\Component\ErrorHandler\Debug;
use Symfony\Component\HttpFoundation\Request;

require dirname(__DIR__) . '/../../bootstrap.php';

if ($_SERVER['APP_DEBUG']) {
	umask(0000);

	Debug::enable();
}

if ($trustedProxies = $_SERVER['TRUSTED_PROXIES'] ?? $_ENV['TRUSTED_PROXIES'] ?? false) {
	Request::setTrustedProxies(
		explode(',', $trustedProxies),
		Request::HEADER_X_FORWARDED_FOR | Request::HEADER_X_FORWARDED_PORT | Request::HEADER_X_FORWARDED_PROTO
	);
}

if ($trustedHosts = $_SERVER['TRUSTED_HOSTS'] ?? $_ENV['TRUSTED_HOSTS'] ?? false) {
	Request::setTrustedHosts([$trustedHosts]);
}

$kernel = new BackofficeFrontendKernel($_SERVER['APP_ENV'], (bool) $_SERVER['APP_DEBUG']);
$request = Request::createFromGlobals();
$response = $kernel->handle($request);
$response->send();
$kernel->terminate($request, $response);
```

## File: `apps/backoffice/frontend/src/BackofficeFrontendKernel.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Apps\Backoffice\Frontend;

use Symfony\Bundle\FrameworkBundle\Kernel\MicroKernelTrait;
use Symfony\Component\Config\Loader\LoaderInterface;
use Symfony\Component\Config\Resource\FileResource;
use Symfony\Component\DependencyInjection\ContainerBuilder;
use Symfony\Component\HttpKernel\Kernel;

use function dirname;

class BackofficeFrontendKernel extends Kernel
{
	use MicroKernelTrait;

	private const string CONFIG_EXTS = '.{xml,yaml}';

	public function registerBundles(): iterable
	{
		$contents = require $this->getProjectDir() . '/config/bundles.php';
		foreach ($contents as $class => $envs) {
			if ($envs[$this->environment] ?? $envs['all'] ?? false) {
				yield new $class();
			}
		}
	}

	public function getProjectDir(): string
	{
		return dirname(__DIR__);
	}

	protected function configureContainer(ContainerBuilder $container, LoaderInterface $loader): void
	{
		$container->addResource(new FileResource($this->getProjectDir() . '/config/bundles.php'));
		$container->setParameter('.container.dumper.inline_class_loader', true);
		$confDir = $this->getProjectDir() . '/config';

		$loader->load($confDir . '/services' . self::CONFIG_EXTS, 'glob');
		$loader->load($confDir . '/services_' . $this->environment . self::CONFIG_EXTS, 'glob');
		$loader->load($confDir . '/services/*' . self::CONFIG_EXTS, 'glob');
	}
}
```

## File: `apps/backoffice/frontend/src/Command/ImportCoursesToElasticsearchCommand.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Apps\Backoffice\Frontend\Command;

use CodelyTv\Backoffice\Courses\Infrastructure\Persistence\ElasticsearchBackofficeCourseRepository;
use CodelyTv\Backoffice\Courses\Infrastructure\Persistence\MySqlBackofficeCourseRepository;
use Symfony\Component\Console\Command\Command;
use Symfony\Component\Console\Input\InputInterface;
use Symfony\Component\Console\Output\OutputInterface;

final class ImportCoursesToElasticsearchCommand extends Command
{
	public function __construct(
		private readonly MySqlBackofficeCourseRepository $mySqlRepository,
		private readonly ElasticsearchBackofficeCourseRepository $elasticRepository
	) {
		parent::__construct();
	}

	public function execute(InputInterface $input, OutputInterface $output): int
	{
		$courses = $this->mySqlRepository->searchAll();

		foreach ($courses as $course) {
			$this->elasticRepository->save($course);
		}

		return 0;
	}
}
```

## File: `apps/backoffice/frontend/src/Controller/Courses/CoursesGetWebController.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Apps\Backoffice\Frontend\Controller\Courses;

use CodelyTv\Mooc\CoursesCounter\Application\Find\CoursesCounterResponse;
use CodelyTv\Mooc\CoursesCounter\Application\Find\FindCoursesCounterQuery;
use CodelyTv\Shared\Domain\ValueObject\SimpleUuid;
use CodelyTv\Shared\Infrastructure\Symfony\WebController;
use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\Response;

final class CoursesGetWebController extends WebController
{
	public function __invoke(Request $request): Response
	{
		/** @var CoursesCounterResponse $coursesCounterResponse */
		$coursesCounterResponse = $this->ask(new FindCoursesCounterQuery());

		return $this->render(
			'pages/courses/courses.html.twig',
			[
				'title' => 'Courses',
				'description' => 'Courses CodelyTV - Backoffice',
				'courses_counter' => $coursesCounterResponse->total(),
				'new_course_id' => SimpleUuid::random()->value(),
			]
		);
	}

	protected function exceptions(): array
	{
		return [];
	}
}
```

## File: `apps/backoffice/frontend/src/Controller/Courses/CoursesPostWebController.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Apps\Backoffice\Frontend\Controller\Courses;

use CodelyTv\Mooc\Courses\Application\Create\CreateCourseCommand;
use CodelyTv\Shared\Infrastructure\Symfony\WebController;
use Symfony\Component\HttpFoundation\RedirectResponse;
use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\Validator\Constraints as Assert;
use Symfony\Component\Validator\ConstraintViolationListInterface;
use Symfony\Component\Validator\Validation;

final class CoursesPostWebController extends WebController
{
	public function __invoke(Request $request): RedirectResponse
	{
		$validationErrors = $this->validateRequest($request);

		return $validationErrors->count()
			? $this->redirectWithErrors('courses_get', $validationErrors, $request)
			: $this->createCourse($request);
	}

	protected function exceptions(): array
	{
		return [];
	}

	private function validateRequest(Request $request): ConstraintViolationListInterface
	{
		$constraint = new Assert\Collection(
			[
				'id' => new Assert\Uuid(),
				'name' => [new Assert\NotBlank(), new Assert\Length(['min' => 1, 'max' => 255])],
				'duration' => [new Assert\NotBlank(), new Assert\Length(['min' => 4, 'max' => 100])],
			]
		);

		$input = $request->request->all();

		return Validation::createValidator()->validate($input, $constraint);
	}

	private function createCourse(Request $request): RedirectResponse
	{
		$this->dispatch(
			new CreateCourseCommand(
				(string) $request->request->get('id'),
				(string) $request->request->get('name'),
				(string) $request->request->get('duration')
			)
		);

		return $this->redirectWithMessage(
			'courses_get',
			sprintf('Feliciades, el curso %s ha sido creado!', $request->request->getAlpha('name'))
		);
	}
}
```

## File: `apps/backoffice/frontend/src/Controller/HealthCheck/HealthCheckGetController.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Apps\Backoffice\Frontend\Controller\HealthCheck;

use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\HttpFoundation\Request;

final class HealthCheckGetController
{
	public function __invoke(Request $request): JsonResponse
	{
		return new JsonResponse(
			[
				'backoffice-frontend' => 'ok',
			]
		);
	}
}
```

## File: `apps/backoffice/frontend/src/Controller/Home/HomeGetWebController.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Apps\Backoffice\Frontend\Controller\Home;

use CodelyTv\Shared\Infrastructure\Symfony\WebController;
use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\Response;

final class HomeGetWebController extends WebController
{
	public function __invoke(Request $request): Response
	{
		return $this->render('pages/home.html.twig', [
			'title' => 'Welcome',
			'description' => 'CodelyTV - Backoffice',
		]);
	}

	protected function exceptions(): array
	{
		return [];
	}
}
```

## File: `apps/backoffice/frontend/src/Controller/Metrics/MetricsController.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Apps\Backoffice\Frontend\Controller\Metrics;

use CodelyTv\Shared\Infrastructure\Monitoring\PrometheusMonitor;
use Prometheus\RenderTextFormat;
use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\Response;

final readonly class MetricsController
{
	public function __construct(private PrometheusMonitor $monitor) {}

	public function __invoke(Request $request): Response
	{
		$renderer = new RenderTextFormat();
		$result = $renderer->render($this->monitor->registry()->getMetricFamilySamples());

		return new Response($result, 200, ['Content-Type' => RenderTextFormat::MIME_TYPE]);
	}
}
```

## File: `apps/backoffice/frontend/templates/master.html.twig`
```
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link href="https://unpkg.com/tailwindcss@^1.0/dist/tailwind.min.css" rel="stylesheet">

    <title>{{ title }}</title>
    <title>{{ description }}</title>
</head>
<body>
{{ include('partials/header.html.twig') }}

{% if flash.has('message') %}
    <div class="flex items-center bg-blue-500 text-white text-sm font-bold px-4 py-3" role="alert">
        <svg class="fill-current w-4 h-4 mr-2" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20">
            <path d="M12.432 0c1.34 0 2.01.912 2.01 1.957 0 1.305-1.164 2.512-2.679 2.512-1.269 0-2.009-.75-1.974-1.99C9.789 1.436 10.67 0 12.432 0zM8.309 20c-1.058 0-1.833-.652-1.093-3.524l1.214-5.092c.211-.814.246-1.141 0-1.141-.317 0-1.689.562-2.502 1.117l-.528-.88c2.572-2.186 5.531-3.467 6.801-3.467 1.057 0 1.233 1.273.705 3.23l-1.391 5.352c-.246.945-.141 1.271.106 1.271.317 0 1.357-.392 2.379-1.207l.6.814C12.098 19.02 9.365 20 8.309 20z"/>
        </svg>
        <p>{{ flash.get('message') }}</p>
    </div>
{% endif %}

<div class="container mx-auto px-4 p-5">
    <h1 class="font-sans text-gray-800 text-center text-5xl mb-10">{% block page_title %}{% endblock %}</h1>
    {% block main %}{% endblock %}
</div>

<div class="clearfix"></div>
{{ include('partials/footer.html.twig') }}

</body>
</html>
```

## File: `apps/backoffice/frontend/templates/pages/home.html.twig`
```
{% extends 'master.html.twig' %}

{% block page_title %}HOME{% endblock %}

{% block main %}
    HOLIII HOME
{% endblock %}
```

## File: `apps/backoffice/frontend/templates/pages/courses/courses.html.twig`
```
{% extends 'master.html.twig' %}

{% block page_title %}Cursos{% endblock %}

{% block main %}
    <div class="max-w-sm rounded overflow-hidden shadow-lg float-left">
        <img class="w-full" src="https://codely.tv/pro/img/bg/cursos-codelytv-pro.png" alt="Sunset in the mountains">
        <div class="px-6 py-4">
            <div class="font-bold text-xl mb-2">Cursos</div>
            <p class="text-gray-700 text-base">
                Actualmente CodelyTV Pro cuenta con <b>{{ courses_counter }}</b> cursos.
            </p>
        </div>
    </div>
    {{ include('pages/courses/partials/new_course_form.html.twig') }}
    <div class="clearfix mb-10"></div>
    <hr class="mb-10">
    {{ include('pages/courses/partials/list_courses.html.twig') }}
{% endblock %}
```

## File: `apps/backoffice/frontend/templates/pages/courses/partials/list_courses.html.twig`
```
<h3 class="font-sans text-gray-800 text-center text-3xl mb-10">Cursos existentes</h3>


<form action="" method="get" id="courses-filters" name="filter-courses">
    <div id="filter-rows">

    </div>
    <div class="clearfix"></div>
    <div class="mt-10 inline-block relative w-2/4">
        <button class="md:w-1/4 bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
                id="add-field-button"
                onclick="addFilter(event)">
            Añadir filtro
        </button>

        <button class="md:w-1/4 bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
                id="filter-button"
                onclick="filterCourses(event)">
            👉 Filtrar 👈
        </button>
    </div>
</form>
<table class="text-left w-full border-collapse">
    <thead>
    <tr>
        <th class="py-4 px-6 bg-grey-lightest font-bold uppercase text-sm text-grey-dark border-b border-grey-light">
            Id
        </th>
        <th class="py-4 px-6 bg-grey-lightest font-bold uppercase text-sm text-grey-dark border-b border-grey-light">
            Nombre
        </th>
        <th class="py-4 px-6 bg-grey-lightest font-bold uppercase text-sm text-grey-dark border-b border-grey-light">
            Duración
        </th>
    </tr>
    </thead>
    <tbody id="courses-list">

    </tbody>
</table>

<script>


    function addCoursesList(url) {
        console.log(url);

        const tableBody = document.getElementById("courses-list");

        fetch(url)
            .then(function (response) {
                return response.json();
            })
            .then(function (courses) {
                tableBody.innerHTML = "";

                courses.forEach(function (course) {
                    let courseRow = document.createElement("tr");

                    courseRow.appendChild(tableCellFor(course.id));
                    courseRow.appendChild(tableCellFor(course.name));
                    courseRow.appendChild(tableCellFor(course.duration));

                    tableBody.appendChild(courseRow);
                })
            });
    }

    function tableCellFor(text) {
        const cell = document.createElement("td");

        cell.appendChild(document.createTextNode(text));

        return cell;
    }

    function addFilter(e) {
        e.preventDefault();

        const filterRows = document.getElementById('filter-rows');
        const totalRows  = document.getElementById('filter-rows').childElementCount;

        const filterRowTemplate = "<div class=\"filter-row\">\n" +
                                  "    <div class=\"inline-block relative w-64 mr-3\">\n" +
                                  "        <label class=\"block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2\" for=\"field\">\n" +
                                  "            Campo\n" +
                                  "        </label>\n" +
                                  "        <select name=\"filters[" +
                                  totalRows +
                                  "][field]\" id=\"field\"\n" +
                                  "                class=\"block appearance-none w-full bg-white border border-gray-400 hover:border-gray-500 px-4 py-2 pr-8 rounded shadow leading-tight focus:outline-none focus:shadow-outline\">\n" +
                                  "            <option value=\"id\">Identificador</option>\n" +
                                  "            <option value=\"name\">Nombre</option>\n" +
                                  "            <option value=\"duration\">Duración</option>\n" +
                                  "        </select>\n" +
                                  "        <div class=\"pointer-events-none absolute inset-y-0 right-0 flex items-center px-2 text-gray-700\">\n" +
                                  "            <svg class=\"fill-current h-4 w-4\" xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 20 20\">\n" +
                                  "                <path d=\"M9.293 12.95l.707.707L15.657 8l-1.414-1.414L10 10.828 5.757 6.586 4.343 8z\"/>\n" +
                                  "            </svg>\n" +
                                  "        </div>\n" +
                                  "    </div>\n" +
                                  "    <div class=\"inline-block relative w-64 mr-3\">\n" +
                                  "        <label class=\"block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2\" for=\"operator\">\n" +
                                  "            Operador\n" +
                                  "        </label>\n" +
                                  "        <select id=\"operator\" name=\"filters[" +
                                  totalRows +
                                  "][operator]\"\n" +
                                  "                class=\"block appearance-none w-full bg-white border border-gray-400 hover:border-gray-500 px-4 py-2 pr-8 rounded shadow leading-tight focus:outline-none focus:shadow-outline\">\n" +
                                  "            <option value=\"=\">es exactamente igual</option>\n" +
                                  "            <option value=\"CONTAINS\">contiene</option>\n" +
                                  "            <option value=\">\">es más grande que</option>\n" +
                                  "            <option value=\"<\">es más pequeño que</option>\n" +
                                  "        </select>\n" +
                                  "        <div class=\"pointer-events-none absolute inset-y-0 right-0 flex items-center px-2 text-gray-700\">\n" +
                                  "            <svg class=\"fill-current h-4 w-4\" xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 20 20\">\n" +
                                  "                <path d=\"M9.293 12.95l.707.707L15.657 8l-1.414-1.414L10 10.828 5.757 6.586 4.343 8z\"/>\n" +
                                  "            </svg>\n" +
                                  "        </div>\n" +
                                  "    </div>\n" +
                                  "    <div class=\"inline-block relative w-64 mr-3\">\n" +
                                  "        <label class=\"block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2\" for=\"value\">\n" +
                                  "            Valor\n" +
                                  "        </label>\n" +
                                  "        <input class=\"appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500\"\n" +
                                  "               id=\"value\" type=\"text\" name=\"filters[" +
                                  totalRows +
                                  "][value]\" placeholder=\"Lo que sea...\">\n" +
                                  "    </div>\n" +
                                  "</div>";

        filterRows.insertAdjacentHTML('beforeend', filterRowTemplate);
    }

    function filterCourses(e) {
        e.preventDefault();

        const form = document.forms["filter-courses"];

        const inputs = Array.from(form.getElementsByTagName("input"))
                            .concat(Array.from(form.getElementsByTagName("select")));

        const urlParts = inputs.map(input => input.name + "=" + input.value);

        const url = "http://localhost:8040/courses?" + urlParts.join("&");

        addCoursesList(url);
    }
</script>

<script>
    addCoursesList("http://localhost:8040/courses");
</script>
```

## File: `apps/backoffice/frontend/templates/pages/courses/partials/new_course_form.html.twig`
```
<form class="w-full max-w-lg float-right" method="post" action="{{ path('courses_post') }}">
    <h2 class="block uppercase tracking-wide text-gray-700 text-3xl font-bold mb-2">Crear curso</h2>
    <div class="flex flex-wrap mb-6 -mx-3">
        <div class="w-full md:w-full px-3 mb-6 md:mb-0">
            <label class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" for="grid-first-name">
                Identificador
            </label>
            <input class="{% if flash.has('errors.id') %}border border-red-500{% endif %} appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
                   id="grid-first-name" type="text" name="id" placeholder="En formado UUID"
                   value="{{ flash.get('inputs.id', new_course_id) }}">

            {% if flash.has('errors.id') %}
                <p class="text-red-500 text-xs italic">{{ flash.get('errors.id') }}</p>
            {% endif %}
        </div>
    </div>
    <div class="flex flex-wrap -mx-3 mb-6">
        <div class="w-full md:w-1/2 px-3 mb-6 md:mb-0">
            <label class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" for="grid-first-name">
                Nombre
            </label>
            <input class="{% if flash.has('errors.name') %}border border-red-500{% endif %} appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
                   id="grid-first-name" type="text" name="name" placeholder="DDD en PHP"
                   value="{{ flash.get('inputs.name') }}">

            {% if flash.has('errors.name') %}
                <p class="text-red-500 text-xs italic">{{ flash.get('errors.name') }}</p>
            {% endif %}
        </div>
        <div class="w-full md:w-1/2 px-3">
            <label class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" for="grid-last-name">
                Duración (en inglés)
            </label>
            <input class="{% if flash.has('errors.duration') %}border border-red-500{% endif %} appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
                   id="grid-last-name" type="text" name="duration" placeholder="8 days"
                   value="{{ flash.get('inputs.duration') }}">
            {% if flash.has('errors.duration') %}
                <p class="text-red-500 text-xs italic">{{ flash.get('errors.duration') }}</p>
            {% endif %}
        </div>
    </div>
    <div class="flex flex-wrap mb-6">
        <button class="md:w-full bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
                type="submit">
            Crear curso!
        </button>
    </div>
</form>
```

## File: `apps/backoffice/frontend/templates/partials/footer.html.twig`
```
<footer class="flex items-center justify-between flex-wrap bg-teal-900 p-5 mt-10">
    <div class="container mx-auto px-4">
        <p class="text-teal-200">
            🤙 CodelyTV - El mejor backoffice de la historia
        </p>
    </div>
</footer>
```

## File: `apps/backoffice/frontend/templates/partials/header.html.twig`
```
<header>
    <nav class="flex items-center justify-between flex-wrap bg-teal-900 p-5">
        <div class="flex items-center flex-shrink-0 text-white mr-6">
            <a href="{{ path('home_get') }}">
                <img src="images/logo.png" alt="" width="150px">
            </a>
        </div>
        <div class="w-full block flex-grow lg:flex lg:items-center lg:w-auto">
            <div class="text-sm lg:flex-grow">
                <a href="#"
                   class="block mt-4 lg:inline-block lg:mt-0 text-teal-200 hover:text-white mr-4">
                    Usuarios
                </a>
                <a href="{{ path('courses_get') }}"
                   class="block mt-4 lg:inline-block lg:mt-0 text-teal-200 hover:text-white mr-4">
                    Cursos
                </a>
                <a href="#" class="block mt-4 lg:inline-block lg:mt-0 text-teal-200 hover:text-white">
                    Vídeos
                </a>
            </div>
            <div>
                <a href="#"
                   class="inline-block text-sm px-4 py-2 leading-none border rounded text-white border-white hover:border-transparent hover:text-teal-500 hover:bg-white mt-4 lg:mt-0">Entrar</a>
            </div>
        </div>
    </nav>
</header>
```

## File: `apps/mooc/backend/config/bundles.php`
```php
<?php

declare(strict_types=1);

return [
	Symfony\Bundle\FrameworkBundle\FrameworkBundle::class => ['all' => true],
	FriendsOfBehat\SymfonyExtension\Bundle\FriendsOfBehatSymfonyExtensionBundle::class => ['test' => true],
	//    WouterJ\EloquentBundle\WouterJEloquentBundle::class                                => ['test' => true]
];
```

## File: `apps/mooc/backend/config/services.yaml`
```yaml
imports:
  - { resource: ../../../../src/Mooc/Shared/Infrastructure/Symfony/DependencyInjection/mooc_services.yaml }

services:
  _defaults:
    autoconfigure: true
    autowire: true

  # Configure
  _instanceof:
    CodelyTv\Shared\Domain\Bus\Event\DomainEventSubscriber:
      tags: ['codely.domain_event_subscriber']

    CodelyTv\Shared\Domain\Bus\Command\CommandHandler:
      tags: ['codely.command_handler']

    CodelyTv\Shared\Domain\Bus\Query\QueryHandler:
      tags: ['codely.query_handler']

  CodelyTv\Apps\Mooc\Backend\Controller\:
    resource: '../src/Controller'
    tags: ['controller.service_arguments']

  CodelyTv\Apps\Mooc\Backend\Command\:
    resource: '../src/Command'
    tags: ['console.command']

  # Wire
  CodelyTv\Shared\:
    resource: '../../../../src/Shared'

  CodelyTv\Mooc\:
    resource: '../../../../src/Mooc'

  # -- TAGGING --
  CodelyTv\Shared\Infrastructure\Bus\Event\InMemory\InMemorySymfonyEventBus:
    arguments: [!tagged codely.domain_event_subscriber]
    lazy: true

  CodelyTv\Shared\Infrastructure\Bus\Event\DomainEventMapping:
    arguments: [!tagged codely.domain_event_subscriber]

  CodelyTv\Shared\Infrastructure\Bus\Event\DomainEventSubscriberLocator:
    arguments: [!tagged codely.domain_event_subscriber]

  CodelyTv\Shared\Infrastructure\Doctrine\DatabaseConnections:
    arguments: [!tagged codely.database_connection]

  CodelyTv\Shared\Infrastructure\Symfony\AddJsonBodyToRequestListener:
    tags:
      - { name: kernel.event_listener, event: kernel.request, method: onKernelRequest }

  CodelyTv\Shared\Infrastructure\Symfony\ApiExceptionListener:
    tags:
      - { name: kernel.event_listener, event: kernel.exception, method: onException }


  # -- APP DEFINITIONS --
  # Command/Query Handlers
  CodelyTv\Shared\Infrastructure\Bus\Command\InMemorySymfonyCommandBus:
    arguments: [!tagged codely.command_handler]

  CodelyTv\Shared\Infrastructure\Bus\Query\InMemorySymfonyQueryBus:
    arguments: [!tagged codely.query_handler]

  # RabbitMQ
  CodelyTv\Shared\Infrastructure\Bus\Event\RabbitMq\RabbitMqConnection:
    arguments:
      - host: '%env(RABBITMQ_HOST)%'
        port: '%env(RABBITMQ_PORT)%'
        vhost: '%env(RABBITMQ_MOOC_VHOST)%'
        login: '%env(RABBITMQ_LOGIN)%'
        password: '%env(RABBITMQ_PASSWORD)%'
        read_timeout: 2
        write_timeout: 2
        connect_timeout: 5

  CodelyTv\Shared\Infrastructure\Bus\Event\RabbitMq\RabbitMqEventBus:
    arguments: ['@CodelyTv\Shared\Infrastructure\Bus\Event\RabbitMq\RabbitMqConnection', '%env(RABBITMQ_EXCHANGE)%']

  CodelyTv\Shared\Infrastructure\Bus\Event\RabbitMq\RabbitMqDomainEventsConsumer:
    arguments:
      - '@CodelyTv\Shared\Infrastructure\Bus\Event\RabbitMq\RabbitMqConnection'
      - '@CodelyTv\Shared\Infrastructure\Bus\Event\DomainEventJsonDeserializer'
      - '%env(RABBITMQ_EXCHANGE)%'
      - '%env(RABBITMQ_MAX_RETRIES)%'

  CodelyTv\Apps\Mooc\Backend\Command\DomainEvents\RabbitMq\ConfigureRabbitMqCommand:
    arguments:
      - '@CodelyTv\Shared\Infrastructure\Bus\Event\RabbitMq\RabbitMqConfigurer'
      - '%env(RABBITMQ_EXCHANGE)%'
      - !tagged codely.domain_event_subscriber

  CodelyTv\Shared\Infrastructure\Bus\Event\WithMonitoring\WithPrometheusMonitoringEventBus:
    arguments: ['@CodelyTv\Shared\Infrastructure\Monitoring\PrometheusMonitor', 'mooc_backend', '@CodelyTv\Shared\Infrastructure\Bus\Event\RabbitMq\RabbitMqEventBus']

  # -- IMPLEMENTATIONS SELECTOR --
  CodelyTv\Shared\Domain\Bus\Event\EventBus: '@CodelyTv\Shared\Infrastructure\Bus\Event\WithMonitoring\WithPrometheusMonitoringEventBus'
```

## File: `apps/mooc/backend/config/services_test.yaml`
```yaml
framework:
  test: true

services:
  _defaults:
    autoconfigure: true
    autowire: true

  CodelyTv\Tests\:
    resource: '../../../../tests'

  # Instance selector
  CodelyTv\Shared\Domain\RandomNumberGenerator: '@CodelyTv\Tests\Shared\Infrastructure\ConstantRandomNumberGenerator'
#  CodelyTv\Shared\Domain\Bus\Event\EventBus: '@CodelyTv\Shared\Infrastructure\Bus\Event\InMemory\InMemorySymfonyEventBus'
```

## File: `apps/mooc/backend/config/routes/courses.yaml`
```yaml
courses_put:
  path: /courses/{id}
  controller: CodelyTv\Apps\Mooc\Backend\Controller\Courses\CoursesPutController
  methods:  [PUT]
```

## File: `apps/mooc/backend/config/routes/courses_counter.yaml`
```yaml
courses_counter_get:
  path: /courses-counter
  controller: CodelyTv\Apps\Mooc\Backend\Controller\CoursesCounter\CoursesCounterGetController
  methods:  [GET]
```

## File: `apps/mooc/backend/config/routes/health-check.yaml`
```yaml
health-check_get:
  path: /health-check
  controller: CodelyTv\Apps\Mooc\Backend\Controller\HealthCheck\HealthCheckGetController
  methods:  [GET]
```

## File: `apps/mooc/backend/config/routes/metrics.yaml`
```yaml
metrics_get:
  path: /metrics
  controller: CodelyTv\Apps\Mooc\Backend\Controller\Metrics\MetricsController
  methods:  [GET]
```

## File: `apps/mooc/backend/config/services/framework.yaml`
```yaml
framework:
  secret: '%env(APP_SECRET)%'
  #csrf_protection: true
  #http_method_override: true

  # Enables session support. Note that the session will ONLY be started if you read or write from it.
  # Remove or comment this section to explicitly disable session support.
  session:
    handler_id: ~
    cookie_secure: auto
    cookie_samesite: lax

  #esi: true
  #fragments: true
  php_errors:
    log: true
```

## File: `apps/mooc/backend/public/index.php`
```php
<?php

declare(strict_types=1);

use CodelyTv\Apps\Mooc\Backend\MoocBackendKernel;
use Symfony\Component\ErrorHandler\Debug;
use Symfony\Component\HttpFoundation\Request;

require dirname(__DIR__) . '/../../bootstrap.php';

if ($_SERVER['APP_DEBUG']) {
	umask(0000);

	Debug::enable();
}

if ($trustedProxies = $_SERVER['TRUSTED_PROXIES'] ?? $_ENV['TRUSTED_PROXIES'] ?? false) {
	Request::setTrustedProxies(
		explode(',', $trustedProxies),
		Request::HEADER_X_FORWARDED_FOR | Request::HEADER_X_FORWARDED_PORT | Request::HEADER_X_FORWARDED_PROTO
	);
}

if ($trustedHosts = $_SERVER['TRUSTED_HOSTS'] ?? $_ENV['TRUSTED_HOSTS'] ?? false) {
	Request::setTrustedHosts([$trustedHosts]);
}

$kernel = new MoocBackendKernel($_SERVER['APP_ENV'], (bool) $_SERVER['APP_DEBUG']);
$request = Request::createFromGlobals();
$response = $kernel->handle($request);
$response->send();
$kernel->terminate($request, $response);
```

## File: `apps/mooc/backend/src/MoocBackendKernel.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Apps\Mooc\Backend;

use Symfony\Bundle\FrameworkBundle\Kernel\MicroKernelTrait;
use Symfony\Component\Config\Loader\LoaderInterface;
use Symfony\Component\Config\Resource\FileResource;
use Symfony\Component\DependencyInjection\ContainerBuilder;
use Symfony\Component\HttpKernel\Kernel;

use function dirname;

class MoocBackendKernel extends Kernel
{
	use MicroKernelTrait;

	private const string CONFIG_EXTS = '.{xml,yaml}';

	public function registerBundles(): iterable
	{
		$contents = require $this->getProjectDir() . '/config/bundles.php';
		foreach ($contents as $class => $envs) {
			if ($envs[$this->environment] ?? $envs['all'] ?? false) {
				yield new $class();
			}
		}
	}

	public function getProjectDir(): string
	{
		return dirname(__DIR__);
	}

	protected function configureContainer(ContainerBuilder $container, LoaderInterface $loader): void
	{
		$container->addResource(new FileResource($this->getProjectDir() . '/config/bundles.php'));
		$container->setParameter('.container.dumper.inline_class_loader', true);
		$confDir = $this->getProjectDir() . '/config';

		$loader->load($confDir . '/services' . self::CONFIG_EXTS, 'glob');
		$loader->load($confDir . '/services_' . $this->environment . self::CONFIG_EXTS, 'glob');
		$loader->load($confDir . '/services/*' . self::CONFIG_EXTS, 'glob');
	}
}
```

## File: `apps/mooc/backend/src/Command/DomainEvents/PublishDomainEventsFromMutationsCommand.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Apps\Mooc\Backend\Command\DomainEvents;

use CodelyTv\Mooc\Courses\Infrastructure\Cdc\DatabaseMutationToCourseCreatedDomainEvent;
use CodelyTv\Shared\Domain\Bus\Event\EventBus;
use CodelyTv\Shared\Infrastructure\Cdc\DatabaseMutationAction;
use CodelyTv\Shared\Infrastructure\Cdc\DatabaseMutationToDomainEvent;
use Doctrine\ORM\EntityManager;
use RuntimeException;
use Symfony\Component\Console\Attribute\AsCommand;
use Symfony\Component\Console\Command\Command;
use Symfony\Component\Console\Input\InputArgument;
use Symfony\Component\Console\Input\InputInterface;
use Symfony\Component\Console\Output\OutputInterface;

#[AsCommand(
	name: 'codely:domain-events:generate-from-mutations',
	description: 'Publish domain events from mutations',
)]
final class PublishDomainEventsFromMutationsCommand extends Command
{
	private array $transformers;

	public function __construct(
		private readonly EntityManager $entityManager,
		private readonly EventBus $eventBus
	) {
		parent::__construct();

		$this->transformers = [
			'courses' => [
				DatabaseMutationAction::INSERT->value => DatabaseMutationToCourseCreatedDomainEvent::class,
				DatabaseMutationAction::UPDATE->value => null,
				DatabaseMutationAction::DELETE->value => null,
			],
		];
	}

	protected function configure(): void
	{
		$this->addArgument('quantity', InputArgument::REQUIRED, 'Quantity of mutations to process');
	}

	protected function execute(InputInterface $input, OutputInterface $output): int
	{
		$totalMutations = (int) $input->getArgument('quantity');

		$this->entityManager->wrapInTransaction(function (EntityManager $entityManager) use ($totalMutations) {
			$mutations = $entityManager->getConnection()
				->executeQuery("SELECT * FROM mutations ORDER BY id ASC LIMIT $totalMutations FOR UPDATE")
				->fetchAllAssociative();

			foreach ($mutations as $mutation) {
				$transformer = $this->findTransformer($mutation['table_name'], $mutation['operation']);

				if ($transformer === null) {
					echo sprintf("Ignoring %s %s\n", $mutation['table_name'], $mutation['operation']);
					continue;
				}

				$domainEvents = $transformer->transform($mutation);

				$this->eventBus->publish(...$domainEvents);
			}

			$entityManager->getConnection()->executeStatement(
				sprintf('DELETE FROM mutations WHERE id IN (%s)', implode(',', array_column($mutations, 'id')))
			);
		});

		return 0;
	}

	private function findTransformer(string $tableName, string $operation): ?DatabaseMutationToDomainEvent
	{
		if (!array_key_exists($tableName, $this->transformers) && array_key_exists(
			$operation,
			$this->transformers[$tableName]
		)) {
			throw new RuntimeException("Transformer not found for table $tableName and operation $operation");
		}

		/** @var class-string<DatabaseMutationToDomainEvent>|null $class */
		$class = $this->transformers[$tableName][$operation];

		return $class ? new $class() : null;
	}
}
```

## File: `apps/mooc/backend/src/Command/DomainEvents/MySql/ConsumeMySqlDomainEventsCommand.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Apps\Mooc\Backend\Command\DomainEvents\MySql;

use CodelyTv\Shared\Domain\Bus\Event\DomainEvent;
use CodelyTv\Shared\Infrastructure\Bus\Event\DomainEventSubscriberLocator;
use CodelyTv\Shared\Infrastructure\Bus\Event\MySql\MySqlDoctrineDomainEventsConsumer;
use CodelyTv\Shared\Infrastructure\Doctrine\DatabaseConnections;
use Symfony\Component\Console\Attribute\AsCommand;
use Symfony\Component\Console\Command\Command;
use Symfony\Component\Console\Input\InputArgument;
use Symfony\Component\Console\Input\InputInterface;
use Symfony\Component\Console\Output\OutputInterface;

use function Lambdish\Phunctional\pipe;

#[AsCommand(name: 'codely:domain-events:mysql:consume', description: 'Consume domain events from MySql',)]
final class ConsumeMySqlDomainEventsCommand extends Command
{
	public function __construct(
		private readonly MySqlDoctrineDomainEventsConsumer $consumer,
		private readonly DatabaseConnections $connections,
		private readonly DomainEventSubscriberLocator $subscriberLocator
	) {
		parent::__construct();
	}

	protected function configure(): void
	{
		$this->addArgument('quantity', InputArgument::REQUIRED, 'Quantity of events to process');
	}

	protected function execute(InputInterface $input, OutputInterface $output): int
	{
		$quantityEventsToProcess = (int) $input->getArgument('quantity');

		$consumer = pipe($this->consumer(), fn () => $this->connections->clear());

		$this->consumer->consume($consumer, $quantityEventsToProcess);

		return 0;
	}

	private function consumer(): callable
	{
		return function (DomainEvent $domainEvent): void {
			$subscribers = $this->subscriberLocator->allSubscribedTo($domainEvent::class);

			foreach ($subscribers as $subscriber) {
				$subscriber($domainEvent);
			}
		};
	}
}
```

## File: `apps/mooc/backend/src/Command/DomainEvents/RabbitMq/ConfigureRabbitMqCommand.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Apps\Mooc\Backend\Command\DomainEvents\RabbitMq;

use CodelyTv\Shared\Infrastructure\Bus\Event\RabbitMq\RabbitMqConfigurer;
use Symfony\Component\Console\Attribute\AsCommand;
use Symfony\Component\Console\Command\Command;
use Symfony\Component\Console\Input\InputInterface;
use Symfony\Component\Console\Output\OutputInterface;
use Traversable;

#[AsCommand(
	name: 'codely:domain-events:rabbitmq:configure',
	description: 'Configure the RabbitMQ to allow publish & consume domain events',
)]
final class ConfigureRabbitMqCommand extends Command
{
	public function __construct(
		private readonly RabbitMqConfigurer $configurer,
		private readonly string $exchangeName,
		private readonly Traversable $subscribers
	) {
		parent::__construct();
	}

	protected function execute(InputInterface $input, OutputInterface $output): int
	{
		$this->configurer->configure($this->exchangeName, ...iterator_to_array($this->subscribers));

		return 0;
	}
}
```

## File: `apps/mooc/backend/src/Command/DomainEvents/RabbitMq/ConsumeRabbitMqDomainEventsCommand.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Apps\Mooc\Backend\Command\DomainEvents\RabbitMq;

use CodelyTv\Shared\Infrastructure\Bus\Event\DomainEventSubscriberLocator;
use CodelyTv\Shared\Infrastructure\Bus\Event\RabbitMq\RabbitMqDomainEventsConsumer;
use CodelyTv\Shared\Infrastructure\Doctrine\DatabaseConnections;
use Symfony\Component\Console\Attribute\AsCommand;
use Symfony\Component\Console\Command\Command;
use Symfony\Component\Console\Input\InputArgument;
use Symfony\Component\Console\Input\InputInterface;
use Symfony\Component\Console\Output\OutputInterface;

use function Lambdish\Phunctional\repeat;

#[AsCommand(
	name: 'codely:domain-events:rabbitmq:consume',
	description: 'Consume domain events from the RabbitMQ',
)]
final class ConsumeRabbitMqDomainEventsCommand extends Command
{
	public function __construct(
		private readonly RabbitMqDomainEventsConsumer $consumer,
		private readonly DatabaseConnections $connections,
		private readonly DomainEventSubscriberLocator $locator
	) {
		parent::__construct();
	}

	protected function configure(): void
	{
		$this
			->addArgument('queue', InputArgument::REQUIRED, 'Queue name')
			->addArgument('quantity', InputArgument::REQUIRED, 'Quantity of events to process');
	}

	protected function execute(InputInterface $input, OutputInterface $output): int
	{
		$queueName = $input->getArgument('queue');
		$eventsToProcess = (int) $input->getArgument('quantity');

		repeat($this->consumer($queueName), $eventsToProcess);

		return 0;
	}

	private function consumer(string $queueName): callable
	{
		return function () use ($queueName): void {
			$subscriber = $this->locator->withRabbitMqQueueNamed($queueName);

			$this->consumer->consume($subscriber, $queueName);

			$this->connections->clear();
		};
	}
}
```

## File: `apps/mooc/backend/src/Command/DomainEvents/RabbitMq/GenerateSupervisorRabbitMqConsumerFilesCommand.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Apps\Mooc\Backend\Command\DomainEvents\RabbitMq;

use CodelyTv\Shared\Domain\Bus\Event\DomainEventSubscriber;
use CodelyTv\Shared\Infrastructure\Bus\Event\DomainEventSubscriberLocator;
use CodelyTv\Shared\Infrastructure\Bus\Event\RabbitMq\RabbitMqQueueNameFormatter;
use Symfony\Component\Console\Attribute\AsCommand;
use Symfony\Component\Console\Command\Command;
use Symfony\Component\Console\Input\InputArgument;
use Symfony\Component\Console\Input\InputInterface;
use Symfony\Component\Console\Output\OutputInterface;

use function Lambdish\Phunctional\each;

#[AsCommand(
	name: 'codely:domain-events:rabbitmq:generate-supervisor-files',
	description: 'Generate the supervisor configuration for every RabbitMQ subscriber',
)]
final class GenerateSupervisorRabbitMqConsumerFilesCommand extends Command
{
	private const EVENTS_TO_PROCESS_AT_TIME = 200;
	private const NUMBERS_OF_PROCESSES_PER_SUBSCRIBER = 1;
	private const SUPERVISOR_PATH = __DIR__ . '/../../../../build/supervisor';

	public function __construct(private readonly DomainEventSubscriberLocator $locator)
	{
		parent::__construct();
	}

	protected function configure(): void
	{
		$this->addArgument('command-path', InputArgument::OPTIONAL, 'Path on this is gonna be deployed', '/var/www');
	}

	protected function execute(InputInterface $input, OutputInterface $output): int
	{
		$path = $input->getArgument('command-path');

		each($this->configCreator($path), $this->locator->all());

		return 0;
	}

	private function configCreator(string $path): callable
	{
		return function (DomainEventSubscriber $subscriber) use ($path): void {
			$queueName = RabbitMqQueueNameFormatter::format($subscriber);
			$subscriberName = RabbitMqQueueNameFormatter::shortFormat($subscriber);

			$fileContent = str_replace(
				['{subscriber_name}', '{queue_name}', '{path}', '{processes}', '{events_to_process}', ],
				[
					$subscriberName,
					$queueName,
					$path,
					self::NUMBERS_OF_PROCESSES_PER_SUBSCRIBER,
					self::EVENTS_TO_PROCESS_AT_TIME,
				],
				$this->template()
			);

			file_put_contents($this->fileName($subscriberName), $fileContent);
		};
	}

	private function template(): string
	{
		return <<<EOF
            [program:codelytv_{queue_name}]
            command      = {path}/apps/mooc/backend/bin/console codely:domain-events:rabbitmq:consume --env=prod {queue_name} {events_to_process}
            process_name = %(program_name)s_%(process_num)02d
            numprocs     = {processes}
            startsecs    = 1
            startretries = 10
            exitcodes    = 2
            stopwaitsecs = 300
            autostart    = true
            EOF;
	}

	private function fileName(string $queue): string
	{
		return sprintf('%s/%s.ini', self::SUPERVISOR_PATH, $queue);
	}
}
```

## File: `apps/mooc/backend/src/Controller/Courses/CoursesPutController.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Apps\Mooc\Backend\Controller\Courses;

use CodelyTv\Mooc\Courses\Application\Create\CreateCourseCommand;
use CodelyTv\Shared\Infrastructure\Symfony\ApiController;
use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\Response;

final class CoursesPutController extends ApiController
{
	public function __invoke(string $id, Request $request): Response
	{
		$this->dispatch(
			new CreateCourseCommand(
				$id,
				(string) $request->request->get('name'),
				(string) $request->request->get('duration')
			)
		);

		return new Response('', Response::HTTP_CREATED);
	}

	protected function exceptions(): array
	{
		return [];
	}
}
```

## File: `apps/mooc/backend/src/Controller/CoursesCounter/CoursesCounterGetController.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Apps\Mooc\Backend\Controller\CoursesCounter;

use CodelyTv\Mooc\CoursesCounter\Application\Find\CoursesCounterResponse;
use CodelyTv\Mooc\CoursesCounter\Application\Find\FindCoursesCounterQuery;
use CodelyTv\Mooc\CoursesCounter\Domain\CoursesCounterNotExist;
use CodelyTv\Shared\Infrastructure\Symfony\ApiController;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\HttpFoundation\Response;

final class CoursesCounterGetController extends ApiController
{
	public function __invoke(): JsonResponse
	{
		/** @var CoursesCounterResponse $response */
		$response = $this->ask(new FindCoursesCounterQuery());

		return new JsonResponse(
			[
				'total' => $response->total(),
			]
		);
	}

	protected function exceptions(): array
	{
		return [
			CoursesCounterNotExist::class => Response::HTTP_NOT_FOUND,
		];
	}
}
```

## File: `apps/mooc/backend/src/Controller/HealthCheck/HealthCheckGetController.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Apps\Mooc\Backend\Controller\HealthCheck;

use CodelyTv\Shared\Domain\RandomNumberGenerator;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\HttpFoundation\Request;

final readonly class HealthCheckGetController
{
	public function __construct(private RandomNumberGenerator $generator) {}

	public function __invoke(Request $request): JsonResponse
	{
		return new JsonResponse(
			[
				'mooc-backend' => 'ok',
				'rand' => $this->generator->generate(),
			]
		);
	}
}
```

## File: `apps/mooc/backend/src/Controller/Metrics/MetricsController.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Apps\Mooc\Backend\Controller\Metrics;

use CodelyTv\Shared\Infrastructure\Monitoring\PrometheusMonitor;
use Prometheus\RenderTextFormat;
use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\Response;

final readonly class MetricsController
{
	public function __construct(private PrometheusMonitor $monitor) {}

	public function __invoke(Request $request): Response
	{
		$renderer = new RenderTextFormat();
		$result = $renderer->render($this->monitor->registry()->getMetricFamilySamples());

		return new Response($result, 200, ['Content-Type' => RenderTextFormat::MIME_TYPE]);
	}
}
```

## File: `apps/mooc/backend/tests/mooc_backend.yml`
```yaml
mooc_backend:
  extensions:
    FriendsOfBehat\SymfonyExtension:
      kernel:
        class: CodelyTv\Apps\Mooc\Backend\MoocBackendKernel
      bootstrap: apps/bootstrap.php
    Behat\MinkExtension:
      sessions:
        symfony:
          symfony: ~
      base_url: ''

  suites:
    health_check:
      paths: [ apps/mooc/backend/tests/features/health_check ]
      contexts:
        - CodelyTv\Tests\Shared\Infrastructure\Behat\ApiContext

    courses:
      paths: [ apps/mooc/backend/tests/features/courses ]
      contexts:
        - CodelyTv\Tests\Shared\Infrastructure\Behat\ApplicationFeatureContext
        - CodelyTv\Tests\Shared\Infrastructure\Behat\ApiContext

    courses_counter:
      paths: [ apps/mooc/backend/tests/features/courses_counter ]
      contexts:
        - CodelyTv\Tests\Shared\Infrastructure\Behat\ApplicationFeatureContext
        - CodelyTv\Tests\Shared\Infrastructure\Behat\ApiContext
```

## File: `apps/mooc/backend/tests/features/courses/course_put.feature`
```
Feature: Create a new course
  In order to have courses on the platform
  As a user with admin permissions
  I want to create a new course

  Scenario: A valid non existing course
    Given I send a PUT request to "/courses/1aab45ba-3c7a-4344-8936-78466eca77fa" with body:
    """
    {
      "name": "The best course",
      "duration": "5 hours"
    }
    """
    Then the response status code should be 201
    And the response should be empty
```

## File: `apps/mooc/backend/tests/features/courses_counter/courses_counter_get.feature`
```
Feature: Obtain the total number of courses
  In order to have a courses counter
  As a user
  I want to see the courses counter

  Scenario: With one course
    Given I send an event to the event bus:
    """
    {
      "data": {
        "id": "c77fa036-cbc7-4414-996b-c6a7a93cae09",
        "type": "course.created",
        "occurred_on": "2019-08-08T08:37:32+00:00",
        "attributes": {
          "id": "8c900b20-e04a-4777-9183-32faab6d2fb5",
          "name": "DDD en PHP!",
          "duration": "25 hours"
        },
        "meta" : {
          "host": "111.26.06.93"
        }
      }
    }
    """
    When I send a "GET" request to "/courses-counter"
    Then the response status code should be 200
    And the response content should be:
    """
    {
      "total": 1
    }
    """

  Scenario: With more than one course having duplicates
    Given I send an event to the event bus:
    """
    {
      "data": {
        "id": "c77fa036-cbc7-4414-996b-c6a7a93cae09",
        "type": "course.created",
        "occurred_on": "2019-08-08T08:37:32+00:00",
        "attributes": {
          "id": "8c900b20-e04a-4777-9183-32faab6d2fb5",
          "name": "DDD en PHP!",
          "duration": "25 hours"
        },
        "meta" : {
          "host": "111.26.06.93"
        }
      }
    }
    """
    And I send an event to the event bus:
    """
    {
      "data": {
        "id": "8c4a4ed8-9458-489e-a167-b099d81fa096",
        "type": "course.created",
        "occurred_on": "2019-08-09T08:36:32+00:00",
        "attributes": {
          "id": "8c4a4ed8-9458-489e-a167-b099d81fa096",
          "name": "DDD en Java",
          "duration": "24 hours"
        },
        "meta" : {
          "host": "111.26.06.93"
        }
      }
    }
    """
    And I send an event to the event bus:
    """
    {
      "data": {
        "id": "8c4a4ed8-9458-489e-a167-b099d81fa096",
        "type": "course.created",
        "occurred_on": "2019-08-09T08:36:32+00:00",
        "attributes": {
          "id": "8c4a4ed8-9458-489e-a167-b099d81fa096",
          "name": "DDD en Java",
          "duration": "24 hours"
        },
        "meta" : {
          "host": "111.26.06.93"
        }
      }
    }
    """
    When I send a "GET" request to "/courses-counter"
    Then the response status code should be 200
    And the response content should be:
    """
    {
      "total": 2
    }
    """
```

## File: `apps/mooc/backend/tests/features/health_check/health_check_get.feature`
```
Feature: Api status
  In order to know the server is up and running
  As a health check
  I want to check the api status

  Scenario: Check the api status
    Given I send a GET request to "/health-check"
    Then the response content should be:
    """
    {
      "mooc-backend": "ok",
      "rand": 1
    }
    """
```

## File: `etc/databases/mooc.sql`
```sql
/* -------------------------
        MOOC CONTEXT
---------------------------- */

-- Generic tables

CREATE TABLE mutations (
	id BIGINT AUTO_INCREMENT PRIMARY KEY,
	table_name VARCHAR(255) NOT NULL,
	operation ENUM ('INSERT', 'UPDATE', 'DELETE') NOT NULL,
	old_value JSON NULL,
	new_value JSON NULL,
	mutation_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8mb4
  COLLATE = utf8mb4_unicode_ci;

CREATE TABLE domain_events (
	id CHAR(36) NOT NULL,
	aggregate_id CHAR(36) NOT NULL,
	name VARCHAR(255) NOT NULL,
	body JSON NOT NULL,
	occurred_on TIMESTAMP NOT NULL,
	PRIMARY KEY (id)
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8mb4
  COLLATE = utf8mb4_unicode_ci;

-- Aggregates tables

CREATE TABLE courses (
	id CHAR(36) NOT NULL,
	name VARCHAR(255) NOT NULL,
	duration VARCHAR(255) NOT NULL,
	PRIMARY KEY (id)
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8mb4
  COLLATE = utf8mb4_unicode_ci;

CREATE TRIGGER after_courses_insert
	AFTER INSERT
	ON courses
	FOR EACH ROW
BEGIN
	INSERT INTO mutations (table_name, operation, new_value, mutation_timestamp)
	VALUES ('courses', 'INSERT', JSON_OBJECT('id', new.id, 'name', new.name, 'duration', new.duration), NOW());
END;

CREATE TRIGGER after_courses_update
	AFTER UPDATE
	ON courses
	FOR EACH ROW
BEGIN
	INSERT INTO mutations (table_name, operation, old_value, new_value, mutation_timestamp)
	VALUES ('courses',
			'UPDATE',
			JSON_OBJECT('id', old.id, 'name', old.name, 'duration', old.duration),
			JSON_OBJECT('id', new.id, 'name', new.name, 'duration', new.duration),
			NOW());
END;

CREATE TRIGGER after_courses_delete
	AFTER DELETE
	ON courses
	FOR EACH ROW
BEGIN
	INSERT INTO mutations (table_name, operation, old_value, mutation_timestamp)
	VALUES ('courses', 'DELETE', JSON_OBJECT('id', old.id, 'name', old.name, 'duration', old.duration), NOW());
END;

CREATE TABLE courses_counter (
	id CHAR(36) NOT NULL,
	total INT NOT NULL,
	existing_courses JSON NOT NULL,
	PRIMARY KEY (id)
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8mb4
  COLLATE = utf8mb4_unicode_ci;

INSERT INTO courses_counter (id, total, existing_courses)
VALUES ("cdf26d7d-3deb-4e8c-9f73-4ac085a8d6f3", 0, "[]");

CREATE TABLE steps (
	id CHAR(36) NOT NULL,
	title VARCHAR(255) NOT NULL,
	duration INT NOT NULL,
	type VARCHAR(255) NOT NULL,
	PRIMARY KEY (id)
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8mb4
  COLLATE = utf8mb4_unicode_ci;

CREATE TABLE steps_video (
	id CHAR(36) NOT NULL,
	url VARCHAR(255) NOT NULL,
	FOREIGN KEY (id) REFERENCES steps(id) ON DELETE CASCADE
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8mb4
  COLLATE = utf8mb4_unicode_ci;

CREATE TABLE steps_exercise (
	id CHAR(36) NOT NULL,
	content VARCHAR(255) NOT NULL,
	FOREIGN KEY (id) REFERENCES steps(id) ON DELETE CASCADE
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8mb4
  COLLATE = utf8mb4_unicode_ci;

CREATE TABLE steps_quiz (
	id CHAR(36) NOT NULL,
	questions TEXT NOT NULL,
	FOREIGN KEY (id) REFERENCES steps(id) ON DELETE CASCADE
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8mb4
  COLLATE = utf8mb4_unicode_ci;


/* -------------------------
      BACKOFFICE CONTEXT
---------------------------- */

CREATE TABLE backoffice_courses (
	id CHAR(36) NOT NULL,
	name VARCHAR(255) NOT NULL,
	duration VARCHAR(255) NOT NULL,
	PRIMARY KEY (id)
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8mb4
  COLLATE = utf8mb4_unicode_ci;
```

## File: `etc/databases/backoffice/courses.json`
```json
{
  "mappings": {
    "courses": {
      "properties": {
        "id": {
          "type": "keyword",
          "index": true
        },
        "name": {
          "type": "text",
          "index": true
        },
        "duration": {
          "type": "text",
          "index": true
        }
      }
    }
  }
}
```

## File: `etc/endpoints/backoffice_frontend.http`
```
# ELASTIC - Search
POST localhost:9200/backoffice_courses/_search
Content-Type: application/json

{
  "query": {
    "term": {
      "name": "Pepe"
    }
  }
}

###
# ELASTIC - Search
POST localhost:9200/backoffice_courses/_search
Content-Type: application/json

###

```

## File: `etc/endpoints/mooc_backend.http`
```
# Create a course
PUT localhost:8030/courses/{{$uuid}}
Content-Type: application/json

{
  "name": "The best course",
  "duration": "5 hours"
}

###
```

## File: `etc/infrastructure/php/php.ini`
```
date.timezone = "UTC"
html_errors = "On"
display_errors = "On"
error_reporting = E_ALL
```

## File: `etc/infrastructure/php/conf.d/apcu.ini`
```
apc.enable_cli=1
apc.enabled=1
apc.shm_segments=1
apc.shm_size=256M
apc.num_files_hint=7000
apc.user_entries_hint=4096
apc.ttl=7200
apc.user_ttl=7200
apc.gc_ttl=3600
apc.max_file_size=1M
apc.stat=1
```

## File: `etc/infrastructure/php/conf.d/opcache.ini`
```
opcache.memory_consumption=128
opcache.interned_strings_buffer=8
opcache.max_accelerated_files=4000
opcache.revalidate_freq=60
opcache.fast_shutdown=1
opcache.enable_cli=1
```

## File: `etc/infrastructure/php/conf.d/xdebug.ini`
```
zend_extension = xdebug.so

;Debugging
xdebug.mode=debug
xdebug.start_with_request = yes
xdebug.discover_client_host = yes
xdebug.client_port = 9001
xdebug.client_host = host.docker.internal

;Profiling
xdebug.mode=profile
xdebug.start_with_request=trigger

xdebug.output_dir = "/tmp/xdebug"
xdebug.max_nesting_level = 500
```

## File: `etc/prometheus/prometheus.yml`
```yaml
scrape_configs:

  - job_name: 'prometheus'
    scrape_interval: 5s
    static_configs:
      - targets: ['localhost:9090']

  - job_name: 'backoffice_backend'
    scrape_interval: 5s
    static_configs:
      - targets: ['codelytv-php_ddd_skeleton-backoffice_backend-php:8040']

  - job_name: 'backoffice_frontend'
    scrape_interval: 5s
    static_configs:
      - targets: ['codelytv-php_ddd_skeleton-backoffice_frontend-php:8041']

  - job_name: 'mooc_backend'
    scrape_interval: 5s
    static_configs:
      - targets: ['codelytv-php_ddd_skeleton-mooc_backend-php:8030']
```

## File: `src/Analytics/DomainEvents/Application/Store/DomainEventStorer.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Analytics\DomainEvents\Application\Store;

use CodelyTv\Analytics\DomainEvents\Domain\AnalyticsDomainEvent;
use CodelyTv\Analytics\DomainEvents\Domain\AnalyticsDomainEventAggregateId;
use CodelyTv\Analytics\DomainEvents\Domain\AnalyticsDomainEventBody;
use CodelyTv\Analytics\DomainEvents\Domain\AnalyticsDomainEventId;
use CodelyTv\Analytics\DomainEvents\Domain\AnalyticsDomainEventName;
use CodelyTv\Analytics\DomainEvents\Domain\DomainEventsRepository;

final readonly class DomainEventStorer
{
	public function __construct(private DomainEventsRepository $repository) {}

	public function store(
		AnalyticsDomainEventId $id,
		AnalyticsDomainEventAggregateId $aggregateId,
		AnalyticsDomainEventName $name,
		AnalyticsDomainEventBody $body
	): void {
		$domainEvent = new AnalyticsDomainEvent($id, $aggregateId, $name, $body);

		$this->repository->save($domainEvent);
	}
}
```

## File: `src/Analytics/DomainEvents/Application/Store/StoreDomainEventOnOccurred.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Analytics\DomainEvents\Application\Store;

use CodelyTv\Analytics\DomainEvents\Domain\AnalyticsDomainEventAggregateId;
use CodelyTv\Analytics\DomainEvents\Domain\AnalyticsDomainEventBody;
use CodelyTv\Analytics\DomainEvents\Domain\AnalyticsDomainEventId;
use CodelyTv\Analytics\DomainEvents\Domain\AnalyticsDomainEventName;
use CodelyTv\Shared\Domain\Bus\Event\DomainEvent;
use CodelyTv\Shared\Domain\Bus\Event\DomainEventSubscriber;

final readonly class StoreDomainEventOnOccurred implements DomainEventSubscriber
{
	public function __construct(private DomainEventStorer $storer) {}

	public static function subscribedTo(): array
	{
		return [DomainEvent::class];
	}

	public function __invoke(DomainEvent $event): void
	{
		$id = new AnalyticsDomainEventId($event->eventId());
		$aggregateId = new AnalyticsDomainEventAggregateId($event->aggregateId());
		$name = new AnalyticsDomainEventName($event::eventName());
		$body = new AnalyticsDomainEventBody($event->toPrimitives());

		$this->storer->store($id, $aggregateId, $name, $body);
	}
}
```

## File: `src/Analytics/DomainEvents/Domain/AnalyticsDomainEvent.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Analytics\DomainEvents\Domain;

final readonly class AnalyticsDomainEvent
{
	public function __construct(
		private AnalyticsDomainEventId $id,
		private AnalyticsDomainEventAggregateId $aggregateId,
		private AnalyticsDomainEventName $name,
		private AnalyticsDomainEventBody $body
	) {}
}
```

## File: `src/Analytics/DomainEvents/Domain/AnalyticsDomainEventAggregateId.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Analytics\DomainEvents\Domain;

use CodelyTv\Shared\Domain\ValueObject\Uuid;

final class AnalyticsDomainEventAggregateId extends Uuid {}
```

## File: `src/Analytics/DomainEvents/Domain/AnalyticsDomainEventBody.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Analytics\DomainEvents\Domain;

final readonly class AnalyticsDomainEventBody
{
	public function __construct(private array $value) {}

	public function value(): array
	{
		return $this->value;
	}
}
```

## File: `src/Analytics/DomainEvents/Domain/AnalyticsDomainEventId.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Analytics\DomainEvents\Domain;

use CodelyTv\Shared\Domain\ValueObject\Uuid;

final class AnalyticsDomainEventId extends Uuid {}
```

## File: `src/Analytics/DomainEvents/Domain/AnalyticsDomainEventName.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Analytics\DomainEvents\Domain;

use CodelyTv\Shared\Domain\ValueObject\StringValueObject;

final class AnalyticsDomainEventName extends StringValueObject {}
```

## File: `src/Analytics/DomainEvents/Domain/DomainEventsRepository.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Analytics\DomainEvents\Domain;

interface DomainEventsRepository
{
	public function save(AnalyticsDomainEvent $event): void;
}
```

## File: `src/Backoffice/Auth/Application/Authenticate/AuthenticateUserCommand.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Backoffice\Auth\Application\Authenticate;

use CodelyTv\Shared\Domain\Bus\Command\Command;

final readonly class AuthenticateUserCommand implements Command
{
	public function __construct(private string $username, private string $password) {}

	public function username(): string
	{
		return $this->username;
	}

	public function password(): string
	{
		return $this->password;
	}
}
```

## File: `src/Backoffice/Auth/Application/Authenticate/AuthenticateUserCommandHandler.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Backoffice\Auth\Application\Authenticate;

use CodelyTv\Backoffice\Auth\Domain\AuthPassword;
use CodelyTv\Backoffice\Auth\Domain\AuthUsername;
use CodelyTv\Shared\Domain\Bus\Command\CommandHandler;

final readonly class AuthenticateUserCommandHandler implements CommandHandler
{
	public function __construct(private UserAuthenticator $authenticator) {}

	public function __invoke(AuthenticateUserCommand $command): void
	{
		$username = new AuthUsername($command->username());
		$password = new AuthPassword($command->password());

		$this->authenticator->authenticate($username, $password);
	}
}
```

## File: `src/Backoffice/Auth/Application/Authenticate/UserAuthenticator.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Backoffice\Auth\Application\Authenticate;

use CodelyTv\Backoffice\Auth\Domain\AuthPassword;
use CodelyTv\Backoffice\Auth\Domain\AuthRepository;
use CodelyTv\Backoffice\Auth\Domain\AuthUser;
use CodelyTv\Backoffice\Auth\Domain\AuthUsername;
use CodelyTv\Backoffice\Auth\Domain\InvalidAuthCredentials;
use CodelyTv\Backoffice\Auth\Domain\InvalidAuthUsername;

final readonly class UserAuthenticator
{
	public function __construct(private AuthRepository $repository) {}

	public function authenticate(AuthUsername $username, AuthPassword $password): void
	{
		$auth = $this->repository->search($username);

		if ($auth === null) {
			throw new InvalidAuthUsername($username);
		}

		$this->ensureCredentialsAreValid($auth, $password);
	}

	private function ensureCredentialsAreValid(AuthUser $auth, AuthPassword $password): void
	{
		if (!$auth->passwordMatches($password)) {
			throw new InvalidAuthCredentials($auth->username());
		}
	}
}
```

## File: `src/Backoffice/Auth/Domain/AuthPassword.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Backoffice\Auth\Domain;

use CodelyTv\Shared\Domain\ValueObject\StringValueObject;

final class AuthPassword extends StringValueObject
{
	public function isEquals(self $other): bool
	{
		return $this->value() === $other->value();
	}
}
```

## File: `src/Backoffice/Auth/Domain/AuthRepository.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Backoffice\Auth\Domain;

interface AuthRepository
{
	public function search(AuthUsername $username): ?AuthUser;
}
```

## File: `src/Backoffice/Auth/Domain/AuthUser.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Backoffice\Auth\Domain;

final readonly class AuthUser
{
	public function __construct(private AuthUsername $username, private AuthPassword $password) {}

	public function passwordMatches(AuthPassword $password): bool
	{
		return $this->password->isEquals($password);
	}

	public function username(): AuthUsername
	{
		return $this->username;
	}
}
```

## File: `src/Backoffice/Auth/Domain/AuthUsername.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Backoffice\Auth\Domain;

use CodelyTv\Shared\Domain\ValueObject\StringValueObject;

final class AuthUsername extends StringValueObject {}
```

## File: `src/Backoffice/Auth/Domain/InvalidAuthCredentials.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Backoffice\Auth\Domain;

use RuntimeException;

final class InvalidAuthCredentials extends RuntimeException
{
	public function __construct(AuthUsername $username)
	{
		parent::__construct(sprintf('The credentials for <%s> are invalid', $username->value()));
	}
}
```

## File: `src/Backoffice/Auth/Domain/InvalidAuthUsername.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Backoffice\Auth\Domain;

use RuntimeException;

final class InvalidAuthUsername extends RuntimeException
{
	public function __construct(AuthUsername $username)
	{
		parent::__construct(sprintf('The user <%s> does not exists', $username->value()));
	}
}
```

## File: `src/Backoffice/Auth/Infrastructure/Persistence/InMemoryAuthRepository.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Backoffice\Auth\Infrastructure\Persistence;

use CodelyTv\Backoffice\Auth\Domain\AuthPassword;
use CodelyTv\Backoffice\Auth\Domain\AuthRepository;
use CodelyTv\Backoffice\Auth\Domain\AuthUser;
use CodelyTv\Backoffice\Auth\Domain\AuthUsername;

use function Lambdish\Phunctional\get;

final class InMemoryAuthRepository implements AuthRepository
{
	private const USERS = [
		'javi' => 'barbitas',
		'rafa' => 'pelazo',
	];

	public function search(AuthUsername $username): ?AuthUser
	{
		$password = get($username->value(), self::USERS);

		return $password !== null ? new AuthUser($username, new AuthPassword($password)) : null;
	}
}
```

## File: `src/Backoffice/Courses/Application/BackofficeCourseResponse.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Backoffice\Courses\Application;

final readonly class BackofficeCourseResponse
{
	public function __construct(private string $id, private string $name, private string $duration) {}

	public function id(): string
	{
		return $this->id;
	}

	public function name(): string
	{
		return $this->name;
	}

	public function duration(): string
	{
		return $this->duration;
	}
}
```

## File: `src/Backoffice/Courses/Application/BackofficeCoursesResponse.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Backoffice\Courses\Application;

use CodelyTv\Shared\Domain\Bus\Query\Response;

final class BackofficeCoursesResponse implements Response
{
	private readonly array $courses;

	public function __construct(BackofficeCourseResponse ...$courses)
	{
		$this->courses = $courses;
	}

	public function courses(): array
	{
		return $this->courses;
	}
}
```

## File: `src/Backoffice/Courses/Application/Create/BackofficeCourseCreator.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Backoffice\Courses\Application\Create;

use CodelyTv\Backoffice\Courses\Domain\BackofficeCourse;
use CodelyTv\Backoffice\Courses\Domain\BackofficeCourseRepository;

final readonly class BackofficeCourseCreator
{
	public function __construct(private BackofficeCourseRepository $repository) {}

	public function create(string $id, string $name, string $duration): void
	{
		$this->repository->save(new BackofficeCourse($id, $name, $duration));
	}
}
```

## File: `src/Backoffice/Courses/Application/Create/CreateBackofficeCourseOnCourseCreated.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Backoffice\Courses\Application\Create;

use CodelyTv\Mooc\Courses\Domain\CourseCreatedDomainEvent;
use CodelyTv\Shared\Domain\Bus\Event\DomainEventSubscriber;

final readonly class CreateBackofficeCourseOnCourseCreated implements DomainEventSubscriber
{
	public function __construct(private BackofficeCourseCreator $creator) {}

	public static function subscribedTo(): array
	{
		return [CourseCreatedDomainEvent::class];
	}

	public function __invoke(CourseCreatedDomainEvent $event): void
	{
		$this->creator->create($event->aggregateId(), $event->name(), $event->duration());
	}
}
```

## File: `src/Backoffice/Courses/Application/SearchAll/AllBackofficeCoursesSearcher.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Backoffice\Courses\Application\SearchAll;

use CodelyTv\Backoffice\Courses\Application\BackofficeCourseResponse;
use CodelyTv\Backoffice\Courses\Application\BackofficeCoursesResponse;
use CodelyTv\Backoffice\Courses\Domain\BackofficeCourse;
use CodelyTv\Backoffice\Courses\Domain\BackofficeCourseRepository;

use function Lambdish\Phunctional\map;

final readonly class AllBackofficeCoursesSearcher
{
	public function __construct(private BackofficeCourseRepository $repository) {}

	public function searchAll(): BackofficeCoursesResponse
	{
		return new BackofficeCoursesResponse(...map($this->toResponse(), $this->repository->searchAll()));
	}

	private function toResponse(): callable
	{
		return static fn (BackofficeCourse $course): BackofficeCourseResponse => new BackofficeCourseResponse(
			$course->id(),
			$course->name(),
			$course->duration()
		);
	}
}
```

## File: `src/Backoffice/Courses/Application/SearchAll/SearchAllBackofficeCoursesQuery.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Backoffice\Courses\Application\SearchAll;

use CodelyTv\Shared\Domain\Bus\Query\Query;

final class SearchAllBackofficeCoursesQuery implements Query {}
```

## File: `src/Backoffice/Courses/Application/SearchAll/SearchAllBackofficeCoursesQueryHandler.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Backoffice\Courses\Application\SearchAll;

use CodelyTv\Backoffice\Courses\Application\BackofficeCoursesResponse;
use CodelyTv\Shared\Domain\Bus\Query\QueryHandler;

final readonly class SearchAllBackofficeCoursesQueryHandler implements QueryHandler
{
	public function __construct(private AllBackofficeCoursesSearcher $searcher) {}

	public function __invoke(SearchAllBackofficeCoursesQuery $query): BackofficeCoursesResponse
	{
		return $this->searcher->searchAll();
	}
}
```

## File: `src/Backoffice/Courses/Application/SearchByCriteria/BackofficeCoursesByCriteriaSearcher.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Backoffice\Courses\Application\SearchByCriteria;

use CodelyTv\Backoffice\Courses\Application\BackofficeCourseResponse;
use CodelyTv\Backoffice\Courses\Application\BackofficeCoursesResponse;
use CodelyTv\Backoffice\Courses\Domain\BackofficeCourse;
use CodelyTv\Backoffice\Courses\Domain\BackofficeCourseRepository;
use CodelyTv\Shared\Domain\Criteria\Criteria;
use CodelyTv\Shared\Domain\Criteria\Filters;
use CodelyTv\Shared\Domain\Criteria\Order;

use function Lambdish\Phunctional\map;

final readonly class BackofficeCoursesByCriteriaSearcher
{
	public function __construct(private BackofficeCourseRepository $repository) {}

	public function search(Filters $filters, Order $order, ?int $limit, ?int $offset): BackofficeCoursesResponse
	{
		$criteria = new Criteria($filters, $order, $offset, $limit);

		return new BackofficeCoursesResponse(...map($this->toResponse(), $this->repository->matching($criteria)));
	}

	private function toResponse(): callable
	{
		return static fn (BackofficeCourse $course): BackofficeCourseResponse => new BackofficeCourseResponse(
			$course->id(),
			$course->name(),
			$course->duration()
		);
	}
}
```

## File: `src/Backoffice/Courses/Application/SearchByCriteria/SearchBackofficeCoursesByCriteriaQuery.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Backoffice\Courses\Application\SearchByCriteria;

use CodelyTv\Shared\Domain\Bus\Query\Query;

final readonly class SearchBackofficeCoursesByCriteriaQuery implements Query
{
	public function __construct(
		private array $filters,
		private ?string $orderBy,
		private ?string $order,
		private ?int $limit,
		private ?int $offset
	) {}

	public function filters(): array
	{
		return $this->filters;
	}

	public function orderBy(): ?string
	{
		return $this->orderBy;
	}

	public function order(): ?string
	{
		return $this->order;
	}

	public function limit(): ?int
	{
		return $this->limit;
	}

	public function offset(): ?int
	{
		return $this->offset;
	}
}
```

## File: `src/Backoffice/Courses/Application/SearchByCriteria/SearchBackofficeCoursesByCriteriaQueryHandler.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Backoffice\Courses\Application\SearchByCriteria;

use CodelyTv\Backoffice\Courses\Application\BackofficeCoursesResponse;
use CodelyTv\Shared\Domain\Bus\Query\QueryHandler;
use CodelyTv\Shared\Domain\Criteria\Filters;
use CodelyTv\Shared\Domain\Criteria\Order;

final readonly class SearchBackofficeCoursesByCriteriaQueryHandler implements QueryHandler
{
	public function __construct(private BackofficeCoursesByCriteriaSearcher $searcher) {}

	public function __invoke(SearchBackofficeCoursesByCriteriaQuery $query): BackofficeCoursesResponse
	{
		$filters = Filters::fromValues($query->filters());
		$order = Order::fromValues($query->orderBy(), $query->order());

		return $this->searcher->search($filters, $order, $query->limit(), $query->offset());
	}
}
```

## File: `src/Backoffice/Courses/Domain/BackofficeCourse.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Backoffice\Courses\Domain;

use CodelyTv\Shared\Domain\Aggregate\AggregateRoot;

final class BackofficeCourse extends AggregateRoot
{
	public function __construct(private readonly string $id, private readonly string $name, private readonly string $duration) {}

	public static function fromPrimitives(array $primitives): self
	{
		return new self($primitives['id'], $primitives['name'], $primitives['duration']);
	}

	public function toPrimitives(): array
	{
		return [
			'id' => $this->id,
			'name' => $this->name,
			'duration' => $this->duration,
		];
	}

	public function id(): string
	{
		return $this->id;
	}

	public function name(): string
	{
		return $this->name;
	}

	public function duration(): string
	{
		return $this->duration;
	}
}
```

## File: `src/Backoffice/Courses/Domain/BackofficeCourseRepository.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Backoffice\Courses\Domain;

use CodelyTv\Shared\Domain\Criteria\Criteria;

interface BackofficeCourseRepository
{
	public function save(BackofficeCourse $course): void;

	public function searchAll(): array;

	public function matching(Criteria $criteria): array;
}
```

## File: `src/Backoffice/Courses/Infrastructure/Persistence/ElasticsearchBackofficeCourseRepository.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Backoffice\Courses\Infrastructure\Persistence;

use CodelyTv\Backoffice\Courses\Domain\BackofficeCourse;
use CodelyTv\Backoffice\Courses\Domain\BackofficeCourseRepository;
use CodelyTv\Shared\Domain\Criteria\Criteria;
use CodelyTv\Shared\Infrastructure\Persistence\Elasticsearch\ElasticsearchRepository;

use function Lambdish\Phunctional\map;

final class ElasticsearchBackofficeCourseRepository extends ElasticsearchRepository implements BackofficeCourseRepository
{
	public function save(BackofficeCourse $course): void
	{
		$this->persist($course->id(), $course->toPrimitives());
	}

	public function searchAll(): array
	{
		return map($this->toCourse(), $this->searchAllInElastic());
	}

	public function matching(Criteria $criteria): array
	{
		return map($this->toCourse(), $this->searchByCriteria($criteria));
	}

	protected function aggregateName(): string
	{
		return 'courses';
	}

	private function toCourse(): callable
	{
		return static fn (array $primitives): BackofficeCourse => BackofficeCourse::fromPrimitives($primitives);
	}
}
```

## File: `src/Backoffice/Courses/Infrastructure/Persistence/InMemoryCacheBackofficeCourseRepository.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Backoffice\Courses\Infrastructure\Persistence;

use CodelyTv\Backoffice\Courses\Domain\BackofficeCourse;
use CodelyTv\Backoffice\Courses\Domain\BackofficeCourseRepository;
use CodelyTv\Shared\Domain\Criteria\Criteria;

use function Lambdish\Phunctional\get;

final class InMemoryCacheBackofficeCourseRepository implements BackofficeCourseRepository
{
	private static array $allCoursesCache = [];
	private static array $matchingCache = [];

	public function __construct(private readonly BackofficeCourseRepository $repository) {}

	public function save(BackofficeCourse $course): void
	{
		$this->repository->save($course);
	}

	public function searchAll(): array
	{
		return empty(self::$allCoursesCache) ? $this->searchAllAndFillCache() : self::$allCoursesCache;
	}

	public function matching(Criteria $criteria): array
	{
		return get($criteria->serialize(), self::$matchingCache) ?: $this->searchMatchingAndFillCache($criteria);
	}

	private function searchAllAndFillCache(): array
	{
		return self::$allCoursesCache = $this->repository->searchAll();
	}

	private function searchMatchingAndFillCache(Criteria $criteria): array
	{
		return self::$matchingCache[$criteria->serialize()] = $this->repository->matching($criteria);
	}
}
```

## File: `src/Backoffice/Courses/Infrastructure/Persistence/MySqlBackofficeCourseRepository.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Backoffice\Courses\Infrastructure\Persistence;

use CodelyTv\Backoffice\Courses\Domain\BackofficeCourse;
use CodelyTv\Backoffice\Courses\Domain\BackofficeCourseRepository;
use CodelyTv\Shared\Domain\Criteria\Criteria;
use CodelyTv\Shared\Infrastructure\Persistence\Doctrine\DoctrineCriteriaConverter;
use CodelyTv\Shared\Infrastructure\Persistence\Doctrine\DoctrineRepository;

final class MySqlBackofficeCourseRepository extends DoctrineRepository implements BackofficeCourseRepository
{
	public function save(BackofficeCourse $course): void
	{
		$this->persist($course);
	}

	public function searchAll(): array
	{
		return $this->repository(BackofficeCourse::class)->findAll();
	}

	public function matching(Criteria $criteria): array
	{
		$doctrineCriteria = DoctrineCriteriaConverter::convert($criteria);

		return $this->repository(BackofficeCourse::class)->matching($doctrineCriteria)->toArray();
	}
}
```

## File: `src/Backoffice/Courses/Infrastructure/Persistence/Doctrine/BackofficeCourse.orm.xml`
```xml
<?xml version="1.0" encoding="UTF-8"?>
<doctrine-mapping xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                  xmlns="http://doctrine-project.org/schemas/orm/doctrine-mapping"
                  xsi:schemaLocation="http://doctrine-project.org/schemas/orm/doctrine-mapping
                          https://www.doctrine-project.org/schemas/orm/doctrine-mapping.xsd">

    <entity name="CodelyTv\Backoffice\Courses\Domain\BackofficeCourse" table="backoffice_courses">
        <id name="id" type="string" column="id" length="36" />
        <id name="name" type="string" column="name" length="255" />
        <id name="duration" type="string" column="duration" length="255" />
    </entity>
</doctrine-mapping>
```

## File: `src/Backoffice/Shared/Infrastructure/Symfony/DependencyInjection/backoffice_services.yaml`
```yaml
services:
  # Databases
  # @todo this should be from backoffice, no mooc
  Doctrine\ORM\EntityManager:
    factory: [ CodelyTv\Mooc\Shared\Infrastructure\Doctrine\MoocEntityManagerFactory, create ]
    arguments:
      - driver: '%env(MOOC_DATABASE_DRIVER)%'
        host: '%env(MOOC_DATABASE_HOST)%'
        port: '%env(MOOC_DATABASE_PORT)%'
        dbname: '%env(MOOC_DATABASE_NAME)%'
        user: '%env(MOOC_DATABASE_USER)%'
        password: '%env(MOOC_DATABASE_PASSWORD)%'
      - '%env(APP_ENV)%'
    tags:
      - { name: codely.database_connection }
    public: true
```

## File: `src/Mooc/Courses/Application/Create/CourseCreator.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Mooc\Courses\Application\Create;

use CodelyTv\Mooc\Courses\Domain\Course;
use CodelyTv\Mooc\Courses\Domain\CourseDuration;
use CodelyTv\Mooc\Courses\Domain\CourseName;
use CodelyTv\Mooc\Courses\Domain\CourseRepository;
use CodelyTv\Mooc\Shared\Domain\Courses\CourseId;
use CodelyTv\Shared\Domain\Bus\Event\EventBus;

final readonly class CourseCreator
{
	public function __construct(private CourseRepository $repository, private EventBus $bus) {}

	public function __invoke(CourseId $id, CourseName $name, CourseDuration $duration): void
	{
		$course = Course::create($id, $name, $duration);

		$this->repository->save($course);
		$this->bus->publish(...$course->pullDomainEvents());
	}
}
```

## File: `src/Mooc/Courses/Application/Create/CreateCourseCommand.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Mooc\Courses\Application\Create;

use CodelyTv\Shared\Domain\Bus\Command\Command;

final readonly class CreateCourseCommand implements Command
{
	public function __construct(private string $id, private string $name, private string $duration) {}

	public function id(): string
	{
		return $this->id;
	}

	public function name(): string
	{
		return $this->name;
	}

	public function duration(): string
	{
		return $this->duration;
	}
}
```

## File: `src/Mooc/Courses/Application/Create/CreateCourseCommandHandler.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Mooc\Courses\Application\Create;

use CodelyTv\Mooc\Courses\Domain\CourseDuration;
use CodelyTv\Mooc\Courses\Domain\CourseName;
use CodelyTv\Mooc\Shared\Domain\Courses\CourseId;
use CodelyTv\Shared\Domain\Bus\Command\CommandHandler;

final readonly class CreateCourseCommandHandler implements CommandHandler
{
	public function __construct(private CourseCreator $creator) {}

	public function __invoke(CreateCourseCommand $command): void
	{
		$id = new CourseId($command->id());
		$name = new CourseName($command->name());
		$duration = new CourseDuration($command->duration());

		$this->creator->__invoke($id, $name, $duration);
	}
}
```

## File: `src/Mooc/Courses/Application/Find/CourseFinder.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Mooc\Courses\Application\Find;

use CodelyTv\Mooc\Courses\Domain\Course;
use CodelyTv\Mooc\Courses\Domain\CourseNotExist;
use CodelyTv\Mooc\Courses\Domain\CourseRepository;
use CodelyTv\Mooc\Shared\Domain\Courses\CourseId;

final readonly class CourseFinder
{
	public function __construct(private CourseRepository $repository) {}

	public function __invoke(CourseId $id): Course
	{
		$course = $this->repository->search($id);

		if ($course === null) {
			throw new CourseNotExist($id);
		}

		return $course;
	}
}
```

## File: `src/Mooc/Courses/Application/Update/CourseRenamer.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Mooc\Courses\Application\Update;

use CodelyTv\Mooc\Courses\Application\Find\CourseFinder;
use CodelyTv\Mooc\Courses\Domain\CourseName;
use CodelyTv\Mooc\Courses\Domain\CourseRepository;
use CodelyTv\Mooc\Shared\Domain\Courses\CourseId;
use CodelyTv\Shared\Domain\Bus\Event\EventBus;

final readonly class CourseRenamer
{
	private CourseFinder $finder;

	public function __construct(private CourseRepository $repository, private EventBus $bus)
	{
		$this->finder = new CourseFinder($repository);
	}

	public function __invoke(CourseId $id, CourseName $newName): void
	{
		$course = $this->finder->__invoke($id);

		$course->rename($newName);

		$this->repository->save($course);
		$this->bus->publish(...$course->pullDomainEvents());
	}
}
```

## File: `src/Mooc/Courses/Domain/Course.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Mooc\Courses\Domain;

use CodelyTv\Mooc\Shared\Domain\Courses\CourseId;
use CodelyTv\Shared\Domain\Aggregate\AggregateRoot;

final class Course extends AggregateRoot
{
	public function __construct(private readonly CourseId $id, private CourseName $name, private readonly CourseDuration $duration) {}

	public static function create(CourseId $id, CourseName $name, CourseDuration $duration): self
	{
		$course = new self($id, $name, $duration);

		$course->record(new CourseCreatedDomainEvent($id->value(), $name->value(), $duration->value()));

		return $course;
	}

	public function id(): CourseId
	{
		return $this->id;
	}

	public function name(): CourseName
	{
		return $this->name;
	}

	public function duration(): CourseDuration
	{
		return $this->duration;
	}

	public function rename(CourseName $newName): void
	{
		$this->name = $newName;
	}
}
```

## File: `src/Mooc/Courses/Domain/CourseCreatedDomainEvent.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Mooc\Courses\Domain;

use CodelyTv\Shared\Domain\Bus\Event\DomainEvent;

final class CourseCreatedDomainEvent extends DomainEvent
{
	public function __construct(
		string $id,
		private readonly string $name,
		private readonly string $duration,
		string $eventId = null,
		string $occurredOn = null
	) {
		parent::__construct($id, $eventId, $occurredOn);
	}

	public static function eventName(): string
	{
		return 'course.created';
	}

	public static function fromPrimitives(
		string $aggregateId,
		array $body,
		string $eventId,
		string $occurredOn
	): DomainEvent {
		return new self($aggregateId, $body['name'], $body['duration'], $eventId, $occurredOn);
	}

	public function toPrimitives(): array
	{
		return [
			'name' => $this->name,
			'duration' => $this->duration,
		];
	}

	public function name(): string
	{
		return $this->name;
	}

	public function duration(): string
	{
		return $this->duration;
	}
}
```

## File: `src/Mooc/Courses/Domain/CourseDuration.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Mooc\Courses\Domain;

use CodelyTv\Shared\Domain\ValueObject\StringValueObject;

final class CourseDuration extends StringValueObject {}
```

## File: `src/Mooc/Courses/Domain/CourseName.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Mooc\Courses\Domain;

use CodelyTv\Shared\Domain\ValueObject\StringValueObject;

final class CourseName extends StringValueObject {}
```

## File: `src/Mooc/Courses/Domain/CourseNotExist.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Mooc\Courses\Domain;

use CodelyTv\Mooc\Shared\Domain\Courses\CourseId;
use CodelyTv\Shared\Domain\DomainError;

final class CourseNotExist extends DomainError
{
	public function __construct(private readonly CourseId $id)
	{
		parent::__construct();
	}

	public function errorCode(): string
	{
		return 'course_not_exist';
	}

	protected function errorMessage(): string
	{
		return sprintf('The course <%s> does not exist', $this->id->value());
	}
}
```

## File: `src/Mooc/Courses/Domain/CourseRepository.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Mooc\Courses\Domain;

use CodelyTv\Mooc\Shared\Domain\Courses\CourseId;

interface CourseRepository
{
	public function save(Course $course): void;

	public function search(CourseId $id): ?Course;
}
```

## File: `src/Mooc/Courses/Infrastructure/Cdc/DatabaseMutationToCourseCreatedDomainEvent.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Mooc\Courses\Infrastructure\Cdc;

use CodelyTv\Mooc\Courses\Domain\CourseCreatedDomainEvent;
use CodelyTv\Shared\Domain\Bus\Event\DomainEvent;
use CodelyTv\Shared\Domain\Utils;
use CodelyTv\Shared\Infrastructure\Cdc\DatabaseMutationAction;
use CodelyTv\Shared\Infrastructure\Cdc\DatabaseMutationToDomainEvent;

final class DatabaseMutationToCourseCreatedDomainEvent implements DatabaseMutationToDomainEvent
{
	/** @return DomainEvent[] */
	public function transform(array $data): array
	{
		$mutation = Utils::jsonDecode($data['new_value']);

		return [
			new CourseCreatedDomainEvent(
				$mutation['id'],
				$mutation['name'],
				$mutation['duration'],
				null,
				$data['mutation_timestamp'],
			),
		];
	}

	public function tableName(): string
	{
		return 'courses';
	}

	public function mutationAction(): DatabaseMutationAction
	{
		return DatabaseMutationAction::INSERT;
	}
}
```

## File: `src/Mooc/Courses/Infrastructure/Persistence/DoctrineCourseRepository.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Mooc\Courses\Infrastructure\Persistence;

use CodelyTv\Mooc\Courses\Domain\Course;
use CodelyTv\Mooc\Courses\Domain\CourseRepository;
use CodelyTv\Mooc\Shared\Domain\Courses\CourseId;
use CodelyTv\Shared\Infrastructure\Persistence\Doctrine\DoctrineRepository;

final class DoctrineCourseRepository extends DoctrineRepository implements CourseRepository
{
	public function save(Course $course): void
	{
		$this->persist($course);
	}

	public function search(CourseId $id): ?Course
	{
		return $this->repository(Course::class)->find($id);
	}
}
```

## File: `src/Mooc/Courses/Infrastructure/Persistence/FileCourseRepository.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Mooc\Courses\Infrastructure\Persistence;

use CodelyTv\Mooc\Courses\Domain\Course;
use CodelyTv\Mooc\Courses\Domain\CourseRepository;
use CodelyTv\Mooc\Shared\Domain\Courses\CourseId;

final class FileCourseRepository implements CourseRepository
{
	private const FILE_PATH = __DIR__ . '/courses';

	public function save(Course $course): void
	{
		file_put_contents($this->fileName($course->id()->value()), serialize($course));
	}

	public function search(CourseId $id): ?Course
	{
		return file_exists($this->fileName($id->value()))
			? unserialize(file_get_contents($this->fileName($id->value())))
			: null;
	}

	private function fileName(string $id): string
	{
		return sprintf('%s.%s.repo', self::FILE_PATH, $id);
	}
}
```

## File: `src/Mooc/Courses/Infrastructure/Persistence/Doctrine/Course.orm.xml`
```xml
<?xml version="1.0" encoding="UTF-8"?>
<doctrine-mapping xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                  xmlns="http://doctrine-project.org/schemas/orm/doctrine-mapping"
                  xsi:schemaLocation="http://doctrine-project.org/schemas/orm/doctrine-mapping
                          https://www.doctrine-project.org/schemas/orm/doctrine-mapping.xsd">

    <entity name="CodelyTv\Mooc\Courses\Domain\Course" table="courses">
        <id name="id" type="course_id" column="id" length="36" />

        <embedded name="name" class="CodelyTv\Mooc\Courses\Domain\CourseName" use-column-prefix="false" />
        <embedded name="duration" class="CodelyTv\Mooc\Courses\Domain\CourseDuration" use-column-prefix="false" />
    </entity>

</doctrine-mapping>
```

## File: `src/Mooc/Courses/Infrastructure/Persistence/Doctrine/CourseDuration.orm.xml`
```xml
<?xml version="1.0" encoding="UTF-8"?>
<doctrine-mapping xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                  xmlns="http://doctrine-project.org/schemas/orm/doctrine-mapping"
                  xsi:schemaLocation="http://doctrine-project.org/schemas/orm/doctrine-mapping
                          https://www.doctrine-project.org/schemas/orm/doctrine-mapping.xsd">

    <embeddable name="CodelyTv\Mooc\Courses\Domain\CourseDuration">
        <field name="value" type="string" column="duration" />
    </embeddable>

</doctrine-mapping>
```

## File: `src/Mooc/Courses/Infrastructure/Persistence/Doctrine/CourseIdType.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Mooc\Courses\Infrastructure\Persistence\Doctrine;

use CodelyTv\Mooc\Shared\Domain\Courses\CourseId;
use CodelyTv\Shared\Infrastructure\Persistence\Doctrine\UuidType;

final class CourseIdType extends UuidType
{
	protected function typeClassName(): string
	{
		return CourseId::class;
	}
}
```

## File: `src/Mooc/Courses/Infrastructure/Persistence/Doctrine/CourseName.orm.xml`
```xml
<?xml version="1.0" encoding="UTF-8"?>
<doctrine-mapping xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                  xmlns="http://doctrine-project.org/schemas/orm/doctrine-mapping"
                  xsi:schemaLocation="http://doctrine-project.org/schemas/orm/doctrine-mapping
                          https://www.doctrine-project.org/schemas/orm/doctrine-mapping.xsd">

    <embeddable name="CodelyTv\Mooc\Courses\Domain\CourseName">
        <field name="value" type="string" column="name" />
    </embeddable>

</doctrine-mapping>
```

## File: `src/Mooc/CoursesCounter/Application/Find/CoursesCounterFinder.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Mooc\CoursesCounter\Application\Find;

use CodelyTv\Mooc\CoursesCounter\Domain\CoursesCounterNotExist;
use CodelyTv\Mooc\CoursesCounter\Domain\CoursesCounterRepository;

final readonly class CoursesCounterFinder
{
	public function __construct(private CoursesCounterRepository $repository) {}

	public function __invoke(): CoursesCounterResponse
	{
		$counter = $this->repository->search();

		if ($counter === null) {
			throw new CoursesCounterNotExist();
		}

		return new CoursesCounterResponse($counter->total()->value());
	}
}
```

## File: `src/Mooc/CoursesCounter/Application/Find/CoursesCounterResponse.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Mooc\CoursesCounter\Application\Find;

use CodelyTv\Shared\Domain\Bus\Query\Response;

final readonly class CoursesCounterResponse implements Response
{
	public function __construct(private int $total) {}

	public function total(): int
	{
		return $this->total;
	}
}
```

## File: `src/Mooc/CoursesCounter/Application/Find/FindCoursesCounterQuery.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Mooc\CoursesCounter\Application\Find;

use CodelyTv\Shared\Domain\Bus\Query\Query;

final class FindCoursesCounterQuery implements Query {}
```

## File: `src/Mooc/CoursesCounter/Application/Find/FindCoursesCounterQueryHandler.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Mooc\CoursesCounter\Application\Find;

use CodelyTv\Shared\Domain\Bus\Query\QueryHandler;

final readonly class FindCoursesCounterQueryHandler implements QueryHandler
{
	public function __construct(private CoursesCounterFinder $finder) {}

	public function __invoke(FindCoursesCounterQuery $query): CoursesCounterResponse
	{
		return $this->finder->__invoke();
	}
}
```

## File: `src/Mooc/CoursesCounter/Application/Increment/CoursesCounterIncrementer.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Mooc\CoursesCounter\Application\Increment;

use CodelyTv\Mooc\CoursesCounter\Domain\CoursesCounter;
use CodelyTv\Mooc\CoursesCounter\Domain\CoursesCounterId;
use CodelyTv\Mooc\CoursesCounter\Domain\CoursesCounterRepository;
use CodelyTv\Mooc\Shared\Domain\Courses\CourseId;
use CodelyTv\Shared\Domain\Bus\Event\EventBus;
use CodelyTv\Shared\Domain\UuidGenerator;

final readonly class CoursesCounterIncrementer
{
	public function __construct(
		private CoursesCounterRepository $repository,
		private UuidGenerator $uuidGenerator,
		private EventBus $bus
	) {}

	public function __invoke(CourseId $courseId): void
	{
		$counter = $this->repository->search() ?: $this->initializeCounter();

		if (!$counter->hasIncremented($courseId)) {
			$counter->increment($courseId);

			$this->repository->save($counter);
			$this->bus->publish(...$counter->pullDomainEvents());
		}
	}

	private function initializeCounter(): CoursesCounter
	{
		return CoursesCounter::initialize(new CoursesCounterId($this->uuidGenerator->generate()));
	}
}
```

## File: `src/Mooc/CoursesCounter/Application/Increment/IncrementCoursesCounterOnCourseCreated.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Mooc\CoursesCounter\Application\Increment;

use CodelyTv\Mooc\Courses\Domain\CourseCreatedDomainEvent;
use CodelyTv\Mooc\Shared\Domain\Courses\CourseId;
use CodelyTv\Shared\Domain\Bus\Event\DomainEventSubscriber;

use function Lambdish\Phunctional\apply;

final readonly class IncrementCoursesCounterOnCourseCreated implements DomainEventSubscriber
{
	public function __construct(private CoursesCounterIncrementer $incrementer) {}

	public static function subscribedTo(): array
	{
		return [CourseCreatedDomainEvent::class];
	}

	public function __invoke(CourseCreatedDomainEvent $event): void
	{
		$courseId = new CourseId($event->aggregateId());

		apply($this->incrementer, [$courseId]);
	}
}
```

## File: `src/Mooc/CoursesCounter/Domain/CoursesCounter.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Mooc\CoursesCounter\Domain;

use CodelyTv\Mooc\Shared\Domain\Courses\CourseId;
use CodelyTv\Shared\Domain\Aggregate\AggregateRoot;

use function Lambdish\Phunctional\search;

final class CoursesCounter extends AggregateRoot
{
	private array $existingCourses;

	public function __construct(
		private readonly CoursesCounterId $id,
		private CoursesCounterTotal $total,
		CourseId ...$existingCourses
	) {
		$this->existingCourses = $existingCourses;
	}

	public static function initialize(CoursesCounterId $id): self
	{
		return new self($id, CoursesCounterTotal::initialize());
	}

	public function id(): CoursesCounterId
	{
		return $this->id;
	}

	public function total(): CoursesCounterTotal
	{
		return $this->total;
	}

	public function existingCourses(): array
	{
		return $this->existingCourses;
	}

	public function increment(CourseId $courseId): void
	{
		$this->total = $this->total->increment();
		$this->existingCourses[] = $courseId;

		$this->record(new CoursesCounterIncrementedDomainEvent($this->id()->value(), $this->total()->value()));
	}

	public function hasIncremented(CourseId $courseId): bool
	{
		$existingCourse = search($this->courseIdComparator($courseId), $this->existingCourses());

		return $existingCourse !== null;
	}

	private function courseIdComparator(CourseId $courseId): callable
	{
		return static fn (CourseId $other): bool => $courseId->equals($other);
	}
}
```

## File: `src/Mooc/CoursesCounter/Domain/CoursesCounterId.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Mooc\CoursesCounter\Domain;

use CodelyTv\Shared\Domain\ValueObject\Uuid;

final class CoursesCounterId extends Uuid {}
```

## File: `src/Mooc/CoursesCounter/Domain/CoursesCounterIncrementedDomainEvent.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Mooc\CoursesCounter\Domain;

use CodelyTv\Shared\Domain\Bus\Event\DomainEvent;

final class CoursesCounterIncrementedDomainEvent extends DomainEvent
{
	public function __construct(
		string $aggregateId,
		private readonly int $total,
		string $eventId = null,
		string $occurredOn = null
	) {
		parent::__construct($aggregateId, $eventId, $occurredOn);
	}

	public static function eventName(): string
	{
		return 'courses_counter.incremented';
	}

	public static function fromPrimitives(
		string $aggregateId,
		array $body,
		string $eventId,
		string $occurredOn
	): DomainEvent {
		return new self($aggregateId, $body['total'], $eventId, $occurredOn);
	}

	public function toPrimitives(): array
	{
		return [
			'total' => $this->total,
		];
	}
}
```

## File: `src/Mooc/CoursesCounter/Domain/CoursesCounterNotExist.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Mooc\CoursesCounter\Domain;

use RuntimeException;

final class CoursesCounterNotExist extends RuntimeException
{
	public function __construct()
	{
		parent::__construct('The courses counter not exist');
	}
}
```

## File: `src/Mooc/CoursesCounter/Domain/CoursesCounterRepository.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Mooc\CoursesCounter\Domain;

interface CoursesCounterRepository
{
	public function save(CoursesCounter $counter): void;

	public function search(): ?CoursesCounter;
}
```

## File: `src/Mooc/CoursesCounter/Domain/CoursesCounterTotal.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Mooc\CoursesCounter\Domain;

use CodelyTv\Shared\Domain\ValueObject\IntValueObject;

final class CoursesCounterTotal extends IntValueObject
{
	public static function initialize(): self
	{
		return new self(0);
	}

	public function increment(): self
	{
		return new self($this->value() + 1);
	}
}
```

## File: `src/Mooc/CoursesCounter/Infrastructure/Persistence/DoctrineCoursesCounterRepository.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Mooc\CoursesCounter\Infrastructure\Persistence;

use CodelyTv\Mooc\CoursesCounter\Domain\CoursesCounter;
use CodelyTv\Mooc\CoursesCounter\Domain\CoursesCounterRepository;
use CodelyTv\Shared\Infrastructure\Persistence\Doctrine\DoctrineRepository;

final class DoctrineCoursesCounterRepository extends DoctrineRepository implements CoursesCounterRepository
{
	public function save(CoursesCounter $counter): void
	{
		$this->persist($counter);
	}

	public function search(): ?CoursesCounter
	{
		return $this->repository(CoursesCounter::class)->findOneBy([]);
	}
}
```

## File: `src/Mooc/CoursesCounter/Infrastructure/Persistence/Doctrine/CourseCounterIdType.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Mooc\CoursesCounter\Infrastructure\Persistence\Doctrine;

use CodelyTv\Mooc\CoursesCounter\Domain\CoursesCounterId;
use CodelyTv\Shared\Infrastructure\Persistence\Doctrine\UuidType;

final class CourseCounterIdType extends UuidType
{
	protected function typeClassName(): string
	{
		return CoursesCounterId::class;
	}
}
```

## File: `src/Mooc/CoursesCounter/Infrastructure/Persistence/Doctrine/CourseIdsType.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Mooc\CoursesCounter\Infrastructure\Persistence\Doctrine;

use CodelyTv\Mooc\Shared\Domain\Courses\CourseId;
use CodelyTv\Shared\Infrastructure\Doctrine\Dbal\DoctrineCustomType;
use Doctrine\DBAL\Platforms\AbstractPlatform;
use Doctrine\DBAL\Types\JsonType;

use function Lambdish\Phunctional\map;

final class CourseIdsType extends JsonType implements DoctrineCustomType
{
	public static function customTypeName(): string
	{
		return 'course_ids';
	}

	public function getName(): string
	{
		return self::customTypeName();
	}

	public function convertToDatabaseValue($value, AbstractPlatform $platform): ?string
	{
		return parent::convertToDatabaseValue(map(fn (CourseId $id): string => $id->value(), $value), $platform);
	}

	public function convertToPHPValue($value, AbstractPlatform $platform): array
	{
		$scalars = parent::convertToPHPValue($value, $platform);

		return map(fn (string $value): CourseId => new CourseId($value), $scalars);
	}
}
```

## File: `src/Mooc/CoursesCounter/Infrastructure/Persistence/Doctrine/CoursesCounter.orm.xml`
```xml
<?xml version="1.0" encoding="UTF-8"?>
<doctrine-mapping xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                  xmlns="http://doctrine-project.org/schemas/orm/doctrine-mapping"
                  xsi:schemaLocation="http://doctrine-project.org/schemas/orm/doctrine-mapping
                          https://www.doctrine-project.org/schemas/orm/doctrine-mapping.xsd">

    <entity name="CodelyTv\Mooc\CoursesCounter\Domain\CoursesCounter" table="courses_counter">
        <id name="id" type="course_counter_id" column="id" length="36" />

        <field name="existingCourses" type="course_ids" column="existing_courses" />

        <embedded name="total"
                  class="CodelyTv\Mooc\CoursesCounter\Domain\CoursesCounterTotal"
                  use-column-prefix="false" />
    </entity>

</doctrine-mapping>
```

## File: `src/Mooc/CoursesCounter/Infrastructure/Persistence/Doctrine/CoursesCounterTotal.orm.xml`
```xml
<?xml version="1.0" encoding="UTF-8"?>
<doctrine-mapping xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                  xmlns="http://doctrine-project.org/schemas/orm/doctrine-mapping"
                  xsi:schemaLocation="http://doctrine-project.org/schemas/orm/doctrine-mapping
                          https://www.doctrine-project.org/schemas/orm/doctrine-mapping.xsd">

    <embeddable name="CodelyTv\Mooc\CoursesCounter\Domain\CoursesCounterTotal">
        <field name="value" type="integer" column="total" />
    </embeddable>

</doctrine-mapping>
```

## File: `src/Mooc/Shared/Domain/Courses/CourseId.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Mooc\Shared\Domain\Courses;

use CodelyTv\Shared\Domain\ValueObject\Uuid;

final class CourseId extends Uuid {}
```

## File: `src/Mooc/Shared/Domain/Videos/VideoUrl.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Mooc\Shared\Domain\Videos;

use CodelyTv\Shared\Domain\ValueObject\StringValueObject;
use InvalidArgumentException;

final class VideoUrl extends StringValueObject
{
	public function __construct(string $value)
	{
		$this->ensureIsValidUrl($value);

		parent::__construct($value);
	}

	private function ensureIsValidUrl(string $url): void
	{
		if (filter_var($url, FILTER_VALIDATE_URL) === false) {
			throw new InvalidArgumentException(sprintf('The url <%s> is not well formatted', $url));
		}
	}
}
```

## File: `src/Mooc/Shared/Infrastructure/Doctrine/DbalTypesSearcher.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Mooc\Shared\Infrastructure\Doctrine;

use function Lambdish\Phunctional\filter;
use function Lambdish\Phunctional\map;
use function Lambdish\Phunctional\reduce;

final class DbalTypesSearcher
{
	private const MAPPINGS_PATH = 'Infrastructure/Persistence/Doctrine';

	public static function inPath(string $path, string $contextName): array
	{
		$possibleDbalDirectories = self::possibleDbalPaths($path);
		$dbalDirectories = filter(self::isExistingDbalPath(), $possibleDbalDirectories);

		return reduce(self::dbalClassesSearcher($contextName), $dbalDirectories, []);
	}

	private static function modulesInPath(string $path): array
	{
		return filter(
			static fn (string $possibleModule): bool => !in_array($possibleModule, ['.', '..'], true),
			scandir($path)
		);
	}

	private static function possibleDbalPaths(string $path): array
	{
		return map(
			static function (mixed $_unused, string $module) use ($path) {
				$mappingsPath = self::MAPPINGS_PATH;

				return realpath("$path/$module/$mappingsPath");
			},
			array_flip(self::modulesInPath($path))
		);
	}

	private static function isExistingDbalPath(): callable
	{
		return static fn (string $path): bool => !empty($path);
	}

	private static function dbalClassesSearcher(string $contextName): callable
	{
		return static function (array $totalNamespaces, string $path) use ($contextName): array {
			$possibleFiles = scandir($path);
			$files = filter(static fn (string $file): bool => str_ends_with($file, 'Type.php'), $possibleFiles);

			$namespaces = map(
				static function (string $file) use ($path, $contextName): string {
					$fullPath = "$path/$file";
					$splittedPath = explode("/src/$contextName/", $fullPath);

					$classWithoutPrefix = str_replace(['.php', '/'], ['', '\\'], $splittedPath[1]);

					return "CodelyTv\\$contextName\\$classWithoutPrefix";
				},
				$files
			);

			return array_merge($totalNamespaces, $namespaces);
		};
	}
}
```

## File: `src/Mooc/Shared/Infrastructure/Doctrine/DoctrinePrefixesSearcher.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Mooc\Shared\Infrastructure\Doctrine;

use function Lambdish\Phunctional\filter;
use function Lambdish\Phunctional\map;
use function Lambdish\Phunctional\reindex;

final class DoctrinePrefixesSearcher
{
	private const MAPPINGS_PATH = 'Infrastructure/Persistence/Doctrine';

	public static function inPath(string $path, string $baseNamespace): array
	{
		$possibleMappingDirectories = self::possibleMappingPaths($path);
		$mappingDirectories = filter(self::isExistingMappingPath(), $possibleMappingDirectories);

		return array_flip(reindex(self::namespaceFormatter($baseNamespace), $mappingDirectories));
	}

	private static function modulesInPath(string $path): array
	{
		return filter(
			static fn (string $possibleModule): bool => !in_array($possibleModule, ['.', '..'], true),
			scandir($path)
		);
	}

	private static function possibleMappingPaths(string $path): array
	{
		return map(
			static function (mixed $_unused, string $module) use ($path) {
				$mappingsPath = self::MAPPINGS_PATH;

				return realpath("$path/$module/$mappingsPath");
			},
			array_flip(self::modulesInPath($path))
		);
	}

	private static function isExistingMappingPath(): callable
	{
		return static fn (string $path): bool => !empty($path);
	}

	private static function namespaceFormatter(string $baseNamespace): callable
	{
		return static fn (string $path, string $module): string => "$baseNamespace\\$module\Domain";
	}
}
```

## File: `src/Mooc/Shared/Infrastructure/Doctrine/MoocEntityManagerFactory.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Mooc\Shared\Infrastructure\Doctrine;

use CodelyTv\Shared\Infrastructure\Doctrine\DoctrineEntityManagerFactory;
use Doctrine\ORM\EntityManagerInterface;

final class MoocEntityManagerFactory
{
	private const SCHEMA_PATH = __DIR__ . '/../../../../../etc/databases/mooc.sql';

	public static function create(array $parameters, string $environment): EntityManagerInterface
	{
		$isDevMode = $environment !== 'prod';

		$prefixes = array_merge(
			DoctrinePrefixesSearcher::inPath(__DIR__ . '/../../../../Mooc', 'CodelyTv\Mooc'),
			DoctrinePrefixesSearcher::inPath(__DIR__ . '/../../../../Backoffice', 'CodelyTv\Backoffice')
		);

		$dbalCustomTypesClasses = DbalTypesSearcher::inPath(__DIR__ . '/../../../../Mooc', 'Mooc');

		return DoctrineEntityManagerFactory::create(
			$parameters,
			$prefixes,
			$isDevMode,
			self::SCHEMA_PATH,
			$dbalCustomTypesClasses
		);
	}
}
```

## File: `src/Mooc/Shared/Infrastructure/Symfony/DependencyInjection/mooc_services.yaml`
```yaml
services:
  # Databases
  Doctrine\ORM\EntityManager:
    factory: [ CodelyTv\Mooc\Shared\Infrastructure\Doctrine\MoocEntityManagerFactory, create ]
    arguments:
      - driver: '%env(MOOC_DATABASE_DRIVER)%'
        host: '%env(MOOC_DATABASE_HOST)%'
        port: '%env(MOOC_DATABASE_PORT)%'
        dbname: '%env(MOOC_DATABASE_NAME)%'
        user: '%env(MOOC_DATABASE_USER)%'
        password: '%env(MOOC_DATABASE_PASSWORD)%'
      - '%env(APP_ENV)%'
    tags:
      - { name: codely.database_connection }
    public: true


  # Courses
  CodelyTv\Mooc\Courses\Domain\CourseRepository: '@CodelyTv\Mooc\Courses\Infrastructure\Persistence\DoctrineCourseRepository'
```

## File: `src/Mooc/Steps/Application/Create/CreateVideoStepCommandHandler.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Mooc\Steps\Application\Create;

use CodelyTv\Shared\Domain\Bus\Command\CommandHandler;

final readonly class CreateVideoStepCommandHandler implements CommandHandler
{
	public function __construct(private VideoStepCreator $creator) {}

	public function __invoke(): void {}
}
```

## File: `src/Mooc/Steps/Application/Create/VideoStepCreator.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Mooc\Steps\Application\Create;

use CodelyTv\Mooc\Steps\Domain\StepRepository;

final readonly class VideoStepCreator
{
	public function __construct(private StepRepository $repository) {}

	public function __invoke(): void {}
}
```

## File: `src/Mooc/Steps/Domain/Step.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Mooc\Steps\Domain;

use CodelyTv\Shared\Domain\Aggregate\AggregateRoot;

abstract class Step extends AggregateRoot
{
	public function __construct(
		public readonly StepId $id,
		private readonly StepTitle $title,
		private readonly StepDuration $duration
	) {}
}
```

## File: `src/Mooc/Steps/Domain/StepDuration.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Mooc\Steps\Domain;

use CodelyTv\Shared\Domain\ValueObject\IntValueObject;

final class StepDuration extends IntValueObject {}
```

## File: `src/Mooc/Steps/Domain/StepId.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Mooc\Steps\Domain;

use CodelyTv\Shared\Domain\ValueObject\Uuid;

final class StepId extends Uuid {}
```

## File: `src/Mooc/Steps/Domain/StepRepository.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Mooc\Steps\Domain;

interface StepRepository
{
	public function save(Step $step): void;

	public function search(StepId $id): ?Step;

	public function delete(Step $step): void;
}
```

## File: `src/Mooc/Steps/Domain/StepTitle.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Mooc\Steps\Domain;

use CodelyTv\Shared\Domain\ValueObject\StringValueObject;

final class StepTitle extends StringValueObject {}
```

## File: `src/Mooc/Steps/Domain/Exercise/ExerciseStep.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Mooc\Steps\Domain\Exercise;

use CodelyTv\Mooc\Steps\Domain\Step;
use CodelyTv\Mooc\Steps\Domain\StepDuration;
use CodelyTv\Mooc\Steps\Domain\StepId;
use CodelyTv\Mooc\Steps\Domain\StepTitle;

final class ExerciseStep extends Step
{
	public function __construct(
		StepId $id,
		StepTitle $title,
		StepDuration $duration,
		private readonly ExerciseStepContent $content
	) {
		parent::__construct($id, $title, $duration);
	}
}
```

## File: `src/Mooc/Steps/Domain/Exercise/ExerciseStepContent.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Mooc\Steps\Domain\Exercise;

use CodelyTv\Shared\Domain\ValueObject\StringValueObject;

final class ExerciseStepContent extends StringValueObject {}
```

## File: `src/Mooc/Steps/Domain/Quiz/QuizStep.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Mooc\Steps\Domain\Quiz;

use CodelyTv\Mooc\Steps\Domain\Step;
use CodelyTv\Mooc\Steps\Domain\StepDuration;
use CodelyTv\Mooc\Steps\Domain\StepId;
use CodelyTv\Mooc\Steps\Domain\StepTitle;

final class QuizStep extends Step
{
	/** @var QuizStepQuestion[] */
	private array $questions;

	public function __construct(
		StepId $id,
		StepTitle $title,
		StepDuration $duration,
		QuizStepQuestion ...$questions
	) {
		parent::__construct($id, $title, $duration);

		$this->questions = $questions;
	}
}
```

## File: `src/Mooc/Steps/Domain/Quiz/QuizStepQuestion.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Mooc\Steps\Domain\Quiz;

final readonly class QuizStepQuestion
{
	public function __construct(private string $question, private array $answers) {}

	public static function fromString(string $value): self
	{
		[$question, $answers] = explode('----', $value);

		return new self($question, explode('****', $answers));
	}

	public function toString(): string
	{
		return $this->question . '----' . implode('****', $this->answers);
	}
}
```

## File: `src/Mooc/Steps/Domain/Video/VideoStep.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Mooc\Steps\Domain\Video;

use CodelyTv\Mooc\Steps\Domain\Step;
use CodelyTv\Mooc\Steps\Domain\StepDuration;
use CodelyTv\Mooc\Steps\Domain\StepId;
use CodelyTv\Mooc\Steps\Domain\StepTitle;

final class VideoStep extends Step
{
	public function __construct(
		StepId $id,
		StepTitle $title,
		StepDuration $duration,
		private readonly VideoStepUrl $url
	) {
		parent::__construct($id, $title, $duration);
	}
}
```

## File: `src/Mooc/Steps/Domain/Video/VideoStepUrl.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Mooc\Steps\Domain\Video;

use CodelyTv\Shared\Domain\ValueObject\StringValueObject;

final class VideoStepUrl extends StringValueObject {}
```

## File: `src/Mooc/Steps/Infrastructure/Persistence/MySqlStepRepository.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Mooc\Steps\Infrastructure\Persistence;

use CodelyTv\Mooc\Steps\Domain\Step;
use CodelyTv\Mooc\Steps\Domain\StepId;
use CodelyTv\Mooc\Steps\Domain\StepRepository;
use CodelyTv\Shared\Infrastructure\Persistence\Doctrine\DoctrineRepository;

final class MySqlStepRepository extends DoctrineRepository implements StepRepository
{
	public function save(Step $step): void
	{
		$this->persist($step);
	}

	public function search(StepId $id): ?Step
	{
		return $this->repository(Step::class)->find($id);
	}

	public function delete(Step $step): void
	{
		$this->remove($step);
	}
}
```

## File: `src/Mooc/Steps/Infrastructure/Persistence/Doctrine/Exercise.ExerciseStep.orm.xml`
```xml
<?xml version="1.0" encoding="UTF-8"?>
<doctrine-mapping xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                  xmlns="http://doctrine-project.org/schemas/orm/doctrine-mapping"
                  xsi:schemaLocation="http://doctrine-project.org/schemas/orm/doctrine-mapping
                          https://www.doctrine-project.org/schemas/orm/doctrine-mapping.xsd">

    <entity name="CodelyTv\Mooc\Steps\Domain\Exercise\ExerciseStep" table="steps_exercise">
        <embedded name="content" class="CodelyTv\Mooc\Steps\Domain\Exercise\ExerciseStepContent" use-column-prefix="false" />
    </entity>
</doctrine-mapping>
```

## File: `src/Mooc/Steps/Infrastructure/Persistence/Doctrine/Exercise.ExerciseStepContent.orm.xml`
```xml
<?xml version="1.0" encoding="UTF-8"?>
<doctrine-mapping xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                  xmlns="http://doctrine-project.org/schemas/orm/doctrine-mapping"
                  xsi:schemaLocation="http://doctrine-project.org/schemas/orm/doctrine-mapping
                          https://www.doctrine-project.org/schemas/orm/doctrine-mapping.xsd">

    <embeddable name="CodelyTv\Mooc\Steps\Domain\Exercise\ExerciseStepContent">
        <field name="value" type="string" column="content" />
    </embeddable>
</doctrine-mapping>
```

## File: `src/Mooc/Steps/Infrastructure/Persistence/Doctrine/Quiz.QuizStep.orm.xml`
```xml
<?xml version="1.0" encoding="UTF-8"?>
<doctrine-mapping xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                  xmlns="http://doctrine-project.org/schemas/orm/doctrine-mapping"
                  xsi:schemaLocation="http://doctrine-project.org/schemas/orm/doctrine-mapping
                          https://www.doctrine-project.org/schemas/orm/doctrine-mapping.xsd">

    <entity name="CodelyTv\Mooc\Steps\Domain\Quiz\QuizStep" table="steps_quiz">
        <field name="questions" type="quiz_step_questions" column="questions" />
    </entity>
</doctrine-mapping>
```

## File: `src/Mooc/Steps/Infrastructure/Persistence/Doctrine/QuizStepQuestionsType.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Mooc\Steps\Infrastructure\Persistence\Doctrine;

use CodelyTv\Mooc\Steps\Domain\Quiz\QuizStepQuestion;
use CodelyTv\Shared\Infrastructure\Doctrine\Dbal\DoctrineCustomType;
use Doctrine\DBAL\Platforms\AbstractPlatform;
use Doctrine\DBAL\Types\JsonType;

use function Lambdish\Phunctional\map;

final class QuizStepQuestionsType extends JsonType implements DoctrineCustomType
{
	public static function customTypeName(): string
	{
		return 'quiz_step_questions';
	}

	public function getName(): string
	{
		return self::customTypeName();
	}

	public function convertToDatabaseValue($value, AbstractPlatform $platform): ?string
	{
		return parent::convertToDatabaseValue(
			map(fn (QuizStepQuestion $question): string => $question->toString(), $value),
			$platform
		);
	}

	public function convertToPHPValue($value, AbstractPlatform $platform): array
	{
		$scalars = parent::convertToPHPValue($value, $platform);

		return map(fn (string $value): QuizStepQuestion => QuizStepQuestion::fromString($value), $scalars);
	}
}
```

## File: `src/Mooc/Steps/Infrastructure/Persistence/Doctrine/Step.orm.xml`
```xml
<?xml version="1.0" encoding="UTF-8"?>
<doctrine-mapping xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                  xmlns="http://doctrine-project.org/schemas/orm/doctrine-mapping"
                  xsi:schemaLocation="http://doctrine-project.org/schemas/orm/doctrine-mapping
                          https://www.doctrine-project.org/schemas/orm/doctrine-mapping.xsd">

    <entity name="CodelyTv\Mooc\Steps\Domain\Step" table="steps" inheritance-type="JOINED">
        <discriminator-column name="type" type="string" />
        <discriminator-map>
            <discriminator-mapping value="exercise" class="CodelyTv\Mooc\Steps\Domain\Exercise\ExerciseStep" />
            <discriminator-mapping value="quiz" class="CodelyTv\Mooc\Steps\Domain\Quiz\QuizStep" />
            <discriminator-mapping value="video" class="CodelyTv\Mooc\Steps\Domain\Video\VideoStep" />
        </discriminator-map>

        <id name="id" type="step_id" column="id" length="36" />

        <embedded name="title" class="CodelyTv\Mooc\Steps\Domain\StepTitle" use-column-prefix="false" />
        <embedded name="duration" class="CodelyTv\Mooc\Steps\Domain\StepDuration" use-column-prefix="false" />
    </entity>
</doctrine-mapping>
```

## File: `src/Mooc/Steps/Infrastructure/Persistence/Doctrine/StepDuration.orm.xml`
```xml
<?xml version="1.0" encoding="UTF-8"?>
<doctrine-mapping xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                  xmlns="http://doctrine-project.org/schemas/orm/doctrine-mapping"
                  xsi:schemaLocation="http://doctrine-project.org/schemas/orm/doctrine-mapping
                          https://www.doctrine-project.org/schemas/orm/doctrine-mapping.xsd">

    <embeddable name="CodelyTv\Mooc\Steps\Domain\StepDuration">
        <field name="value" type="integer" column="duration" />
    </embeddable>
</doctrine-mapping>
```

## File: `src/Mooc/Steps/Infrastructure/Persistence/Doctrine/StepIdType.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Mooc\Steps\Infrastructure\Persistence\Doctrine;

use CodelyTv\Mooc\Steps\Domain\StepId;
use CodelyTv\Shared\Infrastructure\Persistence\Doctrine\UuidType;

final class StepIdType extends UuidType
{
	protected function typeClassName(): string
	{
		return StepId::class;
	}
}
```

## File: `src/Mooc/Steps/Infrastructure/Persistence/Doctrine/StepTitle.orm.xml`
```xml
<?xml version="1.0" encoding="UTF-8"?>
<doctrine-mapping xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                  xmlns="http://doctrine-project.org/schemas/orm/doctrine-mapping"
                  xsi:schemaLocation="http://doctrine-project.org/schemas/orm/doctrine-mapping
                          https://www.doctrine-project.org/schemas/orm/doctrine-mapping.xsd">

    <embeddable name="CodelyTv\Mooc\Steps\Domain\StepTitle">
        <field name="value" type="string" column="title" />
    </embeddable>
</doctrine-mapping>
```

## File: `src/Mooc/Steps/Infrastructure/Persistence/Doctrine/Video.VideoStep.orm.xml`
```xml
<?xml version="1.0" encoding="UTF-8"?>
<doctrine-mapping xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                  xmlns="http://doctrine-project.org/schemas/orm/doctrine-mapping"
                  xsi:schemaLocation="http://doctrine-project.org/schemas/orm/doctrine-mapping
                          https://www.doctrine-project.org/schemas/orm/doctrine-mapping.xsd">

    <entity name="CodelyTv\Mooc\Steps\Domain\Video\VideoStep" table="steps_video">
        <embedded name="url" class="CodelyTv\Mooc\Steps\Domain\Video\VideoStepUrl" use-column-prefix="false" />
    </entity>
</doctrine-mapping>
```

## File: `src/Mooc/Steps/Infrastructure/Persistence/Doctrine/Video.VideoStepUrl.orm.xml`
```xml
<?xml version="1.0" encoding="UTF-8"?>
<doctrine-mapping xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                  xmlns="http://doctrine-project.org/schemas/orm/doctrine-mapping"
                  xsi:schemaLocation="http://doctrine-project.org/schemas/orm/doctrine-mapping
                          https://www.doctrine-project.org/schemas/orm/doctrine-mapping.xsd">

    <embeddable name="CodelyTv\Mooc\Steps\Domain\Video\VideoStepUrl">
        <field name="value" type="string" column="url" />
    </embeddable>
</doctrine-mapping>
```

## File: `src/Mooc/Videos/Application/Create/CreateVideoCommand.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Mooc\Videos\Application\Create;

use CodelyTv\Shared\Domain\Bus\Command\Command;

final readonly class CreateVideoCommand implements Command
{
	public function __construct(
		private string $id,
		private string $type,
		private string $title,
		private string $url,
		private string $courseId
	) {}

	public function id(): string
	{
		return $this->id;
	}

	public function type(): string
	{
		return $this->type;
	}

	public function title(): string
	{
		return $this->title;
	}

	public function url(): string
	{
		return $this->url;
	}

	public function courseId(): string
	{
		return $this->courseId;
	}
}
```

## File: `src/Mooc/Videos/Application/Create/CreateVideoCommandHandler.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Mooc\Videos\Application\Create;

use CodelyTv\Mooc\Shared\Domain\Courses\CourseId;
use CodelyTv\Mooc\Shared\Domain\Videos\VideoUrl;
use CodelyTv\Mooc\Videos\Domain\VideoId;
use CodelyTv\Mooc\Videos\Domain\VideoTitle;
use CodelyTv\Mooc\Videos\Domain\VideoType;
use CodelyTv\Shared\Domain\Bus\Command\CommandHandler;

final readonly class CreateVideoCommandHandler implements CommandHandler
{
	public function __construct(private VideoCreator $creator) {}

	public function __invoke(CreateVideoCommand $command): void
	{
		$id = new VideoId($command->id());
		$type = VideoType::from($command->type());
		$title = new VideoTitle($command->title());
		$url = new VideoUrl($command->url());
		$courseId = new CourseId($command->courseId());

		$this->creator->create($id, $type, $title, $url, $courseId);
	}
}
```

## File: `src/Mooc/Videos/Application/Create/VideoCreator.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Mooc\Videos\Application\Create;

use CodelyTv\Mooc\Shared\Domain\Courses\CourseId;
use CodelyTv\Mooc\Shared\Domain\Videos\VideoUrl;
use CodelyTv\Mooc\Videos\Domain\Video;
use CodelyTv\Mooc\Videos\Domain\VideoId;
use CodelyTv\Mooc\Videos\Domain\VideoRepository;
use CodelyTv\Mooc\Videos\Domain\VideoTitle;
use CodelyTv\Mooc\Videos\Domain\VideoType;
use CodelyTv\Shared\Domain\Bus\Event\EventBus;

final readonly class VideoCreator
{
	public function __construct(private VideoRepository $repository, private EventBus $bus) {}

	public function create(VideoId $id, VideoType $type, VideoTitle $title, VideoUrl $url, CourseId $courseId): void
	{
		$video = Video::create($id, $type, $title, $url, $courseId);

		$this->repository->save($video);

		$this->bus->publish(...$video->pullDomainEvents());
	}
}
```

## File: `src/Mooc/Videos/Application/Find/FindVideoQuery.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Mooc\Videos\Application\Find;

use CodelyTv\Shared\Domain\Bus\Query\Query;

final readonly class FindVideoQuery implements Query
{
	public function __construct(private string $id) {}

	public function id(): string
	{
		return $this->id;
	}
}
```

## File: `src/Mooc/Videos/Application/Find/FindVideoQueryHandler.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Mooc\Videos\Application\Find;

use CodelyTv\Mooc\Videos\Domain\VideoId;
use CodelyTv\Shared\Domain\Bus\Query\QueryHandler;

use function Lambdish\Phunctional\apply;

final readonly class FindVideoQueryHandler implements QueryHandler
{
	private VideoResponseConverter $responseConverter;

	public function __construct(private VideoFinder $finder)
	{
		$this->responseConverter = new VideoResponseConverter();
	}

	public function __invoke(FindVideoQuery $query): VideoResponse
	{
		$id = new VideoId($query->id());

		$video = apply($this->finder, [$id]);

		return apply($this->responseConverter, [$video]);
	}
}
```

## File: `src/Mooc/Videos/Application/Find/VideoFinder.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Mooc\Videos\Application\Find;

use CodelyTv\Mooc\Videos\Domain\Video;
use CodelyTv\Mooc\Videos\Domain\VideoFinder as DomainVideoFinder;
use CodelyTv\Mooc\Videos\Domain\VideoId;
use CodelyTv\Mooc\Videos\Domain\VideoRepository;

final class VideoFinder
{
	private readonly DomainVideoFinder $finder;

	public function __construct(VideoRepository $repository)
	{
		$this->finder = new DomainVideoFinder($repository);
	}

	public function __invoke(VideoId $id): Video
	{
		return $this->finder->__invoke($id);
	}
}
```

## File: `src/Mooc/Videos/Application/Find/VideoResponse.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Mooc\Videos\Application\Find;

use CodelyTv\Shared\Domain\Bus\Query\Response;

final readonly class VideoResponse implements Response
{
	public function __construct(
		private string $id,
		private string $type,
		private string $title,
		private string $url,
		private string $courseId
	) {}
}
```

## File: `src/Mooc/Videos/Application/Find/VideoResponseConverter.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Mooc\Videos\Application\Find;

use CodelyTv\Mooc\Videos\Domain\Video;

final class VideoResponseConverter
{
	public function __invoke(Video $video): VideoResponse
	{
		return new VideoResponse(
			$video->id()->value(),
			$video->type()->value,
			$video->title()->value(),
			$video->url()->value(),
			$video->courseId()->value()
		);
	}
}
```

## File: `src/Mooc/Videos/Application/Trim/TrimVideoCommand.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Mooc\Videos\Application\Trim;

use CodelyTv\Shared\Domain\Bus\Command\Command;

final readonly class TrimVideoCommand implements Command
{
	public function __construct(private string $videoId, private int $keepFromSecond, private int $keepToSecond) {}

	public function videoId(): string
	{
		return $this->videoId;
	}

	public function keepFromSecond(): int
	{
		return $this->keepFromSecond;
	}

	public function keepToSecond(): int
	{
		return $this->keepToSecond;
	}
}
```

## File: `src/Mooc/Videos/Application/Trim/TrimVideoCommandHandler.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Mooc\Videos\Application\Trim;

use CodelyTv\Mooc\Videos\Domain\VideoId;
use CodelyTv\Shared\Domain\SecondsInterval;

final readonly class TrimVideoCommandHandler
{
	public function __construct(private VideoTrimmer $trimmer) {}

	public function __invoke(TrimVideoCommand $command): void
	{
		$id = new VideoId($command->videoId());
		$interval = SecondsInterval::fromValues($command->keepFromSecond(), $command->keepToSecond());

		$this->trimmer->trim($id, $interval);
	}
}
```

## File: `src/Mooc/Videos/Application/Trim/VideoTrimmer.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Mooc\Videos\Application\Trim;

use CodelyTv\Mooc\Videos\Domain\VideoId;
use CodelyTv\Shared\Domain\SecondsInterval;

final class VideoTrimmer
{
	public function trim(VideoId $id, SecondsInterval $interval): void {}
}
```

## File: `src/Mooc/Videos/Application/Update/VideoTitleUpdater.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Mooc\Videos\Application\Update;

use CodelyTv\Mooc\Videos\Domain\VideoFinder;
use CodelyTv\Mooc\Videos\Domain\VideoId;
use CodelyTv\Mooc\Videos\Domain\VideoRepository;
use CodelyTv\Mooc\Videos\Domain\VideoTitle;

final readonly class VideoTitleUpdater
{
	private VideoFinder $finder;

	public function __construct(private VideoRepository $repository)
	{
		$this->finder = new VideoFinder($repository);
	}

	public function __invoke(VideoId $id, VideoTitle $newTitle): void
	{
		$video = $this->finder->__invoke($id);

		$video->updateTitle($newTitle);

		$this->repository->save($video);
	}
}
```

## File: `src/Mooc/Videos/Domain/Video.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Mooc\Videos\Domain;

use CodelyTv\Mooc\Shared\Domain\Courses\CourseId;
use CodelyTv\Mooc\Shared\Domain\Videos\VideoUrl;
use CodelyTv\Shared\Domain\Aggregate\AggregateRoot;

final class Video extends AggregateRoot
{
	public function __construct(
		private readonly VideoId $id,
		private readonly VideoType $type,
		private VideoTitle $title,
		private readonly VideoUrl $url,
		private readonly CourseId $courseId
	) {}

	public static function create(
		VideoId $id,
		VideoType $type,
		VideoTitle $title,
		VideoUrl $url,
		CourseId $courseId
	): self {
		$video = new self($id, $type, $title, $url, $courseId);

		$video->record(
			new VideoCreatedDomainEvent($id->value(), $type->value, $title->value(), $url->value(), $courseId->value())
		);

		return $video;
	}

	public function updateTitle(VideoTitle $newTitle): void
	{
		$this->title = $newTitle;
	}

	public function id(): VideoId
	{
		return $this->id;
	}

	public function type(): VideoType
	{
		return $this->type;
	}

	public function title(): VideoTitle
	{
		return $this->title;
	}

	public function url(): VideoUrl
	{
		return $this->url;
	}

	public function courseId(): CourseId
	{
		return $this->courseId;
	}
}
```

## File: `src/Mooc/Videos/Domain/VideoCreatedDomainEvent.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Mooc\Videos\Domain;

use CodelyTv\Shared\Domain\Bus\Event\DomainEvent;

final class VideoCreatedDomainEvent extends DomainEvent
{
	public function __construct(
		string $id,
		private readonly string $type,
		private readonly string $title,
		private readonly string $url,
		private readonly string $courseId,
		string $eventId = null,
		string $occurredOn = null
	) {
		parent::__construct($id, $eventId, $occurredOn);
	}

	public static function eventName(): string
	{
		return 'video.created';
	}

	public static function fromPrimitives(
		string $aggregateId,
		array $body,
		string $eventId,
		string $occurredOn
	): self {
		return new self(
			$aggregateId,
			$body['type'],
			$body['title'],
			$body['url'],
			$body['course_id'],
			$eventId,
			$occurredOn
		);
	}

	public function toPrimitives(): array
	{
		return [
			'type' => $this->type,
			'title' => $this->title,
			'url' => $this->url,
			'course_id' => $this->courseId,
		];
	}
}
```

## File: `src/Mooc/Videos/Domain/VideoFinder.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Mooc\Videos\Domain;

final readonly class VideoFinder
{
	public function __construct(private VideoRepository $repository) {}

	public function __invoke(VideoId $id): Video
	{
		$video = $this->repository->search($id);

		if ($video === null) {
			throw new VideoNotFound($id);
		}

		return $video;
	}
}
```

## File: `src/Mooc/Videos/Domain/VideoId.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Mooc\Videos\Domain;

use CodelyTv\Shared\Domain\ValueObject\Uuid;

final class VideoId extends Uuid {}
```

## File: `src/Mooc/Videos/Domain/VideoNotFound.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Mooc\Videos\Domain;

use CodelyTv\Shared\Domain\DomainError;

final class VideoNotFound extends DomainError
{
	public function __construct(private readonly VideoId $id)
	{
		parent::__construct();
	}

	public function errorCode(): string
	{
		return 'video_not_found';
	}

	protected function errorMessage(): string
	{
		return sprintf('The video <%s> has not been found', $this->id->value());
	}
}
```

## File: `src/Mooc/Videos/Domain/VideoRepository.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Mooc\Videos\Domain;

use CodelyTv\Shared\Domain\Criteria\Criteria;

interface VideoRepository
{
	public function save(Video $video): void;

	public function search(VideoId $id): ?Video;

	public function searchByCriteria(Criteria $criteria): Videos;
}
```

## File: `src/Mooc/Videos/Domain/VideoTitle.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Mooc\Videos\Domain;

use CodelyTv\Shared\Domain\ValueObject\StringValueObject;

final class VideoTitle extends StringValueObject {}
```

## File: `src/Mooc/Videos/Domain/VideoType.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Mooc\Videos\Domain;

enum VideoType: string
{
	case SCREENCAST = 'screencast';
	case INTERVIEW = 'interview';
}
```

## File: `src/Mooc/Videos/Domain/Videos.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Mooc\Videos\Domain;

use CodelyTv\Shared\Domain\Collection;

final class Videos extends Collection
{
	protected function type(): string
	{
		return Video::class;
	}
}
```

## File: `src/Mooc/Videos/Infrastructure/Persistence/VideoRepositoryMySql.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Mooc\Videos\Infrastructure\Persistence;

use CodelyTv\Mooc\Videos\Domain\Video;
use CodelyTv\Mooc\Videos\Domain\VideoId;
use CodelyTv\Mooc\Videos\Domain\VideoRepository;
use CodelyTv\Mooc\Videos\Domain\Videos;
use CodelyTv\Shared\Domain\Criteria\Criteria;
use CodelyTv\Shared\Infrastructure\Persistence\Doctrine\DoctrineCriteriaConverter;
use CodelyTv\Shared\Infrastructure\Persistence\Doctrine\DoctrineRepository;

final class VideoRepositoryMySql extends DoctrineRepository implements VideoRepository
{
	private static array $criteriaToDoctrineFields = [
		'id' => 'id',
		'type' => 'type',
		'title' => 'title',
		'url' => 'url',
		'course_id' => 'courseId',
	];

	public function save(Video $video): void
	{
		$this->persist($video);
	}

	public function search(VideoId $id): ?Video
	{
		return $this->repository(Video::class)->find($id);
	}

	public function searchByCriteria(Criteria $criteria): Videos
	{
		$doctrineCriteria = DoctrineCriteriaConverter::convert($criteria, self::$criteriaToDoctrineFields);
		$videos = $this->repository(Video::class)->matching($doctrineCriteria)->toArray();

		return new Videos($videos);
	}
}
```

## File: `src/Mooc/Videos/Infrastructure/Persistence/Doctrine/Video.orm.xml`
```xml
<?xml version="1.0" encoding="UTF-8"?>
<doctrine-mapping xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                  xmlns="http://doctrine-project.org/schemas/orm/doctrine-mapping"
                  xsi:schemaLocation="http://doctrine-project.org/schemas/orm/doctrine-mapping
                          https://www.doctrine-project.org/schemas/orm/doctrine-mapping.xsd">

    <entity name="CodelyTv\Mooc\Videos\Domain\Video" table="videos">
        <id name="id" type="video_id" column="id" length="36" />

        <field name="courseId" column="course_id" type="course_id" />

        <embedded name="type" class="CodelyTv\Mooc\Videos\Domain\VideoType" use-column-prefix="false" />
        <embedded name="title" class="CodelyTv\Mooc\Videos\Domain\VideoTitle" use-column-prefix="false" />
        <embedded name="url" class="CodelyTv\Mooc\Shared\Domain\Videos\VideoUrl" use-column-prefix="false" />
    </entity>

</doctrine-mapping>
```

## File: `src/Mooc/Videos/Infrastructure/Persistence/Doctrine/VideoIdType.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Mooc\Videos\Infrastructure\Persistence\Doctrine;

use CodelyTv\Mooc\Videos\Domain\VideoId;
use CodelyTv\Shared\Infrastructure\Persistence\Doctrine\UuidType;

final class VideoIdType extends UuidType
{
	protected function typeClassName(): string
	{
		return VideoId::class;
	}
}
```

## File: `src/Mooc/Videos/Infrastructure/Persistence/Doctrine/VideoTitle.orm.xml`
```xml
<?xml version="1.0" encoding="UTF-8"?>
<doctrine-mapping xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                  xmlns="http://doctrine-project.org/schemas/orm/doctrine-mapping"
                  xsi:schemaLocation="http://doctrine-project.org/schemas/orm/doctrine-mapping
                          https://www.doctrine-project.org/schemas/orm/doctrine-mapping.xsd">

    <embeddable name="CodelyTv\Mooc\Videos\Domain\VideoTitle">
        <field name="value" type="string" column="title" />
    </embeddable>

</doctrine-mapping>
```

## File: `src/Mooc/Videos/Infrastructure/Persistence/Doctrine/VideoType.orm.xml`
```xml
<?xml version="1.0" encoding="UTF-8"?>
<doctrine-mapping xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                  xmlns="http://doctrine-project.org/schemas/orm/doctrine-mapping"
                  xsi:schemaLocation="http://doctrine-project.org/schemas/orm/doctrine-mapping
                          https://www.doctrine-project.org/schemas/orm/doctrine-mapping.xsd">

    <embeddable name="CodelyTv\Mooc\Videos\Domain\VideoType">
        <field name="value" type="string" column="type" />
    </embeddable>

</doctrine-mapping>
```

## File: `src/Shared/Domain/Assert.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Shared\Domain;

use InvalidArgumentException;

final class Assert
{
	public static function arrayOf(string $class, array $items): void
	{
		foreach ($items as $item) {
			self::instanceOf($class, $item);
		}
	}

	public static function instanceOf(string $class, mixed $item): void
	{
		if (!$item instanceof $class) {
			throw new InvalidArgumentException(sprintf('The object <%s> is not an instance of <%s>', $class, $item::class));
		}
	}
}
```

## File: `src/Shared/Domain/Collection.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Shared\Domain;

use ArrayIterator;
use Countable;
use IteratorAggregate;
use Traversable;

/** @template-implements IteratorAggregate<mixed>*/
abstract class Collection implements Countable, IteratorAggregate
{
	public function __construct(private readonly array $items)
	{
		Assert::arrayOf($this->type(), $items);
	}

	abstract protected function type(): string;

	final public function getIterator(): Traversable
	{
		return new ArrayIterator($this->items());
	}

	final public function count(): int
	{
		return count($this->items());
	}

	protected function items(): array
	{
		return $this->items;
	}
}
```

## File: `src/Shared/Domain/DomainError.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Shared\Domain;

use DomainException;

abstract class DomainError extends DomainException
{
	public function __construct()
	{
		parent::__construct($this->errorMessage());
	}

	abstract public function errorCode(): string;

	abstract protected function errorMessage(): string;
}
```

## File: `src/Shared/Domain/Logger.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Shared\Domain;

interface Logger
{
	public function info(string $message, array $context = []): void;

	public function warning(string $message, array $context = []): void;

	public function critical(string $message, array $context = []): void;
}
```

## File: `src/Shared/Domain/Monitoring.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Shared\Domain;

interface Monitoring
{
	public function incrementCounter(int $times): void;

	public function incrementGauge(int $times): void;

	public function decrementGauge(int $times): void;

	public function setGauge(int $value): void;

	public function observeHistogram(int $value, array $labels = []): void;
}
```

## File: `src/Shared/Domain/RandomNumberGenerator.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Shared\Domain;

interface RandomNumberGenerator
{
	public function generate(): int;
}
```

## File: `src/Shared/Domain/Second.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Shared\Domain;

use CodelyTv\Shared\Domain\ValueObject\IntValueObject;

final class Second extends IntValueObject {}
```

## File: `src/Shared/Domain/SecondsInterval.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Shared\Domain;

use DomainException;

final readonly class SecondsInterval
{
	public function __construct(private Second $from, private Second $to)
	{
		$this->ensureIntervalEndsAfterStart($from, $to);
	}

	public static function fromValues(int $from, int $to): self
	{
		return new self(new Second($from), new Second($to));
	}

	private function ensureIntervalEndsAfterStart(Second $from, Second $to): void
	{
		if ($from->isBiggerThan($to)) {
			throw new DomainException('To is bigger than from');
		}
	}
}
```

## File: `src/Shared/Domain/Utils.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Shared\Domain;

use DateTimeImmutable;
use DateTimeInterface;
use function Lambdish\Phunctional\filter;

final class Utils
{
	public static function dateToString(DateTimeInterface $date): string
	{
		return $date->format(DateTimeInterface::ATOM);
	}

	public static function stringToDate(string $date): DateTimeImmutable
	{
		return new DateTimeImmutable($date);
	}

	public static function jsonEncode(array $values): string
	{
		return json_encode($values, JSON_THROW_ON_ERROR);
	}

	public static function jsonDecode(string $json): array
	{
		return json_decode($json, true, flags: JSON_THROW_ON_ERROR);
	}

	public static function toSnakeCase(string $text): string
	{
		return ctype_lower($text) ? $text : strtolower((string) preg_replace('/([^A-Z\s])([A-Z])/', '$1_$2', $text));
	}

	public static function toCamelCase(string $text): string
	{
		return lcfirst(str_replace('_', '', ucwords($text, '_')));
	}

	public static function dot(array $array, string $prepend = ''): array
	{
		$results = [];
		foreach ($array as $key => $value) {
			if (is_array($value) && !empty($value)) {
				$results = array_merge($results, self::dot($value, $prepend . $key . '.'));
			} else {
				$results[$prepend . $key] = $value;
			}
		}

		return $results;
	}

	public static function filesIn(string $path, string $fileType): array
	{
		return filter(
			static fn (string $possibleModule): false | string => strstr($possibleModule, $fileType),
			scandir($path)
		);
	}

	public static function iterableToArray(iterable $iterable): array
	{
		if (is_array($iterable)) {
			return $iterable;
		}

		return iterator_to_array($iterable);
	}
}
```

## File: `src/Shared/Domain/UuidGenerator.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Shared\Domain;

interface UuidGenerator
{
	public function generate(): string;
}
```

## File: `src/Shared/Domain/Aggregate/AggregateRoot.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Shared\Domain\Aggregate;

use CodelyTv\Shared\Domain\Bus\Event\DomainEvent;

abstract class AggregateRoot
{
	private array $domainEvents = [];

	final public function pullDomainEvents(): array
	{
		$domainEvents = $this->domainEvents;
		$this->domainEvents = [];

		return $domainEvents;
	}

	final protected function record(DomainEvent $domainEvent): void
	{
		$this->domainEvents[] = $domainEvent;
	}
}
```

## File: `src/Shared/Domain/Bus/Command/Command.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Shared\Domain\Bus\Command;

interface Command {}
```

## File: `src/Shared/Domain/Bus/Command/CommandBus.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Shared\Domain\Bus\Command;

interface CommandBus
{
	public function dispatch(Command $command): void;
}
```

## File: `src/Shared/Domain/Bus/Command/CommandHandler.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Shared\Domain\Bus\Command;

interface CommandHandler {}
```

## File: `src/Shared/Domain/Bus/Event/DomainEvent.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Shared\Domain\Bus\Event;

use CodelyTv\Shared\Domain\Utils;
use CodelyTv\Shared\Domain\ValueObject\SimpleUuid;
use DateTimeImmutable;

abstract class DomainEvent
{
	private readonly string $eventId;
	private readonly string $occurredOn;

	public function __construct(private readonly string $aggregateId, string $eventId = null, string $occurredOn = null)
	{
		$this->eventId = $eventId ?: SimpleUuid::random()->value();
		$this->occurredOn = $occurredOn ?: Utils::dateToString(new DateTimeImmutable());
	}

	abstract public static function fromPrimitives(
		string $aggregateId,
		array $body,
		string $eventId,
		string $occurredOn
	): self;

	abstract public static function eventName(): string;

	abstract public function toPrimitives(): array;

	final public function aggregateId(): string
	{
		return $this->aggregateId;
	}

	final public function eventId(): string
	{
		return $this->eventId;
	}

	final public function occurredOn(): string
	{
		return $this->occurredOn;
	}
}
```

## File: `src/Shared/Domain/Bus/Event/DomainEventSubscriber.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Shared\Domain\Bus\Event;

interface DomainEventSubscriber
{
	public static function subscribedTo(): array;
}
```

## File: `src/Shared/Domain/Bus/Event/EventBus.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Shared\Domain\Bus\Event;

interface EventBus
{
	public function publish(DomainEvent ...$events): void;
}
```

## File: `src/Shared/Domain/Bus/Query/Query.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Shared\Domain\Bus\Query;

interface Query {}
```

## File: `src/Shared/Domain/Bus/Query/QueryBus.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Shared\Domain\Bus\Query;

interface QueryBus
{
	public function ask(Query $query): ?Response;
}
```

## File: `src/Shared/Domain/Bus/Query/QueryHandler.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Shared\Domain\Bus\Query;

interface QueryHandler {}
```

## File: `src/Shared/Domain/Bus/Query/Response.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Shared\Domain\Bus\Query;

interface Response {}
```

## File: `src/Shared/Domain/Criteria/Criteria.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Shared\Domain\Criteria;

final readonly class Criteria
{
	public function __construct(
		private Filters $filters,
		private Order $order,
		private ?int $offset,
		private ?int $limit
	) {}

	public function hasFilters(): bool
	{
		return $this->filters->count() > 0;
	}

	public function hasOrder(): bool
	{
		return !$this->order->isNone();
	}

	public function plainFilters(): array
	{
		return $this->filters->filters();
	}

	public function filters(): Filters
	{
		return $this->filters;
	}

	public function order(): Order
	{
		return $this->order;
	}

	public function offset(): ?int
	{
		return $this->offset;
	}

	public function limit(): ?int
	{
		return $this->limit;
	}

	public function serialize(): string
	{
		return sprintf(
			'%s~~%s~~%s~~%s',
			$this->filters->serialize(),
			$this->order->serialize(),
			$this->offset ?? 'none',
			$this->limit ?? 'none'
		);
	}
}
```

## File: `src/Shared/Domain/Criteria/Filter.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Shared\Domain\Criteria;

final readonly class Filter
{
	public function __construct(
		private FilterField $field,
		private FilterOperator $operator,
		private FilterValue $value
	) {}

	public static function fromValues(array $values): self
	{
		return new self(
			new FilterField($values['field']),
			FilterOperator::from($values['operator']),
			new FilterValue($values['value'])
		);
	}

	public function field(): FilterField
	{
		return $this->field;
	}

	public function operator(): FilterOperator
	{
		return $this->operator;
	}

	public function value(): FilterValue
	{
		return $this->value;
	}

	public function serialize(): string
	{
		return sprintf('%s.%s.%s', $this->field->value(), $this->operator->value, $this->value->value());
	}
}
```

## File: `src/Shared/Domain/Criteria/FilterField.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Shared\Domain\Criteria;

use CodelyTv\Shared\Domain\ValueObject\StringValueObject;

final class FilterField extends StringValueObject {}
```

## File: `src/Shared/Domain/Criteria/FilterOperator.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Shared\Domain\Criteria;

enum FilterOperator: string
{
	case EQUAL = '=';
	case NOT_EQUAL = '!=';
	case GT = '>';
	case LT = '<';
	case CONTAINS = 'CONTAINS';
	case NOT_CONTAINS = 'NOT_CONTAINS';

	public function isContaining(): bool
	{
		return in_array($this->value, [self::CONTAINS->value, self::NOT_CONTAINS->value], true);
	}
}
```

## File: `src/Shared/Domain/Criteria/FilterValue.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Shared\Domain\Criteria;

use CodelyTv\Shared\Domain\ValueObject\StringValueObject;

final class FilterValue extends StringValueObject {}
```

## File: `src/Shared/Domain/Criteria/Filters.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Shared\Domain\Criteria;

use CodelyTv\Shared\Domain\Collection;

use function Lambdish\Phunctional\reduce;

final class Filters extends Collection
{
	public static function fromValues(array $values): self
	{
		return new self(array_map(self::filterBuilder(), $values));
	}

	private static function filterBuilder(): callable
	{
		return fn (array $values): Filter => Filter::fromValues($values);
	}

	public function add(Filter $filter): self
	{
		return new self(array_merge($this->items(), [$filter]));
	}

	public function filters(): array
	{
		return $this->items();
	}

	public function serialize(): string
	{
		return reduce(
			static fn (string $accumulate, Filter $filter): string => sprintf('%s^%s', $accumulate, $filter->serialize()),
			$this->items(),
			''
		);
	}

	protected function type(): string
	{
		return Filter::class;
	}
}
```

## File: `src/Shared/Domain/Criteria/Order.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Shared\Domain\Criteria;

final readonly class Order
{
	public function __construct(private OrderBy $orderBy, private OrderType $orderType) {}

	public static function createDesc(OrderBy $orderBy): self
	{
		return new self($orderBy, OrderType::DESC);
	}

	public static function fromValues(?string $orderBy, ?string $order): self
	{
		return ($orderBy === null || $order === null) ? self::none() : new self(
			new OrderBy($orderBy),
			OrderType::from($order)
		);
	}

	public static function none(): self
	{
		return new self(new OrderBy(''), OrderType::NONE);
	}

	public function orderBy(): OrderBy
	{
		return $this->orderBy;
	}

	public function orderType(): OrderType
	{
		return $this->orderType;
	}

	public function isNone(): bool
	{
		return $this->orderType()->isNone();
	}

	public function serialize(): string
	{
		return sprintf('%s.%s', $this->orderBy->value(), $this->orderType->value);
	}
}
```

## File: `src/Shared/Domain/Criteria/OrderBy.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Shared\Domain\Criteria;

use CodelyTv\Shared\Domain\ValueObject\StringValueObject;

final class OrderBy extends StringValueObject {}
```

## File: `src/Shared/Domain/Criteria/OrderType.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Shared\Domain\Criteria;

enum OrderType: string
{
	case ASC = 'asc';
	case DESC = 'desc';
	case NONE = 'none';

	public function isNone(): bool
	{
		return $this->value === self::NONE->value;
	}
}
```

## File: `src/Shared/Domain/ValueObject/IntValueObject.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Shared\Domain\ValueObject;

abstract class IntValueObject
{
	public function __construct(protected int $value) {}

	final public function value(): int
	{
		return $this->value;
	}

	final public function isBiggerThan(self $other): bool
	{
		return $this->value() > $other->value();
	}
}
```

## File: `src/Shared/Domain/ValueObject/SimpleUuid.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Shared\Domain\ValueObject;

final class SimpleUuid extends Uuid {}
```

## File: `src/Shared/Domain/ValueObject/StringValueObject.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Shared\Domain\ValueObject;

abstract class StringValueObject
{
	public function __construct(protected string $value) {}

	final public function value(): string
	{
		return $this->value;
	}
}
```

## File: `src/Shared/Domain/ValueObject/Uuid.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Shared\Domain\ValueObject;

use InvalidArgumentException;
use Ramsey\Uuid\Uuid as RamseyUuid;
use Stringable;

abstract class Uuid implements Stringable
{
	final public function __construct(protected string $value)
	{
		$this->ensureIsValidUuid($value);
	}

	final public static function random(): self
	{
		return new static(RamseyUuid::uuid4()->toString());
	}

	final public function value(): string
	{
		return $this->value;
	}

	final public function equals(self $other): bool
	{
		return $this->value() === $other->value();
	}

	public function __toString(): string
	{
		return $this->value();
	}

	private function ensureIsValidUuid(string $id): void
	{
		if (!RamseyUuid::isValid($id)) {
			throw new InvalidArgumentException(sprintf('<%s> does not allow the value <%s>.', self::class, $id));
		}
	}
}
```

## File: `src/Shared/Infrastructure/PhpRandomNumberGenerator.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Shared\Infrastructure;

use CodelyTv\Shared\Domain\RandomNumberGenerator;

final class PhpRandomNumberGenerator implements RandomNumberGenerator
{
	public function generate(): int
	{
		return random_int(1, 5);
	}
}
```

## File: `src/Shared/Infrastructure/RamseyUuidGenerator.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Shared\Infrastructure;

use CodelyTv\Shared\Domain\UuidGenerator;
use Ramsey\Uuid\Uuid;

final class RamseyUuidGenerator implements UuidGenerator
{
	public function generate(): string
	{
		return Uuid::uuid4()->toString();
	}
}
```

## File: `src/Shared/Infrastructure/Bus/CallableFirstParameterExtractor.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Shared\Infrastructure\Bus;

use CodelyTv\Shared\Domain\Bus\Event\DomainEventSubscriber;
use LogicException;
use ReflectionClass;
use ReflectionMethod;
use ReflectionNamedType;

use function Lambdish\Phunctional\map;
use function Lambdish\Phunctional\reduce;
use function Lambdish\Phunctional\reindex;

final class CallableFirstParameterExtractor
{
	public static function forCallables(iterable $callables): array
	{
		return map(self::unflatten(), reindex(self::classExtractor(new self()), $callables));
	}

	public static function forPipedCallables(iterable $callables): array
	{
		return reduce(self::pipedCallablesReducer(), $callables, []);
	}

	private static function classExtractor(self $parameterExtractor): callable
	{
		return static fn (object $handler): ?string => $parameterExtractor->extract($handler);
	}

	private static function pipedCallablesReducer(): callable
	{
		return static function (array $subscribers, DomainEventSubscriber $subscriber): array {
			$subscribedEvents = $subscriber::subscribedTo();

			foreach ($subscribedEvents as $subscribedEvent) {
				$subscribers[$subscribedEvent][] = $subscriber;
			}

			return $subscribers;
		};
	}

	private static function unflatten(): callable
	{
		return static fn (mixed $value): array => [$value];
	}

	public function extract(object $class): ?string
	{
		$reflector = new ReflectionClass($class);
		$method = $reflector->getMethod('__invoke');

		if ($this->hasOnlyOneParameter($method)) {
			return $this->firstParameterClassFrom($method);
		}

		return null;
	}

	private function firstParameterClassFrom(ReflectionMethod $method): string
	{
		/** @var ReflectionNamedType|null $fistParameterType */
		$fistParameterType = $method->getParameters()[0]->getType();

		if ($fistParameterType === null) {
			throw new LogicException('Missing type hint for the first parameter of __invoke');
		}

		return $fistParameterType->getName();
	}

	private function hasOnlyOneParameter(ReflectionMethod $method): bool
	{
		return $method->getNumberOfParameters() === 1;
	}
}
```

## File: `src/Shared/Infrastructure/Bus/Command/CommandNotRegisteredError.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Shared\Infrastructure\Bus\Command;

use CodelyTv\Shared\Domain\Bus\Command\Command;
use RuntimeException;

final class CommandNotRegisteredError extends RuntimeException
{
	public function __construct(Command $command)
	{
		$commandClass = $command::class;

		parent::__construct("The command <$commandClass> hasn't a command handler associated");
	}
}
```

## File: `src/Shared/Infrastructure/Bus/Command/InMemorySymfonyCommandBus.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Shared\Infrastructure\Bus\Command;

use CodelyTv\Shared\Domain\Bus\Command\Command;
use CodelyTv\Shared\Domain\Bus\Command\CommandBus;
use CodelyTv\Shared\Infrastructure\Bus\CallableFirstParameterExtractor;
use Symfony\Component\Messenger\Exception\HandlerFailedException;
use Symfony\Component\Messenger\Exception\NoHandlerForMessageException;
use Symfony\Component\Messenger\Handler\HandlersLocator;
use Symfony\Component\Messenger\MessageBus;
use Symfony\Component\Messenger\Middleware\HandleMessageMiddleware;

final class InMemorySymfonyCommandBus implements CommandBus
{
	private readonly MessageBus $bus;

	public function __construct(iterable $commandHandlers)
	{
		$this->bus = new MessageBus(
			[
				new HandleMessageMiddleware(
					new HandlersLocator(CallableFirstParameterExtractor::forCallables($commandHandlers))
				),
			]
		);
	}

	public function dispatch(Command $command): void
	{
		try {
			$this->bus->dispatch($command);
		} catch (NoHandlerForMessageException) {
			throw new CommandNotRegisteredError($command);
		} catch (HandlerFailedException $error) {
			throw $error->getPrevious() ?? $error;
		}
	}
}
```

## File: `src/Shared/Infrastructure/Bus/Event/DomainEventJsonDeserializer.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Shared\Infrastructure\Bus\Event;

use CodelyTv\Shared\Domain\Bus\Event\DomainEvent;
use CodelyTv\Shared\Domain\Utils;

final readonly class DomainEventJsonDeserializer
{
	public function __construct(private DomainEventMapping $mapping) {}

	public function deserialize(string $domainEvent): DomainEvent
	{
		$eventData = Utils::jsonDecode($domainEvent);
		$eventName = $eventData['data']['type'];
		$eventClass = $this->mapping->for($eventName);

		return $eventClass::fromPrimitives(
			$eventData['data']['attributes']['id'],
			$eventData['data']['attributes'],
			$eventData['data']['id'],
			$eventData['data']['occurred_on']
		);
	}
}
```

## File: `src/Shared/Infrastructure/Bus/Event/DomainEventJsonSerializer.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Shared\Infrastructure\Bus\Event;

use CodelyTv\Shared\Domain\Bus\Event\DomainEvent;

final class DomainEventJsonSerializer
{
	public static function serialize(DomainEvent $domainEvent): string
	{
		return json_encode(
			[
				'data' => [
					'id' => $domainEvent->eventId(),
					'type' => $domainEvent::eventName(),
					'occurred_on' => $domainEvent->occurredOn(),
					'attributes' => array_merge($domainEvent->toPrimitives(), ['id' => $domainEvent->aggregateId()]),
				],
				'meta' => [],
			]
		);
	}
}
```

## File: `src/Shared/Infrastructure/Bus/Event/DomainEventMapping.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Shared\Infrastructure\Bus\Event;

use CodelyTv\Shared\Domain\Bus\Event\DomainEventSubscriber;
use RuntimeException;

use function Lambdish\Phunctional\reduce;
use function Lambdish\Phunctional\reindex;

final class DomainEventMapping
{
	private array $mapping;

	public function __construct(iterable $mapping)
	{
		$this->mapping = reduce($this->eventsExtractor(), $mapping, []);
	}

	public function for(string $name): string
	{
		if (!isset($this->mapping[$name])) {
			throw new RuntimeException("The Domain Event Class for <$name> doesn't exists or have no subscribers");
		}

		return $this->mapping[$name];
	}

	private function eventsExtractor(): callable
	{
		return fn (array $mapping, DomainEventSubscriber $subscriber): array => array_merge(
			$mapping,
			reindex($this->eventNameExtractor(), $subscriber::subscribedTo())
		);
	}

	private function eventNameExtractor(): callable
	{
		return static fn (string $eventClass): string => $eventClass::eventName();
	}
}
```

## File: `src/Shared/Infrastructure/Bus/Event/DomainEventSubscriberLocator.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Shared\Infrastructure\Bus\Event;

use CodelyTv\Shared\Domain\Bus\Event\DomainEventSubscriber;
use CodelyTv\Shared\Infrastructure\Bus\CallableFirstParameterExtractor;
use CodelyTv\Shared\Infrastructure\Bus\Event\RabbitMq\RabbitMqQueueNameFormatter;
use RuntimeException;
use Traversable;

use function Lambdish\Phunctional\search;

final class DomainEventSubscriberLocator
{
	private readonly array $mapping;

	public function __construct(Traversable $mapping)
	{
		$this->mapping = iterator_to_array($mapping);
	}

	public function allSubscribedTo(string $eventClass): array
	{
		$formatted = CallableFirstParameterExtractor::forPipedCallables($this->mapping);

		return $formatted[$eventClass];
	}

	public function withRabbitMqQueueNamed(string $queueName): callable | DomainEventSubscriber
	{
		$subscriber = search(
			static fn (DomainEventSubscriber $subscriber): bool => RabbitMqQueueNameFormatter::format($subscriber) ===
															$queueName,
			$this->mapping
		);

		if ($subscriber === null) {
			throw new RuntimeException("There are no subscribers for the <$queueName> queue");
		}

		return $subscriber;
	}

	public function all(): array
	{
		return $this->mapping;
	}
}
```

## File: `src/Shared/Infrastructure/Bus/Event/InMemory/InMemorySymfonyEventBus.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Shared\Infrastructure\Bus\Event\InMemory;

use CodelyTv\Shared\Domain\Bus\Event\DomainEvent;
use CodelyTv\Shared\Domain\Bus\Event\EventBus;
use CodelyTv\Shared\Infrastructure\Bus\CallableFirstParameterExtractor;
use Symfony\Component\Messenger\Exception\NoHandlerForMessageException;
use Symfony\Component\Messenger\Handler\HandlersLocator;
use Symfony\Component\Messenger\MessageBus;
use Symfony\Component\Messenger\Middleware\HandleMessageMiddleware;

class InMemorySymfonyEventBus implements EventBus
{
	private readonly MessageBus $bus;

	public function __construct(iterable $subscribers)
	{
		$this->bus = new MessageBus(
			[
				new HandleMessageMiddleware(
					new HandlersLocator(CallableFirstParameterExtractor::forPipedCallables($subscribers))
				),
			]
		);
	}

	public function publish(DomainEvent ...$events): void
	{
		foreach ($events as $event) {
			try {
				$this->bus->dispatch($event);
			} catch (NoHandlerForMessageException) {
			}
		}
	}
}
```

## File: `src/Shared/Infrastructure/Bus/Event/MySql/MySqlDoctrineDomainEventsConsumer.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Shared\Infrastructure\Bus\Event\MySql;

use CodelyTv\Shared\Domain\Utils;
use CodelyTv\Shared\Infrastructure\Bus\Event\DomainEventMapping;
use DateTimeImmutable;
use Doctrine\DBAL\Connection;
use Doctrine\ORM\EntityManager;
use RuntimeException;

use function Lambdish\Phunctional\each;
use function Lambdish\Phunctional\map;

final readonly class MySqlDoctrineDomainEventsConsumer
{
	private Connection $connection;

	public function __construct(EntityManager $entityManager, private DomainEventMapping $eventMapping)
	{
		$this->connection = $entityManager->getConnection();
	}

	public function consume(callable $subscribers, int $eventsToConsume): void
	{
		$events = $this->connection
			->executeQuery("SELECT * FROM domain_events ORDER BY occurred_on ASC LIMIT $eventsToConsume")
			->fetchAllAssociative();

		each($this->executeSubscribers($subscribers), $events);

		$ids = implode(', ', map($this->idExtractor(), $events));

		if (!empty($ids)) {
			$this->connection->executeStatement("DELETE FROM domain_events WHERE id IN ($ids)");
		}
	}

	private function executeSubscribers(callable $subscribers): callable
	{
		return function (array $rawEvent) use ($subscribers): void {
			try {
				$domainEventClass = $this->eventMapping->for($rawEvent['name']);
				$domainEvent = $domainEventClass::fromPrimitives(
					$rawEvent['aggregate_id'],
					Utils::jsonDecode($rawEvent['body']),
					$rawEvent['id'],
					$this->formatDate($rawEvent['occurred_on'])
				);

				$subscribers($domainEvent);
			} catch (RuntimeException) {
			}
		};
	}

	private function formatDate(mixed $stringDate): string
	{
		return Utils::dateToString(new DateTimeImmutable($stringDate));
	}

	private function idExtractor(): callable
	{
		return static fn (array $event): string => "'{$event['id']}'";
	}
}
```

## File: `src/Shared/Infrastructure/Bus/Event/MySql/MySqlDoctrineEventBus.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Shared\Infrastructure\Bus\Event\MySql;

use CodelyTv\Shared\Domain\Bus\Event\DomainEvent;
use CodelyTv\Shared\Domain\Bus\Event\EventBus;
use CodelyTv\Shared\Domain\Utils;
use Doctrine\DBAL\Connection;
use Doctrine\ORM\EntityManager;

use function Lambdish\Phunctional\each;

final class MySqlDoctrineEventBus implements EventBus
{
	private const DATABASE_TIMESTAMP_FORMAT = 'Y-m-d H:i:s';
	private readonly Connection $connection;

	public function __construct(EntityManager $entityManager)
	{
		$this->connection = $entityManager->getConnection();
	}

	public function publish(DomainEvent ...$events): void
	{
		each($this->publisher(), $events);
	}

	private function publisher(): callable
	{
		return function (DomainEvent $domainEvent): void {
			$id = $this->connection->quote($domainEvent->eventId());
			$aggregateId = $this->connection->quote($domainEvent->aggregateId());
			$name = $this->connection->quote($domainEvent::eventName());
			$body = $this->connection->quote(Utils::jsonEncode($domainEvent->toPrimitives()));
			$occurredOn = $this->connection->quote(
				Utils::stringToDate($domainEvent->occurredOn())->format(self::DATABASE_TIMESTAMP_FORMAT)
			);

			$this->connection->executeStatement(
				<<<SQL
                                    INSERT INTO domain_events (id,  aggregate_id, name,  body,  occurred_on) 
                                                       VALUES ($id, $aggregateId, $name, $body, $occurredOn);
                    SQL
			);
		};
	}
}
```

## File: `src/Shared/Infrastructure/Bus/Event/RabbitMq/RabbitMqConfigurer.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Shared\Infrastructure\Bus\Event\RabbitMq;

use AMQPQueue;
use CodelyTv\Shared\Domain\Bus\Event\DomainEventSubscriber;

use function Lambdish\Phunctional\each;

final readonly class RabbitMqConfigurer
{
	public function __construct(private RabbitMqConnection $connection) {}

	public function configure(string $exchangeName, DomainEventSubscriber ...$subscribers): void
	{
		$retryExchangeName = RabbitMqExchangeNameFormatter::retry($exchangeName);
		$deadLetterExchangeName = RabbitMqExchangeNameFormatter::deadLetter($exchangeName);

		$this->declareExchange($exchangeName);
		$this->declareExchange($retryExchangeName);
		$this->declareExchange($deadLetterExchangeName);

		$this->declareQueues($exchangeName, $retryExchangeName, $deadLetterExchangeName, ...$subscribers);
	}

	private function declareExchange(string $exchangeName): void
	{
		$exchange = $this->connection->exchange($exchangeName);
		$exchange->setType(AMQP_EX_TYPE_TOPIC);
		$exchange->setFlags(AMQP_DURABLE);
		$exchange->declareExchange();
	}

	private function declareQueues(
		string $exchangeName,
		string $retryExchangeName,
		string $deadLetterExchangeName,
		DomainEventSubscriber ...$subscribers
	): void {
		each($this->queueDeclarator($exchangeName, $retryExchangeName, $deadLetterExchangeName), $subscribers);
	}

	private function queueDeclarator(
		string $exchangeName,
		string $retryExchangeName,
		string $deadLetterExchangeName
	): callable {
		return function (DomainEventSubscriber $subscriber) use (
			$exchangeName,
			$retryExchangeName,
			$deadLetterExchangeName
		): void {
			$queueName = RabbitMqQueueNameFormatter::format($subscriber);
			$retryQueueName = RabbitMqQueueNameFormatter::formatRetry($subscriber);
			$deadLetterQueueName = RabbitMqQueueNameFormatter::formatDeadLetter($subscriber);

			$queue = $this->declareQueue($queueName);
			$retryQueue = $this->declareQueue($retryQueueName, $exchangeName, $queueName, 1000);
			$deadLetterQueue = $this->declareQueue($deadLetterQueueName);

			$queue->bind($exchangeName, $queueName);
			$retryQueue->bind($retryExchangeName, $queueName);
			$deadLetterQueue->bind($deadLetterExchangeName, $queueName);

			foreach ($subscriber::subscribedTo() as $eventClass) {
				$queue->bind($exchangeName, $eventClass::eventName());
			}
		};
	}

	private function declareQueue(
		string $name,
		string $deadLetterExchange = null,
		string $deadLetterRoutingKey = null,
		int $messageTtl = null
	): AMQPQueue {
		$queue = $this->connection->queue($name);

		if ($deadLetterExchange !== null) {
			$queue->setArgument('x-dead-letter-exchange', $deadLetterExchange);
		}

		if ($deadLetterRoutingKey !== null) {
			$queue->setArgument('x-dead-letter-routing-key', $deadLetterRoutingKey);
		}

		if ($messageTtl !== null) {
			$queue->setArgument('x-message-ttl', $messageTtl);
		}

		$queue->setFlags(AMQP_DURABLE);
		$queue->declareQueue();

		return $queue;
	}
}
```

## File: `src/Shared/Infrastructure/Bus/Event/RabbitMq/RabbitMqConnection.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Shared\Infrastructure\Bus\Event\RabbitMq;

use AMQPChannel;
use AMQPConnection;
use AMQPExchange;
use AMQPQueue;

final class RabbitMqConnection
{
	private static ?AMQPConnection $connection = null;
	private static ?AMQPChannel $channel = null;
	/** @var AMQPExchange[] */
	private static array $exchanges = [];
	/** @var AMQPQueue[] */
	private static array $queues = [];

	public function __construct(private readonly array $configuration) {}

	public function queue(string $name): AMQPQueue
	{
		if (!array_key_exists($name, self::$queues)) {
			$queue = new AMQPQueue($this->channel());
			$queue->setName($name);

			self::$queues[$name] = $queue;
		}

		return self::$queues[$name];
	}

	public function exchange(string $name): AMQPExchange
	{
		if (!array_key_exists($name, self::$exchanges)) {
			$exchange = new AMQPExchange($this->channel());
			$exchange->setName($name);

			self::$exchanges[$name] = $exchange;
		}

		return self::$exchanges[$name];
	}

	private function channel(): AMQPChannel
	{
		if (!self::$channel?->isConnected()) {
			self::$channel = new AMQPChannel($this->connection());
		}

		return self::$channel;
	}

	private function connection(): AMQPConnection
	{
		if (self::$connection === null) {
			self::$connection = new AMQPConnection($this->configuration);
		}

		if (!self::$connection->isConnected()) {
			self::$connection->pconnect();
		}

		return self::$connection;
	}
}
```

## File: `src/Shared/Infrastructure/Bus/Event/RabbitMq/RabbitMqDomainEventsConsumer.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Shared\Infrastructure\Bus\Event\RabbitMq;

use AMQPEnvelope;
use AMQPQueue;
use AMQPQueueException;
use CodelyTv\Shared\Domain\Bus\Event\DomainEventSubscriber;
use CodelyTv\Shared\Infrastructure\Bus\Event\DomainEventJsonDeserializer;
use Throwable;

use function Lambdish\Phunctional\assoc;
use function Lambdish\Phunctional\get;

final readonly class RabbitMqDomainEventsConsumer
{
	public function __construct(
		private RabbitMqConnection $connection,
		private DomainEventJsonDeserializer $deserializer,
		private string $exchangeName,
		private int $maxRetries
	) {}

	public function consume(callable | DomainEventSubscriber $subscriber, string $queueName): void
	{
		try {
			$this->connection->queue($queueName)->consume($this->consumer($subscriber));
		} catch (AMQPQueueException) {
			// We don't want to raise an error if there are no messages in the queue
		}
	}

	private function consumer(callable $subscriber): callable
	{
		return function (AMQPEnvelope $envelope, AMQPQueue $queue) use ($subscriber): void {
			$event = $this->deserializer->deserialize($envelope->getBody());

			try {
				$subscriber($event);
			} catch (Throwable $error) {
				$this->handleConsumptionError($envelope, $queue);

				throw $error;
			}

			$queue->ack($envelope->getDeliveryTag());
		};
	}

	private function handleConsumptionError(AMQPEnvelope $envelope, AMQPQueue $queue): void
	{
		$this->hasBeenRedeliveredTooMuch($envelope)
			? $this->sendToDeadLetter($envelope, $queue)
			: $this->sendToRetry($envelope, $queue);

		$queue->ack($envelope->getDeliveryTag());
	}

	private function hasBeenRedeliveredTooMuch(AMQPEnvelope $envelope): bool
	{
		return get('redelivery_count', $envelope->getHeaders(), 0) >= $this->maxRetries;
	}

	private function sendToDeadLetter(AMQPEnvelope $envelope, AMQPQueue $queue): void
	{
		$this->sendMessageTo(RabbitMqExchangeNameFormatter::deadLetter($this->exchangeName), $envelope, $queue);
	}

	private function sendToRetry(AMQPEnvelope $envelope, AMQPQueue $queue): void
	{
		$this->sendMessageTo(RabbitMqExchangeNameFormatter::retry($this->exchangeName), $envelope, $queue);
	}

	private function sendMessageTo(string $exchangeName, AMQPEnvelope $envelope, AMQPQueue $queue): void
	{
		$headers = $envelope->getHeaders();

		$this->connection->exchange($exchangeName)->publish(
			$envelope->getBody(),
			$queue->getName(),
			AMQP_NOPARAM,
			[
				'message_id' => $envelope->getMessageId(),
				'content_type' => $envelope->getContentType(),
				'content_encoding' => $envelope->getContentEncoding(),
				'priority' => $envelope->getPriority(),
				'headers' => assoc($headers, 'redelivery_count', get('redelivery_count', $headers, 0) + 1),
			]
		);
	}
}
```

## File: `src/Shared/Infrastructure/Bus/Event/RabbitMq/RabbitMqEventBus.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Shared\Infrastructure\Bus\Event\RabbitMq;

use AMQPException;
use CodelyTv\Shared\Domain\Bus\Event\DomainEvent;
use CodelyTv\Shared\Domain\Bus\Event\EventBus;
use CodelyTv\Shared\Infrastructure\Bus\Event\DomainEventJsonSerializer;
use CodelyTv\Shared\Infrastructure\Bus\Event\MySql\MySqlDoctrineEventBus;

use function Lambdish\Phunctional\each;

final readonly class RabbitMqEventBus implements EventBus
{
	public function __construct(
		private RabbitMqConnection $connection,
		private string $exchangeName,
		private MySqlDoctrineEventBus $failoverPublisher
	) {}

	public function publish(DomainEvent ...$events): void
	{
		each($this->publisher(), $events);
	}

	private function publisher(): callable
	{
		return function (DomainEvent $event): void {
			try {
				$this->publishEvent($event);
			} catch (AMQPException) {
				$this->failoverPublisher->publish($event);
			}
		};
	}

	private function publishEvent(DomainEvent $event): void
	{
		$body = DomainEventJsonSerializer::serialize($event);
		$routingKey = $event::eventName();
		$messageId = $event->eventId();

		$this->connection->exchange($this->exchangeName)->publish(
			$body,
			$routingKey,
			AMQP_NOPARAM,
			[
				'message_id' => $messageId,
				'content_type' => 'application/json',
				'content_encoding' => 'utf-8',
			]
		);
	}
}
```

## File: `src/Shared/Infrastructure/Bus/Event/RabbitMq/RabbitMqExchangeNameFormatter.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Shared\Infrastructure\Bus\Event\RabbitMq;

final class RabbitMqExchangeNameFormatter
{
	public static function retry(string $exchangeName): string
	{
		return "retry-$exchangeName";
	}

	public static function deadLetter(string $exchangeName): string
	{
		return "dead_letter-$exchangeName";
	}
}
```

## File: `src/Shared/Infrastructure/Bus/Event/RabbitMq/RabbitMqQueueNameFormatter.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Shared\Infrastructure\Bus\Event\RabbitMq;

use CodelyTv\Shared\Domain\Bus\Event\DomainEventSubscriber;
use CodelyTv\Shared\Domain\Utils;

use function Lambdish\Phunctional\last;
use function Lambdish\Phunctional\map;

final class RabbitMqQueueNameFormatter
{
	public static function format(DomainEventSubscriber $subscriber): string
	{
		$subscriberClassPaths = explode('\\', str_replace('CodelyTv', 'codelytv', $subscriber::class));

		$queueNameParts = [
			$subscriberClassPaths[0],
			$subscriberClassPaths[1],
			$subscriberClassPaths[2],
			last($subscriberClassPaths),
		];

		return implode('.', map(self::toSnakeCase(), $queueNameParts));
	}

	public static function formatRetry(DomainEventSubscriber $subscriber): string
	{
		$queueName = self::format($subscriber);

		return "retry.$queueName";
	}

	public static function formatDeadLetter(DomainEventSubscriber $subscriber): string
	{
		$queueName = self::format($subscriber);

		return "dead_letter.$queueName";
	}

	public static function shortFormat(DomainEventSubscriber $subscriber): string
	{
		$subscriberCamelCaseName = (string) last(explode('\\', $subscriber::class));

		return Utils::toSnakeCase($subscriberCamelCaseName);
	}

	private static function toSnakeCase(): callable
	{
		return static fn (string $text): string => Utils::toSnakeCase($text);
	}
}
```

## File: `src/Shared/Infrastructure/Bus/Event/WithMonitoring/WithPrometheusMonitoringEventBus.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Shared\Infrastructure\Bus\Event\WithMonitoring;

use CodelyTv\Shared\Domain\Bus\Event\DomainEvent;
use CodelyTv\Shared\Domain\Bus\Event\EventBus;
use CodelyTv\Shared\Infrastructure\Monitoring\PrometheusMonitor;

use function Lambdish\Phunctional\each;

final readonly class WithPrometheusMonitoringEventBus implements EventBus
{
	public function __construct(
		private PrometheusMonitor $monitor,
		private string $appName,
		private EventBus $bus
	) {}

	public function publish(DomainEvent ...$events): void
	{
		$counter = $this->monitor->registry()->getOrRegisterCounter(
			$this->appName,
			'domain_event',
			'Domain Events',
			['name']
		);

		each(fn (DomainEvent $event) => $counter->inc(['name' => $event::eventName()]), $events);

		$this->bus->publish(...$events);
	}
}
```

## File: `src/Shared/Infrastructure/Bus/Query/InMemorySymfonyQueryBus.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Shared\Infrastructure\Bus\Query;

use CodelyTv\Shared\Domain\Bus\Query\Query;
use CodelyTv\Shared\Domain\Bus\Query\QueryBus;
use CodelyTv\Shared\Domain\Bus\Query\Response;
use CodelyTv\Shared\Infrastructure\Bus\CallableFirstParameterExtractor;
use Symfony\Component\Messenger\Exception\NoHandlerForMessageException;
use Symfony\Component\Messenger\Handler\HandlersLocator;
use Symfony\Component\Messenger\MessageBus;
use Symfony\Component\Messenger\Middleware\HandleMessageMiddleware;
use Symfony\Component\Messenger\Stamp\HandledStamp;

final readonly class InMemorySymfonyQueryBus implements QueryBus
{
	private MessageBus $bus;

	public function __construct(iterable $queryHandlers)
	{
		$this->bus = new MessageBus(
			[
				new HandleMessageMiddleware(new HandlersLocator(CallableFirstParameterExtractor::forCallables($queryHandlers))),
			]
		);
	}

	public function ask(Query $query): ?Response
	{
		try {
			/** @var HandledStamp $stamp */
			$stamp = $this->bus->dispatch($query)->last(HandledStamp::class);

			return $stamp->getResult();
		} catch (NoHandlerForMessageException) {
			throw new QueryNotRegisteredError($query);
		}
	}
}
```

## File: `src/Shared/Infrastructure/Bus/Query/QueryNotRegisteredError.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Shared\Infrastructure\Bus\Query;

use CodelyTv\Shared\Domain\Bus\Query\Query;
use RuntimeException;

final class QueryNotRegisteredError extends RuntimeException
{
	public function __construct(Query $query)
	{
		$queryClass = $query::class;

		parent::__construct("The query <$queryClass> has no associated query handler");
	}
}
```

## File: `src/Shared/Infrastructure/Cdc/DatabaseMutationAction.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Shared\Infrastructure\Cdc;

enum DatabaseMutationAction: string
{
	case INSERT = 'INSERT';
	case UPDATE = 'UPDATE';
	case DELETE = 'DELETE';
}
```

## File: `src/Shared/Infrastructure/Cdc/DatabaseMutationToDomainEvent.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Shared\Infrastructure\Cdc;

use CodelyTv\Shared\Domain\Bus\Event\DomainEvent;

interface DatabaseMutationToDomainEvent
{
	/** @return DomainEvent[] */
	public function transform(array $data): array;

	public function tableName(): string;

	public function mutationAction(): DatabaseMutationAction;
}
```

## File: `src/Shared/Infrastructure/Doctrine/DatabaseConnections.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Shared\Infrastructure\Doctrine;

use CodelyTv\Shared\Domain\Utils;
use CodelyTv\Tests\Shared\Infrastructure\Doctrine\MySqlDatabaseCleaner;
use Doctrine\ORM\EntityManager;

use function Lambdish\Phunctional\apply;
use function Lambdish\Phunctional\each;

final class DatabaseConnections
{
	private readonly array $connections;

	public function __construct(iterable $connections)
	{
		$this->connections = Utils::iterableToArray($connections);
	}

	public function clear(): void
	{
		each(fn (EntityManager $entityManager) => $entityManager->clear(), $this->connections);
	}

	public function truncate(): void
	{
		apply(new MySqlDatabaseCleaner(), array_values($this->connections));
	}
}
```

## File: `src/Shared/Infrastructure/Doctrine/DoctrineEntityManagerFactory.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Shared\Infrastructure\Doctrine;

use CodelyTv\Shared\Infrastructure\Doctrine\Dbal\DbalCustomTypesRegistrar;
use Doctrine\Common\EventManager;
use Doctrine\DBAL\DriverManager;
use Doctrine\DBAL\Platforms\MariaDBPlatform;
use Doctrine\DBAL\Schema\DefaultSchemaManagerFactory;
use Doctrine\DBAL\Schema\MySQLSchemaManager;
use Doctrine\ORM\Configuration;
use Doctrine\ORM\EntityManager;
use Doctrine\ORM\Mapping\Driver\SimplifiedXmlDriver;
use Doctrine\ORM\ORMSetup;
use RuntimeException;

use function Lambdish\Phunctional\dissoc;

final class DoctrineEntityManagerFactory
{
	private static array $sharedPrefixes = [
		__DIR__ . '/../../../Shared/Infrastructure/Persistence/Mappings' => 'CodelyTv\Shared\Domain',
	];

	public static function create(
		array $parameters,
		array $contextPrefixes,
		bool $isDevMode,
		string $schemaFile,
		array $dbalCustomTypesClasses
	): EntityManager {
		if ($isDevMode) {
			self::generateDatabaseIfNotExists($parameters, $schemaFile);
		}

		DbalCustomTypesRegistrar::register($dbalCustomTypesClasses);

		$config = self::createConfiguration($contextPrefixes, $isDevMode);
		$eventManager = new EventManager();

		return new EntityManager(
			DriverManager::getConnection($parameters, $config, $eventManager),
			$config,
			$eventManager
		);
	}

	private static function generateDatabaseIfNotExists(array $parameters, string $schemaFile): void
	{
		self::ensureSchemaFileExists($schemaFile);

		$databaseName = $parameters['dbname'];
		$parametersWithoutDatabaseName = dissoc($parameters, 'dbname');
		$connection = DriverManager::getConnection($parametersWithoutDatabaseName);
		$platform = new MariaDBPlatform();
		$schemaManager = new MySQLSchemaManager($connection, $platform);

		if (!self::databaseExists($databaseName, $schemaManager)) {
			$schemaManager->createDatabase($databaseName);

			$connection->executeStatement(sprintf('USE %s', $databaseName));
			$connection->executeStatement(file_get_contents(realpath($schemaFile)));
		}

		$connection->close();
	}

	private static function databaseExists(string $databaseName, MySQLSchemaManager $schemaManager): bool
	{
		return in_array($databaseName, $schemaManager->listDatabases(), true);
	}

	private static function ensureSchemaFileExists(string $schemaFile): void
	{
		if (!file_exists($schemaFile)) {
			throw new RuntimeException(sprintf('The file <%s> does not exist', $schemaFile));
		}
	}

	private static function createConfiguration(array $contextPrefixes, bool $isDevMode): Configuration
	{
		$config = ORMSetup::createConfiguration($isDevMode);

		$config->setMetadataDriverImpl(new SimplifiedXmlDriver(array_merge(self::$sharedPrefixes, $contextPrefixes)));
		$config->setSchemaManagerFactory(new DefaultSchemaManagerFactory());

		return $config;
	}
}
```

## File: `src/Shared/Infrastructure/Doctrine/Dbal/DbalCustomTypesRegistrar.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Shared\Infrastructure\Doctrine\Dbal;

use Doctrine\DBAL\Types\Type;

use function Lambdish\Phunctional\each;

final class DbalCustomTypesRegistrar
{
	private static bool $initialized = false;

	public static function register(array $customTypeClassNames): void
	{
		if (!self::$initialized) {
			each(self::registerType(), $customTypeClassNames);

			self::$initialized = true;
		}
	}

	private static function registerType(): callable
	{
		return static function (mixed $customTypeClassName): void {
			$name = $customTypeClassName::customTypeName();

			Type::addType($name, $customTypeClassName);
		};
	}
}
```

## File: `src/Shared/Infrastructure/Doctrine/Dbal/DoctrineCustomType.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Shared\Infrastructure\Doctrine\Dbal;

interface DoctrineCustomType
{
	public static function customTypeName(): string;
}
```

## File: `src/Shared/Infrastructure/Elasticsearch/ElasticsearchClient.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Shared\Infrastructure\Elasticsearch;

use Elasticsearch\Client;

final readonly class ElasticsearchClient
{
	public function __construct(private Client $client, private string $indexPrefix) {}

	public function persist(string $aggregateName, string $identifier, array $plainBody): void
	{
		$this->client->index(
			[
				'index' => sprintf('%s_%s', $this->indexPrefix, $aggregateName),
				'id' => $identifier,
				'body' => $plainBody,
			]
		);
	}

	public function client(): Client
	{
		return $this->client;
	}

	public function indexPrefix(): string
	{
		return $this->indexPrefix;
	}
}
```

## File: `src/Shared/Infrastructure/Elasticsearch/ElasticsearchClientFactory.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Shared\Infrastructure\Elasticsearch;

use CodelyTv\Shared\Domain\Utils;
use Elasticsearch\Client;
use Elasticsearch\ClientBuilder;
use Elasticsearch\Common\Exceptions\Missing404Exception;

final class ElasticsearchClientFactory
{
	public function __invoke(
		string $host,
		string $indexPrefix,
		string $schemasFolder,
		string $environment
	): ElasticsearchClient {
		$client = ClientBuilder::create()->setHosts([$host])->build();

		$this->generateIndexIfNotExists($client, $indexPrefix, $schemasFolder, $environment);

		return new ElasticsearchClient($client, $indexPrefix);
	}

	private function generateIndexIfNotExists(
		Client $client,
		string $indexPrefix,
		string $schemasFolder,
		string $environment
	): void {
		if ($environment !== 'prod') {
			return;
		}

		$indexes = Utils::filesIn($schemasFolder, '.json');

		foreach ($indexes as $index) {
			$indexName = str_replace('.json', '', sprintf('%s_%s', $indexPrefix, $index));

			if (!$this->indexExists($client, $indexName)) {
				$indexBody = Utils::jsonDecode(file_get_contents("$schemasFolder/$index"));

				$client->indices()->create(['index' => $indexName, 'body' => $indexBody]);
			}
		}
	}

	private function indexExists(Client $client, string $indexName): bool
	{
		try {
			$client->indices()->getSettings(['index' => $indexName]);

			return true;
		} catch (Missing404Exception) {
			return false;
		}
	}
}
```

## File: `src/Shared/Infrastructure/Logger/MonologLogger.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Shared\Infrastructure\Logger;

use CodelyTv\Shared\Domain\Logger;

final readonly class MonologLogger implements Logger
{
	public function __construct(private \Monolog\Logger $logger) {}

	public function info(string $message, array $context = []): void
	{
		$this->logger->info($message, $context);
	}

	public function warning(string $message, array $context = []): void
	{
		$this->logger->warning($message, $context);
	}

	public function critical(string $message, array $context = []): void
	{
		$this->logger->critical($message, $context);
	}
}
```

## File: `src/Shared/Infrastructure/Monitoring/PrometheusMonitor.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Shared\Infrastructure\Monitoring;

use Prometheus\CollectorRegistry;
use Prometheus\Storage\APC;

final readonly class PrometheusMonitor
{
	private CollectorRegistry $registry;

	public function __construct()
	{
		$this->registry = new CollectorRegistry(new APC());
	}

	public function registry(): CollectorRegistry
	{
		return $this->registry;
	}
}
```

## File: `src/Shared/Infrastructure/Persistence/Doctrine/DoctrineCriteriaConverter.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Shared\Infrastructure\Persistence\Doctrine;

use CodelyTv\Shared\Domain\Criteria\Criteria;
use CodelyTv\Shared\Domain\Criteria\Filter;
use CodelyTv\Shared\Domain\Criteria\FilterField;
use CodelyTv\Shared\Domain\Criteria\OrderBy;
use Doctrine\Common\Collections\Criteria as DoctrineCriteria;
use Doctrine\Common\Collections\Expr\Comparison;
use Doctrine\Common\Collections\Expr\CompositeExpression;

final readonly class DoctrineCriteriaConverter
{
	public function __construct(
		private Criteria $criteria,
		private array $criteriaToDoctrineFields = [],
		private array $hydrators = []
	) {}

	public static function convert(
		Criteria $criteria,
		array $criteriaToDoctrineFields = [],
		array $hydrators = []
	): DoctrineCriteria {
		$converter = new self($criteria, $criteriaToDoctrineFields, $hydrators);

		return $converter->convertToDoctrineCriteria();
	}

	private function convertToDoctrineCriteria(): DoctrineCriteria
	{
		return new DoctrineCriteria(
			$this->buildExpression($this->criteria),
			$this->formatOrder($this->criteria),
			$this->criteria->offset(),
			$this->criteria->limit()
		);
	}

	private function buildExpression(Criteria $criteria): ?CompositeExpression
	{
		if ($criteria->hasFilters()) {
			return new CompositeExpression(
				CompositeExpression::TYPE_AND,
				array_map($this->buildComparison(), $criteria->plainFilters())
			);
		}

		return null;
	}

	private function buildComparison(): callable
	{
		return function (Filter $filter): Comparison {
			$field = $this->mapFieldValue($filter->field());
			$value = $this->existsHydratorFor($field)
				? $this->hydrate($field, $filter->value()->value())
				: $filter->value()->value();

			return new Comparison($field, $filter->operator()->value, $value);
		};
	}

	private function mapFieldValue(FilterField $field): mixed
	{
		return array_key_exists($field->value(), $this->criteriaToDoctrineFields)
			? $this->criteriaToDoctrineFields[$field->value()]
			: $field->value();
	}

	private function formatOrder(Criteria $criteria): ?array
	{
		if (!$criteria->hasOrder()) {
			return null;
		}

		return [$this->mapOrderBy($criteria->order()->orderBy()) => $criteria->order()->orderType()];
	}

	private function mapOrderBy(OrderBy $field): mixed
	{
		return array_key_exists($field->value(), $this->criteriaToDoctrineFields)
			? $this->criteriaToDoctrineFields[$field->value()]
			: $field->value();
	}

	private function existsHydratorFor(mixed $field): bool
	{
		return array_key_exists($field, $this->hydrators);
	}

	private function hydrate(mixed $field, string $value): mixed
	{
		return $this->hydrators[$field]($value);
	}
}
```

## File: `src/Shared/Infrastructure/Persistence/Doctrine/DoctrineRepository.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Shared\Infrastructure\Persistence\Doctrine;

use CodelyTv\Shared\Domain\Aggregate\AggregateRoot;
use Doctrine\ORM\EntityManager;
use Doctrine\ORM\EntityRepository;
use Doctrine\ORM\Exception\NotSupported;

abstract class DoctrineRepository
{
	public function __construct(private readonly EntityManager $entityManager) {}

	protected function entityManager(): EntityManager
	{
		return $this->entityManager;
	}

	protected function persist(AggregateRoot $entity): void
	{
		$this->entityManager()->persist($entity);
		$this->entityManager()->flush($entity);
	}

	protected function remove(AggregateRoot $entity): void
	{
		$this->entityManager()->remove($entity);
		$this->entityManager()->flush($entity);
	}

	/**
	 * @template T of object
	 *
	 * @psalm-param class-string<T> $entityClass
	 *
	 * @psalm-return EntityRepository<T>
	 *
	 * @throws NotSupported
	 */
	protected function repository(string $entityClass): EntityRepository
	{
		return $this->entityManager->getRepository($entityClass);
	}
}
```

## File: `src/Shared/Infrastructure/Persistence/Doctrine/UuidType.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Shared\Infrastructure\Persistence\Doctrine;

use CodelyTv\Shared\Domain\Utils;
use CodelyTv\Shared\Domain\ValueObject\Uuid;
use CodelyTv\Shared\Infrastructure\Doctrine\Dbal\DoctrineCustomType;
use Doctrine\DBAL\Platforms\AbstractPlatform;
use Doctrine\DBAL\Types\StringType;

use function Lambdish\Phunctional\last;

abstract class UuidType extends StringType implements DoctrineCustomType
{
	abstract protected function typeClassName(): string;

	final public static function customTypeName(): string
	{
		return Utils::toSnakeCase(str_replace('Type', '', (string) last(explode('\\', static::class))));
	}

	final public function getName(): string
	{
		return self::customTypeName();
	}

	final public function convertToPHPValue($value, AbstractPlatform $platform): mixed
	{
		$className = $this->typeClassName();

		return new $className($value);
	}

	final public function convertToDatabaseValue($value, AbstractPlatform $platform): string
	{
		/** @var Uuid $value */
		return $value->value();
	}
}
```

## File: `src/Shared/Infrastructure/Persistence/Elasticsearch/ElasticQueryGenerator.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Shared\Infrastructure\Persistence\Elasticsearch;

use CodelyTv\Shared\Domain\Criteria\Filter;
use CodelyTv\Shared\Domain\Criteria\FilterOperator;

final class ElasticQueryGenerator
{
	private const MUST_TYPE = 'must';
	private const MUST_NOT_TYPE = 'must_not';
	private const TERM_TERM = 'term';
	private const TERM_RANGE = 'range';
	private const TERM_WILDCARD = 'wildcard';

	private static array $mustNotFields = [FilterOperator::NOT_EQUAL, FilterOperator::NOT_CONTAINS];

	public function __invoke(array $query, Filter $filter): array
	{
		$type = $this->typeFor($filter->operator());
		$termLevel = $this->termLevelFor($filter->operator());
		$valueTemplate = $filter->operator()->isContaining() ? '*%s*' : '%s';

		return array_merge_recursive(
			$query,
			[
				$type => [
					$termLevel => [
						$filter->field()->value() => sprintf($valueTemplate, strtolower($filter->value()->value())),
					],
				],
			]
		);
	}

	private function typeFor(FilterOperator $operator): string
	{
		return in_array($operator->value, self::$mustNotFields, true) ? self::MUST_NOT_TYPE : self::MUST_TYPE;
	}

	private function termLevelFor(FilterOperator $operator): string
	{
		return match ($operator) {
			FilterOperator::EQUAL => self::TERM_TERM,
			FilterOperator::NOT_EQUAL => '!=',
			FilterOperator::GT, FilterOperator::LT => self::TERM_RANGE,
			FilterOperator::CONTAINS, FilterOperator::NOT_CONTAINS => self::TERM_WILDCARD,
		};
	}
}
```

## File: `src/Shared/Infrastructure/Persistence/Elasticsearch/ElasticsearchCriteriaConverter.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Shared\Infrastructure\Persistence\Elasticsearch;

use CodelyTv\Shared\Domain\Criteria\Criteria;

use function Lambdish\Phunctional\reduce;

final class ElasticsearchCriteriaConverter
{
	public function convert(Criteria $criteria): array
	{
		return [
			'body' => array_merge(
				['from' => $criteria->offset() ?: 0, 'size' => $criteria->limit() ?: 1000],
				$this->formatQuery($criteria),
				$this->formatSort($criteria)
			),
		];
	}

	private function formatQuery(Criteria $criteria): array
	{
		if ($criteria->hasFilters()) {
			return [
				'query' => [
					'bool' => reduce(new ElasticQueryGenerator(), $criteria->filters(), []),
				],
			];
		}

		return [];
	}

	private function formatSort(Criteria $criteria): array
	{
		if ($criteria->hasOrder()) {
			$order = $criteria->order();

			return [
				'sort' => [
					$order->orderBy()->value() => [
						'order' => $order->orderType()->value,
					],
				],
			];
		}

		return [];
	}
}
```

## File: `src/Shared/Infrastructure/Persistence/Elasticsearch/ElasticsearchRepository.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Shared\Infrastructure\Persistence\Elasticsearch;

use CodelyTv\Shared\Domain\Criteria\Criteria;
use CodelyTv\Shared\Infrastructure\Elasticsearch\ElasticsearchClient;
use Elasticsearch\Common\Exceptions\Missing404Exception;

use function Lambdish\Phunctional\get_in;
use function Lambdish\Phunctional\map;

abstract class ElasticsearchRepository
{
	public function __construct(private readonly ElasticsearchClient $client) {}

	abstract protected function aggregateName(): string;

	final public function searchByCriteria(Criteria $criteria): array
	{
		$converter = new ElasticsearchCriteriaConverter();

		$query = $converter->convert($criteria);

		return $this->searchRawElasticsearchQuery($query);
	}

	protected function persist(string $id, array $plainBody): void
	{
		$this->client->persist($this->aggregateName(), $id, $plainBody);
	}

	protected function searchAllInElastic(): array
	{
		return $this->searchRawElasticsearchQuery([]);
	}

	protected function searchRawElasticsearchQuery(array $params): array
	{
		try {
			$result = $this->client->client()->search(array_merge(['index' => $this->indexName()], $params));

			$hits = (array) get_in(['hits', 'hits'], $result, []);

			return map($this->elasticValuesExtractor(), $hits);
		} catch (Missing404Exception) {
			return [];
		}
	}

	protected function indexName(): string
	{
		return sprintf('%s_%s', $this->client->indexPrefix(), $this->aggregateName());
	}

	private function elasticValuesExtractor(): callable
	{
		return static fn (array $elasticValues): array => $elasticValues['_source'];
	}
}
```

## File: `src/Shared/Infrastructure/Symfony/AddJsonBodyToRequestListener.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Shared\Infrastructure\Symfony;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\HttpKernel\Event\RequestEvent;
use Symfony\Component\HttpKernel\Exception\HttpException;

final class AddJsonBodyToRequestListener
{
	public function onKernelRequest(RequestEvent $event): void
	{
		$request = $event->getRequest();
		$requestContents = $request->getContent();

		if (!empty($requestContents) && $this->containsHeader($request, 'Content-Type', 'application/json')) {
			$jsonData = json_decode($requestContents, true, 512, JSON_THROW_ON_ERROR);
			if (!$jsonData) {
				throw new HttpException(Response::HTTP_BAD_REQUEST, 'Invalid json data');
			}
			$jsonDataLowerCase = [];
			foreach ($jsonData as $key => $value) {
				$jsonDataLowerCase[preg_replace_callback(
					'/_(.)/',
					static fn ($matches): string => strtoupper((string) $matches[1]),
					(string) $key
				)] = $value;
			}
			$request->request->replace($jsonDataLowerCase);
		}
	}

	private function containsHeader(Request $request, string $name, string $value): bool
	{
		return str_starts_with((string) $request->headers->get($name), $value);
	}
}
```

## File: `src/Shared/Infrastructure/Symfony/ApiController.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Shared\Infrastructure\Symfony;

use CodelyTv\Shared\Domain\Bus\Command\Command;
use CodelyTv\Shared\Domain\Bus\Command\CommandBus;
use CodelyTv\Shared\Domain\Bus\Query\Query;
use CodelyTv\Shared\Domain\Bus\Query\QueryBus;
use CodelyTv\Shared\Domain\Bus\Query\Response;

use function Lambdish\Phunctional\each;

abstract class ApiController
{
	public function __construct(
		private readonly QueryBus $queryBus,
		private readonly CommandBus $commandBus,
		ApiExceptionsHttpStatusCodeMapping $exceptionHandler
	) {
		each(
			fn (int $httpCode, string $exceptionClass) => $exceptionHandler->register($exceptionClass, $httpCode),
			$this->exceptions()
		);
	}

	abstract protected function exceptions(): array;

	protected function ask(Query $query): ?Response
	{
		return $this->queryBus->ask($query);
	}

	protected function dispatch(Command $command): void
	{
		$this->commandBus->dispatch($command);
	}
}
```

## File: `src/Shared/Infrastructure/Symfony/ApiExceptionListener.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Shared\Infrastructure\Symfony;

use CodelyTv\Shared\Domain\DomainError;
use CodelyTv\Shared\Domain\Utils;
use ReflectionClass;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\HttpKernel\Event\ExceptionEvent;
use Throwable;

final readonly class ApiExceptionListener
{
	public function __construct(private ApiExceptionsHttpStatusCodeMapping $exceptionHandler) {}

	public function onException(ExceptionEvent $event): void
	{
		$exception = $event->getThrowable();

		$event->setResponse(
			new JsonResponse(
				[
					'code' => $this->exceptionCodeFor($exception),
					'message' => $exception->getMessage(),
				],
				$this->exceptionHandler->statusCodeFor($exception::class)
			)
		);
	}

	private function exceptionCodeFor(Throwable $error): string
	{
		$domainErrorClass = DomainError::class;

		return $error instanceof $domainErrorClass
			? $error->errorCode()
			: Utils::toSnakeCase($this->extractClassName($error));
	}

	private function extractClassName(object $object): string
	{
		$reflect = new ReflectionClass($object);

		return $reflect->getShortName();
	}
}
```

## File: `src/Shared/Infrastructure/Symfony/ApiExceptionsHttpStatusCodeMapping.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Shared\Infrastructure\Symfony;

use InvalidArgumentException;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\HttpKernel\Exception\NotFoundHttpException;

use function Lambdish\Phunctional\get;

final class ApiExceptionsHttpStatusCodeMapping
{
	private const DEFAULT_STATUS_CODE = Response::HTTP_INTERNAL_SERVER_ERROR;
	private array $exceptions = [
		InvalidArgumentException::class => Response::HTTP_BAD_REQUEST,
		NotFoundHttpException::class => Response::HTTP_NOT_FOUND,
	];

	public function register(string $exceptionClass, int $statusCode): void
	{
		$this->exceptions[$exceptionClass] = $statusCode;
	}

	public function statusCodeFor(string $exceptionClass): int
	{
		$statusCode = get($exceptionClass, $this->exceptions, self::DEFAULT_STATUS_CODE);

		if ($statusCode === null) {
			throw new InvalidArgumentException("There are no status code mapping for <$exceptionClass>");
		}

		return $statusCode;
	}
}
```

## File: `src/Shared/Infrastructure/Symfony/BasicHttpAuthMiddleware.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Shared\Infrastructure\Symfony;

use CodelyTv\Backoffice\Auth\Application\Authenticate\AuthenticateUserCommand;
use CodelyTv\Backoffice\Auth\Domain\InvalidAuthCredentials;
use CodelyTv\Backoffice\Auth\Domain\InvalidAuthUsername;
use CodelyTv\Shared\Domain\Bus\Command\CommandBus;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\HttpKernel\Event\RequestEvent;

final readonly class BasicHttpAuthMiddleware
{
	public function __construct(private CommandBus $bus) {}

	public function onKernelRequest(RequestEvent $event): void
	{
		$shouldAuthenticate = $event->getRequest()->attributes->get('auth', false);

		if ($shouldAuthenticate) {
			$user = $event->getRequest()->headers->get('php-auth-user');
			$pass = $event->getRequest()->headers->get('php-auth-pw');

			$this->hasIntroducedCredentials($user)
				? $this->authenticate($user, $pass, $event)
				: $this->askForCredentials($event);
		}
	}

	private function hasIntroducedCredentials(?string $user): bool
	{
		return $user !== null;
	}

	private function authenticate(string $user, string $pass, RequestEvent $event): void
	{
		try {
			$this->bus->dispatch(new AuthenticateUserCommand($user, $pass));

			$this->addUserDataToRequest($user, $event);
		} catch (InvalidAuthCredentials | InvalidAuthUsername) {
			$event->setResponse(new JsonResponse(['error' => 'Invalid credentials'], Response::HTTP_FORBIDDEN));
		}
	}

	private function addUserDataToRequest(string $user, RequestEvent $event): void
	{
		$event->getRequest()->attributes->set('authenticated_username', $user);
	}

	private function askForCredentials(RequestEvent $event): void
	{
		$event->setResponse(
			new Response('', Response::HTTP_UNAUTHORIZED, [
				'WWW-Authenticate' => 'Basic realm="CodelyTV"',
			])
		);
	}
}
```

## File: `src/Shared/Infrastructure/Symfony/FlashSession.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Shared\Infrastructure\Symfony;

use CodelyTv\Shared\Domain\Utils;
use Symfony\Component\HttpFoundation\RequestStack;

final class FlashSession
{
	private static array $flashes = [];

	public function __construct(RequestStack $requestStack)
	{
		self::$flashes = Utils::dot($requestStack->getSession()->getFlashBag()->all());
	}

	public function get(string $key, $default = null)
	{
		if (array_key_exists($key, self::$flashes)) {
			return self::$flashes[$key];
		}

		if (array_key_exists($key . '.0', self::$flashes)) {
			return self::$flashes[$key . '.0'];
		}

		if (array_key_exists($key . '.0.0', self::$flashes)) {
			return self::$flashes[$key . '.0.0'];
		}

		return $default;
	}

	public function has(string $key): bool
	{
		return array_key_exists($key, self::$flashes)
			   || array_key_exists($key . '.0', self::$flashes)
			   || array_key_exists($key . '.0.0', self::$flashes);
	}
}
```

## File: `src/Shared/Infrastructure/Symfony/WebController.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Shared\Infrastructure\Symfony;

use CodelyTv\Shared\Domain\Bus\Command\CommandBus;
use CodelyTv\Shared\Domain\Bus\Query\QueryBus;
use Symfony\Component\HttpFoundation\RedirectResponse;
use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\RequestStack;
use Symfony\Component\HttpFoundation\Response as SymfonyResponse;
use Symfony\Component\Routing\RouterInterface;
use Symfony\Component\Validator\ConstraintViolationListInterface;
use Twig\Environment;

abstract class WebController extends ApiController
{
	public function __construct(
		private readonly Environment $twig,
		private readonly RouterInterface $router,
		private readonly RequestStack $requestStack,
		QueryBus $queryBus,
		CommandBus $commandBus,
		ApiExceptionsHttpStatusCodeMapping $exceptionHandler
	) {
		parent::__construct($queryBus, $commandBus, $exceptionHandler);
	}

	final public function render(string $templatePath, array $arguments = []): SymfonyResponse
	{
		return new SymfonyResponse($this->twig->render($templatePath, $arguments));
	}

	final public function redirect(string $routeName): RedirectResponse
	{
		return new RedirectResponse($this->router->generate($routeName), 302);
	}

	final public function redirectWithMessage(string $routeName, string $message): RedirectResponse
	{
		$this->addFlashFor('message', [$message]);

		return $this->redirect($routeName);
	}

	final public function redirectWithErrors(
		string $routeName,
		ConstraintViolationListInterface $errors,
		Request $request
	): RedirectResponse {
		$this->addFlashFor('errors', $this->formatFlashErrors($errors));
		$this->addFlashFor('inputs', $request->request->all());

		return new RedirectResponse($this->router->generate($routeName), 302);
	}

	private function formatFlashErrors(ConstraintViolationListInterface $violations): array
	{
		$errors = [];
		foreach ($violations as $violation) {
			$errors[str_replace(['[', ']'], ['', ''], $violation->getPropertyPath())] = $violation->getMessage();
		}

		return $errors;
	}

	private function addFlashFor(string $prefix, array $messages): void
	{
		foreach ($messages as $key => $message) {
			$this->requestStack->getSession()->getFlashBag()->set($prefix . '.' . $key, $message);
		}
	}
}
```

## File: `tests/Backoffice/Auth/AuthModuleUnitTestCase.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Tests\Backoffice\Auth;

use CodelyTv\Backoffice\Auth\Domain\AuthRepository;
use CodelyTv\Backoffice\Auth\Domain\AuthUser;
use CodelyTv\Backoffice\Auth\Domain\AuthUsername;
use CodelyTv\Tests\Shared\Infrastructure\PhpUnit\UnitTestCase;
use Mockery\MockInterface;

abstract class AuthModuleUnitTestCase extends UnitTestCase
{
	private AuthRepository | MockInterface | null $repository = null;

	protected function shouldSearch(AuthUsername $username, AuthUser $authUser = null): void
	{
		$this->repository()
			->shouldReceive('search')
			->with($this->similarTo($username))
			->once()
			->andReturn($authUser);
	}

	protected function repository(): AuthRepository | MockInterface
	{
		return $this->repository ??= $this->mock(AuthRepository::class);
	}
}
```

## File: `tests/Backoffice/Auth/Application/Authenticate/AuthenticateUserCommandHandlerTest.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Tests\Backoffice\Auth\Application\Authenticate;

use CodelyTv\Backoffice\Auth\Application\Authenticate\AuthenticateUserCommandHandler;
use CodelyTv\Backoffice\Auth\Application\Authenticate\UserAuthenticator;
use CodelyTv\Backoffice\Auth\Domain\InvalidAuthCredentials;
use CodelyTv\Backoffice\Auth\Domain\InvalidAuthUsername;
use CodelyTv\Tests\Backoffice\Auth\AuthModuleUnitTestCase;
use CodelyTv\Tests\Backoffice\Auth\Domain\AuthUserMother;
use CodelyTv\Tests\Backoffice\Auth\Domain\AuthUsernameMother;

final class AuthenticateUserCommandHandlerTest extends AuthModuleUnitTestCase
{
	private AuthenticateUserCommandHandler | null $handler;

	protected function setUp(): void
	{
		parent::setUp();

		$this->handler = new AuthenticateUserCommandHandler(new UserAuthenticator($this->repository()));
	}

	/** @test */
	public function it_should_authenticate_a_valid_user(): void
	{
		$command = AuthenticateUserCommandMother::create();
		$authUser = AuthUserMother::fromCommand($command);

		$this->shouldSearch($authUser->username(), $authUser);

		$this->dispatch($command, $this->handler);
	}

	/** @test */
	public function it_should_throw_an_exception_when_the_user_does_not_exist(): void
	{
		$this->expectException(InvalidAuthUsername::class);

		$command = AuthenticateUserCommandMother::create();
		$username = AuthUsernameMother::create($command->username());

		$this->shouldSearch($username);

		$this->dispatch($command, $this->handler);
	}

	/** @test */
	public function it_should_throw_an_exception_when_the_password_does_not_math(): void
	{
		$this->expectException(InvalidAuthCredentials::class);

		$command = AuthenticateUserCommandMother::create();
		$authUser = AuthUserMother::create(username: AuthUsernameMother::create($command->username()));

		$this->shouldSearch($authUser->username(), $authUser);

		$this->dispatch($command, $this->handler);
	}
}
```

## File: `tests/Backoffice/Auth/Application/Authenticate/AuthenticateUserCommandMother.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Tests\Backoffice\Auth\Application\Authenticate;

use CodelyTv\Backoffice\Auth\Application\Authenticate\AuthenticateUserCommand;
use CodelyTv\Backoffice\Auth\Domain\AuthPassword;
use CodelyTv\Backoffice\Auth\Domain\AuthUsername;
use CodelyTv\Tests\Backoffice\Auth\Domain\AuthPasswordMother;
use CodelyTv\Tests\Backoffice\Auth\Domain\AuthUsernameMother;

final class AuthenticateUserCommandMother
{
	public static function create(
		?AuthUsername $username = null,
		?AuthPassword $password = null
	): AuthenticateUserCommand {
		return new AuthenticateUserCommand(
			$username?->value() ?? AuthUsernameMother::create()->value(),
			$password?->value() ?? AuthPasswordMother::create()->value()
		);
	}
}
```

## File: `tests/Backoffice/Auth/Domain/AuthPasswordMother.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Tests\Backoffice\Auth\Domain;

use CodelyTv\Backoffice\Auth\Domain\AuthPassword;
use CodelyTv\Tests\Shared\Domain\UuidMother;

final class AuthPasswordMother
{
	public static function create(?string $value = null): AuthPassword
	{
		return new AuthPassword($value ?? UuidMother::create());
	}
}
```

## File: `tests/Backoffice/Auth/Domain/AuthUserMother.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Tests\Backoffice\Auth\Domain;

use CodelyTv\Backoffice\Auth\Application\Authenticate\AuthenticateUserCommand;
use CodelyTv\Backoffice\Auth\Domain\AuthPassword;
use CodelyTv\Backoffice\Auth\Domain\AuthUser;
use CodelyTv\Backoffice\Auth\Domain\AuthUsername;

final class AuthUserMother
{
	public static function create(?AuthUsername $username = null, ?AuthPassword $password = null): AuthUser
	{
		return new AuthUser($username ?? AuthUsernameMother::create(), $password ?? AuthPasswordMother::create());
	}

	public static function fromCommand(AuthenticateUserCommand $command): AuthUser
	{
		return self::create(
			AuthUsernameMother::create($command->username()),
			AuthPasswordMother::create($command->password())
		);
	}
}
```

## File: `tests/Backoffice/Auth/Domain/AuthUsernameMother.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Tests\Backoffice\Auth\Domain;

use CodelyTv\Backoffice\Auth\Domain\AuthUsername;
use CodelyTv\Tests\Shared\Domain\WordMother;

final class AuthUsernameMother
{
	public static function create(?string $value = null): AuthUsername
	{
		return new AuthUsername($value ?? WordMother::create());
	}
}
```

## File: `tests/Backoffice/Courses/BackofficeCoursesModuleInfrastructureTestCase.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Tests\Backoffice\Courses;

use CodelyTv\Backoffice\Courses\Infrastructure\Persistence\ElasticsearchBackofficeCourseRepository;
use CodelyTv\Backoffice\Courses\Infrastructure\Persistence\MySqlBackofficeCourseRepository;
use CodelyTv\Tests\Backoffice\Shared\Infraestructure\PhpUnit\BackofficeContextInfrastructureTestCase;
use Doctrine\ORM\EntityManager;

abstract class BackofficeCoursesModuleInfrastructureTestCase extends BackofficeContextInfrastructureTestCase
{
	protected function mySqlRepository(): MySqlBackofficeCourseRepository
	{
		return new MySqlBackofficeCourseRepository($this->service(EntityManager::class));
	}

	protected function elasticRepository(): ElasticsearchBackofficeCourseRepository
	{
		return $this->service(ElasticsearchBackofficeCourseRepository::class);
	}
}
```

## File: `tests/Backoffice/Courses/Domain/BackofficeCourseCriteriaMother.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Tests\Backoffice\Courses\Domain;

use CodelyTv\Shared\Domain\Criteria\Criteria;
use CodelyTv\Tests\Shared\Domain\Criteria\CriteriaMother;
use CodelyTv\Tests\Shared\Domain\Criteria\FilterMother;
use CodelyTv\Tests\Shared\Domain\Criteria\FiltersMother;

final class BackofficeCourseCriteriaMother
{
	public static function nameContains(string $text): Criteria
	{
		return CriteriaMother::create(
			FiltersMother::createOne(
				FilterMother::fromValues([
					'field' => 'name',
					'operator' => 'CONTAINS',
					'value' => $text,
				])
			)
		);
	}
}
```

## File: `tests/Backoffice/Courses/Domain/BackofficeCourseMother.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Tests\Backoffice\Courses\Domain;

use CodelyTv\Backoffice\Courses\Domain\BackofficeCourse;
use CodelyTv\Tests\Mooc\Courses\Domain\CourseDurationMother;
use CodelyTv\Tests\Mooc\Courses\Domain\CourseIdMother;
use CodelyTv\Tests\Mooc\Courses\Domain\CourseNameMother;

final class BackofficeCourseMother
{
	public static function create(?string $id = null, ?string $name = null, ?string $duration = null): BackofficeCourse
	{
		return new BackofficeCourse(
			$id ?? CourseIdMother::create()->value(),
			$name ?? CourseNameMother::create()->value(),
			$duration ?? CourseDurationMother::create()->value()
		);
	}
}
```

## File: `tests/Backoffice/Courses/Infrastructure/Persistence/ElasticsearchBackofficeCourseRepositoryTest.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Tests\Backoffice\Courses\Infrastructure\Persistence;

use CodelyTv\Tests\Backoffice\Courses\BackofficeCoursesModuleInfrastructureTestCase;
use CodelyTv\Tests\Backoffice\Courses\Domain\BackofficeCourseCriteriaMother;
use CodelyTv\Tests\Backoffice\Courses\Domain\BackofficeCourseMother;
use CodelyTv\Tests\Shared\Domain\Criteria\CriteriaMother;

final class ElasticsearchBackofficeCourseRepositoryTest extends BackofficeCoursesModuleInfrastructureTestCase
{
	/** @test */
	public function it_should_save_a_valid_course(): void
	{
		$this->elasticRepository()->save(BackofficeCourseMother::create());
	}

	/** @test */
	public function it_should_search_all_existing_courses(): void
	{
		$existingCourse = BackofficeCourseMother::create();
		$anotherExistingCourse = BackofficeCourseMother::create();
		$existingCourses = [$existingCourse, $anotherExistingCourse];

		$this->elasticRepository()->save($existingCourse);
		$this->elasticRepository()->save($anotherExistingCourse);

		$this->eventually(fn () => $this->assertSimilar($existingCourses, $this->elasticRepository()->searchAll()));
	}

	/** @test */
	public function it_should_search_all_existing_courses_with_an_empty_criteria(): void
	{
		$existingCourse = BackofficeCourseMother::create();
		$anotherExistingCourse = BackofficeCourseMother::create();
		$existingCourses = [$existingCourse, $anotherExistingCourse];

		$this->elasticRepository()->save($existingCourse);
		$this->elasticRepository()->save($anotherExistingCourse);

		$this->eventually(
			fn () => $this->assertSimilar($existingCourses, $this->elasticRepository()->matching(CriteriaMother::empty()))
		);
	}

	/** @test */
	public function it_should_filter_by_criteria(): void
	{
		$dddInPhpCourse = BackofficeCourseMother::create(name: 'DDD en PHP');
		$dddInJavaCourse = BackofficeCourseMother::create(name: 'DDD en Java');
		$intellijCourse = BackofficeCourseMother::create(name: 'Exprimiendo Intellij');
		$dddCourses = [$dddInPhpCourse, $dddInJavaCourse];

		$nameContainsDddCriteria = BackofficeCourseCriteriaMother::nameContains('DDD');

		$this->elasticRepository()->save($dddInJavaCourse);
		$this->elasticRepository()->save($dddInPhpCourse);
		$this->elasticRepository()->save($intellijCourse);

		$this->eventually(
			fn () => $this->assertSimilar($dddCourses, $this->elasticRepository()->matching($nameContainsDddCriteria))
		);
	}
}
```

## File: `tests/Backoffice/Courses/Infrastructure/Persistence/MySqlBackofficeCourseRepositoryTest.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Tests\Backoffice\Courses\Infrastructure\Persistence;

use CodelyTv\Tests\Backoffice\Courses\BackofficeCoursesModuleInfrastructureTestCase;
use CodelyTv\Tests\Backoffice\Courses\Domain\BackofficeCourseCriteriaMother;
use CodelyTv\Tests\Backoffice\Courses\Domain\BackofficeCourseMother;
use CodelyTv\Tests\Shared\Domain\Criteria\CriteriaMother;

final class MySqlBackofficeCourseRepositoryTest extends BackofficeCoursesModuleInfrastructureTestCase
{
	/** @test */
	public function it_should_save_a_valid_course(): void
	{
		$this->mySqlRepository()->save(BackofficeCourseMother::create());
	}

	/** @test */
	public function it_should_search_all_existing_courses(): void
	{
		$existingCourse = BackofficeCourseMother::create();
		$anotherExistingCourse = BackofficeCourseMother::create();
		$existingCourses = [$existingCourse, $anotherExistingCourse];

		$this->mySqlRepository()->save($existingCourse);
		$this->mySqlRepository()->save($anotherExistingCourse);

		$this->assertSimilar($existingCourses, $this->mySqlRepository()->searchAll());
	}

	/** @test */
	public function it_should_search_all_existing_courses_with_an_empty_criteria(): void
	{
		$existingCourse = BackofficeCourseMother::create();
		$anotherExistingCourse = BackofficeCourseMother::create();
		$existingCourses = [$existingCourse, $anotherExistingCourse];

		$this->mySqlRepository()->save($existingCourse);
		$this->mySqlRepository()->save($anotherExistingCourse);
		$this->clearUnitOfWork();

		$this->assertSimilar($existingCourses, $this->mySqlRepository()->matching(CriteriaMother::empty()));
	}

	/** @test */
	public function it_should_filter_by_criteria(): void
	{
		$dddInPhpCourse = BackofficeCourseMother::create(name: 'DDD en PHP');
		$dddInJavaCourse = BackofficeCourseMother::create(name: 'DDD en Java');
		$intellijCourse = BackofficeCourseMother::create(name: 'Exprimiendo Intellij');
		$dddCourses = [$dddInPhpCourse, $dddInJavaCourse];

		$nameContainsDddCriteria = BackofficeCourseCriteriaMother::nameContains('DDD');

		$this->mySqlRepository()->save($dddInJavaCourse);
		$this->mySqlRepository()->save($dddInPhpCourse);
		$this->mySqlRepository()->save($intellijCourse);
		$this->clearUnitOfWork();

		$this->assertSimilar($dddCourses, $this->mySqlRepository()->matching($nameContainsDddCriteria));
	}
}
```

## File: `tests/Backoffice/Shared/Infraestructure/PhpUnit/BackofficeContextInfrastructureTestCase.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Tests\Backoffice\Shared\Infraestructure\PhpUnit;

use CodelyTv\Apps\Backoffice\Backend\BackofficeBackendKernel;
use CodelyTv\Shared\Infrastructure\Elasticsearch\ElasticsearchClient;
use CodelyTv\Tests\Shared\Infrastructure\PhpUnit\InfrastructureTestCase;
use Doctrine\ORM\EntityManager;

abstract class BackofficeContextInfrastructureTestCase extends InfrastructureTestCase
{
	protected function setUp(): void
	{
		parent::setUp();

		$arranger = new BackofficeEnvironmentArranger(
			$this->service(ElasticsearchClient::class),
			$this->service(EntityManager::class)
		);

		$arranger->arrange();
	}

	protected function kernelClass(): string
	{
		return BackofficeBackendKernel::class;
	}
}
```

## File: `tests/Backoffice/Shared/Infraestructure/PhpUnit/BackofficeEnvironmentArranger.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Tests\Backoffice\Shared\Infraestructure\PhpUnit;

use CodelyTv\Shared\Infrastructure\Elasticsearch\ElasticsearchClient;
use CodelyTv\Tests\Shared\Infrastructure\Arranger\EnvironmentArranger;
use CodelyTv\Tests\Shared\Infrastructure\Doctrine\MySqlDatabaseCleaner;
use CodelyTv\Tests\Shared\Infrastructure\Elastic\ElasticDatabaseCleaner;
use Doctrine\ORM\EntityManager;

use function Lambdish\Phunctional\apply;

final readonly class BackofficeEnvironmentArranger implements EnvironmentArranger
{
	public function __construct(private ElasticsearchClient $elasticsearchClient, private EntityManager $entityManager) {}

	public function arrange(): void
	{
		apply(new ElasticDatabaseCleaner(), [$this->elasticsearchClient]);
		apply(new MySqlDatabaseCleaner(), [$this->entityManager]);
	}

	public function close(): void {}
}
```

## File: `tests/Mooc/MoocArchitectureTest.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Tests\Mooc;

use CodelyTv\Tests\Shared\Infrastructure\ArchitectureTest;
use PHPat\Selector\Selector;
use PHPat\Test\Builder\Rule;
use PHPat\Test\PHPat;

final class MoocArchitectureTest
{
	public function test_mooc_domain_should_only_import_itself_and_shared(): Rule
	{
		return PHPat::rule()
			->classes(Selector::inNamespace('/^CodelyTv\\\\Mooc\\\\.+\\\\Domain/', true))
			->canOnlyDependOn()
			->classes(...array_merge(ArchitectureTest::languageClasses(), [
				// Itself
				Selector::inNamespace('/^CodelyTv\\\\Mooc\\\\.+\\\\Domain/', true),
				// Shared
				Selector::inNamespace('CodelyTv\Shared\Domain'),
			]))
			->because('mooc domain can only import itself and shared domain');
	}

	public function test_mooc_application_should_only_import_itself_and_domain(): Rule
	{
		return PHPat::rule()
			->classes(Selector::inNamespace('/^CodelyTv\\\\Mooc\\\\.+\\\\Application/', true))
			->canOnlyDependOn()
			->classes(...array_merge(ArchitectureTest::languageClasses(), [
				// Itself
				Selector::inNamespace('/^CodelyTv\\\\Mooc\\\\.+\\\\Application/', true),
				Selector::inNamespace('/^CodelyTv\\\\Mooc\\\\.+\\\\Domain/', true),
				// Shared
				Selector::inNamespace('CodelyTv\Shared'),
			]))
			->because('mooc application can only import itself and shared');
	}

	public function test_mooc_infrastructure_should_not_import_other_contexts_beside_shared(): Rule
	{
		return PHPat::rule()
			->classes(Selector::inNamespace('CodelyTv\Mooc'))
			->shouldNotDependOn()
			->classes(Selector::inNamespace('CodelyTv'))
			->excluding(
				// Itself
				Selector::inNamespace('CodelyTv\Mooc'),
				// Shared
				Selector::inNamespace('CodelyTv\Shared'),
			);
	}
}
```

## File: `tests/Mooc/Courses/CoursesModuleInfrastructureTestCase.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Tests\Mooc\Courses;

use CodelyTv\Mooc\Courses\Domain\CourseRepository;
use CodelyTv\Tests\Mooc\Shared\Infrastructure\PhpUnit\MoocContextInfrastructureTestCase;

abstract class CoursesModuleInfrastructureTestCase extends MoocContextInfrastructureTestCase
{
	protected function repository(): CourseRepository
	{
		return $this->service(CourseRepository::class);
	}
}
```

## File: `tests/Mooc/Courses/CoursesModuleUnitTestCase.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Tests\Mooc\Courses;

use CodelyTv\Mooc\Courses\Domain\Course;
use CodelyTv\Mooc\Courses\Domain\CourseRepository;
use CodelyTv\Mooc\Shared\Domain\Courses\CourseId;
use CodelyTv\Tests\Shared\Infrastructure\PhpUnit\UnitTestCase;
use Mockery\MockInterface;

abstract class CoursesModuleUnitTestCase extends UnitTestCase
{
	private CourseRepository | MockInterface | null $repository = null;

	protected function shouldSave(Course $course): void
	{
		$this->repository()
			->shouldReceive('save')
			->with($this->similarTo($course))
			->once()
			->andReturnNull();
	}

	protected function shouldSearch(CourseId $id, ?Course $course): void
	{
		$this->repository()
			->shouldReceive('search')
			->with($this->similarTo($id))
			->once()
			->andReturn($course);
	}

	protected function repository(): CourseRepository | MockInterface
	{
		return $this->repository ??= $this->mock(CourseRepository::class);
	}
}
```

## File: `tests/Mooc/Courses/Application/Create/CreateCourseCommandHandlerTest.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Tests\Mooc\Courses\Application\Create;

use CodelyTv\Mooc\Courses\Application\Create\CourseCreator;
use CodelyTv\Mooc\Courses\Application\Create\CreateCourseCommandHandler;
use CodelyTv\Tests\Mooc\Courses\CoursesModuleUnitTestCase;
use CodelyTv\Tests\Mooc\Courses\Domain\CourseCreatedDomainEventMother;
use CodelyTv\Tests\Mooc\Courses\Domain\CourseMother;

final class CreateCourseCommandHandlerTest extends CoursesModuleUnitTestCase
{
	private CreateCourseCommandHandler | null $handler;

	protected function setUp(): void
	{
		parent::setUp();

		$this->handler = new CreateCourseCommandHandler(new CourseCreator($this->repository(), $this->eventBus()));
	}

	/** @test */
	public function it_should_create_a_valid_course(): void
	{
		$command = CreateCourseCommandMother::create();

		$course = CourseMother::fromRequest($command);
		$domainEvent = CourseCreatedDomainEventMother::fromCourse($course);

		$this->shouldSave($course);
		$this->shouldPublishDomainEvent($domainEvent);

		$this->dispatch($command, $this->handler);
	}
}
```

## File: `tests/Mooc/Courses/Application/Create/CreateCourseCommandMother.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Tests\Mooc\Courses\Application\Create;

use CodelyTv\Mooc\Courses\Application\Create\CreateCourseCommand;
use CodelyTv\Mooc\Courses\Domain\CourseDuration;
use CodelyTv\Mooc\Courses\Domain\CourseName;
use CodelyTv\Mooc\Shared\Domain\Courses\CourseId;
use CodelyTv\Tests\Mooc\Courses\Domain\CourseDurationMother;
use CodelyTv\Tests\Mooc\Courses\Domain\CourseIdMother;
use CodelyTv\Tests\Mooc\Courses\Domain\CourseNameMother;

final class CreateCourseCommandMother
{
	public static function create(
		?CourseId $id = null,
		?CourseName $name = null,
		?CourseDuration $duration = null
	): CreateCourseCommand {
		return new CreateCourseCommand(
			$id?->value() ?? CourseIdMother::create()->value(),
			$name?->value() ?? CourseNameMother::create()->value(),
			$duration?->value() ?? CourseDurationMother::create()->value()
		);
	}
}
```

## File: `tests/Mooc/Courses/Application/Update/CourseRenamerTest.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Tests\Mooc\Courses\Application\Update;

use CodelyTv\Mooc\Courses\Application\Update\CourseRenamer;
use CodelyTv\Mooc\Courses\Domain\CourseNotExist;
use CodelyTv\Tests\Mooc\Courses\CoursesModuleUnitTestCase;
use CodelyTv\Tests\Mooc\Courses\Domain\CourseIdMother;
use CodelyTv\Tests\Mooc\Courses\Domain\CourseMother;
use CodelyTv\Tests\Mooc\Courses\Domain\CourseNameMother;
use CodelyTv\Tests\Shared\Domain\DuplicatorMother;

final class CourseRenamerTest extends CoursesModuleUnitTestCase
{
	private CourseRenamer | null $renamer;

	protected function setUp(): void
	{
		parent::setUp();

		$this->renamer = new CourseRenamer($this->repository(), $this->eventBus());
	}

	/** @test */
	public function it_should_rename_an_existing_course(): void
	{
		$course = CourseMother::create();
		$newName = CourseNameMother::create();
		$renamedCourse = DuplicatorMother::with($course, ['name' => $newName]);

		$this->shouldSearch($course->id(), $course);
		$this->shouldSave($renamedCourse);
		$this->shouldNotPublishDomainEvent();

		$this->renamer->__invoke($course->id(), $newName);
	}

	/** @test */
	public function it_should_throw_an_exception_when_the_course_not_exist(): void
	{
		$this->expectException(CourseNotExist::class);

		$id = CourseIdMother::create();

		$this->shouldSearch($id, null);

		$this->renamer->__invoke($id, CourseNameMother::create());
	}
}
```

## File: `tests/Mooc/Courses/Domain/CourseCreatedDomainEventMother.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Tests\Mooc\Courses\Domain;

use CodelyTv\Mooc\Courses\Domain\Course;
use CodelyTv\Mooc\Courses\Domain\CourseCreatedDomainEvent;
use CodelyTv\Mooc\Courses\Domain\CourseDuration;
use CodelyTv\Mooc\Courses\Domain\CourseName;
use CodelyTv\Mooc\Shared\Domain\Courses\CourseId;

final class CourseCreatedDomainEventMother
{
	public static function create(
		?CourseId $id = null,
		?CourseName $name = null,
		?CourseDuration $duration = null
	): CourseCreatedDomainEvent {
		return new CourseCreatedDomainEvent(
			$id?->value() ?? CourseIdMother::create()->value(),
			$name?->value() ?? CourseNameMother::create()->value(),
			$duration?->value() ?? CourseDurationMother::create()->value()
		);
	}

	public static function fromCourse(Course $course): CourseCreatedDomainEvent
	{
		return self::create($course->id(), $course->name(), $course->duration());
	}
}
```

## File: `tests/Mooc/Courses/Domain/CourseDurationMother.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Tests\Mooc\Courses\Domain;

use CodelyTv\Mooc\Courses\Domain\CourseDuration;
use CodelyTv\Tests\Shared\Domain\IntegerMother;
use CodelyTv\Tests\Shared\Domain\RandomElementPicker;

final class CourseDurationMother
{
	public static function create(?string $value = null): CourseDuration
	{
		return new CourseDuration($value ?? self::random());
	}

	private static function random(): string
	{
		return sprintf(
			'%s %s',
			IntegerMother::lessThan(100),
			RandomElementPicker::from('months', 'years', 'days', 'hours', 'minutes', 'seconds')
		);
	}
}
```

## File: `tests/Mooc/Courses/Domain/CourseIdMother.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Tests\Mooc\Courses\Domain;

use CodelyTv\Mooc\Shared\Domain\Courses\CourseId;
use CodelyTv\Tests\Shared\Domain\UuidMother;

final class CourseIdMother
{
	public static function create(?string $value = null): CourseId
	{
		return new CourseId($value ?? UuidMother::create());
	}
}
```

## File: `tests/Mooc/Courses/Domain/CourseMother.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Tests\Mooc\Courses\Domain;

use CodelyTv\Mooc\Courses\Application\Create\CreateCourseCommand;
use CodelyTv\Mooc\Courses\Domain\Course;
use CodelyTv\Mooc\Courses\Domain\CourseDuration;
use CodelyTv\Mooc\Courses\Domain\CourseName;
use CodelyTv\Mooc\Shared\Domain\Courses\CourseId;

final class CourseMother
{
	public static function create(
		?CourseId $id = null,
		?CourseName $name = null,
		?CourseDuration $duration = null
	): Course {
		return new Course(
			$id ?? CourseIdMother::create(),
			$name ?? CourseNameMother::create(),
			$duration ?? CourseDurationMother::create()
		);
	}

	public static function fromRequest(CreateCourseCommand $request): Course
	{
		return self::create(
			CourseIdMother::create($request->id()),
			CourseNameMother::create($request->name()),
			CourseDurationMother::create($request->duration())
		);
	}
}
```

## File: `tests/Mooc/Courses/Domain/CourseNameMother.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Tests\Mooc\Courses\Domain;

use CodelyTv\Mooc\Courses\Domain\CourseName;
use CodelyTv\Tests\Shared\Domain\WordMother;

final class CourseNameMother
{
	public static function create(?string $value = null): CourseName
	{
		return new CourseName($value ?? WordMother::create());
	}
}
```

## File: `tests/Mooc/Courses/Infrastructure/Persistence/CourseRepositoryTest.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Tests\Mooc\Courses\Infrastructure\Persistence;

use CodelyTv\Tests\Mooc\Courses\CoursesModuleInfrastructureTestCase;
use CodelyTv\Tests\Mooc\Courses\Domain\CourseIdMother;
use CodelyTv\Tests\Mooc\Courses\Domain\CourseMother;

final class CourseRepositoryTest extends CoursesModuleInfrastructureTestCase
{
	/** @test */
	public function it_should_save_a_course(): void
	{
		$course = CourseMother::create();

		$this->repository()->save($course);
	}

	/** @test */
	public function it_should_return_an_existing_course(): void
	{
		$course = CourseMother::create();

		$this->repository()->save($course);

		$this->assertEquals($course, $this->repository()->search($course->id()));
	}

	/** @test */
	public function it_should_not_return_a_non_existing_course(): void
	{
		$this->assertNull($this->repository()->search(CourseIdMother::create()));
	}
}
```

## File: `tests/Mooc/CoursesCounter/CoursesCounterModuleUnitTestCase.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Tests\Mooc\CoursesCounter;

use CodelyTv\Mooc\CoursesCounter\Domain\CoursesCounter;
use CodelyTv\Mooc\CoursesCounter\Domain\CoursesCounterRepository;
use CodelyTv\Tests\Shared\Infrastructure\PhpUnit\UnitTestCase;
use Mockery\MockInterface;

abstract class CoursesCounterModuleUnitTestCase extends UnitTestCase
{
	private CoursesCounterRepository | MockInterface | null $repository = null;

	protected function shouldSave(CoursesCounter $course): void
	{
		$this->repository()
			->shouldReceive('save')
			->once()
			->with($this->similarTo($course))
			->andReturnNull();
	}

	protected function shouldSearch(?CoursesCounter $counter): void
	{
		$this->repository()
			->shouldReceive('search')
			->once()
			->andReturn($counter);
	}

	protected function repository(): CoursesCounterRepository | MockInterface
	{
		return $this->repository ??= $this->mock(CoursesCounterRepository::class);
	}
}
```

## File: `tests/Mooc/CoursesCounter/Application/Find/CoursesCounterResponseMother.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Tests\Mooc\CoursesCounter\Application\Find;

use CodelyTv\Mooc\CoursesCounter\Application\Find\CoursesCounterResponse;
use CodelyTv\Mooc\CoursesCounter\Domain\CoursesCounterTotal;
use CodelyTv\Tests\Mooc\CoursesCounter\Domain\CoursesCounterTotalMother;

final class CoursesCounterResponseMother
{
	public static function create(?CoursesCounterTotal $total = null): CoursesCounterResponse
	{
		return new CoursesCounterResponse($total?->value() ?? CoursesCounterTotalMother::create()->value());
	}
}
```

## File: `tests/Mooc/CoursesCounter/Application/Find/FindCoursesCounterQueryHandlerTest.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Tests\Mooc\CoursesCounter\Application\Find;

use CodelyTv\Mooc\CoursesCounter\Application\Find\CoursesCounterFinder;
use CodelyTv\Mooc\CoursesCounter\Application\Find\FindCoursesCounterQuery;
use CodelyTv\Mooc\CoursesCounter\Application\Find\FindCoursesCounterQueryHandler;
use CodelyTv\Mooc\CoursesCounter\Domain\CoursesCounterNotExist;
use CodelyTv\Tests\Mooc\CoursesCounter\CoursesCounterModuleUnitTestCase;
use CodelyTv\Tests\Mooc\CoursesCounter\Domain\CoursesCounterMother;

final class FindCoursesCounterQueryHandlerTest extends CoursesCounterModuleUnitTestCase
{
	private FindCoursesCounterQueryHandler | null $handler;

	protected function setUp(): void
	{
		parent::setUp();

		$this->handler = new FindCoursesCounterQueryHandler(new CoursesCounterFinder($this->repository()));
	}

	/** @test */
	public function it_should_find_an_existing_courses_counter(): void
	{
		$counter = CoursesCounterMother::create();
		$query = new FindCoursesCounterQuery();
		$response = CoursesCounterResponseMother::create($counter->total());

		$this->shouldSearch($counter);

		$this->assertAskResponse($response, $query, $this->handler);
	}

	/** @test */
	public function it_should_throw_an_exception_when_courses_counter_does_not_exists(): void
	{
		$query = new FindCoursesCounterQuery();

		$this->shouldSearch(null);

		$this->assertAskThrowsException(CoursesCounterNotExist::class, $query, $this->handler);
	}
}
```

## File: `tests/Mooc/CoursesCounter/Application/Increment/IncrementCoursesCounterOnCourseCreatedTest.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Tests\Mooc\CoursesCounter\Application\Increment;

use CodelyTv\Mooc\CoursesCounter\Application\Increment\CoursesCounterIncrementer;
use CodelyTv\Mooc\CoursesCounter\Application\Increment\IncrementCoursesCounterOnCourseCreated;
use CodelyTv\Tests\Mooc\Courses\Domain\CourseCreatedDomainEventMother;
use CodelyTv\Tests\Mooc\Courses\Domain\CourseIdMother;
use CodelyTv\Tests\Mooc\CoursesCounter\CoursesCounterModuleUnitTestCase;
use CodelyTv\Tests\Mooc\CoursesCounter\Domain\CoursesCounterIncrementedDomainEventMother;
use CodelyTv\Tests\Mooc\CoursesCounter\Domain\CoursesCounterMother;

final class IncrementCoursesCounterOnCourseCreatedTest extends CoursesCounterModuleUnitTestCase
{
	private IncrementCoursesCounterOnCourseCreated | null $subscriber;

	protected function setUp(): void
	{
		parent::setUp();

		$this->subscriber = new IncrementCoursesCounterOnCourseCreated(
			new CoursesCounterIncrementer($this->repository(), $this->uuidGenerator(), $this->eventBus())
		);
	}

	/** @test */
	public function it_should_initialize_a_new_counter(): void
	{
		$event = CourseCreatedDomainEventMother::create();

		$courseId = CourseIdMother::create($event->aggregateId());
		$newCounter = CoursesCounterMother::withOne($courseId);
		$domainEvent = CoursesCounterIncrementedDomainEventMother::fromCounter($newCounter);

		$this->shouldSearch(null);
		$this->shouldGenerateUuid($newCounter->id()->value());
		$this->shouldSave($newCounter);
		$this->shouldPublishDomainEvent($domainEvent);

		$this->notify($event, $this->subscriber);
	}

	/** @test */
	public function it_should_increment_an_existing_counter(): void
	{
		$event = CourseCreatedDomainEventMother::create();

		$courseId = CourseIdMother::create($event->aggregateId());
		$existingCounter = CoursesCounterMother::create();
		$incrementedCounter = CoursesCounterMother::incrementing($existingCounter, $courseId);
		$domainEvent = CoursesCounterIncrementedDomainEventMother::fromCounter($incrementedCounter);

		$this->shouldSearch($existingCounter);
		$this->shouldSave($incrementedCounter);
		$this->shouldPublishDomainEvent($domainEvent);

		$this->notify($event, $this->subscriber);
	}

	/** @test */
	public function it_should_not_increment_an_already_incremented_course(): void
	{
		$event = CourseCreatedDomainEventMother::create();

		$courseId = CourseIdMother::create($event->aggregateId());
		$existingCounter = CoursesCounterMother::withOne($courseId);

		$this->shouldSearch($existingCounter);

		$this->notify($event, $this->subscriber);
	}
}
```

## File: `tests/Mooc/CoursesCounter/Domain/CoursesCounterIdMother.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Tests\Mooc\CoursesCounter\Domain;

use CodelyTv\Mooc\CoursesCounter\Domain\CoursesCounterId;
use CodelyTv\Tests\Shared\Domain\UuidMother;

final class CoursesCounterIdMother
{
	public static function create(?string $value = null): CoursesCounterId
	{
		return new CoursesCounterId($value ?? UuidMother::create());
	}
}
```

## File: `tests/Mooc/CoursesCounter/Domain/CoursesCounterIncrementedDomainEventMother.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Tests\Mooc\CoursesCounter\Domain;

use CodelyTv\Mooc\CoursesCounter\Domain\CoursesCounter;
use CodelyTv\Mooc\CoursesCounter\Domain\CoursesCounterId;
use CodelyTv\Mooc\CoursesCounter\Domain\CoursesCounterIncrementedDomainEvent;
use CodelyTv\Mooc\CoursesCounter\Domain\CoursesCounterTotal;

final class CoursesCounterIncrementedDomainEventMother
{
	public static function create(
		?CoursesCounterId $id = null,
		?CoursesCounterTotal $total = null
	): CoursesCounterIncrementedDomainEvent {
		return new CoursesCounterIncrementedDomainEvent(
			$id?->value() ?? CoursesCounterIdMother::create()->value(),
			$total?->value() ?? CoursesCounterTotalMother::create()->value()
		);
	}

	public static function fromCounter(CoursesCounter $counter): CoursesCounterIncrementedDomainEvent
	{
		return self::create($counter->id(), $counter->total());
	}
}
```

## File: `tests/Mooc/CoursesCounter/Domain/CoursesCounterMother.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Tests\Mooc\CoursesCounter\Domain;

use CodelyTv\Mooc\CoursesCounter\Domain\CoursesCounter;
use CodelyTv\Mooc\CoursesCounter\Domain\CoursesCounterId;
use CodelyTv\Mooc\CoursesCounter\Domain\CoursesCounterTotal;
use CodelyTv\Mooc\Shared\Domain\Courses\CourseId;
use CodelyTv\Tests\Mooc\Courses\Domain\CourseIdMother;
use CodelyTv\Tests\Shared\Domain\Repeater;

final class CoursesCounterMother
{
	public static function create(
		?CoursesCounterId $id = null,
		?CoursesCounterTotal $total = null,
		CourseId ...$existingCourses
	): CoursesCounter {
		return new CoursesCounter(
			$id ?? CoursesCounterIdMother::create(),
			$total ?? CoursesCounterTotalMother::create(),
			...count($existingCourses) ? $existingCourses : Repeater::random(fn (): CourseId => CourseIdMother::create())
		);
	}

	public static function withOne(CourseId $courseId): CoursesCounter
	{
		return self::create(CoursesCounterIdMother::create(), CoursesCounterTotalMother::one(), $courseId);
	}

	public static function incrementing(CoursesCounter $existingCounter, CourseId $courseId): CoursesCounter
	{
		return self::create(
			$existingCounter->id(),
			CoursesCounterTotalMother::create($existingCounter->total()->value() + 1),
			...array_merge($existingCounter->existingCourses(), [$courseId])
		);
	}
}
```

## File: `tests/Mooc/CoursesCounter/Domain/CoursesCounterTotalMother.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Tests\Mooc\CoursesCounter\Domain;

use CodelyTv\Mooc\CoursesCounter\Domain\CoursesCounterTotal;
use CodelyTv\Tests\Shared\Domain\IntegerMother;

final class CoursesCounterTotalMother
{
	public static function create(?int $value = null): CoursesCounterTotal
	{
		return new CoursesCounterTotal($value ?? IntegerMother::create());
	}

	public static function one(): CoursesCounterTotal
	{
		return self::create(1);
	}

	public static function random(): CoursesCounterTotal
	{
		return self::create(IntegerMother::create());
	}
}
```

## File: `tests/Mooc/Shared/Infrastructure/PhpUnit/MoocContextInfrastructureTestCase.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Tests\Mooc\Shared\Infrastructure\PhpUnit;

use CodelyTv\Apps\Mooc\Backend\MoocBackendKernel;
use CodelyTv\Tests\Shared\Infrastructure\PhpUnit\InfrastructureTestCase;
use Doctrine\ORM\EntityManager;

abstract class MoocContextInfrastructureTestCase extends InfrastructureTestCase
{
	protected function setUp(): void
	{
		parent::setUp();

		$arranger = new MoocEnvironmentArranger($this->service(EntityManager::class));

		$arranger->arrange();
	}

	protected function tearDown(): void
	{
		$arranger = new MoocEnvironmentArranger($this->service(EntityManager::class));

		$arranger->close();

		parent::tearDown();
	}

	protected function kernelClass(): string
	{
		return MoocBackendKernel::class;
	}
}
```

## File: `tests/Mooc/Shared/Infrastructure/PhpUnit/MoocEnvironmentArranger.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Tests\Mooc\Shared\Infrastructure\PhpUnit;

use CodelyTv\Tests\Shared\Infrastructure\Arranger\EnvironmentArranger;
use CodelyTv\Tests\Shared\Infrastructure\Doctrine\MySqlDatabaseCleaner;
use Doctrine\ORM\EntityManager;

use function Lambdish\Phunctional\apply;

final readonly class MoocEnvironmentArranger implements EnvironmentArranger
{
	public function __construct(private EntityManager $entityManager) {}

	public function arrange(): void
	{
		apply(new MySqlDatabaseCleaner(), [$this->entityManager]);
	}

	public function close(): void {}
}
```

## File: `tests/Mooc/Steps/StepsModuleInfrastructureTestCase.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Tests\Mooc\Steps;

use CodelyTv\Mooc\Steps\Domain\StepRepository;
use CodelyTv\Tests\Mooc\Shared\Infrastructure\PhpUnit\MoocContextInfrastructureTestCase;

abstract class StepsModuleInfrastructureTestCase extends MoocContextInfrastructureTestCase
{
	protected function repository(): StepRepository
	{
		return $this->service(StepRepository::class);
	}
}
```

## File: `tests/Mooc/Steps/Domain/StepDurationMother.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Tests\Mooc\Steps\Domain;

use CodelyTv\Mooc\Steps\Domain\StepDuration;
use CodelyTv\Tests\Shared\Domain\IntegerMother;

final class StepDurationMother
{
	public static function create(?int $value = null): StepDuration
	{
		return new StepDuration($value ?? IntegerMother::between(1, 1000));
	}
}
```

## File: `tests/Mooc/Steps/Domain/StepIdMother.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Tests\Mooc\Steps\Domain;

use CodelyTv\Mooc\Steps\Domain\StepId;
use CodelyTv\Tests\Shared\Domain\UuidMother;

final class StepIdMother
{
	public static function create(?string $value = null): StepId
	{
		return new StepId($value ?? UuidMother::create());
	}
}
```

## File: `tests/Mooc/Steps/Domain/StepTitleMother.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Tests\Mooc\Steps\Domain;

use CodelyTv\Mooc\Steps\Domain\StepTitle;
use CodelyTv\Tests\Shared\Domain\WordMother;

final class StepTitleMother
{
	public static function create(?string $value = null): StepTitle
	{
		return new StepTitle($value ?? WordMother::create());
	}
}
```

## File: `tests/Mooc/Steps/Domain/Exercise/ExerciseStepContentMother.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Tests\Mooc\Steps\Domain\Exercise;

use CodelyTv\Mooc\Steps\Domain\Exercise\ExerciseStepContent;
use CodelyTv\Tests\Shared\Domain\WordMother;

final class ExerciseStepContentMother
{
	public static function create(?string $value = null): ExerciseStepContent
	{
		return new ExerciseStepContent($value ?? WordMother::create());
	}
}
```

## File: `tests/Mooc/Steps/Domain/Exercise/ExerciseStepMother.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Tests\Mooc\Steps\Domain\Exercise;

use CodelyTv\Mooc\Steps\Domain\Exercise\ExerciseStep;
use CodelyTv\Mooc\Steps\Domain\Exercise\ExerciseStepContent;
use CodelyTv\Mooc\Steps\Domain\StepDuration;
use CodelyTv\Mooc\Steps\Domain\StepId;
use CodelyTv\Mooc\Steps\Domain\StepTitle;
use CodelyTv\Tests\Mooc\Steps\Domain\StepDurationMother;
use CodelyTv\Tests\Mooc\Steps\Domain\StepIdMother;
use CodelyTv\Tests\Mooc\Steps\Domain\StepTitleMother;

final class ExerciseStepMother
{
	public static function create(
		?StepId $id = null,
		?StepTitle $title = null,
		?StepDuration $duration = null,
		?ExerciseStepContent $content = null
	): ExerciseStep {
		return new ExerciseStep(
			$id ?? StepIdMother::create(),
			$title ?? StepTitleMother::create(),
			$duration ?? StepDurationMother::create(),
			$content ?? ExerciseStepContentMother::create()
		);
	}
}
```

## File: `tests/Mooc/Steps/Domain/Quiz/QuizStepMother.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Tests\Mooc\Steps\Domain\Quiz;

use CodelyTv\Mooc\Steps\Domain\Quiz\QuizStep;
use CodelyTv\Mooc\Steps\Domain\Quiz\QuizStepQuestion;
use CodelyTv\Mooc\Steps\Domain\StepDuration;
use CodelyTv\Mooc\Steps\Domain\StepId;
use CodelyTv\Mooc\Steps\Domain\StepTitle;
use CodelyTv\Tests\Mooc\Steps\Domain\StepDurationMother;
use CodelyTv\Tests\Mooc\Steps\Domain\StepIdMother;
use CodelyTv\Tests\Mooc\Steps\Domain\StepTitleMother;
use CodelyTv\Tests\Shared\Domain\Repeater;

final class QuizStepMother
{
	public static function create(
		?StepId $id = null,
		?StepTitle $title = null,
		?StepDuration $duration = null,
		QuizStepQuestion ...$questions
	): QuizStep {
		$stepQuestions = count($questions) === 0 ? Repeater::random(
			fn (): QuizStepQuestion => QuizStepQuestionMother::create()
		) : $questions;

		return new QuizStep(
			$id ?? StepIdMother::create(),
			$title ?? StepTitleMother::create(),
			$duration ?? StepDurationMother::create(),
			...$stepQuestions
		);
	}
}
```

## File: `tests/Mooc/Steps/Domain/Quiz/QuizStepQuestionMother.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Tests\Mooc\Steps\Domain\Quiz;

use CodelyTv\Mooc\Steps\Domain\Quiz\QuizStepQuestion;
use CodelyTv\Tests\Shared\Domain\Repeater;
use CodelyTv\Tests\Shared\Domain\WordMother;

final class QuizStepQuestionMother
{
	public static function create(?string $question = null, array $answers = []): QuizStepQuestion
	{
		return new QuizStepQuestion(
			$question ?? WordMother::create(),
			count($answers) !== 0 ? $answers : Repeater::random(fn (): string => WordMother::create())
		);
	}
}
```

## File: `tests/Mooc/Steps/Domain/Video/VideoStepMother.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Tests\Mooc\Steps\Domain\Video;

use CodelyTv\Mooc\Steps\Domain\StepDuration;
use CodelyTv\Mooc\Steps\Domain\StepId;
use CodelyTv\Mooc\Steps\Domain\StepTitle;
use CodelyTv\Mooc\Steps\Domain\Video\VideoStep;
use CodelyTv\Mooc\Steps\Domain\Video\VideoStepUrl;
use CodelyTv\Tests\Mooc\Steps\Domain\StepDurationMother;
use CodelyTv\Tests\Mooc\Steps\Domain\StepIdMother;
use CodelyTv\Tests\Mooc\Steps\Domain\StepTitleMother;

final class VideoStepMother
{
	public static function create(
		?StepId $id = null,
		?StepTitle $title = null,
		?StepDuration $duration = null,
		?VideoStepUrl $url = null
	): VideoStep {
		return new VideoStep(
			$id ?? StepIdMother::create(),
			$title ?? StepTitleMother::create(),
			$duration ?? StepDurationMother::create(),
			$url ?? VideoStepUrlMother::create()
		);
	}
}
```

## File: `tests/Mooc/Steps/Domain/Video/VideoStepUrlMother.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Tests\Mooc\Steps\Domain\Video;

use CodelyTv\Mooc\Steps\Domain\Video\VideoStepUrl;
use CodelyTv\Tests\Shared\Domain\WordMother;

final class VideoStepUrlMother
{
	public static function create(?string $value = null): VideoStepUrl
	{
		return new VideoStepUrl($value ?? WordMother::create());
	}
}
```

## File: `tests/Mooc/Steps/Infrastructure/Persistence/MySqlStepRepositoryTest.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Tests\Mooc\Steps\Infrastructure\Persistence;

use CodelyTv\Mooc\Steps\Domain\Step;
use CodelyTv\Tests\Mooc\Steps\Domain\Exercise\ExerciseStepMother;
use CodelyTv\Tests\Mooc\Steps\Domain\Quiz\QuizStepMother;
use CodelyTv\Tests\Mooc\Steps\Domain\Video\VideoStepMother;
use CodelyTv\Tests\Mooc\Steps\StepsModuleInfrastructureTestCase;

final class MySqlStepRepositoryTest extends StepsModuleInfrastructureTestCase
{
	/**
	 * @test
	 * @dataProvider steps
	 */
	public function it_should_save_an_step(Step $step): void
	{
		$this->repository()->save($step);
	}

	/**
	 * @test
	 * @dataProvider steps
	 */
	public function it_should_search_an_existing_step(Step $step): void
	{
		$this->repository()->save($step);

		$this->assertEquals($step, $this->repository()->search($step->id));
	}

	/**
	 * @test
	 * @dataProvider steps
	 */
	public function it_should_delete_an_existing_step(Step $step): void
	{
		$this->repository()->save($step);
		$this->repository()->delete($step);

		$this->assertNull($this->repository()->search($step->id));
	}

	public function steps(): array
	{
		return [
			'video' => [VideoStepMother::create()],
			'exercise' => [ExerciseStepMother::create()],
			'quiz' => [QuizStepMother::create()],
		];
	}
}
```

## File: `tests/Shared/SharedArchitectureTest.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Tests\Shared;

use CodelyTv\Backoffice\Auth\Application\Authenticate\AuthenticateUserCommand;
use CodelyTv\Shared\Domain\Bus\Event\DomainEventSubscriber;
use CodelyTv\Shared\Domain\Bus\Query\Response;
use CodelyTv\Tests\Shared\Infrastructure\ArchitectureTest;
use CodelyTv\Tests\Shared\Infrastructure\Doctrine\MySqlDatabaseCleaner;
use PHPat\Selector\Selector;
use PHPat\Test\Builder\Rule;
use PHPat\Test\PHPat;
use Ramsey\Uuid\Uuid;

final class SharedArchitectureTest
{
	public function test_shared_domain_should_not_import_from_outside(): Rule
	{
		return PHPat::rule()
			->classes(Selector::inNamespace('CodelyTv\Shared\Domain'))
			->canOnlyDependOn()
			->classes(...array_merge(ArchitectureTest::languageClasses(), [
				// Itself
				Selector::inNamespace('CodelyTv\Shared\Domain'),
				// Dependencies treated as domain
				Selector::classname(Uuid::class),
			]))
			->because('shared domain cannot import from outside');
	}

	public function test_shared_infrastructure_should_not_import_from_other_contexts(): Rule
	{
		return PHPat::rule()
			->classes(Selector::inNamespace('CodelyTv\Shared\Infrastructure'))
			->shouldNotDependOn()
			->classes(Selector::inNamespace('CodelyTv'))
			->excluding(
				// Itself
				Selector::inNamespace('CodelyTv\Shared'),
				// This need to be refactored
				Selector::classname(MySqlDatabaseCleaner::class),
				Selector::classname(AuthenticateUserCommand::class),
				Selector::inNamespace('CodelyTv\Backoffice\Auth'),
			);
	}

	public function test_all_use_cases_can_only_have_one_public_method(): Rule
	{
		return PHPat::rule()
			->classes(
				Selector::classname('/^CodelyTv\\\\.+\\\\.+\\\\Application\\\\.+\\\\(?!.*(?:Command|Query)$).*$/', true)
			)
			->excluding(
				Selector::implements(Response::class),
				Selector::implements(DomainEventSubscriber::class),
				Selector::inNamespace('/.*\\\\Tests\\\\.*/', true)
			)
			->shouldHaveOnlyOnePublicMethod();
	}
}
```

## File: `tests/Shared/Domain/DuplicatorMother.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Tests\Shared\Domain;

use ReflectionObject;
use ReflectionProperty;

use function Lambdish\Phunctional\each;

final class DuplicatorMother
{
	public static function with(mixed $object, array $newParams): mixed
	{
		$duplicated = clone $object;
		$reflection = new ReflectionObject($duplicated);

		each(
			static function (ReflectionProperty $property) use ($duplicated, $newParams): void {
				if (isset($newParams[$property->getName()])) {
					$property->setAccessible(true);
					$property->setValue($duplicated, $newParams[$property->getName()]);
				}
			},
			$reflection->getProperties()
		);

		return $duplicated;
	}
}
```

## File: `tests/Shared/Domain/IntegerMother.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Tests\Shared\Domain;

final class IntegerMother
{
	public static function create(): int
	{
		return self::between(1);
	}

	public static function between(int $min, int $max = PHP_INT_MAX): int
	{
		return MotherCreator::random()->numberBetween($min, $max);
	}

	public static function lessThan(int $max): int
	{
		return self::between(1, $max);
	}
}
```

## File: `tests/Shared/Domain/MotherCreator.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Tests\Shared\Domain;

use Faker\Factory;
use Faker\Generator;

final class MotherCreator
{
	private static ?Generator $faker = null;

	public static function random(): Generator
	{
		return self::$faker ??= Factory::create();
	}
}
```

## File: `tests/Shared/Domain/RandomElementPicker.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Tests\Shared\Domain;

final class RandomElementPicker
{
	public static function from(mixed ...$elements): mixed
	{
		return MotherCreator::random()->randomElement($elements);
	}
}
```

## File: `tests/Shared/Domain/Repeater.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Tests\Shared\Domain;

use function Lambdish\Phunctional\repeat;

final class Repeater
{
	public static function repeat(callable $function, int $quantity): array
	{
		return repeat($function, $quantity);
	}

	public static function random(callable $function): array
	{
		return self::repeat($function, IntegerMother::lessThan(5));
	}
}
```

## File: `tests/Shared/Domain/TestUtils.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Tests\Shared\Domain;

use CodelyTv\Tests\Shared\Infrastructure\Mockery\CodelyTvMatcherIsSimilar;
use CodelyTv\Tests\Shared\Infrastructure\PhpUnit\Constraint\CodelyTvConstraintIsSimilar;

final class TestUtils
{
	public static function isSimilar(mixed $expected, mixed $actual): bool
	{
		$constraint = new CodelyTvConstraintIsSimilar($expected);

		return $constraint->evaluate($actual, '', true);
	}

	public static function assertSimilar(mixed $expected, mixed $actual): void
	{
		$constraint = new CodelyTvConstraintIsSimilar($expected);

		$constraint->evaluate($actual);
	}

	public static function similarTo(mixed $value, float $delta = 0.0): CodelyTvMatcherIsSimilar
	{
		return new CodelyTvMatcherIsSimilar($value, $delta);
	}
}
```

## File: `tests/Shared/Domain/UuidMother.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Tests\Shared\Domain;

final class UuidMother
{
	public static function create(): string
	{
		return MotherCreator::random()->unique()->uuid;
	}
}
```

## File: `tests/Shared/Domain/WordMother.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Tests\Shared\Domain;

final class WordMother
{
	public static function create(): string
	{
		return MotherCreator::random()->word;
	}
}
```

## File: `tests/Shared/Domain/Criteria/CriteriaMother.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Tests\Shared\Domain\Criteria;

use CodelyTv\Shared\Domain\Criteria\Criteria;
use CodelyTv\Shared\Domain\Criteria\Filters;
use CodelyTv\Shared\Domain\Criteria\Order;

final class CriteriaMother
{
	public static function create(
		Filters $filters,
		Order $order = null,
		int $offset = null,
		int $limit = null
	): Criteria {
		return new Criteria($filters, $order ?: OrderMother::none(), $offset, $limit);
	}

	public static function empty(): Criteria
	{
		return self::create(FiltersMother::blank(), OrderMother::none());
	}
}
```

## File: `tests/Shared/Domain/Criteria/FilterFieldMother.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Tests\Shared\Domain\Criteria;

use CodelyTv\Shared\Domain\Criteria\FilterField;
use CodelyTv\Tests\Shared\Domain\WordMother;

final class FilterFieldMother
{
	public static function create(?string $fieldName = null): FilterField
	{
		return new FilterField($fieldName ?? WordMother::create());
	}
}
```

## File: `tests/Shared/Domain/Criteria/FilterMother.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Tests\Shared\Domain\Criteria;

use CodelyTv\Shared\Domain\Criteria\Filter;
use CodelyTv\Shared\Domain\Criteria\FilterField;
use CodelyTv\Shared\Domain\Criteria\FilterOperator;
use CodelyTv\Shared\Domain\Criteria\FilterValue;
use CodelyTv\Tests\Shared\Domain\RandomElementPicker;

final class FilterMother
{
	public static function create(
		?FilterField $field = null,
		?FilterOperator $operator = null,
		?FilterValue $value = null
	): Filter {
		return new Filter(
			$field ?? FilterFieldMother::create(),
			$operator ?? self::randomOperator(),
			$value ?? FilterValueMother::create()
		);
	}

	/** @param string[] $values */
	public static function fromValues(array $values): Filter
	{
		return Filter::fromValues($values);
	}


	private static function randomOperator(): FilterOperator
	{
		return RandomElementPicker::from(
			FilterOperator::EQUAL,
			FilterOperator::NOT_EQUAL,
			FilterOperator::GT,
			FilterOperator::LT,
			FilterOperator::CONTAINS,
			FilterOperator::NOT_CONTAINS
		);
	}
}
```

## File: `tests/Shared/Domain/Criteria/FilterValueMother.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Tests\Shared\Domain\Criteria;

use CodelyTv\Shared\Domain\Criteria\FilterValue;
use CodelyTv\Tests\Shared\Domain\WordMother;

final class FilterValueMother
{
	public static function create(?string $value = null): FilterValue
	{
		return new FilterValue($value ?? WordMother::create());
	}
}
```

## File: `tests/Shared/Domain/Criteria/FiltersMother.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Tests\Shared\Domain\Criteria;

use CodelyTv\Shared\Domain\Criteria\Filter;
use CodelyTv\Shared\Domain\Criteria\Filters;

final class FiltersMother
{
	/** @param Filter[] $filters */
	public static function create(array $filters): Filters
	{
		return new Filters($filters);
	}

	public static function createOne(Filter $filter): Filters
	{
		return self::create([$filter]);
	}

	public static function blank(): Filters
	{
		return self::create([]);
	}
}
```

## File: `tests/Shared/Domain/Criteria/OrderByMother.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Tests\Shared\Domain\Criteria;

use CodelyTv\Shared\Domain\Criteria\OrderBy;
use CodelyTv\Tests\Shared\Domain\WordMother;

final class OrderByMother
{
	public static function create(?string $fieldName = null): OrderBy
	{
		return new OrderBy($fieldName ?? WordMother::create());
	}
}
```

## File: `tests/Shared/Domain/Criteria/OrderMother.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Tests\Shared\Domain\Criteria;

use CodelyTv\Shared\Domain\Criteria\Order;
use CodelyTv\Shared\Domain\Criteria\OrderBy;
use CodelyTv\Shared\Domain\Criteria\OrderType;
use CodelyTv\Tests\Shared\Domain\RandomElementPicker;

final class OrderMother
{
	public static function create(?OrderBy $orderBy = null, ?OrderType $orderType = null): Order
	{
		return new Order($orderBy ?? OrderByMother::create(), $orderType ?? self::randomOrderType());
	}

	public static function none(): Order
	{
		return Order::none();
	}

	private static function randomOrderType(): Order
	{
		return RandomElementPicker::from(OrderType::ASC, OrderType::DESC, OrderType::NONE);
	}
}
```

## File: `tests/Shared/Infrastructure/ArchitectureTest.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Tests\Shared\Infrastructure;

use ArrayIterator;
use BackedEnum;
use Countable;
use DateTimeImmutable;
use DateTimeInterface;
use DomainException;
use InvalidArgumentException;
use IteratorAggregate;
use PHPat\Selector\Selector;
use RuntimeException;
use Stringable;
use Throwable;
use Traversable;

final class ArchitectureTest
{
	public static function languageClasses(): array
	{
		return [
			Selector::classname(Throwable::class),
			Selector::classname(InvalidArgumentException::class),
			Selector::classname(RuntimeException::class),
			Selector::classname(DateTimeImmutable::class),
			Selector::classname(DateTimeInterface::class),
			Selector::classname(DomainException::class),
			Selector::classname(Stringable::class),
			Selector::classname(BackedEnum::class),
			Selector::classname(Countable::class),
			Selector::classname(IteratorAggregate::class),
			Selector::classname(Traversable::class),
			Selector::classname(ArrayIterator::class),
		];
	}
}
```

## File: `tests/Shared/Infrastructure/ConstantRandomNumberGenerator.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Tests\Shared\Infrastructure;

use CodelyTv\Shared\Domain\RandomNumberGenerator;

final class ConstantRandomNumberGenerator implements RandomNumberGenerator
{
	public function generate(): int
	{
		return 1;
	}
}
```

## File: `tests/Shared/Infrastructure/Arranger/EnvironmentArranger.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Tests\Shared\Infrastructure\Arranger;

interface EnvironmentArranger
{
	public function arrange(): void;

	public function close(): void;
}
```

## File: `tests/Shared/Infrastructure/Behat/ApiContext.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Tests\Shared\Infrastructure\Behat;

use Behat\Gherkin\Node\PyStringNode;
use Behat\Mink\Session;
use Behat\MinkExtension\Context\RawMinkContext;
use CodelyTv\Tests\Shared\Infrastructure\Mink\MinkHelper;
use CodelyTv\Tests\Shared\Infrastructure\Mink\MinkSessionRequestHelper;
use RuntimeException;

final class ApiContext extends RawMinkContext
{
	private readonly MinkHelper $sessionHelper;
	private readonly MinkSessionRequestHelper $request;

	public function __construct(private readonly Session $minkSession)
	{
		$this->sessionHelper = new MinkHelper($this->minkSession);
		$this->request = new MinkSessionRequestHelper(new MinkHelper($minkSession));
	}

	/**
	 * @Given I send a :method request to :url
	 */
	public function iSendARequestTo(string $method, string $url): void
	{
		$this->request->sendRequest($method, $this->locatePath($url));
	}

	/**
	 * @Given I send a :method request to :url with body:
	 */
	public function iSendARequestToWithBody(string $method, string $url, PyStringNode $body): void
	{
		$this->request->sendRequestWithPyStringNode($method, $this->locatePath($url), $body);
	}

	/**
	 * @Then the response content should be:
	 */
	public function theResponseContentShouldBe(PyStringNode $expectedResponse): void
	{
		$expected = $this->sanitizeOutput($expectedResponse->getRaw());
		$actual = $this->sanitizeOutput($this->sessionHelper->getResponse());

		if ($expected === false || $actual === false) {
			throw new RuntimeException('The outputs could not be parsed as JSON');
		}

		if ($expected !== $actual) {
			throw new RuntimeException(
				sprintf("The outputs does not match!\n\n-- Expected:\n%s\n\n-- Actual:\n%s", $expected, $actual)
			);
		}
	}

	/**
	 * @Then the response should be empty
	 */
	public function theResponseShouldBeEmpty(): void
	{
		$actual = trim($this->sessionHelper->getResponse());

		if (!empty($actual)) {
			throw new RuntimeException(sprintf("The outputs is not empty, Actual:\n%s", $actual));
		}
	}

	/**
	 * @Then print last api response
	 */
	public function printApiResponse(): void
	{
		print_r($this->sessionHelper->getResponse());
	}

	/**
	 * @Then print response headers
	 */
	public function printResponseHeaders(): void
	{
		print_r($this->sessionHelper->getResponseHeaders());
	}

	/**
	 * @Then the response status code should be :expectedResponseCode
	 */
	public function theResponseStatusCodeShouldBe(mixed $expectedResponseCode): void
	{
		if ($this->minkSession->getStatusCode() !== (int) $expectedResponseCode) {
			throw new RuntimeException(
				sprintf(
					'The status code <%s> does not match the expected <%s>',
					$this->minkSession->getStatusCode(),
					$expectedResponseCode
				)
			);
		}
	}

	private function sanitizeOutput(string $output): false | string
	{
		return json_encode(json_decode(trim($output), true, 512, JSON_THROW_ON_ERROR), JSON_THROW_ON_ERROR);
	}
}
```

## File: `tests/Shared/Infrastructure/Behat/ApplicationFeatureContext.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Tests\Shared\Infrastructure\Behat;

use Behat\Behat\Context\Context;
use Behat\Gherkin\Node\PyStringNode;
use CodelyTv\Shared\Infrastructure\Bus\Event\DomainEventJsonDeserializer;
use CodelyTv\Shared\Infrastructure\Bus\Event\InMemory\InMemorySymfonyEventBus;
use CodelyTv\Shared\Infrastructure\Doctrine\DatabaseConnections;

final readonly class ApplicationFeatureContext implements Context
{
	public function __construct(
		private DatabaseConnections $connections,
		private InMemorySymfonyEventBus $bus,
		private DomainEventJsonDeserializer $deserializer
	) {}

	/** @BeforeScenario */
	public function cleanEnvironment(): void
	{
		$this->connections->clear();
		$this->connections->truncate();
	}

	/**
	 * @Given /^I send an event to the event bus:$/
	 */
	public function iSendAnEventToTheEventBus(PyStringNode $event): void
	{
		$domainEvent = $this->deserializer->deserialize($event->getRaw());

		$this->bus->publish($domainEvent);
	}
}
```

## File: `tests/Shared/Infrastructure/Bus/Command/FakeCommand.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Tests\Shared\Infrastructure\Bus\Command;

use CodelyTv\Shared\Domain\Bus\Command\Command;

final class FakeCommand implements Command {}
```

## File: `tests/Shared/Infrastructure/Bus/Command/InMemorySymfonyCommandBusTest.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Tests\Shared\Infrastructure\Bus\Command;

use CodelyTv\Shared\Domain\Bus\Command\Command;
use CodelyTv\Shared\Infrastructure\Bus\Command\CommandNotRegisteredError;
use CodelyTv\Shared\Infrastructure\Bus\Command\InMemorySymfonyCommandBus;
use CodelyTv\Tests\Shared\Infrastructure\PhpUnit\UnitTestCase;
use Mockery\MockInterface;
use RuntimeException;

final class InMemorySymfonyCommandBusTest extends UnitTestCase
{
	private InMemorySymfonyCommandBus | null $commandBus;

	protected function setUp(): void
	{
		parent::setUp();

		$this->commandBus = new InMemorySymfonyCommandBus([$this->commandHandler()]);
	}

	/** @test */
	public function it_should_be_able_to_handle_a_command(): void
	{
		$this->expectException(RuntimeException::class);

		$this->commandBus->dispatch(new FakeCommand());
	}

	/** @test */
	public function it_should_raise_an_exception_dispatching_a_non_registered_command(): void
	{
		$this->expectException(CommandNotRegisteredError::class);

		$this->commandBus->dispatch($this->command());
	}

	private function commandHandler(): object
	{
		return new class() {
			public function __invoke(FakeCommand $command): never
			{
				throw new RuntimeException('This works fine!');
			}
		};
	}

	private function command(): Command | MockInterface
	{
		return $this->mock(Command::class);
	}
}
```

## File: `tests/Shared/Infrastructure/Bus/Event/MySql/MySqlDoctrineEventBusTest.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Tests\Shared\Infrastructure\Bus\Event\MySql;

use CodelyTv\Apps\Mooc\Backend\MoocBackendKernel;
use CodelyTv\Shared\Domain\Bus\Event\DomainEvent;
use CodelyTv\Shared\Infrastructure\Bus\Event\DomainEventMapping;
use CodelyTv\Shared\Infrastructure\Bus\Event\MySql\MySqlDoctrineDomainEventsConsumer;
use CodelyTv\Shared\Infrastructure\Bus\Event\MySql\MySqlDoctrineEventBus;
use CodelyTv\Tests\Mooc\Courses\Domain\CourseCreatedDomainEventMother;
use CodelyTv\Tests\Mooc\CoursesCounter\Domain\CoursesCounterIncrementedDomainEventMother;
use CodelyTv\Tests\Shared\Infrastructure\PhpUnit\InfrastructureTestCase;
use Doctrine\ORM\EntityManager;

final class MySqlDoctrineEventBusTest extends InfrastructureTestCase
{
	private MySqlDoctrineEventBus | null $bus;
	private MySqlDoctrineDomainEventsConsumer | null $consumer;

	protected function setUp(): void
	{
		parent::setUp();

		$this->bus = new MySqlDoctrineEventBus($this->service(EntityManager::class));
		$this->consumer = new MySqlDoctrineDomainEventsConsumer(
			$this->service(EntityManager::class),
			$this->service(DomainEventMapping::class)
		);
	}

	/** @test */
	public function it_should_publish_and_consume_domain_events_from_msql(): void
	{
		$domainEvent = CourseCreatedDomainEventMother::create();
		$anotherDomainEvent = CoursesCounterIncrementedDomainEventMother::create();

		$this->bus->publish($domainEvent, $anotherDomainEvent);

		$this->consumer->consume(
			subscribers: fn (DomainEvent ...$expectedEvents) => $this->assertContainsEquals($domainEvent, $expectedEvents),
			eventsToConsume: 2
		);
	}

	protected function kernelClass(): string
	{
		return MoocBackendKernel::class;
	}
}
```

## File: `tests/Shared/Infrastructure/Bus/Event/RabbitMq/RabbitMqEventBusTest.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Tests\Shared\Infrastructure\Bus\Event\RabbitMq;

use CodelyTv\Apps\Mooc\Backend\MoocBackendKernel;
use CodelyTv\Shared\Domain\Bus\Event\DomainEvent;
use CodelyTv\Shared\Infrastructure\Bus\Event\DomainEventJsonDeserializer;
use CodelyTv\Shared\Infrastructure\Bus\Event\MySql\MySqlDoctrineEventBus;
use CodelyTv\Shared\Infrastructure\Bus\Event\RabbitMq\RabbitMqConfigurer;
use CodelyTv\Shared\Infrastructure\Bus\Event\RabbitMq\RabbitMqConnection;
use CodelyTv\Shared\Infrastructure\Bus\Event\RabbitMq\RabbitMqDomainEventsConsumer;
use CodelyTv\Shared\Infrastructure\Bus\Event\RabbitMq\RabbitMqEventBus;
use CodelyTv\Shared\Infrastructure\Bus\Event\RabbitMq\RabbitMqQueueNameFormatter;
use CodelyTv\Tests\Mooc\Courses\Domain\CourseCreatedDomainEventMother;
use CodelyTv\Tests\Mooc\CoursesCounter\Domain\CoursesCounterIncrementedDomainEventMother;
use CodelyTv\Tests\Shared\Infrastructure\PhpUnit\InfrastructureTestCase;
use RuntimeException;
use Throwable;

final class RabbitMqEventBusTest extends InfrastructureTestCase
{
	private mixed $connection;
	private string $exchangeName;
	private RabbitMqConfigurer $configurer;
	private RabbitMqEventBus $publisher;
	private RabbitMqDomainEventsConsumer $consumer;
	private TestAllWorksOnRabbitMqEventsPublished $fakeSubscriber;
	private bool $consumerHasBeenExecuted;

	protected function setUp(): void
	{
		parent::setUp();

		$this->connection = $this->service(RabbitMqConnection::class);

		$this->exchangeName = 'test_domain_events';
		$this->configurer = new RabbitMqConfigurer($this->connection);
		$this->publisher = new RabbitMqEventBus(
			$this->connection,
			$this->exchangeName,
			$this->service(MySqlDoctrineEventBus::class)
		);
		$this->consumer = new RabbitMqDomainEventsConsumer(
			$this->connection,
			$this->service(DomainEventJsonDeserializer::class),
			$this->exchangeName,
			$maxRetries = 1
		);
		$this->fakeSubscriber = new TestAllWorksOnRabbitMqEventsPublished();
		$this->consumerHasBeenExecuted = false;

		$this->cleanEnvironment($this->connection);
	}

	/** @test */
	public function it_should_publish_and_consume_domain_events_from_rabbitmq(): void
	{
		$domainEvent = CourseCreatedDomainEventMother::create();

		$this->configurer->configure($this->exchangeName, $this->fakeSubscriber);

		$this->publisher->publish($domainEvent);

		$this->consumer->consume(
			$this->assertConsumer($domainEvent),
			RabbitMqQueueNameFormatter::format($this->fakeSubscriber)
		);

		$this->assertTrue($this->consumerHasBeenExecuted);
	}

	/** @test */
	public function it_should_throw_an_exception_consuming_non_existing_domain_events(): void
	{
		$this->expectException(RuntimeException::class);

		$domainEvent = CoursesCounterIncrementedDomainEventMother::create();

		$this->configurer->configure($this->exchangeName, $this->fakeSubscriber);

		$this->publisher->publish($domainEvent);

		$this->consumer->consume(
			$this->assertConsumer($domainEvent),
			RabbitMqQueueNameFormatter::format($this->fakeSubscriber)
		);

		$this->assertTrue($this->consumerHasBeenExecuted);
	}

	/** @test */
	public function it_should_retry_failed_domain_events(): void
	{
		$domainEvent = CourseCreatedDomainEventMother::create();

		$this->configurer->configure($this->exchangeName, $this->fakeSubscriber);

		$this->publisher->publish($domainEvent);

		$this->simulateErrorConsuming();

		sleep(1);

		$this->consumer->consume(
			$this->assertConsumer($domainEvent),
			RabbitMqQueueNameFormatter::format($this->fakeSubscriber)
		);

		$this->assertTrue($this->consumerHasBeenExecuted);
	}

	/** @test */
	public function it_should_send_events_to_dead_letter_after_retry_failed_domain_events(): void
	{
		$domainEvent = CourseCreatedDomainEventMother::create();

		$this->configurer->configure($this->exchangeName, $this->fakeSubscriber);

		$this->publisher->publish($domainEvent);

		$this->simulateErrorConsuming();

		sleep(1);

		$this->simulateErrorConsuming();

		$this->assertDeadLetterContainsEvent(1);
	}

	protected function kernelClass(): string
	{
		return MoocBackendKernel::class;
	}

	private function assertConsumer(DomainEvent ...$expectedDomainEvents): callable
	{
		return function (DomainEvent $domainEvent) use ($expectedDomainEvents): void {
			$this->assertContainsEquals($domainEvent, $expectedDomainEvents);

			$this->consumerHasBeenExecuted = true;
		};
	}

	private function failingConsumer(): callable
	{
		return static function (DomainEvent $domainEvent): never {
			throw new RuntimeException('To test');
		};
	}

	private function simulateErrorConsuming(): void
	{
		try {
			$this->consumer->consume($this->failingConsumer(), RabbitMqQueueNameFormatter::format($this->fakeSubscriber));
		} catch (Throwable $error) {
			$this->assertInstanceOf(RuntimeException::class, $error);
		}
	}

	private function cleanEnvironment(RabbitMqConnection $connection): void
	{
		$connection->queue(RabbitMqQueueNameFormatter::format($this->fakeSubscriber))->delete();
		$connection->queue(RabbitMqQueueNameFormatter::formatRetry($this->fakeSubscriber))->delete();
		$connection->queue(RabbitMqQueueNameFormatter::formatDeadLetter($this->fakeSubscriber))->delete();
	}

	private function assertDeadLetterContainsEvent(int $expectedNumberOfEvents): void
	{
		$totalEventsInDeadLetter = 0;

		while ($this->connection->queue(RabbitMqQueueNameFormatter::formatDeadLetter($this->fakeSubscriber))->get(
			AMQP_AUTOACK
		)) {
			$totalEventsInDeadLetter++;
		}

		$this->assertSame($expectedNumberOfEvents, $totalEventsInDeadLetter);
	}
}
```

## File: `tests/Shared/Infrastructure/Bus/Event/RabbitMq/TestAllWorksOnRabbitMqEventsPublished.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Tests\Shared\Infrastructure\Bus\Event\RabbitMq;

use CodelyTv\Mooc\Courses\Domain\CourseCreatedDomainEvent;
use CodelyTv\Mooc\CoursesCounter\Domain\CoursesCounterIncrementedDomainEvent;
use CodelyTv\Shared\Domain\Bus\Event\DomainEventSubscriber;

final class TestAllWorksOnRabbitMqEventsPublished implements DomainEventSubscriber
{
	public static function subscribedTo(): array
	{
		return [CourseCreatedDomainEvent::class, CoursesCounterIncrementedDomainEvent::class, ];
	}

	public function __invoke(CourseCreatedDomainEvent | CoursesCounterIncrementedDomainEvent $event): void {}
}
```

## File: `tests/Shared/Infrastructure/Bus/Query/FakeQuery.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Tests\Shared\Infrastructure\Bus\Query;

use CodelyTv\Shared\Domain\Bus\Query\Query;

final class FakeQuery implements Query {}
```

## File: `tests/Shared/Infrastructure/Bus/Query/FakeResponse.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Tests\Shared\Infrastructure\Bus\Query;

use CodelyTv\Shared\Domain\Bus\Query\Response;

final readonly class FakeResponse implements Response
{
	public function __construct(private int $number) {}

	public function number(): int
	{
		return $this->number;
	}
}
```

## File: `tests/Shared/Infrastructure/Bus/Query/InMemorySymfonyQueryBusTest.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Tests\Shared\Infrastructure\Bus\Query;

use CodelyTv\Shared\Domain\Bus\Query\Query;
use CodelyTv\Shared\Infrastructure\Bus\Query\InMemorySymfonyQueryBus;
use CodelyTv\Shared\Infrastructure\Bus\Query\QueryNotRegisteredError;
use CodelyTv\Tests\Shared\Infrastructure\PhpUnit\UnitTestCase;
use Mockery\MockInterface;
use RuntimeException;

final class InMemorySymfonyQueryBusTest extends UnitTestCase
{
	private InMemorySymfonyQueryBus | null $queryBus;

	protected function setUp(): void
	{
		parent::setUp();

		$this->queryBus = new InMemorySymfonyQueryBus([$this->queryHandler()]);
	}

	/** @test */
	public function it_should_return_a_response_successfully(): void
	{
		$this->expectException(RuntimeException::class);

		$this->queryBus->ask(new FakeQuery());
	}

	/** @test */
	public function it_should_raise_an_exception_dispatching_a_non_registered_query(): void
	{
		$this->expectException(QueryNotRegisteredError::class);

		$this->queryBus->ask($this->query());
	}

	private function queryHandler(): object
	{
		return new class() {
			public function __invoke(FakeQuery $query): never
			{
				throw new RuntimeException('This works fine!');
			}
		};
	}

	private function query(): MockInterface | Query
	{
		return $this->mock(Query::class);
	}
}
```

## File: `tests/Shared/Infrastructure/Doctrine/MySqlDatabaseCleaner.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Tests\Shared\Infrastructure\Doctrine;

use Doctrine\DBAL\Connection;
use Doctrine\ORM\EntityManagerInterface;

use function Lambdish\Phunctional\first;
use function Lambdish\Phunctional\map;

final class MySqlDatabaseCleaner
{
	public function __invoke(EntityManagerInterface $entityManager): void
	{
		$connection = $entityManager->getConnection();

		$tables = $this->tables($connection);
		$truncateTablesSql = $this->truncateDatabaseSql($tables);

		$connection->executeQuery($truncateTablesSql);
	}

	private function truncateDatabaseSql(array $tables): string
	{
		$truncateTables = map($this->truncateTableSql(), $tables);

		return sprintf('SET FOREIGN_KEY_CHECKS = 0; %s SET FOREIGN_KEY_CHECKS = 1;', implode(' ', $truncateTables));
	}

	private function truncateTableSql(): callable
	{
		return fn (array $table): string => sprintf('TRUNCATE TABLE `%s`;', (string) first($table));
	}

	private function tables(Connection $connection): array
	{
		return $connection->executeQuery('SHOW TABLES')->fetchAllAssociative();
	}
}
```

## File: `tests/Shared/Infrastructure/Elastic/ElasticDatabaseCleaner.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Tests\Shared\Infrastructure\Elastic;

use CodelyTv\Shared\Infrastructure\Elasticsearch\ElasticsearchClient;

use function Lambdish\Phunctional\each;

final class ElasticDatabaseCleaner
{
	public function __invoke(ElasticsearchClient $client): void
	{
		$indices = $client->client()->cat()->indices();

		each(
			static function (array $index) use ($client): void {
				$indexName = $index['index'];

				$client->client()->indices()->delete(['index' => $indexName]);
				$client->client()->indices()->create(['index' => $indexName]);
			},
			$indices
		);
	}
}
```

## File: `tests/Shared/Infrastructure/Mink/MinkHelper.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Tests\Shared\Infrastructure\Mink;

use Behat\Mink\Driver\DriverInterface;
use Behat\Mink\Session;
use Symfony\Component\BrowserKit\AbstractBrowser;
use Symfony\Component\DomCrawler\Crawler;

final readonly class MinkHelper
{
	public function __construct(private Session $session) {}

	public function sendRequest(string $method, string $url, array $optionalParams = []): Crawler
	{
		$defaultOptionalParams = [
			'parameters' => [],
			'files' => [],
			'server' => ['HTTP_ACCEPT' => 'application/json', 'CONTENT_TYPE' => 'application/json'],
			'content' => null,
			'changeHistory' => true,
		];

		$optionalParams = array_merge($defaultOptionalParams, $optionalParams);

		$crawler = $this->getClient()->request(
			$method,
			$url,
			$optionalParams['parameters'],
			$optionalParams['files'],
			$optionalParams['server'],
			$optionalParams['content'],
			$optionalParams['changeHistory']
		);

		return $crawler;
	}

	public function getResponse(): string
	{
		return $this->getSession()->getPage()->getContent();
	}

	public function getResponseHeaders(): array
	{
		return $this->normalizeHeaders(array_change_key_case($this->getSession()->getResponseHeaders(), CASE_LOWER));
	}

	public function resetServerParameters(): void
	{
		$this->getClient()->setServerParameters([]);
	}

	public function getRequest(): object
	{
		return $this->getClient()->getRequest();
	}

	private function getSession(): Session
	{
		return $this->session;
	}

	private function getDriver(): DriverInterface
	{
		return $this->getSession()->getDriver();
	}

	private function getClient(): AbstractBrowser
	{
		return $this->getDriver()->getClient();
	}

	private function normalizeHeaders(array $headers): array
	{
		return array_map('implode', array_filter($headers));
	}
}
```

## File: `tests/Shared/Infrastructure/Mink/MinkSessionRequestHelper.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Tests\Shared\Infrastructure\Mink;

use Behat\Gherkin\Node\PyStringNode;
use Symfony\Component\DomCrawler\Crawler;

final readonly class MinkSessionRequestHelper
{
	public function __construct(private MinkHelper $sessionHelper) {}

	public function sendRequest($method, $url, array $optionalParams = []): void
	{
		$this->request($method, $url, $optionalParams);
	}

	public function sendRequestWithPyStringNode($method, $url, PyStringNode $body): void
	{
		$this->request($method, $url, ['content' => $body->getRaw()]);
	}

	public function request(string $method, string $url, array $optionalParams = []): Crawler
	{
		return $this->sessionHelper->sendRequest($method, $url, $optionalParams);
	}
}
```

## File: `tests/Shared/Infrastructure/Mockery/CodelyTvMatcherIsSimilar.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Tests\Shared\Infrastructure\Mockery;

use CodelyTv\Tests\Shared\Infrastructure\PhpUnit\Constraint\CodelyTvConstraintIsSimilar;
use Mockery\Matcher\MatcherInterface;
use Stringable;

final readonly class CodelyTvMatcherIsSimilar implements Stringable, MatcherInterface
{
	private CodelyTvConstraintIsSimilar $constraint;

	public function __construct(mixed $value, float $delta = 0.0)
	{
		$this->constraint = new CodelyTvConstraintIsSimilar($value, $delta);
	}

	public function match(&$actual): bool
	{
		return $this->constraint->evaluate($actual, '', true);
	}

	public function __toString(): string
	{
		return 'Is similar';
	}
}
```

## File: `tests/Shared/Infrastructure/PhpUnit/InfrastructureTestCase.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Tests\Shared\Infrastructure\PhpUnit;

use CodelyTv\Tests\Shared\Domain\TestUtils;
use Doctrine\ORM\EntityManager;
use Symfony\Bundle\FrameworkBundle\Test\KernelTestCase;
use Throwable;

abstract class InfrastructureTestCase extends KernelTestCase
{
	abstract protected function kernelClass(): string;

	protected function setUp(): void
	{
		$_SERVER['KERNEL_CLASS'] = $this->kernelClass();

		self::bootKernel(['environment' => 'test']);

		parent::setUp();
	}

	protected function assertSimilar(mixed $expected, mixed $actual): void
	{
		TestUtils::assertSimilar($expected, $actual);
	}

	protected function service(string $id): mixed
	{
		return self::getContainer()->get($id);
	}

	protected function parameter(string $parameter): mixed
	{
		return self::getContainer()->getParameter($parameter);
	}

	protected function clearUnitOfWork(): void
	{
		$this->service(EntityManager::class)->clear();
	}

	/** @param int<0, max> $timeToWaitOnErrorInSeconds */
	protected function eventually(
		callable $fn,
		int $totalRetries = 3,
		int $timeToWaitOnErrorInSeconds = 1,
		int $attempt = 0
	): void {
		try {
			$fn();
		} catch (Throwable $error) {
			if ($totalRetries === $attempt) {
				throw $error;
			}

			sleep($timeToWaitOnErrorInSeconds);

			$this->eventually($fn, $totalRetries, $timeToWaitOnErrorInSeconds, $attempt + 1);
		}
	}
}
```

## File: `tests/Shared/Infrastructure/PhpUnit/UnitTestCase.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Tests\Shared\Infrastructure\PhpUnit;

use CodelyTv\Shared\Domain\Bus\Command\Command;
use CodelyTv\Shared\Domain\Bus\Event\DomainEvent;
use CodelyTv\Shared\Domain\Bus\Event\EventBus;
use CodelyTv\Shared\Domain\Bus\Query\Query;
use CodelyTv\Shared\Domain\Bus\Query\Response;
use CodelyTv\Shared\Domain\UuidGenerator;
use CodelyTv\Tests\Shared\Domain\TestUtils;
use CodelyTv\Tests\Shared\Infrastructure\Mockery\CodelyTvMatcherIsSimilar;
use Mockery;
use Mockery\Adapter\Phpunit\MockeryTestCase;
use Mockery\MockInterface;
use Throwable;

abstract class UnitTestCase extends MockeryTestCase
{
	private EventBus | MockInterface | null $eventBus = null;
	private MockInterface | UuidGenerator | null $uuidGenerator = null;

	protected function mock(string $className): MockInterface
	{
		return Mockery::mock($className);
	}

	protected function shouldPublishDomainEvent(DomainEvent $domainEvent): void
	{
		$this->eventBus()
			->shouldReceive('publish')
			->with($this->similarTo($domainEvent))
			->andReturnNull();
	}

	protected function shouldNotPublishDomainEvent(): void
	{
		$this->eventBus()
			->shouldReceive('publish')
			->withNoArgs()
			->andReturnNull();
	}

	protected function eventBus(): EventBus | MockInterface
	{
		return $this->eventBus ??= $this->mock(EventBus::class);
	}

	protected function shouldGenerateUuid(string $uuid): void
	{
		$this->uuidGenerator()
			->shouldReceive('generate')
			->once()
			->withNoArgs()
			->andReturn($uuid);
	}

	protected function uuidGenerator(): MockInterface | UuidGenerator
	{
		return $this->uuidGenerator ??= $this->mock(UuidGenerator::class);
	}

	protected function notify(DomainEvent $event, callable $subscriber): void
	{
		$subscriber($event);
	}

	protected function dispatch(Command $command, callable $commandHandler): void
	{
		$commandHandler($command);
	}

	protected function assertAskResponse(Response $expected, Query $query, callable $queryHandler): void
	{
		$actual = $queryHandler($query);

		$this->assertEquals($expected, $actual);
	}

	/** @param class-string<Throwable> $expectedErrorClass */
	protected function assertAskThrowsException(string $expectedErrorClass, Query $query, callable $queryHandler): void
	{
		$this->expectException($expectedErrorClass);

		$queryHandler($query);
	}

	protected function isSimilar(mixed $expected, mixed $actual): bool
	{
		return TestUtils::isSimilar($expected, $actual);
	}

	protected function assertSimilar(mixed $expected, mixed $actual): void
	{
		TestUtils::assertSimilar($expected, $actual);
	}

	protected function similarTo(mixed $value, float $delta = 0.0): CodelyTvMatcherIsSimilar
	{
		return TestUtils::similarTo($value, $delta);
	}
}
```

## File: `tests/Shared/Infrastructure/PhpUnit/Comparator/AggregateRootArraySimilarComparator.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Tests\Shared\Infrastructure\PhpUnit\Comparator;

use CodelyTv\Shared\Domain\Aggregate\AggregateRoot;
use CodelyTv\Tests\Shared\Domain\TestUtils;
use SebastianBergmann\Comparator\Comparator;
use SebastianBergmann\Comparator\ComparisonFailure;

use function Lambdish\Phunctional\all;
use function Lambdish\Phunctional\any;
use function Lambdish\Phunctional\instance_of;

final class AggregateRootArraySimilarComparator extends Comparator
{
	public function accepts($expected, $actual): bool
	{
		return is_array($expected)
			   && is_array($actual)
			   && (all(instance_of(AggregateRoot::class), $expected)
				   && all(instance_of(AggregateRoot::class), $actual));
	}

	public function assertEquals($expected, $actual, $delta = 0.0, $canonicalize = false, $ignoreCase = false): void
	{
		if (!$this->contains($expected, $actual) || count($expected) !== count($actual)) {
			throw new ComparisonFailure(
				$expected,
				$actual,
				$this->exporter->export($expected),
				$this->exporter->export($actual),
				false,
				'Failed asserting the collection of AGs contains all the expected elements.'
			);
		}
	}

	private function contains(array $expectedArray, array $actualArray): bool
	{
		$exists = fn (AggregateRoot $expected): bool => any(
			fn (AggregateRoot $actual): bool => TestUtils::isSimilar($expected, $actual),
			$actualArray
		);

		return all($exists, $expectedArray);
	}
}
```

## File: `tests/Shared/Infrastructure/PhpUnit/Comparator/AggregateRootSimilarComparator.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Tests\Shared\Infrastructure\PhpUnit\Comparator;

use CodelyTv\Shared\Domain\Aggregate\AggregateRoot;
use CodelyTv\Tests\Shared\Domain\TestUtils;
use ReflectionObject;
use SebastianBergmann\Comparator\Comparator;
use SebastianBergmann\Comparator\ComparisonFailure;

final class AggregateRootSimilarComparator extends Comparator
{
	public function accepts($expected, $actual): bool
	{
		$aggregateRootClass = AggregateRoot::class;

		return $expected instanceof $aggregateRootClass && $actual instanceof $aggregateRootClass;
	}

	public function assertEquals($expected, $actual, $delta = 0.0, $canonicalize = false, $ignoreCase = false): void
	{
		$actualEntity = clone $actual;
		$actualEntity->pullDomainEvents();

		if (!$this->aggregateRootsAreSimilar($expected, $actualEntity)) {
			throw new ComparisonFailure(
				$expected,
				$actual,
				$this->exporter->export($expected),
				$this->exporter->export($actual),
				false,
				'Failed asserting the aggregate roots are equal.'
			);
		}
	}

	private function aggregateRootsAreSimilar(AggregateRoot $expected, AggregateRoot $actual): bool
	{
		if (!$this->aggregateRootsAreTheSameClass($expected, $actual)) {
			return false;
		}

		return $this->aggregateRootPropertiesAreSimilar($expected, $actual);
	}

	private function aggregateRootsAreTheSameClass(AggregateRoot $expected, AggregateRoot $actual): bool
	{
		return $expected::class === $actual::class;
	}

	private function aggregateRootPropertiesAreSimilar(AggregateRoot $expected, AggregateRoot $actual): bool
	{
		$expectedReflected = new ReflectionObject($expected);
		$actualReflected = new ReflectionObject($actual);

		foreach ($expectedReflected->getProperties() as $expectedReflectedProperty) {
			$actualReflectedProperty = $actualReflected->getProperty($expectedReflectedProperty->getName());

			$expectedReflectedProperty->setAccessible(true);
			$actualReflectedProperty->setAccessible(true);

			$expectedProperty = $expectedReflectedProperty->getValue($expected);
			$actualProperty = $actualReflectedProperty->getValue($actual);

			if (!TestUtils::isSimilar($expectedProperty, $actualProperty)) {
				return false;
			}
		}

		return true;
	}
}
```

## File: `tests/Shared/Infrastructure/PhpUnit/Comparator/DateTimeSimilarComparator.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Tests\Shared\Infrastructure\PhpUnit\Comparator;

use DateInterval;
use DateTime;
use DateTimeInterface;
use SebastianBergmann\Comparator\ComparisonFailure;
use SebastianBergmann\Comparator\ObjectComparator;

final class DateTimeSimilarComparator extends ObjectComparator
{
	public function accepts($expected, $actual): bool
	{
		return $expected instanceof DateTimeInterface && $actual instanceof DateTimeInterface;
	}

	public function assertEquals(
		$expected,
		$actual,
		$delta = 0.0,
		$canonicalize = false,
		$ignoreCase = false,
		array &$processed = []
	): void {
		$normalizedDelta = $delta === 0.0 ? 10 : $delta;
		$intervalWithDelta = new DateInterval(sprintf('PT%sS', abs($normalizedDelta)));

		$expectedLower = clone $expected;
		$expectedUpper = clone $expected;

		if ($actual < $expectedLower->sub($intervalWithDelta) || $actual > $expectedUpper->add($intervalWithDelta)) {
			throw new ComparisonFailure(
				$expected,
				$actual,
				$this->dateTimeToString($expected),
				$this->dateTimeToString($actual),
				false,
				'Failed asserting that two DateTime objects are equal.'
			);
		}
	}

	protected function dateTimeToString(DateTimeInterface $datetime): string
	{
		return $datetime->format(DateTime::ATOM) ?: 'Invalid DateTime object';
	}
}
```

## File: `tests/Shared/Infrastructure/PhpUnit/Comparator/DateTimeStringSimilarComparator.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Tests\Shared\Infrastructure\PhpUnit\Comparator;

use DateInterval;
use DateTime;
use DateTimeImmutable;
use DateTimeInterface;
use SebastianBergmann\Comparator\ComparisonFailure;
use SebastianBergmann\Comparator\ObjectComparator;
use Throwable;

final class DateTimeStringSimilarComparator extends ObjectComparator
{
	public function accepts($expected, $actual): bool
	{
		return is_string($expected)
			   && is_string($actual)
			   && $this->isValidDateTimeString($expected)
			   && $this->isValidDateTimeString($actual);
	}

	public function assertEquals(
		$expected,
		$actual,
		$delta = 0.0,
		$canonicalize = false,
		$ignoreCase = false,
		array &$processed = []
	): void {
		$expectedDate = new DateTimeImmutable($expected);
		$actualDate = new DateTimeImmutable($actual);

		$normalizedDelta = $delta === 0.0 ? 10 : $delta;
		$intervalWithDelta = new DateInterval(sprintf('PT%sS', abs($normalizedDelta)));

		if ($actualDate < $expectedDate->sub($intervalWithDelta)
			|| $actualDate > $expectedDate->add($intervalWithDelta)) {
			throw new ComparisonFailure(
				$expectedDate,
				$actualDate,
				$this->dateTimeToString($expectedDate),
				$this->dateTimeToString($actualDate),
				false,
				'Failed asserting that two DateTime strings are equal.'
			);
		}
	}

	protected function dateTimeToString(DateTimeInterface $datetime): string
	{
		$string = $datetime->format(DateTime::ATOM);

		return $string ?: 'Invalid DateTime object';
	}

	private function isValidDateTimeString(string $expected): bool
	{
		$isValid = true;

		try {
			new DateTimeImmutable($expected);
		} catch (Throwable) {
			$isValid = false;
		}

		return $isValid;
	}
}
```

## File: `tests/Shared/Infrastructure/PhpUnit/Comparator/DomainEventArraySimilarComparator.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Tests\Shared\Infrastructure\PhpUnit\Comparator;

use CodelyTv\Shared\Domain\Bus\Event\DomainEvent;
use CodelyTv\Tests\Shared\Domain\TestUtils;
use SebastianBergmann\Comparator\Comparator;
use SebastianBergmann\Comparator\ComparisonFailure;

use function Lambdish\Phunctional\all;
use function Lambdish\Phunctional\any;
use function Lambdish\Phunctional\instance_of;

final class DomainEventArraySimilarComparator extends Comparator
{
	public function accepts($expected, $actual): bool
	{
		return is_array($expected)
			   && is_array($actual)
			   && (all(instance_of(DomainEvent::class), $expected)
				   && all(instance_of(DomainEvent::class), $actual));
	}

	public function assertEquals($expected, $actual, $delta = 0.0, $canonicalize = false, $ignoreCase = false): void
	{
		if (!$this->contains($expected, $actual) || count($expected) !== count($actual)) {
			throw new ComparisonFailure(
				$expected,
				$actual,
				$this->exporter->export($expected),
				$this->exporter->export($actual),
				false,
				'Failed asserting the collection of Events contains all the expected elements.'
			);
		}
	}

	private function contains(array $expectedArray, array $actualArray): bool
	{
		$exists = static fn (DomainEvent $expected): bool => any(
			static fn (DomainEvent $actual): bool => TestUtils::isSimilar($expected, $actual),
			$actualArray
		);

		return all($exists, $expectedArray);
	}
}
```

## File: `tests/Shared/Infrastructure/PhpUnit/Comparator/DomainEventSimilarComparator.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Tests\Shared\Infrastructure\PhpUnit\Comparator;

use CodelyTv\Shared\Domain\Bus\Event\DomainEvent;
use CodelyTv\Tests\Shared\Domain\TestUtils;
use ReflectionObject;
use SebastianBergmann\Comparator\Comparator;
use SebastianBergmann\Comparator\ComparisonFailure;

final class DomainEventSimilarComparator extends Comparator
{
	private static array $ignoredAttributes = ['eventId', 'occurredOn'];

	public function accepts($expected, $actual): bool
	{
		$domainEventRootClass = DomainEvent::class;

		return $expected instanceof $domainEventRootClass && $actual instanceof $domainEventRootClass;
	}

	public function assertEquals($expected, $actual, $delta = 0.0, $canonicalize = false, $ignoreCase = false): void
	{
		if (!$this->areSimilar($expected, $actual)) {
			throw new ComparisonFailure(
				$expected,
				$actual,
				$this->exporter->export($expected),
				$this->exporter->export($actual),
				false,
				'Failed asserting the events are equal.'
			);
		}
	}

	private function areSimilar(DomainEvent $expected, DomainEvent $actual): bool
	{
		if (!$this->areTheSameClass($expected, $actual)) {
			return false;
		}

		return $this->propertiesAreSimilar($expected, $actual);
	}

	private function areTheSameClass(DomainEvent $expected, DomainEvent $actual): bool
	{
		return $expected::class === $actual::class;
	}

	private function propertiesAreSimilar(DomainEvent $expected, DomainEvent $actual): bool
	{
		$expectedReflected = new ReflectionObject($expected);
		$actualReflected = new ReflectionObject($actual);

		foreach ($expectedReflected->getProperties() as $expectedReflectedProperty) {
			if (!in_array($expectedReflectedProperty->getName(), self::$ignoredAttributes, false)) {
				$actualReflectedProperty = $actualReflected->getProperty($expectedReflectedProperty->getName());

				$expectedReflectedProperty->setAccessible(true);
				$actualReflectedProperty->setAccessible(true);

				$expectedProperty = $expectedReflectedProperty->getValue($expected);
				$actualProperty = $actualReflectedProperty->getValue($actual);

				if (!TestUtils::isSimilar($expectedProperty, $actualProperty)) {
					return false;
				}
			}
		}

		return true;
	}
}
```

## File: `tests/Shared/Infrastructure/PhpUnit/Constraint/CodelyTvConstraintIsSimilar.php`
```php
<?php

declare(strict_types=1);

namespace CodelyTv\Tests\Shared\Infrastructure\PhpUnit\Constraint;

use CodelyTv\Tests\Shared\Infrastructure\PhpUnit\Comparator\AggregateRootArraySimilarComparator;
use CodelyTv\Tests\Shared\Infrastructure\PhpUnit\Comparator\AggregateRootSimilarComparator;
use CodelyTv\Tests\Shared\Infrastructure\PhpUnit\Comparator\DateTimeSimilarComparator;
use CodelyTv\Tests\Shared\Infrastructure\PhpUnit\Comparator\DateTimeStringSimilarComparator;
use CodelyTv\Tests\Shared\Infrastructure\PhpUnit\Comparator\DomainEventArraySimilarComparator;
use CodelyTv\Tests\Shared\Infrastructure\PhpUnit\Comparator\DomainEventSimilarComparator;
use PHPUnit\Framework\Constraint\Constraint;
use PHPUnit\Framework\ExpectationFailedException;
use SebastianBergmann\Comparator\ComparisonFailure;
use SebastianBergmann\Comparator\Factory;

use function is_string;
use function sprintf;

// Based on \PHPUnit\Framework\Constraint\IsEqual
final class CodelyTvConstraintIsSimilar extends Constraint
{
	public function __construct(private $value, private readonly float $delta = 0.0) {}

	public function evaluate($other, $description = '', $returnResult = false): bool
	{
		if ($this->value === $other) {
			return true;
		}

		$isValid = true;
		$comparatorFactory = new Factory();

		$comparatorFactory->register(new AggregateRootArraySimilarComparator());
		$comparatorFactory->register(new AggregateRootSimilarComparator());
		$comparatorFactory->register(new DomainEventArraySimilarComparator());
		$comparatorFactory->register(new DomainEventSimilarComparator());
		$comparatorFactory->register(new DateTimeSimilarComparator());
		$comparatorFactory->register(new DateTimeStringSimilarComparator());

		try {
			$comparator = $comparatorFactory->getComparatorFor($other, $this->value);

			$comparator->assertEquals($this->value, $other, $this->delta);
		} catch (ComparisonFailure $f) {
			if (!$returnResult) {
				throw new ExpectationFailedException(trim($description . "\n" . $f->getMessage()), $f);
			}

			$isValid = false;
		}

		return $isValid;
	}

	public function toString(): string
	{
		$delta = '';

		if (is_string($this->value)) {
			if (str_contains($this->value, "\n")) {
				return 'is equal to <text>';
			}

			return sprintf("is equal to '%s'", $this->value);
		}

		if ($this->delta !== 0) {
			$delta = sprintf(' with delta <%F>', $this->delta);
		}

		return sprintf('is equal to %s%s', $this->exporter()->export($this->value), $delta);
	}
}
```


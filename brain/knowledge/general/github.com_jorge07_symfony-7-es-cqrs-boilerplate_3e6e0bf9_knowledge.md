---
id: github.com-jorge07-symfony-7-es-cqrs-boilerplate-3
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:20:16.539050
---

# KNOWLEDGE EXTRACT: github.com_jorge07_symfony-7-es-cqrs-boilerplate_3e6e0bf9
> **Extracted on:** 2026-04-01 16:43:57
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007525262/github.com_jorge07_symfony-7-es-cqrs-boilerplate_3e6e0bf9

---

## File: `.all-contributorsrc`
```
{
  "files": [
    "README.md"
  ],
  "imageSize": 100,
  "commit": false,
  "contributors": [
    {
      "login": "Lutacon",
      "name": "Luis",
      "avatar_url": "https://avatars2.githubusercontent.com/u/2017676?v=4",
      "profile": "http://tacon.eu",
      "contributions": [
        "code"
      ]
    },
    {
      "login": "cv65kr",
      "name": "Kajetan",
      "avatar_url": "https://avatars0.githubusercontent.com/u/9404962?v=4",
      "profile": "https://github.com/cv65kr",
      "contributions": [
        "code"
      ]
    },
    {
      "login": "kowalk",
      "name": "Krzysztof Kowalski",
      "avatar_url": "https://avatars0.githubusercontent.com/u/2781079?v=4",
      "profile": "https://coderslab.pl",
      "contributions": [
        "code"
      ]
    },
    {
      "login": "patrykwozinski",
      "name": "Patryk Woziński",
      "avatar_url": "https://avatars3.githubusercontent.com/u/17459288?v=4",
      "profile": "http://patryk.it",
      "contributions": [
        "code"
      ]
    },
    {
      "login": "jon-ht",
      "name": "jon-ht",
      "avatar_url": "https://avatars3.githubusercontent.com/u/17051512?v=4",
      "profile": "https://github.com/jon-ht",
      "contributions": [
        "code"
      ]
    }
  ],
  "contributorsPerLine": 7,
  "projectName": "symfony-5-es-cqrs-boilerplate",
  "projectOwner": "jorge07",
  "repoType": "github",
  "repoHost": "https://github.com",
  "skipCi": true
}
```

## File: `.coveralls.yml`
```yaml
repo_token: mXFIXUnfdHtX1j3aBrUdU3nBeypTdwzOm
coverage_clover: build/logs/clover.xml
```

## File: `.dockerignore`
```
.git
.github
vendor
node_modules
var
docs-site
doc
.env
.env.local
.env.*.local
tests
e2e
.idea
.vscode
*.md
docker-compose*.yml
etc/*
!etc/artifact/*
```

## File: `.editorconfig`
```
# editorconfig.org

root = true

[*]
charset = utf-8
end_of_line = lf
indent_size = 4
indent_style = space
insert_final_newline = true
trim_trailing_whitespace = true

[{compose.yaml,compose.*.yaml}]
indent_size = 2

[*.md]
trim_trailing_whitespace = false
```

## File: `.env`
```
# This file is a "template" of which env vars need to be defined for your application
# Copy this file to .env file for development, create environment variables when deploying to production
# https://symfony.com/doc/current/best_practices/configuration.html#infrastructure-related-configuration

###> symfony/framework-bundle ###
APP_ENV=dev
APP_DEBUG=1
APP_SECRET=c7375619ac26c8671e52279c31c7f157
#TRUSTED_PROXIES=127.0.0.1,127.0.0.2
#TRUSTED_HOSTS=localhost,example.com
###< symfony/framework-bundle ###
###> lexik/jwt-authentication-bundle ###
JWT_SECRET_KEY=%kernel.project_dir%/config/packages/jwt/private.pem
JWT_PUBLIC_KEY=%kernel.project_dir%/config/packages/jwt/public.pem
JWT_PASSPHRASE=development
JWT_TTL=604800
###< lexik/jwt-authentication-bundle ###

###> symfony/messenger ###
MESSENGER_TRANSPORT_DSN=amqp://guest:guest@rmq:5672
###< symfony/messenger ###
###> doctrine/doctrine-bundle###
DATABASE_HOST=mysql
DATABASE_PORT=3306
DATABASE_NAME=api
DATABASE_USER=root
DATABASE_PASSWORD=api
###< doctrine/doctrine-bundle ###

###> symfony/routing ###
# Configure how to generate URLs in non-HTTP contexts, such as CLI commands.
# See https://symfony.com/doc/current/routing.html#generating-urls-in-commands
DEFAULT_URI=http://localhost
###< symfony/routing ###
```

## File: `.env.dist`
```
# This file is a "template" of which env vars need to be defined for your application
# Copy this file to .env file for development, create environment variables when deploying to production
# https://symfony.com/doc/current/best_practices/configuration.html#infrastructure-related-configuration

###> symfony/framework-bundle ###
APP_ENV=dev
APP_DEBUG=1
APP_SECRET=change_me_in_env_local
#TRUSTED_PROXIES=127.0.0.1,127.0.0.2
#TRUSTED_HOSTS=localhost,example.com
###< symfony/framework-bundle ###
###> lexik/jwt-authentication-bundle ###
JWT_SECRET_KEY=%kernel.project_dir%/config/packages/jwt/private.pem
JWT_PUBLIC_KEY=%kernel.project_dir%/config/packages/jwt/public.pem
JWT_PASSPHRASE=change_me
JWT_TTL=604800
###< lexik/jwt-authentication-bundle ###

###> symfony/messenger ###
MESSENGER_TRANSPORT_DSN=amqp://guest:guest@rmq:5672/%2f/messages
###< symfony/messenger ###
###> doctrine/doctrine-bundle###
DATABASE_HOST=mysql
DATABASE_PORT=3306
DATABASE_NAME=api
DATABASE_USER=root
DATABASE_PASSWORD=change_me
###< doctrine/doctrine-bundle ###
###> symfony/routing ###
# Configure how to generate URLs in non-HTTP contexts, such as CLI commands.
# See https://symfony.com/doc/current/routing.html#generating-urls-in-commands
DEFAULT_URI=http://localhost
###< symfony/routing ###
```

## File: `.env.test`
```
# define your env variables for the test env here
APP_SECRET='$ecretf0rt3st'
SYMFONY_DEPRECATIONS_HELPER=999999
```

## File: `.gitignore`
```
.php-version

###> symfony/framework-bundle ###
/.env.local
/.env.local.php
/.env.*.local
/config/secrets/prod/prod.decrypt.private.php
/public/bundles/
/var/
/vendor/
###< symfony/framework-bundle ###

###> phpstan/phpstan ###
phpstan.neon
###< phpstan/phpstan ###

###> phpunit/phpunit ###
/.phpunit.cache/
/.phpunit.result.cache
/phpunit.xml
###< phpunit/phpunit ###

###> friendsofphp/php-cs-fixer ###
/.php-cs-fixer.php
/.php-cs-fixer.cache
###< friendsofphp/php-cs-fixer ###

###> squizlabs/php_codesniffer ###
/.phpcs-cache
/phpcs.xml
###< squizlabs/php_codesniffer ###

###> lexik/jwt-authentication-bundle ###
/config/jwt/*.pem
###< lexik/jwt-authentication-bundle ###

# IDE
/.idea/

# OS
.DS_Store

# Build
/build/
/report/
.deptrac.cache

# Helm
etc/artifact/chart/charts/
```

## File: `.styleci.yml`
```yaml
preset: symfony

enabled:
- concat_with_spaces
- align_double_arrow

disabled:
- concat_without_spaces
- unalign_double_arrow
```

## File: `LICENSE`
```
MIT License

Copyright (c) 2018 Jorge Arco

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## File: `README.md`
```markdown
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

[Click here for the detailed instructions about how to setup the PHP remote interpreter in PHPStorm.](https://github.com/jorge07/alpine-php/blob/master/doc/IDE.md)

If you're already familiar with it, here a quick configuration reference:

|    Host          	|    Direction  |
|------------------	|--------------	|
|  Docker 4 mac 	   | `localhost`   |
|  Dinghy       	   | `$ dinghy ip` |

**Port:** `2323`

**Filesystem mapping:** `{PROJECT_PATH}` -> `/app`

### Xdebug

To ease your development process, you can use Xdebug with PHPSTORM.

1. Add a Docker interpreter

   ![Docker PHP interpreter](doc/docker-php-interpreter.png)

2. Enable Xdebug listenning. Don't forget to also activate Xdebug helper from your browser.
   
   ![Xdebug activation](doc/xdebug-activation.png)
   
   Additionally, you can check `Break at first line in PHP scripts` to ensure your debug is working.

3. Make a request from you API at http://127.0.0.1/api/doc for example. You should see this popup:

   ![Xdebug mapping](doc/xdebug-mapping.png)
   
   Click on `Accept` and you should be ready to debug ! Start placing breakpoints on your code and enjoy debugging !

> Note for Windows users:
>
> You might need to update `docker-os=` to `docker-os=windows` in [Makefile](makefile)
> or specify its value on command line like `$ make start docker-os=windows`.

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="http://tacon.eu"><img src="https://avatars2.githubusercontent.com/u/2017676?v=4" width="100px;" alt=""/><br /><sub><b>Luis</b></sub></a><br /><a href="https://github.com/jorge07/symfony-6-es-cqrs-boilerplate/commits?author=Lutacon" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/cv65kr"><img src="https://avatars0.githubusercontent.com/u/9404962?v=4" width="100px;" alt=""/><br /><sub><b>Kajetan</b></sub></a><br /><a href="https://github.com/jorge07/symfony-6-es-cqrs-boilerplate/commits?author=cv65kr" title="Code">💻</a></td>
    <td align="center"><a href="https://coderslab.pl"><img src="https://avatars0.githubusercontent.com/u/2781079?v=4" width="100px;" alt=""/><br /><sub><b>Krzysztof Kowalski</b></sub></a><br /><a href="https://github.com/jorge07/symfony-6-es-cqrs-boilerplate/commits?author=kowalk" title="Code">💻</a></td>
    <td align="center"><a href="http://patryk.it"><img src="https://avatars3.githubusercontent.com/u/17459288?v=4" width="100px;" alt=""/><br /><sub><b>Patryk Woziński</b></sub></a><br /><a href="https://github.com/jorge07/symfony-6-es-cqrs-boilerplate/commits?author=patrykwozinski" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/jon-ht"><img src="https://avatars3.githubusercontent.com/u/17051512?v=4" width="100px;" alt=""/><br /><sub><b>jon-ht</b></sub></a><br /><a href="https://github.com/jorge07/symfony-6-es-cqrs-boilerplate/commits?author=jon-ht" title="Code">💻</a></td>
  </tr>
</table>

<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->
<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!
```

## File: `composer.json`
```json
{
    "type": "project",
    "license": "MIT",
    "require": {
        "php": "^8.3",
        "ext-amqp": "*",
        "ext-json": "*",
        "beberlei/assert": "^3.3",
        "broadway/broadway-bundle": "^0.7.0",
        "broadway/event-store-dbal": "^0.6",
        "doctrine/doctrine-bundle": "^2.15",
        "doctrine/doctrine-migrations-bundle": "^3.3",
        "doctrine/instantiator": "^2.0.0 <2.1.0",
        "doctrine/orm": "^3.2",
        "elasticsearch/elasticsearch": "^7.11",
        "lexik/jwt-authentication-bundle": "^3.0",
        "nelmio/api-doc-bundle": "^4.20",
        "ramsey/uuid": "^4.1",
        "ramsey/uuid-doctrine": "^2.0",
        "symfony/amqp-messenger": "^7.0",
        "symfony/asset": "^7.0",
        "symfony/cache": "^7.0",
        "symfony/console": "^7.0",
        "symfony/flex": "^2.4",
        "symfony/framework-bundle": "^7.0",
        "symfony/messenger": "^7.0",
        "symfony/monolog-bundle": "^3.10",
        "symfony/security-bundle": "^7.0",
        "symfony/twig-bundle": "^7.0",
        "symfony/yaml": "^7.0"
    },
    "require-dev": {
        "dama/doctrine-test-bundle": "^8.0",
        "phpstan/phpstan": "^2.0",
        "phpunit/phpunit": "^10.5",
        "rector/rector": "^2.0",
        "roave/security-advisories": "dev-master",
        "sylius-labs/coding-standard": "^v4.2.0",
        "symfony/browser-kit": "^7.0",
        "symfony/css-selector": "^7.0",
        "symfony/dotenv": "^7.0",
        "symfony/phpunit-bridge": "^7.0",
        "symfony/stopwatch": "^7.0",
        "symfony/web-profiler-bundle": "^7.0",
        "vimeo/psalm": "^5.0"
    },
    "config": {
        "preferred-install": {
            "*": "dist"
        },
        "sort-packages": true,
        "allow-plugins": {
            "composer/package-versions-deprecated": true,
            "dealerdirect/phpcodesniffer-composer-installer": true,
            "symfony/flex": true
        }
    },
    "autoload": {
        "psr-4": {
            "App\\": "src/App/",
            "UI\\": "src/UI/"
        }
    },
    "autoload-dev": {
        "psr-4": {
            "Tests\\": "tests/"
        }
    },
    "replace": {
        "symfony/polyfill-iconv": "*"
    },
    "scripts": {
        "auto-scripts": {
            "cache:clear": "symfony-cmd",
            "assets:install %PUBLIC_DIR%": "symfony-cmd"
        },
        "post-install-cmd": [
            "@auto-scripts"
        ],
        "post-update-cmd": [
            "@auto-scripts"
        ]
    },
    "conflict": {
        "symfony/symfony": "*"
    },
    "extra": {
        "symfony": {
            "id": "01C1QKYZ4DSB74RHER7JCF8Q1K",
            "allow-contrib": false,
            "require": "^7.0"
        }
    },
    "name": "jorge07/symfony-5-es-cqrs-boilerplate",
    "description": "Symfony 7 DDD ES CQRS backend boilerplate"
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
    "content-hash": "862a6e0c651a0f39e92eecc8cead04d3",
    "packages": [
        {
            "name": "beberlei/assert",
            "version": "v3.3.3",
            "source": {
                "type": "git",
                "url": "https://github.com/beberlei/assert.git",
                "reference": "b5fd8eacd8915a1b627b8bfc027803f1939734dd"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/beberlei/assert/zipball/b5fd8eacd8915a1b627b8bfc027803f1939734dd",
                "reference": "b5fd8eacd8915a1b627b8bfc027803f1939734dd",
                "shasum": ""
            },
            "require": {
                "ext-ctype": "*",
                "ext-json": "*",
                "ext-mbstring": "*",
                "ext-simplexml": "*",
                "php": "^7.1 || ^8.0"
            },
            "require-dev": {
                "friendsofphp/php-cs-fixer": "*",
                "phpstan/phpstan": "*",
                "phpunit/phpunit": ">=6.0.0",
                "yoast/phpunit-polyfills": "^0.1.0"
            },
            "suggest": {
                "ext-intl": "Needed to allow Assertion::count(), Assertion::isCountable(), Assertion::minCount(), and Assertion::maxCount() to operate on ResourceBundles"
            },
            "type": "library",
            "autoload": {
                "files": [
                    "lib/Assert/functions.php"
                ],
                "psr-4": {
                    "Assert\\": "lib/Assert"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-2-Clause"
            ],
            "authors": [
                {
                    "name": "Benjamin Eberlei",
                    "email": "kontakt@beberlei.de",
                    "role": "Lead Developer"
                },
                {
                    "name": "Richard Quadling",
                    "email": "rquadling@gmail.com",
                    "role": "Collaborator"
                }
            ],
            "description": "Thin assertion library for input validation in business models.",
            "keywords": [
                "assert",
                "assertion",
                "validation"
            ],
            "support": {
                "issues": "https://github.com/beberlei/assert/issues",
                "source": "https://github.com/beberlei/assert/tree/v3.3.3"
            },
            "time": "2024-07-15T13:18:35+00:00"
        },
        {
            "name": "brick/math",
            "version": "0.14.6",
            "source": {
                "type": "git",
                "url": "https://github.com/brick/math.git",
                "reference": "32498d5e1897e7642c0b961ace2df6d7dc9a3bc3"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/brick/math/zipball/32498d5e1897e7642c0b961ace2df6d7dc9a3bc3",
                "reference": "32498d5e1897e7642c0b961ace2df6d7dc9a3bc3",
                "shasum": ""
            },
            "require": {
                "php": "^8.2"
            },
            "require-dev": {
                "php-coveralls/php-coveralls": "^2.2",
                "phpstan/phpstan": "2.1.22",
                "phpunit/phpunit": "^11.5"
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
                "source": "https://github.com/brick/math/tree/0.14.6"
            },
            "funding": [
                {
                    "url": "https://github.com/BenMorel",
                    "type": "github"
                }
            ],
            "time": "2026-02-05T07:59:58+00:00"
        },
        {
            "name": "broadway/broadway",
            "version": "2.5.0",
            "source": {
                "type": "git",
                "url": "https://github.com/broadway/broadway.git",
                "reference": "e99a8981fcfec2169a0e5ca70a8358d59ded68c5"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/broadway/broadway/zipball/e99a8981fcfec2169a0e5ca70a8358d59ded68c5",
                "reference": "e99a8981fcfec2169a0e5ca70a8358d59ded68c5",
                "shasum": ""
            },
            "require": {
                "beberlei/assert": "^3.0",
                "broadway/uuid-generator": "^1.0",
                "php": ">=7.2"
            },
            "require-dev": {
                "broadway/coding-standard": "^1.2",
                "monolog/monolog": "~2.0",
                "phpspec/prophecy": "^1.15",
                "phpstan/phpstan": "^1.0",
                "phpunit/phpunit": "^9.5",
                "psr/log": "^1.1.4",
                "ramsey/uuid": "^4.0"
            },
            "suggest": {
                "broadway/broadway-bundle": "Symfony bundle for broadway/broadway",
                "broadway/broadway-saga": "Saga component for Broadway",
                "broadway/event-store-dbal": "Event store implementation using doctrine/dbal",
                "broadway/read-model-elasticsearch": "Elasticsearch read model implementation",
                "psr/log-implementation": "Implementation for PSR3, LoggerInterface"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "3.0.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Broadway\\": "src/Broadway/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Alexander",
                    "email": "iam.asm89@gmail.com"
                },
                {
                    "name": "Emil",
                    "email": "emil@broekmeulen.com"
                },
                {
                    "name": "Fritsjan",
                    "email": "fritsjan@qandidate.com"
                },
                {
                    "name": "othillo",
                    "email": "othillo@othillo.nl"
                },
                {
                    "name": "Willem-Jan",
                    "email": "wjzijderveld@gmail.com"
                },
                {
                    "name": "Qandidate.com",
                    "homepage": "http://labs.qandidate.com/"
                }
            ],
            "description": "Infrastructure and testing helpers for creating CQRS and event sourced applications.",
            "keywords": [
                "cqrs",
                "ddd",
                "domain-driven design",
                "event sourcing"
            ],
            "support": {
                "issues": "https://github.com/broadway/broadway/issues",
                "source": "https://github.com/broadway/broadway/tree/2.5.0"
            },
            "time": "2023-04-14T17:46:13+00:00"
        },
        {
            "name": "broadway/broadway-bundle",
            "version": "0.7.0",
            "source": {
                "type": "git",
                "url": "https://github.com/broadway/broadway-bundle.git",
                "reference": "a172d195ec05b39eaab27221e46a9a08e0dc447d"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/broadway/broadway-bundle/zipball/a172d195ec05b39eaab27221e46a9a08e0dc447d",
                "reference": "a172d195ec05b39eaab27221e46a9a08e0dc447d",
                "shasum": ""
            },
            "require": {
                "broadway/broadway": "^2.2.1",
                "php": "^7.4 || ^8.0",
                "symfony/console": "^4.4 || ^5.3 || ^6.0 || ^7.0",
                "symfony/http-kernel": "^4.4 || ^5.3 || ^6.0 || ^7.0"
            },
            "require-dev": {
                "broadway/broadway-saga": "^1.0",
                "friendsofphp/php-cs-fixer": "^3.0",
                "matthiasnoback/symfony-config-test": "^4.0 || ^5.0",
                "matthiasnoback/symfony-dependency-injection-test": "^4.0 || ^5.0",
                "monolog/monolog": "~2.0",
                "phpstan/phpstan": "@stable",
                "phpstan/phpstan-symfony": "^1.0",
                "phpunit/phpunit": "^9.5",
                "symfony/framework-bundle": "^4.4 || ^5.3 || ^6.0 || ^7.0",
                "symfony/proxy-manager-bridge": "^4.4 || ^5.3 || ^6.0"
            },
            "suggest": {
                "broadway/event-store-dbal": "Event store implementation using doctrine/dbal",
                "broadway/read-model-elasticsearch": "Elasticsearch read model implementation using elastic/elasticsearch-php",
                "psr/log-implementation": "Implementation for PSR3, LoggerInterface"
            },
            "type": "symfony-bundle",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.0.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Broadway\\Bundle\\BroadwayBundle\\": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Alexander",
                    "email": "iam.asm89@gmail.com"
                },
                {
                    "name": "Emil",
                    "email": "emil@broekmeulen.com"
                },
                {
                    "name": "Fritsjan",
                    "email": "fritsjan@qandidate.com"
                },
                {
                    "name": "othillo",
                    "email": "othillo@othillo.nl"
                },
                {
                    "name": "Willem-Jan",
                    "email": "wjzijderveld@gmail.com"
                },
                {
                    "name": "Qandidate.com",
                    "homepage": "http://labs.qandidate.com/"
                }
            ],
            "description": "Symfony bundle for broadway/broadway.",
            "keywords": [
                "cqrs",
                "ddd",
                "domain-driven design",
                "event sourcing"
            ],
            "support": {
                "issues": "https://github.com/broadway/broadway-bundle/issues",
                "source": "https://github.com/broadway/broadway-bundle/tree/0.7.0"
            },
            "time": "2024-03-28T10:17:47+00:00"
        },
        {
            "name": "broadway/event-store-dbal",
            "version": "0.6.0",
            "source": {
                "type": "git",
                "url": "https://github.com/broadway/event-store-dbal.git",
                "reference": "7cc0b51cdd8312c4f8919d3b2f6688d85b65cc58"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/broadway/event-store-dbal/zipball/7cc0b51cdd8312c4f8919d3b2f6688d85b65cc58",
                "reference": "7cc0b51cdd8312c4f8919d3b2f6688d85b65cc58",
                "shasum": ""
            },
            "require": {
                "broadway/broadway": "^2.3.1",
                "doctrine/dbal": "^3.1",
                "php": ">=7.2"
            },
            "require-dev": {
                "broadway/coding-standard": "^1.2",
                "ext-pdo_sqlite": "*",
                "phpstan/phpstan": "@stable",
                "phpunit/phpunit": "^9.5",
                "ramsey/uuid": "^4.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.0.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Broadway\\EventStore\\Dbal\\": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Alexander",
                    "email": "iam.asm89@gmail.com"
                },
                {
                    "name": "Emil",
                    "email": "emil@broekmeulen.com"
                },
                {
                    "name": "Fritsjan",
                    "email": "fritsjan@qandidate.com"
                },
                {
                    "name": "othillo",
                    "email": "othillo@othillo.nl"
                },
                {
                    "name": "Willem-Jan",
                    "email": "wjzijderveld@gmail.com"
                },
                {
                    "name": "Qandidate.com",
                    "homepage": "http://labs.qandidate.com/"
                }
            ],
            "description": "Event store implementation using doctrine/dbal",
            "support": {
                "issues": "https://github.com/broadway/event-store-dbal/issues",
                "source": "https://github.com/broadway/event-store-dbal/tree/0.6.0"
            },
            "time": "2021-06-24T09:42:53+00:00"
        },
        {
            "name": "broadway/uuid-generator",
            "version": "1.0.0",
            "source": {
                "type": "git",
                "url": "https://github.com/broadway/broadway-uuid-generator.git",
                "reference": "908de6999cdb77f1b323abd3e64e8ce6f86db3e5"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/broadway/broadway-uuid-generator/zipball/908de6999cdb77f1b323abd3e64e8ce6f86db3e5",
                "reference": "908de6999cdb77f1b323abd3e64e8ce6f86db3e5",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2"
            },
            "require-dev": {
                "broadway/coding-standard": "^1.0",
                "phpstan/phpstan": "@stable",
                "phpunit/phpunit": "^8.0",
                "ramsey/uuid": "^3.0"
            },
            "suggest": {
                "ramsey/uuid": "Allows creating UUIDs"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "2.0.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Broadway\\UuidGenerator\\": "src/Broadway/UuidGenerator"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "description": "UUID generator for broadway/broadway.",
            "support": {
                "issues": "https://github.com/broadway/broadway-uuid-generator/issues",
                "source": "https://github.com/broadway/broadway-uuid-generator/tree/master"
            },
            "time": "2020-03-06T10:09:30+00:00"
        },
        {
            "name": "doctrine/collections",
            "version": "2.6.0",
            "source": {
                "type": "git",
                "url": "https://github.com/doctrine/collections.git",
                "reference": "7713da39d8e237f28411d6a616a3dce5e20d5de2"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/doctrine/collections/zipball/7713da39d8e237f28411d6a616a3dce5e20d5de2",
                "reference": "7713da39d8e237f28411d6a616a3dce5e20d5de2",
                "shasum": ""
            },
            "require": {
                "doctrine/deprecations": "^1",
                "php": "^8.1",
                "symfony/polyfill-php84": "^1.30"
            },
            "require-dev": {
                "doctrine/coding-standard": "^14",
                "ext-json": "*",
                "phpstan/phpstan": "^2.1.30",
                "phpstan/phpstan-phpunit": "^2.0.7",
                "phpunit/phpunit": "^10.5.58 || ^11.5.42 || ^12.4"
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
                "source": "https://github.com/doctrine/collections/tree/2.6.0"
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
            "time": "2026-01-15T10:01:58+00:00"
        },
        {
            "name": "doctrine/dbal",
            "version": "3.10.4",
            "source": {
                "type": "git",
                "url": "https://github.com/doctrine/dbal.git",
                "reference": "63a46cb5aa6f60991186cc98c1d1b50c09311868"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/doctrine/dbal/zipball/63a46cb5aa6f60991186cc98c1d1b50c09311868",
                "reference": "63a46cb5aa6f60991186cc98c1d1b50c09311868",
                "shasum": ""
            },
            "require": {
                "composer-runtime-api": "^2",
                "doctrine/deprecations": "^0.5.3|^1",
                "doctrine/event-manager": "^1|^2",
                "php": "^7.4 || ^8.0",
                "psr/cache": "^1|^2|^3",
                "psr/log": "^1|^2|^3"
            },
            "conflict": {
                "doctrine/cache": "< 1.11"
            },
            "require-dev": {
                "doctrine/cache": "^1.11|^2.0",
                "doctrine/coding-standard": "14.0.0",
                "fig/log-test": "^1",
                "jetbrains/phpstorm-stubs": "2023.1",
                "phpstan/phpstan": "2.1.30",
                "phpstan/phpstan-strict-rules": "^2",
                "phpunit/phpunit": "9.6.29",
                "slevomat/coding-standard": "8.24.0",
                "squizlabs/php_codesniffer": "4.0.0",
                "symfony/cache": "^5.4|^6.0|^7.0|^8.0",
                "symfony/console": "^4.4|^5.4|^6.0|^7.0|^8.0"
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
                "source": "https://github.com/doctrine/dbal/tree/3.10.4"
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
            "time": "2025-11-29T10:46:08+00:00"
        },
        {
            "name": "doctrine/deprecations",
            "version": "1.1.5",
            "source": {
                "type": "git",
                "url": "https://github.com/doctrine/deprecations.git",
                "reference": "459c2f5dd3d6a4633d3b5f46ee2b1c40f57d3f38"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/doctrine/deprecations/zipball/459c2f5dd3d6a4633d3b5f46ee2b1c40f57d3f38",
                "reference": "459c2f5dd3d6a4633d3b5f46ee2b1c40f57d3f38",
                "shasum": ""
            },
            "require": {
                "php": "^7.1 || ^8.0"
            },
            "conflict": {
                "phpunit/phpunit": "<=7.5 || >=13"
            },
            "require-dev": {
                "doctrine/coding-standard": "^9 || ^12 || ^13",
                "phpstan/phpstan": "1.4.10 || 2.1.11",
                "phpstan/phpstan-phpunit": "^1.0 || ^2",
                "phpunit/phpunit": "^7.5 || ^8.5 || ^9.6 || ^10.5 || ^11.5 || ^12",
                "psr/log": "^1 || ^2 || ^3"
            },
            "suggest": {
                "psr/log": "Allows logging deprecations via PSR-3 logger implementation"
            },
            "type": "library",
            "autoload": {
                "psr-4": {
                    "Doctrine\\Deprecations\\": "src"
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
                "source": "https://github.com/doctrine/deprecations/tree/1.1.5"
            },
            "time": "2025-04-07T20:06:18+00:00"
        },
        {
            "name": "doctrine/doctrine-bundle",
            "version": "2.18.2",
            "source": {
                "type": "git",
                "url": "https://github.com/doctrine/DoctrineBundle.git",
                "reference": "0ff098b29b8b3c68307c8987dcaed7fd829c6546"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/doctrine/DoctrineBundle/zipball/0ff098b29b8b3c68307c8987dcaed7fd829c6546",
                "reference": "0ff098b29b8b3c68307c8987dcaed7fd829c6546",
                "shasum": ""
            },
            "require": {
                "doctrine/dbal": "^3.7.0 || ^4.0",
                "doctrine/deprecations": "^1.0",
                "doctrine/persistence": "^3.1 || ^4",
                "doctrine/sql-formatter": "^1.0.1",
                "php": "^8.1",
                "symfony/cache": "^6.4 || ^7.0",
                "symfony/config": "^6.4 || ^7.0",
                "symfony/console": "^6.4 || ^7.0",
                "symfony/dependency-injection": "^6.4 || ^7.0",
                "symfony/doctrine-bridge": "^6.4.3 || ^7.0.3",
                "symfony/framework-bundle": "^6.4 || ^7.0",
                "symfony/service-contracts": "^2.5 || ^3"
            },
            "conflict": {
                "doctrine/annotations": ">=3.0",
                "doctrine/cache": "< 1.11",
                "doctrine/orm": "<2.17 || >=4.0",
                "symfony/var-exporter": "< 6.4.1 || 7.0.0",
                "twig/twig": "<2.13 || >=3.0 <3.0.4"
            },
            "require-dev": {
                "doctrine/annotations": "^1 || ^2",
                "doctrine/cache": "^1.11 || ^2.0",
                "doctrine/coding-standard": "^14",
                "doctrine/orm": "^2.17 || ^3.1",
                "friendsofphp/proxy-manager-lts": "^1.0",
                "phpstan/phpstan": "2.1.1",
                "phpstan/phpstan-phpunit": "2.0.3",
                "phpstan/phpstan-strict-rules": "^2",
                "phpunit/phpunit": "^10.5.53 || ^12.3.10",
                "psr/log": "^1.1.4 || ^2.0 || ^3.0",
                "symfony/doctrine-messenger": "^6.4 || ^7.0",
                "symfony/expression-language": "^6.4 || ^7.0",
                "symfony/messenger": "^6.4 || ^7.0",
                "symfony/property-info": "^6.4 || ^7.0",
                "symfony/security-bundle": "^6.4 || ^7.0",
                "symfony/stopwatch": "^6.4 || ^7.0",
                "symfony/string": "^6.4 || ^7.0",
                "symfony/twig-bridge": "^6.4 || ^7.0",
                "symfony/validator": "^6.4 || ^7.0",
                "symfony/var-exporter": "^6.4.1 || ^7.0.1",
                "symfony/web-profiler-bundle": "^6.4 || ^7.0",
                "symfony/yaml": "^6.4 || ^7.0",
                "twig/twig": "^2.14.7 || ^3.0.4"
            },
            "suggest": {
                "doctrine/orm": "The Doctrine ORM integration is optional in the bundle.",
                "ext-pdo": "*",
                "symfony/web-profiler-bundle": "To use the data collector."
            },
            "type": "symfony-bundle",
            "autoload": {
                "psr-4": {
                    "Doctrine\\Bundle\\DoctrineBundle\\": "src"
                }
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
                    "name": "Benjamin Eberlei",
                    "email": "kontakt@beberlei.de"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                },
                {
                    "name": "Doctrine Project",
                    "homepage": "https://www.doctrine-project.org/"
                }
            ],
            "description": "Symfony DoctrineBundle",
            "homepage": "https://www.doctrine-project.org",
            "keywords": [
                "database",
                "dbal",
                "orm",
                "persistence"
            ],
            "support": {
                "issues": "https://github.com/doctrine/DoctrineBundle/issues",
                "source": "https://github.com/doctrine/DoctrineBundle/tree/2.18.2"
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
                    "url": "https://tidelift.com/funding/github/packagist/doctrine%2Fdoctrine-bundle",
                    "type": "tidelift"
                }
            ],
            "time": "2025-12-20T21:35:32+00:00"
        },
        {
            "name": "doctrine/doctrine-migrations-bundle",
            "version": "3.7.0",
            "source": {
                "type": "git",
                "url": "https://github.com/doctrine/DoctrineMigrationsBundle.git",
                "reference": "1e380c6dd8ac8488217f39cff6b77e367f1a644b"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/doctrine/DoctrineMigrationsBundle/zipball/1e380c6dd8ac8488217f39cff6b77e367f1a644b",
                "reference": "1e380c6dd8ac8488217f39cff6b77e367f1a644b",
                "shasum": ""
            },
            "require": {
                "doctrine/doctrine-bundle": "^2.4 || ^3.0",
                "doctrine/migrations": "^3.2",
                "php": "^7.2 || ^8.0",
                "symfony/deprecation-contracts": "^2.1 || ^3",
                "symfony/framework-bundle": "^5.4 || ^6.0 || ^7.0 || ^8.0"
            },
            "require-dev": {
                "composer/semver": "^3.0",
                "doctrine/coding-standard": "^12 || ^14",
                "doctrine/orm": "^2.6 || ^3",
                "phpstan/phpstan": "^1.4 || ^2",
                "phpstan/phpstan-deprecation-rules": "^1 || ^2",
                "phpstan/phpstan-phpunit": "^1 || ^2",
                "phpstan/phpstan-strict-rules": "^1.1 || ^2",
                "phpstan/phpstan-symfony": "^1.3 || ^2",
                "phpunit/phpunit": "^8.5 || ^9.5",
                "symfony/phpunit-bridge": "^6.3 || ^7 || ^8",
                "symfony/var-exporter": "^5.4 || ^6 || ^7 || ^8"
            },
            "type": "symfony-bundle",
            "autoload": {
                "psr-4": {
                    "Doctrine\\Bundle\\MigrationsBundle\\": "src"
                }
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
                    "name": "Doctrine Project",
                    "homepage": "https://www.doctrine-project.org"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Symfony DoctrineMigrationsBundle",
            "homepage": "https://www.doctrine-project.org",
            "keywords": [
                "dbal",
                "migrations",
                "schema"
            ],
            "support": {
                "issues": "https://github.com/doctrine/DoctrineMigrationsBundle/issues",
                "source": "https://github.com/doctrine/DoctrineMigrationsBundle/tree/3.7.0"
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
                    "url": "https://tidelift.com/funding/github/packagist/doctrine%2Fdoctrine-migrations-bundle",
                    "type": "tidelift"
                }
            ],
            "time": "2025-11-15T19:02:59+00:00"
        },
        {
            "name": "doctrine/event-manager",
            "version": "2.1.1",
            "source": {
                "type": "git",
                "url": "https://github.com/doctrine/event-manager.git",
                "reference": "dda33921b198841ca8dbad2eaa5d4d34769d18cf"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/doctrine/event-manager/zipball/dda33921b198841ca8dbad2eaa5d4d34769d18cf",
                "reference": "dda33921b198841ca8dbad2eaa5d4d34769d18cf",
                "shasum": ""
            },
            "require": {
                "php": "^8.1"
            },
            "conflict": {
                "doctrine/common": "<2.9"
            },
            "require-dev": {
                "doctrine/coding-standard": "^14",
                "phpdocumentor/guides-cli": "^1.4",
                "phpstan/phpstan": "^2.1.32",
                "phpunit/phpunit": "^10.5.58"
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
                "source": "https://github.com/doctrine/event-manager/tree/2.1.1"
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
            "time": "2026-01-29T07:11:08+00:00"
        },
        {
            "name": "doctrine/inflector",
            "version": "2.1.0",
            "source": {
                "type": "git",
                "url": "https://github.com/doctrine/inflector.git",
                "reference": "6d6c96277ea252fc1304627204c3d5e6e15faa3b"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/doctrine/inflector/zipball/6d6c96277ea252fc1304627204c3d5e6e15faa3b",
                "reference": "6d6c96277ea252fc1304627204c3d5e6e15faa3b",
                "shasum": ""
            },
            "require": {
                "php": "^7.2 || ^8.0"
            },
            "require-dev": {
                "doctrine/coding-standard": "^12.0 || ^13.0",
                "phpstan/phpstan": "^1.12 || ^2.0",
                "phpstan/phpstan-phpunit": "^1.4 || ^2.0",
                "phpstan/phpstan-strict-rules": "^1.6 || ^2.0",
                "phpunit/phpunit": "^8.5 || ^12.2"
            },
            "type": "library",
            "autoload": {
                "psr-4": {
                    "Doctrine\\Inflector\\": "src"
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
                "source": "https://github.com/doctrine/inflector/tree/2.1.0"
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
            "time": "2025-08-10T19:31:58+00:00"
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
            "name": "doctrine/migrations",
            "version": "3.9.5",
            "source": {
                "type": "git",
                "url": "https://github.com/doctrine/migrations.git",
                "reference": "1b823afbc40f932dae8272574faee53f2755eac5"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/doctrine/migrations/zipball/1b823afbc40f932dae8272574faee53f2755eac5",
                "reference": "1b823afbc40f932dae8272574faee53f2755eac5",
                "shasum": ""
            },
            "require": {
                "composer-runtime-api": "^2",
                "doctrine/dbal": "^3.6 || ^4",
                "doctrine/deprecations": "^0.5.3 || ^1",
                "doctrine/event-manager": "^1.2 || ^2.0",
                "php": "^8.1",
                "psr/log": "^1.1.3 || ^2 || ^3",
                "symfony/console": "^5.4 || ^6.0 || ^7.0 || ^8.0",
                "symfony/stopwatch": "^5.4 || ^6.0 || ^7.0 || ^8.0",
                "symfony/var-exporter": "^6.2 || ^7.0 || ^8.0"
            },
            "conflict": {
                "doctrine/orm": "<2.12 || >=4"
            },
            "require-dev": {
                "doctrine/coding-standard": "^14",
                "doctrine/orm": "^2.13 || ^3",
                "doctrine/persistence": "^2 || ^3 || ^4",
                "doctrine/sql-formatter": "^1.0",
                "ext-pdo_sqlite": "*",
                "fig/log-test": "^1",
                "phpstan/phpstan": "^2",
                "phpstan/phpstan-deprecation-rules": "^2",
                "phpstan/phpstan-phpunit": "^2",
                "phpstan/phpstan-strict-rules": "^2",
                "phpstan/phpstan-symfony": "^2",
                "phpunit/phpunit": "^10.3 || ^11.0 || ^12.0",
                "symfony/cache": "^5.4 || ^6.0 || ^7.0 || ^8.0",
                "symfony/process": "^5.4 || ^6.0 || ^7.0 || ^8.0",
                "symfony/yaml": "^5.4 || ^6.0 || ^7.0 || ^8.0"
            },
            "suggest": {
                "doctrine/sql-formatter": "Allows to generate formatted SQL with the diff command.",
                "symfony/yaml": "Allows the use of yaml for migration configuration files."
            },
            "bin": [
                "bin/doctrine-migrations"
            ],
            "type": "library",
            "autoload": {
                "psr-4": {
                    "Doctrine\\Migrations\\": "src"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Benjamin Eberlei",
                    "email": "kontakt@beberlei.de"
                },
                {
                    "name": "Jonathan Wage",
                    "email": "jonwage@gmail.com"
                },
                {
                    "name": "Michael Simonson",
                    "email": "contact@mikesimonson.com"
                }
            ],
            "description": "PHP Doctrine Migrations project offer additional functionality on top of the database abstraction layer (DBAL) for versioning your database schema and easily deploying changes to it. It is a very easy to use and a powerful tool.",
            "homepage": "https://www.doctrine-project.org/projects/migrations.html",
            "keywords": [
                "database",
                "dbal",
                "migrations"
            ],
            "support": {
                "issues": "https://github.com/doctrine/migrations/issues",
                "source": "https://github.com/doctrine/migrations/tree/3.9.5"
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
                    "url": "https://tidelift.com/funding/github/packagist/doctrine%2Fmigrations",
                    "type": "tidelift"
                }
            ],
            "time": "2025-11-20T11:15:36+00:00"
        },
        {
            "name": "doctrine/orm",
            "version": "3.6.2",
            "source": {
                "type": "git",
                "url": "https://github.com/doctrine/orm.git",
                "reference": "4262eb495b4d2a53b45de1ac58881e0091f2970f"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/doctrine/orm/zipball/4262eb495b4d2a53b45de1ac58881e0091f2970f",
                "reference": "4262eb495b4d2a53b45de1ac58881e0091f2970f",
                "shasum": ""
            },
            "require": {
                "composer-runtime-api": "^2",
                "doctrine/collections": "^2.2",
                "doctrine/dbal": "^3.8.2 || ^4",
                "doctrine/deprecations": "^0.5.3 || ^1",
                "doctrine/event-manager": "^1.2 || ^2",
                "doctrine/inflector": "^1.4 || ^2.0",
                "doctrine/instantiator": "^1.3 || ^2",
                "doctrine/lexer": "^3",
                "doctrine/persistence": "^3.3.1 || ^4",
                "ext-ctype": "*",
                "php": "^8.1",
                "psr/cache": "^1 || ^2 || ^3",
                "symfony/console": "^5.4 || ^6.0 || ^7.0 || ^8.0",
                "symfony/var-exporter": "^6.3.9 || ^7.0 || ^8.0"
            },
            "require-dev": {
                "doctrine/coding-standard": "^14.0",
                "phpbench/phpbench": "^1.0",
                "phpstan/extension-installer": "^1.4",
                "phpstan/phpstan": "2.1.23",
                "phpstan/phpstan-deprecation-rules": "^2",
                "phpunit/phpunit": "^10.5.0 || ^11.5",
                "psr/log": "^1 || ^2 || ^3",
                "symfony/cache": "^5.4 || ^6.2 || ^7.0 || ^8.0"
            },
            "suggest": {
                "ext-dom": "Provides support for XSD validation for XML mapping files",
                "symfony/cache": "Provides cache support for Setup Tool with doctrine/cache 2.0"
            },
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
                "source": "https://github.com/doctrine/orm/tree/3.6.2"
            },
            "time": "2026-01-30T21:41:41+00:00"
        },
        {
            "name": "doctrine/persistence",
            "version": "4.1.1",
            "source": {
                "type": "git",
                "url": "https://github.com/doctrine/persistence.git",
                "reference": "b9c49ad3558bb77ef973f4e173f2e9c2eca9be09"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/doctrine/persistence/zipball/b9c49ad3558bb77ef973f4e173f2e9c2eca9be09",
                "reference": "b9c49ad3558bb77ef973f4e173f2e9c2eca9be09",
                "shasum": ""
            },
            "require": {
                "doctrine/event-manager": "^1 || ^2",
                "php": "^8.1",
                "psr/cache": "^1.0 || ^2.0 || ^3.0"
            },
            "require-dev": {
                "doctrine/coding-standard": "^14",
                "phpstan/phpstan": "2.1.30",
                "phpstan/phpstan-phpunit": "^2",
                "phpstan/phpstan-strict-rules": "^2",
                "phpunit/phpunit": "^10.5.58 || ^12",
                "symfony/cache": "^4.4 || ^5.4 || ^6.0 || ^7.0",
                "symfony/finder": "^4.4 || ^5.4 || ^6.0 || ^7.0"
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
                "source": "https://github.com/doctrine/persistence/tree/4.1.1"
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
            "time": "2025-10-16T20:13:18+00:00"
        },
        {
            "name": "doctrine/sql-formatter",
            "version": "1.5.3",
            "source": {
                "type": "git",
                "url": "https://github.com/doctrine/sql-formatter.git",
                "reference": "a8af23a8e9d622505baa2997465782cbe8bb7fc7"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/doctrine/sql-formatter/zipball/a8af23a8e9d622505baa2997465782cbe8bb7fc7",
                "reference": "a8af23a8e9d622505baa2997465782cbe8bb7fc7",
                "shasum": ""
            },
            "require": {
                "php": "^8.1"
            },
            "require-dev": {
                "doctrine/coding-standard": "^14",
                "ergebnis/phpunit-slow-test-detector": "^2.20",
                "phpstan/phpstan": "^2.1.31",
                "phpunit/phpunit": "^10.5.58"
            },
            "bin": [
                "bin/sql-formatter"
            ],
            "type": "library",
            "autoload": {
                "psr-4": {
                    "Doctrine\\SqlFormatter\\": "src"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Jeremy Dorn",
                    "email": "jeremy@jeremydorn.com",
                    "homepage": "https://jeremydorn.com/"
                }
            ],
            "description": "a PHP SQL highlighting library",
            "homepage": "https://github.com/doctrine/sql-formatter/",
            "keywords": [
                "highlight",
                "sql"
            ],
            "support": {
                "issues": "https://github.com/doctrine/sql-formatter/issues",
                "source": "https://github.com/doctrine/sql-formatter/tree/1.5.3"
            },
            "time": "2025-10-26T09:35:14+00:00"
        },
        {
            "name": "elasticsearch/elasticsearch",
            "version": "v7.17.3",
            "source": {
                "type": "git",
                "url": "https://github.com/elastic/elasticsearch-php.git",
                "reference": "b8a60b4136ee31117d1aa1b19879530eb6d11efb"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/elastic/elasticsearch-php/zipball/b8a60b4136ee31117d1aa1b19879530eb6d11efb",
                "reference": "b8a60b4136ee31117d1aa1b19879530eb6d11efb",
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
                "source": "https://github.com/elastic/elasticsearch-php/tree/v7.17.3"
            },
            "time": "2025-07-14T09:07:02+00:00"
        },
        {
            "name": "ezimuel/guzzlestreams",
            "version": "4.1.0",
            "source": {
                "type": "git",
                "url": "https://github.com/ezimuel/guzzlestreams.git",
                "reference": "903161be81e9f497cc42fb7db982404a4e6441b0"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/ezimuel/guzzlestreams/zipball/903161be81e9f497cc42fb7db982404a4e6441b0",
                "reference": "903161be81e9f497cc42fb7db982404a4e6441b0",
                "shasum": ""
            },
            "require": {
                "php": ">=7.4.0"
            },
            "require-dev": {
                "phpstan/phpstan": "^2.1",
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
                "source": "https://github.com/ezimuel/guzzlestreams/tree/4.1.0"
            },
            "time": "2025-08-05T06:44:46+00:00"
        },
        {
            "name": "ezimuel/ringphp",
            "version": "1.4.0",
            "source": {
                "type": "git",
                "url": "https://github.com/ezimuel/ringphp.git",
                "reference": "bc983599ec7add50c00e420e867c403c8ed16ae7"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/ezimuel/ringphp/zipball/bc983599ec7add50c00e420e867c403c8ed16ae7",
                "reference": "bc983599ec7add50c00e420e867c403c8ed16ae7",
                "shasum": ""
            },
            "require": {
                "ezimuel/guzzlestreams": "^3.0.1 || ^4.0.0",
                "php": ">=5.4.0",
                "react/promise": "^2.0 || ^3.0"
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
                "source": "https://github.com/ezimuel/ringphp/tree/1.4.0"
            },
            "time": "2025-08-07T09:30:38+00:00"
        },
        {
            "name": "lcobucci/jwt",
            "version": "5.6.0",
            "source": {
                "type": "git",
                "url": "https://github.com/lcobucci/jwt.git",
                "reference": "bb3e9f21e4196e8afc41def81ef649c164bca25e"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/lcobucci/jwt/zipball/bb3e9f21e4196e8afc41def81ef649c164bca25e",
                "reference": "bb3e9f21e4196e8afc41def81ef649c164bca25e",
                "shasum": ""
            },
            "require": {
                "ext-openssl": "*",
                "ext-sodium": "*",
                "php": "~8.2.0 || ~8.3.0 || ~8.4.0 || ~8.5.0",
                "psr/clock": "^1.0"
            },
            "require-dev": {
                "infection/infection": "^0.29",
                "lcobucci/clock": "^3.2",
                "lcobucci/coding-standard": "^11.0",
                "phpbench/phpbench": "^1.2",
                "phpstan/extension-installer": "^1.2",
                "phpstan/phpstan": "^1.10.7",
                "phpstan/phpstan-deprecation-rules": "^1.1.3",
                "phpstan/phpstan-phpunit": "^1.3.10",
                "phpstan/phpstan-strict-rules": "^1.5.0",
                "phpunit/phpunit": "^11.1"
            },
            "suggest": {
                "lcobucci/clock": ">= 3.2"
            },
            "type": "library",
            "autoload": {
                "psr-4": {
                    "Lcobucci\\JWT\\": "src"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause"
            ],
            "authors": [
                {
                    "name": "Luís Cobucci",
                    "email": "lcobucci@gmail.com",
                    "role": "Developer"
                }
            ],
            "description": "A simple library to work with JSON Web Token and JSON Web Signature",
            "keywords": [
                "JWS",
                "jwt"
            ],
            "support": {
                "issues": "https://github.com/lcobucci/jwt/issues",
                "source": "https://github.com/lcobucci/jwt/tree/5.6.0"
            },
            "funding": [
                {
                    "url": "https://github.com/lcobucci",
                    "type": "github"
                },
                {
                    "url": "https://www.patreon.com/lcobucci",
                    "type": "patreon"
                }
            ],
            "time": "2025-10-17T11:30:53+00:00"
        },
        {
            "name": "lexik/jwt-authentication-bundle",
            "version": "v3.2.0",
            "source": {
                "type": "git",
                "url": "https://github.com/lexik/LexikJWTAuthenticationBundle.git",
                "reference": "60df75dc70ee6f597929cb2f0812adda591dfa4b"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/lexik/LexikJWTAuthenticationBundle/zipball/60df75dc70ee6f597929cb2f0812adda591dfa4b",
                "reference": "60df75dc70ee6f597929cb2f0812adda591dfa4b",
                "shasum": ""
            },
            "require": {
                "ext-openssl": "*",
                "lcobucci/jwt": "^5.0",
                "php": ">=8.2",
                "symfony/clock": "^6.4|^7.0|^8.0",
                "symfony/config": "^6.4|^7.0|^8.0",
                "symfony/dependency-injection": "^6.4|^7.0|^8.0",
                "symfony/deprecation-contracts": "^2.4|^3.0",
                "symfony/event-dispatcher": "^6.4|^7.0|^8.0",
                "symfony/http-foundation": "^6.4|^7.0|^8.0",
                "symfony/http-kernel": "^6.4|^7.0|^8.0",
                "symfony/property-access": "^6.4|^7.0|^8.0",
                "symfony/security-bundle": "^6.4|^7.0|^8.0",
                "symfony/translation-contracts": "^1.0|^2.0|^3.0"
            },
            "require-dev": {
                "api-platform/core": "^3.0|^4.0",
                "rector/rector": "^1.2",
                "symfony/browser-kit": "^6.4|^7.0|^8.0",
                "symfony/console": "^6.4|^7.0|^8.0",
                "symfony/dom-crawler": "^6.4|^7.0|^8.0",
                "symfony/filesystem": "^6.4|^7.0|^8.0",
                "symfony/framework-bundle": "^6.4|^7.0|^8.0",
                "symfony/phpunit-bridge": "^6.4|^7.0|^8.0",
                "symfony/var-dumper": "^6.4|^7.0|^8.0",
                "symfony/yaml": "^6.4|^7.0|^8.0"
            },
            "suggest": {
                "gesdinet/jwt-refresh-token-bundle": "Implements a refresh token system over Json Web Tokens in Symfony",
                "spomky-labs/lexik-jose-bridge": "Provides a JWT Token encoder with encryption support"
            },
            "type": "symfony-bundle",
            "autoload": {
                "psr-4": {
                    "Lexik\\Bundle\\JWTAuthenticationBundle\\": ""
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
                    "name": "Jeremy Barthe",
                    "email": "j.barthe@lexik.fr",
                    "homepage": "https://github.com/jeremyb"
                },
                {
                    "name": "Nicolas Cabot",
                    "email": "n.cabot@lexik.fr",
                    "homepage": "https://github.com/slashfan"
                },
                {
                    "name": "Cedric Girard",
                    "email": "c.girard@lexik.fr",
                    "homepage": "https://github.com/cedric-g"
                },
                {
                    "name": "Dev Lexik",
                    "email": "dev@lexik.fr",
                    "homepage": "https://github.com/lexik"
                },
                {
                    "name": "Robin Chalas",
                    "email": "robin.chalas@gmail.com",
                    "homepage": "https://github.com/chalasr"
                },
                {
                    "name": "Lexik Community",
                    "homepage": "https://github.com/lexik/LexikJWTAuthenticationBundle/graphs/contributors"
                }
            ],
            "description": "This bundle provides JWT authentication for your Symfony REST API",
            "homepage": "https://github.com/lexik/LexikJWTAuthenticationBundle",
            "keywords": [
                "Authentication",
                "JWS",
                "api",
                "bundle",
                "jwt",
                "rest",
                "symfony"
            ],
            "support": {
                "issues": "https://github.com/lexik/LexikJWTAuthenticationBundle/issues",
                "source": "https://github.com/lexik/LexikJWTAuthenticationBundle/tree/v3.2.0"
            },
            "funding": [
                {
                    "url": "https://github.com/chalasr",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/lexik/jwt-authentication-bundle",
                    "type": "tidelift"
                }
            ],
            "time": "2025-12-20T17:47:00+00:00"
        },
        {
            "name": "monolog/monolog",
            "version": "3.10.0",
            "source": {
                "type": "git",
                "url": "https://github.com/Seldaek/monolog.git",
                "reference": "b321dd6749f0bf7189444158a3ce785cc16d69b0"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/Seldaek/monolog/zipball/b321dd6749f0bf7189444158a3ce785cc16d69b0",
                "reference": "b321dd6749f0bf7189444158a3ce785cc16d69b0",
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
                "mongodb/mongodb": "^1.8 || ^2.0",
                "php-amqplib/php-amqplib": "~2.4 || ^3",
                "php-console/php-console": "^3.1.8",
                "phpstan/phpstan": "^2",
                "phpstan/phpstan-deprecation-rules": "^2",
                "phpstan/phpstan-strict-rules": "^2",
                "phpunit/phpunit": "^10.5.17 || ^11.0.7",
                "predis/predis": "^1.1 || ^2",
                "rollbar/rollbar": "^4.0",
                "ruflin/elastica": "^7 || ^8",
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
                "source": "https://github.com/Seldaek/monolog/tree/3.10.0"
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
            "time": "2026-01-02T08:56:05+00:00"
        },
        {
            "name": "nelmio/api-doc-bundle",
            "version": "v4.38.7",
            "source": {
                "type": "git",
                "url": "https://github.com/nelmio/NelmioApiDocBundle.git",
                "reference": "1d53f99b8015ce466c64f7ffee908a48651273e8"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/nelmio/NelmioApiDocBundle/zipball/1d53f99b8015ce466c64f7ffee908a48651273e8",
                "reference": "1d53f99b8015ce466c64f7ffee908a48651273e8",
                "shasum": ""
            },
            "require": {
                "ext-json": "*",
                "php": ">=7.4",
                "phpdocumentor/reflection-docblock": "^4.3.4 || ^5.0",
                "phpdocumentor/type-resolver": "^1.8.2",
                "psr/cache": "^1.0 || ^2.0 || ^3.0",
                "psr/container": "^1.0 || ^2.0",
                "psr/log": "^1.0 || ^2.0 || ^3.0",
                "symfony/config": "^5.4 || ^6.4 || ^7.1",
                "symfony/console": "^5.4 || ^6.4 || ^7.1",
                "symfony/dependency-injection": "^5.4 || ^6.4 || ^7.1",
                "symfony/deprecation-contracts": "^2.1 || ^3",
                "symfony/framework-bundle": "^5.4.24 || ^6.4 || ^7.1",
                "symfony/http-foundation": "^5.4 || ^6.4 || ^7.1",
                "symfony/http-kernel": "^5.4 || ^6.4 || ^7.1",
                "symfony/options-resolver": "^5.4 || ^6.4 || ^7.1",
                "symfony/property-info": "^5.4.10 || ^6.4 || ^7.1",
                "symfony/routing": "^5.4 || ^6.4 || ^7.1",
                "zircote/swagger-php": "^4.11.1 || ^5.0"
            },
            "conflict": {
                "zircote/swagger-php": "4.8.7 || 5.5.0"
            },
            "require-dev": {
                "api-platform/core": "^2.7.0 || ^3",
                "composer/package-versions-deprecated": "1.11.99.1",
                "doctrine/annotations": "^2.0",
                "friendsofphp/php-cs-fixer": "^3.52",
                "friendsofsymfony/rest-bundle": "^2.8 || ^3.0",
                "jms/serializer": "^1.14 || ^3.0",
                "jms/serializer-bundle": "^2.3 || ^3.0 || ^4.0 || ^5.0",
                "phpstan/phpstan": "^1.10",
                "phpstan/phpstan-phpunit": "^1.3",
                "phpstan/phpstan-strict-rules": "^1.5",
                "phpstan/phpstan-symfony": "^1.3",
                "phpunit/phpunit": "^9.6 || ^10.5",
                "symfony/asset": "^5.4 || ^6.4 || ^7.1",
                "symfony/browser-kit": "^5.4 || ^6.4 || ^7.1",
                "symfony/cache": "^5.4 || ^6.4 || ^7.1",
                "symfony/dom-crawler": "^5.4 || ^6.4 || ^7.1",
                "symfony/expression-language": "^5.4 || ^6.4 || ^7.1",
                "symfony/form": "^5.4 || ^6.4 || ^7.1",
                "symfony/phpunit-bridge": "^6.4",
                "symfony/property-access": "^5.4 || ^6.4 || ^7.1",
                "symfony/security-csrf": "^5.4 || ^6.4 || ^7.1",
                "symfony/serializer": "^5.4 || ^6.4 || ^7.1",
                "symfony/stopwatch": "^5.4 || ^6.4 || ^7.1",
                "symfony/templating": "^5.4 || ^6.4 || ^7.1",
                "symfony/twig-bundle": "^5.4 || ^6.4 || ^7.1",
                "symfony/uid": "^5.4 || ^6.4 || ^7.1",
                "symfony/validator": "^5.4 || ^6.4 || ^7.1",
                "willdurand/hateoas-bundle": "^1.0 || ^2.0"
            },
            "suggest": {
                "api-platform/core": "For using an API oriented framework.",
                "doctrine/annotations": "For using doctrine annotations",
                "friendsofsymfony/rest-bundle": "For using the parameters annotations.",
                "jms/serializer-bundle": "For describing your models.",
                "symfony/asset": "For using the Swagger UI.",
                "symfony/cache": "For using a PSR-6 compatible cache implementation with the API doc generator.",
                "symfony/form": "For describing your form type models.",
                "symfony/monolog-bundle": "For using a PSR-3 compatible logger implementation with the API PHP describer.",
                "symfony/security-csrf": "For using csrf protection tokens in forms.",
                "symfony/serializer": "For describing your models.",
                "symfony/twig-bundle": "For using the Swagger UI.",
                "symfony/validator": "For describing the validation constraints in your models.",
                "willdurand/hateoas-bundle": "For extracting HATEOAS metadata."
            },
            "type": "symfony-bundle",
            "extra": {
                "branch-alias": {
                    "dev-4.x": "4.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Nelmio\\ApiDocBundle\\": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Symfony Community",
                    "homepage": "https://github.com/nelmio/NelmioApiDocBundle/contributors"
                }
            ],
            "description": "Generates documentation for your REST API from annotations and attributes",
            "keywords": [
                "api",
                "doc",
                "documentation",
                "rest"
            ],
            "support": {
                "issues": "https://github.com/nelmio/NelmioApiDocBundle/issues",
                "source": "https://github.com/nelmio/NelmioApiDocBundle/tree/v4.38.7"
            },
            "funding": [
                {
                    "url": "https://github.com/DjordyKoert",
                    "type": "github"
                }
            ],
            "time": "2026-01-08T08:45:13+00:00"
        },
        {
            "name": "nikic/php-parser",
            "version": "v4.19.5",
            "source": {
                "type": "git",
                "url": "https://github.com/nikic/PHP-Parser.git",
                "reference": "51bd93cc741b7fc3d63d20b6bdcd99fdaa359837"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/nikic/PHP-Parser/zipball/51bd93cc741b7fc3d63d20b6bdcd99fdaa359837",
                "reference": "51bd93cc741b7fc3d63d20b6bdcd99fdaa359837",
                "shasum": ""
            },
            "require": {
                "ext-tokenizer": "*",
                "php": ">=7.1"
            },
            "require-dev": {
                "ircmaxell/php-yacc": "^0.0.7",
                "phpunit/phpunit": "^7.0 || ^8.0 || ^9.0"
            },
            "bin": [
                "bin/php-parse"
            ],
            "type": "library",
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
                "source": "https://github.com/nikic/PHP-Parser/tree/v4.19.5"
            },
            "time": "2025-12-06T11:45:25+00:00"
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
            "version": "5.6.6",
            "source": {
                "type": "git",
                "url": "https://github.com/phpDocumentor/ReflectionDocBlock.git",
                "reference": "5cee1d3dfc2d2aa6599834520911d246f656bcb8"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/phpDocumentor/ReflectionDocBlock/zipball/5cee1d3dfc2d2aa6599834520911d246f656bcb8",
                "reference": "5cee1d3dfc2d2aa6599834520911d246f656bcb8",
                "shasum": ""
            },
            "require": {
                "doctrine/deprecations": "^1.1",
                "ext-filter": "*",
                "php": "^7.4 || ^8.0",
                "phpdocumentor/reflection-common": "^2.2",
                "phpdocumentor/type-resolver": "^1.7",
                "phpstan/phpdoc-parser": "^1.7|^2.0",
                "webmozart/assert": "^1.9.1 || ^2"
            },
            "require-dev": {
                "mockery/mockery": "~1.3.5 || ~1.6.0",
                "phpstan/extension-installer": "^1.1",
                "phpstan/phpstan": "^1.8",
                "phpstan/phpstan-mockery": "^1.1",
                "phpstan/phpstan-webmozart-assert": "^1.2",
                "phpunit/phpunit": "^9.5",
                "psalm/phar": "^5.26"
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
                "source": "https://github.com/phpDocumentor/ReflectionDocBlock/tree/5.6.6"
            },
            "time": "2025-12-22T21:13:58+00:00"
        },
        {
            "name": "phpdocumentor/type-resolver",
            "version": "1.12.0",
            "source": {
                "type": "git",
                "url": "https://github.com/phpDocumentor/TypeResolver.git",
                "reference": "92a98ada2b93d9b201a613cb5a33584dde25f195"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/phpDocumentor/TypeResolver/zipball/92a98ada2b93d9b201a613cb5a33584dde25f195",
                "reference": "92a98ada2b93d9b201a613cb5a33584dde25f195",
                "shasum": ""
            },
            "require": {
                "doctrine/deprecations": "^1.0",
                "php": "^7.3 || ^8.0",
                "phpdocumentor/reflection-common": "^2.0",
                "phpstan/phpdoc-parser": "^1.18|^2.0"
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
                "source": "https://github.com/phpDocumentor/TypeResolver/tree/1.12.0"
            },
            "time": "2025-11-21T15:09:14+00:00"
        },
        {
            "name": "phpstan/phpdoc-parser",
            "version": "2.3.2",
            "source": {
                "type": "git",
                "url": "https://github.com/phpstan/phpdoc-parser.git",
                "reference": "a004701b11273a26cd7955a61d67a7f1e525a45a"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/phpstan/phpdoc-parser/zipball/a004701b11273a26cd7955a61d67a7f1e525a45a",
                "reference": "a004701b11273a26cd7955a61d67a7f1e525a45a",
                "shasum": ""
            },
            "require": {
                "php": "^7.4 || ^8.0"
            },
            "require-dev": {
                "doctrine/annotations": "^2.0",
                "nikic/php-parser": "^5.3.0",
                "php-parallel-lint/php-parallel-lint": "^1.2",
                "phpstan/extension-installer": "^1.0",
                "phpstan/phpstan": "^2.0",
                "phpstan/phpstan-phpunit": "^2.0",
                "phpstan/phpstan-strict-rules": "^2.0",
                "phpunit/phpunit": "^9.6",
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
                "source": "https://github.com/phpstan/phpdoc-parser/tree/2.3.2"
            },
            "time": "2026-01-25T14:56:51+00:00"
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
            "version": "3.0.2",
            "source": {
                "type": "git",
                "url": "https://github.com/php-fig/log.git",
                "reference": "f16e1d5863e37f8d8c2a01719f5b34baa2b714d3"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/php-fig/log/zipball/f16e1d5863e37f8d8c2a01719f5b34baa2b714d3",
                "reference": "f16e1d5863e37f8d8c2a01719f5b34baa2b714d3",
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
                "source": "https://github.com/php-fig/log/tree/3.0.2"
            },
            "time": "2024-09-11T13:17:53+00:00"
        },
        {
            "name": "ramsey/collection",
            "version": "2.1.1",
            "source": {
                "type": "git",
                "url": "https://github.com/ramsey/collection.git",
                "reference": "344572933ad0181accbf4ba763e85a0306a8c5e2"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/ramsey/collection/zipball/344572933ad0181accbf4ba763e85a0306a8c5e2",
                "reference": "344572933ad0181accbf4ba763e85a0306a8c5e2",
                "shasum": ""
            },
            "require": {
                "php": "^8.1"
            },
            "require-dev": {
                "captainhook/plugin-composer": "^5.3",
                "ergebnis/composer-normalize": "^2.45",
                "fakerphp/faker": "^1.24",
                "hamcrest/hamcrest-php": "^2.0",
                "jangregor/phpstan-prophecy": "^2.1",
                "mockery/mockery": "^1.6",
                "php-parallel-lint/php-console-highlighter": "^1.0",
                "php-parallel-lint/php-parallel-lint": "^1.4",
                "phpspec/prophecy-phpunit": "^2.3",
                "phpstan/extension-installer": "^1.4",
                "phpstan/phpstan": "^2.1",
                "phpstan/phpstan-mockery": "^2.0",
                "phpstan/phpstan-phpunit": "^2.0",
                "phpunit/phpunit": "^10.5",
                "ramsey/coding-standard": "^2.3",
                "ramsey/conventional-commits": "^1.6",
                "roave/security-advisories": "dev-latest"
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
                "source": "https://github.com/ramsey/collection/tree/2.1.1"
            },
            "time": "2025-03-22T05:38:12+00:00"
        },
        {
            "name": "ramsey/uuid",
            "version": "4.9.2",
            "source": {
                "type": "git",
                "url": "https://github.com/ramsey/uuid.git",
                "reference": "8429c78ca35a09f27565311b98101e2826affde0"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/ramsey/uuid/zipball/8429c78ca35a09f27565311b98101e2826affde0",
                "reference": "8429c78ca35a09f27565311b98101e2826affde0",
                "shasum": ""
            },
            "require": {
                "brick/math": "^0.8.16 || ^0.9 || ^0.10 || ^0.11 || ^0.12 || ^0.13 || ^0.14",
                "php": "^8.0",
                "ramsey/collection": "^1.2 || ^2.0"
            },
            "replace": {
                "rhumsaa/uuid": "self.version"
            },
            "require-dev": {
                "captainhook/captainhook": "^5.25",
                "captainhook/plugin-composer": "^5.3",
                "dealerdirect/phpcodesniffer-composer-installer": "^1.0",
                "ergebnis/composer-normalize": "^2.47",
                "mockery/mockery": "^1.6",
                "paragonie/random-lib": "^2",
                "php-mock/php-mock": "^2.6",
                "php-mock/php-mock-mockery": "^1.5",
                "php-parallel-lint/php-parallel-lint": "^1.4.0",
                "phpbench/phpbench": "^1.2.14",
                "phpstan/extension-installer": "^1.4",
                "phpstan/phpstan": "^2.1",
                "phpstan/phpstan-mockery": "^2.0",
                "phpstan/phpstan-phpunit": "^2.0",
                "phpunit/phpunit": "^9.6",
                "slevomat/coding-standard": "^8.18",
                "squizlabs/php_codesniffer": "^3.13"
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
                "source": "https://github.com/ramsey/uuid/tree/4.9.2"
            },
            "time": "2025-12-14T04:43:48+00:00"
        },
        {
            "name": "ramsey/uuid-doctrine",
            "version": "2.1.0",
            "source": {
                "type": "git",
                "url": "https://github.com/ramsey/uuid-doctrine.git",
                "reference": "491e1bfa4d9d81e52a60470fa92c871f7eef919e"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/ramsey/uuid-doctrine/zipball/491e1bfa4d9d81e52a60470fa92c871f7eef919e",
                "reference": "491e1bfa4d9d81e52a60470fa92c871f7eef919e",
                "shasum": ""
            },
            "require": {
                "doctrine/dbal": "^2.8 || ^3.0 || ^4.0",
                "php": "^8.1",
                "ramsey/uuid": "^3.9.7 || ^4.0"
            },
            "require-dev": {
                "captainhook/plugin-composer": "^5.3",
                "doctrine/orm": "^2.5 || ^3.0",
                "ergebnis/composer-normalize": "^2.28.3",
                "mockery/mockery": "^1.5",
                "php-parallel-lint/php-console-highlighter": "^1.0",
                "php-parallel-lint/php-parallel-lint": "^1.3",
                "phpcsstandards/phpcsutils": "^1.0.0-alpha4",
                "phpstan/extension-installer": "^1.2",
                "phpstan/phpstan": "^1.9",
                "phpstan/phpstan-mockery": "^1.1",
                "phpstan/phpstan-phpunit": "^1.3",
                "phpunit/phpunit": "^10.5",
                "ramsey/coding-standard": "^2.0.3",
                "ramsey/conventional-commits": "^1.3"
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
                    "Ramsey\\Uuid\\Doctrine\\": "src/"
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
            "description": "Use ramsey/uuid as a Doctrine field type.",
            "keywords": [
                "database",
                "doctrine",
                "guid",
                "identifier",
                "uuid"
            ],
            "support": {
                "issues": "https://github.com/ramsey/uuid-doctrine/issues",
                "source": "https://github.com/ramsey/uuid-doctrine/tree/2.1.0"
            },
            "funding": [
                {
                    "url": "https://github.com/ramsey",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/ramsey/uuid-doctrine",
                    "type": "tidelift"
                }
            ],
            "time": "2024-05-27T00:00:21+00:00"
        },
        {
            "name": "react/promise",
            "version": "v3.3.0",
            "source": {
                "type": "git",
                "url": "https://github.com/reactphp/promise.git",
                "reference": "23444f53a813a3296c1368bb104793ce8d88f04a"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/reactphp/promise/zipball/23444f53a813a3296c1368bb104793ce8d88f04a",
                "reference": "23444f53a813a3296c1368bb104793ce8d88f04a",
                "shasum": ""
            },
            "require": {
                "php": ">=7.1.0"
            },
            "require-dev": {
                "phpstan/phpstan": "1.12.28 || 1.4.10",
                "phpunit/phpunit": "^9.6 || ^7.5"
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
                "source": "https://github.com/reactphp/promise/tree/v3.3.0"
            },
            "funding": [
                {
                    "url": "https://opencollective.com/reactphp",
                    "type": "open_collective"
                }
            ],
            "time": "2025-08-19T18:57:03+00:00"
        },
        {
            "name": "symfony/amqp-messenger",
            "version": "v7.4.4",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/amqp-messenger.git",
                "reference": "a075581813717913141d7c60081fc072d7be1540"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/amqp-messenger/zipball/a075581813717913141d7c60081fc072d7be1540",
                "reference": "a075581813717913141d7c60081fc072d7be1540",
                "shasum": ""
            },
            "require": {
                "ext-amqp": "*",
                "php": ">=8.2",
                "symfony/messenger": "^7.3|^8.0"
            },
            "require-dev": {
                "symfony/event-dispatcher": "^6.4|^7.0|^8.0",
                "symfony/process": "^6.4|^7.0|^8.0",
                "symfony/property-access": "^6.4|^7.0|^8.0",
                "symfony/serializer": "^6.4|^7.0|^8.0"
            },
            "type": "symfony-messenger-bridge",
            "autoload": {
                "psr-4": {
                    "Symfony\\Component\\Messenger\\Bridge\\Amqp\\": ""
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
            "description": "Symfony AMQP extension Messenger Bridge",
            "homepage": "https://symfony.com",
            "support": {
                "source": "https://github.com/symfony/amqp-messenger/tree/v7.4.4"
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
                    "url": "https://github.com/nicolas-grekas",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2026-01-08T14:50:10+00:00"
        },
        {
            "name": "symfony/asset",
            "version": "v7.4.4",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/asset.git",
                "reference": "a6f49cf087a1fcfe7130b9b604a8a2b878b06c40"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/asset/zipball/a6f49cf087a1fcfe7130b9b604a8a2b878b06c40",
                "reference": "a6f49cf087a1fcfe7130b9b604a8a2b878b06c40",
                "shasum": ""
            },
            "require": {
                "php": ">=8.2"
            },
            "conflict": {
                "symfony/http-foundation": "<6.4"
            },
            "require-dev": {
                "symfony/http-client": "^6.4|^7.0|^8.0",
                "symfony/http-foundation": "^6.4|^7.0|^8.0",
                "symfony/http-kernel": "^6.4|^7.0|^8.0"
            },
            "type": "library",
            "autoload": {
                "psr-4": {
                    "Symfony\\Component\\Asset\\": ""
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
            "description": "Manages URL generation and versioning of web assets such as CSS stylesheets, JavaScript files and image files",
            "homepage": "https://symfony.com",
            "support": {
                "source": "https://github.com/symfony/asset/tree/v7.4.4"
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
                    "url": "https://github.com/nicolas-grekas",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2026-01-13T10:40:19+00:00"
        },
        {
            "name": "symfony/cache",
            "version": "v7.4.5",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/cache.git",
                "reference": "8dde98d5a4123b53877aca493f9be57b333f14bd"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/cache/zipball/8dde98d5a4123b53877aca493f9be57b333f14bd",
                "reference": "8dde98d5a4123b53877aca493f9be57b333f14bd",
                "shasum": ""
            },
            "require": {
                "php": ">=8.2",
                "psr/cache": "^2.0|^3.0",
                "psr/log": "^1.1|^2|^3",
                "symfony/cache-contracts": "^3.6",
                "symfony/deprecation-contracts": "^2.5|^3",
                "symfony/service-contracts": "^2.5|^3",
                "symfony/var-exporter": "^6.4|^7.0|^8.0"
            },
            "conflict": {
                "doctrine/dbal": "<3.6",
                "ext-redis": "<6.1",
                "ext-relay": "<0.12.1",
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
                "symfony/clock": "^6.4|^7.0|^8.0",
                "symfony/config": "^6.4|^7.0|^8.0",
                "symfony/dependency-injection": "^6.4|^7.0|^8.0",
                "symfony/filesystem": "^6.4|^7.0|^8.0",
                "symfony/http-kernel": "^6.4|^7.0|^8.0",
                "symfony/messenger": "^6.4|^7.0|^8.0",
                "symfony/var-dumper": "^6.4|^7.0|^8.0"
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
                "source": "https://github.com/symfony/cache/tree/v7.4.5"
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
                    "url": "https://github.com/nicolas-grekas",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2026-01-27T16:16:02+00:00"
        },
        {
            "name": "symfony/cache-contracts",
            "version": "v3.6.0",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/cache-contracts.git",
                "reference": "5d68a57d66910405e5c0b63d6f0af941e66fc868"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/cache-contracts/zipball/5d68a57d66910405e5c0b63d6f0af941e66fc868",
                "reference": "5d68a57d66910405e5c0b63d6f0af941e66fc868",
                "shasum": ""
            },
            "require": {
                "php": ">=8.1",
                "psr/cache": "^3.0"
            },
            "type": "library",
            "extra": {
                "thanks": {
                    "url": "https://github.com/symfony/contracts",
                    "name": "symfony/contracts"
                },
                "branch-alias": {
                    "dev-main": "3.6-dev"
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
                "source": "https://github.com/symfony/cache-contracts/tree/v3.6.0"
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
            "time": "2025-03-13T15:25:07+00:00"
        },
        {
            "name": "symfony/clock",
            "version": "v7.4.0",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/clock.git",
                "reference": "9169f24776edde469914c1e7a1442a50f7a4e110"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/clock/zipball/9169f24776edde469914c1e7a1442a50f7a4e110",
                "reference": "9169f24776edde469914c1e7a1442a50f7a4e110",
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
                "source": "https://github.com/symfony/clock/tree/v7.4.0"
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
                    "url": "https://github.com/nicolas-grekas",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2025-11-12T15:39:26+00:00"
        },
        {
            "name": "symfony/config",
            "version": "v7.4.4",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/config.git",
                "reference": "4275b53b8ab0cf37f48bf273dc2285c8178efdfb"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/config/zipball/4275b53b8ab0cf37f48bf273dc2285c8178efdfb",
                "reference": "4275b53b8ab0cf37f48bf273dc2285c8178efdfb",
                "shasum": ""
            },
            "require": {
                "php": ">=8.2",
                "symfony/deprecation-contracts": "^2.5|^3",
                "symfony/filesystem": "^7.1|^8.0",
                "symfony/polyfill-ctype": "~1.8"
            },
            "conflict": {
                "symfony/finder": "<6.4",
                "symfony/service-contracts": "<2.5"
            },
            "require-dev": {
                "symfony/event-dispatcher": "^6.4|^7.0|^8.0",
                "symfony/finder": "^6.4|^7.0|^8.0",
                "symfony/messenger": "^6.4|^7.0|^8.0",
                "symfony/service-contracts": "^2.5|^3",
                "symfony/yaml": "^6.4|^7.0|^8.0"
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
                "source": "https://github.com/symfony/config/tree/v7.4.4"
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
                    "url": "https://github.com/nicolas-grekas",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2026-01-13T11:36:38+00:00"
        },
        {
            "name": "symfony/console",
            "version": "v7.4.4",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/console.git",
                "reference": "41e38717ac1dd7a46b6bda7d6a82af2d98a78894"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/console/zipball/41e38717ac1dd7a46b6bda7d6a82af2d98a78894",
                "reference": "41e38717ac1dd7a46b6bda7d6a82af2d98a78894",
                "shasum": ""
            },
            "require": {
                "php": ">=8.2",
                "symfony/deprecation-contracts": "^2.5|^3",
                "symfony/polyfill-mbstring": "~1.0",
                "symfony/service-contracts": "^2.5|^3",
                "symfony/string": "^7.2|^8.0"
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
                "symfony/config": "^6.4|^7.0|^8.0",
                "symfony/dependency-injection": "^6.4|^7.0|^8.0",
                "symfony/event-dispatcher": "^6.4|^7.0|^8.0",
                "symfony/http-foundation": "^6.4|^7.0|^8.0",
                "symfony/http-kernel": "^6.4|^7.0|^8.0",
                "symfony/lock": "^6.4|^7.0|^8.0",
                "symfony/messenger": "^6.4|^7.0|^8.0",
                "symfony/process": "^6.4|^7.0|^8.0",
                "symfony/stopwatch": "^6.4|^7.0|^8.0",
                "symfony/var-dumper": "^6.4|^7.0|^8.0"
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
                "source": "https://github.com/symfony/console/tree/v7.4.4"
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
                    "url": "https://github.com/nicolas-grekas",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2026-01-13T11:36:38+00:00"
        },
        {
            "name": "symfony/dependency-injection",
            "version": "v7.4.5",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/dependency-injection.git",
                "reference": "76a02cddca45a5254479ad68f9fa274ead0a7ef2"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/dependency-injection/zipball/76a02cddca45a5254479ad68f9fa274ead0a7ef2",
                "reference": "76a02cddca45a5254479ad68f9fa274ead0a7ef2",
                "shasum": ""
            },
            "require": {
                "php": ">=8.2",
                "psr/container": "^1.1|^2.0",
                "symfony/deprecation-contracts": "^2.5|^3",
                "symfony/service-contracts": "^3.6",
                "symfony/var-exporter": "^6.4.20|^7.2.5|^8.0"
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
                "symfony/config": "^6.4|^7.0|^8.0",
                "symfony/expression-language": "^6.4|^7.0|^8.0",
                "symfony/yaml": "^6.4|^7.0|^8.0"
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
                "source": "https://github.com/symfony/dependency-injection/tree/v7.4.5"
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
                    "url": "https://github.com/nicolas-grekas",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2026-01-27T16:16:02+00:00"
        },
        {
            "name": "symfony/deprecation-contracts",
            "version": "v3.6.0",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/deprecation-contracts.git",
                "reference": "63afe740e99a13ba87ec199bb07bbdee937a5b62"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/deprecation-contracts/zipball/63afe740e99a13ba87ec199bb07bbdee937a5b62",
                "reference": "63afe740e99a13ba87ec199bb07bbdee937a5b62",
                "shasum": ""
            },
            "require": {
                "php": ">=8.1"
            },
            "type": "library",
            "extra": {
                "thanks": {
                    "url": "https://github.com/symfony/contracts",
                    "name": "symfony/contracts"
                },
                "branch-alias": {
                    "dev-main": "3.6-dev"
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
                "source": "https://github.com/symfony/deprecation-contracts/tree/v3.6.0"
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
            "time": "2024-09-25T14:21:43+00:00"
        },
        {
            "name": "symfony/doctrine-bridge",
            "version": "v7.4.4",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/doctrine-bridge.git",
                "reference": "3408d9fb7bda6c8db9f3e4099863c9017bcbc62d"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/doctrine-bridge/zipball/3408d9fb7bda6c8db9f3e4099863c9017bcbc62d",
                "reference": "3408d9fb7bda6c8db9f3e4099863c9017bcbc62d",
                "shasum": ""
            },
            "require": {
                "doctrine/event-manager": "^2",
                "doctrine/persistence": "^3.1|^4",
                "php": ">=8.2",
                "symfony/deprecation-contracts": "^2.5|^3",
                "symfony/polyfill-ctype": "~1.8",
                "symfony/polyfill-mbstring": "~1.0",
                "symfony/service-contracts": "^2.5|^3"
            },
            "conflict": {
                "doctrine/collections": "<1.8",
                "doctrine/dbal": "<3.6",
                "doctrine/lexer": "<1.1",
                "doctrine/orm": "<2.15",
                "symfony/cache": "<6.4",
                "symfony/dependency-injection": "<6.4",
                "symfony/form": "<6.4.6|>=7,<7.0.6",
                "symfony/http-foundation": "<6.4",
                "symfony/http-kernel": "<6.4",
                "symfony/lock": "<6.4",
                "symfony/messenger": "<6.4",
                "symfony/property-info": "<6.4",
                "symfony/security-bundle": "<6.4",
                "symfony/security-core": "<6.4",
                "symfony/validator": "<7.4"
            },
            "require-dev": {
                "doctrine/collections": "^1.8|^2.0",
                "doctrine/data-fixtures": "^1.1|^2",
                "doctrine/dbal": "^3.6|^4",
                "doctrine/orm": "^2.15|^3",
                "psr/log": "^1|^2|^3",
                "symfony/cache": "^6.4|^7.0|^8.0",
                "symfony/config": "^6.4|^7.0|^8.0",
                "symfony/dependency-injection": "^6.4|^7.0|^8.0",
                "symfony/doctrine-messenger": "^6.4|^7.0|^8.0",
                "symfony/expression-language": "^6.4|^7.0|^8.0",
                "symfony/form": "^7.2|^8.0",
                "symfony/http-kernel": "^6.4|^7.0|^8.0",
                "symfony/lock": "^6.4|^7.0|^8.0",
                "symfony/messenger": "^6.4|^7.0|^8.0",
                "symfony/property-access": "^6.4|^7.0|^8.0",
                "symfony/property-info": "^6.4|^7.0|^8.0",
                "symfony/security-core": "^6.4|^7.0|^8.0",
                "symfony/stopwatch": "^6.4|^7.0|^8.0",
                "symfony/translation": "^6.4|^7.0|^8.0",
                "symfony/type-info": "^7.1.8|^8.0",
                "symfony/uid": "^6.4|^7.0|^8.0",
                "symfony/validator": "^7.4|^8.0",
                "symfony/var-dumper": "^6.4|^7.0|^8.0"
            },
            "type": "symfony-bridge",
            "autoload": {
                "psr-4": {
                    "Symfony\\Bridge\\Doctrine\\": ""
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
            "description": "Provides integration for Doctrine with various Symfony components",
            "homepage": "https://symfony.com",
            "support": {
                "source": "https://github.com/symfony/doctrine-bridge/tree/v7.4.4"
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
                    "url": "https://github.com/nicolas-grekas",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2026-01-20T16:42:42+00:00"
        },
        {
            "name": "symfony/error-handler",
            "version": "v7.4.4",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/error-handler.git",
                "reference": "8da531f364ddfee53e36092a7eebbbd0b775f6b8"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/error-handler/zipball/8da531f364ddfee53e36092a7eebbbd0b775f6b8",
                "reference": "8da531f364ddfee53e36092a7eebbbd0b775f6b8",
                "shasum": ""
            },
            "require": {
                "php": ">=8.2",
                "psr/log": "^1|^2|^3",
                "symfony/polyfill-php85": "^1.32",
                "symfony/var-dumper": "^6.4|^7.0|^8.0"
            },
            "conflict": {
                "symfony/deprecation-contracts": "<2.5",
                "symfony/http-kernel": "<6.4"
            },
            "require-dev": {
                "symfony/console": "^6.4|^7.0|^8.0",
                "symfony/deprecation-contracts": "^2.5|^3",
                "symfony/http-kernel": "^6.4|^7.0|^8.0",
                "symfony/serializer": "^6.4|^7.0|^8.0",
                "symfony/webpack-encore-bundle": "^1.0|^2.0"
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
                "source": "https://github.com/symfony/error-handler/tree/v7.4.4"
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
                    "url": "https://github.com/nicolas-grekas",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2026-01-20T16:42:42+00:00"
        },
        {
            "name": "symfony/event-dispatcher",
            "version": "v7.4.4",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/event-dispatcher.git",
                "reference": "dc2c0eba1af673e736bb851d747d266108aea746"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/event-dispatcher/zipball/dc2c0eba1af673e736bb851d747d266108aea746",
                "reference": "dc2c0eba1af673e736bb851d747d266108aea746",
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
                "symfony/config": "^6.4|^7.0|^8.0",
                "symfony/dependency-injection": "^6.4|^7.0|^8.0",
                "symfony/error-handler": "^6.4|^7.0|^8.0",
                "symfony/expression-language": "^6.4|^7.0|^8.0",
                "symfony/framework-bundle": "^6.4|^7.0|^8.0",
                "symfony/http-foundation": "^6.4|^7.0|^8.0",
                "symfony/service-contracts": "^2.5|^3",
                "symfony/stopwatch": "^6.4|^7.0|^8.0"
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
                "source": "https://github.com/symfony/event-dispatcher/tree/v7.4.4"
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
                    "url": "https://github.com/nicolas-grekas",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2026-01-05T11:45:34+00:00"
        },
        {
            "name": "symfony/event-dispatcher-contracts",
            "version": "v3.6.0",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/event-dispatcher-contracts.git",
                "reference": "59eb412e93815df44f05f342958efa9f46b1e586"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/event-dispatcher-contracts/zipball/59eb412e93815df44f05f342958efa9f46b1e586",
                "reference": "59eb412e93815df44f05f342958efa9f46b1e586",
                "shasum": ""
            },
            "require": {
                "php": ">=8.1",
                "psr/event-dispatcher": "^1"
            },
            "type": "library",
            "extra": {
                "thanks": {
                    "url": "https://github.com/symfony/contracts",
                    "name": "symfony/contracts"
                },
                "branch-alias": {
                    "dev-main": "3.6-dev"
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
                "source": "https://github.com/symfony/event-dispatcher-contracts/tree/v3.6.0"
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
            "time": "2024-09-25T14:21:43+00:00"
        },
        {
            "name": "symfony/filesystem",
            "version": "v7.4.0",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/filesystem.git",
                "reference": "d551b38811096d0be9c4691d406991b47c0c630a"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/filesystem/zipball/d551b38811096d0be9c4691d406991b47c0c630a",
                "reference": "d551b38811096d0be9c4691d406991b47c0c630a",
                "shasum": ""
            },
            "require": {
                "php": ">=8.2",
                "symfony/polyfill-ctype": "~1.8",
                "symfony/polyfill-mbstring": "~1.8"
            },
            "require-dev": {
                "symfony/process": "^6.4|^7.0|^8.0"
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
                "source": "https://github.com/symfony/filesystem/tree/v7.4.0"
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
                    "url": "https://github.com/nicolas-grekas",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2025-11-27T13:27:24+00:00"
        },
        {
            "name": "symfony/finder",
            "version": "v7.4.5",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/finder.git",
                "reference": "ad4daa7c38668dcb031e63bc99ea9bd42196a2cb"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/finder/zipball/ad4daa7c38668dcb031e63bc99ea9bd42196a2cb",
                "reference": "ad4daa7c38668dcb031e63bc99ea9bd42196a2cb",
                "shasum": ""
            },
            "require": {
                "php": ">=8.2"
            },
            "require-dev": {
                "symfony/filesystem": "^6.4|^7.0|^8.0"
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
                "source": "https://github.com/symfony/finder/tree/v7.4.5"
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
                    "url": "https://github.com/nicolas-grekas",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2026-01-26T15:07:59+00:00"
        },
        {
            "name": "symfony/flex",
            "version": "v2.10.0",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/flex.git",
                "reference": "9cd384775973eabbf6e8b05784dda279fc67c28d"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/flex/zipball/9cd384775973eabbf6e8b05784dda279fc67c28d",
                "reference": "9cd384775973eabbf6e8b05784dda279fc67c28d",
                "shasum": ""
            },
            "require": {
                "composer-plugin-api": "^2.1",
                "php": ">=8.1"
            },
            "conflict": {
                "composer/semver": "<1.7.2",
                "symfony/dotenv": "<5.4"
            },
            "require-dev": {
                "composer/composer": "^2.1",
                "symfony/dotenv": "^6.4|^7.4|^8.0",
                "symfony/filesystem": "^6.4|^7.4|^8.0",
                "symfony/phpunit-bridge": "^6.4|^7.4|^8.0",
                "symfony/process": "^6.4|^7.4|^8.0"
            },
            "type": "composer-plugin",
            "extra": {
                "class": "Symfony\\Flex\\Flex"
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Flex\\": "src"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Fabien Potencier",
                    "email": "fabien.potencier@gmail.com"
                }
            ],
            "description": "Composer plugin for Symfony",
            "support": {
                "issues": "https://github.com/symfony/flex/issues",
                "source": "https://github.com/symfony/flex/tree/v2.10.0"
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
                    "url": "https://github.com/nicolas-grekas",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2025-11-16T09:38:19+00:00"
        },
        {
            "name": "symfony/framework-bundle",
            "version": "v7.4.5",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/framework-bundle.git",
                "reference": "dcf89ca6712d9e1b5d3f14dea0e1c2685a05d1cd"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/framework-bundle/zipball/dcf89ca6712d9e1b5d3f14dea0e1c2685a05d1cd",
                "reference": "dcf89ca6712d9e1b5d3f14dea0e1c2685a05d1cd",
                "shasum": ""
            },
            "require": {
                "composer-runtime-api": ">=2.1",
                "ext-xml": "*",
                "php": ">=8.2",
                "symfony/cache": "^6.4.12|^7.0|^8.0",
                "symfony/config": "^7.4.4|^8.0.4",
                "symfony/dependency-injection": "^7.4.4|^8.0.4",
                "symfony/deprecation-contracts": "^2.5|^3",
                "symfony/error-handler": "^7.3|^8.0",
                "symfony/event-dispatcher": "^6.4|^7.0|^8.0",
                "symfony/filesystem": "^7.1|^8.0",
                "symfony/finder": "^6.4|^7.0|^8.0",
                "symfony/http-foundation": "^7.4|^8.0",
                "symfony/http-kernel": "^7.4|^8.0",
                "symfony/polyfill-mbstring": "~1.0",
                "symfony/polyfill-php85": "^1.32",
                "symfony/routing": "^7.4|^8.0"
            },
            "conflict": {
                "doctrine/persistence": "<1.3",
                "phpdocumentor/reflection-docblock": "<5.2|>=6",
                "phpdocumentor/type-resolver": "<1.5.1",
                "symfony/asset": "<6.4",
                "symfony/asset-mapper": "<6.4",
                "symfony/clock": "<6.4",
                "symfony/console": "<6.4",
                "symfony/dom-crawler": "<6.4",
                "symfony/dotenv": "<6.4",
                "symfony/form": "<7.4",
                "symfony/http-client": "<6.4",
                "symfony/lock": "<6.4",
                "symfony/mailer": "<6.4",
                "symfony/messenger": "<7.4",
                "symfony/mime": "<6.4",
                "symfony/property-access": "<6.4",
                "symfony/property-info": "<6.4",
                "symfony/runtime": "<6.4.13|>=7.0,<7.1.6",
                "symfony/scheduler": "<6.4.4|>=7.0.0,<7.0.4",
                "symfony/security-core": "<6.4",
                "symfony/security-csrf": "<7.2",
                "symfony/serializer": "<7.2.5",
                "symfony/stopwatch": "<6.4",
                "symfony/translation": "<7.3",
                "symfony/twig-bridge": "<6.4",
                "symfony/twig-bundle": "<6.4",
                "symfony/validator": "<6.4",
                "symfony/web-profiler-bundle": "<6.4",
                "symfony/webhook": "<7.2",
                "symfony/workflow": "<7.4"
            },
            "require-dev": {
                "doctrine/persistence": "^1.3|^2|^3",
                "dragonmantank/cron-expression": "^3.1",
                "phpdocumentor/reflection-docblock": "^5.2",
                "seld/jsonlint": "^1.10",
                "symfony/asset": "^6.4|^7.0|^8.0",
                "symfony/asset-mapper": "^6.4|^7.0|^8.0",
                "symfony/browser-kit": "^6.4|^7.0|^8.0",
                "symfony/clock": "^6.4|^7.0|^8.0",
                "symfony/console": "^6.4|^7.0|^8.0",
                "symfony/css-selector": "^6.4|^7.0|^8.0",
                "symfony/dom-crawler": "^6.4|^7.0|^8.0",
                "symfony/dotenv": "^6.4|^7.0|^8.0",
                "symfony/expression-language": "^6.4|^7.0|^8.0",
                "symfony/form": "^7.4|^8.0",
                "symfony/html-sanitizer": "^6.4|^7.0|^8.0",
                "symfony/http-client": "^6.4|^7.0|^8.0",
                "symfony/json-streamer": "^7.3|^8.0",
                "symfony/lock": "^6.4|^7.0|^8.0",
                "symfony/mailer": "^6.4|^7.0|^8.0",
                "symfony/messenger": "^7.4|^8.0",
                "symfony/mime": "^6.4|^7.0|^8.0",
                "symfony/notifier": "^6.4|^7.0|^8.0",
                "symfony/object-mapper": "^7.3|^8.0",
                "symfony/polyfill-intl-icu": "~1.0",
                "symfony/process": "^6.4|^7.0|^8.0",
                "symfony/property-info": "^6.4|^7.0|^8.0",
                "symfony/rate-limiter": "^6.4|^7.0|^8.0",
                "symfony/runtime": "^6.4.13|^7.1.6|^8.0",
                "symfony/scheduler": "^6.4.4|^7.0.4|^8.0",
                "symfony/security-bundle": "^6.4|^7.0|^8.0",
                "symfony/semaphore": "^6.4|^7.0|^8.0",
                "symfony/serializer": "^7.2.5|^8.0",
                "symfony/stopwatch": "^6.4|^7.0|^8.0",
                "symfony/string": "^6.4|^7.0|^8.0",
                "symfony/translation": "^7.3|^8.0",
                "symfony/twig-bundle": "^6.4|^7.0|^8.0",
                "symfony/type-info": "^7.1.8|^8.0",
                "symfony/uid": "^6.4|^7.0|^8.0",
                "symfony/validator": "^7.4|^8.0",
                "symfony/web-link": "^6.4|^7.0|^8.0",
                "symfony/webhook": "^7.2|^8.0",
                "symfony/workflow": "^7.4|^8.0",
                "symfony/yaml": "^7.3|^8.0",
                "twig/twig": "^3.12"
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
                "source": "https://github.com/symfony/framework-bundle/tree/v7.4.5"
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
                    "url": "https://github.com/nicolas-grekas",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2026-01-27T08:59:58+00:00"
        },
        {
            "name": "symfony/http-foundation",
            "version": "v7.4.5",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/http-foundation.git",
                "reference": "446d0db2b1f21575f1284b74533e425096abdfb6"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/http-foundation/zipball/446d0db2b1f21575f1284b74533e425096abdfb6",
                "reference": "446d0db2b1f21575f1284b74533e425096abdfb6",
                "shasum": ""
            },
            "require": {
                "php": ">=8.2",
                "symfony/deprecation-contracts": "^2.5|^3",
                "symfony/polyfill-mbstring": "^1.1"
            },
            "conflict": {
                "doctrine/dbal": "<3.6",
                "symfony/cache": "<6.4.12|>=7.0,<7.1.5"
            },
            "require-dev": {
                "doctrine/dbal": "^3.6|^4",
                "predis/predis": "^1.1|^2.0",
                "symfony/cache": "^6.4.12|^7.1.5|^8.0",
                "symfony/clock": "^6.4|^7.0|^8.0",
                "symfony/dependency-injection": "^6.4|^7.0|^8.0",
                "symfony/expression-language": "^6.4|^7.0|^8.0",
                "symfony/http-kernel": "^6.4|^7.0|^8.0",
                "symfony/mime": "^6.4|^7.0|^8.0",
                "symfony/rate-limiter": "^6.4|^7.0|^8.0"
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
                "source": "https://github.com/symfony/http-foundation/tree/v7.4.5"
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
                    "url": "https://github.com/nicolas-grekas",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2026-01-27T16:16:02+00:00"
        },
        {
            "name": "symfony/http-kernel",
            "version": "v7.4.5",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/http-kernel.git",
                "reference": "229eda477017f92bd2ce7615d06222ec0c19e82a"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/http-kernel/zipball/229eda477017f92bd2ce7615d06222ec0c19e82a",
                "reference": "229eda477017f92bd2ce7615d06222ec0c19e82a",
                "shasum": ""
            },
            "require": {
                "php": ">=8.2",
                "psr/log": "^1|^2|^3",
                "symfony/deprecation-contracts": "^2.5|^3",
                "symfony/error-handler": "^6.4|^7.0|^8.0",
                "symfony/event-dispatcher": "^7.3|^8.0",
                "symfony/http-foundation": "^7.4|^8.0",
                "symfony/polyfill-ctype": "^1.8"
            },
            "conflict": {
                "symfony/browser-kit": "<6.4",
                "symfony/cache": "<6.4",
                "symfony/config": "<6.4",
                "symfony/console": "<6.4",
                "symfony/dependency-injection": "<6.4",
                "symfony/doctrine-bridge": "<6.4",
                "symfony/flex": "<2.10",
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
                "twig/twig": "<3.12"
            },
            "provide": {
                "psr/log-implementation": "1.0|2.0|3.0"
            },
            "require-dev": {
                "psr/cache": "^1.0|^2.0|^3.0",
                "symfony/browser-kit": "^6.4|^7.0|^8.0",
                "symfony/clock": "^6.4|^7.0|^8.0",
                "symfony/config": "^6.4|^7.0|^8.0",
                "symfony/console": "^6.4|^7.0|^8.0",
                "symfony/css-selector": "^6.4|^7.0|^8.0",
                "symfony/dependency-injection": "^6.4|^7.0|^8.0",
                "symfony/dom-crawler": "^6.4|^7.0|^8.0",
                "symfony/expression-language": "^6.4|^7.0|^8.0",
                "symfony/finder": "^6.4|^7.0|^8.0",
                "symfony/http-client-contracts": "^2.5|^3",
                "symfony/process": "^6.4|^7.0|^8.0",
                "symfony/property-access": "^7.1|^8.0",
                "symfony/routing": "^6.4|^7.0|^8.0",
                "symfony/serializer": "^7.1|^8.0",
                "symfony/stopwatch": "^6.4|^7.0|^8.0",
                "symfony/translation": "^6.4|^7.0|^8.0",
                "symfony/translation-contracts": "^2.5|^3",
                "symfony/uid": "^6.4|^7.0|^8.0",
                "symfony/validator": "^6.4|^7.0|^8.0",
                "symfony/var-dumper": "^6.4|^7.0|^8.0",
                "symfony/var-exporter": "^6.4|^7.0|^8.0",
                "twig/twig": "^3.12"
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
                "source": "https://github.com/symfony/http-kernel/tree/v7.4.5"
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
                    "url": "https://github.com/nicolas-grekas",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2026-01-28T10:33:42+00:00"
        },
        {
            "name": "symfony/messenger",
            "version": "v7.4.4",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/messenger.git",
                "reference": "0a39e1b256f280762293f2f441e430c8baf74f9c"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/messenger/zipball/0a39e1b256f280762293f2f441e430c8baf74f9c",
                "reference": "0a39e1b256f280762293f2f441e430c8baf74f9c",
                "shasum": ""
            },
            "require": {
                "php": ">=8.2",
                "psr/log": "^1|^2|^3",
                "symfony/clock": "^6.4|^7.0|^8.0",
                "symfony/deprecation-contracts": "^2.5|^3"
            },
            "conflict": {
                "symfony/console": "<7.2",
                "symfony/event-dispatcher": "<6.4",
                "symfony/event-dispatcher-contracts": "<2.5",
                "symfony/framework-bundle": "<6.4",
                "symfony/http-kernel": "<7.3",
                "symfony/lock": "<7.4",
                "symfony/serializer": "<6.4.32|>=7.3,<7.3.10|>=7.4,<7.4.4|>=8.0,<8.0.4"
            },
            "require-dev": {
                "psr/cache": "^1.0|^2.0|^3.0",
                "symfony/console": "^7.2|^8.0",
                "symfony/dependency-injection": "^6.4|^7.0|^8.0",
                "symfony/event-dispatcher": "^6.4|^7.0|^8.0",
                "symfony/http-kernel": "^7.3|^8.0",
                "symfony/lock": "^7.4|^8.0",
                "symfony/process": "^6.4|^7.0|^8.0",
                "symfony/property-access": "^6.4|^7.0|^8.0",
                "symfony/rate-limiter": "^6.4|^7.0|^8.0",
                "symfony/routing": "^6.4|^7.0|^8.0",
                "symfony/serializer": "^6.4.32|~7.3.10|^7.4.4|^8.0.4",
                "symfony/service-contracts": "^2.5|^3",
                "symfony/stopwatch": "^6.4|^7.0|^8.0",
                "symfony/validator": "^6.4|^7.0|^8.0",
                "symfony/var-dumper": "^6.4|^7.0|^8.0"
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
                "source": "https://github.com/symfony/messenger/tree/v7.4.4"
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
                    "url": "https://github.com/nicolas-grekas",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2026-01-08T14:50:10+00:00"
        },
        {
            "name": "symfony/monolog-bridge",
            "version": "v7.4.4",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/monolog-bridge.git",
                "reference": "9c34e8170b09f062a9a38880a3cb58ee35cb7fd4"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/monolog-bridge/zipball/9c34e8170b09f062a9a38880a3cb58ee35cb7fd4",
                "reference": "9c34e8170b09f062a9a38880a3cb58ee35cb7fd4",
                "shasum": ""
            },
            "require": {
                "monolog/monolog": "^3",
                "php": ">=8.2",
                "symfony/deprecation-contracts": "^2.5|^3",
                "symfony/http-kernel": "^6.4|^7.0|^8.0",
                "symfony/service-contracts": "^2.5|^3"
            },
            "conflict": {
                "symfony/console": "<6.4",
                "symfony/http-foundation": "<6.4",
                "symfony/security-core": "<6.4"
            },
            "require-dev": {
                "symfony/console": "^6.4|^7.0|^8.0",
                "symfony/http-client": "^6.4|^7.0|^8.0",
                "symfony/mailer": "^6.4|^7.0|^8.0",
                "symfony/messenger": "^6.4|^7.0|^8.0",
                "symfony/mime": "^6.4|^7.0|^8.0",
                "symfony/security-core": "^6.4|^7.0|^8.0",
                "symfony/var-dumper": "^6.4|^7.0|^8.0"
            },
            "type": "symfony-bridge",
            "autoload": {
                "psr-4": {
                    "Symfony\\Bridge\\Monolog\\": ""
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
            "description": "Provides integration for Monolog with various Symfony components",
            "homepage": "https://symfony.com",
            "support": {
                "source": "https://github.com/symfony/monolog-bridge/tree/v7.4.4"
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
                    "url": "https://github.com/nicolas-grekas",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2026-01-07T11:35:36+00:00"
        },
        {
            "name": "symfony/monolog-bundle",
            "version": "v3.11.1",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/monolog-bundle.git",
                "reference": "0e675a6e08f791ef960dc9c7e392787111a3f0c1"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/monolog-bundle/zipball/0e675a6e08f791ef960dc9c7e392787111a3f0c1",
                "reference": "0e675a6e08f791ef960dc9c7e392787111a3f0c1",
                "shasum": ""
            },
            "require": {
                "composer-runtime-api": "^2.0",
                "monolog/monolog": "^1.25.1 || ^2.0 || ^3.0",
                "php": ">=8.1",
                "symfony/config": "^6.4 || ^7.0",
                "symfony/dependency-injection": "^6.4 || ^7.0",
                "symfony/deprecation-contracts": "^2.5 || ^3.0",
                "symfony/http-kernel": "^6.4 || ^7.0",
                "symfony/monolog-bridge": "^6.4 || ^7.0",
                "symfony/polyfill-php84": "^1.30"
            },
            "require-dev": {
                "symfony/console": "^6.4 || ^7.0",
                "symfony/phpunit-bridge": "^7.3.3",
                "symfony/yaml": "^6.4 || ^7.0"
            },
            "type": "symfony-bundle",
            "autoload": {
                "psr-4": {
                    "Symfony\\Bundle\\MonologBundle\\": "src"
                }
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
            "description": "Symfony MonologBundle",
            "homepage": "https://symfony.com",
            "keywords": [
                "log",
                "logging"
            ],
            "support": {
                "issues": "https://github.com/symfony/monolog-bundle/issues",
                "source": "https://github.com/symfony/monolog-bundle/tree/v3.11.1"
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
                    "url": "https://github.com/nicolas-grekas",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2025-12-08T07:58:26+00:00"
        },
        {
            "name": "symfony/options-resolver",
            "version": "v7.4.0",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/options-resolver.git",
                "reference": "b38026df55197f9e39a44f3215788edf83187b80"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/options-resolver/zipball/b38026df55197f9e39a44f3215788edf83187b80",
                "reference": "b38026df55197f9e39a44f3215788edf83187b80",
                "shasum": ""
            },
            "require": {
                "php": ">=8.2",
                "symfony/deprecation-contracts": "^2.5|^3"
            },
            "type": "library",
            "autoload": {
                "psr-4": {
                    "Symfony\\Component\\OptionsResolver\\": ""
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
            "description": "Provides an improved replacement for the array_replace PHP function",
            "homepage": "https://symfony.com",
            "keywords": [
                "config",
                "configuration",
                "options"
            ],
            "support": {
                "source": "https://github.com/symfony/options-resolver/tree/v7.4.0"
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
                    "url": "https://github.com/nicolas-grekas",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2025-11-12T15:39:26+00:00"
        },
        {
            "name": "symfony/password-hasher",
            "version": "v7.4.4",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/password-hasher.git",
                "reference": "ab8e0ef42483f31c417c82ecfcf7be7b91d784fe"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/password-hasher/zipball/ab8e0ef42483f31c417c82ecfcf7be7b91d784fe",
                "reference": "ab8e0ef42483f31c417c82ecfcf7be7b91d784fe",
                "shasum": ""
            },
            "require": {
                "php": ">=8.2"
            },
            "conflict": {
                "symfony/security-core": "<6.4"
            },
            "require-dev": {
                "symfony/console": "^6.4|^7.0|^8.0",
                "symfony/security-core": "^6.4|^7.0|^8.0"
            },
            "type": "library",
            "autoload": {
                "psr-4": {
                    "Symfony\\Component\\PasswordHasher\\": ""
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
                    "name": "Robin Chalas",
                    "email": "robin.chalas@gmail.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Provides password hashing utilities",
            "homepage": "https://symfony.com",
            "keywords": [
                "hashing",
                "password"
            ],
            "support": {
                "source": "https://github.com/symfony/password-hasher/tree/v7.4.4"
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
                    "url": "https://github.com/nicolas-grekas",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2026-01-01T22:13:48+00:00"
        },
        {
            "name": "symfony/polyfill-ctype",
            "version": "v1.33.0",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/polyfill-ctype.git",
                "reference": "a3cc8b044a6ea513310cbd48ef7333b384945638"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/polyfill-ctype/zipball/a3cc8b044a6ea513310cbd48ef7333b384945638",
                "reference": "a3cc8b044a6ea513310cbd48ef7333b384945638",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2"
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
                    "url": "https://github.com/symfony/polyfill",
                    "name": "symfony/polyfill"
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
                "source": "https://github.com/symfony/polyfill-ctype/tree/v1.33.0"
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
                    "url": "https://github.com/nicolas-grekas",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2024-09-09T11:45:10+00:00"
        },
        {
            "name": "symfony/polyfill-intl-grapheme",
            "version": "v1.33.0",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/polyfill-intl-grapheme.git",
                "reference": "380872130d3a5dd3ace2f4010d95125fde5d5c70"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/polyfill-intl-grapheme/zipball/380872130d3a5dd3ace2f4010d95125fde5d5c70",
                "reference": "380872130d3a5dd3ace2f4010d95125fde5d5c70",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2"
            },
            "suggest": {
                "ext-intl": "For best performance"
            },
            "type": "library",
            "extra": {
                "thanks": {
                    "url": "https://github.com/symfony/polyfill",
                    "name": "symfony/polyfill"
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
                "source": "https://github.com/symfony/polyfill-intl-grapheme/tree/v1.33.0"
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
                    "url": "https://github.com/nicolas-grekas",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2025-06-27T09:58:17+00:00"
        },
        {
            "name": "symfony/polyfill-intl-normalizer",
            "version": "v1.33.0",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/polyfill-intl-normalizer.git",
                "reference": "3833d7255cc303546435cb650316bff708a1c75c"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/polyfill-intl-normalizer/zipball/3833d7255cc303546435cb650316bff708a1c75c",
                "reference": "3833d7255cc303546435cb650316bff708a1c75c",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2"
            },
            "suggest": {
                "ext-intl": "For best performance"
            },
            "type": "library",
            "extra": {
                "thanks": {
                    "url": "https://github.com/symfony/polyfill",
                    "name": "symfony/polyfill"
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
                "source": "https://github.com/symfony/polyfill-intl-normalizer/tree/v1.33.0"
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
                    "url": "https://github.com/nicolas-grekas",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2024-09-09T11:45:10+00:00"
        },
        {
            "name": "symfony/polyfill-mbstring",
            "version": "v1.33.0",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/polyfill-mbstring.git",
                "reference": "6d857f4d76bd4b343eac26d6b539585d2bc56493"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/polyfill-mbstring/zipball/6d857f4d76bd4b343eac26d6b539585d2bc56493",
                "reference": "6d857f4d76bd4b343eac26d6b539585d2bc56493",
                "shasum": ""
            },
            "require": {
                "ext-iconv": "*",
                "php": ">=7.2"
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
                    "url": "https://github.com/symfony/polyfill",
                    "name": "symfony/polyfill"
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
                "source": "https://github.com/symfony/polyfill-mbstring/tree/v1.33.0"
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
                    "url": "https://github.com/nicolas-grekas",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2024-12-23T08:48:59+00:00"
        },
        {
            "name": "symfony/polyfill-php83",
            "version": "v1.33.0",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/polyfill-php83.git",
                "reference": "17f6f9a6b1735c0f163024d959f700cfbc5155e5"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/polyfill-php83/zipball/17f6f9a6b1735c0f163024d959f700cfbc5155e5",
                "reference": "17f6f9a6b1735c0f163024d959f700cfbc5155e5",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2"
            },
            "type": "library",
            "extra": {
                "thanks": {
                    "url": "https://github.com/symfony/polyfill",
                    "name": "symfony/polyfill"
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
                "source": "https://github.com/symfony/polyfill-php83/tree/v1.33.0"
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
                    "url": "https://github.com/nicolas-grekas",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2025-07-08T02:45:35+00:00"
        },
        {
            "name": "symfony/polyfill-php84",
            "version": "v1.33.0",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/polyfill-php84.git",
                "reference": "d8ced4d875142b6a7426000426b8abc631d6b191"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/polyfill-php84/zipball/d8ced4d875142b6a7426000426b8abc631d6b191",
                "reference": "d8ced4d875142b6a7426000426b8abc631d6b191",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2"
            },
            "type": "library",
            "extra": {
                "thanks": {
                    "url": "https://github.com/symfony/polyfill",
                    "name": "symfony/polyfill"
                }
            },
            "autoload": {
                "files": [
                    "bootstrap.php"
                ],
                "psr-4": {
                    "Symfony\\Polyfill\\Php84\\": ""
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
            "description": "Symfony polyfill backporting some PHP 8.4+ features to lower PHP versions",
            "homepage": "https://symfony.com",
            "keywords": [
                "compatibility",
                "polyfill",
                "portable",
                "shim"
            ],
            "support": {
                "source": "https://github.com/symfony/polyfill-php84/tree/v1.33.0"
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
                    "url": "https://github.com/nicolas-grekas",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2025-06-24T13:30:11+00:00"
        },
        {
            "name": "symfony/polyfill-php85",
            "version": "v1.33.0",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/polyfill-php85.git",
                "reference": "d4e5fcd4ab3d998ab16c0db48e6cbb9a01993f91"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/polyfill-php85/zipball/d4e5fcd4ab3d998ab16c0db48e6cbb9a01993f91",
                "reference": "d4e5fcd4ab3d998ab16c0db48e6cbb9a01993f91",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2"
            },
            "type": "library",
            "extra": {
                "thanks": {
                    "url": "https://github.com/symfony/polyfill",
                    "name": "symfony/polyfill"
                }
            },
            "autoload": {
                "files": [
                    "bootstrap.php"
                ],
                "psr-4": {
                    "Symfony\\Polyfill\\Php85\\": ""
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
            "description": "Symfony polyfill backporting some PHP 8.5+ features to lower PHP versions",
            "homepage": "https://symfony.com",
            "keywords": [
                "compatibility",
                "polyfill",
                "portable",
                "shim"
            ],
            "support": {
                "source": "https://github.com/symfony/polyfill-php85/tree/v1.33.0"
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
                    "url": "https://github.com/nicolas-grekas",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2025-06-23T16:12:55+00:00"
        },
        {
            "name": "symfony/property-access",
            "version": "v7.4.4",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/property-access.git",
                "reference": "fa49bf1ca8fce1ba0e2dba4e4658554cfb9364b1"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/property-access/zipball/fa49bf1ca8fce1ba0e2dba4e4658554cfb9364b1",
                "reference": "fa49bf1ca8fce1ba0e2dba4e4658554cfb9364b1",
                "shasum": ""
            },
            "require": {
                "php": ">=8.2",
                "symfony/property-info": "^6.4.32|~7.3.10|^7.4.4|^8.0.4"
            },
            "require-dev": {
                "symfony/cache": "^6.4|^7.0|^8.0",
                "symfony/var-exporter": "^6.4.1|^7.0.1|^8.0"
            },
            "type": "library",
            "autoload": {
                "psr-4": {
                    "Symfony\\Component\\PropertyAccess\\": ""
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
            "description": "Provides functions to read and write from/to an object or array using a simple string notation",
            "homepage": "https://symfony.com",
            "keywords": [
                "access",
                "array",
                "extraction",
                "index",
                "injection",
                "object",
                "property",
                "property-path",
                "reflection"
            ],
            "support": {
                "source": "https://github.com/symfony/property-access/tree/v7.4.4"
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
                    "url": "https://github.com/nicolas-grekas",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2026-01-05T08:47:25+00:00"
        },
        {
            "name": "symfony/property-info",
            "version": "v7.4.5",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/property-info.git",
                "reference": "1c9d326bd69602561e2ea467a16c09b5972eee21"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/property-info/zipball/1c9d326bd69602561e2ea467a16c09b5972eee21",
                "reference": "1c9d326bd69602561e2ea467a16c09b5972eee21",
                "shasum": ""
            },
            "require": {
                "php": ">=8.2",
                "symfony/deprecation-contracts": "^2.5|^3",
                "symfony/string": "^6.4|^7.0|^8.0",
                "symfony/type-info": "~7.3.10|^7.4.4|^8.0.4"
            },
            "conflict": {
                "phpdocumentor/reflection-docblock": "<5.2|>=6",
                "phpdocumentor/type-resolver": "<1.5.1",
                "symfony/cache": "<6.4",
                "symfony/dependency-injection": "<6.4",
                "symfony/serializer": "<6.4"
            },
            "require-dev": {
                "phpdocumentor/reflection-docblock": "^5.2",
                "phpstan/phpdoc-parser": "^1.0|^2.0",
                "symfony/cache": "^6.4|^7.0|^8.0",
                "symfony/dependency-injection": "^6.4|^7.0|^8.0",
                "symfony/serializer": "^6.4|^7.0|^8.0"
            },
            "type": "library",
            "autoload": {
                "psr-4": {
                    "Symfony\\Component\\PropertyInfo\\": ""
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
                    "name": "Kévin Dunglas",
                    "email": "dunglas@gmail.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Extracts information about PHP class' properties using metadata of popular sources",
            "homepage": "https://symfony.com",
            "keywords": [
                "doctrine",
                "phpdoc",
                "property",
                "symfony",
                "type",
                "validator"
            ],
            "support": {
                "source": "https://github.com/symfony/property-info/tree/v7.4.5"
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
                    "url": "https://github.com/nicolas-grekas",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2026-01-27T16:16:02+00:00"
        },
        {
            "name": "symfony/routing",
            "version": "v7.4.4",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/routing.git",
                "reference": "0798827fe2c79caeed41d70b680c2c3507d10147"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/routing/zipball/0798827fe2c79caeed41d70b680c2c3507d10147",
                "reference": "0798827fe2c79caeed41d70b680c2c3507d10147",
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
                "symfony/config": "^6.4|^7.0|^8.0",
                "symfony/dependency-injection": "^6.4|^7.0|^8.0",
                "symfony/expression-language": "^6.4|^7.0|^8.0",
                "symfony/http-foundation": "^6.4|^7.0|^8.0",
                "symfony/yaml": "^6.4|^7.0|^8.0"
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
                "source": "https://github.com/symfony/routing/tree/v7.4.4"
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
                    "url": "https://github.com/nicolas-grekas",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2026-01-12T12:19:02+00:00"
        },
        {
            "name": "symfony/security-bundle",
            "version": "v7.4.4",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/security-bundle.git",
                "reference": "7281b644c76985ddf3927f5e65152b0cc29d175b"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/security-bundle/zipball/7281b644c76985ddf3927f5e65152b0cc29d175b",
                "reference": "7281b644c76985ddf3927f5e65152b0cc29d175b",
                "shasum": ""
            },
            "require": {
                "composer-runtime-api": ">=2.1",
                "ext-xml": "*",
                "php": ">=8.2",
                "symfony/clock": "^6.4|^7.0|^8.0",
                "symfony/config": "^7.4|^8.0",
                "symfony/dependency-injection": "^6.4.11|^7.1.4|^8.0",
                "symfony/deprecation-contracts": "^2.5|^3",
                "symfony/event-dispatcher": "^6.4|^7.0|^8.0",
                "symfony/http-foundation": "^6.4|^7.0|^8.0",
                "symfony/http-kernel": "^6.4.13|^7.1.6|^8.0",
                "symfony/password-hasher": "^6.4|^7.0|^8.0",
                "symfony/security-core": "^7.4|^8.0",
                "symfony/security-csrf": "^6.4|^7.0|^8.0",
                "symfony/security-http": "^7.4|^8.0",
                "symfony/service-contracts": "^2.5|^3"
            },
            "conflict": {
                "symfony/browser-kit": "<6.4",
                "symfony/console": "<6.4",
                "symfony/framework-bundle": "<6.4",
                "symfony/http-client": "<6.4",
                "symfony/ldap": "<6.4",
                "symfony/serializer": "<6.4",
                "symfony/twig-bundle": "<6.4",
                "symfony/validator": "<6.4"
            },
            "require-dev": {
                "symfony/asset": "^6.4|^7.0|^8.0",
                "symfony/browser-kit": "^6.4|^7.0|^8.0",
                "symfony/console": "^6.4|^7.0|^8.0",
                "symfony/css-selector": "^6.4|^7.0|^8.0",
                "symfony/dom-crawler": "^6.4|^7.0|^8.0",
                "symfony/expression-language": "^6.4|^7.0|^8.0",
                "symfony/form": "^6.4|^7.0|^8.0",
                "symfony/framework-bundle": "^6.4.13|^7.1.6|^8.0",
                "symfony/http-client": "^6.4|^7.0|^8.0",
                "symfony/ldap": "^6.4|^7.0|^8.0",
                "symfony/process": "^6.4|^7.0|^8.0",
                "symfony/rate-limiter": "^6.4|^7.0|^8.0",
                "symfony/runtime": "^6.4.13|^7.1.6|^8.0",
                "symfony/serializer": "^6.4|^7.0|^8.0",
                "symfony/translation": "^6.4|^7.0|^8.0",
                "symfony/twig-bridge": "^6.4|^7.0|^8.0",
                "symfony/twig-bundle": "^6.4|^7.0|^8.0",
                "symfony/validator": "^6.4|^7.0|^8.0",
                "symfony/yaml": "^6.4|^7.0|^8.0",
                "twig/twig": "^3.15",
                "web-token/jwt-library": "^3.3.2|^4.0"
            },
            "type": "symfony-bundle",
            "autoload": {
                "psr-4": {
                    "Symfony\\Bundle\\SecurityBundle\\": ""
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
            "description": "Provides a tight integration of the Security component into the Symfony full-stack framework",
            "homepage": "https://symfony.com",
            "support": {
                "source": "https://github.com/symfony/security-bundle/tree/v7.4.4"
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
                    "url": "https://github.com/nicolas-grekas",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2026-01-10T13:56:23+00:00"
        },
        {
            "name": "symfony/security-core",
            "version": "v7.4.4",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/security-core.git",
                "reference": "958a70725a8d669bec6721f4cd318d209712e944"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/security-core/zipball/958a70725a8d669bec6721f4cd318d209712e944",
                "reference": "958a70725a8d669bec6721f4cd318d209712e944",
                "shasum": ""
            },
            "require": {
                "php": ">=8.2",
                "symfony/deprecation-contracts": "^2.5|^3",
                "symfony/event-dispatcher-contracts": "^2.5|^3",
                "symfony/password-hasher": "^6.4|^7.0|^8.0",
                "symfony/service-contracts": "^2.5|^3"
            },
            "conflict": {
                "symfony/dependency-injection": "<6.4",
                "symfony/event-dispatcher": "<6.4",
                "symfony/http-foundation": "<6.4",
                "symfony/ldap": "<6.4",
                "symfony/translation": "<6.4.3|>=7.0,<7.0.3",
                "symfony/validator": "<6.4"
            },
            "require-dev": {
                "psr/cache": "^1.0|^2.0|^3.0",
                "psr/container": "^1.1|^2.0",
                "psr/log": "^1|^2|^3",
                "symfony/cache": "^6.4|^7.0|^8.0",
                "symfony/dependency-injection": "^6.4|^7.0|^8.0",
                "symfony/event-dispatcher": "^6.4|^7.0|^8.0",
                "symfony/expression-language": "^6.4|^7.0|^8.0",
                "symfony/http-foundation": "^6.4|^7.0|^8.0",
                "symfony/ldap": "^6.4|^7.0|^8.0",
                "symfony/string": "^6.4|^7.0|^8.0",
                "symfony/translation": "^6.4.3|^7.0.3|^8.0",
                "symfony/validator": "^6.4|^7.0|^8.0"
            },
            "type": "library",
            "autoload": {
                "psr-4": {
                    "Symfony\\Component\\Security\\Core\\": ""
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
            "description": "Symfony Security Component - Core Library",
            "homepage": "https://symfony.com",
            "support": {
                "source": "https://github.com/symfony/security-core/tree/v7.4.4"
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
                    "url": "https://github.com/nicolas-grekas",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2026-01-14T09:36:49+00:00"
        },
        {
            "name": "symfony/security-csrf",
            "version": "v7.4.4",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/security-csrf.git",
                "reference": "06a2a2f90f355b8b4ec23685fa6ceff8d5dc41cc"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/security-csrf/zipball/06a2a2f90f355b8b4ec23685fa6ceff8d5dc41cc",
                "reference": "06a2a2f90f355b8b4ec23685fa6ceff8d5dc41cc",
                "shasum": ""
            },
            "require": {
                "php": ">=8.2",
                "symfony/security-core": "^6.4|^7.0|^8.0"
            },
            "conflict": {
                "symfony/http-foundation": "<6.4"
            },
            "require-dev": {
                "psr/log": "^1|^2|^3",
                "symfony/http-foundation": "^6.4|^7.0|^8.0",
                "symfony/http-kernel": "^6.4|^7.0|^8.0"
            },
            "type": "library",
            "autoload": {
                "psr-4": {
                    "Symfony\\Component\\Security\\Csrf\\": ""
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
            "description": "Symfony Security Component - CSRF Library",
            "homepage": "https://symfony.com",
            "support": {
                "source": "https://github.com/symfony/security-csrf/tree/v7.4.4"
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
                    "url": "https://github.com/nicolas-grekas",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2026-01-14T10:11:16+00:00"
        },
        {
            "name": "symfony/security-http",
            "version": "v7.4.4",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/security-http.git",
                "reference": "9d41a473637bf5d074c5f5a73177fd9d769407fd"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/security-http/zipball/9d41a473637bf5d074c5f5a73177fd9d769407fd",
                "reference": "9d41a473637bf5d074c5f5a73177fd9d769407fd",
                "shasum": ""
            },
            "require": {
                "php": ">=8.2",
                "symfony/deprecation-contracts": "^2.5|^3",
                "symfony/event-dispatcher": "^6.4|^7.0",
                "symfony/http-foundation": "^6.4|^7.0|^8.0",
                "symfony/http-kernel": "^6.4|^7.0|^8.0",
                "symfony/polyfill-mbstring": "~1.0",
                "symfony/property-access": "^6.4|^7.0|^8.0",
                "symfony/security-core": "^7.3|^8.0",
                "symfony/service-contracts": "^2.5|^3"
            },
            "conflict": {
                "symfony/clock": "<6.4",
                "symfony/http-client-contracts": "<3.0",
                "symfony/security-bundle": "<6.4",
                "symfony/security-csrf": "<6.4"
            },
            "require-dev": {
                "psr/log": "^1|^2|^3",
                "symfony/cache": "^6.4|^7.0|^8.0",
                "symfony/clock": "^6.4|^7.0|^8.0",
                "symfony/expression-language": "^6.4|^7.0|^8.0",
                "symfony/http-client": "^6.4|^7.0|^8.0",
                "symfony/http-client-contracts": "^3.0",
                "symfony/rate-limiter": "^6.4|^7.0|^8.0",
                "symfony/routing": "^6.4|^7.0|^8.0",
                "symfony/security-csrf": "^6.4|^7.0|^8.0",
                "symfony/translation": "^6.4|^7.0|^8.0",
                "web-token/jwt-library": "^3.3.2|^4.0"
            },
            "type": "library",
            "autoload": {
                "psr-4": {
                    "Symfony\\Component\\Security\\Http\\": ""
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
            "description": "Symfony Security Component - HTTP Integration",
            "homepage": "https://symfony.com",
            "support": {
                "source": "https://github.com/symfony/security-http/tree/v7.4.4"
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
                    "url": "https://github.com/nicolas-grekas",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2026-01-14T10:11:16+00:00"
        },
        {
            "name": "symfony/service-contracts",
            "version": "v3.6.1",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/service-contracts.git",
                "reference": "45112560a3ba2d715666a509a0bc9521d10b6c43"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/service-contracts/zipball/45112560a3ba2d715666a509a0bc9521d10b6c43",
                "reference": "45112560a3ba2d715666a509a0bc9521d10b6c43",
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
                "thanks": {
                    "url": "https://github.com/symfony/contracts",
                    "name": "symfony/contracts"
                },
                "branch-alias": {
                    "dev-main": "3.6-dev"
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
                "source": "https://github.com/symfony/service-contracts/tree/v3.6.1"
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
                    "url": "https://github.com/nicolas-grekas",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2025-07-15T11:30:57+00:00"
        },
        {
            "name": "symfony/stopwatch",
            "version": "v7.4.0",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/stopwatch.git",
                "reference": "8a24af0a2e8a872fb745047180649b8418303084"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/stopwatch/zipball/8a24af0a2e8a872fb745047180649b8418303084",
                "reference": "8a24af0a2e8a872fb745047180649b8418303084",
                "shasum": ""
            },
            "require": {
                "php": ">=8.2",
                "symfony/service-contracts": "^2.5|^3"
            },
            "type": "library",
            "autoload": {
                "psr-4": {
                    "Symfony\\Component\\Stopwatch\\": ""
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
            "description": "Provides a way to profile code",
            "homepage": "https://symfony.com",
            "support": {
                "source": "https://github.com/symfony/stopwatch/tree/v7.4.0"
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
                    "url": "https://github.com/nicolas-grekas",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2025-08-04T07:05:15+00:00"
        },
        {
            "name": "symfony/string",
            "version": "v7.4.4",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/string.git",
                "reference": "1c4b10461bf2ec27537b5f36105337262f5f5d6f"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/string/zipball/1c4b10461bf2ec27537b5f36105337262f5f5d6f",
                "reference": "1c4b10461bf2ec27537b5f36105337262f5f5d6f",
                "shasum": ""
            },
            "require": {
                "php": ">=8.2",
                "symfony/deprecation-contracts": "^2.5|^3.0",
                "symfony/polyfill-ctype": "~1.8",
                "symfony/polyfill-intl-grapheme": "~1.33",
                "symfony/polyfill-intl-normalizer": "~1.0",
                "symfony/polyfill-mbstring": "~1.0"
            },
            "conflict": {
                "symfony/translation-contracts": "<2.5"
            },
            "require-dev": {
                "symfony/emoji": "^7.1|^8.0",
                "symfony/http-client": "^6.4|^7.0|^8.0",
                "symfony/intl": "^6.4|^7.0|^8.0",
                "symfony/translation-contracts": "^2.5|^3.0",
                "symfony/var-exporter": "^6.4|^7.0|^8.0"
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
                "source": "https://github.com/symfony/string/tree/v7.4.4"
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
                    "url": "https://github.com/nicolas-grekas",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2026-01-12T10:54:30+00:00"
        },
        {
            "name": "symfony/translation-contracts",
            "version": "v3.6.1",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/translation-contracts.git",
                "reference": "65a8bc82080447fae78373aa10f8d13b38338977"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/translation-contracts/zipball/65a8bc82080447fae78373aa10f8d13b38338977",
                "reference": "65a8bc82080447fae78373aa10f8d13b38338977",
                "shasum": ""
            },
            "require": {
                "php": ">=8.1"
            },
            "type": "library",
            "extra": {
                "thanks": {
                    "url": "https://github.com/symfony/contracts",
                    "name": "symfony/contracts"
                },
                "branch-alias": {
                    "dev-main": "3.6-dev"
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
                "source": "https://github.com/symfony/translation-contracts/tree/v3.6.1"
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
                    "url": "https://github.com/nicolas-grekas",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2025-07-15T13:41:35+00:00"
        },
        {
            "name": "symfony/twig-bridge",
            "version": "v7.4.5",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/twig-bridge.git",
                "reference": "f2dd26b604e856476ef7e0efa4568bc07eb7ddc8"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/twig-bridge/zipball/f2dd26b604e856476ef7e0efa4568bc07eb7ddc8",
                "reference": "f2dd26b604e856476ef7e0efa4568bc07eb7ddc8",
                "shasum": ""
            },
            "require": {
                "php": ">=8.2",
                "symfony/deprecation-contracts": "^2.5|^3",
                "symfony/translation-contracts": "^2.5|^3",
                "twig/twig": "^3.21"
            },
            "conflict": {
                "phpdocumentor/reflection-docblock": "<5.2|>=6",
                "phpdocumentor/type-resolver": "<1.5.1",
                "symfony/console": "<6.4",
                "symfony/form": "<6.4.32|>7,<7.3.10|>7.4,<7.4.4|>8.0,<8.0.4",
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
                "phpdocumentor/reflection-docblock": "^5.2",
                "symfony/asset": "^6.4|^7.0|^8.0",
                "symfony/asset-mapper": "^6.4|^7.0|^8.0",
                "symfony/console": "^6.4|^7.0|^8.0",
                "symfony/dependency-injection": "^6.4|^7.0|^8.0",
                "symfony/emoji": "^7.1|^8.0",
                "symfony/expression-language": "^6.4|^7.0|^8.0",
                "symfony/finder": "^6.4|^7.0|^8.0",
                "symfony/form": "^6.4.32|~7.3.10|^7.4.4|^8.0.4",
                "symfony/html-sanitizer": "^6.4|^7.0|^8.0",
                "symfony/http-foundation": "^7.3|^8.0",
                "symfony/http-kernel": "^6.4|^7.0|^8.0",
                "symfony/intl": "^6.4|^7.0|^8.0",
                "symfony/mime": "^6.4|^7.0|^8.0",
                "symfony/polyfill-intl-icu": "~1.0",
                "symfony/property-info": "^6.4|^7.0|^8.0",
                "symfony/routing": "^6.4|^7.0|^8.0",
                "symfony/security-acl": "^2.8|^3.0",
                "symfony/security-core": "^6.4|^7.0|^8.0",
                "symfony/security-csrf": "^6.4|^7.0|^8.0",
                "symfony/security-http": "^6.4|^7.0|^8.0",
                "symfony/serializer": "^6.4.3|^7.0.3|^8.0",
                "symfony/stopwatch": "^6.4|^7.0|^8.0",
                "symfony/translation": "^6.4|^7.0|^8.0",
                "symfony/validator": "^6.4|^7.0|^8.0",
                "symfony/web-link": "^6.4|^7.0|^8.0",
                "symfony/workflow": "^6.4|^7.0|^8.0",
                "symfony/yaml": "^6.4|^7.0|^8.0",
                "twig/cssinliner-extra": "^3",
                "twig/inky-extra": "^3",
                "twig/markdown-extra": "^3"
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
                "source": "https://github.com/symfony/twig-bridge/tree/v7.4.5"
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
                    "url": "https://github.com/nicolas-grekas",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2026-01-27T08:59:58+00:00"
        },
        {
            "name": "symfony/twig-bundle",
            "version": "v7.4.4",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/twig-bundle.git",
                "reference": "e8829e02ff96a391ed0703bac9e7ff0537480b6b"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/twig-bundle/zipball/e8829e02ff96a391ed0703bac9e7ff0537480b6b",
                "reference": "e8829e02ff96a391ed0703bac9e7ff0537480b6b",
                "shasum": ""
            },
            "require": {
                "composer-runtime-api": ">=2.1",
                "php": ">=8.2",
                "symfony/config": "^7.4|^8.0",
                "symfony/dependency-injection": "^6.4|^7.0|^8.0",
                "symfony/deprecation-contracts": "^2.5|^3",
                "symfony/http-foundation": "^6.4|^7.0|^8.0",
                "symfony/http-kernel": "^6.4.13|^7.1.6|^8.0",
                "symfony/twig-bridge": "^7.3|^8.0",
                "twig/twig": "^3.12"
            },
            "conflict": {
                "symfony/framework-bundle": "<6.4",
                "symfony/translation": "<6.4"
            },
            "require-dev": {
                "symfony/asset": "^6.4|^7.0|^8.0",
                "symfony/expression-language": "^6.4|^7.0|^8.0",
                "symfony/finder": "^6.4|^7.0|^8.0",
                "symfony/form": "^6.4|^7.0|^8.0",
                "symfony/framework-bundle": "^6.4.13|^7.1.6|^8.0",
                "symfony/routing": "^6.4|^7.0|^8.0",
                "symfony/runtime": "^6.4.13|^7.1.6",
                "symfony/stopwatch": "^6.4|^7.0|^8.0",
                "symfony/translation": "^6.4|^7.0|^8.0",
                "symfony/web-link": "^6.4|^7.0|^8.0",
                "symfony/yaml": "^6.4|^7.0|^8.0"
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
                "source": "https://github.com/symfony/twig-bundle/tree/v7.4.4"
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
                    "url": "https://github.com/nicolas-grekas",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2026-01-06T12:34:24+00:00"
        },
        {
            "name": "symfony/type-info",
            "version": "v7.4.4",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/type-info.git",
                "reference": "f83c725e72b39b2704b9d6fc85070ad6ac7a5889"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/type-info/zipball/f83c725e72b39b2704b9d6fc85070ad6ac7a5889",
                "reference": "f83c725e72b39b2704b9d6fc85070ad6ac7a5889",
                "shasum": ""
            },
            "require": {
                "php": ">=8.2",
                "psr/container": "^1.1|^2.0",
                "symfony/deprecation-contracts": "^2.5|^3"
            },
            "conflict": {
                "phpstan/phpdoc-parser": "<1.30"
            },
            "require-dev": {
                "phpstan/phpdoc-parser": "^1.30|^2.0"
            },
            "type": "library",
            "autoload": {
                "psr-4": {
                    "Symfony\\Component\\TypeInfo\\": ""
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
                    "name": "Mathias Arlaud",
                    "email": "mathias.arlaud@gmail.com"
                },
                {
                    "name": "Baptiste LEDUC",
                    "email": "baptiste.leduc@gmail.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Extracts PHP types information.",
            "homepage": "https://symfony.com",
            "keywords": [
                "PHPStan",
                "phpdoc",
                "symfony",
                "type"
            ],
            "support": {
                "source": "https://github.com/symfony/type-info/tree/v7.4.4"
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
                    "url": "https://github.com/nicolas-grekas",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2026-01-09T12:14:21+00:00"
        },
        {
            "name": "symfony/var-dumper",
            "version": "v7.4.4",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/var-dumper.git",
                "reference": "0e4769b46a0c3c62390d124635ce59f66874b282"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/var-dumper/zipball/0e4769b46a0c3c62390d124635ce59f66874b282",
                "reference": "0e4769b46a0c3c62390d124635ce59f66874b282",
                "shasum": ""
            },
            "require": {
                "php": ">=8.2",
                "symfony/deprecation-contracts": "^2.5|^3",
                "symfony/polyfill-mbstring": "~1.0"
            },
            "conflict": {
                "symfony/console": "<6.4"
            },
            "require-dev": {
                "symfony/console": "^6.4|^7.0|^8.0",
                "symfony/http-kernel": "^6.4|^7.0|^8.0",
                "symfony/process": "^6.4|^7.0|^8.0",
                "symfony/uid": "^6.4|^7.0|^8.0",
                "twig/twig": "^3.12"
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
                "source": "https://github.com/symfony/var-dumper/tree/v7.4.4"
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
                    "url": "https://github.com/nicolas-grekas",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2026-01-01T22:13:48+00:00"
        },
        {
            "name": "symfony/var-exporter",
            "version": "v7.4.0",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/var-exporter.git",
                "reference": "03a60f169c79a28513a78c967316fbc8bf17816f"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/var-exporter/zipball/03a60f169c79a28513a78c967316fbc8bf17816f",
                "reference": "03a60f169c79a28513a78c967316fbc8bf17816f",
                "shasum": ""
            },
            "require": {
                "php": ">=8.2",
                "symfony/deprecation-contracts": "^2.5|^3"
            },
            "require-dev": {
                "symfony/property-access": "^6.4|^7.0|^8.0",
                "symfony/serializer": "^6.4|^7.0|^8.0",
                "symfony/var-dumper": "^6.4|^7.0|^8.0"
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
                "source": "https://github.com/symfony/var-exporter/tree/v7.4.0"
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
                    "url": "https://github.com/nicolas-grekas",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2025-09-11T10:15:23+00:00"
        },
        {
            "name": "symfony/yaml",
            "version": "v7.4.1",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/yaml.git",
                "reference": "24dd4de28d2e3988b311751ac49e684d783e2345"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/yaml/zipball/24dd4de28d2e3988b311751ac49e684d783e2345",
                "reference": "24dd4de28d2e3988b311751ac49e684d783e2345",
                "shasum": ""
            },
            "require": {
                "php": ">=8.2",
                "symfony/deprecation-contracts": "^2.5|^3",
                "symfony/polyfill-ctype": "^1.8"
            },
            "conflict": {
                "symfony/console": "<6.4"
            },
            "require-dev": {
                "symfony/console": "^6.4|^7.0|^8.0"
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
                "source": "https://github.com/symfony/yaml/tree/v7.4.1"
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
                    "url": "https://github.com/nicolas-grekas",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2025-12-04T18:11:45+00:00"
        },
        {
            "name": "twig/twig",
            "version": "v3.23.0",
            "source": {
                "type": "git",
                "url": "https://github.com/twigphp/Twig.git",
                "reference": "a64dc5d2cc7d6cafb9347f6cd802d0d06d0351c9"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/twigphp/Twig/zipball/a64dc5d2cc7d6cafb9347f6cd802d0d06d0351c9",
                "reference": "a64dc5d2cc7d6cafb9347f6cd802d0d06d0351c9",
                "shasum": ""
            },
            "require": {
                "php": ">=8.1.0",
                "symfony/deprecation-contracts": "^2.5|^3",
                "symfony/polyfill-ctype": "^1.8",
                "symfony/polyfill-mbstring": "^1.3"
            },
            "require-dev": {
                "phpstan/phpstan": "^2.0",
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
                "source": "https://github.com/twigphp/Twig/tree/v3.23.0"
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
            "time": "2026-01-23T21:00:41+00:00"
        },
        {
            "name": "webmozart/assert",
            "version": "2.1.2",
            "source": {
                "type": "git",
                "url": "https://github.com/webmozarts/assert.git",
                "reference": "ce6a2f100c404b2d32a1dd1270f9b59ad4f57649"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/webmozarts/assert/zipball/ce6a2f100c404b2d32a1dd1270f9b59ad4f57649",
                "reference": "ce6a2f100c404b2d32a1dd1270f9b59ad4f57649",
                "shasum": ""
            },
            "require": {
                "ext-ctype": "*",
                "ext-date": "*",
                "ext-filter": "*",
                "php": "^8.2"
            },
            "suggest": {
                "ext-intl": "",
                "ext-simplexml": "",
                "ext-spl": ""
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-feature/2-0": "2.0-dev"
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
                },
                {
                    "name": "Woody Gilk",
                    "email": "woody.gilk@gmail.com"
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
                "source": "https://github.com/webmozarts/assert/tree/2.1.2"
            },
            "time": "2026-01-13T14:02:24+00:00"
        },
        {
            "name": "zircote/swagger-php",
            "version": "5.8.1",
            "source": {
                "type": "git",
                "url": "https://github.com/zircote/swagger-php.git",
                "reference": "8adf6bb57561243aca48339e7f39bddf27ae546c"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/zircote/swagger-php/zipball/8adf6bb57561243aca48339e7f39bddf27ae546c",
                "reference": "8adf6bb57561243aca48339e7f39bddf27ae546c",
                "shasum": ""
            },
            "require": {
                "ext-json": "*",
                "nikic/php-parser": "^4.19 || ^5.0",
                "php": ">=7.4",
                "phpstan/phpdoc-parser": "^2.0",
                "psr/log": "^1.1 || ^2.0 || ^3.0",
                "symfony/deprecation-contracts": "^2 || ^3",
                "symfony/finder": "^5.0 || ^6.0 || ^7.0 || ^8.0",
                "symfony/yaml": "^5.4 || ^6.0 || ^7.0 || ^8.0"
            },
            "conflict": {
                "symfony/process": ">=6, <6.4.14"
            },
            "require-dev": {
                "composer/package-versions-deprecated": "^1.11",
                "doctrine/annotations": "^2.0",
                "friendsofphp/php-cs-fixer": "^3.62.0",
                "phpstan/phpstan": "^1.6 || ^2.0",
                "phpunit/phpunit": "^9.0",
                "rector/rector": "^1.0 || ^2.3.1",
                "vimeo/psalm": "^4.30 || ^5.0"
            },
            "suggest": {
                "doctrine/annotations": "^2.0",
                "radebatz/type-info-extras": "^1.0.2"
            },
            "bin": [
                "bin/openapi"
            ],
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "5.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "OpenApi\\": "src"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "Apache-2.0"
            ],
            "authors": [
                {
                    "name": "Robert Allen",
                    "email": "zircote@gmail.com"
                },
                {
                    "name": "Bob Fanger",
                    "email": "bfanger@gmail.com",
                    "homepage": "https://bfanger.nl"
                },
                {
                    "name": "Martin Rademacher",
                    "email": "mano@radebatz.net",
                    "homepage": "https://radebatz.net"
                }
            ],
            "description": "Generate interactive documentation for your RESTful API using PHP attributes (preferred) or PHPDoc annotations",
            "homepage": "https://github.com/zircote/swagger-php",
            "keywords": [
                "api",
                "json",
                "rest",
                "service discovery"
            ],
            "support": {
                "issues": "https://github.com/zircote/swagger-php/issues",
                "source": "https://github.com/zircote/swagger-php/tree/5.8.1"
            },
            "funding": [
                {
                    "url": "https://github.com/zircote",
                    "type": "github"
                }
            ],
            "time": "2026-02-03T23:48:39+00:00"
        }
    ],
    "packages-dev": [
        {
            "name": "amphp/amp",
            "version": "v2.6.5",
            "source": {
                "type": "git",
                "url": "https://github.com/amphp/amp.git",
                "reference": "d7dda98dae26e56f3f6fcfbf1c1f819c9a993207"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/amphp/amp/zipball/d7dda98dae26e56f3f6fcfbf1c1f819c9a993207",
                "reference": "d7dda98dae26e56f3f6fcfbf1c1f819c9a993207",
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
                "source": "https://github.com/amphp/amp/tree/v2.6.5"
            },
            "funding": [
                {
                    "url": "https://github.com/amphp",
                    "type": "github"
                }
            ],
            "time": "2025-09-03T19:41:28+00:00"
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
            "name": "composer/pcre",
            "version": "3.3.2",
            "source": {
                "type": "git",
                "url": "https://github.com/composer/pcre.git",
                "reference": "b2bed4734f0cc156ee1fe9c0da2550420d99a21e"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/composer/pcre/zipball/b2bed4734f0cc156ee1fe9c0da2550420d99a21e",
                "reference": "b2bed4734f0cc156ee1fe9c0da2550420d99a21e",
                "shasum": ""
            },
            "require": {
                "php": "^7.4 || ^8.0"
            },
            "conflict": {
                "phpstan/phpstan": "<1.11.10"
            },
            "require-dev": {
                "phpstan/phpstan": "^1.12 || ^2",
                "phpstan/phpstan-strict-rules": "^1 || ^2",
                "phpunit/phpunit": "^8 || ^9"
            },
            "type": "library",
            "extra": {
                "phpstan": {
                    "includes": [
                        "extension.neon"
                    ]
                },
                "branch-alias": {
                    "dev-main": "3.x-dev"
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
                "source": "https://github.com/composer/pcre/tree/3.3.2"
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
            "time": "2024-11-12T16:29:46+00:00"
        },
        {
            "name": "composer/semver",
            "version": "3.4.4",
            "source": {
                "type": "git",
                "url": "https://github.com/composer/semver.git",
                "reference": "198166618906cb2de69b95d7d47e5fa8aa1b2b95"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/composer/semver/zipball/198166618906cb2de69b95d7d47e5fa8aa1b2b95",
                "reference": "198166618906cb2de69b95d7d47e5fa8aa1b2b95",
                "shasum": ""
            },
            "require": {
                "php": "^5.3.2 || ^7.0 || ^8.0"
            },
            "require-dev": {
                "phpstan/phpstan": "^1.11",
                "symfony/phpunit-bridge": "^3 || ^7"
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
                "source": "https://github.com/composer/semver/tree/3.4.4"
            },
            "funding": [
                {
                    "url": "https://packagist.com",
                    "type": "custom"
                },
                {
                    "url": "https://github.com/composer",
                    "type": "github"
                }
            ],
            "time": "2025-08-20T19:15:30+00:00"
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
            "name": "dama/doctrine-test-bundle",
            "version": "v8.4.1",
            "source": {
                "type": "git",
                "url": "https://github.com/dmaicher/doctrine-test-bundle.git",
                "reference": "d9f4fb01a43da2e279ca190fa25ab9e26f15a0c8"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/dmaicher/doctrine-test-bundle/zipball/d9f4fb01a43da2e279ca190fa25ab9e26f15a0c8",
                "reference": "d9f4fb01a43da2e279ca190fa25ab9e26f15a0c8",
                "shasum": ""
            },
            "require": {
                "doctrine/dbal": "^3.3 || ^4.0",
                "doctrine/doctrine-bundle": "^2.11.0 || ^3.0",
                "php": ">= 8.1",
                "psr/cache": "^2.0 || ^3.0",
                "symfony/cache": "^6.4 || ^7.3 || ^8.0",
                "symfony/framework-bundle": "^6.4 || ^7.3 || ^8.0"
            },
            "conflict": {
                "phpunit/phpunit": "<10.0"
            },
            "require-dev": {
                "behat/behat": "^3.0",
                "friendsofphp/php-cs-fixer": "^3.27",
                "phpstan/phpstan": "^2.0",
                "phpunit/phpunit": "^10.5.57 || ^11.5.41|| ^12.3.14",
                "symfony/dotenv": "^6.4 || ^7.3 || ^8.0",
                "symfony/process": "^6.4 || ^7.3 || ^8.0"
            },
            "type": "symfony-bundle",
            "extra": {
                "branch-alias": {
                    "dev-master": "8.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "DAMA\\DoctrineTestBundle\\": "src"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "David Maicher",
                    "email": "mail@dmaicher.de"
                }
            ],
            "description": "Symfony bundle to isolate doctrine database tests and improve test performance",
            "keywords": [
                "doctrine",
                "isolation",
                "performance",
                "symfony",
                "testing",
                "tests"
            ],
            "support": {
                "issues": "https://github.com/dmaicher/doctrine-test-bundle/issues",
                "source": "https://github.com/dmaicher/doctrine-test-bundle/tree/v8.4.1"
            },
            "time": "2025-12-07T21:48:15+00:00"
        },
        {
            "name": "dealerdirect/phpcodesniffer-composer-installer",
            "version": "v1.2.0",
            "source": {
                "type": "git",
                "url": "https://github.com/PHPCSStandards/composer-installer.git",
                "reference": "845eb62303d2ca9b289ef216356568ccc075ffd1"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/PHPCSStandards/composer-installer/zipball/845eb62303d2ca9b289ef216356568ccc075ffd1",
                "reference": "845eb62303d2ca9b289ef216356568ccc075ffd1",
                "shasum": ""
            },
            "require": {
                "composer-plugin-api": "^2.2",
                "php": ">=5.4",
                "squizlabs/php_codesniffer": "^3.1.0 || ^4.0"
            },
            "require-dev": {
                "composer/composer": "^2.2",
                "ext-json": "*",
                "ext-zip": "*",
                "php-parallel-lint/php-parallel-lint": "^1.4.0",
                "phpcompatibility/php-compatibility": "^9.0 || ^10.0.0@dev",
                "yoast/phpunit-polyfills": "^1.0"
            },
            "type": "composer-plugin",
            "extra": {
                "class": "PHPCSStandards\\Composer\\Plugin\\Installers\\PHPCodeSniffer\\Plugin"
            },
            "autoload": {
                "psr-4": {
                    "PHPCSStandards\\Composer\\Plugin\\Installers\\PHPCodeSniffer\\": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Franck Nijhof",
                    "email": "opensource@frenck.dev",
                    "homepage": "https://frenck.dev",
                    "role": "Open source developer"
                },
                {
                    "name": "Contributors",
                    "homepage": "https://github.com/PHPCSStandards/composer-installer/graphs/contributors"
                }
            ],
            "description": "PHP_CodeSniffer Standards Composer Installer Plugin",
            "keywords": [
                "PHPCodeSniffer",
                "PHP_CodeSniffer",
                "code quality",
                "codesniffer",
                "composer",
                "installer",
                "phpcbf",
                "phpcs",
                "plugin",
                "qa",
                "quality",
                "standard",
                "standards",
                "style guide",
                "stylecheck",
                "tests"
            ],
            "support": {
                "issues": "https://github.com/PHPCSStandards/composer-installer/issues",
                "security": "https://github.com/PHPCSStandards/composer-installer/security/policy",
                "source": "https://github.com/PHPCSStandards/composer-installer"
            },
            "funding": [
                {
                    "url": "https://github.com/PHPCSStandards",
                    "type": "github"
                },
                {
                    "url": "https://github.com/jrfnl",
                    "type": "github"
                },
                {
                    "url": "https://opencollective.com/php_codesniffer",
                    "type": "open_collective"
                },
                {
                    "url": "https://thanks.dev/u/gh/phpcsstandards",
                    "type": "thanks_dev"
                }
            ],
            "time": "2025-11-11T04:32:07+00:00"
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
            "version": "v1.5.3",
            "source": {
                "type": "git",
                "url": "https://github.com/felixfbecker/php-language-server-protocol.git",
                "reference": "a9e113dbc7d849e35b8776da39edaf4313b7b6c9"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/felixfbecker/php-language-server-protocol/zipball/a9e113dbc7d849e35b8776da39edaf4313b7b6c9",
                "reference": "a9e113dbc7d849e35b8776da39edaf4313b7b6c9",
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
                "source": "https://github.com/felixfbecker/php-language-server-protocol/tree/v1.5.3"
            },
            "time": "2024-04-30T00:40:11+00:00"
        },
        {
            "name": "fidry/cpu-core-counter",
            "version": "1.3.0",
            "source": {
                "type": "git",
                "url": "https://github.com/theofidry/cpu-core-counter.git",
                "reference": "db9508f7b1474469d9d3c53b86f817e344732678"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/theofidry/cpu-core-counter/zipball/db9508f7b1474469d9d3c53b86f817e344732678",
                "reference": "db9508f7b1474469d9d3c53b86f817e344732678",
                "shasum": ""
            },
            "require": {
                "php": "^7.2 || ^8.0"
            },
            "require-dev": {
                "fidry/makefile": "^0.2.0",
                "fidry/php-cs-fixer-config": "^1.1.2",
                "phpstan/extension-installer": "^1.2.0",
                "phpstan/phpstan": "^2.0",
                "phpstan/phpstan-deprecation-rules": "^2.0.0",
                "phpstan/phpstan-phpunit": "^2.0",
                "phpstan/phpstan-strict-rules": "^2.0",
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
                "source": "https://github.com/theofidry/cpu-core-counter/tree/1.3.0"
            },
            "funding": [
                {
                    "url": "https://github.com/theofidry",
                    "type": "github"
                }
            ],
            "time": "2025-08-14T07:29:31+00:00"
        },
        {
            "name": "masterminds/html5",
            "version": "2.10.0",
            "source": {
                "type": "git",
                "url": "https://github.com/Masterminds/html5-php.git",
                "reference": "fcf91eb64359852f00d921887b219479b4f21251"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/Masterminds/html5-php/zipball/fcf91eb64359852f00d921887b219479b4f21251",
                "reference": "fcf91eb64359852f00d921887b219479b4f21251",
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
                "source": "https://github.com/Masterminds/html5-php/tree/2.10.0"
            },
            "time": "2025-07-25T09:04:22+00:00"
        },
        {
            "name": "myclabs/deep-copy",
            "version": "1.13.4",
            "source": {
                "type": "git",
                "url": "https://github.com/myclabs/DeepCopy.git",
                "reference": "07d290f0c47959fd5eed98c95ee5602db07e0b6a"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/myclabs/DeepCopy/zipball/07d290f0c47959fd5eed98c95ee5602db07e0b6a",
                "reference": "07d290f0c47959fd5eed98c95ee5602db07e0b6a",
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
                "source": "https://github.com/myclabs/DeepCopy/tree/1.13.4"
            },
            "funding": [
                {
                    "url": "https://tidelift.com/funding/github/packagist/myclabs/deep-copy",
                    "type": "tidelift"
                }
            ],
            "time": "2025-08-01T08:46:24+00:00"
        },
        {
            "name": "netresearch/jsonmapper",
            "version": "v4.5.0",
            "source": {
                "type": "git",
                "url": "https://github.com/cweiske/jsonmapper.git",
                "reference": "8e76efb98ee8b6afc54687045e1b8dba55ac76e5"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/cweiske/jsonmapper/zipball/8e76efb98ee8b6afc54687045e1b8dba55ac76e5",
                "reference": "8e76efb98ee8b6afc54687045e1b8dba55ac76e5",
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
                "source": "https://github.com/cweiske/jsonmapper/tree/v4.5.0"
            },
            "time": "2024-09-08T10:13:13+00:00"
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
            "name": "phpstan/phpstan",
            "version": "2.1.38",
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/phpstan/phpstan/zipball/dfaf1f530e1663aa167bc3e52197adb221582629",
                "reference": "dfaf1f530e1663aa167bc3e52197adb221582629",
                "shasum": ""
            },
            "require": {
                "php": "^7.4|^8.0"
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
            "time": "2026-01-30T17:12:46+00:00"
        },
        {
            "name": "phpunit/php-code-coverage",
            "version": "10.1.16",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/php-code-coverage.git",
                "reference": "7e308268858ed6baedc8704a304727d20bc07c77"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/php-code-coverage/zipball/7e308268858ed6baedc8704a304727d20bc07c77",
                "reference": "7e308268858ed6baedc8704a304727d20bc07c77",
                "shasum": ""
            },
            "require": {
                "ext-dom": "*",
                "ext-libxml": "*",
                "ext-xmlwriter": "*",
                "nikic/php-parser": "^4.19.1 || ^5.1.0",
                "php": ">=8.1",
                "phpunit/php-file-iterator": "^4.1.0",
                "phpunit/php-text-template": "^3.0.1",
                "sebastian/code-unit-reverse-lookup": "^3.0.0",
                "sebastian/complexity": "^3.2.0",
                "sebastian/environment": "^6.1.0",
                "sebastian/lines-of-code": "^2.0.2",
                "sebastian/version": "^4.0.1",
                "theseer/tokenizer": "^1.2.3"
            },
            "require-dev": {
                "phpunit/phpunit": "^10.1"
            },
            "suggest": {
                "ext-pcov": "PHP extension that provides line coverage",
                "ext-xdebug": "PHP extension that provides line coverage as well as branch and path coverage"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-main": "10.1.x-dev"
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
                "source": "https://github.com/sebastianbergmann/php-code-coverage/tree/10.1.16"
            },
            "funding": [
                {
                    "url": "https://github.com/sebastianbergmann",
                    "type": "github"
                }
            ],
            "time": "2024-08-22T04:31:57+00:00"
        },
        {
            "name": "phpunit/php-file-iterator",
            "version": "4.1.0",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/php-file-iterator.git",
                "reference": "a95037b6d9e608ba092da1b23931e537cadc3c3c"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/php-file-iterator/zipball/a95037b6d9e608ba092da1b23931e537cadc3c3c",
                "reference": "a95037b6d9e608ba092da1b23931e537cadc3c3c",
                "shasum": ""
            },
            "require": {
                "php": ">=8.1"
            },
            "require-dev": {
                "phpunit/phpunit": "^10.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-main": "4.0-dev"
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
                "security": "https://github.com/sebastianbergmann/php-file-iterator/security/policy",
                "source": "https://github.com/sebastianbergmann/php-file-iterator/tree/4.1.0"
            },
            "funding": [
                {
                    "url": "https://github.com/sebastianbergmann",
                    "type": "github"
                }
            ],
            "time": "2023-08-31T06:24:48+00:00"
        },
        {
            "name": "phpunit/php-invoker",
            "version": "4.0.0",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/php-invoker.git",
                "reference": "f5e568ba02fa5ba0ddd0f618391d5a9ea50b06d7"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/php-invoker/zipball/f5e568ba02fa5ba0ddd0f618391d5a9ea50b06d7",
                "reference": "f5e568ba02fa5ba0ddd0f618391d5a9ea50b06d7",
                "shasum": ""
            },
            "require": {
                "php": ">=8.1"
            },
            "require-dev": {
                "ext-pcntl": "*",
                "phpunit/phpunit": "^10.0"
            },
            "suggest": {
                "ext-pcntl": "*"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-main": "4.0-dev"
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
                "source": "https://github.com/sebastianbergmann/php-invoker/tree/4.0.0"
            },
            "funding": [
                {
                    "url": "https://github.com/sebastianbergmann",
                    "type": "github"
                }
            ],
            "time": "2023-02-03T06:56:09+00:00"
        },
        {
            "name": "phpunit/php-text-template",
            "version": "3.0.1",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/php-text-template.git",
                "reference": "0c7b06ff49e3d5072f057eb1fa59258bf287a748"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/php-text-template/zipball/0c7b06ff49e3d5072f057eb1fa59258bf287a748",
                "reference": "0c7b06ff49e3d5072f057eb1fa59258bf287a748",
                "shasum": ""
            },
            "require": {
                "php": ">=8.1"
            },
            "require-dev": {
                "phpunit/phpunit": "^10.0"
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
                "security": "https://github.com/sebastianbergmann/php-text-template/security/policy",
                "source": "https://github.com/sebastianbergmann/php-text-template/tree/3.0.1"
            },
            "funding": [
                {
                    "url": "https://github.com/sebastianbergmann",
                    "type": "github"
                }
            ],
            "time": "2023-08-31T14:07:24+00:00"
        },
        {
            "name": "phpunit/php-timer",
            "version": "6.0.0",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/php-timer.git",
                "reference": "e2a2d67966e740530f4a3343fe2e030ffdc1161d"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/php-timer/zipball/e2a2d67966e740530f4a3343fe2e030ffdc1161d",
                "reference": "e2a2d67966e740530f4a3343fe2e030ffdc1161d",
                "shasum": ""
            },
            "require": {
                "php": ">=8.1"
            },
            "require-dev": {
                "phpunit/phpunit": "^10.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-main": "6.0-dev"
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
                "source": "https://github.com/sebastianbergmann/php-timer/tree/6.0.0"
            },
            "funding": [
                {
                    "url": "https://github.com/sebastianbergmann",
                    "type": "github"
                }
            ],
            "time": "2023-02-03T06:57:52+00:00"
        },
        {
            "name": "phpunit/phpunit",
            "version": "10.5.63",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/phpunit.git",
                "reference": "33198268dad71e926626b618f3ec3966661e4d90"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/phpunit/zipball/33198268dad71e926626b618f3ec3966661e4d90",
                "reference": "33198268dad71e926626b618f3ec3966661e4d90",
                "shasum": ""
            },
            "require": {
                "ext-dom": "*",
                "ext-json": "*",
                "ext-libxml": "*",
                "ext-mbstring": "*",
                "ext-xml": "*",
                "ext-xmlwriter": "*",
                "myclabs/deep-copy": "^1.13.4",
                "phar-io/manifest": "^2.0.4",
                "phar-io/version": "^3.2.1",
                "php": ">=8.1",
                "phpunit/php-code-coverage": "^10.1.16",
                "phpunit/php-file-iterator": "^4.1.0",
                "phpunit/php-invoker": "^4.0.0",
                "phpunit/php-text-template": "^3.0.1",
                "phpunit/php-timer": "^6.0.0",
                "sebastian/cli-parser": "^2.0.1",
                "sebastian/code-unit": "^2.0.0",
                "sebastian/comparator": "^5.0.5",
                "sebastian/diff": "^5.1.1",
                "sebastian/environment": "^6.1.0",
                "sebastian/exporter": "^5.1.4",
                "sebastian/global-state": "^6.0.2",
                "sebastian/object-enumerator": "^5.0.0",
                "sebastian/recursion-context": "^5.0.1",
                "sebastian/type": "^4.0.0",
                "sebastian/version": "^4.0.1"
            },
            "suggest": {
                "ext-soap": "To be able to generate mocks based on WSDL files"
            },
            "bin": [
                "phpunit"
            ],
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-main": "10.5-dev"
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
                "source": "https://github.com/sebastianbergmann/phpunit/tree/10.5.63"
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
                    "url": "https://liberapay.com/sebastianbergmann",
                    "type": "liberapay"
                },
                {
                    "url": "https://thanks.dev/u/gh/sebastianbergmann",
                    "type": "thanks_dev"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/phpunit/phpunit",
                    "type": "tidelift"
                }
            ],
            "time": "2026-01-27T05:48:37+00:00"
        },
        {
            "name": "rector/rector",
            "version": "2.3.5",
            "source": {
                "type": "git",
                "url": "https://github.com/rectorphp/rector.git",
                "reference": "9442f4037de6a5347ae157fe8e6c7cda9d909070"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/rectorphp/rector/zipball/9442f4037de6a5347ae157fe8e6c7cda9d909070",
                "reference": "9442f4037de6a5347ae157fe8e6c7cda9d909070",
                "shasum": ""
            },
            "require": {
                "php": "^7.4|^8.0",
                "phpstan/phpstan": "^2.1.36"
            },
            "conflict": {
                "rector/rector-doctrine": "*",
                "rector/rector-downgrade-php": "*",
                "rector/rector-phpunit": "*",
                "rector/rector-symfony": "*"
            },
            "suggest": {
                "ext-dom": "To manipulate phpunit.xml via the custom-rule command"
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
            "homepage": "https://getrector.com/",
            "keywords": [
                "automation",
                "dev",
                "migration",
                "refactoring"
            ],
            "support": {
                "issues": "https://github.com/rectorphp/rector/issues",
                "source": "https://github.com/rectorphp/rector/tree/2.3.5"
            },
            "funding": [
                {
                    "url": "https://github.com/tomasvotruba",
                    "type": "github"
                }
            ],
            "time": "2026-01-28T15:22:48+00:00"
        },
        {
            "name": "roave/security-advisories",
            "version": "dev-master",
            "source": {
                "type": "git",
                "url": "https://github.com/Roave/SecurityAdvisories.git",
                "reference": "7ea2d110787f6807213e27a1255c6b858ad99d89"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/Roave/SecurityAdvisories/zipball/7ea2d110787f6807213e27a1255c6b858ad99d89",
                "reference": "7ea2d110787f6807213e27a1255c6b858ad99d89",
                "shasum": ""
            },
            "conflict": {
                "3f/pygmentize": "<1.2",
                "adaptcms/adaptcms": "<=1.3",
                "admidio/admidio": "<=4.3.16",
                "adodb/adodb-php": "<=5.22.9",
                "aheinze/cockpit": "<2.2",
                "aimeos/ai-admin-graphql": ">=2022.04.1,<2022.10.10|>=2023.04.1,<2023.10.6|>=2024.04.1,<2024.07.2",
                "aimeos/ai-admin-jsonadm": "<2020.10.13|>=2021.04.1,<2021.10.6|>=2022.04.1,<2022.10.3|>=2023.04.1,<2023.10.4|==2024.04.1",
                "aimeos/ai-client-html": ">=2020.04.1,<2020.10.27|>=2021.04.1,<2021.10.22|>=2022.04.1,<2022.10.13|>=2023.04.1,<2023.10.15|>=2024.04.1,<2024.04.7",
                "aimeos/ai-cms-grapesjs": ">=2021.04.1,<2021.10.8|>=2022.04.1,<2022.10.9|>=2023.04.1,<2023.10.15|>=2024.04.1,<2024.10.8|>=2025.04.1,<2025.10.2",
                "aimeos/ai-controller-frontend": "<2020.10.15|>=2021.04.1,<2021.10.8|>=2022.04.1,<2022.10.8|>=2023.04.1,<2023.10.9|==2024.04.1",
                "aimeos/aimeos-core": ">=2022.04.1,<2022.10.17|>=2023.04.1,<2023.10.17|>=2024.04.1,<2024.04.7",
                "aimeos/aimeos-laravel": "==2021.10",
                "aimeos/aimeos-typo3": "<19.10.12|>=20,<20.10.5",
                "airesvsg/acf-to-rest-api": "<=3.1",
                "akaunting/akaunting": "<2.1.13",
                "akeneo/pim-community-dev": "<5.0.119|>=6,<6.0.53",
                "alextselegidis/easyappointments": "<=1.5.2",
                "alexusmai/laravel-file-manager": "<=3.3.1",
                "algolia/algoliasearch-magento-2": "<=3.16.1|>=3.17.0.0-beta1,<=3.17.1",
                "alt-design/alt-redirect": "<1.6.4",
                "altcha-org/altcha": "<1.3.1",
                "alterphp/easyadmin-extension-bundle": ">=1.2,<1.2.11|>=1.3,<1.3.1",
                "amazing/media2click": ">=1,<1.3.3",
                "ameos/ameos_tarteaucitron": "<1.2.23",
                "amphp/artax": "<1.0.6|>=2,<2.0.6",
                "amphp/http": "<=1.7.2|>=2,<=2.1",
                "amphp/http-client": ">=4,<4.4",
                "anchorcms/anchor-cms": "<=0.12.7",
                "andreapollastri/cipi": "<=3.1.15",
                "andrewhaine/silverstripe-form-capture": ">=0.2,<=0.2.3|>=1,<1.0.2|>=2,<2.2.5",
                "aoe/restler": "<1.7.1",
                "apache-solr-for-typo3/solr": "<2.8.3",
                "apereo/phpcas": "<1.6",
                "api-platform/core": "<3.4.17|>=4,<4.0.22|>=4.1,<4.1.5",
                "api-platform/graphql": "<3.4.17|>=4,<4.0.22|>=4.1,<4.1.5",
                "appwrite/server-ce": "<=1.2.1",
                "arc/web": "<3",
                "area17/twill": "<1.2.5|>=2,<2.5.3",
                "artesaos/seotools": "<0.17.2",
                "asymmetricrypt/asymmetricrypt": "<9.9.99",
                "athlon1600/php-proxy": "<=5.1",
                "athlon1600/php-proxy-app": "<=3",
                "athlon1600/youtube-downloader": "<=4",
                "austintoddj/canvas": "<=3.4.2",
                "auth0/auth0-php": ">=3.3,<8.18",
                "auth0/login": "<7.20",
                "auth0/symfony": "<=5.5",
                "auth0/wordpress": "<=5.4",
                "automad/automad": "<2.0.0.0-alpha5",
                "automattic/jetpack": "<9.8",
                "awesome-support/awesome-support": "<=6.0.7",
                "aws/aws-sdk-php": "<3.368",
                "azuracast/azuracast": "<=0.23.1",
                "b13/seo_basics": "<0.8.2",
                "backdrop/backdrop": "<=1.32",
                "backpack/crud": "<3.4.9",
                "backpack/filemanager": "<2.0.2|>=3,<3.0.9",
                "bacula-web/bacula-web": "<9.7.1",
                "badaso/core": "<=2.9.11",
                "bagisto/bagisto": "<2.3.10",
                "barrelstrength/sprout-base-email": "<1.2.7",
                "barrelstrength/sprout-forms": "<3.9",
                "barryvdh/laravel-translation-manager": "<0.6.8",
                "barzahlen/barzahlen-php": "<2.0.1",
                "baserproject/basercms": "<=5.1.1",
                "bassjobsen/bootstrap-3-typeahead": ">4.0.2",
                "bbpress/bbpress": "<2.6.5",
                "bcit-ci/codeigniter": "<3.1.3",
                "bcosca/fatfree": "<3.7.2",
                "bedita/bedita": "<4",
                "bednee/cooluri": "<1.0.30",
                "bigfork/silverstripe-form-capture": ">=3,<3.1.1",
                "billz/raspap-webgui": "<3.3.6",
                "binarytorch/larecipe": "<2.8.1",
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
                "bvbmedia/multishop": "<2.0.39",
                "bytefury/crater": "<6.0.2",
                "cachethq/cachet": "<2.5.1",
                "cadmium-org/cadmium-cms": "<=0.4.9",
                "cakephp/cakephp": "<3.10.3|>=4,<4.0.10|>=4.1,<4.1.4|>=4.2,<4.2.12|>=4.3,<4.3.11|>=4.4,<4.4.10|>=5.2.10,<5.2.12|==5.3",
                "cakephp/database": ">=4.2,<4.2.12|>=4.3,<4.3.11|>=4.4,<4.4.10",
                "cardgate/magento2": "<2.0.33",
                "cardgate/woocommerce": "<=3.1.15",
                "cart2quote/module-quotation": ">=4.1.6,<=4.4.5|>=5,<5.4.4",
                "cart2quote/module-quotation-encoded": ">=4.1.6,<=4.4.5|>=5,<5.4.4",
                "cartalyst/sentry": "<=2.1.6",
                "catfan/medoo": "<1.7.5",
                "causal/oidc": "<4",
                "cecil/cecil": "<7.47.1",
                "centreon/centreon": "<22.10.15",
                "cesnet/simplesamlphp-module-proxystatistics": "<3.1",
                "chriskacerguis/codeigniter-restserver": "<=2.7.1",
                "chrome-php/chrome": "<1.14",
                "ci4-cms-erp/ci4ms": "<0.28.5",
                "civicrm/civicrm-core": ">=4.2,<4.2.9|>=4.3,<4.3.3",
                "ckeditor/ckeditor": "<4.25",
                "clickstorm/cs-seo": ">=6,<6.8|>=7,<7.5|>=8,<8.4|>=9,<9.3",
                "co-stack/fal_sftp": "<0.2.6",
                "cockpit-hq/cockpit": "<2.11.4",
                "code16/sharp": "<9.11.1",
                "codeception/codeception": "<3.1.3|>=4,<4.1.22",
                "codeigniter/framework": "<3.1.10",
                "codeigniter4/framework": "<4.6.2",
                "codeigniter4/shield": "<1.0.0.0-beta8",
                "codiad/codiad": "<=2.8.4",
                "codingms/additional-tca": ">=1.7,<1.15.17|>=1.16,<1.16.9",
                "codingms/modules": "<4.3.11|>=5,<5.7.4|>=6,<6.4.2|>=7,<7.5.5",
                "commerceteam/commerce": ">=0.9.6,<0.9.9",
                "components/jquery": ">=1.0.3,<3.5",
                "composer/composer": "<1.10.27|>=2,<2.2.26|>=2.3,<2.9.3",
                "concrete5/concrete5": "<9.4.3",
                "concrete5/core": "<8.5.8|>=9,<9.1",
                "contao-components/mediaelement": ">=2.14.2,<2.21.1",
                "contao/comments-bundle": ">=2,<4.13.40|>=5.0.0.0-RC1-dev,<5.3.4",
                "contao/contao": ">=3,<3.5.37|>=4,<4.4.56|>=4.5,<4.13.56|>=5,<5.3.38|>=5.4.0.0-RC1-dev,<5.6.1",
                "contao/core": "<3.5.39",
                "contao/core-bundle": "<4.13.57|>=5,<5.3.42|>=5.4,<5.6.5",
                "contao/listing-bundle": ">=3,<=3.5.30|>=4,<4.4.8",
                "contao/managed-edition": "<=1.5",
                "coreshop/core-shop": "<4.1.9",
                "corveda/phpsandbox": "<1.3.5",
                "cosenary/instagram": "<=2.3",
                "couleurcitron/tarteaucitron-wp": "<0.3",
                "cpsit/typo3-mailqueue": "<0.4.3|>=0.5,<0.5.1",
                "craftcms/cms": "<=4.16.16|>=5,<=5.8.20",
                "craftcms/commerce": ">=4.0.0.0-RC1-dev,<=4.10|>=5,<=5.5.1",
                "craftcms/composer": ">=4.0.0.0-RC1-dev,<=4.10|>=5.0.0.0-RC1-dev,<=5.5.1",
                "croogo/croogo": "<=4.0.7",
                "cuyz/valinor": "<0.12",
                "czim/file-handling": "<1.5|>=2,<2.3",
                "czproject/git-php": "<4.0.3",
                "damienharper/auditor-bundle": "<5.2.6",
                "dapphp/securimage": "<3.6.6",
                "darylldoyle/safe-svg": "<1.9.10",
                "datadog/dd-trace": ">=0.30,<0.30.2",
                "datahihi1/tiny-env": "<1.0.3|>=1.0.9,<1.0.11",
                "datatables/datatables": "<1.10.10",
                "david-garcia/phpwhois": "<=4.3.1",
                "dbrisinajumi/d2files": "<1",
                "dcat/laravel-admin": "<=2.1.3|==2.2.0.0-beta|==2.2.2.0-beta",
                "derhansen/fe_change_pwd": "<2.0.5|>=3,<3.0.3",
                "derhansen/sf_event_mgt": "<4.3.1|>=5,<5.1.1|>=7,<7.4",
                "desperado/xml-bundle": "<=0.1.7",
                "dev-lancer/minecraft-motd-parser": "<=1.0.5",
                "devcode-it/openstamanager": "<=2.9.8",
                "devgroup/dotplant": "<2020.09.14-dev",
                "digimix/wp-svg-upload": "<=1",
                "directmailteam/direct-mail": "<6.0.3|>=7,<7.0.3|>=8,<9.5.2",
                "dl/yag": "<3.0.1",
                "dmk/webkitpdf": "<1.1.4",
                "dnadesign/silverstripe-elemental": "<5.3.12",
                "doctrine/annotations": "<1.2.7",
                "doctrine/cache": ">=1,<1.3.2|>=1.4,<1.4.2",
                "doctrine/common": "<2.4.3|>=2.5,<2.5.1",
                "doctrine/dbal": ">=2,<2.0.8|>=2.1,<2.1.2|>=3,<3.1.4",
                "doctrine/doctrine-bundle": "<1.5.2",
                "doctrine/doctrine-module": "<0.7.2",
                "doctrine/mongodb-odm": "<1.0.2",
                "doctrine/mongodb-odm-bundle": "<3.0.1",
                "doctrine/orm": ">=1,<1.2.4|>=2,<2.4.8|>=2.5,<2.5.1|>=2.8.3,<2.8.4",
                "dolibarr/dolibarr": "<21.0.3",
                "dompdf/dompdf": "<2.0.4",
                "doublethreedigital/guest-entries": "<3.1.2",
                "drupal-pattern-lab/unified-twig-extensions": "<=0.1",
                "drupal/access_code": "<2.0.5",
                "drupal/acquia_dam": "<1.1.5",
                "drupal/admin_audit_trail": "<1.0.5",
                "drupal/ai": "<1.0.5",
                "drupal/alogin": "<2.0.6",
                "drupal/cache_utility": "<1.2.1",
                "drupal/civictheme": "<1.12",
                "drupal/commerce_alphabank_redirect": "<1.0.3",
                "drupal/commerce_eurobank_redirect": "<2.1.1",
                "drupal/config_split": "<1.10|>=2,<2.0.2",
                "drupal/core": ">=6,<6.38|>=7,<7.103|>=8,<10.4.9|>=10.5,<10.5.6|>=11,<11.1.9|>=11.2,<11.2.8",
                "drupal/core-recommended": ">=7,<7.102|>=8,<10.2.11|>=10.3,<10.3.9|>=11,<11.0.8",
                "drupal/currency": "<3.5",
                "drupal/drupal": ">=5,<5.11|>=6,<6.38|>=7,<7.102|>=8,<10.2.11|>=10.3,<10.3.9|>=11,<11.0.8",
                "drupal/email_tfa": "<2.0.6",
                "drupal/formatter_suite": "<2.1",
                "drupal/gdpr": "<3.0.1|>=3.1,<3.1.2",
                "drupal/google_tag": "<1.8|>=2,<2.0.8",
                "drupal/ignition": "<1.0.4",
                "drupal/json_field": "<1.5",
                "drupal/lightgallery": "<1.6",
                "drupal/link_field_display_mode_formatter": "<1.6",
                "drupal/matomo": "<1.24",
                "drupal/oauth2_client": "<4.1.3",
                "drupal/oauth2_server": "<2.1",
                "drupal/obfuscate": "<2.0.1",
                "drupal/plausible_tracking": "<1.0.2",
                "drupal/quick_node_block": "<2",
                "drupal/rapidoc_elements_field_formatter": "<1.0.1",
                "drupal/reverse_proxy_header": "<1.1.2",
                "drupal/simple_multistep": "<2",
                "drupal/simple_oauth": ">=6,<6.0.7",
                "drupal/spamspan": "<3.2.1",
                "drupal/tfa": "<1.10",
                "drupal/umami_analytics": "<1.0.1",
                "duncanmcclean/guest-entries": "<3.1.2",
                "dweeves/magmi": "<=0.7.24",
                "ec-cube/ec-cube": "<2.4.4|>=2.11,<=2.17.1|>=3,<=3.0.18.0-patch4|>=4,<=4.1.2",
                "ecodev/newsletter": "<=4",
                "ectouch/ectouch": "<=2.7.2",
                "egroupware/egroupware": "<23.1.20260113|>=26.0.20251208,<26.0.20260113",
                "elefant/cms": "<2.0.7",
                "elgg/elgg": "<3.3.24|>=4,<4.0.5",
                "elijaa/phpmemcacheadmin": "<=1.3",
                "elmsln/haxcms": "<11.0.14",
                "encore/laravel-admin": "<=1.8.19",
                "endroid/qr-code-bundle": "<3.4.2",
                "enhavo/enhavo-app": "<=0.13.1",
                "enshrined/svg-sanitize": "<0.22",
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
                "ezsystems/ezplatform-admin-ui": ">=1.3,<1.3.5|>=1.4,<1.4.6|>=1.5,<1.5.29|>=2.3,<2.3.39|>=3.3,<3.3.39",
                "ezsystems/ezplatform-admin-ui-assets": ">=4,<4.2.1|>=5,<5.0.1|>=5.1,<5.1.1|>=5.3.0.0-beta1,<5.3.5",
                "ezsystems/ezplatform-graphql": ">=1.0.0.0-RC1-dev,<1.0.13|>=2.0.0.0-beta1,<2.3.12",
                "ezsystems/ezplatform-http-cache": "<2.3.16",
                "ezsystems/ezplatform-kernel": "<=1.2.5|>=1.3,<1.3.35",
                "ezsystems/ezplatform-rest": ">=1.2,<=1.2.2|>=1.3,<1.3.8",
                "ezsystems/ezplatform-richtext": ">=2.3,<2.3.26|>=3.3,<3.3.40",
                "ezsystems/ezplatform-solr-search-engine": ">=1.7,<1.7.12|>=2,<2.0.2|>=3.3,<3.3.15",
                "ezsystems/ezplatform-user": ">=1,<1.0.1",
                "ezsystems/ezpublish-kernel": "<=6.13.8.1|>=7,<7.5.31",
                "ezsystems/ezpublish-legacy": "<=2017.12.7.3|>=2018.6,<=2019.03.5.1",
                "ezsystems/platform-ui-assets-bundle": ">=4.2,<4.2.3",
                "ezsystems/repository-forms": ">=2.3,<2.3.2.1-dev|>=2.5,<2.5.15",
                "ezyang/htmlpurifier": "<=4.2",
                "facade/ignition": "<1.16.15|>=2,<2.4.2|>=2.5,<2.5.2",
                "facturascripts/facturascripts": "<2025.81",
                "fastly/magento2": "<1.2.26",
                "feehi/cms": "<=2.1.1",
                "feehi/feehicms": "<=2.1.1",
                "fenom/fenom": "<=2.12.1",
                "filament/actions": ">=3.2,<3.2.123",
                "filament/filament": ">=4,<4.3.1",
                "filament/infolists": ">=3,<3.2.115",
                "filament/tables": ">=3,<3.2.115",
                "filegator/filegator": "<7.8",
                "filp/whoops": "<2.1.13",
                "fineuploader/php-traditional-server": "<=1.2.2",
                "firebase/php-jwt": "<6",
                "fisharebest/webtrees": "<=2.1.18",
                "fixpunkt/fp-masterquiz": "<2.2.1|>=3,<3.5.2",
                "fixpunkt/fp-newsletter": "<1.1.1|>=1.2,<2.1.2|>=2.2,<3.2.6",
                "flarum/core": "<1.8.10",
                "flarum/flarum": "<0.1.0.0-beta8",
                "flarum/framework": "<1.8.10",
                "flarum/mentions": "<1.6.3",
                "flarum/sticky": ">=0.1.0.0-beta14,<=0.1.0.0-beta15",
                "flarum/tags": "<=0.1.0.0-beta13",
                "floriangaerber/magnesium": "<0.3.1",
                "fluidtypo3/vhs": "<5.1.1",
                "fof/byobu": ">=0.3.0.0-beta2,<1.1.7",
                "fof/pretty-mail": "<=1.1.2",
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
                "froala/wysiwyg-editor": "<=4.3",
                "froxlor/froxlor": "<=2.2.5",
                "frozennode/administrator": "<=5.0.12",
                "fuel/core": "<1.8.1",
                "funadmin/funadmin": "<=5.0.2",
                "gaoming13/wechat-php-sdk": "<=1.10.2",
                "genix/cms": "<=1.1.11",
                "georgringer/news": "<1.3.3",
                "geshi/geshi": "<=1.0.9.1",
                "getformwork/formwork": "<2.2",
                "getgrav/grav": "<1.11.0.0-beta1",
                "getkirby/cms": "<3.9.8.3-dev|>=3.10,<3.10.1.2-dev|>=4,<4.7.1|>=5,<=5.2.1",
                "getkirby/kirby": "<3.9.8.3-dev|>=3.10,<3.10.1.2-dev|>=4,<4.7.1",
                "getkirby/panel": "<2.5.14",
                "getkirby/starterkit": "<=3.7.0.2",
                "gilacms/gila": "<=1.15.4",
                "gleez/cms": "<=1.3|==2",
                "globalpayments/php-sdk": "<2",
                "goalgorilla/open_social": "<12.3.11|>=12.4,<12.4.10|>=13.0.0.0-alpha1,<13.0.0.0-alpha11",
                "gogentooss/samlbase": "<1.2.7",
                "google/protobuf": "<3.4",
                "gos/web-socket-bundle": "<1.10.4|>=2,<2.6.1|>=3,<3.3",
                "gp247/core": "<1.1.24",
                "gree/jose": "<2.2.1",
                "gregwar/rst": "<1.0.3",
                "grumpydictator/firefly-iii": "<6.1.17",
                "gugoan/economizzer": "<=0.9.0.0-beta1",
                "guzzlehttp/guzzle": "<6.5.8|>=7,<7.4.5",
                "guzzlehttp/oauth-subscriber": "<0.8.1",
                "guzzlehttp/psr7": "<1.9.1|>=2,<2.4.5",
                "haffner/jh_captcha": "<=2.1.3|>=3,<=3.0.2",
                "handcraftedinthealps/goodby-csv": "<1.4.3",
                "harvesthq/chosen": "<1.8.7",
                "helloxz/imgurl": "<=2.31",
                "hhxsv5/laravel-s": "<3.7.36",
                "hillelcoren/invoice-ninja": "<5.3.35",
                "himiklab/yii2-jqgrid-widget": "<1.0.8",
                "hjue/justwriting": "<=1",
                "hov/jobfair": "<1.0.13|>=2,<2.0.2",
                "httpsoft/http-message": "<1.0.12",
                "hyn/multi-tenant": ">=5.6,<5.7.2",
                "ibexa/admin-ui": ">=4.2,<4.2.3|>=4.6,<4.6.25|>=5,<5.0.3",
                "ibexa/admin-ui-assets": ">=4.6.0.0-alpha1,<4.6.21",
                "ibexa/core": ">=4,<4.0.7|>=4.1,<4.1.4|>=4.2,<4.2.3|>=4.5,<4.5.6|>=4.6,<4.6.2",
                "ibexa/fieldtype-richtext": ">=4.6,<4.6.25|>=5,<5.0.3",
                "ibexa/graphql": ">=2.5,<2.5.31|>=3.3,<3.3.28|>=4.2,<4.2.3",
                "ibexa/http-cache": ">=4.6,<4.6.14",
                "ibexa/post-install": "<1.0.16|>=4.6,<4.6.14",
                "ibexa/solr": ">=4.5,<4.5.4",
                "ibexa/user": ">=4,<4.4.3|>=5,<5.0.4",
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
                "impresspages/impresspages": "<1.0.13",
                "in2code/femanager": "<6.4.2|>=7,<7.5.3|>=8,<8.3.1",
                "in2code/ipandlanguageredirect": "<5.1.2",
                "in2code/lux": "<17.6.1|>=18,<24.0.2",
                "in2code/powermail": "<7.5.1|>=8,<8.5.1|>=9,<10.9.1|>=11,<12.5.3|==13",
                "innologi/typo3-appointments": "<2.0.6",
                "intelliants/subrion": "<4.2.2",
                "inter-mediator/inter-mediator": "==5.5",
                "ipl/web": "<0.10.1",
                "islandora/crayfish": "<4.1",
                "islandora/islandora": ">=2,<2.4.1",
                "ivankristianto/phpwhois": "<=4.3",
                "jackalope/jackalope-doctrine-dbal": "<1.7.4",
                "jambagecom/div2007": "<0.10.2",
                "james-heinrich/getid3": "<1.9.21",
                "james-heinrich/phpthumb": "<=1.7.23",
                "jasig/phpcas": "<1.3.3",
                "jbartels/wec-map": "<3.0.3",
                "jcbrand/converse.js": "<3.3.3",
                "joelbutcher/socialstream": "<5.6|>=6,<6.2",
                "johnbillion/wp-crontrol": "<1.16.2|>=1.17,<1.19.2",
                "joomla/application": "<1.0.13",
                "joomla/archive": "<1.1.12|>=2,<2.0.1",
                "joomla/database": ">=1,<2.2|>=3,<3.4",
                "joomla/filesystem": "<1.6.2|>=2,<2.0.1",
                "joomla/filter": "<2.0.6|>=3,<3.0.5|==4",
                "joomla/framework": "<1.5.7|>=2.5.4,<=3.8.12",
                "joomla/input": ">=2,<2.0.2",
                "joomla/joomla-cms": "<3.9.12|>=4,<4.4.13|>=5,<5.2.6",
                "joomla/joomla-platform": "<1.5.4",
                "joomla/session": "<1.3.1",
                "joyqi/hyper-down": "<=2.4.27",
                "jsdecena/laracom": "<2.0.9",
                "jsmitty12/phpwhois": "<5.1",
                "juzaweb/cms": "<=3.4.2",
                "jweiland/events2": "<8.3.8|>=9,<9.0.6",
                "jweiland/kk-downloader": "<1.2.2",
                "kazist/phpwhois": "<=4.2.6",
                "kelvinmo/simplexrd": "<3.1.1",
                "kevinpapst/kimai2": "<1.16.7",
                "khodakhah/nodcms": "<=3",
                "kimai/kimai": "<2.46",
                "kitodo/presentation": "<3.2.3|>=3.3,<3.3.4",
                "klaviyo/magento2-extension": ">=1,<3",
                "knplabs/knp-snappy": "<=1.4.2",
                "kohana/core": "<3.3.3",
                "koillection/koillection": "<1.6.12",
                "krayin/laravel-crm": "<=1.3",
                "kreait/firebase-php": ">=3.2,<3.8.1",
                "kumbiaphp/kumbiapp": "<=1.1.1",
                "la-haute-societe/tcpdf": "<6.2.22",
                "laminas/laminas-diactoros": "<2.18.1|==2.19|==2.20|==2.21|==2.22|==2.23|>=2.24,<2.24.2|>=2.25,<2.25.2",
                "laminas/laminas-form": "<2.17.1|>=3,<3.0.2|>=3.1,<3.1.1",
                "laminas/laminas-http": "<2.14.2",
                "lara-zeus/artemis": ">=1,<=1.0.6",
                "lara-zeus/dynamic-dashboard": ">=3,<=3.0.1",
                "laravel/fortify": "<1.11.1",
                "laravel/framework": "<10.48.29|>=11,<11.44.1|>=12,<12.1.1",
                "laravel/laravel": ">=5.4,<5.4.22",
                "laravel/pulse": "<1.3.1",
                "laravel/reverb": "<1.7",
                "laravel/socialite": ">=1,<2.0.10",
                "latte/latte": "<2.10.8",
                "lavalite/cms": "<=10.1",
                "lavitto/typo3-form-to-database": "<2.2.5|>=3,<3.2.2|>=4,<4.2.3|>=5,<5.0.2",
                "lcobucci/jwt": ">=3.4,<3.4.6|>=4,<4.0.4|>=4.1,<4.1.5",
                "league/commonmark": "<2.7",
                "league/flysystem": "<1.1.4|>=2,<2.1.1",
                "league/oauth2-server": ">=8.3.2,<8.4.2|>=8.5,<8.5.3",
                "leantime/leantime": "<3.3",
                "lexik/jwt-authentication-bundle": "<2.10.7|>=2.11,<2.11.3",
                "libreform/libreform": ">=2,<=2.0.8",
                "librenms/librenms": "<25.12",
                "liftkit/database": "<2.13.2",
                "lightsaml/lightsaml": "<1.3.5",
                "limesurvey/limesurvey": "<6.5.12",
                "livehelperchat/livehelperchat": "<=3.91",
                "livewire-filemanager/filemanager": "<=1.0.4",
                "livewire/livewire": "<2.12.7|>=3.0.0.0-beta1,<3.6.4",
                "livewire/volt": "<1.7",
                "lms/routes": "<2.1.1",
                "localizationteam/l10nmgr": "<7.4|>=8,<8.7|>=9,<9.2",
                "lomkit/laravel-rest-api": "<2.13",
                "luracast/restler": "<3.1",
                "luyadev/yii-helpers": "<1.2.1",
                "macropay-solutions/laravel-crud-wizard-free": "<3.4.17",
                "maestroerror/php-heic-to-jpg": "<1.0.5",
                "magento/community-edition": "<2.4.6.0-patch13|>=2.4.7.0-beta1,<2.4.7.0-patch8|>=2.4.8.0-beta1,<2.4.8.0-patch3|>=2.4.9.0-alpha1,<2.4.9.0-alpha3|==2.4.9",
                "magento/core": "<=1.9.4.5",
                "magento/magento1ce": "<1.9.4.3-dev",
                "magento/magento1ee": ">=1,<1.14.4.3-dev",
                "magento/product-community-edition": "<2.4.4.0-patch9|>=2.4.5,<2.4.5.0-patch8|>=2.4.6,<2.4.6.0-patch6|>=2.4.7,<2.4.7.0-patch1",
                "magento/project-community-edition": "<=2.0.2",
                "magneto/core": "<1.9.4.4-dev",
                "mahocommerce/maho": "<25.9",
                "maikuolan/phpmussel": ">=1,<1.6",
                "mainwp/mainwp": "<=4.4.3.3",
                "manogi/nova-tiptap": "<=3.2.6",
                "mantisbt/mantisbt": "<2.27.2",
                "marcwillmann/turn": "<0.3.3",
                "marshmallow/nova-tiptap": "<5.7",
                "matomo/matomo": "<1.11",
                "matyhtf/framework": "<3.0.6",
                "mautic/core": "<5.2.9|>=6,<6.0.7",
                "mautic/core-lib": ">=1.0.0.0-beta,<4.4.13|>=5.0.0.0-alpha,<5.1.1",
                "mautic/grapes-js-builder-bundle": ">=4,<4.4.18|>=5,<5.2.9|>=6,<6.0.7",
                "maximebf/debugbar": "<1.19",
                "mdanter/ecc": "<2",
                "mediawiki/abuse-filter": "<1.39.9|>=1.40,<1.41.3|>=1.42,<1.42.2",
                "mediawiki/cargo": "<3.8.3",
                "mediawiki/core": "<1.39.5|==1.40",
                "mediawiki/data-transfer": ">=1.39,<1.39.11|>=1.41,<1.41.3|>=1.42,<1.42.2",
                "mediawiki/matomo": "<2.4.3",
                "mediawiki/semantic-media-wiki": "<4.0.2",
                "mehrwert/phpmyadmin": "<3.2",
                "melisplatform/melis-asset-manager": "<5.0.1",
                "melisplatform/melis-cms": "<5.3.4",
                "melisplatform/melis-cms-slider": "<5.3.1",
                "melisplatform/melis-core": "<5.3.11",
                "melisplatform/melis-front": "<5.0.1",
                "mezzio/mezzio-swoole": "<3.7|>=4,<4.3",
                "mgallegos/laravel-jqgrid": "<=1.3",
                "microsoft/microsoft-graph": ">=1.16,<1.109.1|>=2,<2.0.1",
                "microsoft/microsoft-graph-beta": "<2.0.1",
                "microsoft/microsoft-graph-core": "<2.0.2",
                "microweber/microweber": "<2.0.20",
                "mikehaertl/php-shellcommand": "<1.6.1",
                "mineadmin/mineadmin": "<=3.0.9",
                "miniorange/miniorange-saml": "<1.4.3",
                "mittwald/typo3_forum": "<1.2.1",
                "mobiledetect/mobiledetectlib": "<2.8.32",
                "modx/revolution": "<=3.1",
                "mojo42/jirafeau": "<4.4",
                "mongodb/mongodb": ">=1,<1.9.2",
                "mongodb/mongodb-extension": "<1.21.2",
                "monolog/monolog": ">=1.8,<1.12",
                "moodle/moodle": "<4.4.12|>=4.5.0.0-beta,<4.5.8|>=5.0.0.0-beta,<5.0.4|>=5.1.0.0-beta,<5.1.1",
                "moonshine/moonshine": "<=3.12.5",
                "mos/cimage": "<0.7.19",
                "movim/moxl": ">=0.8,<=0.10",
                "movingbytes/social-network": "<=1.2.1",
                "mpdf/mpdf": "<=7.1.7",
                "munkireport/comment": "<4",
                "munkireport/managedinstalls": "<2.6",
                "munkireport/munki_facts": "<1.5",
                "munkireport/reportdata": "<3.5",
                "munkireport/softwareupdate": "<1.6",
                "mustache/mustache": ">=2,<2.14.1",
                "mwdelaney/wp-enable-svg": "<=0.2",
                "namshi/jose": "<2.2",
                "nasirkhan/laravel-starter": "<11.11",
                "nategood/httpful": "<1",
                "neoan3-apps/template": "<1.1.1",
                "neorazorx/facturascripts": "<2022.04",
                "neos/flow": ">=1,<1.0.4|>=1.1,<1.1.1|>=2,<2.0.1|>=2.3,<2.3.16|>=3,<3.0.12|>=3.1,<3.1.10|>=3.2,<3.2.13|>=3.3,<3.3.13|>=4,<4.0.6",
                "neos/form": ">=1.2,<4.3.3|>=5,<5.0.9|>=5.1,<5.1.3",
                "neos/media-browser": "<7.3.19|>=8,<8.0.16|>=8.1,<8.1.11|>=8.2,<8.2.11|>=8.3,<8.3.9",
                "neos/neos": ">=1.1,<1.1.3|>=1.2,<1.2.13|>=2,<2.0.4|>=2.3,<3.0.20|>=3.1,<3.1.18|>=3.2,<3.2.14|>=3.3,<5.3.10|>=7,<7.0.9|>=7.1,<7.1.7|>=7.2,<7.2.6|>=7.3,<7.3.4|>=8,<8.0.2",
                "neos/swiftmailer": "<5.4.5",
                "nesbot/carbon": "<2.72.6|>=3,<3.8.4",
                "netcarver/textile": "<=4.1.2",
                "netgen/tagsbundle": ">=3.4,<3.4.11|>=4,<4.0.15",
                "nette/application": ">=2,<2.0.19|>=2.1,<2.1.13|>=2.2,<2.2.10|>=2.3,<2.3.14|>=2.4,<2.4.16|>=3,<3.0.6",
                "nette/nette": ">=2,<2.0.19|>=2.1,<2.1.13",
                "neuron-core/neuron-ai": "<=2.8.11",
                "nilsteampassnet/teampass": "<3.1.3.1-dev",
                "nitsan/ns-backup": "<13.0.1",
                "nonfiction/nterchange": "<4.1.1",
                "notrinos/notrinos-erp": "<=0.7",
                "noumo/easyii": "<=0.9",
                "novaksolutions/infusionsoft-php-sdk": "<1",
                "novosga/novosga": "<=2.2.12",
                "nukeviet/nukeviet": "<4.5.02",
                "nyholm/psr7": "<1.6.1",
                "nystudio107/craft-seomatic": "<3.4.12",
                "nzedb/nzedb": "<0.8",
                "nzo/url-encryptor-bundle": ">=4,<4.3.2|>=5,<5.0.1",
                "october/backend": "<1.1.2",
                "october/cms": "<1.0.469|==1.0.469|==1.0.471|==1.1.1",
                "october/october": "<3.7.5",
                "october/rain": "<1.0.472|>=1.1,<1.1.2",
                "october/system": "<=3.7.12|>=4,<=4.0.11",
                "oliverklee/phpunit": "<3.5.15",
                "omeka/omeka-s": "<4.0.3",
                "onelogin/php-saml": "<2.21.1|>=3,<3.8.1|>=4,<4.3.1",
                "oneup/uploader-bundle": ">=1,<1.9.3|>=2,<2.1.5",
                "open-web-analytics/open-web-analytics": "<1.8.1",
                "opencart/opencart": ">=0",
                "openid/php-openid": "<2.3",
                "openmage/magento-lts": "<20.16.1",
                "opensolutions/vimbadmin": "<=3.0.15",
                "opensource-workshop/connect-cms": "<1.8.7|>=2,<2.4.7",
                "orchid/platform": ">=8,<14.43",
                "oro/calendar-bundle": ">=4.2,<=4.2.6|>=5,<=5.0.6|>=5.1,<5.1.1",
                "oro/commerce": ">=4.1,<5.0.11|>=5.1,<5.1.1",
                "oro/crm": ">=1.7,<1.7.4|>=3.1,<4.1.17|>=4.2,<4.2.7",
                "oro/crm-call-bundle": ">=4.2,<=4.2.5|>=5,<5.0.4|>=5.1,<5.1.1",
                "oro/customer-portal": ">=4.1,<=4.1.13|>=4.2,<=4.2.10|>=5,<=5.0.11|>=5.1,<=5.1.3",
                "oro/platform": ">=1.7,<1.7.4|>=3.1,<3.1.29|>=4.1,<4.1.17|>=4.2,<=4.2.10|>=5,<=5.0.12|>=5.1,<=5.1.3",
                "oveleon/contao-cookiebar": "<1.16.3|>=2,<2.1.3",
                "oxid-esales/oxideshop-ce": "<=7.0.5",
                "oxid-esales/paymorrow-module": ">=1,<1.0.2|>=2,<2.0.1",
                "packbackbooks/lti-1-3-php-library": "<5",
                "padraic/humbug_get_contents": "<1.1.2",
                "pagarme/pagarme-php": "<3",
                "pagekit/pagekit": "<=1.0.18",
                "paragonie/ecc": "<2.0.1",
                "paragonie/random_compat": "<2",
                "paragonie/sodium_compat": "<1.24|>=2,<2.5",
                "passbolt/passbolt_api": "<4.6.2",
                "paypal/adaptivepayments-sdk-php": "<=3.9.2",
                "paypal/invoice-sdk-php": "<=3.9",
                "paypal/merchant-sdk-php": "<3.12",
                "paypal/permissions-sdk-php": "<=3.9.1",
                "pear/archive_tar": "<1.4.14",
                "pear/auth": "<1.2.4",
                "pear/crypt_gpg": "<1.6.7",
                "pear/http_request2": "<2.7",
                "pear/pear": "<=1.10.1",
                "pegasus/google-for-jobs": "<1.5.1|>=2,<2.1.1",
                "personnummer/personnummer": "<3.0.2",
                "ph7software/ph7builder": "<=17.9.1",
                "phanan/koel": "<5.1.4",
                "phenx/php-svg-lib": "<0.5.2",
                "php-censor/php-censor": "<2.0.13|>=2.1,<2.1.5",
                "php-mod/curl": "<2.3.2",
                "phpbb/phpbb": "<3.3.11",
                "phpems/phpems": ">=6,<=6.1.3",
                "phpfastcache/phpfastcache": "<6.1.5|>=7,<7.1.2|>=8,<8.0.7",
                "phpmailer/phpmailer": "<6.5",
                "phpmussel/phpmussel": ">=1,<1.6",
                "phpmyadmin/phpmyadmin": "<5.2.2",
                "phpmyfaq/phpmyfaq": "<=4.0.16",
                "phpoffice/common": "<0.2.9",
                "phpoffice/math": "<=0.2",
                "phpoffice/phpexcel": "<=1.8.2",
                "phpoffice/phpspreadsheet": "<1.30|>=2,<2.1.12|>=2.2,<2.4|>=3,<3.10|>=4,<5",
                "phppgadmin/phppgadmin": "<=7.13",
                "phpseclib/phpseclib": "<2.0.47|>=3,<3.0.36",
                "phpservermon/phpservermon": "<3.6",
                "phpsysinfo/phpsysinfo": "<3.4.3",
                "phpunit/phpunit": "<8.5.52|>=9,<9.6.33|>=10,<10.5.62|>=11,<11.5.50|>=12,<12.5.8",
                "phpwhois/phpwhois": "<=4.2.5",
                "phpxmlrpc/extras": "<0.6.1",
                "phpxmlrpc/phpxmlrpc": "<4.9.2",
                "pi/pi": "<=2.5",
                "pimcore/admin-ui-classic-bundle": "<=1.7.15|>=2.0.0.0-RC1-dev,<=2.2.2",
                "pimcore/customer-management-framework-bundle": "<4.2.1",
                "pimcore/data-hub": "<1.2.4",
                "pimcore/data-importer": "<1.8.9|>=1.9,<1.9.3",
                "pimcore/demo": "<10.3",
                "pimcore/ecommerce-framework-bundle": "<1.0.10",
                "pimcore/perspective-editor": "<1.5.1",
                "pimcore/pimcore": "<=11.5.13|>=12.0.0.0-RC1-dev,<12.3.1",
                "pimcore/web2print-tools-bundle": "<=5.2.1|>=6.0.0.0-RC1-dev,<=6.1",
                "piwik/piwik": "<1.11",
                "pixelfed/pixelfed": "<0.12.5",
                "plotly/plotly.js": "<2.25.2",
                "pocketmine/bedrock-protocol": "<8.0.2",
                "pocketmine/pocketmine-mp": "<5.32.1",
                "pocketmine/raklib": ">=0.14,<0.14.6|>=0.15,<0.15.1",
                "pressbooks/pressbooks": "<5.18",
                "prestashop/autoupgrade": ">=4,<4.10.1",
                "prestashop/blockreassurance": "<=5.1.3",
                "prestashop/blockwishlist": ">=2,<2.1.1",
                "prestashop/contactform": ">=1.0.1,<4.3",
                "prestashop/gamification": "<2.3.2",
                "prestashop/prestashop": "<8.2.4|>=9.0.0.0-alpha1,<9.0.3",
                "prestashop/productcomments": "<5.0.2",
                "prestashop/ps_checkout": "<4.4.1|>=5,<5.0.5",
                "prestashop/ps_contactinfo": "<=3.3.2",
                "prestashop/ps_emailsubscription": "<2.6.1",
                "prestashop/ps_facetedsearch": "<3.4.1",
                "prestashop/ps_linklist": "<3.1",
                "privatebin/privatebin": "<1.4|>=1.5,<1.7.4|>=1.7.7,<2.0.3",
                "processwire/processwire": "<=3.0.246",
                "propel/propel": ">=2.0.0.0-alpha1,<=2.0.0.0-alpha7",
                "propel/propel1": ">=1,<=1.7.1",
                "psy/psysh": "<=0.11.22|>=0.12,<=0.12.18",
                "pterodactyl/panel": "<1.12",
                "ptheofan/yii2-statemachine": ">=2.0.0.0-RC1-dev,<=2",
                "ptrofimov/beanstalk_console": "<1.7.14",
                "pubnub/pubnub": "<6.1",
                "punktde/pt_extbase": "<1.5.1",
                "pusher/pusher-php-server": "<2.2.1",
                "pwweb/laravel-core": "<=0.3.6.0-beta",
                "pxlrbt/filament-excel": "<1.1.14|>=2.0.0.0-alpha,<2.3.3",
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
                "redaxo/source": "<=5.20.1",
                "remdex/livehelperchat": "<4.29",
                "renolit/reint-downloadmanager": "<4.0.2|>=5,<5.0.1",
                "reportico-web/reportico": "<=8.1",
                "rhukster/dom-sanitizer": "<1.0.7",
                "rmccue/requests": ">=1.6,<1.8",
                "robrichards/xmlseclibs": "<=3.1.3",
                "roots/soil": "<4.1",
                "roundcube/roundcubemail": "<1.5.10|>=1.6,<1.6.11",
                "rudloff/alltube": "<3.0.3",
                "rudloff/rtmpdump-bin": "<=2.3.1",
                "s-cart/core": "<=9.0.5",
                "s-cart/s-cart": "<6.9",
                "sabberworm/php-css-parser": ">=1,<1.0.1|>=2,<2.0.1|>=3,<3.0.1|>=4,<4.0.1|>=5,<5.0.9|>=5.1,<5.1.3|>=5.2,<5.2.1|>=6,<6.0.2|>=7,<7.0.4|>=8,<8.0.1|>=8.1,<8.1.1|>=8.2,<8.2.1|>=8.3,<8.3.1",
                "sabre/dav": ">=1.6,<1.7.11|>=1.8,<1.8.9",
                "samwilson/unlinked-wikibase": "<1.42",
                "scheb/two-factor-bundle": "<3.26|>=4,<4.11",
                "sensiolabs/connect": "<4.2.3",
                "serluck/phpwhois": "<=4.2.6",
                "setasign/fpdi": "<2.6.4",
                "sfroemken/url_redirect": "<=1.2.1",
                "sheng/yiicms": "<1.2.1",
                "shopware/core": "<6.6.10.9-dev|>=6.7,<6.7.6.1-dev",
                "shopware/platform": "<6.6.10.7-dev|>=6.7,<6.7.3.1-dev",
                "shopware/production": "<=6.3.5.2",
                "shopware/shopware": "<=5.7.17|>=6.4.6,<6.6.10.10-dev|>=6.7,<6.7.6.1-dev",
                "shopware/storefront": "<6.6.10.10-dev|>=6.7,<6.7.5.1-dev",
                "shopxo/shopxo": "<=6.4",
                "showdoc/showdoc": "<2.10.4",
                "shuchkin/simplexlsx": ">=1.0.12,<1.1.13",
                "silverstripe-australia/advancedreports": ">=1,<=2",
                "silverstripe/admin": "<1.13.19|>=2,<2.1.8",
                "silverstripe/assets": ">=1,<1.11.1",
                "silverstripe/cms": "<4.11.3",
                "silverstripe/comments": ">=1.3,<3.1.1",
                "silverstripe/forum": "<=0.6.1|>=0.7,<=0.7.3",
                "silverstripe/framework": "<5.3.23",
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
                "simogeo/filemanager": "<=2.5",
                "simple-updates/phpwhois": "<=1",
                "simplesamlphp/saml2": "<=4.16.15|>=5.0.0.0-alpha1,<=5.0.0.0-alpha19",
                "simplesamlphp/saml2-legacy": "<=4.16.15",
                "simplesamlphp/simplesamlphp": "<1.18.6",
                "simplesamlphp/simplesamlphp-module-infocard": "<1.0.1",
                "simplesamlphp/simplesamlphp-module-openid": "<1",
                "simplesamlphp/simplesamlphp-module-openidprovider": "<0.9",
                "simplesamlphp/xml-common": "<1.20",
                "simplesamlphp/xml-security": "==1.6.11",
                "simplito/elliptic-php": "<1.0.6",
                "sitegeist/fluid-components": "<3.5",
                "sjbr/sr-feuser-register": "<2.6.2|>=5.1,<12.5",
                "sjbr/sr-freecap": "<2.4.6|>=2.5,<2.5.3",
                "sjbr/static-info-tables": "<2.3.1",
                "slim/psr7": "<1.4.1|>=1.5,<1.5.1|>=1.6,<1.6.1",
                "slim/slim": "<2.6",
                "slub/slub-events": "<3.0.3",
                "smarty/smarty": "<4.5.3|>=5,<5.1.1",
                "snipe/snipe-it": "<=8.3.4",
                "socalnick/scn-social-auth": "<1.15.2",
                "socialiteproviders/steam": "<1.1",
                "solspace/craft-freeform": "<4.1.29|>=5,<=5.14.6",
                "soosyze/soosyze": "<=2",
                "spatie/browsershot": "<5.0.5",
                "spatie/image-optimizer": "<1.7.3",
                "spencer14420/sp-php-email-handler": "<1",
                "spipu/html2pdf": "<5.2.8",
                "spiral/roadrunner": "<2025.1",
                "spoon/library": "<1.4.1",
                "spoonity/tcpdf": "<6.2.22",
                "squizlabs/php_codesniffer": ">=1,<2.8.1|>=3,<3.0.1",
                "ssddanbrown/bookstack": "<24.05.1",
                "starcitizentools/citizen-skin": ">=1.9.4,<3.9",
                "starcitizentools/short-description": ">=4,<4.0.1",
                "starcitizentools/tabber-neue": ">=1.9.1,<2.7.2|>=3,<3.1.1",
                "starcitizenwiki/embedvideo": "<=4",
                "statamic/cms": "<=5.22",
                "stormpath/sdk": "<9.9.99",
                "studio-42/elfinder": "<=2.1.64",
                "studiomitte/friendlycaptcha": "<0.1.4",
                "subhh/libconnect": "<7.0.8|>=8,<8.1",
                "sukohi/surpass": "<1",
                "sulu/form-bundle": ">=2,<2.5.3",
                "sulu/sulu": "<1.6.44|>=2,<2.5.25|>=2.6,<2.6.9|>=3.0.0.0-alpha1,<3.0.0.0-alpha3",
                "sumocoders/framework-user-bundle": "<1.4",
                "superbig/craft-audit": "<3.0.2",
                "svewap/a21glossary": "<=0.4.10",
                "swag/paypal": "<5.4.4",
                "swiftmailer/swiftmailer": "<6.2.5",
                "swiftyedit/swiftyedit": "<1.2",
                "sylius/admin-bundle": ">=1,<1.0.17|>=1.1,<1.1.9|>=1.2,<1.2.2",
                "sylius/grid": ">=1,<1.1.19|>=1.2,<1.2.18|>=1.3,<1.3.13|>=1.4,<1.4.5|>=1.5,<1.5.1",
                "sylius/grid-bundle": "<1.10.1",
                "sylius/paypal-plugin": "<1.6.2|>=1.7,<1.7.2|>=2,<2.0.2",
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
                "symfony/http-client": ">=4.3,<5.4.47|>=6,<6.4.15|>=7,<7.1.8",
                "symfony/http-foundation": "<5.4.50|>=6,<6.4.29|>=7,<7.3.7",
                "symfony/http-kernel": ">=2,<4.4.50|>=5,<5.4.20|>=6,<6.0.20|>=6.1,<6.1.12|>=6.2,<6.2.6",
                "symfony/intl": ">=2.7,<2.7.38|>=2.8,<2.8.31|>=3,<3.2.14|>=3.3,<3.3.13",
                "symfony/maker-bundle": ">=1.27,<1.29.2|>=1.30,<1.31.1",
                "symfony/mime": ">=4.3,<4.3.8",
                "symfony/phpunit-bridge": ">=2.8,<2.8.50|>=3,<3.4.26|>=4,<4.1.12|>=4.2,<4.2.7",
                "symfony/polyfill": ">=1,<1.10",
                "symfony/polyfill-php55": ">=1,<1.10",
                "symfony/process": "<5.4.51|>=6,<6.4.33|>=7,<7.1.7|>=7.3,<7.3.11|>=7.4,<7.4.5|>=8,<8.0.5",
                "symfony/proxy-manager-bridge": ">=2.7,<2.7.51|>=2.8,<2.8.50|>=3,<3.4.26|>=4,<4.1.12|>=4.2,<4.2.7",
                "symfony/routing": ">=2,<2.0.19",
                "symfony/runtime": ">=5.3,<5.4.46|>=6,<6.4.14|>=7,<7.1.7",
                "symfony/security": ">=2,<2.7.51|>=2.8,<3.4.49|>=4,<4.4.24|>=5,<5.2.8",
                "symfony/security-bundle": ">=2,<4.4.50|>=5,<5.4.20|>=6,<6.0.20|>=6.1,<6.1.12|>=6.2,<6.4.10|>=7,<7.0.10|>=7.1,<7.1.3",
                "symfony/security-core": ">=2.4,<2.6.13|>=2.7,<2.7.9|>=2.7.30,<2.7.32|>=2.8,<3.4.49|>=4,<4.4.24|>=5,<5.2.9",
                "symfony/security-csrf": ">=2.4,<2.7.48|>=2.8,<2.8.41|>=3,<3.3.17|>=3.4,<3.4.11|>=4,<4.0.11",
                "symfony/security-guard": ">=2.8,<3.4.48|>=4,<4.4.23|>=5,<5.2.8",
                "symfony/security-http": ">=2.3,<2.3.41|>=2.4,<2.7.51|>=2.8,<2.8.50|>=3,<3.4.26|>=4,<4.2.12|>=4.3,<4.3.8|>=4.4,<4.4.7|>=5,<5.0.7|>=5.1,<5.2.8|>=5.3,<5.4.47|>=6,<6.4.15|>=7,<7.1.8",
                "symfony/serializer": ">=2,<2.0.11|>=4.1,<4.4.35|>=5,<5.3.12",
                "symfony/symfony": "<5.4.51|>=6,<6.4.33|>=7,<7.3.11|>=7.4,<7.4.5|>=8,<8.0.5",
                "symfony/translation": ">=2,<2.0.17",
                "symfony/twig-bridge": ">=2,<4.4.51|>=5,<5.4.31|>=6,<6.3.8",
                "symfony/ux-autocomplete": "<2.11.2",
                "symfony/ux-live-component": "<2.25.1",
                "symfony/ux-twig-component": "<2.25.1",
                "symfony/validator": "<5.4.43|>=6,<6.4.11|>=7,<7.1.4",
                "symfony/var-exporter": ">=4.2,<4.2.12|>=4.3,<4.3.8",
                "symfony/web-profiler-bundle": ">=2,<2.3.19|>=2.4,<2.4.9|>=2.5,<2.5.4",
                "symfony/webhook": ">=6.3,<6.3.8",
                "symfony/yaml": ">=2,<2.0.22|>=2.1,<2.1.7|>=2.2.0.0-beta1,<2.2.0.0-beta2",
                "symphonycms/symphony-2": "<2.6.4",
                "t3/dce": "<0.11.5|>=2.2,<2.6.2",
                "t3g/svg-sanitizer": "<1.0.3",
                "t3s/content-consent": "<1.0.3|>=2,<2.0.2",
                "tastyigniter/tastyigniter": "<4",
                "tcg/voyager": "<=1.8",
                "tecnickcom/tc-lib-pdf-font": "<2.6.4",
                "tecnickcom/tcpdf": "<6.8",
                "terminal42/contao-tablelookupwizard": "<3.3.5",
                "thelia/backoffice-default-template": ">=2.1,<2.1.2",
                "thelia/thelia": ">=2.1,<2.1.3",
                "theonedemon/phpwhois": "<=4.2.5",
                "thinkcmf/thinkcmf": "<6.0.8",
                "thorsten/phpmyfaq": "<=4.0.16|>=4.1.0.0-alpha,<=4.1.0.0-beta2",
                "tikiwiki/tiki-manager": "<=17.1",
                "timber/timber": ">=0.16.6,<1.23.1|>=1.24,<1.24.1|>=2,<2.1",
                "tinymce/tinymce": "<7.2",
                "tinymighty/wiki-seo": "<1.2.2",
                "titon/framework": "<9.9.99",
                "tltneon/lgsl": "<7",
                "tobiasbg/tablepress": "<=2.0.0.0-RC1",
                "topthink/framework": "<6.0.17|>=6.1,<=8.0.4",
                "topthink/think": "<=6.1.1",
                "topthink/thinkphp": "<=3.2.3|>=6.1.3,<=8.0.4",
                "torrentpier/torrentpier": "<=2.8.8",
                "tpwd/ke_search": "<4.0.3|>=4.1,<4.6.6|>=5,<5.0.2",
                "tribalsystems/zenario": "<=9.7.61188",
                "truckersmp/phpwhois": "<=4.3.1",
                "ttskch/pagination-service-provider": "<1",
                "twbs/bootstrap": "<3.4.1|>=4,<4.3.1",
                "twig/twig": "<3.11.2|>=3.12,<3.14.1|>=3.16,<3.19",
                "typo3/cms": "<9.5.29|>=10,<10.4.35|>=11,<11.5.23|>=12,<12.2",
                "typo3/cms-backend": "<4.1.14|>=4.2,<4.2.15|>=4.3,<4.3.7|>=4.4,<4.4.4|>=7,<=7.6.50|>=8,<=8.7.39|>=9,<9.5.55|>=10,<=10.4.54|>=11,<=11.5.48|>=12,<=12.4.40|>=13,<=13.4.22|>=14,<=14.0.1",
                "typo3/cms-belog": ">=10,<=10.4.47|>=11,<=11.5.41|>=12,<=12.4.24|>=13,<=13.4.2",
                "typo3/cms-beuser": ">=9,<9.5.55|>=10,<10.4.54|>=11,<11.5.48|>=12,<12.4.37|>=13,<13.4.18",
                "typo3/cms-core": "<=8.7.56|>=9,<9.5.55|>=10,<=10.4.54|>=11,<=11.5.48|>=12,<=12.4.40|>=13,<=13.4.22|>=14,<=14.0.1",
                "typo3/cms-dashboard": ">=10,<10.4.54|>=11,<11.5.48|>=12,<12.4.37|>=13,<13.4.18",
                "typo3/cms-extbase": "<6.2.24|>=7,<7.6.8|==8.1.1",
                "typo3/cms-extensionmanager": ">=10,<=10.4.47|>=11,<=11.5.41|>=12,<=12.4.24|>=13,<=13.4.2",
                "typo3/cms-felogin": ">=4.2,<4.2.3",
                "typo3/cms-fluid": "<4.3.4|>=4.4,<4.4.1",
                "typo3/cms-form": ">=8,<=8.7.39|>=9,<=9.5.24|>=10,<=10.4.47|>=11,<=11.5.41|>=12,<=12.4.24|>=13,<=13.4.2",
                "typo3/cms-frontend": "<4.3.9|>=4.4,<4.4.5",
                "typo3/cms-indexed-search": ">=10,<=10.4.47|>=11,<=11.5.41|>=12,<=12.4.24|>=13,<=13.4.2",
                "typo3/cms-install": "<4.1.14|>=4.2,<4.2.16|>=4.3,<4.3.9|>=4.4,<4.4.5|>=12.2,<12.4.8|==13.4.2",
                "typo3/cms-lowlevel": ">=11,<=11.5.41",
                "typo3/cms-recordlist": ">=11,<11.5.48",
                "typo3/cms-recycler": ">=9,<9.5.55|>=10,<=10.4.54|>=11,<=11.5.48|>=12,<=12.4.40|>=13,<=13.4.22|>=14,<=14.0.1",
                "typo3/cms-redirects": ">=10,<=10.4.54|>=11,<=11.5.48|>=12,<=12.4.40|>=13,<=13.4.22|>=14,<=14.0.1",
                "typo3/cms-rte-ckeditor": ">=9.5,<9.5.42|>=10,<10.4.39|>=11,<11.5.30",
                "typo3/cms-scheduler": ">=11,<=11.5.41",
                "typo3/cms-setup": ">=9,<=9.5.50|>=10,<=10.4.49|>=11,<=11.5.43|>=12,<=12.4.30|>=13,<=13.4.11",
                "typo3/cms-webhooks": ">=12,<=12.4.30|>=13,<=13.4.11",
                "typo3/cms-workspaces": ">=9,<9.5.55|>=10,<10.4.54|>=11,<11.5.48|>=12,<12.4.37|>=13,<13.4.18",
                "typo3/flow": ">=1,<1.0.4|>=1.1,<1.1.1|>=2,<2.0.1|>=2.3,<2.3.16|>=3,<3.0.12|>=3.1,<3.1.10|>=3.2,<3.2.13|>=3.3,<3.3.13|>=4,<4.0.6",
                "typo3/html-sanitizer": ">=1,<=1.5.2|>=2,<=2.1.3",
                "typo3/neos": ">=1.1,<1.1.3|>=1.2,<1.2.13|>=2,<2.0.4|>=2.3,<2.3.99|>=3,<3.0.20|>=3.1,<3.1.18|>=3.2,<3.2.14|>=3.3,<3.3.23|>=4,<4.0.17|>=4.1,<4.1.16|>=4.2,<4.2.12|>=4.3,<4.3.3",
                "typo3/phar-stream-wrapper": ">=1,<2.1.1|>=3,<3.1.1",
                "typo3/swiftmailer": ">=4.1,<4.1.99|>=5.4,<5.4.5",
                "typo3fluid/fluid": ">=2,<2.0.8|>=2.1,<2.1.7|>=2.2,<2.2.4|>=2.3,<2.3.7|>=2.4,<2.4.4|>=2.5,<2.5.11|>=2.6,<2.6.10",
                "ua-parser/uap-php": "<3.8",
                "uasoft-indonesia/badaso": "<=2.9.7",
                "unisharp/laravel-filemanager": "<2.9.1",
                "universal-omega/dynamic-page-list3": "<3.6.4",
                "unopim/unopim": "<=0.3",
                "userfrosting/userfrosting": ">=0.3.1,<4.6.3",
                "usmanhalalit/pixie": "<1.0.3|>=2,<2.0.2",
                "uvdesk/community-skeleton": "<=1.1.1",
                "uvdesk/core-framework": "<=1.1.1",
                "vanilla/safecurl": "<0.9.2",
                "verbb/comments": "<1.5.5",
                "verbb/formie": "<=2.1.43",
                "verbb/image-resizer": "<2.0.9",
                "verbb/knock-knock": "<1.2.8",
                "verot/class.upload.php": "<=2.1.6",
                "vertexvaar/falsftp": "<0.2.6",
                "villagedefrance/opencart-overclocked": "<=1.11.1",
                "vova07/yii2-fileapi-widget": "<0.1.9",
                "vrana/adminer": "<=4.8.1",
                "vufind/vufind": ">=2,<9.1.1",
                "waldhacker/hcaptcha": "<2.1.2",
                "wallabag/tcpdf": "<6.2.22",
                "wallabag/wallabag": "<2.6.11",
                "wanglelecc/laracms": "<=1.0.3",
                "wapplersystems/a21glossary": "<=0.4.10",
                "web-auth/webauthn-framework": ">=3.3,<3.3.4|>=4.5,<4.9",
                "web-auth/webauthn-lib": ">=4.5,<4.9",
                "web-feet/coastercms": "==5.5",
                "web-tp3/wec_map": "<3.0.3",
                "webbuilders-group/silverstripe-kapost-bridge": "<0.4",
                "webcoast/deferred-image-processing": "<1.0.2",
                "webklex/laravel-imap": "<5.3",
                "webklex/php-imap": "<5.3",
                "webpa/webpa": "<3.1.2",
                "webreinvent/vaahcms": "<=2.3.1",
                "wikibase/wikibase": "<=1.39.3",
                "wikimedia/parsoid": "<0.12.2",
                "willdurand/js-translation-bundle": "<2.1.1",
                "winter/wn-backend-module": "<1.2.4",
                "winter/wn-cms-module": "<=1.2.9",
                "winter/wn-dusk-plugin": "<2.1",
                "winter/wn-system-module": "<1.2.4",
                "wintercms/winter": "<=1.2.3",
                "wireui/wireui": "<1.19.3|>=2,<2.1.3",
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
                "yeswiki/yeswiki": "<=4.5.4",
                "yetiforce/yetiforce-crm": "<6.5",
                "yidashi/yii2cmf": "<=2",
                "yii2mod/yii2-cms": "<1.9.2",
                "yiisoft/yii": "<1.1.31",
                "yiisoft/yii2": "<2.0.52",
                "yiisoft/yii2-authclient": "<2.2.15",
                "yiisoft/yii2-bootstrap": "<2.0.4",
                "yiisoft/yii2-dev": "<=2.0.45",
                "yiisoft/yii2-elasticsearch": "<2.0.5",
                "yiisoft/yii2-gii": "<=2.2.4",
                "yiisoft/yii2-jui": "<2.0.4",
                "yiisoft/yii2-redis": "<2.0.20",
                "yikesinc/yikes-inc-easy-mailchimp-extender": "<6.8.6",
                "yoast-seo-for-typo3/yoast_seo": "<7.2.3",
                "yourls/yourls": "<=1.10.2",
                "yuan1994/tpadmin": "<=1.3.12",
                "yungifez/skuul": "<=2.6.5",
                "z-push/z-push-dev": "<2.7.6",
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
            "time": "2026-02-05T22:08:29+00:00"
        },
        {
            "name": "sebastian/cli-parser",
            "version": "2.0.1",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/cli-parser.git",
                "reference": "c34583b87e7b7a8055bf6c450c2c77ce32a24084"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/cli-parser/zipball/c34583b87e7b7a8055bf6c450c2c77ce32a24084",
                "reference": "c34583b87e7b7a8055bf6c450c2c77ce32a24084",
                "shasum": ""
            },
            "require": {
                "php": ">=8.1"
            },
            "require-dev": {
                "phpunit/phpunit": "^10.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-main": "2.0-dev"
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
                "security": "https://github.com/sebastianbergmann/cli-parser/security/policy",
                "source": "https://github.com/sebastianbergmann/cli-parser/tree/2.0.1"
            },
            "funding": [
                {
                    "url": "https://github.com/sebastianbergmann",
                    "type": "github"
                }
            ],
            "time": "2024-03-02T07:12:49+00:00"
        },
        {
            "name": "sebastian/code-unit",
            "version": "2.0.0",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/code-unit.git",
                "reference": "a81fee9eef0b7a76af11d121767abc44c104e503"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/code-unit/zipball/a81fee9eef0b7a76af11d121767abc44c104e503",
                "reference": "a81fee9eef0b7a76af11d121767abc44c104e503",
                "shasum": ""
            },
            "require": {
                "php": ">=8.1"
            },
            "require-dev": {
                "phpunit/phpunit": "^10.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-main": "2.0-dev"
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
                "source": "https://github.com/sebastianbergmann/code-unit/tree/2.0.0"
            },
            "funding": [
                {
                    "url": "https://github.com/sebastianbergmann",
                    "type": "github"
                }
            ],
            "time": "2023-02-03T06:58:43+00:00"
        },
        {
            "name": "sebastian/code-unit-reverse-lookup",
            "version": "3.0.0",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/code-unit-reverse-lookup.git",
                "reference": "5e3a687f7d8ae33fb362c5c0743794bbb2420a1d"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/code-unit-reverse-lookup/zipball/5e3a687f7d8ae33fb362c5c0743794bbb2420a1d",
                "reference": "5e3a687f7d8ae33fb362c5c0743794bbb2420a1d",
                "shasum": ""
            },
            "require": {
                "php": ">=8.1"
            },
            "require-dev": {
                "phpunit/phpunit": "^10.0"
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
            "description": "Looks up which function or method a line of code belongs to",
            "homepage": "https://github.com/sebastianbergmann/code-unit-reverse-lookup/",
            "support": {
                "issues": "https://github.com/sebastianbergmann/code-unit-reverse-lookup/issues",
                "source": "https://github.com/sebastianbergmann/code-unit-reverse-lookup/tree/3.0.0"
            },
            "funding": [
                {
                    "url": "https://github.com/sebastianbergmann",
                    "type": "github"
                }
            ],
            "time": "2023-02-03T06:59:15+00:00"
        },
        {
            "name": "sebastian/comparator",
            "version": "5.0.5",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/comparator.git",
                "reference": "55dfef806eb7dfeb6e7a6935601fef866f8ca48d"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/comparator/zipball/55dfef806eb7dfeb6e7a6935601fef866f8ca48d",
                "reference": "55dfef806eb7dfeb6e7a6935601fef866f8ca48d",
                "shasum": ""
            },
            "require": {
                "ext-dom": "*",
                "ext-mbstring": "*",
                "php": ">=8.1",
                "sebastian/diff": "^5.0",
                "sebastian/exporter": "^5.0"
            },
            "require-dev": {
                "phpunit/phpunit": "^10.5"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-main": "5.0-dev"
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
                "security": "https://github.com/sebastianbergmann/comparator/security/policy",
                "source": "https://github.com/sebastianbergmann/comparator/tree/5.0.5"
            },
            "funding": [
                {
                    "url": "https://github.com/sebastianbergmann",
                    "type": "github"
                },
                {
                    "url": "https://liberapay.com/sebastianbergmann",
                    "type": "liberapay"
                },
                {
                    "url": "https://thanks.dev/u/gh/sebastianbergmann",
                    "type": "thanks_dev"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/sebastian/comparator",
                    "type": "tidelift"
                }
            ],
            "time": "2026-01-24T09:25:16+00:00"
        },
        {
            "name": "sebastian/complexity",
            "version": "3.2.0",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/complexity.git",
                "reference": "68ff824baeae169ec9f2137158ee529584553799"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/complexity/zipball/68ff824baeae169ec9f2137158ee529584553799",
                "reference": "68ff824baeae169ec9f2137158ee529584553799",
                "shasum": ""
            },
            "require": {
                "nikic/php-parser": "^4.18 || ^5.0",
                "php": ">=8.1"
            },
            "require-dev": {
                "phpunit/phpunit": "^10.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-main": "3.2-dev"
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
                "security": "https://github.com/sebastianbergmann/complexity/security/policy",
                "source": "https://github.com/sebastianbergmann/complexity/tree/3.2.0"
            },
            "funding": [
                {
                    "url": "https://github.com/sebastianbergmann",
                    "type": "github"
                }
            ],
            "time": "2023-12-21T08:37:17+00:00"
        },
        {
            "name": "sebastian/diff",
            "version": "5.1.1",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/diff.git",
                "reference": "c41e007b4b62af48218231d6c2275e4c9b975b2e"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/diff/zipball/c41e007b4b62af48218231d6c2275e4c9b975b2e",
                "reference": "c41e007b4b62af48218231d6c2275e4c9b975b2e",
                "shasum": ""
            },
            "require": {
                "php": ">=8.1"
            },
            "require-dev": {
                "phpunit/phpunit": "^10.0",
                "symfony/process": "^6.4"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-main": "5.1-dev"
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
                "security": "https://github.com/sebastianbergmann/diff/security/policy",
                "source": "https://github.com/sebastianbergmann/diff/tree/5.1.1"
            },
            "funding": [
                {
                    "url": "https://github.com/sebastianbergmann",
                    "type": "github"
                }
            ],
            "time": "2024-03-02T07:15:17+00:00"
        },
        {
            "name": "sebastian/environment",
            "version": "6.1.0",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/environment.git",
                "reference": "8074dbcd93529b357029f5cc5058fd3e43666984"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/environment/zipball/8074dbcd93529b357029f5cc5058fd3e43666984",
                "reference": "8074dbcd93529b357029f5cc5058fd3e43666984",
                "shasum": ""
            },
            "require": {
                "php": ">=8.1"
            },
            "require-dev": {
                "phpunit/phpunit": "^10.0"
            },
            "suggest": {
                "ext-posix": "*"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-main": "6.1-dev"
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
            "homepage": "https://github.com/sebastianbergmann/environment",
            "keywords": [
                "Xdebug",
                "environment",
                "hhvm"
            ],
            "support": {
                "issues": "https://github.com/sebastianbergmann/environment/issues",
                "security": "https://github.com/sebastianbergmann/environment/security/policy",
                "source": "https://github.com/sebastianbergmann/environment/tree/6.1.0"
            },
            "funding": [
                {
                    "url": "https://github.com/sebastianbergmann",
                    "type": "github"
                }
            ],
            "time": "2024-03-23T08:47:14+00:00"
        },
        {
            "name": "sebastian/exporter",
            "version": "5.1.4",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/exporter.git",
                "reference": "0735b90f4da94969541dac1da743446e276defa6"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/exporter/zipball/0735b90f4da94969541dac1da743446e276defa6",
                "reference": "0735b90f4da94969541dac1da743446e276defa6",
                "shasum": ""
            },
            "require": {
                "ext-mbstring": "*",
                "php": ">=8.1",
                "sebastian/recursion-context": "^5.0"
            },
            "require-dev": {
                "phpunit/phpunit": "^10.5"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-main": "5.1-dev"
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
                "security": "https://github.com/sebastianbergmann/exporter/security/policy",
                "source": "https://github.com/sebastianbergmann/exporter/tree/5.1.4"
            },
            "funding": [
                {
                    "url": "https://github.com/sebastianbergmann",
                    "type": "github"
                },
                {
                    "url": "https://liberapay.com/sebastianbergmann",
                    "type": "liberapay"
                },
                {
                    "url": "https://thanks.dev/u/gh/sebastianbergmann",
                    "type": "thanks_dev"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/sebastian/exporter",
                    "type": "tidelift"
                }
            ],
            "time": "2025-09-24T06:09:11+00:00"
        },
        {
            "name": "sebastian/global-state",
            "version": "6.0.2",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/global-state.git",
                "reference": "987bafff24ecc4c9ac418cab1145b96dd6e9cbd9"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/global-state/zipball/987bafff24ecc4c9ac418cab1145b96dd6e9cbd9",
                "reference": "987bafff24ecc4c9ac418cab1145b96dd6e9cbd9",
                "shasum": ""
            },
            "require": {
                "php": ">=8.1",
                "sebastian/object-reflector": "^3.0",
                "sebastian/recursion-context": "^5.0"
            },
            "require-dev": {
                "ext-dom": "*",
                "phpunit/phpunit": "^10.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-main": "6.0-dev"
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
            "homepage": "https://www.github.com/sebastianbergmann/global-state",
            "keywords": [
                "global state"
            ],
            "support": {
                "issues": "https://github.com/sebastianbergmann/global-state/issues",
                "security": "https://github.com/sebastianbergmann/global-state/security/policy",
                "source": "https://github.com/sebastianbergmann/global-state/tree/6.0.2"
            },
            "funding": [
                {
                    "url": "https://github.com/sebastianbergmann",
                    "type": "github"
                }
            ],
            "time": "2024-03-02T07:19:19+00:00"
        },
        {
            "name": "sebastian/lines-of-code",
            "version": "2.0.2",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/lines-of-code.git",
                "reference": "856e7f6a75a84e339195d48c556f23be2ebf75d0"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/lines-of-code/zipball/856e7f6a75a84e339195d48c556f23be2ebf75d0",
                "reference": "856e7f6a75a84e339195d48c556f23be2ebf75d0",
                "shasum": ""
            },
            "require": {
                "nikic/php-parser": "^4.18 || ^5.0",
                "php": ">=8.1"
            },
            "require-dev": {
                "phpunit/phpunit": "^10.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-main": "2.0-dev"
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
                "security": "https://github.com/sebastianbergmann/lines-of-code/security/policy",
                "source": "https://github.com/sebastianbergmann/lines-of-code/tree/2.0.2"
            },
            "funding": [
                {
                    "url": "https://github.com/sebastianbergmann",
                    "type": "github"
                }
            ],
            "time": "2023-12-21T08:38:20+00:00"
        },
        {
            "name": "sebastian/object-enumerator",
            "version": "5.0.0",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/object-enumerator.git",
                "reference": "202d0e344a580d7f7d04b3fafce6933e59dae906"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/object-enumerator/zipball/202d0e344a580d7f7d04b3fafce6933e59dae906",
                "reference": "202d0e344a580d7f7d04b3fafce6933e59dae906",
                "shasum": ""
            },
            "require": {
                "php": ">=8.1",
                "sebastian/object-reflector": "^3.0",
                "sebastian/recursion-context": "^5.0"
            },
            "require-dev": {
                "phpunit/phpunit": "^10.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-main": "5.0-dev"
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
                "source": "https://github.com/sebastianbergmann/object-enumerator/tree/5.0.0"
            },
            "funding": [
                {
                    "url": "https://github.com/sebastianbergmann",
                    "type": "github"
                }
            ],
            "time": "2023-02-03T07:08:32+00:00"
        },
        {
            "name": "sebastian/object-reflector",
            "version": "3.0.0",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/object-reflector.git",
                "reference": "24ed13d98130f0e7122df55d06c5c4942a577957"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/object-reflector/zipball/24ed13d98130f0e7122df55d06c5c4942a577957",
                "reference": "24ed13d98130f0e7122df55d06c5c4942a577957",
                "shasum": ""
            },
            "require": {
                "php": ">=8.1"
            },
            "require-dev": {
                "phpunit/phpunit": "^10.0"
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
            "description": "Allows reflection of object attributes, including inherited and non-public ones",
            "homepage": "https://github.com/sebastianbergmann/object-reflector/",
            "support": {
                "issues": "https://github.com/sebastianbergmann/object-reflector/issues",
                "source": "https://github.com/sebastianbergmann/object-reflector/tree/3.0.0"
            },
            "funding": [
                {
                    "url": "https://github.com/sebastianbergmann",
                    "type": "github"
                }
            ],
            "time": "2023-02-03T07:06:18+00:00"
        },
        {
            "name": "sebastian/recursion-context",
            "version": "5.0.1",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/recursion-context.git",
                "reference": "47e34210757a2f37a97dcd207d032e1b01e64c7a"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/recursion-context/zipball/47e34210757a2f37a97dcd207d032e1b01e64c7a",
                "reference": "47e34210757a2f37a97dcd207d032e1b01e64c7a",
                "shasum": ""
            },
            "require": {
                "php": ">=8.1"
            },
            "require-dev": {
                "phpunit/phpunit": "^10.5"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-main": "5.0-dev"
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
                "security": "https://github.com/sebastianbergmann/recursion-context/security/policy",
                "source": "https://github.com/sebastianbergmann/recursion-context/tree/5.0.1"
            },
            "funding": [
                {
                    "url": "https://github.com/sebastianbergmann",
                    "type": "github"
                },
                {
                    "url": "https://liberapay.com/sebastianbergmann",
                    "type": "liberapay"
                },
                {
                    "url": "https://thanks.dev/u/gh/sebastianbergmann",
                    "type": "thanks_dev"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/sebastian/recursion-context",
                    "type": "tidelift"
                }
            ],
            "time": "2025-08-10T07:50:56+00:00"
        },
        {
            "name": "sebastian/type",
            "version": "4.0.0",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/type.git",
                "reference": "462699a16464c3944eefc02ebdd77882bd3925bf"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/type/zipball/462699a16464c3944eefc02ebdd77882bd3925bf",
                "reference": "462699a16464c3944eefc02ebdd77882bd3925bf",
                "shasum": ""
            },
            "require": {
                "php": ">=8.1"
            },
            "require-dev": {
                "phpunit/phpunit": "^10.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-main": "4.0-dev"
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
                "source": "https://github.com/sebastianbergmann/type/tree/4.0.0"
            },
            "funding": [
                {
                    "url": "https://github.com/sebastianbergmann",
                    "type": "github"
                }
            ],
            "time": "2023-02-03T07:10:45+00:00"
        },
        {
            "name": "sebastian/version",
            "version": "4.0.1",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/version.git",
                "reference": "c51fa83a5d8f43f1402e3f32a005e6262244ef17"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/version/zipball/c51fa83a5d8f43f1402e3f32a005e6262244ef17",
                "reference": "c51fa83a5d8f43f1402e3f32a005e6262244ef17",
                "shasum": ""
            },
            "require": {
                "php": ">=8.1"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-main": "4.0-dev"
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
                "source": "https://github.com/sebastianbergmann/version/tree/4.0.1"
            },
            "funding": [
                {
                    "url": "https://github.com/sebastianbergmann",
                    "type": "github"
                }
            ],
            "time": "2023-02-07T11:34:05+00:00"
        },
        {
            "name": "slevomat/coding-standard",
            "version": "8.22.1",
            "source": {
                "type": "git",
                "url": "https://github.com/slevomat/coding-standard.git",
                "reference": "1dd80bf3b93692bedb21a6623c496887fad05fec"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/slevomat/coding-standard/zipball/1dd80bf3b93692bedb21a6623c496887fad05fec",
                "reference": "1dd80bf3b93692bedb21a6623c496887fad05fec",
                "shasum": ""
            },
            "require": {
                "dealerdirect/phpcodesniffer-composer-installer": "^0.6.2 || ^0.7 || ^1.1.2",
                "php": "^7.4 || ^8.0",
                "phpstan/phpdoc-parser": "^2.3.0",
                "squizlabs/php_codesniffer": "^3.13.4"
            },
            "require-dev": {
                "phing/phing": "3.0.1|3.1.0",
                "php-parallel-lint/php-parallel-lint": "1.4.0",
                "phpstan/phpstan": "2.1.24",
                "phpstan/phpstan-deprecation-rules": "2.0.3",
                "phpstan/phpstan-phpunit": "2.0.7",
                "phpstan/phpstan-strict-rules": "2.0.6",
                "phpunit/phpunit": "9.6.8|10.5.48|11.4.4|11.5.36|12.3.10"
            },
            "type": "phpcodesniffer-standard",
            "extra": {
                "branch-alias": {
                    "dev-master": "8.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "SlevomatCodingStandard\\": "SlevomatCodingStandard/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "description": "Slevomat Coding Standard for PHP_CodeSniffer complements Consistence Coding Standard by providing sniffs with additional checks.",
            "keywords": [
                "dev",
                "phpcs"
            ],
            "support": {
                "issues": "https://github.com/slevomat/coding-standard/issues",
                "source": "https://github.com/slevomat/coding-standard/tree/8.22.1"
            },
            "funding": [
                {
                    "url": "https://github.com/kukulich",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/slevomat/coding-standard",
                    "type": "tidelift"
                }
            ],
            "time": "2025-09-13T08:53:30+00:00"
        },
        {
            "name": "spatie/array-to-xml",
            "version": "3.4.4",
            "source": {
                "type": "git",
                "url": "https://github.com/spatie/array-to-xml.git",
                "reference": "88b2f3852a922dd73177a68938f8eb2ec70c7224"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/spatie/array-to-xml/zipball/88b2f3852a922dd73177a68938f8eb2ec70c7224",
                "reference": "88b2f3852a922dd73177a68938f8eb2ec70c7224",
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
                "source": "https://github.com/spatie/array-to-xml/tree/3.4.4"
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
            "time": "2025-12-15T09:00:41+00:00"
        },
        {
            "name": "squizlabs/php_codesniffer",
            "version": "3.13.5",
            "source": {
                "type": "git",
                "url": "https://github.com/PHPCSStandards/PHP_CodeSniffer.git",
                "reference": "0ca86845ce43291e8f5692c7356fccf3bcf02bf4"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/PHPCSStandards/PHP_CodeSniffer/zipball/0ca86845ce43291e8f5692c7356fccf3bcf02bf4",
                "reference": "0ca86845ce43291e8f5692c7356fccf3bcf02bf4",
                "shasum": ""
            },
            "require": {
                "ext-simplexml": "*",
                "ext-tokenizer": "*",
                "ext-xmlwriter": "*",
                "php": ">=5.4.0"
            },
            "require-dev": {
                "phpunit/phpunit": "^4.0 || ^5.0 || ^6.0 || ^7.0 || ^8.0 || ^9.3.4"
            },
            "bin": [
                "bin/phpcbf",
                "bin/phpcs"
            ],
            "type": "library",
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause"
            ],
            "authors": [
                {
                    "name": "Greg Sherwood",
                    "role": "Former lead"
                },
                {
                    "name": "Juliette Reinders Folmer",
                    "role": "Current lead"
                },
                {
                    "name": "Contributors",
                    "homepage": "https://github.com/PHPCSStandards/PHP_CodeSniffer/graphs/contributors"
                }
            ],
            "description": "PHP_CodeSniffer tokenizes PHP, JavaScript and CSS files and detects violations of a defined set of coding standards.",
            "homepage": "https://github.com/PHPCSStandards/PHP_CodeSniffer",
            "keywords": [
                "phpcs",
                "standards",
                "static analysis"
            ],
            "support": {
                "issues": "https://github.com/PHPCSStandards/PHP_CodeSniffer/issues",
                "security": "https://github.com/PHPCSStandards/PHP_CodeSniffer/security/policy",
                "source": "https://github.com/PHPCSStandards/PHP_CodeSniffer",
                "wiki": "https://github.com/PHPCSStandards/PHP_CodeSniffer/wiki"
            },
            "funding": [
                {
                    "url": "https://github.com/PHPCSStandards",
                    "type": "github"
                },
                {
                    "url": "https://github.com/jrfnl",
                    "type": "github"
                },
                {
                    "url": "https://opencollective.com/php_codesniffer",
                    "type": "open_collective"
                },
                {
                    "url": "https://thanks.dev/u/gh/phpcsstandards",
                    "type": "thanks_dev"
                }
            ],
            "time": "2025-11-04T16:30:35+00:00"
        },
        {
            "name": "sylius-labs/coding-standard",
            "version": "v4.5.0",
            "source": {
                "type": "git",
                "url": "https://github.com/SyliusLabs/CodingStandard.git",
                "reference": "91d3c9271a9ccc2eef2bd055dce5a286d84cf5d2"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/SyliusLabs/CodingStandard/zipball/91d3c9271a9ccc2eef2bd055dce5a286d84cf5d2",
                "reference": "91d3c9271a9ccc2eef2bd055dce5a286d84cf5d2",
                "shasum": ""
            },
            "require": {
                "php": "^8.0",
                "slevomat/coding-standard": "^8.0",
                "symplify/easy-coding-standard": "^10.0 || ^11.0 || ^12.0 || ^13.0"
            },
            "conflict": {
                "slevomat/coding-standard": ">=8.23",
                "symplify/package-builder": "^8.3"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "4.4-dev"
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
            "description": "Battle-tested coding standard configuration used in Sylius.",
            "support": {
                "issues": "https://github.com/SyliusLabs/CodingStandard/issues",
                "source": "https://github.com/SyliusLabs/CodingStandard/tree/v4.5.0"
            },
            "time": "2025-11-24T10:57:22+00:00"
        },
        {
            "name": "symfony/browser-kit",
            "version": "v7.4.4",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/browser-kit.git",
                "reference": "bed167eadaaba641f51fc842c9227aa5e251309e"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/browser-kit/zipball/bed167eadaaba641f51fc842c9227aa5e251309e",
                "reference": "bed167eadaaba641f51fc842c9227aa5e251309e",
                "shasum": ""
            },
            "require": {
                "php": ">=8.2",
                "symfony/deprecation-contracts": "^2.5|^3",
                "symfony/dom-crawler": "^6.4|^7.0|^8.0"
            },
            "require-dev": {
                "symfony/css-selector": "^6.4|^7.0|^8.0",
                "symfony/http-client": "^6.4|^7.0|^8.0",
                "symfony/mime": "^6.4|^7.0|^8.0",
                "symfony/process": "^6.4|^7.0|^8.0"
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
                "source": "https://github.com/symfony/browser-kit/tree/v7.4.4"
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
                    "url": "https://github.com/nicolas-grekas",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2026-01-13T10:40:19+00:00"
        },
        {
            "name": "symfony/css-selector",
            "version": "v7.4.0",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/css-selector.git",
                "reference": "ab862f478513e7ca2fe9ec117a6f01a8da6e1135"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/css-selector/zipball/ab862f478513e7ca2fe9ec117a6f01a8da6e1135",
                "reference": "ab862f478513e7ca2fe9ec117a6f01a8da6e1135",
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
                "source": "https://github.com/symfony/css-selector/tree/v7.4.0"
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
                    "url": "https://github.com/nicolas-grekas",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2025-10-30T13:39:42+00:00"
        },
        {
            "name": "symfony/dom-crawler",
            "version": "v7.4.4",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/dom-crawler.git",
                "reference": "71fd6a82fc357c8b5de22f78b228acfc43dee965"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/dom-crawler/zipball/71fd6a82fc357c8b5de22f78b228acfc43dee965",
                "reference": "71fd6a82fc357c8b5de22f78b228acfc43dee965",
                "shasum": ""
            },
            "require": {
                "masterminds/html5": "^2.6",
                "php": ">=8.2",
                "symfony/deprecation-contracts": "^2.5|^3",
                "symfony/polyfill-ctype": "~1.8",
                "symfony/polyfill-mbstring": "~1.0"
            },
            "require-dev": {
                "symfony/css-selector": "^6.4|^7.0|^8.0"
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
                "source": "https://github.com/symfony/dom-crawler/tree/v7.4.4"
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
                    "url": "https://github.com/nicolas-grekas",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2026-01-05T08:47:25+00:00"
        },
        {
            "name": "symfony/dotenv",
            "version": "v7.4.0",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/dotenv.git",
                "reference": "1658a4d34df028f3d93bcdd8e81f04423925a364"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/dotenv/zipball/1658a4d34df028f3d93bcdd8e81f04423925a364",
                "reference": "1658a4d34df028f3d93bcdd8e81f04423925a364",
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
                "symfony/console": "^6.4|^7.0|^8.0",
                "symfony/process": "^6.4|^7.0|^8.0"
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
                "source": "https://github.com/symfony/dotenv/tree/v7.4.0"
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
                    "url": "https://github.com/nicolas-grekas",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2025-11-16T10:14:42+00:00"
        },
        {
            "name": "symfony/phpunit-bridge",
            "version": "v7.4.3",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/phpunit-bridge.git",
                "reference": "f933e68bb9df29d08077a37e1515a23fea8562ab"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/phpunit-bridge/zipball/f933e68bb9df29d08077a37e1515a23fea8562ab",
                "reference": "f933e68bb9df29d08077a37e1515a23fea8562ab",
                "shasum": ""
            },
            "require": {
                "php": ">=8.1.0"
            },
            "require-dev": {
                "symfony/deprecation-contracts": "^2.5|^3",
                "symfony/error-handler": "^6.4.3|^7.0.3|^8.0"
            },
            "bin": [
                "bin/simple-phpunit"
            ],
            "type": "symfony-bridge",
            "extra": {
                "thanks": {
                    "url": "https://github.com/sebastianbergmann/phpunit",
                    "name": "phpunit/phpunit"
                }
            },
            "autoload": {
                "files": [
                    "bootstrap.php"
                ],
                "psr-4": {
                    "Symfony\\Bridge\\PhpUnit\\": ""
                },
                "exclude-from-classmap": [
                    "/Tests/",
                    "/bin/"
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
            "description": "Provides utilities for PHPUnit, especially user deprecation notices management",
            "homepage": "https://symfony.com",
            "keywords": [
                "testing"
            ],
            "support": {
                "source": "https://github.com/symfony/phpunit-bridge/tree/v7.4.3"
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
                    "url": "https://github.com/nicolas-grekas",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2025-12-09T15:33:45+00:00"
        },
        {
            "name": "symfony/web-profiler-bundle",
            "version": "v7.4.4",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/web-profiler-bundle.git",
                "reference": "be165e29e6109efb89bfaefe56e3deccf72a8643"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/web-profiler-bundle/zipball/be165e29e6109efb89bfaefe56e3deccf72a8643",
                "reference": "be165e29e6109efb89bfaefe56e3deccf72a8643",
                "shasum": ""
            },
            "require": {
                "composer-runtime-api": ">=2.1",
                "php": ">=8.2",
                "symfony/config": "^7.3|^8.0",
                "symfony/deprecation-contracts": "^2.5|^3",
                "symfony/framework-bundle": "^6.4.13|^7.1.6|^8.0",
                "symfony/http-kernel": "^6.4.13|^7.1.6|^8.0",
                "symfony/routing": "^6.4|^7.0|^8.0",
                "symfony/twig-bundle": "^6.4|^7.0|^8.0",
                "twig/twig": "^3.15"
            },
            "conflict": {
                "symfony/form": "<6.4",
                "symfony/mailer": "<6.4",
                "symfony/messenger": "<6.4",
                "symfony/serializer": "<7.2",
                "symfony/workflow": "<7.3"
            },
            "require-dev": {
                "symfony/browser-kit": "^6.4|^7.0|^8.0",
                "symfony/console": "^6.4|^7.0|^8.0",
                "symfony/css-selector": "^6.4|^7.0|^8.0",
                "symfony/runtime": "^6.4.13|^7.1.6|^8.0",
                "symfony/stopwatch": "^6.4|^7.0|^8.0"
            },
            "type": "symfony-bundle",
            "autoload": {
                "psr-4": {
                    "Symfony\\Bundle\\WebProfilerBundle\\": ""
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
            "description": "Provides a development tool that gives detailed information about the execution of any request",
            "homepage": "https://symfony.com",
            "keywords": [
                "dev"
            ],
            "support": {
                "source": "https://github.com/symfony/web-profiler-bundle/tree/v7.4.4"
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
                    "url": "https://github.com/nicolas-grekas",
                    "type": "github"
                },
                {
                    "url": "https://tidelift.com/funding/github/packagist/symfony/symfony",
                    "type": "tidelift"
                }
            ],
            "time": "2026-01-07T11:56:45+00:00"
        },
        {
            "name": "symplify/easy-coding-standard",
            "version": "13.0.4",
            "source": {
                "type": "git",
                "url": "https://github.com/easy-coding-standard/easy-coding-standard.git",
                "reference": "5c7e7a07e5d6a98b9dd2e6fc0a9155efb7c166c8"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/easy-coding-standard/easy-coding-standard/zipball/5c7e7a07e5d6a98b9dd2e6fc0a9155efb7c166c8",
                "reference": "5c7e7a07e5d6a98b9dd2e6fc0a9155efb7c166c8",
                "shasum": ""
            },
            "require": {
                "php": ">=7.2"
            },
            "conflict": {
                "friendsofphp/php-cs-fixer": "<3.92.4",
                "phpcsstandards/php_codesniffer": "<4.0.1",
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
                "source": "https://github.com/easy-coding-standard/easy-coding-standard/tree/13.0.4"
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
            "time": "2026-01-05T09:10:04+00:00"
        },
        {
            "name": "theseer/tokenizer",
            "version": "1.3.1",
            "source": {
                "type": "git",
                "url": "https://github.com/theseer/tokenizer.git",
                "reference": "b7489ce515e168639d17feec34b8847c326b0b3c"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/theseer/tokenizer/zipball/b7489ce515e168639d17feec34b8847c326b0b3c",
                "reference": "b7489ce515e168639d17feec34b8847c326b0b3c",
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
                "source": "https://github.com/theseer/tokenizer/tree/1.3.1"
            },
            "funding": [
                {
                    "url": "https://github.com/theseer",
                    "type": "github"
                }
            ],
            "time": "2025-11-17T20:03:58+00:00"
        },
        {
            "name": "vimeo/psalm",
            "version": "5.26.1",
            "source": {
                "type": "git",
                "url": "https://github.com/vimeo/psalm.git",
                "reference": "d747f6500b38ac4f7dfc5edbcae6e4b637d7add0"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/vimeo/psalm/zipball/d747f6500b38ac4f7dfc5edbcae6e4b637d7add0",
                "reference": "d747f6500b38ac4f7dfc5edbcae6e4b637d7add0",
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
                "nikic/php-parser": "^4.17",
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
                    "dev-1.x": "1.x-dev",
                    "dev-2.x": "2.x-dev",
                    "dev-3.x": "3.x-dev",
                    "dev-4.x": "4.x-dev",
                    "dev-master": "5.x-dev"
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
            "time": "2024-09-08T18:53:08+00:00"
        }
    ],
    "aliases": [],
    "minimum-stability": "stable",
    "stability-flags": {
        "roave/security-advisories": 20
    },
    "prefer-stable": false,
    "prefer-lowest": false,
    "platform": {
        "php": "^8.3",
        "ext-amqp": "*",
        "ext-json": "*"
    },
    "platform-dev": [],
    "plugin-api-version": "2.3.0"
}
```

## File: `deptrac.yaml`
```yaml
parameters:
  formatters:
    graphviz:
      groups:
        App:
          - Application
          - Domain
          - Infrastructure
          - Auth
          - UI
          - UIHealth
  paths:
    - ./src
  exclude_files:
  layers:
    - name: Domain
      collectors:
        - type: className
          regex: .*\\Domain\\.*
    - name: Application
      collectors:
        - type: className
          regex: .*Application\\.*
    - name: Infrastructure
      collectors:
        - type: bool
          must:
            - type: className
              regex: .*Infrastructure\\.*
          must_not:
            - type: className
              regex: .*User\\Infrastructure\\Auth\\Auth
    - name: Auth
      collectors:
        - type: className
          regex: .*User\\Infrastructure\\Auth\\Auth;
    - name: UI
      collectors:
        - type: bool
          must:
            - type: className
              regex: UI\\.*
          must_not:
            - type: className
              regex: UI\\Http\\Rest\\Controller\\Healthz\\.*
    - name: UIHealth
      collectors:
        - type: className
          regex: UI\\Http\\Rest\\Controller\\Healthz\\.*
  ruleset:
    Domain:
    Auth:
      - Domain
      - Infrastructure
    Application:
      - Domain
      - Infrastructure
      - Auth
    Infrastructure:
      - Domain
      - Application
      - Auth
    UI:
      - Auth
      - Domain
      - Application
    UIHealth: # Allow access to infra for health checks
      - Infrastructure
      - UI
```

## File: `docker-compose.yml`
```yaml
x-app-volumes: &app-volumes
  - ./:/app:rw,delegated
  # If you develop on Linux, comment out the following volumes to just use bind-mounted project directory from host
  - /app/var/
  - /app/var/cache/
  - /app/var/logs/
  - /app/var/sessions/

x-app-build: &app-build
  build:
    dockerfile: etc/artifact/Dockerfile
    context: .
    target: php-dev

services:

  nginx:
    image: nginx:1.27-alpine
    volumes:
      - ./etc/dev/nginx/nginx.conf:/etc/nginx/conf.d/default.conf:ro
      - ./public:/app/public:ro
    depends_on:
      php:
        condition: service_healthy

  code:
    <<: *app-build
    command: ["sleep", "infinity"]
    volumes: *app-volumes

  php:
    <<: *app-build
    environment:
      - XDEBUG_MODE=debug
      - XDEBUG_CLIENT_HOST=host.docker.internal
    volumes: *app-volumes
    healthcheck:
      test: ["CMD-SHELL", "php-fpm83 -t || exit 1"]
      interval: 5s
      timeout: 3s
      retries: 10
      start_period: 30s
    depends_on:
      mysql:
        condition: service_healthy
      rmq:
        condition: service_healthy
      elasticsearch:
        condition: service_healthy

  workers_events:
    <<: *app-build
    volumes: *app-volumes
    command: ['/app/bin/console', 'messenger:consume', 'events', '-vv', '--memory-limit=256M', '--time-limit=3600']
    restart: unless-stopped
    depends_on:
      mysql:
        condition: service_healthy
      rmq:
        condition: service_healthy
      elasticsearch:
        condition: service_healthy

  workers_users:
    <<: *app-build
    volumes: *app-volumes
    command: ['/app/bin/console', 'messenger:consume', 'users', '-vv', '--memory-limit=256M', '--time-limit=3600']
    restart: unless-stopped
    depends_on:
      mysql:
        condition: service_healthy
      rmq:
        condition: service_healthy
      elasticsearch:
        condition: service_healthy

  mysql:
    image: mysql:8.0.33
    command: --default-authentication-plugin=mysql_native_password
    volumes:
     - "./etc/ci/mysql:/etc/mysql/conf.d"
    tmpfs:
     - /var/lib/mysql/:rw,noexec,nosuid,size=600m
     - /tmp/:rw,noexec,nosuid,size=50m
    environment:
      - MYSQL_ROOT_PASSWORD=api
      - MYSQL_DATABASE=api
    healthcheck:
      test: ["CMD", "mysqladmin", "ping", "-h", "localhost", "-papi"]
      interval: 5s
      timeout: 5s
      retries: 10

  rmq:
    image: rabbitmq:3-management
    environment:
      RABBITMQ_ERLANG_COOKIE: "SWQOKODSQALRPCLNMEQG"
      RABBITMQ_DEFAULT_USER: "guest"
      RABBITMQ_DEFAULT_PASS: "guest"
      RABBITMQ_DEFAULT_VHOST: "/"
    healthcheck:
      test: ["CMD", "rabbitmq-diagnostics", "-q", "ping"]
      interval: 5s
      timeout: 5s
      retries: 10

  elasticsearch:
    image: docker.elastic.co/elasticsearch/elasticsearch:7.17.24
    environment:
      - "discovery.type=single-node"
      - "cluster.name=sf-events"
      - "ES_JAVA_OPTS=-Xms1g -Xmx1g"
    healthcheck:
      test: ["CMD-SHELL", "curl -fsSL http://localhost:9200/_cluster/health || exit 1"]
      interval: 5s
      timeout: 5s
      retries: 10
```

## File: `easy-coding-standard.yml`
```yaml
imports:
  - { resource: 'vendor/sylius-labs/coding-standard/easy-coding-standard.yml' }

services:
  PhpCsFixer\Fixer\FunctionNotation\NativeFunctionInvocationFixer: ~

parameters:
  exclude_files:
    - '**/var/*'
```

## File: `makefile`
```
env=dev
docker-os=
compose=docker compose -f docker-compose.yml -f etc/$(env)/docker-compose.yml

ifeq ($(docker-os), windows)
	ifeq ($(env), dev)
		compose += -f etc/dev/docker-compose.windows.yml
	endif
endif

export compose env docker-os

.PHONY: start
start: erase build start-deps up db ## clean current environment, recreate dependencies and spin up again

.PHONY: start-deps
start-deps:  ## Start all dependencies and wait for healthchecks
		$(compose) up -d --wait mysql rmq elasticsearch

.PHONY: stop
stop: ## stop environment
		$(compose) stop $(s)

.PHONY: rebuild
rebuild: start ## same as start

.PHONY: erase
erase: ## stop and delete containers, clean volumes.
		$(compose) stop
		docker compose rm -v -f

.PHONY: build
build: ## build environment and initialize composer and project dependencies
		$(compose) build --no-cache --parallel

		if [ env = "prod" ]; then \
			echo Building in $(env) mode; \
			$(compose) run --rm php sh -lc 'COMPOSER_MEMORY_LIMIT=-1 composer install --no-ansi --no-dev --no-interaction --no-plugins --no-progress --no-scripts --optimize-autoloader --ignore-platform-reqs'; \
		else \
			$(compose) run --rm php sh -lc 'COMPOSER_MEMORY_LIMIT=-1 composer install --ignore-platform-reqs'; \
		fi

.PHONY: artifact
artifact: ## build production artifact
		docker compose -f etc/artifact/docker-compose.yml build

.PHONY: composer-update
composer-update: ## Update project dependencies
		$(compose) run --rm code sh -lc 'COMPOSER_MEMORY_LIMIT=-1 composer update'

.PHONY: up
up: ## spin up environment
		$(compose) up -d --force-recreate

.PHONY: phpunit
phpunit: db ## execute project unit tests
		$(compose) exec -T php sh -lc "XDEBUG_MODE=coverage ./vendor/bin/phpunit $(conf)"

.PHONY: coverage
coverage:
		$(compose) run --rm php sh -lc "git config --global --add safe.directory /app; \
		composer global require php-coveralls/php-coveralls; \
		../root/.composer/vendor/bin/php-coveralls --coverage_clover=/app/build/logs/clover.xml -v "

.PHONY: phpstan
phpstan: ## executes php analyzers
		$(compose) run --rm code sh -lc './vendor/bin/phpstan analyse --memory-limit=512M'

.PHONY: psalm
psalm: ## execute psalm analyzer
		$(compose) run --rm code sh -lc './vendor/bin/psalm --show-info=false'

.PHONY: cs
cs: ## executes coding standards
		$(compose) run --rm code sh -lc './vendor/bin/ecs check src tests --fix'

.PHONY: cs-check
cs-check: ## executes coding standards in dry run mode
# Disabled until ECS upgrade
# 		$(compose) run --rm code sh -lc './vendor/bin/ecs check src tests'

.PHONY: layer
layer: ## Check issues with layers
		$(compose) run --rm code sh -lc 'bin/deptrac.phar analyze'

.PHONY: db
db: ## recreate database
		$(compose) exec -T php sh -lc './bin/console d:d:d --force --if-exists'
		$(compose) exec -T php sh -lc './bin/console d:d:c --if-not-exists'
		$(compose) exec -T php sh -lc './bin/console d:m:m -n'
.PHONY: dmd
dmd: ## Generate migrations diff file
		$(compose) exec -T php sh -lc './bin/console d:m:diff'


.PHONY: schema-validate
schema-validate: ## validate database schema
		$(compose) exec -T php sh -lc './bin/console d:s:v'

.PHONY: xon
xon: ## activate xdebug simlink
		$(compose) exec -T php sh -lc 'xon | true'

.PHONY: xoff
xoff: ## deactivate xdebug
		$(compose) exec -T php sh -lc 'xoff | true'
		make s='php workers_events workers_users' stop
		make up

.PHONY: sh
sh: ## gets inside a container, use 's' variable to select a service. make s=php sh
		$(compose) exec $(s) sh -l

.PHONY: logs
logs: ## look for 's' service logs, make s=php logs
		$(compose) logs -f $(s)

.PHONY: minikube
minikube:
		@eval $$(minikube docker-env); \
		docker compose -f etc/artifact/docker-compose.yml build --parallel; \
		helm dep up etc/artifact/chart; \
		helm upgrade -i cqrs etc/artifact/chart

.PHONY: htemplate
htemplate:
		helm template cqrs etc/artifact/chart

.PHONY: help
help: ## Display this help message
	@cat $(MAKEFILE_LIST) | grep -e "^[a-zA-Z_\-]*: *.*## *" | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
```

## File: `phpcs.xml.dist`
```
<?xml version="1.0" encoding="UTF-8"?>

<ruleset xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:noNamespaceSchemaLocation="vendor/squizlabs/php_codesniffer/phpcs.xsd">

    <arg name="basepath" value="."/>
    <arg name="cache" value=".phpcs-cache"/>
    <arg name="colors"/>
    <arg name="extensions" value="php"/>

    <rule ref="PSR12"/>

    <file>bin/</file>
    <file>config/</file>
    <file>public/</file>
    <file>src/</file>
    <file>tests/</file>

</ruleset>
```

## File: `phpstan.dist.neon`
```
parameters:
    level: 6
    paths:
        - src/
        - tests/
    excludePaths:
        - src/Infrastructure/Shared/Persistence/Doctrine/Migrations/*
        - src/App/Shared/Infrastructure/Persistence/Doctrine/Migrations/*
    reportUnmatchedIgnoredErrors: false
    ignoreErrors:
        - '#Method .+ should return .+ but returns Broadway\\Domain\\DomainEventStream#'
        - '#Parameter \#1 .+ of class Broadway\\Domain\\DomainMessage constructor expects .+, .+ given#'
        - '#Call to an undefined method Broadway\\EventSourcing\\EventSourcedAggregateRoot::.+\(\)#'
        - '#Property .+ has no type specified#'
        - '#Method .+ has no return type specified#'
        - '#Method .+ has parameter .+ with no type specified#'
        - '#no value type specified in iterable type array#'
        - '#generic class .+ does not specify its types#'
```

## File: `phpunit.xml.dist`
```
<?xml version="1.0" encoding="UTF-8"?>
<!-- https://phpunit.de/manual/current/en/appendixes.configuration.html -->
<phpunit xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:noNamespaceSchemaLocation="https://schema.phpunit.de/10.5/phpunit.xsd"
         colors="true"
         bootstrap="vendor/autoload.php"
         cacheDirectory=".phpunit.cache"
>
  <php>
    <ini name="error_reporting" value="-1"/>
    <env name="KERNEL_CLASS" value="App\Shared\Infrastructure\Kernel"/>
    <env name="APP_ENV" value="test"/>
    <env name="APP_DEBUG" value="1"/>
    <env name="APP_SECRET" value="s$cretf0rt3st"/>
    <env name="SHELL_VERBOSITY" value="-1"/>
    <env name="SYMFONY_DEPRECATIONS_HELPER" value="weak"/>
    <!-- ###+ lexik/jwt-authentication-bundle ### -->
    <env name="JWT_SECRET_KEY" value="%kernel.project_dir%/config/packages/jwt/private.pem"/>
    <env name="JWT_PUBLIC_KEY" value="%kernel.project_dir%/config/packages/jwt/public.pem"/>
    <env name="JWT_PASSPHRASE" value="development"/>
    <env name="JWT_TTL" value="604800"/>
    <!-- ###- lexik/jwt-authentication-bundle ### -->
    <!-- ###+ symfony/messenger ### -->
    <env name="MESSENGER_TRANSPORT_DSN" value="in-memory://" force="true"/>
    <!-- ###- symfony/messenger ### -->
    <!-- ###+ doctrine/doctrine-bundle ### -->
    <env name="DATABASE_HOST" value="mysql"/>
    <env name="DATABASE_PORT" value="3306"/>
    <env name="DATABASE_NAME" value="api"/>
    <env name="DATABASE_USER" value="root"/>
    <env name="DATABASE_PASSWORD" value="api"/>
    <!-- ###- doctrine/doctrine-bundle ### -->
    <!-- ###+ symfony/routing ### -->
    <env name="DEFAULT_URI" value="http://localhost"/>
    <!-- ###- symfony/routing ### -->
  </php>
  <testsuites>
    <testsuite name="Api Test Suite">
      <directory>tests/</directory>
    </testsuite>
  </testsuites>
  <source>
    <include>
      <directory>./src/</directory>
    </include>
    <exclude>
      <directory>./src/App/Shared/Infrastructure/Persistence/Doctrine/Migrations</directory>
      <file>./src/App/Shared/Infrastructure/Kernel.php</file>
    </exclude>
  </source>
  <extensions>
    <bootstrap class="DAMA\DoctrineTestBundle\PHPUnit\PHPUnitExtension"/>
  </extensions>
</phpunit>
```

## File: `psalm.xml`
```xml
<?xml version="1.0"?>
<psalm
        allowStringToStandInForClass="true"
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xmlns="https://getpsalm.org/schema/config"
        xsi:schemaLocation="https://getpsalm.org/schema/config vendor/vimeo/psalm/config.xsd"
>
    <projectFiles>
        <directory name="src" />
        <ignoreFiles>
            <file name="src/App/Shared/Infrastructure/Kernel.php"/>
            <directory name="tests" />
            <directory name="vendor" />
        </ignoreFiles>
    </projectFiles>

    <issueHandlers>
        <!-- level 3 issues - slightly lazy code writing, but provably low false-negatives -->

        <DeprecatedClass>
            <errorLevel type="info">
                <referencedClass name="Doctrine\Common\Persistence\ManagerRegistry" />
                <referencedClass name="Doctrine\Common\Persistence\Mapping\ClassMetadata" />
                <referencedClass name="Doctrine\Common\Persistence\ObjectManager" />
                <referencedClass name="Doctrine\Common\Persistence\ObjectRepository" />
                <referencedClass name="Symfony\Bundle\FrameworkBundle\Command\ContainerAwareCommand" />
                <referencedClass name="Symfony\Bundle\FrameworkBundle\Controller\Controller" />
                <referencedClass name="Symfony\Bundle\FrameworkBundle\Templating\EngineInterface" />
                <referencedClass name="Symfony\Component\Security\Core\Role\Role" />
            </errorLevel>
        </DeprecatedClass>
        <DeprecatedInterface>
            <errorLevel type="info">
                <referencedClass name="Doctrine\Common\Persistence\ObjectManager" />
                <referencedClass name="Doctrine\Common\Persistence\ObjectRepository" />
                <referencedClass name="Symfony\Component\Security\Core\User\AdvancedUserInterface" />
            </errorLevel>
        </DeprecatedInterface>
        <DeprecatedMethod>
            <errorLevel type="info">
                <referencedMethod name="Symfony\Component\EventDispatcher\Event::stopPropagation" />
                <referencedMethod name="Symfony\Component\HttpKernel\Kernel::getRootDir" />
                <referencedMethod name="Symfony\Component\HttpKernel\Event\GetResponseForExceptionEvent::getException" />
            </errorLevel>
        </DeprecatedMethod>

        <InternalMethod>
            <errorLevel type="info">
                <referencedMethod name="PHPUnit\Framework\TestCase::__construct" />
                <referencedMethod name="Symfony\Bundle\SecurityBundle\Security\_FirewallMap::getFirewallConfig" />
            </errorLevel>
        </InternalMethod>

        <MissingReturnType errorLevel="info" />

        <PropertyNotSetInConstructor errorLevel="info" />
        <MissingParamType errorLevel="info" />

        <!-- level 4 issues - points to possible deficiencies in logic, higher false-positives -->

        <MoreSpecificReturnType errorLevel="info" />
        <LessSpecificReturnStatement errorLevel="info" />
        <PossiblyInvalidArgument errorLevel="info" />
        <PossiblyInvalidArrayAccess errorLevel="info" />
        <PossiblyInvalidArrayAssignment errorLevel="info" />
        <PossiblyInvalidArrayOffset errorLevel="info" />
        <PossiblyInvalidCast errorLevel="info" />
        <PossiblyInvalidFunctionCall errorLevel="info" />
        <PossiblyInvalidIterator errorLevel="info" />
        <PossiblyInvalidMethodCall errorLevel="info" />
        <PossiblyInvalidOperand errorLevel="info" />
        <PossiblyInvalidPropertyAssignment errorLevel="info" />
        <PossiblyInvalidPropertyAssignmentValue errorLevel="info" />
        <PossiblyInvalidPropertyFetch errorLevel="info" />
        <PossiblyNullArgument errorLevel="info" />
        <PossiblyNullArrayAccess errorLevel="info" />
        <PossiblyNullArrayAssignment errorLevel="info" />
        <PossiblyNullArrayOffset errorLevel="info" />
        <PossiblyNullFunctionCall errorLevel="info" />
        <PossiblyNullIterator errorLevel="info" />
        <PossiblyNullOperand errorLevel="info" />
        <PossiblyNullPropertyAssignment errorLevel="info" />
        <PossiblyNullPropertyAssignmentValue errorLevel="info" />
        <PossiblyNullPropertyFetch errorLevel="info" />
        <PossiblyNullReference errorLevel="info" />
        <PossiblyUndefinedMethod>
            <errorLevel type="info">
                <referencedMethod name="Symfony\Component\Config\Definition\Builder\NodeDefinition::arrayNode" />
                <referencedMethod name="Symfony\Component\Config\Definition\Builder\NodeDefinition::booleanNode" />
                <referencedMethod name="Symfony\Component\Config\Definition\Builder\NodeDefinition::children" />
                <referencedMethod name="Symfony\Component\Config\Definition\Builder\NodeDefinition::integerNode" />
                <referencedMethod name="Symfony\Component\Config\Definition\Builder\NodeDefinition::scalarNode" />
                <referencedMethod name="Symfony\Component\Config\Definition\Builder\NodeDefinition::variableNode" />
                <referencedMethod name="Symfony\Component\Config\Definition\Builder\NodeParentInterface::end" />
            </errorLevel>
        </PossiblyUndefinedMethod>

        <!-- level 5 issues - should be avoided at mosts costs... -->

        <TooManyArguments>
            <errorLevel type="info">
                <referencedFunction name="Symfony\Contracts\EventDispatcher\EventDispatcherInterface::dispatch" />
                <referencedFunction name="Symfony\Component\HttpKernel\Config\FileLocator::__construct" />
                <referencedFunction name="Symfony\Contracts\EventDispatcher\EventDispatcherInterface::dispatch" />
            </errorLevel>
            <errorLevel type="suppress">
                <referencedFunction name="Doctrine\ORM\Query\Expr::andX" />
                <referencedFunction name="Doctrine\ORM\Query\Expr::orX" />
            </errorLevel>
        </TooManyArguments>

        <!-- level 6 issues - really bad things -->

        <InvalidNullableReturnType errorLevel="info" />
        <NullableReturnStatement errorLevel="info" />
        <InvalidFalsableReturnType errorLevel="info" />
        <FalsableReturnStatement errorLevel="info" />

        <MoreSpecificImplementedParamType errorLevel="info" />
        <LessSpecificImplementedReturnType errorLevel="info" />

        <!-- level 7 issues - even worse -->

        <InvalidArgument>
            <errorLevel type="info">
                <referencedFunction name="Symfony\Component\EventDispatcher\EventDispatcherInterface::dispatch" />
            </errorLevel>
        </InvalidArgument>

        <!-- level 8 issues - some fatal errors in PHP -->

        <MethodSignatureMismatch errorLevel="info" />

        <!-- Custom -->

        <!-- remove after guzzlehttp-release -->
        <!-- see https://github.com/guzzle/guzzle/pull/2273 -->
        <InvalidCatch errorLevel="info" />
    </issueHandlers>
</psalm>
```

## File: `symfony.lock`
```
{
    "broadway/broadway-bundle": {
        "version": "0.7",
        "recipe": {
            "repo": "github.com/symfony/recipes-contrib",
            "branch": "main",
            "version": "0.4",
            "ref": "0601c67ff07896a752e5a72381a22254ff754ea1"
        },
        "files": [
            "config/packages/broadway.yaml"
        ]
    },
    "broadway/event-store-dbal": {
        "version": "0.6",
        "recipe": {
            "repo": "github.com/symfony/recipes-contrib",
            "branch": "main",
            "version": "0.2",
            "ref": "a8e44b60058a2798f65be93037aa1562f4de60eb"
        },
        "files": [
            "config/packages/broadway_event_store_dbal.yaml"
        ]
    },
    "dama/doctrine-test-bundle": {
        "version": "8.4",
        "recipe": {
            "repo": "github.com/symfony/recipes-contrib",
            "branch": "main",
            "version": "8.3",
            "ref": "dfc51177476fb39d014ed89944cde53dc3326d23"
        },
        "files": [
            "config/packages/dama_doctrine_test_bundle.yaml"
        ]
    },
    "doctrine/deprecations": {
        "version": "1.1",
        "recipe": {
            "repo": "github.com/symfony/recipes",
            "branch": "main",
            "version": "1.0",
            "ref": "87424683adc81d7dc305eefec1fced883084aab9"
        }
    },
    "doctrine/doctrine-bundle": {
        "version": "2.18",
        "recipe": {
            "repo": "github.com/symfony/recipes",
            "branch": "main",
            "version": "2.13",
            "ref": "620b57f496f2e599a6015a9fa222c2ee0a32adcb"
        },
        "files": [
            "config/packages/doctrine.yaml",
            "src/Entity/.gitignore",
            "src/Repository/.gitignore"
        ]
    },
    "doctrine/doctrine-migrations-bundle": {
        "version": "3.7",
        "recipe": {
            "repo": "github.com/symfony/recipes",
            "branch": "main",
            "version": "3.1",
            "ref": "1d01ec03c6ecbd67c3375c5478c9a423ae5d6a33"
        },
        "files": [
            "config/packages/doctrine_migrations.yaml",
            "migrations/.gitignore"
        ]
    },
    "lexik/jwt-authentication-bundle": {
        "version": "3.2",
        "recipe": {
            "repo": "github.com/symfony/recipes",
            "branch": "main",
            "version": "2.5",
            "ref": "e9481b233a11ef7e15fe055a2b21fd3ac1aa2bb7"
        },
        "files": [
            "config/packages/lexik_jwt_authentication.yaml"
        ]
    },
    "nelmio/api-doc-bundle": {
        "version": "4.38",
        "recipe": {
            "repo": "github.com/symfony/recipes-contrib",
            "branch": "main",
            "version": "3.0",
            "ref": "c8e0c38e1a280ab9e37587a8fa32b251d5bc1c94"
        },
        "files": [
            "config/packages/nelmio_api_doc.yaml",
            "config/routes/nelmio_api_doc.yaml"
        ]
    },
    "phpstan/phpstan": {
        "version": "2.1",
        "recipe": {
            "repo": "github.com/symfony/recipes-contrib",
            "branch": "main",
            "version": "1.0",
            "ref": "5e490cc197fb6bb1ae22e5abbc531ddc633b6767"
        },
        "files": [
            "phpstan.dist.neon"
        ]
    },
    "phpunit/phpunit": {
        "version": "10.5",
        "recipe": {
            "repo": "github.com/symfony/recipes",
            "branch": "main",
            "version": "10.0",
            "ref": "bb22cf8d8c554a623b427d5f3416b538f5525233"
        },
        "files": [
            ".env.test",
            "phpunit.dist.xml",
            "tests/bootstrap.php"
        ]
    },
    "ramsey/uuid-doctrine": {
        "version": "2.1",
        "recipe": {
            "repo": "github.com/symfony/recipes-contrib",
            "branch": "main",
            "version": "1.3",
            "ref": "471aed0fbf5620b8d7f92b7a5ebbbf6c0945c27a"
        },
        "files": [
            "config/packages/ramsey_uuid_doctrine.yaml"
        ]
    },
    "squizlabs/php_codesniffer": {
        "version": "3.13",
        "recipe": {
            "repo": "github.com/symfony/recipes-contrib",
            "branch": "main",
            "version": "3.6",
            "ref": "1019e5c08d4821cb9b77f4891f8e9c31ff20ac6f"
        },
        "files": [
            "phpcs.xml.dist"
        ]
    },
    "symfony/console": {
        "version": "7.4",
        "recipe": {
            "repo": "github.com/symfony/recipes",
            "branch": "main",
            "version": "5.3",
            "ref": "1781ff40d8a17d87cf53f8d4cf0c8346ed2bb461"
        },
        "files": [
            "bin/console"
        ]
    },
    "symfony/flex": {
        "version": "2.10",
        "recipe": {
            "repo": "github.com/symfony/recipes",
            "branch": "main",
            "version": "2.4",
            "ref": "52e9754527a15e2b79d9a610f98185a1fe46622a"
        },
        "files": [
            ".env",
            ".env.dev"
        ]
    },
    "symfony/framework-bundle": {
        "version": "7.4",
        "recipe": {
            "repo": "github.com/symfony/recipes",
            "branch": "main",
            "version": "7.4",
            "ref": "09f6e081c763a206802674ce0cb34a022f0ffc6d"
        },
        "files": [
            "config/packages/cache.yaml",
            "config/packages/framework.yaml",
            "config/preload.php",
            "config/routes/framework.yaml",
            "config/services.yaml",
            "public/index.php",
            "src/Controller/.gitignore",
            "src/Kernel.php",
            ".editorconfig"
        ]
    },
    "symfony/messenger": {
        "version": "7.4",
        "recipe": {
            "repo": "github.com/symfony/recipes",
            "branch": "main",
            "version": "6.0",
            "ref": "d8936e2e2230637ef97e5eecc0eea074eecae58b"
        },
        "files": [
            "config/packages/messenger.yaml"
        ]
    },
    "symfony/monolog-bundle": {
        "version": "3.11",
        "recipe": {
            "repo": "github.com/symfony/recipes",
            "branch": "main",
            "version": "3.7",
            "ref": "1b9efb10c54cb51c713a9391c9300ff8bceda459"
        },
        "files": [
            "config/packages/monolog.yaml"
        ]
    },
    "symfony/phpunit-bridge": {
        "version": "7.4",
        "recipe": {
            "repo": "github.com/symfony/recipes",
            "branch": "main",
            "version": "7.3",
            "ref": "dc13fec96bd527bd399c3c01f0aab915c67fd544"
        }
    },
    "symfony/property-info": {
        "version": "7.4",
        "recipe": {
            "repo": "github.com/symfony/recipes",
            "branch": "main",
            "version": "7.3",
            "ref": "dae70df71978ae9226ae915ffd5fad817f5ca1f7"
        },
        "files": [
            "config/packages/property_info.yaml"
        ]
    },
    "symfony/routing": {
        "version": "7.4",
        "recipe": {
            "repo": "github.com/symfony/recipes",
            "branch": "main",
            "version": "7.4",
            "ref": "bc94c4fd86f393f3ab3947c18b830ea343e51ded"
        },
        "files": [
            "config/packages/routing.yaml",
            "config/routes.yaml"
        ]
    },
    "symfony/security-bundle": {
        "version": "7.4",
        "recipe": {
            "repo": "github.com/symfony/recipes",
            "branch": "main",
            "version": "7.4",
            "ref": "c42fee7802181cdd50f61b8622715829f5d2335c"
        },
        "files": [
            "config/packages/security.yaml",
            "config/routes/security.yaml"
        ]
    },
    "symfony/twig-bundle": {
        "version": "7.4",
        "recipe": {
            "repo": "github.com/symfony/recipes",
            "branch": "main",
            "version": "6.4",
            "ref": "cab5fd2a13a45c266d45a7d9337e28dee6272877"
        },
        "files": [
            "config/packages/twig.yaml",
            "templates/base.html.twig"
        ]
    },
    "symfony/web-profiler-bundle": {
        "version": "7.4",
        "recipe": {
            "repo": "github.com/symfony/recipes",
            "branch": "main",
            "version": "7.3",
            "ref": "a363460c1b0b4a4d0242f2ce1a843ca0f6ac9026"
        },
        "files": [
            "config/packages/web_profiler.yaml",
            "config/routes/web_profiler.yaml"
        ]
    }
}
```

## File: `config/bundles.php`
```php
<?php

return [
    Symfony\Bundle\FrameworkBundle\FrameworkBundle::class => ['all' => true],
    Broadway\Bundle\BroadwayBundle\BroadwayBundle::class => ['all' => true],
    Doctrine\Bundle\DoctrineBundle\DoctrineBundle::class => ['all' => true],
    Doctrine\Bundle\MigrationsBundle\DoctrineMigrationsBundle::class => ['all' => true],
    Symfony\Bundle\TwigBundle\TwigBundle::class => ['all' => true],
    Symfony\Bundle\WebProfilerBundle\WebProfilerBundle::class => ['dev' => true, 'test' => true],
    DAMA\DoctrineTestBundle\DAMADoctrineTestBundle::class => ['test' => true],
    Symfony\Bundle\SecurityBundle\SecurityBundle::class => ['all' => true],
    Lexik\Bundle\JWTAuthenticationBundle\LexikJWTAuthenticationBundle::class => ['all' => true],
    Nelmio\ApiDocBundle\NelmioApiDocBundle::class => ['all' => true],
    Symfony\Bundle\MonologBundle\MonologBundle::class => ['all' => true],
];
```

## File: `config/preload.php`
```php
<?php

if (file_exists(dirname(__DIR__).'/var/cache/prod/App_KernelProdContainer.preload.php')) {
    require dirname(__DIR__).'/var/cache/prod/App_KernelProdContainer.preload.php';
}
```

## File: `config/reference.php`
```php
<?php

// This file is auto-generated and is for apps only. Bundles SHOULD NOT rely on its content.

namespace Symfony\Component\DependencyInjection\Loader\Configurator;

use Symfony\Component\Config\Loader\ParamConfigurator as Param;

/**
 * This class provides array-shapes for configuring the services and bundles of an application.
 *
 * Services declared with the config() method below are autowired and autoconfigured by default.
 *
 * This is for apps only. Bundles SHOULD NOT use it.
 *
 * Example:
 *
 *     ```php
 *     // config/services.php
 *     namespace Symfony\Component\DependencyInjection\Loader\Configurator;
 *
 *     return App::config([
 *         'services' => [
 *             'App\\' => [
 *                 'resource' => '../src/',
 *             ],
 *         ],
 *     ]);
 *     ```
 *
 * @psalm-type ImportsConfig = list<string|array{
 *     resource: string,
 *     type?: string|null,
 *     ignore_errors?: bool,
 * }>
 * @psalm-type ParametersConfig = array<string, scalar|\UnitEnum|array<scalar|\UnitEnum|array<mixed>|Param|null>|Param|null>
 * @psalm-type ArgumentsType = list<mixed>|array<string, mixed>
 * @psalm-type CallType = array<string, ArgumentsType>|array{0:string, 1?:ArgumentsType, 2?:bool}|array{method:string, arguments?:ArgumentsType, returns_clone?:bool}
 * @psalm-type TagsType = list<string|array<string, array<string, mixed>>> // arrays inside the list must have only one element, with the tag name as the key
 * @psalm-type CallbackType = string|array{0:string|ReferenceConfigurator,1:string}|\Closure|ReferenceConfigurator
 * @psalm-type DeprecationType = array{package: string, version: string, message?: string}
 * @psalm-type DefaultsType = array{
 *     public?: bool,
 *     tags?: TagsType,
 *     resource_tags?: TagsType,
 *     autowire?: bool,
 *     autoconfigure?: bool,
 *     bind?: array<string, mixed>,
 * }
 * @psalm-type InstanceofType = array{
 *     shared?: bool,
 *     lazy?: bool|string,
 *     public?: bool,
 *     properties?: array<string, mixed>,
 *     configurator?: CallbackType,
 *     calls?: list<CallType>,
 *     tags?: TagsType,
 *     resource_tags?: TagsType,
 *     autowire?: bool,
 *     bind?: array<string, mixed>,
 *     constructor?: string,
 * }
 * @psalm-type DefinitionType = array{
 *     class?: string,
 *     file?: string,
 *     parent?: string,
 *     shared?: bool,
 *     synthetic?: bool,
 *     lazy?: bool|string,
 *     public?: bool,
 *     abstract?: bool,
 *     deprecated?: DeprecationType,
 *     factory?: CallbackType,
 *     configurator?: CallbackType,
 *     arguments?: ArgumentsType,
 *     properties?: array<string, mixed>,
 *     calls?: list<CallType>,
 *     tags?: TagsType,
 *     resource_tags?: TagsType,
 *     decorates?: string,
 *     decoration_inner_name?: string,
 *     decoration_priority?: int,
 *     decoration_on_invalid?: 'exception'|'ignore'|null,
 *     autowire?: bool,
 *     autoconfigure?: bool,
 *     bind?: array<string, mixed>,
 *     constructor?: string,
 *     from_callable?: CallbackType,
 * }
 * @psalm-type AliasType = string|array{
 *     alias: string,
 *     public?: bool,
 *     deprecated?: DeprecationType,
 * }
 * @psalm-type PrototypeType = array{
 *     resource: string,
 *     namespace?: string,
 *     exclude?: string|list<string>,
 *     parent?: string,
 *     shared?: bool,
 *     lazy?: bool|string,
 *     public?: bool,
 *     abstract?: bool,
 *     deprecated?: DeprecationType,
 *     factory?: CallbackType,
 *     arguments?: ArgumentsType,
 *     properties?: array<string, mixed>,
 *     configurator?: CallbackType,
 *     calls?: list<CallType>,
 *     tags?: TagsType,
 *     resource_tags?: TagsType,
 *     autowire?: bool,
 *     autoconfigure?: bool,
 *     bind?: array<string, mixed>,
 *     constructor?: string,
 * }
 * @psalm-type StackType = array{
 *     stack: list<DefinitionType|AliasType|PrototypeType|array<class-string, ArgumentsType|null>>,
 *     public?: bool,
 *     deprecated?: DeprecationType,
 * }
 * @psalm-type ServicesConfig = array{
 *     _defaults?: DefaultsType,
 *     _instanceof?: InstanceofType,
 *     ...<string, DefinitionType|AliasType|PrototypeType|StackType|ArgumentsType|null>
 * }
 * @psalm-type ExtensionType = array<string, mixed>
 * @psalm-type FrameworkConfig = array{
 *     secret?: scalar|Param|null,
 *     http_method_override?: bool|Param, // Set true to enable support for the '_method' request parameter to determine the intended HTTP method on POST requests. // Default: false
 *     allowed_http_method_override?: list<string|Param>|null,
 *     trust_x_sendfile_type_header?: scalar|Param|null, // Set true to enable support for xsendfile in binary file responses. // Default: "%env(bool:default::SYMFONY_TRUST_X_SENDFILE_TYPE_HEADER)%"
 *     ide?: scalar|Param|null, // Default: "%env(default::SYMFONY_IDE)%"
 *     test?: bool|Param,
 *     default_locale?: scalar|Param|null, // Default: "en"
 *     set_locale_from_accept_language?: bool|Param, // Whether to use the Accept-Language HTTP header to set the Request locale (only when the "_locale" request attribute is not passed). // Default: false
 *     set_content_language_from_locale?: bool|Param, // Whether to set the Content-Language HTTP header on the Response using the Request locale. // Default: false
 *     enabled_locales?: list<scalar|Param|null>,
 *     trusted_hosts?: list<scalar|Param|null>,
 *     trusted_proxies?: mixed, // Default: ["%env(default::SYMFONY_TRUSTED_PROXIES)%"]
 *     trusted_headers?: list<scalar|Param|null>,
 *     error_controller?: scalar|Param|null, // Default: "error_controller"
 *     handle_all_throwables?: bool|Param, // HttpKernel will handle all kinds of \Throwable. // Default: true
 *     csrf_protection?: bool|array{
 *         enabled?: scalar|Param|null, // Default: null
 *         stateless_token_ids?: list<scalar|Param|null>,
 *         check_header?: scalar|Param|null, // Whether to check the CSRF token in a header in addition to a cookie when using stateless protection. // Default: false
 *         cookie_name?: scalar|Param|null, // The name of the cookie to use when using stateless protection. // Default: "csrf-token"
 *     },
 *     form?: bool|array{ // Form configuration
 *         enabled?: bool|Param, // Default: false
 *         csrf_protection?: bool|array{
 *             enabled?: scalar|Param|null, // Default: null
 *             token_id?: scalar|Param|null, // Default: null
 *             field_name?: scalar|Param|null, // Default: "_token"
 *             field_attr?: array<string, scalar|Param|null>,
 *         },
 *     },
 *     http_cache?: bool|array{ // HTTP cache configuration
 *         enabled?: bool|Param, // Default: false
 *         debug?: bool|Param, // Default: "%kernel.debug%"
 *         trace_level?: "none"|"short"|"full"|Param,
 *         trace_header?: scalar|Param|null,
 *         default_ttl?: int|Param,
 *         private_headers?: list<scalar|Param|null>,
 *         skip_response_headers?: list<scalar|Param|null>,
 *         allow_reload?: bool|Param,
 *         allow_revalidate?: bool|Param,
 *         stale_while_revalidate?: int|Param,
 *         stale_if_error?: int|Param,
 *         terminate_on_cache_hit?: bool|Param,
 *     },
 *     esi?: bool|array{ // ESI configuration
 *         enabled?: bool|Param, // Default: false
 *     },
 *     ssi?: bool|array{ // SSI configuration
 *         enabled?: bool|Param, // Default: false
 *     },
 *     fragments?: bool|array{ // Fragments configuration
 *         enabled?: bool|Param, // Default: false
 *         hinclude_default_template?: scalar|Param|null, // Default: null
 *         path?: scalar|Param|null, // Default: "/_fragment"
 *     },
 *     profiler?: bool|array{ // Profiler configuration
 *         enabled?: bool|Param, // Default: false
 *         collect?: bool|Param, // Default: true
 *         collect_parameter?: scalar|Param|null, // The name of the parameter to use to enable or disable collection on a per request basis. // Default: null
 *         only_exceptions?: bool|Param, // Default: false
 *         only_main_requests?: bool|Param, // Default: false
 *         dsn?: scalar|Param|null, // Default: "file:%kernel.cache_dir%/profiler"
 *         collect_serializer_data?: bool|Param, // Enables the serializer data collector and profiler panel. // Default: false
 *     },
 *     workflows?: bool|array{
 *         enabled?: bool|Param, // Default: false
 *         workflows?: array<string, array{ // Default: []
 *             audit_trail?: bool|array{
 *                 enabled?: bool|Param, // Default: false
 *             },
 *             type?: "workflow"|"state_machine"|Param, // Default: "state_machine"
 *             marking_store?: array{
 *                 type?: "method"|Param,
 *                 property?: scalar|Param|null,
 *                 service?: scalar|Param|null,
 *             },
 *             supports?: list<scalar|Param|null>,
 *             definition_validators?: list<scalar|Param|null>,
 *             support_strategy?: scalar|Param|null,
 *             initial_marking?: list<scalar|Param|null>,
 *             events_to_dispatch?: list<string|Param>|null,
 *             places?: list<array{ // Default: []
 *                 name: scalar|Param|null,
 *                 metadata?: list<mixed>,
 *             }>,
 *             transitions: list<array{ // Default: []
 *                 name: string|Param,
 *                 guard?: string|Param, // An expression to block the transition.
 *                 from?: list<array{ // Default: []
 *                     place: string|Param,
 *                     weight?: int|Param, // Default: 1
 *                 }>,
 *                 to?: list<array{ // Default: []
 *                     place: string|Param,
 *                     weight?: int|Param, // Default: 1
 *                 }>,
 *                 weight?: int|Param, // Default: 1
 *                 metadata?: list<mixed>,
 *             }>,
 *             metadata?: list<mixed>,
 *         }>,
 *     },
 *     router?: bool|array{ // Router configuration
 *         enabled?: bool|Param, // Default: false
 *         resource: scalar|Param|null,
 *         type?: scalar|Param|null,
 *         cache_dir?: scalar|Param|null, // Deprecated: Setting the "framework.router.cache_dir.cache_dir" configuration option is deprecated. It will be removed in version 8.0. // Default: "%kernel.build_dir%"
 *         default_uri?: scalar|Param|null, // The default URI used to generate URLs in a non-HTTP context. // Default: null
 *         http_port?: scalar|Param|null, // Default: 80
 *         https_port?: scalar|Param|null, // Default: 443
 *         strict_requirements?: scalar|Param|null, // set to true to throw an exception when a parameter does not match the requirements set to false to disable exceptions when a parameter does not match the requirements (and return null instead) set to null to disable parameter checks against requirements 'true' is the preferred configuration in development mode, while 'false' or 'null' might be preferred in production // Default: true
 *         utf8?: bool|Param, // Default: true
 *     },
 *     session?: bool|array{ // Session configuration
 *         enabled?: bool|Param, // Default: false
 *         storage_factory_id?: scalar|Param|null, // Default: "session.storage.factory.native"
 *         handler_id?: scalar|Param|null, // Defaults to using the native session handler, or to the native *file* session handler if "save_path" is not null.
 *         name?: scalar|Param|null,
 *         cookie_lifetime?: scalar|Param|null,
 *         cookie_path?: scalar|Param|null,
 *         cookie_domain?: scalar|Param|null,
 *         cookie_secure?: true|false|"auto"|Param, // Default: "auto"
 *         cookie_httponly?: bool|Param, // Default: true
 *         cookie_samesite?: null|"lax"|"strict"|"none"|Param, // Default: "lax"
 *         use_cookies?: bool|Param,
 *         gc_divisor?: scalar|Param|null,
 *         gc_probability?: scalar|Param|null,
 *         gc_maxlifetime?: scalar|Param|null,
 *         save_path?: scalar|Param|null, // Defaults to "%kernel.cache_dir%/sessions" if the "handler_id" option is not null.
 *         metadata_update_threshold?: int|Param, // Seconds to wait between 2 session metadata updates. // Default: 0
 *         sid_length?: int|Param, // Deprecated: Setting the "framework.session.sid_length.sid_length" configuration option is deprecated. It will be removed in version 8.0. No alternative is provided as PHP 8.4 has deprecated the related option.
 *         sid_bits_per_character?: int|Param, // Deprecated: Setting the "framework.session.sid_bits_per_character.sid_bits_per_character" configuration option is deprecated. It will be removed in version 8.0. No alternative is provided as PHP 8.4 has deprecated the related option.
 *     },
 *     request?: bool|array{ // Request configuration
 *         enabled?: bool|Param, // Default: false
 *         formats?: array<string, string|list<scalar|Param|null>>,
 *     },
 *     assets?: bool|array{ // Assets configuration
 *         enabled?: bool|Param, // Default: true
 *         strict_mode?: bool|Param, // Throw an exception if an entry is missing from the manifest.json. // Default: false
 *         version_strategy?: scalar|Param|null, // Default: null
 *         version?: scalar|Param|null, // Default: null
 *         version_format?: scalar|Param|null, // Default: "%%s?%%s"
 *         json_manifest_path?: scalar|Param|null, // Default: null
 *         base_path?: scalar|Param|null, // Default: ""
 *         base_urls?: list<scalar|Param|null>,
 *         packages?: array<string, array{ // Default: []
 *             strict_mode?: bool|Param, // Throw an exception if an entry is missing from the manifest.json. // Default: false
 *             version_strategy?: scalar|Param|null, // Default: null
 *             version?: scalar|Param|null,
 *             version_format?: scalar|Param|null, // Default: null
 *             json_manifest_path?: scalar|Param|null, // Default: null
 *             base_path?: scalar|Param|null, // Default: ""
 *             base_urls?: list<scalar|Param|null>,
 *         }>,
 *     },
 *     asset_mapper?: bool|array{ // Asset Mapper configuration
 *         enabled?: bool|Param, // Default: false
 *         paths?: array<string, scalar|Param|null>,
 *         excluded_patterns?: list<scalar|Param|null>,
 *         exclude_dotfiles?: bool|Param, // If true, any files starting with "." will be excluded from the asset mapper. // Default: true
 *         server?: bool|Param, // If true, a "dev server" will return the assets from the public directory (true in "debug" mode only by default). // Default: true
 *         public_prefix?: scalar|Param|null, // The public path where the assets will be written to (and served from when "server" is true). // Default: "/assets/"
 *         missing_import_mode?: "strict"|"warn"|"ignore"|Param, // Behavior if an asset cannot be found when imported from JavaScript or CSS files - e.g. "import './non-existent.js'". "strict" means an exception is thrown, "warn" means a warning is logged, "ignore" means the import is left as-is. // Default: "warn"
 *         extensions?: array<string, scalar|Param|null>,
 *         importmap_path?: scalar|Param|null, // The path of the importmap.php file. // Default: "%kernel.project_dir%/importmap.php"
 *         importmap_polyfill?: scalar|Param|null, // The importmap name that will be used to load the polyfill. Set to false to disable. // Default: "es-module-shims"
 *         importmap_script_attributes?: array<string, scalar|Param|null>,
 *         vendor_dir?: scalar|Param|null, // The directory to store JavaScript vendors. // Default: "%kernel.project_dir%/assets/vendor"
 *         precompress?: bool|array{ // Precompress assets with Brotli, Zstandard and gzip.
 *             enabled?: bool|Param, // Default: false
 *             formats?: list<scalar|Param|null>,
 *             extensions?: list<scalar|Param|null>,
 *         },
 *     },
 *     translator?: bool|array{ // Translator configuration
 *         enabled?: bool|Param, // Default: false
 *         fallbacks?: list<scalar|Param|null>,
 *         logging?: bool|Param, // Default: false
 *         formatter?: scalar|Param|null, // Default: "translator.formatter.default"
 *         cache_dir?: scalar|Param|null, // Default: "%kernel.cache_dir%/translations"
 *         default_path?: scalar|Param|null, // The default path used to load translations. // Default: "%kernel.project_dir%/translations"
 *         paths?: list<scalar|Param|null>,
 *         pseudo_localization?: bool|array{
 *             enabled?: bool|Param, // Default: false
 *             accents?: bool|Param, // Default: true
 *             expansion_factor?: float|Param, // Default: 1.0
 *             brackets?: bool|Param, // Default: true
 *             parse_html?: bool|Param, // Default: false
 *             localizable_html_attributes?: list<scalar|Param|null>,
 *         },
 *         providers?: array<string, array{ // Default: []
 *             dsn?: scalar|Param|null,
 *             domains?: list<scalar|Param|null>,
 *             locales?: list<scalar|Param|null>,
 *         }>,
 *         globals?: array<string, string|array{ // Default: []
 *             value?: mixed,
 *             message?: string|Param,
 *             parameters?: array<string, scalar|Param|null>,
 *             domain?: string|Param,
 *         }>,
 *     },
 *     validation?: bool|array{ // Validation configuration
 *         enabled?: bool|Param, // Default: false
 *         cache?: scalar|Param|null, // Deprecated: Setting the "framework.validation.cache.cache" configuration option is deprecated. It will be removed in version 8.0.
 *         enable_attributes?: bool|Param, // Default: true
 *         static_method?: list<scalar|Param|null>,
 *         translation_domain?: scalar|Param|null, // Default: "validators"
 *         email_validation_mode?: "html5"|"html5-allow-no-tld"|"strict"|"loose"|Param, // Default: "html5"
 *         mapping?: array{
 *             paths?: list<scalar|Param|null>,
 *         },
 *         not_compromised_password?: bool|array{
 *             enabled?: bool|Param, // When disabled, compromised passwords will be accepted as valid. // Default: true
 *             endpoint?: scalar|Param|null, // API endpoint for the NotCompromisedPassword Validator. // Default: null
 *         },
 *         disable_translation?: bool|Param, // Default: false
 *         auto_mapping?: array<string, array{ // Default: []
 *             services?: list<scalar|Param|null>,
 *         }>,
 *     },
 *     annotations?: bool|array{
 *         enabled?: bool|Param, // Default: false
 *     },
 *     serializer?: bool|array{ // Serializer configuration
 *         enabled?: bool|Param, // Default: false
 *         enable_attributes?: bool|Param, // Default: true
 *         name_converter?: scalar|Param|null,
 *         circular_reference_handler?: scalar|Param|null,
 *         max_depth_handler?: scalar|Param|null,
 *         mapping?: array{
 *             paths?: list<scalar|Param|null>,
 *         },
 *         default_context?: list<mixed>,
 *         named_serializers?: array<string, array{ // Default: []
 *             name_converter?: scalar|Param|null,
 *             default_context?: list<mixed>,
 *             include_built_in_normalizers?: bool|Param, // Whether to include the built-in normalizers // Default: true
 *             include_built_in_encoders?: bool|Param, // Whether to include the built-in encoders // Default: true
 *         }>,
 *     },
 *     property_access?: bool|array{ // Property access configuration
 *         enabled?: bool|Param, // Default: true
 *         magic_call?: bool|Param, // Default: false
 *         magic_get?: bool|Param, // Default: true
 *         magic_set?: bool|Param, // Default: true
 *         throw_exception_on_invalid_index?: bool|Param, // Default: false
 *         throw_exception_on_invalid_property_path?: bool|Param, // Default: true
 *     },
 *     type_info?: bool|array{ // Type info configuration
 *         enabled?: bool|Param, // Default: true
 *         aliases?: array<string, scalar|Param|null>,
 *     },
 *     property_info?: bool|array{ // Property info configuration
 *         enabled?: bool|Param, // Default: true
 *         with_constructor_extractor?: bool|Param, // Registers the constructor extractor.
 *     },
 *     cache?: array{ // Cache configuration
 *         prefix_seed?: scalar|Param|null, // Used to namespace cache keys when using several apps with the same shared backend. // Default: "_%kernel.project_dir%.%kernel.container_class%"
 *         app?: scalar|Param|null, // App related cache pools configuration. // Default: "cache.adapter.filesystem"
 *         system?: scalar|Param|null, // System related cache pools configuration. // Default: "cache.adapter.system"
 *         directory?: scalar|Param|null, // Default: "%kernel.share_dir%/pools/app"
 *         default_psr6_provider?: scalar|Param|null,
 *         default_redis_provider?: scalar|Param|null, // Default: "redis://localhost"
 *         default_valkey_provider?: scalar|Param|null, // Default: "valkey://localhost"
 *         default_memcached_provider?: scalar|Param|null, // Default: "memcached://localhost"
 *         default_doctrine_dbal_provider?: scalar|Param|null, // Default: "database_connection"
 *         default_pdo_provider?: scalar|Param|null, // Default: null
 *         pools?: array<string, array{ // Default: []
 *             adapters?: list<scalar|Param|null>,
 *             tags?: scalar|Param|null, // Default: null
 *             public?: bool|Param, // Default: false
 *             default_lifetime?: scalar|Param|null, // Default lifetime of the pool.
 *             provider?: scalar|Param|null, // Overwrite the setting from the default provider for this adapter.
 *             early_expiration_message_bus?: scalar|Param|null,
 *             clearer?: scalar|Param|null,
 *         }>,
 *     },
 *     php_errors?: array{ // PHP errors handling configuration
 *         log?: mixed, // Use the application logger instead of the PHP logger for logging PHP errors. // Default: true
 *         throw?: bool|Param, // Throw PHP errors as \ErrorException instances. // Default: true
 *     },
 *     exceptions?: array<string, array{ // Default: []
 *         log_level?: scalar|Param|null, // The level of log message. Null to let Symfony decide. // Default: null
 *         status_code?: scalar|Param|null, // The status code of the response. Null or 0 to let Symfony decide. // Default: null
 *         log_channel?: scalar|Param|null, // The channel of log message. Null to let Symfony decide. // Default: null
 *     }>,
 *     web_link?: bool|array{ // Web links configuration
 *         enabled?: bool|Param, // Default: false
 *     },
 *     lock?: bool|string|array{ // Lock configuration
 *         enabled?: bool|Param, // Default: false
 *         resources?: array<string, string|list<scalar|Param|null>>,
 *     },
 *     semaphore?: bool|string|array{ // Semaphore configuration
 *         enabled?: bool|Param, // Default: false
 *         resources?: array<string, scalar|Param|null>,
 *     },
 *     messenger?: bool|array{ // Messenger configuration
 *         enabled?: bool|Param, // Default: true
 *         routing?: array<string, array{ // Default: []
 *             senders?: list<scalar|Param|null>,
 *         }>,
 *         serializer?: array{
 *             default_serializer?: scalar|Param|null, // Service id to use as the default serializer for the transports. // Default: "messenger.transport.native_php_serializer"
 *             symfony_serializer?: array{
 *                 format?: scalar|Param|null, // Serialization format for the messenger.transport.symfony_serializer service (which is not the serializer used by default). // Default: "json"
 *                 context?: array<string, mixed>,
 *             },
 *         },
 *         transports?: array<string, string|array{ // Default: []
 *             dsn?: scalar|Param|null,
 *             serializer?: scalar|Param|null, // Service id of a custom serializer to use. // Default: null
 *             options?: list<mixed>,
 *             failure_transport?: scalar|Param|null, // Transport name to send failed messages to (after all retries have failed). // Default: null
 *             retry_strategy?: string|array{
 *                 service?: scalar|Param|null, // Service id to override the retry strategy entirely. // Default: null
 *                 max_retries?: int|Param, // Default: 3
 *                 delay?: int|Param, // Time in ms to delay (or the initial value when multiplier is used). // Default: 1000
 *                 multiplier?: float|Param, // If greater than 1, delay will grow exponentially for each retry: this delay = (delay * (multiple ^ retries)). // Default: 2
 *                 max_delay?: int|Param, // Max time in ms that a retry should ever be delayed (0 = infinite). // Default: 0
 *                 jitter?: float|Param, // Randomness to apply to the delay (between 0 and 1). // Default: 0.1
 *             },
 *             rate_limiter?: scalar|Param|null, // Rate limiter name to use when processing messages. // Default: null
 *         }>,
 *         failure_transport?: scalar|Param|null, // Transport name to send failed messages to (after all retries have failed). // Default: null
 *         stop_worker_on_signals?: list<scalar|Param|null>,
 *         default_bus?: scalar|Param|null, // Default: null
 *         buses?: array<string, array{ // Default: {"messenger.bus.default":{"default_middleware":{"enabled":true,"allow_no_handlers":false,"allow_no_senders":true},"middleware":[]}}
 *             default_middleware?: bool|string|array{
 *                 enabled?: bool|Param, // Default: true
 *                 allow_no_handlers?: bool|Param, // Default: false
 *                 allow_no_senders?: bool|Param, // Default: true
 *             },
 *             middleware?: list<string|array{ // Default: []
 *                 id: scalar|Param|null,
 *                 arguments?: list<mixed>,
 *             }>,
 *         }>,
 *     },
 *     scheduler?: bool|array{ // Scheduler configuration
 *         enabled?: bool|Param, // Default: false
 *     },
 *     disallow_search_engine_index?: bool|Param, // Enabled by default when debug is enabled. // Default: true
 *     http_client?: bool|array{ // HTTP Client configuration
 *         enabled?: bool|Param, // Default: false
 *         max_host_connections?: int|Param, // The maximum number of connections to a single host.
 *         default_options?: array{
 *             headers?: array<string, mixed>,
 *             vars?: array<string, mixed>,
 *             max_redirects?: int|Param, // The maximum number of redirects to follow.
 *             http_version?: scalar|Param|null, // The default HTTP version, typically 1.1 or 2.0, leave to null for the best version.
 *             resolve?: array<string, scalar|Param|null>,
 *             proxy?: scalar|Param|null, // The URL of the proxy to pass requests through or null for automatic detection.
 *             no_proxy?: scalar|Param|null, // A comma separated list of hosts that do not require a proxy to be reached.
 *             timeout?: float|Param, // The idle timeout, defaults to the "default_socket_timeout" ini parameter.
 *             max_duration?: float|Param, // The maximum execution time for the request+response as a whole.
 *             bindto?: scalar|Param|null, // A network interface name, IP address, a host name or a UNIX socket to bind to.
 *             verify_peer?: bool|Param, // Indicates if the peer should be verified in a TLS context.
 *             verify_host?: bool|Param, // Indicates if the host should exist as a certificate common name.
 *             cafile?: scalar|Param|null, // A certificate authority file.
 *             capath?: scalar|Param|null, // A directory that contains multiple certificate authority files.
 *             local_cert?: scalar|Param|null, // A PEM formatted certificate file.
 *             local_pk?: scalar|Param|null, // A private key file.
 *             passphrase?: scalar|Param|null, // The passphrase used to encrypt the "local_pk" file.
 *             ciphers?: scalar|Param|null, // A list of TLS ciphers separated by colons, commas or spaces (e.g. "RC3-SHA:TLS13-AES-128-GCM-SHA256"...)
 *             peer_fingerprint?: array{ // Associative array: hashing algorithm => hash(es).
 *                 sha1?: mixed,
 *                 pin-sha256?: mixed,
 *                 md5?: mixed,
 *             },
 *             crypto_method?: scalar|Param|null, // The minimum version of TLS to accept; must be one of STREAM_CRYPTO_METHOD_TLSv*_CLIENT constants.
 *             extra?: array<string, mixed>,
 *             rate_limiter?: scalar|Param|null, // Rate limiter name to use for throttling requests. // Default: null
 *             caching?: bool|array{ // Caching configuration.
 *                 enabled?: bool|Param, // Default: false
 *                 cache_pool?: string|Param, // The taggable cache pool to use for storing the responses. // Default: "cache.http_client"
 *                 shared?: bool|Param, // Indicates whether the cache is shared (public) or private. // Default: true
 *                 max_ttl?: int|Param, // The maximum TTL (in seconds) allowed for cached responses. Null means no cap. // Default: null
 *             },
 *             retry_failed?: bool|array{
 *                 enabled?: bool|Param, // Default: false
 *                 retry_strategy?: scalar|Param|null, // service id to override the retry strategy. // Default: null
 *                 http_codes?: array<string, array{ // Default: []
 *                     code?: int|Param,
 *                     methods?: list<string|Param>,
 *                 }>,
 *                 max_retries?: int|Param, // Default: 3
 *                 delay?: int|Param, // Time in ms to delay (or the initial value when multiplier is used). // Default: 1000
 *                 multiplier?: float|Param, // If greater than 1, delay will grow exponentially for each retry: delay * (multiple ^ retries). // Default: 2
 *                 max_delay?: int|Param, // Max time in ms that a retry should ever be delayed (0 = infinite). // Default: 0
 *                 jitter?: float|Param, // Randomness in percent (between 0 and 1) to apply to the delay. // Default: 0.1
 *             },
 *         },
 *         mock_response_factory?: scalar|Param|null, // The id of the service that should generate mock responses. It should be either an invokable or an iterable.
 *         scoped_clients?: array<string, string|array{ // Default: []
 *             scope?: scalar|Param|null, // The regular expression that the request URL must match before adding the other options. When none is provided, the base URI is used instead.
 *             base_uri?: scalar|Param|null, // The URI to resolve relative URLs, following rules in RFC 3985, section 2.
 *             auth_basic?: scalar|Param|null, // An HTTP Basic authentication "username:password".
 *             auth_bearer?: scalar|Param|null, // A token enabling HTTP Bearer authorization.
 *             auth_ntlm?: scalar|Param|null, // A "username:password" pair to use Microsoft NTLM authentication (requires the cURL extension).
 *             query?: array<string, scalar|Param|null>,
 *             headers?: array<string, mixed>,
 *             max_redirects?: int|Param, // The maximum number of redirects to follow.
 *             http_version?: scalar|Param|null, // The default HTTP version, typically 1.1 or 2.0, leave to null for the best version.
 *             resolve?: array<string, scalar|Param|null>,
 *             proxy?: scalar|Param|null, // The URL of the proxy to pass requests through or null for automatic detection.
 *             no_proxy?: scalar|Param|null, // A comma separated list of hosts that do not require a proxy to be reached.
 *             timeout?: float|Param, // The idle timeout, defaults to the "default_socket_timeout" ini parameter.
 *             max_duration?: float|Param, // The maximum execution time for the request+response as a whole.
 *             bindto?: scalar|Param|null, // A network interface name, IP address, a host name or a UNIX socket to bind to.
 *             verify_peer?: bool|Param, // Indicates if the peer should be verified in a TLS context.
 *             verify_host?: bool|Param, // Indicates if the host should exist as a certificate common name.
 *             cafile?: scalar|Param|null, // A certificate authority file.
 *             capath?: scalar|Param|null, // A directory that contains multiple certificate authority files.
 *             local_cert?: scalar|Param|null, // A PEM formatted certificate file.
 *             local_pk?: scalar|Param|null, // A private key file.
 *             passphrase?: scalar|Param|null, // The passphrase used to encrypt the "local_pk" file.
 *             ciphers?: scalar|Param|null, // A list of TLS ciphers separated by colons, commas or spaces (e.g. "RC3-SHA:TLS13-AES-128-GCM-SHA256"...).
 *             peer_fingerprint?: array{ // Associative array: hashing algorithm => hash(es).
 *                 sha1?: mixed,
 *                 pin-sha256?: mixed,
 *                 md5?: mixed,
 *             },
 *             crypto_method?: scalar|Param|null, // The minimum version of TLS to accept; must be one of STREAM_CRYPTO_METHOD_TLSv*_CLIENT constants.
 *             extra?: array<string, mixed>,
 *             rate_limiter?: scalar|Param|null, // Rate limiter name to use for throttling requests. // Default: null
 *             caching?: bool|array{ // Caching configuration.
 *                 enabled?: bool|Param, // Default: false
 *                 cache_pool?: string|Param, // The taggable cache pool to use for storing the responses. // Default: "cache.http_client"
 *                 shared?: bool|Param, // Indicates whether the cache is shared (public) or private. // Default: true
 *                 max_ttl?: int|Param, // The maximum TTL (in seconds) allowed for cached responses. Null means no cap. // Default: null
 *             },
 *             retry_failed?: bool|array{
 *                 enabled?: bool|Param, // Default: false
 *                 retry_strategy?: scalar|Param|null, // service id to override the retry strategy. // Default: null
 *                 http_codes?: array<string, array{ // Default: []
 *                     code?: int|Param,
 *                     methods?: list<string|Param>,
 *                 }>,
 *                 max_retries?: int|Param, // Default: 3
 *                 delay?: int|Param, // Time in ms to delay (or the initial value when multiplier is used). // Default: 1000
 *                 multiplier?: float|Param, // If greater than 1, delay will grow exponentially for each retry: delay * (multiple ^ retries). // Default: 2
 *                 max_delay?: int|Param, // Max time in ms that a retry should ever be delayed (0 = infinite). // Default: 0
 *                 jitter?: float|Param, // Randomness in percent (between 0 and 1) to apply to the delay. // Default: 0.1
 *             },
 *         }>,
 *     },
 *     mailer?: bool|array{ // Mailer configuration
 *         enabled?: bool|Param, // Default: false
 *         message_bus?: scalar|Param|null, // The message bus to use. Defaults to the default bus if the Messenger component is installed. // Default: null
 *         dsn?: scalar|Param|null, // Default: null
 *         transports?: array<string, scalar|Param|null>,
 *         envelope?: array{ // Mailer Envelope configuration
 *             sender?: scalar|Param|null,
 *             recipients?: list<scalar|Param|null>,
 *             allowed_recipients?: list<scalar|Param|null>,
 *         },
 *         headers?: array<string, string|array{ // Default: []
 *             value?: mixed,
 *         }>,
 *         dkim_signer?: bool|array{ // DKIM signer configuration
 *             enabled?: bool|Param, // Default: false
 *             key?: scalar|Param|null, // Key content, or path to key (in PEM format with the `file://` prefix) // Default: ""
 *             domain?: scalar|Param|null, // Default: ""
 *             select?: scalar|Param|null, // Default: ""
 *             passphrase?: scalar|Param|null, // The private key passphrase // Default: ""
 *             options?: array<string, mixed>,
 *         },
 *         smime_signer?: bool|array{ // S/MIME signer configuration
 *             enabled?: bool|Param, // Default: false
 *             key?: scalar|Param|null, // Path to key (in PEM format) // Default: ""
 *             certificate?: scalar|Param|null, // Path to certificate (in PEM format without the `file://` prefix) // Default: ""
 *             passphrase?: scalar|Param|null, // The private key passphrase // Default: null
 *             extra_certificates?: scalar|Param|null, // Default: null
 *             sign_options?: int|Param, // Default: null
 *         },
 *         smime_encrypter?: bool|array{ // S/MIME encrypter configuration
 *             enabled?: bool|Param, // Default: false
 *             repository?: scalar|Param|null, // S/MIME certificate repository service. This service shall implement the `Symfony\Component\Mailer\EventListener\SmimeCertificateRepositoryInterface`. // Default: ""
 *             cipher?: int|Param, // A set of algorithms used to encrypt the message // Default: null
 *         },
 *     },
 *     secrets?: bool|array{
 *         enabled?: bool|Param, // Default: true
 *         vault_directory?: scalar|Param|null, // Default: "%kernel.project_dir%/config/secrets/%kernel.runtime_environment%"
 *         local_dotenv_file?: scalar|Param|null, // Default: "%kernel.project_dir%/.env.%kernel.environment%.local"
 *         decryption_env_var?: scalar|Param|null, // Default: "base64:default::SYMFONY_DECRYPTION_SECRET"
 *     },
 *     notifier?: bool|array{ // Notifier configuration
 *         enabled?: bool|Param, // Default: false
 *         message_bus?: scalar|Param|null, // The message bus to use. Defaults to the default bus if the Messenger component is installed. // Default: null
 *         chatter_transports?: array<string, scalar|Param|null>,
 *         texter_transports?: array<string, scalar|Param|null>,
 *         notification_on_failed_messages?: bool|Param, // Default: false
 *         channel_policy?: array<string, string|list<scalar|Param|null>>,
 *         admin_recipients?: list<array{ // Default: []
 *             email?: scalar|Param|null,
 *             phone?: scalar|Param|null, // Default: ""
 *         }>,
 *     },
 *     rate_limiter?: bool|array{ // Rate limiter configuration
 *         enabled?: bool|Param, // Default: false
 *         limiters?: array<string, array{ // Default: []
 *             lock_factory?: scalar|Param|null, // The service ID of the lock factory used by this limiter (or null to disable locking). // Default: "auto"
 *             cache_pool?: scalar|Param|null, // The cache pool to use for storing the current limiter state. // Default: "cache.rate_limiter"
 *             storage_service?: scalar|Param|null, // The service ID of a custom storage implementation, this precedes any configured "cache_pool". // Default: null
 *             policy: "fixed_window"|"token_bucket"|"sliding_window"|"compound"|"no_limit"|Param, // The algorithm to be used by this limiter.
 *             limiters?: list<scalar|Param|null>,
 *             limit?: int|Param, // The maximum allowed hits in a fixed interval or burst.
 *             interval?: scalar|Param|null, // Configures the fixed interval if "policy" is set to "fixed_window" or "sliding_window". The value must be a number followed by "second", "minute", "hour", "day", "week" or "month" (or their plural equivalent).
 *             rate?: array{ // Configures the fill rate if "policy" is set to "token_bucket".
 *                 interval?: scalar|Param|null, // Configures the rate interval. The value must be a number followed by "second", "minute", "hour", "day", "week" or "month" (or their plural equivalent).
 *                 amount?: int|Param, // Amount of tokens to add each interval. // Default: 1
 *             },
 *         }>,
 *     },
 *     uid?: bool|array{ // Uid configuration
 *         enabled?: bool|Param, // Default: false
 *         default_uuid_version?: 7|6|4|1|Param, // Default: 7
 *         name_based_uuid_version?: 5|3|Param, // Default: 5
 *         name_based_uuid_namespace?: scalar|Param|null,
 *         time_based_uuid_version?: 7|6|1|Param, // Default: 7
 *         time_based_uuid_node?: scalar|Param|null,
 *     },
 *     html_sanitizer?: bool|array{ // HtmlSanitizer configuration
 *         enabled?: bool|Param, // Default: false
 *         sanitizers?: array<string, array{ // Default: []
 *             allow_safe_elements?: bool|Param, // Allows "safe" elements and attributes. // Default: false
 *             allow_static_elements?: bool|Param, // Allows all static elements and attributes from the W3C Sanitizer API standard. // Default: false
 *             allow_elements?: array<string, mixed>,
 *             block_elements?: list<string|Param>,
 *             drop_elements?: list<string|Param>,
 *             allow_attributes?: array<string, mixed>,
 *             drop_attributes?: array<string, mixed>,
 *             force_attributes?: array<string, array<string, string|Param>>,
 *             force_https_urls?: bool|Param, // Transforms URLs using the HTTP scheme to use the HTTPS scheme instead. // Default: false
 *             allowed_link_schemes?: list<string|Param>,
 *             allowed_link_hosts?: list<string|Param>|null,
 *             allow_relative_links?: bool|Param, // Allows relative URLs to be used in links href attributes. // Default: false
 *             allowed_media_schemes?: list<string|Param>,
 *             allowed_media_hosts?: list<string|Param>|null,
 *             allow_relative_medias?: bool|Param, // Allows relative URLs to be used in media source attributes (img, audio, video, ...). // Default: false
 *             with_attribute_sanitizers?: list<string|Param>,
 *             without_attribute_sanitizers?: list<string|Param>,
 *             max_input_length?: int|Param, // The maximum length allowed for the sanitized input. // Default: 0
 *         }>,
 *     },
 *     webhook?: bool|array{ // Webhook configuration
 *         enabled?: bool|Param, // Default: false
 *         message_bus?: scalar|Param|null, // The message bus to use. // Default: "messenger.default_bus"
 *         routing?: array<string, array{ // Default: []
 *             service: scalar|Param|null,
 *             secret?: scalar|Param|null, // Default: ""
 *         }>,
 *     },
 *     remote-event?: bool|array{ // RemoteEvent configuration
 *         enabled?: bool|Param, // Default: false
 *     },
 *     json_streamer?: bool|array{ // JSON streamer configuration
 *         enabled?: bool|Param, // Default: false
 *     },
 * }
 * @psalm-type BroadwayConfig = array{
 *     command_handling?: array{
 *         dispatch_events?: bool|Param, // Default: false
 *         logger?: scalar|Param|null, // Default: false
 *     },
 *     event_store?: scalar|Param|null, // a service definition id implementing Broadway\EventStore\EventStore
 *     saga?: bool|array{
 *         enabled?: bool|Param, // Default: false
 *         state_repository?: scalar|Param|null, // a service definition id implementing Broadway\Saga\State\RepositoryInterface
 *     },
 *     serializer?: array{
 *         payload?: scalar|Param|null, // Default: "broadway.simple_interface_serializer"
 *         readmodel?: scalar|Param|null, // Default: "broadway.simple_interface_serializer"
 *         metadata?: scalar|Param|null, // Default: "broadway.simple_interface_serializer"
 *     },
 *     read_model?: scalar|Param|null, // a service definition id implementing Broadway\ReadModel\RepositoryFactory
 * }
 * @psalm-type DoctrineConfig = array{
 *     dbal?: array{
 *         default_connection?: scalar|Param|null,
 *         types?: array<string, string|array{ // Default: []
 *             class: scalar|Param|null,
 *             commented?: bool|Param, // Deprecated: The doctrine-bundle type commenting features were removed; the corresponding config parameter was deprecated in 2.0 and will be dropped in 3.0.
 *         }>,
 *         driver_schemes?: array<string, scalar|Param|null>,
 *         connections?: array<string, array{ // Default: []
 *             url?: scalar|Param|null, // A URL with connection information; any parameter value parsed from this string will override explicitly set parameters
 *             dbname?: scalar|Param|null,
 *             host?: scalar|Param|null, // Defaults to "localhost" at runtime.
 *             port?: scalar|Param|null, // Defaults to null at runtime.
 *             user?: scalar|Param|null, // Defaults to "root" at runtime.
 *             password?: scalar|Param|null, // Defaults to null at runtime.
 *             override_url?: bool|Param, // Deprecated: The "doctrine.dbal.override_url" configuration key is deprecated.
 *             dbname_suffix?: scalar|Param|null, // Adds the given suffix to the configured database name, this option has no effects for the SQLite platform
 *             application_name?: scalar|Param|null,
 *             charset?: scalar|Param|null,
 *             path?: scalar|Param|null,
 *             memory?: bool|Param,
 *             unix_socket?: scalar|Param|null, // The unix socket to use for MySQL
 *             persistent?: bool|Param, // True to use as persistent connection for the ibm_db2 driver
 *             protocol?: scalar|Param|null, // The protocol to use for the ibm_db2 driver (default to TCPIP if omitted)
 *             service?: bool|Param, // True to use SERVICE_NAME as connection parameter instead of SID for Oracle
 *             servicename?: scalar|Param|null, // Overrules dbname parameter if given and used as SERVICE_NAME or SID connection parameter for Oracle depending on the service parameter.
 *             sessionMode?: scalar|Param|null, // The session mode to use for the oci8 driver
 *             server?: scalar|Param|null, // The name of a running database server to connect to for SQL Anywhere.
 *             default_dbname?: scalar|Param|null, // Override the default database (postgres) to connect to for PostgreSQL connexion.
 *             sslmode?: scalar|Param|null, // Determines whether or with what priority a SSL TCP/IP connection will be negotiated with the server for PostgreSQL.
 *             sslrootcert?: scalar|Param|null, // The name of a file containing SSL certificate authority (CA) certificate(s). If the file exists, the server's certificate will be verified to be signed by one of these authorities.
 *             sslcert?: scalar|Param|null, // The path to the SSL client certificate file for PostgreSQL.
 *             sslkey?: scalar|Param|null, // The path to the SSL client key file for PostgreSQL.
 *             sslcrl?: scalar|Param|null, // The file name of the SSL certificate revocation list for PostgreSQL.
 *             pooled?: bool|Param, // True to use a pooled server with the oci8/pdo_oracle driver
 *             MultipleActiveResultSets?: bool|Param, // Configuring MultipleActiveResultSets for the pdo_sqlsrv driver
 *             use_savepoints?: bool|Param, // Use savepoints for nested transactions
 *             instancename?: scalar|Param|null, // Optional parameter, complete whether to add the INSTANCE_NAME parameter in the connection. It is generally used to connect to an Oracle RAC server to select the name of a particular instance.
 *             connectstring?: scalar|Param|null, // Complete Easy Connect connection descriptor, see https://docs.oracle.com/database/121/NETAG/naming.htm.When using this option, you will still need to provide the user and password parameters, but the other parameters will no longer be used. Note that when using this parameter, the getHost and getPort methods from Doctrine\DBAL\Connection will no longer function as expected.
 *             driver?: scalar|Param|null, // Default: "pdo_mysql"
 *             platform_service?: scalar|Param|null, // Deprecated: The "platform_service" configuration key is deprecated since doctrine-bundle 2.9. DBAL 4 will not support setting a custom platform via connection params anymore.
 *             auto_commit?: bool|Param,
 *             schema_filter?: scalar|Param|null,
 *             logging?: bool|Param, // Default: true
 *             profiling?: bool|Param, // Default: true
 *             profiling_collect_backtrace?: bool|Param, // Enables collecting backtraces when profiling is enabled // Default: false
 *             profiling_collect_schema_errors?: bool|Param, // Enables collecting schema errors when profiling is enabled // Default: true
 *             disable_type_comments?: bool|Param,
 *             server_version?: scalar|Param|null,
 *             idle_connection_ttl?: int|Param, // Default: 600
 *             driver_class?: scalar|Param|null,
 *             wrapper_class?: scalar|Param|null,
 *             keep_slave?: bool|Param, // Deprecated: The "keep_slave" configuration key is deprecated since doctrine-bundle 2.2. Use the "keep_replica" configuration key instead.
 *             keep_replica?: bool|Param,
 *             options?: array<string, mixed>,
 *             mapping_types?: array<string, scalar|Param|null>,
 *             default_table_options?: array<string, scalar|Param|null>,
 *             schema_manager_factory?: scalar|Param|null, // Default: "doctrine.dbal.legacy_schema_manager_factory"
 *             result_cache?: scalar|Param|null,
 *             slaves?: array<string, array{ // Default: []
 *                 url?: scalar|Param|null, // A URL with connection information; any parameter value parsed from this string will override explicitly set parameters
 *                 dbname?: scalar|Param|null,
 *                 host?: scalar|Param|null, // Defaults to "localhost" at runtime.
 *                 port?: scalar|Param|null, // Defaults to null at runtime.
 *                 user?: scalar|Param|null, // Defaults to "root" at runtime.
 *                 password?: scalar|Param|null, // Defaults to null at runtime.
 *                 override_url?: bool|Param, // Deprecated: The "doctrine.dbal.override_url" configuration key is deprecated.
 *                 dbname_suffix?: scalar|Param|null, // Adds the given suffix to the configured database name, this option has no effects for the SQLite platform
 *                 application_name?: scalar|Param|null,
 *                 charset?: scalar|Param|null,
 *                 path?: scalar|Param|null,
 *                 memory?: bool|Param,
 *                 unix_socket?: scalar|Param|null, // The unix socket to use for MySQL
 *                 persistent?: bool|Param, // True to use as persistent connection for the ibm_db2 driver
 *                 protocol?: scalar|Param|null, // The protocol to use for the ibm_db2 driver (default to TCPIP if omitted)
 *                 service?: bool|Param, // True to use SERVICE_NAME as connection parameter instead of SID for Oracle
 *                 servicename?: scalar|Param|null, // Overrules dbname parameter if given and used as SERVICE_NAME or SID connection parameter for Oracle depending on the service parameter.
 *                 sessionMode?: scalar|Param|null, // The session mode to use for the oci8 driver
 *                 server?: scalar|Param|null, // The name of a running database server to connect to for SQL Anywhere.
 *                 default_dbname?: scalar|Param|null, // Override the default database (postgres) to connect to for PostgreSQL connexion.
 *                 sslmode?: scalar|Param|null, // Determines whether or with what priority a SSL TCP/IP connection will be negotiated with the server for PostgreSQL.
 *                 sslrootcert?: scalar|Param|null, // The name of a file containing SSL certificate authority (CA) certificate(s). If the file exists, the server's certificate will be verified to be signed by one of these authorities.
 *                 sslcert?: scalar|Param|null, // The path to the SSL client certificate file for PostgreSQL.
 *                 sslkey?: scalar|Param|null, // The path to the SSL client key file for PostgreSQL.
 *                 sslcrl?: scalar|Param|null, // The file name of the SSL certificate revocation list for PostgreSQL.
 *                 pooled?: bool|Param, // True to use a pooled server with the oci8/pdo_oracle driver
 *                 MultipleActiveResultSets?: bool|Param, // Configuring MultipleActiveResultSets for the pdo_sqlsrv driver
 *                 use_savepoints?: bool|Param, // Use savepoints for nested transactions
 *                 instancename?: scalar|Param|null, // Optional parameter, complete whether to add the INSTANCE_NAME parameter in the connection. It is generally used to connect to an Oracle RAC server to select the name of a particular instance.
 *                 connectstring?: scalar|Param|null, // Complete Easy Connect connection descriptor, see https://docs.oracle.com/database/121/NETAG/naming.htm.When using this option, you will still need to provide the user and password parameters, but the other parameters will no longer be used. Note that when using this parameter, the getHost and getPort methods from Doctrine\DBAL\Connection will no longer function as expected.
 *             }>,
 *             replicas?: array<string, array{ // Default: []
 *                 url?: scalar|Param|null, // A URL with connection information; any parameter value parsed from this string will override explicitly set parameters
 *                 dbname?: scalar|Param|null,
 *                 host?: scalar|Param|null, // Defaults to "localhost" at runtime.
 *                 port?: scalar|Param|null, // Defaults to null at runtime.
 *                 user?: scalar|Param|null, // Defaults to "root" at runtime.
 *                 password?: scalar|Param|null, // Defaults to null at runtime.
 *                 override_url?: bool|Param, // Deprecated: The "doctrine.dbal.override_url" configuration key is deprecated.
 *                 dbname_suffix?: scalar|Param|null, // Adds the given suffix to the configured database name, this option has no effects for the SQLite platform
 *                 application_name?: scalar|Param|null,
 *                 charset?: scalar|Param|null,
 *                 path?: scalar|Param|null,
 *                 memory?: bool|Param,
 *                 unix_socket?: scalar|Param|null, // The unix socket to use for MySQL
 *                 persistent?: bool|Param, // True to use as persistent connection for the ibm_db2 driver
 *                 protocol?: scalar|Param|null, // The protocol to use for the ibm_db2 driver (default to TCPIP if omitted)
 *                 service?: bool|Param, // True to use SERVICE_NAME as connection parameter instead of SID for Oracle
 *                 servicename?: scalar|Param|null, // Overrules dbname parameter if given and used as SERVICE_NAME or SID connection parameter for Oracle depending on the service parameter.
 *                 sessionMode?: scalar|Param|null, // The session mode to use for the oci8 driver
 *                 server?: scalar|Param|null, // The name of a running database server to connect to for SQL Anywhere.
 *                 default_dbname?: scalar|Param|null, // Override the default database (postgres) to connect to for PostgreSQL connexion.
 *                 sslmode?: scalar|Param|null, // Determines whether or with what priority a SSL TCP/IP connection will be negotiated with the server for PostgreSQL.
 *                 sslrootcert?: scalar|Param|null, // The name of a file containing SSL certificate authority (CA) certificate(s). If the file exists, the server's certificate will be verified to be signed by one of these authorities.
 *                 sslcert?: scalar|Param|null, // The path to the SSL client certificate file for PostgreSQL.
 *                 sslkey?: scalar|Param|null, // The path to the SSL client key file for PostgreSQL.
 *                 sslcrl?: scalar|Param|null, // The file name of the SSL certificate revocation list for PostgreSQL.
 *                 pooled?: bool|Param, // True to use a pooled server with the oci8/pdo_oracle driver
 *                 MultipleActiveResultSets?: bool|Param, // Configuring MultipleActiveResultSets for the pdo_sqlsrv driver
 *                 use_savepoints?: bool|Param, // Use savepoints for nested transactions
 *                 instancename?: scalar|Param|null, // Optional parameter, complete whether to add the INSTANCE_NAME parameter in the connection. It is generally used to connect to an Oracle RAC server to select the name of a particular instance.
 *                 connectstring?: scalar|Param|null, // Complete Easy Connect connection descriptor, see https://docs.oracle.com/database/121/NETAG/naming.htm.When using this option, you will still need to provide the user and password parameters, but the other parameters will no longer be used. Note that when using this parameter, the getHost and getPort methods from Doctrine\DBAL\Connection will no longer function as expected.
 *             }>,
 *         }>,
 *     },
 *     orm?: array{
 *         default_entity_manager?: scalar|Param|null,
 *         auto_generate_proxy_classes?: scalar|Param|null, // Auto generate mode possible values are: "NEVER", "ALWAYS", "FILE_NOT_EXISTS", "EVAL", "FILE_NOT_EXISTS_OR_CHANGED", this option is ignored when the "enable_native_lazy_objects" option is true // Default: false
 *         enable_lazy_ghost_objects?: bool|Param, // Enables the new implementation of proxies based on lazy ghosts instead of using the legacy implementation // Default: true
 *         enable_native_lazy_objects?: bool|Param, // Enables the new native implementation of PHP lazy objects instead of generated proxies // Default: false
 *         proxy_dir?: scalar|Param|null, // Configures the path where generated proxy classes are saved when using non-native lazy objects, this option is ignored when the "enable_native_lazy_objects" option is true // Default: "%kernel.build_dir%/doctrine/orm/Proxies"
 *         proxy_namespace?: scalar|Param|null, // Defines the root namespace for generated proxy classes when using non-native lazy objects, this option is ignored when the "enable_native_lazy_objects" option is true // Default: "Proxies"
 *         controller_resolver?: bool|array{
 *             enabled?: bool|Param, // Default: true
 *             auto_mapping?: bool|Param|null, // Set to false to disable using route placeholders as lookup criteria when the primary key doesn't match the argument name // Default: null
 *             evict_cache?: bool|Param, // Set to true to fetch the entity from the database instead of using the cache, if any // Default: false
 *         },
 *         entity_managers?: array<string, array{ // Default: []
 *             query_cache_driver?: string|array{
 *                 type?: scalar|Param|null, // Default: null
 *                 id?: scalar|Param|null,
 *                 pool?: scalar|Param|null,
 *             },
 *             metadata_cache_driver?: string|array{
 *                 type?: scalar|Param|null, // Default: null
 *                 id?: scalar|Param|null,
 *                 pool?: scalar|Param|null,
 *             },
 *             result_cache_driver?: string|array{
 *                 type?: scalar|Param|null, // Default: null
 *                 id?: scalar|Param|null,
 *                 pool?: scalar|Param|null,
 *             },
 *             entity_listeners?: array{
 *                 entities?: array<string, array{ // Default: []
 *                     listeners?: array<string, array{ // Default: []
 *                         events?: list<array{ // Default: []
 *                             type?: scalar|Param|null,
 *                             method?: scalar|Param|null, // Default: null
 *                         }>,
 *                     }>,
 *                 }>,
 *             },
 *             connection?: scalar|Param|null,
 *             class_metadata_factory_name?: scalar|Param|null, // Default: "Doctrine\\ORM\\Mapping\\ClassMetadataFactory"
 *             default_repository_class?: scalar|Param|null, // Default: "Doctrine\\ORM\\EntityRepository"
 *             auto_mapping?: scalar|Param|null, // Default: false
 *             naming_strategy?: scalar|Param|null, // Default: "doctrine.orm.naming_strategy.default"
 *             quote_strategy?: scalar|Param|null, // Default: "doctrine.orm.quote_strategy.default"
 *             typed_field_mapper?: scalar|Param|null, // Default: "doctrine.orm.typed_field_mapper.default"
 *             entity_listener_resolver?: scalar|Param|null, // Default: null
 *             fetch_mode_subselect_batch_size?: scalar|Param|null,
 *             repository_factory?: scalar|Param|null, // Default: "doctrine.orm.container_repository_factory"
 *             schema_ignore_classes?: list<scalar|Param|null>,
 *             report_fields_where_declared?: bool|Param, // Set to "true" to opt-in to the new mapping driver mode that was added in Doctrine ORM 2.16 and will be mandatory in ORM 3.0. See https://github.com/doctrine/orm/pull/10455. // Default: true
 *             validate_xml_mapping?: bool|Param, // Set to "true" to opt-in to the new mapping driver mode that was added in Doctrine ORM 2.14. See https://github.com/doctrine/orm/pull/6728. // Default: false
 *             second_level_cache?: array{
 *                 region_cache_driver?: string|array{
 *                     type?: scalar|Param|null, // Default: null
 *                     id?: scalar|Param|null,
 *                     pool?: scalar|Param|null,
 *                 },
 *                 region_lock_lifetime?: scalar|Param|null, // Default: 60
 *                 log_enabled?: bool|Param, // Default: true
 *                 region_lifetime?: scalar|Param|null, // Default: 3600
 *                 enabled?: bool|Param, // Default: true
 *                 factory?: scalar|Param|null,
 *                 regions?: array<string, array{ // Default: []
 *                     cache_driver?: string|array{
 *                         type?: scalar|Param|null, // Default: null
 *                         id?: scalar|Param|null,
 *                         pool?: scalar|Param|null,
 *                     },
 *                     lock_path?: scalar|Param|null, // Default: "%kernel.cache_dir%/doctrine/orm/slc/filelock"
 *                     lock_lifetime?: scalar|Param|null, // Default: 60
 *                     type?: scalar|Param|null, // Default: "default"
 *                     lifetime?: scalar|Param|null, // Default: 0
 *                     service?: scalar|Param|null,
 *                     name?: scalar|Param|null,
 *                 }>,
 *                 loggers?: array<string, array{ // Default: []
 *                     name?: scalar|Param|null,
 *                     service?: scalar|Param|null,
 *                 }>,
 *             },
 *             hydrators?: array<string, scalar|Param|null>,
 *             mappings?: array<string, bool|string|array{ // Default: []
 *                 mapping?: scalar|Param|null, // Default: true
 *                 type?: scalar|Param|null,
 *                 dir?: scalar|Param|null,
 *                 alias?: scalar|Param|null,
 *                 prefix?: scalar|Param|null,
 *                 is_bundle?: bool|Param,
 *             }>,
 *             dql?: array{
 *                 string_functions?: array<string, scalar|Param|null>,
 *                 numeric_functions?: array<string, scalar|Param|null>,
 *                 datetime_functions?: array<string, scalar|Param|null>,
 *             },
 *             filters?: array<string, string|array{ // Default: []
 *                 class: scalar|Param|null,
 *                 enabled?: bool|Param, // Default: false
 *                 parameters?: array<string, mixed>,
 *             }>,
 *             identity_generation_preferences?: array<string, scalar|Param|null>,
 *         }>,
 *         resolve_target_entities?: array<string, scalar|Param|null>,
 *     },
 * }
 * @psalm-type DoctrineMigrationsConfig = array{
 *     enable_service_migrations?: bool|Param, // Whether to enable fetching migrations from the service container. // Default: false
 *     migrations_paths?: array<string, scalar|Param|null>,
 *     services?: array<string, scalar|Param|null>,
 *     factories?: array<string, scalar|Param|null>,
 *     storage?: array{ // Storage to use for migration status metadata.
 *         table_storage?: array{ // The default metadata storage, implemented as a table in the database.
 *             table_name?: scalar|Param|null, // Default: null
 *             version_column_name?: scalar|Param|null, // Default: null
 *             version_column_length?: scalar|Param|null, // Default: null
 *             executed_at_column_name?: scalar|Param|null, // Default: null
 *             execution_time_column_name?: scalar|Param|null, // Default: null
 *         },
 *     },
 *     migrations?: list<scalar|Param|null>,
 *     connection?: scalar|Param|null, // Connection name to use for the migrations database. // Default: null
 *     em?: scalar|Param|null, // Entity manager name to use for the migrations database (available when doctrine/orm is installed). // Default: null
 *     all_or_nothing?: scalar|Param|null, // Run all migrations in a transaction. // Default: false
 *     check_database_platform?: scalar|Param|null, // Adds an extra check in the generated migrations to allow execution only on the same platform as they were initially generated on. // Default: true
 *     custom_template?: scalar|Param|null, // Custom template path for generated migration classes. // Default: null
 *     organize_migrations?: scalar|Param|null, // Organize migrations mode. Possible values are: "BY_YEAR", "BY_YEAR_AND_MONTH", false // Default: false
 *     enable_profiler?: bool|Param, // Whether or not to enable the profiler collector to calculate and visualize migration status. This adds some queries overhead. // Default: false
 *     transactional?: bool|Param, // Whether or not to wrap migrations in a single transaction. // Default: true
 * }
 * @psalm-type TwigConfig = array{
 *     form_themes?: list<scalar|Param|null>,
 *     globals?: array<string, array{ // Default: []
 *         id?: scalar|Param|null,
 *         type?: scalar|Param|null,
 *         value?: mixed,
 *     }>,
 *     autoescape_service?: scalar|Param|null, // Default: null
 *     autoescape_service_method?: scalar|Param|null, // Default: null
 *     base_template_class?: scalar|Param|null, // Deprecated: The child node "base_template_class" at path "twig.base_template_class" is deprecated.
 *     cache?: scalar|Param|null, // Default: true
 *     charset?: scalar|Param|null, // Default: "%kernel.charset%"
 *     debug?: bool|Param, // Default: "%kernel.debug%"
 *     strict_variables?: bool|Param, // Default: "%kernel.debug%"
 *     auto_reload?: scalar|Param|null,
 *     optimizations?: int|Param,
 *     default_path?: scalar|Param|null, // The default path used to load templates. // Default: "%kernel.project_dir%/templates"
 *     file_name_pattern?: list<scalar|Param|null>,
 *     paths?: array<string, mixed>,
 *     date?: array{ // The default format options used by the date filter.
 *         format?: scalar|Param|null, // Default: "F j, Y H:i"
 *         interval_format?: scalar|Param|null, // Default: "%d days"
 *         timezone?: scalar|Param|null, // The timezone used when formatting dates, when set to null, the timezone returned by date_default_timezone_get() is used. // Default: null
 *     },
 *     number_format?: array{ // The default format options for the number_format filter.
 *         decimals?: int|Param, // Default: 0
 *         decimal_point?: scalar|Param|null, // Default: "."
 *         thousands_separator?: scalar|Param|null, // Default: ","
 *     },
 *     mailer?: array{
 *         html_to_text_converter?: scalar|Param|null, // A service implementing the "Symfony\Component\Mime\HtmlToTextConverter\HtmlToTextConverterInterface". // Default: null
 *     },
 * }
 * @psalm-type WebProfilerConfig = array{
 *     toolbar?: bool|array{ // Profiler toolbar configuration
 *         enabled?: bool|Param, // Default: false
 *         ajax_replace?: bool|Param, // Replace toolbar on AJAX requests // Default: false
 *     },
 *     intercept_redirects?: bool|Param, // Default: false
 *     excluded_ajax_paths?: scalar|Param|null, // Default: "^/((index|app(_[\\w]+)?)\\.php/)?_wdt"
 * }
 * @psalm-type DamaDoctrineTestConfig = array{
 *     enable_static_connection?: mixed, // Default: true
 *     enable_static_meta_data_cache?: bool|Param, // Default: true
 *     enable_static_query_cache?: bool|Param, // Default: true
 *     connection_keys?: list<mixed>,
 * }
 * @psalm-type SecurityConfig = array{
 *     access_denied_url?: scalar|Param|null, // Default: null
 *     session_fixation_strategy?: "none"|"migrate"|"invalidate"|Param, // Default: "migrate"
 *     hide_user_not_found?: bool|Param, // Deprecated: The "hide_user_not_found" option is deprecated and will be removed in 8.0. Use the "expose_security_errors" option instead.
 *     expose_security_errors?: \Symfony\Component\Security\Http\Authentication\ExposeSecurityLevel::None|\Symfony\Component\Security\Http\Authentication\ExposeSecurityLevel::AccountStatus|\Symfony\Component\Security\Http\Authentication\ExposeSecurityLevel::All|Param, // Default: "none"
 *     erase_credentials?: bool|Param, // Default: true
 *     access_decision_manager?: array{
 *         strategy?: "affirmative"|"consensus"|"unanimous"|"priority"|Param,
 *         service?: scalar|Param|null,
 *         strategy_service?: scalar|Param|null,
 *         allow_if_all_abstain?: bool|Param, // Default: false
 *         allow_if_equal_granted_denied?: bool|Param, // Default: true
 *     },
 *     password_hashers?: array<string, string|array{ // Default: []
 *         algorithm?: scalar|Param|null,
 *         migrate_from?: list<scalar|Param|null>,
 *         hash_algorithm?: scalar|Param|null, // Name of hashing algorithm for PBKDF2 (i.e. sha256, sha512, etc..) See hash_algos() for a list of supported algorithms. // Default: "sha512"
 *         key_length?: scalar|Param|null, // Default: 40
 *         ignore_case?: bool|Param, // Default: false
 *         encode_as_base64?: bool|Param, // Default: true
 *         iterations?: scalar|Param|null, // Default: 5000
 *         cost?: int|Param, // Default: null
 *         memory_cost?: scalar|Param|null, // Default: null
 *         time_cost?: scalar|Param|null, // Default: null
 *         id?: scalar|Param|null,
 *     }>,
 *     providers?: array<string, array{ // Default: []
 *         id?: scalar|Param|null,
 *         chain?: array{
 *             providers?: list<scalar|Param|null>,
 *         },
 *         entity?: array{
 *             class: scalar|Param|null, // The full entity class name of your user class.
 *             property?: scalar|Param|null, // Default: null
 *             manager_name?: scalar|Param|null, // Default: null
 *         },
 *         memory?: array{
 *             users?: array<string, array{ // Default: []
 *                 password?: scalar|Param|null, // Default: null
 *                 roles?: list<scalar|Param|null>,
 *             }>,
 *         },
 *         ldap?: array{
 *             service: scalar|Param|null,
 *             base_dn: scalar|Param|null,
 *             search_dn?: scalar|Param|null, // Default: null
 *             search_password?: scalar|Param|null, // Default: null
 *             extra_fields?: list<scalar|Param|null>,
 *             default_roles?: list<scalar|Param|null>,
 *             role_fetcher?: scalar|Param|null, // Default: null
 *             uid_key?: scalar|Param|null, // Default: "sAMAccountName"
 *             filter?: scalar|Param|null, // Default: "({uid_key}={user_identifier})"
 *             password_attribute?: scalar|Param|null, // Default: null
 *         },
 *         lexik_jwt?: array{
 *             class?: scalar|Param|null, // Default: "Lexik\\Bundle\\JWTAuthenticationBundle\\Security\\User\\JWTUser"
 *         },
 *     }>,
 *     firewalls: array<string, array{ // Default: []
 *         pattern?: scalar|Param|null,
 *         host?: scalar|Param|null,
 *         methods?: list<scalar|Param|null>,
 *         security?: bool|Param, // Default: true
 *         user_checker?: scalar|Param|null, // The UserChecker to use when authenticating users in this firewall. // Default: "security.user_checker"
 *         request_matcher?: scalar|Param|null,
 *         access_denied_url?: scalar|Param|null,
 *         access_denied_handler?: scalar|Param|null,
 *         entry_point?: scalar|Param|null, // An enabled authenticator name or a service id that implements "Symfony\Component\Security\Http\EntryPoint\AuthenticationEntryPointInterface".
 *         provider?: scalar|Param|null,
 *         stateless?: bool|Param, // Default: false
 *         lazy?: bool|Param, // Default: false
 *         context?: scalar|Param|null,
 *         logout?: array{
 *             enable_csrf?: bool|Param|null, // Default: null
 *             csrf_token_id?: scalar|Param|null, // Default: "logout"
 *             csrf_parameter?: scalar|Param|null, // Default: "_csrf_token"
 *             csrf_token_manager?: scalar|Param|null,
 *             path?: scalar|Param|null, // Default: "/logout"
 *             target?: scalar|Param|null, // Default: "/"
 *             invalidate_session?: bool|Param, // Default: true
 *             clear_site_data?: list<"*"|"cache"|"cookies"|"storage"|"executionContexts"|Param>,
 *             delete_cookies?: array<string, array{ // Default: []
 *                 path?: scalar|Param|null, // Default: null
 *                 domain?: scalar|Param|null, // Default: null
 *                 secure?: scalar|Param|null, // Default: false
 *                 samesite?: scalar|Param|null, // Default: null
 *                 partitioned?: scalar|Param|null, // Default: false
 *             }>,
 *         },
 *         switch_user?: array{
 *             provider?: scalar|Param|null,
 *             parameter?: scalar|Param|null, // Default: "_switch_user"
 *             role?: scalar|Param|null, // Default: "ROLE_ALLOWED_TO_SWITCH"
 *             target_route?: scalar|Param|null, // Default: null
 *         },
 *         required_badges?: list<scalar|Param|null>,
 *         custom_authenticators?: list<scalar|Param|null>,
 *         login_throttling?: array{
 *             limiter?: scalar|Param|null, // A service id implementing "Symfony\Component\HttpFoundation\RateLimiter\RequestRateLimiterInterface".
 *             max_attempts?: int|Param, // Default: 5
 *             interval?: scalar|Param|null, // Default: "1 minute"
 *             lock_factory?: scalar|Param|null, // The service ID of the lock factory used by the login rate limiter (or null to disable locking). // Default: null
 *             cache_pool?: string|Param, // The cache pool to use for storing the limiter state // Default: "cache.rate_limiter"
 *             storage_service?: string|Param, // The service ID of a custom storage implementation, this precedes any configured "cache_pool" // Default: null
 *         },
 *         x509?: array{
 *             provider?: scalar|Param|null,
 *             user?: scalar|Param|null, // Default: "SSL_CLIENT_S_DN_Email"
 *             credentials?: scalar|Param|null, // Default: "SSL_CLIENT_S_DN"
 *             user_identifier?: scalar|Param|null, // Default: "emailAddress"
 *         },
 *         remote_user?: array{
 *             provider?: scalar|Param|null,
 *             user?: scalar|Param|null, // Default: "REMOTE_USER"
 *         },
 *         jwt?: array{
 *             provider?: scalar|Param|null, // Default: null
 *             authenticator?: scalar|Param|null, // Default: "lexik_jwt_authentication.security.jwt_authenticator"
 *         },
 *         login_link?: array{
 *             check_route: scalar|Param|null, // Route that will validate the login link - e.g. "app_login_link_verify".
 *             check_post_only?: scalar|Param|null, // If true, only HTTP POST requests to "check_route" will be handled by the authenticator. // Default: false
 *             signature_properties: list<scalar|Param|null>,
 *             lifetime?: int|Param, // The lifetime of the login link in seconds. // Default: 600
 *             max_uses?: int|Param, // Max number of times a login link can be used - null means unlimited within lifetime. // Default: null
 *             used_link_cache?: scalar|Param|null, // Cache service id used to expired links of max_uses is set.
 *             success_handler?: scalar|Param|null, // A service id that implements Symfony\Component\Security\Http\Authentication\AuthenticationSuccessHandlerInterface.
 *             failure_handler?: scalar|Param|null, // A service id that implements Symfony\Component\Security\Http\Authentication\AuthenticationFailureHandlerInterface.
 *             provider?: scalar|Param|null, // The user provider to load users from.
 *             secret?: scalar|Param|null, // Default: "%kernel.secret%"
 *             always_use_default_target_path?: bool|Param, // Default: false
 *             default_target_path?: scalar|Param|null, // Default: "/"
 *             login_path?: scalar|Param|null, // Default: "/login"
 *             target_path_parameter?: scalar|Param|null, // Default: "_target_path"
 *             use_referer?: bool|Param, // Default: false
 *             failure_path?: scalar|Param|null, // Default: null
 *             failure_forward?: bool|Param, // Default: false
 *             failure_path_parameter?: scalar|Param|null, // Default: "_failure_path"
 *         },
 *         form_login?: array{
 *             provider?: scalar|Param|null,
 *             remember_me?: bool|Param, // Default: true
 *             success_handler?: scalar|Param|null,
 *             failure_handler?: scalar|Param|null,
 *             check_path?: scalar|Param|null, // Default: "/login_check"
 *             use_forward?: bool|Param, // Default: false
 *             login_path?: scalar|Param|null, // Default: "/login"
 *             username_parameter?: scalar|Param|null, // Default: "_username"
 *             password_parameter?: scalar|Param|null, // Default: "_password"
 *             csrf_parameter?: scalar|Param|null, // Default: "_csrf_token"
 *             csrf_token_id?: scalar|Param|null, // Default: "authenticate"
 *             enable_csrf?: bool|Param, // Default: false
 *             post_only?: bool|Param, // Default: true
 *             form_only?: bool|Param, // Default: false
 *             always_use_default_target_path?: bool|Param, // Default: false
 *             default_target_path?: scalar|Param|null, // Default: "/"
 *             target_path_parameter?: scalar|Param|null, // Default: "_target_path"
 *             use_referer?: bool|Param, // Default: false
 *             failure_path?: scalar|Param|null, // Default: null
 *             failure_forward?: bool|Param, // Default: false
 *             failure_path_parameter?: scalar|Param|null, // Default: "_failure_path"
 *         },
 *         form_login_ldap?: array{
 *             provider?: scalar|Param|null,
 *             remember_me?: bool|Param, // Default: true
 *             success_handler?: scalar|Param|null,
 *             failure_handler?: scalar|Param|null,
 *             check_path?: scalar|Param|null, // Default: "/login_check"
 *             use_forward?: bool|Param, // Default: false
 *             login_path?: scalar|Param|null, // Default: "/login"
 *             username_parameter?: scalar|Param|null, // Default: "_username"
 *             password_parameter?: scalar|Param|null, // Default: "_password"
 *             csrf_parameter?: scalar|Param|null, // Default: "_csrf_token"
 *             csrf_token_id?: scalar|Param|null, // Default: "authenticate"
 *             enable_csrf?: bool|Param, // Default: false
 *             post_only?: bool|Param, // Default: true
 *             form_only?: bool|Param, // Default: false
 *             always_use_default_target_path?: bool|Param, // Default: false
 *             default_target_path?: scalar|Param|null, // Default: "/"
 *             target_path_parameter?: scalar|Param|null, // Default: "_target_path"
 *             use_referer?: bool|Param, // Default: false
 *             failure_path?: scalar|Param|null, // Default: null
 *             failure_forward?: bool|Param, // Default: false
 *             failure_path_parameter?: scalar|Param|null, // Default: "_failure_path"
 *             service?: scalar|Param|null, // Default: "ldap"
 *             dn_string?: scalar|Param|null, // Default: "{user_identifier}"
 *             query_string?: scalar|Param|null,
 *             search_dn?: scalar|Param|null, // Default: ""
 *             search_password?: scalar|Param|null, // Default: ""
 *         },
 *         json_login?: array{
 *             provider?: scalar|Param|null,
 *             remember_me?: bool|Param, // Default: true
 *             success_handler?: scalar|Param|null,
 *             failure_handler?: scalar|Param|null,
 *             check_path?: scalar|Param|null, // Default: "/login_check"
 *             use_forward?: bool|Param, // Default: false
 *             login_path?: scalar|Param|null, // Default: "/login"
 *             username_path?: scalar|Param|null, // Default: "username"
 *             password_path?: scalar|Param|null, // Default: "password"
 *         },
 *         json_login_ldap?: array{
 *             provider?: scalar|Param|null,
 *             remember_me?: bool|Param, // Default: true
 *             success_handler?: scalar|Param|null,
 *             failure_handler?: scalar|Param|null,
 *             check_path?: scalar|Param|null, // Default: "/login_check"
 *             use_forward?: bool|Param, // Default: false
 *             login_path?: scalar|Param|null, // Default: "/login"
 *             username_path?: scalar|Param|null, // Default: "username"
 *             password_path?: scalar|Param|null, // Default: "password"
 *             service?: scalar|Param|null, // Default: "ldap"
 *             dn_string?: scalar|Param|null, // Default: "{user_identifier}"
 *             query_string?: scalar|Param|null,
 *             search_dn?: scalar|Param|null, // Default: ""
 *             search_password?: scalar|Param|null, // Default: ""
 *         },
 *         access_token?: array{
 *             provider?: scalar|Param|null,
 *             remember_me?: bool|Param, // Default: true
 *             success_handler?: scalar|Param|null,
 *             failure_handler?: scalar|Param|null,
 *             realm?: scalar|Param|null, // Default: null
 *             token_extractors?: list<scalar|Param|null>,
 *             token_handler: string|array{
 *                 id?: scalar|Param|null,
 *                 oidc_user_info?: string|array{
 *                     base_uri: scalar|Param|null, // Base URI of the userinfo endpoint on the OIDC server, or the OIDC server URI to use the discovery (require "discovery" to be configured).
 *                     discovery?: array{ // Enable the OIDC discovery.
 *                         cache?: array{
 *                             id: scalar|Param|null, // Cache service id to use to cache the OIDC discovery configuration.
 *                         },
 *                     },
 *                     claim?: scalar|Param|null, // Claim which contains the user identifier (e.g. sub, email, etc.). // Default: "sub"
 *                     client?: scalar|Param|null, // HttpClient service id to use to call the OIDC server.
 *                 },
 *                 oidc?: array{
 *                     discovery?: array{ // Enable the OIDC discovery.
 *                         base_uri: list<scalar|Param|null>,
 *                         cache?: array{
 *                             id: scalar|Param|null, // Cache service id to use to cache the OIDC discovery configuration.
 *                         },
 *                     },
 *                     claim?: scalar|Param|null, // Claim which contains the user identifier (e.g.: sub, email..). // Default: "sub"
 *                     audience: scalar|Param|null, // Audience set in the token, for validation purpose.
 *                     issuers: list<scalar|Param|null>,
 *                     algorithm?: array<mixed>,
 *                     algorithms: list<scalar|Param|null>,
 *                     key?: scalar|Param|null, // Deprecated: The "key" option is deprecated and will be removed in 8.0. Use the "keyset" option instead. // JSON-encoded JWK used to sign the token (must contain a "kty" key).
 *                     keyset?: scalar|Param|null, // JSON-encoded JWKSet used to sign the token (must contain a list of valid public keys).
 *                     encryption?: bool|array{
 *                         enabled?: bool|Param, // Default: false
 *                         enforce?: bool|Param, // When enabled, the token shall be encrypted. // Default: false
 *                         algorithms: list<scalar|Param|null>,
 *                         keyset: scalar|Param|null, // JSON-encoded JWKSet used to decrypt the token (must contain a list of valid private keys).
 *                     },
 *                 },
 *                 cas?: array{
 *                     validation_url: scalar|Param|null, // CAS server validation URL
 *                     prefix?: scalar|Param|null, // CAS prefix // Default: "cas"
 *                     http_client?: scalar|Param|null, // HTTP Client service // Default: null
 *                 },
 *                 oauth2?: scalar|Param|null,
 *             },
 *         },
 *         http_basic?: array{
 *             provider?: scalar|Param|null,
 *             realm?: scalar|Param|null, // Default: "Secured Area"
 *         },
 *         http_basic_ldap?: array{
 *             provider?: scalar|Param|null,
 *             realm?: scalar|Param|null, // Default: "Secured Area"
 *             service?: scalar|Param|null, // Default: "ldap"
 *             dn_string?: scalar|Param|null, // Default: "{user_identifier}"
 *             query_string?: scalar|Param|null,
 *             search_dn?: scalar|Param|null, // Default: ""
 *             search_password?: scalar|Param|null, // Default: ""
 *         },
 *         remember_me?: array{
 *             secret?: scalar|Param|null, // Default: "%kernel.secret%"
 *             service?: scalar|Param|null,
 *             user_providers?: list<scalar|Param|null>,
 *             catch_exceptions?: bool|Param, // Default: true
 *             signature_properties?: list<scalar|Param|null>,
 *             token_provider?: string|array{
 *                 service?: scalar|Param|null, // The service ID of a custom remember-me token provider.
 *                 doctrine?: bool|array{
 *                     enabled?: bool|Param, // Default: false
 *                     connection?: scalar|Param|null, // Default: null
 *                 },
 *             },
 *             token_verifier?: scalar|Param|null, // The service ID of a custom rememberme token verifier.
 *             name?: scalar|Param|null, // Default: "REMEMBERME"
 *             lifetime?: int|Param, // Default: 31536000
 *             path?: scalar|Param|null, // Default: "/"
 *             domain?: scalar|Param|null, // Default: null
 *             secure?: true|false|"auto"|Param, // Default: null
 *             httponly?: bool|Param, // Default: true
 *             samesite?: null|"lax"|"strict"|"none"|Param, // Default: "lax"
 *             always_remember_me?: bool|Param, // Default: false
 *             remember_me_parameter?: scalar|Param|null, // Default: "_remember_me"
 *         },
 *     }>,
 *     access_control?: list<array{ // Default: []
 *         request_matcher?: scalar|Param|null, // Default: null
 *         requires_channel?: scalar|Param|null, // Default: null
 *         path?: scalar|Param|null, // Use the urldecoded format. // Default: null
 *         host?: scalar|Param|null, // Default: null
 *         port?: int|Param, // Default: null
 *         ips?: list<scalar|Param|null>,
 *         attributes?: array<string, scalar|Param|null>,
 *         route?: scalar|Param|null, // Default: null
 *         methods?: list<scalar|Param|null>,
 *         allow_if?: scalar|Param|null, // Default: null
 *         roles?: list<scalar|Param|null>,
 *     }>,
 *     role_hierarchy?: array<string, string|list<scalar|Param|null>>,
 * }
 * @psalm-type LexikJwtAuthenticationConfig = array{
 *     public_key?: scalar|Param|null, // The key used to sign tokens (useless for HMAC). If not set, the key will be automatically computed from the secret key. // Default: null
 *     additional_public_keys?: list<scalar|Param|null>,
 *     secret_key?: scalar|Param|null, // The key used to sign tokens. It can be a raw secret (for HMAC), a raw RSA/ECDSA key or the path to a file itself being plaintext or PEM. // Default: null
 *     pass_phrase?: scalar|Param|null, // The key passphrase (useless for HMAC) // Default: ""
 *     token_ttl?: scalar|Param|null, // Default: 3600
 *     allow_no_expiration?: bool|Param, // Allow tokens without "exp" claim (i.e. indefinitely valid, no lifetime) to be considered valid. Caution: usage of this should be rare. // Default: false
 *     clock_skew?: scalar|Param|null, // Default: 0
 *     encoder?: array{
 *         service?: scalar|Param|null, // Default: "lexik_jwt_authentication.encoder.lcobucci"
 *         signature_algorithm?: scalar|Param|null, // Default: "RS256"
 *     },
 *     user_id_claim?: scalar|Param|null, // Default: "username"
 *     token_extractors?: array{
 *         authorization_header?: bool|array{
 *             enabled?: bool|Param, // Default: true
 *             prefix?: scalar|Param|null, // Default: "Bearer"
 *             name?: scalar|Param|null, // Default: "Authorization"
 *         },
 *         cookie?: bool|array{
 *             enabled?: bool|Param, // Default: false
 *             name?: scalar|Param|null, // Default: "BEARER"
 *         },
 *         query_parameter?: bool|array{
 *             enabled?: bool|Param, // Default: false
 *             name?: scalar|Param|null, // Default: "bearer"
 *         },
 *         split_cookie?: bool|array{
 *             enabled?: bool|Param, // Default: false
 *             cookies?: list<scalar|Param|null>,
 *         },
 *     },
 *     remove_token_from_body_when_cookies_used?: scalar|Param|null, // Default: true
 *     set_cookies?: array<string, array{ // Default: []
 *         lifetime?: scalar|Param|null, // The cookie lifetime. If null, the "token_ttl" option value will be used // Default: null
 *         samesite?: "none"|"lax"|"strict"|Param, // Default: "lax"
 *         path?: scalar|Param|null, // Default: "/"
 *         domain?: scalar|Param|null, // Default: null
 *         secure?: scalar|Param|null, // Default: true
 *         httpOnly?: scalar|Param|null, // Default: true
 *         partitioned?: scalar|Param|null, // Default: false
 *         split?: list<scalar|Param|null>,
 *     }>,
 *     api_platform?: bool|array{ // API Platform compatibility: add check_path in OpenAPI documentation.
 *         enabled?: bool|Param, // Default: false
 *         check_path?: scalar|Param|null, // The login check path to add in OpenAPI. // Default: null
 *         username_path?: scalar|Param|null, // The path to the username in the JSON body. // Default: null
 *         password_path?: scalar|Param|null, // The path to the password in the JSON body. // Default: null
 *     },
 *     access_token_issuance?: bool|array{
 *         enabled?: bool|Param, // Default: false
 *         signature?: array{
 *             algorithm: scalar|Param|null, // The algorithm use to sign the access tokens.
 *             key: scalar|Param|null, // The signature key. It shall be JWK encoded.
 *         },
 *         encryption?: bool|array{
 *             enabled?: bool|Param, // Default: false
 *             key_encryption_algorithm: scalar|Param|null, // The key encryption algorithm is used to encrypt the token.
 *             content_encryption_algorithm: scalar|Param|null, // The key encryption algorithm is used to encrypt the token.
 *             key: scalar|Param|null, // The encryption key. It shall be JWK encoded.
 *         },
 *     },
 *     access_token_verification?: bool|array{
 *         enabled?: bool|Param, // Default: false
 *         signature?: array{
 *             header_checkers?: list<scalar|Param|null>,
 *             claim_checkers?: list<scalar|Param|null>,
 *             mandatory_claims?: list<scalar|Param|null>,
 *             allowed_algorithms?: list<scalar|Param|null>,
 *             keyset: scalar|Param|null, // The signature keyset. It shall be JWKSet encoded.
 *         },
 *         encryption?: bool|array{
 *             enabled?: bool|Param, // Default: false
 *             continue_on_decryption_failure?: bool|Param, // If enable, non-encrypted tokens or tokens that failed during decryption or verification processes are accepted. // Default: false
 *             header_checkers?: list<scalar|Param|null>,
 *             allowed_key_encryption_algorithms?: list<scalar|Param|null>,
 *             allowed_content_encryption_algorithms?: list<scalar|Param|null>,
 *             keyset: scalar|Param|null, // The encryption keyset. It shall be JWKSet encoded.
 *         },
 *     },
 *     blocklist_token?: bool|array{
 *         enabled?: bool|Param, // Default: false
 *         cache?: scalar|Param|null, // Storage to track blocked tokens // Default: "cache.app"
 *     },
 * }
 * @psalm-type NelmioApiDocConfig = array{
 *     type_info?: bool|Param, // Use the symfony/type-info component for determining types. // Default: false
 *     use_validation_groups?: bool|Param, // If true, `groups` passed to @Model annotations will be used to limit validation constraints // Default: false
 *     cache?: array{
 *         pool?: scalar|Param|null, // define cache pool to use // Default: null
 *         item_id?: scalar|Param|null, // define cache item id // Default: null
 *     },
 *     documentation?: array<string, mixed>,
 *     media_types?: list<scalar|Param|null>,
 *     html_config?: array{ // UI configuration options
 *         assets_mode?: scalar|Param|null, // Default: "cdn"
 *         swagger_ui_config?: array<mixed>,
 *         redocly_config?: array<mixed>,
 *         stoplight_config?: array<mixed>,
 *     },
 *     areas?: array<string, array{ // Default: {"default":{"path_patterns":[],"host_patterns":[],"with_annotation":false,"with_attribute":false,"documentation":[],"name_patterns":[],"disable_default_routes":false,"cache":[]}}
 *         path_patterns?: list<scalar|Param|null>,
 *         host_patterns?: list<scalar|Param|null>,
 *         name_patterns?: list<scalar|Param|null>,
 *         with_annotation?: bool|Param, // Deprecated: The "with_annotation" option is deprecated. Use "with_attribute" instead. // whether to filter by annotation // Default: false
 *         with_attribute?: bool|Param, // whether to filter by attribute // Default: false
 *         disable_default_routes?: bool|Param, // if set disables default routes without annotations // Default: false
 *         documentation?: array<string, mixed>,
 *         cache?: array{
 *             pool?: scalar|Param|null, // define cache pool to use // Default: null
 *             item_id?: scalar|Param|null, // define cache item id // Default: null
 *         },
 *     }>,
 *     models?: array{
 *         use_jms?: bool|Param, // Default: false
 *         names?: list<array{ // Default: []
 *             alias: scalar|Param|null,
 *             type: scalar|Param|null,
 *             groups?: mixed, // Default: null
 *             options?: mixed, // Default: null
 *             serializationContext?: list<mixed>,
 *             areas?: list<scalar|Param|null>,
 *         }>,
 *     },
 * }
 * @psalm-type MonologConfig = array{
 *     use_microseconds?: scalar|Param|null, // Default: true
 *     channels?: list<scalar|Param|null>,
 *     handlers?: array<string, array{ // Default: []
 *         type: scalar|Param|null,
 *         id?: scalar|Param|null,
 *         enabled?: bool|Param, // Default: true
 *         priority?: scalar|Param|null, // Default: 0
 *         level?: scalar|Param|null, // Default: "DEBUG"
 *         bubble?: bool|Param, // Default: true
 *         interactive_only?: bool|Param, // Default: false
 *         app_name?: scalar|Param|null, // Default: null
 *         fill_extra_context?: bool|Param, // Default: false
 *         include_stacktraces?: bool|Param, // Default: false
 *         process_psr_3_messages?: array{
 *             enabled?: bool|Param|null, // Default: null
 *             date_format?: scalar|Param|null,
 *             remove_used_context_fields?: bool|Param,
 *         },
 *         path?: scalar|Param|null, // Default: "%kernel.logs_dir%/%kernel.environment%.log"
 *         file_permission?: scalar|Param|null, // Default: null
 *         use_locking?: bool|Param, // Default: false
 *         filename_format?: scalar|Param|null, // Default: "{filename}-{date}"
 *         date_format?: scalar|Param|null, // Default: "Y-m-d"
 *         ident?: scalar|Param|null, // Default: false
 *         logopts?: scalar|Param|null, // Default: 1
 *         facility?: scalar|Param|null, // Default: "user"
 *         max_files?: scalar|Param|null, // Default: 0
 *         action_level?: scalar|Param|null, // Default: "WARNING"
 *         activation_strategy?: scalar|Param|null, // Default: null
 *         stop_buffering?: bool|Param, // Default: true
 *         passthru_level?: scalar|Param|null, // Default: null
 *         excluded_404s?: list<scalar|Param|null>,
 *         excluded_http_codes?: list<array{ // Default: []
 *             code?: scalar|Param|null,
 *             urls?: list<scalar|Param|null>,
 *         }>,
 *         accepted_levels?: list<scalar|Param|null>,
 *         min_level?: scalar|Param|null, // Default: "DEBUG"
 *         max_level?: scalar|Param|null, // Default: "EMERGENCY"
 *         buffer_size?: scalar|Param|null, // Default: 0
 *         flush_on_overflow?: bool|Param, // Default: false
 *         handler?: scalar|Param|null,
 *         url?: scalar|Param|null,
 *         exchange?: scalar|Param|null,
 *         exchange_name?: scalar|Param|null, // Default: "log"
 *         room?: scalar|Param|null,
 *         message_format?: scalar|Param|null, // Default: "text"
 *         api_version?: scalar|Param|null, // Default: null
 *         channel?: scalar|Param|null, // Default: null
 *         bot_name?: scalar|Param|null, // Default: "Monolog"
 *         use_attachment?: scalar|Param|null, // Default: true
 *         use_short_attachment?: scalar|Param|null, // Default: false
 *         include_extra?: scalar|Param|null, // Default: false
 *         icon_emoji?: scalar|Param|null, // Default: null
 *         webhook_url?: scalar|Param|null,
 *         exclude_fields?: list<scalar|Param|null>,
 *         team?: scalar|Param|null,
 *         notify?: scalar|Param|null, // Default: false
 *         nickname?: scalar|Param|null, // Default: "Monolog"
 *         token?: scalar|Param|null,
 *         region?: scalar|Param|null,
 *         source?: scalar|Param|null,
 *         use_ssl?: bool|Param, // Default: true
 *         user?: mixed,
 *         title?: scalar|Param|null, // Default: null
 *         host?: scalar|Param|null, // Default: null
 *         port?: scalar|Param|null, // Default: 514
 *         config?: list<scalar|Param|null>,
 *         members?: list<scalar|Param|null>,
 *         connection_string?: scalar|Param|null,
 *         timeout?: scalar|Param|null,
 *         time?: scalar|Param|null, // Default: 60
 *         deduplication_level?: scalar|Param|null, // Default: 400
 *         store?: scalar|Param|null, // Default: null
 *         connection_timeout?: scalar|Param|null,
 *         persistent?: bool|Param,
 *         dsn?: scalar|Param|null,
 *         hub_id?: scalar|Param|null, // Default: null
 *         client_id?: scalar|Param|null, // Default: null
 *         auto_log_stacks?: scalar|Param|null, // Default: false
 *         release?: scalar|Param|null, // Default: null
 *         environment?: scalar|Param|null, // Default: null
 *         message_type?: scalar|Param|null, // Default: 0
 *         parse_mode?: scalar|Param|null, // Default: null
 *         disable_webpage_preview?: bool|Param|null, // Default: null
 *         disable_notification?: bool|Param|null, // Default: null
 *         split_long_messages?: bool|Param, // Default: false
 *         delay_between_messages?: bool|Param, // Default: false
 *         topic?: int|Param, // Default: null
 *         factor?: int|Param, // Default: 1
 *         tags?: list<scalar|Param|null>,
 *         console_formater_options?: mixed, // Deprecated: "monolog.handlers..console_formater_options.console_formater_options" is deprecated, use "monolog.handlers..console_formater_options.console_formatter_options" instead.
 *         console_formatter_options?: mixed, // Default: []
 *         formatter?: scalar|Param|null,
 *         nested?: bool|Param, // Default: false
 *         publisher?: string|array{
 *             id?: scalar|Param|null,
 *             hostname?: scalar|Param|null,
 *             port?: scalar|Param|null, // Default: 12201
 *             chunk_size?: scalar|Param|null, // Default: 1420
 *             encoder?: "json"|"compressed_json"|Param,
 *         },
 *         mongo?: string|array{
 *             id?: scalar|Param|null,
 *             host?: scalar|Param|null,
 *             port?: scalar|Param|null, // Default: 27017
 *             user?: scalar|Param|null,
 *             pass?: scalar|Param|null,
 *             database?: scalar|Param|null, // Default: "monolog"
 *             collection?: scalar|Param|null, // Default: "logs"
 *         },
 *         mongodb?: string|array{
 *             id?: scalar|Param|null, // ID of a MongoDB\Client service
 *             uri?: scalar|Param|null,
 *             username?: scalar|Param|null,
 *             password?: scalar|Param|null,
 *             database?: scalar|Param|null, // Default: "monolog"
 *             collection?: scalar|Param|null, // Default: "logs"
 *         },
 *         elasticsearch?: string|array{
 *             id?: scalar|Param|null,
 *             hosts?: list<scalar|Param|null>,
 *             host?: scalar|Param|null,
 *             port?: scalar|Param|null, // Default: 9200
 *             transport?: scalar|Param|null, // Default: "Http"
 *             user?: scalar|Param|null, // Default: null
 *             password?: scalar|Param|null, // Default: null
 *         },
 *         index?: scalar|Param|null, // Default: "monolog"
 *         document_type?: scalar|Param|null, // Default: "logs"
 *         ignore_error?: scalar|Param|null, // Default: false
 *         redis?: string|array{
 *             id?: scalar|Param|null,
 *             host?: scalar|Param|null,
 *             password?: scalar|Param|null, // Default: null
 *             port?: scalar|Param|null, // Default: 6379
 *             database?: scalar|Param|null, // Default: 0
 *             key_name?: scalar|Param|null, // Default: "monolog_redis"
 *         },
 *         predis?: string|array{
 *             id?: scalar|Param|null,
 *             host?: scalar|Param|null,
 *         },
 *         from_email?: scalar|Param|null,
 *         to_email?: list<scalar|Param|null>,
 *         subject?: scalar|Param|null,
 *         content_type?: scalar|Param|null, // Default: null
 *         headers?: list<scalar|Param|null>,
 *         mailer?: scalar|Param|null, // Default: null
 *         email_prototype?: string|array{
 *             id: scalar|Param|null,
 *             method?: scalar|Param|null, // Default: null
 *         },
 *         lazy?: bool|Param, // Default: true
 *         verbosity_levels?: array{
 *             VERBOSITY_QUIET?: scalar|Param|null, // Default: "ERROR"
 *             VERBOSITY_NORMAL?: scalar|Param|null, // Default: "WARNING"
 *             VERBOSITY_VERBOSE?: scalar|Param|null, // Default: "NOTICE"
 *             VERBOSITY_VERY_VERBOSE?: scalar|Param|null, // Default: "INFO"
 *             VERBOSITY_DEBUG?: scalar|Param|null, // Default: "DEBUG"
 *         },
 *         channels?: string|array{
 *             type?: scalar|Param|null,
 *             elements?: list<scalar|Param|null>,
 *         },
 *     }>,
 * }
 * @psalm-type ConfigType = array{
 *     imports?: ImportsConfig,
 *     parameters?: ParametersConfig,
 *     services?: ServicesConfig,
 *     framework?: FrameworkConfig,
 *     broadway?: BroadwayConfig,
 *     doctrine?: DoctrineConfig,
 *     doctrine_migrations?: DoctrineMigrationsConfig,
 *     twig?: TwigConfig,
 *     security?: SecurityConfig,
 *     lexik_jwt_authentication?: LexikJwtAuthenticationConfig,
 *     nelmio_api_doc?: NelmioApiDocConfig,
 *     monolog?: MonologConfig,
 *     "when@dev"?: array{
 *         imports?: ImportsConfig,
 *         parameters?: ParametersConfig,
 *         services?: ServicesConfig,
 *         framework?: FrameworkConfig,
 *         broadway?: BroadwayConfig,
 *         doctrine?: DoctrineConfig,
 *         doctrine_migrations?: DoctrineMigrationsConfig,
 *         twig?: TwigConfig,
 *         web_profiler?: WebProfilerConfig,
 *         security?: SecurityConfig,
 *         lexik_jwt_authentication?: LexikJwtAuthenticationConfig,
 *         nelmio_api_doc?: NelmioApiDocConfig,
 *         monolog?: MonologConfig,
 *     },
 *     "when@prod"?: array{
 *         imports?: ImportsConfig,
 *         parameters?: ParametersConfig,
 *         services?: ServicesConfig,
 *         framework?: FrameworkConfig,
 *         broadway?: BroadwayConfig,
 *         doctrine?: DoctrineConfig,
 *         doctrine_migrations?: DoctrineMigrationsConfig,
 *         twig?: TwigConfig,
 *         security?: SecurityConfig,
 *         lexik_jwt_authentication?: LexikJwtAuthenticationConfig,
 *         nelmio_api_doc?: NelmioApiDocConfig,
 *         monolog?: MonologConfig,
 *     },
 *     "when@test"?: array{
 *         imports?: ImportsConfig,
 *         parameters?: ParametersConfig,
 *         services?: ServicesConfig,
 *         framework?: FrameworkConfig,
 *         broadway?: BroadwayConfig,
 *         doctrine?: DoctrineConfig,
 *         doctrine_migrations?: DoctrineMigrationsConfig,
 *         twig?: TwigConfig,
 *         web_profiler?: WebProfilerConfig,
 *         dama_doctrine_test?: DamaDoctrineTestConfig,
 *         security?: SecurityConfig,
 *         lexik_jwt_authentication?: LexikJwtAuthenticationConfig,
 *         nelmio_api_doc?: NelmioApiDocConfig,
 *         monolog?: MonologConfig,
 *     },
 *     ...<string, ExtensionType|array{ // extra keys must follow the when@%env% pattern or match an extension alias
 *         imports?: ImportsConfig,
 *         parameters?: ParametersConfig,
 *         services?: ServicesConfig,
 *         ...<string, ExtensionType>,
 *     }>
 * }
 */
final class App
{
    /**
     * @param ConfigType $config
     *
     * @psalm-return ConfigType
     */
    public static function config(array $config): array
    {
        return AppReference::config($config);
    }
}

namespace Symfony\Component\Routing\Loader\Configurator;

/**
 * This class provides array-shapes for configuring the routes of an application.
 *
 * Example:
 *
 *     ```php
 *     // config/routes.php
 *     namespace Symfony\Component\Routing\Loader\Configurator;
 *
 *     return Routes::config([
 *         'controllers' => [
 *             'resource' => 'routing.controllers',
 *         ],
 *     ]);
 *     ```
 *
 * @psalm-type RouteConfig = array{
 *     path: string|array<string,string>,
 *     controller?: string,
 *     methods?: string|list<string>,
 *     requirements?: array<string,string>,
 *     defaults?: array<string,mixed>,
 *     options?: array<string,mixed>,
 *     host?: string|array<string,string>,
 *     schemes?: string|list<string>,
 *     condition?: string,
 *     locale?: string,
 *     format?: string,
 *     utf8?: bool,
 *     stateless?: bool,
 * }
 * @psalm-type ImportConfig = array{
 *     resource: string,
 *     type?: string,
 *     exclude?: string|list<string>,
 *     prefix?: string|array<string,string>,
 *     name_prefix?: string,
 *     trailing_slash_on_root?: bool,
 *     controller?: string,
 *     methods?: string|list<string>,
 *     requirements?: array<string,string>,
 *     defaults?: array<string,mixed>,
 *     options?: array<string,mixed>,
 *     host?: string|array<string,string>,
 *     schemes?: string|list<string>,
 *     condition?: string,
 *     locale?: string,
 *     format?: string,
 *     utf8?: bool,
 *     stateless?: bool,
 * }
 * @psalm-type AliasConfig = array{
 *     alias: string,
 *     deprecated?: array{package:string, version:string, message?:string},
 * }
 * @psalm-type RoutesConfig = array{
 *     "when@dev"?: array<string, RouteConfig|ImportConfig|AliasConfig>,
 *     "when@prod"?: array<string, RouteConfig|ImportConfig|AliasConfig>,
 *     "when@test"?: array<string, RouteConfig|ImportConfig|AliasConfig>,
 *     ...<string, RouteConfig|ImportConfig|AliasConfig>
 * }
 */
final class Routes
{
    /**
     * @param RoutesConfig $config
     *
     * @psalm-return RoutesConfig
     */
    public static function config(array $config): array
    {
        return $config;
    }
}
```

## File: `config/routes.yaml`
```yaml
api_controllers:
    resource: '../src/UI/Http/Rest/Controller/'
    type: attribute
    prefix: /api

web_controllers:
    resource: '../src/UI/Http/Web/Controller/'
    type: attribute
```

## File: `config/services.yaml`
```yaml
# Put parameters here that don't need to change on each machine where the app is deployed
# https://symfony.com/doc/current/best_practices/configuration.html#application-related-configuration
parameters:
  elastic:
    hosts:
      - '%env(ELASTIC_HOST)%'

  env(ELASTIC_HOST): 'elasticsearch:9200'
  env(DATABASE_URL): 'mysql://root:api@mysql:3306/api?serverVersion=8.0'

  exception_to_status:
    InvalidArgumentException: 400
    App\User\Domain\Exception\InvalidCredentialsException: 401
    App\User\Domain\Exception\ForbiddenException: 403
    App\Shared\Domain\Exception\NotFoundException: 404
    Broadway\Repository\AggregateNotFoundException: 404

services:
    _defaults:
        autowire: true
        autoconfigure: true
        public: false
        bind:
          $elasticConfig: '%elastic%'
          $eventBus: '@broadway.event_handling.event_bus'
          $eventStore: '@broadway.event_store.dbal'

    _instanceof:
        App\Shared\Application\Command\CommandHandlerInterface:
          public: true
          tags:
            - { name: messenger.message_handler, bus: messenger.bus.command }

        App\Shared\Application\Query\QueryHandlerInterface:
          public: true
          tags:
            - { name: messenger.message_handler, bus: messenger.bus.query }

        App\Shared\Infrastructure\Bus\AsyncEvent\AsyncEventHandlerInterface:
          public: true
          tags:
            - { name: messenger.message_handler, bus: messenger.bus.event.async }

        Broadway\EventHandling\EventListener:
          public: true
          tags:
              - { name: broadway.domain.event_listener }

    App\:
        resource: '../src/App/*'
        exclude: '../src/App/**/{Migrations,EventSubscriber}'
    UI\:
        resource: '../src/UI/*'
        exclude: '../src/UI/**/{EventSubscriber}'

    App\Shared\Infrastructure\Bus\Command\MessengerCommandBus:
        arguments:
          - '@messenger.bus.command'

    App\Shared\Infrastructure\Bus\Query\MessengerQueryBus:
        arguments:
          - '@messenger.bus.query'

    App\Shared\Infrastructure\Bus\AsyncEvent\MessengerAsyncEventBus:
        arguments:
          - '@messenger.bus.event.async'

    ### Interface bindings
    App\User\Domain\Repository\UserReadModelRepositoryInterface: '@App\User\Infrastructure\ReadModel\Mysql\MysqlReadModelUserRepository'
    App\Shared\Domain\Repository\EventRepositoryInterface: '@App\Shared\Infrastructure\Event\ReadModel\ElasticSearchEventRepository'
    App\User\Application\Query\Auth\AuthenticationProviderInterface: '@App\User\Infrastructure\Auth\AuthenticationProvider'

    ### UI

    UI\Cli\Command\:
        resource: '../src/UI/Cli/Command'

    UI\Http\Rest\Controller\:
        resource: '../src/UI/Http/Rest/Controller/*'
        tags: [ 'controller.service_arguments' ]

    UI\Http\Web\Controller\:
        resource: '../src/UI/Http/Web/Controller/*'
        tags: [ 'controller.service_arguments' ]

    ### UI Listeners

    UI\Http\Rest\EventSubscriber\ExceptionSubscriber:
        arguments:
            - "%kernel.environment%"
            - "%exception_to_status%"
        tags:
            - { name: 'kernel.event_listener', event: 'kernel.exception' }

    UI\Http\Rest\EventSubscriber\JsonBodyParserSubscriber:
        tags:
            - { name: 'kernel.event_listener', event: 'kernel.request', method: 'onKernelRequest', priority: 100 }
```

## File: `config/services_test.yaml`
```yaml
services:
    _defaults: {}

    Tests\App\Shared\Infrastructure\Event\EventCollectorListener:
      public: true
      tags:
          - { name: broadway.domain.event_listener }
```

## File: `config/doctrine/Domain.ValueObject.Auth.Credentials.orm.xml`
```xml
<?xml version="1.0" encoding="UTF-8"?>
<doctrine-mapping xmlns="https://doctrine-project.org/schemas/orm/doctrine-mapping"
                  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                  xsi:schemaLocation="https://doctrine-project.org/schemas/orm/doctrine-mapping
                  https://www.doctrine-project.org/schemas/orm/doctrine-mapping.xsd">

    <embeddable name="App\User\Domain\ValueObject\Auth\Credentials">
        <field name="email" type="email" column="email" unique="true"/>
        <field name="password" type="hashed_password" column="password"/>
    </embeddable>
</doctrine-mapping>
```

## File: `config/doctrine/Infrastructure.ReadModel.UserView.orm.xml`
```xml
<?xml version="1.0" encoding="UTF-8"?>
<doctrine-mapping xmlns="https://doctrine-project.org/schemas/orm/doctrine-mapping"
                  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                  xsi:schemaLocation="https://doctrine-project.org/schemas/orm/doctrine-mapping
                  https://www.doctrine-project.org/schemas/orm/doctrine-mapping.xsd">

    <entity name="App\User\Infrastructure\ReadModel\UserView" table="users">
        <id name="uuid" type="uuid_binary" column="uuid"/>

        <embedded name="credentials" class="App\User\Domain\ValueObject\Auth\Credentials"/>

        <field name="createdAt" type="datetime_immutable" column="created_at"/>
        <field name="updatedAt" type="datetime_immutable" column="updated_at" nullable="true"/>
    </entity>
</doctrine-mapping>
```

## File: `config/packages/broadway.yaml`
```yaml
broadway:
    event_store: broadway.event_store.dbal
```

## File: `config/packages/broadway_event_store_dbal.yaml`
```yaml
services:
    broadway.event_store.dbal:
        class: Broadway\EventStore\Dbal\DBALEventStore
        arguments:
            - "@doctrine.dbal.default_connection"
            - "@broadway.serializer.payload"
            - "@broadway.serializer.metadata"
            - "events"
            - true
            - "@broadway.uuid.converter"
```

## File: `config/packages/dama_doctrine_test_bundle.yaml`
```yaml
when@test:
    dama_doctrine_test:
        enable_static_connection: true
        enable_static_meta_data_cache: true
        enable_static_query_cache: true
```

## File: `config/packages/doctrine.yaml`
```yaml
doctrine:
    dbal:
        schema_filter: ~^(?!event)~ # this will ignore broadway event store table
        # Using explicit pdo_mysql driver - do not rely on URL scheme
        driver: pdo_mysql
        host: '%env(string:DATABASE_HOST)%'
        port: '%env(int:DATABASE_PORT)%'
        dbname: '%env(string:DATABASE_NAME)%'
        user: '%env(string:DATABASE_USER)%'
        password: '%env(string:DATABASE_PASSWORD)%'
        charset: utf8mb4
        server_version: '8.0.33'
        use_savepoints: true
        types:
          uuid_binary: Ramsey\Uuid\Doctrine\UuidBinaryType
          datetime_immutable: App\Shared\Infrastructure\Persistence\Doctrine\Types\DateTimeType
          email: App\User\Infrastructure\Persistence\Doctrine\Types\EmailType
          hashed_password: App\User\Infrastructure\Persistence\Doctrine\Types\HashedPasswordType
        mapping_types:
          uuid_binary: binary
    orm:
        auto_generate_proxy_classes: '%kernel.debug%'
        naming_strategy: doctrine.orm.naming_strategy.underscore_number_aware
        auto_mapping: false
        mappings:
            User:
                is_bundle: false
                type: xml
                dir: '%kernel.project_dir%/config/doctrine'
                prefix: 'App\User'
                alias: User
```

## File: `config/packages/doctrine_migrations.yaml`
```yaml
doctrine_migrations:
    services:
        Doctrine\Migrations\Version\MigrationFactory: 'App\Shared\Infrastructure\Persistence\Doctrine\MigrationsFactory\ContainerAwareFactory'
    migrations_paths:
        App\Shared\Infrastructure\Persistence\Doctrine\Migrations: '%kernel.project_dir%/src/App/Shared/Infrastructure/Persistence/Doctrine/Migrations'
```

## File: `config/packages/framework.yaml`
```yaml
framework:
    secret: '%env(APP_SECRET)%'
    default_locale: en
    csrf_protection: true
    http_method_override: false
    handle_all_throwables: true

    # Enables session support. Note that the session will ONLY be started if you read or write from it.
    # Remove or comment this section to explicitly disable session support.
    session:
        handler_id: null
        cookie_secure: auto
        cookie_samesite: lax
        storage_factory_id: session.storage.factory.native
    esi: true
    fragments: true
    php_errors:
        log: true
    router:
        strict_requirements: ~
        utf8: true
```

## File: `config/packages/framework_extra.yml`
```yaml
sensio_framework_extra:
    router:
        annotations: false
```

## File: `config/packages/lexik_jwt_authentication.yaml`
```yaml
lexik_jwt_authentication:
    secret_key: '%env(resolve:JWT_SECRET_KEY)%'
    public_key: '%env(resolve:JWT_PUBLIC_KEY)%'
    pass_phrase: '%env(JWT_PASSPHRASE)%'
    token_ttl: '%env(JWT_TTL)%'
```

## File: `config/packages/messenger.yaml`
```yaml
framework:
    messenger:
        default_bus: messenger.bus.command
        failure_transport: failed
        buses:
            # Default middleware is disabled on command/query buses intentionally.
            # These buses follow CQRS: one command = one handler, one query = one handler.
            # Validation and routing middleware are not needed; only handle_message is used.
            messenger.bus.command:
                default_middleware: false
                middleware:
                    - handle_message

            messenger.bus.query:
                default_middleware: false
                middleware:
                    - handle_message

            messenger.bus.event.async:
                default_middleware: allow_no_handlers

        transports:
            events:
                dsn: "%env(MESSENGER_TRANSPORT_DSN)%"
                retry_strategy:
                    delay: 2000
                    max_retries: 5
                    multiplier: 2
                    max_delay: 0
                options:
                    exchange:
                        type: topic
                        name: events
                    queues:
                        events:
                            binding_keys: ['#']

            users:
                dsn: "%env(MESSENGER_TRANSPORT_DSN)%"
                retry_strategy:
                    delay: 2000
                    max_retries: 5
                    multiplier: 2
                    max_delay: 0
                options:
                    exchange:
                        type: topic
                        name: events
                    queues:
                        users:
                            binding_keys: ['#.User.#']
            failed:
                dsn: "%env(MESSENGER_TRANSPORT_DSN)%"
                options:
                    queues:
                        failed:
                            binding_keys: ['#']

        routing:
            'Broadway\Domain\DomainMessage': events
```

## File: `config/packages/monolog.yaml`
```yaml
monolog:
    channels:
        - deprecation # Deprecations are logged in the dedicated "deprecation" channel when it exists

when@dev:
    monolog:
        handlers:
            main:
                type: stream
                path: "%kernel.logs_dir%/%kernel.environment%.log"
                level: debug
                channels: ["!event"]
            console:
                type: console
                process_psr_3_messages: false
                channels: ["!event", "!doctrine", "!console"]

when@test:
    monolog:
        handlers:
            main:
                type: fingers_crossed
                action_level: error
                handler: nested
                excluded_http_codes: [404, 405]
                channels: ["!event"]
            nested:
                type: stream
                path: "%kernel.logs_dir%/%kernel.environment%.log"
                level: debug

when@prod:
    monolog:
        handlers:
            main:
                type: fingers_crossed
                action_level: error
                handler: nested
                excluded_http_codes: [404, 405]
                channels: ["!deprecation"]
                buffer_size: 50 # How many messages should be saved? Prevent memory leaks
            nested:
                type: stream
                path: php://stderr
                level: debug
                formatter: monolog.formatter.json
            console:
                type: console
                process_psr_3_messages: false
                channels: ["!event", "!doctrine"]
            deprecation:
                type: stream
                channels: [deprecation]
                path: php://stderr
                formatter: monolog.formatter.json
```

## File: `config/packages/nelmio_api_doc.yaml`
```yaml
nelmio_api_doc:

    documentation:
        servers:
            - url: http://es.local
              description: API over HTTP
        info:
            title: jorge07/symfony-5-es-cqrs-boilerplate
            description: Symfony 7 DDD ES CQRS backend boilerplate
            version: 1.0.0
        components:
            securitySchemes:
                Bearer:
                    type: http
                    scheme: bearer
                    bearerFormat: JWT
            parameters:
                page:
                    name: page
                    in: query
                    example: 1
                    schema:
                        type: integer
                limit:
                    name: limit
                    in: query
                    example: 10
                    schema:
                        type: integer
            responses:
                events:
                    description: Event list
                    content:
                        application/json:
                            schema:
                                type: object
                                properties:
                                    meta:
                                        ref: "#/components/schemas/ResponseCollectionMeta"
                                    data:
                                        type: array
                                        items:
                                            $ref: "#/components/schemas/DomainMessage"
                                    relationships:
                                        ref: "#/components/schemas/Relationships"

                users:
                    description: Users list
                    content:
                        application/json:
                            schema:
                                type: object
                                properties:
                                    data:
                                        $ref: "#/components/schemas/UserView"
                                    relationships:
                                        ref: "#/components/schemas/Relationships"

            schemas:
                UserView:
                    type: object
                    properties:
                        uuid:
                            type: string
                            example: 7be33fd4-ff46-11ea-adc1-0242ac120002
                        createdAt:
                            type: string
                            format: date-time
                        updatedAt:
                            type: string
                            format: date-time
                        credentials:
                            type: object
                            properties:
                                email:
                                    type: string
                                    example: 'j@j.com'
                                password:
                                    type: string
                                    example: ;klsdjhsd;gjkdhg;sldkgjhs;dlkgjsd;lfgkj

                ResponseCollectionMeta:
                    type: object
                    properties:
                        size:
                            type: integer
                        page:
                            type: integer
                        total:
                            type: integer

                Relationships:
                    type: object
                    properties:
                        data:
                            type: array
                            items:
                                type: object
                                properties:
                                    id:
                                        type: string
                                    type:
                                        type: string
                                    attributes:
                                        type: object
                Error:
                    type: object
                    properties:
                        error:
                            type: object
                            properties:
                                title:
                                    type: string
                                    example: InvalidArgumentException
                                detail:
                                    type: string
                                    example: 'Password should contain at least 6 characters'
                                code:
                                    type: string
                                    example: 500005322

                DomainMessage:
                    type: object
                    properties:
                        playhead:
                            type: integer
                        metadata:
                            type: object
                            $ref: "#/components/schemas/MessageMetadata"
                        payload:
                            type: object
                            example:
                                uuid: "7be33fd4-ff46-11ea-adc1-0242ac120002"
                                credentials:
                                    email: "j@j.com"
                                    password: "$2y$12$v4wrj2vgndDpWfMzTaTDTeftCo0jchvXWJliZ0GNN9bYM9Q0rACSC"
                                created_at: "2020-09-25T15:49:31.750754+00:00"
                        id:
                            type: string
                        recordedOn:
                            type: string
                            format: data-time

                MessageMetadata:
                    type: object
                    properties:
                        values:
                            type: array
                            items:
                                type: string
                                example:
                                    - { stream: master }

        security:
            - Bearer: []
    areas: # to filter documented areas
        path_patterns:
            - ^/api(?!/doc$) # Accepts routes under /api except /api/doc
```

## File: `config/packages/property_info.yaml`
```yaml
framework:
    property_info:
        with_constructor_extractor: true
```

## File: `config/packages/ramsey_uuid_doctrine.yaml`
```yaml
doctrine:
    dbal:
        types:
            uuid: 'Ramsey\Uuid\Doctrine\UuidType'
```

## File: `config/packages/routing.yaml`
```yaml
framework:
    router:
        # Configure how to generate URLs in non-HTTP contexts, such as CLI commands.
        # See https://symfony.com/doc/current/routing.html#generating-urls-in-commands
        default_uri: '%env(DEFAULT_URI)%'

when@prod:
    framework:
        router:
            strict_requirements: null
```

## File: `config/packages/security.yaml`
```yaml
security:
    password_hashers:
        hasher:
            id: App\User\Infrastructure\Auth\PasswordHasher

    providers:
        users:
            id: 'App\User\Infrastructure\Auth\AuthProvider'

    firewalls:
        dev:
            pattern: ^/(_(profiler|wdt)|css|images|js)/
            security: false

        api_healthz:
            pattern:  ^/api/healthz
            stateless: true

        api_doc:
            pattern:  ^/api/doc
            stateless: true

        api_auth:
            pattern:  ^/api/auth
            stateless: true

        api_signup:
            pattern:  ^/api/signup
            stateless: true

        api_secured:
            pattern:  ^/api
            provider: users
            stateless: true
            jwt: ~

        secured_area:
            pattern: ^/
            provider: users
            custom_authenticators:
            - 'App\User\Infrastructure\Auth\Guard\LoginAuthenticator'
            form_login:
              login_path: /sign-in
              check_path: sign-in
            entry_point: form_login
            logout:
              path: /logout
              target: /

    access_control:
        - { path: ^/profile,      roles: ROLE_USER }
        - { path: ^/api/healthz, roles: PUBLIC_ACCESS }
        - { path: ^/api/auth,    roles: PUBLIC_ACCESS }
        - { path: ^/api/signup,  roles: PUBLIC_ACCESS }
        - { path: ^/api/doc,     roles: PUBLIC_ACCESS }
        - { path: ^/api/,        roles: IS_AUTHENTICATED }
        - { path: ^/,            roles: PUBLIC_ACCESS }
```

## File: `config/packages/twig.yaml`
```yaml
twig:
    paths: ['%kernel.project_dir%/src/UI/Http/Web/templates']
    debug: '%kernel.debug%'
    strict_variables: '%kernel.debug%'
```

## File: `config/packages/web_profiler.yaml`
```yaml
when@dev:
    web_profiler:
        toolbar: true

    framework:
        profiler:
            collect_serializer_data: true

when@test:
    framework:
        profiler:
            collect: false
            collect_serializer_data: true
```

## File: `config/packages/dev/monolog.yaml`
```yaml
monolog:
    channels: ['elasticsearch']
    handlers:
        elasticsearch:
            type: stream
            path: "%kernel.logs_dir%/elasticsearch_%kernel.environment%.log"
            level: debug
            channels: ["elasticsearch"]
        main:
            type: stream
            path: "%kernel.logs_dir%/%kernel.environment%.log"
            level: debug
            channels: ["!event", "!elasticsearch"]
        # uncomment to get logging in your browser
        # you may have to allow bigger header sizes in your Web server configuration
        #firephp:
        #    type: firephp
        #    level: info
        #chromephp:
        #    type: chromephp
        #    level: info
        console:
            type: console
            process_psr_3_messages: false
            channels: ["!event", "!doctrine", "!console"]
```

## File: `config/packages/dev/routing.yaml`
```yaml
framework:
    router:
        strict_requirements: true
```

## File: `config/packages/dev/web_profiler.yaml`
```yaml
web_profiler:
    toolbar: true
    intercept_redirects: false

framework:
    profiler: { only_exceptions: false }
```

## File: `config/packages/jwt/private.pem`
```
-----BEGIN RSA PRIVATE KEY-----
Proc-Type: 4,ENCRYPTED
DEK-Info: AES-256-CBC,792228813A9EC4CE7F0C2FA88B8F7E4A

c45CpYXNxDnAQV3BBYy8te6oDL/dwVHmU1Ckkc3cXNG34n/wbD7Hj1E7u6SjZKdO
I2mAuqWvSqPIFb0/x1f1Ft21W8JZlD3zj7dd/kN52xBl1XYhO1GMVGO8jKip6TpY
RLzN5TGn4aSzZcp1g2tLxurc/J96JjIYGx2b1OA6drc6F5AHx2lTluFnnXC8dyEj
HQE3xfHC42ILluIPU/3CVg+RzTz23G2xsn/iz5P2jHfj6bvLseJsTTgge57Wbs+a
q+prszljEwwlULQtt3EU2M8Kcydh9PE3uwwwuejpXg5nflrOer6y9joY84LeLdYq
1BFfY3PEII2ZgcsUx1+wPrd5Ojw0iPS3BSHedaEGJiGAEiQl0NbU/VxOtQmigwhw
TrmqlXDJT08LBKfeTneDpfZZIkwFrSW9GguZczMx5bGRHThEXkalwhZqsfwzuOhl
TqMtbJ5MdI263piHwOjuIsA6/qa5Vy0cRJjURSyjc3y0Qku1XVRjJMh6FAfwyZtM
0KaX/ghUBDA4mCWe5MDhld2p+lSaTPqZAK1lyMfAVgdFNaxhIRhjOKcojY6OFTjN
bcdvh2VObC8bs5Vti+lIRCqEnvk5b7tz3xTyT6p1n0pux0hHGElrNX0JJjumrpa5
f0nbLllpRxf2Kz357EGn17bdPmj7K+h9FAqLsunV3LObt4nW/j4mXLdtAb7+B+gP
zgQuf/5/0Kbvx1lycuhBpP6auRLbmP0c+mhZ03acRpnZGtQjRXbxsMDGWxK/eQw2
MeFKLDBqtMOjc+8y5EAqHyavAfp3YwzbWMAAfxz6bZOwvy30tsBpL83iBHQ7wGq7
b/BKdOcc6i3tz7nfDK7GVODBcpuq9ptTqJmeTV3gPAVaqnSIHq3jb0jVdnnURukx
9sE/IBRqo690hVWj5+TYr1ZxzhEaU7ip8G6qbftI59y3yPnK7QmkcyMfXhtfLTer
BZRy+XMdruCyltzFFScKOKP6x7qsuQ60kpWvCVWglL8mit4XI9bHUiZ2wwwhlGuP
nNLkU7IVtY7L/NcMAa2a+NMM9ezr19QoLbjoH91gxI3fsm4u8+UpBZ7kRUnucOmj
Hh17lG9Xbl/1kqshHSFDRdBVuFZKmRPtIJpi5V3sVJKvoqjbcfeoXjC97IaSZJYU
xFzZWL3xD/vn5JljhlsswTRKp+ZTyhgGrPKRzTvCZcbThrkweE6D3fBVVim6ltLI
uhNWAn/ZlZv1F4K7nEtgqBwJWsB7Xs33J0DOWjiU2+0/oCg9dQQkyiQ5zGJA2tki
3D/Gd+vabB035ZeJ8x345DRCDuMeAjTu4fkfbiFLUd8YGgXfUNk3riPCSxUuOuUf
UQtnQiq7Tg2UTxieunv/ni03+W3muSuPdNJ0z2ok+vMeMeZuDmTr0TlTWhri77eN
pTcqb/1V1Nje8kKTmLTVnDimdfJDtr6c11BMIwOOVnhKF2POh4bQChJSYY5yx5LQ
5gL0qbKhOA5McvDMLVASI/wilhF3Ji2StUuinjSncyVJSxkOA56tG/ASMTYbynws
vg9s0IfuD0g3FxG54KQw6QrYMEuMy3CU2tG/UHO46V6YWHmQMvp/wvfkzq7+b4n9
o9o49uWdpnlml5T5dY9FUdJ9E0KE2nDGjqKSk3gKAXFyeQGUmCjeb64u9gjz7Q1a
2Gefzz8f0J13SfHNOgMMzvR6hja45JA0huaHT4qi3VqUbsvtuiAEJs+GB1u6a2CH
3HCgMB8A9H0EixZXh51PPVfZ6fksZSEz/2SEFCu02UXK3y8u/VcOWZ3qdOMFzaED
N79SOBzNjNuV2/hGwOWFQFEHnYq9Dp2Q8voUEzLHBer5KG20U4NVQwalWv9KiBRB
IJxBKURUltbd0ajgqx45uKVFxdmjNplwDTseygqFmYiFcyi4MaxPG58+nYEz6rRB
YiI68IWS3abre1ftWE5e6Mmod0XegBUk4dG4LSnso+pdsYUUWvUi3uyK+wnA5RSS
Hnfghf9aGKNKpkiooTdQnya9NR7ZbqquQhW6sCn1IeochfMihOez7WQ+TbTNUtbL
HP/hSjzCroBPavSnwlwefZSMHtZdF33UVr6hKddbHUDHtulQjaSzP6BFvyw/AHvq
YAkxZcwJsjDxicp5G7ayYQE7t6geAs1iKrYO9Cl7Qe1LgstPfz4A+bjmCLhd4Xjt
GILyQP0c/ZX0vJBGZfm8n3Mfr2+M9mdmEcNrODifuUdD+HBRiq/uNyBgHcJBv1pR
AsNH/CmAHROFVi4TtTVUlQszn1hfOWb7NPPLKo4ZpF1LBzr6f2Xohz8XWygV+7pY
WqrIkhvww/f7EiiI1bX62DsTkRNAZyHbZ7QEz5Cc4ZxNM5oDgW0QfIwfwlX84Q3m
UUlkiV7802k8vXGdQIuo41vVxr+4DUAlyQwd7UHtAuO1I87ByTEGUswX7ZSAxx8a
z8msiKE1e/iav2Z/lrLanIUpCdqPYrnOMCNFyrzb1qsjH/ieLHyN+3h93JmqEDPC
90N+D+2JJdeuQkjBcvmcyo8gag/1UU4iatqEMRmdpfZf/kzHimIDIFgC0G3ZkRE0
b/IpI1SYcClC2ab4CTfOJ7/tpMM9FZEEP+vJFN/e4w9RrXJwerdbyxBn6thXVQ22
Cl8aP0w/mr6IObSdVbkUdkeBynPsw7Em7NPrG7SzK79xd2EcgFJ8eQXFJVnE5MVe
6yPrR9C4syif8GvfWrSNL+HaNCOxPkz592ZN5wiXRt8YE+wI8n8irDIHldDPNuGu
f/nuwkRCwL2LQCZKHJO3sWBaoFc3N4vSTnWt89QpRPjCrOEf1xBbNJ5ZpfURw087
5Kvs5BPJTOiWQK9FsVyseIU85mONNpxGPrGhnH/YYkXm88OawlNp87BGLO/KUdDx
FKfLxNHNQIAxWI1lHkxC6pgCpgubuv779eO2L4AFuNndKXSmH/jb5HevfMPFjVEB
HbBTF960aC1bNqP8lEVpIv+PUcKfjjaMaVU1ZhFLVUWnl0fru41cI26rw/awGR+0
FPm2Joesl+d5OocUoPGhlQh5PPwE6ZdG+Cc4kuKO2KkYTTuLjkD8N6Irboeqccjx
G2FcaxDlNATrv2H3mDhf7TjklpEnlMSXlGyUDoRoUFclLzYNNqiHoRmw9zvPumq3
-----END RSA PRIVATE KEY-----
```

## File: `config/packages/jwt/public.pem`
```
-----BEGIN PUBLIC KEY-----
MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEArBmtoOEVG2GQ9ttdVxhc
ZbLPrUADHQv1xVqV5H61mVcgfbtoRGdFUFuHD4DVopuSR2FhXMDRz0ukOTgwODOd
ri6+aG2+3Dir1oS4VS63OmvCE+ylS9+EbgJkAJMGRM1/pDg61l89+Xc7Wab2/Io3
Q0o39obFVPLnvOSAKng7Ekm3+fC8bRH3EvN2eYaFmvcxn97gEtym+8x+8PXYIICw
WGRp0Tt62ldNhoWkWiY7c1c4+M3A9gIasoNYyxSU7v2oze+MIStWtkDnzhVtYwDf
3IOVvGxEBAzqYQ9ICI2eUQjf8edcbTIpkI4wBJ1Iz1wi9WJD+c5OP/RMrcKPyO2p
WeHuGbhasevkBeJi1fGClhjb/FwswGeEpcIVN59dafsPJ6U2Oj/RQJQQydEgnNfl
+rxCd/yIl3/Mo0gORL7j2WBPND5k/kVeEFAAA5S6KvwDfvVCJ7ka8IuAsZd5QZCC
OzhpRjCT4JgBa9lJS/ShGguE3/0A0JnqpaqbB+u3qMzRktnVqjTW0htjnmsCB8UH
JTqqSKRUAygJ9MbxQ+o252xEg+S0VHLDHA79ONiOVRZczbVtVjvZLLIVmeJYXTSc
dq97Dy43x+mYSs+RL74Xg+vf4LGoEgBEV++DBg1ELonDoFwdVJwVqUgRk7awf8ZT
gZV/5L0JJAEb4srJ9VrDntkCAwEAAQ==
-----END PUBLIC KEY-----
```

## File: `config/packages/prod/doctrine.yaml`
```yaml
doctrine:
    orm:
        metadata_cache_driver:
            type: pool
            pool: doctrine.system_cache_pool
        query_cache_driver:
            type: pool
            pool: doctrine.system_cache_pool
        result_cache_driver:
            type: pool
            pool: doctrine.result_cache_pool

framework:
    cache:
        pools:
            doctrine.result_cache_pool:
                adapter: cache.app
            doctrine.system_cache_pool:
                adapter: cache.system
```

## File: `config/packages/prod/monolog.yaml`
```yaml
monolog:
    handlers:
        main:
            type:         fingers_crossed
            action_level: error
            handler:      nested
            excluded_http_codes: [404, 405]
            buffer_size: 50
        nested:
            type:  stream
            path:  "php://stdout"
            level: debug
            formatter:  monolog.formatter.json
        console:
            type:  console
            process_psr_3_messages: false
            channels: ["!event", "!doctrine"]
```

## File: `config/packages/test/dama_doctrine_test_bundle.yaml`
```yaml
dama_doctrine_test:
    enable_static_connection: true
    enable_static_meta_data_cache: true
    enable_static_query_cache: true
```

## File: `config/packages/test/framework.yaml`
```yaml
framework:
    test: true
    session:
        storage_factory_id: session.storage.factory.mock_file
    messenger:
        transports:
            events: 'in-memory://'
            users: 'in-memory://'
            failed: 'in-memory://'
```

## File: `config/packages/test/monolog.yaml`
```yaml
monolog:
    handlers:
        main:
            type: fingers_crossed
            action_level: error
            handler: nested
            excluded_http_codes: [404, 405]
            channels: ["!event"]
        nested:
            type: stream
            path: "%kernel.logs_dir%/%kernel.environment%.log"
            level: debug
```

## File: `config/packages/test/web_profiler.yaml`
```yaml
web_profiler:
    toolbar: false
    intercept_redirects: false

framework:
    profiler: { collect: false }
```

## File: `config/routes/framework.yaml`
```yaml
when@dev:
    _errors:
        resource: '@FrameworkBundle/Resources/config/routing/errors.php'
        prefix: /_error
```

## File: `config/routes/nelmio_api_doc.yaml`
```yaml
# Expose your documentation as JSON swagger compliant
app.swagger:
    path: /api/doc.json
    methods: GET
    defaults: { _controller: nelmio_api_doc.controller.swagger }

## Requires the Asset component and the Twig bundle
## $ composer require twig asset
app.swagger_ui:
    path: /api/doc
    methods: GET
    defaults: { _controller: nelmio_api_doc.controller.swagger_ui }
```

## File: `config/routes/security.yaml`
```yaml
_security_logout:
    resource: security.route_loader.logout
    type: service
```

## File: `config/routes/web_profiler.yaml`
```yaml
when@dev:
    web_profiler_wdt:
        resource: '@WebProfilerBundle/Resources/config/routing/wdt.php'
        prefix: /_wdt

    web_profiler_profiler:
        resource: '@WebProfilerBundle/Resources/config/routing/profiler.php'
        prefix: /_profiler
```

## File: `config/routes/dev/twig.yaml`
```yaml
_errors:
    resource: '@FrameworkBundle/Resources/config/routing/errors.xml'
    prefix: /_error
```

## File: `config/routes/dev/web_profiler.yaml`
```yaml
web_profiler_wdt:
    resource: '@WebProfilerBundle/Resources/config/routing/wdt.xml'
    prefix: /_wdt

web_profiler_profiler:
    resource: '@WebProfilerBundle/Resources/config/routing/profiler.xml'
    prefix: /_profiler
```

## File: `doc/Deployment.md`
```markdown
## Kubernetes Deployment

`make minikube`

### Update

`helm upgrade cqrs -f {YOUR CUSTOM YAML FILE} etc/deploy/chart`

### Recommendations

- Use your own chart registry. i.e: https://github.com/helm/chartmuseum
- Use separated `values.yaml` per environment and concat in deployments. i.e: `helm upgrade cqrs -f production.yaml etc/deploy/chart`
- Use helm secrets plugin: https://github.com/futuresimple/helm-secrets
```

## File: `doc/Workflow.md`
```markdown
## Workflow

**Given** An annon user

 **When** enters in homepage 
 
 **Then** should be able to see the Sign Up button
 
![Home](https://imgur.com/ykxHf1d.png)

 **When** user click in Sign Up button 
 
 **Then** should be redirected to Sign Up page

![Sign up](https://imgur.com/qZs8iIP.png)


**Given** a user in Sign Up page

 **When** enter in the form with a valid email and password
 
![invalid email](https://imgur.com/w9Z1w8d.png)

 **Then** it should be registered

  **And** display de user information
 
![signed up](https://imgur.com/XbRtfUh.png)

 **Then** when user enter in Sign In page should be able to Sign In
   
  **And** open a new session

 ![Signed in](https://imgur.com/ZjmTDYU.png)

 **Given** All user events happened in UI
   
   **And** published in rabbit

 ![rmq](https://imgur.com/XobqV9j.png)

  **Then** it should be consumed to be  stored in elastic

   **And** visible in Kibana

![kibana](https://imgur.com/VMRLSDJ.png)
```

## File: `doc/GetStarted/Async.md`
```markdown
# Async Jobs

All events are published in RabbitMQ through `App\Infrastructure\Shared\Event\Publisher\AsyncEventPublisher`. The reason of this is that others can consume this events in background.

#### How it works?

The `AsyncEventPublisher` implements 2 important interfaces.

- `Broadway\EventHandling\EventListener`
	- It binds this class to the **EventBus** and invoke method `handle` that collect the events in memory inside the class.
- `Symfony\Component\EventDispatcher\EventSubscriberInterface`
	- This binds the class to **{KernelEvents,ConsoleEvents}::TERMINATE** Symfony events and invoke method `publish`

By that way we're sending the messages to RabbitMQ after respond to the client so we don't lock the client for things not required to wait.

#### Consume this events

Create you own consumer:
```php
<?php

declare(strict_types=1);

namespace App\Demo\Infrastructure\Event\Consumer;

use OldSound\RabbitMqBundle\RabbitMq\ConsumerInterface;
use PhpAmqpLib\Message\AMQPMessage;

class DemoEventsConsumer implements ConsumerInterface
{
    public function execute(AMQPMessage $msg): void
    {
        var_dump(unserialize($msg->body));
    }
}
```

#### Configure you consumer:

```yaml
old_sound_rabbit_mq:
	...
    multiple_consumers:
        events:
            ....
            queues:
                 ....
+                var_dump_all_events:
+                    name: var_dump_all_events
+                    routing_keys:
+                        - 'App.Domain.#'
+                    callback: App\Demo\Infrastructure\Event\Consumer\DemoEventsConsumer
```

### Running the Consumer

By default all consumers are invoked with container:

`docker-compose.yml`
```yaml
  workers:
    image: jorge07/alpine-php:7.2-dev-sf
    volumes:
      - .:/app
    command: ['/app/bin/console', 'rabbitmq:multiple-consumer', 'events']
```

**To run just our new consumer:** Inside docker container:
`./bin/console rabbitmq:consumer var_dump_all_events`

Full doc with much better example here: https://github.com/php-amqplib/RabbitMqBundle

#### Routing keys

So simple, it replaces namespaces `\` for `.`, example:

`App\User\Domain\Event\UserWasCreated` -> `App.User.Domain.Event.UserWasCreated`

You can bind you consumer to:
 
 - All events: `#` 
 - All domain events: `#.Domain.#`
 - All domain context boundary events: `#.User.Domain.#`
 - A one particular event: `App.User.Domain.Event.UserWasCreated`
 - Combination of keys:
    - `App.User.Domain.#`
    - `App.Payments.Domain.#`
    - `App.Cart.Domain.Event.OrderWasCreated`
    - `App.Cart.Domain.Event.OrderWasCanceled`
 
 Much better explained in the official documentation: https://www.rabbitmq.com/tutorials/tutorial-five-python.html
```

## File: `doc/GetStarted/Buses.md`
```markdown
# Command Bus, Query Bus and Async Event Bus

### Symfony Messenger Component

[Symfony Messenger](https://symfony.com/doc/current/messenger.html) is what we use to distribute messages synchronous and asynchronously.

We've 3 different type of bus:

- Command: `public function handle(CommandInterface $command): void`
- Query: `public function handle(QueryInterface $query): Item|Collection|string|int|null`
- Async Event: `public function handle(EventInterface $event): void`
	
To define a new use case just implement the required interfaces.

Use `./bin/console debug:messenger` to check the configuration.
```

## File: `doc/GetStarted/Projections.md`
```markdown
# Creating a new Projection

A Projection is a representation of a stream of events (aggregates) into a structural representation, usually called, read model.

Let's say we want to store the list of emails in a separated ElasticSearch index for testing purpose.


#### Infrastructure implementation

```php
<?php

declare(strict_types=1);

namespace App\User\Infrastructure\ReadModel\Projections;

use App\User\Domain\ValueObject\Email;
use Broadway\Serializer\Serializable;
use Ramsey\Uuid\Uuid;
use Ramsey\Uuid\UuidInterface;

class UserListProjection implements SerializableReadModel
{
    /** @var UuidInterface */
    public $uuid;

    /** @var Email */
    public $email;

    public static function fromSerializable(Serializable $event): self
    {
        return self::deserialize($event->serialize());
    }

    public static function deserialize(array $data): self
    {
        $instance = new self();

        $instance->uuid = Uuid::fromString($data['uuid']);
        $instance->email = Email::fromString($data['email']);

        return $instance;
    }

    public function serialize(): array
    {
        return [
            'uuid'  => $this->getId(),
            'email' => (string) $this->email,
        ];
    }

    public function getId(): string
    {
        return $this->uuid->toString();
    }
}
```

> Then you need to implement the Infrastructure for this. Something like `App\Infrastructure\User\Query\Repository\UserEmailListElasticSearchRepository`

> If a Doctrine mapping is required, define your mapping in `config/packages/doctrine/mapping` and configure doctrine mapping too if required `config/packages/doctrine.yaml`.

### Migrations

This boilerplate comes with built in migrations thanks to DoctrineMigrationsBundle. 2 options:

- Add your mapping and then use the makefile shortcut: `make dmd`
- Shell into the php container and run ti manually: 
  - `make s=php shell`
  - `./bin/console d:m:diff`

#### Create the Projector Listener

```php
<?php

declare(strict_types=1);

namespace App\User\Infrastructure\Query;

use App\User\Domain\Event\UserWasCreated;
use App\User\Infrastructure\ReadModel\Projections\UserListProjection;
use Broadway\ReadModel\Projector;

class UserEmailReadProjectionFactory extends Projector
{
    protected function applyUserWasCreated(UserWasCreated $userWasCreated): void
    {
        $userReadModel = UserListProjection::deserialize([
            'uuid' => $userWasCreated->uuid,
            'email' => $userWasCreated->credentials->email
		]);

        $this->repository->add($userReadModel);
    }

    protected function applyUserEmailChanged(UserEmailChanged $emailChanged): void
    {
        $this->repository->replace($emailChanged->uuid, $emailChanged->email);
    }
    public function __construct(UserEmailListReadModelRepositoryInterface $repository)
    {
        $this->repository = $repository;
    }

    /** @var UserEmailListReadModelRepositoryInterface */
    private $repository;
}
```

And you're done. 

### Why this works?

`Broadway\ReadModel\Projector` implements `Broadway\EventHandling\EventListener` so it's automatically added to the service container and tagged as a Broadway event listener.

`config/services.yaml`
```yaml

services:
    ...
    _instanceof:
        ...
        Broadway\EventHandling\EventListener:
          public: true
          tags:
              - { name: broadway.domain.event_listener }
```
The `Broadway/EventSourcing/EventSourcingRepository::save` method will store the events in the EventStore and publish all the events in the event bus: 

```php
<?php
...
	public function save(AggregateRoot $aggregate): void
	{
	    // maybe we can get generics one day.... ;)
	    Assert::isInstanceOf($aggregate, $this->aggregateClass);
	    $domainEventStream = $aggregate->getUncommittedEvents();
	    $eventStream = $this->decorateForWrite($aggregate, $domainEventStream);
	    $this->eventStore->append($aggregate->getAggregateRootId(), $eventStream);
	    $this->eventBus->publish($eventStream);
	}
```

The projections are automatically added to the EventBus by the Compiler pass of `broadway-bundle`, [see here](https://github.com/broadway/broadway-bundle/blob/master/src/DependencyInjection/RegisterBusSubscribersCompilerPass.php#L66)
```

## File: `doc/GetStarted/UseCases.md`
```markdown
# Creating a new Use Case

A use case represents an action in the system. These use cases orchestrate the flow of data to and from the entities, and direct those entities to use their enterprise wide business rules to achieve the goals of the use case.
It can be a mutation of the state or a query but not both in a CQRS project.

Let's create a Use Case that just do: `echo "LOOL"`.

### The Command

```php
<?php

declare(strict_types=1);

namespace App\Echo\Application\Command\Log;

use App\Shared\Infrastructure\Bus\Command\CommandInterface;

class EchoCommand implements CommandInterface
{

}
```

### The handler

```php
<?php

declare(strict_types=1);

namespace App\Echo\Application\Command\Log;

use App\Shared\Infrastructure\Bus\Command\CommandHandlerInterface;

class EchoHandler implements CommandHandlerInterface
{
    public function __invoke(EchoCommand $command): void
    {
        echo 'LOOL';
    }
}
```

Now you can use this from UI

### The console command

```php
<?php

declare(strict_types=1);

namespace UI\Cli\Command;

use App\Shared\Infrastructure\Bus\Command\MessengerCommandBus;
use App\Echo\Application\Command\Log\EchoCommand;
use Symfony\Component\Console\Command\Command;
use Symfony\Component\Console\Input\InputInterface;
use Symfony\Component\Console\Output\OutputInterface;

class EchoCli extends Command
{
    protected function configure()
    {
        $this
            ->setName('app:echo')
            ->setDescription('just an echo')
        ;
    }

    protected function execute(InputInterface $input, OutputInterface $output)
    {
        $echoCommand = new EchoCommand();
        $this->commandBus->handle($echoCommand);
    }

    public function __construct(MessengerCommandBus $commandBus)
    {
        parent::__construct();
        $this->commandBus = $commandBus;
    }

    /**
     * @var MessengerCommandBus
     */
    private $commandBus;
}
```

### Let's test it

Enter in the docker container:

`docker-compose exec php sh -l`

Execute:

`./bin/console app:echo`

You should see: `LOOL`

And that's all with 0 config thanks to Symfony 4|5!
```

## File: `doc/GetStarted/Xdebug.md`
```markdown
# Using Xdebug

### Requirements: 

- `docker` 
- `docker-compose`

### Recommendations: 

- When in OSX, due to heavy performance issues with docker4mac I **strongly** recommend [dinghy](https://github.com/codekitchen/dinghy).

## Setup

- Start the project using `make start`. It will start the containers and setup the project. You'll end seeing something like that:

```bash
➜ docker-compose ps        
       Name                      Command               State                                             Ports                                           
---------------------------------------------------------------------------------------------------------------------------------------------------------
api_elasticsearch_1   /usr/local/bin/docker-entr ...   Up      0.0.0.0:9200->9200/tcp, 9300/tcp                                                          
api_kibana_1          /usr/local/bin/kibana-docker     Up      0.0.0.0:5601->5601/tcp                                                                    
api_mysql_1           docker-entrypoint.sh mysqld      Up      0.0.0.0:3306->3306/tcp                                                                    
api_nginx_1           nginx -g daemon off;             Up      443/tcp, 0.0.0.0:80->80/tcp                                                               
api_php_1             /sbin/tini -- supervisord  ...   Up      0.0.0.0:2323->22/tcp, 9000/tcp                                                            
api_rmq_1             docker-entrypoint.sh rabbi ...   Up      15671/tcp, 0.0.0.0:15672->15672/tcp, 25672/tcp, 4369/tcp, 5671/tcp, 0.0.0.0:5672->5672/tcp
api_workers_1         /sbin/tini -- /app/bin/con ...   Up      22/tcp, 9000/tcp  
```
- The php container for development has ssh installed and forwarding the `2323` port. We'll use this to connects to the container as a remote interpreter in our favourite IDE. In PHPStorm, i.e., go to `Languajes & Frameworks > PHP` and configure the connection to have something like:
![debugger](https://i.imgur.com/oTXsPlZ.png)
- Next you'll need to configure phpunit in your IDE to have something like:
![phpunit](https://i.imgur.com/AzFTN9k.png)
- Now you'll be able to run any php test file or phpunit config.
![run test](https://i.imgur.com/PCYXr1U.png) 
```

## File: `etc/artifact/Dockerfile`
```
ARG PHP_VERSION=8.3

FROM jorge07/alpine-php:${PHP_VERSION} AS php-base

# Upgrade PHP to latest patch and install project-specific extensions
RUN apk upgrade --no-cache \
    && apk add --no-cache \
        php83-pdo \
        php83-pdo_mysql \
        php83-simplexml \
        php83-xmlwriter \
        php83-posix \
        php83-fileinfo \
        php83-pecl-amqp

FROM jorge07/alpine-php:${PHP_VERSION}-dev AS php-dev

WORKDIR /app

# Upgrade PHP to latest patch and install project-specific extensions + dev tools
RUN apk upgrade --no-cache \
    && apk add --no-cache \
        php83-pdo \
        php83-pdo_mysql \
        php83-simplexml \
        php83-xmlwriter \
        php83-posix \
        php83-fileinfo \
        php83-pecl-amqp \
        mysql-client

FROM php-dev AS builder

WORKDIR /app

ENV APP_ENV=prod
ENV APP_SECRET=default-secret
# Required by Symfony cache:clear during build
ENV DATABASE_HOST=localhost
ENV DATABASE_PORT=3306
ENV DATABASE_NAME=api
ENV DATABASE_USER=root
ENV DATABASE_PASSWORD=password
ENV DEFAULT_URI=http://localhost

COPY composer.json composer.lock /app

RUN composer install --no-ansi --no-scripts --no-dev --no-interaction --no-progress --optimize-autoloader

COPY bin /app/bin
COPY config /app/config
COPY src /app/src
COPY public /app/public

RUN composer run-script post-install-cmd

FROM php-base AS php

ENV APP_ENV=prod

WORKDIR /app

COPY --from=builder /app /app

FROM nginx:1.27-alpine AS nginx

ENV APP_ENV=prod

WORKDIR /app

COPY etc/artifact/nginx/nginx.conf /etc/nginx/conf.d/default.conf

COPY --from=builder /app/public /app/public
```

## File: `etc/artifact/docker-compose.yml`
```yaml
services:
  php:
    build:
      dockerfile: etc/artifact/Dockerfile
      context: ../..
      target: php
    image: jorge07/cqrs:latest
  nginx:
    build:
      dockerfile: etc/artifact/Dockerfile
      context: ../..
      target: nginx
    image: jorge07/cqrs:nginx-latest
```

## File: `etc/artifact/chart/.helmignore`
```
# Patterns to ignore when building packages.
# This supports shell glob matching, relative path matching, and
# negation (prefixed with !). Only one pattern per line.
.DS_Store
# Common VCS dirs
.git/
.gitignore
.bzr/
.bzrignore
.hg/
.hgignore
.svn/
# Common backup files
*.swp
*.bak
*.tmp
*~
# Various IDEs
.project
.idea/
*.tmproj
.tmpcharts/
```

## File: `etc/artifact/chart/Chart.lock`
```
dependencies:
- name: rabbitmq
  repository: https://charts.bitnami.com/bitnami
  version: 6.25.2
- name: traefik
  repository: https://kubernetes-charts.storage.googleapis.com/
  version: 1.86.2
- name: mysql
  repository: https://kubernetes-charts.storage.googleapis.com/
  version: 1.6.3
- name: elasticsearch
  repository: https://helm.elastic.co
  version: 7.6.2
digest: sha256:4036a27f33dad876c6e4a0628e6d00b8d7746dba9bc406561d4fe399ff769ae6
generated: "2020-05-08T11:19:24.259329+02:00"
```

## File: `etc/artifact/chart/Chart.yaml`
```yaml
apiVersion: v2
appVersion: "1.0"
description: DDD CQRS boilerplate
name: symfony-5-es-cqrs-boilerplate
version: 0.1.0
type: application
dependencies:
  - name: rabbitmq
    version: 6.25.2
    repository: https://charts.bitnami.com/bitnami
    conditions: rabbitmq.selfHosted
  - name: traefik
    version: 28.3.0
    repository: https://traefik.github.io/charts
    conditions: traefik.selfHosted
  - name: mysql
    version: 11.1.17
    repository: https://charts.bitnami.com/bitnami
    conditions: mysql.selfHosted
  - name: elasticsearch
    version: 7.6.2
    repository: https://helm.elastic.co
    conditions: elasticsearch.selfHosted
```

## File: `etc/artifact/chart/values.yaml`
```yaml
replicaCount: 1

autoscaling:
  minReplicas: 1
  maxReplicas: 3
  targetCPUUtilizationPercentage: 85
  targetMemoryUtilizationPercentage: 80

image:
  php:
    repository: jorge07/cqrs
    tag: latest
  nginx:
    repository: jorge07/cqrs
    tag: nginx-latest
  pullPolicy: IfNotPresent

nameOverride: ""
fullnameOverride: ""

service:
  type: ClusterIP
  port: 80

ingress:
  enabled: true
  annotations:
    kubernetes.io/ingress.class: traefik
  path: /
  hosts:
    - demo.minikube.local
  tls: []
  #  - secretName: chart-example-tls
  #    hosts:
  #      - chart-example.local

resources:
  limits:
    cpu: 500m
    memory: 1G
  requests:
    cpu: 250m
    memory: 512Mi

nodeSelector: {}

tolerations: []

affinity: {}

elasticsearch:
  selfHosted: true
  replicas: 1
  antiAffinity: "soft"
  esJavaOpts: "-Xmx128m -Xms128m"
  resources:
    limits:
      memory: 1G
    requests:
      cpu: 250m
      memory: 512Mi

rabbitmq:
  selfHosted: true
  rbacEnabled: true
  rabbitmq:
    username: guest
    password: guest
    erlangCookie: "SWQOKODSQALRPCLNMEQG"

mysql:
  selfHosted: true
  mysqlRootPassword: api
  mysqlUser: api
  mysqlDatabase: api
  imageTag: 8.0.16
  args:
  - --default-authentication-plugin=mysql_native_password

traefik:
  enabled: true
  rbac:
    enabled: true
  dashboard:
    enabled: true
    domain: traefik.local.minikube.com
  serviceType: NodePort

parameters:
  app:
    env: prod
    secret: change_me
  mysql:
    host: cqrs-mysql
    port: 3306
    database: api
    user: root
    pass: api
  rabbit:
    host: "amqp://guest:guest@cqrs-rabbitmq:5672"
  elastic:
    host: "elasticsearch-master:9200"
  jwt:
    hostPath: "/app/config/packages/jwt"
    # REPLACE: Mount your RSA private key via external secret (Vault, sealed-secrets, etc.)
    secretKey: ""
    publicKey: |
      -----BEGIN PUBLIC KEY-----
      MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEArBmtoOEVG2GQ9ttdVxhc
      ZbLPrUADHQv1xVqV5H61mVcgfbtoRGdFUFuHD4DVopuSR2FhXMDRz0ukOTgwODOd
      ri6aG23Dir1oS4VS63OmvCEylS9EbgJkAJMGRM1/pDg61l89Xc7Wab2/Io3
      Q0o39obFVPLnvOSAKng7Ekm3fC8bRH3EvN2eYaFmvcxn97gEtym8x8PXYIICw
      WGRp0Tt62ldNhoWkWiY7c1c4M3A9gIasoNYyxSU7v2ozeMIStWtkDnzhVtYwDf
      3IOVvGxEBAzqYQ9ICI2eUQjf8edcbTIpkI4wBJ1Iz1wi9WJDc5OP/RMrcKPyO2p
      WeHuGbhasevkBeJi1fGClhjb/FwswGeEpcIVN59dafsPJ6U2Oj/RQJQQydEgnNfl
      rxCd/yIl3/Mo0gORL7j2WBPND5k/kVeEFAAA5S6KvwDfvVCJ7ka8IuAsZd5QZCC
      OzhpRjCT4JgBa9lJS/ShGguE3/0A0JnqpaqbBu3qMzRktnVqjTW0htjnmsCB8UH
      JTqqSKRUAygJ9MbxQo252xEgS0VHLDHA79ONiOVRZczbVtVjvZLLIVmeJYXTSc
      dq97Dy43xmYSsRL74Xgvf4LGoEgBEVDBg1ELonDoFwdVJwVqUgRk7awf8ZT
      gZV/5L0JJAEb4srJ9VrDntkCAwEAAQ==
      -----END PUBLIC KEY-----
    # REPLACE: Set JWT passphrase via external secret
    passphrase: ""
    ttl: 3600
```

## File: `etc/artifact/chart/config/mysql.url`
```
mysql://{{ $.Values.parameters.mysql.user }}:{{ $.Values.parameters.mysql.pass }}@{{ $.Values.parameters.mysql.host }}:{{ $.Values.parameters.mysql.port }}/{{ $.Values.parameters.mysql.database }}?serverVersion=8.0
```

## File: `etc/artifact/chart/config/parameters.yaml`
```yaml
- name: APP_ENV
  value: {{ .Values.parameters.app.env | quote }}
- name: APP_SECRET
  valueFrom:
    secretKeyRef:
      name: {{ $.Chart.Name }}-secret
      key: secret
{{- if $.Values.parameters.app.proxy }}
- name: TRUSTED_PROXIES
  value: {{ $.Values.parameters.app.proxy | quote }}
{{- end }}
{{- if $.Values.parameters.app.hosts }}
- name: TRUSTED_HOSTS
  value: {{ $.Values.parameters.app.hosts | quote }}
  {{- end }}
- name: MESSENGER_TRANSPORT_DSN
  valueFrom:
    secretKeyRef:
      name: {{ $.Chart.Name }}-rabbitmq
      key: host
- name: DATABASE_URL
  valueFrom:
    secretKeyRef:
      name: {{ $.Chart.Name }}-mysql
      key: url
- name: JWT_SECRET_KEY
  value: {{ $.Values.parameters.jwt.hostPath }}/private.pem
- name: JWT_PUBLIC_KEY
  value: {{ $.Values.parameters.jwt.hostPath }}/public.pem
- name: JWT_PASSPHRASE
  valueFrom:
    secretKeyRef:
      name: {{ $.Chart.Name }}-jwt
      key: passphrase
- name: JWT_TTL
  value: {{ $.Values.parameters.jwt.ttl | quote }}
- name: ELASTIC_HOST
  value: {{- if $.Values.elasticsearch.selfHosted }} {{ template "elasticHost" . }} {{- else }} {{ $.Values.parameters.elastic.host | quote }} {{- end }}
```

## File: `etc/artifact/chart/templates/NOTES.txt`
```
1. Get the application URL by running these commands:
{{- if .Values.ingress.enabled }}
{{- range .Values.ingress.hosts }}
  http{{ if $.Values.ingress.tls }}s{{ end }}://{{ . }}{{ $.Values.ingress.path }}
{{- end }}
{{- else if contains "NodePort" .Values.service.type }}
  export NODE_PORT=$(kubectl get --namespace {{ .Release.Namespace }} -o jsonpath="{.spec.ports[0].nodePort}" services {{ include "chart.fullname" . }})
  export NODE_IP=$(kubectl get nodes --namespace {{ .Release.Namespace }} -o jsonpath="{.items[0].status.addresses[0].address}")
  echo http://$NODE_IP:$NODE_PORT
{{- else if contains "LoadBalancer" .Values.service.type }}
     NOTE: It may take a few minutes for the LoadBalancer IP to be available.
           You can watch the status of by running 'kubectl get svc -w {{ include "chart.fullname" . }}'
  export SERVICE_IP=$(kubectl get svc --namespace {{ .Release.Namespace }} {{ include "chart.fullname" . }} -o jsonpath='{.status.loadBalancer.ingress[0].ip}')
  echo http://$SERVICE_IP:{{ .Values.service.port }}
{{- else if contains "ClusterIP" .Values.service.type }}
  export POD_NAME=$(kubectl get pods --namespace {{ .Release.Namespace }} -l "app={{ include "chart.name" . }},release={{ .Release.Name }}" -o jsonpath="{.items[0].metadata.name}")
  echo "Visit http://127.0.0.1:8080 to use your application"
  kubectl port-forward $POD_NAME 8080:80
{{- end }}
```

## File: `etc/artifact/chart/templates/_helpers.tpl`
```
{{/* vim: set filetype=mustache: */}}
{{/*
Expand the name of the chart.
*/}}
{{- define "chart.name" -}}
{{- default .Chart.Name .Values.nameOverride | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{/*
Create a default fully qualified app name.
We truncate at 63 chars because some Kubernetes name fields are limited to this (by the DNS naming spec).
If release name contains chart name it will be used as a full name.
*/}}
{{- define "chart.fullname" -}}
{{- if .Values.fullnameOverride -}}
{{- .Values.fullnameOverride | trunc 63 | trimSuffix "-" -}}
{{- else -}}
{{- $name := default .Chart.Name .Values.nameOverride -}}
{{- if contains $name .Release.Name -}}
{{- .Release.Name | trunc 63 | trimSuffix "-" -}}
{{- else -}}
{{- printf "%s-%s" .Release.Name $name | trunc 63 | trimSuffix "-" -}}
{{- end -}}
{{- end -}}
{{- end -}}

{{/*
Create chart name and version as used by the chart label.
*/}}
{{- define "chart.chart" -}}
{{- printf "%s-%s" .Chart.Name .Chart.Version | replace "+" "_" | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{/*
Rabbitmq self hosted hostname
*/}}
{{- define "rabbitHost" -}}
{{- printf "amqp://%s:%s@%s-rabbitmq:5672" .Values.rabbitmq.rabbitmq.username .Values.rabbitmq.rabbitmq.password .Chart.Name | b64enc | quote -}}
{{- end -}}

{{/*
MySQL self hosted hostname
*/}}
{{- define "mysqlHost" -}}
{{- printf "%s-mysql" .Chart.Name | b64enc | quote -}}
{{- end -}}

{{/*
Elastic self hosted hostname
*/}}
{{- define "elasticHost" -}}
{{- printf "%s-elasticsearch-client:9200" .Chart.Name }}
{{- end -}}
```

## File: `etc/artifact/chart/templates/deployment-worker.yaml`
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: {{ include "chart.fullname" . }}-workers
  labels:
    app: {{ include "chart.name" . }}-workers
    chart: {{ include "chart.chart" . }}
    release: {{ .Release.Name }}
    heritage: {{ .Release.Service }}
  annotations:
    checksum/secrets-rmq: {{ include (print $.Template.BasePath "/secrets/rabbitmq.yaml") . | sha256sum }}
    checksum/secrets-app: {{ include (print $.Template.BasePath "/secrets/app-secret.yaml") . | sha256sum }}
    checksum/secrets-jwt: {{ include (print $.Template.BasePath "/secrets/jwt.yaml") . | sha256sum }}
    checksum/secrets-mysql: {{ include (print $.Template.BasePath "/secrets/mysql.yaml") . | sha256sum }}
spec:
  replicas: {{ .Values.replicaCount }}
  selector:
    matchLabels:
      app: {{ include "chart.name" . }}-workers
      release: {{ .Release.Name }}
  template:
    metadata:
      labels:
        app: {{ include "chart.name" . }}-workers
        release: {{ .Release.Name }}
    spec:
      volumes:
      - name: jwt
        secret:
          secretName: {{ .Chart.Name }}-jwt
      containers:
        - name: {{ .Chart.Name }}
          image: "{{ .Values.image.php.repository }}:{{ .Values.image.php.tag }}"
          command: [ '/app/bin/console', 'messenger:consume', 'events', '-vv' ]
          imagePullPolicy: {{ .Values.image.pullPolicy }}
          volumeMounts:
          - name: jwt
            mountPath: {{ .Values.parameters.jwt.hostPath }}
            readOnly: true
          env:
{{ tpl (.Files.Get "config/parameters.yaml") . | indent 12 }}
          ports:
            - name: fast-cgi
              containerPort: 9000
              protocol: TCP
          resources:
{{ toYaml .Values.resources | indent 12 }}
    {{- with .Values.nodeSelector }}
      nodeSelector:
{{ toYaml . | indent 8 }}
    {{- end }}
    {{- with .Values.affinity }}
      affinity:
{{ toYaml . | indent 8 }}
    {{- end }}
    {{- with .Values.tolerations }}
      tolerations:
{{ toYaml . | indent 8 }}
    {{- end }}
```

## File: `etc/artifact/chart/templates/deployment.yaml`
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: {{ include "chart.fullname" . }}
  labels:
    app: {{ include "chart.name" . }}
    chart: {{ include "chart.chart" . }}
    release: {{ .Release.Name }}
    heritage: {{ .Release.Service }}
  annotations:
    checksum/secrets-rmq: {{ include (print $.Template.BasePath "/secrets/rabbitmq.yaml") . | sha256sum }}
    checksum/secrets-app: {{ include (print $.Template.BasePath "/secrets/app-secret.yaml") . | sha256sum }}
    checksum/secrets-jwt: {{ include (print $.Template.BasePath "/secrets/jwt.yaml") . | sha256sum }}
    checksum/secrets-mysql: {{ include (print $.Template.BasePath "/secrets/mysql.yaml") . | sha256sum }}
spec:
  replicas: {{ .Values.replicaCount }}
  selector:
    matchLabels:
      app: {{ include "chart.name" . }}
      release: {{ .Release.Name }}
  template:
    metadata:
      labels:
        app: {{ include "chart.name" . }}
        release: {{ .Release.Name }}
    spec:
      volumes:
      - name: jwt
        secret:
          secretName: {{ .Chart.Name }}-jwt
      containers:
        - name: {{ .Chart.Name }}
          image: "{{ .Values.image.php.repository }}:{{ .Values.image.php.tag }}"
          imagePullPolicy: {{ .Values.image.pullPolicy }}
          volumeMounts:
          - name: jwt
            mountPath: {{ .Values.parameters.jwt.hostPath }}
            readOnly: true
          env:
{{ tpl (.Files.Get "config/parameters.yaml") . | indent 12 }}
          ports:
            - name: fast-cgi
              containerPort: 9000
              protocol: TCP
        - name: {{ .Chart.Name }}-nginx
          image: "{{ .Values.image.nginx.repository }}:{{ .Values.image.nginx.tag }}"
          imagePullPolicy: {{ .Values.image.pullPolicy }}
          ports:
          - name: http
            containerPort: 80
            protocol: TCP
          livenessProbe:
            httpGet:
              path: /api/healthz
              port: http
          readinessProbe:
            httpGet:
              path: /api/healthz
              port: http
          resources:
{{ toYaml .Values.resources | indent 12 }}
    {{- with .Values.nodeSelector }}
      nodeSelector:
{{ toYaml . | indent 8 }}
    {{- end }}
    {{- with .Values.affinity }}
      affinity:
{{ toYaml . | indent 8 }}
    {{- end }}
    {{- with .Values.tolerations }}
      tolerations:
{{ toYaml . | indent 8 }}
    {{- end }}
```

## File: `etc/artifact/chart/templates/hpa.yaml`
```yaml
{{- if .Values.autoscaling }}
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: {{ .Release.Name }}
  labels:
    app: {{ include "chart.name" . }}
    chart: {{ include "chart.chart" . }}
    release: {{ .Release.Name }}
    heritage: {{ .Release.Service }}
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: {{ .Release.Name }}
  minReplicas: {{ .Values.autoscaling.minReplicas }}
  maxReplicas: {{ .Values.autoscaling.maxReplicas }}
  metrics:
    - type: Resource
      resource:
        name: cpu
        target:
          type: Utilization
          averageUtilization: {{ .Values.autoscaling.targetCPUUtilizationPercentage }}
{{- end }}
```

## File: `etc/artifact/chart/templates/ingress.yaml`
```yaml
{{- if .Values.ingress.enabled -}}
{{- $fullName := include "chart.fullname" . -}}
{{- $ingressPath := .Values.ingress.path -}}
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: {{ $fullName }}
  labels:
    app: {{ include "chart.name" . }}
    chart: {{ include "chart.chart" . }}
    release: {{ .Release.Name }}
    heritage: {{ .Release.Service }}
{{- with .Values.ingress.annotations }}
  annotations:
{{ toYaml . | indent 4 }}
{{- end }}
spec:
{{- if .Values.ingress.tls }}
  tls:
  {{- range .Values.ingress.tls }}
    - hosts:
      {{- range .hosts }}
        - {{ . | quote }}
      {{- end }}
      secretName: {{ .secretName }}
  {{- end }}
{{- end }}
  rules:
  {{- range .Values.ingress.hosts }}
    - host: {{ . | quote }}
      http:
        paths:
          - path: {{ $ingressPath }}
            pathType: Prefix
            backend:
              service:
                name: {{ $fullName }}
                port:
                  name: http
  {{- end }}
{{- end }}
```

## File: `etc/artifact/chart/templates/migrations.yaml`
```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: {{ include "chart.fullname" . }}-migrations-{{ date "20060102150405" .Release.Time }}
  labels:
    app: {{ include "chart.name" . }}-migrations
    chart: {{ include "chart.chart" . }}
    release: {{ .Release.Name }}
    heritage: {{ .Release.Service }}
    app.kubernetes.io/component: init-migrations
  annotations:
    checksum/secrets-rmq: {{ include (print $.Template.BasePath "/secrets/rabbitmq.yaml") . | sha256sum }}
    checksum/secrets-app: {{ include (print $.Template.BasePath "/secrets/app-secret.yaml") . | sha256sum }}
    checksum/secrets-jwt: {{ include (print $.Template.BasePath "/secrets/jwt.yaml") . | sha256sum }}
    checksum/secrets-mysql: {{ include (print $.Template.BasePath "/secrets/mysql.yaml") . | sha256sum }}
    helm.sh/hook: "post-install,pre-upgrade"
    helm.sh/hook-weight: "-5"
    helm.sh/hook-delete-policy: hook-succeeded
spec:
  activeDeadlineSeconds: 120
  template:
    metadata:
      labels:
        app: {{ include "chart.name" . }}-migrations
        release: {{ .Release.Name }}
    spec:
      restartPolicy: Never
      volumes:
      - name: jwt
        secret:
          secretName: {{ .Chart.Name }}-jwt
      containers:
        - name: {{ .Chart.Name }}
          image: "{{ .Values.image.php.repository }}:{{ .Values.image.php.tag }}"
          command: [ '/app/bin/console', 'd:migrations:migrate', '-n' ]
          imagePullPolicy: {{ .Values.image.pullPolicy }}
          volumeMounts:
          - name: jwt
            mountPath: {{ .Values.parameters.jwt.hostPath }}
            readOnly: true
          env:
{{ tpl (.Files.Get "config/parameters.yaml") . | indent 12 }}
          resources:
{{ toYaml .Values.resources | indent 12 }}
    {{- with .Values.nodeSelector }}
      nodeSelector:
{{ toYaml . | indent 8 }}
    {{- end }}
    {{- with .Values.affinity }}
      affinity:
{{ toYaml . | indent 8 }}
    {{- end }}
    {{- with .Values.tolerations }}
      tolerations:
{{ toYaml . | indent 8 }}
    {{- end }}
```

## File: `etc/artifact/chart/templates/service.yaml`
```yaml
apiVersion: v1
kind: Service
metadata:
  name: {{ include "chart.fullname" . }}
  labels:
    app: {{ include "chart.name" . }}
    chart: {{ include "chart.chart" . }}
    release: {{ .Release.Name }}
    heritage: {{ .Release.Service }}
spec:
  type: {{ .Values.service.type }}
  ports:
    - port: {{ .Values.service.port }}
      targetPort: http
      protocol: TCP
      name: http
  selector:
    app: {{ include "chart.name" . }}
    release: {{ .Release.Name }}
```

## File: `etc/artifact/chart/templates/secrets/app-secret.yaml`
```yaml
apiVersion: v1
kind: Secret
metadata:
  name: {{ .Chart.Name }}-secret
  labels:
    app: {{ include "chart.name" . }}
    chart: {{ include "chart.chart" . }}
    release: {{ .Release.Name }}
    heritage: {{ .Release.Service }}
type: Opaque
data:
  secret: {{ .Values.parameters.app.secret | b64enc | quote }}
```

## File: `etc/artifact/chart/templates/secrets/jwt.yaml`
```yaml
apiVersion: v1
kind: Secret
metadata:
  name: {{ .Chart.Name }}-jwt
  labels:
    app: {{ include "chart.name" . }}
    chart: {{ include "chart.chart" . }}
    release: {{ .Release.Name }}
    heritage: {{ .Release.Service }}
type: Opaque
data:
  private.pem: {{ .Values.parameters.jwt.secretKey | b64enc | quote }}
  public.pem: {{ .Values.parameters.jwt.publicKey | b64enc | quote }}
  passphrase: {{ .Values.parameters.jwt.passphrase | b64enc | quote }}
```

## File: `etc/artifact/chart/templates/secrets/mysql.yaml`
```yaml
apiVersion: v1
kind: Secret
metadata:
  name: {{ .Chart.Name }}-mysql
  labels:
    app: {{ include "chart.name" . }}
    chart: {{ include "chart.chart" . }}
    release: {{ .Release.Name }}
    heritage: {{ .Release.Service }}
type: Opaque
data:
  url:  {{ tpl (.Files.Get "config/mysql.url") . | b64enc }}
```

## File: `etc/artifact/chart/templates/secrets/rabbitmq.yaml`
```yaml
apiVersion: v1
kind: Secret
metadata:
  name: {{ .Chart.Name }}-rabbitmq
  labels:
    app: {{ include "chart.name" . }}
    chart: {{ include "chart.chart" . }}
    release: {{ .Release.Name }}
    heritage: {{ .Release.Service }}
type: Opaque
data:
  host: {{ .Values.parameters.rabbit.host | b64enc | quote }}
```

## File: `etc/artifact/nginx/nginx.conf`
```
server {
    root /app/public;

    client_max_body_size 10m;

    add_header X-Frame-Options "SAMEORIGIN" always;
    add_header X-Content-Type-Options "nosniff" always;
    add_header X-XSS-Protection "1; mode=block" always;
    add_header Referrer-Policy "strict-origin-when-cross-origin" always;

    location / {
        try_files $uri /index.php$is_args$args;
    }

    location ~ ^/index\.php(/|$) {
        fastcgi_pass 127.0.0.1:9000;
        fastcgi_split_path_info ^(.+\.php)(/.*)$;
        include fastcgi_params;
        fastcgi_param  SCRIPT_FILENAME  $realpath_root$fastcgi_script_name;
        fastcgi_param DOCUMENT_ROOT $realpath_root;
    }
}
```

## File: `etc/ci/docker-compose.yml`
```yaml
# CI docker-compose override (empty, uses base config)
```

## File: `etc/ci/mysql/custom.cnf`
```
[mysqld]
  bind-address             = 0.0.0.0

  innodb_flush_log_at_trx_commit = 2
  innodb_lock_wait_timeout = 50

  max_connect_errors       = 1000000
  max_connections          = 900

  character-set-server           = utf8mb4
  collation-server               = utf8mb4_unicode_ci
  sql_mode                       = "STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION"
  innodb                         = FORCE
  default-storage-engine         = InnoDB
  max_allowed_packet             = 256M
```

## File: `etc/dev/docker-compose.windows.yml`
```yaml
services:

  php:
    environment:
      XDEBUG_CONFIG: remote_connect_back=0 remote_host=host.docker.internal remote_port=9000
```

## File: `etc/dev/docker-compose.yml`
```yaml
services:

  nginx:
    ports:
      - "80:80"

  php:
    ports:
      - "2323:22"
#      - "9003:9003"
    # Allows to debug php script run inside PHP container
    environment:
      PHP_IDE_CONFIG: serverName=es.local

  mysql:
    ports:
      - "3306:3306"

  rmq:
    ports:
      - "15672:15672"
      - "5672:5672"

  kibana:
    image: docker.elastic.co/kibana/kibana:7.11.0
    ports:
      - 5601:5601
    volumes:
      - "./etc/dev/kibana/config:/usr/share/kibana/config/kibana.yml"

  elasticsearch:
    ports:
      - "9200:9200"
```

## File: `etc/dev/kibana/config`
```
---
## Default Kibana configuration from kibana-docker.
## from https://github.com/elastic/kibana/blob/master/config/kibana.yml
#
server.name: kibana
server.host: "0"
elasticsearch.hosts: http://elasticsearch:9200
```

## File: `etc/dev/nginx/nginx.conf`
```
server {
    server_name es.local;

    root /app/public;

    client_max_body_size 10m;

    add_header X-Frame-Options "SAMEORIGIN" always;
    add_header X-Content-Type-Options "nosniff" always;
    add_header X-XSS-Protection "1; mode=block" always;
    add_header Referrer-Policy "strict-origin-when-cross-origin" always;

    location / {
        # try to serve file directly, fallback to index.php
        try_files $uri /index.php$is_args$args;
    }

    location ~ ^/index\.php(/|$) {
        fastcgi_pass php:9000;
        fastcgi_index index.php;
        fastcgi_split_path_info ^(.+\.php)(/.*)$;
        include fastcgi_params;
        fastcgi_param SCRIPT_FILENAME $realpath_root$fastcgi_script_name;
        fastcgi_param DOCUMENT_ROOT $realpath_root;
        fastcgi_param PATH_INFO $fastcgi_path_info;
    }
}
```

## File: `etc/prod/docker-compose.windows.yml`
```yaml
services:

  php:
    environment:
      XDEBUG_CONFIG: remote_connect_back=0 remote_host=host.docker.internal remote_port=9000
```

## File: `etc/prod/docker-compose.yml`
```yaml
services:

  nginx:
    ports:
      - "80:80"

  php:
    ports:
      - "2323:22"
    # Allows to debug php script run inside PHP container
    environment:
      PHP_IDE_CONFIG: serverName=es.local
      # Prod mode doesn't load .env file, remember to add here your new required env vars!
      APP_ENV: "prod"
      APP_DEBUG: 0
      APP_SECRET: ${APP_SECRET}
      JWT_SECRET_KEY: '%kernel.project_dir%/config/packages/jwt/private.pem'
      JWT_PUBLIC_KEY: '%kernel.project_dir%/config/packages/jwt/public.pem'
      JWT_PASSPHRASE: ${JWT_PASSPHRASE}
      JWT_TTL: 604800
      MESSENGER_TRANSPORT_DSN: ${MESSENGER_TRANSPORT_DSN}

  workers:
    environment:
      PHP_IDE_CONFIG: serverName=es.local
      APP_ENV: "prod"
      APP_DEBUG: 0
      APP_SECRET: ${APP_SECRET}
      JWT_SECRET_KEY: '%kernel.project_dir%/config/packages/jwt/private.pem'
      JWT_PUBLIC_KEY: '%kernel.project_dir%/config/packages/jwt/public.pem'
      JWT_PASSPHRASE: ${JWT_PASSPHRASE}
      JWT_TTL: 604800
      MESSENGER_TRANSPORT_DSN: ${MESSENGER_TRANSPORT_DSN}

  mysql:
    ports:
      - "3306:3306"

  rmq:
    ports:
      - "15672:15672"
      - "5672:5672"

  kibana:
    image: docker.elastic.co/kibana/kibana:7.17.24
    ports:
      - 5601:5601
    volumes:
      - "./etc/dev/kibana/config:/usr/share/kibana/config/kibana.yml"

  elasticsearch:
    ports:
      - "9200:9200"

volumes:
  db_data:
```

## File: `etc/prod/kibana/config`
```
---
## Default Kibana configuration from kibana-docker.
## from https://github.com/elastic/kibana/blob/master/config/kibana.yml
#
server.name: kibana
server.host: "0"
elasticsearch.hosts: http://elasticsearch:9200
```

## File: `etc/prod/nginx/nginx.conf`
```
server {
    server_name es.local;

    root /app/public;

    client_max_body_size 10m;

    add_header X-Frame-Options "SAMEORIGIN" always;
    add_header X-Content-Type-Options "nosniff" always;
    add_header X-XSS-Protection "1; mode=block" always;
    add_header Referrer-Policy "strict-origin-when-cross-origin" always;

    location / {
        # try to serve file directly, fallback to index.php
        try_files $uri /index.php$is_args$args;
    }

    location ~ ^/index\.php(/|$) {
        fastcgi_pass php:9000;
        fastcgi_index index.php;
        fastcgi_split_path_info ^(.+\.php)(/.*)$;
        include fastcgi_params;
        fastcgi_param SCRIPT_FILENAME $realpath_root$fastcgi_script_name;
        fastcgi_param DOCUMENT_ROOT $realpath_root;
        fastcgi_param PATH_INFO $fastcgi_path_info;
    }
}
```

## File: `public/index.php`
```php
<?php

declare(strict_types=1);

use App\Shared\Infrastructure\Kernel;
use Symfony\Component\Dotenv\Dotenv;
use Symfony\Component\ErrorHandler\Debug;
use Symfony\Component\HttpFoundation\Request;

require __DIR__ . '/../vendor/autoload.php';

// The check is to ensure we don't use .env in production
if (!isset($_SERVER['APP_ENV'])) {
    if (!class_exists(Dotenv::class)) {
        throw new \RuntimeException('APP_ENV environment variable is not defined. You need to define environment variables for configuration or add "symfony/dotenv" as a Composer dependency to load variables from a .env file.');
    }
    (new Dotenv())->load(__DIR__ . '/../.env');
}

$debug = (bool) ($_SERVER['APP_DEBUG'] ?? ('prod' !== ($_SERVER['APP_ENV'] ?? 'dev')));

if ($debug) {
    Debug::enable();
}

if ($trustedProxies = $_SERVER['TRUSTED_PROXIES'] ?? false) {
    Request::setTrustedProxies(explode(',', (string) $trustedProxies), Request::HEADER_X_FORWARDED_ALL ^ Request::HEADER_X_FORWARDED_HOST);
}

if ($trustedHosts = $_SERVER['TRUSTED_HOSTS'] ?? false) {
    Request::setTrustedHosts(explode(',', (string) $trustedHosts));
}

$kernel = new Kernel($_SERVER['APP_ENV'] ?? 'dev', $debug);
$request = Request::createFromGlobals();
$response = $kernel->handle($request);
$response->send();
$kernel->terminate($request, $response);
```

## File: `src/App/Shared/Application/Command/CommandBusInterface.php`
```php
<?php

declare(strict_types=1);

namespace App\Shared\Application\Command;

interface CommandBusInterface
{
    public function handle(CommandInterface $command): void;
}
```

## File: `src/App/Shared/Application/Command/CommandHandlerInterface.php`
```php
<?php

declare(strict_types=1);

namespace App\Shared\Application\Command;

interface CommandHandlerInterface
{
}
```

## File: `src/App/Shared/Application/Command/CommandInterface.php`
```php
<?php

declare(strict_types=1);

namespace App\Shared\Application\Command;

interface CommandInterface
{
}
```

## File: `src/App/Shared/Application/Query/Collection.php`
```php
<?php

declare(strict_types=1);

namespace App\Shared\Application\Query;

use App\Shared\Domain\Exception\NotFoundException;

class Collection
{
    /**
     * @throws NotFoundException
     */
    public function __construct(
        public readonly int $page,
        public readonly int $limit,
        public readonly int $total,
        public readonly array $data)
    {
        $this->exists($page, $limit, $total);
    }

    /**
     * @throws NotFoundException
     */
    private function exists(int $page, int $limit, int $total): void
    {
        if (($limit * ($page - 1)) >= $total) {
            throw new NotFoundException();
        }
    }
}
```

## File: `src/App/Shared/Application/Query/Item.php`
```php
<?php

declare(strict_types=1);

namespace App\Shared\Application\Query;

use Broadway\ReadModel\SerializableReadModel;

final class Item
{
    private function __construct(
        public readonly string $id,
        public readonly string $type,
        public readonly array $resource,
        public readonly array $relationships = []
    )
    {
    }

    private static function type(SerializableReadModel $model): string
    {
        $path = \explode('\\', $model::class);

        return \array_pop($path);
    }

    public static function fromSerializable(SerializableReadModel $serializableReadModel, array $relations = []): self
    {
        return new self(
            $serializableReadModel->getId(),
            self::type($serializableReadModel),
            $serializableReadModel->serialize(),
            $relations
        );
    }

    public static function fromPayload(string $id, string $type, array $payload, array $relations = []): self
    {
        return new self(
            $id,
            $type,
            $payload,
            $relations
        );
    }
}
```

## File: `src/App/Shared/Application/Query/QueryBusInterface.php`
```php
<?php

declare(strict_types=1);

namespace App\Shared\Application\Query;

interface QueryBusInterface
{
    public function ask(QueryInterface $query): mixed;
}
```

## File: `src/App/Shared/Application/Query/QueryHandlerInterface.php`
```php
<?php

declare(strict_types=1);

namespace App\Shared\Application\Query;

interface QueryHandlerInterface
{
}
```

## File: `src/App/Shared/Application/Query/QueryInterface.php`
```php
<?php

declare(strict_types=1);

namespace App\Shared\Application\Query;

interface QueryInterface
{
}
```

## File: `src/App/Shared/Application/Query/Event/GetEvents/GetEventsHandler.php`
```php
<?php

declare(strict_types=1);

namespace App\Shared\Application\Query\Event\GetEvents;

use App\Shared\Application\Query\Collection;
use App\Shared\Application\Query\QueryHandlerInterface;
use App\Shared\Domain\Exception\NotFoundException;
use App\Shared\Domain\Repository\EventRepositoryInterface;
use Assert\AssertionFailedException;

final class GetEventsHandler implements QueryHandlerInterface
{
    public function __construct(private readonly EventRepositoryInterface $eventRepository)
    {
    }

    /**
     * @throws AssertionFailedException
     * @throws NotFoundException
     */
    public function __invoke(GetEventsQuery $query): Collection
    {
        $result = $this->eventRepository->page($query->page, $query->limit);

        return new Collection($query->page, $query->limit, $result['total']['value'], $result['data']);
    }
}
```

## File: `src/App/Shared/Application/Query/Event/GetEvents/GetEventsQuery.php`
```php
<?php

declare(strict_types=1);

namespace App\Shared\Application\Query\Event\GetEvents;

use App\Shared\Application\Query\QueryInterface;

final class GetEventsQuery implements QueryInterface
{
    public function __construct(
        public readonly int $page = 1,
        public readonly int $limit = 50
    )
    {
    }
}
```

## File: `src/App/Shared/Domain/Exception/DateTimeException.php`
```php
<?php

declare(strict_types=1);

namespace App\Shared\Domain\Exception;

class DateTimeException extends \Exception
{
    public function __construct(\Exception $e)
    {
        parent::__construct('Datetime Malformed or not valid', 500, $e);
    }
}
```

## File: `src/App/Shared/Domain/Exception/DomainException.php`
```php
<?php

declare(strict_types=1);

namespace App\Shared\Domain\Exception;

abstract class DomainException extends \Exception
{
}
```

## File: `src/App/Shared/Domain/Exception/NotFoundException.php`
```php
<?php

declare(strict_types=1);

namespace App\Shared\Domain\Exception;

class NotFoundException extends \Exception
{
    public function __construct()
    {
        parent::__construct('Resource not found');
    }
}
```

## File: `src/App/Shared/Domain/Repository/EventRepositoryInterface.php`
```php
<?php

declare(strict_types=1);

namespace App\Shared\Domain\Repository;

interface EventRepositoryInterface
{
    public function page(int $page = 1, int $limit = 50): array;
}
```

## File: `src/App/Shared/Domain/ValueObject/DateTime.php`
```php
<?php

declare(strict_types=1);

namespace App\Shared\Domain\ValueObject;

use App\Shared\Domain\Exception\DateTimeException;
use DateTimeImmutable;
use Exception;
use Throwable;

/** @psalm-immutable */
final class DateTime extends DateTimeImmutable
{
    public const FORMAT = 'Y-m-d\TH:i:s.uP';

    /**
     * @throws DateTimeException
     */
    public static function now(): self
    {
        return self::create();
    }

    /**
     * @throws DateTimeException
     */
    public static function fromString(string $dateTime): self
    {
        return self::create($dateTime);
    }

    /**
     * @throws DateTimeException
     */
    private static function create(string $dateTime = ''): self
    {
        try {
            return new self($dateTime);
        } catch (Throwable $e) {
            throw new DateTimeException(new Exception($e->getMessage(), (int) $e->getCode(), $e));
        }
    }

    public function toString(): string
    {
        return $this->format(self::FORMAT);
    }
}
```

## File: `src/App/Shared/Infrastructure/Kernel.php`
```php
<?php

declare(strict_types=1);

namespace App\Shared\Infrastructure;

use Symfony\Bundle\FrameworkBundle\Kernel\MicroKernelTrait;
use Symfony\Component\HttpKernel\Kernel as BaseKernel;

class Kernel extends BaseKernel
{
    use MicroKernelTrait;

    public function getCacheDir(): string
    {
        return $this->getProjectDir() . '/var/cache/' . $this->environment;
    }

    public function getLogDir(): string
    {
        return $this->getProjectDir() . '/var/log';
    }

    public function registerBundles(): iterable
    {
        $contents = require $this->getProjectDir() . '/config/bundles.php';
        foreach ($contents as $class => $envs) {
            if (isset($envs['all']) || isset($envs[$this->environment])) {
                yield new $class();
            }
        }
    }
}
```

## File: `src/App/Shared/Infrastructure/Bus/MessageBusExceptionTrait.php`
```php
<?php

declare(strict_types=1);

namespace App\Shared\Infrastructure\Bus;

use Symfony\Component\Messenger\Exception\HandlerFailedException;
use Throwable;

trait MessageBusExceptionTrait
{
    /**
     * @throws Throwable
     */
    public function throwException(HandlerFailedException $exception): never
    {
        while ($exception instanceof HandlerFailedException) {
            /** @var Throwable $exception */
            $exception = $exception->getPrevious();
        }

        throw $exception;
    }
}
```

## File: `src/App/Shared/Infrastructure/Bus/AsyncEvent/AsyncEventHandlerInterface.php`
```php
<?php

declare(strict_types=1);

namespace App\Shared\Infrastructure\Bus\AsyncEvent;

interface AsyncEventHandlerInterface
{
}
```

## File: `src/App/Shared/Infrastructure/Bus/AsyncEvent/MessengerAsyncEventBus.php`
```php
<?php

declare(strict_types=1);

namespace App\Shared\Infrastructure\Bus\AsyncEvent;

use App\Shared\Infrastructure\Bus\MessageBusExceptionTrait;
use Broadway\Domain\DomainMessage;
use Symfony\Component\Messenger\Bridge\Amqp\Transport\AmqpStamp;
use Symfony\Component\Messenger\Exception\HandlerFailedException;
use Symfony\Component\Messenger\MessageBusInterface;
use Throwable;

final class MessengerAsyncEventBus
{
    use MessageBusExceptionTrait;

    public function __construct(private readonly MessageBusInterface $messageBus)
    {
    }

    /**
     * @throws Throwable
     */
    public function handle(DomainMessage $command): void
    {
        try {
            $this->messageBus->dispatch($command, [
                new AmqpStamp($command->getType()),
            ]);
        } catch (HandlerFailedException $error) {
            $this->throwException($error);
        }
    }
}
```

## File: `src/App/Shared/Infrastructure/Bus/Command/MessengerCommandBus.php`
```php
<?php

declare(strict_types=1);

namespace App\Shared\Infrastructure\Bus\Command;

use App\Shared\Application\Command\CommandBusInterface;
use App\Shared\Application\Command\CommandInterface;
use App\Shared\Infrastructure\Bus\MessageBusExceptionTrait;
use Symfony\Component\Messenger\Exception\HandlerFailedException;
use Symfony\Component\Messenger\MessageBusInterface;
use Throwable;

final class MessengerCommandBus implements CommandBusInterface
{
    use MessageBusExceptionTrait;

    public function __construct(private readonly MessageBusInterface $messageBus)
    {
    }

    /**
     * @throws Throwable
     */
    public function handle(CommandInterface $command): void
    {
        try {
            $this->messageBus->dispatch($command);
        } catch (HandlerFailedException $e) {
            $this->throwException($e);
        }
    }
}
```

## File: `src/App/Shared/Infrastructure/Bus/Query/MessengerQueryBus.php`
```php
<?php

declare(strict_types=1);

namespace App\Shared\Infrastructure\Bus\Query;

use App\Shared\Application\Query\Collection;
use App\Shared\Application\Query\Item;
use App\Shared\Application\Query\QueryBusInterface;
use App\Shared\Application\Query\QueryInterface;
use App\Shared\Infrastructure\Bus\MessageBusExceptionTrait;
use Symfony\Component\Messenger\Exception\HandlerFailedException;
use Symfony\Component\Messenger\MessageBusInterface;
use Symfony\Component\Messenger\Stamp\HandledStamp;
use Throwable;

final class MessengerQueryBus implements QueryBusInterface
{
    use MessageBusExceptionTrait;

    public function __construct(private readonly MessageBusInterface $messageBus)
    {
    }

    /**
     * @throws Throwable
     */
    public function ask(QueryInterface $query): mixed
    {
        try {
            $envelope = $this->messageBus->dispatch($query);

            /** @var HandledStamp $stamp */
            $stamp = $envelope->last(HandledStamp::class);

            return $stamp->getResult();
        } catch (HandlerFailedException $e) {
            $this->throwException($e);
        }
    }
}
```

## File: `src/App/Shared/Infrastructure/Event/Consumer/SendEventsToElasticConsumer.php`
```php
<?php

declare(strict_types=1);

namespace App\Shared\Infrastructure\Event\Consumer;

use App\Shared\Infrastructure\Event\ReadModel\ElasticSearchEventRepository;
use Broadway\Domain\DomainMessage;
use Symfony\Component\Messenger\Attribute\AsMessageHandler;

#[AsMessageHandler(bus: 'messenger.bus.event.async', fromTransport: 'events', priority: 10)]
class SendEventsToElasticConsumer
{
    public function __construct(private readonly ElasticSearchEventRepository $eventElasticRepository)
    {
    }

    public function __invoke(DomainMessage $event): void
    {
        $this->eventElasticRepository->store($event);
    }
}
```

## File: `src/App/Shared/Infrastructure/Event/Publisher/AsyncEventPublisher.php`
```php
<?php

declare(strict_types=1);

namespace App\Shared\Infrastructure\Event\Publisher;

use App\Shared\Infrastructure\Bus\AsyncEvent\MessengerAsyncEventBus;
use Broadway\Domain\DomainMessage;
use Broadway\EventHandling\EventListener;
use Symfony\Component\Console\ConsoleEvents;
use Symfony\Component\EventDispatcher\EventSubscriberInterface;
use Symfony\Component\HttpKernel\KernelEvents;
use Throwable;

final class AsyncEventPublisher implements EventSubscriberInterface, EventListener
{
    /** @var DomainMessage[] */
    private array $messages = [];

    public function __construct(private readonly MessengerAsyncEventBus $bus)
    {
    }

    public function handle(DomainMessage $domainMessage): void
    {
        $this->messages[] = $domainMessage;
    }

    public static function getSubscribedEvents(): array
    {
        return [
            KernelEvents::TERMINATE => 'publish',
            ConsoleEvents::TERMINATE => 'publish',
        ];
    }

    /**
     * @throws Throwable
     */
    public function publish(): void
    {
        if (empty($this->messages)) {
            return;
        }

        foreach ($this->messages as $message) {
            $this->bus->handle($message);
        }
    }
}
```

## File: `src/App/Shared/Infrastructure/Event/ReadModel/ElasticSearchEventRepository.php`
```php
<?php

declare(strict_types=1);

namespace App\Shared\Infrastructure\Event\ReadModel;

use App\Shared\Domain\Repository\EventRepositoryInterface;
use App\Shared\Infrastructure\Persistence\ReadModel\Repository\ElasticSearchRepository;
use Broadway\Domain\DomainMessage;

final class ElasticSearchEventRepository extends ElasticSearchRepository implements EventRepositoryInterface
{
    private const INDEX = 'events';

    protected function index(): string
    {
        return self::INDEX;
    }

    public function store(DomainMessage $message): void
    {
        $document = [
            'type' => $message->getType(),
            'payload' => $message->getPayload()->serialize(),
            'occurred_on' => $message->getRecordedOn()->toString(),
        ];

        $this->add($document);
    }
}
```

## File: `src/App/Shared/Infrastructure/Persistence/Doctrine/Migrations/Version20180102233829.php`
```php
<?php

declare(strict_types=1);

namespace App\Shared\Infrastructure\Persistence\Doctrine\Migrations;

use App\Shared\Infrastructure\Persistence\Doctrine\MigrationsFactory\ServiceAwareMigrationInterface;
use Broadway\EventStore\Dbal\DBALEventStore;
use Doctrine\DBAL\Schema\Schema;
use Doctrine\Migrations\AbstractMigration;
use Doctrine\ORM\EntityManagerInterface;

/**
 * @psalm-suppress PropertyNotSetInConstructor
 */
class Version20180102233829 extends AbstractMigration implements ServiceAwareMigrationInterface
{
    private EntityManagerInterface $em;

    private DBALEventStore $eventStore;

    public function setServices(EntityManagerInterface $em, DBALEventStore $eventStore): void
    {
        $this->em = $em;
        $this->eventStore = $eventStore;
    }

    public function up(Schema $schema): void
    {
        $this->eventStore->configureSchema($schema);

        $this->em->flush();
    }

    public function down(Schema $schema): void
    {
        $schema->dropTable('api.events');

        $this->em->flush();
    }

    public function isTransactional(): bool
    {
        return false;
    }
}
```

## File: `src/App/Shared/Infrastructure/Persistence/Doctrine/Migrations/Version20200727170306.php`
```php
<?php

declare(strict_types=1);

namespace App\Shared\Infrastructure\Persistence\Doctrine\Migrations;

use Doctrine\DBAL\Platforms\MySQL80Platform;
use Doctrine\DBAL\Schema\Schema;
use Doctrine\Migrations\AbstractMigration;

/**
 * Auto-generated Migration: Please modify to your needs!
 */
final class Version20200727170306 extends AbstractMigration
{
    public function getDescription(): string
    {
        return '';
    }

    public function up(Schema $schema): void
    {
        // this up() migration is auto-generated, please modify it to your needs
        $this->abortIf(get_class($this->connection->getDatabasePlatform()) !== MySQL80Platform::class, 'Migration can only be executed safely on \'mysql\'.');

        $this->addSql('CREATE TABLE users (uuid BINARY(16) NOT NULL COMMENT \'(DC2Type:uuid_binary)\', created_at DATETIME NOT NULL COMMENT \'(DC2Type:datetime_immutable)\', updated_at DATETIME DEFAULT NULL COMMENT \'(DC2Type:datetime_immutable)\', credentials_email VARCHAR(255) NOT NULL COMMENT \'(DC2Type:email)\', credentials_password VARCHAR(255) NOT NULL COMMENT \'(DC2Type:hashed_password)\', UNIQUE INDEX UNIQ_1483A5E9299C9369 (credentials_email), PRIMARY KEY(uuid)) DEFAULT CHARACTER SET utf8mb4 COLLATE `utf8mb4_unicode_ci` ENGINE = InnoDB');
    }

    public function down(Schema $schema): void
    {
        // this down() migration is auto-generated, please modify it to your needs
        $this->abortIf(get_class($this->connection->getDatabasePlatform()) !== MySQL80Platform::class, 'Migration can only be executed safely on \'mysql\'.');

        $this->addSql('DROP TABLE users');
    }

    /**
     * https://github.com/doctrine/migrations/issues/1104
     */
    public function isTransactional(): bool
    {
        return false;
    }
}
```

## File: `src/App/Shared/Infrastructure/Persistence/Doctrine/MigrationsFactory/ContainerAwareFactory.php`
```php
<?php

declare(strict_types=1);

namespace App\Shared\Infrastructure\Persistence\Doctrine\MigrationsFactory;

use Broadway\EventStore\Dbal\DBALEventStore;
use Doctrine\DBAL\Connection;
use Doctrine\Migrations\AbstractMigration;
use Doctrine\Migrations\Version\MigrationFactory;
use Doctrine\ORM\EntityManagerInterface;
use Psr\Log\LoggerInterface;

/**
 * Custom migration factory that injects services into migrations that need them.
 * This replaces the deprecated ContainerAwareInterface pattern.
 */
final class ContainerAwareFactory implements MigrationFactory
{
    public function __construct(
        private readonly Connection $connection,
        private readonly LoggerInterface $logger,
        private readonly EntityManagerInterface $entityManager,
        private readonly DBALEventStore $eventStore,
    ) {
    }

    public function createVersion(string $migrationClassName): AbstractMigration
    {
        $instance = new $migrationClassName(
            $this->connection,
            $this->logger
        );

        if ($instance instanceof ServiceAwareMigrationInterface) {
            $instance->setServices($this->entityManager, $this->eventStore);
        }

        return $instance;
    }
}
```

## File: `src/App/Shared/Infrastructure/Persistence/Doctrine/MigrationsFactory/ServiceAwareMigrationInterface.php`
```php
<?php

declare(strict_types=1);

namespace App\Shared\Infrastructure\Persistence\Doctrine\MigrationsFactory;

use Broadway\EventStore\Dbal\DBALEventStore;
use Doctrine\ORM\EntityManagerInterface;

/**
 * Interface for migrations that need access to services.
 * This replaces the deprecated ContainerAwareInterface pattern from Symfony 6.x.
 */
interface ServiceAwareMigrationInterface
{
    public function setServices(EntityManagerInterface $em, DBALEventStore $eventStore): void;
}
```

## File: `src/App/Shared/Infrastructure/Persistence/Doctrine/Types/DateTimeType.php`
```php
<?php

declare(strict_types=1);

namespace App\Shared\Infrastructure\Persistence\Doctrine\Types;

use App\Shared\Domain\Exception\DateTimeException;
use App\Shared\Domain\ValueObject\DateTime;
use DateTimeImmutable;
use Doctrine\DBAL\Platforms\AbstractPlatform;
use Doctrine\DBAL\Types\ConversionException;
use Doctrine\DBAL\Types\DateTimeImmutableType;

class DateTimeType extends DateTimeImmutableType
{
    /**
     * {@inheritdoc}
     *
     * @throws \Throwable
     */
    public function getSQLDeclaration(array $column, AbstractPlatform $platform): string
    {
        return $platform->getDateTimeTypeDeclarationSQL($column);
    }

    /**
     * {@inheritdoc}
     *
     * @throws ConversionException
     *
     * @param T $value
     *
     * @return (T is null ? null : string)
     *
     * @template T
     **/
    public function convertToDatabaseValue(mixed $value, AbstractPlatform $platform): ?string
    {
        if (null === $value) {
            return null;
        }

        if ($value instanceof DateTime) {
            return $value->format($platform->getDateTimeFormatString());
        }

        if ($value instanceof DateTimeImmutable) {
            return $value->format($platform->getDateTimeFormatString());
        }

        throw ConversionException::conversionFailedInvalidType($value, $this->getName(), ['null', DateTime::class]);
    }

    /**
     * {@inheritdoc}
     *
     * @throws ConversionException
     *
     * @param T $value
     *
     * @return (T is null ? null : DateTimeImmutable)
     *
     * @template T
     */
    public function convertToPHPValue(mixed $value, AbstractPlatform $platform): ?DateTimeImmutable
    {
        if (null === $value || $value instanceof DateTime) {
            return $value;
        }

        try {
            $dateTime = DateTime::fromString($value);
        } catch (DateTimeException) {
            throw ConversionException::conversionFailedFormat($value, $this->getName(), $platform->getDateTimeFormatString());
        }

        return $dateTime;
    }
}
```

## File: `src/App/Shared/Infrastructure/Persistence/ReadModel/Exception/NotFoundException.php`
```php
<?php

declare(strict_types=1);

namespace App\Shared\Infrastructure\Persistence\ReadModel\Exception;

use App\Shared\Domain\Exception\NotFoundException as DomainNotFoundException;

/**
 * @deprecated Use App\Shared\Domain\Exception\NotFoundException instead.
 */
final class NotFoundException extends DomainNotFoundException
{
}
```

## File: `src/App/Shared/Infrastructure/Persistence/ReadModel/Repository/ElasticSearchRepository.php`
```php
<?php

declare(strict_types=1);

namespace App\Shared\Infrastructure\Persistence\ReadModel\Repository;

use Assert\Assertion;
use Assert\AssertionFailedException;
use Elasticsearch\Client;
use Elasticsearch\ClientBuilder;
use Psr\Log\LoggerInterface;

abstract class ElasticSearchRepository
{
    private readonly Client $client;

    public function __construct(array $elasticConfig, ?LoggerInterface $elasticsearchLogger = null)
    {
        $defaultConfig = [];

        if ($elasticsearchLogger) {
            $defaultConfig['logger'] = $elasticsearchLogger;
            $defaultConfig['tracer'] = $elasticsearchLogger;
        }

        $this->client = ClientBuilder::fromConfig(\array_replace($defaultConfig, $elasticConfig), true);
    }

    abstract protected function index(): string;

    public function search(array $query): array
    {
        $finalQuery = [];

        $finalQuery['index'] = $this->index();
        $finalQuery['body'] = $query;

        return $this->client->search($finalQuery);
    }

    public function refresh(): void
    {
        if ($this->client->indices()->exists(['index' => $this->index()])) {
            $this->client->indices()->refresh(['index' => $this->index()]);
        }
    }

    public function delete(): void
    {
        if ($this->client->indices()->exists(['index' => $this->index()])) {
            $this->client->indices()->delete(['index' => $this->index()]);
        }
    }

    public function reboot(): void
    {
        $this->delete();
        $this->boot();
    }

    public function boot(): void
    {
        if (!$this->client->indices()->exists(['index' => $this->index()])) {
            $this->client->indices()->create(['index' => $this->index()]);
        }
    }

    protected function add(array $document): array
    {
        $query = [];

        $query['index'] = $this->index();
        $query['id'] = $document['id'] ?? null;
        $query['body'] = $document;

        return $this->client->index($query);
    }

    /**
     * @throws AssertionFailedException
     */
    public function page(int $page = 1, int $limit = 50): array
    {
        Assertion::greaterThan($page, 0, 'Pagination need to be > 0');

        $query = [];

        $query['index'] = $this->index();
        $query['from'] = ($page - 1) * $limit;
        $query['size'] = $limit;

        $response = $this->client->search($query);

        return [
            'data' => \array_column($response['hits']['hits'], '_source'),
            'total' => $response['hits']['total'],
        ];
    }

    public function isHealthy(): bool
    {
        try {
            $response = $this->client->cluster()->health();

            return $response['status'] !== 'red';
        } catch (\Throwable) {
            return false;
        }
    }
}
```

## File: `src/App/Shared/Infrastructure/Persistence/ReadModel/Repository/MysqlRepository.php`
```php
<?php

declare(strict_types=1);

namespace App\Shared\Infrastructure\Persistence\ReadModel\Repository;

use App\Shared\Domain\Exception\NotFoundException;
use Doctrine\ORM\AbstractQuery;
use Doctrine\ORM\EntityManagerInterface;
use Doctrine\ORM\EntityRepository;
use Doctrine\ORM\NonUniqueResultException;
use Doctrine\ORM\QueryBuilder;
use Throwable;

abstract class MysqlRepository
{
    protected EntityRepository $repository;

    public function __construct(protected EntityManagerInterface $entityManager)
    {
        $this->setEntityManager();
    }

    /**
     * @important Hold on
     * I don't like this neither but I'm facing this and I don't know how to fix it:
     * docker-compose -f docker-compose.yml -f etc/dev/docker-compose.yml run --rm code sh -lc './vendor/bin/phpstan analyse -l 6 -c phpstan.neon src tests'
        116/116 [▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓] 100%

        ------ -------------------------------------------------------------------------------------------------------------
        Line   src/Infrastructure/Shared/Persistence/ReadModel/Repository/MysqlRepository.php
        ------ -------------------------------------------------------------------------------------------------------------
        25     Unable to resolve the template type T in call to method Doctrine\Persistence\ObjectManager::getRepository()
        ------ -------------------------------------------------------------------------------------------------------------


        [ERROR] Found 1 error
     *
     * If you know how to solve this let me know please and I'll owe you a beer
     */
    abstract protected function setEntityManager(): void;

    public function register(object $model): void
    {
        $this->entityManager->persist($model);
        $this->apply();
    }

    public function apply(): void
    {
        $this->entityManager->flush();
    }

    /**
     * @throws NotFoundException
     * @throws NonUniqueResultException
     */
    protected function oneOrException(QueryBuilder $queryBuilder, mixed $hydration = AbstractQuery::HYDRATE_OBJECT): mixed
    {
        $model = $queryBuilder
            ->getQuery()
            ->getOneOrNullResult($hydration)
        ;

        if (null === $model) {
            throw new NotFoundException();
        }

        return $model;
    }

    public function isHealthy(): bool
    {
        $connection = $this->entityManager->getConnection();

        try {
            $dummySelectSQL = $connection->getDatabasePlatform()->getDummySelectSQL();
            $connection->executeQuery($dummySelectSQL);

            return true;
        } catch (Throwable) {
            $connection->close();

            return false;
        }
    }
}
```

## File: `src/App/User/Application/Command/ChangeEmail/ChangeEmailCommand.php`
```php
<?php

declare(strict_types=1);

namespace App\User\Application\Command\ChangeEmail;

use App\Shared\Application\Command\CommandInterface;
use App\User\Domain\ValueObject\Email;
use Assert\AssertionFailedException;
use Ramsey\Uuid\Uuid;
use Ramsey\Uuid\UuidInterface;

final class ChangeEmailCommand implements CommandInterface
{
    public readonly UuidInterface $userUuid;

    public readonly Email $email;

    /**
     * @throws AssertionFailedException
     */
    public function __construct(string $userUuid, string $email)
    {
        $this->userUuid = Uuid::fromString($userUuid);
        $this->email = Email::fromString($email);
    }
}
```

## File: `src/App/User/Application/Command/ChangeEmail/ChangeEmailHandler.php`
```php
<?php

declare(strict_types=1);

namespace App\User\Application\Command\ChangeEmail;

use App\Shared\Application\Command\CommandHandlerInterface;
use App\User\Domain\Repository\UserRepositoryInterface;
use App\User\Domain\Specification\UniqueEmailSpecificationInterface;

final class ChangeEmailHandler implements CommandHandlerInterface
{
    public function __construct(private readonly UserRepositoryInterface $userRepository, private readonly UniqueEmailSpecificationInterface $uniqueEmailSpecification)
    {
    }

    public function __invoke(ChangeEmailCommand $command): void
    {
        $user = $this->userRepository->get($command->userUuid);

        $user->changeEmail($command->email, $this->uniqueEmailSpecification);

        $this->userRepository->store($user);
    }
}
```

## File: `src/App/User/Application/Command/SignIn/SignInCommand.php`
```php
<?php

declare(strict_types=1);

namespace App\User\Application\Command\SignIn;

use App\Shared\Application\Command\CommandInterface;
use App\User\Domain\ValueObject\Email;
use Assert\AssertionFailedException;

final class SignInCommand implements CommandInterface
{
    public readonly Email $email;

    /**
     * @throws AssertionFailedException
     */
    public function __construct(string $email, public readonly string $plainPassword)
    {
        $this->email = Email::fromString($email);
    }
}
```

## File: `src/App/User/Application/Command/SignIn/SignInHandler.php`
```php
<?php

declare(strict_types=1);

namespace App\User\Application\Command\SignIn;

use App\Shared\Application\Command\CommandHandlerInterface;
use App\User\Domain\Exception\InvalidCredentialsException;
use App\User\Domain\Repository\CheckUserByEmailInterface;
use App\User\Domain\Repository\UserRepositoryInterface;
use App\User\Domain\ValueObject\Email;
use Ramsey\Uuid\UuidInterface;

final class SignInHandler implements CommandHandlerInterface
{
    public function __construct(private readonly UserRepositoryInterface $userStore, private readonly CheckUserByEmailInterface $userCollection)
    {
    }

    public function __invoke(SignInCommand $command): void
    {
        $uuid = $this->uuidFromEmail($command->email);

        $user = $this->userStore->get($uuid);

        $user->signIn($command->plainPassword);

        $this->userStore->store($user);
    }

    private function uuidFromEmail(Email $email): UuidInterface
    {
        $uuid = $this->userCollection->findUuidByEmail($email);

        if (null === $uuid) {
            throw new InvalidCredentialsException();
        }

        return $uuid;
    }
}
```

## File: `src/App/User/Application/Command/SignUp/SignUpCommand.php`
```php
<?php

declare(strict_types=1);

namespace App\User\Application\Command\SignUp;

use App\Shared\Application\Command\CommandInterface;
use Ramsey\Uuid\Uuid;
use Ramsey\Uuid\UuidInterface;

final class SignUpCommand implements CommandInterface
{
    public readonly UuidInterface $uuid;

    public function __construct(string $uuid, public readonly string $email, public readonly string $plainPassword)
    {
        $this->uuid = Uuid::fromString($uuid);
    }
}
```

## File: `src/App/User/Application/Command/SignUp/SignUpHandler.php`
```php
<?php

declare(strict_types=1);

namespace App\User\Application\Command\SignUp;

use App\Shared\Application\Command\CommandHandlerInterface;
use App\Shared\Domain\Exception\DateTimeException;
use App\User\Domain\Repository\UserRepositoryInterface;
use App\User\Domain\Specification\UniqueEmailSpecificationInterface;
use App\User\Domain\User;
use App\User\Domain\ValueObject\Auth\Credentials;
use App\User\Domain\ValueObject\Auth\HashedPassword;
use App\User\Domain\ValueObject\Email;

final class SignUpHandler implements CommandHandlerInterface
{
    public function __construct(private readonly UserRepositoryInterface $userRepository, private readonly UniqueEmailSpecificationInterface $uniqueEmailSpecification)
    {
    }

    /**
     * @throws DateTimeException
     */
    public function __invoke(SignUpCommand $command): void
    {
        $credentials = new Credentials(
            Email::fromString($command->email),
            HashedPassword::encode($command->plainPassword),
        );

        $user = User::create($command->uuid, $credentials, $this->uniqueEmailSpecification);

        $this->userRepository->store($user);
    }
}
```

## File: `src/App/User/Application/Query/Auth/AuthenticationProviderInterface.php`
```php
<?php

declare(strict_types=1);

namespace App\User\Application\Query\Auth;

use App\User\Domain\ValueObject\Auth\HashedPassword;
use App\User\Domain\ValueObject\Email;
use Ramsey\Uuid\UuidInterface;

interface AuthenticationProviderInterface
{
    public function generateToken(UuidInterface $uuid, Email $email, HashedPassword $hashedPassword): string;
}
```

## File: `src/App/User/Application/Query/Auth/GetAuthUserByEmail/GetAuthUserByEmailHandler.php`
```php
<?php

declare(strict_types=1);

namespace App\User\Application\Query\Auth\GetAuthUserByEmail;

use App\Shared\Application\Query\QueryHandlerInterface;
use App\User\Domain\Repository\GetUserCredentialsByEmailInterface;
use App\User\Infrastructure\Auth\Auth;

final class GetAuthUserByEmailHandler implements QueryHandlerInterface
{
    public function __construct(private readonly GetUserCredentialsByEmailInterface $userCredentialsByEmail)
    {
    }

    public function __invoke(GetAuthUserByEmailQuery $query): Auth
    {
        $credentials = $this->userCredentialsByEmail->getCredentialsByEmail($query->email);

        return Auth::create($credentials->uuid, $credentials->email, $credentials->password);
    }
}
```

## File: `src/App/User/Application/Query/Auth/GetAuthUserByEmail/GetAuthUserByEmailQuery.php`
```php
<?php

declare(strict_types=1);

namespace App\User\Application\Query\Auth\GetAuthUserByEmail;

use App\Shared\Application\Query\QueryInterface;
use App\User\Domain\ValueObject\Email;
use Assert\AssertionFailedException;

final class GetAuthUserByEmailQuery implements QueryInterface
{
    public readonly Email $email;

    /**
     * @throws AssertionFailedException
     */
    public function __construct(string $email)
    {
        $this->email = Email::fromString($email);
    }
}
```

## File: `src/App/User/Application/Query/Auth/GetToken/GetTokenHandler.php`
```php
<?php

declare(strict_types=1);

namespace App\User\Application\Query\Auth\GetToken;

use App\Shared\Application\Query\QueryHandlerInterface;
use App\User\Application\Query\Auth\AuthenticationProviderInterface;
use App\User\Domain\Repository\GetUserCredentialsByEmailInterface;

final class GetTokenHandler implements QueryHandlerInterface
{
    public function __construct(private readonly GetUserCredentialsByEmailInterface $userCredentialsByEmail, private readonly AuthenticationProviderInterface $authenticationProvider)
    {
    }

    public function __invoke(GetTokenQuery $query): string
    {
        $credentials = $this->userCredentialsByEmail->getCredentialsByEmail($query->email);

        return $this->authenticationProvider->generateToken($credentials->uuid, $credentials->email, $credentials->password);
    }
}
```

## File: `src/App/User/Application/Query/Auth/GetToken/GetTokenQuery.php`
```php
<?php

declare(strict_types=1);

namespace App\User\Application\Query\Auth\GetToken;

use App\Shared\Application\Query\QueryInterface;
use App\User\Domain\ValueObject\Email;
use Assert\AssertionFailedException;

final class GetTokenQuery implements QueryInterface
{
    public readonly Email $email;

    /**
     * @throws AssertionFailedException
     */
    public function __construct(string $email)
    {
        $this->email = Email::fromString($email);
    }
}
```

## File: `src/App/User/Application/Query/User/FindByEmail/FindByEmailHandler.php`
```php
<?php

declare(strict_types=1);

namespace App\User\Application\Query\User\FindByEmail;

use App\Shared\Application\Query\Item;
use App\Shared\Application\Query\QueryHandlerInterface;
use App\Shared\Domain\Exception\NotFoundException;
use App\User\Domain\Repository\UserReadModelRepositoryInterface;
use App\User\Infrastructure\ReadModel\UserView;
use Doctrine\ORM\NonUniqueResultException;

final class FindByEmailHandler implements QueryHandlerInterface
{
    public function __construct(private readonly UserReadModelRepositoryInterface $repository)
    {
    }

    /**
     * @throws NotFoundException
     * @throws NonUniqueResultException
     */
    public function __invoke(FindByEmailQuery $query): Item
    {
        $userView = $this->repository->oneByEmailAsArray($query->email);

        return Item::fromPayload($userView['uuid']->toString(), UserView::TYPE, $userView);
    }
}
```

## File: `src/App/User/Application/Query/User/FindByEmail/FindByEmailQuery.php`
```php
<?php

declare(strict_types=1);

namespace App\User\Application\Query\User\FindByEmail;

use App\Shared\Application\Query\QueryInterface;
use App\User\Domain\ValueObject\Email;
use Assert\AssertionFailedException;

final class FindByEmailQuery implements QueryInterface
{
    public readonly Email $email;

    /**
     * @throws AssertionFailedException
     */
    public function __construct(string $email)
    {
        $this->email = Email::fromString($email);
    }
}
```

## File: `src/App/User/Domain/User.php`
```php
<?php

declare(strict_types=1);

namespace App\User\Domain;

use App\Shared\Domain\Exception\DateTimeException;
use App\Shared\Domain\ValueObject\DateTime;
use App\User\Domain\Event\UserEmailChanged;
use App\User\Domain\Event\UserSignedIn;
use App\User\Domain\Event\UserWasCreated;
use App\User\Domain\Exception\InvalidCredentialsException;
use App\User\Domain\Specification\UniqueEmailSpecificationInterface;
use App\User\Domain\ValueObject\Auth\Credentials;
use App\User\Domain\ValueObject\Auth\HashedPassword;
use App\User\Domain\ValueObject\Email;
use Assert\Assertion;
use Assert\AssertionFailedException;
use Broadway\EventSourcing\EventSourcedAggregateRoot;
use Ramsey\Uuid\UuidInterface;

/**
 * @psalm-suppress MissingConstructor
 */
class User extends EventSourcedAggregateRoot
{
    private UuidInterface $uuid;

    private Email $email;

    private HashedPassword $hashedPassword;

    private ?DateTime $createdAt = null;

    private ?DateTime $updatedAt = null;

    /**
     * @throws DateTimeException
     */
    public static function create(
        UuidInterface $uuid,
        Credentials $credentials,
        UniqueEmailSpecificationInterface $uniqueEmailSpecification
    ): self {
        $uniqueEmailSpecification->isUnique($credentials->email);

        $user = new self();

        $user->apply(new UserWasCreated($uuid, $credentials, DateTime::now()));

        return $user;
    }

    /**
     * @throws DateTimeException
     */
    public function changeEmail(
        Email $email,
        UniqueEmailSpecificationInterface $uniqueEmailSpecification
    ): void {
        $uniqueEmailSpecification->isUnique($email);
        $this->apply(new UserEmailChanged($this->uuid, $email, DateTime::now()));
    }

    /**
     * @throws InvalidCredentialsException
     */
    public function signIn(string $plainPassword): void
    {
        if (!$this->hashedPassword->match($plainPassword)) {
            throw new InvalidCredentialsException('Invalid credentials entered.');
        }

        $this->apply(new UserSignedIn($this->uuid, $this->email));
    }

    protected function applyUserWasCreated(UserWasCreated $event): void
    {
        $this->uuid = $event->uuid;

        $this->setEmail($event->credentials->email);
        $this->setHashedPassword($event->credentials->password);
        $this->setCreatedAt($event->createdAt);
    }

    /**
     * Event is recorded for audit/tracking purposes; no aggregate state change needed.
     */
    protected function applyUserSignedIn(UserSignedIn $event): void
    {
    }

    /**
     * @throws AssertionFailedException
     */
    protected function applyUserEmailChanged(UserEmailChanged $event): void
    {
        Assertion::notEq($this->email->toString(), $event->email->toString(), 'New email should be different');

        $this->setEmail($event->email);
        $this->setUpdatedAt($event->updatedAt);
    }

    private function setEmail(Email $email): void
    {
        $this->email = $email;
    }

    private function setHashedPassword(HashedPassword $hashedPassword): void
    {
        $this->hashedPassword = $hashedPassword;
    }

    private function setCreatedAt(DateTime $createdAt): void
    {
        $this->createdAt = $createdAt;
    }

    private function setUpdatedAt(DateTime $updatedAt): void
    {
        $this->updatedAt = $updatedAt;
    }

    public function createdAt(): DateTime
    {
        return $this->createdAt;
    }

    public function updatedAt(): ?DateTime
    {
        return $this->updatedAt;
    }

    public function email(): Email
    {
        return $this->email;
    }

    public function uuid(): UuidInterface
    {
        return $this->uuid;
    }

    public function getAggregateRootId(): string
    {
        return $this->uuid->toString();
    }
}
```

## File: `src/App/User/Domain/Event/UserEmailChanged.php`
```php
<?php

declare(strict_types=1);

namespace App\User\Domain\Event;

use App\Shared\Domain\Exception\DateTimeException;
use App\Shared\Domain\ValueObject\DateTime;
use App\User\Domain\ValueObject\Email;
use Assert\Assertion;
use Assert\AssertionFailedException;
use Broadway\Serializer\Serializable;
use Ramsey\Uuid\Uuid;
use Ramsey\Uuid\UuidInterface;

final class UserEmailChanged implements Serializable
{
    public function __construct(public readonly UuidInterface $uuid, public readonly Email $email, public readonly DateTime $updatedAt)
    {
    }

    /**
     * @throws AssertionFailedException
     * @throws DateTimeException
     */
    public static function deserialize(array $data): self
    {
        Assertion::keyExists($data, 'uuid');
        Assertion::keyExists($data, 'email');

        return new self(
            Uuid::fromString($data['uuid']),
            Email::fromString($data['email']),
            DateTime::fromString($data['updated_at'])
        );
    }

    public function serialize(): array
    {
        return [
            'uuid' => $this->uuid->toString(),
            'email' => $this->email->toString(),
            'updated_at' => $this->updatedAt->toString(),
        ];
    }
}
```

## File: `src/App/User/Domain/Event/UserSignedIn.php`
```php
<?php

declare(strict_types=1);

namespace App\User\Domain\Event;

use App\User\Domain\ValueObject\Email;
use Assert\Assertion;
use Assert\AssertionFailedException;
use Broadway\Serializer\Serializable;
use Ramsey\Uuid\Uuid;
use Ramsey\Uuid\UuidInterface;

final class UserSignedIn implements Serializable
{
    public function __construct(public readonly UuidInterface $uuid, public readonly Email $email)
    {
    }

    /**
     * @throws AssertionFailedException
     */
    public static function deserialize(array $data): self
    {
        Assertion::keyExists($data, 'uuid');
        Assertion::keyExists($data, 'email');

        return new self(
            Uuid::fromString($data['uuid']),
            Email::fromString($data['email'])
        );
    }

    public function serialize(): array
    {
        return [
            'uuid' => $this->uuid->toString(),
            'email' => $this->email->toString(),
        ];
    }
}
```

## File: `src/App/User/Domain/Event/UserWasCreated.php`
```php
<?php

declare(strict_types=1);

namespace App\User\Domain\Event;

use App\Shared\Domain\Exception\DateTimeException;
use App\Shared\Domain\ValueObject\DateTime;
use App\User\Domain\ValueObject\Auth\Credentials;
use App\User\Domain\ValueObject\Auth\HashedPassword;
use App\User\Domain\ValueObject\Email;
use Assert\Assertion;
use Assert\AssertionFailedException;
use Broadway\Serializer\Serializable;
use Ramsey\Uuid\Uuid;
use Ramsey\Uuid\UuidInterface;

final class UserWasCreated implements Serializable
{
    public function __construct(public readonly UuidInterface $uuid, public readonly Credentials $credentials, public readonly DateTime $createdAt)
    {
    }

    /**
     * @throws DateTimeException
     * @throws AssertionFailedException
     */
    public static function deserialize(array $data): self
    {
        Assertion::keyExists($data, 'uuid');
        Assertion::keyExists($data, 'credentials');

        return new self(
            Uuid::fromString($data['uuid']),
            new Credentials(
                Email::fromString($data['credentials']['email']),
                HashedPassword::fromHash($data['credentials']['password'])
            ),
            DateTime::fromString($data['created_at'])
        );
    }

    public function serialize(): array
    {
        return [
            'uuid' => $this->uuid->toString(),
            'credentials' => [
                'email' => $this->credentials->email->toString(),
                'password' => $this->credentials->password->toString(),
            ],
            'created_at' => $this->createdAt->toString(),
        ];
    }
}
```

## File: `src/App/User/Domain/Exception/EmailAlreadyExistException.php`
```php
<?php

declare(strict_types=1);

namespace App\User\Domain\Exception;

use App\Shared\Domain\Exception\DomainException;

class EmailAlreadyExistException extends DomainException
{
    public function __construct()
    {
        parent::__construct('Email already registered.');
    }
}
```

## File: `src/App/User/Domain/Exception/ForbiddenException.php`
```php
<?php

declare(strict_types=1);

namespace App\User\Domain\Exception;

use App\Shared\Domain\Exception\DomainException;

class ForbiddenException extends DomainException
{
}
```

## File: `src/App/User/Domain/Exception/InvalidCredentialsException.php`
```php
<?php

declare(strict_types=1);

namespace App\User\Domain\Exception;

use App\Shared\Domain\Exception\DomainException;

class InvalidCredentialsException extends DomainException
{
}
```

## File: `src/App/User/Domain/Repository/CheckUserByEmailInterface.php`
```php
<?php

declare(strict_types=1);

namespace App\User\Domain\Repository;

use App\User\Domain\ValueObject\Email;
use Ramsey\Uuid\UuidInterface;

interface CheckUserByEmailInterface
{
    public function findUuidByEmail(Email $email): ?UuidInterface;
}
```

## File: `src/App/User/Domain/Repository/GetUserCredentialsByEmailInterface.php`
```php
<?php

declare(strict_types=1);

namespace App\User\Domain\Repository;

use App\User\Domain\ValueObject\Auth\UserCredentials;
use App\User\Domain\ValueObject\Email;

interface GetUserCredentialsByEmailInterface
{
    public function getCredentialsByEmail(Email $email): UserCredentials;
}
```

## File: `src/App/User/Domain/Repository/UserReadModelRepositoryInterface.php`
```php
<?php

declare(strict_types=1);

namespace App\User\Domain\Repository;

use App\User\Domain\ValueObject\Email;
use Ramsey\Uuid\UuidInterface;

interface UserReadModelRepositoryInterface
{
    public function oneByUuid(UuidInterface $uuid): mixed;

    public function oneByEmail(Email $email): mixed;

    public function oneByEmailAsArray(Email $email): array;
}
```

## File: `src/App/User/Domain/Repository/UserRepositoryInterface.php`
```php
<?php

declare(strict_types=1);

namespace App\User\Domain\Repository;

use App\User\Domain\User;
use Ramsey\Uuid\UuidInterface;

interface UserRepositoryInterface
{
    public function get(UuidInterface $uuid): User;

    public function store(User $user): void;
}
```

## File: `src/App/User/Domain/Specification/UniqueEmailSpecificationInterface.php`
```php
<?php

declare(strict_types=1);

namespace App\User\Domain\Specification;

use App\User\Domain\Exception\EmailAlreadyExistException;
use App\User\Domain\ValueObject\Email;

interface UniqueEmailSpecificationInterface
{
    /**
     * @throws EmailAlreadyExistException
     */
    public function isUnique(Email $email): bool;
}
```

## File: `src/App/User/Domain/ValueObject/Email.php`
```php
<?php

declare(strict_types=1);

namespace App\User\Domain\ValueObject;

use Assert\Assertion;
use Assert\AssertionFailedException;
use JsonSerializable;

final class Email implements JsonSerializable, \Stringable
{
    private function __construct(private readonly string $email)
    {
    }

    /**
     * @throws AssertionFailedException
     */
    public static function fromString(string $email): self
    {
        Assertion::email($email, 'Not a valid email');

        return new self($email);
    }

    public function toString(): string
    {
        return $this->email;
    }

    public function __toString(): string
    {
        return $this->email;
    }

    public function equals(self $other): bool
    {
        return $this->email === $other->email;
    }

    public function jsonSerialize(): string
    {
        return $this->toString();
    }
}
```

## File: `src/App/User/Domain/ValueObject/Auth/Credentials.php`
```php
<?php

declare(strict_types=1);

namespace App\User\Domain\ValueObject\Auth;

use App\User\Domain\ValueObject\Email;

final class Credentials
{
    public function __construct(
        public readonly Email $email,
        public readonly HashedPassword $password,
    ) {
    }

    public function equals(self $other): bool
    {
        return $this->email->equals($other->email)
            && $this->password->equals($other->password);
    }
}
```

## File: `src/App/User/Domain/ValueObject/Auth/HashedPassword.php`
```php
<?php

declare(strict_types=1);

namespace App\User\Domain\ValueObject\Auth;

use Assert\Assertion;
use Assert\AssertionFailedException;
use const PASSWORD_BCRYPT;
use function password_verify;

final class HashedPassword implements \Stringable
{
    public const COST = 12;

    private function __construct(private readonly string $hashedPassword)
    {
    }

    /**
     * @throws AssertionFailedException
     */
    public static function encode(string $plainPassword): self
    {
        return new self(self::hash($plainPassword));
    }

    public static function fromHash(string $hashedPassword): self
    {
        return new self($hashedPassword);
    }

    public function match(string $plainPassword): bool
    {
        return password_verify($plainPassword, $this->hashedPassword);
    }

    /**
     * @throws AssertionFailedException
     */
    private static function hash(string $plainPassword): string
    {
        Assertion::minLength($plainPassword, 6, 'Min 6 characters password');

        return \password_hash($plainPassword, PASSWORD_BCRYPT, ['cost' => self::COST]);
    }

    public function equals(self $other): bool
    {
        return $this->hashedPassword === $other->hashedPassword;
    }

    public function toString(): string
    {
        return $this->hashedPassword;
    }

    public function __toString(): string
    {
        return $this->hashedPassword;
    }
}
```

## File: `src/App/User/Domain/ValueObject/Auth/UserCredentials.php`
```php
<?php

declare(strict_types=1);

namespace App\User\Domain\ValueObject\Auth;

use App\User\Domain\ValueObject\Email;
use Ramsey\Uuid\UuidInterface;

final class UserCredentials
{
    public function __construct(
        public readonly UuidInterface $uuid,
        public readonly Email $email,
        public readonly HashedPassword $password,
    ) {
    }
}
```

## File: `src/App/User/Infrastructure/Auth/Auth.php`
```php
<?php

declare(strict_types=1);

namespace App\User\Infrastructure\Auth;

use App\User\Domain\ValueObject\Auth\HashedPassword;
use App\User\Domain\ValueObject\Email;
use Ramsey\Uuid\UuidInterface;
use Symfony\Component\PasswordHasher\Hasher\PasswordHasherAwareInterface;
use Symfony\Component\Security\Core\User\PasswordAuthenticatedUserInterface;
use Symfony\Component\Security\Core\User\UserInterface;

final class Auth implements UserInterface, PasswordHasherAwareInterface, PasswordAuthenticatedUserInterface, \Stringable
{
    private function __construct(private readonly UuidInterface $uuid, private readonly Email $email, private readonly HashedPassword $hashedPassword)
    {
    }

    public static function create(UuidInterface $uuid, Email $email, HashedPassword $hashedPassword): self
    {
        return new self($uuid, $email, $hashedPassword);
    }

    public function getUserIdentifier(): string
    {
        return $this->email->toString();
    }

    public function getPassword(): string
    {
        return $this->hashedPassword->toString();
    }

    public function getRoles(): array
    {
        return [
            'ROLE_USER',
        ];
    }

    public function eraseCredentials(): void
    {
        // noop
    }

    public function getPasswordHasherName(): string
    {
        return 'hasher';
    }

    public function uuid(): UuidInterface
    {
        return $this->uuid;
    }

    public function __toString(): string
    {
        return $this->email->toString();
    }
}
```

## File: `src/App/User/Infrastructure/Auth/AuthProvider.php`
```php
<?php

declare(strict_types=1);

namespace App\User\Infrastructure\Auth;

use App\User\Domain\ValueObject\Email;
use App\Shared\Domain\Exception\NotFoundException;
use App\User\Infrastructure\ReadModel\Mysql\MysqlReadModelUserRepository;
use Assert\AssertionFailedException;
use Doctrine\ORM\NonUniqueResultException;
use Symfony\Component\Security\Core\Exception\UserNotFoundException;
use Symfony\Component\Security\Core\User\UserInterface;
use Symfony\Component\Security\Core\User\UserProviderInterface;

/**
 * @implements UserProviderInterface<Auth>
 */
final class AuthProvider implements UserProviderInterface
{
    public function __construct(private readonly MysqlReadModelUserRepository $userReadModelRepository)
    {
    }

    public function loadUserByIdentifier(string $identifier): Auth
    {
        try {
            $credentials = $this->userReadModelRepository->getCredentialsByEmail(
                Email::fromString($identifier)
            );

            return Auth::create($credentials->uuid, $credentials->email, $credentials->password);
        } catch (NotFoundException) {
            throw new UserNotFoundException();
        }
    }

    /**
     * @throws NotFoundException
     * @throws AssertionFailedException
     * @throws NonUniqueResultException
     * @throws \Throwable
     */
    public function loadUserByUsername(string $email): Auth
    {
        $credentials = $this->userReadModelRepository->getCredentialsByEmail(
            Email::fromString($email)
        );

        return Auth::create($credentials->uuid, $credentials->email, $credentials->password);
    }

    /**
     * @throws NotFoundException
     * @throws AssertionFailedException
     * @throws NonUniqueResultException
     */
    public function refreshUser(UserInterface $user): Auth
    {
        return $this->loadUserByUsername($user->getUserIdentifier());
    }

    public function supportsClass(string $class): bool
    {
        return Auth::class === $class;
    }
}
```

## File: `src/App/User/Infrastructure/Auth/AuthenticationProvider.php`
```php
<?php

declare(strict_types=1);

namespace App\User\Infrastructure\Auth;

use App\User\Application\Query\Auth\AuthenticationProviderInterface;
use App\User\Domain\ValueObject\Auth\HashedPassword;
use App\User\Domain\ValueObject\Email;
use Lexik\Bundle\JWTAuthenticationBundle\Services\JWTTokenManagerInterface;
use Ramsey\Uuid\UuidInterface;

final class AuthenticationProvider implements AuthenticationProviderInterface
{
    public function __construct(private readonly JWTTokenManagerInterface $JWTManager)
    {
    }

    public function generateToken(UuidInterface $uuid, Email $email, HashedPassword $hashedPassword): string
    {
        $auth = Auth::create($uuid, $email, $hashedPassword);

        return $this->JWTManager->create($auth);
    }
}
```

## File: `src/App/User/Infrastructure/Auth/PasswordHasher.php`
```php
<?php

declare(strict_types=1);

namespace App\User\Infrastructure\Auth;

use App\User\Domain\ValueObject\Auth\HashedPassword;
use Symfony\Component\PasswordHasher\PasswordHasherInterface;

final class PasswordHasher implements PasswordHasherInterface {

    private string $hasher = HashedPassword::class;

    public function hash(string $plainPassword): string 
    {
        return $this->hasher::encode($plainPassword)->toString();
    }

    public function verify(string $hashedPassword, string $plainPassword): bool
    {
        return $this->hasher::fromHash($hashedPassword)->match($plainPassword);
    }

    public function needsRehash(string $hashedPassword): bool
    {
        return false;
    }
}
```

## File: `src/App/User/Infrastructure/Auth/Guard/LoginAuthenticator.php`
```php
<?php

declare(strict_types=1);

namespace App\User\Infrastructure\Auth\Guard;

use App\User\Application\Command\SignIn\SignInCommand;
use App\User\Application\Query\Auth\GetAuthUserByEmail\GetAuthUserByEmailQuery;
use App\User\Domain\Exception\InvalidCredentialsException;
use App\User\Infrastructure\Auth\Auth;
use App\Shared\Infrastructure\Bus\Command\MessengerCommandBus;
use App\Shared\Infrastructure\Bus\Query\MessengerQueryBus;
use Assert\AssertionFailedException;
use InvalidArgumentException;
use Symfony\Component\HttpFoundation\RedirectResponse;
use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Generator\UrlGeneratorInterface;
use Symfony\Component\Security\Core\Authentication\Token\TokenInterface;
use Symfony\Component\Security\Core\Exception\AuthenticationException;
use Symfony\Component\Security\Http\Authenticator\AbstractLoginFormAuthenticator;
use Symfony\Component\Security\Http\Authenticator\Passport\Badge\UserBadge;
use Symfony\Component\Security\Http\Authenticator\Passport\Credentials\PasswordCredentials;
use Symfony\Component\Security\Http\Authenticator\Passport\Passport;
use Throwable;

final class LoginAuthenticator extends AbstractLoginFormAuthenticator
{
    private const LOGIN = 'login';

    private const SUCCESS_REDIRECT = 'profile';

    public function __construct(private readonly MessengerCommandBus $bus, private readonly MessengerQueryBus $queryBus, private readonly UrlGeneratorInterface $router)
    {
    }

    private function getCredentials(Request $request): array
    {
        return [
            'email' => $request->request->get('_email'),
            'password' => $request->request->get('_password'),
        ];
    }

    public function onAuthenticationSuccess(Request $request, TokenInterface $token, string $firewallName): Response
    {
        return new RedirectResponse($this->router->generate(self::SUCCESS_REDIRECT));
    }

    protected function getLoginUrl(Request $request): string
    {
        return $this->router->generate(self::LOGIN);
    }

    /**
     * @throws AssertionFailedException
     * @throws Throwable
     */
    public function authenticate(Request $request): Passport
    {
        $credentials = $this->getCredentials($request);

        try {
            $email = $credentials['email'];
            $plainPassword = $credentials['password'];

            $signInCommand = new SignInCommand($email, $plainPassword);

            $this->bus->handle($signInCommand);

            return new Passport(
                new UserBadge($email, fn(string $email): Auth => $this->queryBus->ask(new GetAuthUserByEmailQuery($email))),
                new PasswordCredentials($plainPassword)
            );
        } catch (InvalidCredentialsException | InvalidArgumentException) {
            throw new AuthenticationException();
        }
    }
}
```

## File: `src/App/User/Infrastructure/Persistence/Doctrine/Types/EmailType.php`
```php
<?php

declare(strict_types=1);

namespace App\User\Infrastructure\Persistence\Doctrine\Types;

use App\User\Domain\ValueObject\Email;
use Doctrine\DBAL\Platforms\AbstractPlatform;
use Doctrine\DBAL\Types\ConversionException;
use Doctrine\DBAL\Types\StringType;
use Throwable;

final class EmailType extends StringType
{
    private const TYPE = 'email';

    /**
     * @throws ConversionException
     */
    public function convertToDatabaseValue(mixed $value, AbstractPlatform $platform): ?string
    {
        if (null === $value) {
            return null;
        }

        if (!$value instanceof Email) {
            throw ConversionException::conversionFailedInvalidType($value, $this->getName(), ['null', Email::class]);
        }

        return $value->toString();
    }

    /**
     * @throws ConversionException
     */
    public function convertToPHPValue(mixed $value, AbstractPlatform $platform): ?Email
    {
        if (null === $value || $value instanceof Email) {
            return $value;
        }

        try {
            $email = Email::fromString($value);
        } catch (Throwable) {
            throw ConversionException::conversionFailedFormat($value, $this->getName(), 'a valid email address');
        }

        return $email;
    }

    public function getName(): string
    {
        return self::TYPE;
    }
}
```

## File: `src/App/User/Infrastructure/Persistence/Doctrine/Types/HashedPasswordType.php`
```php
<?php

declare(strict_types=1);

namespace App\User\Infrastructure\Persistence\Doctrine\Types;

use App\User\Domain\ValueObject\Auth\HashedPassword;
use Doctrine\DBAL\Platforms\AbstractPlatform;
use Doctrine\DBAL\Types\ConversionException;
use Doctrine\DBAL\Types\StringType;
use Throwable;

final class HashedPasswordType extends StringType
{
    private const TYPE = 'hashed_password';

    /**
     * @throws ConversionException
     */
    public function convertToDatabaseValue(mixed $value, AbstractPlatform $platform): ?string
    {
        if (null === $value) {
            return null;
        }

        if (!$value instanceof HashedPassword) {
            throw ConversionException::conversionFailedInvalidType($value, $this->getName(), ['null', HashedPassword::class]);
        }

        return $value->toString();
    }

    /**
     * @throws ConversionException
     */
    public function convertToPHPValue(mixed $value, AbstractPlatform $platform): ?HashedPassword
    {
        if (null === $value || $value instanceof HashedPassword) {
            return $value;
        }

        try {
            $hashedPassword = HashedPassword::fromHash($value);
        } catch (Throwable) {
            throw ConversionException::conversionFailedFormat($value, $this->getName(), 'a valid hashed password');
        }

        return $hashedPassword;
    }

    public function getName(): string
    {
        return self::TYPE;
    }
}
```

## File: `src/App/User/Infrastructure/ReadModel/UserView.php`
```php
<?php

declare(strict_types=1);

namespace App\User\Infrastructure\ReadModel;

use App\Shared\Domain\Exception\DateTimeException;
use App\Shared\Domain\ValueObject\DateTime;
use App\User\Domain\ValueObject\Auth\Credentials;
use App\User\Domain\ValueObject\Auth\HashedPassword;
use App\User\Domain\ValueObject\Email;
use Assert\AssertionFailedException;
use Broadway\ReadModel\SerializableReadModel;
use Broadway\Serializer\Serializable;
use Ramsey\Uuid\Uuid;
use Ramsey\Uuid\UuidInterface;

/**
 * @psalm-suppress MissingConstructor
 */
class UserView implements SerializableReadModel
{
    final public const string TYPE = 'UserView';

    private readonly UuidInterface $uuid;

    private Credentials $credentials;

    public DateTime $createdAt;

    public ?DateTime $updatedAt;

    private function __construct(UuidInterface $uuid, Credentials $credentials, DateTime $createdAt, ?DateTime $updatedAt)
    {
        $this->uuid = $uuid;
        $this->credentials = $credentials;
        $this->createdAt = $createdAt;
        $this->updatedAt = $updatedAt;
    }

    /**
     * @throws DateTimeException
     * @throws AssertionFailedException
     */
    public static function fromSerializable(Serializable $event): self
    {
        return self::deserialize($event->serialize());
    }

    /**
     * @throws DateTimeException
     * @throws AssertionFailedException
     */
    public static function deserialize(array $data): self
    {
        return new self(
            Uuid::fromString($data['uuid']),
            new Credentials(
                Email::fromString($data['credentials']['email']),
                HashedPassword::fromHash($data['credentials']['password'] ?? '')
            ),
            DateTime::fromString($data['created_at']),
            isset($data['updated_at']) ? DateTime::fromString($data['updated_at']) : null
        );
    }

    public function serialize(): array
    {
        return [
            'uuid' => $this->getId(),
            'credentials' => [
                'email' => (string) $this->credentials->email,
            ],
        ];
    }

    public function uuid(): UuidInterface
    {
        return $this->uuid;
    }

    public function email(): string
    {
        return (string) $this->credentials->email;
    }

    public function hashedPassword(): HashedPassword
    {
        return $this->credentials->password;
    }

    public function changeEmail(Email $email): void
    {
        $this->credentials = new Credentials($email, $this->credentials->password);
    }

    public function changeUpdatedAt(DateTime $updatedAt): void
    {
        $this->updatedAt = $updatedAt;
    }

    public function getId(): string
    {
        return $this->uuid->toString();
    }
}
```

## File: `src/App/User/Infrastructure/ReadModel/Mysql/MysqlReadModelUserRepository.php`
```php
<?php

declare(strict_types=1);

namespace App\User\Infrastructure\ReadModel\Mysql;

use App\User\Domain\Repository\CheckUserByEmailInterface;
use App\User\Domain\Repository\GetUserCredentialsByEmailInterface;
use App\User\Domain\Repository\UserReadModelRepositoryInterface;
use App\User\Domain\ValueObject\Auth\UserCredentials;
use App\User\Domain\ValueObject\Email;
use App\Shared\Domain\Exception\NotFoundException;
use App\Shared\Infrastructure\Persistence\ReadModel\Repository\MysqlRepository;
use App\User\Infrastructure\ReadModel\UserView;
use Doctrine\ORM\AbstractQuery;
use Doctrine\ORM\EntityRepository;
use Doctrine\ORM\NonUniqueResultException;
use Doctrine\ORM\QueryBuilder;
use Ramsey\Uuid\UuidInterface;

final class MysqlReadModelUserRepository extends MysqlRepository implements CheckUserByEmailInterface, GetUserCredentialsByEmailInterface, UserReadModelRepositoryInterface
{
    protected function setEntityManager(): void
    {
        /** @var EntityRepository $objectRepository */
        $objectRepository = $this->entityManager->getRepository(UserView::class);
        $this->repository = $objectRepository;
    }

    private function getUserByEmailQueryBuilder(Email $email): QueryBuilder
    {
        return $this->repository
            ->createQueryBuilder('user')
            ->where('user.credentials.email = :email')
            ->setParameter('email', $email->toString());
    }

    /**
     * @throws NotFoundException
     * @throws NonUniqueResultException
     */
    public function oneByUuid(UuidInterface $uuid): UserView
    {
        $qb = $this->repository
            ->createQueryBuilder('user')
            ->where('user.uuid = :uuid')
            ->setParameter('uuid', $uuid->getBytes())
        ;

        return $this->oneOrException($qb);
    }

    /**
     * @throws NonUniqueResultException
     */
    public function findUuidByEmail(Email $email): ?UuidInterface
    {
        $userId = $this->getUserByEmailQueryBuilder($email)
            ->select('user.uuid')
            ->getQuery()
            ->getOneOrNullResult(AbstractQuery::HYDRATE_ARRAY)
        ;

        return $userId['uuid'] ?? null;
    }

    /**
     * @throws NotFoundException
     * @throws NonUniqueResultException
     */
    public function oneByEmail(Email $email): UserView
    {
        return $this->oneOrException(
            $this->getUserByEmailQueryBuilder($email)
        );
    }

    /**
     * @throws NotFoundException
     * @throws NonUniqueResultException
     */
    public function oneByEmailAsArray(Email $email): array
    {
        return $this->oneOrException(
            $this->getUserByEmailQueryBuilder($email)
            ->select('
                user.uuid, 
                user.credentials.email, 
                user.createdAt, 
                user.updatedAt'
            ),
            AbstractQuery::HYDRATE_ARRAY
        );
    }

    public function add(UserView $userRead): void
    {
        $this->register($userRead);
    }

    /**
     * @throws NotFoundException
     * @throws NonUniqueResultException
     */
    public function getCredentialsByEmail(Email $email): UserCredentials
    {
        $qb = $this->repository
            ->createQueryBuilder('user')
            ->where('user.credentials.email = :email')
            ->setParameter('email', $email->toString());

        $user = $this->oneOrException($qb, AbstractQuery::HYDRATE_ARRAY);

        return new UserCredentials(
            $user['uuid'],
            $user['credentials.email'],
            $user['credentials.password'],
        );
    }
}
```

## File: `src/App/User/Infrastructure/ReadModel/Projections/ConsoleProjectionFactory.php`
```php
<?php

declare(strict_types=1);

namespace App\User\Infrastructure\ReadModel\Projections;

use App\User\Domain\Event\UserSignedIn;
use App\Shared\Infrastructure\Bus\AsyncEvent\MessengerAsyncEventBus;
use Broadway\Domain\DomainMessage;
use Psr\Log\LoggerInterface;
use Symfony\Component\Messenger\Attribute\AsMessageHandler;
/**
 * Class ConsoleProjectionFactory
 *
 * @description This is a dummy example about how to handle custom Events
 *  In this case all events sent to users transport will be consumed here.
 *  In this example we only act on UserSignedIn event.
 *
 *  In order to be able to process all events to be sent to Elasticseach I didn't find any other solution than send the
 *  DomainMessage instead the Event itself so it's send to the Async event bus inside the envelop. That a problem
 *  when trying to identify the object itself for routing or others. Because of this I added a routing key to the
 *  messenger envelope in the async event bus so you can configure symfony messenger to route your events to a different
 *  transport base on routing keys. There's room for improvement here but I'm facing messenger limitations so will
 *  probably need to contribute to the project to get certain features like multiple messages per handler
 * (a la EventListener) instead the current one to one binding or Subscription models.
 *
 *  An example of how to use this:
 *      MessengerConfig:
 *
 * @see MessengerAsyncEventBus::handle
 */
#[AsMessageHandler(bus: 'messenger.bus.event.async', fromTransport: 'users', priority: 10)]
final class ConsoleProjectionFactory
{
    public function __construct(private readonly LoggerInterface $logger)
    {
    }
    public function __invoke(DomainMessage $message): void
    {
        if (!$message->getPayload() instanceof UserSignedIn) {
            return;
        }

        $this->onUserSignedIn($message->getPayload());
    }

    private function onUserSignedIn(UserSignedIn $event): void
    {
        $this->logger->info('Welcome to the jungle ' . $event->email->toString());
    }
}
```

## File: `src/App/User/Infrastructure/ReadModel/Projections/UserProjectionFactory.php`
```php
<?php

declare(strict_types=1);

namespace App\User\Infrastructure\ReadModel\Projections;

use App\Shared\Domain\Exception\DateTimeException;
use App\User\Domain\Event\UserEmailChanged;
use App\User\Domain\Event\UserWasCreated;
use App\Shared\Domain\Exception\NotFoundException;
use App\User\Infrastructure\ReadModel\Mysql\MysqlReadModelUserRepository;
use App\User\Infrastructure\ReadModel\UserView;
use Assert\AssertionFailedException;
use Broadway\ReadModel\Projector;
use Doctrine\ORM\NonUniqueResultException;

final class UserProjectionFactory extends Projector
{
    public function __construct(private readonly MysqlReadModelUserRepository $repository)
    {
    }

    /**
     * @throws AssertionFailedException
     * @throws DateTimeException
     */
    protected function applyUserWasCreated(UserWasCreated $userWasCreated): void
    {
        $userReadModel = UserView::fromSerializable($userWasCreated);

        $this->repository->add($userReadModel);
    }

    /**
     * @throws NotFoundException
     * @throws NonUniqueResultException
     */
    protected function applyUserEmailChanged(UserEmailChanged $emailChanged): void
    {
        $userReadModel = $this->repository->oneByUuid($emailChanged->uuid);

        $userReadModel->changeEmail($emailChanged->email);
        $userReadModel->changeUpdatedAt($emailChanged->updatedAt);

        $this->repository->apply();
    }
}
```

## File: `src/App/User/Infrastructure/Repository/UserStore.php`
```php
<?php

declare(strict_types=1);

namespace App\User\Infrastructure\Repository;

use App\User\Domain\Repository\UserRepositoryInterface;
use App\User\Domain\User;
use Broadway\EventHandling\EventBus;
use Broadway\EventSourcing\AggregateFactory\PublicConstructorAggregateFactory;
use Broadway\EventSourcing\EventSourcingRepository;
use Broadway\EventStore\EventStore;
use Ramsey\Uuid\UuidInterface;

final class UserStore extends EventSourcingRepository implements UserRepositoryInterface
{
    public function __construct(
        EventStore $eventStore,
        EventBus $eventBus,
        array $eventStreamDecorators = []
    ) {
        parent::__construct(
            $eventStore,
            $eventBus,
            User::class,
            new PublicConstructorAggregateFactory(),
            $eventStreamDecorators
        );
    }

    public function store(User $user): void
    {
        $this->save($user);
    }

    public function get(UuidInterface $uuid): User
    {
        /** @var User $user */
        $user = $this->load($uuid->toString());

        return $user;
    }
}
```

## File: `src/App/User/Infrastructure/Specification/UniqueEmailSpecification.php`
```php
<?php

declare(strict_types=1);

namespace App\User\Infrastructure\Specification;

use App\User\Domain\Exception\EmailAlreadyExistException;
use App\User\Domain\Repository\CheckUserByEmailInterface;
use App\User\Domain\Specification\UniqueEmailSpecificationInterface;
use App\User\Domain\ValueObject\Email;
use Doctrine\ORM\NonUniqueResultException;

/**
 * Application-level uniqueness check. A UNIQUE index on credentials_email
 * (see Version20200727170306 migration) acts as a safety net at the DB level.
 */
final class UniqueEmailSpecification implements UniqueEmailSpecificationInterface
{
    public function __construct(private readonly CheckUserByEmailInterface $checkUserByEmail)
    {
    }

    /**
     * @throws EmailAlreadyExistException
     */
    public function isUnique(Email $email): bool
    {
        try {
            if ($this->checkUserByEmail->findUuidByEmail($email)) {
                throw new EmailAlreadyExistException();
            }
        } catch (NonUniqueResultException) {
            throw new EmailAlreadyExistException();
        }

        return true;
    }
}
```

## File: `src/UI/Cli/Command/CreateUserCommand.php`
```php
<?php

declare(strict_types=1);

namespace UI\Cli\Command;

use App\Shared\Application\Command\CommandBusInterface;
use App\User\Application\Command\SignUp\SignUpCommand as CreateUser;
use Assert\AssertionFailedException;
use Exception;
use Ramsey\Uuid\Uuid;
use Symfony\Component\Console\Command\Command;
use Symfony\Component\Console\Input\InputArgument;
use Symfony\Component\Console\Input\InputInterface;
use Symfony\Component\Console\Output\OutputInterface;
use Throwable;
use Symfony\Component\Console\Attribute\AsCommand;

#[AsCommand(name: 'app:create-user', description: 'Given a uuid and email, generates a new user.')]
class CreateUserCommand extends Command
{
    public function __construct(private readonly CommandBusInterface $commandBus)
    {
        parent::__construct();
    }

    protected function configure(): void
    {
        $this->setDescription('Given a uuid and email, generates a new user.')
            ->addArgument('email', InputArgument::REQUIRED, 'User email')
            ->addArgument('password', InputArgument::REQUIRED, 'User password')
            ->addArgument('uuid', InputArgument::OPTIONAL, 'User Uuid')
        ;
    }

    /**
     * @throws Exception
     * @throws AssertionFailedException
     * @throws Throwable
     */
    protected function execute(InputInterface $input, OutputInterface $output): int
    {
        /** @var string $uuid */
        $uuid = $input->getArgument('uuid') ?: Uuid::uuid4()->toString();
        /** @var string $email */
        $email = $input->getArgument('email');
        /** @var string $password */
        $password = $input->getArgument('password');

        $command = new CreateUser($uuid, $email, $password);

        $this->commandBus->handle($command);

        $output->writeln('<info>User Created: </info>');
        $output->writeln('');
        $output->writeln("Uuid: $uuid");
        $output->writeln("Email: $email");

        return Command::SUCCESS;
    }
}
```

## File: `src/UI/Http/Session.php`
```php
<?php

declare(strict_types=1);

namespace UI\Http;

use App\User\Domain\Exception\InvalidCredentialsException;
use App\User\Infrastructure\Auth\Auth;
use Symfony\Component\Security\Core\Authentication\Token\Storage\TokenStorageInterface;

final class Session
{
    public function __construct(private readonly TokenStorageInterface $tokenStorage)
    {
    }

    public function get(): Auth
    {
        $token = $this->tokenStorage->getToken();

        if (!$token) {
            throw new InvalidCredentialsException();
        }

        $user = $token->getUser();

        if (!$user instanceof Auth) {
            throw new InvalidCredentialsException();
        }

        return $user;
    }
}
```

## File: `src/UI/Http/Rest/Controller/CommandController.php`
```php
<?php

declare(strict_types=1);

namespace UI\Http\Rest\Controller;

use App\Shared\Application\Command\CommandBusInterface;
use App\Shared\Application\Command\CommandInterface;
use Throwable;

abstract class CommandController
{
    public function __construct(private readonly CommandBusInterface $commandBus)
    {
    }

    /**
     * @throws Throwable
     */
    protected function handle(CommandInterface $command): void
    {
        $this->commandBus->handle($command);
    }
}
```

## File: `src/UI/Http/Rest/Controller/CommandQueryController.php`
```php
<?php

declare(strict_types=1);

namespace UI\Http\Rest\Controller;

use App\Shared\Application\Command\CommandBusInterface;
use App\Shared\Application\Command\CommandInterface;
use App\Shared\Application\Query\QueryBusInterface;
use Symfony\Component\Routing\Generator\UrlGeneratorInterface;
use Throwable;

abstract class CommandQueryController extends QueryController
{
    public function __construct(
        private readonly CommandBusInterface $commandBus,
        QueryBusInterface $queryBus,
        UrlGeneratorInterface $router
    ) {
        parent::__construct($queryBus, $router);
    }

    /**
     * @throws Throwable
     */
    protected function handle(CommandInterface $command): void
    {
        $this->commandBus->handle($command);
    }
}
```

## File: `src/UI/Http/Rest/Controller/QueryController.php`
```php
<?php

declare(strict_types=1);

namespace UI\Http\Rest\Controller;

use App\Shared\Application\Query\Collection;
use App\Shared\Application\Query\Item;
use App\Shared\Application\Query\QueryBusInterface;
use App\Shared\Application\Query\QueryInterface;
use UI\Http\Rest\Response\OpenApi;
use Symfony\Component\Routing\Generator\UrlGeneratorInterface;
use Throwable;

abstract class QueryController
{
    private const int CACHE_MAX_AGE = 31_536_000;

    public function __construct(
        // Year.
        private readonly QueryBusInterface $queryBus,
        private readonly UrlGeneratorInterface $router
    )
    {
    }

    /**
     * @throws Throwable
     */
    protected function ask(QueryInterface $query): mixed
    {
        return $this->queryBus->ask($query);
    }

    protected function jsonCollection(Collection $collection, int $status = OpenApi::HTTP_OK, bool $isImmutable = false): OpenApi
    {
        $response = OpenApi::collection($collection, $status);

        $this->decorateWithCache($response, $collection, $isImmutable);

        return $response;
    }

    protected function json(Item $resource, int $status = OpenApi::HTTP_OK): OpenApi
    {
        return OpenApi::one($resource, $status);
    }

    protected function route(string $name, array $params = []): string
    {
        return $this->router->generate($name, $params);
    }

    private function decorateWithCache(OpenApi $response, Collection $collection, bool $isImmutable): void
    {
        if ($isImmutable && $collection->limit === \count($collection->data)) {
            $response
                ->setMaxAge(self::CACHE_MAX_AGE)
                ->setSharedMaxAge(self::CACHE_MAX_AGE);
        }
    }
}
```

## File: `src/UI/Http/Rest/Controller/Auth/CheckController.php`
```php
<?php

declare(strict_types=1);

namespace UI\Http\Rest\Controller\Auth;

use App\User\Application\Command\SignIn\SignInCommand;
use App\User\Application\Query\Auth\GetToken\GetTokenQuery;
use App\User\Domain\Exception\InvalidCredentialsException;
use Symfony\Component\HttpFoundation\Response;
use UI\Http\Rest\Controller\CommandQueryController;
use UI\Http\Rest\Response\OpenApi;
use Assert\Assertion;
use Assert\AssertionFailedException;
use OpenApi\Attributes as OA;
use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\Routing\Attribute\Route;
use Throwable;

final class CheckController extends CommandQueryController
{
    /**
     * @throws AssertionFailedException
     * @throws InvalidCredentialsException
     * @throws Throwable
     */
    #[OA\Response(
        response: Response::HTTP_OK,
        description: 'Login success',
        content: new OA\JsonContent(
            properties: [
                new OA\Property(property: 'token', type: 'string'),
            ],
            type: 'object'
        )
    )]
    #[OA\Response(
        response: Response::HTTP_BAD_REQUEST,
        description: 'Bad request',
    )]
    #[OA\Response(
        response: Response::HTTP_UNAUTHORIZED,
        description: 'Bad credentials',
    )]
    #[OA\RequestBody(
        content: new OA\JsonContent(
            properties: [
                new OA\Property(property: '_password', type: 'string'),
                new OA\Property(property: '_username', type: 'string'),
            ],
            type: 'object'
        )
    )]
    #[OA\Tag(name: 'Auth')]
    #[Route(path: '/auth_check', name: 'auth_check', requirements: ['_username' => '\w+', '_password' => '\w+'], methods: [Request::METHOD_POST])]
    public function __invoke(Request $request): OpenApi
    {
        $username = (string) $request->request->get('_username');

        Assertion::notEmpty($username, 'Username cant\'t be empty');

        $signInCommand = new SignInCommand(
            $username,
            (string) $request->request->get('_password')
        );

        $this->handle($signInCommand);

        return OpenApi::fromPayload(
            [
                'token' => $this->ask(new GetTokenQuery($username)),
            ],
            OpenApi::HTTP_OK
        );
    }
}
```

## File: `src/UI/Http/Rest/Controller/Event/GetEventsController.php`
```php
<?php

declare(strict_types=1);

namespace UI\Http\Rest\Controller\Event;

use App\Shared\Application\Query\Collection;
use App\Shared\Application\Query\Event\GetEvents\GetEventsQuery;
use Symfony\Component\HttpFoundation\Response;
use UI\Http\Rest\Controller\QueryController;
use UI\Http\Rest\Response\OpenApi;
use Assert\Assertion;
use Assert\AssertionFailedException;
use Nelmio\ApiDocBundle\Annotation\Security;
use OpenApi\Attributes as OA;
use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\Routing\Attribute\Route;
use Throwable;

class GetEventsController extends QueryController
{
    /**
     * @throws AssertionFailedException
     * @throws Throwable
     */
    #[OA\Response(
        ref: '#/components/responses/events',
        response: Response::HTTP_OK,
        description: 'Return events list'
    )]
    #[OA\Response(
        response: Response::HTTP_BAD_REQUEST,
        description: 'Bad request',
        content: new OA\JsonContent(ref: '#/components/schemas/Error')
    )]
    #[OA\Response(
        response: Response::HTTP_CONFLICT,
        description: 'Conflict'
    )]
    #[OA\Parameter(ref: '#/components/parameters/page')]
    #[OA\Parameter(ref: '#/components/parameters/limit')]
    #[OA\Tag(name: 'Events')]
    #[Security(name: 'Bearer')]
    #[Route(path: '/events', name: 'events', methods: [Request::METHOD_GET])]
    public function __invoke(Request $request): OpenApi
    {
        $page = $request->query->get('page', 1);
        $limit = $request->query->get('limit', 50);

        Assertion::numeric($page, 'Page number must be an integer');
        Assertion::numeric($limit, 'Limit results must be an integer');

        $query = new GetEventsQuery((int) $page, (int) $limit);

        /** @var Collection $response */
        $response = $this->ask($query);

        return $this->jsonCollection($response, 200, true);
    }
}
```

## File: `src/UI/Http/Rest/Controller/Healthz/HealthzController.php`
```php
<?php

declare(strict_types=1);

namespace UI\Http\Rest\Controller\Healthz;

use App\Shared\Infrastructure\Event\ReadModel\ElasticSearchEventRepository;
use App\User\Infrastructure\ReadModel\Mysql\MysqlReadModelUserRepository;
use Symfony\Component\HttpFoundation\Response;
use UI\Http\Rest\Response\OpenApi;
use OpenApi\Attributes as OA;
use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\Routing\Attribute\Route;

final class HealthzController
{
    public function __construct(
        private readonly ElasticSearchEventRepository $elasticSearchEventRepository,
        private readonly MysqlReadModelUserRepository $mysqlReadModelUserRepository
    ){
    }

    #[OA\Response(
        response: Response::HTTP_OK,
        description: 'OK'
    )]
    #[OA\Response(
        response: Response::HTTP_INTERNAL_SERVER_ERROR,
        description: 'Something not ok'
    )]
    #[OA\Tag(name: 'Healthz')]
    #[Route(path: '/healthz', name: 'healthz', methods: [Request::METHOD_GET])]
    public function __invoke(Request $request): OpenApi
    {
        $elastic = null;
        $mysql = null;

        if (
            (true === ($elastic = $this->elasticSearchEventRepository->isHealthy())) &&
            (true === ($mysql = $this->mysqlReadModelUserRepository->isHealthy()))
        ) {
            return OpenApi::empty(200);
        }

        return OpenApi::fromPayload(
            [
                'Healthy services' => [
                    'Elastic' => $elastic,
                    'MySQL' => $mysql,
                ],
            ],
            500
        );
    }
}
```

## File: `src/UI/Http/Rest/Controller/User/GetUserByEmailController.php`
```php
<?php

declare(strict_types=1);

namespace UI\Http\Rest\Controller\User;

use App\Shared\Application\Query\Item;
use App\User\Application\Query\User\FindByEmail\FindByEmailQuery;
use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\Response;
use UI\Http\Rest\Controller\QueryController;
use UI\Http\Rest\Response\OpenApi;
use Assert\Assertion;
use Assert\AssertionFailedException;
use Nelmio\ApiDocBundle\Annotation\Security;
use OpenApi\Attributes as OA;
use Symfony\Component\Routing\Attribute\Route;
use Throwable;

final class GetUserByEmailController extends QueryController
{
    /**
     * @throws AssertionFailedException
     * @throws Throwable
     */
    #[OA\Response(
        ref: '#/components/responses/users',
        response: Response::HTTP_OK,
        description: 'Returns the user of the given email',
    )]
    #[OA\Response(
        response: Response::HTTP_BAD_REQUEST,
        description: 'Bad request',
    )]
    #[OA\Response(
        response: Response::HTTP_NOT_FOUND,
        description: 'Not found',
    )]
    #[OA\Tag(name: 'User')]
    #[Security(name: 'Bearer')]
    #[Route(path: '/user/{email}', name: 'find_user', methods: [Request::METHOD_GET])]
    public function __invoke(string $email): OpenApi
    {
        Assertion::email($email, "Email can\'t be empty or invalid");

        $query = new FindByEmailQuery($email);

        /** @var Item $user */
        $user = $this->ask($query);

        return $this->json($user);
    }
}
```

## File: `src/UI/Http/Rest/Controller/User/SignUpController.php`
```php
<?php

declare(strict_types=1);

namespace UI\Http\Rest\Controller\User;

use App\User\Application\Command\SignUp\SignUpCommand;
use Symfony\Component\HttpFoundation\Response;
use UI\Http\Rest\Controller\CommandController;
use UI\Http\Rest\Response\OpenApi;
use Assert\Assertion;
use Assert\AssertionFailedException;
use OpenApi\Attributes as OA;
use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\Routing\Attribute\Route;
use Throwable;

final class SignUpController extends CommandController
{
    /**
     * @throws AssertionFailedException
     * @throws Throwable
     */
    #[OA\Response(
        response: Response::HTTP_CREATED,
        description: 'User created successfully',
    )]
    #[OA\Response(
        response: Response::HTTP_BAD_REQUEST,
        description: 'Bad request',
    )]
    #[OA\Response(
        response: Response::HTTP_CONFLICT,
        description: 'Conflict',
    )]
    #[OA\RequestBody(
        content: new OA\JsonContent(
            properties: [
                new OA\Property(property: 'uuid', type: 'string', format: 'uuid'),
                new OA\Property(property: 'email', type: 'string', format: 'email'),
                new OA\Property(property: 'password', type: 'string', format: 'string'),
            ],
            type: 'object',
        )
    )]
    #[OA\Tag(name: 'User')]
    #[Route(path: '/signup', name: 'user_create', methods: [Request::METHOD_POST])]
    public function __invoke(Request $request): OpenApi
    {
        $uuid = (string) $request->request->get('uuid');
        $email = (string) $request->request->get('email');
        $plainPassword = (string) $request->request->get('password');

        Assertion::notEmpty($uuid, "Uuid can\'t be empty");
        Assertion::notEmpty($email, "Email can\'t be empty");
        Assertion::notEmpty($plainPassword, "Password can\'t be empty");

        $commandRequest = new SignUpCommand($uuid, $email, $plainPassword);

        $this->handle($commandRequest);

        return OpenApi::created("/user/$email");
    }
}
```

## File: `src/UI/Http/Rest/Controller/User/UserChangeEmailController.php`
```php
<?php

declare(strict_types=1);

namespace UI\Http\Rest\Controller\User;

use App\Shared\Application\Command\CommandBusInterface;
use App\User\Application\Command\ChangeEmail\ChangeEmailCommand;
use App\User\Domain\Exception\ForbiddenException;
use Symfony\Component\HttpFoundation\Response;
use UI\Http\Rest\Controller\CommandController;
use UI\Http\Session;
use Assert\Assertion;
use Assert\AssertionFailedException;
use Nelmio\ApiDocBundle\Annotation\Security;
use OpenApi\Attributes as OA;
use Ramsey\Uuid\Uuid;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\Routing\Attribute\Route;
use Throwable;

final class UserChangeEmailController extends CommandController
{
    public function __construct(private readonly Session $session, CommandBusInterface $commandBus)
    {
        parent::__construct($commandBus);
    }

    /**
     * @throws AssertionFailedException
     * @throws Throwable
     */
    #[OA\Response(
        response: Response::HTTP_CREATED,
        description: 'Email changed'
    )]
    #[OA\Response(
        response: Response::HTTP_BAD_REQUEST,
        description: 'Bad request'
    )]
    #[OA\Response(
        response: Response::HTTP_CONFLICT,
        description: 'Conflict',
    )]
    #[OA\RequestBody(
        content: new OA\JsonContent(
            properties: [
                new OA\Property(property: 'email', type: 'string', format: 'email')
            ],
            type: 'object'
        )
    )]
    #[OA\Parameter(
        name: 'uuid',
        in: 'path',
        schema: new OA\Schema(type: 'string', format: 'uuid')
    )]
    #[OA\Tag(name: 'User')]
    #[Security(name: 'Bearer')]
    #[Route(path: '/users/{uuid}/email', name: 'user_change_email', methods: [Request::METHOD_POST])]
    public function __invoke(string $uuid, Request $request): JsonResponse
    {
        $this->validateUuid($uuid);

        $email = (string) $request->request->get('email');

        Assertion::notEmpty($email, "Email can\'t be empty");

        $command = new ChangeEmailCommand($uuid, $email);

        $this->handle($command);

        return new JsonResponse();
    }

    private function validateUuid(string $uuid): void
    {
        if (!$this->session->get()->uuid()->equals(Uuid::fromString($uuid))) {
            throw new ForbiddenException();
        }
    }
}
```

## File: `src/UI/Http/Rest/EventSubscriber/ExceptionSubscriber.php`
```php
<?php

declare(strict_types=1);

namespace UI\Http\Rest\EventSubscriber;

use Symfony\Component\EventDispatcher\EventSubscriberInterface;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\HttpKernel\Event\ExceptionEvent;
use Symfony\Component\HttpKernel\Exception\HttpExceptionInterface;
use Symfony\Component\HttpKernel\KernelEvents;
use Throwable;

final class ExceptionSubscriber implements EventSubscriberInterface
{
    public function __construct(private readonly string $environment, private readonly array $exceptionToStatus = [])
    {
    }

    public static function getSubscribedEvents(): array
    {
        return [
            KernelEvents::EXCEPTION => 'onKernelException',
        ];
    }

    public function onKernelException(ExceptionEvent $event): void
    {
        $request = $event->getRequest();
        if ($request->getContentTypeFormat() !== 'json') {
            return;
        }

        $exception = $event->getThrowable();

        $response = new JsonResponse();
        $response->headers->set('Content-Type', 'application/vnd.api+json');
        $response->setStatusCode($this->determineStatusCode($exception));
        $response->setData($this->getErrorMessage($exception));

        $event->setResponse($response);
    }

    private function getErrorMessage(Throwable $exception): array
    {
        $error = [
            'error' => [
                'title' => \str_replace('\\', '.', $exception::class),
                'detail' => $this->getExceptionMessage($exception),
                'code' => $exception->getCode(),
            ],
        ];

        if ('dev' === $this->environment) {
            $error = [...$error, ...[
                'meta' => [
                    'file' => $exception->getFile(),
                    'line' => $exception->getLine(),
                    'message' => $exception->getMessage(),
                    'trace' => $exception->getTrace(),
                    'traceString' => $exception->getTraceAsString(),
                ],
            ]];
        }

        return $error;
    }

    private function getExceptionMessage(Throwable $exception): string
    {
        return $exception->getMessage();
    }

    private function determineStatusCode(Throwable $exception): int
    {
        $exceptionClass = $exception::class;

        foreach ($this->exceptionToStatus as $class => $status) {
            if (\is_a($exceptionClass, $class, true)) {
                return $status;
            }
        }

        // Process HttpExceptionInterface after `exceptionToStatus` to allow overrides from config
        if ($exception instanceof HttpExceptionInterface) {
            return $exception->getStatusCode();
        }

        // Default status code is always 500
        return Response::HTTP_INTERNAL_SERVER_ERROR;
    }
}
```

## File: `src/UI/Http/Rest/EventSubscriber/JsonBodyParserSubscriber.php`
```php
<?php

declare(strict_types=1);

namespace UI\Http\Rest\EventSubscriber;

use const JSON_THROW_ON_ERROR;
use Symfony\Component\EventDispatcher\EventSubscriberInterface;
use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\HttpKernel\Event\RequestEvent;
use Symfony\Component\HttpKernel\KernelEvents;
use Throwable;

class JsonBodyParserSubscriber implements EventSubscriberInterface
{
    public static function getSubscribedEvents(): array
    {
        return [
            KernelEvents::REQUEST => 'onKernelRequest',
        ];
    }

    public function onKernelRequest(RequestEvent $event): void
    {
        $request = $event->getRequest();
        if (!$this->isJsonRequest($request)) {
            return;
        }

        $content = $request->getContent();
        if (empty($content)) {
            return;
        }

        if (!$this->transformJsonBody($request)) {
            $response = new Response('Unable to parse json request.', Response::HTTP_BAD_REQUEST);
            $event->setResponse($response);
        }
    }

    private function isJsonRequest(Request $request): bool
    {
        return 'json' === $request->getContentTypeFormat();
    }

    private function transformJsonBody(Request $request): bool
    {
        try {
            $data = \json_decode(
                $request->getContent(),
                true,
                512,
                JSON_THROW_ON_ERROR
            );
        } catch (Throwable) {
            return false;
        }

        if (null === $data) {
            return true;
        }

        $request->request->replace($data);

        return true;
    }
}
```

## File: `src/UI/Http/Rest/Response/OpenApi.php`
```php
<?php

declare(strict_types=1);

namespace UI\Http\Rest\Response;

use App\Shared\Application\Query\Collection;
use App\Shared\Application\Query\Item;
use Symfony\Component\HttpFoundation\JsonResponse;

class OpenApi extends JsonResponse
{
    private function __construct(mixed $data = null, int $status = self::HTTP_OK, array $headers = [], bool $json = false)
    {
        parent::__construct($data, $status, $headers, $json);
    }

    public static function fromPayload(array $payload, int $status): self
    {
        return new self($payload, $status);
    }

    public static function empty(int $status): self
    {
        return new self(null, $status);
    }

    public static function one(Item $resource, int $status = self::HTTP_OK): self
    {
        return new self(
            [
                'data' => self::model($resource),
                'relationships' => self::relations($resource->relationships),
            ],
            $status
        );
    }

    public static function created(?string $location = null): self
    {
        return new self(
            null,
            self::HTTP_CREATED,
            ($location !== null) ? ['location' => $location] : []
        );
    }

    public static function collection(Collection $collection, int $status = self::HTTP_OK): self
    {
        /**
         * @psalm-suppress MissingClosureParamType
         *
         * @param Item|array $data
         *
         * @return array
         */
        $transformer = fn($data): array => $data instanceof Item ? self::model($data) : $data;

        $resources = \array_map($transformer, $collection->data);

        return new self(
            [
                'meta' => [
                    'size' => $collection->limit,
                    'page' => $collection->page,
                    'total' => $collection->total,
                ],
                'data' => $resources,
            ],
            $status
        );
    }

    private static function model(Item $resource): array
    {
        return [
            'id' => $resource->id,
            'type' => $resource->type,
            'attributes' => $resource->resource,
        ];
    }

    /**
     * @param Item[] $relations
     */
    private static function relations($relations): array
    {
        $result = [];

        foreach ($relations as $relation) {
            $result[$relation->type] = [
                'data' => self::model($relation),
            ];
        }

        return $result;
    }
}
```

## File: `src/UI/Http/Web/Controller/AbstractRenderController.php`
```php
<?php

declare(strict_types=1);

namespace UI\Http\Web\Controller;

use App\Shared\Application\Command\CommandBusInterface;
use App\Shared\Application\Command\CommandInterface;
use App\Shared\Application\Query\Collection;
use App\Shared\Application\Query\Item;
use App\Shared\Application\Query\QueryBusInterface;
use App\Shared\Application\Query\QueryInterface;
use Symfony\Component\HttpFoundation\Response;
use Throwable;
use Twig;

abstract class AbstractRenderController
{
    public function __construct(private readonly Twig\Environment $template, private readonly CommandBusInterface $commandBus, private readonly QueryBusInterface $queryBus)
    {
    }

    /**
     * @throws Twig\Error\LoaderError
     * @throws Twig\Error\RuntimeError
     * @throws Twig\Error\SyntaxError
     */
    protected function render(string $view, array $parameters = [], int $code = Response::HTTP_OK): Response
    {
        $content = $this->template->render($view, $parameters);

        return new Response($content, $code);
    }

    /**
     * @throws Throwable
     */
    protected function handle(CommandInterface $command): void
    {
        $this->commandBus->handle($command);
    }

    /**\
     * @throws Throwable
     */
    protected function ask(QueryInterface $query): mixed
    {
        return $this->queryBus->ask($query);
    }
}
```

## File: `src/UI/Http/Web/Controller/HomeController.php`
```php
<?php

declare(strict_types=1);

namespace UI\Http\Web\Controller;

use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Attribute\Route;
use Twig\Error\LoaderError;
use Twig\Error\RuntimeError;
use Twig\Error\SyntaxError;

class HomeController extends AbstractRenderController
{
    /**
     *
     * @throws LoaderError
     * @throws RuntimeError
     * @throws SyntaxError
     */
    #[Route(path: '/', name: 'home', methods: ['GET'])]
    public function get(): Response
    {
        return $this->render('home/index.html.twig');
    }
}
```

## File: `src/UI/Http/Web/Controller/ProfileController.php`
```php
<?php

declare(strict_types=1);

namespace UI\Http\Web\Controller;

use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Attribute\Route;
use Twig\Error\LoaderError;
use Twig\Error\RuntimeError;
use Twig\Error\SyntaxError;

class ProfileController extends AbstractRenderController
{
    /**
     *
     * @throws LoaderError
     * @throws RuntimeError
     * @throws SyntaxError
     */
    #[Route(path: '/profile', name: 'profile', methods: ['GET'])]
    public function profile(): Response
    {
        return $this->render('profile/index.html.twig');
    }
}
```

## File: `src/UI/Http/Web/Controller/SecurityController.php`
```php
<?php

declare(strict_types=1);

namespace UI\Http\Web\Controller;

use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Attribute\Route;
use Symfony\Component\Security\Core\Exception\AuthenticationException;
use Symfony\Component\Security\Http\Authentication\AuthenticationUtils;
use Twig\Error\LoaderError;
use Twig\Error\RuntimeError;
use Twig\Error\SyntaxError;

class SecurityController extends AbstractRenderController
{
    /**
     *
     * @throws LoaderError
     * @throws RuntimeError
     * @throws SyntaxError
     */
    #[Route(path: '/sign-in', name: 'login', methods: ['GET', 'POST'])]
    public function login(AuthenticationUtils $authUtils): Response
    {
        return $this->render('signin/login.html.twig', [
            'last_username' => $authUtils->getLastUsername(),
            'error' => $authUtils->getLastAuthenticationError(),
        ]);
    }

    #[Route(path: '/logout', name: 'logout')]
    public function logout(): never
    {
        throw new AuthenticationException('I shouldn\'t be here..');
    }
}
```

## File: `src/UI/Http/Web/Controller/SignUpController.php`
```php
<?php

declare(strict_types=1);

namespace UI\Http\Web\Controller;

use App\User\Application\Command\SignUp\SignUpCommand;
use App\User\Domain\Exception\EmailAlreadyExistException;
use Assert\Assertion;
use Assert\AssertionFailedException;
use InvalidArgumentException;
use Ramsey\Uuid\Uuid;
use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Attribute\Route;
use Throwable;
use Twig\Error\LoaderError;
use Twig\Error\RuntimeError;
use Twig\Error\SyntaxError;

class SignUpController extends AbstractRenderController
{
    /**
     *
     * @throws LoaderError
     * @throws RuntimeError
     * @throws SyntaxError
     */
    #[Route(path: '/sign-up', name: 'sign-up', methods: ['GET'])]
    public function get(): Response
    {
        $uuid = Uuid::uuid4()->toString();

        return $this->render('signup/index.html.twig', ['uuid' => $uuid]);
    }

    /**
     *
     * @throws AssertionFailedException
     * @throws Throwable
     * @throws LoaderError
     * @throws RuntimeError
     * @throws SyntaxError
     */
    #[Route(path: '/sign-up', name: 'sign-up-post', methods: ['POST'])]
    public function post(Request $request): Response
    {
        $errorHTTPStatusCode = null;
        $afterErrorUuid = Uuid::uuid4()->toString();


        $uuid = $request->request->get('uuid');
        $email = $request->request->get('email');
        $password = $request->request->get('password');

        try {
            Assertion::notNull($uuid, 'Missing uuid');
            Assertion::notNull($email, 'Email can\'t be null');
            Assertion::notNull($password, 'Password can\'t be null');

            $this->handle(new SignUpCommand((string) $uuid, (string) $email, (string) $password));

            return $this->render('signup/user_created.html.twig', ['uuid' => $uuid, 'email' => $email]);
        } catch (EmailAlreadyExistException $exception) {
            $errorHTTPStatusCode = Response::HTTP_CONFLICT;

            return $this->render('signup/index.html.twig', ['uuid' => $afterErrorUuid, 'error' => $exception->getMessage()], $errorHTTPStatusCode);
        } catch (InvalidArgumentException $exception) {
            $errorHTTPStatusCode= Response::HTTP_BAD_REQUEST;

            return $this->render('signup/index.html.twig', ['uuid' => $afterErrorUuid, 'error' => $exception->getMessage()], $errorHTTPStatusCode);
        }
    }
}
```

## File: `src/UI/Http/Web/templates/base.html.twig`
```
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <title>{% block title %}Hey!{% endblock %}</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        {% block stylesheets %}
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bulma/0.6.2/css/bulma.min.css">
        {% endblock %}
    </head>
    <body>
        {% include 'components/header/menu.html.twig' only %}
        <br>
        <section class="section">
            {% block body %}{% endblock %}
        </section>
        {% block javascripts %}{% endblock %}
        <script>
          document.addEventListener('DOMContentLoaded', function () {
            // Get all "navbar-burger" elements
            var $navbarBurgers = Array.prototype.slice.call(document.querySelectorAll('.navbar-burger'), 0);
            // Check if there are any navbar burgers
            if ($navbarBurgers.length > 0) {
              // Add a click event on each of them
              $navbarBurgers.forEach(function ($el) {
                $el.addEventListener('click', function () {
                  var $target = document.getElementById($el.dataset.target);
                  // Toggle the class on both the "navbar-burger" and the "navbar-menu"
                  $el.classList.toggle('is-active');
                  $target.classList.toggle('is-active');
                });
              });
            }
          });
        </script>
    </body>
</html>
```

## File: `src/UI/Http/Web/templates/components/card.html.twig`
```
<div class="card">
    <div class="card-header">
        <p class="card-header-title">
            {{ title }}
        </p>
    </div>
    <div class="card-content">
        {{ text }}
    </div>
</div>
```

## File: `src/UI/Http/Web/templates/components/header/menu.html.twig`
```
<nav class="navbar is-fixed-top" style="box-shadow: 1px -4px 18px #ccc;">
    <div class="navbar-brand">
        <a class="navbar-item" href="/">
            <h2>Ola que ase QRS</h2>
        </a>
        <div class="navbar-burger burger" data-target="nav">
            <span></span>
            <span></span>
            <span></span>
        </div>
    </div>
    <div id="nav" class="navbar-menu">
        <div class="navbar-start">
            <div class="navbar-item has-dropdown is-hoverable">
                <a class="navbar-link">
                    Docs
                </a>
                <div class="navbar-dropdown is-boxed">
                    <a class="navbar-item" href="/">
                        Overview
                    </a>
                    <a class="navbar-item" href="/">
                        Modifiers
                    </a>
                </div>
            </div>
        </div>

        <div class="navbar-end">
            <div class="navbar-item">
                {% if is_granted('ROLE_USER') %}
                    <span class="tag is-white">{{ app.user.userIdentifier }}</span>
                    <a class="button is-danger" href="{{ path('logout') }}">Exit</a>
                {% else %}
                    <div class="field is-grouped">
                        <div class="control">
                            <a class="button is-info" href="{{ path('sign-up') }}">Sign up</a>
                            <a class="button is-primary" href="{{ path('login') }}">Sign in</a>
                        </div>
                    </div>
                {% endif %}
            </div>
        </div>
    </div>
</nav>
```

## File: `src/UI/Http/Web/templates/home/index.html.twig`
```
{% extends 'base.html.twig' %}

{% block body %}
<div class="container">
    <div class="columns is-centered">
        <div class="column is-half">
            {% include 'components/card.html.twig' with { 'title': 'Hello!', 'text': 'Lorem ipsum hamend awer fiti carem conde moren. Fistro pecadorem de las praderum.'} only %}
        </div>
    </div>
</div>
{% endblock body %}
```

## File: `src/UI/Http/Web/templates/profile/index.html.twig`
```
{% extends 'base.html.twig' %}

{% block body %}
<div class="container">
    <div class="columns is-centered">
        <div class="column is-half">
            <h2>Hi {{ app.user.userIdentifier }}</h2>
        </div>
    </div>
</div>
{% endblock body %}
```

## File: `src/UI/Http/Web/templates/signin/login.html.twig`
```
{% extends 'base.html.twig' %}

{% block body %}
    <div class="container">
        <div class="columns is-centered">
            <div class="column is-half">
                {% if error %}
                    <div class="notification is-danger">{{ error.messageKey|trans(error.messageData, 'security') }}</div>
                {% endif %}
                <form action="{{ path('login') }}" method="post">
                    <div class="field">
                        <label for="username">Username:</label>
                        <div class="control">
                            <input class="input" type="text" id="username" name="_email" value="{{ last_username }}" />
                        </div>
                    </div>
                    <div class="field">
                        <label for="password">Password:</label>
                        <div class="control">
                            <input class="input" type="password" id="password" name="_password" />
                        </div>
                    </div>
                    <div class="field">
                        <div class="control">
                            <button class="button is-link" type="submit">Sign in</button>
                        </div>
                    </div>
                </form>
            </div>
        </div>
    </div>
{% endblock body %}
```

## File: `src/UI/Http/Web/templates/signup/index.html.twig`
```
{% extends 'base.html.twig' %}

{% block body %}
<div class="container">
    <div class="columns is-centered">
        <div class="column is-half">
            {% if error is defined %}
                <div class="notification is-danger">{{ error }}</div>
            {% endif %}
            <form name="signUp" action="{{ path('sign-up') }}" method="post">
                <div class="control">
                    <input class="input" name="uuid" type="hidden" value="{{ uuid }}" id="uuid">
                </div>
                <div class="field">
                    <label for="email">Email</label>
                    <div class="control">
                        <input class="input" name="email" type="email" placeholder="asd@as.as" id="email">
                    </div>
                </div>
                <div class="field">
                    <label for="password">Password</label>
                    <div class="control">
                        <input class="input" name="password" type="password" placeholder="******" id="password">
                    </div>
                </div>
                <div class="field">
                    <div class="control">
                        <input class="button is-link" type="submit" value="Send">
                    </div>
                </div>
            </form>
        </div>
    </div>
</div>
{% endblock body %}
```

## File: `src/UI/Http/Web/templates/signup/user_created.html.twig`
```
{% extends 'base.html.twig' %}

{% block body %}
<div class="container">
    <div class="columns is-centered">
        <div class="column is-half">
            <h2>Hello {{ email }}</h2>
            <i>Your id is {{ uuid }}</i>
        </div>
    </div>
</div>
{% endblock body %}
```

## File: `tests/App/Shared/Application/ApplicationTestCase.php`
```php
<?php

declare(strict_types=1);

namespace Tests\App\Shared\Application;

use App\Shared\Application\Command\CommandBusInterface;
use App\Shared\Application\Command\CommandInterface;
use App\Shared\Application\Query\QueryBusInterface;
use App\Shared\Application\Query\QueryInterface;
use Symfony\Bundle\FrameworkBundle\Test\KernelTestCase;
use Symfony\Component\EventDispatcher\EventDispatcher;
use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\HttpKernel\Event\TerminateEvent;
use Symfony\Component\HttpKernel\KernelEvents;
use Throwable;

abstract class ApplicationTestCase extends KernelTestCase
{
    private ?CommandBusInterface $commandBus;

    private ?QueryBusInterface $queryBus;

    protected function setUp(): void
    {
        self::bootKernel();

        $this->commandBus = $this->service(CommandBusInterface::class);
        $this->queryBus = $this->service(QueryBusInterface::class);
    }

    /**
     * @return mixed
     *
     * @throws Throwable
     */
    protected function ask(QueryInterface $query)
    {
        return $this->queryBus->ask($query);
    }

    /**
     * @throws Throwable
     */
    protected function handle(CommandInterface $command): void
    {
        $this->commandBus->handle($command);
    }

    /**
     * @return object|null
     */
    protected function service(string $serviceId)
    {
        return $this->getContainer()->get($serviceId);
    }

    protected function fireTerminateEvent(): void
    {
        /** @var EventDispatcher $dispatcher */
        $dispatcher = $this->service('event_dispatcher');

        $dispatcher->dispatch(
            new TerminateEvent(
                static::$kernel,
                Request::create('/'),
                new Response()
            ),
            KernelEvents::TERMINATE
        );
    }

    protected function tearDown(): void
    {
        parent::tearDown();
        $this->commandBus = null;
        $this->queryBus = null;
    }
}
```

## File: `tests/App/Shared/Application/Query/CollectionTest.php`
```php
<?php

declare(strict_types=1);

namespace Tests\App\Shared\Application\Query;

use App\Shared\Application\Query\Collection;
use App\Shared\Domain\Exception\NotFoundException;
use PHPUnit\Framework\TestCase;

class CollectionTest extends TestCase
{
    /**
     * @test
     *
     * @group unit
     *
     * @throws NotFoundException
     */
    public function must_throw_not_found_exception_on_not_page_found(): void
    {
        $this->expectException(NotFoundException::class);

        new Collection(2, 10, 2, []);
    }
}
```

## File: `tests/App/Shared/Application/Query/Event/GetEvents/GetEventsTest.php`
```php
<?php

declare(strict_types=1);

namespace Tests\App\Application\Query\Event\GetEvents;

use App\Shared\Application\Query\Collection;
use App\Shared\Application\Query\Event\GetEvents\GetEventsQuery;
use App\Shared\Application\Query\Item;
use App\Shared\Infrastructure\Event\Consumer\SendEventsToElasticConsumer;
use App\Shared\Infrastructure\Event\ReadModel\ElasticSearchEventRepository;
use App\User\Application\Command\SignUp\SignUpCommand;
use App\User\Domain\Event\UserWasCreated;
use Assert\AssertionFailedException;
use Broadway\Domain\DomainMessage;
use Broadway\Domain\Metadata;
use Ramsey\Uuid\Uuid;
use Tests\App\Shared\Application\ApplicationTestCase;
use Throwable;

final class GetEventsTest extends ApplicationTestCase
{

    /**
     * @throws \App\Shared\Domain\Exception\DateTimeException
     * @throws \Assert\AssertionFailedException
     * @throws \Throwable
     */
    protected function setUp(): void
    {
        parent::setUp();

        /** @var ElasticSearchEventRepository $eventReadStore */
        $eventReadStore = $this->service(ElasticSearchEventRepository::class);
        $eventReadStore->reboot();

        $command = new SignUpCommand(
            Uuid::uuid4()->toString(),
            'asd@asd.asd',
            'qwerqwer'
        );

        $this->handle($command);

        /** @var SendEventsToElasticConsumer $consumer
         */
        $consumer = $this->service(SendEventsToElasticConsumer::class);
        $data = [
            'uuid' => $uuid = Uuid::uuid4()->toString(),
            'credentials' => [
                'email' => 'asd@asd.asd',
                'password' => '$2y$12$90mmbScglod8M3adPNvXsOIyiFC.AqOpgTktQTnnu1.Pvn5inVcUm',
            ],
            'created_at' => '2020-02-20',
        ];

        $consumer(DomainMessage::recordNow($uuid, 1, new Metadata(), UserWasCreated::deserialize($data)));

        $this->fireTerminateEvent();

        /** @var ElasticSearchEventRepository $eventReadStore */
        $eventReadStore = $this->service(ElasticSearchEventRepository::class);
        $eventReadStore->refresh();
    }

    /**
     * @test
     *
     * @group integration
     *
     * @throws Throwable
     */
    public function processed_events_must_be_in_elastic_search(): void
    {
        $response = $this->ask(new GetEventsQuery());

        self::assertInstanceOf(Collection::class, $response);

        $item = $response->data[0];

        self::assertSame(1, $response->total);
        self::assertSame('App.User.Domain.Event.UserWasCreated', $item['type']);
        self::assertSame('asd@asd.asd', $item['payload']['credentials']['email']);
    }

    protected function tearDown(): void
    {
        /** @var ElasticSearchEventRepository $eventReadStore */
        $eventReadStore = $this->service(ElasticSearchEventRepository::class);
        $eventReadStore->delete();

        parent::tearDown();
    }
}
```

## File: `tests/App/Shared/Domain/ValueObject/DateTimeTest.php`
```php
<?php

declare(strict_types=1);

namespace Tests\App\Shared\Domain\ValueObject;

use App\Shared\Domain\Exception\DateTimeException;
use App\Shared\Domain\ValueObject\DateTime;
use PHPUnit\Framework\TestCase;

class DateTimeTest extends TestCase
{
    final public const BAD_DATETIME = 'LOL';

    /**
     * @test
     *
     * @group unit
     *
     * @throws DateTimeException
     */
    public function given_a_bad_formatted_datetime_string_it_should_throw_an_exception_when_we_try_to_create_datetime(): void
    {
        $this->expectException(DateTimeException::class);
        DateTime::fromString(self::BAD_DATETIME);
    }
}
```

## File: `tests/App/Shared/Infrastructure/Event/EventCollectorListener.php`
```php
<?php

declare(strict_types=1);

namespace Tests\App\Shared\Infrastructure\Event;

use Broadway\Domain\DomainMessage;
use Broadway\EventHandling\EventListener;

class EventCollectorListener implements EventListener
{
    public function handle(DomainMessage $domainMessage): void
    {
        $this->publishedEvents[] = $domainMessage;
    }

    public function popEvents(): array
    {
        $events = $this->publishedEvents;

        $this->publishedEvents = [];

        return $events;
    }

    private array $publishedEvents = [];
}
```

## File: `tests/App/Shared/Infrastructure/Event/Publisher/EventPublisherTest.php`
```php
<?php

declare(strict_types=1);

namespace Tests\App\Shared\Infrastructure\Event\Publisher;

use App\Shared\Domain\Exception\DateTimeException;
use App\Shared\Domain\ValueObject\DateTime as DomainDateTime;
use App\User\Domain\Event\UserWasCreated;
use App\Shared\Infrastructure\Event\Publisher\AsyncEventPublisher;
use Assert\AssertionFailedException;
use Broadway\Domain\DomainMessage;
use Broadway\Domain\Metadata;
use Ramsey\Uuid\Uuid;
use Symfony\Component\Messenger\Transport\TransportInterface;
use Tests\App\Shared\Application\ApplicationTestCase;
use Throwable;

class EventPublisherTest extends ApplicationTestCase
{
    private ?AsyncEventPublisher $publisher;

    private ?TransportInterface $transport;

    protected function setUp(): void
    {
        parent::setUp();

        $this->publisher = $this->service(AsyncEventPublisher::class);
        $this->transport = $this->service('messenger.transport.events');
    }

    /**
     * @test
     *
     * @group integration
     *
     * @throws AssertionFailedException
     * @throws DateTimeException
     * @throws Throwable
     */
    public function events_are_consumed(): void
    {
        $current = DomainDateTime::now();

        $data = [
            'uuid' => $uuid = Uuid::uuid4()->toString(),
            'credentials' => [
                'email' => 'lol@lol.com',
                'password' => 'lkasjbdalsjdbalsdbaljsdhbalsjbhd987',
            ],
            'created_at' => $current->toString(),
        ];

        $this->publisher->handle(DomainMessage::recordNow($uuid, 1, new Metadata(), UserWasCreated::deserialize($data)));

        $this->publisher->publish();

        $transportMessages = $this->transport->get();
        self::assertCount(1, $transportMessages);

        $event = $transportMessages[0]->getMessage()->getPayload();

        self::assertInstanceOf(UserWasCreated::class, $event);
        self::assertSame($data, $event->serialize(), 'Check that its the same event');
    }

    protected function tearDown(): void
    {
        $this->publisher = null;
        $this->transport = null;
    }
}
```

## File: `tests/App/Shared/Infrastructure/Event/Query/EventElasticRepositoryTest.php`
```php
<?php

declare(strict_types=1);

namespace Tests\App\Shared\Infrastructure\Event\Query;

use App\Shared\Domain\Exception\DateTimeException;
use App\Shared\Domain\ValueObject\DateTime as DomainDateTime;
use App\User\Domain\Event\UserWasCreated;
use App\Shared\Infrastructure\Event\ReadModel\ElasticSearchEventRepository;
use Assert\AssertionFailedException;
use Broadway\Domain\DomainMessage;
use Broadway\Domain\Metadata;
use PHPUnit\Framework\TestCase;

class EventElasticRepositoryTest extends TestCase
{
    private ?ElasticSearchEventRepository $repository;

    protected function setUp(): void
    {
        $this->repository = new ElasticSearchEventRepository(
            [
                'hosts' => [
                    'elasticsearch',
                ],
            ]
        );
        $this->repository->reboot();
        $this->repository->refresh();
    }

    /**
     * @test
     *
     * @group integration
     *
     * @throws AssertionFailedException
     * @throws DateTimeException
     */
    public function an_event_should_be_stored_in_elastic(): void
    {
        $data = [
            'uuid' => $uuid = 'e937f793-45d8-41e9-a756-a2bc711e3172',
            'credentials' => [
                'email' => 'lol@lol.com',
                'password' => 'lkasjbdalsjdbalsdbaljsdhbalsjbhd987',
            ],
            'created_at' => DomainDateTime::now()->toString(),
        ];

        $event = DomainMessage::recordNow($uuid, 1, new Metadata(), UserWasCreated::deserialize($data));

        $this->repository->store($event);
        $this->repository->refresh();

        $result = $this->repository->search([
            'query' => [
                'match' => [
                    'type' => $event->getType(),
                ],
            ],
        ]);

        self::assertSame(1, $result['hits']['total']['value']);
    }

    protected function tearDown(): void
    {
        $this->repository->delete();
        $this->repository = null;
    }
}
```

## File: `tests/App/Shared/Infrastructure/Persistence/Doctrine/DateTimeTypeTest.php`
```php
<?php

declare(strict_types=1);

namespace Tests\App\Shared\Infrastructure\Persistence\Doctrine;

use App\Shared\Infrastructure\Persistence\Doctrine\Types\DateTimeType;
use Doctrine\DBAL\Platforms\MySQLPlatform;
use Doctrine\DBAL\Types\ConversionException;
use Doctrine\DBAL\Types\Type;
use PHPUnit\Framework\TestCase;
use Doctrine\DBAL\Exception;

class DateTimeTypeTest extends TestCase
{
    final public const TYPE = 'lol';

    final public const BAD_DATE = 'lol';

    private \Doctrine\DBAL\Types\Type $dateTimeType;

    /**
     * @throws \Throwable
     */
    public function setUp(): void
    {
        if (!Type::hasType(self::TYPE)) {
            Type::addType(self::TYPE, DateTimeType::class);
        }

        $this->dateTimeType = Type::getType(self::TYPE);
    }

    /**
     * @test
     *
     * @group unit
     */
    public function given_a_datetimetype_when_i_get_the_sql_declaration_then_it_should_print_the_platform_string(): void
    {
        self::assertSame('DATETIME', $this->dateTimeType->getSQLDeclaration([], new MySQLPlatform()));
    }

    /**
     * @test
     *
     * @group unit
     */
    public function given_a_datetimetype_with_a_invalid_date_then_it_should_throw_an_exception(): void
    {
        $this->expectException(ConversionException::class);

        $this->dateTimeType->convertToPHPValue(self::BAD_DATE, new MySQLPlatform());
    }

    /**
     * @test
     *
     * @group unit
     */
    public function given_a_datetimetype_with_a_null_date_then_it_should_return_null(): void
    {
        self::assertNull($this->dateTimeType->convertToPHPValue(null, new MySQLPlatform()));
    }

    /**
     * @test
     *
     * @group unit
     */
    public function given_a_php_datetime_value_it_should_throw_an_exception(): void
    {
        $this->expectException(ConversionException::class);

        $this->dateTimeType->convertToDatabaseValue(self::BAD_DATE, new MySQLPlatform());
    }

    /**
     * @test
     *
     * @group unit
     */
    public function given_a_php_datetimetype_with_a_null_date_then_it_should_return_null(): void
    {
        self::assertNull($this->dateTimeType->convertToDatabaseValue(null, new MySQLPlatform()));
    }

    /**
     * @test
     *
     * @group unit
     *
     * @throws \Exception
     */
    public function given_a_php_an_immutable_datetime_value_it_should_return_a_correct_format(): void
    {
        $datetimeImmutable = new \DateTimeImmutable();
        $mysqlPlatform = new MySQLPlatform();

        self::assertSame(
            $this->dateTimeType->convertToDatabaseValue($datetimeImmutable, $mysqlPlatform),
            $datetimeImmutable->format($mysqlPlatform->getDateTimeFormatString())
        );
    }
}
```

## File: `tests/App/User/Application/Command/ChangeEmail/ChangeEmailHandlerTest.php`
```php
<?php

declare(strict_types=1);

namespace Tests\App\Application\Command\User\ChangeEmail;


use App\User\Application\Command\ChangeEmail\ChangeEmailCommand;
use App\User\Application\Command\SignUp\SignUpCommand;
use App\User\Domain\Event\UserEmailChanged;
use Assert\AssertionFailedException;
use Broadway\Domain\DomainMessage;
use Exception;
use Ramsey\Uuid\Uuid;
use Tests\App\Shared\Application\ApplicationTestCase;
use Tests\App\Shared\Infrastructure\Event\EventCollectorListener;
use Throwable;

class ChangeEmailHandlerTest extends ApplicationTestCase
{
    /**
     * @test
     *
     * @group integration
     *
     * @throws Exception
     * @throws AssertionFailedException
     * @throws Throwable
     */
    public function update_user_email_should_command_should_fire_event(): void
    {
        $command = new SignUpCommand($uuid = Uuid::uuid4()->toString(), 'asd@asd.asd', 'password');

        $this->handle($command);

        $email = 'lol@asd.asd';

        $command = new ChangeEmailCommand($uuid, $email);

        $this->handle($command);

        /** @var EventCollectorListener $eventCollector
         */
        $eventCollector = $this->service(EventCollectorListener::class);

        /** @var DomainMessage[] $events */
        $events = $eventCollector->popEvents();

        self::assertCount(2, $events);

        /** @var UserEmailChanged $emailChangedEmail */
        $emailChangedEmail = $events[1]->getPayload();

        self::assertInstanceOf(UserEmailChanged::class, $emailChangedEmail);
        self::assertSame($email, $emailChangedEmail->email->toString());
    }
}
```

## File: `tests/App/User/Application/Command/SignIn/SignInTest.php`
```php
<?php

declare(strict_types=1);

namespace Tests\App\Application\Command\User\SignIn;

use App\User\Application\Command\SignIn\SignInCommand;
use App\User\Application\Command\SignUp\SignUpCommand;
use App\User\Domain\Event\UserSignedIn;
use App\User\Domain\Exception\InvalidCredentialsException;
use Assert\AssertionFailedException;
use Broadway\Domain\DomainMessage;
use Exception;
use Ramsey\Uuid\Uuid;
use Tests\App\Shared\Application\ApplicationTestCase;
use Tests\App\Shared\Infrastructure\Event\EventCollectorListener;
use Throwable;

final class SignInTest extends ApplicationTestCase
{
    /**
     * @test
     *
     * @group integration
     *
     * @throws Throwable
     */
    public function user_sign_up_with_valid_credentials(): void
    {
        $command = new SignInCommand(
            'asd@asd.asd',
            'qwerqwer'
        );

        $this->handle($command);

        /** @var EventCollectorListener $eventCollector */
        $eventCollector = $this->service(EventCollectorListener::class);
        /** @var DomainMessage[] $events */
        $events = $eventCollector->popEvents();

        self::assertInstanceOf(UserSignedIn::class, $events[1]->getPayload());
    }

    /**
     * @test
     *
     * @group integration
     *
     * @dataProvider invalidCredentials
     *
     * @throws AssertionFailedException
     * @throws Throwable
     */
    public function user_sign_up_with_invalid_credentials_must_throw_domain_exception(string $email, string $pass): void
    {
        $this->expectException(InvalidCredentialsException::class);

        $command = new SignInCommand($email, $pass);

        $this->handle($command);
    }

    public static function invalidCredentials(): array
    {
        return [
          [
              'email' => 'asd@asd.asd',
              'pass' => 'qwerqwer123',
          ],
          [
              'email' => 'asd@asd.com',
              'pass' => 'qwerqwer',
          ],
        ];
    }

    /**
     * @throws Exception
     * @throws AssertionFailedException
     * @throws Throwable
     */
    protected function setUp(): void
    {
        parent::setUp();

        $command = new SignUpCommand(
            Uuid::uuid4()->toString(),
            'asd@asd.asd',
            'qwerqwer'
        );

        $this->handle($command);
    }
}
```

## File: `tests/App/User/Application/Command/SignUp/SignUpHandlerTest.php`
```php
<?php

declare(strict_types=1);

namespace Tests\App\Application\Command\User\SignUp;

use App\User\Application\Command\SignUp\SignUpCommand;
use App\User\Domain\Event\UserWasCreated;
use Broadway\Domain\DomainMessage;
use Ramsey\Uuid\Uuid;
use Tests\App\Shared\Application\ApplicationTestCase;
use Tests\App\Shared\Infrastructure\Event\EventCollectorListener;

class SignUpHandlerTest extends ApplicationTestCase
{
    /**
     * @test
     *
     * @group integration
     *
     * @throws \Exception
     * @throws \Assert\AssertionFailedException
     */
    public function command_handler_must_fire_domain_event(): void
    {
        $uuid = Uuid::uuid4();
        $email = 'asd@asd.asd';

        $command = new SignUpCommand($uuid->toString(), $email, 'password');
        $this
            ->handle($command);

        /** @var EventCollectorListener $collector */
        $collector = $this->service(EventCollectorListener::class);

        /** @var DomainMessage[] $events */
        $events = $collector->popEvents();

        self::assertCount(1, $events);

        /** @var UserWasCreated $userCreatedEvent */
        $userCreatedEvent = $events[0]->getPayload();

        self::assertInstanceOf(UserWasCreated::class, $userCreatedEvent);
    }
}
```

## File: `tests/App/User/Application/Query/FindByEmail/FindByEmailHandlerTest.php`
```php
<?php

declare(strict_types=1);

namespace Tests\App\User\Application\Query\FindByEmail;

use App\Shared\Application\Query\Item;
use App\User\Application\Command\SignUp\SignUpCommand;
use App\User\Application\Query\User\FindByEmail\FindByEmailQuery;
use Assert\AssertionFailedException;
use Ramsey\Uuid\Uuid;
use Tests\App\Shared\Application\ApplicationTestCase;
use Throwable;

class FindByEmailHandlerTest extends ApplicationTestCase
{
    /**
     * @test
     *
     * @group integration
     *
     * @throws AssertionFailedException
     * @throws Throwable
     */
    public function query_command_integration(): void
    {
        $email = $this->createUserRead();

        $this->fireTerminateEvent();

        /** @var Item $result */
        $result = $this->ask(new FindByEmailQuery($email));

        self::assertInstanceOf(Item::class, $result);
        self::assertSame('UserView', $result->type);
        self::assertSame($email, $result->resource['credentials.email']->toString());
    }

    /**
     * @throws Throwable
     * @throws AssertionFailedException
     */
    private function createUserRead(): string
    {
        $uuid = Uuid::uuid4()->toString();
        $email = 'lol@lol.com';

        $this->handle(new SignUpCommand($uuid, $email, 'password'));

        return $email;
    }
}
```

## File: `tests/App/User/Domain/UserTest.php`
```php
<?php

declare(strict_types=1);

namespace Tests\App\User\Domain;

use App\User\Domain\Event\UserEmailChanged;
use App\User\Domain\Event\UserWasCreated;
use App\User\Domain\Exception\EmailAlreadyExistException;
use App\User\Domain\Specification\UniqueEmailSpecificationInterface;
use App\User\Domain\User;
use App\User\Domain\ValueObject\Auth\Credentials;
use App\User\Domain\ValueObject\Auth\HashedPassword;
use App\User\Domain\ValueObject\Email;
use Broadway\Domain\DomainMessage;
use PHPUnit\Framework\TestCase;
use Ramsey\Uuid\Uuid;

class UserTest extends TestCase implements UniqueEmailSpecificationInterface
{
    private bool $isUniqueException = false;

    /**
     * @test
     *
     * @group unit
     *
     * @throws \Exception
     * @throws \Assert\AssertionFailedException
     */
    public function given_a_valid_email_it_should_create_a_user_instance(): void
    {
        $emailString = 'lol@aso.maximo';

        $user = User::create(
            Uuid::uuid4(),
            new Credentials(
                Email::fromString($emailString),
                HashedPassword::encode('password')
            ),
            $this
        );

        self::assertSame($emailString, $user->email()->toString());
        self::assertNotEmpty($user->uuid()->toString());

        $events = $user->getUncommittedEvents();

        self::assertCount(1, $events->getIterator(), 'Only one event should be in the buffer');

        /** @var DomainMessage $event */
        $event = $events->getIterator()->current();

        self::assertInstanceOf(UserWasCreated::class, $event->getPayload(), 'First event should be UserWasCreated');
    }

    /**
     * @test
     *
     * @group unit
     *
     * @throws \Exception
     * @throws \Assert\AssertionFailedException
     */
    public function given_a_new_email_it_should_change_if_not_eq_to_prev_email(): void
    {
        $emailString = 'lol@aso.maximo';

        $user = User::create(
            Uuid::uuid4(),
            new Credentials(
                Email::fromString($emailString),
                HashedPassword::encode('password')
            ),
            $this
        );

        $newEmail = 'weba@aso.maximo';

        $user->changeEmail(Email::fromString($newEmail), $this);

        self::assertSame($user->email()->toString(), $newEmail, 'Emails should be equals');

        $events = $user->getUncommittedEvents();

        self::assertCount(2, $events->getIterator(), '2 event should be in the buffer');

        /** @var DomainMessage $event */
        $event = $events->getIterator()->offsetGet(1);

        self::assertInstanceOf(UserEmailChanged::class, $event->getPayload(), 'Second event should be UserEmailChanged');
    }

    /**
     * @test
     *
     * @group unit
     *
     * @throws \Exception
     * @throws \Assert\AssertionFailedException
     */
    public function given_a_registered_email_it_should_throw_an_email_already_exists_exception(): void
    {
        self::expectException(EmailAlreadyExistException::class);

        $this->isUniqueException = true;

        $emailString = 'lol@aso.maximo';

        $user = User::create(
            Uuid::uuid4(),
            new Credentials(
                Email::fromString($emailString),
                HashedPassword::encode('password')
            ),
            $this
        );

        $newEmail = 'weba@aso.maximo';

        $user->changeEmail(Email::fromString($newEmail), $this);
    }

    /**
     * @throws EmailAlreadyExistException
     */
    public function isUnique(Email $email): bool
    {
        if ($this->isUniqueException) {
            throw new EmailAlreadyExistException();
        }

        return true;
    }

    /**
     * @test
     *
     * @group unit
     */
    public function given_a_new_email_when_email_changes_should_update_the_update_at_field(): void
    {
        $emailString = 'lol@aso.maximo';

        $user = User::create(
            Uuid::uuid4(),
            new Credentials(
                Email::fromString($emailString),
                HashedPassword::encode('password')
            ),
            $this
        );

        self::assertNotEmpty($user->createdAt()->toString());
        self::assertNull($user->updatedAt());

        $initialUpdatedAt = $user->updatedAt();
        \usleep(1000);
        $newEmail = 'weba@aso.maximo';
        $user->changeEmail(Email::fromString($newEmail), $this);

        self::assertNotSame($user->updatedAt()->toString(), $initialUpdatedAt);
    }
}
```

## File: `tests/App/User/Domain/Event/UserEmailChangedTest.php`
```php
<?php

declare(strict_types=1);

namespace Tests\App\User\Domain\User\Event;

use App\Shared\Domain\ValueObject\DateTime;
use App\User\Domain\Event\UserEmailChanged;
use App\User\Domain\ValueObject\Email;
use PHPUnit\Framework\TestCase;

class UserEmailChangedTest extends TestCase
{
    /**
     * @test
     *
     * @group unit
     *
     * @throws \App\Shared\Domain\Exception\DateTimeException
     * @throws \Assert\AssertionFailedException
     * @throws \Throwable
     */
    public function event_should_be_deserializable(): void
    {
        $event = UserEmailChanged::deserialize([
            'uuid' => 'eb62dfdc-2086-11e8-b467-0ed5f89f718b',
            'email' => 'asd@asd.asd',
            'updated_at' => DateTime::now()->toString(),
        ]);

        self::assertInstanceOf(UserEmailChanged::class, $event);
        self::assertSame('eb62dfdc-2086-11e8-b467-0ed5f89f718b', $event->uuid->toString());
        self::assertInstanceOf(Email::class, $event->email);
    }

    /**
     * @test
     *
     * @group unit
     *
     * @throws \App\Shared\Domain\Exception\DateTimeException
     * @throws \Assert\AssertionFailedException
     * @throws \Throwable
     */
    public function event_should_fail_when_deserialize_with_wrong_data(): void
    {
        $this->expectException(\InvalidArgumentException::class);

        UserEmailChanged::deserialize([
            'uuids' => 'eb62dfdc-2086-11e8-b467-0ed5f89f718b',
            'emails' => 'asd@asd.asd',
            'updated_at' => DateTime::now()->toString(),
        ]);
    }

    /**
     * @test
     *
     * @group unit
     *
     * @throws \App\Shared\Domain\Exception\DateTimeException
     * @throws \Assert\AssertionFailedException
     * @throws \Throwable
     */
    public function event_should_be_serializable(): void
    {
        $event = UserEmailChanged::deserialize([
            'uuid' => 'eb62dfdc-2086-11e8-b467-0ed5f89f718b',
            'email' => 'asd@asd.asd',
            'updated_at' => DateTime::now()->toString(),
        ]);

        $serialized = $event->serialize();

        self::assertArrayHasKey('uuid', $serialized);
        self::assertArrayHasKey('email', $serialized);
    }
}
```

## File: `tests/App/User/Domain/Event/UserSignedInTest.php`
```php
<?php

declare(strict_types=1);

namespace Tests\App\User\Domain\Event;

use App\User\Domain\Event\UserSignedIn;
use App\User\Domain\ValueObject\Email;
use PHPUnit\Framework\TestCase;

class UserSignedInTest extends TestCase
{
    /**
     * @test
     *
     * @group unit
     *
     * @throws \Assert\AssertionFailedException
     */
    public function event_should_be_deserializable(): void
    {
        $event = UserSignedIn::deserialize([
            'uuid' => 'eb62dfdc-2086-11e8-b467-0ed5f89f718b',
            'email' => 'an@email.com',
        ]);

        self::assertSame('eb62dfdc-2086-11e8-b467-0ed5f89f718b', $event->uuid->toString());
        self::assertInstanceOf(Email::class, $event->email);
    }

    /**
     * @test
     *
     * @group unit
     *
     * @throws \Assert\AssertionFailedException
     */
    public function event_shoud_be_serializable(): void
    {
        $event = UserSignedIn::deserialize([
            'uuid' => 'eb62dfdc-2086-11e8-b467-0ed5f89f718b',
            'email' => 'an@email.com',
        ]);

        $serialized = $event->serialize();

        self::assertArrayHasKey('uuid', $serialized);
        self::assertArrayHasKey('email', $serialized);
    }

    /**
     * @test
     *
     * @group unit
     *
     * @throws \Assert\AssertionFailedException
     */
    public function event_should_fail_when_deserialize_with_incorrect_data(): void
    {
        $this->expectException(\InvalidArgumentException::class);

        UserSignedIn::deserialize([
            'notAnUuid' => 'eb62dfdc-2086-11e8-b467-0ed5f89f718b',
            'notAnEmail' => 'an@email.com',
        ]);
    }
}
```

## File: `tests/App/User/Domain/ValueObject/EmailTest.php`
```php
<?php

declare(strict_types=1);

namespace Tests\App\User\Domain\ValueObject;

use App\User\Domain\ValueObject\Email;
use PHPUnit\Framework\TestCase;

class EmailTest extends TestCase
{
    /**
     * @test
     *
     * @group unit
     *
     * @throws \Assert\AssertionFailedException
     */
    public function invalid_email_should_throw_an_exception(): void
    {
        $this->expectException(\InvalidArgumentException::class);

        Email::fromString('asd');
    }

    /**
     * @test
     *
     * @group unit
     *
     * @throws \Assert\AssertionFailedException
     */
    public function valid_email_should_be_able_to_convert_to_string(): void
    {
        $email = Email::fromString('an@email.com');

        self::assertSame('an@email.com', $email->toString());
        self::assertSame('an@email.com', (string) $email);
    }
}
```

## File: `tests/App/User/Domain/ValueObject/Auth/HashedPasswordTest.php`
```php
<?php

declare(strict_types=1);

namespace Tests\App\User\Domain\ValueObject\Auth;

use App\User\Domain\ValueObject\Auth\HashedPassword;
use PHPUnit\Framework\TestCase;

class HashedPasswordTest extends TestCase
{
    /**
     * @test
     *
     * @group unit
     */
    public function encoded_password_should_be_validated(): void
    {
        $pass = HashedPassword::encode('1234567890');

        self::assertTrue($pass->match('1234567890'));
    }

    /**
     * @test
     *
     * @group unit
     */
    public function min_6_password_length(): void
    {
        $this->expectException(\InvalidArgumentException::class);

        HashedPassword::encode('12345');
    }

    /**
     * @test
     *
     * @group unit
     */
    public function from_hash_password_should_still_valid(): void
    {
        $pass = HashedPassword::fromHash((string) HashedPassword::encode('1234567890'));

        self::assertTrue($pass->match('1234567890'));
    }
}
```

## File: `tests/UI/Cli/AbstractConsoleTestCase.php`
```php
<?php

declare(strict_types=1);

namespace Tests\UI\Cli;

use Symfony\Bundle\FrameworkBundle\Console\Application;
use Symfony\Component\Console\Command\Command;
use Symfony\Component\Console\Tester\CommandTester;
use Tests\App\Shared\Application\ApplicationTestCase;

class AbstractConsoleTestCase extends ApplicationTestCase
{
    final protected function app(Command $command, string $alias): CommandTester
    {
        $kernel = self::bootKernel();
        $application = new Application($kernel);
        $application->add($command);

        $command = $application->find($alias);

        return new CommandTester($command);
    }
}
```

## File: `tests/UI/Cli/Command/CreateUserCommandTest.php`
```php
<?php

declare(strict_types=1);

namespace Tests\UI\Cli\Command;

use App\Shared\Application\Command\CommandBusInterface;
use App\Shared\Application\Query\Item;
use App\User\Application\Query\User\FindByEmail\FindByEmailQuery;
use Assert\AssertionFailedException;
use Ramsey\Uuid\Uuid;
use Tests\UI\Cli\AbstractConsoleTestCase;
use Throwable;
use UI\Cli\Command\CreateUserCommand;

class CreateUserCommandTest extends AbstractConsoleTestCase
{
    /**
     * @test
     *
     * @group e2e
     *
     * @throws Throwable
     * @throws AssertionFailedException
     */
    public function command_integration_with_bus_success(): void
    {
        $email = 'jorge.arcoma@gmail.com';

        /** @var CommandBusInterface $commandBus */
        $commandBus = $this->service(CommandBusInterface::class);
        $commandTester = $this->app($command = new CreateUserCommand($commandBus), 'app:create-user');

        $commandTester->execute([
            'command' => $command->getName(),
            'uuid' => Uuid::uuid4()->toString(),
            'email' => $email,
            'password' => 'jorgepass',
        ]);

        $output = $commandTester->getDisplay();

        $this->assertStringContainsString('User Created:', $output);
        $this->assertStringContainsString('Email: jorge.arcoma@gmail.com', $output);

        /** @var Item $result */
        $result = $this->ask(new FindByEmailQuery($email));

        self::assertInstanceOf(Item::class, $result);
        self::assertSame('UserView', $result->type);
        self::assertSame($email, $result->resource['credentials.email']->toString());
    }
}
```

## File: `tests/UI/Http/Rest/Controller/JsonApiTestCase.php`
```php
<?php

declare(strict_types=1);

namespace Tests\UI\Http\Rest\Controller;

use App\Shared\Infrastructure\Bus\Command\MessengerCommandBus;
use App\User\Application\Command\SignUp\SignUpCommand;
use Assert\AssertionFailedException;
use Ramsey\Uuid\Uuid;
use Ramsey\Uuid\UuidInterface;
use Symfony\Bundle\FrameworkBundle\KernelBrowser;
use Symfony\Bundle\FrameworkBundle\Test\WebTestCase;
use Symfony\Component\EventDispatcher\EventDispatcher;
use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\HttpKernel\Event\TerminateEvent;
use Symfony\Component\HttpKernel\KernelEvents;
use Throwable;

abstract class JsonApiTestCase extends WebTestCase
{
    public const DEFAULT_EMAIL = 'lol@lo.com';

    public const DEFAULT_PASS = '1234567890';

    protected ?KernelBrowser $cli;

    private ?string $token = null;

    protected ?UuidInterface $userUuid = null;

    protected function setUp(): void
    {
        self::ensureKernelShutdown();
        $this->cli = static::createClient();
    }

    /**
     * @throws AssertionFailedException
     * @throws Throwable
     */
    protected function createUser(string $email = self::DEFAULT_EMAIL, string $password = self::DEFAULT_PASS): string
    {
        $this->userUuid = Uuid::uuid4();

        $signUp = new SignUpCommand(
            $this->userUuid->toString(),
            $email,
            $password
        );

        /** @var MessengerCommandBus $commandBus */
        $commandBus = $this->getContainer()->get(MessengerCommandBus::class);

        $commandBus->handle($signUp);

        return $email;
    }

    protected function post(string $uri, array $params): void
    {
        $this->cli->request(
            'POST',
            $uri,
            [],
            [],
            $this->headers(),
            (string) \json_encode($params, JSON_THROW_ON_ERROR)
        );
    }

    protected function get(string $uri, array $parameters = []): void
    {
        $this->cli->request(
            'GET',
            $uri,
            $parameters,
            [],
            $this->headers()
        );
    }

    protected function auth(string $username = self::DEFAULT_EMAIL, string $password = self::DEFAULT_PASS): void
    {
        $this->post('/api/auth_check', [
            '_username' => $username ?: self::DEFAULT_EMAIL,
            '_password' => $password ?: self::DEFAULT_PASS,
        ]);

        /** @var string $content */
        $content = $this->cli->getResponse()->getContent();

        $response = \json_decode($content, true, 512, JSON_THROW_ON_ERROR);

        $this->token = $response['token'];
    }

    protected function logout(): void
    {
        $this->token = null;
    }

    private function headers(): array
    {
        $headers = [
            'CONTENT_TYPE' => 'application/json',
        ];

        if ($this->token) {
            $headers['HTTP_Authorization'] = 'Bearer ' . $this->token;
        }

        return $headers;
    }

    protected function fireTerminateEvent(): void
    {
        /** @var EventDispatcher $dispatcher */
        $dispatcher = $this->cli->getContainer()->get('event_dispatcher');

        $dispatcher->dispatch(
            new TerminateEvent(
                static::$kernel,
                Request::create('/'),
                new Response()
            ),
            KernelEvents::TERMINATE
        );
    }

    protected function tearDown(): void
    {
        parent::tearDown();
        $this->cli = null;
        $this->token = null;
        $this->userUuid = null;
    }
}
```

## File: `tests/UI/Http/Rest/Controller/Auth/CheckControllerTest.php`
```php
<?php

declare(strict_types=1);

namespace Tests\UI\Http\Rest\Controller\Auth;

use Tests\UI\Http\Rest\Controller\JsonApiTestCase;
use Symfony\Component\HttpFoundation\Response;

class CheckControllerTest extends JsonApiTestCase
{
    /**
     * @test
     *
     * @group e2e
     */
    public function bad_credentials_must_fail_with_401(): void
    {
        $this->post('/api/auth_check', [
            '_username' => 'oze@lol.com',
            '_password' => 'qwer',
        ]);

        self::assertSame(Response::HTTP_UNAUTHORIZED, $this->cli->getResponse()->getStatusCode());
    }

    /**
     * @test
     *
     * @group e2e
     */
    public function email_must_be_valid_or_fail_with_400(): void
    {
        $this->post('/api/auth_check', [
            '_username' => 'oze@',
            '_password' => 'qwer',
        ]);

        self::assertSame(Response::HTTP_BAD_REQUEST, $this->cli->getResponse()->getStatusCode());
    }
}
```

## File: `tests/UI/Http/Rest/Controller/Events/GetEventsControllerTest.php`
```php
<?php

declare(strict_types=1);

namespace Tests\UI\Http\Rest\Controller\Events;

use App\Shared\Infrastructure\Event\ReadModel\ElasticSearchEventRepository;
use Tests\UI\Http\Rest\Controller\JsonApiTestCase;
use Assert\AssertionFailedException;
use Exception;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Messenger\EventListener\StopWorkerOnMessageLimitListener;
use Symfony\Component\Messenger\Worker;
use Throwable;

class GetEventsControllerTest extends JsonApiTestCase
{
    private ?Worker $worker = null;

    /**
     * @throws AssertionFailedException
     * @throws Throwable
     */
    protected function setUp(): void
    {
        parent::setUp();

        /** @var ElasticSearchEventRepository $eventReadStore */
        $eventReadStore = $this->getContainer()->get(ElasticSearchEventRepository::class);

        $eventReadStore->reboot();

        $this->createUser();
        $this->auth();
        $this->fireTerminateEvent();
        $eventDispatcher = $this->getContainer()->get('event_dispatcher');
        $eventDispatcher->addSubscriber(new StopWorkerOnMessageLimitListener(2));
        $this->worker = new Worker(
            [
                'events' => $this->getContainer()->get('messenger.transport.events'),
                'users' => $this->getContainer()->get('messenger.transport.users'),
            ],
            $this->getContainer()->get('messenger.bus.event.async'),
            $eventDispatcher,
            $this->getContainer()->get('logger')
        );

        $this->worker->run();
        $this->refreshIndex();
    }

    /**
     * @test
     *
     * @group e2e
     */
    public function events_list_must_return_404_when_no_page_found(): void
    {
        $this->get('/api/events?page=100');

        self::assertSame(Response::HTTP_NOT_FOUND, $this->cli->getResponse()->getStatusCode());
    }

    /**
     * @test
     *
     * @group e2e
     *
     * @throws Exception
     */
    public function user_was_created_and_sign_in_events_should_be_present_in_elastic_search(): void
    {
        $this->get('/api/events', ['limit' => 2]);
        self::assertSame(Response::HTTP_OK, $this->cli->getResponse()->getStatusCode());

        /** @var string $content */
        $content = $this->cli->getResponse()->getContent();

        $responseDecoded = \json_decode($content, true, 512, JSON_THROW_ON_ERROR);

        self::assertSame(2, $responseDecoded['meta']['total']);
        self::assertSame(1, $responseDecoded['meta']['page']);
        self::assertSame(2, $responseDecoded['meta']['size']);

        self::assertSame('App.User.Domain.Event.UserWasCreated', $responseDecoded['data'][0]['type']);
        self::assertSame(self::DEFAULT_EMAIL, $responseDecoded['data'][0]['payload']['credentials']['email']);
        self::assertSame('App.User.Domain.Event.UserSignedIn', $responseDecoded['data'][1]['type']);
        self::assertSame(self::DEFAULT_EMAIL, $responseDecoded['data'][1]['payload']['email']);
    }

    /**
     * @test
     *
     * @group e2e
     */
    public function given_invalid_page_returns_400_status(): void
    {
        $this->get('/api/events?page=two');

        self::assertSame(Response::HTTP_BAD_REQUEST, $this->cli->getResponse()->getStatusCode());
    }

    /**
     * @test
     *
     * @group e2e
     */
    public function given_invalid_limit_returns_400_status(): void
    {
        $this->get('/api/events?limit=three');

        self::assertSame(Response::HTTP_BAD_REQUEST, $this->cli->getResponse()->getStatusCode());
    }

    private function refreshIndex(): void
    {
        /** @var ElasticSearchEventRepository $eventReadStore */
        $eventReadStore = $this->getContainer()->get(ElasticSearchEventRepository::class);
        $eventReadStore->refresh();
    }

    protected function tearDown(): void
    {
        /** @var ElasticSearchEventRepository $eventReadStore */
        $eventReadStore = $this->getContainer()->get(ElasticSearchEventRepository::class);
        $eventReadStore->delete();
        if ($this->worker) {
            $this->worker->stop();
        }
        parent::tearDown();
    }
}
```

## File: `tests/UI/Http/Rest/Controller/Healthz/HealthzControllerTest.php`
```php
<?php

declare(strict_types=1);

namespace Tests\UI\Http\Rest\Controller\Healthz;

use Tests\UI\Http\Rest\Controller\JsonApiTestCase;
use Symfony\Component\HttpFoundation\Response;

class HealthzControllerTest extends JsonApiTestCase
{
    /**
     * @test
     *
     * @group e2e
     */
    public function events_list_must_return_404_when_no_page_found(): void
    {
        $this->get('/api/healthz');

        self::assertSame(Response::HTTP_OK, $this->cli->getResponse()->getStatusCode());
    }
}
```

## File: `tests/UI/Http/Rest/Controller/User/ChangeEmailControllerTest.php`
```php
<?php

declare(strict_types=1);

namespace Tests\UI\Http\Rest\Controller\User;

use App\User\Domain\Event\UserEmailChanged;
use Tests\App\Shared\Infrastructure\Event\EventCollectorListener;
use Broadway\Domain\DomainMessage;
use Exception;
use Ramsey\Uuid\Uuid;
use Symfony\Component\HttpFoundation\Response;
use Tests\UI\Http\Rest\Controller\JsonApiTestCase;
use Throwable;

class ChangeEmailControllerTest extends JsonApiTestCase
{
    /**
     * @test
     *
     * @group e2e
     *
     * @throws Exception
     */
    public function given_a_valid_uuid_and_email_should_return_a_201_status_code(): void
    {
        $this->post('/api/users/' . $this->userUuid->toString() . '/email', [
            'email' => 'weba@jo.com',
        ]);

        self::assertSame(Response::HTTP_OK, $this->cli->getResponse()->getStatusCode());

        /** @var EventCollectorListener $eventCollector */
        $eventCollector = $this->getContainer()->get(EventCollectorListener::class);

        /** @var DomainMessage[] $events */
        $events = $eventCollector->popEvents();

        self::assertInstanceOf(UserEmailChanged::class, $events[0]->getPayload());
    }

    /**
     * @test
     *
     * @group e2e
     */
    public function given_a_valid_uuid_and_email_user_should_not_change_others_email_and_gets_401(): void
    {
        $this->post('/api/users/' . Uuid::uuid4()->toString() . '/email', [
            'email' => 'weba@jo.com',
        ]);

        self::assertSame(Response::HTTP_FORBIDDEN, $this->cli->getResponse()->getStatusCode());

        /** @var EventCollectorListener $eventCollector */
        $eventCollector = $this->getContainer()->get(EventCollectorListener::class);

        /** @var DomainMessage[] $events */
        $events = $eventCollector->popEvents();

        self::assertCount(0, $events);
    }

    /**
     * @test
     *
     * @group e2e
     *
     * @throws Exception
     */
    public function given_a_invalid__email_should_return_a_400_status_code(): void
    {
        $this->post('/api/users/' . $this->userUuid->toString() . '/email', [
            'email' => 'webajo.com',
        ]);

        self::assertSame(Response::HTTP_BAD_REQUEST, $this->cli->getResponse()->getStatusCode());
    }

    /**
     * @throws Throwable
     */
    protected function setUp(): void
    {
        parent::setUp();

        $this->createUser();
        $this->auth();
    }
}
```

## File: `tests/UI/Http/Rest/Controller/User/GetUserByEmailControllerTest.php`
```php
<?php

declare(strict_types=1);

namespace Tests\UI\Http\Rest\Controller\User;

use Tests\App\Shared\Infrastructure\Event\EventCollectorListener;
use Tests\UI\Http\Rest\Controller\JsonApiTestCase;
use Assert\AssertionFailedException;
use Symfony\Component\HttpFoundation\Response;
use Throwable;

class GetUserByEmailControllerTest extends JsonApiTestCase
{
    /**
     * @test
     *
     * @group e2e
     *
     * @throws AssertionFailedException
     * @throws Throwable
     */
    public function invalid_input_parameters_should_return_400_status_code(): void
    {
        $this->createUser();
        $this->auth();

        $this->get('/api/user/asd@');

        self::assertSame(Response::HTTP_BAD_REQUEST, $this->cli->getResponse()->getStatusCode());

        /** @var EventCollectorListener $eventCollector */
        $eventCollector = $this->getContainer()->get(EventCollectorListener::class);

        $events = $eventCollector->popEvents();

        self::assertCount(0, $events);
    }

    /**
     * @test
     *
     * @group e2e
     *
     * @throws AssertionFailedException
     * @throws Throwable
     */
    public function valid_input_parameters_should_return_404_status_code_when_not_exist(): void
    {
        $this->createUser();
        $this->auth();

        $this->get('/api/user/asd@asd.asd');

        self::assertSame(Response::HTTP_NOT_FOUND, $this->cli->getResponse()->getStatusCode());

        /** @var EventCollectorListener $eventCollector */
        $eventCollector = $this->getContainer()->get(EventCollectorListener::class);

        $events = $eventCollector->popEvents();

        self::assertCount(0, $events);
    }

    /**
     * @test
     *
     * @group e2e
     *
     * @throws AssertionFailedException
     * @throws Throwable
     */
    public function valid_input_parameters_should_return_200_status_code_when_exist(): void
    {
        $emailString = $this->createUser();
        $this->auth();

        $this->get('/api/user/' . $emailString);

        self::assertSame(Response::HTTP_OK, $this->cli->getResponse()->getStatusCode());

        $response = \json_decode($this->cli->getResponse()->getContent(), true, 512, JSON_THROW_ON_ERROR);

        self::assertArrayHasKey('data', $response);
        self::assertArrayHasKey('id', $response['data']);
        self::assertArrayHasKey('type', $response['data']);
        self::assertArrayHasKey('attributes', $response['data']);
        self::assertArrayHasKey('uuid', $response['data']['attributes']);
        self::assertArrayHasKey('credentials.email', $response['data']['attributes']);
        self::assertArrayHasKey('createdAt', $response['data']['attributes']);
        self::assertEquals($emailString, $response['data']['attributes']['credentials.email']);

        /** @var EventCollectorListener $eventCollector */
        $eventCollector = $this->getContainer()->get(EventCollectorListener::class);

        $events = $eventCollector->popEvents();

        self::assertCount(0, $events);
    }
}
```

## File: `tests/UI/Http/Rest/Controller/User/SignUpControllerTest.php`
```php
<?php

declare(strict_types=1);

namespace Tests\UI\Http\Rest\Controller\User;

use App\User\Domain\Event\UserWasCreated;
use Tests\App\Shared\Infrastructure\Event\EventCollectorListener;
use Tests\UI\Http\Rest\Controller\JsonApiTestCase;
use Broadway\Domain\DomainMessage;
use Ramsey\Uuid\Uuid;
use Symfony\Component\HttpFoundation\Response;

class SignUpControllerTest extends JsonApiTestCase
{
    /**
     * @test
     *
     * @group e2e
     *
     * @throws \Exception
     */
    public function given_a_valid_uuid_and_email_and_password_should_return_a_201_status_code(): void
    {
        $this->post('/api/signup', [
            'uuid' => Uuid::uuid4()->toString(),
            'email' => 'jo@jo.com',
            'password' => 'oaisudaosudoaudo',
        ]);

        self::assertSame(Response::HTTP_CREATED, $this->cli->getResponse()->getStatusCode());

        /** @var EventCollectorListener $eventCollector */
        $eventCollector = $this->getContainer()->get(EventCollectorListener::class);

        /** @var DomainMessage[] $events */
        $events = $eventCollector->popEvents();

        self::assertCount(1, $events);

        $userWasCreatedEvent = $events[0];

        self::assertInstanceOf(UserWasCreated::class, $userWasCreatedEvent->getPayload());
    }

    /**
     * @test
     *
     * @group e2e
     *
     * @throws \Exception
     */
    public function given_a_email_which_used_by_other_user_should_return_a_400_status_code(): void
    {
        $this->createUser();

        $this->post('/api/signup', [
            'email' => JsonApiTestCase::DEFAULT_EMAIL,
            'password' => 'oaisudaosudoaudo',
        ]);

        self::assertSame(Response::HTTP_BAD_REQUEST, $this->cli->getResponse()->getStatusCode());

        /** @var EventCollectorListener $eventCollector */
        $eventCollector = $this->getContainer()->get(EventCollectorListener::class);

        /** @var DomainMessage[] $events */
        $events = $eventCollector->popEvents();

        self::assertCount(1, $events);

        $userWasCreatedEvent = $events[0];

        self::assertInstanceOf(UserWasCreated::class, $userWasCreatedEvent->getPayload());
    }

    /**
     * @test
     *
     * @group e2e
     *
     * @throws \Exception
     */
    public function invalid_input_parameters_should_return_400_status_code(): void
    {
        $this->post('/api/signup', [
            'uuid' => Uuid::uuid4()->toString(),
            'email' => 'invalid email',
        ]);

        self::assertSame(Response::HTTP_BAD_REQUEST, $this->cli->getResponse()->getStatusCode());

        /** @var EventCollectorListener $eventCollector */
        $eventCollector = $this->getContainer()->get(EventCollectorListener::class);

        $events = $eventCollector->popEvents();

        self::assertCount(0, $events);
    }
}
```

## File: `tests/UI/Http/Rest/EventSubscriber/JsonBodyParserSubscriberTest.php`
```php
<?php

declare(strict_types=1);

namespace Tests\UI\Http\Rest\EventSubscriber;

use UI\Http\Rest\EventSubscriber\JsonBodyParserSubscriber;
use PHPUnit\Framework\TestCase;
use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\HttpKernel\Event\RequestEvent;
use Symfony\Component\HttpKernel\HttpKernelInterface;

class JsonBodyParserSubscriberTest extends TestCase
{
    /**
     * @test
     *
     * @group unit
     */
    public function when_json_body_is_invalid(): void
    {
        $jsonBodyParserSubscriber = new JsonBodyParserSubscriber();
        $request = new Request([], [], [], [], [], [], '{"test":');
        $request->headers->set('Content-Type', 'application/json');

        $requestEvent = new RequestEvent(
            $this->createMock(HttpKernelInterface::class),
            $request,
            HttpKernelInterface::MAIN_REQUEST
        );

        $jsonBodyParserSubscriber->onKernelRequest($requestEvent);

        $response = $requestEvent->getResponse();

        self::assertEquals('Unable to parse json request.', $response->getContent());
        self::assertEquals(Response::HTTP_BAD_REQUEST, $response->getStatusCode());
    }
}
```

## File: `tests/UI/Http/Rest/Response/OpenApiResponseTest.php`
```php
<?php

declare(strict_types=1);

namespace Tests\UI\Http\Rest\Response;

use App\Shared\Application\Query\Collection;
use App\Shared\Application\Query\Item;
use App\Shared\Domain\Exception\DateTimeException;
use App\Shared\Domain\ValueObject\DateTime;
use App\User\Domain\ValueObject\Email;
use App\User\Infrastructure\ReadModel\UserView;
use UI\Http\Rest\Response\OpenApi;
use Assert\AssertionFailedException;
use Exception;
use PHPUnit\Framework\TestCase;
use Ramsey\Uuid\Uuid;
use Ramsey\Uuid\UuidInterface;

class OpenApiResponseTest extends TestCase
{
    /**
     * @test
     *
     * @group unit
     *
     * @throws Exception
     * @throws AssertionFailedException
     */
    public function format_collection(): void
    {
        $users = [
            Item::fromSerializable(self::createUserView(Uuid::uuid4(), Email::fromString('asd1@asd.asd'))),
            Item::fromSerializable(self::createUserView(Uuid::uuid4(), Email::fromString('asd2@asd.asd'))),
        ];

        $response = \json_decode(OpenApi::collection(new Collection(1, 10, \count($users), $users))->getContent(), true, 512, JSON_THROW_ON_ERROR);

        self::assertArrayHasKey('data', $response);
        self::assertArrayHasKey('meta', $response);
        self::assertArrayHasKey('total', $response['meta']);
        self::assertArrayHasKey('page', $response['meta']);
        self::assertArrayHasKey('size', $response['meta']);
        self::assertCount(2, $response['data']);
    }

    /**
     * @test
     *
     * @group unit
     *
     * @throws AssertionFailedException
     * @throws Exception
     */
    public function format_one_output(): void
    {
        $userView = self::createUserView(Uuid::uuid4(), Email::fromString('demo@asd.asd'));

        $response = \json_decode(OpenApi::one(Item::fromSerializable($userView))->getContent(), true, 512, JSON_THROW_ON_ERROR);

        self::assertArrayHasKey('data', $response);
        self::assertSame('UserView', $response['data']['type']);
        self::assertCount(2, $response['data']['attributes']);
    }

    /**
     * @throws DateTimeException
     * @throws AssertionFailedException
     */
    private static function createUserView(UuidInterface $uuid, Email $email): UserView
    {
        return UserView::deserialize([
            'uuid' => $uuid->toString(),
            'credentials' => [
                'email' => $email->toString(),
                'password' => 'ljalsjdlajsdljlajsd',
            ],
            'created_at' => DateTime::now()->toString(),
            'updated_at' => DateTime::now()->toString(),
        ]);
    }
}
```

## File: `tests/UI/Http/Web/Controller/HomeControllerTest.php`
```php
<?php

declare(strict_types=1);

namespace Tests\App\UI\Http\Web\Controller;

use Symfony\Bundle\FrameworkBundle\Test\WebTestCase;

class HomeControllerTest extends WebTestCase
{
    /**
     * @test
     *
     * @group e2e
     */
    public function home_should_have_link_to_sign_up(): void
    {
        self::ensureKernelShutdown();
        $client = self::createClient();

        $crawler = $client->request('GET', '/');

        $this->assertGreaterThan(0, $crawler->filter('html:contains("Hello!")')->count());
        $this->assertGreaterThan(0, $crawler->filter('html:contains("Sign up")')->count());
    }

    /**
     * @test
     *
     * @group e2e
     */
    public function sign_up_button_should_redirect_to_sign_up_page(): void
    {
        self::ensureKernelShutdown();
        $client = self::createClient();

        $crawler = $client->request('GET', '/');

        $link = $crawler->selectLink('Sign up')->link();

        $crawler = $client->click($link);

        $this->assertGreaterThan('/sign-up', $crawler->getUri());
    }
}
```

## File: `tests/UI/Http/Web/Controller/ProfileControllerTest.php`
```php
<?php

declare(strict_types=1);

namespace Tests\App\UI\Http\Web\Controller;

use Symfony\Bundle\FrameworkBundle\Test\WebTestCase;
use Symfony\Component\HttpFoundation\RedirectResponse;
use Symfony\Component\HttpFoundation\Response;

class ProfileControllerTest extends WebTestCase
{
    /**
     * @test
     *
     * @group e2e
     */
    public function anon_user_should_be_redirected_to_sign_in(): void
    {
        self::ensureKernelShutdown();
        $client = self::createClient();

        $client->request('GET', '/profile');

        /** @var RedirectResponse $response */
        $response = $client->getResponse();
        $this->assertSame(Response::HTTP_FOUND, $response->getStatusCode());
        $this->assertStringContainsString('/sign-in', $response->getTargetUrl());
    }
}
```

## File: `tests/UI/Http/Web/Controller/SecurityControllerTest.php`
```php
<?php

declare(strict_types=1);

namespace Tests\App\UI\Http\Web\Controller;

use Symfony\Bundle\FrameworkBundle\KernelBrowser;
use Symfony\Bundle\FrameworkBundle\Test\WebTestCase;

class SecurityControllerTest extends WebTestCase
{
    /**
     * @test
     *
     * @group e2e
     */
    public function sign_in_after_create_user(): void
    {

        $client = $this->createUser('jorge@gmail.com', 'crqs-demo');

        self::ensureKernelShutdown();

        $crawler = $client->request('GET', '/sign-in');
        $form = $crawler->selectButton('Sign in')->form();

        $form->get('_email')->setValue('jorge@gmail.com');
        $form->get('_password')->setValue('crqs-demo');

        $client->submit($form);

        $crawler = $client->followRedirect();

        self::assertSame('/profile', \parse_url($crawler->getUri(), \PHP_URL_PATH));
        self::assertSame(1, $crawler->filter('html:contains("Hi jorge@gmail.com")')->count());

    }

    /**
     * @test
     *
     * @group e2e
     */
    public function logout_should_remove_session_and_profile_redirect_sign_in(): void
    {
        $client = $this->createUser('jorge@gmail.com');

        self::ensureKernelShutdown();

        $crawler = $client->request('GET', '/sign-in');

        $form = $crawler->selectButton('Sign in')->form();

        $form->get('_email')->setValue('jorge@gmail.com');
        $form->get('_password')->setValue('crqs-demo');

        $client->submit($form);

        $crawler = $client->followRedirect();
        self::assertSame('/profile', \parse_url($crawler->getUri(), \PHP_URL_PATH));

        $client->click($crawler->selectLink('Exit')->link());

        $crawler = $client->followRedirect();
        self::assertSame('/', \parse_url($crawler->getUri(), \PHP_URL_PATH));

        $client->request('GET', '/profile');

        $crawler = $client->followRedirect();
        self::assertSame('/sign-in', \parse_url($crawler->getUri(), \PHP_URL_PATH));
    }

    /**
     * @test
     *
     * @group e2e
     */
    public function login_should_display_an_error_when_bad_credentials(): void
    {
        self::ensureKernelShutdown();
        $client = self::createClient();

        $crawler = $client->request('GET', '/sign-in');

        $form = $crawler->selectButton('Sign in')->form();

        $form->get('_email')->setValue('an@email.com');
        $form->get('_password')->setValue('password-so-safe');

        $client->submit($form);

        $crawler = $client->followRedirect();
        self::assertSame(1, $crawler->filter('html:contains("An authentication exception occurred.")')->count());
    }

    /**
     * @test
     *
     * @group e2e
     */
    public function login_should_display_an_error_when_bad_invalid_email(): void
    {
        self::ensureKernelShutdown();
        $client = self::createClient();

        $crawler = $client->request('GET', '/sign-in');

        $form = $crawler->selectButton('Sign in')->form();

        $form->get('_email')->setValue('an@email');
        $form->get('_password')->setValue('password-so-safe');

        $client->submit($form);

        $crawler = $client->followRedirect();
        self::assertSame(1, $crawler->filter('html:contains("An authentication exception occurred.")')->count());
    }

    private function createUser(string $email, string $password = 'crqs-demo'): KernelBrowser
    {
        self::ensureKernelShutdown();
        $client = self::createClient();

        $crawler = $client->request('GET', '/sign-up');

        $form = $crawler->selectButton('Send')->form();

        $form->get('email')->setValue($email);
        $form->get('password')->setValue($password);

        $client->submit($form);

        return $client;
    }
}
```

## File: `tests/UI/Http/Web/Controller/SignUpControllerTest.php`
```php
<?php

declare(strict_types=1);

namespace Tests\App\UI\Http\Web\Controller;

use Symfony\Bundle\FrameworkBundle\Test\WebTestCase;
use Symfony\Component\DomCrawler\Crawler;

class SignUpControllerTest extends WebTestCase
{
    /**
     * @test
     *
     * @group e2e
     */
    public function sign_up_page_form_format(): void
    {
        $client = self::createClient();

        $crawler = $client->request('GET', '/sign-up');

        $this->assertSame(1, $crawler->filter('label:contains("Email")')->count());
        $this->assertSame(1, $crawler->selectButton('Send')->count());
    }

    /**
     * @test
     *
     * @group e2e
     */
    public function sign_up_form_create_user_success(): void
    {
        $crawler = $this->createUser($email = 'ads@asd.asd');

        self::assertSame(1, $crawler->filter('html:contains("Hello ' . $email . '")')->count());
        self::assertSame(1, $crawler->filter('html:contains("Your id is ")')->count());
    }

    /**
     * @test
     *
     * @group e2e
     */
    public function sign_up_form_create_user_invalid_email(): void
    {
        $crawler = $this->createUser('jorge@gmail');

        self::assertSame(1, $crawler->filter('html:contains("Not a valid email")')->count());
    }

    /**
     * @test
     *
     * @group e2e
     */
    public function sign_up_form_create_user_with_email_already_taken(): void
    {
        $this->createUser('jorge.arcoma@gmail.com');
        $crawler = $this->createUser('jorge.arcoma@gmail.com');

        self::assertSame(1, $crawler->filter('html:contains("Email already registered.")')->count());
    }

    private function createUser(string $email, string $password = 'crqs-demo'): Crawler
    {
        self::ensureKernelShutdown();
        $client = self::createClient();

        $crawler = $client->request('GET', '/sign-up');

        $form = $crawler->selectButton('Send')->form();

        $form->get('email')->setValue($email);
        $form->get('password')->setValue($password);

        return $client->submit($form);
    }
}
```


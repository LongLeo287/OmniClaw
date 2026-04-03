---
id: github.com-franzose-symfony-ddd-wishlist-11b089fd-
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:51.469262
---

# KNOWLEDGE EXTRACT: github.com_franzose_symfony-ddd-wishlist_11b089fd
> **Extracted on:** 2026-04-01 14:17:01
> **Source:** D:/LongLeo/AI OS CORP/AI OS/core/security/QUARANTINE/KI-BATCH-20260331205007523832/github.com_franzose_symfony-ddd-wishlist_11b089fd

---

## File: `.gitignore`
```
/.idea
/.web-server-pid
/app/config/parameters.yml
/app/config/parameters_permanent.yml
/build/
/phpunit.xml
/var/*
!/var/cache
/var/cache/*
!var/cache/.gitkeep
!/var/logs
/var/logs/*
!var/logs/.gitkeep
!/var/sessions
/var/sessions/*
!var/sessions/.gitkeep
!var/SymfonyRequirements.php
/bower_components/
/node_modules/
/vendor/
/web/assets/
/web/bundles/
docker-compose.yml
```

## File: `.travis.yml`
```yaml
sudo: required
language: php
services:
  - docker
php:
  - '7.1'
  - nightly
before_install:
  - echo "extension=redis.so" >> ~/.phpenv/versions/$(phpenv version-name)/etc/php.ini
  - cp ./app/config/parameters.yml.dist ./app/config/parameters.yml
  - cp ./app/config/parameters_permanent.yml.dist ./app/config/parameters_permanent.yml
  - cp ./docker-compose.yml.dist ./docker-compose.yml
  - docker-compose up -d
install:
  - travis_retry composer install --no-interaction --prefer-source
  - npm install
script: vendor/bin/phpunit --coverage-text --coverage-clover=coverage.xml --colors
after_script:
  - wget https://scrutinizer-ci.com/ocular.phar
  - php ocular.phar code-coverage:upload --format=php-clover coverage.xml
```

## File: `LICENSE.txt`
```
The MIT License (MIT)

Copyright (c) 2017 Jan Iwanow

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
[![](https://img.shields.io/packagist/dt/franzose/symfony-ddd-wishlist.svg)](https://packagist.org/packages/franzose/symfony-ddd-wishlist)
[![](https://travis-ci.org/franzose/symfony-ddd-wishlist.svg?branch=master)](https://travis-ci.org/franzose/symfony-ddd-wishlist)
[![](https://scrutinizer-ci.com/g/franzose/symfony-ddd-wishlist/badges/quality-score.png?b=master)](https://scrutinizer-ci.com/g/franzose/symfony-ddd-wishlist?branch=master)

[На русском](https://github.com/franzose/symfony-ddd-wishlist/blob/master/README_RUS.md)

Wishlist
========

*I'm still working on the project, so some things can be unimplemented yet.*

This repository serves as an implementation of DDD, domain driven design, with usage of Symfony 3, PostgreSQL, and Redis as a backend and Vue.js/Sass as a frontend. The project is heavily inspired by [DDD Cargo Sample in PHP](https://github.com/codeliner/php-ddd-cargo-sample).

The basis for the project is a fairly simple domain, a wish list. Each wish can have its own price, daily fee and a fund which is implemented as a list of deposits to the wish. Wish can be fulfilled and is fulfilled as soon as its fund has enough money. Mistaken deposits can be removed or transfered to another wish. Any wish can have surplus funds, so they can also be transfered to other wishes.

## Installation
Clone the repository and run the following commands to install all the dependencies and build frontend scripts and styles:
```bash
cd /path/to/webroot
git clone https://github.com/franzose/symfony-ddd-wishlist.git
cd symfony-ddd-wishlist
composer self-update
composer install
npm install
./node_modules/.bin/encore dev
```

### PostgreSQL, Redis, and PHP dev server
To simplify backend setup, the project uses a couple of Docker images (so you need to install Docker too) that you'll find in `docker-compose.yml.dist` file. Run the following commands to start PostgreSQL and Redis, and also fill the database with some data:

```bash
cp ./app/config/parameters.yml.dist ./app/config/parameters.yml
cp ./app/config/parameters_permanent.yml.dist ./app/config/parameters_permanent.yml
cp ./docker-compose.yml.dist ./docker-compose.yml
docker-compose up -d
php bin/console doctrine:fixtures:load --fixtures=/path/to/src/Infrastructure/Persistence/Doctrine/Fixture/LoadWishesData.php
php bin/console server:start
```

## Project structure
TODO: write about project structure

## Support
If you have any problems using the application, please open a Github issue. The same applies to any questions or feature requests.

## Contributions
Any contribution is appreciated. This application serves as an example implementation of the domain driven design. I'd be very glad of any kind of shares of this repository being it a tweet, a post, a link, or whatever.

## Tests
The application is covered by unit and functional tests. Functional tests use SQLite database. Before running tests, please copy PHPUnit's configuration file:

```bash
cp ./phpunit.xml.dist ./phpunit.xml
```

Then use the following command to run tests:

```bash
./vendor/bin/phpunit
```
```

## File: `README_RUS.md`
```markdown
[![](https://img.shields.io/packagist/dt/franzose/symfony-ddd-wishlist.svg)](https://packagist.org/packages/franzose/symfony-ddd-wishlist)
[![](https://travis-ci.org/franzose/symfony-ddd-wishlist.svg?branch=master)](https://travis-ci.org/franzose/symfony-ddd-wishlist)
[![](https://scrutinizer-ci.com/g/franzose/symfony-ddd-wishlist/badges/quality-score.png?b=master)](https://scrutinizer-ci.com/g/franzose/symfony-ddd-wishlist?branch=master)

[In English](https://github.com/franzose/symfony-ddd-wishlist/blob/master/README.md)

Wishlist
========

*Я всё еще работаю над проектом, поэтому некоторые вещи могут оставаться нереализованными.*

Этот репозиторий посвящен реализации предметно-ориентированного проектирования (DDD) с использованием Symfony 3, PostgreSQL и Redis для серверной части, а также Vue.js/SASS для фронтенда.

За основу проекта взята довольно простая предметная область — вишлист. Это список желаний, в который можно добавлять свои желания, а также их исполнять. Каждое желание имеет свою стоимость, размер ежедневного денежного вклада и копилку, выраженную набором вкладов в это желание. Чтобы исполнить желание, необходимо вложить в него достаточное количество денег. Ошибочные вклады можно удалять, либо перенаправлять на другие желания. У желаний могут быть излишки вкладов, которые также можно перенаправлять на другие желания.

## Установка
Склонируйте репозиторий и выполните следующие команды, чтобы установить все зависимости и собрать скрипты со стилями для фронтенда:
```bash
cd /path/to/webroot
git clone https://github.com/franzose/symfony-ddd-wishlist.git
cd symfony-ddd-wishlist
composer self-update
composer install
npm install
./node_modules/.bin/encore dev
```

### PostgreSQL, Redis и dev-сервер PHP
Для упрощения разворачивания базы данных и кеша в проекте используются образы Docker (так что его тоже придётся установить), указанные в файле `docker-compose.yml.dist`. Выполните следующие команды, чтобы запустить PostgreSQL и Redis, а также заполнить базу данных начальными данными:

```bash
cp ./app/config/parameters.yml.dist ./app/config/parameters.yml
cp ./app/config/parameters_permanent.yml.dist ./app/config/parameters_permanent.yml
cp ./docker-compose.yml.dist ./docker-compose.yml
docker-compose up -d
php bin/console doctrine:fixtures:load --fixtures=/path/to/src/Infrastructure/Persistence/Doctrine/Fixture/LoadWishesData.php
php bin/console server:start
```

## Структура проекта
TODO: написать про структуру проекта

## Поддержка
Если у вас возникли какие-либо проблемы в процессе использования данного приложения, пожалуйста напишите об этом в отдельной задаче. То же касается вопросов по реализации функциональности или запросов на добавление новых возможностей.

## Собственный вклад
Любой вклад ценен. Данное приложение служит одним из примеров реализации предметно-ориентированного проектирования. Хорошим или плохим, это уже не мне решать. Поэтому я был бы очень рад распространению информации об этом репозитории в широкие массы (<s>зараспространите среди жильцов вашего ЖЭКа, как вы это любите</s>).

## Тесты
Приложение покрыто юнит- и функциональными тестами. Для функциональных тестов используется база данных SQLite. Перед запуском тестов скопируйте конфигурационный файл-образец PHPUnit:

```bash
cp ./phpunit.xml.dist ./phpunit.xml
```

Затем, чтобы запустить тесты, используйте следующую команду:

```bash
./vendor/bin/phpunit
```
```

## File: `composer.json`
```json
{
    "name": "franzose/symfony-ddd-wishlist",
    "license": "MIT",
    "type": "project",
    "keywords": ["symfony", "ddd", "vuejs", "wishlist", "sample app"],
    "description": "Wishlist, a sample application on Symfony 3 and Vue.js built with DDD in mind.",
    "autoload": {
        "psr-4": {
            "Wishlist\\": "src/"
        },
        "classmap": [
            "app/AppKernel.php",
            "app/AppCache.php"
        ]
    },
    "autoload-dev": {
        "psr-4": {
            "Wishlist\\Tests\\": "tests/"
        },
        "files": [
            "vendor/symfony/symfony/src/Symfony/Component/VarDumper/Resources/functions/dump.php"
        ]
    },
    "require": {
        "php": ">=7.1",
        "doctrine/doctrine-bundle": "^1.6",
        "doctrine/orm": "^2.5",
        "friendsofsymfony/jsrouting-bundle": "^1.6",
        "incenteev/composer-parameter-handler": "^2.0",
        "moneyphp/money": "^3.0",
        "ramsey/uuid": "^3.6",
        "ramsey/uuid-doctrine": "^1.4",
        "sensio/distribution-bundle": "^5.0.19",
        "sensio/framework-extra-bundle": "^3.0.2",
        "symfony/monolog-bundle": "^3.1.0",
        "symfony/polyfill-apcu": "^1.0",
        "symfony/swiftmailer-bundle": "^2.3.10",
        "symfony/symfony": "3.3.*",
        "twig/twig": "^1.0||^2.0",
        "webmozart/assert": "^1.2"
    },
    "require-dev": {
        "doctrine/doctrine-fixtures-bundle": "^2.3",
        "fzaninotto/faker": "^1.6",
        "liip/functional-test-bundle": "^1.8",
        "mockery/mockery": "^0.9.9",
        "phpunit/phpunit": "^6.2",
        "sensio/generator-bundle": "^3.0",
        "symfony/phpunit-bridge": "^3.0"
    },
    "scripts": {
        "symfony-scripts": [
            "Incenteev\\ParameterHandler\\ScriptHandler::buildParameters",
            "Sensio\\Bundle\\DistributionBundle\\Composer\\ScriptHandler::buildBootstrap",
            "Sensio\\Bundle\\DistributionBundle\\Composer\\ScriptHandler::clearCache",
            "Sensio\\Bundle\\DistributionBundle\\Composer\\ScriptHandler::installAssets",
            "Sensio\\Bundle\\DistributionBundle\\Composer\\ScriptHandler::installRequirementsFile",
            "Sensio\\Bundle\\DistributionBundle\\Composer\\ScriptHandler::prepareDeploymentTarget"
        ],
        "post-install-cmd": [
            "@symfony-scripts"
        ],
        "post-update-cmd": [
            "@symfony-scripts"
        ]
    },
    "config": {
        "sort-packages": true
    },
    "extra": {
        "symfony-app-dir": "app",
        "symfony-bin-dir": "bin",
        "symfony-var-dir": "var",
        "symfony-web-dir": "web",
        "symfony-tests-dir": "tests",
        "symfony-assets-install": "relative",
        "incenteev-parameters": {
            "file": "app/config/parameters.yml"
        },
        "branch-alias": null
    }
}
```

## File: `composer.lock`
```
{
    "_readme": [
        "This file locks the dependencies of your project to a known state",
        "Read more about it at https://getcomposer.org/doc/01-basic-usage.md#composer-lock-the-lock-file",
        "This file is @generated automatically"
    ],
    "content-hash": "34bec5a4620cfeae2ebed9ec0308fd04",
    "packages": [
        {
            "name": "composer/ca-bundle",
            "version": "1.0.7",
            "source": {
                "type": "git",
                "url": "https://github.com/composer/ca-bundle.git",
                "reference": "b17e6153cb7f33c7e44eb59578dc12eee5dc8e12"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/composer/ca-bundle/zipball/b17e6153cb7f33c7e44eb59578dc12eee5dc8e12",
                "reference": "b17e6153cb7f33c7e44eb59578dc12eee5dc8e12",
                "shasum": ""
            },
            "require": {
                "ext-openssl": "*",
                "ext-pcre": "*",
                "php": "^5.3.2 || ^7.0"
            },
            "require-dev": {
                "phpunit/phpunit": "^4.5",
                "psr/log": "^1.0",
                "symfony/process": "^2.5 || ^3.0"
            },
            "suggest": {
                "symfony/process": "This is necessary to reliably check whether openssl_x509_parse is vulnerable on older php versions, but can be ignored on PHP 5.5.6+"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Composer\\CaBundle\\": "src"
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
            "description": "Lets you find a path to the system CA bundle, and includes a fallback to the Mozilla CA bundle.",
            "keywords": [
                "cabundle",
                "cacert",
                "certificate",
                "ssl",
                "tls"
            ],
            "time": "2017-03-06T11:59:08+00:00"
        },
        {
            "name": "doctrine/annotations",
            "version": "v1.2.7",
            "source": {
                "type": "git",
                "url": "https://github.com/doctrine/annotations.git",
                "reference": "f25c8aab83e0c3e976fd7d19875f198ccf2f7535"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/doctrine/annotations/zipball/f25c8aab83e0c3e976fd7d19875f198ccf2f7535",
                "reference": "f25c8aab83e0c3e976fd7d19875f198ccf2f7535",
                "shasum": ""
            },
            "require": {
                "doctrine/lexer": "1.*",
                "php": ">=5.3.2"
            },
            "require-dev": {
                "doctrine/cache": "1.*",
                "phpunit/phpunit": "4.*"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.3.x-dev"
                }
            },
            "autoload": {
                "psr-0": {
                    "Doctrine\\Common\\Annotations\\": "lib/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Roman Borschel",
                    "email": "roman@code-factory.org"
                },
                {
                    "name": "Benjamin Eberlei",
                    "email": "kontakt@beberlei.de"
                },
                {
                    "name": "Guilherme Blanco",
                    "email": "guilhermeblanco@gmail.com"
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
            "description": "Docblock Annotations Parser",
            "homepage": "http://www.doctrine-project.org",
            "keywords": [
                "annotations",
                "docblock",
                "parser"
            ],
            "time": "2015-08-31T12:32:49+00:00"
        },
        {
            "name": "doctrine/cache",
            "version": "v1.6.1",
            "source": {
                "type": "git",
                "url": "https://github.com/doctrine/cache.git",
                "reference": "b6f544a20f4807e81f7044d31e679ccbb1866dc3"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/doctrine/cache/zipball/b6f544a20f4807e81f7044d31e679ccbb1866dc3",
                "reference": "b6f544a20f4807e81f7044d31e679ccbb1866dc3",
                "shasum": ""
            },
            "require": {
                "php": "~5.5|~7.0"
            },
            "conflict": {
                "doctrine/common": ">2.2,<2.4"
            },
            "require-dev": {
                "phpunit/phpunit": "~4.8|~5.0",
                "predis/predis": "~1.0",
                "satooshi/php-coveralls": "~0.6"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.6.x-dev"
                }
            },
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
                    "name": "Roman Borschel",
                    "email": "roman@code-factory.org"
                },
                {
                    "name": "Benjamin Eberlei",
                    "email": "kontakt@beberlei.de"
                },
                {
                    "name": "Guilherme Blanco",
                    "email": "guilhermeblanco@gmail.com"
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
            "description": "Caching library offering an object-oriented API for many cache backends",
            "homepage": "http://www.doctrine-project.org",
            "keywords": [
                "cache",
                "caching"
            ],
            "time": "2016-10-29T11:16:17+00:00"
        },
        {
            "name": "doctrine/collections",
            "version": "v1.3.0",
            "source": {
                "type": "git",
                "url": "https://github.com/doctrine/collections.git",
                "reference": "6c1e4eef75f310ea1b3e30945e9f06e652128b8a"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/doctrine/collections/zipball/6c1e4eef75f310ea1b3e30945e9f06e652128b8a",
                "reference": "6c1e4eef75f310ea1b3e30945e9f06e652128b8a",
                "shasum": ""
            },
            "require": {
                "php": ">=5.3.2"
            },
            "require-dev": {
                "phpunit/phpunit": "~4.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.2.x-dev"
                }
            },
            "autoload": {
                "psr-0": {
                    "Doctrine\\Common\\Collections\\": "lib/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Roman Borschel",
                    "email": "roman@code-factory.org"
                },
                {
                    "name": "Benjamin Eberlei",
                    "email": "kontakt@beberlei.de"
                },
                {
                    "name": "Guilherme Blanco",
                    "email": "guilhermeblanco@gmail.com"
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
            "description": "Collections Abstraction library",
            "homepage": "http://www.doctrine-project.org",
            "keywords": [
                "array",
                "collections",
                "iterator"
            ],
            "time": "2015-04-14T22:21:58+00:00"
        },
        {
            "name": "doctrine/common",
            "version": "v2.6.2",
            "source": {
                "type": "git",
                "url": "https://github.com/doctrine/common.git",
                "reference": "7bce00698899aa2c06fe7365c76e4d78ddb15fa3"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/doctrine/common/zipball/7bce00698899aa2c06fe7365c76e4d78ddb15fa3",
                "reference": "7bce00698899aa2c06fe7365c76e4d78ddb15fa3",
                "shasum": ""
            },
            "require": {
                "doctrine/annotations": "1.*",
                "doctrine/cache": "1.*",
                "doctrine/collections": "1.*",
                "doctrine/inflector": "1.*",
                "doctrine/lexer": "1.*",
                "php": "~5.5|~7.0"
            },
            "require-dev": {
                "phpunit/phpunit": "~4.8|~5.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "2.7.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Doctrine\\Common\\": "lib/Doctrine/Common"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Roman Borschel",
                    "email": "roman@code-factory.org"
                },
                {
                    "name": "Benjamin Eberlei",
                    "email": "kontakt@beberlei.de"
                },
                {
                    "name": "Guilherme Blanco",
                    "email": "guilhermeblanco@gmail.com"
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
            "description": "Common Library for Doctrine projects",
            "homepage": "http://www.doctrine-project.org",
            "keywords": [
                "annotations",
                "collections",
                "eventmanager",
                "persistence",
                "spl"
            ],
            "time": "2016-11-30T16:50:46+00:00"
        },
        {
            "name": "doctrine/dbal",
            "version": "v2.5.12",
            "source": {
                "type": "git",
                "url": "https://github.com/doctrine/dbal.git",
                "reference": "7b9e911f9d8b30d43b96853dab26898c710d8f44"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/doctrine/dbal/zipball/7b9e911f9d8b30d43b96853dab26898c710d8f44",
                "reference": "7b9e911f9d8b30d43b96853dab26898c710d8f44",
                "shasum": ""
            },
            "require": {
                "doctrine/common": ">=2.4,<2.8-dev",
                "php": ">=5.3.2"
            },
            "require-dev": {
                "phpunit/phpunit": "4.*",
                "symfony/console": "2.*||^3.0"
            },
            "suggest": {
                "symfony/console": "For helpful console commands such as SQL execution and import of files."
            },
            "bin": [
                "bin/doctrine-dbal"
            ],
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "2.5.x-dev"
                }
            },
            "autoload": {
                "psr-0": {
                    "Doctrine\\DBAL\\": "lib/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Roman Borschel",
                    "email": "roman@code-factory.org"
                },
                {
                    "name": "Benjamin Eberlei",
                    "email": "kontakt@beberlei.de"
                },
                {
                    "name": "Guilherme Blanco",
                    "email": "guilhermeblanco@gmail.com"
                },
                {
                    "name": "Jonathan Wage",
                    "email": "jonwage@gmail.com"
                }
            ],
            "description": "Database Abstraction Layer",
            "homepage": "http://www.doctrine-project.org",
            "keywords": [
                "database",
                "dbal",
                "persistence",
                "queryobject"
            ],
            "time": "2017-02-08T12:53:47+00:00"
        },
        {
            "name": "doctrine/doctrine-bundle",
            "version": "1.6.8",
            "source": {
                "type": "git",
                "url": "https://github.com/doctrine/DoctrineBundle.git",
                "reference": "6e96577cbbdbb5b6dcca2ff203d665976b51beb0"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/doctrine/DoctrineBundle/zipball/6e96577cbbdbb5b6dcca2ff203d665976b51beb0",
                "reference": "6e96577cbbdbb5b6dcca2ff203d665976b51beb0",
                "shasum": ""
            },
            "require": {
                "doctrine/dbal": "~2.3",
                "doctrine/doctrine-cache-bundle": "~1.2",
                "jdorn/sql-formatter": "~1.1",
                "php": ">=5.5.9",
                "symfony/console": "~2.7|~3.0|~4.0",
                "symfony/dependency-injection": "~2.7|~3.0|~4.0",
                "symfony/doctrine-bridge": "~2.7|~3.0|~4.0",
                "symfony/framework-bundle": "~2.7|~3.0|~4.0"
            },
            "require-dev": {
                "doctrine/orm": "~2.3",
                "phpunit/phpunit": "~4",
                "satooshi/php-coveralls": "^1.0",
                "symfony/phpunit-bridge": "~2.7|~3.0|~4.0",
                "symfony/property-info": "~2.8|~3.0|~4.0",
                "symfony/validator": "~2.7|~3.0|~4.0",
                "symfony/yaml": "~2.7|~3.0|~4.0",
                "twig/twig": "~1.12|~2.0"
            },
            "suggest": {
                "doctrine/orm": "The Doctrine ORM integration is optional in the bundle.",
                "symfony/web-profiler-bundle": "To use the data collector."
            },
            "type": "symfony-bundle",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.6.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Doctrine\\Bundle\\DoctrineBundle\\": ""
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Symfony Community",
                    "homepage": "http://symfony.com/contributors"
                },
                {
                    "name": "Benjamin Eberlei",
                    "email": "kontakt@beberlei.de"
                },
                {
                    "name": "Doctrine Project",
                    "homepage": "http://www.doctrine-project.org/"
                },
                {
                    "name": "Fabien Potencier",
                    "email": "fabien@symfony.com"
                }
            ],
            "description": "Symfony DoctrineBundle",
            "homepage": "http://www.doctrine-project.org",
            "keywords": [
                "database",
                "dbal",
                "orm",
                "persistence"
            ],
            "time": "2017-05-18T08:15:18+00:00"
        },
        {
            "name": "doctrine/doctrine-cache-bundle",
            "version": "1.3.0",
            "source": {
                "type": "git",
                "url": "https://github.com/doctrine/DoctrineCacheBundle.git",
                "reference": "18c600a9b82f6454d2e81ca4957cdd56a1cf3504"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/doctrine/DoctrineCacheBundle/zipball/18c600a9b82f6454d2e81ca4957cdd56a1cf3504",
                "reference": "18c600a9b82f6454d2e81ca4957cdd56a1cf3504",
                "shasum": ""
            },
            "require": {
                "doctrine/cache": "^1.4.2",
                "doctrine/inflector": "~1.0",
                "php": ">=5.3.2",
                "symfony/doctrine-bridge": "~2.2|~3.0"
            },
            "require-dev": {
                "instaclick/coding-standard": "~1.1",
                "instaclick/object-calisthenics-sniffs": "dev-master",
                "instaclick/symfony2-coding-standard": "dev-remaster",
                "phpunit/phpunit": "~4",
                "predis/predis": "~0.8",
                "satooshi/php-coveralls": "~0.6.1",
                "squizlabs/php_codesniffer": "~1.5",
                "symfony/console": "~2.2|~3.0",
                "symfony/finder": "~2.2|~3.0",
                "symfony/framework-bundle": "~2.2|~3.0",
                "symfony/phpunit-bridge": "~2.7|~3.0",
                "symfony/security-acl": "~2.3|~3.0",
                "symfony/validator": "~2.2|~3.0",
                "symfony/yaml": "~2.2|~3.0"
            },
            "suggest": {
                "symfony/security-acl": "For using this bundle to cache ACLs"
            },
            "type": "symfony-bundle",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.2.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Doctrine\\Bundle\\DoctrineCacheBundle\\": ""
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Symfony Community",
                    "homepage": "http://symfony.com/contributors"
                },
                {
                    "name": "Benjamin Eberlei",
                    "email": "kontakt@beberlei.de"
                },
                {
                    "name": "Fabio B. Silva",
                    "email": "fabio.bat.silva@gmail.com"
                },
                {
                    "name": "Guilherme Blanco",
                    "email": "guilhermeblanco@hotmail.com"
                },
                {
                    "name": "Doctrine Project",
                    "homepage": "http://www.doctrine-project.org/"
                },
                {
                    "name": "Fabien Potencier",
                    "email": "fabien@symfony.com"
                }
            ],
            "description": "Symfony Bundle for Doctrine Cache",
            "homepage": "http://www.doctrine-project.org",
            "keywords": [
                "cache",
                "caching"
            ],
            "time": "2016-01-26T17:28:51+00:00"
        },
        {
            "name": "doctrine/inflector",
            "version": "v1.1.0",
            "source": {
                "type": "git",
                "url": "https://github.com/doctrine/inflector.git",
                "reference": "90b2128806bfde671b6952ab8bea493942c1fdae"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/doctrine/inflector/zipball/90b2128806bfde671b6952ab8bea493942c1fdae",
                "reference": "90b2128806bfde671b6952ab8bea493942c1fdae",
                "shasum": ""
            },
            "require": {
                "php": ">=5.3.2"
            },
            "require-dev": {
                "phpunit/phpunit": "4.*"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.1.x-dev"
                }
            },
            "autoload": {
                "psr-0": {
                    "Doctrine\\Common\\Inflector\\": "lib/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Roman Borschel",
                    "email": "roman@code-factory.org"
                },
                {
                    "name": "Benjamin Eberlei",
                    "email": "kontakt@beberlei.de"
                },
                {
                    "name": "Guilherme Blanco",
                    "email": "guilhermeblanco@gmail.com"
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
            "description": "Common String Manipulations with regard to casing and singular/plural rules.",
            "homepage": "http://www.doctrine-project.org",
            "keywords": [
                "inflection",
                "pluralize",
                "singularize",
                "string"
            ],
            "time": "2015-11-06T14:35:42+00:00"
        },
        {
            "name": "doctrine/instantiator",
            "version": "1.0.5",
            "source": {
                "type": "git",
                "url": "https://github.com/doctrine/instantiator.git",
                "reference": "8e884e78f9f0eb1329e445619e04456e64d8051d"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/doctrine/instantiator/zipball/8e884e78f9f0eb1329e445619e04456e64d8051d",
                "reference": "8e884e78f9f0eb1329e445619e04456e64d8051d",
                "shasum": ""
            },
            "require": {
                "php": ">=5.3,<8.0-DEV"
            },
            "require-dev": {
                "athletic/athletic": "~0.1.8",
                "ext-pdo": "*",
                "ext-phar": "*",
                "phpunit/phpunit": "~4.0",
                "squizlabs/php_codesniffer": "~2.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.0.x-dev"
                }
            },
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
                    "homepage": "http://ocramius.github.com/"
                }
            ],
            "description": "A small, lightweight utility to instantiate objects in PHP without invoking their constructors",
            "homepage": "https://github.com/doctrine/instantiator",
            "keywords": [
                "constructor",
                "instantiate"
            ],
            "time": "2015-06-14T21:17:01+00:00"
        },
        {
            "name": "doctrine/lexer",
            "version": "v1.0.1",
            "source": {
                "type": "git",
                "url": "https://github.com/doctrine/lexer.git",
                "reference": "83893c552fd2045dd78aef794c31e694c37c0b8c"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/doctrine/lexer/zipball/83893c552fd2045dd78aef794c31e694c37c0b8c",
                "reference": "83893c552fd2045dd78aef794c31e694c37c0b8c",
                "shasum": ""
            },
            "require": {
                "php": ">=5.3.2"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.0.x-dev"
                }
            },
            "autoload": {
                "psr-0": {
                    "Doctrine\\Common\\Lexer\\": "lib/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Roman Borschel",
                    "email": "roman@code-factory.org"
                },
                {
                    "name": "Guilherme Blanco",
                    "email": "guilhermeblanco@gmail.com"
                },
                {
                    "name": "Johannes Schmitt",
                    "email": "schmittjoh@gmail.com"
                }
            ],
            "description": "Base library for a lexer that can be used in Top-Down, Recursive Descent Parsers.",
            "homepage": "http://www.doctrine-project.org",
            "keywords": [
                "lexer",
                "parser"
            ],
            "time": "2014-09-09T13:34:57+00:00"
        },
        {
            "name": "doctrine/orm",
            "version": "v2.5.6",
            "source": {
                "type": "git",
                "url": "https://github.com/doctrine/doctrine2.git",
                "reference": "e6c434196c8ef058239aaa0724b4aadb0107940b"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/doctrine/doctrine2/zipball/e6c434196c8ef058239aaa0724b4aadb0107940b",
                "reference": "e6c434196c8ef058239aaa0724b4aadb0107940b",
                "shasum": ""
            },
            "require": {
                "doctrine/cache": "~1.4",
                "doctrine/collections": "~1.2",
                "doctrine/common": ">=2.5-dev,<2.8-dev",
                "doctrine/dbal": ">=2.5-dev,<2.6-dev",
                "doctrine/instantiator": "~1.0.1",
                "ext-pdo": "*",
                "php": ">=5.4",
                "symfony/console": "~2.5|~3.0"
            },
            "require-dev": {
                "phpunit/phpunit": "~4.0",
                "symfony/yaml": "~2.3|~3.0"
            },
            "suggest": {
                "symfony/yaml": "If you want to use YAML Metadata Mapping Driver"
            },
            "bin": [
                "bin/doctrine",
                "bin/doctrine.php"
            ],
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "2.6.x-dev"
                }
            },
            "autoload": {
                "psr-0": {
                    "Doctrine\\ORM\\": "lib/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Roman Borschel",
                    "email": "roman@code-factory.org"
                },
                {
                    "name": "Benjamin Eberlei",
                    "email": "kontakt@beberlei.de"
                },
                {
                    "name": "Guilherme Blanco",
                    "email": "guilhermeblanco@gmail.com"
                },
                {
                    "name": "Jonathan Wage",
                    "email": "jonwage@gmail.com"
                }
            ],
            "description": "Object-Relational-Mapper for PHP",
            "homepage": "http://www.doctrine-project.org",
            "keywords": [
                "database",
                "orm"
            ],
            "time": "2016-12-18T15:42:34+00:00"
        },
        {
            "name": "fig/link-util",
            "version": "1.0.0",
            "source": {
                "type": "git",
                "url": "https://github.com/php-fig/link-util.git",
                "reference": "1a07821801a148be4add11ab0603e4af55a72fac"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/php-fig/link-util/zipball/1a07821801a148be4add11ab0603e4af55a72fac",
                "reference": "1a07821801a148be4add11ab0603e4af55a72fac",
                "shasum": ""
            },
            "require": {
                "php": ">=5.5.0",
                "psr/link": "~1.0@dev"
            },
            "require-dev": {
                "phpunit/phpunit": "^5.1",
                "squizlabs/php_codesniffer": "^2.3.1"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.0.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Fig\\Link\\": "src/"
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
            "description": "Common utility implementations for HTTP links",
            "keywords": [
                "http",
                "http-link",
                "link",
                "psr",
                "psr-13",
                "rest"
            ],
            "time": "2016-10-17T18:31:11+00:00"
        },
        {
            "name": "friendsofsymfony/jsrouting-bundle",
            "version": "1.6.0",
            "source": {
                "type": "git",
                "url": "https://github.com/FriendsOfSymfony/FOSJsRoutingBundle.git",
                "reference": "2f52d924692647db02bbcb27c159fef03bf000c9"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/FriendsOfSymfony/FOSJsRoutingBundle/zipball/2f52d924692647db02bbcb27c159fef03bf000c9",
                "reference": "2f52d924692647db02bbcb27c159fef03bf000c9",
                "shasum": ""
            },
            "require": {
                "php": ">=5.3.2",
                "symfony/console": "~2.0|3.*",
                "symfony/framework-bundle": "~2.0|3.*",
                "symfony/serializer": "~2.0|3.*",
                "willdurand/jsonp-callback-validator": "~1.0"
            },
            "require-dev": {
                "symfony/expression-language": "~2.4|3.*"
            },
            "type": "symfony-bundle",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.5-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "FOS\\JsRoutingBundle\\": ""
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "FriendsOfSymfony Community",
                    "homepage": "https://github.com/friendsofsymfony/FOSJsRoutingBundle/contributors"
                },
                {
                    "name": "William Durand",
                    "email": "william.durand1@gmail.com"
                }
            ],
            "description": "A pretty nice way to expose your Symfony2 routing to client applications.",
            "homepage": "http://friendsofsymfony.github.com",
            "keywords": [
                "Js Routing",
                "javascript",
                "routing"
            ],
            "time": "2015-10-28T15:08:39+00:00"
        },
        {
            "name": "incenteev/composer-parameter-handler",
            "version": "v2.1.2",
            "source": {
                "type": "git",
                "url": "https://github.com/Incenteev/ParameterHandler.git",
                "reference": "d7ce7f06136109e81d1cb9d57066c4d4a99cf1cc"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/Incenteev/ParameterHandler/zipball/d7ce7f06136109e81d1cb9d57066c4d4a99cf1cc",
                "reference": "d7ce7f06136109e81d1cb9d57066c4d4a99cf1cc",
                "shasum": ""
            },
            "require": {
                "php": ">=5.3.3",
                "symfony/yaml": "~2.3|~3.0"
            },
            "require-dev": {
                "composer/composer": "1.0.*@dev",
                "phpspec/prophecy-phpunit": "~1.0",
                "symfony/filesystem": "~2.2"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "2.1.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Incenteev\\ParameterHandler\\": ""
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Christophe Coevoet",
                    "email": "stof@notk.org"
                }
            ],
            "description": "Composer script handling your ignored parameter file",
            "homepage": "https://github.com/Incenteev/ParameterHandler",
            "keywords": [
                "parameters management"
            ],
            "time": "2015-11-10T17:04:01+00:00"
        },
        {
            "name": "jdorn/sql-formatter",
            "version": "v1.2.17",
            "source": {
                "type": "git",
                "url": "https://github.com/jdorn/sql-formatter.git",
                "reference": "64990d96e0959dff8e059dfcdc1af130728d92bc"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/jdorn/sql-formatter/zipball/64990d96e0959dff8e059dfcdc1af130728d92bc",
                "reference": "64990d96e0959dff8e059dfcdc1af130728d92bc",
                "shasum": ""
            },
            "require": {
                "php": ">=5.2.4"
            },
            "require-dev": {
                "phpunit/phpunit": "3.7.*"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.3.x-dev"
                }
            },
            "autoload": {
                "classmap": [
                    "lib"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Jeremy Dorn",
                    "email": "jeremy@jeremydorn.com",
                    "homepage": "http://jeremydorn.com/"
                }
            ],
            "description": "a PHP SQL highlighting library",
            "homepage": "https://github.com/jdorn/sql-formatter/",
            "keywords": [
                "highlight",
                "sql"
            ],
            "time": "2014-01-12T16:20:24+00:00"
        },
        {
            "name": "moneyphp/money",
            "version": "v3.0.5",
            "source": {
                "type": "git",
                "url": "https://github.com/moneyphp/money.git",
                "reference": "2bd76fb0ba281bd90150a747bb7a8415c7e241f3"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/moneyphp/money/zipball/2bd76fb0ba281bd90150a747bb7a8415c7e241f3",
                "reference": "2bd76fb0ba281bd90150a747bb7a8415c7e241f3",
                "shasum": ""
            },
            "require": {
                "php": ">=5.5"
            },
            "require-dev": {
                "cache/taggable-cache": "^0.4.0",
                "ext-bcmath": "*",
                "ext-gmp": "*",
                "ext-intl": "*",
                "florianv/swap": "^3.0",
                "henrikbjorn/phpspec-code-coverage": "^2.0.2",
                "moneyphp/iso-currencies": "^3.0",
                "php-http/message": "^1.4",
                "php-http/mock-client": "^0.3.3",
                "phpspec/phpspec": "^2.5",
                "phpunit/phpunit": "^4.5",
                "psr/cache": "^1.0",
                "sllh/php-cs-fixer-styleci-bridge": "^2.1"
            },
            "suggest": {
                "ext-bcmath": "Calculate without integer limits",
                "ext-gmp": "Calculate without integer limits",
                "ext-intl": "Format Money objects with intl",
                "florianv/swap": "Exchange rates library for PHP",
                "psr/cache-implementation": "Used for Currency caching"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "3.0-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Money\\": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Mathias Verraes",
                    "email": "mathias@verraes.net",
                    "homepage": "http://verraes.net"
                },
                {
                    "name": "Frederik Bosch",
                    "email": "f.bosch@genkgo.nl"
                },
                {
                    "name": "MÃ¡rk SÃ¡gi-KazÃ¡r",
                    "email": "mark.sagi-kazar@gmail.com"
                }
            ],
            "description": "PHP implementation of Fowler's Money pattern",
            "homepage": "http://verraes.net/2011/04/fowler-money-pattern-in-php/",
            "keywords": [
                "Value Object",
                "money",
                "vo"
            ],
            "time": "2017-04-26T12:54:44+00:00"
        },
        {
            "name": "monolog/monolog",
            "version": "1.23.0",
            "source": {
                "type": "git",
                "url": "https://github.com/Seldaek/monolog.git",
                "reference": "fd8c787753b3a2ad11bc60c063cff1358a32a3b4"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/Seldaek/monolog/zipball/fd8c787753b3a2ad11bc60c063cff1358a32a3b4",
                "reference": "fd8c787753b3a2ad11bc60c063cff1358a32a3b4",
                "shasum": ""
            },
            "require": {
                "php": ">=5.3.0",
                "psr/log": "~1.0"
            },
            "provide": {
                "psr/log-implementation": "1.0.0"
            },
            "require-dev": {
                "aws/aws-sdk-php": "^2.4.9 || ^3.0",
                "doctrine/couchdb": "~1.0@dev",
                "graylog2/gelf-php": "~1.0",
                "jakub-onderka/php-parallel-lint": "0.9",
                "php-amqplib/php-amqplib": "~2.4",
                "php-console/php-console": "^3.1.3",
                "phpunit/phpunit": "~4.5",
                "phpunit/phpunit-mock-objects": "2.3.0",
                "ruflin/elastica": ">=0.90 <3.0",
                "sentry/sentry": "^0.13",
                "swiftmailer/swiftmailer": "^5.3|^6.0"
            },
            "suggest": {
                "aws/aws-sdk-php": "Allow sending log messages to AWS services like DynamoDB",
                "doctrine/couchdb": "Allow sending log messages to a CouchDB server",
                "ext-amqp": "Allow sending log messages to an AMQP server (1.0+ required)",
                "ext-mongo": "Allow sending log messages to a MongoDB server",
                "graylog2/gelf-php": "Allow sending log messages to a GrayLog2 server",
                "mongodb/mongodb": "Allow sending log messages to a MongoDB server via PHP Driver",
                "php-amqplib/php-amqplib": "Allow sending log messages to an AMQP server using php-amqplib",
                "php-console/php-console": "Allow sending log messages to Google Chrome",
                "rollbar/rollbar": "Allow sending log messages to Rollbar",
                "ruflin/elastica": "Allow sending log messages to an Elastic Search server",
                "sentry/sentry": "Allow sending log messages to a Sentry server"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "2.0.x-dev"
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
                    "homepage": "http://seld.be"
                }
            ],
            "description": "Sends your logs to files, sockets, inboxes, databases and various web services",
            "homepage": "http://github.com/Seldaek/monolog",
            "keywords": [
                "log",
                "logging",
                "psr-3"
            ],
            "time": "2017-06-19T01:22:40+00:00"
        },
        {
            "name": "paragonie/random_compat",
            "version": "v2.0.10",
            "source": {
                "type": "git",
                "url": "https://github.com/paragonie/random_compat.git",
                "reference": "634bae8e911eefa89c1abfbf1b66da679ac8f54d"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/paragonie/random_compat/zipball/634bae8e911eefa89c1abfbf1b66da679ac8f54d",
                "reference": "634bae8e911eefa89c1abfbf1b66da679ac8f54d",
                "shasum": ""
            },
            "require": {
                "php": ">=5.2.0"
            },
            "require-dev": {
                "phpunit/phpunit": "4.*|5.*"
            },
            "suggest": {
                "ext-libsodium": "Provides a modern crypto API that can be used to generate random bytes."
            },
            "type": "library",
            "autoload": {
                "files": [
                    "lib/random.php"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Paragon Initiative Enterprises",
                    "email": "security@paragonie.com",
                    "homepage": "https://paragonie.com"
                }
            ],
            "description": "PHP 5.x polyfill for random_bytes() and random_int() from PHP 7",
            "keywords": [
                "csprng",
                "pseudorandom",
                "random"
            ],
            "time": "2017-03-13T16:27:32+00:00"
        },
        {
            "name": "psr/cache",
            "version": "1.0.1",
            "source": {
                "type": "git",
                "url": "https://github.com/php-fig/cache.git",
                "reference": "d11b50ad223250cf17b86e38383413f5a6764bf8"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/php-fig/cache/zipball/d11b50ad223250cf17b86e38383413f5a6764bf8",
                "reference": "d11b50ad223250cf17b86e38383413f5a6764bf8",
                "shasum": ""
            },
            "require": {
                "php": ">=5.3.0"
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
                    "homepage": "http://www.php-fig.org/"
                }
            ],
            "description": "Common interface for caching libraries",
            "keywords": [
                "cache",
                "psr",
                "psr-6"
            ],
            "time": "2016-08-06T20:24:11+00:00"
        },
        {
            "name": "psr/container",
            "version": "1.0.0",
            "source": {
                "type": "git",
                "url": "https://github.com/php-fig/container.git",
                "reference": "b7ce3b176482dbbc1245ebf52b181af44c2cf55f"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/php-fig/container/zipball/b7ce3b176482dbbc1245ebf52b181af44c2cf55f",
                "reference": "b7ce3b176482dbbc1245ebf52b181af44c2cf55f",
                "shasum": ""
            },
            "require": {
                "php": ">=5.3.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.0.x-dev"
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
                    "homepage": "http://www.php-fig.org/"
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
            "time": "2017-02-14T16:28:37+00:00"
        },
        {
            "name": "psr/link",
            "version": "1.0.0",
            "source": {
                "type": "git",
                "url": "https://github.com/php-fig/link.git",
                "reference": "eea8e8662d5cd3ae4517c9b864493f59fca95562"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/php-fig/link/zipball/eea8e8662d5cd3ae4517c9b864493f59fca95562",
                "reference": "eea8e8662d5cd3ae4517c9b864493f59fca95562",
                "shasum": ""
            },
            "require": {
                "php": ">=5.3.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.0.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Psr\\Link\\": "src/"
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
            "description": "Common interfaces for HTTP links",
            "keywords": [
                "http",
                "http-link",
                "link",
                "psr",
                "psr-13",
                "rest"
            ],
            "time": "2016-10-28T16:06:13+00:00"
        },
        {
            "name": "psr/log",
            "version": "1.0.2",
            "source": {
                "type": "git",
                "url": "https://github.com/php-fig/log.git",
                "reference": "4ebe3a8bf773a19edfe0a84b6585ba3d401b724d"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/php-fig/log/zipball/4ebe3a8bf773a19edfe0a84b6585ba3d401b724d",
                "reference": "4ebe3a8bf773a19edfe0a84b6585ba3d401b724d",
                "shasum": ""
            },
            "require": {
                "php": ">=5.3.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.0.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Psr\\Log\\": "Psr/Log/"
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
            "description": "Common interface for logging libraries",
            "homepage": "https://github.com/php-fig/log",
            "keywords": [
                "log",
                "psr",
                "psr-3"
            ],
            "time": "2016-10-10T12:19:37+00:00"
        },
        {
            "name": "psr/simple-cache",
            "version": "1.0.0",
            "source": {
                "type": "git",
                "url": "https://github.com/php-fig/simple-cache.git",
                "reference": "753fa598e8f3b9966c886fe13f370baa45ef0e24"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/php-fig/simple-cache/zipball/753fa598e8f3b9966c886fe13f370baa45ef0e24",
                "reference": "753fa598e8f3b9966c886fe13f370baa45ef0e24",
                "shasum": ""
            },
            "require": {
                "php": ">=5.3.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.0.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Psr\\SimpleCache\\": "src/"
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
            "description": "Common interfaces for simple caching",
            "keywords": [
                "cache",
                "caching",
                "psr",
                "psr-16",
                "simple-cache"
            ],
            "time": "2017-01-02T13:31:39+00:00"
        },
        {
            "name": "ramsey/uuid",
            "version": "3.6.1",
            "source": {
                "type": "git",
                "url": "https://github.com/ramsey/uuid.git",
                "reference": "4ae32dd9ab8860a4bbd750ad269cba7f06f7934e"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/ramsey/uuid/zipball/4ae32dd9ab8860a4bbd750ad269cba7f06f7934e",
                "reference": "4ae32dd9ab8860a4bbd750ad269cba7f06f7934e",
                "shasum": ""
            },
            "require": {
                "paragonie/random_compat": "^1.0|^2.0",
                "php": "^5.4 || ^7.0"
            },
            "replace": {
                "rhumsaa/uuid": "self.version"
            },
            "require-dev": {
                "apigen/apigen": "^4.1",
                "codeception/aspect-mock": "^1.0 | ^2.0",
                "doctrine/annotations": "~1.2.0",
                "goaop/framework": "1.0.0-alpha.2 | ^1.0 | ^2.1",
                "ircmaxell/random-lib": "^1.1",
                "jakub-onderka/php-parallel-lint": "^0.9.0",
                "mockery/mockery": "^0.9.4",
                "moontoast/math": "^1.1",
                "php-mock/php-mock-phpunit": "^0.3|^1.1",
                "phpunit/phpunit": "^4.7|>=5.0 <5.4",
                "satooshi/php-coveralls": "^0.6.1",
                "squizlabs/php_codesniffer": "^2.3"
            },
            "suggest": {
                "ext-libsodium": "Provides the PECL libsodium extension for use with the SodiumRandomGenerator",
                "ext-uuid": "Provides the PECL UUID extension for use with the PeclUuidTimeGenerator and PeclUuidRandomGenerator",
                "ircmaxell/random-lib": "Provides RandomLib for use with the RandomLibAdapter",
                "moontoast/math": "Provides support for converting UUID to 128-bit integer (in string form).",
                "ramsey/uuid-console": "A console application for generating UUIDs with ramsey/uuid",
                "ramsey/uuid-doctrine": "Allows the use of Ramsey\\Uuid\\Uuid as Doctrine field type."
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "3.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Ramsey\\Uuid\\": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Marijn Huizendveld",
                    "email": "marijn.huizendveld@gmail.com"
                },
                {
                    "name": "Thibaud Fabre",
                    "email": "thibaud@aztech.io"
                },
                {
                    "name": "Ben Ramsey",
                    "email": "ben@benramsey.com",
                    "homepage": "https://benramsey.com"
                }
            ],
            "description": "Formerly rhumsaa/uuid. A PHP 5.4+ library for generating RFC 4122 version 1, 3, 4, and 5 universally unique identifiers (UUID).",
            "homepage": "https://github.com/ramsey/uuid",
            "keywords": [
                "guid",
                "identifier",
                "uuid"
            ],
            "time": "2017-03-26T20:37:53+00:00"
        },
        {
            "name": "ramsey/uuid-doctrine",
            "version": "1.4.0",
            "source": {
                "type": "git",
                "url": "https://github.com/ramsey/uuid-doctrine.git",
                "reference": "8a7d64a91e58f1f76bb8a6d3167cb3d41b765c7a"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/ramsey/uuid-doctrine/zipball/8a7d64a91e58f1f76bb8a6d3167cb3d41b765c7a",
                "reference": "8a7d64a91e58f1f76bb8a6d3167cb3d41b765c7a",
                "shasum": ""
            },
            "require": {
                "doctrine/orm": "^2.5",
                "php": "^5.4 || ^7.0",
                "ramsey/uuid": "^3.0"
            },
            "require-dev": {
                "jakub-onderka/php-parallel-lint": "^0.9.0",
                "phpunit/phpunit": "^4.7 || ^5.0",
                "satooshi/php-coveralls": "^0.6.1",
                "squizlabs/php_codesniffer": "^2.3"
            },
            "type": "library",
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
                    "name": "Marijn Huizendveld",
                    "email": "marijn.huizendveld@gmail.com"
                },
                {
                    "name": "Ben Ramsey",
                    "email": "ben@benramsey.com",
                    "homepage": "http://benramsey.com"
                }
            ],
            "description": "Allow the use of a ramsey/uuid UUID as Doctrine field type.",
            "homepage": "https://github.com/ramsey/uuid-doctrine",
            "keywords": [
                "doctrine",
                "guid",
                "identifier",
                "uuid"
            ],
            "time": "2017-07-05T15:42:57+00:00"
        },
        {
            "name": "sensio/distribution-bundle",
            "version": "v5.0.20",
            "source": {
                "type": "git",
                "url": "https://github.com/sensiolabs/SensioDistributionBundle.git",
                "reference": "4b019d4c0bd64438c42e4b6b0726085b409be8d9"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sensiolabs/SensioDistributionBundle/zipball/4b019d4c0bd64438c42e4b6b0726085b409be8d9",
                "reference": "4b019d4c0bd64438c42e4b6b0726085b409be8d9",
                "shasum": ""
            },
            "require": {
                "php": ">=5.3.9",
                "sensiolabs/security-checker": "~3.0|~4.0",
                "symfony/class-loader": "~2.3|~3.0",
                "symfony/config": "~2.3|~3.0",
                "symfony/dependency-injection": "~2.3|~3.0",
                "symfony/filesystem": "~2.3|~3.0",
                "symfony/http-kernel": "~2.3|~3.0",
                "symfony/process": "~2.3|~3.0"
            },
            "type": "symfony-bundle",
            "extra": {
                "branch-alias": {
                    "dev-master": "5.0.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Sensio\\Bundle\\DistributionBundle\\": ""
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
                }
            ],
            "description": "Base bundle for Symfony Distributions",
            "keywords": [
                "configuration",
                "distribution"
            ],
            "time": "2017-05-11T16:21:03+00:00"
        },
        {
            "name": "sensio/framework-extra-bundle",
            "version": "v3.0.26",
            "source": {
                "type": "git",
                "url": "https://github.com/sensiolabs/SensioFrameworkExtraBundle.git",
                "reference": "6d6cbe971554f0a2cc84965850481eb04a2a0059"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sensiolabs/SensioFrameworkExtraBundle/zipball/6d6cbe971554f0a2cc84965850481eb04a2a0059",
                "reference": "6d6cbe971554f0a2cc84965850481eb04a2a0059",
                "shasum": ""
            },
            "require": {
                "doctrine/common": "~2.2",
                "symfony/dependency-injection": "~2.3|~3.0",
                "symfony/framework-bundle": "~2.3|~3.0"
            },
            "require-dev": {
                "doctrine/doctrine-bundle": "~1.5",
                "doctrine/orm": "~2.4,>=2.4.5",
                "symfony/asset": "~2.7|~3.0",
                "symfony/browser-kit": "~2.3|~3.0",
                "symfony/dom-crawler": "~2.3|~3.0",
                "symfony/expression-language": "~2.4|~3.0",
                "symfony/finder": "~2.3|~3.0",
                "symfony/phpunit-bridge": "~3.2",
                "symfony/psr-http-message-bridge": "^0.3",
                "symfony/security-bundle": "~2.4|~3.0",
                "symfony/templating": "~2.3|~3.0",
                "symfony/translation": "~2.3|~3.0",
                "symfony/twig-bundle": "~2.3|~3.0",
                "symfony/yaml": "~2.3|~3.0",
                "twig/twig": "~1.12|~2.0",
                "zendframework/zend-diactoros": "^1.3"
            },
            "suggest": {
                "symfony/expression-language": "",
                "symfony/psr-http-message-bridge": "To use the PSR-7 converters",
                "symfony/security-bundle": ""
            },
            "type": "symfony-bundle",
            "extra": {
                "branch-alias": {
                    "dev-master": "3.0.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Sensio\\Bundle\\FrameworkExtraBundle\\": ""
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
                }
            ],
            "description": "This bundle provides a way to configure your controllers with annotations",
            "keywords": [
                "annotations",
                "controllers"
            ],
            "time": "2017-05-11T17:01:57+00:00"
        },
        {
            "name": "sensiolabs/security-checker",
            "version": "v4.0.4",
            "source": {
                "type": "git",
                "url": "https://github.com/sensiolabs/security-checker.git",
                "reference": "9e69eddf3bc49d1ee5c7908564da3141796d4bbc"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sensiolabs/security-checker/zipball/9e69eddf3bc49d1ee5c7908564da3141796d4bbc",
                "reference": "9e69eddf3bc49d1ee5c7908564da3141796d4bbc",
                "shasum": ""
            },
            "require": {
                "composer/ca-bundle": "^1.0",
                "symfony/console": "~2.7|~3.0"
            },
            "bin": [
                "security-checker"
            ],
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "4.0-dev"
                }
            },
            "autoload": {
                "psr-0": {
                    "SensioLabs\\Security": ""
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
            "description": "A security checker for your composer.lock",
            "time": "2017-03-31T14:50:32+00:00"
        },
        {
            "name": "swiftmailer/swiftmailer",
            "version": "v5.4.8",
            "source": {
                "type": "git",
                "url": "https://github.com/swiftmailer/swiftmailer.git",
                "reference": "9a06dc570a0367850280eefd3f1dc2da45aef517"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/swiftmailer/swiftmailer/zipball/9a06dc570a0367850280eefd3f1dc2da45aef517",
                "reference": "9a06dc570a0367850280eefd3f1dc2da45aef517",
                "shasum": ""
            },
            "require": {
                "php": ">=5.3.3"
            },
            "require-dev": {
                "mockery/mockery": "~0.9.1",
                "symfony/phpunit-bridge": "~3.2"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "5.4-dev"
                }
            },
            "autoload": {
                "files": [
                    "lib/swift_required.php"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Chris Corbyn"
                },
                {
                    "name": "Fabien Potencier",
                    "email": "fabien@symfony.com"
                }
            ],
            "description": "Swiftmailer, free feature-rich PHP mailer",
            "homepage": "http://swiftmailer.org",
            "keywords": [
                "email",
                "mail",
                "mailer"
            ],
            "time": "2017-05-01T15:54:03+00:00"
        },
        {
            "name": "symfony/monolog-bundle",
            "version": "v3.1.0",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/monolog-bundle.git",
                "reference": "6f96c7dbb6b2ef70b307a1a6f897153cbca3da47"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/monolog-bundle/zipball/6f96c7dbb6b2ef70b307a1a6f897153cbca3da47",
                "reference": "6f96c7dbb6b2ef70b307a1a6f897153cbca3da47",
                "shasum": ""
            },
            "require": {
                "monolog/monolog": "~1.22",
                "php": ">=5.3.2",
                "symfony/config": "~2.7|~3.0",
                "symfony/dependency-injection": "~2.7|~3.0",
                "symfony/http-kernel": "~2.7|~3.0",
                "symfony/monolog-bridge": "~2.7|~3.0"
            },
            "require-dev": {
                "phpunit/phpunit": "^4.8",
                "symfony/console": "~2.3|~3.0",
                "symfony/yaml": "~2.3|~3.0"
            },
            "type": "symfony-bundle",
            "extra": {
                "branch-alias": {
                    "dev-master": "3.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Bundle\\MonologBundle\\": ""
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Symfony Community",
                    "homepage": "http://symfony.com/contributors"
                },
                {
                    "name": "Fabien Potencier",
                    "email": "fabien@symfony.com"
                }
            ],
            "description": "Symfony MonologBundle",
            "homepage": "http://symfony.com",
            "keywords": [
                "log",
                "logging"
            ],
            "time": "2017-03-26T11:55:59+00:00"
        },
        {
            "name": "symfony/polyfill-apcu",
            "version": "v1.4.0",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/polyfill-apcu.git",
                "reference": "2e7965b8cdfbba50d0092d3f6dca97dddec409e2"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/polyfill-apcu/zipball/2e7965b8cdfbba50d0092d3f6dca97dddec409e2",
                "reference": "2e7965b8cdfbba50d0092d3f6dca97dddec409e2",
                "shasum": ""
            },
            "require": {
                "php": ">=5.3.3"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.4-dev"
                }
            },
            "autoload": {
                "files": [
                    "bootstrap.php"
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
            "description": "Symfony polyfill backporting apcu_* functions to lower PHP versions",
            "homepage": "https://symfony.com",
            "keywords": [
                "apcu",
                "compatibility",
                "polyfill",
                "portable",
                "shim"
            ],
            "time": "2017-06-09T08:25:21+00:00"
        },
        {
            "name": "symfony/polyfill-intl-icu",
            "version": "v1.4.0",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/polyfill-intl-icu.git",
                "reference": "3191cbe0ce64987bd382daf6724af31c53daae01"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/polyfill-intl-icu/zipball/3191cbe0ce64987bd382daf6724af31c53daae01",
                "reference": "3191cbe0ce64987bd382daf6724af31c53daae01",
                "shasum": ""
            },
            "require": {
                "php": ">=5.3.3",
                "symfony/intl": "~2.3|~3.0|~4.0"
            },
            "suggest": {
                "ext-intl": "For best performance"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.4-dev"
                }
            },
            "autoload": {
                "files": [
                    "bootstrap.php"
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
            "description": "Symfony polyfill for intl's ICU-related data and classes",
            "homepage": "https://symfony.com",
            "keywords": [
                "compatibility",
                "icu",
                "intl",
                "polyfill",
                "portable",
                "shim"
            ],
            "time": "2017-06-09T08:25:21+00:00"
        },
        {
            "name": "symfony/polyfill-mbstring",
            "version": "v1.4.0",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/polyfill-mbstring.git",
                "reference": "f29dca382a6485c3cbe6379f0c61230167681937"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/polyfill-mbstring/zipball/f29dca382a6485c3cbe6379f0c61230167681937",
                "reference": "f29dca382a6485c3cbe6379f0c61230167681937",
                "shasum": ""
            },
            "require": {
                "php": ">=5.3.3"
            },
            "suggest": {
                "ext-mbstring": "For best performance"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.4-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Polyfill\\Mbstring\\": ""
                },
                "files": [
                    "bootstrap.php"
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
            "description": "Symfony polyfill for the Mbstring extension",
            "homepage": "https://symfony.com",
            "keywords": [
                "compatibility",
                "mbstring",
                "polyfill",
                "portable",
                "shim"
            ],
            "time": "2017-06-09T14:24:12+00:00"
        },
        {
            "name": "symfony/polyfill-php56",
            "version": "v1.4.0",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/polyfill-php56.git",
                "reference": "bc0b7d6cb36b10cfabb170a3e359944a95174929"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/polyfill-php56/zipball/bc0b7d6cb36b10cfabb170a3e359944a95174929",
                "reference": "bc0b7d6cb36b10cfabb170a3e359944a95174929",
                "shasum": ""
            },
            "require": {
                "php": ">=5.3.3",
                "symfony/polyfill-util": "~1.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.4-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Polyfill\\Php56\\": ""
                },
                "files": [
                    "bootstrap.php"
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
            "description": "Symfony polyfill backporting some PHP 5.6+ features to lower PHP versions",
            "homepage": "https://symfony.com",
            "keywords": [
                "compatibility",
                "polyfill",
                "portable",
                "shim"
            ],
            "time": "2017-06-09T08:25:21+00:00"
        },
        {
            "name": "symfony/polyfill-php70",
            "version": "v1.4.0",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/polyfill-php70.git",
                "reference": "032fd647d5c11a9ceab8ee8747e13b5448e93874"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/polyfill-php70/zipball/032fd647d5c11a9ceab8ee8747e13b5448e93874",
                "reference": "032fd647d5c11a9ceab8ee8747e13b5448e93874",
                "shasum": ""
            },
            "require": {
                "paragonie/random_compat": "~1.0|~2.0",
                "php": ">=5.3.3"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.4-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Polyfill\\Php70\\": ""
                },
                "files": [
                    "bootstrap.php"
                ],
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
            "description": "Symfony polyfill backporting some PHP 7.0+ features to lower PHP versions",
            "homepage": "https://symfony.com",
            "keywords": [
                "compatibility",
                "polyfill",
                "portable",
                "shim"
            ],
            "time": "2017-06-09T14:24:12+00:00"
        },
        {
            "name": "symfony/polyfill-util",
            "version": "v1.4.0",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/polyfill-util.git",
                "reference": "ebccbde4aad410f6438d86d7d261c6b4d2b9a51d"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/polyfill-util/zipball/ebccbde4aad410f6438d86d7d261c6b4d2b9a51d",
                "reference": "ebccbde4aad410f6438d86d7d261c6b4d2b9a51d",
                "shasum": ""
            },
            "require": {
                "php": ">=5.3.3"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.4-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Polyfill\\Util\\": ""
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
            "description": "Symfony utilities for portability of PHP codes",
            "homepage": "https://symfony.com",
            "keywords": [
                "compat",
                "compatibility",
                "polyfill",
                "shim"
            ],
            "time": "2017-06-09T08:25:21+00:00"
        },
        {
            "name": "symfony/swiftmailer-bundle",
            "version": "v2.6.2",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/swiftmailer-bundle.git",
                "reference": "deabc81120c2086571f7c4484ab785c5e1b84f75"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/swiftmailer-bundle/zipball/deabc81120c2086571f7c4484ab785c5e1b84f75",
                "reference": "deabc81120c2086571f7c4484ab785c5e1b84f75",
                "shasum": ""
            },
            "require": {
                "php": ">=5.3.2",
                "swiftmailer/swiftmailer": "~4.2|~5.0",
                "symfony/config": "~2.7|~3.0",
                "symfony/dependency-injection": "~2.7|~3.0",
                "symfony/http-kernel": "~2.7|~3.0"
            },
            "require-dev": {
                "symfony/console": "~2.7|~3.0",
                "symfony/framework-bundle": "~2.7|~3.0",
                "symfony/phpunit-bridge": "~3.3@dev",
                "symfony/yaml": "~2.7|~3.0"
            },
            "suggest": {
                "psr/log": "Allows logging"
            },
            "type": "symfony-bundle",
            "extra": {
                "branch-alias": {
                    "dev-master": "2.6-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Bundle\\SwiftmailerBundle\\": ""
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Symfony Community",
                    "homepage": "http://symfony.com/contributors"
                },
                {
                    "name": "Fabien Potencier",
                    "email": "fabien@symfony.com"
                }
            ],
            "description": "Symfony SwiftmailerBundle",
            "homepage": "http://symfony.com",
            "time": "2017-05-22T04:58:24+00:00"
        },
        {
            "name": "symfony/symfony",
            "version": "v3.3.4",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/symfony.git",
                "reference": "82f7cba3c272bcd266f2d27ad6f07832c2eb3a1c"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/symfony/zipball/82f7cba3c272bcd266f2d27ad6f07832c2eb3a1c",
                "reference": "82f7cba3c272bcd266f2d27ad6f07832c2eb3a1c",
                "shasum": ""
            },
            "require": {
                "doctrine/common": "~2.4",
                "fig/link-util": "^1.0",
                "php": ">=5.5.9",
                "psr/cache": "~1.0",
                "psr/container": "^1.0",
                "psr/link": "^1.0",
                "psr/log": "~1.0",
                "psr/simple-cache": "^1.0",
                "symfony/polyfill-intl-icu": "~1.0",
                "symfony/polyfill-mbstring": "~1.0",
                "symfony/polyfill-php56": "~1.0",
                "symfony/polyfill-php70": "~1.0",
                "symfony/polyfill-util": "~1.0",
                "twig/twig": "~1.34|~2.4"
            },
            "conflict": {
                "phpdocumentor/reflection-docblock": "<3.0",
                "phpdocumentor/type-resolver": "<0.2.0",
                "phpunit/phpunit": "<4.8.35|<5.4.3,>=5.0"
            },
            "provide": {
                "psr/cache-implementation": "1.0",
                "psr/container-implementation": "1.0",
                "psr/simple-cache-implementation": "1.0"
            },
            "replace": {
                "symfony/asset": "self.version",
                "symfony/browser-kit": "self.version",
                "symfony/cache": "self.version",
                "symfony/class-loader": "self.version",
                "symfony/config": "self.version",
                "symfony/console": "self.version",
                "symfony/css-selector": "self.version",
                "symfony/debug": "self.version",
                "symfony/debug-bundle": "self.version",
                "symfony/dependency-injection": "self.version",
                "symfony/doctrine-bridge": "self.version",
                "symfony/dom-crawler": "self.version",
                "symfony/dotenv": "self.version",
                "symfony/event-dispatcher": "self.version",
                "symfony/expression-language": "self.version",
                "symfony/filesystem": "self.version",
                "symfony/finder": "self.version",
                "symfony/form": "self.version",
                "symfony/framework-bundle": "self.version",
                "symfony/http-foundation": "self.version",
                "symfony/http-kernel": "self.version",
                "symfony/inflector": "self.version",
                "symfony/intl": "self.version",
                "symfony/ldap": "self.version",
                "symfony/monolog-bridge": "self.version",
                "symfony/options-resolver": "self.version",
                "symfony/process": "self.version",
                "symfony/property-access": "self.version",
                "symfony/property-info": "self.version",
                "symfony/proxy-manager-bridge": "self.version",
                "symfony/routing": "self.version",
                "symfony/security": "self.version",
                "symfony/security-bundle": "self.version",
                "symfony/security-core": "self.version",
                "symfony/security-csrf": "self.version",
                "symfony/security-guard": "self.version",
                "symfony/security-http": "self.version",
                "symfony/serializer": "self.version",
                "symfony/stopwatch": "self.version",
                "symfony/templating": "self.version",
                "symfony/translation": "self.version",
                "symfony/twig-bridge": "self.version",
                "symfony/twig-bundle": "self.version",
                "symfony/validator": "self.version",
                "symfony/var-dumper": "self.version",
                "symfony/web-link": "self.version",
                "symfony/web-profiler-bundle": "self.version",
                "symfony/web-server-bundle": "self.version",
                "symfony/workflow": "self.version",
                "symfony/yaml": "self.version"
            },
            "require-dev": {
                "cache/integration-tests": "dev-master",
                "doctrine/cache": "~1.6",
                "doctrine/data-fixtures": "1.0.*",
                "doctrine/dbal": "~2.4",
                "doctrine/doctrine-bundle": "~1.4",
                "doctrine/orm": "~2.4,>=2.4.5",
                "egulias/email-validator": "~1.2,>=1.2.8|~2.0",
                "monolog/monolog": "~1.11",
                "ocramius/proxy-manager": "~0.4|~1.0|~2.0",
                "phpdocumentor/reflection-docblock": "^3.0",
                "predis/predis": "~1.0",
                "sensio/framework-extra-bundle": "^3.0.2",
                "symfony/phpunit-bridge": "~3.2",
                "symfony/polyfill-apcu": "~1.1",
                "symfony/security-acl": "~2.8|~3.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "3.3-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Bridge\\Doctrine\\": "src/Symfony/Bridge/Doctrine/",
                    "Symfony\\Bridge\\Monolog\\": "src/Symfony/Bridge/Monolog/",
                    "Symfony\\Bridge\\ProxyManager\\": "src/Symfony/Bridge/ProxyManager/",
                    "Symfony\\Bridge\\Twig\\": "src/Symfony/Bridge/Twig/",
                    "Symfony\\Bundle\\": "src/Symfony/Bundle/",
                    "Symfony\\Component\\": "src/Symfony/Component/"
                },
                "classmap": [
                    "src/Symfony/Component/Intl/Resources/stubs"
                ],
                "exclude-from-classmap": [
                    "**/Tests/"
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
            "description": "The Symfony PHP framework",
            "homepage": "https://symfony.com",
            "keywords": [
                "framework"
            ],
            "time": "2017-07-05T13:28:34+00:00"
        },
        {
            "name": "twig/twig",
            "version": "v1.34.4",
            "source": {
                "type": "git",
                "url": "https://github.com/twigphp/Twig.git",
                "reference": "f878bab48edb66ad9c6ed626bf817f60c6c096ee"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/twigphp/Twig/zipball/f878bab48edb66ad9c6ed626bf817f60c6c096ee",
                "reference": "f878bab48edb66ad9c6ed626bf817f60c6c096ee",
                "shasum": ""
            },
            "require": {
                "php": ">=5.3.3"
            },
            "require-dev": {
                "psr/container": "^1.0",
                "symfony/debug": "~2.7",
                "symfony/phpunit-bridge": "~3.3@dev"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.34-dev"
                }
            },
            "autoload": {
                "psr-0": {
                    "Twig_": "lib/"
                },
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
                    "name": "Armin Ronacher",
                    "email": "armin.ronacher@active-4.com",
                    "role": "Project Founder"
                },
                {
                    "name": "Twig Team",
                    "homepage": "http://twig.sensiolabs.org/contributors",
                    "role": "Contributors"
                }
            ],
            "description": "Twig, the flexible, fast, and secure template language for PHP",
            "homepage": "http://twig.sensiolabs.org",
            "keywords": [
                "templating"
            ],
            "time": "2017-07-04T13:19:31+00:00"
        },
        {
            "name": "webmozart/assert",
            "version": "1.2.0",
            "source": {
                "type": "git",
                "url": "https://github.com/webmozart/assert.git",
                "reference": "2db61e59ff05fe5126d152bd0655c9ea113e550f"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/webmozart/assert/zipball/2db61e59ff05fe5126d152bd0655c9ea113e550f",
                "reference": "2db61e59ff05fe5126d152bd0655c9ea113e550f",
                "shasum": ""
            },
            "require": {
                "php": "^5.3.3 || ^7.0"
            },
            "require-dev": {
                "phpunit/phpunit": "^4.6",
                "sebastian/version": "^1.0.1"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.3-dev"
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
            "time": "2016-11-23T20:04:58+00:00"
        },
        {
            "name": "willdurand/jsonp-callback-validator",
            "version": "v1.1.0",
            "source": {
                "type": "git",
                "url": "https://github.com/willdurand/JsonpCallbackValidator.git",
                "reference": "1a7d388bb521959e612ef50c5c7b1691b097e909"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/willdurand/JsonpCallbackValidator/zipball/1a7d388bb521959e612ef50c5c7b1691b097e909",
                "reference": "1a7d388bb521959e612ef50c5c7b1691b097e909",
                "shasum": ""
            },
            "require": {
                "php": ">=5.3.0"
            },
            "require-dev": {
                "phpunit/phpunit": "~3.7"
            },
            "type": "library",
            "autoload": {
                "psr-0": {
                    "JsonpCallbackValidator": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "William Durand",
                    "email": "william.durand1@gmail.com",
                    "homepage": "http://www.willdurand.fr"
                }
            ],
            "description": "JSONP callback validator.",
            "time": "2014-01-20T22:35:06+00:00"
        }
    ],
    "packages-dev": [
        {
            "name": "doctrine/data-fixtures",
            "version": "v1.2.2",
            "source": {
                "type": "git",
                "url": "https://github.com/doctrine/data-fixtures.git",
                "reference": "17fa5bfe6ff52e35cb3d9ec37c934a2f4bd1fa2e"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/doctrine/data-fixtures/zipball/17fa5bfe6ff52e35cb3d9ec37c934a2f4bd1fa2e",
                "reference": "17fa5bfe6ff52e35cb3d9ec37c934a2f4bd1fa2e",
                "shasum": ""
            },
            "require": {
                "doctrine/common": "~2.2",
                "php": "^5.6 || ^7.0"
            },
            "conflict": {
                "doctrine/orm": "< 2.4"
            },
            "require-dev": {
                "doctrine/dbal": "^2.5.4",
                "doctrine/orm": "^2.5.4",
                "phpunit/phpunit": "^5.4.6"
            },
            "suggest": {
                "doctrine/mongodb-odm": "For loading MongoDB ODM fixtures",
                "doctrine/orm": "For loading ORM fixtures",
                "doctrine/phpcr-odm": "For loading PHPCR ODM fixtures"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.3.x-dev"
                }
            },
            "autoload": {
                "psr-0": {
                    "Doctrine\\Common\\DataFixtures": "lib/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Jonathan Wage",
                    "email": "jonwage@gmail.com"
                }
            ],
            "description": "Data Fixtures for all Doctrine Object Managers",
            "homepage": "http://www.doctrine-project.org",
            "keywords": [
                "database"
            ],
            "time": "2016-09-20T10:07:57+00:00"
        },
        {
            "name": "doctrine/doctrine-fixtures-bundle",
            "version": "2.3.0",
            "source": {
                "type": "git",
                "url": "https://github.com/doctrine/DoctrineFixturesBundle.git",
                "reference": "0f1a2f91b349e10f5c343f75ab71d23aace5b029"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/doctrine/DoctrineFixturesBundle/zipball/0f1a2f91b349e10f5c343f75ab71d23aace5b029",
                "reference": "0f1a2f91b349e10f5c343f75ab71d23aace5b029",
                "shasum": ""
            },
            "require": {
                "doctrine/data-fixtures": "~1.0",
                "doctrine/doctrine-bundle": "~1.0",
                "php": ">=5.3.2",
                "symfony/doctrine-bridge": "~2.3|~3.0"
            },
            "type": "symfony-bundle",
            "extra": {
                "branch-alias": {
                    "dev-master": "2.2.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Doctrine\\Bundle\\FixturesBundle\\": ""
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Symfony Community",
                    "homepage": "http://symfony.com/contributors"
                },
                {
                    "name": "Doctrine Project",
                    "homepage": "http://www.doctrine-project.org"
                },
                {
                    "name": "Fabien Potencier",
                    "email": "fabien@symfony.com"
                }
            ],
            "description": "Symfony DoctrineFixturesBundle",
            "homepage": "http://www.doctrine-project.org",
            "keywords": [
                "Fixture",
                "persistence"
            ],
            "time": "2015-11-04T21:23:23+00:00"
        },
        {
            "name": "fzaninotto/faker",
            "version": "v1.6.0",
            "source": {
                "type": "git",
                "url": "https://github.com/fzaninotto/Faker.git",
                "reference": "44f9a286a04b80c76a4e5fb7aad8bb539b920123"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/fzaninotto/Faker/zipball/44f9a286a04b80c76a4e5fb7aad8bb539b920123",
                "reference": "44f9a286a04b80c76a4e5fb7aad8bb539b920123",
                "shasum": ""
            },
            "require": {
                "php": "^5.3.3|^7.0"
            },
            "require-dev": {
                "ext-intl": "*",
                "phpunit/phpunit": "~4.0",
                "squizlabs/php_codesniffer": "~1.5"
            },
            "type": "library",
            "extra": {
                "branch-alias": []
            },
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
                    "name": "FranÃ§ois Zaninotto"
                }
            ],
            "description": "Faker is a PHP library that generates fake data for you.",
            "keywords": [
                "data",
                "faker",
                "fixtures"
            ],
            "time": "2016-04-29T12:21:54+00:00"
        },
        {
            "name": "hamcrest/hamcrest-php",
            "version": "v1.2.2",
            "source": {
                "type": "git",
                "url": "https://github.com/hamcrest/hamcrest-php.git",
                "reference": "b37020aa976fa52d3de9aa904aa2522dc518f79c"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/hamcrest/hamcrest-php/zipball/b37020aa976fa52d3de9aa904aa2522dc518f79c",
                "reference": "b37020aa976fa52d3de9aa904aa2522dc518f79c",
                "shasum": ""
            },
            "require": {
                "php": ">=5.3.2"
            },
            "replace": {
                "cordoval/hamcrest-php": "*",
                "davedevelopment/hamcrest-php": "*",
                "kodova/hamcrest-php": "*"
            },
            "require-dev": {
                "phpunit/php-file-iterator": "1.3.3",
                "satooshi/php-coveralls": "dev-master"
            },
            "type": "library",
            "autoload": {
                "classmap": [
                    "hamcrest"
                ],
                "files": [
                    "hamcrest/Hamcrest.php"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD"
            ],
            "description": "This is the PHP port of Hamcrest Matchers",
            "keywords": [
                "test"
            ],
            "time": "2015-05-11T14:41:42+00:00"
        },
        {
            "name": "liip/functional-test-bundle",
            "version": "1.8.0",
            "source": {
                "type": "git",
                "url": "https://github.com/liip/LiipFunctionalTestBundle.git",
                "reference": "e18866bc434fccdf0d04a4e776289ed999862b66"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/liip/LiipFunctionalTestBundle/zipball/e18866bc434fccdf0d04a4e776289ed999862b66",
                "reference": "e18866bc434fccdf0d04a4e776289ed999862b66",
                "shasum": ""
            },
            "require": {
                "doctrine/common": "~2.0",
                "php": "^5.6.0|^7.0",
                "symfony/browser-kit": "~2.3|~3.0",
                "symfony/framework-bundle": "2.3.*|~2.7|~3.0"
            },
            "require-dev": {
                "brianium/paratest": "~0.12.0|~0.13.2",
                "doctrine/data-fixtures": "1.2.2",
                "doctrine/doctrine-fixtures-bundle": "~2.3",
                "doctrine/orm": "~2.5",
                "doctrine/phpcr-bundle": "~1.3",
                "doctrine/phpcr-odm": "~1.3",
                "hautelook/alice-bundle": "~0.2|~1.2",
                "jackalope/jackalope-doctrine-dbal": "1.1.*|1.2.*",
                "nelmio/alice": "~1.7|~2.0",
                "phpunit/phpunit": "^4.8.35|^5.7|^6.1",
                "symfony/assetic-bundle": "~2.3",
                "symfony/console": "~2.5|~3.0",
                "symfony/monolog-bundle": "~2.4",
                "symfony/phpunit-bridge": "^2.7|~3.0",
                "symfony/symfony": "~2.3.27|~2.7|~3.0",
                "twig/twig": "~1.12|~2.0"
            },
            "suggest": {
                "brianium/paratest": "Required when using paratest to parallelize tests",
                "doctrine/dbal": "Required when using the fixture loading functionality with an ORM and SQLite",
                "doctrine/doctrine-fixtures-bundle": "Required when using the fixture loading functionality",
                "doctrine/orm": "Required when using the fixture loading functionality with an ORM and SQLite",
                "hautelook/alice-bundle": "Required when using loadFixtureFiles functionality with custom providers",
                "nelmio/alice": "Required when using loadFixtureFiles functionality",
                "symfony/framework-bundle": "To use assertStatusCode and assertValidationErrors ~2.5"
            },
            "type": "symfony-bundle",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.7.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Liip\\FunctionalTestBundle\\": ""
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Liip AG",
                    "homepage": "http://www.liip.ch/"
                },
                {
                    "name": "Community contributions",
                    "homepage": "https://github.com/liip/LiipFunctionalTestBundle/contributors"
                }
            ],
            "description": "This bundles provides additional functional test-cases for Symfony2 applications",
            "keywords": [
                "Symfony2"
            ],
            "time": "2017-06-19T09:12:22+00:00"
        },
        {
            "name": "mockery/mockery",
            "version": "0.9.9",
            "source": {
                "type": "git",
                "url": "https://github.com/mockery/mockery.git",
                "reference": "6fdb61243844dc924071d3404bb23994ea0b6856"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/mockery/mockery/zipball/6fdb61243844dc924071d3404bb23994ea0b6856",
                "reference": "6fdb61243844dc924071d3404bb23994ea0b6856",
                "shasum": ""
            },
            "require": {
                "hamcrest/hamcrest-php": "~1.1",
                "lib-pcre": ">=7.0",
                "php": ">=5.3.2"
            },
            "require-dev": {
                "phpunit/phpunit": "~4.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "0.9.x-dev"
                }
            },
            "autoload": {
                "psr-0": {
                    "Mockery": "library/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause"
            ],
            "authors": [
                {
                    "name": "PÃ¡draic Brady",
                    "email": "padraic.brady@gmail.com",
                    "homepage": "http://blog.astrumfutura.com"
                },
                {
                    "name": "Dave Marshall",
                    "email": "dave.marshall@atstsolutions.co.uk",
                    "homepage": "http://davedevelopment.co.uk"
                }
            ],
            "description": "Mockery is a simple yet flexible PHP mock object framework for use in unit testing with PHPUnit, PHPSpec or any other testing framework. Its core goal is to offer a test double framework with a succinct API capable of clearly defining all possible object operations and interactions using a human readable Domain Specific Language (DSL). Designed as a drop in alternative to PHPUnit's phpunit-mock-objects library, Mockery is easy to integrate with PHPUnit and can operate alongside phpunit-mock-objects without the World ending.",
            "homepage": "http://github.com/padraic/mockery",
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
            "time": "2017-02-28T12:52:32+00:00"
        },
        {
            "name": "myclabs/deep-copy",
            "version": "1.6.1",
            "source": {
                "type": "git",
                "url": "https://github.com/myclabs/DeepCopy.git",
                "reference": "8e6e04167378abf1ddb4d3522d8755c5fd90d102"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/myclabs/DeepCopy/zipball/8e6e04167378abf1ddb4d3522d8755c5fd90d102",
                "reference": "8e6e04167378abf1ddb4d3522d8755c5fd90d102",
                "shasum": ""
            },
            "require": {
                "php": ">=5.4.0"
            },
            "require-dev": {
                "doctrine/collections": "1.*",
                "phpunit/phpunit": "~4.1"
            },
            "type": "library",
            "autoload": {
                "psr-4": {
                    "DeepCopy\\": "src/DeepCopy/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "description": "Create deep copies (clones) of your objects",
            "homepage": "https://github.com/myclabs/DeepCopy",
            "keywords": [
                "clone",
                "copy",
                "duplicate",
                "object",
                "object graph"
            ],
            "time": "2017-04-12T18:52:22+00:00"
        },
        {
            "name": "phar-io/manifest",
            "version": "1.0.1",
            "source": {
                "type": "git",
                "url": "https://github.com/phar-io/manifest.git",
                "reference": "2df402786ab5368a0169091f61a7c1e0eb6852d0"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/phar-io/manifest/zipball/2df402786ab5368a0169091f61a7c1e0eb6852d0",
                "reference": "2df402786ab5368a0169091f61a7c1e0eb6852d0",
                "shasum": ""
            },
            "require": {
                "ext-dom": "*",
                "ext-phar": "*",
                "phar-io/version": "^1.0.1",
                "php": "^5.6 || ^7.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.0.x-dev"
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
            "time": "2017-03-05T18:14:27+00:00"
        },
        {
            "name": "phar-io/version",
            "version": "1.0.1",
            "source": {
                "type": "git",
                "url": "https://github.com/phar-io/version.git",
                "reference": "a70c0ced4be299a63d32fa96d9281d03e94041df"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/phar-io/version/zipball/a70c0ced4be299a63d32fa96d9281d03e94041df",
                "reference": "a70c0ced4be299a63d32fa96d9281d03e94041df",
                "shasum": ""
            },
            "require": {
                "php": "^5.6 || ^7.0"
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
            "time": "2017-03-05T17:38:23+00:00"
        },
        {
            "name": "phpdocumentor/reflection-common",
            "version": "1.0",
            "source": {
                "type": "git",
                "url": "https://github.com/phpDocumentor/ReflectionCommon.git",
                "reference": "144c307535e82c8fdcaacbcfc1d6d8eeb896687c"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/phpDocumentor/ReflectionCommon/zipball/144c307535e82c8fdcaacbcfc1d6d8eeb896687c",
                "reference": "144c307535e82c8fdcaacbcfc1d6d8eeb896687c",
                "shasum": ""
            },
            "require": {
                "php": ">=5.5"
            },
            "require-dev": {
                "phpunit/phpunit": "^4.6"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.0.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "phpDocumentor\\Reflection\\": [
                        "src"
                    ]
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
            "time": "2015-12-27T11:43:31+00:00"
        },
        {
            "name": "phpdocumentor/reflection-docblock",
            "version": "3.1.1",
            "source": {
                "type": "git",
                "url": "https://github.com/phpDocumentor/ReflectionDocBlock.git",
                "reference": "8331b5efe816ae05461b7ca1e721c01b46bafb3e"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/phpDocumentor/ReflectionDocBlock/zipball/8331b5efe816ae05461b7ca1e721c01b46bafb3e",
                "reference": "8331b5efe816ae05461b7ca1e721c01b46bafb3e",
                "shasum": ""
            },
            "require": {
                "php": ">=5.5",
                "phpdocumentor/reflection-common": "^1.0@dev",
                "phpdocumentor/type-resolver": "^0.2.0",
                "webmozart/assert": "^1.0"
            },
            "require-dev": {
                "mockery/mockery": "^0.9.4",
                "phpunit/phpunit": "^4.4"
            },
            "type": "library",
            "autoload": {
                "psr-4": {
                    "phpDocumentor\\Reflection\\": [
                        "src/"
                    ]
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
            "description": "With this component, a library can provide support for annotations via DocBlocks or otherwise retrieve information that is embedded in a DocBlock.",
            "time": "2016-09-30T07:12:33+00:00"
        },
        {
            "name": "phpdocumentor/type-resolver",
            "version": "0.2.1",
            "source": {
                "type": "git",
                "url": "https://github.com/phpDocumentor/TypeResolver.git",
                "reference": "e224fb2ea2fba6d3ad6fdaef91cd09a172155ccb"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/phpDocumentor/TypeResolver/zipball/e224fb2ea2fba6d3ad6fdaef91cd09a172155ccb",
                "reference": "e224fb2ea2fba6d3ad6fdaef91cd09a172155ccb",
                "shasum": ""
            },
            "require": {
                "php": ">=5.5",
                "phpdocumentor/reflection-common": "^1.0"
            },
            "require-dev": {
                "mockery/mockery": "^0.9.4",
                "phpunit/phpunit": "^5.2||^4.8.24"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.0.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "phpDocumentor\\Reflection\\": [
                        "src/"
                    ]
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
            "time": "2016-11-25T06:54:22+00:00"
        },
        {
            "name": "phpspec/prophecy",
            "version": "v1.7.0",
            "source": {
                "type": "git",
                "url": "https://github.com/phpspec/prophecy.git",
                "reference": "93d39f1f7f9326d746203c7c056f300f7f126073"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/phpspec/prophecy/zipball/93d39f1f7f9326d746203c7c056f300f7f126073",
                "reference": "93d39f1f7f9326d746203c7c056f300f7f126073",
                "shasum": ""
            },
            "require": {
                "doctrine/instantiator": "^1.0.2",
                "php": "^5.3|^7.0",
                "phpdocumentor/reflection-docblock": "^2.0|^3.0.2",
                "sebastian/comparator": "^1.1|^2.0",
                "sebastian/recursion-context": "^1.0|^2.0|^3.0"
            },
            "require-dev": {
                "phpspec/phpspec": "^2.5|^3.2",
                "phpunit/phpunit": "^4.8 || ^5.6.5"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.6.x-dev"
                }
            },
            "autoload": {
                "psr-0": {
                    "Prophecy\\": "src/"
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
                },
                {
                    "name": "Marcello Duarte",
                    "email": "marcello.duarte@gmail.com"
                }
            ],
            "description": "Highly opinionated mocking framework for PHP 5.3+",
            "homepage": "https://github.com/phpspec/prophecy",
            "keywords": [
                "Double",
                "Dummy",
                "fake",
                "mock",
                "spy",
                "stub"
            ],
            "time": "2017-03-02T20:05:34+00:00"
        },
        {
            "name": "phpunit/php-code-coverage",
            "version": "5.2.1",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/php-code-coverage.git",
                "reference": "dc421f9ca5082a0c0cb04afb171c765f79add85b"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/php-code-coverage/zipball/dc421f9ca5082a0c0cb04afb171c765f79add85b",
                "reference": "dc421f9ca5082a0c0cb04afb171c765f79add85b",
                "shasum": ""
            },
            "require": {
                "ext-dom": "*",
                "ext-xmlwriter": "*",
                "php": "^7.0",
                "phpunit/php-file-iterator": "^1.3",
                "phpunit/php-text-template": "^1.2",
                "phpunit/php-token-stream": "^1.4.11 || ^2.0",
                "sebastian/code-unit-reverse-lookup": "^1.0",
                "sebastian/environment": "^3.0",
                "sebastian/version": "^2.0",
                "theseer/tokenizer": "^1.1"
            },
            "require-dev": {
                "ext-xdebug": "^2.5",
                "phpunit/phpunit": "^6.0"
            },
            "suggest": {
                "ext-xdebug": "^2.5.3"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "5.2.x-dev"
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
                    "email": "sb@sebastian-bergmann.de",
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
            "time": "2017-04-21T08:03:57+00:00"
        },
        {
            "name": "phpunit/php-file-iterator",
            "version": "1.4.2",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/php-file-iterator.git",
                "reference": "3cc8f69b3028d0f96a9078e6295d86e9bf019be5"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/php-file-iterator/zipball/3cc8f69b3028d0f96a9078e6295d86e9bf019be5",
                "reference": "3cc8f69b3028d0f96a9078e6295d86e9bf019be5",
                "shasum": ""
            },
            "require": {
                "php": ">=5.3.3"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.4.x-dev"
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
                    "email": "sb@sebastian-bergmann.de",
                    "role": "lead"
                }
            ],
            "description": "FilterIterator implementation that filters files based on a list of suffixes.",
            "homepage": "https://github.com/sebastianbergmann/php-file-iterator/",
            "keywords": [
                "filesystem",
                "iterator"
            ],
            "time": "2016-10-03T07:40:28+00:00"
        },
        {
            "name": "phpunit/php-text-template",
            "version": "1.2.1",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/php-text-template.git",
                "reference": "31f8b717e51d9a2afca6c9f046f5d69fc27c8686"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/php-text-template/zipball/31f8b717e51d9a2afca6c9f046f5d69fc27c8686",
                "reference": "31f8b717e51d9a2afca6c9f046f5d69fc27c8686",
                "shasum": ""
            },
            "require": {
                "php": ">=5.3.3"
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
            "time": "2015-06-21T13:50:34+00:00"
        },
        {
            "name": "phpunit/php-timer",
            "version": "1.0.9",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/php-timer.git",
                "reference": "3dcf38ca72b158baf0bc245e9184d3fdffa9c46f"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/php-timer/zipball/3dcf38ca72b158baf0bc245e9184d3fdffa9c46f",
                "reference": "3dcf38ca72b158baf0bc245e9184d3fdffa9c46f",
                "shasum": ""
            },
            "require": {
                "php": "^5.3.3 || ^7.0"
            },
            "require-dev": {
                "phpunit/phpunit": "^4.8.35 || ^5.7 || ^6.0"
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
                    "email": "sb@sebastian-bergmann.de",
                    "role": "lead"
                }
            ],
            "description": "Utility class for timing",
            "homepage": "https://github.com/sebastianbergmann/php-timer/",
            "keywords": [
                "timer"
            ],
            "time": "2017-02-26T11:10:40+00:00"
        },
        {
            "name": "phpunit/php-token-stream",
            "version": "1.4.11",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/php-token-stream.git",
                "reference": "e03f8f67534427a787e21a385a67ec3ca6978ea7"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/php-token-stream/zipball/e03f8f67534427a787e21a385a67ec3ca6978ea7",
                "reference": "e03f8f67534427a787e21a385a67ec3ca6978ea7",
                "shasum": ""
            },
            "require": {
                "ext-tokenizer": "*",
                "php": ">=5.3.3"
            },
            "require-dev": {
                "phpunit/phpunit": "~4.2"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.4-dev"
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
            "description": "Wrapper around PHP's tokenizer extension.",
            "homepage": "https://github.com/sebastianbergmann/php-token-stream/",
            "keywords": [
                "tokenizer"
            ],
            "time": "2017-02-27T10:12:30+00:00"
        },
        {
            "name": "phpunit/phpunit",
            "version": "6.2.3",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/phpunit.git",
                "reference": "fa5711d0559fc4b64deba0702be52d41434cbcb7"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/phpunit/zipball/fa5711d0559fc4b64deba0702be52d41434cbcb7",
                "reference": "fa5711d0559fc4b64deba0702be52d41434cbcb7",
                "shasum": ""
            },
            "require": {
                "ext-dom": "*",
                "ext-json": "*",
                "ext-libxml": "*",
                "ext-mbstring": "*",
                "ext-xml": "*",
                "myclabs/deep-copy": "^1.3",
                "phar-io/manifest": "^1.0.1",
                "phar-io/version": "^1.0",
                "php": "^7.0",
                "phpspec/prophecy": "^1.7",
                "phpunit/php-code-coverage": "^5.2",
                "phpunit/php-file-iterator": "^1.4",
                "phpunit/php-text-template": "^1.2",
                "phpunit/php-timer": "^1.0.6",
                "phpunit/phpunit-mock-objects": "^4.0",
                "sebastian/comparator": "^2.0",
                "sebastian/diff": "^1.4.3 || ^2.0",
                "sebastian/environment": "^3.0.2",
                "sebastian/exporter": "^3.1",
                "sebastian/global-state": "^1.1 || ^2.0",
                "sebastian/object-enumerator": "^3.0.2",
                "sebastian/resource-operations": "^1.0",
                "sebastian/version": "^2.0"
            },
            "conflict": {
                "phpdocumentor/reflection-docblock": "3.0.2",
                "phpunit/dbunit": "<3.0"
            },
            "require-dev": {
                "ext-pdo": "*"
            },
            "suggest": {
                "ext-xdebug": "*",
                "phpunit/php-invoker": "^1.1"
            },
            "bin": [
                "phpunit"
            ],
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "6.2.x-dev"
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
            "description": "The PHP Unit Testing framework.",
            "homepage": "https://phpunit.de/",
            "keywords": [
                "phpunit",
                "testing",
                "xunit"
            ],
            "time": "2017-07-03T15:54:24+00:00"
        },
        {
            "name": "phpunit/phpunit-mock-objects",
            "version": "4.0.2",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/phpunit-mock-objects.git",
                "reference": "d8833b396dce9162bb2eb5d59aee5a3ab3cfa5b4"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/phpunit-mock-objects/zipball/d8833b396dce9162bb2eb5d59aee5a3ab3cfa5b4",
                "reference": "d8833b396dce9162bb2eb5d59aee5a3ab3cfa5b4",
                "shasum": ""
            },
            "require": {
                "doctrine/instantiator": "^1.0.2",
                "php": "^7.0",
                "phpunit/php-text-template": "^1.2",
                "sebastian/exporter": "^3.0"
            },
            "conflict": {
                "phpunit/phpunit": "<6.0"
            },
            "require-dev": {
                "phpunit/phpunit": "^6.0"
            },
            "suggest": {
                "ext-soap": "*"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "4.0.x-dev"
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
                    "email": "sb@sebastian-bergmann.de",
                    "role": "lead"
                }
            ],
            "description": "Mock Object library for PHPUnit",
            "homepage": "https://github.com/sebastianbergmann/phpunit-mock-objects/",
            "keywords": [
                "mock",
                "xunit"
            ],
            "time": "2017-06-30T08:15:21+00:00"
        },
        {
            "name": "sebastian/code-unit-reverse-lookup",
            "version": "1.0.1",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/code-unit-reverse-lookup.git",
                "reference": "4419fcdb5eabb9caa61a27c7a1db532a6b55dd18"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/code-unit-reverse-lookup/zipball/4419fcdb5eabb9caa61a27c7a1db532a6b55dd18",
                "reference": "4419fcdb5eabb9caa61a27c7a1db532a6b55dd18",
                "shasum": ""
            },
            "require": {
                "php": "^5.6 || ^7.0"
            },
            "require-dev": {
                "phpunit/phpunit": "^5.7 || ^6.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.0.x-dev"
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
            "time": "2017-03-04T06:30:41+00:00"
        },
        {
            "name": "sebastian/comparator",
            "version": "2.0.0",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/comparator.git",
                "reference": "20f84f468cb67efee293246e6a09619b891f55f0"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/comparator/zipball/20f84f468cb67efee293246e6a09619b891f55f0",
                "reference": "20f84f468cb67efee293246e6a09619b891f55f0",
                "shasum": ""
            },
            "require": {
                "php": "^7.0",
                "sebastian/diff": "^1.2",
                "sebastian/exporter": "^3.0"
            },
            "require-dev": {
                "phpunit/phpunit": "^6.0"
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
                },
                {
                    "name": "Sebastian Bergmann",
                    "email": "sebastian@phpunit.de"
                }
            ],
            "description": "Provides the functionality to compare PHP values for equality",
            "homepage": "http://www.github.com/sebastianbergmann/comparator",
            "keywords": [
                "comparator",
                "compare",
                "equality"
            ],
            "time": "2017-03-03T06:26:08+00:00"
        },
        {
            "name": "sebastian/diff",
            "version": "1.4.3",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/diff.git",
                "reference": "7f066a26a962dbe58ddea9f72a4e82874a3975a4"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/diff/zipball/7f066a26a962dbe58ddea9f72a4e82874a3975a4",
                "reference": "7f066a26a962dbe58ddea9f72a4e82874a3975a4",
                "shasum": ""
            },
            "require": {
                "php": "^5.3.3 || ^7.0"
            },
            "require-dev": {
                "phpunit/phpunit": "^4.8.35 || ^5.7 || ^6.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.4-dev"
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
                    "name": "Kore Nordmann",
                    "email": "mail@kore-nordmann.de"
                },
                {
                    "name": "Sebastian Bergmann",
                    "email": "sebastian@phpunit.de"
                }
            ],
            "description": "Diff implementation",
            "homepage": "https://github.com/sebastianbergmann/diff",
            "keywords": [
                "diff"
            ],
            "time": "2017-05-22T07:24:03+00:00"
        },
        {
            "name": "sebastian/environment",
            "version": "3.1.0",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/environment.git",
                "reference": "cd0871b3975fb7fc44d11314fd1ee20925fce4f5"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/environment/zipball/cd0871b3975fb7fc44d11314fd1ee20925fce4f5",
                "reference": "cd0871b3975fb7fc44d11314fd1ee20925fce4f5",
                "shasum": ""
            },
            "require": {
                "php": "^7.0"
            },
            "require-dev": {
                "phpunit/phpunit": "^6.1"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "3.1.x-dev"
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
            "time": "2017-07-01T08:51:00+00:00"
        },
        {
            "name": "sebastian/exporter",
            "version": "3.1.0",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/exporter.git",
                "reference": "234199f4528de6d12aaa58b612e98f7d36adb937"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/exporter/zipball/234199f4528de6d12aaa58b612e98f7d36adb937",
                "reference": "234199f4528de6d12aaa58b612e98f7d36adb937",
                "shasum": ""
            },
            "require": {
                "php": "^7.0",
                "sebastian/recursion-context": "^3.0"
            },
            "require-dev": {
                "ext-mbstring": "*",
                "phpunit/phpunit": "^6.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "3.1.x-dev"
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
                },
                {
                    "name": "Sebastian Bergmann",
                    "email": "sebastian@phpunit.de"
                },
                {
                    "name": "Adam Harvey",
                    "email": "aharvey@php.net"
                }
            ],
            "description": "Provides the functionality to export PHP variables for visualization",
            "homepage": "http://www.github.com/sebastianbergmann/exporter",
            "keywords": [
                "export",
                "exporter"
            ],
            "time": "2017-04-03T13:19:02+00:00"
        },
        {
            "name": "sebastian/global-state",
            "version": "2.0.0",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/global-state.git",
                "reference": "e8ba02eed7bbbb9e59e43dedd3dddeff4a56b0c4"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/global-state/zipball/e8ba02eed7bbbb9e59e43dedd3dddeff4a56b0c4",
                "reference": "e8ba02eed7bbbb9e59e43dedd3dddeff4a56b0c4",
                "shasum": ""
            },
            "require": {
                "php": "^7.0"
            },
            "require-dev": {
                "phpunit/phpunit": "^6.0"
            },
            "suggest": {
                "ext-uopz": "*"
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
            "description": "Snapshotting of global state",
            "homepage": "http://www.github.com/sebastianbergmann/global-state",
            "keywords": [
                "global state"
            ],
            "time": "2017-04-27T15:39:26+00:00"
        },
        {
            "name": "sebastian/object-enumerator",
            "version": "3.0.2",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/object-enumerator.git",
                "reference": "31dd3379d16446c5d86dec32ab1ad1f378581ad8"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/object-enumerator/zipball/31dd3379d16446c5d86dec32ab1ad1f378581ad8",
                "reference": "31dd3379d16446c5d86dec32ab1ad1f378581ad8",
                "shasum": ""
            },
            "require": {
                "php": "^7.0",
                "sebastian/object-reflector": "^1.0",
                "sebastian/recursion-context": "^3.0"
            },
            "require-dev": {
                "phpunit/phpunit": "^6.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "3.0.x-dev"
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
            "time": "2017-03-12T15:17:29+00:00"
        },
        {
            "name": "sebastian/object-reflector",
            "version": "1.1.1",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/object-reflector.git",
                "reference": "773f97c67f28de00d397be301821b06708fca0be"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/object-reflector/zipball/773f97c67f28de00d397be301821b06708fca0be",
                "reference": "773f97c67f28de00d397be301821b06708fca0be",
                "shasum": ""
            },
            "require": {
                "php": "^7.0"
            },
            "require-dev": {
                "phpunit/phpunit": "^6.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.1-dev"
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
            "time": "2017-03-29T09:07:27+00:00"
        },
        {
            "name": "sebastian/recursion-context",
            "version": "3.0.0",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/recursion-context.git",
                "reference": "5b0cd723502bac3b006cbf3dbf7a1e3fcefe4fa8"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/recursion-context/zipball/5b0cd723502bac3b006cbf3dbf7a1e3fcefe4fa8",
                "reference": "5b0cd723502bac3b006cbf3dbf7a1e3fcefe4fa8",
                "shasum": ""
            },
            "require": {
                "php": "^7.0"
            },
            "require-dev": {
                "phpunit/phpunit": "^6.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "3.0.x-dev"
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
                    "name": "Jeff Welch",
                    "email": "whatthejeff@gmail.com"
                },
                {
                    "name": "Sebastian Bergmann",
                    "email": "sebastian@phpunit.de"
                },
                {
                    "name": "Adam Harvey",
                    "email": "aharvey@php.net"
                }
            ],
            "description": "Provides functionality to recursively process PHP variables",
            "homepage": "http://www.github.com/sebastianbergmann/recursion-context",
            "time": "2017-03-03T06:23:57+00:00"
        },
        {
            "name": "sebastian/resource-operations",
            "version": "1.0.0",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/resource-operations.git",
                "reference": "ce990bb21759f94aeafd30209e8cfcdfa8bc3f52"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/resource-operations/zipball/ce990bb21759f94aeafd30209e8cfcdfa8bc3f52",
                "reference": "ce990bb21759f94aeafd30209e8cfcdfa8bc3f52",
                "shasum": ""
            },
            "require": {
                "php": ">=5.6.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.0.x-dev"
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
            "time": "2015-07-28T20:34:47+00:00"
        },
        {
            "name": "sebastian/version",
            "version": "2.0.1",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/version.git",
                "reference": "99732be0ddb3361e16ad77b68ba41efc8e979019"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/version/zipball/99732be0ddb3361e16ad77b68ba41efc8e979019",
                "reference": "99732be0ddb3361e16ad77b68ba41efc8e979019",
                "shasum": ""
            },
            "require": {
                "php": ">=5.6"
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
                    "name": "Sebastian Bergmann",
                    "email": "sebastian@phpunit.de",
                    "role": "lead"
                }
            ],
            "description": "Library that helps with managing the version number of Git-hosted PHP projects",
            "homepage": "https://github.com/sebastianbergmann/version",
            "time": "2016-10-03T07:35:21+00:00"
        },
        {
            "name": "sensio/generator-bundle",
            "version": "v3.1.4",
            "source": {
                "type": "git",
                "url": "https://github.com/sensiolabs/SensioGeneratorBundle.git",
                "reference": "37f9f4e165b033fb76cc2320838321cc57140e65"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sensiolabs/SensioGeneratorBundle/zipball/37f9f4e165b033fb76cc2320838321cc57140e65",
                "reference": "37f9f4e165b033fb76cc2320838321cc57140e65",
                "shasum": ""
            },
            "require": {
                "symfony/console": "~2.7|~3.0",
                "symfony/framework-bundle": "~2.7|~3.0",
                "symfony/process": "~2.7|~3.0",
                "symfony/yaml": "~2.7|~3.0",
                "twig/twig": "^1.28.2|^2.0"
            },
            "require-dev": {
                "doctrine/orm": "~2.4",
                "symfony/doctrine-bridge": "~2.7|~3.0",
                "symfony/filesystem": "~2.7|~3.0",
                "symfony/phpunit-bridge": "^3.3"
            },
            "type": "symfony-bundle",
            "extra": {
                "branch-alias": {
                    "dev-master": "3.1.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Sensio\\Bundle\\GeneratorBundle\\": ""
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
                }
            ],
            "description": "This bundle generates code for you",
            "time": "2017-03-15T01:02:10+00:00"
        },
        {
            "name": "symfony/phpunit-bridge",
            "version": "v3.3.4",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/phpunit-bridge.git",
                "reference": "c2c124b7f9de79f4a64dc011f041a3a2c768b913"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/phpunit-bridge/zipball/c2c124b7f9de79f4a64dc011f041a3a2c768b913",
                "reference": "c2c124b7f9de79f4a64dc011f041a3a2c768b913",
                "shasum": ""
            },
            "require": {
                "php": ">=5.3.3"
            },
            "conflict": {
                "phpunit/phpunit": "<4.8.35|<5.4.3,>=5.0"
            },
            "suggest": {
                "ext-zip": "Zip support is required when using bin/simple-phpunit",
                "symfony/debug": "For tracking deprecated interfaces usages at runtime with DebugClassLoader"
            },
            "bin": [
                "bin/simple-phpunit"
            ],
            "type": "symfony-bridge",
            "extra": {
                "branch-alias": {
                    "dev-master": "3.3-dev"
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
            "description": "Symfony PHPUnit Bridge",
            "homepage": "https://symfony.com",
            "time": "2017-06-12T13:35:45+00:00"
        },
        {
            "name": "theseer/tokenizer",
            "version": "1.1.0",
            "source": {
                "type": "git",
                "url": "https://github.com/theseer/tokenizer.git",
                "reference": "cb2f008f3f05af2893a87208fe6a6c4985483f8b"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/theseer/tokenizer/zipball/cb2f008f3f05af2893a87208fe6a6c4985483f8b",
                "reference": "cb2f008f3f05af2893a87208fe6a6c4985483f8b",
                "shasum": ""
            },
            "require": {
                "ext-dom": "*",
                "ext-tokenizer": "*",
                "ext-xmlwriter": "*",
                "php": "^7.0"
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
            "time": "2017-04-07T12:08:54+00:00"
        }
    ],
    "aliases": [],
    "minimum-stability": "stable",
    "stability-flags": [],
    "prefer-stable": false,
    "prefer-lowest": false,
    "platform": {
        "php": ">=7.1"
    },
    "platform-dev": []
}
```

## File: `docker-compose.yml.dist`
```
version: "3.1"
services:
    db:
        image: postgres:latest
        restart: always
        ports:
            - "4500:5432"
        environment:
            POSTGRES_USER: postgres
            POSTGRES_PASSWORD: userpass
            POSTGRES_DB: symfony_wishlist
    cache:
        image: redis:latest
        restart: always
        ports:
            - "4600:6379"
```

## File: `npm-shrinkwrap.json`
```json
{
  "name": "wishlist",
  "version": "1.0.0",
  "dependencies": {
    "@symfony/webpack-encore": {
      "version": "0.10.0",
      "from": "@symfony/webpack-encore@latest",
      "resolved": "https://registry.npmjs.org/@symfony/webpack-encore/-/webpack-encore-0.10.0.tgz"
    },
    "abbrev": {
      "version": "1.1.0",
      "from": "abbrev@>=1.0.0 <2.0.0",
      "resolved": "https://registry.npmjs.org/abbrev/-/abbrev-1.1.0.tgz"
    },
    "accepts": {
      "version": "1.3.3",
      "from": "accepts@>=1.3.3 <1.4.0",
      "resolved": "https://registry.npmjs.org/accepts/-/accepts-1.3.3.tgz"
    },
    "acorn": {
      "version": "5.1.1",
      "from": "acorn@>=5.0.0 <6.0.0",
      "resolved": "https://registry.npmjs.org/acorn/-/acorn-5.1.1.tgz"
    },
    "acorn-dynamic-import": {
      "version": "2.0.2",
      "from": "acorn-dynamic-import@>=2.0.0 <3.0.0",
      "resolved": "https://registry.npmjs.org/acorn-dynamic-import/-/acorn-dynamic-import-2.0.2.tgz",
      "dependencies": {
        "acorn": {
          "version": "4.0.13",
          "from": "acorn@>=4.0.3 <5.0.0",
          "resolved": "https://registry.npmjs.org/acorn/-/acorn-4.0.13.tgz"
        }
      }
    },
    "adjust-sourcemap-loader": {
      "version": "1.1.0",
      "from": "adjust-sourcemap-loader@>=1.1.0 <2.0.0",
      "resolved": "https://registry.npmjs.org/adjust-sourcemap-loader/-/adjust-sourcemap-loader-1.1.0.tgz",
      "dependencies": {
        "camelcase": {
          "version": "1.2.1",
          "from": "camelcase@>=1.2.1 <2.0.0",
          "resolved": "https://registry.npmjs.org/camelcase/-/camelcase-1.2.1.tgz"
        },
        "lodash.defaults": {
          "version": "3.1.2",
          "from": "lodash.defaults@>=3.1.2 <4.0.0",
          "resolved": "https://registry.npmjs.org/lodash.defaults/-/lodash.defaults-3.1.2.tgz",
          "dependencies": {
            "lodash.assign": {
              "version": "3.2.0",
              "from": "lodash.assign@>=3.0.0 <4.0.0",
              "resolved": "https://registry.npmjs.org/lodash.assign/-/lodash.assign-3.2.0.tgz"
            }
          }
        }
      }
    },
    "ajv": {
      "version": "5.2.2",
      "from": "ajv@>=5.0.0 <6.0.0",
      "resolved": "https://registry.npmjs.org/ajv/-/ajv-5.2.2.tgz"
    },
    "ajv-keywords": {
      "version": "1.5.1",
      "from": "ajv-keywords@>=1.1.1 <2.0.0",
      "resolved": "https://registry.npmjs.org/ajv-keywords/-/ajv-keywords-1.5.1.tgz"
    },
    "align-text": {
      "version": "0.1.4",
      "from": "align-text@>=0.1.3 <0.2.0",
      "resolved": "https://registry.npmjs.org/align-text/-/align-text-0.1.4.tgz"
    },
    "alphanum-sort": {
      "version": "1.0.2",
      "from": "alphanum-sort@>=1.0.1 <2.0.0",
      "resolved": "https://registry.npmjs.org/alphanum-sort/-/alphanum-sort-1.0.2.tgz"
    },
    "amdefine": {
      "version": "1.0.1",
      "from": "amdefine@>=0.0.4",
      "resolved": "https://registry.npmjs.org/amdefine/-/amdefine-1.0.1.tgz"
    },
    "ansi-html": {
      "version": "0.0.7",
      "from": "ansi-html@0.0.7",
      "resolved": "https://registry.npmjs.org/ansi-html/-/ansi-html-0.0.7.tgz"
    },
    "ansi-regex": {
      "version": "2.1.1",
      "from": "ansi-regex@>=2.0.0 <3.0.0",
      "resolved": "https://registry.npmjs.org/ansi-regex/-/ansi-regex-2.1.1.tgz"
    },
    "ansi-styles": {
      "version": "2.2.1",
      "from": "ansi-styles@>=2.2.1 <3.0.0",
      "resolved": "https://registry.npmjs.org/ansi-styles/-/ansi-styles-2.2.1.tgz"
    },
    "anymatch": {
      "version": "1.3.0",
      "from": "anymatch@>=1.3.0 <2.0.0",
      "resolved": "https://registry.npmjs.org/anymatch/-/anymatch-1.3.0.tgz"
    },
    "argparse": {
      "version": "1.0.9",
      "from": "argparse@>=1.0.7 <2.0.0",
      "resolved": "https://registry.npmjs.org/argparse/-/argparse-1.0.9.tgz"
    },
    "arr-diff": {
      "version": "2.0.0",
      "from": "arr-diff@>=2.0.0 <3.0.0",
      "resolved": "https://registry.npmjs.org/arr-diff/-/arr-diff-2.0.0.tgz"
    },
    "arr-flatten": {
      "version": "1.1.0",
      "from": "arr-flatten@>=1.0.1 <2.0.0",
      "resolved": "https://registry.npmjs.org/arr-flatten/-/arr-flatten-1.1.0.tgz"
    },
    "array-find-index": {
      "version": "1.0.2",
      "from": "array-find-index@>=1.0.1 <2.0.0",
      "resolved": "https://registry.npmjs.org/array-find-index/-/array-find-index-1.0.2.tgz"
    },
    "array-flatten": {
      "version": "2.1.1",
      "from": "array-flatten@>=2.1.0 <3.0.0",
      "resolved": "https://registry.npmjs.org/array-flatten/-/array-flatten-2.1.1.tgz"
    },
    "array-union": {
      "version": "1.0.2",
      "from": "array-union@>=1.0.1 <2.0.0",
      "resolved": "https://registry.npmjs.org/array-union/-/array-union-1.0.2.tgz"
    },
    "array-uniq": {
      "version": "1.0.3",
      "from": "array-uniq@>=1.0.1 <2.0.0",
      "resolved": "https://registry.npmjs.org/array-uniq/-/array-uniq-1.0.3.tgz"
    },
    "array-unique": {
      "version": "0.2.1",
      "from": "array-unique@>=0.2.1 <0.3.0",
      "resolved": "https://registry.npmjs.org/array-unique/-/array-unique-0.2.1.tgz"
    },
    "arrify": {
      "version": "1.0.1",
      "from": "arrify@>=1.0.0 <2.0.0",
      "resolved": "https://registry.npmjs.org/arrify/-/arrify-1.0.1.tgz"
    },
    "asn1.js": {
      "version": "4.9.1",
      "from": "asn1.js@>=4.0.0 <5.0.0",
      "resolved": "https://registry.npmjs.org/asn1.js/-/asn1.js-4.9.1.tgz"
    },
    "assert": {
      "version": "1.4.1",
      "from": "assert@>=1.3.0 <2.0.0",
      "resolved": "https://registry.npmjs.org/assert/-/assert-1.4.1.tgz"
    },
    "async": {
      "version": "2.5.0",
      "from": "async@>=2.1.2 <3.0.0",
      "resolved": "https://registry.npmjs.org/async/-/async-2.5.0.tgz"
    },
    "async-each": {
      "version": "1.0.1",
      "from": "async-each@>=1.0.0 <2.0.0",
      "resolved": "https://registry.npmjs.org/async-each/-/async-each-1.0.1.tgz"
    },
    "atob": {
      "version": "1.1.3",
      "from": "atob@>=1.1.0 <1.2.0",
      "resolved": "https://registry.npmjs.org/atob/-/atob-1.1.3.tgz"
    },
    "autoprefixer": {
      "version": "6.7.7",
      "from": "autoprefixer@>=6.3.1 <7.0.0",
      "resolved": "https://registry.npmjs.org/autoprefixer/-/autoprefixer-6.7.7.tgz",
      "dependencies": {
        "browserslist": {
          "version": "1.7.7",
          "from": "browserslist@>=1.7.6 <2.0.0",
          "resolved": "https://registry.npmjs.org/browserslist/-/browserslist-1.7.7.tgz"
        }
      }
    },
    "babel-code-frame": {
      "version": "6.22.0",
      "from": "babel-code-frame@>=6.22.0 <7.0.0",
      "resolved": "https://registry.npmjs.org/babel-code-frame/-/babel-code-frame-6.22.0.tgz"
    },
    "babel-core": {
      "version": "6.25.0",
      "from": "babel-core@>=6.24.0 <7.0.0",
      "resolved": "https://registry.npmjs.org/babel-core/-/babel-core-6.25.0.tgz"
    },
    "babel-generator": {
      "version": "6.25.0",
      "from": "babel-generator@>=6.25.0 <7.0.0",
      "resolved": "https://registry.npmjs.org/babel-generator/-/babel-generator-6.25.0.tgz"
    },
    "babel-helper-builder-binary-assignment-operator-visitor": {
      "version": "6.24.1",
      "from": "babel-helper-builder-binary-assignment-operator-visitor@>=6.24.1 <7.0.0",
      "resolved": "https://registry.npmjs.org/babel-helper-builder-binary-assignment-operator-visitor/-/babel-helper-builder-binary-assignment-operator-visitor-6.24.1.tgz"
    },
    "babel-helper-call-delegate": {
      "version": "6.24.1",
      "from": "babel-helper-call-delegate@>=6.24.1 <7.0.0",
      "resolved": "https://registry.npmjs.org/babel-helper-call-delegate/-/babel-helper-call-delegate-6.24.1.tgz"
    },
    "babel-helper-define-map": {
      "version": "6.24.1",
      "from": "babel-helper-define-map@>=6.24.1 <7.0.0",
      "resolved": "https://registry.npmjs.org/babel-helper-define-map/-/babel-helper-define-map-6.24.1.tgz"
    },
    "babel-helper-explode-assignable-expression": {
      "version": "6.24.1",
      "from": "babel-helper-explode-assignable-expression@>=6.24.1 <7.0.0",
      "resolved": "https://registry.npmjs.org/babel-helper-explode-assignable-expression/-/babel-helper-explode-assignable-expression-6.24.1.tgz"
    },
    "babel-helper-function-name": {
      "version": "6.24.1",
      "from": "babel-helper-function-name@>=6.24.1 <7.0.0",
      "resolved": "https://registry.npmjs.org/babel-helper-function-name/-/babel-helper-function-name-6.24.1.tgz"
    },
    "babel-helper-get-function-arity": {
      "version": "6.24.1",
      "from": "babel-helper-get-function-arity@>=6.24.1 <7.0.0",
      "resolved": "https://registry.npmjs.org/babel-helper-get-function-arity/-/babel-helper-get-function-arity-6.24.1.tgz"
    },
    "babel-helper-hoist-variables": {
      "version": "6.24.1",
      "from": "babel-helper-hoist-variables@>=6.24.1 <7.0.0",
      "resolved": "https://registry.npmjs.org/babel-helper-hoist-variables/-/babel-helper-hoist-variables-6.24.1.tgz"
    },
    "babel-helper-optimise-call-expression": {
      "version": "6.24.1",
      "from": "babel-helper-optimise-call-expression@>=6.24.1 <7.0.0",
      "resolved": "https://registry.npmjs.org/babel-helper-optimise-call-expression/-/babel-helper-optimise-call-expression-6.24.1.tgz"
    },
    "babel-helper-regex": {
      "version": "6.24.1",
      "from": "babel-helper-regex@>=6.24.1 <7.0.0",
      "resolved": "https://registry.npmjs.org/babel-helper-regex/-/babel-helper-regex-6.24.1.tgz"
    },
    "babel-helper-remap-async-to-generator": {
      "version": "6.24.1",
      "from": "babel-helper-remap-async-to-generator@>=6.24.1 <7.0.0",
      "resolved": "https://registry.npmjs.org/babel-helper-remap-async-to-generator/-/babel-helper-remap-async-to-generator-6.24.1.tgz"
    },
    "babel-helper-replace-supers": {
      "version": "6.24.1",
      "from": "babel-helper-replace-supers@>=6.24.1 <7.0.0",
      "resolved": "https://registry.npmjs.org/babel-helper-replace-supers/-/babel-helper-replace-supers-6.24.1.tgz"
    },
    "babel-helpers": {
      "version": "6.24.1",
      "from": "babel-helpers@>=6.24.1 <7.0.0",
      "resolved": "https://registry.npmjs.org/babel-helpers/-/babel-helpers-6.24.1.tgz"
    },
    "babel-loader": {
      "version": "7.1.1",
      "from": "babel-loader@>=7.1.0 <8.0.0",
      "resolved": "https://registry.npmjs.org/babel-loader/-/babel-loader-7.1.1.tgz"
    },
    "babel-messages": {
      "version": "6.23.0",
      "from": "babel-messages@>=6.23.0 <7.0.0",
      "resolved": "https://registry.npmjs.org/babel-messages/-/babel-messages-6.23.0.tgz"
    },
    "babel-plugin-check-es2015-constants": {
      "version": "6.22.0",
      "from": "babel-plugin-check-es2015-constants@>=6.22.0 <7.0.0",
      "resolved": "https://registry.npmjs.org/babel-plugin-check-es2015-constants/-/babel-plugin-check-es2015-constants-6.22.0.tgz"
    },
    "babel-plugin-syntax-async-functions": {
      "version": "6.13.0",
      "from": "babel-plugin-syntax-async-functions@>=6.8.0 <7.0.0",
      "resolved": "https://registry.npmjs.org/babel-plugin-syntax-async-functions/-/babel-plugin-syntax-async-functions-6.13.0.tgz"
    },
    "babel-plugin-syntax-exponentiation-operator": {
      "version": "6.13.0",
      "from": "babel-plugin-syntax-exponentiation-operator@>=6.8.0 <7.0.0",
      "resolved": "https://registry.npmjs.org/babel-plugin-syntax-exponentiation-operator/-/babel-plugin-syntax-exponentiation-operator-6.13.0.tgz"
    },
    "babel-plugin-syntax-trailing-function-commas": {
      "version": "6.22.0",
      "from": "babel-plugin-syntax-trailing-function-commas@>=6.22.0 <7.0.0",
      "resolved": "https://registry.npmjs.org/babel-plugin-syntax-trailing-function-commas/-/babel-plugin-syntax-trailing-function-commas-6.22.0.tgz"
    },
    "babel-plugin-transform-async-to-generator": {
      "version": "6.24.1",
      "from": "babel-plugin-transform-async-to-generator@>=6.22.0 <7.0.0",
      "resolved": "https://registry.npmjs.org/babel-plugin-transform-async-to-generator/-/babel-plugin-transform-async-to-generator-6.24.1.tgz"
    },
    "babel-plugin-transform-es2015-arrow-functions": {
      "version": "6.22.0",
      "from": "babel-plugin-transform-es2015-arrow-functions@>=6.22.0 <7.0.0",
      "resolved": "https://registry.npmjs.org/babel-plugin-transform-es2015-arrow-functions/-/babel-plugin-transform-es2015-arrow-functions-6.22.0.tgz"
    },
    "babel-plugin-transform-es2015-block-scoped-functions": {
      "version": "6.22.0",
      "from": "babel-plugin-transform-es2015-block-scoped-functions@>=6.22.0 <7.0.0",
      "resolved": "https://registry.npmjs.org/babel-plugin-transform-es2015-block-scoped-functions/-/babel-plugin-transform-es2015-block-scoped-functions-6.22.0.tgz"
    },
    "babel-plugin-transform-es2015-block-scoping": {
      "version": "6.24.1",
      "from": "babel-plugin-transform-es2015-block-scoping@>=6.23.0 <7.0.0",
      "resolved": "https://registry.npmjs.org/babel-plugin-transform-es2015-block-scoping/-/babel-plugin-transform-es2015-block-scoping-6.24.1.tgz"
    },
    "babel-plugin-transform-es2015-classes": {
      "version": "6.24.1",
      "from": "babel-plugin-transform-es2015-classes@>=6.23.0 <7.0.0",
      "resolved": "https://registry.npmjs.org/babel-plugin-transform-es2015-classes/-/babel-plugin-transform-es2015-classes-6.24.1.tgz"
    },
    "babel-plugin-transform-es2015-computed-properties": {
      "version": "6.24.1",
      "from": "babel-plugin-transform-es2015-computed-properties@>=6.22.0 <7.0.0",
      "resolved": "https://registry.npmjs.org/babel-plugin-transform-es2015-computed-properties/-/babel-plugin-transform-es2015-computed-properties-6.24.1.tgz"
    },
    "babel-plugin-transform-es2015-destructuring": {
      "version": "6.23.0",
      "from": "babel-plugin-transform-es2015-destructuring@>=6.23.0 <7.0.0",
      "resolved": "https://registry.npmjs.org/babel-plugin-transform-es2015-destructuring/-/babel-plugin-transform-es2015-destructuring-6.23.0.tgz"
    },
    "babel-plugin-transform-es2015-duplicate-keys": {
      "version": "6.24.1",
      "from": "babel-plugin-transform-es2015-duplicate-keys@>=6.22.0 <7.0.0",
      "resolved": "https://registry.npmjs.org/babel-plugin-transform-es2015-duplicate-keys/-/babel-plugin-transform-es2015-duplicate-keys-6.24.1.tgz"
    },
    "babel-plugin-transform-es2015-for-of": {
      "version": "6.23.0",
      "from": "babel-plugin-transform-es2015-for-of@>=6.23.0 <7.0.0",
      "resolved": "https://registry.npmjs.org/babel-plugin-transform-es2015-for-of/-/babel-plugin-transform-es2015-for-of-6.23.0.tgz"
    },
    "babel-plugin-transform-es2015-function-name": {
      "version": "6.24.1",
      "from": "babel-plugin-transform-es2015-function-name@>=6.22.0 <7.0.0",
      "resolved": "https://registry.npmjs.org/babel-plugin-transform-es2015-function-name/-/babel-plugin-transform-es2015-function-name-6.24.1.tgz"
    },
    "babel-plugin-transform-es2015-literals": {
      "version": "6.22.0",
      "from": "babel-plugin-transform-es2015-literals@>=6.22.0 <7.0.0",
      "resolved": "https://registry.npmjs.org/babel-plugin-transform-es2015-literals/-/babel-plugin-transform-es2015-literals-6.22.0.tgz"
    },
    "babel-plugin-transform-es2015-modules-amd": {
      "version": "6.24.1",
      "from": "babel-plugin-transform-es2015-modules-amd@>=6.22.0 <7.0.0",
      "resolved": "https://registry.npmjs.org/babel-plugin-transform-es2015-modules-amd/-/babel-plugin-transform-es2015-modules-amd-6.24.1.tgz"
    },
    "babel-plugin-transform-es2015-modules-commonjs": {
      "version": "6.24.1",
      "from": "babel-plugin-transform-es2015-modules-commonjs@>=6.23.0 <7.0.0",
      "resolved": "https://registry.npmjs.org/babel-plugin-transform-es2015-modules-commonjs/-/babel-plugin-transform-es2015-modules-commonjs-6.24.1.tgz"
    },
    "babel-plugin-transform-es2015-modules-systemjs": {
      "version": "6.24.1",
      "from": "babel-plugin-transform-es2015-modules-systemjs@>=6.23.0 <7.0.0",
      "resolved": "https://registry.npmjs.org/babel-plugin-transform-es2015-modules-systemjs/-/babel-plugin-transform-es2015-modules-systemjs-6.24.1.tgz"
    },
    "babel-plugin-transform-es2015-modules-umd": {
      "version": "6.24.1",
      "from": "babel-plugin-transform-es2015-modules-umd@>=6.23.0 <7.0.0",
      "resolved": "https://registry.npmjs.org/babel-plugin-transform-es2015-modules-umd/-/babel-plugin-transform-es2015-modules-umd-6.24.1.tgz"
    },
    "babel-plugin-transform-es2015-object-super": {
      "version": "6.24.1",
      "from": "babel-plugin-transform-es2015-object-super@>=6.22.0 <7.0.0",
      "resolved": "https://registry.npmjs.org/babel-plugin-transform-es2015-object-super/-/babel-plugin-transform-es2015-object-super-6.24.1.tgz"
    },
    "babel-plugin-transform-es2015-parameters": {
      "version": "6.24.1",
      "from": "babel-plugin-transform-es2015-parameters@>=6.23.0 <7.0.0",
      "resolved": "https://registry.npmjs.org/babel-plugin-transform-es2015-parameters/-/babel-plugin-transform-es2015-parameters-6.24.1.tgz"
    },
    "babel-plugin-transform-es2015-shorthand-properties": {
      "version": "6.24.1",
      "from": "babel-plugin-transform-es2015-shorthand-properties@>=6.22.0 <7.0.0",
      "resolved": "https://registry.npmjs.org/babel-plugin-transform-es2015-shorthand-properties/-/babel-plugin-transform-es2015-shorthand-properties-6.24.1.tgz"
    },
    "babel-plugin-transform-es2015-spread": {
      "version": "6.22.0",
      "from": "babel-plugin-transform-es2015-spread@>=6.22.0 <7.0.0",
      "resolved": "https://registry.npmjs.org/babel-plugin-transform-es2015-spread/-/babel-plugin-transform-es2015-spread-6.22.0.tgz"
    },
    "babel-plugin-transform-es2015-sticky-regex": {
      "version": "6.24.1",
      "from": "babel-plugin-transform-es2015-sticky-regex@>=6.22.0 <7.0.0",
      "resolved": "https://registry.npmjs.org/babel-plugin-transform-es2015-sticky-regex/-/babel-plugin-transform-es2015-sticky-regex-6.24.1.tgz"
    },
    "babel-plugin-transform-es2015-template-literals": {
      "version": "6.22.0",
      "from": "babel-plugin-transform-es2015-template-literals@>=6.22.0 <7.0.0",
      "resolved": "https://registry.npmjs.org/babel-plugin-transform-es2015-template-literals/-/babel-plugin-transform-es2015-template-literals-6.22.0.tgz"
    },
    "babel-plugin-transform-es2015-typeof-symbol": {
      "version": "6.23.0",
      "from": "babel-plugin-transform-es2015-typeof-symbol@>=6.23.0 <7.0.0",
      "resolved": "https://registry.npmjs.org/babel-plugin-transform-es2015-typeof-symbol/-/babel-plugin-transform-es2015-typeof-symbol-6.23.0.tgz"
    },
    "babel-plugin-transform-es2015-unicode-regex": {
      "version": "6.24.1",
      "from": "babel-plugin-transform-es2015-unicode-regex@>=6.22.0 <7.0.0",
      "resolved": "https://registry.npmjs.org/babel-plugin-transform-es2015-unicode-regex/-/babel-plugin-transform-es2015-unicode-regex-6.24.1.tgz"
    },
    "babel-plugin-transform-exponentiation-operator": {
      "version": "6.24.1",
      "from": "babel-plugin-transform-exponentiation-operator@>=6.22.0 <7.0.0",
      "resolved": "https://registry.npmjs.org/babel-plugin-transform-exponentiation-operator/-/babel-plugin-transform-exponentiation-operator-6.24.1.tgz"
    },
    "babel-plugin-transform-regenerator": {
      "version": "6.24.1",
      "from": "babel-plugin-transform-regenerator@>=6.22.0 <7.0.0",
      "resolved": "https://registry.npmjs.org/babel-plugin-transform-regenerator/-/babel-plugin-transform-regenerator-6.24.1.tgz"
    },
    "babel-plugin-transform-strict-mode": {
      "version": "6.24.1",
      "from": "babel-plugin-transform-strict-mode@>=6.24.1 <7.0.0",
      "resolved": "https://registry.npmjs.org/babel-plugin-transform-strict-mode/-/babel-plugin-transform-strict-mode-6.24.1.tgz"
    },
    "babel-preset-env": {
      "version": "1.6.0",
      "from": "babel-preset-env@>=1.2.2 <2.0.0",
      "resolved": "https://registry.npmjs.org/babel-preset-env/-/babel-preset-env-1.6.0.tgz"
    },
    "babel-register": {
      "version": "6.24.1",
      "from": "babel-register@>=6.24.1 <7.0.0",
      "resolved": "https://registry.npmjs.org/babel-register/-/babel-register-6.24.1.tgz"
    },
    "babel-runtime": {
      "version": "6.23.0",
      "from": "babel-runtime@>=6.22.0 <7.0.0",
      "resolved": "https://registry.npmjs.org/babel-runtime/-/babel-runtime-6.23.0.tgz"
    },
    "babel-template": {
      "version": "6.25.0",
      "from": "babel-template@>=6.25.0 <7.0.0",
      "resolved": "https://registry.npmjs.org/babel-template/-/babel-template-6.25.0.tgz"
    },
    "babel-traverse": {
      "version": "6.25.0",
      "from": "babel-traverse@>=6.25.0 <7.0.0",
      "resolved": "https://registry.npmjs.org/babel-traverse/-/babel-traverse-6.25.0.tgz"
    },
    "babel-types": {
      "version": "6.25.0",
      "from": "babel-types@>=6.25.0 <7.0.0",
      "resolved": "https://registry.npmjs.org/babel-types/-/babel-types-6.25.0.tgz"
    },
    "babylon": {
      "version": "6.17.4",
      "from": "babylon@>=6.17.2 <7.0.0",
      "resolved": "https://registry.npmjs.org/babylon/-/babylon-6.17.4.tgz"
    },
    "balanced-match": {
      "version": "1.0.0",
      "from": "balanced-match@>=1.0.0 <2.0.0",
      "resolved": "https://registry.npmjs.org/balanced-match/-/balanced-match-1.0.0.tgz"
    },
    "base64-js": {
      "version": "1.2.1",
      "from": "base64-js@>=1.0.2 <2.0.0",
      "resolved": "https://registry.npmjs.org/base64-js/-/base64-js-1.2.1.tgz"
    },
    "batch": {
      "version": "0.6.1",
      "from": "batch@0.6.1",
      "resolved": "https://registry.npmjs.org/batch/-/batch-0.6.1.tgz"
    },
    "big.js": {
      "version": "3.1.3",
      "from": "big.js@>=3.1.3 <4.0.0",
      "resolved": "https://registry.npmjs.org/big.js/-/big.js-3.1.3.tgz"
    },
    "binary-extensions": {
      "version": "1.8.0",
      "from": "binary-extensions@>=1.0.0 <2.0.0",
      "resolved": "https://registry.npmjs.org/binary-extensions/-/binary-extensions-1.8.0.tgz"
    },
    "bluebird": {
      "version": "3.5.0",
      "from": "bluebird@>=3.1.1 <4.0.0",
      "resolved": "https://registry.npmjs.org/bluebird/-/bluebird-3.5.0.tgz"
    },
    "bn.js": {
      "version": "4.11.7",
      "from": "bn.js@>=4.1.1 <5.0.0",
      "resolved": "https://registry.npmjs.org/bn.js/-/bn.js-4.11.7.tgz"
    },
    "bonjour": {
      "version": "3.5.0",
      "from": "bonjour@>=3.5.0 <4.0.0",
      "resolved": "https://registry.npmjs.org/bonjour/-/bonjour-3.5.0.tgz"
    },
    "boolbase": {
      "version": "1.0.0",
      "from": "boolbase@>=1.0.0 <1.1.0",
      "resolved": "https://registry.npmjs.org/boolbase/-/boolbase-1.0.0.tgz"
    },
    "brace-expansion": {
      "version": "1.1.8",
      "from": "brace-expansion@>=1.1.7 <2.0.0",
      "resolved": "https://registry.npmjs.org/brace-expansion/-/brace-expansion-1.1.8.tgz"
    },
    "braces": {
      "version": "1.8.5",
      "from": "braces@>=1.8.2 <2.0.0",
      "resolved": "https://registry.npmjs.org/braces/-/braces-1.8.5.tgz"
    },
    "brorand": {
      "version": "1.1.0",
      "from": "brorand@>=1.0.1 <2.0.0",
      "resolved": "https://registry.npmjs.org/brorand/-/brorand-1.1.0.tgz"
    },
    "browserify-aes": {
      "version": "1.0.6",
      "from": "browserify-aes@>=1.0.4 <2.0.0",
      "resolved": "https://registry.npmjs.org/browserify-aes/-/browserify-aes-1.0.6.tgz"
    },
    "browserify-cipher": {
      "version": "1.0.0",
      "from": "browserify-cipher@>=1.0.0 <2.0.0",
      "resolved": "https://registry.npmjs.org/browserify-cipher/-/browserify-cipher-1.0.0.tgz"
    },
    "browserify-des": {
      "version": "1.0.0",
      "from": "browserify-des@>=1.0.0 <2.0.0",
      "resolved": "https://registry.npmjs.org/browserify-des/-/browserify-des-1.0.0.tgz"
    },
    "browserify-rsa": {
      "version": "4.0.1",
      "from": "browserify-rsa@>=4.0.0 <5.0.0",
      "resolved": "https://registry.npmjs.org/browserify-rsa/-/browserify-rsa-4.0.1.tgz"
    },
    "browserify-sign": {
      "version": "4.0.4",
      "from": "browserify-sign@>=4.0.0 <5.0.0",
      "resolved": "https://registry.npmjs.org/browserify-sign/-/browserify-sign-4.0.4.tgz"
    },
    "browserify-zlib": {
      "version": "0.1.4",
      "from": "browserify-zlib@>=0.1.4 <0.2.0",
      "resolved": "https://registry.npmjs.org/browserify-zlib/-/browserify-zlib-0.1.4.tgz"
    },
    "browserslist": {
      "version": "2.1.5",
      "from": "browserslist@>=2.1.2 <3.0.0",
      "resolved": "https://registry.npmjs.org/browserslist/-/browserslist-2.1.5.tgz"
    },
    "buffer": {
      "version": "4.9.1",
      "from": "buffer@>=4.3.0 <5.0.0",
      "resolved": "https://registry.npmjs.org/buffer/-/buffer-4.9.1.tgz",
      "dependencies": {
        "isarray": {
          "version": "1.0.0",
          "from": "isarray@>=1.0.0 <2.0.0",
          "resolved": "https://registry.npmjs.org/isarray/-/isarray-1.0.0.tgz"
        }
      }
    },
    "buffer-indexof": {
      "version": "1.1.0",
      "from": "buffer-indexof@>=1.0.0 <2.0.0",
      "resolved": "https://registry.npmjs.org/buffer-indexof/-/buffer-indexof-1.1.0.tgz"
    },
    "buffer-xor": {
      "version": "1.0.3",
      "from": "buffer-xor@>=1.0.2 <2.0.0",
      "resolved": "https://registry.npmjs.org/buffer-xor/-/buffer-xor-1.0.3.tgz"
    },
    "builtin-modules": {
      "version": "1.1.1",
      "from": "builtin-modules@>=1.0.0 <2.0.0",
      "resolved": "https://registry.npmjs.org/builtin-modules/-/builtin-modules-1.1.1.tgz"
    },
    "builtin-status-codes": {
      "version": "3.0.0",
      "from": "builtin-status-codes@>=3.0.0 <4.0.0",
      "resolved": "https://registry.npmjs.org/builtin-status-codes/-/builtin-status-codes-3.0.0.tgz"
    },
    "bytes": {
      "version": "2.5.0",
      "from": "bytes@2.5.0",
      "resolved": "https://registry.npmjs.org/bytes/-/bytes-2.5.0.tgz"
    },
    "camelcase": {
      "version": "4.1.0",
      "from": "camelcase@>=4.0.0 <5.0.0",
      "resolved": "https://registry.npmjs.org/camelcase/-/camelcase-4.1.0.tgz"
    },
    "camelcase-keys": {
      "version": "2.1.0",
      "from": "camelcase-keys@>=2.0.0 <3.0.0",
      "resolved": "https://registry.npmjs.org/camelcase-keys/-/camelcase-keys-2.1.0.tgz",
      "dependencies": {
        "camelcase": {
          "version": "2.1.1",
          "from": "camelcase@>=2.0.0 <3.0.0",
          "resolved": "https://registry.npmjs.org/camelcase/-/camelcase-2.1.1.tgz"
        }
      }
    },
    "caniuse-api": {
      "version": "1.6.1",
      "from": "caniuse-api@>=1.5.2 <2.0.0",
      "resolved": "https://registry.npmjs.org/caniuse-api/-/caniuse-api-1.6.1.tgz",
      "dependencies": {
        "browserslist": {
          "version": "1.7.7",
          "from": "browserslist@>=1.3.6 <2.0.0",
          "resolved": "https://registry.npmjs.org/browserslist/-/browserslist-1.7.7.tgz"
        }
      }
    },
    "caniuse-db": {
      "version": "1.0.30000701",
      "from": "caniuse-db@>=1.0.30000634 <2.0.0",
      "resolved": "https://registry.npmjs.org/caniuse-db/-/caniuse-db-1.0.30000701.tgz"
    },
    "caniuse-lite": {
      "version": "1.0.30000701",
      "from": "caniuse-lite@>=1.0.30000684 <2.0.0",
      "resolved": "https://registry.npmjs.org/caniuse-lite/-/caniuse-lite-1.0.30000701.tgz"
    },
    "center-align": {
      "version": "0.1.3",
      "from": "center-align@>=0.1.1 <0.2.0",
      "resolved": "https://registry.npmjs.org/center-align/-/center-align-0.1.3.tgz"
    },
    "chalk": {
      "version": "1.1.3",
      "from": "chalk@>=1.1.3 <2.0.0",
      "resolved": "https://registry.npmjs.org/chalk/-/chalk-1.1.3.tgz"
    },
    "chokidar": {
      "version": "1.7.0",
      "from": "chokidar@>=1.7.0 <2.0.0",
      "resolved": "https://registry.npmjs.org/chokidar/-/chokidar-1.7.0.tgz"
    },
    "cipher-base": {
      "version": "1.0.4",
      "from": "cipher-base@>=1.0.0 <2.0.0",
      "resolved": "https://registry.npmjs.org/cipher-base/-/cipher-base-1.0.4.tgz"
    },
    "clap": {
      "version": "1.2.0",
      "from": "clap@>=1.0.9 <2.0.0",
      "resolved": "https://registry.npmjs.org/clap/-/clap-1.2.0.tgz"
    },
    "clean-webpack-plugin": {
      "version": "0.1.16",
      "from": "clean-webpack-plugin@>=0.1.16 <0.2.0",
      "resolved": "https://registry.npmjs.org/clean-webpack-plugin/-/clean-webpack-plugin-0.1.16.tgz"
    },
    "cliui": {
      "version": "2.1.0",
      "from": "cliui@>=2.1.0 <3.0.0",
      "resolved": "https://registry.npmjs.org/cliui/-/cliui-2.1.0.tgz"
    },
    "clone": {
      "version": "1.0.2",
      "from": "clone@>=1.0.2 <2.0.0",
      "resolved": "https://registry.npmjs.org/clone/-/clone-1.0.2.tgz"
    },
    "co": {
      "version": "4.6.0",
      "from": "co@>=4.6.0 <5.0.0",
      "resolved": "https://registry.npmjs.org/co/-/co-4.6.0.tgz"
    },
    "coa": {
      "version": "1.0.4",
      "from": "coa@>=1.0.1 <1.1.0",
      "resolved": "https://registry.npmjs.org/coa/-/coa-1.0.4.tgz"
    },
    "code-point-at": {
      "version": "1.1.0",
      "from": "code-point-at@>=1.0.0 <2.0.0",
      "resolved": "https://registry.npmjs.org/code-point-at/-/code-point-at-1.1.0.tgz"
    },
    "color": {
      "version": "0.11.4",
      "from": "color@>=0.11.0 <0.12.0",
      "resolved": "https://registry.npmjs.org/color/-/color-0.11.4.tgz"
    },
    "color-convert": {
      "version": "1.9.0",
      "from": "color-convert@>=1.3.0 <2.0.0",
      "resolved": "https://registry.npmjs.org/color-convert/-/color-convert-1.9.0.tgz"
    },
    "color-name": {
      "version": "1.1.3",
      "from": "color-name@>=1.1.1 <2.0.0",
      "resolved": "https://registry.npmjs.org/color-name/-/color-name-1.1.3.tgz"
    },
    "color-string": {
      "version": "0.3.0",
      "from": "color-string@>=0.3.0 <0.4.0",
      "resolved": "https://registry.npmjs.org/color-string/-/color-string-0.3.0.tgz"
    },
    "colormin": {
      "version": "1.1.2",
      "from": "colormin@>=1.0.5 <2.0.0",
      "resolved": "https://registry.npmjs.org/colormin/-/colormin-1.1.2.tgz"
    },
    "colors": {
      "version": "1.1.2",
      "from": "colors@>=1.1.2 <1.2.0",
      "resolved": "https://registry.npmjs.org/colors/-/colors-1.1.2.tgz"
    },
    "commander": {
      "version": "2.11.0",
      "from": "commander@>=2.9.0 <3.0.0",
      "resolved": "https://registry.npmjs.org/commander/-/commander-2.11.0.tgz"
    },
    "commondir": {
      "version": "1.0.1",
      "from": "commondir@>=1.0.1 <2.0.0",
      "resolved": "https://registry.npmjs.org/commondir/-/commondir-1.0.1.tgz"
    },
    "compressible": {
      "version": "2.0.10",
      "from": "compressible@>=2.0.10 <2.1.0",
      "resolved": "https://registry.npmjs.org/compressible/-/compressible-2.0.10.tgz"
    },
    "compression": {
      "version": "1.7.0",
      "from": "compression@>=1.5.2 <2.0.0",
      "resolved": "https://registry.npmjs.org/compression/-/compression-1.7.0.tgz"
    },
    "concat-map": {
      "version": "0.0.1",
      "from": "concat-map@0.0.1",
      "resolved": "https://registry.npmjs.org/concat-map/-/concat-map-0.0.1.tgz"
    },
    "config-chain": {
      "version": "1.1.11",
      "from": "config-chain@>=1.1.5 <1.2.0",
      "resolved": "https://registry.npmjs.org/config-chain/-/config-chain-1.1.11.tgz"
    },
    "connect-history-api-fallback": {
      "version": "1.3.0",
      "from": "connect-history-api-fallback@>=1.3.0 <2.0.0",
      "resolved": "https://registry.npmjs.org/connect-history-api-fallback/-/connect-history-api-fallback-1.3.0.tgz"
    },
    "console-browserify": {
      "version": "1.1.0",
      "from": "console-browserify@>=1.1.0 <2.0.0",
      "resolved": "https://registry.npmjs.org/console-browserify/-/console-browserify-1.1.0.tgz"
    },
    "consolidate": {
      "version": "0.14.5",
      "from": "consolidate@>=0.14.0 <0.15.0",
      "resolved": "https://registry.npmjs.org/consolidate/-/consolidate-0.14.5.tgz"
    },
    "constants-browserify": {
      "version": "1.0.0",
      "from": "constants-browserify@>=1.0.0 <2.0.0",
      "resolved": "https://registry.npmjs.org/constants-browserify/-/constants-browserify-1.0.0.tgz"
    },
    "content-disposition": {
      "version": "0.5.2",
      "from": "content-disposition@0.5.2",
      "resolved": "https://registry.npmjs.org/content-disposition/-/content-disposition-0.5.2.tgz"
    },
    "content-type": {
      "version": "1.0.2",
      "from": "content-type@>=1.0.2 <1.1.0",
      "resolved": "https://registry.npmjs.org/content-type/-/content-type-1.0.2.tgz"
    },
    "convert-source-map": {
      "version": "1.5.0",
      "from": "convert-source-map@>=1.1.0 <2.0.0",
      "resolved": "https://registry.npmjs.org/convert-source-map/-/convert-source-map-1.5.0.tgz"
    },
    "cookie": {
      "version": "0.3.1",
      "from": "cookie@0.3.1",
      "resolved": "https://registry.npmjs.org/cookie/-/cookie-0.3.1.tgz"
    },
    "cookie-signature": {
      "version": "1.0.6",
      "from": "cookie-signature@1.0.6",
      "resolved": "https://registry.npmjs.org/cookie-signature/-/cookie-signature-1.0.6.tgz"
    },
    "core-js": {
      "version": "2.4.1",
      "from": "core-js@>=2.4.0 <3.0.0",
      "resolved": "https://registry.npmjs.org/core-js/-/core-js-2.4.1.tgz"
    },
    "core-util-is": {
      "version": "1.0.2",
      "from": "core-util-is@>=1.0.0 <1.1.0",
      "resolved": "https://registry.npmjs.org/core-util-is/-/core-util-is-1.0.2.tgz"
    },
    "cosmiconfig": {
      "version": "2.2.2",
      "from": "cosmiconfig@>=2.1.0 <3.0.0",
      "resolved": "https://registry.npmjs.org/cosmiconfig/-/cosmiconfig-2.2.2.tgz",
      "dependencies": {
        "minimist": {
          "version": "1.2.0",
          "from": "minimist@>=1.2.0 <2.0.0",
          "resolved": "https://registry.npmjs.org/minimist/-/minimist-1.2.0.tgz"
        }
      }
    },
    "create-ecdh": {
      "version": "4.0.0",
      "from": "create-ecdh@>=4.0.0 <5.0.0",
      "resolved": "https://registry.npmjs.org/create-ecdh/-/create-ecdh-4.0.0.tgz"
    },
    "create-hash": {
      "version": "1.1.3",
      "from": "create-hash@>=1.1.0 <2.0.0",
      "resolved": "https://registry.npmjs.org/create-hash/-/create-hash-1.1.3.tgz"
    },
    "create-hmac": {
      "version": "1.1.6",
      "from": "create-hmac@>=1.1.0 <2.0.0",
      "resolved": "https://registry.npmjs.org/create-hmac/-/create-hmac-1.1.6.tgz"
    },
    "cross-spawn": {
      "version": "4.0.2",
      "from": "cross-spawn@>=4.0.0 <5.0.0",
      "resolved": "https://registry.npmjs.org/cross-spawn/-/cross-spawn-4.0.2.tgz"
    },
    "crypto-browserify": {
      "version": "3.11.1",
      "from": "crypto-browserify@>=3.11.0 <4.0.0",
      "resolved": "https://registry.npmjs.org/crypto-browserify/-/crypto-browserify-3.11.1.tgz"
    },
    "css": {
      "version": "2.2.1",
      "from": "css@>=2.0.0 <3.0.0",
      "resolved": "https://registry.npmjs.org/css/-/css-2.2.1.tgz",
      "dependencies": {
        "source-map": {
          "version": "0.1.43",
          "from": "source-map@>=0.1.38 <0.2.0",
          "resolved": "https://registry.npmjs.org/source-map/-/source-map-0.1.43.tgz"
        }
      }
    },
    "css-color-names": {
      "version": "0.0.4",
      "from": "css-color-names@0.0.4",
      "resolved": "https://registry.npmjs.org/css-color-names/-/css-color-names-0.0.4.tgz"
    },
    "css-loader": {
      "version": "0.26.4",
      "from": "css-loader@>=0.26.2 <0.27.0",
      "resolved": "https://registry.npmjs.org/css-loader/-/css-loader-0.26.4.tgz"
    },
    "css-select": {
      "version": "1.2.0",
      "from": "css-select@>=1.1.0 <2.0.0",
      "resolved": "https://registry.npmjs.org/css-select/-/css-select-1.2.0.tgz"
    },
    "css-selector-tokenizer": {
      "version": "0.7.0",
      "from": "css-selector-tokenizer@>=0.7.0 <0.8.0",
      "resolved": "https://registry.npmjs.org/css-selector-tokenizer/-/css-selector-tokenizer-0.7.0.tgz",
      "dependencies": {
        "regexpu-core": {
          "version": "1.0.0",
          "from": "regexpu-core@>=1.0.0 <2.0.0",
          "resolved": "https://registry.npmjs.org/regexpu-core/-/regexpu-core-1.0.0.tgz"
        }
      }
    },
    "css-what": {
      "version": "2.1.0",
      "from": "css-what@>=2.1.0 <2.2.0",
      "resolved": "https://registry.npmjs.org/css-what/-/css-what-2.1.0.tgz"
    },
    "cssesc": {
      "version": "0.1.0",
      "from": "cssesc@>=0.1.0 <0.2.0",
      "resolved": "https://registry.npmjs.org/cssesc/-/cssesc-0.1.0.tgz"
    },
    "cssnano": {
      "version": "3.10.0",
      "from": "cssnano@>=2.6.1 <4.0.0",
      "resolved": "https://registry.npmjs.org/cssnano/-/cssnano-3.10.0.tgz"
    },
    "csso": {
      "version": "2.3.2",
      "from": "csso@>=2.3.1 <2.4.0",
      "resolved": "https://registry.npmjs.org/csso/-/csso-2.3.2.tgz"
    },
    "currently-unhandled": {
      "version": "0.4.1",
      "from": "currently-unhandled@>=0.4.1 <0.5.0",
      "resolved": "https://registry.npmjs.org/currently-unhandled/-/currently-unhandled-0.4.1.tgz"
    },
    "date-now": {
      "version": "0.1.4",
      "from": "date-now@>=0.1.4 <0.2.0",
      "resolved": "https://registry.npmjs.org/date-now/-/date-now-0.1.4.tgz"
    },
    "de-indent": {
      "version": "1.0.2",
      "from": "de-indent@>=1.0.2 <2.0.0",
      "resolved": "https://registry.npmjs.org/de-indent/-/de-indent-1.0.2.tgz"
    },
    "debug": {
      "version": "2.6.8",
      "from": "debug@>=2.1.1 <3.0.0",
      "resolved": "https://registry.npmjs.org/debug/-/debug-2.6.8.tgz"
    },
    "decamelize": {
      "version": "1.2.0",
      "from": "decamelize@>=1.1.2 <2.0.0",
      "resolved": "https://registry.npmjs.org/decamelize/-/decamelize-1.2.0.tgz"
    },
    "decompress-response": {
      "version": "3.3.0",
      "from": "decompress-response@>=3.2.0 <4.0.0",
      "resolved": "https://registry.npmjs.org/decompress-response/-/decompress-response-3.3.0.tgz"
    },
    "deep-equal": {
      "version": "1.0.1",
      "from": "deep-equal@>=1.0.1 <2.0.0",
      "resolved": "https://registry.npmjs.org/deep-equal/-/deep-equal-1.0.1.tgz"
    },
    "defined": {
      "version": "1.0.0",
      "from": "defined@>=1.0.0 <2.0.0",
      "resolved": "https://registry.npmjs.org/defined/-/defined-1.0.0.tgz"
    },
    "del": {
      "version": "3.0.0",
      "from": "del@>=3.0.0 <4.0.0",
      "resolved": "https://registry.npmjs.org/del/-/del-3.0.0.tgz",
      "dependencies": {
        "pify": {
          "version": "3.0.0",
          "from": "pify@>=3.0.0 <4.0.0",
          "resolved": "https://registry.npmjs.org/pify/-/pify-3.0.0.tgz"
        }
      }
    },
    "depd": {
      "version": "1.1.0",
      "from": "depd@>=1.1.0 <1.2.0",
      "resolved": "https://registry.npmjs.org/depd/-/depd-1.1.0.tgz"
    },
    "des.js": {
      "version": "1.0.0",
      "from": "des.js@>=1.0.0 <2.0.0",
      "resolved": "https://registry.npmjs.org/des.js/-/des.js-1.0.0.tgz"
    },
    "destroy": {
      "version": "1.0.4",
      "from": "destroy@>=1.0.4 <1.1.0",
      "resolved": "https://registry.npmjs.org/destroy/-/destroy-1.0.4.tgz"
    },
    "detect-indent": {
      "version": "4.0.0",
      "from": "detect-indent@>=4.0.0 <5.0.0",
      "resolved": "https://registry.npmjs.org/detect-indent/-/detect-indent-4.0.0.tgz"
    },
    "detect-node": {
      "version": "2.0.3",
      "from": "detect-node@>=2.0.3 <3.0.0",
      "resolved": "https://registry.npmjs.org/detect-node/-/detect-node-2.0.3.tgz"
    },
    "diffie-hellman": {
      "version": "5.0.2",
      "from": "diffie-hellman@>=5.0.0 <6.0.0",
      "resolved": "https://registry.npmjs.org/diffie-hellman/-/diffie-hellman-5.0.2.tgz"
    },
    "dns-equal": {
      "version": "1.0.0",
      "from": "dns-equal@>=1.0.0 <2.0.0",
      "resolved": "https://registry.npmjs.org/dns-equal/-/dns-equal-1.0.0.tgz"
    },
    "dns-packet": {
      "version": "1.1.1",
      "from": "dns-packet@>=1.0.1 <2.0.0",
      "resolved": "https://registry.npmjs.org/dns-packet/-/dns-packet-1.1.1.tgz"
    },
    "dns-txt": {
      "version": "2.0.2",
      "from": "dns-txt@>=2.0.2 <3.0.0",
      "resolved": "https://registry.npmjs.org/dns-txt/-/dns-txt-2.0.2.tgz"
    },
    "dom-converter": {
      "version": "0.1.4",
      "from": "dom-converter@>=0.1.0 <0.2.0",
      "resolved": "https://registry.npmjs.org/dom-converter/-/dom-converter-0.1.4.tgz",
      "dependencies": {
        "utila": {
          "version": "0.3.3",
          "from": "utila@>=0.3.0 <0.4.0",
          "resolved": "https://registry.npmjs.org/utila/-/utila-0.3.3.tgz"
        }
      }
    },
    "dom-serializer": {
      "version": "0.1.0",
      "from": "dom-serializer@>=0.0.0 <1.0.0",
      "resolved": "https://registry.npmjs.org/dom-serializer/-/dom-serializer-0.1.0.tgz",
      "dependencies": {
        "domelementtype": {
          "version": "1.1.3",
          "from": "domelementtype@>=1.1.1 <1.2.0",
          "resolved": "https://registry.npmjs.org/domelementtype/-/domelementtype-1.1.3.tgz"
        }
      }
    },
    "domain-browser": {
      "version": "1.1.7",
      "from": "domain-browser@>=1.1.1 <2.0.0",
      "resolved": "https://registry.npmjs.org/domain-browser/-/domain-browser-1.1.7.tgz"
    },
    "domelementtype": {
      "version": "1.3.0",
      "from": "domelementtype@>=1.0.0 <2.0.0",
      "resolved": "https://registry.npmjs.org/domelementtype/-/domelementtype-1.3.0.tgz"
    },
    "domhandler": {
      "version": "2.1.0",
      "from": "domhandler@>=2.1.0 <2.2.0",
      "resolved": "https://registry.npmjs.org/domhandler/-/domhandler-2.1.0.tgz"
    },
    "domutils": {
      "version": "1.5.1",
      "from": "domutils@1.5.1",
      "resolved": "https://registry.npmjs.org/domutils/-/domutils-1.5.1.tgz"
    },
    "duplexer3": {
      "version": "0.1.4",
      "from": "duplexer3@>=0.1.4 <0.2.0",
      "resolved": "https://registry.npmjs.org/duplexer3/-/duplexer3-0.1.4.tgz"
    },
    "editorconfig": {
      "version": "0.13.2",
      "from": "editorconfig@>=0.13.2 <0.14.0",
      "resolved": "https://registry.npmjs.org/editorconfig/-/editorconfig-0.13.2.tgz",
      "dependencies": {
        "lru-cache": {
          "version": "3.2.0",
          "from": "lru-cache@>=3.2.0 <4.0.0",
          "resolved": "https://registry.npmjs.org/lru-cache/-/lru-cache-3.2.0.tgz"
        }
      }
    },
    "ee-first": {
      "version": "1.1.1",
      "from": "ee-first@1.1.1",
      "resolved": "https://registry.npmjs.org/ee-first/-/ee-first-1.1.1.tgz"
    },
    "electron-to-chromium": {
      "version": "1.3.15",
      "from": "electron-to-chromium@>=1.3.14 <2.0.0",
      "resolved": "https://registry.npmjs.org/electron-to-chromium/-/electron-to-chromium-1.3.15.tgz"
    },
    "elliptic": {
      "version": "6.4.0",
      "from": "elliptic@>=6.0.0 <7.0.0",
      "resolved": "https://registry.npmjs.org/elliptic/-/elliptic-6.4.0.tgz"
    },
    "emojis-list": {
      "version": "2.1.0",
      "from": "emojis-list@>=2.0.0 <3.0.0",
      "resolved": "https://registry.npmjs.org/emojis-list/-/emojis-list-2.1.0.tgz"
    },
    "encodeurl": {
      "version": "1.0.1",
      "from": "encodeurl@>=1.0.1 <1.1.0",
      "resolved": "https://registry.npmjs.org/encodeurl/-/encodeurl-1.0.1.tgz"
    },
    "enhanced-resolve": {
      "version": "3.3.0",
      "from": "enhanced-resolve@>=3.3.0 <4.0.0",
      "resolved": "https://registry.npmjs.org/enhanced-resolve/-/enhanced-resolve-3.3.0.tgz"
    },
    "entities": {
      "version": "1.1.1",
      "from": "entities@>=1.1.1 <1.2.0",
      "resolved": "https://registry.npmjs.org/entities/-/entities-1.1.1.tgz"
    },
    "errno": {
      "version": "0.1.4",
      "from": "errno@>=0.1.3 <0.2.0",
      "resolved": "https://registry.npmjs.org/errno/-/errno-0.1.4.tgz"
    },
    "error-ex": {
      "version": "1.3.1",
      "from": "error-ex@>=1.2.0 <2.0.0",
      "resolved": "https://registry.npmjs.org/error-ex/-/error-ex-1.3.1.tgz"
    },
    "error-stack-parser": {
      "version": "2.0.1",
      "from": "error-stack-parser@>=2.0.0 <3.0.0",
      "resolved": "https://registry.npmjs.org/error-stack-parser/-/error-stack-parser-2.0.1.tgz"
    },
    "escape-html": {
      "version": "1.0.3",
      "from": "escape-html@>=1.0.3 <1.1.0",
      "resolved": "https://registry.npmjs.org/escape-html/-/escape-html-1.0.3.tgz"
    },
    "escape-string-regexp": {
      "version": "1.0.5",
      "from": "escape-string-regexp@>=1.0.2 <2.0.0",
      "resolved": "https://registry.npmjs.org/escape-string-regexp/-/escape-string-regexp-1.0.5.tgz"
    },
    "esprima": {
      "version": "2.7.3",
      "from": "esprima@>=2.6.0 <3.0.0",
      "resolved": "https://registry.npmjs.org/esprima/-/esprima-2.7.3.tgz"
    },
    "esutils": {
      "version": "2.0.2",
      "from": "esutils@>=2.0.2 <3.0.0",
      "resolved": "https://registry.npmjs.org/esutils/-/esutils-2.0.2.tgz"
    },
    "etag": {
      "version": "1.8.0",
      "from": "etag@>=1.8.0 <1.9.0",
      "resolved": "https://registry.npmjs.org/etag/-/etag-1.8.0.tgz"
    },
    "eventemitter3": {
      "version": "1.2.0",
      "from": "eventemitter3@>=1.0.0 <2.0.0",
      "resolved": "https://registry.npmjs.org/eventemitter3/-/eventemitter3-1.2.0.tgz"
    },
    "events": {
      "version": "1.1.1",
      "from": "events@>=1.0.0 <2.0.0",
      "resolved": "https://registry.npmjs.org/events/-/events-1.1.1.tgz"
    },
    "eventsource": {
      "version": "0.1.6",
      "from": "eventsource@0.1.6",
      "resolved": "https://registry.npmjs.org/eventsource/-/eventsource-0.1.6.tgz"
    },
    "evp_bytestokey": {
      "version": "1.0.0",
      "from": "evp_bytestokey@>=1.0.0 <2.0.0",
      "resolved": "https://registry.npmjs.org/evp_bytestokey/-/evp_bytestokey-1.0.0.tgz"
    },
    "execa": {
      "version": "0.5.1",
      "from": "execa@>=0.5.0 <0.6.0",
      "resolved": "https://registry.npmjs.org/execa/-/execa-0.5.1.tgz"
    },
    "expand-brackets": {
      "version": "0.1.5",
      "from": "expand-brackets@>=0.1.4 <0.2.0",
      "resolved": "https://registry.npmjs.org/expand-brackets/-/expand-brackets-0.1.5.tgz"
    },
    "expand-range": {
      "version": "1.8.2",
      "from": "expand-range@>=1.8.1 <2.0.0",
      "resolved": "https://registry.npmjs.org/expand-range/-/expand-range-1.8.2.tgz"
    },
    "express": {
      "version": "4.15.3",
      "from": "express@>=4.13.3 <5.0.0",
      "resolved": "https://registry.npmjs.org/express/-/express-4.15.3.tgz",
      "dependencies": {
        "array-flatten": {
          "version": "1.1.1",
          "from": "array-flatten@1.1.1",
          "resolved": "https://registry.npmjs.org/array-flatten/-/array-flatten-1.1.1.tgz"
        },
        "debug": {
          "version": "2.6.7",
          "from": "debug@2.6.7",
          "resolved": "https://registry.npmjs.org/debug/-/debug-2.6.7.tgz"
        }
      }
    },
    "extglob": {
      "version": "0.3.2",
      "from": "extglob@>=0.3.1 <0.4.0",
      "resolved": "https://registry.npmjs.org/extglob/-/extglob-0.3.2.tgz"
    },
    "extract-text-webpack-plugin": {
      "version": "2.1.2",
      "from": "extract-text-webpack-plugin@>=2.1.0 <3.0.0",
      "resolved": "https://registry.npmjs.org/extract-text-webpack-plugin/-/extract-text-webpack-plugin-2.1.2.tgz"
    },
    "fast-deep-equal": {
      "version": "1.0.0",
      "from": "fast-deep-equal@>=1.0.0 <2.0.0",
      "resolved": "https://registry.npmjs.org/fast-deep-equal/-/fast-deep-equal-1.0.0.tgz"
    },
    "fastparse": {
      "version": "1.1.1",
      "from": "fastparse@>=1.1.1 <2.0.0",
      "resolved": "https://registry.npmjs.org/fastparse/-/fastparse-1.1.1.tgz"
    },
    "faye-websocket": {
      "version": "0.10.0",
      "from": "faye-websocket@>=0.10.0 <0.11.0",
      "resolved": "https://registry.npmjs.org/faye-websocket/-/faye-websocket-0.10.0.tgz"
    },
    "file-loader": {
      "version": "0.10.1",
      "from": "file-loader@>=0.10.1 <0.11.0",
      "resolved": "https://registry.npmjs.org/file-loader/-/file-loader-0.10.1.tgz"
    },
    "filename-regex": {
      "version": "2.0.1",
      "from": "filename-regex@>=2.0.0 <3.0.0",
      "resolved": "https://registry.npmjs.org/filename-regex/-/filename-regex-2.0.1.tgz"
    },
    "fill-range": {
      "version": "2.2.3",
      "from": "fill-range@>=2.1.0 <3.0.0",
      "resolved": "https://registry.npmjs.org/fill-range/-/fill-range-2.2.3.tgz"
    },
    "finalhandler": {
      "version": "1.0.3",
      "from": "finalhandler@>=1.0.3 <1.1.0",
      "resolved": "https://registry.npmjs.org/finalhandler/-/finalhandler-1.0.3.tgz",
      "dependencies": {
        "debug": {
          "version": "2.6.7",
          "from": "debug@2.6.7",
          "resolved": "https://registry.npmjs.org/debug/-/debug-2.6.7.tgz"
        }
      }
    },
    "find-cache-dir": {
      "version": "1.0.0",
      "from": "find-cache-dir@>=1.0.0 <2.0.0",
      "resolved": "https://registry.npmjs.org/find-cache-dir/-/find-cache-dir-1.0.0.tgz"
    },
    "find-up": {
      "version": "2.1.0",
      "from": "find-up@>=2.1.0 <3.0.0",
      "resolved": "https://registry.npmjs.org/find-up/-/find-up-2.1.0.tgz"
    },
    "flatten": {
      "version": "1.0.2",
      "from": "flatten@>=1.0.2 <2.0.0",
      "resolved": "https://registry.npmjs.org/flatten/-/flatten-1.0.2.tgz"
    },
    "for-in": {
      "version": "1.0.2",
      "from": "for-in@>=1.0.1 <2.0.0",
      "resolved": "https://registry.npmjs.org/for-in/-/for-in-1.0.2.tgz"
    },
    "for-own": {
      "version": "0.1.5",
      "from": "for-own@>=0.1.4 <0.2.0",
      "resolved": "https://registry.npmjs.org/for-own/-/for-own-0.1.5.tgz"
    },
    "forwarded": {
      "version": "0.1.0",
      "from": "forwarded@>=0.1.0 <0.2.0",
      "resolved": "https://registry.npmjs.org/forwarded/-/forwarded-0.1.0.tgz"
    },
    "fresh": {
      "version": "0.5.0",
      "from": "fresh@0.5.0",
      "resolved": "https://registry.npmjs.org/fresh/-/fresh-0.5.0.tgz"
    },
    "friendly-errors-webpack-plugin": {
      "version": "1.6.1",
      "from": "friendly-errors-webpack-plugin@>=1.6.1 <2.0.0",
      "resolved": "https://registry.npmjs.org/friendly-errors-webpack-plugin/-/friendly-errors-webpack-plugin-1.6.1.tgz"
    },
    "fs-extra": {
      "version": "2.1.2",
      "from": "fs-extra@>=2.0.0 <3.0.0",
      "resolved": "https://registry.npmjs.org/fs-extra/-/fs-extra-2.1.2.tgz"
    },
    "fs.realpath": {
      "version": "1.0.0",
      "from": "fs.realpath@>=1.0.0 <2.0.0",
      "resolved": "https://registry.npmjs.org/fs.realpath/-/fs.realpath-1.0.0.tgz"
    },
    "fsevents": {
      "version": "1.1.2",
      "from": "fsevents@>=1.0.0 <2.0.0",
      "resolved": "https://registry.npmjs.org/fsevents/-/fsevents-1.1.2.tgz",
      "optional": true,
      "dependencies": {
        "abbrev": {
          "version": "1.1.0",
          "from": "abbrev@1.1.0",
          "resolved": "https://registry.npmjs.org/abbrev/-/abbrev-1.1.0.tgz",
          "optional": true
        },
        "ajv": {
          "version": "4.11.8",
          "from": "ajv@4.11.8",
          "resolved": "https://registry.npmjs.org/ajv/-/ajv-4.11.8.tgz",
          "optional": true
        },
        "ansi-regex": {
          "version": "2.1.1",
          "from": "ansi-regex@2.1.1",
          "resolved": "https://registry.npmjs.org/ansi-regex/-/ansi-regex-2.1.1.tgz"
        },
        "aproba": {
          "version": "1.1.1",
          "from": "aproba@1.1.1",
          "resolved": "https://registry.npmjs.org/aproba/-/aproba-1.1.1.tgz",
          "optional": true
        },
        "are-we-there-yet": {
          "version": "1.1.4",
          "from": "are-we-there-yet@1.1.4",
          "resolved": "https://registry.npmjs.org/are-we-there-yet/-/are-we-there-yet-1.1.4.tgz",
          "optional": true
        },
        "asn1": {
          "version": "0.2.3",
          "from": "asn1@0.2.3",
          "resolved": "https://registry.npmjs.org/asn1/-/asn1-0.2.3.tgz",
          "optional": true
        },
        "assert-plus": {
          "version": "0.2.0",
          "from": "assert-plus@0.2.0",
          "resolved": "https://registry.npmjs.org/assert-plus/-/assert-plus-0.2.0.tgz",
          "optional": true
        },
        "asynckit": {
          "version": "0.4.0",
          "from": "asynckit@0.4.0",
          "resolved": "https://registry.npmjs.org/asynckit/-/asynckit-0.4.0.tgz",
          "optional": true
        },
        "aws-sign2": {
          "version": "0.6.0",
          "from": "aws-sign2@0.6.0",
          "resolved": "https://registry.npmjs.org/aws-sign2/-/aws-sign2-0.6.0.tgz",
          "optional": true
        },
        "aws4": {
          "version": "1.6.0",
          "from": "aws4@1.6.0",
          "resolved": "https://registry.npmjs.org/aws4/-/aws4-1.6.0.tgz",
          "optional": true
        },
        "balanced-match": {
          "version": "0.4.2",
          "from": "balanced-match@0.4.2",
          "resolved": "https://registry.npmjs.org/balanced-match/-/balanced-match-0.4.2.tgz"
        },
        "bcrypt-pbkdf": {
          "version": "1.0.1",
          "from": "bcrypt-pbkdf@1.0.1",
          "resolved": "https://registry.npmjs.org/bcrypt-pbkdf/-/bcrypt-pbkdf-1.0.1.tgz",
          "optional": true
        },
        "block-stream": {
          "version": "0.0.9",
          "from": "block-stream@0.0.9",
          "resolved": "https://registry.npmjs.org/block-stream/-/block-stream-0.0.9.tgz"
        },
        "boom": {
          "version": "2.10.1",
          "from": "boom@2.10.1",
          "resolved": "https://registry.npmjs.org/boom/-/boom-2.10.1.tgz"
        },
        "brace-expansion": {
          "version": "1.1.7",
          "from": "brace-expansion@1.1.7",
          "resolved": "https://registry.npmjs.org/brace-expansion/-/brace-expansion-1.1.7.tgz"
        },
        "buffer-shims": {
          "version": "1.0.0",
          "from": "buffer-shims@1.0.0",
          "resolved": "https://registry.npmjs.org/buffer-shims/-/buffer-shims-1.0.0.tgz"
        },
        "caseless": {
          "version": "0.12.0",
          "from": "caseless@0.12.0",
          "resolved": "https://registry.npmjs.org/caseless/-/caseless-0.12.0.tgz",
          "optional": true
        },
        "co": {
          "version": "4.6.0",
          "from": "co@4.6.0",
          "resolved": "https://registry.npmjs.org/co/-/co-4.6.0.tgz",
          "optional": true
        },
        "code-point-at": {
          "version": "1.1.0",
          "from": "code-point-at@1.1.0",
          "resolved": "https://registry.npmjs.org/code-point-at/-/code-point-at-1.1.0.tgz"
        },
        "combined-stream": {
          "version": "1.0.5",
          "from": "combined-stream@1.0.5",
          "resolved": "https://registry.npmjs.org/combined-stream/-/combined-stream-1.0.5.tgz"
        },
        "concat-map": {
          "version": "0.0.1",
          "from": "concat-map@0.0.1",
          "resolved": "https://registry.npmjs.org/concat-map/-/concat-map-0.0.1.tgz"
        },
        "console-control-strings": {
          "version": "1.1.0",
          "from": "console-control-strings@1.1.0",
          "resolved": "https://registry.npmjs.org/console-control-strings/-/console-control-strings-1.1.0.tgz"
        },
        "core-util-is": {
          "version": "1.0.2",
          "from": "core-util-is@1.0.2",
          "resolved": "https://registry.npmjs.org/core-util-is/-/core-util-is-1.0.2.tgz"
        },
        "cryptiles": {
          "version": "2.0.5",
          "from": "cryptiles@2.0.5",
          "resolved": "https://registry.npmjs.org/cryptiles/-/cryptiles-2.0.5.tgz",
          "optional": true
        },
        "dashdash": {
          "version": "1.14.1",
          "from": "dashdash@1.14.1",
          "resolved": "https://registry.npmjs.org/dashdash/-/dashdash-1.14.1.tgz",
          "optional": true,
          "dependencies": {
            "assert-plus": {
              "version": "1.0.0",
              "from": "assert-plus@1.0.0",
              "resolved": "https://registry.npmjs.org/assert-plus/-/assert-plus-1.0.0.tgz",
              "optional": true
            }
          }
        },
        "debug": {
          "version": "2.6.8",
          "from": "debug@2.6.8",
          "resolved": "https://registry.npmjs.org/debug/-/debug-2.6.8.tgz",
          "optional": true
        },
        "deep-extend": {
          "version": "0.4.2",
          "from": "deep-extend@0.4.2",
          "resolved": "https://registry.npmjs.org/deep-extend/-/deep-extend-0.4.2.tgz",
          "optional": true
        },
        "delayed-stream": {
          "version": "1.0.0",
          "from": "delayed-stream@1.0.0",
          "resolved": "https://registry.npmjs.org/delayed-stream/-/delayed-stream-1.0.0.tgz"
        },
        "delegates": {
          "version": "1.0.0",
          "from": "delegates@1.0.0",
          "resolved": "https://registry.npmjs.org/delegates/-/delegates-1.0.0.tgz",
          "optional": true
        },
        "ecc-jsbn": {
          "version": "0.1.1",
          "from": "ecc-jsbn@0.1.1",
          "resolved": "https://registry.npmjs.org/ecc-jsbn/-/ecc-jsbn-0.1.1.tgz",
          "optional": true
        },
        "extend": {
          "version": "3.0.1",
          "from": "extend@3.0.1",
          "resolved": "https://registry.npmjs.org/extend/-/extend-3.0.1.tgz",
          "optional": true
        },
        "extsprintf": {
          "version": "1.0.2",
          "from": "extsprintf@1.0.2",
          "resolved": "https://registry.npmjs.org/extsprintf/-/extsprintf-1.0.2.tgz"
        },
        "forever-agent": {
          "version": "0.6.1",
          "from": "forever-agent@0.6.1",
          "resolved": "https://registry.npmjs.org/forever-agent/-/forever-agent-0.6.1.tgz",
          "optional": true
        },
        "form-data": {
          "version": "2.1.4",
          "from": "form-data@2.1.4",
          "resolved": "https://registry.npmjs.org/form-data/-/form-data-2.1.4.tgz",
          "optional": true
        },
        "fs.realpath": {
          "version": "1.0.0",
          "from": "fs.realpath@1.0.0",
          "resolved": "https://registry.npmjs.org/fs.realpath/-/fs.realpath-1.0.0.tgz"
        },
        "fstream": {
          "version": "1.0.11",
          "from": "fstream@1.0.11",
          "resolved": "https://registry.npmjs.org/fstream/-/fstream-1.0.11.tgz"
        },
        "fstream-ignore": {
          "version": "1.0.5",
          "from": "fstream-ignore@1.0.5",
          "resolved": "https://registry.npmjs.org/fstream-ignore/-/fstream-ignore-1.0.5.tgz",
          "optional": true
        },
        "gauge": {
          "version": "2.7.4",
          "from": "gauge@2.7.4",
          "resolved": "https://registry.npmjs.org/gauge/-/gauge-2.7.4.tgz",
          "optional": true
        },
        "getpass": {
          "version": "0.1.7",
          "from": "getpass@0.1.7",
          "resolved": "https://registry.npmjs.org/getpass/-/getpass-0.1.7.tgz",
          "optional": true,
          "dependencies": {
            "assert-plus": {
              "version": "1.0.0",
              "from": "assert-plus@1.0.0",
              "resolved": "https://registry.npmjs.org/assert-plus/-/assert-plus-1.0.0.tgz",
              "optional": true
            }
          }
        },
        "glob": {
          "version": "7.1.2",
          "from": "glob@7.1.2",
          "resolved": "https://registry.npmjs.org/glob/-/glob-7.1.2.tgz"
        },
        "graceful-fs": {
          "version": "4.1.11",
          "from": "graceful-fs@4.1.11",
          "resolved": "https://registry.npmjs.org/graceful-fs/-/graceful-fs-4.1.11.tgz"
        },
        "har-schema": {
          "version": "1.0.5",
          "from": "har-schema@1.0.5",
          "resolved": "https://registry.npmjs.org/har-schema/-/har-schema-1.0.5.tgz",
          "optional": true
        },
        "har-validator": {
          "version": "4.2.1",
          "from": "har-validator@4.2.1",
          "resolved": "https://registry.npmjs.org/har-validator/-/har-validator-4.2.1.tgz",
          "optional": true
        },
        "has-unicode": {
          "version": "2.0.1",
          "from": "has-unicode@2.0.1",
          "resolved": "https://registry.npmjs.org/has-unicode/-/has-unicode-2.0.1.tgz",
          "optional": true
        },
        "hawk": {
          "version": "3.1.3",
          "from": "hawk@3.1.3",
          "resolved": "https://registry.npmjs.org/hawk/-/hawk-3.1.3.tgz",
          "optional": true
        },
        "hoek": {
          "version": "2.16.3",
          "from": "hoek@2.16.3",
          "resolved": "https://registry.npmjs.org/hoek/-/hoek-2.16.3.tgz"
        },
        "http-signature": {
          "version": "1.1.1",
          "from": "http-signature@1.1.1",
          "resolved": "https://registry.npmjs.org/http-signature/-/http-signature-1.1.1.tgz",
          "optional": true
        },
        "inflight": {
          "version": "1.0.6",
          "from": "inflight@1.0.6",
          "resolved": "https://registry.npmjs.org/inflight/-/inflight-1.0.6.tgz"
        },
        "inherits": {
          "version": "2.0.3",
          "from": "inherits@2.0.3",
          "resolved": "https://registry.npmjs.org/inherits/-/inherits-2.0.3.tgz"
        },
        "ini": {
          "version": "1.3.4",
          "from": "ini@1.3.4",
          "resolved": "https://registry.npmjs.org/ini/-/ini-1.3.4.tgz",
          "optional": true
        },
        "is-fullwidth-code-point": {
          "version": "1.0.0",
          "from": "is-fullwidth-code-point@1.0.0",
          "resolved": "https://registry.npmjs.org/is-fullwidth-code-point/-/is-fullwidth-code-point-1.0.0.tgz"
        },
        "is-typedarray": {
          "version": "1.0.0",
          "from": "is-typedarray@1.0.0",
          "resolved": "https://registry.npmjs.org/is-typedarray/-/is-typedarray-1.0.0.tgz",
          "optional": true
        },
        "isarray": {
          "version": "1.0.0",
          "from": "isarray@1.0.0",
          "resolved": "https://registry.npmjs.org/isarray/-/isarray-1.0.0.tgz"
        },
        "isstream": {
          "version": "0.1.2",
          "from": "isstream@0.1.2",
          "resolved": "https://registry.npmjs.org/isstream/-/isstream-0.1.2.tgz",
          "optional": true
        },
        "jodid25519": {
          "version": "1.0.2",
          "from": "jodid25519@1.0.2",
          "resolved": "https://registry.npmjs.org/jodid25519/-/jodid25519-1.0.2.tgz",
          "optional": true
        },
        "jsbn": {
          "version": "0.1.1",
          "from": "jsbn@0.1.1",
          "resolved": "https://registry.npmjs.org/jsbn/-/jsbn-0.1.1.tgz",
          "optional": true
        },
        "json-schema": {
          "version": "0.2.3",
          "from": "json-schema@0.2.3",
          "resolved": "https://registry.npmjs.org/json-schema/-/json-schema-0.2.3.tgz",
          "optional": true
        },
        "json-stable-stringify": {
          "version": "1.0.1",
          "from": "json-stable-stringify@1.0.1",
          "resolved": "https://registry.npmjs.org/json-stable-stringify/-/json-stable-stringify-1.0.1.tgz",
          "optional": true
        },
        "json-stringify-safe": {
          "version": "5.0.1",
          "from": "json-stringify-safe@5.0.1",
          "resolved": "https://registry.npmjs.org/json-stringify-safe/-/json-stringify-safe-5.0.1.tgz",
          "optional": true
        },
        "jsonify": {
          "version": "0.0.0",
          "from": "jsonify@0.0.0",
          "resolved": "https://registry.npmjs.org/jsonify/-/jsonify-0.0.0.tgz",
          "optional": true
        },
        "jsprim": {
          "version": "1.4.0",
          "from": "jsprim@1.4.0",
          "resolved": "https://registry.npmjs.org/jsprim/-/jsprim-1.4.0.tgz",
          "optional": true,
          "dependencies": {
            "assert-plus": {
              "version": "1.0.0",
              "from": "assert-plus@1.0.0",
              "resolved": "https://registry.npmjs.org/assert-plus/-/assert-plus-1.0.0.tgz",
              "optional": true
            }
          }
        },
        "mime-db": {
          "version": "1.27.0",
          "from": "mime-db@1.27.0",
          "resolved": "https://registry.npmjs.org/mime-db/-/mime-db-1.27.0.tgz"
        },
        "mime-types": {
          "version": "2.1.15",
          "from": "mime-types@2.1.15",
          "resolved": "https://registry.npmjs.org/mime-types/-/mime-types-2.1.15.tgz"
        },
        "minimatch": {
          "version": "3.0.4",
          "from": "minimatch@3.0.4",
          "resolved": "https://registry.npmjs.org/minimatch/-/minimatch-3.0.4.tgz"
        },
        "minimist": {
          "version": "0.0.8",
          "from": "minimist@0.0.8",
          "resolved": "https://registry.npmjs.org/minimist/-/minimist-0.0.8.tgz"
        },
        "mkdirp": {
          "version": "0.5.1",
          "from": "mkdirp@0.5.1",
          "resolved": "https://registry.npmjs.org/mkdirp/-/mkdirp-0.5.1.tgz"
        },
        "ms": {
          "version": "2.0.0",
          "from": "ms@2.0.0",
          "resolved": "https://registry.npmjs.org/ms/-/ms-2.0.0.tgz",
          "optional": true
        },
        "node-pre-gyp": {
          "version": "0.6.36",
          "from": "node-pre-gyp@^0.6.36",
          "resolved": "https://registry.npmjs.org/node-pre-gyp/-/node-pre-gyp-0.6.36.tgz",
          "optional": true
        },
        "nopt": {
          "version": "4.0.1",
          "from": "nopt@4.0.1",
          "resolved": "https://registry.npmjs.org/nopt/-/nopt-4.0.1.tgz",
          "optional": true
        },
        "npmlog": {
          "version": "4.1.0",
          "from": "npmlog@4.1.0",
          "resolved": "https://registry.npmjs.org/npmlog/-/npmlog-4.1.0.tgz",
          "optional": true
        },
        "number-is-nan": {
          "version": "1.0.1",
          "from": "number-is-nan@1.0.1",
          "resolved": "https://registry.npmjs.org/number-is-nan/-/number-is-nan-1.0.1.tgz"
        },
        "oauth-sign": {
          "version": "0.8.2",
          "from": "oauth-sign@0.8.2",
          "resolved": "https://registry.npmjs.org/oauth-sign/-/oauth-sign-0.8.2.tgz",
          "optional": true
        },
        "object-assign": {
          "version": "4.1.1",
          "from": "object-assign@4.1.1",
          "resolved": "https://registry.npmjs.org/object-assign/-/object-assign-4.1.1.tgz",
          "optional": true
        },
        "once": {
          "version": "1.4.0",
          "from": "once@1.4.0",
          "resolved": "https://registry.npmjs.org/once/-/once-1.4.0.tgz"
        },
        "os-homedir": {
          "version": "1.0.2",
          "from": "os-homedir@1.0.2",
          "resolved": "https://registry.npmjs.org/os-homedir/-/os-homedir-1.0.2.tgz",
          "optional": true
        },
        "os-tmpdir": {
          "version": "1.0.2",
          "from": "os-tmpdir@1.0.2",
          "resolved": "https://registry.npmjs.org/os-tmpdir/-/os-tmpdir-1.0.2.tgz",
          "optional": true
        },
        "osenv": {
          "version": "0.1.4",
          "from": "osenv@0.1.4",
          "resolved": "https://registry.npmjs.org/osenv/-/osenv-0.1.4.tgz",
          "optional": true
        },
        "path-is-absolute": {
          "version": "1.0.1",
          "from": "path-is-absolute@1.0.1",
          "resolved": "https://registry.npmjs.org/path-is-absolute/-/path-is-absolute-1.0.1.tgz"
        },
        "performance-now": {
          "version": "0.2.0",
          "from": "performance-now@0.2.0",
          "resolved": "https://registry.npmjs.org/performance-now/-/performance-now-0.2.0.tgz",
          "optional": true
        },
        "process-nextick-args": {
          "version": "1.0.7",
          "from": "process-nextick-args@1.0.7",
          "resolved": "https://registry.npmjs.org/process-nextick-args/-/process-nextick-args-1.0.7.tgz"
        },
        "punycode": {
          "version": "1.4.1",
          "from": "punycode@1.4.1",
          "resolved": "https://registry.npmjs.org/punycode/-/punycode-1.4.1.tgz",
          "optional": true
        },
        "qs": {
          "version": "6.4.0",
          "from": "qs@6.4.0",
          "resolved": "https://registry.npmjs.org/qs/-/qs-6.4.0.tgz",
          "optional": true
        },
        "rc": {
          "version": "1.2.1",
          "from": "rc@1.2.1",
          "resolved": "https://registry.npmjs.org/rc/-/rc-1.2.1.tgz",
          "optional": true,
          "dependencies": {
            "minimist": {
              "version": "1.2.0",
              "from": "minimist@1.2.0",
              "resolved": "https://registry.npmjs.org/minimist/-/minimist-1.2.0.tgz",
              "optional": true
            }
          }
        },
        "readable-stream": {
          "version": "2.2.9",
          "from": "readable-stream@2.2.9",
          "resolved": "https://registry.npmjs.org/readable-stream/-/readable-stream-2.2.9.tgz"
        },
        "request": {
          "version": "2.81.0",
          "from": "request@2.81.0",
          "resolved": "https://registry.npmjs.org/request/-/request-2.81.0.tgz",
          "optional": true
        },
        "rimraf": {
          "version": "2.6.1",
          "from": "rimraf@2.6.1",
          "resolved": "https://registry.npmjs.org/rimraf/-/rimraf-2.6.1.tgz"
        },
        "safe-buffer": {
          "version": "5.0.1",
          "from": "safe-buffer@5.0.1",
          "resolved": "https://registry.npmjs.org/safe-buffer/-/safe-buffer-5.0.1.tgz"
        },
        "semver": {
          "version": "5.3.0",
          "from": "semver@5.3.0",
          "resolved": "https://registry.npmjs.org/semver/-/semver-5.3.0.tgz",
          "optional": true
        },
        "set-blocking": {
          "version": "2.0.0",
          "from": "set-blocking@2.0.0",
          "resolved": "https://registry.npmjs.org/set-blocking/-/set-blocking-2.0.0.tgz",
          "optional": true
        },
        "signal-exit": {
          "version": "3.0.2",
          "from": "signal-exit@3.0.2",
          "resolved": "https://registry.npmjs.org/signal-exit/-/signal-exit-3.0.2.tgz",
          "optional": true
        },
        "sntp": {
          "version": "1.0.9",
          "from": "sntp@1.0.9",
          "resolved": "https://registry.npmjs.org/sntp/-/sntp-1.0.9.tgz",
          "optional": true
        },
        "sshpk": {
          "version": "1.13.0",
          "from": "sshpk@1.13.0",
          "resolved": "https://registry.npmjs.org/sshpk/-/sshpk-1.13.0.tgz",
          "optional": true,
          "dependencies": {
            "assert-plus": {
              "version": "1.0.0",
              "from": "assert-plus@1.0.0",
              "resolved": "https://registry.npmjs.org/assert-plus/-/assert-plus-1.0.0.tgz",
              "optional": true
            }
          }
        },
        "string_decoder": {
          "version": "1.0.1",
          "from": "string_decoder@1.0.1",
          "resolved": "https://registry.npmjs.org/string_decoder/-/string_decoder-1.0.1.tgz"
        },
        "string-width": {
          "version": "1.0.2",
          "from": "string-width@1.0.2",
          "resolved": "https://registry.npmjs.org/string-width/-/string-width-1.0.2.tgz"
        },
        "stringstream": {
          "version": "0.0.5",
          "from": "stringstream@0.0.5",
          "resolved": "https://registry.npmjs.org/stringstream/-/stringstream-0.0.5.tgz",
          "optional": true
        },
        "strip-ansi": {
          "version": "3.0.1",
          "from": "strip-ansi@3.0.1",
          "resolved": "https://registry.npmjs.org/strip-ansi/-/strip-ansi-3.0.1.tgz"
        },
        "strip-json-comments": {
          "version": "2.0.1",
          "from": "strip-json-comments@2.0.1",
          "resolved": "https://registry.npmjs.org/strip-json-comments/-/strip-json-comments-2.0.1.tgz",
          "optional": true
        },
        "tar": {
          "version": "2.2.1",
          "from": "tar@2.2.1",
          "resolved": "https://registry.npmjs.org/tar/-/tar-2.2.1.tgz"
        },
        "tar-pack": {
          "version": "3.4.0",
          "from": "tar-pack@3.4.0",
          "resolved": "https://registry.npmjs.org/tar-pack/-/tar-pack-3.4.0.tgz",
          "optional": true
        },
        "tough-cookie": {
          "version": "2.3.2",
          "from": "tough-cookie@2.3.2",
          "resolved": "https://registry.npmjs.org/tough-cookie/-/tough-cookie-2.3.2.tgz",
          "optional": true
        },
        "tunnel-agent": {
          "version": "0.6.0",
          "from": "tunnel-agent@0.6.0",
          "resolved": "https://registry.npmjs.org/tunnel-agent/-/tunnel-agent-0.6.0.tgz",
          "optional": true
        },
        "tweetnacl": {
          "version": "0.14.5",
          "from": "tweetnacl@0.14.5",
          "resolved": "https://registry.npmjs.org/tweetnacl/-/tweetnacl-0.14.5.tgz",
          "optional": true
        },
        "uid-number": {
          "version": "0.0.6",
          "from": "uid-number@0.0.6",
          "resolved": "https://registry.npmjs.org/uid-number/-/uid-number-0.0.6.tgz",
          "optional": true
        },
        "util-deprecate": {
          "version": "1.0.2",
          "from": "util-deprecate@1.0.2",
          "resolved": "https://registry.npmjs.org/util-deprecate/-/util-deprecate-1.0.2.tgz"
        },
        "uuid": {
          "version": "3.0.1",
          "from": "uuid@3.0.1",
          "resolved": "https://registry.npmjs.org/uuid/-/uuid-3.0.1.tgz",
          "optional": true
        },
        "verror": {
          "version": "1.3.6",
          "from": "verror@1.3.6",
          "resolved": "https://registry.npmjs.org/verror/-/verror-1.3.6.tgz",
          "optional": true
        },
        "wide-align": {
          "version": "1.1.2",
          "from": "wide-align@1.1.2",
          "resolved": "https://registry.npmjs.org/wide-align/-/wide-align-1.1.2.tgz",
          "optional": true
        },
        "wrappy": {
          "version": "1.0.2",
          "from": "wrappy@1.0.2",
          "resolved": "https://registry.npmjs.org/wrappy/-/wrappy-1.0.2.tgz"
        }
      }
    },
    "function-bind": {
      "version": "1.1.0",
      "from": "function-bind@>=1.0.2 <2.0.0",
      "resolved": "https://registry.npmjs.org/function-bind/-/function-bind-1.1.0.tgz"
    },
    "get-caller-file": {
      "version": "1.0.2",
      "from": "get-caller-file@>=1.0.1 <2.0.0",
      "resolved": "https://registry.npmjs.org/get-caller-file/-/get-caller-file-1.0.2.tgz"
    },
    "get-stdin": {
      "version": "4.0.1",
      "from": "get-stdin@>=4.0.1 <5.0.0",
      "resolved": "https://registry.npmjs.org/get-stdin/-/get-stdin-4.0.1.tgz"
    },
    "get-stream": {
      "version": "2.3.1",
      "from": "get-stream@>=2.2.0 <3.0.0",
      "resolved": "https://registry.npmjs.org/get-stream/-/get-stream-2.3.1.tgz"
    },
    "glob": {
      "version": "7.1.2",
      "from": "glob@>=7.0.5 <8.0.0",
      "resolved": "https://registry.npmjs.org/glob/-/glob-7.1.2.tgz"
    },
    "glob-base": {
      "version": "0.3.0",
      "from": "glob-base@>=0.3.0 <0.4.0",
      "resolved": "https://registry.npmjs.org/glob-base/-/glob-base-0.3.0.tgz"
    },
    "glob-parent": {
      "version": "2.0.0",
      "from": "glob-parent@>=2.0.0 <3.0.0",
      "resolved": "https://registry.npmjs.org/glob-parent/-/glob-parent-2.0.0.tgz"
    },
    "globals": {
      "version": "9.18.0",
      "from": "globals@>=9.0.0 <10.0.0",
      "resolved": "https://registry.npmjs.org/globals/-/globals-9.18.0.tgz"
    },
    "globby": {
      "version": "6.1.0",
      "from": "globby@>=6.1.0 <7.0.0",
      "resolved": "https://registry.npmjs.org/globby/-/globby-6.1.0.tgz"
    },
    "got": {
      "version": "7.1.0",
      "from": "got@>=7.0.0 <8.0.0",
      "resolved": "https://registry.npmjs.org/got/-/got-7.1.0.tgz",
      "dependencies": {
        "get-stream": {
          "version": "3.0.0",
          "from": "get-stream@>=3.0.0 <4.0.0",
          "resolved": "https://registry.npmjs.org/get-stream/-/get-stream-3.0.0.tgz"
        }
      }
    },
    "graceful-fs": {
      "version": "4.1.11",
      "from": "graceful-fs@>=4.1.2 <5.0.0",
      "resolved": "https://registry.npmjs.org/graceful-fs/-/graceful-fs-4.1.11.tgz"
    },
    "handle-thing": {
      "version": "1.2.5",
      "from": "handle-thing@>=1.2.5 <2.0.0",
      "resolved": "https://registry.npmjs.org/handle-thing/-/handle-thing-1.2.5.tgz"
    },
    "has": {
      "version": "1.0.1",
      "from": "has@>=1.0.1 <2.0.0",
      "resolved": "https://registry.npmjs.org/has/-/has-1.0.1.tgz"
    },
    "has-ansi": {
      "version": "2.0.0",
      "from": "has-ansi@>=2.0.0 <3.0.0",
      "resolved": "https://registry.npmjs.org/has-ansi/-/has-ansi-2.0.0.tgz"
    },
    "has-flag": {
      "version": "1.0.0",
      "from": "has-flag@>=1.0.0 <2.0.0",
      "resolved": "https://registry.npmjs.org/has-flag/-/has-flag-1.0.0.tgz"
    },
    "has-symbol-support-x": {
      "version": "1.4.0",
      "from": "has-symbol-support-x@>=1.4.0 <2.0.0",
      "resolved": "https://registry.npmjs.org/has-symbol-support-x/-/has-symbol-support-x-1.4.0.tgz"
    },
    "has-to-string-tag-x": {
      "version": "1.4.0",
      "from": "has-to-string-tag-x@>=1.2.0 <2.0.0",
      "resolved": "https://registry.npmjs.org/has-to-string-tag-x/-/has-to-string-tag-x-1.4.0.tgz"
    },
    "hash-base": {
      "version": "2.0.2",
      "from": "hash-base@>=2.0.0 <3.0.0",
      "resolved": "https://registry.npmjs.org/hash-base/-/hash-base-2.0.2.tgz"
    },
    "hash-sum": {
      "version": "1.0.2",
      "from": "hash-sum@>=1.0.2 <2.0.0",
      "resolved": "https://registry.npmjs.org/hash-sum/-/hash-sum-1.0.2.tgz"
    },
    "hash.js": {
      "version": "1.1.3",
      "from": "hash.js@>=1.0.0 <2.0.0",
      "resolved": "https://registry.npmjs.org/hash.js/-/hash.js-1.1.3.tgz"
    },
    "he": {
      "version": "1.1.1",
      "from": "he@>=1.1.0 <2.0.0",
      "resolved": "https://registry.npmjs.org/he/-/he-1.1.1.tgz"
    },
    "hmac-drbg": {
      "version": "1.0.1",
      "from": "hmac-drbg@>=1.0.0 <2.0.0",
      "resolved": "https://registry.npmjs.org/hmac-drbg/-/hmac-drbg-1.0.1.tgz"
    },
    "home-or-tmp": {
      "version": "2.0.0",
      "from": "home-or-tmp@>=2.0.0 <3.0.0",
      "resolved": "https://registry.npmjs.org/home-or-tmp/-/home-or-tmp-2.0.0.tgz"
    },
    "hosted-git-info": {
      "version": "2.5.0",
      "from": "hosted-git-info@>=2.1.4 <3.0.0",
      "resolved": "https://registry.npmjs.org/hosted-git-info/-/hosted-git-info-2.5.0.tgz"
    },
    "hpack.js": {
      "version": "2.1.6",
      "from": "hpack.js@>=2.1.6 <3.0.0",
      "resolved": "https://registry.npmjs.org/hpack.js/-/hpack.js-2.1.6.tgz",
      "dependencies": {
        "isarray": {
          "version": "1.0.0",
          "from": "isarray@>=1.0.0 <1.1.0",
          "resolved": "https://registry.npmjs.org/isarray/-/isarray-1.0.0.tgz"
        },
        "readable-stream": {
          "version": "2.3.3",
          "from": "readable-stream@>=2.0.1 <3.0.0",
          "resolved": "https://registry.npmjs.org/readable-stream/-/readable-stream-2.3.3.tgz"
        },
        "string_decoder": {
          "version": "1.0.3",
          "from": "string_decoder@>=1.0.3 <1.1.0",
          "resolved": "https://registry.npmjs.org/string_decoder/-/string_decoder-1.0.3.tgz"
        }
      }
    },
    "html-comment-regex": {
      "version": "1.1.1",
      "from": "html-comment-regex@>=1.1.0 <2.0.0",
      "resolved": "https://registry.npmjs.org/html-comment-regex/-/html-comment-regex-1.1.1.tgz"
    },
    "html-entities": {
      "version": "1.2.1",
      "from": "html-entities@>=1.2.0 <2.0.0",
      "resolved": "https://registry.npmjs.org/html-entities/-/html-entities-1.2.1.tgz"
    },
    "htmlparser2": {
      "version": "3.3.0",
      "from": "htmlparser2@>=3.3.0 <3.4.0",
      "resolved": "https://registry.npmjs.org/htmlparser2/-/htmlparser2-3.3.0.tgz",
      "dependencies": {
        "domutils": {
          "version": "1.1.6",
          "from": "domutils@>=1.1.0 <1.2.0",
          "resolved": "https://registry.npmjs.org/domutils/-/domutils-1.1.6.tgz"
        }
      }
    },
    "http-deceiver": {
      "version": "1.2.7",
      "from": "http-deceiver@>=1.2.7 <2.0.0",
      "resolved": "https://registry.npmjs.org/http-deceiver/-/http-deceiver-1.2.7.tgz"
    },
    "http-errors": {
      "version": "1.6.1",
      "from": "http-errors@>=1.6.1 <1.7.0",
      "resolved": "https://registry.npmjs.org/http-errors/-/http-errors-1.6.1.tgz"
    },
    "http-proxy": {
      "version": "1.16.2",
      "from": "http-proxy@>=1.16.2 <2.0.0",
      "resolved": "https://registry.npmjs.org/http-proxy/-/http-proxy-1.16.2.tgz"
    },
    "http-proxy-middleware": {
      "version": "0.17.4",
      "from": "http-proxy-middleware@>=0.17.4 <0.18.0",
      "resolved": "https://registry.npmjs.org/http-proxy-middleware/-/http-proxy-middleware-0.17.4.tgz",
      "dependencies": {
        "is-extglob": {
          "version": "2.1.1",
          "from": "is-extglob@>=2.1.0 <3.0.0",
          "resolved": "https://registry.npmjs.org/is-extglob/-/is-extglob-2.1.1.tgz"
        },
        "is-glob": {
          "version": "3.1.0",
          "from": "is-glob@>=3.1.0 <4.0.0",
          "resolved": "https://registry.npmjs.org/is-glob/-/is-glob-3.1.0.tgz"
        }
      }
    },
    "https-browserify": {
      "version": "0.0.1",
      "from": "https-browserify@0.0.1",
      "resolved": "https://registry.npmjs.org/https-browserify/-/https-browserify-0.0.1.tgz"
    },
    "icss-replace-symbols": {
      "version": "1.1.0",
      "from": "icss-replace-symbols@>=1.1.0 <2.0.0",
      "resolved": "https://registry.npmjs.org/icss-replace-symbols/-/icss-replace-symbols-1.1.0.tgz"
    },
    "ieee754": {
      "version": "1.1.8",
      "from": "ieee754@>=1.1.4 <2.0.0",
      "resolved": "https://registry.npmjs.org/ieee754/-/ieee754-1.1.8.tgz"
    },
    "indent-string": {
      "version": "2.1.0",
      "from": "indent-string@>=2.1.0 <3.0.0",
      "resolved": "https://registry.npmjs.org/indent-string/-/indent-string-2.1.0.tgz"
    },
    "indexes-of": {
      "version": "1.0.1",
      "from": "indexes-of@>=1.0.1 <2.0.0",
      "resolved": "https://registry.npmjs.org/indexes-of/-/indexes-of-1.0.1.tgz"
    },
    "indexof": {
      "version": "0.0.1",
      "from": "indexof@0.0.1",
      "resolved": "https://registry.npmjs.org/indexof/-/indexof-0.0.1.tgz"
    },
    "inflight": {
      "version": "1.0.6",
      "from": "inflight@>=1.0.4 <2.0.0",
      "resolved": "https://registry.npmjs.org/inflight/-/inflight-1.0.6.tgz"
    },
    "inherits": {
      "version": "2.0.3",
      "from": "inherits@>=2.0.0 <3.0.0",
      "resolved": "https://registry.npmjs.org/inherits/-/inherits-2.0.3.tgz"
    },
    "ini": {
      "version": "1.3.4",
      "from": "ini@>=1.3.4 <2.0.0",
      "resolved": "https://registry.npmjs.org/ini/-/ini-1.3.4.tgz"
    },
    "internal-ip": {
      "version": "1.2.0",
      "from": "internal-ip@>=1.2.0 <2.0.0",
      "resolved": "https://registry.npmjs.org/internal-ip/-/internal-ip-1.2.0.tgz"
    },
    "interpret": {
      "version": "1.0.3",
      "from": "interpret@>=1.0.0 <2.0.0",
      "resolved": "https://registry.npmjs.org/interpret/-/interpret-1.0.3.tgz"
    },
    "invariant": {
      "version": "2.2.2",
      "from": "invariant@>=2.2.0 <3.0.0",
      "resolved": "https://registry.npmjs.org/invariant/-/invariant-2.2.2.tgz"
    },
    "invert-kv": {
      "version": "1.0.0",
      "from": "invert-kv@>=1.0.0 <2.0.0",
      "resolved": "https://registry.npmjs.org/invert-kv/-/invert-kv-1.0.0.tgz"
    },
    "ip": {
      "version": "1.1.5",
      "from": "ip@>=1.1.0 <2.0.0",
      "resolved": "https://registry.npmjs.org/ip/-/ip-1.1.5.tgz"
    },
    "ipaddr.js": {
      "version": "1.3.0",
      "from": "ipaddr.js@1.3.0",
      "resolved": "https://registry.npmjs.org/ipaddr.js/-/ipaddr.js-1.3.0.tgz"
    },
    "is-absolute-url": {
      "version": "2.1.0",
      "from": "is-absolute-url@>=2.0.0 <3.0.0",
      "resolved": "https://registry.npmjs.org/is-absolute-url/-/is-absolute-url-2.1.0.tgz"
    },
    "is-arrayish": {
      "version": "0.2.1",
      "from": "is-arrayish@>=0.2.1 <0.3.0",
      "resolved": "https://registry.npmjs.org/is-arrayish/-/is-arrayish-0.2.1.tgz"
    },
    "is-binary-path": {
      "version": "1.0.1",
      "from": "is-binary-path@>=1.0.0 <2.0.0",
      "resolved": "https://registry.npmjs.org/is-binary-path/-/is-binary-path-1.0.1.tgz"
    },
    "is-buffer": {
      "version": "1.1.5",
      "from": "is-buffer@>=1.1.5 <2.0.0",
      "resolved": "https://registry.npmjs.org/is-buffer/-/is-buffer-1.1.5.tgz"
    },
    "is-builtin-module": {
      "version": "1.0.0",
      "from": "is-builtin-module@>=1.0.0 <2.0.0",
      "resolved": "https://registry.npmjs.org/is-builtin-module/-/is-builtin-module-1.0.0.tgz"
    },
    "is-directory": {
      "version": "0.3.1",
      "from": "is-directory@>=0.3.1 <0.4.0",
      "resolved": "https://registry.npmjs.org/is-directory/-/is-directory-0.3.1.tgz"
    },
    "is-dotfile": {
      "version": "1.0.3",
      "from": "is-dotfile@>=1.0.0 <2.0.0",
      "resolved": "https://registry.npmjs.org/is-dotfile/-/is-dotfile-1.0.3.tgz"
    },
    "is-equal-shallow": {
      "version": "0.1.3",
      "from": "is-equal-shallow@>=0.1.3 <0.2.0",
      "resolved": "https://registry.npmjs.org/is-equal-shallow/-/is-equal-shallow-0.1.3.tgz"
    },
    "is-extendable": {
      "version": "0.1.1",
      "from": "is-extendable@>=0.1.1 <0.2.0",
      "resolved": "https://registry.npmjs.org/is-extendable/-/is-extendable-0.1.1.tgz"
    },
    "is-extglob": {
      "version": "1.0.0",
      "from": "is-extglob@>=1.0.0 <2.0.0",
      "resolved": "https://registry.npmjs.org/is-extglob/-/is-extglob-1.0.0.tgz"
    },
    "is-finite": {
      "version": "1.0.2",
      "from": "is-finite@>=1.0.0 <2.0.0",
      "resolved": "https://registry.npmjs.org/is-finite/-/is-finite-1.0.2.tgz"
    },
    "is-fullwidth-code-point": {
      "version": "1.0.0",
      "from": "is-fullwidth-code-point@>=1.0.0 <2.0.0",
      "resolved": "https://registry.npmjs.org/is-fullwidth-code-point/-/is-fullwidth-code-point-1.0.0.tgz"
    },
    "is-glob": {
      "version": "2.0.1",
      "from": "is-glob@>=2.0.0 <3.0.0",
      "resolved": "https://registry.npmjs.org/is-glob/-/is-glob-2.0.1.tgz"
    },
    "is-number": {
      "version": "2.1.0",
      "from": "is-number@>=2.1.0 <3.0.0",
      "resolved": "https://registry.npmjs.org/is-number/-/is-number-2.1.0.tgz"
    },
    "is-object": {
      "version": "1.0.1",
      "from": "is-object@>=1.0.1 <2.0.0",
      "resolved": "https://registry.npmjs.org/is-object/-/is-object-1.0.1.tgz"
    },
    "is-path-cwd": {
      "version": "1.0.0",
      "from": "is-path-cwd@>=1.0.0 <2.0.0",
      "resolved": "https://registry.npmjs.org/is-path-cwd/-/is-path-cwd-1.0.0.tgz"
    },
    "is-path-in-cwd": {
      "version": "1.0.0",
      "from": "is-path-in-cwd@>=1.0.0 <2.0.0",
      "resolved": "https://registry.npmjs.org/is-path-in-cwd/-/is-path-in-cwd-1.0.0.tgz"
    },
    "is-path-inside": {
      "version": "1.0.0",
      "from": "is-path-inside@>=1.0.0 <2.0.0",
      "resolved": "https://registry.npmjs.org/is-path-inside/-/is-path-inside-1.0.0.tgz"
    },
    "is-plain-obj": {
      "version": "1.1.0",
      "from": "is-plain-obj@>=1.0.0 <2.0.0",
      "resolved": "https://registry.npmjs.org/is-plain-obj/-/is-plain-obj-1.1.0.tgz"
    },
    "is-posix-bracket": {
      "version": "0.1.1",
      "from": "is-posix-bracket@>=0.1.0 <0.2.0",
      "resolved": "https://registry.npmjs.org/is-posix-bracket/-/is-posix-bracket-0.1.1.tgz"
    },
    "is-primitive": {
      "version": "2.0.0",
      "from": "is-primitive@>=2.0.0 <3.0.0",
      "resolved": "https://registry.npmjs.org/is-primitive/-/is-primitive-2.0.0.tgz"
    },
    "is-retry-allowed": {
      "version": "1.1.0",
      "from": "is-retry-allowed@>=1.0.0 <2.0.0",
      "resolved": "https://registry.npmjs.org/is-retry-allowed/-/is-retry-allowed-1.1.0.tgz"
    },
    "is-stream": {
      "version": "1.1.0",
      "from": "is-stream@>=1.1.0 <2.0.0",
      "resolved": "https://registry.npmjs.org/is-stream/-/is-stream-1.1.0.tgz"
    },
    "is-svg": {
      "version": "2.1.0",
      "from": "is-svg@>=2.0.0 <3.0.0",
      "resolved": "https://registry.npmjs.org/is-svg/-/is-svg-2.1.0.tgz"
    },
    "is-utf8": {
      "version": "0.2.1",
      "from": "is-utf8@>=0.2.0 <0.3.0",
      "resolved": "https://registry.npmjs.org/is-utf8/-/is-utf8-0.2.1.tgz"
    },
    "isarray": {
      "version": "0.0.1",
      "from": "isarray@0.0.1",
      "resolved": "https://registry.npmjs.org/isarray/-/isarray-0.0.1.tgz"
    },
    "isexe": {
      "version": "2.0.0",
      "from": "isexe@>=2.0.0 <3.0.0",
      "resolved": "https://registry.npmjs.org/isexe/-/isexe-2.0.0.tgz"
    },
    "isobject": {
      "version": "2.1.0",
      "from": "isobject@>=2.0.0 <3.0.0",
      "resolved": "https://registry.npmjs.org/isobject/-/isobject-2.1.0.tgz",
      "dependencies": {
        "isarray": {
          "version": "1.0.0",
          "from": "isarray@1.0.0",
          "resolved": "https://registry.npmjs.org/isarray/-/isarray-1.0.0.tgz"
        }
      }
    },
    "isurl": {
      "version": "1.0.0",
      "from": "isurl@>=1.0.0-alpha5 <2.0.0",
      "resolved": "https://registry.npmjs.org/isurl/-/isurl-1.0.0.tgz"
    },
    "js-base64": {
      "version": "2.1.9",
      "from": "js-base64@>=2.1.9 <3.0.0",
      "resolved": "https://registry.npmjs.org/js-base64/-/js-base64-2.1.9.tgz"
    },
    "js-beautify": {
      "version": "1.6.14",
      "from": "js-beautify@>=1.6.3 <2.0.0",
      "resolved": "https://registry.npmjs.org/js-beautify/-/js-beautify-1.6.14.tgz"
    },
    "js-tokens": {
      "version": "3.0.2",
      "from": "js-tokens@>=3.0.0 <4.0.0",
      "resolved": "https://registry.npmjs.org/js-tokens/-/js-tokens-3.0.2.tgz"
    },
    "js-yaml": {
      "version": "3.7.0",
      "from": "js-yaml@>=3.7.0 <3.8.0",
      "resolved": "https://registry.npmjs.org/js-yaml/-/js-yaml-3.7.0.tgz"
    },
    "jsesc": {
      "version": "1.3.0",
      "from": "jsesc@>=1.3.0 <2.0.0",
      "resolved": "https://registry.npmjs.org/jsesc/-/jsesc-1.3.0.tgz"
    },
    "json-loader": {
      "version": "0.5.4",
      "from": "json-loader@>=0.5.4 <0.6.0",
      "resolved": "https://registry.npmjs.org/json-loader/-/json-loader-0.5.4.tgz"
    },
    "json-schema-traverse": {
      "version": "0.3.1",
      "from": "json-schema-traverse@>=0.3.0 <0.4.0",
      "resolved": "https://registry.npmjs.org/json-schema-traverse/-/json-schema-traverse-0.3.1.tgz"
    },
    "json-stable-stringify": {
      "version": "1.0.1",
      "from": "json-stable-stringify@>=1.0.1 <2.0.0",
      "resolved": "https://registry.npmjs.org/json-stable-stringify/-/json-stable-stringify-1.0.1.tgz"
    },
    "json3": {
      "version": "3.3.2",
      "from": "json3@>=3.3.2 <4.0.0",
      "resolved": "https://registry.npmjs.org/json3/-/json3-3.3.2.tgz"
    },
    "json5": {
      "version": "0.5.1",
      "from": "json5@>=0.5.0 <0.6.0",
      "resolved": "https://registry.npmjs.org/json5/-/json5-0.5.1.tgz"
    },
    "jsonfile": {
      "version": "2.4.0",
      "from": "jsonfile@>=2.1.0 <3.0.0",
      "resolved": "https://registry.npmjs.org/jsonfile/-/jsonfile-2.4.0.tgz"
    },
    "jsonify": {
      "version": "0.0.0",
      "from": "jsonify@>=0.0.0 <0.1.0",
      "resolved": "https://registry.npmjs.org/jsonify/-/jsonify-0.0.0.tgz"
    },
    "kind-of": {
      "version": "3.2.2",
      "from": "kind-of@>=3.0.2 <4.0.0",
      "resolved": "https://registry.npmjs.org/kind-of/-/kind-of-3.2.2.tgz"
    },
    "lazy-cache": {
      "version": "1.0.4",
      "from": "lazy-cache@>=1.0.3 <2.0.0",
      "resolved": "https://registry.npmjs.org/lazy-cache/-/lazy-cache-1.0.4.tgz"
    },
    "lcid": {
      "version": "1.0.0",
      "from": "lcid@>=1.0.0 <2.0.0",
      "resolved": "https://registry.npmjs.org/lcid/-/lcid-1.0.0.tgz"
    },
    "load-json-file": {
      "version": "1.1.0",
      "from": "load-json-file@>=1.0.0 <2.0.0",
      "resolved": "https://registry.npmjs.org/load-json-file/-/load-json-file-1.1.0.tgz"
    },
    "loader-runner": {
      "version": "2.3.0",
      "from": "loader-runner@>=2.3.0 <3.0.0",
      "resolved": "https://registry.npmjs.org/loader-runner/-/loader-runner-2.3.0.tgz"
    },
    "loader-utils": {
      "version": "1.1.0",
      "from": "loader-utils@>=1.1.0 <2.0.0",
      "resolved": "https://registry.npmjs.org/loader-utils/-/loader-utils-1.1.0.tgz"
    },
    "locate-path": {
      "version": "2.0.0",
      "from": "locate-path@>=2.0.0 <3.0.0",
      "resolved": "https://registry.npmjs.org/locate-path/-/locate-path-2.0.0.tgz"
    },
    "lodash": {
      "version": "4.17.4",
      "from": "lodash@>=3.5.0 <5.0.0",
      "resolved": "https://registry.npmjs.org/lodash/-/lodash-4.17.4.tgz"
    },
    "lodash._baseassign": {
      "version": "3.2.0",
      "from": "lodash._baseassign@>=3.0.0 <4.0.0",
      "resolved": "https://registry.npmjs.org/lodash._baseassign/-/lodash._baseassign-3.2.0.tgz"
    },
    "lodash._basecopy": {
      "version": "3.0.1",
      "from": "lodash._basecopy@>=3.0.0 <4.0.0",
      "resolved": "https://registry.npmjs.org/lodash._basecopy/-/lodash._basecopy-3.0.1.tgz"
    },
    "lodash._bindcallback": {
      "version": "3.0.1",
      "from": "lodash._bindcallback@>=3.0.0 <4.0.0",
      "resolved": "https://registry.npmjs.org/lodash._bindcallback/-/lodash._bindcallback-3.0.1.tgz"
    },
    "lodash._createassigner": {
      "version": "3.1.1",
      "from": "lodash._createassigner@>=3.0.0 <4.0.0",
      "resolved": "https://registry.npmjs.org/lodash._createassigner/-/lodash._createassigner-3.1.1.tgz"
    },
    "lodash._getnative": {
      "version": "3.9.1",
      "from": "lodash._getnative@>=3.0.0 <4.0.0",
      "resolved": "https://registry.npmjs.org/lodash._getnative/-/lodash._getnative-3.9.1.tgz"
    },
    "lodash._isiterateecall": {
      "version": "3.0.9",
      "from": "lodash._isiterateecall@>=3.0.0 <4.0.0",
      "resolved": "https://registry.npmjs.org/lodash._isiterateecall/-/lodash._isiterateecall-3.0.9.tgz"
    },
    "lodash.assign": {
      "version": "4.2.0",
      "from": "lodash.assign@>=4.0.1 <5.0.0",
      "resolved": "https://registry.npmjs.org/lodash.assign/-/lodash.assign-4.2.0.tgz"
    },
    "lodash.camelcase": {
      "version": "4.3.0",
      "from": "lodash.camelcase@>=4.3.0 <5.0.0",
      "resolved": "https://registry.npmjs.org/lodash.camelcase/-/lodash.camelcase-4.3.0.tgz"
    },
    "lodash.defaults": {
      "version": "4.2.0",
      "from": "lodash.defaults@>=4.0.0 <5.0.0",
      "resolved": "https://registry.npmjs.org/lodash.defaults/-/lodash.defaults-4.2.0.tgz"
    },
    "lodash.isarguments": {
      "version": "3.1.0",
      "from": "lodash.isarguments@>=3.0.0 <4.0.0",
      "resolved": "https://registry.npmjs.org/lodash.isarguments/-/lodash.isarguments-3.1.0.tgz"
    },
    "lodash.isarray": {
      "version": "3.0.4",
      "from": "lodash.isarray@>=3.0.0 <4.0.0",
      "resolved": "https://registry.npmjs.org/lodash.isarray/-/lodash.isarray-3.0.4.tgz"
    },
    "lodash.keys": {
      "version": "3.1.2",
      "from": "lodash.keys@>=3.0.0 <4.0.0",
      "resolved": "https://registry.npmjs.org/lodash.keys/-/lodash.keys-3.1.2.tgz"
    },
    "lodash.memoize": {
      "version": "4.1.2",
      "from": "lodash.memoize@>=4.1.2 <5.0.0",
      "resolved": "https://registry.npmjs.org/lodash.memoize/-/lodash.memoize-4.1.2.tgz"
    },
    "lodash.restparam": {
      "version": "3.6.1",
      "from": "lodash.restparam@>=3.0.0 <4.0.0",
      "resolved": "https://registry.npmjs.org/lodash.restparam/-/lodash.restparam-3.6.1.tgz"
    },
    "lodash.uniq": {
      "version": "4.5.0",
      "from": "lodash.uniq@>=4.5.0 <5.0.0",
      "resolved": "https://registry.npmjs.org/lodash.uniq/-/lodash.uniq-4.5.0.tgz"
    },
    "longest": {
      "version": "1.0.1",
      "from": "longest@>=1.0.1 <2.0.0",
      "resolved": "https://registry.npmjs.org/longest/-/longest-1.0.1.tgz"
    },
    "loose-envify": {
      "version": "1.3.1",
      "from": "loose-envify@>=1.0.0 <2.0.0",
      "resolved": "https://registry.npmjs.org/loose-envify/-/loose-envify-1.3.1.tgz"
    },
    "loud-rejection": {
      "version": "1.6.0",
      "from": "loud-rejection@>=1.0.0 <2.0.0",
      "resolved": "https://registry.npmjs.org/loud-rejection/-/loud-rejection-1.6.0.tgz"
    },
    "lowercase-keys": {
      "version": "1.0.0",
      "from": "lowercase-keys@>=1.0.0 <2.0.0",
      "resolved": "https://registry.npmjs.org/lowercase-keys/-/lowercase-keys-1.0.0.tgz"
    },
    "lru-cache": {
      "version": "4.1.1",
      "from": "lru-cache@>=4.0.1 <5.0.0",
      "resolved": "https://registry.npmjs.org/lru-cache/-/lru-cache-4.1.1.tgz"
    },
    "macaddress": {
      "version": "0.2.8",
      "from": "macaddress@>=0.2.8 <0.3.0",
      "resolved": "https://registry.npmjs.org/macaddress/-/macaddress-0.2.8.tgz"
    },
    "make-dir": {
      "version": "1.0.0",
      "from": "make-dir@>=1.0.0 <2.0.0",
      "resolved": "https://registry.npmjs.org/make-dir/-/make-dir-1.0.0.tgz"
    },
    "map-obj": {
      "version": "1.0.1",
      "from": "map-obj@>=1.0.1 <2.0.0",
      "resolved": "https://registry.npmjs.org/map-obj/-/map-obj-1.0.1.tgz"
    },
    "math-expression-evaluator": {
      "version": "1.2.17",
      "from": "math-expression-evaluator@>=1.2.14 <2.0.0",
      "resolved": "https://registry.npmjs.org/math-expression-evaluator/-/math-expression-evaluator-1.2.17.tgz"
    },
    "media-typer": {
      "version": "0.3.0",
      "from": "media-typer@0.3.0",
      "resolved": "https://registry.npmjs.org/media-typer/-/media-typer-0.3.0.tgz"
    },
    "mem": {
      "version": "1.1.0",
      "from": "mem@>=1.1.0 <2.0.0",
      "resolved": "https://registry.npmjs.org/mem/-/mem-1.1.0.tgz"
    },
    "memory-fs": {
      "version": "0.4.1",
      "from": "memory-fs@>=0.4.1 <0.5.0",
      "resolved": "https://registry.npmjs.org/memory-fs/-/memory-fs-0.4.1.tgz",
      "dependencies": {
        "isarray": {
          "version": "1.0.0",
          "from": "isarray@>=1.0.0 <1.1.0",
          "resolved": "https://registry.npmjs.org/isarray/-/isarray-1.0.0.tgz"
        },
        "readable-stream": {
          "version": "2.3.3",
          "from": "readable-stream@>=2.0.1 <3.0.0",
          "resolved": "https://registry.npmjs.org/readable-stream/-/readable-stream-2.3.3.tgz"
        },
        "string_decoder": {
          "version": "1.0.3",
          "from": "string_decoder@>=1.0.3 <1.1.0",
          "resolved": "https://registry.npmjs.org/string_decoder/-/string_decoder-1.0.3.tgz"
        }
      }
    },
    "meow": {
      "version": "3.7.0",
      "from": "meow@>=3.3.0 <4.0.0",
      "resolved": "https://registry.npmjs.org/meow/-/meow-3.7.0.tgz",
      "dependencies": {
        "minimist": {
          "version": "1.2.0",
          "from": "minimist@>=1.1.3 <2.0.0",
          "resolved": "https://registry.npmjs.org/minimist/-/minimist-1.2.0.tgz"
        }
      }
    },
    "merge-descriptors": {
      "version": "1.0.1",
      "from": "merge-descriptors@1.0.1",
      "resolved": "https://registry.npmjs.org/merge-descriptors/-/merge-descriptors-1.0.1.tgz"
    },
    "methods": {
      "version": "1.1.2",
      "from": "methods@>=1.1.2 <1.2.0",
      "resolved": "https://registry.npmjs.org/methods/-/methods-1.1.2.tgz"
    },
    "micromatch": {
      "version": "2.3.11",
      "from": "micromatch@>=2.1.5 <3.0.0",
      "resolved": "https://registry.npmjs.org/micromatch/-/micromatch-2.3.11.tgz"
    },
    "miller-rabin": {
      "version": "4.0.0",
      "from": "miller-rabin@>=4.0.0 <5.0.0",
      "resolved": "https://registry.npmjs.org/miller-rabin/-/miller-rabin-4.0.0.tgz"
    },
    "mime": {
      "version": "1.3.4",
      "from": "mime@1.3.4",
      "resolved": "https://registry.npmjs.org/mime/-/mime-1.3.4.tgz"
    },
    "mime-db": {
      "version": "1.27.0",
      "from": "mime-db@>=1.27.0 <1.28.0",
      "resolved": "https://registry.npmjs.org/mime-db/-/mime-db-1.27.0.tgz"
    },
    "mime-types": {
      "version": "2.1.15",
      "from": "mime-types@>=2.1.11 <2.2.0",
      "resolved": "https://registry.npmjs.org/mime-types/-/mime-types-2.1.15.tgz"
    },
    "mimic-fn": {
      "version": "1.1.0",
      "from": "mimic-fn@>=1.0.0 <2.0.0",
      "resolved": "https://registry.npmjs.org/mimic-fn/-/mimic-fn-1.1.0.tgz"
    },
    "mimic-response": {
      "version": "1.0.0",
      "from": "mimic-response@>=1.0.0 <2.0.0",
      "resolved": "https://registry.npmjs.org/mimic-response/-/mimic-response-1.0.0.tgz"
    },
    "minimalistic-assert": {
      "version": "1.0.0",
      "from": "minimalistic-assert@>=1.0.0 <2.0.0",
      "resolved": "https://registry.npmjs.org/minimalistic-assert/-/minimalistic-assert-1.0.0.tgz"
    },
    "minimalistic-crypto-utils": {
      "version": "1.0.1",
      "from": "minimalistic-crypto-utils@>=1.0.0 <2.0.0",
      "resolved": "https://registry.npmjs.org/minimalistic-crypto-utils/-/minimalistic-crypto-utils-1.0.1.tgz"
    },
    "minimatch": {
      "version": "3.0.4",
      "from": "minimatch@>=3.0.2 <4.0.0",
      "resolved": "https://registry.npmjs.org/minimatch/-/minimatch-3.0.4.tgz"
    },
    "minimist": {
      "version": "0.0.8",
      "from": "minimist@0.0.8",
      "resolved": "https://registry.npmjs.org/minimist/-/minimist-0.0.8.tgz"
    },
    "mkdirp": {
      "version": "0.5.1",
      "from": "mkdirp@>=0.5.1 <0.6.0",
      "resolved": "https://registry.npmjs.org/mkdirp/-/mkdirp-0.5.1.tgz"
    },
    "ms": {
      "version": "2.0.0",
      "from": "ms@2.0.0",
      "resolved": "https://registry.npmjs.org/ms/-/ms-2.0.0.tgz"
    },
    "multicast-dns": {
      "version": "6.1.1",
      "from": "multicast-dns@>=6.0.1 <7.0.0",
      "resolved": "https://registry.npmjs.org/multicast-dns/-/multicast-dns-6.1.1.tgz"
    },
    "multicast-dns-service-types": {
      "version": "1.1.0",
      "from": "multicast-dns-service-types@>=1.1.0 <2.0.0",
      "resolved": "https://registry.npmjs.org/multicast-dns-service-types/-/multicast-dns-service-types-1.1.0.tgz"
    },
    "nan": {
      "version": "2.6.2",
      "from": "nan@>=2.3.0 <3.0.0",
      "resolved": "https://registry.npmjs.org/nan/-/nan-2.6.2.tgz"
    },
    "negotiator": {
      "version": "0.6.1",
      "from": "negotiator@0.6.1",
      "resolved": "https://registry.npmjs.org/negotiator/-/negotiator-0.6.1.tgz"
    },
    "node-forge": {
      "version": "0.6.33",
      "from": "node-forge@0.6.33",
      "resolved": "https://registry.npmjs.org/node-forge/-/node-forge-0.6.33.tgz"
    },
    "node-libs-browser": {
      "version": "2.0.0",
      "from": "node-libs-browser@>=2.0.0 <3.0.0",
      "resolved": "https://registry.npmjs.org/node-libs-browser/-/node-libs-browser-2.0.0.tgz",
      "dependencies": {
        "isarray": {
          "version": "1.0.0",
          "from": "isarray@>=1.0.0 <1.1.0",
          "resolved": "https://registry.npmjs.org/isarray/-/isarray-1.0.0.tgz"
        },
        "readable-stream": {
          "version": "2.3.3",
          "from": "readable-stream@>=2.0.5 <3.0.0",
          "resolved": "https://registry.npmjs.org/readable-stream/-/readable-stream-2.3.3.tgz",
          "dependencies": {
            "string_decoder": {
              "version": "1.0.3",
              "from": "string_decoder@>=1.0.3 <1.1.0",
              "resolved": "https://registry.npmjs.org/string_decoder/-/string_decoder-1.0.3.tgz"
            }
          }
        }
      }
    },
    "nopt": {
      "version": "3.0.6",
      "from": "nopt@>=2.0.0 <3.0.0||>=3.0.0 <4.0.0",
      "resolved": "https://registry.npmjs.org/nopt/-/nopt-3.0.6.tgz"
    },
    "normalize-package-data": {
      "version": "2.4.0",
      "from": "normalize-package-data@>=2.3.2 <3.0.0",
      "resolved": "https://registry.npmjs.org/normalize-package-data/-/normalize-package-data-2.4.0.tgz"
    },
    "normalize-path": {
      "version": "2.1.1",
      "from": "normalize-path@>=2.0.1 <3.0.0",
      "resolved": "https://registry.npmjs.org/normalize-path/-/normalize-path-2.1.1.tgz"
    },
    "normalize-range": {
      "version": "0.1.2",
      "from": "normalize-range@>=0.1.2 <0.2.0",
      "resolved": "https://registry.npmjs.org/normalize-range/-/normalize-range-0.1.2.tgz"
    },
    "normalize-url": {
      "version": "1.9.1",
      "from": "normalize-url@>=1.4.0 <2.0.0",
      "resolved": "https://registry.npmjs.org/normalize-url/-/normalize-url-1.9.1.tgz"
    },
    "npm-run-path": {
      "version": "2.0.2",
      "from": "npm-run-path@>=2.0.0 <3.0.0",
      "resolved": "https://registry.npmjs.org/npm-run-path/-/npm-run-path-2.0.2.tgz"
    },
    "nth-check": {
      "version": "1.0.1",
      "from": "nth-check@>=1.0.1 <1.1.0",
      "resolved": "https://registry.npmjs.org/nth-check/-/nth-check-1.0.1.tgz"
    },
    "num2fraction": {
      "version": "1.2.2",
      "from": "num2fraction@>=1.2.2 <2.0.0",
      "resolved": "https://registry.npmjs.org/num2fraction/-/num2fraction-1.2.2.tgz"
    },
    "number-is-nan": {
      "version": "1.0.1",
      "from": "number-is-nan@>=1.0.0 <2.0.0",
      "resolved": "https://registry.npmjs.org/number-is-nan/-/number-is-nan-1.0.1.tgz"
    },
    "object-assign": {
      "version": "4.1.1",
      "from": "object-assign@>=4.0.1 <5.0.0",
      "resolved": "https://registry.npmjs.org/object-assign/-/object-assign-4.1.1.tgz"
    },
    "object-path": {
      "version": "0.9.2",
      "from": "object-path@>=0.9.2 <0.10.0",
      "resolved": "https://registry.npmjs.org/object-path/-/object-path-0.9.2.tgz"
    },
    "object.omit": {
      "version": "2.0.1",
      "from": "object.omit@>=2.0.0 <3.0.0",
      "resolved": "https://registry.npmjs.org/object.omit/-/object.omit-2.0.1.tgz"
    },
    "obuf": {
      "version": "1.1.1",
      "from": "obuf@>=1.1.1 <2.0.0",
      "resolved": "https://registry.npmjs.org/obuf/-/obuf-1.1.1.tgz"
    },
    "on-finished": {
      "version": "2.3.0",
      "from": "on-finished@>=2.3.0 <2.4.0",
      "resolved": "https://registry.npmjs.org/on-finished/-/on-finished-2.3.0.tgz"
    },
    "on-headers": {
      "version": "1.0.1",
      "from": "on-headers@>=1.0.1 <1.1.0",
      "resolved": "https://registry.npmjs.org/on-headers/-/on-headers-1.0.1.tgz"
    },
    "once": {
      "version": "1.4.0",
      "from": "once@>=1.3.0 <2.0.0",
      "resolved": "https://registry.npmjs.org/once/-/once-1.4.0.tgz"
    },
    "opn": {
      "version": "4.0.2",
      "from": "opn@4.0.2",
      "resolved": "https://registry.npmjs.org/opn/-/opn-4.0.2.tgz"
    },
    "original": {
      "version": "1.0.0",
      "from": "original@>=0.0.5",
      "resolved": "https://registry.npmjs.org/original/-/original-1.0.0.tgz",
      "dependencies": {
        "url-parse": {
          "version": "1.0.5",
          "from": "url-parse@>=1.0.0 <1.1.0",
          "resolved": "https://registry.npmjs.org/url-parse/-/url-parse-1.0.5.tgz"
        }
      }
    },
    "os-browserify": {
      "version": "0.2.1",
      "from": "os-browserify@>=0.2.0 <0.3.0",
      "resolved": "https://registry.npmjs.org/os-browserify/-/os-browserify-0.2.1.tgz"
    },
    "os-homedir": {
      "version": "1.0.2",
      "from": "os-homedir@>=1.0.0 <2.0.0",
      "resolved": "https://registry.npmjs.org/os-homedir/-/os-homedir-1.0.2.tgz"
    },
    "os-locale": {
      "version": "1.4.0",
      "from": "os-locale@>=1.4.0 <2.0.0",
      "resolved": "https://registry.npmjs.org/os-locale/-/os-locale-1.4.0.tgz"
    },
    "os-tmpdir": {
      "version": "1.0.2",
      "from": "os-tmpdir@>=1.0.1 <2.0.0",
      "resolved": "https://registry.npmjs.org/os-tmpdir/-/os-tmpdir-1.0.2.tgz"
    },
    "p-cancelable": {
      "version": "0.3.0",
      "from": "p-cancelable@>=0.3.0 <0.4.0",
      "resolved": "https://registry.npmjs.org/p-cancelable/-/p-cancelable-0.3.0.tgz"
    },
    "p-finally": {
      "version": "1.0.0",
      "from": "p-finally@>=1.0.0 <2.0.0",
      "resolved": "https://registry.npmjs.org/p-finally/-/p-finally-1.0.0.tgz"
    },
    "p-limit": {
      "version": "1.1.0",
      "from": "p-limit@>=1.1.0 <2.0.0",
      "resolved": "https://registry.npmjs.org/p-limit/-/p-limit-1.1.0.tgz"
    },
    "p-locate": {
      "version": "2.0.0",
      "from": "p-locate@>=2.0.0 <3.0.0",
      "resolved": "https://registry.npmjs.org/p-locate/-/p-locate-2.0.0.tgz"
    },
    "p-map": {
      "version": "1.1.1",
      "from": "p-map@>=1.1.1 <2.0.0",
      "resolved": "https://registry.npmjs.org/p-map/-/p-map-1.1.1.tgz"
    },
    "p-timeout": {
      "version": "1.2.0",
      "from": "p-timeout@>=1.1.1 <2.0.0",
      "resolved": "https://registry.npmjs.org/p-timeout/-/p-timeout-1.2.0.tgz"
    },
    "pako": {
      "version": "0.2.9",
      "from": "pako@>=0.2.0 <0.3.0",
      "resolved": "https://registry.npmjs.org/pako/-/pako-0.2.9.tgz"
    },
    "parse-asn1": {
      "version": "5.1.0",
      "from": "parse-asn1@>=5.0.0 <6.0.0",
      "resolved": "https://registry.npmjs.org/parse-asn1/-/parse-asn1-5.1.0.tgz"
    },
    "parse-glob": {
      "version": "3.0.4",
      "from": "parse-glob@>=3.0.4 <4.0.0",
      "resolved": "https://registry.npmjs.org/parse-glob/-/parse-glob-3.0.4.tgz"
    },
    "parse-json": {
      "version": "2.2.0",
      "from": "parse-json@>=2.2.0 <3.0.0",
      "resolved": "https://registry.npmjs.org/parse-json/-/parse-json-2.2.0.tgz"
    },
    "parseurl": {
      "version": "1.3.1",
      "from": "parseurl@>=1.3.1 <1.4.0",
      "resolved": "https://registry.npmjs.org/parseurl/-/parseurl-1.3.1.tgz"
    },
    "path-browserify": {
      "version": "0.0.0",
      "from": "path-browserify@0.0.0",
      "resolved": "https://registry.npmjs.org/path-browserify/-/path-browserify-0.0.0.tgz"
    },
    "path-exists": {
      "version": "3.0.0",
      "from": "path-exists@>=3.0.0 <4.0.0",
      "resolved": "https://registry.npmjs.org/path-exists/-/path-exists-3.0.0.tgz"
    },
    "path-is-absolute": {
      "version": "1.0.1",
      "from": "path-is-absolute@>=1.0.0 <2.0.0",
      "resolved": "https://registry.npmjs.org/path-is-absolute/-/path-is-absolute-1.0.1.tgz"
    },
    "path-is-inside": {
      "version": "1.0.2",
      "from": "path-is-inside@>=1.0.1 <2.0.0",
      "resolved": "https://registry.npmjs.org/path-is-inside/-/path-is-inside-1.0.2.tgz"
    },
    "path-key": {
      "version": "2.0.1",
      "from": "path-key@>=2.0.0 <3.0.0",
      "resolved": "https://registry.npmjs.org/path-key/-/path-key-2.0.1.tgz"
    },
    "path-parse": {
      "version": "1.0.5",
      "from": "path-parse@>=1.0.5 <2.0.0",
      "resolved": "https://registry.npmjs.org/path-parse/-/path-parse-1.0.5.tgz"
    },
    "path-to-regexp": {
      "version": "0.1.7",
      "from": "path-to-regexp@0.1.7",
      "resolved": "https://registry.npmjs.org/path-to-regexp/-/path-to-regexp-0.1.7.tgz"
    },
    "path-type": {
      "version": "1.1.0",
      "from": "path-type@>=1.0.0 <2.0.0",
      "resolved": "https://registry.npmjs.org/path-type/-/path-type-1.1.0.tgz"
    },
    "pbkdf2": {
      "version": "3.0.12",
      "from": "pbkdf2@>=3.0.3 <4.0.0",
      "resolved": "https://registry.npmjs.org/pbkdf2/-/pbkdf2-3.0.12.tgz"
    },
    "pify": {
      "version": "2.3.0",
      "from": "pify@>=2.3.0 <3.0.0",
      "resolved": "https://registry.npmjs.org/pify/-/pify-2.3.0.tgz"
    },
    "pinkie": {
      "version": "2.0.4",
      "from": "pinkie@>=2.0.0 <3.0.0",
      "resolved": "https://registry.npmjs.org/pinkie/-/pinkie-2.0.4.tgz"
    },
    "pinkie-promise": {
      "version": "2.0.1",
      "from": "pinkie-promise@>=2.0.0 <3.0.0",
      "resolved": "https://registry.npmjs.org/pinkie-promise/-/pinkie-promise-2.0.1.tgz"
    },
    "pkg-dir": {
      "version": "2.0.0",
      "from": "pkg-dir@>=2.0.0 <3.0.0",
      "resolved": "https://registry.npmjs.org/pkg-dir/-/pkg-dir-2.0.0.tgz"
    },
    "pkg-up": {
      "version": "1.0.0",
      "from": "pkg-up@>=1.0.0 <2.0.0",
      "resolved": "https://registry.npmjs.org/pkg-up/-/pkg-up-1.0.0.tgz",
      "dependencies": {
        "find-up": {
          "version": "1.1.2",
          "from": "find-up@>=1.0.0 <2.0.0",
          "resolved": "https://registry.npmjs.org/find-up/-/find-up-1.1.2.tgz"
        },
        "path-exists": {
          "version": "2.1.0",
          "from": "path-exists@>=2.0.0 <3.0.0",
          "resolved": "https://registry.npmjs.org/path-exists/-/path-exists-2.1.0.tgz"
        }
      }
    },
    "portfinder": {
      "version": "1.0.13",
      "from": "portfinder@>=1.0.9 <2.0.0",
      "resolved": "https://registry.npmjs.org/portfinder/-/portfinder-1.0.13.tgz",
      "dependencies": {
        "async": {
          "version": "1.5.2",
          "from": "async@>=1.5.2 <2.0.0",
          "resolved": "https://registry.npmjs.org/async/-/async-1.5.2.tgz"
        }
      }
    },
    "postcss": {
      "version": "5.2.17",
      "from": "postcss@>=5.0.6 <6.0.0",
      "resolved": "https://registry.npmjs.org/postcss/-/postcss-5.2.17.tgz",
      "dependencies": {
        "supports-color": {
          "version": "3.2.3",
          "from": "supports-color@>=3.2.3 <4.0.0",
          "resolved": "https://registry.npmjs.org/supports-color/-/supports-color-3.2.3.tgz"
        }
      }
    },
    "postcss-calc": {
      "version": "5.3.1",
      "from": "postcss-calc@>=5.2.0 <6.0.0",
      "resolved": "https://registry.npmjs.org/postcss-calc/-/postcss-calc-5.3.1.tgz"
    },
    "postcss-colormin": {
      "version": "2.2.2",
      "from": "postcss-colormin@>=2.1.8 <3.0.0",
      "resolved": "https://registry.npmjs.org/postcss-colormin/-/postcss-colormin-2.2.2.tgz"
    },
    "postcss-convert-values": {
      "version": "2.6.1",
      "from": "postcss-convert-values@>=2.3.4 <3.0.0",
      "resolved": "https://registry.npmjs.org/postcss-convert-values/-/postcss-convert-values-2.6.1.tgz"
    },
    "postcss-discard-comments": {
      "version": "2.0.4",
      "from": "postcss-discard-comments@>=2.0.4 <3.0.0",
      "resolved": "https://registry.npmjs.org/postcss-discard-comments/-/postcss-discard-comments-2.0.4.tgz"
    },
    "postcss-discard-duplicates": {
      "version": "2.1.0",
      "from": "postcss-discard-duplicates@>=2.0.1 <3.0.0",
      "resolved": "https://registry.npmjs.org/postcss-discard-duplicates/-/postcss-discard-duplicates-2.1.0.tgz"
    },
    "postcss-discard-empty": {
      "version": "2.1.0",
      "from": "postcss-discard-empty@>=2.0.1 <3.0.0",
      "resolved": "https://registry.npmjs.org/postcss-discard-empty/-/postcss-discard-empty-2.1.0.tgz"
    },
    "postcss-discard-overridden": {
      "version": "0.1.1",
      "from": "postcss-discard-overridden@>=0.1.1 <0.2.0",
      "resolved": "https://registry.npmjs.org/postcss-discard-overridden/-/postcss-discard-overridden-0.1.1.tgz"
    },
    "postcss-discard-unused": {
      "version": "2.2.3",
      "from": "postcss-discard-unused@>=2.2.1 <3.0.0",
      "resolved": "https://registry.npmjs.org/postcss-discard-unused/-/postcss-discard-unused-2.2.3.tgz"
    },
    "postcss-filter-plugins": {
      "version": "2.0.2",
      "from": "postcss-filter-plugins@>=2.0.0 <3.0.0",
      "resolved": "https://registry.npmjs.org/postcss-filter-plugins/-/postcss-filter-plugins-2.0.2.tgz"
    },
    "postcss-load-config": {
      "version": "1.2.0",
      "from": "postcss-load-config@>=1.1.0 <2.0.0",
      "resolved": "https://registry.npmjs.org/postcss-load-config/-/postcss-load-config-1.2.0.tgz"
    },
    "postcss-load-options": {
      "version": "1.2.0",
      "from": "postcss-load-options@>=1.2.0 <2.0.0",
      "resolved": "https://registry.npmjs.org/postcss-load-options/-/postcss-load-options-1.2.0.tgz"
    },
    "postcss-load-plugins": {
      "version": "2.3.0",
      "from": "postcss-load-plugins@>=2.3.0 <3.0.0",
      "resolved": "https://registry.npmjs.org/postcss-load-plugins/-/postcss-load-plugins-2.3.0.tgz"
    },
    "postcss-merge-idents": {
      "version": "2.1.7",
      "from": "postcss-merge-idents@>=2.1.5 <3.0.0",
      "resolved": "https://registry.npmjs.org/postcss-merge-idents/-/postcss-merge-idents-2.1.7.tgz"
    },
    "postcss-merge-longhand": {
      "version": "2.0.2",
      "from": "postcss-merge-longhand@>=2.0.1 <3.0.0",
      "resolved": "https://registry.npmjs.org/postcss-merge-longhand/-/postcss-merge-longhand-2.0.2.tgz"
    },
    "postcss-merge-rules": {
      "version": "2.1.2",
      "from": "postcss-merge-rules@>=2.0.3 <3.0.0",
      "resolved": "https://registry.npmjs.org/postcss-merge-rules/-/postcss-merge-rules-2.1.2.tgz",
      "dependencies": {
        "browserslist": {
          "version": "1.7.7",
          "from": "browserslist@>=1.5.2 <2.0.0",
          "resolved": "https://registry.npmjs.org/browserslist/-/browserslist-1.7.7.tgz"
        }
      }
    },
    "postcss-message-helpers": {
      "version": "2.0.0",
      "from": "postcss-message-helpers@>=2.0.0 <3.0.0",
      "resolved": "https://registry.npmjs.org/postcss-message-helpers/-/postcss-message-helpers-2.0.0.tgz"
    },
    "postcss-minify-font-values": {
      "version": "1.0.5",
      "from": "postcss-minify-font-values@>=1.0.2 <2.0.0",
      "resolved": "https://registry.npmjs.org/postcss-minify-font-values/-/postcss-minify-font-values-1.0.5.tgz"
    },
    "postcss-minify-gradients": {
      "version": "1.0.5",
      "from": "postcss-minify-gradients@>=1.0.1 <2.0.0",
      "resolved": "https://registry.npmjs.org/postcss-minify-gradients/-/postcss-minify-gradients-1.0.5.tgz"
    },
    "postcss-minify-params": {
      "version": "1.2.2",
      "from": "postcss-minify-params@>=1.0.4 <2.0.0",
      "resolved": "https://registry.npmjs.org/postcss-minify-params/-/postcss-minify-params-1.2.2.tgz"
    },
    "postcss-minify-selectors": {
      "version": "2.1.1",
      "from": "postcss-minify-selectors@>=2.0.4 <3.0.0",
      "resolved": "https://registry.npmjs.org/postcss-minify-selectors/-/postcss-minify-selectors-2.1.1.tgz"
    },
    "postcss-modules-extract-imports": {
      "version": "1.1.0",
      "from": "postcss-modules-extract-imports@>=1.0.0 <2.0.0",
      "resolved": "https://registry.npmjs.org/postcss-modules-extract-imports/-/postcss-modules-extract-imports-1.1.0.tgz",
      "dependencies": {
        "ansi-styles": {
          "version": "3.1.0",
          "from": "ansi-styles@>=3.1.0 <4.0.0",
          "resolved": "https://registry.npmjs.org/ansi-styles/-/ansi-styles-3.1.0.tgz"
        },
        "chalk": {
          "version": "2.0.1",
          "from": "chalk@>=2.0.1 <3.0.0",
          "resolved": "https://registry.npmjs.org/chalk/-/chalk-2.0.1.tgz"
        },
        "has-flag": {
          "version": "2.0.0",
          "from": "has-flag@>=2.0.0 <3.0.0",
          "resolved": "https://registry.npmjs.org/has-flag/-/has-flag-2.0.0.tgz"
        },
        "postcss": {
          "version": "6.0.6",
          "from": "postcss@>=6.0.1 <7.0.0",
          "resolved": "https://registry.npmjs.org/postcss/-/postcss-6.0.6.tgz"
        },
        "supports-color": {
          "version": "4.2.0",
          "from": "supports-color@>=4.1.0 <5.0.0",
          "resolved": "https://registry.npmjs.org/supports-color/-/supports-color-4.2.0.tgz"
        }
      }
    },
    "postcss-modules-local-by-default": {
      "version": "1.2.0",
      "from": "postcss-modules-local-by-default@>=1.0.1 <2.0.0",
      "resolved": "https://registry.npmjs.org/postcss-modules-local-by-default/-/postcss-modules-local-by-default-1.2.0.tgz",
      "dependencies": {
        "ansi-styles": {
          "version": "3.1.0",
          "from": "ansi-styles@>=3.1.0 <4.0.0",
          "resolved": "https://registry.npmjs.org/ansi-styles/-/ansi-styles-3.1.0.tgz"
        },
        "chalk": {
          "version": "2.0.1",
          "from": "chalk@>=2.0.1 <3.0.0",
          "resolved": "https://registry.npmjs.org/chalk/-/chalk-2.0.1.tgz"
        },
        "has-flag": {
          "version": "2.0.0",
          "from": "has-flag@>=2.0.0 <3.0.0",
          "resolved": "https://registry.npmjs.org/has-flag/-/has-flag-2.0.0.tgz"
        },
        "postcss": {
          "version": "6.0.6",
          "from": "postcss@>=6.0.1 <7.0.0",
          "resolved": "https://registry.npmjs.org/postcss/-/postcss-6.0.6.tgz"
        },
        "supports-color": {
          "version": "4.2.0",
          "from": "supports-color@>=4.1.0 <5.0.0",
          "resolved": "https://registry.npmjs.org/supports-color/-/supports-color-4.2.0.tgz"
        }
      }
    },
    "postcss-modules-scope": {
      "version": "1.1.0",
      "from": "postcss-modules-scope@>=1.0.0 <2.0.0",
      "resolved": "https://registry.npmjs.org/postcss-modules-scope/-/postcss-modules-scope-1.1.0.tgz",
      "dependencies": {
        "ansi-styles": {
          "version": "3.1.0",
          "from": "ansi-styles@>=3.1.0 <4.0.0",
          "resolved": "https://registry.npmjs.org/ansi-styles/-/ansi-styles-3.1.0.tgz"
        },
        "chalk": {
          "version": "2.0.1",
          "from": "chalk@>=2.0.1 <3.0.0",
          "resolved": "https://registry.npmjs.org/chalk/-/chalk-2.0.1.tgz"
        },
        "has-flag": {
          "version": "2.0.0",
          "from": "has-flag@>=2.0.0 <3.0.0",
          "resolved": "https://registry.npmjs.org/has-flag/-/has-flag-2.0.0.tgz"
        },
        "postcss": {
          "version": "6.0.6",
          "from": "postcss@>=6.0.1 <7.0.0",
          "resolved": "https://registry.npmjs.org/postcss/-/postcss-6.0.6.tgz"
        },
        "supports-color": {
          "version": "4.2.0",
          "from": "supports-color@>=4.1.0 <5.0.0",
          "resolved": "https://registry.npmjs.org/supports-color/-/supports-color-4.2.0.tgz"
        }
      }
    },
    "postcss-modules-values": {
      "version": "1.3.0",
      "from": "postcss-modules-values@>=1.1.0 <2.0.0",
      "resolved": "https://registry.npmjs.org/postcss-modules-values/-/postcss-modules-values-1.3.0.tgz",
      "dependencies": {
        "ansi-styles": {
          "version": "3.1.0",
          "from": "ansi-styles@>=3.1.0 <4.0.0",
          "resolved": "https://registry.npmjs.org/ansi-styles/-/ansi-styles-3.1.0.tgz"
        },
        "chalk": {
          "version": "2.0.1",
          "from": "chalk@>=2.0.1 <3.0.0",
          "resolved": "https://registry.npmjs.org/chalk/-/chalk-2.0.1.tgz"
        },
        "has-flag": {
          "version": "2.0.0",
          "from": "has-flag@>=2.0.0 <3.0.0",
          "resolved": "https://registry.npmjs.org/has-flag/-/has-flag-2.0.0.tgz"
        },
        "postcss": {
          "version": "6.0.6",
          "from": "postcss@>=6.0.1 <7.0.0",
          "resolved": "https://registry.npmjs.org/postcss/-/postcss-6.0.6.tgz"
        },
        "supports-color": {
          "version": "4.2.0",
          "from": "supports-color@>=4.1.0 <5.0.0",
          "resolved": "https://registry.npmjs.org/supports-color/-/supports-color-4.2.0.tgz"
        }
      }
    },
    "postcss-normalize-charset": {
      "version": "1.1.1",
      "from": "postcss-normalize-charset@>=1.1.0 <2.0.0",
      "resolved": "https://registry.npmjs.org/postcss-normalize-charset/-/postcss-normalize-charset-1.1.1.tgz"
    },
    "postcss-normalize-url": {
      "version": "3.0.8",
      "from": "postcss-normalize-url@>=3.0.7 <4.0.0",
      "resolved": "https://registry.npmjs.org/postcss-normalize-url/-/postcss-normalize-url-3.0.8.tgz"
    },
    "postcss-ordered-values": {
      "version": "2.2.3",
      "from": "postcss-ordered-values@>=2.1.0 <3.0.0",
      "resolved": "https://registry.npmjs.org/postcss-ordered-values/-/postcss-ordered-values-2.2.3.tgz"
    },
    "postcss-reduce-idents": {
      "version": "2.4.0",
      "from": "postcss-reduce-idents@>=2.2.2 <3.0.0",
      "resolved": "https://registry.npmjs.org/postcss-reduce-idents/-/postcss-reduce-idents-2.4.0.tgz"
    },
    "postcss-reduce-initial": {
      "version": "1.0.1",
      "from": "postcss-reduce-initial@>=1.0.0 <2.0.0",
      "resolved": "https://registry.npmjs.org/postcss-reduce-initial/-/postcss-reduce-initial-1.0.1.tgz"
    },
    "postcss-reduce-transforms": {
      "version": "1.0.4",
      "from": "postcss-reduce-transforms@>=1.0.3 <2.0.0",
      "resolved": "https://registry.npmjs.org/postcss-reduce-transforms/-/postcss-reduce-transforms-1.0.4.tgz"
    },
    "postcss-selector-parser": {
      "version": "2.2.3",
      "from": "postcss-selector-parser@>=2.2.2 <3.0.0",
      "resolved": "https://registry.npmjs.org/postcss-selector-parser/-/postcss-selector-parser-2.2.3.tgz"
    },
    "postcss-svgo": {
      "version": "2.1.6",
      "from": "postcss-svgo@>=2.1.1 <3.0.0",
      "resolved": "https://registry.npmjs.org/postcss-svgo/-/postcss-svgo-2.1.6.tgz"
    },
    "postcss-unique-selectors": {
      "version": "2.0.2",
      "from": "postcss-unique-selectors@>=2.0.2 <3.0.0",
      "resolved": "https://registry.npmjs.org/postcss-unique-selectors/-/postcss-unique-selectors-2.0.2.tgz"
    },
    "postcss-value-parser": {
      "version": "3.3.0",
      "from": "postcss-value-parser@>=3.2.3 <4.0.0",
      "resolved": "https://registry.npmjs.org/postcss-value-parser/-/postcss-value-parser-3.3.0.tgz"
    },
    "postcss-zindex": {
      "version": "2.2.0",
      "from": "postcss-zindex@>=2.0.1 <3.0.0",
      "resolved": "https://registry.npmjs.org/postcss-zindex/-/postcss-zindex-2.2.0.tgz"
    },
    "prepend-http": {
      "version": "1.0.4",
      "from": "prepend-http@>=1.0.0 <2.0.0",
      "resolved": "https://registry.npmjs.org/prepend-http/-/prepend-http-1.0.4.tgz"
    },
    "preserve": {
      "version": "0.2.0",
      "from": "preserve@>=0.2.0 <0.3.0",
      "resolved": "https://registry.npmjs.org/preserve/-/preserve-0.2.0.tgz"
    },
    "pretty-error": {
      "version": "2.1.1",
      "from": "pretty-error@>=2.1.1 <3.0.0",
      "resolved": "https://registry.npmjs.org/pretty-error/-/pretty-error-2.1.1.tgz"
    },
    "private": {
      "version": "0.1.7",
      "from": "private@>=0.1.6 <0.2.0",
      "resolved": "https://registry.npmjs.org/private/-/private-0.1.7.tgz"
    },
    "process": {
      "version": "0.11.10",
      "from": "process@>=0.11.0 <0.12.0",
      "resolved": "https://registry.npmjs.org/process/-/process-0.11.10.tgz"
    },
    "process-nextick-args": {
      "version": "1.0.7",
      "from": "process-nextick-args@>=1.0.6 <1.1.0",
      "resolved": "https://registry.npmjs.org/process-nextick-args/-/process-nextick-args-1.0.7.tgz"
    },
    "proto-list": {
      "version": "1.2.4",
      "from": "proto-list@>=1.2.1 <1.3.0",
      "resolved": "https://registry.npmjs.org/proto-list/-/proto-list-1.2.4.tgz"
    },
    "proxy-addr": {
      "version": "1.1.4",
      "from": "proxy-addr@>=1.1.4 <1.2.0",
      "resolved": "https://registry.npmjs.org/proxy-addr/-/proxy-addr-1.1.4.tgz"
    },
    "prr": {
      "version": "0.0.0",
      "from": "prr@>=0.0.0 <0.1.0",
      "resolved": "https://registry.npmjs.org/prr/-/prr-0.0.0.tgz"
    },
    "pseudomap": {
      "version": "1.0.2",
      "from": "pseudomap@>=1.0.2 <2.0.0",
      "resolved": "https://registry.npmjs.org/pseudomap/-/pseudomap-1.0.2.tgz"
    },
    "public-encrypt": {
      "version": "4.0.0",
      "from": "public-encrypt@>=4.0.0 <5.0.0",
      "resolved": "https://registry.npmjs.org/public-encrypt/-/public-encrypt-4.0.0.tgz"
    },
    "punycode": {
      "version": "1.4.1",
      "from": "punycode@>=1.2.4 <2.0.0",
      "resolved": "https://registry.npmjs.org/punycode/-/punycode-1.4.1.tgz"
    },
    "q": {
      "version": "1.5.0",
      "from": "q@>=1.1.2 <2.0.0",
      "resolved": "https://registry.npmjs.org/q/-/q-1.5.0.tgz"
    },
    "qs": {
      "version": "6.4.0",
      "from": "qs@6.4.0",
      "resolved": "https://registry.npmjs.org/qs/-/qs-6.4.0.tgz"
    },
    "query-string": {
      "version": "4.3.4",
      "from": "query-string@>=4.1.0 <5.0.0",
      "resolved": "https://registry.npmjs.org/query-string/-/query-string-4.3.4.tgz"
    },
    "querystring": {
      "version": "0.2.0",
      "from": "querystring@0.2.0",
      "resolved": "https://registry.npmjs.org/querystring/-/querystring-0.2.0.tgz"
    },
    "querystring-es3": {
      "version": "0.2.1",
      "from": "querystring-es3@>=0.2.0 <0.3.0",
      "resolved": "https://registry.npmjs.org/querystring-es3/-/querystring-es3-0.2.1.tgz"
    },
    "querystringify": {
      "version": "0.0.4",
      "from": "querystringify@>=0.0.0 <0.1.0",
      "resolved": "https://registry.npmjs.org/querystringify/-/querystringify-0.0.4.tgz"
    },
    "randomatic": {
      "version": "1.1.7",
      "from": "randomatic@>=1.1.3 <2.0.0",
      "resolved": "https://registry.npmjs.org/randomatic/-/randomatic-1.1.7.tgz",
      "dependencies": {
        "is-number": {
          "version": "3.0.0",
          "from": "is-number@>=3.0.0 <4.0.0",
          "resolved": "https://registry.npmjs.org/is-number/-/is-number-3.0.0.tgz",
          "dependencies": {
            "kind-of": {
              "version": "3.2.2",
              "from": "kind-of@^3.0.2",
              "resolved": "https://registry.npmjs.org/kind-of/-/kind-of-3.2.2.tgz"
            }
          }
        },
        "kind-of": {
          "version": "4.0.0",
          "from": "kind-of@>=4.0.0 <5.0.0",
          "resolved": "https://registry.npmjs.org/kind-of/-/kind-of-4.0.0.tgz"
        }
      }
    },
    "randombytes": {
      "version": "2.0.5",
      "from": "randombytes@>=2.0.0 <3.0.0",
      "resolved": "https://registry.npmjs.org/randombytes/-/randombytes-2.0.5.tgz"
    },
    "range-parser": {
      "version": "1.2.0",
      "from": "range-parser@>=1.2.0 <1.3.0",
      "resolved": "https://registry.npmjs.org/range-parser/-/range-parser-1.2.0.tgz"
    },
    "read-pkg": {
      "version": "1.1.0",
      "from": "read-pkg@>=1.0.0 <2.0.0",
      "resolved": "https://registry.npmjs.org/read-pkg/-/read-pkg-1.1.0.tgz"
    },
    "read-pkg-up": {
      "version": "1.0.1",
      "from": "read-pkg-up@>=1.0.1 <2.0.0",
      "resolved": "https://registry.npmjs.org/read-pkg-up/-/read-pkg-up-1.0.1.tgz",
      "dependencies": {
        "find-up": {
          "version": "1.1.2",
          "from": "find-up@>=1.0.0 <2.0.0",
          "resolved": "https://registry.npmjs.org/find-up/-/find-up-1.1.2.tgz"
        },
        "path-exists": {
          "version": "2.1.0",
          "from": "path-exists@>=2.0.0 <3.0.0",
          "resolved": "https://registry.npmjs.org/path-exists/-/path-exists-2.1.0.tgz"
        }
      }
    },
    "readable-stream": {
      "version": "1.0.34",
      "from": "readable-stream@>=1.0.0 <1.1.0",
      "resolved": "https://registry.npmjs.org/readable-stream/-/readable-stream-1.0.34.tgz"
    },
    "readdirp": {
      "version": "2.1.0",
      "from": "readdirp@>=2.0.0 <3.0.0",
      "resolved": "https://registry.npmjs.org/readdirp/-/readdirp-2.1.0.tgz",
      "dependencies": {
        "isarray": {
          "version": "1.0.0",
          "from": "isarray@>=1.0.0 <1.1.0",
          "resolved": "https://registry.npmjs.org/isarray/-/isarray-1.0.0.tgz"
        },
        "readable-stream": {
          "version": "2.3.3",
          "from": "readable-stream@>=2.0.2 <3.0.0",
          "resolved": "https://registry.npmjs.org/readable-stream/-/readable-stream-2.3.3.tgz"
        },
        "string_decoder": {
          "version": "1.0.3",
          "from": "string_decoder@>=1.0.3 <1.1.0",
          "resolved": "https://registry.npmjs.org/string_decoder/-/string_decoder-1.0.3.tgz"
        }
      }
    },
    "redent": {
      "version": "1.0.0",
      "from": "redent@>=1.0.0 <2.0.0",
      "resolved": "https://registry.npmjs.org/redent/-/redent-1.0.0.tgz"
    },
    "reduce-css-calc": {
      "version": "1.3.0",
      "from": "reduce-css-calc@>=1.2.6 <2.0.0",
      "resolved": "https://registry.npmjs.org/reduce-css-calc/-/reduce-css-calc-1.3.0.tgz",
      "dependencies": {
        "balanced-match": {
          "version": "0.4.2",
          "from": "balanced-match@>=0.4.2 <0.5.0",
          "resolved": "https://registry.npmjs.org/balanced-match/-/balanced-match-0.4.2.tgz"
        }
      }
    },
    "reduce-function-call": {
      "version": "1.0.2",
      "from": "reduce-function-call@>=1.0.1 <2.0.0",
      "resolved": "https://registry.npmjs.org/reduce-function-call/-/reduce-function-call-1.0.2.tgz",
      "dependencies": {
        "balanced-match": {
          "version": "0.4.2",
          "from": "balanced-match@>=0.4.2 <0.5.0",
          "resolved": "https://registry.npmjs.org/balanced-match/-/balanced-match-0.4.2.tgz"
        }
      }
    },
    "regenerate": {
      "version": "1.3.2",
      "from": "regenerate@>=1.2.1 <2.0.0",
      "resolved": "https://registry.npmjs.org/regenerate/-/regenerate-1.3.2.tgz"
    },
    "regenerator-runtime": {
      "version": "0.10.5",
      "from": "regenerator-runtime@>=0.10.0 <0.11.0",
      "resolved": "https://registry.npmjs.org/regenerator-runtime/-/regenerator-runtime-0.10.5.tgz"
    },
    "regenerator-transform": {
      "version": "0.9.11",
      "from": "regenerator-transform@0.9.11",
      "resolved": "https://registry.npmjs.org/regenerator-transform/-/regenerator-transform-0.9.11.tgz"
    },
    "regex-cache": {
      "version": "0.4.3",
      "from": "regex-cache@>=0.4.2 <0.5.0",
      "resolved": "https://registry.npmjs.org/regex-cache/-/regex-cache-0.4.3.tgz"
    },
    "regex-parser": {
      "version": "2.2.7",
      "from": "regex-parser@>=2.2.1 <3.0.0",
      "resolved": "https://registry.npmjs.org/regex-parser/-/regex-parser-2.2.7.tgz"
    },
    "regexpu-core": {
      "version": "2.0.0",
      "from": "regexpu-core@>=2.0.0 <3.0.0",
      "resolved": "https://registry.npmjs.org/regexpu-core/-/regexpu-core-2.0.0.tgz"
    },
    "regjsgen": {
      "version": "0.2.0",
      "from": "regjsgen@>=0.2.0 <0.3.0",
      "resolved": "https://registry.npmjs.org/regjsgen/-/regjsgen-0.2.0.tgz"
    },
    "regjsparser": {
      "version": "0.1.5",
      "from": "regjsparser@>=0.1.4 <0.2.0",
      "resolved": "https://registry.npmjs.org/regjsparser/-/regjsparser-0.1.5.tgz",
      "dependencies": {
        "jsesc": {
          "version": "0.5.0",
          "from": "jsesc@>=0.5.0 <0.6.0",
          "resolved": "https://registry.npmjs.org/jsesc/-/jsesc-0.5.0.tgz"
        }
      }
    },
    "remove-trailing-separator": {
      "version": "1.0.2",
      "from": "remove-trailing-separator@>=1.0.1 <2.0.0",
      "resolved": "https://registry.npmjs.org/remove-trailing-separator/-/remove-trailing-separator-1.0.2.tgz"
    },
    "renderkid": {
      "version": "2.0.1",
      "from": "renderkid@>=2.0.1 <3.0.0",
      "resolved": "https://registry.npmjs.org/renderkid/-/renderkid-2.0.1.tgz",
      "dependencies": {
        "utila": {
          "version": "0.3.3",
          "from": "utila@>=0.3.0 <0.4.0",
          "resolved": "https://registry.npmjs.org/utila/-/utila-0.3.3.tgz"
        }
      }
    },
    "repeat-element": {
      "version": "1.1.2",
      "from": "repeat-element@>=1.1.2 <2.0.0",
      "resolved": "https://registry.npmjs.org/repeat-element/-/repeat-element-1.1.2.tgz"
    },
    "repeat-string": {
      "version": "1.6.1",
      "from": "repeat-string@>=1.5.2 <2.0.0",
      "resolved": "https://registry.npmjs.org/repeat-string/-/repeat-string-1.6.1.tgz"
    },
    "repeating": {
      "version": "2.0.1",
      "from": "repeating@>=2.0.0 <3.0.0",
      "resolved": "https://registry.npmjs.org/repeating/-/repeating-2.0.1.tgz"
    },
    "require-directory": {
      "version": "2.1.1",
      "from": "require-directory@>=2.1.1 <3.0.0",
      "resolved": "https://registry.npmjs.org/require-directory/-/require-directory-2.1.1.tgz"
    },
    "require-from-string": {
      "version": "1.2.1",
      "from": "require-from-string@>=1.1.0 <2.0.0",
      "resolved": "https://registry.npmjs.org/require-from-string/-/require-from-string-1.2.1.tgz"
    },
    "require-main-filename": {
      "version": "1.0.1",
      "from": "require-main-filename@>=1.0.1 <2.0.0",
      "resolved": "https://registry.npmjs.org/require-main-filename/-/require-main-filename-1.0.1.tgz"
    },
    "requires-port": {
      "version": "1.0.0",
      "from": "requires-port@>=1.0.0 <2.0.0",
      "resolved": "https://registry.npmjs.org/requires-port/-/requires-port-1.0.0.tgz"
    },
    "resolve": {
      "version": "1.3.3",
      "from": "resolve@>=1.3.3 <2.0.0",
      "resolved": "https://registry.npmjs.org/resolve/-/resolve-1.3.3.tgz"
    },
    "resolve-url": {
      "version": "0.2.1",
      "from": "resolve-url@>=0.2.1 <0.3.0",
      "resolved": "https://registry.npmjs.org/resolve-url/-/resolve-url-0.2.1.tgz"
    },
    "resolve-url-loader": {
      "version": "2.1.0",
      "from": "resolve-url-loader@>=2.0.2 <3.0.0",
      "resolved": "https://registry.npmjs.org/resolve-url-loader/-/resolve-url-loader-2.1.0.tgz"
    },
    "rework": {
      "version": "1.0.1",
      "from": "rework@>=1.0.1 <2.0.0",
      "resolved": "https://registry.npmjs.org/rework/-/rework-1.0.1.tgz",
      "dependencies": {
        "convert-source-map": {
          "version": "0.3.5",
          "from": "convert-source-map@>=0.3.3 <0.4.0",
          "resolved": "https://registry.npmjs.org/convert-source-map/-/convert-source-map-0.3.5.tgz"
        }
      }
    },
    "rework-visit": {
      "version": "1.0.0",
      "from": "rework-visit@>=1.0.0 <2.0.0",
      "resolved": "https://registry.npmjs.org/rework-visit/-/rework-visit-1.0.0.tgz"
    },
    "right-align": {
      "version": "0.1.3",
      "from": "right-align@>=0.1.1 <0.2.0",
      "resolved": "https://registry.npmjs.org/right-align/-/right-align-0.1.3.tgz"
    },
    "rimraf": {
      "version": "2.5.4",
      "from": "rimraf@>=2.5.1 <2.6.0",
      "resolved": "https://registry.npmjs.org/rimraf/-/rimraf-2.5.4.tgz"
    },
    "ripemd160": {
      "version": "2.0.1",
      "from": "ripemd160@>=2.0.0 <3.0.0",
      "resolved": "https://registry.npmjs.org/ripemd160/-/ripemd160-2.0.1.tgz"
    },
    "safe-buffer": {
      "version": "5.1.1",
      "from": "safe-buffer@>=5.1.1 <5.2.0",
      "resolved": "https://registry.npmjs.org/safe-buffer/-/safe-buffer-5.1.1.tgz"
    },
    "sax": {
      "version": "1.2.4",
      "from": "sax@>=1.2.1 <1.3.0",
      "resolved": "https://registry.npmjs.org/sax/-/sax-1.2.4.tgz"
    },
    "schema-utils": {
      "version": "0.3.0",
      "from": "schema-utils@>=0.3.0 <0.4.0",
      "resolved": "https://registry.npmjs.org/schema-utils/-/schema-utils-0.3.0.tgz"
    },
    "select-hose": {
      "version": "2.0.0",
      "from": "select-hose@>=2.0.0 <3.0.0",
      "resolved": "https://registry.npmjs.org/select-hose/-/select-hose-2.0.0.tgz"
    },
    "selfsigned": {
      "version": "1.9.1",
      "from": "selfsigned@>=1.9.1 <2.0.0",
      "resolved": "https://registry.npmjs.org/selfsigned/-/selfsigned-1.9.1.tgz"
    },
    "semver": {
      "version": "5.3.0",
      "from": "semver@>=5.3.0 <6.0.0",
      "resolved": "https://registry.npmjs.org/semver/-/semver-5.3.0.tgz"
    },
    "send": {
      "version": "0.15.3",
      "from": "send@0.15.3",
      "resolved": "https://registry.npmjs.org/send/-/send-0.15.3.tgz",
      "dependencies": {
        "debug": {
          "version": "2.6.7",
          "from": "debug@2.6.7",
          "resolved": "https://registry.npmjs.org/debug/-/debug-2.6.7.tgz"
        }
      }
    },
    "serve-index": {
      "version": "1.9.0",
      "from": "serve-index@>=1.7.2 <2.0.0",
      "resolved": "https://registry.npmjs.org/serve-index/-/serve-index-1.9.0.tgz"
    },
    "serve-static": {
      "version": "1.12.3",
      "from": "serve-static@1.12.3",
      "resolved": "https://registry.npmjs.org/serve-static/-/serve-static-1.12.3.tgz"
    },
    "set-blocking": {
      "version": "2.0.0",
      "from": "set-blocking@>=2.0.0 <3.0.0",
      "resolved": "https://registry.npmjs.org/set-blocking/-/set-blocking-2.0.0.tgz"
    },
    "set-immediate-shim": {
      "version": "1.0.1",
      "from": "set-immediate-shim@>=1.0.1 <2.0.0",
      "resolved": "https://registry.npmjs.org/set-immediate-shim/-/set-immediate-shim-1.0.1.tgz"
    },
    "setimmediate": {
      "version": "1.0.5",
      "from": "setimmediate@>=1.0.4 <2.0.0",
      "resolved": "https://registry.npmjs.org/setimmediate/-/setimmediate-1.0.5.tgz"
    },
    "setprototypeof": {
      "version": "1.0.3",
      "from": "setprototypeof@1.0.3",
      "resolved": "https://registry.npmjs.org/setprototypeof/-/setprototypeof-1.0.3.tgz"
    },
    "sha.js": {
      "version": "2.4.8",
      "from": "sha.js@>=2.4.0 <3.0.0",
      "resolved": "https://registry.npmjs.org/sha.js/-/sha.js-2.4.8.tgz"
    },
    "sigmund": {
      "version": "1.0.1",
      "from": "sigmund@>=1.0.1 <2.0.0",
      "resolved": "https://registry.npmjs.org/sigmund/-/sigmund-1.0.1.tgz"
    },
    "signal-exit": {
      "version": "3.0.2",
      "from": "signal-exit@>=3.0.0 <4.0.0",
      "resolved": "https://registry.npmjs.org/signal-exit/-/signal-exit-3.0.2.tgz"
    },
    "slash": {
      "version": "1.0.0",
      "from": "slash@>=1.0.0 <2.0.0",
      "resolved": "https://registry.npmjs.org/slash/-/slash-1.0.0.tgz"
    },
    "sockjs": {
      "version": "0.3.18",
      "from": "sockjs@0.3.18",
      "resolved": "https://registry.npmjs.org/sockjs/-/sockjs-0.3.18.tgz"
    },
    "sockjs-client": {
      "version": "1.1.2",
      "from": "sockjs-client@1.1.2",
      "resolved": "https://registry.npmjs.org/sockjs-client/-/sockjs-client-1.1.2.tgz",
      "dependencies": {
        "faye-websocket": {
          "version": "0.11.1",
          "from": "faye-websocket@>=0.11.0 <0.12.0",
          "resolved": "https://registry.npmjs.org/faye-websocket/-/faye-websocket-0.11.1.tgz"
        }
      }
    },
    "sort-keys": {
      "version": "1.1.2",
      "from": "sort-keys@>=1.0.0 <2.0.0",
      "resolved": "https://registry.npmjs.org/sort-keys/-/sort-keys-1.1.2.tgz"
    },
    "source-list-map": {
      "version": "0.1.8",
      "from": "source-list-map@>=0.1.7 <0.2.0",
      "resolved": "https://registry.npmjs.org/source-list-map/-/source-list-map-0.1.8.tgz"
    },
    "source-map": {
      "version": "0.5.6",
      "from": "source-map@>=0.5.0 <0.6.0",
      "resolved": "https://registry.npmjs.org/source-map/-/source-map-0.5.6.tgz"
    },
    "source-map-resolve": {
      "version": "0.3.1",
      "from": "source-map-resolve@>=0.3.0 <0.4.0",
      "resolved": "https://registry.npmjs.org/source-map-resolve/-/source-map-resolve-0.3.1.tgz"
    },
    "source-map-support": {
      "version": "0.4.15",
      "from": "source-map-support@>=0.4.2 <0.5.0",
      "resolved": "https://registry.npmjs.org/source-map-support/-/source-map-support-0.4.15.tgz"
    },
    "source-map-url": {
      "version": "0.3.0",
      "from": "source-map-url@>=0.3.0 <0.4.0",
      "resolved": "https://registry.npmjs.org/source-map-url/-/source-map-url-0.3.0.tgz"
    },
    "spdx-correct": {
      "version": "1.0.2",
      "from": "spdx-correct@>=1.0.0 <1.1.0",
      "resolved": "https://registry.npmjs.org/spdx-correct/-/spdx-correct-1.0.2.tgz"
    },
    "spdx-expression-parse": {
      "version": "1.0.4",
      "from": "spdx-expression-parse@>=1.0.0 <1.1.0",
      "resolved": "https://registry.npmjs.org/spdx-expression-parse/-/spdx-expression-parse-1.0.4.tgz"
    },
    "spdx-license-ids": {
      "version": "1.2.2",
      "from": "spdx-license-ids@>=1.0.2 <2.0.0",
      "resolved": "https://registry.npmjs.org/spdx-license-ids/-/spdx-license-ids-1.2.2.tgz"
    },
    "spdy": {
      "version": "3.4.7",
      "from": "spdy@>=3.4.1 <4.0.0",
      "resolved": "https://registry.npmjs.org/spdy/-/spdy-3.4.7.tgz"
    },
    "spdy-transport": {
      "version": "2.0.20",
      "from": "spdy-transport@>=2.0.18 <3.0.0",
      "resolved": "https://registry.npmjs.org/spdy-transport/-/spdy-transport-2.0.20.tgz",
      "dependencies": {
        "isarray": {
          "version": "1.0.0",
          "from": "isarray@>=1.0.0 <1.1.0",
          "resolved": "https://registry.npmjs.org/isarray/-/isarray-1.0.0.tgz"
        },
        "readable-stream": {
          "version": "2.3.3",
          "from": "readable-stream@>=2.2.9 <3.0.0",
          "resolved": "https://registry.npmjs.org/readable-stream/-/readable-stream-2.3.3.tgz"
        },
        "string_decoder": {
          "version": "1.0.3",
          "from": "string_decoder@>=1.0.3 <1.1.0",
          "resolved": "https://registry.npmjs.org/string_decoder/-/string_decoder-1.0.3.tgz"
        }
      }
    },
    "sprintf-js": {
      "version": "1.0.3",
      "from": "sprintf-js@>=1.0.2 <1.1.0",
      "resolved": "https://registry.npmjs.org/sprintf-js/-/sprintf-js-1.0.3.tgz"
    },
    "stackframe": {
      "version": "1.0.3",
      "from": "stackframe@>=1.0.3 <2.0.0",
      "resolved": "https://registry.npmjs.org/stackframe/-/stackframe-1.0.3.tgz"
    },
    "statuses": {
      "version": "1.3.1",
      "from": "statuses@>=1.3.1 <1.4.0",
      "resolved": "https://registry.npmjs.org/statuses/-/statuses-1.3.1.tgz"
    },
    "stream-browserify": {
      "version": "2.0.1",
      "from": "stream-browserify@>=2.0.1 <3.0.0",
      "resolved": "https://registry.npmjs.org/stream-browserify/-/stream-browserify-2.0.1.tgz",
      "dependencies": {
        "isarray": {
          "version": "1.0.0",
          "from": "isarray@>=1.0.0 <1.1.0",
          "resolved": "https://registry.npmjs.org/isarray/-/isarray-1.0.0.tgz"
        },
        "readable-stream": {
          "version": "2.3.3",
          "from": "readable-stream@>=2.0.2 <3.0.0",
          "resolved": "https://registry.npmjs.org/readable-stream/-/readable-stream-2.3.3.tgz"
        },
        "string_decoder": {
          "version": "1.0.3",
          "from": "string_decoder@>=1.0.3 <1.1.0",
          "resolved": "https://registry.npmjs.org/string_decoder/-/string_decoder-1.0.3.tgz"
        }
      }
    },
    "stream-http": {
      "version": "2.7.2",
      "from": "stream-http@>=2.3.1 <3.0.0",
      "resolved": "https://registry.npmjs.org/stream-http/-/stream-http-2.7.2.tgz",
      "dependencies": {
        "isarray": {
          "version": "1.0.0",
          "from": "isarray@>=1.0.0 <1.1.0",
          "resolved": "https://registry.npmjs.org/isarray/-/isarray-1.0.0.tgz"
        },
        "readable-stream": {
          "version": "2.3.3",
          "from": "readable-stream@>=2.2.6 <3.0.0",
          "resolved": "https://registry.npmjs.org/readable-stream/-/readable-stream-2.3.3.tgz"
        },
        "string_decoder": {
          "version": "1.0.3",
          "from": "string_decoder@>=1.0.3 <1.1.0",
          "resolved": "https://registry.npmjs.org/string_decoder/-/string_decoder-1.0.3.tgz"
        }
      }
    },
    "strict-uri-encode": {
      "version": "1.1.0",
      "from": "strict-uri-encode@>=1.0.0 <2.0.0",
      "resolved": "https://registry.npmjs.org/strict-uri-encode/-/strict-uri-encode-1.1.0.tgz"
    },
    "string_decoder": {
      "version": "0.10.31",
      "from": "string_decoder@>=0.10.0 <0.11.0",
      "resolved": "https://registry.npmjs.org/string_decoder/-/string_decoder-0.10.31.tgz"
    },
    "string-length": {
      "version": "1.0.1",
      "from": "string-length@>=1.0.1 <2.0.0",
      "resolved": "https://registry.npmjs.org/string-length/-/string-length-1.0.1.tgz"
    },
    "string-width": {
      "version": "1.0.2",
      "from": "string-width@>=1.0.2 <2.0.0",
      "resolved": "https://registry.npmjs.org/string-width/-/string-width-1.0.2.tgz"
    },
    "strip-ansi": {
      "version": "3.0.1",
      "from": "strip-ansi@>=3.0.0 <4.0.0",
      "resolved": "https://registry.npmjs.org/strip-ansi/-/strip-ansi-3.0.1.tgz"
    },
    "strip-bom": {
      "version": "2.0.0",
      "from": "strip-bom@>=2.0.0 <3.0.0",
      "resolved": "https://registry.npmjs.org/strip-bom/-/strip-bom-2.0.0.tgz"
    },
    "strip-eof": {
      "version": "1.0.0",
      "from": "strip-eof@>=1.0.0 <2.0.0",
      "resolved": "https://registry.npmjs.org/strip-eof/-/strip-eof-1.0.0.tgz"
    },
    "strip-indent": {
      "version": "1.0.1",
      "from": "strip-indent@>=1.0.1 <2.0.0",
      "resolved": "https://registry.npmjs.org/strip-indent/-/strip-indent-1.0.1.tgz"
    },
    "style-loader": {
      "version": "0.13.2",
      "from": "style-loader@>=0.13.2 <0.14.0",
      "resolved": "https://registry.npmjs.org/style-loader/-/style-loader-0.13.2.tgz"
    },
    "supports-color": {
      "version": "2.0.0",
      "from": "supports-color@>=2.0.0 <3.0.0",
      "resolved": "https://registry.npmjs.org/supports-color/-/supports-color-2.0.0.tgz"
    },
    "svgo": {
      "version": "0.7.2",
      "from": "svgo@>=0.7.0 <0.8.0",
      "resolved": "https://registry.npmjs.org/svgo/-/svgo-0.7.2.tgz"
    },
    "tapable": {
      "version": "0.2.6",
      "from": "tapable@>=0.2.5 <0.3.0",
      "resolved": "https://registry.npmjs.org/tapable/-/tapable-0.2.6.tgz"
    },
    "thunky": {
      "version": "0.1.0",
      "from": "thunky@>=0.1.0 <0.2.0",
      "resolved": "https://registry.npmjs.org/thunky/-/thunky-0.1.0.tgz"
    },
    "timed-out": {
      "version": "4.0.1",
      "from": "timed-out@>=4.0.0 <5.0.0",
      "resolved": "https://registry.npmjs.org/timed-out/-/timed-out-4.0.1.tgz"
    },
    "timers-browserify": {
      "version": "2.0.2",
      "from": "timers-browserify@>=2.0.2 <3.0.0",
      "resolved": "https://registry.npmjs.org/timers-browserify/-/timers-browserify-2.0.2.tgz"
    },
    "to-arraybuffer": {
      "version": "1.0.1",
      "from": "to-arraybuffer@>=1.0.0 <2.0.0",
      "resolved": "https://registry.npmjs.org/to-arraybuffer/-/to-arraybuffer-1.0.1.tgz"
    },
    "to-fast-properties": {
      "version": "1.0.3",
      "from": "to-fast-properties@>=1.0.1 <2.0.0",
      "resolved": "https://registry.npmjs.org/to-fast-properties/-/to-fast-properties-1.0.3.tgz"
    },
    "trim-newlines": {
      "version": "1.0.0",
      "from": "trim-newlines@>=1.0.0 <2.0.0",
      "resolved": "https://registry.npmjs.org/trim-newlines/-/trim-newlines-1.0.0.tgz"
    },
    "trim-right": {
      "version": "1.0.1",
      "from": "trim-right@>=1.0.1 <2.0.0",
      "resolved": "https://registry.npmjs.org/trim-right/-/trim-right-1.0.1.tgz"
    },
    "tty-browserify": {
      "version": "0.0.0",
      "from": "tty-browserify@0.0.0",
      "resolved": "https://registry.npmjs.org/tty-browserify/-/tty-browserify-0.0.0.tgz"
    },
    "type-is": {
      "version": "1.6.15",
      "from": "type-is@>=1.6.15 <1.7.0",
      "resolved": "https://registry.npmjs.org/type-is/-/type-is-1.6.15.tgz"
    },
    "uglify-js": {
      "version": "2.8.29",
      "from": "uglify-js@>=2.8.27 <3.0.0",
      "resolved": "https://registry.npmjs.org/uglify-js/-/uglify-js-2.8.29.tgz",
      "dependencies": {
        "camelcase": {
          "version": "1.2.1",
          "from": "camelcase@>=1.0.2 <2.0.0",
          "resolved": "https://registry.npmjs.org/camelcase/-/camelcase-1.2.1.tgz"
        },
        "yargs": {
          "version": "3.10.0",
          "from": "yargs@>=3.10.0 <3.11.0",
          "resolved": "https://registry.npmjs.org/yargs/-/yargs-3.10.0.tgz"
        }
      }
    },
    "uglify-to-browserify": {
      "version": "1.0.2",
      "from": "uglify-to-browserify@>=1.0.0 <1.1.0",
      "resolved": "https://registry.npmjs.org/uglify-to-browserify/-/uglify-to-browserify-1.0.2.tgz",
      "optional": true
    },
    "uniq": {
      "version": "1.0.1",
      "from": "uniq@>=1.0.1 <2.0.0",
      "resolved": "https://registry.npmjs.org/uniq/-/uniq-1.0.1.tgz"
    },
    "uniqid": {
      "version": "4.1.1",
      "from": "uniqid@>=4.0.0 <5.0.0",
      "resolved": "https://registry.npmjs.org/uniqid/-/uniqid-4.1.1.tgz"
    },
    "uniqs": {
      "version": "2.0.0",
      "from": "uniqs@>=2.0.0 <3.0.0",
      "resolved": "https://registry.npmjs.org/uniqs/-/uniqs-2.0.0.tgz"
    },
    "unpipe": {
      "version": "1.0.0",
      "from": "unpipe@>=1.0.0 <1.1.0",
      "resolved": "https://registry.npmjs.org/unpipe/-/unpipe-1.0.0.tgz"
    },
    "urix": {
      "version": "0.1.0",
      "from": "urix@>=0.1.0 <0.2.0",
      "resolved": "https://registry.npmjs.org/urix/-/urix-0.1.0.tgz"
    },
    "url": {
      "version": "0.11.0",
      "from": "url@>=0.11.0 <0.12.0",
      "resolved": "https://registry.npmjs.org/url/-/url-0.11.0.tgz",
      "dependencies": {
        "punycode": {
          "version": "1.3.2",
          "from": "punycode@1.3.2",
          "resolved": "https://registry.npmjs.org/punycode/-/punycode-1.3.2.tgz"
        }
      }
    },
    "url-parse": {
      "version": "1.1.9",
      "from": "url-parse@>=1.1.1 <2.0.0",
      "resolved": "https://registry.npmjs.org/url-parse/-/url-parse-1.1.9.tgz",
      "dependencies": {
        "querystringify": {
          "version": "1.0.0",
          "from": "querystringify@>=1.0.0 <1.1.0",
          "resolved": "https://registry.npmjs.org/querystringify/-/querystringify-1.0.0.tgz"
        }
      }
    },
    "url-parse-lax": {
      "version": "1.0.0",
      "from": "url-parse-lax@>=1.0.0 <2.0.0",
      "resolved": "https://registry.npmjs.org/url-parse-lax/-/url-parse-lax-1.0.0.tgz"
    },
    "url-search-params": {
      "version": "0.7.1",
      "from": "url-search-params@latest",
      "resolved": "https://registry.npmjs.org/url-search-params/-/url-search-params-0.7.1.tgz"
    },
    "url-to-options": {
      "version": "1.0.1",
      "from": "url-to-options@>=1.0.1 <2.0.0",
      "resolved": "https://registry.npmjs.org/url-to-options/-/url-to-options-1.0.1.tgz"
    },
    "util": {
      "version": "0.10.3",
      "from": "util@0.10.3",
      "resolved": "https://registry.npmjs.org/util/-/util-0.10.3.tgz",
      "dependencies": {
        "inherits": {
          "version": "2.0.1",
          "from": "inherits@2.0.1",
          "resolved": "https://registry.npmjs.org/inherits/-/inherits-2.0.1.tgz"
        }
      }
    },
    "util-deprecate": {
      "version": "1.0.2",
      "from": "util-deprecate@>=1.0.1 <1.1.0",
      "resolved": "https://registry.npmjs.org/util-deprecate/-/util-deprecate-1.0.2.tgz"
    },
    "utila": {
      "version": "0.4.0",
      "from": "utila@>=0.4.0 <0.5.0",
      "resolved": "https://registry.npmjs.org/utila/-/utila-0.4.0.tgz"
    },
    "utils-merge": {
      "version": "1.0.0",
      "from": "utils-merge@1.0.0",
      "resolved": "https://registry.npmjs.org/utils-merge/-/utils-merge-1.0.0.tgz"
    },
    "uuid": {
      "version": "2.0.3",
      "from": "uuid@>=2.0.2 <3.0.0",
      "resolved": "https://registry.npmjs.org/uuid/-/uuid-2.0.3.tgz"
    },
    "validate-npm-package-license": {
      "version": "3.0.1",
      "from": "validate-npm-package-license@>=3.0.1 <4.0.0",
      "resolved": "https://registry.npmjs.org/validate-npm-package-license/-/validate-npm-package-license-3.0.1.tgz"
    },
    "vary": {
      "version": "1.1.1",
      "from": "vary@>=1.1.1 <1.2.0",
      "resolved": "https://registry.npmjs.org/vary/-/vary-1.1.1.tgz"
    },
    "vendors": {
      "version": "1.0.1",
      "from": "vendors@>=1.0.0 <2.0.0",
      "resolved": "https://registry.npmjs.org/vendors/-/vendors-1.0.1.tgz"
    },
    "vm-browserify": {
      "version": "0.0.4",
      "from": "vm-browserify@0.0.4",
      "resolved": "https://registry.npmjs.org/vm-browserify/-/vm-browserify-0.0.4.tgz"
    },
    "vue": {
      "version": "2.4.2",
      "from": "vue@latest",
      "resolved": "https://registry.npmjs.org/vue/-/vue-2.4.2.tgz"
    },
    "vue-hot-reload-api": {
      "version": "2.1.0",
      "from": "vue-hot-reload-api@>=2.1.0 <3.0.0",
      "resolved": "https://registry.npmjs.org/vue-hot-reload-api/-/vue-hot-reload-api-2.1.0.tgz"
    },
    "vue-loader": {
      "version": "13.0.2",
      "from": "vue-loader@latest",
      "resolved": "https://registry.npmjs.org/vue-loader/-/vue-loader-13.0.2.tgz",
      "dependencies": {
        "ansi-styles": {
          "version": "3.2.0",
          "from": "ansi-styles@>=3.1.0 <4.0.0",
          "resolved": "https://registry.npmjs.org/ansi-styles/-/ansi-styles-3.2.0.tgz"
        },
        "chalk": {
          "version": "2.0.1",
          "from": "chalk@>=2.0.1 <3.0.0",
          "resolved": "https://registry.npmjs.org/chalk/-/chalk-2.0.1.tgz"
        },
        "has-flag": {
          "version": "2.0.0",
          "from": "has-flag@>=2.0.0 <3.0.0",
          "resolved": "https://registry.npmjs.org/has-flag/-/has-flag-2.0.0.tgz"
        },
        "postcss": {
          "version": "6.0.8",
          "from": "postcss@>=6.0.1 <7.0.0",
          "resolved": "https://registry.npmjs.org/postcss/-/postcss-6.0.8.tgz"
        },
        "supports-color": {
          "version": "4.2.1",
          "from": "supports-color@>=4.2.0 <5.0.0",
          "resolved": "https://registry.npmjs.org/supports-color/-/supports-color-4.2.1.tgz"
        }
      }
    },
    "vue-notifyjs": {
      "version": "0.1.7",
      "from": "vue-notifyjs@latest",
      "resolved": "https://registry.npmjs.org/vue-notifyjs/-/vue-notifyjs-0.1.7.tgz"
    },
    "vue-resource": {
      "version": "1.3.4",
      "from": "vue-resource@latest",
      "resolved": "https://registry.npmjs.org/vue-resource/-/vue-resource-1.3.4.tgz"
    },
    "vue-router": {
      "version": "2.7.0",
      "from": "vue-router@latest",
      "resolved": "https://registry.npmjs.org/vue-router/-/vue-router-2.7.0.tgz"
    },
    "vue-style-loader": {
      "version": "3.0.1",
      "from": "vue-style-loader@>=3.0.0 <4.0.0",
      "resolved": "https://registry.npmjs.org/vue-style-loader/-/vue-style-loader-3.0.1.tgz"
    },
    "vue-template-compiler": {
      "version": "2.4.2",
      "from": "vue-template-compiler@latest",
      "resolved": "https://registry.npmjs.org/vue-template-compiler/-/vue-template-compiler-2.4.2.tgz"
    },
    "vue-template-es2015-compiler": {
      "version": "1.5.3",
      "from": "vue-template-es2015-compiler@>=1.5.3 <2.0.0",
      "resolved": "https://registry.npmjs.org/vue-template-es2015-compiler/-/vue-template-es2015-compiler-1.5.3.tgz"
    },
    "watchpack": {
      "version": "1.4.0",
      "from": "watchpack@>=1.3.1 <2.0.0",
      "resolved": "https://registry.npmjs.org/watchpack/-/watchpack-1.4.0.tgz"
    },
    "wbuf": {
      "version": "1.7.2",
      "from": "wbuf@>=1.7.2 <2.0.0",
      "resolved": "https://registry.npmjs.org/wbuf/-/wbuf-1.7.2.tgz"
    },
    "webpack": {
      "version": "2.7.0",
      "from": "webpack@>=2.2.0 <3.0.0",
      "resolved": "https://registry.npmjs.org/webpack/-/webpack-2.7.0.tgz",
      "dependencies": {
        "ajv": {
          "version": "4.11.8",
          "from": "ajv@>=4.7.0 <5.0.0",
          "resolved": "https://registry.npmjs.org/ajv/-/ajv-4.11.8.tgz"
        },
        "camelcase": {
          "version": "3.0.0",
          "from": "camelcase@>=3.0.0 <4.0.0",
          "resolved": "https://registry.npmjs.org/camelcase/-/camelcase-3.0.0.tgz"
        },
        "cliui": {
          "version": "3.2.0",
          "from": "cliui@>=3.2.0 <4.0.0",
          "resolved": "https://registry.npmjs.org/cliui/-/cliui-3.2.0.tgz"
        },
        "loader-utils": {
          "version": "0.2.17",
          "from": "loader-utils@>=0.2.16 <0.3.0",
          "resolved": "https://registry.npmjs.org/loader-utils/-/loader-utils-0.2.17.tgz"
        },
        "supports-color": {
          "version": "3.2.3",
          "from": "supports-color@>=3.1.0 <4.0.0",
          "resolved": "https://registry.npmjs.org/supports-color/-/supports-color-3.2.3.tgz"
        },
        "yargs": {
          "version": "6.6.0",
          "from": "yargs@>=6.0.0 <7.0.0",
          "resolved": "https://registry.npmjs.org/yargs/-/yargs-6.6.0.tgz"
        }
      }
    },
    "webpack-chunk-hash": {
      "version": "0.4.0",
      "from": "webpack-chunk-hash@>=0.4.0 <0.5.0",
      "resolved": "https://registry.npmjs.org/webpack-chunk-hash/-/webpack-chunk-hash-0.4.0.tgz"
    },
    "webpack-dev-middleware": {
      "version": "1.11.0",
      "from": "webpack-dev-middleware@>=1.11.0 <2.0.0",
      "resolved": "https://registry.npmjs.org/webpack-dev-middleware/-/webpack-dev-middleware-1.11.0.tgz"
    },
    "webpack-dev-server": {
      "version": "2.5.1",
      "from": "webpack-dev-server@>=2.4.5 <3.0.0",
      "resolved": "https://registry.npmjs.org/webpack-dev-server/-/webpack-dev-server-2.5.1.tgz",
      "dependencies": {
        "camelcase": {
          "version": "3.0.0",
          "from": "camelcase@>=3.0.0 <4.0.0",
          "resolved": "https://registry.npmjs.org/camelcase/-/camelcase-3.0.0.tgz"
        },
        "cliui": {
          "version": "3.2.0",
          "from": "cliui@>=3.2.0 <4.0.0",
          "resolved": "https://registry.npmjs.org/cliui/-/cliui-3.2.0.tgz"
        },
        "supports-color": {
          "version": "3.2.3",
          "from": "supports-color@>=3.1.1 <4.0.0",
          "resolved": "https://registry.npmjs.org/supports-color/-/supports-color-3.2.3.tgz"
        },
        "yargs": {
          "version": "6.6.0",
          "from": "yargs@>=6.0.0 <7.0.0",
          "resolved": "https://registry.npmjs.org/yargs/-/yargs-6.6.0.tgz"
        }
      }
    },
    "webpack-sources": {
      "version": "1.0.1",
      "from": "webpack-sources@>=1.0.1 <2.0.0",
      "resolved": "https://registry.npmjs.org/webpack-sources/-/webpack-sources-1.0.1.tgz",
      "dependencies": {
        "source-list-map": {
          "version": "2.0.0",
          "from": "source-list-map@>=2.0.0 <3.0.0",
          "resolved": "https://registry.npmjs.org/source-list-map/-/source-list-map-2.0.0.tgz"
        }
      }
    },
    "websocket-driver": {
      "version": "0.6.5",
      "from": "websocket-driver@>=0.5.1",
      "resolved": "https://registry.npmjs.org/websocket-driver/-/websocket-driver-0.6.5.tgz"
    },
    "websocket-extensions": {
      "version": "0.1.1",
      "from": "websocket-extensions@>=0.1.1",
      "resolved": "https://registry.npmjs.org/websocket-extensions/-/websocket-extensions-0.1.1.tgz"
    },
    "whet.extend": {
      "version": "0.9.9",
      "from": "whet.extend@>=0.9.9 <0.10.0",
      "resolved": "https://registry.npmjs.org/whet.extend/-/whet.extend-0.9.9.tgz"
    },
    "which": {
      "version": "1.2.14",
      "from": "which@>=1.2.9 <2.0.0",
      "resolved": "https://registry.npmjs.org/which/-/which-1.2.14.tgz"
    },
    "which-module": {
      "version": "1.0.0",
      "from": "which-module@>=1.0.0 <2.0.0",
      "resolved": "https://registry.npmjs.org/which-module/-/which-module-1.0.0.tgz"
    },
    "window-size": {
      "version": "0.1.0",
      "from": "window-size@0.1.0",
      "resolved": "https://registry.npmjs.org/window-size/-/window-size-0.1.0.tgz"
    },
    "wordwrap": {
      "version": "0.0.2",
      "from": "wordwrap@0.0.2",
      "resolved": "https://registry.npmjs.org/wordwrap/-/wordwrap-0.0.2.tgz"
    },
    "wrap-ansi": {
      "version": "2.1.0",
      "from": "wrap-ansi@>=2.0.0 <3.0.0",
      "resolved": "https://registry.npmjs.org/wrap-ansi/-/wrap-ansi-2.1.0.tgz"
    },
    "wrappy": {
      "version": "1.0.2",
      "from": "wrappy@>=1.0.0 <2.0.0",
      "resolved": "https://registry.npmjs.org/wrappy/-/wrappy-1.0.2.tgz"
    },
    "xtend": {
      "version": "4.0.1",
      "from": "xtend@>=4.0.0 <5.0.0",
      "resolved": "https://registry.npmjs.org/xtend/-/xtend-4.0.1.tgz"
    },
    "y18n": {
      "version": "3.2.1",
      "from": "y18n@>=3.2.1 <4.0.0",
      "resolved": "https://registry.npmjs.org/y18n/-/y18n-3.2.1.tgz"
    },
    "yallist": {
      "version": "2.1.2",
      "from": "yallist@>=2.1.2 <3.0.0",
      "resolved": "https://registry.npmjs.org/yallist/-/yallist-2.1.2.tgz"
    },
    "yargs": {
      "version": "8.0.2",
      "from": "yargs@>=8.0.1 <9.0.0",
      "resolved": "https://registry.npmjs.org/yargs/-/yargs-8.0.2.tgz",
      "dependencies": {
        "ansi-regex": {
          "version": "3.0.0",
          "from": "ansi-regex@>=3.0.0 <4.0.0",
          "resolved": "https://registry.npmjs.org/ansi-regex/-/ansi-regex-3.0.0.tgz"
        },
        "cliui": {
          "version": "3.2.0",
          "from": "cliui@>=3.2.0 <4.0.0",
          "resolved": "https://registry.npmjs.org/cliui/-/cliui-3.2.0.tgz",
          "dependencies": {
            "string-width": {
              "version": "1.0.2",
              "from": "string-width@^1.0.1",
              "resolved": "https://registry.npmjs.org/string-width/-/string-width-1.0.2.tgz"
            }
          }
        },
        "load-json-file": {
          "version": "2.0.0",
          "from": "load-json-file@>=2.0.0 <3.0.0",
          "resolved": "https://registry.npmjs.org/load-json-file/-/load-json-file-2.0.0.tgz"
        },
        "os-locale": {
          "version": "2.0.0",
          "from": "os-locale@>=2.0.0 <3.0.0",
          "resolved": "https://registry.npmjs.org/os-locale/-/os-locale-2.0.0.tgz"
        },
        "path-type": {
          "version": "2.0.0",
          "from": "path-type@>=2.0.0 <3.0.0",
          "resolved": "https://registry.npmjs.org/path-type/-/path-type-2.0.0.tgz"
        },
        "read-pkg": {
          "version": "2.0.0",
          "from": "read-pkg@>=2.0.0 <3.0.0",
          "resolved": "https://registry.npmjs.org/read-pkg/-/read-pkg-2.0.0.tgz"
        },
        "read-pkg-up": {
          "version": "2.0.0",
          "from": "read-pkg-up@>=2.0.0 <3.0.0",
          "resolved": "https://registry.npmjs.org/read-pkg-up/-/read-pkg-up-2.0.0.tgz"
        },
        "string-width": {
          "version": "2.1.0",
          "from": "string-width@>=2.0.0 <3.0.0",
          "resolved": "https://registry.npmjs.org/string-width/-/string-width-2.1.0.tgz",
          "dependencies": {
            "is-fullwidth-code-point": {
              "version": "2.0.0",
              "from": "is-fullwidth-code-point@>=2.0.0 <3.0.0",
              "resolved": "https://registry.npmjs.org/is-fullwidth-code-point/-/is-fullwidth-code-point-2.0.0.tgz"
            },
            "strip-ansi": {
              "version": "4.0.0",
              "from": "strip-ansi@>=4.0.0 <5.0.0",
              "resolved": "https://registry.npmjs.org/strip-ansi/-/strip-ansi-4.0.0.tgz"
            }
          }
        },
        "strip-bom": {
          "version": "3.0.0",
          "from": "strip-bom@>=3.0.0 <4.0.0",
          "resolved": "https://registry.npmjs.org/strip-bom/-/strip-bom-3.0.0.tgz"
        },
        "which-module": {
          "version": "2.0.0",
          "from": "which-module@>=2.0.0 <3.0.0",
          "resolved": "https://registry.npmjs.org/which-module/-/which-module-2.0.0.tgz"
        },
        "yargs-parser": {
          "version": "7.0.0",
          "from": "yargs-parser@>=7.0.0 <8.0.0",
          "resolved": "https://registry.npmjs.org/yargs-parser/-/yargs-parser-7.0.0.tgz"
        }
      }
    },
    "yargs-parser": {
      "version": "4.2.1",
      "from": "yargs-parser@>=4.2.0 <5.0.0",
      "resolved": "https://registry.npmjs.org/yargs-parser/-/yargs-parser-4.2.1.tgz",
      "dependencies": {
        "camelcase": {
          "version": "3.0.0",
          "from": "camelcase@>=3.0.0 <4.0.0",
          "resolved": "https://registry.npmjs.org/camelcase/-/camelcase-3.0.0.tgz"
        }
      }
    }
  }
}
```

## File: `package.json`
```json
{
  "name": "wishlist",
  "version": "1.0.0",
  "description": "Wishlist DDD app",
  "main": "index.js",
  "directories": {
    "test": "tests"
  },
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "keywords": [
    "wishlist",
    "ddd",
    "symfony"
  ],
  "author": "Jan Iwanow <iwanow.jan@gmail.com> (http://janiwanow.com)",
  "license": "MIT",
  "dependencies": {
    "@symfony/webpack-encore": "^0.10.0",
    "url-search-params": "^0.7.1",
    "vue": "^2.4.2",
    "vue-loader": "^13.0.2",
    "vue-notifyjs": "^0.1.7",
    "vue-resource": "^1.3.4",
    "vue-router": "^2.7.0",
    "vue-template-compiler": "^2.4.2"
  },
  "devDependencies": {
    "node-sass": "^4.5.3",
    "sass-loader": "^6.0.6"
  }
}
```

## File: `phpunit.xml.dist`
```
<?xml version="1.0" encoding="UTF-8"?>

<!-- https://phpunit.de/manual/current/en/appendixes.configuration.html -->
<phpunit xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:noNamespaceSchemaLocation="http://schema.phpunit.de/4.8/phpunit.xsd"
         backupGlobals="false"
         colors="true"
         bootstrap="vendor/autoload.php"
>
    <php>
        <ini name="error_reporting" value="-1" />
        <server name="KERNEL_CLASS" value="AppKernel" />
    </php>

    <testsuites>
        <testsuite name="Project Test Suite">
            <directory>tests</directory>
        </testsuite>
    </testsuites>

    <filter>
        <whitelist>
            <directory>src</directory>
            <exclude>
                <directory>src/*Bundle/Resources</directory>
                <directory>src/*/*Bundle/Resources</directory>
                <directory>src/*/Bundle/*Bundle/Resources</directory>
            </exclude>
        </whitelist>
    </filter>
</phpunit>
```

## File: `webpack.config.js`
```javascript
const Encore = require('@symfony/webpack-encore');

Encore
    .setOutputPath('web/assets/')
    .setPublicPath('/assets')
    .cleanupOutputBeforeBuild()
    .addEntry('app', './app/Resources/assets/js/app.js')
    .addStyleEntry('styles', './app/Resources/assets/scss/app.scss')
    .enableSassLoader()
    .enableVueLoader()
    .enableSourceMaps(!Encore.isProduction())
;

module.exports = Encore.getWebpackConfig();
```

## File: `app/.htaccess`
```
<IfModule mod_authz_core.c>
    Require all denied
</IfModule>
<IfModule !mod_authz_core.c>
    Order deny,allow
    Deny from all
</IfModule>
```

## File: `app/AppCache.php`
```php
<?php

use Symfony\Bundle\FrameworkBundle\HttpCache\HttpCache;

class AppCache extends HttpCache
{
}
```

## File: `app/AppKernel.php`
```php
<?php

use Symfony\Component\HttpKernel\Kernel;
use Symfony\Component\Config\Loader\LoaderInterface;

class AppKernel extends Kernel
{
    public function registerBundles()
    {
        $bundles = [
            new Symfony\Bundle\FrameworkBundle\FrameworkBundle(),
            new Symfony\Bundle\SecurityBundle\SecurityBundle(),
            new Symfony\Bundle\TwigBundle\TwigBundle(),
            new Symfony\Bundle\MonologBundle\MonologBundle(),
            new Symfony\Bundle\SwiftmailerBundle\SwiftmailerBundle(),
            new Doctrine\Bundle\DoctrineBundle\DoctrineBundle(),
            new Sensio\Bundle\FrameworkExtraBundle\SensioFrameworkExtraBundle(),
            new FOS\JsRoutingBundle\FOSJsRoutingBundle(),
        ];

        $env = $this->getEnvironment();

        if (in_array($env, ['dev', 'test'], true)) {
            $bundles[] = new Symfony\Bundle\DebugBundle\DebugBundle();
            $bundles[] = new Symfony\Bundle\WebProfilerBundle\WebProfilerBundle();
            $bundles[] = new Sensio\Bundle\DistributionBundle\SensioDistributionBundle();

            if ('dev' === $env) {
                $bundles[] = new Sensio\Bundle\GeneratorBundle\SensioGeneratorBundle();
                $bundles[] = new Symfony\Bundle\WebServerBundle\WebServerBundle();
            }

            $bundles[] = new Doctrine\Bundle\FixturesBundle\DoctrineFixturesBundle();
            $bundles[] = new Liip\FunctionalTestBundle\LiipFunctionalTestBundle();
        }

        return $bundles;
    }

    public function getRootDir()
    {
        return __DIR__;
    }

    public function getCacheDir()
    {
        return dirname(__DIR__).'/var/cache/'.$this->getEnvironment();
    }

    public function getLogDir()
    {
        return dirname(__DIR__).'/var/logs';
    }

    public function registerContainerConfiguration(LoaderInterface $loader)
    {
        $loader->load($this->getRootDir().'/config/config_'.$this->getEnvironment().'.yml');
    }
}
```

## File: `app/Resources/assets/js/app.js`
```javascript
import Vue from 'vue';
import VueResource from 'vue-resource';
import VueRouter from 'vue-router';
import Notify from 'vue-notifyjs';
import Wishlist from './wishlist';

Vue.use(VueResource);
Vue.use(VueRouter);
Vue.use(Notify);

window.addEventListener('load', function () {
    const routes = [
        {
            path: Routing.generate('wishlist.index'),
            component: Wishlist
        }
    ];

    const router = new VueRouter({
        routes,
        mode: 'history',
        linkActiveClass: 'is-active',
        linkExactActiveClass: 'is-current'
    });

    new Vue({
        router,
        el: '#wishlist'
    });
});
```

## File: `app/Resources/assets/js/new-deposit-form.js`
```javascript
import Vue from 'vue';

export default {
    template:
    `
    <tr>
        <td>
            <div class="new-deposit-form table__padded">
                <input
                    class="new-deposit-form__value"
                    type="number"
                    :placeholder="lang.enterNewDeposit"
                    required
                    @input="changeValue">
                <button
                    class="new-deposit-form__submit button button--primary"
                    type="button"
                    :disabled="shouldButtonBeDisabled"
                    @click="makeDeposit">{{ lang.deposit }}</button>
            </div>
        </td>
    </tr>
    `,
    props: [
        'wish'
    ],
    data() {
        return {
            lang: window.translations,
            amount: null,
            shouldButtonBeDisabled: false
        }
    },
    methods: {
        changeValue(event) {
            const amount = parseInt(event.target.value);

            this.amount = isNaN(amount) ? null : amount;
            this.shouldButtonBeDisabled = '' === event.target.value || 0 >= this.amount;
        },
        makeDeposit() {
            const url = Routing.generate('wishlist.wish.deposit', {
                wishId: this.wish.id
            });

            const payload = new FormData();
            payload.append('amount', this.amount);

            Vue.http.post(url, payload)
                .then(response => response.body)
                .then(response => {
                    let deposit = response.deposit;

                    this.wish.deposits.unshift(deposit);
                    this.wish.fund = parseInt(this.wish.fund) + parseInt(deposit.amount);
                })
                .catch(response => {
                    this.$notify({
                        type: 'danger',
                        message: ('violations' in response.body
                            ? response.body.violations.amount
                            : 'Internal Server Error'
                        )
                    });
                });
        }
    }
};
```

## File: `app/Resources/assets/js/pagination.js`
```javascript
export default {
    template:
        `
        <div class="table__pagination pagination">
            <router-link :to="prevPage" class="pagination__link pagination__link--prev">
                <svg class="pagination__icon" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path transform="scale(-1,1) translate(-24,0)" d="M13.025 1l-2.847 2.828 6.176 6.176h-16.354v3.992h16.354l-6.176 6.176 2.847 2.828 10.975-11z"></path></svg>
            </router-link>
            {{ pagination.startIndex }}-{{ pagination.endIndex }}
            {{ lang.of }}
            {{ pagination.total }}
            {{ lang.total }}
            <router-link :to="nextPage" class="pagination__link pagination__link--next">
                <svg class="pagination__icon" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path d="M13.025 1l-2.847 2.828 6.176 6.176h-16.354v3.992h16.354l-6.176 6.176 2.847 2.828 10.975-11z"></path></svg>
            </router-link>
        </div>
        `,
    props: [
        'route',
        'pagination',
        'lang',
    ],
    computed: {
        prevPage() {
            const page = this.pagination.page > 1
                ? this.pagination.page - 1
                : this.pagination.page;

            return Routing.generate(this.route, { page });
        },
        nextPage() {
            return Routing.generate(this.route, { page: this.pagination.page + 1 });
        }
    }
};
```

## File: `app/Resources/assets/js/wish-deposit.js`
```javascript
import Vue from 'vue';

export default {
    template:
        `
        <tr>
            <td>{{ deposit.amount }}</td>
            <td class="wishlist__muted">{{ deposit.currency }}</td>
            <td class="wishlist__muted">{{ deposit.createdAt }}</td>
            <td class="wish-deposits__withdraw">
                <button
                    class="wish-deposits__withdraw-button button button--danger"
                    type="button"
                    @click="withdraw">
                    {{ lang.withdraw }}
                </button>
            </td>
        </tr>
        `,
    props: [
        'wish',
        'deposit'
    ],
    data() {
        return {
            lang: window.translations,
        }
    },
    methods: {
        withdraw() {
            const url = Routing.generate('wishlist.wish.withdraw', {
                wishId: this.wish.id,
                depositId: this.deposit.id
            });

            Vue.http.delete(url)
                .then(response => {
                    this.wish.deposits = this.wish.deposits.filter(deposit => {
                        return deposit.id !== this.deposit.id;
                    });

                    this.wish.fund = parseInt(this.wish.fund) - parseInt(this.deposit.amount);
                })
                .catch(response => {
                    this.$notify({
                        type: 'danger',
                        message: ('violations' in response.body
                                ? response.body.violations.depositId
                                : 'Internal Server Error'
                        )
                    });
                });
        }
    }
};
```

## File: `app/Resources/assets/js/wish-deposits.js`
```javascript
import Deposit from './wish-deposit';
import NewDepositForm from './new-deposit-form';

export default {
    template:
        `
        <div class="wish-deposits" :class="{ 'is-active': isActive }">
            <table class="wish-deposits__table table">
                <caption class="table__caption">
                    <div class="table__caption-wrapper">
                        <div class="table__caption-text">{{ lang.depositsOf }} ‘{{ wish.name }}’</div>
                        <svg @click="close" class="table__close" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path d="M24 20.188l-8.315-8.209 8.2-8.282-3.697-3.697-8.212 8.318-8.31-8.203-3.666 3.666 8.321 8.24-8.206 8.313 3.666 3.666 8.237-8.318 8.285 8.203z"/></svg>
                    </div>
                </caption>
                <tbody class="wish-deposits__rows">
                <tr is="new-deposit-form" :wish="wish" />
                <tr is="deposit"
                    v-for="deposit in wish.deposits"
                    :lang="lang"
                    :wish="wish"
                    :deposit="deposit"
                    :key="deposit.id" />
                </tbody>
            </table>
        </div>
        `,
    components: {
        deposit: Deposit,
        newDepositForm: NewDepositForm
    },
    props: [
        'wish',
        'isActive'
    ],
    data() {
        return {
            lang: window.translations
        }
    },
    methods: {
        close() {
            this.$emit('closed');
        }
    }
};
```

## File: `app/Resources/assets/js/wishlist-item.js`
```javascript
export default {
    template:
        `
        <tr :class="{ 'wishlist__wish js-wish': true, 'is-unpublished': !wish.isPublished }"
            :data-id="wish.id">
            <td class="wishlist__muted">{{ wish.createdAt }}</td>
            <td class="wishlist__name" @click="choose(wish)">{{ wish.name }}</td>
            <td>{{ wish.fund }} {{ lang.of }} {{ wish.price }}</td>
            <td class="wishlist__muted">{{ wish.currency }}</td>
            <td>
                <button
                    type="button"
                    class="wishlist__publish-button"
                    data-url="#"
                    @click="togglePublishedStatus(wish, $event)">
                    {{ wish.isPublished ? lang.unpublish : lang.publish }}
                </button>
            </td>
        </tr>
        `,
    props: [
        'wish',
        'lang',
    ],
    methods: {
        choose(wish) {
            this.$emit('chosen', wish);
        },
        togglePublishedStatus(wish) {
            wish.isPublished = !wish.isPublished;

            this.$emit(
                wish.isPublished ? 'published' : 'unpublished',
                wish
            );
        }
    }
};
```

## File: `app/Resources/assets/js/wishlist.js`
```javascript
import Vue from 'vue';
import Pagination from './pagination';
import WishlistItem from './wishlist-item';
import Deposits from './wish-deposits';

export default {
    template:
        `
        <div>
            <table class="table">
                <caption class="table__caption">
                    <div class="table__caption-wrapper">
                        <div class="table__caption-text">{{ lang.title }}</div>
                        <pagination
                            route="wishlist.index"
                            :lang="lang"
                            :pagination="pagination" />
                    </div>
                </caption>
                <tbody>
                <tr is="wishlist-item"
                    v-for="wish in wishlist"
                    :lang="lang"
                    :wish="wish"
                    :key="wish.id"
                    @published="publish"
                    @unpublished="unpublish"
                    @chosen="showDeposits"></tr>
                </tbody>
            </table>
            <deposits
                :isActive="shouldShowDeposits"
                :wish="chosenWish"
                @closed="hideDeposits" />
        </div>
        `,
    components: {
        pagination: Pagination,
        wishlistItem: WishlistItem,
        deposits: Deposits
    },
    data() {
        return {
            wishlist: [],
            pagination: {},
            lang: window.translations,
            shouldShowDeposits: false,
            chosenWish: {},
        }
    },
    beforeRouteEnter(to, from, next) {
        Vue.http.get(Routing.generate('wishlist.index', {
            page: to.query.page || 1
        }))
            .then(response => response.body)
            .then(response => {
                next(vm => {
                    vm.wishlist = response.wishes;
                    vm.pagination = response.pagination;
                    vm.$emit('activated');
                });
            });
    },
    beforeRouteUpdate (to, from, next) {
        Vue.http.get(Routing.generate('wishlist.index', {
            page: to.query.page || 1
        }))
            .then(response => response.body)
            .then(response => {
                this.wishlist = response.wishes;
                this.pagination = response.pagination;

                next();
            });
    },
    methods: {
        publish(wish) {
            this.$http.put(Routing.generate('wishlist.wish.publish', {
                wishId: wish.id
            }))
                .catch(e => {
                    wish.isPublished = false;
                });
        },
        unpublish(wish) {
            this.$http.put(Routing.generate('wishlist.wish.unpublish', {
                wishId: wish.id
            }))
                .catch(e => {
                    wish.isPublished = true;
                });
        },
        showDeposits(wish) {
            this.shouldShowDeposits = true;
            this.chosenWish = wish;
        },
        hideDeposits() {
            this.shouldShowDeposits = false;

            setTimeout(() => {
                this.chosenWish = {};
            }, 350);
        }
    }
};
```

## File: `app/Resources/assets/scss/app.scss`
```scss
@import "common";
@import "components/button";
@import "components/notifications";
@import "blocks/table";
@import "blocks/pagination";
@import "blocks/wishlist";
@import "blocks/wish-deposits";
@import "blocks/new-deposit-form";
```

## File: `app/Resources/assets/scss/common.scss`
```scss
* {
    margin: 0;
    padding: 0;

    *,
    *:before,
    *:after {
        box-sizing: border-box;
    }
}

html {
    font-size: 20px;
}

body,
input,
textarea,
select,
button {
    font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
}

body {
    font-size: 1rem;
    line-height: 1.5;
    font-weight: 300;
}

table {
    border-collapse: collapse;
}

input,
textarea,
select,
button {
    padding: .25rem;
    font-size: .875rem;
    border: 1px solid #dfdfdf;
    border-radius: 3px;
    outline: none;

    &[disabled] {
        opacity: .5;
        cursor: default;
    }
}

button {
    padding-left: 1rem;
    padding-right: 1rem;
}

select,
button {
    cursor: pointer;
}
```

## File: `app/Resources/assets/scss/blocks/new-deposit-form.scss`
```scss
.new-deposit-form {
    display: flex;
    justify-content: center;

    &__value {
        margin-right: .5rem;
    }

    &__submit {
        //
    }
}
```

## File: `app/Resources/assets/scss/blocks/pagination.scss`
```scss
.pagination {
    &__link {
        display: inline-block;
        position: relative;
        top: .35rem;
        width: 24px;
        height: 24px;
        font-family: monospace;
        font-size: 1.25rem;
        line-height: 0;
        text-decoration: none;
        color: #8ac249;
        text-shadow: 0 1px 0 #5a8c21;
        cursor: pointer;

        &--prev {
            margin-right: 1rem;
        }

        &--next {
            margin-left: 1rem;
        }

        &.is-current {
            display: none;
        }
    }

    &__icon {
        margin-left: -.5rem;
    }
}
```

## File: `app/Resources/assets/scss/blocks/table.scss`
```scss
.table {
    tr {
        &:not(:last-child) {
            border-bottom: 1px solid #eee;
        }

        &:hover {
            background: rgba(69,183,235, .1);
            border-bottom-color: rgba(69,183,235, .15);
        }
    }

    td {
        padding: .125rem .5rem;
    }

    &__caption {
        margin-bottom: .25rem;
        text-align: left;
        text-indent: .45rem;
        font-variant: small-caps;
        text-transform: lowercase;
        letter-spacing: .125rem;
        font-weight: 500;
    }

    &__caption-wrapper {
        display: flex;
        align-items: flex-end;
        justify-content: space-between;
    }

    &__pagination {
        position: relative;
        top: -.125rem;
        font-size: .65rem;
        color: #777;
    }

    &__close {
        position: absolute;
        top: 1.45rem;
        right: 1rem;
        width: 16px;
        height: 16px;
        cursor: pointer;
    }

    &__padded {
        padding: 1rem;
    }

    &__button {
        display: block;
        margin: 0 auto;
    }
}
```

## File: `app/Resources/assets/scss/blocks/wish-deposits.scss`
```scss
.wish-deposits {
    position: absolute;
    top: 0;
    z-index: -1;
    width: 100%;
    min-height: 100%;
    padding: 1rem;
    background: #fff;
    box-shadow: 0 0 10px #eee;
    border-radius: 4px;
    opacity: 0;
    transition: z-index .35s, opacity .35s;

    &.is-active {
        z-index: 5;
        opacity: 1;
    }

    &__table {
        width: 100%;
    }

    &__rows {
        display: block;
        height: 310px;
        overflow: auto;
    }

    &__withdraw {
        text-align: right;
    }

    &__withdraw-button {
        position: relative;
        top: -.125rem;
        font-size: .65rem;
    }

    tr {
        display: flex;
        justify-content: space-between;
        align-items: center;
    }

    td {
        display: block;
        width: 100%;

        &:nth-child(2) {
            flex-grow: 1;
        }
    }
}
```

## File: `app/Resources/assets/scss/blocks/wishlist.scss`
```scss
.wishlist {
    position: relative;
    max-width: 35rem;
    margin: 3rem auto;

    &__muted {
        font-size: .75rem;
        color: #777;
    }

    &__name {
        min-width: 5rem;
        cursor: pointer;
    }

    &__wish {
        &.is-unpublished {
            color: #bbb;
        }
    }

    &__publish-button {
        padding: 0 .25rem;
        font-size: .75rem;
        font-family: inherit;
        color: #333;
        border: 0;
        border-radius: 2px;
        background: #ffd121;
        cursor: pointer;
        outline: none;
    }

    &__wish--unpublished &__publish-button {
        color: #fff;
        background: #00a5f2;
    }
}
```

## File: `app/Resources/assets/scss/components/button.scss`
```scss
.button {
    border: 0;

    &--primary {
        color: #fff;
        background-color: #68c0e4;
    }

    &--danger {
        color: #fff;
        background-color: #ef4423;
    }
}
```

## File: `app/Resources/assets/scss/components/notifications.scss`
```scss
.notifications {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;

    .alert {
        padding: .25rem;
        text-align: center;
    }

    .alert-danger {
        color: #fff;
        background-color: #ff5d21;
    }

    .close {
        display: none;
    }
}
```

## File: `app/Resources/translations/messages.en.yml`
```yaml
wishlist:
    search_form:
        input_placeholder: Wish name here
        button_label: Search
    table:
        title: Wishlist
        of: of
        total: total
        publish: Publish
        unpublish: Unpublish
        deposits_of: Deposits of
        enter_new_deposit: Enter new deposit
        deposit: Deposit
        withdraw: Withdraw
```

## File: `app/Resources/views/base.html.twig`
```
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8" />
        <title>{% block title %}Welcome!{% endblock %} • Wishlist</title>
        <link rel="stylesheet" href="{{ asset('assets/styles.css') }}">
        <link rel="icon" type="image/x-icon" href="{{ asset('favicon.ico') }}" />
    </head>
    <body>
        <div class="layout">
            {% block body %}{% endblock %}
        </div>
        <script>
            window.translations = {
                title: '{{ 'wishlist.table.title'|trans }}',
                publish: '{{ 'wishlist.table.publish'|trans }}',
                unpublish: '{{ 'wishlist.table.unpublish'|trans }}',
                of: '{{ 'wishlist.table.of'|trans }}',
                depositsOf: '{{ 'wishlist.table.deposits_of'|trans }}',
                enterNewDeposit: '{{ 'wishlist.table.enter_new_deposit'|trans }}',
                deposit: '{{ 'wishlist.table.deposit'|trans }}',
                withdraw: '{{ 'wishlist.table.withdraw'|trans }}'
            };
        </script>
        <script src="{{ asset('assets/app.js') }}"></script>
        <script src="{{ asset('bundles/fosjsrouting/js/router.js') }}"></script>
        <script src="{{ path('fos_js_routing_js', { callback: 'fos.Router.setData' }) }}"></script>
    </body>
</html>
```

## File: `app/Resources/views/wishlist/index.html.twig`
```
{% extends '::base.html.twig' %}

{% block body %}
    <div id="wishlist"
         class="wishlist js-wishlist">
        <div>
            <notifications />
        </div>
        <router-view />
    </div>
{% endblock %}
```

## File: `app/config/config.yml`
```yaml
imports:
    - { resource: parameters.yml }
    - { resource: parameters_permanent.yml }
    - { resource: security.yml }
    - { resource: services.yml }

# Put parameters here that don't need to change on each machine where the app is deployed
# https://symfony.com/doc/current/best_practices/configuration.html#application-related-configuration
parameters:
    locale: en

framework:
    #esi: ~
    translator: { fallbacks: ['%locale%'] }
    secret: '%secret%'
    router:
        resource: '%kernel.project_dir%/app/config/routing.yml'
        strict_requirements: ~
    form: ~
    csrf_protection: ~
    validation: { enable_annotations: true }
    #serializer: { enable_annotations: true }
    templating:
        engines: ['twig']
    default_locale: '%locale%'
    trusted_hosts: ~
    session:
        # https://symfony.com/doc/current/reference/configuration/framework.html#handler-id
        handler_id: session.handler.native_file
        save_path: '%kernel.project_dir%/var/sessions/%kernel.environment%'
    fragments: ~
    http_method_override: true
    assets: ~
    php_errors:
        log: true
    cache:
        app: cache.adapter.redis
        default_psr6_provider: cache.adapter.redis
        default_redis_provider: redis://localhost:4600

# Twig Configuration
twig:
    debug: '%kernel.debug%'
    strict_variables: '%kernel.debug%'

# Doctrine Configuration
doctrine:
    dbal:
        driver: '%database_driver%'
        host: '%database_host%'
        port: '%database_port%'
        dbname: '%database_name%'
        user: '%database_user%'
        password: '%database_password%'
        charset: UTF8
        types:
            wish_id: Wishlist\Infrastructure\Persistence\Doctrine\Type\WishIdType
            deposit_id: Wishlist\Infrastructure\Persistence\Doctrine\Type\DepositIdType

    orm:
        auto_generate_proxy_classes: '%kernel.debug%'
        naming_strategy: doctrine.orm.naming_strategy.underscore
        auto_mapping: true
        second_level_cache:
            enabled: true
        mappings:
            Money:
                type: yml
                dir: "%kernel.root_dir%/config/doctrine/Money"
                is_bundle: false
                prefix: Money
                alias: Money
            Wishlist\Domain:
                type: yml
                dir: "%kernel.root_dir%/config/doctrine/Wishlist"
                is_bundle: false
                prefix: Wishlist\Domain
                alias: Wishlist

# Swiftmailer Configuration
swiftmailer:
    transport: '%mailer_transport%'
    host: '%mailer_host%'
    username: '%mailer_user%'
    password: '%mailer_password%'
    spool: { type: memory }
```

## File: `app/config/config_dev.yml`
```yaml
imports:
    - { resource: config.yml }

framework:
    router:
        resource: '%kernel.project_dir%/app/config/routing_dev.yml'
        strict_requirements: true
    profiler: { only_exceptions: false }

web_profiler:
    toolbar: true
    intercept_redirects: false

monolog:
    handlers:
        main:
            type: stream
            path: '%kernel.logs_dir%/%kernel.environment%.log'
            level: debug
            channels: ['!event']
        console:
            type: console
            process_psr_3_messages: false
            channels: ['!event', '!doctrine', '!console']
        # To follow logs in real time, execute the following command:
        # `bin/console server:log -vv`
        server_log:
            type: server_log
            process_psr_3_messages: false
            host: 127.0.0.1:9911
        # uncomment to get logging in your browser
        # you may have to allow bigger header sizes in your Web server configuration
        #firephp:
        #    type: firephp
        #    level: info
        #chromephp:
        #    type: chromephp
        #    level: info

#swiftmailer:
#    delivery_addresses: ['me@example.com']
```

## File: `app/config/config_prod.yml`
```yaml
imports:
    - { resource: config.yml }

#doctrine:
#    orm:
#        metadata_cache_driver: apc
#        result_cache_driver: apc
#        query_cache_driver: apc

monolog:
    handlers:
        main:
            type: fingers_crossed
            action_level: error
            handler: nested
        nested:
            type: stream
            path: '%kernel.logs_dir%/%kernel.environment%.log'
            level: debug
        console:
            type: console
            process_psr_3_messages: false
```

## File: `app/config/config_test.yml`
```yaml
imports:
    - { resource: config_dev.yml }
    - { resource: services_test.yml }

framework:
    test: ~
    session:
        storage_id: session.storage.mock_file
    profiler:
        collect: false

web_profiler:
    toolbar: false
    intercept_redirects: false

swiftmailer:
    disable_delivery: true

liip_functional_test: ~

doctrine:
    dbal:
        driver: pdo_sqlite
        path: "%kernel.cache_dir%/test.db"
```

## File: `app/config/parameters.yml.dist`
```
parameters:
    database_host: 127.0.0.1
    database_port: 4500
    database_name: symfony_wishlist
    database_user: postgres
    database_password: userpass
    mailer_transport: smtp
    mailer_host: 127.0.0.1
    mailer_user: ~
    mailer_password: ~
    secret: ThisHasToBeChangedToSomethingSecure
```

## File: `app/config/parameters_permanent.yml.dist`
```
parameters:
    database_driver: pdo_pgsql
    default_currency_code: USD
```

## File: `app/config/routing.yml`
```yaml
app:
    resource: '../src/Http/Controller'
    type: annotation

fos_js_routing:
    resource: "@FOSJsRoutingBundle/Resources/config/routing/routing.xml"
```

## File: `app/config/routing_dev.yml`
```yaml
_wdt:
    resource: '@WebProfilerBundle/Resources/config/routing/wdt.xml'
    prefix: /_wdt

_profiler:
    resource: '@WebProfilerBundle/Resources/config/routing/profiler.xml'
    prefix: /_profiler

_errors:
    resource: '@TwigBundle/Resources/config/routing/errors.xml'
    prefix: /_error

_main:
    resource: routing.yml
```

## File: `app/config/security.yml`
```yaml
# To get started with security, check out the documentation:
# https://symfony.com/doc/current/security.html
security:

    # https://symfony.com/doc/current/security.html#b-configuring-how-users-are-loaded
    providers:
        in_memory:
            memory: ~

    firewalls:
        # disables authentication for assets and the profiler, adapt it according to your needs
        dev:
            pattern: ^/(_(profiler|wdt)|css|images|js)/
            security: false

        main:
            anonymous: ~
            # activate different ways to authenticate

            # https://symfony.com/doc/current/security.html#a-configuring-how-your-users-will-authenticate
            #http_basic: ~

            # https://symfony.com/doc/current/security/form_login_setup.html
            #form_login: ~
```

## File: `app/config/services.yml`
```yaml
# Learn more about services, parameters and containers at
# https://symfony.com/doc/current/service_container.html
parameters:
    #parameter_name: value

services:
    # default configuration for services in *this* file
    _defaults:
        # automatically injects dependencies in your services
        autowire: true
        # automatically registers your services as commands, event subscribers, etc.
        autoconfigure: true
        # this means you cannot fetch services directly from the container via $container->get()
        # if you need to do this, you can override this setting on individual services
        public: false

    # controllers are imported separately to make sure they're public
    # and have a tag that allows actions to type-hint services
    Wishlist\Http\Controller\:
        resource: '../../src/Http/Controller'
        public: true
        tags: ['controller.service_arguments']

    Wishlist\Domain\WishRepositoryInterface:
        class: Wishlist\Infrastructure\Persistence\Doctrine\WishRepository
        autowire: true

    Symfony\Component\Cache\Adapter\TagAwareAdapterInterface:
        class: Symfony\Component\Cache\Adapter\TagAwareAdapterInterface
        factory: [Wishlist\Infrastructure\Cache\TagAwareAdapterFactory, createAdapter]
        arguments:
            - '@cache.app'

    wishlist.wish.repository:
        class: Wishlist\Infrastructure\Persistence\Common\CachingWishRepository
        arguments:
            - '@Wishlist\Domain\WishRepositoryInterface'
            - '@Symfony\Component\Cache\Adapter\TagAwareAdapterInterface'

    wishlist.currency.factory:
        class: Wishlist\Infrastructure\Currency\DefaultCurrencyFactory
        public: true
        factory: [Wishlist\Infrastructure\Currency\DefaultCurrencyFactory, createCurrency]
        arguments:
            - '%default_currency_code%'

    Wishlist\Application\WishlistInterface:
        class: Wishlist\Application\Wishlist
        arguments:
            - '@wishlist.wish.repository'
            - "@=service('wishlist.currency.factory')"

    Wishlist\Infrastructure\Validation\ConstraintViolationListTransformerInterface:
        class: Wishlist\Infrastructure\Validation\ConstraintViolationListTransformer

    wishlist.event_listener.domain_exception:
        class: Wishlist\Http\EventListener\DomainExceptionListener
        tags:
            - { name: kernel.event_listener, event: kernel.exception }
```

## File: `app/config/services_test.yml`
```yaml
services:
    wishlist.wish.repository:
        class: Wishlist\Infrastructure\Persistence\Doctrine\WishRepository
        autowire: true
        public: false
```

## File: `app/config/doctrine/Money/Currency.orm.yml`
```yaml
Money\Currency:
    type: embeddable
    fields:
        code:
            type: string
            nullable: false
            length: 3
```

## File: `app/config/doctrine/Money/Money.orm.yml`
```yaml
Money\Money:
    type: embeddable
    embedded:
        currency:
            class: Money\Currency
    fields:
        amount:
            type: decimal
            precision: 20
            scale: 2
            nullable: false
```

## File: `app/config/doctrine/Wishlist/Deposit.orm.yml`
```yaml
Wishlist\Domain\Deposit:
    type: entity
    table: deposits
    id:
        id:
            type: deposit_id
            generator:
                strategy: none
    manyToOne:
        wish:
            targetEntity: Wishlist\Domain\Wish
            inversedBy: deposits
            joinColumn:
                name: wish_id
                referencedColumnName: id
                nullable: false
    embedded:
        amount:
            class: Money\Money
            columnPrefix: false
    fields:
        createdAt:
            type: datetime
            nullable: false
            column: created_at
```

## File: `app/config/doctrine/Wishlist/Expense.orm.yml`
```yaml
Wishlist\Domain\Expense:
    type: embeddable
    embedded:
        price:
            class: Money\Money
        fee:
            class: Money\Money
        initialFund:
            class: Money\Money
```

## File: `app/config/doctrine/Wishlist/Wish.orm.yml`
```yaml
Wishlist\Domain\Wish:
    type: entity
    table: wishes
    id:
        id:
            type: wish_id
            generator:
                strategy: none
    embedded:
        name:
            class: Wishlist\Domain\WishName
            columnPrefix: false
        expense:
            class: Wishlist\Domain\Expense
            columnPrefix: false
    oneToMany:
        deposits:
            targetEntity: Wishlist\Domain\Deposit
            mappedBy: wish
            orphanRemoval: true
            orderBy:
                createdAt: DESC
            cascade: [persist]
    fields:
        published:
            type: boolean
            nullable: false
            options:
                default: false
        createdAt:
            type: datetime
            nullable: false
            column: created_at
        updatedAt:
            type: datetime
            nullable: false
            column: updated_at
```

## File: `app/config/doctrine/Wishlist/WishName.orm.yml`
```yaml
Wishlist\Domain\WishName:
    type: embeddable
    fields:
        name:
            type: string
            nullable: false
```

## File: `src/.htaccess`
```
<IfModule mod_authz_core.c>
    Require all denied
</IfModule>
<IfModule !mod_authz_core.c>
    Order deny,allow
    Deny from all
</IfModule>
```

## File: `src/Application/Wishlist.php`
```php
<?php

namespace Wishlist\Application;

use Money\Currency;
use Money\Money;
use Wishlist\Application\Assembler\ListWishDtoAssembler;
use Wishlist\Application\Dto\DepositDto;
use Wishlist\Application\Dto\NewWishDto;
use Wishlist\Domain\DepositId;
use Wishlist\Domain\Exception\InvalidIdentityException;
use Wishlist\Domain\Exception\WishNotFoundException;
use Wishlist\Domain\Expense;
use Wishlist\Domain\Wish;
use Wishlist\Domain\WishId;
use Wishlist\Domain\WishName;
use Wishlist\Domain\WishRepositoryInterface;

class Wishlist implements WishlistInterface
{
    private $wishes;
    private $currency;

    public function __construct(WishRepositoryInterface $wishes, Currency $currency)
    {
        $this->wishes = $wishes;
        $this->currency = $currency;
    }

    public function getWishesByPage(int $page, int $limit): array
    {
        $wishes = $this->wishes->slice($page * $limit, $limit);

        return (new ListWishDtoAssembler())->toArrayOfDto($wishes);
    }

    public function addNewWish(NewWishDto $dto): string
    {
        $wishId = WishId::next();
        $this->wishes->put($this->createWishFromIdAndDto($wishId, $dto));

        return $wishId->getId();
    }

    private function createWishFromIdAndDto(WishId $wishId, NewWishDto $dto): Wish
    {
        $wish = new Wish(
            $wishId,
            new WishName($dto->name),
            Expense::fromCurrencyAndScalars(
                $this->currency,
                $dto->price,
                $dto->fee,
                $dto->initialFund
            )
        );

        if ($dto->isPublished) {
            $wish->publish();
        }

        return $wish;
    }

    public function deposit(string $wishId, int $amount): DepositDto
    {
        $wish = $this->getWish($wishId);
        $deposit = $wish->deposit(new Money($amount, $this->currency));
        $this->wishes->put($wish);

        $dto = new DepositDto();
        $dto->depositId = $deposit->getId()->getId();
        $dto->amount = $deposit->getMoney()->getAmount();
        $dto->currency = $deposit->getMoney()->getCurrency();
        $dto->createdAt = $deposit->getDate()->format('d.m.Y H:i');

        return $dto;
    }

    public function withdraw(string $wishId, string $depositId): Money
    {
        $wish = $this->getWish($wishId);
        $wish->withdraw(DepositId::fromString($depositId));
        $this->wishes->put($wish);

        return $wish->getFund();
    }

    public function publish(string $wishId)
    {
        $wish = $this->getWish($wishId);
        $wish->publish();
        $this->wishes->put($wish);
    }

    public function unpublish(string $wishId)
    {
        $wish = $this->getWish($wishId);
        $wish->unpublish();
        $this->wishes->put($wish);
    }

    private function getWish(string $wishId): Wish
    {
        try {
            return $this->wishes->get(WishId::fromString($wishId));
        } catch (InvalidIdentityException $ex) {
            throw new WishNotFoundException($wishId);
        }
    }

    public function getTotalWishesNumber(): int
    {
        return $this->wishes->count();
    }
}
```

## File: `src/Application/WishlistInterface.php`
```php
<?php

namespace Wishlist\Application;

use Money\Money;
use Wishlist\Application\Dto\DepositDto;
use Wishlist\Application\Dto\NewWishDto;

interface WishlistInterface
{
    public function addNewWish(NewWishDto $dto): string;
    public function deposit(string $wishId, int $amount): DepositDto;
    public function withdraw(string $wishId, string $depositId): Money;
    public function publish(string $wishId);
    public function unpublish(string $wishId);
    public function getWishesByPage(int $page, int $limit): array;
    public function getTotalWishesNumber(): int;
}
```

## File: `src/Application/Assembler/ListWishDtoAssembler.php`
```php
<?php

namespace Wishlist\Application\Assembler;

use Wishlist\Application\Dto\DepositDto;
use Wishlist\Application\Dto\ListWishDto;
use Wishlist\Domain\Deposit;
use Wishlist\Domain\Wish;

class ListWishDtoAssembler
{
    /**
     * @param array|Wish[] $wishes
     *
     * @return array
     */
    public function toArrayOfDto(array $wishes): array
    {
        return array_map(function (Wish $wish) {
            $dto = new ListWishDto();
            $dto->id = $wish->getId()->getId();
            $dto->name = $wish->getName();
            $dto->fund = $wish->getFund()->getAmount();
            $dto->price = $wish->getPrice()->getAmount();
            $dto->createdAt = $wish->getCreatedAt()->format('d.m');
            $dto->isPublished = $wish->isPublished();
            $dto->currency = $wish->getCurrency()->getCode();
            $dto->deposits = $this->assembleDeposits($wish->getDeposits());

            return $dto;
        }, $wishes);
    }

    private function assembleDeposits(array $deposits)
    {
        return array_map(function (Deposit $deposit) {
            $dto = new DepositDto();
            $dto->id = $deposit->getId()->getId();
            $dto->amount = $deposit->getMoney()->getAmount();
            $dto->currency = $deposit->getMoney()->getCurrency()->getCode();
            $dto->createdAt = $deposit->getDate()->format('d.m.Y H:i');

            return $dto;
        }, $deposits);
    }
}
```

## File: `src/Application/Dto/DepositDto.php`
```php
<?php

namespace Wishlist\Application\Dto;

class DepositDto implements \JsonSerializable
{
    public $id;
    public $amount;
    public $currency;
    public $createdAt;

    public function jsonSerialize()
    {
        return [
            'id' => $this->id,
            'amount' => $this->amount,
            'currency' => $this->currency,
            'createdAt' => $this->createdAt
        ];
    }
}
```

## File: `src/Application/Dto/ListWishDto.php`
```php
<?php

namespace Wishlist\Application\Dto;

class ListWishDto
{
    public $id;
    public $name;
    public $price;
    public $fund;
    public $createdAt;
    public $isPublished;
    public $currency;
    public $deposits;
}
```

## File: `src/Application/Dto/NewWishDto.php`
```php
<?php

namespace Wishlist\Application\Dto;

final class NewWishDto
{
    public $name;
    public $price;
    public $fee;
    public $initialFund;
    public $isPublished;
}
```

## File: `src/Domain/AbstractId.php`
```php
<?php

namespace Wishlist\Domain;

use Ramsey\Uuid\Exception\InvalidUuidStringException;
use Ramsey\Uuid\Uuid;
use Ramsey\Uuid\UuidInterface;
use Wishlist\Domain\Exception\InvalidIdentityException;

abstract class AbstractId
{
    protected $id;

    private function __construct(UuidInterface $id)
    {
        $this->id = $id;
    }

    public static function fromString(string $id)
    {
        try {
            return new static(Uuid::fromString($id));
        } catch (InvalidUuidStringException $exception) {
            throw new InvalidIdentityException($id);
        }
    }

    public static function next()
    {
        return new static(Uuid::uuid4());
    }

    public function getId(): string
    {
        return $this->id->toString();
    }

    public function equalTo(AbstractId $id): bool
    {
        return $this->getId() === $id->getId() &&
               get_class($this) === get_class($id);
    }

    public function __toString(): string
    {
        return $this->getId();
    }
}
```

## File: `src/Domain/Deposit.php`
```php
<?php

namespace Wishlist\Domain;

use DateTimeImmutable;
use DateTimeInterface;
use Money\Money;
use Webmozart\Assert\Assert;

class Deposit
{
    private $id;
    private $wish;
    private $amount;
    private $createdAt;

    public function __construct(DepositId $id, Wish $wish, Money $amount)
    {
        Assert::false($amount->isZero(), 'Deposit must not be empty.');

        $this->id = $id;
        $this->wish = $wish;
        $this->amount = $amount;
        $this->createdAt = new DateTimeImmutable();
    }

    public function getId(): DepositId
    {
        return $this->id;
    }

    public function getWish(): Wish
    {
        return $this->wish;
    }

    public function getMoney(): Money
    {
        return $this->amount;
    }

    public function getDate(): DateTimeInterface
    {
        return $this->createdAt;
    }
}
```

## File: `src/Domain/DepositId.php`
```php
<?php

namespace Wishlist\Domain;

final class DepositId extends AbstractId
{
    //
}
```

## File: `src/Domain/Expense.php`
```php
<?php

namespace Wishlist\Domain;

use Money\Currency;
use Money\Money;
use Webmozart\Assert\Assert;

final class Expense
{
    private $price;
    private $fee;
    private $initialFund;

    private function __construct(Money $price, Money $fee, Money $initialFund)
    {
        $this->price = $price;
        $this->fee = $fee;
        $this->initialFund = $initialFund;
    }

    public static function fromCurrencyAndScalars(
        Currency $currency,
        int $price,
        int $fee,
        int $initialFund = null
    ) {
        foreach ([$price, $fee] as $argument) {
            Assert::notEmpty($argument);
            Assert::greaterThan($argument, 0);
        }

        Assert::lessThan($fee, $price, 'Fee must be less than price.');

        if (null !== $initialFund) {
            Assert::greaterThanEq($initialFund, 0);
            Assert::lessThan($initialFund, $price, 'Initial fund must be less than price.');
        }

        return new static(
            new Money($price, $currency),
            new Money($fee, $currency),
            new Money($initialFund ?? 0, $currency)
        );
    }

    public function getCurrency(): Currency
    {
        return $this->price->getCurrency();
    }

    public function getPrice(): Money
    {
        return $this->price;
    }

    public function changePrice(Money $amount): Expense
    {
        Assert::true($amount->getCurrency()->equals($this->getCurrency()));

        return new static($amount, $this->fee, $this->initialFund);
    }

    public function getFee(): Money
    {
        return $this->fee;
    }

    public function changeFee(Money $amount): Expense
    {
        Assert::true($amount->getCurrency()->equals($this->getCurrency()));

        return new static($this->price, $amount, $this->initialFund);
    }

    public function getInitialFund(): Money
    {
        return $this->initialFund;
    }
}
```

## File: `src/Domain/Wish.php`
```php
<?php

namespace Wishlist\Domain;

use DateInterval;
use DateTimeImmutable;
use DateTimeInterface;
use Doctrine\Common\Collections\ArrayCollection;
use Money\Currency;
use Money\Money;
use Webmozart\Assert\Assert;
use Wishlist\Domain\Exception\DepositDoesNotExistException;
use Wishlist\Domain\Exception\DepositIsTooSmallException;
use Wishlist\Domain\Exception\WishIsFulfilledException;
use Wishlist\Domain\Exception\WishIsUnpublishedException;

class Wish
{
    private $id;
    private $name;
    private $expense;
    /** @var Deposit[] */
    private $deposits;
    private $published = false;
    private $createdAt;
    private $updatedAt;

    public function __construct(
        WishId $id,
        WishName $name,
        Expense $expense,
        DateTimeImmutable $createdAt = null
    ) {
        $this->id = $id;
        $this->name = $name;
        $this->expense = $expense;
        $this->deposits = new ArrayCollection();
        $this->createdAt = $createdAt ?? new DateTimeImmutable();
        $this->updatedAt = $createdAt ?? new DateTimeImmutable();
    }

    public function deposit(Money $amount): Deposit
    {
        $this->assertCanDeposit($amount);

        $deposit = new Deposit(DepositId::next(), $this, $amount);
        $this->deposits->add($deposit);

        return $deposit;
    }

    private function assertCanDeposit(Money $amount)
    {
        if (!$this->published) {
            throw new WishIsUnpublishedException($this->getId());
        }

        if ($this->isFulfilled()) {
            throw new WishIsFulfilledException($this->getId());
        }

        if ($amount->lessThan($this->getFee())) {
            throw new DepositIsTooSmallException($amount, $this->getFee());
        }

        Assert::true(
            $amount->isSameCurrency($this->expense->getPrice()),
            'Deposit currency must match the price\'s one.'
        );
    }

    public function isFulfilled(): bool
    {
        return $this->getFund()->greaterThanOrEqual($this->expense->getPrice());
    }

    public function withdraw(DepositId $depositId)
    {
        $this->assertCanWithdraw();

        $deposit = $this->getDepositById($depositId);
        $this->deposits->removeElement($deposit);
    }

    private function assertCanWithdraw()
    {
        if (!$this->published) {
            throw new WishIsUnpublishedException($this->getId());
        }

        if ($this->isFulfilled()) {
            throw new WishIsFulfilledException($this->getId());
        }
    }

    private function getDepositById(DepositId $depositId): Deposit
    {
        $deposit = $this->deposits->filter(
            function (Deposit $deposit) use ($depositId) {
                return $deposit->getId()->equalTo($depositId);
            }
        )->first();

        if (!$deposit) {
            throw new DepositDoesNotExistException($depositId);
        }

        return $deposit;
    }

    public function calculateSurplusFunds(): Money
    {
        $difference = $this->getPrice()->subtract($this->getFund());

        return $difference->isNegative()
            ? $difference->absolute()
            : new Money(0, $this->getCurrency());
    }

    public function predictFulfillmentDateBasedOnFee(): DateTimeInterface
    {
        $daysToGo = ceil(
            $this->getPrice()
            ->divide($this->getFee()->getAmount())
            ->getAmount()
        );

        return $this->createFutureDate($daysToGo);
    }

    public function predictFulfillmentDateBasedOnFund(): DateTimeInterface
    {
        $daysToGo = ceil(
            $this->getPrice()
            ->subtract($this->getFund())
            ->divide($this->getFee()->getAmount())
            ->getAmount()
        );

        return $this->createFutureDate($daysToGo);
    }

    private function createFutureDate($daysToGo): DateTimeInterface
    {
        return (new DateTimeImmutable())->add(new DateInterval("P{$daysToGo}D"));
    }

    public function publish()
    {
        $this->published = true;
        $this->updatedAt = new DateTimeImmutable();
    }

    public function unpublish()
    {
        $this->published = false;
        $this->updatedAt = new DateTimeImmutable();
    }

    public function isPublished(): bool
    {
        return $this->published;
    }

    public function getId(): WishId
    {
        return $this->id;
    }

    public function getName(): string
    {
        return (string) $this->name;
    }

    public function getPrice(): Money
    {
        return $this->expense->getPrice();
    }

    public function changePrice(Money $amount)
    {
        $this->expense = $this->expense->changePrice($amount);
        $this->updatedAt = new DateTimeImmutable();
    }

    public function getFee(): Money
    {
        return $this->expense->getFee();
    }

    public function changeFee(Money $amount)
    {
        $this->expense = $this->expense->changeFee($amount);
        $this->updatedAt = new DateTimeImmutable();
    }

    public function getFund(): Money
    {
        return array_reduce($this->deposits->toArray(), function (Money $fund, Deposit $deposit) {
            return $fund->add($deposit->getMoney());
        }, $this->expense->getInitialFund());
    }

    /**
     * @return array|Deposit[]
     */
    public function getDeposits(): array
    {
        return $this->deposits->toArray();
    }

    public function getCurrency(): Currency
    {
        return $this->expense->getCurrency();
    }

    public function getCreatedAt(): DateTimeInterface
    {
        return $this->createdAt;
    }

    public function getUpdatedAt(): DateTimeInterface
    {
        return $this->updatedAt;
    }
}
```

## File: `src/Domain/WishId.php`
```php
<?php

namespace Wishlist\Domain;

final class WishId extends AbstractId
{
    //
}
```

## File: `src/Domain/WishName.php`
```php
<?php

namespace Wishlist\Domain;

use Webmozart\Assert\Assert;

final class WishName
{
    private $name;

    public function __construct(string $name)
    {
        Assert::notEmpty($name, 'Name must not be empty.');

        $this->name = $name;
    }

    public function getValue(): string
    {
        return $this->name;
    }

    public function __toString(): string
    {
        return $this->getValue();
    }
}
```

## File: `src/Domain/WishRepositoryInterface.php`
```php
<?php

namespace Wishlist\Domain;

interface WishRepositoryInterface
{
    public function get(WishId $wishId): Wish;
    public function put(Wish $wish);
    public function slice(int $offset, int $limit): array;
    public function contains(Wish $wish): bool;
    public function containsId(WishId $wishId): bool;
    public function count(): int;
    public function getNextWishId(): WishId;
}
```

## File: `src/Domain/Exception/DepositDoesNotExistException.php`
```php
<?php

namespace Wishlist\Domain\Exception;

use Exception;
use Wishlist\Domain\DepositId;

class DepositDoesNotExistException extends Exception implements DomainExceptionInterface, NotFoundExceptionInterface
{
    public function __construct(DepositId $id)
    {
        parent::__construct('Deposit does not exist: ' . $id);
    }
}
```

## File: `src/Domain/Exception/DepositIsTooSmallException.php`
```php
<?php

namespace Wishlist\Domain\Exception;

use Exception;
use Money\Money;

class DepositIsTooSmallException extends Exception
{
    public function __construct(Money $deposit, Money $fee)
    {
        parent::__construct(
            sprintf(
                'Deposit %s %s is too small. It must not be less than %s %s',
                $deposit->getAmount(),
                $deposit->getCurrency(),
                $fee->getAmount(),
                $fee->getCurrency()
            )
        );
    }
}
```

## File: `src/Domain/Exception/DomainExceptionInterface.php`
```php
<?php

namespace Wishlist\Domain\Exception;

interface DomainExceptionInterface
{

}
```

## File: `src/Domain/Exception/InvalidIdentityException.php`
```php
<?php

namespace Wishlist\Domain\Exception;

use Exception;

class InvalidIdentityException extends Exception
{
    public function __construct($identifier)
    {
        parent::__construct('Invalid identity: ' . (string) $identifier);
    }
}
```

## File: `src/Domain/Exception/InvalidOperationExceptionInterface.php`
```php
<?php

namespace Wishlist\Domain\Exception;

interface InvalidOperationExceptionInterface
{
    //
}
```

## File: `src/Domain/Exception/NotFoundExceptionInterface.php`
```php
<?php

namespace Wishlist\Domain\Exception;

interface NotFoundExceptionInterface
{

}
```

## File: `src/Domain/Exception/WishIsFulfilledException.php`
```php
<?php

namespace Wishlist\Domain\Exception;

use Exception;
use Wishlist\Domain\WishId;

class WishIsFulfilledException extends Exception implements DomainExceptionInterface, InvalidOperationExceptionInterface
{
    public function __construct(WishId $wishId)
    {
        parent::__construct('The wish is fulfilled. ID: ' . $wishId);
    }
}
```

## File: `src/Domain/Exception/WishIsUnpublishedException.php`
```php
<?php

namespace Wishlist\Domain\Exception;

use Exception;
use Wishlist\Domain\WishId;

class WishIsUnpublishedException extends Exception implements DomainExceptionInterface, InvalidOperationExceptionInterface
{
    public function __construct(WishId $wishId)
    {
        parent::__construct('The wish is unpublished. ID: ' . $wishId);
    }
}
```

## File: `src/Domain/Exception/WishNotFoundException.php`
```php
<?php

namespace Wishlist\Domain\Exception;

use Exception;

class WishNotFoundException extends Exception implements DomainExceptionInterface, NotFoundExceptionInterface
{
    public function __construct($wishId)
    {
        parent::__construct('Wish not found. ID: ' . (string) $wishId);
    }
}
```

## File: `src/Http/Controller/WishlistController.php`
```php
<?php

namespace Wishlist\Http\Controller;

use Sensio\Bundle\FrameworkExtraBundle\Configuration\Route;
use Symfony\Bundle\FrameworkBundle\Templating\EngineInterface;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\Routing\RouterInterface;
use Symfony\Component\Translation\TranslatorInterface;
use Symfony\Component\Validator\Constraints\Collection;
use Symfony\Component\Validator\Constraints\GreaterThan;
use Symfony\Component\Validator\Constraints\Required;
use Symfony\Component\Validator\Validator\ValidatorInterface;
use Wishlist\Application\WishlistInterface;
use Wishlist\Infrastructure\Validation\ConstraintViolationListTransformerInterface;

class WishlistController
{
    private $engine;
    private $router;
    private $translator;
    private $validator;
    private $wishlist;

    public function __construct(
        EngineInterface $engine,
        RouterInterface $router,
        TranslatorInterface $translator,
        ValidatorInterface $validator,
        WishlistInterface $wishlist
    ) {
        $this->engine = $engine;
        $this->router = $router;
        $this->translator = $translator;
        $this->validator = $validator;
        $this->wishlist = $wishlist;
    }

    /**
     * @Route(
     *     "/wishes",
     *     name="wishlist.index",
     *     methods={"GET"},
     *     options={"expose"=true}
     * )
     * @param Request $request
     *
     * @return \Symfony\Component\HttpFoundation\Response
     */
    public function indexAction(Request $request)
    {
        $page = $request->query->getInt('page', 1) - 1;
        $limit = $request->query->getInt('limit', 10);

        if ($request->isXmlHttpRequest()) {
            $startIndex = $page * $limit + 1;
            $endIndex = $startIndex + $limit - 1;

            $wishes = $this->wishlist->getWishesByPage($page, $limit);
            $total = $this->wishlist->getTotalWishesNumber();
            $totalPages = ceil($total / $limit);
            $page++;

            return new JsonResponse([
                'wishes' => $wishes,
                'pagination' => compact(
                    'page',
                    'limit',
                    'startIndex',
                    'endIndex',
                    'total',
                    'totalPages'
                )
            ]);
        }

        return $this->engine->renderResponse(
            ':wishlist:index.html.twig',
            compact('page', 'limit')
        );
    }

    /**
     * @Route(
     *     "/wishes/{wishId}/publish",
     *     name="wishlist.wish.publish",
     *     methods={"PUT"},
     *     options={"expose"=true}
     * )
     * @param string $wishId
     *
     * @return JsonResponse
     */
    public function publishAction(string $wishId)
    {
        $this->wishlist->publish($wishId);

        return new JsonResponse([
            'url' => $this->router->generate('wishlist.wish.unpublish', compact('wishId')),
            'label' => $this->translator->trans('wishlist.table.unpublish'),
            'published' => true
        ]);
    }

    /**
     * @Route(
     *     "/wishes/{wishId}/unpublish",
     *     name="wishlist.wish.unpublish",
     *     methods={"PUT"},
     *     options={"expose"=true}
     * )
     * @param string $wishId
     *
     * @return JsonResponse
     */
    public function unpublishAction(string $wishId)
    {
        $this->wishlist->unpublish($wishId);

        return new JsonResponse([
            'url' => $this->router->generate('wishlist.wish.publish', compact('wishId')),
            'label' => $this->translator->trans('wishlist.table.publish'),
            'published' => false
        ]);
    }

    /**
     * @Route(
     *     "/wishes/{wishId}/deposit",
     *     name="wishlist.wish.deposit",
     *     methods={"POST"},
     *     options={"expose"=true}
     * )
     * @param Request $request
     * @param ConstraintViolationListTransformerInterface $transformer
     *
     * @return JsonResponse
     */
    public function depositAction(
        Request $request,
        ConstraintViolationListTransformerInterface $transformer
    ) {
        $wishId = $request->get('wishId');
        $amount = $request->request->getInt('amount');

        $violations = $this->validator->validate(compact('amount'), new Collection([
            'amount' => new Required([
                new GreaterThan([
                    'value' => 0
                ])
            ])
        ]));

        if ($violations->count() > 0) {
            return new JsonResponse([
                'success' => false,
                'violations' => $transformer->toArray($violations)
            ], JsonResponse::HTTP_UNPROCESSABLE_ENTITY);
        }

        $deposit = $this->wishlist->deposit($wishId, $amount);

        return new JsonResponse([
            'success' => true,
            'deposit' => $deposit,
        ]);
    }

    /**
     * @Route(
     *     "/wishes/{wishId}/{depositId}/withdraw",
     *     name="wishlist.wish.withdraw",
     *     methods={"DELETE"},
     *     options={"expose"=true}
     * )
     *
     * @param string $wishId
     * @param string $depositId
     *
     * @return JsonResponse
     */
    public function withdrawAction(string $wishId, string $depositId)
    {
        $this->wishlist->withdraw($wishId, $depositId);

        return new JsonResponse([
            'success' => true
        ]);
    }
}
```

## File: `src/Http/EventListener/DomainExceptionListener.php`
```php
<?php

namespace Wishlist\Http\EventListener;

use Exception;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\HttpKernel\Event\GetResponseForExceptionEvent;
use Wishlist\Domain\Exception\DomainExceptionInterface;
use Wishlist\Domain\Exception\InvalidOperationExceptionInterface;
use Wishlist\Domain\Exception\NotFoundExceptionInterface;

class DomainExceptionListener
{
    private static $exceptionClassesToHttpCodes = [
        NotFoundExceptionInterface::class => Response::HTTP_NOT_FOUND,
        InvalidOperationExceptionInterface::class => Response::HTTP_UNPROCESSABLE_ENTITY
    ];

    public function onKernelException(GetResponseForExceptionEvent $event)
    {
        $exception = $event->getException();

        if (!$this->isSatisfiedByEvent($event)) {
            return;
        }

        $response = new JsonResponse(
            [
                'success' => false,
                'message' => $exception->getMessage()
            ],
            $this->getResponseCodeFromException($exception)
        );

        $event->setResponse($response);
    }

    private function isSatisfiedByEvent(GetResponseForExceptionEvent $event)
    {
        return $event->getException() instanceof DomainExceptionInterface &&
               $event->getRequest()->isXmlHttpRequest();
    }

    private function getResponseCodeFromException(Exception $exception)
    {
        foreach (static::$exceptionClassesToHttpCodes as $class => $code) {
            if ($exception instanceof $class) {
                return $code;
            }
        }

        return Response::HTTP_INTERNAL_SERVER_ERROR;
    }
}
```

## File: `src/Infrastructure/Cache/CacheOptions.php`
```php
<?php

namespace Wishlist\Infrastructure\Cache;

use Webmozart\Assert\Assert;

final class CacheOptions
{
    private $key;
    private $lifetime;
    private $tags;

    public function __construct(string $key, int $lifetime, array $tags = [])
    {
        Assert::notEmpty($key);
        Assert::greaterThanEq($lifetime, 0);

        if (!empty($tags)) {
            Assert::allStringNotEmpty($tags);
        }

        $this->key = $key;
        $this->lifetime = $lifetime;
        $this->tags = $tags;
    }

    public function getKey(): string
    {
        return $this->key;
    }

    public function getLifetime(): int
    {
        return $this->lifetime;
    }

    public function getTags(): array
    {
        return $this->tags;
    }
}
```

## File: `src/Infrastructure/Cache/TagAwareAdapterFactory.php`
```php
<?php

namespace Wishlist\Infrastructure\Cache;

use Symfony\Component\Cache\Adapter\AdapterInterface;
use Symfony\Component\Cache\Adapter\TagAwareAdapter;

class TagAwareAdapterFactory
{
    public static function createAdapter(AdapterInterface $adapter): TagAwareAdapter
    {
        return new TagAwareAdapter($adapter, $adapter);
    }
}
```

## File: `src/Infrastructure/Currency/DefaultCurrencyFactory.php`
```php
<?php

namespace Wishlist\Infrastructure\Currency;

use Money\Currency;

class DefaultCurrencyFactory
{
    public static function createCurrency(string $code = 'USD'): Currency
    {
        return new Currency($code);
    }
}
```

## File: `src/Infrastructure/Persistence/Common/CachingWishRepository.php`
```php
<?php

namespace Wishlist\Infrastructure\Persistence\Common;

use Closure;
use Symfony\Component\Cache\Adapter\TagAwareAdapterInterface;
use Wishlist\Domain\Wish;
use Wishlist\Domain\WishId;
use Wishlist\Domain\WishRepositoryInterface;
use Wishlist\Infrastructure\Cache\CacheOptions;

class CachingWishRepository implements WishRepositoryInterface
{
    private $repository;
    private $cache;

    public function __construct(WishRepositoryInterface $repository, TagAwareAdapterInterface $cache)
    {
        $this->repository = $repository;
        $this->cache = $cache;
    }

    public function get(WishId $wishId): Wish
    {
        $cacheOptions = new CacheOptions('wishlist.wish.' . $wishId->getId(), 5 * 60);

        return $this->fetch(function () use ($wishId) {
            return $this->repository->get($wishId);
        }, $cacheOptions);
    }

    public function put(Wish $wish)
    {
        $this->repository->put($wish);

        $this->cache->deleteItems($this->getKeysToExpire($wish));
        $this->cache->invalidateTags($this->getTagsToExpire());
    }

    private function getKeysToExpire(Wish $wish): array
    {
        return [
            'wishlist.wish.' . $wish->getId(),
            'wishlist.contains.' . $wish->getId(),
            'wishlist.count',
        ];
    }

    private function getTagsToExpire(): array
    {
        return [
            'wishlist.slice'
        ];
    }

    public function slice(int $offset, int $limit): array
    {
        $cacheOptions = new CacheOptions(
            sprintf('wishlist.slice.%d.%d', $offset, $limit),
            5 * 60,
            ['wishlist.slice']
        );

        return $this->fetch(function () use ($offset, $limit) {
            return $this->repository->slice($offset, $limit);
        }, $cacheOptions);
    }

    public function contains(Wish $wish): bool
    {
        $cacheOptions = new CacheOptions(
            sprintf('wishlist.contains.%s', $wish->getId()->getId()),
            5 * 60
        );

        return $this->fetch(function () use ($wish) {
            return $this->repository->contains($wish);
        }, $cacheOptions);
    }

    public function containsId(WishId $wishId): bool
    {
        $cacheOptions = new CacheOptions(
            sprintf('wishlist.contains.%s', $wishId->getId()),
            5 * 60
        );

        return $this->fetch(function () use ($wishId) {
            return $this->repository->containsId($wishId);
        }, $cacheOptions);
    }

    public function count(): int
    {
        $cacheOptions = new CacheOptions(
            'wishlist.count',
            5 * 60
        );

        return $this->fetch(function () {
            return $this->repository->count();
        }, $cacheOptions);
    }

    public function getNextWishId(): WishId
    {
        return $this->repository->getNextWishId();
    }

    private function fetch(Closure $fetch, CacheOptions $options)
    {
        $cacheItem = $this->cache->getItem($options->getKey());
        $cacheItem->expiresAfter($options->getLifetime());

        if ($cacheItem->isHit()) {
            return $cacheItem->get();
        }

        $results = $fetch();
        $cacheItem->tag($options->getTags());
        $cacheItem->set($results);
        $this->cache->save($cacheItem);

        return $results;
    }
}
```

## File: `src/Infrastructure/Persistence/Doctrine/WishRepository.php`
```php
<?php

namespace Wishlist\Infrastructure\Persistence\Doctrine;

use Doctrine\ORM\EntityManagerInterface;
use Doctrine\ORM\EntityRepository;
use Doctrine\ORM\Tools\Pagination\Paginator;
use Wishlist\Domain\Exception\WishNotFoundException;
use Wishlist\Domain\Wish;
use Wishlist\Domain\WishId;
use Wishlist\Domain\WishRepositoryInterface;

final class WishRepository implements WishRepositoryInterface
{
    private $manager;
    /** @var EntityRepository */
    private $wishes;

    public function __construct(EntityManagerInterface $manager)
    {
        $this->manager = $manager;
        $this->wishes  = $this->manager->getRepository(Wish::class);
    }

    public function get(WishId $wishId): Wish
    {
        $wish = $this->wishes
            ->createQueryBuilder('wish')
            ->select(['wish', 'deposits'])
            ->leftJoin('wish.deposits', 'deposits')
            ->andWhere('wish.id = :id')
            ->setParameter('id', $wishId)
            ->getQuery()
            ->getSingleResult();

        if (null === $wish) {
            throw new WishNotFoundException($wishId);
        }

        return $wish;
    }

    public function put(Wish $wish)
    {
        $wish = $this->manager->merge($wish);
        $this->manager->persist($wish);
        $this->manager->flush();
    }

    public function slice(int $offset, int $limit): array
    {
        $query = $this->wishes
            ->createQueryBuilder('wish')
            ->select(['wish', 'deposits'])
            ->leftJoin('wish.deposits', 'deposits')
            ->orderBy('wish.createdAt', 'DESC')
            ->setFirstResult($offset)
            ->setMaxResults($limit)
            ->getQuery();

        return (new Paginator($query, true))
            ->getIterator()
            ->getArrayCopy();
    }

    public function contains(Wish $wish): bool
    {
        return $this->containsId($wish->getId());
    }

    public function containsId(WishId $wishId): bool
    {
        return null !== $this->manager
            ->createQueryBuilder()
            ->select('wish.id')
            ->from('Wishlist:Wish', 'wish')
            ->andWhere('wish.id = :id')
            ->setParameter('id', $wishId)
            ->getQuery()
            ->getSingleResult();
    }

    public function count(): int
    {
        return $this->manager
            ->createQueryBuilder()
            ->select('count(wish)')
            ->from('Wishlist:Wish', 'wish')
            ->getQuery()
            ->getSingleScalarResult();
    }

    public function getNextWishId(): WishId
    {
        return WishId::next();
    }
}
```

## File: `src/Infrastructure/Persistence/Doctrine/Fixture/LoadWishesData.php`
```php
<?php

namespace Wishlist\Infrastructure\Persistence\Doctrine\Fixture;

use DateTimeImmutable;
use Doctrine\Common\DataFixtures\AbstractFixture;
use Doctrine\Common\DataFixtures\OrderedFixtureInterface;
use Doctrine\Common\Persistence\ObjectManager;
use Faker\Factory;
use Money\Currency;
use Money\Money;
use Wishlist\Domain\Expense;
use Wishlist\Domain\Wish;
use Wishlist\Domain\WishId;
use Wishlist\Domain\WishName;

class LoadWishesData extends AbstractFixture implements OrderedFixtureInterface
{
    /**
     * {@inheritdoc}
     */
    public function load(ObjectManager $manager)
    {
        $faker = Factory::create();
        $currency = new Currency('USD');

        foreach (range(0, 19) as $wishIndex) {
            $seconds = $wishIndex * 10;
            $wish = new Wish(
                WishId::next(),
                new WishName($faker->sentence(3)),
                Expense::fromCurrencyAndScalars(
                    $currency,
                    $faker->numberBetween(10000, 50000),
                    $faker->numberBetween(10, 50),
                    $faker->numberBetween(0, 50)
                ),
                new DateTimeImmutable("now - {$seconds} seconds")
            );

            $wish->publish();

            foreach (range(0, $faker->numberBetween(5, 25)) as $depositIndex) {
                $wish->deposit(new Money($faker->numberBetween(60, 120), $currency));
            }

            $manager->persist($wish);
            $manager->flush();

            $this->addReference("wish-{$wishIndex}", $wish);
        }

        $unpublishedWish = new Wish(
            WishId::next(),
            new WishName($faker->sentence(3)),
            Expense::fromCurrencyAndScalars(
                $currency,
                $faker->numberBetween(10000, 50000),
                $faker->numberBetween(10, 50),
                $faker->numberBetween(0, 50)
            ),
            new DateTimeImmutable('now - 1 day')
        );

        $unpublishedWish->publish();
        $unpublishedWish->deposit(new Money(100, $currency));
        $unpublishedWish->unpublish();
        $manager->persist($unpublishedWish);
        $manager->flush();
        $this->addReference('wish-unpublished', $unpublishedWish);

        $almostFulfilledWish = new Wish(
            WishId::next(),
            new WishName($faker->sentence(3)),
            Expense::fromCurrencyAndScalars(
                $currency,
                45000,
                100,
                44900
            ),
            new DateTimeImmutable('now - 2 days')
        );

        $manager->persist($almostFulfilledWish);
        $manager->flush();
        $this->addReference('wish-almost-fulfilled', $almostFulfilledWish);

        $fulfilledWish = new Wish(
            WishId::next(),
            new WishName($faker->sentence(3)),
            Expense::fromCurrencyAndScalars(
                $currency,
                50000,
                100,
                49900
            ),
            new DateTimeImmutable('now - 5 days')
        );

        $fulfilledWish->publish();
        $fulfilledWish->deposit(new Money(100, $currency));
        $manager->persist($fulfilledWish);
        $manager->flush();
        $this->addReference('wish-fulfilled', $fulfilledWish);
    }

    /**
     * Get the order of this fixture
     *
     * @return integer
     */
    public function getOrder()
    {
        return 1;
    }
}
```

## File: `src/Infrastructure/Persistence/Doctrine/Type/DepositIdType.php`
```php
<?php

namespace Wishlist\Infrastructure\Persistence\Doctrine\Type;

use Doctrine\DBAL\Platforms\AbstractPlatform;
use Doctrine\DBAL\Types\ConversionException;
use InvalidArgumentException;
use Ramsey\Uuid\Doctrine\UuidType;
use Wishlist\Domain\DepositId;

class DepositIdType extends UuidType
{
    const NAME = 'deposit_id';

    public function convertToPHPValue($value, AbstractPlatform $platform)
    {
        if (empty($value)) {
            return null;
        }

        if ($value instanceof DepositId) {
            return $value;
        }

        try {
            $uuid = DepositId::fromString($value);
        } catch (InvalidArgumentException $exception) {
            throw ConversionException::conversionFailed($value, static::NAME);
        }

        return $uuid;
    }

    public function convertToDatabaseValue($value, AbstractPlatform $platform)
    {
        if (empty($value)) {
            return null;
        }

        if ($value instanceof DepositId) {
            return (string) $value;
        }

        throw ConversionException::conversionFailed($value, static::NAME);
    }
}
```

## File: `src/Infrastructure/Persistence/Doctrine/Type/WishIdType.php`
```php
<?php

namespace Wishlist\Infrastructure\Persistence\Doctrine\Type;

use Doctrine\DBAL\Platforms\AbstractPlatform;
use Doctrine\DBAL\Types\ConversionException;
use InvalidArgumentException;
use Ramsey\Uuid\Doctrine\UuidType;
use Wishlist\Domain\WishId;

class WishIdType extends UuidType
{
    const NAME = 'wish_id';

    public function convertToPHPValue($value, AbstractPlatform $platform)
    {
        if (empty($value)) {
            return null;
        }

        if ($value instanceof WishId) {
            return $value;
        }

        try {
            $uuid = WishId::fromString($value);
        } catch (InvalidArgumentException $exception) {
            throw ConversionException::conversionFailed($value, static::NAME);
        }

        return $uuid;
    }

    public function convertToDatabaseValue($value, AbstractPlatform $platform)
    {
        if (empty($value)) {
            return null;
        }

        if ($value instanceof WishId) {
            return (string) $value;
        }

        throw ConversionException::conversionFailed($value, static::NAME);
    }
}
```

## File: `src/Infrastructure/Persistence/Memory/WishRepository.php`
```php
<?php

namespace Wishlist\Infrastructure\Persistence\Memory;

use Webmozart\Assert\Assert;
use Wishlist\Domain\Exception\WishNotFoundException;
use Wishlist\Domain\Wish;
use Wishlist\Domain\WishId;
use Wishlist\Domain\WishRepositoryInterface;

class WishRepository implements WishRepositoryInterface
{
    private $wishes = [];

    public function __construct(array $wishes = [])
    {
        Assert::allIsInstanceOf($wishes, Wish::class);

        $this->wishes = $wishes;
    }

    public function get(WishId $wishId): Wish
    {
        if (!$this->containsId($wishId)) {
            throw new WishNotFoundException($wishId);
        }

        return $this->wishes[$wishId->getId()];
    }

    public function put(Wish $wish)
    {
        $this->wishes[$wish->getId()->getId()] = $wish;
    }

    public function slice(int $offset, int $limit): array
    {
        return array_slice($this->wishes, $offset, $limit, true);
    }

    public function contains(Wish $wish): bool
    {
        return in_array($wish, $this->wishes, true);
    }

    public function containsId(WishId $wishId): bool
    {
        return array_key_exists($wishId->getId(), $this->wishes);
    }

    public function count(): int
    {
        return count($this->wishes);
    }

    public function getNextWishId(): WishId
    {
        return WishId::next();
    }
}
```

## File: `src/Infrastructure/Validation/ConstraintViolationListTransformer.php`
```php
<?php

namespace Wishlist\Infrastructure\Validation;

use Symfony\Component\Validator\ConstraintViolationInterface;
use Symfony\Component\Validator\ConstraintViolationListInterface;

class ConstraintViolationListTransformer implements ConstraintViolationListTransformerInterface
{
    public function toArray(ConstraintViolationListInterface $violations): array
    {
        $result = [];

        /** @var ConstraintViolationInterface $violation */
        foreach ($violations as $violation) {
            $property = trim($violation->getPropertyPath(), '[]');

            $result[$property] = $violation->getMessage();
        }

        return $result;
    }
}
```

## File: `src/Infrastructure/Validation/ConstraintViolationListTransformerInterface.php`
```php
<?php

namespace Wishlist\Infrastructure\Validation;

use Symfony\Component\Validator\ConstraintViolationListInterface;

interface ConstraintViolationListTransformerInterface
{
    public function toArray(ConstraintViolationListInterface $violations): array;
}
```

## File: `tests/Application/WishlistTest.php`
```php
<?php

namespace Wishlist\Tests\Application;

use Money\Currency;
use Money\Money;
use Wishlist\Application\Dto\ListWishDto;
use Wishlist\Application\Dto\NewWishDto;
use Wishlist\Application\Wishlist;
use PHPUnit\Framework\TestCase;
use Wishlist\Domain\Expense;
use Wishlist\Domain\Wish;
use Wishlist\Domain\WishId;
use Wishlist\Domain\WishName;
use Wishlist\Infrastructure\Persistence\Memory\WishRepository;

class WishlistTest extends TestCase
{
    /**
     * @var array|WishId[]
     */
    private $wishIds = [];
    private $wishIdsNumber = 0;

    public function setUp()
    {
        parent::setUp();

        foreach (range(0, 15) as $index) {
            $this->wishIds[] = WishId::next();
        }

        $this->wishIdsNumber = count($this->wishIds);
    }

    public function testGetWishesByPage()
    {
        $page = 2;
        $limit = 5;
        $repository = new WishRepository($this->createWishes());
        $wishlist = new Wishlist($repository, new Currency('USD'));

        $wishes = $wishlist->getWishesByPage($page, $limit);

        $expectedIds = array_slice($this->wishIds, $page * $limit, $limit);
        static::assertEquals($expectedIds, array_keys($wishes));

        foreach ($wishes as $wish) {
            static::assertInstanceOf(ListWishDto::class, $wish);
        }
    }

    public function testAddNewWish()
    {
        $repository = new WishRepository();
        $wishlist = new Wishlist($repository, new Currency('USD'));
        $dto = new NewWishDto();
        $dto->name = 'Foo Bar';
        $dto->price = 1000;
        $dto->fee = 10;
        $dto->initialFund = 10;
        $dto->isPublished = true;

        $wishId = $wishlist->addNewWish($dto);
        $typedWishId = WishId::fromString($wishId);

        static::assertTrue($repository->containsId($typedWishId));

        $wish = $repository->get($typedWishId);
        static::assertEquals($dto->name, $wish->getName());
        static::assertEquals($dto->price, $wish->getPrice()->getAmount());
        static::assertEquals($dto->fee, $wish->getFee()->getAmount());
        static::assertEquals($dto->initialFund, $wish->getFund()->getAmount());
        static::assertEquals($dto->isPublished, $wish->isPublished());
    }

    public function testDeposit()
    {
        $repository = new WishRepository($this->createWishes());
        $repositoryCapacity = $repository->count();
        $wishlist = new Wishlist($repository, new Currency('USD'));

        $deposit = $wishlist->deposit($this->wishIds[0]->getId(), 100);

        static::assertSame($repositoryCapacity, $repository->count());
        static::assertSame(
            $deposit->depositId,
            $repository->get($this->wishIds[0])->getDeposits()[0]->getId()->getId()
        );

        static::assertEquals(110, $repository->get($this->wishIds[0])->getFund()->getAmount());
    }

    public function testWithdraw()
    {
        $repository = new WishRepository($this->createWishes());
        $repositoryCapacity = $repository->count();
        $wishlist = new Wishlist($repository, new Currency('USD'));
        $wishId = $this->wishIds[0]->getId();
        $deposit = $wishlist->deposit($wishId, 25);

        $amount = $wishlist->withdraw($wishId, $deposit->depositId);

        static::assertSame($repositoryCapacity, $repository->count());
        static::assertTrue($amount->equals($repository->get($this->wishIds[0])->getFund()));
        static::assertEquals(10, $amount->getAmount());
    }

    public function testUnpublish()
    {
        $repository = new WishRepository($this->createWishes());
        $repositoryCapacity = $repository->count();
        $wishlist = new Wishlist($repository, new Currency('USD'));

        $wishlist->unpublish($this->wishIds[0]->getId());

        static::assertSame($repositoryCapacity, $repository->count());
        static::assertFalse($repository->get($this->wishIds[0])->isPublished());
    }

    public function testPublish()
    {
        $repository = new WishRepository($this->createWishes());
        $repositoryCapacity = $repository->count();
        $wishlist = new Wishlist($repository, new Currency('USD'));

        $wishlist->unpublish($this->wishIds[0]->getId());
        $wishlist->publish($this->wishIds[0]->getId());

        static::assertSame($repositoryCapacity, $repository->count());
        static::assertTrue($repository->get($this->wishIds[0])->isPublished());
    }

    private function createWishes(): array
    {
        $wishes = [];

        foreach (range(0, $this->wishIdsNumber - 1) as $index) {
            $wish = new Wish(
                $this->wishIds[$index],
                new WishName('Qux'),
                Expense::fromCurrencyAndScalars(
                    new Currency('USD'),
                    ($index + 1) * 100,
                    ($index + 1) * 5,
                    ($index + 1) * 10
                )
            );

            $wish->publish();

            $wishes[$this->wishIds[$index]->getId()] = $wish;
        }

        return $wishes;
    }
}
```

## File: `tests/Domain/DepositTest.php`
```php
<?php

namespace Wishlist\Tests\Domain;

use Mockery;
use Money\Currency;
use Money\Money;
use PHPUnit\Framework\TestCase;
use Wishlist\Domain\Deposit;
use Wishlist\Domain\DepositId;
use Wishlist\Domain\Wish;

class DepositTest extends TestCase
{
    /**
     * @expectedException \InvalidArgumentException
     */
    public function testDepositAmountMustNotBeZero()
    {
        $wish = Mockery::mock(Wish::class);
        $amount = new Money(0, new Currency('USD'));

        new Deposit(DepositId::next(), $wish, $amount);
    }
}
```

## File: `tests/Domain/ExpenseTest.php`
```php
<?php

namespace Wishlist\Tests\Domain;

use Money\Currency;
use Money\Money;
use Wishlist\Domain\Expense;
use PHPUnit\Framework\TestCase;

class ExpenseTest extends TestCase
{
    /**
     * @expectedException \InvalidArgumentException
     * @dataProvider nonsensePriceDataProvider
     */
    public function testPriceAndFeeMustBePositiveNumber($price, $fee, $initialFund)
    {
        Expense::fromCurrencyAndScalars(new Currency('USD'), $price, $fee, $initialFund);
    }

    public function nonsensePriceDataProvider()
    {
        return [
            'Price must be greater than zero' => [0, 0, 0],
            'Fee must be greater than zero' => [1, 0, 0],
            'Price must be positive' => [-1, -1, 0],
            'Fee must be positive' => [1, -1, 0],
            'Initial fund must be positive' => [2, 1, -1],
        ];
    }

    /**
     * @expectedException \InvalidArgumentException
     */
    public function testFeeMustBeLessThanPrice()
    {
        Expense::fromCurrencyAndScalars(new Currency('USD'), 100, 150);
    }

    /**
     * @expectedException \InvalidArgumentException
     */
    public function testInitialFundMustBeLessThanPrice()
    {
        Expense::fromCurrencyAndScalars(new Currency('USD'), 100, 50, 150);
    }

    /**
     * @expectedException \InvalidArgumentException
     */
    public function testNewPriceMustBeOfTheSameCurrency()
    {
        $expense = Expense::fromCurrencyAndScalars(new Currency('USD'), 100, 50, 25);

        $expense->changePrice(new Money(200, new Currency('RUB')));
    }

    public function testChangePriceMustReturnANewInstance()
    {
        $expense = Expense::fromCurrencyAndScalars(new Currency('USD'), 100, 50, 25);

        $actual = $expense->changePrice(new Money(200, new Currency('USD')));

        static::assertNotSame($expense, $actual);
        static::assertEquals(200, $actual->getPrice()->getAmount());
    }

    /**
     * @expectedException \InvalidArgumentException
     */
    public function testNewFeeMustBeOfTheSameCurrency()
    {
        $expense = Expense::fromCurrencyAndScalars(new Currency('USD'), 100, 50, 25);

        $expense->changeFee(new Money(200, new Currency('RUB')));
    }

    public function testChangeFeeMustReturnANewInstance()
    {
        $expense = Expense::fromCurrencyAndScalars(new Currency('USD'), 100, 10, 25);

        $actual = $expense->changeFee(new Money(20, new Currency('USD')));

        static::assertNotSame($expense, $actual);
        static::assertEquals(20, $actual->getFee()->getAmount());
    }
}
```

## File: `tests/Domain/IdentityTest.php`
```php
<?php

namespace Wishlist\Tests\Domain;

use Wishlist\Domain\DepositId;
use Wishlist\Domain\WishId;
use PHPUnit\Framework\TestCase;

class IdentityTest extends TestCase
{
    public function testFromValidString()
    {
        $string = '550e8400-e29b-41d4-a716-446655440000';
        $wishId = WishId::fromString($string);

        static::assertInstanceOf(WishId::class, $wishId);
        static::assertEquals($string, $wishId->getId());
        static::assertEquals($string, (string) $wishId);
    }

    public function testEquality()
    {
        $string = '550e8400-e29b-41d4-a716-446655440000';
        $wishIdOne = WishId::fromString($string);
        $wishIdTwo = WishId::fromString($string);
        $wishIdThree = WishId::next();
        $depositId = DepositId::fromString('550e8400-e29b-41d4-a716-446655440000');

        static::assertTrue($wishIdOne->equalTo($wishIdTwo));
        static::assertFalse($wishIdTwo->equalTo($wishIdThree));
        static::assertFalse($wishIdOne->equalTo($depositId));
    }
}
```

## File: `tests/Domain/WishNameTest.php`
```php
<?php

namespace Wishlist\Tests\Domain;

use Wishlist\Domain\WishName;
use PHPUnit\Framework\TestCase;

class WishNameTest extends TestCase
{
    /**
     * @expectedException \InvalidArgumentException
     */
    public function testShouldNotCreateWithEmptyString()
    {
        new WishName('');
    }

    public function testGetValueShouldReturnTheName()
    {
        $expected = 'A bucket of candies';
        $name = new WishName($expected);

        static::assertEquals($expected, $name->getValue());
        static::assertEquals($expected, (string) $name);
    }
}
```

## File: `tests/Domain/WishTest.php`
```php
<?php

namespace Wishlist\Tests\Domain;

use DateInterval;
use DateTimeImmutable;
use Money\Currency;
use Money\Money;
use Symfony\Bundle\FrameworkBundle\Tests\TestCase;
use Wishlist\Domain\DepositId;
use Wishlist\Domain\Expense;
use Wishlist\Domain\Wish;
use Wishlist\Domain\WishId;
use Wishlist\Domain\WishName;

class WishTest extends TestCase
{
    public function testCreatedAndUpdatedAtMustBeEqualUponCreation()
    {
        $wish = $this->createWishWithEmptyFund();
        $diff = $wish->getCreatedAt()->diff($wish->getUpdatedAt());

        static::assertNotSame($wish->getCreatedAt(), $wish->getUpdatedAt());
        static::assertTrue($diff->y === 0);
        static::assertTrue($diff->m === 0);
        static::assertTrue($diff->d === 0);
        static::assertTrue($diff->h === 0);
        static::assertTrue($diff->i === 0);
        static::assertTrue($diff->s === 0);
    }

    /**
     * @expectedException \Wishlist\Domain\Exception\DepositIsTooSmallException
     */
    public function testMustDeclineDepositIfItIsLessThanFee()
    {
        $wish = $this->createWishWithPriceAndFee(1000, 100);
        $wish->publish();

        $wish->deposit(new Money(50, new Currency('USD')));
    }

    public function testExtraDepositMustFulfillTheWish()
    {
        $wish = $this->createWishWithPriceAndFund(1000, 900);
        $wish->publish();

        $wish->deposit(new Money(150, new Currency('USD')));

        static::assertTrue($wish->isFulfilled());
    }

    /**
     * @expectedException \Wishlist\Domain\Exception\WishIsUnpublishedException
     */
    public function testMustNotDepositWhenUnpublished()
    {
        $wish = $this->createWishWithEmptyFund();
        $wish->deposit(new Money(100, new Currency('USD')));
    }

    /**
     * @expectedException \Wishlist\Domain\Exception\WishIsFulfilledException
     */
    public function testMustNotDepositWhenFulfilled()
    {
        $fulfilled = $this->createWishWithPriceAndFund(500, 450);
        $fulfilled->publish();

        $fulfilled->deposit(new Money(100, new Currency('USD')));
        $fulfilled->deposit(new Money(100, new Currency('USD')));
    }

    /**
     * @expectedException \Wishlist\Domain\Exception\WishIsUnpublishedException
     */
    public function testMustNotWithdrawIfUnpublished()
    {
        $wish = $this->createWishWithPriceAndFund(500, 0);
        $wish->publish();
        $deposit = $wish->deposit(new Money(100, new Currency('USD')));
        $wish->unpublish();

        $wish->withdraw($deposit->getId());
    }

    /**
     * @expectedException \Wishlist\Domain\Exception\WishIsFulfilledException
     */
    public function testMustNotWithdrawIfFulfilled()
    {
        $wish = $this->createWishWithPriceAndFund(500, 450);
        $wish->publish();
        $deposit = $wish->deposit(new Money(100, new Currency('USD')));

        $wish->withdraw($deposit->getId());
    }

    /**
     * @expectedException \Wishlist\Domain\Exception\DepositDoesNotExistException
     */
    public function testWithdrawMustThrowOnNonExistentId()
    {
        $wish = $this->createWishWithEmptyFund();
        $wish->publish();

        $wish->withdraw(DepositId::next());
    }

    public function testDepositShouldAddDepositToInternalCollection()
    {
        $wish = $this->createWishWithEmptyFund();
        $wish->publish();
        $depositMoney = new Money(150, new Currency('USD'));

        $wish->deposit($depositMoney);

        $deposits = $wish->getDeposits();
        static::assertCount(1, $deposits);
        static::assertArrayHasKey(0, $deposits);

        $deposit = $deposits[0];
        static::assertTrue($deposit->getMoney()->equals($depositMoney));
        static::assertSame($wish, $deposit->getWish());
    }

    public function testWithdrawShouldRemoveDepositFromInternalCollection()
    {
        $wish = $this->createWishWithEmptyFund();
        $wish->publish();
        $wish->deposit(new Money(150, new Currency('USD')));

        $wish->withdraw($wish->getDeposits()[0]->getId());

        static::assertCount(0, $wish->getDeposits());
    }

    /**
     * @expectedException \InvalidArgumentException
     */
    public function testDepositAndPriceCurrenciesMustMatch()
    {
        $wish = $this->createWishWithEmptyFund();
        $wish->publish();

        $wish->deposit(new Money(125, new Currency('RUB')));
    }

    public function testSurplusFundsMustBe100()
    {
        $wish = $this->createWishWithPriceAndFund(500, 300);
        $wish->publish();

        $wish->deposit(new Money(100, new Currency('USD')));
        $wish->deposit(new Money(200, new Currency('USD')));

        $expected = new Money(100, new Currency('USD'));
        static::assertTrue($wish->calculateSurplusFunds()->equals($expected));
    }

    public function testSurplusFundsMustBeZero()
    {
        $wish = $this->createWishWithPriceAndFund(500, 250);
        $wish->publish();

        $wish->deposit(new Money(100, new Currency('USD')));

        $expected = new Money(0, new Currency('USD'));
        static::assertTrue($wish->calculateSurplusFunds()->equals($expected));
    }

    public function testFulfillmentDatePredictionBasedOnFee()
    {
        $price = 1500;
        $fee = 20;
        $wish = $this->createWishWithPriceAndFee($price, $fee);
        $daysToGo = ceil($price / $fee);

        $expected = (new DateTimeImmutable())->add(new DateInterval("P{$daysToGo}D"));

        static::assertEquals(
            $expected->getTimestamp(),
            $wish->predictFulfillmentDateBasedOnFee()->getTimestamp()
        );
    }

    public function testFulfillmentDatePredictionBasedOnFund()
    {
        $price = 1500;
        $fund = 250;
        $fee = 25;
        $wish = $this->createWish($price, $fee, $fund);
        $daysToGo = ceil(($price - $fund) / $fee);

        $expected = (new DateTimeImmutable())->add(new DateInterval("P{$daysToGo}D"));

        static::assertEquals(
            $expected->getTimestamp(),
            $wish->predictFulfillmentDateBasedOnFund()->getTimestamp()
        );
    }

    public function testPublishShouldPublishTheWish()
    {
        $wish = $this->createWishWithEmptyFund();
        $updatedAt = $wish->getUpdatedAt();

        $wish->publish();

        static::assertTrue($wish->isPublished());
        static::assertNotSame($updatedAt, $wish->getUpdatedAt());
    }

    public function testUnpublishShouldUnpublishTheWish()
    {
        $wish = $this->createWishWithEmptyFund();
        $updatedAt = $wish->getUpdatedAt();

        $wish->unpublish();

        static::assertFalse($wish->isPublished());
        static::assertNotSame($updatedAt, $wish->getUpdatedAt());
    }

    public function testChangePrice()
    {
        $wish = $this->createWishWithPriceAndFee(1000, 10);
        $expected = new Money(1500, new Currency('USD'));
        $updatedAt = $wish->getUpdatedAt();

        static::assertSame($updatedAt, $wish->getUpdatedAt());

        $wish->changePrice($expected);

        static::assertTrue($wish->getPrice()->equals($expected));
        static::assertNotSame($updatedAt, $wish->getUpdatedAt());
    }

    public function testChangeFee()
    {
        $wish = $this->createWishWithPriceAndFee(1000, 10);
        $expected = new Money(50, new Currency('USD'));
        $updatedAt = $wish->getUpdatedAt();

        static::assertSame($updatedAt, $wish->getUpdatedAt());

        $wish->changeFee($expected);

        static::assertTrue($wish->getFee()->equals($expected));
        static::assertNotSame($updatedAt, $wish->getUpdatedAt());
    }

    public function testGetName()
    {
        $wish = $this->createWishWithName('foo');

        static::assertEquals('foo', $wish->getName());
    }

    private function createWishWithName(string $name): Wish
    {
        return new Wish(
            WishId::next(),
            new WishName($name),
            Expense::fromCurrencyAndScalars(
                new Currency('USD'),
                1000,
                100
            )
        );
    }

    private function createWishWithEmptyFund(): Wish
    {
        return new Wish(
            WishId::next(),
            new WishName('Bicycle'),
            Expense::fromCurrencyAndScalars(
                new Currency('USD'),
                1000,
                100
            )
        );
    }

    private function createWishWithPriceAndFund(int $price, int $fund): Wish
    {
        return new Wish(
            WishId::next(),
            new WishName('Bicycle'),
            Expense::fromCurrencyAndScalars(
                new Currency('USD'),
                $price,
                10,
                $fund
            )
        );
    }

    private function createWishWithPriceAndFee(int $price, int $fee): Wish
    {
        return new Wish(
            WishId::next(),
            new WishName('Bicycle'),
            Expense::fromCurrencyAndScalars(
                new Currency('USD'),
                $price,
                $fee
            )
        );
    }

    private function createWish(int $price, int $fee, int $fund): Wish
    {
        return new Wish(
            WishId::next(),
            new WishName('Bicycle'),
            Expense::fromCurrencyAndScalars(
                new Currency('USD'),
                $price,
                $fee,
                $fund
            )
        );
    }
}
```

## File: `tests/Http/Controller/WishlistControllerTest.php`
```php
<?php

namespace Wishlist\Tests\Http\Controller;

use Doctrine\Common\DataFixtures\ReferenceRepository;
use Liip\FunctionalTestBundle\Test\WebTestCase;
use Symfony\Component\BrowserKit\Client;
use Symfony\Component\DomCrawler\Crawler;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\RouterInterface;
use Symfony\Component\Translation\TranslatorInterface;
use Wishlist\Domain\Wish;
use Wishlist\Infrastructure\Persistence\Doctrine\Fixture\LoadWishesData;

class WishlistControllerTest extends WebTestCase
{
    /**
     * @var array|Wish[]
     */
    private $fixtures;

    /**
     * @var ReferenceRepository
     */
    private $references;

    /**
     * @var RouterInterface
     */
    private $router;

    /**
     * @var TranslatorInterface
     */
    private $translator;

    public function setUp()
    {
        parent::setUp();

        $executor = $this->loadFixtures([
            LoadWishesData::class,
        ]);

        $this->references = $executor->getReferenceRepository();
        $this->fixtures = $this->references->getReferences();

        $container = $this->getContainer();
        $this->router = $container->get('router');
        $this->translator = $container->get('translator');
    }

    public function testIndexActionShouldShowVueTemplate()
    {
        $client = $this->makeClient();

        $crawler = $client->request('GET', '/wishes');

        $this->assertStatusCode(Response::HTTP_OK, $client);
        $this->assertThereIsOnlyOneWishlist($crawler);
    }

    private function assertThereIsOnlyOneWishlist(Crawler $crawler): void
    {
        static::assertEquals(1, $crawler->filter('.js-wishlist')->count());
    }

    /**
     * @param array $parameters
     * @dataProvider queryParametersDataProvider
     */
    public function testIndexActionShouldReturnJsonOnAjaxCall(array $parameters)
    {
        $limit = $parameters['limit'] ?? 10;
        $client = $this->makeClient();

        $client->request(
            'GET',
            '/wishes',
            $parameters,
            [],
            ['HTTP_X-Requested-With' => 'XMLHttpRequest']
        );

        $response = $client->getResponse();

        $this->assertStatusCode(Response::HTTP_OK, $client);
        static::assertInstanceOf(JsonResponse::class, $response);

        $actual = $this->parseJson($response);

        foreach (['wishes', 'pagination'] as $key) {
            static::assertArrayHasKey($key, $actual);
        }

        static::assertCount($limit, $actual['wishes']);

        $paginationKeys = [
            'page',
            'limit',
            'startIndex',
            'endIndex',
            'total',
            'totalPages'
        ];

        foreach ($paginationKeys as $key) {
            static::assertArrayHasKey($key, $actual['pagination']);
        }

        $this->assertOrderedByDate(array_column($actual['wishes'], 'id'), $limit);
    }

    public function queryParametersDataProvider()
    {
        return [
            'Should show latest 10 wishes' => [[]],
            'Should also show the same (latest) 10 wishes' => [['page' => 1]],
            'Should show given number of wishes on the given page' => [['page' => 1, 'limit' => 15]]
        ];
    }

    private function assertOrderedByDate($wishIds, $limit = 10)
    {
        static::assertEquals($this->getFixtureWishIds(0, $limit), $wishIds);
    }

    private function getFixtureWishIds(int $offset = null, int $limit = null): array
    {
        $fixtures = $this->fixtures;

        usort($fixtures, function (Wish $one, Wish $two) {
            return $one->getCreatedAt() < $two->getCreatedAt() ? 1 : -1;
        });

        $ids = array_map(function (Wish $wish) {
            return $wish->getId()->getId();
        }, $fixtures);

        if (null === $offset) {
            return $ids;
        }

        return array_slice($ids, $offset, $limit, true);
    }

    public function testPublishShouldReturn404IfWishDoesNotExist()
    {
        $client = $this->makeClient();

        $this->sendPublishRequest($client, 'nonsense');

        $this->assertStatusCode(Response::HTTP_NOT_FOUND, $client);
    }

    public function testPublishShouldPublishTheWish()
    {
        $client = $this->makeClient();
        $fixtureKey = 'wish-unpublished';
        $wishId = $this->fixtures[$fixtureKey]->getId()->getId();

        $this->sendPublishRequest($client, $wishId);
        $response = $client->getResponse();

        $this->assertStatusCode(Response::HTTP_OK, $client);
        static::assertInstanceOf(JsonResponse::class, $response);
        static::assertEquals(
            [
                'url' => $this->router->generate('wishlist.wish.unpublish', compact('wishId')),
                'label' => $this->translator->trans('wishlist.table.unpublish'),
                'published' => true
            ],
            $this->parseJson($response)
        );

        static::assertTrue($this->getFixtureReference($fixtureKey)->isPublished());
    }

    public function testUnpublishShouldReturn404IfWishDoesNotExist()
    {
        $client = $this->makeClient();

        $this->sendUnpublishRequest($client, 'nonsense');

        $this->assertStatusCode(Response::HTTP_NOT_FOUND, $client);
    }

    public function testUnpublishShouldUnpublishTheWish()
    {
        $client = $this->makeClient();
        $fixtureKey = 'wish-0';
        $wishId = $this->fixtures[$fixtureKey]->getId()->getId();

        $this->sendUnpublishRequest($client, $wishId);
        $response = $client->getResponse();

        $this->assertStatusCode(Response::HTTP_OK, $client);
        static::assertInstanceOf(JsonResponse::class, $response);
        static::assertEquals(
            [
                'url' => $this->router->generate('wishlist.wish.publish', compact('wishId')),
                'label' => $this->translator->trans('wishlist.table.publish'),
                'published' => false
            ],
            $this->parseJson($response)
        );

        static::assertFalse($this->getFixtureReference($fixtureKey)->isPublished());
    }

    private function sendPublishRequest(Client $client, string $wishId): void
    {
        $client->request(
            'PUT',
            $this->router->generate('wishlist.wish.publish', compact('wishId')),
            [],
            [],
            ['HTTP_X-Requested-With' => 'XMLHttpRequest',]
        );
    }

    private function sendUnpublishRequest(Client $client, string $wishId): void
    {
        $client->request(
            'PUT',
            $this->router->generate('wishlist.wish.unpublish', compact('wishId')),
            [],
            [],
            ['HTTP_X-Requested-With' => 'XMLHttpRequest',]
        );
    }

    public function testSimpleDeposit()
    {
        $client = $this->makeClient();

        $this->sendDepositRequest(
            $client,
            $this->fixtures['wish-0']->getId()->getId(),
            335
        );

        $response = $client->getResponse();

        $this->assertStatusCode(Response::HTTP_OK, $client);
        static::assertInstanceOf(JsonResponse::class, $response);

        $json = $this->parseJson($response);
        static::assertArrayHasKey('success', $json);
        static::assertTrue($json['success']);
        static::assertArrayHasKey('deposit', $json);

        $depositKeys = [
            'id',
            'amount',
            'currency',
            'createdAt'
        ];

        foreach ($depositKeys as $key) {
            static::assertArrayHasKey($key, $json['deposit']);
        }
    }

    public function testDepositShouldFailValidation()
    {
        $client = $this->makeClient();

        $this->sendDepositRequest(
            $client,
            $this->fixtures['wish-0']->getId()->getId(),
            'nonsense'
        );

        $response = $client->getResponse();
        $json = $this->parseJson($response);
        $this->assertStatusCode(Response::HTTP_UNPROCESSABLE_ENTITY, $client);
        static::assertInstanceOf(JsonResponse::class, $response);
        static::assertArrayHasKey('success', $json);
        static::assertFalse($json['success']);
        static::assertArrayHasKey('violations', $json);
        static::assertArrayHasKey('amount', $json['violations']);
    }

    public function testMustNotDepositToUnpublishedWish()
    {
        $client = $this->makeClient();

        $this->sendDepositRequest(
            $client,
            $this->fixtures['wish-unpublished']->getId()->getId(),
            123
        );

        $response = $client->getResponse();
        $json = $this->parseJson($response);
        $this->assertStatusCode(Response::HTTP_UNPROCESSABLE_ENTITY, $client);
        static::assertInstanceOf(JsonResponse::class, $response);
        static::assertArrayHasKey('success', $json);
        static::assertFalse($json['success']);
        static::assertArrayHasKey('message', $json);
    }

    public function testMustNotDepositToFulfilledWish()
    {
        $client = $this->makeClient();

        $this->sendDepositRequest(
            $client,
            $this->fixtures['wish-fulfilled']->getId()->getId(),
            999
        );

        $response = $client->getResponse();
        $json = $this->parseJson($response);
        $this->assertStatusCode(Response::HTTP_UNPROCESSABLE_ENTITY, $client);
        static::assertInstanceOf(JsonResponse::class, $response);
        static::assertArrayHasKey('success', $json);
        static::assertFalse($json['success']);
        static::assertArrayHasKey('message', $json);
    }

    private function sendDepositRequest(Client $client, string $wishId, $amount): void
    {
        $client->request(
            'POST',
            $this->router->generate('wishlist.wish.deposit', compact('wishId')),
            compact('amount'),
            [],
            ['HTTP_X-Requested-With' => 'XMLHttpRequest']
        );
    }

    public function testMustNotWithdrawUnpublishedWish()
    {
        $client = $this->makeClient();
        $wish = $this->fixtures['wish-unpublished'];
        $depositId = $wish->getDeposits()[0]->getId()->getId();

        $this->sendWithdrawRequest($client, $wish->getId()->getId(), $depositId);

        $response = $client->getResponse();
        $json = $this->parseJson($response);
        $this->assertStatusCode(Response::HTTP_UNPROCESSABLE_ENTITY, $client);
        static::assertInstanceOf(JsonResponse::class, $response);
        static::assertArrayHasKey('success', $json);
        static::assertFalse($json['success']);
        static::assertArrayHasKey('message', $json);
    }

    public function testMustNotWithdrawFulfilledWish()
    {
        $client = $this->makeClient();
        $wish = $this->fixtures['wish-fulfilled'];
        $depositId = $wish->getDeposits()[0]->getId()->getId();

        $this->sendWithdrawRequest($client, $wish->getId()->getId(), $depositId);

        $response = $client->getResponse();
        $json = $this->parseJson($response);
        $this->assertStatusCode(Response::HTTP_UNPROCESSABLE_ENTITY, $client);
        static::assertInstanceOf(JsonResponse::class, $response);
        static::assertArrayHasKey('success', $json);
        static::assertFalse($json['success']);
        static::assertArrayHasKey('message', $json);
    }

    public function testSimpleWithdraw()
    {
        $client = $this->makeClient();
        $wish = $this->fixtures['wish-0'];
        $wishId = $wish->getId()->getId();
        $depositId = $wish->getDeposits()[0]->getId()->getId();

        $this->sendWithdrawRequest($client, $wishId, $depositId);

        $response = $client->getResponse();
        $json = $this->parseJson($response);
        $this->assertStatusCode(Response::HTTP_OK, $client);
        static::assertInstanceOf(JsonResponse::class, $response);
        static::assertArrayHasKey('success', $json);
        static::assertTrue($json['success']);
    }

    private function sendWithdrawRequest(Client $client, string $wishId, string $depositId): void
    {
        $client->request(
            'DELETE',
            $this->router->generate(
                'wishlist.wish.withdraw',
                compact('wishId', 'depositId')
            ),
            [],
            [],
            ['HTTP_X-Requested-With' => 'XMLHttpRequest']
        );
    }

    /**
     * @param Response $response
     *
     * @return mixed
     */
    private function parseJson(Response $response)
    {
        return json_decode($response->getContent(), true);
    }

    /**
     * @param string $name
     *
     * @return object|Wish
     */
    private function getFixtureReference(string $name): Wish
    {
        return $this->references->getReference($name);
    }
}
```

## File: `tests/Infrastructure/Persistence/Memory/WishRepositoryTest.php`
```php
<?php

namespace Wishlist\Tests\Infrastructure\Persistence\Memory;

use Money\Currency;
use Wishlist\Domain\Expense;
use Wishlist\Domain\Wish;
use Wishlist\Domain\WishId;
use Wishlist\Domain\WishName;
use Wishlist\Domain\WishRepositoryInterface;
use Wishlist\Infrastructure\Persistence\Memory\WishRepository;
use PHPUnit\Framework\TestCase;

class WishRepositoryTest extends TestCase
{
    /**
     * @expectedException \InvalidArgumentException
     */
    public function testConstructorShouldAcceptWishesOnly()
    {
        new WishRepository([
            'foo',
            'bar',
        ]);
    }

    /**
     * @expectedException \Wishlist\Domain\Exception\WishNotFoundException
     */
    public function testGetShouldThrowOnNonExistentId()
    {
        $repository = new WishRepository();
        $repository->get(WishId::next());
    }

    public function testPutShouldSaveToInternalArray()
    {
        $repository = new WishRepository();
        $wishId = WishId::next();

        $repository->put(new Wish(
            $wishId,
            new WishName('Qux'),
            Expense::fromCurrencyAndScalars(
                new Currency('USD'),
                1000,
                20,
                400
            )
        ));

        static::assertEquals(1, $repository->count());
        static::assertSame($wishId, $repository->get($wishId)->getId());
    }

    public function testSliceShouldReturnAPortion()
    {
        $repository = new WishRepository();
        $wishes = $this->createWishesIndexedById($repository, 5);

        static::assertSame(
            array_slice($wishes, 1, 3, true),
            $repository->slice(1, 3)
        );
    }

    public function testHassersShouldSearchInInternalArray()
    {
        $repository = new WishRepository();
        $wishes = $this->createWishesIndexedByNumber($repository, 2);
        $anotherWish = $this->createWish();

        static::assertTrue($repository->contains($wishes[0]));
        static::assertTrue($repository->contains($wishes[1]));
        static::assertTrue($repository->containsId($wishes[0]->getId()));
        static::assertTrue($repository->containsId($wishes[1]->getId()));
        static::assertFalse($repository->contains($anotherWish));
        static::assertFalse($repository->containsId($anotherWish->getId()));
    }

    public function testNextWishIdMustAlwaysBeUnique()
    {
        $repository = new WishRepository();
        $wishIdOne = $repository->getNextWishId();
        $wishIdTwo = $repository->getNextWishId();

        static::assertNotSame($wishIdOne, $wishIdTwo);
        static::assertFalse($wishIdOne->equalTo($wishIdTwo));
    }

    private function createWishesIndexedByNumber(WishRepositoryInterface $repository, int $number)
    {
        $wishes = [];

        foreach (range(0, $number - 1) as $index) {
            $wishId = WishId::next();
            $wishes[$index] = $this->createWish($wishId);
            $repository->put($wishes[$index]);
        }

        return $wishes;
    }

    private function createWishesIndexedById(WishRepositoryInterface $repository, int $number)
    {
        $wishes = [];

        foreach (range(0, $number - 1) as $index) {
            $wishId = WishId::next();
            $wishes[$wishId->getId()] = $this->createWish($wishId);
            $repository->put($wishes[$wishId->getId()]);
        }

        return $wishes;
    }

    private function createWish(WishId $wishId = null): Wish
    {
        return new Wish(
            $wishId ?? WishId::next(),
            new WishName('Qux'),
            Expense::fromCurrencyAndScalars(
                new Currency('USD'),
                1000,
                20,
                400
            )
        );
    }
}
```

## File: `var/SymfonyRequirements.php`
```php
<?php

/*
 * This file is part of the Symfony package.
 *
 * (c) Fabien Potencier <fabien@symfony.com>
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

/*
 * Users of PHP 5.2 should be able to run the requirements checks.
 * This is why the file and all classes must be compatible with PHP 5.2+
 * (e.g. not using namespaces and closures).
 *
 * ************** CAUTION **************
 *
 * DO NOT EDIT THIS FILE as it will be overridden by Composer as part of
 * the installation/update process. The original file resides in the
 * SensioDistributionBundle.
 *
 * ************** CAUTION **************
 */

/**
 * Represents a single PHP requirement, e.g. an installed extension.
 * It can be a mandatory requirement or an optional recommendation.
 * There is a special subclass, named PhpIniRequirement, to check a php.ini configuration.
 *
 * @author Tobias Schultze <http://tobion.de>
 */
class Requirement
{
    private $fulfilled;
    private $testMessage;
    private $helpText;
    private $helpHtml;
    private $optional;

    /**
     * Constructor that initializes the requirement.
     *
     * @param bool        $fulfilled   Whether the requirement is fulfilled
     * @param string      $testMessage The message for testing the requirement
     * @param string      $helpHtml    The help text formatted in HTML for resolving the problem
     * @param string|null $helpText    The help text (when null, it will be inferred from $helpHtml, i.e. stripped from HTML tags)
     * @param bool        $optional    Whether this is only an optional recommendation not a mandatory requirement
     */
    public function __construct($fulfilled, $testMessage, $helpHtml, $helpText = null, $optional = false)
    {
        $this->fulfilled = (bool) $fulfilled;
        $this->testMessage = (string) $testMessage;
        $this->helpHtml = (string) $helpHtml;
        $this->helpText = null === $helpText ? strip_tags($this->helpHtml) : (string) $helpText;
        $this->optional = (bool) $optional;
    }

    /**
     * Returns whether the requirement is fulfilled.
     *
     * @return bool true if fulfilled, otherwise false
     */
    public function isFulfilled()
    {
        return $this->fulfilled;
    }

    /**
     * Returns the message for testing the requirement.
     *
     * @return string The test message
     */
    public function getTestMessage()
    {
        return $this->testMessage;
    }

    /**
     * Returns the help text for resolving the problem.
     *
     * @return string The help text
     */
    public function getHelpText()
    {
        return $this->helpText;
    }

    /**
     * Returns the help text formatted in HTML.
     *
     * @return string The HTML help
     */
    public function getHelpHtml()
    {
        return $this->helpHtml;
    }

    /**
     * Returns whether this is only an optional recommendation and not a mandatory requirement.
     *
     * @return bool true if optional, false if mandatory
     */
    public function isOptional()
    {
        return $this->optional;
    }
}

/**
 * Represents a PHP requirement in form of a php.ini configuration.
 *
 * @author Tobias Schultze <http://tobion.de>
 */
class PhpIniRequirement extends Requirement
{
    /**
     * Constructor that initializes the requirement.
     *
     * @param string        $cfgName           The configuration name used for ini_get()
     * @param bool|callback $evaluation        Either a boolean indicating whether the configuration should evaluate to true or false,
     *                                         or a callback function receiving the configuration value as parameter to determine the fulfillment of the requirement
     * @param bool          $approveCfgAbsence If true the Requirement will be fulfilled even if the configuration option does not exist, i.e. ini_get() returns false.
     *                                         This is helpful for abandoned configs in later PHP versions or configs of an optional extension, like Suhosin.
     *                                         Example: You require a config to be true but PHP later removes this config and defaults it to true internally.
     * @param string|null   $testMessage       The message for testing the requirement (when null and $evaluation is a boolean a default message is derived)
     * @param string|null   $helpHtml          The help text formatted in HTML for resolving the problem (when null and $evaluation is a boolean a default help is derived)
     * @param string|null   $helpText          The help text (when null, it will be inferred from $helpHtml, i.e. stripped from HTML tags)
     * @param bool          $optional          Whether this is only an optional recommendation not a mandatory requirement
     */
    public function __construct($cfgName, $evaluation, $approveCfgAbsence = false, $testMessage = null, $helpHtml = null, $helpText = null, $optional = false)
    {
        $cfgValue = ini_get($cfgName);

        if (is_callable($evaluation)) {
            if (null === $testMessage || null === $helpHtml) {
                throw new InvalidArgumentException('You must provide the parameters testMessage and helpHtml for a callback evaluation.');
            }

            $fulfilled = call_user_func($evaluation, $cfgValue);
        } else {
            if (null === $testMessage) {
                $testMessage = sprintf('%s %s be %s in php.ini',
                    $cfgName,
                    $optional ? 'should' : 'must',
                    $evaluation ? 'enabled' : 'disabled'
                );
            }

            if (null === $helpHtml) {
                $helpHtml = sprintf('Set <strong>%s</strong> to <strong>%s</strong> in php.ini<a href="#phpini">*</a>.',
                    $cfgName,
                    $evaluation ? 'on' : 'off'
                );
            }

            $fulfilled = $evaluation == $cfgValue;
        }

        parent::__construct($fulfilled || ($approveCfgAbsence && false === $cfgValue), $testMessage, $helpHtml, $helpText, $optional);
    }
}

/**
 * A RequirementCollection represents a set of Requirement instances.
 *
 * @author Tobias Schultze <http://tobion.de>
 */
class RequirementCollection implements IteratorAggregate
{
    /**
     * @var Requirement[]
     */
    private $requirements = array();

    /**
     * Gets the current RequirementCollection as an Iterator.
     *
     * @return Traversable A Traversable interface
     */
    public function getIterator()
    {
        return new ArrayIterator($this->requirements);
    }

    /**
     * Adds a Requirement.
     *
     * @param Requirement $requirement A Requirement instance
     */
    public function add(Requirement $requirement)
    {
        $this->requirements[] = $requirement;
    }

    /**
     * Adds a mandatory requirement.
     *
     * @param bool        $fulfilled   Whether the requirement is fulfilled
     * @param string      $testMessage The message for testing the requirement
     * @param string      $helpHtml    The help text formatted in HTML for resolving the problem
     * @param string|null $helpText    The help text (when null, it will be inferred from $helpHtml, i.e. stripped from HTML tags)
     */
    public function addRequirement($fulfilled, $testMessage, $helpHtml, $helpText = null)
    {
        $this->add(new Requirement($fulfilled, $testMessage, $helpHtml, $helpText, false));
    }

    /**
     * Adds an optional recommendation.
     *
     * @param bool        $fulfilled   Whether the recommendation is fulfilled
     * @param string      $testMessage The message for testing the recommendation
     * @param string      $helpHtml    The help text formatted in HTML for resolving the problem
     * @param string|null $helpText    The help text (when null, it will be inferred from $helpHtml, i.e. stripped from HTML tags)
     */
    public function addRecommendation($fulfilled, $testMessage, $helpHtml, $helpText = null)
    {
        $this->add(new Requirement($fulfilled, $testMessage, $helpHtml, $helpText, true));
    }

    /**
     * Adds a mandatory requirement in form of a php.ini configuration.
     *
     * @param string        $cfgName           The configuration name used for ini_get()
     * @param bool|callback $evaluation        Either a boolean indicating whether the configuration should evaluate to true or false,
     *                                         or a callback function receiving the configuration value as parameter to determine the fulfillment of the requirement
     * @param bool          $approveCfgAbsence If true the Requirement will be fulfilled even if the configuration option does not exist, i.e. ini_get() returns false.
     *                                         This is helpful for abandoned configs in later PHP versions or configs of an optional extension, like Suhosin.
     *                                         Example: You require a config to be true but PHP later removes this config and defaults it to true internally.
     * @param string        $testMessage       The message for testing the requirement (when null and $evaluation is a boolean a default message is derived)
     * @param string        $helpHtml          The help text formatted in HTML for resolving the problem (when null and $evaluation is a boolean a default help is derived)
     * @param string|null   $helpText          The help text (when null, it will be inferred from $helpHtml, i.e. stripped from HTML tags)
     */
    public function addPhpIniRequirement($cfgName, $evaluation, $approveCfgAbsence = false, $testMessage = null, $helpHtml = null, $helpText = null)
    {
        $this->add(new PhpIniRequirement($cfgName, $evaluation, $approveCfgAbsence, $testMessage, $helpHtml, $helpText, false));
    }

    /**
     * Adds an optional recommendation in form of a php.ini configuration.
     *
     * @param string        $cfgName           The configuration name used for ini_get()
     * @param bool|callback $evaluation        Either a boolean indicating whether the configuration should evaluate to true or false,
     *                                         or a callback function receiving the configuration value as parameter to determine the fulfillment of the requirement
     * @param bool          $approveCfgAbsence If true the Requirement will be fulfilled even if the configuration option does not exist, i.e. ini_get() returns false.
     *                                         This is helpful for abandoned configs in later PHP versions or configs of an optional extension, like Suhosin.
     *                                         Example: You require a config to be true but PHP later removes this config and defaults it to true internally.
     * @param string        $testMessage       The message for testing the requirement (when null and $evaluation is a boolean a default message is derived)
     * @param string        $helpHtml          The help text formatted in HTML for resolving the problem (when null and $evaluation is a boolean a default help is derived)
     * @param string|null   $helpText          The help text (when null, it will be inferred from $helpHtml, i.e. stripped from HTML tags)
     */
    public function addPhpIniRecommendation($cfgName, $evaluation, $approveCfgAbsence = false, $testMessage = null, $helpHtml = null, $helpText = null)
    {
        $this->add(new PhpIniRequirement($cfgName, $evaluation, $approveCfgAbsence, $testMessage, $helpHtml, $helpText, true));
    }

    /**
     * Adds a requirement collection to the current set of requirements.
     *
     * @param RequirementCollection $collection A RequirementCollection instance
     */
    public function addCollection(RequirementCollection $collection)
    {
        $this->requirements = array_merge($this->requirements, $collection->all());
    }

    /**
     * Returns both requirements and recommendations.
     *
     * @return Requirement[]
     */
    public function all()
    {
        return $this->requirements;
    }

    /**
     * Returns all mandatory requirements.
     *
     * @return Requirement[]
     */
    public function getRequirements()
    {
        $array = array();
        foreach ($this->requirements as $req) {
            if (!$req->isOptional()) {
                $array[] = $req;
            }
        }

        return $array;
    }

    /**
     * Returns the mandatory requirements that were not met.
     *
     * @return Requirement[]
     */
    public function getFailedRequirements()
    {
        $array = array();
        foreach ($this->requirements as $req) {
            if (!$req->isFulfilled() && !$req->isOptional()) {
                $array[] = $req;
            }
        }

        return $array;
    }

    /**
     * Returns all optional recommendations.
     *
     * @return Requirement[]
     */
    public function getRecommendations()
    {
        $array = array();
        foreach ($this->requirements as $req) {
            if ($req->isOptional()) {
                $array[] = $req;
            }
        }

        return $array;
    }

    /**
     * Returns the recommendations that were not met.
     *
     * @return Requirement[]
     */
    public function getFailedRecommendations()
    {
        $array = array();
        foreach ($this->requirements as $req) {
            if (!$req->isFulfilled() && $req->isOptional()) {
                $array[] = $req;
            }
        }

        return $array;
    }

    /**
     * Returns whether a php.ini configuration is not correct.
     *
     * @return bool php.ini configuration problem?
     */
    public function hasPhpIniConfigIssue()
    {
        foreach ($this->requirements as $req) {
            if (!$req->isFulfilled() && $req instanceof PhpIniRequirement) {
                return true;
            }
        }

        return false;
    }

    /**
     * Returns the PHP configuration file (php.ini) path.
     *
     * @return string|false php.ini file path
     */
    public function getPhpIniConfigPath()
    {
        return get_cfg_var('cfg_file_path');
    }
}

/**
 * This class specifies all requirements and optional recommendations that
 * are necessary to run the Symfony Standard Edition.
 *
 * @author Tobias Schultze <http://tobion.de>
 * @author Fabien Potencier <fabien@symfony.com>
 */
class SymfonyRequirements extends RequirementCollection
{
    const LEGACY_REQUIRED_PHP_VERSION = '5.3.3';
    const REQUIRED_PHP_VERSION = '5.5.9';

    /**
     * Constructor that initializes the requirements.
     */
    public function __construct()
    {
        /* mandatory requirements follow */

        $installedPhpVersion = phpversion();
        $requiredPhpVersion = $this->getPhpRequiredVersion();

        $this->addRecommendation(
            $requiredPhpVersion,
            'Vendors should be installed in order to check all requirements.',
            'Run the <code>composer install</code> command.',
            'Run the "composer install" command.'
        );

        if (false !== $requiredPhpVersion) {
            $this->addRequirement(
                version_compare($installedPhpVersion, $requiredPhpVersion, '>='),
                sprintf('PHP version must be at least %s (%s installed)', $requiredPhpVersion, $installedPhpVersion),
                sprintf('You are running PHP version "<strong>%s</strong>", but Symfony needs at least PHP "<strong>%s</strong>" to run.
                Before using Symfony, upgrade your PHP installation, preferably to the latest version.',
                    $installedPhpVersion, $requiredPhpVersion),
                sprintf('Install PHP %s or newer (installed version is %s)', $requiredPhpVersion, $installedPhpVersion)
            );
        }

        $this->addRequirement(
            version_compare($installedPhpVersion, '5.3.16', '!='),
            'PHP version must not be 5.3.16 as Symfony won\'t work properly with it',
            'Install PHP 5.3.17 or newer (or downgrade to an earlier PHP version)'
        );

        $this->addRequirement(
            is_dir(__DIR__.'/../vendor/composer'),
            'Vendor libraries must be installed',
            'Vendor libraries are missing. Install composer following instructions from <a href="http://getcomposer.org/">http://getcomposer.org/</a>. '.
                'Then run "<strong>php composer.phar install</strong>" to install them.'
        );

        $cacheDir = is_dir(__DIR__.'/../var/cache') ? __DIR__.'/../var/cache' : __DIR__.'/cache';

        $this->addRequirement(
            is_writable($cacheDir),
            'app/cache/ or var/cache/ directory must be writable',
            'Change the permissions of either "<strong>app/cache/</strong>" or  "<strong>var/cache/</strong>" directory so that the web server can write into it.'
        );

        $logsDir = is_dir(__DIR__.'/../var/logs') ? __DIR__.'/../var/logs' : __DIR__.'/logs';

        $this->addRequirement(
            is_writable($logsDir),
            'app/logs/ or var/logs/ directory must be writable',
            'Change the permissions of either "<strong>app/logs/</strong>" or  "<strong>var/logs/</strong>" directory so that the web server can write into it.'
        );

        if (version_compare($installedPhpVersion, '7.0.0', '<')) {
            $this->addPhpIniRequirement(
                'date.timezone', true, false,
                'date.timezone setting must be set',
                'Set the "<strong>date.timezone</strong>" setting in php.ini<a href="#phpini">*</a> (like Europe/Paris).'
            );
        }

        if (false !== $requiredPhpVersion && version_compare($installedPhpVersion, $requiredPhpVersion, '>=')) {
            $timezones = array();
            foreach (DateTimeZone::listAbbreviations() as $abbreviations) {
                foreach ($abbreviations as $abbreviation) {
                    $timezones[$abbreviation['timezone_id']] = true;
                }
            }

            $this->addRequirement(
                isset($timezones[@date_default_timezone_get()]),
                sprintf('Configured default timezone "%s" must be supported by your installation of PHP', @date_default_timezone_get()),
                'Your default timezone is not supported by PHP. Check for typos in your <strong>php.ini</strong> file and have a look at the list of deprecated timezones at <a href="http://php.net/manual/en/timezones.others.php">http://php.net/manual/en/timezones.others.php</a>.'
            );
        }

        $this->addRequirement(
            function_exists('iconv'),
            'iconv() must be available',
            'Install and enable the <strong>iconv</strong> extension.'
        );

        $this->addRequirement(
            function_exists('json_encode'),
            'json_encode() must be available',
            'Install and enable the <strong>JSON</strong> extension.'
        );

        $this->addRequirement(
            function_exists('session_start'),
            'session_start() must be available',
            'Install and enable the <strong>session</strong> extension.'
        );

        $this->addRequirement(
            function_exists('ctype_alpha'),
            'ctype_alpha() must be available',
            'Install and enable the <strong>ctype</strong> extension.'
        );

        $this->addRequirement(
            function_exists('token_get_all'),
            'token_get_all() must be available',
            'Install and enable the <strong>Tokenizer</strong> extension.'
        );

        $this->addRequirement(
            function_exists('simplexml_import_dom'),
            'simplexml_import_dom() must be available',
            'Install and enable the <strong>SimpleXML</strong> extension.'
        );

        if (function_exists('apc_store') && ini_get('apc.enabled')) {
            if (version_compare($installedPhpVersion, '5.4.0', '>=')) {
                $this->addRequirement(
                    version_compare(phpversion('apc'), '3.1.13', '>='),
                    'APC version must be at least 3.1.13 when using PHP 5.4',
                    'Upgrade your <strong>APC</strong> extension (3.1.13+).'
                );
            } else {
                $this->addRequirement(
                    version_compare(phpversion('apc'), '3.0.17', '>='),
                    'APC version must be at least 3.0.17',
                    'Upgrade your <strong>APC</strong> extension (3.0.17+).'
                );
            }
        }

        $this->addPhpIniRequirement('detect_unicode', false);

        if (extension_loaded('suhosin')) {
            $this->addPhpIniRequirement(
                'suhosin.executor.include.whitelist',
                create_function('$cfgValue', 'return false !== stripos($cfgValue, "phar");'),
                false,
                'suhosin.executor.include.whitelist must be configured correctly in php.ini',
                'Add "<strong>phar</strong>" to <strong>suhosin.executor.include.whitelist</strong> in php.ini<a href="#phpini">*</a>.'
            );
        }

        if (extension_loaded('xdebug')) {
            $this->addPhpIniRequirement(
                'xdebug.show_exception_trace', false, true
            );

            $this->addPhpIniRequirement(
                'xdebug.scream', false, true
            );

            $this->addPhpIniRecommendation(
                'xdebug.max_nesting_level',
                create_function('$cfgValue', 'return $cfgValue > 100;'),
                true,
                'xdebug.max_nesting_level should be above 100 in php.ini',
                'Set "<strong>xdebug.max_nesting_level</strong>" to e.g. "<strong>250</strong>" in php.ini<a href="#phpini">*</a> to stop Xdebug\'s infinite recursion protection erroneously throwing a fatal error in your project.'
            );
        }

        $pcreVersion = defined('PCRE_VERSION') ? (float) PCRE_VERSION : null;

        $this->addRequirement(
            null !== $pcreVersion,
            'PCRE extension must be available',
            'Install the <strong>PCRE</strong> extension (version 8.0+).'
        );

        if (extension_loaded('mbstring')) {
            $this->addPhpIniRequirement(
                'mbstring.func_overload',
                create_function('$cfgValue', 'return (int) $cfgValue === 0;'),
                true,
                'string functions should not be overloaded',
                'Set "<strong>mbstring.func_overload</strong>" to <strong>0</strong> in php.ini<a href="#phpini">*</a> to disable function overloading by the mbstring extension.'
            );
        }

        /* optional recommendations follow */

        if (file_exists(__DIR__.'/../vendor/composer')) {
            require_once __DIR__.'/../vendor/autoload.php';

            try {
                $r = new ReflectionClass('Sensio\Bundle\DistributionBundle\SensioDistributionBundle');

                $contents = file_get_contents(dirname($r->getFileName()).'/Resources/skeleton/app/SymfonyRequirements.php');
            } catch (ReflectionException $e) {
                $contents = '';
            }
            $this->addRecommendation(
                file_get_contents(__FILE__) === $contents,
                'Requirements file should be up-to-date',
                'Your requirements file is outdated. Run composer install and re-check your configuration.'
            );
        }

        $this->addRecommendation(
            version_compare($installedPhpVersion, '5.3.4', '>='),
            'You should use at least PHP 5.3.4 due to PHP bug #52083 in earlier versions',
            'Your project might malfunction randomly due to PHP bug #52083 ("Notice: Trying to get property of non-object"). Install PHP 5.3.4 or newer.'
        );

        $this->addRecommendation(
            version_compare($installedPhpVersion, '5.3.8', '>='),
            'When using annotations you should have at least PHP 5.3.8 due to PHP bug #55156',
            'Install PHP 5.3.8 or newer if your project uses annotations.'
        );

        $this->addRecommendation(
            version_compare($installedPhpVersion, '5.4.0', '!='),
            'You should not use PHP 5.4.0 due to the PHP bug #61453',
            'Your project might not work properly due to the PHP bug #61453 ("Cannot dump definitions which have method calls"). Install PHP 5.4.1 or newer.'
        );

        $this->addRecommendation(
            version_compare($installedPhpVersion, '5.4.11', '>='),
            'When using the logout handler from the Symfony Security Component, you should have at least PHP 5.4.11 due to PHP bug #63379 (as a workaround, you can also set invalidate_session to false in the security logout handler configuration)',
            'Install PHP 5.4.11 or newer if your project uses the logout handler from the Symfony Security Component.'
        );

        $this->addRecommendation(
            (version_compare($installedPhpVersion, '5.3.18', '>=') && version_compare($installedPhpVersion, '5.4.0', '<'))
            ||
            version_compare($installedPhpVersion, '5.4.8', '>='),
            'You should use PHP 5.3.18+ or PHP 5.4.8+ to always get nice error messages for fatal errors in the development environment due to PHP bug #61767/#60909',
            'Install PHP 5.3.18+ or PHP 5.4.8+ if you want nice error messages for all fatal errors in the development environment.'
        );

        if (null !== $pcreVersion) {
            $this->addRecommendation(
                $pcreVersion >= 8.0,
                sprintf('PCRE extension should be at least version 8.0 (%s installed)', $pcreVersion),
                '<strong>PCRE 8.0+</strong> is preconfigured in PHP since 5.3.2 but you are using an outdated version of it. Symfony probably works anyway but it is recommended to upgrade your PCRE extension.'
            );
        }

        $this->addRecommendation(
            class_exists('DomDocument'),
            'PHP-DOM and PHP-XML modules should be installed',
            'Install and enable the <strong>PHP-DOM</strong> and the <strong>PHP-XML</strong> modules.'
        );

        $this->addRecommendation(
            function_exists('mb_strlen'),
            'mb_strlen() should be available',
            'Install and enable the <strong>mbstring</strong> extension.'
        );

        $this->addRecommendation(
            function_exists('utf8_decode'),
            'utf8_decode() should be available',
            'Install and enable the <strong>XML</strong> extension.'
        );

        $this->addRecommendation(
            function_exists('filter_var'),
            'filter_var() should be available',
            'Install and enable the <strong>filter</strong> extension.'
        );

        if (!defined('PHP_WINDOWS_VERSION_BUILD')) {
            $this->addRecommendation(
                function_exists('posix_isatty'),
                'posix_isatty() should be available',
                'Install and enable the <strong>php_posix</strong> extension (used to colorize the CLI output).'
            );
        }

        $this->addRecommendation(
            extension_loaded('intl'),
            'intl extension should be available',
            'Install and enable the <strong>intl</strong> extension (used for validators).'
        );

        if (extension_loaded('intl')) {
            // in some WAMP server installations, new Collator() returns null
            $this->addRecommendation(
                null !== new Collator('fr_FR'),
                'intl extension should be correctly configured',
                'The intl extension does not behave properly. This problem is typical on PHP 5.3.X x64 WIN builds.'
            );

            // check for compatible ICU versions (only done when you have the intl extension)
            if (defined('INTL_ICU_VERSION')) {
                $version = INTL_ICU_VERSION;
            } else {
                $reflector = new ReflectionExtension('intl');

                ob_start();
                $reflector->info();
                $output = strip_tags(ob_get_clean());

                preg_match('/^ICU version +(?:=> )?(.*)$/m', $output, $matches);
                $version = $matches[1];
            }

            $this->addRecommendation(
                version_compare($version, '4.0', '>='),
                'intl ICU version should be at least 4+',
                'Upgrade your <strong>intl</strong> extension with a newer ICU version (4+).'
            );

            if (class_exists('Symfony\Component\Intl\Intl')) {
                $this->addRecommendation(
                    \Symfony\Component\Intl\Intl::getIcuDataVersion() <= \Symfony\Component\Intl\Intl::getIcuVersion(),
                    sprintf('intl ICU version installed on your system is outdated (%s) and does not match the ICU data bundled with Symfony (%s)', \Symfony\Component\Intl\Intl::getIcuVersion(), \Symfony\Component\Intl\Intl::getIcuDataVersion()),
                    'To get the latest internationalization data upgrade the ICU system package and the intl PHP extension.'
                );
                if (\Symfony\Component\Intl\Intl::getIcuDataVersion() <= \Symfony\Component\Intl\Intl::getIcuVersion()) {
                    $this->addRecommendation(
                        \Symfony\Component\Intl\Intl::getIcuDataVersion() === \Symfony\Component\Intl\Intl::getIcuVersion(),
                        sprintf('intl ICU version installed on your system (%s) does not match the ICU data bundled with Symfony (%s)', \Symfony\Component\Intl\Intl::getIcuVersion(), \Symfony\Component\Intl\Intl::getIcuDataVersion()),
                        'To avoid internationalization data inconsistencies upgrade the symfony/intl component.'
                    );
                }
            }

            $this->addPhpIniRecommendation(
                'intl.error_level',
                create_function('$cfgValue', 'return (int) $cfgValue === 0;'),
                true,
                'intl.error_level should be 0 in php.ini',
                'Set "<strong>intl.error_level</strong>" to "<strong>0</strong>" in php.ini<a href="#phpini">*</a> to inhibit the messages when an error occurs in ICU functions.'
            );
        }

        $accelerator =
            (extension_loaded('eaccelerator') && ini_get('eaccelerator.enable'))
            ||
            (extension_loaded('apc') && ini_get('apc.enabled'))
            ||
            (extension_loaded('Zend Optimizer+') && ini_get('zend_optimizerplus.enable'))
            ||
            (extension_loaded('Zend OPcache') && ini_get('opcache.enable'))
            ||
            (extension_loaded('xcache') && ini_get('xcache.cacher'))
            ||
            (extension_loaded('wincache') && ini_get('wincache.ocenabled'))
        ;

        $this->addRecommendation(
            $accelerator,
            'a PHP accelerator should be installed',
            'Install and/or enable a <strong>PHP accelerator</strong> (highly recommended).'
        );

        if (strtoupper(substr(PHP_OS, 0, 3)) === 'WIN') {
            $this->addRecommendation(
                $this->getRealpathCacheSize() >= 5 * 1024 * 1024,
                'realpath_cache_size should be at least 5M in php.ini',
                'Setting "<strong>realpath_cache_size</strong>" to e.g. "<strong>5242880</strong>" or "<strong>5M</strong>" in php.ini<a href="#phpini">*</a> may improve performance on Windows significantly in some cases.'
            );
        }

        $this->addPhpIniRecommendation('short_open_tag', false);

        $this->addPhpIniRecommendation('magic_quotes_gpc', false, true);

        $this->addPhpIniRecommendation('register_globals', false, true);

        $this->addPhpIniRecommendation('session.auto_start', false);

        $this->addRecommendation(
            class_exists('PDO'),
            'PDO should be installed',
            'Install <strong>PDO</strong> (mandatory for Doctrine).'
        );

        if (class_exists('PDO')) {
            $drivers = PDO::getAvailableDrivers();
            $this->addRecommendation(
                count($drivers) > 0,
                sprintf('PDO should have some drivers installed (currently available: %s)', count($drivers) ? implode(', ', $drivers) : 'none'),
                'Install <strong>PDO drivers</strong> (mandatory for Doctrine).'
            );
        }
    }

    /**
     * Loads realpath_cache_size from php.ini and converts it to int.
     *
     * (e.g. 16k is converted to 16384 int)
     *
     * @return int
     */
    protected function getRealpathCacheSize()
    {
        $size = ini_get('realpath_cache_size');
        $size = trim($size);
        $unit = '';
        if (!ctype_digit($size)) {
            $unit = strtolower(substr($size, -1, 1));
            $size = (int) substr($size, 0, -1);
        }
        switch ($unit) {
            case 'g':
                return $size * 1024 * 1024 * 1024;
            case 'm':
                return $size * 1024 * 1024;
            case 'k':
                return $size * 1024;
            default:
                return (int) $size;
        }
    }

    /**
     * Defines PHP required version from Symfony version.
     *
     * @return string|false The PHP required version or false if it could not be guessed
     */
    protected function getPhpRequiredVersion()
    {
        if (!file_exists($path = __DIR__.'/../composer.lock')) {
            return false;
        }

        $composerLock = json_decode(file_get_contents($path), true);
        foreach ($composerLock['packages'] as $package) {
            $name = $package['name'];
            if ('symfony/symfony' !== $name && 'symfony/http-kernel' !== $name) {
                continue;
            }

            return (int) $package['version'][1] > 2 ? self::REQUIRED_PHP_VERSION : self::LEGACY_REQUIRED_PHP_VERSION;
        }

        return false;
    }
}
```

## File: `web/.htaccess`
```
# Use the front controller as index file. It serves as a fallback solution when
# every other rewrite/redirect fails (e.g. in an aliased environment without
# mod_rewrite). Additionally, this reduces the matching process for the
# start page (path "/") because otherwise Apache will apply the rewriting rules
# to each configured DirectoryIndex file (e.g. index.php, index.html, index.pl).
DirectoryIndex app.php

# By default, Apache does not evaluate symbolic links if you did not enable this
# feature in your server configuration. Uncomment the following line if you
# install assets as symlinks or if you experience problems related to symlinks
# when compiling LESS/Sass/CoffeScript assets.
# Options FollowSymlinks

# Disabling MultiViews prevents unwanted negotiation, e.g. "/app" should not resolve
# to the front controller "/app.php" but be rewritten to "/app.php/app".
<IfModule mod_negotiation.c>
    Options -MultiViews
</IfModule>

<IfModule mod_rewrite.c>
    RewriteEngine On

    # Determine the RewriteBase automatically and set it as environment variable.
    # If you are using Apache aliases to do mass virtual hosting or installed the
    # project in a subdirectory, the base path will be prepended to allow proper
    # resolution of the app.php file and to redirect to the correct URI. It will
    # work in environments without path prefix as well, providing a safe, one-size
    # fits all solution. But as you do not need it in this case, you can comment
    # the following 2 lines to eliminate the overhead.
    RewriteCond %{REQUEST_URI}::$1 ^(/.+)/(.*)::\2$
    RewriteRule ^(.*) - [E=BASE:%1]

    # Sets the HTTP_AUTHORIZATION header removed by Apache
    RewriteCond %{HTTP:Authorization} .
    RewriteRule ^ - [E=HTTP_AUTHORIZATION:%{HTTP:Authorization}]

    # Redirect to URI without front controller to prevent duplicate content
    # (with and without `/app.php`). Only do this redirect on the initial
    # rewrite by Apache and not on subsequent cycles. Otherwise we would get an
    # endless redirect loop (request -> rewrite to front controller ->
    # redirect -> request -> ...).
    # So in case you get a "too many redirects" error or you always get redirected
    # to the start page because your Apache does not expose the REDIRECT_STATUS
    # environment variable, you have 2 choices:
    # - disable this feature by commenting the following 2 lines or
    # - use Apache >= 2.3.9 and replace all L flags by END flags and remove the
    #   following RewriteCond (best solution)
    RewriteCond %{ENV:REDIRECT_STATUS} ^$
    RewriteRule ^app\.php(?:/(.*)|$) %{ENV:BASE}/$1 [R=301,L]

    # If the requested filename exists, simply serve it.
    # We only want to let Apache serve files and not directories.
    RewriteCond %{REQUEST_FILENAME} -f
    RewriteRule ^ - [L]

    # Rewrite all other queries to the front controller.
    RewriteRule ^ %{ENV:BASE}/app.php [L]
</IfModule>

<IfModule !mod_rewrite.c>
    <IfModule mod_alias.c>
        # When mod_rewrite is not available, we instruct a temporary redirect of
        # the start page to the front controller explicitly so that the website
        # and the generated links can still be used.
        RedirectMatch 302 ^/$ /app.php/
        # RedirectTemp cannot be used instead
    </IfModule>
</IfModule>
```

## File: `web/app.php`
```php
<?php

use Symfony\Component\HttpFoundation\Request;

require __DIR__.'/../vendor/autoload.php';
if (PHP_VERSION_ID < 70000) {
    include_once __DIR__.'/../var/bootstrap.php.cache';
}

$kernel = new AppKernel('prod', false);
if (PHP_VERSION_ID < 70000) {
    $kernel->loadClassCache();
}
//$kernel = new AppCache($kernel);

// When using the HttpCache, you need to call the method in your front controller instead of relying on the configuration parameter
//Request::enableHttpMethodParameterOverride();
$request = Request::createFromGlobals();
$response = $kernel->handle($request);
$response->send();
$kernel->terminate($request, $response);
```

## File: `web/app_dev.php`
```php
<?php

use Symfony\Component\Debug\Debug;
use Symfony\Component\HttpFoundation\Request;

// If you don't want to setup permissions the proper way, just uncomment the following PHP line
// read https://symfony.com/doc/current/setup.html#checking-symfony-application-configuration-and-setup
// for more information
//umask(0000);

// This check prevents access to debug front controllers that are deployed by accident to production servers.
// Feel free to remove this, extend it, or make something more sophisticated.
if (isset($_SERVER['HTTP_CLIENT_IP'])
    || isset($_SERVER['HTTP_X_FORWARDED_FOR'])
    || !(in_array(@$_SERVER['REMOTE_ADDR'], ['127.0.0.1', '::1'], true) || PHP_SAPI === 'cli-server')
) {
    header('HTTP/1.0 403 Forbidden');
    exit('You are not allowed to access this file. Check '.basename(__FILE__).' for more information.');
}

require __DIR__.'/../vendor/autoload.php';
Debug::enable();

$kernel = new AppKernel('dev', true);
if (PHP_VERSION_ID < 70000) {
    $kernel->loadClassCache();
}
$request = Request::createFromGlobals();
$response = $kernel->handle($request);
$response->send();
$kernel->terminate($request, $response);
```

## File: `web/config.php`
```php
<?php

/*
 * ************** CAUTION **************
 *
 * DO NOT EDIT THIS FILE as it will be overridden by Composer as part of
 * the installation/update process. The original file resides in the
 * SensioDistributionBundle.
 *
 * ************** CAUTION **************
 */

if (!isset($_SERVER['HTTP_HOST'])) {
    exit("This script cannot be run from the CLI. Run it from a browser.\n");
}

if (!in_array(@$_SERVER['REMOTE_ADDR'], array(
    '127.0.0.1',
    '::1',
))) {
    header('HTTP/1.0 403 Forbidden');
    exit('This script is only accessible from localhost.');
}

require_once dirname(__FILE__).'/../var/SymfonyRequirements.php';

$symfonyRequirements = new SymfonyRequirements();

$majorProblems = $symfonyRequirements->getFailedRequirements();
$minorProblems = $symfonyRequirements->getFailedRecommendations();
$hasMajorProblems = (bool) count($majorProblems);
$hasMinorProblems = (bool) count($minorProblems);

?>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
        <meta name="robots" content="noindex,nofollow" />
        <title>Symfony Configuration Checker</title>
        <style>
            /* styles copied from symfony framework bundle */
            html {
                background: #eee;
            }
            body {
                font: 11px Verdana, Arial, sans-serif;
                color: #333;
            }
            .sf-reset, .sf-reset .block, .sf-reset #message {
                margin: auto;
            }
            img {
                border: 0;
            }
            .clear {
                clear: both;
                height: 0;
                font-size: 0;
                line-height: 0;
            }
            .clear-fix:after {
                content: "\0020";
                display: block;
                height: 0;
                clear: both;
                visibility: hidden;
            }
            .clear-fix {
                display: inline-block;
            }
            * html .clear-fix {
                height: 1%;
            }
            .clear-fix {
                display: block;
            }
            .header {
                padding: 30px 30px 20px 30px;
            }
            .header-logo {
                float: left;
            }
            .search {
                float: right;
                padding-top: 20px;
            }
            .search label {
                line-height: 28px;
                vertical-align: middle;
            }
            .search input {
                width: 195px;
                font-size: 12px;
                border: 1px solid #dadada;
                background: #fff url(data:image/gif;base64,R0lGODlhAQAFAKIAAPX19e/v7/39/fr6+urq6gAAAAAAAAAAACH5BAAAAAAALAAAAAABAAUAAAMESAEjCQA7) repeat-x left top;
                padding: 5px 6px;
                color: #565656;
            }
            .search input[type="search"] {
                -webkit-appearance: textfield;
            }
            #content {
                width: 970px;
                margin: 0 auto;
            }
            #content pre {
                white-space: normal;
                font-family: Arial, Helvetica, sans-serif;
            }

            /*
            Copyright (c) 2010, Yahoo! Inc. All rights reserved.
            Code licensed under the BSD License:
            http://developer.yahoo.com/yui/license.html
            version: 3.1.2
            build: 56
            */
            .sf-reset div,.sf-reset dl,.sf-reset dt,.sf-reset dd,.sf-reset ul,.sf-reset ol,.sf-reset li,.sf-reset h1,.sf-reset h2,.sf-reset h3,.sf-reset h4,.sf-reset h5,.sf-reset h6,.sf-reset pre,.sf-reset code,.sf-reset form,.sf-reset fieldset,.sf-reset legend,.sf-reset input,.sf-reset textarea,.sf-reset p,.sf-reset blockquote,.sf-reset th,.sf-reset td{margin:0;padding:0;}.sf-reset table{border-collapse:collapse;border-spacing:0;}.sf-reset fieldset,.sf-reset img{border:0;}.sf-reset address,.sf-reset caption,.sf-reset cite,.sf-reset code,.sf-reset dfn,.sf-reset em,.sf-reset strong,.sf-reset th,.sf-reset var{font-style:normal;font-weight:normal;}.sf-reset li{list-style:none;}.sf-reset caption,.sf-reset th{text-align:left;}.sf-reset h1,.sf-reset h2,.sf-reset h3,.sf-reset h4,.sf-reset h5,.sf-reset h6{font-size:100%;font-weight:normal;}.sf-reset q:before,.sf-reset q:after{content:'';}.sf-reset abbr,.sf-reset acronym{border:0;font-variant:normal;}.sf-reset sup{vertical-align:text-top;}.sf-reset sub{vertical-align:text-bottom;}.sf-reset input,.sf-reset textarea,.sf-reset select{font-family:inherit;font-size:inherit;font-weight:inherit;}.sf-reset input,.sf-reset textarea,.sf-reset select{font-size:100%;}.sf-reset legend{color:#000;}
            .sf-reset abbr {
                border-bottom: 1px dotted #000;
                cursor: help;
            }
            .sf-reset p {
                font-size: 14px;
                line-height: 20px;
                padding-bottom: 20px;
            }
            .sf-reset strong {
                color: #313131;
                font-weight: bold;
            }
            .sf-reset a {
                color: #6c6159;
            }
            .sf-reset a img {
                border: none;
            }
            .sf-reset a:hover {
                text-decoration: underline;
            }
            .sf-reset em {
                font-style: italic;
            }
            .sf-reset h2,
            .sf-reset h3 {
                font-weight: bold;
            }
            .sf-reset h1 {
                font-family: Georgia, "Times New Roman", Times, serif;
                font-size: 20px;
                color: #313131;
                word-wrap: break-word;
            }
            .sf-reset li {
                padding-bottom: 10px;
            }
            .sf-reset .block {
                -moz-border-radius: 16px;
                -webkit-border-radius: 16px;
                border-radius: 16px;
                margin-bottom: 20px;
                background-color: #FFFFFF;
                border: 1px solid #dfdfdf;
                padding: 40px 50px;
                word-break: break-all;
            }
            .sf-reset h2 {
                font-size: 16px;
                font-family: Arial, Helvetica, sans-serif;
            }
            .sf-reset li a {
                background: none;
                color: #868686;
                text-decoration: none;
            }
            .sf-reset li a:hover {
                background: none;
                color: #313131;
                text-decoration: underline;
            }
            .sf-reset ol {
                padding: 10px 0;
            }
            .sf-reset ol li {
                list-style: decimal;
                margin-left: 20px;
                padding: 2px;
                padding-bottom: 20px;
            }
            .sf-reset ol ol li {
                list-style-position: inside;
                margin-left: 0;
                white-space: nowrap;
                font-size: 12px;
                padding-bottom: 0;
            }
            .sf-reset li .selected {
                background-color: #ffd;
            }
            .sf-button {
                display: -moz-inline-box;
                display: inline-block;
                text-align: center;
                vertical-align: middle;
                border: 0;
                background: transparent none;
                text-transform: uppercase;
                cursor: pointer;
                font: bold 11px Arial, Helvetica, sans-serif;
            }
            .sf-button span {
                text-decoration: none;
                display: block;
                height: 28px;
                float: left;
            }
            .sf-button .border-l {
                text-decoration: none;
                display: block;
                height: 28px;
                float: left;
                padding: 0 0 0 7px;
                background: transparent url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAcAAAAcCAYAAACtQ6WLAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAQtJREFUeNpiPHnyJAMakARiByDWYEGT8ADiYGVlZStubm5xlv///4MEQYoKZGRkQkRERLRYWVl5wYJQyXBZWdkwCQkJUxAHKgaWlAHSLqKiosb//v1DsYMFKGCvoqJiDmQzwXTAJYECulxcXNLoumCSoszMzDzoumDGghQwYZUECWIzkrAkSIIGOmlkLI10AiX//P379x8jIyMTNmPf/v79+ysLCwsvuiQoNi5//fr1Kch4dAyS3P/gwYMTQBP+wxwHw0xA4gkQ73v9+vUZdJ2w1Lf82bNn4iCHCQoKasHsZw4ODgbRIL8c+/Lly5M3b978Y2dn5wC6npkFLXnsAOKLjx49AmUHLYAAAwBoQubG016R5wAAAABJRU5ErkJggg==) no-repeat top left;
            }
            .sf-button .border-r {
                padding: 0 7px 0 0;
                background: transparent url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAcAAAAcCAYAAACtQ6WLAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAR1JREFUeNpiPHnyZCMDA8MNID5gZmb2nAEJMH7//v3N169fX969e/cYkL8WqGAHXPLv37//QYzfv39/fvPmzbUnT56sAXInmJub/2H5/x8sx8DCwsIrISFhDmQyPX78+CmQXs70798/BmQsKipqBNTgdvz4cWkmkE5kDATMioqKZkCFdiwg1eiAi4tLGqhQF24nMmBmZuYEigth1QkEbEBxTlySYPvJkwSJ00AnjYylgU6gxB8g/oFVEphkvgLF32KNMmCCewYUv4qhEyj47+HDhyeBzIMYOoEp8CxQw56wsLAncJ1//vz5/P79+2svX74EJc2V4BT58+fPd8CE/QKYHMGJOiIiAp6oWW7evDkNSF8DZYfIyEiU7AAQYACJ2vxVdJW4eQAAAABJRU5ErkJggg==) right top no-repeat;
            }
            .sf-button .btn-bg {
                padding: 0 14px;
                color: #636363;
                line-height: 28px;
                background: transparent url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAAcCAYAAACgXdXMAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAClJREFUeNpiPnny5EKGf//+/Wf6//8/A4QAcrGzKCZwGc9sa2urBBBgAIbDUoYVp9lmAAAAAElFTkSuQmCC) repeat-x top left;
            }
            .sf-button:hover .border-l,
            .sf-button-selected .border-l {
                background: transparent url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAcAAAAcCAYAAACtQ6WLAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAR9JREFUeNpi/P//PwMyOHfunDqQSgNiexZkibNnzxYBqZa3HOs5v7PcYQBLnjlzhg1IbfzIdsTjA/t+ht9Mr8GKwZL//v3r+sB+0OMN+zqIEf8gFMvJkyd1gXTOa9YNDP//otrPAtSV/Jp9HfPff78Z0AEL0LUeXxivMfxD0wXTqfjj/2ugkf+wSrL9/YtpJEyS4S8WI5Ek/+GR/POPFjr//cenE6/kP9q4Fo/kr39/mdj+M/zFkGQCSj5i+ccPjLJ/GBgkuYOHQR1sNDpmAkb2LBmWwL///zKCIxwZM0VHR18G6p4uxeLLAA4tJMwEshiou1iMxXaHLGswA+t/YbhORuQUv2DBAnCifvxzI+enP3dQJUFg/vz5sOzgBBBgAPxX9j0YnH4JAAAAAElFTkSuQmCC) no-repeat top left;
            }
            .sf-button:hover .border-r,
            .sf-button-selected .border-r {
                background: transparent url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAcAAAAcCAYAAACtQ6WLAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAT5JREFUeNpiPHv27BkGBoaDQDzLyMjoJgMSYHrM3WX8hn1d0f///88DFRYhSzIuv2X5H8Rg/SfKIPDTkYH/l80OINffxMTkF9O/f/8ZQPgnwyuGl+wrGd6x7vf49+9fO9jYf3+Bkkj4NesmBqAV+SdPntQC6vzHgIz//gOawbqOGchOxtAJwp8Zr4F0e7D8/fuPAR38/P8eZIo0yz8skv8YvoIk+YE6/zNgAyD7sRqLkPzzjxY6/+HS+R+fTkZ8djLh08lCUCcuSWawJGbwMTGwg7zyBatX2Bj5QZKPsBrLzaICktzN8g/NWEYGZgYZjoC/wMiei5FMpFh8QPSU6Ojoy3Cd7EwiDBJsDgxiLNY7gLrKQGIsHAxSDHxAO2TZ/b8D+TVxcXF9MCtYtLiKLgDpfUDVsxITE1GyA0CAAQA2E/N8VuHyAAAAAABJRU5ErkJggg==) right top no-repeat;
            }
            .sf-button:hover .btn-bg,
            .sf-button-selected .btn-bg {
                color: #FFFFFF;
                text-shadow:0 1px 1px #6b9311;
                background: transparent url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAAcCAIAAAAvP0KbAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAEFJREFUeNpiPnv2LNMdvlymf///M/37B8R/QfQ/MP33L4j+B6Qh7L9//sHpf2h8MA1V+w/KRjYLaDaLCU8vQIABAFO3TxZriO4yAAAAAElFTkSuQmCC) repeat-x top left;
            }

            /* styles copied from bundles/sensiodistribution/webconfigurator/css/install.css */
            body {
                font-size: 14px;
                font-family: "Lucida Sans Unicode", "Lucida Grande", Verdana, Arial, Helvetica, sans-serif;
            }
            .sf-reset h1.title {
                font-size: 45px;
                padding-bottom: 30px;
            }
            .sf-reset h2 {
                font-weight: bold;
                color: #FFFFFF;
                /* Font is reset to sans-serif (like body) */
                font-family: "Lucida Sans Unicode", "Lucida Grande", Verdana, Arial, Helvetica, sans-serif;
                margin-bottom: 10px;
                background-color: #aacd4e;
                padding: 2px 4px;
                display: inline-block;
                text-transform: uppercase;
            }
            .sf-reset ul a,
            .sf-reset ul a:hover {
                background: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUAAAAICAYAAAAx8TU7AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAFdJREFUeNpiYACBjjOhDEiACSggCKTLgXQ5TJARqhIkcReIKxgqTGYxwvV0nDEGkmeAOIwJySiQ4HsgvseIpGo3ELsCtZ9lRDIvDCiwhwHJPEFkJwEEGACq6hdnax8y1AAAAABJRU5ErkJggg==) no-repeat right 7px;
                padding-right: 10px;
            }
            .sf-reset ul, ol {
                padding-left: 20px;
            }
            .sf-reset li {
                padding-bottom: 18px;
            }
            .sf-reset ol li {
                list-style-type: decimal;
            }
            .sf-reset ul li {
                list-style-type: none;
            }
            .sf-reset .symfony-blocks-install {
                overflow: hidden;
            }
            .sf-reset .symfony-install-continue {
                font-size: 0.95em;
                padding-left: 0;
            }
            .sf-reset .symfony-install-continue li {
                padding-bottom: 10px;
            }
            .sf-reset .ok {
                color: #fff;
                font-family: "Lucida Sans Unicode", "Lucida Grande", Verdana, Arial, Helvetica, sans-serif;
                background-color: #6d6;
                padding: 10px;
                margin-bottom: 20px;
            }
            .sf-reset .ko {
                background-color: #d66;
            }
            .sf-reset p.help {
                padding: 12px 16px;
                word-break: break-word;
            }
            .version {
                text-align: right;
                font-size: 10px;
                margin-right: 20px;
            }
            .sf-reset a,
            .sf-reset li a {
                color: #08C;
                text-decoration: none;
            }
            .sf-reset a:hover,
            .sf-reset li a:hover {
                color: #08C;
                text-decoration: underline;
            }
            .sf-reset textarea {
                padding: 7px;
            }
        </style>
    </head>
    <body>
        <div id="content">
            <div class="header clear-fix">
                <div class="header-logo">
                    <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAALYAAAA+CAMAAACxzRGDAAAAUVBMVEX////Ly8yko6WLioxkYmVXVVkwLjLl5eWxsLJKSEzy8vJxcHLY2Ni+vb89Oz9XVVh+fH+Yl5n///+xsbLY2Nlxb3KkpKWXlph+fX+LiYy+vr/IZP61AAAAAXRSTlMAQObYZgAABRBJREFUeNrVmtuWoyAQRS1FEEQSzQU7//+hYxUiXsKQZLJWM+chsUloN+WhCuguYoKyYqzmvGasKqH4HyRKxndipcgcumH8qViTM7TkUclcwaHmf5XM0eWq4km1KjdqXfMXJHVe1J3hL8lk5fCGv6wmT+o0d87U+XNrk0Y9nfv+7LM6ZJH5ZBL6LAbSxQ3Q5FDr22Skr8PQSy4n7isnsQxSX4r6pobhjCHHeDNOKrO3yGmCvZOjV9jmt8ulTdXFKdbKLNh+kOMvBzuVRa4Y7MUsdEUSWQe7xxCfZmcwjHU83LqzFvSbJQOXQvptbPnEFoyZtUUGwTeKuLuTHyT1kaP0P6cR01OKvv448gtl61dqZfmJezQmU/t+1R2fJLtBwXV6uWGwB9SZPrn0fKO2WAvQN1PUhHjTom3xgXYTkvlSKHs19OhslETq6X3HrXbjt8XbGj9b4Gi+lUAnL6XxQj8Pyk9N4Bt1xUrsLVN/3isYMug8rODMdbgOvoHs8uAb2fcANIAzkKCLYy+AXRpSU8sr1r4P67xhLgPp7vM32zlqt7Bhq2fI1Hwp+VgANxok59SsGV3oqdUL0YVDMRY7Yg8QLbVUU4NZNoOq5hJHuxEM28Sh/IyUZ8D3reR+yc58EGvOy2U0HQL6G9V+kWyEWHmzaMx6t4o9RhOm/riUiYrzqij4Ptqkn7AaCXqc+F47m04ahfde7YIz8RHEBN6BdVwdIGRVdNbKqYu1Hc0x0wBY4wqC8+XUgBGnj81SZsQB+0yAS1x/BlI/6ebHHk0lauQLuPDpu6EwAVJ7T0rl2uXa23jcqNyOZekhqYHRz3JOANrF4wCCmEs1f9D1lUe0n4NAATed80Y5e0Q7CO2TezM/BR6wKdgQzKbCF4uOQC3Bk0fKAzbFlyRWg3gksA/gmm7eOjrpaKX7fHlEW2xLbE6GZsPiCiShVzN7RG2xTz2G+OJtEqzdJ7APxy3MrSsV0VukXbKMp9lhs5BN6dr3CN+sySUaoxGwfRUM3I/gdPYONgVU+PLX4vUWm32AvUySarbONvcpV2RQEPKKjEBHFk01kQDGRblnn8ZuE9g+JUl8OWAPbkFK2K6JxhJVvF47FzYYnAN22ttwxKYCoH36rheEB7KG/HF/YUaa2G5JF+55tpyrl7B1WHM39HuP2N2EXPl1UBu8vbj4OjvD+NoTE4ssF+ScARgaJY1N7+u8bY/Y9BSM5PKwJbvMVab32YP5FB5TtcYVrGoASolVLTzI7kVsYVxRtAb5n2JXq1vCdtd47XtYItynrN0835PasLg0y13aOPbmPI+on2Lr9e5tjSHvgkAvclUjL3Fsdaw03IzgTR62yYClk7QMah4IQ0qSsoYYbOix6zJR1ZGDNMOY3Bb6W5S6jiyovep3t7bUPyoq7OkjYumrfESp8zSBc/OLosVf+nTnnKjsqR16++WDwpI8FxJWRFTlI6NKnqYJaL96TqjAbo9Toi5QiWBDcmfdFV+T8dkvFe5bItgstbM2X6QG2mVun+cazfRwOS0eiaeRRJKgLfc3BQAqfnhJyz8lfR6580SF/FXVu83Nz1xrrnFqqXL6Qxl47DNSm4RFflvN5sABDD8peouqLLKQXVdGbnqf+qIpOxON4ZyYdJEJ6sy4zS2c5eRPTT4Jyp46qDE5/ptAWqJOQ9e6yE82FXBbZCk1/tXVoshVoopE3CB0zmraI3nbqCJ/gW3ZMgtbC5nh/QHlOoOZBxQCRgAAAABJRU5ErkJggg==" alt="Symfony" />
                </div>

                <div class="search">
                  <form method="get" action="http://symfony.com/search">
                    <div class="form-row">

                      <label for="search-id">
                                <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAQAAAC1+jfqAAABUElEQVQoz2NgAIJ29iBdD0d7X2cPb+tY2f9MDMjgP2O2hKu7vS8CBlisZUNSMJ3fxRMkXO61wm2ue6I3iB1q8Z8ZriDZFCS03fm/wX+1/xp/TBo8QPxeqf+MUAW+QIFKj/+q/wX/c/3n/i/6Qd/bx943z/Q/K1SBI1D9fKv/AhCn/Wf5L5EHdFGKw39OqAIXoPpOMziX4T9/DFBBnuN/HqhAEtCKCNf/XDA/rZRyAmrpsvrPDVUw3wrkqCiLaewg6TohX1d7X0ffs5r/OaAKfinmgt3t4ulr4+Xg4ANip3j+l/zPArNT4LNOD0pAgWCSOUIBy3+h/+pXbBa5tni0eMx23+/mB1YSYnENroT5Pw/QSOX/mkCo+l/jgo0v2KJA643s8PgAmsMBDCbu/5xALHPB2husxN9uCzsDOgAq5kAoaZVnYMCh5Ky1r88Eh/+iABM8jUk7ClYIAAAAAElFTkSuQmCC" alt="Search on Symfony website" />
                      </label>

                      <input name="q" id="search-id" type="search" placeholder="Search on Symfony website" />

                      <button type="submit" class="sf-button">
                          <span class="border-l">
                            <span class="border-r">
                                <span class="btn-bg">OK</span>
                            </span>
                        </span>
                      </button>
                    </div>
                   </form>
                </div>
            </div>

            <div class="sf-reset">
                <div class="block">
                    <div class="symfony-block-content">
                        <h1 class="title">Configuration Checker</h1>
                        <p>
                            This script analyzes your system to check whether is
                            ready to run Symfony applications.
                        </p>

                        <?php if ($hasMajorProblems): ?>
                            <h2 class="ko">Major problems</h2>
                            <p>Major problems have been detected and <strong>must</strong> be fixed before continuing:</p>
                            <ol>
                                <?php foreach ($majorProblems as $problem): ?>
                                    <li><?php echo $problem->getTestMessage() ?>
                                        <p class="help"><em><?php echo $problem->getHelpHtml() ?></em></p>
                                    </li>
                                <?php endforeach; ?>
                            </ol>
                        <?php endif; ?>

                        <?php if ($hasMinorProblems): ?>
                            <h2>Recommendations</h2>
                            <p>
                                <?php if ($hasMajorProblems): ?>Additionally, to<?php else: ?>To<?php endif; ?> enhance your Symfony experience,
                                it’s recommended that you fix the following:
                            </p>
                            <ol>
                                <?php foreach ($minorProblems as $problem): ?>
                                    <li><?php echo $problem->getTestMessage() ?>
                                        <p class="help"><em><?php echo $problem->getHelpHtml() ?></em></p>
                                    </li>
                                <?php endforeach; ?>
                            </ol>
                        <?php endif; ?>

                        <?php if ($symfonyRequirements->hasPhpIniConfigIssue()): ?>
                            <p id="phpini">*
                                <?php if ($symfonyRequirements->getPhpIniConfigPath()): ?>
                                    Changes to the <strong>php.ini</strong> file must be done in "<strong><?php echo $symfonyRequirements->getPhpIniConfigPath() ?></strong>".
                                <?php else: ?>
                                    To change settings, create a "<strong>php.ini</strong>".
                                <?php endif; ?>
                            </p>
                        <?php endif; ?>

                        <?php if (!$hasMajorProblems && !$hasMinorProblems): ?>
                            <p class="ok">All checks passed successfully. Your system is ready to run Symfony applications.</p>
                        <?php endif; ?>

                        <ul class="symfony-install-continue">
                            <?php if ($hasMajorProblems || $hasMinorProblems): ?>
                                <li><a href="config.php">Re-check configuration</a></li>
                            <?php endif; ?>
                        </ul>
                    </div>
                </div>
            </div>
            <div class="version">Symfony Standard Edition</div>
        </div>
    </body>
</html>
```

## File: `web/robots.txt`
```
# www.robotstxt.org/
# www.google.com/support/webmasters/bin/answer.py?hl=en&answer=156449

User-agent: *
Disallow:
```


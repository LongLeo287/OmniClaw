---
id: github.com-jorge07-ddd-playground-a55a6efd-knowled
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:20:16.482762
---

# KNOWLEDGE EXTRACT: github.com_jorge07_ddd-playground_a55a6efd
> **Extracted on:** 2026-04-01 14:35:50
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007524002/github.com_jorge07_ddd-playground_a55a6efd

---

## File: `.dockerignore`
```
app/config/parameters.yml
etc/infrastructure/context-*/
doc/
report/
vendor/
web/bundles/
var/
!var/cache/.gitkeep
!var/logs/.gitkeep
!var/sessions/.gitkeep
```

## File: `.gitignore`
```
/app/config/parameters.yml
/build/
/composer.phar
/deptrac.phar
/vendor/
/web/bundles/
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
/phpunit.xml
report/
!report/.gitkeep
.idea/
```

## File: `.gitlab-ci.yml`
```yaml
stages:
  - build
  - test
  - aceptation
  - clean
  - release

before_script:
  - export RELEASE=${CI_BUILD_REF_NAME}
  - cd etc/infrastructure

build:
  stage: build
  script:
    - mkdir -p context-${RELEASE}/build
    - docker pull jorge07/alpine-php:7.1
    - docker pull jorge07/alpine-php:7.1-dev
    - docker-compose -p ${RELEASE} -f build/docker-compose.yml pull
    - docker-compose -p ${RELEASE} -f build/docker-compose.yml build
    - docker-compose -p ${RELEASE} -f build/docker-compose.yml up -d
    - docker exec sf-build-${RELEASE} ant build

test-mess-detector:
  stage: test
  script:
    - docker exec ${RELEASE}_fpm_1 ./vendor/bin/phpmd src text cleancode, codesize, controversial, design, naming, unusedcode
  allow_failure: true

test-deptrac:
  stage: test
  script:
    - docker exec ${RELEASE}_fpm_1 wget http://get.sensiolabs.de/deptrac.phar
    - docker exec ${RELEASE}_fpm_1 php deptrac.phar analyze --formatter-graphviz=0

test-coverage:
  stage: test
  script:
    - docker exec ${RELEASE}_fpm_1 ant unit-and-functional

aceptation:
  stage: aceptation
  script:
    - docker exec ${RELEASE}_fpm_1 ant acceptation

clean-build:
  stage: clean
  script:
    - docker-compose -p ${RELEASE} -f build/docker-compose.yml down --volumes
  when: always

release:tags:
  stage: release
  only:
    - tags

  script:
    - docker build -t sf-build-${RELEASE} -f build/fpm/Dockerfile ../../
    - docker run -d --name building-${RELEASE} sf-build-${RELEASE}
    - docker cp building-${RELEASE}:/app context-${RELEASE}/build/
    - docker rm -f building-${RELEASE}
    - cp -R prod/fpm context-${RELEASE}/build/fpm
    - cp -R prod/nginx context-${RELEASE}/build/nginx
    - docker login -u jorge07 -p ${GITLAB_PASSWORD} registry.gitlab.com
    - docker-compose -f prod/docker-compose.build.yml build
    - docker-compose -f prod/docker-compose.build.yml push
```

## File: `Jenkinsfile`
```
pipeline {

    agent any

    environment {
        APP_NAME = 'DDD'
    }

    stages {

        stage("Checkout") {
            steps {

                checkout scm
            }
        }

        stage("Environment") {
            steps {

                sh 'docker pull jorge07/alpine-php:7.1-dev-sf'
                sh "docker-compose -f etc/infrastructure/build/docker-compose.yml pull"
                sh "docker-compose -f etc/infrastructure/build/docker-compose.yml build"
                sh "docker-compose -f etc/infrastructure/build/docker-compose.yml up -d"
            }
        }

        stage("Build") {
            steps {

                sh "docker exec build_fpm_1 ant build"
            }
        }

        stage("Tests") {
            steps {

                parallel(
                    "Acceptation": {

                       sh "docker exec build_fpm_1 curl nginx"
                       sh "docker exec build_fpm_1 ant acceptation"
                    },
                    "Unit and functional": {

                       sh "docker exec build_fpm_1 ant unit-and-functional"
                    }
                )
            }
        }
    }

    post {
        success {

            echo 'ok'
            // slackSend (color: '#43A047', message: "${env.APP_NAME} -> All green. See: (${env.BUILD_URL})")
        }

        failure {

            echo 'ko'
            // slackSend (color: '#CF0000', message: "${env.APP_NAME} -> Ops! Something was wrong... See: (${env.BUILD_URL})")
        }
        always {

            sh "docker-compose -f etc/infrastructure/build/docker-compose.yml down --volumes"
        }
    }
}
```

## File: `README.md`
```markdown
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

## File: `behat.yml`
```yaml
default:
    suites:
        home:
            paths:
                - "%paths.base%/tests/UI/Behat/Features/Home"
            contexts:
                - Tests\Leos\UI\Behat\Context\Api\Home\HomeContext:
                    path: http://nginx
                    basePath: %paths.base%
                    responsesPath: %paths.base%/tests/UI/Responses/Home

        security:
            paths:
                - "%paths.base%/tests/UI/Behat/Features/Security"
            contexts:
                - Tests\Leos\UI\Behat\Context\Api\Security\SecurityContext:
                    path: http://nginx
                    basePath: %paths.base%
                    responsesPath: %paths.base%/tests/UI/Responses/Security

        wallet:
            paths:
                - "%paths.base%/tests/UI/Behat/Features/Wallet"
            contexts:
                - Tests\Leos\UI\Behat\Context\Api\Wallet\WalletContext:
                    path: http://nginx
                    basePath: %paths.base%
                    responsesPath: %paths.base%/tests/UI/Responses/Wallet

        monitor:
            paths:
                - "%paths.base%/tests/UI/Behat/Features/Monitor"
            contexts:
                - Tests\Leos\UI\Behat\Context\Api\Monitor\MonitorContext:
                    path: http://nginx
                    basePath: %paths.base%
                    responsesPath: %paths.base%/tests/UI/Responses/Monitor
```

## File: `build.xml`
```xml
<?xml version="1.0" encoding="UTF-8"?>

<project name="Leos" default="build">
    <property name="workspace" value="/app"/>
    <property name="sourcedir" value="${workspace}/src"/>
    <property name="consoledir" value="${workspace}/bin"/>
    <property name="vardir" value="${workspace}/var"/>
    <property name="vendordir" value="${workspace}/vendor"/>
    <property name="bindir" value="${vendordir}/bin"/>

    <target name="clean" description="Cleanup build artifacts">
        <delete dir="${workspace}/report"/>
    </target>

    <target name="waitfor" description="wait for mysql socket">
        <waitfor>
            <socket server="mysql" port="3306"/>
        </waitfor>
    </target>

    <target name="prepare" depends="clean" description="Prepare for build">
        <mkdir dir="${workspace}/report"/>
    </target>

    <target name="createdatabase" description="Load fixtures">
        <exec executable="php" failonerror="false">
            <arg value="${consoledir}/console"/>
            <arg value="doctrine:database:drop"/>
            <arg value="--force"/>
            <arg value="--no-interaction"/>
        </exec>

        <exec executable="php" failonerror="true">
            <arg value="${consoledir}/console"/>
            <arg value="doctrine:database:create"/>
            <arg value="--no-interaction"/>
        </exec>

        <exec executable="php" failonerror="true">
            <arg value="${consoledir}/console"/>
            <arg value="doctrine:schema:create"/>
            <arg value="--no-interaction"/>
        </exec>

    </target>


    <target name="createdatabase-test" description="Load fixtures">
        <exec executable="php" failonerror="false">
            <arg value="${consoledir}/console"/>
            <arg value="doctrine:database:drop"/>
            <arg value="--force"/>
            <arg value="--no-interaction"/>
            <arg value="--env=test"/>
        </exec>

        <exec executable="php" failonerror="true">
            <arg value="${consoledir}/console"/>
            <arg value="doctrine:database:create"/>
            <arg value="--no-interaction"/>
            <arg value="--env=test"/>
        </exec>

        <exec executable="php" failonerror="true">
            <arg value="${consoledir}/console"/>
            <arg value="doctrine:schema:create"/>
            <arg value="--no-interaction"/>
            <arg value="--env=test"/>
        </exec>

    </target>

    <target name="apidoc" description="Dump an HTML file with the API documentation">
        <exec executable="php" output="${workspace}/doc/api_doc.html">
            <arg value="${consoledir}/console" />
            <arg value="api:doc:dump" />
            <arg value="--format=html" />
        </exec>
    </target>

    <target name="cachewarm" description="Wipe test and dev caches">
        <delete dir="${project.basedir}/var/cache/dev"/>
        <delete dir="${project.basedir}/var/cache/test"/>
        <exec executable="php">
            <arg value="${consoledir}/console"/>
            <arg value="cache:w"/>
        </exec>
        <exec executable="php">
            <arg value="${consoledir}/console"/>
            <arg value="cache:w"/>
            <arg value="--env=test"/>
        </exec>
    </target>

    <target name="phpunit" description="Run PHPUnit tests">
        <exec executable="${bindir}/phpunit" failonerror="true">
            <arg value="-c"/>
            <arg path="${workspace}/phpunit.xml.dist"/>
        </exec>
    </target>

    <target name="behat" description="Run Behat tests">
        <exec executable="${bindir}/behat" failonerror="true">
            <arg value="-c"/>
            <arg path="${workspace}/behat.yml"/>
            <arg value="-f"/>
            <arg value="progress"/>
        </exec>
    </target>

    <target name="build" depends="waitfor, prepare, createdatabase, createdatabase-test" description="Prepare project dependencies"/>
    <target name="unit-and-functional" depends="cachewarm, phpunit" description="Run project unit and functional tests"/>
    <target name="acceptation" depends="cachewarm, behat" description="Run project acceptation tests"/>
</project>
```

## File: `composer.json`
```json
{
    "name": "jorge.arco/ddd",
    "license": "proprietary",
    "type": "project",
    "autoload": {
        "psr-4": {
            "Leos\\": "src"
        },
        "classmap": [
            "app/AppKernel.php",
            "app/AppCache.php"
        ]
    },
    "autoload-dev": {
        "psr-4": {
            "Tests\\Leos\\": "tests/"
        }
    },
    "require": {
        "php": ">=7.0.1",
        "symfony/symfony": "3.3.*",
        "doctrine/orm": "^2.5",
        "doctrine/doctrine-bundle": "^1.6",
        "doctrine/doctrine-cache-bundle": "^1.2",
        "symfony/swiftmailer-bundle": "^2.3",
        "symfony/monolog-bundle": "^2.8",
        "symfony/polyfill-apcu": "^1.0",
        "sensio/distribution-bundle": "^5.0",
        "sensio/framework-extra-bundle": "^3.0.2",
        "incenteev/composer-parameter-handler": "^2.0",

        "ramsey/uuid": "^3.5",
        "snc/redis-bundle": "2.x-dev",
        "predis/predis": "^1.0",

        "nelmio/api-doc-bundle": "^2.13",
        "friendsofsymfony/rest-bundle": "^2.2",
        "jms/serializer-bundle": "^2.2",
        "white-october/pagerfanta-bundle": "^1.0",
        "willdurand/hateoas-bundle": "^1.3",
        "lexik/jwt-authentication-bundle": "^2.4",
        "ramsey/uuid-doctrine": "^1.4",
        "league/tactician-bundle": "1.0",
        "php-amqplib/rabbitmq-bundle": "^1.13",
        "league/tactician-doctrine": "^1.1",
        "friendsofsymfony/elastica-bundle": "^4.0"
    },
    "require-dev": {
        "sensio/generator-bundle": "^3.0",
        "symfony/phpunit-bridge": "^3.0",
        "phpunit/phpunit": "^6",
        "lakion/api-test-case": "^2.0",
        "behat/symfony2-extension": "^2.1",
        "guzzlehttp/guzzle": "^6.2",
        "behat/behat": "^3.1",
        "symfony/psr-http-message-bridge": "^0.2.0",
        "phpmd/phpmd": "^2.4"
    },
    "scripts": {
        "post-install-cmd": [
            "Incenteev\\ParameterHandler\\ScriptHandler::buildParameters",
            "Sensio\\Bundle\\DistributionBundle\\Composer\\ScriptHandler::buildBootstrap",
            "Sensio\\Bundle\\DistributionBundle\\Composer\\ScriptHandler::clearCache",
            "Sensio\\Bundle\\DistributionBundle\\Composer\\ScriptHandler::installAssets",
            "Sensio\\Bundle\\DistributionBundle\\Composer\\ScriptHandler::installRequirementsFile",
            "Sensio\\Bundle\\DistributionBundle\\Composer\\ScriptHandler::prepareDeploymentTarget"
        ],
        "post-update-cmd": [
            "Incenteev\\ParameterHandler\\ScriptHandler::buildParameters",
            "Sensio\\Bundle\\DistributionBundle\\Composer\\ScriptHandler::buildBootstrap",
            "Sensio\\Bundle\\DistributionBundle\\Composer\\ScriptHandler::clearCache",
            "Sensio\\Bundle\\DistributionBundle\\Composer\\ScriptHandler::installAssets",
            "Sensio\\Bundle\\DistributionBundle\\Composer\\ScriptHandler::installRequirementsFile",
            "Sensio\\Bundle\\DistributionBundle\\Composer\\ScriptHandler::prepareDeploymentTarget"
        ]
    },
    "config": {
        "platform": {
            "php": "7.0.9"
        }
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
        }
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
    "content-hash": "257157a936246cf570ac264ceeffe483",
    "packages": [
        {
            "name": "composer/ca-bundle",
            "version": "1.0.8",
            "source": {
                "type": "git",
                "url": "https://github.com/composer/ca-bundle.git",
                "reference": "9dd73a03951357922d8aee6cc084500de93e2343"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/composer/ca-bundle/zipball/9dd73a03951357922d8aee6cc084500de93e2343",
                "reference": "9dd73a03951357922d8aee6cc084500de93e2343",
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
            "time": "2017-09-11T07:24:36+00:00"
        },
        {
            "name": "doctrine/annotations",
            "version": "v1.4.0",
            "source": {
                "type": "git",
                "url": "https://github.com/doctrine/annotations.git",
                "reference": "54cacc9b81758b14e3ce750f205a393d52339e97"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/doctrine/annotations/zipball/54cacc9b81758b14e3ce750f205a393d52339e97",
                "reference": "54cacc9b81758b14e3ce750f205a393d52339e97",
                "shasum": ""
            },
            "require": {
                "doctrine/lexer": "1.*",
                "php": "^5.6 || ^7.0"
            },
            "require-dev": {
                "doctrine/cache": "1.*",
                "phpunit/phpunit": "^5.7"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.4.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Doctrine\\Common\\Annotations\\": "lib/Doctrine/Common/Annotations"
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
            "time": "2017-02-24T16:22:25+00:00"
        },
        {
            "name": "doctrine/cache",
            "version": "v1.6.2",
            "source": {
                "type": "git",
                "url": "https://github.com/doctrine/cache.git",
                "reference": "eb152c5100571c7a45470ff2a35095ab3f3b900b"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/doctrine/cache/zipball/eb152c5100571c7a45470ff2a35095ab3f3b900b",
                "reference": "eb152c5100571c7a45470ff2a35095ab3f3b900b",
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
            "time": "2017-07-22T12:49:21+00:00"
        },
        {
            "name": "doctrine/collections",
            "version": "v1.4.0",
            "source": {
                "type": "git",
                "url": "https://github.com/doctrine/collections.git",
                "reference": "1a4fb7e902202c33cce8c55989b945612943c2ba"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/doctrine/collections/zipball/1a4fb7e902202c33cce8c55989b945612943c2ba",
                "reference": "1a4fb7e902202c33cce8c55989b945612943c2ba",
                "shasum": ""
            },
            "require": {
                "php": "^5.6 || ^7.0"
            },
            "require-dev": {
                "doctrine/coding-standard": "~0.1@dev",
                "phpunit/phpunit": "^5.7"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.3.x-dev"
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
            "time": "2017-01-03T10:49:41+00:00"
        },
        {
            "name": "doctrine/common",
            "version": "v2.7.3",
            "source": {
                "type": "git",
                "url": "https://github.com/doctrine/common.git",
                "reference": "4acb8f89626baafede6ee5475bc5844096eba8a9"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/doctrine/common/zipball/4acb8f89626baafede6ee5475bc5844096eba8a9",
                "reference": "4acb8f89626baafede6ee5475bc5844096eba8a9",
                "shasum": ""
            },
            "require": {
                "doctrine/annotations": "1.*",
                "doctrine/cache": "1.*",
                "doctrine/collections": "1.*",
                "doctrine/inflector": "1.*",
                "doctrine/lexer": "1.*",
                "php": "~5.6|~7.0"
            },
            "require-dev": {
                "phpunit/phpunit": "^5.4.6"
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
            "time": "2017-07-22T08:35:12+00:00"
        },
        {
            "name": "doctrine/dbal",
            "version": "v2.5.13",
            "source": {
                "type": "git",
                "url": "https://github.com/doctrine/dbal.git",
                "reference": "729340d8d1eec8f01bff708e12e449a3415af873"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/doctrine/dbal/zipball/729340d8d1eec8f01bff708e12e449a3415af873",
                "reference": "729340d8d1eec8f01bff708e12e449a3415af873",
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
            "time": "2017-07-22T20:44:48+00:00"
        },
        {
            "name": "doctrine/doctrine-bundle",
            "version": "1.6.10",
            "source": {
                "type": "git",
                "url": "https://github.com/doctrine/DoctrineBundle.git",
                "reference": "d276b1849ce1c252d3e0993e4ae1f0424118be8f"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/doctrine/DoctrineBundle/zipball/d276b1849ce1c252d3e0993e4ae1f0424118be8f",
                "reference": "d276b1849ce1c252d3e0993e4ae1f0424118be8f",
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
            "time": "2017-09-29T17:50:40+00:00"
        },
        {
            "name": "doctrine/doctrine-cache-bundle",
            "version": "1.3.1",
            "source": {
                "type": "git",
                "url": "https://github.com/doctrine/DoctrineCacheBundle.git",
                "reference": "cfc629363a4a1d7b3f21c4689c53aa05519eed52"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/doctrine/DoctrineCacheBundle/zipball/cfc629363a4a1d7b3f21c4689c53aa05519eed52",
                "reference": "cfc629363a4a1d7b3f21c4689c53aa05519eed52",
                "shasum": ""
            },
            "require": {
                "doctrine/cache": "^1.4.2",
                "doctrine/inflector": "~1.0",
                "php": ">=5.3.2",
                "symfony/doctrine-bridge": "~2.2|~3.0|~4.0"
            },
            "require-dev": {
                "instaclick/coding-standard": "~1.1",
                "instaclick/object-calisthenics-sniffs": "dev-master",
                "instaclick/symfony2-coding-standard": "dev-remaster",
                "phpunit/phpunit": "~4",
                "predis/predis": "~0.8",
                "satooshi/php-coveralls": "^1.0",
                "squizlabs/php_codesniffer": "~1.5",
                "symfony/console": "~2.2|~3.0|~4.0",
                "symfony/finder": "~2.2|~3.0|~4.0",
                "symfony/framework-bundle": "~2.2|~3.0|~4.0",
                "symfony/phpunit-bridge": "~2.7|~3.0|~4.0",
                "symfony/security-acl": "~2.3|~3.0",
                "symfony/validator": "~2.2|~3.0|~4.0",
                "symfony/yaml": "~2.2|~3.0|~4.0"
            },
            "suggest": {
                "symfony/security-acl": "For using this bundle to cache ACLs"
            },
            "type": "symfony-bundle",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.3.x-dev"
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
            "time": "2017-09-29T14:39:10+00:00"
        },
        {
            "name": "doctrine/inflector",
            "version": "v1.2.0",
            "source": {
                "type": "git",
                "url": "https://github.com/doctrine/inflector.git",
                "reference": "e11d84c6e018beedd929cff5220969a3c6d1d462"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/doctrine/inflector/zipball/e11d84c6e018beedd929cff5220969a3c6d1d462",
                "reference": "e11d84c6e018beedd929cff5220969a3c6d1d462",
                "shasum": ""
            },
            "require": {
                "php": "^7.0"
            },
            "require-dev": {
                "phpunit/phpunit": "^6.2"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.2.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Doctrine\\Common\\Inflector\\": "lib/Doctrine/Common/Inflector"
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
            "time": "2017-07-22T12:18:28+00:00"
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
            "version": "v2.5.11",
            "source": {
                "type": "git",
                "url": "https://github.com/doctrine/doctrine2.git",
                "reference": "249b737094f1e7cba4f0a8d19acf5be6cf3ed504"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/doctrine/doctrine2/zipball/249b737094f1e7cba4f0a8d19acf5be6cf3ed504",
                "reference": "249b737094f1e7cba4f0a8d19acf5be6cf3ed504",
                "shasum": ""
            },
            "require": {
                "doctrine/cache": "~1.4",
                "doctrine/collections": "~1.2",
                "doctrine/common": ">=2.5-dev,<2.9-dev",
                "doctrine/dbal": ">=2.5-dev,<2.7-dev",
                "doctrine/instantiator": "^1.0.1",
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
            "time": "2017-09-18T06:50:20+00:00"
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
            "name": "friendsofsymfony/elastica-bundle",
            "version": "v4.0.1",
            "source": {
                "type": "git",
                "url": "https://github.com/FriendsOfSymfony/FOSElasticaBundle.git",
                "reference": "454f8d8d4cb99add96f08e1e38652ccbcd5d5542"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/FriendsOfSymfony/FOSElasticaBundle/zipball/454f8d8d4cb99add96f08e1e38652ccbcd5d5542",
                "reference": "454f8d8d4cb99add96f08e1e38652ccbcd5d5542",
                "shasum": ""
            },
            "require": {
                "php": ">=5.5.0",
                "psr/log": "~1.0",
                "ruflin/elastica": "3.2.*",
                "symfony/asset": "~2.7|~3.0",
                "symfony/console": "~2.7|~3.0",
                "symfony/form": "~2.7|~3.0",
                "symfony/framework-bundle": "~2.7|~3.0",
                "symfony/property-access": "~2.7|~3.0",
                "symfony/templating": "~2.7|~3.0",
                "symfony/translation": "~2.7|~3.0"
            },
            "require-dev": {
                "doctrine/doctrine-bundle": "~1.6",
                "doctrine/orm": "~2.4",
                "doctrine/phpcr-bundle": "~1.2",
                "jackalope/jackalope-doctrine-dbal": "~1.1",
                "jms/serializer-bundle": "~1.1",
                "knplabs/knp-components": "~1.2",
                "knplabs/knp-paginator-bundle": "~2.4",
                "pagerfanta/pagerfanta": "~1.0",
                "phpunit/phpunit": "~4.8|~5.0",
                "propel/propel1": "1.6.*",
                "symfony/browser-kit": "~2.7|~3.0",
                "symfony/dependency-injection": "~2.7|~3.0",
                "symfony/expression-language": "~2.7|~3.0",
                "symfony/serializer": "~2.7|~3.0",
                "symfony/twig-bundle": "~2.7|~3.0",
                "symfony/validator": "~2.7|~3.0",
                "symfony/yaml": "~2.7|~3.0"
            },
            "type": "symfony-bundle",
            "extra": {
                "branch-alias": {
                    "dev-master": "4.0.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "FOS\\ElasticaBundle\\": ""
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Tim Nagel",
                    "email": "tim@nagel.com.au"
                },
                {
                    "name": "Richard Miller",
                    "email": "richard.miller@limethinking.co.uk"
                },
                {
                    "name": "FriendsOfSymfony Community",
                    "homepage": "https://github.com/FriendsOfSymfony/FOSElasticaBundle/contributors"
                },
                {
                    "name": "Jeremy Mikola",
                    "email": "jmikola@gmail.com"
                }
            ],
            "description": "Elasticsearch PHP integration for your Symfony2 project using Elastica",
            "homepage": "https://github.com/FriendsOfSymfony/FOSElasticaBundle",
            "keywords": [
                "doctrine2",
                "elastica",
                "elasticsearch",
                "mongodb",
                "propel",
                "search"
            ],
            "time": "2017-08-10T13:45:18+00:00"
        },
        {
            "name": "friendsofsymfony/rest-bundle",
            "version": "2.2.0",
            "source": {
                "type": "git",
                "url": "https://github.com/FriendsOfSymfony/FOSRestBundle.git",
                "reference": "d62a6c0f4bc699f899865d7e7bc7a4186aef9a86"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/FriendsOfSymfony/FOSRestBundle/zipball/d62a6c0f4bc699f899865d7e7bc7a4186aef9a86",
                "reference": "d62a6c0f4bc699f899865d7e7bc7a4186aef9a86",
                "shasum": ""
            },
            "require": {
                "doctrine/inflector": "^1.0",
                "php": "^5.5.9|~7.0",
                "psr/log": "^1.0",
                "symfony/config": "^2.7|^3.0",
                "symfony/debug": "^2.7|^3.0",
                "symfony/dependency-injection": "^2.7|^3.0",
                "symfony/event-dispatcher": "^2.7|^3.0",
                "symfony/finder": "^2.7|^3.0",
                "symfony/framework-bundle": "^2.7|^3.0",
                "symfony/http-foundation": "^2.7|^3.0",
                "symfony/http-kernel": "^2.7|^3.0",
                "symfony/routing": "^2.7|^3.0",
                "symfony/security-core": "^2.7|^3.0",
                "symfony/templating": "^2.7|^3.0",
                "willdurand/jsonp-callback-validator": "^1.0",
                "willdurand/negotiation": "^2.0"
            },
            "conflict": {
                "jms/serializer": "1.3.0",
                "sensio/framework-extra-bundle": "<3.0.13"
            },
            "require-dev": {
                "jms/serializer-bundle": "^1.0",
                "phpoption/phpoption": "^1.1",
                "psr/http-message": "^1.0",
                "sensio/framework-extra-bundle": "^3.0.13",
                "symfony/asset": "^2.7|^3.0",
                "symfony/browser-kit": "^2.7|^3.0",
                "symfony/css-selector": "^2.7|^3.0",
                "symfony/dependency-injection": "^2.7|^3.0",
                "symfony/expression-language": "~2.7|^3.0",
                "symfony/form": "^2.7|^3.0",
                "symfony/phpunit-bridge": "^3.2",
                "symfony/security-bundle": "^2.7|^3.0",
                "symfony/serializer": "^2.7.11|^3.0.4",
                "symfony/twig-bundle": "^2.7|^3.0",
                "symfony/validator": "^2.7|^3.0",
                "symfony/web-profiler-bundle": "^2.7|^3.0",
                "symfony/yaml": "^2.7|^3.0"
            },
            "suggest": {
                "jms/serializer-bundle": "Add support for advanced serialization capabilities, recommended, requires ^1.0",
                "sensio/framework-extra-bundle": "Add support for route annotations and the view response listener, requires ^3.0",
                "symfony/expression-language": "Add support for using the expression language in the routing, requires ^2.7|^3.0",
                "symfony/serializer": "Add support for basic serialization capabilities and xml decoding, requires ^2.7|^3.0",
                "symfony/validator": "Add support for validation capabilities in the ParamFetcher, requires ^2.7|^3.0"
            },
            "type": "symfony-bundle",
            "extra": {
                "branch-alias": {
                    "dev-master": "2.2-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "FOS\\RestBundle\\": ""
                },
                "exclude-from-classmap": [
                    "Tests/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Lukas Kahwe Smith",
                    "email": "smith@pooteeweet.org"
                },
                {
                    "name": "FriendsOfSymfony Community",
                    "homepage": "https://github.com/friendsofsymfony/FOSRestBundle/contributors"
                },
                {
                    "name": "Konstantin Kudryashov",
                    "email": "ever.zet@gmail.com"
                }
            ],
            "description": "This Bundle provides various tools to rapidly develop RESTful API's with Symfony",
            "homepage": "http://friendsofsymfony.github.com",
            "keywords": [
                "rest"
            ],
            "time": "2017-04-06T12:55:03+00:00"
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
            "name": "jms/metadata",
            "version": "1.6.0",
            "source": {
                "type": "git",
                "url": "https://github.com/schmittjoh/metadata.git",
                "reference": "6a06970a10e0a532fb52d3959547123b84a3b3ab"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/schmittjoh/metadata/zipball/6a06970a10e0a532fb52d3959547123b84a3b3ab",
                "reference": "6a06970a10e0a532fb52d3959547123b84a3b3ab",
                "shasum": ""
            },
            "require": {
                "php": ">=5.3.0"
            },
            "require-dev": {
                "doctrine/cache": "~1.0",
                "symfony/cache": "~3.1"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.5.x-dev"
                }
            },
            "autoload": {
                "psr-0": {
                    "Metadata\\": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "Apache-2.0"
            ],
            "authors": [
                {
                    "name": "Johannes M. Schmitt",
                    "email": "schmittjoh@gmail.com"
                }
            ],
            "description": "Class/method/property metadata management in PHP",
            "keywords": [
                "annotations",
                "metadata",
                "xml",
                "yaml"
            ],
            "time": "2016-12-05T10:18:33+00:00"
        },
        {
            "name": "jms/parser-lib",
            "version": "1.0.0",
            "source": {
                "type": "git",
                "url": "https://github.com/schmittjoh/parser-lib.git",
                "reference": "c509473bc1b4866415627af0e1c6cc8ac97fa51d"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/schmittjoh/parser-lib/zipball/c509473bc1b4866415627af0e1c6cc8ac97fa51d",
                "reference": "c509473bc1b4866415627af0e1c6cc8ac97fa51d",
                "shasum": ""
            },
            "require": {
                "phpoption/phpoption": ">=0.9,<2.0-dev"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.0-dev"
                }
            },
            "autoload": {
                "psr-0": {
                    "JMS\\": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "Apache2"
            ],
            "description": "A library for easily creating recursive-descent parsers.",
            "time": "2012-11-18T18:08:43+00:00"
        },
        {
            "name": "jms/serializer",
            "version": "1.9.0",
            "source": {
                "type": "git",
                "url": "https://github.com/schmittjoh/serializer.git",
                "reference": "f4683f41ebf21e60667447bb49939bee35807c3c"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/schmittjoh/serializer/zipball/f4683f41ebf21e60667447bb49939bee35807c3c",
                "reference": "f4683f41ebf21e60667447bb49939bee35807c3c",
                "shasum": ""
            },
            "require": {
                "doctrine/annotations": "^1.0",
                "doctrine/instantiator": "^1.0.3",
                "jms/metadata": "~1.1",
                "jms/parser-lib": "1.*",
                "php": ">=5.5.0",
                "phpcollection/phpcollection": "~0.1",
                "phpoption/phpoption": "^1.1"
            },
            "conflict": {
                "jms/serializer-bundle": "<1.2.1",
                "twig/twig": "<1.12"
            },
            "require-dev": {
                "doctrine/orm": "~2.1",
                "doctrine/phpcr-odm": "^1.3|^2.0",
                "ext-pdo_sqlite": "*",
                "jackalope/jackalope-doctrine-dbal": "^1.1.5",
                "phpunit/phpunit": "^4.8|^5.0",
                "propel/propel1": "~1.7",
                "symfony/expression-language": "^2.6|^3.0",
                "symfony/filesystem": "^2.1",
                "symfony/form": "~2.1|^3.0",
                "symfony/translation": "^2.1|^3.0",
                "symfony/validator": "^2.2|^3.0",
                "symfony/yaml": "^2.1|^3.0",
                "twig/twig": "~1.12|~2.0"
            },
            "suggest": {
                "doctrine/cache": "Required if you like to use cache functionality.",
                "doctrine/collections": "Required if you like to use doctrine collection types as ArrayCollection.",
                "symfony/yaml": "Required if you'd like to serialize data to YAML format."
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.9-dev"
                }
            },
            "autoload": {
                "psr-0": {
                    "JMS\\Serializer": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "Apache-2.0"
            ],
            "authors": [
                {
                    "name": "Asmir Mustafic",
                    "email": "goetas@gmail.com"
                },
                {
                    "name": "Johannes M. Schmitt",
                    "email": "schmittjoh@gmail.com"
                }
            ],
            "description": "Library for (de-)serializing data of any complexity; supports XML, JSON, and YAML.",
            "homepage": "http://jmsyst.com/libs/serializer",
            "keywords": [
                "deserialization",
                "jaxb",
                "json",
                "serialization",
                "xml"
            ],
            "time": "2017-09-28T15:17:28+00:00"
        },
        {
            "name": "jms/serializer-bundle",
            "version": "2.2.0",
            "source": {
                "type": "git",
                "url": "https://github.com/schmittjoh/JMSSerializerBundle.git",
                "reference": "dd40bfcb58ce01a950393f258d3d02a8dc4f4127"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/schmittjoh/JMSSerializerBundle/zipball/dd40bfcb58ce01a950393f258d3d02a8dc4f4127",
                "reference": "dd40bfcb58ce01a950393f258d3d02a8dc4f4127",
                "shasum": ""
            },
            "require": {
                "jms/serializer": "^1.9",
                "php": "^5.4|^7.0",
                "phpoption/phpoption": "^1.1.0",
                "symfony/framework-bundle": "~2.3|~3.0|~4.0"
            },
            "require-dev": {
                "doctrine/doctrine-bundle": "*",
                "doctrine/orm": "*",
                "phpunit/phpunit": "^4.8.35|^5.4.3|^6.0",
                "symfony/browser-kit": "*",
                "symfony/class-loader": "*",
                "symfony/css-selector": "*",
                "symfony/expression-language": "~2.6|~3.0|~4.0",
                "symfony/finder": "*",
                "symfony/form": "*",
                "symfony/process": "*",
                "symfony/stopwatch": "*",
                "symfony/twig-bundle": "*",
                "symfony/validator": "*",
                "symfony/yaml": "*"
            },
            "suggest": {
                "jms/di-extra-bundle": "Required to get lazy loading (de)serialization visitors, ~1.3"
            },
            "type": "symfony-bundle",
            "extra": {
                "branch-alias": {
                    "dev-master": "2.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "JMS\\SerializerBundle\\": ""
                },
                "exclude-from-classmap": [
                    "/Tests/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "Apache-2.0"
            ],
            "authors": [
                {
                    "name": "Asmir Mustafic",
                    "email": "goetas@gmail.com"
                },
                {
                    "name": "Johannes M. Schmitt",
                    "email": "schmittjoh@gmail.com"
                }
            ],
            "description": "Allows you to easily serialize, and deserialize data of any complexity",
            "homepage": "http://jmsyst.com/bundles/JMSSerializerBundle",
            "keywords": [
                "deserialization",
                "jaxb",
                "json",
                "serialization",
                "xml"
            ],
            "time": "2017-09-29T08:48:26+00:00"
        },
        {
            "name": "league/tactician",
            "version": "v1.0.2",
            "source": {
                "type": "git",
                "url": "https://github.com/thephpleague/tactician.git",
                "reference": "1f3aaad497f07a8bef147a37c7e3f2f7c23fcd21"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/thephpleague/tactician/zipball/1f3aaad497f07a8bef147a37c7e3f2f7c23fcd21",
                "reference": "1f3aaad497f07a8bef147a37c7e3f2f7c23fcd21",
                "shasum": ""
            },
            "require": {
                "php": ">=5.5"
            },
            "require-dev": {
                "mockery/mockery": "~0.9",
                "phpunit/phpunit": "~4.3",
                "squizlabs/php_codesniffer": "~2.3"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "2.0-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "League\\Tactician\\": "src"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Ross Tuck",
                    "homepage": "http://tactician.thephpleague.com"
                }
            ],
            "description": "A small, flexible command bus. Handy for building service layers.",
            "keywords": [
                "command",
                "command bus",
                "service layer"
            ],
            "time": "2016-02-20T11:14:36+00:00"
        },
        {
            "name": "league/tactician-bundle",
            "version": "v1.0",
            "source": {
                "type": "git",
                "url": "https://github.com/thephpleague/tactician-bundle.git",
                "reference": "f0c7d41bed86cec6e12e5ae2e95a24883848b04c"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/thephpleague/tactician-bundle/zipball/f0c7d41bed86cec6e12e5ae2e95a24883848b04c",
                "reference": "f0c7d41bed86cec6e12e5ae2e95a24883848b04c",
                "shasum": ""
            },
            "require": {
                "league/tactician": "^1.0",
                "league/tactician-container": "^2.0",
                "php": ">=7.0",
                "symfony/config": "^2.8|^3.0",
                "symfony/dependency-injection": "^2.8|^3.0",
                "symfony/http-kernel": "^2.8|^3.0",
                "symfony/yaml": "^2.8|^3.0"
            },
            "require-dev": {
                "league/tactician-doctrine": "^1.1",
                "matthiasnoback/symfony-config-test": "^3.0",
                "matthiasnoback/symfony-dependency-injection-test": "^2.1",
                "mockery/mockery": "~0.9.9",
                "phpunit/phpunit": "~6.1",
                "symfony/framework-bundle": "^2.8|^3.0",
                "symfony/security": "^2.8|^3.0",
                "symfony/security-bundle": "^2.8|^3.0",
                "symfony/validator": "^2.8|^3.0"
            },
            "suggest": {
                "league/tactician-doctrine": "For doctrine transaction middleware",
                "symfony/security": "For command security middleware",
                "symfony/validator": "For command validator middleware"
            },
            "type": "symfony-bundle",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.0-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "League\\Tactician\\Bundle\\": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Rafael Dohms",
                    "homepage": "http://doh.ms"
                },
                {
                    "name": "Xander Smalbil",
                    "email": "xander@videofunk.nl"
                },
                {
                    "name": "Richard Tuin",
                    "homepage": "http://www.rtuin.nl/"
                },
                {
                    "name": "Ross Tuck",
                    "email": "me@rosstuck.com"
                }
            ],
            "description": "Bundle to integrate Tactician with Symfony projects",
            "keywords": [
                "bundle",
                "symfony",
                "tactician"
            ],
            "time": "2017-08-11T05:40:40+00:00"
        },
        {
            "name": "league/tactician-container",
            "version": "2.0.0",
            "source": {
                "type": "git",
                "url": "https://github.com/thephpleague/tactician-container.git",
                "reference": "d1a5d884e072b8cafbff802d07766076eb2ffcb0"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/thephpleague/tactician-container/zipball/d1a5d884e072b8cafbff802d07766076eb2ffcb0",
                "reference": "d1a5d884e072b8cafbff802d07766076eb2ffcb0",
                "shasum": ""
            },
            "require": {
                "league/tactician": "^1.0",
                "php": ">=5.5",
                "psr/container": "^1.0"
            },
            "require-dev": {
                "league/container": "~2.3",
                "phpunit/phpunit": "~4.3",
                "squizlabs/php_codesniffer": "~2.0"
            },
            "type": "library",
            "autoload": {
                "psr-4": {
                    "League\\Tactician\\Container\\": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Nigel Greenway",
                    "homepage": "http://futurepixels.co.uk"
                }
            ],
            "description": "Tactician integration for any container implementing PSR-11",
            "keywords": [
                "container",
                "container-interop",
                "di",
                "interoperable",
                "league",
                "tactician"
            ],
            "time": "2017-04-13T06:27:12+00:00"
        },
        {
            "name": "league/tactician-doctrine",
            "version": "v1.1",
            "source": {
                "type": "git",
                "url": "https://github.com/thephpleague/tactician-doctrine.git",
                "reference": "f5a214a110d07dabdd05ee7fb3a155af2d1c0e6c"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/thephpleague/tactician-doctrine/zipball/f5a214a110d07dabdd05ee7fb3a155af2d1c0e6c",
                "reference": "f5a214a110d07dabdd05ee7fb3a155af2d1c0e6c",
                "shasum": ""
            },
            "require": {
                "doctrine/dbal": "^2.4",
                "league/tactician": "^1.0",
                "php": ">=5.5"
            },
            "require-dev": {
                "doctrine/orm": "~2.4",
                "mockery/mockery": "~0.9.7",
                "phpunit/phpunit": "~4.8",
                "squizlabs/php_codesniffer": "~2.0"
            },
            "suggest": {
                "doctrine/orm": "Required if you need to use ORM Transaction Middleware"
            },
            "type": "library",
            "autoload": {
                "psr-4": {
                    "League\\Tactician\\Doctrine\\": "src"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Ross Tuck"
                }
            ],
            "description": "Plugins for Tactician commands using Doctrine, like wrapping every command in a transaction",
            "homepage": "https://github.com/thephpleague/tactician-doctrine",
            "keywords": [
                "command bus",
                "doctrine",
                "tactician",
                "transactions"
            ],
            "time": "2017-01-05T09:49:53+00:00"
        },
        {
            "name": "lexik/jwt-authentication-bundle",
            "version": "v2.4.1",
            "source": {
                "type": "git",
                "url": "https://github.com/lexik/LexikJWTAuthenticationBundle.git",
                "reference": "7f213110d12315514879d44d8b90134ec99c24be"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/lexik/LexikJWTAuthenticationBundle/zipball/7f213110d12315514879d44d8b90134ec99c24be",
                "reference": "7f213110d12315514879d44d8b90134ec99c24be",
                "shasum": ""
            },
            "require": {
                "namshi/jose": "^7.2",
                "php": "^5.5|^7.0",
                "symfony/console": "^2.8|^3.0",
                "symfony/framework-bundle": "^2.8|^3.0",
                "symfony/security-bundle": "^2.8|^3.0"
            },
            "require-dev": {
                "friendsofphp/php-cs-fixer": "^1.1",
                "lcobucci/jwt": "~3.2",
                "phpunit/phpunit": "^4.8|^5.0",
                "symfony/browser-kit": "^2.8|^3.0",
                "symfony/dom-crawler": "^2.8|^3.0",
                "symfony/phpunit-bridge": "~3.2",
                "symfony/yaml": "^2.8|^3.0"
            },
            "suggest": {
                "gesdinet/jwt-refresh-token-bundle": "Implements a refresh token system over Json Web Tokens in Symfony",
                "lcobucci/jwt": "For using the LcobucciJWTEncoder",
                "spomky-labs/lexik-jose-bridge": "Provides a JWT Token encoder with encryption support"
            },
            "type": "symfony-bundle",
            "extra": {
                "branch-alias": {
                    "dev-master": "2.x-dev"
                }
            },
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
                    "name": "Robin Chalas",
                    "email": "robin.chalas@gmail.com",
                    "homepage": "https://github.com/chalasr"
                },
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
                    "name": "Lexik Community",
                    "homepage": "https://github.com/lexik/LexikJWTAuthenticationBundle/graphs/contributors"
                },
                {
                    "name": "Dev Lexik",
                    "email": "dev@lexik.fr",
                    "homepage": "https://github.com/lexik"
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
            "time": "2017-06-29T13:44:14+00:00"
        },
        {
            "name": "michelf/php-markdown",
            "version": "1.7.0",
            "source": {
                "type": "git",
                "url": "https://github.com/michelf/php-markdown.git",
                "reference": "1f51cc520948f66cd2af8cbc45a5ee175e774220"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/michelf/php-markdown/zipball/1f51cc520948f66cd2af8cbc45a5ee175e774220",
                "reference": "1f51cc520948f66cd2af8cbc45a5ee175e774220",
                "shasum": ""
            },
            "require": {
                "php": ">=5.3.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-lib": "1.4.x-dev"
                }
            },
            "autoload": {
                "psr-0": {
                    "Michelf": ""
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause"
            ],
            "authors": [
                {
                    "name": "Michel Fortin",
                    "email": "michel.fortin@michelf.ca",
                    "homepage": "https://michelf.ca/",
                    "role": "Developer"
                },
                {
                    "name": "John Gruber",
                    "homepage": "https://daringfireball.net/"
                }
            ],
            "description": "PHP Markdown",
            "homepage": "https://michelf.ca/projects/php-markdown/",
            "keywords": [
                "markdown"
            ],
            "time": "2016-10-29T18:58:20+00:00"
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
            "name": "namshi/jose",
            "version": "7.2.3",
            "source": {
                "type": "git",
                "url": "https://github.com/namshi/jose.git",
                "reference": "89a24d7eb3040e285dd5925fcad992378b82bcff"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/namshi/jose/zipball/89a24d7eb3040e285dd5925fcad992378b82bcff",
                "reference": "89a24d7eb3040e285dd5925fcad992378b82bcff",
                "shasum": ""
            },
            "require": {
                "ext-date": "*",
                "ext-hash": "*",
                "ext-json": "*",
                "ext-pcre": "*",
                "ext-spl": "*",
                "php": ">=5.5",
                "symfony/polyfill-php56": "^1.0"
            },
            "require-dev": {
                "phpseclib/phpseclib": "^2.0",
                "phpunit/phpunit": "^4.5|^5.0",
                "satooshi/php-coveralls": "^1.0"
            },
            "suggest": {
                "ext-openssl": "Allows to use OpenSSL as crypto engine.",
                "phpseclib/phpseclib": "Allows to use Phpseclib as crypto engine, use version ^2.0."
            },
            "type": "library",
            "autoload": {
                "psr-4": {
                    "Namshi\\JOSE\\": "src/Namshi/JOSE/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Alessandro Nadalin",
                    "email": "alessandro.nadalin@gmail.com"
                },
                {
                    "name": "Alessandro Cinelli (cirpo)",
                    "email": "alessandro.cinelli@gmail.com"
                }
            ],
            "description": "JSON Object Signing and Encryption library for PHP.",
            "keywords": [
                "JSON Web Signature",
                "JSON Web Token",
                "JWS",
                "json",
                "jwt",
                "token"
            ],
            "time": "2016-12-05T07:27:31+00:00"
        },
        {
            "name": "nelmio/api-doc-bundle",
            "version": "2.13.2",
            "target-dir": "Nelmio/ApiDocBundle",
            "source": {
                "type": "git",
                "url": "https://github.com/nelmio/NelmioApiDocBundle.git",
                "reference": "adcdd91950db72346be4a8af82cc05883b97cef3"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/nelmio/NelmioApiDocBundle/zipball/adcdd91950db72346be4a8af82cc05883b97cef3",
                "reference": "adcdd91950db72346be4a8af82cc05883b97cef3",
                "shasum": ""
            },
            "require": {
                "michelf/php-markdown": "~1.4",
                "php": ">=5.4",
                "symfony/console": "~2.3|~3.0",
                "symfony/framework-bundle": "~2.3|~3.0",
                "symfony/twig-bundle": "~2.3|~3.0"
            },
            "conflict": {
                "jms/serializer": "<0.12",
                "jms/serializer-bundle": "<0.11",
                "symfony/symfony": "~2.7.8",
                "twig/twig": "<1.12"
            },
            "require-dev": {
                "doctrine/doctrine-bundle": "~1.5",
                "doctrine/orm": "~2.3",
                "dunglas/api-bundle": "~1.0@dev",
                "friendsofsymfony/rest-bundle": "~1.0|~2.0",
                "jms/serializer-bundle": ">=0.11",
                "sensio/framework-extra-bundle": "~3.0",
                "symfony/browser-kit": "~2.3|~3.0",
                "symfony/css-selector": "~2.3|~3.0",
                "symfony/finder": "~2.3|~3.0",
                "symfony/form": "~2.3|~3.0",
                "symfony/phpunit-bridge": "~2.7|~3.0",
                "symfony/serializer": "~2.7|~3.0",
                "symfony/validator": "~2.3|~3.0",
                "symfony/yaml": "~2.3|~3.0"
            },
            "suggest": {
                "dunglas/api-bundle": "For making use of resources definitions of DunglasApiBundle.",
                "friendsofsymfony/rest-bundle": "For making use of REST information in the doc.",
                "jms/serializer": "For making use of serializer information in the doc.",
                "symfony/form": "For using form definitions as input.",
                "symfony/validator": "For making use of validator information in the doc."
            },
            "type": "symfony-bundle",
            "extra": {
                "branch-alias": {
                    "dev-master": "2.13-dev"
                }
            },
            "autoload": {
                "psr-0": {
                    "Nelmio\\ApiDocBundle": ""
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Nelmio",
                    "homepage": "http://nelm.io"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://github.com/nelmio/NelmioApiDocBundle/contributors"
                }
            ],
            "description": "Generates documentation for your REST API from annotations",
            "keywords": [
                "api",
                "doc",
                "documentation",
                "rest"
            ],
            "time": "2017-05-13T14:53:58+00:00"
        },
        {
            "name": "pagerfanta/pagerfanta",
            "version": "v1.0.5",
            "source": {
                "type": "git",
                "url": "https://github.com/whiteoctober/Pagerfanta.git",
                "reference": "29aade64addfdfb12c05aabf160f09d1aea6b143"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/whiteoctober/Pagerfanta/zipball/29aade64addfdfb12c05aabf160f09d1aea6b143",
                "reference": "29aade64addfdfb12c05aabf160f09d1aea6b143",
                "shasum": ""
            },
            "require": {
                "php": ">=5.3.0"
            },
            "require-dev": {
                "doctrine/orm": "~2.3",
                "doctrine/phpcr-odm": "1.*",
                "jackalope/jackalope-doctrine-dbal": "1.*",
                "jmikola/geojson": "~1.0",
                "mandango/mandango": "~1.0@dev",
                "mandango/mondator": "~1.0@dev",
                "phpunit/phpunit": "~4 | ~5",
                "propel/propel": "~2.0@dev",
                "propel/propel1": "~1.6",
                "ruflin/elastica": "~1.3",
                "solarium/solarium": "~3.1"
            },
            "suggest": {
                "doctrine/mongodb-odm": "To use the DoctrineODMMongoDBAdapter.",
                "doctrine/orm": "To use the DoctrineORMAdapter.",
                "doctrine/phpcr-odm": "To use the DoctrineODMPhpcrAdapter. >= 1.1.0",
                "mandango/mandango": "To use the MandangoAdapter.",
                "propel/propel": "To use the Propel2Adapter",
                "propel/propel1": "To use the PropelAdapter",
                "solarium/solarium": "To use the SolariumAdapter."
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.0.x-dev"
                }
            },
            "autoload": {
                "psr-0": {
                    "Pagerfanta\\": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Pablo Díez",
                    "email": "pablodip@gmail.com"
                }
            ],
            "description": "Pagination for PHP 5.3",
            "keywords": [
                "page",
                "pagination",
                "paginator",
                "paging"
            ],
            "time": "2017-03-20T13:46:15+00:00"
        },
        {
            "name": "paragonie/random_compat",
            "version": "v2.0.11",
            "source": {
                "type": "git",
                "url": "https://github.com/paragonie/random_compat.git",
                "reference": "5da4d3c796c275c55f057af5a643ae297d96b4d8"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/paragonie/random_compat/zipball/5da4d3c796c275c55f057af5a643ae297d96b4d8",
                "reference": "5da4d3c796c275c55f057af5a643ae297d96b4d8",
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
            "time": "2017-09-27T21:40:39+00:00"
        },
        {
            "name": "php-amqplib/php-amqplib",
            "version": "v2.7.0",
            "source": {
                "type": "git",
                "url": "https://github.com/php-amqplib/php-amqplib.git",
                "reference": "f48748546e398d846134c594dfca9070c4c3b356"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/php-amqplib/php-amqplib/zipball/f48748546e398d846134c594dfca9070c4c3b356",
                "reference": "f48748546e398d846134c594dfca9070c4c3b356",
                "shasum": ""
            },
            "require": {
                "ext-bcmath": "*",
                "ext-mbstring": "*",
                "php": ">=5.3.0"
            },
            "replace": {
                "videlalvaro/php-amqplib": "self.version"
            },
            "require-dev": {
                "phpunit/phpunit": "^4.8",
                "scrutinizer/ocular": "^1.1",
                "squizlabs/php_codesniffer": "^2.5"
            },
            "suggest": {
                "ext-sockets": "Use AMQPSocketConnection"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "2.7-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "PhpAmqpLib\\": "PhpAmqpLib/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "LGPL-2.1"
            ],
            "authors": [
                {
                    "name": "Alvaro Videla",
                    "role": "Original Maintainer"
                },
                {
                    "name": "John Kelly",
                    "email": "johnmkelly86@gmail.com",
                    "role": "Maintainer"
                },
                {
                    "name": "Raúl Araya",
                    "email": "nubeiro@gmail.com",
                    "role": "Maintainer"
                }
            ],
            "description": "Formerly videlalvaro/php-amqplib.  This library is a pure PHP implementation of the AMQP protocol. It's been tested against RabbitMQ.",
            "homepage": "https://github.com/php-amqplib/php-amqplib/",
            "keywords": [
                "message",
                "queue",
                "rabbitmq"
            ],
            "time": "2017-08-03T22:06:21+00:00"
        },
        {
            "name": "php-amqplib/rabbitmq-bundle",
            "version": "v1.13.0",
            "source": {
                "type": "git",
                "url": "https://github.com/php-amqplib/RabbitMqBundle.git",
                "reference": "564e87c7d4c47f545838de57a78f657a8304374b"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/php-amqplib/RabbitMqBundle/zipball/564e87c7d4c47f545838de57a78f657a8304374b",
                "reference": "564e87c7d4c47f545838de57a78f657a8304374b",
                "shasum": ""
            },
            "require": {
                "php": ">=5.3.0",
                "php-amqplib/php-amqplib": "~2.6",
                "psr/log": "~1.0",
                "symfony/config": "~2.3 || ~3.0",
                "symfony/console": "~2.3 || ~3.0",
                "symfony/dependency-injection": "~2.3 || ~3.0",
                "symfony/event-dispatcher": "~2.3 || ~3.0",
                "symfony/yaml": "~2.3 || ~3.0"
            },
            "replace": {
                "oldsound/rabbitmq-bundle": "self.version"
            },
            "require-dev": {
                "phpunit/phpunit": "~4.8 || ~5.0",
                "symfony/debug": "~2.3 || ~3.0",
                "symfony/serializer": "~2.3 || ~3.0"
            },
            "suggest": {
                "symfony/framework-bundle": "To use this lib as a full Symfony Bundle and to use the profiler data collector"
            },
            "type": "symfony-bundle",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.10.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "OldSound\\RabbitMqBundle\\": ""
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
                    "name": "Alvaro Videla"
                }
            ],
            "description": "Integrates php-amqplib with Symfony & RabbitMq. Formerly oldsound/rabbitmq-bundle.",
            "keywords": [
                "AMQP",
                "Symfony2",
                "message",
                "queue",
                "rabbitmq"
            ],
            "time": "2017-06-12T07:05:02+00:00"
        },
        {
            "name": "phpcollection/phpcollection",
            "version": "0.5.0",
            "source": {
                "type": "git",
                "url": "https://github.com/schmittjoh/php-collection.git",
                "reference": "f2bcff45c0da7c27991bbc1f90f47c4b7fb434a6"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/schmittjoh/php-collection/zipball/f2bcff45c0da7c27991bbc1f90f47c4b7fb434a6",
                "reference": "f2bcff45c0da7c27991bbc1f90f47c4b7fb434a6",
                "shasum": ""
            },
            "require": {
                "phpoption/phpoption": "1.*"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "0.4-dev"
                }
            },
            "autoload": {
                "psr-0": {
                    "PhpCollection": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "Apache2"
            ],
            "authors": [
                {
                    "name": "Johannes M. Schmitt",
                    "email": "schmittjoh@gmail.com"
                }
            ],
            "description": "General-Purpose Collection Library for PHP",
            "keywords": [
                "collection",
                "list",
                "map",
                "sequence",
                "set"
            ],
            "time": "2015-05-17T12:39:23+00:00"
        },
        {
            "name": "phpoption/phpoption",
            "version": "1.5.0",
            "source": {
                "type": "git",
                "url": "https://github.com/schmittjoh/php-option.git",
                "reference": "94e644f7d2051a5f0fcf77d81605f152eecff0ed"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/schmittjoh/php-option/zipball/94e644f7d2051a5f0fcf77d81605f152eecff0ed",
                "reference": "94e644f7d2051a5f0fcf77d81605f152eecff0ed",
                "shasum": ""
            },
            "require": {
                "php": ">=5.3.0"
            },
            "require-dev": {
                "phpunit/phpunit": "4.7.*"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.3-dev"
                }
            },
            "autoload": {
                "psr-0": {
                    "PhpOption\\": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "Apache2"
            ],
            "authors": [
                {
                    "name": "Johannes M. Schmitt",
                    "email": "schmittjoh@gmail.com"
                }
            ],
            "description": "Option Type for PHP",
            "keywords": [
                "language",
                "option",
                "php",
                "type"
            ],
            "time": "2015-07-25T16:39:46+00:00"
        },
        {
            "name": "predis/predis",
            "version": "v1.1.1",
            "source": {
                "type": "git",
                "url": "https://github.com/nrk/predis.git",
                "reference": "f0210e38881631afeafb56ab43405a92cafd9fd1"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/nrk/predis/zipball/f0210e38881631afeafb56ab43405a92cafd9fd1",
                "reference": "f0210e38881631afeafb56ab43405a92cafd9fd1",
                "shasum": ""
            },
            "require": {
                "php": ">=5.3.9"
            },
            "require-dev": {
                "phpunit/phpunit": "~4.8"
            },
            "suggest": {
                "ext-curl": "Allows access to Webdis when paired with phpiredis",
                "ext-phpiredis": "Allows faster serialization and deserialization of the Redis protocol"
            },
            "type": "library",
            "autoload": {
                "psr-4": {
                    "Predis\\": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Daniele Alessandri",
                    "email": "suppakilla@gmail.com",
                    "homepage": "http://clorophilla.net"
                }
            ],
            "description": "Flexible and feature-complete Redis client for PHP and HHVM",
            "homepage": "http://github.com/nrk/predis",
            "keywords": [
                "nosql",
                "predis",
                "redis"
            ],
            "time": "2016-06-16T16:22:20+00:00"
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
            "version": "3.7.1",
            "source": {
                "type": "git",
                "url": "https://github.com/ramsey/uuid.git",
                "reference": "45cffe822057a09e05f7bd09ec5fb88eeecd2334"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/ramsey/uuid/zipball/45cffe822057a09e05f7bd09ec5fb88eeecd2334",
                "reference": "45cffe822057a09e05f7bd09ec5fb88eeecd2334",
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
            "time": "2017-09-22T20:46:04+00:00"
        },
        {
            "name": "ramsey/uuid-doctrine",
            "version": "1.4.1",
            "source": {
                "type": "git",
                "url": "https://github.com/ramsey/uuid-doctrine.git",
                "reference": "d9002c7fe2cc5507e9292fe90d78d1e89b9d985e"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/ramsey/uuid-doctrine/zipball/d9002c7fe2cc5507e9292fe90d78d1e89b9d985e",
                "reference": "d9002c7fe2cc5507e9292fe90d78d1e89b9d985e",
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
            "time": "2017-07-18T16:21:14+00:00"
        },
        {
            "name": "ruflin/elastica",
            "version": "3.2.3",
            "source": {
                "type": "git",
                "url": "https://github.com/ruflin/Elastica.git",
                "reference": "02bf2fbb8ad6b679869af145eed89436a1c50229"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/ruflin/Elastica/zipball/02bf2fbb8ad6b679869af145eed89436a1c50229",
                "reference": "02bf2fbb8ad6b679869af145eed89436a1c50229",
                "shasum": ""
            },
            "require": {
                "php": ">=5.4.0",
                "psr/log": "~1.0"
            },
            "require-dev": {
                "aws/aws-sdk-php": "~3.0",
                "guzzlehttp/guzzle": "~6.0"
            },
            "suggest": {
                "aws/aws-sdk-php": "Allow using IAM authentication with Amazon ElasticSearch Service",
                "egeloen/http-adapter": "Allow using httpadapter transport",
                "guzzlehttp/guzzle": "Allow using guzzle 6 as the http transport (Requires php 5.5)",
                "monolog/monolog": "Logging request"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "3.2.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Elastica\\": "lib/Elastica/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Nicolas Ruflin",
                    "homepage": "http://ruflin.com/"
                }
            ],
            "description": "Elasticsearch Client",
            "homepage": "http://elastica.io/",
            "keywords": [
                "client",
                "search"
            ],
            "time": "2016-09-23T10:24:25+00:00"
        },
        {
            "name": "sensio/distribution-bundle",
            "version": "v5.0.21",
            "source": {
                "type": "git",
                "url": "https://github.com/sensiolabs/SensioDistributionBundle.git",
                "reference": "eb6266b3b472e4002538610b28a0a04bcf94891a"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sensiolabs/SensioDistributionBundle/zipball/eb6266b3b472e4002538610b28a0a04bcf94891a",
                "reference": "eb6266b3b472e4002538610b28a0a04bcf94891a",
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
            "time": "2017-08-25T16:55:44+00:00"
        },
        {
            "name": "sensio/framework-extra-bundle",
            "version": "v3.0.27",
            "source": {
                "type": "git",
                "url": "https://github.com/sensiolabs/SensioFrameworkExtraBundle.git",
                "reference": "2651d2c70c5fec10beaa670c61fd8ff1e8b3869a"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sensiolabs/SensioFrameworkExtraBundle/zipball/2651d2c70c5fec10beaa670c61fd8ff1e8b3869a",
                "reference": "2651d2c70c5fec10beaa670c61fd8ff1e8b3869a",
                "shasum": ""
            },
            "require": {
                "doctrine/common": "~2.2",
                "symfony/dependency-injection": "~2.3|~3.0|~4.0",
                "symfony/framework-bundle": "~2.3|~3.0|~4.0"
            },
            "require-dev": {
                "doctrine/doctrine-bundle": "~1.5",
                "doctrine/orm": "~2.4,>=2.4.5",
                "symfony/asset": "~2.7|~3.0|~4.0",
                "symfony/browser-kit": "~2.3|~3.0|~4.0",
                "symfony/dom-crawler": "~2.3|~3.0|~4.0",
                "symfony/expression-language": "~2.4|~3.0|~4.0",
                "symfony/finder": "~2.3|~3.0|~4.0",
                "symfony/phpunit-bridge": "~3.2|~4.0",
                "symfony/psr-http-message-bridge": "^0.3|^1.0",
                "symfony/security-bundle": "~2.4|~3.0|~4.0",
                "symfony/templating": "~2.3|~3.0|~4.0",
                "symfony/translation": "~2.3|~3.0|~4.0",
                "symfony/twig-bundle": "~2.3|~3.0|~4.0",
                "symfony/yaml": "~2.3|~3.0|~4.0",
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
            "time": "2017-08-23T12:40:59+00:00"
        },
        {
            "name": "sensiolabs/security-checker",
            "version": "v4.1.5",
            "source": {
                "type": "git",
                "url": "https://github.com/sensiolabs/security-checker.git",
                "reference": "55553c3ad6ae2121c1b1475d4c880d71b31b8f68"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sensiolabs/security-checker/zipball/55553c3ad6ae2121c1b1475d4c880d71b31b8f68",
                "reference": "55553c3ad6ae2121c1b1475d4c880d71b31b8f68",
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
                    "dev-master": "4.1-dev"
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
            "time": "2017-08-22T22:18:16+00:00"
        },
        {
            "name": "snc/redis-bundle",
            "version": "dev-master",
            "source": {
                "type": "git",
                "url": "https://github.com/snc/SncRedisBundle.git",
                "reference": "ba3903f5eb60159c3b6afdee31a23b594fedf212"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/snc/SncRedisBundle/zipball/ba3903f5eb60159c3b6afdee31a23b594fedf212",
                "reference": "ba3903f5eb60159c3b6afdee31a23b594fedf212",
                "shasum": ""
            },
            "require": {
                "php": ">=5.3.3",
                "symfony/framework-bundle": "^2.7 || ^3.0",
                "symfony/yaml": "^2.7 || ^3.0"
            },
            "require-dev": {
                "doctrine/cache": "1.*",
                "phpunit/phpunit": "4.8.*",
                "predis/predis": "^1.0",
                "symfony/console": "^2.7 || ^3.0",
                "symfony/phpunit-bridge": "^2.7 || ^3.0"
            },
            "suggest": {
                "monolog/monolog": "If you want to use the monolog redis handler.",
                "predis/predis": "If you want to use predis.",
                "symfony/console": "If you want to use commands to interact with the redis database"
            },
            "type": "symfony-bundle",
            "extra": {
                "branch-alias": {
                    "dev-master": "2.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Snc\\RedisBundle\\": ""
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Henrik Westphal",
                    "email": "henrik.westphal@gmail.com"
                },
                {
                    "name": "Community contributors",
                    "homepage": "https://github.com/snc/SncRedisBundle/contributors"
                }
            ],
            "description": "A Redis bundle for Symfony",
            "homepage": "https://github.com/snc/SncRedisBundle",
            "keywords": [
                "nosql",
                "redis",
                "symfony"
            ],
            "time": "2017-10-01 12:53:59"
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
            "version": "v2.12.1",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/monolog-bundle.git",
                "reference": "b0146bdca7ba2a65f3bbe7010423c7393b29ec3f"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/monolog-bundle/zipball/b0146bdca7ba2a65f3bbe7010423c7393b29ec3f",
                "reference": "b0146bdca7ba2a65f3bbe7010423c7393b29ec3f",
                "shasum": ""
            },
            "require": {
                "monolog/monolog": "~1.18",
                "php": ">=5.3.2",
                "symfony/config": "~2.3|~3.0",
                "symfony/dependency-injection": "~2.3|~3.0",
                "symfony/http-kernel": "~2.3|~3.0",
                "symfony/monolog-bridge": "~2.3|~3.0"
            },
            "require-dev": {
                "phpunit/phpunit": "^4.8",
                "symfony/console": "~2.3|~3.0",
                "symfony/yaml": "~2.3|~3.0"
            },
            "type": "symfony-bundle",
            "extra": {
                "branch-alias": {
                    "dev-master": "2.x-dev"
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
            "time": "2017-01-02T19:04:26+00:00"
        },
        {
            "name": "symfony/polyfill-apcu",
            "version": "v1.5.0",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/polyfill-apcu.git",
                "reference": "cec32398a973a9bfe9d2f94f4b5d5e186b40b698"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/polyfill-apcu/zipball/cec32398a973a9bfe9d2f94f4b5d5e186b40b698",
                "reference": "cec32398a973a9bfe9d2f94f4b5d5e186b40b698",
                "shasum": ""
            },
            "require": {
                "php": ">=5.3.3"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.5-dev"
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
            "time": "2017-07-05T15:09:33+00:00"
        },
        {
            "name": "symfony/polyfill-intl-icu",
            "version": "v1.5.0",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/polyfill-intl-icu.git",
                "reference": "4aa0b65dc71a7369c1e7e6e2a3ca027d9decdb09"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/polyfill-intl-icu/zipball/4aa0b65dc71a7369c1e7e6e2a3ca027d9decdb09",
                "reference": "4aa0b65dc71a7369c1e7e6e2a3ca027d9decdb09",
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
                    "dev-master": "1.5-dev"
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
            "time": "2017-06-14T15:44:48+00:00"
        },
        {
            "name": "symfony/polyfill-mbstring",
            "version": "v1.5.0",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/polyfill-mbstring.git",
                "reference": "7c8fae0ac1d216eb54349e6a8baa57d515fe8803"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/polyfill-mbstring/zipball/7c8fae0ac1d216eb54349e6a8baa57d515fe8803",
                "reference": "7c8fae0ac1d216eb54349e6a8baa57d515fe8803",
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
                    "dev-master": "1.5-dev"
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
            "time": "2017-06-14T15:44:48+00:00"
        },
        {
            "name": "symfony/polyfill-php56",
            "version": "v1.5.0",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/polyfill-php56.git",
                "reference": "e85ebdef569b84e8709864e1a290c40f156b30ca"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/polyfill-php56/zipball/e85ebdef569b84e8709864e1a290c40f156b30ca",
                "reference": "e85ebdef569b84e8709864e1a290c40f156b30ca",
                "shasum": ""
            },
            "require": {
                "php": ">=5.3.3",
                "symfony/polyfill-util": "~1.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.5-dev"
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
            "time": "2017-06-14T15:44:48+00:00"
        },
        {
            "name": "symfony/polyfill-php70",
            "version": "v1.5.0",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/polyfill-php70.git",
                "reference": "b6482e68974486984f59449ecea1fbbb22ff840f"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/polyfill-php70/zipball/b6482e68974486984f59449ecea1fbbb22ff840f",
                "reference": "b6482e68974486984f59449ecea1fbbb22ff840f",
                "shasum": ""
            },
            "require": {
                "paragonie/random_compat": "~1.0|~2.0",
                "php": ">=5.3.3"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.5-dev"
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
            "time": "2017-06-14T15:44:48+00:00"
        },
        {
            "name": "symfony/polyfill-util",
            "version": "v1.5.0",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/polyfill-util.git",
                "reference": "67925d1cf0b84bd234a83bebf26d4eb281744c6d"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/polyfill-util/zipball/67925d1cf0b84bd234a83bebf26d4eb281744c6d",
                "reference": "67925d1cf0b84bd234a83bebf26d4eb281744c6d",
                "shasum": ""
            },
            "require": {
                "php": ">=5.3.3"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.5-dev"
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
            "time": "2017-07-05T15:09:33+00:00"
        },
        {
            "name": "symfony/swiftmailer-bundle",
            "version": "v2.6.3",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/swiftmailer-bundle.git",
                "reference": "11555c338f3c367b0a1bd2f024a53aa813f4ce00"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/swiftmailer-bundle/zipball/11555c338f3c367b0a1bd2f024a53aa813f4ce00",
                "reference": "11555c338f3c367b0a1bd2f024a53aa813f4ce00",
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
            "time": "2017-07-22T07:18:13+00:00"
        },
        {
            "name": "symfony/symfony",
            "version": "v3.3.9",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/symfony.git",
                "reference": "a9d2f68ae9946000e2bcc3403d218ec0124f992a"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/symfony/zipball/a9d2f68ae9946000e2bcc3403d218ec0124f992a",
                "reference": "a9d2f68ae9946000e2bcc3403d218ec0124f992a",
                "shasum": ""
            },
            "require": {
                "doctrine/common": "~2.4",
                "ext-xml": "*",
                "fig/link-util": "^1.0",
                "php": "^5.5.9|>=7.0.8",
                "psr/cache": "~1.0",
                "psr/container": "^1.0",
                "psr/link": "^1.0",
                "psr/log": "~1.0",
                "psr/simple-cache": "^1.0",
                "symfony/polyfill-apcu": "~1.1",
                "symfony/polyfill-intl-icu": "~1.0",
                "symfony/polyfill-mbstring": "~1.0",
                "symfony/polyfill-php56": "~1.0",
                "symfony/polyfill-php70": "~1.0",
                "symfony/polyfill-util": "~1.0",
                "twig/twig": "~1.34|~2.4"
            },
            "conflict": {
                "phpdocumentor/reflection-docblock": "<3.0||>=3.2.0,<3.2.2",
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
                "phpdocumentor/reflection-docblock": "^3.0|^4.0",
                "predis/predis": "~1.0",
                "sensio/framework-extra-bundle": "^3.0.2",
                "symfony/phpunit-bridge": "~3.2",
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
            "time": "2017-09-11T16:13:42+00:00"
        },
        {
            "name": "twig/twig",
            "version": "v2.4.4",
            "source": {
                "type": "git",
                "url": "https://github.com/twigphp/Twig.git",
                "reference": "eddb97148ad779f27e670e1e3f19fb323aedafeb"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/twigphp/Twig/zipball/eddb97148ad779f27e670e1e3f19fb323aedafeb",
                "reference": "eddb97148ad779f27e670e1e3f19fb323aedafeb",
                "shasum": ""
            },
            "require": {
                "php": "^7.0",
                "symfony/polyfill-mbstring": "~1.0"
            },
            "require-dev": {
                "psr/container": "^1.0",
                "symfony/debug": "~2.7",
                "symfony/phpunit-bridge": "~3.3@dev"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "2.4-dev"
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
            "time": "2017-09-27T18:10:31+00:00"
        },
        {
            "name": "white-october/pagerfanta-bundle",
            "version": "v1.0.8",
            "source": {
                "type": "git",
                "url": "https://github.com/whiteoctober/WhiteOctoberPagerfantaBundle.git",
                "reference": "ba78522935b141e7e3dee637dc0095fb44fde65b"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/whiteoctober/WhiteOctoberPagerfantaBundle/zipball/ba78522935b141e7e3dee637dc0095fb44fde65b",
                "reference": "ba78522935b141e7e3dee637dc0095fb44fde65b",
                "shasum": ""
            },
            "require": {
                "pagerfanta/pagerfanta": "1.0.*",
                "symfony/framework-bundle": "~2.3|~3.0",
                "symfony/property-access": "~2.3|~3.0",
                "symfony/twig-bundle": "~2.3|~3.0"
            },
            "require-dev": {
                "phpunit/phpunit": "~3.7",
                "symfony/symfony": "~2.3|~3.0"
            },
            "type": "symfony-bundle",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.0.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "WhiteOctober\\PagerfantaBundle\\": ""
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Pablo Díez",
                    "email": "pablodip@gmail.com"
                }
            ],
            "description": "Bundle to use Pagerfanta with Symfony2",
            "keywords": [
                "page",
                "paging"
            ],
            "time": "2017-02-10T16:54:59+00:00"
        },
        {
            "name": "willdurand/hateoas",
            "version": "2.11.0",
            "source": {
                "type": "git",
                "url": "https://github.com/willdurand/Hateoas.git",
                "reference": "bc5c1035f7f040f13810fbed9ac87ba540af7758"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/willdurand/Hateoas/zipball/bc5c1035f7f040f13810fbed9ac87ba540af7758",
                "reference": "bc5c1035f7f040f13810fbed9ac87ba540af7758",
                "shasum": ""
            },
            "require": {
                "doctrine/annotations": "~1.0",
                "doctrine/common": "~2.0",
                "jms/metadata": "~1.1",
                "jms/serializer": "^1.7",
                "php": "^5.5|^7.0",
                "phpoption/phpoption": ">=1.1.0,<2.0-dev",
                "symfony/expression-language": "~2.4 || ~3.0"
            },
            "require-dev": {
                "pagerfanta/pagerfanta": "~1.0",
                "phpunit/phpunit": "~4.5",
                "symfony/dependency-injection": "~2.4 || ~3.0",
                "symfony/routing": "~2.4 || ~3.0",
                "symfony/yaml": "~2.4 || ~3.0",
                "twig/twig": "~1.12"
            },
            "suggest": {
                "symfony/routing": "To use the SymfonyRouteFactory.",
                "symfony/yaml": "To use yaml based configuration.",
                "twig/twig": "To use the Twig extensions."
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "2.11-dev"
                }
            },
            "autoload": {
                "psr-0": {
                    "Hateoas": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Adrien Brault",
                    "email": "adrien.brault@gmail.com"
                },
                {
                    "name": "William Durand",
                    "email": "william.durand1@gmail.com"
                }
            ],
            "description": "A PHP library to support implementing representations for HATEOAS REST web services",
            "time": "2017-05-22T10:27:33+00:00"
        },
        {
            "name": "willdurand/hateoas-bundle",
            "version": "1.3.0",
            "source": {
                "type": "git",
                "url": "https://github.com/willdurand/BazingaHateoasBundle.git",
                "reference": "bf57a3e45a26937726f370933eec4d8a7062733c"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/willdurand/BazingaHateoasBundle/zipball/bf57a3e45a26937726f370933eec4d8a7062733c",
                "reference": "bf57a3e45a26937726f370933eec4d8a7062733c",
                "shasum": ""
            },
            "require": {
                "jms/serializer-bundle": "~1.0 || ^2.0",
                "php": ">5.4",
                "symfony/framework-bundle": "~2.3 || ~3.0",
                "willdurand/hateoas": "^2.10.0"
            },
            "require-dev": {
                "phpunit/phpunit": "~4.5",
                "symfony/expression-language": "~2.4 || ~3.0",
                "twig/twig": "~1.12"
            },
            "type": "symfony-bundle",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.3-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Bazinga\\Bundle\\HateoasBundle\\": ""
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "William Durand",
                    "email": "william.durand1@gmail.com"
                }
            ],
            "description": "Integration of Hateoas into Symfony2.",
            "keywords": [
                "HATEOAS",
                "rest"
            ],
            "time": "2017-06-07T17:54:37+00:00"
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
        },
        {
            "name": "willdurand/negotiation",
            "version": "v2.3.1",
            "source": {
                "type": "git",
                "url": "https://github.com/willdurand/Negotiation.git",
                "reference": "03436ededa67c6e83b9b12defac15384cb399dc9"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/willdurand/Negotiation/zipball/03436ededa67c6e83b9b12defac15384cb399dc9",
                "reference": "03436ededa67c6e83b9b12defac15384cb399dc9",
                "shasum": ""
            },
            "require": {
                "php": ">=5.4.0"
            },
            "require-dev": {
                "phpunit/phpunit": "~4.5"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "2.3-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Negotiation\\": "src/Negotiation"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "William Durand",
                    "email": "will+git@drnd.me"
                }
            ],
            "description": "Content Negotiation tools for PHP provided as a standalone library.",
            "homepage": "http://williamdurand.fr/Negotiation/",
            "keywords": [
                "accept",
                "content",
                "format",
                "header",
                "negotiation"
            ],
            "time": "2017-05-14T17:21:12+00:00"
        }
    ],
    "packages-dev": [
        {
            "name": "behat/behat",
            "version": "v3.4.1",
            "source": {
                "type": "git",
                "url": "https://github.com/Behat/Behat.git",
                "reference": "cb51d4b0b11ea6d3897f3589a871a63a33632692"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/Behat/Behat/zipball/cb51d4b0b11ea6d3897f3589a871a63a33632692",
                "reference": "cb51d4b0b11ea6d3897f3589a871a63a33632692",
                "shasum": ""
            },
            "require": {
                "behat/gherkin": "^4.5.1",
                "behat/transliterator": "^1.2",
                "container-interop/container-interop": "^1.2",
                "ext-mbstring": "*",
                "php": ">=5.3.3",
                "psr/container": "^1.0",
                "symfony/class-loader": "~2.1||~3.0",
                "symfony/config": "~2.3||~3.0",
                "symfony/console": "~2.5||~3.0",
                "symfony/dependency-injection": "~2.1||~3.0",
                "symfony/event-dispatcher": "~2.1||~3.0",
                "symfony/translation": "~2.3||~3.0",
                "symfony/yaml": "~2.1||~3.0"
            },
            "require-dev": {
                "herrera-io/box": "~1.6.1",
                "phpunit/phpunit": "~4.5",
                "symfony/process": "~2.5|~3.0"
            },
            "suggest": {
                "behat/mink-extension": "for integration with Mink testing framework",
                "behat/symfony2-extension": "for integration with Symfony2 web framework",
                "behat/yii-extension": "for integration with Yii web framework"
            },
            "bin": [
                "bin/behat"
            ],
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "3.2.x-dev"
                }
            },
            "autoload": {
                "psr-0": {
                    "Behat\\Behat": "src/",
                    "Behat\\Testwork": "src/"
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
            "description": "Scenario-oriented BDD framework for PHP 5.3",
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
            "time": "2017-09-18T11:10:28+00:00"
        },
        {
            "name": "behat/gherkin",
            "version": "v4.5.1",
            "source": {
                "type": "git",
                "url": "https://github.com/Behat/Gherkin.git",
                "reference": "74ac03d52c5e23ad8abd5c5cce4ab0e8dc1b530a"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/Behat/Gherkin/zipball/74ac03d52c5e23ad8abd5c5cce4ab0e8dc1b530a",
                "reference": "74ac03d52c5e23ad8abd5c5cce4ab0e8dc1b530a",
                "shasum": ""
            },
            "require": {
                "php": ">=5.3.1"
            },
            "require-dev": {
                "phpunit/phpunit": "~4.5|~5",
                "symfony/phpunit-bridge": "~2.7|~3",
                "symfony/yaml": "~2.3|~3"
            },
            "suggest": {
                "symfony/yaml": "If you want to parse features, represented in YAML files"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "4.4-dev"
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
            "description": "Gherkin DSL parser for PHP 5.3",
            "homepage": "http://behat.org/",
            "keywords": [
                "BDD",
                "Behat",
                "Cucumber",
                "DSL",
                "gherkin",
                "parser"
            ],
            "time": "2017-08-30T11:04:43+00:00"
        },
        {
            "name": "behat/symfony2-extension",
            "version": "2.1.1",
            "source": {
                "type": "git",
                "url": "https://github.com/Behat/Symfony2Extension.git",
                "reference": "cb9ff0ff2f1a901379616d95cc701601d139160c"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/Behat/Symfony2Extension/zipball/cb9ff0ff2f1a901379616d95cc701601d139160c",
                "reference": "cb9ff0ff2f1a901379616d95cc701601d139160c",
                "shasum": ""
            },
            "require": {
                "behat/behat": "~3.0,>=3.0.4",
                "php": ">=5.3.3",
                "symfony/framework-bundle": "~2.0|~3.0"
            },
            "require-dev": {
                "behat/mink-browserkit-driver": "~1.0",
                "behat/mink-extension": "~2.0",
                "phpspec/phpspec": "~2.0",
                "phpunit/phpunit": "~4.0",
                "symfony/symfony": "~2.1|~3.0"
            },
            "type": "behat-extension",
            "extra": {
                "branch-alias": {
                    "dev-master": "2.1.x-dev"
                }
            },
            "autoload": {
                "psr-0": {
                    "Behat\\Symfony2Extension": "src/"
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
                },
                {
                    "name": "Konstantin Kudryashov",
                    "email": "ever.zet@gmail.com"
                }
            ],
            "description": "Symfony2 framework extension for Behat",
            "homepage": "http://behat.org",
            "keywords": [
                "BDD",
                "framework",
                "symfony"
            ],
            "time": "2016-01-13T17:06:48+00:00"
        },
        {
            "name": "behat/transliterator",
            "version": "v1.2.0",
            "source": {
                "type": "git",
                "url": "https://github.com/Behat/Transliterator.git",
                "reference": "826ce7e9c2a6664c0d1f381cbb38b1fb80a7ee2c"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/Behat/Transliterator/zipball/826ce7e9c2a6664c0d1f381cbb38b1fb80a7ee2c",
                "reference": "826ce7e9c2a6664c0d1f381cbb38b1fb80a7ee2c",
                "shasum": ""
            },
            "require": {
                "php": ">=5.3.3"
            },
            "require-dev": {
                "chuyskywalker/rolling-curl": "^3.1",
                "php-yaoi/php-yaoi": "^1.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.2-dev"
                }
            },
            "autoload": {
                "psr-0": {
                    "Behat\\Transliterator": "src/"
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
            "time": "2017-04-04T11:38:05+00:00"
        },
        {
            "name": "coduo/php-matcher",
            "version": "2.3.0",
            "source": {
                "type": "git",
                "url": "https://github.com/coduo/php-matcher.git",
                "reference": "79a27d13e0edc699ede6e64bcfee1e9bb5498793"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/coduo/php-matcher/zipball/79a27d13e0edc699ede6e64bcfee1e9bb5498793",
                "reference": "79a27d13e0edc699ede6e64bcfee1e9bb5498793",
                "shasum": ""
            },
            "require": {
                "coduo/php-to-string": "^2",
                "doctrine/lexer": "1.0.*",
                "ext-filter": "*",
                "openlss/lib-array2xml": "~0.0.9",
                "php": ">=5.3.0",
                "symfony/expression-language": "^2.3|^3.0",
                "symfony/property-access": "^2.3|^3.0"
            },
            "require-dev": {
                "phpunit/phpunit": "^4.8"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "2.4-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Coduo\\PHPMatcher\\": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Norbert Orzechowicz",
                    "email": "norbert@orzechowicz.pl"
                },
                {
                    "name": "Michał Dąbrowski",
                    "email": "dabrowski@brillante.pl"
                }
            ],
            "description": "PHP Matcher enables you to match values with patterns",
            "keywords": [
                "Match",
                "json",
                "matcher",
                "tests"
            ],
            "time": "2017-09-04T10:03:41+00:00"
        },
        {
            "name": "coduo/php-to-string",
            "version": "2.0.1",
            "source": {
                "type": "git",
                "url": "https://github.com/coduo/php-to-string.git",
                "reference": "4c1d7e2e76017719edc70e944ace0ec570748a78"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/coduo/php-to-string/zipball/4c1d7e2e76017719edc70e944ace0ec570748a78",
                "reference": "4c1d7e2e76017719edc70e944ace0ec570748a78",
                "shasum": ""
            },
            "require": {
                "php": ">=5.3.0"
            },
            "require-dev": {
                "coduo/phpspec-data-provider-extension": "^1",
                "phpspec/phpspec": "^2"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "2.1-dev"
                }
            },
            "autoload": {
                "psr-0": {
                    "": "src"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Norbert Orzechowicz",
                    "email": "norbert@orzechowicz.pl"
                },
                {
                    "name": "Michał Dąbrowski",
                    "email": "dabrowski@brillante.pl"
                }
            ],
            "keywords": [
                "php",
                "string",
                "to",
                "to string"
            ],
            "time": "2016-01-20T18:29:02+00:00"
        },
        {
            "name": "container-interop/container-interop",
            "version": "1.2.0",
            "source": {
                "type": "git",
                "url": "https://github.com/container-interop/container-interop.git",
                "reference": "79cbf1341c22ec75643d841642dd5d6acd83bdb8"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/container-interop/container-interop/zipball/79cbf1341c22ec75643d841642dd5d6acd83bdb8",
                "reference": "79cbf1341c22ec75643d841642dd5d6acd83bdb8",
                "shasum": ""
            },
            "require": {
                "psr/container": "^1.0"
            },
            "type": "library",
            "autoload": {
                "psr-4": {
                    "Interop\\Container\\": "src/Interop/Container/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "description": "Promoting the interoperability of container objects (DIC, SL, etc.)",
            "homepage": "https://github.com/container-interop/container-interop",
            "time": "2017-02-14T19:40:03+00:00"
        },
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
            "name": "fzaninotto/faker",
            "version": "v1.7.1",
            "source": {
                "type": "git",
                "url": "https://github.com/fzaninotto/Faker.git",
                "reference": "d3ed4cc37051c1ca52d22d76b437d14809fc7e0d"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/fzaninotto/Faker/zipball/d3ed4cc37051c1ca52d22d76b437d14809fc7e0d",
                "reference": "d3ed4cc37051c1ca52d22d76b437d14809fc7e0d",
                "shasum": ""
            },
            "require": {
                "php": "^5.3.3 || ^7.0"
            },
            "require-dev": {
                "ext-intl": "*",
                "phpunit/phpunit": "^4.0 || ^5.0",
                "squizlabs/php_codesniffer": "^1.5"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.8-dev"
                }
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
                    "name": "François Zaninotto"
                }
            ],
            "description": "Faker is a PHP library that generates fake data for you.",
            "keywords": [
                "data",
                "faker",
                "fixtures"
            ],
            "time": "2017-08-15T16:48:10+00:00"
        },
        {
            "name": "guzzlehttp/guzzle",
            "version": "6.3.0",
            "source": {
                "type": "git",
                "url": "https://github.com/guzzle/guzzle.git",
                "reference": "f4db5a78a5ea468d4831de7f0bf9d9415e348699"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/guzzle/guzzle/zipball/f4db5a78a5ea468d4831de7f0bf9d9415e348699",
                "reference": "f4db5a78a5ea468d4831de7f0bf9d9415e348699",
                "shasum": ""
            },
            "require": {
                "guzzlehttp/promises": "^1.0",
                "guzzlehttp/psr7": "^1.4",
                "php": ">=5.5"
            },
            "require-dev": {
                "ext-curl": "*",
                "phpunit/phpunit": "^4.0 || ^5.0",
                "psr/log": "^1.0"
            },
            "suggest": {
                "psr/log": "Required for using the Log middleware"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "6.2-dev"
                }
            },
            "autoload": {
                "files": [
                    "src/functions_include.php"
                ],
                "psr-4": {
                    "GuzzleHttp\\": "src/"
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
            "description": "Guzzle is a PHP HTTP client library",
            "homepage": "http://guzzlephp.org/",
            "keywords": [
                "client",
                "curl",
                "framework",
                "http",
                "http client",
                "rest",
                "web service"
            ],
            "time": "2017-06-22T18:50:49+00:00"
        },
        {
            "name": "guzzlehttp/promises",
            "version": "v1.3.1",
            "source": {
                "type": "git",
                "url": "https://github.com/guzzle/promises.git",
                "reference": "a59da6cf61d80060647ff4d3eb2c03a2bc694646"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/guzzle/promises/zipball/a59da6cf61d80060647ff4d3eb2c03a2bc694646",
                "reference": "a59da6cf61d80060647ff4d3eb2c03a2bc694646",
                "shasum": ""
            },
            "require": {
                "php": ">=5.5.0"
            },
            "require-dev": {
                "phpunit/phpunit": "^4.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.4-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "GuzzleHttp\\Promise\\": "src/"
                },
                "files": [
                    "src/functions_include.php"
                ]
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
            "description": "Guzzle promises library",
            "keywords": [
                "promise"
            ],
            "time": "2016-12-20T10:07:11+00:00"
        },
        {
            "name": "guzzlehttp/psr7",
            "version": "1.4.2",
            "source": {
                "type": "git",
                "url": "https://github.com/guzzle/psr7.git",
                "reference": "f5b8a8512e2b58b0071a7280e39f14f72e05d87c"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/guzzle/psr7/zipball/f5b8a8512e2b58b0071a7280e39f14f72e05d87c",
                "reference": "f5b8a8512e2b58b0071a7280e39f14f72e05d87c",
                "shasum": ""
            },
            "require": {
                "php": ">=5.4.0",
                "psr/http-message": "~1.0"
            },
            "provide": {
                "psr/http-message-implementation": "1.0"
            },
            "require-dev": {
                "phpunit/phpunit": "~4.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.4-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "GuzzleHttp\\Psr7\\": "src/"
                },
                "files": [
                    "src/functions_include.php"
                ]
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
                },
                {
                    "name": "Tobias Schultze",
                    "homepage": "https://github.com/Tobion"
                }
            ],
            "description": "PSR-7 message implementation that also provides common utility methods",
            "keywords": [
                "http",
                "message",
                "request",
                "response",
                "stream",
                "uri",
                "url"
            ],
            "time": "2017-03-20T17:10:46+00:00"
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
            "name": "lakion/api-test-case",
            "version": "v2.0.0",
            "source": {
                "type": "git",
                "url": "https://github.com/Lakion/ApiTestCase.git",
                "reference": "0a1e83fc693503e292ca525cd751ad3158b2e47c"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/Lakion/ApiTestCase/zipball/0a1e83fc693503e292ca525cd751ad3158b2e47c",
                "reference": "0a1e83fc693503e292ca525cd751ad3158b2e47c",
                "shasum": ""
            },
            "require": {
                "coduo/php-matcher": "^2.1",
                "doctrine/data-fixtures": "^1.2",
                "doctrine/doctrine-bundle": "^1.6",
                "doctrine/orm": "^2.5",
                "nelmio/alice": "^2.2",
                "php": "^7.0",
                "phpspec/php-diff": "^1.1",
                "phpunit/phpunit": "^6.0",
                "polishsymfonycommunity/symfony-mocker-container": "^1.0",
                "symfony/browser-kit": "^3.2",
                "symfony/finder": "^3.2",
                "symfony/framework-bundle": "^3.2"
            },
            "require-dev": {
                "symfony/serializer": "^3.2"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "2.0-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Lakion\\ApiTestCase\\": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Łukasz Chruściel",
                    "email": "lukasz.chrusciel@lakion.com"
                },
                {
                    "name": "Michał Marcinkowski",
                    "email": "michal.marcinkowski@lakion.com"
                },
                {
                    "name": "Paweł Jędrzejewski",
                    "email": "pawel.jedrzejewski@lakion.com",
                    "homepage": "http://pjedrzejewski.com"
                },
                {
                    "name": "Arkadiusz Krakowiak",
                    "email": "arkadiusz.krakowiak@lakion.com"
                }
            ],
            "description": "Perfect PHPUnit TestCase for JSON/XML API TDD with Symfony.",
            "keywords": [
                "TDD",
                "api",
                "doctrine",
                "json",
                "phpunit",
                "symfony",
                "xml"
            ],
            "time": "2017-06-27T07:50:08+00:00"
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
                    "name": "Pádraic Brady",
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
            "name": "nelmio/alice",
            "version": "v2.3.1",
            "source": {
                "type": "git",
                "url": "https://github.com/nelmio/alice.git",
                "reference": "0976436419f61863a072b390ea4c2ff75e62e364"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/nelmio/alice/zipball/0976436419f61863a072b390ea4c2ff75e62e364",
                "reference": "0976436419f61863a072b390ea4c2ff75e62e364",
                "shasum": ""
            },
            "require": {
                "fzaninotto/faker": "^1.5",
                "php": "^5.6||^7.0",
                "symfony/yaml": "^2.0||^3.0"
            },
            "require-dev": {
                "doctrine/common": "^2.3",
                "phpspec/prophecy": "^1.5.0",
                "phpunit/phpunit": "^5.6||^6.0",
                "symfony/phpunit-bridge": "^3.0",
                "symfony/property-access": "^2.2||^3.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "3.0.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Nelmio\\Alice\\": "src/Nelmio/Alice"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Jordi Boggiano",
                    "email": "j.boggiano@seld.be"
                },
                {
                    "name": "Tim Shelburne",
                    "email": "shelburt02@gmail.com"
                },
                {
                    "name": "Théo FIDRY",
                    "email": "theo.fidry@gmail.com"
                }
            ],
            "description": "Expressive fixtures generator",
            "keywords": [
                "Fixture",
                "data",
                "orm",
                "test"
            ],
            "time": "2017-03-24T16:33:53+00:00"
        },
        {
            "name": "openlss/lib-array2xml",
            "version": "0.0.10",
            "source": {
                "type": "git",
                "url": "https://github.com/openlss/lib-array2xml.git",
                "reference": "f6686668959a342ec326c5ad82ac557d767f34ef"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/openlss/lib-array2xml/zipball/f6686668959a342ec326c5ad82ac557d767f34ef",
                "reference": "f6686668959a342ec326c5ad82ac557d767f34ef",
                "shasum": ""
            },
            "require": {
                "php": ">=5.3.2"
            },
            "type": "library",
            "autoload": {
                "psr-0": {
                    "LSS": ""
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "Apache-2.0"
            ],
            "authors": [
                {
                    "name": "Bryan Tong",
                    "email": "contact@nullivex.com",
                    "homepage": "http://bryantong.com"
                },
                {
                    "name": "Tony Butler",
                    "email": "spudz76@gmail.com",
                    "homepage": "http://openlss.org"
                }
            ],
            "description": "Array2XML conversion library credit to lalit.org",
            "homepage": "http://openlss.org",
            "keywords": [
                "array",
                "array conversion",
                "xml",
                "xml conversion"
            ],
            "time": "2015-09-16T18:59:23+00:00"
        },
        {
            "name": "pdepend/pdepend",
            "version": "2.5.0",
            "source": {
                "type": "git",
                "url": "https://github.com/pdepend/pdepend.git",
                "reference": "0c50874333149c0dad5a2877801aed148f2767ff"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/pdepend/pdepend/zipball/0c50874333149c0dad5a2877801aed148f2767ff",
                "reference": "0c50874333149c0dad5a2877801aed148f2767ff",
                "shasum": ""
            },
            "require": {
                "php": ">=5.3.7",
                "symfony/config": "^2.3.0|^3",
                "symfony/dependency-injection": "^2.3.0|^3",
                "symfony/filesystem": "^2.3.0|^3"
            },
            "require-dev": {
                "phpunit/phpunit": "^4.4.0,<4.8",
                "squizlabs/php_codesniffer": "^2.0.0"
            },
            "bin": [
                "src/bin/pdepend"
            ],
            "type": "library",
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
            "time": "2017-01-19T14:23:36+00:00"
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
            "version": "1.0.1",
            "source": {
                "type": "git",
                "url": "https://github.com/phpDocumentor/ReflectionCommon.git",
                "reference": "21bdeb5f65d7ebf9f43b1b25d404f87deab5bfb6"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/phpDocumentor/ReflectionCommon/zipball/21bdeb5f65d7ebf9f43b1b25d404f87deab5bfb6",
                "reference": "21bdeb5f65d7ebf9f43b1b25d404f87deab5bfb6",
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
            "time": "2017-09-11T18:02:19+00:00"
        },
        {
            "name": "phpdocumentor/reflection-docblock",
            "version": "4.1.1",
            "source": {
                "type": "git",
                "url": "https://github.com/phpDocumentor/ReflectionDocBlock.git",
                "reference": "2d3d238c433cf69caeb4842e97a3223a116f94b2"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/phpDocumentor/ReflectionDocBlock/zipball/2d3d238c433cf69caeb4842e97a3223a116f94b2",
                "reference": "2d3d238c433cf69caeb4842e97a3223a116f94b2",
                "shasum": ""
            },
            "require": {
                "php": "^7.0",
                "phpdocumentor/reflection-common": "^1.0@dev",
                "phpdocumentor/type-resolver": "^0.4.0",
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
            "time": "2017-08-30T18:51:59+00:00"
        },
        {
            "name": "phpdocumentor/type-resolver",
            "version": "0.4.0",
            "source": {
                "type": "git",
                "url": "https://github.com/phpDocumentor/TypeResolver.git",
                "reference": "9c977708995954784726e25d0cd1dddf4e65b0f7"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/phpDocumentor/TypeResolver/zipball/9c977708995954784726e25d0cd1dddf4e65b0f7",
                "reference": "9c977708995954784726e25d0cd1dddf4e65b0f7",
                "shasum": ""
            },
            "require": {
                "php": "^5.5 || ^7.0",
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
            "time": "2017-07-14T14:27:02+00:00"
        },
        {
            "name": "phpmd/phpmd",
            "version": "2.6.0",
            "source": {
                "type": "git",
                "url": "https://github.com/phpmd/phpmd.git",
                "reference": "4e9924b2c157a3eb64395460fcf56b31badc8374"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/phpmd/phpmd/zipball/4e9924b2c157a3eb64395460fcf56b31badc8374",
                "reference": "4e9924b2c157a3eb64395460fcf56b31badc8374",
                "shasum": ""
            },
            "require": {
                "ext-xml": "*",
                "pdepend/pdepend": "^2.5",
                "php": ">=5.3.9"
            },
            "require-dev": {
                "phpunit/phpunit": "^4.0",
                "squizlabs/php_codesniffer": "^2.0"
            },
            "bin": [
                "src/bin/phpmd"
            ],
            "type": "project",
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
                    "name": "Other contributors",
                    "homepage": "https://github.com/phpmd/phpmd/graphs/contributors",
                    "role": "Contributors"
                },
                {
                    "name": "Marc Würth",
                    "email": "ravage@bluewin.ch",
                    "homepage": "https://github.com/ravage84",
                    "role": "Project Maintainer"
                }
            ],
            "description": "PHPMD is a spin-off project of PHP Depend and aims to be a PHP equivalent of the well known Java tool PMD.",
            "homepage": "http://phpmd.org/",
            "keywords": [
                "mess detection",
                "mess detector",
                "pdepend",
                "phpmd",
                "pmd"
            ],
            "time": "2017-01-20T14:41:10+00:00"
        },
        {
            "name": "phpspec/php-diff",
            "version": "v1.1.0",
            "source": {
                "type": "git",
                "url": "https://github.com/phpspec/php-diff.git",
                "reference": "0464787bfa7cd13576c5a1e318709768798bec6a"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/phpspec/php-diff/zipball/0464787bfa7cd13576c5a1e318709768798bec6a",
                "reference": "0464787bfa7cd13576c5a1e318709768798bec6a",
                "shasum": ""
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.0.x-dev"
                }
            },
            "autoload": {
                "psr-0": {
                    "Diff": "lib/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause"
            ],
            "authors": [
                {
                    "name": "Chris Boulton",
                    "homepage": "http://github.com/chrisboulton"
                }
            ],
            "description": "A comprehensive library for generating differences between two hashable objects (strings or arrays).",
            "time": "2016-04-07T12:29:16+00:00"
        },
        {
            "name": "phpspec/prophecy",
            "version": "v1.7.2",
            "source": {
                "type": "git",
                "url": "https://github.com/phpspec/prophecy.git",
                "reference": "c9b8c6088acd19d769d4cc0ffa60a9fe34344bd6"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/phpspec/prophecy/zipball/c9b8c6088acd19d769d4cc0ffa60a9fe34344bd6",
                "reference": "c9b8c6088acd19d769d4cc0ffa60a9fe34344bd6",
                "shasum": ""
            },
            "require": {
                "doctrine/instantiator": "^1.0.2",
                "php": "^5.3|^7.0",
                "phpdocumentor/reflection-docblock": "^2.0|^3.0.2|^4.0",
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
                    "dev-master": "1.7.x-dev"
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
            "time": "2017-09-04T11:05:03+00:00"
        },
        {
            "name": "phpunit/php-code-coverage",
            "version": "5.2.2",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/php-code-coverage.git",
                "reference": "8ed1902a57849e117b5651fc1a5c48110946c06b"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/php-code-coverage/zipball/8ed1902a57849e117b5651fc1a5c48110946c06b",
                "reference": "8ed1902a57849e117b5651fc1a5c48110946c06b",
                "shasum": ""
            },
            "require": {
                "ext-dom": "*",
                "ext-xmlwriter": "*",
                "php": "^7.0",
                "phpunit/php-file-iterator": "^1.4.2",
                "phpunit/php-text-template": "^1.2.1",
                "phpunit/php-token-stream": "^1.4.11 || ^2.0",
                "sebastian/code-unit-reverse-lookup": "^1.0.1",
                "sebastian/environment": "^3.0",
                "sebastian/version": "^2.0.1",
                "theseer/tokenizer": "^1.1"
            },
            "require-dev": {
                "ext-xdebug": "^2.5",
                "phpunit/phpunit": "^6.0"
            },
            "suggest": {
                "ext-xdebug": "^2.5.5"
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
            "time": "2017-08-03T12:40:43+00:00"
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
            "version": "2.0.1",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/php-token-stream.git",
                "reference": "9a02332089ac48e704c70f6cefed30c224e3c0b0"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/php-token-stream/zipball/9a02332089ac48e704c70f6cefed30c224e3c0b0",
                "reference": "9a02332089ac48e704c70f6cefed30c224e3c0b0",
                "shasum": ""
            },
            "require": {
                "ext-tokenizer": "*",
                "php": "^7.0"
            },
            "require-dev": {
                "phpunit/phpunit": "^6.2.4"
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
            "description": "Wrapper around PHP's tokenizer extension.",
            "homepage": "https://github.com/sebastianbergmann/php-token-stream/",
            "keywords": [
                "tokenizer"
            ],
            "time": "2017-08-20T05:47:52+00:00"
        },
        {
            "name": "phpunit/phpunit",
            "version": "6.3.1",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/phpunit.git",
                "reference": "c0ff817b36a827e64bf5f57bc72278150cf30a77"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/phpunit/zipball/c0ff817b36a827e64bf5f57bc72278150cf30a77",
                "reference": "c0ff817b36a827e64bf5f57bc72278150cf30a77",
                "shasum": ""
            },
            "require": {
                "ext-dom": "*",
                "ext-json": "*",
                "ext-libxml": "*",
                "ext-mbstring": "*",
                "ext-xml": "*",
                "myclabs/deep-copy": "^1.6.1",
                "phar-io/manifest": "^1.0.1",
                "phar-io/version": "^1.0",
                "php": "^7.0",
                "phpspec/prophecy": "^1.7",
                "phpunit/php-code-coverage": "^5.2.2",
                "phpunit/php-file-iterator": "^1.4.2",
                "phpunit/php-text-template": "^1.2.1",
                "phpunit/php-timer": "^1.0.9",
                "phpunit/phpunit-mock-objects": "^4.0.3",
                "sebastian/comparator": "^2.0.2",
                "sebastian/diff": "^2.0",
                "sebastian/environment": "^3.1",
                "sebastian/exporter": "^3.1",
                "sebastian/global-state": "^2.0",
                "sebastian/object-enumerator": "^3.0.3",
                "sebastian/resource-operations": "^1.0",
                "sebastian/version": "^2.0.1"
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
                    "dev-master": "6.3.x-dev"
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
            "time": "2017-09-24T07:25:54+00:00"
        },
        {
            "name": "phpunit/phpunit-mock-objects",
            "version": "4.0.4",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/phpunit-mock-objects.git",
                "reference": "2f789b59ab89669015ad984afa350c4ec577ade0"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/phpunit-mock-objects/zipball/2f789b59ab89669015ad984afa350c4ec577ade0",
                "reference": "2f789b59ab89669015ad984afa350c4ec577ade0",
                "shasum": ""
            },
            "require": {
                "doctrine/instantiator": "^1.0.5",
                "php": "^7.0",
                "phpunit/php-text-template": "^1.2.1",
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
            "time": "2017-08-03T14:08:16+00:00"
        },
        {
            "name": "polishsymfonycommunity/symfony-mocker-container",
            "version": "v1.0.2",
            "source": {
                "type": "git",
                "url": "https://github.com/PolishSymfonyCommunity/SymfonyMockerContainer.git",
                "reference": "111537c17f32f1bda5ed0253e723b57915c08ff4"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/PolishSymfonyCommunity/SymfonyMockerContainer/zipball/111537c17f32f1bda5ed0253e723b57915c08ff4",
                "reference": "111537c17f32f1bda5ed0253e723b57915c08ff4",
                "shasum": ""
            },
            "require": {
                "mockery/mockery": ">=0.7.0",
                "php": ">=5.3.2",
                "symfony/dependency-injection": ">=2.0.0"
            },
            "type": "library",
            "autoload": {
                "psr-0": {
                    "PSS\\SymfonyMockerContainer": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Polish Symfony Community",
                    "homepage": "http://symfonylab.pl"
                },
                {
                    "name": "Jakub Zalas",
                    "email": "jakub@zalas.pl",
                    "homepage": "http://www.zalas.eu"
                }
            ],
            "description": "Provides base Symfony dependency injection container enabling service mocking.",
            "homepage": "http://symfonylab.pl",
            "keywords": [
                "BDD",
                "Behat",
                "TDD",
                "mock",
                "mockery",
                "test"
            ],
            "time": "2016-03-04T08:53:43+00:00"
        },
        {
            "name": "psr/http-message",
            "version": "1.0.1",
            "source": {
                "type": "git",
                "url": "https://github.com/php-fig/http-message.git",
                "reference": "f6561bf28d520154e4b0ec72be95418abe6d9363"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/php-fig/http-message/zipball/f6561bf28d520154e4b0ec72be95418abe6d9363",
                "reference": "f6561bf28d520154e4b0ec72be95418abe6d9363",
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
                    "Psr\\Http\\Message\\": "src/"
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
            "description": "Common interface for HTTP messages",
            "homepage": "https://github.com/php-fig/http-message",
            "keywords": [
                "http",
                "http-message",
                "psr",
                "psr-7",
                "request",
                "response"
            ],
            "time": "2016-08-06T14:39:51+00:00"
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
            "version": "2.0.2",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/comparator.git",
                "reference": "ae068fede81d06e7bb9bb46a367210a3d3e1fe6a"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/comparator/zipball/ae068fede81d06e7bb9bb46a367210a3d3e1fe6a",
                "reference": "ae068fede81d06e7bb9bb46a367210a3d3e1fe6a",
                "shasum": ""
            },
            "require": {
                "php": "^7.0",
                "sebastian/diff": "^2.0",
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
            "time": "2017-08-03T07:14:59+00:00"
        },
        {
            "name": "sebastian/diff",
            "version": "2.0.1",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/diff.git",
                "reference": "347c1d8b49c5c3ee30c7040ea6fc446790e6bddd"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/diff/zipball/347c1d8b49c5c3ee30c7040ea6fc446790e6bddd",
                "reference": "347c1d8b49c5c3ee30c7040ea6fc446790e6bddd",
                "shasum": ""
            },
            "require": {
                "php": "^7.0"
            },
            "require-dev": {
                "phpunit/phpunit": "^6.2"
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
            "time": "2017-08-03T08:09:46+00:00"
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
            "version": "3.0.3",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/object-enumerator.git",
                "reference": "7cfd9e65d11ffb5af41198476395774d4c8a84c5"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/object-enumerator/zipball/7cfd9e65d11ffb5af41198476395774d4c8a84c5",
                "reference": "7cfd9e65d11ffb5af41198476395774d4c8a84c5",
                "shasum": ""
            },
            "require": {
                "php": "^7.0",
                "sebastian/object-reflector": "^1.1.1",
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
            "time": "2017-08-03T12:35:26+00:00"
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
            "version": "v3.1.6",
            "source": {
                "type": "git",
                "url": "https://github.com/sensiolabs/SensioGeneratorBundle.git",
                "reference": "128bc5dabc91ca40b7445f094968dd70ccd58305"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sensiolabs/SensioGeneratorBundle/zipball/128bc5dabc91ca40b7445f094968dd70ccd58305",
                "reference": "128bc5dabc91ca40b7445f094968dd70ccd58305",
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
            "time": "2017-07-18T07:57:44+00:00"
        },
        {
            "name": "symfony/phpunit-bridge",
            "version": "v3.3.9",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/phpunit-bridge.git",
                "reference": "27d159bd9bd14a3bd9d3e136081c321a0d621c03"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/phpunit-bridge/zipball/27d159bd9bd14a3bd9d3e136081c321a0d621c03",
                "reference": "27d159bd9bd14a3bd9d3e136081c321a0d621c03",
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
            "time": "2017-09-05T11:23:06+00:00"
        },
        {
            "name": "symfony/psr-http-message-bridge",
            "version": "v0.2",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/psr-http-message-bridge.git",
                "reference": "dc7e308e1dc2898a46776e2221a643cb08315453"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/psr-http-message-bridge/zipball/dc7e308e1dc2898a46776e2221a643cb08315453",
                "reference": "dc7e308e1dc2898a46776e2221a643cb08315453",
                "shasum": ""
            },
            "require": {
                "php": ">=5.3.3",
                "psr/http-message": "~1.0",
                "symfony/http-foundation": "~2.3|~3.0"
            },
            "require-dev": {
                "symfony/phpunit-bridge": "~2.7|~3.0"
            },
            "suggest": {
                "zendframework/zend-diactoros": "To use the Zend Diactoros factory"
            },
            "type": "symfony-bridge",
            "autoload": {
                "psr-4": {
                    "Symfony\\Bridge\\PsrHttpMessage\\": ""
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
            "description": "PSR HTTP message bridge",
            "homepage": "http://symfony.com",
            "keywords": [
                "http",
                "http-message",
                "psr-7"
            ],
            "time": "2015-05-29T17:57:12+00:00"
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
        }
    ],
    "aliases": [],
    "minimum-stability": "stable",
    "stability-flags": {
        "snc/redis-bundle": 20
    },
    "prefer-stable": false,
    "prefer-lowest": false,
    "platform": {
        "php": ">=7.0.1"
    },
    "platform-dev": [],
    "platform-overrides": {
        "php": "7.0.9"
    }
}
```

## File: `depfile.yml`
```yaml
paths:
  - ./src
exclude_files:
layers:
  - name: Domain
    collectors:
      - type: className
        regex: Leos\\Domain\\.*
  - name: Application
    collectors:
      - type: className
        regex: Leos\\Application\\.*
  - name: Infrastructure
    collectors:
      - type: className
        regex: Leos\\Infrastructure\\.*
ruleset:
  Domain:
  Application:
    - Domain
  Infrastructure:
    - Domain
    - Application
```

## File: `phpunit.xml.dist`
```
<?xml version="1.0" encoding="UTF-8"?>

<!-- https://phpunit.de/manual/current/en/appendixes.configuration.html -->
<phpunit xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:noNamespaceSchemaLocation="http://schema.phpunit.de/4.8/phpunit.xsd"
         backupGlobals="false"
         colors="false"
         bootstrap="app/autoload.php"
         convertNoticesToExceptions="false"
>
    <php>
        <ini name="error_reporting" value="-1" />
        <env name="SYMFONY_DEPRECATIONS_HELPER" value="weak" />
        <server name="KERNEL_DIR" value="app/" />
        <server name="KERNEL_CLASS" value="AppKernel" />
        <server name="FIXTURES_DIR" value="../tests/UI/Fixtures" />
        <server name="EXPECTED_RESPONSE_DIR" value="../tests/UI/Responses" />
        <server name="IS_DOCTRINE_ORM_SUPPORTED" value="true" />
    </php>

    <testsuites>
        <testsuite name="Leos Test Suite">
            <directory>tests</directory>
        </testsuite>
    </testsuites>
    <logging>
        <log type="coverage-html" target="report/report" lowUpperBound="35" highLowerBound="70"/>
    </logging>
    <filter>
        <whitelist>
            <directory>src</directory>
            <exclude>
                <directory>src/*Bundle/Resources</directory>
                <directory>src/*Bundle/DependencyInjection</directory>
                <directory>src/*/*Bundle/Resources</directory>
                <directory>src/*/*Bundle/DependencyInjection</directory>
                <directory>src/*/Bundle/*Bundle/Resources</directory>
                <directory>src/*/Bundle/*Bundle/DependencyInjection</directory>
                <directory>src/*/*/*Bundle/DependencyInjection</directory>
            </exclude>
        </whitelist>
    </filter>
</phpunit>
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
use PSS\SymfonyMockerContainer\DependencyInjection\MockerContainer;

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

            new JMS\SerializerBundle\JMSSerializerBundle(),
            new Nelmio\ApiDocBundle\NelmioApiDocBundle(),
            new FOS\RestBundle\FOSRestBundle(),
            new Bazinga\Bundle\HateoasBundle\BazingaHateoasBundle(),
            new WhiteOctober\PagerfantaBundle\WhiteOctoberPagerfantaBundle(),

            new Snc\RedisBundle\SncRedisBundle(),
            new Lexik\Bundle\JWTAuthenticationBundle\LexikJWTAuthenticationBundle(),

            new League\Tactician\Bundle\TacticianBundle(),

            new Leos\UI\RestBundle\LeosUIRestBundle(),
            new Leos\Infrastructure\CommonBundle\LeosInfrastructureCommonBundle(),
            new Leos\Infrastructure\WalletBundle\LeosInfrastructureWalletBundle(),
            new Leos\Infrastructure\TransactionBundle\LeosInfrastructureTransactionBundle(),
            new Leos\Infrastructure\MoneyBundle\LeosInfrastructureMoneyBundle(),
            new Leos\Infrastructure\SecurityBundle\LeosInfrastructureSecurityBundle(),
            new Leos\Infrastructure\UserBundle\LeosInfrastructureUserBundle(),
            new Leos\Infrastructure\PaymentBundle\LeosInfrastructurePaymentBundle(),
            new OldSound\RabbitMqBundle\OldSoundRabbitMqBundle(),
            new FOS\ElasticaBundle\FOSElasticaBundle(),
        ];

        if (in_array($this->getEnvironment(), ['dev', 'test'], true)) {
            $bundles[] = new Symfony\Bundle\DebugBundle\DebugBundle();
            $bundles[] = new Symfony\Bundle\WebProfilerBundle\WebProfilerBundle();
            $bundles[] = new Sensio\Bundle\DistributionBundle\SensioDistributionBundle();
            $bundles[] = new Sensio\Bundle\GeneratorBundle\SensioGeneratorBundle();
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

    protected function getContainerBaseClass()
    {
        if ('test' === $this->environment) {
            return MockerContainer::class;
        }

        return parent::getContainerBaseClass();
    }

}
```

## File: `app/autoload.php`
```php
<?php

use Doctrine\Common\Annotations\AnnotationRegistry;
use Composer\Autoload\ClassLoader;

/**
 * @var ClassLoader $loader
 */
$loader = require __DIR__.'/../vendor/autoload.php';

AnnotationRegistry::registerLoader([$loader, 'loadClass']);

return $loader;
```

## File: `app/Resources/views/base.html.twig`
```
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8" />
        <title>{% block title %}Welcome!{% endblock %}</title>
        {% block stylesheets %}{% endblock %}
        <link rel="icon" type="image/x-icon" href="{{ asset('favicon.ico') }}" />
    </head>
    <body>
        {% block body %}{% endblock %}
        {% block javascripts %}{% endblock %}
    </body>
</html>
```

## File: `app/Resources/views/default/index.html.twig`
```
{% extends 'base.html.twig' %}

{% block body %}
    <div id="wrapper">
        <div id="container">
            <div id="welcome">
                <h1><span>Welcome to</span> Symfony {{ constant('Symfony\\Component\\HttpKernel\\Kernel::VERSION') }}</h1>
            </div>

            <div id="status">
                <p>
                    <svg id="icon-status" width="1792" height="1792" viewBox="0 0 1792 1792" xmlns="http://www.w3.org/2000/svg"><path d="M1671 566q0 40-28 68l-724 724-136 136q-28 28-68 28t-68-28l-136-136-362-362q-28-28-28-68t28-68l136-136q28-28 68-28t68 28l294 295 656-657q28-28 68-28t68 28l136 136q28 28 28 68z" fill="#759E1A"/></svg>

                    Your application is now ready. You can start working on it at:
                    <code>{{ base_dir }}/</code>
                </p>
            </div>

            <div id="next">
                <h2>What's next?</h2>
                <p>
                    <svg id="icon-book" version="1.1" xmlns="http://www.w3.org/2000/svg" x="0px" y="0px" viewBox="-12.5 9 64 64" enable-background="new -12.5 9 64 64" xml:space="preserve">
                        <path fill="#AAA" d="M6.8,40.8c2.4,0.8,4.5-0.7,4.9-2.5c0.2-1.2-0.3-2.1-1.3-3.2l-0.8-0.8c-0.4-0.5-0.6-1.3-0.2-1.9
                            c0.4-0.5,0.9-0.8,1.8-0.5c1.3,0.4,1.9,1.3,2.9,2.2c-0.4,1.4-0.7,2.9-0.9,4.2l-0.2,1c-0.7,4-1.3,6.2-2.7,7.5
                            c-0.3,0.3-0.7,0.5-1.3,0.6c-0.3,0-0.4-0.3-0.4-0.3c0-0.3,0.2-0.3,0.3-0.4c0.2-0.1,0.5-0.3,0.4-0.8c0-0.7-0.6-1.3-1.3-1.3
                            c-0.6,0-1.4,0.6-1.4,1.7s1,1.9,2.4,1.8c0.8,0,2.5-0.3,4.2-2.5c2-2.5,2.5-5.4,2.9-7.4l0.5-2.8c0.3,0,0.5,0.1,0.8,0.1
                            c2.4,0.1,3.7-1.3,3.7-2.3c0-0.6-0.3-1.2-0.9-1.2c-0.4,0-0.8,0.3-1,0.8c-0.1,0.6,0.8,1.1,0.1,1.5c-0.5,0.3-1.4,0.6-2.7,0.4l0.3-1.3
                            c0.5-2.6,1-5.7,3.2-5.8c0.2,0,0.8,0,0.8,0.4c0,0.2,0,0.2-0.2,0.5c-0.2,0.3-0.3,0.4-0.2,0.7c0,0.7,0.5,1.1,1.2,1.1
                            c0.9,0,1.2-1,1.2-1.4c0-1.2-1.2-1.8-2.6-1.8c-1.5,0.1-2.8,0.9-3.7,2.1c-1.1,1.3-1.8,2.9-2.3,4.5c-0.9-0.8-1.6-1.8-3.1-2.3
                            c-1.1-0.7-2.3-0.5-3.4,0.3c-0.5,0.4-0.8,1-1,1.6c-0.4,1.5,0.4,2.9,0.8,3.4l0.9,1c0.2,0.2,0.6,0.8,0.4,1.5c-0.3,0.8-1.2,1.3-2.1,1
                            c-0.4-0.2-1-0.5-0.9-0.9c0.1-0.2,0.2-0.3,0.3-0.5s0.1-0.3,0.1-0.3c0.2-0.6-0.1-1.4-0.7-1.6c-0.6-0.2-1.2,0-1.3,0.8
                            C4.3,38.4,4.7,40,6.8,40.8z M46.1,20.9c0-4.2-3.2-7.5-7.1-7.5h-3.8C34.8,10.8,32.7,9,30.2,9L-2.3,9.1c-2.8,0.1-4.9,2.4-4.9,5.4
                            L-7,58.6c0,4.8,8.1,13.9,11.6,14.1l34.7-0.1c3.9,0,7-3.4,7-7.6L46.1,20.9z M-0.3,36.4c0-8.6,6.5-15.6,14.5-15.6
                            c8,0,14.5,7,14.5,15.6S22.1,52,14.2,52C6.1,52-0.3,45-0.3,36.4z M42.1,65.1c0,1.8-1.5,3.1-3.1,3.1H4.6c-0.7,0-3-1.8-4.5-4.4h30.4
                            c2.8,0,5-2.4,5-5.4V17.9h3.7c1.6,0,2.9,1.4,2.9,3.1V65.1L42.1,65.1z"/>
                    </svg>

                    Read the documentation to learn
                    <a href="http://symfony.com/doc/{{ constant('Symfony\\Component\\HttpKernel\\Kernel::VERSION')[:3] }}/book/page_creation.html">
                        How to create your first page in Symfony
                    </a>
                </p>
            </div>

        </div>
    </div>
{% endblock %}

{% block stylesheets %}
<style>
    body { background: #F5F5F5; font: 18px/1.5 sans-serif; }
    h1, h2 { line-height: 1.2; margin: 0 0 .5em; }
    h1 { font-size: 36px; }
    h2 { font-size: 21px; margin-bottom: 1em; }
    p { margin: 0 0 1em 0; }
    a { color: #0000F0; }
    a:hover { text-decoration: none; }
    code { background: #F5F5F5; max-width: 100px; padding: 2px 6px; word-wrap: break-word; }
    #wrapper { background: #FFF; margin: 1em auto; max-width: 800px; width: 95%; }
    #container { padding: 2em; }
    #welcome, #status { margin-bottom: 2em; }
    #welcome h1 span { display: block; font-size: 75%; }
    #icon-status, #icon-book { float: left; height: 64px; margin-right: 1em; margin-top: -4px; width: 64px; }
    #icon-book { display: none; }

    @media (min-width: 768px) {
        #wrapper { width: 80%; margin: 2em auto; }
        #icon-book { display: inline-block; }
        #status a, #next a { display: block; }

        @-webkit-keyframes fade-in { 0% { opacity: 0; } 100% { opacity: 1; } }
        @keyframes fade-in { 0% { opacity: 0; } 100% { opacity: 1; } }
        .sf-toolbar { opacity: 0; -webkit-animation: fade-in 1s .2s forwards; animation: fade-in 1s .2s forwards;}
    }
</style>
{% endblock %}
```

## File: `app/config/config.yml`
```yaml
imports:
    - { resource: parameters.yml }
    - { resource: security.yml }
    - { resource: services.yml }
    - { resource: bundles/serializer.yml }
    - { resource: bundles/rest.yml }
    - { resource: bundles/doc.yml }
    - { resource: bundles/doctrine.yml }
    - { resource: bundles/redis.yml }
    - { resource: bundles/jwt.yml }
    - { resource: bundles/bus.yml }
    - { resource: bundles/rmq.yml }
    - { resource: bundles/elastic.yml }

# Put parameters here that don't need to change on each machine where the app is deployed
# http://symfony.com/doc/current/best_practices/configuration.html#application-related-configuration
parameters:
    locale: en

framework:
    #esi:             ~
    #translator:      { fallbacks: ["%locale%"] }
    secret:          "%secret%"
    router:
        resource: "%kernel.root_dir%/config/routing.yml"
        strict_requirements: ~
    form:            ~
    csrf_protection: ~
    validation:      { enable_annotations: true }
    templating:
        engines: ['twig']
    default_locale:  "%locale%"
    trusted_hosts:   ~
    session:
        handler_id:  snc_redis.session.handler
    fragments:       ~
    http_method_override: true
    assets: ~

# Twig Configuration
twig:
    debug:            "%kernel.debug%"
    strict_variables: "%kernel.debug%"

# Swiftmailer Configuration
swiftmailer:
    transport: "%mailer_transport%"
    host:      "%mailer_host%"
    username:  "%mailer_user%"
    password:  "%mailer_password%"
    spool:     { type: memory }
```

## File: `app/config/config_dev.yml`
```yaml
imports:
    - { resource: config.yml }

framework:
    router:
        resource: "%kernel.root_dir%/config/routing_dev.yml"
        strict_requirements: true
    profiler: { only_exceptions: false }

web_profiler:
    toolbar: true
    intercept_redirects: false

monolog:
    handlers:
        main:
            type: stream
            path: "%kernel.logs_dir%/%kernel.environment%.log"
            level: debug
            channels: ["!event"]
        console:
            type:   console
            channels: ["!event", "!doctrine"]
        # uncomment to get logging in your browser
        # you may have to allow bigger header sizes in your Web server configuration
        #firephp:
        #    type:   firephp
        #    level:  info
        #chromephp:
        #    type:   chromephp
        #    level:  info

#swiftmailer:
#    delivery_address: me@example.com
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
            type:         fingers_crossed
            action_level: error
            handler:      nested
        nested:
            type:  stream
            path:  "%kernel.logs_dir%/%kernel.environment%.log"
            level: debug
        console:
            type:  console
```

## File: `app/config/config_test.yml`
```yaml
imports:
    - { resource: config_dev.yml }

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

doctrine:
    dbal:
        dbname:   "test_%database_name%" # Allow test in parallel
```

## File: `app/config/parameters.yml.dist`
```
# This file is a "template" of what your parameters.yml file should look like
# Set parameters here that may be different on each deployment target of the app, e.g. development, staging, production.
# http://symfony.com/doc/current/best_practices/configuration.html#infrastructure-related-configuration
parameters:
    database_host:     mysql
    database_port:     ~
    database_name:     ddd
    database_user:     root
    database_password: root

    redis_host: redis
    session_ttl: 7800

    mailer_transport:  smtp
    mailer_host:       127.0.0.1
    mailer_user:       ~
    mailer_password:   ~

    # A secret key that's used to generate certain security-related tokens
    secret:            ThisTokenIsNotSoSecretChangeIt

    jwt_private_key_path: '%kernel.root_dir%/config/security/jwt/private.pem'
    jwt_public_key_path: '%kernel.root_dir%/config/security/jwt/public.pem'

    jwt_key_pass_phrase:  'leonardo'
    jwt_token_ttl:        86400

    api_supported_versions: v1|v2

    rmq_host: rmq
    rmq_port: 5672
    rmq_user: guest
    rmq_pass: guest

    elastic_host: elasticsearch
    elastic_port: 9200
```

## File: `app/config/routing.yml`
```yaml
NelmioApiDocBundle:
    resource: "@NelmioApiDocBundle/Resources/config/routing.yml"
    prefix:   /api/doc

api:
    type:   rest
    prefix: /api/{version}
    defaults:
        _format: json
        version: v1

    requirements:
        _format: "json"
        version: "(%api_supported_versions%)"
    resource: "@LeosUIRestBundle/Resources/config/routing.yml"

public:
    type:   rest
    prefix: /
    defaults:
        _format: json
    requirements:
        _format: "json"

    resource: "@LeosUIRestBundle/Resources/config/routing_public.yml"
```

## File: `app/config/routing_dev.yml`
```yaml
_wdt:
    resource: "@WebProfilerBundle/Resources/config/routing/wdt.xml"
    prefix:   /_wdt

_profiler:
    resource: "@WebProfilerBundle/Resources/config/routing/profiler.xml"
    prefix:   /_profiler

_errors:
    resource: "@TwigBundle/Resources/config/routing/errors.xml"
    prefix:   /_error

_main:
    resource: routing.yml
```

## File: `app/config/security.yml`
```yaml
# To get started with security, check out the documentation:
# http://symfony.com/doc/current/book/security.html
security:
    encoders:
        harsh:
            algorithm: bcrypt
            cost: 12

    providers:
        customers:
            id: leos.security.user_provider

    firewalls:
        # disables authentication for assets and the profiler, adapt it according to your needs
        dev:
            pattern: ^/(_(profiler|wdt)|css|images|js)/
            security: false
            stateless:  true

        doc_area:
            pattern:    ^/api/doc
            stateless: true
            security: false

        secured_area:
            pattern:    ^/api/
            stateless: true
            provider: customers
            guard:
                authenticators:
                    - lexik_jwt_authentication.jwt_token_authenticator

        public:
            pattern:  ^/
            stateless: true
            anonymous: true

    access_control:

        - { path: ^/,     roles: IS_AUTHENTICATED_ANONYMOUSLY }
        - { path: ^/api/doc,     roles: IS_AUTHENTICATED_ANONYMOUSLY }

        - { path: ^/api/,  roles: IS_AUTHENTICATED_FULLY       }
```

## File: `app/config/services.yml`
```yaml
services:
    _defaults:
        public: false
        autowire: true

    JMS\Serializer\SerializerInterface: "@jms_serializer"
    Lexik\Bundle\JWTAuthenticationBundle\Services\JWTTokenManagerInterface: "@lexik_jwt_authentication.jwt_manager"
    Symfony\Component\Form\FormFactoryInterface: "@form.factory"
    Symfony\Component\Security\Http\Authentication\AuthenticationUtils: "@security.authentication_utils"
    Symfony\Component\Security\Core\Encoder\EncoderFactoryInterface: "@security.encoder_factory.generic"
    Psr\Log\LoggerInterface: "@monolog.logger"
```

## File: `app/config/bundles/bus.yml`
```yaml
tactician:
    commandbus:
        default:
            middleware:
                - leos.event.bus.middleware.dispatcher
                - tactician.middleware.doctrine
                - leos.event.bus.middleware.event_publisher
                - leos.event.bus.middleware.event_store
                - tactician.middleware.command_handler
        query:
            middleware:
                - tactician.middleware.command_handler
```

## File: `app/config/bundles/doc.yml`
```yaml
nelmio_api_doc:
    sandbox:
        authentication:
            delivery: header
            name: access_token
    cache:
        enabled: true
    exclude_sections: ["private", "exclusive"]
    swagger:
        api_base_path: /api
        swagger_version: 1.2
        api_version: 3.14
        info:
            title: DDD PlayGroud
            description: Sandbox environment
            contact: jorge.arcoma@gmail.com
            license: MIT
```

## File: `app/config/bundles/doctrine.yml`
```yaml
# Doctrine Configuration
doctrine:
    dbal:
        driver:   pdo_mysql
        host:     "%database_host%"
        port:     "%database_port%"
        dbname:   "%database_name%"
        user:     "%database_user%"
        password: "%database_password%"
        charset:  UTF8
        server_version: '5.7'

        types:
            walletId: Leos\Infrastructure\WalletBundle\Doctrine\Types\WalletIdType
            transactionId: Leos\Infrastructure\TransactionBundle\Doctrine\Types\TransactionIdType
            userId: Leos\Infrastructure\UserBundle\Doctrine\Types\UserIdType
            eventAwareId: Leos\Infrastructure\CommonBundle\Doctrine\Types\EventAwareIdType

        mapping_types:
            json: string

    orm:
        auto_generate_proxy_classes: "%kernel.debug%"
        naming_strategy: doctrine.orm.naming_strategy.underscore
        auto_mapping: true
        mappings:

            Transaction:
                type: yml
                prefix: Leos\Domain\Transaction\Model
                dir: '%kernel.root_dir%/../src/Infrastructure/TransactionBundle/Resources/config/persistence/Model'
                is_bundle: false

            TransactionValueObject:
                type: yml
                prefix: Leos\Domain\Transaction\ValueObject
                dir: '%kernel.root_dir%/../src/Infrastructure/TransactionBundle/Resources/config/persistence/ValueObject'
                is_bundle: false

            Payment:
                type: yml
                prefix: Leos\Domain\Payment\Model
                dir: '%kernel.root_dir%/../src/Infrastructure/PaymentBundle/Resources/config/persistence/Model'
                is_bundle: false


            WalletFactory:
                type: yml
                prefix: Leos\Domain\Wallet\Factory
                dir: '%kernel.root_dir%/../src/Infrastructure/WalletBundle/Resources/config/persistence/Factory'
                is_bundle: false

            Wallet:
                type: yml
                prefix: Leos\Domain\Wallet\Model
                dir: '%kernel.root_dir%/../src/Infrastructure/WalletBundle/Resources/config/persistence/Model'
                is_bundle: false

            Money:
                type: yml
                prefix: Leos\Domain\Money\ValueObject
                dir: '%kernel.root_dir%/../src/Infrastructure/MoneyBundle/Resources/config/persistence/ValueObject'
                is_bundle: false

            WalletValueObject:
                type: yml
                prefix: Leos\Domain\Wallet\ValueObject
                dir: '%kernel.root_dir%/../src/Infrastructure/WalletBundle/Resources/config/persistence/ValueObject'
                is_bundle: false

            User:
                type: yml
                prefix: Leos\Domain\User\Model
                dir: '%kernel.root_dir%/../src/Infrastructure/UserBundle/Resources/config/persistence/Model'
                is_bundle: false

            Security:
                type: yml
                prefix: Leos\Domain\Security\ValueObject
                dir: '%kernel.root_dir%/../src/Infrastructure/SecurityBundle/Resources/config/persistence/ValueObject'
                is_bundle: false

            Common:
                type: yml
                prefix: Leos\Infrastructure\CommonBundle\Event
                dir: '%kernel.root_dir%/../src/Infrastructure/CommonBundle/Resources/config/persistence'
                is_bundle: false
```

## File: `app/config/bundles/elastic.yml`
```yaml
fos_elastica:
  clients:
    default: { host: '%elastic_host%', port: '%elastic_port%' }
  indexes:
    events:
      types:
        events:
          properties:
            type: ~
            uuid: ~
            event: ~
            createdAt: ~
```

## File: `app/config/bundles/jwt.yml`
```yaml
lexik_jwt_authentication:
    private_key_path: "%jwt_private_key_path%"
    public_key_path:  "%jwt_public_key_path%"
    pass_phrase:      "%jwt_key_pass_phrase%"
    token_ttl:        "%jwt_token_ttl%"
    user_identity_field: username
    token_extractors:
        authorization_header:
            enabled: true
            prefix:  Bearer
            name:    Authorization
        cookie:
            enabled: true
            name:    BEARER
        query_parameter:
            enabled: false
```

## File: `app/config/bundles/redis.yml`
```yaml
snc_redis:
    clients:
        default:
            type: predis
            alias: default
            dsn: "redis://%redis_host%"

        session:
            type: predis
            alias: session
            dsn: "redis://%redis_host%"
    session:
        client: session
        prefix: ddd:session:
        ttl: "%session_ttl%"
```

## File: `app/config/bundles/rest.yml`
```yaml
fos_rest:
    versioning:
        enabled: true
        resolvers:
            query:
              parameter_name: version
            media_type:
                enabled: true
                regex: '/(v|version)=(?P<version>[0-9\.]+)/'

    serializer:
        version: "v1"
        serialize_null: true

    routing_loader:
        default_format: json

    view:
        view_response_listener: 'force'
        formats:
            json: true

        mime_types:
            json: ['application/json', 'application/json;version=2.0']

    format_listener:
        rules:
            - { path: '^/', priorities: ['json'], fallback_format: json, prefer_extension: true }

    param_fetcher_listener: force

    exception:
        enabled: true
        codes:
            'InvalidArgumentException': 400
            'Doctrine\ORM\OptimisticLockException': 409
            'Doctrine\DBAL\Exception\UniqueConstraintViolationException': 409

            'Leos\Domain\Common\Exception\NotFoundException': 404
            'Leos\Domain\Security\Exception\AuthenticationException': 401

            'Leos\Domain\Wallet\Exception\Credit\CreditNotEnoughException': 409
            'Leos\Domain\Transaction\Exception\InvalidTransactionTypeException': 409
            'Leos\Domain\Transaction\Exception\InvalidTransactionStateException': 409

        messages:
            'InvalidArgumentException': true
            'Leos\Domain\Common\Exception\NotFoundException': true
            'Leos\Domain\Security\Exception\AuthenticationException': true
            'Leos\Domain\Wallet\Exception\Credit\CreditNotEnoughException': true
            'Leos\Domain\Transaction\Exception\InvalidTransactionTypeException': true
            'Leos\Domain\Transaction\Exception\InvalidTransactionStateException': true
```

## File: `app/config/bundles/rmq.yml`
```yaml
old_sound_rabbit_mq:
    connections:
        default:
            host:     "%rmq_host%"
            port:     "%rmq_port%"
            user:     "%rmq_user%"
            password: "%rmq_pass%"
            vhost:    '/'
            lazy:     true
            connection_timeout: 3
            read_write_timeout: 3

            keepalive: false

            heartbeat: 0

    producers:
        events:
            connection:       default
            exchange_options: { name: 'events', type: topic }


    multiple_consumers:
        events:
            connection:       default
            exchange_options: { name: 'events', type: topic }
            queues:
                user:
                    name:     user
                    callback: leos.evens.async.consumer.events
                    routing_keys:
                        - 'UserWasCreated'
                transactions:
                    name:     transactions
                    callback: leos.evens.async.consumer.events
                    routing_keys:
                        - 'TransactionWasCreated'
                elastic:
                    name:     elastic
                    routing_keys:
                        - '#'
                    callback: leos.evens.async.store.events
```

## File: `app/config/bundles/serializer.yml`
```yaml
jms_serializer:
  metadata:
    auto_detection: true
    directories:
      Common:
        namespace_prefix: "Leos\\Domain\\Common"
        path: "@LeosInfrastructureCommonBundle/Resources/config/serializer/common"

      Wallet:
        namespace_prefix: "Leos\\Domain\\Wallet"
        path: "@LeosInfrastructureWalletBundle/Resources/config/serializer/wallet"

      Money:
        namespace_prefix: "Leos\\Domain\\Money"
        path: "@LeosInfrastructureMoneyBundle/Resources/config/serializer/money"

      Transaction:
        namespace_prefix: "Leos\\Domain\\Transaction"
        path: "@LeosInfrastructureTransactionBundle/Resources/config/serializer/transaction"

      Payment:
        namespace_prefix: "Leos\\Domain\\Payment"
        path: "@LeosInfrastructurePaymentBundle/Resources/config/serializer"

      Security:
        namespace_prefix: "Leos\\Domain\\Security"
        path: "@LeosInfrastructureSecurityBundle/Resources/config/serializer/auth"

      User:
        namespace_prefix: "Leos\\Domain\\User"
        path: "@LeosInfrastructureUserBundle/Resources/config/serializer/user"
```

## File: `app/config/security/jwt/private.pem`
```
-----BEGIN RSA PRIVATE KEY-----
Proc-Type: 4,ENCRYPTED
DEK-Info: AES-256-CBC,4658E645E01B6A1325B67F19F045818E

6W5HsM5bRDJP2FvXDWoy+HhS3UJJBtfkzfsVTeZnjZI68HOEIAdDMrAoi8sFvf4C
+sSM1QvKCqDW4wMG/VhjUdfZ0p6Az2JXAXOVSx1HtFWbAGuoOrmDBRwX2s/cDaRg
iHsrZN28W7s8Sf2XqFhSFxlFHnpo3i+IlOtRUmY4wZpl6pMFplf7mpQaZq0aQo5i
4ZzC9pUln6GQ3P/uiKFd2CMUg1Jt3HwGt09kIediXzGKaxtEpZ6UmoH2yPZprXE7
n2Gm+sQaC2fSRJKOVfhYNM1WT5Hc4p906XthxpNFzIqFopP3Effh5sXciMj4s9bD
q+RuX8uF942BupNIG5Px15jIfc0V7S5Erl1a6cj28Mrvh1ndUnBVjS2jCzd9poQI
GXQ5gUl/BiTv6XgId2h/fC06fsMXjsJNmESkqVkDPIdcqXBcTkLQU11sW/PF20zw
fdQZLHimVSgu/LTckzujf78O9Hqtdya9UdxVD/ahYG+OH+7ubvUUV7Gs00Y/VFmD
5jigMOEFSkbxZh7VnYRnfDoMLatTtwIV/tRStfPKJ54t0ZDRnNmxg7+5G7fCwpsf
ycf5NDnUQnxyGu6zxn3d9W67LvVVzIIk1XSvCCvHmJ3LcsFSxLAUbUrGsq3ixxoN
DCgduZUaDWYKErBiMO3gywzKgeffgo1Y7elqRXoVcUVZdUYSdIvFCGUkNmXiENG8
y1QmZlblVb54GVLe8ABZKPAhT7RFwA9YiNSc5usYA3s0ADLI2vfYQaX5kRnmAX+6
rwSa3IHzJIoD4efak4tEgC7IUO/hhAbaOXiZQeSnQ+Ko7LKEDbWJ8MEXRq+4f6qp
4LIJOxIT3SS2aBTMRSYsKgAObwTjIGdrXpinPkjVXdCFZ6mcyuVPinUXIRyUJEn7
qHHec8CmHZ1D+qgiqC8CrFvFuysJ86UyY/kVbt2Ld+UoaBOx9cZFFEINMcstV0c1
GSYFKhGHPoMUIj3A0QgLA10MQJ8s4H6uQdvrbtCXRg1FpK5DokOMi3iSi63hjrR+
AOQj/0J1qI9mtOTsyKI+k+rB+xvDsLHMbsYI92VK/dNIUBSRPSI3XK429IakyyA4
olvL+abzlhFM86yDVfFBbxDn32Hh2d4rFkyhPHvO5dWspXrYyj4wcL8ezD4KyjcP
erCgvT3ol5yzcx0UBwrcbqZClLtS3p3nTwOXehRAJb6MPaDlNtSwMZMr93cQY9i+
eEDwu8DTCKLND4GULPfEl64A1yz61KMHLqHjZEmhf+RDt8Hb3TT9MDSU9sN1MIHF
cUeWEZ6V6+oE3I4R/KPdYPSvAw8FKOKawXtYqCUa4Q9/gpbZ8pPU9EHgAcBJ1kCm
MNUy5B2IKD9GDZxdCbBEkzR1bK9ll05Tta8PcdBPScFe/gDo2myWgWqeYRFtnqhR
Kr8j0S7mlT6gAr8iqnTDbQ+zhRKaFM9j+ijx0CK6mY3wuxT6SkNSqdoMWgI9ScZz
jWzSbehI32tmSGsXM/YoBni5VRCpD73uSNdf/pr1MpNjfn/XMgwczAsi6aMaRahJ
evJvWYC/qOFOd4mBAlg4ARI0GMUVhlqrPCr+mzxx/blf7ImrApA9Pa8BTdxdeuSr
pOr9Jg6L2XHz4IkDRhwXBYYILOIB1VUF4FjKmlWoQUsCjJKg5XwIiPoiPRttLYpd
KMPwJPqGffcy6KHCD6DpgOePecq4rvGA6OLplerZy7ymrhF+HX8cwahdJtRFA87H
oRPC4mnqw3/aqlVwcPTvHl5BYAZhZosSmduXx741zlZ6tNkK4iA/bM44TaQfx6Q1
LYA/U6g3jjoofr7vLDwEeLreyqHWd96LwrFJCaePX+yiO9IaiW0MItM6NRQBda4F
jL49JlpnzE7zp/vTYY4XsCIir8Ap4qmRtWA+bJlhh6FXglnwby6Ehdpv8VbBSbea
xZ/qK+p+QiU59B2ekXAePybc9Wlo94H1ojEfwNZXOTPBvAMZIkZy/dZf/5NUghrw
9QHOv/b3S5fs+S/K0AuVC8reFYkw3ad4rxr4Pggtw1GrSt3KgCRy9RFogdOxDn63
QhhFcpnUOdP5Q05q84uEzWvBxtDydEcIoXzR/9Yki1tL7yzLCoysdVSeqyiLZrRg
QjMUvvwK2yc/tSeoGHz9nuSU8npx8qF7IpMSFRdi40471Km6iDsJl+T1jf4G5dxI
vhkXTCsdWbnulue01oRSp1ktcFYgulX353r4j9tLQmANujxGSI7GW1z8qCpvXhYu
PjkjpYqosXcr6Vt2ywB5+5t+xJZgFmLc9Z2usbLsLot7ZMh87ajcHKEXacaVvAJH
CuF461m/M3vIOzxEUErRzEOINzgT1dTk2gkk91kjmDneTiI5/7jKR7Hwgvc2k/Ol
B3XuL3e3ruWhd/WC5vUv+H5ICLTncKSq6H5VDWQLkScKERHdI87K49awbtq+scaH
6xcf4v184W9vhSqHkT1YhvUizu1aRvfv/B1/+bwIVriMP2/cXBJoGwKXzPyzSrXY
KF6kvT1jquT9MHk3livRExDt8ta4qrPLrbtTtNtwRgYjhDJI04B2LJoX6ewv3KNX
2KIKBtR36EBmMFBLkGuNgTfT2VmW7rXxmWS9eDdzLVOWAay7Gfkg/OHYiO2eL7je
vK+T5zGyrm8mv+zZYmuR0HdtQGIrmLdkRFDPf0HcNrbf87frFjT0vqNcJFJ/YGyh
ZnWTHEmCGR87bIRc6SJ9DpLPbu0ab4aicoe74CcMnQ4I590BKUL4xqHQ75et//Tv
HvGhWilTl6opyRvdQ/65lgniOsf2mrgkQD6WdRe+GK8/m62JL+mdfAuBnUA51trD
BI35nO21J4oWMmYp3zb+cnwvkFOT+NHpGEieqzvr2Yk1QG0ZPiVfxZGePkY0lPIR
o8QeeAQ1rgwQPkAUQmOPCLyKWnu96BT2s76hs+MvEOWA6ObJo75eb1WfRpmUmdlJ
AaALr3AkuRvYrL+1j/ojr4XHCUxdzh6UoFu4JLwkGRxAtDrKtvDcQmFJvw2lWbfr
uW9zdhucCpeCPHO5zG22FPV2iYg9YWJeGhG+D6aPp7/So3s/JiLAqjgBiT89OKRE
gmHco2gqZuobKmW6m5feZRf9Gh8/VvpUQa1IBCAtRQ9euP+/RGPL2RZ/J4Enn+Aa
-----END RSA PRIVATE KEY-----
```

## File: `app/config/security/jwt/public.pem`
```
-----BEGIN PUBLIC KEY-----
MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAtwgCQ1bKd6dH/gfn5/q+
pXnjuWFL7eqfBbapE/AxKnZMuJcFSx/6uAjk/8PZrLDcZpx+IuzMH0/2n7tEW1Vs
beBP9X7wvsU3f3KJTH5ieYWUT77jUrn4NVJyHCU7s+00yKvRTrw9QUSpbwSGm4ah
abiOdiKBl0bjc6dxaj/f9hnK2VuL7aDSWLlEg/RfOnprzw3huDAWNXr4rNKXArWE
67vexVPxfkK+z2YMNVUmuzyDsXORAy4vKed5N25Z+BtNnF2HWJbo/p3OkHnFR1Ti
55gn34+CzSvGd6/iadFmXsLyFoKcIM3X+yypE3vDpkNrb7efHuZEHZsd4IezheFL
jhit3Eooy2LZEeCqHmCChKGkjiXnK9nhl18ssBqRbtjsZZIEPYXPRK9uzvGZmWYr
8IZyCKrhq4H0oKxev3yN37hKry2zFEC9Epyw1RLSr4s5/0MQ5f//7EVZcAGqw9dd
HOajInQ2IVNQgWJz/r0TjNbtzHFjByYDI0/dCAcRlnBH8UbyKQAIGyfKEpYXhZ/u
EaKZuhgms2CvTzDZj3BHa5w3zcAH08qkkud5jHHX/9zYJliALHwtEVg9s4imzzTS
01nved4TiGczm7KruGnMUPbi1GUVA5Xa5ntYs7LuCGpAa8VfEA5rKVP6Jp19gfqb
f6BiGnlPn9E1IQV+kn/LvjkCAwEAAQ==
-----END PUBLIC KEY-----
```

## File: `etc/infrastructure/dev/docker-compose.yml`
```yaml
version: '2'
services:
  nginx:
    build: nginx
    depends_on:
      - fpm
    ports:
      - "80:80"
    volumes_from:
      - fpm

  fpm:
    image: jorge07/alpine-php:7.1-dev-sf
    ports:
      - "2323:22"
      - "9000:9000"
    volumes:
      - "$PWD:/app"
    depends_on:
      - mysql

  redis:
    image: redis:3.2-alpine

  mysql:
    image: mysql:5.7
    ports:
      - "3306:3306"
    environment:
      - MYSQL_ROOT_PASSWORD=root
      - MYSQL_DATABASE=ddd
    volumes:
      - db_data:/var/lib/mysql

  rmq:
    image: rabbitmq:3-management
    environment:
      RABBITMQ_ERLANG_COOKIE: "SWQOKODSQALRPCLNMEQG"
      RABBITMQ_DEFAULT_USER: "guest"
      RABBITMQ_DEFAULT_PASS: "guest"
      RABBITMQ_DEFAULT_VHOST: "/"
    ports:
      - "15672:15672"
      - "5672:5672"

  kibana:
    image: kibana:5.5
    ports:
      - 5601:5601
    volumes:
      - "$PWD/etc/infrastructure/dev/kibana/config:/usr/share/kibana/config"

  elasticsearch:
    image: elasticsearch:5.5
    ports:
      - 9200:9200

volumes:
  db_data:
```

## File: `etc/infrastructure/dev/kibana/config`
```
---
## Default Kibana configuration from kibana-docker.
## from https://github.com/elastic/kibana-docker/blob/master/build/kibana/config/kibana.yml
#
server.name: kibana
server.host: "0"
elasticsearch.url: http://elasticsearch:9200

## Disable X-Pack
## see https://www.elastic.co/guide/en/x-pack/current/xpack-settings.html
##     https://www.elastic.co/guide/en/x-pack/current/installing-xpack.html#xpack-enabling
#
xpack.security.enabled: false
xpack.monitoring.enabled: false
xpack.ml.enabled: false
xpack.graph.enabled: false
xpack.reporting.enabled: false
xpack.grokdebugger.enabled: false
```

## File: `etc/infrastructure/dev/nginx/Dockerfile`
```
FROM nginx:1.11-alpine

RUN apk --update add curl \
    && rm -rf /var/cache/apk/*

COPY ddd.conf /etc/nginx/conf.d/default.conf

RUN mkdir -p /app/var/logs/nginx \
    && touch /app/var/logs/nginx/access.log && ln -sf /dev/stdout /app/var/logs/nginx/access.log \
    && touch /app/var/logs/nginx/error.log  && ln -sf /dev/stdout /app/var/logs/nginx/error.log

HEALTHCHECK --interval=5m --timeout=3s \
  CMD curl -f http://localhost/monitor/ping || exit 1

```

## File: `etc/infrastructure/dev/nginx/ddd.conf`
```
server {
    server_name ddd.dev www.ddd.dev;
    root /app/web;

    location / {
        # try to serve file directly, fallback to app.php
        try_files $uri /app_dev.php$is_args$args;
    }
    # DEV
    # This rule should only be placed on your development environment
    # In production, don't include this and don't deploy app_dev.php or config.php
    location ~ ^/(app|app_dev|config)\.php(/|$) {
        fastcgi_pass fpm:9000;
        fastcgi_split_path_info ^(.+\.php)(/.*)$;
        include fastcgi_params;
        # When you are using symlinks to link the document root to the
        # current version of your application, you should pass the real
        # application path instead of the path to the symlink to PHP
        # FPM.
        # Otherwise, PHP's OPcache may not properly detect changes to
        # your PHP files (see https://github.com/zendtech/ZendOptimizerPlus/issues/126
        # for more information).
        fastcgi_param  SCRIPT_FILENAME  $realpath_root$fastcgi_script_name;
        fastcgi_param DOCUMENT_ROOT $realpath_root;
    }
}
```

## File: `etc/infrastructure/prod/docker-compose.build.yml`
```yaml
version: '2'
services:
  fpm:
    build:
      context: ../context-${RELEASE}/build
      dockerfile: fpm/Dockerfile
    image: sf-prod:${RELEASE}

  nginx:
    build:
      context: ../context-${RELEASE}/build
      dockerfile: nginx/Dockerfile
    image: nginx-prod:${RELEASE}
```

## File: `etc/infrastructure/prod/docker-compose.yml`
```yaml
version: '2'
services:
  fpm:
    image: registry.gitlab.com/jorge07/leos-sf-prod:${RELEASE}

  nginx:
    image: registry.gitlab.com/jorge07/leos-nginx-prod:${RELEASE}
```

## File: `etc/infrastructure/prod/fpm/Dockerfile`
```
FROM jorge07/alpine-php:7.1

ENV SYMFONY_ENV prod

COPY app/app /app/app
COPY fpm/parameters.yml /app/app/config/parameters.yml
COPY app/bin /app/bin
COPY app/var /app/var
COPY app/web /app/web
COPY app/src /app/src
COPY app/vendor /app/vendor

RUN php /app/bin/console c:w
```

## File: `etc/infrastructure/prod/fpm/parameters.yml`
```yaml
parameters:
    database_host: mysql
    database_port: null
    database_name: ddd
    database_user: root
    database_password: root
    redis_host: redis
    session_ttl: 7800
    mailer_transport: smtp
    mailer_host: 127.0.0.1
    mailer_user: null
    mailer_password: null
    secret: ThisTokenIsNotSoSecretChangeIt
    jwt_private_key_path: %kernel.root_dir%/security/jwt/private.pem
    jwt_public_key_path:  %kernel.root_dir%/security/jwt/public.pem
    jwt_key_pass_phrase:  'leonardo'
    jwt_token_ttl:        86400
```

## File: `etc/infrastructure/prod/nginx/Dockerfile`
```
FROM nginx:1.11-alpine

RUN apk --update add curl \
    && rm -rf /var/cache/apk/*

COPY nginx/ddd.conf /etc/nginx/conf.d/default.conf
COPY app/web /app/web

RUN rm -rf /app/web/app_dev.php

HEALTHCHECK --interval=5m --timeout=3s \
  CMD curl -f http://localhost/monitor/ping || exit 1
```

## File: `etc/infrastructure/prod/nginx/ddd.conf`
```
server {
    root /app/web;

    location / {
        # try to serve file directly, fallback to app.php
        try_files $uri /app.php$is_args$args;
    }
    # PROD
    location ~ ^/app\.php(/|$) {
        fastcgi_pass fpm:9000;
        fastcgi_split_path_info ^(.+\.php)(/.*)$;
        include fastcgi_params;
        # When you are using symlinks to link the document root to the
        # current version of your application, you should pass the real
        # application path instead of the path to the symlink to PHP
        # FPM.
        # Otherwise, PHP's OPcache may not properly detect changes to
        # your PHP files (see https://github.com/zendtech/ZendOptimizerPlus/issues/126
        # for more information).
        fastcgi_param  SCRIPT_FILENAME  $realpath_root$fastcgi_script_name;
        fastcgi_param DOCUMENT_ROOT $realpath_root;
        # Prevents URIs that include the front controller. This will 404:
        # http://letsbonus-api.dev/app.php/some-path
        # Remove the internal directive to allow URIs like this
        internal;
    }
}
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

## File: `src/Application/Request/Common/Pagination.php`
```php
<?php

namespace Leos\Application\Request\Common;

/**
 * Class Pagination
 * 
 * @package Leos\Application\Request\Common
 */
class Pagination
{

    const
        LIMIT = 500,
        PAGE = 1
    ;

    /**
     * @var array
     */
    private $filters = [];

    /**
     * @var array
     */
    private $operators = [];

    /**
     * @var array
     */
    private $values = [];

    /**
     * @var array
     */
    private $sort = [];

    /**
     * @var int
     */
    private $limit = self::LIMIT;

    /**
     * @var int
     */
    private $page = self::PAGE;

    /**
     * Pagination constructor.
     * @param array $data
     */
    public function __construct(array $data = [])
    {
        $this->filters   = $data['filterParam'] ?? [];
        $this->operators = $data['filterOp'] ?? [];
        $this->values    = $data['filterValue'] ?? [];
        $this->sort      = array_combine($data['orderParameter'] ?? [], $data['orderValue'] ?? []);
        $this->limit     = $data['limit'] ?? self::LIMIT;
        $this->page      = $data['page'] ?? self::PAGE;
    }

    /**
     * @return array
     */
    public function getFilters(): array
    {
        return $this->filters;
    }

    /**
     * @return array
     */
    public function getOperators(): array
    {
        return $this->operators;
    }

    /**
     * @return array
     */
    public function getValues(): array
    {
        return $this->values;
    }

    /**
     * @return array
     */
    public function getSort(): array
    {
        return $this->sort;
    }

    /**
     * @return int
     */
    public function getLimit(): int
    {
        return $this->limit;
    }

    /**
     * @return int
     */
    public function getPage(): int
    {
        return $this->page;
    }
}
```

## File: `src/Application/UseCase/Security/LoginHandler.php`
```php
<?php

namespace Leos\Application\UseCase\Security;

use Leos\Application\UseCase\Security\Request\Login;

use Leos\Domain\Security\Exception\AuthenticationException;
use Leos\Domain\User\Model\User;
use Leos\Domain\User\Repository\UserRepositoryInterface;

use Leos\Infrastructure\SecurityBundle\Security\Model\Auth;

use Lexik\Bundle\JWTAuthenticationBundle\Services\JWTTokenManagerInterface;
use Symfony\Component\Security\Core\Encoder\EncoderFactoryInterface;
use Symfony\Component\Security\Http\Authentication\AuthenticationUtils;

/**
 * Class LoginHandler
 *
 * @package Leos\Application\UseCase\Security
 */
class LoginHandler
{
    /**
     * @var AuthenticationUtils
     */
    private $authenticationUtils;

    /**
     * @var UserRepositoryInterface
     */
    private $userRepository;

    /**
     * @var EncoderFactoryInterface
     */
    private $encoderFactory;

    /**
     * @var JWTTokenManagerInterface
     */
    private $JWTManager;

    /**
     * LoginHandler constructor.
     *
     * @param AuthenticationUtils $authenticationUtils
     * @param UserRepositoryInterface $userRepository
     * @param EncoderFactoryInterface $encoderFactory
     * @param JWTTokenManagerInterface $JWTManager
     */
    public function __construct(
        AuthenticationUtils $authenticationUtils,
        UserRepositoryInterface $userRepository,
        EncoderFactoryInterface $encoderFactory,
        JWTTokenManagerInterface $JWTManager
    )
    {
        $this->authenticationUtils = $authenticationUtils;
        $this->userRepository = $userRepository;
        $this->encoderFactory = $encoderFactory;
        $this->JWTManager = $JWTManager;
    }

    /**
     * @param Login $request
     * @return string
     * @throws AuthenticationException
     */
    public function handle(Login $request): string
    {
        /** @var User $user */
        $user = $this->userRepository->findOneByUsername($request->username());

        if (!$user) {

            throw new AuthenticationException();
        }

        $authUser = new Auth(
            (string) $user->uuid(),
            $user->auth()
        );

        $encoder = $this->encoderFactory->getEncoder($authUser);

        if (!$encoder->isPasswordValid($authUser->getPassword(), $request->plainPassword(), $authUser->getSalt())) {

            throw new AuthenticationException();
        }

        return $this->JWTManager->create($authUser);
    }
}
```

## File: `src/Application/UseCase/Security/Request/Login.php`
```php
<?php

namespace Leos\Application\UseCase\Security\Request;

/**
 * Class Login
 * 
 * @package Leos\Application\UseCase\Security\Request
 */
class Login
{
    /**
     * @var string
     */
    private $username;

    /**
     * @var string
     */
    private $plainPassword;

    /**
     * Login constructor.
     *
     * @param string $username
     * @param string $plainPassword
     */
    public function __construct(string $username, string $plainPassword)
    {
        $this->username = $username;
        $this->plainPassword = $plainPassword;
    }

    /**
     * @return string
     */
    public function username(): string
    {
        return $this->username;
    }

    /**
     * @return string
     */
    public function plainPassword(): string
    {
        return $this->plainPassword;
    }
}
```

## File: `src/Application/UseCase/Transaction/CreateDepositHandler.php`
```php
<?php

namespace Leos\Application\UseCase\Transaction;

use Leos\Application\UseCase\Transaction\Request\CreateDeposit;

use Leos\Application\UseCase\Wallet\GetWalletHandler;
use Leos\Application\UseCase\Wallet\Request\GetWallet;

use Leos\Domain\Payment\Model\Deposit;
use Leos\Domain\Payment\ValueObject\DepositDetails;
use Leos\Domain\User\Repository\UserRepositoryInterface;
use Leos\Domain\Transaction\Repository\TransactionRepositoryInterface;

/**
 * Class CreateDepositHandler
 *
 * @package Leos\Application\UseCase\Transaction
 */
class CreateDepositHandler
{
    /**
     * @var TransactionRepositoryInterface
     */
    private $repository;

    /**
     * @var UserRepositoryInterface
     */
    private $userRepository;

    /**
     * @var GetWalletHandler
     */
    private $walletQuery;

    /**
     * Withdrawal constructor.
     * @param TransactionRepositoryInterface $repository
     * @param UserRepositoryInterface $userRepository
     * @param GetWalletHandler $walletQuery
     */
    public function __construct(
        TransactionRepositoryInterface $repository,
        UserRepositoryInterface $userRepository,
        GetWalletHandler $walletQuery)
    {
        $this->repository = $repository;
        $this->userRepository = $userRepository;
        $this->walletQuery = $walletQuery;
    }

    /**
     * @param CreateDeposit $request
     *
     * @return Deposit
     */
    public function handle(CreateDeposit $request): Deposit
    {
        $wallet = $this->walletQuery->handle(new GetWallet($request->walletId()));

        $transaction = Deposit::create(
            $wallet,
            $request->real(),
            new DepositDetails($request->provider())
        );

        $this->repository->save($transaction);

        return $transaction;
    }
}
```

## File: `src/Application/UseCase/Transaction/CreateWalletHandler.php`
```php
<?php

namespace Leos\Application\UseCase\Transaction;

use Leos\Application\UseCase\Transaction\Request\CreateWallet;

use Leos\Domain\Wallet\Model\Wallet;
use Leos\Domain\Wallet\Factory\WalletFactory;
use Leos\Domain\User\Repository\UserRepositoryInterface;
use Leos\Domain\Transaction\Repository\TransactionRepositoryInterface;

/**
 * Class CreateWalletHandler
 *
 * @package Leos\Application\UseCase\Transaction
 */
class CreateWalletHandler
{
    /**
     * @var TransactionRepositoryInterface
     */
    private $repository;

    /**
     * @var UserRepositoryInterface
     */
    private $userRepository;

    /**
     * Withdrawal constructor.
     * @param TransactionRepositoryInterface $repository
     * @param UserRepositoryInterface $userRepository
     */
    public function __construct(
        TransactionRepositoryInterface $repository,
        UserRepositoryInterface $userRepository)
    {
        $this->repository = $repository;
        $this->userRepository = $userRepository;
    }

    /**
     * @param CreateWallet $request
     * @return Wallet
     */
    public function handle(CreateWallet $request): Wallet
    {
        $transaction = WalletFactory::create(
            $this->userRepository->findOneByUuid($request->userId()),
            $request->currency()
        );

        $this->repository->save($transaction);

        return $transaction->wallet();
    }
}
```

## File: `src/Application/UseCase/Transaction/RollbackDepositHandler.php`
```php
<?php

namespace Leos\Application\UseCase\Transaction;

use Leos\Application\UseCase\Transaction\Request\RollbackDeposit as RollbackDepositRequest;

use Leos\Domain\Payment\Model\Deposit;
use Leos\Domain\Payment\Model\RollbackDeposit;
use Leos\Domain\Transaction\Exception\InvalidTransactionTypeException;
use Leos\Domain\User\Repository\UserRepositoryInterface;
use Leos\Domain\Transaction\Repository\TransactionRepositoryInterface;

/**
 * Class RollbackDepositHandler
 *
 * @package Leos\Application\UseCase\Transaction
 */
class RollbackDepositHandler
{
    /**
     * @var TransactionRepositoryInterface
     */
    private $repository;

    /**
     * @var UserRepositoryInterface
     */
    private $userRepository;

    /**
     * Withdrawal constructor.
     * @param TransactionRepositoryInterface $repository
     * @param UserRepositoryInterface $userRepository
     */
    public function __construct(
        TransactionRepositoryInterface $repository,
        UserRepositoryInterface $userRepository)
    {
        $this->repository = $repository;
        $this->userRepository = $userRepository;
    }

    /**
     * @param RollbackDepositRequest $request
     * @return RollbackDeposit
     * @throws InvalidTransactionTypeException
     */
    public function handle(RollbackDepositRequest $request): RollbackDeposit
    {
        /** @var Deposit $deposit */
        $deposit = $this->repository->get($request->depositId());

        if (!$deposit instanceof Deposit) {

            throw new InvalidTransactionTypeException();
        }

        $rollback = $deposit->rollback();

        $this->repository->save($rollback);

        return $rollback;
    }
}
```

## File: `src/Application/UseCase/Transaction/RollbackWithdrawalHandler.php`
```php
<?php

namespace Leos\Application\UseCase\Transaction;

use Leos\Application\UseCase\Transaction\Request\RollbackWithdrawal as RollbackWithdrawalRequest;

use Leos\Domain\Payment\Model\Withdrawal;
use Leos\Domain\Payment\Model\RollbackWithdrawal;
use Leos\Domain\User\Repository\UserRepositoryInterface;
use Leos\Domain\Transaction\Exception\TransactionNotFoundException;
use Leos\Domain\Transaction\Exception\InvalidTransactionTypeException;
use Leos\Domain\Transaction\Repository\TransactionRepositoryInterface;

/**
 * Class RollbackWithdrawalHandler
 *
 * @package Leos\Application\UseCase\Wallet
 */
class RollbackWithdrawalHandler
{
    /**
     * @var TransactionRepositoryInterface
     */
    private $repository;

    /**
     * @var UserRepositoryInterface
     */
    private $userRepository;

    /**
     * @param TransactionRepositoryInterface $repository
     * @param UserRepositoryInterface $userRepository
     */
    public function __construct(
        TransactionRepositoryInterface $repository,
        UserRepositoryInterface $userRepository)
    {
        $this->repository = $repository;
        $this->userRepository = $userRepository;
    }

    /**
     * @param RollbackWithdrawalRequest $request
     *
     * @return RollbackWithdrawal
     *
     * @throws InvalidTransactionTypeException
     * @throws TransactionNotFoundException
     */
    public function handle(RollbackWithdrawalRequest $request): RollbackWithdrawal
    {
        $withdrawal = $this->repository->get($request->withdrawalId());

        if (!$withdrawal instanceof Withdrawal) {

            throw new InvalidTransactionTypeException();
        }

        $this->repository->save(
            $rollback = $withdrawal->rollback()
        );

        return $rollback;
    }

}
```

## File: `src/Application/UseCase/Transaction/WithdrawalHandler.php`
```php
<?php

namespace Leos\Application\UseCase\Transaction;

use Leos\Application\UseCase\Wallet\GetWalletHandler;
use Leos\Application\UseCase\Wallet\Request\GetWallet;
use Leos\Application\UseCase\Transaction\Request\Withdrawal as WithdrawalRequest;

use Leos\Domain\Payment\Model\Withdrawal;
use Leos\Domain\Payment\ValueObject\WithdrawalDetails;
use Leos\Domain\User\Repository\UserRepositoryInterface;
use Leos\Domain\Transaction\Exception\InvalidTransactionTypeException;
use Leos\Domain\Transaction\Repository\TransactionRepositoryInterface;

/**
 * Class WithdrawalHandler
 *
 * @package Leos\Application\UseCase\Transaction
 */
class WithdrawalHandler
{
    /**
     * @var TransactionRepositoryInterface
     */
    private $repository;

    /**
     * @var UserRepositoryInterface
     */
    private $userRepository;

    /**
     * @var GetWalletHandler
     */
    private $walletQuery;

    /**
     * Withdrawal constructor.
     * @param TransactionRepositoryInterface $repository
     * @param UserRepositoryInterface $userRepository
     * @param GetWalletHandler $walletQuery
     */
    public function __construct(
        TransactionRepositoryInterface $repository,
        UserRepositoryInterface $userRepository,
        GetWalletHandler $walletQuery)
    {
        $this->repository = $repository;
        $this->userRepository = $userRepository;
        $this->walletQuery = $walletQuery;
    }

    /**
     * @param WithdrawalRequest $request
     * @return Withdrawal
     * @throws InvalidTransactionTypeException
     */
    public function handle(WithdrawalRequest $request): Withdrawal
    {
        $wallet = $this->walletQuery->handle(new GetWallet($request->walletId()));

        $transaction = Withdrawal::create(
            $wallet,
            $request->real(),
            new WithdrawalDetails($request->provider())
        );

        $this->repository->save($transaction);

        return $transaction;
    }
}
```

## File: `src/Application/UseCase/Transaction/Request/CreateDeposit.php`
```php
<?php

namespace Leos\Application\UseCase\Transaction\Request;

use Leos\Domain\Money\ValueObject\Money;
use Leos\Domain\Money\ValueObject\Currency;
use Leos\Domain\Wallet\ValueObject\WalletId;
use Leos\Domain\Payment\Exception\MinDepositAmountException;

/**
 * Class CreateDeposit
 * 
 * @package Leos\Application\UseCase\Transaction\Request
 */
class CreateDeposit
{
    /**
     * @var WalletId
     */
    private $uid;

    /**
     * @var Money
     */
    private $real;
    /**
     * @var string
     */
    private $provider;

    /**
     * @param string $uid
     * @param string $currency
     * @param float $amountReal
     * @param string $provider
     */
    public function __construct(string $uid, string $currency, float $amountReal, string $provider)
    {
        $this->uid = new WalletId($uid);
        $this->setReal($amountReal, new Currency($currency));
        $this->provider = $provider;
    }

    /**
     * @param float $amount
     * @param Currency $currency
     *
     * @throws MinDepositAmountException
     */
    protected function setReal(float $amount, Currency $currency)
    {
        if (0.00 >= $amount) {

            throw new MinDepositAmountException();
        }

        $this->real = new Money($amount, $currency);
    }

    /**
     * @return WalletId
     */
    public function walletId(): WalletId
    {
        return $this->uid;
    }

    /**
     * @return Money
     */
    public function real(): Money
    {
        return $this->real;
    }

    /**
     * @return string
     */
    public function provider(): string
    {
        return $this->provider;
    }
}
```

## File: `src/Application/UseCase/Transaction/Request/CreateWallet.php`
```php
<?php

namespace Leos\Application\UseCase\Transaction\Request;

use Leos\Domain\User\ValueObject\UserId;
use Leos\Domain\Money\ValueObject\Currency;

/**
 * Class CreateWallet
 * 
 * @package Leos\Application\UseCase\Transaction\Request
 */
class CreateWallet
{
    /**
     * @var UserId
     */
    private $userId;

    /**
     * @var Currency
     */
    private $currency;

    /**
     * @param string $userId
     * @param string $currency
     */
    public function __construct(string $userId, string $currency = Currency::DEFAULT)
    {
        $this->userId = new UserId($userId);
        $this->currency = new Currency($currency);
    }

    /**
     * @return UserId
     */
    public function userId(): UserId
    {
        return $this->userId;
    }

    /**
     * @return Currency
     */
    public function currency(): Currency
    {
       return $this->currency;
    }

}
```

## File: `src/Application/UseCase/Transaction/Request/RollbackDeposit.php`
```php
<?php

namespace Leos\Application\UseCase\Transaction\Request;

use Leos\Domain\Transaction\ValueObject\TransactionId;

/**
 * Class RollbackDeposit
 * 
 * @package Leos\Application\UseCase\Transaction\Request
 */
class RollbackDeposit
{
    /**
     * @var TransactionId
     */
    private $depositId;

    /**
     * RollbackDeposit constructor.
     *
     * @param string $depositId
     */
    public function __construct(string $depositId)
    {
        $this->depositId = new TransactionId($depositId);
    }

    public function depositId(): TransactionId
    {
        return $this->depositId;
    }
}
```

## File: `src/Application/UseCase/Transaction/Request/RollbackWithdrawal.php`
```php
<?php

namespace Leos\Application\UseCase\Transaction\Request;

use Leos\Domain\Transaction\ValueObject\TransactionId;

/**
 * Class RollbackWithdrawal
 * 
 * @package Leos\Application\UseCase\Transaction\Request
 */
class RollbackWithdrawal
{
    /**
     * @var TransactionId
     */
    private $withdrawalId;

    /**
     * RollbackDepositDTO constructor.
     *
     * @param string $withdrawalId
     */
    public function __construct(string $withdrawalId)
    {
        $this->withdrawalId = new TransactionId($withdrawalId);
    }

    public function withdrawalId(): TransactionId
    {
        return $this->withdrawalId;
    }
}
```

## File: `src/Application/UseCase/Transaction/Request/Withdrawal.php`
```php
<?php

namespace Leos\Application\UseCase\Transaction\Request;

use Leos\Domain\Money\ValueObject\Money;
use Leos\Domain\Money\ValueObject\Currency;
use Leos\Domain\Wallet\ValueObject\WalletId;
use Leos\Domain\Payment\Exception\MinWithdrawalAmountException;

/**
 * Class Withdrawal
 * 
 * @package Leos\Application\UseCase\Transaction\Request
 */
class Withdrawal
{
    /**
     * @var WalletId
     */
    private $uid;

    /**
     * @var Money
     */
    private $real;
    /**
     * @var string
     */
    private $provider;

    /**
     * @param string $uid
     * @param string $currency
     * @param float $amountReal
     * @param string $provider
     */
    public function __construct(string $uid, string $currency, float $amountReal, string $provider)
    {
        $this->uid = new WalletId($uid);
        $this->setReal($amountReal, new Currency($currency));
        $this->provider = $provider;
    }

    /**
     * @param float $amount
     * @param Currency $currency
     */
    protected function setReal(float $amount, Currency $currency)
    {
        if (0.00 >= $amount) {

            throw new MinWithdrawalAmountException();
        }

        $this->real = new Money($amount, $currency);
    }

    /**
     * @return WalletId
     */
    public function walletId(): WalletId
    {
        return $this->uid;
    }

    /**
     * @return Money
     */
    public function real(): Money
    {
        return $this->real;
    }

    /**
     * @return string
     */
    public function provider(): string
    {
        return $this->provider;
    }
}
```

## File: `src/Application/UseCase/User/GetUserHandler.php`
```php
<?php

namespace Leos\Application\UseCase\User;

use Leos\Application\UseCase\User\Request\GetUser;

use Leos\Domain\User\Model\User;
use Leos\Domain\User\Exception\UserNotFoundException;
use Leos\Domain\User\Repository\UserRepositoryInterface;

/**
 * Class GetUserHandler
 *
 * @package Leos\Application\UseCase\User
 */
class GetUserHandler
{
    /**
     * @var UserRepositoryInterface
     */
    private $repository;

    public function __construct(UserRepositoryInterface $repository)
    {
        $this->repository = $repository;
    }

    /**
     * @param GetUser $request
     * @return User
     * @throws UserNotFoundException
     */
    public function handle(GetUser $request): User
    {
        return $this->repository->getOneByUuid($request->uuid());
    }
}
```

## File: `src/Application/UseCase/User/RegisterUserHandler.php`
```php
<?php

namespace Leos\Application\UseCase\User;

use Leos\Application\UseCase\User\Request\Register;

use Leos\Domain\User\Model\User;
use Leos\Domain\User\Factory\UserFactoryInterface;
use Leos\Domain\User\Repository\UserRepositoryInterface;

/**
 * Class RegisterUserHandler
 * 
 * @package Leos\Application\UseCase\User
 */
class RegisterUserHandler
{
    /**
     * @var UserRepositoryInterface
     */
    private $repository;
    
    /**
     * @var UserFactoryInterface
     */
    private $factory;

    public function __construct(UserRepositoryInterface $repository, UserFactoryInterface $factory)
    {
        $this->repository = $repository;
        $this->factory = $factory;
    }

    public function handle(Register $request): User
    {
        /** @var User $user */
        $user = $this->factory->register($request->toForm());
        
        $this->repository->save($user);

        return $user;
    }
}
```

## File: `src/Application/UseCase/User/Request/GetUser.php`
```php
<?php

namespace Leos\Application\UseCase\User\Request;

use Leos\Domain\User\ValueObject\UserId;

/**
 * Class GetUser
 *
 * @package Leos\Application\UseCase\User\Request
 */
class GetUser
{
    /**
     * @var UserId
     */
    private $uuid;

    /**
     * GetUser constructor.
     * @param string $uuid
     */
    public function __construct(string $uuid)
    {

        $this->uuid = new UserId($uuid);
    }

    /**
     * @return UserId
     */
    public function uuid(): UserId
    {
        return $this->uuid;
    }
}
```

## File: `src/Application/UseCase/User/Request/Register.php`
```php
<?php

namespace Leos\Application\UseCase\User\Request;

use Leos\Domain\User\ValueObject\UserId;

/**
 * Class Register
 * 
 * @package Leos\Application\UseCase\User\Request
 */
class Register
{
    /**
     * @var string
     */
    private $username;
    
    /**
     * @var string
     */
    private $email;
    
    /**
     * @var string
     */
    private $plainPassword;

    /**
     * @var UserId
     */
    private $userId;

    public function __construct(UserId $userId, string $username, string $email, string $plainPassword)
    {
        $this->username = $username;
        $this->email = $email;
        $this->plainPassword = $plainPassword;
        $this->userId = $userId;
    }

    public function toForm(): array
    {
        return [
            'uuid'      => $this->userId,
            'username'  => $this->username,
            'email'     => $this->email,
            'password'  => $this->plainPassword
        ];
    }
}
```

## File: `src/Application/UseCase/Wallet/FindWalletHandler.php`
```php
<?php

namespace Leos\Application\UseCase\Wallet;

use Leos\Application\Request\Common\Pagination;

use Leos\Domain\Wallet\Repository\WalletRepositoryInterface;
use Pagerfanta\Pagerfanta;

/**
 * Class FindWalletHandler
 *
 * @package Leos\Domain\Wallet\UseCase
 */
final class FindWalletHandler
{
    /**
     * @var WalletRepositoryInterface
     */
    private $repository;

    /**
     * FindWalletHandler constructor.
     * @param WalletRepositoryInterface $repository
     */
    public function __construct(WalletRepositoryInterface $repository)
    {
        $this->repository = $repository;
    }

    /**
     * @param Pagination $request
     * @return Pagerfanta
     */
    public function handle(Pagination $request): Pagerfanta
    {
        return $this->repository->findAll(
            $request->getFilters(),
            $request->getOperators(),
            $request->getValues(),
            $request->getSort()
        );
    }
}
```

## File: `src/Application/UseCase/Wallet/GetWalletHandler.php`
```php
<?php

namespace Leos\Application\UseCase\Wallet;

use Leos\Application\UseCase\Wallet\Request\GetWallet;

use Leos\Domain\Wallet\Model\Wallet;
use Leos\Domain\Wallet\Repository\WalletRepositoryInterface;

/**
 * Class GetWalletHandler
 *
 * @package Leos\Domain\Wallet\UseCase
 */
final class GetWalletHandler
{
    /**
     * @var WalletRepositoryInterface
     */
    private $repository;

    public function __construct(WalletRepositoryInterface $repository)
    {
        $this->repository = $repository;
    }

    public function handle(GetWallet $request): Wallet
    {
        return $this->repository->get($request->uuid());
    }
}
```

## File: `src/Application/UseCase/Wallet/Request/Find.php`
```php
<?php

namespace Leos\Application\UseCase\Wallet\Request;

use Leos\Application\Request\Common\Pagination;

/**
 * Class Find
 *
 * @package Leos\Application\UseCase\Wallet\Request
 */
class Find extends Pagination
{

}
```

## File: `src/Application/UseCase/Wallet/Request/GetWallet.php`
```php
<?php

namespace Leos\Application\UseCase\Wallet\Request;

use Leos\Domain\Wallet\ValueObject\WalletId;

/**
 * Class GetWallet
 *
 * @package Leos\Application\UseCase\Wallet\Request
 */
class GetWallet
{
    /**
     * @var WalletId
     */
    private $uuid;

    /**
     * GetWallet constructor.
     * @param string $uuid
     */
    public function __construct(string $uuid)
    {
        $this->uuid = new WalletId($uuid);
    }

    /**
     * @return WalletId
     */
    public function uuid(): WalletId
    {
        return $this->uuid;
    }
}
```

## File: `src/Domain/Common/Event/AbstractEvent.php`
```php
<?php

namespace Leos\Domain\Common\Event;

abstract class AbstractEvent implements EventInterface
{
    /**
     * @var EventId
     */
    private $uuid;

    /**
     * @var string
     */
    private $type;

    /**
     * @var \DateTimeImmutable
     */
    private $createdAt;

    public function __construct()
    {
        $this->uuid = new EventId();

        $this->setType();
        $this->createdAt = new \DateTimeImmutable();
    }

    private function setType(): void
    {
        $path = explode('\\', get_class($this));

        $this->type = array_pop($path);
    }

    public function type(): string
    {
        return $this->type;
    }

    public function uuid(): EventId
    {
        return $this->uuid;
    }

    public function createdAt(): \DateTimeImmutable
    {
        return $this->createdAt;
    }
}
```

## File: `src/Domain/Common/Event/EventCollector.php`
```php
<?php

namespace Leos\Domain\Common\Event;

class EventCollector
{
    /**
     * @var static
     */
    private static $instance;

    /**
     * @var EventInterface[]
     */
    private $events = [];

    private function __construct()
    {
    }

    public static function instance(): self
    {
        if (null === self::$instance) {

            self::$instance = new self();
        }

        return self::$instance;
    }

    private function addEvent(EventInterface $event): void
    {
        self::instance()->events[] = $event;
    }

    public function collect(EventInterface $event): void
    {
        $this->addEvent($event);
    }

    public function flush(): void
    {
        self::instance()->events = [];

        reset(self::instance()->events);
    }

    /**
     * @return EventInterface[]
     */
    public function events(): array
    {
        return self::instance()->events;
    }

    public function remove(int $key): void
    {
        if (true === array_key_exists($key, self::instance()->events)) {

            unset(self::instance()->events[$key]);
        }
    }

    public function shutdown()
    {
        self::$instance = null;
    }
}
```

## File: `src/Domain/Common/Event/EventDispatcherInterface.php`
```php
<?php

namespace Leos\Domain\Common\Event;


interface EventDispatcherInterface
{
    public function record(EventInterface $event): void;

    public function dispatch(): void;
}
```

## File: `src/Domain/Common/Event/EventId.php`
```php
<?php

namespace Leos\Domain\Common\Event;

use Leos\Domain\Common\ValueObject\AggregateRootId;

class EventId extends AggregateRootId
{
}
```

## File: `src/Domain/Common/Event/EventInterface.php`
```php
<?php

namespace Leos\Domain\Common\Event;

interface EventInterface
{
    public function uuid(): EventId;

    public function type(): string;

    public function createdAt(): \DateTimeImmutable;
}
```

## File: `src/Domain/Common/Event/EventPublisher.php`
```php
<?php

namespace Leos\Domain\Common\Event;

final class EventPublisher
{
    /** @var self */
    private static $instance;

    /**
     * @var EventDispatcherInterface
     */
    private $dispatcher;

    private function __construct(EventDispatcherInterface $dispatcher)
    {
        $this->dispatcher = $dispatcher;
    }

    public static function boot(EventDispatcherInterface $dispatcher): void
    {
        if (!static::$instance) {

            static::$instance = new self($dispatcher);
        }
    }

    public static function raise(EventInterface $event): void
    {
        if (!static::$instance) {

            throw new \LogicException('EventPublisher needs to be booted before invoke raise.');
        }

        static::$instance->dispatcher->record($event);
    }
}
```

## File: `src/Domain/Common/Exception/InvalidUUIDException.php`
```php
<?php

namespace Leos\Domain\Common\Exception;

/**
 * Class InvalidUUIDException
 *
 * @package Leos\Domain\Common\Exception
 */
class InvalidUUIDException extends \InvalidArgumentException
{
    /**
     * InvalidUUIDException constructor.
     */
    public function __construct()
    {
        parent::__construct("aggregator_root.exception.invalid_uuid", 400);
    }
}
```

## File: `src/Domain/Common/Exception/NotFoundException.php`
```php
<?php

namespace Leos\Domain\Common\Exception;

/**
 * Class NotFoundException
 *
 * @package Domain\Common\Exception
 */
abstract class NotFoundException extends \Exception
{

}
```

## File: `src/Domain/Common/ValueObject/AggregateRoot.php`
```php
<?php

namespace Leos\Domain\Common\ValueObject;

use Leos\Domain\Common\Event\EventInterface;
use Leos\Domain\Common\Event\EventPublisher;

abstract class AggregateRoot
{
    /**
     * @var AggregateRootId
     */
    protected $uuid;

    protected function __construct(AggregateRootId $aggregateRootId)
    {
        $this->uuid = $aggregateRootId;
    }

    public function uuid(): AggregateRootId
    {
        return $this->uuid;
    }

    final public function equals(AggregateRootId $aggregateRootId)
    {
        return $this->uuid->equals($aggregateRootId);
    }

    final protected function raise(EventInterface $event): void
    {
        EventPublisher::raise($event);
    }

    public function __toString(): string
    {
        return (string) $this->uuid;
    }
}
```

## File: `src/Domain/Common/ValueObject/AggregateRootId.php`
```php
<?php

declare(strict_types=1);

namespace Leos\Domain\Common\ValueObject;

use Leos\Domain\Common\Exception\InvalidUUIDException;
use Ramsey\Uuid\Uuid;

/**
 * Class AggregateRootId
 *
 * Its the unique identifier and will be auto-generated if not value is set.
 *
 * @package Leos\Domain\Common\ValueObject
 */
abstract class AggregateRootId
{
    /**
     * @var string
     */
    protected $uuid;

    public function __construct(?string $id = null)
    {
        try {

            $this->uuid = Uuid::fromString($id ?: (string) Uuid::uuid4())->toString();

        } catch (\InvalidArgumentException $e) {

            throw new InvalidUUIDException();
        }
    }

    public function equals(AggregateRootId $aggregateRootId): bool
    {
        return $this->uuid === $aggregateRootId->__toString();
    }

    public function bytes(): string
    {
        return Uuid::fromString($this->uuid)->getBytes();
    }

    public static function fromBytes(string $bytes): self
    {
        return new static(Uuid::fromBytes($bytes)->toString());
    }

    public static function toBytes(string $uid): string
    {
        return (new static($uid))->bytes();
    }

    public function __toString(): string
    {
        return (string) $this->uuid;
    }
}
```

## File: `src/Domain/Money/Exception/CurrencyWrongCodeException.php`
```php
<?php

namespace Leos\Domain\Money\Exception;

/**
 * Class CurrencyWrongCodeException
 *
 * @package Leos\Domain\Money\Exception
 */
class CurrencyWrongCodeException extends \InvalidArgumentException
{
    /**
     * CreditNotEnoughException constructor.
     */
    public function __construct()
    {
        parent::__construct('currency.exception.wrong_code', 5001, null);
    }
}
```

## File: `src/Domain/Money/ValueObject/Currency.php`
```php
<?php

declare(strict_types=1);

namespace Leos\Domain\Money\ValueObject;

use Leos\Domain\Money\Exception\CurrencyWrongCodeException;

/**
 * Class Currency
 *
 * @package Leos\Domain\Money\ValueObject
 */
class Currency
{
    const DEFAULT = 'EUR';
    
    /**
     * @var string ISO code string
     */
    private $code;

    /**
     * @var float
     */
    private $exchange;

    public function __construct(string $code = 'EUR', float $exchange = 1.0)
    {
        $this->setCode($code);
        $this->exchange = $exchange;
    }

    public function equals(Currency $currency): bool
    {
        return ($currency->code() === $this->code && $currency->exchange() === $this->exchange);
    }

    private function setCode(string $code)
    {
        if (!preg_match('/^[A-Z]{3}$/', $code)) {

            throw new CurrencyWrongCodeException();
        }

        $this->code = $code;
    }

    public function code(): string
    {
        return $this->code;
    }

    public function exchange(): float
    {
        return $this->exchange;
    }
}
```

## File: `src/Domain/Money/ValueObject/Money.php`
```php
<?php

declare(strict_types=1);

namespace Leos\Domain\Money\ValueObject;

/**
 * Class Money
 *
 * @package Leos\Domain\Money\ValueObject
 */
class Money
{
    /**
     * @var float
     */
    private $amount;
    
    /**
     * @var Currency
     */
    private $currency;

    public function __construct(float $amount = 0.00, Currency $currency)
    {
        $this->amount = $amount;
        $this->currency = $currency;
    }

    public function amount(): float
    {
        return $this->amount;
    }

    public function currency(): Currency
    {
        return $this->currency;
    }
}
```

## File: `src/Domain/Payment/Exception/InvalidProviderException.php`
```php
<?php

namespace Leos\Domain\Payment\Exception;

/**
 * Class InvalidProviderException
 *
 * @package Leos\Domain\Payment\Exception
 */
class InvalidProviderException extends \InvalidArgumentException
{
    /**
     * InvalidProviderException constructor.
     */
    public function __construct()
    {
        parent::__construct('payment.exception.invalid_provider', 2200);
    }
}
```

## File: `src/Domain/Payment/Exception/MinDepositAmountException.php`
```php
<?php

namespace Leos\Domain\Payment\Exception;

/**
 * Class MinDepositAmountException
 *
 * @package Leos\Domain\Payment\Exception
 */
class MinDepositAmountException extends \InvalidArgumentException
{
    /**
     * MinDepositAmountException constructor.
     */
    public function __construct()
    {
        parent::__construct("deposit.exception.amount_must_be_higher_than_0", 77000);
    }
}
```

## File: `src/Domain/Payment/Exception/MinWithdrawalAmountException.php`
```php
<?php

namespace Leos\Domain\Payment\Exception;

/**
 * Class MinWithdrawalAmountException
 *
 * @package Leos\Domain\Payment\Exception
 */
class MinWithdrawalAmountException extends \InvalidArgumentException
{
    /**
     * MinDepositAmountException constructor.
     */
    public function __construct()
    {
        parent::__construct("withdrawal.exception.amount_must_be_higher_than_0", 87000);
    }
}
```

## File: `src/Domain/Payment/Model/Deposit.php`
```php
<?php

namespace Leos\Domain\Payment\Model;

use Leos\Domain\Transaction\ValueObject\TransactionState;
use Leos\Domain\Wallet\Model\Wallet;
use Leos\Domain\Money\ValueObject\Money;
use Leos\Domain\Payment\ValueObject\DepositDetails;
use Leos\Domain\Transaction\Model\AbstractTransaction;
use Leos\Domain\Transaction\ValueObject\TransactionType;

/**
 * Class Deposit
 *
 * @package Leos\Domain\Payment\Model
 */
class Deposit extends AbstractTransaction
{
    public function __construct(Wallet $wallet, Money $real, DepositDetails $details)
    {
        parent::__construct(TransactionType::DEPOSIT, $wallet, $real, new Money(0, $real->currency()));
        $this->setState(TransactionState::ACTIVE);
        $this->details = $details;
    }

    public static function create(Wallet $wallet, Money $real, DepositDetails $details): self
    {
        $deposit = new self($wallet, $real, $details);

        $deposit->raiseEvent();

        return $deposit;
    }

    public function rollback(): RollbackDeposit
    {
        $this->setState(TransactionState::REVERTED);

        return new RollbackDeposit($this);
    }

    public function details(): DepositDetails
    {
        return $this->details;
    }
}
```

## File: `src/Domain/Payment/Model/RollbackDeposit.php`
```php
<?php

namespace Leos\Domain\Payment\Model;

use Leos\Domain\Transaction\Model\AbstractTransaction;
use Leos\Domain\Transaction\ValueObject\TransactionState;
use Leos\Domain\Transaction\ValueObject\TransactionType;

/**
 * Class RollbackDeposit
 *
 * @package Leos\Domain\Payment\Model
 */
class RollbackDeposit extends AbstractTransaction
{
    public function __construct(Deposit $deposit)
    {
        parent::__construct(
            TransactionType::ROLLBACK_DEPOSIT,
            $deposit->wallet(),
            $deposit->realMoney(),
            $deposit->bonusMoney()
        );
        $this->setState(TransactionState::ACTIVE);
        $this->setReferralTransaction($deposit);
        $this->setDetails($deposit->details());
    }

    /**
     * @return mixed
     */
    public function details()
    {
        return $this->details;
    }
}
```

## File: `src/Domain/Payment/Model/RollbackWithdrawal.php`
```php
<?php

namespace Leos\Domain\Payment\Model;

use Leos\Domain\Transaction\Model\AbstractTransaction;
use Leos\Domain\Transaction\ValueObject\TransactionState;
use Leos\Domain\Transaction\ValueObject\TransactionType;

/**
 * Class RollbackWithdrawal
 *
 * @package Leos\Domain\Payment\Model
 */
class RollbackWithdrawal extends AbstractTransaction
{
    public function __construct(Withdrawal $withdrawal)
    {
        parent::__construct(
            TransactionType::ROLLBACK_WITHDRAWAL,
            $withdrawal->wallet(),
            $withdrawal->realMoney(),
            $withdrawal->bonusMoney()
        );

        $this->setState(TransactionState::ACTIVE);
        $this->setReferralTransaction($withdrawal);
        $this->setDetails($withdrawal->details());
    }

    /**
     * @return mixed
     */
    public function details()
    {
        return $this->details;
    }
}
```

## File: `src/Domain/Payment/Model/Withdrawal.php`
```php
<?php

namespace Leos\Domain\Payment\Model;

use Leos\Domain\Wallet\Model\Wallet;
use Leos\Domain\Money\ValueObject\Money;
use Leos\Domain\Transaction\Model\AbstractTransaction;
use Leos\Domain\Payment\ValueObject\WithdrawalDetails;
use Leos\Domain\Transaction\ValueObject\TransactionState;
use Leos\Domain\Transaction\ValueObject\TransactionType;

/**
 * Class Withdrawal
 *
 * @package Leos\Domain\Payment\Model
 */
class Withdrawal extends AbstractTransaction
{
    public function __construct(Wallet $wallet, Money $real, WithdrawalDetails $details)
    {
        parent::__construct(TransactionType::WITHDRAWAL, $wallet, $real, new Money(0, $real->currency()));
        $this->setState(TransactionState::ACTIVE);
        $this->details = $details;
    }

    public static function create(Wallet $wallet, Money $real, WithdrawalDetails $details): self
    {
        $withdrawal = new self($wallet, $real, $details);

        $withdrawal->raiseEvent();

        return $withdrawal;
    }

    public function rollback(): RollbackWithdrawal
    {
        $this->setState(TransactionState::REVERTED);

        return new RollbackWithdrawal($this);
    }

    /**
     * @return mixed
     */
    public function details()
    {
        return $this->details;
    }
}
```

## File: `src/Domain/Payment/ValueObject/DepositDetails.php`
```php
<?php

namespace Leos\Domain\Payment\ValueObject;

use Leos\Domain\Payment\Exception\InvalidProviderException;

/**
 * Class DepositDetails
 * 
 * @package Leos\Domain\Payment\ValueObject
 */
class DepositDetails
{
    /**
     * @var string
     */
    private $provider;

    public function __construct(string $provider)
    {
        $this->setProvider($provider);
    }

    private function setProvider(string $provider): void
    {
        if (strlen($provider) < 3) {
            
            throw new InvalidProviderException();
        }

        $this->provider = $provider;
    }

    public function provider(): string
    {
        return $this->provider;
    }
}
```

## File: `src/Domain/Payment/ValueObject/WithdrawalDetails.php`
```php
<?php

namespace Leos\Domain\Payment\ValueObject;
use Leos\Domain\Payment\Exception\InvalidProviderException;

/**
 * Class WithdrawalDetails
 * 
 * @package Leos\Domain\Payment\ValueObject
 */
class WithdrawalDetails
{
    /**
     * @var string
     */
    private $provider;

    public function __construct(string $provider)
    {
        $this->setProvider($provider);
    }

    private function setProvider(string $provider): void
    {
        if (strlen($provider) < 3) {

            throw new InvalidProviderException();
        }

        $this->provider = $provider;
    }

    public function provider(): string
    {
        return $this->provider;
    }
}
```

## File: `src/Domain/Security/Exception/AuthenticationException.php`
```php
<?php

namespace Leos\Domain\Security\Exception;

/**
 * Class AuthenticationException
 *
 * @package Leos\Domain\Security\Exception
 */
class AuthenticationException extends \Exception
{
    /**
     * AuthenticationException constructor.
     */
    public function __construct()
    {
        parent::__construct('security.exception.authentication_exception');
    }
}
```

## File: `src/Domain/Security/Exception/InvalidPasswordException.php`
```php
<?php

namespace Leos\Domain\Security\Exception;

/**
 * Class InvalidPasswordException
 *
 * @package Leos\Domain\Security\Exception
 */
class InvalidPasswordException extends \InvalidArgumentException
{
    /**
     * InvalidPasswordException constructor.
     */
    public function __construct()
    {
        parent::__construct("security.exception.invalid_password", 6005);
    }
}
```

## File: `src/Domain/Security/Exception/NullPasswordException.php`
```php
<?php

namespace Leos\Domain\Security\Exception;

/**
 * Class NullPasswordException
 *
 * @package Leos\Domain\Security\Exception
 */
class NullPasswordException extends \InvalidArgumentException
{
    /**
     * NullPasswordException constructor.
     */
    public function __construct()
    {
        parent::__construct("security.exception.null_password", 6006);
    }
}
```

## File: `src/Domain/Security/ValueObject/AuthUser.php`
```php
<?php

namespace Leos\Domain\Security\ValueObject;

use Leos\Domain\User\Exception\UserPasswordsAreNotEquals;

/**
 * Class AuthUser
 *
 * @package Leos\Domain\Security\Model
 */
final class AuthUser
{
    const DEFAULT_ROLES = [
        'ROLE_USER'
    ];

    /**
     * @var string
     */
    private $username;
    
    /**
     * @var string
     */
    private $passwordHash;

    /**
     * @var array
     */
    private $roles = [];

    public function __construct(string $username, EncodedPasswordInterface $encodedPassword, array $roles = [])
    {
        $this->username = $username;
        $this->passwordHash = (string) $encodedPassword;
        $this->roles = array_merge(self::DEFAULT_ROLES, $roles);
    }

    public function username(): string
    {
        return $this->username;
    }

    public function password(): string
    {
        return $this->passwordHash;
    }

    public function roles(): array
    {
        return $this->roles;
    }

    public function changePassword(EncodedPasswordInterface $oldPassword, EncodedPasswordInterface $newPassword): void
    {
        if (!$oldPassword->matchHash($this->passwordHash)) {

            throw new UserPasswordsAreNotEquals();
        }

        $this->passwordHash = (string) $newPassword;
    }
}
```

## File: `src/Domain/Security/ValueObject/EncodedPasswordInterface.php`
```php
<?php

namespace Leos\Domain\Security\ValueObject;

/**
 * Interface EncodedPasswordInterface
 *
 * @package Leos\Domain\Security\ValueObject
 */
interface EncodedPasswordInterface
{
    public function __construct(string $plainPassword);

    public function matchHash(string $hash): bool;

    public function __toString(): string;
}
```

## File: `src/Domain/Transaction/Event/TransactionWasCreated.php`
```php
<?php

namespace Leos\Domain\Transaction\Event;

use Leos\Domain\Common\Event\AbstractEvent;
use Leos\Domain\Common\ValueObject\AggregateRootId;
use Leos\Domain\Money\ValueObject\Currency;
use Leos\Domain\Wallet\ValueObject\WalletId;

class TransactionWasCreated extends AbstractEvent
{
    /**
     * @var string
     */
    private $transactionId;

    /**
     * @var string
     */
    private $walletId;

    /**
     * @var string
     */
    private $userId;

    /**
     * @var int
     */
    private $real;

    /**
     * @var int
     */
    private $bonus;

    /**
     * @var \DateTime
     */
    private $createdAt;

    /**
     * @var string
     */
    private $type;

    /**
     * @var string
     */
    private $currency;

    public function __construct(
        AggregateRootId $transactionId,
        string $type,
        WalletId $walletId,
        AggregateRootId $userId,
        int $real,
        int $bonus,
        Currency $currency,
        \DateTime $createdAt
    ) {
        parent::__construct();

        $this->transactionId = $transactionId->__toString();
        $this->type = $type;
        $this->walletId = $walletId->__toString();
        $this->userId = $userId->__toString();
        $this->real = $real;
        $this->bonus = $bonus;
        $this->createdAt = $createdAt;
        $this->currency = $currency->code();
    }
}
```

## File: `src/Domain/Transaction/Exception/InvalidTransactionStateException.php`
```php
<?php

namespace Leos\Domain\Transaction\Exception;

/**
 * Class InvalidTransactionStateException
 * 
 * @package Leos\Domain\Transaction\Exception
 */
class InvalidTransactionStateException extends \Exception
{
    /**
     * InvalidTransactionStateException constructor.
     */
    public function __construct()
    {
        parent::__construct("transaction.exception.invalid_state", 9007);
    }
}
```

## File: `src/Domain/Transaction/Exception/InvalidTransactionTypeException.php`
```php
<?php

namespace Leos\Domain\Transaction\Exception;

/**
 * Class InvalidTransactionTypeException
 * 
 * @package Leos\Domain\Transaction\Exception
 */
class InvalidTransactionTypeException extends \Exception
{
    /**
     * InvalidTransactionTypeException constructor.
     */
    public function __construct()
    {
        parent::__construct("transaction.exception.invalid_type", 9006);
    }
}
```

## File: `src/Domain/Transaction/Exception/TransactionNotFoundException.php`
```php
<?php

namespace Leos\Domain\Transaction\Exception;

use Leos\Domain\Common\Exception\NotFoundException;

/**
 * Class TransactionNotFoundException
 *
 * @package Leos\Domain\Transaction\Exception
 */
class TransactionNotFoundException extends NotFoundException
{

    /**
     * TransactionNotFoundException constructor.
     */
    public function __construct()
    {
        parent::__construct('transaction.exception.not_found', 6004);
    }
}
```

## File: `src/Domain/Transaction/Model/AbstractTransaction.php`
```php
<?php
declare(strict_types=1);

namespace Leos\Domain\Transaction\Model;

use Leos\Domain\Common\ValueObject\AggregateRoot;
use Leos\Domain\Transaction\Event\TransactionWasCreated;
use Leos\Domain\Wallet\Model\Wallet;
use Leos\Domain\Money\ValueObject\Money;
use Leos\Domain\Wallet\ValueObject\Credit;
use Leos\Domain\Money\ValueObject\Currency;
use Leos\Domain\Transaction\ValueObject\TransactionId;
use Leos\Domain\Transaction\ValueObject\TransactionType;
use Leos\Domain\Transaction\ValueObject\TransactionState;
use Leos\Domain\Transaction\Exception\InvalidTransactionStateException;

/**
 * Class Transaction
 *
 * @package Leos\Domain\Transaction\Model
 */
abstract class AbstractTransaction extends AggregateRoot
{
    /**
     * @var TransactionType
     */
    protected $type;

    /**
     * @var string
     */
    private $state = TransactionState::PENDING;

    /**
     * @var Credit
     */
    protected $prevReal;

    /**
     * @var Credit
     */
    protected $prevBonus;

    /**
     * @var int
     */
    protected $operationReal = 0;

    /**
     * @var int
     */
    protected $operationBonus = 0;

    /**
     * @var Wallet
     */
    protected $wallet;

    /**
     * @var Currency
     */
    protected $currency;

    /**
     * @var mixed
     */
    protected $details;

    /**
     * @var null|AbstractTransaction
     */
    protected $referralTransaction;

    /**
     * @var \DateTime
     */
    protected $createdAt;

    /**
     * @var null|\DateTime
     */
    protected $updatedAt;

    public function __construct(
        string $type,
        Wallet $wallet,
        Money $real,
        Money $bonus
    )
    {
        parent::__construct(new TransactionId());

        $this->type = new TransactionType($type);
        $this->wallet = $wallet;
        $this->prevReal = $wallet->real();
        $this->prevBonus = $wallet->bonus();
        $this->currency = $real->currency();
        $this->process($real, $bonus);
        $this->createdAt = new \DateTime();
    }

    protected function raiseEvent(): void
    {
        $this->raise(
            new TransactionWasCreated(
                $this->uuid(),
                $this->type()->__toString(),
                $this->wallet->walletId(),
                $this->wallet->user()->uuid(),
                $this->operationReal(),
                $this->operationBonus(),
                $this->currency(),
                $this->createdAt()
            )
        );
    }

    private function process(Money $real, Money $bonus): void
    {
        switch (true){

            case $this->type()->isDebit():

                $this->wallet
                    ->removeRealMoney($real)
                    ->removeBonusMoney($bonus)
                ;

                break;

            case $this->type()->isCredit():

                $this->wallet
                    ->addRealMoney($real)
                    ->addBonusMoney($bonus)
                ;

                break;
            case (string) $this->type() === TransactionType::CREATE_WALLET:

                break;

            default:
                throw new \LogicException('transaction.exception.unknown_type');
        }

        $this->operationReal = $this->wallet->real()->diff($this->prevReal);
        $this->operationBonus = $this->wallet->bonus()->diff($this->prevBonus);
    }

    public function realMoney(): Money
    {
        return (new Credit((int) abs($this->operationReal)))
            ->toMoney($this->currency());
    }

    public function bonusMoney(): Money
    {
        return (new Credit((int) abs($this->operationBonus)))
            ->toMoney($this->currency());
    }

    public function type(): TransactionType
    {
        return $this->type;
    }

    public function is(): string
    {
        return $this->state;
    }

    /**
     * @param string $newState
     *
     * @return AbstractTransaction
     *
     * @throws InvalidTransactionStateException
     */
    final protected function setState(string $newState): self
    {
        if (!TransactionState::can($this, $newState)) {

            throw new InvalidTransactionStateException();
        }

        $this->state = $newState;

        return $this;
    }

    public function operationReal(): int
    {
        return $this->operationReal;
    }

    public function operationBonus(): int
    {
        return $this->operationBonus;
    }

    public function prevReal(): Credit
    {
        return $this->prevReal;
    }

    public function prevBonus(): Credit
    {
        return $this->prevBonus;
    }

    public function wallet(): Wallet
    {
        return $this->wallet;
    }

    public function currency(): Currency
    {
        return $this->currency;
    }

    public function createdAt(): \DateTime
    {
        return $this->createdAt;
    }

    public function updatedAt(): ?\DateTime
    {
        return $this->updatedAt;
    }

    /**
     * @return mixed
     */
    public abstract function details();

    /**
     * @param mixed $details
     * 
     * @return AbstractTransaction
     */
    public function setDetails($details): self
    {
        $this->details = $details;

        return $this;
    }

    public function referralTransaction(): ?AbstractTransaction
    {
        return $this->referralTransaction;
    }

    protected function setReferralTransaction(AbstractTransaction $referralTransaction): self
    {
        $this->referralTransaction = $referralTransaction;

        return $this;
    }

    public function rollback()
    {
        // Implement when need it
    }
}
```

## File: `src/Domain/Transaction/Repository/TransactionRepositoryInterface.php`
```php
<?php

namespace Leos\Domain\Transaction\Repository;

use Leos\Domain\Transaction\Model\AbstractTransaction;
use Leos\Domain\Transaction\ValueObject\TransactionId;
use Leos\Domain\Transaction\Exception\TransactionNotFoundException;

/**
 * Interface TransactionRepository
 *
 * @package Leos\Domain\Transaction\Repository
 */
interface TransactionRepositoryInterface
{

    /**
     * @param TransactionId $transactionId
     *
     * @return AbstractTransaction
     *
     * @throws TransactionNotFoundException
     */
    public function get(TransactionId $transactionId): AbstractTransaction;

    public function save(AbstractTransaction $transaction): void;
}
```

## File: `src/Domain/Transaction/ValueObject/TransactionId.php`
```php
<?php

namespace Leos\Domain\Transaction\ValueObject;

use Leos\Domain\Common\ValueObject\AggregateRootId;

/**
 * Class TransactionId
 *
 * @package Leos\Domain\Transaction\ValueObject
 */
class TransactionId extends AggregateRootId
{

}
```

## File: `src/Domain/Transaction/ValueObject/TransactionState.php`
```php
<?php

namespace Leos\Domain\Transaction\ValueObject;

use Leos\Domain\Transaction\Model\AbstractTransaction;

/**
 * Class TransactionState
 *
 * @package Leos\Domain\Transaction\ValueObject
 */
class TransactionState
{
    const
        ACTIVE = 'active',
        PENDING = 'pending',
        REVERTED = 'reverted'
    ;

    public static function can(AbstractTransaction $transaction, string $new): bool
    {
        $can = false;

        $current = $transaction->is();
        $type = (string) $transaction->type();

        switch ($new) {

            case self::ACTIVE:
                $can = self::canActivate($current);
                break;
            case self::PENDING:

                $can = self::canWait($current, $type);
                break;
            case self::REVERTED:
                $can = self::canRevert($current, $type);
                break;
        }

        return $can;
    }

    private static function canActivate(string $state): bool
    {
        return $state !== static::REVERTED;
    }

    private static function canRevert(string $state, string $type): bool
    {
        return $state === static::ACTIVE && !in_array($type, [
            TransactionType::ROLLBACK_DEPOSIT,
            TransactionType::ROLLBACK_WITHDRAWAL
        ]);
    }

    private static function canWait(string $state, string $type): bool
    {
        return $state === static::ACTIVE && !in_array($type, [
            TransactionType::ROLLBACK_DEPOSIT,
            TransactionType::ROLLBACK_WITHDRAWAL
        ]);
    }
}
```

## File: `src/Domain/Transaction/ValueObject/TransactionType.php`
```php
<?php

namespace Leos\Domain\Transaction\ValueObject;

use Leos\Domain\Transaction\Exception\InvalidTransactionTypeException;

/**
 * Class TransactionType
 *
 * @package Leos\Domain\Transaction\Model
 */
class TransactionType
{
    const
        CREATE_WALLET = 'create_wallet',
        DEPOSIT = 'deposit',
        WITHDRAWAL = 'withdrawal',
        ROLLBACK_DEPOSIT = 'rollback_deposit',
        ROLLBACK_WITHDRAWAL = 'rollback_withdrawal'
    ;

    /**
     * @var string
     */
    private $type;

    public function __construct(string $type)
    {
        $this->setType($type);
    }

    /**
     * @param string $type
     *
     * @throws InvalidTransactionTypeException
     */
    private function setType(string $type): void
    {
        if (!self::isValid($type)) {

            throw new InvalidTransactionTypeException();
        }

        $this->type = $type;
    }

    public static function types(): array
    {
        return [
            self::CREATE_WALLET,
            self::DEPOSIT,
            self::ROLLBACK_DEPOSIT,
            self::WITHDRAWAL,
            self::ROLLBACK_WITHDRAWAL
        ];
    }

    public function isCredit(): bool
    {
        return in_array($this->type, [
            self::DEPOSIT,
            self::ROLLBACK_WITHDRAWAL
        ]);
    }

    public function isDebit(): bool
    {
        return in_array($this->type, [
            self::ROLLBACK_DEPOSIT,
            self::WITHDRAWAL
        ]);
    }

    public static function isValid(string $type): bool
    {
        return in_array($type, self::types());
    }

    public function __toString(): string
    {
        return (string) $this->type;
    }
}
```

## File: `src/Domain/User/Event/UserPasswordWasChanged.php`
```php
<?php

namespace Leos\Domain\User\Event;

use Leos\Domain\Common\Event\AbstractEvent;
use Leos\Domain\User\ValueObject\UserId;

class UserPasswordWasChanged extends AbstractEvent
{
    /**
     * @var string
     */
    private $userId;

    public function __construct(UserId $userId)
    {
        parent::__construct();
        $this->userId = (string) $userId;
    }

    public function getUserId(): string
    {
        return $this->userId;
    }
}
```

## File: `src/Domain/User/Event/UserWasCreated.php`
```php
<?php

namespace Leos\Domain\User\Event;

use Leos\Domain\Common\Event\AbstractEvent;
use Leos\Domain\User\ValueObject\UserId;

class UserWasCreated extends AbstractEvent
{
    /**
     * @var string
     */
    private $userId;

    /**
     * @var string
     */
    private $username;

    /**
     * @var string
     */
    private $email;

    public function __construct(UserId $userId, string $username, string $email)
    {
        parent::__construct();
        $this->userId = (string) $userId;
        $this->username = $username;
        $this->email = $email;
    }

    public function userId(): string
    {
        return $this->userId;
    }

    public function username(): string
    {
        return $this->username;
    }

    public function email(): string
    {
        return $this->email;
    }
}
```

## File: `src/Domain/User/Event/Handler/OnUserWasCreated.php`
```php
<?php

namespace Leos\Domain\User\Event\Handler;

use Leos\Infrastructure\CommonBundle\Event\EventAware;

class OnUserWasCreated
{

    public function __invoke(EventAware $eventAware): void
    {
        // I.E send welcome email
    }
}
```

## File: `src/Domain/User/Exception/UserNotFoundException.php`
```php
<?php

namespace Leos\Domain\User\Exception;

use Leos\Domain\Common\Exception\NotFoundException;

/**
 * Class UserNotFoundException
 *
 * @package Leos\Domain\User\Exception
 */
class UserNotFoundException extends NotFoundException
{
    /**
     * UserNotFoundException constructor.
     */
    public function __construct()
    {
        parent::__construct("user.exception.not_found", 2004);
    }
}
```

## File: `src/Domain/User/Exception/UserPasswordsAreNotEquals.php`
```php
<?php

namespace Leos\Domain\User\Exception;

class UserPasswordsAreNotEquals extends \InvalidArgumentException
{
    public function __construct()
    {
        parent::__construct('user.password.not.equals');
    }
}
```

## File: `src/Domain/User/Factory/UserFactoryInterface.php`
```php
<?php

namespace Leos\Domain\User\Factory;

use Leos\Domain\User\Model\User;

/**
 * Interface UserFactoryInterface
 *
 * @package Leos\Domain\User\Factory
 */
interface UserFactoryInterface
{
    public function register(array $data): User;
}
```

## File: `src/Domain/User/Model/User.php`
```php
<?php

namespace Leos\Domain\User\Model;

use Doctrine\Common\Collections\ArrayCollection;

use Leos\Domain\Common\ValueObject\AggregateRoot;
use Leos\Domain\User\Event\UserPasswordWasChanged;
use Leos\Domain\User\Event\UserWasCreated;
use Leos\Domain\Wallet\Model\Wallet;
use Leos\Domain\User\ValueObject\UserId;
use Leos\Domain\Security\ValueObject\AuthUser;
use Leos\Domain\Security\ValueObject\EncodedPasswordInterface;

/**
 * Class User
 *
 * @package Leos\Domain\User\Model
 */
class User extends AggregateRoot
{
    /**
     * @var UserId
     */
    protected $uuid;

    /**
     * @var string
     */
    private $email;

    /**
     * @var AuthUser
     */
    private $auth;

    /**
     * @var Wallet[]|ArrayCollection
     */
    private $wallets;

    /**
     * @var \DateTime
     */
    private $createdAt;

    /**
     * @var null|\DateTime
     */
    private $updatedAt;

    public function __construct(
        UserId $userId,
        string $username,
        string $email,
        EncodedPasswordInterface $encodedPassword
    ) {
        parent::__construct($userId);

        $this->auth = new AuthUser($username, $encodedPassword);
        $this->setEmail($email);
        $this->wallets = new ArrayCollection();
        $this->createdAt = new \DateTime();
    }

    public static function create(
        UserId $userId,
        string $username,
        string $email,
        EncodedPasswordInterface $encodedPassword
    ): User {

        $user = new self($userId, $username, $email, $encodedPassword);

        $user->raise(
            new UserWasCreated($userId, $username, $email)
        );

        return $user;
    }

    public function changePassword(EncodedPasswordInterface $oldPassword, EncodedPasswordInterface $newPassword)
    {
        $this->auth->changePassword($oldPassword, $newPassword);

        $this->raise(
            new UserPasswordWasChanged($this->uuid)
        );
    }

    private function setEmail(string $email)
    {
        if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {

            throw new \InvalidArgumentException("Invalid email $email");
        }

        $this->email = $email;
    }

    public function email(): string
    {
        return $this->email;
    }

    public function username(): string
    {
        return $this->auth->username();
    }

    public function auth(): AuthUser
    {
        return $this->auth;
    }

    public function createdAt(): \DateTime
    {
        return $this->createdAt;
    }

    public function updatedAt(): ?\DateTime
    {
        return $this->updatedAt;
    }

    public function realBalance(): int
    {
        $total = 0;

        foreach ($this->wallets as $wallet) {

            $total += $wallet->real()->amount();
        }

        return $total;
    }

    public function bonusBalance(): int
    {
        $total = 0;

        foreach ($this->wallets as $wallet) {

            $total += $wallet->bonus()->amount();
        }

        return $total;
    }
}
```

## File: `src/Domain/User/Repository/UserRepositoryInterface.php`
```php
<?php

namespace Leos\Domain\User\Repository;

use Leos\Domain\User\Model\User;
use Leos\Domain\User\ValueObject\UserId;

/**
 * Interface UserRepositoryInterface
 *
 * @package Leos\Domain\User\Repository
 */
interface UserRepositoryInterface
{
    public function getOneByUuid(UserId $userId): User;

    public function findOneByUuid(UserId $userId): ?User;

    public function findOneByUsername(string $username): ?User;

    public function save(User $user): void;
}
```

## File: `src/Domain/User/ValueObject/UserId.php`
```php
<?php

namespace Leos\Domain\User\ValueObject;

use Leos\Domain\Common\ValueObject\AggregateRootId;

/**
 * Class UserId
 *
 * @package Leos\Domain\User\ValueObject
 */
class UserId extends AggregateRootId
{
    /** @var  string */
    protected $uuid;
}
```

## File: `src/Domain/Wallet/Exception/Credit/CreditNotEnoughException.php`
```php
<?php

namespace Leos\Domain\Wallet\Exception\Credit;

/**
 * Class CreditNotEnoughException
 *
 * @package Domain\Wallet\Exception\Credit
 */
class CreditNotEnoughException extends \Exception
{
    /**
     * CreditNotEnoughException constructor.
     */
    public function __construct()
    {
        parent::__construct('credit.exception.not_enough_founds', 4001);
    }
}
```

## File: `src/Domain/Wallet/Exception/Wallet/WalletNotFoundException.php`
```php
<?php

namespace Leos\Domain\Wallet\Exception\Wallet;

use Leos\Domain\Common\Exception\NotFoundException;

/**
 * Class WalletNotFoundException
 * 
 * @package Leos\Domain\Wallet\Exception\Wallet
 */
class WalletNotFoundException extends NotFoundException
{
    /**
     * WalletNotFoundException constructor.
     */
    public function __construct()
    {
        parent::__construct('wallet.exception.not_found', 8004);
    }
}
```

## File: `src/Domain/Wallet/Factory/WalletFactory.php`
```php
<?php

namespace Leos\Domain\Wallet\Factory;

use Leos\Domain\User\Model\User;
use Leos\Domain\Wallet\Model\Wallet;
use Leos\Domain\Money\ValueObject\Money;
use Leos\Domain\Money\ValueObject\Currency;
use Leos\Domain\Transaction\Model\AbstractTransaction;
use Leos\Domain\Transaction\ValueObject\TransactionType;

/**
 * Class WalletFactory
 *
 * @package Leos\Domain\Wallet\Factory
 */
class WalletFactory extends AbstractTransaction
{
    public function __construct(User $user, Currency $currency)
    {
        parent::__construct(TransactionType::CREATE_WALLET, new Wallet($user), new Money(0, $currency), new Money(0, $currency));
    }

    public static function create(User $user, Currency $currency): self
    {
        $transaction = new self($user, $currency);

        $transaction->raiseEvent();

        return $transaction;
    }

    /**
     * @return mixed
     */
    public function details()
    {
        return $this->details;
    }
}
```

## File: `src/Domain/Wallet/Model/Wallet.php`
```php
<?php

declare(strict_types=1);

namespace Leos\Domain\Wallet\Model;

use Leos\Domain\Money\ValueObject\Money;
use Leos\Domain\User\Model\User;
use Leos\Domain\Wallet\ValueObject\Credit;
use Leos\Domain\Wallet\ValueObject\WalletId;

/**
 * Class Wallet
 * 
 * @package Domain\Wallet\Model
 */
class Wallet
{
    /**
     * @var WalletId
     */
    private $id;

    /**
     * @var User
     */
    private $user;

    /**
     * @var Credit
     */
    private $real;

    /**
     * @var Credit
     */
    private $bonus;

    /**
     * @var \DateTime
     */
    private $createdAt;

    /**
     * @var null|\DateTime
     */
    private $updatedAt;

    public function __construct(User $user)
    {
        $this->id = new WalletId();
        $this->user = $user;
        $this->real = new Credit(0);
        $this->bonus = new Credit(0);
        $this->createdAt = new \DateTime();
    }

    public function addRealMoney(Money $money): self
    {
        $this->real = $this->real->add($money);

        return $this;
    }

    public function removeRealMoney(Money $money): self
    {
        $this->real = $this->real->remove($money);

        return $this;
    }

    public function addBonusMoney(Money $money): self
    {
        $this->bonus = $this->bonus->add($money);

        return $this;
    }

    public function removeBonusMoney(Money $money): self
    {
        $this->bonus = $this->bonus->remove($money);

        return $this;
    }

    public function id(): string
    {
        return $this->id->__toString();
    }

    public function walletId(): WalletId
    {
        return $this->id;
    }

    public function user(): User
    {
        return $this->user;
    }

    public function real(): Credit
    {
        return $this->real;
    }

    public function bonus(): Credit
    {
        return $this->bonus;
    }

    public function createdAt(): \DateTime
    {
        return $this->createdAt;
    }

    public function updatedAt(): ?\DateTime
    {
        return $this->updatedAt;
    }
}
```

## File: `src/Domain/Wallet/Repository/WalletRepositoryInterface.php`
```php
<?php

namespace Leos\Domain\Wallet\Repository;

use Leos\Domain\Wallet\Model\Wallet;
use Leos\Domain\Wallet\ValueObject\WalletId;
use Leos\Domain\Wallet\Exception\Wallet\WalletNotFoundException;

/**
 * Interface WalletRepositoryInterface
 *
 * @package Leos\Domain\Wallet\Repository
 */
interface WalletRepositoryInterface
{
    /**
     * @param array $keys
     * @param array $operators
     * @param array $values
     * @param array $sort
     *
     * @return Wallet[]|\Pagerfanta\Pagerfanta
     */
    public function findAll(array $keys = [], array $operators = [], array $values = [], array $sort = []);

    /**
     * @param WalletId $uid
     *
     * @throws WalletNotFoundException
     *
     * @return Wallet
     */
    public function get(WalletId $uid): Wallet;

    public function findOneById(WalletId $uid): ?Wallet;

}
```

## File: `src/Domain/Wallet/ValueObject/Credit.php`
```php
<?php

declare(strict_types=1);

namespace Leos\Domain\Wallet\ValueObject;

use Leos\Domain\Money\ValueObject\Currency;
use Leos\Domain\Money\ValueObject\Money;
use Leos\Domain\Wallet\Exception\Credit\CreditNotEnoughException;

/**
 * Class Credit
 *
 * @package Domain\Wallet\Model
 */
final class Credit
{
    /**
     * @var int
     */
    private $amount;

    /**
     * @var \DateTime
     */
    private $generatedAt;

    public function __construct(int $amount)
    {
        $this->amount = $amount;
        $this->generatedAt = new \DateTime();
    }

    public static function moneyToCredit(Money $money): self
    {
        return new self(intval($money->amount() * 100));
    }

    public function toMoney(Currency $currency): Money
    {
        return new Money(floatval($this->amount() / 100), $currency);
    }

    public function add(Money $money): self
    {
        return new self($this->amount + self::moneyToCredit($money)->amount());
    }

    public function remove(Money $money): self
    {
        if ($this->amount < self::moneyToCredit($money)->amount()) {

            throw new CreditNotEnoughException();
        }

        return new self($this->amount - self::moneyToCredit($money)->amount());
    }

    public function equals(Credit $credit): bool
    {
        return ($this->amount === $credit->amount());
    }

    public function amount(): int
    {
        return $this->amount;
    }

    public function diff(Credit $credit): int
    {
        return $this->amount - $credit->amount();
    }

    public function generatedAt(): \DateTime
    {
        return $this->generatedAt;
    }

    public function __toString(): string
    {
        return (string) $this->amount;
    }
}
```

## File: `src/Domain/Wallet/ValueObject/WalletId.php`
```php
<?php

namespace Leos\Domain\Wallet\ValueObject;

use Leos\Domain\Common\ValueObject\AggregateRootId;

/**
 * Class WalletId
 * @package Leos\Domain\Wallet\ValueObject
 */
class WalletId extends AggregateRootId
{
    /**
     * @var string
     */
    protected $uuid;
}
```

## File: `src/Infrastructure/CommonBundle/LeosInfrastructureCommonBundle.php`
```php
<?php

namespace Leos\Infrastructure\CommonBundle;

use Doctrine\DBAL\Types\Type;
use Leos\Infrastructure\CommonBundle\Doctrine\Types\JsonDocumentType;
use Leos\Infrastructure\CommonBundle\Event\EventAware;
use Symfony\Component\HttpKernel\Bundle\Bundle;

class LeosInfrastructureCommonBundle extends Bundle
{
    public function boot()
    {
        parent::boot();

        // Initialize Event Publisher
        $this->container->get('Leos\Domain\Common\Event\EventDispatcherInterface');

        $this->addDBALType('event', EventAware::class);
    }

    /**
     * @param string $type
     * @param string $object
     *
     * @throws \Doctrine\DBAL\DBALException
     */
    private function addDBALType(string $type, string $object): void
    {
        if (!Type::hasType($type)) {

            Type::addType($type, JsonDocumentType::class);

            /** @var JsonDocumentType $type */
            $type = Type::getType($type);

            $type->setSerializer(
                $this->container->get('jms_serializer')
            );

            $type->setType($object);
        }
    }
}
```

## File: `src/Infrastructure/CommonBundle/Bus/Middleware/EventDispatcherMiddleware.php`
```php
<?php

namespace Leos\Infrastructure\CommonBundle\Bus\Middleware;

use League\Tactician\Middleware;
use Leos\Domain\Common\Event\EventDispatcherInterface;

class EventDispatcherMiddleware implements Middleware
{

    /**
     * @var EventDispatcherInterface
     */
    private $eventDispatcher;

    public function __construct(EventDispatcherInterface $eventDispatcher)
    {
        $this->eventDispatcher = $eventDispatcher;
    }

    public function execute($command, callable $next)
    {
        $returnValue = $next($command);

        $this->eventDispatcher->dispatch();

        return $returnValue;
    }
}
```

## File: `src/Infrastructure/CommonBundle/Bus/Middleware/EventPublisherMiddleware.php`
```php
<?php

namespace Leos\Infrastructure\CommonBundle\Bus\Middleware;

use JMS\Serializer\SerializerInterface;
use League\Tactician\Middleware;
use Leos\Domain\Common\Event\EventCollector;
use Leos\Infrastructure\CommonBundle\Event\EventAware;

use OldSound\RabbitMqBundle\RabbitMq\Producer;

class EventPublisherMiddleware implements Middleware
{
    /**
     * @var Producer
     */
    private $producer;

    /**
     * @var EventCollector
     */
    private $eventCollector;

    /**
     * @var SerializerInterface
     */
    private $serializer;

    public function __construct(Producer $producer, EventCollector $eventCollector, SerializerInterface $serializer)
    {
        $this->producer = $producer;
        $this->producer
            ->setContentType('application/json');
        $this->eventCollector = $eventCollector;
        $this->serializer = $serializer;
    }

    public function execute($command, callable $next)
    {
        $returnValue = $next($command);

        $events = $this->eventCollector->events();

        foreach ($events as $event) {

            $serializedEvent = $this->serializer->serialize($event, 'json');

            $this->producer->publish($serializedEvent, $event->type());
        }

        return $returnValue;
    }
}
```

## File: `src/Infrastructure/CommonBundle/Bus/Middleware/EventStoreMiddleware.php`
```php
<?php

namespace Leos\Infrastructure\CommonBundle\Bus\Middleware;

use League\Tactician\Middleware;
use Leos\Domain\Common\Event\EventCollector;
use Leos\Infrastructure\CommonBundle\Event\EventAware;
use Leos\Infrastructure\CommonBundle\Repository\EventStoreRepository;

class EventStoreMiddleware implements Middleware
{
    /**
     * @var EventStoreRepository
     */
    private $eventStoreRepository;

    /**
     * @var EventCollector
     */
    private $eventCollector;

    public function __construct(EventStoreRepository $eventStoreRepository, EventCollector $eventCollector)
    {
        $this->eventStoreRepository = $eventStoreRepository;
        $this->eventCollector = $eventCollector;
    }

    public function execute($command, callable $next)
    {
        $returnValue = $next($command);

        $events = $this->eventCollector->events();

        foreach ($events as $event) {

            $symfonyEvent = new EventAware($event);
            $this->eventStoreRepository->store($symfonyEvent);
        }

        return $returnValue;
    }
}
```

## File: `src/Infrastructure/CommonBundle/DependencyInjection/LeosInfrastructureCommonExtension.php`
```php
<?php

namespace Leos\Infrastructure\CommonBundle\DependencyInjection;

use Symfony\Component\DependencyInjection\ContainerBuilder;
use Symfony\Component\Config\FileLocator;
use Symfony\Component\HttpKernel\DependencyInjection\Extension;
use Symfony\Component\DependencyInjection\Loader;

/**
 * This is the class that loads and manages your bundle configuration.
 *
 * @link http://symfony.com/doc/current/cookbook/bundles/extension.html
 */
class LeosInfrastructureCommonExtension extends Extension
{
    /**
     * {@inheritdoc}
     */
    public function load(array $configs, ContainerBuilder $container)
    {
        $loader = new Loader\YamlFileLoader($container, new FileLocator(__DIR__.'/../Resources/config'));
        $loader->load('services.yml');
    }
}
```

## File: `src/Infrastructure/CommonBundle/Doctrine/ORM/Repository/EntityRepository.php`
```php
<?php
namespace Leos\Infrastructure\CommonBundle\Doctrine\ORM\Repository;

use Doctrine\ORM\EntityRepository as BaseEntityRepository;

use Doctrine\ORM\QueryBuilder;
use Pagerfanta\Pagerfanta;
use Pagerfanta\Adapter\ArrayAdapter;
use Pagerfanta\Adapter\DoctrineORMAdapter;

/**
 * Class EntityRepository
 * 
 * @package Leos\Infrastructure\CommonBundle\Doctrine\ORM\Repository
 */
class EntityRepository extends BaseEntityRepository
{

    const OPERATOR_GT = "gt";
    const OPERATOR_LT = "lt";
    const OPERATOR_EQ = "eq";
    const OPERATOR_LTE = "lte";
    const OPERATOR_GTE = "gte" ;
    const OPERATOR_LIKE = "like" ;
    const OPERATOR_BETWEEN = "between";

    /**
     * @param QueryBuilder $queryBuilder
     * @param string $alias
     * @param array $keys
     * @param array $operators
     * @param array $values
     * @param array $sorting
     *
     * @return Pagerfanta
     */
    public function createOperatorPaginator(
        QueryBuilder $queryBuilder,
        string $alias,
        array $keys = [],
        array $operators = [],
        array $values = [],
        array $sorting = []
    ): Pagerfanta
    {

        $this->applyCriteriaOperator($alias, $queryBuilder, $keys, $operators, $values);
        $this->applySorting($alias, $queryBuilder, $sorting);

        return $this->getPaginator($queryBuilder);
    }

    /**
     * @param QueryBuilder $queryBuilder
     *
     * @return Pagerfanta
     */
    protected function getPaginator(QueryBuilder $queryBuilder): Pagerfanta
    {
        return new Pagerfanta(new DoctrineORMAdapter($queryBuilder, true, false));
    }

    /**
     * @param array $objects
     *
     * @return Pagerfanta
     */
    protected function getArrayPaginator($objects): Pagerfanta
    {
        return new Pagerfanta(new ArrayAdapter($objects));
    }

    /**
     * @param string $alias
     * @param QueryBuilder $queryBuilder
     * @param array $keys
     * @param array $operators
     * @param array $values
     *
     * @return QueryBuilder
     */
    protected function applyCriteriaOperator(
        string $alias,
        QueryBuilder $queryBuilder,
        array $keys = [],
        array $operators = [],
        array $values = []
    ): QueryBuilder
    {
        foreach ($keys as $position => $value) {

            if (null === $value) continue;

            $name = $this->getPropertyName($alias, $value);
            $parameter = ':' . str_replace('.', '_', $value) . $position;

            $operation = $operators[$position];
            $parameterValue = $values[$position];


            switch ($operation) {

                case static::OPERATOR_GT:
                    $queryBuilder->andWhere($queryBuilder->expr()->gt($name, $parameter));
                    break;

                case static::OPERATOR_LT:
                    $queryBuilder->andWhere($queryBuilder->expr()->lt($name, $parameter));
                    break;

                case static::OPERATOR_GTE:
                    $queryBuilder->andWhere($queryBuilder->expr()->gte($name, $parameter));
                    break;

                case static::OPERATOR_LTE:
                    $queryBuilder->andWhere($queryBuilder->expr()->lte($name, $parameter));
                    break;

                case static::OPERATOR_LIKE:
                    $queryBuilder->andWhere($queryBuilder->expr()->like($name, $parameter));
                    $parameterValue = "%" . $parameterValue . "%";
                    break;

                case static::OPERATOR_BETWEEN:
                    $queryBuilder->andWhere($queryBuilder->expr()->between($name, $values[0], $values[1]));
                    break;

                case static::OPERATOR_EQ:

                default:
                    if (null === $parameterValue) {

                        $queryBuilder->andWhere($queryBuilder->expr()->isNull($parameter));

                    } elseif (is_array($parameterValue)) {

                        $queryBuilder->andWhere($queryBuilder->expr()->in($name, $parameter));

                    } elseif ('' !== $parameterValue) {

                        $queryBuilder->andWhere($queryBuilder->expr()->eq($name, $parameter));
                    }
            }

            $queryBuilder->setParameter($parameter, $parameterValue);
        }

        return $queryBuilder;
    }

    /**
     * @param string $alias
     * @param QueryBuilder $queryBuilder
     * @param array $sorting
     *
     * @return QueryBuilder
     */
    protected function applySorting(string $alias, QueryBuilder $queryBuilder, array $sorting = []): QueryBuilder
    {
        foreach ($sorting as $property => $order) {
            if (!empty($order) ) {
                $queryBuilder->addOrderBy($this->getPropertyName($alias, $property), $order);
            }
        }

        return $queryBuilder;
    }

    /**
     * @param string $alias
     * @param string $name
     *
     * @return string
     */
    protected function getPropertyName(string $alias, string $name): string
    {
        return (false === $this->startsWith($name, $alias)) ? $alias.'.'.$name : $name;
    }

    /**
     * @param string $haystack
     * @param string $needle
     *
     * @return bool
     */
    private function startsWith(string $haystack, string $needle): bool
    {
        return $needle === "" || strrpos($haystack, $needle, -strlen($haystack)) !== false;
    }
}

```

## File: `src/Infrastructure/CommonBundle/Doctrine/Types/EventAwareIdType.php`
```php
<?php

namespace Leos\Infrastructure\CommonBundle\Doctrine\Types;

use Doctrine\DBAL\Platforms\AbstractPlatform;
use Leos\Infrastructure\CommonBundle\Event\EventAwareId;
use Ramsey\Uuid\Doctrine\UuidBinaryType;

class EventAwareIdType extends UuidBinaryType
{
    const NAME = 'eventAwareId';

    public function convertToPHPValue($value, AbstractPlatform $platform)
    {
        return (null === $value) ? null : EventAwareId::fromBytes($value);
    }

    /**
     * @param EventAwareId $value
     * @param AbstractPlatform $platform
     * @return null
     */
    public function convertToDatabaseValue($value, AbstractPlatform $platform)
    {
        return  (null === $value) ? null : $value->bytes();
    }

    public function getName()
    {
        return self::NAME;
    }
}
```

## File: `src/Infrastructure/CommonBundle/Doctrine/Types/EventType.php`
```php
<?php

namespace Leos\Infrastructure\CommonBundle\Doctrine\Types;

use Doctrine\DBAL\Platforms\AbstractPlatform;
use Leos\Infrastructure\CommonBundle\Event\EventAwareId;
use Ramsey\Uuid\Doctrine\UuidBinaryType;

class EventType extends UuidBinaryType
{
    const NAME = 'event';

    /**
     * @param null|string $value
     * @param AbstractPlatform $platform
     * @return \Leos\Domain\Common\ValueObject\AggregateRootId|null
     */
    public function convertToPHPValue($value, AbstractPlatform $platform)
    {
        return (null === $value) ? null : EventAwareId::fromBytes($value);
    }

    /**
     * @param EventAwareId $value
     * @param AbstractPlatform $platform
     * @return null
     */
    public function convertToDatabaseValue($value, AbstractPlatform $platform)
    {
        return  (null === $value) ? null : $value->bytes();
    }

    public function getName()
    {
        return self::NAME;
    }
}
```

## File: `src/Infrastructure/CommonBundle/Doctrine/Types/JsonDocumentType.php`
```php
<?php

namespace Leos\Infrastructure\CommonBundle\Doctrine\Types;

use Doctrine\DBAL\Types\Type;
use JMS\Serializer\Serializer;

use Doctrine\DBAL\Platforms\AbstractPlatform;

/**
 * Class JsonDocumentType
 *
 * @package Leos\Infrastructure\CommonBundle\Doctrine\Types
 */
class JsonDocumentType extends Type
{
    /**
     * @var string
     */
    private $type;

    /**
     * @var Serializer
     */
    private $serializer;

    public function setType(string $type): void
    {
        $this->type = $type;
    }

    public function getSerializer(): Serializer
    {
        return $this->serializer;
    }

    public function setSerializer(Serializer $serializer): void
    {
        $this->serializer = $serializer;
    }

    /**
     * {@inheritdoc}
     */
    public function convertToDatabaseValue($value, AbstractPlatform $platform)
    {
        return $this->getSerializer()->serialize($value, 'json');
    }

    /**
     * {@inheritdoc}
     */
    public function convertToPHPValue($value, AbstractPlatform $platform)
    {
        return $this->getSerializer()->deserialize($value, $this->type, 'json');
    }

    /**
     * @param array $field
     * @param AbstractPlatform $platform
     *
     * @return string
     */
    public function getSQLDeclaration(array $field, AbstractPlatform $platform)
    {
        return 'JSON';
    }

    /**
     * Gets the name of this type.
     *
     * @return string
     */
    public function getName()
    {
        return 'JSON';
    }
}
```

## File: `src/Infrastructure/CommonBundle/Event/AsyncElasticEventStore.php`
```php
<?php

namespace Leos\Infrastructure\CommonBundle\Event;

use Elastica\Document;
use Elastica\Type;
use OldSound\RabbitMqBundle\RabbitMq\ConsumerInterface;
use PhpAmqpLib\Message\AMQPMessage;

class AsyncElasticEventStore implements ConsumerInterface
{
    /**
     * @var Type
     */
    private $type;

    public function __construct(Type $type)
    {
        $this->type = $type;
    }

    public function execute(AMQPMessage $msg)
    {
        try {
            $event = $this->decode($msg->getBody());

            $this->store($event);

        } catch (\Exception $exception) {

            echo $exception->getMessage();

            echo "\n";

            return self::MSG_REJECT_REQUEUE;
        }

        return self::MSG_ACK;
    }

    private function decode(string $msg): array
    {
      return json_decode($msg, true);
    }

    private function store(array $event): void
    {
        $doc = new Document(
            $event['uuid'],
            $event
        );

        $this->type->addDocument($doc);
    }
}
```

## File: `src/Infrastructure/CommonBundle/Event/AsyncEventConsumer.php`
```php
<?php

namespace Leos\Infrastructure\CommonBundle\Event;

use OldSound\RabbitMqBundle\RabbitMq\ConsumerInterface;
use PhpAmqpLib\Message\AMQPMessage;

class AsyncEventConsumer implements ConsumerInterface
{

    /**
     * @param AMQPMessage $msg The message
     * @return mixed false to reject and requeue, any other value to acknowledge
     */
    public function execute(AMQPMessage $msg)
    {
        var_dump($msg->getBody());

        return self::MSG_ACK;
    }
}
```

## File: `src/Infrastructure/CommonBundle/Event/EventAware.php`
```php
<?php

namespace Leos\Infrastructure\CommonBundle\Event;

use Leos\Domain\Common\Event\EventInterface;
use Symfony\Component\EventDispatcher\Event;

class EventAware extends Event
{
    /**
     * @var EventAwareId
     */
    private $uuid;

    /**
     * @var EventInterface
     */
    private $event;

    /**
     * @var \DateTimeImmutable
     */
    private $createdAt;

    /**
     * @var string
     */
    private $type;

    public function __construct(EventInterface $event)
    {
        $this->uuid = new EventAwareId((string) $event->uuid());
        $this->event = $event;
        $this->type = $event->type();
        $this->createdAt = $event->createdAt();
    }

    public function type(): string
    {
        return $this->type;
    }

    public function uuid(): EventAwareId
    {
        return $this->uuid;
    }

    public function event(): EventInterface
    {
        return $this->event;
    }

    public function createdAt(): \DateTimeImmutable
    {
        return $this->createdAt;
    }
}
```

## File: `src/Infrastructure/CommonBundle/Event/EventAwareId.php`
```php
<?php

namespace Leos\Infrastructure\CommonBundle\Event;

use Leos\Domain\Common\ValueObject\AggregateRootId;

class EventAwareId extends AggregateRootId
{
    /** @var string */
    protected $uuid;
}
```

## File: `src/Infrastructure/CommonBundle/Event/EventDispatcher.php`
```php
<?php

namespace Leos\Infrastructure\CommonBundle\Event;

use Leos\Domain\Common\Event\EventCollector;
use Leos\Domain\Common\Event\EventDispatcherInterface;
use Leos\Domain\Common\Event\EventInterface;
use Leos\Domain\Common\Event\EventPublisher;
use Symfony\Component\EventDispatcher\EventDispatcherInterface as InfrastructureDispatcher;

class EventDispatcher implements EventDispatcherInterface
{
    /**
     * @var InfrastructureDispatcher
     */
    private $dispatcher;

    /**
     * @var EventCollector
     */
    private $collector;

    public function __construct(InfrastructureDispatcher $dispatcher, EventCollector $collector)
    {
        $this->dispatcher = $dispatcher;
        $this->collector = $collector;
        $this->bootPublisher();
    }

    private function bootPublisher(): void
    {
        EventPublisher::boot($this);
    }

    public function record(EventInterface $event): void
    {
        $this->collector->collect($event);
    }

    public function dispatch(): void
    {
        foreach ($this->collector->events() as $key => $event) {

            $this->dispatcher->dispatch($event->type(), new EventAware($event));

            $this->collector->remove($key);
        }
    }
}
```

## File: `src/Infrastructure/CommonBundle/Exception/Form/FormException.php`
```php
<?php

namespace Leos\Infrastructure\CommonBundle\Exception\Form;

use Symfony\Component\Form\FormInterface;

class FormException extends \Exception
{
    /**
     * @var FormInterface
     */
    private $form;

    public function __construct(FormInterface $form)
    {
        parent::__construct("Form Error", 0);

        $this->form = $form;
    }

    public function getForm(): FormInterface
    {
        return $this->form;
    }
}
```

## File: `src/Infrastructure/CommonBundle/Exception/Form/FormFactoryException.php`
```php
<?php

namespace Leos\Infrastructure\CommonBundle\Exception\Form;

class FormFactoryException extends \LogicException
{

    public function __construct()
    {
        parent::__construct("form.factory.exception.form_class_required", 5005);
    }
}
```

## File: `src/Infrastructure/CommonBundle/Factory/AbstractFactory.php`
```php
<?php

namespace Leos\Infrastructure\CommonBundle\Factory;

use Symfony\Component\Form\FormFactoryInterface;
use Symfony\Component\Form\FormInterface;

use Leos\Infrastructure\CommonBundle\Exception\Form\FormException;
use Leos\Infrastructure\CommonBundle\Exception\Form\FormFactoryException;

/**
 * Class AbstractFactory
 *
 * @package Leos\Infrastructure\CommonBundle\Factory
 */
abstract class AbstractFactory
{
    const
        CREATE = 'POST',
        REPLACE = 'PUT',
        UPDATE = 'PATCH'
    ;

    /**
     * @var FormFactoryInterface
     */
    private $formFactory;

    /**
     * @var string
     */
    protected $formClass;

    public function __construct(FormFactoryInterface $formFactory)
    {
        $this->formFactory = $formFactory;
        
        if (!$this->formClass) {
            
            throw new FormFactoryException();
        }
    }

    /**
     * @param string $action
     * @param array $data
     * @param null|object $object
     *
     * @return mixed
     *
     * @throws FormException
     */
    protected function execute(string $action = self::CREATE, array $data, $object = null)
    {
        $form = $this->createForm($action, $object)->submit($data, self::UPDATE !== $action);

        if (!$form->isValid()) {

            throw new FormException($form);
        }

        $this->setTimestamp($action, $object);

        return $form->getData();
    }

    private function setTimestamp(string $action, $object): void
    {
        if (is_object($object)
            && in_array($action, [ self::UPDATE, self::REPLACE ])
            && method_exists($object, 'setUpdate')
        ) {

            $object->setUpdate(new \DateTimeImmutable());
        }
    }

    private function createForm(string $action = self::CREATE, $object = null): FormInterface
    {
        return $this->formFactory->create($this->formClass, $object, [
            'method' => $action
        ]);
    }
}
```

## File: `src/Infrastructure/CommonBundle/Pagination/PagerTrait.php`
```php
<?php
namespace Leos\Infrastructure\CommonBundle\Pagination;

use Leos\Application\Request\Common\Pagination;

use Pagerfanta\Pagerfanta;
use Hateoas\Configuration\Route;
use Hateoas\Representation\PaginatedRepresentation;
use Hateoas\Representation\Factory\PagerfantaFactory;

/**
 * Trait PagerTrait
 *
 * @package Leos\Infrastructure\CommonBundle\Pagination
 */
Trait PagerTrait
{
    /**
     * @param Pagerfanta $pager
     * @param string $route
     * @param array $params
     * @param int $limit
     * @param int $page
     *
     * @return PaginatedRepresentation
     */
    public function getPagination(
        Pagerfanta $pager,
        string $route,
        array $params  = [],
        int $limit = Pagination::LIMIT, // I dont like have application inside infrastructure...
        int $page = Pagination::PAGE): PaginatedRepresentation
    {
        $pager
            ->setMaxPerPage($limit)
            ->setCurrentPage($page);

        //Merge pagination parameters
        $params = array_merge($params, [
            'limit' => $limit,
            'page' => $page
        ]);

        return (new PagerfantaFactory())->createRepresentation($pager, new Route($route, $params));
    }

}
```

## File: `src/Infrastructure/CommonBundle/Repository/EventStoreRepository.php`
```php
<?php

namespace Leos\Infrastructure\CommonBundle\Repository;

use Leos\Infrastructure\CommonBundle\Doctrine\ORM\Repository\EntityRepository;
use Leos\Infrastructure\CommonBundle\Event\EventAware;

class EventStoreRepository extends EntityRepository
{

    public function store(EventAware $eventAware)
    {
        $this->_em->persist($eventAware);
    }
}
```

## File: `src/Infrastructure/CommonBundle/Resources/config/services.yml`
```yaml
services:

    leos.abstract.repository:
        abstract: true
        factory: ["@doctrine.orm.entity_manager", "getRepository"]

    Leos\Infrastructure\CommonBundle\Repository\EventStoreRepository:
        parent: leos.abstract.repository
        class: Leos\Infrastructure\CommonBundle\Repository\EventStoreRepository
        arguments:
            - Leos\Infrastructure\CommonBundle\Event\EventAware

    Leos\Domain\Common\Event\EventDispatcherInterface:
        class: Leos\Infrastructure\CommonBundle\Event\EventDispatcher
        public: true
        autowire: true

    Leos\Domain\Common\Event\EventCollector:
        factory: ["Leos\\Domain\\Common\\Event\\EventCollector", "instance"]
        public: true

    leos.evens.async.consumer.events:
        class: Leos\Infrastructure\CommonBundle\Event\AsyncEventConsumer

    leos.evens.async.store.events:
        class: Leos\Infrastructure\CommonBundle\Event\AsyncElasticEventStore
        arguments:
          - '@fos_elastica.index.events.events'

    leos.event.bus.middleware.event_store:
        class: Leos\Infrastructure\CommonBundle\Bus\Middleware\EventStoreMiddleware
        autowire: true

    leos.event.bus.middleware.event_publisher:
        class: Leos\Infrastructure\CommonBundle\Bus\Middleware\EventPublisherMiddleware
        arguments:
          - '@old_sound_rabbit_mq.events_producer'
          - '@Leos\Domain\Common\Event\EventCollector'
          - '@jms_serializer.serializer'

    leos.event.bus.middleware.dispatcher:
        class: Leos\Infrastructure\CommonBundle\Bus\Middleware\EventDispatcherMiddleware
        autowire: true
```

## File: `src/Infrastructure/CommonBundle/Resources/config/persistence/EventAware.orm.yml`
```yaml
Leos\Infrastructure\CommonBundle\Event\EventAware:
    type: entity
    table: events
    repositoryClass: Leos\Infrastructure\CommonBundle\Repository\EventStoreRepository
    id:
      uuid:
        type: eventAwareId
        nullable: false
    indexes:
      type_index:
        columns: [ type ]

    fields:
      type:
        type: string
        length: 255
        nullable: false

      event:
        type: event

      createdAt:
        type: datetime

    lifecycleCallbacks: {  }
```

## File: `src/Infrastructure/CommonBundle/Resources/config/serializer/common/Event.AbstractEvent.yml`
```yaml
Leos\Domain\Common\Event\AbstractEvent:
    properties:
        uuid:
            expose: true
            type: Leos\Domain\Common\ValueObject\AggregateRootId
            groups: ['Identifier']
            inline: true

        createdAt:
            expose: true
            type: DateTimeImmutable

        type:
            expose: true
```

## File: `src/Infrastructure/CommonBundle/Resources/config/serializer/common/ValueObject.AggregateRoot.yml`
```yaml
Leos\Domain\Common\ValueObject\AggregateRoot:
    exclusion_policy: ALL
    properties:
        uuid:
            expose: true
            groups: ['Identifier']
```

## File: `src/Infrastructure/CommonBundle/Resources/config/serializer/common/ValueObject.AggregateRootId.yml`
```yaml
Leos\Domain\Common\ValueObject\AggregateRootId:
    properties:
        uuid:
            expose: true
```

## File: `src/Infrastructure/MoneyBundle/LeosInfrastructureMoneyBundle.php`
```php
<?php

namespace Leos\Infrastructure\MoneyBundle;

use Symfony\Component\HttpKernel\Bundle\Bundle;

class LeosInfrastructureMoneyBundle extends Bundle
{
}
```

## File: `src/Infrastructure/MoneyBundle/DependencyInjection/LeosInfrastructureMoneyExtension.php`
```php
<?php

namespace Leos\Infrastructure\MoneyBundle\DependencyInjection;

use Symfony\Component\DependencyInjection\ContainerBuilder;
use Symfony\Component\Config\FileLocator;
use Symfony\Component\HttpKernel\DependencyInjection\Extension;
use Symfony\Component\DependencyInjection\Loader;

/**
 * This is the class that loads and manages your bundle configuration.
 *
 * @link http://symfony.com/doc/current/cookbook/bundles/extension.html
 */
class LeosInfrastructureMoneyExtension extends Extension
{
    /**
     * {@inheritdoc}
     */
    public function load(array $configs, ContainerBuilder $container)
    {
        $loader = new Loader\YamlFileLoader($container, new FileLocator(__DIR__.'/../Resources/config'));
        $loader->load('services.yml');
    }
}
```

## File: `src/Infrastructure/MoneyBundle/Resources/config/services.yml`
```yaml
services:
```

## File: `src/Infrastructure/MoneyBundle/Resources/config/persistence/ValueObject/Currency.orm.yml`
```yaml
Leos\Domain\Money\ValueObject\Currency:
  type: embeddable
  fields:
    code:
      type: string
      length: 3

    exchange:
      type: decimal
      precision: 10
      scale: 4
```

## File: `src/Infrastructure/MoneyBundle/Resources/config/serializer/money/ValueObject.Currency.yml`
```yaml
Leos\Domain\Money\ValueObject\Currency:
    exclusion_policy: ALL
    properties:
        code:
            expose: true
            groups: [Basic]
            serialized_name: code

        exchange:
            expose: true
            groups: [Basic]
            serialized_name: echange

```

## File: `src/Infrastructure/PaymentBundle/LeosInfrastructurePaymentBundle.php`
```php
<?php

namespace Leos\Infrastructure\PaymentBundle;

use Doctrine\DBAL\Types\Type;

use Leos\Domain\Payment\ValueObject\DepositDetails;
use Leos\Domain\Payment\ValueObject\WithdrawalDetails;

use Leos\Infrastructure\CommonBundle\Doctrine\Types\JsonDocumentType;

use Symfony\Component\HttpKernel\Bundle\Bundle;

/**
 * Class LeosInfrastructurePaymentBundle
 *
 * @package Leos\Infrastructure\PaymentBundle
 */
class LeosInfrastructurePaymentBundle extends Bundle
{
    public function boot()
    {
        $this->addDBALType('deposit_details', DepositDetails::class);
        $this->addDBALType('withdrawal_details', WithdrawalDetails::class);
    }

    /**
     * @param string $type
     * @param string $object
     *
     * @throws \Doctrine\DBAL\DBALException
     */
    private function addDBALType(string $type, string $object): void
    {
        if (!Type::hasType($type)) {

            Type::addType($type, JsonDocumentType::class);

            /** @var JsonDocumentType $type */
            $type = Type::getType($type);

            $type->setSerializer(
                $this->container->get('jms_serializer')
            );

            $type->setType($object);
        }
    }
}
```

## File: `src/Infrastructure/PaymentBundle/DependencyInjection/LeosInfrastructurePaymentExtension.php`
```php
<?php

namespace Leos\Infrastructure\PaymentBundle\DependencyInjection;

use Symfony\Component\DependencyInjection\ContainerBuilder;
use Symfony\Component\Config\FileLocator;
use Symfony\Component\HttpKernel\DependencyInjection\Extension;
use Symfony\Component\DependencyInjection\Loader;

/**
 * This is the class that loads and manages your bundle configuration.
 *
 * @link http://symfony.com/doc/current/cookbook/bundles/extension.html
 */
class LeosInfrastructurePaymentExtension extends Extension
{
    /**
     * {@inheritdoc}
     */
    public function load(array $configs, ContainerBuilder $container)
    {
        $loader = new Loader\YamlFileLoader($container, new FileLocator(__DIR__.'/../Resources/config'));
        $loader->load('services.yml');
    }
}
```

## File: `src/Infrastructure/PaymentBundle/Resources/config/services.yml`
```yaml
services:

```

## File: `src/Infrastructure/PaymentBundle/Resources/config/persistence/Model/Deposit.orm.yml`
```yaml
Leos\Domain\Payment\Model\Deposit:
    type: entity
    fields:
      details:
        type: deposit_details
```

## File: `src/Infrastructure/PaymentBundle/Resources/config/persistence/Model/RollbackDeposit.orm.yml`
```yaml
Leos\Domain\Payment\Model\RollbackDeposit:
    type: entity
    fields:
      details:
        type: deposit_details
```

## File: `src/Infrastructure/PaymentBundle/Resources/config/persistence/Model/RollbackWithdrawal.orm.yml`
```yaml
Leos\Domain\Payment\Model\RollbackWithdrawal:
    type: entity
    fields:
      details:
        type: withdrawal_details
```

## File: `src/Infrastructure/PaymentBundle/Resources/config/persistence/Model/Withdrawal.orm.yml`
```yaml
Leos\Domain\Payment\Model\Withdrawal:
    type: entity
    fields:
      details:
        type: withdrawal_details
```

## File: `src/Infrastructure/PaymentBundle/Resources/config/serializer/Model.Deposit.yml`
```yaml
Leos\Domain\Payment\Model\Deposit:
    properties:
        details:
            expose: true
            groups: [Basic]
            type: Leos\Domain\Payment\ValueObject\DepositDetails
```

## File: `src/Infrastructure/PaymentBundle/Resources/config/serializer/Model.RollbackDeposit.yml`
```yaml
Leos\Domain\Payment\Model\RollbackDeposit:
    properties:
        details:
            expose: true
            groups: [Basic]
            type: Leos\Domain\Payment\ValueObject\DepositDetails
```

## File: `src/Infrastructure/PaymentBundle/Resources/config/serializer/Model.RollbackWithdrawal.yml`
```yaml
Leos\Domain\Payment\Model\RollbackWithdrawal:
    properties:
        details:
            expose: true
            groups: [Basic]
            type: Leos\Domain\Payment\ValueObject\WithdrawalDetails

```

## File: `src/Infrastructure/PaymentBundle/Resources/config/serializer/Model.Withdrawal.yml`
```yaml
Leos\Domain\Payment\Model\Withdrawal:
    properties:
        details:
            expose: true
            groups: [Basic]
            type: Leos\Domain\Payment\ValueObject\WithdrawalDetails
```

## File: `src/Infrastructure/PaymentBundle/Resources/config/serializer/ValueObject.DepositDetails.yml`
```yaml
Leos\Domain\Payment\ValueObject\DepositDetails:
    exclusion_policy: ALL
    properties:
      provider:
          type: string
          groups: [Basic]
```

## File: `src/Infrastructure/PaymentBundle/Resources/config/serializer/ValueObject.WithdrawalDetails.yml`
```yaml
Leos\Domain\Payment\ValueObject\WithdrawalDetails:
    exclusion_policy: ALL
    properties:
      provider:
          type: string
          groups: [Basic]

```

## File: `src/Infrastructure/SecurityBundle/LeosInfrastructureSecurityBundle.php`
```php
<?php

namespace Leos\Infrastructure\SecurityBundle;

use Symfony\Component\HttpKernel\Bundle\Bundle;

class LeosInfrastructureSecurityBundle extends Bundle
{
}
```

## File: `src/Infrastructure/SecurityBundle/DependencyInjection/LeosInfrastructureSecurityExtension.php`
```php
<?php

namespace Leos\Infrastructure\SecurityBundle\DependencyInjection;

use Symfony\Component\DependencyInjection\ContainerBuilder;
use Symfony\Component\Config\FileLocator;
use Symfony\Component\HttpKernel\DependencyInjection\Extension;
use Symfony\Component\DependencyInjection\Loader;

/**
 * This is the class that loads and manages your bundle configuration.
 *
 * @link http://symfony.com/doc/current/cookbook/bundles/extension.html
 */
class LeosInfrastructureSecurityExtension extends Extension
{
    /**
     * {@inheritdoc}
     */
    public function load(array $configs, ContainerBuilder $container)
    {
        $loader = new Loader\YamlFileLoader($container, new FileLocator(__DIR__.'/../Resources/config'));
        $loader->load('services.yml');
    }
}
```

## File: `src/Infrastructure/SecurityBundle/EventListener/JWTCreatedListener.php`
```php
<?php

namespace Leos\Infrastructure\SecurityBundle\EventListener;

use JMS\Serializer\ArrayTransformerInterface;
use Leos\Infrastructure\SecurityBundle\Security\Model\Auth;
use Lexik\Bundle\JWTAuthenticationBundle\Event\JWTCreatedEvent;

/**
 * Class JWTCreatedListener
 *
 * @package Leos\Infrastructure\SecurityBundle\EventListener
 */
class JWTCreatedListener
{
    /**
     * @var ArrayTransformerInterface
     */
    private $serializer;

    public function __construct(ArrayTransformerInterface $serializer)
    {
        $this->serializer = $serializer;
    }

    public function onJWTCreated(JWTCreatedEvent $event): void
    {
        $expiration = new \DateTime('+1 day');

        /** @var Auth $user */
        $user             = $event->getUser();
        $payload          = $event->getData();
        $payload['exp']   = $expiration->getTimestamp();

        $serializerUser = $this->serializer->toArray($user);

        $event->setData(array_merge($payload, $serializerUser));
    }
}
```

## File: `src/Infrastructure/SecurityBundle/Resources/config/services.yml`
```yaml
imports:
    - { resource: application/use_case.yml }

services:

  leos.security.user_provider:
    class: Leos\Infrastructure\SecurityBundle\Security\UserProvider\UserProvider
    autowire: true

  leos.event.jwt_created_listener:
    class: Leos\Infrastructure\SecurityBundle\EventListener\JWTCreatedListener
    autowire: true
    tags:
      - { name: kernel.event_listener, event: lexik_jwt_authentication.on_jwt_created, method: onJWTCreated }
```

## File: `src/Infrastructure/SecurityBundle/Resources/config/application/use_case.yml`
```yaml
services:

    Leos\Application\UseCase\Security\LoginHandler:
        public: true
        autowire: true
        tags:
          - { name: tactician.handler, command: Leos\Application\UseCase\Security\Request\Login }

```

## File: `src/Infrastructure/SecurityBundle/Resources/config/persistence/ValueObject/AuthUser.orm.yml`
```yaml
Leos\Domain\Security\ValueObject\AuthUser:
  type: embeddable
  fields:
    username:
      type: string
      unique: true
      nullable: false

    passwordHash:
      type: string
      nullable: false
```

## File: `src/Infrastructure/SecurityBundle/Resources/config/serializer/auth/ValueObject.AuthUser.yml`
```yaml
Leos\Domain\Security\ValueObject\AuthUser:
    exclusion_policy: ALL
    properties:
        username:
            expose: true
            groups: [Auth]

        roles:
            expose: true
            groups: [Auth]
```

## File: `src/Infrastructure/SecurityBundle/Security/Model/Auth.php`
```php
<?php

namespace Leos\Infrastructure\SecurityBundle\Security\Model;

use Leos\Domain\Security\ValueObject\AuthUser;

use Symfony\Component\Security\Core\User\UserInterface;
use Symfony\Component\Security\Core\Encoder\EncoderAwareInterface;

/**
 * Class Auth
 *
 * @package Leos\Infrastructure\SecurityBundle\Security\Model
 */
class Auth implements UserInterface, EncoderAwareInterface
{
    /**
     * @var string
     */
    private $uuid;

    /**
     * @var AuthUser
     */
    private $authUser;

    public function __construct(string $uuid, AuthUser $authUser)
    {
        $this->uuid = $uuid;
        $this->authUser = $authUser;
    }

    public function id(): string
    {
        return $this->uuid;
    }

    /**
     * Returns the roles granted to the user.
     *
     * <code>
     * public function getRoles()
     * {
     *     return array('ROLE_USER');
     * }
     * </code>
     *
     * Alternatively, the roles might be stored on a ``roles`` property,
     * and populated in any number of different ways when the user object
     * is created.
     *
     * @return (Role|string)[] The user roles
     */
    public function getRoles()
    {
        return $this->authUser->roles();
    }

    /**
     * Returns the password used to authenticate the user.
     *
     * This should be the encoded password. On authentication, a plain-text
     * password will be salted, encoded, and then compared to this value.
     *
     * @return string The password
     */
    public function getPassword()
    {
        return $this->authUser->password();
    }

    /**
     * Returns the salt that was originally used to encode the password.
     *
     * This can return null if the password was not encoded using a salt.
     *
     * @return string|null The salt
     */
    public function getSalt()
    {
        return null;
    }

    /**
     * Returns the username used to authenticate the user.
     *
     * @return string The username
     */
    public function getUsername()
    {
        return $this->authUser->username();
    }

    /**
     * Removes sensitive data from the user.
     *
     * This is important if, at any given point, sensitive information like
     * the plain-text password is stored on this object.
     */
    public function eraseCredentials()
    {

    }

    /**
     * Gets the name of the encoder used to encode the password.
     *
     * If the method returns null, the standard way to retrieve the encoder
     * will be used instead.
     *
     * @return string
     */
    public function getEncoderName()
    {
        return 'harsh';
    }
}
```

## File: `src/Infrastructure/SecurityBundle/Security/UserProvider/UserProvider.php`
```php
<?php

namespace Leos\Infrastructure\SecurityBundle\Security\UserProvider;

use Leos\Domain\User\Repository\UserRepositoryInterface;

use Leos\Infrastructure\SecurityBundle\Security\Model\Auth;

use Symfony\Component\Security\Core\User\UserInterface;
use Symfony\Component\Security\Core\User\UserProviderInterface;
use Symfony\Component\Security\Core\Exception\UnsupportedUserException;
use Symfony\Component\Security\Core\Exception\UsernameNotFoundException;

/**
 * Class UserProvider
 * 
 * @package Leos\Infrastructure\SecurityBundle\Security\UserProvider
 */
class UserProvider implements UserProviderInterface
{
    /**
     * @var UserRepositoryInterface
     */
    private $repository;

    public function __construct(UserRepositoryInterface $repository)
    {
        $this->repository = $repository;
    }

    /**
     * Loads the user for the given username.
     *
     * This method must throw UsernameNotFoundException if the user is not
     * found.
     *
     * @param string $username The username
     *
     * @return UserInterface
     *
     * @throws UsernameNotFoundException if the user is not found
     */
    public function loadUserByUsername($username)
    {
        $user = $this->repository->findOneByUsername($username);

        if (!$user) {

            throw new UsernameNotFoundException();
        }

        return new Auth($user->uuid()->__toString(), $user->auth());
    }

    /**
     * Refreshes the user for the account interface.
     *
     * It is up to the implementation to decide if the user data should be
     * totally reloaded (e.g. from the database), or if the UserInterface
     * object can just be merged into some internal array of users / identity
     * map.
     *
     * @param UserInterface $user
     *
     * @return UserInterface
     *
     * @throws UnsupportedUserException if the account is not supported
     */
    public function refreshUser(UserInterface $user)
    {
        return $this->loadUserByUsername($user->getUsername());
    }

    /**
     * Whether this provider supports the given user class.
     *
     * @param string $class
     *
     * @return bool
     */
    public function supportsClass($class)
    {
        return Auth::class === $class;
    }
}
```

## File: `src/Infrastructure/SecurityBundle/ValueObject/EncodedPassword.php`
```php
<?php

namespace Leos\Infrastructure\SecurityBundle\ValueObject;

use Leos\Domain\Security\Exception\InvalidPasswordException;
use Leos\Domain\Security\Exception\NullPasswordException;
use Leos\Domain\Security\ValueObject\EncodedPasswordInterface;

use Symfony\Component\Security\Core\Encoder\BCryptPasswordEncoder;

/**
 * Class EncodedPassword
 *
 * @package Leos\Infrastructure\SecurityBundle\ValueObject
 */
final class EncodedPassword implements EncodedPasswordInterface
{
    const
        COST = 12
    ;

    /**
     * @var string
     */
    private $password;

    /**
     * @var string
     */
    private $plainPassword;

    /**
     * @var BCryptPasswordEncoder
     */
    private $encoder;
    
    /**
     * EncodedPassword constructor.
     *
     * @param string|null $plainPassword
     *
     * @throws InvalidPasswordException
     * @throws NullPasswordException
     */
    public function __construct(?string $plainPassword = null)
    {
        if (null === $plainPassword) {

            throw new NullPasswordException();
        }

        $this->encoder = new BCryptPasswordEncoder(static::COST);

        $this->validate($plainPassword);

        $this->setPassword($plainPassword);
    }

    private function setPassword(string $plainPassword): void
    {
        $this->plainPassword = $plainPassword;

        $this->password = $this->encoder->encodePassword($plainPassword, null);
    }

    public function matchHash(string $encodedPassword): bool
    {
        return password_verify($this->plainPassword, $encodedPassword);
    }

    /**
     * @param string|null $plainPassword
     * @throws InvalidPasswordException
     */
    private function validate(?string $plainPassword): void
    {
        if (8 > strlen($plainPassword)) {

            throw new InvalidPasswordException();
        }
    }

    public function __toString(): string
    {
        return $this->password;
    }
}
```

## File: `src/Infrastructure/TransactionBundle/LeosInfrastructureTransactionBundle.php`
```php
<?php

namespace Leos\Infrastructure\TransactionBundle;

use Symfony\Component\HttpKernel\Bundle\Bundle;

class LeosInfrastructureTransactionBundle extends Bundle
{
}
```

## File: `src/Infrastructure/TransactionBundle/DependencyInjection/LeosInfrastructureTransactionExtension.php`
```php
<?php

namespace Leos\Infrastructure\TransactionBundle\DependencyInjection;

use Symfony\Component\DependencyInjection\ContainerBuilder;
use Symfony\Component\Config\FileLocator;
use Symfony\Component\HttpKernel\DependencyInjection\Extension;
use Symfony\Component\DependencyInjection\Loader;

/**
 * This is the class that loads and manages your bundle configuration.
 *
 * @link http://symfony.com/doc/current/cookbook/bundles/extension.html
 */
class LeosInfrastructureTransactionExtension extends Extension
{
    /**
     * {@inheritdoc}
     */
    public function load(array $configs, ContainerBuilder $container)
    {
        $loader = new Loader\YamlFileLoader($container, new FileLocator(__DIR__.'/../Resources/config'));
        $loader->load('services.yml');
    }
}
```

## File: `src/Infrastructure/TransactionBundle/Doctrine/Types/TransactionIdType.php`
```php
<?php

namespace Leos\Infrastructure\TransactionBundle\Doctrine\Types;

use Ramsey\Uuid\Doctrine\UuidBinaryType;

use Doctrine\DBAL\Platforms\AbstractPlatform;

use Leos\Domain\Transaction\ValueObject\TransactionId;

/**
 * Class TransactionType
 *
 * @package Leos\Infrastructure\TransactionBundle\Doctrine\Types
 */
class TransactionIdType extends UuidBinaryType
{
    const TRANSACTION_ID = 'transactionId';
    
    public function convertToPHPValue($value, AbstractPlatform $platform)
    {
        return (null === $value) ? null : TransactionId::fromBytes($value);
    }

    /**
     * @param TransactionId $value
     * @param AbstractPlatform $platform
     * @return null|string
     */
    public function convertToDatabaseValue($value, AbstractPlatform $platform)
    {
        if (is_string($value)) {

            return TransactionId::toBytes($value);
        }
        
        return (null === $value) ? null : $value->bytes();
    }

    public function getName()
    {
        return self::TRANSACTION_ID;
    }
}
```

## File: `src/Infrastructure/TransactionBundle/Repository/TransactionRepository.php`
```php
<?php

namespace Leos\Infrastructure\TransactionBundle\Repository;

use Leos\Domain\Transaction\Exception\TransactionNotFoundException;
use Leos\Domain\Transaction\Model\AbstractTransaction;
use Leos\Domain\Transaction\Repository\TransactionRepositoryInterface;

use Leos\Domain\Transaction\ValueObject\TransactionId;
use Leos\Infrastructure\CommonBundle\Doctrine\ORM\Repository\EntityRepository;

/**
 * Class TransactionRepository
 * 
 * @package Leos\Infrastructure\WalletBundle\Repository
 */
class TransactionRepository extends EntityRepository implements TransactionRepositoryInterface
{
    /**
     * @param TransactionId $transactionId
     *
     * @return AbstractTransaction
     *
     * @throws TransactionNotFoundException
     */
    public function get(TransactionId $transactionId): AbstractTransaction
    {
        $transaction = $this->createQueryBuilder('transaction')
            ->where('transaction.uuid = :id')
            ->setParameter('id', $transactionId->bytes())
            ->getQuery()
            ->getOneOrNullResult()
        ;

        if (!$transaction) {

            throw new TransactionNotFoundException();
        }

        return $transaction;
    }

    public function save(AbstractTransaction $transaction): void
    {
        $this->_em->persist($transaction);
    }
}
```

## File: `src/Infrastructure/TransactionBundle/Resources/config/services.yml`
```yaml
imports:
    - { resource: services/repository.yml }
    - { resource: application/use_case.yml }
```

## File: `src/Infrastructure/TransactionBundle/Resources/config/application/use_case.yml`
```yaml
services:

    leos.use_case.create_wallet:
        class: Leos\Application\UseCase\Transaction\CreateWalletHandler
        autowire: true
        tags:
          - { name: tactician.handler, command: Leos\Application\UseCase\Transaction\Request\CreateWallet }

    leos.use_case.create_deposit:
        class: Leos\Application\UseCase\Transaction\CreateDepositHandler
        autowire: true
        tags:
          - { name: tactician.handler, command: Leos\Application\UseCase\Transaction\Request\CreateDeposit }

    leos.use_case.rollback_deposit:
        class: Leos\Application\UseCase\Transaction\RollbackDepositHandler
        autowire: true
        tags:
          - { name: tactician.handler, command: Leos\Application\UseCase\Transaction\Request\RollbackDeposit }

    leos.use_case.create_withdrawal:
        class: Leos\Application\UseCase\Transaction\WithdrawalHandler
        autowire: true
        tags:
          - { name: tactician.handler, command: Leos\Application\UseCase\Transaction\Request\Withdrawal }

    leos.use_case.rollback_withdrawal:
        class: Leos\Application\UseCase\Transaction\RollbackWithdrawalHandler
        autowire: true
        tags:
          - { name: tactician.handler, command: Leos\Application\UseCase\Transaction\Request\RollbackWithdrawal }
```

## File: `src/Infrastructure/TransactionBundle/Resources/config/persistence/Model/AbstractTransaction.orm.yml`
```yaml
Leos\Domain\Transaction\Model\AbstractTransaction:
    type: entity
    table: transaction
    inheritanceType: SINGLE_TABLE
    discriminatorColumn:
      name: discriminator
      type: string
    discriminatorMap:
      deposit: Leos\Domain\Payment\Model\Deposit
      rollback_deposit: Leos\Domain\Payment\Model\RollbackDeposit
      rollback_withdrawal: Leos\Domain\Payment\Model\RollbackWithdrawal
      withdrawal: Leos\Domain\Payment\Model\Withdrawal
      create_wallet: Leos\Domain\Wallet\Factory\WalletFactory

    repositoryClass: Leos\Infrastructure\TransactionBundle\Repository\TransactionRepository

    id:
      uuid:
        id: true
        column: id
        type: transactionId
        generator:
          strategy: UUID

    fields:
      createdAt:
        type: datetimetz

      updatedAt:
        type: datetimetz
        nullable: true

      operationReal:
        type: integer

      operationBonus:
        type: integer

      state:
        type: string

    embedded:

      type:
        class: Leos\Domain\Transaction\ValueObject\TransactionType

      prevReal:
        class: Leos\Domain\Wallet\ValueObject\Credit

      prevBonus:
        class: Leos\Domain\Wallet\ValueObject\Credit

      currency:
        class: Leos\Domain\Money\ValueObject\Currency

    manyToOne:
        wallet:
          targetEntity: Leos\Domain\Wallet\Model\Wallet
          joinColumn:
            name: wallet_id
            referencedColumnName: id
            nullable: false
            onDelete: CASCADE
          cascade:
            - all

        referralTransaction:
          targetEntity: Leos\Domain\Transaction\Model\AbstractTransaction
          joinColumn:
            name: referral_transaction_id
            nullable: true
            referencedColumnName: id
            onDelete: CASCADE
          cascade:
            - all

    lifecycleCallbacks: {  }
```

## File: `src/Infrastructure/TransactionBundle/Resources/config/persistence/ValueObject/TransactionType.orm.yml`
```yaml
Leos\Domain\Transaction\ValueObject\TransactionType:
  type: embeddable
  fields:
    type:
      type: string
```

## File: `src/Infrastructure/TransactionBundle/Resources/config/serializer/transaction/Model.AbstractTransaction.yml`
```yaml
Leos\Domain\Transaction\Model\AbstractTransaction:
    exclusion_policy: ALL
    discriminator:
      field_name: discriminator
      map:
        deposit: Leos\Domain\Payment\Model\Deposit
        rollback_deposit: Leos\Domain\Payment\Model\RollbackDeposit
        withdrawal: Leos\Domain\Payment\Model\Withdrawal
        rollback_withdrawal: Leos\Domain\Payment\Model\RollbackWithdrawal
        create_wallet: Leos\Domain\Wallet\Factory\WalletFactory

    properties:
        type:
            expose: true
            groups: [Basic]
            inline: true
            type: Leos\Domain\Transaction\ValueObject\TransactionType

        operationReal:
            expose: true
            groups: [Basic]

        operationBonus:
            expose: true
            groups: [Basic]

        prevReal:
            expose: true
            groups: [Basic]
            type: Leos\Domain\Wallet\ValueObject\Credit

        prevBonus:
            expose: true
            groups: [Basic]
            type: Leos\Domain\Wallet\ValueObject\Credit

        createdAt:
            expose: true
            groups: [Basic]

        updatedAt:
            expose: true
            groups: [Basic]

        wallet:
            expose: true
            groups: [Identifier, Basic]
            type: Leos\Domain\Wallet\Model\Wallet

        details:
            expose: true
            groups: [Basic]

        referralTransaction:
            expose: true
            groups: [Basic]
            type: Leos\Domain\Transaction\Model\AbstractTransaction
```

## File: `src/Infrastructure/TransactionBundle/Resources/config/serializer/transaction/ValueObject.TransactionType.yml`
```yaml
Leos\Domain\Transaction\ValueObject\TransactionType:
    exclusion_policy: ALL
    properties:
      type:
          type: string
          groups: [Basic]
```

## File: `src/Infrastructure/TransactionBundle/Resources/config/services/repository.yml`
```yaml
services:
    Leos\Domain\Transaction\Repository\TransactionRepositoryInterface:
        parent: leos.abstract.repository
        class: Leos\Infrastructure\TransactionBundle\Repository\TransactionRepository
        arguments:
            - Leos\Domain\Transaction\Model\AbstractTransaction
```

## File: `src/Infrastructure/UserBundle/LeosInfrastructureUserBundle.php`
```php
<?php

namespace Leos\Infrastructure\UserBundle;

use Symfony\Component\HttpKernel\Bundle\Bundle;

/**
 * Class LeosInfrastructureUserBundle
 *
 * @package Leos\Infrastructure\UserBundle
 */
class LeosInfrastructureUserBundle extends Bundle
{
    
}
```

## File: `src/Infrastructure/UserBundle/DependencyInjection/LeosInfrastructureUserExtension.php`
```php
<?php

namespace Leos\Infrastructure\UserBundle\DependencyInjection;

use Symfony\Component\DependencyInjection\ContainerBuilder;
use Symfony\Component\Config\FileLocator;
use Symfony\Component\HttpKernel\DependencyInjection\Extension;
use Symfony\Component\DependencyInjection\Loader;

/**
 * This is the class that loads and manages your bundle configuration.
 *
 * @link http://symfony.com/doc/current/cookbook/bundles/extension.html
 */
class LeosInfrastructureUserExtension extends Extension
{
    /**
     * {@inheritdoc}
     */
    public function load(array $configs, ContainerBuilder $container)
    {
        $loader = new Loader\YamlFileLoader($container, new FileLocator(__DIR__.'/../Resources/config'));
        $loader->load('services.yml');
    }
}
```

## File: `src/Infrastructure/UserBundle/Doctrine/Types/UserIdType.php`
```php
<?php

namespace Leos\Infrastructure\UserBundle\Doctrine\Types;

use Ramsey\Uuid\Doctrine\UuidBinaryType;

use Doctrine\DBAL\Platforms\AbstractPlatform;

use Leos\Domain\User\ValueObject\UserId;

/**
 * Class UserIdType
 *
 * @package Leos\Infrastructure\WalletBundle\Doctrine\Types
 */
class UserIdType extends UuidBinaryType
{
    const USER_ID = 'userId';
    
    public function convertToPHPValue($value, AbstractPlatform $platform)
    {
        return (null === $value) ? null : UserId::fromBytes($value);
    }

    /**
     * @param UserId $value
     * @param AbstractPlatform $platform
     * @return null
     */
    public function convertToDatabaseValue($value, AbstractPlatform $platform)
    {
        return  (null === $value) ? null : $value->bytes();
    }

    public function getName()
    {
        return self::USER_ID;
    }
}
```

## File: `src/Infrastructure/UserBundle/Factory/UserFactory.php`
```php
<?php

namespace Leos\Infrastructure\UserBundle\Factory;

use Leos\Domain\User\Factory\UserFactoryInterface;
use Leos\Domain\User\Model\User;
use Leos\Infrastructure\CommonBundle\Factory\AbstractFactory;
use Leos\Infrastructure\UserBundle\Factory\Form\RegisterType;
use Symfony\Component\Form\FormFactoryInterface;

/**
 * Class UserFactory
 *
 * @package Leos\Infrastructure\UserBundle\Factory
 */
class UserFactory extends AbstractFactory implements UserFactoryInterface
{
    public function __construct(FormFactoryInterface $factory)
    {
        $this->formClass = RegisterType::class;
        parent::__construct($factory);
    }

    public function register(array $data): User
    {
        return $this->execute(self::CREATE, $data);
    }
}
```

## File: `src/Infrastructure/UserBundle/Factory/Form/ChangePasswordType.php`
```php
<?php

namespace Leos\Infrastructure\UserBundle\Factory\Form;


use Leos\Domain\User\Model\User;
use Leos\Infrastructure\CommonBundle\Factory\AbstractFactory;
use Leos\Infrastructure\SecurityBundle\ValueObject\EncodedPassword;
use Symfony\Component\Form\AbstractType;
use Symfony\Component\Form\Extension\Core\Type\PasswordType;
use Symfony\Component\Form\FormBuilderInterface;
use Symfony\Component\Form\FormEvent;
use Symfony\Component\Form\FormEvents;
use Symfony\Component\OptionsResolver\OptionsResolver;

class ChangePasswordType extends AbstractType
{
    /**
     * @param FormBuilderInterface $builder
     * @param array $options
     */
    public function buildForm(FormBuilderInterface $builder, array $options)
    {
        $builder
            ->add('oldPassword', PasswordType::class, [
                'mapped' => false
            ])
            ->add('newPassword', PasswordType::class, [
                'mapped' => false
            ])
            ->addEventListener(FormEvents::POST_SUBMIT, function (FormEvent $event){
                /** @var User $user */
                $user = $event->getData();

                $oldPassword = $event->getForm()->get('oldPassword')->getData();
                $newPassword = $event->getForm()->get('newPassword')->getData();

                $user->changePassword(
                    new EncodedPassword($oldPassword),
                    new EncodedPassword($newPassword)
                );
            })
        ;
    }

    /**
     * @param OptionsResolver $resolver
     */
    public function configureOptions(OptionsResolver $resolver)
    {
        $resolver->setDefaults([
            'data_class' => User::class,
            'csrf_protection' => false,
            'method' => AbstractFactory::UPDATE
        ]);
    }
}
```

## File: `src/Infrastructure/UserBundle/Factory/Form/RegisterType.php`
```php
<?php

namespace Leos\Infrastructure\UserBundle\Factory\Form;

use Leos\Domain\User\Model\User;
use Leos\Domain\User\ValueObject\UserId;

use Leos\Infrastructure\SecurityBundle\ValueObject\EncodedPassword;

use Symfony\Component\Form\AbstractType;
use Symfony\Component\Form\FormInterface;
use Symfony\Component\Form\FormBuilderInterface;
use Symfony\Component\OptionsResolver\OptionsResolver;
use Symfony\Component\Form\Extension\Core\Type\TextType;
use Symfony\Component\Form\Extension\Core\Type\EmailType;
use Symfony\Component\Form\Extension\Core\Type\PasswordType;
use Symfony\Component\Validator\Constraints\Email;
use Symfony\Component\Validator\Constraints\NotBlank;
use Symfony\Component\Validator\Constraints\NotNull;

/**
 * Class RegisterType
 *
 * @package Leos\Infrastructure\UserBundle\Factory\Form
 */
class RegisterType extends AbstractType
{
    /**
     * @param FormBuilderInterface $builder
     * @param array $options
     */
    public function buildForm(FormBuilderInterface $builder, array $options)
    {
        $builder
            ->add('uuid', null, [
                'mapped' => false
            ])
            ->add('email', EmailType::class, [
                'mapped' => false,
                'constraints' => [
                    new NotBlank([
                        'message' => 'user.exception.email.not_blank'
                    ]),
                    new NotNull([
                        'message' => 'user.exception.null.not_null'
                    ]),
                    new Email([
                        'message' => 'user.exception.email.not_valid'
                    ])
                ]
            ])
            ->add('username', TextType::class, [
                'mapped' => false,
                'constraints' => [
                    new NotBlank([
                        'message' => 'user.exception.username.not_blank'
                    ]),
                    new NotNull([
                        'message' => 'user.exception.username.not_null'
                    ])
                ]
            ])
            ->add('password', PasswordType::class, [
                'mapped' => false
            ]);
    }

    /**
     * @param OptionsResolver $resolver
     */
    public function configureOptions(OptionsResolver $resolver)
    {
        $resolver->setDefaults([
            'data_class' => User::class,
            'csrf_protection' => false,
            'empty_data' => function (FormInterface $form) {

                return User::create(
                    $form->get('uuid')->getData(),
                    (string) $form->get('username')->getData(),
                    (string) $form->get('email')->getData(),
                    new EncodedPassword((string) $form->get('password')->getData())
                );
            }
        ]);
    }
}
```

## File: `src/Infrastructure/UserBundle/Repository/UserRepository.php`
```php
<?php

namespace Leos\Infrastructure\UserBundle\Repository;

use Doctrine\ORM\EntityRepository;
use Leos\Domain\User\Exception\UserNotFoundException;
use Leos\Domain\User\Model\User;
use Leos\Domain\User\Repository\UserRepositoryInterface;
use Leos\Domain\User\ValueObject\UserId;

/**
 * Class UserRepository
 * 
 * @package Leos\Infrastructure\UserBundle\Repository
 */
class UserRepository extends EntityRepository implements UserRepositoryInterface
{
    public function findOneByUsername(string $username): ?User
    {
        return $this->createQueryBuilder('user')
            ->where('user.auth.username = :username')
            ->setParameter('username', $username)
            ->getQuery()
//            ->useResultCache(true, null, 'user.findByUsername'.$username)
            ->getOneOrNullResult()
        ;
    }

    public function findOneByUuid(UserId $userId): ?User
    {
        return $this->createQueryBuilder('user')
            ->where('user.uuid = :id')
            ->setParameter('id', $userId->bytes())
            ->getQuery()
//            ->useResultCache(true, null, 'user.findOneById'.$username)
            ->getOneOrNullResult()
        ;
    }

    public function getOneByUuid(UserId $userId): User
    {
        $user = $this->findOneByUuid($userId);

        if (!$user) {

            throw new UserNotFoundException();
        }

        return $user;
    }

    public function save(User $user): void
    {
        $this->_em->persist($user);
    }
}
```

## File: `src/Infrastructure/UserBundle/Resources/config/services.yml`
```yaml
imports:
    - { resource: services/factory.yml }
    - { resource: services/repository.yml }
    - { resource: application/use_case.yml }
    - { resource: services/eventListener.yml }
```

## File: `src/Infrastructure/UserBundle/Resources/config/application/use_case.yml`
```yaml
services:

    leos.use_case.user_command:
        class: Leos\Application\UseCase\User\RegisterUserHandler
        autowire: true
        tags:
          - { name: tactician.handler, command: Leos\Application\UseCase\User\Request\Register }

    leos.use_case.user_query:
        class: Leos\Application\UseCase\User\GetUserHandler
        autowire: true
        tags:
          - { name: tactician.handler, command: Leos\Application\UseCase\User\Request\GetUser }

```

## File: `src/Infrastructure/UserBundle/Resources/config/persistence/Model/User.orm.yml`
```yaml
Leos\Domain\User\Model\User:
    type: entity
    table: user
    repositoryClass: Leos\Infrastructure\UserBundle\Repository\UserRepository
    id:
      uuid:
        type: userId
        nullable: false
    indexes:
      email_index:
        columns: [ email ]

    uniqueConstraints:
        search_idx:
          columns: [ auth_username ]

    fields:
      email:
        type: string
        unique: true
        length: 32
        nullable: false

      createdAt:
        type: datetime

      updatedAt:
        type: datetime
        nullable: true

    embedded:
      auth:
        class: Leos\Domain\Security\ValueObject\AuthUser

    lifecycleCallbacks: {  }
```

## File: `src/Infrastructure/UserBundle/Resources/config/serializer/user/Model.User.yml`
```yaml
Leos\Domain\User\Model\User:
    exclusion_policy: ALL
    properties:
        email:
            expose: true
            groups: [Basic]

        createdAt:
            expose: true
            groups: [Basic]

        updatedAt:
            expose: true
            groups: [Basic]

    virtual_properties:
        uuid:
            serialized_name: uuid
            expose: true
            groups: [Identifier]
            type: string
```

## File: `src/Infrastructure/UserBundle/Resources/config/serializer/user/ValueObject.UserId.yml`
```yaml
Leos\Domain\User\ValueObject\UserId:
    exclusion_policy: ALL
    properties:
        uuid:
            expose: true
            groups: [Identifier]
```

## File: `src/Infrastructure/UserBundle/Resources/config/services/eventListener.yml`
```yaml
services:
    leos.event.listener.on_user_was_created:
        class: Leos\Domain\User\Event\Handler\OnUserWasCreated
        public: true
        tags:
            - { name: kernel.event_listener, event: UserWasCreated, method: __invoke }
```

## File: `src/Infrastructure/UserBundle/Resources/config/services/factory.yml`
```yaml
services:
    Leos\Domain\User\Factory\UserFactoryInterface:
        class: Leos\Infrastructure\UserBundle\Factory\UserFactory
        autowire: true
```

## File: `src/Infrastructure/UserBundle/Resources/config/services/repository.yml`
```yaml
services:
    Leos\Domain\User\Repository\UserRepositoryInterface:
        parent: leos.abstract.repository
        class: Leos\Infrastructure\UserBundle\Repository\UserRepository
        arguments:
            - Leos\Domain\User\Model\User
```

## File: `src/Infrastructure/WalletBundle/LeosInfrastructureWalletBundle.php`
```php
<?php

namespace Leos\Infrastructure\WalletBundle;

use Doctrine\DBAL\Types\Type;
use Symfony\Component\HttpKernel\Bundle\Bundle;

class LeosInfrastructureWalletBundle extends Bundle
{

}
```

## File: `src/Infrastructure/WalletBundle/DependencyInjection/LeosInfrastructureWalletExtension.php`
```php
<?php

namespace Leos\Infrastructure\WalletBundle\DependencyInjection;

use Symfony\Component\DependencyInjection\ContainerBuilder;
use Symfony\Component\Config\FileLocator;
use Symfony\Component\HttpKernel\DependencyInjection\Extension;
use Symfony\Component\DependencyInjection\Loader;

/**
 * This is the class that loads and manages your bundle configuration.
 *
 * @link http://symfony.com/doc/current/cookbook/bundles/extension.html
 */
class LeosInfrastructureWalletExtension extends Extension
{
    /**
     * {@inheritdoc}
     */
    public function load(array $configs, ContainerBuilder $container)
    {
        $loader = new Loader\YamlFileLoader($container, new FileLocator(__DIR__.'/../Resources/config'));
        $loader->load('services.yml');
    }
}
```

## File: `src/Infrastructure/WalletBundle/Doctrine/Types/WalletIdType.php`
```php
<?php

namespace Leos\Infrastructure\WalletBundle\Doctrine\Types;

use Ramsey\Uuid\Doctrine\UuidBinaryType;
use Doctrine\DBAL\Platforms\AbstractPlatform;

use Leos\Domain\Wallet\ValueObject\WalletId;

/**
 * Class WalletType
 *
 * @package Leos\Infrastructure\WalletBundle\Doctrine\Types
 */
class WalletIdType extends UuidBinaryType
{
    const WALLET_ID = 'walletId';
    
    public function convertToPHPValue($value, AbstractPlatform $platform)
    {
        return (null === $value) ? null : WalletId::fromBytes($value);
    }

    /**
     * @param WalletId $value
     * @param AbstractPlatform $platform
     * @return null
     */
    public function convertToDatabaseValue($value, AbstractPlatform $platform)
    {
        return (null === $value) ? null : $value->bytes();
    }

    public function getName()
    {
        return self::WALLET_ID;
    }
}
```

## File: `src/Infrastructure/WalletBundle/Repository/WalletRepository.php`
```php
<?php

namespace Leos\Infrastructure\WalletBundle\Repository;

use Leos\Domain\Wallet\Model\Wallet;
use Leos\Domain\Wallet\ValueObject\WalletId;
use Leos\Domain\Wallet\Repository\WalletRepositoryInterface;
use Leos\Domain\Wallet\Exception\Wallet\WalletNotFoundException;

use Leos\Infrastructure\CommonBundle\Doctrine\ORM\Repository\EntityRepository;

/**
 * Class WalletRepository
 * @package Leos\Infrastructure\WalletBundle\Repository
 */
class WalletRepository extends EntityRepository implements WalletRepositoryInterface
{
    /**
     * @param array $filters
     * @param array $operators
     * @param array $values
     * @param array $sort
     * @return \Pagerfanta\Pagerfanta|Wallet[]
     */
    public function findAll(array $filters = [], array $operators = [], array $values = [], array $sort = [])
    {
        $queryBuilder = $this->createQueryBuilder($alias = 'wallet');

        return $this->createOperatorPaginator($queryBuilder, $alias, $filters, $operators, $values, $sort);
    }
    /**
     * @param WalletId $uid
     * @return Wallet
     * @throws WalletNotFoundException
     */
    public function get(WalletId $uid): Wallet
    {
        $wallet = $this->findOneById($uid);

        if (!$wallet) {

            throw new WalletNotFoundException();
        }

        return $wallet;
    }

    public function findOneById(WalletId $uid): ?Wallet
    {
        return $this->createQueryBuilder('wallet')
            ->where('wallet.id = :id')
            ->setParameter('id', $uid->bytes())
            ->getQuery()
            ->getOneOrNullResult()
        ;
    }
}
```

## File: `src/Infrastructure/WalletBundle/Resources/config/services.yml`
```yaml
imports:
    - { resource: services/factory.yml }
    - { resource: services/repository.yml }
    - { resource: application/use_case.yml }
```

## File: `src/Infrastructure/WalletBundle/Resources/config/application/use_case.yml`
```yaml
services:

    Leos\Application\UseCase\Wallet\GetWalletHandler:
        public: true
        autowire: true
        tags:
          - { name: tactician.handler, command: Leos\Application\UseCase\Wallet\Request\GetWallet }

    Leos\Application\UseCase\Wallet\FindWalletHandler:
        public: true
        autowire: true
        tags:
          - { name: tactician.handler, command: Leos\Application\UseCase\Wallet\Request\Find }
```

## File: `src/Infrastructure/WalletBundle/Resources/config/persistence/Factory/WalletFactory.orm.yml`
```yaml
Leos\Domain\Wallet\Factory\WalletFactory:
    type: entity
```

## File: `src/Infrastructure/WalletBundle/Resources/config/persistence/Model/Wallet.orm.yml`
```yaml
Leos\Domain\Wallet\Model\Wallet:
    type: entity
    table: wallet
    repositoryClass: Leos\Infrastructure\WalletBundle\Repository\WalletRepository
    id:
      id:
        type: walletId
        nullable: false

    fields:
      createdAt:
        type: datetime

      updatedAt:
        type: datetime
        nullable: true

    embedded:
      real:
        class: Leos\Domain\Wallet\ValueObject\Credit

      bonus:
        class: Leos\Domain\Wallet\ValueObject\Credit

    manyToOne:
      user:
        targetEntity: Leos\Domain\User\Model\User
        joinColumn:
          name: user
          referencedColumnName: uuid
          nullable: false
          onDelete: CASCADE
        cascade:
          - all

    lifecycleCallbacks: {  }
```

## File: `src/Infrastructure/WalletBundle/Resources/config/persistence/ValueObject/Credit.orm.yml`
```yaml
Leos\Domain\Wallet\ValueObject\Credit:
  type: embeddable
  fields:
    amount:
      type: integer
    generatedAt:
      type: datetime
```

## File: `src/Infrastructure/WalletBundle/Resources/config/serializer/money/ValueObject.Currency.yml`
```yaml
Leos\Domain\Money\ValueObject\Currency:
    exclusion_policy: ALL
    properties:
        code:
            expose: true
            groups: [Basic]
            serialized_name: code

        exchange:
            expose: true
            groups: [Basic]
            serialized_name: echange

```

## File: `src/Infrastructure/WalletBundle/Resources/config/serializer/wallet/Factory.WalletFactory.yml`
```yaml
Leos\Domain\Walelt\Factory\WalletFactory: {}
```

## File: `src/Infrastructure/WalletBundle/Resources/config/serializer/wallet/Model.Wallet.yml`
```yaml
Leos\Domain\Wallet\Model\Wallet:
    exclusion_policy: ALL
    properties:
        id:
            expose: true
            inline: true
            groups: [Basic]
            type: Leos\Domain\Wallet\ValueObject\WalletId

        real:
            expose: true
            groups: [Basic]
            type: Leos\Domain\Wallet\ValueObject\Credit

        bonus:
            expose: true
            groups: [Basic]
            type: Leos\Domain\Wallet\ValueObject\Credit

        createdAt:
            expose: true
            groups: [Basic]

        updatedAt:
            expose: true
            groups: [Basic]
```

## File: `src/Infrastructure/WalletBundle/Resources/config/serializer/wallet/ValueObject.Credit.yml`
```yaml
Leos\Domain\Wallet\ValueObject\Credit:
    exclusion_policy: ALL
    properties:
        amount:
            expose: true
            groups: [Basic]
        generatedAt:
            expose: true
            groups: [Basic]
```

## File: `src/Infrastructure/WalletBundle/Resources/config/serializer/wallet/ValueObject.WalletId.yml`
```yaml
Leos\Domain\Wallet\ValueObject\WalletId:
    exclusion_policy: ALL
    properties:
        uuid:
            expose: true
            groups: [Basic]
```

## File: `src/Infrastructure/WalletBundle/Resources/config/services/factory.yml`
```yaml
services:
```

## File: `src/Infrastructure/WalletBundle/Resources/config/services/repository.yml`
```yaml
services:
    Leos\Domain\Wallet\Repository\WalletRepositoryInterface:
        parent: leos.abstract.repository
        class: Leos\Infrastructure\WalletBundle\Repository\WalletRepository
        arguments:
            - Leos\Domain\Wallet\Model\Wallet
```

## File: `src/UI/RestBundle/LeosUIRestBundle.php`
```php
<?php

namespace Leos\UI\RestBundle;

use Symfony\Component\HttpKernel\Bundle\Bundle;

class LeosUIRestBundle extends Bundle
{
}
```

## File: `src/UI/RestBundle/Controller/AbstractBusController.php`
```php
<?php

namespace Leos\UI\RestBundle\Controller;

use League\Tactician\CommandBus;

abstract class AbstractBusController extends AbstractController
{
    /**
     * @var CommandBus
     */
    private $bus;

    /**
     * @var CommandBus
     */
    private $queryBus;

    public function __construct(CommandBus $bus, CommandBus $queryBus)
    {
        $this->bus = $bus;
        $this->queryBus = $queryBus;
    }

    /**
     * @param object $commandRequest
     * @return mixed
     */
    public function handle($commandRequest)
    {
        return $this->bus->handle($commandRequest);
    }

    /**
     * @param object $commandRequest
     * @return mixed
     */
    public function ask($commandRequest)
    {
        return $this->queryBus->handle($commandRequest);
    }
}
```

## File: `src/UI/RestBundle/Controller/AbstractController.php`
```php
<?php

namespace Leos\UI\RestBundle\Controller;

use FOS\RestBundle\View\View;
use FOS\RestBundle\Controller\ControllerTrait;
use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\HttpFoundation\RequestStack;

/**
 * Class AbstractController
 *
 * @package Leos\UI\RestBundle\Controller
 */
abstract class AbstractController
{
    use ControllerTrait;

    /**
     * @var RequestStack $requestStack
     */
    private $requestStack;

    /**
     * @param RequestStack $requestStack
     */
    public function setRequestStack(RequestStack $requestStack)
    {
        $this->requestStack = $requestStack;
    }
    
    /**
     * @param string $route
     * @param array $parameters
     * @param int $statusCode
     * @param array $headers
     * @return \FOS\RestBundle\View\View
     */
    protected function routeRedirectView(
        $route,
        array $parameters = [],
        $statusCode = Response::HTTP_CREATED,
        array $headers = [])
    {
        return View::createRouteRedirect(
            $route,
            array_merge([
                'version' => $this->getVersion(),
                '_format' => $this->getFormat()
            ],
                $parameters
            ),
            $statusCode,
            $headers
        );
    }

    /**
     * @return string
     */
    public function getFormat(): string
    {
        return $this->getRequest()->getRequestFormat('json');
    }

    /**
     * @return string
     */
    public function getVersion(): string
    {
        return $this->getRequest()->attributes->get('version') ?: 'v1';
    }

    /**
     * @return null|\Symfony\Component\HttpFoundation\Request
     */
    protected function getRequest(): ?Request
    {
        return $this->requestStack->getMasterRequest();
    }
}
```

## File: `src/UI/RestBundle/Controller/Home/HomeController.php`
```php
<?php

namespace Leos\UI\RestBundle\Controller\Home;

use Nelmio\ApiDocBundle\Annotation\ApiDoc;
use FOS\RestBundle\Controller\Annotations\RouteResource;

use Leos\UI\RestBundle\Controller\AbstractController;

use Symfony\Bundle\FrameworkBundle\Routing\Router;
use Symfony\Component\Routing\Generator\UrlGeneratorInterface;

/**
 * Class HomeController
 *
 * @package Leos\Leos\UI\RestBundle\Controller\Home
 *
 * @RouteResource("", pluralize=false)
 */
class HomeController extends AbstractController
{
    /**
     * @var Router
     */
    private $router;

    public function __construct(Router $router)
    {
        $this->router = $router;
    }
    
    /**
     * @ApiDoc(
     *     resource = true,
     *     section="Home",
     *     description = "Home",
     *     statusCodes = {
     *       200 = "Returned when successful"
     *     }
     * )
     *
     * @return array
     */
    public function getAction(): array
    {
        return [
            'wallet' => $this->route('cget_wallet')
        ];
    }

    private function route(string $routeName): string
    {
        return  $this->router->generate(
            $routeName,
            [
                'version' => $this->getVersion()
            ],
            UrlGeneratorInterface::ABSOLUTE_URL
        );
    }

}
```

## File: `src/UI/RestBundle/Controller/Monitor/StatusController.php`
```php
<?php

namespace Leos\UI\RestBundle\Controller\Monitor;

use Leos\UI\RestBundle\Controller\AbstractController;

use Nelmio\ApiDocBundle\Annotation\ApiDoc;
use FOS\RestBundle\Controller\Annotations\RouteResource;

/**
 * Class StatusController
 *
 * @package Leos\UI\RestBundle\Controller\Monitor
 *
 * @RouteResource("Monitor")
 */
class StatusController extends AbstractController
{
    /**
     * @ApiDoc(
     *     resource = true,
     *     section="Monitor",
     *     description = "Ping status",
     *     statusCodes = {
     *       200 = "Returned when successful"
     *     }
     * )
     *
     * @return string
     */
    public function getPingAction(): string
    {
        return "pong";
    }
}
```

## File: `src/UI/RestBundle/Controller/Rollback/RollbackController.php`
```php
<?php

namespace Leos\UI\RestBundle\Controller\Rollback;

use Leos\UI\RestBundle\Controller\AbstractBusController;

use Leos\Application\UseCase\Transaction\Request\RollbackDeposit as RollbackDepositRequest;
use Leos\Application\UseCase\Transaction\Request\RollbackWithdrawal as RollbackWithdrawalRequest;

use Leos\Domain\Payment\Model\RollbackDeposit;
use Leos\Domain\Payment\Model\RollbackWithdrawal;

use Nelmio\ApiDocBundle\Annotation\ApiDoc;

use FOS\RestBundle\Request\ParamFetcher;
use FOS\RestBundle\Controller\Annotations\View;
use FOS\RestBundle\Controller\Annotations\RequestParam;
use FOS\RestBundle\Controller\Annotations\RouteResource;

/**
 * Class RollbackController
 *
 * @package Leos\UI\RestBundle\Controller\Rollback
 *
 * @RouteResource("Rollback", pluralize=false)
 */
class RollbackController extends AbstractBusController
{
    /**
     * @ApiDoc(
     *     resource = true,
     *     section="Rollback",
     *     description = "Rollback the given deposit",
     *     statusCodes = {
     *       202 = "Returned when successful",
     *       400 = "Returned when Bad request",
     *       404 = "Returned when not found"
     *     }
     * )
     *
     * @RequestParam(name="deposit", description="Deposit identifier")
     *
     * @View(statusCode=202, serializerGroups={"Identifier", "Basic"})
     *
     * @param ParamFetcher $fetcher
     *
     * @return RollbackDeposit
     */
    public function postDepositAction(ParamFetcher $fetcher): RollbackDeposit
    {
        return $this->handle(
            new RollbackDepositRequest($fetcher->get('deposit'))
        );
    }

    /**
     * @ApiDoc(
     *     resource = true,
     *     section="Rollback",
     *     description = "Rollback the given withdrawal",
     *     statusCodes = {
     *       202 = "Returned when successful",
     *       400 = "Returned when Bad request",
     *       404 = "Returned when not found"
     *     }
     * )
     *
     * @RequestParam(name="withdrawal", description="Withdrawal identifier")
     *
     * @View(statusCode=202, serializerGroups={"Identifier", "Basic"})
     *
     * @param ParamFetcher $fetcher
     *
     * @return RollbackWithdrawal
     */
    public function postWithdrawalAction(ParamFetcher $fetcher): RollbackWithdrawal
    {
        return $this->handle(
            new RollbackWithdrawalRequest($fetcher->get('withdrawal'))
        );
    }
}
```

## File: `src/UI/RestBundle/Controller/Security/SecurityController.php`
```php
<?php

namespace Leos\UI\RestBundle\Controller\Security;

use Leos\Domain\Security\Exception\AuthenticationException;
use Leos\Domain\User\ValueObject\UserId;
use Leos\UI\RestBundle\Controller\AbstractBusController;

use Leos\Application\UseCase\User\Request\Register;
use Leos\Application\UseCase\Security\Request\Login;

use Leos\Domain\User\Model\User;

use Leos\Infrastructure\CommonBundle\Exception\Form\FormException;

use FOS\RestBundle\Request\ParamFetcher;
use FOS\RestBundle\Controller\Annotations\View;
use FOS\RestBundle\Controller\Annotations\RequestParam;
use FOS\RestBundle\Controller\Annotations\RouteResource;

use Nelmio\ApiDocBundle\Annotation\ApiDoc;

use Doctrine\DBAL\Exception\UniqueConstraintViolationException;

use Symfony\Component\HttpKernel\Exception\ConflictHttpException;

/**
 * Class SecurityController
 *
 * @package Leos\UI\RestBundle\Controller\Security
 *
 * @RouteResource("Auth", pluralize=false)
 */
class SecurityController extends AbstractBusController
{
    /**
     * @ApiDoc(
     *     resource = true,
     *     section="Public",
     *     description = "Login a user on the system",
     *     statusCodes = {
     *       200 = "Returned when successful"
     *     }
     * )
     *
     * @RequestParam(name="_username", description="Unique username identifier")
     * @RequestParam(name="_password", description="User plain password")
     *
     * @View(statusCode=200)
     *
     * @param ParamFetcher $fetcher
     *
     * @throws AuthenticationException
     *
     * @return array
     */
    public function postLoginAction(ParamFetcher $fetcher): array
    {
        return [
            'token' => $this->handle(
                new Login(
                    $fetcher->get('_username'),
                    $fetcher->get('_password')
                )
            )
        ];
    }


    /**
     * @ApiDoc(
     *     resource = true,
     *     section="Public",
     *     description = "Register a user on the system",
     *     output = "Leos\Domain\User\Model\User",
     *     statusCodes = {
     *       201 = "Returned when successful",
     *       400 = "Returned when bad request",
     *       409 = "Returned when already exist"
     *     }
     * )
     *
     * @RequestParam(name="username", strict=false, default="", description="Unique username")
     * @RequestParam(name="email", strict=false, default="", description="Unique email")
     * @RequestParam(name="password", strict=false, default="", description="Plain password")
     *
     * @View(statusCode=201, serializerGroups={"Identifier", "Basic"})
     *
     * @param ParamFetcher $fetcher
     *
     * @return \Symfony\Component\Form\FormInterface|\FOS\RestBundle\View\View
     */
    public function postRegisterAction(ParamFetcher $fetcher)
    {
        try {

            /** @var User $user */
            $user = $this->handle(
                new Register(
                    new UserId(),
                    $fetcher->get('username'),
                    $fetcher->get('email'),
                    $fetcher->get('password')
                )
            );

            return $this
                ->routeRedirectView(
                    'get_user',
                    [
                        'uuid' => $user->uuid()->__toString()
                    ]
                )
                ->setData($user)
            ;
        } catch (FormException $e) {

            return $e->getForm();

        } catch (UniqueConstraintViolationException $e) {

            throw new ConflictHttpException('user.exception.already_exist');
        }
    }
}
```

## File: `src/UI/RestBundle/Controller/User/UserController.php`
```php
<?php

namespace Leos\UI\RestBundle\Controller\User;

use Leos\Application\UseCase\User\Request\GetUser;

use Leos\Domain\User\Model\User;

use Leos\UI\RestBundle\Controller\AbstractBusController;
use Nelmio\ApiDocBundle\Annotation\ApiDoc;

use FOS\RestBundle\Controller\Annotations\View;
use FOS\RestBundle\Controller\Annotations\RouteResource;

/**
 * Class UserController
 *
 * @RouteResource("User", pluralize=false)
 *
 * @package Leos\UI\RestBundle\Controller\User
 */
class UserController extends AbstractBusController
{
    /**
     * @ApiDoc(
     *     resource = true,
     *     section="User",
     *     description = "Gets a user for the given identifier",
     *     output = "Leos\Domain\User\Model\User",
     *     statusCodes = {
     *       200 = "Returned when successful",
     *       404 = "Returned when not found"
     *     }
     * )
     *
     * @View(statusCode=200)
     *
     * @param string $uuid
     * @return User
     */
    public function getAction(string $uuid): User
    {
        return $this->ask(new GetUser($uuid));
    }
}
```

## File: `src/UI/RestBundle/Controller/Wallet/WalletController.php`
```php
<?php

namespace Leos\UI\RestBundle\Controller\Wallet;

use Leos\Domain\Payment\Model\Deposit;
use Leos\Infrastructure\CommonBundle\Exception\Form\FormException;
use Leos\UI\RestBundle\Controller\AbstractBusController;

use Leos\Application\UseCase\Wallet\Request\Find;
use Leos\Application\UseCase\Wallet\Request\GetWallet;
use Leos\Application\UseCase\Transaction\Request\CreateDeposit;
use Leos\Application\UseCase\Transaction\Request\Withdrawal;
use Leos\Application\UseCase\Transaction\Request\CreateWallet;


use Leos\Domain\Wallet\Model\Wallet;
use Leos\Domain\Payment\Model\Withdrawal as WithdrawalModel;
use Leos\Infrastructure\CommonBundle\Pagination\PagerTrait;

use Nelmio\ApiDocBundle\Annotation\ApiDoc;

use Hateoas\Representation\PaginatedRepresentation;

use FOS\RestBundle\Request\ParamFetcher;
use FOS\RestBundle\Controller\Annotations\View;
use FOS\RestBundle\Controller\Annotations\QueryParam;
use FOS\RestBundle\Controller\Annotations\RequestParam;
use FOS\RestBundle\Controller\Annotations\RouteResource;

use Symfony\Component\Form\Form;

/**
 * Class WalletController
 *
 * @package Leos\UI\RestBundle\Controller\Wallet
 *
 * @RouteResource("Wallet", pluralize=false)
 */
class WalletController extends AbstractBusController
{
    use PagerTrait;

    /**
     * @ApiDoc(
     *     resource = true,
     *     section="Wallet",
     *     description = "List wallet collection",
     *     output = "Leos\Domain\Wallet\Model\Wallet",
     *     statusCodes = {
     *       201 = "Returned when successful",
     *       400 = "Returned when Bad Request",
     *       404 = "Returned when page not found"
     *     }
     * )
     *
     * @QueryParam(
     *     name="page",
     *     default="1",
     *     description="Page Number"
     * )
     * @QueryParam(
     *     name="limit",
     *     default="500",
     *     description="Items per page"
     * )
     *
     * @QueryParam(
     *     name="orderParameter",
     *     nullable=true,
     *     requirements="(real.amount|bonus.amount|createdAt|updatedAt)",
     *     map=true,
     *     description="Order Parameter"
     * )
     *
     * @QueryParam(
     *     name="orderValue",
     *     nullable=true,
     *     requirements="(ASC|DESC)",
     *     map=true,
     *     description="Order Value"
     * )
     *
     * @QueryParam(
     *     name="filterParam",
     *     nullable=true,
     *     requirements="(real.amount|bonus.amount|createdAt|updatedAt)",
     *     strict=true,
     *     map=true,
     *     description="Keys to filter"
     * )
     *
     * @QueryParam(
     *     name="filterOp",
     *     nullable=true,
     *     requirements="(gt|gte|lt|lte|eq|like|between)",
     *     strict=true,
     *     map=true,
     *     description="Operators to filter"
     * )
     *
     * @QueryParam(
     *     name="filterValue",
     *     map=true,
     *     description="Values to filter"
     * )
     *
     * @View(statusCode=200, serializerGroups={"Default", "Identifier", "Basic"})
     *
     * @param ParamFetcher $fetcher
     *
     * @return PaginatedRepresentation
     */
    public function cgetAction(ParamFetcher $fetcher): PaginatedRepresentation
    {
        $request = new Find($fetcher->all());

        return $this->getPagination(
            $this->ask($request),
            'cget_wallet',
            [],
            $request->getLimit(),
            $request->getPage()
        );
    }

    /**
     * @ApiDoc(
     *     resource = true,
     *     section="Wallet",
     *     description = "Gets a wallet for the given identifier",
     *     output = "Leos\Domain\Wallet\Model\Wallet",
     *     statusCodes = {
     *       200 = "Returned when successful",
     *       404 = "Returned when not found"
     *     }
     * )
     *
     * @View(statusCode=200, serializerGroups={"Identifier", "Basic"})
     *
     * @param string $walletId
     *
     * @return Wallet
     */
    public function getAction(string $walletId): Wallet
    {
        return $this->ask(new GetWallet($walletId));
    }

    /**
     * @ApiDoc(
     *     resource = true,
     *     section="Wallet",
     *     description = "Create a new Wallet",
     *     output = "Leos\Domain\Wallet\Model\Wallet",
     *     statusCodes = {
     *       201 = "Returned when successful"
     *     }
     * )
     *
     * @RequestParam(name="userId",   default="none", description="The user identifier")
     * @RequestParam(name="currency", default="EUR",  description="The currency of the wallet")
     *
     * @View(statusCode=201)
     *
     * @param ParamFetcher $fetcher
     *
     * @return \FOS\RestBundle\View\View|Form
     */
    public function postAction(ParamFetcher $fetcher)
    {
        try {
            /** @var Wallet $wallet */
            $wallet = $this->handle(
                new CreateWallet(
                    $fetcher->get('userId'),
                    $fetcher->get('currency')
                )
            );
        } catch (FormException $exception) {

            return $exception->getForm();
        }

        return $this->routeRedirectView('get_wallet', [ 'walletId' => $wallet->id() ]);
    }

    /**
     * @ApiDoc(
     *     resource = true,
     *     section="Wallet",
     *     description = "Generate a positive insertion on the given Wallet",
     *     output = "Leos\Domain\Debit\Model\Debit",
     *     statusCodes = {
     *       202 = "Returned when successful",
     *       400 = "Returned when bad request",
     *       404 = "Returned when wallet not found"
     *     }
     * )
     *
     * @RequestParam(name="real",     default="0",   description="Deposit amount")
     * @RequestParam(name="currency", default="EUR", description="Currency")
     * @RequestParam(name="provider", default="", description="Payment provider")
     *
     * @View(statusCode=202, serializerGroups={"Identifier", "Basic"})
     *
     * @param string $uid
     * @param ParamFetcher $fetcher
     *
     * @return Deposit
     */
    public function postDepositAction(string $uid, ParamFetcher $fetcher): Deposit
    {
        return $this->handle(
            new CreateDeposit(
                $uid,
                $fetcher->get('currency'),
                (float) $fetcher->get('real'),
                $fetcher->get('provider')
            )
        );
    }

    /**
     * @ApiDoc(
     *     resource = true,
     *     section="Wallet",
     *     description = "Generate a negative insertion on the given Wallet",
     *     output = "Leos\Domain\Payment\Model\Withdrawal",
     *     statusCodes = {
     *       202 = "Returned when successful",
     *       400 = "Returned when bad request",
     *       404 = "Returned when wallet not found",
     *       409 = "Returned when not enough founds"
     *     }
     * )
     *
     * @RequestParam(name="real",     default="0",  description="Withdrawal amount")
     * @RequestParam(name="currency", default="EUR", description="Currency")
     * @RequestParam(name="provider", default="", description="Payment provider")
     *
     * @View(statusCode=202, serializerGroups={"Identifier", "Basic"})
     *
     * @param string $uid
     * @param ParamFetcher $fetcher
     *
     * @return WithdrawalModel
     */
    public function postWithdrawalAction(string $uid, ParamFetcher $fetcher): WithdrawalModel
    {
        return $this->handle(
            new Withdrawal(
                $uid,
                $fetcher->get('currency'),
                (float) $fetcher->get('real'),
                $fetcher->get('provider')
            )
        );
    }
}
```

## File: `src/UI/RestBundle/DependencyInjection/LeosUIRestExtension.php`
```php
<?php

namespace Leos\UI\RestBundle\DependencyInjection;

use Symfony\Component\DependencyInjection\ContainerBuilder;
use Symfony\Component\Config\FileLocator;
use Symfony\Component\HttpKernel\DependencyInjection\Extension;
use Symfony\Component\DependencyInjection\Loader;

/**
 * This is the class that loads and manages your bundle configuration.
 *
 * @link http://symfony.com/doc/current/cookbook/bundles/extension.html
 */
class LeosUIRestExtension extends Extension
{
    /**
     * {@inheritdoc}
     */
    public function load(array $configs, ContainerBuilder $container)
    {
        $loader = new Loader\YamlFileLoader($container, new FileLocator(__DIR__.'/../Resources/config'));
        $loader->load('services.yml');
    }
}
```

## File: `src/UI/RestBundle/Resources/config/routing.yml`
```yaml
user:
    type: rest
    resource: leos.controller.user

wallet:
    type: rest
    resource: leos.controller.wallet

rollback:
    type: rest
    resource: leos.controller.wallet_rollback
```

## File: `src/UI/RestBundle/Resources/config/routing_public.yml`
```yaml
home:
    type: rest
    resource: leos.controller.home

monitor:
    type: rest
    resource: leos.controller.monitor

security:
    type: rest
    resource: leos.controller.security
```

## File: `src/UI/RestBundle/Resources/config/services.yml`
```yaml
imports:
    - { resource: services/common.yml }

services:

    leos.controller.home:
      class: Leos\UI\RestBundle\Controller\Home\HomeController
      parent: leos.abstract.controller
      arguments:
        - "@fos_rest.router"

    leos.controller.security:
      class: Leos\UI\RestBundle\Controller\Security\SecurityController
      parent: leos.abstract.bus_controller

    leos.controller.monitor:
      class: Leos\UI\RestBundle\Controller\Monitor\StatusController
      parent: leos.abstract.controller

    leos.controller.wallet:
      class: Leos\UI\RestBundle\Controller\Wallet\WalletController
      parent: leos.abstract.bus_controller


    leos.controller.wallet_rollback:
      class: Leos\UI\RestBundle\Controller\Rollback\RollbackController
      parent: leos.abstract.bus_controller

    leos.controller.user:
      class: Leos\UI\RestBundle\Controller\User\UserController
      parent: leos.abstract.bus_controller
```

## File: `src/UI/RestBundle/Resources/config/services/common.yml`
```yaml
services:
    leos.abstract.controller:
        abstract: true
        calls:
          - [ setRequestStack, ["@request_stack"]]

    leos.abstract.bus_controller:
        abstract: true
        parent: leos.abstract.controller
        arguments:
          - "@tactician.commandbus"
          - "@tactician.commandbus.query"
```

## File: `tests/Application/Request/Wallet/CreateWalletDTOTest.php`
```php
<?php

namespace Tests\Leos\Application\Request\Wallet;

use Leos\Application\UseCase\Transaction\Request\CreateWallet;
use PHPUnit\Framework\TestCase;
use Ramsey\Uuid\Uuid;


/**
 * Class CreateWalletDTOTest
 *
 * @package Tests\Leos\Application\DTO\Wallet
 */
class CreateWalletDTOTest extends TestCase
{
    /**
     * @group unit
     */
    public function testGetters()
    {
        $dto = new CreateWallet(Uuid::uuid4(), 'EUR');

        self::assertEquals('EUR', $dto->currency()->code());
    }

    /**
     * @group unit
     *
     * @expectedException Leos\Domain\Money\Exception\CurrencyWrongCodeException
     */
    public function testConstructWrongCurrency()
    {
        new CreateWallet(Uuid::uuid4(), 'EURAZO');
    }
}
```

## File: `tests/Application/UseCase/Transaction/TransactionCommandTest.php`
```php
<?php

namespace Tests\Leos\Application\UseCase\Transaction;

use Lakion\ApiTestCase\JsonApiTestCase;
use Leos\Application\UseCase\Transaction\Request\CreateWallet;
use Leos\Domain\Transaction\Repository\TransactionRepositoryInterface;
use Leos\Domain\User\Model\User;
use Leos\Domain\User\Repository\UserRepositoryInterface;

use Leos\Domain\Wallet\Model\Wallet;
use Leos\Domain\Wallet\Repository\WalletRepositoryInterface;
use Tests\Leos\Domain\User\Model\UserTest;

/**
 * Class TransactionCommandTest
 */
class TransactionCommandTest extends JsonApiTestCase
{
    private $fixture = [];

    public function setUp()
    {
        $this->setUpClient();

        $repo = self::getMockBuilder(TransactionRepositoryInterface::class)
            ->setMethods(['save', 'get'])->getMock();

        $userRepo = self::getMockBuilder(UserRepositoryInterface::class)
            ->setMethods(['save', 'getOneByUuid', 'findOneByUuid', 'findOneByUsername']);

        $mock = $userRepo->getMock();

        $this->fixture['user'] = UserTest::create();

        $mock->method('findOneByUuid')->with((string) $this->fixture['user']->uuid())->willReturn($this->fixture['user']);

        $walletRepo = self::getMockBuilder(WalletRepositoryInterface::class)
            ->setMethods(['save', 'get', 'findOneById', 'findAll'])->getMock();

        $container = $this->client->getContainer();

        $container->set('Leos\Domain\Wallet\Repository\WalletRepositoryInterface', $walletRepo);
        $container->set('Leos\Domain\Transaction\Repository\TransactionRepositoryInterface', $repo);
        $container->set('Leos\Domain\User\Repository\UserRepositoryInterface', $mock);
    }

    /**
     * @group functional
     */
    public function testShouldCreateTransactionWithNewWallet()
    {
        /** @var User $user */
        $user = $this->fixture['user'];
        $result = $this->get('tactician.commandbus')->handle(new CreateWallet((string) $user->uuid(), 'EUR'));

        self::assertInstanceOf(Wallet::class, $result);
        self::assertTrue($result->user()->uuid()->equals($user->uuid()));
        self::assertEquals(0, $result->real()->amount());
        self::assertEquals(0, $result->bonus()->amount());
    }
}
```

## File: `tests/Domain/Common/Event/EventCollectorTest.php`
```php
<?php

namespace Tests\Leos\Domain\Common\Event;

use Leos\Domain\Common\Event\EventCollector;
use Leos\Domain\User\Event\UserWasCreated;
use Leos\Domain\User\ValueObject\UserId;
use PHPUnit\Framework\TestCase;

class EventCollectorTest extends TestCase
{
    public function setUp()
    {
        $this->tearDown();
        EventCollector::instance()->flush();
    }

    public function testEventIsStored()
    {
        $collector = $this->userCreated();

        $events = $collector->events();

        self::assertEquals('UserWasCreated', $events[0]->type());
    }

    public function testEventFlushCleanAll()
    {
        $collector = $this->userCreated();

        $events = $collector->events();

        $collector->flush();

        self::assertNotEquals(count($events), $collector->events());
    }

    private function userCreated(): EventCollector
    {
        $collector = EventCollector::instance();

        $collector->collect(new UserWasCreated(new UserId(), 'paco', 'paso@pas.com'));

        return $collector;
    }

    public function tearDown()
    {
        EventCollector::instance()->shutdown();
    }
}
```

## File: `tests/Domain/Common/Event/EventPublisherTest.php`
```php
<?php

namespace Tests\Leos\Domain\Common\Event;

use Leos\Domain\Common\Event\EventCollector;
use Leos\Domain\Common\Event\EventDispatcherInterface;
use Leos\Domain\Common\Event\EventPublisher;
use Leos\Domain\User\Event\UserWasCreated;
use Leos\Domain\User\ValueObject\UserId;
use Symfony\Bundle\FrameworkBundle\Test\KernelTestCase;

class EventPublisherTest extends KernelTestCase
{
    /**
     * @var EventDispatcherInterface
     */
    private $dispatcher;

    public function setUp()
    {
        $this->dispatcher = self::bootKernel()
            ->getContainer()
            ->get('Leos\Domain\Common\Event\EventDispatcherInterface')
        ;
    }

    public function testRaiseEventShouldBeRecorded()
    {
        EventPublisher::boot($this->dispatcher);

        EventPublisher::raise(new UserWasCreated(new UserId(), 'paco', 'paco@a.com'));

        $events = EventCollector::instance()->events();

        self::assertCount(1, $events);
        self::assertInstanceOf(UserWasCreated::class, $events[0]);
    }
}
```

## File: `tests/Domain/Common/ValueObject/AggregateRootIdTest.php`
```php
<?php

namespace Tests\Leos\Domain\Common\ValueObject;

use Leos\Domain\User\ValueObject\UserId;
use PHPUnit\Framework\TestCase;

/**
 * Class AggregateRootIdTest
 *
 * @package Leos\Domain\Common\ValueObject
 */
class AggregateRootIdTest extends TestCase
{
    /**
     * @group unit
     */
    public function testEquals()
    {
        $uuid = new UserId();
        $uuid2 = new UserId();
        $uuid3 = new UserId((string) $uuid);

        self::assertTrue($uuid->equals($uuid3));
        self::assertFalse($uuid->equals($uuid2));
    }

    /**
     * @group unit
     *
     * @expectedException Leos\Domain\Common\Exception\InvalidUUIDException
     */
    public function testWrongUUId()
    {
        new UserId(21);
    }
}
```

## File: `tests/Domain/Money/ValueObject/CurrencyTest.php`
```php
<?php

namespace Tests\Leos\Domain\Money\ValueObject;

use Leos\Domain\Money\ValueObject\Currency;
use Leos\Domain\Money\Exception\CurrencyWrongCodeException;
use PHPUnit\Framework\TestCase;

/**
 * Class CurrencyTest
 *
 * @package Tests\Leos\Domain\Money\ValueObject
 */
class CurrencyTest extends TestCase
{
    /**
     * @group unit
     */
    public function testCurrencyBadCode()
    {
        try{
            
            new Currency('EURO', 3);

        } catch (CurrencyWrongCodeException $e) {
            
            self::assertGreaterThan(5000, $e->getCode());
        }
    }

    /**
     * @group unit
     */
    public function testCurrencyGetters()
    {
        $currency = new Currency('EUR', 1);

        self::assertEquals('EUR', $currency->code());
        self::assertEquals(1, $currency->exchange());
    }

    /**
     * @group unit
     */
    public function testCurrencyEqual()
    {
        $currency = new Currency('EUR', 1);
        $currency2 = new Currency('EUR', 1);
        $currency3 = new Currency('EUR', 3);
        $currency4 = new Currency('GBP', 8);

        self::assertTrue($currency->equals($currency2));
        self::assertFalse($currency->equals($currency3));
        self::assertFalse($currency->equals($currency4));
    }

}
```

## File: `tests/Domain/Money/ValueObject/MoneyTest.php`
```php
<?php

namespace Tests\Leos\Domain\Money\ValueObject;

use Leos\Domain\Money\ValueObject\Money;
use Leos\Domain\Money\ValueObject\Currency;
use PHPUnit\Framework\TestCase;

/**
 * Class MoneyTest
 * @package Tests\Leos\Domain\Money\ValueObject
 */
class MoneyTest extends TestCase
{
    /**
     * @group unit
     */
    public function testMoneyGetters()
    {
        $money = new Money(100, $currency = new Currency('EUR', 1));

        self::assertEquals(100, $money->amount());
        self::assertEquals($currency, $money->currency());
    }
}
```

## File: `tests/Domain/Payment/Model/DepositTest.php`
```php
<?php

namespace Tests\Leos\Domain\Payment\Model;

use Leos\Domain\Payment\Model\Deposit;
use Leos\Domain\Payment\Model\RollbackDeposit;
use Leos\Domain\Payment\ValueObject\DepositDetails;
use Leos\Domain\Wallet\Model\Wallet;
use Leos\Domain\Money\ValueObject\Money;
use Leos\Domain\Money\ValueObject\Currency;
use Leos\Domain\Transaction\Model\AbstractTransaction;
use PHPUnit\Framework\TestCase;
use Tests\Leos\Domain\User\Model\UserTest;
use Tests\Leos\Domain\Wallet\Model\WalletTest;

/**
 * Class DepositTest
 *
 * @package Leos\Domain\Payment\Model
 */
class DepositTest extends TestCase
{
    /**
     * @group unit
     */
    public function testConstruct()
    {
        $transaction = new Deposit(
            WalletTest::create(),
            new Money(10, new Currency('EUR', 1)),
            new DepositDetails('paypal')
        );

        self::assertInstanceOf(AbstractTransaction::class, $transaction);
        self::assertEquals(1000, $transaction->wallet()->real()->amount());
        self::assertInstanceOf(RollbackDeposit::class, $transaction->rollback());
        self::assertInstanceOf(DepositDetails::class, $transaction->details());
    }
}
```

## File: `tests/Domain/Payment/Model/RollbackDepositTest.php`
```php
<?php

namespace Tests\Leos\Domain\Payment\Model;

use Leos\Domain\Payment\Model\Deposit;
use Leos\Domain\Payment\Model\RollbackDeposit;
use Leos\Domain\Payment\ValueObject\DepositDetails;
use Leos\Domain\Wallet\Model\Wallet;
use Leos\Domain\Money\ValueObject\Money;
use Leos\Domain\Money\ValueObject\Currency;
use Leos\Domain\Transaction\Model\AbstractTransaction;
use PHPUnit\Framework\TestCase;
use Tests\Leos\Domain\Wallet\Model\WalletTest;

/**
 * Class RollbackDepositTest
 * 
 * @package Leos\Domain\Payment\Model
 */
class RollbackDepositTest extends TestCase
{
    /**
     * @group unit
     */
    public function testConstruct()
    {
        $transaction = new RollbackDeposit(
            new Deposit(
                WalletTest::create(),
                new Money(10, new Currency('EUR', 1)),
                new DepositDetails('paypal')
            )
        );

        self::assertInstanceOf(AbstractTransaction::class, $transaction);
        self::assertEquals(0, $transaction->wallet()->real()->amount());
    }
}
```

## File: `tests/Domain/Payment/Model/RollbackWithdrawalTest.php`
```php
<?php

namespace Tests\Leos\Domain\Payment\Model;

use Leos\Domain\Wallet\Model\Wallet;
use Leos\Domain\Money\ValueObject\Money;
use Leos\Domain\Money\ValueObject\Currency;
use Leos\Domain\Payment\Model\Withdrawal;
use Leos\Domain\Payment\Model\RollbackWithdrawal;
use Leos\Domain\Transaction\Model\AbstractTransaction;
use Leos\Domain\Payment\ValueObject\WithdrawalDetails;
use PHPUnit\Framework\TestCase;
use Tests\Leos\Domain\Wallet\Model\WalletTest;

/**
 * Class RollbackWithdrawalTest
 *
 * @package Tests\Leos\Domain\Payment\Model
 */
class RollbackWithdrawalTest extends TestCase
{
    /**
     * @group unit
     */
    public function testConstruct()
    {
        $wallet = WalletTest::create();

        $wallet->addRealMoney(new Money(50 ,$currency = new Currency('EUR', 1)));

        $transaction = new RollbackWithdrawal(
            new Withdrawal($wallet, new Money(50, $currency), new WithdrawalDetails('paypal'))
        );

        self::assertInstanceOf(AbstractTransaction::class, $transaction);
        self::assertInstanceOf(WithdrawalDetails::class, $transaction->details());
        self::assertEquals(5000, $transaction->wallet()->real()->amount());
    }
}
```

## File: `tests/Domain/Payment/Model/WithdrawalTest.php`
```php
<?php

namespace Tests\Leos\Domain\Payment\Model;

use Leos\Domain\Wallet\Model\Wallet;
use Leos\Domain\Money\ValueObject\Money;
use Leos\Domain\Money\ValueObject\Currency;
use Leos\Domain\Payment\Model\RollbackWithdrawal;
use Leos\Domain\Payment\Model\Withdrawal;
use Leos\Domain\Transaction\Model\AbstractTransaction;
use Leos\Domain\Payment\ValueObject\WithdrawalDetails;
use PHPUnit\Framework\TestCase;
use Tests\Leos\Domain\Wallet\Model\WalletTest;

/**
 * Class WithdrawalTest
 *
 * @package Tests\Leos\Domain\Payment\Model
 */
class WithdrawalTest extends TestCase
{
    /**
     * @group unit
     */
    public function testConstruct()
    {
        $wallet = WalletTest::create();

        $wallet->addRealMoney(new Money(50 ,$currency = new Currency('EUR', 1)));

        $transaction = new Withdrawal($wallet, new Money(50, $currency), new WithdrawalDetails('paypal'));

        self::assertInstanceOf(AbstractTransaction::class, $transaction);
        self::assertInstanceOf(WithdrawalDetails::class, $transaction->details());
        self::assertEquals(0, $transaction->wallet()->real()->amount());
        self::assertInstanceOf(RollbackWithdrawal::class, $transaction->rollback());
    }
}
```

## File: `tests/Domain/Payment/ValueObject/DepositDetailsTest.php`
```php
<?php

namespace Tests\Leos\Domain\Payment\ValueObject;

use Leos\Domain\Payment\Exception\InvalidProviderException;
use Leos\Domain\Payment\ValueObject\DepositDetails;
use PHPUnit\Framework\TestCase;

/**
 * Class DepositDetailsTest
 * 
 * @package Tests\Leos\Domain\Payment\ValueObject
 */
class DepositDetailsTest extends TestCase
{

    /**
     * @group unit
     */
    public function testGetters()
    {
        $details =  new DepositDetails('paypal');

        self::assertEquals('paypal', $details->provider());
    }


    /**
     * @group unit
     */
    public function testInvalidProvider()
    {
        self::expectException(InvalidProviderException::class);

        new DepositDetails('as');
    }
}
```

## File: `tests/Domain/Payment/ValueObject/WithdrawalDetailsTest.php`
```php
<?php

namespace Tests\Leos\Domain\Payment\ValueObject;

use Leos\Domain\Payment\Exception\InvalidProviderException;
use Leos\Domain\Payment\ValueObject\WithdrawalDetails;
use PHPUnit\Framework\TestCase;

/**
 * Class WithdrawalDetailsTest
 *
 * @package Tests\Leos\Domain\Payment\ValueObject
 */
class WithdrawalDetailsTest extends TestCase
{
    /**
     * @group unit
     */
    public function testGetters()
    {
        $details = new WithdrawalDetails('paypal');

        self::assertEquals('paypal', $details->provider());
    }

    /**
     * @group unit
     */
    public function testInvalidProvider()
    {
        self::expectException(InvalidProviderException::class);

        new WithdrawalDetails('as');
    }
}
```

## File: `tests/Domain/Transaction/Model/TransactionTest.php`
```php
<?php

namespace Tests\Leos\Domain\Transaction\Model;

use Leos\Domain\Payment\Model\Deposit;
use Leos\Domain\Payment\ValueObject\DepositDetails;
use Leos\Domain\Money\ValueObject\Currency;
use Leos\Domain\Money\ValueObject\Money;
use Leos\Domain\Transaction\ValueObject\TransactionType;
use Leos\Domain\Wallet\Model\Wallet;
use Leos\Domain\Wallet\ValueObject\Credit;
use Leos\Domain\Wallet\ValueObject\WalletId;
use PHPUnit\Framework\TestCase;
use Tests\Leos\Domain\Wallet\Model\WalletTest;

/**
 * Class TransactionTest
 *
 * @package Leos\Domain\Transaction\Model
 */
class TransactionTest extends TestCase
{
    /**
     * @group unit
     */
    public function testGetters()
    {
        $wallet = WalletTest::create();

        $currency = new Currency('EUR', 1);

        $transaction = new Deposit(
            $wallet,
            new Money(50.00, $currency),
            new DepositDetails('paypal')
        );

        self::assertTrue(null !== $transaction->uuid());
        self::assertEquals($wallet, $transaction->wallet());
        self::assertEquals(TransactionType::DEPOSIT, (string) $transaction->type());
        self::assertEquals(0, $transaction->prevReal()->amount());
        self::assertEquals(0, $transaction->prevBonus()->amount());
        self::assertEquals(5000, $transaction->operationReal());
        self::assertInstanceOf(Money::class, $transaction->realMoney());
        self::assertInstanceOf(Money::class, $transaction->bonusMoney());
        self::assertEquals(0, $transaction->operationBonus());
        self::assertNull($transaction->referralTransaction());
        self::assertEquals($currency->code(), $transaction->currency()->code());
        self::assertNotNull($transaction->createdAt());
        self::assertNull($transaction->updatedAt());
        self::assertNull($transaction->referralTransaction());
    }
}
```

## File: `tests/Domain/Transaction/ValueObject/TransactionTypeTest.php`
```php
<?php

namespace Tests\Leos\Domain\Transaction\ValueObject;

use Leos\Domain\Transaction\ValueObject\TransactionType;
use PHPUnit\Framework\TestCase;

/**
 * Class TransactionTypeTest
 *
 * @package Tests\Leos\Domain\Transaction\Model
 */
class TransactionTypeTest extends TestCase
{
    /**
     * @group unit
     */
    public function testTypes()
    {
        self::assertTrue(is_array(TransactionType::types()));
        self::assertTrue(in_array('deposit', TransactionType::types()));
        self::assertTrue(in_array('withdrawal', TransactionType::types()));
    }

    /**
     * @group unit
     */
    public function testGetters()
    {
        $type = new TransactionType(TransactionType::WITHDRAWAL);

        self::assertEquals(TransactionType::WITHDRAWAL, (string) $type);
    }

    /**
     * @group unit
     */
    public function testValidation()
    {
        self::assertFalse(TransactionType::isValid('Nigga'));
    }

    /**
     * @group unit
     */
    public function testConstructValidation()
    {
        try {

            new TransactionType('Nigga');

            self::assertTrue(false);

        } catch (\Exception $e) {

            self::assertTrue(true);
        }
    }
}
```

## File: `tests/Domain/User/Model/UserTest.php`
```php
<?php

namespace Tests\Leos\Domain\User\Model;

use Leos\Domain\Security\Exception\InvalidPasswordException;
use Leos\Domain\Security\Exception\NullPasswordException;
use Leos\Domain\User\Model\User;
use Leos\Domain\User\ValueObject\UserId;
use Leos\Infrastructure\SecurityBundle\ValueObject\EncodedPassword;
use PHPUnit\Framework\TestCase;

/**
 * Class UserTest
 *
 * @package Tests\Leos\Domain\User\Model
 */
class UserTest extends TestCase
{
    /**
     * @group unit
     */
    public function testGetters()
    {
        $user = new User(
            new UserId,
            $username = 'jorge',
            $email = 'jorge.arcoma@gmail.com',
            new EncodedPassword($password = 'iyoquease')
        );
        
        self::assertNotNull($user->uuid());
        self::assertNotNull($user->createdAt());
        self::assertNull($user->updatedAt());
        self::assertEquals($username, $user->auth()->username());
        self::assertEquals($email, $user->email());
        self::assertNotEquals($password, $user->auth()->password());
    }

    /**
     * @group unit
     */
    public function testMinPasswordLength()
    {
        self::expectException(InvalidPasswordException::class);

        new User(
            new UserId,
            'jorge',
            'jorge.arcoma@gmail.com',
            new EncodedPassword('iyoque')
        );
    }

    /**
     * @group unit
     */
    public function testNullPassword()
    {
        self::expectException(NullPasswordException::class);

        new User(
            new UserId,
            'jorge',
            'jorge.arcoma@gmail.com',
            new EncodedPassword(null)
        );
    }

    public static function create(string $name = null, string $email = null, string $pwd = null): User
    {
        return new User(
            new UserId,
            $name ?? 'jorge',
            $email ?? 'jorge.arcoma@gmail.com',
            new EncodedPassword($pwd ?? 'iyoquease')
        );
    }
}
```

## File: `tests/Domain/Wallet/Exception/Wallet/WalletNotFoundExceptionTest.php`
```php
<?php

namespace Tests\Leos\Domain\Wallet\Exception\Wallet;

use Leos\Domain\Wallet\Exception\Wallet\WalletNotFoundException;
use PHPUnit\Framework\TestCase;

/**
 * Class WalletNotFoundExceptionTest
 *
 * @package Tests\Leos\Domain\Wallet\Exception\Wallet
 */
class WalletNotFoundExceptionTest extends TestCase
{
    /**
     * @group unit
     */
    public function testGetters()
    {
        $e = new WalletNotFoundException();

        self::assertContains('not_found', $e->getMessage());
        self::assertGreaterThan(8000, $e->getCode());
        self::assertLessThan(9000, $e->getCode());
    }
}
```

## File: `tests/Domain/Wallet/Model/WalletTest.php`
```php
<?php

namespace Tests\Leos\Domain\Wallet\Model;

use Leos\Domain\Wallet\Model\Wallet;
use Leos\Domain\Wallet\ValueObject\Credit;
use Leos\Domain\Wallet\ValueObject\WalletId;
use Leos\Domain\Wallet\Exception\Credit\CreditNotEnoughException;

use Leos\Domain\Money\ValueObject\Money;
use Leos\Domain\Money\ValueObject\Currency;
use PHPUnit\Framework\TestCase;
use Tests\Leos\Domain\User\Model\UserTest;

/**
 * Class WalletTest
 *
 * @package Leos\Domain\Wallet\Model
 */
class WalletTest extends TestCase
{

    /**
     * @group unit
     */
    public function testWalletGetters()
    {
        $wallet = self::create();

        $real = new Credit(100);
        $bonus = new Credit(100);

        $currency = $this->getTestCurrency();

        $wallet->addRealMoney($real->toMoney($currency));
        $wallet->addBonusMoney($bonus->toMoney($currency));

        self::assertEquals(100, $wallet->real()->amount());
        self::assertEquals(100, $wallet->bonus()->amount());
        self::assertNotNull($wallet->createdAt());
        self::assertNull($wallet->updatedAt());
        self::assertInstanceOf(WalletId::class, $wallet->walletId());
        self::assertNotNull($wallet->id());
        self::assertNotNull($wallet->walletId()->__toString());
        self::assertNotNull($wallet->user());
    }

    /**
     * @group unit
     */
    public function testWalletAddCredit()
    {
        $wallet = self::create();

        $real = new Credit(100);
        $bonus = new Credit(100);

        $currency = $this->getTestCurrency();

        $wallet->addRealMoney($real->toMoney($currency));
        $wallet->addBonusMoney($bonus->toMoney($currency));
        $wallet->addRealMoney(new Money(2.50, $this->getTestCurrency()));

        self::assertNotSame($real, $wallet->real());
        self::assertFalse($real->equals($wallet->real()));

        self::assertEquals(350, $wallet->real()->amount());

        $wallet->addBonusMoney(new Money(2.50, $this->getTestCurrency()));

        self::assertNotSame($real, $wallet->bonus());
        self::assertFalse($real->equals($wallet->bonus()));

        self::assertEquals(350, $wallet->bonus()->amount());
    }

    /**
     * @group unit
     */
    public function testWalletRemoveCredit()
    {
        $wallet = self::create();

        $real = new Credit(350);
        $bonus = new Credit(350);

        $currency = $this->getTestCurrency();

        $wallet->addRealMoney($real->toMoney($currency));
        $wallet->addBonusMoney($bonus->toMoney($currency));

        $wallet->removeRealMoney(new Money(2.50, $this->getTestCurrency()));

        self::assertNotSame($real, $wallet->real());
        self::assertFalse($real->equals($wallet->real()));

        self::assertEquals(100, $wallet->real()->amount());

        $wallet->removeBonusMoney(new Money(2.50, $this->getTestCurrency()));

        self::assertNotSame($real, $wallet->bonus());
        self::assertFalse($real->equals($wallet->bonus()));

        self::assertEquals(100, $wallet->bonus()->amount());
    }

    /**
     * @group unit
     */
    public function testWalletFailWhenRemoveWithNotEnoughCredit()
    {
        try {

            $wallet = self::create();

            $real = new Credit(350);
            $bonus = new Credit(350);
            $currency = $this->getTestCurrency();

            $wallet->addRealMoney($real->toMoney($currency));
            $wallet->addBonusMoney($bonus->toMoney($currency));

            $wallet->removeRealMoney(new Money(8.50, $this->getTestCurrency()));

            self::assertEquals(true, false, "Remove money with not enough credit should throw an exception");

        } catch (\Exception $e) {

            self::assertGreaterThan(4000, $e->getCode());
            self::assertInstanceOf(CreditNotEnoughException::class, $e);
        }
    }

    /**
     * @return Currency
     */
    private function getTestCurrency(): Currency
    {
        return new Currency('EUR', 1);
    }

    public static function create(): Wallet
    {
        return new Wallet(UserTest::create());
    }
}
```

## File: `tests/Domain/Wallet/ValueObject/CreditTest.php`
```php
<?php

namespace Tests\Leos\Domain\Wallet\ValueObject;

use Leos\Domain\Wallet\ValueObject\Credit;
use PHPUnit\Framework\TestCase;

/**
 * Class CreditTest
 * @package Leos\Domain\Wallet\Model
 */
class CreditTest extends TestCase
{
    /**
     * @group unit
     */
    public function testCreditGetters()
    {
        $credit = new Credit(100);

        self::assertEquals(100, $credit->amount());
        self::assertEquals(100, (string) $credit);
        self::assertNotNull($credit->generatedAt());
    }
}
```

## File: `tests/Infrastructure/CommonBundle/Factory/FactoryTest.php`
```php
<?php

namespace Tests\Leos\Infrastructure\CommonBundle\Factory;

use Leos\Infrastructure\CommonBundle\Exception\Form\FormFactoryException;
use Symfony\Bundle\FrameworkBundle\Test\WebTestCase;
use Tests\Leos\Infrastructure\CommonBundle\Factory\Fixture\FixtureFactory;

/**
 * Class FactoryTest
 * @package Tests\Leos\Infrastructure\CommonBundle\Factory
 */
class FactoryTest extends WebTestCase
{

    /**
     * @group unit
     */
    public function testConstruct()
    {
        try {
            new FixtureFactory(self::createClient()->getContainer()->get('form.factory'));

            self::assertFalse(true, "exception not throw");
        } catch (FormFactoryException $exception) {

            self::assertTrue(true);
            return;
        }

        self::assertFalse(true, "exception not throw");
    }
}
```

## File: `tests/Infrastructure/CommonBundle/Factory/Fixture/FixtureFactory.php`
```php
<?php

namespace Tests\Leos\Infrastructure\CommonBundle\Factory\Fixture;

use Leos\Infrastructure\CommonBundle\Factory\AbstractFactory;

/**
 * Class FixtureFactory
 * @package Tests\Leos\Infrastructure\Common\Factory\Fixture
 */
class FixtureFactory extends AbstractFactory
{

}
```

## File: `tests/Infrastructure/UserBundle/SerializerIntegrationTest.php`
```php
<?php

namespace Tests\Leos\Infrastructure\UserBundle;

use JMS\Serializer\Serializer;
use Lakion\ApiTestCase\JsonApiTestCase;
use Tests\Leos\Domain\User\Model\UserTest;

class SerializerIntegrationTest extends JsonApiTestCase
{

    public function testUserSerialization()
    {
        $this->setUpClient();

        /** @var Serializer $serializer */
        $serializer = $this->client->getContainer()->get('jms_serializer');

        $serializedUser = $serializer->toArray(UserTest::create());

        self::assertNotNull($serializedUser['uuid']);
        self::assertArrayNotHasKey('auth', $serializedUser);
    }
}
```

## File: `tests/Infrastructure/UserBundle/Factory/Form/ChangePasswordTypeTest.php`
```php
<?php

namespace Tests\Leos\Infrastructure\UserBundle\Factory\Form;

use Lakion\ApiTestCase\JsonApiTestCase;
use Leos\Domain\User\Model\User;
use Leos\Infrastructure\UserBundle\Factory\Form\ChangePasswordType;
use Tests\Leos\Domain\User\Model\UserTest;

class ChangePasswordTypeTest extends JsonApiTestCase
{

    public function setUp()
    {
        self::setUpClient();
    }

    public function testChangePassword()
    {
        $user = UserTest::create();

        $originalPass = $user->auth()->password();

        $form = $this->client->getContainer()->get('form.factory')->create(ChangePasswordType::class, $user);

        $form->submit(['oldPassword' => 'iyoquease', 'newPassword' => 'iyoquease2']);
        /** @var User $user */
        $user = $form->getData();

        self::assertNotEquals($user->auth()->password(), $originalPass);
    }
}
```

## File: `tests/Infrastructure/WalletBundle/Doctrine/Types/WalletItTypeTest.php`
```php
<?php

namespace Tests\Leos\Infrastructure\WalletBundle\Doctrine\Types;

use Doctrine\DBAL\Types\Type;
use PHPUnit\Framework\TestCase;

/**
 * Class WalletItTypeTest
 *
 * @package Leos\Infrastructure\WalletBundle\Doctrine\Types
 */
class WalletItTypeTest extends TestCase
{
    /**
     * @group unit
     *
     * @throws \Doctrine\DBAL\DBALException
     */
    public function testType()
    {
        if (!Type::hasType('walletId')) { // Prevent error on cascade test execution

            Type::addType('walletId', 'Leos\Infrastructure\WalletBundle\Doctrine\Types\WalletIdType');
        }

        $type = Type::getType('walletId');

        self::assertEquals('walletId', $type->getName());
    }
}
```

## File: `tests/UI/Behat/Context/Api/ApiContext.php`
```php
<?php

namespace Tests\Leos\UI\Behat\Context\Api;

use Behat\Behat\Context\Context;
use GuzzleHttp\Client as Http;
use GuzzleHttp\RequestOptions;
use GuzzleHttp\Exception\ClientException;

use Psr\Http\Message\ResponseInterface;

use Lakion\ApiTestCase\JsonApiTestCase;

use Coduo\PHPMatcher\Matcher\Matcher;
use Coduo\PHPMatcher\Factory\SimpleFactory;

use Behat\Gherkin\Node\PyStringNode;

use Symfony\Bridge\PsrHttpMessage\Factory\HttpFoundationFactory;

/**
 * Class ApiContext
 *
 * @package Tests\Leos\Leos\UI\Behat\Context\Api
 */
class ApiContext extends JsonApiTestCase implements Context
{
    const
        FIXTURES = '/tests/UI/Fixtures',
        RESPONSES = '/tests/UI/Responses/'
    ;

    /**
     * @var Http
     */
    private $http;

    /**
     * @var array
     */
    private $options = [];

    /**
     * @var ResponseInterface
     */
    protected $response;

    /**
     * @var string
     */
    protected $resource;

    /**
     * @var Matcher
     */
    private $matcher;

    /**
     * @var HttpFoundationFactory
     */
    private $httpFoundationFactory;

    /**
     * @var array
     */
    private $placeholders = [];

    /**
     * ApiContext constructor.
     *
     * @param string $path
     * @param string $basePath
     * @param string $responsesPath
     * @param string $fixturesPath
     */
    public function __construct(string $path, string $basePath, string $responsesPath = null, string $fixturesPath = null)
    {
        $_SERVER['IS_DOCTRINE_ORM_SUPPORTED'] = true;
        $_SERVER['KERNEL_DIR'] = $basePath . '/app';
        $_SERVER['KERNEL_CLASS'] = 'AppKernel';
        parent::__construct();

        $this->http = new Http([
            // Base URI is used with relative requests
            'base_uri' => $path,
            'timeout'         => 5.0,
            'connect_timeout' => 2.5,
            'content-type' => 'application/json',
        ]);

        $this->bootKernel(['environment' => 'dev']);

        $this->dataFixturesPath = $fixturesPath ?: $basePath.self::FIXTURES;
        $this->expectedResponsesPath = $responsesPath ?: $basePath.self::RESPONSES;

        $this->matcher = (new SimpleFactory())->createMatcher();
        $this->httpFoundationFactory = new HttpFoundationFactory();
    }

    public function http(): Http
    {
        return $this->http;
    }

    /**
     * @param string $string
     *
     * @return string
     */
    final protected function placeholders(string $string): string
    {
        foreach($this->placeholders as $key => $value) {

            $string = str_replace('%' . $key . '%', $value, $string);
        }

        return $string;
    }

    /**
     * @param string $key
     * @param $value
     *
     * @return ApiContext
     */
    protected function addPlaceHolder(string $key, $value): self
    {
        $this->placeholders[$key] = $value;

        return $this;
    }

    /**
     * @param string $key
     *
     * @return ApiContext
     */
    protected function removePlaceHolder(string $key): self
    {
        unset($this->placeholders[$key]);

        return $this;
    }

    /**
     * @return ApiContext
     */
    protected function cleanPlaceHolders(): self
    {
        $this->placeholders = [];

        return $this;
    }

    /**
     * @When /^I send a "([^"]*)" request to "([^"]*)"$/
     *
     * @param $method
     * @param $uri
     */
    public function iSendARequestTo($method, $uri)
    {
        $this->request($method, $uri);
    }

    /**
     * @When /^I send a "([^"]*)" to "([^"]*)" with:$/
     *
     * @param $method
     * @param $uri
     * @param PyStringNode $string
     */
    public function iSendAToWith($method, $uri, PyStringNode $string)
    {
        $this->request($method, $uri, [
            RequestOptions::JSON => json_decode(
                $this->placeholders($string->getRaw()),
                true
            )
        ]);

    }

    /**
     * @When /^I send a "([^"]*)" to resource "([^"]*)" with:$/
     *
     * @param $method
     * @param $uri
     * @param PyStringNode $string
     */
    public function iSendAToResourceWith($method, $uri, PyStringNode $string)
    {
        $this->request($method, $this->resource . $uri, [
            RequestOptions::JSON => json_decode($string->getRaw(), true)
        ]);
    }

    /**
     * @When /^I request again the resource$/
     */
    public function iRequestAgainResource()
    {
        $this->request('GET', $this->resource);
    }

    /**
     * @When /^I send a "([^"]*)" to the resource with:$/
     *
     * @param $method
     * @param PyStringNode $string
     */
    public function iSendAToTheResourceWith($method, PyStringNode $string)
    {
        $this->request($method, $this->resource, [
            RequestOptions::JSON => json_decode($string->getRaw(), true)
        ]);
    }

    /**
     * @Given /^the response should match with code "([^"]*)" and body:$/
     *
     * @param PyStringNode $expected
     */
    public function theResponseShouldMatchWith(int $code, PyStringNode $expected)
    {
        $this->theResponseCodeIs($code);

        self::assertTrue(
            $this->matcher->match(
                (string) $this->response->getBody(),
                $expected->getRaw()
            ),
            'Response match error'
        );
    }

    /**
     * @Then /^I should be redirected to resource$/
     */
    public function iShouldBeRedirectedToResource()
    {
        self::assertNotNull($this->response->getHeaderLine('location'));

        $this->resource = $this->response->getHeaderLine('location');
        $this->request('GET', $this->resource);
    }

    /**
     * @Given /^the response body match with file "([^"]*)" and status code is "([^"]*)"$/
     *
     * @param string $file
     * @param int $code
     */
    public function theResponseBodyMatchWithFileAndStatusCodeIs(string $file, int $code)
    {
        self::assertResponse(
            $this->httpFoundationFactory->createResponse($this->response),
            $file,
            $code
        );
    }
    
    /**
     * @param string $location
     *
     * @return string
     */
    protected function getResourceIdFromLocation(string $location): string
    {
        return substr($location, strrpos($location, '/')+1);
    }

    /**
     * @Given /^the response code is "([^"]*)"$/
     *
     * @param int $code
     */
    public function theResponseCodeIs(int $code)
    {
        self::assertEquals($this->response->getStatusCode(),$code);
    }

    /**
     * @Given /^a user "([^"]*)" logged with password "([^"]*)"$/
     *
     * @param string $user
     * @param string $pass
     */
    public function aUserLoggedWithPassword(string $user, string $pass)
    {
        $this->request('POST', '/auth/login', [
            RequestOptions::JSON => [
                '_username' => $user,
                '_password' => $pass
            ]
        ]);

        self::assertEquals(200, $this->response->getStatusCode(), 'User cannot be logged due to credentials error');

        $this->options[RequestOptions::HEADERS] = [
            'Authorization' =>  'Bearer ' . json_decode($this->response->getBody(), true)['token']
        ];
    }

    /**
     * @param string $method
     * @param string $uri
     * @param array $options
     */
    protected function request(string $method, string $uri, array $options = [])
    {
        try{

            $options = array_merge($this->options, $options);

            $this->response = $this->http->request($method, $uri, $options);

        } catch (ClientException $e) {

            if ($e->hasResponse()) {

                $this->response = $e->getResponse();
            }
        }
    }


    /**
     * @beforeClass
     */
    public static function createSharedKernel(string $env = 'dev')
    {
        static::$sharedKernel = static::createKernel(['debug' => false, 'environment' => $env]);
        static::$sharedKernel->boot();
    }
}
```

## File: `tests/UI/Behat/Context/Api/Home/HomeContext.php`
```php
<?php

namespace Tests\Leos\UI\Behat\Context\Api\Home;

use Tests\Leos\UI\Behat\Context\Api\ApiContext;

class HomeContext extends ApiContext
{

}
```

## File: `tests/UI/Behat/Context/Api/Monitor/MonitorContext.php`
```php
<?php

namespace Tests\Leos\UI\Behat\Context\Api\Monitor;


use Tests\Leos\UI\Behat\Context\Api\ApiContext;

class MonitorContext extends ApiContext
{

}
```

## File: `tests/UI/Behat/Context/Api/Security/SecurityContext.php`
```php
<?php

namespace Tests\Leos\UI\Behat\Context\Api\Security;

use Tests\Leos\UI\Behat\Context\Api\ApiContext;

/**
 * Class SecurityContext
 *
 * @package Tests\Leos\UI\Behat\Context\Api\Security
 */
class SecurityContext extends ApiContext
{
    /**
     * @Given /^a list of users persisted$/
     */
    public function aListOfWalletsPersisted()
    {
        $this->createSharedKernel('dev');
        $this->setUpDatabase();
        $this->loadFixturesFromDirectory('user');
    }
    
    
}
```

## File: `tests/UI/Behat/Context/Api/Wallet/WalletContext.php`
```php
<?php

namespace Tests\Leos\UI\Behat\Context\Api\Wallet;

use GuzzleHttp\RequestOptions;
use Leos\Domain\User\Model\User;
use Tests\Leos\UI\Behat\Context\Api\ApiContext;

/**
 * Class WalletContext
 * 
 * @package Tests\Leos\UI\Behat\Context\Api\Wallet
 */
class WalletContext extends ApiContext
{
    /**
     * @var string
     */
    private $transaction;

    /**
     * @Given /^a list of wallets persisted$/
     */
    public function aListOfWalletsPersisted()
    {
        $this->createSharedKernel('dev');
        $this->setUpDatabase();
        /** @var User[]|mixed $fixtures */
        $fixtures = $this->loadFixturesFromDirectory('wallet');

        $this->addPlaceHolder('userId', $fixtures['jorge']->uuid()->__toString());
    }

    /**
     * @Then /^I rollback the deposit$/
     */
    public function iRollbackTheDeposit()
    {
        $this->request('POST', '/api/v1/rollback/deposit.json', [
            RequestOptions::JSON => [
                'deposit' => $this->transaction
            ]
        ]);
    }

    /**
     * @Then /^I rollback the withdrawal/
     */
    public function iRollbackTheWithdrawal()
    {
        $this->request('POST', '/api/v1/rollback/withdrawal.json', [
            RequestOptions::JSON => [
                'withdrawal' => $this->transaction
            ]
        ]);
    }

    /**
     * @Given /^I store the transaction$/
     */
    public function iStoreTheTransaction()
    {
        $this->transaction = json_decode((string) $this->response->getBody(), true)['uuid'];
    }

}
```

## File: `tests/UI/Behat/Features/Home/home.feature`
```
Feature: Home endpoint
  As an user
  I want see the home

  Scenario: List home
    When I send a "GET" request to "/"
    And the response body match with file "home" and status code is "200"
```

## File: `tests/UI/Behat/Features/Monitor/ping.feature`
```
Feature: Ping endpoint
  As an admin
  I want monitor the project

  Scenario: Create a new wallet
    When I send a "GET" request to "/monitor/ping.json"
    And the response body match with file "ping" and status code is "200"
```

## File: `tests/UI/Behat/Features/Security/login.feature`
```
Feature: Login in the platform
  As a user
  I wanna be available to login in the platform

  Scenario: Login successfully as jorge
    Given a list of users persisted
    When I send a "POST" to "/auth/login" with:
    """
    {
      "_username": "jorge",
      "_password": "iyoque123"
    }
    """
    Then the response body match with file "login_ok" and status code is "200"

  Scenario: Try to login as jorge with wrong password
    Given a list of users persisted
    When I send a "POST" to "/auth/login" with:
    """
    {
      "_username": "jorge",
      "_password": "vaya, vaya cabesa"
    }
    """
    Then the response code is "401"
```

## File: `tests/UI/Behat/Features/Security/register.feature`
```
Feature: Register a new user in the platform
  As a user
  I wanna be available to register in the platform

  Scenario: Register successfully as paco
    When I send a "POST" to "/auth/register" with:
    """
    {
       "username": "paco",
       "email": "paco@gmail.com",
       "password": "qweqwe1234567890"
    }
    """
    Then the response code is "201"

  Scenario: Try to register as paco with wrong password
    Given a list of users persisted
    When I send a "POST" to "/auth/register" with:
    """
    {
       "username": "paco",
       "email": "paco@gmail.com",
       "password": "123"
    }
    """
    Then the response body match with file "wrong_password_scenario" and status code is "400"

  Scenario: Try to register as paco with wrong email
    When I send a "POST" to "/auth/register" with:
    """
    {
       "username": "paco",
       "email": "paco",
       "password": "987654321987"
    }
    """
    Then the response body match with file "wrong_email_scenario" and status code is "400"
```

## File: `tests/UI/Behat/Features/Wallet/wallet.feature`
```
Feature: Wallet endpoint
  As a user
  I want test the wallet workflow

  Background:
    Given a list of wallets persisted
    And a user "jorge" logged with password "iyoque123"

  Scenario: Create a new wallet and use it
    When I send a "POST" to "/api/v1/wallet.json" with:
    """
    {
      "userId": "%userId%",
      "currency": "EUR"
    }
    """
    And the response code is "201"
    Then I should be redirected to resource
    And the response body match with file "get_wallet" and status code is "200"
    Then I send a "POST" to resource "/deposit.json" with:
    """
    {
      "real": 100,
      "provider": "paypal"
    }
    """
    And the response body match with file "deposit" and status code is "202"
    Then I send a "POST" to resource "/deposit.json" with:
    """
    {
      "real": 9,
      "provider": "paypal"
    }
    """
    And the response code is "202"
    Then I send a "POST" to resource "/withdrawal.json" with:
    """
    {
      "real": 64,
      "provider": "paypal"
    }
    """
    And the response body match with file "withdrawal_final_behat" and status code is "202"


  Scenario: I will rollback deposit
    When I send a "POST" to "/api/v1/wallet.json" with:
    """
    {
      "userId": "%userId%",
      "currency": "EUR"
    }
    """
    And the response code is "201"
    Then I should be redirected to resource
    And the response body match with file "get_wallet" and status code is "200"
    Then I send a "POST" to resource "/deposit.json" with:
    """
    {
      "real": 100,
      "provider": "paypal"
    }
    """
    And the response should match with code "202" and body:
    """
    {
      "uuid":"@string@",
      "type":"deposit",
      "prev_real": {
        "amount":0,
        "generated_at":"@string@.isDateTime()"
      },
      "prev_bonus": {
        "amount":0,
        "generated_at":"@string@.isDateTime()"
      },
      "operation_real": 10000,
      "operation_bonus": 0,
      "wallet": {
        "uuid": "@string@",
        "real": {
          "amount":10000,
          "generated_at":"@string@.isDateTime()"
        },
        "bonus": {
          "amount":0,
          "generated_at":"@string@.isDateTime()"
        },
        "created_at":"@string@.isDateTime()",
        "updated_at":null
      },
      "details": {
        "provider": "paypal"
      },
      "referral_transaction":null,
      "created_at":"@string@.isDateTime()",
      "updated_at":null
    }
    """

    And I store the transaction

    Then I rollback the deposit
    And the response code is "202"

    Then I request again the resource
    """
    """
    And the response body match with file "get_wallet" and status code is "200"

  Scenario: I will rollback withdrawal
    When I send a "POST" to "/api/v1/wallet.json" with:
    """
    {
      "userId": "%userId%",
      "currency": "EUR"
    }
    """
    And the response code is "201"
    Then I should be redirected to resource
    And the response body match with file "get_wallet" and status code is "200"
    Then I send a "POST" to resource "/deposit.json" with:
    """
    {
      "real": 50,
      "provider": "redsys"
    }
    """
    And the response code is "202"

    Then I send a "POST" to resource "/withdrawal.json" with:
    """
    {
      "real": 50,
      "provider": "paypal"
    }
    """
    And the response code is "202"
    And I store the transaction

    Then I rollback the withdrawal
    And the response body match with file "rollback_withdrawal_scenario" and status code is "202"

  Scenario: Try to get a non existent wallet
    When I send a "GET" request to "/api/v1/wallet/0cb00000-646e-11e6-a5a2-0000ac1b0000.json"
    And the response code is "404"


  Scenario: List the wallets
    When I send a "GET" request to "/api/v1/wallet.json"
    And the response body match with file "cget_wallet" and status code is "200"


  Scenario: Filter the wallets
    When I send a "GET" request to "/api/v1/wallet.json?filterParam[]=real.amount&filterOp[]=eq&filterValue[]=50"
    And the response body match with file "cget_wallet_filter_50" and status code is "200"
```

## File: `tests/UI/Fixtures/user/list.yml`
```yaml
Leos\Infrastructure\SecurityBundle\ValueObject\EncodedPassword:
    jorge-pass:
      __construct: ['iyoque123']
    marcel-pass:
      __construct: ['023548123']
    sebas-pass:
      __construct: ['elnalgasvuelve']
    tito-pass:
      __construct: ['dispensy']


Leos\Domain\User\ValueObject\UserId:
    one:
      __construct: ['fc03e3ec-c3a1-11e6-a4a6-cec0c932ce01']
    two:
      __construct: ['fc03e3ec-c3a1-11e6-a4a6-cec0c932ce02']
    three:
      __construct: ['fc03e3ec-c3a1-11e6-a4a6-cec0c932ce03']
    four:
      __construct: ['fc03e3ec-c3a1-11e6-a4a6-cec0c932ce04']
Leos\Domain\User\Model\User:
    jorge:
      __construct: ['@one', 'jorge', 'jorge.arcoma@gmail.com', '@jorge-pass']
    marcel:
      __construct: ['@two', 'marcel', '1ma@gmail.com', '@marcel-pass']
    sebas:
      __construct: ['@three', 'sebas', 'sebidchi@gmail.com', '@sebas-pass']
    tito:
      __construct: ['@four', 'vrios', 'vrios@gmail.com', '@tito-pass']
```

## File: `tests/UI/Fixtures/wallet/list.yml`
```yaml
include:
  - ../user/list.yml

Leos\Domain\Money\ValueObject\Currency:
    EUR:
      __construct: ['EUR']

Leos\Domain\Money\ValueObject\Money:
    money-0:
      __construct: [0, '@EUR']
    money-05:
      __construct: [0.5, '@EUR']
    money-10:
      __construct: [10, '@EUR']
    money-50:
      __construct: [50, '@EUR']
    money-100:
      __construct: [100, '@EUR']


Leos\Domain\Wallet\ValueObject\WalletId:
    wallet-id-1:
      __construct: [null]
    wallet-id-2:
      __construct: [null]
    wallet-id-3:
      __construct: [null]
    wallet-id-4:
      __construct: [null]


Leos\Domain\Wallet\Model\Wallet:
    wallet1:
      __construct: ['@jorge', '@wallet-id-1']
      addRealmoney: ['@money-05']
    wallet2:
      __construct: ['@marcel', '@wallet-id-2']
      addRealmoney: ['@money-50']
      addBonusmoney: ['@money-50']
    wallet3:
      __construct: ['@sebas', '@wallet-id-3']
      addBonusmoney: ['@money-100']
```

## File: `tests/UI/Responses/Home/home.json`
```json
{
  "wallet": "@string@.contains('wallet')"
}
```

## File: `tests/UI/Responses/Monitor/ping.json`
```json
"pong"
```

## File: `tests/UI/Responses/Security/login_ok.json`
```json
{
  "token": "@string@"
}
```

## File: `tests/UI/Responses/Security/wrong_email_scenario.json`
```json
{
  "code":400,
  "message": "Invalid email paco"
}
```

## File: `tests/UI/Responses/Security/wrong_password_scenario.json`
```json
{
  "code": 400,
  "message": "security.exception.invalid_password"
}
```

## File: `tests/UI/Responses/User/new_user.json`
```json
{
  "uuid": "@string@",
  "email": "@string@",
  "created_at": "@string@.isDateTime()",
  "updated_at": null
}
```

## File: `tests/UI/Responses/User/updated_user.json`
```json
{
  "uuid": "@string@",
  "email": "@string@",
  "auth": {
    "username": "@string@",
    "roles": "@array@"
  },
  "created_at": "@string@.isDateTime()",
  "updated_at": "@string@.isDateTime()"
}
```

## File: `tests/UI/Responses/Wallet/cget_wallet.json`
```json
{
    "page": "@integer@",
    "limit": "@integer@",
    "pages": "@integer@",
    "total": "@integer@",
    "_links": {
        "self": {
            "href": "@string@.contains('api')"
        },
        "first": {
            "href": "@string@.contains('api')"
        },
        "last": {
            "href": "@string@.contains('api')"
        }
    },
    "_embedded": {
        "items": [
            {
                "uuid": "@string@",
                "real": {
                    "amount": "@integer@",
                    "generated_at": "@string@.isDateTime()"
                },
                "bonus": {
                    "amount": "@integer@",
                    "generated_at": "@string@.isDateTime()"
                },
                "created_at": "@string@.isDateTime()",
                "updated_at": null
            },
          "@...@"
        ]
    }
}
```

## File: `tests/UI/Responses/Wallet/cget_wallet_filter_50.json`
```json
{
    "page": "@integer@",
    "limit": "@integer@",
    "pages": "@integer@",
    "total": "@integer@",
    "_links": {
        "self": {
            "href": "@string@.contains('api')"
        },
        "first": {
            "href": "@string@.contains('api')"
        },
        "last": {
            "href": "@string@.contains('api')"
        }
    },
    "_embedded": {
        "items": [
            {
                "uuid": "@string@",
                "real": {
                    "amount": 50,
                    "generated_at": "@string@.isDateTime()"
                },
                "bonus": {
                    "amount": "@integer@",
                    "generated_at": "@string@.isDateTime()"
                },
                "created_at": "@string@.isDateTime()",
                "updated_at": null
            }
        ]
    }
}
```

## File: `tests/UI/Responses/Wallet/deposit.json`
```json
{
  "uuid":"@string@",
  "type":"deposit",
  "prev_real": {
    "amount":0,
    "generated_at":"@string@.isDateTime()"
  },
  "prev_bonus": {
    "amount":0,
    "generated_at":"@string@.isDateTime()"
  },
  "operation_real": 10000,
  "operation_bonus": 0,
  "wallet": {
    "uuid": "@string@",
    "real": {
      "amount":10000,
      "generated_at":"@string@.isDateTime()"
    },
    "bonus": {
      "amount":0,
      "generated_at":"@string@.isDateTime()"
    },
    "created_at":"@string@.isDateTime()",
    "updated_at":null
  },
  "details": {
    "provider": "paypal"
  },
  "referral_transaction":null,
  "created_at":"@string@.isDateTime()",
  "updated_at":null
}
```

## File: `tests/UI/Responses/Wallet/get_wallet.json`
```json
{
    "uuid": "@string@",
    "real": {
        "amount": "@integer@",
        "generated_at": "@string@.isDateTime()"
    },
    "bonus": {
        "amount": "@integer@",
        "generated_at": "@string@.isDateTime()"
    },
    "created_at": "@string@.isDateTime()",
    "updated_at": null
}
```

## File: `tests/UI/Responses/Wallet/rollback_deposit_scenario.json`
```json
{
  "uuid":"@string@",
  "type":"rollback_deposit",
  "prev_real": {
    "amount": 10000,
    "generated_at":"@string@.isDateTime()"
  },
  "prev_bonus": {
    "amount":0,
    "generated_at":"@string@.isDateTime()"
  },
  "operation_real": 10000,
  "operation_bonus": 0,
  "wallet": {
    "uuid": "@string@",
    "real": {
      "amount":0,
      "generated_at":"@string@.isDateTime()"
    },
    "bonus": {
      "amount":0,
      "generated_at":"@string@.isDateTime()"
    },
    "created_at":"@string@.isDateTime()",
    "updated_at":null
  },
  "details": {
    "provider": "paypal"
  },
  "referral_transaction": "@array@",
  "created_at":"@string@.isDateTime()",
  "updated_at":null
}
```

## File: `tests/UI/Responses/Wallet/rollback_withdrawal_scenario.json`
```json
{
  "uuid":"@string@",
  "type":"rollback_withdrawal",
  "prev_real": {
    "amount":0,
    "generated_at":"@string@.isDateTime()"
  },
  "prev_bonus": {
    "amount":0,
    "generated_at":"@string@.isDateTime()"
  },
  "operation_real": 5000,
  "operation_bonus": 0,
  "wallet": {
    "uuid": "@string@",
    "real": {
      "amount":5000,
      "generated_at":"@string@.isDateTime()"
    },
    "bonus": {
      "amount":0,
      "generated_at":"@string@.isDateTime()"
    },
    "created_at":"@string@.isDateTime()",
    "updated_at":null
  },
  "details": {
    "provider": "paypal"
  },
  "referral_transaction": "@array@",
  "created_at":"@string@.isDateTime()",
  "updated_at":null
}
```

## File: `tests/UI/Responses/Wallet/withdrawal.json`
```json
{
  "uuid":"@string@",
  "type":"withdrawal",
  "prev_real": {
    "amount": 5000,
    "generated_at":"@string@.isDateTime()"
  },
  "prev_bonus": {
    "amount": 0,
    "generated_at":"@string@.isDateTime()"
  },
  "operation_real": -500,
  "operation_bonus": 0,
  "wallet": {
    "uuid": "@string@",
    "real": {
      "amount": 4500,
      "generated_at":"@string@.isDateTime()"
    },
    "bonus": {
      "amount": 0,
      "generated_at":"@string@.isDateTime()"
    },
    "created_at":"@string@.isDateTime()",
    "updated_at":null
  },
  "details": {
    "provider": "paypal"
  },
  "referral_transaction":null,
  "created_at":"@string@.isDateTime()",
  "updated_at":null
}
```

## File: `tests/UI/Responses/Wallet/withdrawal_final_behat.json`
```json
{
  "uuid":"@string@",
  "type":"withdrawal",
  "prev_real": {
    "amount": 10900,
    "generated_at":"@string@.isDateTime()"
  },
  "prev_bonus": {
    "amount": 0,
    "generated_at":"@string@.isDateTime()"
  },
  "operation_real": -6400,
  "operation_bonus":0,
  "wallet": {
    "uuid": "@string@",
    "real": {
      "amount": 4500,
      "generated_at":"@string@.isDateTime()"
    },
    "bonus": {
      "amount": 0,
      "generated_at":"@string@.isDateTime()"
    },
    "created_at":"@string@.isDateTime()",
    "updated_at":null
  },
  "details": {
    "provider": "paypal"
  },
  "referral_transaction":null,
  "created_at":"@string@.isDateTime()",
  "updated_at":null
}
```

## File: `tests/UI/RestBundle/Controller/Home/HomeControllerTest.php`
```php
<?php

namespace Tests\Leos\UI\RestBundle\Controller\Home;

use Lakion\ApiTestCase\JsonApiTestCase;

class HomeControllerTest extends JsonApiTestCase
{
    public function setUp()
    {
        $this->setUpClient();
    }

    /**
     * @group integration
     */
    public function testGetAction()
    {
        $this->client->request('GET', '/');

        self::assertResponse($this->client->getResponse(), "Home/home");
    }
}
```

## File: `tests/UI/RestBundle/Controller/Monitor/StatusControllerTest.php`
```php
<?php

namespace Tests\Leos\UI\RestBundle\Controller\Monitor;

use Lakion\ApiTestCase\JsonApiTestCase;

/**
 * Class StatusControllerTest
 *
 * @package Leos\UI\RestBundle\Controller\Monitor
 */
class StatusControllerTest extends JsonApiTestCase
{
    public function setUp()
    {
        $this->setUpClient();
    }

    /**
     * @group integration
     */
    public function testPingAction()
    {
        $this->client->request('GET', '/monitor/ping.json');

        self::assertResponse($this->client->getResponse(), "Monitor/ping");
    }
}
```

## File: `tests/UI/RestBundle/Controller/Rollback/RollbackControllerTest.php`
```php
<?php

namespace Tests\Leos\UI\RestBundle\Controller\Wallet;

use Lakion\ApiTestCase\JsonApiTestCase;
use Tests\Leos\UI\RestBundle\Controller\Security\SecurityTrait;

/**
 * Class RollbackControllerTest
 * 
 * @package Leos\UI\RestBundle\Controller\Wallet
 */
class RollbackControllerTest extends JsonApiTestCase
{
    use SecurityTrait;

    private $databaseLoaded = false;

    public function setUp()
    {
        if (!$this->client) {

            $this->setUpClient();
        }

        if (!$this->databaseLoaded) {

            $this->setUpDatabase();
            $this->databaseLoaded = true;
        }
    }

    /**
     * @group integration
     */
    public function testRollbackDepositAction()
    {
        $this->loginClient('jorge', 'iyoque123');

        $userId = $this->users['jorge']->uuid()->__toString();

        $this->client->request('POST', '/api/v1/wallet.json', [
            'userId' => $userId
        ]);

        $response = $this->client->getResponse();
        self::assertEquals(201, $response->getStatusCode());

        $this->client->request('POST', $response->headers->get('location') . '/deposit.json', [
            'real' => 100,
            'provider' => 'paypal'
        ]);

        $response = $this->client->getResponse();

        $this->client->request('POST', '/api/v1/rollback/deposit.json', [
            'deposit' => json_decode($response->getContent(), true)['uuid']
        ]);

        $response = $this->client->getResponse();
        self::assertEquals(202, $response->getStatusCode());
    }

    /**
     * @group integration
     */
    public function testRollbackDepositNotFoundAction()
    {
        $this->loginClient('jorge', 'iyoque123');

        $this->client->request('POST', '/api/v1/rollback/deposit.json', [
            'deposit' => '0cb00000-646e-11e6-a5a2-0000ac1b0000'
        ]);

        $response = $this->client->getResponse();
        self::assertEquals(404, $response->getStatusCode());
    }
    /**
     * @group integration
     */
    public function testRollbackWithdrawalNotFoundAction()
    {
        $this->loginClient('jorge', 'iyoque123');

        $this->client->request('POST', '/api/v1/rollback/withdrawal.json', [
            'withdrawal' => '0cb00000-646e-11e6-a5a2-0000ac1b0000'
        ]);

        $response = $this->client->getResponse();
        self::assertEquals(404, $response->getStatusCode());
    }

    /**
     * @group integration
     */
    public function testRollbackWithdrawalAction()
    {
        $this->loginClient('jorge', 'iyoque123');

        $userId = $this->users['jorge']->uuid()->__toString();

        $this->client->request('POST', '/api/v1/wallet.json', [
            'userId' => $userId
        ]);


        $response = $this->client->getResponse();
        self::assertEquals(201, $response->getStatusCode());

        $this->client->request('POST', $response->headers->get('location') . '/deposit.json', [
            'real' => 50,
            'provider' => 'paypal'
        ]);

        $this->client->request('POST', $response->headers->get('location') . '/withdrawal.json', [
            'real' => 5,
            'provider' => 'paypal'
        ]);

        $response = $this->client->getResponse();

        self::assertResponse($response, "Wallet/withdrawal", 202);

        $this->client->request('POST', '/api/v1/rollback/withdrawal.json', [
            'withdrawal' => json_decode($response->getContent(), true)['uuid']
        ]);

        $response = $this->client->getResponse();
        self::assertEquals(202, $response->getStatusCode());
    }

    /**
     * @group integration
     */
    public function testRollbackDepositGivenAWithdrawalAction()
    {
        $this->loginClient('jorge', 'iyoque123');

        $userId = $this->users['jorge']->uuid()->__toString();

        $this->client->request('POST', '/api/v1/wallet.json', [
            'userId' => $userId
        ]);

        $response = $this->client->getResponse();
        self::assertEquals(201, $response->getStatusCode());

        $this->client->request('POST', $response->headers->get('location') . '/deposit.json', [
            'real' => 50,
            'provider' => 'paypal'
        ]);

        $this->client->request('POST', $response->headers->get('location') . '/withdrawal.json', [
            'real' => 5,
            'provider' => 'paypal'
        ]);

        $response = $this->client->getResponse();

        self::assertResponse($response, "Wallet/withdrawal", 202);

        $this->client->request('POST', '/api/v1/rollback/deposit.json', [
            'deposit' => json_decode($response->getContent(), true)['uuid']
        ]);

        $response = $this->client->getResponse();
        self::assertEquals(409, $response->getStatusCode());
        self::assertContains('type', $response->getContent());
    }
}
```

## File: `tests/UI/RestBundle/Controller/Security/SecurityTest.php`
```php
<?php

namespace Leos\UI\RestBundle\Controller\Security;

use Lakion\ApiTestCase\JsonApiTestCase;

/**
 * Class SecurityTest
 * 
 * @package Leos\UI\RestBundle\Controller\Security
 */
class SecurityTest extends JsonApiTestCase
{
    private $databaseLoaded = false;

    public function setUp()
    {
        if (!$this->client) {

            $this->setUpClient();
        }

        if (!$this->databaseLoaded) {

            $this->setUpDatabase();
            $this->databaseLoaded = true;
        }
    }

    /**
     * @group integration
     */
    public function testLoginSuccess()
    {
        $this->loadFixturesFromDirectory('user');

        $this->client->request('POST', '/auth/login.json', [
            '_username' => 'jorge',
            '_password' => 'iyoque123'
        ]);

        $response =  $this->client->getResponse();

        self::assertResponse($response, 'Security/login_ok', 200);
    }
    
    /**
     * @group integration
     */
    public function testLoginInvalidUser()
    {
        $this->loadFixturesFromDirectory('user');

        $this->client->request('POST', '/auth/login.json', [
            '_username' => 'manolo',
            '_password' => 'qwerty'
        ]);

        $response =  $this->client->getResponse();

        self::assertEquals(401, $response->getStatusCode());
    }

    /**
     * @group integration
     */
    public function testLoginWithWrongPassword()
    {
        $this->loadFixturesFromDirectory('user');

        $this->client->request('POST', '/auth/login.json', [
            '_username' => 'jorge',
            '_password' => 'qwerty'
        ]);

        $response =  $this->client->getResponse();

        self::assertEquals(401, $response->getStatusCode());
    }

    /**
     * @group integration
     */
    public function testLoginWithMissingUsername()
    {
        $this->client->request('POST', '/auth/login.json', [
            '_password' => 'qwerty'
        ]);

        $response =  $this->client->getResponse();

        self::assertEquals(400, $response->getStatusCode());
        self::assertContains('username',  $response->getContent());
    }

    /**
     * @group integration
     */
    public function testLoginWithMissingPassword()
    {
        $this->client->request('POST', '/auth/login.json', [
            '_username' => 'jorge'
        ]);

        $response =  $this->client->getResponse();

        self::assertEquals(400, $response->getStatusCode());
        self::assertContains('password',  $response->getContent());
    }
}
```

## File: `tests/UI/RestBundle/Controller/Security/SecurityTrait.php`
```php
<?php

namespace Tests\Leos\UI\RestBundle\Controller\Security;

use Leos\Domain\User\Model\User;

/**
 * Class SecurityTrait
 *
 * @package Leos\UI\RestBundle\Controller\Security
 */
trait SecurityTrait
{
    /**
     * @var string
     */
    protected $accessToken = [];

    /**
     * @var User[]
     */
    protected $users = [];

    /**
     * @param string $username
     * @param string $password
     * @param bool $fixture
     *
     */
    public function loginClient(string $username, string $password, bool $fixture = true)
    {
        if (!isset($this->accessToken[$username])) {

            if ($fixture) {
                $this->users = $this->loadFixturesFromDirectory('user');
            }

            $this->client->request('POST', '/auth/login.json', [
                '_username' => $username,
                '_password' => $password
            ]);

            $response =  $this->client->getResponse();

            self::assertResponseCode($response, 200);

            $data = json_decode($response->getContent(), true);

            $this->accessToken[$username] = $data['token'];
        }

        $this->client->setServerParameter('HTTP_Authorization', sprintf('Bearer %s', $this->accessToken[$username]));
    }

}
```

## File: `tests/UI/RestBundle/Controller/User/UserControllerTest.php`
```php
<?php

namespace Tests\Leos\UI\RestBundle\Controller\User;

use Lakion\ApiTestCase\JsonApiTestCase;
use Tests\Leos\UI\RestBundle\Controller\Security\SecurityTrait;

/**
 * Class UserControllerTest
 *
 * @package Leos\UI\RestBundle\Controller\User
 */
class UserControllerTest extends JsonApiTestCase
{
    use SecurityTrait;

    private $databaseLoaded = false;

    public function setUp()
    {

        if (!$this->client) {

            $this->setUpClient();
        }

        if (!$this->databaseLoaded) {

            $this->setUpDatabase();
            $this->databaseLoaded = true;
        }
    }

    /**
     * @group integration
     */
    public function testCreateUser()
    {
        $this->client->request('POST', '/auth/register', [
            'username' => 'paco',
            'email' => 'paco@gmail.com',
            'password' => 'qweqwe1234567890'
        ]);

        $response = $this->client->getResponse();

        self::assertResponse($response, "User/new_user", 201);

        $this->loginClient('paco', 'qweqwe1234567890');

        $this->client->request('GET', $response->headers->get('location'));

        $response = $this->client->getResponse();

        self::assertResponse($response, "User/new_user", 200);
    }

    /**
     * @group integration
     */
    public function testCreateUserWithWrongPassword()
    {
        $this->client->request('POST', '/auth/register', [
            'username' => 'paco',
            'email' => 'paco@gmail.com',
            'password' => 'qwe'
        ]);

        $response = $this->client->getResponse();

        self::assertEquals(400, $response->getStatusCode());
        self::assertContains('password', $response->getContent());
    }

    /**
     * @group integration
     */
    public function testCreateUserWithWrongEmail()
    {
        $this->client->request('POST', '/auth/register', [
            'username' => 'paco',
            'email' => 'paco',
            'password' => 'qwe1313ghg1313'
        ]);

        $response = $this->client->getResponse();

        self::assertEquals(400, $response->getStatusCode());
        self::assertContains('email', $response->getContent());
    }

    /**
     * @group integration
     */
    public function testCreateUserWithEmptyParams()
    {

        $this->client->request('POST', '/auth/register', [
            'username' => '',
            'email' => '',
            'password' => 'qwe1313ghg1313'
        ]);

        $response = $this->client->getResponse();

        self::assertEquals(400, $response->getStatusCode());
    }

    /**
     * @group integration
     */
    public function testCreateUserWithWrongUsername()
    {
        $this->loadFixturesFromDirectory('user');

        $this->client->request('POST', '/auth/register', [
            'username' => 'jorge',
            'email' => 'paco@gmail.com',
            'password' => 'qwe1234567'
        ]);

        $response = $this->client->getResponse();

        self::assertEquals(409, $response->getStatusCode());
        self::assertContains('already_exist', $response->getContent());
    }

    /**
     * @group integration
     */
    public function testFindUserWithWrongUUIDFormat()
    {
        $this->loginClient('jorge', 'iyoque123');

        $this->client->request('GET', '/api/v1/user/adadadasda.json');

        $response = $this->client->getResponse();

        self::assertEquals(400, $response->getStatusCode());
        self::assertContains('uuid', $response->getContent());
    }
    /**
     * @group integration
     */
    public function testFindUserWithNotExistingUUID()
    {
        $this->loginClient('jorge', 'iyoque123');

        $this->client->request('GET', '/api/v1/user/0cb00000-646e-11e6-a5a2-0000ac1b0000.json');

        $response = $this->client->getResponse();

        self::assertEquals(404, $response->getStatusCode());
    }
}
```

## File: `tests/UI/RestBundle/Controller/Wallet/WalletControllerTest.php`
```php
<?php

namespace Tests\Leos\UI\RestBundle\Controller\Wallet;

use Lakion\ApiTestCase\JsonApiTestCase;
use Tests\Leos\UI\RestBundle\Controller\Security\SecurityTrait;

/**
 * Class WalletControllerTest
 * 
 * @package Leos\UI\RestBundle\Controller\Wallet
 */
class WalletControllerTest extends JsonApiTestCase
{
    use SecurityTrait;

    private $databaseLoaded = false;

    public function setUp()
    {
        if (!$this->client) {

            $this->setUpClient();
        }

        if (!$this->databaseLoaded) {

            $this->setUpDatabase();
            $this->databaseLoaded = true;
        }
    }

    /**
     * @group integration
     */
    public function testCreateWalletAction()
    {
        $this->loginClient('jorge', 'iyoque123');

        $userId = $this->users['jorge']->uuid()->__toString();

        $this->client->request('POST', '/api/v1/wallet.json', [
            'userId' => $userId
        ]);

        $response = $this->client->getResponse();

        self::assertEquals($response->getStatusCode(), 201);

        $this->redirect($response->headers->get('Location'), 'Wallet/get_wallet', 200);
    }

    /**
     * @group integration
     */
    public function testCreateWalletWithWrongCurrencyAction()
    {
        $this->loginClient('jorge', 'iyoque123');

        $userId = $this->users['jorge']->uuid()->__toString();

        $this->client->request('POST', '/api/v1/wallet.json', [
            'userId' => $userId,
            'currency' => 'EURAZO'
        ]);

        self::assertEquals(400, $this->client->getResponse()->getStatusCode());
        self::assertContains('currency', $this->client->getResponse()->getContent());
    }

    /**
     * @group integration
     */
    public function testGetWalletActionNotFound()
    {
        $this->loginClient('jorge', 'iyoque123');

        $this->client->request('GET', '/api/v1/wallet/0.json');

        self::assertEquals($this->client->getResponse()->getStatusCode(), 404);
    }

    /**
     * @group integration
     */
    public function testDepositAction()
    {
        $this->loginClient('jorge', 'iyoque123');

        $userId = $this->users['jorge']->uuid()->__toString();

        $this->client->request('POST', '/api/v1/wallet.json', [
            'userId' => $userId
        ]);

        $response = $this->client->getResponse();
        self::assertEquals(201, $response->getStatusCode());

        $this->client->request('POST', $response->headers->get('location') . '/deposit.json', [
            'real' => 100,
            'provider' => 'paypal'
        ]);

        $response = $this->client->getResponse();
        self::assertResponse($response, "Wallet/deposit", 202);
    }

    /**
     * @group integration
     */
    public function testDepositBadUUIDAction()
    {
        $this->loginClient('jorge', 'iyoque123');

        $this->client->request('POST',  '/api/v1/wallet/404/deposit.json', [
            'real' => 5,
            'bonus' => 5,
            'provider' => 'paypal'
        ]);

        self::assertEquals(400, $this->client->getResponse()->getStatusCode());
    }

    /**
     * @group integration
     */
    public function testDeposit400WrongCurrencyAction()
    {
        $this->loginClient('jorge', 'iyoque123');

        $this->client->request('POST',  '/api/v1/wallet/0cb00000-646e-11e6-a5a2-0000ac1b0000/deposit.json', [
            'real' => 5,
            'bonus' => 5,
            'currency' => 'LIBRAS',
            'provider' => 'paypal'
        ]);

        self::assertEquals(400, $this->client->getResponse()->getStatusCode());
        self::assertContains('currency', $this->client->getResponse()->getContent());
    }

    /**
     * @group integration
     */
    public function testWithdrawalAction()
    {
        $this->loginClient('jorge', 'iyoque123');

        $userId = $this->users['jorge']->uuid()->__toString();

        $this->client->request('POST', '/api/v1/wallet.json', [
            'userId' => $userId
        ]);

        $response = $this->client->getResponse();
        self::assertEquals(201, $response->getStatusCode());

        $this->client->request('POST', $response->headers->get('location') . '/deposit.json', [
            'real' => 50,
            'provider' => 'paypal'
        ]);

        $this->client->request('POST', $response->headers->get('location') . '/withdrawal.json', [
            'real' => 5,
            'provider' => 'paypal'
        ]);

        self::assertResponse($this->client->getResponse(), "Wallet/withdrawal", 202);
    }

    /**
     * @group integration
     */
    public function testWithdrawalShouldFailWhenMinAmountAction()
    {
        $this->loginClient('jorge', 'iyoque123');

        $userId = $this->users['jorge']->uuid()->__toString();

        $this->client->request('POST', '/api/v1/wallet.json', [
            'userId' => $userId
        ]);

        $response = $this->client->getResponse();
        self::assertEquals(201, $response->getStatusCode());

        $this->client->request('POST', $response->headers->get('location') . '/deposit.json', [
            'real' => 50,
            'provider' => 'paypal'
        ]);

        $this->client->request('POST', $response->headers->get('location') . '/withdrawal.json', [
            'real' => 0,
            'provider' => 'paypal'
        ]);

        self::assertEquals($this->client->getResponse()->getStatusCode(), 400);
        self::assertContains('amount_must_be_higher_than_0', $this->client->getResponse()->getContent());
    }

    /**
     * @group integration
     */
    public function testDepositWrongCurrencyAction()
    {
        $this->loginClient('jorge', 'iyoque123');

        $userId = $this->users['jorge']->uuid()->__toString();

        $this->client->request('POST', '/api/v1/wallet.json', [
            'userId' => $userId
        ]);

        $response = $this->client->getResponse();

        self::assertEquals(201, $response->getStatusCode());

        $this->client->request('POST', $response->headers->get('location') . '/deposit.json', [
            'real' => 50,
            'currency' => 'LIBRAS',
            'provider' => 'paypal'
        ]);

        self::assertEquals(400, $this->client->getResponse()->getStatusCode());
        self::assertContains('currency', $this->client->getResponse()->getContent());
    }


    /**
     * @group integration
     */
    public function testDepositWrongAmountAction()
    {
        $this->loginClient('jorge', 'iyoque123');

        $userId = $this->users['jorge']->uuid()->__toString();

        $this->client->request('POST', '/api/v1/wallet.json', [
            'userId' => $userId
        ]);

        $response = $this->client->getResponse();

        self::assertEquals(201, $response->getStatusCode());

        $this->client->request('POST', $response->headers->get('location') . '/deposit.json', [
            'real' => 0,
            'currency' => 'EUR',
            'provider' => 'paypal'
        ]);

        self::assertEquals(400, $this->client->getResponse()->getStatusCode());
        self::assertContains('amount', $this->client->getResponse()->getContent());
    }


    /**
     * @group integration
     */
    public function testDeposit404Action()
    {
        $this->loginClient('jorge', 'iyoque123');

        $this->client->request('POST',  '/api/v1/wallet/0cb00000-646e-11e6-a5a2-0000ac1b0000/deposit.json', [
            'real' => 5,
            'provider' => 'paypal'
        ]);

        self::assertEquals(404, $this->client->getResponse()->getStatusCode());
    }


    /**
     * @group integration
     */
    public function testWithdrawal400WrongCurrencyAction()
    {
        $this->loginClient('jorge', 'iyoque123');

        $this->client->request('POST',  '/api/v1/wallet/0cb00000-646e-11e6-a5a2-0000ac1b0000/withdrawal.json', [
            'real' => 5,
            'bonus' => 5,
            'currency' => 'LIBRAS',
            'provider' => 'paypal'
        ]);

        self::assertEquals(400, $this->client->getResponse()->getStatusCode());
        self::assertContains('currency', $this->client->getResponse()->getContent());
    }

    /**
     * @group integration
     */
    public function testWithdrawal409Action()
    {
        $this->loginClient('jorge', 'iyoque123');

        $userId = $this->users['jorge']->uuid()->__toString();

        $this->client->request('POST', '/api/v1/wallet.json', [
            'userId' => $userId
        ]);

        $response = $this->client->getResponse();

        $this->client->request('POST', $response->headers->get('location') . '/withdrawal.json', [
            'real' => 60,
            'bonus' => 5,
            'provider' => 'paypal'
        ]);

        self::assertEquals(409, $this->client->getResponse()->getStatusCode());
    }

    /**
     * @group integration
     */
    public function testWithdrawalBadUUIDAction()
    {
        $this->loginClient('jorge', 'iyoque123');

        $this->client->request('POST',  '/api/v1/wallet/404/withdrawal.json', [
            'real' => 5,
            'bonus' => 5,
            'provider' => 'paypal'
        ]);

        self::assertEquals(400, $this->client->getResponse()->getStatusCode());
    }

    /**
     * @group integration
     */
    public function testWithdrawal404Action()
    {
        $this->loginClient('jorge', 'iyoque123');
        
        $this->client->request('POST',  '/api/v1/wallet/0cb00000-646e-11e6-a5a2-0000ac1b0000/withdrawal.json', [
            'real' => 5,
            'bonus' => 5,
            'provider' => 'paypal'
        ]);

        self::assertEquals(404, $this->client->getResponse()->getStatusCode());
    }


    /**
     * @group integration
     */
    public function testWalletCollectionAction()
    {
        $this->loadFixturesFromDirectory('wallet');

        $this->loginClient('jorge', 'iyoque123', false);

        $this->client->request('GET',  '/api/v1/wallet.json');

        self::assertResponse($this->client->getResponse(), "Wallet/cget_wallet", 200);
    }

    /**
     * @group integration
     */
    public function testWalletCollectionFilterAction()
    {
        $this->loadFixturesFromDirectory('wallet');

        $this->loginClient('jorge', 'iyoque123', false);

        $this->client->request('GET',  '/api/v1/wallet.json?filterParam[]=real.amount&filterOp[]=eq&filterValue[]=50');

        self::assertResponse($this->client->getResponse(), "Wallet/cget_wallet_filter_50", 200);
    }

    /**
     * @param string $location
     * @param string $responseFile
     * @param int $code
     */
    private function redirect(string $location, string $responseFile, int $code)
    {
        $this->client->request('GET', $location);

        self::assertResponse($this->client->getResponse(), $responseFile, $code);
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

/**
 * @var Composer\Autoload\ClassLoader
 */
$loader = require __DIR__.'/../app/autoload.php';
include_once __DIR__.'/../var/bootstrap.php.cache';

$kernel = new AppKernel('prod', false);
$kernel->loadClassCache();
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

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\Debug\Debug;

// If you don't want to setup permissions the proper way, just uncomment the following PHP line
// read http://symfony.com/doc/current/book/installation.html#checking-symfony-application-configuration-and-setup
// for more information
//umask(0000);

/**
 * @var Composer\Autoload\ClassLoader $loader
 */
$loader = require __DIR__.'/../app/autoload.php';
Debug::enable();

$kernel = new AppKernel('dev', true);
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


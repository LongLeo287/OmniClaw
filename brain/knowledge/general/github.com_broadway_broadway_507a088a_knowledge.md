---
id: github.com-broadway-broadway-507a088a-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:35.907530
---

# KNOWLEDGE EXTRACT: github.com_broadway_broadway_507a088a
> **Extracted on:** 2026-04-01 16:53:01
> **Source:** D:/LongLeo/AI OS CORP/AI OS/core/security/QUARANTINE/KI-BATCH-20260331205007525394/github.com_broadway_broadway_507a088a

---

## File: `.docheader`
```
/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */
```

## File: `.gitignore`
```
/vendor/
composer.lock
.php-cs-fixer.cache
.phpunit.result.cache
```

## File: `.php-cs-fixer.php`
```php
<?php

$config = require 'vendor/broadway/coding-standard/.php-cs-fixer.dist.php';

$config->setFinder(
    \PhpCsFixer\Finder::create()
        ->in([
            __DIR__ . '/src',
            __DIR__ . '/test',
            __DIR__ . '/examples',
        ])
);

return $config;
```

## File: `CHANGELOG.md`
```markdown
# Changelog

## v2.0.x

#### BC breaks

* [4e6fe27](http://github.com/broadway/broadway/commit/4e6fe27eb4c35d67fc5a2cffccfca62000f9f929) Finalized concrete classes (Nikita Konstantinov)
* [5c3cc30](http://github.com/broadway/broadway/commit/5c3cc30a03ef92358745cb9bdfcae46c554195b4) required PHP 7 (othillo)
* [8ee2fd2](http://github.com/broadway/broadway/commit/8ee2fd2ebb2adcb144f9f8160e106f3b18498036) required PHPUnit 6 (Alexander Bachmann)

#### Other changes

* [f74c855](http://github.com/broadway/broadway/commit/f74c85589b9ad096a2e8bbab917fca773898cd13) Added a closure command handler (Francesco Trucchia)
* [b21c245](http://github.com/broadway/broadway/commit/b21c245f4788c62df4fa5200e2f313481521a589) Provide access to Metadata values (Reen Lokum)
* [05e88ce](http://github.com/broadway/broadway/commit/05e88ce83837bea224b65df70f9ebceebd39ed90) Moved to Symfony coding standards (Reen Lokum)
* [df69c8d](http://github.com/broadway/broadway/commit/df69c8d1996fcb9786635ef7bfadb4873c9be3cd) Added reflection serializer (Alexander Bachmann)
* [8486286](http://github.com/broadway/broadway/commit/848628664e61faaced00bc41926989c63c76e8e7) moved RepositoryTestCase, EventStoreTest, EventStoreManagementTest to Testing namespace (Robin van der Vleuten)

## v1.0.x

#### BC breaks

- The EventStore interface added a `loadFromPlayhead` method
- The ReadModelTestCase is renamed to SerializableReadModelTestCase
- We moved the Doctrine DBAL event store implementation to a [separate repository](https://github.com/broadway/event-store-dbal)
- We moved the Elasticsearch read model implementation to a [separate repository](https://github.com/broadway/read-model-elasticsearch) 
- We moved the Symfony bundle to a [separate repository](https://github.com/broadway/broadway-bundle)
- We moved the Saga component to a [separate repository](https://github.com/broadway/broadway-saga)
- DBALEventStore and InMemoryEventStore can now throw DuplicatePlayheadException.
  Ensure you are catching EventStoreException instead of specific driver exceptions.

## v0.10.x

#### Other changes

- allow specifying the DateTime used in the ReadModel Scenario
- added the ReflectionAggregateFactory as an alternative to the NamedConstructorAggregateFactory
- specify ReadModel type searching Elasticsearch read model repository
- added PHPUnit as a development dependency
- adopted new PHP 5.4 and PHP 5.5 language features (DateTimeImmutable, ::class, short array syntax)

## v0.9.x

#### BC breaks

- We raised the minimum required version of symfony/dependency-injection from 2.3 to 2.6.

#### Other changes

- The Symfony Bundle is now Symfony 3 compatible
- The DBALEventStore can now be disabled in configuration
- elasticsearch/elasticsearch-php 2.0 is now also supported
- Serializers are now configurable in the Symfony Bundle

## v0.8.x

#### BC breaks

- We raised the minimum required PHP version from 5.3 to 5.5.

#### Other changes

- Support for [querying the event store](https://github.com/qandidate-labs/broadway/commit/e81d4ea167ce97383a9a4b7d85542e8b5e11900a) using criteria
- The `COMMAND_FAILURE` event now receives [an associative array](https://github.com/qandidate-labs/broadway/blob/140d23f90259bace9601b17ebf749317cd859180/src/Broadway/CommandHandling/EventDispatchingCommandBus.php#L48) when it gets dispatched.
- Fixed a locale issue with creating DateTime objects.

## v0.7.x

#### Symfony Bundle

- You can now configure which Doctrine DBAL connection should be used for the event store
- The auditing command logger service now only gets registered when it's explicitly enabled
- You can now register Sagas with the tag `broadway.saga`
- The `broadway:event-store:schema:drop` command no longer errors when there is no schema

##### Other changes

- There are now [Saga examples](https://github.com/qandidate-labs/broadway/tree/df7445befdb68c9f8b1795d1c454e0dff06ff7a6/examples/saga)
- The DBALEventStore now also works with mysqli

## v0.6.x

#### BC breaks

- The Scenario for CommandHandling now clears the recorded events after each `then`. So for each then you only need to supply the **newly** recorded events.

## v0.5.x

#### BC breaks

- DomainMessageInterface has been removed, and DomainMessage has been made final.
- Renamed `add` method to `save` for [aggregate root repositories](https://github.com/mbadolato/broadway/commit/9b07dfc4998d70b4c6d25dcacf114a60ea7f1450).

##### Symfony Bundle

- The global `storage_suffix` parameter has been removed and has been replaced with a configuration value: `saga.mongodb.storage_suffix`.

#### Summary of other changes

- New example on how to use child entities.
- The EventSourcing Scenario has been updated to support all the latest changes.
- An AggregateRootScenarioTestCase has been added with an example on how to use it.
- The command bus and event bus have been made more resilient.
- We now publish the decorated event stream on the event bus.
- Added possibility to use binary as UUID column. See README in the Bundle for configuration details.
- The CLI Command in the Bundle doesn't throw errors anymore if the schema already exists.

## v0.4.x

#### BC breaks

- Updated `beberlei/assert` requirement to 2.0.

## v0.3.0

#### BC breaks

- The AggregateFactory is a new required constructor argument for a EventSourcingRepository and the order of the arguments changed.

#### Summary of changes

- Added Aggregate Factories for instantiating aggregates. Now we are not bound to a public constructor.
- A bugfix that caused an infinite loop when supplying a string to the CommandHandler.
- Saga base class is now abstract.
- More typehints to interfaces instead of concrete classes.
- Multiple CS fixes.
```

## File: `LICENSE`
```
Copyright (c) 2020 Broadway project - https://github.com/broadway

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
```

## File: `Makefile`
```
.DEFAULT_GOAL:=help

.PHONY: dependencies
dependencies:
	composer install --no-interaction --no-suggest --no-scripts --ansi

.PHONY: test
test:
	vendor/bin/phpunit --testdox --exclude-group=none --colors=always

.PHONY: qa
qa: php-cs-fixer-ci phpstan

.PHONY: php-cs-fixer
php-cs-fixer:
	vendor/bin/php-cs-fixer fix --no-interaction --allow-risky=yes --diff --verbose

.PHONY: php-cs-fixer-ci
php-cs-fixer-ci:
	vendor/bin/php-cs-fixer fix --no-interaction --allow-risky=yes --diff --verbose

PHONY: phpstan
phpstan:
	vendor/bin/phpstan analyse --level=5 src/

.PHONY: changelog
changelog:
	git log $$(git describe --abbrev=0 --tags)...HEAD --no-merges --pretty=format:"* [%h](http://github.com/${TRAVIS_REPO_SLUG}/commit/%H) %s (%cN)"

.PHONY: license
license:
	vendor/bin/docheader check --no-interaction --ansi -vvv {src,test,examples}

# Based on https://suva.sh/posts/well-documented-makefiles/
help:  ## Display this help
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m<target>\033[0m\n\nTargets:\n"} /^[a-zA-Z_-]+:.*?##/ { printf "  \033[36m%-20s\033[0m %s\n", $$1, $$2 }' $(MAKEFILE_LIST)
```

## File: `README.md`
```markdown
Broadway
========

Broadway is a project providing infrastructure and testing helpers for creating
CQRS and event sourced applications. Broadway tries hard to not get in your
way. The project contains several loosely coupled components that can be used
together to provide a full CQRS\ES experience.

![build status](https://github.com/broadway/broadway/actions/workflows/ci.yml/badge.svg)

## About

Read the blog post about this repository at:
- http://labs.qandidate.com/blog/2014/08/26/broadway-our-cqrs-es-framework-open-sourced/

## Installation

```
$ composer require broadway/broadway
```

## Documentation
You can find detailed documentation of the Broadway bundle on [broadway.github.io/broadway](https://broadway.github.io/broadway/).

Feel free to join #qandidate on freenode with questions and remarks!

## Acknowledgements

The broadway project is heavily inspired by other open source project such as
[AggregateSource], [Axon Framework] and [Ncqrs].

[Axon Framework]: http://www.axonframework.org/
[Ncqrs]: https://github.com/ncqrs/ncqrs
[AggregateSource]: https://github.com/yreynhout/AggregateSource

We also like to thank [Benjamin], [Marijn] and [Mathias] for the conversations
we had along the way that helped us shape the broadway project. In particular
Marijn for giving us access to his in-house developed CQRS framework.

[Benjamin]: https://twitter.com/beberlei
[Marijn]: https://twitter.com/huizendveld
[Mathias]: https://twitter.com/mathiasverraes

## License

MIT, see LICENSE.
```

## File: `UPGRADE.md`
```markdown
# Upgrade to 2.0

## Concrete classes are made final

As it is no longer possible to extend these classes it is necessary to use composition for code reuse.

## PHP 7

Many interfaces have updated method signatures because of added (return) type hints. When implementing
these interfaces the method signatures must adhere to the parent's signatures.

## PHPUnit 6
PHPUnit is required when you use Broadway's test helpers like Scenarios and base test cases in
the `src/*/Testing/*` directories. In this case you will need to update your projects to PHPUnit 6.

## Test helpers
The RepositoryTestCase, EventStoreTest, EventStoreManagementTest are moved from `test` to `src` and into
the `Testing` namespace. It's now easier to use them without autoloading magic but you need to reimport
the classes with the updated namespace in your project.

# Upgrade to 1.0

## Symfony bundle, DBAL event store, Elasticsearch read models and saga are moved to separate repositories.

To retain these functionalities you need to install the following packages:

```
composer require broadway/broadway-bundle
composer require broadway/event-store-dbal
composer require broadway/read-model-elasticsearch
composer require broadway/broadway-saga
```

You can also check the [Broadway demo project](https://github.com/broadway/broadway-demo). 

## New bundle configuration

The bundle allows you to configure your own event store or read model 
implementation using service ids. 

It no longer configures the DBAL event store and Elasticsearch read models 
by default. For more information check the bundle's [README.md](https://github.com/broadway/broadway-bundle/blob/master/README.md).  

## Renamed interfaces and simple implementations

Most interfaces were changed to remove the `Interface` suffix. This meant
also some simple implementations provided by Broadway were changed.

This is the complete list of changes:

### Renamed interfaces

* Broadway/Auditing/CommandSerializerInterface -> CommandSerializer
* Broadway/CommandHandling/CommandBusInterface -> CommandBus
* Broadway/CommandHandling/CommandHandlerInterface -> CommandHandler
* Broadway/EventDispatcher/EventDispatcherInterface -> EventDispatcher
* Broadway/EventHandling/EventBusInterface -> EventBus
* Broadway/EventHandling/EventListenerInterface -> EventListener
* Broadway/EventSourcing/AggregateFactory/AggregateFactoryInterface -> AggregateFactory
* Broadway/EventSourcing/EventSourcedEntityInterface -> EventSourcedEntity
* Broadway/EventSourcing/EventStreamDecoratorInterface -> EventStreamDecorator
* Broadway/EventSourcing/MetadataEnrichment/MetadataEnricherInterface -> MetadataEnricher
* Broadway/EventStore/EventStoreInterface -> EventStore
* Broadway/EventStore/EventVisitorInterface -> EventVisitor
* Broadway/EventStore/Management/EventStoreManagementInterface -> EventStoreManagement
* Broadway/ReadModel/ReadModelInterface -> Identifiable
* Broadway/ReadModel/RepositoryFactoryInterface -> RepositoryFactory
* Broadway/ReadModel/RepositoryInterface -> Repository
* Broadway/ReadModel/SerializableReadModelInterface -> SerializableReadModel
* Broadway/ReadModel/TransferableInterface -> Transferable
* Broadway/Repository/RepositoryInterface -> Repository
* Broadway/Serializer/SerializableInterface -> Serializable
* Broadway/Serializer/SerializerInterface -> Serializer

### Renamed implementations

* Broadway/Auditing/CommandSerializer -> NullByteCommandSerializer
* Broadway/CommandHandling/CommandHandler -> SimpleCommandHandler
* Broadway/EventDispatcher/EventDispatcher -> CallableEventDispatcher
* Broadway/EventSourcing/EventSourcedEntity -> SimpleEventSourcedEntity
* Broadway/ReadModel/ReadModelTestCase -> SerializableReadModelTestCase

### Dropped interfaces
* Broadway/Domain/DomainEventStreamInterface
* Broadway/ReadModel/ProjectorInterface
```

## File: `composer.json`
```json
{
    "name": "broadway/broadway",
    "description": "Infrastructure and testing helpers for creating CQRS and event sourced applications.",
    "keywords": ["cqrs", "event sourcing", "domain-driven design", "ddd"],
    "license": "MIT",
    "require": {
        "beberlei/assert": "^3.0",
        "broadway/uuid-generator": "^1.0",
        "php": ">=7.2"
    },
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
    "require-dev": {
        "monolog/monolog": "~2.0",
        "phpunit/phpunit": "^9.5",
        "ramsey/uuid": "^4.0",
        "broadway/coding-standard": "^1.2",
        "phpstan/phpstan": "^1.0",
        "psr/log": "^1.1.4",
        "phpspec/prophecy": "^1.15"
    },
    "suggest": {
        "psr/log-implementation": "Implementation for PSR3, LoggerInterface",
        "broadway/event-store-dbal": "Event store implementation using doctrine/dbal",
        "broadway/read-model-elasticsearch": "Elasticsearch read model implementation",
        "broadway/broadway-saga": "Saga component for Broadway",
        "broadway/broadway-bundle": "Symfony bundle for broadway/broadway"
    },
    "autoload": {
        "psr-4": {
            "Broadway\\": "src/Broadway/"
        }
    },
    "autoload-dev": {
        "psr-4": {
            "Broadway\\": "test/Broadway/"
        }
    },
    "extra": {
        "branch-alias": {
            "dev-master": "3.0.x-dev"
        }
    }
}
```

## File: `phpstan-baseline.neon`
```
parameters:
	ignoreErrors:
		-
			message: "#^Property Broadway\\\\CommandHandling\\\\Testing\\\\TraceableCommandBus\\:\\:\\$commandHandlers is never read, only written\\.$#"
			count: 1
			path: src/Broadway/CommandHandling/Testing/TraceableCommandBus.php

		-
			message: "#^Unsafe usage of new static\\(\\)\\.$#"
			count: 2
			path: src/Broadway/EventStore/Management/Testing/EventStoreManagementTest.php

```

## File: `phpstan.neon`
```
includes:
    - phpstan-baseline.neon
```

## File: `phpunit.xml.dist`
```
<?xml version="1.0" encoding="UTF-8"?>

<phpunit backupGlobals="false"
         backupStaticAttributes="false"
         colors="true"
         convertErrorsToExceptions="true"
         convertNoticesToExceptions="true"
         convertWarningsToExceptions="true"
         processIsolation="false"
         stopOnFailure="false"
         bootstrap="vendor/autoload.php"
>
  <testsuites>
    <testsuite name="Broadway Test Suite">
      <directory>./test/</directory>
    </testsuite>
    <testsuite name="Broadway Example Test Suite">
      <directory>./examples/</directory>
    </testsuite>
  </testsuites>
  <filter>
    <whitelist>
      <directory suffix=".php">./src/</directory>
    </whitelist>
  </filter>
  <groups>
    <exclude>
      <group>functional</group>
    </exclude>
  </groups>
</phpunit>
```

## File: `brain/knowledge/docs_legacy/examples.md`
```markdown
## Examples

Examples can be found in the [`examples/`][examples] directory. Most of the
examples focus on showing how one of the components works. There is also a more
[deliberate example][example] using several components and showing how you can
test your event sourced model.

[examples]: https://github.com/broadway/broadway/tree/master/examples
[example]: https://github.com/broadway/broadway/tree/master/examples/event-sourced-domain-with-tests
```

## File: `brain/knowledge/docs_legacy/index.md`
```markdown
* Introduction
* Components
    * [Auditing](components/auditing.md)
    * [CommandHandling](components/command_handling.md)
    * [Domain](../../../vault/archives/archive_legacy/node/doc/api/domain.md)
    * [EventDispatcher](components/event_dispatcher.md)
    * [EventHandling](components/event_handling.md)
    * [EventSourcing](components/event_sourcing.md)
    * [EventStore](components/event_store.md)
        * [Doctrine DBAL](https://github.com/broadway/event-store-dbal)
        * [MongoDB](https://github.com/broadway/event-store-mongodb)
    * [Processor](components/processor.md)
    * [ReadModel](components/read_model.md)
        * [Elasticsearch](https://github.com/broadway/read-model-elasticsearch)
        * [MongoDB](https://github.com/broadway/read-model-mongodb)
    * [Repository](../../../core/security/QUARANTINE/vetted/repos/trivy/docs/guide/target/repository.md)
    * [Saga](https://github.com/broadway/broadway-saga)
    * [Sensitive data handling](https://github.com/broadway/broadway-sensitive-data)
    * [Serializer](components/serializer.md)
    * [Snapshotting](https://github.com/broadway/snapshotting)
* [Integrations](../../../core/security/QUARANTINE/vetted/repos/claude_code_templates/cli_tool/components/skills/ai_research/mlops_tensorboard/references/integrations.md)
* [Examples](examples.md)

# Introduction

Broadway is a project providing infrastructure and testing helpers for creating
CQRS and event sourced applications. Broadway tries hard to not get in your
way. The project contains several loosely coupled components that can be used
together to provide a full CQRS\ES experience.

Read the blog post about this repository at: [Bringing CQRS and Event Sourcing to PHP. Open sourcing Broadway!](http://labs.qandidate.com/blog/2014/08/26/broadway-our-cqrs-es-framework-open-sourced/)
```

## File: `brain/knowledge/docs_legacy/integrations.md`
```markdown
# Integrations

- There is a [bundle] available to use with your Symfony application.

- A [Laravel package] is also available to allow the use of Broadway inside a Laravel application.

Contributions for integrations with other projects are appreciated!

[bundle]: https://github.com/broadway/broadway-bundle
[Laravel package]: https://github.com/nWidart/Laravel-broadway
```

## File: `brain/knowledge/docs_legacy/components/auditing.md`
```markdown
Auditing Component
==================

Add an audit trail to your application. Currently enables you to log whether
commands were successful or failed due to an exception.

## Usage

Register the `CommandLogger` event listener with the
`EventDispatchingCommandHandler`. The logger will use the injected logger to
log whether a command was executed successfully or errored.

## Example

The [`examples/`][examples] directory at the root of the project contains a
runnable auditing (`auditing`). The code you find there contains comments with
what is happening.

[examples]: ../../examples/
```

## File: `brain/knowledge/docs_legacy/components/command_handling.md`
```markdown
CommandHandling Component
=========================

Primitives to use commands in your application.

## Command bus

An interface and two simple implementations of a command bus where commands can
be dispatched on.

## Command handler

An interface and convenient base class that command handlers can extend.

The base class provided by this component uses a convention to find out whether
the command handler can execute a command or not. To signal that your command
handler can handle a command `ExampleCommand`, just implement the
`handleExampleCommand` method in the extending class.

```php
use Broadway\CommandHandling\SimpleCommandHandler;

/**
 * A command handler that only handles ExampleCommand commands.
 */
class ExampleCommandHandler extends SimpleCommandHandler
{
    /**
     * Method handling ExampleCommand commands.
     *
     * The fact that this method handles the ExampleCommand is signalled by the
     * convention of the method name: `handle<CommandClassName>`.
     */
    public function handleExampleCommand(ExampleCommand $command)
    {
        echo $command->getMessage() . "\n";
    }
}
```

## Testing

A helper to implement scenario based tests for command handlers that use an
event store.

## Example

The [`examples/`][examples] directory at the root of the project contains a
runnable command handling example (`command-handling`). The code you find there
contains comments with what is happening.

[examples]: ../../examples/
```

## File: `brain/knowledge/docs_legacy/components/domain.md`
```markdown
Domain Component
================

Component that contains the domain abstractions of the broadway framework.

Main interesting abstractions include the aggregate root and domain messages/events.
```

## File: `brain/knowledge/docs_legacy/components/event_dispatcher.md`
```markdown
Event Dispatcher Component
==========================

Event dispatcher component providing event dispatchers to your application.

The component provides an event dispatcher interface and a simple
implementation. In the future it would be great to have integrations with other
implementations.

## Example

The [`examples/`][examples] directory at the root of the project contains a
runnable event dispatcher example (`event-dispatcher`). The code you find there
contains comments with what is happening.

[examples]: ../../examples/
```

## File: `brain/knowledge/docs_legacy/components/event_handling.md`
```markdown
Event Handling Component
========================

Provides event bus and event listeners abstractions.

The component provides interfaces for an event bus and event listeners, but
also an implementation of a simple event bus and an event bus that will record
published events (useful for testing).

## Example

The [`examples/`][examples] directory at the root of the project contains a
runnable event handling example (`event-handling`). The code you find there
contains comments with what is happening.

[examples]: ../../examples/
```

## File: `brain/knowledge/docs_legacy/components/event_sourcing.md`
```markdown
Event Sourcing Component
========================

Component building on other broadway components to provide a full event
sourcing experience.

This component provides base classes for event sourced aggregate roots and
entities, an event sourced repository implementation and testing helpers.
```

## File: `brain/knowledge/docs_legacy/components/event_store.md`
```markdown
Event Store Component
=====================

The event store component provides an interface and several implementations of
an event store.

It currently has an in-memory event store implementation that is useful for using in tests.

The [broadway/event-store-dbal] package provides an event store implementation backed by a
relational database based on [doctrine/dbal].

[broadway/event-store-dbal]: https://github.com/broadway/event-store-dbal
[doctrine/dbal]: https://github.com/doctrine/dbal
```

## File: `brain/knowledge/docs_legacy/components/processor.md`
```markdown
Processor Component
===================

Provides processor capabilities to your application.
```

## File: `brain/knowledge/docs_legacy/components/read_model.md`
```markdown
Read Model Component
====================

Add read models to your application.

This component provides storage for your read models, a projector
implementation to create read models from event streams and testing helpers.

### Basic implementation

Note that the repositories are meant for basic read/writes. Use them to create and retrieve read models.
They should not be used to do complex queries. Please use the underlaying storage directly to do more advanced querying.
```

## File: `brain/knowledge/docs_legacy/components/repository.md`
```markdown
Repository Component
====================

Component providing an abstraction of the storage of aggregates.

> Note: there is not a lot to see here right now. In the future this component
> will deal with more details about locking and storage conflicts.
```

## File: `brain/knowledge/docs_legacy/components/serializer.md`
```markdown
Serializer Component
====================

Serializer component provides serializers to your application.

The component provides a simple serializer interface and a serializer
implementation based on "handwritten" serializers. In the future it would be
great to have support for more broadly used serializer implementations.

## Example

The [`examples/`][examples] directory at the root of the project contains a
runnable serializer example (`serializer`). The code you find there
contains comments with what is happening.

[examples]: ../../examples/
```

## File: `examples/bootstrap.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

if (file_exists($file = __DIR__.'/../vendor/autoload.php')) {
    $loader = require_once $file;
} else {
    throw new RuntimeException('Install dependencies to the examples.');
}

/**
 * Simple logger to be used in examples.
 */
class StdoutLogger extends Psr\Log\AbstractLogger
{
    public function log($level, $message, array $context = [])
    {
        echo sprintf("[%s] %s - %s\n", $level, $message, json_encode($context));
    }
}
```

## File: `examples/auditing/log-command-status.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

require_once __DIR__.'/../bootstrap.php';

/*
 * Some setup and helpers. Real example below. ;)
 */
class ExampleCommandHandler extends Broadway\CommandHandling\SimpleCommandHandler
{
    public function handleExampleCommand(ExampleCommand $command)
    {
    }

    public function handleExampleFailureCommand(ExampleFailureCommand $command)
    {
        throw new RuntimeException('Failed!!');
    }
}

class BaseCommand
{
    private $message;

    public function __construct($message)
    {
        $this->message = $message;
    }

    public function getMessage()
    {
        return $this->message;
    }
}

class ExampleCommand extends BaseCommand
{
}
class ExampleFailureCommand extends BaseCommand
{
}

// Setup the system to handle commands
$commandHandler = new ExampleCommandHandler();
$eventDispatcher = new Broadway\EventDispatcher\CallableEventDispatcher();
$simpleCommandBus = new Broadway\CommandHandling\SimpleCommandBus();
$commandBus = new Broadway\CommandHandling\EventDispatchingCommandBus($simpleCommandBus, $eventDispatcher);
$commandBus->subscribe($commandHandler);

// Dependencies of auditing logger
$logger = new StdoutLogger();
$commandSerializer = new Broadway\Auditing\NullByteCommandSerializer();

/*
 * The actual example!
 */

// setup the command logger
$commandAuditLogger = new Broadway\Auditing\CommandLogger($logger, $commandSerializer);

// register the command logger with the event dispatcher of the command bus
$eventDispatcher->addListener('broadway.command_handling.command_success', [$commandAuditLogger, 'onCommandHandlingSuccess']);
$eventDispatcher->addListener('broadway.command_handling.command_failure', [$commandAuditLogger, 'onCommandHandlingFailure']);

echo "Dispatching the command that will succeed.\n";
$command = new ExampleCommand('Hi from command!');
$commandBus->dispatch($command);

try {
    echo "Dispatching the command that will fail.\n";
    $command = new ExampleFailureCommand('Hi from failure command!');
    $commandBus->dispatch($command);
} catch (Exception $e) {
    echo "See? It failed.\n";
}
```

## File: `examples/command-handling/command-handling.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

require_once __DIR__.'/../bootstrap.php';

/**
 * A command handler that only handles ExampleCommand commands.
 */
class ExampleCommandHandler extends Broadway\CommandHandling\SimpleCommandHandler
{
    /**
     * Method handling ExampleCommand commands.
     *
     * The fact that this method handles the ExampleCommand is signalled by the
     * convention of the method name: `handle<CommandClassName>`.
     */
    public function handleExampleCommand(ExampleCommand $command)
    {
        echo $command->getMessage()."\n";
    }
}

/**
 * Command object.
 */
class ExampleCommand
{
    private $message;

    public function __construct($message)
    {
        $this->message = $message;
    }

    public function getMessage()
    {
        return $this->message;
    }
}

// Setup the command handler
$commandHandler = new ExampleCommandHandler();

// Create a command bus and subscribe the command handler at the command bus
$commandBus = new Broadway\CommandHandling\SimpleCommandBus();
$commandBus->subscribe($commandHandler);

// Create and dispatch the command!
$command = new ExampleCommand('Hi from command!');
$commandBus->dispatch($command);
```

## File: `examples/event-dispatcher/event-dispatcher.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

require_once __DIR__.'/../bootstrap.php';

$eventDispatcher = new Broadway\EventDispatcher\CallableEventDispatcher();

// You can register any callable
$eventDispatcher->addListener('my_event', function ($arg1, $arg2) {
    echo "Arg1: $arg1\n";
    echo "Arg2: $arg2\n";
});

// Dispatch with an array of arguments
$eventDispatcher->dispatch('my_event', ['one', 'two']);
```

## File: `examples/event-handling/event-handling.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

require_once __DIR__.'/../bootstrap.php';

// An event listener implements the handle method
class MyEventListener implements Broadway\EventHandling\EventListener
{
    public function handle(Broadway\Domain\DomainMessage $domainMessage)
    {
        echo "Got a domain message, yay!\n";
    }
}

// Create the event bus and subscribe the created event listener
$eventBus = new Broadway\EventHandling\SimpleEventBus();
$eventListener = new MyEventListener();
$eventBus->subscribe($eventListener);

// Create a domain event stream to publish
$metadata = new Broadway\Domain\Metadata(['source' => 'example']);
$domainMessage = Broadway\Domain\DomainMessage::recordNow(42, 1, $metadata, new stdClass());
$domainEventStream = new Broadway\Domain\DomainEventStream([$domainMessage]);

// Publish the message, and get output from the event handler \o/
$eventBus->publish($domainEventStream);
```

## File: `examples/event-handling-using-read-models/InvitationProjectorsTest.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

require_once __DIR__.'/ReadModelClasses.php';

class InvitationStatusProjectorTest extends Broadway\ReadModel\Testing\ProjectorScenarioTestCase
{
    /**
     * The createProjector function allows you to inject more dependencies into your projector.
     */
    protected function createProjector(Broadway\ReadModel\InMemory\InMemoryRepository $repository): Broadway\ReadModel\Projector
    {
        $this->repository = $repository;

        return new InvitationStatusProjector($repository);
    }

    /**
     * @test
     */
    public function it_keeps_track_of_the_status_of_an_invitation_when_someone_is_invited()
    {
        $invitationId = '1337';
        $expectedReadModel = new InvitationStatusReadModel($invitationId);
        $this->assertEquals($expectedReadModel->getId(), $invitationId);
        $this->assertTrue($expectedReadModel->getIsOpen());
        $this->assertFalse($expectedReadModel->getIsClosed());
        $this->assertFalse($expectedReadModel->getIsAccepted());
        $this->assertFalse($expectedReadModel->getIsDeclined());

        $this->scenario
            ->given([])
            ->when(new InvitedEvent($invitationId, 'fritsjanb'))
            ->then([$expectedReadModel]);
    }

    /**
     * @test
     */
    public function it_keeps_track_of_the_status_when_an_invitation_is_accepted()
    {
        $invitationId = '1337';

        $expectedReadModel = new InvitationStatusReadModel($invitationId);
        $expectedReadModel->flagAccepted();

        $this->assertEquals($expectedReadModel->getId(), $invitationId);
        $this->assertFalse($expectedReadModel->getIsOpen());
        $this->assertTrue($expectedReadModel->getIsClosed());
        $this->assertTrue($expectedReadModel->getIsAccepted());
        $this->assertFalse($expectedReadModel->getIsDeclined());

        $this->scenario
            ->given([new InvitedEvent($invitationId, 'fritsjanb')])
            ->when(new AcceptedEvent($invitationId))
            ->then([$expectedReadModel]);
    }

    /**
     * @test
     */
    public function it_keeps_track_of_the_status_when_an_invitation_is_declined()
    {
        $invitationId = '1337';

        $expectedReadModel = new InvitationStatusReadModel($invitationId);
        $expectedReadModel->flagDeclined();

        $this->assertEquals($expectedReadModel->getId(), $invitationId);
        $this->assertFalse($expectedReadModel->getIsOpen());
        $this->assertTrue($expectedReadModel->getIsClosed());
        $this->assertFalse($expectedReadModel->getIsAccepted());
        $this->assertTrue($expectedReadModel->getIsDeclined());

        $this->scenario
            ->given([new InvitedEvent($invitationId, 'fritsjanb')])
            ->when(new DeclinedEvent($invitationId))
            ->then([$expectedReadModel]);
    }
}

class InvitationStatusCountProjectorTest extends PHPUnit\Framework\TestCase
{
    /**
     * @test
     */
    public function it_keeps_track_of_the_status_counts_of_all_invitations()
    {
        $projector = new InvitationStatusCountProjector(new CounterRepository());

        $id1 = 'id-1';
        $id2 = 'id-2';
        $id3 = 'id-3';
        $projector->handle($this->createDomainMessageForEvent(new InvitedEvent($id1, 'fritsjanb'), 0));
        $projector->handle($this->createDomainMessageForEvent(new InvitedEvent($id2, 'John Doe'), 0));
        $projector->handle($this->createDomainMessageForEvent(new AcceptedEvent($id2), 1));
        $projector->handle($this->createDomainMessageForEvent(new InvitedEvent($id3, 'Jane Doe'), 0));
        $projector->handle($this->createDomainMessageForEvent(new DeclinedEvent($id3), 1));

        $expectedCounters = new Counters();
        $expectedCounters->invitedCounter = 3;
        $expectedCounters->openCounter = 1;
        $expectedCounters->acceptedCounter = 1;
        $expectedCounters->declinedCounter = 1;

        $this->assertEquals($projector->exposeStatusCounts(), $expectedCounters);
    }

    private function createDomainMessageForEvent(InvitationEvent $event, $playhead): Broadway\Domain\DomainMessage
    {
        $occurredOn = Broadway\Domain\DateTime::now();

        return new Broadway\Domain\DomainMessage($event->invitationId, $playhead, new Broadway\Domain\Metadata([]), $event, $occurredOn);
    }
}
```

## File: `examples/event-handling-using-read-models/ReadModelClasses.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

require_once __DIR__.'/../bootstrap.php';

// We reuse the Invites aggregate and events
require_once __DIR__.'/../event-sourced-domain-with-tests/Invites.php';

use Broadway\ReadModel\Repository;

/*
 * A Projector is an EventListener and can be registered with the EventBus.
 * When an Aggregated is saved to an an EventSourcingRepository its
 * DomainEventStream is stored in the EventStore and the events are published
 * to the EventBus. The EventBus passes the events to all interested
 * EventListeners.
 *
 * Broadway ships with a ReadModel Repository class that can be used to help
 * make and store read models. This example's InvitationStatusProjector shows
 * you how this is done.
 *
 * However, you can easily change how you are going to store and update your
 * read models - simply extend a Projector to get events and do anything you
 * want. InvitationStatusCountProjector shows a simple example of what is
 * possible.
 */
class InvitationStatusProjector extends Broadway\ReadModel\Projector
{
    private $repository;

    public function __construct(Repository $repository)
    {
        $this->repository = $repository;
    }

    public function exposeStatusOfInvitation($invitationId): InvitationStatusReadModel
    {
        return $this->loadReadModel($invitationId);
    }

    protected function applyInvitedEvent(InvitedEvent $event)
    {
        $readModel = new InvitationStatusReadModel($event->invitationId);

        $this->repository->save($readModel);
    }

    protected function applyAcceptedEvent(AcceptedEvent $event)
    {
        $readModel = $this->loadReadModel($event->invitationId);
        $readModel->flagAccepted();

        $this->repository->save($readModel);
    }

    protected function applyDeclinedEvent(DeclinedEvent $event)
    {
        $readModel = $this->loadReadModel($event->invitationId);
        $readModel->flagDeclined();

        $this->repository->save($readModel);
    }

    private function loadReadModel($id)
    {
        return $this->repository->find($id);
    }
}

/**
 * InvitationStatusReadModel implements Identifiable (through
 * SerializableReadModel) in order to support the ReadModel Repository. If you
 * are not using this Repository, there is no need to implement Identifiable
 * (nor SerializableReadModel).
 */
class InvitationStatusReadModel implements Broadway\ReadModel\SerializableReadModel
{
    private $invitationId;
    private $isOpen = true;
    private $isAccepted = false;
    private $isDeclined = false;

    public function __construct(string $invitationId)
    {
        $this->invitationId = $invitationId;
    }

    public function getId(): string
    {
        return $this->invitationId;
    }

    public function flagAccepted(): void
    {
        $this->isAccepted = true;
        $this->isOpen = false;
        $this->isDeclined = false;
    }

    public function flagDeclined(): void
    {
        $this->isDeclined = true;
        $this->isOpen = false;
        $this->isAccepted = false;
    }

    public static function deserialize(array $data)
    {
        $readModel = new self($data['invitationId']);

        $readModel->isOpen = $data['isOpen'];
        $readModel->isAccepted = $data['isAccepted'];
        $readModel->isDeclined = $data['isDeclined'];

        return $readModel;
    }

    public function serialize(): array
    {
        return [
            'invitationId' => $this->invitationId,
            'isOpen' => $this->isOpen,
            'isAccepted' => $this->isAccepted,
            'isDeclined' => $this->isDeclined,
        ];
    }

    public function getIsOpen(): bool
    {
        return $this->isOpen;
    }

    public function getIsClosed(): bool
    {
        return !$this->isOpen;
    }

    public function getIsAccepted(): bool
    {
        return $this->isAccepted;
    }

    public function getIsDeclined(): bool
    {
        return $this->isDeclined;
    }
}

/*
 * The following projector keeps track of how many invitations are open,
 * closed, accepted and declined. Note that it does not use a regular
 * ReadModel\Repository or Identifiable ReadModel.
 *
 * The example keeps track of the counts in memory. In a real application some
 * form of storage should be used.
 */
class InvitationStatusCountProjector extends Broadway\ReadModel\Projector
{
    private $repository;

    public function __construct(CounterRepository $repository)
    {
        $this->repository = $repository;
    }

    public function exposeStatusCounts(): Counters
    {
        return $this->getCounters();
    }

    protected function applyInvitedEvent(InvitedEvent $event)
    {
        $counters = $this->getCounters();
        $counters->applyInvited();

        $this->storeCounters($counters);
    }

    protected function applyAcceptedEvent(AcceptedEvent $event)
    {
        $counters = $this->getCounters();
        $counters->applyAccepted();

        $this->storeCounters($counters);
    }

    protected function applyDeclinedEvent(DeclinedEvent $event)
    {
        $counters = $this->getCounters();
        $counters->applyDeclined();

        $this->storeCounters($counters);
    }

    private function storeCounters($counters)
    {
        $this->repository->storeCounters($counters);
    }

    private function getCounters()
    {
        return $this->repository->getCounters();
    }
}

class CounterRepository
{
    private $counters;

    public function storeCounters(Counters $counters): void
    {
        $this->counters = $counters;
    }

    public function getCounters(): Counters
    {
        if (null !== $this->counters) {
            return $this->counters;
        }

        return new Counters();
    }
}

class Counters
{
    public $invitedCounter = 0;
    public $acceptedCounter = 0;
    public $declinedCounter = 0;
    public $openCounter = 0;

    public function applyInvited()
    {
        ++$this->invitedCounter;
        ++$this->openCounter;
    }

    public function applyAccepted()
    {
        ++$this->acceptedCounter;
        --$this->openCounter;
    }

    public function applyDeclined()
    {
        ++$this->declinedCounter;
        --$this->openCounter;
    }
}
```

## File: `examples/event-handling-using-read-models/example-creating-readmodels.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

require_once __DIR__.'/ReadModelClasses.php';

$invitationStatusProjector = new InvitationStatusProjector(new Broadway\ReadModel\InMemory\InMemoryRepository());
$invitationStatusCountProjector = new InvitationStatusCountProjector(new CounterRepository());

$eventStore = new Broadway\EventStore\InMemoryEventStore();

// We subscribe the projectors to the event bus
$eventBus = new Broadway\EventHandling\SimpleEventBus();
$eventBus->subscribe($invitationStatusProjector);
$eventBus->subscribe($invitationStatusCountProjector);

$commandBus = new Broadway\CommandHandling\SimpleCommandBus();
// The InvitationRepository gets both the event store and event bus. When
// saving an aggregate, events are persisted in the event store, and all
// subscribers to the event bus get notified.
$commandBus->subscribe(new InvitationCommandHandler(new InvitationRepository($eventStore, $eventBus)));

// We dispatch the commands to the command bus. The command handler receives
// the commands and stores them to the InvitationRepository. The
// InvitationRepository makes sure the events are persisted in the event store,
// and passes the events to the event bus. The event bus makes sure our
// projectors receives the events, allowing our read models to be updated.
$commandBus->dispatch(new InviteCommand('invitationId', 'John Doe'));
$commandBus->dispatch(new InviteCommand('anotherInvitation', 'Jane Doe'));
$commandBus->dispatch(new InviteCommand('a third invitation', '<insert name here>'));
$commandBus->dispatch(new AcceptCommand('invitationId'));
$commandBus->dispatch(new DeclineCommand('a third invitation'));

var_dump($invitationStatusProjector->exposeStatusOfInvitation('invitationId'));
var_dump($invitationStatusCountProjector->exposeStatusCounts());
```

## File: `examples/event-sourced-child-entity/Parts.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

require_once __DIR__.'/../bootstrap.php';

/**
 * Part aggregate root.
 */
class Part extends Broadway\EventSourcing\EventSourcedAggregateRoot
{
    private $partId;
    private $manufacturer;

    /**
     * Factory method to create a part.
     */
    public static function manufacture($partId, $manufacturerId, $manufacturerName)
    {
        $part = new self();

        // After instantiation of the object we apply the "PartWasManufacturedEvent".
        $part->apply(new PartWasManufacturedEvent($partId, $manufacturerId, $manufacturerName));

        return $part;
    }

    /**
     * Every aggregate root will expose its id.
     */
    public function getAggregateRootId(): string
    {
        return $this->partId;
    }

    public function renameManufacturer($manufacturerName)
    {
        $this->manufacturer->rename($manufacturerName);
    }

    public function applyPartWasManufacturedEvent(PartWasManufacturedEvent $event)
    {
        $this->partId = $event->partId;

        // We create the entity in our event handler so that it will be created
        // when the aggregate root is reconstituted from an event stream. Once
        // the child entity is instantiated and returned by getChildEntities()
        // it can emit and apply events itself.
        $this->manufacturer = new Manufacturer(
            $event->partId,
            $event->manufacturerId,
            $event->manufacturerName
        );
    }

    protected function getChildEntities(): array
    {
        // Since the aggregate root always handles the events first we can rely
        // on $this->manufacturer being set by the time the child entities are
        // requested *provided* PartWasManufacturedEvent is the first event in
        // the event stream.
        return [$this->manufacturer];
    }
}

class Manufacturer extends Broadway\EventSourcing\SimpleEventSourcedEntity
{
    private $partId;
    private $manufacturerId;
    private $manufacturerName;

    public function __construct($partId, $manufacturerId, $manufacturerName)
    {
        $this->partId = $partId;
        $this->manufacturerId = $manufacturerId;
        $this->manufacturerName = $manufacturerName;
    }

    public function rename($manufacturerName)
    {
        if ($this->manufacturerName === $manufacturerName) {
            // If the name is not actually different we do not need to do
            // anything here.
            return;
        }

        // This event may also be handled by the aggregate root.
        $this->apply(new PartManufacturerWasRenamedEvent($this->partId, $manufacturerName));
    }

    protected function applyPartManufacturerWasRenamedEvent(PartManufacturerWasRenamedEvent $event)
    {
        $this->manufacturerName = $event->manufacturerName;
    }
}

class ManufacturePartCommand
{
    public $partId;
    public $manufacturerId;
    public $manufacturerName;

    public function __construct($partId, $manufacturerId, $manufacturerName)
    {
        $this->partId = $partId;
        $this->manufacturerId = $manufacturerId;
        $this->manufacturerName = $manufacturerName;
    }
}

class PartWasManufacturedEvent
{
    public $partId;
    public $manufacturerId;
    public $manufacturerName;

    public function __construct($partId, $manufacturerId, $manufacturerName)
    {
        $this->partId = $partId;
        $this->manufacturerId = $manufacturerId;
        $this->manufacturerName = $manufacturerName;
    }
}

class RenameManufacturerForPartCommand
{
    public $partId;
    public $manufacturerName;

    public function __construct($partId, $manufacturerName)
    {
        $this->partId = $partId;
        $this->manufacturerName = $manufacturerName;
    }
}

class PartManufacturerWasRenamedEvent
{
    public $partId;
    public $manufacturerName;

    public function __construct($partId, $manufacturerName)
    {
        $this->partId = $partId;
        $this->manufacturerName = $manufacturerName;
    }
}

/**
 * A repository that will only store and retrieve Part aggregate roots.
 */
class PartRepository extends Broadway\EventSourcing\EventSourcingRepository
{
    public function __construct(Broadway\EventStore\EventStore $eventStore, Broadway\EventHandling\EventBus $eventBus)
    {
        parent::__construct($eventStore, $eventBus, 'Part', new Broadway\EventSourcing\AggregateFactory\PublicConstructorAggregateFactory());
    }
}

/*
 * A command handler will be registered with the command bus and handle the
 * commands that are dispatched.
 */
class PartCommandHandler extends Broadway\CommandHandling\SimpleCommandHandler
{
    private $repository;

    public function __construct(Broadway\EventSourcing\EventSourcingRepository $repository)
    {
        $this->repository = $repository;
    }

    /**
     * A new part aggregate root is created and added to the repository.
     */
    protected function handleManufacturePartCommand(ManufacturePartCommand $command)
    {
        $part = Part::manufacture($command->partId, $command->manufacturerId, $command->manufacturerName);

        $this->repository->save($part);
    }

    /**
     * An existing part aggregate root is loaded and renameManufacturerTo() is
     * called.
     */
    protected function handleRenameManufacturerForPartCommand(RenameManufacturerForPartCommand $command)
    {
        $part = $this->repository->load($command->partId);

        $part->renameManufacturer($command->manufacturerName);

        $this->repository->save($part);
    }
}
```

## File: `examples/event-sourced-child-entity/PartsTest.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

use Broadway\CommandHandling\CommandHandler;

require_once __DIR__.'/Parts.php';

/**
 * We drive the tests of our aggregate root through the command handler.
 *
 * A command handler scenario consists of three steps:
 *
 * - First, the scenario is setup with a history of events that already took place.
 * - Second, a command is dispatched (this is handled by the command handler)
 * - Third, the outcome is asserted. This can either be 1) some events are
 *   recorded, or 2) an exception is thrown.
 */
class PartsCommandHandlerTest extends Broadway\CommandHandling\Testing\CommandHandlerScenarioTestCase
{
    private $generator;

    protected function setUp(): void
    {
        parent::setUp();
        $this->generator = new Broadway\UuidGenerator\Rfc4122\Version4Generator();
    }

    protected function createCommandHandler(Broadway\EventStore\EventStore $eventStore, Broadway\EventHandling\EventBus $eventBus): CommandHandler
    {
        $repository = new PartRepository($eventStore, $eventBus);

        return new PartCommandHandler($repository);
    }

    /**
     * @test
     */
    public function it_can_manufacture()
    {
        $id = $this->generator->generate();

        $this->scenario
            ->withAggregateId($id)
            ->given([])
            ->when(new ManufacturePartCommand($id, 'acme', 'Acme, Inc'))
            ->then([new PartWasManufacturedEvent($id, 'acme', 'Acme, Inc')]);
    }

    /**
     * @test
     */
    public function it_can_rename_manufacturer()
    {
        $id = $this->generator->generate();

        $this->scenario
            ->withAggregateId($id)
            ->given([new PartWasManufacturedEvent($id, 'acme', 'Acme, Inc')])
            ->when(new RenameManufacturerForPartCommand($id, 'Acme, Inc.'))
            ->then([new PartManufacturerWasRenamedEvent($id, 'Acme, Inc.')]);
    }

    /**
     * @test
     */
    public function it_does_not_rename_manufacturer_to_the_same_name()
    {
        $id = $this->generator->generate();

        $this->scenario
            ->withAggregateId($id)
            ->given([
                new PartWasManufacturedEvent($id, 'acme', 'Acme, Inc'),
                new PartWasManufacturedEvent($id, 'acme', 'Acme, Inc.'),
            ])
            ->when(new RenameManufacturerForPartCommand($id, 'Acme, Inc.'))
            ->then([]);
    }
}
```

## File: `examples/event-sourced-child-entity/README.md`
```markdown
Event sourced child entity with tests
=====================================

A small example of an implementation of a small domain model that includes an
aggregate root with a child entity. The example consists of two files. The
first file `Parts` contains the implementation of the domain model. The second
file `PartsTest` contains a PHPUnit test suite to test the domain.

The two files contain comments about what is happening.

The PHPUnit tests can be run by changing to this directory and running:

```bash
$ phpunit .
PHPUnit 4.1.0 by Sebastian Bergmann.

.......

Time: 70 ms, Memory: 4.00Mb

OK (7 tests, 9 assertions)
```
```

## File: `examples/event-sourced-domain-with-tests/InvitationCommandHandlerTest.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

use Broadway\CommandHandling\CommandHandler;

require_once __DIR__.'/Invites.php';

/**
 * We drive the tests of our aggregate root through the command handler.
 *
 * A command handler scenario consists of three steps:
 *
 * - First, the scenario is setup with a history of events that already took place.
 * - Second, a command is dispatched (this is handled by the command handler)
 * - Third, the outcome is asserted. This can either be 1) some events are
 *   recorded, or 2) an exception is thrown.
 */
class InvitationCommandHandlerTest extends Broadway\CommandHandling\Testing\CommandHandlerScenarioTestCase
{
    private $generator;

    protected function setUp(): void
    {
        parent::setUp();
        $this->generator = new Broadway\UuidGenerator\Rfc4122\Version4Generator();
    }

    protected function createCommandHandler(Broadway\EventStore\EventStore $eventStore, Broadway\EventHandling\EventBus $eventBus): CommandHandler
    {
        $repository = new InvitationRepository($eventStore, $eventBus);

        return new InvitationCommandHandler($repository);
    }

    /**
     * @test
     */
    public function it_can_invite_someone()
    {
        $id = $this->generator->generate();

        $this->scenario
            ->withAggregateId($id)
            ->given([])
            ->when(new InviteCommand($id, 'asm89'))
            ->then([new InvitedEvent($id, 'asm89')]);
    }

    /**
     * @test
     */
    public function new_invites_can_be_accepted()
    {
        $id = $this->generator->generate();

        $this->scenario
            ->withAggregateId($id)
            ->given([new InvitedEvent($id, 'asm89')])
            ->when(new AcceptCommand($id))
            ->then([new AcceptedEvent($id)]);
    }

    /**
     * @test
     */
    public function accepting_an_accepted_invite_yields_no_change()
    {
        $id = $this->generator->generate();

        $this->scenario
            ->withAggregateId($id)
            ->given([new InvitedEvent($id, 'asm89'), new AcceptedEvent($id)])
            ->when(new AcceptCommand($id))
            ->then([]);
    }

    /**
     * @test
     */
    public function an_accepted_invite_cannot_be_declined()
    {
        $this->expectException(RuntimeException::class);
        $this->expectExceptionMessage('Already accepted');

        $id = $this->generator->generate();

        $this->scenario
            ->withAggregateId($id)
            ->given([new InvitedEvent($id, 'asm89'), new AcceptedEvent($id)])
            ->when(new DeclineCommand($id));
    }

    /**
     * @test
     */
    public function new_invites_can_be_declined()
    {
        $id = $this->generator->generate();

        $this->scenario
            ->withAggregateId($id)
            ->given([new InvitedEvent($id, 'asm89')])
            ->when(new DeclineCommand($id))
            ->then([new DeclinedEvent($id)]);
    }

    /**
     * @test
     */
    public function declining_a_declined_invite_yields_no_change()
    {
        $id = $this->generator->generate();

        $this->scenario
            ->withAggregateId($id)
            ->given([new InvitedEvent($id, 'asm89'), new DeclinedEvent($id)])
            ->when(new DeclineCommand($id))
            ->then([]);
    }

    /**
     * @test
     */
    public function a_declined_invite_cannot_be_accepted()
    {
        $this->expectException(RuntimeException::class);
        $this->expectExceptionMessage('Already declined');

        $id = $this->generator->generate();

        $this->scenario
            ->withAggregateId($id)
            ->given([new InvitedEvent($id, 'asm89'), new DeclinedEvent($id)])
            ->when(new AcceptCommand($id));
    }
}
```

## File: `examples/event-sourced-domain-with-tests/Invites.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

use Broadway\Serializer\Serializable;

require_once __DIR__.'/../bootstrap.php';

/**
 * Invitation aggregate root.
 *
 * The aggregate root will guard that the invitation can only be accepted OR
 * declined, but not both.
 */
class Invitation extends Broadway\EventSourcing\EventSourcedAggregateRoot
{
    private $accepted = false;
    private $declined = false;
    private $invitationId;

    /**
     * Factory method to create an invitation.
     */
    public static function invite($invitationId, $name)
    {
        $invitation = new self();

        // After instantiation of the object we apply the "InvitedEvent".
        $invitation->apply(new InvitedEvent($invitationId, $name));

        return $invitation;
    }

    /**
     * Every aggregate root will expose its id.
     *
     * {@inheritdoc}
     */
    public function getAggregateRootId(): string
    {
        return $this->invitationId;
    }

    /*
     * The two methods below are part of the public API of the aggregate root.
     */

    public function accept()
    {
        // throw if already declined
        if ($this->declined) {
            throw new RuntimeException('Already declined.');
        }

        /* If the invitation is already accepted, nothing happens we do not
         * throw an exception, but also no event is recorded. This is one way of
         * implementing idempotency in your event sourced aggregate roots
         */
        if ($this->accepted) {
            return;
        }

        $this->apply(new AcceptedEvent($this->invitationId));
    }

    public function decline()
    {
        if ($this->accepted) {
            throw new RuntimeException('Already accepted.');
        }

        if ($this->declined) {
            return;
        }

        $this->apply(new DeclinedEvent($this->invitationId));
    }

    /*
     * The methods below are called as the aggregate root is reconstituted from
     * the previously recorded events.
     */

    protected function applyAcceptedEvent(AcceptedEvent $event)
    {
        /* if we encounter an AcceptedEvent we change the internal state of the
         * aggregate root. This happens if the aggregate root gets reconstituted.
         */
        $this->accepted = true;
    }

    protected function applyDeclinedEvent(DeclinedEvent $event)
    {
        $this->declined = true;
    }

    protected function applyInvitedEvent(InvitedEvent $event)
    {
        $this->invitationId = $event->invitationId;
    }
}

/**
 * A repository that will only store and retrieve Invitation aggregate roots.
 *
 * This repository uses the base class provided by the EventSourcing component.
 */
class InvitationRepository extends Broadway\EventSourcing\EventSourcingRepository
{
    public function __construct(Broadway\EventStore\EventStore $eventStore, Broadway\EventHandling\EventBus $eventBus)
    {
        parent::__construct($eventStore, $eventBus, 'Invitation', new Broadway\EventSourcing\AggregateFactory\PublicConstructorAggregateFactory());
    }
}

/*
 * When using CQRS with commands, a lot of times you will find that you have a
 * command object and a "dual" event. Mind though that this is not always the
 * case. The following classes show the commands and events for our small
 * domain model.
 */

/* All commands and events below will cary the id of the aggregate root. For
 * our convenience and readability later on we provide base classes that hold
 * this data.
 */
abstract class InvitationCommand
{
    public $invitationId;

    public function __construct($invitationId)
    {
        $this->invitationId = $invitationId;
    }
}
abstract class InvitationEvent implements Serializable
{
    public $invitationId;

    public function __construct($invitationId)
    {
        $this->invitationId = $invitationId;
    }

    public function serialize(): array
    {
        return ['invitationId' => $this->invitationId];
    }

    public static function deserialize(array $eventData)
    {
        return new static($eventData['invitationId']);
    }
}

// The "real" commands and events below.
class InviteCommand extends InvitationCommand
{
    public $name;

    public function __construct($invitationId, $name)
    {
        parent::__construct($invitationId);

        $this->name = $name;
    }
}

class InvitedEvent extends InvitationEvent
{
    public $name;

    public function __construct($invitationId, $name)
    {
        parent::__construct($invitationId);

        $this->name = $name;
    }

    public function serialize(): array
    {
        return [
            'invitationId' => $this->invitationId,
            'name' => $this->name,
        ];
    }

    public static function deserialize(array $eventData)
    {
        $event = new static($eventData['invitationId']);
        $event->name = $eventData['name'];

        return $event;
    }
}

// The meaning from these commands and events can be found in the name :)
class AcceptCommand extends InvitationCommand
{
}
class AcceptedEvent extends InvitationEvent
{
}
class DeclineCommand extends InvitationCommand
{
}
class DeclinedEvent extends InvitationEvent
{
}

/*
 * A command handler will be registered with the command bus and handle the
 * commands that are dispatched. The command handler can be seen as a small
 * layer between your application code and the actual domain code.
 *
 * In the end a command handler listens for commands and translates commands to
 * method calls on the actual aggregate roots.
 */
class InvitationCommandHandler extends Broadway\CommandHandling\SimpleCommandHandler
{
    private $repository;

    public function __construct(Broadway\EventSourcing\EventSourcingRepository $repository)
    {
        $this->repository = $repository;
    }

    /**
     * A new invite aggregate root is created and added to the repository.
     */
    protected function handleInviteCommand(InviteCommand $command)
    {
        $invitation = Invitation::invite($command->invitationId, $command->name);

        $this->repository->save($invitation);
    }

    /**
     * An existing invite is loaded from the repository and the accept() method
     * is called.
     */
    protected function handleAcceptCommand(AcceptCommand $command)
    {
        $invitation = $this->repository->load($command->invitationId);

        $invitation->accept();

        $this->repository->save($invitation);
    }

    protected function handleDeclineCommand(DeclineCommand $command)
    {
        $invitation = $this->repository->load($command->invitationId);

        $invitation->decline();

        $this->repository->save($invitation);
    }
}
```

## File: `examples/event-sourced-domain-with-tests/InvitesTest.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

require_once __DIR__.'/Invites.php';

/**.
 *
 * An aggregate root scenario consists of three steps:
 *
 * - First, the scenario is setup with a history of events that already took place.
 * - Second, an action is taken on the aggregate.
 * - Third, the outcome is asserted. This can either be 1) some events are
 *   recorded, or 2) an exception is thrown.
 */
class InvitesTest extends Broadway\EventSourcing\Testing\AggregateRootScenarioTestCase
{
    private $generator;

    protected function setUp(): void
    {
        parent::setUp();
        $this->generator = new Broadway\UuidGenerator\Rfc4122\Version4Generator();
    }

    protected function getAggregateRootClass(): string
    {
        return Invitation::class;
    }

    /**
     * @test
     */
    public function it_can_invite_someone()
    {
        $id = $this->generator->generate();

        $this->scenario
            ->when(function () use ($id) {
                return Invitation::invite($id, 'asm89');
            })
            ->then([new InvitedEvent($id, 'asm89')]);
    }

    /**
     * @test
     */
    public function new_invites_can_be_accepted()
    {
        $id = $this->generator->generate();

        $this->scenario
            ->withAggregateId($id)
            ->given([new InvitedEvent($id, 'asm89')])
            ->when(function ($invite) {
                $invite->accept();
            })
            ->then([new AcceptedEvent($id)]);
    }

    /**
     * @test
     */
    public function accepting_an_accepted_invite_yields_no_change()
    {
        $id = $this->generator->generate();

        $this->scenario
            ->withAggregateId($id)
            ->given([new InvitedEvent($id, 'asm89'), new AcceptedEvent($id)])
            ->when(function ($aggregate) {
                $aggregate->accept();
            })
            ->then([]);
    }

    /**
     * @test
     */
    public function an_accepted_invite_cannot_be_declined()
    {
        $this->expectException(RuntimeException::class);
        $this->expectExceptionMessage('Already accepted');

        $id = $this->generator->generate();

        $this->scenario
            ->withAggregateId($id)
            ->given([new InvitedEvent($id, 'asm89'), new AcceptedEvent($id)])
            ->when(function ($invite) {
                $invite->decline();
            });
    }

    /**
     * @test
     */
    public function new_invites_can_be_declined()
    {
        $id = $this->generator->generate();

        $this->scenario
            ->withAggregateId($id)
            ->given([new InvitedEvent($id, 'asm89')])
            ->when(function ($invite) {
                $invite->decline();
            })
            ->then([new DeclinedEvent($id)]);
    }

    /**
     * @test
     */
    public function declining_a_declined_invite_yields_no_change()
    {
        $id = $this->generator->generate();

        $this->scenario
            ->withAggregateId($id)
            ->given([new InvitedEvent($id, 'asm89'), new DeclinedEvent($id)])
            ->when(function ($invite) {
                $invite->decline();
            })
            ->then([]);
    }

    /**
     * @test
     */
    public function a_declined_invite_cannot_be_accepted()
    {
        $this->expectException(RuntimeException::class);
        $this->expectExceptionMessage('Already declined');

        $id = $this->generator->generate();

        $this->scenario
            ->withAggregateId($id)
            ->given([new InvitedEvent($id, 'asm89'), new DeclinedEvent($id)])
            ->when(function ($invite) {
                $invite->accept();
            });
    }
}
```

## File: `examples/event-sourced-domain-with-tests/README.md`
```markdown
Event sourced domain with tests
===============================

A small example of an implementation of a small domain model. The example
consists of three files. The first file `Invites` contains the implementation of
the domain model. The second file `InvitesTest` contains a PHPUnit test suite
to only test the Invites model. The third file `InvitationCommandHandlerTest` contains
a PHPunit test suite to test the available commands.

The files contain comments about what is happening.

The PHPUnit tests can be run by changing to this directory and running:

```bash
$ phpunit .
PHPUnit 4.1.0 by Sebastian Bergmann.

..............

Time: 52 ms, Memory: 4.50Mb

OK (14 tests, 19 assertions)
```
```

## File: `examples/event-sourced-multiple-dyanmic-child-entities/JobSeekers.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

require_once __DIR__.'/../bootstrap.php';

/**
 * JobSeeker aggregate root.
 */
class JobSeeker extends Broadway\EventSourcing\EventSourcedAggregateRoot
{
    private $jobSeekerId;
    private $jobs = [];

    /**
     * Factory method to create a job seeker.
     */
    public static function startLookingForWork($jobSeekerId)
    {
        $jobSeeker = new self();

        // After instantiation of the object we apply the "JobSeekerStartedLookingForWorkEvent".
        $jobSeeker->apply(new JobSeekerStartedLookingForWorkEvent($jobSeekerId));

        return $jobSeeker;
    }

    /**
     * Every aggregate root will expose its id.
     */
    public function getAggregateRootId(): string
    {
        return $this->jobSeekerId;
    }

    public function heldJob($jobId, $title, $description)
    {
        if (array_key_exists($jobId, $this->jobs)) {
            throw new InvalidArgumentException("Job {$jobId} already assigned to this job seeker.");
        }
        $this->apply(new JobWasAddedToJobSeekerEvent($this->jobSeekerId, $jobId, $title, $description));
    }

    public function removeAccidentallyAddedJob($jobId)
    {
        $this->apply(new AccidentallyAddedJobWasRemovedFromJobSeekerEvent($this->jobSeekerId, $jobId));
    }

    public function describeJob($jobId, $title, $description)
    {
        if (!array_key_exists($jobId, $this->jobs)) {
            throw new InvalidArgumentException("Job {$jobId} is not assigned to this job seeker.");
        }
        $this->jobs[$jobId]->describe($title, $description);
    }

    public function applyJobSeekerStartedLookingForWorkEvent(JobSeekerStartedLookingForWorkEvent $event)
    {
        $this->jobSeekerId = $event->jobSeekerId;
    }

    public function applyJobWasAddedToJobSeekerEvent(JobWasAddedToJobSeekerEvent $event)
    {
        $this->jobs[$event->jobId] = new Job(
            $event->jobSeekerId,
            $event->jobId,
            $event->title,
            $event->description
        );
    }

    public function applyAccidentallyAddedJobWasRemovedFromJobSeekerEvent(
        AccidentallyAddedJobWasRemovedFromJobSeekerEvent $event
    ) {
        unset($this->jobs[$event->jobId]);
    }

    protected function getChildEntities(): array
    {
        return $this->jobs;
    }
}

class Job extends Broadway\EventSourcing\SimpleEventSourcedEntity
{
    private $jobSeekerId;
    private $jobId;
    private $title;
    private $description;

    public function __construct($jobSeekerId, $jobId, $title, $description)
    {
        $this->jobSeekerId = $jobSeekerId;
        $this->jobId = $jobId;
        $this->title = $title;
        $this->description = $description;
    }

    public function describe($title, $description)
    {
        if ($title === $this->title && $description === $this->description) {
            // If there is no change to the title and description we do not need to
            // generate an event.
            return;
        }

        $this->apply(new JobWasDescribedForJobSeekerEvent(
            $this->jobSeekerId,
            $this->jobId,
            $title,
            $description
        ));
    }

    public function applyJobWasDescribedForJobSeekerEvent(JobWasDescribedForJobSeekerEvent $event)
    {
        if ($event->jobId !== $this->jobId) {
            // Make sure that we only apply events that are intended for
            // *this* job instance and no others.
            return;
        }

        $this->title = $event->title;
        $this->description = $event->description;
    }
}

class JobSeekerStartLookingForWorkCommand
{
    public $jobSeekerId;

    public function __construct($jobSeekerId)
    {
        $this->jobSeekerId = $jobSeekerId;
    }
}

class JobSeekerStartedLookingForWorkEvent
{
    public $jobSeekerId;

    public function __construct($jobSeekerId)
    {
        $this->jobSeekerId = $jobSeekerId;
    }
}

class AddJobToJobSeekerCommand
{
    public $jobSeekerId;
    public $jobId;
    public $title;
    public $description;

    public function __construct($jobSeekerId, $jobId, $title, $description)
    {
        $this->jobSeekerId = $jobSeekerId;
        $this->jobId = $jobId;
        $this->title = $title;
        $this->description = $description;
    }
}

class JobWasAddedToJobSeekerEvent
{
    public $jobSeekerId;
    public $jobId;
    public $title;
    public $description;

    public function __construct($jobSeekerId, $jobId, $title, $description)
    {
        $this->jobSeekerId = $jobSeekerId;
        $this->jobId = $jobId;
        $this->title = $title;
        $this->description = $description;
    }
}

class DescribeJobForJobSeekerCommand
{
    public $jobSeekerId;
    public $jobId;
    public $title;
    public $description;

    public function __construct($jobSeekerId, $jobId, $title, $description)
    {
        $this->jobSeekerId = $jobSeekerId;
        $this->jobId = $jobId;
        $this->title = $title;
        $this->description = $description;
    }
}

class JobWasDescribedForJobSeekerEvent
{
    public $jobSeekerId;
    public $jobId;
    public $title;
    public $description;

    public function __construct($jobSeekerId, $jobId, $title, $description)
    {
        $this->jobSeekerId = $jobSeekerId;
        $this->jobId = $jobId;
        $this->title = $title;
        $this->description = $description;
    }
}

class RemoveAccidentallyAddedJobFromJobSeekerCommand
{
    public $jobSeekerId;
    public $jobId;

    public function __construct($jobSeekerId, $jobId)
    {
        $this->jobSeekerId = $jobSeekerId;
        $this->jobId = $jobId;
    }
}

class AccidentallyAddedJobWasRemovedFromJobSeekerEvent
{
    public $jobSeekerId;
    public $jobId;

    public function __construct($jobSeekerId, $jobId)
    {
        $this->jobSeekerId = $jobSeekerId;
        $this->jobId = $jobId;
    }
}

/**
 * A repository that will only store and retrieve JobSeeker aggregate roots.
 */
class JobSeekerRepository extends Broadway\EventSourcing\EventSourcingRepository
{
    public function __construct(Broadway\EventStore\EventStore $eventStore, Broadway\EventHandling\EventBus $eventBus)
    {
        parent::__construct($eventStore, $eventBus, 'JobSeeker', new Broadway\EventSourcing\AggregateFactory\PublicConstructorAggregateFactory());
    }
}

/*
 * A command handler will be registered with the command bus and handle the
 * commands that are dispatched.
 */
class JobSeekerCommandHandler extends Broadway\CommandHandling\SimpleCommandHandler
{
    private $repository;

    public function __construct(Broadway\EventSourcing\EventSourcingRepository $repository)
    {
        $this->repository = $repository;
    }

    /**
     * A new job seeker aggregate root is created and added to the repository.
     */
    protected function handleJobSeekerStartLookingForWorkCommand(JobSeekerStartLookingForWorkCommand $command)
    {
        $jobSeeker = JobSeeker::startLookingForWork($command->jobSeekerId);

        $this->repository->save($jobSeeker);
    }

    /**
     * An existing job seeker aggregate root is loaded and heldJob() is
     * called.
     */
    protected function handleAddJobToJobSeekerCommand(AddJobToJobSeekerCommand $command)
    {
        $jobSeeker = $this->repository->load($command->jobSeekerId);

        $jobSeeker->heldJob($command->jobId, $command->title, $command->description);

        $this->repository->save($jobSeeker);
    }

    /**
     * An existing job seeker aggregate root is loaded and describeJob() is
     * called.
     */
    protected function handleDescribeJobForJobSeekerCommand(DescribeJobForJobSeekerCommand $command)
    {
        $jobSeeker = $this->repository->load($command->jobSeekerId);

        $jobSeeker->describeJob($command->jobId, $command->title, $command->description);

        $this->repository->save($jobSeeker);
    }

    /**
     * An existing job seeker aggregate root is loaded and removeAccidentallyAddedJob()
     * is called.
     */
    protected function handleRemoveAccidentallyAddedJobFromJobSeekerCommand(RemoveAccidentallyAddedJobFromJobSeekerCommand $command)
    {
        $jobSeeker = $this->repository->load($command->jobSeekerId);

        $jobSeeker->removeAccidentallyAddedJob($command->jobId);

        $this->repository->save($jobSeeker);
    }
}
```

## File: `examples/event-sourced-multiple-dyanmic-child-entities/JobSeekersTest.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

use Broadway\CommandHandling\CommandHandler;

require_once __DIR__.'/JobSeekers.php';

/**
 * We drive the tests of our aggregate root through the command handler.
 *
 * A command handler scenario consists of three steps:
 *
 * - First, the scenario is setup with a history of events that already took place.
 * - Second, a command is dispatched (this is handled by the command handler)
 * - Third, the outcome is asserted. This can either be 1) some events are
 *   recorded, or 2) an exception is thrown.
 */
class JobSeekersCommandHandlerTest extends Broadway\CommandHandling\Testing\CommandHandlerScenarioTestCase
{
    private $generator;

    protected function setUp(): void
    {
        parent::setUp();
        $this->generator = new Broadway\UuidGenerator\Rfc4122\Version4Generator();
    }

    protected function createCommandHandler(Broadway\EventStore\EventStore $eventStore, Broadway\EventHandling\EventBus $eventBus): CommandHandler
    {
        $repository = new JobSeekerRepository($eventStore, $eventBus);

        return new JobSeekerCommandHandler($repository);
    }

    /**
     * @test
     */
    public function it_can_start_looking_for_work()
    {
        $id = $this->generator->generate();

        $this->scenario
            ->withAggregateId($id)
            ->given([])
            ->when(new JobSeekerStartLookingForWorkCommand($id))
            ->then([new JobSeekerStartedLookingForWorkEvent($id)]);
    }

    /**
     * @test
     */
    public function it_can_add_a_job()
    {
        $id = $this->generator->generate();

        $this->scenario
            ->withAggregateId($id)
            ->given([new JobSeekerStartedLookingForWorkEvent($id)])
            ->when(new AddJobToJobSeekerCommand($id, 'job-000', 'Title Zero', 'Description for zero.'))
            ->then([new JobWasAddedToJobSeekerEvent($id, 'job-000', 'Title Zero', 'Description for zero.')]);
    }

    /**
     * @test
     */
    public function it_can_describe_a_job()
    {
        $id = $this->generator->generate();

        $this->scenario
            ->withAggregateId($id)
            ->given([
                new JobSeekerStartedLookingForWorkEvent($id),
                new JobWasAddedToJobSeekerEvent($id, 'job-000', 'Title Zero', 'Description for zero.'),
            ])
            ->when(new DescribeJobForJobSeekerCommand($id, 'job-000', 'Title Double-Oh-Zero', 'Description for zero.'))
            ->then([new JobWasDescribedForJobSeekerEvent($id, 'job-000', 'Title Double-Oh-Zero', 'Description for zero.')]);
    }

    /**
     * @test
     */
    public function it_applies_the_describe_event_to_the_correct_job()
    {
        $id = $this->generator->generate();

        $this->scenario
            ->withAggregateId($id)
            ->given([
                new JobSeekerStartedLookingForWorkEvent($id),
                new JobWasAddedToJobSeekerEvent($id, 'job-000', 'Title Zero', 'Description for zero.'),
                new JobWasAddedToJobSeekerEvent($id, 'job-001', 'Title One', 'Description for one.'),
                new JobWasAddedToJobSeekerEvent($id, 'job-002', 'Title Two', 'Description for two.'),
            ])

            //
            // Trying to describe jobs with the same name and description should result in no new events since
            // our logic dictates that we ignore describe calls that do not change either the title or the
            // description.
            //

            ->when(new DescribeJobForJobSeekerCommand($id, 'job-000', 'Title Zero', 'Description for zero.'))
            ->then([])

            ->when(new DescribeJobForJobSeekerCommand($id, 'job-001', 'Title One', 'Description for one.'))
            ->then([])

            ->when(new DescribeJobForJobSeekerCommand($id, 'job-002', 'Title Two', 'Description for two.'))
            ->then([])

            //
            // Describing one of the jobs with a different title or description should trigger a job was described
            // event. We have already tested for that and we know it works. What we want to test for now is that the
            // event is only being applied to the instance we expect.
            //

            // Describe job-001 with a new title and description and we expect that the event will be triggered.

            ->when(new DescribeJobForJobSeekerCommand($id, 'job-001', 'Title Double-Oh-ONE!', 'Description for the one.'))
            ->then([new JobWasDescribedForJobSeekerEvent($id, 'job-001', 'Title Double-Oh-ONE!', 'Description for the one.')])

            // Next we describe our other two jobs with the previously specified title and description. If our
            // apply logic is correct, the title and description should still be the same and we should not get
            // a new event.

            ->when(new DescribeJobForJobSeekerCommand($id, 'job-000', 'Title Zero', 'Description for zero.'))
            ->then([])

            ->when(new DescribeJobForJobSeekerCommand($id, 'job-002', 'Title Two', 'Description for two.'))
            ->then([])

            // Lastly, we make one final check to see what happens when we describe job-001 again with the original
            // title and description from what it was first added. Since these values are different, we should see
            // one more describe event to set things back to normal.

            ->when(new DescribeJobForJobSeekerCommand($id, 'job-001', 'Title One', 'Description for one.'))
            ->then([new JobWasDescribedForJobSeekerEvent($id, 'job-001', 'Title One', 'Description for one.')])

        ;
    }

    /**
     * @test
     */
    public function it_can_remove_an_accidentally_added_job()
    {
        $id = $this->generator->generate();

        $this->scenario
            ->withAggregateId($id)
            ->given([
                new JobSeekerStartedLookingForWorkEvent($id),
                new JobWasAddedToJobSeekerEvent($id, 'job-000', 'Title Zero', 'Description for zero.'),
                new JobWasAddedToJobSeekerEvent($id, 'job-001', 'Title One OOPS!', 'Description for one ooops.'),
                new JobWasAddedToJobSeekerEvent($id, 'job-002', 'Title Two', 'Description for two.'),
            ])
            ->when(new RemoveAccidentallyAddedJobFromJobSeekerCommand($id, 'job-001'))
            ->then([new AccidentallyAddedJobWasRemovedFromJobSeekerEvent($id, 'job-001')])

            // To ensure that this command was successful, we try to add the job again. If the job can be added again
            // we know that the removal worked.
            ->when(new AddJobToJobSeekerCommand($id, 'job-001', 'Title Double-Oh-One!', 'Description for the one.'))
            ->then([new JobWasAddedToJobSeekerEvent($id, 'job-001', 'Title Double-Oh-One!', 'Description for the one.')])

        ;
    }

    /**
     * @test
     */
    public function it_cannot_add_the_same_job_if_job_is_already_assigned()
    {
        $this->expectException(InvalidArgumentException::class);
        $this->expectExceptionMessage('Job job-000 already assigned to this job seeker');

        $id = $this->generator->generate();

        $this->scenario
            ->withAggregateId($id)
            ->given([
                new JobSeekerStartedLookingForWorkEvent($id),
                new JobWasAddedToJobSeekerEvent($id, 'job-000', 'Title Zero', 'Description for zero.'),
            ])
            ->when(new AddJobToJobSeekerCommand($id, 'job-000', 'Title Double-Oh-Zero!', 'Description for the zero.'))
            ->then([]);
    }

    /**
     * @test
     */
    public function it_cannot_describe_a_job_it_knows_nothing_about()
    {
        $this->expectException(InvalidArgumentException::class);
        $this->expectExceptionMessage('Job job-000 is not assigned to this job seeker');

        $id = $this->generator->generate();

        $this->scenario
            ->withAggregateId($id)
            ->given([new JobSeekerStartedLookingForWorkEvent($id)])
            ->when(new DescribeJobForJobSeekerCommand($id, 'job-000', 'Title Double-Oh-Zero', 'Description for zero.'))
            ->then([]);
    }
}
```

## File: `examples/event-sourced-multiple-dyanmic-child-entities/README.md`
```markdown
Event sourced multiple dynamic child entities with tests
========================================================

A small example of an implementation of a small domain model that includes an
aggregate root that maintains a collection of child entities. The example
consists of two files. The first file `JobSeekers` contains the implementation
of the domain model. The second file `JobSeekersTest` contains a PHPUnit test
suite to test the domain.

The two files contain comments about what is happening.


The Story
---------

The purpose of this example is to show how dynamically created Child Entities of
an Aggregate Root can be managed. Compare this to a Child Entity whose entire
lifecycle is completely tied to its parent Aggregate Root where it is created
when the Aggregate Root itself is created.

In this contrived domain, a Job Seeker may have held zero or more Jobs. Jobs
can have a title and a description and can be removed from the Job Seeker if
they are added accidentally. Jobs may also be described after they have been
held in case typos are made.

The example shows how to manage the creation of new Child Entities (Jobs), how
to modify Child Entities with events, how to ensure that the correct Child
Entities are updated when Events are applied, and how to remove Child Entities
if needed.

The tests show how the domain can be exercised using commands. It also shows
how to test to ensure that Child Entities are being created, managed, and
moved correctly.


Running Tests
-------------

The PHPUnit tests can be run by changing to this directory and running:

```bash
$ phpunit .
PHPUnit 4.1.0 by Sebastian Bergmann.

.......

Time: 70 ms, Memory: 4.00Mb

OK (7 tests, 9 assertions)
```
```

## File: `examples/querying-the-event-store/query-dbal-events.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

use Broadway\Domain\DateTime;
use Broadway\Domain\DomainMessage;
use Broadway\EventStore\Dbal\DBALEventStore;
use Broadway\Serializer\SimpleInterfaceSerializer;
use Doctrine\DBAL\DriverManager;

require __DIR__.'/query-memory-events-with-criteria.php';

if (!class_exists(DBALEventStore::class)) {
    $logger->error('The query-dbal-events example is only runnable when you have DBALEventStore available');

    return 1;
}

$serializer = new SimpleInterfaceSerializer();

$connection = DriverManager::getConnection(['driver' => 'pdo_sqlite', 'memory' => true]);
$schemaManager = $connection->getSchemaManager();

$schema = $schemaManager->createSchema();

$store = new DBALEventStore($connection, $serializer, $serializer, 'events', false);
$schemaManager->createTable($store->configureTable($schema));

$store->append($staleInvited->getAggregateRootId(), $staleInvitationEvents);
$store->append($acceptedInvite->getAggregateRootId(), $acceptedInviteEvents);
$store->append($declinedInvite->getAggregateRootId(), $declinedInviteEvents);

// That other example was with the InMemoryStore, but you can use the same idea
// with more complex SQL queries that are not supported with the Criteria object

$sql = "SELECT a.*
    FROM events a
    LEFT JOIN events b ON a.uuid = b.uuid
    AND b.type IN ('AcceptedEvent', 'DeclinedEvent')
    WHERE a.`type` = 'InvitedEvent' AND b.uuid IS NULL;";

$stmt = $connection->executeQuery($sql);
$stmt->execute();

$staleInvites = [];
while ($row = $stmt->fetch()) {
    // Rebuilding of the DomainMessage
    // the specifics depend on the event-store implementation
    // this example is based on the broadway/event-store-dbal implementation
    $domainMessage = new DomainMessage(
        $row['uuid'],
        (int) $row['playhead'],
        $serializer->deserialize(json_decode($row['metadata'], true)),
        $serializer->deserialize(json_decode($row['payload'], true)),
        DateTime::fromString($row['recorded_on'])
    );
    $staleInvites[$row['uuid']] = $domainMessage;
}

foreach ($staleInvites as $inviteMessage) {
    $logger->info('Stale invite (from sql via domainmessage): '.$inviteMessage->getId());
}
```

## File: `examples/querying-the-event-store/query-memory-events-with-criteria.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

use Broadway\Domain\DomainEventStream;
use Broadway\EventStore\CallableEventVisitor;
use Broadway\EventStore\InMemoryEventStore;
use Broadway\EventStore\Management\Criteria;

require __DIR__.'/../event-sourced-domain-with-tests/Invites.php';

$logger = new StdoutLogger();
$store = new InMemoryEventStore();

// Prepare some invites
$staleInvited = Invitation::invite('061e5360-ff48-4468-a672-e49ed77e0fc2', 'Barry');
$acceptedInvite = Invitation::invite('590ae831-b854-40e6-bcc2-ca7d9d552421', 'Mary');
$acceptedInvite->accept();
$declinedInvite = Invitation::invite('caae5d47-5ee7-4821-9f21-a2b65b373438', 'Larry');
$declinedInvite->decline();

// Store the events
$staleInvitationEvents = $staleInvited->getUncommittedEvents();
$acceptedInviteEvents = $acceptedInvite->getUncommittedEvents();
$declinedInviteEvents = $declinedInvite->getUncommittedEvents();
$store->append($staleInvited->getAggregateRootId(), $staleInvitationEvents);
$store->append($acceptedInvite->getAggregateRootId(), $acceptedInviteEvents);
$store->append($declinedInvite->getAggregateRootId(), $declinedInviteEvents);

$allMessages = new DomainEventStream(array_merge(
    $staleInvitationEvents->getIterator()->getArrayCopy(),
    $acceptedInviteEvents->getIterator()->getArrayCopy(),
    $declinedInviteEvents->getIterator()->getArrayCopy()
));

// Create the criteria to retrieve AcceptedEvent events
$acceptedInvitesCriteria = Criteria::create()->withEventTypes([strtr(AcceptedEvent::class, '\\', '.')]);

// Query the event store with the criteria and fill an array with ids of accepted invites
$acceptedEventsReadModel = [];
$store->visitEvents($acceptedInvitesCriteria, new CallableEventVisitor(function ($domainMessage) use (&$acceptedEventsReadModel) {
    $acceptedEventsReadModel[] = ['inviteId' => $domainMessage->getPayload()->invitationId];
}));

$logger->info('Accepted invites', $acceptedEventsReadModel);

// For more complex cases you would need more complex queries.
// The Criteria will only deal with simple use cases.
// If you need more complex queries you could do something like this

$staleInvites = [];
foreach ($allMessages as $domainMessage) {
    switch ($domainMessage->getType()) {
        case 'InvitedEvent':
            $staleInvites[(string) $domainMessage->getId()] = $domainMessage;
            break;
        case 'AcceptedEvent':
        case 'DeclinedEvent':
            unset($staleInvites[(string) $domainMessage->getId()]);
            break;
    }
}

$logger->info('Stale invites', array_keys($staleInvites));

foreach (array_keys($staleInvites) as $inviteId) {
    $invite = $store->load($inviteId);
    // Example: if we would want to expire invites that haven't been accepted or declined yet
    // $invite->expire();
}
```

## File: `examples/replaying-projectors/README.md`
```markdown
Replaying an aggregate
======================

This example demonstrates how Broadway can be used in order to replay a single
aggregate. You have to be cautious when using a replayer, and consider all the
possible consequences of your action. For example, you might not want to resend
all the emails to your customers. In general, replaying EventListeners that
have side effects is discouraged!

You can specify which events need to be loaded from the EventStore using the
\Broadway\EventStore\Management\Criteria object. It allows you to specify all
events corresponding to a specific aggregate root type, all events corresponding
to a single aggregate id (as this example shows), or only events of a specific
type.

The example shows how to use \Broadway\EventStore\Management\EventStoreManagent
to load events and how to pass the events to a
\Broadway\EventStore\EventVisitor. This visitor can be anything you want. In
this example the EventVisitor passes the events to a specific EventListener.
```

## File: `examples/replaying-projectors/example.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

require_once __DIR__.'/../bootstrap.php';

use Broadway\Domain\DomainEventStream;
use Broadway\Domain\DomainMessage;
use Broadway\Domain\Metadata;
use Broadway\EventHandling\EventListener;
use Broadway\EventStore\EventVisitor;
use Broadway\EventStore\InMemoryEventStore;
use Broadway\EventStore\Management\Criteria;
use Broadway\EventStore\Management\EventStoreManagement;

$eventStore = new InMemoryEventStore();

$aggregateId = 'aggregate_to_replay';

class SimpleEvent
{
}

// First, we fill up the event store with the events of two aggregates
$domainEventStream = new DomainEventStream([
    DomainMessage::recordNow($aggregateId, 0, new Metadata(), new SimpleEvent()),
    DomainMessage::recordNow($aggregateId, 1, new Metadata(), new SimpleEvent()),
]);

$eventStore->append($aggregateId, $domainEventStream);

$secondAggregateId = 'do_not_replay_this_one';

$domainEventStream = new DomainEventStream([
    DomainMessage::recordNow($secondAggregateId, 0, new Metadata(), new SimpleEvent()),
]);

$eventStore->append($secondAggregateId, $domainEventStream);

// Now, we define a Replayer class. This example allows the replaying of a
// single aggregate, and passes the events to a EventListener.
class Replayer implements EventVisitor
{
    public function __construct(EventStoreManagement $eventStore, EventListener $eventListener)
    {
        $this->eventStore = $eventStore;
        $this->eventListener = $eventListener;
    }

    public function doWithEvent(DomainMessage $domainMessage): void
    {
        $this->eventListener->handle($domainMessage);
    }

    public function replayForAggregate(string $aggregateId): void
    {
        $criteria = new Criteria();
        $criteria = $criteria->withAggregateRootIds([$aggregateId]);

        $this->eventStore->visitEvents($criteria, $this);
    }
}

class ExampleEventListener implements EventListener
{
    public function handle(DomainMessage $domainMessage): void
    {
        var_dump($domainMessage->getPayload());
    }
}

$replayer = new Replayer($eventStore, new ExampleEventListener());
$replayer->replayForAggregate($aggregateId);
```

## File: `examples/serializer/SerializableEventTest.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

use Broadway\Serializer\Serializable;
use Broadway\Serializer\Testing\SerializableEventTestCase;

class SerializableEventTest extends SerializableEventTestCase
{
    protected function createEvent()
    {
        return new SerializableInviteEvent('invitationId', 'name');
    }
}

class SerializableInviteEvent implements Serializable
{
    private $invitationId;
    private $name;

    public function __construct(string $invitationId, string $name)
    {
        $this->invitationId = $invitationId;
        $this->name = $name;
    }

    public static function deserialize(array $data)
    {
        return new self($data['invitationId'], $data['name']);
    }

    public function serialize(): array
    {
        return [
            'invitationId' => $this->invitationId,
            'name' => $this->name,
        ];
    }
}
```

## File: `examples/serializer/serializer.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

require_once __DIR__.'/../bootstrap.php';

class SerializeMe implements Broadway\Serializer\Serializable
{
    private $message;

    public function __construct($message)
    {
        $this->message = $message;
    }

    public static function deserialize(array $data)
    {
        return new self($data['message']);
    }

    public function serialize()
    {
        return [
            'message' => $this->message,
        ];
    }
}

// Setup the simple serializer
$serializer = new Broadway\Serializer\SimpleInterfaceSerializer();

// Create something to serialize
$serializeMe = new SerializeMe("Hi, i'm serialized?");

// Serialize
$serialized = $serializer->serialize($serializeMe);
var_dump($serialized);

// Deserialize
$deserialized = $serializer->deserialize($serialized);
var_dump($deserialized);
```

## File: `examples/upcasting/UpcastingExampleTest.php`
```php
<?php

declare(strict_types=1);

use Broadway\Domain\DomainEventStream;
use Broadway\Domain\DomainMessage;
use Broadway\Domain\Metadata;
use Broadway\EventHandling\SimpleEventBus;
use Broadway\EventStore\InMemoryEventStore;
use Broadway\Upcasting\SequentialUpcasterChain;
use Broadway\Upcasting\UpcastingEventStore;
use Ramsey\Uuid\Uuid;

require_once __DIR__.'/Users.php';
require_once __DIR__.'/UserCreated.php';
require_once __DIR__.'/UserCreatedV2.php';
require_once __DIR__.'/User.php';
require_once __DIR__.'/UserCreatedUpcasterV1toV2.php';
require_once __DIR__.'/UserCreatedUpcasterV2toV3.php';

class UpcastingExampleTest extends PHPUnit\Framework\TestCase
{
    /**
     * @var SimpleEventBus
     */
    private $eventBus;

    protected function setUp(): void
    {
        $this->eventBus = new SimpleEventBus();
    }

    public function it_should_do_nothing_if_there_are_no_new_versions(): void
    {
        $userId = Uuid::uuid4()->toString();

        $eventStore = new UpcastingEventStore(
            new InMemoryEventStore(),
            new SequentialUpcasterChain([
                new UserCreatedUpcasterV1toV2(),
                new UserCreatedUpcasterV2toV3(),
            ])
        );

        $events[] = DomainMessage::recordNow(
            $userId,
            0,
            new Metadata([]),
            new UserCreatedV3($userId, 'matiux', 'xuitam', 36, 'Italy')
        );

        $eventStore->append($userId, new DomainEventStream($events));

        $users = new Users($eventStore, $this->eventBus);

        $matiux = $users->load($userId);

        self::assertInstanceOf(User::class, $matiux);
        self::assertEquals('matiux xuitam of age: 36', $matiux->name());
        self::assertEquals('Italy', $matiux->country());
    }

    /**
     * @test
     *
     * @testdox It should upcast UserCreatedV1 to UserCreateV3 when only v1 stored
     */
    public function it_should_upcast_user_created_v1_to_user_created_v3_when_only_v1_stored(): void
    {
        $userId = Uuid::uuid4()->toString();

        $eventStore = new UpcastingEventStore(
            new InMemoryEventStore(),
            new SequentialUpcasterChain([
                new UserCreatedUpcasterV1toV2(),
                new UserCreatedUpcasterV2toV3(),
            ])
        );

        $events[] = DomainMessage::recordNow(
            $userId,
            0,
            new Metadata([]),
            new UserCreated($userId, 'matiux')
        );

        $eventStore->append($userId, new DomainEventStream($events));

        $users = new Users($eventStore, $this->eventBus);

        $matiux = $users->load($userId);

        self::assertInstanceOf(User::class, $matiux);
        self::assertEquals('matiux N/A of age: -1', $matiux->name());
        self::assertEquals('N/A', $matiux->country());
    }

    /**
     * @test
     *
     * @testdox It should upcast UserCreatedV1 to UserCreateV3 when v1 and v2 are stored
     */
    public function it_should_upcast_user_created_v1_to_user_created_v3_when_v1_and_v2_are_stored(): void
    {
        $userId = Uuid::uuid4()->toString();

        $eventStore = new UpcastingEventStore(
            new InMemoryEventStore(),
            new SequentialUpcasterChain([
                new UserCreatedUpcasterV1toV2(),
                new UserCreatedUpcasterV2toV3(),
            ])
        );

        $events[] = DomainMessage::recordNow(
            $userId,
            0,
            new Metadata([]),
            new UserCreated($userId, 'matiux')
        );

        $events[] = DomainMessage::recordNow(
            $userId,
            1,
            new Metadata([]),
            new UserCreatedV2($userId, 'matiux', 'xuitam', 'Italy')
        );

        $eventStore->append($userId, new DomainEventStream($events));

        $users = new Users($eventStore, $this->eventBus);

        $matiux = $users->load($userId);

        self::assertInstanceOf(User::class, $matiux);
        self::assertEquals('matiux xuitam of age: -1', $matiux->name());
        self::assertEquals('Italy', $matiux->country());
    }
}
```

## File: `examples/upcasting/User.php`
```php
<?php

declare(strict_types=1);

use Broadway\EventSourcing\EventSourcedAggregateRoot;

class User extends EventSourcedAggregateRoot
{
    private $userId;
    private $name;
    private $surname;
    private $age;
    private $country;

    public static function create(string $userId, string $name, string $surname, int $age, string $country): self
    {
        $user = new self();
        $user->apply(new UserCreatedV3($userId, $name, $surname, $age, $country));

        return $user;
    }

    protected function applyUserCreatedV3(UserCreatedV3 $event): void
    {
        $this->userId = $event->userId;
        $this->name = $event->name;
        $this->surname = $event->surname;
        $this->age = $event->age;
        $this->country = $event->country;
    }

    public function getAggregateRootId(): string
    {
        return $this->userId;
    }

    public function name(): string
    {
        return sprintf('%s %s of age: %d', $this->name, $this->surname, $this->age);
    }

    public function age(): int
    {
        return $this->age;
    }

    public function country(): string
    {
        return $this->country;
    }
}
```

## File: `examples/upcasting/UserCreated.php`
```php
<?php

declare(strict_types=1);

class UserCreated implements Broadway\Serializer\Serializable
{
    public $userId;
    public $name;

    public function __construct(string $userId, string $name)
    {
        $this->userId = $userId;
        $this->name = $name;
    }

    public static function deserialize(array $data)
    {
        return new self(
            $data['userId'],
            $data['name']
        );
    }

    public function serialize(): array
    {
        return [
            'userId' => $this->userId,
            'name' => $this->name,
        ];
    }
}
```

## File: `examples/upcasting/UserCreatedUpcasterV1toV2.php`
```php
<?php

declare(strict_types=1);

use Broadway\Domain\DomainMessage;
use Broadway\Upcasting\Upcaster;

require_once __DIR__.'/UserCreated.php';
require_once __DIR__.'/UserCreatedV2.php';

/**
 * @implements Upcaster<UserCreated, UserCreatedV2>
 */
class UserCreatedUpcasterV1toV2 implements Upcaster
{
    public function supports(DomainMessage $domainMessage): bool
    {
        return $domainMessage->getPayload() instanceof UserCreated;
    }

    public function upcast(DomainMessage $domainMessage): DomainMessage
    {
        $payload = $domainMessage->getPayload();

        $upcastedEvent = new UserCreatedV2(
            $payload->userId,
            $payload->name,
            'N/A',
            'N/A'
        );

        return new DomainMessage(
            $domainMessage->getId(),
            $domainMessage->getPlayhead(),
            $domainMessage->getMetadata(),
            $upcastedEvent,
            $domainMessage->getRecordedOn()
        );
    }
}
```

## File: `examples/upcasting/UserCreatedUpcasterV2toV3.php`
```php
<?php

declare(strict_types=1);

use Broadway\Domain\DomainMessage;
use Broadway\Upcasting\Upcaster;

require_once __DIR__.'/UserCreatedV2.php';
require_once __DIR__.'/UserCreatedV3.php';

/**
 * @implements Upcaster<UserCreatedV2, UserCreatedV3>
 */
class UserCreatedUpcasterV2toV3 implements Upcaster
{
    public function supports(DomainMessage $domainMessage): bool
    {
        return $domainMessage->getPayload() instanceof UserCreatedV2;
    }

    public function upcast(DomainMessage $domainMessage): DomainMessage
    {
        $payload = $domainMessage->getPayload();

        $upcastedEvent = new UserCreatedV3(
            $payload->userId,
            $payload->name,
            $payload->surname,
            -1,
            $payload->country
        );

        return new DomainMessage(
            $domainMessage->getId(),
            $domainMessage->getPlayhead(),
            $domainMessage->getMetadata(),
            $upcastedEvent,
            $domainMessage->getRecordedOn()
        );
    }
}
```

## File: `examples/upcasting/UserCreatedV2.php`
```php
<?php

declare(strict_types=1);

class UserCreatedV2 implements Broadway\Serializer\Serializable
{
    public $userId;
    public $name;
    public $surname;
    public $country;

    public function __construct(string $userId, string $name, string $surname, string $country)
    {
        $this->userId = $userId;
        $this->name = $name;
        $this->surname = $surname;
        $this->country = $country;
    }

    public static function deserialize(array $data)
    {
        return new self(
            $data['userId'],
            $data['name'],
            $data['surname'],
            $data['country']
        );
    }

    public function serialize(): array
    {
        return [
            'userId' => $this->userId,
            'name' => $this->name,
            'surname' => $this->surname,
            'country' => $this->country,
        ];
    }
}
```

## File: `examples/upcasting/UserCreatedV3.php`
```php
<?php

declare(strict_types=1);

class UserCreatedV3 implements Broadway\Serializer\Serializable
{
    public $userId;
    public $name;
    public $surname;
    public $age;
    public $country;

    public function __construct(string $userId, string $name, string $surname, int $age, string $country)
    {
        $this->userId = $userId;
        $this->name = $name;
        $this->surname = $surname;
        $this->age = $age;
        $this->country = $country;
    }

    public static function deserialize(array $data)
    {
        return new self(
            $data['userId'],
            $data['name'],
            $data['surname'],
            $data['age'],
            $data['country']
        );
    }

    public function serialize(): array
    {
        return [
            'userId' => $this->userId,
            'name' => $this->name,
            'surname' => $this->surname,
            'age' => $this->age,
            'country' => $this->country,
        ];
    }
}
```

## File: `examples/upcasting/Users.php`
```php
<?php

declare(strict_types=1);

use Broadway\EventHandling\EventBus;
use Broadway\EventSourcing\EventSourcingRepository;
use Broadway\EventStore\EventStore;

require_once __DIR__.'/User.php';

class Users extends EventSourcingRepository
{
    public function __construct(EventStore $eventStore, EventBus $eventBus)
    {
        parent::__construct(
            $eventStore,
            $eventBus,
            User::class,
            new Broadway\EventSourcing\AggregateFactory\PublicConstructorAggregateFactory()
        );
    }
}
```

## File: `src/Broadway/Auditing/CommandLogger.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

namespace Broadway\Auditing;

use Exception;
use Psr\Log\LoggerInterface;

/**
 * Logs whether commands where executed successfully or whether they failed.
 *
 * This object can be registered as an event listener.
 */
final class CommandLogger
{
    private $logger;
    private $commandSerializer;

    public function __construct(LoggerInterface $logger, CommandSerializer $commandSerializer)
    {
        $this->logger = $logger;
        $this->commandSerializer = $commandSerializer;
    }

    /**
     * @param mixed $command Command that was executed successfully
     */
    public function onCommandHandlingSuccess($command): void
    {
        $messageData = [
            'status' => 'success',
            'command' => $this->getCommandData($command),
        ];

        $this->logger->info(json_encode($messageData));
    }

    /**
     * @param mixed      $command   Command that errored
     * @param \Exception $exception Exception that occured during the execution of the command
     */
    public function onCommandHandlingFailure($command, \Exception $exception): void
    {
        $messageData = [
            'status' => 'failure',
            'command' => $this->getCommandData($command),
            'exception' => [
                'message' => $exception->getMessage(),
                'file' => $exception->getFile(),
                'class' => get_class($exception),
                'line' => $exception->getLine(),
                'code' => $exception->getCode(),
            ],
        ];

        $this->logger->info(json_encode($messageData));
    }

    private function getCommandData($command): array
    {
        return [
            'class' => get_class($command),
            'data' => $this->commandSerializer->serialize($command),
        ];
    }
}
```

## File: `src/Broadway/Auditing/CommandSerializer.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

namespace Broadway\Auditing;

/**
 * Serializes commands to an array of scalars.
 */
interface CommandSerializer
{
    /**
     * Serializes the command.
     */
    public function serialize($command): array;
}
```

## File: `src/Broadway/Auditing/NullByteCommandSerializer.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

namespace Broadway\Auditing;

/**
 * Command serializer that uses php hacks to get the data from a command.
 *
 * There are many other ways to implement serialization on commands, but since
 * this is only for logging purposes we get away with this solution for now.
 */
final class NullByteCommandSerializer implements CommandSerializer
{
    public function serialize($command): array
    {
        $serializedCommand = [];
        foreach ((array) $command as $key => $value) {
            $serializedCommand[str_replace("\0", '-', $key)] = $value;
        }

        return $serializedCommand;
    }
}
```

## File: `src/Broadway/CommandHandling/ClosureCommandHandler.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

namespace Broadway\CommandHandling;

use Broadway\CommandHandling\Exception\ClosureParameterNotAnObjectException;
use Broadway\CommandHandling\Exception\CommandNotAnObjectException;

/**
 * Using this class command handlers can be registered with closures.
 */
class ClosureCommandHandler implements CommandHandler
{
    /**
     * @var \Closure[]
     */
    private $handlers = [];

    public function add(\Closure $handler): void
    {
        $reflection = new \ReflectionFunction($handler);
        if (0 === $reflection->getNumberOfParameters()) {
            throw new ClosureParameterNotAnObjectException();
        }

        $reflectionType = $reflection->getParameters()[0]->getType();
        if ($reflectionType instanceof \ReflectionNamedType && !$reflectionType->isBuiltin()) {
            $this->handlers[$reflectionType->getName()] = $handler;
        } else {
            throw new ClosureParameterNotAnObjectException();
        }
    }

    public function handle($command): void
    {
        if (!is_object($command)) {
            throw new CommandNotAnObjectException();
        }

        $index = get_class($command);

        if (!isset($this->handlers[$index])) {
            return;
        }

        $this->handlers[$index]($command);
    }
}
```

## File: `src/Broadway/CommandHandling/CommandBus.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

namespace Broadway\CommandHandling;

/**
 * Dispatches command objects to the subscribed command handlers.
 */
interface CommandBus
{
    /**
     * Dispatches the command $command to the proper CommandHandler.
     */
    public function dispatch($command): void;

    /**
     * Subscribes the command handler to this CommandBus.
     */
    public function subscribe(CommandHandler $handler): void;
}
```

## File: `src/Broadway/CommandHandling/CommandHandler.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

namespace Broadway\CommandHandling;

/**
 * Handles dispatched commands.
 */
interface CommandHandler
{
    public function handle($command): void;
}
```

## File: `src/Broadway/CommandHandling/EventDispatchingCommandBus.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

namespace Broadway\CommandHandling;

use Broadway\EventDispatcher\EventDispatcher;

/**
 * Command bus decorator that dispatches events.
 *
 * Dispatches events signalling whether a command was executed successfully or
 * if it failed.
 */
final class EventDispatchingCommandBus implements CommandBus
{
    public const EVENT_COMMAND_SUCCESS = 'broadway.command_handling.command_success';
    public const EVENT_COMMAND_FAILURE = 'broadway.command_handling.command_failure';

    private $commandBus;
    private $dispatcher;

    public function __construct(CommandBus $commandBus, EventDispatcher $dispatcher)
    {
        $this->commandBus = $commandBus;
        $this->dispatcher = $dispatcher;
    }

    public function dispatch($command): void
    {
        try {
            $this->commandBus->dispatch($command);
            $this->dispatcher->dispatch(self::EVENT_COMMAND_SUCCESS, ['command' => $command]);
        } catch (\Exception $e) {
            $this->dispatcher->dispatch(
                self::EVENT_COMMAND_FAILURE,
                ['command' => $command, 'exception' => $e]
            );

            throw $e;
        }
    }

    public function subscribe(CommandHandler $handler): void
    {
        $this->commandBus->subscribe($handler);
    }
}
```

## File: `src/Broadway/CommandHandling/SimpleCommandBus.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

namespace Broadway\CommandHandling;

/**
 * Simple synchronous dispatching of commands.
 */
final class SimpleCommandBus implements CommandBus
{
    private $commandHandlers = [];
    private $queue = [];
    private $isDispatching = false;

    public function subscribe(CommandHandler $handler): void
    {
        $this->commandHandlers[] = $handler;
    }

    public function dispatch($command): void
    {
        $this->queue[] = $command;

        if (!$this->isDispatching) {
            $this->isDispatching = true;

            try {
                while ($command = array_shift($this->queue)) {
                    foreach ($this->commandHandlers as $handler) {
                        $handler->handle($command);
                    }
                }
            } finally {
                $this->isDispatching = false;
            }
        }
    }
}
```

## File: `src/Broadway/CommandHandling/SimpleCommandHandler.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

namespace Broadway\CommandHandling;

use Broadway\CommandHandling\Exception\CommandNotAnObjectException;

/**
 * Convenience base class for command handlers.
 *
 * Command handlers using this base class will implement `handle<CommandName>`
 * methods for each command they can handle.
 *
 * Note: the convention used does not take namespaces into account.
 */
abstract class SimpleCommandHandler implements CommandHandler
{
    public function handle($command): void
    {
        $method = $this->getHandleMethod($command);

        if (!method_exists($this, $method)) {
            return;
        }

        $this->$method($command);
    }

    private function getHandleMethod($command): string
    {
        if (!is_object($command)) {
            throw new CommandNotAnObjectException();
        }

        $classParts = explode('\\', get_class($command));

        return 'handle'.end($classParts);
    }
}
```

## File: `src/Broadway/CommandHandling/Exception/ClosureParameterNotAnObjectException.php`
```php
<?php

declare(strict_types=1);

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

namespace Broadway\CommandHandling\Exception;

/**
 * Closure parameter should be object.
 */
class ClosureParameterNotAnObjectException extends \InvalidArgumentException
{
}
```

## File: `src/Broadway/CommandHandling/Exception/CommandNotAnObjectException.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

namespace Broadway\CommandHandling\Exception;

/**
 * Commands should be objects.
 */
final class CommandNotAnObjectException extends \InvalidArgumentException
{
}
```

## File: `src/Broadway/CommandHandling/Testing/CommandHandlerScenarioTestCase.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

namespace Broadway\CommandHandling\Testing;

use Broadway\CommandHandling\CommandHandler;
use Broadway\EventHandling\EventBus;
use Broadway\EventHandling\SimpleEventBus;
use Broadway\EventStore\EventStore;
use Broadway\EventStore\InMemoryEventStore;
use Broadway\EventStore\TraceableEventStore;
use PHPUnit\Framework\TestCase;

/**
 * Base test case that can be used to set up a command handler scenario.
 */
abstract class CommandHandlerScenarioTestCase extends TestCase
{
    /**
     * @var Scenario
     */
    protected $scenario;

    protected function setUp(): void
    {
        $this->scenario = $this->createScenario();
    }

    protected function createScenario(): Scenario
    {
        $eventStore = new TraceableEventStore(new InMemoryEventStore());
        $eventBus = new SimpleEventBus();
        $commandHandler = $this->createCommandHandler($eventStore, $eventBus);

        return new Scenario($this, $eventStore, $commandHandler);
    }

    /**
     * Create a command handler for the given scenario test case.
     */
    abstract protected function createCommandHandler(EventStore $eventStore, EventBus $eventBus): CommandHandler;
}
```

## File: `src/Broadway/CommandHandling/Testing/Scenario.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

namespace Broadway\CommandHandling\Testing;

use Broadway\CommandHandling\CommandHandler;
use Broadway\Domain\DomainEventStream;
use Broadway\Domain\DomainMessage;
use Broadway\Domain\Metadata;
use Broadway\EventStore\TraceableEventStore;
use PHPUnit\Framework\TestCase;

/**
 * Helper testing scenario to test command handlers.
 *
 * The scenario will help with testing command handlers. A scenario consists of
 * three steps:
 *
 * 1) given(): Load a history of events in the event store
 * 2) when():  Dispatch a command
 * 3) then():  events that should have been persisted
 */
class Scenario
{
    private $eventStore;
    private $commandHandler;
    private $testCase;
    private $aggregateId;

    public function __construct(
        TestCase $testCase,
        TraceableEventStore $eventStore,
        CommandHandler $commandHandler
    ) {
        $this->testCase = $testCase;
        $this->eventStore = $eventStore;
        $this->commandHandler = $commandHandler;
        $this->aggregateId = '1';
    }

    public function withAggregateId(string $aggregateId): self
    {
        $this->aggregateId = $aggregateId;

        return $this;
    }

    /**
     * @param mixed[] $events
     */
    public function given(?array $events): self
    {
        if (null === $events) {
            return $this;
        }

        $messages = [];
        $playhead = -1;
        foreach ($events as $event) {
            ++$playhead;
            $messages[] = DomainMessage::recordNow($this->aggregateId, $playhead, new Metadata([]), $event);
        }

        $this->eventStore->append($this->aggregateId, new DomainEventStream($messages));

        return $this;
    }

    public function when($command): self
    {
        $this->eventStore->trace();

        $this->commandHandler->handle($command);

        return $this;
    }

    /**
     * @param mixed[] $events
     */
    public function then(array $events): self
    {
        $this->testCase->assertEquals($events, $this->eventStore->getEvents());

        $this->eventStore->clearEvents();

        return $this;
    }
}
```

## File: `src/Broadway/CommandHandling/Testing/TraceableCommandBus.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

namespace Broadway\CommandHandling\Testing;

use Broadway\CommandHandling\CommandBus;
use Broadway\CommandHandling\CommandHandler;

/**
 * Command bus that is able to record all dispatched commands.
 */
final class TraceableCommandBus implements CommandBus
{
    private $commandHandlers = [];
    private $commands = [];
    private $record = false;

    public function subscribe(CommandHandler $handler): void
    {
        $this->commandHandlers[] = $handler;
    }

    public function dispatch($command): void
    {
        if (!$this->record) {
            return;
        }

        $this->commands[] = $command;
    }

    /**
     * @return mixed[]
     */
    public function getRecordedCommands(): array
    {
        return $this->commands;
    }

    public function record(): bool
    {
        return $this->record = true;
    }
}
```

## File: `src/Broadway/Domain/AggregateRoot.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

namespace Broadway\Domain;

/**
 * Represents entities that are an aggregate root.
 */
interface AggregateRoot
{
    public function getUncommittedEvents(): DomainEventStream;

    public function getAggregateRootId(): string;
}
```

## File: `src/Broadway/Domain/DateTime.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

namespace Broadway\Domain;

/**
 * Immutable DateTime implementation with some helper methods.
 */
final class DateTime
{
    public const FORMAT_STRING = 'Y-m-d\TH:i:s.uP';

    private $dateTime;

    private function __construct(\DateTimeImmutable $dateTime)
    {
        $this->dateTime = $dateTime;
    }

    public static function now(): self
    {
        return new self(
            \DateTimeImmutable::createFromFormat(
                'U.u',
                sprintf('%.6F', microtime(true)),
                new \DateTimeZone('UTC')
            )
        );
    }

    public function toString(): string
    {
        return $this->dateTime->format(self::FORMAT_STRING);
    }

    public static function fromString(string $dateTimeString): self
    {
        return new self(new \DateTimeImmutable($dateTimeString));
    }

    public function equals(self $dateTime): bool
    {
        return $this->toString() === $dateTime->toString();
    }

    public function comesAfter(self $dateTime): bool
    {
        return $this->dateTime > $dateTime->dateTime;
    }

    public function add(string $intervalSpec): self
    {
        $dateTime = $this->dateTime->add(new \DateInterval($intervalSpec));

        return new self($dateTime);
    }

    public function sub(string $intervalSpec): self
    {
        $dateTime = $this->dateTime->sub(new \DateInterval($intervalSpec));

        return new self($dateTime);
    }

    public function diff(self $dateTime): \DateInterval
    {
        return $this->dateTime->diff($dateTime->dateTime);
    }

    public function toBeginningOfWeek(): self
    {
        return new self(new \DateTimeImmutable($this->dateTime->format('o-\WW-1'), new \DateTimeZone('UTC')));
    }

    public function toYearWeekString(): string
    {
        return $this->dateTime->format('oW');
    }

    public function toNative(): \DateTimeImmutable
    {
        return $this->dateTime;
    }
}
```

## File: `src/Broadway/Domain/DomainEventStream.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

namespace Broadway\Domain;

/**
 * Represents a stream of DomainEventMessages in sequence.
 */
final class DomainEventStream implements \IteratorAggregate
{
    private $events;

    /**
     * @param mixed[] $events
     */
    public function __construct(array $events)
    {
        $this->events = $events;
    }

    public function getIterator(): \ArrayIterator
    {
        return new \ArrayIterator($this->events);
    }
}
```

## File: `src/Broadway/Domain/DomainMessage.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

namespace Broadway\Domain;

/**
 * Represents an important change in the domain.
 */
final class DomainMessage
{
    /**
     * @var int
     */
    private $playhead;

    /**
     * @var Metadata
     */
    private $metadata;

    private $payload;

    /**
     * @var string
     */
    private $id;

    /**
     * @var DateTime
     */
    private $recordedOn;

    public function __construct($id, int $playhead, Metadata $metadata, $payload, DateTime $recordedOn)
    {
        $this->id = (string) $id;
        $this->playhead = $playhead;
        $this->metadata = $metadata;
        $this->payload = $payload;
        $this->recordedOn = $recordedOn;
    }

    public function getId(): string
    {
        return $this->id;
    }

    public function getPlayhead(): int
    {
        return $this->playhead;
    }

    public function getMetadata(): Metadata
    {
        return $this->metadata;
    }

    public function getPayload()
    {
        return $this->payload;
    }

    public function getRecordedOn(): DateTime
    {
        return $this->recordedOn;
    }

    public function getType(): string
    {
        return strtr(get_class($this->payload), '\\', '.');
    }

    public static function recordNow($id, int $playhead, Metadata $metadata, $payload): self
    {
        return new self($id, $playhead, $metadata, $payload, DateTime::now());
    }

    /**
     * Creates a new DomainMessage with all things equal, except metadata.
     *
     * @param Metadata $metadata Metadata to add
     */
    public function andMetadata(Metadata $metadata): self
    {
        $newMetadata = $this->metadata->merge($metadata);

        return new self($this->id, $this->playhead, $newMetadata, $this->payload, $this->recordedOn);
    }
}
```

## File: `src/Broadway/Domain/Metadata.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

namespace Broadway\Domain;

use Broadway\Serializer\Serializable;

/**
 * Metadata adding extra information to the DomainMessage.
 */
final class Metadata implements Serializable
{
    private $values = [];

    public function __construct(array $values = [])
    {
        $this->values = $values;
    }

    /**
     * Helper method to construct an instance containing the key and value.
     */
    public static function kv($key, $value): self
    {
        return new self([$key => $value]);
    }

    /**
     * Merges the values of this and the other instance.
     */
    public function merge(self $otherMetadata): self
    {
        return new self(array_merge($this->values, $otherMetadata->values));
    }

    /**
     * Returns an array with all metadata.
     *
     * @return mixed[]
     */
    public function all(): array
    {
        return $this->values;
    }

    /**
     * Get a specific metadata value based on key.
     */
    public function get(string $key)
    {
        return $this->values[$key] ?? null;
    }

    public function serialize(): array
    {
        return $this->values;
    }

    public static function deserialize(array $data): self
    {
        return new self($data);
    }
}
```

## File: `src/Broadway/EventDispatcher/CallableEventDispatcher.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

namespace Broadway\EventDispatcher;

/**
 * Event dispatcher implementation.
 */
final class CallableEventDispatcher implements EventDispatcher
{
    private $listeners = [];

    public function dispatch(string $eventName, array $arguments): void
    {
        if (!isset($this->listeners[$eventName])) {
            return;
        }

        foreach ($this->listeners[$eventName] as $listener) {
            call_user_func_array($listener, $arguments);
        }
    }

    public function addListener(string $eventName, callable $callable): void
    {
        if (!isset($this->listeners[$eventName])) {
            $this->listeners[$eventName] = [];
        }

        $this->listeners[$eventName][] = $callable;
    }
}
```

## File: `src/Broadway/EventDispatcher/EventDispatcher.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

namespace Broadway\EventDispatcher;

/**
 * Base type for an event dispatcher.
 */
interface EventDispatcher
{
    public function dispatch(string $eventName, array $arguments): void;

    public function addListener(string $eventName, callable $callable): void;
}
```

## File: `src/Broadway/EventDispatcher/Testing/TraceableEventDispatcher.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

namespace Broadway\EventDispatcher\Testing;

use Broadway\EventDispatcher\EventDispatcher;

final class TraceableEventDispatcher implements EventDispatcher
{
    private $dispatchedEvents = [];

    public function dispatch(string $eventName, array $arguments): void
    {
        $this->dispatchedEvents[] = ['event' => $eventName, 'arguments' => $arguments];
    }

    public function addListener(string $eventName, callable $callable): void
    {
        return;
    }

    /**
     * @return mixed[]
     */
    public function getDispatchedEvents(): array
    {
        return $this->dispatchedEvents;
    }
}
```

## File: `src/Broadway/EventHandling/EventBus.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

namespace Broadway\EventHandling;

use Broadway\Domain\DomainEventStream;

/**
 * Publishes events to the subscribed event listeners.
 */
interface EventBus
{
    /**
     * Subscribes the event listener to the event bus.
     */
    public function subscribe(EventListener $eventListener): void;

    /**
     * Publishes the events from the domain event stream to the listeners.
     */
    public function publish(DomainEventStream $domainMessages): void;
}
```

## File: `src/Broadway/EventHandling/EventListener.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

namespace Broadway\EventHandling;

use Broadway\Domain\DomainMessage;

/**
 * Handles dispatched events.
 */
interface EventListener
{
    public function handle(DomainMessage $domainMessage): void;
}
```

## File: `src/Broadway/EventHandling/ReliableEventBus.php`
```php
<?php

declare(strict_types=1);

namespace Broadway\EventHandling;

use Broadway\Domain\DomainEventStream;
use Broadway\Domain\DomainMessage;
use Psr\Log\LoggerInterface;

class ReliableEventBus implements EventBus
{
    /** @var array */
    private $eventListeners = [];

    /** @var array */
    private $queue = [];

    /** @var bool */
    private $isPublishing = false;

    /** @var LoggerInterface */
    private $logger;

    public function __construct(LoggerInterface $logger)
    {
        $this->logger = $logger;
    }

    public function subscribe(EventListener $eventListener): void
    {
        $this->eventListeners[] = $eventListener;
    }

    public function publish(DomainEventStream $domainMessages): void
    {
        foreach ($domainMessages as $domainMessage) {
            $this->queue[] = $domainMessage;
        }

        if (!$this->isPublishing) {
            $this->isPublishing = true;

            try {
                while ($domainMessage = array_shift($this->queue)) {
                    $this->handleMessages($domainMessage);
                }
            } finally {
                $this->isPublishing = false;
            }
        }
    }

    private function handleMessages(DomainMessage $domainMessage): void
    {
        foreach ($this->eventListeners as $eventListener) {
            try {
                $eventListener->handle($domainMessage);
            } catch (\Throwable $exception) {
                $this->logger->error(sprintf('[Event LISTENER]: %s, failed with message %s', get_class($eventListener), $exception->getMessage()), [
                    'exception' => $exception,
                ]);
            }
        }
    }
}
```

## File: `src/Broadway/EventHandling/SimpleEventBus.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

namespace Broadway\EventHandling;

use Broadway\Domain\DomainEventStream;

/**
 * Simple synchronous publishing of events.
 */
final class SimpleEventBus implements EventBus
{
    private $eventListeners = [];
    private $queue = [];
    private $isPublishing = false;

    public function subscribe(EventListener $eventListener): void
    {
        $this->eventListeners[] = $eventListener;
    }

    public function publish(DomainEventStream $domainMessages): void
    {
        foreach ($domainMessages as $domainMessage) {
            $this->queue[] = $domainMessage;
        }

        if (!$this->isPublishing) {
            $this->isPublishing = true;

            try {
                while ($domainMessage = array_shift($this->queue)) {
                    foreach ($this->eventListeners as $eventListener) {
                        $eventListener->handle($domainMessage);
                    }
                }
            } finally {
                $this->isPublishing = false;
            }
        }
    }
}
```

## File: `src/Broadway/EventHandling/TraceableEventBus.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

namespace Broadway\EventHandling;

use Broadway\Domain\DomainEventStream;
use Broadway\Domain\DomainMessage;

/**
 * Event bus that is able to record all dispatched events.
 */
final class TraceableEventBus implements EventBus
{
    private $eventBus;
    private $recorded = [];
    private $tracing = false;

    public function __construct(EventBus $eventBus)
    {
        $this->eventBus = $eventBus;
    }

    public function subscribe(EventListener $eventListener): void
    {
        $this->eventBus->subscribe($eventListener);
    }

    public function publish(DomainEventStream $domainMessages): void
    {
        $this->eventBus->publish($domainMessages);

        if (!$this->tracing) {
            return;
        }

        foreach ($domainMessages as $domainMessage) {
            $this->recorded[] = $domainMessage;
        }
    }

    /**
     * @return mixed[] Payloads of the recorded events
     */
    public function getEvents(): array
    {
        return array_map(
            function (DomainMessage $message) {
                return $message->getPayload();
            },
            $this->recorded
        );
    }

    /**
     * Start tracing.
     */
    public function trace(): void
    {
        $this->tracing = true;
    }
}
```

## File: `src/Broadway/EventSourcing/AggregateRootAlreadyRegisteredException.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

namespace Broadway\EventSourcing;

/**
 * Exception thrown when an aggregate root is already registered.
 */
final class AggregateRootAlreadyRegisteredException extends \RuntimeException
{
}
```

## File: `src/Broadway/EventSourcing/EventSourcedAggregateRoot.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

namespace Broadway\EventSourcing;

use Broadway\Domain\AggregateRoot as AggregateRootInterface;
use Broadway\Domain\DomainEventStream;
use Broadway\Domain\DomainMessage;
use Broadway\Domain\Metadata;

/**
 * Convenience base class for event sourced aggregate roots.
 */
abstract class EventSourcedAggregateRoot implements AggregateRootInterface
{
    /**
     * @var array
     */
    private $uncommittedEvents = [];
    private $playhead = -1; // 0-based playhead allows events[0] to contain playhead 0

    /**
     * Applies an event. The event is added to the AggregateRoot's list of uncommitted events.
     */
    public function apply($event): void
    {
        $this->handleRecursively($event);

        ++$this->playhead;
        $this->uncommittedEvents[] = DomainMessage::recordNow(
            $this->getAggregateRootId(),
            $this->playhead,
            new Metadata([]),
            $event
        );
    }

    public function getUncommittedEvents(): DomainEventStream
    {
        $stream = new DomainEventStream($this->uncommittedEvents);

        $this->uncommittedEvents = [];

        return $stream;
    }

    /**
     * Initializes the aggregate using the given "history" of events.
     */
    public function initializeState(DomainEventStream $stream): void
    {
        foreach ($stream as $message) {
            ++$this->playhead;
            $this->handleRecursively($message->getPayload());
        }
    }

    /**
     * Handles event if capable.
     */
    protected function handle($event): void
    {
        $method = $this->getApplyMethod($event);

        if (!method_exists($this, $method)) {
            return;
        }

        $this->$method($event);
    }

    protected function handleRecursively($event): void
    {
        $this->handle($event);

        foreach ($this->getChildEntities() as $entity) {
            $entity->registerAggregateRoot($this);
            $entity->handleRecursively($event);
        }
    }

    /**
     * Returns all child entities.
     *
     * Override this method if your aggregate root contains child entities.
     *
     * @return EventSourcedEntity[]
     */
    protected function getChildEntities(): array
    {
        return [];
    }

    private function getApplyMethod($event): string
    {
        $classParts = explode('\\', get_class($event));

        return 'apply'.end($classParts);
    }

    public function getPlayhead(): int
    {
        return $this->playhead;
    }
}
```

## File: `src/Broadway/EventSourcing/EventSourcedEntity.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

namespace Broadway\EventSourcing;

/**
 * Interface representing event sourced entities.
 */
interface EventSourcedEntity
{
    /**
     * Recursively handles $event.
     */
    public function handleRecursively($event): void;

    /**
     * Registers aggregateRoot as this EventSourcedEntity's aggregate root.
     *
     * @throws AggregateRootAlreadyRegisteredException
     */
    public function registerAggregateRoot(EventSourcedAggregateRoot $aggregateRoot): void;
}
```

## File: `src/Broadway/EventSourcing/EventSourcingRepository.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

namespace Broadway\EventSourcing;

use Assert\Assertion as Assert;
use Broadway\Domain\AggregateRoot;
use Broadway\Domain\DomainEventStream;
use Broadway\EventHandling\EventBus;
use Broadway\EventSourcing\AggregateFactory\AggregateFactory;
use Broadway\EventStore\EventStore;
use Broadway\EventStore\EventStreamNotFoundException;
use Broadway\Repository\AggregateNotFoundException;
use Broadway\Repository\Repository;

/**
 * Naive initial implementation of an event sourced aggregate repository.
 */
class EventSourcingRepository implements Repository
{
    private $eventStore;
    private $eventBus;
    private $aggregateClass;
    private $eventStreamDecorators = [];
    private $aggregateFactory;

    /**
     * @param EventStreamDecorator[] $eventStreamDecorators
     */
    public function __construct(
        EventStore $eventStore,
        EventBus $eventBus,
        string $aggregateClass,
        AggregateFactory $aggregateFactory,
        array $eventStreamDecorators = []
    ) {
        $this->assertExtendsEventSourcedAggregateRoot($aggregateClass);

        $this->eventStore = $eventStore;
        $this->eventBus = $eventBus;
        $this->aggregateClass = $aggregateClass;
        $this->aggregateFactory = $aggregateFactory;
        $this->eventStreamDecorators = $eventStreamDecorators;
    }

    public function load($id): AggregateRoot
    {
        try {
            $domainEventStream = $this->eventStore->load($id);

            return $this->aggregateFactory->create($this->aggregateClass, $domainEventStream);
        } catch (EventStreamNotFoundException $e) {
            throw AggregateNotFoundException::create($id, $e);
        }
    }

    public function save(AggregateRoot $aggregate): void
    {
        // maybe we can get generics one day.... ;)
        Assert::isInstanceOf($aggregate, $this->aggregateClass);

        $domainEventStream = $aggregate->getUncommittedEvents();
        $eventStream = $this->decorateForWrite($aggregate, $domainEventStream);
        $this->eventStore->append($aggregate->getAggregateRootId(), $eventStream);
        $this->eventBus->publish($eventStream);
    }

    private function decorateForWrite(AggregateRoot $aggregate, DomainEventStream $eventStream): DomainEventStream
    {
        $aggregateType = get_class($aggregate);
        $aggregateIdentifier = $aggregate->getAggregateRootId();

        foreach ($this->eventStreamDecorators as $eventStreamDecorator) {
            $eventStream = $eventStreamDecorator->decorateForWrite($aggregateType, $aggregateIdentifier, $eventStream);
        }

        return $eventStream;
    }

    private function assertExtendsEventSourcedAggregateRoot(string $class): void
    {
        Assert::subclassOf(
            $class,
            EventSourcedAggregateRoot::class,
            sprintf("Class '%s' is not an EventSourcedAggregateRoot.", $class)
        );
    }
}
```

## File: `src/Broadway/EventSourcing/EventStreamDecorator.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

namespace Broadway\EventSourcing;

use Broadway\Domain\DomainEventStream;

/**
 * Interface implemented by event stream decorators.
 *
 * An event stream decorator can alter the domain event stream before it is
 * written. An example would be adding metadata before writing the events to
 * storage.
 */
interface EventStreamDecorator
{
    public function decorateForWrite(string $aggregateType, string $aggregateIdentifier, DomainEventStream $eventStream): DomainEventStream;
}
```

## File: `src/Broadway/EventSourcing/SimpleEventSourcedEntity.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

namespace Broadway\EventSourcing;

/**
 * Convenience base class for event sourced entities.
 */
abstract class SimpleEventSourcedEntity implements EventSourcedEntity
{
    /**
     * @var EventSourcedAggregateRoot|null
     */
    private $aggregateRoot;

    public function handleRecursively($event): void
    {
        $this->handle($event);

        foreach ($this->getChildEntities() as $entity) {
            $entity->registerAggregateRoot($this->aggregateRoot);
            $entity->handleRecursively($event);
        }
    }

    public function registerAggregateRoot(EventSourcedAggregateRoot $aggregateRoot): void
    {
        if (null !== $this->aggregateRoot && $this->aggregateRoot !== $aggregateRoot) {
            throw new AggregateRootAlreadyRegisteredException();
        }

        $this->aggregateRoot = $aggregateRoot;
    }

    protected function apply($event): void
    {
        $this->aggregateRoot->apply($event);
    }

    /**
     * Handles event if capable.
     */
    protected function handle($event): void
    {
        $method = $this->getApplyMethod($event);

        if (!method_exists($this, $method)) {
            return;
        }

        $this->$method($event);
    }

    /**
     * Returns all child entities.
     *
     * @return EventSourcedEntity[]
     */
    protected function getChildEntities(): array
    {
        return [];
    }

    private function getApplyMethod($event): string
    {
        $classParts = explode('\\', get_class($event));

        return 'apply'.end($classParts);
    }
}
```

## File: `src/Broadway/EventSourcing/AggregateFactory/AggregateFactory.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

namespace Broadway\EventSourcing\AggregateFactory;

use Broadway\Domain\DomainEventStream;
use Broadway\EventSourcing\EventSourcedAggregateRoot;

interface AggregateFactory
{
    /**
     * @param string $aggregateClass the FQCN of the Aggregate to create
     */
    public function create(string $aggregateClass, DomainEventStream $domainEventStream): EventSourcedAggregateRoot;
}
```

## File: `src/Broadway/EventSourcing/AggregateFactory/NamedConstructorAggregateFactory.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

namespace Broadway\EventSourcing\AggregateFactory;

use Assert\Assertion as Assert;
use Broadway\Domain\DomainEventStream;
use Broadway\EventSourcing\EventSourcedAggregateRoot;

/**
 * Creates aggregates by passing a DomainEventStream to the given public static method
 * which is itself responsible for returning an instance of itself.
 * E.g. (\Vendor\AggregateRoot::instantiateForReconstitution())->initializeState($domainEventStream);.
 */
final class NamedConstructorAggregateFactory implements AggregateFactory
{
    /**
     * @var string the name of the method to call on the Aggregate
     */
    private $staticConstructorMethod;

    public function __construct(string $staticConstructorMethod = 'instantiateForReconstitution')
    {
        $this->staticConstructorMethod = $staticConstructorMethod;
    }

    public function create(string $aggregateClass, DomainEventStream $domainEventStream): EventSourcedAggregateRoot
    {
        $methodCall = sprintf('%s::%s', $aggregateClass, $this->staticConstructorMethod);

        Assert::true(
            method_exists($aggregateClass, $this->staticConstructorMethod),
            sprintf('NamedConstructorAggregateFactory expected %s to exist', $methodCall)
        );

        $aggregate = call_user_func($methodCall);

        Assert::isInstanceOf($aggregate, $aggregateClass);

        $aggregate->initializeState($domainEventStream);

        return $aggregate;
    }
}
```

## File: `src/Broadway/EventSourcing/AggregateFactory/PublicConstructorAggregateFactory.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

namespace Broadway\EventSourcing\AggregateFactory;

use Broadway\Domain\DomainEventStream;
use Broadway\EventSourcing\EventSourcedAggregateRoot;

/**
 * Creates aggregates by instantiating the aggregateClass and then
 * passing a DomainEventStream to the public initializeState() method.
 * E.g. (new \Vendor\AggregateRoot)->initializeState($domainEventStream);.
 */
final class PublicConstructorAggregateFactory implements AggregateFactory
{
    public function create(string $aggregateClass, DomainEventStream $domainEventStream): EventSourcedAggregateRoot
    {
        $aggregate = new $aggregateClass();
        $aggregate->initializeState($domainEventStream);

        return $aggregate;
    }
}
```

## File: `src/Broadway/EventSourcing/AggregateFactory/ReflectionAggregateFactory.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

namespace Broadway\EventSourcing\AggregateFactory;

use Broadway\Domain\DomainEventStream;
use Broadway\EventSourcing\EventSourcedAggregateRoot;

/**
 * Creates aggregates with reflection without constructor.
 */
final class ReflectionAggregateFactory implements AggregateFactory
{
    public function create(string $aggregateClass, DomainEventStream $domainEventStream): EventSourcedAggregateRoot
    {
        $class = new \ReflectionClass($aggregateClass);
        $aggregate = $class->newInstanceWithoutConstructor();

        if (!$aggregate instanceof EventSourcedAggregateRoot) {
            throw new \LogicException(sprintf('Impossible to initialize "%s"', $aggregateClass));
        }

        $aggregate->initializeState($domainEventStream);

        return $aggregate;
    }
}
```

## File: `src/Broadway/EventSourcing/MetadataEnrichment/MetadataEnricher.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

namespace Broadway\EventSourcing\MetadataEnrichment;

use Broadway\Domain\Metadata;

/**
 * Adds extra metadata to already existing metadata.
 */
interface MetadataEnricher
{
    public function enrich(Metadata $metadata): Metadata;
}
```

## File: `src/Broadway/EventSourcing/MetadataEnrichment/MetadataEnrichingEventStreamDecorator.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

namespace Broadway\EventSourcing\MetadataEnrichment;

use Broadway\Domain\DomainEventStream;
use Broadway\Domain\Metadata;
use Broadway\EventSourcing\EventStreamDecorator;

/**
 * Event stream decorator that adds extra metadata.
 */
final class MetadataEnrichingEventStreamDecorator implements EventStreamDecorator
{
    private $metadataEnrichers;

    /**
     * @param MetadataEnricher[] $metadataEnrichers
     */
    public function __construct(array $metadataEnrichers = [])
    {
        $this->metadataEnrichers = $metadataEnrichers;
    }

    public function registerEnricher(MetadataEnricher $enricher): void
    {
        $this->metadataEnrichers[] = $enricher;
    }

    public function decorateForWrite(string $aggregateType, string $aggregateIdentifier, DomainEventStream $eventStream): DomainEventStream
    {
        if (empty($this->metadataEnrichers)) {
            return $eventStream;
        }

        $messages = [];

        foreach ($eventStream as $message) {
            $metadata = new Metadata();

            foreach ($this->metadataEnrichers as $metadataEnricher) {
                $metadata = $metadataEnricher->enrich($metadata);
            }

            $messages[] = $message->andMetadata($metadata);
        }

        return new DomainEventStream($messages);
    }
}
```

## File: `src/Broadway/EventSourcing/Testing/AggregateRootScenarioTestCase.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

namespace Broadway\EventSourcing\Testing;

use Broadway\EventSourcing\AggregateFactory\AggregateFactory;
use Broadway\EventSourcing\AggregateFactory\PublicConstructorAggregateFactory;
use PHPUnit\Framework\TestCase;

/**
 * Base test case that can be used to set up a command handler scenario.
 */
abstract class AggregateRootScenarioTestCase extends TestCase
{
    /**
     * @var Scenario
     */
    protected $scenario;

    protected function setUp(): void
    {
        $this->scenario = $this->createScenario();
    }

    protected function createScenario(): Scenario
    {
        $aggregateRootClass = $this->getAggregateRootClass();
        $factory = $this->getAggregateRootFactory();

        return new Scenario($this, $factory, $aggregateRootClass);
    }

    /**
     * Returns a string representing the aggregate root.
     *
     * @return string AggregateRoot
     */
    abstract protected function getAggregateRootClass(): string;

    /**
     * Returns a factory for instantiating an aggregate.
     *
     * @return AggregateFactory $factory
     */
    protected function getAggregateRootFactory(): AggregateFactory
    {
        return new PublicConstructorAggregateFactory();
    }
}
```

## File: `src/Broadway/EventSourcing/Testing/Scenario.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

namespace Broadway\EventSourcing\Testing;

use Broadway\Domain\DomainEventStream;
use Broadway\Domain\DomainMessage;
use Broadway\Domain\Metadata;
use Broadway\EventSourcing\AggregateFactory\AggregateFactory;
use PHPUnit\Framework\TestCase;

/**
 * Helper testing scenario to test command event sourced aggregate roots.
 *
 * The scenario will help with testing event sourced aggregate roots. A
 * scenario consists of three steps:
 *
 * 1) given(): Initialize the aggregate root using a history of events
 * 2) when():  A callable that calls a method on the event sourced aggregate root
 * 3) then():  Events that should have been applied
 */
class Scenario
{
    private $testCase;
    private $factory;

    private $aggregateRootClass;
    private $aggregateRootInstance;
    private $aggregateId;

    public function __construct(TestCase $testCase, AggregateFactory $factory, string $aggregateRootClass)
    {
        $this->testCase = $testCase;
        $this->factory = $factory;
        $this->aggregateRootClass = $aggregateRootClass;
        $this->aggregateId = '1';
    }

    public function withAggregateId(string $aggregateId): self
    {
        $this->aggregateId = $aggregateId;

        return $this;
    }

    /**
     * @param mixed[] $givens
     */
    public function given(?array $givens): self
    {
        if (null === $givens) {
            return $this;
        }

        $messages = [];
        $playhead = -1;
        foreach ($givens as $event) {
            ++$playhead;
            $messages[] = DomainMessage::recordNow(
                $this->aggregateId, $playhead, new Metadata([]), $event
            );
        }

        $this->aggregateRootInstance = $this->factory->create(
            $this->aggregateRootClass, new DomainEventStream($messages)
        );

        return $this;
    }

    public function when(callable $when): self
    {
        if (!is_callable($when)) {
            return $this;
        }

        if (null === $this->aggregateRootInstance) {
            $this->aggregateRootInstance = $when($this->aggregateRootInstance);

            $this->testCase->assertInstanceOf($this->aggregateRootClass, $this->aggregateRootInstance);
        } else {
            $when($this->aggregateRootInstance);
        }

        return $this;
    }

    /**
     * @param mixed[] $thens
     */
    public function then(array $thens): self
    {
        $this->testCase->assertEquals($thens, $this->getEvents());

        return $this;
    }

    /**
     * @return mixed[] Payloads of the recorded events
     */
    private function getEvents(): array
    {
        return array_map(function (DomainMessage $message) {
            return $message->getPayload();
        }, iterator_to_array($this->aggregateRootInstance->getUncommittedEvents()));
    }
}
```

## File: `src/Broadway/EventStore/CallableEventVisitor.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

namespace Broadway\EventStore;

use Broadway\Domain\DomainMessage;

final class CallableEventVisitor implements EventVisitor
{
    /**
     * @var callable
     */
    private $callable;

    public function __construct(callable $callable)
    {
        $this->callable = $callable;
    }

    public function doWithEvent(DomainMessage $domainMessage): void
    {
        call_user_func($this->callable, $domainMessage);
    }
}
```

## File: `src/Broadway/EventStore/ConcurrencyConflictResolvingEventStore.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

namespace Broadway\EventStore;

use Broadway\Domain\DomainEventStream;
use Broadway\Domain\DomainMessage;
use Broadway\EventStore\ConcurrencyConflictResolver\ConcurrencyConflictResolver;
use Broadway\EventStore\Exception\DuplicatePlayheadException;

final class ConcurrencyConflictResolvingEventStore implements EventStore
{
    /** @var EventStore */
    private $eventStore;

    /** @var ConcurrencyConflictResolver */
    private $conflictResolver;

    public function __construct(EventStore $eventStore, ConcurrencyConflictResolver $conflictResolver)
    {
        $this->eventStore = $eventStore;
        $this->conflictResolver = $conflictResolver;
    }

    public function append($id, DomainEventStream $uncommittedEvents): void
    {
        $id = (string) $id;

        if (empty(iterator_to_array($uncommittedEvents))) {
            return;
        }

        try {
            $this->eventStore->append($id, $uncommittedEvents);
        } catch (DuplicatePlayheadException $e) {
            $uncommittedPlayhead = $this->getStartingPlayhead($uncommittedEvents);

            $committedEvents = $this->eventStore->loadFromPlayhead($id, $uncommittedPlayhead);
            $conflictingEvents = $this->getConflictingEvents($uncommittedEvents, $committedEvents);

            $conflictResolvedEvents = [];
            $playhead = $this->getCurrentPlayhead($committedEvents);

            /** @var DomainMessage $uncommittedEvent */
            foreach ($uncommittedEvents as $uncommittedEvent) {
                foreach ($conflictingEvents as $conflictingEvent) {
                    if ($this->conflictResolver->conflictsWith($conflictingEvent, $uncommittedEvent)) {
                        throw $e;
                    }
                }

                ++$playhead;

                $conflictResolvedEvents[] = new DomainMessage(
                    $id,
                    $playhead,
                    $uncommittedEvent->getMetadata(),
                    $uncommittedEvent->getPayload(),
                    $uncommittedEvent->getRecordedOn());
            }

            $this->append($id, new DomainEventStream($conflictResolvedEvents));
        }
    }

    public function load($id): DomainEventStream
    {
        return $this->eventStore->load($id);
    }

    public function loadFromPlayhead($id, int $playhead): DomainEventStream
    {
        return $this->eventStore->loadFromPlayhead($id, $playhead);
    }

    private function getCurrentPlayhead(DomainEventStream $committedEvents): int
    {
        $events = iterator_to_array($committedEvents);
        /** @var DomainMessage $lastEvent */
        $lastEvent = end($events);
        $playhead = $lastEvent->getPlayhead();

        return $playhead;
    }

    private function getStartingPlayhead(DomainEventStream $uncommittedEvents): int
    {
        $events = iterator_to_array($uncommittedEvents);
        /** @var DomainMessage $firstEvent */
        $firstEvent = current($events);
        $playhead = $firstEvent->getPlayhead();

        return $playhead;
    }

    /**
     * @return DomainMessage[]
     */
    private function getConflictingEvents(
        DomainEventStream $uncommittedEvents,
        DomainEventStream $committedEvents
    ): array {
        $conflictingEvents = [];

        /** @var DomainMessage $committedEvent */
        foreach ($committedEvents as $committedEvent) {
            /** @var DomainMessage $uncommittedEvent */
            foreach ($uncommittedEvents as $uncommittedEvent) {
                if ($committedEvent->getPlayhead() >= $uncommittedEvent->getPlayhead()) {
                    $conflictingEvents[] = $committedEvent;

                    break;
                }
            }
        }

        return $conflictingEvents;
    }
}
```

## File: `src/Broadway/EventStore/EventStore.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

namespace Broadway\EventStore;

use Broadway\Domain\DomainEventStream;
use Broadway\EventStore\Exception\DuplicatePlayheadException;

/**
 * Loads and stores events.
 */
interface EventStore
{
    public function load($id): DomainEventStream;

    public function loadFromPlayhead($id, int $playhead): DomainEventStream;

    /**
     * @throws DuplicatePlayheadException
     */
    public function append($id, DomainEventStream $eventStream): void;
}
```

## File: `src/Broadway/EventStore/EventStoreException.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

namespace Broadway\EventStore;

/**
 * Exceptions thrown by event store implementations.
 */
abstract class EventStoreException extends \RuntimeException
{
}
```

## File: `src/Broadway/EventStore/EventStreamNotFoundException.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

namespace Broadway\EventStore;

/**
 * Exception thrown if an event stream is not found.
 */
final class EventStreamNotFoundException extends EventStoreException
{
}
```

## File: `src/Broadway/EventStore/EventVisitor.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

namespace Broadway\EventStore;

use Broadway\Domain\DomainMessage;

interface EventVisitor
{
    public function doWithEvent(DomainMessage $domainMessage): void;
}
```

## File: `src/Broadway/EventStore/InMemoryEventStore.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

namespace Broadway\EventStore;

use Broadway\Domain\DomainEventStream;
use Broadway\Domain\DomainMessage;
use Broadway\EventStore\Exception\DuplicatePlayheadException;
use Broadway\EventStore\Management\Criteria;
use Broadway\EventStore\Management\EventStoreManagement;

/**
 * In-memory implementation of an event store.
 *
 * Useful for testing code that uses an event store.
 */
final class InMemoryEventStore implements EventStore, EventStoreManagement
{
    private $events = [];

    public function load($id): DomainEventStream
    {
        $id = (string) $id;

        if (isset($this->events[$id])) {
            return new DomainEventStream($this->events[$id]);
        }

        throw new EventStreamNotFoundException(sprintf('EventStream not found for aggregate with id %s', $id));
    }

    public function loadFromPlayhead($id, int $playhead): DomainEventStream
    {
        $id = (string) $id;

        if (!isset($this->events[$id])) {
            return new DomainEventStream([]);
        }

        return new DomainEventStream(
            array_values(
                array_filter(
                    $this->events[$id],
                    function ($event) use ($playhead) {
                        return $playhead <= $event->getPlayhead();
                    }
                )
            )
        );
    }

    public function append($id, DomainEventStream $eventStream): void
    {
        $id = (string) $id;

        if (!isset($this->events[$id])) {
            $this->events[$id] = [];
        }

        $this->assertStream($this->events[$id], $eventStream);

        /** @var DomainMessage $event */
        foreach ($eventStream as $event) {
            $playhead = $event->getPlayhead();

            $this->events[$id][$playhead] = $event;
        }
    }

    /**
     * @param DomainMessage[] $events
     */
    private function assertStream(array $events, DomainEventStream $eventsToAppend): void
    {
        /** @var DomainMessage $event */
        foreach ($eventsToAppend as $event) {
            $playhead = $event->getPlayhead();

            if (isset($events[$playhead])) {
                throw new DuplicatePlayheadException($eventsToAppend);
            }
        }
    }

    public function visitEvents(Criteria $criteria, EventVisitor $eventVisitor): void
    {
        foreach ($this->events as $id => $events) {
            foreach ($events as $event) {
                if (!$criteria->isMatchedBy($event)) {
                    continue;
                }

                $eventVisitor->doWithEvent($event);
            }
        }
    }
}
```

## File: `src/Broadway/EventStore/InMemoryEventStoreException.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

namespace Broadway\EventStore;

/**
 * Wraps exceptions thrown by the in-memory event store.
 */
class InMemoryEventStoreException extends EventStoreException
{
}
```

## File: `src/Broadway/EventStore/TraceableEventStore.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

namespace Broadway\EventStore;

use Broadway\Domain\DomainEventStream;
use Broadway\Domain\DomainMessage;

/**
 * Event store that is able to record all appended events.
 */
final class TraceableEventStore implements EventStore
{
    private $eventStore;
    private $recorded = [];
    private $tracing = false;

    public function __construct(EventStore $eventStore)
    {
        $this->eventStore = $eventStore;
    }

    public function append($id, DomainEventStream $eventStream): void
    {
        $this->eventStore->append($id, $eventStream);

        if (!$this->tracing) {
            return;
        }

        foreach ($eventStream as $event) {
            $this->recorded[] = $event;
        }
    }

    /**
     * @return mixed[] Appended events
     */
    public function getEvents(): array
    {
        return array_map(
            function (DomainMessage $message) {
                return $message->getPayload();
            },
            $this->recorded
        );
    }

    public function load($id): DomainEventStream
    {
        return $this->eventStore->load($id);
    }

    public function loadFromPlayhead($id, int $playhead): DomainEventStream
    {
        return $this->eventStore->loadFromPlayhead($id, $playhead);
    }

    /**
     * Start tracing.
     */
    public function trace(): void
    {
        $this->tracing = true;
    }

    /**
     * Clear any previously recorded events.
     */
    public function clearEvents(): void
    {
        $this->recorded = [];
    }
}
```

## File: `src/Broadway/EventStore/ConcurrencyConflictResolver/BlacklistConcurrencyConflictResolver.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

namespace Broadway\EventStore\ConcurrencyConflictResolver;

use Assert\Assertion;
use Broadway\Domain\DomainMessage;

final class BlacklistConcurrencyConflictResolver implements ConcurrencyConflictResolver
{
    private $conflictingEvents = [];

    public function registerConflictingEvents(string $eventClass1, string $eventClass2): void
    {
        Assertion::classExists($eventClass1, $eventClass1.' is not a class');
        Assertion::classExists($eventClass2, $eventClass2.' is not a class');

        // bidirectional, unqiue class mapping
        $this->conflictingEvents[$eventClass1][$eventClass2] = true;
        $this->conflictingEvents[$eventClass2][$eventClass1] = true;
    }

    public function conflictsWith(DomainMessage $event1, DomainMessage $event2): bool
    {
        return isset($this->conflictingEvents[get_class($event1->getPayload())][get_class($event2->getPayload())]);
    }
}
```

## File: `src/Broadway/EventStore/ConcurrencyConflictResolver/ConcurrencyConflictResolver.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

namespace Broadway\EventStore\ConcurrencyConflictResolver;

use Broadway\Domain\DomainMessage;

interface ConcurrencyConflictResolver
{
    public function conflictsWith(DomainMessage $event1, DomainMessage $event2): bool;
}
```

## File: `src/Broadway/EventStore/ConcurrencyConflictResolver/WhitelistConcurrencyConflictResolver.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

namespace Broadway\EventStore\ConcurrencyConflictResolver;

use Assert\Assertion;
use Broadway\Domain\DomainMessage;

final class WhitelistConcurrencyConflictResolver implements ConcurrencyConflictResolver
{
    private $independentEvents = [];

    public function registerIndependentEvents(string $eventClass1, string $eventClass2): void
    {
        Assertion::classExists($eventClass1, $eventClass1.' is not a class');
        Assertion::classExists($eventClass2, $eventClass2.' is not a class');

        // bidirectional, unique class mapping
        $this->independentEvents[$eventClass1][$eventClass2] = true;
        $this->independentEvents[$eventClass2][$eventClass1] = true;
    }

    public function conflictsWith(DomainMessage $event1, DomainMessage $event2): bool
    {
        return !isset($this->independentEvents[get_class($event1->getPayload())][get_class($event2->getPayload())]);
    }
}
```

## File: `src/Broadway/EventStore/Exception/DuplicatePlayheadException.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

namespace Broadway\EventStore\Exception;

use Broadway\Domain\DomainEventStream;
use Broadway\EventStore\EventStoreException;

final class DuplicatePlayheadException extends EventStoreException
{
    /**
     * @var DomainEventStream
     */
    private $eventStream;

    /**
     * @param \Exception $previous
     */
    public function __construct(DomainEventStream $eventStream, $previous = null)
    {
        parent::__construct('', 0, $previous);

        $this->eventStream = $eventStream;
    }

    public function getEventStream(): DomainEventStream
    {
        return $this->eventStream;
    }
}
```

## File: `src/Broadway/EventStore/Exception/InvalidIdentifierException.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

namespace Broadway\EventStore\Exception;

/**
 * Class InvalidIdentifierException.
 */
final class InvalidIdentifierException extends \InvalidArgumentException
{
}
```

## File: `src/Broadway/EventStore/Management/Criteria.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

namespace Broadway\EventStore\Management;

use Broadway\Domain\DomainMessage;

final class Criteria
{
    private $aggregateRootTypes = [];
    private $aggregateRootIds = [];
    private $eventTypes = [];

    /**
     * Create a new criteria with the specified aggregate root types.
     *
     * @param string[] $aggregateRootTypes
     */
    public function withAggregateRootTypes(array $aggregateRootTypes): self
    {
        $instance = clone $this;
        $instance->aggregateRootTypes = $aggregateRootTypes;

        return $instance;
    }

    /**
     * Create a new criteria with the specified aggregate root IDs.
     *
     * @param mixed[] $aggregateRootIds
     */
    public function withAggregateRootIds(array $aggregateRootIds): self
    {
        $instance = clone $this;
        $instance->aggregateRootIds = $aggregateRootIds;

        return $instance;
    }

    /**
     * Create a new criteria with the specified event types.
     *
     * @param mixed[] $eventTypes
     */
    public function withEventTypes(array $eventTypes): self
    {
        $instance = clone $this;
        $instance->eventTypes = $eventTypes;

        return $instance;
    }

    /**
     * Get the aggregate root types for the criteria.
     *
     * @return string[]
     */
    public function getAggregateRootTypes(): array
    {
        return $this->aggregateRootTypes;
    }

    /**
     * Get the aggregate root IDs for the criteria.
     *
     * @return mixed[]
     */
    public function getAggregateRootIds(): array
    {
        return $this->aggregateRootIds;
    }

    /**
     * Get the event types for the criteria.
     *
     * @return mixed[]
     */
    public function getEventTypes(): array
    {
        return $this->eventTypes;
    }

    /**
     * Create a new criteria.
     */
    public static function create(): self
    {
        return new static();
    }

    /**
     * Determine if a domain message is matched by this criteria.
     */
    public function isMatchedBy(DomainMessage $domainMessage): bool
    {
        if ($this->aggregateRootTypes) {
            throw new CriteriaNotSupportedException('Cannot match criteria based on aggregate root types.');
        }

        if ($this->aggregateRootIds && !in_array($domainMessage->getId(), $this->aggregateRootIds)) {
            return false;
        }

        if ($this->eventTypes && !in_array($domainMessage->getType(), $this->eventTypes)) {
            return false;
        }

        return true;
    }
}
```

## File: `src/Broadway/EventStore/Management/CriteriaNotSupportedException.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

namespace Broadway\EventStore\Management;

/**
 * Criteria not supported by implementation.
 *
 * In some cases an event store implementation may implement management
 * but not be able to satisfy all criteria options. In this case, the
 * implementation must throw this exception.
 *
 * Class CriteriaNotSupportedException
 */
final class CriteriaNotSupportedException extends EventStoreManagementException
{
}
```

## File: `src/Broadway/EventStore/Management/EventStoreManagement.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

namespace Broadway\EventStore\Management;

use Broadway\EventStore\EventVisitor;

interface EventStoreManagement
{
    public function visitEvents(Criteria $criteria, EventVisitor $eventVisitor): void;
}
```

## File: `src/Broadway/EventStore/Management/EventStoreManagementException.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

namespace Broadway\EventStore\Management;

/**
 * Exceptions thrown by event store implementations.
 */
abstract class EventStoreManagementException extends \RuntimeException
{
}
```

## File: `src/Broadway/EventStore/Management/Testing/EventStoreManagementTest.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

namespace Broadway\EventStore\Management\Testing;

use Broadway\Domain\DateTime;
use Broadway\Domain\DomainEventStream;
use Broadway\Domain\DomainMessage;
use Broadway\Domain\Metadata;
use Broadway\EventStore\EventStore;
use Broadway\EventStore\EventVisitor;
use Broadway\EventStore\Management\Criteria;
use Broadway\EventStore\Management\CriteriaNotSupportedException;
use Broadway\EventStore\Management\EventStoreManagement;
use Broadway\Serializer\Serializable;
use PHPUnit\Framework\TestCase;

abstract class EventStoreManagementTest extends TestCase
{
    /**
     * @var EventStore|EventStoreManagement
     */
    protected $eventStore;

    /**
     * @var DateTime
     */
    protected $now;

    protected function setUp(): void
    {
        $this->now = DateTime::now();
        $this->eventStore = $this->createEventStore();
        $this->createAndInsertEventFixtures();
    }

    protected function visitEvents(?Criteria $criteria = null)
    {
        $eventVisitor = new RecordingEventVisitor();

        $this->eventStore->visitEvents($criteria, $eventVisitor);

        return $eventVisitor->getVisitedEvents();
    }

    abstract protected function createEventStore();

    /** @test */
    public function it_visits_all_events()
    {
        $visitedEvents = $this->visitEvents(Criteria::create());

        $this->assertVisitedEventsArEquals($this->getEventFixtures(), $visitedEvents);
    }

    /** @test */
    public function it_visits_aggregate_root_ids()
    {
        $visitedEvents = $this->visitEvents(Criteria::create()->withAggregateRootIds([
            $this->getId(1),
            $this->getId(3),
        ]));

        $this->assertVisitedEventsArEquals([
            $this->createDomainMessage(1, 0, new Start()),
            $this->createDomainMessage(1, 1, new Middle('a')),
            $this->createDomainMessage(1, 2, new Middle('b')),
            $this->createDomainMessage(1, 3, new Middle('c')),
            $this->createDomainMessage(3, 0, new Start()),
            $this->createDomainMessage(3, 1, new Middle('a')),
            $this->createDomainMessage(3, 2, new Middle('b')),
            $this->createDomainMessage(3, 3, new Middle('c')),
            $this->createDomainMessage(1, 4, new Middle('d')),
            $this->createDomainMessage(3, 4, new Middle('d')),
            $this->createDomainMessage(1, 5, new End()),
            $this->createDomainMessage(3, 5, new End()),
        ], $visitedEvents);
    }

    /** @test */
    public function it_visits_event_types()
    {
        $visitedEvents = $this->visitEvents(Criteria::create()
            ->withEventTypes([
                'Broadway.EventStore.Management.Testing.Start',
                'Broadway.EventStore.Management.Testing.End',
            ])
        );

        $this->assertVisitedEventsArEquals([
            $this->createDomainMessage(1, 0, new Start()),
            $this->createDomainMessage(2, 0, new Start()),
            $this->createDomainMessage(2, 5, new End()),
            $this->createDomainMessage(3, 0, new Start()),
            $this->createDomainMessage(4, 0, new Start()),
            $this->createDomainMessage(4, 5, new End()),
            $this->createDomainMessage(1, 5, new End()),
            $this->createDomainMessage(3, 5, new End()),
        ], $visitedEvents);
    }

    /**
     * @test
     */
    public function it_visits_aggregate_root_types()
    {
        $this->expectException(CriteriaNotSupportedException::class);

        $this->visitEvents(Criteria::create()
            ->withAggregateRootTypes([
                'Broadway.EventStore.Management.Testing.AggregateTypeOne',
                'Broadway.EventStore.Management.Testing.AggregateTypeTwo',
            ])
        );
    }

    private function createAndInsertEventFixtures()
    {
        foreach ($this->getEventFixtures() as $domainMessage) {
            $this->eventStore->append($domainMessage->getId(), new DomainEventStream([$domainMessage]));
        }
    }

    /**
     * @return DomainMessage[]
     */
    protected function getEventFixtures()
    {
        return [
            $this->createDomainMessage(1, 0, new Start()),
            $this->createDomainMessage(1, 1, new Middle('a')),
            $this->createDomainMessage(1, 2, new Middle('b')),

            $this->createDomainMessage(2, 0, new Start()),
            $this->createDomainMessage(2, 1, new Middle('a')),
            $this->createDomainMessage(2, 2, new Middle('b')),
            $this->createDomainMessage(2, 3, new Middle('c')),
            $this->createDomainMessage(2, 4, new Middle('d')),
            $this->createDomainMessage(2, 5, new End()),

            $this->createDomainMessage(1, 3, new Middle('c')),

            $this->createDomainMessage(3, 0, new Start()),
            $this->createDomainMessage(3, 1, new Middle('a')),
            $this->createDomainMessage(3, 2, new Middle('b')),
            $this->createDomainMessage(3, 3, new Middle('c')),

            $this->createDomainMessage(1, 4, new Middle('d')),

            $this->createDomainMessage(4, 0, new Start()),
            $this->createDomainMessage(4, 1, new Middle('a')),
            $this->createDomainMessage(4, 2, new Middle('b')),
            $this->createDomainMessage(4, 3, new Middle('c')),
            $this->createDomainMessage(4, 4, new Middle('d')),
            $this->createDomainMessage(4, 5, new End()),

            $this->createDomainMessage(3, 4, new Middle('d')),

            $this->createDomainMessage(1, 5, new End()),

            $this->createDomainMessage(3, 5, new End()),
        ];
    }

    private function createDomainMessage($id, int $playhead, $event)
    {
        $id = $this->getId($id);

        return new DomainMessage((string) $id, $playhead, new Metadata([]), $event, $this->now);
    }

    private function getId($id): string
    {
        return sprintf('%08d-%04d-4%03d-%04d-%012d', $id, $id, $id, $id, $id);
    }

    private function assertVisitedEventsArEquals(array $expectedEvents, array $actualEvents)
    {
        $this->assertEquals(
            $this->groupEventsByAggregateTypeAndId($expectedEvents),
            $this->groupEventsByAggregateTypeAndId($actualEvents)
        );
    }

    /**
     * @param DomainMessage[] $events
     */
    private function groupEventsByAggregateTypeAndId(array $events)
    {
        $eventsByAggregateTypeAndId = [];
        foreach ($events as $event) {
            $type = $event->getType();
            $id = $event->getId();

            if (!array_key_exists($type, $eventsByAggregateTypeAndId)) {
                $eventsByAggregateTypeAndId[$type] = [];
            }

            if (!array_key_exists($id, $eventsByAggregateTypeAndId[$type])) {
                $eventsByAggregateTypeAndId[$type][$id] = [];
            }

            $eventsByAggregateTypeAndId[$type][$id][] = $event;
        }

        return $eventsByAggregateTypeAndId;
    }
}

class RecordingEventVisitor implements EventVisitor
{
    /**
     * @var DomainMessage[]
     */
    private $visitedEvents;

    public function doWithEvent(DomainMessage $domainMessage): void
    {
        $this->visitedEvents[] = $domainMessage;
    }

    public function getVisitedEvents()
    {
        return $this->visitedEvents;
    }

    public function clearVisitedEvents()
    {
        $this->visitedEvents = [];
    }
}

class Event implements Serializable
{
    public static function deserialize(array $data)
    {
        return new static();
    }

    public function serialize(): array
    {
        return [];
    }
}

class Start extends Event
{
}

class Middle extends Event
{
    public $position;

    public function __construct($position)
    {
        $this->position = $position;
    }

    public static function deserialize(array $data)
    {
        return new static($data['position']);
    }

    public function serialize(): array
    {
        return [
            'position' => $this->position,
        ];
    }
}

class End extends Event
{
}
```

## File: `src/Broadway/EventStore/Testing/EventStoreTest.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

namespace Broadway\EventStore\Testing;

use Broadway\Domain\DateTime;
use Broadway\Domain\DomainEventStream;
use Broadway\Domain\DomainMessage;
use Broadway\Domain\Metadata;
use Broadway\EventStore\EventStreamNotFoundException;
use Broadway\EventStore\Exception\DuplicatePlayheadException;
use Broadway\Serializer\Serializable;
use Broadway\UuidGenerator\Rfc4122\Version4Generator;
use PHPUnit\Framework\Error\Error;
use PHPUnit\Framework\TestCase;

abstract class EventStoreTest extends TestCase
{
    /**
     * @varEventStore
     */
    protected $eventStore;

    /**
     * @test
     *
     * @dataProvider idDataProvider
     */
    public function it_creates_a_new_entry_when_id_is_new($id)
    {
        $domainEventStream = new DomainEventStream([
            $this->createDomainMessage($id, 0),
            $this->createDomainMessage($id, 1),
            $this->createDomainMessage($id, 2),
            $this->createDomainMessage($id, 3),
        ]);

        $this->eventStore->append($id, $domainEventStream);

        $this->assertEquals($domainEventStream, $this->eventStore->load($id));
    }

    /**
     * @test
     *
     * @dataProvider idDataProvider
     */
    public function it_appends_to_an_already_existing_stream($id)
    {
        $dateTime = DateTime::fromString('2014-03-12T14:17:19.176169+00:00');
        $domainEventStream = new DomainEventStream([
            $this->createDomainMessage($id, 0, $dateTime),
            $this->createDomainMessage($id, 1, $dateTime),
            $this->createDomainMessage($id, 2, $dateTime),
        ]);
        $this->eventStore->append($id, $domainEventStream);
        $appendedEventStream = new DomainEventStream([
            $this->createDomainMessage($id, 3, $dateTime),
            $this->createDomainMessage($id, 4, $dateTime),
            $this->createDomainMessage($id, 5, $dateTime),
        ]);

        $this->eventStore->append($id, $appendedEventStream);

        $expected = new DomainEventStream([
            $this->createDomainMessage($id, 0, $dateTime),
            $this->createDomainMessage($id, 1, $dateTime),
            $this->createDomainMessage($id, 2, $dateTime),
            $this->createDomainMessage($id, 3, $dateTime),
            $this->createDomainMessage($id, 4, $dateTime),
            $this->createDomainMessage($id, 5, $dateTime),
        ]);
        $this->assertEquals($expected, $this->eventStore->load($id));
    }

    /**
     * @test
     *
     * @dataProvider idDataProvider
     */
    public function it_throws_an_exception_when_requesting_the_stream_of_a_non_existing_aggregate($id)
    {
        $this->expectException(EventStreamNotFoundException::class);

        $this->eventStore->load($id);
    }

    /**
     * @test
     *
     * @dataProvider idDataProvider
     */
    public function it_throws_an_exception_when_appending_a_duplicate_playhead($id)
    {
        $eventStream = new DomainEventStream([$this->createDomainMessage($id, 0)]);

        $this->expectException(DuplicatePlayheadException::class);

        $this->eventStore->append($id, $eventStream);
        $this->eventStore->append($id, $eventStream);
    }

    /**
     * @test
     */
    public function it_throws_an_exception_when_an_id_cannot_be_converted_to_a_string()
    {
        $id = new IdentityThatCannotBeConvertedToAString();

        if (PHP_VERSION_ID >= 70400) {
            $this->expectException(\Throwable::class);
        } else {
            $this->expectException(Error::class);
        }

        $this->expectExceptionMessage(sprintf(
            'Object of class %s could not be converted to string',
            IdentityThatCannotBeConvertedToAString::class
        ));

        $this->eventStore->append($id, new DomainEventStream([]));
    }

    /**
     * @test
     *
     * @dataProvider idDataProvider
     */
    public function it_loads_events_starting_from_a_given_playhead($id)
    {
        $dateTime = DateTime::fromString('2014-03-12T14:17:19.176169+00:00');
        $domainEventStream = new DomainEventStream([
            $this->createDomainMessage($id, 0, $dateTime),
            $this->createDomainMessage($id, 1, $dateTime),
            $this->createDomainMessage($id, 2, $dateTime),
            $this->createDomainMessage($id, 3, $dateTime),
        ]);

        $this->eventStore->append($id, $domainEventStream);

        $expected = new DomainEventStream([
            $this->createDomainMessage($id, 2, $dateTime),
            $this->createDomainMessage($id, 3, $dateTime),
        ]);

        $this->assertEquals($expected, $this->eventStore->loadFromPlayhead($id, 2));
    }

    /** @test */
    public function empty_set_of_events_can_be_added(): void
    {
        $domainMessage = $this->createDomainMessage(1, 0);
        $baseStream = new DomainEventStream([$domainMessage]);
        $this->eventStore->append(1, $baseStream);
        $appendedEventStream = new DomainEventStream([]);

        $this->eventStore->append(1, $appendedEventStream);

        $events = $this->eventStore->load(1);
        $this->assertCount(1, $events);
    }

    /**
     * @test
     *
     * @dataProvider idDataProvider
     */
    public function it_returns_empty_event_stream_when_no_events_are_committed_since_given_playhead($id)
    {
        $this->eventStore->append($id, new DomainEventStream([
            $this->createDomainMessage($id, 0),
        ]));

        $this->assertEquals(
            new DomainEventStream([]),
            $this->eventStore->loadFromPlayhead($id, 1)
        );
    }

    public function idDataProvider()
    {
        return [
            'Simple String' => [
                'Yolntbyaac', // You only live nine times because you are a cat
            ],
            'Identitiy' => [
                new StringIdentity(
                    'Yolntbyaac' // You only live nine times because you are a cat
                ),
            ],
            'Integer' => [
                42, // test an int
            ],
            'UUID String' => [
                (new Version4Generator())->generate(), // test UUID
            ],
        ];
    }

    protected function createDomainMessage($id, int $playhead, ?DateTime $recordedOn = null)
    {
        return new DomainMessage($id, $playhead, new Metadata([]), new Event(), $recordedOn ? $recordedOn : DateTime::now());
    }
}

class Event implements Serializable
{
    public static function deserialize(array $data)
    {
        return new self();
    }

    public function serialize(): array
    {
        return [];
    }
}

class StringIdentity
{
    private $id;

    public function __construct($id)
    {
        $this->id = $id;
    }

    public function __toString()
    {
        return (string) $this->id;
    }
}

class IdentityThatCannotBeConvertedToAString
{
}
```

## File: `src/Broadway/Processor/Processor.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

namespace Broadway\Processor;

use Broadway\Domain\DomainMessage;
use Broadway\EventHandling\EventListener;

/**
 * Base class for event stream processors.
 */
abstract class Processor implements EventListener
{
    public function handle(DomainMessage $domainMessage): void
    {
        $event = $domainMessage->getPayload();
        $method = $this->getHandleMethod($event);

        if (!method_exists($this, $method)) {
            return;
        }

        $this->$method($event, $domainMessage);
    }

    private function getHandleMethod($event): string
    {
        $classParts = explode('\\', get_class($event));

        return 'handle'.end($classParts);
    }
}
```

## File: `src/Broadway/ReadModel/Identifiable.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

namespace Broadway\ReadModel;

/**
 * Represents a read model.
 */
interface Identifiable
{
    public function getId(): string;
}
```

## File: `src/Broadway/ReadModel/Projector.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

namespace Broadway\ReadModel;

use Broadway\Domain\DomainMessage;
use Broadway\EventHandling\EventListener;

/**
 * Handles events and projects to a read model.
 */
abstract class Projector implements EventListener
{
    public function handle(DomainMessage $domainMessage): void
    {
        $event = $domainMessage->getPayload();
        $method = $this->getHandleMethod($event);

        if (!method_exists($this, $method)) {
            return;
        }

        $this->$method($event, $domainMessage);
    }

    private function getHandleMethod($event): string
    {
        $classParts = explode('\\', get_class($event));

        return 'apply'.end($classParts);
    }
}
```

## File: `src/Broadway/ReadModel/Repository.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

namespace Broadway\ReadModel;

/**
 * Abstraction for the storage of read models.
 */
interface Repository
{
    public function save(Identifiable $data): void;

    public function find($id): ?Identifiable;

    /**
     * @return Identifiable[]
     */
    public function findBy(array $fields): array;

    /**
     * @return Identifiable[]
     */
    public function findAll(): array;

    public function remove($id): void;
}
```

## File: `src/Broadway/ReadModel/RepositoryFactory.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

namespace Broadway\ReadModel;

/**
 * Creates repositories.
 */
interface RepositoryFactory
{
    public function create(string $name, string $class): Repository;
}
```

## File: `src/Broadway/ReadModel/SerializableReadModel.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

namespace Broadway\ReadModel;

use Broadway\Serializer\Serializable;

/**
 * Represents a serializable read model.
 */
interface SerializableReadModel extends Serializable, Identifiable
{
}
```

## File: `src/Broadway/ReadModel/Transferable.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

namespace Broadway\ReadModel;

/**
 * Represent a repository that can transfer its data to another repository.
 */
interface Transferable
{
    public function transferTo(Repository $otherRepository): void;
}
```

## File: `src/Broadway/ReadModel/InMemory/InMemoryRepository.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

namespace Broadway\ReadModel\InMemory;

use Broadway\ReadModel\Identifiable;
use Broadway\ReadModel\Repository;
use Broadway\ReadModel\Transferable;

/**
 * In-memory implementation of a read model repository.
 *
 * The in-memory repository is useful for testing code.
 */
final class InMemoryRepository implements Repository, Transferable
{
    private $data = [];

    public function save(Identifiable $model): void
    {
        $this->data[$model->getId()] = $model;
    }

    public function find($id): ?Identifiable
    {
        $id = (string) $id;
        if (isset($this->data[$id])) {
            return $this->data[$id];
        }

        return null;
    }

    public function findBy(array $fields): array
    {
        if (!$fields) {
            return [];
        }

        return array_values(array_filter($this->data, function ($model) use ($fields) {
            foreach ($fields as $field => $value) {
                $getter = 'get'.ucfirst($field);

                $modelValue = $model->$getter();

                if (is_array($modelValue) && !in_array($value, $modelValue)) {
                    return false;
                } elseif (!is_array($modelValue) && $modelValue !== $value) {
                    return false;
                }
            }

            return true;
        }));
    }

    public function findAll(): array
    {
        return array_values($this->data);
    }

    public function transferTo(Repository $otherRepository): void
    {
        foreach ($this->data as $model) {
            $otherRepository->save($model);
        }
    }

    public function remove($id): void
    {
        unset($this->data[(string) $id]);
    }
}
```

## File: `src/Broadway/ReadModel/InMemory/InMemoryRepositoryFactory.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

namespace Broadway\ReadModel\InMemory;

use Broadway\ReadModel\Repository;
use Broadway\ReadModel\RepositoryFactory;

/**
 * Creates in-memory repositories.
 */
final class InMemoryRepositoryFactory implements RepositoryFactory
{
    public function create(string $name, string $class): Repository
    {
        return new InMemoryRepository();
    }
}
```

## File: `src/Broadway/ReadModel/Testing/DomainMessageScenario.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

namespace Broadway\ReadModel\Testing;

use Assert\Assertion;
use Broadway\Domain\DomainMessage;
use Broadway\EventHandling\EventListener;
use Broadway\ReadModel\Repository;
use PHPUnit\Framework\TestCase;

/**
 * Helper testing scenario to test projects.
 *
 * The scenario will help with testing projectors. A scenario consists of
 * three steps:
 *
 * 1) given(): Lets the projector handle some domain messages
 * 2) when():  When a specific domain message is handled
 * 3) then():  The repository should contain these read models
 */
final class DomainMessageScenario
{
    private $testCase;
    private $projector;
    private $repository;

    public function __construct(
        TestCase $testCase,
        Repository $repository,
        EventListener $projector
    ) {
        $this->testCase = $testCase;
        $this->repository = $repository;
        $this->projector = $projector;
    }

    /**
     * @param DomainMessage[] $domainMessages
     */
    public function given(array $domainMessages = []): self
    {
        Assertion::allIsInstanceOf($domainMessages, DomainMessage::class);

        foreach ($domainMessages as $given) {
            $this->projector->handle($given);
        }

        return $this;
    }

    public function when(DomainMessage $domainMessage): self
    {
        $this->projector->handle($domainMessage);

        return $this;
    }

    public function then(array $expectedData): self
    {
        $this->testCase->assertEquals($expectedData, $this->repository->findAll());

        return $this;
    }
}
```

## File: `src/Broadway/ReadModel/Testing/ProjectorScenarioTestCase.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

namespace Broadway\ReadModel\Testing;

use Broadway\ReadModel\InMemory\InMemoryRepository;
use Broadway\ReadModel\Projector;
use PHPUnit\Framework\TestCase;

/**
 * Base test case that can be used to set up a projector scenario.
 */
abstract class ProjectorScenarioTestCase extends TestCase
{
    /**
     * @var Scenario
     */
    protected $scenario;

    protected function setUp(): void
    {
        $this->scenario = $this->createScenario();
    }

    protected function createScenario(): Scenario
    {
        $repository = new InMemoryRepository();

        return new Scenario($this, $repository, $this->createProjector($repository));
    }

    abstract protected function createProjector(InMemoryRepository $repository): Projector;
}
```

## File: `src/Broadway/ReadModel/Testing/RepositoryTestCase.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

namespace Broadway\ReadModel\Testing;

use Broadway\ReadModel\Repository;
use PHPUnit\Framework\TestCase;

abstract class RepositoryTestCase extends TestCase
{
    /**
     * @var Repository
     */
    protected $repository;

    protected function setUp(): void
    {
        $this->repository = $this->createRepository();
    }

    abstract protected function createRepository(): Repository;

    /**
     * @test
     */
    public function it_saves_and_finds_read_models_by_id()
    {
        $model = $this->createReadModel('1', 'othillo', 'bar');

        $this->repository->save($model);

        $this->assertEquals($model, $this->repository->find(1));
    }

    /**
     * @test
     */
    public function it_saves_and_finds_read_models_with_a_value_object_id()
    {
        $id = new TestReadModelId('42');
        $model = $this->createReadModel($id, 'othillo', 'bar');

        $this->repository->save($model);

        $this->assertEquals($model, $this->repository->find($id));
    }

    /**
     * @test
     */
    public function it_returns_null_if_not_found_on_empty_repo()
    {
        $this->assertEquals(null, $this->repository->find(2));
    }

    /**
     * @test
     */
    public function it_returns_null_if_not_found()
    {
        $model = $this->createReadModel('1', 'othillo', 'bar');

        $this->repository->save($model);

        $this->assertNull($this->repository->find(2));
    }

    /**
     * @test
     */
    public function it_finds_by_name()
    {
        $model1 = $this->createReadModel('1', 'othillo', 'bar');
        $model2 = $this->createReadModel('2', 'asm89', 'baz');

        $this->repository->save($model1);
        $this->repository->save($model2);

        $this->assertEquals([$model1], $this->repository->findBy(['name' => 'othillo']));
        $this->assertEquals([$model2], $this->repository->findBy(['name' => 'asm89']));
    }

    /**
     * @test
     */
    public function it_finds_by_one_element_in_array()
    {
        $model1 = $this->createReadModel('1', 'othillo', 'bar', ['elem1', 'elem2']);
        $model2 = $this->createReadModel('2', 'asm89', 'baz', ['elem3', 'elem4']);

        $this->repository->save($model1);
        $this->repository->save($model2);

        $this->assertEquals([$model1], $this->repository->findBy(['array' => 'elem1']));
        $this->assertEquals([$model2], $this->repository->findBy(['array' => 'elem4']));
    }

    /**
     * @test
     */
    public function it_finds_if_all_clauses_match()
    {
        $model1 = $this->createReadModel('1', 'othillo', 'bar');
        $model2 = $this->createReadModel('2', 'asm89', 'baz');

        $this->repository->save($model1);
        $this->repository->save($model2);

        $this->assertEquals([$model1], $this->repository->findBy(['name' => 'othillo', 'foo' => 'bar']));
        $this->assertEquals([$model2], $this->repository->findBy(['name' => 'asm89', 'foo' => 'baz']));
    }

    /**
     * @test
     */
    public function it_does_not_find_when_one_of_the_clauses_doesnt_match()
    {
        $model1 = $this->createReadModel('1', 'othillo', 'bar');
        $model2 = $this->createReadModel('2', 'asm89', 'baz');

        $this->repository->save($model1);
        $this->repository->save($model2);

        $this->assertEquals([], $this->repository->findBy(['name' => 'othillo', 'foo' => 'baz']));
        $this->assertEquals([], $this->repository->findBy(['name' => 'asm89', 'foo' => 'bar']));
    }

    /**
     * @test
     */
    public function it_returns_empty_array_when_found_nothing()
    {
        $model1 = $this->createReadModel('1', 'othillo', 'bar');
        $model2 = $this->createReadModel('2', 'asm89', 'baz');

        $this->repository->save($model1);
        $this->repository->save($model2);

        $this->assertEquals([], $this->repository->findBy(['name' => 'Jan']));
    }

    /**
     * @test
     */
    public function it_returns_empty_array_when_searching_for_empty_array()
    {
        $model = $this->createReadModel('1', 'othillo', 'bar');

        $this->repository->save($model);

        $this->assertEquals([], $this->repository->findBy([]));
    }

    /**
     * @test
     */
    public function it_removes_a_readmodel()
    {
        $model = $this->createReadModel('1', 'John', 'Foo', ['foo' => 'bar']);
        $this->repository->save($model);

        $this->repository->remove('1');

        $this->assertEquals([], $this->repository->findAll());
    }

    /**
     * @test
     */
    public function it_removes_a_read_model_using_a_value_object_as_its_id()
    {
        $id = new TestReadModelId('175');

        $model = $this->createReadModel($id, 'Bado', 'Foo', ['foo' => 'bar']);
        $this->repository->save($model);

        $this->repository->remove($id);

        $this->assertEquals([], $this->repository->findAll());
    }

    /**
     * @test
     */
    public function it_returns_all_read_models()
    {
        $model1 = $this->createReadModel('1', 'othillo', 'bar');
        $model2 = $this->createReadModel('2', 'asm89', 'baz');
        $model3 = $this->createReadModel('3', 'edelprino', 'baz');

        $this->repository->save($model1);
        $this->repository->save($model2);
        $this->repository->save($model3);

        $this->assertEquals([$model1, $model2, $model3], $this->repository->findAll());
    }

    protected function createReadModel($id, $name, $foo, array $array = [])
    {
        return new RepositoryTestReadModel($id, $name, $foo, $array);
    }
}

class TestReadModelId
{
    private $value;

    public function __construct($value)
    {
        $this->value = $value;
    }

    public function __toString()
    {
        return $this->value;
    }
}
```

## File: `src/Broadway/ReadModel/Testing/RepositoryTestReadModel.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

namespace Broadway\ReadModel\Testing;

use Broadway\ReadModel\SerializableReadModel;

class RepositoryTestReadModel implements SerializableReadModel
{
    private $id;
    private $name;
    private $foo;
    private $array;

    public function __construct($id, string $name, $foo, array $array)
    {
        $this->id = (string) $id;
        $this->name = $name;
        $this->foo = $foo;
        $this->array = $array;
    }

    public function getId(): string
    {
        return $this->id;
    }

    public function getName(): string
    {
        return $this->name;
    }

    public function getFoo()
    {
        return $this->foo;
    }

    public function getArray(): array
    {
        return $this->array;
    }

    public function serialize(): array
    {
        return get_object_vars($this);
    }

    public static function deserialize(array $data)
    {
        return new self($data['id'], $data['name'], $data['foo'], $data['array']);
    }
}
```

## File: `src/Broadway/ReadModel/Testing/Scenario.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

namespace Broadway\ReadModel\Testing;

use Broadway\Domain\DateTime;
use Broadway\Domain\DomainMessage;
use Broadway\Domain\Metadata;
use Broadway\EventHandling\EventListener;
use Broadway\ReadModel\Repository;
use PHPUnit\Framework\TestCase;

/**
 * Helper testing scenario to test projects.
 *
 * The scenario will help with testing projectors. A scenario consists of
 * three steps:
 *
 * 1) given(): Lets the projector handle some events
 * 2) when():  When a specific event is handled
 * 3) then():  The repository should contain these read models
 */
class Scenario
{
    private $testCase;
    private $projector;
    private $repository;
    private $playhead;
    private $aggregateId;
    private $dateTimeGenerator;

    public function __construct(
        TestCase $testCase,
        Repository $repository,
        EventListener $projector
    ) {
        $this->testCase = $testCase;
        $this->repository = $repository;
        $this->projector = $projector;
        $this->playhead = -1;
        $this->aggregateId = '1';
        $this->dateTimeGenerator = function ($event) {
            return DateTime::now();
        };
    }

    public function withAggregateId(string $aggregateId): self
    {
        $this->aggregateId = $aggregateId;

        return $this;
    }

    public function withDateTimeGenerator(callable $dateTimeGenerator): self
    {
        $this->dateTimeGenerator = $dateTimeGenerator;

        return $this;
    }

    public function given(array $events = []): self
    {
        foreach ($events as $given) {
            $this->projector->handle($this->createDomainMessageForEvent($given, null));
        }

        return $this;
    }

    public function when($event, ?DateTime $occurredOn = null): self
    {
        $this->projector->handle($this->createDomainMessageForEvent($event, $occurredOn));

        return $this;
    }

    public function then(array $expectedData): self
    {
        $this->testCase->assertEquals($expectedData, $this->repository->findAll());

        return $this;
    }

    /**
     * @param ?DateTime $occurredOn
     */
    private function createDomainMessageForEvent($event, ?DateTime $occurredOn): DomainMessage
    {
        ++$this->playhead;

        if (null === $occurredOn) {
            $dateTimeGenerator = $this->dateTimeGenerator;
            $occurredOn = $dateTimeGenerator($event);
        }

        return new DomainMessage($this->aggregateId, $this->playhead, new Metadata([]), $event, $occurredOn);
    }
}
```

## File: `src/Broadway/ReadModel/Testing/SerializableReadModelTestCase.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

namespace Broadway\ReadModel\Testing;

use Broadway\ReadModel\SerializableReadModel;
use Broadway\Serializer\Serializable;
use Broadway\Serializer\SimpleInterfaceSerializer;
use PHPUnit\Framework\TestCase;

/**
 * Base test case that can be used to test a serializable read model.
 */
abstract class SerializableReadModelTestCase extends TestCase
{
    /**
     * @test
     */
    public function its_serializable()
    {
        $this->assertInstanceOf(Serializable::class, $this->createSerializableReadModel());
    }

    /**
     * @test
     */
    public function serializing_and_deserializing_yields_the_same_object()
    {
        $serializer = new SimpleInterfaceSerializer();
        $readModel = $this->createSerializableReadModel();

        $serialized = $serializer->serialize($readModel);
        $deserialized = $serializer->deserialize($serialized);

        $this->assertEquals($readModel, $deserialized);
    }

    abstract protected function createSerializableReadModel(): SerializableReadModel;
}
```

## File: `src/Broadway/Replaying/Replayer.php`
```php
<?php

declare(strict_types=1);

namespace Broadway\Replaying;

use Broadway\EventStore\EventVisitor;
use Broadway\EventStore\Management\Criteria;
use Broadway\EventStore\Management\EventStoreManagement;

final class Replayer
{
    private $eventStore;
    private $eventVisitor;

    public function __construct(
        EventStoreManagement $eventStore,
        EventVisitor $eventVisitor
    ) {
        $this->eventStore = $eventStore;
        $this->eventVisitor = $eventVisitor;
    }

    public function replay(Criteria $criteria)
    {
        $this->eventStore->visitEvents($criteria, $this->eventVisitor);
    }
}
```

## File: `src/Broadway/Repository/AggregateNotFoundException.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

namespace Broadway\Repository;

use Exception;

/**
 * Exception thrown when an aggregate is not found.
 */
final class AggregateNotFoundException extends \RuntimeException
{
    public static function create($id, ?\Exception $previous = null): self
    {
        return new self(sprintf("Aggregate with id '%s' not found", $id), 0, $previous);
    }
}
```

## File: `src/Broadway/Repository/Repository.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

namespace Broadway\Repository;

use Broadway\Domain\AggregateRoot;

/**
 * Repository for aggregate roots.
 */
interface Repository
{
    /**
     * Adds the aggregate to the repository.
     */
    public function save(AggregateRoot $aggregate): void;

    /**
     * Loads an aggregate from the given id.
     *
     * @throws AggregateNotFoundException
     */
    public function load($id): AggregateRoot;
}
```

## File: `src/Broadway/Serializer/ReflectionSerializer.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

namespace Broadway\Serializer;

use Assert\Assertion as Assert;

/**
 * Serializer that deeply serializes objects with the help of reflection.
 */
class ReflectionSerializer implements Serializer
{
    public function serialize($object): array
    {
        return $this->serializeObjectRecursively($object);
    }

    private function serializeValue($value)
    {
        if (is_object($value)) {
            return $this->serializeObjectRecursively($value);
        } elseif (is_array($value)) {
            return $this->serializeArrayRecursively($value);
        }

        return $value;
    }

    private function serializeArrayRecursively(array $array): array
    {
        $data = [];
        foreach ($array as $key => $value) {
            $data[$key] = $this->serializeValue($value);
        }

        return $data;
    }

    /**
     * @param object $object
     */
    private function serializeObjectRecursively($object): array
    {
        $reflection = new \ReflectionClass($object);
        $properties = $reflection->getProperties();

        $data = [];
        foreach ($properties as $property) {
            $name = $property->getName();

            $property->setAccessible(true);
            $value = $property->getValue($object);
            $property->setAccessible(false);

            $data[$name] = $this->serializeValue($value);
        }

        return [
            'class' => get_class($object),
            'payload' => $data,
        ];
    }

    public function deserialize(array $serializedObject)
    {
        return $this->deserializeObjectRecursively($serializedObject);
    }

    private function deserializeValue($value)
    {
        if (is_array($value) && isset($value['class']) && isset($value['payload'])) {
            return $this->deserializeObjectRecursively($value);
        } elseif (is_array($value)) {
            return $this->deserializeArrayRecursively($value);
        }

        return $value;
    }

    private function deserializeArrayRecursively(array $array): array
    {
        $data = [];
        foreach ($array as $key => $value) {
            $data[$key] = $this->deserializeValue($value);
        }

        return $data;
    }

    /**
     * @param array $serializedObject
     *
     * @return object
     */
    private function deserializeObjectRecursively($serializedObject)
    {
        Assert::keyExists($serializedObject, 'class', "Key 'class' should be set.");
        Assert::keyExists($serializedObject, 'payload', "Key 'payload' should be set.");

        $reflection = new \ReflectionClass($serializedObject['class']);
        $properties = $reflection->getProperties();
        $object = $reflection->newInstanceWithoutConstructor();

        foreach ($serializedObject['payload'] as $name => $value) {
            $matchedProperty = $this->findProperty($properties, $name);
            if (null === $matchedProperty) {
                throw new SerializationException(sprintf('Property \'%s\' not found for object \'%s\'', $name, $serializedObject['class']));
            }

            $value = $this->deserializeValue($value);

            $matchedProperty->setAccessible(true);
            $matchedProperty->setValue($object, $value);
            $matchedProperty->setAccessible(false);
        }

        return $object;
    }

    /**
     * @param \ReflectionProperty[] $properties
     */
    private function findProperty(array $properties, string $name): ?\ReflectionProperty
    {
        foreach ($properties as $property) {
            if ($property->getName() === $name) {
                return $property;
            }
        }

        return null;
    }
}
```

## File: `src/Broadway/Serializer/Serializable.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

namespace Broadway\Serializer;

/**
 * Contract for objects serializable by the SimpleInterfaceSerializer.
 */
interface Serializable
{
    /**
     * @return mixed The object instance
     */
    public static function deserialize(array $data);

    public function serialize(): array;
}
```

## File: `src/Broadway/Serializer/SerializationException.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

namespace Broadway\Serializer;

/**
 * Exception thrown if an error occurs during (de)serialization.
 */
class SerializationException extends \RuntimeException
{
}
```

## File: `src/Broadway/Serializer/Serializer.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

namespace Broadway\Serializer;

/**
 * Interface for classes that can serialize arbitrary objects into arrays with
 * scalars (for now).
 */
interface Serializer
{
    /**
     * @throws SerializationException
     */
    public function serialize($object): array;

    /**
     * @throws SerializationException
     */
    public function deserialize(array $serializedObject);
}
```

## File: `src/Broadway/Serializer/SimpleInterfaceSerializer.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

namespace Broadway\Serializer;

use Assert\Assertion as Assert;

/**
 * Serializer that serializes objects that implement a specific interface.
 */
final class SimpleInterfaceSerializer implements Serializer
{
    public function serialize($object): array
    {
        if (!$object instanceof Serializable) {
            throw new SerializationException(sprintf('Object \'%s\' does not implement Broadway\Serializer\Serializable', get_class($object)));
        }

        return [
            'class' => get_class($object),
            'payload' => $object->serialize(),
        ];
    }

    public function deserialize(array $serializedObject)
    {
        Assert::keyExists($serializedObject, 'class', "Key 'class' should be set.");
        Assert::keyExists($serializedObject, 'payload', "Key 'payload' should be set.");

        if (!in_array(Serializable::class, class_implements($serializedObject['class']))) {
            throw new SerializationException(sprintf('Class \'%s\' does not implement Broadway\Serializer\Serializable', $serializedObject['class']));
        }

        return $serializedObject['class']::deserialize($serializedObject['payload']);
    }
}
```

## File: `src/Broadway/Serializer/Testing/SerializableEventTestCase.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

namespace Broadway\Serializer\Testing;

use Broadway\Serializer\Serializable;
use Broadway\Serializer\SimpleInterfaceSerializer;
use PHPUnit\Framework\TestCase;

/**
 * Helper to test if events implement the Serializable contract.
 */
abstract class SerializableEventTestCase extends TestCase
{
    /**
     * @test
     */
    public function its_serializable()
    {
        $this->assertInstanceOf(Serializable::class, $this->createEvent());
    }

    /**
     * @test
     */
    public function serializing_and_deserializing_yields_the_same_object()
    {
        $serializer = new SimpleInterfaceSerializer();
        $event = $this->createEvent();

        $serialized = $serializer->serialize($event);
        $deserialized = $serializer->deserialize($serialized);

        $this->assertEquals($event, $deserialized);
    }

    abstract protected function createEvent();
}
```

## File: `src/Broadway/Upcasting/SequentialUpcasterChain.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2022 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

namespace Broadway\Upcasting;

use Broadway\Domain\DomainMessage;

final class SequentialUpcasterChain implements UpcasterChain
{
    /**
     * @var Upcaster[]
     */
    private $upcasters;

    /**
     * @param Upcaster[] $upcasters
     */
    public function __construct(array $upcasters)
    {
        $this->upcasters = $upcasters;
    }

    public function upcast(DomainMessage $domainMessage): DomainMessage
    {
        foreach ($this->upcasters as $upcaster) {
            if ($upcaster->supports($domainMessage)) {
                $domainMessage = $upcaster->upcast($domainMessage);
            }
        }

        return $domainMessage;
    }
}
```

## File: `src/Broadway/Upcasting/Upcaster.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2022 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

namespace Broadway\Upcasting;

use Broadway\Domain\DomainMessage;

interface Upcaster
{
    public function supports(DomainMessage $domainMessage): bool;

    public function upcast(DomainMessage $domainMessage): DomainMessage;
}
```

## File: `src/Broadway/Upcasting/UpcasterChain.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2022 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

namespace Broadway\Upcasting;

use Broadway\Domain\DomainMessage;

interface UpcasterChain
{
    public function upcast(DomainMessage $domainMessage): DomainMessage;
}
```

## File: `src/Broadway/Upcasting/UpcastingEventStore.php`
```php
<?php

declare(strict_types=1);

namespace Broadway\Upcasting;

use Broadway\Domain\DomainEventStream;
use Broadway\EventStore\EventStore;
use Broadway\EventStore\EventVisitor;
use Broadway\EventStore\Management\Criteria;
use Broadway\EventStore\Management\EventStoreManagement;

final class UpcastingEventStore implements EventStore, EventStoreManagement
{
    /**
     * @var EventStore&EventStoreManagement
     */
    private $eventStore;
    /**
     * @var UpcasterChain
     */
    private $upcasterChain;

    public function __construct($eventStore, UpcasterChain $upcasterChain)
    {
        $this->eventStore = $eventStore;
        $this->upcasterChain = $upcasterChain;
    }

    public function load($id): DomainEventStream
    {
        return $this->upcastStream(
            $this->eventStore->load($id),
            $id
        );
    }

    private function upcastStream(DomainEventStream $eventStream, $id): DomainEventStream
    {
        $upcastedEvents = [];

        foreach ($eventStream as $domainMessage) {
            $upcastedEvents[] = $this->upcasterChain->upcast($domainMessage);
        }

        return new DomainEventStream($upcastedEvents);
    }

    public function loadFromPlayhead($id, int $playhead): DomainEventStream
    {
        return $this->upcastStream(
            $this->eventStore->loadFromPlayhead($id, $playhead),
            $id
        );
    }

    public function append($id, DomainEventStream $eventStream): void
    {
        $this->eventStore->append($id, $eventStream);
    }

    public function visitEvents(Criteria $criteria, EventVisitor $eventVisitor): void
    {
        $this->eventStore->visitEvents($criteria, $eventVisitor);
    }
}
```

## File: `test/Broadway/Auditing/CommandLoggerTest.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

namespace Broadway\Auditing;

use PHPUnit\Framework\TestCase;

class CommandLoggerTest extends TestCase
{
    /**
     * @var TraceableLogger
     */
    private $logger;

    /**
     * @var Command
     */
    private $command;

    /**
     * @var CommandLogger
     */
    private $commandAuditLogger;

    /**
     * @var CommandSerializer
     */
    private $commandSerializer;

    protected function setUp(): void
    {
        $this->logger = new TraceableLogger();

        $this->commandSerializer = $this->prophesize(CommandSerializer::class);

        $this->command = new Command();
        $this->exception = new MyException('Yolo', 5);

        $this->commandAuditLogger = new CommandLogger($this->logger, $this->commandSerializer->reveal());
    }

    /**
     * @test
     */
    public function it_logs_the_command_on_success()
    {
        $this->commandSerializer
            ->serialize($this->command)
            ->willReturn(['all' => 'the data']);

        $this->commandAuditLogger->onCommandHandlingSuccess($this->command);

        $this->assertCount(1, $this->logger->info);
        $this->assertEquals('{"status":"success","command":{"class":"Broadway\\\\Auditing\\\\Command","data":{"all":"the data"}}}', $this->logger->info[0]);
    }

    /**
     * @test
     */
    public function it_logs_the_command_on_failure()
    {
        $this->commandSerializer
            ->serialize($this->command)
            ->willReturn(['all' => 'the data']);

        $this->commandAuditLogger->onCommandHandlingFailure($this->command, $this->exception);

        $this->assertCount(1, $this->logger->info);
        $loggedData = json_decode($this->logger->info[0], true);

        $this->assertArrayHasKey('status', $loggedData);
        $this->assertEquals('failure', $loggedData['status']);
        $this->assertArrayHasKey('command', $loggedData);
        $this->assertArrayHasKey('class', $loggedData['command']);
        $this->assertEquals('Broadway\Auditing\Command', $loggedData['command']['class']);
        $this->assertArrayHasKey('data', $loggedData['command']);
        $this->assertEquals(['all' => 'the data'], $loggedData['command']['data']);

        $this->assertArrayHasKey('exception', $loggedData);
        $this->assertArrayHasKey('message', $loggedData['exception']);
        $this->assertArrayHasKey('file', $loggedData['exception']);
        $this->assertArrayHasKey('class', $loggedData['exception']);
        $this->assertArrayHasKey('line', $loggedData['exception']);
        $this->assertArrayHasKey('code', $loggedData['exception']);

        $this->assertEquals('Yolo', $loggedData['exception']['message']);
        $this->assertEquals('Broadway\Auditing\MyException', $loggedData['exception']['class']);
        $this->assertStringEndsWith('test/Broadway/Auditing/CommandLoggerTest.php', $loggedData['exception']['file']);
    }
}

use Psr\Log\LoggerInterface;

class TraceableLogger implements LoggerInterface
{
    public $info = [];

    public function emergency($message, array $context = [])
    {
    }

    public function alert($message, array $context = [])
    {
    }

    public function critical($message, array $context = [])
    {
    }

    public function error($message, array $context = [])
    {
    }

    public function warning($message, array $context = [])
    {
    }

    public function notice($message, array $context = [])
    {
    }

    public function info($message, array $context = [])
    {
        $this->info[] = $message;
    }

    public function debug($message, array $context = [])
    {
    }

    public function log($level, $message, array $context = [])
    {
    }
}

class Command
{
    public $name = 'name';
}

class MyException extends \Exception
{
}
```

## File: `test/Broadway/Auditing/NullByteCommandSerializerTest.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

namespace Broadway\Auditing;

use PHPUnit\Framework\TestCase;

class NullByteCommandSerializerTest extends TestCase
{
    /**
     * @var NullByteCommandSerializer
     */
    private $commandSerializer;

    /**
     * @var MyCommand
     */
    private $command;

    protected function setUp(): void
    {
        $this->commandSerializer = new NullByteCommandSerializer();
        $this->command = new MyCommand();
    }

    /**
     * @test
     */
    public function it_returns_a_json_string()
    {
        $serializedCommand = $this->commandSerializer->serialize($this->command);

        $this->assertTrue(is_array($serializedCommand));

        $expected = [
            'public' => 'public',
            '-*-protected' => 'protected',
            '-Broadway\\Auditing\\MyCommand-private' => 'private',
        ];

        $this->assertEquals($expected, $serializedCommand);
    }
}

class MyCommand
{
    public $public = 'public';
    protected $protected = 'protected';
    private $private = 'private';
}
```

## File: `test/Broadway/CommandHandling/ClosureCommandHandlerTest.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

namespace Broadway\CommandHandling;

use Broadway\CommandHandling\Exception\ClosureParameterNotAnObjectException;
use Broadway\CommandHandling\Exception\CommandNotAnObjectException;
use PHPUnit\Framework\TestCase;

class ClosureCommandHandlerTest extends TestCase
{
    /**
     * @test
     */
    public function it_delegates_command_to_proper_handle_function()
    {
        $commandHandler = new ClosureCommandHandler();
        $commandHandler->add(function (ClosureCommandHandlerTestCommand $command) {
            $command->handle = true;
        });

        $command = new ClosureCommandHandlerTestCommand();
        $commandHandler->handle($command);

        $this->assertTrue($command->handle);
    }

    /**
     * @test
     */
    public function it_throws_when_handling_a_non_object_command()
    {
        $commandHandler = new ClosureCommandHandler();

        $this->expectException(CommandNotAnObjectException::class);

        $commandHandler->handle('foo');
    }

    /**
     * @test
     */
    public function it_throws_when_adding_a_closure_without_an_object_argument()
    {
        $commandHandler = new ClosureCommandHandler();
        $this->expectException(ClosureParameterNotAnObjectException::class);

        $commandHandler->add(function ($params = null) { });
    }

    /**
     * @test
     */
    public function it_throws_when_adding_a_closure_without_an_object_argument_and_no_params()
    {
        $commandHandler = new ClosureCommandHandler();
        $this->expectException(ClosureParameterNotAnObjectException::class);

        $commandHandler->add(function () { });
    }
}

class ClosureCommandHandlerTestCommand
{
    public $handle = false;
}
```

## File: `test/Broadway/CommandHandling/CommandHandlerTest.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

namespace Broadway\CommandHandling;

use Broadway\CommandHandling\Exception\CommandNotAnObjectException;
use PHPUnit\Framework\TestCase;

class CommandHandlerTest extends TestCase
{
    /**
     * @test
     */
    public function it_delegates_command_to_proper_handle_function()
    {
        $commandHandler = new TestCommandHandler();
        $command = new CommandHandlerTestCommand();
        $commandHandler->handle($command);

        $this->assertTrue($commandHandler->handled);
    }

    /**
     * @test
     *
     * @dataProvider unresolvableCommands
     */
    public function handle_should_throw_exception_when_impossible_to_delegate_to_a_valid_method($command)
    {
        $commandHandler = new TestCommandHandler();

        $this->expectException(CommandNotAnObjectException::class);

        $commandHandler->handle($command);
    }

    public function unresolvableCommands()
    {
        return [
            [null],
            [false],
            ['foo'],
            [1],
            [['foo', 'bar']],
        ];
    }
}

class TestCommandHandler extends SimpleCommandHandler
{
    public $handled = false;

    public function handleCommandHandlerTestCommand(CommandHandlerTestCommand $command)
    {
        $this->handled = true;
    }
}

class CommandHandlerTestCommand
{
}
```

## File: `test/Broadway/CommandHandling/EventDispatchingCommandBusTest.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

namespace Broadway\CommandHandling;

use Broadway\EventDispatcher\EventDispatcher;
use PHPUnit\Framework\MockObject\MockObject;
use PHPUnit\Framework\TestCase;

class EventDispatchingCommandBusTest extends TestCase
{
    /**
     * @var CommandBus|MockObject
     */
    private $baseCommandBus;

    /**
     * @var Command
     */
    private $command;

    /**
     * @var EventDispatcher|MockObject
     */
    private $eventDispatcher;

    /**
     * @var EventDispatchingCommandBus
     */
    private $eventDispatchingCommandBus;

    /**
     * @var CommandHandler|MockObject
     */
    private $subscriber;

    protected function setUp(): void
    {
        $this->eventDispatcher = $this->createMock(EventDispatcher::class);
        $this->baseCommandBus = $this->createMock(CommandBus::class);
        $this->subscriber = $this->createMock(CommandHandler::class);

        $this->command = new Command();

        $this->eventDispatchingCommandBus = new EventDispatchingCommandBus($this->baseCommandBus, $this->eventDispatcher);
    }

    /**
     * @test
     */
    public function it_dispatches_the_success_event()
    {
        $this->eventDispatcher->expects($this->once())
            ->method('dispatch')
            ->with(EventDispatchingCommandBus::EVENT_COMMAND_SUCCESS, ['command' => $this->command]);

        $this->eventDispatchingCommandBus->dispatch($this->command);
    }

    /**
     * @test
     */
    public function it_dispatches_the_failure_event_and_forwards_the_exception()
    {
        $exception = new MyException();
        $this->eventDispatcher->expects($this->once())
            ->method('dispatch')
            ->with(
                EventDispatchingCommandBus::EVENT_COMMAND_FAILURE,
                ['command' => $this->command, 'exception' => $exception]
            );

        $this->baseCommandBus->expects($this->once())
            ->method('dispatch')
            ->with($this->command)
            ->will($this->throwException($exception));

        $this->expectException(MyException::class);

        $this->eventDispatchingCommandBus->dispatch($this->command);
    }

    /**
     * @test
     */
    public function it_forwards_the_dispatched_command()
    {
        $this->baseCommandBus->expects($this->once())
            ->method('dispatch')
            ->with($this->command);

        $this->eventDispatchingCommandBus->dispatch($this->command);
    }

    /**
     * @test
     */
    public function it_forwards_the_subscriber()
    {
        $this->baseCommandBus->expects($this->once())
            ->method('subscribe')
            ->with($this->subscriber);

        $this->eventDispatchingCommandBus->subscribe($this->subscriber);
    }
}

class Command
{
}

class MyException extends \Exception
{
}
```

## File: `test/Broadway/CommandHandling/SimpleCommandBusTest.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

namespace Broadway\CommandHandling;

use PHPUnit\Framework\MockObject\MockObject;
use PHPUnit\Framework\TestCase;

class SimpleCommandBusTest extends TestCase
{
    /**
     * @var SimpleCommandBus
     */
    private $commandBus;

    protected function setUp(): void
    {
        $this->commandBus = new SimpleCommandBus();
    }

    /**
     * @test
     */
    public function it_dispatches_commands_to_subscribed_handlers()
    {
        $command = ['Hi' => 'There'];

        $this->commandBus->subscribe($this->createCommandHandlerMock($command));
        $this->commandBus->subscribe($this->createCommandHandlerMock($command));
        $this->commandBus->dispatch($command);
    }

    /**
     * @test
     */
    public function it_does_not_handle_new_commands_before_all_commandhandlers_have_run()
    {
        $command1 = ['foo' => 'bar'];
        $command2 = ['foo' => 'bas'];

        $commandHandler = $this->createMock(CommandHandler::class);

        $commandHandler
            ->expects($this->at(0))
            ->method('handle')
            ->with($command1);

        $commandHandler
            ->expects($this->at(1))
            ->method('handle')
            ->with($command2);

        $this->commandBus->subscribe(new SimpleCommandBusTestHandler($this->commandBus, $command2));
        $this->commandBus->subscribe($commandHandler);
        $this->commandBus->dispatch($command1);
    }

    /**
     * @test
     */
    public function it_should_still_handle_commands_after_exception()
    {
        $command1 = ['foo' => 'bar'];
        $command2 = ['foo' => 'bas'];

        $commandHandler = $this->createMock(CommandHandler::class);
        $simpleHandler = $this->createMock(CommandHandler::class);

        $commandHandler
            ->expects($this->at(0))
            ->method('handle')
            ->with($command1)
            ->will($this->throwException(new \Exception('I failed.')));

        $commandHandler
            ->expects($this->at(1))
            ->method('handle')
            ->with($command2);

        $simpleHandler
            ->expects($this->once())
            ->method('handle')
            ->with($command2);

        $this->commandBus->subscribe($commandHandler);
        $this->commandBus->subscribe($simpleHandler);

        try {
            $this->commandBus->dispatch($command1);
        } catch (\Exception $e) {
            $this->assertEquals('I failed.', $e->getMessage());
        }

        $this->commandBus->dispatch($command2);
    }

    private function createCommandHandlerMock(array $expectedCommand): MockObject
    {
        $mock = $this->createMock(CommandHandler::class);

        $mock
            ->expects($this->once())
            ->method('handle')
            ->with($expectedCommand);

        return $mock;
    }
}

class SimpleCommandBusTestHandler implements CommandHandler
{
    private $commandBus;
    private $handled = false;
    private $dispatchableCommand;

    public function __construct($commandBus, $dispatchableCommand)
    {
        $this->commandBus = $commandBus;
        $this->dispatchableCommand = $dispatchableCommand;
    }

    public function handle($command): void
    {
        if (!$this->handled) {
            $this->commandBus->dispatch($this->dispatchableCommand);
            $this->handled = true;
        }
    }
}
```

## File: `test/Broadway/CommandHandling/Testing/TraceableCommandBusTest.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

namespace Broadway\CommandHandling\Testing;

use PHPUnit\Framework\TestCase;

class TraceableCommandBusTest extends TestCase
{
    /**
     * @var TraceableCommandBus
     */
    private $commandBus;

    protected function setUp(): void
    {
        $this->commandBus = new TraceableCommandBus();
    }

    /**
     * @test
     */
    public function it_records_commands_when_recording_is_activated()
    {
        $command1 = ['Not' => 'Recorded'];
        $command2 = ['Hello' => 'There'];
        $command3 = ['Tomato' => 'Juice'];

        $this->commandBus->dispatch($command1);
        $this->assertEquals($this->commandBus->getRecordedCommands(), []);

        $this->commandBus->record();

        $this->commandBus->dispatch($command2);
        $this->commandBus->dispatch($command3);

        $this->assertEquals($this->commandBus->getRecordedCommands(), [$command2, $command3]);
    }
}
```

## File: `test/Broadway/Domain/DateTimeTest.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

namespace Broadway\Domain;

use PHPUnit\Framework\TestCase;

class DateTimeTest extends TestCase
{
    /**
     * @test
     */
    public function it_converts_back_and_forth()
    {
        $string = '2014-03-12T14:17:19.176169+00:00';
        $dateTime = DateTime::fromString($string);

        $this->assertEquals($string, $dateTime->toString());
    }

    /**
     * @test
     */
    public function it_creates_now()
    {
        $this->assertInstanceOf('Broadway\Domain\DateTime', DateTime::now());
    }

    /**
     * @test
     *
     * @dataProvider provideDatesAndIntervals
     */
    public function it_adds_intervals($dateTime, $interval, $expectedDateTime)
    {
        $dateTime = DateTime::fromString($dateTime)->add($interval);

        $this->assertEquals($expectedDateTime, $dateTime->toString());
    }

    /**
     * @test
     *
     * @dataProvider provideDatesAndIntervals
     */
    public function it_subtracts_intervals($expectedDateTime, $interval, $dateTime)
    {
        $dateTime = DateTime::fromString($dateTime)->sub($interval);

        $this->assertEquals($expectedDateTime, $dateTime->toString());
    }

    /**
     * @test
     */
    public function it_returns_a_new_instance_when_adding_interval()
    {
        $dateTime = DateTime::fromString('2015-03-14T00:00:00.000000+00:00');
        $newDateTime = $dateTime->add('PT0S');

        $this->assertNotSame($newDateTime, $dateTime);
    }

    /**
     * @test
     *
     * @dataProvider provideDateDiffs
     */
    public function it_diffs2_dates($date1, $date2, $expectedDiff)
    {
        $diff = DateTime::fromString($date1)->diff(DateTime::fromString($date2));

        $this->assertEquals($expectedDiff['ymdhis'], $diff->format('%y%m%d%h%i%s'));
        $this->assertEquals($expectedDiff['days'], $diff->days, '"days" is incorrect');
        $this->assertEquals($expectedDiff['invert'], $diff->invert, '"invert" is incorrect');
    }

    /**
     * @test
     */
    public function it_compares2_dates()
    {
        $this->assertTrue(DateTime::fromString('2014-01-01T01:01:01.123456+0000')->equals(DateTime::fromString('2014-01-01T01:01:01.123456+0000')));  // exact the same
        $this->assertTrue(DateTime::fromString('2014-01-01T01:01:01.123456+02:00')->equals(DateTime::fromString('2014-01-01T01:01:01.123456+0200'))); // different TimeZone format
        $this->assertTrue(DateTime::fromString('2014-01-01T13:37:42.000000+0000')->equals(DateTime::fromString('2014-01-01T13:37:42+0000')));         // with and without milliseconds
    }

    /**
     * @test
     *
     * @dataProvider provideGreaterThanDates
     */
    public function it_returns_if_a_date_is_gt_another_date($date1, $date2, $bool)
    {
        $this->assertSame($bool, DateTime::fromString($date1)->comesAfter(DateTime::fromString($date2)));
    }

    /**
     * @test
     */
    public function it_returns_the_native_date_time_object()
    {
        $this->assertInstanceOf(\DateTimeImmutable::class, DateTime::now()->toNative());
    }

    public function provideDatesAndIntervals()
    {
        return [
            ['2015-03-14T00:00:00.000000+00:00', 'P6W',            '2015-04-25T00:00:00.000000+00:00'],
            ['2000-01-01T00:00:00.000000+00:00', 'P7Y5M4DT4H3M2S', '2007-06-05T04:03:02.000000+00:00'],
        ];
    }

    /**
     * @test
     *
     * @dataProvider provideBeginningOfWeek
     */
    public function it_converts_to_the_beginning_of_week($dateTime, $expectedBeginningOfWeek)
    {
        $beginningOfWeek = DateTime::fromString($dateTime)->toBeginningOfWeek();

        $this->assertEquals($expectedBeginningOfWeek, $beginningOfWeek->toString());
    }

    public function provideBeginningOfWeek()
    {
        return [
            ['2015-03-14T00:00:00.000000+00:00', '2015-03-09T00:00:00.000000+00:00'],
            ['2015-03-09T00:00:00.000000+00:00', '2015-03-09T00:00:00.000000+00:00'],
            ['2015-03-15T23:59:59.000000+00:00', '2015-03-09T00:00:00.000000+00:00'],
        ];
    }

    public function provideDateDiffs()
    {
        return [
            ['2014-04-22T13:37:42.123456+02:00', '2014-04-23T13:37:42.123456+02:00', ['ymdhis' => '001000', 'days' => 1,  'invert' => 0]],
            ['2014-04-22T13:37:42.123456+02:00', '2014-05-24T13:37:42.123456+02:00', ['ymdhis' => '012000', 'days' => 32, 'invert' => 0]],
            ['2014-04-22T13:37:42.123456+00:00', '2014-04-22T13:37:42.123456+02:00', ['ymdhis' => '000200', 'days' => 0,  'invert' => 1]],
        ];
    }

    public function provideGreaterThanDates()
    {
        return [
            ['2014-05-01T12:00:00.000000+00:00', '2014-05-01T12:00:00.000000+00:00', false], // equal
            ['2014-04-22T13:37:42.123456+02:00', '2014-04-22T13:37:42.123456+00:00', false], // timezone
            ['2014-04-22T13:37:42.123456+00:00', '2014-04-22T12:37:42.123456+00:00', true],  // time
            ['2014-04-21T13:37:42.123456+00:00', '2014-04-22T13:37:42.123456+00:00', false],  // date
        ];
    }
}
```

## File: `test/Broadway/Domain/DomainEventStreamTest.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

namespace Broadway\Domain;

use PHPUnit\Framework\TestCase;

class DomainEventStreamTest extends TestCase
{
    /**
     * @test
     */
    public function it_returns_all_events_when_traversing()
    {
        $expectedEvents = ['event1', 'event2', 'event42'];
        $domainEventStream = new DomainEventStream($expectedEvents);

        $events = [];
        foreach ($domainEventStream as $event) {
            $events[] = $event;
        }

        $this->assertEquals($expectedEvents, $events);
    }
}
```

## File: `test/Broadway/Domain/DomainMessageTest.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

namespace Broadway\Domain;

use PHPUnit\Framework\TestCase;

class DomainMessageTest extends TestCase
{
    /**
     * @test
     */
    public function it_has_getters()
    {
        $id = 'Hi thur';
        $payload = new SomeEvent();
        $playhead = 15;
        $metadata = new Metadata(['meta']);
        $type = 'Broadway.Domain.SomeEvent';

        $domainMessage = DomainMessage::recordNow($id, $playhead, $metadata, $payload);

        $this->assertEquals($id, $domainMessage->getId());
        $this->assertEquals($payload, $domainMessage->getPayload());
        $this->assertEquals($playhead, $domainMessage->getPlayhead());
        $this->assertEquals($metadata, $domainMessage->getMetadata());
        $this->assertEquals($metadata, $domainMessage->getMetadata());
        $this->assertEquals($type, $domainMessage->getType());
    }

    /**
     * @test
     */
    public function it_returns_a_new_instance_with_more_metadata_on_and_metadata()
    {
        $domainMessage = DomainMessage::recordNow('id', 42, new Metadata(), 'payload');

        $this->assertNotSame($domainMessage, $domainMessage->andMetadata(Metadata::kv('foo', 42)));
    }

    /**
     * @test
     */
    public function it_keeps_all_data_the_same_expect_metadata_on_and_metadata()
    {
        $domainMessage = DomainMessage::recordNow('id', 42, new Metadata(), 'payload');

        $newMessage = $domainMessage->andMetadata(Metadata::kv('foo', 42));

        $this->assertSame($domainMessage->getId(), $newMessage->getId());
        $this->assertSame($domainMessage->getPlayhead(), $newMessage->getPlayhead());
        $this->assertSame($domainMessage->getPayload(), $newMessage->getPayload());
        $this->assertSame($domainMessage->getRecordedOn(), $newMessage->getRecordedOn());

        $this->assertNotSame($domainMessage->getMetadata(), $newMessage->getMetadata());
    }

    /**
     * @test
     */
    public function it_merges_the_metadata_instances_on_and_metadata()
    {
        $domainMessage = DomainMessage::recordNow('id', 42, Metadata::kv('bar', 1337), 'payload');

        $newMessage = $domainMessage->andMetadata(Metadata::kv('foo', 42));

        $expected = new Metadata(['bar' => 1337, 'foo' => 42]);
        $this->assertEquals($expected, $newMessage->getMetadata());
    }
}

class SomeEvent
{
}
```

## File: `test/Broadway/Domain/MetadataTest.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

namespace Broadway\Domain;

use PHPUnit\Framework\TestCase;

class MetadataTest extends TestCase
{
    /**
     * @test
     */
    public function it_contains_values_from_both_instances_after_merge()
    {
        $m1 = new Metadata(['foo' => 42]);
        $m2 = new Metadata(['bar' => 1337]);

        $expected = new Metadata(['foo' => 42, 'bar' => 1337]);
        $this->assertEquals($expected, $m1->merge($m2));
    }

    /**
     * @test
     */
    public function it_overrides_values_with_data_from_other_instance_on_merge()
    {
        $m1 = new Metadata(['foo' => 42]);
        $m2 = new Metadata(['foo' => 1337]);

        $expected = new Metadata(['foo' => 1337]);
        $this->assertEquals($expected, $m1->merge($m2));
    }

    /**
     * @test
     */
    public function it_constructs_an_instance_containing_the_key_and_value()
    {
        $m1 = Metadata::kv('foo', 42);

        $expected = new Metadata(['foo' => 42]);
        $this->assertEquals($expected, $m1);
    }

    /**
     * @test
     */
    public function it_returns_all_values()
    {
        $m1 = new Metadata(['foo' => 42, 'bar' => 1337]);

        $expected = ['foo' => 42, 'bar' => 1337];
        $this->assertEquals($expected, $m1->all());
    }

    /**
     * @test
     */
    public function it_returns_null_when_get_contains_unset_key()
    {
        $m1 = new Metadata(['foo' => 42]);

        $this->assertNull($m1->get('bar'));
    }

    /**
     * @test
     */
    public function it_returns_the_value_of_a_key_with_get()
    {
        $m1 = new Metadata(['foo' => 42]);

        $expected = 42;
        $this->assertEquals($expected, $m1->get('foo'));
    }
}
```

## File: `test/Broadway/EventDispatcher/EventDispatcherTest.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

namespace Broadway\EventDispatcher;

use PHPUnit\Framework\TestCase;

class EventDispatcherTest extends TestCase
{
    /**
     * @var CallableEventDispatcher
     */
    private $dispatcher;

    /**
     * @var TracableEventListener
     */
    private $listener1;

    /**
     * @var TracableEventListener
     */
    private $listener2;

    protected function setUp(): void
    {
        $this->dispatcher = new CallableEventDispatcher();
        $this->listener1 = new TracableEventListener();
        $this->listener2 = new TracableEventListener();

        $this->assertFalse($this->listener1->isCalled());
        $this->assertFalse($this->listener2->isCalled());
    }

    /**
     * @test
     */
    public function it_calls_the_subscribed_listeners()
    {
        $this->dispatcher->addListener('event', [$this->listener1, 'handleEvent']);
        $this->dispatcher->addListener('event', [$this->listener2, 'handleEvent']);

        $this->dispatcher->dispatch('event', ['value1', 'value2']);

        $this->assertTrue($this->listener1->isCalled());
        $this->assertTrue($this->listener2->isCalled());
    }

    /**
     * @test
     */
    public function it_only_calls_the_listener_subscribed_to_a_given_event()
    {
        $this->dispatcher->addListener('event1', [$this->listener1, 'handleEvent']);
        $this->dispatcher->addListener('event2', [$this->listener2, 'handleEvent']);

        $this->dispatcher->dispatch('event1', ['value1', 'value2']);

        $this->assertTrue($this->listener1->isCalled());
        $this->assertFalse($this->listener2->isCalled());
    }
}

class TracableEventListener
{
    private $isCalled = false;

    public function isCalled()
    {
        return $this->isCalled;
    }

    public function handleEvent($value1, $value2)
    {
        $this->isCalled = true;
    }
}
```

## File: `test/Broadway/EventHandling/ReliableEventBusTest.php`
```php
<?php

declare(strict_types=1);

namespace Vonq\Webshop\Tests\Broadway\EventHandling;

use Broadway\Domain\DomainEventStream;
use Broadway\Domain\DomainMessage;
use Broadway\Domain\Metadata;
use Broadway\EventHandling\EventListener;
use Broadway\EventHandling\ReliableEventBus;
use Monolog\Handler\TestHandler;
use Monolog\Logger;
use PHPUnit\Framework\MockObject\MockObject;
use PHPUnit\Framework\TestCase;
use Psr\Log\LoggerInterface;

class ReliableEventBusTest extends TestCase
{
    /**
     * @var ReliableEventBus
     */
    private $eventBus;

    /** @var LoggerInterface */
    private $logger;

    /** @var TestHandler */
    private $testHandler;

    protected function setUp(): void
    {
        $this->logger = new Logger('main');
        $this->testHandler = new TestHandler();
        $this->logger->pushHandler($this->testHandler);

        $this->eventBus = new ReliableEventBus($this->logger);
    }

    /**
     * @test
     */
    public function it_should_process_the_next_handle_when_a_handler_fails()
    {
        $domainMessage = $this->createDomainMessage([]);

        $domainEventStream = new DomainEventStream([$domainMessage]);

        $eventListener1 = $this->createEventListenerMock();
        $eventListener1
            ->expects($this->at(0))
            ->method('handle')
            ->willThrowException(new \Exception());

        $eventListener2 = $this->prophesize(EventListener::class);
        $eventListener2->handle($domainMessage)->shouldBeCalledOnce();

        $this->eventBus->subscribe($eventListener1);
        $this->eventBus->subscribe($eventListener2->reveal());
        $this->eventBus->publish($domainEventStream);

        $this->assertTrue($this->testHandler->hasErrorThatContains(sprintf('[Event LISTENER]: %s', get_class($eventListener1))));
    }

    /**
     * @test
     */
    public function it_subscribes_an_event_listener()
    {
        $domainMessage = $this->createDomainMessage(['foo' => 'bar']);

        $eventListener = $this->createEventListenerMock();
        $eventListener
            ->expects($this->once())
            ->method('handle')
            ->with($domainMessage);

        $this->eventBus->subscribe($eventListener);

        $this->eventBus->publish(new DomainEventStream([$domainMessage]));
    }

    /**
     * @test
     */
    public function it_publishes_events_to_subscribed_event_listeners()
    {
        $domainMessage1 = $this->createDomainMessage([]);
        $domainMessage2 = $this->createDomainMessage([]);

        $domainEventStream = new DomainEventStream([$domainMessage1, $domainMessage2]);

        $eventListener1 = $this->createEventListenerMock();
        $eventListener1
            ->expects($this->at(0))
            ->method('handle')
            ->with($domainMessage1);
        $eventListener1
            ->expects($this->at(1))
            ->method('handle')
            ->with($domainMessage2);

        $eventListener2 = $this->createEventListenerMock();
        $eventListener2
            ->expects($this->at(0))
            ->method('handle')
            ->with($domainMessage1);
        $eventListener2
            ->expects($this->at(1))
            ->method('handle')
            ->with($domainMessage2);

        $this->eventBus->subscribe($eventListener1);
        $this->eventBus->subscribe($eventListener2);
        $this->eventBus->publish($domainEventStream);
    }

    /**
     * @test
     */
    public function it_does_not_dispatch_new_events_before_all_listeners_have_run()
    {
        $domainMessage1 = $this->createDomainMessage(['foo' => 'bar']);
        $domainMessage2 = $this->createDomainMessage(['foo' => 'bas']);

        $domainEventStream = new DomainEventStream([$domainMessage1]);

        $eventListener1 = new SimpleEventBusTestListener($this->eventBus, new DomainEventStream([$domainMessage2]));

        $eventListener2 = $this->createEventListenerMock();
        $eventListener2
            ->expects($this->at(0))
            ->method('handle')
            ->with($domainMessage1);
        $eventListener2
            ->expects($this->at(1))
            ->method('handle')
            ->with($domainMessage2);

        $this->eventBus->subscribe($eventListener1);
        $this->eventBus->subscribe($eventListener2);
        $this->eventBus->publish($domainEventStream);
    }

    /**
     * @test
     */
    public function it_should_still_publish_events_after_exception()
    {
        $domainMessage1 = $this->createDomainMessage(['foo' => 'bar']);
        $domainMessage2 = $this->createDomainMessage(['foo' => 'bas']);

        $domainEventStream1 = new DomainEventStream([$domainMessage1]);
        $domainEventStream2 = new DomainEventStream([$domainMessage2]);

        $eventListener = $this->createEventListenerMock();
        $eventListener
            ->expects($this->at(0))
            ->method('handle')
            ->with($domainMessage1)
            ->will($this->throwException(new \Exception('I failed.')));

        $eventListener
            ->expects($this->at(1))
            ->method('handle')
            ->with($domainMessage2);

        $this->eventBus->subscribe($eventListener);

        $this->eventBus->publish($domainEventStream1);
        $this->eventBus->publish($domainEventStream2);
    }

    private function createEventListenerMock(): MockObject
    {
        return $this->createMock(EventListener::class);
    }

    private function createDomainMessage($payload)
    {
        return DomainMessage::recordNow(1, 1, new Metadata([]), new SimpleEventBusTestEvent($payload));
    }
}

class SimpleEventBusTestEvent
{
    public $data;

    public function __construct($data)
    {
        $this->data = $data;
    }
}

class SimpleEventBusTestListener implements EventListener
{
    private $eventBus;
    private $handled = false;
    private $publishableStream;

    public function __construct($eventBus, $publishableStream)
    {
        $this->eventBus = $eventBus;
        $this->publishableStream = $publishableStream;
    }

    public function handle(DomainMessage $domainMessage): void
    {
        if (!$this->handled) {
            $this->eventBus->publish($this->publishableStream);
            $this->handled = true;
        }
    }
}
```

## File: `test/Broadway/EventHandling/SimpleEventBusTest.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

namespace Broadway\EventHandling;

use Broadway\Domain\DomainEventStream;
use Broadway\Domain\DomainMessage;
use Broadway\Domain\Metadata;
use PHPUnit\Framework\MockObject\MockObject;
use PHPUnit\Framework\TestCase;

class SimpleEventBusTest extends TestCase
{
    /**
     * @var SimpleEventBus
     */
    private $eventBus;

    protected function setUp(): void
    {
        $this->eventBus = new SimpleEventBus();
    }

    /**
     * @test
     */
    public function it_subscribes_an_event_listener()
    {
        $domainMessage = $this->createDomainMessage(['foo' => 'bar']);

        $eventListener = $this->createEventListenerMock();
        $eventListener
            ->expects($this->once())
            ->method('handle')
            ->with($domainMessage);

        $this->eventBus->subscribe($eventListener);

        $this->eventBus->publish(new DomainEventStream([$domainMessage]));
    }

    /**
     * @test
     */
    public function it_publishes_events_to_subscribed_event_listeners()
    {
        $domainMessage1 = $this->createDomainMessage([]);
        $domainMessage2 = $this->createDomainMessage([]);

        $domainEventStream = new DomainEventStream([$domainMessage1, $domainMessage2]);

        $eventListener1 = $this->createEventListenerMock();
        $eventListener1
            ->expects($this->at(0))
            ->method('handle')
            ->with($domainMessage1);
        $eventListener1
            ->expects($this->at(1))
            ->method('handle')
            ->with($domainMessage2);

        $eventListener2 = $this->createEventListenerMock();
        $eventListener2
            ->expects($this->at(0))
            ->method('handle')
            ->with($domainMessage1);
        $eventListener2
            ->expects($this->at(1))
            ->method('handle')
            ->with($domainMessage2);

        $this->eventBus->subscribe($eventListener1);
        $this->eventBus->subscribe($eventListener2);
        $this->eventBus->publish($domainEventStream);
    }

    /**
     * @test
     */
    public function it_does_not_dispatch_new_events_before_all_listeners_have_run()
    {
        $domainMessage1 = $this->createDomainMessage(['foo' => 'bar']);
        $domainMessage2 = $this->createDomainMessage(['foo' => 'bas']);

        $domainEventStream = new DomainEventStream([$domainMessage1]);

        $eventListener1 = new SimpleEventBusTestListener($this->eventBus, new DomainEventStream([$domainMessage2]));

        $eventListener2 = $this->createEventListenerMock();
        $eventListener2
            ->expects($this->at(0))
            ->method('handle')
            ->with($domainMessage1);
        $eventListener2
            ->expects($this->at(1))
            ->method('handle')
            ->with($domainMessage2);

        $this->eventBus->subscribe($eventListener1);
        $this->eventBus->subscribe($eventListener2);
        $this->eventBus->publish($domainEventStream);
    }

    /**
     * @test
     */
    public function it_should_still_publish_events_after_exception()
    {
        $domainMessage1 = $this->createDomainMessage(['foo' => 'bar']);
        $domainMessage2 = $this->createDomainMessage(['foo' => 'bas']);

        $domainEventStream1 = new DomainEventStream([$domainMessage1]);
        $domainEventStream2 = new DomainEventStream([$domainMessage2]);

        $eventListener = $this->createEventListenerMock();
        $eventListener
            ->expects($this->at(0))
            ->method('handle')
            ->with($domainMessage1)
            ->will($this->throwException(new \Exception('I failed.')));

        $eventListener
            ->expects($this->at(1))
            ->method('handle')
            ->with($domainMessage2);

        $this->eventBus->subscribe($eventListener);

        try {
            $this->eventBus->publish($domainEventStream1);
        } catch (\Exception $e) {
            $this->assertEquals('I failed.', $e->getMessage());
        }

        $this->eventBus->publish($domainEventStream2);
    }

    private function createEventListenerMock(): MockObject
    {
        return $this->createMock(EventListener::class);
    }

    private function createDomainMessage($payload)
    {
        return DomainMessage::recordNow(1, 1, new Metadata([]), new SimpleEventBusTestEvent($payload));
    }
}

class SimpleEventBusTestEvent
{
    public $data;

    public function __construct($data)
    {
        $this->data = $data;
    }
}

class SimpleEventBusTestListener implements EventListener
{
    private $eventBus;
    private $handled = false;
    private $publishableStream;

    public function __construct($eventBus, $publishableStream)
    {
        $this->eventBus = $eventBus;
        $this->publishableStream = $publishableStream;
    }

    public function handle(DomainMessage $domainMessage): void
    {
        if (!$this->handled) {
            $this->eventBus->publish($this->publishableStream);
            $this->handled = true;
        }
    }
}
```

## File: `test/Broadway/EventSourcing/AbstractEventSourcingRepositoryTest.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

namespace Broadway\EventSourcing;

use Assert\InvalidArgumentException;
use Broadway\Domain\AggregateRoot;
use Broadway\Domain\DomainEventStream;
use Broadway\Domain\DomainMessage;
use Broadway\Domain\Metadata;
use Broadway\EventHandling\SimpleEventBus;
use Broadway\EventHandling\TraceableEventBus;
use Broadway\EventSourcing\AggregateFactory\PublicConstructorAggregateFactory;
use Broadway\EventSourcing\MetadataEnrichment\MetadataEnricher;
use Broadway\EventSourcing\MetadataEnrichment\MetadataEnrichingEventStreamDecorator;
use Broadway\EventStore\EventStore;
use Broadway\EventStore\InMemoryEventStore;
use Broadway\EventStore\TraceableEventStore;
use Broadway\ReadModel\Projector;
use Broadway\Repository\AggregateNotFoundException;
use PHPUnit\Framework\TestCase;

abstract class AbstractEventSourcingRepositoryTest extends TestCase
{
    /** @var TraceableEventBus */
    protected $eventBus;

    /** @var TraceableEventStoreDecorator */
    protected $eventStreamDecorator;

    /** @var EventStore */
    protected $eventStore;

    /** @var EventSourcingRepository */
    protected $repository;

    protected function setUp(): void
    {
        $this->eventStore = new TraceableEventStore(new InMemoryEventStore());
        $this->eventStore->trace();

        $this->eventBus = new TraceableEventBus(new SimpleEventBus());
        $this->eventBus->trace();

        $this->eventStreamDecorator = new TraceableEventStoreDecorator();
        $this->eventStreamDecorator->trace();

        $this->repository = $this->createEventSourcingRepository($this->eventStore, $this->eventBus, [$this->eventStreamDecorator]);
    }

    /**
     * @test
     *
     * @dataProvider objectsNotOfConfiguredClass
     */
    public function it_throws_an_exception_when_adding_an_aggregate_that_is_not_of_the_configured_class($aggregate)
    {
        $this->expectException(InvalidArgumentException::class);

        $this->repository->save($aggregate);
    }

    public function objectsNotOfConfiguredClass()
    {
        return [
            [new TestAggregate()],
            [new AnotherTestEventSourcedAggregate()],
        ];
    }

    /**
     * @test
     */
    public function it_adds_an_aggregate_root()
    {
        $aggregate = $this->createAggregate();
        $aggregate->apply(new DidNumberEvent(42));
        $aggregate->apply(new DidNumberEvent(1337));

        $this->repository->save($aggregate);

        $expected = [new DidNumberEvent(42), new DidNumberEvent(1337)];
        $this->assertEquals($expected, $this->eventStore->getEvents());
        $this->assertEquals($expected, $this->eventBus->getEvents());
    }

    /**
     * @test
     */
    public function it_loads_an_aggregate()
    {
        $this->eventStore->append(42, new DomainEventStream([
            DomainMessage::recordNow(42, 0, new Metadata([]), new DidNumberEvent(1337)),
        ]));

        $aggregate = $this->repository->load(42);

        $expectedAggregate = $this->createAggregate();
        $expectedAggregate->apply(new DidNumberEvent(1337));
        $expectedAggregate->getUncommittedEvents();

        $this->assertEquals($expectedAggregate, $aggregate);
    }

    /**
     * @test
     */
    public function it_throws_an_exception_if_aggregate_was_not_found()
    {
        $this->expectException(AggregateNotFoundException::class);

        $this->repository->load('does-not-exist');
    }

    /**
     * @test
     */
    public function it_calls_the_event_stream_decorators()
    {
        $aggregate = $this->createAggregate();
        $aggregate->apply(new DidNumberEvent(42));

        $this->repository->save($aggregate);

        $this->assertTrue($this->eventStreamDecorator->isCalled());
    }

    /**
     * @test
     */
    public function it_calls_the_event_stream_decorators_with_the_correct_arguments()
    {
        $event = new DidNumberEvent(42);

        $aggregate = $this->createAggregate();
        $aggregate->apply($event);

        $this->repository->save($aggregate);

        $lastCall = $this->eventStreamDecorator->getLastCall();

        $this->assertEquals($aggregate->getAggregateRootId(), $lastCall['aggregateIdentifier']);
        $this->assertEquals(get_class($aggregate), $lastCall['aggregateType']);

        $events = iterator_to_array($lastCall['eventStream']);
        $this->assertCount(1, $events);

        $this->assertSame($event, $events[0]->getPayload());
    }

    /**
     * @test
     */
    public function it_publishes_decorated_events()
    {
        $projector = new TestMetadataPublishedProjector();
        $this->eventBus->subscribe($projector);

        $repository = new EventSourcingRepository(
            $this->eventStore,
            $this->eventBus,
            get_class($this->createAggregate()),
            new PublicConstructorAggregateFactory(),
            [new MetadataEnrichingEventStreamDecorator([new TestDecorationMetadataEnricher()])]
        );

        $aggregate = $this->createAggregate();
        $aggregate->apply(new DidNumberEvent(42));
        $repository->save($aggregate);

        $metadata = $projector->getMetadata();
        $data = $metadata->serialize();

        $this->assertArrayHasKey('decoration_test', $data);
        $this->assertEquals('I am a decorated test', $data['decoration_test']);
    }

    /**
     * @return EventSourcingRepository
     */
    abstract protected function createEventSourcingRepository(TraceableEventStore $eventStore, TraceableEventBus $eventBus, array $eventStreamDecorators);

    /**
     * @return EventSourcedAggregateRoot
     */
    abstract protected function createAggregate();
}

class DidNumberEvent
{
    public $number;

    public function __construct($number)
    {
        $this->number = $number;
    }
}

class AnotherTestEventSourcedAggregate extends EventSourcedAggregateRoot
{
    public function getAggregateRootId(): string
    {
        return '1337';
    }
}

class TestAggregate implements AggregateRoot
{
    public function getAggregateRootId(): string
    {
        return '42';
    }

    public function getUncommittedEvents(): DomainEventStream
    {
        return new DomainEventStream([]);
    }
}

class TraceableEventstoreDecorator implements EventStreamDecorator
{
    private $tracing = false;
    private $calls;

    public function decorateForWrite(string $aggregateType, string $aggregateIdentifier, DomainEventStream $eventStream): DomainEventStream
    {
        if ($this->tracing) {
            $this->calls[] = ['aggregateType' => $aggregateType, 'aggregateIdentifier' => $aggregateIdentifier, 'eventStream' => $eventStream];
        }

        return $eventStream;
    }

    public function trace()
    {
        $this->tracing = true;
    }

    public function isCalled()
    {
        return count($this->calls) > 0;
    }

    public function getLastCall()
    {
        if (!$this->isCalled()) {
            throw new \RuntimeException('was never called');
        }

        return $this->calls[count($this->calls) - 1];
    }
}

class TestDecorationMetadataEnricher implements MetadataEnricher
{
    public function enrich(Metadata $metadata): Metadata
    {
        return new Metadata(['decoration_test' => 'I am a decorated test']);
    }
}

class TestMetadataPublishedProjector extends Projector
{
    private $metadata;

    public function applyDidNumberEvent(DidNumberEvent $event, DomainMessage $domainMessage)
    {
        $this->metadata = $domainMessage->getMetadata();
    }

    /**
     * @return Metadata
     */
    public function getMetadata()
    {
        return $this->metadata;
    }
}
```

## File: `test/Broadway/EventSourcing/EventSourcedAggregateRootTest.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

namespace Broadway\EventSourcing;

use Broadway\Domain\DomainEventStream;
use Broadway\Domain\DomainMessage;
use Broadway\Domain\Metadata;
use PHPUnit\Framework\TestCase;

class EventSourcedAggregateRootTest extends TestCase
{
    /**
     * @test
     */
    public function it_applies_using_an_incrementing_playhead()
    {
        $aggregateRoot = new MyTestAggregateRoot();
        $aggregateRoot->apply(new AggregateEvent());
        $aggregateRoot->apply(new AggregateEvent());
        $eventStream = $aggregateRoot->getUncommittedEvents();

        $i = 0;
        foreach ($eventStream as $domainMessage) {
            $this->assertEquals($i, $domainMessage->getPlayhead());
            ++$i;
        }
        $this->assertEquals(2, $i);
    }

    /**
     * @test
     */
    public function it_sets_internal_playhead_when_initializing()
    {
        $aggregateRoot = new MyTestAggregateRoot();
        $aggregateRoot->initializeState($this->toDomainEventStream([new AggregateEvent()]));

        $aggregateRoot->apply(new AggregateEvent());

        $eventStream = $aggregateRoot->getUncommittedEvents();
        foreach ($eventStream as $domainMessage) {
            $this->assertEquals(1, $domainMessage->getPlayhead());
        }
    }

    /**
     * @test
     */
    public function it_calls_apply_for_specific_events()
    {
        $aggregateRoot = new MyTestAggregateRoot();
        $aggregateRoot->initializeState($this->toDomainEventStream([new AggregateEvent()]));

        $this->assertTrue($aggregateRoot->isCalled);
    }

    private function toDomainEventStream(array $events)
    {
        $messages = [];
        $playhead = -1;
        foreach ($events as $event) {
            ++$playhead;
            $messages[] = DomainMessage::recordNow(1, $playhead, new Metadata([]), $event);
        }

        return new DomainEventStream($messages);
    }
}

class MyTestAggregateRoot extends EventSourcedAggregateRoot
{
    public $isCalled = false;

    public function getAggregateRootId(): string
    {
        return 'y0l0';
    }

    public function applyAggregateEvent($event)
    {
        $this->isCalled = true;
    }
}

class AggregateEvent
{
}
```

## File: `test/Broadway/EventSourcing/EventSourcingRepositoryTest.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

namespace Broadway\EventSourcing;

use Assert\InvalidArgumentException;
use Broadway\Domain\DomainEventStream;
use Broadway\Domain\DomainMessage;
use Broadway\Domain\Metadata;
use Broadway\EventHandling\TraceableEventBus;
use Broadway\EventSourcing\AggregateFactory\NamedConstructorAggregateFactory;
use Broadway\EventSourcing\AggregateFactory\PublicConstructorAggregateFactory;
use Broadway\EventStore\TraceableEventStore;

class EventSourcingRepositoryTest extends AbstractEventSourcingRepositoryTest
{
    protected function createEventSourcingRepository(TraceableEventStore $eventStore, TraceableEventBus $eventBus, array $eventStreamDecorators)
    {
        return new EventSourcingRepository($eventStore, $eventBus, TestEventSourcedAggregate::class, new PublicConstructorAggregateFactory(), $eventStreamDecorators);
    }

    protected function createAggregate()
    {
        return new TestEventSourcedAggregate();
    }

    /**
     * @test
     */
    public function it_throws_an_exception_when_instantiated_with_a_class_that_is_not_an_event_sourced_aggregate_root()
    {
        $this->expectException(InvalidArgumentException::class);

        new EventSourcingRepository($this->eventStore, $this->eventBus, stdClass::class, new PublicConstructorAggregateFactory());
    }

    /**
     * @test
     */
    public function it_can_use_an_alternative_aggregate_factory_to_create_the_aggregate()
    {
        // make sure events exist in the event store
        $id = 'y0l0';
        $this->eventStore->append($id, new DomainEventStream([
            DomainMessage::recordNow(42, 0, new Metadata([]), new DidEvent()),
        ]));

        $repository = $this->repositoryWithStaticAggregateFactory();
        $aggregate = $repository->load('y0l0');
        $this->assertTrue($aggregate->constructorWasCalled);
        $this->assertEquals($aggregate->instantiatedThrough, 'instantiateForReconstitution');

        $repository = $this->repositoryWithStaticAggregateFactory('justAnotherInstantiation');
        $aggregate = $repository->load('y0l0');
        $this->assertTrue($aggregate->constructorWasCalled);
        $this->assertEquals($aggregate->instantiatedThrough, 'justAnotherInstantiation');
    }

    /**
     * @test
     */
    public function it_throws_an_exception_if_the_static_method_does_not_exist()
    {
        // make sure events exist in the event store
        $id = 'y0l0';
        $this->eventStore->append($id, new DomainEventStream([
            DomainMessage::recordNow(42, 0, new Metadata([]), new DidEvent()),
        ]));

        $this->expectException(InvalidArgumentException::class);

        $repository = $this->repositoryWithStaticAggregateFactory('someUnknownStaticmethod');
        $repository->load('y0l0');
    }

    protected function repositoryWithStaticAggregateFactory($staticMethod = null)
    {
        if (is_null($staticMethod)) {
            $staticFactory = new NamedConstructorAggregateFactory();
        } else {
            $staticFactory = new NamedConstructorAggregateFactory($staticMethod);
        }

        return new EventSourcingRepository(
            $this->eventStore,
            $this->eventBus,
            TestEventSourcedAggregateWithStaticConstructor::class,
            $staticFactory,
            []
        );
    }
}

class TestEventSourcedAggregate extends EventSourcedAggregateRoot
{
    public $numbers;

    public function getAggregateRootId(): string
    {
        return '42';
    }

    protected function applyDidNumberEvent($event)
    {
        $this->numbers[] = $event->number;
    }
}

class TestEventSourcedAggregateWithStaticConstructor extends EventSourcedAggregateRoot
{
    public $constructorWasCalled = false;
    public $instantiatedThrough;

    private function __construct($instantiatedThrough)
    {
        $this->constructorWasCalled = true;
        $this->instantiatedThrough = $instantiatedThrough;
    }

    public function getAggregateRootId(): string
    {
        return 'y0l0';
    }

    public static function instantiateForReconstitution()
    {
        return new self(__FUNCTION__);
    }

    public static function justAnotherInstantiation()
    {
        return new self(__FUNCTION__);
    }
}

class DidEvent
{
}
```

## File: `test/Broadway/EventSourcing/SimpleEventSourcedEntityTest.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

namespace Broadway\EventSourcing;

use PHPUnit\Framework\TestCase;

class SimpleEventSourcedEntityTest extends TestCase
{
    /**
     * @test
     */
    public function it_handles_events_recursively()
    {
        $aggregateRoot = new Aggregate();
        $child = new Entity();

        $aggregateRoot->addChildEntity($child);

        $mock = $this->getMockBuilder('Broadway\EventSourcing\Entity')
            ->setMethods(['handleRecursively'])
            ->getMock();

        $mock->expects($this->once())
            ->method('handleRecursively');

        $child->addChildEntity($mock);

        $aggregateRoot->doApply();
    }

    /**
     * @test
     */
    public function it_applies_events_to_aggregate_root()
    {
        $aggregateRoot = $this->getMockBuilder('Broadway\EventSourcing\Aggregate')
            ->setMethods(['apply'])
            ->getMock();

        $aggregateRoot->expects($this->once())
            ->method('apply');

        $child = new Entity();
        $grandChild = new Entity();

        $aggregateRoot->addChildEntity($child);

        $child->addChildEntity($grandChild);
        $aggregateRoot->doHandleRecursively();  // Initialize tree structure

        $grandChild->doApply();
    }

    /**
     * @test
     */
    public function it_can_only_have_one_root()
    {
        $root1 = new Aggregate();
        $root2 = new Aggregate();

        $entity = new Entity();

        $root1->addChildEntity($entity);
        $root2->addChildEntity($entity);

        $this->expectException(AggregateRootAlreadyRegisteredException::class);

        $root1->doHandleRecursively();
        $root2->doHandleRecursively();
    }
}

class Aggregate extends EventSourcedAggregateRoot
{
    private $children = [];

    protected function getChildEntities(): array
    {
        return $this->children;
    }

    public function addChildEntity($entity)
    {
        $this->children[] = $entity;
    }

    public function doApply()
    {
        $this->apply(new Event());
    }

    public function doHandleRecursively()
    {
        $this->handleRecursively(new Event());
    }

    public function getAggregateRootId(): string
    {
        return '42';
    }
}

class Entity extends SimpleEventSourcedEntity
{
    private $children = [];

    protected function getChildEntities(): array
    {
        return $this->children;
    }

    public function addChildEntity($entity)
    {
        $this->children[] = $entity;
    }

    protected function applyEvent($event)
    {
    }

    public function doApply()
    {
        $this->apply(new Event());
    }
}

class Event
{
}
```

## File: `test/Broadway/EventSourcing/AggregateFactory/ReflectionAggregateFactoryTest.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

namespace Broadway\EventSourcing\AggregateFactory;

use Broadway\Domain\DomainEventStream;
use Broadway\EventSourcing\EventSourcedAggregateRoot;
use PHPUnit\Framework\TestCase;

final class ReflectionAggregateFactoryTest extends TestCase
{
    /**
     * @var ReflectionAggregateFactory
     */
    private $factory;

    protected function setUp(): void
    {
        $this->factory = new ReflectionAggregateFactory();
    }

    /**
     * @test
     */
    public function it_creates_instance_of_aggregate_with_private_constructor()
    {
        $aggregate = $this->factory->create(
            TestAggregateWithPrivateConstructor::class,
            new DomainEventStream([])
        );

        $this->assertInstanceOf(TestAggregateWithPrivateConstructor::class, $aggregate);
    }

    /**
     * @test
     */
    public function it_creates_instance_of_aggregate_with_public_constructor()
    {
        $aggregate = $this->factory->create(
            TestAggregateWithPublicConstructor::class,
            new DomainEventStream([])
        );

        $this->assertInstanceOf(TestAggregateWithPublicConstructor::class, $aggregate);
    }

    /**
     * @test
     */
    public function it_does_not_handle_weird_classes()
    {
        $this->expectException(\LogicException::class);
        $this->expectExceptionMessage(sprintf('Impossible to initialize "%s"', \stdClass::class));

        $this->factory->create(\stdClass::class, new DomainEventStream([]));
    }
}

final class TestAggregateWithPrivateConstructor extends EventSourcedAggregateRoot
{
    private function __construct()
    {
    }

    public function getAggregateRootId(): string
    {
        return 'foo42';
    }
}

final class TestAggregateWithPublicConstructor extends EventSourcedAggregateRoot
{
    public function getAggregateRootId(): string
    {
        return 'foo42';
    }
}
```

## File: `test/Broadway/EventSourcing/MetadataEnrichment/MetadataEnrichingEventStreamDecoratorTest.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

namespace Broadway\EventSourcing\MetadataEnrichment;

use Broadway\Domain\DomainEventStream;
use Broadway\Domain\DomainMessage;
use Broadway\Domain\Metadata;
use PHPUnit\Framework\TestCase;

class MetadataEnrichingEventStreamDecoratorTest extends TestCase
{
    /**
     * @test
     */
    public function it_returns_the_original_event_stream_if_no_enrichers_are_registered()
    {
        $decorator = new MetadataEnrichingEventStreamDecorator();

        $eventStream = $this->createDomainEventStream();

        $newEventStream = $decorator->decorateForWrite('id', 'type', $eventStream);

        $this->assertSame($eventStream, $newEventStream);
    }

    /**
     * @test
     */
    public function it_calls_the_enricher_for_every_event()
    {
        $enricher = new TracableMetadataEnricher();
        $decorator = new MetadataEnrichingEventStreamDecorator([$enricher]);

        $eventStream = $this->createDomainEventStream();

        $newEventStream = $decorator->decorateForWrite('id', 'type', $eventStream);

        $this->assertEquals(2, $enricher->callCount());
    }

    /**
     * @test
     */
    public function it_returns_a_domain_eventstream_with_messages_with_extra_metadata()
    {
        $enricher = new TracableMetadataEnricher();
        $decorator = new MetadataEnrichingEventStreamDecorator([$enricher]);

        $eventStream = $this->createDomainEventStream();

        $newEventStream = $decorator->decorateForWrite('id', 'type', $eventStream);

        $messages = iterator_to_array($newEventStream);

        $this->assertCount(2, $messages);

        $expectedMetadata = new Metadata(['bar' => 1337, 'traced' => true]);

        foreach ($messages as $message) {
            $this->assertEquals($expectedMetadata, $message->getMetadata());
        }
    }

    /**
     * @test
     */
    public function it_calls_the_enricher_when_registered_later()
    {
        $constructorEnricher = new TracableMetadataEnricher();
        $newlyRegisteredEnricher = new TracableMetadataEnricher();
        $decorator = new MetadataEnrichingEventStreamDecorator([$constructorEnricher]);
        $decorator->registerEnricher($newlyRegisteredEnricher);

        $decorator->decorateForWrite('id', 'type', $this->createDomainEventStream());

        $this->assertEquals(2, $constructorEnricher->callCount());
        $this->assertEquals(2, $newlyRegisteredEnricher->callCount());
    }

    private function createDomainEventStream()
    {
        $m1 = DomainMessage::recordNow('id', 42, Metadata::kv('bar', 1337), 'payload');
        $m2 = DomainMessage::recordNow('id', 42, Metadata::kv('bar', 1337), 'payload');

        return new DomainEventStream([$m1, $m2]);
    }
}

class TracableMetadataEnricher implements MetadataEnricher
{
    private $calls;

    public function enrich(Metadata $metadata): Metadata
    {
        $this->calls[] = $metadata;

        return $metadata->merge(Metadata::kv('traced', true));
    }

    public function callCount(): int
    {
        return count($this->calls);
    }
}
```

## File: `test/Broadway/EventStore/ConflictResolvingEventStoreTest.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

namespace Broadway\EventStore;

use Broadway\Domain\DomainEventStream;
use Broadway\Domain\DomainMessage;
use Broadway\EventStore\ConcurrencyConflictResolver\ConcurrencyConflictResolver;
use Broadway\EventStore\Testing\EventStoreTest;
use PHPUnit\Framework\MockObject\MockObject;
use Prophecy\Argument;

class ConflictResolvingEventStoreTest extends EventStoreTest
{
    /** @var ConcurrencyConflictResolver|MockObject */
    protected $concurrencyResolver;

    protected function setUp(): void
    {
        $this->concurrencyResolver = $this->prophesize(ConcurrencyConflictResolver::class);
        $this->concurrencyResolver
            ->conflictsWith(Argument::type(DomainMessage::class), Argument::type(DomainMessage::class))
            ->willReturn(true);

        $this->eventStore = new ConcurrencyConflictResolvingEventStore(
            new InMemoryEventStore(), $this->concurrencyResolver->reveal());
    }

    /** @test */
    public function events_can_be_appended_although_playheads_conflict_if_events_are_independent()
    {
        $this->concurrencyResolver
            ->conflictsWith(Argument::type(DomainMessage::class), Argument::type(DomainMessage::class))
            ->willReturn(false);

        $domainMessage = $this->createDomainMessage(1, 0);
        $baseStream = new DomainEventStream([$domainMessage]);
        $this->eventStore->append(1, $baseStream);
        $appendedEventStream = new DomainEventStream([$domainMessage]);

        $this->eventStore->append(1, $appendedEventStream);

        $events = $this->eventStore->load(1);
        $this->assertCount(2, $events);
    }
}
```

## File: `test/Broadway/EventStore/InMemoryEventStoreTest.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

namespace Broadway\EventStore;

use Broadway\EventStore\Testing\EventStoreTest;

class InMemoryEventStoreTest extends EventStoreTest
{
    protected function setUp(): void
    {
        $this->eventStore = new InMemoryEventStore();
    }
}
```

## File: `test/Broadway/EventStore/ConcurrencyConflictResolver/BlacklistConcurrencyConflictResolverTest.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

namespace Broadway\EventStore\ConcurrencyConflictResolver;

class BlacklistConcurrencyConflictResolverTest extends ConcurrencyConflictResolverTest
{
    /** @var BlacklistConcurrencyConflictResolver */
    private $conflictResolver;

    protected function setUp(): void
    {
        $this->conflictResolver = new BlacklistConcurrencyConflictResolver();
    }

    /** @test */
    public function events_never_conflict_if_no_conflicting_events_are_registered()
    {
        $event = $this->createDomainMessage(1, 0, new Event());
        $this->assertFalse($this->conflictResolver->conflictsWith($event, $event));
    }

    /** @test */
    public function independent_events_do_not_conflict()
    {
        $event = $this->createDomainMessage(1, 0, new Event());
        $otherEvent = $this->createDomainMessage(1, 0, new OtherEvent());
        $this->conflictResolver->registerConflictingEvents(Event::class, Event::class);
        $this->assertTrue($this->conflictResolver->conflictsWith($event, $event));
        $this->assertFalse($this->conflictResolver->conflictsWith($event, $otherEvent));

        $this->conflictResolver->registerConflictingEvents(Event::class, OtherEvent::class);
        $this->assertTrue($this->conflictResolver->conflictsWith($otherEvent, $event));
        $this->assertTrue($this->conflictResolver->conflictsWith($event, $otherEvent));
    }
}
```

## File: `test/Broadway/EventStore/ConcurrencyConflictResolver/ConcurrencyConflictResolverTest.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

namespace Broadway\EventStore\ConcurrencyConflictResolver;

use Broadway\Domain\DateTime;
use Broadway\Domain\DomainMessage;
use Broadway\Domain\Metadata;
use PHPUnit\Framework\TestCase;

abstract class ConcurrencyConflictResolverTest extends TestCase
{
    protected function createDomainMessage($id, $playhead, $event)
    {
        return new DomainMessage($id, $playhead, new Metadata([]), $event, DateTime::now());
    }
}
```

## File: `test/Broadway/EventStore/ConcurrencyConflictResolver/Event.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

namespace Broadway\EventStore\ConcurrencyConflictResolver;

class Event
{
}
```

## File: `test/Broadway/EventStore/ConcurrencyConflictResolver/OtherEvent.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

namespace Broadway\EventStore\ConcurrencyConflictResolver;

class OtherEvent
{
}
```

## File: `test/Broadway/EventStore/ConcurrencyConflictResolver/WhitelistConcurrencyConflictResolverTest.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

namespace Broadway\EventStore\ConcurrencyConflictResolver;

class WhitelistConcurrencyConflictResolverTest extends ConcurrencyConflictResolverTest
{
    /** @var WhitelistConcurrencyConflictResolver */
    private $conflictResolver;

    protected function setUp(): void
    {
        $this->conflictResolver = new WhitelistConcurrencyConflictResolver();
    }

    /** @test */
    public function events_always_conflict_if_no_independent_events_are_registered()
    {
        $event = $this->createDomainMessage(1, 0, new Event());
        $this->assertTrue($this->conflictResolver->conflictsWith($event, $event));
    }

    /** @test */
    public function independent_events_do_not_conflict()
    {
        $event = $this->createDomainMessage(1, 0, new Event());
        $otherEvent = $this->createDomainMessage(1, 0, new OtherEvent());
        $this->conflictResolver->registerIndependentEvents(Event::class, Event::class);
        $this->assertFalse($this->conflictResolver->conflictsWith($event, $event));
        $this->assertTrue($this->conflictResolver->conflictsWith($event, $otherEvent));

        $this->conflictResolver->registerIndependentEvents(Event::class, OtherEvent::class);
        $this->assertFalse($this->conflictResolver->conflictsWith($otherEvent, $event));
        $this->assertFalse($this->conflictResolver->conflictsWith($event, $otherEvent));
    }
}
```

## File: `test/Broadway/EventStore/Management/InMemoryEventStoreManagementTest.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

namespace Broadway\EventStore\Management;

use Broadway\EventStore\InMemoryEventStore;
use Broadway\EventStore\Management\Testing\EventStoreManagementTest;

class InMemoryEventStoreManagementTest extends EventStoreManagementTest
{
    public function createEventStore()
    {
        return new InMemoryEventStore();
    }
}
```

## File: `test/Broadway/Processor/ProcessorTest.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

namespace Broadway\Processor;

use Broadway\Domain\DomainMessage;
use Broadway\Domain\Metadata;
use PHPUnit\Framework\TestCase;

class ProcessorTest extends TestCase
{
    /**
     * @test
     */
    public function it_passes_the_event_and_domain_message()
    {
        $testProcessor = new TestProcessor();
        $testEvent = new TestEvent();

        $this->assertFalse($testProcessor->isCalled());

        $testProcessor->handle($this->createDomainMessage($testEvent));

        $this->assertTrue($testProcessor->isCalled());
    }

    private function createDomainMessage($event)
    {
        return DomainMessage::recordNow(1, 1, new Metadata([]), $event);
    }
}

class TestProcessor extends Processor
{
    private $isCalled = false;

    public function handleTestEvent($event, DomainMessage $domainMessage)
    {
        $this->isCalled = true;
    }

    public function isCalled()
    {
        return $this->isCalled;
    }
}

class TestEvent
{
}
```

## File: `test/Broadway/ReadModel/ProjectorTest.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

namespace Broadway\ReadModel;

use Broadway\Domain\DomainMessage;
use Broadway\Domain\Metadata;
use PHPUnit\Framework\TestCase;

class ProjectorTest extends TestCase
{
    /**
     * @test
     */
    public function it_passes_the_event_and_domain_message()
    {
        $testProjector = new TestProjector();
        $testEvent = new TestEvent();

        $this->assertFalse($testProjector->isCalled());

        $testProjector->handle($this->createDomainMessage($testEvent));

        $this->assertTrue($testProjector->isCalled());
    }

    private function createDomainMessage($event)
    {
        return DomainMessage::recordNow(1, 1, new Metadata([]), $event);
    }
}

class TestProjector extends Projector
{
    private $isCalled = false;

    public function applyTestEvent($event, DomainMessage $domainMessage)
    {
        $this->isCalled = true;
    }

    public function isCalled()
    {
        return $this->isCalled;
    }
}

class TestEvent
{
}
```

## File: `test/Broadway/ReadModel/InMemory/InMemoryRepositoryFactoryTest.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

namespace Broadway\ReadModel\InMemory;

use PHPUnit\Framework\TestCase;

class InMemoryRepositoryFactoryTest extends TestCase
{
    /**
     * @test
     */
    public function it_creates_an_in_memory_repository()
    {
        $repository = new InMemoryRepository();
        $factory = new InMemoryRepositoryFactory();

        $this->assertEquals($repository, $factory->create('test', 'class'));
    }
}
```

## File: `test/Broadway/ReadModel/InMemory/InMemoryRepositoryTest.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

namespace Broadway\ReadModel\InMemory;

use Broadway\ReadModel\Repository;
use Broadway\ReadModel\Testing\RepositoryTestCase;
use Broadway\ReadModel\Testing\RepositoryTestReadModel;

class InMemoryRepositoryTest extends RepositoryTestCase
{
    protected function createRepository(): Repository
    {
        return new InMemoryRepository();
    }

    /**
     * @test
     */
    public function it_can_be_transferred_to_another_repository()
    {
        $repository = $this->createRepository();

        $model1 = $this->createReadModel('1', 'othillo', 'bar');
        $model2 = $this->createReadModel('2', 'asm89', 'baz');

        $this->repository->save($model1);
        $this->repository->save($model2);

        $targetRepository = new InMemoryRepository();

        $repository->transferTo($targetRepository);

        $this->assertEquals($targetRepository->findAll(), $repository->findAll());
    }

    protected function createReadModel($id, $name, $foo, array $array = []): RepositoryTestReadModel
    {
        return new RepositoryTestReadModel($id, $name, $foo, $array);
    }
}
```

## File: `test/Broadway/Serializer/ReflectionSerializerTest.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

namespace Broadway\Serializer;

use Assert\InvalidArgumentException;
use PHPUnit\Framework\TestCase;

class ReflectionSerializerTest extends TestCase
{
    /**
     * @var Serializer
     */
    private $serializer;

    protected function setUp(): void
    {
        $this->serializer = new ReflectionSerializer();
    }

    /**
     * @test
     *
     * @todo custom exception
     */
    public function it_throws_an_exception_if_class_not_set_in_data()
    {
        $this->expectException(InvalidArgumentException::class);
        $this->expectExceptionMessage('Key \'class\' should be set');

        $this->serializer->deserialize([]);
    }

    /**
     * @test
     *
     * @todo custom exception
     */
    public function it_throws_an_exception_if_payload_not_set_in_data()
    {
        $this->expectException(InvalidArgumentException::class);
        $this->expectExceptionMessage('Key \'payload\' should be set');

        $this->serializer->deserialize(['class' => 'SomeClass']);
    }

    /**
     * @test
     */
    public function it_serializes_objects()
    {
        $object = new TestReflectable(
            [new TestReflectableObject(['A', 1, 1.0], 11)],
            new TestReflectableObject(['B', 2, 2.0], 22),
            33
        );

        $this->assertEquals([
            'class' => 'Broadway\Serializer\TestReflectable',
            'payload' => [
                'simpleValue' => 33,
                'arrayOfObjects' => [
                    [
                        'class' => 'Broadway\Serializer\TestReflectableObject',
                        'payload' => [
                            'simpleArray' => ['A', 1, 1.0],
                            'value' => 11,
                        ],
                    ],
                ],
                'object' => [
                    'class' => 'Broadway\Serializer\TestReflectableObject',
                    'payload' => [
                        'simpleArray' => ['B', 2, 2.0],
                        'value' => 22,
                    ],
                ],
            ],
        ], $this->serializer->serialize($object));
    }

    /**
     * @test
     */
    public function it_deserializes_array()
    {
        $data = [
            'class' => 'Broadway\Serializer\TestReflectable',
            'payload' => [
                'simpleValue' => 33,
                'arrayOfObjects' => [
                    [
                        'class' => 'Broadway\Serializer\TestReflectableObject',
                        'payload' => [
                            'simpleArray' => ['A', 1, 1.0],
                            'value' => 11,
                        ],
                    ],
                ],
                'object' => [
                    'class' => 'Broadway\Serializer\TestReflectableObject',
                    'payload' => [
                        'simpleArray' => ['B', 2, 2.0],
                        'value' => 22,
                    ],
                ],
            ],
        ];

        $object = new TestReflectable(
            [new TestReflectableObject(['A', 1, 1.0], 11)],
            new TestReflectableObject(['B', 2, 2.0], 22),
            33
        );

        $this->assertEquals($object, $this->serializer->deserialize($data));
    }
}

class TestReflectableObject
{
    private $simpleArray;
    private $value;

    public function __construct(array $simpleArray, $value)
    {
        $this->simpleArray = $simpleArray;
        $this->value = $value;
    }
}

class TestReflectable
{
    private $arrayOfObjects;
    private $object;
    private $simpleValue;

    public function __construct(array $arrayOfObjects, $object, $simpleValue)
    {
        $this->arrayOfObjects = $arrayOfObjects;
        $this->object = $object;
        $this->simpleValue = $simpleValue;
    }
}
```

## File: `test/Broadway/Serializer/SimpleInterfaceSerializerTest.php`
```php
<?php

/*
 * This file is part of the broadway/broadway package.
 *
 * (c) 2020 Broadway project
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

declare(strict_types=1);

namespace Broadway\Serializer;

use Assert\InvalidArgumentException;
use PHPUnit\Framework\TestCase;

class SimpleInterfaceSerializerTest extends TestCase
{
    /**
     * @var SimpleInterfaceSerializer
     */
    private $serializer;

    protected function setUp(): void
    {
        $this->serializer = new SimpleInterfaceSerializer();
    }

    /**
     * @test
     */
    public function it_throws_an_exception_if_an_object_does_not_implement_serializable()
    {
        $this->expectException(SerializationException::class);
        $this->expectExceptionMessage(sprintf(
            'Object \'%s\' does not implement %s',
            \stdClass::class,
            Serializable::class
        ));

        $this->serializer->serialize(new \stdClass());
    }

    /**
     * @test
     *
     * @todo custom exception
     */
    public function it_throws_an_exception_if_class_not_set_in_data()
    {
        $this->expectException(InvalidArgumentException::class);
        $this->expectExceptionMessage('Key \'class\' should be set');

        $this->serializer->deserialize([]);
    }

    /**
     * @test
     *
     * @todo custom exception
     */
    public function it_throws_an_exception_if_payload_not_set_in_data()
    {
        $this->expectException(InvalidArgumentException::class);
        $this->expectExceptionMessage('Key \'payload\' should be set');

        $this->serializer->deserialize(['class' => 'SomeClass']);
    }

    /**
     * @test
     */
    public function it_serializes_objects_implementing_serializable()
    {
        $object = new TestSerializable('bar');

        $this->assertEquals([
            'class' => 'Broadway\Serializer\TestSerializable',
            'payload' => ['foo' => 'bar'],
        ], $this->serializer->serialize($object));
    }

    /**
     * @test
     */
    public function it_deserializes_classes_implementing_serializable()
    {
        $data = ['class' => 'Broadway\Serializer\TestSerializable', 'payload' => ['foo' => 'bar']];

        $this->assertEquals(new TestSerializable('bar'), $this->serializer->deserialize($data));
    }

    /**
     * @test
     */
    public function it_can_deserialize_classes_it_has_serialized()
    {
        $object = new TestSerializable('bar');

        $serialized = $this->serializer->serialize($object);
        $deserialized = $this->serializer->deserialize($serialized);

        $this->assertEquals($object, $deserialized);
    }
}

class TestSerializable implements Serializable
{
    private $foo;

    public function __construct($foo)
    {
        $this->foo = $foo;
    }

    /**
     * @return $this
     */
    public static function deserialize(array $data)
    {
        return new self($data['foo']);
    }

    public function serialize(): array
    {
        return ['foo' => $this->foo];
    }
}
```

## File: `test/Broadway/Upcasting/SequentialUpcasterChainTest.php`
```php
<?php

declare(strict_types=1);

namespace Broadway\Upcasting;

use Broadway\Domain\DateTime;
use Broadway\Domain\DomainMessage;
use Broadway\Domain\Metadata;
use PHPUnit\Framework\TestCase;

class SequentialUpcasterChainTest extends TestCase
{
    /**
     * @test
     */
    public function it_should_upcast_domain_messages_sequentially(): void
    {
        $sequentialUpcasterChain = new SequentialUpcasterChain([
            new SomeEventV1toV2Upcaster(),
            new SomeEventV2toV3Upcaster(),
        ]);

        $domainMessage = new DomainMessage(1, 0, new Metadata(), new SomeEvent('matiux'), DateTime::now());

        $upcastedDomainMessage = $sequentialUpcasterChain->upcast($domainMessage);

        self::assertInstanceOf(SomeEventV3::class, $upcastedDomainMessage->getPayload());
        self::assertEquals('N/A', $upcastedDomainMessage->getPayload()->surname);
        self::assertEquals(0, $upcastedDomainMessage->getPayload()->age);
    }
}

class SomeEvent
{
    public $name;

    public function __construct(string $name)
    {
        $this->name = $name;
    }
}

class SomeEventV2
{
    public $name;
    public $surname;

    public function __construct(string $name, string $surname)
    {
        $this->name = $name;
        $this->surname = $surname;
    }
}

class SomeEventV3
{
    public $name;
    public $surname;
    public $age;

    public function __construct(string $name, string $surname, int $age)
    {
        $this->name = $name;
        $this->surname = $surname;
        $this->age = $age;
    }
}

class SomeEventV1toV2Upcaster implements Upcaster
{
    public function supports(DomainMessage $domainMessage): bool
    {
        return $domainMessage->getPayload() instanceof SomeEvent;
    }

    public function upcast(DomainMessage $domainMessage): DomainMessage
    {
        $payload = $domainMessage->getPayload();

        $upcastedEvent = new SomeEventV2(
            $payload->name,
            'N/A'
        );

        return new DomainMessage(
            $domainMessage->getId(),
            $domainMessage->getPlayhead(),
            $domainMessage->getMetadata(),
            $upcastedEvent,
            $domainMessage->getRecordedOn()
        );
    }
}

class SomeEventV2toV3Upcaster implements Upcaster
{
    public function supports(DomainMessage $domainMessage): bool
    {
        return $domainMessage->getPayload() instanceof SomeEventV2;
    }

    public function upcast(DomainMessage $domainMessage): DomainMessage
    {
        $payload = $domainMessage->getPayload();

        $upcastedEvent = new SomeEventV3(
            $payload->name,
            $payload->surname,
            0
        );

        return new DomainMessage(
            $domainMessage->getId(),
            $domainMessage->getPlayhead(),
            $domainMessage->getMetadata(),
            $upcastedEvent,
            $domainMessage->getRecordedOn()
        );
    }
}
```

## File: `test/Broadway/Upcasting/UpcastingEventStoreTest.php`
```php
<?php

declare(strict_types=1);

namespace Broadway\Upcasting;

use Broadway\Domain\DomainEventStream;
use Broadway\Domain\DomainMessage;
use Broadway\Domain\Metadata;
use Broadway\EventStore\InMemoryEventStore;
use PHPUnit\Framework\TestCase;

class UpcastingEventStoreTest extends TestCase
{
    /**
     * @test
     */
    public function it_should_call_upcaster_when_event_stream_is_not_empty(): void
    {
        $upcasterChain = $this->createMock(UpcasterChain::class);

        $eventStore = new UpcastingEventStore(new InMemoryEventStore(), $upcasterChain);

        $events[] = DomainMessage::recordNow(5, 0, new Metadata([]), 'Foo');
        $events[] = DomainMessage::recordNow(5, 1, new Metadata([]), 'Bar');

        $upcasterChain->expects($this->exactly(2))
            ->method('upcast')
            ->willReturnMap([
                [$events[0], $events[0]],
                [$events[1], $events[1]],
            ]);

        $eventStore->append(1, new DomainEventStream($events));
        $eventStore->load(1);
    }
}
```


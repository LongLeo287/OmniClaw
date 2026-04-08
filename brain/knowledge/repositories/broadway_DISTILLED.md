---
id: repo-fetched-broadway-144313
type: knowledge
owner: OA
registered_at: 2026-04-05T04:02:28.346936
tags: ["auto-cloned", "oa-assimilated"]
---

# FETCHED_broadway_144313

## Assimilation Report
Auto-cloned repository: FETCHED_broadway_144313

## Application for OmniClaw
No structural integration blueprint provided.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
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

### File: CHANGELOG.md
```md
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

### File: UPGRADE.md
```md
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

### File: VETTING_REPORT.md
```md
---
title: Auto Vetting Report for broadway
date: 2026-04-05
analyst: civ_vetting_pipeline
status: AUTO_VETTED
---

# Auto-Vetted Repository
This repository was automatically swept and vetted by the batch processor. Only documentation remains.

```

### File: docs\examples.md
```md
## Examples

Examples can be found in the [`examples/`][examples] directory. Most of the
examples focus on showing how one of the components works. There is also a more
[deliberate example][example] using several components and showing how you can
test your event sourced model.

[examples]: https://github.com/broadway/broadway/tree/master/examples
[example]: https://github.com/broadway/broadway/tree/master/examples/event-sourced-domain-with-tests

```

### File: docs\index.md
```md
* Introduction
* Components
    * [Auditing](components/auditing.md)
    * [CommandHandling](components/command_handling.md)
    * [Domain](components/domain.md)
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
    * [Repository](components/repository.md)
    * [Saga](https://github.com/broadway/broadway-saga)
    * [Sensitive data handling](https://github.com/broadway/broadway-sensitive-data)
    * [Serializer](components/serializer.md)
    * [Snapshotting](https://github.com/broadway/snapshotting)
* [Integrations](integrations.md)
* [Examples](examples.md)

# Introduction

Broadway is a project providing infrastructure and testing helpers for creating
CQRS and event sourced applications. Broadway tries hard to not get in your
way. The project contains several loosely coupled components that can be used
together to provide a full CQRS\ES experience.

Read the blog post about this repository at: [Bringing CQRS and Event Sourcing to PHP. Open sourcing Broadway!](http://labs.qandidate.com/blog/2014/08/26/broadway-our-cqrs-es-framework-open-sourced/)

```

### File: docs\integrations.md
```md
# Integrations

- There is a [bundle] available to use with your Symfony application.

- A [Laravel package] is also available to allow the use of Broadway inside a Laravel application.

Contributions for integrations with other projects are appreciated!

[bundle]: https://github.com/broadway/broadway-bundle
[Laravel package]: https://github.com/nWidart/Laravel-broadway

```


---
id: commanded
type: knowledge
owner: OA_Triage
---
# commanded
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
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
- [Using Commanded](guides/Usage.md)
  - [Aggregates](guides/Aggregates.md)
    - [Example aggregate](guides/Aggregates.md#example-aggregate)
    - [`Commanded.Aggregate.Multi`](guides/Aggregates.md#using-commandedaggregatemulti-to-return-multiple-events)
    - [Aggregate state snapshots](guides/Aggregates.md#aggregate-state-snapshots)
  - [Commands](guides/Commands.md)
    - [Command handlers](guides/Commands.md#command-handlers)
    - [Command dispatch and routing](guides/Commands.md#command-dispatch-and-routing)
      - [Define aggregate identity](guides/Commands.md#define-aggregate-identity)
      - [Multi-command registration](guides/Commands.md#multi-command-registration)
      - [Dispatch timeouts](guides/Commands.md#timeouts)
      - [Dispatch consistency guarantee](guides/Commands.md#command-dispatch-consistency-guarantee)
      - [Dispatch returning execution result](guides/Commands.md#dispatch-returning-execution-result)
      - [Aggregate lifespan](guides/Commands.md#aggregate-lifespan)
      - [Composite command routers](guides/Commands.md#composite-command-routers)
    - [Middleware](guides/Commands.md#middleware)
      - [Example middleware](guides/Commands.md#example-middleware)
    - [Composite command routers](guides/Commands.md#composite-command-routers)
  - [Events](guides/Events.md)
    - [Domain events](guides/Events.md#domain-events)
    - [Event handlers](guides/Events.md#event-handlers)
      - [Consistency guarantee](guides/Events.md#consistency-guarantee)
      - [Error handling](guides/Events.md#handling-errors)
    - [Upcasting events](guides/Events.md#upcasting-events)
  - [Process managers](guides/Process%20Managers.md)
    - [Example process manager](guides/Process%20Managers.md#example-process-manager)
  - [Supervision](guides/Supervision.md)
  - [Serialization](guides/Serialization.md)
    - [Default JSON serializer](guides/Serialization.md#default-json-serializer)
    - [Configuring JSON serialization](guides/Serialization.md#configuring-json-serialization)
    - [Decoding event structs](guides/Serialization.md#decoding-event-structs)
    - [Using an alternative serialization format](guides/Serialization.md#using-an-alternative-serialization-format)
    - [Customising serialization](guides/Serialization.md#customising-serialization)
  - [Read model projections](guides/Read%20Model%20Projections.md)
- [Deployment](guides/Deployment.md)
  - [Single node deployment](guides/Deployment.md#single-node-deployment)
  - [Multi node cluster deployment](guides/Deployment.md#multi-node-cluster-deployment)
  - [Multi node, but not clustered deployment](guides/Deployment.md#multi-node-but-not-clustered-deployment)
- [Testing with Commanded](guides/Testing.md)
- [Used in production?](#used-in-production)
- [Example application](#example-application)
- [Learn Commanded in 20 minutes](#learn-commanded-in-20-minutes)
- [Choosing an event store provider](guides/Choosing%20an%20Event%20Store.md#writing-your-own-event-store-provider)
- [Tooling](https://github.com/commanded/commanded/wiki/Tooling)
- [Contributing](#contributing)
- [Need help?](#need-help)

---

## Used in production?

Yes, see the [companies using Commanded](https://github.com/commanded/commanded/wiki/Companies-using-Commanded).

## Example application

[Conduit](https://github.com/slashdotdash/conduit) is an open source, example Phoenix 1.3 web application implementing the CQRS/ES pattern in Elixir. It was built to demonstrate the implementation of Commanded in an Elixir application for the [Building Conduit](https://leanpub.com/buildingconduit) book.

## Learn Commanded in 20 minutes

[Watch Bernardo Amorim introduce CQRS and event sourcing](https://www.youtube.com/watch?v=S3f6sAXa3-c) at Code Beam SF 2018. Including a tutorial on how to implement an Elixir application using these concepts with Commanded.

## Contributing

Pull requests to contribute new or improved features, and extend documentation are most welcome.

Please follow the existing coding conventions, or refer to the [Elixir style guide](https://github.com/niftyn8/elixir_style_guide).

You should include unit tests to cover any changes. Run `mix test` to execute the test suite.

### Contributors

Commanded exists thanks to the following people who have contributed.

<a href="https://github.com/commanded/commanded/graphs/contributors"><img src="https://opencollective.com/commanded/contributors.svg?width=890&button=false" width="890" /></a>

- [Adil Yarulin](https://github.com/ayarulin)
- [Alexandre de Souza](https://github.com/aleDsz)
- [Andrey Akulov](https://github.com/astery)
- [Andrzej Sliwa](https://github.com/andrzejsliwa)
- [Ben Smith](https://github.com/slashdotdash)
- [Benjamin Moss](https://github.com/drteeth)
- [Bernardo Amorim](https://github.com/bamorim)
- [Brenton Annan](https://github.com/brentonannan)
- [Chris Brodt](https://github.com/uberbrodt)
- [Chris Martin](https://github.com/trbngr)
- [Christophe Juniet](https://github.com/cjuniet)
- [Danilo Silva](https://github.com/silvadanilo)
- [Dave Lucia](https://github.com/davydog187)
- [David Carlin](https://github.com/davich)
- [Damir Vandic](https://github.com/dvic)
- [Danni Friedland](https://github.com/BlueHotDog)
- [Dilaksun Bavarajan](https://github.com/DilaksunB)
- [Ernesto](https://github.com/lex-mala)
- [Fernando Mendes](https://github.com/justmendes)
- [Florian Ebeling](https://github.com/febeling)
- [Henry Hazan](https://github.com/henry-hz)
- [JC](https://github.com/jccf091)
- [Joan Zapata](https://github.com/JoanZapata)
- [Joao Gilberto Moura](https://github.com/joaobalsini)
- [João Thallis](https://github.com/joaothallis)
- [John Wilger](https://github.com/jwilger)
- [Joseph Lozano](https://github.com/joseph-lozano)
- [Kian-Meng Ang](https://github.com/kianmeng)
- [Kok J Sam](https://github.com/sammkj)
- [Leif Gensert](https://github.com/leifg)
- [Luís Ferreira](https://github.com/zamith)
- [Marcelo Dominguez](https://github.com/marpo60)
- [Matt Doughty](https://github.com/m-doughty)
- [Matthew Boehlig](https://github.com/thetamind)
- [Michael Herold](https://github.com/michaelherold)
- [Miguel Palhas](https://github.com/naps62)
- [Nigel Thorne](https://github.com/nigelthorne)
- [Olafur Arason](https://github.com/olafura)
- [Paolo Laurenti](https://github.com/PaoloLaurenti)
- [Patrick Detlefsen](https://github.com/patrickdet)
- [Phil Chen](https://github.com/fahchen)
- [Raphaël Lustin](https://github.com/rlustin)
- [Štefan Ľupták](https://github.com/EskiMag)
- [Tobiasz Małecki](https://github.com/amatalai)
- [Vladimir Drobyshevskiy](https://github.com/vheathen)
- [Willy Wombat](https://github.com/octowombat)
- [Yordis Prieto](https://github.com/yordis)
- [Yuri de Figueiredo](https://github.com/y86)
- [Zven](https://github.com/zven21)

## Need help?

Please [open an issue](https://github.com/commanded/commanded/issues) if you encounter a problem, or need assistance. You can also seek help in the #commanded channel in the [official Elixir Slack](https://elixir-lang.slack.com/).

```

### File: BACKERS.md
```md
# Sponsors & Backers

## Sponsors via GitHub

Thank you to all our sponsors! 🙏

### Companies

[![Alembic](https://user-images.githubusercontent.com/3167/177830256-26a74e82-60ff-4c20-bd84-64ee7c12512c.svg "Alembic")](https://alembic.com.au/)

> We're a software consultancy specialising in Elixir, TypeScript, GraphQL and React

---

### Individuals

* Benjamin Moss ([@drteeth](https://github.com/drteeth))
* Bill Tihen ([@btihen](https://github.com/btihen))
* Bruno Antunes ([@sardaukar](https://github.com/sardaukar))
* Calum Boal ([@Cgboal](https://github.com/Cgboal))
* Danilo Silva ([@silvadanilo](https://github.com/silvadanilo))
* Dirk Elmendorf ([@delmendo](https://github.com/delmendo))
* Kacper Perzankowski ([@perzanko](https://github.com/perzanko))
* Kevin Stevens ([@KevDog](https://github.com/KevDog))
* Luca Zulian ([@lucazulian](https://github.com/lucazulian))
* Niklas Johansson ([@Raphexion](https://github.com/Raphexion))
* Qiu Hua ([@qhwa](https://github.com/qhwa))

## Backers via OpenCollective

Thank you to all our backers! 🙏

* [Axle Payments](https://www.axlepayments.com/)
* [Gray Beam](https://twitter.com/graybeamcode)
* [Smarkup](https://smarkup.com/)
* [Zach Baker](https://opencollective.com/zach-baker)

<a href="https://opencollective.com/commanded#backers" target="_blank"><img src="https://opencollective.com/commanded/tiers/backers.svg?width=890"></a>

## Sponsors via OpenCollective

<a href="https://opencollective.com/commanded#backers" target="_blank"><img src="https://opencollective.com/commanded/tiers/bronze-sponsors.svg?width=890"></a> <a href="https://opencollective.com/commanded#backers" target="_blank"><img src="https://opencollective.com/commanded/tiers/silver-sponsors.svg?width=890&button=false"></a> <a href="https://opencollective.com/commanded#backers" target="_blank"><img src="https://opencollective.com/commanded/tiers/gold-sponsors.svg?width=890&button=false"></a> <a href="https://opencollective.com/commanded#backers" target="_blank"><img src="https://opencollective.com/commanded/tiers/platinum-sponsors.svg?width=890&button=false"></a>

```

### File: CHANGELOG.md
```md
# Changelog

## v1.4.9

### Enhancements

* Put telemetry on dehydration by @cdegroot in https://github.com/commanded/commanded/issues/552
* Add issue template by @yordis in https://github.com/commanded/commanded/issues/630
* Add generic serializer behaviour by @Nezteb in https://github.com/commanded/commanded/issues/626
* Add aggregate behaviour by @Nezteb in https://github.com/commanded/commanded/issues/627
* Batching support by @fmterrorf in https://github.com/commanded/commanded/issues/569
* Make Aggregate.take_snapshot/3 a blocking call by @satom99 in https://github.com/commanded/commanded/issues/636

### Bug fixes

* Fix flakey test by @drteeth in https://github.com/commanded/commanded/pull/599
* Fix malformed markdown link by @djonn in https://github.com/commanded/commanded/issues/619
* Update elixir slack link by @afomi in https://github.com/commanded/commanded/issues/620

## v1.4.8

### Bug fixes

* `Commanded.Event.ErrorHandler` now keeps surounding failure context by @drteeth in https://github.com/commanded/commanded/issues/617

## v1.4.7

### Enhancements

* Application-wide event handler error handling by @drteeth in https://github.com/commanded/commanded/pull/605
* chore: remove asdf file by @yordis in https://github.com/commanded/commanded/pull/570
* chore: improve docs about aggregate version by @yordis in https://github.com/commanded/commanded/pull/608
* Update include_aggregate_version documentation by @TylerPachal in https://github.com/commanded/commanded/pull/609

### Bug fixes

* Fix flakey test by @drteeth in https://github.com/commanded/commanded/pull/599
* feat: default aggregate lifespan configuration by @yordis in https://github.com/commanded/commanded/pull/548
* Aggregate.handle_* now properly handles lifespans by @drteeth in https://github.com/commanded/commanded/pull/606
* Allow registration handle_call/cast callbacks to be called by @drteeth in https://github.com/commanded/commanded/pull/607
* Update local_cluster by @drteeth in https://github.com/commanded/commanded/pull/610

## v1.4.6

### Enhancements
- Includes changelog updates
- Version bump

## v1.4.5

### Enhancements
- Support OTP 26 and Elixir 1.17 ([#595](https://github.com/commanded/commanded/pull/595)).

## v1.4.4

### Enhancements
- feat: put aggregate_state into assigns of the pipeline ([#502](https://github.com/commanded/commanded/pull/502)).
- Add tag to partition test case ([#525](https://github.com/commanded/commanded/pull/525)).
- Make before_reset/0 an explicit callback function ([#550](https://github.com/commanded/commanded/pull/550)).
- New `Event.Handler.after_start/1` callback allows configuration in the handler's process ([#568](https://github.com/commanded/commanded/pull/568)).

### Bug fixes
- Fix EventData typespec ([#495](https://github.com/commanded/commanded/pull/495)).
- Fix refute_receive_event examples ([#557](https://github.com/commanded/commanded/pull/557)).
- Fix interested? function doc ([#562](https://github.com/commanded/commanded/pull/562)).
- Use TypeProvider for process managers snapshot serialization ([#558](https://github.com/commanded/commanded/pull/558)).
- fix(router.ex): Telemetry is not emitted if dispatch fails for {:error, :unregistered_command} ([#563](in https://github.com/commanded/commanded/pull/563)).

## v1.4.3

### Enhancements

- Use `Logger.warning` to fix deprecation warnings ([#542](https://github.com/commanded/commanded/pull/542)).
- Add typespec to `CompositeRouter.dispatch/2` function ([#536](https://github.com/commanded/commanded/pull/536)).
- Support `opts` in `Commanded.EventStore.append_to_stream` function ([#528](https://github.com/commanded/commanded/pull/528)).
- Process manager metadata access ([#514](https://github.com/commanded/commanded/pull/514)).

### Bug fixes

-  Correct parameter type in `ProcessManager.after_command/1` callback function ([#533](https://github.com/commanded/commanded/pull/533)).

## v1.4.2

- Record aggregate state while processing `Commanded.Aggregate.Multi` ([#507](https://github.com/commanded/commanded/pull/507)).
- Properly handle EXIT signal in event handler ([#512](https://github.com/commanded/commanded/pull/512)).
- Separate logging a process managers error ([#513](https://github.com/commanded/commanded/pull/513)).

## v1.4.1

### Enhancements

- Retry command execution when the aggregate process is down ([#494](https://github.com/commanded/commanded/pull/494)).

### Bug fixes

- Remove duplicate apply function call when receiving missed events published to an aggregate's event stream ([364c877](https://github.com/commanded/commanded/commit/364c877e8f30a18d90544676fb58b94132d50720)).
- Fix typespec typo in Commanded.Application ([#503](https://github.com/commanded/commanded/pull/503)).

## v1.4.0

### Enhancements

- Allow a process manager to stop after dispatching a command ([#460](https://github.com/commanded/commanded/pull/460)).
- Replace `use Mix.Config` with `import Config` in config files ([#467](https://github.com/commanded/commanded/pull/467)).
- Event handler concurrency ([#486](https://github.com/commanded/commanded/pull/486)).
- Remove `elixir_uuid` dependency ([#493](https://github.com/commanded/commanded/pull/493)).
- Support and test for OTP 25 ([#489](https://github.com/commanded/commanded/pull/489)).

---

## v1.3.1

### Bug fixes

- Event Handler not calling `init/1` callback function on restart ([#463](https://github.com/commanded/commanded/pull/463)).
- Call process manager `init/1` function on process restart ([#464](https://github.com/commanded/commanded/pull/464)).

## v1.3.0

### Enhancements

- Allow command identity to be provided during dispatch ([#406](https://github.com/commanded/commanded/pull/406)).
- Define `Commanded.Telemetry` module to emit consistent telemetry events ([#414](https://github.com/commanded/commanded/pull/414)).
- Telemetry `[:commanded, :aggregate, :execute]` events ([#407](https://github.com/commanded/commanded/pull/407)).
- Telemetry `[:commanded, :event, :handle]` events ([#408](https://github.com/commanded/commanded/pull/408)).
- Telemetry `[:commanded, :process_manager, :handle]` events ([#418](https://github.com/commanded/commanded/pull/418)).
- Telemetry `[:commanded, :application, :dispatch]` ([#423](https://github.com/commanded/commanded/pull/423)).
- Graceful shutdown of event handlers ([#431](https://github.com/commanded/commanded/pull/431)).
- Ensure command dispatch metadata is a map ([#432](https://github.com/commanded/commanded/pull/432)).
- Retry command execution on node down ([#429](https://github.com/commanded/commanded/pull/429)).
- Dispatch returning resultant events ([#444](https://github.com/commanded/commanded/pull/444)).
- Get aggregate state ([#448](https://github.com/commanded/commanded/pull/448)).
- Support telemetry v1.0 ([#456](https://github.com/commanded/commanded/pull/456)).

## v1.2.0

### Enhancements

- Add `init/1` callback function to event handlers and process managers ([#393](https://github.com/commanded/commanded/pull/393)).
- Include `application` and `handler_name` as additional event handler metadata ([#396](https://github.com/commanded/commanded/pull/396)).
- Allow `GenServer` start options to be provided when starting event handlers and process managers ([#398](https://github.com/commanded/commanded/pull/398)).
- Add `hibernate_after` option to application config ([#399](https://github.com/commanded/commanded/pull/399)).
- Add support for providing adapter-specific event store subscription options ([#391](https://github.com/commanded/commanded/pull/391)).
- Support custom state for event handlers ([#400](https://github.com/commanded/commanded/pull/400)).
- Allow event handlers and process manager `error` callback to return failure context struct ([#397](https://github.com/commanded/commanded/issues/397)).
- Allow a before execute function to be defined which is called with the command dispatch execution context and aggregate state before ([#402](https://github.com/commanded/commanded/pull/402)).

### Bug fixes

- Allow process manager `error/3` callback to return `:skip` for failed commands, not just failed events ([#362](https://github.com/commanded/commanded/issues/362)).

---

## v1.1.1

### Enhancements

- Capture exception on Process Manager `apply/2` and call `error/3` callback functions ([#380](https://github.com/commanded/commanded/pull/380)).
- Include metadata in upcaster protocol ([#389](https://github.com/commanded/commanded/pull/389)).

### Bug fixes

- Fix `Commanded.Aggregate.Multi.execute/2` calls which return ` Multi` struct ([#385](https://github.com/commanded/commanded/pull/385])).

## v1.1.0

### Enhancements

- Dynamic Commanded applications ([#324](https://github.com/commanded/commanded/pull/324)).
- Log and ignore unexpected messages received by event handlers and process manager instances ([#333](https://github.com/commanded/commanded/pull/333))
- Process manager `identity/0` function ([#334](https://github.com/commanded/commanded/pull/334)).
- Extend `Commanded.AggregateCase` ExUnit case template to support `Commanded.Aggregate.Multi`.
- Allow `Commanded.Aggregate.Multi` to return events as `:ok` tagged tuples.
- Run the formatter in CI ([#341](https://github.com/commanded/commanded/pull/341)).
- Add stacktraces to EventHandler error logging ([#340](https://github.com/commanded/commanded/pull/340))
- `refute_receive_event/4` only tests newly created events ([#347](https://github.com/commanded/commanded/pull/347)).
- Allow Commanded Application name to be set dynamically in middleware ([#352](https://github.com/commanded/commanded/pull/352)).
- Remove router module compile-time checking ([#363](https://github.com/commanded/commanded/pull/363)).
- Reduce memory consumption during aggregate state rebuild ([#368](https://github.com/commanded/commanded/pull/368)).
- Upgrade to `phoenix_pubsub` to 2.0 ([#365](https://github.com/commanded/commanded/pull/365)).
- Ignore `:not_found` error when resetting InMemory event store ([#354](https://github.com/commanded/commanded/pull/354)).
- Add `router/1` to `locals_without_parens` in Mix format config ([#351](https://github.com/commanded/commanded/pull/351)).
- Include stacktrace in event handler and process manager `error` callback functions ([#342](https://github.com/commanded/commanded/pull/342)).
- Call event handler's `error/3` callback function when `handle/2` function returns an invalid value ([#372](https://github.com/commanded/commanded/pull/372)).

### Bug fixes

- Fixes the typespec for command dispatch ([#325](https://github.com/commanded/commanded/pull/325)).
- Process manager stops if `interested?/1` returns an empty list ([#335](https://github.com/commanded/commanded/pull/335)).

---

## v1.0.1

### Enhancements

- Global registry using Erlang's `:global` module ([#344](https://github.com/commanded/commanded/pull/344)).
- Command dispatch return ([#331](https://github.com/commanded/commanded/pull/331)).

### Bug fixes

- Fix distributed subscription registration bug ([#345](https://github.com/commanded/commanded/pull/345)).
- Retry event handler and process manager subscriptions on error ([#348](https://github.com/commanded/commanded/pull/348)).

## v1.0.0

### Breaking changes

- Support multiple Commanded apps ([#298](https://github.com/commanded/commanded/pull/298)).

### Enhancements

- Define adapter behaviour modules for event store, pubsub, and registry ([#311](https://github.com/commanded/commanded/pull/311)).
- Add `AggregateCase` ExUnit case template to support aggregate unit testing ([#315](https://github.com/commanded/commanded/pull/315)).
- Application config lookup ([#318](https://github.com/commanded/commanded/pull/318)).

### Bug fixes

- Fix process manager exception on start ([#307](https://github.com/commanded/commanded/pull/307)).
- Fix commanded aggregate race ([#308](https://github.com/commanded/commanded/pull/308)).
- Fix Dialyzer warnings and include in Travis CI ([#317](https://github.com/commanded/commanded/pull/317)).

### Upgrading

[Follow the upgrade guide](https://hexdocs.pm/commanded/1.0.0/0.19-1.0.html) to define and use your own Commanded application.

---

## v0.19.1

### Enhancements

- Reset event handler mix task `mix commanded.reset MyApp.Handler` ([#293](https://github.com/commanded/commanded/pull/293)).

### Bug fixes

- Fix regression in `Commanded.Middleware.Logger.delta` ([#295](https://github.com/commanded/commanded/pull/295)).

## v0.19.0

### Enhancements

- Update typespec for `data` and `metadata` fields in `Commanded.EventStore.EventData` struct ([#246](https://github.com/commanded/commanded/pull/246)).
- Add `include_execution_result` and `aggregate_version` to typespec for router command dispatch ([#262](https://github.com/commanded/commanded/pull/262)).
- Add `.formatter.exs` to Hex package ([#247](https://github.com/commanded/commanded/pull/247)).
- Event upcasting ([#263](https://github.com/commanded/commanded/pull/263)).
- Support `:ok` tagged tuple events from aggregate ([#268](https://github.com/commanded/commanded/pull/268)).
- Modify `Commanded.Registration.start_child` to pass a child_spec ([#273](https://github.com/commanded/commanded/pull/273)).
- Add `supervisor_child_spec/2` to `Commanded.Registration` behaviour ([#277](https://github.com/commanded/commanded/pull/277)) used by [Commanded Horde Registry](https://github.com/uberbrodt/commanded_horde_registry).
- Ensure Commanded can be compiled when optional Jason dependency is not present ([#286](https://github.com/commanded/commanded/pull/286)).
- Fix Aggregate initialization races ([#287](https://github.com/commanded/commanded/pull/287)).
- Support `{:system, varname}` format in Phoenix PubSub config ([#291](https://github.com/commanded/commanded/pull/291)).

### Breaking changes

- Use `DateTime` instead of `NaiveDateTime` for all datetimes ([#254](https://github.com/commanded/commanded/pull/254)).

    This affects the `created_at` field defined in the `Commanded.EventStore.RecordedEvent`. You will need to migrate from `NaiveDateTime` to `DateTime` if you use this field in your code (such as in an event handler's metadata).

---

## v0.18.1

### Enhancements

- Process manager idle process timeout ([#290](https://github.com/commanded/commanded/pull/290)).
- Register event handler and process manager subscriptions on process start ([#272](https://github.com/commanded/commanded/pull/272)).

## v0.18.0

### Enhancements

- Rename `uuid` dependency to `elixir_uuid` ([#178](https://github.com/commanded/commanded/pull/178)).
- Allow aggregate identity to be of any type that implements the `String.Chars` protocol ([#166](https://github.com/commanded/commanded/pull/166)).
- Process manager and event handler error & exception handling ([#192](https://github.com/commanded/commanded/pull/192)).
- Process manager event handling timeout ([#193](https://github.com/commanded/commanded/pull/193)).
- Allow event handlers to subscribe to individual streams 
... [TRUNCATED]
```


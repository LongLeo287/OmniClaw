---
id: eventstore
type: knowledge
owner: OA_Triage
---
# eventstore
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
# EventStore

Event store implemented in Elixir. Uses [PostgreSQL](http://www.postgresql.org/) as the underlying storage engine.

Requires Elixir v1.10 and PostgreSQL v9.5 or newer.

EventStore supports [running on a cluster of nodes](guides/Cluster.md).

- [Changelog](CHANGELOG.md)
- [Wiki](https://github.com/commanded/eventstore/wiki)
- [Frequently asked questions](https://github.com/commanded/eventstore/wiki/FAQ)
- [Getting help](https://github.com/commanded/eventstore/wiki/Getting-help)
- [Latest published Hex package](https://hex.pm/packages/eventstore) & [documentation](https://hexdocs.pm/eventstore/)

MIT License

![Build Status](https://github.com/commanded/eventstore/workflows/Test/badge.svg?branch=master)

---

### Overview

> This README and the following guides follow the `master` branch which may not be the currently published version.
> [Read docs for the latest published version of EventStore on Hex](https://hexdocs.pm/eventstore/).

- [Getting started](guides/Getting%20Started.md)
  - [Using an existing database](guides/Getting%20Started.md#using-an-existing-database)
  - [Reset an existing database](guides/Getting%20Started.md#reset-an-existing-database)
  - [Initialize a database using an Elixir release](guides/Getting%20Started.md#initialize-a-database-using-an-elixir-release)
  - [Using Postgres schemas](guides/Getting%20Started.md#using-postgres-schemas)
  - [Event data and metadata data type](guides/Getting%20Started.md#event-data-and-metadata-data-type)
    - [Using the `jsonb` data type](guides/Getting%20Started.md#using-the-jsonb-data-type)
  - [Using with PgBouncer](guides/Getting%20Started.md#using-with-pg-bouncer)
- [Using the EventStore](guides/Usage.md)
  - [Writing to a stream](guides/Usage.md#writing-to-a-stream)
    - [Appending events to an existing stream](guides/Usage.md#appending-events-to-an-existing-stream)
  - [Reading from a stream](guides/Usage.md#reading-from-a-stream)
  - [Reading from all streams](guides/Usage.md#reading-from-all-streams)
  - [Stream from all streams](guides/Usage.md#stream-from-all-streams)
  - [Linking events between streams](guides/Usage.md#linking-events-between-streams)
  - [Deleting streams](guides/Usage.md#deleting-streams)
- [Subscriptions](guides/Subscriptions.md)
  - [Transient subscriptions](guides/Subscriptions.md#transient-subscriptions)
  - [Persistent subscriptions](guides/Subscriptions.md#persistent-subscriptions)
    - [Acknowledge received events](guides/Subscriptions.md#acknowledge-received-events)
    - [Subscription concurrency](guides/Subscriptions.md#subscription-concurrency)
    - [Example persistent subscriber](guides/Subscriptions.md#example-persistent-subscriber)
    - [Deleting a persistent subscription](guides/Subscriptions.md#deleting-a-persistent-subscription)
- [Running on a cluster](guides/Cluster.md)
- [Event serialization](guides/Event%20Serialization.md)
- [Upgrading an EventStore](guides/Upgrades.md)
- [Used in production?](#used-in-production)
- [Backup and administration](#backup-and-administration)
- [Benchmarking performance](#benchmarking-performance)
- [Contributing](#contributing)
  - [Contributors](#contributors)
- [Need help?](#need-help)

---

## Example usage

Define an event store module:

```elixir
defmodule MyEventStore do
  use EventStore, otp_app: :my_app
end
```

Start the event store:

```elixir
{:ok, _pid} = MyEventStore.start_link()
```

Create one or more event structs to be persisted (serialized to JSON by default):

```elixir
defmodule ExampleEvent do
  defstruct [:key]
end
```

Append events to a stream:

```elixir
stream_uuid = EventStore.UUID.uuid4()
expected_version = 0

events = [
  %EventStore.EventData{
    event_type: "Elixir.ExampleEvent",
    data: %ExampleEvent{key: "value"},
    metadata: %{user: "someuser@example.com"}
  }
]

:ok = MyEventStore.append_to_stream(stream_uuid, expected_version, events)
```

Read all events from a single stream, starting at the stream's first event:

```elixir
{:ok, events} = MyEventStore.read_stream_forward(stream_uuid)
```

More: [Usage guide](guides/Usage.md)

Subscribe to events appended to all streams:

```elixir
{:ok, subscription} = MyEventStore.subscribe_to_all_streams("example_subscription", self())

# Wait for the subscription confirmation
receive do
  {:subscribed, ^subscription} ->
    IO.puts("Successfully subscribed to all streams")
end

# Receive a batch of events appended to the event store
receive do
  {:events, events} ->
    IO.puts("Received events: #{inspect events}")

    # Acknowledge successful receipt of events
    :ok = MyEventStore.ack(subscription, events)
end
```

In production use you would use a [`GenServer` subscriber process](guides/Subscriptions.md#example-subscriber) and the `handle_info/2` callback to receive events.

More: [Subscriptions guide](guides/Subscriptions.md)

## Used in production?

Yes, this event store is being used in production.

PostgreSQL is used for the underlying storage. Providing guarantees to store data securely. It is ACID-compliant and transactional. PostgreSQL has a proven architecture. A strong reputation for reliability, data integrity, and correctness.

## Backup and administration

You can use any standard PostgreSQL tool to manage the event store data:

- [Backup and restore](https://www.postgresql.org/docs/current/static/backup-dump.html).
- [Continuous archiving and Point-in-Time Recovery (PITR)](https://www.postgresql.org/docs/current/static/continuous-archiving.html).

## Benchmarking performance

Run the benchmark suite using mix with the `bench` environment, as configured in `config/bench.exs`. Logging is disabled for benchmarking.

```console
MIX_ENV=bench mix do es.reset, app.start, bench
```

Example output:

```
## AppendEventsBench
benchmark name                         iterations   average time
append events, single writer                  100   20288.68 µs/op
append events, 10 concurrent writers           10   127416.90 µs/op
append events, 20 concurrent writers            5   376836.60 µs/op
append events, 50 concurrent writers            2   582350.50 µs/op
## ReadEventsBench
benchmark name                         iterations   average time
read events, single reader                    500   3674.93 µs/op
read events, 10 concurrent readers             50   44653.98 µs/op
read events, 20 concurrent readers             20   73927.55 µs/op
read events, 50 concurrent readers             10   188244.80 µs/op
## SubscribeToStreamBench
benchmark name                         iterations   average time
subscribe to stream, 1 subscription           100   27687.97 µs/op
subscribe to stream, 10 subscriptions          50   56047.72 µs/op
subscribe to stream, 20 subscriptions          10   194164.40 µs/op
subscribe to stream, 50 subscriptions           5   320435.40 µs/op
```

After running two benchmarks you can compare the runs:

```console
MIX_ENV=bench mix bench.cmp -d percent
```

You can also produce an HTML page containing a graph comparing benchmark runs:

```console
MIX_ENV=bench mix bench.graph
```

Taking the above example output, the append events benchmark is for writing 100 events in a single batch. That's what the µs/op average time is measuring. For a single writer it takes on average 0.02s per 100 events appended (4,929 events/sec) and for 50 concurrent writers it's 50 x 100 events in 0.58s (8,586 events/sec).

For reading events it takes a single reader 3.67ms to read 100 events (27,211 events/sec) and for 50 concurrent readers it takes 0.19s (26,561 events/sec).

### Using the benchmark suite

The purpose of the benchmark suite is to measure the performance impact of proposed changes, as opposed to looking at the raw numbers. The above figures are taken when run against a local PostgreSQL database. You can run the benchmarks against your own hardware to get indicative performance figures for the Event Store.

The benchmark suite is configured to use Erlang's [external term format](http://erlang.org/doc/apps/erts/erl_ext_dist.html) serialization. Using another serialization format, such as JSON, will likely have a negative impact on performance.

## Testing

Tests can be run using any Postgres database instance, including via Docker.

To use Docker, first pull the latest Postgres image:

```shell
docker pull postgres
```

A [tmpfs](https://docs.docker.com/storage/tmpfs/) mount can be used to run the Docker container with the Postgres data directory stored in memory.

```shell
docker run --rm \
  --name postgres \
  --tmpfs=/pgtmpfs \
  -e PGDATA=/pgtmpfs \
  -e POSTGRES_PASSWORD=postgres \
  -e POSTGRES_USER=postgres \
  -p 5432:5432 \
  postgres
```

Alternatively, use Docker Compose
```shell
docker compose up
```

### Running tests

Create and initialize the test event store databases:

```
MIX_ENV=test mix event_store.setup
```

Run the test suite:

```
mix test
```

## Contributing

Pull requests to contribute new or improved features, and extend documentation are most welcome.

Please follow the existing coding conventions, or refer to the [Elixir style guide](https://github.com/niftyn8/elixir_style_guide).

You should include unit tests to cover any changes.

### Contributors

EventStore exists thanks to the following people who have contributed.

- [Andreas Riemer](https://github.com/arfl)
- [Andrey Akulov](https://github.com/astery)
- [Basile Nouvellet](https://github.com/BasileNouvellet)
- [Ben Smith](https://github.com/slashdotdash)
- [Bruce Williams](https://github.com/bruce)
- [Chris Brodt](https://github.com/uberbrodt)
- [Chris Martin](https://github.com/trbngr)
- [Christian Green](https://github.com/Arthien)
- [Craig Savolainen](https://github.com/maedhr)
- [Damir Vandic](https://github.com/dvic)
- [David Soff](https://github.com/Davidsoff)
- [Derek Kraan](https://github.com/derekkraan)
- [Diogo Scudelletti](https://github.com/scudelletti)
- [Dominik Guzei](https://github.com/DominikGuzei)
- [Douglas Vought](https://github.com/voughtdq)
- [Eamon Taaffe](https://github.com/eamontaaffe)
- [Floris Huetink](https://github.com/florish)
- [Fredrik Teschke](https://github.com/ftes)
- [Ilya Suzdalnitskiy](https://github.com/suzdalnitski)
- [Jan Vereecken](https://github.com/javereec)
- [Kai Kuchenbecker](https://github.com/kaikuchn)
- [Kaz Walker](https://github.com/KazW)
- [Morten Berg Nissen](https://github.com/mbnissen)
- [Nicholas Henry](https://github.com/nicholasjhenry)
- [Olafur Arason](https://github.com/olafura)
- [Ole Michaelis](https://github.com/OleMchls)
- [Paul Iannazzo](https://github.com/boxxxie)
- [Piotr Szmielew](https://github.com/esse)
- [Raphaël Lustin](https://github.com/rlustin)
- [Ryan Young](https://github.com/ryoung786)
- [Samuel Roze](https://github.com/sroze)
- [Simon Harris](https://github.com/harukizaemon)
- [Stuart Corbishley](https://github.com/stuartc)
- [Thomas Coopman](https://github.com/tcoopman)
- [Victor Oliveira Nascimento](https://github.com/victorolinasc)
- [Yamil Díaz Aguirre](https://github.com/Yamilquery)
- [Yannis Weishaupt](https://github.com/MrYawe)
- [Yordis Prieto](https://github.com/yordis)

## Need help?

Please [open an issue](https://github.com/commanded/eventstore/issues) if you encounter a problem, or need assistance. You can also seek help in the #commanded channel in the [official Elixir Slack](https://elixir-slackin.herokuapp.com/).

```

### File: CHANGELOG.md
```md
# Changelog

## v1.4.8

### Bug fixes

* Stream.stream_forward and Stream.stream_backward should handle gaps by @lachiemurray in https://github.com/commanded/eventstore/pull/297
* Use event count based on the batch by @yordis in https://github.com/commanded/eventstore/pull/302
* Remove status from sort_by options by @yordis in https://github.com/commanded/eventstore/pull/304
* Start pubsub supervisor before subscriptions supervisor by @drteeth in https://github.com/commanded/eventstore/pull/300

### Enhancements

* Add documentation for deleting streams by @quarterpi in https://github.com/commanded/eventstore/pull/305

## v1.4.7

### Enhancements

* Add support for overriding created_at timestamps for copy transform workflows by @Johnabell in https://github.com/commanded/eventstore/pull/282

### Bug fixes

* fix: merge session mode pool config with main config, preserving options by @gf3 in https://github.com/commanded/eventstore/pull/293

## v1.4.6

### Enhancements

* Expands CI test matrix to cover supported Elixir and OTP versions ([#291](https://github.com/commanded/eventstore/pull/291)).
* Bump version
* Updates changelog :)

## v1.4.5

### Enhancements

* Add a docker compose file for standing up a suitable development database ([#290](https://github.com/commanded/eventstore/pull/290)).

### Bug fixes

* `append_to_stream` can now properly append more than 1000 events again ([#289](https://github.com/commanded/eventstore/pull/289)).

## v1.4.4

### Bug fixes

* Handle `DBConnection.ConnectionError` errors when appending events to storage ([#261](https://github.com/commanded/eventstore/pull/261)).

## v1.4.3

### Enhancements

* Support Elixir v1.11 and later.
* Parse url with encoded hash in password ([#275](https://github.com/commanded/eventstore/pull/275)).
* Allow configuring the default database ([#277](https://github.com/commanded/eventstore/pull/277)).
* Fix Elixir `Logger.warn/2` warning deprecation message ([#278](https://github.com/commanded/eventstore/pull/278)).
* Quote schema names in SQL ([#266](https://github.com/commanded/eventstore/pull/266)).
* Fix unused read batch size ([#279](https://github.com/commanded/eventstore/pull/279)).

## v1.4.2

### Enhancements

* Allow `disconnect_on_error_codes` to be passed to the event store Postgrex connection ([#263](https://github.com/commanded/eventstore/pull/263)).
* Support all `Postgrex` and `DBConnection` options when configuring an event store ([#273](https://github.com/commanded/eventstore/pull/273)).

### Bug fixes

* Dialyzer error when calling `EventStore.subscribe/2` with `:name` option ([#268](https://github.com/commanded/eventstore/pull/268)).
* Terminate a monitored process only if there are no other processes registered to use it ([#272](https://github.com/commanded/eventstore/pull/272)).

## v1.4.1

### Enhancements

- Allow `:parameters` to be passed to the EventStore database connection ([#257](https://github.com/commanded/eventstore/pull/257)).
- Use configurable `:timeout` option for subscription database queries ([#259](https://github.com/commanded/eventstore/pull/259)).

## v1.4.0

- List running event store instances ([#244](https://github.com/commanded/eventstore/pull/244)).
- Paginate streams ([#246](https://github.com/commanded/eventstore/pull/246)).
- Add `stream_info/2` function ([#247](https://github.com/commanded/eventstore/pull/247)).
- Remove unmaintained `elixir_uuid` dependency ([#253](https://github.com/commanded/eventstore/pull/253)).
- Add option to use EventStore with PgBouncer ([#249](https://github.com/commanded/eventstore/pull/249)).

---

## v1.3.2

### Enhancements

- Add postgrex `socket_options` option ([#242](https://github.com/commanded/eventstore/pull/242)).

### Bug fixes

- Fix bug with subscriptions trigger in older Postgres versions ([#241](https://github.com/commanded/eventstore/pull/241)).

### Upgrading

This release includes a database migration to be run. Please read the [Upgrading an EventStore](https://hexdocs.pm/eventstore/upgrades.html) guide for details on how to migrate an existing database.

## v1.3.1

### Bug fixes

- Support running event store migrations when using a schema ([#239](https://github.com/commanded/eventstore/pull/239)).

## v1.3.0

- Improve performance of appending events under normal and degraded network conditions ([#230](https://github.com/commanded/eventstore/pull/230)).
- Subscription checkpoint tuning ([#237](https://github.com/commanded/eventstore/pull/237)).

## Bug fixes

- Fix bug with catch-up all streams subscription where the checkpoint is not committed for hard deleted streams ([#238](https://github.com/commanded/eventstore/pull/238)).

### Upgrading

This release requires a database migration to be run. Please read the [Upgrading an EventStore](https://hexdocs.pm/eventstore/upgrades.html) guide for details on how to migrate an existing database.

---

## v1.2.3

- Add `:configure` to postgrex connection options ([#233](https://github.com/commanded/eventstore/pull/233)).
- Use runtime configuration in Mix tasks ([#236](https://github.com/commanded/eventstore/pull/236)).

## v1.2.2

- Read stream and stream events backward ([#234](https://github.com/commanded/eventstore/pull/234)).

## v1.2.1

- Allow optional `event_id` to be included in `EventStore.EventData` struct ([#229](https://github.com/commanded/eventstore/pull/229)).
- Adds an option to supply an existing database connection or transaction to `EventStore` functions ([#231](https://github.com/commanded/eventstore/pull/231)).

## v1.2.0

### Enhancements

- Delete event stream ([#203](https://github.com/commanded/eventstore/pull/203)).
- Introduce `mix event_store.migrations` task to list migration status ([#207](https://github.com/commanded/eventstore/pull/207)).
- Remove distributed registry ([#210](https://github.com/commanded/eventstore/pull/210)).
- Hibernate subscription process after inactivity ([#214](https://github.com/commanded/eventstore/pull/214)).
- Runtime event store configuration ([#217](https://github.com/commanded/eventstore/pull/217)).
- Shared database connection pools ([#216](https://github.com/commanded/eventstore/pull/216)).
- Shared database connection for notifications ([#225](https://github.com/commanded/eventstore/pull/225)).
- Transient subscriptions ([#215](https://github.com/commanded/eventstore/pull/215))
- Improve resilience when database connection is unavailable ([#226](https://github.com/commanded/eventstore/pull/226)).

### Upgrading

This release requires a database migration to be run. Please read the [Upgrading an EventStore](https://hexdocs.pm/eventstore/upgrades.html) guide for details on how to migrate an existing database.

### Breaking changes

Usage of `EventStore.Tasks.Init` task to initialise an event store database has been changed as follows:

Previous usage:

```elixir
:ok = EventStore.Tasks.Init.exec(MyApp.EventStore, config, opts)
```

Usage now:

```elixir
:ok = EventStore.Tasks.Init.exec(config)
:ok = EventStore.Tasks.Init.exec(config, opts)
```

### Bug fixes

- Support appending events to a stream with `:any_version` concurrently ([#209](https://github.com/commanded/eventstore/pull/209)).

---

## v1.1.0

### Enhancements

- Support Postgres schemas ([#182](https://github.com/commanded/eventstore/pull/182)).
- Dynamic event store ([#184](https://github.com/commanded/eventstore/pull/184)).
- Add `timeout` option to config ([#189](https://github.com/commanded/eventstore/pull/189)).
- Namespace advisory lock to prevent clash with other applications ([#166](https://github.com/commanded/eventstore/issues/166)).
- Use database lock to prevent migrations from running concurrently ([#204](https://github.com/commanded/eventstore/pull/204)).

### Breaking changes

The following EventStore API functions have been changed where previously (in v1.0 and earlier) the last argument was an optional timeout (a non-negative integer or `:infinity`). This has been changed to be an optional Keyword list, which may include a timeout (e.g. `[timeout: 5_000]`). The `stream_forward` and `stream_all_forward` functions now also require the optional `read_batch_size` argument to be provided as part of the options Keyword list.

These changes were required to support dynamic event stores where an event store name can be included in the options to each function. If you did not provide a timeout to any of these functions then you will not need to make any changes to your code. See the example usages below for details.

- `EventStore.append_to_stream`
- `EventStore.link_to_stream`
- `EventStore.read_stream_forward`
- `EventStore.read_all_streams_forward`
- `EventStore.stream_forward`
- `EventStore.stream_all_forward`

Previous usage:

```elixir
EventStore.append_to_stream(stream_uuid, expected_version, events, timeout)
EventStore.link_to_stream(stream_uuid, expected_version, events_or_event_ids, timeout)
EventStore.read_stream_forward(stream_uuid, start_version, count, timeout)
EventStore.read_all_streams_forward(start_version, count, timeout)
EventStore.stream_forward(stream_uuid, start_version, read_batch_size, timeout)
EventStore.stream_all_forward(start_version, read_batch_size, timeout)
```

Usage now:

```elixir
EventStore.append_to_stream(stream_uuid, expected_version, events, timeout: timeout)
EventStore.link_to_stream(stream_uuid, expected_version, events_or_event_ids, timeout: timeout)
EventStore.read_stream_forward(stream_uuid, start_version, count, timeout: timeout)
EventStore.read_all_streams_forward(start_version, count, timeout: timeout)
EventStore.stream_forward(stream_uuid, start_version, read_batch_size: read_batch_size, timeout: timeout)
EventStore.stream_all_forward(start_version, read_batch_size: read_batch_size, timeout: timeout)
```

### Upgrading

This release requires a database migration to be run. Please read the [Upgrading an EventStore](https://hexdocs.pm/eventstore/upgrades.html) guide for details on how to migrate an existing database.

---

## v1.0.3

### Bug fixes

- Use event's stream version when appending events to a stream ([#202](https://github.com/commanded/eventstore/pull/202)).

## v1.0.2

#### Enhancements

- Prevent double supervision by starting / stopping supervisor manually ([#194](https://github.com/commanded/eventstore/pull/194)).
- Use `DynamicSupervisor` for subscriptions.

## v1.0.1

### Bug fixes

- Fix `EventStore.Registration.DistributedForwarder` state when running multiple nodes ([#186](https://github.com/commanded/eventstore/pull/186)).

## v1.0.0

### Enhancements

- Support multiple event stores ([#168](https://github.com/commanded/eventstore/pull/168)).
- Add support for `queue_target` and `queue_interval` database connection settings ([#172](https://github.com/commanded/eventstore/pull/172)).
- Add support for `created_at` values to be of type `NaiveDateTime` ([#175](https://github.com/commanded/eventstore/pull/175)).

### Bug fixes

- Fix function clause error on `DBConnection.ConnectionError` ([#167](https://github.com/commanded/eventstore/issues/167)).

### Upgrading

[Follow the upgrade guide](guides/upgrades/0.17-1.0.md) to define and use your own application specific event store].

---

## v0.17.0

### Enhancements

- SSL support including Mix tasks ([#161](https://github.com/commanded/eventstore/pull/161)).
- Use `timestamp with time zone` for timestamp fields ([#150](https://github.com/commanded/eventstore/pull/150)).

### Upgrading

Upgrade your existing EventStore database by running:

```console
mix event_store.migrate
```

**Note**: The migrate command is idempotent and can be safely run multiple times.

You can drop and recreate an EventStore database by running:

```console
mix do event_store.drop, event_store.create, event_store.init
```

---

## v0.16.2

### Bug fixes

- Fix issue with concurrent subscription partitioning ([#162](https://github.com/commanded/eventstore/pull/162)).
- Reliably start `EventStore.Notifications.Supervisor` on `:global` name clash ([#165](https://github.com/commanded/eventstore/pull/165)).

## v0.16.1

### Bug fixes

- Stop Postgrex database connection process in mix `event_store.init` and `event_store.migrate` tasks after use to prevent IEx shutdown when tasks are run together (as `mix do event_store.init, event_store.migrate`).
- Ensure the event store application doesn't crash when the database connection is lost ([#159](https://github.com/commanded/eventstore/pull/159)).

## v0.16.0

### Enhancements

- Add `:socket` and `:socket_dir` config options ([#132](https://github.com/commanded/eventstore/pull/132)).
- Rename `uuid` dependency to `elixir_uuid` ([#135](https://github.com/commanded/eventstore/pull/135)).
- Subscription concurrency ([#134](https://github.com/commanded/eventstore/pull/134)).
- Send `:subscribed` message to all subscribers connected to a subscription ([#136](https://github.com/commanded/eventstore/pull/136)).
- Update to `postgrex` v0.14 ([#143](https://github.com/commanded/eventstore/pull/143)).

### Breaking changes

- Replace `:poison` with `:jason` for JSON event data & metadata serialization ([#144](https://github.com/commanded/eventstore/pull/144)).

  To support this change you will need to derive the `Jason.Encoder` protocol for all of your events.

  This can be done by adding `@derive Jason.Encoder` before defining the struct in every event module.

  ```elixir
  defmodule Event1 do
    @derive Jason.Encoder
    defstruct [:id, :data]
  end
  ```

  Or using `Protocol.derive/2` for each event, as shown below.

  ```elixir
  require Protocol

  for event <- [Event1, Event2, Event3] do
    Protocol.derive(Jason.Encoder, event)
  end
  ```

---

## 0.15.1

### Enhancements

- Use a timeout of `:infinity` for the migration task (`mix event_store.migrate`) to allow database migration to run longer than the default 15 seconds.

### Bug fixes

- Socket closing causes the event store to never receive notifications ([#130](https://github.com/commanded/eventstore/pull/130)).
- Subscription with selector function should notify pending events after all filtered ([#131](https://github.com/commanded/eventstore/pull/131)).

## 0.15.0

- Support system environment variables for all config ([#115](https://github.com/commanded/eventstore/pull/115)).
- Allow subscriptions to filter the events they receive ([#114](https://github.com/commanded/eventstore/pull/114)).
- Allow callers to omit `event_type` when event data is a struct ([#118](https://github.com/commanded/eventstore/pull/118)).
- Remove dependency on `psql` for `event_store.create`, `event_store.init`, `event_store.migrate`, and `event_store.drop` mix tasks ([#117](https://github.com/commanded/eventstore/pull/117)).
- Supports query parameters in URL for database connection ([#119](https://github.com/commanded/eventstore/pull/119)).
- Improve typespecs and include Dialyzer in Travis CI build ([#121](https://github.com/commanded/eventstore/pull/121)).

---

## 0.14.0

- Add JSONB support ([#86](https:/
... [TRUNCATED]
```

### File: guides\Architecture.md
```md
### PostgreSQL usage

EventStore creates multiple connections to the Postres database:

- a pooled connection, that you configure via `config/config.exs`, used for most database operations (e.g. reading/appending events);
- a connection used to listen for event notifications (using Postgres' `LISTEN` / `NOTIFY`);
- and another connection for subscription [advisory locks](https://www.postgresql.org/docs/current/static/explicit-locking.html#ADVISORY-LOCKS).

If you configure EventStore to use a `pool_size` of 10, then you will have 12 Postgres database connections in total.

The pooled connection uses `:exp` back-off. However the other connections use `:stop` back-off so that the connection process terminates when the database connection is broken. These connections are monitored by another process and will be restarted.

#### Why are these connections stopped on error?

Related processes need to be notified when the connection exits or is restarted. The [postgrex](https://hexdocs.pm/postgrex/) library doesn't provide a way of being notified when the connection terminates. As an example, EventStore uses [Postgres' advisory locks](https://www.postgresql.org/docs/current/static/explicit-locking.html#ADVISORY-LOCKS) to guarantee only one instance of a subscription runs, regardless of how many nodes are running (or whether they are clustered). These advisory locks are tied to a database connection and are released when the connection terminates. When this happens, EventStore attempts to reacquire the locks. The `EventStore.MonitoredServer` module provides this process monitoring and `after_exit` and `after_restart` callback functions.

```

### File: guides\Cluster.md
```md
# Running on a cluster of nodes

EventStore supports running on multiple nodes as either a [distributed Erlang](http://erlang.org/doc/reference_manual/distributed.html) cluster or as multiple single instance nodes.

## Event publication

PostgreSQL's `LISTEN` / `NOTIFY` is used to pub/sub event notifications. A listener database connection process is started on each node. It connects to the database to listen for events and publishes them to interested subscription processes running on the node. The approach is the same regardless of whether distributed Erlang is used or not.

## Subscriptions

PostgreSQL's [advisory locks](https://www.postgresql.org/docs/current/static/explicit-locking.html#ADVISORY-LOCKS) are used to limit each uniquely named subscription to run at most once. This prevents multiple instances of a subscription from running on different nodes. Advisory locks are faster than table locks, are stored in memory to avoid table bloat, and are automatically cleaned up by the server at the end of the session.

## Automatic cluster formation

You can use [libcluster](https://github.com/bitwalker/libcluster) to automatically form clusters of Erlang nodes, with either static or dynamic node membership.

You will need to include `libcluster` as an additional dependency in `mix.exs`:

```elixir
defp deps do
  [{:libcluster, "~> 2.2"}]
end
```

Then configure your preferred cluster topology in the environment config (e.g. `config/config.exs`). An example is shown below using the standard Erlang `epmd` daemon strategy:

```elixir
config :libcluster,
  topologies: [
    example: [
      strategy: Cluster.Strategy.Epmd,
      config: [hosts: [:"node1@127.0.0.1", :"node2@127.0.0.1", :"node3@127.0.0.1"]],
    ]
  ]
```

Please refer to the [`libcluster` documentation](https://hexdocs.pm/libcluster/) for more detail.

### Starting a cluster

  1. Run an [Erlang Port Mapper Daemon](http://erlang.org/doc/man/epmd.html) (epmd):

      ```console
      $ epmd -d
      ```

  2. Start an `iex` console per node:

      ```console
      $ MIX_ENV=distributed iex --name node1@127.0.0.1 -S mix
      ```

      ```console
      $ MIX_ENV=distributed iex --name node2@127.0.0.1 -S mix
      ```

      ```console
      $ MIX_ENV=distributed iex --name node3@127.0.0.1 -S mix
      ```

The cluster will be automatically formed as soon as the nodes start.

## Static cluster topology and formation

Instead of using `libcluster` you can configure the `:kernel` application to wait for cluster formation before starting your application during node start up. This approach is useful when you have a static cluster topology that can be defined in config.

The `sync_nodes_optional` configuration specifies which nodes to attempt to connect to within the `sync_nodes_timeout` window, defined in milliseconds, before continuing with startup. There is also a `sync_nodes_mandatory` setting which can be used to enforce all nodes are connected within the timeout window or else the node terminates.

Each node requires its own individual configuration, listing the other nodes in the cluster:

```elixir
# node1 config
config :kernel,
  sync_nodes_optional: [:"node2@192.168.1.1", :"node3@192.168.1.2"],
  sync_nodes_timeout: 30_000
```

The `sync_nodes_timeout` can be configured as `:infinity` to wait indefinitely for all nodes to
connect. All involved nodes must have the same value for `sync_nodes_timeout`.

The above approach will *only work* for Elixir releases. You will need to use [Erlang's `sys.config`](http://erlang.org/doc/man/config.html) file for development purposes.

The Erlang equivalent of the `:kernerl` mix config, as above, is:

```erlang
% node1.sys.config
[{kernel,
  [
    {sync_nodes_optional, ['node2@127.0.0.1', 'node3@127.0.0.1']},
    {sync_nodes_timeout, 30000}
  ]}
].
```

### Starting a cluster

  1. Run an [Erlang Port Mapper Daemon](http://erlang.org/doc/man/epmd.html) (epmd):

      ```console
      $ epmd -d
      ```

  2. Start an `iex` console per node:

      ```console
      $ MIX_ENV=distributed iex --name node1@127.0.0.1 --erl "-config cluster/node1.sys.config" -S mix
      ```

      ```console
      $ MIX_ENV=distributed iex --name node2@127.0.0.1 --erl "-config cluster/node2.sys.config" -S mix
      ```

      ```console
      $ MIX_ENV=distributed iex --name node3@127.0.0.1 --erl "-config cluster/node3.sys.config" -S mix
      ```

The node specific `<node>.sys.config` files ensure the cluster is formed before starting your application, assuming this occurs within the 30 seconds timeout.

Once the cluster has formed, you can use your event store module from any node.

## Usage

Using the event store when run on a cluster of nodes is identical to single node usage. You can subscribe to a stream, or all streams, on one node and append events to the stream on another. The subscription will be notified of the appended events.

### Append events to a stream

```elixir
alias EventStore.EventData
alias MyApp.EventStore

defmodule ExampleEvent do
  defstruct [:key]
end

stream_uuid = EventStore.UUID.uuid4()

events = [
  %EventData{
    event_type: "Elixir.ExampleEvent",
    data: %ExampleEvent{key: "value"},
    metadata: %{user: "someuser@example.com"},
  }
]

:ok = EventStore.append_to_stream(stream_uuid, 0, events)
```

### Read all events

```elixir
alias MyApp.EventStore

recorded_events = EventStore.stream_all_forward() |> Enum.to_list()
```

### Subscribe to all Streams

```elixir
alias MyApp.EventStore

{:ok, subscription} = EventStore.subscribe_to_all_streams("example-subscription", self(), start_from: :origin)

receive do
  {:subscribed, ^subscription} ->
    IO.puts("Successfully subscribed to all streams")
end

receive do
  {:events, events} ->
    IO.puts("Received events: #{inspect(events)}")

    :ok = EventStore.ack(subscription, events)
end
```

```

### File: guides\Event Serialization.md
```md
# Event serialization

The default serialization of event data and metadata uses Erlang's [external term format](http://erlang.org/doc/apps/erts/erl_ext_dist.html). This is not a recommended serialization format for production usage as backwards compatibility is only guaranteed going back at least two major releases.

You must implement the `EventStore.Serializer` behaviour to provide your preferred serialization format.

## JSON serialization using Jason

EventStore includes a JSON serializer using Jason in the `EventStore.JsonSerializer` module. To include it, add `{:jason, "~> 1.1"}` to your application's mix dependencies and configure your EventStore as below.

```elixir
config :eventstore, MyApp.EventStore, serializer: EventStore.JsonSerializer
```

## Example JSON serializer using Poison

The example serializer below serializes event data and metadata to JSON using the [Poison](https://github.com/devinus/poison) library.

```elixir
defmodule JsonSerializer do
  @moduledoc """
  A serializer that uses the JSON format.
  """

  @behaviour EventStore.Serializer

  @doc """
  Serialize given term to JSON binary data.
  """
  def serialize(term) do
    Poison.encode!(term)
  end

  @doc """
  Deserialize given JSON binary data to the expected type.
  """
  def deserialize(binary, config) do
    type = case Keyword.get(config, :type, nil) do
      nil -> []
      type -> type |> String.to_existing_atom |> struct
    end
    Poison.decode!(binary, as: type)
  end
end
```

Configure the JSON serializer for your event store by setting the `serializer` option in the mix environment configuration file (e.g. `config/dev.exs`):

```elixir
config :eventstore, MyApp.EventStore, serializer: JsonSerializer
```

You must set the `event_type` field to a string representing the type of event being persisted when using this serializer:

```elixir
%EventStore.EventData{
  event_type: "Elixir.ExampleEvent",
  data: %ExampleEvent{key: "value"},
  metadata: %{user: "someuser@example.com"},
}
```

You can use `Atom.to_string/1` to get a string representation of a given event struct compatible with the example `JsonSerializer` module:

```elixir
event = %ExampleEvent{key: "value"}
event_type = Atom.to_string(event.__struct__)  #=> "Elixir.ExampleEvent"
```

```

### File: guides\FAQ.md
```md
## Frequently asked questions

- [What version of PostgreSQL is supported?](#what-version-of-postgresql-is-supported)
- [Which PostgreSQL hosting provider is supported?](#which-postgresql-hosting-provider-is-supported)

---

### What version of PostgreSQL is supported?

PostgreSQL v9.5 or later.

---

### Which PostgreSQL hosting provider is supported?

You can verify a potential hosting provider by running the EventStore test suite against an instance of the hosted PostgreSQL database. If all tests pass, then you should be fine.

To run the test suite you must first clone this GitHub repository:

```console
git clone https://github.com/commanded/eventstore.git
cd eventstore
mix deps.get
```

Then configure your database connection settings for the test environment, in `config/test.exs`.

Once configured, you can create the test database and run the tests:

```console
MIX_ENV=test mix do event_store.create, event_store.init
mix test
```


```

### File: guides\Getting Started.md
```md
# Getting started

EventStore is [available in Hex](https://hex.pm/packages/eventstore) and can be installed as follows:

  1. Add eventstore to your list of dependencies in `mix.exs`:

      ```elixir
      def deps do
        [{:eventstore, "~> 1.4"}]
      end
      ```

      Run `mix deps.get` to install the new dependency.

  2. Define an event store module for your application:

      ```elixir
      defmodule MyApp.EventStore do
        use EventStore, otp_app: :my_app

        # Optional `init/1` function to modify config at runtime.
        def init(config) do
          {:ok, config}
        end
      end
      ```

  3. Add a config entry containing the PostgreSQL database connection details for your event store module to each environment's mix config file (e.g. `config/dev.exs`):

      ```elixir
      config :my_app, MyApp.EventStore,
        serializer: EventStore.JsonSerializer,
        username: "postgres",
        password: "postgres",
        database: "eventstore",
        hostname: "localhost"

      # OR use a URL to connect instead
      config :my_app, MyApp.EventStore,
        serializer: EventStore.JsonSerializer,
        url: "postgres://postgres:postgres@localhost/eventstore"
      ```


      **Note:** Some managed database providers (such as DigitalOcean) don't provide access to the default `postgres` database. In such case, you can specify a default database in the following way:

      ```elixir
      config :my_app, MyApp.EventStore,
        default_database: "defaultdb",
      ```

      **Note:** To use an EventStore with Commanded you should configure the event
      store to use Commanded's JSON serializer which provides additional support for
      JSON decoding:

      ```elixir
      config :my_app, MyApp.EventStore, serializer: Commanded.Serialization.JsonSerializer
      ```

      Configure optional database connection settings:

      ```elixir
      config :my_app, MyApp.EventStore,
        pool_size: 10
        queue_target: 50
        queue_interval: 1_000,
        schema: "schema_name"
      ```

      The database connection pool configuration options are:

      - `:pool_size` - The number of connections (default: `10`).

      Handling requests is done through a queue. When DBConnection is started, there are two relevant options to control the queue:

      - `:queue_target` - in milliseconds (default: 50ms).
      - `:queue_interval` - in milliseconds (default: 1,000ms).

      Additional options:

      - `:schema` - define the Postgres schema to use (default: `public` schema).
      - `:timeout` - set the default database query timeout in milliseconds (default: 15,000ms).
      - `:shared_connection_pool` - allows a database connection pool to be shared amongst multiple event store instances (default: `nil`).

      Subscription options:

      - `:subscription_retry_interval` - interval between subscription connection retry attempts (default: 60,000ms).
      - `:subscription_hibernate_after` - subscriptions will automatically hibernate to save memory after a period of inactivity (default: 15,000ms).

  4. Add your event store module to the `event_stores` list for your app in mix config:

      ```elixir
      # config/config.exs
      config :my_app, event_stores: [MyApp.EventStore]
      ```

      This ensures the event store mix tasks can be run without specifying the event store as a command line argument (e.g. `mix event_store.init -e MyApp.EventStore`).

  5. Create and initialize the event store database and tables using the `mix` tasks:

      ```console
      $ mix do event_store.create, event_store.init
      ```

  6. The final piece of configuration is to setup your event store as a supervisor within your application's supervision tree (e.g. in `lib/my_app/application.ex`, inside the `start/2` function):

      ```elixir
      defmodule MyApp.Application do
        use Application

        def start(_type, _args) do
          children = [
            MyApp.EventStore
          ]

          opts = [strategy: :one_for_one, name: MyApp.Supervisor]
          Supervisor.start_link(children, opts)
        end
      end
      ```

## Using an existing database

You can use an existing PostgreSQL database with EventStore by running the following `mix` task to create and initialize the event store tables:

```console
$ mix event_store.init
```

## Reset an existing database

To drop an existing EventStore database and recreate it you can run the following `mix` tasks:

```console
$ mix do event_store.drop, event_store.create, event_store.init
```

*Warning* This will drop the database and delete all data.

## Initialize a database using an Elixir release

If you're using an Elixir release build by the task [mix release](https://hexdocs.pm/mix/Mix.Tasks.Release.html) you won't have `mix` available therefore you won't be able to run the following command in order to initialize a new database.

```console
$ mix do event_store.create, event_store.init
```

To do that you can use task modules defined inside EventStore (in `lib/mix/tasks`):

* [EventStore.Tasks.Create](https://github.com/commanded/eventstore/blob/master/lib/event_store/tasks/create.ex)
* [EventStore.Tasks.Init](https://github.com/commanded/eventstore/blob/master/lib/event_store/tasks/init.ex)

 So you can take advantage of the [running one-off commands](https://hexdocs.pm/mix/Mix.Tasks.Release.html#module-one-off-commands-eval-and-rpc) supported by Mix release, using a helper module defined like this:

```elixir
defmodule MyApp.ReleaseTasks do
  def init_event_store do
    {:ok, _} = Application.ensure_all_started(:postgrex)
    {:ok, _} = Application.ensure_all_started(:ssl)

    :ok = Application.load(:my_app)

    config = MyApp.EventStore.config()

    :ok = EventStore.Tasks.Create.exec(config, [])
    :ok = EventStore.Tasks.Init.exec(config, [])
  end
end
```

## Using Postgres schemas

A Postgres database contains one or more [named schemas](https://www.postgresql.org/docs/current/ddl-schemas.html), which in turn contain tables. By default tables are defined in a schema named "public".

An EventStore can be configured to use a different schema name. Specify the schema when using the `EventStore` macro in your event store module:

```elixir
defmodule MyApp.EventStore do
  use EventStore, otp_app: :my_app, schema: "example"
end
```

Or provide the schema as an option in the `init/1` callback function:

```elixir
defmodule MyApp.EventStore do
  use EventStore, otp_app: :my_app

  def init(config) do
    {:ok, Keyword.put(config, :schema, "example")}
  end
end
```

Or define it in environment config when configuring the database connection settings:

```elixir
# config/config.exs
config :my_app, MyApp.EventStore, schema: "example"
```

This feature allows you to define and start multiple event stores sharing a single Postgres database, but with their data isolated and segregated by schema.

Note the `mix event_store.<task>` tasks to create, initialize, and drop an event store database will also handle creating and/or dropping the schema.

## Event data and metadata data type

EventStore has support for persisting event data and metadata as either:

  - Binary data, using the [`bytea` data type](https://www.postgresql.org/docs/current/static/datatype-binary.html), designed for storing binary strings.
  - JSON data, using the [`jsonb` data type](https://www.postgresql.org/docs/current/static/datatype-json.html), specifically designed for storing JSON encoded data.

The default data type is `bytea`. This can be used with any binary serializer, such as the Erlang Term format, JSON data encoded to binary, and other serialization formats.

### Using the `jsonb` data type

The advantage this format is that it allows you to execute ad-hoc SQL queries against the event data or metadata using PostgreSQL's native JSON query support.

To enable native JSON support you need to configure your event store to use the `jsonb` data type. You must also use the `EventStore.JsonbSerializer` serializer, to ensure event data and metadata is correctly serialized to JSON, and include the Postgres types module (`EventStore.PostgresTypes`) for the Postgrex library to support JSON.

```elixir
# config/config.exs
config :my_app, MyApp.EventStore,
  column_data_type: "jsonb",
  serializer: EventStore.JsonbSerializer,
  types: EventStore.PostgresTypes
```

Finally, you need to include the Jason library as a dependency in `mix.exs` to enable Postgrex JSON support and then run `mix deps.get` to install.

```elixir
# mix.exs
defp deps do
  [{:jason, "~> 1.2"}]
end
```

These settings must be configured *before* creating the EventStore database. It's not possible to migrate between `bytea` and `jsonb` data types once you've created the database. This must be decided in advance.

## Using with PgBouncer

EventStore uses `LISTEN/NOTIFY` and `pg_advisory_locks` Postgres capabilities. Unfortunately, they are not compatible with PgBouncer running in transaction (most typical) mode.

As a workaround, you can provide an additional `session_mode_url` parameter to the EventStore config:

```
config :my_app, MyApp.EventStore,
  url: "postgres://postgres:pgbouncer-in-transaction-mode@localhost/eventstore"
  session_mode_url: "postgres://postgres:pgbouncer-in-session-mode@localhost/eventstore"
```

This will allow the EventStore to use your regular pool settings to connect to the database defined in `url` for most database operations. It will separately establish connections using the `session_mode_url` where necessary which you should point to PgBouncer in session mode or connected directly to the Postgres instance.

```

### File: guides\Subscriptions.md
```md
# Subscriptions

There are two types of subscriptions provided by EventStore:

1. [Transient subscriptions](#transient-subscriptions) where new events are broadcast to subscribers immediately after they have been appended to storage.
2. [Persistent subscriptions](#persistent-subscriptions) which guarantee at-least-once delivery of every persisted event, provide back-pressure, and can be started, paused, and resumed from any position, including from the stream's origin.

## Event pub/sub

PostgreSQL's `LISTEN` and `NOTIFY` commands are used to pub/sub event notifications from the database. An after update trigger on the `streams` table is used to execute `NOTIFY` for each batch of inserted events. The notification payload contains the stream uuid, stream id, and first / last stream versions (e.g. `stream-12345,1,1,5`).

A single process will connect to the database to listen for these notifications. It fetches the event data and broadcasts to all interested subscriptions. This approach supports running an EventStore on multiple nodes, regardless of whether they are connected together to form a cluster using distributed Erlang. One connection per node is used for single node and multi-node deployments.

## Transient subscriptions

Use `c:EventStore.subscribe/2` to create a transient subscription to a single stream identified by its `stream_uuid`. Events will be received in batches as an `{:events, events}` message, where `events` is a collection of `EventStore.RecordedEvent` structs.

You can use `$all` as the stream identity to subscribe to events appended to all streams. With transient subscriptions you do not need to acknowledge receipt of the published events. The subscription will terminate when the subscriber process stops running.

#### Subscribe to single stream events

Subscribe to events appended to a *single* stream:

```elixir
alias MyApp.EventStore

:ok = EventStore.subscribe(stream_uuid)

# receive first batch of events
receive do
  {:events, events} ->
    IO.puts("Received events: " <> inspect(events))
end
```

#### Filtering events

You can provide an event selector function that filters each `RecordedEvent` before sending it to the subscriber:

```elixir
alias EventStore.RecordedEvent
alias MyApp.EventStore

EventStore.subscribe(stream_uuid, selector: fn
  %RecordedEvent{data: data} -> data != nil
end)

# receive first batch of mapped event data
receive do
  {:events, %RecordedEvent{} = event_data} ->
    IO.puts("Received non nil event data: " <> inspect(event_data))
end
```

#### Mapping events

You can provide an event mapping function that maps each `RecordedEvent` before sending it to the subscriber:

```elixir
alias EventStore.RecordedEvent
alias MyApp.EventStore

EventStore.subscribe(stream_uuid, mapper: fn
  %RecordedEvent{data: data} -> data
end)

# receive first batch of mapped event data
receive do
  {:events, event_data} ->
    IO.puts("Received event data: " <> inspect(event_data))
end
```

## Persistent subscriptions

Persistent subscriptions to a stream will guarantee *at least once* delivery of every persisted event. Each subscription may be independently paused, then later resumed from where it stopped. The last received and acknowledged event is stored by the EventStore to support resuming at a later time or whenever the subscriber process restarts.

A subscription can be created to receive events appended to a single or all streams.

Subscriptions must be uniquely named. By default a subscription only supports a single subscriber. Attempting to connect two subscribers to the same subscription will return `{:error, :subscription_already_exists}`. You can optionally create a [competing consumer subscription with multiple subscribers](#subscription-concurrency).

### `:subscribed` message

Once the subscription has successfully subscribed to the stream it will send the subscriber a `{:subscribed, subscription}` message. This indicates the subscription succeeded and you will begin receiving events.

Only one instance of a named subscription to a stream can connect to the database. This guarantees that starting the same subscription on each node when run on a cluster, or when running multiple single instance nodes, will only allow one subscription to actually connect. Therefore you can defer any initialisation until receipt of the `{:subscribed, subscription}` message to prevent duplicate effort by multiple nodes racing to create or subscribe to the same subscription.

### `:events` message

For each batch of events appended to the event store your subscriber will receive a `{:events, events}` message. The `events` list is a collection of `EventStore.RecordedEvent` structs.

### Subscription start from

By default subscriptions are created from the stream origin; they will receive all events from the stream. You can optionally specify a given start position:

- `:origin` - subscribe to events from the start of the stream (identical to using `0`). This is the default behaviour.
- `:current` - subscribe to events from the current version.
- `event_number` (integer) - specify an exact event number to subscribe from. This will be the same as the stream version for single stream subscriptions.

### Acknowledge received events

Receipt of each event by the subscriber must be acknowledged. This allows the subscription to resume on failure without missing an event and to indicate the subscription is ready to receive the next event.

The subscriber receives an `{:events, events}` tuple containing the published events. A subscription is returned when subscribing to the stream. This should be used to send the acknowledgement to using the `c:EventStore.ack/2` function:

 ```elixir
 alias MyApp.EventStore

 :ok = EventStore.ack(subscription, events)
 ```

A subscriber can confirm receipt of each event in a batch by sending multiple acks, one per event. The subscriber may confirm receipt of the last event in the batch in a single ack.

A subscriber will not receive further published events until it has confirmed receipt of all received events. This provides back pressure to the subscription to prevent the subscriber from being overwhelmed with messages if it cannot keep up. The subscription will buffer events until the subscriber is ready to receive, or an overflow occurs. At which point it will move into a catch-up mode and query events and replay them from storage until caught up.

#### Subscribe to all events

Subscribe to events appended to all streams:

```elixir
alias MyApp.EventStore

{:ok, subscription} = EventStore.subscribe_to_all_streams("example_all_subscription", self())

# Wait for the subscription confirmation
receive do
  {:subscribed, ^subscription} ->
    IO.puts("Successfully subscribed to all streams")
end

receive do
  {:events, events} ->
    IO.puts "Received events: #{inspect events}"

    # Acknowledge receipt
    :ok = EventStore.ack(subscription, events)
end
```

Unsubscribe from all streams:

```elixir
alias MyApp.EventStore

:ok = EventStore.unsubscribe_from_all_streams("example_all_subscription")
```

#### Subscribe to single stream events

Subscribe to events appended to a *single* stream:

```elixir
alias MyApp.EventStore

stream_uuid = EventStore.UUID.uuid4()
{:ok, subscription} = EventStore.subscribe_to_stream(stream_uuid, "example_single_subscription", self())

# Wait for the subscription confirmation
receive do
  {:subscribed, ^subscription} ->
    IO.puts("Successfully subscribed to single stream")
end

receive do
  {:events, events} ->
    # Process events & acknowledge receipt
    :ok = EventStore.ack(subscription, events)
end
```

Unsubscribe from a single stream:

```elixir
alias MyApp.EventStore

:ok = EventStore.unsubscribe_from_stream(stream_uuid, "example_single_subscription")
```

#### Start subscription from a given position

You can choose to receive events from a given starting position.

The supported options are:

  - `:origin` - Start receiving events from the beginning of the stream or all streams (default).
  - `:current` - Subscribe to newly appended events only, skipping already persisted events.
  - `event_number` (integer) - Specify an exact event number to subscribe from. This will be the same as the stream version for single stream subscriptions.

Example all stream subscription that will receive new events appended after the subscription has been created:

```elixir
alias MyApp.EventStore

{:ok, subscription} = EventStore.subscribe_to_all_streams("example_subscription", self(), start_from: :current)
```

#### Event Filtering

You can provide an event selector function that run in the subscription process, before sending the event to your mapper and subscriber. You can use this to filter events before dispatching to a subscriber.

Subscribe to all streams and provide a `selector` function that only sends data that the selector function returns `true` for.

```elixir
alias EventStore.RecordedEvent
alias MyApp.EventStore

selector = fn %RecordedEvent{event_number: event_number} ->
  rem(event_number) == 0
end

{:ok, subscription} = EventStore.subscribe_to_all_streams("example_subscription", self(), selector: selector)

# wait for the subscription confirmation
receive do
  {:subscribed, ^subscription} ->
    IO.puts("Successfully subscribed to all streams")
end

receive do
  {:events, filtered_events} ->
    # ... process events & ack receipt using last `event_number`
    RecordedEvent{event_number: event_number} = List.last(filtered_events)

    :ok = EventStore.ack(subscription, event_number)
end
```

#### Mapping events

You can provide an event mapping function that runs in the subscription process, before sending the event to your subscriber. You can use this to change the data received.

Subscribe to all streams and provide a `mapper` function that sends only the event data:

```elixir
alias EventStore.RecordedEvent
alias MyApp.EventStore

mapper = fn %RecordedEvent{event_number: event_number, data: data} ->
  {event_number, data}
end

{:ok, subscription} = EventStore.subscribe_to_all_streams("example_subscription", self(), mapper: mapper)

# wait for the subscription confirmation
receive do
  {:subscribed, ^subscription} ->
    IO.puts("Successfully subscribed to all streams")
end

receive do
  {:events, mapped_events} ->
    # ... process events & ack receipt using last `event_number`
    {event_number, _data} = List.last(mapped_events)

    :ok = EventStore.ack(subscription, event_number)
end
```

### Subscription concurrency

A single persistent subscription can support multiple subscribers. Events will be distributed to subscribers evenly using a round-robin algorithm. The [competing consumers pattern](https://docs.microsoft.com/en-us/azure/architecture/patterns/competing-consumers) enables multiple subscribers to process events concurrently to optimise throughput, to improve scalability and availability, and to balance the workload.

By default a subscription will only allow a single subscriber but you can opt-in to concurrent subscriptions be providing a non-negative `concurrency_limit` as a subscription option.

#### Subscription concurrency configuration options

- `concurrency_limit` defines the maximum number of concurrent subscribers allowed to connect to the subscription. By default only one subscriber may connect. If too many subscribers attempt to connect to the
  subscription an `{:error, :too_many_subscribers}` is returned.

- `buffer_size` limits how many in-flight events will be sent to the subscriber process before acknowledgement of successful processing. This limits the number of messages sent to the subscriber and stops their message queue from getting filled with events. Defaults to one in-flight event.

- `partition_by` is an optional function used to partition events to subscribers. It can be used to guarantee processing order when multiple subscribers have subscribed to a single subscription as described in [Ordering guarantee](#ordering-guarantee) below. The function is passed a single argument (an `EventStore.RecordedEvent` struct) and must return the partition key. As an example to guarantee events for a single stream are processed serially, but different streams are processed concurrently, you could use the `stream_uuid` as the partition key.

### Ordering guarantee

With multiple subscriber processes connected to a single subscription the ordering of event processing is no longer guaranteed since events may be processed in differing amounts of time. This can cause problems if your event handling code expects events to be processed in the order they were originally appended to a steam.

You can use a `partition_by` function to guarantee ordering of events within a particular group (e.g. per stream) but still allow events for different groups to be processed concurrently.


Partitioning gives you the benefits of competing consumers but still allows event ordering by partition where required.

#### Partition by example

```elixir
alias EventStore.RecordedEvent
alias MyApp.EventStore

by_stream = fn %RecordedEvent{stream_uuid: stream_uuid} -> stream_uuid end

{:ok, _subscription} =
  EventStore.subscribe_to_stream(stream_uuid, "example", self(),
    concurrency_limit: 10,
    partition_by: by_stream
  )
```

The above subscription would ensure that events for each stream are processed serially (by a single subscriber) in the order they were appended to the stream, but events for any other stream can be processed concurrently by another subscriber.

### Example persistent subscriber

Use a `GenServer` process to subscribe to the event store and track all notified events:

```elixir
# An example subscriber
defmodule Subscriber do
  use GenServer

  alias MyApp.EventStore

  def start_link do
    GenServer.start_link(__MODULE__, [])
  end

  def received_events(subscriber) do
    GenServer.call(subscriber, :received_events)
  end

  def init(events) do
    # Subscribe to events from all streams
    {:ok, subscription} = EventStore.subscribe_to_all_streams("example_subscription", self())

    {:ok, %{events: events, subscription: subscription}}
  end

  # Successfully subscribed to all streams
  def handle_info({:subscribed, subscription}, %{subscription: subscription} = state) do
    {:noreply, state}
  end

  # Event notification
  def handle_info({:events, events}, state) do
    %{events: existing_events, subscription: subscription} = state

    # Confirm receipt of received events
    :ok = EventStore.ack(subscription, events)

    {:noreply, %{state | events: existing_events ++ events}}
  end

  def handle_call(:received_events, _from, %{events: events} = state) do
    {:reply, events, state}
  end
end
```

Start your subscriber process, which subscribes to all streams in the event store:

```elixir
{:ok, subscriber} = Subscriber.start_link()
```

### Deleting a persistent subscription

You can delete a single stream or all stream subscription without requiring an active subscriber:

```elixir
alias MyApp
... [TRUNCATED]
```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.

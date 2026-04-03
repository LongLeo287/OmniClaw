---
id: github.com-otobus-event-bus-a238d4fd-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:10.031508
---

# KNOWLEDGE EXTRACT: github.com_otobus_event_bus_a238d4fd
> **Extracted on:** 2026-04-01 15:33:43
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007524599/github.com_otobus_event_bus_a238d4fd

---

## File: `.formatter.exs`
```
# Used by "mix format"
[
  inputs: ["{mix,.formatter}.exs", "{config,lib,test}/**/*.{ex,exs}"],
  line_length: 80
]
```

## File: `.gitignore`
```
# The directory Mix will write compiled artifacts to.
/_build/

# If you run "mix test --cover", coverage assets end up here.
/cover/

# The directory Mix downloads your dependencies sources to.
/deps/

# Where third-party dependencies like ExDoc output generated docs.
/doc/

# Ignore .fetch files in case you like to edit your project deps locally.
/.fetch

# If the VM crashes, it generates a dump, let's ignore it too.
erl_crash.dump

# Also ignore archive artifacts (built via "mix archive.build").
*.ez

# Ignore package tarball (built via "mix hex.build").
event_bus-*.tar

# Temporary files for e.g. tests.
/tmp/

# Misc.
.DS_Store
```

## File: `.travis.yml`
```yaml
language: elixir
elixir:
  - 1.13
otp_release:
  - 20.0
matrix:
  include:
    - elixir: 1.13
      otp_release: 24.0
env:
  - MIX_ENV=test
script:
  - mix dialyzer
  - mix coveralls.travis
  - mix credo --strict
  - mix test
```

## File: `CHANGELOG.md`
```markdown
# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

## [1.7.X] 2022-01-02
- Doc enhancements by @kianmeng
- Apply credo library suggestions
- Fix warnings for the new elixir version 1.13

## [1.6.X] 2020-01-20

- Update type names and docs for consistent naming convention (Note: there is no logic or method name change)
- Update the Travis script to prevent breaks on merges:
- - Include dialyzer warnings
- - Include coverage
- - Include credo checks
- Update `EventBus.Model.Event` struct optional attribute type specs to allow `nil` values
- Update license year
- Change `EventBus.Service.Store.fetch` to return a safe value when ETS data is missing and log it

## [1.5.X] 2018.09.27

- Fix Elixir `v1.7.x` warnings for string to atom conversions
- Remove deprecated `EventBus.Util.String` module
- Move the time calculation logic into the new `MonotonicTime` utility module
- Set `initialized_at` value on `EventSource` helper to a monotonically increasing time
- Enhance tests for the `:second` time unit
- Enhance tests for the `unique_id` generator

## [1.4.X] 2018.09.07

- Add public types to main module to increase type safety and readability
- Remove allowence of passing string on topic registration/deregistration
- Allow passing `event_shadow` to `mark_as_completed/1` and `mark_as_skipped/1`
- Update wrong spec for unsubscribe/1
- Add more test for unsubscribe/1
- Add questions section
- Change default `@eb_tme_unit` to `:microsecond`
- Change all instances of `micro_seconds` and `microseconds` to `microsecond`, as per Erlang 19+
- Fix dialyzer warnings
- Update the id generator source in test configuration

## [1.3.X] 2018.08.04

- Set default transaction to the id
- Delegate optional variables to optional library configuration when building/notifying events with Event builder
- Add random id generator for Event builder
- Introduce `fetch_event_data` function to fetch only event data
- Log empty topic subscribers
- Add missing tests for existence check
- Update time spent calculation for EventSource block
- Remove support for system event tracing (Update the wiki to create wrapper for system event tracing)
- Dialyzer enhancements
- Test and documentation enhancements

## [1.2.X] 2018.02.24

- Remove support for system event tracing for `notify` action (unnecessary)
- Move internal modules under managers namespace for better documentation
- Add `subscribed?` function to check subscriptions

## [1.1.X] 2018.02.21

- Optional system events which notify the `eb_action_called` topic for the actions: `notify`, `register_topic`, `unregister_topic`, `subscribe`, `unsubscribe`, `mark_as_completed`, `mark_as_skipped`
- Add public exist? function to Topic, Watcher, and Store
- Check existence of topic in a blocking manner
- Register/Unregister topic in a blocking manner

## [1.0.0] 2018.01.23

- Move build and notify blocks into EventSource
- Add use keyword for Source for developer friendly require and aliases
- Split GenServers and Services
- Move utility functions into its own module
- Add addons section to README
- Switch to microseconds when auto event structuring with `EventSource` to increase compatibility with Zipkin and Datadog APM
- Error topic introduced for dynamic event builder/notifier with `EventSource`. Now you can pass `:error_topic` key, EvetSource automatically check the result of execution block for `{:error, _}` tuple and create an event structure for the given `:error_topic`.
- Add elixir formatter config to format code

## [0.9.0] 2018.01.06

- Add `source` attribute to increase traceability
- Add optional configuration to Subscriber to use the same module/function with different configurations to process the event. The aim of this change is increasing re-useability of the subscriber with several configurations. For example, this will allow writing an HTTP consumer or an AWS lambda caller function with different configurations.

## [0.8.0] 2018.01.06

- Register/unregister topics on-demand (`EventBus.register_topic/1` and `EventBus.unregister/1`)
- Add block/yield builder for Event with auto `initialized_at` and `occurred_at` attribute assignments
- Add block/yield notifier for delivering/notifying events creation with same benefits of build block
- Add changelog file

## [0.7.0] 2018.01.06

- Add `initialized_at` attribute
```

## File: `CODE_OF_CONDUCT.md`
```markdown
# Contributor Code of Conduct

As contributors and maintainers of this project, and in the interest of fostering an open and welcoming community, we pledge to respect all people who contribute through reporting issues, posting feature requests, updating documentation, submitting pull requests or patches, and other activities.

We are committed to making participation in this project a harassment-free experience for everyone, regardless of level of experience, gender, gender identity and expression, sexual orientation, disability, personal appearance, body size, race, ethnicity, age, religion, or nationality.

Examples of unacceptable behavior by participants include:

* The use of sexualized language or imagery
* Unwelcome sexual advances
* Discrimination based on age, disability, gender, nationality, race, religion, sexuality, or similar personal characteristic
* Personal attacks
* Trolling or insulting/derogatory comments
* Public or private harassment
* Bullying or systematic harassment
* Publishing other's private information, such as physical or electronic addresses, without explicit permission
* Other unethical or unprofessional conduct
* Insulting, demeaning, hateful, or threatening remarks
* Incitement to any of these

Project maintainers have the right and responsibility to remove, edit, or reject comments, commits, code, wiki edits, issues, and other contributions that are not aligned to this Code of Conduct. By adopting this Code of Conduct, project maintainers commit themselves to fairly and consistently applying these principles to every aspect of managing this project. Project maintainers who do not follow or enforce the Code of Conduct may be permanently removed from the project team.

This code of conduct applies both within project spaces and in public spaces when an individual is representing the project or its community.

Instances of abusive, harassing, or otherwise unacceptable behavior may be reported by opening an issue or contacting one or more of the project maintainers.

This Code of Conduct is adapted from the [Contributor Covenant][1], version 1.2.0, available at [http://contributor-covenant.org/version/1/2/0/][2].

[1]: http://contributor-covenant.org
[2]: http://contributor-covenant.org/version/1/2/0/
```

## File: `CONTRIBUTING.md`
```markdown
# Contributing

## Issues, Bugs, Documentation, Enhancements

Create an issue if there is a bug.

Fork the project.

Make your improvements and write your tests(make sure you covered all the cases).

Make a pull request.
```

## File: `LICENSE.md`
```markdown
MIT License

Copyright (c) 2022 Mustafa Turan

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

## File: `PULL_REQUEST_TEMPLATE.md`
```markdown
//cc @otobus @mustafaturan

### Description
...

### Changes

- [ ] Change 1 
- [ ] Change 2
- [ ] ...

### Is it ready?

- [ ] Created an issue and defined what the problem is
- [ ] Fixed the defined issue
- [ ] The changes have only one commit (if possible please answer the why question with your commit message, and ofcourse a commit may have multiple messages)
- [ ] The changes don't break current functionality
- [ ] All tests are covered and passing travis
- [ ] Used Elixir formatter for only modified file and fixed any of them breaks current consistency. 
- [ ] Added specs and docs if a new function introduced
- [ ] Updated specs and docs if changed any params of a function
- [ ] Updated changelog
- [ ] Updated readme
- [ ] Didn't bump the version

### References

- Issue #
```

## File: `QUESTIONS.md`
```markdown
# Questions

In case you have a question, please create [stackoverflow](https://stackoverflow.com/) question with `#elixir-eventbus` hashtag and ping me from twitter handler [`@mustafaturan`](https://twitter.com/mustafaturan).
```

## File: `README.md`
```markdown
# EventBus

[![Build Status](https://travis-ci.org/otobus/event_bus.svg?branch=master)](https://travis-ci.org/otobus/event_bus)
[![Module Version](https://img.shields.io/hexpm/v/event_bus.svg)](https://hex.pm/packages/event_bus)
[![Hex Docs](https://img.shields.io/badge/hex-docs-lightgreen.svg)](https://hexdocs.pm/event_bus/)
[![Total Download](https://img.shields.io/hexpm/dt/event_bus.svg)](https://hex.pm/packages/event_bus)
[![License](https://img.shields.io/hexpm/l/event_bus.svg)](https://github.com/otobus/event_bus/blob/master/LICENSE)
[![Last Updated](https://img.shields.io/github/last-commit/otobus/event_bus.svg)](https://github.com/otobus/event_bus/commits/master)

Traceable, extendable and minimalist event bus implementation for Elixir with built-in event store and event watcher based on ETS.

![Event Bus](https://cdn-images-1.medium.com/max/1600/1*0fcfAiHvNeHCRYhp-a32YA.png)

## Table of Contents

[Features](#features)

[Getting Started](#getting-started)

[Installation](#installation)

[Usage](#usage)

- [Register event topics in `config.exs`](#register-event-topics-in-configexs)

- [Register/unregister event topics on demand](#registerunregister-event-topics-on-demand)

- [Subscribe to the 'event bus' with a subscriber and list of given topics](#subscribe-to-the-event-bus-with-a-subscriber-and-list-of-given-topics-notification-manager-will-match-with-regex)

- [Unsubscribe from the 'event bus'](#unsubscribe-from-the-event-bus)

- [List subscribers](#list-subscribers)

- [List subscribers of a specific event](#list-subscribers-of-a-specific-event)

- [Event data structure](#event-data-structure)

- [Define an event struct](#event-data-structure)

- [Notify all subscribers with `EventBus.Model.Event` data](#notify-all-subscribers-with-eventbusmodelevent-data)

- [Fetch an event from the store](#fetch-an-event-from-the-store)

- [Mark as completed on Event Observation Manager](#mark-as-completed-on-event-observation-manager)

- [Mark as skipped on Event Observation Manager](#mark-as-skipped-on-event-observation-manager)

- [Check if a topic exists?](#check-if-a-topic-exists)

- [Use block builder to build `EventBus.Model.Event` struct](#use-block-builder-to-build-eventbusmodelevent-struct)

- [Use block notifier to notify event data to given topic](#use-block-notifier-to-notify-event-data-to-given-topic)

[Sample Subscriber Implementation](#sample-subscriber-implementation)

[Event Storage Details](#event-storage-details)

[Traceability](#traceability)

[EventBus.Metrics and UI](#eventbusmetrics-library)

[Documentation](#documentation)

[Addons](#addons)

[Wiki](https://github.com/otobus/event_bus/wiki)

[Contributing](./CONTRIBUTING.md)

[License](./LICENSE.md)

[Code of Conduct](./CODE_OF_CONDUCT.md)

[Questions](./QUESTIONS.md)

## Features

- Fast data writes with enabled concurrent writes to ETS.

- Fast data reads with enabled concurrent reads from ETS.

- Fast by design. Almost all implementation data accesses have O(1) complexity.

- Memory friendly. Instead of pushing event data, pushes event shadow(event id and topic) to only interested subscribers.

- Applies [queueing theory](https://www.vividcortex.com/resources/queueing-theory) to handle inputs.

- Extendable with addons.

- Traceable with optional attributes. Optional attributes compatible with opentracing platform.

- Minimal with required attributes(In case, you want it work minimal use 3 required attributes to deliver your events).

## Getting Started

Start using `event_bus` library in five basic steps:

- [1: Installing Library Package](https://github.com/otobus/event_bus/wiki/Installing-Library-Package)
- [2: Creating/Registering Topics](https://github.com/otobus/event_bus/wiki/Creating-(Registering)-Topics)
- [3: Emitting/Dispatching an Event](https://github.com/otobus/event_bus/wiki/Emitting-(Dispatching)-an-Event)
- [4: Creating Simple Event Consumers/Listeners/Subscribers](https://github.com/otobus/event_bus/wiki/Creating-Event-Consumers)
- [5: Subscribing Consumer/Listener/Subscriber for a Topic](https://github.com/otobus/event_bus/wiki/Subscribing-Consumers-to-Topic(s))

## Installation

The package can be installed by adding `:event_bus` to your list of dependencies in `mix.exs`:

```elixir
def deps do
  [
    {:event_bus, "~> 1.7.0"}
  ]
end
```

Be sure to include `event_bus` in your `mix.exs` Mixfile:

```elixir
def application do
  [
    applications: [
      # ...
      :event_bus
    ]
  ]
end
```

## Usage

##### Register event topics in `config.exs`

```elixir
config :event_bus, topics: [:message_received, :another_event_occurred]
```

##### Register/unregister event topics on demand
```elixir
# register
EventBus.register_topic(:webhook_received)
> :ok

# unregister topic
# Warning: It also deletes the related topic tables!
EventBus.unregister_topic(:webhook_received)
> :ok
```

##### Subscribe to the 'event bus' with a subscriber and list of given topics, `Notification Manager` will match with Regex

```elixir
# to catch every event topic
EventBus.subscribe({MyEventSubscriber, [".*"]})
> :ok

# to catch specific topics
EventBus.subscribe({MyEventSubscriber, ["purchase_", "booking_confirmed$", "flight_passed$"]})
> :ok

# if your subscriber has a config
config = %{}
subscriber = {MyEventSubscriber, config}
EventBus.subscribe({subscriber, [".*"]})
> :ok
```

##### Unsubscribe from the 'event bus'
```elixir
EventBus.unsubscribe(MyEventSubscriber)
> :ok

# if your subscriber has a config
config = %{}
EventBus.unsubscribe({MyEventSubscriber, config})
> :ok
```

##### List subscribers
```elixir
EventBus.subscribers()
> [{MyEventSubscriber, [".*"]}, {{AnotherSubscriber, %{}}, [".*"]}]
```

##### List subscribers of a specific event
```elixir
EventBus.subscribers(:hello_received)
> [MyEventSubscriber, {{AnotherSubscriber, %{}}}]
```

##### Event data structure

Data structure for `EventBus.Model.Event`

```elixir
%EventBus.Model.Event{
  id: String.t | integer(), # required
  transaction_id: String.t | integer(), # optional
  topic: atom(), # required
  data: any() # required,
  initialized_at: integer(), # optional, might be seconds, milliseconds or microseconds even nanoseconds since Elixir does not have a limit on integer size
  occurred_at: integer(), # optional, might be seconds, milliseconds or microseconds even nanoseconds since Elixir does not have a limit on integer size
  source: String.t, # optional, source of the event, who created it
  ttl: integer() # optional, might be seconds, milliseconds or microseconds even nanoseconds since Elixir does not have a limit on integer size. If `ttl` field is set, it is recommended to set `occurred_at` field too.
}
```

**`transaction_id` attribute**

Firstly, `transaction_id` attribute is an optional field, if you need to store any meta identifier related to event transaction, it is the place to store. Secondly, `transaction_id` is one of the good ways to track events related to the same transaction on a chain of events. If you have time, have a look to the [story](https://hackernoon.com/trace-monitor-chain-of-microservice-logs-in-the-same-transaction-f13420f2d42c).

**`initialized_at` attribute**

Optional, but good to have field for all events to track when the event generator started to process for generating this event.

**`occurred_at` attribute**

Optional, but good to have field for all events to track when the event occurred with unix timestamp value. The library does not automatically set this value since the value depends on the timing choice.

**`ttl` attribute**

Optional, but might to have field for all events to invalidate an event after a certain amount of time. Currently, the `event_bus` library does not do any specific thing using this field. If you need to discard an event in a certain amount of time, that field would be very useful.

Note: If you set this field, then `occurred_at` field is required.

##### Define an event struct

```elixir
alias EventBus.Model.Event
event = %Event{id: "123", transaction_id: "1",
  topic: :hello_received, data: %{message: "Hello"}}
another_event = %Event{id: "124", transaction_id: "1",
  topic: :bye_received, data: [user_id: 1, goal: "exit"]}
```
**Important Note:** It is important to have unique identifier for each event struct per topic. I recommend to use a unique id generator like `{:uuid, "~> 1.1"}`.

##### Notify all subscribers with `EventBus.Model.Event` data
```elixir
EventBus.notify(event)
> :ok
EventBus.notify(another_event)
> :ok
```

##### Fetch an event from the store
```elixir
topic = :bye_received
id = "124"
EventBus.fetch_event({topic, id})
> %EventBus.Model.Event{data: [user_id: 1, goal: "exit"], id: "124", topic: :bye_received, transaction_id: "1"}

# To fetch only the event data
EventBus.fetch_event_data({topic, id})
> [user_id: 1, goal: "exit"]
```

##### Mark as completed on Event Observation Manager
```elixir
subscriber = MyEventSubscriber
# If your subscriber has config then pass tuple
subscriber = {MyEventSubscriber, config}
EventBus.mark_as_completed({subscriber, {:bye_received, id}})
> :ok
```

##### Mark as skipped on Event Observation Manager
```elixir
subscriber = MyEventSubscriber
# If your subscriber has config then pass tuple
subscriber = {MyEventSubscriber, config}
EventBus.mark_as_skipped({subscriber, {:bye_received, id}})
> :ok
```

##### Check if a topic exists?
```elixir
EventBus.topic_exist?(:metrics_updated)
> false
```

##### Use block builder to build `EventBus.Model.Event` struct

Builder automatically sets `initialized_at` and `occurred_at` attributes
```elixir
use EventBus.EventSource

id = "some unique id"
topic = :user_created
transaction_id = "tx" # optional
ttl = 600_000 # optional
source = "my event creator" # optional

params = %{id: id, topic: topic, transaction_id: transaction_id, ttl: ttl, source: source}
EventSource.build(params) do
  # do some calc in here
  Process.sleep(1)
  # as a result return only the event data
  %{email: "jd@example.com", name: "John Doe"}
end
> %EventBus.Model.Event{data: %{email: "jd@example.com", name: "John Doe"},
 id: "some unique id", initialized_at: 1515274599140491,
 occurred_at: 1515274599141211, source: "my event creator", topic: :user_created, transaction_id: "tx", ttl: 600000}
```

It is recommended to set optional params in event_bus application config, this will allow you to auto generate majority of optional values without writing code. Here is a sample config for event_bus:

```elixir
config :event_bus,
  topics: [], # list of atoms
  ttl: 30_000_000, # integer
  time_unit: :microsecond, # atom
  id_generator: EventBus.Util.Base62 # module: must implement 'unique_id/0' function
```

After having such config like above, you can generate events without providing optional attributes like below:

```elixir
# Without optional params
params = %{topic: topic}
EventSource.build(params) do
  %{email: "jd@example.com", name: "John Doe"}
end
> %EventBus.Model.Event{data: %{email: "jd@example.com", name: "John Doe"},
 id: "Ewk7fL6Erv0vsW6S", initialized_at: 1515274599140491,
 occurred_at: 1515274599141211, source: "AutoModuleName", topic: :user_created,
 transaction_id: nil, ttl: 30_000_000}

# With optional error topic param
params = %{id: id, topic: topic, error_topic: :user_create_erred}
EventSource.build(params) do
  {:error, %{email: "Invalid format"}}
end
> %EventBus.Model.Event{data: {:error, %{email: "Invalid format"}},
 id: "some unique id", initialized_at: 1515274599140491,
 occurred_at: 1515274599141211, source: nil, topic: :user_create_erred,
 transaction_id: nil, ttl: 30_000_000}
```

##### Use block notifier to notify event data to given topic

Builder automatically sets `initialized_at` and `occurred_at` attributes
```elixir
use EventBus.EventSource

id = "some unique id"
topic = :user_created
error_topic = :user_create_erred # optional (in case error tuple return in yield execution, it will use :error_topic value as :topic for event creation)
transaction_id = "tx" # optional
ttl = 600_000 # optional
source = "my event creator" # optional
EventBus.register_topic(topic) # in case you didn't register it in `config.exs`

params = %{id: id, topic: topic, transaction_id: transaction_id, ttl: ttl, source: source, error_topic: error_topic}
EventSource.notify(params) do
  # do some calc in here
  # as a result return only the event data
  %{email: "mrsjd@example.com", name: "Mrs Jane Doe"}
end
> # it automatically calls notify method with event data and return only event data as response
> %{email: "mrsjd@example.com", name: "Mrs Jane Doe"}
```

### Sample Subscriber Implementation

```elixir
defmodule MyEventSubscriber do
  ...

  # if your subscriber does not have a config
  def process({topic, id} = event_shadow) do
    GenServer.cast(__MODULE__, event_shadow)
    :ok
  end

  ...

  # if your subscriber has a config
  def process({config, topic, id} = event_shadow_with_conf) do
    GenServer.cast(__MODULE__, event_shadow_with_conf)
    :ok
  end

  ...


  # if your subscriber does not have a config
  def handle_cast({:bye_received, id} = event_shadow, state) do
    event = EventBus.fetch_event(event_shadow)
    # do sth with event

    # update the watcher!
    # version >= 1.4.0
    EventBus.mark_as_completed({__MODULE__, event_shadow})
    # all versions
    EventBus.mark_as_completed({__MODULE__, :bye_received, id})
    ...
    {:noreply, state}
  end

  def handle_cast({:hello_received, id} = event_shadow, state) do
    event = EventBus.fetch_event({:hello_received, id})
    # do sth with EventBus.Model.Event

    # update the watcher!
    # version >= 1.4.0
    EventBus.mark_as_completed({__MODULE__, event_shadow})
    # all versions
    EventBus.mark_as_completed({__MODULE__, :hello_received, id})
    ...
    {:noreply, state}
  end

  def handle_cast({topic, id} = event_shadow, state) do
    # version >= 1.4.0
    EventBus.mark_as_skipped({__MODULE__, event_shadow})

    # all versions
    EventBus.mark_as_skipped({__MODULE__, topic, id})
    {:noreply, state}
  end

  ...

  # if your subscriber has a config
  def handle_cast({config, :bye_received, id}, state) do
    event = EventBus.fetch_event({:bye_received, id})
    # do sth with event

    # update the watcher!
    subscriber = {__MODULE__, config}
    EventBus.mark_as_completed({subscriber, :bye_received, id})
    ...
    {:noreply, state}
  end

  def handle_cast({config, :hello_received, id}, state) do
    event = EventBus.fetch_event({:hello_received, id})
    # do sth with EventBus.Model.Event

    # update the watcher!
    subscriber = {__MODULE__, config}
    EventBus.mark_as_completed({subscriber, :hello_received, id})
    ...
    {:noreply, state}
  end

  def handle_cast({config, topic, id}, state) do
    subscriber = {__MODULE__, config}
    EventBus.mark_as_skipped({subscriber, topic, id})
    {:noreply, state}
  end

  ...
end
```

## Event Storage Details

When an event configured in `config` file, 2 ETS tables will be created for the event on app start.

All event data is temporarily saved to the ETS tables with the name `:eb_es_<<topic>>` until all subscribers processed the data. This table is a read heavy table. When a subscriber needs to process the event data, it queries this table to fetch event data.

To watch event status, a separate watcher table is created for each event type with the name `:eb_ew_<<topic>>`. This table is used for keeping the status of the event. `Observation Manager` updates this table frequently with the notification of the event subscribers.

When all subscribers process the event data, data in the event store and watcher, automatically deleted by the `Observation Manager`. If you need to see the status of unprocessed events, event watcher table is one of the good places to query.

For example; to get the list unprocessed events for `:hello_received` event:

```elixir
# The following command will return a list of tuples with the `id`, and `event_subscribers_list` where `subscribers` is the list of event subscribers, `completers` is the subscribers those processed the event and notified `Observation Manager`, and lastly `skippers` is the subscribers those skipped the event without processing.

# Assume you have an event with the name ':hello_received'
:ets.tab2list(:eb_ew_hello_received)
> [{id, {subscribers, completers, skippers}}, ...]
```

ETS storage SHOULD NOT be considered as a persistent storage. If you need to store events to a persistent data store, then subscribe to all event types by a module with `[".*"]` event topic then save every event data.

For example;

```elixir
EventBus.subscribe({MyDataStore, [".*"]})

# then in your data store save the event
defmodule MyDataStore do
  ...

  def process({topic, id} = event_shadow) do
    GenServer.cast(__MODULE__, event_shadow)
    :ok
  end

  ...

  def handle_cast({topic, id}, state) do
    event = EventBus.fetch_event({topic, id})
    # write your logic to save event_data to a persistent store

    EventBus.mark_as_completed({__MODULE__, {topic, id}})
    {:noreply, state}
  end
end
```

## Traceability

EventBus comes with a good enough data structure to track the event life cycle with its optional parameters. For a traceable system, it is highly recommend to fill optional fields on event data. It is also encouraged to use `EventSource.notify` block/yield to automatically set the `initialized_at` and `occurred_at` values.

### System Events

This feature removed with the version 1.3 to keep the core library simple. If you need to trace system events please check the sample wrapper implementation from the [wiki page](https://github.com/otobus/event_bus/wiki/Tracing-System-Events).

### EventBus.Metrics Library

EventBus has some addons to extend its optional functionalities. One of them is `event_bus_metrics` library which comes with a UI, RESTful endpoints and SSE streams to provide instant metrics for event_bus topics.

[EventBus.Metrics Instructions](https://github.com/otobus/event_bus/wiki/EventBus-Metrics-and-UI)

## Documentation

- [Wiki](https://github.com/otobus/event_bus/wiki)

- [Module docs](https://hexdocs.pm/event_bus)

- [The story](https://medium.com/@mustafaturan/event-bus-implementation-s-d2854a9fafd5)

## Addons

A few sample addons listed below. Please do not hesitate to add your own addon to the list.

| Addon Name           | Description   | Link          | Docs          |
| -------------------- | ------------- | ------------- | ------------- |
| `event_bus_postgres` | Fast event consumer to persist `event_bus` events to Postgres using GenStage          | [Github](https://github.com/otobus/event_bus_postgres) | [HexDocs](https://hexdocs.pm/event_bus_postgres) |
| `event_bus_logger`   | Deadly simple log subscriber implementation                                             | [Github](https://github.com/otobus/event_bus_logger)   | [HexDocs](https://hexdocs.pm/event_bus_logger)   |
| `event_bus_metrics`  | Metrics UI and metrics API endpoints for EventBus events for debugging and monitoring | [Hex](https://hex.pm/packages/event_bus_metrics)       | [HexDocs](https://hexdocs.pm/event_bus_metrics)  |

Note: The addons under [https://github.com/otobus](https://github.com/otobus) organization implemented as a sample, but feel free to use them in your project with respecting their licenses.

## Copyright and License

MIT

Copyright (c) 2022 Mustafa Turan

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```

## File: `_config.yml`
```yaml
theme: jekyll-theme-cayman
```

## File: `coveralls.json`
```json
{
  "skip_files": [
    "test/support",
    "lib/event_bus.ex"
  ],
  "custom_stop_words": [
    "defdelegate"
  ]
}
```

## File: `mix.exs`
```
defmodule EventBus.Mixfile do
  use Mix.Project

  @source_url "https://github.com/otobus/event_bus"
  @version "1.7.0"

  def project do
    [
      app: :event_bus,
      version: @version,
      elixir: "~> 1.5",
      elixirc_paths: elixirc_paths(Mix.env()),
      build_embedded: Mix.env() == :prod,
      start_permanent: Mix.env() == :prod,
      package: package(),
      deps: deps(),
      docs: docs(),
      dialyzer: [plt_add_deps: :transitive],
      test_coverage: [tool: ExCoveralls]
    ]
  end

  def application do
    # Specify extra applications you'll use from Erlang/Elixir
    [
      extra_applications: [:logger, :crypto],
      mod: {EventBus.Application, []}
    ]
  end

  defp elixirc_paths(:test) do
    ["lib", "test/support"]
  end

  defp elixirc_paths(_) do
    ["lib"]
  end

  defp deps do
    [
      {:credo, "~> 1.6", only: [:dev, :test]},
      {:dialyxir, "~> 1.0", only: [:dev, :test], runtime: false},
      {:excoveralls, "~> 0.13", only: [:test]},
      {:ex_doc, ">= 0.0.0", only: [:dev], runtime: false}
    ]
  end

  defp description do
    """
    Traceable, extendable and minimalist event bus implementation for Elixir
    with built-in event store and event watcher based on ETS
    """
  end

  defp package do
    [
      name: :event_bus,
      description: description(),
      files: ["lib", "mix.exs", "README.md", "CHANGELOG.md", "LICENSE.md"],
      maintainers: ["Mustafa Turan"],
      licenses: ["MIT"],
      links: %{
        "Changelog" => "https://hexdocs.pm/event_bus/changelog.html",
        "GitHub" => @source_url
      }
    ]
  end

  defp docs do
    [
      extras: [
        "CHANGELOG.md": [title: "Changelog"],
        "CONTRIBUTING.md": [title: "Contributing"],
        "CODE_OF_CONDUCT.md": [title: "Code of Conduct"],
        "LICENSE.md": [title: "License"],
        "QUESTIONS.md": [title: "Questions"],
        "README.md": [title: "Overview"]
      ],
      main: "readme",
      source_url: @source_url,
      source_ref: "v#{@version}",
      formatters: ["html"]
    ]
  end
end
```

## File: `mix.lock`
```
%{
  "bunt": {:hex, :bunt, "0.2.0", "951c6e801e8b1d2cbe58ebbd3e616a869061ddadcc4863d0a2182541acae9a38", [:mix], [], "hexpm", "7af5c7e09fe1d40f76c8e4f9dd2be7cebd83909f31fee7cd0e9eadc567da8353"},
  "certifi": {:hex, :certifi, "2.8.0", "d4fb0a6bb20b7c9c3643e22507e42f356ac090a1dcea9ab99e27e0376d695eba", [:rebar3], [], "hexpm", "6ac7efc1c6f8600b08d625292d4bbf584e14847ce1b6b5c44d983d273e1097ea"},
  "credo": {:hex, :credo, "1.6.1", "7dc76dcdb764a4316c1596804c48eada9fff44bd4b733a91ccbf0c0f368be61e", [:mix], [{:bunt, "~> 0.2.0", [hex: :bunt, repo: "hexpm", optional: false]}, {:file_system, "~> 0.2.8", [hex: :file_system, repo: "hexpm", optional: false]}, {:jason, "~> 1.0", [hex: :jason, repo: "hexpm", optional: false]}], "hexpm", "698607fb5993720c7e93d2d8e76f2175bba024de964e160e2f7151ef3ab82ac5"},
  "dialyxir": {:hex, :dialyxir, "1.1.0", "c5aab0d6e71e5522e77beff7ba9e08f8e02bad90dfbeffae60eaf0cb47e29488", [:mix], [{:erlex, ">= 0.2.6", [hex: :erlex, repo: "hexpm", optional: false]}], "hexpm", "07ea8e49c45f15264ebe6d5b93799d4dd56a44036cf42d0ad9c960bc266c0b9a"},
  "earmark_parser": {:hex, :earmark_parser, "1.4.18", "e1b2be73eb08a49fb032a0208bf647380682374a725dfb5b9e510def8397f6f2", [:mix], [], "hexpm", "114a0e85ec3cf9e04b811009e73c206394ffecfcc313e0b346de0d557774ee97"},
  "erlex": {:hex, :erlex, "0.2.6", "c7987d15e899c7a2f34f5420d2a2ea0d659682c06ac607572df55a43753aa12e", [:mix], [], "hexpm", "2ed2e25711feb44d52b17d2780eabf998452f6efda104877a3881c2f8c0c0c75"},
  "ex_doc": {:hex, :ex_doc, "0.26.0", "1922164bac0b18b02f84d6f69cab1b93bc3e870e2ad18d5dacb50a9e06b542a3", [:mix], [{:earmark_parser, "~> 1.4.0", [hex: :earmark_parser, repo: "hexpm", optional: false]}, {:makeup_elixir, "~> 0.14", [hex: :makeup_elixir, repo: "hexpm", optional: false]}, {:makeup_erlang, "~> 0.1", [hex: :makeup_erlang, repo: "hexpm", optional: false]}], "hexpm", "2775d66e494a9a48355db7867478ffd997864c61c65a47d31c4949459281c78d"},
  "excoveralls": {:hex, :excoveralls, "0.14.4", "295498f1ae47bdc6dce59af9a585c381e1aefc63298d48172efaaa90c3d251db", [:mix], [{:hackney, "~> 1.16", [hex: :hackney, repo: "hexpm", optional: false]}, {:jason, "~> 1.0", [hex: :jason, repo: "hexpm", optional: false]}], "hexpm", "e3ab02f2df4c1c7a519728a6f0a747e71d7d6e846020aae338173619217931c1"},
  "file_system": {:hex, :file_system, "0.2.10", "fb082005a9cd1711c05b5248710f8826b02d7d1784e7c3451f9c1231d4fc162d", [:mix], [], "hexpm", "41195edbfb562a593726eda3b3e8b103a309b733ad25f3d642ba49696bf715dc"},
  "hackney": {:hex, :hackney, "1.18.0", "c4443d960bb9fba6d01161d01cd81173089686717d9490e5d3606644c48d121f", [:rebar3], [{:certifi, "~>2.8.0", [hex: :certifi, repo: "hexpm", optional: false]}, {:idna, "~>6.1.0", [hex: :idna, repo: "hexpm", optional: false]}, {:metrics, "~>1.0.0", [hex: :metrics, repo: "hexpm", optional: false]}, {:mimerl, "~>1.1", [hex: :mimerl, repo: "hexpm", optional: false]}, {:parse_trans, "3.3.1", [hex: :parse_trans, repo: "hexpm", optional: false]}, {:ssl_verify_fun, "~>1.1.0", [hex: :ssl_verify_fun, repo: "hexpm", optional: false]}, {:unicode_util_compat, "~>0.7.0", [hex: :unicode_util_compat, repo: "hexpm", optional: false]}], "hexpm", "9afcda620704d720db8c6a3123e9848d09c87586dc1c10479c42627b905b5c5e"},
  "idna": {:hex, :idna, "6.1.1", "8a63070e9f7d0c62eb9d9fcb360a7de382448200fbbd1b106cc96d3d8099df8d", [:rebar3], [{:unicode_util_compat, "~>0.7.0", [hex: :unicode_util_compat, repo: "hexpm", optional: false]}], "hexpm", "92376eb7894412ed19ac475e4a86f7b413c1b9fbb5bd16dccd57934157944cea"},
  "jason": {:hex, :jason, "1.3.0", "fa6b82a934feb176263ad2df0dbd91bf633d4a46ebfdffea0c8ae82953714946", [:mix], [{:decimal, "~> 1.0 or ~> 2.0", [hex: :decimal, repo: "hexpm", optional: true]}], "hexpm", "53fc1f51255390e0ec7e50f9cb41e751c260d065dcba2bf0d08dc51a4002c2ac"},
  "makeup": {:hex, :makeup, "1.0.5", "d5a830bc42c9800ce07dd97fa94669dfb93d3bf5fcf6ea7a0c67b2e0e4a7f26c", [:mix], [{:nimble_parsec, "~> 0.5 or ~> 1.0", [hex: :nimble_parsec, repo: "hexpm", optional: false]}], "hexpm", "cfa158c02d3f5c0c665d0af11512fed3fba0144cf1aadee0f2ce17747fba2ca9"},
  "makeup_elixir": {:hex, :makeup_elixir, "0.15.2", "dc72dfe17eb240552857465cc00cce390960d9a0c055c4ccd38b70629227e97c", [:mix], [{:makeup, "~> 1.0", [hex: :makeup, repo: "hexpm", optional: false]}, {:nimble_parsec, "~> 1.1", [hex: :nimble_parsec, repo: "hexpm", optional: false]}], "hexpm", "fd23ae48d09b32eff49d4ced2b43c9f086d402ee4fd4fcb2d7fad97fa8823e75"},
  "makeup_erlang": {:hex, :makeup_erlang, "0.1.1", "3fcb7f09eb9d98dc4d208f49cc955a34218fc41ff6b84df7c75b3e6e533cc65f", [:mix], [{:makeup, "~> 1.0", [hex: :makeup, repo: "hexpm", optional: false]}], "hexpm", "174d0809e98a4ef0b3309256cbf97101c6ec01c4ab0b23e926a9e17df2077cbb"},
  "metrics": {:hex, :metrics, "1.0.1", "25f094dea2cda98213cecc3aeff09e940299d950904393b2a29d191c346a8486", [:rebar3], [], "hexpm", "69b09adddc4f74a40716ae54d140f93beb0fb8978d8636eaded0c31b6f099f16"},
  "mimerl": {:hex, :mimerl, "1.2.0", "67e2d3f571088d5cfd3e550c383094b47159f3eee8ffa08e64106cdf5e981be3", [:rebar3], [], "hexpm", "f278585650aa581986264638ebf698f8bb19df297f66ad91b18910dfc6e19323"},
  "nimble_parsec": {:hex, :nimble_parsec, "1.2.0", "b44d75e2a6542dcb6acf5d71c32c74ca88960421b6874777f79153bbbbd7dccc", [:mix], [], "hexpm", "52b2871a7515a5ac49b00f214e4165a40724cf99798d8e4a65e4fd64ebd002c1"},
  "parse_trans": {:hex, :parse_trans, "3.3.1", "16328ab840cc09919bd10dab29e431da3af9e9e7e7e6f0089dd5a2d2820011d8", [:rebar3], [], "hexpm", "07cd9577885f56362d414e8c4c4e6bdf10d43a8767abb92d24cbe8b24c54888b"},
  "ssl_verify_fun": {:hex, :ssl_verify_fun, "1.1.6", "cf344f5692c82d2cd7554f5ec8fd961548d4fd09e7d22f5b62482e5aeaebd4b0", [:make, :mix, :rebar3], [], "hexpm", "bdb0d2471f453c88ff3908e7686f86f9be327d065cc1ec16fa4540197ea04680"},
  "unicode_util_compat": {:hex, :unicode_util_compat, "0.7.0", "bc84380c9ab48177092f43ac89e4dfa2c6d62b40b8bd132b1059ecc7232f9a78", [:rebar3], [], "hexpm", "25eee6d67df61960cf6a794239566599b09e17e668d3700247bc498638152521"},
}
```

## File: `config/config.exs`
```
import Config

import_config "#{Mix.env()}.exs"
```

## File: `config/dev.exs`
```
import Config
```

## File: `config/prod.exs`
```
import Config
```

## File: `config/test.exs`
```
import Config

config :event_bus,
  topics: [:metrics_received, :metrics_summed],
  ttl: 30_000_000,
  time_unit: :microsecond,
  id_generator: EventBus.Util.Base62
```

## File: `lib/event_bus.ex`
```
defmodule EventBus do
  @moduledoc """
  Traceable, extendable and minimalist event bus implementation for Elixir with
  built-in event store and event observation manager based on ETS.
  """

  alias EventBus.Manager.{
    Notification,
    Observation,
    Store,
    Subscription,
    Topic
  }

  alias EventBus.Model.Event

  @typedoc "EventBus.Model.Event struct"
  @type event :: Event.t()

  @typedoc "Event id"
  @type event_id :: String.t() | integer()

  @typedoc "Tuple of topic name and event id"
  @type event_shadow :: {topic(), event_id()}

  @typedoc "Event subscriber"
  @type subscriber :: subscriber_without_config() | subscriber_with_config()

  @typedoc "Subscriber configuration"
  @type subscriber_config :: any()

  @typedoc "List of event subscribers"
  @type subscribers :: list(subscriber())

  @typedoc "Event subscriber with config"
  @type subscriber_with_config :: {module(), subscriber_config()}

  @typedoc "Tuple of subscriber and event reference"
  @type subscriber_with_event_ref ::
          subscriber_with_event_shadow() | subscriber_with_topic_and_event_id()

  @typedoc "Tuple of subscriber and event shadow"
  @type subscriber_with_event_shadow :: {subscriber(), event_shadow()}

  @typedoc "Tuple of subscriber, topic and event id"
  @type subscriber_with_topic_and_event_id ::
          {subscriber(), topic(), event_id()}

  @typedoc "Tuple of subscriber and list of topic patterns"
  @type subscriber_with_topic_patterns :: {subscriber(), topic_patterns()}

  @typedoc "Event subscriber without config"
  @type subscriber_without_config :: module()

  @typedoc "Topic name"
  @type topic :: atom()

  @typedoc "List of topic names"
  @type topics :: list(topic())

  @typedoc "Regex pattern to match topic name"
  @type topic_pattern :: String.t()

  @typedoc "List of topic patterns"
  @type topic_patterns :: list(topic_pattern())

  @doc """
  Send an event to all subscribers.

  ## Examples

      event = %Event{id: 1, topic: :webhook_received,
        data: %{"message" => "Hi all!"}}
      EventBus.notify(event)
      :ok

  """
  @spec notify(event()) :: :ok
  defdelegate notify(event),
    to: Notification,
    as: :notify

  @doc """
  Check if a topic registered.

  ## Examples

      EventBus.topic_exist?(:demo_topic)
      true

  """
  @spec topic_exist?(topic()) :: boolean()
  defdelegate topic_exist?(topic),
    to: Topic,
    as: :exist?

  @doc """
  List all the registered topics.

  ## Examples

      EventBus.topics()
      [:metrics_summed]

  """
  @spec topics() :: topics()
  defdelegate topics,
    to: Topic,
    as: :all

  @doc """
  Register a topic.

  ## Examples

      EventBus.register_topic(:demo_topic)
      :ok

  """
  @spec register_topic(topic()) :: :ok
  defdelegate register_topic(topic),
    to: Topic,
    as: :register

  @doc """
  Unregister a topic.

  ## Examples

      EventBus.unregister_topic(:demo_topic)
      :ok

  """
  @spec unregister_topic(topic()) :: :ok
  defdelegate unregister_topic(topic),
    to: Topic,
    as: :unregister

  @doc """
  Subscribe a subscriber to the event bus.

  ## Examples

      EventBus.subscribe({MyEventSubscriber, [".*"]})
      :ok

      # For configurable subscribers you can pass tuple of subscriber and config
      my_config = %{}
      EventBus.subscribe({{OtherSubscriber, my_config}, [".*"]})
      :ok

  """
  @spec subscribe(subscriber_with_topic_patterns()) :: :ok
  defdelegate subscribe(subscriber_with_topic_patterns),
    to: Subscription,
    as: :subscribe

  @doc """
  Unsubscribe a subscriber from the event bus.

  ## Examples

      EventBus.unsubscribe(MyEventSubscriber)
      :ok

      # For configurable subscribers you must pass tuple of subscriber and config
      my_config = %{}
      EventBus.unsubscribe({OtherSubscriber, my_config})
      :ok

  """
  @spec unsubscribe(subscriber()) :: :ok
  defdelegate unsubscribe(subscriber),
    to: Subscription,
    as: :unsubscribe

  @doc """
  Check if the given subscriber subscribed to the event bus for the given topic
  patterns.

  ## Examples

      EventBus.subscribe({MyEventSubscriber, [".*"]})
      :ok

      EventBus.subscribed?({MyEventSubscriber, [".*"]})
      true

      EventBus.subscribed?({MyEventSubscriber, ["some_initialized"]})
      false

      EventBus.subscribed?({AnothEventSubscriber, [".*"]})
      false

  """
  @spec subscribed?(subscriber_with_topic_patterns()) :: boolean()
  defdelegate subscribed?(subscriber_with_topic_patterns),
    to: Subscription,
    as: :subscribed?

  @doc """
  List the subscribers.

  ## Examples

      EventBus.subscribers()
      [MyEventSubscriber]

      # One usual and one configured subscriber with its config
      EventBus.subscribers()
      [MyEventSubscriber, {OtherSubscriber, %{}}]

  """
  @spec subscribers() :: subscribers()
  defdelegate subscribers,
    to: Subscription,
    as: :subscribers

  @doc """
  List the subscribers for the given topic.

  ## Examples

      EventBus.subscribers(:metrics_received)
      [MyEventSubscriber]

      # One usual and one configured subscriber with its config
      EventBus.subscribers(:metrics_received)
      [MyEventSubscriber, {OtherSubscriber, %{}}]

  """
  @spec subscribers(topic()) :: subscribers()
  defdelegate subscribers(topic),
    to: Subscription,
    as: :subscribers

  @doc """
  Fetch an event.

  ## Examples

      EventBus.fetch_event({:hello_received, "123"})
      %EventBus.Model.Model{}

  """
  @spec fetch_event(event_shadow()) :: event() | nil
  defdelegate fetch_event(event_shadow),
    to: Store,
    as: :fetch

  @doc """
  Fetch an event's data.

  ## Examples

      EventBus.fetch_event_data({:hello_received, "123"})

  """
  @spec fetch_event_data(event_shadow()) :: any()
  defdelegate fetch_event_data(event_shadow),
    to: Store,
    as: :fetch_data

  @doc """
  Mark the event as completed for the subscriber.

  ## Examples

      topic        = :hello_received
      event_id     = "124"
      event_shadow = {topic, event_id}

      # For regular subscribers
      EventBus.mark_as_completed({MyEventSubscriber, event_shadow})

      # For configurable subscribers you must pass tuple of subscriber and config
      my_config = %{}
      subscriber  = {OtherSubscriber, my_config}

      EventBus.mark_as_completed({subscriber, event_shadow})
      :ok

  """
  @spec mark_as_completed(subscriber_with_event_ref()) :: :ok
  defdelegate mark_as_completed(subscriber_with_event_ref),
    to: Observation,
    as: :mark_as_completed

  @doc """
  Mark the event as skipped for the subscriber.

  ## Examples

      EventBus.mark_as_skipped({MyEventSubscriber, {:unmatched_occurred, "124"}})

      # For configurable subscribers you must pass tuple of subscriber and config
      my_config = %{}
      subscriber  = {OtherSubscriber, my_config}
      EventBus.mark_as_skipped({subscriber, {:unmatched_occurred, "124"}})
      :ok

  """
  @spec mark_as_skipped(subscriber_with_event_ref()) :: :ok
  defdelegate mark_as_skipped(subscriber_with_event_ref),
    to: Observation,
    as: :mark_as_skipped
end
```

## File: `lib/event_bus/application.ex`
```
defmodule EventBus.Application do
  @moduledoc false

  use Application
  alias EventBus.Manager.{
    Notification,
    Observation,
    Store,
    Subscription,
    Topic
  }

  def start(_type, _args) do
    import Supervisor.Spec, warn: false

    children = [
      %{
        id: make_ref(),
        restart: :permanent,
        start: {Topic, :start_link, []}
      },
      %{
        id: make_ref(),
        restart: :permanent,
        start: {Subscription, :start_link, []}
      },
      %{
        id: make_ref(),
        restart: :permanent,
        start: {Notification, :start_link, []}
      },
      %{
        id: make_ref(),
        restart: :permanent,
        start: {Store, :start_link, []}
      },
      %{
        id: make_ref(),
        restart: :permanent,
        start: {Observation, :start_link, []}
      }
    ]

    opts = [strategy: :one_for_one, name: EventBus.Supervisor]
    link = Supervisor.start_link(children, opts)
    register_topics()
    link
  end

  defp register_topics do
    Topic.register_from_config()
  end
end
```

## File: `lib/event_bus/event_source.ex`
```
defmodule EventBus.EventSource do
  @moduledoc """
  Event builder and notifier blocks/yields for EventBus.
  """

  alias EventBus.Model.Event
  alias EventBus.Util.MonotonicTime
  alias __MODULE__

  defmacro __using__(_) do
    quote do
      require EventBus.EventSource

      alias EventBus.EventSource
      alias EventBus.Model.Event
      alias EventBus.Util.Base62

      @eb_app :event_bus
      @eb_source String.replace("#{__MODULE__}", "Elixir.", "")
    end
  end

  @doc """
  Dynamic event builder block with auto setters.

  It auto sets `:id`, `:transaction_id`, `:source`, `:ttl`, `:initialized_at`,
  and `:occurred_at` fields when they are not provided in the params.
  """
  defmacro build(params, do: yield) do
    quote do
      initialized_at = MonotonicTime.now()
      params = unquote(params)

      {topic, data} =
        case unquote(yield) do
          {:error, error} ->
            {params[:error_topic] || params[:topic], {:error, error}}

          result ->
            {params[:topic], result}
        end

      eb_ttl = Application.get_env(@eb_app, :ttl)
      eb_id_gen = Application.get_env(@eb_app, :id_generator, Base62)
      id = Map.get(params, :id, eb_id_gen.unique_id())

      %Event{
        id: id,
        topic: topic,
        transaction_id: Map.get(params, :transaction_id, id),
        data: data,
        initialized_at: initialized_at,
        occurred_at: MonotonicTime.now(),
        source: Map.get(params, :source, @eb_source),
        ttl: Map.get(params, :ttl, eb_ttl)
      }
    end
  end

  @doc """
  Dynamic event emitter block with auto setters.

  It auto sets `:id`, `:transaction_id`, `:source`, `:ttl`, `:initialized_at`,
  and `:occurred_at` fields when they are not provided in the params.
  """
  defmacro notify(params, do: yield) do
    quote do
      event =
        EventSource.build unquote(params) do
          unquote(yield)
        end

      EventBus.notify(event)
      event.data
    end
  end
end
```

## File: `lib/event_bus/managers/notification.ex`
```
defmodule EventBus.Manager.Notification do
  @moduledoc false

  ###########################################################################
  # Notification is responsible for saving events, creating event watcher and
  # delivering events to subscribers.
  ###########################################################################

  use GenServer

  alias EventBus.Model.Event
  alias EventBus.Service.Notification, as: NotificationService

  @typep event :: EventBus.event()

  @backend NotificationService

  @doc false
  def start_link do
    GenServer.start_link(__MODULE__, nil, name: __MODULE__)
  end

  @doc false
  def init(args) do
    {:ok, args}
  end

  @doc """
  Notify event to event.topic subscribers in the current node
  """
  @spec notify(event()) :: :ok
  def notify(%Event{} = event) do
    GenServer.cast(__MODULE__, {:notify, event})
  end

  ###########################################################################
  # PRIVATE API
  ###########################################################################

  @doc false
  @spec handle_cast({:notify, event()}, term()) :: no_return()
  def handle_cast({:notify, event}, state) do
    @backend.notify(event)
    {:noreply, state}
  end
end
```

## File: `lib/event_bus/managers/observation.ex`
```
defmodule EventBus.Manager.Observation do
  @moduledoc false

  ###########################################################################
  # Event Observation module is a helper to get info for the events and also an
  # organizer for the events happened in time. It automatically deletes
  # processed events from the ETS table. Event subscribers are responsible for
  # notifying the Event Observation on completions and skips.
  ###########################################################################

  use GenServer

  alias EventBus.Service.Observation, as: ObservationService

  @typep event_shadow :: EventBus.event_shadow()
  @typep subscribers :: EventBus.subscribers()
  @typep subscribers_with_event_shadow :: {subscribers(), event_shadow()}
  @typep subscriber_with_event_ref :: EventBus.subscriber_with_event_ref()
  @typep topic :: EventBus.topic()
  @typep watcher :: {subscribers(), subscribers(), subscribers()}

  @backend ObservationService

  @doc false
  def start_link do
    GenServer.start_link(__MODULE__, nil, name: __MODULE__)
  end

  @doc false
  def init(args) do
    {:ok, args}
  end

  @doc """
  Check if the topic exists?
  It's important to keep this in blocking manner to prevent double creations in
  sub modules
  """
  @spec exist?(topic()) :: boolean()
  def exist?(topic) do
    GenServer.call(__MODULE__, {:exist?, topic})
  end

  @doc """
  Register a topic to the watcher
  """
  @spec register_topic(topic()) :: :ok
  def register_topic(topic) do
    GenServer.call(__MODULE__, {:register_topic, topic})
  end

  @doc """
  Unregister a topic from the watcher
  """
  @spec unregister_topic(topic()) :: :ok
  def unregister_topic(topic) do
    GenServer.call(__MODULE__, {:unregister_topic, topic})
  end

  @doc """
  Mark event as completed on the watcher
  """
  @spec mark_as_completed(subscriber_with_event_ref()) :: :ok
  def mark_as_completed({subscriber, topic, id}) do
    GenServer.cast(__MODULE__, {:mark_as_completed, {subscriber, {topic, id}}})
  end

  def mark_as_completed({subscriber, {topic, id}}) do
    GenServer.cast(__MODULE__, {:mark_as_completed, {subscriber, {topic, id}}})
  end

  @doc """
  Mark event as skipped on the watcher
  """
  @spec mark_as_skipped(subscriber_with_event_ref()) :: :ok
  def mark_as_skipped({subscriber, topic, id}) do
    GenServer.cast(__MODULE__, {:mark_as_skipped, {subscriber, {topic, id}}})
  end

  def mark_as_skipped({subscriber, {topic, id}}) do
    GenServer.cast(__MODULE__, {:mark_as_skipped, {subscriber, {topic, id}}})
  end

  @doc """
  Create an watcher
  """
  @spec create(subscribers_with_event_shadow()) :: :ok
  def create({subscribers, {topic, id}}) do
    GenServer.call(__MODULE__, {:save, {topic, id}, {subscribers, [], []}})
  end

  ###########################################################################
  # DELEGATIONS
  ###########################################################################

  @doc """
  Fetch the watcher
  """
  @spec fetch(event_shadow()) :: any()
  defdelegate fetch(event_shadow),
    to: @backend,
    as: :fetch

  ###########################################################################
  # PRIVATE API
  ###########################################################################

  @doc false
  @spec handle_call({:register_topic, topic()}, any(), term())
    :: {:reply, :ok, term()}
  def handle_call({:register_topic, topic}, _from, state) do
    @backend.register_topic(topic)
    {:reply, :ok, state}
  end

  @spec handle_call({:unregister_topic, topic()}, any(), term())
    :: {:reply, :ok, term()}
  def handle_call({:unregister_topic, topic}, _from, state) do
    @backend.unregister_topic(topic)
    {:reply, :ok, state}
  end

  @doc false
  @spec handle_call({:exist?, topic()}, any(), term())
    :: {:reply, boolean(), term()}
  def handle_call({:exist?, topic}, _from, state) do
    {:reply, @backend.exist?(topic), state}
  end

  @doc false
  @spec handle_call({:save, event_shadow(), watcher()}, any(), term())
    :: {:reply, :ok, term()}
  def handle_call({:save, {topic, id}, watcher}, _from, state) do
    @backend.save({topic, id}, watcher)
    {:reply, :ok, state}
  end

  @doc false
  @spec handle_cast({:mark_as_completed, subscriber_with_event_ref()}, term())
    :: no_return()
  def handle_cast({:mark_as_completed, {subscriber, {topic, id}}}, state) do
    @backend.mark_as_completed({subscriber, {topic, id}})
    {:noreply, state}
  end

  @doc false
  @spec handle_cast({:mark_as_skipped, subscriber_with_event_ref()}, term())
    :: no_return()
  def handle_cast({:mark_as_skipped, {subscriber, {topic, id}}}, state) do
    @backend.mark_as_skipped({subscriber, {topic, id}})
    {:noreply, state}
  end
end
```

## File: `lib/event_bus/managers/store.ex`
```
defmodule EventBus.Manager.Store do
  @moduledoc false

  ###########################################################################
  # Event store is a storage handler for events. It allows to create and delete
  # stores for a topic. And allows fetching, deleting and saving events for the
  # topic.
  ###########################################################################

  use GenServer

  alias EventBus.Model.Event
  alias EventBus.Service.Store, as: StoreService

  @typep event :: EventBus.event()
  @typep event_shadow :: EventBus.event_shadow()
  @typep topic :: EventBus.topic()

  @backend StoreService

  @doc false
  def start_link do
    GenServer.start_link(__MODULE__, nil, name: __MODULE__)
  end

  @doc false
  def init(args) do
    {:ok, args}
  end

  @doc """
  Check if the topic exists?
  It's important to keep this in blocking manner to prevent double creations in
  sub modules
  """
  @spec exist?(topic()) :: boolean()
  def exist?(topic) do
    GenServer.call(__MODULE__, {:exist?, topic})
  end

  @doc """
  Register a topic to the store
  """
  @spec register_topic(topic()) :: :ok
  def register_topic(topic) do
    GenServer.call(__MODULE__, {:register_topic, topic})
  end

  @doc """
  Unregister the topic from the store
  """
  @spec unregister_topic(topic()) :: :ok
  def unregister_topic(topic) do
    GenServer.call(__MODULE__, {:unregister_topic, topic})
  end

  @doc """
  Save an event to the store
  """
  @spec create(event()) :: :ok
  def create(%Event{} = event) do
    GenServer.call(__MODULE__, {:create, event})
  end

  @doc """
  Delete an event from the store
  """
  @spec delete(event_shadow()) :: :ok
  def delete({topic, id}) do
    GenServer.cast(__MODULE__, {:delete, {topic, id}})
  end

  ###########################################################################
  # DELEGATIONS
  ###########################################################################

  @doc """
  Fetch an event from the store
  """
  @spec fetch(event_shadow()) :: event() | nil
  defdelegate fetch(event_shadow),
    to: @backend,
    as: :fetch

  @doc """
  Fetch an event's data from the store
  """
  @spec fetch_data(event_shadow()) :: any()
  defdelegate fetch_data(event_shadow),
    to: @backend,
    as: :fetch_data

  ###########################################################################
  # PRIVATE API
  ###########################################################################

  @doc false
  @spec handle_call({:register_topic, topic()}, any(), term())
    :: {:reply, :ok, term()}
  def handle_call({:register_topic, topic}, _from, state) do
    @backend.register_topic(topic)
    {:reply, :ok, state}
  end

  @spec handle_call({:unregister_topic, topic()}, any(), term())
    :: {:reply, :ok, term()}
  def handle_call({:unregister_topic, topic}, _from, state) do
    @backend.unregister_topic(topic)
    {:reply, :ok, state}
  end

  @doc false
  @spec handle_call({:exist?, topic()}, any(), term())
    :: {:reply, boolean(), term()}
  def handle_call({:exist?, topic}, _from, state) do
    {:reply, @backend.exist?(topic), state}
  end

  @doc false
  @spec handle_call({:create, event()}, any(), term()) :: no_return()
  def handle_call({:create, event}, _from, state) do
    @backend.create(event)
    {:reply, :ok, state}
  end

  @spec handle_cast({:delete, event_shadow()}, term()) :: no_return()
  def handle_cast({:delete, {topic, id}}, state) do
    @backend.delete({topic, id})
    {:noreply, state}
  end
end
```

## File: `lib/event_bus/managers/subscription.ex`
```
defmodule EventBus.Manager.Subscription do
  @moduledoc false

  ###########################################################################
  # Subscription manager
  ###########################################################################

  use GenServer

  alias EventBus.Service.Subscription, as: SubscriptionService

  @typep subscriber :: EventBus.subscriber()
  @typep subscribers :: EventBus.subscribers()
  @typep subscriber_with_topic_patterns :: EventBus.subscriber_with_topic_patterns()
  @typep topic :: EventBus.topic()

  @backend SubscriptionService

  @doc false
  def start_link do
    GenServer.start_link(__MODULE__, nil, name: __MODULE__)
  end

  @doc false
  def init(args) do
    {:ok, args}
  end

  @doc """
  Does the subscriber subscribe to topic_patterns?
  """
  @spec subscribed?(subscriber_with_topic_patterns()) :: boolean()
  def subscribed?({_subscriber, _topic_patterns} = subscriber) do
    GenServer.call(__MODULE__, {:subscribed?, subscriber})
  end

  @doc """
  Subscribe the subscriber to topic_patterns
  """
  @spec subscribe(subscriber_with_topic_patterns()) :: :ok
  def subscribe({subscriber, topic_patterns}) do
    GenServer.cast(__MODULE__, {:subscribe, {subscriber, topic_patterns}})
  end

  @doc """
  Unsubscribe the subscriber
  """
  @spec unsubscribe(subscriber()) :: :ok
  def unsubscribe(subscriber) do
    GenServer.cast(__MODULE__, {:unsubscribe, subscriber})
  end

  @doc """
  Set subscribers to the topic
  """
  @spec register_topic(topic()) :: :ok
  def register_topic(topic) do
    GenServer.cast(__MODULE__, {:register_topic, topic})
  end

  @doc """
  Unset subscribers from the topic
  """
  @spec unregister_topic(topic()) :: :ok
  def unregister_topic(topic) do
    GenServer.cast(__MODULE__, {:unregister_topic, topic})
  end

  ###########################################################################
  # DELEGATIONS
  ###########################################################################

  @doc """
  Fetch subscribers
  """
  @spec subscribers() :: subscribers()
  defdelegate subscribers,
    to: @backend,
    as: :subscribers

  @doc """
  Fetch subscribers of the topic
  """
  @spec subscribers(topic()) :: subscribers()
  defdelegate subscribers(topic),
    to: @backend,
    as: :subscribers

  ###########################################################################
  # PRIVATE API
  ###########################################################################

  @doc false
  @spec handle_call({:subscribed?, subscriber_with_topic_patterns()}, any(), term())
    :: {:reply, boolean(), term()}
  def handle_call({:subscribed?, subscriber}, _from, state) do
    {:reply, @backend.subscribed?(subscriber), state}
  end

  @doc false
  @spec handle_cast({:subscribe, subscriber_with_topic_patterns()}, term())
    :: no_return()
  def handle_cast({:subscribe, {subscriber, topic_patterns}}, state) do
    @backend.subscribe({subscriber, topic_patterns})
    {:noreply, state}
  end

  @doc false
  @spec handle_cast({:unsubscribe, subscriber()}, term()) :: no_return()
  def handle_cast({:unsubscribe, subscriber}, state) do
    @backend.unsubscribe(subscriber)
    {:noreply, state}
  end

  @doc false
  @spec handle_cast({:register_topic, topic()}, term()) :: no_return()
  def handle_cast({:register_topic, topic}, state) do
    @backend.register_topic(topic)
    {:noreply, state}
  end

  @doc false
  @spec handle_cast({:unregister_topic, topic()}, term()) :: no_return()
  def handle_cast({:unregister_topic, topic}, state) do
    @backend.unregister_topic(topic)
    {:noreply, state}
  end
end
```

## File: `lib/event_bus/managers/topic.ex`
```
defmodule EventBus.Manager.Topic do
  @moduledoc false

  ###########################################################################
  # Topic manager
  ###########################################################################

  use GenServer

  alias EventBus.Service.Topic, as: TopicService

  @typep topic :: EventBus.topic()
  @typep topics :: EventBus.topics()

  @backend TopicService

  @doc false
  def start_link do
    GenServer.start_link(__MODULE__, nil, name: __MODULE__)
  end

  @doc false
  def init(args) do
    {:ok, args}
  end

  @doc """
  Check if the topic exists?
  It's important to keep this in blocking manner to prevent double creations in
  sub modules
  """
  @spec exist?(topic()) :: boolean()
  def exist?(topic) do
    GenServer.call(__MODULE__, {:exist?, topic})
  end

  @doc """
  Register a topic
  """
  @spec register(topic()) :: :ok
  def register(topic) do
    GenServer.call(__MODULE__, {:register, topic})
  end

  @doc """
  Unregister a topic
  """
  @spec unregister(topic()) :: :ok
  def unregister(topic) do
    GenServer.call(__MODULE__, {:unregister, topic})
  end

  ###########################################################################
  # DELEGATIONS
  ###########################################################################

  @doc """
  List all registered topics
  """
  @spec all() :: topics()
  defdelegate all,
    to: @backend,
    as: :all

  @doc """
  Register all topics from config
  """
  @spec register_from_config() :: :ok
  defdelegate register_from_config,
    to: @backend,
    as: :register_from_config

  ###########################################################################
  # PRIVATE API
  ###########################################################################

  @doc false
  @spec handle_call({:exist?, topic()}, any(), term())
    :: {:reply, boolean(), term()}
  def handle_call({:exist?, topic}, _from, state) do
    {:reply, @backend.exist?(topic), state}
  end

  @doc false
  @spec handle_call({:register, topic()}, any(), term()) :: {:reply, :ok, term()}
  def handle_call({:register, topic}, _from, state) do
    @backend.register(topic)
    {:reply, :ok, state}
  end

  @doc false
  @spec handle_call({:unregister, topic()}, any(), term())
    :: {:reply, :ok, term()}
  def handle_call({:unregister, topic}, _from, state) do
    @backend.unregister(topic)
    {:reply, :ok, state}
  end
end
```

## File: `lib/event_bus/models/event.ex`
```
defmodule EventBus.Model.Event do
  @moduledoc """
  Structure and type for Event model.
  """

  @enforce_keys [:id, :topic, :data]

  defstruct [
    :id,
    :transaction_id,
    :topic,
    :data,
    :initialized_at,
    :occurred_at,
    :source,
    :ttl
  ]

  @typedoc """
  Definition of the Event struct.

  * :id - Identifier
  * :transaction_id - Transaction identifier, if event belongs to a transaction
  * :topic - Topic name
  * :data - Context
  * :initialized_at - When the process initialized to generate this event
  * :occurred_at - When it is occurred
  * :source - Who created this event: module, function or service name are good
  * :ttl - Time to live value
  """
  @type t :: %__MODULE__{
          id: String.t() | integer(),
          transaction_id: String.t() | integer() | nil,
          topic: atom(),
          data: any(),
          initialized_at: integer() | nil,
          occurred_at: integer() | nil,
          source: String.t() | nil,
          ttl: integer() | nil
        }

  @doc """
  Calculates the duration of the event, and simple answer of how long does it
  take to generate this event.
  """
  @spec duration(__MODULE__.t()) :: integer()
  def duration(%__MODULE__{
        initialized_at: initialized_at,
        occurred_at: occurred_at
      })
      when is_integer(initialized_at) and is_integer(occurred_at) do
    occurred_at - initialized_at
  end

  def duration(%__MODULE__{}) do
    0
  end
end
```

## File: `lib/event_bus/services/notification.ex`
```
defmodule EventBus.Service.Notification do
  @moduledoc false

  require Logger

  alias EventBus.Manager.Observation, as: ObservationManager
  alias EventBus.Manager.Store, as: StoreManager
  alias EventBus.Manager.Subscription, as: SubscriptionManager
  alias EventBus.Model.Event

  @typep event :: EventBus.event()
  @typep event_shadow :: EventBus.event_shadow()
  @typep subscriber :: EventBus.subscriber()
  @typep subscribers :: EventBus.subscribers()
  @typep topic :: EventBus.topic()

  @doc false
  @spec notify(event()) :: :ok
  def notify(%Event{id: id, topic: topic} = event) do
    subscribers = SubscriptionManager.subscribers(topic)

    if subscribers == [] do
      warn_missing_topic_subscription(topic)
    else
      :ok = StoreManager.create(event)
      :ok = ObservationManager.create({subscribers, {topic, id}})

      notify_subscribers(subscribers, {topic, id})
    end

    :ok
  end

  @spec notify_subscribers(subscribers(), event_shadow()) :: :ok
  defp notify_subscribers(subscribers, event_shadow) do
    Enum.each(subscribers, fn subscriber ->
      notify_subscriber(subscriber, event_shadow)
    end)
    :ok
  end

  @spec notify_subscriber(subscriber(), event_shadow()) :: no_return()
  defp notify_subscriber({subscriber, config}, {topic, id}) do
    subscriber.process({config, topic, id})
  rescue
    error ->
      log_error(subscriber, error)
      ObservationManager.mark_as_skipped({{subscriber, config}, {topic, id}})
  end

  defp notify_subscriber(subscriber, {topic, id}) do
    subscriber.process({topic, id})
  rescue
    error ->
      log_error(subscriber, error)
      ObservationManager.mark_as_skipped({subscriber, {topic, id}})
  end

  @spec registration_status(topic()) :: String.t()
  defp registration_status(topic) do
    if EventBus.topic_exist?(topic), do: "", else: " doesn't exist!"
  end

  @spec warn_missing_topic_subscription(topic()) :: no_return()
  defp warn_missing_topic_subscription(topic) do
    msg =
      "Topic(:#{topic}#{registration_status(topic)}) doesn't have subscribers"

    Logger.warn(msg)
  end

  @spec log_error(module(), any()) :: no_return()
  defp log_error(subscriber, error) do
    msg = "#{subscriber}.process/1 raised an error!\n#{inspect(error)}"
    Logger.info(msg)
  end
end
```

## File: `lib/event_bus/services/observation.ex`
```
defmodule EventBus.Service.Observation do
  @moduledoc false

  require Logger

  alias EventBus.Manager.Store, as: StoreManager
  alias :ets, as: Ets

  @typep event_shadow :: EventBus.event_shadow()
  @typep subscribers :: EventBus.subscribers()
  @typep subscriber_with_event_ref :: EventBus.subscriber_with_event_ref()
  @typep topic :: EventBus.topic()
  @typep watcher :: {subscribers(), subscribers(), subscribers()}

  @ets_opts [
    :set,
    :public,
    :named_table,
    {:write_concurrency, true},
    {:read_concurrency, true}
  ]
  @prefix "eb_ew_"

  @doc false
  @spec exist?(topic()) :: boolean()
  def exist?(topic) do
    table_name = table_name(topic)
    all_tables = Ets.all()
    Enum.any?(all_tables, fn table -> table == table_name end)
  end

  @doc false
  @spec register_topic(topic()) :: :ok
  def register_topic(topic) do
    unless exist?(topic), do: Ets.new(table_name(topic), @ets_opts)
    :ok
  end

  @doc false
  @spec unregister_topic(topic()) :: :ok
  def unregister_topic(topic) do
    if exist?(topic), do: Ets.delete(table_name(topic))
    :ok
  end

  @doc false
  @spec mark_as_completed(subscriber_with_event_ref()) :: :ok
  def mark_as_completed({subscriber, event_shadow}) do
    case fetch(event_shadow) do
      {subscribers, completers, skippers} ->
        save_or_delete(event_shadow, {subscribers, [subscriber | completers], skippers})
        nil -> :ok
    end
  end

  @doc false
  @spec mark_as_skipped(subscriber_with_event_ref()) :: :ok
  def mark_as_skipped({subscriber, event_shadow}) do
    case fetch(event_shadow) do
      {subscribers, completers, skippers} ->
        save_or_delete(event_shadow, {subscribers, completers, [subscriber | skippers]})
      nil -> :ok
    end
  end

  @doc false
  @spec fetch(event_shadow()) :: {subscribers(), subscribers(), subscribers()} | nil
  def fetch({topic, id}) do
    case Ets.lookup(table_name(topic), id) do
      [{_, data}] -> data
      _ ->
        Logger.log(:info, fn ->
          "[EVENTBUS][OBSERVATION]\s#{topic}.#{id}.ets_fetch_error"
        end)

        nil
    end
  end

  @doc false
  @spec save(event_shadow(), watcher()) :: :ok
  def save({topic, id}, watcher) do
    save_or_delete({topic, id}, watcher)
  end

  @spec complete?(watcher()) :: boolean()
  defp complete?({subscribers, completers, skippers}) do
    length(subscribers) == length(completers) + length(skippers)
  end

  @spec save_or_delete(event_shadow(), watcher()) :: :ok
  defp save_or_delete({topic, id}, watcher) do
    if complete?(watcher) do
      delete_with_relations({topic, id})
    else
      Ets.insert(table_name(topic), {id, watcher})
    end

    :ok
  end

  @spec delete_with_relations(event_shadow()) :: :ok
  defp delete_with_relations({topic, id}) do
    StoreManager.delete({topic, id})
    Ets.delete(table_name(topic), id)

    :ok
  end

  @spec table_name(topic()) :: atom()
  defp table_name(topic) do
    String.to_atom("#{@prefix}#{topic}")
  end
end
```

## File: `lib/event_bus/services/store.ex`
```
defmodule EventBus.Service.Store do
  @moduledoc false

  require Logger

  alias EventBus.Model.Event
  alias :ets, as: Ets

  @typep event :: EventBus.event()
  @typep event_shadow :: EventBus.event_shadow()
  @typep topic :: EventBus.topic()

  @ets_opts [:set, :public, :named_table, {:read_concurrency, true}]
  @prefix "eb_es_"

  @doc false
  @spec exist?(topic()) :: boolean()
  def exist?(topic) do
    table_name = table_name(topic)
    all_tables = Ets.all()
    Enum.any?(all_tables, fn table -> table == table_name end)
  end

  @doc false
  @spec register_topic(topic()) :: :ok
  def register_topic(topic) do
    unless exist?(topic), do: Ets.new(table_name(topic), @ets_opts)
    :ok
  end

  @doc false
  @spec unregister_topic(topic()) :: :ok
  def unregister_topic(topic) do
    if exist?(topic), do: Ets.delete(table_name(topic))
    :ok
  end

  @doc false
  @spec fetch(event_shadow()) :: event() | nil
  def fetch({topic, id}) do
    case Ets.lookup(table_name(topic), id) do
      [{_, %Event{} = event}] -> event
      _ ->
        Logger.log(:info, fn ->
          "[EVENTBUS][STORE]\s#{topic}.#{id}.ets_fetch_error"
        end)

        nil
    end
  end

  @doc false
  @spec fetch_data(event_shadow()) :: any()
  def fetch_data({topic, id}) do
    event = fetch({topic, id}) || %{}
    Map.get(event, :data)
  end

  @doc false
  @spec delete(event_shadow()) :: :ok
  def delete({topic, id}) do
    Ets.delete(table_name(topic), id)
    :ok
  end

  @doc false
  @spec create(event()) :: :ok
  def create(%Event{id: id, topic: topic} = event) do
    Ets.insert(table_name(topic), {id, event})
    :ok
  end

  defp table_name(topic) do
    String.to_atom("#{@prefix}#{topic}")
  end
end
```

## File: `lib/event_bus/services/subscription.ex`
```
defmodule EventBus.Service.Subscription do
  @moduledoc false

  alias EventBus.Manager.Topic, as: TopicManager
  alias EventBus.Util.Regex, as: RegexUtil

  @app :event_bus
  @namespace :subscriptions

  @typep subscriber :: EventBus.subscriber()
  @typep subscribers :: EventBus.subscribers()
  @typep subscriber_with_topic_patterns :: EventBus.subscriber_with_topic_patterns()
  @typep topic :: EventBus.topic()

  @spec subscribed?(subscriber_with_topic_patterns()) :: boolean()
  def subscribed?(subscriber) do
    Enum.member?(subscribers(), subscriber)
  end

  @doc false
  @spec subscribe(subscriber_with_topic_patterns()) :: :ok
  def subscribe({subscriber, topics}) do
    {subscribers, topic_map} = load_state()
    subscribers = add_or_update_subscriber(subscribers, {subscriber, topics})

    topic_map =
      topic_map
      |> add_subscriber_to_topic_map({subscriber, topics})
      |> Enum.into(%{})

    save_state({subscribers, topic_map})
  end

  @doc false
  @spec unsubscribe(subscriber()) :: :ok
  def unsubscribe(subscriber) do
    {subscribers, topic_map} = load_state()
    subscribers = List.keydelete(subscribers, subscriber, 0)

    topic_map =
      topic_map
      |> remove_subscriber_from_topic_map(subscriber)
      |> Enum.into(%{})

    save_state({subscribers, topic_map})
  end

  @doc false
  @spec register_topic(topic()) :: :ok
  def register_topic(topic) do
    {subscribers, topic_map} = load_state()
    topic_subscribers = topic_subscribers(subscribers, topic)

    save_state({subscribers, Map.put(topic_map, topic, topic_subscribers)})
  end

  @doc false
  @spec unregister_topic(topic()) :: :ok
  def unregister_topic(topic) do
    {subscribers, topic_map} = load_state()
    save_state({subscribers, Map.drop(topic_map, [topic])})
  end

  @doc false
  @spec subscribers() :: subscribers()
  def subscribers do
    {subscribers, _topic_map} = load_state()
    subscribers
  end

  @spec subscribers(topic()) :: subscribers()
  def subscribers(topic) do
    {_subscribers, topic_map} = load_state()
    topic_map[topic] || []
  end

  defp topic_subscribers(subscribers, topic) do
    Enum.reduce(subscribers, [], fn {subscriber, topics}, acc ->
      if RegexUtil.superset?(topics, topic), do: [subscriber | acc], else: acc
    end)
  end

  defp remove_subscriber_from_topic_map(topic_map, subscriber) do
    Enum.map(topic_map, fn {topic, topic_subscribers} ->
      topic_subscribers = List.delete(topic_subscribers, subscriber)
      {topic, topic_subscribers}
    end)
  end

  defp add_subscriber_to_topic_map(topic_map, {subscriber, topics}) do
    Enum.map(topic_map, fn {topic, topic_subscribers} ->
      topic_subscribers = List.delete(topic_subscribers, subscriber)

      if RegexUtil.superset?(topics, topic) do
        {topic, [subscriber | topic_subscribers]}
      else
        {topic, topic_subscribers}
      end
    end)
  end

  defp add_or_update_subscriber(subscribers, {subscriber, topics}) do
    if List.keymember?(subscribers, subscriber, 0) do
      List.keyreplace(subscribers, subscriber, 0, {subscriber, topics})
    else
      [{subscriber, topics} | subscribers]
    end
  end

  defp save_state(state) do
    Application.put_env(@app, @namespace, state, persistent: true)
  end

  defp load_state do
    Application.get_env(@app, @namespace, {[], init_topic_map()})
  end

  defp init_topic_map do
    Enum.into(TopicManager.all(), %{}, fn topic -> {topic, []} end)
  end
end
```

## File: `lib/event_bus/services/topic.ex`
```
defmodule EventBus.Service.Topic do
  @moduledoc false

  alias EventBus.Manager.Observation, as: ObservationManager
  alias EventBus.Manager.Store, as: StoreManager
  alias EventBus.Manager.Subscription, as: SubscriptionManager

  @typep topic :: EventBus.topic()
  @typep topics :: EventBus.topics()

  @app :event_bus
  @namespace :topics
  @modules [StoreManager, SubscriptionManager, ObservationManager]

  @doc false
  @spec all() :: topics()
  def all do
    Application.get_env(:event_bus, :topics, [])
  end

  @doc false
  @spec exist?(topic()) :: boolean()
  def exist?(topic) do
    Enum.member?(all(), topic)
  end

  @doc false
  @spec register_from_config() :: :ok
  def register_from_config do
    Enum.each(all(), fn topic ->
      Enum.each(@modules, fn mod -> mod.register_topic(topic) end)
    end)

    :ok
  end

  @doc false
  @spec register(topic()) :: :ok
  def register(topic) do
    unless exist?(topic) do
      Application.put_env(@app, @namespace, [topic | all()], persistent: true)
      Enum.each(@modules, fn mod -> mod.register_topic(topic) end)
    end

    :ok
  end

  @doc false
  @spec unregister(topic()) :: :ok
  def unregister(topic) do
    if exist?(topic) do
      Enum.each(@modules, fn mod -> mod.unregister_topic(topic) end)
      topics = List.delete(all(), topic)
      Application.put_env(@app, @namespace, topics, persistent: true)
    end

    :ok
  end
end
```

## File: `lib/event_bus/utils/base62.ex`
```
defmodule EventBus.Util.Base62 do
  @moduledoc false

  @mapping '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

  @doc """
  Generates partially sequential, base62 unique identifier.
  """
  @spec unique_id() :: String.t()
  def unique_id do
    now() <> node_id() <> random(4, 14_776_336)
  end

  @doc """
  Converts given integer to base62.
  """
  @spec encode(integer()) :: String.t()
  def encode(num) when num < 62 do
    << Enum.at(@mapping, num) >>
  end

  def encode(num) do
    encode(div(num, 62)) <> encode(rem(num, 62))
  end

  # Generates random base62 string with crypto:strong_rand_bytes
  defp random(size, max) do
    size
    |> :crypto.strong_rand_bytes()
    |> :crypto.bytes_to_integer()
    |> rem(max)
    |> encode()
    |> String.pad_leading(size, "0")
  end

  # Current time (microsecond) encoded in base62
  defp now do
    encode(System.os_time(:microsecond))
  end

  # Assigns a random node_id on first call
  defp node_id do
    case Application.get_env(:event_bus, :node_id) do
      nil -> save_node_id(random(3, 238_328))
      nid -> nid
    end
  end

  defp save_node_id(node_id) do
    Application.put_env(:event_bus, :node_id, node_id, persistent: true)
    node_id
  end
end
```

## File: `lib/event_bus/utils/monotonic_time.ex`
```
defmodule EventBus.Util.MonotonicTime do
  @moduledoc false

  @eb_app :event_bus

  @doc """
  Calculates monotonically increasing current time.
  """
  @spec now() :: integer()
  def now do
    init_time() + monotonic_time()
  end

  defp init_time do
    case Application.get_env(@eb_app, :init_time) do
      nil ->
        time = os_time() - monotonic_time()
        save_init_time(time)

      time ->
        time
    end
  end

  defp save_init_time(time) do
    Application.put_env(@eb_app, :init_time, time, persistent: true)
    time
  end

  defp os_time do
    time_unit = Application.get_env(@eb_app, :time_unit, :microsecond)
    System.os_time(time_unit)
  end

  defp monotonic_time do
    time_unit = Application.get_env(@eb_app, :time_unit, :microsecond)
    System.monotonic_time(time_unit)
  end
end
```

## File: `lib/event_bus/utils/regex.ex`
```
defmodule EventBus.Util.Regex do
  @moduledoc false
  # Regex util for event bus

  @doc """
  It checks if the given list of keys includes the key.
  """
  @spec superset?(list(String.t() | atom()), String.t() | atom()) :: boolean()
  def superset?(keys, key) do
    regex_pattern = build_regex_pattern(keys)

    case Regex.compile(regex_pattern) do
      {:ok, pattern} -> Regex.match?(pattern, "#{key}")
      _ -> false
    end
  end

  @spec build_regex_pattern(list(String.t() | atom())) :: String.t()
  defp build_regex_pattern(keys) do
    keys
    |> Enum.map_join("|", fn key -> "^(#{key})" end)
  end
end
```

## File: `test/event_bus_test.exs`
```
defmodule EventBusTest do
  use ExUnit.Case, async: false

  import ExUnit.CaptureLog

  alias EventBus.Model.Event

  alias EventBus.Support.Helper.{
    BadOne,
    Calculator,
    InputLogger,
    MemoryLeakerOne
  }

  @event %Event{
    id: "M1",
    transaction_id: "T1",
    data: [1, 7],
    topic: :metrics_received,
    source: "EventBusTest"
  }

  setup do
    for subscriber <- EventBus.subscribers() do
      EventBus.unsubscribe(subscriber)
    end

    :ok
  end

  test "notify" do
    EventBus.subscribe({{InputLogger, %{}}, [".*"]})
    EventBus.subscribe({{BadOne, %{}}, [".*"]})
    EventBus.subscribe({{Calculator, %{}}, ["metrics_received"]})
    EventBus.subscribe({{MemoryLeakerOne, %{}}, [".*"]})
    # Wait until the subscribers subscribe to the topics
    Process.sleep(100)

    logs =
      capture_log(fn ->
        EventBus.notify(@event)
        # Wait until the subscribers process the event
        Process.sleep(300)
      end)

    assert String.contains?(logs, "BadOne.process/1 raised an error!")

    assert String.contains?(
             logs,
             "Event log for %EventBus.Model.Event{data:" <>
               " [1, 7], id: \"M1\", initialized_at: nil, occurred_at: nil," <>
               " source: \"EventBusTest\", topic: :metrics_received," <>
               " transaction_id: \"T1\", ttl: nil}"
           )

    assert String.contains?(
             logs,
             "Event log for %EventBus.Model.Event{data:" <>
               " {8, [1, 7]}, id: \"E123\", initialized_at: nil," <>
               " occurred_at: nil, source: \"Logger\"," <>
               " topic: :metrics_summed, transaction_id: \"T1\", ttl: nil}"
           )
  end
end
```

## File: `test/test_helper.exs`
```
ExUnit.start()
```

## File: `test/event_bus/event_source_test.exs`
```
defmodule EventBus.EventSourceTest do
  use ExUnit.Case
  use EventBus.EventSource

  doctest EventSource

  setup do
    EventBus.register_topic(:user_created)
    :ok
  end

  test "build with all params" do
    id = 1
    topic = :user_created
    data = %{id: 1, name: "me", email: "me@example.com"}
    transaction_id = "t1"
    ttl = 100
    params = %{
      id: id,
      topic: topic,
      transaction_id: transaction_id,
      ttl: ttl,
      source: "me"
    }

    event =
      EventSource.build params do
        Process.sleep(1_000)
        data
      end

    assert event.data == data
    assert event.id == id
    assert event.topic == topic
    assert event.transaction_id == transaction_id
    assert event.ttl == ttl
    assert event.source == "me"
    refute is_nil(event.initialized_at)
    refute is_nil(event.occurred_at)
    assert Event.duration(event) > 0
  end

  test "build without passing source" do
    topic = :user_created
    event =
      EventSource.build %{topic: topic} do
        "some event data"
      end

    assert event.source == "EventBus.EventSourceTest"
  end

  test "build without passing ttl, sets the ttl from app configuration" do
    topic = :user_created
    event =
      EventSource.build %{topic: topic} do
        "some event data"
      end

    assert event.ttl == 30_000_000
  end

  test "build without passing id, sets the id with unique_id function" do
    topic = :user_created
    event =
      EventSource.build %{topic: topic} do
        "some event data"
      end

    refute is_nil(event.id)
  end

  test "build with error topic" do
    id = 1
    topic = :user_created
    error_topic = :user_create_erred
    data = %{email: "Invalid format"}
    transaction_id = "t1"
    ttl = 100

    event =
      EventSource.build %{
        id: id,
        topic: topic,
        transaction_id: transaction_id,
        ttl: ttl,
        error_topic: error_topic
      } do
        {:error, data}
      end

    assert event.data == {:error, data}
    assert event.id == id
    assert event.topic == error_topic
    assert event.transaction_id == transaction_id
    assert event.ttl == ttl
    assert event.source == "EventBus.EventSourceTest"
    refute is_nil(event.initialized_at)
    refute is_nil(event.occurred_at)
  end

  test "notify" do
    id = 1
    topic = :user_created
    data = %{id: 1, name: "me", email: "me@example.com"}

    result =
      EventSource.notify %{id: id, topic: topic} do
        data
      end

    assert result == data
  end
end
```

## File: `test/event_bus/managers/notification_test.exs`
```
defmodule EventBus.Manager.NotificationTest do
  use ExUnit.Case, async: false

  alias EventBus.Manager.Notification
  alias EventBus.Model.Event

  doctest Notification

  @topic :metrics_received
  @event %Event{
    id: "E1",
    transaction_id: "T1",
    topic: @topic,
    data: [1, 2],
    source: "NotifierTest"
  }

  setup do
    refute is_nil(Process.whereis(Notification))
    :ok
  end

  test "notify" do
    assert :ok == Notification.notify(@event)
  end
end
```

## File: `test/event_bus/managers/observation_test.exs`
```
defmodule EventBus.Manager.ObservationTest do
  use ExUnit.Case, async: false
  alias EventBus.Manager.Observation

  alias EventBus.Support.Helper.{
    BadOne,
    Calculator,
    InputLogger,
    MemoryLeakerOne
  }

  doctest Observation

  setup do
    :ok
  end

  test "exist?" do
    topic = :metrics_received_1
    Observation.register_topic(topic)

    assert Observation.exist?(topic)
  end

  test "register_topic" do
    assert :ok == Observation.register_topic(:metrics_destroyed)
  end

  test "unregister_topic" do
    topic = :metrics_destroyed
    Observation.register_topic(topic)

    assert :ok == Observation.unregister_topic(topic)
  end

  test "create" do
    topic = :some_event_occurred1
    id = "E1"

    subscribers = [
      {InputLogger, %{}},
      {Calculator, %{}},
      {MemoryLeakerOne, %{}},
      {BadOne, %{}}
    ]

    Observation.register_topic(topic)

    assert :ok == Observation.create({subscribers, {topic, id}})
  end

  test "complete" do
    topic = :some_event_occurred2
    id = "E1"

    subscribers = [
      {InputLogger, %{}},
      {Calculator, %{}},
      {MemoryLeakerOne, %{}},
      {BadOne, %{}}
    ]

    Observation.register_topic(topic)
    Observation.create({subscribers, {topic, id}})

    subscriber = {InputLogger, %{}}
    another_subscriber = {Calculator, %{}}

    # With an event_shadow tuple
    assert :ok === Observation.mark_as_completed({subscriber, {topic, id}})

    # With an open tuple
    assert :ok === Observation.mark_as_completed({another_subscriber, topic, id})
  end

  test "skip" do
    topic = :some_event_occurred3
    id = "E1"

    subscribers = [
      {InputLogger, %{}},
      {Calculator, %{}},
      {MemoryLeakerOne, %{}},
      {BadOne, %{}}
    ]

    Observation.register_topic(topic)
    Observation.create({subscribers, {topic, id}})

    subscriber = {InputLogger, %{}}
    another_subscriber = {Calculator, %{}}

    # With an event_shadow tuple
    assert :ok == Observation.mark_as_skipped({subscriber, {topic, id}})

    # With an open tuple
    assert :ok == Observation.mark_as_skipped({another_subscriber, topic, id})
  end
end
```

## File: `test/event_bus/managers/store_test.exs`
```
defmodule EventBus.Manager.StoreTest do
  use ExUnit.Case, async: false

  alias EventBus.Manager.Store
  alias EventBus.Model.Event

  doctest Store

  @topic :metrics_stored

  setup do
    refute is_nil(Process.whereis(Store))

    Store.unregister_topic(@topic)
    Store.register_topic(@topic)
    :ok
  end

  test "exist?" do
    topic = :metrics_received_1
    Store.register_topic(topic)

    assert Store.exist?(topic)
  end

  test "register_topic" do
    assert :ok == Store.register_topic(@topic)
  end

  test "unregister_topic" do
    Store.register_topic(@topic)
    assert :ok == Store.unregister_topic(@topic)
  end

  test "create" do
    event = %Event{id: "E1", transaction_id: "T1", data: %{}, topic: @topic}
    assert :ok == Store.create(event)
  end

  test "delete" do
    event = %Event{id: "E1", transaction_id: "T1", data: [1, 2], topic: @topic}
    Store.create(event)

    assert :ok == Store.delete({event.topic, event.id})
  end
end
```

## File: `test/event_bus/managers/subscription_test.exs`
```
defmodule EventBus.Manager.SubscriptionTest do
  use ExUnit.Case, async: false

  alias EventBus.Manager.Subscription
  alias EventBus.Support.Helper.{AnotherCalculator, InputLogger}

  doctest Subscription

  setup do
    on_exit(fn ->
      Subscription.unregister_topic(:auto_subscribed)
    end)

    for {subscriber, _topics} <- Subscription.subscribers() do
      Subscription.unsubscribe(subscriber)
    end

    :ok
  end

  test "subscribed?" do
    Subscription.subscribe({{InputLogger, %{}}, [".*"]})
    assert Subscription.subscribed?({{InputLogger, %{}}, [".*"]})
    refute Subscription.subscribed?({InputLogger, [".*"]})
  end

  test "subscribe" do
    assert :ok == Subscription.subscribe({{InputLogger, %{}}, [".*"]})
    assert Subscription.subscribed?({{InputLogger, %{}}, [".*"]})

    assert :ok == Subscription.subscribe({AnotherCalculator, [".*"]})
    assert Subscription.subscribed?({AnotherCalculator, [".*"]})
  end

  test "unsubscribe" do
    Subscription.subscribe({{InputLogger, %{}}, [".*"]})
    Subscription.subscribe({AnotherCalculator, [".*"]})

    assert :ok == Subscription.unsubscribe({InputLogger, %{}})
    refute Subscription.subscribed?({{InputLogger, %{}}, [".*"]})

    assert :ok == Subscription.unsubscribe(AnotherCalculator)
    refute Subscription.subscribed?({AnotherCalculator, [".*"]})
  end

  test "register_topic" do
    assert :ok == Subscription.register_topic(:auto_subscribed)
  end

  test "unregister_topic" do
    topic = :auto_subscribed
    Subscription.register_topic(topic)

    assert :ok == Subscription.unregister_topic(topic)
  end
end
```

## File: `test/event_bus/managers/topic_test.exs`
```
defmodule EventBus.Manager.TopicTest do
  use ExUnit.Case, async: false
  alias EventBus.Manager.Topic

  doctest Topic

  setup do
    on_exit(fn ->
      topics = [:t1, :t2]
      Enum.each(topics, fn topic -> Topic.unregister(topic) end)
    end)

    :ok
  end

  test "exist?" do
    topic = :metrics_received_1
    Topic.register(topic)

    assert Topic.exist?(topic)
  end

  test "register_topic" do
    assert :ok == Topic.register(:t1)
  end

  test "unregister_topic" do
    topic = :t2
    Topic.register(topic)

    assert :ok == Topic.unregister(topic)
  end
end
```

## File: `test/event_bus/models/event_test.exs`
```
defmodule EventBus.Model.EventTest do
  use ExUnit.Case
  require EventBus.Model.Event
  alias EventBus.Model.Event
  alias EventBus.Util.MonotonicTime

  doctest Event

  setup do
    EventBus.register_topic(:user_created)
    :ok
  end

  test "duration" do
    initialized_at = MonotonicTime.now()
    # Do sth in this frame
    # For example; sleep 1 second
    Process.sleep(1_000)

    event = %Event{
      id: 1,
      topic: "user_created",
      data: %{id: 1, name: "me", email: "me@example.com"},
      initialized_at: initialized_at,
      occurred_at: MonotonicTime.now()
    }

    assert Event.duration(event) > 0
  end

  test "duration should return 0 if initialized_at and/or occurred_at is nil" do
    event = %Event{
      id: 1,
      topic: "user_created",
      data: %{id: 1, name: "me", email: "me@example.com"}
    }

    assert Event.duration(event) == 0
  end
end
```

## File: `test/event_bus/services/notification_test.exs`
```
defmodule EventBus.Service.NotificationTest do
  use ExUnit.Case, async: false

  import ExUnit.CaptureLog

  alias EventBus.Model.Event
  alias EventBus.Service.Notification

  alias EventBus.Support.Helper.{
    AnotherBadOne,
    AnotherCalculator,
    BadOne,
    Calculator,
    InputLogger,
    MemoryLeakerOne
  }

  doctest Notification

  @topic :metrics_received
  @event %Event{
    id: "E1",
    transaction_id: "T1",
    topic: @topic,
    data: [1, 2],
    source: "NotificationTest"
  }

  setup do
    for topic <- EventBus.topics() do
      EventBus.unregister_topic(topic)
    end

    for {subscriber, _} <- EventBus.subscribers() do
      EventBus.unsubscribe(subscriber)
    end

    :ok
  end

  test "notify" do
    EventBus.register_topic(:metrics_received)
    EventBus.register_topic(:metrics_summed)

    EventBus.subscribe(
      {{InputLogger, %{}}, ["metrics_received$", "metrics_summed$"]}
    )

    EventBus.subscribe({{BadOne, %{}}, [".*"]})
    EventBus.subscribe({AnotherBadOne, [".*"]})
    EventBus.subscribe({{Calculator, %{}}, ["metrics_received$"]})
    EventBus.subscribe({{MemoryLeakerOne, %{}}, [".*"]})

    # This subscriber deos not have a config!!!
    EventBus.subscribe({AnotherCalculator, ["metrics_received$"]})

    # Sleep until subscriptions complete
    Process.sleep(200)

    logs =
      capture_log(fn ->
        Notification.notify(@event)
        Process.sleep(200)
      end)

    assert String.contains?(logs, "BadOne.process/1 raised an error!")

    assert String.contains?(logs, "AnotherBadOne.process/1 raised an error!")

    assert String.contains?(logs, "I don't want to handle your event")

    assert String.contains?(
             logs,
             "Event log for %EventBus.Model.Event{data: [1, 2], id: \"E1\", initialized_at: nil, occurred_at: nil, source: \"NotificationTest\", topic: :metrics_received, transaction_id: \"T1\", ttl: nil}"
           )

    assert String.contains?(
             logs,
             "Event log for %EventBus.Model.Event{data: {3, [1, 2]}, id: \"E123\", initialized_at: nil, occurred_at: nil, source: \"Logger\", topic: :metrics_summed, transaction_id: \"T1\", ttl: nil}"
           )

    assert String.contains?(
             logs,
             "Event log for %EventBus.Model.Event{data: {3, [1, 2]}, id: \"E123\", initialized_at: nil, occurred_at: nil, source: \"AnotherCalculator\", topic: :metrics_summed, transaction_id: \"T1\", ttl: nil}"
           )
  end

  test "notify without subscribers" do
    EventBus.register_topic(:metrics_received)

    logs =
      capture_log(fn ->
        Notification.notify(@event)
        Process.sleep(100)
      end)

    assert String.contains?(
             logs,
             "Topic(:metrics_received) doesn't have subscribers"
           )
  end
end
```

## File: `test/event_bus/services/observation_test.exs`
```
defmodule EventBus.Service.ObservationTest do
  use ExUnit.Case, async: false

  alias EventBus.Service.{Observation, Topic}
  alias EventBus.Support.Helper.{
    BadOne,
    Calculator,
    InputLogger,
    MemoryLeakerOne
  }

  doctest Observation

  setup do
    on_exit(fn ->
      topics = Topic.all() -- [:metrics_received, :metrics_summed]
      Enum.each(topics, fn topic -> Topic.unregister(topic) end)
    end)

    :ok
  end

  test "exist?" do
    topic = :metrics_received_1
    Observation.register_topic(topic)

    assert Observation.exist?(topic)
  end

  test "register_topic" do
    topic = :metrics_destroyed
    Observation.register_topic(topic)
    all_tables = :ets.all()
    table_name = String.to_atom("eb_ew_#{topic}")

    assert Enum.any?(all_tables, fn t -> t == table_name end)
  end

  test "unregister_topic" do
    topic = :metrics_destroyed
    Observation.register_topic(topic)
    Observation.unregister_topic(topic)
    all_tables = :ets.all()
    table_name = String.to_atom("eb_ew_#{topic}")

    refute Enum.any?(all_tables, fn t -> t == table_name end)
  end

  test "create and fetch" do
    topic = :some_event_occurred1
    id = "E1"

    subscribers = [
      {InputLogger, %{}},
      {Calculator, %{}},
      {MemoryLeakerOne, %{}},
      {BadOne, %{}}
    ]

    Observation.register_topic(topic)
    Observation.save({topic, id}, {subscribers, [], []})

    assert {subscribers, [], []} == Observation.fetch({topic, id})
  end

  test "fetch a non-existent id" do
    topic = :some_event_occurred1
    id = "NA"

    Observation.register_topic(topic)

    assert nil == Observation.fetch({topic, id})
  end

  test "complete" do
    topic = :some_event_occurred2
    id = "E1"

    subscribers = [
      {InputLogger, %{}},
      {Calculator, %{}},
      {MemoryLeakerOne, %{}},
      {BadOne, %{}}
    ]

    Observation.register_topic(topic)
    Observation.save({topic, id}, {subscribers, [], []})
    Observation.mark_as_completed({{InputLogger, %{}}, {topic, id}})

    assert {subscribers, [{InputLogger, %{}}], []} == Observation.fetch({topic, id})
  end

  test "skip" do
    id = "E1"
    topic = :some_event_occurred3

    subscribers = [
      {InputLogger, %{}},
      {Calculator, %{}},
      {MemoryLeakerOne, %{}},
      {BadOne, %{}}
    ]

    Observation.register_topic(topic)
    Observation.save({topic, id}, {subscribers, [], []})
    Observation.mark_as_skipped({{InputLogger, %{}}, {topic, id}})

    assert {subscribers, [], [{InputLogger, %{}}]} == Observation.fetch({topic, id})
  end
end
```

## File: `test/event_bus/services/store_test.exs`
```
defmodule EventBus.Service.StoreTest do
  use ExUnit.Case, async: false
  alias EventBus.Model.Event
  alias EventBus.Service.Store

  doctest Store

  setup do
    :ok
  end

  test "exist?" do
    topic = :metrics_received_1
    Store.register_topic(topic)

    assert Store.exist?(topic)
  end

  test "register_topic" do
    topic = :metrics_received_1
    Store.register_topic(topic)
    all_tables = :ets.all()
    table_name = String.to_atom("eb_es_#{topic}")

    assert Enum.any?(all_tables, fn t -> t == table_name end)
  end

  test "unregister_topic" do
    topic = :metrics_received_1
    Store.unregister_topic(topic)
    all_tables = :ets.all()
    table_name = String.to_atom("eb_es_#{topic}")

    refute Enum.any?(all_tables, fn t -> t == table_name end)
  end

  test "create" do
    topic = :metrics_received_2
    Store.register_topic(topic)

    event = %Event{
      id: "E1",
      transaction_id: "T1",
      data: ["Mustafa", "Turan"],
      topic: topic
    }

    assert :ok == Store.create(event)
  end

  test "fetch" do
    topic = :metrics_received_3
    Store.register_topic(topic)

    first_event = %Event{
      id: "E1",
      transaction_id: "T1",
      data: ["Mustafa", "Turan"],
      topic: topic
    }

    second_event = %Event{
      id: "E2",
      transaction_id: "T1",
      data: %{name: "Mustafa", surname: "Turan"},
      topic: topic
    }

    :ok = Store.create(first_event)
    :ok = Store.create(second_event)

    assert first_event == Store.fetch({topic, first_event.id})
    assert second_event == Store.fetch({topic, second_event.id})
  end

  test "fetch_data" do
    topic = :metrics_received_4
    Store.register_topic(topic)

    event = %Event{
      id: "E1",
      transaction_id: "T1",
      data: ["Mustafa", "Turan"],
      topic: topic
    }

    :ok = Store.create(event)

    assert event.data == Store.fetch_data({topic, event.id})
  end

  test "delete and fetch" do
    topic = :metrics_received_5
    Store.register_topic(topic)

    event = %Event{
      id: "E1",
      transaction_id: "T1",
      data: ["Mustafa", "Turan"],
      topic: topic
    }

    :ok = Store.create(event)
    Store.delete({topic, event.id})

    assert is_nil(Store.fetch({topic, event.id}))
  end
end
```

## File: `test/event_bus/services/subscription_test.exs`
```
defmodule EventBus.Service.SubscriptionTest do
  use ExUnit.Case, async: false

  alias EventBus.Support.Helper.{
    AnotherCalculator,
    Calculator,
    InputLogger,
    MemoryLeakerOne
  }

  alias EventBus.Service.Subscription

  doctest Subscription

  setup do
    on_exit(fn ->
      Subscription.unregister_topic(:auto_subscribed)
      Subscription.unregister_topic(:metrics_received)
      Subscription.unregister_topic(:metrics_summed)
      Process.sleep(100)
    end)

    Subscription.register_topic(:auto_subscribed)
    Subscription.register_topic(:metrics_received)
    Subscription.register_topic(:metrics_summed)
    Process.sleep(100)

    for {subscriber, _topics} <- Subscription.subscribers() do
      Subscription.unsubscribe(subscriber)
    end

    Process.sleep(100)
    :ok
  end

  test "subscribed?" do
    Subscription.subscribe({{InputLogger, %{}}, [".*"]})
    assert Subscription.subscribed?({{InputLogger, %{}}, [".*"]})
    refute Subscription.subscribed?({InputLogger, [".*"]})
  end

  test "subscribe" do
    Subscription.subscribe({{InputLogger, %{}}, [".*"]})
    Subscription.subscribe({{Calculator, %{}}, [".*"]})
    Subscription.subscribe({{MemoryLeakerOne, %{}}, [".*"]})
    Subscription.subscribe({AnotherCalculator, [".*"]})
    Process.sleep(300)

    assert [
             {AnotherCalculator, [".*"]},
             {{MemoryLeakerOne, %{}}, [".*"]},
             {{Calculator, %{}}, [".*"]},
             {{InputLogger, %{}}, [".*"]}
           ] == Subscription.subscribers()
  end

  test "does not subscribe same subscriber" do
    Subscription.subscribe({{InputLogger, %{}}, [".*"]})
    Subscription.subscribe({{InputLogger, %{}}, [".*"]})
    Subscription.subscribe({{InputLogger, %{}}, [".*"]})
    Process.sleep(300)

    assert [{{InputLogger, %{}}, [".*"]}] == Subscription.subscribers()
  end

  test "unsubscribe" do
    Subscription.subscribe({{InputLogger, %{}}, [".*"]})
    Subscription.subscribe({{Calculator, %{}}, [".*"]})
    Subscription.subscribe({{MemoryLeakerOne, %{}}, [".*"]})
    Subscription.subscribe({AnotherCalculator, [".*"]})
    Subscription.unsubscribe({Calculator, %{}})
    Subscription.unsubscribe(AnotherCalculator)
    Process.sleep(300)

    assert [{{MemoryLeakerOne, %{}}, [".*"]}, {{InputLogger, %{}}, [".*"]}] ==
             Subscription.subscribers()
  end

  test "register_topic auto subscribe workers" do
    topic = :auto_subscribed

    Subscription.subscribe({{InputLogger, %{}}, [".*"]})
    Subscription.subscribe({{Calculator, %{}}, [".*"]})
    Subscription.subscribe({{MemoryLeakerOne, %{}}, ["other_received$"]})
    Subscription.subscribe({AnotherCalculator, [".*"]})

    Subscription.register_topic(topic)

    Process.sleep(300)

    assert [{InputLogger, %{}}, {Calculator, %{}}, AnotherCalculator] ==
             Subscription.subscribers(topic)
  end

  test "unregister_topic delete subscribers" do
    topic = :auto_subscribed

    Subscription.subscribe({{InputLogger, %{}}, [".*"]})
    Subscription.subscribe({{Calculator, %{}}, [".*"]})
    Subscription.subscribe({{MemoryLeakerOne, %{}}, ["other_received$"]})
    Subscription.subscribe({AnotherCalculator, [".*"]})

    Subscription.register_topic(topic)
    Subscription.unregister_topic(topic)
    Process.sleep(300)

    assert [] == Subscription.subscribers(topic)
  end

  test "subscribers" do
    Subscription.subscribe({{InputLogger, %{}}, [".*"]})
    Process.sleep(300)

    assert [{{InputLogger, %{}}, [".*"]}] == Subscription.subscribers()
  end

  test "subscribers with event type" do
    Subscription.subscribe({{InputLogger, %{}}, [".*"]})
    Process.sleep(300)

    assert [{InputLogger, %{}}] == Subscription.subscribers(:metrics_received)
    assert [{InputLogger, %{}}] == Subscription.subscribers(:metrics_summed)
  end

  test "subscribers with event type and without config" do
    Subscription.subscribe({AnotherCalculator, [".*"]})
    Process.sleep(300)

    assert [AnotherCalculator] == Subscription.subscribers(:metrics_received)
    assert [AnotherCalculator] == Subscription.subscribers(:metrics_summed)
  end

  test "state persistency to Application environment" do
    Subscription.subscribe(
      {{InputLogger, %{}}, ["metrics_received", "metrics_summed"]}
    )

    Subscription.subscribe({AnotherCalculator, ["metrics_received$"]})
    Process.sleep(300)

    expected = {
      [
        {AnotherCalculator, ["metrics_received$"]},
        {{InputLogger, %{}}, ["metrics_received", "metrics_summed"]}
      ],
      %{
        metrics_received: [AnotherCalculator, {InputLogger, %{}}],
        metrics_summed: [{InputLogger, %{}}],
        auto_subscribed: []
      }
    }

    assert expected == Application.get_env(:event_bus, :subscriptions)
  end
end
```

## File: `test/event_bus/services/topic_test.exs`
```
defmodule EventBus.Service.TopicTest do
  use ExUnit.Case, async: false
  alias EventBus.Service.Topic

  doctest Topic

  setup do
    on_exit(fn ->
      topics = Topic.all() -- [:metrics_received, :metrics_summed]
      Enum.each(topics, fn topic -> Topic.unregister(topic) end)
    end)

    :ok
  end

  test "exist?" do
    topic = :metrics_received_1
    Topic.register(topic)

    assert Topic.exist?(topic)
  end

  test "register_topic" do
    topic = :t1
    Topic.register(topic)
    all_tables = :ets.all()

    store_table_name = String.to_atom("eb_es_#{topic}")
    watcher_table_name = String.to_atom("eb_ew_#{topic}")

    assert Enum.any?(Topic.all(), fn t -> t == topic end)
    assert Enum.any?(all_tables, fn t -> t == store_table_name end)
    assert Enum.any?(all_tables, fn t -> t == watcher_table_name end)
  end

  test "register_topic does not re-register same topic" do
    topic = :t2
    Topic.register(topic)
    topic_count = length(Topic.all())
    Topic.register(topic)

    assert topic_count == length(Topic.all())
  end

  test "unregister_topic" do
    topic = :t3
    Topic.register(topic)
    Topic.unregister(topic)
    all_tables = :ets.all()

    store_table_name = String.to_atom("eb_es_#{topic}")
    watcher_table_name = String.to_atom("eb_ew_#{topic}")

    refute Enum.any?(Topic.all(), fn t -> t == topic end)
    refute Enum.any?(all_tables, fn t -> t == store_table_name end)
    refute Enum.any?(all_tables, fn t -> t == watcher_table_name end)
  end

  test "all" do
    topic = :t3
    Topic.register(topic)
    assert [:t3, :metrics_received, :metrics_summed] == Topic.all()
  end

  test "exist? with an existent topic" do
    assert Topic.exist?(:metrics_received)
  end

  test "exist? with a non-existent topic" do
    refute Topic.exist?(:unknown_called)
  end
end
```

## File: `test/event_bus/utils/base62_test.exs`
```
defmodule EventBus.Util.Base62Test do
  use ExUnit.Case

  alias EventBus.Util.Base62

  test "encode" do
    assert "0" == Base62.encode(0)
    assert "z" == Base62.encode(61)
    assert "10" == Base62.encode(62)
    assert "1p0uwg6tOzJ" == Base62.encode(1_529_891_323_138_833_953)
  end

  test "unique_id" do
    refute Base62.unique_id() == Base62.unique_id()
  end

  test "unique_id length must match" do
    assert 16 == String.length(Base62.unique_id())
  end

  test "unique_id does not change node_id configuration on multiple calls" do
    # First call
    Base62.unique_id()
    node_id = Application.get_env(:event_bus, :node_id)

    # Second call
    Base62.unique_id()
    assert node_id == Application.get_env(:event_bus, :node_id)
  end
end
```

## File: `test/event_bus/utils/monotonic_time_test.exs`
```
defmodule EventBus.Util.MonotonicTimeTest do
  use ExUnit.Case

  alias EventBus.Util.MonotonicTime

  test "now should return int" do
    assert is_integer(MonotonicTime.now())
  end

  test "now should increase on every call" do
    assert MonotonicTime.now() <= MonotonicTime.now()
  end

  test "now does not change init_time configuration on multiple calls" do
    # First call
    MonotonicTime.now()
    init_time = Application.get_env(:event_bus, :init_time) # init_time

    # Second call
    MonotonicTime.now()
    assert init_time == Application.get_env(:event_bus, :init_time)
  end
end
```

## File: `test/event_bus/utils/regex_test.exs`
```
defmodule EventBus.Util.RegexTest do
  use ExUnit.Case
  alias EventBus.Util.Regex, as: RegexUtil

  test "superset? should return true when it is superset of given key" do
    assert RegexUtil.superset?(~w(.*), "some")
    assert RegexUtil.superset?(~w(metrics painted), "metrics_received")
  end

  test "superset? should return false when it is not superset of given key" do
    refute RegexUtil.superset?(~w(metrics_sum$), "metrics_summed")
  end
end
```

## File: `test/support/helper.ex`
```
defmodule EventBus.Support.Helper do
  alias EventBus.Model.Event

  defmodule InputLogger do
    @moduledoc """
    I am the logger
    """

    require Logger

    @doc false
    def process({config, topic, id}) do
      event = EventBus.fetch_event({topic, id})
      Logger.info(fn -> "Event log for #{inspect(event)}" end)
      EventBus.mark_as_completed({{__MODULE__, config}, topic, id})
    end
  end

  defmodule Calculator do
    @moduledoc """
    Brand new fun calculator
    """

    require Logger

    @doc false
    def process({config, :metrics_received, id}) do
      event = EventBus.fetch_event({:metrics_received, id})
      inputs = event.data
      # handle an event
      sum = Enum.reduce(inputs, 0, &(&1 + &2))
      # create a new event if necessary
      new_event = %Event{
        id: "E123",
        transaction_id: event.transaction_id,
        topic: :metrics_summed,
        data: {sum, inputs},
        source: "Logger"
      }

      EventBus.notify(new_event)
      EventBus.mark_as_completed({{__MODULE__, config}, :metrics_received, id})
    end

    @doc false
    def process({config, topic, id}) do
      EventBus.mark_as_skipped({{__MODULE__, config}, topic, id})
    end
  end

  defmodule AnotherCalculator do
    @moduledoc """
    Crazy calculation service
    """

    require Logger

    @doc false
    def process({:metrics_received, id}) do
      event = EventBus.fetch_event({:metrics_received, id})
      inputs = event.data
      # handle an event
      sum = Enum.reduce(inputs, 0, &(&1 + &2))
      # create a new event if necessary
      new_event = %Event{
        id: "E123",
        transaction_id: event.transaction_id,
        topic: :metrics_summed,
        data: {sum, inputs},
        source: "AnotherCalculator"
      }

      EventBus.notify(new_event)
      EventBus.mark_as_completed({__MODULE__, :metrics_received, id})
    end

    @doc false
    def process({topic, id}) do
      EventBus.mark_as_skipped({__MODULE__, topic, id})
    end
  end

  defmodule MemoryLeakerOne do
    @moduledoc """
    Adds all sums to a list without caring memory (bad one)
    """

    use GenServer

    @doc false
    def start_link do
      GenServer.start_link(__MODULE__, [], name: __MODULE__)
    end

    @doc false
    def init(args) do
      {:ok, args}
    end

    @doc false
    def process({config, :metrics_summed, id}) do
      GenServer.cast(__MODULE__, {config, :metrics_summed, id})
    end

    @doc false
    def process({config, topic, id}) do
      EventBus.mark_as_skipped({{__MODULE__, config}, topic, id})
    end

    @doc false
    def handle_cast({config, :metrics_summed, id}, state) do
      event = EventBus.fetch_event({:metrics_summed, id})
      new_state = [event | state]
      EventBus.mark_as_completed({{__MODULE__, config}, :metrics_summed, id})
      {:noreply, new_state}
    end
  end

  defmodule BadOne do
    @moduledoc """
    A bad subscriber implementation with wrong arity
    All events will be marked as skipped
    """

    @doc false
    def process(_, _) do
      # it has wrong arity, can't be a subscriber
    end
  end

  defmodule AnotherBadOne do
    @moduledoc """
    A bad subscriber implementation with error raising
    If the process raise an error the the event will be marked as skipped
    """

    @doc false
    def process(_) do
      raise "I don't want to handle your event"
    end
  end
end
```


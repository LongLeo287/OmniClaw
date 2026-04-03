---
id: github.com-message-db-message-db-e401d530-knowledg
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:20:24.967907
---

# KNOWLEDGE EXTRACT: github.com_message-db_message-db_e401d530
> **Extracted on:** 2026-04-01 16:40:31
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007525218/github.com_message-db_message-db_e401d530

---

## File: `.gitignore`
```
.DS_store
.bundle/
Gemfile.lock
*.gem
gems
```

## File: `CHANGES.md`
```markdown
# Changes

## 1.3.0

Wed Oct 12 2022

This version requires the use of an update script for existing installations. For instructions, see:

[https://github.com/message-db/message-db/blob/master/database/update/1.3.0.md](https://github.com/message-db/message-db/blob/master/database/update/1.3.0.md)

- The `get_last_stream_message` function can receive an optional `type` argument that constrains the result to the last message of a stream of a specified message type (see: [http://docs.eventide-project.org/user-guide/message-db/server-functions.html#get-last-message-from-a-stream](http://docs.eventide-project.org/user-guide/message-db/server-functions.html#get-last-message-from-a-stream))
- The database installation scripts terminate on error, rather than proceeding with the rest of the installation when a script error occurs

## 1.2.6

Sat Mar 13 2021

- The `uninstall.sh` script quotes the database name when dropping it, allowing database names that contain dashes

## 1.2.5

Fri Mar 12 2021

- The `print-messages.sh` script sorts messages explicitly by `global_position`

## 1.2.4

Sun Mar 7 2021

- The `messages` tables columns are ordered for more efficient physical storage allocation.

This version should not be considered an update to an existing database. It requires a new installation of the database, and therefore its advantages will only apply to new databases.

## 1.2.3

Fri May 15 2020

- The `md5` function is no longer granted privileges for the message_store user as the function is built-in and the grant is superfluous

## 1.2.2

Mon May 4 2020

This version requires the use of an update script for existing installations. For instructions, see:

[https://github.com/message-db/message-db/blob/master/database/update/1.2.2.md](https://github.com/message-db/message-db/blob/master/database/update/1.2.2.md)

- The `get_category_messages` server function will return the entire, unlimited extent of messages in a category if -1 is sent as the `batch_size` argument
- The `get_stream_messages` server function will return the entire, unlimited extent of messages in a stream if -1 is sent as the `batch_size` argument

## 1.2.1

Thu Apr 30 2020

- The `DROP OWNED BY message_store` statement is removed from the uninstall script. The use of `DROP OWNED BY` is prohibited on AWS RDS. And ultimately, it's superfluous because no database objects are owned by the message_store role.

## 1.2.0

Mon Apr 27 2020

- Install script will not create the database when the CREATE_DATABASE environment variable is set to "off"

## 1.1.6

Mon Jan 6 2020

- Install and uninstall scripts explicitly connect to the postgres database when running the psql utility, and do not depend on the existence of a user database

## 1.1.5

Fri Dec 20 2019

- Changes applied to a pre-v1 message store are documented in database/update/1.0.0.md
- The v1 update script prints out a link to the changes doc

## 1.1.4

Fri Dec 20 2019

- The update script is deprecated in preparation of versioned update scripts
- Update scripts are located in database/updates
- The update code for the v1.0.0 database is moved to database/updates/1.0.0.sh

## 1.1.3

Fri Dec 20 2019

- The update script is corrected for its referencing of the gen_random_uuid from the message_store schema

## 1.1.2

Thu Dec 19 2019

- The pgcrypto extension is not installed into the message_store schema

## 1.1.1

Wed Dec 18 2019

- Vestigial debug output is removed from write_message

## 1.1.0

Wed Dec 11 2019

- The message_store role does not own the schema

# 1.0.0

Tue Dec 10 2019

- Initial release
```

## File: `MIT-License.txt`
```
Copyright (c) 2015-present Scott Bellware

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```

## File: `README.md`
```markdown
![Message DB](http://docs.eventide-project.org/message-db-logo-90x105.png)

# Message DB

**Microservice Native Event Store and Message Store for Postgres**

A fully-featured event store and message store implemented in PostgreSQL for Pub/Sub, Event Sourcing, Messaging, and Evented Microservices applications.

## Features

- Pub/Sub
- JSON message data
- Event streams
- Stream categories
- Metadata
- Message queues
- Message storage
- Consumer groups
- Service host
- Administration tools
- Reports

## Rationale

An event sourcing and Pub/Sub message store built on Postgres for simple cloud or local hosting. A minimalist implementation of the essential features of tools like [Event Store](https://eventstore.org) or [Kafka](https://kafka.apache.org), with built-in support for messaging patterns like Pub/Sub, and consumer patterns like consumer groups.

Message DB was extracted from the [Eventide Project](http://docs.eventide-project.org) to make it easier for users to write clients in the language of their choosing.

## User Guide

A complete user guide is available on the Eventide Project docs site:

[http://docs.eventide-project.org/user-guide/message-db/](http://docs.eventide-project.org/user-guide/message-db/)

## Installation

Message DB can be installed either as a Ruby Gem, an NPM package, or can simply be cloned from this repository.

### Git Clone

``` bash
git clone git@github.com:message-db/message-db.git
```

### As a Ruby Gem

``` bash
gem install message-db
```

### As an NPM Module

``` bash
npm install @eventide/message-db
```

## Create the Postgres Database

Running the database installation script creates the database, schema, table, indexes, functions, views, types, a user role, and limit the user's privileges to the message store's public interface.

### Requirements

Make sure that your default Postgres user has administrative privileges.

### From the Git Clone

The installation script is in the `database` directory of the cloned repo. Change directory to the `message-db` directory where you cloned the repo, and run the script:

``` bash
database/install.sh
```

### From the Ruby Executable

If you installed Message DB via RubyGems, a database installation Ruby executable will be installed with the `message-db` gem.

The executable will be in the gem executable search path and may also be executed through bundler:

``` bash
bundle exec mdb-create-db
```

For more information about Ruby executables installed with the `message-db` Ruby Gem, see the Eventide docs on the administration tools that are bundled with the gem:

[http://docs.eventide-project.org/user-guide/message-db/tools.html](http://docs.eventide-project.org/user-guide/message-db/tools.html)

### From the NPM Module

The `message-db` NPM module doesn't ship with any special tooling other than the bundled scripts.

To execute the installation script, navigate to the directory where the `message-db` module is installed and run the script:

``` bash
install.sh
```

### Database Name

By default, the database creation tool will create a database named `message_store`.

If you prefer either a different database name, you can override the name using the `DATABASE_NAME` environment variable.

``` bash
DATABASE_NAME=some_other_database database/install.sh
```

### Uninstalling the Database

If you need to drop the database (for example, on a local dev machine):

``` bash
database/uninstall.sh
```

If you're upgrading a previous version of the database:

``` bash
database/update.sh
```

## API Overview

The message store provides an interface of Postgres server functions that can be used with any programming language or through the `psql` command line tool.

Interaction with the underlying store through the Postgres server functions ensures correct writing and reading messages, streams, and categories.

### Write a Message

Write a JSON-formatted message to a named stream, optionally specifying JSON-formatted metadata and an expected version number.

``` sql
write_message(
  id varchar,
  stream_name varchar,
  type varchar,
  data jsonb,
  metadata jsonb DEFAULT NULL,
  expected_version bigint DEFAULT NULL
)
```

#### Returns

Position of the message written.

#### Arguments

| Name | Description | Type | Default | Example |
| --- | --- | --- | --- | --- |
| id | UUID of the message being written | varchar | | a5eb2a97-84d9-4ccf-8a56-7160338b11e2 |
| stream_name | Name of stream to which the message is written | varchar | | someStream-123 |
| type | The type of the message | varchar | | Withdrawn |
| data | JSON representation of the message body | jsonb | | {"someAttribute": "some value"} |
| metadata (optional) | JSON representation of the message metadata | jsonb | NULL | {"metadataAttribute": "some meta data value"} |
| expected_version (optional) | Version that the stream is expected to be when the message is written | bigint | NULL | 11 |

#### Usage

``` sql
SELECT write_message('a11e9022-e741-4450-bf9c-c4cc5ddb6ea3', 'someStream-123', 'SomeMessageType', '{"someAttribute": "some value"}', '{"metadataAttribute": "some meta data value"}');
```

```
-[ RECORD 1 ]-+--
write_message | 0
```

Example: [https://github.com/message-db/message-db/blob/master/database/write-test-message.sh](https://github.com/message-db/message-db/blob/master/database/write-test-message.sh)

### Get Messages from a Stream

Retrieve messages from a single stream, optionally specifying the starting position, the number of messages to retrieve, and an additional condition that will be appended to the SQL command's WHERE clause.

``` sql
get_stream_messages(
  stream_name varchar,
  position bigint DEFAULT 0,
  batch_size bigint DEFAULT 1000,
  condition varchar DEFAULT NULL
)
```

#### Arguments

| Name | Description | Type | Default | Example |
| --- | --- | --- | --- | --- |
| stream_name | Name of stream to retrieve messages from | varchar | | someStream-123 |
| position (optional) | Starting position of the messages to retrieve | bigint | 0 | 11 |
| batch_size (optional) | Number of messages to retrieve | bigint | 1000 | 111 |
| condition (optional) | SQL condition to filter the batch by | varchar | NULL | messages.time >= current_time |

#### Usage

``` sql
SELECT * FROM get_stream_messages('someStream-123', 0, 1000, condition => 'messages.time >= current_time');
```

```
-[ RECORD 1 ]---+---------------------------------------------------------
id              | 4b96f09e-104a-4b1f-b198-5b3b46cf1d06
stream_name     | someStream-123
type            | SomeType
position        | 0
global_position | 1
data            | {"attribute": "some value"}
metadata        | {"metaAttribute": "some meta value"}
time            | 2019-11-24 17:56:09.71594
-[ RECORD 2 ]---+---------------------------------------------------------
id              | d94e79e3-cdda-49a3-9aad-ce5d70a5edd7
stream_name     | someStream-123
type            | SomeType
position        | 1
global_position | 2
data            | {"attribute": "some value"}
metadata        | {"metaAttribute": "some meta value"}
time            | 2019-11-24 17:56:09.75969
```

Example: [https://github.com/message-db/message-db/blob/master/test/get-stream-messages/get-stream-messages.sh](https://github.com/message-db/message-db/blob/master/test/get-stream-messages/get-stream-messages.sh)

### Get Messages from a Category

Retrieve messages from a category of streams, optionally specifying the starting position, the number of messages to retrieve, the correlation category for Pub/Sub, consumer group parameters, and an additional condition that will be appended to the SQL command's WHERE clause.

``` sql
CREATE OR REPLACE FUNCTION get_category_messages(
  category_name varchar,
  position bigint DEFAULT 0,
  batch_size bigint DEFAULT 1000,
  correlation varchar DEFAULT NULL,
  consumer_group_member bigint DEFAULT NULL,
  consumer_group_size bigint DEFAULT NULL,
  condition varchar DEFAULT NULL
)
```

#### Arguments

| Name | Description | Type | Default | Example |
| --- | --- | --- | --- | --- |
| category_name | Name of the category to retrieve messages from | varchar | | someCategory |
| position (optional) | Global position to start retrieving messages from | bigint | 1 | 11 |
| batch_size (optional) | Number of messages to retrieve | bigint | 1000 | 111 |
| correlation (optional) | Category or stream name recorded in message metadata's `correlationStreamName` attribute to filter the batch by | varchar | NULL | someCorrelationCategory |
| consumer_group_member (optional) | The zero-based member number of an individual consumer that is participating in a consumer group | bigint | NULL | 1 |
| consumer_group_size (optional) | The size of a group of consumers that are cooperatively processing a single category | bigint | NULL | 2 |
| condition (optional) | SQL condition to filter the batch by | varchar | NULL | messages.time >= current_time |

#### Usage

``` sql
SELECT * FROM get_category_messages('someCategory', 1, 1000, correlation => 'someCorrelationCategory', consumer_group_member => 1, consumer_group_size => 2, condition => 'messages.time >= current_time');
```

```
-[ RECORD 1 ]---+---------------------------------------------------------
id              | 28d8347f-677e-4738-b6b9-954f1b15463b
stream_name     | someCategory-123
type            | SomeType
position        | 0
global_position | 111
data            | {"attribute": "some value"}
metadata        | {"correlationStreamName": "someCorrelationCategory-123"}
time            | 2019-11-24 17:51:49.836341
-[ RECORD 2 ]---+---------------------------------------------------------
id              | 57894da7-680b-4483-825c-732dcf873e93
stream_name     | someCategory-456
type            | SomeType
position        | 1
global_position | 1111
data            | {"attribute": "some value"}
metadata        | {"correlationStreamName": "someCorrelationCategory-123"}
time            | 2019-11-24 17:51:49.879011
```

Note: Where `someStream-123` is a _stream name_, `someStream` is a _category_. Reading the `someStream` category retrieves messages from all streams whose names start with `someStream` and are followed by an ID, or where `someStream` is the whole stream name.

Example: [https://github.com/message-db/message-db/blob/master/test/get-category-messages/get-category-messages.sh](https://github.com/message-db/message-db/blob/master/test/get-category-messages/get-category-messages.sh)

### Full API Reference

- [write_message](http://docs.eventide-project.org/user-guide/message-db/server-functions.html#write-a-message)
- [get_stream_messages](http://docs.eventide-project.org/user-guide/message-db/server-functions.html#get-messages-from-a-stream)
- [get_category_messages](http://docs.eventide-project.org/user-guide/message-db/server-functions.html#get-messages-from-a-category)
- [get_last_stream_message](http://docs.eventide-project.org/user-guide/message-db/server-functions.html#get-last-message-from-a-stream)
- [stream_version](http://docs.eventide-project.org/user-guide/message-db/server-functions.html#get-stream-version-from-a-stream)
- [id](http://docs.eventide-project.org/user-guide/message-db/server-functions.html#get-the-id-from-a-stream-name)
- [cardinal_id](http://docs.eventide-project.org/user-guide/message-db/server-functions.html#get-the-cardinal-id-from-a-stream-name)
- [category](http://docs.eventide-project.org/user-guide/message-db/server-functions.html#get-the-category-from-a-stream-name)
- [is_category](http://docs.eventide-project.org/user-guide/message-db/server-functions.html#determine-whether-a-stream-name-is-a-category)
- [acquire_lock](http://docs.eventide-project.org/user-guide/message-db/server-functions.html#acquire-a-lock-for-a-stream-name)
- [hash_64](http://docs.eventide-project.org/user-guide/message-db/server-functions.html#calculate-a-64-bit-hash-for-a-stream-name)
- [message_store_version](http://docs.eventide-project.org/user-guide/message-db/server-functions.html#get-message-store-database-schema-version)

## Structure

The message store is a single table named `messages`.

## Messages Table

| Column | Description | Type | Default | Nullable |
| --- | --- | --- | --- | --- |
| id | Identifier of a message record | UUID | gen_random_uuid() | No |
| stream_name | Name of stream to which the message belongs | varchar | | No |
| type | The type of the message | varchar | | No |
| position | The ordinal position of the message in its stream. Position is gapless. | bigint | | No |
| global_position | Primary key. The ordinal position of the message in the entire message store. Global position may have gaps. | bigint | | No |
| data | Message payload | jsonb | NULL | Yes |
| metadata | Message metadata | jsonb | NULL | Yes |
| time | Timestamp when the message was written. The timestamp does not include a time zone. | timestamp | now() AT TIME ZONE 'utc' | No |

## Indexes

| Name | Columns | Unique | Note |
| --- | --- | --- | --- |
| messages_id | id | Yes | Enforce uniqueness as secondary key |
| messages_stream | stream_name, position | Yes | Ensures uniqueness of position number in a stream |
| messages_category | category(stream_name), global_position, category(metadata->>'correlationStreamName') | No | Used when retrieving by category name |

## Database

By default, the message store database is named `message_store`.

## Schema

All message store database objects are contained within a schema named `message_store`.

## User/Role

A role named `message_store` is created. The `message_store` role is given the `LOGIN` attribute, but no password is assigned. A password [can be assigned to the role](https://www.postgresql.org/docs/current/sql-alterrole.html), or the `message_store` role can be [granted to another Postgres user](https://www.postgresql.org/docs/current/role-membership.html).

## Source Code

View complete source code at:

[https://github.com/message-db/message-db/tree/master/database](https://github.com/message-db/message-db/tree/master/database)

## License

The Postgres Message Store is released under the [MIT License](https://github.com/message-db/message-db/blob/master/MIT-License.txt).

```

## File: `recreate-database.sh`
```bash
#!/usr/bin/env bash

database/uninstall.sh
database/install.sh
```

## File: `test.sh`
```bash
#!/usr/bin/env bash

set -e

test/hash-64.sh

test/category/stream-name.sh
test/category/category.sh

test/is_category/category.sh
test/is_category/stream-name.sh

test/id/stream-name.sh
test/id/category.sh
test/id/compound-id/stream-name.sh

test/cardinal-id/stream-name-with-compound-id.sh
test/cardinal-id/stream-name-with-single-id.sh
test/cardinal-id/category.sh

test/write-message/write-message.sh
test/write-message/expected-version.sh
test/write-message/expected-version-error.sh

test/get-stream-messages/get-stream-messages.sh
test/get-stream-messages/error-not-stream-name.sh

test/get-stream-messages/batch_size/limited.sh
test/get-stream-messages/batch_size/unlimited.sh

test/get-stream-messages/condition/condition.sh
test/get-stream-messages/condition/error-deactivated.sh
test/get-stream-messages/condition/error-not-activated.sh

test/get-category-messages/get-category-messages.sh
test/get-category-messages/error-not-category.sh

test/get-category-messages/batch_size/limited.sh
test/get-category-messages/batch_size/unlimited.sh

test/get-category-messages/correlated/correlated.sh
test/get-category-messages/correlated/error-stream-name.sh

test/get-category-messages/consumer-group/consumer-group.sh
test/get-category-messages/consumer-group/correlated.sh

test/get-category-messages/consumer-group/error/missing-group-member.sh
test/get-category-messages/consumer-group/error/missing-group-size.sh
test/get-category-messages/consumer-group/error/group-member-equal-to-group-size.sh
test/get-category-messages/consumer-group/error/group-member-greater-than-group-size.sh
test/get-category-messages/consumer-group/error/group-member-too-small.sh
test/get-category-messages/consumer-group/error/group-size-too-small.sh

test/get-category-messages/condition/condition.sh
test/get-category-messages/condition/error-deactivated.sh
test/get-category-messages/condition/error-not-activated.sh
test/get-category-messages/condition/condition-correlated.sh

test/get-last-stream-message/get-last-stream-message.sh
test/get-last-stream-message/type.sh

test/stream-version/stream-version.sh

test/message-store-version.sh

test/reports/messages.sh
test/reports/stream-summary.sh
test/reports/type-summary.sh
test/reports/stream-type-summary.sh
test/reports/type-stream-summary.sh
test/reports/category-type-summary.sh
test/reports/type-category-summary.sh

echo "Done"
echo
```

## File: `database/VERSION.txt`
```
1.3.0
```

## File: `database/benchmark.sh`
```bash
#!/usr/bin/env bash

set -u

uuid=$(echo $(uuidgen) | tr '[:upper:]' '[:lower:]')

stream_name="testStream-$uuid"
if [ ! -z ${STREAM_NAME+x} ]; then
  stream_name=$STREAM_NAME
fi

cycles=1000
if [ ! -z ${CYCLES+x} ]; then
  cycles=$CYCLES
fi

function script_dir {
  val="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
  echo "$val"
}

base=$(script_dir)

echo
echo "Benchmark $cycles cycles (Stream Name: $stream_name)"
echo "= = ="
echo

if [ -z ${DATABASE_NAME+x} ]; then
  echo "(DATABASE_NAME is not set)"
  database=message_store
else
  database=$DATABASE_NAME
fi
echo "Database name is: $database"
echo

function run_psql {
  psql $database -v ON_ERROR_STOP=1 "$@"
}

echo "Installing benchmark scripts"
echo

run_psql -q -f $base/benchmark_write.sql
run_psql -q -f $base/benchmark_get.sql

echo
echo "Benchmarking write"
echo "- - -"
echo

run_psql -U message_store -c "EXPLAIN ANALYZE SELECT benchmark_write('$stream_name'::varchar, $cycles::int);"

echo

echo
echo "Benchmarking get"
echo "- - -"
echo

run_psql -U message_store -c "EXPLAIN ANALYZE SELECT benchmark_get('$stream_name'::varchar, $cycles::int);"

echo "= = ="
echo "Done"
echo
```

## File: `database/benchmark_get.sql`
```sql
CREATE OR REPLACE FUNCTION benchmark_get(
  stream_name varchar,
  cycles int DEFAULT 1000
)
RETURNS void
AS $$
BEGIN
  RAISE NOTICE '» benchmark_get';
  RAISE NOTICE 'stream_name: %', benchmark_get.stream_name;
  RAISE NOTICE 'cycles: %', benchmark_get.cycles;

  FOR i IN 1..cycles LOOP
    IF current_setting('message_store.debug_benchmark', true) = 'on' OR current_setting('message_store.debug', true) = 'on' THEN
      RAISE NOTICE '%', i;
    END IF;

    PERFORM get_stream_messages(stream_name, "position" => i - 1, batch_size => 1);
  END LOOP;
END;
$$ LANGUAGE plpgsql
VOLATILE;
```

## File: `database/benchmark_write.sql`
```sql
CREATE OR REPLACE FUNCTION benchmark_write(
  stream_name varchar,
  cycles int DEFAULT 1000
)
RETURNS void
AS $$
BEGIN
  RAISE NOTICE '» benchmark_write';
  RAISE NOTICE 'stream_name: %', benchmark_write.stream_name;
  RAISE NOTICE 'cycles: %', benchmark_write.cycles;

  FOR i IN 1..cycles LOOP
    IF current_setting('message_store.debug_benchmark', true) = 'on' OR current_setting('message_store.debug', true) = 'on' THEN
      RAISE NOTICE '%', i;
    END IF;

    PERFORM write_message(gen_random_uuid()::varchar, stream_name::varchar, 'SomeType'::varchar, '{"attribute": "some value"}'::jsonb, '{"metaAttribute": "some meta value", "correlationStreamName": "someCorrelation-123"}'::jsonb);
  END LOOP;
END;
$$ LANGUAGE plpgsql
VOLATILE;
```

## File: `database/clear-messages.sh`
```bash
#!/usr/bin/env bash

set -e

echo
echo "Clearing Messages Table"
echo "= = ="
echo

default_name=message_store

if [ -z ${DATABASE_NAME+x} ]; then
  echo "(DATABASE_NAME is not set)"
  database=$default_name
else
  database=$DATABASE_NAME
fi
echo "Database name is: $database"

echo

psql $database -v ON_ERROR_STOP=1 -q -c "TRUNCATE message_store.messages RESTART IDENTITY;"

echo "= = ="
echo "Done Clearing Messages Table"
echo
```

## File: `database/install-functions.sh`
```bash
#!/usr/bin/env bash

set -e

if [ -z ${DATABASE_NAME+x} ]; then
  database=message_store
  echo "(DATABASE_NAME is not set. Using: $database.)"
else
  database=$DATABASE_NAME
fi

function run_psql_file {
  psql $database -q -v ON_ERROR_STOP=1 -f "$1"
}

function script_dir {
  val="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
  echo "$val"
}

function create-types {
  base=$(script_dir)

  echo "» message type"
  run_psql_file $base/types/message.sql
}

function create-functions {
  base=$(script_dir)

  echo "» message_store_version function"
  run_psql_file $base/functions/message-store-version.sql

  echo "» hash_64 function"
  run_psql_file $base/functions/hash-64.sql

  echo "» acquire_lock function"
  run_psql_file $base/functions/acquire-lock.sql

  echo "» category function"
  run_psql_file $base/functions/category.sql

  echo "» is_category function"
  run_psql_file $base/functions/is-category.sql

  echo "» id function"
  run_psql_file $base/functions/id.sql

  echo "» cardinal_id function"
  run_psql_file $base/functions/cardinal-id.sql

  echo "» stream_version function"
  run_psql_file $base/functions/stream-version.sql

  echo "» write_message function"
  run_psql_file $base/functions/write-message.sql

  echo "» get_stream_messages function"
  run_psql_file $base/functions/get-stream-messages.sql

  echo "» get_category_messages function"
  run_psql_file $base/functions/get-category-messages.sql

  echo "» get_last_stream_message function"
  run_psql_file $base/functions/get-last-stream-message.sql
}

echo "Creating Types"
echo "- - -"
create-types
echo

echo "Creating Functions"
echo "- - -"
create-functions
echo
```

## File: `database/install-indexes.sh`
```bash
#!/usr/bin/env bash

set -e

if [ -z ${DATABASE_NAME+x} ]; then
  database=message_store
  echo "(DATABASE_NAME is not set. Using: $database.)"
else
  database=$DATABASE_NAME
fi

function run_psql_file {
  psql $database -q -v ON_ERROR_STOP=1 -f "$1"
}

function script_dir {
  val="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
  echo "$val"
}

function create-indexes {
  base=$(script_dir)

  echo "» messages_id index"
  run_psql_file $base/indexes/messages-id.sql

  echo "» messages_stream index"
  run_psql_file $base/indexes/messages-stream.sql

  echo "» messages_category index"
  run_psql_file $base/indexes/messages-category.sql
}

echo "Creating Indexes"
echo "- - -"
create-indexes
echo
```

## File: `database/install-privileges.sh`
```bash
#!/usr/bin/env bash

set -e

if [ -z ${DATABASE_NAME+x} ]; then
  database=message_store
  echo "(DATABASE_NAME is not set. Using: $database.)"
else
  database=$DATABASE_NAME
fi

function run_psql_file {
  psql $database -q -v ON_ERROR_STOP=1 -f "$1"
}

function script_dir {
  val="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
  echo "$val"
}

function grant-privileges {
  base=$(script_dir)

  echo "» schema privileges"
  run_psql_file $base/privileges/schema.sql

  echo "» messages table privileges"
  run_psql_file $base/privileges/table.sql

  echo "» sequence privileges"
  run_psql_file $base/privileges/sequence.sql

  echo "» functions privileges"
  run_psql_file $base/privileges/functions.sql

  echo "» views privileges"
  run_psql_file $base/privileges/views.sql
}

echo "Granting Privileges"
echo "- - -"
grant-privileges
echo
```

## File: `database/install-views.sh`
```bash
#!/usr/bin/env bash

set -e

if [ -z ${DATABASE_NAME+x} ]; then
  database=message_store
  echo "(DATABASE_NAME is not set. Using: $database.)"
else
  database=$DATABASE_NAME
fi

function run_psql_file {
  psql $database -q -v ON_ERROR_STOP=1 -f "$1"
}

function script_dir {
  val="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
  echo "$val"
}

function create-views {
  base=$(script_dir)

  echo "» stream_summary view"
  run_psql_file $base/views/stream-summary.sql

  echo "» type_summary view"
  run_psql_file $base/views/type-summary.sql

  echo "» stream_type_summary view"
  run_psql_file $base/views/stream-type-summary.sql

  echo "» type_stream_summary view"
  run_psql_file $base/views/type-stream-summary.sql

  echo "» category_type_summary view"
  run_psql_file $base/views/category-type-summary.sql

  echo "» type_category_summary view"
  run_psql_file $base/views/type-category-summary.sql
}

echo "Creating Views"
echo "- - -"
create-views
echo
```

## File: `database/install.sh`
```bash
#!/usr/bin/env bash

set -e

function run_psql {
  psql -q -v ON_ERROR_STOP=1 "$@"
}

function script_dir {
  val="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
  echo "$val"
}

base=$(script_dir)

echo
echo "Installing Database"
echo "Version: $(cat $base/VERSION.txt)"
echo "= = ="

if [ -z ${DATABASE_NAME+x} ]; then
  database=message_store
  echo "DATABASE_NAME is not set. Using: $database."
  export DATABASE_NAME=$database
else
  database=$DATABASE_NAME
fi


if [ -z ${CREATE_DATABASE+x} ]; then
  CREATE_DATABASE="on"
fi

create_database=true
if [ "$CREATE_DATABASE" = "off" ] ; then
  create_database=false
fi


if [ -z ${PGOPTIONS+x} ]; then
  export PGOPTIONS='-c client_min_messages=warning'
fi

function create-user {
  base=$(script_dir)

  echo "» message_store role"
  run_psql postgres -f $base/roles/message-store.sql
}

function create-database {
  echo "» $database database"
  createdb $database
}

function create-schema {
  echo "» message_store schema"
  run_psql $database -f $base/schema/message-store.sql
}

function create-extensions {
  base=$(script_dir)

  echo "» pgcrypto extension"
  run_psql $database -f $base/extensions/pgcrypto.sql
}

function create-table {
  base=$(script_dir)

  echo "» messages table"
  run_psql $database -f $base/tables/messages.sql
}

echo

echo "Creating User"
echo "- - -"
create-user
echo

echo "Creating Database"
echo "- - -"
if [ "$create_database" = true ] ; then
  create-database
else
  echo "Database creation is deactivated. Not creating the database."
fi
echo

echo "Creating Schema"
echo "- - -"
create-schema
echo

echo "Creating Extensions"
echo "- - -"
create-extensions
echo

echo "Creating Table"
echo "- - -"
create-table
echo

# Install functions
source $base/install-functions.sh

# Install indexes
source $base/install-indexes.sh

# Install views
source $base/install-views.sh

# Install privileges
source $base/install-privileges.sh

echo "= = ="
echo "Done Installing Database"
echo "Version: $(cat $base/VERSION.txt)"
echo
```

## File: `database/print-category-type-summary.sh`
```bash
#!/usr/bin/env bash

set -e

echo

default_name=message_store

if [ -z ${DATABASE_USER+x} ]; then
  echo "(DATABASE_USER is not set)"
  user=$default_name
else
  user=$DATABASE_USER
fi
echo "Database user is: $user"

if [ -z ${DATABASE_NAME+x} ]; then
  echo "(DATABASE_NAME is not set)"
  database=$default_name
else
  database=$DATABASE_NAME
fi
echo "Database name is: $database"

if [ -z ${CATEGORY+x} ]; then
  echo "(CATEGORY is not set)"
  category=''
else
  category=$CATEGORY
  echo "Category is: $CATEGORY"
fi

function run_psql_command {
  psql $database -v ON_ERROR_STOP=1 -U $user -P pager=off -c "$1"
}

echo
echo "Category Type Summary"
echo "= = ="
echo

if [ -z $category ]; then
  run_psql_command "SELECT * FROM category_type_summary;"
  run_psql_command "SELECT COUNT(*) AS total_count FROM messages;"
else
  run_psql_command "SELECT * FROM category_type_summary WHERE category LIKE '%$category%';"
  run_psql_command "SELECT COUNT(*) AS total_count FROM messages WHERE category(stream_name) LIKE '%$category%';"
fi
```

## File: `database/print-message-store-version.sh`
```bash
#!/usr/bin/env bash

set -e

echo
echo "Printing Message Store Version"
echo "= = ="
echo

default_name=message_store

if [ -z ${DATABASE_USER+x} ]; then
  echo "(DATABASE_USER is not set)"
  user=$default_name
else
  user=$DATABASE_USER
fi
echo "Database user is: $user"

if [ -z ${DATABASE_NAME+x} ]; then
  echo "(DATABASE_NAME is not set)"
  database=$default_name
else
  database=$DATABASE_NAME
fi
echo "Database name is: $database"

default_table_name=messages

echo

psql $database -v ON_ERROR_STOP=1 -U $user -P pager=off -c "SELECT message_store_version();"
```

## File: `database/print-messages.sh`
```bash
#!/usr/bin/env bash

set -e

echo
echo "Printing Messages"
echo "= = ="
echo

default_name=message_store

if [ -z ${DATABASE_USER+x} ]; then
  echo "(DATABASE_USER is not set)"
  user=$default_name
else
  user=$DATABASE_USER
fi
echo "Database user is: $user"

if [ -z ${DATABASE_NAME+x} ]; then
  echo "(DATABASE_NAME is not set)"
  database=$default_name
else
  database=$DATABASE_NAME
fi
echo "Database name is: $database"

default_table_name=messages

if [ -z ${STREAM_NAME+x} ]; then
  echo "(STREAM_NAME is not set)"
  stream_name=''
else
  stream_name=$STREAM_NAME
  echo "Stream name is: $STREAM_NAME"
fi

function run_psql_command {
  psql $database -v ON_ERROR_STOP=1 -U $user -P pager=off -x -c "$1"
}

echo

if [ -z $stream_name ]; then
  run_psql_command "SELECT * FROM messages ORDER BY global_position ASC"
else
  run_psql_command "SELECT * FROM messages WHERE stream_name = '$stream_name' ORDER BY global_position ASC"
fi
```

## File: `database/print-stream-summary.sh`
```bash
#!/usr/bin/env bash

set -e

echo

default_name=message_store

if [ -z ${DATABASE_USER+x} ]; then
  echo "(DATABASE_USER is not set)"
  user=$default_name
else
  user=$DATABASE_USER
fi
echo "Database user is: $user"

if [ -z ${DATABASE_NAME+x} ]; then
  echo "(DATABASE_NAME is not set)"
  database=$default_name
else
  database=$DATABASE_NAME
fi
echo "Database name is: $database"

if [ -z ${STREAM_NAME+x} ]; then
  echo "(STREAM_NAME is not set)"
  stream_name=''
else
  stream_name=$STREAM_NAME
  echo "Stream name is: $STREAM_NAME"
fi

function run_psql_command {
  psql $database -v ON_ERROR_STOP=1 -U $user -P pager=off -c "$1"
}

echo
echo "Stream Summary"
echo "= = ="
echo

if [ -z $stream_name ]; then
  run_psql_command "SELECT * FROM stream_summary ORDER BY message_count DESC;"
  run_psql_command "SELECT COUNT(*) AS total_count FROM messages;"
else
  run_psql_command "SELECT * FROM stream_summary WHERE stream_name LIKE '%$stream_name%' ORDER BY message_count DESC;"
  run_psql_command "SELECT COUNT(*) AS total_count FROM messages WHERE stream_name LIKE '%$stream_name%';"
fi
```

## File: `database/print-stream-type-summary.sh`
```bash
#!/usr/bin/env bash

set -e

echo

default_name=message_store

if [ -z ${DATABASE_USER+x} ]; then
  echo "(DATABASE_USER is not set)"
  user=$default_name
else
  user=$DATABASE_USER
fi
echo "Database user is: $user"

if [ -z ${DATABASE_NAME+x} ]; then
  echo "(DATABASE_NAME is not set)"
  database=$default_name
else
  database=$DATABASE_NAME
fi
echo "Database name is: $database"

if [ -z ${STREAM_NAME+x} ]; then
  echo "(STREAM_NAME is not set)"
  stream_name=''
else
  stream_name=$STREAM_NAME
  echo "Stream name is: $STREAM_NAME"
fi

function run_psql_command {
  psql $database -v ON_ERROR_STOP=1 -U $user -P pager=off -c "$1"
}

echo
echo "Stream Type Summary"
echo "= = ="
echo

if [ -z $stream_name ]; then
  run_psql_command "SELECT * FROM stream_type_summary ORDER BY stream_name, message_count DESC, type;"
  run_psql_command "SELECT COUNT(*) AS total_count FROM messages;"
else
  run_psql_command "SELECT * FROM stream_type_summary WHERE stream_name LIKE '%$stream_name%' ORDER BY stream_name, message_count DESC;"
  run_psql_command "SELECT COUNT(*) AS total_count FROM messages WHERE stream_name LIKE '%$stream_name%';"
fi
```

## File: `database/print-type-category-summary.sh`
```bash
#!/usr/bin/env bash

set -e

echo

default_name=message_store

if [ -z ${DATABASE_USER+x} ]; then
  echo "(DATABASE_USER is not set)"
  user=$default_name
else
  user=$DATABASE_USER
fi
echo "Database user is: $user"

if [ -z ${DATABASE_NAME+x} ]; then
  echo "(DATABASE_NAME is not set)"
  database=$default_name
else
  database=$DATABASE_NAME
fi
echo "Database name is: $database"

if [ -z ${TYPE+x} ]; then
  echo "(TYPE is not set)"
  type=''
else
  type=$TYPE
  echo "Type is: $TYPE"
fi

function run_psql_command {
  psql $database -v ON_ERROR_STOP=1 -U $user -P pager=off -c "$1"
}

echo
echo "Type Category Summary"
echo "= = ="
echo

if [ -z $type ]; then
  run_psql_command "SELECT * FROM type_category_summary;"
  run_psql_command "SELECT COUNT(*) AS total_count FROM messages;"
else
  run_psql_command "SELECT * FROM type_category_summary WHERE type LIKE '%$type%';"
  run_psql_command "SELECT COUNT(*) AS total_count FROM messages WHERE type LIKE '%$type%';"
fi
```

## File: `database/print-type-stream-summary.sh`
```bash
#!/usr/bin/env bash

set -e

echo

default_name=message_store

if [ -z ${DATABASE_USER+x} ]; then
  echo "(DATABASE_USER is not set)"
  user=$default_name
else
  user=$DATABASE_USER
fi
echo "Database user is: $user"

if [ -z ${DATABASE_NAME+x} ]; then
  echo "(DATABASE_NAME is not set)"
  database=$default_name
else
  database=$DATABASE_NAME
fi
echo "Database name is: $database"

if [ -z ${TYPE+x} ]; then
  echo "(TYPE is not set)"
  type=''
else
  type=$TYPE
  echo "Type is: $TYPE"
fi

function run_psql_command {
  psql $database -v ON_ERROR_STOP=1 -U $user -P pager=off -c "$1"
}

echo
echo "Type Stream Summary"
echo "= = ="
echo

if [ -z $type ]; then
  run_psql_command "SELECT * FROM type_stream_summary ORDER BY type, message_count DESC, stream_name;"
  run_psql_command "SELECT COUNT(*) AS total_count FROM messages;"
else
  run_psql_command "SELECT * FROM type_stream_summary WHERE type LIKE '%$type%' ORDER BY type, message_count DESC, stream_name;"
  run_psql_command "SELECT COUNT(*) AS total_count FROM messages WHERE type LIKE '%$type%';"
fi
```

## File: `database/print-type-summary.sh`
```bash
#!/usr/bin/env bash

set -e

echo

default_name=message_store

if [ -z ${DATABASE_USER+x} ]; then
  echo "(DATABASE_USER is not set)"
  user=$default_name
else
  user=$DATABASE_USER
fi
echo "Database user is: $user"

if [ -z ${DATABASE_NAME+x} ]; then
  echo "(DATABASE_NAME is not set)"
  database=$default_name
else
  database=$DATABASE_NAME
fi
echo "Database name is: $database"

if [ -z ${TYPE+x} ]; then
  echo "(TYPE is not set)"
  type=''
else
  type=$TYPE
  echo "Type is: $TYPE"
fi

function run_psql_command {
  psql $database -v ON_ERROR_STOP=1 -U $user -P pager=off -c "$1"
}

echo
echo "Type Summary"
echo "= = ="
echo

if [ -z $type ]; then
  run_psql_command "SELECT * FROM type_summary ORDER BY message_count DESC;"
  run_psql_command "SELECT COUNT(*) AS total_count FROM messages;"
else
  run_psql_command "SELECT * FROM type_summary WHERE type LIKE '%$type%' ORDER BY message_count DESC;"
  run_psql_command "SELECT COUNT(*) AS total_count FROM messages WHERE type LIKE '%$type%';"
fi
```

## File: `database/uninstall.sh`
```bash
#!/usr/bin/env bash

set -e

function run_psql_command {
  psql -q -v ON_ERROR_STOP=1 -P pager=off postgres -c "$1"
}

function script_dir {
  val="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
  echo "$val"
}

base=$(script_dir)

echo
echo "Uninstalling Database"
echo "Version: $(cat $base/VERSION.txt)"
echo "= = ="

if [ -z ${DATABASE_NAME+x} ]; then
  database=message_store
  echo "DATABASE_NAME is not set. Using: $database."
else
  database=$DATABASE_NAME
fi
echo

if [ -z ${PGOPTIONS+x} ]; then
  export PGOPTIONS='-c client_min_messages=warning'
fi

function delete-user {
  echo "» message_store user"
  run_psql_command "DROP ROLE IF EXISTS message_store;"
}

function delete-database {
  echo "» $database database"
  run_psql_command "DROP DATABASE IF EXISTS \"$database\";"
}

echo "Deleting database"
echo "- - -"
delete-database
echo

echo "Deleting database user"
echo "- - -"
delete-user

echo

echo "= = ="
echo "Done Uninstalling Database"
echo "Version: $(cat $base/VERSION.txt)"
echo
```

## File: `database/update.sh`
```bash
#!/usr/bin/env bash

set -e

echo
echo "WARNING: OBSOLETE"
echo
echo "The ${BASH_SOURCE[0]} has been deprecated"
echo "See the database/update directory for current update scripts"
echo

current_directory="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
update_directory="$current_directory/update"

echo "Contents of $update_directory"
ls -1 $update_directory

echo
```

## File: `database/write-test-message.sh`
```bash
#!/usr/bin/env bash

set -ue

function run_psql {
  psql -v ON_ERROR_STOP=1 "$@"
}

instances=1
if [ ! -z ${INSTANCES+x} ]; then
  instances=$INSTANCES
fi

uuid=$(echo $(uuidgen) | tr '[:upper:]' '[:lower:]')
stream_name="testStream-$uuid"
if [ ! -z ${STREAM_NAME+x} ]; then
  stream_name=$STREAM_NAME
fi

type="SomeType"
if [ ! -z ${TYPE+x} ]; then
  type=$TYPE
fi

title="Writing $instances Messages to Stream $stream_name"
if [ -z ${METADATA+x} ]; then
  metadata="'{\"metaAttribute\": \"some meta value\"}'"
else
  metadata="$METADATA"
  title="$title with Metadata $metadata"
fi

metadata="$metadata::jsonb"

echo
echo $title
echo "= = ="
echo

default_name=message_store

if [ -z ${DATABASE_USER+x} ]; then
  echo "(DATABASE_USER is not set)"
  user=$default_name
else
  user=$DATABASE_USER
fi
echo "Database user is: $user"

if [ -z ${DATABASE_NAME+x} ]; then
  echo "(DATABASE_NAME is not set)"
  database=$default_name
else
  database=$DATABASE_NAME
fi
echo "Database name is: $database"
echo


for (( i=1; i<=instances; i++ )); do
  uuid=$(echo $(uuidgen) | tr '[:upper:]' '[:lower:]')

  echo "Instance: $i, Message ID: $uuid"

  run_psql $database -U $user -c "SELECT write_message('$uuid'::varchar, '$stream_name'::varchar, '$type'::varchar, '{\"attribute\": \"some value\"}'::jsonb, $metadata);" > /dev/null
done


echo
run_psql $database -U $user -P pager=off -x -c "SELECT * FROM messages WHERE stream_name = '$stream_name';"

echo
```

## File: `database/extensions/pgcrypto.sql`
```sql
CREATE EXTENSION IF NOT EXISTS pgcrypto;
```

## File: `database/functions/acquire-lock.sql`
```sql
CREATE OR REPLACE FUNCTION message_store.acquire_lock(
  stream_name varchar
)
RETURNS bigint
AS $$
DECLARE
  _category varchar;
  _category_name_hash bigint;
BEGIN
  _category := category(acquire_lock.stream_name);
  _category_name_hash := hash_64(_category);
  PERFORM pg_advisory_xact_lock(_category_name_hash);

  IF current_setting('message_store.debug_write', true) = 'on' OR current_setting('message_store.debug', true) = 'on' THEN
    RAISE NOTICE '» acquire_lock';
    RAISE NOTICE 'stream_name: %', acquire_lock.stream_name;
    RAISE NOTICE '_category: %', _category;
    RAISE NOTICE '_category_name_hash: %', _category_name_hash;
  END IF;

  RETURN _category_name_hash;
END;
$$ LANGUAGE plpgsql
VOLATILE;
```

## File: `database/functions/cardinal-id.sql`
```sql
CREATE OR REPLACE FUNCTION message_store.cardinal_id(
  stream_name varchar
)
RETURNS varchar
AS $$
DECLARE
  _id varchar;
BEGIN
  _id := id(cardinal_id.stream_name);

  IF _id IS NULL THEN
    RETURN NULL;
  END IF;

  RETURN SPLIT_PART(_id, '+', 1);
END;
$$ LANGUAGE plpgsql
IMMUTABLE;
```

## File: `database/functions/category.sql`
```sql
CREATE OR REPLACE FUNCTION message_store.category(
  stream_name varchar
)
RETURNS varchar
AS $$
BEGIN
  RETURN SPLIT_PART(category.stream_name, '-', 1);
END;
$$ LANGUAGE plpgsql
IMMUTABLE;
```

## File: `database/functions/get-category-messages.sql`
```sql
CREATE OR REPLACE FUNCTION message_store.get_category_messages(
  category varchar,
  "position" bigint DEFAULT 1,
  batch_size bigint DEFAULT 1000,
  correlation varchar DEFAULT NULL,
  consumer_group_member bigint DEFAULT NULL,
  consumer_group_size bigint DEFAULT NULL,
  condition varchar DEFAULT NULL
)
RETURNS SETOF message_store.message
AS $$
DECLARE
  _command text;
BEGIN
  IF NOT is_category(get_category_messages.category) THEN
    RAISE EXCEPTION
      'Must be a category: %',
      get_category_messages.category;
  END IF;

  position := COALESCE(position, 1);
  batch_size := COALESCE(batch_size, 1000);

  _command := '
    SELECT
      id::varchar,
      stream_name::varchar,
      type::varchar,
      position::bigint,
      global_position::bigint,
      data::varchar,
      metadata::varchar,
      time::timestamp
    FROM
      messages
    WHERE
      category(stream_name) = $1 AND
      global_position >= $2';

  IF get_category_messages.correlation IS NOT NULL THEN
    IF position('-' IN get_category_messages.correlation) > 0 THEN
      RAISE EXCEPTION
        'Correlation must be a category (Correlation: %)',
        get_category_messages.correlation;
    END IF;

    _command := _command || ' AND
      category(metadata->>''correlationStreamName'') = $4';
  END IF;

  IF (get_category_messages.consumer_group_member IS NOT NULL AND
      get_category_messages.consumer_group_size IS NULL) OR
      (get_category_messages.consumer_group_member IS NULL AND
      get_category_messages.consumer_group_size IS NOT NULL) THEN

    RAISE EXCEPTION
      'Consumer group member and size must be specified (Consumer Group Member: %, Consumer Group Size: %)',
      get_category_messages.consumer_group_member,
      get_category_messages.consumer_group_size;
  END IF;

  IF get_category_messages.consumer_group_member IS NOT NULL AND
      get_category_messages.consumer_group_size IS NOT NULL THEN

    IF get_category_messages.consumer_group_size < 1 THEN
      RAISE EXCEPTION
        'Consumer group size must not be less than 1 (Consumer Group Member: %, Consumer Group Size: %)',
        get_category_messages.consumer_group_member,
        get_category_messages.consumer_group_size;
    END IF;

    IF get_category_messages.consumer_group_member < 0 THEN
      RAISE EXCEPTION
        'Consumer group member must not be less than 0 (Consumer Group Member: %, Consumer Group Size: %)',
        get_category_messages.consumer_group_member,
        get_category_messages.consumer_group_size;
    END IF;

    IF get_category_messages.consumer_group_member >= get_category_messages.consumer_group_size THEN
      RAISE EXCEPTION
        'Consumer group member must be less than the group size (Consumer Group Member: %, Consumer Group Size: %)',
        get_category_messages.consumer_group_member,
        get_category_messages.consumer_group_size;
    END IF;

    _command := _command || ' AND
      MOD(@hash_64(cardinal_id(stream_name)), $6) = $5';
  END IF;

  IF get_category_messages.condition IS NOT NULL THEN
    IF current_setting('message_store.sql_condition', true) IS NULL OR
        current_setting('message_store.sql_condition', true) = 'off' THEN
      RAISE EXCEPTION
        'Retrieval with SQL condition is not activated';
    END IF;

    _command := _command || ' AND
      (%s)';
    _command := format(_command, get_category_messages.condition);
  END IF;

  _command := _command || '
    ORDER BY
      global_position ASC';

  IF get_category_messages.batch_size != -1 THEN
    _command := _command || '
      LIMIT
        $3';
  END IF;

  IF current_setting('message_store.debug_get', true) = 'on' OR current_setting('message_store.debug', true) = 'on' THEN
    RAISE NOTICE '» get_category_messages';
    RAISE NOTICE 'category ($1): %', get_category_messages.category;
    RAISE NOTICE 'position ($2): %', get_category_messages.position;
    RAISE NOTICE 'batch_size ($3): %', get_category_messages.batch_size;
    RAISE NOTICE 'correlation ($4): %', get_category_messages.correlation;
    RAISE NOTICE 'consumer_group_member ($5): %', get_category_messages.consumer_group_member;
    RAISE NOTICE 'consumer_group_size ($6): %', get_category_messages.consumer_group_size;
    RAISE NOTICE 'condition: %', get_category_messages.condition;
    RAISE NOTICE 'Generated Command: %', _command;
  END IF;

  RETURN QUERY EXECUTE _command USING
    get_category_messages.category,
    get_category_messages.position,
    get_category_messages.batch_size,
    get_category_messages.correlation,
    get_category_messages.consumer_group_member,
    get_category_messages.consumer_group_size::smallint;
END;
$$ LANGUAGE plpgsql
VOLATILE;
```

## File: `database/functions/get-last-stream-message.sql`
```sql
CREATE OR REPLACE FUNCTION message_store.get_last_stream_message(
  stream_name varchar,
  type varchar DEFAULT NULL
)
RETURNS SETOF message_store.message
AS $$
DECLARE
  _command text;
BEGIN
  _command := '
    SELECT
      id::varchar,
      stream_name::varchar,
      type::varchar,
      position::bigint,
      global_position::bigint,
      data::varchar,
      metadata::varchar,
      time::timestamp
    FROM
      messages
    WHERE
      stream_name = $1';

  IF get_last_stream_message.type IS NOT NULL THEN
    _command := _command || ' AND
      type = $2';
  END IF;

  _command := _command || '
    ORDER BY
      position DESC
    LIMIT
      1';

  IF current_setting('message_store.debug_get', true) = 'on' OR current_setting('message_store.debug', true) = 'on' THEN
    RAISE NOTICE '» get_last_message';
    RAISE NOTICE 'stream_name ($1): %', get_last_stream_message.stream_name;
    RAISE NOTICE 'type ($2): %', get_last_stream_message.type;
    RAISE NOTICE 'Generated Command: %', _command;
  END IF;

  RETURN QUERY EXECUTE _command USING
    get_last_stream_message.stream_name,
    get_last_stream_message.type;
END;
$$ LANGUAGE plpgsql
VOLATILE;
```

## File: `database/functions/get-stream-messages.sql`
```sql
CREATE OR REPLACE FUNCTION message_store.get_stream_messages(
  stream_name varchar,
  "position" bigint DEFAULT 0,
  batch_size bigint DEFAULT 1000,
  condition varchar DEFAULT NULL
)
RETURNS SETOF message_store.message
AS $$
DECLARE
  _command text;
  _setting text;
BEGIN
  IF is_category(get_stream_messages.stream_name) THEN
    RAISE EXCEPTION
      'Must be a stream name: %',
      get_stream_messages.stream_name;
  END IF;

  position := COALESCE(position, 0);
  batch_size := COALESCE(batch_size, 1000);

  _command := '
    SELECT
      id::varchar,
      stream_name::varchar,
      type::varchar,
      position::bigint,
      global_position::bigint,
      data::varchar,
      metadata::varchar,
      time::timestamp
    FROM
      messages
    WHERE
      stream_name = $1 AND
      position >= $2';

  IF get_stream_messages.condition IS NOT NULL THEN
    IF current_setting('message_store.sql_condition', true) IS NULL OR
        current_setting('message_store.sql_condition', true) = 'off' THEN
      RAISE EXCEPTION
        'Retrieval with SQL condition is not activated';
    END IF;

    _command := _command || ' AND
      (%s)';
    _command := format(_command, get_stream_messages.condition);
  END IF;

  _command := _command || '
    ORDER BY
      position ASC';

  IF get_stream_messages.batch_size != -1 THEN
    _command := _command || '
      LIMIT
        $3';
  END IF;

  IF current_setting('message_store.debug_get', true) = 'on' OR current_setting('message_store.debug', true) = 'on' THEN
    RAISE NOTICE '» get_stream_messages';
    RAISE NOTICE 'stream_name ($1): %', get_stream_messages.stream_name;
    RAISE NOTICE 'position ($2): %', get_stream_messages.position;
    RAISE NOTICE 'batch_size ($3): %', get_stream_messages.batch_size;
    RAISE NOTICE 'condition ($4): %', get_stream_messages.condition;
    RAISE NOTICE 'Generated Command: %', _command;
  END IF;

  RETURN QUERY EXECUTE _command USING
    get_stream_messages.stream_name,
    get_stream_messages.position,
    get_stream_messages.batch_size;
END;
$$ LANGUAGE plpgsql
VOLATILE;
```

## File: `database/functions/hash-64.sql`
```sql
CREATE OR REPLACE FUNCTION message_store.hash_64(
  value varchar
)
RETURNS bigint
AS $$
DECLARE
  _hash bigint;
BEGIN
  SELECT left('x' || md5(hash_64.value), 17)::bit(64)::bigint INTO _hash;
  return _hash;
END;
$$ LANGUAGE plpgsql
IMMUTABLE;
```

## File: `database/functions/id.sql`
```sql
CREATE OR REPLACE FUNCTION message_store.id(
  stream_name varchar
)
RETURNS varchar
AS $$
DECLARE
  _id_separator_position integer;
BEGIN
  _id_separator_position := STRPOS(id.stream_name, '-');

  IF _id_separator_position = 0 THEN
    RETURN NULL;
  END IF;

  RETURN SUBSTRING(id.stream_name, _id_separator_position + 1);
END;
$$ LANGUAGE plpgsql
IMMUTABLE;
```

## File: `database/functions/is-category.sql`
```sql
CREATE OR REPLACE FUNCTION message_store.is_category(
  stream_name varchar
)
RETURNS boolean
AS $$
BEGIN
  IF NOT STRPOS(is_category.stream_name, '-') = 0 THEN
    RETURN FALSE;
  END IF;

  RETURN TRUE;
END;
$$ LANGUAGE plpgsql
IMMUTABLE;
```

## File: `database/functions/message-store-version.sql`
```sql
CREATE OR REPLACE FUNCTION message_store.message_store_version()
RETURNS varchar
AS $$
BEGIN
  RETURN '1.3.0';
END;
$$ LANGUAGE plpgsql
VOLATILE;
```

## File: `database/functions/stream-version.sql`
```sql
CREATE OR REPLACE FUNCTION message_store.stream_version(
  stream_name varchar
)
RETURNS bigint
AS $$
DECLARE
  _stream_version bigint;
BEGIN
  SELECT
    max(position) into _stream_version
  FROM
    messages
  WHERE
    messages.stream_name = stream_version.stream_name;

  RETURN _stream_version;
END;
$$ LANGUAGE plpgsql
VOLATILE;
```

## File: `database/functions/write-message.sql`
```sql
CREATE OR REPLACE FUNCTION message_store.write_message(
  id varchar,
  stream_name varchar,
  "type" varchar,
  data jsonb,
  metadata jsonb DEFAULT NULL,
  expected_version bigint DEFAULT NULL
)
RETURNS bigint
AS $$
DECLARE
  _message_id uuid;
  _stream_version bigint;
  _next_position bigint;
BEGIN
  PERFORM acquire_lock(write_message.stream_name);

  _stream_version := stream_version(write_message.stream_name);

  IF _stream_version IS NULL THEN
    _stream_version := -1;
  END IF;

  IF write_message.expected_version IS NOT NULL THEN
    IF write_message.expected_version != _stream_version THEN
      RAISE EXCEPTION
        'Wrong expected version: % (Stream: %, Stream Version: %)',
        write_message.expected_version,
        write_message.stream_name,
        _stream_version;
    END IF;
  END IF;

  _next_position := _stream_version + 1;

  _message_id = uuid(write_message.id);

  INSERT INTO messages
    (
      id,
      stream_name,
      position,
      type,
      data,
      metadata
    )
  VALUES
    (
      _message_id,
      write_message.stream_name,
      _next_position,
      write_message.type,
      write_message.data,
      write_message.metadata
    )
  ;

  IF current_setting('message_store.debug_write', true) = 'on' OR current_setting('message_store.debug', true) = 'on' THEN
    RAISE NOTICE '» write_message';
    RAISE NOTICE 'id ($1): %', write_message.id;
    RAISE NOTICE 'stream_name ($2): %', write_message.stream_name;
    RAISE NOTICE 'type ($3): %', write_message.type;
    RAISE NOTICE 'data ($4): %', write_message.data;
    RAISE NOTICE 'metadata ($5): %', write_message.metadata;
    RAISE NOTICE 'expected_version ($6): %', write_message.expected_version;
    RAISE NOTICE '_stream_version: %', _stream_version;
    RAISE NOTICE '_next_position: %', _next_position;
  END IF;

  RETURN _next_position;
END;
$$ LANGUAGE plpgsql
VOLATILE;
```

## File: `database/indexes/messages-category.sql`
```sql
DROP INDEX IF EXISTS message_store.messages_category;

CREATE INDEX messages_category ON message_store.messages (
  message_store.category(stream_name),
  global_position,
  message_store.category(metadata->>'correlationStreamName')
);
```

## File: `database/indexes/messages-id.sql`
```sql
DROP INDEX IF EXISTS message_store.messages_id;

CREATE UNIQUE INDEX messages_id ON message_store.messages (
  id
);
```

## File: `database/indexes/messages-stream.sql`
```sql
DROP INDEX IF EXISTS messages_stream;

CREATE UNIQUE INDEX messages_stream ON message_store.messages (
  stream_name,
  position
);
```

## File: `database/privileges/functions.sql`
```sql
GRANT EXECUTE ON FUNCTION gen_random_uuid() TO message_store;

GRANT EXECUTE ON FUNCTION message_store.acquire_lock(varchar) TO message_store;
GRANT EXECUTE ON FUNCTION message_store.cardinal_id(varchar) TO message_store;
GRANT EXECUTE ON FUNCTION message_store.category(varchar) TO message_store;
GRANT EXECUTE ON FUNCTION message_store.get_category_messages(varchar, bigint, bigint, varchar, bigint, bigint, varchar) TO message_store;
GRANT EXECUTE ON FUNCTION message_store.get_last_stream_message(varchar, varchar) TO message_store;
GRANT EXECUTE ON FUNCTION message_store.get_stream_messages(varchar, bigint, bigint, varchar) TO message_store;
GRANT EXECUTE ON FUNCTION message_store.hash_64(varchar) TO message_store;
GRANT EXECUTE ON FUNCTION message_store.id(varchar) TO message_store;
GRANT EXECUTE ON FUNCTION message_store.is_category(varchar) TO message_store;
GRANT EXECUTE ON FUNCTION message_store.message_store_version() TO message_store;
GRANT EXECUTE ON FUNCTION message_store.stream_version(varchar) TO message_store;
GRANT EXECUTE ON FUNCTION message_store.write_message(varchar, varchar, varchar, jsonb, jsonb, bigint) TO message_store;
```

## File: `database/privileges/schema.sql`
```sql
GRANT USAGE ON SCHEMA message_store TO message_store;
```

## File: `database/privileges/sequence.sql`
```sql
GRANT USAGE, SELECT ON SEQUENCE message_store.messages_global_position_seq TO message_store;
```

## File: `database/privileges/table.sql`
```sql
GRANT SELECT, INSERT ON message_store.messages TO message_store;
```

## File: `database/privileges/views.sql`
```sql
GRANT SELECT ON message_store.category_type_summary TO message_store;
GRANT SELECT ON message_store.stream_summary TO message_store;
GRANT SELECT ON message_store.stream_type_summary TO message_store;
GRANT SELECT ON message_store.type_category_summary TO message_store;
GRANT SELECT ON message_store.type_stream_summary TO message_store;
GRANT SELECT ON message_store.type_summary TO message_store;
```

## File: `database/roles/message-store.sql`
```sql
DO $$
BEGIN
  CREATE ROLE message_store WITH LOGIN;
EXCEPTION
  WHEN duplicate_object THEN
      RAISE NOTICE 'The message_store role already exists';
END$$;
```

## File: `database/schema/message-store.sql`
```sql
CREATE SCHEMA IF NOT EXISTS message_store;
```

## File: `database/tables/messages.sql`
```sql
CREATE TABLE IF NOT EXISTS message_store.messages (
  global_position bigserial NOT NULL,
  position bigint NOT NULL,
  time TIMESTAMP WITHOUT TIME ZONE DEFAULT (now() AT TIME ZONE 'utc') NOT NULL,
  stream_name text NOT NULL,
  type text NOT NULL,
  data jsonb,
  metadata jsonb,
  id UUID NOT NULL DEFAULT gen_random_uuid()
);

ALTER TABLE message_store.messages ADD PRIMARY KEY (global_position) NOT DEFERRABLE INITIALLY IMMEDIATE;
```

## File: `database/types/message.sql`
```sql
DO $$
BEGIN
  DROP TYPE IF EXISTS message_store.message CASCADE;

  CREATE TYPE message_store.message AS (
    id varchar,
    stream_name varchar,
    type varchar,
    position bigint,
    global_position bigint,
    data varchar,
    metadata varchar,
    time timestamp
  );
END$$;
```

## File: `database/update/1.0.0.md`
```markdown
# 1.0.0 Update

Note: Formerly, `postgres-message-store`.

The following changes are made by the 1.0.0.sh update script:

- **Note: There are no changes to the `messages` table, and no data migration is necessary**
- The executables named `evt-pg-*` are renamed to `mdb-*`
- **[breaking change]** The `get_category_messages` server function supports pub/sub directly by receiving a `correlation` argument and composing the correlation metadata query condition directly in the server function ([http://docs.eventide-project.org/user-guide/message-db/server-functions.html#get-messages-from-a-category](http://docs.eventide-project.org/user-guide/message-db/server-functions.html#get-messages-from-a-category))
- **[breaking change]** The message_store database and its objects are contained in a Postgres schema named `message_store`
- **[breaking change]** The `get_category_messages` server function supports consumer groups via the `consumer_group_member` and `consumer_group_size` parameters ([http://docs.eventide-project.org/user-guide/message-db/server-functions.html#get-messages-from-a-category](http://docs.eventide-project.org/user-guide/message-db/server-functions.html#get-messages-from-a-category))
- The retrieval server functions provide debugging output that is activated via the Postgres setting, `message_store.debug_get` ([http://docs.eventide-project.org/user-guide/message-db/server-functions.html#debugging-output](http://docs.eventide-project.org/user-guide/message-db/server-functions.html#debugging-output))
- The write server function provides debugging output that is activated via the Postgres setting, `message_store.debug_write` ([http://docs.eventide-project.org/user-guide/message-db/server-functions.html#debugging-output](http://docs.eventide-project.org/user-guide/message-db/server-functions.html#debugging-output))
- The `message_store.debug` Postgres setting activates both the retrieval and write debug output ([http://docs.eventide-project.org/user-guide/message-db/server-functions.html#debugging-output](http://docs.eventide-project.org/user-guide/message-db/server-functions.html#debugging-output))
- `id` stream parsing function ([http://docs.eventide-project.org/user-guide/message-db/server-functions.html#get-the-id-from-a-stream-name](http://docs.eventide-project.org/user-guide/message-db/server-functions.html#get-the-id-from-a-stream-name))
- `cardinal_id` stream parsing function ([http://docs.eventide-project.org/user-guide/message-db/server-functions.html#get-the-cardinal-id-from-a-stream-name](http://docs.eventide-project.org/user-guide/message-db/server-functions.html#get-the-cardinal-id-from-a-stream-name))
- `acquire_lock` function encapsulates the application of the advisory lock used by the `write_message` function ([http://docs.eventide-project.org/user-guide/message-db/server-functions.html#get-message-store-database-schema-version](http://docs.eventide-project.org/user-guide/message-db/server-functions.html#get-message-store-database-schema-version))
- Database management tool output is clarified
- **[breaking change]** All server function parameter names are no longer named with underscore prefixes ([http://docs.eventide-project.org/user-guide/message-db/server-functions.html](http://docs.eventide-project.org/user-guide/message-db/server-functions.html))
- Indexes are no longer built with the `CONCURRENTLY` option ([http://docs.eventide-project.org/user-guide/message-db/anatomy.html#source-code](http://docs.eventide-project.org/user-guide/message-db/anatomy.html#source-code))
- **[breaking change]** The `messages_category_global_position_idx` is removed and replaced with the `messages_category` index, which now indexes correlation metadata
- **[breaking change]** The `messages_stream_name_position_uniq_idx` is removed and replaced with the `messages_stream` index, which now indexes correlation metadata
- **[breaking change]** The `messages_id_uniq_idx` is removed and replaced with the `messages_id` index
- Message DB RubyGem: [https://github.com/message-db/ruby-gem](https://github.com/message-db/ruby-gem)
- Message DB NPM Module: [https://github.com/message-db/npm-module](https://github.com/message-db/npm-module)
- Improvements to interactive tests ([https://github.com/eventide-project/message-store-postgres/tree/master/test](https://github.com/eventide-project/message-store-postgres/tree/master/test))
```

## File: `database/update/1.0.0.sh`
```bash
#!/usr/bin/env bash

set -e

echo
echo "Message DB"
echo
echo "Update the message_store database"
echo
echo "WARNING:"
echo "This script updates a pre-v1 message_store database to Message DB v1.x"
echo "Do not run this script on a Message DB v1 database"
echo
echo "Fore more information about the changes made to the message store by"
echo "this update, see: https://github.com/message-db/message-db/blob/master/database/update/1.0.0.md"
echo
echo "- Press CTRL+C to stop this script from running"
echo "- Press RETURN to allow the script to proceed"
echo
read

function script_dir {
  val="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
  echo "$val"
}

base="$(script_dir)/.."
echo $base

echo
echo "Updating Database"
echo "Version: $(cat $base/VERSION.txt)"
echo "= = ="

if [ -z ${DATABASE_NAME+x} ]; then
  echo "(DATABASE_NAME is not set. Default will be used.)"
  database=message_store
  export DATABASE_NAME=$database
else
  database=$DATABASE_NAME
fi
echo

if [ -z ${PGOPTIONS+x} ]; then
  export PGOPTIONS='-c client_min_messages=warning'
fi

function delete-extensions {
  echo "» pgcrypto extension"
  psql $database -q -c "DROP EXTENSION IF EXISTS pgcrypto";
}

function delete-indexes {
  echo "» messages_id_uniq_idx index"
  psql $database -q -c "DROP INDEX IF EXISTS messages_id_uniq_idx CASCADE";

  echo "» messages_stream_name_position_uniq_idx index"
  psql $database -q -c "DROP INDEX IF EXISTS messages_stream_name_position_uniq_idx";

  echo "» messages_category_global_position_idx index"
  psql $database -q -c "DROP INDEX IF EXISTS messages_category_global_position_idx";
}

function delete-views {
  echo "» stream_summary view"
  psql $database -q -c "DROP VIEW IF EXISTS stream_summary CASCADE";

  echo "» type_summary view"
  psql $database -q -c "DROP VIEW IF EXISTS type_summary CASCADE";

  echo "» stream_type_summary view"
  psql $database -q -c "DROP VIEW IF EXISTS stream_type_summary CASCADE";

  echo "» type_stream_summary view"
  psql $database -q -c "DROP VIEW IF EXISTS type_stream_summary CASCADE";

  echo "» category_type_summary view"
  psql $database -q -c "DROP VIEW IF EXISTS category_type_summary CASCADE";

  echo "» type_category_summary view"
  psql $database -q -c "DROP VIEW IF EXISTS type_category_summary CASCADE";
}

function delete-functions {
  echo "» hash_64 function"
  psql $database -q -c "DROP FUNCTION IF EXISTS hash_64 CASCADE";

  echo "» category function"
  psql $database -q -c "DROP FUNCTION IF EXISTS category CASCADE";

  echo "» stream_version function"
  psql $database -q -c "DROP FUNCTION IF EXISTS stream_version CASCADE";

  echo "» write_message function"
  psql $database -q -c "DROP FUNCTION IF EXISTS write_message CASCADE";

  echo "» get_stream_messages function"
  psql $database -q -c "DROP FUNCTION IF EXISTS get_stream_messages CASCADE";

  echo "» get_category_messages function"
  psql $database -q -c "DROP FUNCTION IF EXISTS get_category_messages CASCADE";

  echo "» get_last_message function"
  psql $database -q -c "DROP FUNCTION IF EXISTS get_last_message CASCADE";
}

function delete-extensions {
  echo "» pgcrypto extension"
  psql $database -q -c "DROP EXTENSION IF EXISTS pgcrypto CASCADE";
}

function create-schema {
  echo "» message_store schema"
  psql $database -q -f $base/schema/message-store.sql
}

function add-table-to-schema {
  echo "» messages table"
  psql $database -q -c "ALTER TABLE messages SET SCHEMA message_store";
}

function create-extensions {
  echo "» pgcrypto extension"
  psql $database -q -f $base/extensions/pgcrypto.sql
}

function set-default-value {
  echo "» id column"
  psql $database -q -c "ALTER TABLE message_store.messages ALTER COLUMN id SET DEFAULT gen_random_uuid()";
}

echo "Deleting Views"
echo "- - -"
delete-views
echo

echo "Deleting Indexes"
echo "- - -"
delete-indexes
echo

echo "Deleting Functions"
echo "- - -"
delete-functions
echo

echo "Deleting Extensions"
echo "- - -"
delete-extensions
echo

echo "Creating Schema"
echo "- - -"
create-schema
echo

echo "Creating Extensions"
echo "- - -"
create-extensions
echo

echo "Adding Table to Schema"
echo "- - -"
add-table-to-schema
echo

echo "Set Default Value for ID Column"
echo "- - -"
set-default-value
echo

# Install functions
source $base/install-functions.sh

# Install indexes
source $base/install-indexes.sh

# Install views
source $base/install-views.sh

# Install privileges
source $base/install-privileges.sh

echo "= = ="
echo "Done Updating Database"
echo "Version: $(cat $base/VERSION.txt)"
echo
```

## File: `database/update/1.2.2.md`
```markdown
# 1.2.2 Update

Note: There are no backward-incompatible changes in this update.

This update requires the execution of the v1.2.2 update script: `1.2.2.sh`. For instructions on applying update scripts, see:

[http://docs.eventide-project.org/user-guide/message-db/update.html](http://docs.eventide-project.org/user-guide/message-db/update.html)

The following changes are made by the 1.2.2.sh update script:

- The `get_category_messages` server function will return the entire, unlimited extent of messages in a category if -1 is sent as the `batch_size` argument
- The `get_stream_messages` server function will return the entire, unlimited extent of messages in a stream if -1 is sent as the `batch_size` argument
```

## File: `database/update/1.2.2.sh`
```bash
#!/usr/bin/env bash

set -e

echo
echo "Message DB"
echo
echo "Update the message_store database to v1.2.2"
echo
echo "WARNING:"
echo "This script updates a post-v1 message_store database to Message DB v1.2.2"
echo "Do not run this script on a Message DB pre-v1 database"
echo
echo "Fore more information about the changes made to the message store by"
echo "this update, see: https://github.com/message-db/message-db/blob/master/database/update/1.2.2.md"
echo
echo "- Press CTRL+C to stop this script from running"
echo "- Press RETURN to allow the script to proceed"
echo

read

function script_dir {
  val="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
  echo "$val"
}

base="$(script_dir)/.."
echo $base

echo
echo "Updating Database"
echo "Version: $(cat $base/VERSION.txt)"
echo "= = ="

if [ -z ${DATABASE_NAME+x} ]; then
  echo "(DATABASE_NAME is not set. Default will be used.)"
  database=message_store
  export DATABASE_NAME=$database
else
  database=$DATABASE_NAME
fi
echo

if [ -z ${PGOPTIONS+x} ]; then
  export PGOPTIONS='-c client_min_messages=warning'
fi

function install-functions {
  echo "» get_stream_messages function"
  psql $database -q -f $base/functions/get-stream-messages.sql

  echo "» get_category_messages function"
  psql $database -q -f $base/functions/get-category-messages.sql
}

echo "Installing Functions"
echo "- - -"
install-functions
echo

echo "= = ="
echo "Done Updating Database"
echo "Version: $(cat $base/VERSION.txt)"
echo
```

## File: `database/update/1.3.0.md`
```markdown
# 1.3.0 Update

Note: There are no backward-incompatible changes in this update.

For more information about Message DB update scripts, see:

[http://docs.eventide-project.org/user-guide/message-db/update.html](http://docs.eventide-project.org/user-guide/message-db/update.html)

The following changes are made by the v1.3.0 update script:

- The `get_last_stream_message` function is replaced with an implementation that receives the additional `type` argument that constrains the result to the last message of a stream of a specified message type (see: [http://docs.eventide-project.org/user-guide/message-db/server-functions.html#get-last-message-from-a-stream](http://docs.eventide-project.org/user-guide/message-db/server-functions.html#get-last-message-from-a-stream))
- Grants the execution privilege for the new `get_last_stream_message` function implementation to the `message_store` role
- The database installation scripts terminate on error, rather than proceeding with the rest of the installation when a script error occurs, as was the case with previous versions
```

## File: `database/update/1.3.0.sh`
```bash
#!/usr/bin/env bash

set -e

echo
echo "Message DB"
echo
echo "Update the message_store database to v1.3.0"
echo
echo "Fore more information about the changes made to the message store by"
echo "this update, see: https://github.com/message-db/message-db/blob/master/database/update/1.3.0.md"
echo
echo "- Press CTRL+C to cancel"
echo "- Press RETURN to proceed with the update"
echo

read

function run_psql {
  psql $database -q -v ON_ERROR_STOP=1 -c "$@"
}

function run_psql_file {
  psql $database -q -v ON_ERROR_STOP=1 -f "$1"
}

function script_dir {
  val="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
  echo "$val"
}

base="$(script_dir)/.."
echo $base

echo
echo "Updating Database"
echo "Version: 1.3.0"
echo "= = ="

if [ -z ${DATABASE_NAME+x} ]; then
  echo "(DATABASE_NAME is not set. Default will be used.)"
  database=message_store
  export DATABASE_NAME=$database
else
  database=$DATABASE_NAME
fi
echo

if [ -z ${PGOPTIONS+x} ]; then
  export PGOPTIONS='-c client_min_messages=warning'
fi

function delete-functions {
  echo "» get_last_message function"
  run_psql "DROP FUNCTION IF EXISTS message_store.get_last_stream_message(varchar) CASCADE";

  echo "» message_store_version function"
  run_psql "DROP FUNCTION IF EXISTS message_store.message_store_version CASCADE";
}

function install-functions {
  echo "» get_last_stream_message function"
  run_psql_file $base/functions/get-last-stream-message.sql

  echo "» message_store_version function"
  run_psql_file $base/functions/message-store-version.sql
}

function grant-privileges {
  echo "» get_last_stream_message function privilege"
  run_psql "GRANT EXECUTE ON FUNCTION message_store.get_last_stream_message(varchar, varchar) TO message_store;"

  echo "» message_store_version function"
  run_psql "GRANT EXECUTE ON FUNCTION message_store.message_store_version TO message_store;"
}

echo "Deleting Functions"
echo "- - -"
delete-functions
echo

echo "Installing Functions"
echo "- - -"
install-functions
echo

echo "Granting Privileges to the Function"
echo "- - -"
grant-privileges
echo

echo "= = ="
echo "Done Updating Database"
echo "Version: 1.3.0"
echo
```

## File: `database/views/category-type-summary.sql`
```sql
CREATE OR REPLACE VIEW message_store.category_type_summary AS
  WITH
    type_count AS (
      SELECT
        message_store.category(stream_name) AS category,
        type,
        COUNT(id) AS message_count
      FROM
        message_store.messages
      GROUP BY
        category,
        type
    ),

    total_count AS (
      SELECT
        COUNT(id)::decimal AS total_count
      FROM
        message_store.messages
    )

  SELECT
    category,
    type,
    message_count,
    ROUND((message_count / total_count)::decimal * 100, 2) AS percent
  FROM
    type_count,
    total_count
  ORDER BY
    category,
    type;
```

## File: `database/views/stream-summary.sql`
```sql
CREATE OR REPLACE VIEW message_store.stream_summary AS
  WITH
    stream_count AS (
      SELECT
        stream_name,
        COUNT(id) AS message_count
      FROM
        message_store.messages
      GROUP BY
        stream_name
    ),

    total_count AS (
      SELECT
        COUNT(id)::decimal AS total_count
      FROM
        message_store.messages
    )

  SELECT
    stream_name,
    message_count,
    ROUND((message_count / total_count)::decimal * 100, 2) AS percent
  FROM
    stream_count,
    total_count
  ORDER BY
    stream_name;
```

## File: `database/views/stream-type-summary.sql`
```sql
CREATE OR REPLACE VIEW message_store.stream_type_summary AS
  WITH
    type_count AS (
      SELECT
        stream_name,
        type,
        COUNT(id) AS message_count
      FROM
        message_store.messages
      GROUP BY
        stream_name,
        type
    ),

    total_count AS (
      SELECT
        COUNT(id)::decimal AS total_count
      FROM
        message_store.messages
    )

  SELECT
    stream_name,
    type,
    message_count,
    ROUND((message_count / total_count)::decimal * 100, 2) AS percent
  FROM
    type_count,
    total_count
  ORDER BY
    stream_name,
    type;
```

## File: `database/views/type-category-summary.sql`
```sql
CREATE OR REPLACE VIEW message_store.type_category_summary AS
  WITH
    type_count AS (
      SELECT
        type,
        message_store.category(stream_name) AS category,
        COUNT(id) AS message_count
      FROM
        message_store.messages
      GROUP BY
        type,
        category
    ),

    total_count AS (
      SELECT
        COUNT(id)::decimal AS total_count
      FROM
        message_store.messages
    )

  SELECT
    type,
    category,
    message_count,
    ROUND((message_count / total_count)::decimal * 100, 2) AS percent
  FROM
    type_count,
    total_count
  ORDER BY
    type,
    category;
```

## File: `database/views/type-stream-summary.sql`
```sql
CREATE OR REPLACE VIEW message_store.type_stream_summary AS
  WITH
    type_count AS (
      SELECT
        type,
        stream_name,
        COUNT(id) AS message_count
      FROM
        message_store.messages
      GROUP BY
        type,
        stream_name
    ),

    total_count AS (
      SELECT
        COUNT(id)::decimal AS total_count
      FROM
        message_store.messages
    )

  SELECT
    type,
    stream_name,
    message_count,
    ROUND((message_count / total_count)::decimal * 100, 2) AS percent
  FROM
    type_count,
    total_count
  ORDER BY
    type,
    stream_name;
```

## File: `database/views/type-summary.sql`
```sql
CREATE OR REPLACE VIEW message_store.type_summary AS
  WITH
    type_count AS (
      SELECT
        type,
        COUNT(id) AS message_count
      FROM
        message_store.messages
      GROUP BY
        type
    ),

    total_count AS (
      SELECT
        COUNT(id)::decimal AS total_count
      FROM
        message_store.messages
    )

  SELECT
    type,
    message_count,
    ROUND((message_count / total_count)::decimal * 100, 2) AS percent
  FROM
    type_count,
    total_count
  ORDER BY
    type;
```

## File: `test/_controls.sh`
```bash
source test/_controls/category.sh
source test/_controls/id.sh
source test/_controls/type.sh
source test/_controls/stream-name.sh
source test/_controls/compound-id-stream-name.sh
source test/_controls/write-message.sh
source test/_controls/write-message-correlated.sh
```

## File: `test/acquire-lock.sh`
```bash
#!/usr/bin/env bash

set -e

echo
echo "ACQUIRE LOCK"
echo "============"
echo

source test/_controls.sh

stream_name=$(stream-name)

echo "Stream Name:"
echo $stream_name
echo

psql message_store -U message_store -x -c "SELECT acquire_lock('$stream_name');"

echo "= = ="
echo
```

## File: `test/hash-64.sh`
```bash
#!/usr/bin/env bash

set -e

echo
echo "GET HASH 64"
echo "==========="
echo

source test/_controls.sh

stream_name=$(stream-name)

echo "Stream Name:"
echo $stream_name
echo

psql message_store -U message_store -x -c "SELECT hash_64('$stream_name');"

echo "= = ="
echo
```

## File: `test/message-store-version.sh`
```bash
#!/usr/bin/env bash

set -e

echo
echo "PRINT MESSAGE STORE VERSION"
echo "==========================="
echo "- Retrieve message store database schema version from the message_store_version server function"
echo

database/print-message-store-version.sh

echo "= = ="
echo
```

## File: `test/_controls/category.sh`
```bash
function category {
  local uuid=$(echo $(uuidgen) | tr '[:upper:]' '[:lower:]')
  local category_suffix=${uuid:0:8}
  local category="${1:-testStream}X$category_suffix"
  echo $category
}
```

## File: `test/_controls/compound-id-stream-name.sh`
```bash
function compound-id-stream-name {
  local category=${1:-$(category)}
  local cardinal_id=${2:-$(id)}
  local stream_name="$category-$cardinal_id+$(id)"
  echo $stream_name
}
```

## File: `test/_controls/id.sh`
```bash
function id {
  local uuid=$(echo $(uuidgen) | tr '[:upper:]' '[:lower:]')
  echo $uuid
}
```

## File: `test/_controls/stream-name.sh`
```bash
function stream-name {
  local category=${1:-$(category)}
  local stream_name="$category-$(id)"
  echo $stream_name
}
```

## File: `test/_controls/type.sh`
```bash
function type {
  type="SomeType"
  echo $type
}
```

## File: `test/_controls/write-message-correlated.sh`
```bash
function write-message-correlated {
  local stream_name=${1:-$(stream-name)}
  local instances=${2:-1}
  local correlation_stream_name=${3:-"someCorrelation"}

  if [ ! -z ${CORRELATION+x} ]; then
    correlation_stream_name=$CORRELATION
  fi

  metadata="'{\"correlationStreamName\": \"$correlation_stream_name\"}'"

  METADATA=$metadata STREAM_NAME=$stream_name INSTANCES=$instances database/write-test-message.sh > /dev/null
}
```

## File: `test/_controls/write-message.sh`
```bash
function write-message {
  local stream_name=${1:-$(stream-name)}
  local instances=${2:-1}
  STREAM_NAME=$stream_name INSTANCES=$instances database/write-test-message.sh > /dev/null
}
```

## File: `test/_query-plan/get-category-messages-consumer-group-correlated.sh`
```bash
#!/usr/bin/env bash

set -e

echo
echo "QUERY PLAN - GET CATEGORY MESSAGES - CONSUMER GROUP - CORRELATED"
echo "================================================================"
echo "- Write 2 messages each to 5 entity streams in the same category"
echo "- Retrieve a batch of messages from the category, starting at global position 0 and matching the correlation category"
echo

source test/_controls.sh

category=$(category)
echo "Category:"
echo $category
echo

correlation=$(category)
correlation_stream_name=$(stream-name $correlation)
echo "Correlation:"
echo $correlation
echo

for i in {1..1000}; do
  stream_name=$(stream-name $category)

  echo "Stream Name: $stream_name"

  write-message-correlated $stream_name 1
  write-message-correlated $stream_name 1 $correlation_stream_name
done
echo

cmd="
  LOAD 'auto_explain';
  SET auto_explain.log_min_duration = 0;
  SET auto_explain.log_nested_statements=on;
  EXPLAIN ANALYZE SELECT * FROM get_category_messages('$category', correlation => '$correlation', consumer_group_member => 0, consumer_group_size => 2);
"

echo "Command:"
echo "$cmd"
echo

psql message_store -P pager=off -x -c "$cmd"

echo "= = ="
echo
```

## File: `test/_query-plan/get-category-messages-correlated.sh`
```bash
#!/usr/bin/env bash

set -e

echo
echo "QUERY PLAN - GET CATEGORY MESSAGES - CORRELATED"
echo "==============================================="
echo "- Write 2 messages each to 3 entity streams in the same category"
echo "- Retrieve a batch of 2 messages from the category, starting at global position 0 and matching the correlation category"
echo

source test/_controls.sh

category=$(category)
echo "Category:"
echo $category
echo

correlation=$(category)
correlation_stream_name=$(stream-name $correlation)
echo "Correlation:"
echo $correlation
echo

for i in {1..3}; do
  stream_name=$(stream-name $category)

  echo "Stream Name: $stream_name"

  write-message-correlated $stream_name 1
  write-message-correlated $stream_name 1 $correlation_stream_name
done
echo

cmd="
  LOAD 'auto_explain';
  SET auto_explain.log_min_duration = 0;
  SET auto_explain.log_nested_statements=on;
  EXPLAIN ANALYZE SELECT * FROM get_category_messages('$category', 0, 2, correlation => '$correlation');
"

echo "Command:"
echo "$cmd"
echo

psql message_store -P pager=off -x -c "$cmd"

echo "= = ="
echo
```

## File: `test/_query-plan/get-category-messages.sh`
```bash
#!/usr/bin/env bash

set -e

echo
echo "QUERY PLAN - GET CATEGORY MESSAGES"
echo "=================================="
echo "- Write 2 messages each to 3 entity streams in the same category"
echo "- Retrieve a batch of messages from the category"
echo

source test/_controls.sh

category=$(category)

echo "Category:"
echo $category
echo

for i in {1..3}; do
  stream_name=$(stream-name $category)
  echo $stream_name
  write-message $stream_name 2
done
echo

cmd="
  LOAD 'auto_explain';
  SET auto_explain.log_min_duration = 0;
  SET auto_explain.log_nested_statements=on;
  EXPLAIN ANALYZE SELECT * FROM get_category_messages('$category');
"

echo "Command:"
echo "$cmd"
echo

psql message_store -P pager=off -x -c "$cmd"

echo "= = ="
echo
```

## File: `test/_query-plan/get-stream-messages-correlated.sh`
```bash
#!/usr/bin/env bash

set -e

echo
echo "ANALYZE QUERY PLAN - GET STREAM MESSAGES CORRELATED"
echo "==================================================="
echo "- Write 3 messages to an entity stream"
echo "- Retrieve a batch of messages from the stream matching the correlation category"
echo

source test/_controls.sh

correlation=$(category)
correlation_stream_name=$(stream-name $correlation)
echo "Correlation:"
echo $correlation
echo

stream_name=$(stream-name)

echo "Stream Name:"
echo $stream_name
echo

write-message-correlated $stream_name 1
write-message-correlated $stream_name 2 $correlation_stream_name

cmd="
  LOAD 'auto_explain';
  SET auto_explain.log_min_duration = 0;
  SET auto_explain.log_nested_statements=on;
  EXPLAIN ANALYZE SELECT * FROM get_stream_messages('$stream_name', correlation => '$correlation');
"

echo "Command:"
echo "$cmd"
echo

psql message_store -P pager=off -x -c "$cmd"

echo "= = ="
echo
```

## File: `test/_query-plan/get-stream-messages.sh`
```bash
#!/usr/bin/env bash

set -e

echo
echo "QUERY PLAN - GET STREAM MESSAGES"
echo "================================"
echo "- Write 3 messages to an entity stream"
echo "- Retrieve a batch of messages from the stream"
echo

source test/_controls.sh

stream_name=$(stream-name)

echo "Stream Name:"
echo $stream_name
echo

write-message $stream_name 3

cmd="
  LOAD 'auto_explain';
  SET auto_explain.log_min_duration = 0;
  SET auto_explain.log_nested_statements=on;
  EXPLAIN ANALYZE SELECT * FROM get_stream_messages('$stream_name');
"

echo "Command:"
echo "$cmd"
echo

psql message_store -P pager=off -x -c "$cmd"

echo "= = ="
echo
```

## File: `test/cardinal-id/category.sh`
```bash
#!/usr/bin/env bash

set -e

echo
echo "CARDINAL ID - FROM CATEGORY"
echo "==========================="
echo

source test/_controls.sh

stream_name=$(category)

echo "Stream Name:"
echo $stream_name
echo

psql message_store -U message_store -x -c "SELECT cardinal_id('$stream_name');"

echo "= = ="
echo
```

## File: `test/cardinal-id/stream-name-with-compound-id.sh`
```bash
#!/usr/bin/env bash

set -e

echo
echo "CARDINAL ID - FROM STREAM NAME WITH COMPOUND ID"
echo "==============================================="
echo

source test/_controls.sh

stream_name=$(compound-id-stream-name)

echo "Stream Name:"
echo $stream_name
echo

psql message_store -U message_store -x -c "SELECT cardinal_id('$stream_name');"

echo "= = ="
echo
```

## File: `test/cardinal-id/stream-name-with-single-id.sh`
```bash
#!/usr/bin/env bash

set -e

echo
echo "CARDINAL ID - FROM STREAM NAME WITH SINGLE ID"
echo "============================================="
echo

source test/_controls.sh

stream_name=$(stream-name)

echo "Stream Name:"
echo $stream_name
echo

psql message_store -U message_store -x -c "SELECT cardinal_id('$stream_name');"

echo "= = ="
echo
```

## File: `test/category/category.sh`
```bash
#!/usr/bin/env bash

set -e

echo
echo "CATEGORY - FROM CATEGORY"
echo "========================"
echo

source test/_controls.sh

category=$(category)

echo "Category:"
echo $category
echo

psql message_store -U message_store -x -c "SELECT category('$category');"

echo "= = ="
echo
```

## File: `test/category/stream-name.sh`
```bash
#!/usr/bin/env bash

set -e

echo
echo "CATEGORY - FROM STREAM NAME"
echo "==========================="
echo

source test/_controls.sh

stream_name=$(stream-name)

echo "Stream Name:"
echo $stream_name
echo

psql message_store -U message_store -x -c "SELECT category('$stream_name');"

echo "= = ="
echo
```

## File: `test/get-category-messages/error-not-category.sh`
```bash
#!/usr/bin/env bash

set -e

echo
echo "GET CATEGORY MESSAGES - ERROR - NOT CATEGORY"
echo "============================================"
echo "- Retrieve a batch of messages from the category using a stream name instead of a category"
echo "- Terminates with an error"
echo

source test/_controls.sh

stream_name=$(stream-name)

cmd="SELECT * FROM get_category_messages('$stream_name');"

echo "Command:"
echo "$cmd"
echo

set +e
psql message_store -U message_store -P pager=off -x -c "$cmd"
set -e

echo "= = ="
echo
```

## File: `test/get-category-messages/get-category-messages.sh`
```bash
#!/usr/bin/env bash

set -e

echo
echo "GET CATEGORY MESSAGES"
echo "====================="
echo "- Write 2 messages each to 3 entity streams in the same category"
echo "- Retrieve a batch of messages from the category"
echo

source test/_controls.sh

category=$(category)

echo "Category:"
echo $category
echo

for i in {1..3}; do
  stream_name=$(stream-name $category)
  echo $stream_name
  write-message $stream_name 2
done
echo

cmd="SELECT * FROM get_category_messages('$category');"

echo "Command:"
echo "$cmd"
echo

psql message_store -U message_store -P pager=off -x -c "$cmd"

echo "= = ="
echo
```

## File: `test/get-category-messages/batch_size/limited.sh`
```bash
#!/usr/bin/env bash

set -e

echo
echo "GET CATEGORY MESSAGES - BATCH SIZE - LIMTED"
echo "==========================================="
echo "- Write 2 messages each to 3 entity streams in the same category"
echo "- Retrieve a batch of 2 messages from the category"
echo

source test/_controls.sh

category=$(category)

echo "Category:"
echo $category
echo

for i in {1..3}; do
  stream_name=$(stream-name $category)
  echo $stream_name
  write-message $stream_name 2
done
echo

cmd="SELECT * FROM get_category_messages('$category', batch_size => 2);"

echo "Command:"
echo "$cmd"
echo

psql message_store -U message_store -P pager=off -x -c "$cmd"

echo "= = ="
echo
```

## File: `test/get-category-messages/batch_size/unlimited.sh`
```bash
#!/usr/bin/env bash

set -e

echo
echo "GET CATEGORY MESSAGES - BATCH SIZE - UNLIMTED"
echo "============================================="
echo "- Write 2 messages each to 3 entity streams in the same category"
echo "- Retrieve an unlimited batch of messages from the category"
echo

source test/_controls.sh

category=$(category)

echo "Category:"
echo $category
echo

for i in {1..3}; do
  stream_name=$(stream-name $category)
  echo $stream_name
  write-message $stream_name 2
done
echo

cmd="SELECT * FROM get_category_messages('$category', batch_size => -1);"

echo "Command:"
echo "$cmd"
echo

psql message_store -U message_store -P pager=off -x -c "$cmd"

echo "= = ="
echo
```

## File: `test/get-category-messages/condition/condition-correlated.sh`
```bash
#!/usr/bin/env bash

set -e

echo
echo "GET CATEGORY MESSAGES - CONDITION CORRELATED"
echo "============================================"
echo "- Write 2 messages each to 3 entity streams in the same category"
echo "- Retrieve a batch of 2 messages from the category, starting at global position 0, where the position is greater than or equal to 1, and matching the correlation category"
echo

source test/_controls.sh

category=$(category)
echo "Category:"
echo $category
echo

correlation=$(category)
correlation_stream_name=$(stream-name $correlation)
echo "Correlation:"
echo $correlation
echo

for i in {1..3}; do
  stream_name=$(stream-name $category)

  echo "Stream Name: $stream_name"

  write-message-correlated $stream_name 1
  write-message-correlated $stream_name 1 $correlation_stream_name
done
echo

cmd="SELECT * FROM get_category_messages('$category', 0, 2, correlation => '$correlation', condition => 'position >= 1');"

echo "Command:"
echo "$cmd"
echo

PGOPTIONS='-c message_store.sql_condition=on' psql message_store -U message_store -P pager=off -x -c "$cmd"

echo "= = ="
echo
```

## File: `test/get-category-messages/condition/condition.sh`
```bash
#!/usr/bin/env bash

set -e

echo
echo "GET CATEGORY MESSAGES - CONDITION"
echo "================================="
echo "- Write 2 messages each to 3 entity streams in the same category"
echo "- Retrieve a batch of 2 messages from the category, starting at global position 0 where the position is greater than or equal to 1"
echo

source test/_controls.sh

category=$(category)

echo "Category:"
echo $category
echo

for i in {1..3}; do
  stream_name=$(stream-name $category)
  echo $stream_name
  write-message $stream_name 2
done
echo

cmd="SELECT * FROM get_category_messages('$category', 0, 2, condition => 'position >= 1');"

echo "Command:"
echo "$cmd"
echo

PGOPTIONS='-c message_store.sql_condition=on' psql message_store -U message_store -P pager=off -x -c "$cmd"

echo "= = ="
echo
```

## File: `test/get-category-messages/condition/error-deactivated.sh`
```bash
#!/usr/bin/env bash

set -e

echo
echo "ERROR - GET CATEGORY MESSAGES - CONDITION - FEATURE DEACTIVATED"
echo "==============================================================="
echo "- Retrieve a batch of messages from the category using the SQL condition when the SQL condition feature is deactivated"
echo "- Terminates with an error"
echo

source test/_controls.sh

category=$(category)

echo "Category:"
echo $category
echo

cmd="SELECT * FROM get_category_messages('$category', condition => 'position >= 1');"

echo "Command:"
echo "$cmd"
echo

set +e
PGOPTIONS='-c message_store.sql_condition=off' psql message_store -U message_store -P pager=off -x -c "$cmd"
set -e

echo "= = ="
echo
```

## File: `test/get-category-messages/condition/error-not-activated.sh`
```bash
#!/usr/bin/env bash

set -e

echo
echo "ERROR - GET CATEGORY MESSAGES - CONDITION - FEATURE NOT ACTIVATED"
echo "================================================================="
echo "- Retrieve a batch of messages from the category using the SQL condition when the SQL condition feature is deactivated"
echo "- Terminates with an error"
echo

source test/_controls.sh

category=$(category)

echo "Category:"
echo $category
echo

cmd="SELECT * FROM get_category_messages('$category', condition => 'position >= 1');"

echo "Command:"
echo "$cmd"
echo

set +e
psql message_store -U message_store -P pager=off -x -c "$cmd"
set -e

echo "= = ="
echo
```

## File: `test/get-category-messages/consumer-group/consumer-group.sh`
```bash
#!/usr/bin/env bash

set -e

echo
echo "GET CATEGORY MESSAGES - CONSUMER GROUP"
echo "======================================"
echo "- Write 10 messages to 2 entity streams in the same category but with different cardinal IDs"
echo "- Retrieve a batch of messages from the category that match the consumer group conditions"
echo

source test/_controls.sh

category=$(category)
echo "Category:"
echo $category
echo


cardinal_id_1=$(id)
echo "Cardinal ID 1:"
echo $cardinal_id_1
echo

for i in {1..10}; do
  stream_name=$(compound-id-stream-name $category $cardinal_id_1)

  echo "Stream Name: $stream_name"

  write-message-correlated $stream_name
done
echo


cardinal_id_2=$(id)
echo "Cardinal ID 2:"
echo $cardinal_id_2
echo

for i in {1..10}; do
  stream_name=$(compound-id-stream-name $category $cardinal_id_2)

  echo "Stream Name: $stream_name"

  write-message-correlated $stream_name
done
echo


cmd="SELECT * FROM get_category_messages('$category');"
cmd_0="SELECT * FROM get_category_messages('$category', consumer_group_member => 0, consumer_group_size => 2);"
cmd_1="SELECT * FROM get_category_messages('$category', consumer_group_member => 1, consumer_group_size => 2);"

echo "Command:"
echo "$cmd"
echo

echo "Command 0:"
echo "$cmd_0"
echo

echo "Command 1:"
echo "$cmd_1"
echo

psql message_store -U message_store -P pager=off -x -c "$cmd"
echo
psql message_store -U message_store -P pager=off -x -c "$cmd_0"
echo
psql message_store -U message_store -P pager=off -x -c "$cmd_1"


cmd_count="SELECT COUNT(*) AS total FROM get_category_messages('$category');"
cmd_count_0="SELECT COUNT(*) AS modulo_0 FROM get_category_messages('$category', consumer_group_member => 0, consumer_group_size => 2);"
cmd_count_1="SELECT COUNT(*) AS modulo_1 FROM get_category_messages('$category', consumer_group_member => 1, consumer_group_size => 2);"

echo "Command Count:"
echo "$cmd_count"
echo

echo "Command Count 0:"
echo "$cmd_count_0"
echo

echo "Command Count 1:"
echo "$cmd_count_1"
echo

psql message_store -U message_store -P pager=off -x -c "$cmd_count"
echo
psql message_store -U message_store -P pager=off -x -c "$cmd_count_0"
echo
psql message_store -U message_store -P pager=off -x -c "$cmd_count_1"

echo "= = ="
echo
```

## File: `test/get-category-messages/consumer-group/correlated.sh`
```bash
#!/usr/bin/env bash

set -e

echo
echo "GET CATEGORY MESSAGES - CONSUMER GROUP - CORRELATED"
echo "==================================================="
echo "- Write 2 messages each to 10 entity streams in the same category"
echo "- Half of the messages have a different cardinal ID that the other half"
echo "- Retrieve messages from the category that match the consumer group conditions"
echo

source test/_controls.sh

category=$(category)
echo "Category:"
echo $category
echo

correlation=$(category)
correlation_stream_name=$(stream-name $correlation)
echo "Correlation:"
echo $correlation
echo


cardinal_id_1=$(id)
echo "Cardinal ID 1:"
echo $cardinal_id_1
echo

for i in {1..5}; do
  stream_name=$(compound-id-stream-name $category $cardinal_id_1)

  echo "Stream Name: $stream_name"

  write-message-correlated $stream_name 1
  write-message-correlated $stream_name 1 $correlation_stream_name
done
echo


cardinal_id_2=$(id)
echo "Cardinal ID 2:"
echo $cardinal_id_2
echo

for i in {1..5}; do
  stream_name=$(compound-id-stream-name $category $cardinal_id_2)

  echo "Stream Name: $stream_name"

  write-message-correlated $stream_name 1
  write-message-correlated $stream_name 1 $correlation_stream_name
done
echo


echo "All messages written to the category"
echo

cmd="SELECT * FROM get_category_messages('$category');"

echo "Command:"
echo "$cmd"
echo

psql message_store -U message_store -P pager=off -x -c "$cmd"


echo "Correlated messages written to the category for consumer member 0"
echo

cmd="SELECT * FROM get_category_messages('$category', 0, 10, correlation => '$correlation', consumer_group_member => 0, consumer_group_size => 2);"

echo "Command:"
echo "$cmd"
echo

psql message_store -U message_store -P pager=off -x -c "$cmd"


echo "A batch of 1 message written to the category for consumer member 0 greater than global position 2"
echo

cmd="SELECT * FROM get_category_messages('$category', 2, 1, correlation => '$correlation', consumer_group_member => 0, consumer_group_size => 2);"

echo "Command:"
echo "$cmd"
echo

psql message_store -U message_store -P pager=off -x -c "$cmd"

echo "= = ="
echo
```

## File: `test/get-category-messages/consumer-group/error/group-member-equal-to-group-size.sh`
```bash
#!/usr/bin/env bash

set -e

echo
echo "GET CATEGORY MESSAGES - CONSUMER GROUP - ERROR - GROUP MEMBER EQUAL TO GROUP SIZE"
echo "================================================================================="
echo "- Retrieve a batch of messages from the category with a consumer group member equal to the group size"
echo "- Terminates with an error"
echo

source test/_controls.sh

cmd="SELECT * FROM get_category_messages('someCategory', consumer_group_member => 1, consumer_group_size => 1);"

echo "Command:"
echo "$cmd"
echo

set +e
psql message_store -U message_store -P pager=off -x -c "$cmd"
set -e

echo "= = ="
echo
```

## File: `test/get-category-messages/consumer-group/error/group-member-greater-than-group-size.sh`
```bash
#!/usr/bin/env bash

set -e

echo
echo "GET CATEGORY MESSAGES - CONSUMER GROUP - ERROR - GROUP MEMBER GREATER THAN GROUP SIZE"
echo "====================================================================================="
echo "- Retrieve a batch of messages from the category with a consumer group member equals the group size"
echo "- Terminates with an error"
echo

source test/_controls.sh

cmd="SELECT * FROM get_category_messages('someCategory', consumer_group_member => 2, consumer_group_size => 1);"

echo "Command:"
echo "$cmd"
echo

set +e
psql message_store -U message_store -P pager=off -x -c "$cmd"
set -e

echo "= = ="
echo
```

## File: `test/get-category-messages/consumer-group/error/group-member-too-small.sh`
```bash
#!/usr/bin/env bash

set -e

echo
echo "GET CATEGORY MESSAGES - CONSUMER GROUP - ERROR - GROUP MEMBER TOO SMALL"
echo "======================================================================="
echo "- Retrieve a batch of messages from the category with a consumer group member that is too small"
echo "- Terminates with an error"
echo

source test/_controls.sh

cmd="SELECT * FROM get_category_messages('someCategory', consumer_group_member => -1, consumer_group_size => 1);"

echo "Command:"
echo "$cmd"
echo

set +e
psql message_store -U message_store -P pager=off -x -c "$cmd"
set -e

echo "= = ="
echo
```

## File: `test/get-category-messages/consumer-group/error/group-size-too-small.sh`
```bash
#!/usr/bin/env bash

set -e

echo
echo "GET CATEGORY MESSAGES - CONSUMER GROUP - ERROR - GROUP SIZE TOO SMALL"
echo "====================================================================="
echo "- Retrieve a batch of messages from the category with a consumer group size that is too small"
echo "- Terminates with an error"
echo

source test/_controls.sh

cmd="SELECT * FROM get_category_messages('someCategory', consumer_group_member => 0, consumer_group_size => 0);"

echo "Command:"
echo "$cmd"
echo

set +e
psql message_store -U message_store -P pager=off -x -c "$cmd"
set -e

echo "= = ="
echo
```

## File: `test/get-category-messages/consumer-group/error/missing-group-member.sh`
```bash
#!/usr/bin/env bash

set -e

echo
echo "GET CATEGORY MESSAGES - CONSUMER GROUP - ERROR - MISSING GROUP MEMBER"
echo "====================================================================="
echo "- Retrieve a batch of messages from the category, omitting the consumer group member argument"
echo "- Terminates with an error"
echo

source test/_controls.sh

cmd="SELECT * FROM get_category_messages('someCategory', consumer_group_member => 1);"

echo "Command:"
echo "$cmd"
echo

set +e
psql message_store -U message_store -P pager=off -x -c "$cmd"
set -e

echo "= = ="
echo
```

## File: `test/get-category-messages/consumer-group/error/missing-group-size.sh`
```bash
#!/usr/bin/env bash

set -e

echo
echo "GET CATEGORY MESSAGES - CONSUMER GROUP - ERROR - MISSING GROUP SIZE"
echo "==================================================================="
echo "- Retrieve a batch of messages from the category, omitting the consumer group size argument"
echo "- Terminates with an error"
echo

source test/_controls.sh

cmd="SELECT * FROM get_category_messages('someCategory', consumer_group_size => 1);"

echo "Command:"
echo "$cmd"
echo

set +e
psql message_store -U message_store -P pager=off -x -c "$cmd"
set -e

echo "= = ="
echo
```

## File: `test/get-category-messages/correlated/correlated.sh`
```bash
#!/usr/bin/env bash

set -e

echo
echo "GET CATEGORY MESSAGES - CORRELATED"
echo "=================================="
echo "- Write 2 messages each to 3 entity streams in the same category"
echo "- Retrieve a batch of 2 messages from the category, starting at global position 0 and matching the correlation category"
echo

source test/_controls.sh

category=$(category)
echo "Category:"
echo $category
echo

correlation=$(category)
correlation_stream_name=$(stream-name $correlation)
echo "Correlation:"
echo $correlation
echo

for i in {1..3}; do
  stream_name=$(stream-name $category)

  echo "Stream Name: $stream_name"

  write-message-correlated $stream_name 1
  write-message-correlated $stream_name 1 $correlation_stream_name
done
echo

cmd="SELECT * FROM get_category_messages('$category', 0, 2, correlation => '$correlation');"

echo "Command:"
echo "$cmd"
echo

psql message_store -U message_store -P pager=off -x -c "$cmd"

echo "= = ="
echo
```

## File: `test/get-category-messages/correlated/error-stream-name.sh`
```bash
#!/usr/bin/env bash

set -e

echo
echo "GET CATEGORY MESSAGES - CORRELATED STREAM NAME ERROR"
echo "===================================================="
echo "- Retrieve a messages using a stream name as the correlation value"
echo "- Terminates with an error"
echo

source test/_controls.sh

category=$(category)
echo "Category:"
echo $category
echo

stream_name=$(stream-name)

echo "Stream Name:"
echo $stream_name
echo

cmd="SELECT * FROM get_category_messages('$category', correlation => '$stream_name');"

echo "Command:"
echo "$cmd"
echo

set +e
psql message_store -U message_store -P pager=off -x -c "$cmd"
set -e

echo "= = ="
echo
```

## File: `test/get-last-stream-message/get-last-stream-message.sh`
```bash
#!/usr/bin/env bash

set -e

echo
echo "GET LAST STREAM MESSAGE"
echo "====================================="
echo "- Write 2 messages to an entity stream"
echo "- Retrieve the last message in the stream"
echo

source test/_controls.sh

stream_name=$(stream-name)

echo "Stream Name:"
echo $stream_name
echo

STREAM_NAME=$stream_name INSTANCES=2 database/write-test-message.sh > /dev/null

cmd="SELECT * FROM get_last_stream_message('$stream_name');"

echo "Command:"
echo "$cmd"
echo

psql message_store -U message_store -P pager=off -x -c "$cmd"

echo "= = ="
echo
```

## File: `test/get-last-stream-message/type.sh`
```bash
#!/usr/bin/env bash

set -e

echo
echo "GET LAST STREAM MESSAGE - TYPE"
echo "====================================="
echo "- Write 2 messages to an entity stream of type"
echo "- Write 1 messages to an entity stream of another type"
echo "- Retrieve the last message in the stream of the first type"
echo

source test/_controls.sh

stream_name=$(stream-name)

echo "Stream Name:"
echo $stream_name
echo

type=$(type)
echo "Type:"
echo $type
echo

other_type="SomeOtherType"
echo "Other Type:"
echo $other_type
echo

STREAM_NAME=$stream_name TYPE=$type INSTANCES=2 database/write-test-message.sh > /dev/null
STREAM_NAME=$stream_name TYPE=$other_type INSTANCES=1 database/write-test-message.sh > /dev/null

cmd="SELECT * FROM get_last_stream_message('$stream_name', '$type');"

echo "Command:"
echo "$cmd"
echo

psql message_store -U message_store -P pager=off -x -c "$cmd"

echo "= = ="
echo
```

## File: `test/get-stream-messages/error-not-stream-name.sh`
```bash
#!/usr/bin/env bash

set -e

echo
echo "GET STREAM MESSAGES - ERROR - NOT STREAM NAME"
echo "============================================="
echo "- Retrieve a batch of messages from the stream using a category instead of a stream name"
echo "- Terminates with an error"
echo

source test/_controls.sh

category=$(category)

cmd="SELECT * FROM get_stream_messages('$category');"

echo "Command:"
echo "$cmd"
echo

set +e
psql message_store -U message_store -P pager=off -x -c "$cmd"
set -e

echo "= = ="
echo
```

## File: `test/get-stream-messages/get-stream-messages.sh`
```bash
#!/usr/bin/env bash

set -e

echo
echo "GET STREAM MESSAGES"
echo "==================="
echo "- Write 3 messages to an entity stream"
echo "- Retrieve a batch of messages from the stream"
echo

source test/_controls.sh

stream_name=$(stream-name)

echo "Stream Name:"
echo $stream_name
echo

write-message $stream_name 3

cmd="SELECT * FROM get_stream_messages('$stream_name');"

echo "Command:"
echo "$cmd"
echo

psql message_store -U message_store -P pager=off -x -c "$cmd"

echo "= = ="
echo
```

## File: `test/get-stream-messages/batch_size/limited.sh`
```bash
#!/usr/bin/env bash

set -e

echo
echo "GET STREAM MESSAGES - BATCH SIZE - LIMTED"
echo "========================================="
echo "- Write 3 messages to an entity stream"
echo "- Retrieve a batch of 2 messages from the stream"
echo

source test/_controls.sh

stream_name=$(stream-name)

echo "Stream Name:"
echo $stream_name
echo

write-message $stream_name 3

cmd="SELECT * FROM get_stream_messages('$stream_name', batch_size => 2);"

echo "Command:"
echo "$cmd"
echo

psql message_store -U message_store -P pager=off -x -c "$cmd"

echo "= = ="
echo
```

## File: `test/get-stream-messages/batch_size/unlimited.sh`
```bash
#!/usr/bin/env bash

set -e

echo
echo "GET STREAM MESSAGES - BATCH SIZE - UNLIMTED"
echo "==========================================="
echo "- Write 3 messages to an entity stream"
echo "- Retrieve an unlimited batch of messages from the stream"
echo

source test/_controls.sh

stream_name=$(stream-name)

echo "Stream Name:"
echo $stream_name
echo

write-message $stream_name 3

cmd="SELECT * FROM get_stream_messages('$stream_name', batch_size => -1);"

echo "Command:"
echo "$cmd"
echo

psql message_store -U message_store -P pager=off -x -c "$cmd"

echo "= = ="
echo
```

## File: `test/get-stream-messages/condition/condition.sh`
```bash
#!/usr/bin/env bash

set -e

echo
echo "GET STREAM MESSAGES - CONDITION"
echo "==============================="
echo "- Write 3 messages to an entity stream"
echo "- Retrieve a batch of 2 messages from the stream, starting at position 0 where the global position is greater than or equal to 1"
echo

source test/_controls.sh

stream_name=$(stream-name)

echo "Stream Name:"
echo $stream_name
echo

write-message $stream_name 3

cmd="SELECT * FROM get_stream_messages('$stream_name', 0, 2, condition => 'global_position >= 1');"

echo "Command:"
echo "$cmd"
echo

PGOPTIONS='-c message_store.sql_condition=on' psql message_store -U message_store -P pager=off -x -c "$cmd"

echo "= = ="
echo
```

## File: `test/get-stream-messages/condition/error-deactivated.sh`
```bash
#!/usr/bin/env bash

set -e

echo
echo "ERROR - GET STREAM MESSAGES - CONDITION - FEATURE DEACTIVATED"
echo "============================================================="
echo "- Retrieve a batch of messages from the stream using the SQL condition when the SQL condition feature is deactivated"
echo "- Terminates with an error"
echo

source test/_controls.sh

stream_name=$(stream-name)

echo "Stream Name:"
echo $stream_name
echo

cmd="SELECT * FROM get_stream_messages('$stream_name', condition => 'position >= 1');"

echo "Command:"
echo "$cmd"
echo

set +e
PGOPTIONS='-c message_store.sql_condition=off' psql message_store -U message_store -P pager=off -x -c "$cmd"
set -e

echo "= = ="
echo
```

## File: `test/get-stream-messages/condition/error-not-activated.sh`
```bash
#!/usr/bin/env bash

set -e

echo
echo "ERROR - GET STREAM MESSAGES - CONDITION - FEATURE NOT ACTIVATED"
echo "==============================================================="
echo "- Retrieve a batch of messages from the stream using the SQL condition when the SQL condition feature is deactivated"
echo "- Terminates with an error"
echo

source test/_controls.sh

stream_name=$(stream-name)

echo "Stream Name:"
echo $stream_name
echo

cmd="SELECT * FROM get_stream_messages('$stream_name', condition => 'position >= 1');"

echo "Command:"
echo "$cmd"
echo

set +e
psql message_store -U message_store -P pager=off -x -c "$cmd"
set -e

echo "= = ="
echo
```

## File: `test/id/category.sh`
```bash
#!/usr/bin/env bash

set -e

echo
echo "ID - FROM CATEGORY"
echo "=================="
echo

source test/_controls.sh

stream_name=$(category)

echo "Stream Name:"
echo $stream_name
echo

psql message_store -U message_store -x -c "SELECT id('$stream_name');"

echo "= = ="
echo
```

## File: `test/id/stream-name.sh`
```bash
#!/usr/bin/env bash

set -e

echo
echo "ID - FROM STREAM NAME"
echo "====================="
echo

source test/_controls.sh

stream_name=$(stream-name)

echo "Stream Name:"
echo $stream_name
echo

psql message_store -U message_store -x -c "SELECT id('$stream_name');"

echo "= = ="
echo
```

## File: `test/id/compound-id/stream-name.sh`
```bash
#!/usr/bin/env bash

set -e

echo
echo "GET ID FROM STREAM NAME WITH COMPOUND ID"
echo "========================================"
echo

source test/_controls.sh

stream_name=$(compound-id-stream-name)

echo "Stream Name:"
echo $stream_name
echo

psql message_store -U message_store -x -c "SELECT id('$stream_name');"

echo "= = ="
echo
```

## File: `test/is_category/category.sh`
```bash
#!/usr/bin/env bash

set -e

echo
echo "IS CATEGORY - CATEGORY"
echo "======================"
echo

source test/_controls.sh

category=$(category)

echo "Category:"
echo $category
echo

psql message_store -U message_store -x -c "SELECT is_category('$category');"

echo "= = ="
echo
```

## File: `test/is_category/stream-name.sh`
```bash
#!/usr/bin/env bash

set -e

echo
echo "IS CATEGORY - STREAM NAME"
echo "========================="
echo

source test/_controls.sh

stream_name=$(stream-name)

echo "Stream Name:"
echo $stream_name
echo

psql message_store -U message_store -x -c "SELECT is_category('$stream_name');"

echo "= = ="
echo
```

## File: `test/reports/category-type-summary.sh`
```bash
#!/usr/bin/env bash

set -e

echo
echo "PRINT CATEGORY TYPE SUMMARY"
echo "==========================="
echo "- Write 3 messages to 3 entity streams"
echo "- Print the category type summary"
echo

source test/_controls.sh

write-message
write-message
write-message

database/print-category-type-summary.sh

echo "= = ="
echo
```

## File: `test/reports/messages.sh`
```bash
#!/usr/bin/env bash

set -e

echo
echo "PRINT MESSAGES"
echo "=============="
echo "- Write 3 messages to an entity stream"
echo "- Print the messages in the stream"
echo

source test/_controls.sh

stream_name=$(stream-name)

echo "Stream Name:"
echo $stream_name

write-message $stream_name 3

STREAM_NAME=$stream_name database/print-messages.sh

echo "= = ="
echo
```

## File: `test/reports/stream-summary.sh`
```bash
#!/usr/bin/env bash

set -e

echo
echo "PRINT STREAM SUMMARY"
echo "===================="
echo "- Write 3 messages to an entity stream"
echo "- Write a messages to another entity stream"
echo "- Print the message summary for the stream"
echo

source test/_controls.sh

stream_name=$(stream-name)

echo "Stream Name:"
echo $stream_name

write-message $stream_name 3
write-message

STREAM_NAME=$stream_name database/print-stream-summary.sh

echo "= = ="
echo
```

## File: `test/reports/stream-type-summary.sh`
```bash
#!/usr/bin/env bash

set -e

echo
echo "PRINT STREAM TYPE SUMMARY"
echo "========================="
echo "- Write 3 messages to an entity streams"
echo "- Write a messages to 2 other entity streams"
echo "- Print the stream type summary"
echo

source test/_controls.sh

stream_name=$(stream-name)

echo "Stream Name:"
echo $stream_name

write-message $stream_name 3
write-message
write-message

STREAM_NAME=$stream_name database/print-stream-type-summary.sh

echo "= = ="
echo
```

## File: `test/reports/type-category-summary.sh`
```bash
#!/usr/bin/env bash

set -e

echo
echo "PRINT TYPE CATEGORY SUMMARY"
echo "==========================="
echo "- Write 3 messages to 3 entity streams"
echo "- Print the type category summary"
echo

source test/_controls.sh

write-message
write-message
write-message

database/print-type-category-summary.sh

echo "= = ="
echo
```

## File: `test/reports/type-stream-summary.sh`
```bash
#!/usr/bin/env bash

set -e

echo
echo "PRINT TYPE STREAM SUMMARY"
echo "========================="
echo "- Write 3 messages to 3 entity streams"
echo "- Print the type stream summary"
echo

source test/_controls.sh

write-message
write-message
write-message

database/print-type-stream-summary.sh

echo "= = ="
echo
```

## File: `test/reports/type-summary.sh`
```bash
#!/usr/bin/env bash

set -e

echo
echo "PRINT TYPE SUMMARY"
echo "=================="
echo "- Write 3 messages to 3 entity streams"
echo "- Print the type summary"
echo

source test/_controls.sh

write-message
write-message
write-message

database/print-type-summary.sh

echo "= = ="
echo
```

## File: `test/stream-version/stream-version.sh`
```bash
#!/usr/bin/env bash

set -e

echo
echo "STREAM VERSION"
echo "=============="
echo "- Write 2 messages to an entity stream"
echo "- Retrieve stream version"
echo

source test/_controls.sh

stream_name=$(stream-name)

echo "Stream Name:"
echo $stream_name
echo

write-message $stream_name 2

cmd="SELECT * FROM stream_version('$stream_name');"

echo "Command:"
echo "$cmd"
echo

psql message_store -U message_store -P pager=off -x -c "$cmd"

echo "= = ="
echo
```

## File: `test/write-message/expected-version-error.sh`
```bash
#!/usr/bin/env bash

set -e

echo
echo "WRITE MESSAGE - EXPECTED VERSION ERROR"
echo "======================================"
echo "- Write a single message to an entity stream"
echo "- Write another message with the expected version of 1 that does not match a stream with one message"
echo "- Terminates with an error"
echo

source test/_controls.sh

stream_name=$(stream-name)

echo "Stream Name:"
echo $stream_name
echo

type=$(type)

write-message $stream_name

cmd="SELECT write_message(gen_random_uuid()::varchar, '$stream_name'::varchar, '$type'::varchar, '{\"attribute\": \"some value\"}'::jsonb, '{\"metaAttribute\": \"some meta value\"}'::jsonb, 1::bigint);"

echo "Command:"
echo "$cmd"
echo

set +e
psql message_store -U message_store -x -c "$cmd"
set -e

echo "= = ="
echo
```

## File: `test/write-message/expected-version.sh`
```bash
#!/usr/bin/env bash

set -e

echo
echo "WRITE MESSAGE - EXPECTED VERSION"
echo "================================"
echo "- Write a single message to an entity stream"
echo "- Write another message with the expected version of 0 that matches a stream with one message"
echo

source test/_controls.sh

stream_name=$(stream-name)

echo "Stream Name:"
echo $stream_name
echo

type=$(type)

write-message $stream_name

cmd="SELECT write_message(gen_random_uuid()::varchar, '$stream_name'::varchar, '$type'::varchar, '{\"attribute\": \"some value\"}'::jsonb, '{\"metaAttribute\": \"some meta value\"}'::jsonb, 0::bigint);"

echo "Command:"
echo "$cmd"
echo

psql message_store -U message_store -x -c "$cmd"

echo "= = ="
echo
```

## File: `test/write-message/write-message.sh`
```bash
#!/usr/bin/env bash

set -e

echo
echo "WRITE MESSAGE"
echo "============="
echo "Write a single message to an entity stream"
echo

source test/_controls.sh

stream_name=$(stream-name)

echo "Stream Name:"
echo $stream_name
echo

type=$(type)

cmd="SELECT write_message(gen_random_uuid()::varchar, '$stream_name'::varchar, '$type'::varchar, '{\"attribute\": \"some value\"}'::jsonb, '{\"metaAttribute\": \"some meta value\"}'::jsonb);"

echo "Command:"
echo "$cmd"
echo

psql message_store -U message_store -x -c "$cmd"

psql message_store -U message_store -P pager=off -x -c "SELECT * FROM messages WHERE stream_name = '$stream_name';"

echo "= = ="
echo
```


---
id: iddd
type: knowledge
owner: OA_Triage
---
# iddd
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
These are the sample Bounded Contexts from the book
"Implementing Domain-Driven Design" by Vaughn Vernon:

http://vaughnvernon.co/?page_id=168

The models and surrounding architectural mechanisms
may be in various states of flux as the are refined
over time. Some tests may be incomplete. The code is
not meant to be a reflection of a production quality
work, but rather as a set of reference projects for
the book.

Points of Interest
==================

The iddd_agilepm project uses a key-value store as
its underlying persistence mechanism, and in particular
is LevelDB. Actually the LevelDB in use is a pure Java
implementation: https://github.com/dain/leveldb

Currently iddd_agilepm doesn't employ a container of
any kind (such as Spring).

The iddd_collaboration project uses Event Sourcing and
CQRS. It purposely avoids the use of an object-relational
mapper, showing that a simple JDBC-based query engine
and DTO matter can be used instead. This technique does
have its limitations, but it is meant to be small and fast
and require no configuration or annotations. It is not
meant to be perfect.

It may be helpful to make one additional mental note on
the iddd_collaboration CQRS implementation. To keep the
example simple it persists the Event Sourced write model
and the CQRS read model in one thread. Since two different
stores are used--LevelDB for the Event Journal and MySQL
for the read model--there may be very slight opportunities
for inconsistency, but not much. The idea was to keep the
two models as close to consistent as possible without
using the same data storage (and transaction) for both.
Two different storage mechanisms were used purposely to
demonstrate that they can be separate.

The iddd_identityaccess project uses object-relational
mapping (Hibernate), but so as not to leave it "boring" it
provides a RESTful client interface and even publishes
Domain-Event notifications via REST (logs) and RabbitMQ.

Finally the iddd_common project provides a number of reusable
components. This is not an attempt to be a framework, but
just leverages reuse to the degree that code copying doesn't
liter each project. This is not a recommendation, but it
did work well and save a considerable amount of work while
producing the samples.

Usage
=====

Requires
--------

- Java 7 (8+ does not work)
- MySQL Client + Server
- RabbitMQ

Setup (with Docker)
-------------------

To make it easy to run the tests and it requirements,
the `startContainers.sh` script is provided. Which
will start a:
- MySQL Server container
- RabbitMQ Server container
- RabbitMQ Management container

If the `mysql` command is available, which is the mysql client,
also the required SQL scripts will be imported into the MySQL
Server.

If you use the `startContainers.sh` script, you don't need
MySQL Server and RabbitMQ installed locally. Instead,
Docker needs to be installed as the script will start
MySQL and RabbitMQ in Docker containers.

Build
------

You can build the project by running:

```
./gradlew build
```

This automatically downloads Gradle and builds the project, including running the tests.

The Gradle build using Maven repositories was provided by
Michael Andrews (Github michaelajr and Twitter @MichaelAJr).
Thanks much!


I hope you benefit from the samples.

Vaughn Vernon
Author: Implementing Domain-Driven Design
Twitter: @VaughnVernon
http://vaughnvernon.co/

```

### File: README.txt
```txt
These are the sample Bounded Contexts for C#.NET from the book "Implementing Domain-Driven Design" by Vaughn Vernon: http://vaughnvernon.co/?page_id=168 

Java Samples: https://github.com/VaughnVernon/IDDD_Samples

NOTE: These are currently an early work in progress. It's
been pushed here so contributors can create pull requests,
etc.

Please don't complain unless you are willing to help ;)

Vaughn
```

### File: LICENSE.txt
```txt
//   Copyright 2012,2013 Vaughn Vernon
//
//   Licensed under the Apache License, Version 2.0 (the "License");
//   you may not use this file except in compliance with the License.
//   You may obtain a copy of the License at
//
//       http://www.apache.org/licenses/LICENSE-2.0
//
//   Unless required by applicable law or agreed to in writing, software
//   distributed under the License is distributed on an "AS IS" BASIS,
//   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
//   See the License for the specific language governing permissions and
//   limitations under the License.


```

### File: startContainers.sh
```sh
#!/bin/bash

host="0.0.0.0"

mysqlUser="root"
mysqlPassword="root"
mysqlContainerName="iddd-mysql"
mysqlPort="3306"

rabbitmqNodeName="$(hostname)"
rabbitmqContainerName="iddd-rabbitmq"
rabbitmqManagementHttpPort="8080"

containers[0]="${mysqlContainerName}"
containers[1]="${rabbitmqContainerName}"

function start() {
    echo "Starting MySQL Server container..."
    docker rm -f "${mysqlContainerName}"
    docker run --name "${mysqlContainerName}" -p "${mysqlPort}":3306 -e MYSQL_ROOT_PASSWORD="${mysqlPassword}" -d mysql

    echo "Waiting for MySQL Server to be up and running..."
    waitForContainer "${mysqlContainerName}" "mysqld: ready for connections."

    local testSqlFiles="$(find $(pwd) -name *.sql | grep -i "test")"
    local sqlFiles="$(find $(pwd) -name *.sql | grep -vi "test")"
    if which mysql > /dev/null; then
        for sql in ${testSqlFiles}; do
            echo "Importing [${sql}]"
            $(mysql --host="${host}"  --port=3306 --protocol=TCP --user="${mysqlUser}" --password="${mysqlPassword}" < ${sql})
        done
        for sql in ${sqlFiles}; do
            echo "Importing [${sql}]"
            $(mysql --host="${host}" --port=3306 --protocol=TCP --user="${mysqlUser}" --password="${mysqlPassword}" < ${sql})
        done
    else
        echo -e
        echo "!! mysql command not found"
        echo "!! You need to import the following SQL files into MySQL Server, yourself:"
        for sql in ${testSqlFiles}; do
            echo ${sql}
        done
        for sql in ${sqlFiles}; do
            echo ${sql}
        done
        echo -e
        echo "You can find MySQL Server on [localhost] port [${mysqlPort}]"
        echo -e
        read -rsp "Press any key to continue..."
        echo -e
    fi

    echo "Starting RabbitMQ container..."
    docker rm -f "${rabbitmqContainerName}"
    docker run --name "${rabbitmqContainerName}" -p 5672:5672 -p "${rabbitmqManagementHttpPort}":15672 -e RABBITMQ_NODENAME="${rabbitmqNodeName}" -d rabbitmq:3-management
    echo "Waiting for RabbitMQ to be up and running..."
    waitForContainer "${rabbitmqContainerName}" "Server startup complete;"

    echo -e
    echo "RabbitMQ Management available at [http://localhost:${rabbitmqManagementHttpPort}]"
    echo "(Login with user/pass of [guest/guest])"
}

function status() {
    docker ps -a | head -1
    for name in ${containers[@]}; do
        docker ps -a | grep "${name}"
    done
}

function stop() {
    for name in ${containers[@]}; do
        echo "Stopping container [${name}]..."
        docker stop "${name}" > /dev/null 2>&1
    done
}

function usage() {
    echo "Usage: $(basename $0) <command> [<args>]"
    echo -e
    echo "Available commands:"
    echo "  start          Start external dependencies for this project in Docker containers"
    echo "                 (incl. MySQL Server and RabbitMQ)"
    echo "  stop           Stop the Docker containers"
    echo -e
}

function requires() {
    local command=$1
    which ${command} > /dev/null 2>&1 || { echo "!! This script requires [${command}] to be installed" && exit 1; }
}

function waitForContainer() {
    local containerName="$1"
    local logMsg="$2"
    until docker logs ${containerName} 2>&1 | grep "${logMsg}" > /dev/null; do
        sleep 1s
    done
}


requires 'docker'

command=$1; shift
case "${command}" in
    start)
        start
        ;;
    stop)
        stop
        ;;
    status)
        status
        ;;
    *)
        usage
        exit 1
       ;;
esac

```


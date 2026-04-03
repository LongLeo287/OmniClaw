---
id: github.com-codelytv-java-ddd-example-f7ef82df-know
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:40.821059
---

# KNOWLEDGE EXTRACT: github.com_CodelyTV_java-ddd-example_f7ef82df
> **Extracted on:** 2026-04-01 14:57:23
> **Source:** D:/LongLeo/AI OS CORP/AI OS/core/security/QUARANTINE/KI-BATCH-20260331205007524177/github.com_CodelyTV_java-ddd-example_f7ef82df

---

## File: `.editorconfig`
```
root = true

[*]
charset = utf-8
end_of_line = lf
insert_final_newline = true
trim_trailing_whitespace = true

[*.java]
indent_size = 4
indent_style = tab
```

## File: `.env`
```
# See apps/main/resources/.env
```

## File: `.gitignore`
```
# Gradle
.gradle
build/

# Ignore Gradle GUI config
gradle-app.setting

/var/log/*
!/var/log/.gitkeep

.env.local
.env.*.local
```

## File: `Dockerfile`
```
FROM openjdk:21-slim-buster
WORKDIR /app

RUN apt update && apt install -y curl git

ENV NVM_DIR /usr/local/nvm
ENV NODE_VERSION 18.0.0

RUN mkdir -p $NVM_DIR
RUN curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.1/install.sh | bash

RUN . $NVM_DIR/nvm.sh && nvm install $NODE_VERSION && nvm alias default $NODE_VERSION && nvm use default

ENV NODE_PATH $NVM_DIR/versions/node/v$NODE_VERSION/lib/node_modules
ENV PATH      $NVM_DIR/versions/node/v$NODE_VERSION/bin:$PATH
```

## File: `HEAD`
```
ref: refs/heads/main
```

## File: `Makefile`
```
all: build

start:
	@docker compose -f docker-compose.ci.yml up -d

build:
	@./gradlew build --warning-mode all

lint:
	@docker exec codely-java_ddd_example-test_server ./gradlew spotlessCheck

run-tests:
	@./gradlew test --warning-mode all

test:
	@docker exec codely-java_ddd_example-test_server ./gradlew test --warning-mode all

run:
	@./gradlew :run

ping-mysql:
	@docker exec codely-java_ddd_example-mysql mysqladmin --user=root --password= --host "127.0.0.1" ping --silent

# Start the app
start-mooc_backend:
	@./gradlew bootRun --args='mooc_backend server'

start-backoffice_frontend:
	@./gradlew bootRun --args='backoffice_frontend server'
```

## File: `README.md`
```markdown
<p align="center">
  <a href="https://codely.com">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://codely.com/logo/codely_logo-dark.svg">
      <source media="(prefers-color-scheme: light)" srcset="https://codely.com/logo/codely_logo-light.svg">
      <img alt="Codely logo" src="https://codely.com/logo/codely_logo.svg">
    </picture>
  </a>
</p>

<h1 align="center">
  ☕🚀 Java DDD example: Save the boilerplate in your new projects
</h1>

<p align="center">
    <a href="https://github.com/CodelyTV"><img src="https://img.shields.io/badge/Codely-OS-green.svg?style=flat-square" alt="Codely Open Source projects"/></a>
    <a href="https://pro.codely.com"><img src="https://img.shields.io/badge/Codely-Pro-black.svg?style=flat-square" alt="Codely Pro courses"/></a>
    <a href="https://github.com/CodelyTV/java-ddd-example/actions"><img src="https://github.com/CodelyTV/java-ddd-example/workflows/CI/badge.svg" alt="CI pipeline status"></a>
</p>

> ⚡ Start your Java projects as fast as possible

## ℹ️ Introduction

This is a repository intended to serve as a starting point if you want to bootstrap a Java project with JUnit and Gradle.

Here you have the [course on CodelyTV Pro where we explain step by step all this](https://pro.codely.tv/library/ddd-en-java/about/?utm_source=github&utm_medium=social&utm_campaign=readme) (Spanish)

## 🏁 How To Start

1. Install Java 11: `brew cask install corretto`
2. Set it as your default JVM: `export JAVA_HOME='/Library/Java/JavaVirtualMachines/amazon-corretto-11.jdk/Contents/Home'`
3. Clone this repository: `git clone https://github.com/CodelyTV/java-ddd-example`.
4. Bring up the Docker environment: `make up`.
5. Execute some [Gradle lifecycle tasks](https://docs.gradle.org/current/userguide/java_plugin.html#lifecycle_tasks) in order to check everything is OK:
    1. Create [the project JAR](https://docs.gradle.org/current/userguide/java_plugin.html#sec:jar): `make build`
    2. Run the tests and plugins verification tasks: `make test`
6. Start developing!

## ☝️ How to update dependencies

* Gradle ([releases](https://gradle.org/releases/)): `./gradlew wrapper --gradle-version=WANTED_VERSION --distribution-type=bin`

## 💡 Related repositories

### ☕ Java

* 📂 [Java Basic example](https://github.com/CodelyTV/java-basic-example)
* ⚛ [Java OOP Examples](https://github.com/CodelyTV/java-oop-examples)
* 🧱 [Java SOLID Examples](https://github.com/CodelyTV/java-solid-examples)
* 🥦 [Java DDD Example](https://github.com/CodelyTV/java-ddd-example)

### 🐘 PHP

* 📂 [PHP Basic example](https://github.com/CodelyTV/php-basic-example)
* 🎩 [PHP DDD example](https://github.com/CodelyTV/php-ddd-example)
* 🥦 [PHP DDD Example](https://github.com/CodelyTV/php-ddd-example)

### 🧬 Scala

* 📂 [Scala Basic example](https://github.com/CodelyTV/scala-basic-example)
* ⚡ [Scala Basic example (g8 template)](https://github.com/CodelyTV/scala-basic-example.g8)
* ⚛ [Scala Examples](https://github.com/CodelyTV/scala-examples)
* 🥦 [Scala DDD Example](https://github.com/CodelyTV/scala-ddd-example)
```

## File: `build.gradle`
```
// Main project (located in apps/)
buildscript {
    repositories {
        mavenCentral()
    }
    dependencies {
        classpath('org.springframework.boot:spring-boot-gradle-plugin:3.1.5')
    }
}

plugins {
    id "com.diffplug.spotless" version "6.22.0"
}

spotless {
    java {
        prettier(['prettier': '2.8.8', 'prettier-plugin-java': '2.2.0'])
                .config(['parser': 'java', 'useTabs': true, 'printWidth': 120])

        importOrder('\\#', 'java', '', 'tv.codely')
        removeUnusedImports()

        endWithNewline()

        formatAnnotations()
    }
}

// Common for all projects
allprojects {
    apply plugin: 'java'
    apply plugin: 'io.spring.dependency-management'
    apply plugin: 'org.springframework.boot'

    java {
        sourceCompatibility = JavaVersion.VERSION_21
        targetCompatibility = JavaVersion.VERSION_21
    }


    repositories {
        mavenCentral()
        maven { url 'https://repo.spring.io/milestone' }
    }

    ext {
        set('springCloudVersion', "Hoxton.M3")
        set('elasticsearchVersion', '6.8.4')
    }

    dependencies {
        // Prod
        implementation 'org.apache.logging.log4j:log4j-core:2.21.1'
        implementation 'org.apache.logging.log4j:log4j-api:2.21.1'
        implementation 'com.vlkan.log4j2:log4j2-logstash-layout:1.0.5'
        implementation 'io.github.cdimascio:dotenv-java:3.0.0'
        implementation 'org.hibernate.orm:hibernate-core:6.3.1.Final'
        implementation 'jakarta.persistence:jakarta.persistence-api:3.2.0-B01'
        implementation 'org.springframework:spring-orm:6.0.13'
        implementation 'org.springframework:spring-context-support:6.0.13'
        implementation 'org.apache.tomcat:tomcat-dbcp:10.1.15'
        implementation 'com.sun.xml.bind:jaxb-impl:4.0.4'
        implementation 'jakarta.xml.bind:jakarta.xml.bind-api:4.0.1'
        implementation 'org.freemarker:freemarker-gae:2.3.32'
        implementation 'org.reflections:reflections:0.10.2'
        implementation 'com.google.guava:guava:31.0.1-jre'
        implementation 'org.springframework.boot:spring-boot-starter-amqp'
        implementation "org.elasticsearch.client:elasticsearch-rest-client:${elasticsearchVersion}"
        implementation "org.elasticsearch.client:elasticsearch-rest-high-level-client:${elasticsearchVersion}"
        implementation 'mysql:mysql-connector-java:8.0.28'

        // Test
        testImplementation 'org.junit.jupiter:junit-jupiter-api:5.5.2'
        testImplementation 'org.mockito:mockito-core:3.3.3'
        testImplementation 'com.github.javafaker:javafaker:1.0.1'
        testImplementation 'org.junit.jupiter:junit-jupiter-engine:5.5.2'
    }

    dependencyManagement {
        imports {
            mavenBom "org.springframework.cloud:spring-cloud-dependencies:${springCloudVersion}"
        }
    }

    test {
        useJUnitPlatform()

        testLogging {
            events "passed", "skipped", "failed"
        }
    }

    task view_paths {
        doLast { task ->
            println "$task.project.name"
            println "------------------"
            println "Main: $sourceSets.main.java.srcDirTrees"
            println "   Resources: $sourceSets.main.resources.srcDirTrees"
            println "Tests: $sourceSets.test.java.srcDirTrees"
            println "   Resources: $sourceSets.test.resources.srcDirTrees"
        }
    }
}

// All subprojects (located in src/*)
subprojects {
    group = "tv.codely.${rootProject.name}"

    sourceSets {
        main {
            java { srcDirs = ['main'] }
            resources { srcDirs = ['main/resources'] }
        }

        test {
            java { srcDirs = ['test'] }
            resources { srcDirs = ['test/resources'] }
        }
    }

    dependencies {
        implementation 'org.springframework.boot:spring-boot-starter-web:3.1.5'

        testImplementation rootProject.sourceSets.main.output
        testImplementation 'org.springframework.boot:spring-boot-starter-test:3.1.5'

        if (project.name != "shared") {
            implementation project(":shared")
            testImplementation project(":shared").sourceSets.test.output
        }
    }

    bootJar {
        enabled = false
    }

    jar {
        enabled = true
    }
}


sourceSets {
    main {
        java { srcDirs = ['apps/main'] }
        resources { srcDirs = ['apps/main/resources'] }
    }

    test {
        java { srcDirs = ['apps/test'] }
        resources { srcDirs = ['apps/test/resources'] }
    }
}

bootJar {
    archiveBaseName.set('java-ddd-example')
    archiveVersion.set('0.0.1')
    duplicatesStrategy = DuplicatesStrategy.EXCLUDE
}


dependencies {
    implementation 'org.springframework.boot:spring-boot-starter-web:3.1.5'

    implementation project(":shared")
    implementation project(":backoffice")
    implementation project(":mooc")

    testImplementation 'org.springframework.boot:spring-boot-starter-test:3.1.5'
    testImplementation project(":shared").sourceSets.test.output
}
```

## File: `config`
```
[core]
	repositoryformatversion = 0
	filemode = false
	bare = false
	logallrefupdates = true
	symlinks = false
	ignorecase = true
[remote "origin"]
	url = https://github.com/CodelyTV/java-ddd-example
	fetch = +refs/heads/main:refs/remotes/origin/main
[branch "main"]
	remote = origin
	merge = refs/heads/main
```

## File: `description`
```
Unnamed repository; edit this file 'description' to name the repository.
```

## File: `docker-compose.ci.yml`
```yaml
version: '3'

services:
  shared_mysql:
    container_name: codely-java_ddd_example-mysql
    image: mysql:8
    platform: linux/amd64
    ports:
      - "3306:3306"
    environment:
      - MYSQL_ROOT_PASSWORD=
      - MYSQL_ALLOW_EMPTY_PASSWORD=yes
    entrypoint:
      sh -c "
        echo 'CREATE DATABASE IF NOT EXISTS mooc;CREATE DATABASE IF NOT EXISTS backoffice;' > /docker-entrypoint-initdb.d/init.sql;
        /usr/local/bin/docker-entrypoint.sh --character-set-server=utf8mb4 --collation-server=utf8mb4_unicode_ci
      "
    command: ["--default-authentication-plugin=mysql_native_password"]

  shared_rabbitmq:
    container_name: codely-java_ddd_example-rabbitmq
    image: 'rabbitmq:3.7-management'
    platform: linux/amd64
    restart: unless-stopped
    ports:
      - "5630:5672"
      - "8090:15672"
    environment:
      - RABBITMQ_DEFAULT_USER=codely
      - RABBITMQ_DEFAULT_PASS=c0d3ly

  backoffice_elasticsearch:
    container_name: codely-java_ddd_example-elasticsearch
    image: 'elasticsearch:6.8.4'
    platform: linux/amd64
    restart: unless-stopped
    ports:
      - "9300:9300"
      - "9200:9200"
    environment:
      - discovery.type=single-node

  test_server_java:
    container_name: codely-java_ddd_example-test_server
    build:
      context: .
      dockerfile: Dockerfile
    restart: unless-stopped
    volumes:
      - .:/app:delegated
    depends_on:
      - shared_mysql
      - shared_rabbitmq
      - backoffice_elasticsearch
    tty: true
```

## File: `docker-compose.yml`
```yaml
version: '3'

services:
  shared_mysql:
    container_name: codely-java_ddd_example-mysql
    image: mysql:8
    platform: linux/amd64
    ports:
      - "3306:3306"
    environment:
      - MYSQL_ROOT_PASSWORD=
      - MYSQL_ALLOW_EMPTY_PASSWORD=yes
    entrypoint:
      sh -c "
        echo 'CREATE DATABASE IF NOT EXISTS mooc;CREATE DATABASE IF NOT EXISTS backoffice;' > /docker-entrypoint-initdb.d/init.sql;
        /usr/local/bin/docker-entrypoint.sh --character-set-server=utf8mb4 --collation-server=utf8mb4_unicode_ci
      "
    command: ["--default-authentication-plugin=mysql_native_password"]

  shared_rabbitmq:
    container_name: codely-java_ddd_example-rabbitmq
    image: 'rabbitmq:3.7-management'
    platform: linux/amd64
    restart: unless-stopped
    ports:
      - "5630:5672"
      - "8090:15672"
    environment:
      - RABBITMQ_DEFAULT_USER=codely
      - RABBITMQ_DEFAULT_PASS=c0d3ly

  backoffice_elasticsearch:
    container_name: codely-java_ddd_example-elasticsearch
    image: 'elasticsearch:6.8.4'
    platform: linux/amd64
    restart: unless-stopped
    ports:
      - "9300:9300"
      - "9200:9200"
    environment:
      - discovery.type=single-node

  backoffice_backend_server_java:
    container_name: codely-java_ddd_example-backoffice_backend_server
    build:
      context: .
      dockerfile: Dockerfile
    restart: unless-stopped
    ports:
      - "8040:8040"
    volumes:
      - .:/app:delegated
      - backoffice_backend_gradle_cache:/app/.gradle
    depends_on:
      - shared_mysql
      - shared_rabbitmq
      - backoffice_elasticsearch
    command: ["./gradlew", "bootRun", "--args", "backoffice_backend server"]

  backoffice_frontend_server_java:
    container_name: codely-java_ddd_example-backoffice_frontend_server
    build:
      context: .
      dockerfile: Dockerfile
    restart: unless-stopped
    ports:
      - "8041:8041"
    volumes:
      - .:/app:delegated
      - backoffice_frontend_gradle_cache:/app/.gradle
    depends_on:
      - shared_mysql
      - shared_rabbitmq
      - backoffice_elasticsearch
    command: ["./gradlew", "bootRun", "--args", "backoffice_frontend server"]

  mooc_backend_server_java:
    container_name: codely-java_ddd_example-mooc_backend_server
    build:
      context: .
      dockerfile: Dockerfile
    restart: unless-stopped
    ports:
      - "8030:8030"
    volumes:
      - .:/app:delegated
      - mooc_backend_gradle_cache:/app/.gradle
    depends_on:
      - shared_mysql
      - shared_rabbitmq
      - backoffice_elasticsearch
    command: ["./gradlew", "bootRun", "--args", "mooc_backend server"]

  test_server_java:
    container_name: codely-java_ddd_example-test_server
    build:
      context: .
      dockerfile: Dockerfile
    restart: unless-stopped
    volumes:
      - .:/app:delegated
      - test_gradle_cache:/app/.gradle
    depends_on:
      - shared_mysql
      - shared_rabbitmq
      - backoffice_elasticsearch
    tty: true

volumes:
  backoffice_backend_gradle_cache:
  backoffice_frontend_gradle_cache:
  mooc_backend_gradle_cache:
  test_gradle_cache:
```

## File: `gradlew`
```
#!/bin/sh

#
# Copyright © 2015-2021 the original authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

##############################################################################
#
#   Gradle start up script for POSIX generated by Gradle.
#
#   Important for running:
#
#   (1) You need a POSIX-compliant shell to run this script. If your /bin/sh is
#       noncompliant, but you have some other compliant shell such as ksh or
#       bash, then to run this script, type that shell name before the whole
#       command line, like:
#
#           ksh Gradle
#
#       Busybox and similar reduced shells will NOT work, because this script
#       requires all of these POSIX shell features:
#         * functions;
#         * expansions «$var», «${var}», «${var:-default}», «${var+SET}»,
#           «${var#prefix}», «${var%suffix}», and «$( cmd )»;
#         * compound commands having a testable exit status, especially «case»;
#         * various built-in commands including «command», «set», and «ulimit».
#
#   Important for patching:
#
#   (2) This script targets any POSIX shell, so it avoids extensions provided
#       by Bash, Ksh, etc; in particular arrays are avoided.
#
#       The "traditional" practice of packing multiple parameters into a
#       space-separated string is a well documented source of bugs and security
#       problems, so this is (mostly) avoided, by progressively accumulating
#       options in "$@", and eventually passing that to Java.
#
#       Where the inherited environment variables (DEFAULT_JVM_OPTS, JAVA_OPTS,
#       and GRADLE_OPTS) rely on word-splitting, this is performed explicitly;
#       see the in-line comments for details.
#
#       There are tweaks for specific operating systems such as AIX, CygWin,
#       Darwin, MinGW, and NonStop.
#
#   (3) This script is generated from the Groovy template
#       https://github.com/gradle/gradle/blob/HEAD/subprojects/plugins/src/main/resources/org/gradle/api/internal/plugins/unixStartScript.txt
#       within the Gradle project.
#
#       You can find Gradle at https://github.com/gradle/gradle/.
#
##############################################################################

# Attempt to set APP_HOME

# Resolve links: $0 may be a link
app_path=$0

# Need this for daisy-chained symlinks.
while
    APP_HOME=${app_path%"${app_path##*/}"}  # leaves a trailing /; empty if no leading path
    [ -h "$app_path" ]
do
    ls=$( ls -ld "$app_path" )
    link=${ls#*' -> '}
    case $link in             #(
      /*)   app_path=$link ;; #(
      *)    app_path=$APP_HOME$link ;;
    esac
done

# This is normally unused
# shellcheck disable=SC2034
APP_BASE_NAME=${0##*/}
# Discard cd standard output in case $CDPATH is set (https://github.com/gradle/gradle/issues/25036)
APP_HOME=$( cd "${APP_HOME:-./}" > /dev/null && pwd -P ) || exit

# Use the maximum available, or set MAX_FD != -1 to use that value.
MAX_FD=maximum

warn () {
    echo "$*"
} >&2

die () {
    echo
    echo "$*"
    echo
    exit 1
} >&2

# OS specific support (must be 'true' or 'false').
cygwin=false
msys=false
darwin=false
nonstop=false
case "$( uname )" in                #(
  CYGWIN* )         cygwin=true  ;; #(
  Darwin* )         darwin=true  ;; #(
  MSYS* | MINGW* )  msys=true    ;; #(
  NONSTOP* )        nonstop=true ;;
esac

CLASSPATH=$APP_HOME/gradle/wrapper/gradle-wrapper.jar


# Determine the Java command to use to start the JVM.
if [ -n "$JAVA_HOME" ] ; then
    if [ -x "$JAVA_HOME/jre/sh/java" ] ; then
        # IBM's JDK on AIX uses strange locations for the executables
        JAVACMD=$JAVA_HOME/jre/sh/java
    else
        JAVACMD=$JAVA_HOME/bin/java
    fi
    if [ ! -x "$JAVACMD" ] ; then
        die "ERROR: JAVA_HOME is set to an invalid directory: $JAVA_HOME

Please set the JAVA_HOME variable in your environment to match the
location of your Java installation."
    fi
else
    JAVACMD=java
    if ! command -v java >/dev/null 2>&1
    then
        die "ERROR: JAVA_HOME is not set and no 'java' command could be found in your PATH.

Please set the JAVA_HOME variable in your environment to match the
location of your Java installation."
    fi
fi

# Increase the maximum file descriptors if we can.
if ! "$cygwin" && ! "$darwin" && ! "$nonstop" ; then
    case $MAX_FD in #(
      max*)
        # In POSIX sh, ulimit -H is undefined. That's why the result is checked to see if it worked.
        # shellcheck disable=SC2039,SC3045
        MAX_FD=$( ulimit -H -n ) ||
            warn "Could not query maximum file descriptor limit"
    esac
    case $MAX_FD in  #(
      '' | soft) :;; #(
      *)
        # In POSIX sh, ulimit -n is undefined. That's why the result is checked to see if it worked.
        # shellcheck disable=SC2039,SC3045
        ulimit -n "$MAX_FD" ||
            warn "Could not set maximum file descriptor limit to $MAX_FD"
    esac
fi

# Collect all arguments for the java command, stacking in reverse order:
#   * args from the command line
#   * the main class name
#   * -classpath
#   * -D...appname settings
#   * --module-path (only if needed)
#   * DEFAULT_JVM_OPTS, JAVA_OPTS, and GRADLE_OPTS environment variables.

# For Cygwin or MSYS, switch paths to Windows format before running java
if "$cygwin" || "$msys" ; then
    APP_HOME=$( cygpath --path --mixed "$APP_HOME" )
    CLASSPATH=$( cygpath --path --mixed "$CLASSPATH" )

    JAVACMD=$( cygpath --unix "$JAVACMD" )

    # Now convert the arguments - kludge to limit ourselves to /bin/sh
    for arg do
        if
            case $arg in                                #(
              -*)   false ;;                            # don't mess with options #(
              /?*)  t=${arg#/} t=/${t%%/*}              # looks like a POSIX filepath
                    [ -e "$t" ] ;;                      #(
              *)    false ;;
            esac
        then
            arg=$( cygpath --path --ignore --mixed "$arg" )
        fi
        # Roll the args list around exactly as many times as the number of
        # args, so each arg winds up back in the position where it started, but
        # possibly modified.
        #
        # NB: a `for` loop captures its iteration list before it begins, so
        # changing the positional parameters here affects neither the number of
        # iterations, nor the values presented in `arg`.
        shift                   # remove old arg
        set -- "$@" "$arg"      # push replacement arg
    done
fi


# Add default JVM options here. You can also use JAVA_OPTS and GRADLE_OPTS to pass JVM options to this script.
DEFAULT_JVM_OPTS='"-Xmx64m" "-Xms64m"'

# Collect all arguments for the java command:
#   * DEFAULT_JVM_OPTS, JAVA_OPTS, JAVA_OPTS, and optsEnvironmentVar are not allowed to contain shell fragments,
#     and any embedded shellness will be escaped.
#   * For example: A user cannot expect ${Hostname} to be expanded, as it is an environment variable and will be
#     treated as '${Hostname}' itself on the command line.

set -- \
        "-Dorg.gradle.appname=$APP_BASE_NAME" \
        -classpath "$CLASSPATH" \
        org.gradle.wrapper.GradleWrapperMain \
        "$@"

# Stop when "xargs" is not available.
if ! command -v xargs >/dev/null 2>&1
then
    die "xargs is not available"
fi

# Use "xargs" to parse quoted args.
#
# With -n1 it outputs one arg per line, with the quotes and backslashes removed.
#
# In Bash we could simply go:
#
#   readarray ARGS < <( xargs -n1 <<<"$var" ) &&
#   set -- "${ARGS[@]}" "$@"
#
# but POSIX shell has neither arrays nor command substitution, so instead we
# post-process each arg (as a line of input to sed) to backslash-escape any
# character that might be a shell metacharacter, then use eval to reverse
# that process (while maintaining the separation between arguments), and wrap
# the whole thing up as a single "set" statement.
#
# This will of course break if any of these variables contains a newline or
# an unmatched quote.
#

eval "set -- $(
        printf '%s\n' "$DEFAULT_JVM_OPTS $JAVA_OPTS $GRADLE_OPTS" |
        xargs -n1 |
        sed ' s~[^-[:alnum:]+,./:=@_]~\\&~g; ' |
        tr '\n' ' '
    )" '"$@"'

exec "$JAVACMD" "$@"
```

## File: `gradlew.bat`
```
@rem
@rem Copyright 2015 the original author or authors.
@rem
@rem Licensed under the Apache License, Version 2.0 (the "License");
@rem you may not use this file except in compliance with the License.
@rem You may obtain a copy of the License at
@rem
@rem      https://www.apache.org/licenses/LICENSE-2.0
@rem
@rem Unless required by applicable law or agreed to in writing, software
@rem distributed under the License is distributed on an "AS IS" BASIS,
@rem WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
@rem See the License for the specific language governing permissions and
@rem limitations under the License.
@rem

@if "%DEBUG%"=="" @echo off
@rem ##########################################################################
@rem
@rem  Gradle startup script for Windows
@rem
@rem ##########################################################################

@rem Set local scope for the variables with windows NT shell
if "%OS%"=="Windows_NT" setlocal

set DIRNAME=%~dp0
if "%DIRNAME%"=="" set DIRNAME=.
@rem This is normally unused
set APP_BASE_NAME=%~n0
set APP_HOME=%DIRNAME%

@rem Resolve any "." and ".." in APP_HOME to make it shorter.
for %%i in ("%APP_HOME%") do set APP_HOME=%%~fi

@rem Add default JVM options here. You can also use JAVA_OPTS and GRADLE_OPTS to pass JVM options to this script.
set DEFAULT_JVM_OPTS="-Xmx64m" "-Xms64m"

@rem Find java.exe
if defined JAVA_HOME goto findJavaFromJavaHome

set JAVA_EXE=java.exe
%JAVA_EXE% -version >NUL 2>&1
if %ERRORLEVEL% equ 0 goto execute

echo.
echo ERROR: JAVA_HOME is not set and no 'java' command could be found in your PATH.
echo.
echo Please set the JAVA_HOME variable in your environment to match the
echo location of your Java installation.

goto fail

:findJavaFromJavaHome
set JAVA_HOME=%JAVA_HOME:"=%
set JAVA_EXE=%JAVA_HOME%/bin/java.exe

if exist "%JAVA_EXE%" goto execute

echo.
echo ERROR: JAVA_HOME is set to an invalid directory: %JAVA_HOME%
echo.
echo Please set the JAVA_HOME variable in your environment to match the
echo location of your Java installation.

goto fail

:execute
@rem Setup the command line

set CLASSPATH=%APP_HOME%\gradle\wrapper\gradle-wrapper.jar


@rem Execute Gradle
"%JAVA_EXE%" %DEFAULT_JVM_OPTS% %JAVA_OPTS% %GRADLE_OPTS% "-Dorg.gradle.appname=%APP_BASE_NAME%" -classpath "%CLASSPATH%" org.gradle.wrapper.GradleWrapperMain %*

:end
@rem End local scope for the variables with windows NT shell
if %ERRORLEVEL% equ 0 goto mainEnd

:fail
rem Set variable GRADLE_EXIT_CONSOLE if you need the _script_ return code instead of
rem the _cmd.exe /c_ return code!
set EXIT_CODE=%ERRORLEVEL%
if %EXIT_CODE% equ 0 set EXIT_CODE=1
if not ""=="%GRADLE_EXIT_CONSOLE%" exit %EXIT_CODE%
exit /b %EXIT_CODE%

:mainEnd
if "%OS%"=="Windows_NT" endlocal

:omega
```

## File: `packed-refs`
```
# pack-refs with: peeled fully-peeled sorted 
3a58e3294da6230472e2c6337417a9e6f796d46b refs/remotes/origin/main
```

## File: `settings.gradle`
```
rootProject.name = 'java-ddd-example'

include ':shared'
project(':shared').projectDir = new File('src/shared')

include ':analytics'
project(':analytics').projectDir = new File('src/analytics')

include ':backoffice'
project(':backoffice').projectDir = new File('src/backoffice')

include ':mooc'
project(':mooc').projectDir = new File('src/mooc')
```

## File: `shallow`
```
3a58e3294da6230472e2c6337417a9e6f796d46b
```

## File: `CodelyTV-java-ddd-example-3a58e32/.editorconfig`
```
root = true

[*]
charset = utf-8
end_of_line = lf
insert_final_newline = true
trim_trailing_whitespace = true

[*.java]
indent_size = 4
indent_style = tab
```

## File: `CodelyTV-java-ddd-example-3a58e32/.env`
```
# See apps/main/resources/.env
```

## File: `CodelyTV-java-ddd-example-3a58e32/.gitignore`
```
# Gradle
.gradle
build/

# Ignore Gradle GUI config
gradle-app.setting

/var/log/*
!/var/log/.gitkeep

.env.local
.env.*.local
```

## File: `CodelyTV-java-ddd-example-3a58e32/Dockerfile`
```
FROM openjdk:21-slim-buster
WORKDIR /app

RUN apt update && apt install -y curl git

ENV NVM_DIR /usr/local/nvm
ENV NODE_VERSION 18.0.0

RUN mkdir -p $NVM_DIR
RUN curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.1/install.sh | bash

RUN . $NVM_DIR/nvm.sh && nvm install $NODE_VERSION && nvm alias default $NODE_VERSION && nvm use default

ENV NODE_PATH $NVM_DIR/versions/node/v$NODE_VERSION/lib/node_modules
ENV PATH      $NVM_DIR/versions/node/v$NODE_VERSION/bin:$PATH
```

## File: `CodelyTV-java-ddd-example-3a58e32/Makefile`
```
all: build

start:
	@docker compose -f docker-compose.ci.yml up -d

build:
	@./gradlew build --warning-mode all

lint:
	@docker exec codely-java_ddd_example-test_server ./gradlew spotlessCheck

run-tests:
	@./gradlew test --warning-mode all

test:
	@docker exec codely-java_ddd_example-test_server ./gradlew test --warning-mode all

run:
	@./gradlew :run

ping-mysql:
	@docker exec codely-java_ddd_example-mysql mysqladmin --user=root --password= --host "127.0.0.1" ping --silent

# Start the app
start-mooc_backend:
	@./gradlew bootRun --args='mooc_backend server'

start-backoffice_frontend:
	@./gradlew bootRun --args='backoffice_frontend server'
```

## File: `CodelyTV-java-ddd-example-3a58e32/README.md`
```markdown
<p align="center">
  <a href="https://codely.com">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://codely.com/logo/codely_logo-dark.svg">
      <source media="(prefers-color-scheme: light)" srcset="https://codely.com/logo/codely_logo-light.svg">
      <img alt="Codely logo" src="https://codely.com/logo/codely_logo.svg">
    </picture>
  </a>
</p>

<h1 align="center">
  ☕🚀 Java DDD example: Save the boilerplate in your new projects
</h1>

<p align="center">
    <a href="https://github.com/CodelyTV"><img src="https://img.shields.io/badge/Codely-OS-green.svg?style=flat-square" alt="Codely Open Source projects"/></a>
    <a href="https://pro.codely.com"><img src="https://img.shields.io/badge/Codely-Pro-black.svg?style=flat-square" alt="Codely Pro courses"/></a>
    <a href="https://github.com/CodelyTV/java-ddd-example/actions"><img src="https://github.com/CodelyTV/java-ddd-example/workflows/CI/badge.svg" alt="CI pipeline status"></a>
</p>

> ⚡ Start your Java projects as fast as possible

## ℹ️ Introduction

This is a repository intended to serve as a starting point if you want to bootstrap a Java project with JUnit and Gradle.

Here you have the [course on CodelyTV Pro where we explain step by step all this](https://pro.codely.tv/library/ddd-en-java/about/?utm_source=github&utm_medium=social&utm_campaign=readme) (Spanish)

## 🏁 How To Start

1. Install Java 11: `brew cask install corretto`
2. Set it as your default JVM: `export JAVA_HOME='/Library/Java/JavaVirtualMachines/amazon-corretto-11.jdk/Contents/Home'`
3. Clone this repository: `git clone https://github.com/CodelyTV/java-ddd-example`.
4. Bring up the Docker environment: `make up`.
5. Execute some [Gradle lifecycle tasks](https://docs.gradle.org/current/userguide/java_plugin.html#lifecycle_tasks) in order to check everything is OK:
    1. Create [the project JAR](https://docs.gradle.org/current/userguide/java_plugin.html#sec:jar): `make build`
    2. Run the tests and plugins verification tasks: `make test`
6. Start developing!

## ☝️ How to update dependencies

* Gradle ([releases](https://gradle.org/releases/)): `./gradlew wrapper --gradle-version=WANTED_VERSION --distribution-type=bin`

## 💡 Related repositories

### ☕ Java

* 📂 [Java Basic example](https://github.com/CodelyTV/java-basic-example)
* ⚛ [Java OOP Examples](https://github.com/CodelyTV/java-oop-examples)
* 🧱 [Java SOLID Examples](https://github.com/CodelyTV/java-solid-examples)
* 🥦 [Java DDD Example](https://github.com/CodelyTV/java-ddd-example)

### 🐘 PHP

* 📂 [PHP Basic example](https://github.com/CodelyTV/php-basic-example)
* 🎩 [PHP DDD example](https://github.com/CodelyTV/php-ddd-example)
* 🥦 [PHP DDD Example](https://github.com/CodelyTV/php-ddd-example)

### 🧬 Scala

* 📂 [Scala Basic example](https://github.com/CodelyTV/scala-basic-example)
* ⚡ [Scala Basic example (g8 template)](https://github.com/CodelyTV/scala-basic-example.g8)
* ⚛ [Scala Examples](https://github.com/CodelyTV/scala-examples)
* 🥦 [Scala DDD Example](https://github.com/CodelyTV/scala-ddd-example)
```

## File: `CodelyTV-java-ddd-example-3a58e32/build.gradle`
```
// Main project (located in apps/)
buildscript {
    repositories {
        mavenCentral()
    }
    dependencies {
        classpath('org.springframework.boot:spring-boot-gradle-plugin:3.1.5')
    }
}

plugins {
    id "com.diffplug.spotless" version "6.22.0"
}

spotless {
    java {
        prettier(['prettier': '2.8.8', 'prettier-plugin-java': '2.2.0'])
                .config(['parser': 'java', 'useTabs': true, 'printWidth': 120])

        importOrder('\\#', 'java', '', 'tv.codely')
        removeUnusedImports()

        endWithNewline()

        formatAnnotations()
    }
}

// Common for all projects
allprojects {
    apply plugin: 'java'
    apply plugin: 'io.spring.dependency-management'
    apply plugin: 'org.springframework.boot'

    java {
        sourceCompatibility = JavaVersion.VERSION_21
        targetCompatibility = JavaVersion.VERSION_21
    }


    repositories {
        mavenCentral()
        maven { url 'https://repo.spring.io/milestone' }
    }

    ext {
        set('springCloudVersion', "Hoxton.M3")
        set('elasticsearchVersion', '6.8.4')
    }

    dependencies {
        // Prod
        implementation 'org.apache.logging.log4j:log4j-core:2.21.1'
        implementation 'org.apache.logging.log4j:log4j-api:2.21.1'
        implementation 'com.vlkan.log4j2:log4j2-logstash-layout:1.0.5'
        implementation 'io.github.cdimascio:dotenv-java:3.0.0'
        implementation 'org.hibernate.orm:hibernate-core:6.3.1.Final'
        implementation 'jakarta.persistence:jakarta.persistence-api:3.2.0-B01'
        implementation 'org.springframework:spring-orm:6.0.13'
        implementation 'org.springframework:spring-context-support:6.0.13'
        implementation 'org.apache.tomcat:tomcat-dbcp:10.1.15'
        implementation 'com.sun.xml.bind:jaxb-impl:4.0.4'
        implementation 'jakarta.xml.bind:jakarta.xml.bind-api:4.0.1'
        implementation 'org.freemarker:freemarker-gae:2.3.32'
        implementation 'org.reflections:reflections:0.10.2'
        implementation 'com.google.guava:guava:31.0.1-jre'
        implementation 'org.springframework.boot:spring-boot-starter-amqp'
        implementation "org.elasticsearch.client:elasticsearch-rest-client:${elasticsearchVersion}"
        implementation "org.elasticsearch.client:elasticsearch-rest-high-level-client:${elasticsearchVersion}"
        implementation 'mysql:mysql-connector-java:8.0.28'

        // Test
        testImplementation 'org.junit.jupiter:junit-jupiter-api:5.5.2'
        testImplementation 'org.mockito:mockito-core:3.3.3'
        testImplementation 'com.github.javafaker:javafaker:1.0.1'
        testImplementation 'org.junit.jupiter:junit-jupiter-engine:5.5.2'
    }

    dependencyManagement {
        imports {
            mavenBom "org.springframework.cloud:spring-cloud-dependencies:${springCloudVersion}"
        }
    }

    test {
        useJUnitPlatform()

        testLogging {
            events "passed", "skipped", "failed"
        }
    }

    task view_paths {
        doLast { task ->
            println "$task.project.name"
            println "------------------"
            println "Main: $sourceSets.main.java.srcDirTrees"
            println "   Resources: $sourceSets.main.resources.srcDirTrees"
            println "Tests: $sourceSets.test.java.srcDirTrees"
            println "   Resources: $sourceSets.test.resources.srcDirTrees"
        }
    }
}

// All subprojects (located in src/*)
subprojects {
    group = "tv.codely.${rootProject.name}"

    sourceSets {
        main {
            java { srcDirs = ['main'] }
            resources { srcDirs = ['main/resources'] }
        }

        test {
            java { srcDirs = ['test'] }
            resources { srcDirs = ['test/resources'] }
        }
    }

    dependencies {
        implementation 'org.springframework.boot:spring-boot-starter-web:3.1.5'

        testImplementation rootProject.sourceSets.main.output
        testImplementation 'org.springframework.boot:spring-boot-starter-test:3.1.5'

        if (project.name != "shared") {
            implementation project(":shared")
            testImplementation project(":shared").sourceSets.test.output
        }
    }

    bootJar {
        enabled = false
    }

    jar {
        enabled = true
    }
}


sourceSets {
    main {
        java { srcDirs = ['apps/main'] }
        resources { srcDirs = ['apps/main/resources'] }
    }

    test {
        java { srcDirs = ['apps/test'] }
        resources { srcDirs = ['apps/test/resources'] }
    }
}

bootJar {
    archiveBaseName.set('java-ddd-example')
    archiveVersion.set('0.0.1')
    duplicatesStrategy = DuplicatesStrategy.EXCLUDE
}


dependencies {
    implementation 'org.springframework.boot:spring-boot-starter-web:3.1.5'

    implementation project(":shared")
    implementation project(":backoffice")
    implementation project(":mooc")

    testImplementation 'org.springframework.boot:spring-boot-starter-test:3.1.5'
    testImplementation project(":shared").sourceSets.test.output
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/docker-compose.ci.yml`
```yaml
version: '3'

services:
  shared_mysql:
    container_name: codely-java_ddd_example-mysql
    image: mysql:8
    platform: linux/amd64
    ports:
      - "3306:3306"
    environment:
      - MYSQL_ROOT_PASSWORD=
      - MYSQL_ALLOW_EMPTY_PASSWORD=yes
    entrypoint:
      sh -c "
        echo 'CREATE DATABASE IF NOT EXISTS mooc;CREATE DATABASE IF NOT EXISTS backoffice;' > /docker-entrypoint-initdb.d/init.sql;
        /usr/local/bin/docker-entrypoint.sh --character-set-server=utf8mb4 --collation-server=utf8mb4_unicode_ci
      "
    command: ["--default-authentication-plugin=mysql_native_password"]

  shared_rabbitmq:
    container_name: codely-java_ddd_example-rabbitmq
    image: 'rabbitmq:3.7-management'
    platform: linux/amd64
    restart: unless-stopped
    ports:
      - "5630:5672"
      - "8090:15672"
    environment:
      - RABBITMQ_DEFAULT_USER=codely
      - RABBITMQ_DEFAULT_PASS=c0d3ly

  backoffice_elasticsearch:
    container_name: codely-java_ddd_example-elasticsearch
    image: 'elasticsearch:6.8.4'
    platform: linux/amd64
    restart: unless-stopped
    ports:
      - "9300:9300"
      - "9200:9200"
    environment:
      - discovery.type=single-node

  test_server_java:
    container_name: codely-java_ddd_example-test_server
    build:
      context: .
      dockerfile: Dockerfile
    restart: unless-stopped
    volumes:
      - .:/app:delegated
    depends_on:
      - shared_mysql
      - shared_rabbitmq
      - backoffice_elasticsearch
    tty: true
```

## File: `CodelyTV-java-ddd-example-3a58e32/docker-compose.yml`
```yaml
version: '3'

services:
  shared_mysql:
    container_name: codely-java_ddd_example-mysql
    image: mysql:8
    platform: linux/amd64
    ports:
      - "3306:3306"
    environment:
      - MYSQL_ROOT_PASSWORD=
      - MYSQL_ALLOW_EMPTY_PASSWORD=yes
    entrypoint:
      sh -c "
        echo 'CREATE DATABASE IF NOT EXISTS mooc;CREATE DATABASE IF NOT EXISTS backoffice;' > /docker-entrypoint-initdb.d/init.sql;
        /usr/local/bin/docker-entrypoint.sh --character-set-server=utf8mb4 --collation-server=utf8mb4_unicode_ci
      "
    command: ["--default-authentication-plugin=mysql_native_password"]

  shared_rabbitmq:
    container_name: codely-java_ddd_example-rabbitmq
    image: 'rabbitmq:3.7-management'
    platform: linux/amd64
    restart: unless-stopped
    ports:
      - "5630:5672"
      - "8090:15672"
    environment:
      - RABBITMQ_DEFAULT_USER=codely
      - RABBITMQ_DEFAULT_PASS=c0d3ly

  backoffice_elasticsearch:
    container_name: codely-java_ddd_example-elasticsearch
    image: 'elasticsearch:6.8.4'
    platform: linux/amd64
    restart: unless-stopped
    ports:
      - "9300:9300"
      - "9200:9200"
    environment:
      - discovery.type=single-node

  backoffice_backend_server_java:
    container_name: codely-java_ddd_example-backoffice_backend_server
    build:
      context: .
      dockerfile: Dockerfile
    restart: unless-stopped
    ports:
      - "8040:8040"
    volumes:
      - .:/app:delegated
      - backoffice_backend_gradle_cache:/app/.gradle
    depends_on:
      - shared_mysql
      - shared_rabbitmq
      - backoffice_elasticsearch
    command: ["./gradlew", "bootRun", "--args", "backoffice_backend server"]

  backoffice_frontend_server_java:
    container_name: codely-java_ddd_example-backoffice_frontend_server
    build:
      context: .
      dockerfile: Dockerfile
    restart: unless-stopped
    ports:
      - "8041:8041"
    volumes:
      - .:/app:delegated
      - backoffice_frontend_gradle_cache:/app/.gradle
    depends_on:
      - shared_mysql
      - shared_rabbitmq
      - backoffice_elasticsearch
    command: ["./gradlew", "bootRun", "--args", "backoffice_frontend server"]

  mooc_backend_server_java:
    container_name: codely-java_ddd_example-mooc_backend_server
    build:
      context: .
      dockerfile: Dockerfile
    restart: unless-stopped
    ports:
      - "8030:8030"
    volumes:
      - .:/app:delegated
      - mooc_backend_gradle_cache:/app/.gradle
    depends_on:
      - shared_mysql
      - shared_rabbitmq
      - backoffice_elasticsearch
    command: ["./gradlew", "bootRun", "--args", "mooc_backend server"]

  test_server_java:
    container_name: codely-java_ddd_example-test_server
    build:
      context: .
      dockerfile: Dockerfile
    restart: unless-stopped
    volumes:
      - .:/app:delegated
      - test_gradle_cache:/app/.gradle
    depends_on:
      - shared_mysql
      - shared_rabbitmq
      - backoffice_elasticsearch
    tty: true

volumes:
  backoffice_backend_gradle_cache:
  backoffice_frontend_gradle_cache:
  mooc_backend_gradle_cache:
  test_gradle_cache:
```

## File: `CodelyTV-java-ddd-example-3a58e32/gradlew`
```
#!/bin/sh

#
# Copyright © 2015-2021 the original authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

##############################################################################
#
#   Gradle start up script for POSIX generated by Gradle.
#
#   Important for running:
#
#   (1) You need a POSIX-compliant shell to run this script. If your /bin/sh is
#       noncompliant, but you have some other compliant shell such as ksh or
#       bash, then to run this script, type that shell name before the whole
#       command line, like:
#
#           ksh Gradle
#
#       Busybox and similar reduced shells will NOT work, because this script
#       requires all of these POSIX shell features:
#         * functions;
#         * expansions «$var», «${var}», «${var:-default}», «${var+SET}»,
#           «${var#prefix}», «${var%suffix}», and «$( cmd )»;
#         * compound commands having a testable exit status, especially «case»;
#         * various built-in commands including «command», «set», and «ulimit».
#
#   Important for patching:
#
#   (2) This script targets any POSIX shell, so it avoids extensions provided
#       by Bash, Ksh, etc; in particular arrays are avoided.
#
#       The "traditional" practice of packing multiple parameters into a
#       space-separated string is a well documented source of bugs and security
#       problems, so this is (mostly) avoided, by progressively accumulating
#       options in "$@", and eventually passing that to Java.
#
#       Where the inherited environment variables (DEFAULT_JVM_OPTS, JAVA_OPTS,
#       and GRADLE_OPTS) rely on word-splitting, this is performed explicitly;
#       see the in-line comments for details.
#
#       There are tweaks for specific operating systems such as AIX, CygWin,
#       Darwin, MinGW, and NonStop.
#
#   (3) This script is generated from the Groovy template
#       https://github.com/gradle/gradle/blob/HEAD/subprojects/plugins/src/main/resources/org/gradle/api/internal/plugins/unixStartScript.txt
#       within the Gradle project.
#
#       You can find Gradle at https://github.com/gradle/gradle/.
#
##############################################################################

# Attempt to set APP_HOME

# Resolve links: $0 may be a link
app_path=$0

# Need this for daisy-chained symlinks.
while
    APP_HOME=${app_path%"${app_path##*/}"}  # leaves a trailing /; empty if no leading path
    [ -h "$app_path" ]
do
    ls=$( ls -ld "$app_path" )
    link=${ls#*' -> '}
    case $link in             #(
      /*)   app_path=$link ;; #(
      *)    app_path=$APP_HOME$link ;;
    esac
done

# This is normally unused
# shellcheck disable=SC2034
APP_BASE_NAME=${0##*/}
# Discard cd standard output in case $CDPATH is set (https://github.com/gradle/gradle/issues/25036)
APP_HOME=$( cd "${APP_HOME:-./}" > /dev/null && pwd -P ) || exit

# Use the maximum available, or set MAX_FD != -1 to use that value.
MAX_FD=maximum

warn () {
    echo "$*"
} >&2

die () {
    echo
    echo "$*"
    echo
    exit 1
} >&2

# OS specific support (must be 'true' or 'false').
cygwin=false
msys=false
darwin=false
nonstop=false
case "$( uname )" in                #(
  CYGWIN* )         cygwin=true  ;; #(
  Darwin* )         darwin=true  ;; #(
  MSYS* | MINGW* )  msys=true    ;; #(
  NONSTOP* )        nonstop=true ;;
esac

CLASSPATH=$APP_HOME/gradle/wrapper/gradle-wrapper.jar


# Determine the Java command to use to start the JVM.
if [ -n "$JAVA_HOME" ] ; then
    if [ -x "$JAVA_HOME/jre/sh/java" ] ; then
        # IBM's JDK on AIX uses strange locations for the executables
        JAVACMD=$JAVA_HOME/jre/sh/java
    else
        JAVACMD=$JAVA_HOME/bin/java
    fi
    if [ ! -x "$JAVACMD" ] ; then
        die "ERROR: JAVA_HOME is set to an invalid directory: $JAVA_HOME

Please set the JAVA_HOME variable in your environment to match the
location of your Java installation."
    fi
else
    JAVACMD=java
    if ! command -v java >/dev/null 2>&1
    then
        die "ERROR: JAVA_HOME is not set and no 'java' command could be found in your PATH.

Please set the JAVA_HOME variable in your environment to match the
location of your Java installation."
    fi
fi

# Increase the maximum file descriptors if we can.
if ! "$cygwin" && ! "$darwin" && ! "$nonstop" ; then
    case $MAX_FD in #(
      max*)
        # In POSIX sh, ulimit -H is undefined. That's why the result is checked to see if it worked.
        # shellcheck disable=SC2039,SC3045
        MAX_FD=$( ulimit -H -n ) ||
            warn "Could not query maximum file descriptor limit"
    esac
    case $MAX_FD in  #(
      '' | soft) :;; #(
      *)
        # In POSIX sh, ulimit -n is undefined. That's why the result is checked to see if it worked.
        # shellcheck disable=SC2039,SC3045
        ulimit -n "$MAX_FD" ||
            warn "Could not set maximum file descriptor limit to $MAX_FD"
    esac
fi

# Collect all arguments for the java command, stacking in reverse order:
#   * args from the command line
#   * the main class name
#   * -classpath
#   * -D...appname settings
#   * --module-path (only if needed)
#   * DEFAULT_JVM_OPTS, JAVA_OPTS, and GRADLE_OPTS environment variables.

# For Cygwin or MSYS, switch paths to Windows format before running java
if "$cygwin" || "$msys" ; then
    APP_HOME=$( cygpath --path --mixed "$APP_HOME" )
    CLASSPATH=$( cygpath --path --mixed "$CLASSPATH" )

    JAVACMD=$( cygpath --unix "$JAVACMD" )

    # Now convert the arguments - kludge to limit ourselves to /bin/sh
    for arg do
        if
            case $arg in                                #(
              -*)   false ;;                            # don't mess with options #(
              /?*)  t=${arg#/} t=/${t%%/*}              # looks like a POSIX filepath
                    [ -e "$t" ] ;;                      #(
              *)    false ;;
            esac
        then
            arg=$( cygpath --path --ignore --mixed "$arg" )
        fi
        # Roll the args list around exactly as many times as the number of
        # args, so each arg winds up back in the position where it started, but
        # possibly modified.
        #
        # NB: a `for` loop captures its iteration list before it begins, so
        # changing the positional parameters here affects neither the number of
        # iterations, nor the values presented in `arg`.
        shift                   # remove old arg
        set -- "$@" "$arg"      # push replacement arg
    done
fi


# Add default JVM options here. You can also use JAVA_OPTS and GRADLE_OPTS to pass JVM options to this script.
DEFAULT_JVM_OPTS='"-Xmx64m" "-Xms64m"'

# Collect all arguments for the java command:
#   * DEFAULT_JVM_OPTS, JAVA_OPTS, JAVA_OPTS, and optsEnvironmentVar are not allowed to contain shell fragments,
#     and any embedded shellness will be escaped.
#   * For example: A user cannot expect ${Hostname} to be expanded, as it is an environment variable and will be
#     treated as '${Hostname}' itself on the command line.

set -- \
        "-Dorg.gradle.appname=$APP_BASE_NAME" \
        -classpath "$CLASSPATH" \
        org.gradle.wrapper.GradleWrapperMain \
        "$@"

# Stop when "xargs" is not available.
if ! command -v xargs >/dev/null 2>&1
then
    die "xargs is not available"
fi

# Use "xargs" to parse quoted args.
#
# With -n1 it outputs one arg per line, with the quotes and backslashes removed.
#
# In Bash we could simply go:
#
#   readarray ARGS < <( xargs -n1 <<<"$var" ) &&
#   set -- "${ARGS[@]}" "$@"
#
# but POSIX shell has neither arrays nor command substitution, so instead we
# post-process each arg (as a line of input to sed) to backslash-escape any
# character that might be a shell metacharacter, then use eval to reverse
# that process (while maintaining the separation between arguments), and wrap
# the whole thing up as a single "set" statement.
#
# This will of course break if any of these variables contains a newline or
# an unmatched quote.
#

eval "set -- $(
        printf '%s\n' "$DEFAULT_JVM_OPTS $JAVA_OPTS $GRADLE_OPTS" |
        xargs -n1 |
        sed ' s~[^-[:alnum:]+,./:=@_]~\\&~g; ' |
        tr '\n' ' '
    )" '"$@"'

exec "$JAVACMD" "$@"
```

## File: `CodelyTV-java-ddd-example-3a58e32/gradlew.bat`
```
@rem
@rem Copyright 2015 the original author or authors.
@rem
@rem Licensed under the Apache License, Version 2.0 (the "License");
@rem you may not use this file except in compliance with the License.
@rem You may obtain a copy of the License at
@rem
@rem      https://www.apache.org/licenses/LICENSE-2.0
@rem
@rem Unless required by applicable law or agreed to in writing, software
@rem distributed under the License is distributed on an "AS IS" BASIS,
@rem WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
@rem See the License for the specific language governing permissions and
@rem limitations under the License.
@rem

@if "%DEBUG%"=="" @echo off
@rem ##########################################################################
@rem
@rem  Gradle startup script for Windows
@rem
@rem ##########################################################################

@rem Set local scope for the variables with windows NT shell
if "%OS%"=="Windows_NT" setlocal

set DIRNAME=%~dp0
if "%DIRNAME%"=="" set DIRNAME=.
@rem This is normally unused
set APP_BASE_NAME=%~n0
set APP_HOME=%DIRNAME%

@rem Resolve any "." and ".." in APP_HOME to make it shorter.
for %%i in ("%APP_HOME%") do set APP_HOME=%%~fi

@rem Add default JVM options here. You can also use JAVA_OPTS and GRADLE_OPTS to pass JVM options to this script.
set DEFAULT_JVM_OPTS="-Xmx64m" "-Xms64m"

@rem Find java.exe
if defined JAVA_HOME goto findJavaFromJavaHome

set JAVA_EXE=java.exe
%JAVA_EXE% -version >NUL 2>&1
if %ERRORLEVEL% equ 0 goto execute

echo.
echo ERROR: JAVA_HOME is not set and no 'java' command could be found in your PATH.
echo.
echo Please set the JAVA_HOME variable in your environment to match the
echo location of your Java installation.

goto fail

:findJavaFromJavaHome
set JAVA_HOME=%JAVA_HOME:"=%
set JAVA_EXE=%JAVA_HOME%/bin/java.exe

if exist "%JAVA_EXE%" goto execute

echo.
echo ERROR: JAVA_HOME is set to an invalid directory: %JAVA_HOME%
echo.
echo Please set the JAVA_HOME variable in your environment to match the
echo location of your Java installation.

goto fail

:execute
@rem Setup the command line

set CLASSPATH=%APP_HOME%\gradle\wrapper\gradle-wrapper.jar


@rem Execute Gradle
"%JAVA_EXE%" %DEFAULT_JVM_OPTS% %JAVA_OPTS% %GRADLE_OPTS% "-Dorg.gradle.appname=%APP_BASE_NAME%" -classpath "%CLASSPATH%" org.gradle.wrapper.GradleWrapperMain %*

:end
@rem End local scope for the variables with windows NT shell
if %ERRORLEVEL% equ 0 goto mainEnd

:fail
rem Set variable GRADLE_EXIT_CONSOLE if you need the _script_ return code instead of
rem the _cmd.exe /c_ return code!
set EXIT_CODE=%ERRORLEVEL%
if %EXIT_CODE% equ 0 set EXIT_CODE=1
if not ""=="%GRADLE_EXIT_CONSOLE%" exit %EXIT_CODE%
exit /b %EXIT_CODE%

:mainEnd
if "%OS%"=="Windows_NT" endlocal

:omega
```

## File: `CodelyTV-java-ddd-example-3a58e32/settings.gradle`
```
rootProject.name = 'java-ddd-example'

include ':shared'
project(':shared').projectDir = new File('src/shared')

include ':analytics'
project(':analytics').projectDir = new File('src/analytics')

include ':backoffice'
project(':backoffice').projectDir = new File('src/backoffice')

include ':mooc'
project(':mooc').projectDir = new File('src/mooc')
```

## File: `CodelyTV-java-ddd-example-3a58e32/apps/main/resources/.env`
```
#              MOOC              #
#--------------------------------#
MOOC_BACKEND_SERVER_PORT=8030
# MySql
MOOC_DATABASE_HOST=codely-java_ddd_example-mysql
MOOC_DATABASE_PORT=3306
MOOC_DATABASE_NAME=mooc
MOOC_DATABASE_USER=root
MOOC_DATABASE_PASSWORD=

#           BACKOFFICE           #
#--------------------------------#
BACKOFFICE_BACKEND_SERVER_PORT=8040
BACKOFFICE_FRONTEND_SERVER_PORT=8041
# MySql
BACKOFFICE_DATABASE_HOST=codely-java_ddd_example-mysql
BACKOFFICE_DATABASE_PORT=3306
BACKOFFICE_DATABASE_NAME=backoffice
BACKOFFICE_DATABASE_USER=root
BACKOFFICE_DATABASE_PASSWORD=
# Elasticsearch
BACKOFFICE_ELASTICSEARCH_HOST=codely-java_ddd_example-elasticsearch
BACKOFFICE_ELASTICSEARCH_PORT=9200
BACKOFFICE_ELASTICSEARCH_INDEX_PREFIX=backoffice

#             COMMON             #
#--------------------------------#
# RabbitMQ
RABBITMQ_HOST=codely-java_ddd_example-rabbitmq
RABBITMQ_PORT=5672
RABBITMQ_LOGIN=codely
RABBITMQ_PASSWORD=c0d3ly
RABBITMQ_EXCHANGE=domain_events
RABBITMQ_MAX_RETRIES=5
```

## File: `CodelyTV-java-ddd-example-3a58e32/apps/main/resources/log4j2.properties`
```
name                                            = CodelyTvJavaDddExample
property.filename                               = logs
appenders                                       = console, file

status                                          = warn

appender.console.name                           = CONSOLE
appender.console.type                           = CONSOLE
appender.console.target                         = SYSTEM_OUT

appender.console.logstash.type                  = LogstashLayout
appender.console.logstash.dateTimeFormatPattern = yyyy-MM-dd'T'HH:mm:ss.SSSZZZ
appender.console.logstash.eventTemplateUri      = classpath:LogstashJsonEventLayoutV1.json
appender.console.logstash.prettyPrintEnabled    = true
appender.console.logstash.stackTraceEnabled     = true

appender.file.type                              = File
appender.file.name                              = LOGFILE
appender.file.fileName                          = var/log/java-ddd-example.log
appender.file.logstash.type                     = LogstashLayout
appender.file.logstash.dateTimeFormatPattern    = yyyy-MM-dd'T'HH:mm:ss.SSSZZZ
appender.file.logstash.eventTemplateUri         = classpath:LogstashJsonEventLayoutV1.json
appender.file.logstash.prettyPrintEnabled       = false
appender.file.logstash.stackTraceEnabled        = true

loggers                                         = file
logger.file.name                                = tv.codely.java_ddd_example
logger.file.level                               = info
logger.file.appenderRefs                        = file
logger.file.appenderRef.file.ref                = LOGFILE

rootLogger.level                                = info
rootLogger.appenderRefs                         = stdout
rootLogger.appenderRef.stdout.ref               = CONSOLE
```

## File: `CodelyTV-java-ddd-example-3a58e32/apps/main/resources/backoffice_frontend/templates/master.ftl`
```
<#import "spring.ftl" as spring />

<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link href="https://unpkg.com/tailwindcss@^1.0/dist/tailwind.min.css" rel="stylesheet">

    <title>${title}</title>
    <title>${description}</title>
</head>
<body>
<#include "partials/header.ftl">

<div class="container mx-auto px-4 p-5">
    <h1 class="font-sans text-gray-800 text-center text-5xl mb-10"><@page_title/></h1>
    <@main/>
</div>

<div class="clearfix"></div>

<#include "partials/footer.ftl">
</body>
</html>
```

## File: `CodelyTV-java-ddd-example-3a58e32/apps/main/resources/backoffice_frontend/templates/pages/home.ftl`
```
<#include "../master.ftl">

<#macro page_title>HOME</#macro>

<#macro main>
    Estamos en la home!
</#macro>
```

## File: `CodelyTV-java-ddd-example-3a58e32/apps/main/resources/backoffice_frontend/templates/pages/courses/courses.ftl`
```
<#include "../../master.ftl">

<#macro page_title>Cursos</#macro>

<#macro main>
    <div class="max-w-sm rounded overflow-hidden shadow-lg float-left">
        <img class="w-full" src="https://codely.tv/pro/img/bg/cursos-codelytv-pro.png" alt="Sunset in the mountains">
        <div class="px-6 py-4">
            <div class="font-bold text-xl mb-2">Cursos</div>
            <p class="text-gray-700 text-base">
                Actualmente CodelyTV Pro cuenta con <b>${courses_counter}</b> cursos.
            </p>
        </div>
    </div>

    <#include "partials/new_course_form.ftl">
    <div class="clearfix mb-10"></div>
    <hr class="mb-10">
    <#include "partials/list_courses.ftl">
</#macro>
```

## File: `CodelyTV-java-ddd-example-3a58e32/apps/main/resources/backoffice_frontend/templates/pages/courses/partials/list_courses.ftl`
```
<h3 class="font-sans text-gray-800 text-center text-3xl mb-10">Cursos existentes</h3>


<form action="" method="get" id="courses-filters" name="filter-courses">
    <div id="filter-rows">

    </div>
    <div class="clearfix"></div>
    <div class="mt-10 inline-block relative w-2/4">
        <button class="md:w-1/4 bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
                id="add-field-button"
                onclick="addFilter(event)">
            Añadir filtro
        </button>

        <button class="md:w-1/4 bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
                id="filter-button"
                onclick="filterCourses(event)">
            👉 Filtrar 👈
        </button>
    </div>
</form>
<table class="text-left w-full border-collapse">
    <thead>
    <tr>
        <th class="py-4 px-6 bg-grey-lightest font-bold uppercase text-sm text-grey-dark border-b border-grey-light">
            Id
        </th>
        <th class="py-4 px-6 bg-grey-lightest font-bold uppercase text-sm text-grey-dark border-b border-grey-light">
            Nombre
        </th>
        <th class="py-4 px-6 bg-grey-lightest font-bold uppercase text-sm text-grey-dark border-b border-grey-light">
            Duración
        </th>
    </tr>
    </thead>
    <tbody id="courses-list">

    </tbody>
</table>

<script>


    function addCoursesList(url) {
        console.log(url);

        const tableBody = document.getElementById("courses-list");

        fetch(encodeURI(url))
            .then(function (response) {
                return response.json();
            })
            .then(function (courses) {
                tableBody.innerHTML = "";

                courses.forEach(function (course) {
                    let courseRow = document.createElement("tr");

                    courseRow.appendChild(tableCellFor(course.id));
                    courseRow.appendChild(tableCellFor(course.name));
                    courseRow.appendChild(tableCellFor(course.duration));

                    tableBody.appendChild(courseRow);
                })
            });
    }

    function tableCellFor(text) {
        const cell = document.createElement("td");

        cell.appendChild(document.createTextNode(text));

        return cell;
    }

    function addFilter(e) {
        e.preventDefault();

        const filterRows = document.getElementById('filter-rows');
        const totalRows  = document.getElementById('filter-rows').childElementCount;

        const filterRowTemplate = "<div class=\"filter-row\">\n" +
                                  "    <div class=\"inline-block relative w-64 mr-3\">\n" +
                                  "        <label class=\"block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2\" for=\"field\">\n" +
                                  "            Campo\n" +
                                  "        </label>\n" +
                                  "        <select name=\"filters[" +
                                  totalRows +
                                  "][field]\" id=\"field\"\n" +
                                  "                class=\"block appearance-none w-full bg-white border border-gray-400 hover:border-gray-500 px-4 py-2 pr-8 rounded shadow leading-tight focus:outline-none focus:shadow-outline\">\n" +
                                  "            <option value=\"id\">Identificador</option>\n" +
                                  "            <option value=\"name\">Nombre</option>\n" +
                                  "            <option value=\"duration\">Duración</option>\n" +
                                  "        </select>\n" +
                                  "        <div class=\"pointer-events-none absolute inset-y-0 right-0 flex items-center px-2 text-gray-700\">\n" +
                                  "            <svg class=\"fill-current h-4 w-4\" xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 20 20\">\n" +
                                  "                <path d=\"M9.293 12.95l.707.707L15.657 8l-1.414-1.414L10 10.828 5.757 6.586 4.343 8z\"/>\n" +
                                  "            </svg>\n" +
                                  "        </div>\n" +
                                  "    </div>\n" +
                                  "    <div class=\"inline-block relative w-64 mr-3\">\n" +
                                  "        <label class=\"block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2\" for=\"operator\">\n" +
                                  "            Operador\n" +
                                  "        </label>\n" +
                                  "        <select id=\"operator\" name=\"filters[" +
                                  totalRows +
                                  "][operator]\"\n" +
                                  "                class=\"block appearance-none w-full bg-white border border-gray-400 hover:border-gray-500 px-4 py-2 pr-8 rounded shadow leading-tight focus:outline-none focus:shadow-outline\">\n" +
                                  "            <option value=\"=\">es exactamente igual</option>\n" +
                                  "            <option value=\"CONTAINS\">contiene</option>\n" +
                                  "            <option value=\">\">es más grande que</option>\n" +
                                  "            <option value=\"<\">es más pequeño que</option>\n" +
                                  "        </select>\n" +
                                  "        <div class=\"pointer-events-none absolute inset-y-0 right-0 flex items-center px-2 text-gray-700\">\n" +
                                  "            <svg class=\"fill-current h-4 w-4\" xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 20 20\">\n" +
                                  "                <path d=\"M9.293 12.95l.707.707L15.657 8l-1.414-1.414L10 10.828 5.757 6.586 4.343 8z\"/>\n" +
                                  "            </svg>\n" +
                                  "        </div>\n" +
                                  "    </div>\n" +
                                  "    <div class=\"inline-block relative w-64 mr-3\">\n" +
                                  "        <label class=\"block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2\" for=\"value\">\n" +
                                  "            Valor\n" +
                                  "        </label>\n" +
                                  "        <input class=\"appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500\"\n" +
                                  "               id=\"value\" type=\"text\" name=\"filters[" +
                                  totalRows +
                                  "][value]\" placeholder=\"Lo que sea...\">\n" +
                                  "    </div>\n" +
                                  "</div>";

        filterRows.insertAdjacentHTML('beforeend', filterRowTemplate);
    }

    function filterCourses(e) {
        e.preventDefault();

        const form = document.forms["filter-courses"];

        const inputs = Array.from(form.getElementsByTagName("input"))
                            .concat(Array.from(form.getElementsByTagName("select")));

        const urlParts = inputs.map(input => input.name + "=" + input.value);

        const url = "http://localhost:8091/courses?" + urlParts.join("&");

        addCoursesList(url);
    }
</script>

<script>
    addCoursesList("http://localhost:8091/courses");
</script>
```

## File: `CodelyTV-java-ddd-example-3a58e32/apps/main/resources/backoffice_frontend/templates/pages/courses/partials/new_course_form.ftl`
```
<form class="w-full max-w-lg float-right" method="post" action="/courses">
    <h2 class="block uppercase tracking-wide text-gray-700 text-3xl font-bold mb-2">Crear curso</h2>
    <div class="flex flex-wrap mb-6 -mx-3">
        <div class="w-full md:w-full px-3 mb-6 md:mb-0">
            <label class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" for="grid-first-name">
                Identificador
            </label>
            <input class="<#if errors['id']?? >border border-red-500</#if> appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
                   id="grid-first-name" type="text" name="id" placeholder="En formado UUID"
                   value="${(inputs['id'])!generated_uuid}">

            <#if errors['id']?? >
                <#list errors['id'] as errorMessage>
                    <p class="text-red-500 text-xs italic">${errorMessage}</p>
                </#list>
            </#if>
        </div>
    </div>
    <div class="flex flex-wrap -mx-3 mb-6">
        <div class="w-full md:w-1/2 px-3 mb-6 md:mb-0">
            <label class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" for="grid-first-name">
                Nombre
            </label>
            <input class="<#if errors['name']?? >border border-red-500</#if> appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
                   id="grid-first-name" type="text" name="name" placeholder="DDD en PHP"
                   value="${(inputs['name'])!""}">

            <#if errors['name']?? >
                <#list errors['name'] as errorMessage>
                    <p class="text-red-500 text-xs italic">${errorMessage}</p>
                </#list>
            </#if>
        </div>
        <div class="w-full md:w-1/2 px-3">
            <label class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" for="grid-last-name">
                Duración (en inglés)
            </label>
            <input class="<#if errors['duration']?? >border border-red-500</#if> appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
                   id="grid-last-name" type="text" name="duration" placeholder="8 days"
                   value="${(inputs['duration'])!""}">
            <#if errors['duration']?? >
                <#list errors['duration'] as errorMessage>
                    <p class="text-red-500 text-xs italic">${errorMessage}</p>
                </#list>
            </#if>
        </div>
    </div>
    <div class="flex flex-wrap mb-6">
        <button class="md:w-full bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
                type="submit">
            Crear curso!
        </button>
    </div>
</form>
```

## File: `CodelyTV-java-ddd-example-3a58e32/apps/main/resources/backoffice_frontend/templates/partials/footer.ftl`
```
<footer class="flex items-center justify-between flex-wrap bg-teal-900 p-5 mt-10">
    <div class="container mx-auto px-4">
        <p class="text-teal-200">
            🤙 CodelyTV - El mejor backoffice de la historia
        </p>
    </div>
</footer>
```

## File: `CodelyTV-java-ddd-example-3a58e32/apps/main/resources/backoffice_frontend/templates/partials/header.ftl`
```
<header>
    <nav class="flex items-center justify-between flex-wrap bg-teal-900 p-5">
        <div class="flex items-center flex-shrink-0 text-white mr-6">
            <a href="/">
                <img src="images/logo.png" alt="" width="150px">
            </a>
        </div>
        <div class="w-full block flex-grow lg:flex lg:items-center lg:w-auto">
            <div class="text-sm lg:flex-grow">
                <a href="#"
                   class="block mt-4 lg:inline-block lg:mt-0 text-teal-200 hover:text-white mr-4">
                    Usuarios
                </a>
                <a href="/courses"
                   class="block mt-4 lg:inline-block lg:mt-0 text-teal-200 hover:text-white mr-4">
                    Cursos
                </a>
                <a href="#" class="block mt-4 lg:inline-block lg:mt-0 text-teal-200 hover:text-white">
                    Vídeos
                </a>
            </div>
            <div>
                <a href="#"
                   class="inline-block text-sm px-4 py-2 leading-none border rounded text-white border-white hover:border-transparent hover:text-teal-500 hover:bg-white mt-4 lg:mt-0">Entrar</a>
            </div>
        </div>
    </nav>
</header>
```

## File: `CodelyTV-java-ddd-example-3a58e32/apps/main/tv/codely/apps/Starter.java`
```java
package tv.codely.apps;

import java.util.Arrays;
import java.util.HashMap;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.WebApplicationType;
import org.springframework.context.ConfigurableApplicationContext;

import tv.codely.apps.backoffice.backend.BackofficeBackendApplication;
import tv.codely.apps.backoffice.frontend.BackofficeFrontendApplication;
import tv.codely.apps.mooc.backend.MoocBackendApplication;
import tv.codely.shared.infrastructure.cli.ConsoleCommand;

public class Starter {

	public static void main(String[] args) {
		if (args.length < 2) {
			throw new RuntimeException("There are not enough arguments");
		}

		String applicationName = args[0];
		String commandName = args[1];
		boolean isServerCommand = commandName.equals("server");

		ensureApplicationExist(applicationName);
		ensureCommandExist(applicationName, commandName);

		Class<?> applicationClass = applications().get(applicationName);

		SpringApplication app = new SpringApplication(applicationClass);

		if (!isServerCommand) {
			app.setWebApplicationType(WebApplicationType.NONE);
		}

		ConfigurableApplicationContext context = app.run(args);

		if (!isServerCommand) {
			ConsoleCommand command = (ConsoleCommand) context.getBean(commands().get(applicationName).get(commandName));

			command.execute(Arrays.copyOfRange(args, 2, args.length));
		}
	}

	private static void ensureApplicationExist(String applicationName) {
		if (!applications().containsKey(applicationName)) {
			throw new RuntimeException(
				String.format(
					"The application <%s> doesn't exist. Valids:\n- %s",
					applicationName,
					String.join("\n- ", applications().keySet())
				)
			);
		}
	}

	private static void ensureCommandExist(String applicationName, String commandName) {
		if (!"server".equals(commandName) && !existCommand(applicationName, commandName)) {
			throw new RuntimeException(
				String.format(
					"The command <%s> for application <%s> doesn't exist. Valids (application.command):\n- api\n- %s",
					commandName,
					applicationName,
					String.join("\n- ", commands().get(applicationName).keySet())
				)
			);
		}
	}

	private static HashMap<String, Class<?>> applications() {
		HashMap<String, Class<?>> applications = new HashMap<>();

		applications.put("mooc_backend", MoocBackendApplication.class);
		applications.put("backoffice_backend", BackofficeBackendApplication.class);
		applications.put("backoffice_frontend", BackofficeFrontendApplication.class);

		return applications;
	}

	private static HashMap<String, HashMap<String, Class<?>>> commands() {
		HashMap<String, HashMap<String, Class<?>>> commands = new HashMap<>();

		commands.put("mooc_backend", MoocBackendApplication.commands());
		commands.put("backoffice_backend", BackofficeBackendApplication.commands());
		commands.put("backoffice_frontend", BackofficeFrontendApplication.commands());

		return commands;
	}

	private static Boolean existCommand(String applicationName, String commandName) {
		HashMap<String, HashMap<String, Class<?>>> commands = commands();

		return commands.containsKey(applicationName) && commands.get(applicationName).containsKey(commandName);
	}
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/apps/main/tv/codely/apps/backoffice/backend/BackofficeBackendApplication.java`
```java
package tv.codely.apps.backoffice.backend;

import java.util.HashMap;

import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.autoconfigure.orm.jpa.HibernateJpaAutoConfiguration;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.FilterType;

import tv.codely.shared.domain.Service;

@SpringBootApplication(exclude = HibernateJpaAutoConfiguration.class)
@ComponentScan(
	includeFilters = @ComponentScan.Filter(type = FilterType.ANNOTATION, classes = Service.class),
	value = { "tv.codely.shared", "tv.codely.backoffice", "tv.codely.apps.backoffice.backend" }
)
public class BackofficeBackendApplication {

	public static HashMap<String, Class<?>> commands() {
		return new HashMap<String, Class<?>>() {
			{}
		};
	}
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/apps/main/tv/codely/apps/backoffice/backend/config/BackofficeBackendServerConfiguration.java`
```java
package tv.codely.apps.backoffice.backend.config;

import org.springframework.boot.web.servlet.FilterRegistrationBean;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import tv.codely.apps.backoffice.backend.middleware.BasicHttpAuthMiddleware;
import tv.codely.shared.domain.bus.command.CommandBus;

@Configuration
public class BackofficeBackendServerConfiguration {

	private final CommandBus bus;

	public BackofficeBackendServerConfiguration(CommandBus bus) {
		this.bus = bus;
	}

	@Bean
	public FilterRegistrationBean<BasicHttpAuthMiddleware> basicHttpAuthMiddleware() {
		FilterRegistrationBean<BasicHttpAuthMiddleware> registrationBean = new FilterRegistrationBean<>();

		registrationBean.setFilter(new BasicHttpAuthMiddleware(bus));
		registrationBean.addUrlPatterns("/health-check");

		return registrationBean;
	}
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/apps/main/tv/codely/apps/backoffice/backend/config/BackofficeBackendServerPortCustomizer.java`
```java
package tv.codely.apps.backoffice.backend.config;

import org.springframework.boot.web.server.ConfigurableWebServerFactory;
import org.springframework.boot.web.server.WebServerFactoryCustomizer;
import org.springframework.stereotype.Component;

import tv.codely.shared.infrastructure.config.Parameter;
import tv.codely.shared.infrastructure.config.ParameterNotExist;

@Component
public final class BackofficeBackendServerPortCustomizer
	implements WebServerFactoryCustomizer<ConfigurableWebServerFactory> {

	private final Parameter param;

	public BackofficeBackendServerPortCustomizer(Parameter param) {
		this.param = param;
	}

	@Override
	public void customize(ConfigurableWebServerFactory factory) {
		try {
			factory.setPort(param.getInt("BACKOFFICE_BACKEND_SERVER_PORT"));
		} catch (ParameterNotExist parameterNotExist) {
			parameterNotExist.printStackTrace();
		}
	}
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/apps/main/tv/codely/apps/backoffice/backend/controller/courses/CoursesGetController.java`
```java
package tv.codely.apps.backoffice.backend.controller.courses;

import java.io.Serializable;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Optional;
import java.util.stream.Collectors;

import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.*;

import tv.codely.backoffice.courses.application.BackofficeCoursesResponse;
import tv.codely.backoffice.courses.application.search_by_criteria.SearchBackofficeCoursesByCriteriaQuery;
import tv.codely.shared.domain.DomainError;
import tv.codely.shared.domain.bus.command.CommandBus;
import tv.codely.shared.domain.bus.query.QueryBus;
import tv.codely.shared.domain.bus.query.QueryHandlerExecutionError;
import tv.codely.shared.infrastructure.spring.ApiController;

@RestController
@CrossOrigin(origins = "*", methods = { RequestMethod.GET })
public final class CoursesGetController extends ApiController {

	public CoursesGetController(QueryBus queryBus, CommandBus commandBus) {
		super(queryBus, commandBus);
	}

	@GetMapping("/courses")
	public List<HashMap<String, String>> index(@RequestParam HashMap<String, Serializable> params)
		throws QueryHandlerExecutionError {
		BackofficeCoursesResponse courses = ask(
			new SearchBackofficeCoursesByCriteriaQuery(
				parseFilters(params),
				Optional.ofNullable((String) params.get("order_by")),
				Optional.ofNullable((String) params.get("order")),
				Optional.ofNullable((Integer) params.get("limit")),
				Optional.ofNullable((Integer) params.get("offset"))
			)
		);

		return courses
			.courses()
			.stream()
			.map(response ->
				new HashMap<String, String>() {
					{
						put("id", response.id());
						put("name", response.name());
						put("duration", response.duration());
					}
				}
			)
			.collect(Collectors.toList());
	}

	@Override
	public HashMap<Class<? extends DomainError>, HttpStatus> errorMapping() {
		return null;
	}

	private List<HashMap<String, String>> parseFilters(HashMap<String, Serializable> params) {
		int maxParams = params.size();

		List<HashMap<String, String>> filters = new ArrayList<>();

		for (int possibleFilterKey = 0; possibleFilterKey < maxParams; possibleFilterKey++) {
			if (params.containsKey(String.format("filters[%s][field]", possibleFilterKey))) {
				int key = possibleFilterKey;

				filters.add(
					new HashMap<String, String>() {
						{
							put("field", (String) params.get(String.format("filters[%s][field]", key)));
							put("operator", (String) params.get(String.format("filters[%s][operator]", key)));
							put("value", (String) params.get(String.format("filters[%s][value]", key)));
						}
					}
				);
			}
		}

		return filters;
	}
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/apps/main/tv/codely/apps/backoffice/backend/controller/health_check/HealthCheckGetController.java`
```java
package tv.codely.apps.backoffice.backend.controller.health_check;

import java.util.HashMap;

import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import tv.codely.shared.domain.DomainError;
import tv.codely.shared.domain.bus.command.CommandBus;
import tv.codely.shared.domain.bus.query.QueryBus;
import tv.codely.shared.infrastructure.spring.ApiController;

@RestController
public final class HealthCheckGetController extends ApiController {

	public HealthCheckGetController(QueryBus queryBus, CommandBus commandBus) {
		super(queryBus, commandBus);
	}

	@GetMapping("/health-check")
	public HashMap<String, String> index() {
		HashMap<String, String> status = new HashMap<>();
		status.put("application", "backoffice_backend");
		status.put("status", "ok");

		return status;
	}

	@Override
	public HashMap<Class<? extends DomainError>, HttpStatus> errorMapping() {
		return null;
	}
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/apps/main/tv/codely/apps/backoffice/backend/middleware/BasicHttpAuthMiddleware.java`
```java
package tv.codely.apps.backoffice.backend.middleware;

import java.io.IOException;
import java.util.Base64;

import jakarta.servlet.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

import tv.codely.backoffice.auth.application.authenticate.AuthenticateUserCommand;
import tv.codely.backoffice.auth.domain.InvalidAuthCredentials;
import tv.codely.backoffice.auth.domain.InvalidAuthUsername;
import tv.codely.shared.domain.bus.command.CommandBus;
import tv.codely.shared.domain.bus.command.CommandHandlerExecutionError;

public final class BasicHttpAuthMiddleware implements Filter {

	private final CommandBus bus;

	public BasicHttpAuthMiddleware(CommandBus bus) {
		this.bus = bus;
	}

	@Override
	public void doFilter(ServletRequest request, ServletResponse response, FilterChain chain)
		throws IOException, ServletException {
		String authorizationHeader = ((HttpServletRequest) request).getHeader("authorization");

		if (hasIntroducedCredentials(authorizationHeader)) {
			authenticate(authorizationHeader, chain, request, response);
		} else {
			askForCredentials(response);
		}
	}

	private boolean hasIntroducedCredentials(String authorizationHeader) {
		return null != authorizationHeader;
	}

	private void authenticate(
		String authorizationHeader,
		FilterChain chain,
		ServletRequest request,
		ServletResponse response
	) throws IOException, ServletException {
		String[] auth = decodeAuth(authorizationHeader);
		String user = auth[0];
		String pass = auth[1];

		try {
			bus.dispatch(new AuthenticateUserCommand(user, pass));

			request.setAttribute("authentication_username", user);

			chain.doFilter(request, response);
		} catch (InvalidAuthUsername | InvalidAuthCredentials | CommandHandlerExecutionError error) {
			setInvalidCredentials(response);
		}
	}

	private String[] decodeAuth(String authString) {
		return new String(Base64.getDecoder().decode(authString.split("\\s+")[1])).split(":");
	}

	private void setInvalidCredentials(ServletResponse response) {
		HttpServletResponse httpServletResponse = (HttpServletResponse) response;
		httpServletResponse.reset();
		httpServletResponse.setStatus(HttpServletResponse.SC_FORBIDDEN);
	}

	private void askForCredentials(ServletResponse response) {
		HttpServletResponse httpServletResponse = (HttpServletResponse) response;
		httpServletResponse.reset();
		httpServletResponse.setStatus(HttpServletResponse.SC_UNAUTHORIZED);
		httpServletResponse.setHeader("WWW-Authenticate", "Basic realm=\"CodelyTV\"");
	}
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/apps/main/tv/codely/apps/backoffice/frontend/BackofficeFrontendApplication.java`
```java
package tv.codely.apps.backoffice.frontend;

import java.util.HashMap;

import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.autoconfigure.orm.jpa.HibernateJpaAutoConfiguration;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.FilterType;

import tv.codely.shared.domain.Service;

@SpringBootApplication(exclude = HibernateJpaAutoConfiguration.class)
@ComponentScan(
	includeFilters = @ComponentScan.Filter(type = FilterType.ANNOTATION, classes = Service.class),
	value = { "tv.codely.shared", "tv.codely.backoffice", "tv.codely.mooc", "tv.codely.apps.backoffice.frontend" }
)
public class BackofficeFrontendApplication {

	public static HashMap<String, Class<?>> commands() {
		return new HashMap<String, Class<?>>() {
			{}
		};
	}
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/apps/main/tv/codely/apps/backoffice/frontend/config/BackofficeFrontendServerPortCustomizer.java`
```java
package tv.codely.apps.backoffice.frontend.config;

import org.springframework.boot.web.server.ConfigurableWebServerFactory;
import org.springframework.boot.web.server.WebServerFactoryCustomizer;
import org.springframework.stereotype.Component;

import tv.codely.shared.infrastructure.config.Parameter;
import tv.codely.shared.infrastructure.config.ParameterNotExist;

@Component
public final class BackofficeFrontendServerPortCustomizer
	implements WebServerFactoryCustomizer<ConfigurableWebServerFactory> {

	private final Parameter param;

	public BackofficeFrontendServerPortCustomizer(Parameter param) {
		this.param = param;
	}

	@Override
	public void customize(ConfigurableWebServerFactory factory) {
		try {
			factory.setPort(param.getInt("BACKOFFICE_FRONTEND_SERVER_PORT"));
		} catch (ParameterNotExist parameterNotExist) {
			parameterNotExist.printStackTrace();
		}
	}
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/apps/main/tv/codely/apps/backoffice/frontend/config/BackofficeFrontendWebConfig.java`
```java
package tv.codely.apps.backoffice.frontend.config;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.servlet.ViewResolver;
import org.springframework.web.servlet.config.annotation.EnableWebMvc;
import org.springframework.web.servlet.config.annotation.ResourceHandlerRegistry;
import org.springframework.web.servlet.config.annotation.ViewResolverRegistry;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;
import org.springframework.web.servlet.view.freemarker.FreeMarkerConfigurer;
import org.springframework.web.servlet.view.freemarker.FreeMarkerViewResolver;

@Configuration
@EnableWebMvc
public class BackofficeFrontendWebConfig implements WebMvcConfigurer {

	@Override
	public void configureViewResolvers(ViewResolverRegistry registry) {
		registry.freeMarker();
	}

	@Override
	public void addResourceHandlers(ResourceHandlerRegistry registry) {
		registry.addResourceHandler("/**").addResourceLocations("classpath:/backoffice_frontend/public/");
	}

	@Bean
	public ViewResolver getViewResolver() {
		FreeMarkerViewResolver resolver = new FreeMarkerViewResolver();
		resolver.setCache(false);
		resolver.setSuffix(".ftl");
		return resolver;
	}

	@Bean
	public FreeMarkerConfigurer freeMarkerConfigurer() {
		FreeMarkerConfigurer configurer = new FreeMarkerConfigurer();
		configurer.setTemplateLoaderPath("classpath:/backoffice_frontend/templates/");
		configurer.setDefaultEncoding("UTF-8");
		//        configurer.setFreemarkerVariables(new HashMap<String, Object>() {{
		//            put("flash", new Flash());
		//        }});

		return configurer;
	}
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/apps/main/tv/codely/apps/backoffice/frontend/controller/courses/CoursesGetWebController.java`
```java
package tv.codely.apps.backoffice.frontend.controller.courses;

import java.io.Serializable;
import java.util.HashMap;
import java.util.List;
import java.util.UUID;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.servlet.ModelAndView;

import tv.codely.mooc.courses_counter.application.find.CoursesCounterResponse;
import tv.codely.mooc.courses_counter.application.find.FindCoursesCounterQuery;
import tv.codely.shared.domain.bus.query.QueryBus;
import tv.codely.shared.domain.bus.query.QueryHandlerExecutionError;

@Controller
public final class CoursesGetWebController {

	private final QueryBus bus;

	public CoursesGetWebController(QueryBus bus) {
		this.bus = bus;
	}

	@GetMapping("/courses")
	public ModelAndView index(
		@ModelAttribute("inputs") HashMap<String, Serializable> inputs,
		@ModelAttribute("errors") HashMap<String, List<String>> errors
	) throws QueryHandlerExecutionError {
		CoursesCounterResponse counterResponse = bus.ask(new FindCoursesCounterQuery());

		return new ModelAndView(
			"pages/courses/courses",
			new HashMap<String, Serializable>() {
				{
					put("title", "Courses");
					put("description", "Courses CodelyTV - Backoffice");
					put("courses_counter", counterResponse.total());
					put("inputs", inputs);
					put("errors", errors);
					put("generated_uuid", UUID.randomUUID().toString());
				}
			}
		);
	}
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/apps/main/tv/codely/apps/backoffice/frontend/controller/courses/CoursesPostWebController.java`
```java
package tv.codely.apps.backoffice.frontend.controller.courses;

import java.io.Serializable;
import java.util.HashMap;

import org.springframework.http.MediaType;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.servlet.mvc.support.RedirectAttributes;
import org.springframework.web.servlet.view.RedirectView;

import tv.codely.mooc.courses.application.create.CreateCourseCommand;
import tv.codely.shared.domain.bus.command.CommandBus;
import tv.codely.shared.domain.bus.command.CommandHandlerExecutionError;
import tv.codely.shared.infrastructure.validation.ValidationResponse;
import tv.codely.shared.infrastructure.validation.Validator;

@Controller
public final class CoursesPostWebController {

	private final CommandBus bus;
	private final HashMap<String, String> rules = new HashMap<String, String>() {
		{
			put("id", "required|not_empty|uuid");
			put("name", "required|not_empty|string");
			put("duration", "required|not_empty|string");
		}
	};

	public CoursesPostWebController(CommandBus bus) {
		this.bus = bus;
	}

	@PostMapping(value = "/courses", consumes = MediaType.APPLICATION_FORM_URLENCODED_VALUE)
	public RedirectView index(@RequestParam HashMap<String, Serializable> request, RedirectAttributes attributes)
		throws Exception {
		ValidationResponse validationResponse = Validator.validate(request, rules);

		return validationResponse.hasErrors()
			? redirectWithErrors(validationResponse, request, attributes)
			: createCourse(request);
	}

	private RedirectView redirectWithErrors(
		ValidationResponse validationResponse,
		HashMap<String, Serializable> request,
		RedirectAttributes attributes
	) {
		attributes.addFlashAttribute("errors", validationResponse.errors());
		attributes.addFlashAttribute("inputs", request);

		return new RedirectView("/courses");
	}

	private RedirectView createCourse(HashMap<String, Serializable> request) throws CommandHandlerExecutionError {
		bus.dispatch(
			new CreateCourseCommand(
				request.get("id").toString(),
				request.get("name").toString(),
				request.get("duration").toString()
			)
		);

		return new RedirectView("/courses");
	}
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/apps/main/tv/codely/apps/backoffice/frontend/controller/health_check/HealthCheckGetController.java`
```java
package tv.codely.apps.backoffice.frontend.controller.health_check;

import java.util.HashMap;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public final class HealthCheckGetController {

	@GetMapping("/health-check")
	public HashMap<String, String> index() {
		HashMap<String, String> status = new HashMap<>();
		status.put("application", "backoffice_frontend");
		status.put("status", "ok");

		return status;
	}
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/apps/main/tv/codely/apps/backoffice/frontend/controller/home/HomeGetWebController.java`
```java
package tv.codely.apps.backoffice.frontend.controller.home;

import java.io.Serializable;
import java.util.HashMap;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.servlet.ModelAndView;

@Controller
public final class HomeGetWebController {

	@GetMapping("/")
	public ModelAndView index() {
		return new ModelAndView(
			"pages/home",
			new HashMap<String, Serializable>() {
				{
					put("title", "Welcome");
					put("description", "CodelyTV - Backoffice");
				}
			}
		);
	}
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/apps/main/tv/codely/apps/mooc/backend/MoocBackendApplication.java`
```java
package tv.codely.apps.mooc.backend;

import java.util.HashMap;

import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.autoconfigure.orm.jpa.HibernateJpaAutoConfiguration;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.FilterType;

import tv.codely.apps.mooc.backend.command.ConsumeMySqlDomainEventsCommand;
import tv.codely.apps.mooc.backend.command.ConsumeRabbitMqDomainEventsCommand;
import tv.codely.shared.domain.Service;

@SpringBootApplication(exclude = HibernateJpaAutoConfiguration.class)
@ComponentScan(
	includeFilters = @ComponentScan.Filter(type = FilterType.ANNOTATION, classes = Service.class),
	value = { "tv.codely.shared", "tv.codely.mooc", "tv.codely.apps.mooc.backend" }
)
public class MoocBackendApplication {

	public static HashMap<String, Class<?>> commands() {
		return new HashMap<String, Class<?>>() {
			{
				put("domain-events:mysql:consume", ConsumeMySqlDomainEventsCommand.class);
				put("domain-events:rabbitmq:consume", ConsumeRabbitMqDomainEventsCommand.class);
			}
		};
	}
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/apps/main/tv/codely/apps/mooc/backend/command/ConsumeMySqlDomainEventsCommand.java`
```java
package tv.codely.apps.mooc.backend.command;

import tv.codely.shared.infrastructure.bus.event.mysql.MySqlDomainEventsConsumer;
import tv.codely.shared.infrastructure.cli.ConsoleCommand;

public final class ConsumeMySqlDomainEventsCommand extends ConsoleCommand {

	private final MySqlDomainEventsConsumer consumer;

	public ConsumeMySqlDomainEventsCommand(MySqlDomainEventsConsumer consumer) {
		this.consumer = consumer;
	}

	@Override
	public void execute(String[] args) {
		consumer.consume();
	}
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/apps/main/tv/codely/apps/mooc/backend/command/ConsumeRabbitMqDomainEventsCommand.java`
```java
package tv.codely.apps.mooc.backend.command;

import tv.codely.shared.infrastructure.bus.event.rabbitmq.RabbitMqDomainEventsConsumer;
import tv.codely.shared.infrastructure.cli.ConsoleCommand;

public final class ConsumeRabbitMqDomainEventsCommand extends ConsoleCommand {

	private final RabbitMqDomainEventsConsumer consumer;

	public ConsumeRabbitMqDomainEventsCommand(RabbitMqDomainEventsConsumer consumer) {
		this.consumer = consumer;
	}

	@Override
	public void execute(String[] args) {
		consumer.consume();
	}
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/apps/main/tv/codely/apps/mooc/backend/config/MoocBackendServerConfiguration.java`
```java
package tv.codely.apps.mooc.backend.config;

import org.springframework.boot.web.servlet.FilterRegistrationBean;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.servlet.mvc.method.annotation.RequestMappingHandlerMapping;

import tv.codely.shared.infrastructure.spring.ApiExceptionMiddleware;

@Configuration
public class MoocBackendServerConfiguration {

	private final RequestMappingHandlerMapping mapping;

	public MoocBackendServerConfiguration(RequestMappingHandlerMapping mapping) {
		this.mapping = mapping;
	}

	@Bean
	public FilterRegistrationBean<ApiExceptionMiddleware> apiExceptionMiddleware() {
		FilterRegistrationBean<ApiExceptionMiddleware> registrationBean = new FilterRegistrationBean<>();

		registrationBean.setFilter(new ApiExceptionMiddleware(mapping));

		return registrationBean;
	}
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/apps/main/tv/codely/apps/mooc/backend/config/MoocBackendServerPortCustomizer.java`
```java
package tv.codely.apps.mooc.backend.config;

import org.springframework.boot.web.server.ConfigurableWebServerFactory;
import org.springframework.boot.web.server.WebServerFactoryCustomizer;
import org.springframework.stereotype.Component;

import tv.codely.shared.infrastructure.config.Parameter;
import tv.codely.shared.infrastructure.config.ParameterNotExist;

@Component
public final class MoocBackendServerPortCustomizer implements WebServerFactoryCustomizer<ConfigurableWebServerFactory> {

	private final Parameter param;

	public MoocBackendServerPortCustomizer(Parameter param) {
		this.param = param;
	}

	@Override
	public void customize(ConfigurableWebServerFactory factory) {
		try {
			factory.setPort(param.getInt("MOOC_BACKEND_SERVER_PORT"));
		} catch (ParameterNotExist parameterNotExist) {
			parameterNotExist.printStackTrace();
		}
	}
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/apps/main/tv/codely/apps/mooc/backend/controller/courses/CourseGetController.java`
```java
package tv.codely.apps.mooc.backend.controller.courses;

import java.io.Serializable;
import java.util.HashMap;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RestController;

import tv.codely.mooc.courses.application.CourseResponse;
import tv.codely.mooc.courses.application.find.FindCourseQuery;
import tv.codely.mooc.courses.domain.CourseNotExist;
import tv.codely.shared.domain.DomainError;
import tv.codely.shared.domain.bus.command.CommandBus;
import tv.codely.shared.domain.bus.query.QueryBus;
import tv.codely.shared.domain.bus.query.QueryHandlerExecutionError;
import tv.codely.shared.infrastructure.spring.ApiController;

@RestController
public final class CourseGetController extends ApiController {

	public CourseGetController(QueryBus queryBus, CommandBus commandBus) {
		super(queryBus, commandBus);
	}

	@GetMapping("/courses/{id}")
	public ResponseEntity<HashMap<String, Serializable>> index(@PathVariable String id)
		throws QueryHandlerExecutionError {
		CourseResponse course = ask(new FindCourseQuery(id));

		return ResponseEntity
			.ok()
			.body(
				new HashMap<String, Serializable>() {
					{
						put("id", course.id());
						put("name", course.name());
						put("duration", course.duration());
					}
				}
			);
	}

	@Override
	public HashMap<Class<? extends DomainError>, HttpStatus> errorMapping() {
		return new HashMap<Class<? extends DomainError>, HttpStatus>() {
			{
				put(CourseNotExist.class, HttpStatus.NOT_FOUND);
			}
		};
	}
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/apps/main/tv/codely/apps/mooc/backend/controller/courses/CoursesPutController.java`
```java
package tv.codely.apps.mooc.backend.controller.courses;

import java.util.HashMap;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import tv.codely.mooc.courses.application.create.CreateCourseCommand;
import tv.codely.shared.domain.DomainError;
import tv.codely.shared.domain.bus.command.CommandBus;
import tv.codely.shared.domain.bus.command.CommandHandlerExecutionError;
import tv.codely.shared.domain.bus.query.QueryBus;
import tv.codely.shared.infrastructure.spring.ApiController;

@RestController
public final class CoursesPutController extends ApiController {

	public CoursesPutController(QueryBus queryBus, CommandBus commandBus) {
		super(queryBus, commandBus);
	}

	@PutMapping(value = "/courses/{id}")
	public ResponseEntity<String> index(@PathVariable String id, @RequestBody Request request)
		throws CommandHandlerExecutionError {
		dispatch(new CreateCourseCommand(id, request.name(), request.duration()));

		return new ResponseEntity<>(HttpStatus.CREATED);
	}

	@Override
	public HashMap<Class<? extends DomainError>, HttpStatus> errorMapping() {
		return null;
	}
}

final class Request {

	private String name;
	private String duration;

	public void setDuration(String duration) {
		this.duration = duration;
	}

	public void setName(String name) {
		this.name = name;
	}

	String name() {
		return name;
	}

	String duration() {
		return duration;
	}
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/apps/main/tv/codely/apps/mooc/backend/controller/courses_counter/CoursesCounterGetController.java`
```java
package tv.codely.apps.mooc.backend.controller.courses_counter;

import java.util.HashMap;

import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import tv.codely.mooc.courses_counter.application.find.CoursesCounterResponse;
import tv.codely.mooc.courses_counter.application.find.FindCoursesCounterQuery;
import tv.codely.shared.domain.DomainError;
import tv.codely.shared.domain.bus.command.CommandBus;
import tv.codely.shared.domain.bus.query.QueryBus;
import tv.codely.shared.domain.bus.query.QueryHandlerExecutionError;
import tv.codely.shared.infrastructure.spring.ApiController;

@RestController
public final class CoursesCounterGetController extends ApiController {

	public CoursesCounterGetController(QueryBus queryBus, CommandBus commandBus) {
		super(queryBus, commandBus);
	}

	@GetMapping("/courses-counter")
	public HashMap<String, Integer> index() throws QueryHandlerExecutionError {
		CoursesCounterResponse response = ask(new FindCoursesCounterQuery());

		return new HashMap<String, Integer>() {
			{
				put("total", response.total());
			}
		};
	}

	@Override
	public HashMap<Class<? extends DomainError>, HttpStatus> errorMapping() {
		return null;
	}
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/apps/main/tv/codely/apps/mooc/backend/controller/health_check/HealthCheckGetController.java`
```java
package tv.codely.apps.mooc.backend.controller.health_check;

import java.util.HashMap;

import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import tv.codely.shared.domain.DomainError;
import tv.codely.shared.domain.bus.command.CommandBus;
import tv.codely.shared.domain.bus.query.QueryBus;
import tv.codely.shared.infrastructure.spring.ApiController;

@RestController
public final class HealthCheckGetController extends ApiController {

	public HealthCheckGetController(QueryBus queryBus, CommandBus commandBus) {
		super(queryBus, commandBus);
	}

	@GetMapping("/health-check")
	public HashMap<String, String> index() {
		HashMap<String, String> status = new HashMap<>();
		status.put("application", "mooc_backend");
		status.put("status", "ok");

		return status;
	}

	@Override
	public HashMap<Class<? extends DomainError>, HttpStatus> errorMapping() {
		return null;
	}
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/apps/main/tv/codely/apps/mooc/backend/controller/notifications/NewsletterNotificationPutController.java`
```java
package tv.codely.apps.mooc.backend.controller.notifications;

import java.util.HashMap;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RestController;

import tv.codely.mooc.notifications.application.send_new_courses_newsletter.SendNewCoursesNewsletterCommand;
import tv.codely.shared.domain.DomainError;
import tv.codely.shared.domain.bus.command.CommandBus;
import tv.codely.shared.domain.bus.command.CommandHandlerExecutionError;
import tv.codely.shared.domain.bus.query.QueryBus;
import tv.codely.shared.infrastructure.spring.ApiController;

@RestController
public final class NewsletterNotificationPutController extends ApiController {

	public NewsletterNotificationPutController(QueryBus queryBus, CommandBus commandBus) {
		super(queryBus, commandBus);
	}

	@PutMapping(value = "/newsletter/{id}")
	public ResponseEntity<String> index(@PathVariable String id) throws CommandHandlerExecutionError {
		dispatch(new SendNewCoursesNewsletterCommand(id));

		return new ResponseEntity<>(HttpStatus.CREATED);
	}

	@Override
	public HashMap<Class<? extends DomainError>, HttpStatus> errorMapping() {
		return null;
	}
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/apps/test/resources/log4j2.properties`
```
name                                         = CodelyTvJavaDddExample
property.filename                            = logs
appenders                                    = console, file

status                                       = warn

appender.console.name                        = CONSOLE
appender.console.type                        = CONSOLE
appender.console.target                      = SYSTEM_OUT

appender.console.layout.type                 = PatternLayout
appender.console.layout.pattern              = [%level] [%date{HH:mm:ss.SSS}] [%class{0}#%method:%line] %message \(%mdc\) %n%throwable
appender.console.filter.threshold.type       = ThresholdFilter
appender.console.filter.threshold.level      = info

appender.file.type                           = File
appender.file.name                           = LOGFILE
appender.file.fileName                       = var/log/java-ddd-example-test.log
appender.file.logstash.type                  = LogstashLayout
appender.file.logstash.dateTimeFormatPattern = yyyy-MM-dd'T'HH:mm:ss.SSSZZZ
appender.file.logstash.eventTemplateUri      = classpath:LogstashJsonEventLayoutV1.json
appender.file.logstash.prettyPrintEnabled    = false
appender.file.logstash.stackTraceEnabled     = true

loggers                                      = file
logger.file.name                             = tv.codely.java_ddd_example
logger.file.level                            = info
logger.file.appenderRefs                     = file
logger.file.appenderRef.file.ref             = LOGFILE

rootLogger.level                             = info
rootLogger.appenderRefs                      = stdout
rootLogger.appenderRef.stdout.ref            = CONSOLE
```

## File: `CodelyTV-java-ddd-example-3a58e32/apps/test/tv/codely/apps/ApplicationTestCase.java`
```java
package tv.codely.apps;

import static org.springframework.http.MediaType.APPLICATION_JSON;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.get;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.request;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.content;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status;

import java.util.Arrays;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.AutoConfigureMockMvc;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.http.HttpHeaders;
import org.springframework.http.HttpMethod;
import org.springframework.test.web.servlet.MockMvc;
import org.springframework.test.web.servlet.ResultMatcher;

import tv.codely.shared.domain.bus.event.DomainEvent;
import tv.codely.shared.domain.bus.event.EventBus;

@SpringBootTest
@AutoConfigureMockMvc
public abstract class ApplicationTestCase {

	@Autowired
	private MockMvc mockMvc;

	@Autowired
	private EventBus eventBus;

	protected void assertResponse(String endpoint, Integer expectedStatusCode, String expectedResponse) throws Exception {
		ResultMatcher response = expectedResponse.isEmpty() ? content().string("") : content().json(expectedResponse);

		mockMvc.perform(get(endpoint)).andExpect(status().is(expectedStatusCode)).andExpect(response);
	}

	protected void assertResponse(
		String endpoint,
		Integer expectedStatusCode,
		String expectedResponse,
		HttpHeaders headers
	) throws Exception {
		ResultMatcher response = expectedResponse.isEmpty() ? content().string("") : content().json(expectedResponse);

		mockMvc.perform(get(endpoint).headers(headers)).andExpect(status().is(expectedStatusCode)).andExpect(response);
	}

	protected void assertRequestWithBody(String method, String endpoint, String body, Integer expectedStatusCode)
		throws Exception {
		mockMvc
			.perform(request(HttpMethod.valueOf(method), endpoint).content(body).contentType(APPLICATION_JSON))
			.andExpect(status().is(expectedStatusCode))
			.andExpect(content().string(""));
	}

	protected void assertRequest(String method, String endpoint, Integer expectedStatusCode) throws Exception {
		mockMvc
			.perform(request(HttpMethod.valueOf(method), endpoint))
			.andExpect(status().is(expectedStatusCode))
			.andExpect(content().string(""));
	}

	protected void givenISendEventsToTheBus(DomainEvent... domainEvents) {
		eventBus.publish(Arrays.asList(domainEvents));
	}
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/apps/test/tv/codely/apps/backoffice/BackofficeApplicationTestCase.java`
```java
package tv.codely.apps.backoffice;

import org.springframework.transaction.annotation.Transactional;

import tv.codely.apps.ApplicationTestCase;

@Transactional("backoffice-transaction_manager")
public abstract class BackofficeApplicationTestCase extends ApplicationTestCase {}
```

## File: `CodelyTV-java-ddd-example-3a58e32/apps/test/tv/codely/apps/backoffice/backend/controller/health_check/HealthCheckGetControllerShould.java`
```java
package tv.codely.apps.backoffice.backend.controller.health_check;

import org.junit.jupiter.api.Test;
import org.springframework.http.HttpHeaders;

import tv.codely.apps.ApplicationTestCase;

final class HealthCheckGetControllerShould extends ApplicationTestCase {

	@Test
	void check_the_app_is_working_ok_with_valid_credentials() throws Exception {
		HttpHeaders headers = new HttpHeaders();
		headers.setBasicAuth("javi", "barbitas");

		assertResponse("/health-check", 200, "{'application':'backoffice_backend','status':'ok'}", headers);
	}

	@Test
	void not_check_the_app_is_working_ok_with_invalid_credentials() throws Exception {
		HttpHeaders headers = new HttpHeaders();
		headers.setBasicAuth("tipo_de_incognito", "homer.sampson");

		assertResponse("/health-check", 403, "", headers);
	}

	@Test
	void not_check_the_app_is_working_ok_with_invalid_credentials_of_an_existing_user() throws Exception {
		HttpHeaders headers = new HttpHeaders();
		headers.setBasicAuth("rafa", "incorrect.password");

		assertResponse("/health-check", 403, "", headers);
	}

	@Test
	void not_check_the_app_is_working_ok_with_no_credentials() throws Exception {
		assertResponse("/health-check", 401, "");
	}
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/apps/test/tv/codely/apps/backoffice/frontend/controller/health_check/HealthCheckGetControllerShould.java`
```java
package tv.codely.apps.backoffice.frontend.controller.health_check;

import org.junit.jupiter.api.Test;

import tv.codely.apps.ApplicationTestCase;

final class HealthCheckGetControllerShould extends ApplicationTestCase {

	@Test
	void check_the_app_is_working_ok() throws Exception {
		assertResponse("/health-check", 200, "{'application':'backoffice_frontend','status':'ok'}");
	}
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/apps/test/tv/codely/apps/mooc/MoocApplicationTestCase.java`
```java
package tv.codely.apps.mooc;

import org.springframework.transaction.annotation.Transactional;

import tv.codely.apps.ApplicationTestCase;

@Transactional("mooc-transaction_manager")
public abstract class MoocApplicationTestCase extends ApplicationTestCase {}
```

## File: `CodelyTV-java-ddd-example-3a58e32/apps/test/tv/codely/apps/mooc/backend/controller/courses/CourseGetControllerShould.java`
```java
package tv.codely.apps.mooc.backend.controller.courses;

import org.junit.jupiter.api.Test;

import tv.codely.apps.mooc.MoocApplicationTestCase;

final class CourseGetControllerShould extends MoocApplicationTestCase {

	@Test
	void find_an_existing_course() throws Exception {
		String id = "99ad55f5-6eab-4d73-b383-c63268e251e8";
		String body = "{\"name\": \"The best course\", \"duration\": \"5 hours\"}";

		givenThereIsACourse(id, body);

		assertResponse(String.format("/courses/%s", id), 200, body);
	}

	@Test
	void no_find_a_non_existing_course() throws Exception {
		String id = "4ecc0cb3-05b2-4238-b7e1-1fbb0d5d3661";
		String body =
			"{\"error_code\": \"course_not_exist\", \"message\": \"The course <4ecc0cb3-05b2-4238-b7e1-1fbb0d5d3661> doesn't exist\"}";

		assertResponse(String.format("/courses/%s", id), 404, body);
	}

	private void givenThereIsACourse(String id, String body) throws Exception {
		assertRequestWithBody("PUT", String.format("/courses/%s", id), body, 201);
	}
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/apps/test/tv/codely/apps/mooc/backend/controller/courses/CoursesPutControllerShould.java`
```java
package tv.codely.apps.mooc.backend.controller.courses;

import org.junit.jupiter.api.Test;

import tv.codely.apps.mooc.MoocApplicationTestCase;

public final class CoursesPutControllerShould extends MoocApplicationTestCase {

	@Test
	void create_a_valid_non_existing_course() throws Exception {
		assertRequestWithBody(
			"PUT",
			"/courses/1aab45ba-3c7a-4344-8936-78466eca77fa",
			"{\"name\": \"The best course\", \"duration\": \"5 hours\"}",
			201
		);
	}
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/apps/test/tv/codely/apps/mooc/backend/controller/courses_counter/CoursesCounterGetControllerShould.java`
```java
package tv.codely.apps.mooc.backend.controller.courses_counter;

import org.junit.jupiter.api.Test;

import tv.codely.apps.mooc.MoocApplicationTestCase;
import tv.codely.shared.domain.course.CourseCreatedDomainEvent;

public final class CoursesCounterGetControllerShould extends MoocApplicationTestCase {

	@Test
	void get_the_counter_with_one_course() throws Exception {
		givenISendEventsToTheBus(
			new CourseCreatedDomainEvent("8f34bc99-e0e2-4296-a008-75f51f03aeb4", "DDD en Java", "7 days")
		);

		assertResponse("/courses-counter", 200, "{'total': 1}");
	}

	@Test
	void get_the_counter_with_more_than_one_course() throws Exception {
		givenISendEventsToTheBus(
			new CourseCreatedDomainEvent("8f34bc99-e0e2-4296-a008-75f51f03aeb4", "DDD en Java", "7 days"),
			new CourseCreatedDomainEvent("3642f700-868a-4778-9317-a2d542d01785", "DDD en PHP", "6 days"),
			new CourseCreatedDomainEvent("92dd8402-69f3-4900-b569-3f2c2797065f", "DDD en Cobol", "10 years")
		);

		assertResponse("/courses-counter", 200, "{'total': 3}");
	}

	@Test
	void get_the_counter_with_more_than_one_course_having_duplicated_events() throws Exception {
		givenISendEventsToTheBus(
			new CourseCreatedDomainEvent("8f34bc99-e0e2-4296-a008-75f51f03aeb4", "DDD en Java", "7 days"),
			new CourseCreatedDomainEvent("8f34bc99-e0e2-4296-a008-75f51f03aeb4", "DDD en Java", "7 days"),
			new CourseCreatedDomainEvent("8f34bc99-e0e2-4296-a008-75f51f03aeb4", "DDD en Java", "7 days"),
			new CourseCreatedDomainEvent("3642f700-868a-4778-9317-a2d542d01785", "DDD en PHP", "6 days"),
			new CourseCreatedDomainEvent("3642f700-868a-4778-9317-a2d542d01785", "DDD en PHP", "6 days"),
			new CourseCreatedDomainEvent("3642f700-868a-4778-9317-a2d542d01785", "DDD en PHP", "6 days"),
			new CourseCreatedDomainEvent("3642f700-868a-4778-9317-a2d542d01785", "DDD en PHP", "6 days"),
			new CourseCreatedDomainEvent("92dd8402-69f3-4900-b569-3f2c2797065f", "DDD en Cobol", "10 years"),
			new CourseCreatedDomainEvent("92dd8402-69f3-4900-b569-3f2c2797065f", "DDD en Cobol", "10 years")
		);

		assertResponse("/courses-counter", 200, "{'total': 3}");
	}
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/apps/test/tv/codely/apps/mooc/backend/controller/health_check/HealthCheckGetControllerShould.java`
```java
package tv.codely.apps.mooc.backend.controller.health_check;

import org.junit.jupiter.api.Test;

import tv.codely.apps.mooc.MoocApplicationTestCase;

final class HealthCheckGetControllerShould extends MoocApplicationTestCase {

	@Test
	void check_the_app_is_working_ok() throws Exception {
		assertResponse("/health-check", 200, "{'application':'mooc_backend','status':'ok'}");
	}
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/apps/test/tv/codely/apps/mooc/backend/controller/notifications/NewsletterNotificationPutControllerShould.java`
```java
package tv.codely.apps.mooc.backend.controller.notifications;

import org.junit.jupiter.api.Test;

import tv.codely.apps.mooc.MoocApplicationTestCase;

final class NewsletterNotificationPutControllerShould extends MoocApplicationTestCase {

	@Test
	void create_a_valid_non_existing_course() throws Exception {
		assertRequest("PUT", "/newsletter/6eebbe60-50e7-400a-810c-3e0af0943ee6", 201);
	}
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/doc/endpoints/backoffice_frontend.http`
```
# ELASTIC - Search
POST localhost:9200/backoffice_courses/_search
Content-Type: application/json

{
  "query": {
    "term": {
      "name": "git avanzado"
    }
  }
}

###

# ELASTIC - debug
POST localhost:9200/backoffice_courses/_search
Content-Type: application/json

{
  "from": 0,
  "size": 1000,
  "query": {
    "bool": {
      "must": [
        {
          "term": {
            "name": {
              "value": "pepe2"
            }
          }
        }
      ],
      "adjust_pure_negative": true,
      "boost": 1.0
    }
  }
}

###
# ELASTIC - Search
POST localhost:9200/backoffice_courses/_search
Content-Type: application/json

###
# ELASTIC - Mapping
GET localhost:9200/backoffice_courses/_mapping
Content-Type: application/json

###
# ELASTIC - Change mapping
PUT localhost:9200/backoffice_courses/_mapping/_doc
Content-Type: application/json

{
  "properties": {
    "name": {
      "type": "text",
      "fielddata": true
    }
  }
}

###
# ELASTIC - DELETE
DELETE localhost:9200/backoffice_courses

###

PUT localhost:9200/backoffice_courses/_settings
Content-Type: application/json

{
  "index": {
    "blocks": {
      "read_only_allow_delete": "false"
    }
  }
}

###
```

## File: `CodelyTV-java-ddd-example-3a58e32/gradle/wrapper/gradle-wrapper.properties`
```
distributionBase=GRADLE_USER_HOME
distributionPath=wrapper/dists
distributionUrl=https\://services.gradle.org/distributions/gradle-8.4-bin.zip
networkTimeout=10000
validateDistributionUrl=true
zipStoreBase=GRADLE_USER_HOME
zipStorePath=wrapper/dists
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/analytics/main/tv/codely/analytics/domain_events/application/store/DomainEventStorer.java`
```java
package tv.codely.analytics.domain_events.application.store;

import tv.codely.analytics.domain_events.domain.*;

public final class DomainEventStorer {
    private DomainEventsRepository repository;

    public DomainEventStorer(DomainEventsRepository repository) {
        this.repository = repository;
    }

    public void store(
        AnalyticsDomainEventId id,
        AnalyticsDomainEventAggregateId aggregateId,
        AnalyticsDomainEventName name,
        AnalyticsDomainEventBody body
    ) {
        AnalyticsDomainEvent domainEvent = new AnalyticsDomainEvent(id, aggregateId, name, body);

        repository.save(domainEvent);
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/analytics/main/tv/codely/analytics/domain_events/application/store/StoreDomainEventOnOccurred.java`
```java
package tv.codely.analytics.domain_events.application.store;

import org.springframework.context.event.EventListener;
import tv.codely.analytics.domain_events.domain.AnalyticsDomainEventAggregateId;
import tv.codely.analytics.domain_events.domain.AnalyticsDomainEventBody;
import tv.codely.analytics.domain_events.domain.AnalyticsDomainEventId;
import tv.codely.analytics.domain_events.domain.AnalyticsDomainEventName;
import tv.codely.shared.domain.bus.event.DomainEvent;
import tv.codely.shared.domain.bus.event.DomainEventSubscriber;

@DomainEventSubscriber({DomainEvent.class})
public final class StoreDomainEventOnOccurred {
    private final DomainEventStorer storer;

    public StoreDomainEventOnOccurred(DomainEventStorer storer) {
        this.storer = storer;
    }

    @EventListener
    public void on(DomainEvent event) {
        AnalyticsDomainEventId          id          = new AnalyticsDomainEventId(event.eventId());
        AnalyticsDomainEventAggregateId aggregateId = new AnalyticsDomainEventAggregateId(event.aggregateId());
        AnalyticsDomainEventName        name        = new AnalyticsDomainEventName(event.eventName());
        AnalyticsDomainEventBody        body        = new AnalyticsDomainEventBody(event.toPrimitives());

        storer.store(id, aggregateId, name, body);
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/analytics/main/tv/codely/analytics/domain_events/domain/AnalyticsDomainEvent.java`
```java
package tv.codely.analytics.domain_events.domain;

public final class AnalyticsDomainEvent {
    private final AnalyticsDomainEventId          id;
    private final AnalyticsDomainEventAggregateId aggregateId;
    private final AnalyticsDomainEventName        name;
    private final AnalyticsDomainEventBody        body;

    public AnalyticsDomainEvent(
        AnalyticsDomainEventId id,
        AnalyticsDomainEventAggregateId aggregateId,
        AnalyticsDomainEventName name,
        AnalyticsDomainEventBody body
    ) {

        this.id          = id;
        this.aggregateId = aggregateId;
        this.name        = name;
        this.body        = body;
    }

    public AnalyticsDomainEventId getId() {
        return id;
    }

    public AnalyticsDomainEventAggregateId getAggregateId() {
        return aggregateId;
    }

    public AnalyticsDomainEventName getName() {
        return name;
    }

    public AnalyticsDomainEventBody getBody() {
        return body;
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/analytics/main/tv/codely/analytics/domain_events/domain/AnalyticsDomainEventAggregateId.java`
```java
package tv.codely.analytics.domain_events.domain;

import tv.codely.shared.domain.Identifier;

public final class AnalyticsDomainEventAggregateId extends Identifier {
    public AnalyticsDomainEventAggregateId(String value) {
        super(value);
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/analytics/main/tv/codely/analytics/domain_events/domain/AnalyticsDomainEventBody.java`
```java
package tv.codely.analytics.domain_events.domain;

import java.io.Serializable;
import java.util.HashMap;

public final class AnalyticsDomainEventBody {
    private HashMap<String, Serializable> value;

    public HashMap<String, Serializable> getValue() {
        return value;
    }

    public AnalyticsDomainEventBody(HashMap<String, Serializable> value) {
        this.value = value;
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/analytics/main/tv/codely/analytics/domain_events/domain/AnalyticsDomainEventId.java`
```java
package tv.codely.analytics.domain_events.domain;

import tv.codely.shared.domain.Identifier;

public final class AnalyticsDomainEventId extends Identifier {
    public AnalyticsDomainEventId(String value) {
        super(value);
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/analytics/main/tv/codely/analytics/domain_events/domain/AnalyticsDomainEventName.java`
```java
package tv.codely.analytics.domain_events.domain;

import tv.codely.shared.domain.StringValueObject;

public final class AnalyticsDomainEventName extends StringValueObject {
    public AnalyticsDomainEventName(String value) {
        super(value);
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/analytics/main/tv/codely/analytics/domain_events/domain/DomainEventsRepository.java`
```java
package tv.codely.analytics.domain_events.domain;

public interface DomainEventsRepository {
    void save(AnalyticsDomainEvent event);
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/backoffice/build.gradle`
```
dependencies {
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/backoffice/main/resources/database/backoffice.sql`
```sql
CREATE TABLE IF NOT EXISTS `courses` (
    `id` CHAR(36) NOT NULL,
    `name` VARCHAR(255) NOT NULL,
    `duration` VARCHAR(255) NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/backoffice/main/resources/database/backoffice/backoffice_courses.json`
```json
{
  "mappings": {
    "courses": {
      "properties": {
        "id": {
          "type": "keyword",
          "index": true
        },
        "name": {
          "type": "text",
          "index": true,
          "fielddata": true
        },
        "duration": {
          "type": "text",
          "index": true,
          "fielddata": true
        }
      }
    }
  }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/backoffice/main/tv/codely/backoffice/auth/application/authenticate/AuthenticateUserCommand.java`
```java
package tv.codely.backoffice.auth.application.authenticate;

import tv.codely.shared.domain.bus.command.Command;

public final class AuthenticateUserCommand implements Command {
    private final String username;
    private final String password;

    public AuthenticateUserCommand(String username, String password) {
        this.username = username;
        this.password = password;
    }

    public String username() {
        return username;
    }

    public String password() {
        return password;
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/backoffice/main/tv/codely/backoffice/auth/application/authenticate/AuthenticateUserCommandHandler.java`
```java
package tv.codely.backoffice.auth.application.authenticate;

import tv.codely.backoffice.auth.domain.AuthPassword;
import tv.codely.backoffice.auth.domain.AuthUsername;
import tv.codely.shared.domain.Service;
import tv.codely.shared.domain.bus.command.CommandHandler;

@Service
public final class AuthenticateUserCommandHandler implements CommandHandler<AuthenticateUserCommand> {
    private final UserAuthenticator authenticator;

    public AuthenticateUserCommandHandler(UserAuthenticator authenticator) {
        this.authenticator = authenticator;
    }

    @Override
    public void handle(AuthenticateUserCommand command) {
        AuthUsername username = new AuthUsername(command.username());
        AuthPassword password = new AuthPassword(command.password());

        authenticator.authenticate(username, password);
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/backoffice/main/tv/codely/backoffice/auth/application/authenticate/UserAuthenticator.java`
```java
package tv.codely.backoffice.auth.application.authenticate;

import tv.codely.backoffice.auth.domain.*;
import tv.codely.shared.domain.Service;

import java.util.Optional;

@Service
public final class UserAuthenticator {
    private final AuthRepository repository;

    public UserAuthenticator(AuthRepository repository) {
        this.repository = repository;
    }

    public void authenticate(AuthUsername username, AuthPassword password) {
        Optional<AuthUser> auth = repository.search(username);

        ensureUserExist(auth, username);
        ensureCredentialsAreValid(auth.get(), password);
    }

    private void ensureUserExist(Optional<AuthUser> auth, AuthUsername username) {
        if (!auth.isPresent()) {
            throw new InvalidAuthUsername(username);
        }
    }

    private void ensureCredentialsAreValid(AuthUser auth, AuthPassword password) {
        if (!auth.passwordMatches(password)) {
            throw new InvalidAuthCredentials(auth.username());
        }
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/backoffice/main/tv/codely/backoffice/auth/domain/AuthPassword.java`
```java
package tv.codely.backoffice.auth.domain;

import tv.codely.shared.domain.StringValueObject;

public final class AuthPassword extends StringValueObject {
    public AuthPassword(String value) {
        super(value);
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/backoffice/main/tv/codely/backoffice/auth/domain/AuthRepository.java`
```java
package tv.codely.backoffice.auth.domain;

import java.util.Optional;

public interface AuthRepository {
    Optional<AuthUser> search(AuthUsername username);
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/backoffice/main/tv/codely/backoffice/auth/domain/AuthUser.java`
```java
package tv.codely.backoffice.auth.domain;

public final class AuthUser {
    private final AuthUsername username;
    private final AuthPassword password;

    public AuthUser(AuthUsername username, AuthPassword password) {
        this.username = username;
        this.password = password;
    }

    public AuthUsername username() {
        return username;
    }

    public boolean passwordMatches(AuthPassword password) {
        return this.password.equals(password);
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/backoffice/main/tv/codely/backoffice/auth/domain/AuthUsername.java`
```java
package tv.codely.backoffice.auth.domain;

import tv.codely.shared.domain.StringValueObject;

public final class AuthUsername extends StringValueObject {
    public AuthUsername(String value) {
        super(value);
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/backoffice/main/tv/codely/backoffice/auth/domain/InvalidAuthCredentials.java`
```java
package tv.codely.backoffice.auth.domain;

public final class InvalidAuthCredentials extends RuntimeException {
    public InvalidAuthCredentials(AuthUsername username) {
        super(String.format("The credentials for <%s> are invalid", username.value()));
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/backoffice/main/tv/codely/backoffice/auth/domain/InvalidAuthUsername.java`
```java
package tv.codely.backoffice.auth.domain;

public final class InvalidAuthUsername extends RuntimeException {
    public InvalidAuthUsername(AuthUsername username) {
        super(String.format("The user <%s> does not exist", username.value()));
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/backoffice/main/tv/codely/backoffice/auth/infrastructure/persistence/InMemoryAuthRepository.java`
```java
package tv.codely.backoffice.auth.infrastructure.persistence;

import tv.codely.backoffice.auth.domain.AuthPassword;
import tv.codely.backoffice.auth.domain.AuthRepository;
import tv.codely.backoffice.auth.domain.AuthUser;
import tv.codely.backoffice.auth.domain.AuthUsername;
import tv.codely.shared.domain.Service;

import java.util.HashMap;
import java.util.Optional;

@Service
public final class InMemoryAuthRepository implements AuthRepository {
    private final HashMap<AuthUsername, AuthPassword> users = new HashMap<AuthUsername, AuthPassword>() {{
        put(new AuthUsername("javi"), new AuthPassword("barbitas"));
        put(new AuthUsername("rafa"), new AuthPassword("pelazo"));
    }};

    @Override
    public Optional<AuthUser> search(AuthUsername username) {
        return users.containsKey(username)
            ? Optional.of(new AuthUser(username, users.get(username)))
            : Optional.empty();
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/backoffice/main/tv/codely/backoffice/courses/application/BackofficeCourseResponse.java`
```java
package tv.codely.backoffice.courses.application;

import tv.codely.backoffice.courses.domain.BackofficeCourse;
import tv.codely.shared.domain.bus.query.Response;

public final class BackofficeCourseResponse implements Response {
    private final String id;
    private final String name;
    private final String duration;

    public BackofficeCourseResponse(String id, String name, String duration) {
        this.id       = id;
        this.name     = name;
        this.duration = duration;
    }

    public static BackofficeCourseResponse fromAggregate(BackofficeCourse course) {
        return new BackofficeCourseResponse(course.id(), course.name(), course.duration());
    }

    public String id() {
        return id;
    }

    public String name() {
        return name;
    }

    public String duration() {
        return duration;
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/backoffice/main/tv/codely/backoffice/courses/application/BackofficeCoursesResponse.java`
```java
package tv.codely.backoffice.courses.application;

import tv.codely.shared.domain.bus.query.Response;

import java.util.List;

public final class BackofficeCoursesResponse implements Response {
    private final List<BackofficeCourseResponse> courses;

    public BackofficeCoursesResponse(List<BackofficeCourseResponse> courses) {
        this.courses = courses;
    }

    public List<BackofficeCourseResponse> courses() {
        return courses;
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/backoffice/main/tv/codely/backoffice/courses/application/create/BackofficeCourseCreator.java`
```java
package tv.codely.backoffice.courses.application.create;

import tv.codely.backoffice.courses.domain.BackofficeCourse;
import tv.codely.backoffice.courses.domain.BackofficeCourseRepository;
import tv.codely.shared.domain.Service;

@Service
public final class BackofficeCourseCreator {
    private final BackofficeCourseRepository repository;

    public BackofficeCourseCreator(BackofficeCourseRepository repository) {
        this.repository = repository;
    }

    public void create(String id, String name, String duration) {
        this.repository.save(new BackofficeCourse(id, name, duration));
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/backoffice/main/tv/codely/backoffice/courses/application/create/CreateBackofficeCourseOnCourseCreated.java`
```java
package tv.codely.backoffice.courses.application.create;

import org.springframework.context.event.EventListener;
import tv.codely.shared.domain.Service;
import tv.codely.shared.domain.bus.event.DomainEventSubscriber;
import tv.codely.shared.domain.course.CourseCreatedDomainEvent;

@Service
@DomainEventSubscriber({CourseCreatedDomainEvent.class})
public final class CreateBackofficeCourseOnCourseCreated {
    private final BackofficeCourseCreator creator;

    public CreateBackofficeCourseOnCourseCreated(BackofficeCourseCreator creator) {
        this.creator = creator;
    }

    @EventListener
    public void on(CourseCreatedDomainEvent event) {
        creator.create(event.aggregateId(), event.name(), event.duration());
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/backoffice/main/tv/codely/backoffice/courses/application/search_all/AllBackofficeCoursesSearcher.java`
```java
package tv.codely.backoffice.courses.application.search_all;

import tv.codely.backoffice.courses.application.BackofficeCourseResponse;
import tv.codely.backoffice.courses.application.BackofficeCoursesResponse;
import tv.codely.backoffice.courses.domain.BackofficeCourseRepository;
import tv.codely.shared.domain.Service;

import java.util.stream.Collectors;

@Service
public final class AllBackofficeCoursesSearcher {
    private final BackofficeCourseRepository repository;

    public AllBackofficeCoursesSearcher(BackofficeCourseRepository repository) {
        this.repository = repository;
    }

    public BackofficeCoursesResponse search() {
        return new BackofficeCoursesResponse(
            repository.searchAll().stream().map(BackofficeCourseResponse::fromAggregate).collect(Collectors.toList())
        );
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/backoffice/main/tv/codely/backoffice/courses/application/search_all/SearchAllBackofficeCoursesQuery.java`
```java
package tv.codely.backoffice.courses.application.search_all;

import tv.codely.shared.domain.bus.query.Query;

public final class SearchAllBackofficeCoursesQuery implements Query {
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/backoffice/main/tv/codely/backoffice/courses/application/search_all/SearchAllBackofficeCoursesQueryHandler.java`
```java
package tv.codely.backoffice.courses.application.search_all;

import tv.codely.backoffice.courses.application.BackofficeCoursesResponse;
import tv.codely.shared.domain.Service;
import tv.codely.shared.domain.bus.query.QueryHandler;

@Service
public final class SearchAllBackofficeCoursesQueryHandler implements QueryHandler<SearchAllBackofficeCoursesQuery, BackofficeCoursesResponse> {
    private final AllBackofficeCoursesSearcher searcher;

    public SearchAllBackofficeCoursesQueryHandler(AllBackofficeCoursesSearcher searcher) {
        this.searcher = searcher;
    }

    @Override
    public BackofficeCoursesResponse handle(SearchAllBackofficeCoursesQuery query) {
        return searcher.search();
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/backoffice/main/tv/codely/backoffice/courses/application/search_by_criteria/BackofficeCoursesByCriteriaSearcher.java`
```java
package tv.codely.backoffice.courses.application.search_by_criteria;

import tv.codely.backoffice.courses.application.BackofficeCourseResponse;
import tv.codely.backoffice.courses.application.BackofficeCoursesResponse;
import tv.codely.backoffice.courses.domain.BackofficeCourseRepository;
import tv.codely.shared.domain.Service;
import tv.codely.shared.domain.criteria.Criteria;
import tv.codely.shared.domain.criteria.Filters;
import tv.codely.shared.domain.criteria.Order;

import java.util.Optional;
import java.util.stream.Collectors;

@Service
public final class BackofficeCoursesByCriteriaSearcher {
    private final BackofficeCourseRepository repository;

    public BackofficeCoursesByCriteriaSearcher(BackofficeCourseRepository repository) {
        this.repository = repository;
    }

    public BackofficeCoursesResponse search(
        Filters filters,
        Order order,
        Optional<Integer> limit,
        Optional<Integer> offset
    ) {
        Criteria criteria = new Criteria(filters, order, limit, offset);

        return new BackofficeCoursesResponse(
            repository.matching(criteria)
                      .stream()
                      .map(BackofficeCourseResponse::fromAggregate)
                      .collect(Collectors.toList())
        );
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/backoffice/main/tv/codely/backoffice/courses/application/search_by_criteria/SearchBackofficeCoursesByCriteriaQuery.java`
```java
package tv.codely.backoffice.courses.application.search_by_criteria;

import tv.codely.shared.domain.bus.query.Query;

import java.util.HashMap;
import java.util.List;
import java.util.Optional;

public final class SearchBackofficeCoursesByCriteriaQuery implements Query {
    private final List<HashMap<String, String>> filters;
    private final Optional<String>              orderBy;
    private final Optional<String>              orderType;
    private final Optional<Integer>             limit;
    private final Optional<Integer>             offset;

    public SearchBackofficeCoursesByCriteriaQuery(
        List<HashMap<String, String>> filters,
        Optional<String> orderBy,
        Optional<String> orderType,
        Optional<Integer> limit,
        Optional<Integer> offset
    ) {
        this.filters   = filters;
        this.orderBy   = orderBy;
        this.orderType = orderType;
        this.limit     = limit;
        this.offset    = offset;
    }

    public List<HashMap<String, String>> filters() {
        return filters;
    }

    public Optional<String> orderBy() {
        return orderBy;
    }

    public Optional<String> orderType() {
        return orderType;
    }

    public Optional<Integer> limit() {
        return limit;
    }

    public Optional<Integer> offset() {
        return offset;
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/backoffice/main/tv/codely/backoffice/courses/application/search_by_criteria/SearchBackofficeCoursesByCriteriaQueryHandler.java`
```java
package tv.codely.backoffice.courses.application.search_by_criteria;

import tv.codely.backoffice.courses.application.BackofficeCoursesResponse;
import tv.codely.shared.domain.Service;
import tv.codely.shared.domain.bus.query.QueryHandler;
import tv.codely.shared.domain.criteria.Filters;
import tv.codely.shared.domain.criteria.Order;

@Service
public final class SearchBackofficeCoursesByCriteriaQueryHandler implements QueryHandler<SearchBackofficeCoursesByCriteriaQuery, BackofficeCoursesResponse> {
    private final BackofficeCoursesByCriteriaSearcher searcher;

    public SearchBackofficeCoursesByCriteriaQueryHandler(BackofficeCoursesByCriteriaSearcher searcher) {
        this.searcher = searcher;
    }

    @Override
    public BackofficeCoursesResponse handle(SearchBackofficeCoursesByCriteriaQuery query) {
        Filters filters = Filters.fromValues(query.filters());
        Order   order   = Order.fromValues(query.orderBy(), query.orderType());

        return searcher.search(filters, order, query.limit(), query.offset());
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/backoffice/main/tv/codely/backoffice/courses/domain/BackofficeCourse.java`
```java
package tv.codely.backoffice.courses.domain;

import java.io.Serializable;
import java.util.HashMap;
import java.util.Map;
import java.util.Objects;

public final class BackofficeCourse {
    private final String id;
    private final String name;
    private final String duration;

    public BackofficeCourse() {
        id       = null;
        name     = null;
        duration = null;
    }

    public BackofficeCourse(String id, String name, String duration) {
        this.id       = id;
        this.name     = name;
        this.duration = duration;
    }

    public static BackofficeCourse fromPrimitives(Map<String, Object> plainData) {
        return new BackofficeCourse(
            (String) plainData.get("id"),
            (String) plainData.get("name"),
            (String) plainData.get("duration")
        );
    }

    public String id() {
        return id;
    }

    public String name() {
        return name;
    }

    public String duration() {
        return duration;
    }

    public HashMap<String, Serializable> toPrimitives() {
        return new HashMap<String, Serializable>() {{
            put("id", id);
            put("name", name);
            put("duration", duration);
        }};
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) {
            return true;
        }
        if (o == null || getClass() != o.getClass()) {
            return false;
        }
        BackofficeCourse that = (BackofficeCourse) o;
        return id.equals(that.id) &&
               name.equals(that.name) &&
               duration.equals(that.duration);
    }

    @Override
    public int hashCode() {
        return Objects.hash(id, name, duration);
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/backoffice/main/tv/codely/backoffice/courses/domain/BackofficeCourseRepository.java`
```java
package tv.codely.backoffice.courses.domain;

import tv.codely.shared.domain.criteria.Criteria;

import java.util.List;

public interface BackofficeCourseRepository {
    void save(BackofficeCourse course);

    List<BackofficeCourse> searchAll();

    List<BackofficeCourse> matching(Criteria criteria);
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/backoffice/main/tv/codely/backoffice/courses/infrastructure/persistence/ElasticsearchBackofficeCourseRepository.java`
```java
package tv.codely.backoffice.courses.infrastructure.persistence;

import org.springframework.context.annotation.Primary;
import tv.codely.backoffice.courses.domain.BackofficeCourse;
import tv.codely.backoffice.courses.domain.BackofficeCourseRepository;
import tv.codely.shared.domain.Service;
import tv.codely.shared.domain.criteria.Criteria;
import tv.codely.shared.infrastructure.elasticsearch.ElasticsearchClient;
import tv.codely.shared.infrastructure.elasticsearch.ElasticsearchRepository;

import java.util.List;

@Primary
@Service
public final class ElasticsearchBackofficeCourseRepository extends ElasticsearchRepository<BackofficeCourse> implements BackofficeCourseRepository {
    public ElasticsearchBackofficeCourseRepository(ElasticsearchClient client) {
        super(client);
    }

    @Override
    public void save(BackofficeCourse course) {
        persist(course.id(), course.toPrimitives());
    }

    @Override
    public List<BackofficeCourse> searchAll() {
        return searchAllInElastic(BackofficeCourse::fromPrimitives);
    }

    @Override
    public List<BackofficeCourse> matching(Criteria criteria) {
        return searchByCriteria(criteria, BackofficeCourse::fromPrimitives);
    }

    @Override
    protected String moduleName() {
        return "courses";
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/backoffice/main/tv/codely/backoffice/courses/infrastructure/persistence/InMemoryCacheBackofficeCourseRepository.java`
```java
package tv.codely.backoffice.courses.infrastructure.persistence;

import tv.codely.backoffice.courses.domain.BackofficeCourse;
import tv.codely.backoffice.courses.domain.BackofficeCourseRepository;
import tv.codely.shared.domain.criteria.Criteria;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

public final class InMemoryCacheBackofficeCourseRepository implements BackofficeCourseRepository {
    private final BackofficeCourseRepository              repository;
    private       List<BackofficeCourse>                  courses         = new ArrayList<>();
    private       HashMap<String, List<BackofficeCourse>> matchingCourses = new HashMap<>();

    public InMemoryCacheBackofficeCourseRepository(BackofficeCourseRepository repository) {
        this.repository = repository;
    }

    @Override
    public void save(BackofficeCourse course) {
        repository.save(course);
    }

    @Override
    public List<BackofficeCourse> searchAll() {
        return courses.isEmpty() ? searchAndFillCache() : courses;
    }

    @Override
    public List<BackofficeCourse> matching(Criteria criteria) {
        return matchingCourses.containsKey(criteria.serialize())
            ? matchingCourses.get(criteria.serialize())
            : searchMatchingAndFillCache(criteria);
    }

    private List<BackofficeCourse> searchMatchingAndFillCache(Criteria criteria) {
        List<BackofficeCourse> courses = repository.matching(criteria);

        this.matchingCourses.put(criteria.serialize(), courses);

        return courses;
    }

    private List<BackofficeCourse> searchAndFillCache() {
        List<BackofficeCourse> courses = repository.searchAll();

        this.courses = courses;

        return courses;
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/backoffice/main/tv/codely/backoffice/courses/infrastructure/persistence/MySqlBackofficeCourseRepository.java`
```java
package tv.codely.backoffice.courses.infrastructure.persistence;

import org.hibernate.SessionFactory;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.transaction.annotation.Transactional;
import tv.codely.backoffice.courses.domain.BackofficeCourse;
import tv.codely.backoffice.courses.domain.BackofficeCourseRepository;
import tv.codely.shared.domain.Service;
import tv.codely.shared.domain.criteria.Criteria;
import tv.codely.shared.infrastructure.hibernate.HibernateRepository;

import java.util.List;

@Service
@Transactional("backoffice-transaction_manager")
public class MySqlBackofficeCourseRepository extends HibernateRepository<BackofficeCourse> implements BackofficeCourseRepository {
    public MySqlBackofficeCourseRepository(@Qualifier("backoffice-session_factory") SessionFactory sessionFactory) {
        super(sessionFactory, BackofficeCourse.class);
    }

    @Override
    public void save(BackofficeCourse course) {
        persist(course);
    }

    @Override
    public List<BackofficeCourse> searchAll() {
        return all();
    }

    @Override
    public List<BackofficeCourse> matching(Criteria criteria) {
        return byCriteria(criteria);
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/backoffice/main/tv/codely/backoffice/shared/infrastructure/persistence/BackofficeElasticsearchConfiguration.java`
```java
package tv.codely.backoffice.shared.infrastructure.persistence;

import org.apache.http.HttpHost;
import org.elasticsearch.client.Request;
import org.elasticsearch.client.RequestOptions;
import org.elasticsearch.client.RestClient;
import org.elasticsearch.client.RestHighLevelClient;
import org.elasticsearch.client.indices.GetIndexRequest;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.core.io.Resource;
import org.springframework.core.io.support.ResourcePatternResolver;
import tv.codely.shared.domain.Utils;
import tv.codely.shared.infrastructure.config.Parameter;
import tv.codely.shared.infrastructure.config.ParameterNotExist;
import tv.codely.shared.infrastructure.elasticsearch.ElasticsearchClient;

import java.io.IOException;
import java.util.Objects;
import java.util.Scanner;

@Configuration
public class BackofficeElasticsearchConfiguration {
    private final Parameter               config;
    private final ResourcePatternResolver resourceResolver;

    public BackofficeElasticsearchConfiguration(Parameter config, ResourcePatternResolver resourceResolver) {
        this.config           = config;
        this.resourceResolver = resourceResolver;
    }

    @Bean
    public ElasticsearchClient elasticsearchClient() throws ParameterNotExist, Exception {
		ElasticsearchClient client = new ElasticsearchClient(
			new RestHighLevelClient(
				RestClient.builder(
					new HttpHost(
						config.get("BACKOFFICE_ELASTICSEARCH_HOST"),
						config.getInt("BACKOFFICE_ELASTICSEARCH_PORT"),
						"http"
					)
				)
			),
			RestClient.builder(
				new HttpHost(
					config.get("BACKOFFICE_ELASTICSEARCH_HOST"),
					config.getInt("BACKOFFICE_ELASTICSEARCH_PORT"),
					"http"
				)).build(),
			config.get("BACKOFFICE_ELASTICSEARCH_INDEX_PREFIX")
		);

		Utils.retry(10, 10000, () -> {
            try {
                generateIndexIfNotExists(client, "backoffice");
            } catch (IOException e) {
                throw new RuntimeException(e);
            }
        });

        return client;
    }

    private void generateIndexIfNotExists(ElasticsearchClient client, String contextName) throws IOException {
        Resource[] jsonsIndexes = resourceResolver.getResources(
            String.format("classpath:database/%s/*.json", contextName)
        );

        for (Resource jsonIndex : jsonsIndexes) {
            String indexName = Objects.requireNonNull(jsonIndex.getFilename()).replace(".json", "");

            if (!indexExists(indexName, client)) {
                String indexBody = new Scanner(
                    jsonIndex.getInputStream(),
                    "UTF-8"
                ).useDelimiter("\\A").next();

                Request request = new Request("PUT", indexName);
                request.setJsonEntity(indexBody);

                client.lowLevelClient().performRequest(request);
            }
        }
    }

    private boolean indexExists(String indexName, ElasticsearchClient client) throws IOException {
        return client.highLevelClient().indices().exists(new GetIndexRequest(indexName), RequestOptions.DEFAULT);
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/backoffice/main/tv/codely/backoffice/shared/infrastructure/persistence/BackofficeHibernateConfiguration.java`
```java
package tv.codely.backoffice.shared.infrastructure.persistence;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.orm.hibernate5.LocalSessionFactoryBean;
import org.springframework.transaction.PlatformTransactionManager;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import tv.codely.shared.infrastructure.config.Parameter;
import tv.codely.shared.infrastructure.config.ParameterNotExist;
import tv.codely.shared.infrastructure.hibernate.HibernateConfigurationFactory;

import javax.sql.DataSource;
import java.io.IOException;

@Configuration
@EnableTransactionManagement
public class BackofficeHibernateConfiguration {
    private final HibernateConfigurationFactory factory;
    private final Parameter                     config;
    private final String                        CONTEXT_NAME = "backoffice";

    public BackofficeHibernateConfiguration(HibernateConfigurationFactory factory, Parameter config) {
        this.factory = factory;
        this.config  = config;
    }

    @Bean("backoffice-transaction_manager")
    public PlatformTransactionManager hibernateTransactionManager() throws IOException, ParameterNotExist {
        return factory.hibernateTransactionManager(sessionFactory());
    }

    @Bean("backoffice-session_factory")
    public LocalSessionFactoryBean sessionFactory() throws IOException, ParameterNotExist {
        return factory.sessionFactory(CONTEXT_NAME, dataSource());
    }

    @Bean("backoffice-data_source")
    public DataSource dataSource() throws IOException, ParameterNotExist {
        return factory.dataSource(
            config.get("BACKOFFICE_DATABASE_HOST"),
            config.getInt("BACKOFFICE_DATABASE_PORT"),
            config.get("BACKOFFICE_DATABASE_NAME"),
            config.get("BACKOFFICE_DATABASE_USER"),
            config.get("BACKOFFICE_DATABASE_PASSWORD")
        );
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/backoffice/main/tv/codely/backoffice/shared/infrastructure/persistence/BackofficeMySqlEventBusConfiguration.java`
```java
package tv.codely.backoffice.shared.infrastructure.persistence;

import org.hibernate.SessionFactory;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import tv.codely.shared.infrastructure.bus.event.DomainEventsInformation;
import tv.codely.shared.infrastructure.bus.event.mysql.MySqlDomainEventsConsumer;
import tv.codely.shared.infrastructure.bus.event.mysql.MySqlEventBus;
import tv.codely.shared.infrastructure.bus.event.spring.SpringApplicationEventBus;

@Configuration
public class BackofficeMySqlEventBusConfiguration {
    private final SessionFactory            sessionFactory;
    private final DomainEventsInformation   domainEventsInformation;
    private final SpringApplicationEventBus bus;

    public BackofficeMySqlEventBusConfiguration(
        @Qualifier("backoffice-session_factory") SessionFactory sessionFactory,
        DomainEventsInformation domainEventsInformation,
        SpringApplicationEventBus bus
    ) {
        this.sessionFactory          = sessionFactory;
        this.domainEventsInformation = domainEventsInformation;
        this.bus                     = bus;
    }

    @Bean
    public MySqlEventBus backofficeMysqlEventBus() {
        return new MySqlEventBus(sessionFactory);
    }

    @Bean
    public MySqlDomainEventsConsumer backofficeMySqlDomainEventsConsumer() {
        return new MySqlDomainEventsConsumer(sessionFactory, domainEventsInformation, bus);
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/backoffice/main/tv/codely/backoffice/shared/infrastructure/persistence/BackofficeRabbitMqEventBusConfiguration.java`
```java
package tv.codely.backoffice.shared.infrastructure.persistence;

import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import tv.codely.shared.infrastructure.bus.event.mysql.MySqlEventBus;
import tv.codely.shared.infrastructure.bus.event.rabbitmq.RabbitMqEventBus;
import tv.codely.shared.infrastructure.bus.event.rabbitmq.RabbitMqPublisher;

@Configuration
public class BackofficeRabbitMqEventBusConfiguration {
    private final RabbitMqPublisher publisher;
    private final MySqlEventBus     failoverPublisher;

    public BackofficeRabbitMqEventBusConfiguration(
        RabbitMqPublisher publisher,
        @Qualifier("backofficeMysqlEventBus") MySqlEventBus failoverPublisher
    ) {
        this.publisher         = publisher;
        this.failoverPublisher = failoverPublisher;
    }

    @Bean
    public RabbitMqEventBus backofficeRabbitMqEventBus() {
        return new RabbitMqEventBus(publisher, failoverPublisher);
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/backoffice/test/tv/codely/backoffice/BackofficeContextInfrastructureTestCase.java`
```java
package tv.codely.backoffice;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.ContextConfiguration;
import tv.codely.apps.backoffice.frontend.BackofficeFrontendApplication;
import tv.codely.backoffice.courses.ElasticsearchEnvironmentArranger;
import tv.codely.shared.infrastructure.InfrastructureTestCase;

import java.io.IOException;

@ContextConfiguration(classes = BackofficeFrontendApplication.class)
@SpringBootTest
public abstract class BackofficeContextInfrastructureTestCase extends InfrastructureTestCase {
    @Autowired
    private ElasticsearchEnvironmentArranger elasticsearchArranger;

    protected void clearElasticsearch() throws IOException {
        elasticsearchArranger.arrange("backoffice", "backoffice_courses");
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/backoffice/test/tv/codely/backoffice/auth/AuthModuleUnitTestCase.java`
```java
package tv.codely.backoffice.auth;

import org.junit.jupiter.api.BeforeEach;
import org.mockito.Mockito;
import tv.codely.backoffice.auth.domain.AuthRepository;
import tv.codely.backoffice.auth.domain.AuthUser;
import tv.codely.backoffice.auth.domain.AuthUsername;
import tv.codely.shared.infrastructure.UnitTestCase;

import java.util.Optional;

import static org.mockito.Mockito.mock;

public abstract class AuthModuleUnitTestCase extends UnitTestCase {
    protected AuthRepository repository;

    @BeforeEach
    protected void setUp() {
        super.setUp();

        repository = mock(AuthRepository.class);
    }

    public void shouldSearch(AuthUsername username, AuthUser user) {
        Mockito.when(repository.search(username)).thenReturn(Optional.of(user));
    }

    public void shouldSearch(AuthUsername username) {
        Mockito.when(repository.search(username)).thenReturn(Optional.empty());
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/backoffice/test/tv/codely/backoffice/auth/application/authenticate/AuthenticateUserCommandHandlerShould.java`
```java
package tv.codely.backoffice.auth.application.authenticate;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import tv.codely.backoffice.auth.AuthModuleUnitTestCase;
import tv.codely.backoffice.auth.domain.AuthUser;
import tv.codely.backoffice.auth.domain.AuthUserMother;
import tv.codely.backoffice.auth.domain.InvalidAuthCredentials;
import tv.codely.backoffice.auth.domain.InvalidAuthUsername;

import static org.junit.jupiter.api.Assertions.assertThrows;

final class AuthenticateUserCommandHandlerShould extends AuthModuleUnitTestCase {
    private AuthenticateUserCommandHandler handler;

    @BeforeEach
    protected void setUp() {
        super.setUp();

        handler = new AuthenticateUserCommandHandler(new UserAuthenticator(repository));
    }

    @Test
    void authenticate_a_valid_user() {
        AuthenticateUserCommand command  = AuthenticateUserCommandMother.random();
        AuthUser                authUser = AuthUserMother.fromCommand(command);

        shouldSearch(authUser.username(), authUser);

        handler.handle(command);
    }

    @Test
    void throw_an_exception_when_the_user_does_not_exist() {
        assertThrows(InvalidAuthUsername.class, () -> {
            AuthenticateUserCommand command  = AuthenticateUserCommandMother.random();
            AuthUser                authUser = AuthUserMother.fromCommand(command);

            shouldSearch(authUser.username());

            handler.handle(command);
        });
    }

    @Test
    void throw_an_exception_when_the_password_does_not_math() {
        assertThrows(InvalidAuthCredentials.class, () -> {
            AuthenticateUserCommand command  = AuthenticateUserCommandMother.random();
            AuthUser                authUser = AuthUserMother.withUsername(command.username());

            shouldSearch(authUser.username(), authUser);

            handler.handle(command);
        });
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/backoffice/test/tv/codely/backoffice/auth/application/authenticate/AuthenticateUserCommandMother.java`
```java
package tv.codely.backoffice.auth.application.authenticate;

import tv.codely.backoffice.auth.domain.AuthPassword;
import tv.codely.backoffice.auth.domain.AuthPasswordMother;
import tv.codely.backoffice.auth.domain.AuthUsername;
import tv.codely.backoffice.auth.domain.AuthUsernameMother;

public final class AuthenticateUserCommandMother {
    public static AuthenticateUserCommand create(AuthUsername username, AuthPassword password) {
        return new AuthenticateUserCommand(username.value(), password.value());
    }

    public static AuthenticateUserCommand random() {
        return create(AuthUsernameMother.random(), AuthPasswordMother.random());
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/backoffice/test/tv/codely/backoffice/auth/domain/AuthPasswordMother.java`
```java
package tv.codely.backoffice.auth.domain;

import tv.codely.shared.domain.WordMother;

public final class AuthPasswordMother {
    public static AuthPassword create(String value) {
        return new AuthPassword(value);
    }

    public static AuthPassword random() {
        return create(WordMother.random());
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/backoffice/test/tv/codely/backoffice/auth/domain/AuthUserMother.java`
```java
package tv.codely.backoffice.auth.domain;

import tv.codely.backoffice.auth.application.authenticate.AuthenticateUserCommand;

public final class AuthUserMother {
    public static AuthUser create(AuthUsername username, AuthPassword password) {
        return new AuthUser(username, password);
    }

    public static AuthUser random() {
        return create(AuthUsernameMother.random(), AuthPasswordMother.random());
    }

    public static AuthUser fromCommand(AuthenticateUserCommand command) {
        return create(AuthUsernameMother.create(command.username()), AuthPasswordMother.create(command.password()));
    }

    public static AuthUser withUsername(String username) {
        return create(AuthUsernameMother.create(username), AuthPasswordMother.random());
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/backoffice/test/tv/codely/backoffice/auth/domain/AuthUsernameMother.java`
```java
package tv.codely.backoffice.auth.domain;

import tv.codely.shared.domain.WordMother;

public final class AuthUsernameMother {
    public static AuthUsername create(String value) {
        return new AuthUsername(value);
    }

    public static AuthUsername random() {
        return create(WordMother.random());
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/backoffice/test/tv/codely/backoffice/courses/ElasticsearchEnvironmentArranger.java`
```java
package tv.codely.backoffice.courses;

import org.elasticsearch.client.Request;
import org.springframework.core.io.Resource;
import org.springframework.core.io.support.ResourcePatternResolver;
import tv.codely.shared.domain.Service;
import tv.codely.shared.infrastructure.elasticsearch.ElasticsearchClient;

import java.io.IOException;
import java.util.Objects;
import java.util.Scanner;

@Service
public final class ElasticsearchEnvironmentArranger {
    ResourcePatternResolver resourceResolver;
    ElasticsearchClient     client;

    public ElasticsearchEnvironmentArranger(
        ResourcePatternResolver resourceResolver,
        ElasticsearchClient client
    ) {
        this.resourceResolver = resourceResolver;
        this.client           = client;
    }

    public void arrange(String contextName, String index) throws IOException {
        client.delete(index);

        Resource[] jsonsIndexes = resourceResolver.getResources(
            String.format("classpath:database/%s/%s.json", contextName, index)
        );

        for (Resource jsonIndex : jsonsIndexes) {
            String indexName = Objects.requireNonNull(jsonIndex.getFilename()).replace(".json", "");

            String indexBody = new Scanner(
                jsonIndex.getInputStream(),
                "UTF-8"
            ).useDelimiter("\\A").next();

            Request request = new Request("PUT", indexName);
            request.setJsonEntity(indexBody);

            client.lowLevelClient().performRequest(request);
        }
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/backoffice/test/tv/codely/backoffice/courses/domain/BackofficeCourseCriteriaMother.java`
```java
package tv.codely.backoffice.courses.domain;

import tv.codely.shared.domain.criteria.Criteria;
import tv.codely.shared.domain.criteria.Filter;
import tv.codely.shared.domain.criteria.Filters;
import tv.codely.shared.domain.criteria.Order;

import java.util.Arrays;

public final class BackofficeCourseCriteriaMother {
    public static Criteria nameAndDurationContains(String name, String duration) {
        Filter nameFilter     = Filter.create("name", "contains", name);
        Filter durationFilter = Filter.create("duration", "contains", duration);

        return new Criteria(new Filters(Arrays.asList(nameFilter, durationFilter)), Order.asc("name"));
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/backoffice/test/tv/codely/backoffice/courses/domain/BackofficeCourseMother.java`
```java
package tv.codely.backoffice.courses.domain;

import tv.codely.shared.domain.UuidMother;
import tv.codely.shared.domain.WordMother;

public final class BackofficeCourseMother {
    public static BackofficeCourse create(String id, String name, String duration) {
        return new BackofficeCourse(id, name, duration);
    }

    public static BackofficeCourse create(String name, String duration) {
        return new BackofficeCourse(UuidMother.random(), name, duration);
    }

    public static BackofficeCourse random() {
        return create(UuidMother.random(), WordMother.random(), WordMother.random());
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/backoffice/test/tv/codely/backoffice/courses/infrastructure/persistence/ElasticsearchBackofficeCourseRepositoryShould.java`
```java
package tv.codely.backoffice.courses.infrastructure.persistence;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import tv.codely.backoffice.BackofficeContextInfrastructureTestCase;
import tv.codely.backoffice.courses.domain.BackofficeCourse;
import tv.codely.backoffice.courses.domain.BackofficeCourseCriteriaMother;
import tv.codely.backoffice.courses.domain.BackofficeCourseMother;
import tv.codely.shared.domain.criteria.Criteria;

import java.io.IOException;
import java.util.Arrays;
import java.util.List;

import static org.junit.jupiter.api.Assertions.assertEquals;

final class ElasticsearchBackofficeCourseRepositoryShould extends BackofficeContextInfrastructureTestCase {
    @Autowired
    private ElasticsearchBackofficeCourseRepository repository;

    @BeforeEach
    protected void setUp() throws IOException {
        clearElasticsearch();
    }

    @Test
    void save_a_course() {
        repository.save(BackofficeCourseMother.random());
    }

    @Test
    void search_all_existing_courses() throws Exception {
        BackofficeCourse course        = BackofficeCourseMother.random();
        BackofficeCourse anotherCourse = BackofficeCourseMother.random();

        List<BackofficeCourse> expected = Arrays.asList(course, anotherCourse);

        repository.save(course);
        repository.save(anotherCourse);

        eventually(() -> assertEquals(expected, repository.searchAll()));
    }

    @Test
    void search_courses_using_a_criteria() throws Exception {
        BackofficeCourse matchingCourse        = BackofficeCourseMother.create("DDD en Java", "3 days");
        BackofficeCourse anotherMatchingCourse = BackofficeCourseMother.create("DDD en TypeScript", "2.5 days");
        BackofficeCourse intellijCourse        = BackofficeCourseMother.create("Exprimiendo Intellij", "48 hours");
        BackofficeCourse cobolCourse           = BackofficeCourseMother.create("DDD en Cobol", "5 years");

        Criteria               criteria = BackofficeCourseCriteriaMother.nameAndDurationContains("DDD", "days");
        List<BackofficeCourse> expected = Arrays.asList(matchingCourse, anotherMatchingCourse);

        repository.save(matchingCourse);
        repository.save(anotherMatchingCourse);
        repository.save(intellijCourse);
        repository.save(cobolCourse);

        eventually(() -> assertEquals(expected, repository.matching(criteria)));
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/backoffice/test/tv/codely/backoffice/courses/infrastructure/persistence/InMemoryCacheBackofficeCourseRepositoryShould.java`
```java
package tv.codely.backoffice.courses.infrastructure.persistence;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.mockito.Mockito;
import tv.codely.backoffice.BackofficeContextInfrastructureTestCase;
import tv.codely.backoffice.courses.domain.BackofficeCourse;
import tv.codely.backoffice.courses.domain.BackofficeCourseCriteriaMother;
import tv.codely.backoffice.courses.domain.BackofficeCourseMother;
import tv.codely.backoffice.courses.domain.BackofficeCourseRepository;
import tv.codely.shared.domain.criteria.Criteria;

import java.util.Arrays;
import java.util.List;

import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.Matchers.containsInAnyOrder;
import static org.mockito.Mockito.*;

final class InMemoryCacheBackofficeCourseRepositoryShould extends BackofficeContextInfrastructureTestCase {
    private InMemoryCacheBackofficeCourseRepository repository;
    private BackofficeCourseRepository              innerRepository;

    @BeforeEach
    protected void setUp() {
        innerRepository = mock(BackofficeCourseRepository.class);
        repository      = new InMemoryCacheBackofficeCourseRepository(innerRepository);
    }

    @Test
    void save_a_course() {
        BackofficeCourse course = BackofficeCourseMother.random();

        repository.save(course);

        shouldHaveSaved(course);
    }

    @Test
    void search_all_existing_courses() {
        BackofficeCourse       course        = BackofficeCourseMother.random();
        BackofficeCourse       anotherCourse = BackofficeCourseMother.random();
        List<BackofficeCourse> courses       = Arrays.asList(course, anotherCourse);

        shouldSearchAll(courses);

        assertThat(courses, containsInAnyOrder(repository.searchAll().toArray()));
    }

    @Test
    void search_all_existing_courses_without_hitting_the_inner_repository_the_second_time() {
        BackofficeCourse       course        = BackofficeCourseMother.random();
        BackofficeCourse       anotherCourse = BackofficeCourseMother.random();
        List<BackofficeCourse> courses       = Arrays.asList(course, anotherCourse);

        shouldSearchAll(courses);

        assertThat(courses, containsInAnyOrder(repository.searchAll().toArray()));
        assertThat(courses, containsInAnyOrder(repository.searchAll().toArray()));
    }

    @Test
    void search_courses_using_a_criteria() {
        BackofficeCourse       matchingCourse        = BackofficeCourseMother.create("DDD en Java", "3 days");
        BackofficeCourse       anotherMatchingCourse = BackofficeCourseMother.create("DDD en TypeScript", "2.5 days");
        List<BackofficeCourse> matchingCourses       = Arrays.asList(matchingCourse, anotherMatchingCourse);

        Criteria criteria = BackofficeCourseCriteriaMother.nameAndDurationContains("DDD", "days");

        shouldSearchMatching(criteria, matchingCourses);

        assertThat(matchingCourses, containsInAnyOrder(repository.matching(criteria).toArray()));
    }

    @Test
    void search_courses_using_a_criteria_without_hitting_the_inner_repository_the_second_time() {
        BackofficeCourse       matchingCourse        = BackofficeCourseMother.create("DDD en Java", "3 days");
        BackofficeCourse       anotherMatchingCourse = BackofficeCourseMother.create("DDD en TypeScript", "2.5 days");
        List<BackofficeCourse> matchingCourses       = Arrays.asList(matchingCourse, anotherMatchingCourse);

        Criteria criteria = BackofficeCourseCriteriaMother.nameAndDurationContains("DDD", "days");

        shouldSearchMatching(criteria, matchingCourses);

        assertThat(matchingCourses, containsInAnyOrder(repository.matching(criteria).toArray()));
        assertThat(matchingCourses, containsInAnyOrder(repository.matching(criteria).toArray()));
    }

    private void shouldSearchAll(List<BackofficeCourse> courses) {
        Mockito.when(innerRepository.searchAll()).thenReturn(courses);
    }

    private void shouldSearchMatching(Criteria criteria, List<BackofficeCourse> courses) {
        Mockito.when(innerRepository.matching(criteria)).thenReturn(courses);
    }

    private void shouldHaveSaved(BackofficeCourse course) {
        verify(innerRepository, atLeastOnce()).save(course);
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/backoffice/test/tv/codely/backoffice/courses/infrastructure/persistence/MySqlBackofficeCourseRepositoryShould.java`
```java
package tv.codely.backoffice.courses.infrastructure.persistence;

import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import tv.codely.backoffice.BackofficeContextInfrastructureTestCase;
import tv.codely.backoffice.courses.domain.BackofficeCourse;
import tv.codely.backoffice.courses.domain.BackofficeCourseCriteriaMother;
import tv.codely.backoffice.courses.domain.BackofficeCourseMother;
import tv.codely.backoffice.courses.domain.BackofficeCourseRepository;
import tv.codely.shared.domain.criteria.Criteria;

import jakarta.transaction.Transactional;
import java.util.Arrays;

import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.Matchers.containsInAnyOrder;

@Transactional
class MySqlBackofficeCourseRepositoryShould extends BackofficeContextInfrastructureTestCase {
    @Autowired
    @Qualifier("mySqlBackofficeCourseRepository")
    private BackofficeCourseRepository repository;

    @Test
    void save_a_course() {
        repository.save(BackofficeCourseMother.random());
    }

    @Test
    void search_all_existing_courses() {
        BackofficeCourse course        = BackofficeCourseMother.random();
        BackofficeCourse anotherCourse = BackofficeCourseMother.random();

        repository.save(course);
        repository.save(anotherCourse);

        assertThat(Arrays.asList(course, anotherCourse), containsInAnyOrder(repository.searchAll().toArray()));
    }

    @Test
    void search_courses_using_a_criteria() {
        BackofficeCourse matchingCourse        = BackofficeCourseMother.create("DDD en Java", "3 days");
        BackofficeCourse anotherMatchingCourse = BackofficeCourseMother.create("DDD en TypeScript", "2.5 days");
        BackofficeCourse intellijCourse        = BackofficeCourseMother.create("Exprimiendo Intellij", "48 hours");
        BackofficeCourse cobolCourse           = BackofficeCourseMother.create("DDD en Cobol", "5 years");

        Criteria criteria = BackofficeCourseCriteriaMother.nameAndDurationContains("DDD", "days");

        repository.save(matchingCourse);
        repository.save(anotherMatchingCourse);
        repository.save(intellijCourse);
        repository.save(cobolCourse);

        assertThat(
            Arrays.asList(matchingCourse, anotherMatchingCourse),
            containsInAnyOrder(repository.matching(criteria).toArray())
        );
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/mooc/build.gradle`
```
dependencies {
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/mooc/main/resources/database/mooc.sql`
```sql
CREATE TABLE IF NOT EXISTS courses (
	id CHAR(36) NOT NULL,
	name VARCHAR(255) NOT NULL,
	duration VARCHAR(255) NOT NULL,
	PRIMARY KEY (id)
)
	ENGINE = InnoDB
	DEFAULT CHARSET = utf8mb4
	COLLATE = utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS courses_counter (
	id CHAR(36) NOT NULL,
	total INT NOT NULL,
	existing_courses JSON NOT NULL,
	PRIMARY KEY (id)
)
	ENGINE = InnoDB
	DEFAULT CHARSET = utf8mb4
	COLLATE = utf8mb4_unicode_ci;
INSERT IGNORE INTO courses_counter (id, total, existing_courses)
VALUES ('efbaff16-8fcd-4689-9fc9-ec545d641c46', 0, '[]');

CREATE TABLE IF NOT EXISTS steps (
	id CHAR(36) NOT NULL,
	title VARCHAR(155) NOT NULL,
	PRIMARY KEY (id)
)
	ENGINE = InnoDB
	DEFAULT CHARSET = utf8mb4
	COLLATE = utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS steps_challenges (
	id CHAR(36) NOT NULL,
	statement TEXT NOT NULL,
	PRIMARY KEY (id),
	CONSTRAINT fk_steps_challenges__step_id FOREIGN KEY (id) REFERENCES steps(id)
)
	ENGINE = InnoDB
	DEFAULT CHARSET = utf8mb4
	COLLATE = utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS steps_videos (
	id CHAR(36) NOT NULL,
	url VARCHAR(255) NOT NULL,
	text TEXT NOT NULL,
	PRIMARY KEY (id),
	CONSTRAINT fk_steps_video__step_id FOREIGN KEY (id) REFERENCES steps(id)
)
	ENGINE = InnoDB
	DEFAULT CHARSET = utf8mb4
	COLLATE = utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS domain_events (
	id CHAR(36) NOT NULL,
	aggregate_id CHAR(36) NOT NULL,
	name VARCHAR(255) NOT NULL,
	body JSON NOT NULL,
	occurred_on TIMESTAMP NOT NULL,
	PRIMARY KEY (id)
)
	ENGINE = InnoDB
	DEFAULT CHARSET = utf8mb4
	COLLATE = utf8mb4_unicode_ci;
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/mooc/main/tv/codely/mooc/courses/application/CourseResponse.java`
```java
package tv.codely.mooc.courses.application;

import tv.codely.mooc.courses.domain.Course;
import tv.codely.shared.domain.bus.query.Response;

public final class CourseResponse implements Response {
    private final String id;
    private final String name;
    private final String duration;

    public CourseResponse(String id, String name, String duration) {
        this.id       = id;
        this.name     = name;
        this.duration = duration;
    }

    public static CourseResponse fromAggregate(Course course) {
        return new CourseResponse(course.id().value(), course.name().value(), course.duration().value());
    }

    public String id() {
        return id;
    }

    public String name() {
        return name;
    }

    public String duration() {
        return duration;
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/mooc/main/tv/codely/mooc/courses/application/CoursesResponse.java`
```java
package tv.codely.mooc.courses.application;

import tv.codely.shared.domain.bus.query.Response;

import java.util.List;

public final class CoursesResponse implements Response {
    private final List<CourseResponse> courses;

    public CoursesResponse(List<CourseResponse> courses) {
        this.courses = courses;
    }

    public List<CourseResponse> courses() {
        return courses;
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/mooc/main/tv/codely/mooc/courses/application/create/CourseCreator.java`
```java
package tv.codely.mooc.courses.application.create;

import tv.codely.mooc.courses.domain.*;
import tv.codely.shared.domain.Service;
import tv.codely.shared.domain.bus.event.EventBus;

@Service
public final class CourseCreator {
    private final CourseRepository repository;
    private final EventBus         eventBus;

    public CourseCreator(CourseRepository repository, EventBus eventBus) {
        this.repository = repository;
        this.eventBus   = eventBus;
    }

    public void create(CourseId id, CourseName name, CourseDuration duration) {
        Course course = Course.create(id, name, duration);

        repository.save(course);
        eventBus.publish(course.pullDomainEvents());
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/mooc/main/tv/codely/mooc/courses/application/create/CreateCourseCommand.java`
```java
package tv.codely.mooc.courses.application.create;

import tv.codely.shared.domain.bus.command.Command;

public final class CreateCourseCommand implements Command {
    private final String id;
    private final String name;
    private final String duration;

    public CreateCourseCommand(String id, String name, String duration) {
        this.id       = id;
        this.name     = name;
        this.duration = duration;
    }

    public String id() {
        return id;
    }

    public String name() {
        return name;
    }

    public String duration() {
        return duration;
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/mooc/main/tv/codely/mooc/courses/application/create/CreateCourseCommandHandler.java`
```java
package tv.codely.mooc.courses.application.create;

import tv.codely.mooc.courses.domain.CourseDuration;
import tv.codely.mooc.courses.domain.CourseId;
import tv.codely.mooc.courses.domain.CourseName;
import tv.codely.shared.domain.Service;
import tv.codely.shared.domain.bus.command.CommandHandler;

@Service
public final class CreateCourseCommandHandler implements CommandHandler<CreateCourseCommand> {
    private final CourseCreator creator;

    public CreateCourseCommandHandler(CourseCreator creator) {
        this.creator = creator;
    }

    @Override
    public void handle(CreateCourseCommand command) {
        CourseId       id       = new CourseId(command.id());
        CourseName     name     = new CourseName(command.name());
        CourseDuration duration = new CourseDuration(command.duration());

        creator.create(id, name, duration);
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/mooc/main/tv/codely/mooc/courses/application/find/CourseFinder.java`
```java
package tv.codely.mooc.courses.application.find;

import tv.codely.mooc.courses.application.CourseResponse;
import tv.codely.mooc.courses.domain.CourseId;
import tv.codely.mooc.courses.domain.CourseNotExist;
import tv.codely.mooc.courses.domain.CourseRepository;
import tv.codely.shared.domain.Service;

@Service
public final class CourseFinder {
    private final CourseRepository repository;

    public CourseFinder(CourseRepository repository) {
        this.repository = repository;
    }

    public CourseResponse find(CourseId id) throws CourseNotExist {
        return repository.search(id)
                         .map(CourseResponse::fromAggregate)
                         .orElseThrow(() -> new CourseNotExist(id));
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/mooc/main/tv/codely/mooc/courses/application/find/FindCourseQuery.java`
```java
package tv.codely.mooc.courses.application.find;

import tv.codely.shared.domain.bus.query.Query;

public final class FindCourseQuery implements Query {
    private final String id;

    public FindCourseQuery(String id) {
        this.id = id;
    }

    public String id() {
        return id;
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/mooc/main/tv/codely/mooc/courses/application/find/FindCourseQueryHandler.java`
```java
package tv.codely.mooc.courses.application.find;

import tv.codely.mooc.courses.application.CourseResponse;
import tv.codely.mooc.courses.domain.CourseId;
import tv.codely.mooc.courses.domain.CourseNotExist;
import tv.codely.shared.domain.Service;
import tv.codely.shared.domain.bus.query.QueryHandler;

@Service
public final class FindCourseQueryHandler implements QueryHandler<FindCourseQuery, CourseResponse> {
    private final CourseFinder finder;

    public FindCourseQueryHandler(CourseFinder finder) {
        this.finder = finder;
    }

    @Override
    public CourseResponse handle(FindCourseQuery query) throws CourseNotExist {
        return finder.find(new CourseId(query.id()));
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/mooc/main/tv/codely/mooc/courses/application/search_last/LastCoursesSearcher.java`
```java
package tv.codely.mooc.courses.application.search_last;

import tv.codely.mooc.courses.application.CourseResponse;
import tv.codely.mooc.courses.application.CoursesResponse;
import tv.codely.mooc.courses.domain.CourseRepository;
import tv.codely.shared.domain.Service;
import tv.codely.shared.domain.criteria.Criteria;
import tv.codely.shared.domain.criteria.Filters;
import tv.codely.shared.domain.criteria.Order;

import java.util.Optional;
import java.util.stream.Collectors;

@Service
public final class LastCoursesSearcher {
    private final CourseRepository repository;

    public LastCoursesSearcher(CourseRepository repository) {
        this.repository = repository;
    }

    public CoursesResponse search(int courses) {
        Criteria criteria = new Criteria(
            Filters.none(),
            Order.none(),
            Optional.of(courses),
            Optional.empty()
        );

        return new CoursesResponse(
            repository.matching(criteria).stream().map(CourseResponse::fromAggregate).collect(Collectors.toList())
        );
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/mooc/main/tv/codely/mooc/courses/application/search_last/SearchLastCoursesQuery.java`
```java
package tv.codely.mooc.courses.application.search_last;

import tv.codely.shared.domain.bus.query.Query;

import java.util.Objects;

public final class SearchLastCoursesQuery implements Query {
    private final Integer total;

    public SearchLastCoursesQuery(Integer total) {
        this.total = total;
    }

    public Integer total() {
        return total;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) {
            return true;
        }
        if (o == null || getClass() != o.getClass()) {
            return false;
        }
        SearchLastCoursesQuery that = (SearchLastCoursesQuery) o;
        return total.equals(that.total);
    }

    @Override
    public int hashCode() {
        return Objects.hash(total);
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/mooc/main/tv/codely/mooc/courses/application/search_last/SearchLastCoursesQueryHandler.java`
```java
package tv.codely.mooc.courses.application.search_last;

import tv.codely.mooc.courses.application.CoursesResponse;
import tv.codely.shared.domain.Service;
import tv.codely.shared.domain.bus.query.QueryHandler;

@Service
public final class SearchLastCoursesQueryHandler implements QueryHandler<SearchLastCoursesQuery, CoursesResponse> {
    private final LastCoursesSearcher searcher;

    public SearchLastCoursesQueryHandler(LastCoursesSearcher searcher) {
        this.searcher = searcher;
    }

    @Override
    public CoursesResponse handle(SearchLastCoursesQuery query) {
        return searcher.search(query.total());
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/mooc/main/tv/codely/mooc/courses/domain/Course.java`
```java
package tv.codely.mooc.courses.domain;

import tv.codely.shared.domain.AggregateRoot;
import tv.codely.shared.domain.course.CourseCreatedDomainEvent;

import java.util.Objects;

public final class Course extends AggregateRoot {
    private final CourseId       id;
    private final CourseName     name;
    private final CourseDuration duration;

    public Course(CourseId id, CourseName name, CourseDuration duration) {
        this.id       = id;
        this.name     = name;
        this.duration = duration;
    }

    private Course() {
        id       = null;
        name     = null;
        duration = null;
    }

    public static Course create(CourseId id, CourseName name, CourseDuration duration) {
        Course course = new Course(id, name, duration);

        course.record(new CourseCreatedDomainEvent(id.value(), name.value(), duration.value()));

        return course;
    }

    public CourseId id() {
        return id;
    }

    public CourseName name() {
        return name;
    }

    public CourseDuration duration() {
        return duration;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) {
            return true;
        }
        if (o == null || getClass() != o.getClass()) {
            return false;
        }
        Course course = (Course) o;
        return id.equals(course.id) &&
               name.equals(course.name) &&
               duration.equals(course.duration);
    }

    @Override
    public int hashCode() {
        return Objects.hash(id, name, duration);
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/mooc/main/tv/codely/mooc/courses/domain/CourseDuration.java`
```java
package tv.codely.mooc.courses.domain;

import tv.codely.shared.domain.StringValueObject;

public final class CourseDuration extends StringValueObject {
    public CourseDuration(String value) {
        super(value);
    }

    private CourseDuration() {
        super("");
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/mooc/main/tv/codely/mooc/courses/domain/CourseId.java`
```java
package tv.codely.mooc.courses.domain;

import tv.codely.shared.domain.Identifier;

public final class CourseId extends Identifier {
    public CourseId(String value) {
        super(value);
    }

    public CourseId() {
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/mooc/main/tv/codely/mooc/courses/domain/CourseName.java`
```java
package tv.codely.mooc.courses.domain;

import tv.codely.shared.domain.StringValueObject;

public final class CourseName extends StringValueObject {
    public CourseName(String value) {
        super(value);
    }

    public CourseName() {
        super("");
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/mooc/main/tv/codely/mooc/courses/domain/CourseNotExist.java`
```java
package tv.codely.mooc.courses.domain;

import tv.codely.shared.domain.DomainError;

public final class CourseNotExist extends DomainError {
    public CourseNotExist(CourseId id) {
        super("course_not_exist", String.format("The course <%s> doesn't exist", id.value()));
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/mooc/main/tv/codely/mooc/courses/domain/CourseRepository.java`
```java
package tv.codely.mooc.courses.domain;

import tv.codely.shared.domain.criteria.Criteria;

import java.util.List;
import java.util.Optional;

public interface CourseRepository {
    void save(Course course);

    Optional<Course> search(CourseId id);

    List<Course> matching(Criteria criteria);
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/mooc/main/tv/codely/mooc/courses/infrastructure/persistence/InMemoryCourseRepository.java`
```java
package tv.codely.mooc.courses.infrastructure.persistence;

import tv.codely.mooc.courses.domain.Course;
import tv.codely.mooc.courses.domain.CourseId;
import tv.codely.mooc.courses.domain.CourseRepository;
import tv.codely.shared.domain.criteria.Criteria;

import java.util.HashMap;
import java.util.List;
import java.util.Optional;

public final class InMemoryCourseRepository implements CourseRepository {
    private HashMap<String, Course> courses = new HashMap<>();

    @Override
    public void save(Course course) {
        courses.put(course.id().value(), course);
    }

    public Optional<Course> search(CourseId id) {
        return Optional.ofNullable(courses.get(id.value()));
    }

    @Override
    public List<Course> matching(Criteria criteria) {
        return null;
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/mooc/main/tv/codely/mooc/courses/infrastructure/persistence/MySqlCourseRepository.java`
```java
package tv.codely.mooc.courses.infrastructure.persistence;

import org.hibernate.SessionFactory;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.transaction.annotation.Transactional;
import tv.codely.mooc.courses.domain.Course;
import tv.codely.mooc.courses.domain.CourseId;
import tv.codely.mooc.courses.domain.CourseRepository;
import tv.codely.shared.domain.Service;
import tv.codely.shared.domain.criteria.Criteria;
import tv.codely.shared.infrastructure.hibernate.HibernateRepository;

import java.util.List;
import java.util.Optional;

@Service
@Transactional("mooc-transaction_manager")
public class MySqlCourseRepository extends HibernateRepository<Course> implements CourseRepository {
    public MySqlCourseRepository(@Qualifier("mooc-session_factory") SessionFactory sessionFactory) {
        super(sessionFactory, Course.class);
    }

    @Override
    public void save(Course course) {
        persist(course);
    }

    @Override
    public Optional<Course> search(CourseId id) {
        return byId(id);
    }

    @Override
    public List<Course> matching(Criteria criteria) {
        return byCriteria(criteria);
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/mooc/main/tv/codely/mooc/courses_counter/application/find/CoursesCounterFinder.java`
```java
package tv.codely.mooc.courses_counter.application.find;

import tv.codely.mooc.courses_counter.domain.CoursesCounter;
import tv.codely.mooc.courses_counter.domain.CoursesCounterNotInitialized;
import tv.codely.mooc.courses_counter.domain.CoursesCounterRepository;
import tv.codely.shared.domain.Service;

@Service
public final class CoursesCounterFinder {
    private CoursesCounterRepository repository;

    public CoursesCounterFinder(CoursesCounterRepository repository) {
        this.repository = repository;
    }

    public CoursesCounterResponse find() {
        CoursesCounter coursesCounter = repository.search().orElseGet(() -> {
            throw new CoursesCounterNotInitialized();
        });

        return new CoursesCounterResponse(coursesCounter.total().value());
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/mooc/main/tv/codely/mooc/courses_counter/application/find/CoursesCounterResponse.java`
```java
package tv.codely.mooc.courses_counter.application.find;

import tv.codely.shared.domain.bus.query.Response;

import java.util.Objects;

public final class CoursesCounterResponse implements Response {
    private Integer total;

    public CoursesCounterResponse(Integer total) {
        this.total = total;
    }

    public Integer total() {
        return total;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) {
            return true;
        }
        if (o == null || getClass() != o.getClass()) {
            return false;
        }
        CoursesCounterResponse that = (CoursesCounterResponse) o;
        return total.equals(that.total);
    }

    @Override
    public int hashCode() {
        return Objects.hash(total);
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/mooc/main/tv/codely/mooc/courses_counter/application/find/FindCoursesCounterQuery.java`
```java
package tv.codely.mooc.courses_counter.application.find;

import tv.codely.shared.domain.bus.query.Query;

public final class FindCoursesCounterQuery implements Query {
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/mooc/main/tv/codely/mooc/courses_counter/application/find/FindCoursesCounterQueryHandler.java`
```java
package tv.codely.mooc.courses_counter.application.find;

import tv.codely.shared.domain.Service;
import tv.codely.shared.domain.bus.query.QueryHandler;

@Service
public final class FindCoursesCounterQueryHandler implements QueryHandler<FindCoursesCounterQuery, CoursesCounterResponse> {
    private final CoursesCounterFinder finder;

    public FindCoursesCounterQueryHandler(CoursesCounterFinder finder) {
        this.finder = finder;
    }

    @Override
    public CoursesCounterResponse handle(FindCoursesCounterQuery query) {
        return finder.find();
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/mooc/main/tv/codely/mooc/courses_counter/application/increment/CoursesCounterIncrementer.java`
```java
package tv.codely.mooc.courses_counter.application.increment;

import tv.codely.mooc.courses.domain.CourseId;
import tv.codely.mooc.courses_counter.domain.CoursesCounter;
import tv.codely.mooc.courses_counter.domain.CoursesCounterRepository;
import tv.codely.shared.domain.Service;
import tv.codely.shared.domain.UuidGenerator;

@Service
public final class CoursesCounterIncrementer {
    private CoursesCounterRepository repository;
    private UuidGenerator            uuidGenerator;

    public CoursesCounterIncrementer(CoursesCounterRepository repository, UuidGenerator uuidGenerator) {
        this.repository    = repository;
        this.uuidGenerator = uuidGenerator;
    }

    public void increment(CourseId id) {
        CoursesCounter counter = repository.search()
                                           .orElseGet(() -> CoursesCounter.initialize(uuidGenerator.generate()));

        if (!counter.hasIncremented(id)) {
            counter.increment(id);

            repository.save(counter);
        }
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/mooc/main/tv/codely/mooc/courses_counter/application/increment/IncrementCoursesCounterOnCourseCreated.java`
```java
package tv.codely.mooc.courses_counter.application.increment;

import org.springframework.context.event.EventListener;
import tv.codely.mooc.courses.domain.CourseId;
import tv.codely.shared.domain.Service;
import tv.codely.shared.domain.bus.event.DomainEventSubscriber;
import tv.codely.shared.domain.course.CourseCreatedDomainEvent;

@Service
@DomainEventSubscriber({CourseCreatedDomainEvent.class})
public final class IncrementCoursesCounterOnCourseCreated {
    private final CoursesCounterIncrementer incrementer;

    public IncrementCoursesCounterOnCourseCreated(CoursesCounterIncrementer incrementer) {
        this.incrementer = incrementer;
    }

    @EventListener
    public void on(CourseCreatedDomainEvent event) {
        CourseId courseId = new CourseId(event.aggregateId());

        incrementer.increment(courseId);
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/mooc/main/tv/codely/mooc/courses_counter/domain/CoursesCounter.java`
```java
package tv.codely.mooc.courses_counter.domain;

import tv.codely.mooc.courses.domain.CourseId;

import java.util.ArrayList;
import java.util.List;
import java.util.Objects;

public final class CoursesCounter {
    private CoursesCounterId    id;
    private CoursesCounterTotal total;
    private List<CourseId>      existingCourses;

    public CoursesCounter(CoursesCounterId id, CoursesCounterTotal total, List<CourseId> existingCourses) {
        this.id              = id;
        this.total           = total;
        this.existingCourses = existingCourses;
    }

    private CoursesCounter() {
        this.id              = null;
        this.total           = null;
        this.existingCourses = null;
    }

    public static CoursesCounter initialize(String id) {
        return new CoursesCounter(new CoursesCounterId(id), CoursesCounterTotal.initialize(), new ArrayList<>());
    }

    public CoursesCounterId id() {
        return id;
    }

    public CoursesCounterTotal total() {
        return total;
    }

    public List<CourseId> existingCourses() {
        return existingCourses;
    }

    public boolean hasIncremented(CourseId id) {
        return existingCourses.contains(id);
    }

    public void increment(CourseId id) {
        total = total.increment();
        existingCourses.add(id);
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) {
            return true;
        }
        if (o == null || getClass() != o.getClass()) {
            return false;
        }
        CoursesCounter that = (CoursesCounter) o;
        return id.equals(that.id) &&
               total.equals(that.total) &&
               existingCourses.equals(that.existingCourses);
    }

    @Override
    public int hashCode() {
        return Objects.hash(id, total, existingCourses);
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/mooc/main/tv/codely/mooc/courses_counter/domain/CoursesCounterId.java`
```java
package tv.codely.mooc.courses_counter.domain;

import tv.codely.shared.domain.Identifier;

public final class CoursesCounterId extends Identifier {
    public CoursesCounterId(String value) {
        super(value);
    }

    private CoursesCounterId() {
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/mooc/main/tv/codely/mooc/courses_counter/domain/CoursesCounterNotInitialized.java`
```java
package tv.codely.mooc.courses_counter.domain;

public final class CoursesCounterNotInitialized extends RuntimeException {
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/mooc/main/tv/codely/mooc/courses_counter/domain/CoursesCounterRepository.java`
```java
package tv.codely.mooc.courses_counter.domain;

import java.util.Optional;

public interface CoursesCounterRepository {
    void save(CoursesCounter counter);

    Optional<CoursesCounter> search();
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/mooc/main/tv/codely/mooc/courses_counter/domain/CoursesCounterTotal.java`
```java
package tv.codely.mooc.courses_counter.domain;

import tv.codely.shared.domain.IntValueObject;

public final class CoursesCounterTotal extends IntValueObject {
    public CoursesCounterTotal(Integer value) {
        super(value);
    }

    public CoursesCounterTotal() {
        super(null);
    }

    public static CoursesCounterTotal initialize() {
        return new CoursesCounterTotal(0);
    }

    public CoursesCounterTotal increment() {
        return new CoursesCounterTotal(value() + 1);
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/mooc/main/tv/codely/mooc/courses_counter/infrastructure/persistence/MySqlCoursesCounterRepository.java`
```java
package tv.codely.mooc.courses_counter.infrastructure.persistence;

import org.hibernate.SessionFactory;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.transaction.annotation.Transactional;
import tv.codely.mooc.courses_counter.domain.CoursesCounter;
import tv.codely.mooc.courses_counter.domain.CoursesCounterRepository;
import tv.codely.shared.domain.Service;
import tv.codely.shared.infrastructure.hibernate.HibernateRepository;

import java.util.List;
import java.util.Optional;

@Service
@Transactional("mooc-transaction_manager")
public class MySqlCoursesCounterRepository extends HibernateRepository<CoursesCounter> implements CoursesCounterRepository {
    public MySqlCoursesCounterRepository(@Qualifier("mooc-session_factory") SessionFactory sessionFactory) {
        super(sessionFactory, CoursesCounter.class);
    }

    @Override
    public void save(CoursesCounter counter) {
        persist(counter);
    }

    @Override
    public Optional<CoursesCounter> search() {
        List<CoursesCounter> coursesCounter = all();

        return 0 == coursesCounter.size() ? Optional.empty() : Optional.ofNullable(coursesCounter.get(0));
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/mooc/main/tv/codely/mooc/notifications/application/send_new_courses_newsletter/NewCoursesNewsletterSender.java`
```java
package tv.codely.mooc.notifications.application.send_new_courses_newsletter;

import tv.codely.mooc.courses.application.CoursesResponse;
import tv.codely.mooc.courses.application.search_last.SearchLastCoursesQuery;
import tv.codely.mooc.notifications.domain.EmailSender;
import tv.codely.mooc.notifications.domain.NewCoursesNewsletter;
import tv.codely.mooc.students.application.StudentResponse;
import tv.codely.mooc.students.application.StudentsResponse;
import tv.codely.mooc.students.application.search_all.SearchAllStudentsQuery;
import tv.codely.shared.domain.Service;
import tv.codely.shared.domain.UuidGenerator;
import tv.codely.shared.domain.bus.event.EventBus;
import tv.codely.shared.domain.bus.query.QueryBus;

@Service
public final class NewCoursesNewsletterSender {
    private final static Integer       TOTAL_COURSES = 3;
    private final        QueryBus      queryBus;
    private final        EmailSender   sender;
    private final        UuidGenerator uuidGenerator;
    private final        EventBus      eventBus;

    public NewCoursesNewsletterSender(
        QueryBus queryBus,
        UuidGenerator uuidGenerator,
        EmailSender sender,
        EventBus eventBus
    ) {
        this.queryBus      = queryBus;
        this.uuidGenerator = uuidGenerator;
        this.sender        = sender;
        this.eventBus      = eventBus;
    }

    public void send() {
        CoursesResponse courses = queryBus.ask(new SearchLastCoursesQuery(TOTAL_COURSES));

        if (courses.courses().size() > 0) {
            StudentsResponse students = queryBus.ask(new SearchAllStudentsQuery());

            students.students().forEach(student -> send(student, courses));
        }
    }

    public void send(StudentResponse student, CoursesResponse courses) {
        NewCoursesNewsletter newsletter = NewCoursesNewsletter.send(uuidGenerator.generate(), student, courses);

        sender.send(newsletter);

        eventBus.publish(newsletter.pullDomainEvents());
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/mooc/main/tv/codely/mooc/notifications/application/send_new_courses_newsletter/SendNewCoursesNewsletterCommand.java`
```java
package tv.codely.mooc.notifications.application.send_new_courses_newsletter;

import tv.codely.shared.domain.bus.command.Command;

public final class SendNewCoursesNewsletterCommand implements Command {
    private final String id;

    public SendNewCoursesNewsletterCommand(String id) {
        this.id = id;
    }

    public String id() {
        return id;
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/mooc/main/tv/codely/mooc/notifications/application/send_new_courses_newsletter/SendNewCoursesNewsletterCommandHandler.java`
```java
package tv.codely.mooc.notifications.application.send_new_courses_newsletter;

import tv.codely.shared.domain.Service;
import tv.codely.shared.domain.bus.command.CommandHandler;

@Service
public final class SendNewCoursesNewsletterCommandHandler implements CommandHandler<SendNewCoursesNewsletterCommand> {
    private final NewCoursesNewsletterSender sender;

    public SendNewCoursesNewsletterCommandHandler(NewCoursesNewsletterSender sender) {
        this.sender = sender;
    }

    @Override
    public void handle(SendNewCoursesNewsletterCommand command) {
        sender.send();
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/mooc/main/tv/codely/mooc/notifications/domain/Email.java`
```java
package tv.codely.mooc.notifications.domain;

import tv.codely.shared.domain.AggregateRoot;

import java.util.Objects;

public abstract class Email extends AggregateRoot {
    private final EmailId id;
    private final String  from;
    private final String  to;
    private final String  subject;
    private final String  body;

    public Email(EmailId id, String from, String to, String subject, String body) {
        this.id      = id;
        this.from    = from;
        this.to      = to;
        this.subject = subject;
        this.body    = body;
    }

    public EmailId id() {
        return id;
    }

    public String from() {
        return from;
    }

    public String to() {
        return to;
    }

    public String subject() {
        return subject;
    }

    public String body() {
        return body;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) {
            return true;
        }
        if (o == null || getClass() != o.getClass()) {
            return false;
        }
        Email email = (Email) o;
        return id.equals(email.id) &&
               from.equals(email.from) &&
               to.equals(email.to) &&
               subject.equals(email.subject) &&
               body.equals(email.body);
    }

    @Override
    public int hashCode() {
        return Objects.hash(id, from, to, subject, body);
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/mooc/main/tv/codely/mooc/notifications/domain/EmailId.java`
```java
package tv.codely.mooc.notifications.domain;

import tv.codely.shared.domain.Identifier;

public final class EmailId extends Identifier {
    public EmailId(String value) {
        super(value);
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/mooc/main/tv/codely/mooc/notifications/domain/EmailSender.java`
```java
package tv.codely.mooc.notifications.domain;

public interface EmailSender {
    void send(Email email);
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/mooc/main/tv/codely/mooc/notifications/domain/NewCoursesNewsletter.java`
```java
package tv.codely.mooc.notifications.domain;

import tv.codely.mooc.courses.application.CoursesResponse;
import tv.codely.mooc.students.application.StudentResponse;

import java.util.Objects;

public final class NewCoursesNewsletter extends Email {
    private final StudentResponse student;
    private final CoursesResponse courses;

    public NewCoursesNewsletter(EmailId id, StudentResponse student, CoursesResponse courses) {
        super(id, "news@codely.tv", student.email(), "Último cursos en CodelyTV", formatBody(student, courses));

        this.student = student;
        this.courses = courses;
    }

    private static String formatBody(StudentResponse student, CoursesResponse courses) {
        return String.format(
            "Hoy es tu día de suerte... %s vas a ver %s nuevos cursos",
            student.name(),
            courses.courses().size()
        );
    }

    public static NewCoursesNewsletter send(String id, StudentResponse student, CoursesResponse courses) {
        NewCoursesNewsletter newsletter = new NewCoursesNewsletter(new EmailId(id), student, courses);

        newsletter.record(new NewCoursesNewsletterEmailSent(id, student.id()));

        return newsletter;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) {
            return true;
        }
        if (o == null || getClass() != o.getClass()) {
            return false;
        }
        if (!super.equals(o)) {
            return false;
        }
        NewCoursesNewsletter that = (NewCoursesNewsletter) o;
        return student.equals(that.student) &&
               courses.equals(that.courses);
    }

    @Override
    public int hashCode() {
        return Objects.hash(super.hashCode(), student, courses);
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/mooc/main/tv/codely/mooc/notifications/domain/NewCoursesNewsletterEmailSent.java`
```java
package tv.codely.mooc.notifications.domain;

import tv.codely.shared.domain.bus.event.DomainEvent;

import java.io.Serializable;
import java.util.HashMap;
import java.util.Objects;

public final class NewCoursesNewsletterEmailSent extends DomainEvent {
    private final String studentId;

    public NewCoursesNewsletterEmailSent() {
        super(null);

        this.studentId = null;
    }

    public NewCoursesNewsletterEmailSent(String aggregateId, String studentId) {
        super(aggregateId);

        this.studentId = studentId;
    }

    public NewCoursesNewsletterEmailSent(
        String aggregateId,
        String eventId,
        String occurredOn,
        String studentId
    ) {
        super(aggregateId, eventId, occurredOn);

        this.studentId = studentId;
    }

    @Override
    public String eventName() {
        return "new_courses_newsletter_email.sent";
    }

    @Override
    public HashMap<String, Serializable> toPrimitives() {
        return new HashMap<String, Serializable>() {{
            put("student_id", studentId);
        }};
    }

    @Override
    public NewCoursesNewsletterEmailSent fromPrimitives(
        String aggregateId,
        HashMap<String, Serializable> body,
        String eventId,
        String occurredOn
    ) {
        return new NewCoursesNewsletterEmailSent(
            aggregateId,
            eventId,
            occurredOn,
            (String) body.get("student_id")
        );
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) {
            return true;
        }
        if (o == null || getClass() != o.getClass()) {
            return false;
        }
        NewCoursesNewsletterEmailSent that = (NewCoursesNewsletterEmailSent) o;
        return studentId.equals(that.studentId);
    }

    @Override
    public int hashCode() {
        return Objects.hash(studentId);
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/mooc/main/tv/codely/mooc/notifications/infrastructure/FakeEmailSender.java`
```java
package tv.codely.mooc.notifications.infrastructure;

import tv.codely.mooc.notifications.domain.Email;
import tv.codely.mooc.notifications.domain.EmailSender;
import tv.codely.shared.domain.Service;

@Service
public final class FakeEmailSender implements EmailSender {
    @Override
    public void send(Email email) {
        // In the future...
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/mooc/main/tv/codely/mooc/shared/infrastructure/persistence/MoocHibernateConfiguration.java`
```java
package tv.codely.mooc.shared.infrastructure.persistence;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.orm.hibernate5.LocalSessionFactoryBean;
import org.springframework.transaction.PlatformTransactionManager;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import tv.codely.shared.infrastructure.config.Parameter;
import tv.codely.shared.infrastructure.config.ParameterNotExist;
import tv.codely.shared.infrastructure.hibernate.HibernateConfigurationFactory;

import javax.sql.DataSource;
import java.io.IOException;

@Configuration
@EnableTransactionManagement
public class MoocHibernateConfiguration {
    private final HibernateConfigurationFactory factory;
    private final Parameter                     config;
    private final String                        CONTEXT_NAME = "mooc";

    public MoocHibernateConfiguration(HibernateConfigurationFactory factory, Parameter config) {
        this.factory = factory;
        this.config  = config;
    }

    @Bean("mooc-transaction_manager")
    public PlatformTransactionManager hibernateTransactionManager() throws IOException, ParameterNotExist {
        return factory.hibernateTransactionManager(sessionFactory());
    }

    @Bean("mooc-session_factory")
    public LocalSessionFactoryBean sessionFactory() throws IOException, ParameterNotExist {
        return factory.sessionFactory(CONTEXT_NAME, dataSource());
    }

    @Bean("mooc-data_source")
    public DataSource dataSource() throws IOException, ParameterNotExist {
        return factory.dataSource(
            config.get("MOOC_DATABASE_HOST"),
            config.getInt("MOOC_DATABASE_PORT"),
            config.get("MOOC_DATABASE_NAME"),
            config.get("MOOC_DATABASE_USER"),
            config.get("MOOC_DATABASE_PASSWORD")
        );
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/mooc/main/tv/codely/mooc/shared/infrastructure/persistence/MoocMySqlEventBusConfiguration.java`
```java
package tv.codely.mooc.shared.infrastructure.persistence;

import org.hibernate.SessionFactory;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import tv.codely.shared.infrastructure.bus.event.DomainEventsInformation;
import tv.codely.shared.infrastructure.bus.event.mysql.MySqlDomainEventsConsumer;
import tv.codely.shared.infrastructure.bus.event.mysql.MySqlEventBus;
import tv.codely.shared.infrastructure.bus.event.spring.SpringApplicationEventBus;

@Configuration
public class MoocMySqlEventBusConfiguration {
    private final SessionFactory            sessionFactory;
    private final DomainEventsInformation   domainEventsInformation;
    private final SpringApplicationEventBus bus;

    public MoocMySqlEventBusConfiguration(
        @Qualifier("mooc-session_factory") SessionFactory sessionFactory,
        DomainEventsInformation domainEventsInformation,
        SpringApplicationEventBus bus
    ) {
        this.sessionFactory          = sessionFactory;
        this.domainEventsInformation = domainEventsInformation;
        this.bus                     = bus;
    }

    @Bean
    public MySqlEventBus moocMysqlEventBus() {
        return new MySqlEventBus(sessionFactory);
    }

    @Bean
    public MySqlDomainEventsConsumer moocMySqlDomainEventsConsumer() {
        return new MySqlDomainEventsConsumer(sessionFactory, domainEventsInformation, bus);
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/mooc/main/tv/codely/mooc/shared/infrastructure/persistence/MoocRabbitMqEventBusConfiguration.java`
```java
package tv.codely.mooc.shared.infrastructure.persistence;

import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import tv.codely.shared.infrastructure.bus.event.mysql.MySqlEventBus;
import tv.codely.shared.infrastructure.bus.event.rabbitmq.RabbitMqEventBus;
import tv.codely.shared.infrastructure.bus.event.rabbitmq.RabbitMqPublisher;

@Configuration
public class MoocRabbitMqEventBusConfiguration {
    private final RabbitMqPublisher publisher;
    private final MySqlEventBus     failoverPublisher;

    public MoocRabbitMqEventBusConfiguration(
        RabbitMqPublisher publisher,
        @Qualifier("moocMysqlEventBus") MySqlEventBus failoverPublisher
    ) {
        this.publisher         = publisher;
        this.failoverPublisher = failoverPublisher;
    }

    @Bean
    public RabbitMqEventBus moocRabbitMqEventBus() {
        return new RabbitMqEventBus(publisher, failoverPublisher);
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/mooc/main/tv/codely/mooc/steps/domain/Step.java`
```java
package tv.codely.mooc.steps.domain;

import java.util.Objects;

public abstract class Step {
    private final StepId    id;
    private final StepTitle title;

    public Step(StepId id, StepTitle title) {
        this.id    = id;
        this.title = title;
    }

    public StepId id() {
        return id;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) {
            return true;
        }
        if (o == null || getClass() != o.getClass()) {
            return false;
        }
        Step step = (Step) o;
        return id.equals(step.id) &&
               title.equals(step.title);
    }

    @Override
    public int hashCode() {
        return Objects.hash(id, title);
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/mooc/main/tv/codely/mooc/steps/domain/StepId.java`
```java
package tv.codely.mooc.steps.domain;

import tv.codely.shared.domain.Identifier;

public final class StepId extends Identifier {
    public StepId(String value) {
        super(value);
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/mooc/main/tv/codely/mooc/steps/domain/StepRepository.java`
```java
package tv.codely.mooc.steps.domain;

import java.util.Optional;

public interface StepRepository {
    void save(Step step);

    Optional<? extends Step> search(StepId id);
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/mooc/main/tv/codely/mooc/steps/domain/StepTitle.java`
```java
package tv.codely.mooc.steps.domain;

import tv.codely.shared.domain.StringValueObject;

public final class StepTitle extends StringValueObject {
    public StepTitle(String value) {
        super(value);
    }

    private StepTitle() {
        super(null);
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/mooc/main/tv/codely/mooc/steps/domain/challenge/ChallengeStep.java`
```java
package tv.codely.mooc.steps.domain.challenge;

import tv.codely.mooc.steps.domain.Step;
import tv.codely.mooc.steps.domain.StepId;
import tv.codely.mooc.steps.domain.StepTitle;

import java.util.Objects;

public final class ChallengeStep extends Step {
    private final ChallengeStepStatement statement;

    public ChallengeStep(StepId id, StepTitle title, ChallengeStepStatement statement) {
        super(id, title);

        this.statement = statement;
    }

    private ChallengeStep() {
        super(null, null);

        this.statement = null;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) {
            return true;
        }
        if (o == null || getClass() != o.getClass()) {
            return false;
        }
        if (!super.equals(o)) {
            return false;
        }
        ChallengeStep that = (ChallengeStep) o;
        return statement.equals(that.statement);
    }

    @Override
    public int hashCode() {
        return Objects.hash(super.hashCode(), statement);
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/mooc/main/tv/codely/mooc/steps/domain/challenge/ChallengeStepStatement.java`
```java
package tv.codely.mooc.steps.domain.challenge;

import tv.codely.shared.domain.StringValueObject;

public final class ChallengeStepStatement extends StringValueObject {
    public ChallengeStepStatement(String value) {
        super(value);
    }

    public ChallengeStepStatement() {
        super(null);
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/mooc/main/tv/codely/mooc/steps/domain/video/VideoStep.java`
```java
package tv.codely.mooc.steps.domain.video;

import tv.codely.mooc.steps.domain.Step;
import tv.codely.mooc.steps.domain.StepId;
import tv.codely.mooc.steps.domain.StepTitle;
import tv.codely.shared.domain.VideoUrl;

public final class VideoStep extends Step {
    private final VideoUrl      videoUrl;
    private final VideoStepText text;

    public VideoStep(StepId id, StepTitle title, VideoUrl videoUrl, VideoStepText text) {
        super(id, title);

        this.videoUrl = videoUrl;
        this.text     = text;
    }

    private VideoStep() {
        super(null, null);

        this.videoUrl = null;
        this.text     = null;
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/mooc/main/tv/codely/mooc/steps/domain/video/VideoStepText.java`
```java
package tv.codely.mooc.steps.domain.video;

import tv.codely.shared.domain.StringValueObject;

public final class VideoStepText extends StringValueObject {
    public VideoStepText(String value) {
        super(value);
    }

    private VideoStepText() {
        super(null);
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/mooc/main/tv/codely/mooc/steps/infrastructure/persistence/MySqlStepRepository.java`
```java
package tv.codely.mooc.steps.infrastructure.persistence;

import org.hibernate.SessionFactory;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.transaction.annotation.Transactional;
import tv.codely.mooc.steps.domain.Step;
import tv.codely.mooc.steps.domain.StepId;
import tv.codely.mooc.steps.domain.StepRepository;
import tv.codely.shared.domain.Service;
import tv.codely.shared.infrastructure.hibernate.HibernateRepository;

import java.util.Optional;

@Service
@Transactional("mooc-transaction_manager")
public class MySqlStepRepository extends HibernateRepository<Step> implements StepRepository {
    public MySqlStepRepository(@Qualifier("mooc-session_factory") SessionFactory sessionFactory) {
        super(sessionFactory, Step.class);
    }

    @Override
    public void save(Step step) {
        persist(step);
    }

    @Override
    public Optional<? extends Step> search(StepId id) {
        return byId(id);
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/mooc/main/tv/codely/mooc/students/application/StudentResponse.java`
```java
package tv.codely.mooc.students.application;

import tv.codely.mooc.students.domain.Student;
import tv.codely.shared.domain.bus.query.Response;

public final class StudentResponse implements Response {
    private final String id;
    private final String name;
    private final String surname;
    private final String email;

    public StudentResponse(String id, String name, String surname, String email) {
        this.id      = id;
        this.name    = name;
        this.surname = surname;
        this.email   = email;
    }

    public static StudentResponse fromAggregate(Student student) {
        return new StudentResponse(student.id().value(), student.name(), student.surname(), student.email());
    }

    public String id() {
        return id;
    }

    public String name() {
        return name;
    }

    public String surname() {
        return surname;
    }

    public String email() {
        return email;
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/mooc/main/tv/codely/mooc/students/application/StudentsResponse.java`
```java
package tv.codely.mooc.students.application;

import tv.codely.shared.domain.bus.query.Response;

import java.util.List;

public final class StudentsResponse implements Response {
    private final List<StudentResponse> students;

    public StudentsResponse(List<StudentResponse> students) {
        this.students = students;
    }

    public List<StudentResponse> students() {
        return students;
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/mooc/main/tv/codely/mooc/students/application/search_all/AllStudentsSearcher.java`
```java
package tv.codely.mooc.students.application.search_all;

import tv.codely.mooc.students.application.StudentResponse;
import tv.codely.mooc.students.application.StudentsResponse;
import tv.codely.mooc.students.domain.StudentRepository;
import tv.codely.shared.domain.Service;

import java.util.stream.Collectors;

@Service
public final class AllStudentsSearcher {
    private final StudentRepository repository;

    public AllStudentsSearcher(StudentRepository repository) {
        this.repository = repository;
    }

    public StudentsResponse search() {
        return new StudentsResponse(
            repository.searchAll().stream().map(StudentResponse::fromAggregate).collect(Collectors.toList())
        );
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/mooc/main/tv/codely/mooc/students/application/search_all/SearchAllStudentsQuery.java`
```java
package tv.codely.mooc.students.application.search_all;

import tv.codely.shared.domain.bus.query.Query;

import java.util.Objects;

public final class SearchAllStudentsQuery implements Query {
    @Override
    public boolean equals(Object o) {
        if (this == o) {
            return true;
        }
        return o != null && getClass() == o.getClass();
    }

    @Override
    public int hashCode() {
        return Objects.hash("SearchAllStudentsQuery");
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/mooc/main/tv/codely/mooc/students/application/search_all/SearchAllStudentsQueryHandler.java`
```java
package tv.codely.mooc.students.application.search_all;

import tv.codely.mooc.students.application.StudentsResponse;
import tv.codely.shared.domain.Service;
import tv.codely.shared.domain.bus.query.QueryHandler;

@Service
public final class SearchAllStudentsQueryHandler implements QueryHandler<SearchAllStudentsQuery, StudentsResponse> {
    private final AllStudentsSearcher searcher;

    public SearchAllStudentsQueryHandler(AllStudentsSearcher searcher) {
        this.searcher = searcher;
    }

    @Override
    public StudentsResponse handle(SearchAllStudentsQuery query) {
        return searcher.search();
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/mooc/main/tv/codely/mooc/students/domain/Student.java`
```java
package tv.codely.mooc.students.domain;

public final class Student {
    private final StudentId id;
    private final String    name;
    private final String    surname;
    private final String    email;

    public Student(StudentId id, String name, String surname, String email) {
        this.id      = id;
        this.name    = name;
        this.surname = surname;
        this.email   = email;
    }

    public StudentId id() {
        return id;
    }

    public String name() {
        return name;
    }

    public String surname() {
        return surname;
    }

    public String email() {
        return email;
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/mooc/main/tv/codely/mooc/students/domain/StudentId.java`
```java
package tv.codely.mooc.students.domain;

import tv.codely.shared.domain.Identifier;

public final class StudentId extends Identifier {
    public StudentId(String value) {
        super(value);
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/mooc/main/tv/codely/mooc/students/domain/StudentRepository.java`
```java
package tv.codely.mooc.students.domain;

import java.util.List;

public interface StudentRepository {
    List<Student> searchAll();
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/mooc/main/tv/codely/mooc/students/infrastructure/InMemoryStudentRepository.java`
```java
package tv.codely.mooc.students.infrastructure;

import tv.codely.mooc.students.domain.Student;
import tv.codely.mooc.students.domain.StudentId;
import tv.codely.mooc.students.domain.StudentRepository;
import tv.codely.shared.domain.Service;
import tv.codely.shared.domain.UuidGenerator;

import java.util.Arrays;
import java.util.List;

@Service
public final class InMemoryStudentRepository implements StudentRepository {
    private UuidGenerator generator;

    public InMemoryStudentRepository(UuidGenerator generator) {
        this.generator = generator;
    }

    @Override
    public List<Student> searchAll() {
        return Arrays.asList(
            new Student(new StudentId(generator.generate()), "name", "surname", "email@mail.com"),
            new Student(new StudentId(generator.generate()), "Other name", "Other surname", "another@mail.com")
        );
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/mooc/test/tv/codely/mooc/MoocContextInfrastructureTestCase.java`
```java
package tv.codely.mooc;

import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.ContextConfiguration;
import tv.codely.apps.mooc.backend.MoocBackendApplication;
import tv.codely.shared.infrastructure.InfrastructureTestCase;

@ContextConfiguration(classes = MoocBackendApplication.class)
@SpringBootTest
public abstract class MoocContextInfrastructureTestCase extends InfrastructureTestCase {
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/mooc/test/tv/codely/mooc/courses/CoursesModuleInfrastructureTestCase.java`
```java
package tv.codely.mooc.courses;

import org.springframework.beans.factory.annotation.Autowired;
import tv.codely.mooc.MoocContextInfrastructureTestCase;
import tv.codely.mooc.courses.domain.CourseRepository;
import tv.codely.mooc.courses.infrastructure.persistence.InMemoryCourseRepository;

public abstract class CoursesModuleInfrastructureTestCase extends MoocContextInfrastructureTestCase {
    protected InMemoryCourseRepository inMemoryCourseRepository = new InMemoryCourseRepository();
    @Autowired
    protected CourseRepository         mySqlCourseRepository;
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/mooc/test/tv/codely/mooc/courses/CoursesModuleUnitTestCase.java`
```java
package tv.codely.mooc.courses;

import org.junit.jupiter.api.BeforeEach;
import tv.codely.mooc.courses.domain.Course;
import tv.codely.mooc.courses.domain.CourseRepository;
import tv.codely.shared.infrastructure.UnitTestCase;

import static org.mockito.Mockito.*;

public abstract class CoursesModuleUnitTestCase extends UnitTestCase {
    protected CourseRepository repository;

    @BeforeEach
    protected void setUp() {
        super.setUp();

        repository = mock(CourseRepository.class);
    }

    public void shouldHaveSaved(Course course) {
        verify(repository, atLeastOnce()).save(course);
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/mooc/test/tv/codely/mooc/courses/application/CourseResponseMother.java`
```java
package tv.codely.mooc.courses.application;

import tv.codely.mooc.courses.domain.*;

public final class CourseResponseMother {
    public static CourseResponse create(CourseId id, CourseName name, CourseDuration duration) {
        return new CourseResponse(id.value(), name.value(), duration.value());
    }

    public static CourseResponse random() {
        return create(CourseIdMother.random(), CourseNameMother.random(), CourseDurationMother.random());
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/mooc/test/tv/codely/mooc/courses/application/CoursesResponseMother.java`
```java
package tv.codely.mooc.courses.application;

import tv.codely.shared.domain.ListMother;

import java.util.Collections;
import java.util.List;

public final class CoursesResponseMother {
    public static CoursesResponse create(List<CourseResponse> courses) {
        return new CoursesResponse(courses);
    }

    public static CoursesResponse random() {
        return create(ListMother.random(CourseResponseMother::random));
    }

    public static CoursesResponse times(int times) {
        return create(ListMother.create(times, CourseResponseMother::random));
    }

    public static CoursesResponse empty() {
        return create(Collections.emptyList());
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/mooc/test/tv/codely/mooc/courses/application/create/CreateCourseCommandHandlerShould.java`
```java
package tv.codely.mooc.courses.application.create;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import tv.codely.mooc.courses.CoursesModuleUnitTestCase;
import tv.codely.mooc.courses.domain.Course;
import tv.codely.mooc.courses.domain.CourseCreatedDomainEventMother;
import tv.codely.mooc.courses.domain.CourseMother;
import tv.codely.shared.domain.course.CourseCreatedDomainEvent;

final class CreateCourseCommandHandlerShould extends CoursesModuleUnitTestCase {
    private CreateCourseCommandHandler handler;

    @BeforeEach
    protected void setUp() {
        super.setUp();

        handler = new CreateCourseCommandHandler(new CourseCreator(repository, eventBus));
    }

    @Test
    void create_a_valid_course() {
        CreateCourseCommand command = CreateCourseCommandMother.random();

        Course                   course      = CourseMother.fromRequest(command);
        CourseCreatedDomainEvent domainEvent = CourseCreatedDomainEventMother.fromCourse(course);

        handler.handle(command);

        shouldHaveSaved(course);
        shouldHavePublished(domainEvent);
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/mooc/test/tv/codely/mooc/courses/application/create/CreateCourseCommandMother.java`
```java
package tv.codely.mooc.courses.application.create;

import tv.codely.mooc.courses.domain.*;

public final class CreateCourseCommandMother {
    public static CreateCourseCommand create(CourseId id, CourseName name, CourseDuration duration) {
        return new CreateCourseCommand(id.value(), name.value(), duration.value());
    }

    public static CreateCourseCommand random() {
        return create(CourseIdMother.random(), CourseNameMother.random(), CourseDurationMother.random());
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/mooc/test/tv/codely/mooc/courses/application/search_last/SearchLastCoursesQueryMother.java`
```java
package tv.codely.mooc.courses.application.search_last;

import tv.codely.shared.domain.IntegerMother;

public final class SearchLastCoursesQueryMother {
    public static SearchLastCoursesQuery create(Integer total) {
        return new SearchLastCoursesQuery(total);
    }

    public static SearchLastCoursesQuery random() {
        return create(IntegerMother.random());
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/mooc/test/tv/codely/mooc/courses/domain/CourseCreatedDomainEventMother.java`
```java
package tv.codely.mooc.courses.domain;

import tv.codely.shared.domain.course.CourseCreatedDomainEvent;

public final class CourseCreatedDomainEventMother {
    public static CourseCreatedDomainEvent create(CourseId id, CourseName name, CourseDuration duration) {
        return new CourseCreatedDomainEvent(id.value(), name.value(), duration.value());
    }

    public static CourseCreatedDomainEvent fromCourse(Course course) {
        return create(course.id(), course.name(), course.duration());
    }

    public static CourseCreatedDomainEvent random() {
        return create(CourseIdMother.random(), CourseNameMother.random(), CourseDurationMother.random());
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/mooc/test/tv/codely/mooc/courses/domain/CourseDurationMother.java`
```java
package tv.codely.mooc.courses.domain;

import tv.codely.shared.domain.IntegerMother;
import tv.codely.shared.domain.RandomElementPicker;

public final class CourseDurationMother {
    public static CourseDuration create(String value) {
        return new CourseDuration(value);
    }

    public static CourseDuration random() {
        return create(
            String.format(
                "%s %s",
                IntegerMother.random(),
                RandomElementPicker.from("months", "years", "days", "hours", "minutes", "seconds")
            )
        );
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/mooc/test/tv/codely/mooc/courses/domain/CourseIdMother.java`
```java
package tv.codely.mooc.courses.domain;

import tv.codely.shared.domain.UuidMother;

public final class CourseIdMother {
    public static CourseId create(String value) {
        return new CourseId(value);
    }

    public static CourseId random() {
        return create(UuidMother.random());
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/mooc/test/tv/codely/mooc/courses/domain/CourseMother.java`
```java
package tv.codely.mooc.courses.domain;

import tv.codely.mooc.courses.application.create.CreateCourseCommand;

public final class CourseMother {
    public static Course create(CourseId id, CourseName name, CourseDuration duration) {
        return new Course(id, name, duration);
    }

    public static Course fromRequest(CreateCourseCommand request) {
        return create(
            CourseIdMother.create(request.id()),
            CourseNameMother.create(request.name()),
            CourseDurationMother.create(request.duration())
        );
    }

    public static Course random() {
        return create(CourseIdMother.random(), CourseNameMother.random(), CourseDurationMother.random());
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/mooc/test/tv/codely/mooc/courses/domain/CourseNameMother.java`
```java
package tv.codely.mooc.courses.domain;

import tv.codely.shared.domain.WordMother;

public final class CourseNameMother {
    public static CourseName create(String value) {
        return new CourseName(value);
    }

    public static CourseName random() {
        return create(WordMother.random());
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/mooc/test/tv/codely/mooc/courses/infrastructure/persistence/InMemoryCourseRepositoryShould.java`
```java
package tv.codely.mooc.courses.infrastructure.persistence;

import org.junit.jupiter.api.Test;
import tv.codely.mooc.courses.CoursesModuleInfrastructureTestCase;
import tv.codely.mooc.courses.domain.Course;
import tv.codely.mooc.courses.domain.CourseIdMother;
import tv.codely.mooc.courses.domain.CourseMother;

import java.util.Optional;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertFalse;

final class InMemoryCourseRepositoryShould extends CoursesModuleInfrastructureTestCase {
    @Test
    void save_a_course() {
        Course course = CourseMother.random();

        inMemoryCourseRepository.save(course);
    }

    @Test
    void return_an_existing_course() {
        Course course = CourseMother.random();

        inMemoryCourseRepository.save(course);

        assertEquals(Optional.of(course), inMemoryCourseRepository.search(course.id()));
    }

    @Test
    void not_return_a_non_existing_course() {
        assertFalse(inMemoryCourseRepository.search(CourseIdMother.random()).isPresent());
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/mooc/test/tv/codely/mooc/courses/infrastructure/persistence/MySqlCourseRepositoryShould.java`
```java
package tv.codely.mooc.courses.infrastructure.persistence;

import org.junit.jupiter.api.Test;
import tv.codely.mooc.courses.CoursesModuleInfrastructureTestCase;
import tv.codely.mooc.courses.domain.Course;
import tv.codely.mooc.courses.domain.CourseIdMother;
import tv.codely.mooc.courses.domain.CourseMother;

import jakarta.transaction.Transactional;
import java.util.Optional;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertFalse;

@Transactional
class MySqlCourseRepositoryShould extends CoursesModuleInfrastructureTestCase {
    @Test
    void save_a_course() {
        Course course = CourseMother.random();

        mySqlCourseRepository.save(course);
    }

    @Test
    void return_an_existing_course() {
        Course course = CourseMother.random();

        mySqlCourseRepository.save(course);

        assertEquals(Optional.of(course), mySqlCourseRepository.search(course.id()));
    }

    @Test
    void not_return_a_non_existing_course() {
        assertFalse(mySqlCourseRepository.search(CourseIdMother.random()).isPresent());
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/mooc/test/tv/codely/mooc/courses_counter/CoursesCounterModuleInfrastructureTestCase.java`
```java
package tv.codely.mooc.courses_counter;

import org.springframework.beans.factory.annotation.Autowired;
import tv.codely.mooc.MoocContextInfrastructureTestCase;
import tv.codely.mooc.courses_counter.domain.CoursesCounterRepository;

public abstract class CoursesCounterModuleInfrastructureTestCase extends MoocContextInfrastructureTestCase {
    @Autowired
    protected CoursesCounterRepository repository;
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/mooc/test/tv/codely/mooc/courses_counter/CoursesCounterModuleUnitTestCase.java`
```java
package tv.codely.mooc.courses_counter;

import org.junit.jupiter.api.BeforeEach;
import org.mockito.Mockito;
import tv.codely.mooc.courses_counter.domain.CoursesCounter;
import tv.codely.mooc.courses_counter.domain.CoursesCounterRepository;
import tv.codely.shared.infrastructure.UnitTestCase;

import java.util.Optional;

import static org.mockito.Mockito.*;

public abstract class CoursesCounterModuleUnitTestCase extends UnitTestCase {
    protected CoursesCounterRepository repository;

    @BeforeEach
    protected void setUp() {
        super.setUp();

        repository = mock(CoursesCounterRepository.class);
    }

    public void shouldSearch(CoursesCounter course) {
        Mockito.when(repository.search()).thenReturn(Optional.of(course));
    }

    public void shouldSearch() {
        Mockito.when(repository.search()).thenReturn(Optional.empty());
    }

    public void shouldHaveSaved(CoursesCounter course) {
        verify(repository, atLeastOnce()).save(course);
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/mooc/test/tv/codely/mooc/courses_counter/application/find/CoursesCounterResponseMother.java`
```java
package tv.codely.mooc.courses_counter.application.find;

import tv.codely.shared.domain.IntegerMother;

final class CoursesCounterResponseMother {
    public static CoursesCounterResponse create(Integer value) {
        return new CoursesCounterResponse(value);
    }

    public static CoursesCounterResponse random() {
        return create(IntegerMother.random());
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/mooc/test/tv/codely/mooc/courses_counter/application/find/FindCoursesCounterQueryHandlerShould.java`
```java
package tv.codely.mooc.courses_counter.application.find;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import tv.codely.mooc.courses_counter.CoursesCounterModuleUnitTestCase;
import tv.codely.mooc.courses_counter.domain.CoursesCounter;
import tv.codely.mooc.courses_counter.domain.CoursesCounterMother;
import tv.codely.mooc.courses_counter.domain.CoursesCounterNotInitialized;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;

final class FindCoursesCounterQueryHandlerShould extends CoursesCounterModuleUnitTestCase {
    FindCoursesCounterQueryHandler handler;

    @BeforeEach
    protected void setUp() {
        super.setUp();

        handler = new FindCoursesCounterQueryHandler(new CoursesCounterFinder(repository));
    }

    @Test
    void it_should_find_an_existing_courses_counter() {
        CoursesCounter          counter  = CoursesCounterMother.random();
        FindCoursesCounterQuery query    = new FindCoursesCounterQuery();
        CoursesCounterResponse  response = CoursesCounterResponseMother.create(counter.total().value());

        shouldSearch(counter);

        assertEquals(response, handler.handle(query));
    }

    @Test
    void it_should_throw_an_exception_when_courses_counter_does_not_exists() {
        FindCoursesCounterQuery query = new FindCoursesCounterQuery();

        shouldSearch();

        assertThrows(CoursesCounterNotInitialized.class, () -> handler.handle(query));
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/mooc/test/tv/codely/mooc/courses_counter/application/increment/IncrementCoursesCounterOnCourseCreatedShould.java`
```java
package tv.codely.mooc.courses_counter.application.increment;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import tv.codely.mooc.courses.domain.CourseCreatedDomainEventMother;
import tv.codely.mooc.courses.domain.CourseId;
import tv.codely.mooc.courses.domain.CourseIdMother;
import tv.codely.mooc.courses_counter.CoursesCounterModuleUnitTestCase;
import tv.codely.mooc.courses_counter.domain.CoursesCounter;
import tv.codely.mooc.courses_counter.domain.CoursesCounterMother;
import tv.codely.shared.domain.course.CourseCreatedDomainEvent;

final class IncrementCoursesCounterOnCourseCreatedShould extends CoursesCounterModuleUnitTestCase {
    IncrementCoursesCounterOnCourseCreated subscriber;

    @BeforeEach
    protected void setUp() {
        super.setUp();

        subscriber = new IncrementCoursesCounterOnCourseCreated(
            new CoursesCounterIncrementer(repository, uuidGenerator)
        );
    }

    @Test
    void it_should_initialize_a_new_counter() {
        CourseCreatedDomainEvent event = CourseCreatedDomainEventMother.random();

        CourseId       courseId   = CourseIdMother.create(event.aggregateId());
        CoursesCounter newCounter = CoursesCounterMother.withOne(courseId);

        shouldSearch();
        shouldGenerateUuid(newCounter.id().value());

        subscriber.on(event);

        shouldHaveSaved(newCounter);
    }

    @Test
    void it_should_increment_an_existing_counter() {
        CourseCreatedDomainEvent event = CourseCreatedDomainEventMother.random();

        CourseId       courseId           = CourseIdMother.create(event.aggregateId());
        CoursesCounter existingCounter    = CoursesCounterMother.random();
        CoursesCounter incrementedCounter = CoursesCounterMother.incrementing(existingCounter, courseId);

        shouldSearch(existingCounter);

        subscriber.on(event);

        shouldHaveSaved(incrementedCounter);
    }

    @Test
    void it_should_not_increment_an_already_incremented_course() {
        CourseCreatedDomainEvent event = CourseCreatedDomainEventMother.random();

        CourseId       courseId        = CourseIdMother.create(event.aggregateId());
        CoursesCounter existingCounter = CoursesCounterMother.withOne(courseId);

        shouldSearch(existingCounter);

        subscriber.on(event);
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/mooc/test/tv/codely/mooc/courses_counter/domain/CoursesCounterIdMother.java`
```java
package tv.codely.mooc.courses_counter.domain;

import tv.codely.shared.domain.UuidMother;

public final class CoursesCounterIdMother {
    public static CoursesCounterId create(String value) {
        return new CoursesCounterId(value);
    }

    public static CoursesCounterId random() {
        return create(UuidMother.random());
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/mooc/test/tv/codely/mooc/courses_counter/domain/CoursesCounterMother.java`
```java
package tv.codely.mooc.courses_counter.domain;

import tv.codely.mooc.courses.domain.CourseId;
import tv.codely.mooc.courses.domain.CourseIdMother;
import tv.codely.shared.domain.ListMother;

import java.util.ArrayList;
import java.util.List;

public final class CoursesCounterMother {
    public static CoursesCounter create(
        CoursesCounterId id,
        CoursesCounterTotal total,
        List<CourseId> existingCourses
    ) {
        return new CoursesCounter(id, total, existingCourses);
    }

    public static CoursesCounter withOne(CourseId courseId) {
        return create(CoursesCounterIdMother.random(), CoursesCounterTotalMother.one(), ListMother.one(courseId));
    }

    public static CoursesCounter random() {
        List<CourseId> existingCourses = ListMother.random(CourseIdMother::random);

        return create(
            CoursesCounterIdMother.random(),
            CoursesCounterTotalMother.create(existingCourses.size()),
            existingCourses
        );
    }

    public static CoursesCounter incrementing(CoursesCounter existingCounter, CourseId courseId) {
        List<CourseId> existingCourses = new ArrayList<>(existingCounter.existingCourses());
        existingCourses.add(courseId);

        return create(
            existingCounter.id(),
            CoursesCounterTotalMother.create(existingCounter.total().value() + 1),
            existingCourses
        );
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/mooc/test/tv/codely/mooc/courses_counter/domain/CoursesCounterTotalMother.java`
```java
package tv.codely.mooc.courses_counter.domain;

import tv.codely.shared.domain.IntegerMother;

public final class CoursesCounterTotalMother {
    public static CoursesCounterTotal create(Integer value) {
        return new CoursesCounterTotal(value);
    }

    public static CoursesCounterTotal random() {
        return create(IntegerMother.random());
    }

    public static CoursesCounterTotal one() {
        return create(1);
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/mooc/test/tv/codely/mooc/courses_counter/infrastructure/persistence/MySqlCoursesCounterRepositoryShould.java`
```java
package tv.codely.mooc.courses_counter.infrastructure.persistence;

import org.junit.jupiter.api.Test;
import tv.codely.mooc.courses_counter.CoursesCounterModuleInfrastructureTestCase;
import tv.codely.mooc.courses_counter.domain.CoursesCounter;
import tv.codely.mooc.courses_counter.domain.CoursesCounterMother;

import jakarta.transaction.Transactional;
import java.util.Optional;

import static org.junit.jupiter.api.Assertions.assertEquals;

@Transactional
class MySqlCoursesCounterRepositoryShould extends CoursesCounterModuleInfrastructureTestCase {
    @Test
    void return_an_existing_courses_counter() {
        CoursesCounter counter = CoursesCounterMother.random();

        repository.save(counter);

        assertEquals(Optional.of(counter), repository.search());
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/mooc/test/tv/codely/mooc/notifications/application/NotificationsModuleUnitTestCase.java`
```java
package tv.codely.mooc.notifications.application;

import org.junit.jupiter.api.BeforeEach;
import org.mockito.ArgumentCaptor;
import tv.codely.mooc.notifications.domain.Email;
import tv.codely.mooc.notifications.domain.EmailSender;
import tv.codely.shared.infrastructure.UnitTestCase;

import java.util.List;

import static org.junit.jupiter.api.Assertions.assertTrue;
import static org.mockito.Mockito.*;

public abstract class NotificationsModuleUnitTestCase extends UnitTestCase {
    protected EmailSender sender;

    @BeforeEach
    protected void setUp() {
        super.setUp();

        sender = mock(EmailSender.class);
    }

    public void shouldHaveSentEmail(Email email) {
        ArgumentCaptor<Email> argument = ArgumentCaptor.forClass(Email.class);

        verify(sender, atLeastOnce()).send(argument.capture());

        List<Email> emails = argument.getAllValues();

        assertTrue(emails.contains(email));
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/mooc/test/tv/codely/mooc/notifications/application/send_new_courses_newsletter/SendNewCoursesNewsletterCommandHandlerShould.java`
```java
package tv.codely.mooc.notifications.application.send_new_courses_newsletter;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import tv.codely.mooc.courses.application.CoursesResponse;
import tv.codely.mooc.courses.application.CoursesResponseMother;
import tv.codely.mooc.courses.application.search_last.SearchLastCoursesQuery;
import tv.codely.mooc.courses.application.search_last.SearchLastCoursesQueryMother;
import tv.codely.mooc.notifications.application.NotificationsModuleUnitTestCase;
import tv.codely.mooc.notifications.domain.NewCoursesNewsletter;
import tv.codely.mooc.notifications.domain.NewCoursesNewsletterEmailSent;
import tv.codely.mooc.notifications.domain.NewCoursesNewsletterEmailSentMother;
import tv.codely.mooc.notifications.domain.NewCoursesNewsletterMother;
import tv.codely.mooc.students.application.StudentResponse;
import tv.codely.mooc.students.application.StudentResponseMother;
import tv.codely.mooc.students.application.StudentsResponse;
import tv.codely.mooc.students.application.StudentsResponseMother;
import tv.codely.mooc.students.application.search_all.SearchAllStudentsQuery;
import tv.codely.mooc.students.application.search_all.SearchAllStudentsQueryMother;
import tv.codely.shared.domain.bus.command.CommandHandlerExecutionError;
import tv.codely.shared.domain.bus.query.QueryHandlerExecutionError;

import java.util.Arrays;

final class SendNewCoursesNewsletterCommandHandlerShould extends NotificationsModuleUnitTestCase {
    SendNewCoursesNewsletterCommandHandler handler;

    @BeforeEach
    protected void setUp() {
        super.setUp();

        handler = new SendNewCoursesNewsletterCommandHandler(
            new NewCoursesNewsletterSender(queryBus, uuidGenerator, sender, eventBus)
        );
    }

    @Test
    void not_send_the_newsletter_when_there_are_no_courses() throws QueryHandlerExecutionError, CommandHandlerExecutionError {
        SendNewCoursesNewsletterCommand command = SendNewCoursesNewsletterCommandMother.random();

        SearchLastCoursesQuery coursesQuery    = SearchLastCoursesQueryMother.create(3);
        CoursesResponse        coursesResponse = CoursesResponseMother.empty();

        shouldAsk(coursesQuery, coursesResponse);

        handler.handle(command);
    }

    @Test
    void not_send_the_newsletter_when_there_are_no_students() throws QueryHandlerExecutionError, CommandHandlerExecutionError {
        SendNewCoursesNewsletterCommand command = SendNewCoursesNewsletterCommandMother.random();

        SearchLastCoursesQuery coursesQuery    = SearchLastCoursesQueryMother.create(3);
        CoursesResponse        coursesResponse = CoursesResponseMother.random();

        SearchAllStudentsQuery studentsQuery    = SearchAllStudentsQueryMother.random();
        StudentsResponse       studentsResponse = StudentsResponseMother.empty();

        shouldAsk(coursesQuery, coursesResponse);
        shouldAsk(studentsQuery, studentsResponse);

        handler.handle(command);
    }

    @Test
    void send_the_new_courses_newsletter() throws QueryHandlerExecutionError, CommandHandlerExecutionError {
        SendNewCoursesNewsletterCommand command = SendNewCoursesNewsletterCommandMother.random();

        SearchLastCoursesQuery coursesQuery    = SearchLastCoursesQueryMother.create(3);
        CoursesResponse        coursesResponse = CoursesResponseMother.times(3);

        SearchAllStudentsQuery studentsQuery    = SearchAllStudentsQueryMother.random();
        StudentResponse        student          = StudentResponseMother.random();
        StudentResponse        otherStudent     = StudentResponseMother.random();
        StudentsResponse       studentsResponse = StudentsResponseMother.create(Arrays.asList(student, otherStudent));

        NewCoursesNewsletter newsletter      = NewCoursesNewsletterMother.create(student, coursesResponse);
        NewCoursesNewsletter otherNewsletter = NewCoursesNewsletterMother.create(otherStudent, coursesResponse);

        NewCoursesNewsletterEmailSent domainEvent = NewCoursesNewsletterEmailSentMother.create(
            newsletter.id(),
            student.id()
        );
        NewCoursesNewsletterEmailSent otherDomainEvent = NewCoursesNewsletterEmailSentMother.create(
            otherNewsletter.id(),
            otherStudent.id()
        );

        shouldAsk(coursesQuery, coursesResponse);
        shouldAsk(studentsQuery, studentsResponse);

        shouldGenerateUuids(newsletter.id().value(), otherNewsletter.id().value());

        handler.handle(command);

        shouldHaveSentEmail(newsletter);
        shouldHavePublished(domainEvent);

        shouldHaveSentEmail(otherNewsletter);
        shouldHavePublished(otherDomainEvent);
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/mooc/test/tv/codely/mooc/notifications/application/send_new_courses_newsletter/SendNewCoursesNewsletterCommandMother.java`
```java
package tv.codely.mooc.notifications.application.send_new_courses_newsletter;

import tv.codely.shared.domain.UuidMother;

public final class SendNewCoursesNewsletterCommandMother {
    public static SendNewCoursesNewsletterCommand random() {
        return new SendNewCoursesNewsletterCommand(UuidMother.random());
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/mooc/test/tv/codely/mooc/notifications/domain/EmailIdMother.java`
```java
package tv.codely.mooc.notifications.domain;

import tv.codely.shared.domain.UuidMother;

public final class EmailIdMother {
    public static EmailId create(String value) {
        return new EmailId(value);
    }

    public static EmailId random() {
        return create(UuidMother.random());
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/mooc/test/tv/codely/mooc/notifications/domain/NewCoursesNewsletterEmailSentMother.java`
```java
package tv.codely.mooc.notifications.domain;

import tv.codely.mooc.students.domain.StudentIdMother;

public final class NewCoursesNewsletterEmailSentMother {
    public static NewCoursesNewsletterEmailSent create(EmailId id, String studentId) {
        return new NewCoursesNewsletterEmailSent(id.value(), studentId);
    }

    public static NewCoursesNewsletterEmailSent random() {
        return create(EmailIdMother.random(), StudentIdMother.random().value());
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/mooc/test/tv/codely/mooc/notifications/domain/NewCoursesNewsletterMother.java`
```java
package tv.codely.mooc.notifications.domain;

import tv.codely.mooc.courses.application.CoursesResponse;
import tv.codely.mooc.courses.application.CoursesResponseMother;
import tv.codely.mooc.students.application.StudentResponse;
import tv.codely.mooc.students.application.StudentResponseMother;

public final class NewCoursesNewsletterMother {
    public static NewCoursesNewsletter create(EmailId id, StudentResponse student, CoursesResponse courses) {
        return new NewCoursesNewsletter(id, student, courses);
    }

    public static NewCoursesNewsletter create(StudentResponse student, CoursesResponse courses) {
        return new NewCoursesNewsletter(EmailIdMother.random(), student, courses);
    }

    public static NewCoursesNewsletter random() {
        return create(EmailIdMother.random(), StudentResponseMother.random(), CoursesResponseMother.random());
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/mooc/test/tv/codely/mooc/steps/StepsModuleInfrastructureTestCase.java`
```java
package tv.codely.mooc.steps;

import org.springframework.beans.factory.annotation.Autowired;
import tv.codely.mooc.MoocContextInfrastructureTestCase;
import tv.codely.mooc.steps.domain.StepRepository;

public abstract class StepsModuleInfrastructureTestCase extends MoocContextInfrastructureTestCase {
    @Autowired
    protected StepRepository repository;
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/mooc/test/tv/codely/mooc/steps/domain/StepIdMother.java`
```java
package tv.codely.mooc.steps.domain;

import tv.codely.shared.domain.UuidMother;

public final class StepIdMother {
    public static StepId create(String value) {
        return new StepId(value);
    }

    public static StepId random() {
        return create(UuidMother.random());
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/mooc/test/tv/codely/mooc/steps/domain/StepTitleMother.java`
```java
package tv.codely.mooc.steps.domain;

import tv.codely.shared.domain.WordMother;

public final class StepTitleMother {
    public static StepTitle create(String value) {
        return new StepTitle(value);
    }

    public static StepTitle random() {
        return create(WordMother.random());
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/mooc/test/tv/codely/mooc/steps/domain/challenge/ChallengeStepMother.java`
```java
package tv.codely.mooc.steps.domain.challenge;

import tv.codely.mooc.steps.domain.StepId;
import tv.codely.mooc.steps.domain.StepIdMother;
import tv.codely.mooc.steps.domain.StepTitle;
import tv.codely.mooc.steps.domain.StepTitleMother;

public final class ChallengeStepMother {
    public static ChallengeStep create(StepId id, StepTitle title, ChallengeStepStatement statement) {
        return new ChallengeStep(id, title, statement);
    }

    public static ChallengeStep random() {
        return create(StepIdMother.random(), StepTitleMother.random(), ChallengeStepStatementMother.random());
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/mooc/test/tv/codely/mooc/steps/domain/challenge/ChallengeStepStatementMother.java`
```java
package tv.codely.mooc.steps.domain.challenge;

import tv.codely.shared.domain.WordMother;

public final class ChallengeStepStatementMother {
    public static ChallengeStepStatement create(String value) {
        return new ChallengeStepStatement(value);
    }

    public static ChallengeStepStatement random() {
        return create(WordMother.random());
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/mooc/test/tv/codely/mooc/steps/domain/video/VideoStepMother.java`
```java
package tv.codely.mooc.steps.domain.video;

import tv.codely.mooc.steps.domain.StepId;
import tv.codely.mooc.steps.domain.StepIdMother;
import tv.codely.mooc.steps.domain.StepTitle;
import tv.codely.mooc.steps.domain.StepTitleMother;
import tv.codely.shared.domain.VideoUrl;
import tv.codely.shared.domain.VideoUrlMother;

public final class VideoStepMother {
    public static VideoStep create(StepId id, StepTitle title, VideoUrl videoUrl, VideoStepText text) {
        return new VideoStep(id, title, videoUrl, text);
    }

    public static VideoStep random() {
        return create(
            StepIdMother.random(),
            StepTitleMother.random(),
            VideoUrlMother.random(),
            VideoStepTextMother.random()
        );
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/mooc/test/tv/codely/mooc/steps/domain/video/VideoStepTextMother.java`
```java
package tv.codely.mooc.steps.domain.video;

import tv.codely.shared.domain.WordMother;

public final class VideoStepTextMother {
    public static VideoStepText create(String value) {
        return new VideoStepText(value);
    }

    public static VideoStepText random() {
        return create(WordMother.random());
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/mooc/test/tv/codely/mooc/steps/infrastructure/persistence/MySqlStepRepositoryShould.java`
```java
package tv.codely.mooc.steps.infrastructure.persistence;

import org.junit.jupiter.api.Test;
import tv.codely.mooc.steps.StepsModuleInfrastructureTestCase;
import tv.codely.mooc.steps.domain.Step;
import tv.codely.mooc.steps.domain.StepIdMother;
import tv.codely.mooc.steps.domain.challenge.ChallengeStepMother;
import tv.codely.mooc.steps.domain.video.VideoStepMother;

import jakarta.transaction.Transactional;
import java.util.Arrays;
import java.util.List;
import java.util.Optional;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertFalse;

@Transactional
class MySqlStepRepositoryShould extends StepsModuleInfrastructureTestCase {
    @Test
    void save_a_step() {
        for (Step step : steps()) {
            repository.save(step);
        }
    }

    @Test
    void return_an_existing_step() {
        for (Step step : steps()) {
            repository.save(step);

            assertEquals(Optional.of(step), repository.search(step.id()));
        }
    }

    @Test
    void not_return_a_non_existing_course() {
        assertFalse(repository.search(StepIdMother.random()).isPresent());
    }

    private List<? extends Step> steps() {
        return Arrays.asList(ChallengeStepMother.random(), VideoStepMother.random());
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/mooc/test/tv/codely/mooc/students/application/StudentResponseMother.java`
```java
package tv.codely.mooc.students.application;

import tv.codely.mooc.students.domain.StudentId;
import tv.codely.mooc.students.domain.StudentIdMother;
import tv.codely.shared.domain.EmailMother;
import tv.codely.shared.domain.WordMother;

public final class StudentResponseMother {
    public static StudentResponse create(StudentId id, String name, String surname, String email) {
        return new StudentResponse(id.value(), name, surname, email);
    }

    public static StudentResponse random() {
        return create(StudentIdMother.random(), WordMother.random(), WordMother.random(), EmailMother.random());
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/mooc/test/tv/codely/mooc/students/application/StudentsResponseMother.java`
```java
package tv.codely.mooc.students.application;

import tv.codely.shared.domain.ListMother;

import java.util.Collections;
import java.util.List;

public final class StudentsResponseMother {
    public static StudentsResponse create(List<StudentResponse> courses) {
        return new StudentsResponse(courses);
    }

    public static StudentsResponse random() {
        return create(ListMother.random(StudentResponseMother::random));
    }

    public static StudentsResponse empty() {
        return create(Collections.emptyList());
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/mooc/test/tv/codely/mooc/students/application/search_all/SearchAllStudentsQueryMother.java`
```java
package tv.codely.mooc.students.application.search_all;

public final class SearchAllStudentsQueryMother {
    public static SearchAllStudentsQuery random() {
        return new SearchAllStudentsQuery();
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/mooc/test/tv/codely/mooc/students/domain/StudentIdMother.java`
```java
package tv.codely.mooc.students.domain;

import tv.codely.shared.domain.UuidMother;

public final class StudentIdMother {
    public static StudentId create(String value) {
        return new StudentId(value);
    }

    public static StudentId random() {
        return create(UuidMother.random());
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/shared/build.gradle`
```
dependencies {
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/shared/main/tv/codely/shared/domain/AggregateRoot.java`
```java
package tv.codely.shared.domain;

import tv.codely.shared.domain.bus.event.DomainEvent;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public abstract class AggregateRoot {
    private List<DomainEvent> domainEvents = new ArrayList<>();

    final public List<DomainEvent> pullDomainEvents() {
        List<DomainEvent> events = domainEvents;

        domainEvents = Collections.emptyList();

        return events;
    }

    final protected void record(DomainEvent event) {
        domainEvents.add(event);
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/shared/main/tv/codely/shared/domain/DomainError.java`
```java
package tv.codely.shared.domain;

public abstract class DomainError extends RuntimeException {
    private final String errorCode;
    private final String errorMessage;

    public DomainError(String errorCode, String errorMessage) {
        super(errorMessage);

        this.errorCode    = errorCode;
        this.errorMessage = errorMessage;
    }

    public String errorCode() {
        return errorCode;
    }

    public String errorMessage() {
        return errorMessage;
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/shared/main/tv/codely/shared/domain/Identifier.java`
```java
package tv.codely.shared.domain;

import java.io.Serializable;
import java.util.Objects;
import java.util.UUID;

public abstract class Identifier implements Serializable {
    final protected String value;

    public Identifier(String value) {
        ensureValidUuid(value);

        this.value = value;
    }

    protected Identifier() {
        this.value = null;
    }

    public String value() {
        return value;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) {
            return true;
        }
        if (o == null || getClass() != o.getClass()) {
            return false;
        }
        Identifier that = (Identifier) o;
        return value.equals(that.value);
    }

    @Override
    public int hashCode() {
        return Objects.hash(value);
    }

    private void ensureValidUuid(String value) throws IllegalArgumentException {
        UUID.fromString(value);
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/shared/main/tv/codely/shared/domain/IntValueObject.java`
```java
package tv.codely.shared.domain;

import java.util.Objects;

public abstract class IntValueObject {
    private Integer value;

    public IntValueObject(Integer value) {
        this.value = value;
    }

    public Integer value() {
        return value;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) {
            return true;
        }
        if (o == null || getClass() != o.getClass()) {
            return false;
        }
        IntValueObject that = (IntValueObject) o;
        return value.equals(that.value);
    }

    @Override
    public int hashCode() {
        return Objects.hash(value);
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/shared/main/tv/codely/shared/domain/Logger.java`
```java
package tv.codely.shared.domain;

import java.io.Serializable;
import java.util.HashMap;

public interface Logger {
    void info(String $message);
    void info(String $message, HashMap<String, Serializable> $context);

    void warning(String $message);
    void warning(String $message, HashMap<String, Serializable> $context);

    void critical(String $message);
    void critical(String $message, HashMap<String, Serializable> $context);
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/shared/main/tv/codely/shared/domain/Monitoring.java`
```java
package tv.codely.shared.domain;

import java.util.HashMap;

public interface Monitoring {
    void incrementCounter(int times);

    void incrementGauge(int times);
    void decrementGauge(int times);
    void setGauge(int value);

    void observeHistogram(int value, HashMap<String, String> labels);
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/shared/main/tv/codely/shared/domain/Service.java`
```java
package tv.codely.shared.domain;

import java.lang.annotation.*;

@Retention(RetentionPolicy.RUNTIME)
@Target(ElementType.TYPE)
@Inherited
public @interface Service {
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/shared/main/tv/codely/shared/domain/StringValueObject.java`
```java
package tv.codely.shared.domain;

import java.util.Objects;

public abstract class StringValueObject {
    private String value;

    public StringValueObject(String value) {
        this.value = value;
    }

    public String value() {
        return value;
    }

    @Override
    public String toString() {
        return this.value();
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) {
            return true;
        }
        if (!(o instanceof StringValueObject)) {
            return false;
        }
        StringValueObject that = (StringValueObject) o;
        return Objects.equals(value, that.value);
    }

    @Override
    public int hashCode() {
        return Objects.hash(value);
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/shared/main/tv/codely/shared/domain/Utils.java`
```java
package tv.codely.shared.domain;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.google.common.base.CaseFormat;

import java.io.IOException;
import java.io.Serializable;
import java.sql.Timestamp;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.HashMap;

public final class Utils {
    public static String dateToString(LocalDateTime dateTime) {
        return dateTime.format(DateTimeFormatter.ISO_LOCAL_DATE);
    }

    public static String dateToString(Timestamp timestamp) {
        return dateToString(timestamp.toLocalDateTime());
    }

    public static String jsonEncode(HashMap<String, Serializable> map) {
        try {
            return new ObjectMapper().writeValueAsString(map);
        } catch (JsonProcessingException e) {
            return "";
        }
    }

    public static HashMap<String, Serializable> jsonDecode(String body) {
        try {
            return new ObjectMapper().readValue(body, HashMap.class);
        } catch (IOException e) {
            return null;
        }
    }

    public static String toSnake(String text) {
        return CaseFormat.UPPER_CAMEL.to(CaseFormat.LOWER_UNDERSCORE, text);
    }

    public static String toCamel(String text) {
        return CaseFormat.LOWER_UNDERSCORE.to(CaseFormat.UPPER_CAMEL, text);
    }

    public static String toCamelFirstLower(String text) {
        return CaseFormat.LOWER_UNDERSCORE.to(CaseFormat.LOWER_CAMEL, text);
    }

	public static void retry(int numberOfRetries, long waitTimeInMillis, Runnable operation) throws Exception {
		for (int i = 0; i < numberOfRetries; i++) {
			try {
				operation.run();
				return; // Success, exit the method
			} catch (Exception ex) {
				System.out.println("Retry " + (i + 1) + "/" + numberOfRetries + " fail. Retrying…");
				if (i >= numberOfRetries - 1) {
					throw ex;
				}

				try {
					Thread.sleep(waitTimeInMillis);
				} catch (InterruptedException ie) {
					Thread.currentThread().interrupt();

					throw new Exception("Operation interrupted while retrying", ie);
				}
			}
		}
	}

}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/shared/main/tv/codely/shared/domain/UuidGenerator.java`
```java
package tv.codely.shared.domain;

public interface UuidGenerator {
    String generate();
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/shared/main/tv/codely/shared/domain/VideoUrl.java`
```java
package tv.codely.shared.domain;

public final class VideoUrl extends StringValueObject {
    public VideoUrl(String value) {
        super(value);
    }

    public VideoUrl() {
        super(null);
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/shared/main/tv/codely/shared/domain/bus/command/Command.java`
```java
package tv.codely.shared.domain.bus.command;

public interface Command {
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/shared/main/tv/codely/shared/domain/bus/command/CommandBus.java`
```java
package tv.codely.shared.domain.bus.command;

public interface CommandBus {
    void dispatch(Command command) throws CommandHandlerExecutionError;
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/shared/main/tv/codely/shared/domain/bus/command/CommandHandler.java`
```java
package tv.codely.shared.domain.bus.command;

public interface CommandHandler<T extends Command> {
    void handle(T command);
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/shared/main/tv/codely/shared/domain/bus/command/CommandHandlerExecutionError.java`
```java
package tv.codely.shared.domain.bus.command;

public final class CommandHandlerExecutionError extends RuntimeException {
    public CommandHandlerExecutionError(Throwable cause) {
        super(cause);
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/shared/main/tv/codely/shared/domain/bus/command/CommandNotRegisteredError.java`
```java
package tv.codely.shared.domain.bus.command;

public final class CommandNotRegisteredError extends Exception {
    public CommandNotRegisteredError(Class<? extends Command> command) {
        super(String.format("The command <%s> hasn't a command handler associated", command.toString()));
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/shared/main/tv/codely/shared/domain/bus/event/DomainEvent.java`
```java
package tv.codely.shared.domain.bus.event;

import tv.codely.shared.domain.Utils;

import java.io.Serializable;
import java.time.LocalDateTime;
import java.util.HashMap;
import java.util.UUID;

public abstract class DomainEvent {
    private String aggregateId;
    private String eventId;
    private String occurredOn;

    public DomainEvent(String aggregateId) {
        this.aggregateId = aggregateId;
        this.eventId     = UUID.randomUUID().toString();
        this.occurredOn  = Utils.dateToString(LocalDateTime.now());
    }

    public DomainEvent(String aggregateId, String eventId, String occurredOn) {
        this.aggregateId = aggregateId;
        this.eventId     = eventId;
        this.occurredOn  = occurredOn;
    }

    protected DomainEvent() {
    }

    public abstract String eventName();

    public abstract HashMap<String, Serializable> toPrimitives();

    public abstract DomainEvent fromPrimitives(
        String aggregateId,
        HashMap<String, Serializable> body,
        String eventId,
        String occurredOn
    );

    public String aggregateId() {
        return aggregateId;
    }

    public String eventId() {
        return eventId;
    }

    public String occurredOn() {
        return occurredOn;
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/shared/main/tv/codely/shared/domain/bus/event/DomainEventSubscriber.java`
```java
package tv.codely.shared.domain.bus.event;

import java.lang.annotation.*;

@Retention(RetentionPolicy.RUNTIME)
@Target(ElementType.TYPE)
@Inherited
public @interface DomainEventSubscriber {
    Class<? extends DomainEvent>[] value();
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/shared/main/tv/codely/shared/domain/bus/event/EventBus.java`
```java
package tv.codely.shared.domain.bus.event;

import java.util.List;

public interface EventBus {
    void publish(final List<DomainEvent> events);
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/shared/main/tv/codely/shared/domain/bus/query/Query.java`
```java
package tv.codely.shared.domain.bus.query;

public interface Query {
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/shared/main/tv/codely/shared/domain/bus/query/QueryBus.java`
```java
package tv.codely.shared.domain.bus.query;

public interface QueryBus {
    <R> R ask(Query query) throws QueryHandlerExecutionError;
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/shared/main/tv/codely/shared/domain/bus/query/QueryHandler.java`
```java
package tv.codely.shared.domain.bus.query;

public interface QueryHandler<Q extends Query, R extends Response> {
    R handle(Q query);
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/shared/main/tv/codely/shared/domain/bus/query/QueryHandlerExecutionError.java`
```java
package tv.codely.shared.domain.bus.query;

public final class QueryHandlerExecutionError extends RuntimeException {
    public QueryHandlerExecutionError(Throwable cause) {
        super(cause);
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/shared/main/tv/codely/shared/domain/bus/query/QueryNotRegisteredError.java`
```java
package tv.codely.shared.domain.bus.query;

public final class QueryNotRegisteredError extends Exception {
    public QueryNotRegisteredError(Class<? extends Query> query) {
        super(String.format("The query <%s> hasn't a query handler associated", query.toString()));
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/shared/main/tv/codely/shared/domain/bus/query/Response.java`
```java
package tv.codely.shared.domain.bus.query;

public interface Response {
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/shared/main/tv/codely/shared/domain/course/CourseCreatedDomainEvent.java`
```java
package tv.codely.shared.domain.course;

import tv.codely.shared.domain.bus.event.DomainEvent;

import java.io.Serializable;
import java.util.HashMap;
import java.util.Objects;

public final class CourseCreatedDomainEvent extends DomainEvent {
    private final String name;
    private final String duration;

    public CourseCreatedDomainEvent() {
        super(null);

        this.name     = null;
        this.duration = null;
    }

    public CourseCreatedDomainEvent(String aggregateId, String name, String duration) {
        super(aggregateId);

        this.name     = name;
        this.duration = duration;
    }

    public CourseCreatedDomainEvent(
        String aggregateId,
        String eventId,
        String occurredOn,
        String name,
        String duration
    ) {
        super(aggregateId, eventId, occurredOn);

        this.name     = name;
        this.duration = duration;
    }

    @Override
    public String eventName() {
        return "course.created";
    }

    @Override
    public HashMap<String, Serializable> toPrimitives() {
        return new HashMap<String, Serializable>() {{
            put("name", name);
            put("duration", duration);
        }};
    }

    @Override
    public CourseCreatedDomainEvent fromPrimitives(
        String aggregateId,
        HashMap<String, Serializable> body,
        String eventId,
        String occurredOn
    ) {
        return new CourseCreatedDomainEvent(
            aggregateId,
            eventId,
            occurredOn,
            (String) body.get("name"),
            (String) body.get("duration")
        );
    }

    public String name() {
        return name;
    }

    public String duration() {
        return duration;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) {
            return true;
        }
        if (o == null || getClass() != o.getClass()) {
            return false;
        }
        CourseCreatedDomainEvent that = (CourseCreatedDomainEvent) o;
        return name.equals(that.name) &&
               duration.equals(that.duration);
    }

    @Override
    public int hashCode() {
        return Objects.hash(name, duration);
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/shared/main/tv/codely/shared/domain/criteria/Criteria.java`
```java
package tv.codely.shared.domain.criteria;

import java.util.Optional;

public final class Criteria {
    private final Filters           filters;
    private final Order             order;
    private final Optional<Integer> limit;
    private final Optional<Integer> offset;

    public Criteria(Filters filters, Order order, Optional<Integer> limit, Optional<Integer> offset) {
        this.filters = filters;
        this.order   = order;
        this.limit   = limit;
        this.offset  = offset;
    }

    public Criteria(Filters filters, Order order) {
        this.filters = filters;
        this.order   = order;
        this.limit   = Optional.empty();
        this.offset  = Optional.empty();
    }

    public Filters filters() {
        return filters;
    }

    public Order order() {
        return order;
    }

    public Optional<Integer> limit() {
        return limit;
    }

    public Optional<Integer> offset() {
        return offset;
    }

    public boolean hasFilters() {
        return filters.filters().size() > 0;
    }

    public String serialize() {
        return String.format(
            "%s~~%s~~%s~~%s",
            filters.serialize(),
            order.serialize(),
            offset.orElse(0),
            limit.orElse(0)
        );
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/shared/main/tv/codely/shared/domain/criteria/Filter.java`
```java
package tv.codely.shared.domain.criteria;

import java.util.HashMap;

public final class Filter {
    private final FilterField    field;
    private final FilterOperator operator;
    private final FilterValue    value;

    public Filter(FilterField field, FilterOperator operator, FilterValue value) {
        this.field    = field;
        this.operator = operator;
        this.value    = value;
    }

    public static Filter create(String field, String operator, String value) {
        return new Filter(
            new FilterField(field),
            FilterOperator.fromValue(operator.toUpperCase()),
            new FilterValue(value)
        );
    }

    public static Filter fromValues(HashMap<String, String> values) {
        return new Filter(
            new FilterField(values.get("field")),
            FilterOperator.fromValue(values.get("operator")),
            new FilterValue(values.get("value"))
        );
    }

    public FilterField field() {
        return field;
    }

    public FilterOperator operator() {
        return operator;
    }

    public FilterValue value() {
        return value;
    }

    public String serialize() {
        return String.format("%s.%s.%s", field.value(), operator.value(), value.value());
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/shared/main/tv/codely/shared/domain/criteria/FilterField.java`
```java
package tv.codely.shared.domain.criteria;

import tv.codely.shared.domain.StringValueObject;

public final class FilterField extends StringValueObject {
    public FilterField(String value) {
        super(value);
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/shared/main/tv/codely/shared/domain/criteria/FilterOperator.java`
```java
package tv.codely.shared.domain.criteria;

public enum FilterOperator {
    EQUAL("="),
    NOT_EQUAL("!="),
    GT(">"),
    LT("<"),
    CONTAINS("CONTAINS"),
    NOT_CONTAINS("NOT_CONTAINS");

    private final String operator;

    FilterOperator(String operator) {
        this.operator = operator;
    }

    public static FilterOperator fromValue(String value) {
        switch (value) {
            case "=": return FilterOperator.EQUAL;
            case "!=": return FilterOperator.NOT_EQUAL;
            case ">": return FilterOperator.GT;
            case "<": return FilterOperator.LT;
            case "CONTAINS": return FilterOperator.CONTAINS;
            case "NOT_CONTAINS": return FilterOperator.NOT_CONTAINS;
            default: return null;
        }
    }

    public boolean isPositive() {
        return this != NOT_EQUAL && this != NOT_CONTAINS;
    }

    public String value() {
        return operator;
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/shared/main/tv/codely/shared/domain/criteria/FilterValue.java`
```java
package tv.codely.shared.domain.criteria;

import tv.codely.shared.domain.StringValueObject;

public final class FilterValue extends StringValueObject {
    public FilterValue(String value) {
        super(value);
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/shared/main/tv/codely/shared/domain/criteria/Filters.java`
```java
package tv.codely.shared.domain.criteria;

import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.stream.Collectors;

public final class Filters {
    private final List<Filter> filters;

    public Filters(List<Filter> filters) {
        this.filters = filters;
    }

    public static Filters fromValues(List<HashMap<String, String>> filters) {
        return new Filters(filters.stream().map(Filter::fromValues).collect(Collectors.toList()));
    }

    public static Filters none() {
        return new Filters(Collections.emptyList());
    }

    public List<Filter> filters() {
        return filters;
    }

    public String serialize() {
        return filters.stream().map(Filter::serialize).collect(Collectors.joining("^"));
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/shared/main/tv/codely/shared/domain/criteria/Order.java`
```java
package tv.codely.shared.domain.criteria;

import java.util.Optional;

public final class Order {
    private final OrderBy   orderBy;
    private final OrderType orderType;

    public Order(OrderBy orderBy, OrderType orderType) {
        this.orderBy   = orderBy;
        this.orderType = orderType;
    }

    public static Order fromValues(Optional<String> orderBy, Optional<String> orderType) {
        return orderBy.map(order -> new Order(new OrderBy(order), OrderType.valueOf(orderType.orElse("ASC"))))
                      .orElseGet(Order::none);
    }

    public static Order none() {
        return new Order(new OrderBy(""), OrderType.NONE);
    }

    public static Order desc(String orderBy) {
        return new Order(new OrderBy(orderBy), OrderType.DESC);
    }

    public static Order asc(String orderBy) {
        return new Order(new OrderBy(orderBy), OrderType.ASC);
    }

    public OrderBy orderBy() {
        return orderBy;
    }

    public OrderType orderType() {
        return orderType;
    }

    public boolean hasOrder() {
        return !orderType.isNone();
    }

    public String serialize() {
        return String.format("%s.%s", orderBy.value(), orderType.value());
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/shared/main/tv/codely/shared/domain/criteria/OrderBy.java`
```java
package tv.codely.shared.domain.criteria;

import tv.codely.shared.domain.StringValueObject;

public final class OrderBy extends StringValueObject {
    public OrderBy(String value) {
        super(value);
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/shared/main/tv/codely/shared/domain/criteria/OrderType.java`
```java
package tv.codely.shared.domain.criteria;

public enum OrderType {
    ASC("asc"),
    DESC("desc"),
    NONE("none");
    private final String type;

    OrderType(String type) {
        this.type = type;
    }

    public boolean isNone() {
        return this == NONE;
    }

    public boolean isAsc() {
        return this == ASC;
    }

    public String value() {
        return type;
    }
}

```

## File: `CodelyTV-java-ddd-example-3a58e32/src/shared/main/tv/codely/shared/infrastructure/JavaUuidGenerator.java`
```java
package tv.codely.shared.infrastructure;

import tv.codely.shared.domain.Service;
import tv.codely.shared.domain.UuidGenerator;

import java.util.UUID;

@Service
public final class JavaUuidGenerator implements UuidGenerator {
    @Override
    public String generate() {
        return UUID.randomUUID().toString();
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/shared/main/tv/codely/shared/infrastructure/bus/command/CommandHandlersInformation.java`
```java
package tv.codely.shared.infrastructure.bus.command;

import org.reflections.Reflections;
import tv.codely.shared.domain.Service;
import tv.codely.shared.domain.bus.command.Command;
import tv.codely.shared.domain.bus.command.CommandHandler;
import tv.codely.shared.domain.bus.command.CommandNotRegisteredError;

import java.lang.reflect.ParameterizedType;
import java.util.HashMap;
import java.util.Set;

@Service
public final class CommandHandlersInformation {
    HashMap<Class<? extends Command>, Class<? extends CommandHandler>> indexedCommandHandlers;

    public CommandHandlersInformation() {
        Reflections                          reflections = new Reflections("tv.codely");
        Set<Class<? extends CommandHandler>> classes     = reflections.getSubTypesOf(CommandHandler.class);

        indexedCommandHandlers = formatHandlers(classes);
    }

    public Class<? extends CommandHandler> search(Class<? extends Command> commandClass) throws CommandNotRegisteredError {
        Class<? extends CommandHandler> commandHandlerClass = indexedCommandHandlers.get(commandClass);

        if (null == commandHandlerClass) {
            throw new CommandNotRegisteredError(commandClass);
        }

        return commandHandlerClass;
    }

    private HashMap<Class<? extends Command>, Class<? extends CommandHandler>> formatHandlers(
        Set<Class<? extends CommandHandler>> commandHandlers
    ) {
        HashMap<Class<? extends Command>, Class<? extends CommandHandler>> handlers = new HashMap<>();

        for (Class<? extends CommandHandler> handler : commandHandlers) {
            ParameterizedType        paramType    = (ParameterizedType) handler.getGenericInterfaces()[0];
            Class<? extends Command> commandClass = (Class<? extends Command>) paramType.getActualTypeArguments()[0];

            handlers.put(commandClass, handler);
        }

        return handlers;
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/shared/main/tv/codely/shared/infrastructure/bus/command/InMemoryCommandBus.java`
```java
package tv.codely.shared.infrastructure.bus.command;

import org.springframework.context.ApplicationContext;
import tv.codely.shared.domain.Service;
import tv.codely.shared.domain.bus.command.Command;
import tv.codely.shared.domain.bus.command.CommandBus;
import tv.codely.shared.domain.bus.command.CommandHandler;
import tv.codely.shared.domain.bus.command.CommandHandlerExecutionError;

@Service
public final class InMemoryCommandBus implements CommandBus {
    private final CommandHandlersInformation information;
    private final ApplicationContext         context;

    public InMemoryCommandBus(CommandHandlersInformation information, ApplicationContext context) {
        this.information = information;
        this.context     = context;
    }

    @Override
    public void dispatch(Command command) throws CommandHandlerExecutionError {
        try {
            Class<? extends CommandHandler> commandHandlerClass = information.search(command.getClass());

            CommandHandler handler = context.getBean(commandHandlerClass);

            handler.handle(command);
        } catch (Throwable error) {
            throw new CommandHandlerExecutionError(error);
        }
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/shared/main/tv/codely/shared/infrastructure/bus/event/DomainEventJsonDeserializer.java`
```java
package tv.codely.shared.infrastructure.bus.event;

import tv.codely.shared.domain.Service;
import tv.codely.shared.domain.Utils;
import tv.codely.shared.domain.bus.event.DomainEvent;

import java.io.Serializable;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import java.util.HashMap;

@Service
public final class DomainEventJsonDeserializer {
    private final DomainEventsInformation information;

    public DomainEventJsonDeserializer(DomainEventsInformation information) {
        this.information = information;
    }

    public DomainEvent deserialize(String body) throws InvocationTargetException, IllegalAccessException, NoSuchMethodException, InstantiationException {
        HashMap<String, Serializable> eventData        = Utils.jsonDecode(body);
        HashMap<String, Serializable> data             = (HashMap<String, Serializable>) eventData.get("data");
        HashMap<String, Serializable> attributes       = (HashMap<String, Serializable>) data.get("attributes");
        Class<? extends DomainEvent>  domainEventClass = information.forName((String) data.get("type"));

        DomainEvent nullInstance = domainEventClass.getConstructor().newInstance();

        Method fromPrimitivesMethod = domainEventClass.getMethod(
            "fromPrimitives",
            String.class,
            HashMap.class,
            String.class,
            String.class
        );

        Object domainEvent = fromPrimitivesMethod.invoke(
            nullInstance,
            (String) attributes.get("id"),
            attributes,
            (String) data.get("id"),
            (String) data.get("occurred_on")
        );

        return (DomainEvent) domainEvent;
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/shared/main/tv/codely/shared/infrastructure/bus/event/DomainEventJsonSerializer.java`
```java
package tv.codely.shared.infrastructure.bus.event;

import tv.codely.shared.domain.Utils;
import tv.codely.shared.domain.bus.event.DomainEvent;

import java.io.Serializable;
import java.util.HashMap;

public final class DomainEventJsonSerializer {
    public static String serialize(DomainEvent domainEvent) {
        HashMap<String, Serializable> attributes = domainEvent.toPrimitives();
        attributes.put("id", domainEvent.aggregateId());

        return Utils.jsonEncode(new HashMap<String, Serializable>() {{
            put("data", new HashMap<String, Serializable>() {{
                put("id", domainEvent.eventId());
                put("type", domainEvent.eventName());
                put("occurred_on", domainEvent.occurredOn());
                put("attributes", attributes);
            }});
            put("meta", new HashMap<String, Serializable>());
        }});
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/shared/main/tv/codely/shared/infrastructure/bus/event/DomainEventSubscriberInformation.java`
```java
package tv.codely.shared.infrastructure.bus.event;

import tv.codely.shared.domain.Utils;
import tv.codely.shared.domain.bus.event.DomainEvent;

import java.util.List;

public final class DomainEventSubscriberInformation {
    private final Class<?>                           subscriberClass;
    private final List<Class<? extends DomainEvent>> subscribedEvents;

    public DomainEventSubscriberInformation(
        Class<?> subscriberClass,
        List<Class<? extends DomainEvent>> subscribedEvents
    ) {
        this.subscriberClass  = subscriberClass;
        this.subscribedEvents = subscribedEvents;
    }

    public Class<?> subscriberClass() {
        return subscriberClass;
    }

    public String contextName() {
        String[] nameParts = subscriberClass.getName().split("\\.");

        return nameParts[2];
    }

    public String moduleName() {
        String[] nameParts = subscriberClass.getName().split("\\.");

        return nameParts[3];
    }

    public String className() {
        String[] nameParts = subscriberClass.getName().split("\\.");

        return nameParts[nameParts.length - 1];
    }

    public List<Class<? extends DomainEvent>> subscribedEvents() {
        return subscribedEvents;
    }

    public String formatRabbitMqQueueName() {
        return String.format("codely.%s.%s.%s", contextName(), moduleName(), Utils.toSnake(className()));
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/shared/main/tv/codely/shared/infrastructure/bus/event/DomainEventSubscribersInformation.java`
```java
package tv.codely.shared.infrastructure.bus.event;

import org.reflections.Reflections;
import tv.codely.shared.domain.Service;
import tv.codely.shared.domain.bus.event.DomainEventSubscriber;

import java.util.Arrays;
import java.util.Collection;
import java.util.HashMap;
import java.util.Set;

@Service
public final class DomainEventSubscribersInformation {
    HashMap<Class<?>, DomainEventSubscriberInformation> information;

    public DomainEventSubscribersInformation(HashMap<Class<?>, DomainEventSubscriberInformation> information) {
        this.information = information;
    }

    public DomainEventSubscribersInformation() {
        this(scanDomainEventSubscribers());
    }

    private static HashMap<Class<?>, DomainEventSubscriberInformation> scanDomainEventSubscribers() {
        Reflections   reflections = new Reflections("tv.codely");
        Set<Class<?>> subscribers = reflections.getTypesAnnotatedWith(DomainEventSubscriber.class);

        HashMap<Class<?>, DomainEventSubscriberInformation> subscribersInformation = new HashMap<>();

        for (Class<?> subscriberClass : subscribers) {
            DomainEventSubscriber annotation = subscriberClass.getAnnotation(DomainEventSubscriber.class);

            subscribersInformation.put(
                subscriberClass,
                new DomainEventSubscriberInformation(subscriberClass, Arrays.asList(annotation.value()))
            );
        }

        return subscribersInformation;
    }

    public Collection<DomainEventSubscriberInformation> all() {
        return information.values();
    }

    public String[] rabbitMqFormattedNames() {
        return information.values()
                          .stream()
                          .map(DomainEventSubscriberInformation::formatRabbitMqQueueName)
                          .distinct()
                          .toArray(String[]::new);
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/shared/main/tv/codely/shared/infrastructure/bus/event/DomainEventsInformation.java`
```java
package tv.codely.shared.infrastructure.bus.event;

import org.reflections.Reflections;
import tv.codely.shared.domain.Service;
import tv.codely.shared.domain.bus.event.DomainEvent;

import java.lang.reflect.InvocationTargetException;
import java.util.HashMap;
import java.util.Map;
import java.util.Objects;
import java.util.Set;

@Service
public final class DomainEventsInformation {
    HashMap<String, Class<? extends DomainEvent>> indexedDomainEvents;

    public DomainEventsInformation() {
        Reflections                       reflections = new Reflections("tv.codely");
        Set<Class<? extends DomainEvent>> classes     = reflections.getSubTypesOf(DomainEvent.class);

        try {
            indexedDomainEvents = formatEvents(classes);
        } catch (NoSuchMethodException | IllegalAccessException | InstantiationException | InvocationTargetException e) {
            e.printStackTrace();
        }
    }

    public Class<? extends DomainEvent> forName(String name) {
        return indexedDomainEvents.get(name);
    }

    public String forClass(Class<? extends DomainEvent> domainEventClass) {
        return indexedDomainEvents.entrySet()
                                  .stream()
                                  .filter(entry -> Objects.equals(entry.getValue(), domainEventClass))
                                  .map(Map.Entry::getKey)
                                  .findFirst().orElse("");
    }

    private HashMap<String, Class<? extends DomainEvent>> formatEvents(
        Set<Class<? extends DomainEvent>> domainEvents
    ) throws NoSuchMethodException, IllegalAccessException, InvocationTargetException, InstantiationException {
        HashMap<String, Class<? extends DomainEvent>> events = new HashMap<>();

        for (Class<? extends DomainEvent> domainEvent : domainEvents) {
            DomainEvent nullInstance = domainEvent.getConstructor().newInstance();

            events.put((String) domainEvent.getMethod("eventName").invoke(nullInstance), domainEvent);
        }

        return events;
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/shared/main/tv/codely/shared/infrastructure/bus/query/InMemoryQueryBus.java`
```java
package tv.codely.shared.infrastructure.bus.query;

import org.springframework.context.ApplicationContext;
import tv.codely.shared.domain.Service;
import tv.codely.shared.domain.bus.query.*;

@Service
public final class InMemoryQueryBus implements QueryBus {
    private final QueryHandlersInformation information;
    private final ApplicationContext       context;

    public InMemoryQueryBus(QueryHandlersInformation information, ApplicationContext context) {
        this.information = information;
        this.context     = context;
    }

    @Override
    public Response ask(Query query) throws QueryHandlerExecutionError {
        try {
            Class<? extends QueryHandler> queryHandlerClass = information.search(query.getClass());

            QueryHandler handler = context.getBean(queryHandlerClass);

            return handler.handle(query);
        } catch (Throwable error) {
            throw new QueryHandlerExecutionError(error);
        }
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/shared/main/tv/codely/shared/infrastructure/bus/query/QueryHandlersInformation.java`
```java
package tv.codely.shared.infrastructure.bus.query;

import org.reflections.Reflections;
import tv.codely.shared.domain.Service;
import tv.codely.shared.domain.bus.query.Query;
import tv.codely.shared.domain.bus.query.QueryHandler;
import tv.codely.shared.domain.bus.query.QueryNotRegisteredError;

import java.lang.reflect.ParameterizedType;
import java.util.HashMap;
import java.util.Set;

@Service
public final class QueryHandlersInformation {
    HashMap<Class<? extends Query>, Class<? extends QueryHandler>> indexedQueryHandlers;

    public QueryHandlersInformation() {
        Reflections                        reflections = new Reflections("tv.codely");
        Set<Class<? extends QueryHandler>> classes     = reflections.getSubTypesOf(QueryHandler.class);

        indexedQueryHandlers = formatHandlers(classes);
    }

    public Class<? extends QueryHandler> search(Class<? extends Query> queryClass) throws QueryNotRegisteredError {
        Class<? extends QueryHandler> queryHandlerClass = indexedQueryHandlers.get(queryClass);

        if (null == queryHandlerClass) {
            throw new QueryNotRegisteredError(queryClass);
        }

        return queryHandlerClass;
    }

    private HashMap<Class<? extends Query>, Class<? extends QueryHandler>> formatHandlers(
        Set<Class<? extends QueryHandler>> queryHandlers
    ) {
        HashMap<Class<? extends Query>, Class<? extends QueryHandler>> handlers = new HashMap<>();

        for (Class<? extends QueryHandler> handler : queryHandlers) {
            ParameterizedType      paramType  = (ParameterizedType) handler.getGenericInterfaces()[0];
            Class<? extends Query> queryClass = (Class<? extends Query>) paramType.getActualTypeArguments()[0];

            handlers.put(queryClass, handler);
        }

        return handlers;
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/shared/main/tv/codely/shared/infrastructure/cli/ConsoleCommand.java`
```java
package tv.codely.shared.infrastructure.cli;

import tv.codely.shared.domain.Service;

@Service
public abstract class ConsoleCommand {
    private static final String ANSI_RESET = "\u001B[0m";
    private static final String ANSI_RED   = "\u001B[31m";
    private static final String ANSI_CYAN  = "\u001B[36m";
    private static final String ANSI_GREEN = "\u001B[32m";

    abstract public void execute(String[] args);

    protected void log(String text) {
        System.out.println(String.format("%s%s%s", ANSI_GREEN, text, ANSI_RESET));
    }

    protected void info(String text) {
        System.out.println(String.format("%s%s%s", ANSI_CYAN, text, ANSI_RESET));
    }

    protected void error(String text) {
        System.out.println(String.format("%s%s%s", ANSI_RED, text, ANSI_RESET));
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/shared/main/tv/codely/shared/infrastructure/config/EnvironmentConfig.java`
```java
package tv.codely.shared.infrastructure.config;

import io.github.cdimascio.dotenv.Dotenv;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.core.io.Resource;
import org.springframework.core.io.ResourceLoader;

@Configuration
public class EnvironmentConfig {
    ResourceLoader resourceLoader;

    public EnvironmentConfig(ResourceLoader resourceLoader) {
        this.resourceLoader = resourceLoader;
    }

    @Bean
    public Dotenv dotenv() {
        Resource resource = resourceLoader.getResource("classpath:/.env.local");

        return Dotenv
            .configure()
            .directory("/")
            .filename(resource.exists() ? ".env.local" : ".env")
            .load();
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/shared/main/tv/codely/shared/infrastructure/config/Parameter.java`
```java
package tv.codely.shared.infrastructure.config;

import io.github.cdimascio.dotenv.Dotenv;
import tv.codely.shared.domain.Service;

@Service
public final class Parameter {
    private final Dotenv dotenv;

    public Parameter(Dotenv dotenv) {
        this.dotenv = dotenv;
    }

    public String get(String key) throws ParameterNotExist {
        String value = dotenv.get(key);

        if (null == value) {
            throw new ParameterNotExist(key);
        }

        return value;
    }

    public Integer getInt(String key) throws ParameterNotExist {
        String value = get(key);

        return Integer.parseInt(value);
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/shared/main/tv/codely/shared/infrastructure/config/ParameterNotExist.java`
```java
package tv.codely.shared.infrastructure.config;

public final class ParameterNotExist extends Throwable {
    public ParameterNotExist(String key) {
        super(String.format("The parameter <%s> does not exist in the environment file", key));
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/shared/main/tv/codely/shared/infrastructure/elasticsearch/ElasticsearchClient.java`
```java
package tv.codely.shared.infrastructure.elasticsearch;

import org.elasticsearch.action.admin.indices.delete.DeleteIndexRequest;
import org.elasticsearch.action.index.IndexRequest;
import org.elasticsearch.client.RequestOptions;
import org.elasticsearch.client.RestClient;
import org.elasticsearch.client.RestHighLevelClient;

import java.io.IOException;
import java.io.Serializable;
import java.util.HashMap;

public final class ElasticsearchClient {
    private final RestHighLevelClient highLevelClient;
    private final RestClient          lowLevelClient;
    private final String              indexPrefix;

    public ElasticsearchClient(RestHighLevelClient highLevelClient, RestClient lowLevelClient, String indexPrefix) {
        this.highLevelClient = highLevelClient;
        this.lowLevelClient  = lowLevelClient;
        this.indexPrefix     = indexPrefix;
    }

    public RestHighLevelClient highLevelClient() {
        return highLevelClient;
    }

    public RestClient lowLevelClient() {
        return lowLevelClient;
    }

    public String indexPrefix() {
        return indexPrefix;
    }

    public void persist(String moduleName, String id, HashMap<String, Serializable> plainBody) throws IOException {
        IndexRequest request = new IndexRequest(indexFor(moduleName), moduleName, id).source(plainBody);

        highLevelClient().index(request, RequestOptions.DEFAULT);
    }

    public String indexFor(String moduleName) {
        return String.format("%s_%s", indexPrefix(), moduleName);
    }

    public void delete(String index) throws IOException {
        highLevelClient.indices().delete(new DeleteIndexRequest(index), RequestOptions.DEFAULT);
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/shared/main/tv/codely/shared/infrastructure/elasticsearch/ElasticsearchCriteriaConverter.java`
```java
package tv.codely.shared.infrastructure.elasticsearch;

import org.elasticsearch.index.query.BoolQueryBuilder;
import org.elasticsearch.index.query.QueryBuilder;
import org.elasticsearch.index.query.QueryBuilders;
import org.elasticsearch.search.builder.SearchSourceBuilder;
import org.elasticsearch.search.sort.SortOrder;
import tv.codely.shared.domain.criteria.Criteria;
import tv.codely.shared.domain.criteria.Filter;
import tv.codely.shared.domain.criteria.FilterOperator;
import tv.codely.shared.domain.criteria.Filters;

import java.util.HashMap;
import java.util.function.Function;

public final class ElasticsearchCriteriaConverter {
    private final HashMap<FilterOperator, Function<Filter, QueryBuilder>> queryTransformers = new HashMap<FilterOperator, Function<Filter, QueryBuilder>>() {{
        put(FilterOperator.EQUAL, ElasticsearchCriteriaConverter.this::termQuery);
        put(FilterOperator.NOT_EQUAL, ElasticsearchCriteriaConverter.this::termQuery);
        put(FilterOperator.GT, ElasticsearchCriteriaConverter.this::greaterThanQueryTransformer);
        put(FilterOperator.LT, ElasticsearchCriteriaConverter.this::lowerThanQueryTransformer);
        put(FilterOperator.CONTAINS, ElasticsearchCriteriaConverter.this::wildcardTransformer);
        put(FilterOperator.NOT_CONTAINS, ElasticsearchCriteriaConverter.this::wildcardTransformer);
    }};

    public SearchSourceBuilder convert(Criteria criteria) {
        SearchSourceBuilder sourceBuilder = new SearchSourceBuilder();

        sourceBuilder.from(criteria.offset().orElse(0));
        sourceBuilder.size(criteria.limit().orElse(1000));

        if (criteria.order().hasOrder()) {
            sourceBuilder.sort(
                criteria.order().orderBy().value(),
                SortOrder.fromString(criteria.order().orderType().value())
            );
        }

        if (criteria.hasFilters()) {
            QueryBuilder queryBuilder = generateQueryBuilder(criteria.filters());

            sourceBuilder.query(queryBuilder);
        }

        return sourceBuilder;
    }

    private QueryBuilder generateQueryBuilder(Filters filters) {
        BoolQueryBuilder boolQueryBuilder = new BoolQueryBuilder();

        for (Filter filter : filters.filters()) {
            QueryBuilder query = queryForFilter(filter);

            if (isPositiveOperator(filter.operator())) {
                boolQueryBuilder.must(query);
            } else {
                boolQueryBuilder.mustNot(query);
            }
        }

        return boolQueryBuilder;
    }

    private boolean isPositiveOperator(FilterOperator operator) {
        return operator.isPositive();
    }

    private QueryBuilder queryForFilter(Filter filter) {
        Function<Filter, QueryBuilder> transformer = queryTransformers.get(filter.operator());

        return transformer.apply(filter);
    }

    private QueryBuilder termQuery(Filter filter) {
        return QueryBuilders.termQuery(filter.field().value(), filter.value().value().toLowerCase());
    }

    private QueryBuilder greaterThanQueryTransformer(Filter filter) {
        return QueryBuilders.rangeQuery(filter.field().value()).gt(filter.value().value().toLowerCase());
    }

    private QueryBuilder lowerThanQueryTransformer(Filter filter) {
        return QueryBuilders.rangeQuery(filter.field().value()).lt(filter.value().value().toLowerCase());
    }

    private QueryBuilder wildcardTransformer(Filter filter) {
        return QueryBuilders.wildcardQuery(
            filter.field().value(),
            String.format("*%s*", filter.value().value().toLowerCase())
        );
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/shared/main/tv/codely/shared/infrastructure/elasticsearch/ElasticsearchRepository.java`
```java
package tv.codely.shared.infrastructure.elasticsearch;

import org.elasticsearch.action.search.SearchRequest;
import org.elasticsearch.action.search.SearchResponse;
import org.elasticsearch.client.RequestOptions;
import org.elasticsearch.search.builder.SearchSourceBuilder;
import tv.codely.shared.domain.criteria.Criteria;

import java.io.IOException;
import java.io.Serializable;
import java.util.*;
import java.util.function.Function;
import java.util.stream.Collectors;

public abstract class ElasticsearchRepository<T> {
    private final ElasticsearchClient            client;
    private final ElasticsearchCriteriaConverter criteriaConverter;

    public ElasticsearchRepository(ElasticsearchClient client) {
        this.client            = client;
        this.criteriaConverter = new ElasticsearchCriteriaConverter();
    }

    abstract protected String moduleName();

    protected List<T> searchAllInElastic(Function<Map<String, Object>, T> unserializer) {
        return searchAllInElastic(unserializer, new SearchSourceBuilder());
    }

    protected List<T> searchAllInElastic(
        Function<Map<String, Object>, T> unserializer,
        SearchSourceBuilder sourceBuilder
    ) {
        SearchRequest request = new SearchRequest(client.indexFor(moduleName())).source(sourceBuilder);
        try {
            SearchResponse response = client.highLevelClient().search(request, RequestOptions.DEFAULT);

            return Arrays.stream(response.getHits().getHits())
                         .map(hit -> unserializer.apply(hit.getSourceAsMap()))
                         .collect(Collectors.toList());
        } catch (IOException e) {
            e.printStackTrace();
        }

        return Collections.emptyList();
    }

    protected List<T> searchByCriteria(Criteria criteria, Function<Map<String, Object>, T> unserializer) {
        return searchAllInElastic(unserializer, criteriaConverter.convert(criteria));
    }

    protected void persist(String id, HashMap<String, Serializable> plainBody) {
        try {
            client.persist(moduleName(), id, plainBody);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/shared/main/tv/codely/shared/infrastructure/hibernate/HibernateConfigurationFactory.java`
```java
package tv.codely.shared.infrastructure.hibernate;

import org.apache.tomcat.dbcp.dbcp2.BasicDataSource;
import org.hibernate.cfg.AvailableSettings;
import org.springframework.core.io.FileSystemResource;
import org.springframework.core.io.Resource;
import org.springframework.core.io.support.ResourcePatternResolver;
import org.springframework.orm.hibernate5.HibernateTransactionManager;
import org.springframework.orm.hibernate5.LocalSessionFactoryBean;
import org.springframework.transaction.PlatformTransactionManager;
import tv.codely.shared.domain.Service;

import javax.sql.DataSource;
import java.io.File;
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.util.*;
import java.util.stream.Collectors;

@Service
public final class HibernateConfigurationFactory {
    private final ResourcePatternResolver resourceResolver;

    public HibernateConfigurationFactory(ResourcePatternResolver resourceResolver) {
        this.resourceResolver = resourceResolver;
    }

    public PlatformTransactionManager hibernateTransactionManager(LocalSessionFactoryBean sessionFactory) {
        HibernateTransactionManager transactionManager = new HibernateTransactionManager();
        transactionManager.setSessionFactory(sessionFactory.getObject());

        return transactionManager;
    }

    public LocalSessionFactoryBean sessionFactory(String contextName, DataSource dataSource) {
        LocalSessionFactoryBean sessionFactory = new LocalSessionFactoryBean();
        sessionFactory.setDataSource(dataSource);
        sessionFactory.setHibernateProperties(hibernateProperties());

        List<Resource> mappingFiles = searchMappingFiles(contextName);

        sessionFactory.setMappingLocations(mappingFiles.toArray(new Resource[mappingFiles.size()]));

        return sessionFactory;
    }

    public DataSource dataSource(
        String host,
        Integer port,
        String databaseName,
        String username,
        String password
    ) throws IOException {
        BasicDataSource dataSource = new BasicDataSource();
        dataSource.setDriverClassName("com.mysql.cj.jdbc.Driver");
        dataSource.setUrl(
            String.format(
                "jdbc:mysql://%s:%s/%s?useUnicode=true&useJDBCCompliantTimezoneShift=true&useLegacyDatetimeCode=false&serverTimezone=UTC",
                host,
                port,
                databaseName
            )
        );
        dataSource.setUsername(username);
        dataSource.setPassword(password);

        Resource mysqlResource = resourceResolver.getResource(String.format(
            "classpath:database/%s.sql",
            databaseName
        ));
        String mysqlSentences = new Scanner(mysqlResource.getInputStream(), StandardCharsets.UTF_8).useDelimiter("\\A").next();

        dataSource.setConnectionInitSqls(new ArrayList<>(Arrays.asList(mysqlSentences.split(";"))));

        return dataSource;
    }

    private List<Resource> searchMappingFiles(String contextName) {
        List<String> modules   = subdirectoriesFor(contextName);
        List<String> goodPaths = new ArrayList<>();

        for (String module : modules) {
            String[] files = mappingFilesIn(module + "/infrastructure/persistence/hibernate/");

            for (String file : files) {
                goodPaths.add(module + "/infrastructure/persistence/hibernate/" + file);
            }
        }

        return goodPaths.stream().map(FileSystemResource::new).collect(Collectors.toList());
    }

    private List<String> subdirectoriesFor(String contextName) {
        String path = "./src/" + contextName + "/main/tv/codely/" + contextName + "/";

        String[] files = new File(path).list((current, name) -> new File(current, name).isDirectory());

        if (null == files) {
            path  = "./main/tv/codely/" + contextName + "/";
            files = new File(path).list((current, name) -> new File(current, name).isDirectory());
        }

        if (null == files) {
            return Collections.emptyList();
        }

        String finalPath = path;

        return Arrays.stream(files).map(file -> finalPath + file).collect(Collectors.toList());
    }

    private String[] mappingFilesIn(String path) {
		List<String> fileList = new ArrayList<>();

		String[] hbmFiles = new File(path).list((current, name) -> new File(current, name).getName().contains(".hbm.xml"));
        String[] ormFiles = new File(path).list((current, name) -> new File(current, name).getName().contains(".orm.xml"));

		if (hbmFiles != null) {
			fileList.addAll(Arrays.asList(hbmFiles));
		}
		if (ormFiles != null) {
			fileList.addAll(Arrays.asList(ormFiles));
		}

		return fileList.toArray(new String[0]);
    }

    private Properties hibernateProperties() {
        Properties hibernateProperties = new Properties();
        hibernateProperties.put(AvailableSettings.HBM2DDL_AUTO, "none");
        hibernateProperties.put(AvailableSettings.SHOW_SQL, "false");
        hibernateProperties.put(AvailableSettings.DIALECT, "org.hibernate.dialect.MySQLDialect");
        hibernateProperties.put(AvailableSettings.TRANSFORM_HBM_XML, true);

        return hibernateProperties;
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/shared/main/tv/codely/shared/infrastructure/hibernate/HibernateCriteriaConverter.java`
```java
package tv.codely.shared.infrastructure.hibernate;

import jakarta.persistence.criteria.*;
import tv.codely.shared.domain.criteria.Criteria;
import tv.codely.shared.domain.criteria.Filter;
import tv.codely.shared.domain.criteria.FilterOperator;

import java.util.HashMap;
import java.util.List;
import java.util.function.BiFunction;
import java.util.stream.Collectors;

public final class HibernateCriteriaConverter<T> {
    private final CriteriaBuilder builder;
    private final HashMap<FilterOperator, BiFunction<Filter, Root<T>, Predicate>> predicateTransformers = new HashMap<FilterOperator, BiFunction<Filter, Root<T>, Predicate>>() {{
        put(FilterOperator.EQUAL, HibernateCriteriaConverter.this::equalsPredicateTransformer);
        put(FilterOperator.NOT_EQUAL, HibernateCriteriaConverter.this::notEqualsPredicateTransformer);
        put(FilterOperator.GT, HibernateCriteriaConverter.this::greaterThanPredicateTransformer);
        put(FilterOperator.LT, HibernateCriteriaConverter.this::lowerThanPredicateTransformer);
        put(FilterOperator.CONTAINS, HibernateCriteriaConverter.this::containsPredicateTransformer);
        put(FilterOperator.NOT_CONTAINS, HibernateCriteriaConverter.this::notContainsPredicateTransformer);
    }};

    public HibernateCriteriaConverter(CriteriaBuilder builder) {
        this.builder = builder;
    }

    public CriteriaQuery<T> convert(Criteria criteria, Class<T> aggregateClass) {
        CriteriaQuery<T> hibernateCriteria = builder.createQuery(aggregateClass);
        Root<T>          root              = hibernateCriteria.from(aggregateClass);

        hibernateCriteria.where(formatPredicates(criteria.filters().filters(), root));

        if (criteria.order().hasOrder()) {
            Path<Object> orderBy = root.get(criteria.order().orderBy().value());
            Order        order   = criteria.order().orderType().isAsc() ? builder.asc(orderBy) : builder.desc(orderBy);

            hibernateCriteria.orderBy(order);
        }

        return hibernateCriteria;
    }

    private Predicate[] formatPredicates(List<Filter> filters, Root<T> root) {
        List<Predicate> predicates = filters.stream().map(filter -> formatPredicate(
            filter,
            root
        )).collect(Collectors.toList());

        Predicate[] predicatesArray = new Predicate[predicates.size()];
        predicatesArray = predicates.toArray(predicatesArray);

        return predicatesArray;
    }

    private Predicate formatPredicate(Filter filter, Root<T> root) {
        BiFunction<Filter, Root<T>, Predicate> transformer = predicateTransformers.get(filter.operator());

        return transformer.apply(filter, root);
    }

    private Predicate equalsPredicateTransformer(Filter filter, Root<T> root) {
        return builder.equal(root.get(filter.field().value()), filter.value().value());
    }

    private Predicate notEqualsPredicateTransformer(Filter filter, Root<T> root) {
        return builder.notEqual(root.get(filter.field().value()), filter.value().value());
    }

    private Predicate greaterThanPredicateTransformer(Filter filter, Root<T> root) {
        return builder.greaterThan(root.get(filter.field().value()), filter.value().value());
    }

    private Predicate lowerThanPredicateTransformer(Filter filter, Root<T> root) {
        return builder.lessThan(root.get(filter.field().value()), filter.value().value());
    }

    private Predicate containsPredicateTransformer(Filter filter, Root<T> root) {
        return builder.like(root.get(filter.field().value()), String.format("%%%s%%", filter.value().value()));
    }

    private Predicate notContainsPredicateTransformer(Filter filter, Root<T> root) {
        return builder.notLike(root.get(filter.field().value()), String.format("%%%s%%", filter.value().value()));
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/shared/main/tv/codely/shared/infrastructure/hibernate/HibernateRepository.java`
```java
package tv.codely.shared.infrastructure.hibernate;

import jakarta.persistence.criteria.CriteriaQuery;
import org.hibernate.SessionFactory;
import tv.codely.shared.domain.Identifier;
import tv.codely.shared.domain.criteria.Criteria;

import java.util.List;
import java.util.Optional;

public abstract class HibernateRepository<T> {
    protected final SessionFactory             sessionFactory;
    protected final Class<T>                   aggregateClass;
    protected final HibernateCriteriaConverter<T> criteriaConverter;

    public HibernateRepository(SessionFactory sessionFactory, Class<T> aggregateClass) {
        this.sessionFactory    = sessionFactory;
        this.aggregateClass    = aggregateClass;
        this.criteriaConverter = new HibernateCriteriaConverter<>(sessionFactory.getCriteriaBuilder());
    }

    protected void persist(T entity) {
        sessionFactory.getCurrentSession().saveOrUpdate(entity);
        sessionFactory.getCurrentSession().flush();
        sessionFactory.getCurrentSession().clear();
    }

    protected Optional<T> byId(Identifier id) {
        return Optional.ofNullable(sessionFactory.getCurrentSession().byId(aggregateClass).load(id));
    }

    protected List<T> byCriteria(Criteria criteria) {
        CriteriaQuery<T> hibernateCriteria = criteriaConverter.convert(criteria, aggregateClass);

        return sessionFactory.getCurrentSession().createQuery(hibernateCriteria).getResultList();
    }

    protected List<T> all() {
        CriteriaQuery<T> criteria = sessionFactory.getCriteriaBuilder().createQuery(aggregateClass);

        criteria.from(aggregateClass);

        return sessionFactory.getCurrentSession().createQuery(criteria).getResultList();
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/shared/main/tv/codely/shared/infrastructure/hibernate/JsonListType.java`
```java
package tv.codely.shared.infrastructure.hibernate;

import com.fasterxml.jackson.annotation.JsonAutoDetect;
import com.fasterxml.jackson.annotation.PropertyAccessor;
import com.fasterxml.jackson.databind.JavaType;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.hibernate.HibernateException;
import org.hibernate.engine.spi.SharedSessionContractImplementor;
import org.hibernate.usertype.DynamicParameterizedType;
import org.hibernate.usertype.UserType;

import java.io.IOException;
import java.io.Serializable;
import java.io.StringWriter;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Types;
import java.util.*;

public class JsonListType implements UserType, DynamicParameterizedType {
    private static final ObjectMapper OBJECT_MAPPER = new ObjectMapper();
    private JavaType valueType = null;
    private Class<?> classType = null;

    @Override
    public int getSqlType() {
        return Types.LONGVARCHAR;
    }

    @Override
    public Class<?> returnedClass() {
        return classType;
    }

    @Override
    public boolean equals(Object x, Object y) throws HibernateException {
        return Objects.equals(x, y);
    }

    @Override
    public int hashCode(Object x) throws HibernateException {
        return Objects.hashCode(x);
    }

    @Override
    public void nullSafeSet(
        PreparedStatement st,
        Object value,
        int index,
        SharedSessionContractImplementor session
    ) throws HibernateException, SQLException {
        nullSafeSet(st, value, index);
    }

	@Override
	public Object nullSafeGet(
		ResultSet resultSet,
		int index,
		SharedSessionContractImplementor session,
		Object owner
	) throws HibernateException, SQLException {

		String value = resultSet.getString(index).replace("\"value\"", "").replace("{:", "").replace("}", "");
		Object result = null;
		if (valueType == null) {
			throw new HibernateException("Value type not set.");
		}
		if (value != null && !value.equals("")) {
			try {
				result = OBJECT_MAPPER.readValue(value, valueType);
			} catch (IOException e) {
				throw new HibernateException("Exception deserializing value " + value, e);
			}
		}
		return result;
	}

    public void nullSafeSet(PreparedStatement st, Object value, int index) throws HibernateException, SQLException {
        StringWriter sw = new StringWriter();
        OBJECT_MAPPER.setVisibility(PropertyAccessor.FIELD, JsonAutoDetect.Visibility.ANY);

        if (value == null) {
            st.setNull(index, Types.VARCHAR);
        } else {
            try {
                OBJECT_MAPPER.writeValue(sw, value);
                st.setString(index, sw.toString());
            } catch (IOException e) {
                throw new HibernateException("Exception serializing value " + value, e);
            }
        }
    }

    @Override
    public Object deepCopy(Object value) throws HibernateException {
        if (value == null) {
            return null;
        } else if (valueType.isCollectionLikeType()) {
            Object newValue = new ArrayList<>();
            Collection newValueCollection = (Collection) newValue;
            newValueCollection.addAll((Collection) value);
            return newValueCollection;
        }

        return null;
    }

    @Override
    public boolean isMutable() {
        return true;
    }

    @Override
    public Serializable disassemble(Object value) throws HibernateException {
        return (Serializable) deepCopy(value);
    }

    @Override
    public Object assemble(Serializable cached, Object owner) throws HibernateException {
        return deepCopy(cached);
    }

    @Override
    public Object replace(Object original, Object target, Object owner) throws HibernateException {
        return deepCopy(original);
    }

    @Override
    public void setParameterValues(Properties parameters) {
        try {
            Class<?> entityClass = Class.forName(parameters.getProperty("list_of"));

            valueType = OBJECT_MAPPER.getTypeFactory().constructCollectionType(ArrayList.class, entityClass);
            classType = List.class;
        } catch (ClassNotFoundException e) {
            throw new IllegalArgumentException(e);
        }
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/shared/main/tv/codely/shared/infrastructure/spring/ApiController.java`
```java
package tv.codely.shared.infrastructure.spring;

import org.springframework.http.HttpStatus;
import tv.codely.shared.domain.DomainError;
import tv.codely.shared.domain.bus.command.Command;
import tv.codely.shared.domain.bus.command.CommandBus;
import tv.codely.shared.domain.bus.command.CommandHandlerExecutionError;
import tv.codely.shared.domain.bus.query.Query;
import tv.codely.shared.domain.bus.query.QueryBus;
import tv.codely.shared.domain.bus.query.QueryHandlerExecutionError;

import java.util.HashMap;

public abstract class ApiController {
    private final QueryBus   queryBus;
    private final CommandBus commandBus;

    public ApiController(QueryBus queryBus, CommandBus commandBus) {
        this.queryBus   = queryBus;
        this.commandBus = commandBus;
    }

    protected void dispatch(Command command) throws CommandHandlerExecutionError {
        commandBus.dispatch(command);
    }

    protected <R> R ask(Query query) throws QueryHandlerExecutionError {
        return queryBus.ask(query);
    }

    abstract public HashMap<Class<? extends DomainError>, HttpStatus> errorMapping();
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/shared/main/tv/codely/shared/infrastructure/spring/ApiExceptionMiddleware.java`
```java
package tv.codely.shared.infrastructure.spring;

import org.springframework.http.HttpStatus;
import org.springframework.web.method.HandlerMethod;
import org.springframework.web.servlet.mvc.method.annotation.RequestMappingHandlerMapping;
import org.springframework.web.util.NestedServletException;
import tv.codely.shared.domain.DomainError;
import tv.codely.shared.domain.Utils;
import tv.codely.shared.domain.bus.command.CommandHandlerExecutionError;
import tv.codely.shared.domain.bus.query.QueryHandlerExecutionError;

import jakarta.servlet.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.HashMap;
import java.util.Objects;

public final class ApiExceptionMiddleware implements Filter {
    private RequestMappingHandlerMapping mapping;

    public ApiExceptionMiddleware(RequestMappingHandlerMapping mapping) {
        this.mapping = mapping;
    }

    @Override
    public void doFilter(
        ServletRequest request,
        ServletResponse response,
        FilterChain chain
    ) throws ServletException {
        HttpServletRequest  httpRequest  = ((HttpServletRequest) request);
        HttpServletResponse httpResponse = ((HttpServletResponse) response);

        try {
            Object possibleController = (
                (HandlerMethod) Objects.requireNonNull(
                    mapping.getHandler(httpRequest)).getHandler()
            ).getBean();

            try {
                chain.doFilter(request, response);
            } catch (Exception exception) {
                if (possibleController instanceof ApiController) {
                    handleCustomError(response, httpResponse, (ApiController) possibleController, exception);
                }
            }
        } catch (Exception e) {
            throw new ServletException(e);
        }
    }

    private void handleCustomError(
        ServletResponse response,
        HttpServletResponse httpResponse,
        ApiController possibleController,
        Exception exception
    ) throws IOException {
        HashMap<Class<? extends DomainError>, HttpStatus> errorMapping = possibleController
            .errorMapping();
        Throwable error = (
            exception.getCause() instanceof CommandHandlerExecutionError ||
            exception.getCause() instanceof QueryHandlerExecutionError
        )
            ? exception.getCause().getCause() : exception.getCause();

        int    statusCode   = statusFor(errorMapping, error);
        String errorCode    = errorCodeFor(error);
        String errorMessage = error.getMessage();

        httpResponse.reset();
        httpResponse.setHeader("Content-Type", "application/json");
        httpResponse.setStatus(statusCode);
        PrintWriter writer = response.getWriter();
        writer.write(String.format(
            "{\"error_code\": \"%s\", \"message\": \"%s\"}",
            errorCode,
            errorMessage
        ));
        writer.close();
    }

    private String errorCodeFor(Throwable error) {
        if (error instanceof DomainError) {
            return ((DomainError) error).errorCode();
        }

        return Utils.toSnake(error.getClass().toString());
    }

    private int statusFor(HashMap<Class<? extends DomainError>, HttpStatus> errorMapping, Throwable error) {
        return errorMapping.getOrDefault(error.getClass(), HttpStatus.INTERNAL_SERVER_ERROR).value();
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/shared/main/tv/codely/shared/infrastructure/validation/ValidationResponse.java`
```java
package tv.codely.shared.infrastructure.validation;

import java.util.HashMap;
import java.util.List;

public final class ValidationResponse {
    private HashMap<String, List<String>> validationErrors;

    public ValidationResponse(HashMap<String, List<String>> validationErrors) {
        this.validationErrors = validationErrors;
    }

    public Boolean hasErrors() {
        return !validationErrors.isEmpty();
    }

    public HashMap<String, List<String>> errors() {
        return validationErrors;
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/shared/main/tv/codely/shared/infrastructure/validation/Validator.java`
```java
package tv.codely.shared.infrastructure.validation;

import tv.codely.shared.infrastructure.validation.validators.*;

import java.io.Serializable;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public final class Validator {
    private static final HashMap<String, FieldValidator> validators = new HashMap<String, FieldValidator>() {{
        put("required", new RequiredValidator());
        put("string", new StringValidator());
        put("not_empty", new NotEmptyValidator());
        put("uuid", new UuidValidator());
    }};

    public static ValidationResponse validate(
        HashMap<String, Serializable> input,
        HashMap<String, String> combinedRules
    ) throws ValidatorNotExist {
        HashMap<String, List<String>> validationErrors = new HashMap<>();

        for (Map.Entry<String, String> entry : combinedRules.entrySet()) {
            String[] rules = entry.getValue().split("\\|");

            for (String rule : rules) {
                FieldValidator validator = validators.get(rule);

                if (null == validator) {
                    throw new ValidatorNotExist(rule);
                }

                if (!validator.isValid(entry.getKey(), input)) {
                    List<String> existingErrors = validationErrors.getOrDefault(entry.getKey(), new ArrayList<>());
                    existingErrors.add(validator.errorMessage(entry.getKey()));

                    validationErrors.put(entry.getKey(), existingErrors);
                }
            }
        }

        return new ValidationResponse(validationErrors);
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/shared/main/tv/codely/shared/infrastructure/validation/ValidatorNotExist.java`
```java
package tv.codely.shared.infrastructure.validation;

public final class ValidatorNotExist extends Exception {
    public ValidatorNotExist(String name) {
        super(String.format("The validator <%s> does not exist", name));
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/shared/main/tv/codely/shared/infrastructure/validation/validators/FieldValidator.java`
```java
package tv.codely.shared.infrastructure.validation.validators;

import java.io.Serializable;
import java.util.HashMap;

public interface FieldValidator {
    Boolean isValid(String fieldName, HashMap<String, Serializable> fields);

    String errorMessage(String fieldName);
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/shared/main/tv/codely/shared/infrastructure/validation/validators/NotEmptyValidator.java`
```java
package tv.codely.shared.infrastructure.validation.validators;

import java.io.Serializable;
import java.util.HashMap;

public final class NotEmptyValidator implements FieldValidator {
    @Override
    public Boolean isValid(String fieldName, HashMap<String, Serializable> fields) {
        return !fields.get(fieldName).toString().isEmpty();
    }

    @Override
    public String errorMessage(String fieldName) {
        return String.format("The field <%s> should not be empty", fieldName);
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/shared/main/tv/codely/shared/infrastructure/validation/validators/RequiredValidator.java`
```java
package tv.codely.shared.infrastructure.validation.validators;

import java.io.Serializable;
import java.util.HashMap;

public final class RequiredValidator implements FieldValidator {
    @Override
    public Boolean isValid(String fieldName, HashMap<String, Serializable> fields) {
        return fields.containsKey(fieldName);
    }

    @Override
    public String errorMessage(String fieldName) {
        return String.format("The field <%s> is required", fieldName);
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/shared/main/tv/codely/shared/infrastructure/validation/validators/StringValidator.java`
```java
package tv.codely.shared.infrastructure.validation.validators;

import java.io.Serializable;
import java.util.HashMap;

public final class StringValidator implements FieldValidator {
    @Override
    public Boolean isValid(String fieldName, HashMap<String, Serializable> fields) {
        return true;
    }

    @Override
    public String errorMessage(String fieldName) {
        return String.format("The field <%s> should be of type string", fieldName);
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/shared/main/tv/codely/shared/infrastructure/validation/validators/UuidValidator.java`
```java
package tv.codely.shared.infrastructure.validation.validators;

import java.io.Serializable;
import java.util.HashMap;
import java.util.regex.Pattern;

public final class UuidValidator implements FieldValidator {
    @Override
    public Boolean isValid(String fieldName, HashMap<String, Serializable> fields) {
        Pattern uuidPattern = Pattern.compile("[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$");

        return uuidPattern.matcher((String) fields.get(fieldName)).matches();
    }

    @Override
    public String errorMessage(String fieldName) {
        return String.format("The field <%s> is not a valid uuid", fieldName);
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/shared/test/tv/codely/shared/domain/EmailMother.java`
```java
package tv.codely.shared.domain;

public final class EmailMother {
    public static String random() {
        return MotherCreator.random().internet().emailAddress();
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/shared/test/tv/codely/shared/domain/IntegerMother.java`
```java
package tv.codely.shared.domain;

public final class IntegerMother {
    public static Integer random() {
        return MotherCreator.random().number().randomDigit();
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/shared/test/tv/codely/shared/domain/ListMother.java`
```java
package tv.codely.shared.domain;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.function.Supplier;

public final class ListMother {
    public static <T> List<T> create(Integer size, Supplier<T> creator) {
        ArrayList<T> list = new ArrayList<>();

        for (int i = 0; i < size; i++) {
            list.add(creator.get());
        }

        return list;
    }

    public static <T> List<T> random(Supplier<T> creator) {
        return create(IntegerMother.random(), creator);
    }

    public static <T> List<T> one(T element) {
        return Collections.singletonList(element);
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/shared/test/tv/codely/shared/domain/MotherCreator.java`
```java
package tv.codely.shared.domain;

import com.github.javafaker.Faker;

public final class MotherCreator {
    private final static Faker faker = new Faker();

    public static Faker random() {
        return faker;
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/shared/test/tv/codely/shared/domain/RandomElementPicker.java`
```java
package tv.codely.shared.domain;

import java.util.Random;

public final class RandomElementPicker {
    @SafeVarargs
    public static <T> T from(T... elements) {
        Random rand = new Random();

        return elements[rand.nextInt(elements.length)];
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/shared/test/tv/codely/shared/domain/UuidMother.java`
```java
package tv.codely.shared.domain;

import java.util.UUID;

public final class UuidMother {
    public static String random() {
        return UUID.randomUUID().toString();
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/shared/test/tv/codely/shared/domain/VideoUrlMother.java`
```java
package tv.codely.shared.domain;

public final class VideoUrlMother {
    public static VideoUrl create(String value) {
        return new VideoUrl(value);
    }

    public static VideoUrl random() {
        return create(MotherCreator.random().internet().url());
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/shared/test/tv/codely/shared/domain/WordMother.java`
```java
package tv.codely.shared.domain;

public final class WordMother {
    public static String random() {
        return MotherCreator.random().lorem().word();
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/shared/test/tv/codely/shared/infrastructure/InfrastructureTestCase.java`
```java
package tv.codely.shared.infrastructure;

public abstract class InfrastructureTestCase {
    private final int MAX_ATTEMPTS                   = 3;
    private final int MILLIS_TO_WAIT_BETWEEN_RETRIES = 300;

    protected void eventually(Runnable assertion) throws Exception {
        int     attempts = 0;
        boolean allOk    = false;

        while (attempts < MAX_ATTEMPTS && !allOk) {
            try {
                assertion.run();

                allOk = true;
            } catch (Throwable error) {
                attempts++;

                if (attempts > MAX_ATTEMPTS) {
                    throw new Exception(
                        String.format("Could not assert after some retries. Last error: %s", error.getMessage())
                    );
                }

                Thread.sleep(MILLIS_TO_WAIT_BETWEEN_RETRIES);
            }
        }
    }
}
```

## File: `CodelyTV-java-ddd-example-3a58e32/src/shared/test/tv/codely/shared/infrastructure/UnitTestCase.java`
```java
package tv.codely.shared.infrastructure;

import org.junit.jupiter.api.BeforeEach;
import tv.codely.shared.domain.UuidGenerator;
import tv.codely.shared.domain.bus.event.DomainEvent;
import tv.codely.shared.domain.bus.event.EventBus;
import tv.codely.shared.domain.bus.query.*;

import java.util.Collections;
import java.util.List;

import static org.mockito.Mockito.*;

public abstract class UnitTestCase {
    protected EventBus      eventBus;
    protected QueryBus      queryBus;
    protected UuidGenerator uuidGenerator;

    @BeforeEach
    protected void setUp() {
        eventBus      = mock(EventBus.class);
        queryBus      = mock(QueryBus.class);
        uuidGenerator = mock(UuidGenerator.class);
    }

    public void shouldHavePublished(List<DomainEvent> domainEvents) {
        verify(eventBus, atLeastOnce()).publish(domainEvents);
    }

    public void shouldHavePublished(DomainEvent domainEvent) {
        shouldHavePublished(Collections.singletonList(domainEvent));
    }

    public void shouldGenerateUuid(String uuid) {
        when(uuidGenerator.generate()).thenReturn(uuid);
    }

    public void shouldGenerateUuids(String uuid, String... others) {
        when(uuidGenerator.generate()).thenReturn(uuid, others);
    }

    public void shouldAsk(Query query, Response response) {
        when(queryBus.ask(query)).thenReturn(response);
    }
}
```

## File: `apps/main/resources/.env`
```
#              MOOC              #
#--------------------------------#
MOOC_BACKEND_SERVER_PORT=8030
# MySql
MOOC_DATABASE_HOST=codely-java_ddd_example-mysql
MOOC_DATABASE_PORT=3306
MOOC_DATABASE_NAME=mooc
MOOC_DATABASE_USER=root
MOOC_DATABASE_PASSWORD=

#           BACKOFFICE           #
#--------------------------------#
BACKOFFICE_BACKEND_SERVER_PORT=8040
BACKOFFICE_FRONTEND_SERVER_PORT=8041
# MySql
BACKOFFICE_DATABASE_HOST=codely-java_ddd_example-mysql
BACKOFFICE_DATABASE_PORT=3306
BACKOFFICE_DATABASE_NAME=backoffice
BACKOFFICE_DATABASE_USER=root
BACKOFFICE_DATABASE_PASSWORD=
# Elasticsearch
BACKOFFICE_ELASTICSEARCH_HOST=codely-java_ddd_example-elasticsearch
BACKOFFICE_ELASTICSEARCH_PORT=9200
BACKOFFICE_ELASTICSEARCH_INDEX_PREFIX=backoffice

#             COMMON             #
#--------------------------------#
# RabbitMQ
RABBITMQ_HOST=codely-java_ddd_example-rabbitmq
RABBITMQ_PORT=5672
RABBITMQ_LOGIN=codely
RABBITMQ_PASSWORD=c0d3ly
RABBITMQ_EXCHANGE=domain_events
RABBITMQ_MAX_RETRIES=5
```

## File: `apps/main/resources/log4j2.properties`
```
name                                            = CodelyTvJavaDddExample
property.filename                               = logs
appenders                                       = console, file

status                                          = warn

appender.console.name                           = CONSOLE
appender.console.type                           = CONSOLE
appender.console.target                         = SYSTEM_OUT

appender.console.logstash.type                  = LogstashLayout
appender.console.logstash.dateTimeFormatPattern = yyyy-MM-dd'T'HH:mm:ss.SSSZZZ
appender.console.logstash.eventTemplateUri      = classpath:LogstashJsonEventLayoutV1.json
appender.console.logstash.prettyPrintEnabled    = true
appender.console.logstash.stackTraceEnabled     = true

appender.file.type                              = File
appender.file.name                              = LOGFILE
appender.file.fileName                          = var/log/java-ddd-example.log
appender.file.logstash.type                     = LogstashLayout
appender.file.logstash.dateTimeFormatPattern    = yyyy-MM-dd'T'HH:mm:ss.SSSZZZ
appender.file.logstash.eventTemplateUri         = classpath:LogstashJsonEventLayoutV1.json
appender.file.logstash.prettyPrintEnabled       = false
appender.file.logstash.stackTraceEnabled        = true

loggers                                         = file
logger.file.name                                = tv.codely.java_ddd_example
logger.file.level                               = info
logger.file.appenderRefs                        = file
logger.file.appenderRef.file.ref                = LOGFILE

rootLogger.level                                = info
rootLogger.appenderRefs                         = stdout
rootLogger.appenderRef.stdout.ref               = CONSOLE
```

## File: `apps/main/resources/backoffice_frontend/templates/master.ftl`
```
<#import "spring.ftl" as spring />

<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link href="https://unpkg.com/tailwindcss@^1.0/dist/tailwind.min.css" rel="stylesheet">

    <title>${title}</title>
    <title>${description}</title>
</head>
<body>
<#include "partials/header.ftl">

<div class="container mx-auto px-4 p-5">
    <h1 class="font-sans text-gray-800 text-center text-5xl mb-10"><@page_title/></h1>
    <@main/>
</div>

<div class="clearfix"></div>

<#include "partials/footer.ftl">
</body>
</html>
```

## File: `apps/main/resources/backoffice_frontend/templates/pages/home.ftl`
```
<#include "../master.ftl">

<#macro page_title>HOME</#macro>

<#macro main>
    Estamos en la home!
</#macro>
```

## File: `apps/main/resources/backoffice_frontend/templates/pages/courses/courses.ftl`
```
<#include "../../master.ftl">

<#macro page_title>Cursos</#macro>

<#macro main>
    <div class="max-w-sm rounded overflow-hidden shadow-lg float-left">
        <img class="w-full" src="https://codely.tv/pro/img/bg/cursos-codelytv-pro.png" alt="Sunset in the mountains">
        <div class="px-6 py-4">
            <div class="font-bold text-xl mb-2">Cursos</div>
            <p class="text-gray-700 text-base">
                Actualmente CodelyTV Pro cuenta con <b>${courses_counter}</b> cursos.
            </p>
        </div>
    </div>

    <#include "partials/new_course_form.ftl">
    <div class="clearfix mb-10"></div>
    <hr class="mb-10">
    <#include "partials/list_courses.ftl">
</#macro>
```

## File: `apps/main/resources/backoffice_frontend/templates/pages/courses/partials/list_courses.ftl`
```
<h3 class="font-sans text-gray-800 text-center text-3xl mb-10">Cursos existentes</h3>


<form action="" method="get" id="courses-filters" name="filter-courses">
    <div id="filter-rows">

    </div>
    <div class="clearfix"></div>
    <div class="mt-10 inline-block relative w-2/4">
        <button class="md:w-1/4 bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
                id="add-field-button"
                onclick="addFilter(event)">
            Añadir filtro
        </button>

        <button class="md:w-1/4 bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
                id="filter-button"
                onclick="filterCourses(event)">
            👉 Filtrar 👈
        </button>
    </div>
</form>
<table class="text-left w-full border-collapse">
    <thead>
    <tr>
        <th class="py-4 px-6 bg-grey-lightest font-bold uppercase text-sm text-grey-dark border-b border-grey-light">
            Id
        </th>
        <th class="py-4 px-6 bg-grey-lightest font-bold uppercase text-sm text-grey-dark border-b border-grey-light">
            Nombre
        </th>
        <th class="py-4 px-6 bg-grey-lightest font-bold uppercase text-sm text-grey-dark border-b border-grey-light">
            Duración
        </th>
    </tr>
    </thead>
    <tbody id="courses-list">

    </tbody>
</table>

<script>


    function addCoursesList(url) {
        console.log(url);

        const tableBody = document.getElementById("courses-list");

        fetch(encodeURI(url))
            .then(function (response) {
                return response.json();
            })
            .then(function (courses) {
                tableBody.innerHTML = "";

                courses.forEach(function (course) {
                    let courseRow = document.createElement("tr");

                    courseRow.appendChild(tableCellFor(course.id));
                    courseRow.appendChild(tableCellFor(course.name));
                    courseRow.appendChild(tableCellFor(course.duration));

                    tableBody.appendChild(courseRow);
                })
            });
    }

    function tableCellFor(text) {
        const cell = document.createElement("td");

        cell.appendChild(document.createTextNode(text));

        return cell;
    }

    function addFilter(e) {
        e.preventDefault();

        const filterRows = document.getElementById('filter-rows');
        const totalRows  = document.getElementById('filter-rows').childElementCount;

        const filterRowTemplate = "<div class=\"filter-row\">\n" +
                                  "    <div class=\"inline-block relative w-64 mr-3\">\n" +
                                  "        <label class=\"block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2\" for=\"field\">\n" +
                                  "            Campo\n" +
                                  "        </label>\n" +
                                  "        <select name=\"filters[" +
                                  totalRows +
                                  "][field]\" id=\"field\"\n" +
                                  "                class=\"block appearance-none w-full bg-white border border-gray-400 hover:border-gray-500 px-4 py-2 pr-8 rounded shadow leading-tight focus:outline-none focus:shadow-outline\">\n" +
                                  "            <option value=\"id\">Identificador</option>\n" +
                                  "            <option value=\"name\">Nombre</option>\n" +
                                  "            <option value=\"duration\">Duración</option>\n" +
                                  "        </select>\n" +
                                  "        <div class=\"pointer-events-none absolute inset-y-0 right-0 flex items-center px-2 text-gray-700\">\n" +
                                  "            <svg class=\"fill-current h-4 w-4\" xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 20 20\">\n" +
                                  "                <path d=\"M9.293 12.95l.707.707L15.657 8l-1.414-1.414L10 10.828 5.757 6.586 4.343 8z\"/>\n" +
                                  "            </svg>\n" +
                                  "        </div>\n" +
                                  "    </div>\n" +
                                  "    <div class=\"inline-block relative w-64 mr-3\">\n" +
                                  "        <label class=\"block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2\" for=\"operator\">\n" +
                                  "            Operador\n" +
                                  "        </label>\n" +
                                  "        <select id=\"operator\" name=\"filters[" +
                                  totalRows +
                                  "][operator]\"\n" +
                                  "                class=\"block appearance-none w-full bg-white border border-gray-400 hover:border-gray-500 px-4 py-2 pr-8 rounded shadow leading-tight focus:outline-none focus:shadow-outline\">\n" +
                                  "            <option value=\"=\">es exactamente igual</option>\n" +
                                  "            <option value=\"CONTAINS\">contiene</option>\n" +
                                  "            <option value=\">\">es más grande que</option>\n" +
                                  "            <option value=\"<\">es más pequeño que</option>\n" +
                                  "        </select>\n" +
                                  "        <div class=\"pointer-events-none absolute inset-y-0 right-0 flex items-center px-2 text-gray-700\">\n" +
                                  "            <svg class=\"fill-current h-4 w-4\" xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 20 20\">\n" +
                                  "                <path d=\"M9.293 12.95l.707.707L15.657 8l-1.414-1.414L10 10.828 5.757 6.586 4.343 8z\"/>\n" +
                                  "            </svg>\n" +
                                  "        </div>\n" +
                                  "    </div>\n" +
                                  "    <div class=\"inline-block relative w-64 mr-3\">\n" +
                                  "        <label class=\"block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2\" for=\"value\">\n" +
                                  "            Valor\n" +
                                  "        </label>\n" +
                                  "        <input class=\"appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500\"\n" +
                                  "               id=\"value\" type=\"text\" name=\"filters[" +
                                  totalRows +
                                  "][value]\" placeholder=\"Lo que sea...\">\n" +
                                  "    </div>\n" +
                                  "</div>";

        filterRows.insertAdjacentHTML('beforeend', filterRowTemplate);
    }

    function filterCourses(e) {
        e.preventDefault();

        const form = document.forms["filter-courses"];

        const inputs = Array.from(form.getElementsByTagName("input"))
                            .concat(Array.from(form.getElementsByTagName("select")));

        const urlParts = inputs.map(input => input.name + "=" + input.value);

        const url = "http://localhost:8091/courses?" + urlParts.join("&");

        addCoursesList(url);
    }
</script>

<script>
    addCoursesList("http://localhost:8091/courses");
</script>
```

## File: `apps/main/resources/backoffice_frontend/templates/pages/courses/partials/new_course_form.ftl`
```
<form class="w-full max-w-lg float-right" method="post" action="/courses">
    <h2 class="block uppercase tracking-wide text-gray-700 text-3xl font-bold mb-2">Crear curso</h2>
    <div class="flex flex-wrap mb-6 -mx-3">
        <div class="w-full md:w-full px-3 mb-6 md:mb-0">
            <label class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" for="grid-first-name">
                Identificador
            </label>
            <input class="<#if errors['id']?? >border border-red-500</#if> appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
                   id="grid-first-name" type="text" name="id" placeholder="En formado UUID"
                   value="${(inputs['id'])!generated_uuid}">

            <#if errors['id']?? >
                <#list errors['id'] as errorMessage>
                    <p class="text-red-500 text-xs italic">${errorMessage}</p>
                </#list>
            </#if>
        </div>
    </div>
    <div class="flex flex-wrap -mx-3 mb-6">
        <div class="w-full md:w-1/2 px-3 mb-6 md:mb-0">
            <label class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" for="grid-first-name">
                Nombre
            </label>
            <input class="<#if errors['name']?? >border border-red-500</#if> appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
                   id="grid-first-name" type="text" name="name" placeholder="DDD en PHP"
                   value="${(inputs['name'])!""}">

            <#if errors['name']?? >
                <#list errors['name'] as errorMessage>
                    <p class="text-red-500 text-xs italic">${errorMessage}</p>
                </#list>
            </#if>
        </div>
        <div class="w-full md:w-1/2 px-3">
            <label class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" for="grid-last-name">
                Duración (en inglés)
            </label>
            <input class="<#if errors['duration']?? >border border-red-500</#if> appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
                   id="grid-last-name" type="text" name="duration" placeholder="8 days"
                   value="${(inputs['duration'])!""}">
            <#if errors['duration']?? >
                <#list errors['duration'] as errorMessage>
                    <p class="text-red-500 text-xs italic">${errorMessage}</p>
                </#list>
            </#if>
        </div>
    </div>
    <div class="flex flex-wrap mb-6">
        <button class="md:w-full bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
                type="submit">
            Crear curso!
        </button>
    </div>
</form>
```

## File: `apps/main/resources/backoffice_frontend/templates/partials/footer.ftl`
```
<footer class="flex items-center justify-between flex-wrap bg-teal-900 p-5 mt-10">
    <div class="container mx-auto px-4">
        <p class="text-teal-200">
            🤙 CodelyTV - El mejor backoffice de la historia
        </p>
    </div>
</footer>
```

## File: `apps/main/resources/backoffice_frontend/templates/partials/header.ftl`
```
<header>
    <nav class="flex items-center justify-between flex-wrap bg-teal-900 p-5">
        <div class="flex items-center flex-shrink-0 text-white mr-6">
            <a href="/">
                <img src="images/logo.png" alt="" width="150px">
            </a>
        </div>
        <div class="w-full block flex-grow lg:flex lg:items-center lg:w-auto">
            <div class="text-sm lg:flex-grow">
                <a href="#"
                   class="block mt-4 lg:inline-block lg:mt-0 text-teal-200 hover:text-white mr-4">
                    Usuarios
                </a>
                <a href="/courses"
                   class="block mt-4 lg:inline-block lg:mt-0 text-teal-200 hover:text-white mr-4">
                    Cursos
                </a>
                <a href="#" class="block mt-4 lg:inline-block lg:mt-0 text-teal-200 hover:text-white">
                    Vídeos
                </a>
            </div>
            <div>
                <a href="#"
                   class="inline-block text-sm px-4 py-2 leading-none border rounded text-white border-white hover:border-transparent hover:text-teal-500 hover:bg-white mt-4 lg:mt-0">Entrar</a>
            </div>
        </div>
    </nav>
</header>
```

## File: `apps/main/tv/codely/apps/Starter.java`
```java
package tv.codely.apps;

import java.util.Arrays;
import java.util.HashMap;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.WebApplicationType;
import org.springframework.context.ConfigurableApplicationContext;

import tv.codely.apps.backoffice.backend.BackofficeBackendApplication;
import tv.codely.apps.backoffice.frontend.BackofficeFrontendApplication;
import tv.codely.apps.mooc.backend.MoocBackendApplication;
import tv.codely.shared.infrastructure.cli.ConsoleCommand;

public class Starter {

	public static void main(String[] args) {
		if (args.length < 2) {
			throw new RuntimeException("There are not enough arguments");
		}

		String applicationName = args[0];
		String commandName = args[1];
		boolean isServerCommand = commandName.equals("server");

		ensureApplicationExist(applicationName);
		ensureCommandExist(applicationName, commandName);

		Class<?> applicationClass = applications().get(applicationName);

		SpringApplication app = new SpringApplication(applicationClass);

		if (!isServerCommand) {
			app.setWebApplicationType(WebApplicationType.NONE);
		}

		ConfigurableApplicationContext context = app.run(args);

		if (!isServerCommand) {
			ConsoleCommand command = (ConsoleCommand) context.getBean(commands().get(applicationName).get(commandName));

			command.execute(Arrays.copyOfRange(args, 2, args.length));
		}
	}

	private static void ensureApplicationExist(String applicationName) {
		if (!applications().containsKey(applicationName)) {
			throw new RuntimeException(
				String.format(
					"The application <%s> doesn't exist. Valids:\n- %s",
					applicationName,
					String.join("\n- ", applications().keySet())
				)
			);
		}
	}

	private static void ensureCommandExist(String applicationName, String commandName) {
		if (!"server".equals(commandName) && !existCommand(applicationName, commandName)) {
			throw new RuntimeException(
				String.format(
					"The command <%s> for application <%s> doesn't exist. Valids (application.command):\n- api\n- %s",
					commandName,
					applicationName,
					String.join("\n- ", commands().get(applicationName).keySet())
				)
			);
		}
	}

	private static HashMap<String, Class<?>> applications() {
		HashMap<String, Class<?>> applications = new HashMap<>();

		applications.put("mooc_backend", MoocBackendApplication.class);
		applications.put("backoffice_backend", BackofficeBackendApplication.class);
		applications.put("backoffice_frontend", BackofficeFrontendApplication.class);

		return applications;
	}

	private static HashMap<String, HashMap<String, Class<?>>> commands() {
		HashMap<String, HashMap<String, Class<?>>> commands = new HashMap<>();

		commands.put("mooc_backend", MoocBackendApplication.commands());
		commands.put("backoffice_backend", BackofficeBackendApplication.commands());
		commands.put("backoffice_frontend", BackofficeFrontendApplication.commands());

		return commands;
	}

	private static Boolean existCommand(String applicationName, String commandName) {
		HashMap<String, HashMap<String, Class<?>>> commands = commands();

		return commands.containsKey(applicationName) && commands.get(applicationName).containsKey(commandName);
	}
}
```

## File: `apps/main/tv/codely/apps/backoffice/backend/BackofficeBackendApplication.java`
```java
package tv.codely.apps.backoffice.backend;

import java.util.HashMap;

import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.autoconfigure.orm.jpa.HibernateJpaAutoConfiguration;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.FilterType;

import tv.codely.shared.domain.Service;

@SpringBootApplication(exclude = HibernateJpaAutoConfiguration.class)
@ComponentScan(
	includeFilters = @ComponentScan.Filter(type = FilterType.ANNOTATION, classes = Service.class),
	value = { "tv.codely.shared", "tv.codely.backoffice", "tv.codely.apps.backoffice.backend" }
)
public class BackofficeBackendApplication {

	public static HashMap<String, Class<?>> commands() {
		return new HashMap<String, Class<?>>() {
			{}
		};
	}
}
```

## File: `apps/main/tv/codely/apps/backoffice/backend/config/BackofficeBackendServerConfiguration.java`
```java
package tv.codely.apps.backoffice.backend.config;

import org.springframework.boot.web.servlet.FilterRegistrationBean;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import tv.codely.apps.backoffice.backend.middleware.BasicHttpAuthMiddleware;
import tv.codely.shared.domain.bus.command.CommandBus;

@Configuration
public class BackofficeBackendServerConfiguration {

	private final CommandBus bus;

	public BackofficeBackendServerConfiguration(CommandBus bus) {
		this.bus = bus;
	}

	@Bean
	public FilterRegistrationBean<BasicHttpAuthMiddleware> basicHttpAuthMiddleware() {
		FilterRegistrationBean<BasicHttpAuthMiddleware> registrationBean = new FilterRegistrationBean<>();

		registrationBean.setFilter(new BasicHttpAuthMiddleware(bus));
		registrationBean.addUrlPatterns("/health-check");

		return registrationBean;
	}
}
```

## File: `apps/main/tv/codely/apps/backoffice/backend/config/BackofficeBackendServerPortCustomizer.java`
```java
package tv.codely.apps.backoffice.backend.config;

import org.springframework.boot.web.server.ConfigurableWebServerFactory;
import org.springframework.boot.web.server.WebServerFactoryCustomizer;
import org.springframework.stereotype.Component;

import tv.codely.shared.infrastructure.config.Parameter;
import tv.codely.shared.infrastructure.config.ParameterNotExist;

@Component
public final class BackofficeBackendServerPortCustomizer
	implements WebServerFactoryCustomizer<ConfigurableWebServerFactory> {

	private final Parameter param;

	public BackofficeBackendServerPortCustomizer(Parameter param) {
		this.param = param;
	}

	@Override
	public void customize(ConfigurableWebServerFactory factory) {
		try {
			factory.setPort(param.getInt("BACKOFFICE_BACKEND_SERVER_PORT"));
		} catch (ParameterNotExist parameterNotExist) {
			parameterNotExist.printStackTrace();
		}
	}
}
```

## File: `apps/main/tv/codely/apps/backoffice/backend/controller/courses/CoursesGetController.java`
```java
package tv.codely.apps.backoffice.backend.controller.courses;

import java.io.Serializable;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Optional;
import java.util.stream.Collectors;

import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.*;

import tv.codely.backoffice.courses.application.BackofficeCoursesResponse;
import tv.codely.backoffice.courses.application.search_by_criteria.SearchBackofficeCoursesByCriteriaQuery;
import tv.codely.shared.domain.DomainError;
import tv.codely.shared.domain.bus.command.CommandBus;
import tv.codely.shared.domain.bus.query.QueryBus;
import tv.codely.shared.domain.bus.query.QueryHandlerExecutionError;
import tv.codely.shared.infrastructure.spring.ApiController;

@RestController
@CrossOrigin(origins = "*", methods = { RequestMethod.GET })
public final class CoursesGetController extends ApiController {

	public CoursesGetController(QueryBus queryBus, CommandBus commandBus) {
		super(queryBus, commandBus);
	}

	@GetMapping("/courses")
	public List<HashMap<String, String>> index(@RequestParam HashMap<String, Serializable> params)
		throws QueryHandlerExecutionError {
		BackofficeCoursesResponse courses = ask(
			new SearchBackofficeCoursesByCriteriaQuery(
				parseFilters(params),
				Optional.ofNullable((String) params.get("order_by")),
				Optional.ofNullable((String) params.get("order")),
				Optional.ofNullable((Integer) params.get("limit")),
				Optional.ofNullable((Integer) params.get("offset"))
			)
		);

		return courses
			.courses()
			.stream()
			.map(response ->
				new HashMap<String, String>() {
					{
						put("id", response.id());
						put("name", response.name());
						put("duration", response.duration());
					}
				}
			)
			.collect(Collectors.toList());
	}

	@Override
	public HashMap<Class<? extends DomainError>, HttpStatus> errorMapping() {
		return null;
	}

	private List<HashMap<String, String>> parseFilters(HashMap<String, Serializable> params) {
		int maxParams = params.size();

		List<HashMap<String, String>> filters = new ArrayList<>();

		for (int possibleFilterKey = 0; possibleFilterKey < maxParams; possibleFilterKey++) {
			if (params.containsKey(String.format("filters[%s][field]", possibleFilterKey))) {
				int key = possibleFilterKey;

				filters.add(
					new HashMap<String, String>() {
						{
							put("field", (String) params.get(String.format("filters[%s][field]", key)));
							put("operator", (String) params.get(String.format("filters[%s][operator]", key)));
							put("value", (String) params.get(String.format("filters[%s][value]", key)));
						}
					}
				);
			}
		}

		return filters;
	}
}
```

## File: `apps/main/tv/codely/apps/backoffice/backend/controller/health_check/HealthCheckGetController.java`
```java
package tv.codely.apps.backoffice.backend.controller.health_check;

import java.util.HashMap;

import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import tv.codely.shared.domain.DomainError;
import tv.codely.shared.domain.bus.command.CommandBus;
import tv.codely.shared.domain.bus.query.QueryBus;
import tv.codely.shared.infrastructure.spring.ApiController;

@RestController
public final class HealthCheckGetController extends ApiController {

	public HealthCheckGetController(QueryBus queryBus, CommandBus commandBus) {
		super(queryBus, commandBus);
	}

	@GetMapping("/health-check")
	public HashMap<String, String> index() {
		HashMap<String, String> status = new HashMap<>();
		status.put("application", "backoffice_backend");
		status.put("status", "ok");

		return status;
	}

	@Override
	public HashMap<Class<? extends DomainError>, HttpStatus> errorMapping() {
		return null;
	}
}
```

## File: `apps/main/tv/codely/apps/backoffice/backend/middleware/BasicHttpAuthMiddleware.java`
```java
package tv.codely.apps.backoffice.backend.middleware;

import java.io.IOException;
import java.util.Base64;

import jakarta.servlet.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

import tv.codely.backoffice.auth.application.authenticate.AuthenticateUserCommand;
import tv.codely.backoffice.auth.domain.InvalidAuthCredentials;
import tv.codely.backoffice.auth.domain.InvalidAuthUsername;
import tv.codely.shared.domain.bus.command.CommandBus;
import tv.codely.shared.domain.bus.command.CommandHandlerExecutionError;

public final class BasicHttpAuthMiddleware implements Filter {

	private final CommandBus bus;

	public BasicHttpAuthMiddleware(CommandBus bus) {
		this.bus = bus;
	}

	@Override
	public void doFilter(ServletRequest request, ServletResponse response, FilterChain chain)
		throws IOException, ServletException {
		String authorizationHeader = ((HttpServletRequest) request).getHeader("authorization");

		if (hasIntroducedCredentials(authorizationHeader)) {
			authenticate(authorizationHeader, chain, request, response);
		} else {
			askForCredentials(response);
		}
	}

	private boolean hasIntroducedCredentials(String authorizationHeader) {
		return null != authorizationHeader;
	}

	private void authenticate(
		String authorizationHeader,
		FilterChain chain,
		ServletRequest request,
		ServletResponse response
	) throws IOException, ServletException {
		String[] auth = decodeAuth(authorizationHeader);
		String user = auth[0];
		String pass = auth[1];

		try {
			bus.dispatch(new AuthenticateUserCommand(user, pass));

			request.setAttribute("authentication_username", user);

			chain.doFilter(request, response);
		} catch (InvalidAuthUsername | InvalidAuthCredentials | CommandHandlerExecutionError error) {
			setInvalidCredentials(response);
		}
	}

	private String[] decodeAuth(String authString) {
		return new String(Base64.getDecoder().decode(authString.split("\\s+")[1])).split(":");
	}

	private void setInvalidCredentials(ServletResponse response) {
		HttpServletResponse httpServletResponse = (HttpServletResponse) response;
		httpServletResponse.reset();
		httpServletResponse.setStatus(HttpServletResponse.SC_FORBIDDEN);
	}

	private void askForCredentials(ServletResponse response) {
		HttpServletResponse httpServletResponse = (HttpServletResponse) response;
		httpServletResponse.reset();
		httpServletResponse.setStatus(HttpServletResponse.SC_UNAUTHORIZED);
		httpServletResponse.setHeader("WWW-Authenticate", "Basic realm=\"CodelyTV\"");
	}
}
```

## File: `apps/main/tv/codely/apps/backoffice/frontend/BackofficeFrontendApplication.java`
```java
package tv.codely.apps.backoffice.frontend;

import java.util.HashMap;

import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.autoconfigure.orm.jpa.HibernateJpaAutoConfiguration;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.FilterType;

import tv.codely.shared.domain.Service;

@SpringBootApplication(exclude = HibernateJpaAutoConfiguration.class)
@ComponentScan(
	includeFilters = @ComponentScan.Filter(type = FilterType.ANNOTATION, classes = Service.class),
	value = { "tv.codely.shared", "tv.codely.backoffice", "tv.codely.mooc", "tv.codely.apps.backoffice.frontend" }
)
public class BackofficeFrontendApplication {

	public static HashMap<String, Class<?>> commands() {
		return new HashMap<String, Class<?>>() {
			{}
		};
	}
}
```

## File: `apps/main/tv/codely/apps/backoffice/frontend/config/BackofficeFrontendServerPortCustomizer.java`
```java
package tv.codely.apps.backoffice.frontend.config;

import org.springframework.boot.web.server.ConfigurableWebServerFactory;
import org.springframework.boot.web.server.WebServerFactoryCustomizer;
import org.springframework.stereotype.Component;

import tv.codely.shared.infrastructure.config.Parameter;
import tv.codely.shared.infrastructure.config.ParameterNotExist;

@Component
public final class BackofficeFrontendServerPortCustomizer
	implements WebServerFactoryCustomizer<ConfigurableWebServerFactory> {

	private final Parameter param;

	public BackofficeFrontendServerPortCustomizer(Parameter param) {
		this.param = param;
	}

	@Override
	public void customize(ConfigurableWebServerFactory factory) {
		try {
			factory.setPort(param.getInt("BACKOFFICE_FRONTEND_SERVER_PORT"));
		} catch (ParameterNotExist parameterNotExist) {
			parameterNotExist.printStackTrace();
		}
	}
}
```

## File: `apps/main/tv/codely/apps/backoffice/frontend/config/BackofficeFrontendWebConfig.java`
```java
package tv.codely.apps.backoffice.frontend.config;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.servlet.ViewResolver;
import org.springframework.web.servlet.config.annotation.EnableWebMvc;
import org.springframework.web.servlet.config.annotation.ResourceHandlerRegistry;
import org.springframework.web.servlet.config.annotation.ViewResolverRegistry;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;
import org.springframework.web.servlet.view.freemarker.FreeMarkerConfigurer;
import org.springframework.web.servlet.view.freemarker.FreeMarkerViewResolver;

@Configuration
@EnableWebMvc
public class BackofficeFrontendWebConfig implements WebMvcConfigurer {

	@Override
	public void configureViewResolvers(ViewResolverRegistry registry) {
		registry.freeMarker();
	}

	@Override
	public void addResourceHandlers(ResourceHandlerRegistry registry) {
		registry.addResourceHandler("/**").addResourceLocations("classpath:/backoffice_frontend/public/");
	}

	@Bean
	public ViewResolver getViewResolver() {
		FreeMarkerViewResolver resolver = new FreeMarkerViewResolver();
		resolver.setCache(false);
		resolver.setSuffix(".ftl");
		return resolver;
	}

	@Bean
	public FreeMarkerConfigurer freeMarkerConfigurer() {
		FreeMarkerConfigurer configurer = new FreeMarkerConfigurer();
		configurer.setTemplateLoaderPath("classpath:/backoffice_frontend/templates/");
		configurer.setDefaultEncoding("UTF-8");
		//        configurer.setFreemarkerVariables(new HashMap<String, Object>() {{
		//            put("flash", new Flash());
		//        }});

		return configurer;
	}
}
```

## File: `apps/main/tv/codely/apps/backoffice/frontend/controller/courses/CoursesGetWebController.java`
```java
package tv.codely.apps.backoffice.frontend.controller.courses;

import java.io.Serializable;
import java.util.HashMap;
import java.util.List;
import java.util.UUID;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.servlet.ModelAndView;

import tv.codely.mooc.courses_counter.application.find.CoursesCounterResponse;
import tv.codely.mooc.courses_counter.application.find.FindCoursesCounterQuery;
import tv.codely.shared.domain.bus.query.QueryBus;
import tv.codely.shared.domain.bus.query.QueryHandlerExecutionError;

@Controller
public final class CoursesGetWebController {

	private final QueryBus bus;

	public CoursesGetWebController(QueryBus bus) {
		this.bus = bus;
	}

	@GetMapping("/courses")
	public ModelAndView index(
		@ModelAttribute("inputs") HashMap<String, Serializable> inputs,
		@ModelAttribute("errors") HashMap<String, List<String>> errors
	) throws QueryHandlerExecutionError {
		CoursesCounterResponse counterResponse = bus.ask(new FindCoursesCounterQuery());

		return new ModelAndView(
			"pages/courses/courses",
			new HashMap<String, Serializable>() {
				{
					put("title", "Courses");
					put("description", "Courses CodelyTV - Backoffice");
					put("courses_counter", counterResponse.total());
					put("inputs", inputs);
					put("errors", errors);
					put("generated_uuid", UUID.randomUUID().toString());
				}
			}
		);
	}
}
```

## File: `apps/main/tv/codely/apps/backoffice/frontend/controller/courses/CoursesPostWebController.java`
```java
package tv.codely.apps.backoffice.frontend.controller.courses;

import java.io.Serializable;
import java.util.HashMap;

import org.springframework.http.MediaType;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.servlet.mvc.support.RedirectAttributes;
import org.springframework.web.servlet.view.RedirectView;

import tv.codely.mooc.courses.application.create.CreateCourseCommand;
import tv.codely.shared.domain.bus.command.CommandBus;
import tv.codely.shared.domain.bus.command.CommandHandlerExecutionError;
import tv.codely.shared.infrastructure.validation.ValidationResponse;
import tv.codely.shared.infrastructure.validation.Validator;

@Controller
public final class CoursesPostWebController {

	private final CommandBus bus;
	private final HashMap<String, String> rules = new HashMap<String, String>() {
		{
			put("id", "required|not_empty|uuid");
			put("name", "required|not_empty|string");
			put("duration", "required|not_empty|string");
		}
	};

	public CoursesPostWebController(CommandBus bus) {
		this.bus = bus;
	}

	@PostMapping(value = "/courses", consumes = MediaType.APPLICATION_FORM_URLENCODED_VALUE)
	public RedirectView index(@RequestParam HashMap<String, Serializable> request, RedirectAttributes attributes)
		throws Exception {
		ValidationResponse validationResponse = Validator.validate(request, rules);

		return validationResponse.hasErrors()
			? redirectWithErrors(validationResponse, request, attributes)
			: createCourse(request);
	}

	private RedirectView redirectWithErrors(
		ValidationResponse validationResponse,
		HashMap<String, Serializable> request,
		RedirectAttributes attributes
	) {
		attributes.addFlashAttribute("errors", validationResponse.errors());
		attributes.addFlashAttribute("inputs", request);

		return new RedirectView("/courses");
	}

	private RedirectView createCourse(HashMap<String, Serializable> request) throws CommandHandlerExecutionError {
		bus.dispatch(
			new CreateCourseCommand(
				request.get("id").toString(),
				request.get("name").toString(),
				request.get("duration").toString()
			)
		);

		return new RedirectView("/courses");
	}
}
```

## File: `apps/main/tv/codely/apps/backoffice/frontend/controller/health_check/HealthCheckGetController.java`
```java
package tv.codely.apps.backoffice.frontend.controller.health_check;

import java.util.HashMap;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public final class HealthCheckGetController {

	@GetMapping("/health-check")
	public HashMap<String, String> index() {
		HashMap<String, String> status = new HashMap<>();
		status.put("application", "backoffice_frontend");
		status.put("status", "ok");

		return status;
	}
}
```

## File: `apps/main/tv/codely/apps/backoffice/frontend/controller/home/HomeGetWebController.java`
```java
package tv.codely.apps.backoffice.frontend.controller.home;

import java.io.Serializable;
import java.util.HashMap;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.servlet.ModelAndView;

@Controller
public final class HomeGetWebController {

	@GetMapping("/")
	public ModelAndView index() {
		return new ModelAndView(
			"pages/home",
			new HashMap<String, Serializable>() {
				{
					put("title", "Welcome");
					put("description", "CodelyTV - Backoffice");
				}
			}
		);
	}
}
```

## File: `apps/main/tv/codely/apps/mooc/backend/MoocBackendApplication.java`
```java
package tv.codely.apps.mooc.backend;

import java.util.HashMap;

import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.autoconfigure.orm.jpa.HibernateJpaAutoConfiguration;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.FilterType;

import tv.codely.apps.mooc.backend.command.ConsumeMySqlDomainEventsCommand;
import tv.codely.apps.mooc.backend.command.ConsumeRabbitMqDomainEventsCommand;
import tv.codely.shared.domain.Service;

@SpringBootApplication(exclude = HibernateJpaAutoConfiguration.class)
@ComponentScan(
	includeFilters = @ComponentScan.Filter(type = FilterType.ANNOTATION, classes = Service.class),
	value = { "tv.codely.shared", "tv.codely.mooc", "tv.codely.apps.mooc.backend" }
)
public class MoocBackendApplication {

	public static HashMap<String, Class<?>> commands() {
		return new HashMap<String, Class<?>>() {
			{
				put("domain-events:mysql:consume", ConsumeMySqlDomainEventsCommand.class);
				put("domain-events:rabbitmq:consume", ConsumeRabbitMqDomainEventsCommand.class);
			}
		};
	}
}
```

## File: `apps/main/tv/codely/apps/mooc/backend/command/ConsumeMySqlDomainEventsCommand.java`
```java
package tv.codely.apps.mooc.backend.command;

import tv.codely.shared.infrastructure.bus.event.mysql.MySqlDomainEventsConsumer;
import tv.codely.shared.infrastructure.cli.ConsoleCommand;

public final class ConsumeMySqlDomainEventsCommand extends ConsoleCommand {

	private final MySqlDomainEventsConsumer consumer;

	public ConsumeMySqlDomainEventsCommand(MySqlDomainEventsConsumer consumer) {
		this.consumer = consumer;
	}

	@Override
	public void execute(String[] args) {
		consumer.consume();
	}
}
```

## File: `apps/main/tv/codely/apps/mooc/backend/command/ConsumeRabbitMqDomainEventsCommand.java`
```java
package tv.codely.apps.mooc.backend.command;

import tv.codely.shared.infrastructure.bus.event.rabbitmq.RabbitMqDomainEventsConsumer;
import tv.codely.shared.infrastructure.cli.ConsoleCommand;

public final class ConsumeRabbitMqDomainEventsCommand extends ConsoleCommand {

	private final RabbitMqDomainEventsConsumer consumer;

	public ConsumeRabbitMqDomainEventsCommand(RabbitMqDomainEventsConsumer consumer) {
		this.consumer = consumer;
	}

	@Override
	public void execute(String[] args) {
		consumer.consume();
	}
}
```

## File: `apps/main/tv/codely/apps/mooc/backend/config/MoocBackendServerConfiguration.java`
```java
package tv.codely.apps.mooc.backend.config;

import org.springframework.boot.web.servlet.FilterRegistrationBean;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.servlet.mvc.method.annotation.RequestMappingHandlerMapping;

import tv.codely.shared.infrastructure.spring.ApiExceptionMiddleware;

@Configuration
public class MoocBackendServerConfiguration {

	private final RequestMappingHandlerMapping mapping;

	public MoocBackendServerConfiguration(RequestMappingHandlerMapping mapping) {
		this.mapping = mapping;
	}

	@Bean
	public FilterRegistrationBean<ApiExceptionMiddleware> apiExceptionMiddleware() {
		FilterRegistrationBean<ApiExceptionMiddleware> registrationBean = new FilterRegistrationBean<>();

		registrationBean.setFilter(new ApiExceptionMiddleware(mapping));

		return registrationBean;
	}
}
```

## File: `apps/main/tv/codely/apps/mooc/backend/config/MoocBackendServerPortCustomizer.java`
```java
package tv.codely.apps.mooc.backend.config;

import org.springframework.boot.web.server.ConfigurableWebServerFactory;
import org.springframework.boot.web.server.WebServerFactoryCustomizer;
import org.springframework.stereotype.Component;

import tv.codely.shared.infrastructure.config.Parameter;
import tv.codely.shared.infrastructure.config.ParameterNotExist;

@Component
public final class MoocBackendServerPortCustomizer implements WebServerFactoryCustomizer<ConfigurableWebServerFactory> {

	private final Parameter param;

	public MoocBackendServerPortCustomizer(Parameter param) {
		this.param = param;
	}

	@Override
	public void customize(ConfigurableWebServerFactory factory) {
		try {
			factory.setPort(param.getInt("MOOC_BACKEND_SERVER_PORT"));
		} catch (ParameterNotExist parameterNotExist) {
			parameterNotExist.printStackTrace();
		}
	}
}
```

## File: `apps/main/tv/codely/apps/mooc/backend/controller/courses/CourseGetController.java`
```java
package tv.codely.apps.mooc.backend.controller.courses;

import java.io.Serializable;
import java.util.HashMap;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RestController;

import tv.codely.mooc.courses.application.CourseResponse;
import tv.codely.mooc.courses.application.find.FindCourseQuery;
import tv.codely.mooc.courses.domain.CourseNotExist;
import tv.codely.shared.domain.DomainError;
import tv.codely.shared.domain.bus.command.CommandBus;
import tv.codely.shared.domain.bus.query.QueryBus;
import tv.codely.shared.domain.bus.query.QueryHandlerExecutionError;
import tv.codely.shared.infrastructure.spring.ApiController;

@RestController
public final class CourseGetController extends ApiController {

	public CourseGetController(QueryBus queryBus, CommandBus commandBus) {
		super(queryBus, commandBus);
	}

	@GetMapping("/courses/{id}")
	public ResponseEntity<HashMap<String, Serializable>> index(@PathVariable String id)
		throws QueryHandlerExecutionError {
		CourseResponse course = ask(new FindCourseQuery(id));

		return ResponseEntity
			.ok()
			.body(
				new HashMap<String, Serializable>() {
					{
						put("id", course.id());
						put("name", course.name());
						put("duration", course.duration());
					}
				}
			);
	}

	@Override
	public HashMap<Class<? extends DomainError>, HttpStatus> errorMapping() {
		return new HashMap<Class<? extends DomainError>, HttpStatus>() {
			{
				put(CourseNotExist.class, HttpStatus.NOT_FOUND);
			}
		};
	}
}
```

## File: `apps/main/tv/codely/apps/mooc/backend/controller/courses/CoursesPutController.java`
```java
package tv.codely.apps.mooc.backend.controller.courses;

import java.util.HashMap;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import tv.codely.mooc.courses.application.create.CreateCourseCommand;
import tv.codely.shared.domain.DomainError;
import tv.codely.shared.domain.bus.command.CommandBus;
import tv.codely.shared.domain.bus.command.CommandHandlerExecutionError;
import tv.codely.shared.domain.bus.query.QueryBus;
import tv.codely.shared.infrastructure.spring.ApiController;

@RestController
public final class CoursesPutController extends ApiController {

	public CoursesPutController(QueryBus queryBus, CommandBus commandBus) {
		super(queryBus, commandBus);
	}

	@PutMapping(value = "/courses/{id}")
	public ResponseEntity<String> index(@PathVariable String id, @RequestBody Request request)
		throws CommandHandlerExecutionError {
		dispatch(new CreateCourseCommand(id, request.name(), request.duration()));

		return new ResponseEntity<>(HttpStatus.CREATED);
	}

	@Override
	public HashMap<Class<? extends DomainError>, HttpStatus> errorMapping() {
		return null;
	}
}

final class Request {

	private String name;
	private String duration;

	public void setDuration(String duration) {
		this.duration = duration;
	}

	public void setName(String name) {
		this.name = name;
	}

	String name() {
		return name;
	}

	String duration() {
		return duration;
	}
}
```

## File: `apps/main/tv/codely/apps/mooc/backend/controller/courses_counter/CoursesCounterGetController.java`
```java
package tv.codely.apps.mooc.backend.controller.courses_counter;

import java.util.HashMap;

import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import tv.codely.mooc.courses_counter.application.find.CoursesCounterResponse;
import tv.codely.mooc.courses_counter.application.find.FindCoursesCounterQuery;
import tv.codely.shared.domain.DomainError;
import tv.codely.shared.domain.bus.command.CommandBus;
import tv.codely.shared.domain.bus.query.QueryBus;
import tv.codely.shared.domain.bus.query.QueryHandlerExecutionError;
import tv.codely.shared.infrastructure.spring.ApiController;

@RestController
public final class CoursesCounterGetController extends ApiController {

	public CoursesCounterGetController(QueryBus queryBus, CommandBus commandBus) {
		super(queryBus, commandBus);
	}

	@GetMapping("/courses-counter")
	public HashMap<String, Integer> index() throws QueryHandlerExecutionError {
		CoursesCounterResponse response = ask(new FindCoursesCounterQuery());

		return new HashMap<String, Integer>() {
			{
				put("total", response.total());
			}
		};
	}

	@Override
	public HashMap<Class<? extends DomainError>, HttpStatus> errorMapping() {
		return null;
	}
}
```

## File: `apps/main/tv/codely/apps/mooc/backend/controller/health_check/HealthCheckGetController.java`
```java
package tv.codely.apps.mooc.backend.controller.health_check;

import java.util.HashMap;

import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import tv.codely.shared.domain.DomainError;
import tv.codely.shared.domain.bus.command.CommandBus;
import tv.codely.shared.domain.bus.query.QueryBus;
import tv.codely.shared.infrastructure.spring.ApiController;

@RestController
public final class HealthCheckGetController extends ApiController {

	public HealthCheckGetController(QueryBus queryBus, CommandBus commandBus) {
		super(queryBus, commandBus);
	}

	@GetMapping("/health-check")
	public HashMap<String, String> index() {
		HashMap<String, String> status = new HashMap<>();
		status.put("application", "mooc_backend");
		status.put("status", "ok");

		return status;
	}

	@Override
	public HashMap<Class<? extends DomainError>, HttpStatus> errorMapping() {
		return null;
	}
}
```

## File: `apps/main/tv/codely/apps/mooc/backend/controller/notifications/NewsletterNotificationPutController.java`
```java
package tv.codely.apps.mooc.backend.controller.notifications;

import java.util.HashMap;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RestController;

import tv.codely.mooc.notifications.application.send_new_courses_newsletter.SendNewCoursesNewsletterCommand;
import tv.codely.shared.domain.DomainError;
import tv.codely.shared.domain.bus.command.CommandBus;
import tv.codely.shared.domain.bus.command.CommandHandlerExecutionError;
import tv.codely.shared.domain.bus.query.QueryBus;
import tv.codely.shared.infrastructure.spring.ApiController;

@RestController
public final class NewsletterNotificationPutController extends ApiController {

	public NewsletterNotificationPutController(QueryBus queryBus, CommandBus commandBus) {
		super(queryBus, commandBus);
	}

	@PutMapping(value = "/newsletter/{id}")
	public ResponseEntity<String> index(@PathVariable String id) throws CommandHandlerExecutionError {
		dispatch(new SendNewCoursesNewsletterCommand(id));

		return new ResponseEntity<>(HttpStatus.CREATED);
	}

	@Override
	public HashMap<Class<? extends DomainError>, HttpStatus> errorMapping() {
		return null;
	}
}
```

## File: `apps/test/resources/log4j2.properties`
```
name                                         = CodelyTvJavaDddExample
property.filename                            = logs
appenders                                    = console, file

status                                       = warn

appender.console.name                        = CONSOLE
appender.console.type                        = CONSOLE
appender.console.target                      = SYSTEM_OUT

appender.console.layout.type                 = PatternLayout
appender.console.layout.pattern              = [%level] [%date{HH:mm:ss.SSS}] [%class{0}#%method:%line] %message \(%mdc\) %n%throwable
appender.console.filter.threshold.type       = ThresholdFilter
appender.console.filter.threshold.level      = info

appender.file.type                           = File
appender.file.name                           = LOGFILE
appender.file.fileName                       = var/log/java-ddd-example-test.log
appender.file.logstash.type                  = LogstashLayout
appender.file.logstash.dateTimeFormatPattern = yyyy-MM-dd'T'HH:mm:ss.SSSZZZ
appender.file.logstash.eventTemplateUri      = classpath:LogstashJsonEventLayoutV1.json
appender.file.logstash.prettyPrintEnabled    = false
appender.file.logstash.stackTraceEnabled     = true

loggers                                      = file
logger.file.name                             = tv.codely.java_ddd_example
logger.file.level                            = info
logger.file.appenderRefs                     = file
logger.file.appenderRef.file.ref             = LOGFILE

rootLogger.level                             = info
rootLogger.appenderRefs                      = stdout
rootLogger.appenderRef.stdout.ref            = CONSOLE
```

## File: `apps/test/tv/codely/apps/ApplicationTestCase.java`
```java
package tv.codely.apps;

import static org.springframework.http.MediaType.APPLICATION_JSON;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.get;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.request;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.content;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status;

import java.util.Arrays;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.AutoConfigureMockMvc;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.http.HttpHeaders;
import org.springframework.http.HttpMethod;
import org.springframework.test.web.servlet.MockMvc;
import org.springframework.test.web.servlet.ResultMatcher;

import tv.codely.shared.domain.bus.event.DomainEvent;
import tv.codely.shared.domain.bus.event.EventBus;

@SpringBootTest
@AutoConfigureMockMvc
public abstract class ApplicationTestCase {

	@Autowired
	private MockMvc mockMvc;

	@Autowired
	private EventBus eventBus;

	protected void assertResponse(String endpoint, Integer expectedStatusCode, String expectedResponse) throws Exception {
		ResultMatcher response = expectedResponse.isEmpty() ? content().string("") : content().json(expectedResponse);

		mockMvc.perform(get(endpoint)).andExpect(status().is(expectedStatusCode)).andExpect(response);
	}

	protected void assertResponse(
		String endpoint,
		Integer expectedStatusCode,
		String expectedResponse,
		HttpHeaders headers
	) throws Exception {
		ResultMatcher response = expectedResponse.isEmpty() ? content().string("") : content().json(expectedResponse);

		mockMvc.perform(get(endpoint).headers(headers)).andExpect(status().is(expectedStatusCode)).andExpect(response);
	}

	protected void assertRequestWithBody(String method, String endpoint, String body, Integer expectedStatusCode)
		throws Exception {
		mockMvc
			.perform(request(HttpMethod.valueOf(method), endpoint).content(body).contentType(APPLICATION_JSON))
			.andExpect(status().is(expectedStatusCode))
			.andExpect(content().string(""));
	}

	protected void assertRequest(String method, String endpoint, Integer expectedStatusCode) throws Exception {
		mockMvc
			.perform(request(HttpMethod.valueOf(method), endpoint))
			.andExpect(status().is(expectedStatusCode))
			.andExpect(content().string(""));
	}

	protected void givenISendEventsToTheBus(DomainEvent... domainEvents) {
		eventBus.publish(Arrays.asList(domainEvents));
	}
}
```

## File: `apps/test/tv/codely/apps/backoffice/BackofficeApplicationTestCase.java`
```java
package tv.codely.apps.backoffice;

import org.springframework.transaction.annotation.Transactional;

import tv.codely.apps.ApplicationTestCase;

@Transactional("backoffice-transaction_manager")
public abstract class BackofficeApplicationTestCase extends ApplicationTestCase {}
```

## File: `apps/test/tv/codely/apps/backoffice/backend/controller/health_check/HealthCheckGetControllerShould.java`
```java
package tv.codely.apps.backoffice.backend.controller.health_check;

import org.junit.jupiter.api.Test;
import org.springframework.http.HttpHeaders;

import tv.codely.apps.ApplicationTestCase;

final class HealthCheckGetControllerShould extends ApplicationTestCase {

	@Test
	void check_the_app_is_working_ok_with_valid_credentials() throws Exception {
		HttpHeaders headers = new HttpHeaders();
		headers.setBasicAuth("javi", "barbitas");

		assertResponse("/health-check", 200, "{'application':'backoffice_backend','status':'ok'}", headers);
	}

	@Test
	void not_check_the_app_is_working_ok_with_invalid_credentials() throws Exception {
		HttpHeaders headers = new HttpHeaders();
		headers.setBasicAuth("tipo_de_incognito", "homer.sampson");

		assertResponse("/health-check", 403, "", headers);
	}

	@Test
	void not_check_the_app_is_working_ok_with_invalid_credentials_of_an_existing_user() throws Exception {
		HttpHeaders headers = new HttpHeaders();
		headers.setBasicAuth("rafa", "incorrect.password");

		assertResponse("/health-check", 403, "", headers);
	}

	@Test
	void not_check_the_app_is_working_ok_with_no_credentials() throws Exception {
		assertResponse("/health-check", 401, "");
	}
}
```

## File: `apps/test/tv/codely/apps/backoffice/frontend/controller/health_check/HealthCheckGetControllerShould.java`
```java
package tv.codely.apps.backoffice.frontend.controller.health_check;

import org.junit.jupiter.api.Test;

import tv.codely.apps.ApplicationTestCase;

final class HealthCheckGetControllerShould extends ApplicationTestCase {

	@Test
	void check_the_app_is_working_ok() throws Exception {
		assertResponse("/health-check", 200, "{'application':'backoffice_frontend','status':'ok'}");
	}
}
```

## File: `apps/test/tv/codely/apps/mooc/MoocApplicationTestCase.java`
```java
package tv.codely.apps.mooc;

import org.springframework.transaction.annotation.Transactional;

import tv.codely.apps.ApplicationTestCase;

@Transactional("mooc-transaction_manager")
public abstract class MoocApplicationTestCase extends ApplicationTestCase {}
```

## File: `apps/test/tv/codely/apps/mooc/backend/controller/courses/CourseGetControllerShould.java`
```java
package tv.codely.apps.mooc.backend.controller.courses;

import org.junit.jupiter.api.Test;

import tv.codely.apps.mooc.MoocApplicationTestCase;

final class CourseGetControllerShould extends MoocApplicationTestCase {

	@Test
	void find_an_existing_course() throws Exception {
		String id = "99ad55f5-6eab-4d73-b383-c63268e251e8";
		String body = "{\"name\": \"The best course\", \"duration\": \"5 hours\"}";

		givenThereIsACourse(id, body);

		assertResponse(String.format("/courses/%s", id), 200, body);
	}

	@Test
	void no_find_a_non_existing_course() throws Exception {
		String id = "4ecc0cb3-05b2-4238-b7e1-1fbb0d5d3661";
		String body =
			"{\"error_code\": \"course_not_exist\", \"message\": \"The course <4ecc0cb3-05b2-4238-b7e1-1fbb0d5d3661> doesn't exist\"}";

		assertResponse(String.format("/courses/%s", id), 404, body);
	}

	private void givenThereIsACourse(String id, String body) throws Exception {
		assertRequestWithBody("PUT", String.format("/courses/%s", id), body, 201);
	}
}
```

## File: `apps/test/tv/codely/apps/mooc/backend/controller/courses/CoursesPutControllerShould.java`
```java
package tv.codely.apps.mooc.backend.controller.courses;

import org.junit.jupiter.api.Test;

import tv.codely.apps.mooc.MoocApplicationTestCase;

public final class CoursesPutControllerShould extends MoocApplicationTestCase {

	@Test
	void create_a_valid_non_existing_course() throws Exception {
		assertRequestWithBody(
			"PUT",
			"/courses/1aab45ba-3c7a-4344-8936-78466eca77fa",
			"{\"name\": \"The best course\", \"duration\": \"5 hours\"}",
			201
		);
	}
}
```

## File: `apps/test/tv/codely/apps/mooc/backend/controller/courses_counter/CoursesCounterGetControllerShould.java`
```java
package tv.codely.apps.mooc.backend.controller.courses_counter;

import org.junit.jupiter.api.Test;

import tv.codely.apps.mooc.MoocApplicationTestCase;
import tv.codely.shared.domain.course.CourseCreatedDomainEvent;

public final class CoursesCounterGetControllerShould extends MoocApplicationTestCase {

	@Test
	void get_the_counter_with_one_course() throws Exception {
		givenISendEventsToTheBus(
			new CourseCreatedDomainEvent("8f34bc99-e0e2-4296-a008-75f51f03aeb4", "DDD en Java", "7 days")
		);

		assertResponse("/courses-counter", 200, "{'total': 1}");
	}

	@Test
	void get_the_counter_with_more_than_one_course() throws Exception {
		givenISendEventsToTheBus(
			new CourseCreatedDomainEvent("8f34bc99-e0e2-4296-a008-75f51f03aeb4", "DDD en Java", "7 days"),
			new CourseCreatedDomainEvent("3642f700-868a-4778-9317-a2d542d01785", "DDD en PHP", "6 days"),
			new CourseCreatedDomainEvent("92dd8402-69f3-4900-b569-3f2c2797065f", "DDD en Cobol", "10 years")
		);

		assertResponse("/courses-counter", 200, "{'total': 3}");
	}

	@Test
	void get_the_counter_with_more_than_one_course_having_duplicated_events() throws Exception {
		givenISendEventsToTheBus(
			new CourseCreatedDomainEvent("8f34bc99-e0e2-4296-a008-75f51f03aeb4", "DDD en Java", "7 days"),
			new CourseCreatedDomainEvent("8f34bc99-e0e2-4296-a008-75f51f03aeb4", "DDD en Java", "7 days"),
			new CourseCreatedDomainEvent("8f34bc99-e0e2-4296-a008-75f51f03aeb4", "DDD en Java", "7 days"),
			new CourseCreatedDomainEvent("3642f700-868a-4778-9317-a2d542d01785", "DDD en PHP", "6 days"),
			new CourseCreatedDomainEvent("3642f700-868a-4778-9317-a2d542d01785", "DDD en PHP", "6 days"),
			new CourseCreatedDomainEvent("3642f700-868a-4778-9317-a2d542d01785", "DDD en PHP", "6 days"),
			new CourseCreatedDomainEvent("3642f700-868a-4778-9317-a2d542d01785", "DDD en PHP", "6 days"),
			new CourseCreatedDomainEvent("92dd8402-69f3-4900-b569-3f2c2797065f", "DDD en Cobol", "10 years"),
			new CourseCreatedDomainEvent("92dd8402-69f3-4900-b569-3f2c2797065f", "DDD en Cobol", "10 years")
		);

		assertResponse("/courses-counter", 200, "{'total': 3}");
	}
}
```

## File: `apps/test/tv/codely/apps/mooc/backend/controller/health_check/HealthCheckGetControllerShould.java`
```java
package tv.codely.apps.mooc.backend.controller.health_check;

import org.junit.jupiter.api.Test;

import tv.codely.apps.mooc.MoocApplicationTestCase;

final class HealthCheckGetControllerShould extends MoocApplicationTestCase {

	@Test
	void check_the_app_is_working_ok() throws Exception {
		assertResponse("/health-check", 200, "{'application':'mooc_backend','status':'ok'}");
	}
}
```

## File: `apps/test/tv/codely/apps/mooc/backend/controller/notifications/NewsletterNotificationPutControllerShould.java`
```java
package tv.codely.apps.mooc.backend.controller.notifications;

import org.junit.jupiter.api.Test;

import tv.codely.apps.mooc.MoocApplicationTestCase;

final class NewsletterNotificationPutControllerShould extends MoocApplicationTestCase {

	@Test
	void create_a_valid_non_existing_course() throws Exception {
		assertRequest("PUT", "/newsletter/6eebbe60-50e7-400a-810c-3e0af0943ee6", 201);
	}
}
```

## File: `doc/endpoints/backoffice_frontend.http`
```
# ELASTIC - Search
POST localhost:9200/backoffice_courses/_search
Content-Type: application/json

{
  "query": {
    "term": {
      "name": "git avanzado"
    }
  }
}

###

# ELASTIC - debug
POST localhost:9200/backoffice_courses/_search
Content-Type: application/json

{
  "from": 0,
  "size": 1000,
  "query": {
    "bool": {
      "must": [
        {
          "term": {
            "name": {
              "value": "pepe2"
            }
          }
        }
      ],
      "adjust_pure_negative": true,
      "boost": 1.0
    }
  }
}

###
# ELASTIC - Search
POST localhost:9200/backoffice_courses/_search
Content-Type: application/json

###
# ELASTIC - Mapping
GET localhost:9200/backoffice_courses/_mapping
Content-Type: application/json

###
# ELASTIC - Change mapping
PUT localhost:9200/backoffice_courses/_mapping/_doc
Content-Type: application/json

{
  "properties": {
    "name": {
      "type": "text",
      "fielddata": true
    }
  }
}

###
# ELASTIC - DELETE
DELETE localhost:9200/backoffice_courses

###

PUT localhost:9200/backoffice_courses/_settings
Content-Type: application/json

{
  "index": {
    "blocks": {
      "read_only_allow_delete": "false"
    }
  }
}

###
```

## File: `gradle/wrapper/gradle-wrapper.properties`
```
distributionBase=GRADLE_USER_HOME
distributionPath=wrapper/dists
distributionUrl=https\://services.gradle.org/distributions/gradle-8.4-bin.zip
networkTimeout=10000
validateDistributionUrl=true
zipStoreBase=GRADLE_USER_HOME
zipStorePath=wrapper/dists
```

## File: `hooks/applypatch-msg.sample`
```
#!/bin/sh
#
# An example hook script to check the commit log message taken by
# applypatch from an e-mail message.
#
# The hook should exit with non-zero status after issuing an
# appropriate message if it wants to stop the commit.  The hook is
# allowed to edit the commit message file.
#
# To enable this hook, rename this file to "applypatch-msg".

. git-sh-setup
commitmsg="$(git rev-parse --git-path hooks/commit-msg)"
test -x "$commitmsg" && exec "$commitmsg" ${1+"$@"}
:
```

## File: `hooks/commit-msg.sample`
```
#!/bin/sh
#
# An example hook script to check the commit log message.
# Called by "git commit" with one argument, the name of the file
# that has the commit message.  The hook should exit with non-zero
# status after issuing an appropriate message if it wants to stop the
# commit.  The hook is allowed to edit the commit message file.
#
# To enable this hook, rename this file to "commit-msg".

# Uncomment the below to add a Signed-off-by line to the message.
# Doing this in a hook is a bad idea in general, but the prepare-commit-msg
# hook is more suited to it.
#
# SOB=$(git var GIT_AUTHOR_IDENT | sed -n 's/^\(.*>\).*$/Signed-off-by: \1/p')
# grep -qs "^$SOB" "$1" || echo "$SOB" >> "$1"

# This example catches duplicate Signed-off-by lines.

test "" = "$(grep '^Signed-off-by: ' "$1" |
	 sort | uniq -c | sed -e '/^[ 	]*1[ 	]/d')" || {
	echo >&2 Duplicate Signed-off-by lines.
	exit 1
}
```

## File: `hooks/fsmonitor-watchman.sample`
```
#!/usr/bin/perl

use strict;
use warnings;
use IPC::Open2;

# An example hook script to integrate Watchman
# (https://facebook.github.io/watchman/) with git to speed up detecting
# new and modified files.
#
# The hook is passed a version (currently 2) and last update token
# formatted as a string and outputs to stdout a new update token and
# all files that have been modified since the update token. Paths must
# be relative to the root of the working tree and separated by a single NUL.
#
# To enable this hook, rename this file to "query-watchman" and set
# 'git config core.fsmonitor .git/hooks/query-watchman'
#
my ($version, $last_update_token) = @ARGV;

# Uncomment for debugging
# print STDERR "$0 $version $last_update_token\n";

# Check the hook interface version
if ($version ne 2) {
	die "Unsupported query-fsmonitor hook version '$version'.\n" .
	    "Falling back to scanning...\n";
}

my $git_work_tree = get_working_dir();

my $retry = 1;

my $json_pkg;
eval {
	require JSON::XS;
	$json_pkg = "JSON::XS";
	1;
} or do {
	require JSON::PP;
	$json_pkg = "JSON::PP";
};

launch_watchman();

sub launch_watchman {
	my $o = watchman_query();
	if (is_work_tree_watched($o)) {
		output_result($o->{clock}, @{$o->{files}});
	}
}

sub output_result {
	my ($clockid, @files) = @_;

	# Uncomment for debugging watchman output
	# open (my $fh, ">", ".git/watchman-output.out");
	# binmode $fh, ":utf8";
	# print $fh "$clockid\n@files\n";
	# close $fh;

	binmode STDOUT, ":utf8";
	print $clockid;
	print "\0";
	local $, = "\0";
	print @files;
}

sub watchman_clock {
	my $response = qx/watchman clock "$git_work_tree"/;
	die "Failed to get clock id on '$git_work_tree'.\n" .
		"Falling back to scanning...\n" if $? != 0;

	return $json_pkg->new->utf8->decode($response);
}

sub watchman_query {
	my $pid = open2(\*CHLD_OUT, \*CHLD_IN, 'watchman -j --no-pretty')
	or die "open2() failed: $!\n" .
	"Falling back to scanning...\n";

	# In the query expression below we're asking for names of files that
	# changed since $last_update_token but not from the .git folder.
	#
	# To accomplish this, we're using the "since" generator to use the
	# recency index to select candidate nodes and "fields" to limit the
	# output to file names only. Then we're using the "expression" term to
	# further constrain the results.
	my $last_update_line = "";
	if (substr($last_update_token, 0, 1) eq "c") {
		$last_update_token = "\"$last_update_token\"";
		$last_update_line = qq[\n"since": $last_update_token,];
	}
	my $query = <<"	END";
		["query", "$git_work_tree", {$last_update_line
			"fields": ["name"],
			"expression": ["not", ["dirname", ".git"]]
		}]
	END

	# Uncomment for debugging the watchman query
	# open (my $fh, ">", ".git/watchman-query.json");
	# print $fh $query;
	# close $fh;

	print CHLD_IN $query;
	close CHLD_IN;
	my $response = do {local $/; <CHLD_OUT>};

	# Uncomment for debugging the watch response
	# open ($fh, ">", ".git/watchman-response.json");
	# print $fh $response;
	# close $fh;

	die "Watchman: command returned no output.\n" .
	"Falling back to scanning...\n" if $response eq "";
	die "Watchman: command returned invalid output: $response\n" .
	"Falling back to scanning...\n" unless $response =~ /^\{/;

	return $json_pkg->new->utf8->decode($response);
}

sub is_work_tree_watched {
	my ($output) = @_;
	my $error = $output->{error};
	if ($retry > 0 and $error and $error =~ m/unable to resolve root .* directory (.*) is not watched/) {
		$retry--;
		my $response = qx/watchman watch "$git_work_tree"/;
		die "Failed to make watchman watch '$git_work_tree'.\n" .
		    "Falling back to scanning...\n" if $? != 0;
		$output = $json_pkg->new->utf8->decode($response);
		$error = $output->{error};
		die "Watchman: $error.\n" .
		"Falling back to scanning...\n" if $error;

		# Uncomment for debugging watchman output
		# open (my $fh, ">", ".git/watchman-output.out");
		# close $fh;

		# Watchman will always return all files on the first query so
		# return the fast "everything is dirty" flag to git and do the
		# Watchman query just to get it over with now so we won't pay
		# the cost in git to look up each individual file.
		my $o = watchman_clock();
		$error = $output->{error};

		die "Watchman: $error.\n" .
		"Falling back to scanning...\n" if $error;

		output_result($o->{clock}, ("/"));
		$last_update_token = $o->{clock};

		eval { launch_watchman() };
		return 0;
	}

	die "Watchman: $error.\n" .
	"Falling back to scanning...\n" if $error;

	return 1;
}

sub get_working_dir {
	my $working_dir;
	if ($^O =~ 'msys' || $^O =~ 'cygwin') {
		$working_dir = Win32::GetCwd();
		$working_dir =~ tr/\\/\//;
	} else {
		require Cwd;
		$working_dir = Cwd::cwd();
	}

	return $working_dir;
}
```

## File: `hooks/post-update.sample`
```
#!/bin/sh
#
# An example hook script to prepare a packed repository for use over
# dumb transports.
#
# To enable this hook, rename this file to "post-update".

exec git update-server-info
```

## File: `hooks/pre-applypatch.sample`
```
#!/bin/sh
#
# An example hook script to verify what is about to be committed
# by applypatch from an e-mail message.
#
# The hook should exit with non-zero status after issuing an
# appropriate message if it wants to stop the commit.
#
# To enable this hook, rename this file to "pre-applypatch".

. git-sh-setup
precommit="$(git rev-parse --git-path hooks/pre-commit)"
test -x "$precommit" && exec "$precommit" ${1+"$@"}
:
```

## File: `hooks/pre-commit.sample`
```
#!/bin/sh
#
# An example hook script to verify what is about to be committed.
# Called by "git commit" with no arguments.  The hook should
# exit with non-zero status after issuing an appropriate message if
# it wants to stop the commit.
#
# To enable this hook, rename this file to "pre-commit".

if git rev-parse --verify HEAD >/dev/null 2>&1
then
	against=HEAD
else
	# Initial commit: diff against an empty tree object
	against=$(git hash-object -t tree /dev/null)
fi

# If you want to allow non-ASCII filenames set this variable to true.
allownonascii=$(git config --type=bool hooks.allownonascii)

# Redirect output to stderr.
exec 1>&2

# Cross platform projects tend to avoid non-ASCII filenames; prevent
# them from being added to the repository. We exploit the fact that the
# printable range starts at the space character and ends with tilde.
if [ "$allownonascii" != "true" ] &&
	# Note that the use of brackets around a tr range is ok here, (it's
	# even required, for portability to Solaris 10's /usr/bin/tr), since
	# the square bracket bytes happen to fall in the designated range.
	test $(git diff-index --cached --name-only --diff-filter=A -z $against |
	  LC_ALL=C tr -d '[ -~]\0' | wc -c) != 0
then
	cat <<\EOF
Error: Attempt to add a non-ASCII file name.

This can cause problems if you want to work with people on other platforms.

To be portable it is advisable to rename the file.

If you know what you are doing you can disable this check using:

  git config hooks.allownonascii true
EOF
	exit 1
fi

# If there are whitespace errors, print the offending file names and fail.
exec git diff-index --check --cached $against --
```

## File: `hooks/pre-merge-commit.sample`
```
#!/bin/sh
#
# An example hook script to verify what is about to be committed.
# Called by "git merge" with no arguments.  The hook should
# exit with non-zero status after issuing an appropriate message to
# stderr if it wants to stop the merge commit.
#
# To enable this hook, rename this file to "pre-merge-commit".

. git-sh-setup
test -x "$GIT_DIR/hooks/pre-commit" &&
        exec "$GIT_DIR/hooks/pre-commit"
:
```

## File: `hooks/pre-push.sample`
```
#!/bin/sh

# An example hook script to verify what is about to be pushed.  Called by "git
# push" after it has checked the remote status, but before anything has been
# pushed.  If this script exits with a non-zero status nothing will be pushed.
#
# This hook is called with the following parameters:
#
# $1 -- Name of the remote to which the push is being done
# $2 -- URL to which the push is being done
#
# If pushing without using a named remote those arguments will be equal.
#
# Information about the commits which are being pushed is supplied as lines to
# the standard input in the form:
#
#   <local ref> <local oid> <remote ref> <remote oid>
#
# This sample shows how to prevent push of commits where the log message starts
# with "WIP" (work in progress).

remote="$1"
url="$2"

zero=$(git hash-object --stdin </dev/null | tr '[0-9a-f]' '0')

while read local_ref local_oid remote_ref remote_oid
do
	if test "$local_oid" = "$zero"
	then
		# Handle delete
		:
	else
		if test "$remote_oid" = "$zero"
		then
			# New branch, examine all commits
			range="$local_oid"
		else
			# Update to existing branch, examine new commits
			range="$remote_oid..$local_oid"
		fi

		# Check for WIP commit
		commit=$(git rev-list -n 1 --grep '^WIP' "$range")
		if test -n "$commit"
		then
			echo >&2 "Found WIP commit in $local_ref, not pushing"
			exit 1
		fi
	fi
done

exit 0
```

## File: `hooks/pre-rebase.sample`
```
#!/bin/sh
#
# Copyright (c) 2006, 2008 Junio C Hamano
#
# The "pre-rebase" hook is run just before "git rebase" starts doing
# its job, and can prevent the command from running by exiting with
# non-zero status.
#
# The hook is called with the following parameters:
#
# $1 -- the upstream the series was forked from.
# $2 -- the branch being rebased (or empty when rebasing the current branch).
#
# This sample shows how to prevent topic branches that are already
# merged to 'next' branch from getting rebased, because allowing it
# would result in rebasing already published history.

publish=next
basebranch="$1"
if test "$#" = 2
then
	topic="refs/heads/$2"
else
	topic=`git symbolic-ref HEAD` ||
	exit 0 ;# we do not interrupt rebasing detached HEAD
fi

case "$topic" in
refs/heads/??/*)
	;;
*)
	exit 0 ;# we do not interrupt others.
	;;
esac

# Now we are dealing with a topic branch being rebased
# on top of master.  Is it OK to rebase it?

# Does the topic really exist?
git show-ref -q "$topic" || {
	echo >&2 "No such branch $topic"
	exit 1
}

# Is topic fully merged to master?
not_in_master=`git rev-list --pretty=oneline ^master "$topic"`
if test -z "$not_in_master"
then
	echo >&2 "$topic is fully merged to master; better remove it."
	exit 1 ;# we could allow it, but there is no point.
fi

# Is topic ever merged to next?  If so you should not be rebasing it.
only_next_1=`git rev-list ^master "^$topic" ${publish} | sort`
only_next_2=`git rev-list ^master           ${publish} | sort`
if test "$only_next_1" = "$only_next_2"
then
	not_in_topic=`git rev-list "^$topic" master`
	if test -z "$not_in_topic"
	then
		echo >&2 "$topic is already up to date with master"
		exit 1 ;# we could allow it, but there is no point.
	else
		exit 0
	fi
else
	not_in_next=`git rev-list --pretty=oneline ^${publish} "$topic"`
	/usr/bin/perl -e '
		my $topic = $ARGV[0];
		my $msg = "* $topic has commits already merged to public branch:\n";
		my (%not_in_next) = map {
			/^([0-9a-f]+) /;
			($1 => 1);
		} split(/\n/, $ARGV[1]);
		for my $elem (map {
				/^([0-9a-f]+) (.*)$/;
				[$1 => $2];
			} split(/\n/, $ARGV[2])) {
			if (!exists $not_in_next{$elem->[0]}) {
				if ($msg) {
					print STDERR $msg;
					undef $msg;
				}
				print STDERR " $elem->[1]\n";
			}
		}
	' "$topic" "$not_in_next" "$not_in_master"
	exit 1
fi

<<\DOC_END

This sample hook safeguards topic branches that have been
published from being rewound.

The workflow assumed here is:

 * Once a topic branch forks from "master", "master" is never
   merged into it again (either directly or indirectly).

 * Once a topic branch is fully cooked and merged into "master",
   it is deleted.  If you need to build on top of it to correct
   earlier mistakes, a new topic branch is created by forking at
   the tip of the "master".  This is not strictly necessary, but
   it makes it easier to keep your history simple.

 * Whenever you need to test or publish your changes to topic
   branches, merge them into "next" branch.

The script, being an example, hardcodes the publish branch name
to be "next", but it is trivial to make it configurable via
$GIT_DIR/config mechanism.

With this workflow, you would want to know:

(1) ... if a topic branch has ever been merged to "next".  Young
    topic branches can have stupid mistakes you would rather
    clean up before publishing, and things that have not been
    merged into other branches can be easily rebased without
    affecting other people.  But once it is published, you would
    not want to rewind it.

(2) ... if a topic branch has been fully merged to "master".
    Then you can delete it.  More importantly, you should not
    build on top of it -- other people may already want to
    change things related to the topic as patches against your
    "master", so if you need further changes, it is better to
    fork the topic (perhaps with the same name) afresh from the
    tip of "master".

Let's look at this example:

		   o---o---o---o---o---o---o---o---o---o "next"
		  /       /           /           /
		 /   a---a---b A     /           /
		/   /               /           /
	       /   /   c---c---c---c B         /
	      /   /   /             \         /
	     /   /   /   b---b C     \       /
	    /   /   /   /             \     /
    ---o---o---o---o---o---o---o---o---o---o---o "master"


A, B and C are topic branches.

 * A has one fix since it was merged up to "next".

 * B has finished.  It has been fully merged up to "master" and "next",
   and is ready to be deleted.

 * C has not merged to "next" at all.

We would want to allow C to be rebased, refuse A, and encourage
B to be deleted.

To compute (1):

	git rev-list ^master ^topic next
	git rev-list ^master        next

	if these match, topic has not merged in next at all.

To compute (2):

	git rev-list master..topic

	if this is empty, it is fully merged to "master".

DOC_END
```

## File: `hooks/pre-receive.sample`
```
#!/bin/sh
#
# An example hook script to make use of push options.
# The example simply echoes all push options that start with 'echoback='
# and rejects all pushes when the "reject" push option is used.
#
# To enable this hook, rename this file to "pre-receive".

if test -n "$GIT_PUSH_OPTION_COUNT"
then
	i=0
	while test "$i" -lt "$GIT_PUSH_OPTION_COUNT"
	do
		eval "value=\$GIT_PUSH_OPTION_$i"
		case "$value" in
		echoback=*)
			echo "echo from the pre-receive-hook: ${value#*=}" >&2
			;;
		reject)
			exit 1
		esac
		i=$((i + 1))
	done
fi
```

## File: `hooks/prepare-commit-msg.sample`
```
#!/bin/sh
#
# An example hook script to prepare the commit log message.
# Called by "git commit" with the name of the file that has the
# commit message, followed by the description of the commit
# message's source.  The hook's purpose is to edit the commit
# message file.  If the hook fails with a non-zero status,
# the commit is aborted.
#
# To enable this hook, rename this file to "prepare-commit-msg".

# This hook includes three examples. The first one removes the
# "# Please enter the commit message..." help message.
#
# The second includes the output of "git diff --name-status -r"
# into the message, just before the "git status" output.  It is
# commented because it doesn't cope with --amend or with squashed
# commits.
#
# The third example adds a Signed-off-by line to the message, that can
# still be edited.  This is rarely a good idea.

COMMIT_MSG_FILE=$1
COMMIT_SOURCE=$2
SHA1=$3

/usr/bin/perl -i.bak -ne 'print unless(m/^. Please enter the commit message/..m/^#$/)' "$COMMIT_MSG_FILE"

# case "$COMMIT_SOURCE,$SHA1" in
#  ,|template,)
#    /usr/bin/perl -i.bak -pe '
#       print "\n" . `git diff --cached --name-status -r`
# 	 if /^#/ && $first++ == 0' "$COMMIT_MSG_FILE" ;;
#  *) ;;
# esac

# SOB=$(git var GIT_COMMITTER_IDENT | sed -n 's/^\(.*>\).*$/Signed-off-by: \1/p')
# git interpret-trailers --in-place --trailer "$SOB" "$COMMIT_MSG_FILE"
# if test -z "$COMMIT_SOURCE"
# then
#   /usr/bin/perl -i.bak -pe 'print "\n" if !$first_line++' "$COMMIT_MSG_FILE"
# fi
```

## File: `hooks/push-to-checkout.sample`
```
#!/bin/sh

# An example hook script to update a checked-out tree on a git push.
#
# This hook is invoked by git-receive-pack(1) when it reacts to git
# push and updates reference(s) in its repository, and when the push
# tries to update the branch that is currently checked out and the
# receive.denyCurrentBranch configuration variable is set to
# updateInstead.
#
# By default, such a push is refused if the working tree and the index
# of the remote repository has any difference from the currently
# checked out commit; when both the working tree and the index match
# the current commit, they are updated to match the newly pushed tip
# of the branch. This hook is to be used to override the default
# behaviour; however the code below reimplements the default behaviour
# as a starting point for convenient modification.
#
# The hook receives the commit with which the tip of the current
# branch is going to be updated:
commit=$1

# It can exit with a non-zero status to refuse the push (when it does
# so, it must not modify the index or the working tree).
die () {
	echo >&2 "$*"
	exit 1
}

# Or it can make any necessary changes to the working tree and to the
# index to bring them to the desired state when the tip of the current
# branch is updated to the new commit, and exit with a zero status.
#
# For example, the hook can simply run git read-tree -u -m HEAD "$1"
# in order to emulate git fetch that is run in the reverse direction
# with git push, as the two-tree form of git read-tree -u -m is
# essentially the same as git switch or git checkout that switches
# branches while keeping the local changes in the working tree that do
# not interfere with the difference between the branches.

# The below is a more-or-less exact translation to shell of the C code
# for the default behaviour for git's push-to-checkout hook defined in
# the push_to_deploy() function in builtin/receive-pack.c.
#
# Note that the hook will be executed from the repository directory,
# not from the working tree, so if you want to perform operations on
# the working tree, you will have to adapt your code accordingly, e.g.
# by adding "cd .." or using relative paths.

if ! git update-index -q --ignore-submodules --refresh
then
	die "Up-to-date check failed"
fi

if ! git diff-files --quiet --ignore-submodules --
then
	die "Working directory has unstaged changes"
fi

# This is a rough translation of:
#
#   head_has_history() ? "HEAD" : EMPTY_TREE_SHA1_HEX
if git cat-file -e HEAD 2>/dev/null
then
	head=HEAD
else
	head=$(git hash-object -t tree --stdin </dev/null)
fi

if ! git diff-index --quiet --cached --ignore-submodules $head --
then
	die "Working directory has staged changes"
fi

if ! git read-tree -u -m "$commit"
then
	die "Could not update working tree to new HEAD"
fi
```

## File: `hooks/sendemail-validate.sample`
```
#!/bin/sh

# An example hook script to validate a patch (and/or patch series) before
# sending it via email.
#
# The hook should exit with non-zero status after issuing an appropriate
# message if it wants to prevent the email(s) from being sent.
#
# To enable this hook, rename this file to "sendemail-validate".
#
# By default, it will only check that the patch(es) can be applied on top of
# the default upstream branch without conflicts in a secondary worktree. After
# validation (successful or not) of the last patch of a series, the worktree
# will be deleted.
#
# The following config variables can be set to change the default remote and
# remote ref that are used to apply the patches against:
#
#   sendemail.validateRemote (default: origin)
#   sendemail.validateRemoteRef (default: HEAD)
#
# Replace the TODO placeholders with appropriate checks according to your
# needs.

validate_cover_letter () {
	file="$1"
	# TODO: Replace with appropriate checks (e.g. spell checking).
	true
}

validate_patch () {
	file="$1"
	# Ensure that the patch applies without conflicts.
	git am -3 "$file" || return
	# TODO: Replace with appropriate checks for this patch
	# (e.g. checkpatch.pl).
	true
}

validate_series () {
	# TODO: Replace with appropriate checks for the whole series
	# (e.g. quick build, coding style checks, etc.).
	true
}

# main -------------------------------------------------------------------------

if test "$GIT_SENDEMAIL_FILE_COUNTER" = 1
then
	remote=$(git config --default origin --get sendemail.validateRemote) &&
	ref=$(git config --default HEAD --get sendemail.validateRemoteRef) &&
	worktree=$(mktemp --tmpdir -d sendemail-validate.XXXXXXX) &&
	git worktree add -fd --checkout "$worktree" "refs/remotes/$remote/$ref" &&
	git config --replace-all sendemail.validateWorktree "$worktree"
else
	worktree=$(git config --get sendemail.validateWorktree)
fi || {
	echo "sendemail-validate: error: failed to prepare worktree" >&2
	exit 1
}

unset GIT_DIR GIT_WORK_TREE
cd "$worktree" &&

if grep -q "^diff --git " "$1"
then
	validate_patch "$1"
else
	validate_cover_letter "$1"
fi &&

if test "$GIT_SENDEMAIL_FILE_COUNTER" = "$GIT_SENDEMAIL_FILE_TOTAL"
then
	git config --unset-all sendemail.validateWorktree &&
	trap 'git worktree remove -ff "$worktree"' EXIT &&
	validate_series
fi
```

## File: `hooks/update.sample`
```
#!/bin/sh
#
# An example hook script to block unannotated tags from entering.
# Called by "git receive-pack" with arguments: refname sha1-old sha1-new
#
# To enable this hook, rename this file to "update".
#
# Config
# ------
# hooks.allowunannotated
#   This boolean sets whether unannotated tags will be allowed into the
#   repository.  By default they won't be.
# hooks.allowdeletetag
#   This boolean sets whether deleting tags will be allowed in the
#   repository.  By default they won't be.
# hooks.allowmodifytag
#   This boolean sets whether a tag may be modified after creation. By default
#   it won't be.
# hooks.allowdeletebranch
#   This boolean sets whether deleting branches will be allowed in the
#   repository.  By default they won't be.
# hooks.denycreatebranch
#   This boolean sets whether remotely creating branches will be denied
#   in the repository.  By default this is allowed.
#

# --- Command line
refname="$1"
oldrev="$2"
newrev="$3"

# --- Safety check
if [ -z "$GIT_DIR" ]; then
	echo "Don't run this script from the command line." >&2
	echo " (if you want, you could supply GIT_DIR then run" >&2
	echo "  $0 <ref> <oldrev> <newrev>)" >&2
	exit 1
fi

if [ -z "$refname" -o -z "$oldrev" -o -z "$newrev" ]; then
	echo "usage: $0 <ref> <oldrev> <newrev>" >&2
	exit 1
fi

# --- Config
allowunannotated=$(git config --type=bool hooks.allowunannotated)
allowdeletebranch=$(git config --type=bool hooks.allowdeletebranch)
denycreatebranch=$(git config --type=bool hooks.denycreatebranch)
allowdeletetag=$(git config --type=bool hooks.allowdeletetag)
allowmodifytag=$(git config --type=bool hooks.allowmodifytag)

# check for no description
projectdesc=$(sed -e '1q' "$GIT_DIR/description")
case "$projectdesc" in
"Unnamed repository"* | "")
	echo "*** Project description file hasn't been set" >&2
	exit 1
	;;
esac

# --- Check types
# if $newrev is 0000...0000, it's a commit to delete a ref.
zero=$(git hash-object --stdin </dev/null | tr '[0-9a-f]' '0')
if [ "$newrev" = "$zero" ]; then
	newrev_type=delete
else
	newrev_type=$(git cat-file -t $newrev)
fi

case "$refname","$newrev_type" in
	refs/tags/*,commit)
		# un-annotated tag
		short_refname=${refname##refs/tags/}
		if [ "$allowunannotated" != "true" ]; then
			echo "*** The un-annotated tag, $short_refname, is not allowed in this repository" >&2
			echo "*** Use 'git tag [ -a | -s ]' for tags you want to propagate." >&2
			exit 1
		fi
		;;
	refs/tags/*,delete)
		# delete tag
		if [ "$allowdeletetag" != "true" ]; then
			echo "*** Deleting a tag is not allowed in this repository" >&2
			exit 1
		fi
		;;
	refs/tags/*,tag)
		# annotated tag
		if [ "$allowmodifytag" != "true" ] && git rev-parse $refname > /dev/null 2>&1
		then
			echo "*** Tag '$refname' already exists." >&2
			echo "*** Modifying a tag is not allowed in this repository." >&2
			exit 1
		fi
		;;
	refs/heads/*,commit)
		# branch
		if [ "$oldrev" = "$zero" -a "$denycreatebranch" = "true" ]; then
			echo "*** Creating a branch is not allowed in this repository" >&2
			exit 1
		fi
		;;
	refs/heads/*,delete)
		# delete branch
		if [ "$allowdeletebranch" != "true" ]; then
			echo "*** Deleting a branch is not allowed in this repository" >&2
			exit 1
		fi
		;;
	refs/remotes/*,commit)
		# tracking branch
		;;
	refs/remotes/*,delete)
		# delete tracking branch
		if [ "$allowdeletebranch" != "true" ]; then
			echo "*** Deleting a tracking branch is not allowed in this repository" >&2
			exit 1
		fi
		;;
	*)
		# Anything else (is there anything else?)
		echo "*** Update hook: unknown type of update to ref $refname of type $newrev_type" >&2
		exit 1
		;;
esac

# --- Finished
exit 0
```

## File: `info/exclude`
```
# git ls-files --others --exclude-from=.git/info/exclude
# Lines that start with '#' are comments.
# For a project mostly in C, the following would be a good set of
# exclude patterns (uncomment them if you want to use them):
# *.[oa]
# *~
```

## File: `logs/HEAD`
```
0000000000000000000000000000000000000000 3a58e3294da6230472e2c6337417a9e6f796d46b MaiKhue <R9000P 2021@MaiKhue.(none)> 1775030241 +0700	clone: from https://github.com/CodelyTV/java-ddd-example
```

## File: `logs/refs/heads/main`
```
0000000000000000000000000000000000000000 3a58e3294da6230472e2c6337417a9e6f796d46b MaiKhue <R9000P 2021@MaiKhue.(none)> 1775030241 +0700	clone: from https://github.com/CodelyTV/java-ddd-example
```

## File: `logs/refs/remotes/origin/HEAD`
```
0000000000000000000000000000000000000000 3a58e3294da6230472e2c6337417a9e6f796d46b MaiKhue <R9000P 2021@MaiKhue.(none)> 1775030241 +0700	clone: from https://github.com/CodelyTV/java-ddd-example
```

## File: `refs/heads/main`
```
3a58e3294da6230472e2c6337417a9e6f796d46b
```

## File: `refs/remotes/origin/HEAD`
```
ref: refs/remotes/origin/main
```

## File: `src/analytics/main/tv/codely/analytics/domain_events/application/store/DomainEventStorer.java`
```java
package tv.codely.analytics.domain_events.application.store;

import tv.codely.analytics.domain_events.domain.*;

public final class DomainEventStorer {
    private DomainEventsRepository repository;

    public DomainEventStorer(DomainEventsRepository repository) {
        this.repository = repository;
    }

    public void store(
        AnalyticsDomainEventId id,
        AnalyticsDomainEventAggregateId aggregateId,
        AnalyticsDomainEventName name,
        AnalyticsDomainEventBody body
    ) {
        AnalyticsDomainEvent domainEvent = new AnalyticsDomainEvent(id, aggregateId, name, body);

        repository.save(domainEvent);
    }
}
```

## File: `src/analytics/main/tv/codely/analytics/domain_events/application/store/StoreDomainEventOnOccurred.java`
```java
package tv.codely.analytics.domain_events.application.store;

import org.springframework.context.event.EventListener;
import tv.codely.analytics.domain_events.domain.AnalyticsDomainEventAggregateId;
import tv.codely.analytics.domain_events.domain.AnalyticsDomainEventBody;
import tv.codely.analytics.domain_events.domain.AnalyticsDomainEventId;
import tv.codely.analytics.domain_events.domain.AnalyticsDomainEventName;
import tv.codely.shared.domain.bus.event.DomainEvent;
import tv.codely.shared.domain.bus.event.DomainEventSubscriber;

@DomainEventSubscriber({DomainEvent.class})
public final class StoreDomainEventOnOccurred {
    private final DomainEventStorer storer;

    public StoreDomainEventOnOccurred(DomainEventStorer storer) {
        this.storer = storer;
    }

    @EventListener
    public void on(DomainEvent event) {
        AnalyticsDomainEventId          id          = new AnalyticsDomainEventId(event.eventId());
        AnalyticsDomainEventAggregateId aggregateId = new AnalyticsDomainEventAggregateId(event.aggregateId());
        AnalyticsDomainEventName        name        = new AnalyticsDomainEventName(event.eventName());
        AnalyticsDomainEventBody        body        = new AnalyticsDomainEventBody(event.toPrimitives());

        storer.store(id, aggregateId, name, body);
    }
}
```

## File: `src/analytics/main/tv/codely/analytics/domain_events/domain/AnalyticsDomainEvent.java`
```java
package tv.codely.analytics.domain_events.domain;

public final class AnalyticsDomainEvent {
    private final AnalyticsDomainEventId          id;
    private final AnalyticsDomainEventAggregateId aggregateId;
    private final AnalyticsDomainEventName        name;
    private final AnalyticsDomainEventBody        body;

    public AnalyticsDomainEvent(
        AnalyticsDomainEventId id,
        AnalyticsDomainEventAggregateId aggregateId,
        AnalyticsDomainEventName name,
        AnalyticsDomainEventBody body
    ) {

        this.id          = id;
        this.aggregateId = aggregateId;
        this.name        = name;
        this.body        = body;
    }

    public AnalyticsDomainEventId getId() {
        return id;
    }

    public AnalyticsDomainEventAggregateId getAggregateId() {
        return aggregateId;
    }

    public AnalyticsDomainEventName getName() {
        return name;
    }

    public AnalyticsDomainEventBody getBody() {
        return body;
    }
}
```

## File: `src/analytics/main/tv/codely/analytics/domain_events/domain/AnalyticsDomainEventAggregateId.java`
```java
package tv.codely.analytics.domain_events.domain;

import tv.codely.shared.domain.Identifier;

public final class AnalyticsDomainEventAggregateId extends Identifier {
    public AnalyticsDomainEventAggregateId(String value) {
        super(value);
    }
}
```

## File: `src/analytics/main/tv/codely/analytics/domain_events/domain/AnalyticsDomainEventBody.java`
```java
package tv.codely.analytics.domain_events.domain;

import java.io.Serializable;
import java.util.HashMap;

public final class AnalyticsDomainEventBody {
    private HashMap<String, Serializable> value;

    public HashMap<String, Serializable> getValue() {
        return value;
    }

    public AnalyticsDomainEventBody(HashMap<String, Serializable> value) {
        this.value = value;
    }
}
```

## File: `src/analytics/main/tv/codely/analytics/domain_events/domain/AnalyticsDomainEventId.java`
```java
package tv.codely.analytics.domain_events.domain;

import tv.codely.shared.domain.Identifier;

public final class AnalyticsDomainEventId extends Identifier {
    public AnalyticsDomainEventId(String value) {
        super(value);
    }
}
```

## File: `src/analytics/main/tv/codely/analytics/domain_events/domain/AnalyticsDomainEventName.java`
```java
package tv.codely.analytics.domain_events.domain;

import tv.codely.shared.domain.StringValueObject;

public final class AnalyticsDomainEventName extends StringValueObject {
    public AnalyticsDomainEventName(String value) {
        super(value);
    }
}
```

## File: `src/analytics/main/tv/codely/analytics/domain_events/domain/DomainEventsRepository.java`
```java
package tv.codely.analytics.domain_events.domain;

public interface DomainEventsRepository {
    void save(AnalyticsDomainEvent event);
}
```

## File: `src/backoffice/build.gradle`
```
dependencies {
}
```

## File: `src/backoffice/main/resources/database/backoffice.sql`
```sql
CREATE TABLE IF NOT EXISTS `courses` (
    `id` CHAR(36) NOT NULL,
    `name` VARCHAR(255) NOT NULL,
    `duration` VARCHAR(255) NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
```

## File: `src/backoffice/main/resources/database/backoffice/backoffice_courses.json`
```json
{
  "mappings": {
    "courses": {
      "properties": {
        "id": {
          "type": "keyword",
          "index": true
        },
        "name": {
          "type": "text",
          "index": true,
          "fielddata": true
        },
        "duration": {
          "type": "text",
          "index": true,
          "fielddata": true
        }
      }
    }
  }
}
```

## File: `src/backoffice/main/tv/codely/backoffice/auth/application/authenticate/AuthenticateUserCommand.java`
```java
package tv.codely.backoffice.auth.application.authenticate;

import tv.codely.shared.domain.bus.command.Command;

public final class AuthenticateUserCommand implements Command {
    private final String username;
    private final String password;

    public AuthenticateUserCommand(String username, String password) {
        this.username = username;
        this.password = password;
    }

    public String username() {
        return username;
    }

    public String password() {
        return password;
    }
}
```

## File: `src/backoffice/main/tv/codely/backoffice/auth/application/authenticate/AuthenticateUserCommandHandler.java`
```java
package tv.codely.backoffice.auth.application.authenticate;

import tv.codely.backoffice.auth.domain.AuthPassword;
import tv.codely.backoffice.auth.domain.AuthUsername;
import tv.codely.shared.domain.Service;
import tv.codely.shared.domain.bus.command.CommandHandler;

@Service
public final class AuthenticateUserCommandHandler implements CommandHandler<AuthenticateUserCommand> {
    private final UserAuthenticator authenticator;

    public AuthenticateUserCommandHandler(UserAuthenticator authenticator) {
        this.authenticator = authenticator;
    }

    @Override
    public void handle(AuthenticateUserCommand command) {
        AuthUsername username = new AuthUsername(command.username());
        AuthPassword password = new AuthPassword(command.password());

        authenticator.authenticate(username, password);
    }
}
```

## File: `src/backoffice/main/tv/codely/backoffice/auth/application/authenticate/UserAuthenticator.java`
```java
package tv.codely.backoffice.auth.application.authenticate;

import tv.codely.backoffice.auth.domain.*;
import tv.codely.shared.domain.Service;

import java.util.Optional;

@Service
public final class UserAuthenticator {
    private final AuthRepository repository;

    public UserAuthenticator(AuthRepository repository) {
        this.repository = repository;
    }

    public void authenticate(AuthUsername username, AuthPassword password) {
        Optional<AuthUser> auth = repository.search(username);

        ensureUserExist(auth, username);
        ensureCredentialsAreValid(auth.get(), password);
    }

    private void ensureUserExist(Optional<AuthUser> auth, AuthUsername username) {
        if (!auth.isPresent()) {
            throw new InvalidAuthUsername(username);
        }
    }

    private void ensureCredentialsAreValid(AuthUser auth, AuthPassword password) {
        if (!auth.passwordMatches(password)) {
            throw new InvalidAuthCredentials(auth.username());
        }
    }
}
```

## File: `src/backoffice/main/tv/codely/backoffice/auth/domain/AuthPassword.java`
```java
package tv.codely.backoffice.auth.domain;

import tv.codely.shared.domain.StringValueObject;

public final class AuthPassword extends StringValueObject {
    public AuthPassword(String value) {
        super(value);
    }
}
```

## File: `src/backoffice/main/tv/codely/backoffice/auth/domain/AuthRepository.java`
```java
package tv.codely.backoffice.auth.domain;

import java.util.Optional;

public interface AuthRepository {
    Optional<AuthUser> search(AuthUsername username);
}
```

## File: `src/backoffice/main/tv/codely/backoffice/auth/domain/AuthUser.java`
```java
package tv.codely.backoffice.auth.domain;

public final class AuthUser {
    private final AuthUsername username;
    private final AuthPassword password;

    public AuthUser(AuthUsername username, AuthPassword password) {
        this.username = username;
        this.password = password;
    }

    public AuthUsername username() {
        return username;
    }

    public boolean passwordMatches(AuthPassword password) {
        return this.password.equals(password);
    }
}
```

## File: `src/backoffice/main/tv/codely/backoffice/auth/domain/AuthUsername.java`
```java
package tv.codely.backoffice.auth.domain;

import tv.codely.shared.domain.StringValueObject;

public final class AuthUsername extends StringValueObject {
    public AuthUsername(String value) {
        super(value);
    }
}
```

## File: `src/backoffice/main/tv/codely/backoffice/auth/domain/InvalidAuthCredentials.java`
```java
package tv.codely.backoffice.auth.domain;

public final class InvalidAuthCredentials extends RuntimeException {
    public InvalidAuthCredentials(AuthUsername username) {
        super(String.format("The credentials for <%s> are invalid", username.value()));
    }
}
```

## File: `src/backoffice/main/tv/codely/backoffice/auth/domain/InvalidAuthUsername.java`
```java
package tv.codely.backoffice.auth.domain;

public final class InvalidAuthUsername extends RuntimeException {
    public InvalidAuthUsername(AuthUsername username) {
        super(String.format("The user <%s> does not exist", username.value()));
    }
}
```

## File: `src/backoffice/main/tv/codely/backoffice/auth/infrastructure/persistence/InMemoryAuthRepository.java`
```java
package tv.codely.backoffice.auth.infrastructure.persistence;

import tv.codely.backoffice.auth.domain.AuthPassword;
import tv.codely.backoffice.auth.domain.AuthRepository;
import tv.codely.backoffice.auth.domain.AuthUser;
import tv.codely.backoffice.auth.domain.AuthUsername;
import tv.codely.shared.domain.Service;

import java.util.HashMap;
import java.util.Optional;

@Service
public final class InMemoryAuthRepository implements AuthRepository {
    private final HashMap<AuthUsername, AuthPassword> users = new HashMap<AuthUsername, AuthPassword>() {{
        put(new AuthUsername("javi"), new AuthPassword("barbitas"));
        put(new AuthUsername("rafa"), new AuthPassword("pelazo"));
    }};

    @Override
    public Optional<AuthUser> search(AuthUsername username) {
        return users.containsKey(username)
            ? Optional.of(new AuthUser(username, users.get(username)))
            : Optional.empty();
    }
}
```

## File: `src/backoffice/main/tv/codely/backoffice/courses/application/BackofficeCourseResponse.java`
```java
package tv.codely.backoffice.courses.application;

import tv.codely.backoffice.courses.domain.BackofficeCourse;
import tv.codely.shared.domain.bus.query.Response;

public final class BackofficeCourseResponse implements Response {
    private final String id;
    private final String name;
    private final String duration;

    public BackofficeCourseResponse(String id, String name, String duration) {
        this.id       = id;
        this.name     = name;
        this.duration = duration;
    }

    public static BackofficeCourseResponse fromAggregate(BackofficeCourse course) {
        return new BackofficeCourseResponse(course.id(), course.name(), course.duration());
    }

    public String id() {
        return id;
    }

    public String name() {
        return name;
    }

    public String duration() {
        return duration;
    }
}
```

## File: `src/backoffice/main/tv/codely/backoffice/courses/application/BackofficeCoursesResponse.java`
```java
package tv.codely.backoffice.courses.application;

import tv.codely.shared.domain.bus.query.Response;

import java.util.List;

public final class BackofficeCoursesResponse implements Response {
    private final List<BackofficeCourseResponse> courses;

    public BackofficeCoursesResponse(List<BackofficeCourseResponse> courses) {
        this.courses = courses;
    }

    public List<BackofficeCourseResponse> courses() {
        return courses;
    }
}
```

## File: `src/backoffice/main/tv/codely/backoffice/courses/application/create/BackofficeCourseCreator.java`
```java
package tv.codely.backoffice.courses.application.create;

import tv.codely.backoffice.courses.domain.BackofficeCourse;
import tv.codely.backoffice.courses.domain.BackofficeCourseRepository;
import tv.codely.shared.domain.Service;

@Service
public final class BackofficeCourseCreator {
    private final BackofficeCourseRepository repository;

    public BackofficeCourseCreator(BackofficeCourseRepository repository) {
        this.repository = repository;
    }

    public void create(String id, String name, String duration) {
        this.repository.save(new BackofficeCourse(id, name, duration));
    }
}
```

## File: `src/backoffice/main/tv/codely/backoffice/courses/application/create/CreateBackofficeCourseOnCourseCreated.java`
```java
package tv.codely.backoffice.courses.application.create;

import org.springframework.context.event.EventListener;
import tv.codely.shared.domain.Service;
import tv.codely.shared.domain.bus.event.DomainEventSubscriber;
import tv.codely.shared.domain.course.CourseCreatedDomainEvent;

@Service
@DomainEventSubscriber({CourseCreatedDomainEvent.class})
public final class CreateBackofficeCourseOnCourseCreated {
    private final BackofficeCourseCreator creator;

    public CreateBackofficeCourseOnCourseCreated(BackofficeCourseCreator creator) {
        this.creator = creator;
    }

    @EventListener
    public void on(CourseCreatedDomainEvent event) {
        creator.create(event.aggregateId(), event.name(), event.duration());
    }
}
```

## File: `src/backoffice/main/tv/codely/backoffice/courses/application/search_all/AllBackofficeCoursesSearcher.java`
```java
package tv.codely.backoffice.courses.application.search_all;

import tv.codely.backoffice.courses.application.BackofficeCourseResponse;
import tv.codely.backoffice.courses.application.BackofficeCoursesResponse;
import tv.codely.backoffice.courses.domain.BackofficeCourseRepository;
import tv.codely.shared.domain.Service;

import java.util.stream.Collectors;

@Service
public final class AllBackofficeCoursesSearcher {
    private final BackofficeCourseRepository repository;

    public AllBackofficeCoursesSearcher(BackofficeCourseRepository repository) {
        this.repository = repository;
    }

    public BackofficeCoursesResponse search() {
        return new BackofficeCoursesResponse(
            repository.searchAll().stream().map(BackofficeCourseResponse::fromAggregate).collect(Collectors.toList())
        );
    }
}
```

## File: `src/backoffice/main/tv/codely/backoffice/courses/application/search_all/SearchAllBackofficeCoursesQuery.java`
```java
package tv.codely.backoffice.courses.application.search_all;

import tv.codely.shared.domain.bus.query.Query;

public final class SearchAllBackofficeCoursesQuery implements Query {
}
```

## File: `src/backoffice/main/tv/codely/backoffice/courses/application/search_all/SearchAllBackofficeCoursesQueryHandler.java`
```java
package tv.codely.backoffice.courses.application.search_all;

import tv.codely.backoffice.courses.application.BackofficeCoursesResponse;
import tv.codely.shared.domain.Service;
import tv.codely.shared.domain.bus.query.QueryHandler;

@Service
public final class SearchAllBackofficeCoursesQueryHandler implements QueryHandler<SearchAllBackofficeCoursesQuery, BackofficeCoursesResponse> {
    private final AllBackofficeCoursesSearcher searcher;

    public SearchAllBackofficeCoursesQueryHandler(AllBackofficeCoursesSearcher searcher) {
        this.searcher = searcher;
    }

    @Override
    public BackofficeCoursesResponse handle(SearchAllBackofficeCoursesQuery query) {
        return searcher.search();
    }
}
```

## File: `src/backoffice/main/tv/codely/backoffice/courses/application/search_by_criteria/BackofficeCoursesByCriteriaSearcher.java`
```java
package tv.codely.backoffice.courses.application.search_by_criteria;

import tv.codely.backoffice.courses.application.BackofficeCourseResponse;
import tv.codely.backoffice.courses.application.BackofficeCoursesResponse;
import tv.codely.backoffice.courses.domain.BackofficeCourseRepository;
import tv.codely.shared.domain.Service;
import tv.codely.shared.domain.criteria.Criteria;
import tv.codely.shared.domain.criteria.Filters;
import tv.codely.shared.domain.criteria.Order;

import java.util.Optional;
import java.util.stream.Collectors;

@Service
public final class BackofficeCoursesByCriteriaSearcher {
    private final BackofficeCourseRepository repository;

    public BackofficeCoursesByCriteriaSearcher(BackofficeCourseRepository repository) {
        this.repository = repository;
    }

    public BackofficeCoursesResponse search(
        Filters filters,
        Order order,
        Optional<Integer> limit,
        Optional<Integer> offset
    ) {
        Criteria criteria = new Criteria(filters, order, limit, offset);

        return new BackofficeCoursesResponse(
            repository.matching(criteria)
                      .stream()
                      .map(BackofficeCourseResponse::fromAggregate)
                      .collect(Collectors.toList())
        );
    }
}
```

## File: `src/backoffice/main/tv/codely/backoffice/courses/application/search_by_criteria/SearchBackofficeCoursesByCriteriaQuery.java`
```java
package tv.codely.backoffice.courses.application.search_by_criteria;

import tv.codely.shared.domain.bus.query.Query;

import java.util.HashMap;
import java.util.List;
import java.util.Optional;

public final class SearchBackofficeCoursesByCriteriaQuery implements Query {
    private final List<HashMap<String, String>> filters;
    private final Optional<String>              orderBy;
    private final Optional<String>              orderType;
    private final Optional<Integer>             limit;
    private final Optional<Integer>             offset;

    public SearchBackofficeCoursesByCriteriaQuery(
        List<HashMap<String, String>> filters,
        Optional<String> orderBy,
        Optional<String> orderType,
        Optional<Integer> limit,
        Optional<Integer> offset
    ) {
        this.filters   = filters;
        this.orderBy   = orderBy;
        this.orderType = orderType;
        this.limit     = limit;
        this.offset    = offset;
    }

    public List<HashMap<String, String>> filters() {
        return filters;
    }

    public Optional<String> orderBy() {
        return orderBy;
    }

    public Optional<String> orderType() {
        return orderType;
    }

    public Optional<Integer> limit() {
        return limit;
    }

    public Optional<Integer> offset() {
        return offset;
    }
}
```

## File: `src/backoffice/main/tv/codely/backoffice/courses/domain/BackofficeCourse.java`
```java
package tv.codely.backoffice.courses.domain;

import java.io.Serializable;
import java.util.HashMap;
import java.util.Map;
import java.util.Objects;

public final class BackofficeCourse {
    private final String id;
    private final String name;
    private final String duration;

    public BackofficeCourse() {
        id       = null;
        name     = null;
        duration = null;
    }

    public BackofficeCourse(String id, String name, String duration) {
        this.id       = id;
        this.name     = name;
        this.duration = duration;
    }

    public static BackofficeCourse fromPrimitives(Map<String, Object> plainData) {
        return new BackofficeCourse(
            (String) plainData.get("id"),
            (String) plainData.get("name"),
            (String) plainData.get("duration")
        );
    }

    public String id() {
        return id;
    }

    public String name() {
        return name;
    }

    public String duration() {
        return duration;
    }

    public HashMap<String, Serializable> toPrimitives() {
        return new HashMap<String, Serializable>() {{
            put("id", id);
            put("name", name);
            put("duration", duration);
        }};
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) {
            return true;
        }
        if (o == null || getClass() != o.getClass()) {
            return false;
        }
        BackofficeCourse that = (BackofficeCourse) o;
        return id.equals(that.id) &&
               name.equals(that.name) &&
               duration.equals(that.duration);
    }

    @Override
    public int hashCode() {
        return Objects.hash(id, name, duration);
    }
}
```

## File: `src/backoffice/main/tv/codely/backoffice/courses/domain/BackofficeCourseRepository.java`
```java
package tv.codely.backoffice.courses.domain;

import tv.codely.shared.domain.criteria.Criteria;

import java.util.List;

public interface BackofficeCourseRepository {
    void save(BackofficeCourse course);

    List<BackofficeCourse> searchAll();

    List<BackofficeCourse> matching(Criteria criteria);
}
```

## File: `src/backoffice/main/tv/codely/backoffice/courses/infrastructure/persistence/ElasticsearchBackofficeCourseRepository.java`
```java
package tv.codely.backoffice.courses.infrastructure.persistence;

import org.springframework.context.annotation.Primary;
import tv.codely.backoffice.courses.domain.BackofficeCourse;
import tv.codely.backoffice.courses.domain.BackofficeCourseRepository;
import tv.codely.shared.domain.Service;
import tv.codely.shared.domain.criteria.Criteria;
import tv.codely.shared.infrastructure.elasticsearch.ElasticsearchClient;
import tv.codely.shared.infrastructure.elasticsearch.ElasticsearchRepository;

import java.util.List;

@Primary
@Service
public final class ElasticsearchBackofficeCourseRepository extends ElasticsearchRepository<BackofficeCourse> implements BackofficeCourseRepository {
    public ElasticsearchBackofficeCourseRepository(ElasticsearchClient client) {
        super(client);
    }

    @Override
    public void save(BackofficeCourse course) {
        persist(course.id(), course.toPrimitives());
    }

    @Override
    public List<BackofficeCourse> searchAll() {
        return searchAllInElastic(BackofficeCourse::fromPrimitives);
    }

    @Override
    public List<BackofficeCourse> matching(Criteria criteria) {
        return searchByCriteria(criteria, BackofficeCourse::fromPrimitives);
    }

    @Override
    protected String moduleName() {
        return "courses";
    }
}
```

## File: `src/backoffice/main/tv/codely/backoffice/courses/infrastructure/persistence/InMemoryCacheBackofficeCourseRepository.java`
```java
package tv.codely.backoffice.courses.infrastructure.persistence;

import tv.codely.backoffice.courses.domain.BackofficeCourse;
import tv.codely.backoffice.courses.domain.BackofficeCourseRepository;
import tv.codely.shared.domain.criteria.Criteria;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

public final class InMemoryCacheBackofficeCourseRepository implements BackofficeCourseRepository {
    private final BackofficeCourseRepository              repository;
    private       List<BackofficeCourse>                  courses         = new ArrayList<>();
    private       HashMap<String, List<BackofficeCourse>> matchingCourses = new HashMap<>();

    public InMemoryCacheBackofficeCourseRepository(BackofficeCourseRepository repository) {
        this.repository = repository;
    }

    @Override
    public void save(BackofficeCourse course) {
        repository.save(course);
    }

    @Override
    public List<BackofficeCourse> searchAll() {
        return courses.isEmpty() ? searchAndFillCache() : courses;
    }

    @Override
    public List<BackofficeCourse> matching(Criteria criteria) {
        return matchingCourses.containsKey(criteria.serialize())
            ? matchingCourses.get(criteria.serialize())
            : searchMatchingAndFillCache(criteria);
    }

    private List<BackofficeCourse> searchMatchingAndFillCache(Criteria criteria) {
        List<BackofficeCourse> courses = repository.matching(criteria);

        this.matchingCourses.put(criteria.serialize(), courses);

        return courses;
    }

    private List<BackofficeCourse> searchAndFillCache() {
        List<BackofficeCourse> courses = repository.searchAll();

        this.courses = courses;

        return courses;
    }
}
```

## File: `src/backoffice/main/tv/codely/backoffice/courses/infrastructure/persistence/MySqlBackofficeCourseRepository.java`
```java
package tv.codely.backoffice.courses.infrastructure.persistence;

import org.hibernate.SessionFactory;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.transaction.annotation.Transactional;
import tv.codely.backoffice.courses.domain.BackofficeCourse;
import tv.codely.backoffice.courses.domain.BackofficeCourseRepository;
import tv.codely.shared.domain.Service;
import tv.codely.shared.domain.criteria.Criteria;
import tv.codely.shared.infrastructure.hibernate.HibernateRepository;

import java.util.List;

@Service
@Transactional("backoffice-transaction_manager")
public class MySqlBackofficeCourseRepository extends HibernateRepository<BackofficeCourse> implements BackofficeCourseRepository {
    public MySqlBackofficeCourseRepository(@Qualifier("backoffice-session_factory") SessionFactory sessionFactory) {
        super(sessionFactory, BackofficeCourse.class);
    }

    @Override
    public void save(BackofficeCourse course) {
        persist(course);
    }

    @Override
    public List<BackofficeCourse> searchAll() {
        return all();
    }

    @Override
    public List<BackofficeCourse> matching(Criteria criteria) {
        return byCriteria(criteria);
    }
}
```

## File: `src/backoffice/main/tv/codely/backoffice/courses/infrastructure/persistence/hibernate/BackofficeCourse.hbm.xml`
```xml
<?xml version = "1.0" encoding = "utf-8"?>
<!DOCTYPE hibernate-mapping PUBLIC
        "-//Hibernate/Hibernate Mapping DTD//EN"
        "http://www.hibernate.org/dtd/hibernate-mapping-3.0.dtd">

<hibernate-mapping>
    <class name="tv.codely.backoffice.courses.domain.BackofficeCourse" table="courses">
        <id name="id" column="id" access="field" length="36" />

        <property name="name" column="name" type="string" access="field" />

        <property name="duration" column="duration" type="string" access="field" />
    </class>
</hibernate-mapping>
```

## File: `src/backoffice/main/tv/codely/backoffice/shared/infrastructure/persistence/BackofficeElasticsearchConfiguration.java`
```java
package tv.codely.backoffice.shared.infrastructure.persistence;

import org.apache.http.HttpHost;
import org.elasticsearch.client.Request;
import org.elasticsearch.client.RequestOptions;
import org.elasticsearch.client.RestClient;
import org.elasticsearch.client.RestHighLevelClient;
import org.elasticsearch.client.indices.GetIndexRequest;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.core.io.Resource;
import org.springframework.core.io.support.ResourcePatternResolver;
import tv.codely.shared.domain.Utils;
import tv.codely.shared.infrastructure.config.Parameter;
import tv.codely.shared.infrastructure.config.ParameterNotExist;
import tv.codely.shared.infrastructure.elasticsearch.ElasticsearchClient;

import java.io.IOException;
import java.util.Objects;
import java.util.Scanner;

@Configuration
public class BackofficeElasticsearchConfiguration {
    private final Parameter               config;
    private final ResourcePatternResolver resourceResolver;

    public BackofficeElasticsearchConfiguration(Parameter config, ResourcePatternResolver resourceResolver) {
        this.config           = config;
        this.resourceResolver = resourceResolver;
    }

    @Bean
    public ElasticsearchClient elasticsearchClient() throws ParameterNotExist, Exception {
		ElasticsearchClient client = new ElasticsearchClient(
			new RestHighLevelClient(
				RestClient.builder(
					new HttpHost(
						config.get("BACKOFFICE_ELASTICSEARCH_HOST"),
						config.getInt("BACKOFFICE_ELASTICSEARCH_PORT"),
						"http"
					)
				)
			),
			RestClient.builder(
				new HttpHost(
					config.get("BACKOFFICE_ELASTICSEARCH_HOST"),
					config.getInt("BACKOFFICE_ELASTICSEARCH_PORT"),
					"http"
				)).build(),
			config.get("BACKOFFICE_ELASTICSEARCH_INDEX_PREFIX")
		);

		Utils.retry(10, 10000, () -> {
            try {
                generateIndexIfNotExists(client, "backoffice");
            } catch (IOException e) {
                throw new RuntimeException(e);
            }
        });

        return client;
    }

    private void generateIndexIfNotExists(ElasticsearchClient client, String contextName) throws IOException {
        Resource[] jsonsIndexes = resourceResolver.getResources(
            String.format("classpath:database/%s/*.json", contextName)
        );

        for (Resource jsonIndex : jsonsIndexes) {
            String indexName = Objects.requireNonNull(jsonIndex.getFilename()).replace(".json", "");

            if (!indexExists(indexName, client)) {
                String indexBody = new Scanner(
                    jsonIndex.getInputStream(),
                    "UTF-8"
                ).useDelimiter("\\A").next();

                Request request = new Request("PUT", indexName);
                request.setJsonEntity(indexBody);

                client.lowLevelClient().performRequest(request);
            }
        }
    }

    private boolean indexExists(String indexName, ElasticsearchClient client) throws IOException {
        return client.highLevelClient().indices().exists(new GetIndexRequest(indexName), RequestOptions.DEFAULT);
    }
}
```

## File: `src/backoffice/main/tv/codely/backoffice/shared/infrastructure/persistence/BackofficeHibernateConfiguration.java`
```java
package tv.codely.backoffice.shared.infrastructure.persistence;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.orm.hibernate5.LocalSessionFactoryBean;
import org.springframework.transaction.PlatformTransactionManager;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import tv.codely.shared.infrastructure.config.Parameter;
import tv.codely.shared.infrastructure.config.ParameterNotExist;
import tv.codely.shared.infrastructure.hibernate.HibernateConfigurationFactory;

import javax.sql.DataSource;
import java.io.IOException;

@Configuration
@EnableTransactionManagement
public class BackofficeHibernateConfiguration {
    private final HibernateConfigurationFactory factory;
    private final Parameter                     config;
    private final String                        CONTEXT_NAME = "backoffice";

    public BackofficeHibernateConfiguration(HibernateConfigurationFactory factory, Parameter config) {
        this.factory = factory;
        this.config  = config;
    }

    @Bean("backoffice-transaction_manager")
    public PlatformTransactionManager hibernateTransactionManager() throws IOException, ParameterNotExist {
        return factory.hibernateTransactionManager(sessionFactory());
    }

    @Bean("backoffice-session_factory")
    public LocalSessionFactoryBean sessionFactory() throws IOException, ParameterNotExist {
        return factory.sessionFactory(CONTEXT_NAME, dataSource());
    }

    @Bean("backoffice-data_source")
    public DataSource dataSource() throws IOException, ParameterNotExist {
        return factory.dataSource(
            config.get("BACKOFFICE_DATABASE_HOST"),
            config.getInt("BACKOFFICE_DATABASE_PORT"),
            config.get("BACKOFFICE_DATABASE_NAME"),
            config.get("BACKOFFICE_DATABASE_USER"),
            config.get("BACKOFFICE_DATABASE_PASSWORD")
        );
    }
}
```

## File: `src/backoffice/main/tv/codely/backoffice/shared/infrastructure/persistence/BackofficeMySqlEventBusConfiguration.java`
```java
package tv.codely.backoffice.shared.infrastructure.persistence;

import org.hibernate.SessionFactory;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import tv.codely.shared.infrastructure.bus.event.DomainEventsInformation;
import tv.codely.shared.infrastructure.bus.event.mysql.MySqlDomainEventsConsumer;
import tv.codely.shared.infrastructure.bus.event.mysql.MySqlEventBus;
import tv.codely.shared.infrastructure.bus.event.spring.SpringApplicationEventBus;

@Configuration
public class BackofficeMySqlEventBusConfiguration {
    private final SessionFactory            sessionFactory;
    private final DomainEventsInformation   domainEventsInformation;
    private final SpringApplicationEventBus bus;

    public BackofficeMySqlEventBusConfiguration(
        @Qualifier("backoffice-session_factory") SessionFactory sessionFactory,
        DomainEventsInformation domainEventsInformation,
        SpringApplicationEventBus bus
    ) {
        this.sessionFactory          = sessionFactory;
        this.domainEventsInformation = domainEventsInformation;
        this.bus                     = bus;
    }

    @Bean
    public MySqlEventBus backofficeMysqlEventBus() {
        return new MySqlEventBus(sessionFactory);
    }

    @Bean
    public MySqlDomainEventsConsumer backofficeMySqlDomainEventsConsumer() {
        return new MySqlDomainEventsConsumer(sessionFactory, domainEventsInformation, bus);
    }
}
```

## File: `src/backoffice/main/tv/codely/backoffice/shared/infrastructure/persistence/BackofficeRabbitMqEventBusConfiguration.java`
```java
package tv.codely.backoffice.shared.infrastructure.persistence;

import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import tv.codely.shared.infrastructure.bus.event.mysql.MySqlEventBus;
import tv.codely.shared.infrastructure.bus.event.rabbitmq.RabbitMqEventBus;
import tv.codely.shared.infrastructure.bus.event.rabbitmq.RabbitMqPublisher;

@Configuration
public class BackofficeRabbitMqEventBusConfiguration {
    private final RabbitMqPublisher publisher;
    private final MySqlEventBus     failoverPublisher;

    public BackofficeRabbitMqEventBusConfiguration(
        RabbitMqPublisher publisher,
        @Qualifier("backofficeMysqlEventBus") MySqlEventBus failoverPublisher
    ) {
        this.publisher         = publisher;
        this.failoverPublisher = failoverPublisher;
    }

    @Bean
    public RabbitMqEventBus backofficeRabbitMqEventBus() {
        return new RabbitMqEventBus(publisher, failoverPublisher);
    }
}
```

## File: `src/backoffice/test/tv/codely/backoffice/BackofficeContextInfrastructureTestCase.java`
```java
package tv.codely.backoffice;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.ContextConfiguration;
import tv.codely.apps.backoffice.frontend.BackofficeFrontendApplication;
import tv.codely.backoffice.courses.ElasticsearchEnvironmentArranger;
import tv.codely.shared.infrastructure.InfrastructureTestCase;

import java.io.IOException;

@ContextConfiguration(classes = BackofficeFrontendApplication.class)
@SpringBootTest
public abstract class BackofficeContextInfrastructureTestCase extends InfrastructureTestCase {
    @Autowired
    private ElasticsearchEnvironmentArranger elasticsearchArranger;

    protected void clearElasticsearch() throws IOException {
        elasticsearchArranger.arrange("backoffice", "backoffice_courses");
    }
}
```

## File: `src/backoffice/test/tv/codely/backoffice/auth/AuthModuleUnitTestCase.java`
```java
package tv.codely.backoffice.auth;

import org.junit.jupiter.api.BeforeEach;
import org.mockito.Mockito;
import tv.codely.backoffice.auth.domain.AuthRepository;
import tv.codely.backoffice.auth.domain.AuthUser;
import tv.codely.backoffice.auth.domain.AuthUsername;
import tv.codely.shared.infrastructure.UnitTestCase;

import java.util.Optional;

import static org.mockito.Mockito.mock;

public abstract class AuthModuleUnitTestCase extends UnitTestCase {
    protected AuthRepository repository;

    @BeforeEach
    protected void setUp() {
        super.setUp();

        repository = mock(AuthRepository.class);
    }

    public void shouldSearch(AuthUsername username, AuthUser user) {
        Mockito.when(repository.search(username)).thenReturn(Optional.of(user));
    }

    public void shouldSearch(AuthUsername username) {
        Mockito.when(repository.search(username)).thenReturn(Optional.empty());
    }
}
```

## File: `src/backoffice/test/tv/codely/backoffice/auth/application/authenticate/AuthenticateUserCommandHandlerShould.java`
```java
package tv.codely.backoffice.auth.application.authenticate;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import tv.codely.backoffice.auth.AuthModuleUnitTestCase;
import tv.codely.backoffice.auth.domain.AuthUser;
import tv.codely.backoffice.auth.domain.AuthUserMother;
import tv.codely.backoffice.auth.domain.InvalidAuthCredentials;
import tv.codely.backoffice.auth.domain.InvalidAuthUsername;

import static org.junit.jupiter.api.Assertions.assertThrows;

final class AuthenticateUserCommandHandlerShould extends AuthModuleUnitTestCase {
    private AuthenticateUserCommandHandler handler;

    @BeforeEach
    protected void setUp() {
        super.setUp();

        handler = new AuthenticateUserCommandHandler(new UserAuthenticator(repository));
    }

    @Test
    void authenticate_a_valid_user() {
        AuthenticateUserCommand command  = AuthenticateUserCommandMother.random();
        AuthUser                authUser = AuthUserMother.fromCommand(command);

        shouldSearch(authUser.username(), authUser);

        handler.handle(command);
    }

    @Test
    void throw_an_exception_when_the_user_does_not_exist() {
        assertThrows(InvalidAuthUsername.class, () -> {
            AuthenticateUserCommand command  = AuthenticateUserCommandMother.random();
            AuthUser                authUser = AuthUserMother.fromCommand(command);

            shouldSearch(authUser.username());

            handler.handle(command);
        });
    }

    @Test
    void throw_an_exception_when_the_password_does_not_math() {
        assertThrows(InvalidAuthCredentials.class, () -> {
            AuthenticateUserCommand command  = AuthenticateUserCommandMother.random();
            AuthUser                authUser = AuthUserMother.withUsername(command.username());

            shouldSearch(authUser.username(), authUser);

            handler.handle(command);
        });
    }
}
```

## File: `src/backoffice/test/tv/codely/backoffice/auth/application/authenticate/AuthenticateUserCommandMother.java`
```java
package tv.codely.backoffice.auth.application.authenticate;

import tv.codely.backoffice.auth.domain.AuthPassword;
import tv.codely.backoffice.auth.domain.AuthPasswordMother;
import tv.codely.backoffice.auth.domain.AuthUsername;
import tv.codely.backoffice.auth.domain.AuthUsernameMother;

public final class AuthenticateUserCommandMother {
    public static AuthenticateUserCommand create(AuthUsername username, AuthPassword password) {
        return new AuthenticateUserCommand(username.value(), password.value());
    }

    public static AuthenticateUserCommand random() {
        return create(AuthUsernameMother.random(), AuthPasswordMother.random());
    }
}
```

## File: `src/backoffice/test/tv/codely/backoffice/auth/domain/AuthPasswordMother.java`
```java
package tv.codely.backoffice.auth.domain;

import tv.codely.shared.domain.WordMother;

public final class AuthPasswordMother {
    public static AuthPassword create(String value) {
        return new AuthPassword(value);
    }

    public static AuthPassword random() {
        return create(WordMother.random());
    }
}
```

## File: `src/backoffice/test/tv/codely/backoffice/auth/domain/AuthUserMother.java`
```java
package tv.codely.backoffice.auth.domain;

import tv.codely.backoffice.auth.application.authenticate.AuthenticateUserCommand;

public final class AuthUserMother {
    public static AuthUser create(AuthUsername username, AuthPassword password) {
        return new AuthUser(username, password);
    }

    public static AuthUser random() {
        return create(AuthUsernameMother.random(), AuthPasswordMother.random());
    }

    public static AuthUser fromCommand(AuthenticateUserCommand command) {
        return create(AuthUsernameMother.create(command.username()), AuthPasswordMother.create(command.password()));
    }

    public static AuthUser withUsername(String username) {
        return create(AuthUsernameMother.create(username), AuthPasswordMother.random());
    }
}
```

## File: `src/backoffice/test/tv/codely/backoffice/auth/domain/AuthUsernameMother.java`
```java
package tv.codely.backoffice.auth.domain;

import tv.codely.shared.domain.WordMother;

public final class AuthUsernameMother {
    public static AuthUsername create(String value) {
        return new AuthUsername(value);
    }

    public static AuthUsername random() {
        return create(WordMother.random());
    }
}
```

## File: `src/backoffice/test/tv/codely/backoffice/courses/ElasticsearchEnvironmentArranger.java`
```java
package tv.codely.backoffice.courses;

import org.elasticsearch.client.Request;
import org.springframework.core.io.Resource;
import org.springframework.core.io.support.ResourcePatternResolver;
import tv.codely.shared.domain.Service;
import tv.codely.shared.infrastructure.elasticsearch.ElasticsearchClient;

import java.io.IOException;
import java.util.Objects;
import java.util.Scanner;

@Service
public final class ElasticsearchEnvironmentArranger {
    ResourcePatternResolver resourceResolver;
    ElasticsearchClient     client;

    public ElasticsearchEnvironmentArranger(
        ResourcePatternResolver resourceResolver,
        ElasticsearchClient client
    ) {
        this.resourceResolver = resourceResolver;
        this.client           = client;
    }

    public void arrange(String contextName, String index) throws IOException {
        client.delete(index);

        Resource[] jsonsIndexes = resourceResolver.getResources(
            String.format("classpath:database/%s/%s.json", contextName, index)
        );

        for (Resource jsonIndex : jsonsIndexes) {
            String indexName = Objects.requireNonNull(jsonIndex.getFilename()).replace(".json", "");

            String indexBody = new Scanner(
                jsonIndex.getInputStream(),
                "UTF-8"
            ).useDelimiter("\\A").next();

            Request request = new Request("PUT", indexName);
            request.setJsonEntity(indexBody);

            client.lowLevelClient().performRequest(request);
        }
    }
}
```

## File: `src/backoffice/test/tv/codely/backoffice/courses/domain/BackofficeCourseCriteriaMother.java`
```java
package tv.codely.backoffice.courses.domain;

import tv.codely.shared.domain.criteria.Criteria;
import tv.codely.shared.domain.criteria.Filter;
import tv.codely.shared.domain.criteria.Filters;
import tv.codely.shared.domain.criteria.Order;

import java.util.Arrays;

public final class BackofficeCourseCriteriaMother {
    public static Criteria nameAndDurationContains(String name, String duration) {
        Filter nameFilter     = Filter.create("name", "contains", name);
        Filter durationFilter = Filter.create("duration", "contains", duration);

        return new Criteria(new Filters(Arrays.asList(nameFilter, durationFilter)), Order.asc("name"));
    }
}
```

## File: `src/backoffice/test/tv/codely/backoffice/courses/domain/BackofficeCourseMother.java`
```java
package tv.codely.backoffice.courses.domain;

import tv.codely.shared.domain.UuidMother;
import tv.codely.shared.domain.WordMother;

public final class BackofficeCourseMother {
    public static BackofficeCourse create(String id, String name, String duration) {
        return new BackofficeCourse(id, name, duration);
    }

    public static BackofficeCourse create(String name, String duration) {
        return new BackofficeCourse(UuidMother.random(), name, duration);
    }

    public static BackofficeCourse random() {
        return create(UuidMother.random(), WordMother.random(), WordMother.random());
    }
}
```

## File: `src/backoffice/test/tv/codely/backoffice/courses/infrastructure/persistence/ElasticsearchBackofficeCourseRepositoryShould.java`
```java
package tv.codely.backoffice.courses.infrastructure.persistence;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import tv.codely.backoffice.BackofficeContextInfrastructureTestCase;
import tv.codely.backoffice.courses.domain.BackofficeCourse;
import tv.codely.backoffice.courses.domain.BackofficeCourseCriteriaMother;
import tv.codely.backoffice.courses.domain.BackofficeCourseMother;
import tv.codely.shared.domain.criteria.Criteria;

import java.io.IOException;
import java.util.Arrays;
import java.util.List;

import static org.junit.jupiter.api.Assertions.assertEquals;

final class ElasticsearchBackofficeCourseRepositoryShould extends BackofficeContextInfrastructureTestCase {
    @Autowired
    private ElasticsearchBackofficeCourseRepository repository;

    @BeforeEach
    protected void setUp() throws IOException {
        clearElasticsearch();
    }

    @Test
    void save_a_course() {
        repository.save(BackofficeCourseMother.random());
    }

    @Test
    void search_all_existing_courses() throws Exception {
        BackofficeCourse course        = BackofficeCourseMother.random();
        BackofficeCourse anotherCourse = BackofficeCourseMother.random();

        List<BackofficeCourse> expected = Arrays.asList(course, anotherCourse);

        repository.save(course);
        repository.save(anotherCourse);

        eventually(() -> assertEquals(expected, repository.searchAll()));
    }

    @Test
    void search_courses_using_a_criteria() throws Exception {
        BackofficeCourse matchingCourse        = BackofficeCourseMother.create("DDD en Java", "3 days");
        BackofficeCourse anotherMatchingCourse = BackofficeCourseMother.create("DDD en TypeScript", "2.5 days");
        BackofficeCourse intellijCourse        = BackofficeCourseMother.create("Exprimiendo Intellij", "48 hours");
        BackofficeCourse cobolCourse           = BackofficeCourseMother.create("DDD en Cobol", "5 years");

        Criteria               criteria = BackofficeCourseCriteriaMother.nameAndDurationContains("DDD", "days");
        List<BackofficeCourse> expected = Arrays.asList(matchingCourse, anotherMatchingCourse);

        repository.save(matchingCourse);
        repository.save(anotherMatchingCourse);
        repository.save(intellijCourse);
        repository.save(cobolCourse);

        eventually(() -> assertEquals(expected, repository.matching(criteria)));
    }
}
```

## File: `src/backoffice/test/tv/codely/backoffice/courses/infrastructure/persistence/InMemoryCacheBackofficeCourseRepositoryShould.java`
```java
package tv.codely.backoffice.courses.infrastructure.persistence;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.mockito.Mockito;
import tv.codely.backoffice.BackofficeContextInfrastructureTestCase;
import tv.codely.backoffice.courses.domain.BackofficeCourse;
import tv.codely.backoffice.courses.domain.BackofficeCourseCriteriaMother;
import tv.codely.backoffice.courses.domain.BackofficeCourseMother;
import tv.codely.backoffice.courses.domain.BackofficeCourseRepository;
import tv.codely.shared.domain.criteria.Criteria;

import java.util.Arrays;
import java.util.List;

import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.Matchers.containsInAnyOrder;
import static org.mockito.Mockito.*;

final class InMemoryCacheBackofficeCourseRepositoryShould extends BackofficeContextInfrastructureTestCase {
    private InMemoryCacheBackofficeCourseRepository repository;
    private BackofficeCourseRepository              innerRepository;

    @BeforeEach
    protected void setUp() {
        innerRepository = mock(BackofficeCourseRepository.class);
        repository      = new InMemoryCacheBackofficeCourseRepository(innerRepository);
    }

    @Test
    void save_a_course() {
        BackofficeCourse course = BackofficeCourseMother.random();

        repository.save(course);

        shouldHaveSaved(course);
    }

    @Test
    void search_all_existing_courses() {
        BackofficeCourse       course        = BackofficeCourseMother.random();
        BackofficeCourse       anotherCourse = BackofficeCourseMother.random();
        List<BackofficeCourse> courses       = Arrays.asList(course, anotherCourse);

        shouldSearchAll(courses);

        assertThat(courses, containsInAnyOrder(repository.searchAll().toArray()));
    }

    @Test
    void search_all_existing_courses_without_hitting_the_inner_repository_the_second_time() {
        BackofficeCourse       course        = BackofficeCourseMother.random();
        BackofficeCourse       anotherCourse = BackofficeCourseMother.random();
        List<BackofficeCourse> courses       = Arrays.asList(course, anotherCourse);

        shouldSearchAll(courses);

        assertThat(courses, containsInAnyOrder(repository.searchAll().toArray()));
        assertThat(courses, containsInAnyOrder(repository.searchAll().toArray()));
    }

    @Test
    void search_courses_using_a_criteria() {
        BackofficeCourse       matchingCourse        = BackofficeCourseMother.create("DDD en Java", "3 days");
        BackofficeCourse       anotherMatchingCourse = BackofficeCourseMother.create("DDD en TypeScript", "2.5 days");
        List<BackofficeCourse> matchingCourses       = Arrays.asList(matchingCourse, anotherMatchingCourse);

        Criteria criteria = BackofficeCourseCriteriaMother.nameAndDurationContains("DDD", "days");

        shouldSearchMatching(criteria, matchingCourses);

        assertThat(matchingCourses, containsInAnyOrder(repository.matching(criteria).toArray()));
    }

    @Test
    void search_courses_using_a_criteria_without_hitting_the_inner_repository_the_second_time() {
        BackofficeCourse       matchingCourse        = BackofficeCourseMother.create("DDD en Java", "3 days");
        BackofficeCourse       anotherMatchingCourse = BackofficeCourseMother.create("DDD en TypeScript", "2.5 days");
        List<BackofficeCourse> matchingCourses       = Arrays.asList(matchingCourse, anotherMatchingCourse);

        Criteria criteria = BackofficeCourseCriteriaMother.nameAndDurationContains("DDD", "days");

        shouldSearchMatching(criteria, matchingCourses);

        assertThat(matchingCourses, containsInAnyOrder(repository.matching(criteria).toArray()));
        assertThat(matchingCourses, containsInAnyOrder(repository.matching(criteria).toArray()));
    }

    private void shouldSearchAll(List<BackofficeCourse> courses) {
        Mockito.when(innerRepository.searchAll()).thenReturn(courses);
    }

    private void shouldSearchMatching(Criteria criteria, List<BackofficeCourse> courses) {
        Mockito.when(innerRepository.matching(criteria)).thenReturn(courses);
    }

    private void shouldHaveSaved(BackofficeCourse course) {
        verify(innerRepository, atLeastOnce()).save(course);
    }
}
```

## File: `src/backoffice/test/tv/codely/backoffice/courses/infrastructure/persistence/MySqlBackofficeCourseRepositoryShould.java`
```java
package tv.codely.backoffice.courses.infrastructure.persistence;

import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import tv.codely.backoffice.BackofficeContextInfrastructureTestCase;
import tv.codely.backoffice.courses.domain.BackofficeCourse;
import tv.codely.backoffice.courses.domain.BackofficeCourseCriteriaMother;
import tv.codely.backoffice.courses.domain.BackofficeCourseMother;
import tv.codely.backoffice.courses.domain.BackofficeCourseRepository;
import tv.codely.shared.domain.criteria.Criteria;

import jakarta.transaction.Transactional;
import java.util.Arrays;

import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.Matchers.containsInAnyOrder;

@Transactional
class MySqlBackofficeCourseRepositoryShould extends BackofficeContextInfrastructureTestCase {
    @Autowired
    @Qualifier("mySqlBackofficeCourseRepository")
    private BackofficeCourseRepository repository;

    @Test
    void save_a_course() {
        repository.save(BackofficeCourseMother.random());
    }

    @Test
    void search_all_existing_courses() {
        BackofficeCourse course        = BackofficeCourseMother.random();
        BackofficeCourse anotherCourse = BackofficeCourseMother.random();

        repository.save(course);
        repository.save(anotherCourse);

        assertThat(Arrays.asList(course, anotherCourse), containsInAnyOrder(repository.searchAll().toArray()));
    }

    @Test
    void search_courses_using_a_criteria() {
        BackofficeCourse matchingCourse        = BackofficeCourseMother.create("DDD en Java", "3 days");
        BackofficeCourse anotherMatchingCourse = BackofficeCourseMother.create("DDD en TypeScript", "2.5 days");
        BackofficeCourse intellijCourse        = BackofficeCourseMother.create("Exprimiendo Intellij", "48 hours");
        BackofficeCourse cobolCourse           = BackofficeCourseMother.create("DDD en Cobol", "5 years");

        Criteria criteria = BackofficeCourseCriteriaMother.nameAndDurationContains("DDD", "days");

        repository.save(matchingCourse);
        repository.save(anotherMatchingCourse);
        repository.save(intellijCourse);
        repository.save(cobolCourse);

        assertThat(
            Arrays.asList(matchingCourse, anotherMatchingCourse),
            containsInAnyOrder(repository.matching(criteria).toArray())
        );
    }
}
```

## File: `src/mooc/build.gradle`
```
dependencies {
}
```

## File: `src/mooc/main/resources/database/mooc.sql`
```sql
CREATE TABLE IF NOT EXISTS courses (
	id CHAR(36) NOT NULL,
	name VARCHAR(255) NOT NULL,
	duration VARCHAR(255) NOT NULL,
	PRIMARY KEY (id)
)
	ENGINE = InnoDB
	DEFAULT CHARSET = utf8mb4
	COLLATE = utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS courses_counter (
	id CHAR(36) NOT NULL,
	total INT NOT NULL,
	existing_courses JSON NOT NULL,
	PRIMARY KEY (id)
)
	ENGINE = InnoDB
	DEFAULT CHARSET = utf8mb4
	COLLATE = utf8mb4_unicode_ci;
INSERT IGNORE INTO courses_counter (id, total, existing_courses)
VALUES ('efbaff16-8fcd-4689-9fc9-ec545d641c46', 0, '[]');

CREATE TABLE IF NOT EXISTS steps (
	id CHAR(36) NOT NULL,
	title VARCHAR(155) NOT NULL,
	PRIMARY KEY (id)
)
	ENGINE = InnoDB
	DEFAULT CHARSET = utf8mb4
	COLLATE = utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS steps_challenges (
	id CHAR(36) NOT NULL,
	statement TEXT NOT NULL,
	PRIMARY KEY (id),
	CONSTRAINT fk_steps_challenges__step_id FOREIGN KEY (id) REFERENCES steps(id)
)
	ENGINE = InnoDB
	DEFAULT CHARSET = utf8mb4
	COLLATE = utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS steps_videos (
	id CHAR(36) NOT NULL,
	url VARCHAR(255) NOT NULL,
	text TEXT NOT NULL,
	PRIMARY KEY (id),
	CONSTRAINT fk_steps_video__step_id FOREIGN KEY (id) REFERENCES steps(id)
)
	ENGINE = InnoDB
	DEFAULT CHARSET = utf8mb4
	COLLATE = utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS domain_events (
	id CHAR(36) NOT NULL,
	aggregate_id CHAR(36) NOT NULL,
	name VARCHAR(255) NOT NULL,
	body JSON NOT NULL,
	occurred_on TIMESTAMP NOT NULL,
	PRIMARY KEY (id)
)
	ENGINE = InnoDB
	DEFAULT CHARSET = utf8mb4
	COLLATE = utf8mb4_unicode_ci;
```

## File: `src/mooc/main/tv/codely/mooc/courses/application/CourseResponse.java`
```java
package tv.codely.mooc.courses.application;

import tv.codely.mooc.courses.domain.Course;
import tv.codely.shared.domain.bus.query.Response;

public final class CourseResponse implements Response {
    private final String id;
    private final String name;
    private final String duration;

    public CourseResponse(String id, String name, String duration) {
        this.id       = id;
        this.name     = name;
        this.duration = duration;
    }

    public static CourseResponse fromAggregate(Course course) {
        return new CourseResponse(course.id().value(), course.name().value(), course.duration().value());
    }

    public String id() {
        return id;
    }

    public String name() {
        return name;
    }

    public String duration() {
        return duration;
    }
}
```

## File: `src/mooc/main/tv/codely/mooc/courses/application/CoursesResponse.java`
```java
package tv.codely.mooc.courses.application;

import tv.codely.shared.domain.bus.query.Response;

import java.util.List;

public final class CoursesResponse implements Response {
    private final List<CourseResponse> courses;

    public CoursesResponse(List<CourseResponse> courses) {
        this.courses = courses;
    }

    public List<CourseResponse> courses() {
        return courses;
    }
}
```

## File: `src/mooc/main/tv/codely/mooc/courses/application/create/CourseCreator.java`
```java
package tv.codely.mooc.courses.application.create;

import tv.codely.mooc.courses.domain.*;
import tv.codely.shared.domain.Service;
import tv.codely.shared.domain.bus.event.EventBus;

@Service
public final class CourseCreator {
    private final CourseRepository repository;
    private final EventBus         eventBus;

    public CourseCreator(CourseRepository repository, EventBus eventBus) {
        this.repository = repository;
        this.eventBus   = eventBus;
    }

    public void create(CourseId id, CourseName name, CourseDuration duration) {
        Course course = Course.create(id, name, duration);

        repository.save(course);
        eventBus.publish(course.pullDomainEvents());
    }
}
```

## File: `src/mooc/main/tv/codely/mooc/courses/application/create/CreateCourseCommand.java`
```java
package tv.codely.mooc.courses.application.create;

import tv.codely.shared.domain.bus.command.Command;

public final class CreateCourseCommand implements Command {
    private final String id;
    private final String name;
    private final String duration;

    public CreateCourseCommand(String id, String name, String duration) {
        this.id       = id;
        this.name     = name;
        this.duration = duration;
    }

    public String id() {
        return id;
    }

    public String name() {
        return name;
    }

    public String duration() {
        return duration;
    }
}
```

## File: `src/mooc/main/tv/codely/mooc/courses/application/create/CreateCourseCommandHandler.java`
```java
package tv.codely.mooc.courses.application.create;

import tv.codely.mooc.courses.domain.CourseDuration;
import tv.codely.mooc.courses.domain.CourseId;
import tv.codely.mooc.courses.domain.CourseName;
import tv.codely.shared.domain.Service;
import tv.codely.shared.domain.bus.command.CommandHandler;

@Service
public final class CreateCourseCommandHandler implements CommandHandler<CreateCourseCommand> {
    private final CourseCreator creator;

    public CreateCourseCommandHandler(CourseCreator creator) {
        this.creator = creator;
    }

    @Override
    public void handle(CreateCourseCommand command) {
        CourseId       id       = new CourseId(command.id());
        CourseName     name     = new CourseName(command.name());
        CourseDuration duration = new CourseDuration(command.duration());

        creator.create(id, name, duration);
    }
}
```

## File: `src/mooc/main/tv/codely/mooc/courses/application/find/CourseFinder.java`
```java
package tv.codely.mooc.courses.application.find;

import tv.codely.mooc.courses.application.CourseResponse;
import tv.codely.mooc.courses.domain.CourseId;
import tv.codely.mooc.courses.domain.CourseNotExist;
import tv.codely.mooc.courses.domain.CourseRepository;
import tv.codely.shared.domain.Service;

@Service
public final class CourseFinder {
    private final CourseRepository repository;

    public CourseFinder(CourseRepository repository) {
        this.repository = repository;
    }

    public CourseResponse find(CourseId id) throws CourseNotExist {
        return repository.search(id)
                         .map(CourseResponse::fromAggregate)
                         .orElseThrow(() -> new CourseNotExist(id));
    }
}
```

## File: `src/mooc/main/tv/codely/mooc/courses/application/find/FindCourseQuery.java`
```java
package tv.codely.mooc.courses.application.find;

import tv.codely.shared.domain.bus.query.Query;

public final class FindCourseQuery implements Query {
    private final String id;

    public FindCourseQuery(String id) {
        this.id = id;
    }

    public String id() {
        return id;
    }
}
```

## File: `src/mooc/main/tv/codely/mooc/courses/application/find/FindCourseQueryHandler.java`
```java
package tv.codely.mooc.courses.application.find;

import tv.codely.mooc.courses.application.CourseResponse;
import tv.codely.mooc.courses.domain.CourseId;
import tv.codely.mooc.courses.domain.CourseNotExist;
import tv.codely.shared.domain.Service;
import tv.codely.shared.domain.bus.query.QueryHandler;

@Service
public final class FindCourseQueryHandler implements QueryHandler<FindCourseQuery, CourseResponse> {
    private final CourseFinder finder;

    public FindCourseQueryHandler(CourseFinder finder) {
        this.finder = finder;
    }

    @Override
    public CourseResponse handle(FindCourseQuery query) throws CourseNotExist {
        return finder.find(new CourseId(query.id()));
    }
}
```

## File: `src/mooc/main/tv/codely/mooc/courses/application/search_last/LastCoursesSearcher.java`
```java
package tv.codely.mooc.courses.application.search_last;

import tv.codely.mooc.courses.application.CourseResponse;
import tv.codely.mooc.courses.application.CoursesResponse;
import tv.codely.mooc.courses.domain.CourseRepository;
import tv.codely.shared.domain.Service;
import tv.codely.shared.domain.criteria.Criteria;
import tv.codely.shared.domain.criteria.Filters;
import tv.codely.shared.domain.criteria.Order;

import java.util.Optional;
import java.util.stream.Collectors;

@Service
public final class LastCoursesSearcher {
    private final CourseRepository repository;

    public LastCoursesSearcher(CourseRepository repository) {
        this.repository = repository;
    }

    public CoursesResponse search(int courses) {
        Criteria criteria = new Criteria(
            Filters.none(),
            Order.none(),
            Optional.of(courses),
            Optional.empty()
        );

        return new CoursesResponse(
            repository.matching(criteria).stream().map(CourseResponse::fromAggregate).collect(Collectors.toList())
        );
    }
}
```

## File: `src/mooc/main/tv/codely/mooc/courses/application/search_last/SearchLastCoursesQuery.java`
```java
package tv.codely.mooc.courses.application.search_last;

import tv.codely.shared.domain.bus.query.Query;

import java.util.Objects;

public final class SearchLastCoursesQuery implements Query {
    private final Integer total;

    public SearchLastCoursesQuery(Integer total) {
        this.total = total;
    }

    public Integer total() {
        return total;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) {
            return true;
        }
        if (o == null || getClass() != o.getClass()) {
            return false;
        }
        SearchLastCoursesQuery that = (SearchLastCoursesQuery) o;
        return total.equals(that.total);
    }

    @Override
    public int hashCode() {
        return Objects.hash(total);
    }
}
```

## File: `src/mooc/main/tv/codely/mooc/courses/application/search_last/SearchLastCoursesQueryHandler.java`
```java
package tv.codely.mooc.courses.application.search_last;

import tv.codely.mooc.courses.application.CoursesResponse;
import tv.codely.shared.domain.Service;
import tv.codely.shared.domain.bus.query.QueryHandler;

@Service
public final class SearchLastCoursesQueryHandler implements QueryHandler<SearchLastCoursesQuery, CoursesResponse> {
    private final LastCoursesSearcher searcher;

    public SearchLastCoursesQueryHandler(LastCoursesSearcher searcher) {
        this.searcher = searcher;
    }

    @Override
    public CoursesResponse handle(SearchLastCoursesQuery query) {
        return searcher.search(query.total());
    }
}
```

## File: `src/mooc/main/tv/codely/mooc/courses/domain/Course.java`
```java
package tv.codely.mooc.courses.domain;

import tv.codely.shared.domain.AggregateRoot;
import tv.codely.shared.domain.course.CourseCreatedDomainEvent;

import java.util.Objects;

public final class Course extends AggregateRoot {
    private final CourseId       id;
    private final CourseName     name;
    private final CourseDuration duration;

    public Course(CourseId id, CourseName name, CourseDuration duration) {
        this.id       = id;
        this.name     = name;
        this.duration = duration;
    }

    private Course() {
        id       = null;
        name     = null;
        duration = null;
    }

    public static Course create(CourseId id, CourseName name, CourseDuration duration) {
        Course course = new Course(id, name, duration);

        course.record(new CourseCreatedDomainEvent(id.value(), name.value(), duration.value()));

        return course;
    }

    public CourseId id() {
        return id;
    }

    public CourseName name() {
        return name;
    }

    public CourseDuration duration() {
        return duration;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) {
            return true;
        }
        if (o == null || getClass() != o.getClass()) {
            return false;
        }
        Course course = (Course) o;
        return id.equals(course.id) &&
               name.equals(course.name) &&
               duration.equals(course.duration);
    }

    @Override
    public int hashCode() {
        return Objects.hash(id, name, duration);
    }
}
```

## File: `src/mooc/main/tv/codely/mooc/courses/domain/CourseDuration.java`
```java
package tv.codely.mooc.courses.domain;

import tv.codely.shared.domain.StringValueObject;

public final class CourseDuration extends StringValueObject {
    public CourseDuration(String value) {
        super(value);
    }

    private CourseDuration() {
        super("");
    }
}
```

## File: `src/mooc/main/tv/codely/mooc/courses/domain/CourseId.java`
```java
package tv.codely.mooc.courses.domain;

import tv.codely.shared.domain.Identifier;

public final class CourseId extends Identifier {
    public CourseId(String value) {
        super(value);
    }

    public CourseId() {
    }
}
```

## File: `src/mooc/main/tv/codely/mooc/courses/domain/CourseName.java`
```java
package tv.codely.mooc.courses.domain;

import tv.codely.shared.domain.StringValueObject;

public final class CourseName extends StringValueObject {
    public CourseName(String value) {
        super(value);
    }

    public CourseName() {
        super("");
    }
}
```

## File: `src/mooc/main/tv/codely/mooc/courses/domain/CourseNotExist.java`
```java
package tv.codely.mooc.courses.domain;

import tv.codely.shared.domain.DomainError;

public final class CourseNotExist extends DomainError {
    public CourseNotExist(CourseId id) {
        super("course_not_exist", String.format("The course <%s> doesn't exist", id.value()));
    }
}
```

## File: `src/mooc/main/tv/codely/mooc/courses/domain/CourseRepository.java`
```java
package tv.codely.mooc.courses.domain;

import tv.codely.shared.domain.criteria.Criteria;

import java.util.List;
import java.util.Optional;

public interface CourseRepository {
    void save(Course course);

    Optional<Course> search(CourseId id);

    List<Course> matching(Criteria criteria);
}
```

## File: `src/mooc/main/tv/codely/mooc/courses/infrastructure/persistence/InMemoryCourseRepository.java`
```java
package tv.codely.mooc.courses.infrastructure.persistence;

import tv.codely.mooc.courses.domain.Course;
import tv.codely.mooc.courses.domain.CourseId;
import tv.codely.mooc.courses.domain.CourseRepository;
import tv.codely.shared.domain.criteria.Criteria;

import java.util.HashMap;
import java.util.List;
import java.util.Optional;

public final class InMemoryCourseRepository implements CourseRepository {
    private HashMap<String, Course> courses = new HashMap<>();

    @Override
    public void save(Course course) {
        courses.put(course.id().value(), course);
    }

    public Optional<Course> search(CourseId id) {
        return Optional.ofNullable(courses.get(id.value()));
    }

    @Override
    public List<Course> matching(Criteria criteria) {
        return null;
    }
}
```

## File: `src/mooc/main/tv/codely/mooc/courses/infrastructure/persistence/MySqlCourseRepository.java`
```java
package tv.codely.mooc.courses.infrastructure.persistence;

import org.hibernate.SessionFactory;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.transaction.annotation.Transactional;
import tv.codely.mooc.courses.domain.Course;
import tv.codely.mooc.courses.domain.CourseId;
import tv.codely.mooc.courses.domain.CourseRepository;
import tv.codely.shared.domain.Service;
import tv.codely.shared.domain.criteria.Criteria;
import tv.codely.shared.infrastructure.hibernate.HibernateRepository;

import java.util.List;
import java.util.Optional;

@Service
@Transactional("mooc-transaction_manager")
public class MySqlCourseRepository extends HibernateRepository<Course> implements CourseRepository {
    public MySqlCourseRepository(@Qualifier("mooc-session_factory") SessionFactory sessionFactory) {
        super(sessionFactory, Course.class);
    }

    @Override
    public void save(Course course) {
        persist(course);
    }

    @Override
    public Optional<Course> search(CourseId id) {
        return byId(id);
    }

    @Override
    public List<Course> matching(Criteria criteria) {
        return byCriteria(criteria);
    }
}
```

## File: `src/mooc/main/tv/codely/mooc/courses/infrastructure/persistence/hibernate/Course.hbm.xml`
```xml
<?xml version = "1.0" encoding = "utf-8"?>
<!DOCTYPE hibernate-mapping PUBLIC
        "-//Hibernate/Hibernate Mapping DTD//EN"
        "http://www.hibernate.org/dtd/hibernate-mapping-3.0.dtd">

<hibernate-mapping>
    <class name="tv.codely.mooc.courses.domain.Course" table="courses">
        <composite-id name="id" class="tv.codely.mooc.courses.domain.CourseId" access="field">
            <key-property column="id" name="value" length="36" access="field" />
        </composite-id>

        <component name="name" class="tv.codely.mooc.courses.domain.CourseName" access="field">
            <property name="value" column="name" type="string" access="field" />
        </component>

        <component name="duration" class="tv.codely.mooc.courses.domain.CourseDuration" access="field">
            <property name="value" column="duration" type="string" access="field" />
        </component>
    </class>
</hibernate-mapping>
```

## File: `src/mooc/main/tv/codely/mooc/courses_counter/application/find/CoursesCounterFinder.java`
```java
package tv.codely.mooc.courses_counter.application.find;

import tv.codely.mooc.courses_counter.domain.CoursesCounter;
import tv.codely.mooc.courses_counter.domain.CoursesCounterNotInitialized;
import tv.codely.mooc.courses_counter.domain.CoursesCounterRepository;
import tv.codely.shared.domain.Service;

@Service
public final class CoursesCounterFinder {
    private CoursesCounterRepository repository;

    public CoursesCounterFinder(CoursesCounterRepository repository) {
        this.repository = repository;
    }

    public CoursesCounterResponse find() {
        CoursesCounter coursesCounter = repository.search().orElseGet(() -> {
            throw new CoursesCounterNotInitialized();
        });

        return new CoursesCounterResponse(coursesCounter.total().value());
    }
}
```

## File: `src/mooc/main/tv/codely/mooc/courses_counter/application/find/CoursesCounterResponse.java`
```java
package tv.codely.mooc.courses_counter.application.find;

import tv.codely.shared.domain.bus.query.Response;

import java.util.Objects;

public final class CoursesCounterResponse implements Response {
    private Integer total;

    public CoursesCounterResponse(Integer total) {
        this.total = total;
    }

    public Integer total() {
        return total;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) {
            return true;
        }
        if (o == null || getClass() != o.getClass()) {
            return false;
        }
        CoursesCounterResponse that = (CoursesCounterResponse) o;
        return total.equals(that.total);
    }

    @Override
    public int hashCode() {
        return Objects.hash(total);
    }
}
```

## File: `src/mooc/main/tv/codely/mooc/courses_counter/application/find/FindCoursesCounterQuery.java`
```java
package tv.codely.mooc.courses_counter.application.find;

import tv.codely.shared.domain.bus.query.Query;

public final class FindCoursesCounterQuery implements Query {
}
```

## File: `src/mooc/main/tv/codely/mooc/courses_counter/application/find/FindCoursesCounterQueryHandler.java`
```java
package tv.codely.mooc.courses_counter.application.find;

import tv.codely.shared.domain.Service;
import tv.codely.shared.domain.bus.query.QueryHandler;

@Service
public final class FindCoursesCounterQueryHandler implements QueryHandler<FindCoursesCounterQuery, CoursesCounterResponse> {
    private final CoursesCounterFinder finder;

    public FindCoursesCounterQueryHandler(CoursesCounterFinder finder) {
        this.finder = finder;
    }

    @Override
    public CoursesCounterResponse handle(FindCoursesCounterQuery query) {
        return finder.find();
    }
}
```

## File: `src/mooc/main/tv/codely/mooc/courses_counter/application/increment/CoursesCounterIncrementer.java`
```java
package tv.codely.mooc.courses_counter.application.increment;

import tv.codely.mooc.courses.domain.CourseId;
import tv.codely.mooc.courses_counter.domain.CoursesCounter;
import tv.codely.mooc.courses_counter.domain.CoursesCounterRepository;
import tv.codely.shared.domain.Service;
import tv.codely.shared.domain.UuidGenerator;

@Service
public final class CoursesCounterIncrementer {
    private CoursesCounterRepository repository;
    private UuidGenerator            uuidGenerator;

    public CoursesCounterIncrementer(CoursesCounterRepository repository, UuidGenerator uuidGenerator) {
        this.repository    = repository;
        this.uuidGenerator = uuidGenerator;
    }

    public void increment(CourseId id) {
        CoursesCounter counter = repository.search()
                                           .orElseGet(() -> CoursesCounter.initialize(uuidGenerator.generate()));

        if (!counter.hasIncremented(id)) {
            counter.increment(id);

            repository.save(counter);
        }
    }
}
```

## File: `src/mooc/main/tv/codely/mooc/courses_counter/application/increment/IncrementCoursesCounterOnCourseCreated.java`
```java
package tv.codely.mooc.courses_counter.application.increment;

import org.springframework.context.event.EventListener;
import tv.codely.mooc.courses.domain.CourseId;
import tv.codely.shared.domain.Service;
import tv.codely.shared.domain.bus.event.DomainEventSubscriber;
import tv.codely.shared.domain.course.CourseCreatedDomainEvent;

@Service
@DomainEventSubscriber({CourseCreatedDomainEvent.class})
public final class IncrementCoursesCounterOnCourseCreated {
    private final CoursesCounterIncrementer incrementer;

    public IncrementCoursesCounterOnCourseCreated(CoursesCounterIncrementer incrementer) {
        this.incrementer = incrementer;
    }

    @EventListener
    public void on(CourseCreatedDomainEvent event) {
        CourseId courseId = new CourseId(event.aggregateId());

        incrementer.increment(courseId);
    }
}
```

## File: `src/mooc/main/tv/codely/mooc/courses_counter/domain/CoursesCounter.java`
```java
package tv.codely.mooc.courses_counter.domain;

import tv.codely.mooc.courses.domain.CourseId;

import java.util.ArrayList;
import java.util.List;
import java.util.Objects;

public final class CoursesCounter {
    private CoursesCounterId    id;
    private CoursesCounterTotal total;
    private List<CourseId>      existingCourses;

    public CoursesCounter(CoursesCounterId id, CoursesCounterTotal total, List<CourseId> existingCourses) {
        this.id              = id;
        this.total           = total;
        this.existingCourses = existingCourses;
    }

    private CoursesCounter() {
        this.id              = null;
        this.total           = null;
        this.existingCourses = null;
    }

    public static CoursesCounter initialize(String id) {
        return new CoursesCounter(new CoursesCounterId(id), CoursesCounterTotal.initialize(), new ArrayList<>());
    }

    public CoursesCounterId id() {
        return id;
    }

    public CoursesCounterTotal total() {
        return total;
    }

    public List<CourseId> existingCourses() {
        return existingCourses;
    }

    public boolean hasIncremented(CourseId id) {
        return existingCourses.contains(id);
    }

    public void increment(CourseId id) {
        total = total.increment();
        existingCourses.add(id);
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) {
            return true;
        }
        if (o == null || getClass() != o.getClass()) {
            return false;
        }
        CoursesCounter that = (CoursesCounter) o;
        return id.equals(that.id) &&
               total.equals(that.total) &&
               existingCourses.equals(that.existingCourses);
    }

    @Override
    public int hashCode() {
        return Objects.hash(id, total, existingCourses);
    }
}
```

## File: `src/mooc/main/tv/codely/mooc/courses_counter/domain/CoursesCounterId.java`
```java
package tv.codely.mooc.courses_counter.domain;

import tv.codely.shared.domain.Identifier;

public final class CoursesCounterId extends Identifier {
    public CoursesCounterId(String value) {
        super(value);
    }

    private CoursesCounterId() {
    }
}
```

## File: `src/mooc/main/tv/codely/mooc/courses_counter/domain/CoursesCounterNotInitialized.java`
```java
package tv.codely.mooc.courses_counter.domain;

public final class CoursesCounterNotInitialized extends RuntimeException {
}
```

## File: `src/mooc/main/tv/codely/mooc/courses_counter/domain/CoursesCounterRepository.java`
```java
package tv.codely.mooc.courses_counter.domain;

import java.util.Optional;

public interface CoursesCounterRepository {
    void save(CoursesCounter counter);

    Optional<CoursesCounter> search();
}
```

## File: `src/mooc/main/tv/codely/mooc/courses_counter/domain/CoursesCounterTotal.java`
```java
package tv.codely.mooc.courses_counter.domain;

import tv.codely.shared.domain.IntValueObject;

public final class CoursesCounterTotal extends IntValueObject {
    public CoursesCounterTotal(Integer value) {
        super(value);
    }

    public CoursesCounterTotal() {
        super(null);
    }

    public static CoursesCounterTotal initialize() {
        return new CoursesCounterTotal(0);
    }

    public CoursesCounterTotal increment() {
        return new CoursesCounterTotal(value() + 1);
    }
}
```

## File: `src/mooc/main/tv/codely/mooc/courses_counter/infrastructure/persistence/MySqlCoursesCounterRepository.java`
```java
package tv.codely.mooc.courses_counter.infrastructure.persistence;

import org.hibernate.SessionFactory;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.transaction.annotation.Transactional;
import tv.codely.mooc.courses_counter.domain.CoursesCounter;
import tv.codely.mooc.courses_counter.domain.CoursesCounterRepository;
import tv.codely.shared.domain.Service;
import tv.codely.shared.infrastructure.hibernate.HibernateRepository;

import java.util.List;
import java.util.Optional;

@Service
@Transactional("mooc-transaction_manager")
public class MySqlCoursesCounterRepository extends HibernateRepository<CoursesCounter> implements CoursesCounterRepository {
    public MySqlCoursesCounterRepository(@Qualifier("mooc-session_factory") SessionFactory sessionFactory) {
        super(sessionFactory, CoursesCounter.class);
    }

    @Override
    public void save(CoursesCounter counter) {
        persist(counter);
    }

    @Override
    public Optional<CoursesCounter> search() {
        List<CoursesCounter> coursesCounter = all();

        return 0 == coursesCounter.size() ? Optional.empty() : Optional.ofNullable(coursesCounter.get(0));
    }
}
```

## File: `src/mooc/main/tv/codely/mooc/courses_counter/infrastructure/persistence/hibernate/CoursesCounter.hbm.xml`
```xml
<?xml version = "1.0" encoding = "utf-8"?>
<!DOCTYPE hibernate-mapping PUBLIC
        "-//Hibernate/Hibernate Mapping DTD//EN"
        "http://www.hibernate.org/dtd/hibernate-mapping-3.0.dtd">

<hibernate-mapping>

    <class name="tv.codely.mooc.courses_counter.domain.CoursesCounter" table="courses_counter">

        <composite-id name="id" class="tv.codely.mooc.courses_counter.domain.CoursesCounterId" access="field">
            <key-property column="id" name="value" length="36" access="field" />
        </composite-id>

        <component name="total" class="tv.codely.mooc.courses_counter.domain.CoursesCounterTotal" access="field">
            <property name="value" column="total" type="integer" access="field" />
        </component>

        <property name="existingCourses" column="existing_courses" access="field">
            <type name="tv.codely.shared.infrastructure.hibernate.JsonListType">
                <param name="list_of">tv.codely.mooc.courses.domain.CourseId</param>
            </type>
        </property>
    </class>
</hibernate-mapping>
```

## File: `src/mooc/main/tv/codely/mooc/notifications/application/send_new_courses_newsletter/NewCoursesNewsletterSender.java`
```java
package tv.codely.mooc.notifications.application.send_new_courses_newsletter;

import tv.codely.mooc.courses.application.CoursesResponse;
import tv.codely.mooc.courses.application.search_last.SearchLastCoursesQuery;
import tv.codely.mooc.notifications.domain.EmailSender;
import tv.codely.mooc.notifications.domain.NewCoursesNewsletter;
import tv.codely.mooc.students.application.StudentResponse;
import tv.codely.mooc.students.application.StudentsResponse;
import tv.codely.mooc.students.application.search_all.SearchAllStudentsQuery;
import tv.codely.shared.domain.Service;
import tv.codely.shared.domain.UuidGenerator;
import tv.codely.shared.domain.bus.event.EventBus;
import tv.codely.shared.domain.bus.query.QueryBus;

@Service
public final class NewCoursesNewsletterSender {
    private final static Integer       TOTAL_COURSES = 3;
    private final        QueryBus      queryBus;
    private final        EmailSender   sender;
    private final        UuidGenerator uuidGenerator;
    private final        EventBus      eventBus;

    public NewCoursesNewsletterSender(
        QueryBus queryBus,
        UuidGenerator uuidGenerator,
        EmailSender sender,
        EventBus eventBus
    ) {
        this.queryBus      = queryBus;
        this.uuidGenerator = uuidGenerator;
        this.sender        = sender;
        this.eventBus      = eventBus;
    }

    public void send() {
        CoursesResponse courses = queryBus.ask(new SearchLastCoursesQuery(TOTAL_COURSES));

        if (courses.courses().size() > 0) {
            StudentsResponse students = queryBus.ask(new SearchAllStudentsQuery());

            students.students().forEach(student -> send(student, courses));
        }
    }

    public void send(StudentResponse student, CoursesResponse courses) {
        NewCoursesNewsletter newsletter = NewCoursesNewsletter.send(uuidGenerator.generate(), student, courses);

        sender.send(newsletter);

        eventBus.publish(newsletter.pullDomainEvents());
    }
}
```

## File: `src/mooc/main/tv/codely/mooc/notifications/application/send_new_courses_newsletter/SendNewCoursesNewsletterCommand.java`
```java
package tv.codely.mooc.notifications.application.send_new_courses_newsletter;

import tv.codely.shared.domain.bus.command.Command;

public final class SendNewCoursesNewsletterCommand implements Command {
    private final String id;

    public SendNewCoursesNewsletterCommand(String id) {
        this.id = id;
    }

    public String id() {
        return id;
    }
}
```

## File: `src/mooc/main/tv/codely/mooc/notifications/application/send_new_courses_newsletter/SendNewCoursesNewsletterCommandHandler.java`
```java
package tv.codely.mooc.notifications.application.send_new_courses_newsletter;

import tv.codely.shared.domain.Service;
import tv.codely.shared.domain.bus.command.CommandHandler;

@Service
public final class SendNewCoursesNewsletterCommandHandler implements CommandHandler<SendNewCoursesNewsletterCommand> {
    private final NewCoursesNewsletterSender sender;

    public SendNewCoursesNewsletterCommandHandler(NewCoursesNewsletterSender sender) {
        this.sender = sender;
    }

    @Override
    public void handle(SendNewCoursesNewsletterCommand command) {
        sender.send();
    }
}
```

## File: `src/mooc/main/tv/codely/mooc/notifications/domain/Email.java`
```java
package tv.codely.mooc.notifications.domain;

import tv.codely.shared.domain.AggregateRoot;

import java.util.Objects;

public abstract class Email extends AggregateRoot {
    private final EmailId id;
    private final String  from;
    private final String  to;
    private final String  subject;
    private final String  body;

    public Email(EmailId id, String from, String to, String subject, String body) {
        this.id      = id;
        this.from    = from;
        this.to      = to;
        this.subject = subject;
        this.body    = body;
    }

    public EmailId id() {
        return id;
    }

    public String from() {
        return from;
    }

    public String to() {
        return to;
    }

    public String subject() {
        return subject;
    }

    public String body() {
        return body;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) {
            return true;
        }
        if (o == null || getClass() != o.getClass()) {
            return false;
        }
        Email email = (Email) o;
        return id.equals(email.id) &&
               from.equals(email.from) &&
               to.equals(email.to) &&
               subject.equals(email.subject) &&
               body.equals(email.body);
    }

    @Override
    public int hashCode() {
        return Objects.hash(id, from, to, subject, body);
    }
}
```

## File: `src/mooc/main/tv/codely/mooc/notifications/domain/EmailId.java`
```java
package tv.codely.mooc.notifications.domain;

import tv.codely.shared.domain.Identifier;

public final class EmailId extends Identifier {
    public EmailId(String value) {
        super(value);
    }
}
```

## File: `src/mooc/main/tv/codely/mooc/notifications/domain/EmailSender.java`
```java
package tv.codely.mooc.notifications.domain;

public interface EmailSender {
    void send(Email email);
}
```

## File: `src/mooc/main/tv/codely/mooc/notifications/domain/NewCoursesNewsletter.java`
```java
package tv.codely.mooc.notifications.domain;

import tv.codely.mooc.courses.application.CoursesResponse;
import tv.codely.mooc.students.application.StudentResponse;

import java.util.Objects;

public final class NewCoursesNewsletter extends Email {
    private final StudentResponse student;
    private final CoursesResponse courses;

    public NewCoursesNewsletter(EmailId id, StudentResponse student, CoursesResponse courses) {
        super(id, "news@codely.tv", student.email(), "Último cursos en CodelyTV", formatBody(student, courses));

        this.student = student;
        this.courses = courses;
    }

    private static String formatBody(StudentResponse student, CoursesResponse courses) {
        return String.format(
            "Hoy es tu día de suerte... %s vas a ver %s nuevos cursos",
            student.name(),
            courses.courses().size()
        );
    }

    public static NewCoursesNewsletter send(String id, StudentResponse student, CoursesResponse courses) {
        NewCoursesNewsletter newsletter = new NewCoursesNewsletter(new EmailId(id), student, courses);

        newsletter.record(new NewCoursesNewsletterEmailSent(id, student.id()));

        return newsletter;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) {
            return true;
        }
        if (o == null || getClass() != o.getClass()) {
            return false;
        }
        if (!super.equals(o)) {
            return false;
        }
        NewCoursesNewsletter that = (NewCoursesNewsletter) o;
        return student.equals(that.student) &&
               courses.equals(that.courses);
    }

    @Override
    public int hashCode() {
        return Objects.hash(super.hashCode(), student, courses);
    }
}
```

## File: `src/mooc/main/tv/codely/mooc/notifications/domain/NewCoursesNewsletterEmailSent.java`
```java
package tv.codely.mooc.notifications.domain;

import tv.codely.shared.domain.bus.event.DomainEvent;

import java.io.Serializable;
import java.util.HashMap;
import java.util.Objects;

public final class NewCoursesNewsletterEmailSent extends DomainEvent {
    private final String studentId;

    public NewCoursesNewsletterEmailSent() {
        super(null);

        this.studentId = null;
    }

    public NewCoursesNewsletterEmailSent(String aggregateId, String studentId) {
        super(aggregateId);

        this.studentId = studentId;
    }

    public NewCoursesNewsletterEmailSent(
        String aggregateId,
        String eventId,
        String occurredOn,
        String studentId
    ) {
        super(aggregateId, eventId, occurredOn);

        this.studentId = studentId;
    }

    @Override
    public String eventName() {
        return "new_courses_newsletter_email.sent";
    }

    @Override
    public HashMap<String, Serializable> toPrimitives() {
        return new HashMap<String, Serializable>() {{
            put("student_id", studentId);
        }};
    }

    @Override
    public NewCoursesNewsletterEmailSent fromPrimitives(
        String aggregateId,
        HashMap<String, Serializable> body,
        String eventId,
        String occurredOn
    ) {
        return new NewCoursesNewsletterEmailSent(
            aggregateId,
            eventId,
            occurredOn,
            (String) body.get("student_id")
        );
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) {
            return true;
        }
        if (o == null || getClass() != o.getClass()) {
            return false;
        }
        NewCoursesNewsletterEmailSent that = (NewCoursesNewsletterEmailSent) o;
        return studentId.equals(that.studentId);
    }

    @Override
    public int hashCode() {
        return Objects.hash(studentId);
    }
}
```

## File: `src/mooc/main/tv/codely/mooc/notifications/infrastructure/FakeEmailSender.java`
```java
package tv.codely.mooc.notifications.infrastructure;

import tv.codely.mooc.notifications.domain.Email;
import tv.codely.mooc.notifications.domain.EmailSender;
import tv.codely.shared.domain.Service;

@Service
public final class FakeEmailSender implements EmailSender {
    @Override
    public void send(Email email) {
        // In the future...
    }
}
```

## File: `src/mooc/main/tv/codely/mooc/shared/infrastructure/persistence/MoocHibernateConfiguration.java`
```java
package tv.codely.mooc.shared.infrastructure.persistence;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.orm.hibernate5.LocalSessionFactoryBean;
import org.springframework.transaction.PlatformTransactionManager;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import tv.codely.shared.infrastructure.config.Parameter;
import tv.codely.shared.infrastructure.config.ParameterNotExist;
import tv.codely.shared.infrastructure.hibernate.HibernateConfigurationFactory;

import javax.sql.DataSource;
import java.io.IOException;

@Configuration
@EnableTransactionManagement
public class MoocHibernateConfiguration {
    private final HibernateConfigurationFactory factory;
    private final Parameter                     config;
    private final String                        CONTEXT_NAME = "mooc";

    public MoocHibernateConfiguration(HibernateConfigurationFactory factory, Parameter config) {
        this.factory = factory;
        this.config  = config;
    }

    @Bean("mooc-transaction_manager")
    public PlatformTransactionManager hibernateTransactionManager() throws IOException, ParameterNotExist {
        return factory.hibernateTransactionManager(sessionFactory());
    }

    @Bean("mooc-session_factory")
    public LocalSessionFactoryBean sessionFactory() throws IOException, ParameterNotExist {
        return factory.sessionFactory(CONTEXT_NAME, dataSource());
    }

    @Bean("mooc-data_source")
    public DataSource dataSource() throws IOException, ParameterNotExist {
        return factory.dataSource(
            config.get("MOOC_DATABASE_HOST"),
            config.getInt("MOOC_DATABASE_PORT"),
            config.get("MOOC_DATABASE_NAME"),
            config.get("MOOC_DATABASE_USER"),
            config.get("MOOC_DATABASE_PASSWORD")
        );
    }
}
```

## File: `src/mooc/main/tv/codely/mooc/shared/infrastructure/persistence/MoocMySqlEventBusConfiguration.java`
```java
package tv.codely.mooc.shared.infrastructure.persistence;

import org.hibernate.SessionFactory;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import tv.codely.shared.infrastructure.bus.event.DomainEventsInformation;
import tv.codely.shared.infrastructure.bus.event.mysql.MySqlDomainEventsConsumer;
import tv.codely.shared.infrastructure.bus.event.mysql.MySqlEventBus;
import tv.codely.shared.infrastructure.bus.event.spring.SpringApplicationEventBus;

@Configuration
public class MoocMySqlEventBusConfiguration {
    private final SessionFactory            sessionFactory;
    private final DomainEventsInformation   domainEventsInformation;
    private final SpringApplicationEventBus bus;

    public MoocMySqlEventBusConfiguration(
        @Qualifier("mooc-session_factory") SessionFactory sessionFactory,
        DomainEventsInformation domainEventsInformation,
        SpringApplicationEventBus bus
    ) {
        this.sessionFactory          = sessionFactory;
        this.domainEventsInformation = domainEventsInformation;
        this.bus                     = bus;
    }

    @Bean
    public MySqlEventBus moocMysqlEventBus() {
        return new MySqlEventBus(sessionFactory);
    }

    @Bean
    public MySqlDomainEventsConsumer moocMySqlDomainEventsConsumer() {
        return new MySqlDomainEventsConsumer(sessionFactory, domainEventsInformation, bus);
    }
}
```

## File: `src/mooc/main/tv/codely/mooc/shared/infrastructure/persistence/MoocRabbitMqEventBusConfiguration.java`
```java
package tv.codely.mooc.shared.infrastructure.persistence;

import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import tv.codely.shared.infrastructure.bus.event.mysql.MySqlEventBus;
import tv.codely.shared.infrastructure.bus.event.rabbitmq.RabbitMqEventBus;
import tv.codely.shared.infrastructure.bus.event.rabbitmq.RabbitMqPublisher;

@Configuration
public class MoocRabbitMqEventBusConfiguration {
    private final RabbitMqPublisher publisher;
    private final MySqlEventBus     failoverPublisher;

    public MoocRabbitMqEventBusConfiguration(
        RabbitMqPublisher publisher,
        @Qualifier("moocMysqlEventBus") MySqlEventBus failoverPublisher
    ) {
        this.publisher         = publisher;
        this.failoverPublisher = failoverPublisher;
    }

    @Bean
    public RabbitMqEventBus moocRabbitMqEventBus() {
        return new RabbitMqEventBus(publisher, failoverPublisher);
    }
}
```

## File: `src/mooc/main/tv/codely/mooc/steps/domain/Step.java`
```java
package tv.codely.mooc.steps.domain;

import java.util.Objects;

public abstract class Step {
    private final StepId    id;
    private final StepTitle title;

    public Step(StepId id, StepTitle title) {
        this.id    = id;
        this.title = title;
    }

    public StepId id() {
        return id;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) {
            return true;
        }
        if (o == null || getClass() != o.getClass()) {
            return false;
        }
        Step step = (Step) o;
        return id.equals(step.id) &&
               title.equals(step.title);
    }

    @Override
    public int hashCode() {
        return Objects.hash(id, title);
    }
}
```

## File: `src/mooc/main/tv/codely/mooc/steps/domain/StepId.java`
```java
package tv.codely.mooc.steps.domain;

import tv.codely.shared.domain.Identifier;

public final class StepId extends Identifier {
    public StepId(String value) {
        super(value);
    }
}
```

## File: `src/mooc/main/tv/codely/mooc/steps/domain/StepRepository.java`
```java
package tv.codely.mooc.steps.domain;

import java.util.Optional;

public interface StepRepository {
    void save(Step step);

    Optional<? extends Step> search(StepId id);
}
```

## File: `src/mooc/main/tv/codely/mooc/steps/domain/StepTitle.java`
```java
package tv.codely.mooc.steps.domain;

import tv.codely.shared.domain.StringValueObject;

public final class StepTitle extends StringValueObject {
    public StepTitle(String value) {
        super(value);
    }

    private StepTitle() {
        super(null);
    }
}
```

## File: `src/mooc/main/tv/codely/mooc/steps/domain/challenge/ChallengeStep.java`
```java
package tv.codely.mooc.steps.domain.challenge;

import tv.codely.mooc.steps.domain.Step;
import tv.codely.mooc.steps.domain.StepId;
import tv.codely.mooc.steps.domain.StepTitle;

import java.util.Objects;

public final class ChallengeStep extends Step {
    private final ChallengeStepStatement statement;

    public ChallengeStep(StepId id, StepTitle title, ChallengeStepStatement statement) {
        super(id, title);

        this.statement = statement;
    }

    private ChallengeStep() {
        super(null, null);

        this.statement = null;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) {
            return true;
        }
        if (o == null || getClass() != o.getClass()) {
            return false;
        }
        if (!super.equals(o)) {
            return false;
        }
        ChallengeStep that = (ChallengeStep) o;
        return statement.equals(that.statement);
    }

    @Override
    public int hashCode() {
        return Objects.hash(super.hashCode(), statement);
    }
}
```

## File: `src/mooc/main/tv/codely/mooc/steps/domain/challenge/ChallengeStepStatement.java`
```java
package tv.codely.mooc.steps.domain.challenge;

import tv.codely.shared.domain.StringValueObject;

public final class ChallengeStepStatement extends StringValueObject {
    public ChallengeStepStatement(String value) {
        super(value);
    }

    public ChallengeStepStatement() {
        super(null);
    }
}
```

## File: `src/mooc/main/tv/codely/mooc/steps/domain/video/VideoStep.java`
```java
package tv.codely.mooc.steps.domain.video;

import tv.codely.mooc.steps.domain.Step;
import tv.codely.mooc.steps.domain.StepId;
import tv.codely.mooc.steps.domain.StepTitle;
import tv.codely.shared.domain.VideoUrl;

public final class VideoStep extends Step {
    private final VideoUrl      videoUrl;
    private final VideoStepText text;

    public VideoStep(StepId id, StepTitle title, VideoUrl videoUrl, VideoStepText text) {
        super(id, title);

        this.videoUrl = videoUrl;
        this.text     = text;
    }

    private VideoStep() {
        super(null, null);

        this.videoUrl = null;
        this.text     = null;
    }
}
```

## File: `src/mooc/main/tv/codely/mooc/steps/domain/video/VideoStepText.java`
```java
package tv.codely.mooc.steps.domain.video;

import tv.codely.shared.domain.StringValueObject;

public final class VideoStepText extends StringValueObject {
    public VideoStepText(String value) {
        super(value);
    }

    private VideoStepText() {
        super(null);
    }
}
```

## File: `src/mooc/main/tv/codely/mooc/steps/infrastructure/persistence/MySqlStepRepository.java`
```java
package tv.codely.mooc.steps.infrastructure.persistence;

import org.hibernate.SessionFactory;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.transaction.annotation.Transactional;
import tv.codely.mooc.steps.domain.Step;
import tv.codely.mooc.steps.domain.StepId;
import tv.codely.mooc.steps.domain.StepRepository;
import tv.codely.shared.domain.Service;
import tv.codely.shared.infrastructure.hibernate.HibernateRepository;

import java.util.Optional;

@Service
@Transactional("mooc-transaction_manager")
public class MySqlStepRepository extends HibernateRepository<Step> implements StepRepository {
    public MySqlStepRepository(@Qualifier("mooc-session_factory") SessionFactory sessionFactory) {
        super(sessionFactory, Step.class);
    }

    @Override
    public void save(Step step) {
        persist(step);
    }

    @Override
    public Optional<? extends Step> search(StepId id) {
        return byId(id);
    }
}
```

## File: `src/mooc/main/tv/codely/mooc/steps/infrastructure/persistence/hibernate/VideoStep.hbm.xml`
```xml
<?xml version = "1.0" encoding = "utf-8"?>
<!DOCTYPE hibernate-mapping PUBLIC
        "-//Hibernate/Hibernate Mapping DTD//EN"
        "http://www.hibernate.org/dtd/hibernate-mapping-3.0.dtd">

<hibernate-mapping>
    <class name="tv.codely.mooc.steps.domain.Step" table="steps">
        <composite-id name="id" class="tv.codely.mooc.steps.domain.StepId" access="field">
            <key-property column="id" name="value" length="36" access="field" />
        </composite-id>

        <component name="title" class="tv.codely.mooc.steps.domain.StepTitle" access="field">
            <property name="value" column="title" type="string" access="field" />
        </component>

        <joined-subclass name="tv.codely.mooc.steps.domain.challenge.ChallengeStep" table="steps_challenges">
            <key column="id" />

            <component name="statement" class="tv.codely.mooc.steps.domain.challenge.ChallengeStepStatement"
                       access="field">
                <property name="value" column="statement" type="string" access="field" />
            </component>
        </joined-subclass>

        <joined-subclass name="tv.codely.mooc.steps.domain.video.VideoStep" table="steps_videos">
            <key column="id" />

            <component name="videoUrl" class="tv.codely.shared.domain.VideoUrl" access="field">
                <property name="value" column="url" type="string" access="field" />
            </component>

            <component name="text" class="tv.codely.mooc.steps.domain.video.VideoStepText" access="field">
                <property name="value" column="text" type="string" access="field" />
            </component>
        </joined-subclass>
    </class>
</hibernate-mapping>
```

## File: `src/mooc/main/tv/codely/mooc/students/application/StudentResponse.java`
```java
package tv.codely.mooc.students.application;

import tv.codely.mooc.students.domain.Student;
import tv.codely.shared.domain.bus.query.Response;

public final class StudentResponse implements Response {
    private final String id;
    private final String name;
    private final String surname;
    private final String email;

    public StudentResponse(String id, String name, String surname, String email) {
        this.id      = id;
        this.name    = name;
        this.surname = surname;
        this.email   = email;
    }

    public static StudentResponse fromAggregate(Student student) {
        return new StudentResponse(student.id().value(), student.name(), student.surname(), student.email());
    }

    public String id() {
        return id;
    }

    public String name() {
        return name;
    }

    public String surname() {
        return surname;
    }

    public String email() {
        return email;
    }
}
```

## File: `src/mooc/main/tv/codely/mooc/students/application/StudentsResponse.java`
```java
package tv.codely.mooc.students.application;

import tv.codely.shared.domain.bus.query.Response;

import java.util.List;

public final class StudentsResponse implements Response {
    private final List<StudentResponse> students;

    public StudentsResponse(List<StudentResponse> students) {
        this.students = students;
    }

    public List<StudentResponse> students() {
        return students;
    }
}
```

## File: `src/mooc/main/tv/codely/mooc/students/application/search_all/AllStudentsSearcher.java`
```java
package tv.codely.mooc.students.application.search_all;

import tv.codely.mooc.students.application.StudentResponse;
import tv.codely.mooc.students.application.StudentsResponse;
import tv.codely.mooc.students.domain.StudentRepository;
import tv.codely.shared.domain.Service;

import java.util.stream.Collectors;

@Service
public final class AllStudentsSearcher {
    private final StudentRepository repository;

    public AllStudentsSearcher(StudentRepository repository) {
        this.repository = repository;
    }

    public StudentsResponse search() {
        return new StudentsResponse(
            repository.searchAll().stream().map(StudentResponse::fromAggregate).collect(Collectors.toList())
        );
    }
}
```

## File: `src/mooc/main/tv/codely/mooc/students/application/search_all/SearchAllStudentsQuery.java`
```java
package tv.codely.mooc.students.application.search_all;

import tv.codely.shared.domain.bus.query.Query;

import java.util.Objects;

public final class SearchAllStudentsQuery implements Query {
    @Override
    public boolean equals(Object o) {
        if (this == o) {
            return true;
        }
        return o != null && getClass() == o.getClass();
    }

    @Override
    public int hashCode() {
        return Objects.hash("SearchAllStudentsQuery");
    }
}
```

## File: `src/mooc/main/tv/codely/mooc/students/application/search_all/SearchAllStudentsQueryHandler.java`
```java
package tv.codely.mooc.students.application.search_all;

import tv.codely.mooc.students.application.StudentsResponse;
import tv.codely.shared.domain.Service;
import tv.codely.shared.domain.bus.query.QueryHandler;

@Service
public final class SearchAllStudentsQueryHandler implements QueryHandler<SearchAllStudentsQuery, StudentsResponse> {
    private final AllStudentsSearcher searcher;

    public SearchAllStudentsQueryHandler(AllStudentsSearcher searcher) {
        this.searcher = searcher;
    }

    @Override
    public StudentsResponse handle(SearchAllStudentsQuery query) {
        return searcher.search();
    }
}
```

## File: `src/mooc/main/tv/codely/mooc/students/domain/Student.java`
```java
package tv.codely.mooc.students.domain;

public final class Student {
    private final StudentId id;
    private final String    name;
    private final String    surname;
    private final String    email;

    public Student(StudentId id, String name, String surname, String email) {
        this.id      = id;
        this.name    = name;
        this.surname = surname;
        this.email   = email;
    }

    public StudentId id() {
        return id;
    }

    public String name() {
        return name;
    }

    public String surname() {
        return surname;
    }

    public String email() {
        return email;
    }
}
```

## File: `src/mooc/main/tv/codely/mooc/students/domain/StudentId.java`
```java
package tv.codely.mooc.students.domain;

import tv.codely.shared.domain.Identifier;

public final class StudentId extends Identifier {
    public StudentId(String value) {
        super(value);
    }
}
```

## File: `src/mooc/main/tv/codely/mooc/students/domain/StudentRepository.java`
```java
package tv.codely.mooc.students.domain;

import java.util.List;

public interface StudentRepository {
    List<Student> searchAll();
}
```

## File: `src/mooc/main/tv/codely/mooc/students/infrastructure/InMemoryStudentRepository.java`
```java
package tv.codely.mooc.students.infrastructure;

import tv.codely.mooc.students.domain.Student;
import tv.codely.mooc.students.domain.StudentId;
import tv.codely.mooc.students.domain.StudentRepository;
import tv.codely.shared.domain.Service;
import tv.codely.shared.domain.UuidGenerator;

import java.util.Arrays;
import java.util.List;

@Service
public final class InMemoryStudentRepository implements StudentRepository {
    private UuidGenerator generator;

    public InMemoryStudentRepository(UuidGenerator generator) {
        this.generator = generator;
    }

    @Override
    public List<Student> searchAll() {
        return Arrays.asList(
            new Student(new StudentId(generator.generate()), "name", "surname", "email@mail.com"),
            new Student(new StudentId(generator.generate()), "Other name", "Other surname", "another@mail.com")
        );
    }
}
```

## File: `src/mooc/test/tv/codely/mooc/MoocContextInfrastructureTestCase.java`
```java
package tv.codely.mooc;

import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.ContextConfiguration;
import tv.codely.apps.mooc.backend.MoocBackendApplication;
import tv.codely.shared.infrastructure.InfrastructureTestCase;

@ContextConfiguration(classes = MoocBackendApplication.class)
@SpringBootTest
public abstract class MoocContextInfrastructureTestCase extends InfrastructureTestCase {
}
```

## File: `src/mooc/test/tv/codely/mooc/courses/CoursesModuleInfrastructureTestCase.java`
```java
package tv.codely.mooc.courses;

import org.springframework.beans.factory.annotation.Autowired;
import tv.codely.mooc.MoocContextInfrastructureTestCase;
import tv.codely.mooc.courses.domain.CourseRepository;
import tv.codely.mooc.courses.infrastructure.persistence.InMemoryCourseRepository;

public abstract class CoursesModuleInfrastructureTestCase extends MoocContextInfrastructureTestCase {
    protected InMemoryCourseRepository inMemoryCourseRepository = new InMemoryCourseRepository();
    @Autowired
    protected CourseRepository         mySqlCourseRepository;
}
```

## File: `src/mooc/test/tv/codely/mooc/courses/CoursesModuleUnitTestCase.java`
```java
package tv.codely.mooc.courses;

import org.junit.jupiter.api.BeforeEach;
import tv.codely.mooc.courses.domain.Course;
import tv.codely.mooc.courses.domain.CourseRepository;
import tv.codely.shared.infrastructure.UnitTestCase;

import static org.mockito.Mockito.*;

public abstract class CoursesModuleUnitTestCase extends UnitTestCase {
    protected CourseRepository repository;

    @BeforeEach
    protected void setUp() {
        super.setUp();

        repository = mock(CourseRepository.class);
    }

    public void shouldHaveSaved(Course course) {
        verify(repository, atLeastOnce()).save(course);
    }
}
```

## File: `src/mooc/test/tv/codely/mooc/courses/application/CourseResponseMother.java`
```java
package tv.codely.mooc.courses.application;

import tv.codely.mooc.courses.domain.*;

public final class CourseResponseMother {
    public static CourseResponse create(CourseId id, CourseName name, CourseDuration duration) {
        return new CourseResponse(id.value(), name.value(), duration.value());
    }

    public static CourseResponse random() {
        return create(CourseIdMother.random(), CourseNameMother.random(), CourseDurationMother.random());
    }
}
```

## File: `src/mooc/test/tv/codely/mooc/courses/application/CoursesResponseMother.java`
```java
package tv.codely.mooc.courses.application;

import tv.codely.shared.domain.ListMother;

import java.util.Collections;
import java.util.List;

public final class CoursesResponseMother {
    public static CoursesResponse create(List<CourseResponse> courses) {
        return new CoursesResponse(courses);
    }

    public static CoursesResponse random() {
        return create(ListMother.random(CourseResponseMother::random));
    }

    public static CoursesResponse times(int times) {
        return create(ListMother.create(times, CourseResponseMother::random));
    }

    public static CoursesResponse empty() {
        return create(Collections.emptyList());
    }
}
```

## File: `src/mooc/test/tv/codely/mooc/courses/application/create/CreateCourseCommandHandlerShould.java`
```java
package tv.codely.mooc.courses.application.create;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import tv.codely.mooc.courses.CoursesModuleUnitTestCase;
import tv.codely.mooc.courses.domain.Course;
import tv.codely.mooc.courses.domain.CourseCreatedDomainEventMother;
import tv.codely.mooc.courses.domain.CourseMother;
import tv.codely.shared.domain.course.CourseCreatedDomainEvent;

final class CreateCourseCommandHandlerShould extends CoursesModuleUnitTestCase {
    private CreateCourseCommandHandler handler;

    @BeforeEach
    protected void setUp() {
        super.setUp();

        handler = new CreateCourseCommandHandler(new CourseCreator(repository, eventBus));
    }

    @Test
    void create_a_valid_course() {
        CreateCourseCommand command = CreateCourseCommandMother.random();

        Course                   course      = CourseMother.fromRequest(command);
        CourseCreatedDomainEvent domainEvent = CourseCreatedDomainEventMother.fromCourse(course);

        handler.handle(command);

        shouldHaveSaved(course);
        shouldHavePublished(domainEvent);
    }
}
```

## File: `src/mooc/test/tv/codely/mooc/courses/application/create/CreateCourseCommandMother.java`
```java
package tv.codely.mooc.courses.application.create;

import tv.codely.mooc.courses.domain.*;

public final class CreateCourseCommandMother {
    public static CreateCourseCommand create(CourseId id, CourseName name, CourseDuration duration) {
        return new CreateCourseCommand(id.value(), name.value(), duration.value());
    }

    public static CreateCourseCommand random() {
        return create(CourseIdMother.random(), CourseNameMother.random(), CourseDurationMother.random());
    }
}
```

## File: `src/mooc/test/tv/codely/mooc/courses/application/search_last/SearchLastCoursesQueryMother.java`
```java
package tv.codely.mooc.courses.application.search_last;

import tv.codely.shared.domain.IntegerMother;

public final class SearchLastCoursesQueryMother {
    public static SearchLastCoursesQuery create(Integer total) {
        return new SearchLastCoursesQuery(total);
    }

    public static SearchLastCoursesQuery random() {
        return create(IntegerMother.random());
    }
}
```

## File: `src/mooc/test/tv/codely/mooc/courses/domain/CourseCreatedDomainEventMother.java`
```java
package tv.codely.mooc.courses.domain;

import tv.codely.shared.domain.course.CourseCreatedDomainEvent;

public final class CourseCreatedDomainEventMother {
    public static CourseCreatedDomainEvent create(CourseId id, CourseName name, CourseDuration duration) {
        return new CourseCreatedDomainEvent(id.value(), name.value(), duration.value());
    }

    public static CourseCreatedDomainEvent fromCourse(Course course) {
        return create(course.id(), course.name(), course.duration());
    }

    public static CourseCreatedDomainEvent random() {
        return create(CourseIdMother.random(), CourseNameMother.random(), CourseDurationMother.random());
    }
}
```

## File: `src/mooc/test/tv/codely/mooc/courses/domain/CourseDurationMother.java`
```java
package tv.codely.mooc.courses.domain;

import tv.codely.shared.domain.IntegerMother;
import tv.codely.shared.domain.RandomElementPicker;

public final class CourseDurationMother {
    public static CourseDuration create(String value) {
        return new CourseDuration(value);
    }

    public static CourseDuration random() {
        return create(
            String.format(
                "%s %s",
                IntegerMother.random(),
                RandomElementPicker.from("months", "years", "days", "hours", "minutes", "seconds")
            )
        );
    }
}
```

## File: `src/mooc/test/tv/codely/mooc/courses/domain/CourseIdMother.java`
```java
package tv.codely.mooc.courses.domain;

import tv.codely.shared.domain.UuidMother;

public final class CourseIdMother {
    public static CourseId create(String value) {
        return new CourseId(value);
    }

    public static CourseId random() {
        return create(UuidMother.random());
    }
}
```

## File: `src/mooc/test/tv/codely/mooc/courses/domain/CourseMother.java`
```java
package tv.codely.mooc.courses.domain;

import tv.codely.mooc.courses.application.create.CreateCourseCommand;

public final class CourseMother {
    public static Course create(CourseId id, CourseName name, CourseDuration duration) {
        return new Course(id, name, duration);
    }

    public static Course fromRequest(CreateCourseCommand request) {
        return create(
            CourseIdMother.create(request.id()),
            CourseNameMother.create(request.name()),
            CourseDurationMother.create(request.duration())
        );
    }

    public static Course random() {
        return create(CourseIdMother.random(), CourseNameMother.random(), CourseDurationMother.random());
    }
}
```

## File: `src/mooc/test/tv/codely/mooc/courses/domain/CourseNameMother.java`
```java
package tv.codely.mooc.courses.domain;

import tv.codely.shared.domain.WordMother;

public final class CourseNameMother {
    public static CourseName create(String value) {
        return new CourseName(value);
    }

    public static CourseName random() {
        return create(WordMother.random());
    }
}
```

## File: `src/mooc/test/tv/codely/mooc/courses/infrastructure/persistence/InMemoryCourseRepositoryShould.java`
```java
package tv.codely.mooc.courses.infrastructure.persistence;

import org.junit.jupiter.api.Test;
import tv.codely.mooc.courses.CoursesModuleInfrastructureTestCase;
import tv.codely.mooc.courses.domain.Course;
import tv.codely.mooc.courses.domain.CourseIdMother;
import tv.codely.mooc.courses.domain.CourseMother;

import java.util.Optional;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertFalse;

final class InMemoryCourseRepositoryShould extends CoursesModuleInfrastructureTestCase {
    @Test
    void save_a_course() {
        Course course = CourseMother.random();

        inMemoryCourseRepository.save(course);
    }

    @Test
    void return_an_existing_course() {
        Course course = CourseMother.random();

        inMemoryCourseRepository.save(course);

        assertEquals(Optional.of(course), inMemoryCourseRepository.search(course.id()));
    }

    @Test
    void not_return_a_non_existing_course() {
        assertFalse(inMemoryCourseRepository.search(CourseIdMother.random()).isPresent());
    }
}
```

## File: `src/mooc/test/tv/codely/mooc/courses/infrastructure/persistence/MySqlCourseRepositoryShould.java`
```java
package tv.codely.mooc.courses.infrastructure.persistence;

import org.junit.jupiter.api.Test;
import tv.codely.mooc.courses.CoursesModuleInfrastructureTestCase;
import tv.codely.mooc.courses.domain.Course;
import tv.codely.mooc.courses.domain.CourseIdMother;
import tv.codely.mooc.courses.domain.CourseMother;

import jakarta.transaction.Transactional;
import java.util.Optional;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertFalse;

@Transactional
class MySqlCourseRepositoryShould extends CoursesModuleInfrastructureTestCase {
    @Test
    void save_a_course() {
        Course course = CourseMother.random();

        mySqlCourseRepository.save(course);
    }

    @Test
    void return_an_existing_course() {
        Course course = CourseMother.random();

        mySqlCourseRepository.save(course);

        assertEquals(Optional.of(course), mySqlCourseRepository.search(course.id()));
    }

    @Test
    void not_return_a_non_existing_course() {
        assertFalse(mySqlCourseRepository.search(CourseIdMother.random()).isPresent());
    }
}
```

## File: `src/mooc/test/tv/codely/mooc/courses_counter/CoursesCounterModuleInfrastructureTestCase.java`
```java
package tv.codely.mooc.courses_counter;

import org.springframework.beans.factory.annotation.Autowired;
import tv.codely.mooc.MoocContextInfrastructureTestCase;
import tv.codely.mooc.courses_counter.domain.CoursesCounterRepository;

public abstract class CoursesCounterModuleInfrastructureTestCase extends MoocContextInfrastructureTestCase {
    @Autowired
    protected CoursesCounterRepository repository;
}
```

## File: `src/mooc/test/tv/codely/mooc/courses_counter/CoursesCounterModuleUnitTestCase.java`
```java
package tv.codely.mooc.courses_counter;

import org.junit.jupiter.api.BeforeEach;
import org.mockito.Mockito;
import tv.codely.mooc.courses_counter.domain.CoursesCounter;
import tv.codely.mooc.courses_counter.domain.CoursesCounterRepository;
import tv.codely.shared.infrastructure.UnitTestCase;

import java.util.Optional;

import static org.mockito.Mockito.*;

public abstract class CoursesCounterModuleUnitTestCase extends UnitTestCase {
    protected CoursesCounterRepository repository;

    @BeforeEach
    protected void setUp() {
        super.setUp();

        repository = mock(CoursesCounterRepository.class);
    }

    public void shouldSearch(CoursesCounter course) {
        Mockito.when(repository.search()).thenReturn(Optional.of(course));
    }

    public void shouldSearch() {
        Mockito.when(repository.search()).thenReturn(Optional.empty());
    }

    public void shouldHaveSaved(CoursesCounter course) {
        verify(repository, atLeastOnce()).save(course);
    }
}
```

## File: `src/mooc/test/tv/codely/mooc/courses_counter/application/find/CoursesCounterResponseMother.java`
```java
package tv.codely.mooc.courses_counter.application.find;

import tv.codely.shared.domain.IntegerMother;

final class CoursesCounterResponseMother {
    public static CoursesCounterResponse create(Integer value) {
        return new CoursesCounterResponse(value);
    }

    public static CoursesCounterResponse random() {
        return create(IntegerMother.random());
    }
}
```

## File: `src/mooc/test/tv/codely/mooc/courses_counter/application/find/FindCoursesCounterQueryHandlerShould.java`
```java
package tv.codely.mooc.courses_counter.application.find;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import tv.codely.mooc.courses_counter.CoursesCounterModuleUnitTestCase;
import tv.codely.mooc.courses_counter.domain.CoursesCounter;
import tv.codely.mooc.courses_counter.domain.CoursesCounterMother;
import tv.codely.mooc.courses_counter.domain.CoursesCounterNotInitialized;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;

final class FindCoursesCounterQueryHandlerShould extends CoursesCounterModuleUnitTestCase {
    FindCoursesCounterQueryHandler handler;

    @BeforeEach
    protected void setUp() {
        super.setUp();

        handler = new FindCoursesCounterQueryHandler(new CoursesCounterFinder(repository));
    }

    @Test
    void it_should_find_an_existing_courses_counter() {
        CoursesCounter          counter  = CoursesCounterMother.random();
        FindCoursesCounterQuery query    = new FindCoursesCounterQuery();
        CoursesCounterResponse  response = CoursesCounterResponseMother.create(counter.total().value());

        shouldSearch(counter);

        assertEquals(response, handler.handle(query));
    }

    @Test
    void it_should_throw_an_exception_when_courses_counter_does_not_exists() {
        FindCoursesCounterQuery query = new FindCoursesCounterQuery();

        shouldSearch();

        assertThrows(CoursesCounterNotInitialized.class, () -> handler.handle(query));
    }
}
```

## File: `src/mooc/test/tv/codely/mooc/courses_counter/application/increment/IncrementCoursesCounterOnCourseCreatedShould.java`
```java
package tv.codely.mooc.courses_counter.application.increment;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import tv.codely.mooc.courses.domain.CourseCreatedDomainEventMother;
import tv.codely.mooc.courses.domain.CourseId;
import tv.codely.mooc.courses.domain.CourseIdMother;
import tv.codely.mooc.courses_counter.CoursesCounterModuleUnitTestCase;
import tv.codely.mooc.courses_counter.domain.CoursesCounter;
import tv.codely.mooc.courses_counter.domain.CoursesCounterMother;
import tv.codely.shared.domain.course.CourseCreatedDomainEvent;

final class IncrementCoursesCounterOnCourseCreatedShould extends CoursesCounterModuleUnitTestCase {
    IncrementCoursesCounterOnCourseCreated subscriber;

    @BeforeEach
    protected void setUp() {
        super.setUp();

        subscriber = new IncrementCoursesCounterOnCourseCreated(
            new CoursesCounterIncrementer(repository, uuidGenerator)
        );
    }

    @Test
    void it_should_initialize_a_new_counter() {
        CourseCreatedDomainEvent event = CourseCreatedDomainEventMother.random();

        CourseId       courseId   = CourseIdMother.create(event.aggregateId());
        CoursesCounter newCounter = CoursesCounterMother.withOne(courseId);

        shouldSearch();
        shouldGenerateUuid(newCounter.id().value());

        subscriber.on(event);

        shouldHaveSaved(newCounter);
    }

    @Test
    void it_should_increment_an_existing_counter() {
        CourseCreatedDomainEvent event = CourseCreatedDomainEventMother.random();

        CourseId       courseId           = CourseIdMother.create(event.aggregateId());
        CoursesCounter existingCounter    = CoursesCounterMother.random();
        CoursesCounter incrementedCounter = CoursesCounterMother.incrementing(existingCounter, courseId);

        shouldSearch(existingCounter);

        subscriber.on(event);

        shouldHaveSaved(incrementedCounter);
    }

    @Test
    void it_should_not_increment_an_already_incremented_course() {
        CourseCreatedDomainEvent event = CourseCreatedDomainEventMother.random();

        CourseId       courseId        = CourseIdMother.create(event.aggregateId());
        CoursesCounter existingCounter = CoursesCounterMother.withOne(courseId);

        shouldSearch(existingCounter);

        subscriber.on(event);
    }
}
```

## File: `src/mooc/test/tv/codely/mooc/courses_counter/domain/CoursesCounterIdMother.java`
```java
package tv.codely.mooc.courses_counter.domain;

import tv.codely.shared.domain.UuidMother;

public final class CoursesCounterIdMother {
    public static CoursesCounterId create(String value) {
        return new CoursesCounterId(value);
    }

    public static CoursesCounterId random() {
        return create(UuidMother.random());
    }
}
```

## File: `src/mooc/test/tv/codely/mooc/courses_counter/domain/CoursesCounterMother.java`
```java
package tv.codely.mooc.courses_counter.domain;

import tv.codely.mooc.courses.domain.CourseId;
import tv.codely.mooc.courses.domain.CourseIdMother;
import tv.codely.shared.domain.ListMother;

import java.util.ArrayList;
import java.util.List;

public final class CoursesCounterMother {
    public static CoursesCounter create(
        CoursesCounterId id,
        CoursesCounterTotal total,
        List<CourseId> existingCourses
    ) {
        return new CoursesCounter(id, total, existingCourses);
    }

    public static CoursesCounter withOne(CourseId courseId) {
        return create(CoursesCounterIdMother.random(), CoursesCounterTotalMother.one(), ListMother.one(courseId));
    }

    public static CoursesCounter random() {
        List<CourseId> existingCourses = ListMother.random(CourseIdMother::random);

        return create(
            CoursesCounterIdMother.random(),
            CoursesCounterTotalMother.create(existingCourses.size()),
            existingCourses
        );
    }

    public static CoursesCounter incrementing(CoursesCounter existingCounter, CourseId courseId) {
        List<CourseId> existingCourses = new ArrayList<>(existingCounter.existingCourses());
        existingCourses.add(courseId);

        return create(
            existingCounter.id(),
            CoursesCounterTotalMother.create(existingCounter.total().value() + 1),
            existingCourses
        );
    }
}
```

## File: `src/mooc/test/tv/codely/mooc/courses_counter/domain/CoursesCounterTotalMother.java`
```java
package tv.codely.mooc.courses_counter.domain;

import tv.codely.shared.domain.IntegerMother;

public final class CoursesCounterTotalMother {
    public static CoursesCounterTotal create(Integer value) {
        return new CoursesCounterTotal(value);
    }

    public static CoursesCounterTotal random() {
        return create(IntegerMother.random());
    }

    public static CoursesCounterTotal one() {
        return create(1);
    }
}
```

## File: `src/mooc/test/tv/codely/mooc/courses_counter/infrastructure/persistence/MySqlCoursesCounterRepositoryShould.java`
```java
package tv.codely.mooc.courses_counter.infrastructure.persistence;

import org.junit.jupiter.api.Test;
import tv.codely.mooc.courses_counter.CoursesCounterModuleInfrastructureTestCase;
import tv.codely.mooc.courses_counter.domain.CoursesCounter;
import tv.codely.mooc.courses_counter.domain.CoursesCounterMother;

import jakarta.transaction.Transactional;
import java.util.Optional;

import static org.junit.jupiter.api.Assertions.assertEquals;

@Transactional
class MySqlCoursesCounterRepositoryShould extends CoursesCounterModuleInfrastructureTestCase {
    @Test
    void return_an_existing_courses_counter() {
        CoursesCounter counter = CoursesCounterMother.random();

        repository.save(counter);

        assertEquals(Optional.of(counter), repository.search());
    }
}
```

## File: `src/mooc/test/tv/codely/mooc/notifications/application/NotificationsModuleUnitTestCase.java`
```java
package tv.codely.mooc.notifications.application;

import org.junit.jupiter.api.BeforeEach;
import org.mockito.ArgumentCaptor;
import tv.codely.mooc.notifications.domain.Email;
import tv.codely.mooc.notifications.domain.EmailSender;
import tv.codely.shared.infrastructure.UnitTestCase;

import java.util.List;

import static org.junit.jupiter.api.Assertions.assertTrue;
import static org.mockito.Mockito.*;

public abstract class NotificationsModuleUnitTestCase extends UnitTestCase {
    protected EmailSender sender;

    @BeforeEach
    protected void setUp() {
        super.setUp();

        sender = mock(EmailSender.class);
    }

    public void shouldHaveSentEmail(Email email) {
        ArgumentCaptor<Email> argument = ArgumentCaptor.forClass(Email.class);

        verify(sender, atLeastOnce()).send(argument.capture());

        List<Email> emails = argument.getAllValues();

        assertTrue(emails.contains(email));
    }
}
```

## File: `src/mooc/test/tv/codely/mooc/notifications/application/send_new_courses_newsletter/SendNewCoursesNewsletterCommandMother.java`
```java
package tv.codely.mooc.notifications.application.send_new_courses_newsletter;

import tv.codely.shared.domain.UuidMother;

public final class SendNewCoursesNewsletterCommandMother {
    public static SendNewCoursesNewsletterCommand random() {
        return new SendNewCoursesNewsletterCommand(UuidMother.random());
    }
}
```

## File: `src/mooc/test/tv/codely/mooc/notifications/domain/EmailIdMother.java`
```java
package tv.codely.mooc.notifications.domain;

import tv.codely.shared.domain.UuidMother;

public final class EmailIdMother {
    public static EmailId create(String value) {
        return new EmailId(value);
    }

    public static EmailId random() {
        return create(UuidMother.random());
    }
}
```

## File: `src/mooc/test/tv/codely/mooc/notifications/domain/NewCoursesNewsletterEmailSentMother.java`
```java
package tv.codely.mooc.notifications.domain;

import tv.codely.mooc.students.domain.StudentIdMother;

public final class NewCoursesNewsletterEmailSentMother {
    public static NewCoursesNewsletterEmailSent create(EmailId id, String studentId) {
        return new NewCoursesNewsletterEmailSent(id.value(), studentId);
    }

    public static NewCoursesNewsletterEmailSent random() {
        return create(EmailIdMother.random(), StudentIdMother.random().value());
    }
}
```

## File: `src/mooc/test/tv/codely/mooc/notifications/domain/NewCoursesNewsletterMother.java`
```java
package tv.codely.mooc.notifications.domain;

import tv.codely.mooc.courses.application.CoursesResponse;
import tv.codely.mooc.courses.application.CoursesResponseMother;
import tv.codely.mooc.students.application.StudentResponse;
import tv.codely.mooc.students.application.StudentResponseMother;

public final class NewCoursesNewsletterMother {
    public static NewCoursesNewsletter create(EmailId id, StudentResponse student, CoursesResponse courses) {
        return new NewCoursesNewsletter(id, student, courses);
    }

    public static NewCoursesNewsletter create(StudentResponse student, CoursesResponse courses) {
        return new NewCoursesNewsletter(EmailIdMother.random(), student, courses);
    }

    public static NewCoursesNewsletter random() {
        return create(EmailIdMother.random(), StudentResponseMother.random(), CoursesResponseMother.random());
    }
}
```

## File: `src/mooc/test/tv/codely/mooc/steps/StepsModuleInfrastructureTestCase.java`
```java
package tv.codely.mooc.steps;

import org.springframework.beans.factory.annotation.Autowired;
import tv.codely.mooc.MoocContextInfrastructureTestCase;
import tv.codely.mooc.steps.domain.StepRepository;

public abstract class StepsModuleInfrastructureTestCase extends MoocContextInfrastructureTestCase {
    @Autowired
    protected StepRepository repository;
}
```

## File: `src/mooc/test/tv/codely/mooc/steps/domain/StepIdMother.java`
```java
package tv.codely.mooc.steps.domain;

import tv.codely.shared.domain.UuidMother;

public final class StepIdMother {
    public static StepId create(String value) {
        return new StepId(value);
    }

    public static StepId random() {
        return create(UuidMother.random());
    }
}
```

## File: `src/mooc/test/tv/codely/mooc/steps/domain/StepTitleMother.java`
```java
package tv.codely.mooc.steps.domain;

import tv.codely.shared.domain.WordMother;

public final class StepTitleMother {
    public static StepTitle create(String value) {
        return new StepTitle(value);
    }

    public static StepTitle random() {
        return create(WordMother.random());
    }
}
```

## File: `src/mooc/test/tv/codely/mooc/steps/domain/challenge/ChallengeStepMother.java`
```java
package tv.codely.mooc.steps.domain.challenge;

import tv.codely.mooc.steps.domain.StepId;
import tv.codely.mooc.steps.domain.StepIdMother;
import tv.codely.mooc.steps.domain.StepTitle;
import tv.codely.mooc.steps.domain.StepTitleMother;

public final class ChallengeStepMother {
    public static ChallengeStep create(StepId id, StepTitle title, ChallengeStepStatement statement) {
        return new ChallengeStep(id, title, statement);
    }

    public static ChallengeStep random() {
        return create(StepIdMother.random(), StepTitleMother.random(), ChallengeStepStatementMother.random());
    }
}
```

## File: `src/mooc/test/tv/codely/mooc/steps/domain/challenge/ChallengeStepStatementMother.java`
```java
package tv.codely.mooc.steps.domain.challenge;

import tv.codely.shared.domain.WordMother;

public final class ChallengeStepStatementMother {
    public static ChallengeStepStatement create(String value) {
        return new ChallengeStepStatement(value);
    }

    public static ChallengeStepStatement random() {
        return create(WordMother.random());
    }
}
```

## File: `src/mooc/test/tv/codely/mooc/steps/domain/video/VideoStepMother.java`
```java
package tv.codely.mooc.steps.domain.video;

import tv.codely.mooc.steps.domain.StepId;
import tv.codely.mooc.steps.domain.StepIdMother;
import tv.codely.mooc.steps.domain.StepTitle;
import tv.codely.mooc.steps.domain.StepTitleMother;
import tv.codely.shared.domain.VideoUrl;
import tv.codely.shared.domain.VideoUrlMother;

public final class VideoStepMother {
    public static VideoStep create(StepId id, StepTitle title, VideoUrl videoUrl, VideoStepText text) {
        return new VideoStep(id, title, videoUrl, text);
    }

    public static VideoStep random() {
        return create(
            StepIdMother.random(),
            StepTitleMother.random(),
            VideoUrlMother.random(),
            VideoStepTextMother.random()
        );
    }
}
```

## File: `src/mooc/test/tv/codely/mooc/steps/domain/video/VideoStepTextMother.java`
```java
package tv.codely.mooc.steps.domain.video;

import tv.codely.shared.domain.WordMother;

public final class VideoStepTextMother {
    public static VideoStepText create(String value) {
        return new VideoStepText(value);
    }

    public static VideoStepText random() {
        return create(WordMother.random());
    }
}
```

## File: `src/mooc/test/tv/codely/mooc/steps/infrastructure/persistence/MySqlStepRepositoryShould.java`
```java
package tv.codely.mooc.steps.infrastructure.persistence;

import org.junit.jupiter.api.Test;
import tv.codely.mooc.steps.StepsModuleInfrastructureTestCase;
import tv.codely.mooc.steps.domain.Step;
import tv.codely.mooc.steps.domain.StepIdMother;
import tv.codely.mooc.steps.domain.challenge.ChallengeStepMother;
import tv.codely.mooc.steps.domain.video.VideoStepMother;

import jakarta.transaction.Transactional;
import java.util.Arrays;
import java.util.List;
import java.util.Optional;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertFalse;

@Transactional
class MySqlStepRepositoryShould extends StepsModuleInfrastructureTestCase {
    @Test
    void save_a_step() {
        for (Step step : steps()) {
            repository.save(step);
        }
    }

    @Test
    void return_an_existing_step() {
        for (Step step : steps()) {
            repository.save(step);

            assertEquals(Optional.of(step), repository.search(step.id()));
        }
    }

    @Test
    void not_return_a_non_existing_course() {
        assertFalse(repository.search(StepIdMother.random()).isPresent());
    }

    private List<? extends Step> steps() {
        return Arrays.asList(ChallengeStepMother.random(), VideoStepMother.random());
    }
}
```

## File: `src/mooc/test/tv/codely/mooc/students/application/StudentResponseMother.java`
```java
package tv.codely.mooc.students.application;

import tv.codely.mooc.students.domain.StudentId;
import tv.codely.mooc.students.domain.StudentIdMother;
import tv.codely.shared.domain.EmailMother;
import tv.codely.shared.domain.WordMother;

public final class StudentResponseMother {
    public static StudentResponse create(StudentId id, String name, String surname, String email) {
        return new StudentResponse(id.value(), name, surname, email);
    }

    public static StudentResponse random() {
        return create(StudentIdMother.random(), WordMother.random(), WordMother.random(), EmailMother.random());
    }
}
```

## File: `src/mooc/test/tv/codely/mooc/students/application/StudentsResponseMother.java`
```java
package tv.codely.mooc.students.application;

import tv.codely.shared.domain.ListMother;

import java.util.Collections;
import java.util.List;

public final class StudentsResponseMother {
    public static StudentsResponse create(List<StudentResponse> courses) {
        return new StudentsResponse(courses);
    }

    public static StudentsResponse random() {
        return create(ListMother.random(StudentResponseMother::random));
    }

    public static StudentsResponse empty() {
        return create(Collections.emptyList());
    }
}
```

## File: `src/mooc/test/tv/codely/mooc/students/application/search_all/SearchAllStudentsQueryMother.java`
```java
package tv.codely.mooc.students.application.search_all;

public final class SearchAllStudentsQueryMother {
    public static SearchAllStudentsQuery random() {
        return new SearchAllStudentsQuery();
    }
}
```

## File: `src/mooc/test/tv/codely/mooc/students/domain/StudentIdMother.java`
```java
package tv.codely.mooc.students.domain;

import tv.codely.shared.domain.UuidMother;

public final class StudentIdMother {
    public static StudentId create(String value) {
        return new StudentId(value);
    }

    public static StudentId random() {
        return create(UuidMother.random());
    }
}
```

## File: `src/shared/build.gradle`
```
dependencies {
}
```

## File: `src/shared/main/tv/codely/shared/domain/AggregateRoot.java`
```java
package tv.codely.shared.domain;

import tv.codely.shared.domain.bus.event.DomainEvent;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public abstract class AggregateRoot {
    private List<DomainEvent> domainEvents = new ArrayList<>();

    final public List<DomainEvent> pullDomainEvents() {
        List<DomainEvent> events = domainEvents;

        domainEvents = Collections.emptyList();

        return events;
    }

    final protected void record(DomainEvent event) {
        domainEvents.add(event);
    }
}
```

## File: `src/shared/main/tv/codely/shared/domain/DomainError.java`
```java
package tv.codely.shared.domain;

public abstract class DomainError extends RuntimeException {
    private final String errorCode;
    private final String errorMessage;

    public DomainError(String errorCode, String errorMessage) {
        super(errorMessage);

        this.errorCode    = errorCode;
        this.errorMessage = errorMessage;
    }

    public String errorCode() {
        return errorCode;
    }

    public String errorMessage() {
        return errorMessage;
    }
}
```

## File: `src/shared/main/tv/codely/shared/domain/Identifier.java`
```java
package tv.codely.shared.domain;

import java.io.Serializable;
import java.util.Objects;
import java.util.UUID;

public abstract class Identifier implements Serializable {
    final protected String value;

    public Identifier(String value) {
        ensureValidUuid(value);

        this.value = value;
    }

    protected Identifier() {
        this.value = null;
    }

    public String value() {
        return value;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) {
            return true;
        }
        if (o == null || getClass() != o.getClass()) {
            return false;
        }
        Identifier that = (Identifier) o;
        return value.equals(that.value);
    }

    @Override
    public int hashCode() {
        return Objects.hash(value);
    }

    private void ensureValidUuid(String value) throws IllegalArgumentException {
        UUID.fromString(value);
    }
}
```

## File: `src/shared/main/tv/codely/shared/domain/IntValueObject.java`
```java
package tv.codely.shared.domain;

import java.util.Objects;

public abstract class IntValueObject {
    private Integer value;

    public IntValueObject(Integer value) {
        this.value = value;
    }

    public Integer value() {
        return value;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) {
            return true;
        }
        if (o == null || getClass() != o.getClass()) {
            return false;
        }
        IntValueObject that = (IntValueObject) o;
        return value.equals(that.value);
    }

    @Override
    public int hashCode() {
        return Objects.hash(value);
    }
}
```

## File: `src/shared/main/tv/codely/shared/domain/Logger.java`
```java
package tv.codely.shared.domain;

import java.io.Serializable;
import java.util.HashMap;

public interface Logger {
    void info(String $message);
    void info(String $message, HashMap<String, Serializable> $context);

    void warning(String $message);
    void warning(String $message, HashMap<String, Serializable> $context);

    void critical(String $message);
    void critical(String $message, HashMap<String, Serializable> $context);
}
```

## File: `src/shared/main/tv/codely/shared/domain/Monitoring.java`
```java
package tv.codely.shared.domain;

import java.util.HashMap;

public interface Monitoring {
    void incrementCounter(int times);

    void incrementGauge(int times);
    void decrementGauge(int times);
    void setGauge(int value);

    void observeHistogram(int value, HashMap<String, String> labels);
}
```

## File: `src/shared/main/tv/codely/shared/domain/Service.java`
```java
package tv.codely.shared.domain;

import java.lang.annotation.*;

@Retention(RetentionPolicy.RUNTIME)
@Target(ElementType.TYPE)
@Inherited
public @interface Service {
}
```

## File: `src/shared/main/tv/codely/shared/domain/StringValueObject.java`
```java
package tv.codely.shared.domain;

import java.util.Objects;

public abstract class StringValueObject {
    private String value;

    public StringValueObject(String value) {
        this.value = value;
    }

    public String value() {
        return value;
    }

    @Override
    public String toString() {
        return this.value();
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) {
            return true;
        }
        if (!(o instanceof StringValueObject)) {
            return false;
        }
        StringValueObject that = (StringValueObject) o;
        return Objects.equals(value, that.value);
    }

    @Override
    public int hashCode() {
        return Objects.hash(value);
    }
}
```

## File: `src/shared/main/tv/codely/shared/domain/Utils.java`
```java
package tv.codely.shared.domain;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.google.common.base.CaseFormat;

import java.io.IOException;
import java.io.Serializable;
import java.sql.Timestamp;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.HashMap;

public final class Utils {
    public static String dateToString(LocalDateTime dateTime) {
        return dateTime.format(DateTimeFormatter.ISO_LOCAL_DATE);
    }

    public static String dateToString(Timestamp timestamp) {
        return dateToString(timestamp.toLocalDateTime());
    }

    public static String jsonEncode(HashMap<String, Serializable> map) {
        try {
            return new ObjectMapper().writeValueAsString(map);
        } catch (JsonProcessingException e) {
            return "";
        }
    }

    public static HashMap<String, Serializable> jsonDecode(String body) {
        try {
            return new ObjectMapper().readValue(body, HashMap.class);
        } catch (IOException e) {
            return null;
        }
    }

    public static String toSnake(String text) {
        return CaseFormat.UPPER_CAMEL.to(CaseFormat.LOWER_UNDERSCORE, text);
    }

    public static String toCamel(String text) {
        return CaseFormat.LOWER_UNDERSCORE.to(CaseFormat.UPPER_CAMEL, text);
    }

    public static String toCamelFirstLower(String text) {
        return CaseFormat.LOWER_UNDERSCORE.to(CaseFormat.LOWER_CAMEL, text);
    }

	public static void retry(int numberOfRetries, long waitTimeInMillis, Runnable operation) throws Exception {
		for (int i = 0; i < numberOfRetries; i++) {
			try {
				operation.run();
				return; // Success, exit the method
			} catch (Exception ex) {
				System.out.println("Retry " + (i + 1) + "/" + numberOfRetries + " fail. Retrying…");
				if (i >= numberOfRetries - 1) {
					throw ex;
				}

				try {
					Thread.sleep(waitTimeInMillis);
				} catch (InterruptedException ie) {
					Thread.currentThread().interrupt();

					throw new Exception("Operation interrupted while retrying", ie);
				}
			}
		}
	}

}
```

## File: `src/shared/main/tv/codely/shared/domain/UuidGenerator.java`
```java
package tv.codely.shared.domain;

public interface UuidGenerator {
    String generate();
}
```

## File: `src/shared/main/tv/codely/shared/domain/VideoUrl.java`
```java
package tv.codely.shared.domain;

public final class VideoUrl extends StringValueObject {
    public VideoUrl(String value) {
        super(value);
    }

    public VideoUrl() {
        super(null);
    }
}
```

## File: `src/shared/main/tv/codely/shared/domain/bus/command/Command.java`
```java
package tv.codely.shared.domain.bus.command;

public interface Command {
}
```

## File: `src/shared/main/tv/codely/shared/domain/bus/command/CommandBus.java`
```java
package tv.codely.shared.domain.bus.command;

public interface CommandBus {
    void dispatch(Command command) throws CommandHandlerExecutionError;
}
```

## File: `src/shared/main/tv/codely/shared/domain/bus/command/CommandHandler.java`
```java
package tv.codely.shared.domain.bus.command;

public interface CommandHandler<T extends Command> {
    void handle(T command);
}
```

## File: `src/shared/main/tv/codely/shared/domain/bus/command/CommandHandlerExecutionError.java`
```java
package tv.codely.shared.domain.bus.command;

public final class CommandHandlerExecutionError extends RuntimeException {
    public CommandHandlerExecutionError(Throwable cause) {
        super(cause);
    }
}
```

## File: `src/shared/main/tv/codely/shared/domain/bus/command/CommandNotRegisteredError.java`
```java
package tv.codely.shared.domain.bus.command;

public final class CommandNotRegisteredError extends Exception {
    public CommandNotRegisteredError(Class<? extends Command> command) {
        super(String.format("The command <%s> hasn't a command handler associated", command.toString()));
    }
}
```

## File: `src/shared/main/tv/codely/shared/domain/bus/event/DomainEvent.java`
```java
package tv.codely.shared.domain.bus.event;

import tv.codely.shared.domain.Utils;

import java.io.Serializable;
import java.time.LocalDateTime;
import java.util.HashMap;
import java.util.UUID;

public abstract class DomainEvent {
    private String aggregateId;
    private String eventId;
    private String occurredOn;

    public DomainEvent(String aggregateId) {
        this.aggregateId = aggregateId;
        this.eventId     = UUID.randomUUID().toString();
        this.occurredOn  = Utils.dateToString(LocalDateTime.now());
    }

    public DomainEvent(String aggregateId, String eventId, String occurredOn) {
        this.aggregateId = aggregateId;
        this.eventId     = eventId;
        this.occurredOn  = occurredOn;
    }

    protected DomainEvent() {
    }

    public abstract String eventName();

    public abstract HashMap<String, Serializable> toPrimitives();

    public abstract DomainEvent fromPrimitives(
        String aggregateId,
        HashMap<String, Serializable> body,
        String eventId,
        String occurredOn
    );

    public String aggregateId() {
        return aggregateId;
    }

    public String eventId() {
        return eventId;
    }

    public String occurredOn() {
        return occurredOn;
    }
}
```

## File: `src/shared/main/tv/codely/shared/domain/bus/event/DomainEventSubscriber.java`
```java
package tv.codely.shared.domain.bus.event;

import java.lang.annotation.*;

@Retention(RetentionPolicy.RUNTIME)
@Target(ElementType.TYPE)
@Inherited
public @interface DomainEventSubscriber {
    Class<? extends DomainEvent>[] value();
}
```

## File: `src/shared/main/tv/codely/shared/domain/bus/event/EventBus.java`
```java
package tv.codely.shared.domain.bus.event;

import java.util.List;

public interface EventBus {
    void publish(final List<DomainEvent> events);
}
```

## File: `src/shared/main/tv/codely/shared/domain/bus/query/Query.java`
```java
package tv.codely.shared.domain.bus.query;

public interface Query {
}
```

## File: `src/shared/main/tv/codely/shared/domain/bus/query/QueryBus.java`
```java
package tv.codely.shared.domain.bus.query;

public interface QueryBus {
    <R> R ask(Query query) throws QueryHandlerExecutionError;
}
```

## File: `src/shared/main/tv/codely/shared/domain/bus/query/QueryHandler.java`
```java
package tv.codely.shared.domain.bus.query;

public interface QueryHandler<Q extends Query, R extends Response> {
    R handle(Q query);
}
```

## File: `src/shared/main/tv/codely/shared/domain/bus/query/QueryHandlerExecutionError.java`
```java
package tv.codely.shared.domain.bus.query;

public final class QueryHandlerExecutionError extends RuntimeException {
    public QueryHandlerExecutionError(Throwable cause) {
        super(cause);
    }
}
```

## File: `src/shared/main/tv/codely/shared/domain/bus/query/QueryNotRegisteredError.java`
```java
package tv.codely.shared.domain.bus.query;

public final class QueryNotRegisteredError extends Exception {
    public QueryNotRegisteredError(Class<? extends Query> query) {
        super(String.format("The query <%s> hasn't a query handler associated", query.toString()));
    }
}
```

## File: `src/shared/main/tv/codely/shared/domain/bus/query/Response.java`
```java
package tv.codely.shared.domain.bus.query;

public interface Response {
}
```

## File: `src/shared/main/tv/codely/shared/domain/course/CourseCreatedDomainEvent.java`
```java
package tv.codely.shared.domain.course;

import tv.codely.shared.domain.bus.event.DomainEvent;

import java.io.Serializable;
import java.util.HashMap;
import java.util.Objects;

public final class CourseCreatedDomainEvent extends DomainEvent {
    private final String name;
    private final String duration;

    public CourseCreatedDomainEvent() {
        super(null);

        this.name     = null;
        this.duration = null;
    }

    public CourseCreatedDomainEvent(String aggregateId, String name, String duration) {
        super(aggregateId);

        this.name     = name;
        this.duration = duration;
    }

    public CourseCreatedDomainEvent(
        String aggregateId,
        String eventId,
        String occurredOn,
        String name,
        String duration
    ) {
        super(aggregateId, eventId, occurredOn);

        this.name     = name;
        this.duration = duration;
    }

    @Override
    public String eventName() {
        return "course.created";
    }

    @Override
    public HashMap<String, Serializable> toPrimitives() {
        return new HashMap<String, Serializable>() {{
            put("name", name);
            put("duration", duration);
        }};
    }

    @Override
    public CourseCreatedDomainEvent fromPrimitives(
        String aggregateId,
        HashMap<String, Serializable> body,
        String eventId,
        String occurredOn
    ) {
        return new CourseCreatedDomainEvent(
            aggregateId,
            eventId,
            occurredOn,
            (String) body.get("name"),
            (String) body.get("duration")
        );
    }

    public String name() {
        return name;
    }

    public String duration() {
        return duration;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) {
            return true;
        }
        if (o == null || getClass() != o.getClass()) {
            return false;
        }
        CourseCreatedDomainEvent that = (CourseCreatedDomainEvent) o;
        return name.equals(that.name) &&
               duration.equals(that.duration);
    }

    @Override
    public int hashCode() {
        return Objects.hash(name, duration);
    }
}
```

## File: `src/shared/main/tv/codely/shared/domain/criteria/Criteria.java`
```java
package tv.codely.shared.domain.criteria;

import java.util.Optional;

public final class Criteria {
    private final Filters           filters;
    private final Order             order;
    private final Optional<Integer> limit;
    private final Optional<Integer> offset;

    public Criteria(Filters filters, Order order, Optional<Integer> limit, Optional<Integer> offset) {
        this.filters = filters;
        this.order   = order;
        this.limit   = limit;
        this.offset  = offset;
    }

    public Criteria(Filters filters, Order order) {
        this.filters = filters;
        this.order   = order;
        this.limit   = Optional.empty();
        this.offset  = Optional.empty();
    }

    public Filters filters() {
        return filters;
    }

    public Order order() {
        return order;
    }

    public Optional<Integer> limit() {
        return limit;
    }

    public Optional<Integer> offset() {
        return offset;
    }

    public boolean hasFilters() {
        return filters.filters().size() > 0;
    }

    public String serialize() {
        return String.format(
            "%s~~%s~~%s~~%s",
            filters.serialize(),
            order.serialize(),
            offset.orElse(0),
            limit.orElse(0)
        );
    }
}
```

## File: `src/shared/main/tv/codely/shared/domain/criteria/Filter.java`
```java
package tv.codely.shared.domain.criteria;

import java.util.HashMap;

public final class Filter {
    private final FilterField    field;
    private final FilterOperator operator;
    private final FilterValue    value;

    public Filter(FilterField field, FilterOperator operator, FilterValue value) {
        this.field    = field;
        this.operator = operator;
        this.value    = value;
    }

    public static Filter create(String field, String operator, String value) {
        return new Filter(
            new FilterField(field),
            FilterOperator.fromValue(operator.toUpperCase()),
            new FilterValue(value)
        );
    }

    public static Filter fromValues(HashMap<String, String> values) {
        return new Filter(
            new FilterField(values.get("field")),
            FilterOperator.fromValue(values.get("operator")),
            new FilterValue(values.get("value"))
        );
    }

    public FilterField field() {
        return field;
    }

    public FilterOperator operator() {
        return operator;
    }

    public FilterValue value() {
        return value;
    }

    public String serialize() {
        return String.format("%s.%s.%s", field.value(), operator.value(), value.value());
    }
}
```

## File: `src/shared/main/tv/codely/shared/domain/criteria/FilterField.java`
```java
package tv.codely.shared.domain.criteria;

import tv.codely.shared.domain.StringValueObject;

public final class FilterField extends StringValueObject {
    public FilterField(String value) {
        super(value);
    }
}
```

## File: `src/shared/main/tv/codely/shared/domain/criteria/FilterOperator.java`
```java
package tv.codely.shared.domain.criteria;

public enum FilterOperator {
    EQUAL("="),
    NOT_EQUAL("!="),
    GT(">"),
    LT("<"),
    CONTAINS("CONTAINS"),
    NOT_CONTAINS("NOT_CONTAINS");

    private final String operator;

    FilterOperator(String operator) {
        this.operator = operator;
    }

    public static FilterOperator fromValue(String value) {
        switch (value) {
            case "=": return FilterOperator.EQUAL;
            case "!=": return FilterOperator.NOT_EQUAL;
            case ">": return FilterOperator.GT;
            case "<": return FilterOperator.LT;
            case "CONTAINS": return FilterOperator.CONTAINS;
            case "NOT_CONTAINS": return FilterOperator.NOT_CONTAINS;
            default: return null;
        }
    }

    public boolean isPositive() {
        return this != NOT_EQUAL && this != NOT_CONTAINS;
    }

    public String value() {
        return operator;
    }
}
```

## File: `src/shared/main/tv/codely/shared/domain/criteria/FilterValue.java`
```java
package tv.codely.shared.domain.criteria;

import tv.codely.shared.domain.StringValueObject;

public final class FilterValue extends StringValueObject {
    public FilterValue(String value) {
        super(value);
    }
}
```

## File: `src/shared/main/tv/codely/shared/domain/criteria/Filters.java`
```java
package tv.codely.shared.domain.criteria;

import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.stream.Collectors;

public final class Filters {
    private final List<Filter> filters;

    public Filters(List<Filter> filters) {
        this.filters = filters;
    }

    public static Filters fromValues(List<HashMap<String, String>> filters) {
        return new Filters(filters.stream().map(Filter::fromValues).collect(Collectors.toList()));
    }

    public static Filters none() {
        return new Filters(Collections.emptyList());
    }

    public List<Filter> filters() {
        return filters;
    }

    public String serialize() {
        return filters.stream().map(Filter::serialize).collect(Collectors.joining("^"));
    }
}
```

## File: `src/shared/main/tv/codely/shared/domain/criteria/Order.java`
```java
package tv.codely.shared.domain.criteria;

import java.util.Optional;

public final class Order {
    private final OrderBy   orderBy;
    private final OrderType orderType;

    public Order(OrderBy orderBy, OrderType orderType) {
        this.orderBy   = orderBy;
        this.orderType = orderType;
    }

    public static Order fromValues(Optional<String> orderBy, Optional<String> orderType) {
        return orderBy.map(order -> new Order(new OrderBy(order), OrderType.valueOf(orderType.orElse("ASC"))))
                      .orElseGet(Order::none);
    }

    public static Order none() {
        return new Order(new OrderBy(""), OrderType.NONE);
    }

    public static Order desc(String orderBy) {
        return new Order(new OrderBy(orderBy), OrderType.DESC);
    }

    public static Order asc(String orderBy) {
        return new Order(new OrderBy(orderBy), OrderType.ASC);
    }

    public OrderBy orderBy() {
        return orderBy;
    }

    public OrderType orderType() {
        return orderType;
    }

    public boolean hasOrder() {
        return !orderType.isNone();
    }

    public String serialize() {
        return String.format("%s.%s", orderBy.value(), orderType.value());
    }
}
```

## File: `src/shared/main/tv/codely/shared/domain/criteria/OrderBy.java`
```java
package tv.codely.shared.domain.criteria;

import tv.codely.shared.domain.StringValueObject;

public final class OrderBy extends StringValueObject {
    public OrderBy(String value) {
        super(value);
    }
}
```

## File: `src/shared/main/tv/codely/shared/domain/criteria/OrderType.java`
```java
package tv.codely.shared.domain.criteria;

public enum OrderType {
    ASC("asc"),
    DESC("desc"),
    NONE("none");
    private final String type;

    OrderType(String type) {
        this.type = type;
    }

    public boolean isNone() {
        return this == NONE;
    }

    public boolean isAsc() {
        return this == ASC;
    }

    public String value() {
        return type;
    }
}

```

## File: `src/shared/main/tv/codely/shared/infrastructure/JavaUuidGenerator.java`
```java
package tv.codely.shared.infrastructure;

import tv.codely.shared.domain.Service;
import tv.codely.shared.domain.UuidGenerator;

import java.util.UUID;

@Service
public final class JavaUuidGenerator implements UuidGenerator {
    @Override
    public String generate() {
        return UUID.randomUUID().toString();
    }
}
```

## File: `src/shared/main/tv/codely/shared/infrastructure/bus/command/CommandHandlersInformation.java`
```java
package tv.codely.shared.infrastructure.bus.command;

import org.reflections.Reflections;
import tv.codely.shared.domain.Service;
import tv.codely.shared.domain.bus.command.Command;
import tv.codely.shared.domain.bus.command.CommandHandler;
import tv.codely.shared.domain.bus.command.CommandNotRegisteredError;

import java.lang.reflect.ParameterizedType;
import java.util.HashMap;
import java.util.Set;

@Service
public final class CommandHandlersInformation {
    HashMap<Class<? extends Command>, Class<? extends CommandHandler>> indexedCommandHandlers;

    public CommandHandlersInformation() {
        Reflections                          reflections = new Reflections("tv.codely");
        Set<Class<? extends CommandHandler>> classes     = reflections.getSubTypesOf(CommandHandler.class);

        indexedCommandHandlers = formatHandlers(classes);
    }

    public Class<? extends CommandHandler> search(Class<? extends Command> commandClass) throws CommandNotRegisteredError {
        Class<? extends CommandHandler> commandHandlerClass = indexedCommandHandlers.get(commandClass);

        if (null == commandHandlerClass) {
            throw new CommandNotRegisteredError(commandClass);
        }

        return commandHandlerClass;
    }

    private HashMap<Class<? extends Command>, Class<? extends CommandHandler>> formatHandlers(
        Set<Class<? extends CommandHandler>> commandHandlers
    ) {
        HashMap<Class<? extends Command>, Class<? extends CommandHandler>> handlers = new HashMap<>();

        for (Class<? extends CommandHandler> handler : commandHandlers) {
            ParameterizedType        paramType    = (ParameterizedType) handler.getGenericInterfaces()[0];
            Class<? extends Command> commandClass = (Class<? extends Command>) paramType.getActualTypeArguments()[0];

            handlers.put(commandClass, handler);
        }

        return handlers;
    }
}
```

## File: `src/shared/main/tv/codely/shared/infrastructure/bus/command/InMemoryCommandBus.java`
```java
package tv.codely.shared.infrastructure.bus.command;

import org.springframework.context.ApplicationContext;
import tv.codely.shared.domain.Service;
import tv.codely.shared.domain.bus.command.Command;
import tv.codely.shared.domain.bus.command.CommandBus;
import tv.codely.shared.domain.bus.command.CommandHandler;
import tv.codely.shared.domain.bus.command.CommandHandlerExecutionError;

@Service
public final class InMemoryCommandBus implements CommandBus {
    private final CommandHandlersInformation information;
    private final ApplicationContext         context;

    public InMemoryCommandBus(CommandHandlersInformation information, ApplicationContext context) {
        this.information = information;
        this.context     = context;
    }

    @Override
    public void dispatch(Command command) throws CommandHandlerExecutionError {
        try {
            Class<? extends CommandHandler> commandHandlerClass = information.search(command.getClass());

            CommandHandler handler = context.getBean(commandHandlerClass);

            handler.handle(command);
        } catch (Throwable error) {
            throw new CommandHandlerExecutionError(error);
        }
    }
}
```

## File: `src/shared/main/tv/codely/shared/infrastructure/bus/event/DomainEventJsonDeserializer.java`
```java
package tv.codely.shared.infrastructure.bus.event;

import tv.codely.shared.domain.Service;
import tv.codely.shared.domain.Utils;
import tv.codely.shared.domain.bus.event.DomainEvent;

import java.io.Serializable;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import java.util.HashMap;

@Service
public final class DomainEventJsonDeserializer {
    private final DomainEventsInformation information;

    public DomainEventJsonDeserializer(DomainEventsInformation information) {
        this.information = information;
    }

    public DomainEvent deserialize(String body) throws InvocationTargetException, IllegalAccessException, NoSuchMethodException, InstantiationException {
        HashMap<String, Serializable> eventData        = Utils.jsonDecode(body);
        HashMap<String, Serializable> data             = (HashMap<String, Serializable>) eventData.get("data");
        HashMap<String, Serializable> attributes       = (HashMap<String, Serializable>) data.get("attributes");
        Class<? extends DomainEvent>  domainEventClass = information.forName((String) data.get("type"));

        DomainEvent nullInstance = domainEventClass.getConstructor().newInstance();

        Method fromPrimitivesMethod = domainEventClass.getMethod(
            "fromPrimitives",
            String.class,
            HashMap.class,
            String.class,
            String.class
        );

        Object domainEvent = fromPrimitivesMethod.invoke(
            nullInstance,
            (String) attributes.get("id"),
            attributes,
            (String) data.get("id"),
            (String) data.get("occurred_on")
        );

        return (DomainEvent) domainEvent;
    }
}
```

## File: `src/shared/main/tv/codely/shared/infrastructure/bus/event/DomainEventJsonSerializer.java`
```java
package tv.codely.shared.infrastructure.bus.event;

import tv.codely.shared.domain.Utils;
import tv.codely.shared.domain.bus.event.DomainEvent;

import java.io.Serializable;
import java.util.HashMap;

public final class DomainEventJsonSerializer {
    public static String serialize(DomainEvent domainEvent) {
        HashMap<String, Serializable> attributes = domainEvent.toPrimitives();
        attributes.put("id", domainEvent.aggregateId());

        return Utils.jsonEncode(new HashMap<String, Serializable>() {{
            put("data", new HashMap<String, Serializable>() {{
                put("id", domainEvent.eventId());
                put("type", domainEvent.eventName());
                put("occurred_on", domainEvent.occurredOn());
                put("attributes", attributes);
            }});
            put("meta", new HashMap<String, Serializable>());
        }});
    }
}
```

## File: `src/shared/main/tv/codely/shared/infrastructure/bus/event/DomainEventSubscriberInformation.java`
```java
package tv.codely.shared.infrastructure.bus.event;

import tv.codely.shared.domain.Utils;
import tv.codely.shared.domain.bus.event.DomainEvent;

import java.util.List;

public final class DomainEventSubscriberInformation {
    private final Class<?>                           subscriberClass;
    private final List<Class<? extends DomainEvent>> subscribedEvents;

    public DomainEventSubscriberInformation(
        Class<?> subscriberClass,
        List<Class<? extends DomainEvent>> subscribedEvents
    ) {
        this.subscriberClass  = subscriberClass;
        this.subscribedEvents = subscribedEvents;
    }

    public Class<?> subscriberClass() {
        return subscriberClass;
    }

    public String contextName() {
        String[] nameParts = subscriberClass.getName().split("\\.");

        return nameParts[2];
    }

    public String moduleName() {
        String[] nameParts = subscriberClass.getName().split("\\.");

        return nameParts[3];
    }

    public String className() {
        String[] nameParts = subscriberClass.getName().split("\\.");

        return nameParts[nameParts.length - 1];
    }

    public List<Class<? extends DomainEvent>> subscribedEvents() {
        return subscribedEvents;
    }

    public String formatRabbitMqQueueName() {
        return String.format("codely.%s.%s.%s", contextName(), moduleName(), Utils.toSnake(className()));
    }
}
```

## File: `src/shared/main/tv/codely/shared/infrastructure/bus/event/DomainEventSubscribersInformation.java`
```java
package tv.codely.shared.infrastructure.bus.event;

import org.reflections.Reflections;
import tv.codely.shared.domain.Service;
import tv.codely.shared.domain.bus.event.DomainEventSubscriber;

import java.util.Arrays;
import java.util.Collection;
import java.util.HashMap;
import java.util.Set;

@Service
public final class DomainEventSubscribersInformation {
    HashMap<Class<?>, DomainEventSubscriberInformation> information;

    public DomainEventSubscribersInformation(HashMap<Class<?>, DomainEventSubscriberInformation> information) {
        this.information = information;
    }

    public DomainEventSubscribersInformation() {
        this(scanDomainEventSubscribers());
    }

    private static HashMap<Class<?>, DomainEventSubscriberInformation> scanDomainEventSubscribers() {
        Reflections   reflections = new Reflections("tv.codely");
        Set<Class<?>> subscribers = reflections.getTypesAnnotatedWith(DomainEventSubscriber.class);

        HashMap<Class<?>, DomainEventSubscriberInformation> subscribersInformation = new HashMap<>();

        for (Class<?> subscriberClass : subscribers) {
            DomainEventSubscriber annotation = subscriberClass.getAnnotation(DomainEventSubscriber.class);

            subscribersInformation.put(
                subscriberClass,
                new DomainEventSubscriberInformation(subscriberClass, Arrays.asList(annotation.value()))
            );
        }

        return subscribersInformation;
    }

    public Collection<DomainEventSubscriberInformation> all() {
        return information.values();
    }

    public String[] rabbitMqFormattedNames() {
        return information.values()
                          .stream()
                          .map(DomainEventSubscriberInformation::formatRabbitMqQueueName)
                          .distinct()
                          .toArray(String[]::new);
    }
}
```

## File: `src/shared/main/tv/codely/shared/infrastructure/bus/event/DomainEventsInformation.java`
```java
package tv.codely.shared.infrastructure.bus.event;

import org.reflections.Reflections;
import tv.codely.shared.domain.Service;
import tv.codely.shared.domain.bus.event.DomainEvent;

import java.lang.reflect.InvocationTargetException;
import java.util.HashMap;
import java.util.Map;
import java.util.Objects;
import java.util.Set;

@Service
public final class DomainEventsInformation {
    HashMap<String, Class<? extends DomainEvent>> indexedDomainEvents;

    public DomainEventsInformation() {
        Reflections                       reflections = new Reflections("tv.codely");
        Set<Class<? extends DomainEvent>> classes     = reflections.getSubTypesOf(DomainEvent.class);

        try {
            indexedDomainEvents = formatEvents(classes);
        } catch (NoSuchMethodException | IllegalAccessException | InstantiationException | InvocationTargetException e) {
            e.printStackTrace();
        }
    }

    public Class<? extends DomainEvent> forName(String name) {
        return indexedDomainEvents.get(name);
    }

    public String forClass(Class<? extends DomainEvent> domainEventClass) {
        return indexedDomainEvents.entrySet()
                                  .stream()
                                  .filter(entry -> Objects.equals(entry.getValue(), domainEventClass))
                                  .map(Map.Entry::getKey)
                                  .findFirst().orElse("");
    }

    private HashMap<String, Class<? extends DomainEvent>> formatEvents(
        Set<Class<? extends DomainEvent>> domainEvents
    ) throws NoSuchMethodException, IllegalAccessException, InvocationTargetException, InstantiationException {
        HashMap<String, Class<? extends DomainEvent>> events = new HashMap<>();

        for (Class<? extends DomainEvent> domainEvent : domainEvents) {
            DomainEvent nullInstance = domainEvent.getConstructor().newInstance();

            events.put((String) domainEvent.getMethod("eventName").invoke(nullInstance), domainEvent);
        }

        return events;
    }
}
```

## File: `src/shared/main/tv/codely/shared/infrastructure/bus/event/mysql/MySqlDomainEventsConsumer.java`
```java
package tv.codely.shared.infrastructure.bus.event.mysql;

import jakarta.transaction.Transactional;
import org.hibernate.SessionFactory;
import org.hibernate.query.NativeQuery;
import org.springframework.beans.factory.annotation.Qualifier;
import tv.codely.shared.domain.Utils;
import tv.codely.shared.domain.bus.event.DomainEvent;
import tv.codely.shared.domain.bus.event.EventBus;
import tv.codely.shared.infrastructure.bus.event.DomainEventsInformation;

import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import java.sql.Timestamp;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;

public class MySqlDomainEventsConsumer {
	private final SessionFactory sessionFactory;
	private final DomainEventsInformation domainEventsInformation;
	private final EventBus bus;
	private final Integer CHUNKS = 200;
	private Boolean shouldStop = false;

	public MySqlDomainEventsConsumer(
		@Qualifier("mooc-session_factory") SessionFactory sessionFactory,
		DomainEventsInformation domainEventsInformation,
		EventBus bus
	) {
		this.sessionFactory = sessionFactory;
		this.domainEventsInformation = domainEventsInformation;
		this.bus = bus;
	}

	@Transactional
	public void consume() {
		while (!shouldStop) {
			NativeQuery query = sessionFactory.getCurrentSession().createNativeQuery(
				"SELECT * FROM domain_events ORDER BY occurred_on ASC LIMIT :chunk"
			);

			query.setParameter("chunk", CHUNKS);

			List<Object[]> events = query.list();

			try {
				for (Object[] event : events) {
					executeSubscribers(
						(String) event[0],
						(String) event[1],
						(String) event[2],
						(String) event[3],
						(Timestamp) event[4]
					);
				}
			} catch (NoSuchMethodException | IllegalAccessException | InvocationTargetException |
					 InstantiationException e) {
				e.printStackTrace();
			}

			sessionFactory.getCurrentSession().clear();
		}
	}

	public void stop() {
		shouldStop = true;
	}

	private void executeSubscribers(
		String id, String aggregateId, String eventName, String body, Timestamp occurredOn
	) throws NoSuchMethodException, IllegalAccessException, InvocationTargetException, InstantiationException {

		Class<? extends DomainEvent> domainEventClass = domainEventsInformation.forName(eventName);

		DomainEvent nullInstance = domainEventClass.getConstructor().newInstance();

		Method fromPrimitivesMethod = domainEventClass.getMethod(
			"fromPrimitives",
			String.class,
			HashMap.class,
			String.class,
			String.class
		);

		Object domainEvent = fromPrimitivesMethod.invoke(
			nullInstance,
			aggregateId,
			Utils.jsonDecode(body),
			id,
			Utils.dateToString(occurredOn)
		);

		bus.publish(Collections.singletonList((DomainEvent) domainEvent));
	}
}
```

## File: `src/shared/main/tv/codely/shared/infrastructure/bus/event/mysql/MySqlEventBus.java`
```java
package tv.codely.shared.infrastructure.bus.event.mysql;

import org.hibernate.SessionFactory;
import org.hibernate.query.NativeQuery;
import tv.codely.shared.domain.Utils;
import tv.codely.shared.domain.bus.event.DomainEvent;
import tv.codely.shared.domain.bus.event.EventBus;

import java.io.Serializable;
import java.util.HashMap;
import java.util.List;

public final class MySqlEventBus implements EventBus {
    private final SessionFactory sessionFactory;

    public MySqlEventBus(SessionFactory sessionFactory) {
        this.sessionFactory = sessionFactory;
    }

    @Override
    public void publish(List<DomainEvent> events) {
        events.forEach(this::publish);
    }

    private void publish(DomainEvent domainEvent) {
        String                        id          = domainEvent.eventId();
        String                        aggregateId = domainEvent.aggregateId();
        String                        name        = domainEvent.eventName();
        HashMap<String, Serializable> body        = domainEvent.toPrimitives();
        String                        occurredOn  = domainEvent.occurredOn();

        NativeQuery query = sessionFactory.getCurrentSession().createNativeQuery(
            "INSERT INTO domain_events (id,  aggregate_id, name,  body,  occurred_on) " +
            "VALUES (:id, :aggregateId, :name, :body, :occurredOn);"
        );

        query.setParameter("id", id)
             .setParameter("aggregateId", aggregateId)
             .setParameter("name", name)
             .setParameter("body", Utils.jsonEncode(body))
             .setParameter("occurredOn", occurredOn);

        query.executeUpdate();
    }
}
```

## File: `src/shared/main/tv/codely/shared/infrastructure/bus/event/rabbitmq/RabbitMqDomainEventsConsumer.java`
```java
package tv.codely.shared.infrastructure.bus.event.rabbitmq;

import org.springframework.amqp.core.Message;
import org.springframework.amqp.core.MessageBuilder;
import org.springframework.amqp.core.MessagePropertiesBuilder;
import org.springframework.amqp.rabbit.annotation.RabbitListener;
import org.springframework.amqp.rabbit.listener.AbstractMessageListenerContainer;
import org.springframework.amqp.rabbit.listener.RabbitListenerEndpointRegistry;
import org.springframework.context.ApplicationContext;
import tv.codely.shared.domain.Service;
import tv.codely.shared.domain.Utils;
import tv.codely.shared.domain.bus.event.DomainEvent;
import tv.codely.shared.infrastructure.bus.event.DomainEventJsonDeserializer;
import tv.codely.shared.infrastructure.bus.event.DomainEventSubscribersInformation;

import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import java.util.HashMap;
import java.util.Map;

@Service
public final class RabbitMqDomainEventsConsumer {
    private final String                      CONSUMER_NAME          = "domain_events_consumer";
    private final int                         MAX_RETRIES            = 2;
    private final DomainEventJsonDeserializer deserializer;
    private final ApplicationContext          context;
    private final RabbitMqPublisher           publisher;
    private final HashMap<String, Object>     domainEventSubscribers = new HashMap<>();
    RabbitListenerEndpointRegistry registry;
    private DomainEventSubscribersInformation information;

    public RabbitMqDomainEventsConsumer(
        RabbitListenerEndpointRegistry registry,
        DomainEventSubscribersInformation information,
        DomainEventJsonDeserializer deserializer,
        ApplicationContext context,
        RabbitMqPublisher publisher
    ) {
        this.registry     = registry;
        this.information  = information;
        this.deserializer = deserializer;
        this.context      = context;
        this.publisher    = publisher;
    }

    public void consume() {
        AbstractMessageListenerContainer container = (AbstractMessageListenerContainer) registry.getListenerContainer(
            CONSUMER_NAME
        );

        container.addQueueNames(information.rabbitMqFormattedNames());

        container.start();
    }

    @RabbitListener(id = CONSUMER_NAME, autoStartup = "false")
    public void consumer(Message message) throws Exception {
        String      serializedMessage = new String(message.getBody());
        DomainEvent domainEvent       = deserializer.deserialize(serializedMessage);

        String queue = message.getMessageProperties().getConsumerQueue();

        Object subscriber = domainEventSubscribers.containsKey(queue)
            ? domainEventSubscribers.get(queue)
            : subscriberFor(queue);

        Method subscriberOnMethod = subscriber.getClass().getMethod("on", domainEvent.getClass());

        try {
            subscriberOnMethod.invoke(subscriber, domainEvent);
        } catch (IllegalAccessException | IllegalArgumentException | InvocationTargetException error) {
            throw new Exception(String.format(
                "The subscriber <%s> should implement a method `on` listening the domain event <%s>",
                queue,
                domainEvent.eventName()
            ));
        } catch (Exception error) {
            handleConsumptionError(message, queue);
        }
    }

    public void withSubscribersInformation(DomainEventSubscribersInformation information) {
        this.information = information;
    }

    private void handleConsumptionError(Message message, String queue) {
        if (hasBeenRedeliveredTooMuch(message)) {
            sendToDeadLetter(message, queue);
        } else {
            sendToRetry(message, queue);
        }
    }

    private void sendToRetry(Message message, String queue) {
        sendMessageTo(RabbitMqExchangeNameFormatter.retry("domain_events"), message, queue);
    }

    private void sendToDeadLetter(Message message, String queue) {
        sendMessageTo(RabbitMqExchangeNameFormatter.deadLetter("domain_events"), message, queue);
    }

    private void sendMessageTo(String exchange, Message message, String queue) {
        Map<String, Object> headers = message.getMessageProperties().getHeaders();

        headers.put("redelivery_count", (int) headers.getOrDefault("redelivery_count", 0) + 1);

        MessageBuilder.fromMessage(message).andProperties(
            MessagePropertiesBuilder.newInstance()
                                    .setContentEncoding("utf-8")
                                    .setContentType("application/json")
                                    .copyHeaders(headers)
                                    .build());

        publisher.publish(message, exchange, queue);
    }

    private boolean hasBeenRedeliveredTooMuch(Message message) {
        return (int) message.getMessageProperties().getHeaders().getOrDefault("redelivery_count", 0) >= MAX_RETRIES;
    }

    private Object subscriberFor(String queue) throws Exception {
        String[] queueParts     = queue.split("\\.");
        String   subscriberName = Utils.toCamelFirstLower(queueParts[queueParts.length - 1]);

        try {
            Object subscriber = context.getBean(subscriberName);
            domainEventSubscribers.put(queue, subscriber);

            return subscriber;
        } catch (Exception e) {
            throw new Exception(String.format("There are not registered subscribers for <%s> queue", queue));
        }
    }
}
```

## File: `src/shared/main/tv/codely/shared/infrastructure/bus/event/rabbitmq/RabbitMqEventBus.java`
```java
package tv.codely.shared.infrastructure.bus.event.rabbitmq;

import org.springframework.amqp.AmqpException;
import tv.codely.shared.domain.bus.event.DomainEvent;
import tv.codely.shared.domain.bus.event.EventBus;
import tv.codely.shared.infrastructure.bus.event.mysql.MySqlEventBus;

import java.util.Collections;
import java.util.List;

public class RabbitMqEventBus implements EventBus {
    private final RabbitMqPublisher publisher;
    private final MySqlEventBus     failoverPublisher;
    private final String            exchangeName;

    public RabbitMqEventBus(RabbitMqPublisher publisher, MySqlEventBus failoverPublisher) {
        this.publisher         = publisher;
        this.failoverPublisher = failoverPublisher;
        this.exchangeName      = "domain_events";
    }

    @Override
    public void publish(List<DomainEvent> events) {
        events.forEach(this::publish);
    }

    private void publish(DomainEvent domainEvent) {
        try {
            this.publisher.publish(domainEvent, exchangeName);
        } catch (AmqpException error) {
            failoverPublisher.publish(Collections.singletonList(domainEvent));
        }
    }
}
```

## File: `src/shared/main/tv/codely/shared/infrastructure/bus/event/rabbitmq/RabbitMqEventBusConfiguration.java`
```java
package tv.codely.shared.infrastructure.bus.event.rabbitmq;

import org.springframework.amqp.core.*;
import org.springframework.amqp.rabbit.connection.CachingConnectionFactory;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import tv.codely.shared.infrastructure.bus.event.DomainEventSubscribersInformation;
import tv.codely.shared.infrastructure.bus.event.DomainEventsInformation;
import tv.codely.shared.infrastructure.config.Parameter;
import tv.codely.shared.infrastructure.config.ParameterNotExist;

import java.util.ArrayList;
import java.util.Collection;
import java.util.HashMap;
import java.util.List;
import java.util.stream.Collectors;

@Configuration
public class RabbitMqEventBusConfiguration {
    private final DomainEventSubscribersInformation domainEventSubscribersInformation;
    private final DomainEventsInformation           domainEventsInformation;
    private final Parameter                         config;
    private final String                            exchangeName;

    public RabbitMqEventBusConfiguration(
        DomainEventSubscribersInformation domainEventSubscribersInformation,
        DomainEventsInformation domainEventsInformation,
        Parameter config
    ) throws ParameterNotExist {
        this.domainEventSubscribersInformation = domainEventSubscribersInformation;
        this.domainEventsInformation           = domainEventsInformation;
        this.config                            = config;
        this.exchangeName                      = config.get("RABBITMQ_EXCHANGE");
    }

    @Bean
    public CachingConnectionFactory connection() throws ParameterNotExist {
        CachingConnectionFactory factory = new CachingConnectionFactory();

        factory.setHost(config.get("RABBITMQ_HOST"));
        factory.setPort(config.getInt("RABBITMQ_PORT"));
        factory.setUsername(config.get("RABBITMQ_LOGIN"));
        factory.setPassword(config.get("RABBITMQ_PASSWORD"));

        return factory;
    }

    @Bean
    public Declarables declaration() {
        String retryExchangeName      = RabbitMqExchangeNameFormatter.retry(exchangeName);
        String deadLetterExchangeName = RabbitMqExchangeNameFormatter.deadLetter(exchangeName);

        TopicExchange    domainEventsExchange           = new TopicExchange(exchangeName, true, false);
        TopicExchange    retryDomainEventsExchange      = new TopicExchange(retryExchangeName, true, false);
        TopicExchange    deadLetterDomainEventsExchange = new TopicExchange(deadLetterExchangeName, true, false);
        List<Declarable> declarables                    = new ArrayList<>();
        declarables.add(domainEventsExchange);
        declarables.add(retryDomainEventsExchange);
        declarables.add(deadLetterDomainEventsExchange);

        Collection<Declarable> queuesAndBindings = declareQueuesAndBindings(
            domainEventsExchange,
            retryDomainEventsExchange,
            deadLetterDomainEventsExchange
        ).stream().flatMap(Collection::stream).collect(Collectors.toList());

        declarables.addAll(queuesAndBindings);

        return new Declarables(declarables);
    }

    private Collection<Collection<Declarable>> declareQueuesAndBindings(
        TopicExchange domainEventsExchange,
        TopicExchange retryDomainEventsExchange,
        TopicExchange deadLetterDomainEventsExchange
    ) {
        return domainEventSubscribersInformation.all().stream().map(information -> {
            String queueName           = RabbitMqQueueNameFormatter.format(information);
            String retryQueueName      = RabbitMqQueueNameFormatter.formatRetry(information);
            String deadLetterQueueName = RabbitMqQueueNameFormatter.formatDeadLetter(information);

            Queue queue = QueueBuilder.durable(queueName).build();
            Queue retryQueue = QueueBuilder.durable(retryQueueName).withArguments(
                retryQueueArguments(domainEventsExchange, queueName)
            ).build();
            Queue deadLetterQueue = QueueBuilder.durable(deadLetterQueueName).build();

            Binding fromExchangeSameQueueBinding = BindingBuilder
                .bind(queue)
                .to(domainEventsExchange)
                .with(queueName);

            Binding fromRetryExchangeSameQueueBinding = BindingBuilder
                .bind(retryQueue)
                .to(retryDomainEventsExchange)
                .with(queueName);

            Binding fromDeadLetterExchangeSameQueueBinding = BindingBuilder
                .bind(deadLetterQueue)
                .to(deadLetterDomainEventsExchange)
                .with(queueName);

            List<Binding> fromExchangeDomainEventsBindings = information.subscribedEvents().stream().map(
                domainEventClass -> {
                    String eventName = domainEventsInformation.forClass(domainEventClass);
                    return BindingBuilder
                        .bind(queue)
                        .to(domainEventsExchange)
                        .with(eventName);
                }).collect(Collectors.toList());

            List<Declarable> queuesAndBindings = new ArrayList<>();
            queuesAndBindings.add(queue);
            queuesAndBindings.add(fromExchangeSameQueueBinding);
            queuesAndBindings.addAll(fromExchangeDomainEventsBindings);

            queuesAndBindings.add(retryQueue);
            queuesAndBindings.add(fromRetryExchangeSameQueueBinding);

            queuesAndBindings.add(deadLetterQueue);
            queuesAndBindings.add(fromDeadLetterExchangeSameQueueBinding);

            return queuesAndBindings;
        }).collect(Collectors.toList());
    }

    private HashMap<String, Object> retryQueueArguments(TopicExchange exchange, String routingKey) {
        return new HashMap<String, Object>() {{
            put("x-dead-letter-exchange", exchange.getName());
            put("x-dead-letter-routing-key", routingKey);
            put("x-message-ttl", 1000);
        }};
    }
}
```

## File: `src/shared/main/tv/codely/shared/infrastructure/bus/event/rabbitmq/RabbitMqExchangeNameFormatter.java`
```java
package tv.codely.shared.infrastructure.bus.event.rabbitmq;

public final class RabbitMqExchangeNameFormatter {
    public static String retry(String exchangeName) {
        return String.format("retry-%s", exchangeName);
    }

    public static String deadLetter(String exchangeName) {
        return String.format("dead_letter-%s", exchangeName);
    }
}
```

## File: `src/shared/main/tv/codely/shared/infrastructure/bus/event/rabbitmq/RabbitMqPublisher.java`
```java
package tv.codely.shared.infrastructure.bus.event.rabbitmq;

import org.springframework.amqp.AmqpException;
import org.springframework.amqp.core.Message;
import org.springframework.amqp.core.MessagePropertiesBuilder;
import org.springframework.amqp.rabbit.core.RabbitTemplate;
import tv.codely.shared.domain.Service;
import tv.codely.shared.domain.bus.event.DomainEvent;
import tv.codely.shared.infrastructure.bus.event.DomainEventJsonSerializer;

@Service
public final class RabbitMqPublisher {
    private final RabbitTemplate rabbitTemplate;

    public RabbitMqPublisher(RabbitTemplate rabbitTemplate) {
        this.rabbitTemplate = rabbitTemplate;
    }

    public void publish(DomainEvent domainEvent, String exchangeName) throws AmqpException {
        String serializedDomainEvent = DomainEventJsonSerializer.serialize(domainEvent);

        Message message = new Message(
            serializedDomainEvent.getBytes(),
            MessagePropertiesBuilder.newInstance()
                                    .setContentEncoding("utf-8")
                                    .setContentType("application/json")
                                    .build()
        );

        rabbitTemplate.send(exchangeName, domainEvent.eventName(), message);
    }

    public void publish(Message domainEvent, String exchangeName, String routingKey) throws AmqpException {
        rabbitTemplate.send(exchangeName, routingKey, domainEvent);
    }
}
```

## File: `src/shared/main/tv/codely/shared/infrastructure/bus/event/rabbitmq/RabbitMqQueueNameFormatter.java`
```java
package tv.codely.shared.infrastructure.bus.event.rabbitmq;

import tv.codely.shared.infrastructure.bus.event.DomainEventSubscriberInformation;

public final class RabbitMqQueueNameFormatter {
    public static String format(DomainEventSubscriberInformation information) {
        return information.formatRabbitMqQueueName();
    }

    public static String formatRetry(DomainEventSubscriberInformation information) {
        return String.format("retry.%s", format(information));
    }

    public static String formatDeadLetter(DomainEventSubscriberInformation information) {
        return String.format("dead_letter.%s", format(information));
    }
}
```

## File: `src/shared/main/tv/codely/shared/infrastructure/bus/event/spring/SpringApplicationEventBus.java`
```java
package tv.codely.shared.infrastructure.bus.event.spring;

import org.springframework.context.ApplicationEventPublisher;
import org.springframework.context.annotation.Primary;
import tv.codely.shared.domain.Service;
import tv.codely.shared.domain.bus.event.DomainEvent;
import tv.codely.shared.domain.bus.event.EventBus;

import java.util.List;

@Primary
@Service
public class SpringApplicationEventBus implements EventBus {
    private final ApplicationEventPublisher publisher;

    public SpringApplicationEventBus(ApplicationEventPublisher publisher) {
        this.publisher = publisher;
    }

    @Override
    public void publish(final List<DomainEvent> events) {
        events.forEach(this::publish);
    }

    private void publish(final DomainEvent event) {
        this.publisher.publishEvent(event);
    }
}
```

## File: `src/shared/main/tv/codely/shared/infrastructure/bus/query/InMemoryQueryBus.java`
```java
package tv.codely.shared.infrastructure.bus.query;

import org.springframework.context.ApplicationContext;
import tv.codely.shared.domain.Service;
import tv.codely.shared.domain.bus.query.*;

@Service
public final class InMemoryQueryBus implements QueryBus {
    private final QueryHandlersInformation information;
    private final ApplicationContext       context;

    public InMemoryQueryBus(QueryHandlersInformation information, ApplicationContext context) {
        this.information = information;
        this.context     = context;
    }

    @Override
    public Response ask(Query query) throws QueryHandlerExecutionError {
        try {
            Class<? extends QueryHandler> queryHandlerClass = information.search(query.getClass());

            QueryHandler handler = context.getBean(queryHandlerClass);

            return handler.handle(query);
        } catch (Throwable error) {
            throw new QueryHandlerExecutionError(error);
        }
    }
}
```

## File: `src/shared/main/tv/codely/shared/infrastructure/bus/query/QueryHandlersInformation.java`
```java
package tv.codely.shared.infrastructure.bus.query;

import org.reflections.Reflections;
import tv.codely.shared.domain.Service;
import tv.codely.shared.domain.bus.query.Query;
import tv.codely.shared.domain.bus.query.QueryHandler;
import tv.codely.shared.domain.bus.query.QueryNotRegisteredError;

import java.lang.reflect.ParameterizedType;
import java.util.HashMap;
import java.util.Set;

@Service
public final class QueryHandlersInformation {
    HashMap<Class<? extends Query>, Class<? extends QueryHandler>> indexedQueryHandlers;

    public QueryHandlersInformation() {
        Reflections                        reflections = new Reflections("tv.codely");
        Set<Class<? extends QueryHandler>> classes     = reflections.getSubTypesOf(QueryHandler.class);

        indexedQueryHandlers = formatHandlers(classes);
    }

    public Class<? extends QueryHandler> search(Class<? extends Query> queryClass) throws QueryNotRegisteredError {
        Class<? extends QueryHandler> queryHandlerClass = indexedQueryHandlers.get(queryClass);

        if (null == queryHandlerClass) {
            throw new QueryNotRegisteredError(queryClass);
        }

        return queryHandlerClass;
    }

    private HashMap<Class<? extends Query>, Class<? extends QueryHandler>> formatHandlers(
        Set<Class<? extends QueryHandler>> queryHandlers
    ) {
        HashMap<Class<? extends Query>, Class<? extends QueryHandler>> handlers = new HashMap<>();

        for (Class<? extends QueryHandler> handler : queryHandlers) {
            ParameterizedType      paramType  = (ParameterizedType) handler.getGenericInterfaces()[0];
            Class<? extends Query> queryClass = (Class<? extends Query>) paramType.getActualTypeArguments()[0];

            handlers.put(queryClass, handler);
        }

        return handlers;
    }
}
```

## File: `src/shared/main/tv/codely/shared/infrastructure/cli/ConsoleCommand.java`
```java
package tv.codely.shared.infrastructure.cli;

import tv.codely.shared.domain.Service;

@Service
public abstract class ConsoleCommand {
    private static final String ANSI_RESET = "\u001B[0m";
    private static final String ANSI_RED   = "\u001B[31m";
    private static final String ANSI_CYAN  = "\u001B[36m";
    private static final String ANSI_GREEN = "\u001B[32m";

    abstract public void execute(String[] args);

    protected void log(String text) {
        System.out.println(String.format("%s%s%s", ANSI_GREEN, text, ANSI_RESET));
    }

    protected void info(String text) {
        System.out.println(String.format("%s%s%s", ANSI_CYAN, text, ANSI_RESET));
    }

    protected void error(String text) {
        System.out.println(String.format("%s%s%s", ANSI_RED, text, ANSI_RESET));
    }
}
```

## File: `src/shared/main/tv/codely/shared/infrastructure/config/EnvironmentConfig.java`
```java
package tv.codely.shared.infrastructure.config;

import io.github.cdimascio.dotenv.Dotenv;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.core.io.Resource;
import org.springframework.core.io.ResourceLoader;

@Configuration
public class EnvironmentConfig {
    ResourceLoader resourceLoader;

    public EnvironmentConfig(ResourceLoader resourceLoader) {
        this.resourceLoader = resourceLoader;
    }

    @Bean
    public Dotenv dotenv() {
        Resource resource = resourceLoader.getResource("classpath:/.env.local");

        return Dotenv
            .configure()
            .directory("/")
            .filename(resource.exists() ? ".env.local" : ".env")
            .load();
    }
}
```

## File: `src/shared/main/tv/codely/shared/infrastructure/config/Parameter.java`
```java
package tv.codely.shared.infrastructure.config;

import io.github.cdimascio.dotenv.Dotenv;
import tv.codely.shared.domain.Service;

@Service
public final class Parameter {
    private final Dotenv dotenv;

    public Parameter(Dotenv dotenv) {
        this.dotenv = dotenv;
    }

    public String get(String key) throws ParameterNotExist {
        String value = dotenv.get(key);

        if (null == value) {
            throw new ParameterNotExist(key);
        }

        return value;
    }

    public Integer getInt(String key) throws ParameterNotExist {
        String value = get(key);

        return Integer.parseInt(value);
    }
}
```

## File: `src/shared/main/tv/codely/shared/infrastructure/config/ParameterNotExist.java`
```java
package tv.codely.shared.infrastructure.config;

public final class ParameterNotExist extends Throwable {
    public ParameterNotExist(String key) {
        super(String.format("The parameter <%s> does not exist in the environment file", key));
    }
}
```

## File: `src/shared/main/tv/codely/shared/infrastructure/elasticsearch/ElasticsearchClient.java`
```java
package tv.codely.shared.infrastructure.elasticsearch;

import org.elasticsearch.action.admin.indices.delete.DeleteIndexRequest;
import org.elasticsearch.action.index.IndexRequest;
import org.elasticsearch.client.RequestOptions;
import org.elasticsearch.client.RestClient;
import org.elasticsearch.client.RestHighLevelClient;

import java.io.IOException;
import java.io.Serializable;
import java.util.HashMap;

public final class ElasticsearchClient {
    private final RestHighLevelClient highLevelClient;
    private final RestClient          lowLevelClient;
    private final String              indexPrefix;

    public ElasticsearchClient(RestHighLevelClient highLevelClient, RestClient lowLevelClient, String indexPrefix) {
        this.highLevelClient = highLevelClient;
        this.lowLevelClient  = lowLevelClient;
        this.indexPrefix     = indexPrefix;
    }

    public RestHighLevelClient highLevelClient() {
        return highLevelClient;
    }

    public RestClient lowLevelClient() {
        return lowLevelClient;
    }

    public String indexPrefix() {
        return indexPrefix;
    }

    public void persist(String moduleName, String id, HashMap<String, Serializable> plainBody) throws IOException {
        IndexRequest request = new IndexRequest(indexFor(moduleName), moduleName, id).source(plainBody);

        highLevelClient().index(request, RequestOptions.DEFAULT);
    }

    public String indexFor(String moduleName) {
        return String.format("%s_%s", indexPrefix(), moduleName);
    }

    public void delete(String index) throws IOException {
        highLevelClient.indices().delete(new DeleteIndexRequest(index), RequestOptions.DEFAULT);
    }
}
```

## File: `src/shared/main/tv/codely/shared/infrastructure/elasticsearch/ElasticsearchCriteriaConverter.java`
```java
package tv.codely.shared.infrastructure.elasticsearch;

import org.elasticsearch.index.query.BoolQueryBuilder;
import org.elasticsearch.index.query.QueryBuilder;
import org.elasticsearch.index.query.QueryBuilders;
import org.elasticsearch.search.builder.SearchSourceBuilder;
import org.elasticsearch.search.sort.SortOrder;
import tv.codely.shared.domain.criteria.Criteria;
import tv.codely.shared.domain.criteria.Filter;
import tv.codely.shared.domain.criteria.FilterOperator;
import tv.codely.shared.domain.criteria.Filters;

import java.util.HashMap;
import java.util.function.Function;

public final class ElasticsearchCriteriaConverter {
    private final HashMap<FilterOperator, Function<Filter, QueryBuilder>> queryTransformers = new HashMap<FilterOperator, Function<Filter, QueryBuilder>>() {{
        put(FilterOperator.EQUAL, ElasticsearchCriteriaConverter.this::termQuery);
        put(FilterOperator.NOT_EQUAL, ElasticsearchCriteriaConverter.this::termQuery);
        put(FilterOperator.GT, ElasticsearchCriteriaConverter.this::greaterThanQueryTransformer);
        put(FilterOperator.LT, ElasticsearchCriteriaConverter.this::lowerThanQueryTransformer);
        put(FilterOperator.CONTAINS, ElasticsearchCriteriaConverter.this::wildcardTransformer);
        put(FilterOperator.NOT_CONTAINS, ElasticsearchCriteriaConverter.this::wildcardTransformer);
    }};

    public SearchSourceBuilder convert(Criteria criteria) {
        SearchSourceBuilder sourceBuilder = new SearchSourceBuilder();

        sourceBuilder.from(criteria.offset().orElse(0));
        sourceBuilder.size(criteria.limit().orElse(1000));

        if (criteria.order().hasOrder()) {
            sourceBuilder.sort(
                criteria.order().orderBy().value(),
                SortOrder.fromString(criteria.order().orderType().value())
            );
        }

        if (criteria.hasFilters()) {
            QueryBuilder queryBuilder = generateQueryBuilder(criteria.filters());

            sourceBuilder.query(queryBuilder);
        }

        return sourceBuilder;
    }

    private QueryBuilder generateQueryBuilder(Filters filters) {
        BoolQueryBuilder boolQueryBuilder = new BoolQueryBuilder();

        for (Filter filter : filters.filters()) {
            QueryBuilder query = queryForFilter(filter);

            if (isPositiveOperator(filter.operator())) {
                boolQueryBuilder.must(query);
            } else {
                boolQueryBuilder.mustNot(query);
            }
        }

        return boolQueryBuilder;
    }

    private boolean isPositiveOperator(FilterOperator operator) {
        return operator.isPositive();
    }

    private QueryBuilder queryForFilter(Filter filter) {
        Function<Filter, QueryBuilder> transformer = queryTransformers.get(filter.operator());

        return transformer.apply(filter);
    }

    private QueryBuilder termQuery(Filter filter) {
        return QueryBuilders.termQuery(filter.field().value(), filter.value().value().toLowerCase());
    }

    private QueryBuilder greaterThanQueryTransformer(Filter filter) {
        return QueryBuilders.rangeQuery(filter.field().value()).gt(filter.value().value().toLowerCase());
    }

    private QueryBuilder lowerThanQueryTransformer(Filter filter) {
        return QueryBuilders.rangeQuery(filter.field().value()).lt(filter.value().value().toLowerCase());
    }

    private QueryBuilder wildcardTransformer(Filter filter) {
        return QueryBuilders.wildcardQuery(
            filter.field().value(),
            String.format("*%s*", filter.value().value().toLowerCase())
        );
    }
}
```

## File: `src/shared/main/tv/codely/shared/infrastructure/elasticsearch/ElasticsearchRepository.java`
```java
package tv.codely.shared.infrastructure.elasticsearch;

import org.elasticsearch.action.search.SearchRequest;
import org.elasticsearch.action.search.SearchResponse;
import org.elasticsearch.client.RequestOptions;
import org.elasticsearch.search.builder.SearchSourceBuilder;
import tv.codely.shared.domain.criteria.Criteria;

import java.io.IOException;
import java.io.Serializable;
import java.util.*;
import java.util.function.Function;
import java.util.stream.Collectors;

public abstract class ElasticsearchRepository<T> {
    private final ElasticsearchClient            client;
    private final ElasticsearchCriteriaConverter criteriaConverter;

    public ElasticsearchRepository(ElasticsearchClient client) {
        this.client            = client;
        this.criteriaConverter = new ElasticsearchCriteriaConverter();
    }

    abstract protected String moduleName();

    protected List<T> searchAllInElastic(Function<Map<String, Object>, T> unserializer) {
        return searchAllInElastic(unserializer, new SearchSourceBuilder());
    }

    protected List<T> searchAllInElastic(
        Function<Map<String, Object>, T> unserializer,
        SearchSourceBuilder sourceBuilder
    ) {
        SearchRequest request = new SearchRequest(client.indexFor(moduleName())).source(sourceBuilder);
        try {
            SearchResponse response = client.highLevelClient().search(request, RequestOptions.DEFAULT);

            return Arrays.stream(response.getHits().getHits())
                         .map(hit -> unserializer.apply(hit.getSourceAsMap()))
                         .collect(Collectors.toList());
        } catch (IOException e) {
            e.printStackTrace();
        }

        return Collections.emptyList();
    }

    protected List<T> searchByCriteria(Criteria criteria, Function<Map<String, Object>, T> unserializer) {
        return searchAllInElastic(unserializer, criteriaConverter.convert(criteria));
    }

    protected void persist(String id, HashMap<String, Serializable> plainBody) {
        try {
            client.persist(moduleName(), id, plainBody);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

## File: `src/shared/main/tv/codely/shared/infrastructure/hibernate/HibernateConfigurationFactory.java`
```java
package tv.codely.shared.infrastructure.hibernate;

import org.apache.tomcat.dbcp.dbcp2.BasicDataSource;
import org.hibernate.cfg.AvailableSettings;
import org.springframework.core.io.FileSystemResource;
import org.springframework.core.io.Resource;
import org.springframework.core.io.support.ResourcePatternResolver;
import org.springframework.orm.hibernate5.HibernateTransactionManager;
import org.springframework.orm.hibernate5.LocalSessionFactoryBean;
import org.springframework.transaction.PlatformTransactionManager;
import tv.codely.shared.domain.Service;

import javax.sql.DataSource;
import java.io.File;
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.util.*;
import java.util.stream.Collectors;

@Service
public final class HibernateConfigurationFactory {
    private final ResourcePatternResolver resourceResolver;

    public HibernateConfigurationFactory(ResourcePatternResolver resourceResolver) {
        this.resourceResolver = resourceResolver;
    }

    public PlatformTransactionManager hibernateTransactionManager(LocalSessionFactoryBean sessionFactory) {
        HibernateTransactionManager transactionManager = new HibernateTransactionManager();
        transactionManager.setSessionFactory(sessionFactory.getObject());

        return transactionManager;
    }

    public LocalSessionFactoryBean sessionFactory(String contextName, DataSource dataSource) {
        LocalSessionFactoryBean sessionFactory = new LocalSessionFactoryBean();
        sessionFactory.setDataSource(dataSource);
        sessionFactory.setHibernateProperties(hibernateProperties());

        List<Resource> mappingFiles = searchMappingFiles(contextName);

        sessionFactory.setMappingLocations(mappingFiles.toArray(new Resource[mappingFiles.size()]));

        return sessionFactory;
    }

    public DataSource dataSource(
        String host,
        Integer port,
        String databaseName,
        String username,
        String password
    ) throws IOException {
        BasicDataSource dataSource = new BasicDataSource();
        dataSource.setDriverClassName("com.mysql.cj.jdbc.Driver");
        dataSource.setUrl(
            String.format(
                "jdbc:mysql://%s:%s/%s?useUnicode=true&useJDBCCompliantTimezoneShift=true&useLegacyDatetimeCode=false&serverTimezone=UTC",
                host,
                port,
                databaseName
            )
        );
        dataSource.setUsername(username);
        dataSource.setPassword(password);

        Resource mysqlResource = resourceResolver.getResource(String.format(
            "classpath:database/%s.sql",
            databaseName
        ));
        String mysqlSentences = new Scanner(mysqlResource.getInputStream(), StandardCharsets.UTF_8).useDelimiter("\\A").next();

        dataSource.setConnectionInitSqls(new ArrayList<>(Arrays.asList(mysqlSentences.split(";"))));

        return dataSource;
    }

    private List<Resource> searchMappingFiles(String contextName) {
        List<String> modules   = subdirectoriesFor(contextName);
        List<String> goodPaths = new ArrayList<>();

        for (String module : modules) {
            String[] files = mappingFilesIn(module + "/infrastructure/persistence/hibernate/");

            for (String file : files) {
                goodPaths.add(module + "/infrastructure/persistence/hibernate/" + file);
            }
        }

        return goodPaths.stream().map(FileSystemResource::new).collect(Collectors.toList());
    }

    private List<String> subdirectoriesFor(String contextName) {
        String path = "./src/" + contextName + "/main/tv/codely/" + contextName + "/";

        String[] files = new File(path).list((current, name) -> new File(current, name).isDirectory());

        if (null == files) {
            path  = "./main/tv/codely/" + contextName + "/";
            files = new File(path).list((current, name) -> new File(current, name).isDirectory());
        }

        if (null == files) {
            return Collections.emptyList();
        }

        String finalPath = path;

        return Arrays.stream(files).map(file -> finalPath + file).collect(Collectors.toList());
    }

    private String[] mappingFilesIn(String path) {
		List<String> fileList = new ArrayList<>();

		String[] hbmFiles = new File(path).list((current, name) -> new File(current, name).getName().contains(".hbm.xml"));
        String[] ormFiles = new File(path).list((current, name) -> new File(current, name).getName().contains(".orm.xml"));

		if (hbmFiles != null) {
			fileList.addAll(Arrays.asList(hbmFiles));
		}
		if (ormFiles != null) {
			fileList.addAll(Arrays.asList(ormFiles));
		}

		return fileList.toArray(new String[0]);
    }

    private Properties hibernateProperties() {
        Properties hibernateProperties = new Properties();
        hibernateProperties.put(AvailableSettings.HBM2DDL_AUTO, "none");
        hibernateProperties.put(AvailableSettings.SHOW_SQL, "false");
        hibernateProperties.put(AvailableSettings.DIALECT, "org.hibernate.dialect.MySQLDialect");
        hibernateProperties.put(AvailableSettings.TRANSFORM_HBM_XML, true);

        return hibernateProperties;
    }
}
```

## File: `src/shared/main/tv/codely/shared/infrastructure/hibernate/HibernateCriteriaConverter.java`
```java
package tv.codely.shared.infrastructure.hibernate;

import jakarta.persistence.criteria.*;
import tv.codely.shared.domain.criteria.Criteria;
import tv.codely.shared.domain.criteria.Filter;
import tv.codely.shared.domain.criteria.FilterOperator;

import java.util.HashMap;
import java.util.List;
import java.util.function.BiFunction;
import java.util.stream.Collectors;

public final class HibernateCriteriaConverter<T> {
    private final CriteriaBuilder builder;
    private final HashMap<FilterOperator, BiFunction<Filter, Root<T>, Predicate>> predicateTransformers = new HashMap<FilterOperator, BiFunction<Filter, Root<T>, Predicate>>() {{
        put(FilterOperator.EQUAL, HibernateCriteriaConverter.this::equalsPredicateTransformer);
        put(FilterOperator.NOT_EQUAL, HibernateCriteriaConverter.this::notEqualsPredicateTransformer);
        put(FilterOperator.GT, HibernateCriteriaConverter.this::greaterThanPredicateTransformer);
        put(FilterOperator.LT, HibernateCriteriaConverter.this::lowerThanPredicateTransformer);
        put(FilterOperator.CONTAINS, HibernateCriteriaConverter.this::containsPredicateTransformer);
        put(FilterOperator.NOT_CONTAINS, HibernateCriteriaConverter.this::notContainsPredicateTransformer);
    }};

    public HibernateCriteriaConverter(CriteriaBuilder builder) {
        this.builder = builder;
    }

    public CriteriaQuery<T> convert(Criteria criteria, Class<T> aggregateClass) {
        CriteriaQuery<T> hibernateCriteria = builder.createQuery(aggregateClass);
        Root<T>          root              = hibernateCriteria.from(aggregateClass);

        hibernateCriteria.where(formatPredicates(criteria.filters().filters(), root));

        if (criteria.order().hasOrder()) {
            Path<Object> orderBy = root.get(criteria.order().orderBy().value());
            Order        order   = criteria.order().orderType().isAsc() ? builder.asc(orderBy) : builder.desc(orderBy);

            hibernateCriteria.orderBy(order);
        }

        return hibernateCriteria;
    }

    private Predicate[] formatPredicates(List<Filter> filters, Root<T> root) {
        List<Predicate> predicates = filters.stream().map(filter -> formatPredicate(
            filter,
            root
        )).collect(Collectors.toList());

        Predicate[] predicatesArray = new Predicate[predicates.size()];
        predicatesArray = predicates.toArray(predicatesArray);

        return predicatesArray;
    }

    private Predicate formatPredicate(Filter filter, Root<T> root) {
        BiFunction<Filter, Root<T>, Predicate> transformer = predicateTransformers.get(filter.operator());

        return transformer.apply(filter, root);
    }

    private Predicate equalsPredicateTransformer(Filter filter, Root<T> root) {
        return builder.equal(root.get(filter.field().value()), filter.value().value());
    }

    private Predicate notEqualsPredicateTransformer(Filter filter, Root<T> root) {
        return builder.notEqual(root.get(filter.field().value()), filter.value().value());
    }

    private Predicate greaterThanPredicateTransformer(Filter filter, Root<T> root) {
        return builder.greaterThan(root.get(filter.field().value()), filter.value().value());
    }

    private Predicate lowerThanPredicateTransformer(Filter filter, Root<T> root) {
        return builder.lessThan(root.get(filter.field().value()), filter.value().value());
    }

    private Predicate containsPredicateTransformer(Filter filter, Root<T> root) {
        return builder.like(root.get(filter.field().value()), String.format("%%%s%%", filter.value().value()));
    }

    private Predicate notContainsPredicateTransformer(Filter filter, Root<T> root) {
        return builder.notLike(root.get(filter.field().value()), String.format("%%%s%%", filter.value().value()));
    }
}
```

## File: `src/shared/main/tv/codely/shared/infrastructure/hibernate/HibernateRepository.java`
```java
package tv.codely.shared.infrastructure.hibernate;

import jakarta.persistence.criteria.CriteriaQuery;
import org.hibernate.SessionFactory;
import tv.codely.shared.domain.Identifier;
import tv.codely.shared.domain.criteria.Criteria;

import java.util.List;
import java.util.Optional;

public abstract class HibernateRepository<T> {
    protected final SessionFactory             sessionFactory;
    protected final Class<T>                   aggregateClass;
    protected final HibernateCriteriaConverter<T> criteriaConverter;

    public HibernateRepository(SessionFactory sessionFactory, Class<T> aggregateClass) {
        this.sessionFactory    = sessionFactory;
        this.aggregateClass    = aggregateClass;
        this.criteriaConverter = new HibernateCriteriaConverter<>(sessionFactory.getCriteriaBuilder());
    }

    protected void persist(T entity) {
        sessionFactory.getCurrentSession().saveOrUpdate(entity);
        sessionFactory.getCurrentSession().flush();
        sessionFactory.getCurrentSession().clear();
    }

    protected Optional<T> byId(Identifier id) {
        return Optional.ofNullable(sessionFactory.getCurrentSession().byId(aggregateClass).load(id));
    }

    protected List<T> byCriteria(Criteria criteria) {
        CriteriaQuery<T> hibernateCriteria = criteriaConverter.convert(criteria, aggregateClass);

        return sessionFactory.getCurrentSession().createQuery(hibernateCriteria).getResultList();
    }

    protected List<T> all() {
        CriteriaQuery<T> criteria = sessionFactory.getCriteriaBuilder().createQuery(aggregateClass);

        criteria.from(aggregateClass);

        return sessionFactory.getCurrentSession().createQuery(criteria).getResultList();
    }
}
```

## File: `src/shared/main/tv/codely/shared/infrastructure/hibernate/JsonListType.java`
```java
package tv.codely.shared.infrastructure.hibernate;

import com.fasterxml.jackson.annotation.JsonAutoDetect;
import com.fasterxml.jackson.annotation.PropertyAccessor;
import com.fasterxml.jackson.databind.JavaType;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.hibernate.HibernateException;
import org.hibernate.engine.spi.SharedSessionContractImplementor;
import org.hibernate.usertype.DynamicParameterizedType;
import org.hibernate.usertype.UserType;

import java.io.IOException;
import java.io.Serializable;
import java.io.StringWriter;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Types;
import java.util.*;

public class JsonListType implements UserType, DynamicParameterizedType {
    private static final ObjectMapper OBJECT_MAPPER = new ObjectMapper();
    private JavaType valueType = null;
    private Class<?> classType = null;

    @Override
    public int getSqlType() {
        return Types.LONGVARCHAR;
    }

    @Override
    public Class<?> returnedClass() {
        return classType;
    }

    @Override
    public boolean equals(Object x, Object y) throws HibernateException {
        return Objects.equals(x, y);
    }

    @Override
    public int hashCode(Object x) throws HibernateException {
        return Objects.hashCode(x);
    }

    @Override
    public void nullSafeSet(
        PreparedStatement st,
        Object value,
        int index,
        SharedSessionContractImplementor session
    ) throws HibernateException, SQLException {
        nullSafeSet(st, value, index);
    }

	@Override
	public Object nullSafeGet(
		ResultSet resultSet,
		int index,
		SharedSessionContractImplementor session,
		Object owner
	) throws HibernateException, SQLException {

		String value = resultSet.getString(index).replace("\"value\"", "").replace("{:", "").replace("}", "");
		Object result = null;
		if (valueType == null) {
			throw new HibernateException("Value type not set.");
		}
		if (value != null && !value.equals("")) {
			try {
				result = OBJECT_MAPPER.readValue(value, valueType);
			} catch (IOException e) {
				throw new HibernateException("Exception deserializing value " + value, e);
			}
		}
		return result;
	}

    public void nullSafeSet(PreparedStatement st, Object value, int index) throws HibernateException, SQLException {
        StringWriter sw = new StringWriter();
        OBJECT_MAPPER.setVisibility(PropertyAccessor.FIELD, JsonAutoDetect.Visibility.ANY);

        if (value == null) {
            st.setNull(index, Types.VARCHAR);
        } else {
            try {
                OBJECT_MAPPER.writeValue(sw, value);
                st.setString(index, sw.toString());
            } catch (IOException e) {
                throw new HibernateException("Exception serializing value " + value, e);
            }
        }
    }

    @Override
    public Object deepCopy(Object value) throws HibernateException {
        if (value == null) {
            return null;
        } else if (valueType.isCollectionLikeType()) {
            Object newValue = new ArrayList<>();
            Collection newValueCollection = (Collection) newValue;
            newValueCollection.addAll((Collection) value);
            return newValueCollection;
        }

        return null;
    }

    @Override
    public boolean isMutable() {
        return true;
    }

    @Override
    public Serializable disassemble(Object value) throws HibernateException {
        return (Serializable) deepCopy(value);
    }

    @Override
    public Object assemble(Serializable cached, Object owner) throws HibernateException {
        return deepCopy(cached);
    }

    @Override
    public Object replace(Object original, Object target, Object owner) throws HibernateException {
        return deepCopy(original);
    }

    @Override
    public void setParameterValues(Properties parameters) {
        try {
            Class<?> entityClass = Class.forName(parameters.getProperty("list_of"));

            valueType = OBJECT_MAPPER.getTypeFactory().constructCollectionType(ArrayList.class, entityClass);
            classType = List.class;
        } catch (ClassNotFoundException e) {
            throw new IllegalArgumentException(e);
        }
    }
}
```

## File: `src/shared/main/tv/codely/shared/infrastructure/spring/ApiController.java`
```java
package tv.codely.shared.infrastructure.spring;

import org.springframework.http.HttpStatus;
import tv.codely.shared.domain.DomainError;
import tv.codely.shared.domain.bus.command.Command;
import tv.codely.shared.domain.bus.command.CommandBus;
import tv.codely.shared.domain.bus.command.CommandHandlerExecutionError;
import tv.codely.shared.domain.bus.query.Query;
import tv.codely.shared.domain.bus.query.QueryBus;
import tv.codely.shared.domain.bus.query.QueryHandlerExecutionError;

import java.util.HashMap;

public abstract class ApiController {
    private final QueryBus   queryBus;
    private final CommandBus commandBus;

    public ApiController(QueryBus queryBus, CommandBus commandBus) {
        this.queryBus   = queryBus;
        this.commandBus = commandBus;
    }

    protected void dispatch(Command command) throws CommandHandlerExecutionError {
        commandBus.dispatch(command);
    }

    protected <R> R ask(Query query) throws QueryHandlerExecutionError {
        return queryBus.ask(query);
    }

    abstract public HashMap<Class<? extends DomainError>, HttpStatus> errorMapping();
}
```

## File: `src/shared/main/tv/codely/shared/infrastructure/spring/ApiExceptionMiddleware.java`
```java
package tv.codely.shared.infrastructure.spring;

import org.springframework.http.HttpStatus;
import org.springframework.web.method.HandlerMethod;
import org.springframework.web.servlet.mvc.method.annotation.RequestMappingHandlerMapping;
import org.springframework.web.util.NestedServletException;
import tv.codely.shared.domain.DomainError;
import tv.codely.shared.domain.Utils;
import tv.codely.shared.domain.bus.command.CommandHandlerExecutionError;
import tv.codely.shared.domain.bus.query.QueryHandlerExecutionError;

import jakarta.servlet.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.HashMap;
import java.util.Objects;

public final class ApiExceptionMiddleware implements Filter {
    private RequestMappingHandlerMapping mapping;

    public ApiExceptionMiddleware(RequestMappingHandlerMapping mapping) {
        this.mapping = mapping;
    }

    @Override
    public void doFilter(
        ServletRequest request,
        ServletResponse response,
        FilterChain chain
    ) throws ServletException {
        HttpServletRequest  httpRequest  = ((HttpServletRequest) request);
        HttpServletResponse httpResponse = ((HttpServletResponse) response);

        try {
            Object possibleController = (
                (HandlerMethod) Objects.requireNonNull(
                    mapping.getHandler(httpRequest)).getHandler()
            ).getBean();

            try {
                chain.doFilter(request, response);
            } catch (Exception exception) {
                if (possibleController instanceof ApiController) {
                    handleCustomError(response, httpResponse, (ApiController) possibleController, exception);
                }
            }
        } catch (Exception e) {
            throw new ServletException(e);
        }
    }

    private void handleCustomError(
        ServletResponse response,
        HttpServletResponse httpResponse,
        ApiController possibleController,
        Exception exception
    ) throws IOException {
        HashMap<Class<? extends DomainError>, HttpStatus> errorMapping = possibleController
            .errorMapping();
        Throwable error = (
            exception.getCause() instanceof CommandHandlerExecutionError ||
            exception.getCause() instanceof QueryHandlerExecutionError
        )
            ? exception.getCause().getCause() : exception.getCause();

        int    statusCode   = statusFor(errorMapping, error);
        String errorCode    = errorCodeFor(error);
        String errorMessage = error.getMessage();

        httpResponse.reset();
        httpResponse.setHeader("Content-Type", "application/json");
        httpResponse.setStatus(statusCode);
        PrintWriter writer = response.getWriter();
        writer.write(String.format(
            "{\"error_code\": \"%s\", \"message\": \"%s\"}",
            errorCode,
            errorMessage
        ));
        writer.close();
    }

    private String errorCodeFor(Throwable error) {
        if (error instanceof DomainError) {
            return ((DomainError) error).errorCode();
        }

        return Utils.toSnake(error.getClass().toString());
    }

    private int statusFor(HashMap<Class<? extends DomainError>, HttpStatus> errorMapping, Throwable error) {
        return errorMapping.getOrDefault(error.getClass(), HttpStatus.INTERNAL_SERVER_ERROR).value();
    }
}
```

## File: `src/shared/main/tv/codely/shared/infrastructure/validation/ValidationResponse.java`
```java
package tv.codely.shared.infrastructure.validation;

import java.util.HashMap;
import java.util.List;

public final class ValidationResponse {
    private HashMap<String, List<String>> validationErrors;

    public ValidationResponse(HashMap<String, List<String>> validationErrors) {
        this.validationErrors = validationErrors;
    }

    public Boolean hasErrors() {
        return !validationErrors.isEmpty();
    }

    public HashMap<String, List<String>> errors() {
        return validationErrors;
    }
}
```

## File: `src/shared/main/tv/codely/shared/infrastructure/validation/Validator.java`
```java
package tv.codely.shared.infrastructure.validation;

import tv.codely.shared.infrastructure.validation.validators.*;

import java.io.Serializable;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public final class Validator {
    private static final HashMap<String, FieldValidator> validators = new HashMap<String, FieldValidator>() {{
        put("required", new RequiredValidator());
        put("string", new StringValidator());
        put("not_empty", new NotEmptyValidator());
        put("uuid", new UuidValidator());
    }};

    public static ValidationResponse validate(
        HashMap<String, Serializable> input,
        HashMap<String, String> combinedRules
    ) throws ValidatorNotExist {
        HashMap<String, List<String>> validationErrors = new HashMap<>();

        for (Map.Entry<String, String> entry : combinedRules.entrySet()) {
            String[] rules = entry.getValue().split("\\|");

            for (String rule : rules) {
                FieldValidator validator = validators.get(rule);

                if (null == validator) {
                    throw new ValidatorNotExist(rule);
                }

                if (!validator.isValid(entry.getKey(), input)) {
                    List<String> existingErrors = validationErrors.getOrDefault(entry.getKey(), new ArrayList<>());
                    existingErrors.add(validator.errorMessage(entry.getKey()));

                    validationErrors.put(entry.getKey(), existingErrors);
                }
            }
        }

        return new ValidationResponse(validationErrors);
    }
}
```

## File: `src/shared/main/tv/codely/shared/infrastructure/validation/ValidatorNotExist.java`
```java
package tv.codely.shared.infrastructure.validation;

public final class ValidatorNotExist extends Exception {
    public ValidatorNotExist(String name) {
        super(String.format("The validator <%s> does not exist", name));
    }
}
```

## File: `src/shared/main/tv/codely/shared/infrastructure/validation/validators/FieldValidator.java`
```java
package tv.codely.shared.infrastructure.validation.validators;

import java.io.Serializable;
import java.util.HashMap;

public interface FieldValidator {
    Boolean isValid(String fieldName, HashMap<String, Serializable> fields);

    String errorMessage(String fieldName);
}
```

## File: `src/shared/main/tv/codely/shared/infrastructure/validation/validators/NotEmptyValidator.java`
```java
package tv.codely.shared.infrastructure.validation.validators;

import java.io.Serializable;
import java.util.HashMap;

public final class NotEmptyValidator implements FieldValidator {
    @Override
    public Boolean isValid(String fieldName, HashMap<String, Serializable> fields) {
        return !fields.get(fieldName).toString().isEmpty();
    }

    @Override
    public String errorMessage(String fieldName) {
        return String.format("The field <%s> should not be empty", fieldName);
    }
}
```

## File: `src/shared/main/tv/codely/shared/infrastructure/validation/validators/RequiredValidator.java`
```java
package tv.codely.shared.infrastructure.validation.validators;

import java.io.Serializable;
import java.util.HashMap;

public final class RequiredValidator implements FieldValidator {
    @Override
    public Boolean isValid(String fieldName, HashMap<String, Serializable> fields) {
        return fields.containsKey(fieldName);
    }

    @Override
    public String errorMessage(String fieldName) {
        return String.format("The field <%s> is required", fieldName);
    }
}
```

## File: `src/shared/main/tv/codely/shared/infrastructure/validation/validators/StringValidator.java`
```java
package tv.codely.shared.infrastructure.validation.validators;

import java.io.Serializable;
import java.util.HashMap;

public final class StringValidator implements FieldValidator {
    @Override
    public Boolean isValid(String fieldName, HashMap<String, Serializable> fields) {
        return true;
    }

    @Override
    public String errorMessage(String fieldName) {
        return String.format("The field <%s> should be of type string", fieldName);
    }
}
```

## File: `src/shared/main/tv/codely/shared/infrastructure/validation/validators/UuidValidator.java`
```java
package tv.codely.shared.infrastructure.validation.validators;

import java.io.Serializable;
import java.util.HashMap;
import java.util.regex.Pattern;

public final class UuidValidator implements FieldValidator {
    @Override
    public Boolean isValid(String fieldName, HashMap<String, Serializable> fields) {
        Pattern uuidPattern = Pattern.compile("[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$");

        return uuidPattern.matcher((String) fields.get(fieldName)).matches();
    }

    @Override
    public String errorMessage(String fieldName) {
        return String.format("The field <%s> is not a valid uuid", fieldName);
    }
}
```

## File: `src/shared/test/tv/codely/shared/domain/EmailMother.java`
```java
package tv.codely.shared.domain;

public final class EmailMother {
    public static String random() {
        return MotherCreator.random().internet().emailAddress();
    }
}
```

## File: `src/shared/test/tv/codely/shared/domain/IntegerMother.java`
```java
package tv.codely.shared.domain;

public final class IntegerMother {
    public static Integer random() {
        return MotherCreator.random().number().randomDigit();
    }
}
```

## File: `src/shared/test/tv/codely/shared/domain/ListMother.java`
```java
package tv.codely.shared.domain;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.function.Supplier;

public final class ListMother {
    public static <T> List<T> create(Integer size, Supplier<T> creator) {
        ArrayList<T> list = new ArrayList<>();

        for (int i = 0; i < size; i++) {
            list.add(creator.get());
        }

        return list;
    }

    public static <T> List<T> random(Supplier<T> creator) {
        return create(IntegerMother.random(), creator);
    }

    public static <T> List<T> one(T element) {
        return Collections.singletonList(element);
    }
}
```

## File: `src/shared/test/tv/codely/shared/domain/MotherCreator.java`
```java
package tv.codely.shared.domain;

import com.github.javafaker.Faker;

public final class MotherCreator {
    private final static Faker faker = new Faker();

    public static Faker random() {
        return faker;
    }
}
```

## File: `src/shared/test/tv/codely/shared/domain/RandomElementPicker.java`
```java
package tv.codely.shared.domain;

import java.util.Random;

public final class RandomElementPicker {
    @SafeVarargs
    public static <T> T from(T... elements) {
        Random rand = new Random();

        return elements[rand.nextInt(elements.length)];
    }
}
```

## File: `src/shared/test/tv/codely/shared/domain/UuidMother.java`
```java
package tv.codely.shared.domain;

import java.util.UUID;

public final class UuidMother {
    public static String random() {
        return UUID.randomUUID().toString();
    }
}
```

## File: `src/shared/test/tv/codely/shared/domain/VideoUrlMother.java`
```java
package tv.codely.shared.domain;

public final class VideoUrlMother {
    public static VideoUrl create(String value) {
        return new VideoUrl(value);
    }

    public static VideoUrl random() {
        return create(MotherCreator.random().internet().url());
    }
}
```

## File: `src/shared/test/tv/codely/shared/domain/WordMother.java`
```java
package tv.codely.shared.domain;

public final class WordMother {
    public static String random() {
        return MotherCreator.random().lorem().word();
    }
}
```

## File: `src/shared/test/tv/codely/shared/infrastructure/InfrastructureTestCase.java`
```java
package tv.codely.shared.infrastructure;

public abstract class InfrastructureTestCase {
    private final int MAX_ATTEMPTS                   = 3;
    private final int MILLIS_TO_WAIT_BETWEEN_RETRIES = 300;

    protected void eventually(Runnable assertion) throws Exception {
        int     attempts = 0;
        boolean allOk    = false;

        while (attempts < MAX_ATTEMPTS && !allOk) {
            try {
                assertion.run();

                allOk = true;
            } catch (Throwable error) {
                attempts++;

                if (attempts > MAX_ATTEMPTS) {
                    throw new Exception(
                        String.format("Could not assert after some retries. Last error: %s", error.getMessage())
                    );
                }

                Thread.sleep(MILLIS_TO_WAIT_BETWEEN_RETRIES);
            }
        }
    }
}
```

## File: `src/shared/test/tv/codely/shared/infrastructure/UnitTestCase.java`
```java
package tv.codely.shared.infrastructure;

import org.junit.jupiter.api.BeforeEach;
import tv.codely.shared.domain.UuidGenerator;
import tv.codely.shared.domain.bus.event.DomainEvent;
import tv.codely.shared.domain.bus.event.EventBus;
import tv.codely.shared.domain.bus.query.*;

import java.util.Collections;
import java.util.List;

import static org.mockito.Mockito.*;

public abstract class UnitTestCase {
    protected EventBus      eventBus;
    protected QueryBus      queryBus;
    protected UuidGenerator uuidGenerator;

    @BeforeEach
    protected void setUp() {
        eventBus      = mock(EventBus.class);
        queryBus      = mock(QueryBus.class);
        uuidGenerator = mock(UuidGenerator.class);
    }

    public void shouldHavePublished(List<DomainEvent> domainEvents) {
        verify(eventBus, atLeastOnce()).publish(domainEvents);
    }

    public void shouldHavePublished(DomainEvent domainEvent) {
        shouldHavePublished(Collections.singletonList(domainEvent));
    }

    public void shouldGenerateUuid(String uuid) {
        when(uuidGenerator.generate()).thenReturn(uuid);
    }

    public void shouldGenerateUuids(String uuid, String... others) {
        when(uuidGenerator.generate()).thenReturn(uuid, others);
    }

    public void shouldAsk(Query query, Response response) {
        when(queryBus.ask(query)).thenReturn(response);
    }
}
```


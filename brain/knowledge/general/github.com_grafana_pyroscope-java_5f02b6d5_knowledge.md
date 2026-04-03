---
id: github.com-grafana-pyroscope-java-5f02b6d5-knowled
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:20:04.438496
---

# KNOWLEDGE EXTRACT: github.com_grafana_pyroscope-java_5f02b6d5
> **Extracted on:** 2026-04-01 16:24:03
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007525099/github.com_grafana_pyroscope-java_5f02b6d5

---

## File: `.dockerignore`
```
.gradle
**/build/
**/out/
```

## File: `.editorconfig`
```
root = true

[*]
end_of_line = lf
indent_style = space

[{*.java,build.gradle,settings.gradle}]
indent_size = 4
```

## File: `.gitattributes`
```
#
# https://help.github.com/articles/dealing-with-line-endings/
#
# These are explicitly windows files and should use crlf
*.bat           text eol=crlf

```

## File: `.gitignore`
```
out/
/.idea/
/.vscode/

# Ignore Gradle project-specific cache directory
.gradle

# Ignore Gradle build output directory
build

# Compiled class file
*.class

# Log file
*.log

# BlueJ files
*.ctxt

# Mobile Tools for Java (J2ME)
.mtj.tmp/

# Package Files #
*.jar
*.war
*.nar
*.ear
*.zip
*.tar.gz
*.rar

# Exception for async-profiler distribution
!async-profiler-grafana-fork-dist/lib/async-profiler.jar

# virtual machine crash logs, see http://www.java.com/en/download/help/error_hotspot.xml
hs_err_pid*

.settings
.project
.classpath
```

## File: `CODEOWNERS`
```
* @grafana/pyroscope-java @grafana/pyroscope-team
```

## File: `LICENSE`
```

                                 Apache License
                           Version 2.0, January 2004
                        http://www.apache.org/licenses/

   TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

   1. Definitions.

      "License" shall mean the terms and conditions for use, reproduction,
      and distribution as defined by Sections 1 through 9 of this document.

      "Licensor" shall mean the copyright owner or entity authorized by
      the copyright owner that is granting the License.

      "Legal Entity" shall mean the union of the acting entity and all
      other entities that control, are controlled by, or are under common
      control with that entity. For the purposes of this definition,
      "control" means (i) the power, direct or indirect, to cause the
      direction or management of such entity, whether by contract or
      otherwise, or (ii) ownership of fifty percent (50%) or more of the
      outstanding shares, or (iii) beneficial ownership of such entity.

      "You" (or "Your") shall mean an individual or Legal Entity
      exercising permissions granted by this License.

      "Source" form shall mean the preferred form for making modifications,
      including but not limited to software source code, documentation
      source, and configuration files.

      "Object" form shall mean any form resulting from mechanical
      transformation or translation of a Source form, including but
      not limited to compiled object code, generated documentation,
      and conversions to other media types.

      "Work" shall mean the work of authorship, whether in Source or
      Object form, made available under the License, as indicated by a
      copyright notice that is included in or attached to the work
      (an example is provided in the Appendix below).

      "Derivative Works" shall mean any work, whether in Source or Object
      form, that is based on (or derived from) the Work and for which the
      editorial revisions, annotations, elaborations, or other modifications
      represent, as a whole, an original work of authorship. For the purposes
      of this License, Derivative Works shall not include works that remain
      separable from, or merely link (or bind by name) to the interfaces of,
      the Work and Derivative Works thereof.

      "Contribution" shall mean any work of authorship, including
      the original version of the Work and any modifications or additions
      to that Work or Derivative Works thereof, that is intentionally
      submitted to Licensor for inclusion in the Work by the copyright owner
      or by an individual or Legal Entity authorized to submit on behalf of
      the copyright owner. For the purposes of this definition, "submitted"
      means any form of electronic, verbal, or written communication sent
      to the Licensor or its representatives, including but not limited to
      communication on electronic mailing lists, source code control systems,
      and issue tracking systems that are managed by, or on behalf of, the
      Licensor for the purpose of discussing and improving the Work, but
      excluding communication that is conspicuously marked or otherwise
      designated in writing by the copyright owner as "Not a Contribution."

      "Contributor" shall mean Licensor and any individual or Legal Entity
      on behalf of whom a Contribution has been received by Licensor and
      subsequently incorporated within the Work.

   2. Grant of Copyright License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      copyright license to reproduce, prepare Derivative Works of,
      publicly display, publicly perform, sublicense, and distribute the
      Work and such Derivative Works in Source or Object form.

   3. Grant of Patent License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      (except as stated in this section) patent license to make, have made,
      use, offer to sell, sell, import, and otherwise transfer the Work,
      where such license applies only to those patent claims licensable
      by such Contributor that are necessarily infringed by their
      Contribution(s) alone or by combination of their Contribution(s)
      with the Work to which such Contribution(s) was submitted. If You
      institute patent litigation against any entity (including a
      cross-claim or counterclaim in a lawsuit) alleging that the Work
      or a Contribution incorporated within the Work constitutes direct
      or contributory patent infringement, then any patent licenses
      granted to You under this License for that Work shall terminate
      as of the date such litigation is filed.

   4. Redistribution. You may reproduce and distribute copies of the
      Work or Derivative Works thereof in any medium, with or without
      modifications, and in Source or Object form, provided that You
      meet the following conditions:

      (a) You must give any other recipients of the Work or
          Derivative Works a copy of this License; and

      (b) You must cause any modified files to carry prominent notices
          stating that You changed the files; and

      (c) You must retain, in the Source form of any Derivative Works
          that You distribute, all copyright, patent, trademark, and
          attribution notices from the Source form of the Work,
          excluding those notices that do not pertain to any part of
          the Derivative Works; and

      (d) If the Work includes a "NOTICE" text file as part of its
          distribution, then any Derivative Works that You distribute must
          include a readable copy of the attribution notices contained
          within such NOTICE file, excluding those notices that do not
          pertain to any part of the Derivative Works, in at least one
          of the following places: within a NOTICE text file distributed
          as part of the Derivative Works; within the Source form or
          documentation, if provided along with the Derivative Works; or,
          within a display generated by the Derivative Works, if and
          wherever such third-party notices normally appear. The contents
          of the NOTICE file are for informational purposes only and
          do not modify the License. You may add Your own attribution
          notices within Derivative Works that You distribute, alongside
          or as an addendum to the NOTICE text from the Work, provided
          that such additional attribution notices cannot be construed
          as modifying the License.

      You may add Your own copyright statement to Your modifications and
      may provide additional or different license terms and conditions
      for use, reproduction, or distribution of Your modifications, or
      for any such Derivative Works as a whole, provided Your use,
      reproduction, and distribution of the Work otherwise complies with
      the conditions stated in this License.

   5. Submission of Contributions. Unless You explicitly state otherwise,
      any Contribution intentionally submitted for inclusion in the Work
      by You to the Licensor shall be under the terms and conditions of
      this License, without any additional terms or conditions.
      Notwithstanding the above, nothing herein shall supersede or modify
      the terms of any separate license agreement you may have executed
      with Licensor regarding such Contributions.

   6. Trademarks. This License does not grant permission to use the trade
      names, trademarks, service marks, or product names of the Licensor,
      except as required for reasonable and customary use in describing the
      origin of the Work and reproducing the content of the NOTICE file.

   7. Disclaimer of Warranty. Unless required by applicable law or
      agreed to in writing, Licensor provides the Work (and each
      Contributor provides its Contributions) on an "AS IS" BASIS,
      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
      implied, including, without limitation, any warranties or conditions
      of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
      PARTICULAR PURPOSE. You are solely responsible for determining the
      appropriateness of using or redistributing the Work and assume any
      risks associated with Your exercise of permissions under this License.

   8. Limitation of Liability. In no event and under no legal theory,
      whether in tort (including negligence), contract, or otherwise,
      unless required by applicable law (such as deliberate and grossly
      negligent acts) or agreed to in writing, shall any Contributor be
      liable to You for damages, including any direct, indirect, special,
      incidental, or consequential damages of any character arising as a
      result of this License or out of the use or inability to use the
      Work (including but not limited to damages for loss of goodwill,
      work stoppage, computer failure or malfunction, or any and all
      other commercial damages or losses), even if such Contributor
      has been advised of the possibility of such damages.

   9. Accepting Warranty or Additional Liability. While redistributing
      the Work or Derivative Works thereof, You may choose to offer,
      and charge a fee for, acceptance of support, warranty, indemnity,
      or other liability obligations and/or rights consistent with this
      License. However, in accepting such obligations, You may act only
      on Your own behalf and on Your sole responsibility, not on behalf
      of any other Contributor, and only if You agree to indemnify,
      defend, and hold each Contributor harmless for any liability
      incurred by, or claims asserted against, such Contributor by reason
      of your accepting any such warranty or additional liability.

   END OF TERMS AND CONDITIONS

   APPENDIX: How to apply the Apache License to your work.

      To apply the Apache License to your work, attach the following
      boilerplate notice, with the fields enclosed by brackets "[]"
      replaced with your own identifying information. (Don't include
      the brackets!)  The text should be enclosed in the appropriate
      comment syntax for the file format. We also recommend that a
      file or class name and description of purpose be included on the
      same "printed page" as the copyright notice for easier
      identification within third-party archives.

   Copyright 2020 Pyroscope, Inc

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
```

## File: `Makefile`
```
GRAFANA_PYROSCOPE_VERSION := 4.3.0.1

.PHONY: download-async-profiler
download-async-profiler:
	./scripts/download-async-profiler.sh -v $(GRAFANA_PYROSCOPE_VERSION) -r https://github.com/grafana/async-profiler -d async-profiler-grafana-fork-dist
	#./scripts/download-async-profiler.sh -v 4.0 -r https://github.com/async-profiler/async-profiler -d async-profiler-genuine-dist

.PHONY: clean
clean:
	rm -rf agent/build

.PHONY: build
build:
	./gradlew shadowJar

.PHONY: publish
publish:
	@echo "./gradlew clean :agent:shadowJar publishToSonatype closeAndReleaseSonatypeStagingRepository"
	@./gradlew clean :agent:shadowJar publishToSonatype closeAndReleaseSonatypeStagingRepository \
		-PsonatypeUsername="$(NEXUS_USERNAME)" \
		-PsonatypePassword="$(NEXUS_PASSWORD)" \
		-Psigning.secretKeyRingFile="$(NEXUS_GPG_SECRING_FILE)" \
		-Psigning.password="$(NEXUS_GPG_PASSWORD)" \
		-Psigning.keyId="$(NEXUS_GPG_KEY_ID)"
	@echo "https://central.sonatype.org/publish/release/#locate-and-examine-your-staging-repository"

.PHONY: test
test:
	./gradlew test

.PHONY: docker-example-base
docker-example-base: build
	cp agent/build/libs/pyroscope.jar examples
	docker compose -f examples/docker-compose-base.yml build
	docker compose -f examples/docker-compose-base.yml up

.PHONY: docker-example-expt
docker-example-expt: build
	cp agent/build/libs/pyroscope.jar examples
	docker compose -f examples/docker-compose-expt.yml build
	docker compose -f examples/docker-compose-expt.yml up

ITEST_SERVICE ?=

.PHONY: itest
itest:
	docker compose -f docker-compose-itest.yaml up --build --force-recreate -d pyroscope $(ITEST_SERVICE)
	cd itest/query && go run . $(ITEST_SERVICE)
	docker compose -f docker-compose-itest.yaml down pyroscope $(ITEST_SERVICE)
```

## File: `README.md`
```markdown
# Pyroscope Java agent

The Java profiling agent for Pyroscope.io. Based
on [async-profiler](https://github.com/jvm-profiling-tools/async-profiler).

## Distribution

The agent is distributed as a single JAR file `pyroscope.jar`. It contains native async-profiler libraries for:

- Linux on x64;
- Linux on ARM64;
- MacOS on x64.
- MacOS on ARM64.

## Windows OS support

It also contains support for Windows OS, through JFR profiler. In order to use JFR as profiler in place of
async-profiler,
you need to configure profiler type, either through configuration file or environment variable.

By setting `PYROSCOPE_PROFILER_TYPE` configuration variable to `JFR`, agent will use JVM built-in profiler.

## Downloads

Visit [releases](https://github.com/pyroscope-io/pyroscope-java/releases) page to download the latest version
of `pyroscope.jar`

## Usage

Visit [docs](https://pyroscope.io/docs/java/) page for usage and configuration documentation.

## Building

If you want to build the agent JAR yourself, from this repo run:

```shell
./gradlew shadowJar
```

The file will be in `agent/build/libs/pyroscope.jar`.

## Maintainers

This package is maintained by [@grafana/pyroscope-java](https://github.com/orgs/grafana/teams/pyroscope-java).
Mention this team on issues or PRs for feedback.
```

## File: `TODO`
```
TODO support multiple simultaneous profiling modes (profiling event types)
  - async-profiler dump format
    - ATM, the collapsed dump format (what we're using) is not supported for multiple-event profiling
      - can it be supported?
      - see
        - https://github.com/jvm-profiling-tools/async-profiler/issues/150
        - https://github.com/jvm-profiling-tools/async-profiler/issues/357
  - data flow changes
    - ATM, sample snapshots are uploaded specifying event-type-dependent parameters per snapshot
      - so multiple-event profiling needs a dedicated queue+snapshot+upload pipeline for each event type used simultaneously

TODO support per-thread profiling
  - use AsnycProfiler::execute
    - see
      - https://github.com/jvm-profiling-tools/async-profiler/issues/473
```

## File: `alpine-test.Dockerfile`
```
ARG IMAGE_VERSION
ARG JAVA_VERSION

FROM alpine:3.23.3@sha256:25109184c71bdad752c8312a8623239686a9a2071e8825f20acb8f2198c3f659 AS builder
ARG JAVA_VERSION
RUN if [ "${JAVA_VERSION}" -ge 25 ] 2>/dev/null; then \
        apk add openjdk17; \
    else \
        apk add openjdk11; \
    fi

WORKDIR /app
ADD gradlew build.gradle settings.gradle gradle.properties /app/
ADD gradle gradle
RUN if [ "${JAVA_VERSION}" -ge 25 ] 2>/dev/null; then ./gradlew --no-daemon wrapper --gradle-version=9.0; fi
RUN ./gradlew --no-daemon --version
ADD agent agent
ADD async-profiler-grafana-fork-dist async-profiler-grafana-fork-dist
ADD demo/build.gradle demo/

RUN ./gradlew --no-daemon shadowJar

FROM alpine:${IMAGE_VERSION} AS runner
ARG IMAGE_VERSION
ARG JAVA_VERSION
RUN apk add --no-cache curl && \
    curl -fsSL https://cdn.azul.com/public_keys/alpine-signing@azul.com-5d5dc44c.rsa.pub -o /etc/apk/keys/alpine-signing@azul.com-5d5dc44c.rsa.pub && \
    echo "https://repos.azul.com/zulu/alpine" >> /etc/apk/repositories && \
    apk update && \
    apk add zulu${JAVA_VERSION}-jdk

WORKDIR /app
ADD demo demo
COPY --from=builder /app/agent/build/libs/pyroscope.jar /app/agent/build/libs/pyroscope.jar

RUN javac demo/src/main/java/Fib.java

ENV PYROSCOPE_LOG_LEVEL=debug
ENV PYROSCOPE_SERVER_ADDRESS=http://pyroscope:4040
ENV PYROSCOPE_APPLICATION_NAME=alpine-${IMAGE_VERSION}-${JAVA_VERSION}
ENV PYROSCOPE_UPLOAD_INTERVAL=15s

CMD ["java", "-javaagent:/app/agent/build/libs/pyroscope.jar", "-cp", "demo/src/main/java/", "Fib"]
```

## File: `build.gradle`
```
plugins {
	id 'io.github.gradle-nexus.publish-plugin' version '1.3.0'
}

group = "io.pyroscope"
version = project.properties['pyroscope_version']

nexusPublishing {
    repositories {
        sonatype {
            nexusUrl.set(uri("https://ossrh-staging-api.central.sonatype.com/service/local/"))
            snapshotRepositoryUrl.set(uri("https://central.sonatype.com/repository/maven-snapshots/"))
        }
    }
}
```

## File: `docker-compose-itest.yaml`
```yaml
services:
  alpine-3.16-8:
    build:
      platforms:
        - linux/amd64
      context: .
      dockerfile: alpine-test.Dockerfile
      args:
        IMAGE_VERSION: 3.16
        JAVA_VERSION: 8
  alpine-3.16-11:
    build:
      platforms:
        - linux/amd64
      context: .
      dockerfile: alpine-test.Dockerfile
      args:
        IMAGE_VERSION: 3.16
        JAVA_VERSION: 11
  alpine-3.16-17:
    build:
      platforms:
        - linux/amd64
      context: .
      dockerfile: alpine-test.Dockerfile
      args:
        IMAGE_VERSION: 3.16
        JAVA_VERSION: 17
  alpine-3.17-8:
    build:
      platforms:
        - linux/amd64
      context: .
      dockerfile: alpine-test.Dockerfile
      args:
        IMAGE_VERSION: 3.17
        JAVA_VERSION: 8
  alpine-3.17-11:
    build:
      platforms:
        - linux/amd64
      context: .
      dockerfile: alpine-test.Dockerfile
      args:
        IMAGE_VERSION: 3.17
        JAVA_VERSION: 11
  alpine-3.17-17:
    build:
      platforms:
        - linux/amd64
      context: .
      dockerfile: alpine-test.Dockerfile
      args:
        IMAGE_VERSION: 3.17
        JAVA_VERSION: 17
  alpine-3.18-8:
    build:
      platforms:
        - linux/amd64
      context: .
      dockerfile: alpine-test.Dockerfile
      args:
        IMAGE_VERSION: 3.18
        JAVA_VERSION: 8
  alpine-3.18-11:
    build:
      platforms:
        - linux/amd64
      context: .
      dockerfile: alpine-test.Dockerfile
      args:
        IMAGE_VERSION: 3.18
        JAVA_VERSION: 11
  alpine-3.18-17:
    build:
      platforms:
        - linux/amd64
      context: .
      dockerfile: alpine-test.Dockerfile
      args:
        IMAGE_VERSION: 3.18
        JAVA_VERSION: 17
  alpine-3.18-21:
    build:
      platforms:
        - linux/amd64
      context: .
      dockerfile: alpine-test.Dockerfile
      args:
        IMAGE_VERSION: 3.18
        JAVA_VERSION: 21
  alpine-3.19-8:
    build:
      platforms:
        - linux/amd64
      context: .
      dockerfile: alpine-test.Dockerfile
      args:
        IMAGE_VERSION: 3.19
        JAVA_VERSION: 8
  alpine-3.19-11:
    build:
      platforms:
        - linux/amd64
      context: .
      dockerfile: alpine-test.Dockerfile
      args:
        IMAGE_VERSION: 3.19
        JAVA_VERSION: 11
  alpine-3.19-17:
    build:
      platforms:
        - linux/amd64
      context: .
      dockerfile: alpine-test.Dockerfile
      args:
        IMAGE_VERSION: 3.19
        JAVA_VERSION: 17
  alpine-3.19-21:
    build:
      platforms:
        - linux/amd64
      context: .
      dockerfile: alpine-test.Dockerfile
      args:
        IMAGE_VERSION: 3.19
        JAVA_VERSION: 21
  alpine-3.19-25:
    build:
      platforms:
        - linux/amd64
      context: .
      dockerfile: alpine-test.Dockerfile
      args:
        IMAGE_VERSION: 3.19
        JAVA_VERSION: 25

  ubuntu-18.04-8:
    build:
      platforms:
        - linux/amd64
      context: .
      dockerfile: ubuntu-test.Dockerfile
      args:
        IMAGE_VERSION: 18.04
        JAVA_VERSION: 8
  ubuntu-18.04-11:
    build:
      platforms:
        - linux/amd64
      context: .
      dockerfile: ubuntu-test.Dockerfile
      args:
        IMAGE_VERSION: 18.04
        JAVA_VERSION: 11
  ubuntu-18.04-17:
    build:
      platforms:
        - linux/amd64
      context: .
      dockerfile: ubuntu-test.Dockerfile
      args:
        IMAGE_VERSION: 18.04
        JAVA_VERSION: 17
  ubuntu-20.04-8:
    build:
      platforms:
        - linux/amd64
      context: .
      dockerfile: ubuntu-test.Dockerfile
      args:
        IMAGE_VERSION: 20.04
        JAVA_VERSION: 8
  ubuntu-20.04-11:
    build:
      platforms:
        - linux/amd64
      context: .
      dockerfile: ubuntu-test.Dockerfile
      args:
        IMAGE_VERSION: 20.04
        JAVA_VERSION: 11
  ubuntu-20.04-17:
    build:
      platforms:
        - linux/amd64
      context: .
      dockerfile: ubuntu-test.Dockerfile
      args:
        IMAGE_VERSION: 20.04
        JAVA_VERSION: 17
  ubuntu-20.04-21:
    build:
      platforms:
        - linux/amd64
      context: .
      dockerfile: ubuntu-test.Dockerfile
      args:
        IMAGE_VERSION: 20.04
        JAVA_VERSION: 21
  ubuntu-20.04-25:
    build:
      platforms:
        - linux/amd64
      context: .
      dockerfile: ubuntu-test.Dockerfile
      args:
        IMAGE_VERSION: 20.04
        JAVA_VERSION: 25
  ubuntu-22.04-8:
    build:
      platforms:
        - linux/amd64
      context: .
      dockerfile: ubuntu-test.Dockerfile
      args:
        IMAGE_VERSION: 22.04
        JAVA_VERSION: 8
  ubuntu-22.04-11:
    build:
      platforms:
        - linux/amd64
      context: .
      dockerfile: ubuntu-test.Dockerfile
      args:
        IMAGE_VERSION: 22.04
        JAVA_VERSION: 11
  ubuntu-22.04-17:
    build:
      platforms:
        - linux/amd64
      context: .
      dockerfile: ubuntu-test.Dockerfile
      args:
        IMAGE_VERSION: 22.04
        JAVA_VERSION: 17
  ubuntu-22.04-21:
    build:
      platforms:
        - linux/amd64
      context: .
      dockerfile: ubuntu-test.Dockerfile
      args:
        IMAGE_VERSION: 22.04
        JAVA_VERSION: 21
  ubuntu-22.04-25:
    build:
      platforms:
        - linux/amd64
      context: .
      dockerfile: ubuntu-test.Dockerfile
      args:
        IMAGE_VERSION: 22.04
        JAVA_VERSION: 25
  pyroscope:
    image: 'grafana/pyroscope:1.18.0@sha256:e7edae4fd99dbb8695a1e03d7db96ab247630cf83842407908922b2f66aafc6a'
    ports:
      - 4040:4040


```

## File: `gradle.properties`
```
pyroscope_version=2.5.2
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
# SPDX-License-Identifier: Apache-2.0
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
#       https://github.com/gradle/gradle/blob/HEAD/platforms/jvm/plugins-application/src/main/resources/org/gradle/api/internal/plugins/unixStartScript.txt
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
APP_HOME=$( cd -P "${APP_HOME:-./}" > /dev/null && printf '%s\n' "$PWD" ) || exit

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

CLASSPATH="\\\"\\\""


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
#   * DEFAULT_JVM_OPTS, JAVA_OPTS, and optsEnvironmentVar are not allowed to contain shell fragments,
#     and any embedded shellness will be escaped.
#   * For example: A user cannot expect ${Hostname} to be expanded, as it is an environment variable and will be
#     treated as '${Hostname}' itself on the command line.

set -- \
        "-Dorg.gradle.appname=$APP_BASE_NAME" \
        -classpath "$CLASSPATH" \
        -jar "$APP_HOME/gradle/wrapper/gradle-wrapper.jar" \
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
@rem SPDX-License-Identifier: Apache-2.0
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

echo. 1>&2
echo ERROR: JAVA_HOME is not set and no 'java' command could be found in your PATH. 1>&2
echo. 1>&2
echo Please set the JAVA_HOME variable in your environment to match the 1>&2
echo location of your Java installation. 1>&2

goto fail

:findJavaFromJavaHome
set JAVA_HOME=%JAVA_HOME:"=%
set JAVA_EXE=%JAVA_HOME%/bin/java.exe

if exist "%JAVA_EXE%" goto execute

echo. 1>&2
echo ERROR: JAVA_HOME is set to an invalid directory: %JAVA_HOME% 1>&2
echo. 1>&2
echo Please set the JAVA_HOME variable in your environment to match the 1>&2
echo location of your Java installation. 1>&2

goto fail

:execute
@rem Setup the command line

set CLASSPATH=


@rem Execute Gradle
"%JAVA_EXE%" %DEFAULT_JVM_OPTS% %JAVA_OPTS% %GRADLE_OPTS% "-Dorg.gradle.appname=%APP_BASE_NAME%" -classpath "%CLASSPATH%" -jar "%APP_HOME%\gradle\wrapper\gradle-wrapper.jar" %*

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

## File: `settings.gradle`
```
rootProject.name = 'pyroscope-java'
include('agent')
include('demo')
```

## File: `ubuntu-test.Dockerfile`
```
ARG IMAGE_VERSION
ARG JAVA_VERSION

FROM ubuntu:18.04@sha256:152dc042452c496007f07ca9127571cb9c29697f42acbfad72324b2bb2e43c98 AS builder
ARG JAVA_VERSION
RUN apt-get update && \
    if [ "${JAVA_VERSION}" -ge 25 ] 2>/dev/null; then \
        apt-get install -y openjdk-17-jdk-headless; \
    else \
        apt-get install -y openjdk-11-jdk-headless; \
    fi

WORKDIR /app
ADD gradlew build.gradle settings.gradle gradle.properties /app/
ADD gradle gradle
RUN if [ "${JAVA_VERSION}" -ge 25 ] 2>/dev/null; then ./gradlew --no-daemon wrapper --gradle-version=9.0; fi
RUN ./gradlew --no-daemon --version
ADD agent agent
ADD async-profiler-grafana-fork-dist async-profiler-grafana-fork-dist
ADD demo/build.gradle demo/


RUN ./gradlew --no-daemon shadowJar

FROM ubuntu:${IMAGE_VERSION} AS runner
ARG IMAGE_VERSION
ARG JAVA_VERSION
RUN apt-get update && \
    apt-get install -y gnupg curl && \
    curl -fsSL https://repos.azul.com/azul-repo.key | gpg --dearmor -o /usr/share/keyrings/azul.gpg && \
    echo "deb [signed-by=/usr/share/keyrings/azul.gpg] https://repos.azul.com/zulu/deb stable main" > /etc/apt/sources.list.d/zulu.list && \
    apt-get update && \
    apt-get install -y zulu${JAVA_VERSION}-jdk

WORKDIR /app
ADD demo demo
COPY --from=builder /app/agent/build/libs/pyroscope.jar /app/agent/build/libs/pyroscope.jar

RUN javac demo/src/main/java/Fib.java

ENV PYROSCOPE_LOG_LEVEL=debug
ENV PYROSCOPE_SERVER_ADDRESS=http://pyroscope:4040
ENV PYROSCOPE_UPLOAD_INTERVAL=5s
ENV PYROSCOPE_APPLICATION_NAME=ubuntu-${IMAGE_VERSION}-${JAVA_VERSION}

CMD ["java", "-javaagent:/app/agent/build/libs/pyroscope.jar", "-cp", "demo/src/main/java/", "Fib"]
```

## File: `agent/build.gradle`
```
import java.util.jar.JarFile

plugins {
    id 'java-library'
    id 'maven-publish'
    id 'signing'
    id "com.gradleup.shadow" version '8.3.9'
}

repositories {
    mavenCentral()
}

def asyncProfilerDistDir = file("$rootDir/async-profiler-grafana-fork-dist/lib")
def pyroscopeVersion = project.properties['pyroscope_version']
dependencies {
    api files("$asyncProfilerDistDir/async-profiler.jar")
    compileOnly 'org.jetbrains:annotations:26.0.2-1'
    implementation('com.squareup.okhttp3:okhttp:4.12.0')
    implementation("com.squareup.moshi:moshi:1.15.2")
    implementation("org.jetbrains.kotlin:kotlin-stdlib-jdk8:2.3.0")
    api 'com.google.protobuf:protobuf-java:4.33.5'
    testImplementation 'org.junit.jupiter:junit-jupiter:5.14.2'
    testRuntimeOnly 'org.junit.platform:junit-platform-launcher'
    testImplementation group: 'org.mockito', name: 'mockito-core', version: '3.12.4'
    testImplementation group: 'org.mockito', name: 'mockito-junit-jupiter', version: '3.12.4'
}

// Create a JAR containing ONLY the 3 bootstrap-api classes
// This JAR will be embedded as a resource for bootstrap classloader injection
task bootstrapApiJar(type: Jar) {
    dependsOn compileJava
    archiveBaseName.set('pyroscope-bootstrap')
    archiveVersion.set('')
    archiveClassifier.set('')

    // Include only the 3 bootstrap-api classes from compiled output
    from(sourceSets.main.java.classesDirectory) {
        include 'io/pyroscope/javaagent/api/ProfilerApi.class'
        include 'io/pyroscope/javaagent/api/ProfilerApiHolder.class'
        include 'io/pyroscope/javaagent/api/ProfilerScopedContext.class'
    }

    destinationDirectory.set(file("$buildDir/libs"))
}

// Copy the bootstrap JAR into resources as .bin file
// BootstrapApiInjector reads this resource at runtime
task copyBootstrapToResources(type: Copy) {
    dependsOn bootstrapApiJar
    from(bootstrapApiJar.archiveFile)
    into(sourceSets.main.output.resourcesDir)
    rename { 'pyroscope-bootstrap.jar.bin' }
}

processResources.dependsOn copyBootstrapToResources

javadoc{
    // excluded as javadoc generation fails on inaccessible sun.management.VMManagement class
    exclude("io/pyroscope/javaagent/CurrentPidProvider.java")
}

jar {
    manifest {
        attributes(
                'Premain-Class': 'io.pyroscope.javaagent.PyroscopeAgent'
        )
    }
    from(asyncProfilerDistDir) {
        include "**.so"
        include "**.so.sha1"
    }
}

test {
    useJUnitPlatform()
    maxHeapSize = "1g"
    jvmArgs '-XX:MaxMetaspaceSize=512m'
    workingDir = rootDir
    dependsOn shadowJar
    doFirst {
        systemProperty 'shadowJar.path', shadowJar.archiveFile.get().asFile.absolutePath
    }
}

java {
    sourceCompatibility = JavaVersion.VERSION_1_8
    targetCompatibility = JavaVersion.VERSION_1_8
    withJavadocJar()
    withSourcesJar()
}

shadowJar {
    dependsOn copyBootstrapToResources

    exclude 'Log4j-*'
    exclude 'META-INF/org/apache/logging/log4j/**'
    exclude 'META-INF/services/**'

    from(asyncProfilerDistDir) {
        include "**.so"
        include "**.so.sha1"
    }

    archiveFileName = "pyroscope.jar"

    minimize()
    archiveClassifier.set('')
    relocate("com.google",    "io.pyroscope.vendor.com.google")
    relocate("one.profiler",  "io.pyroscope.vendor.one.profiler")
    relocate("okio",  "io.pyroscope.vendor.okio")
    relocate("okhttp3",  "io.pyroscope.vendor.okhttp3")
    relocate("kotlin",  "io.pyroscope.vendor.kotlin")
    relocate("com",  "io.pyroscope.vendor.com")

    dependencies {
        exclude "org/jetbrains/**"
        exclude "org/intellij/**"
        exclude "google/protobuf/**"
    }
}

publishing {
    publications {
        shadow(MavenPublication) { publication ->
            project.shadow.component(publication)
            groupId = 'io.pyroscope'
            artifactId = 'agent'
            version = pyroscopeVersion
            artifacts = [ shadowJar, javadocJar, sourcesJar ]
            pom {
                name = 'Pyroscope Java agent'
                description = 'The Java profiling agent for Pyroscope.io. Based on async-profiler.'
                url = 'https://pyroscope.io'
                licenses {
                    license {
                        name = 'The Apache License, Version 2.0'
                        url = 'http://www.apache.org/licenses/LICENSE-2.0.txt'
                    }
                }
                developers {
                    developer {
                        id = 'pyroscope'
                        name = 'Pyroscope'
                        email = 'anatoly@pyroscope.io'
                    }
                }
                scm {
                    connection = 'scm:git:git://github.com/pyroscope-io/pyroscope-java.git'
                    developerConnection = 'scm:git:ssh://github.com/pyroscope-io/pyroscope-java.git'
                    url = 'https://github.com/pyroscope-io/pyroscope-java'
                }
            }
        }
    }
    repositories {
        maven {
            credentials {
                username project.hasProperty('nexusUsername') ? project.nexusUsername : ''
                password project.hasProperty('nexusPassword') ? project.nexusPassword : ''
            }
            url "https://s01.oss.sonatype.org/service/local/staging/deploy/maven2/"
        }
    }
}

signing {
    sign publishing.publications.shadow
}

afterEvaluate {
    if (project.tasks.findByName('signShadowPublication')) {
        project.tasks.named('signShadowPublication').configure {
            dependsOn 'jar'
            dependsOn 'sourcesJar'
            dependsOn 'javadocJar'
        }
    }
}

generateMetadataFileForShadowPublication.dependsOn 'jar'
```

## File: `agent/jfr_labels.proto`
```
syntax = "proto3";

package io.pyroscope.labels.pb;

message Context {
    map<int64,int64> labels = 1;
}
message LabelsSnapshot {
  map<int64, Context> contexts = 1;
  map<int64, string> strings = 2;
}
```

## File: `agent/src/main/java/io/pyroscope/Preconditions.java`
```java
package io.pyroscope;

import org.jetbrains.annotations.NotNull;
import org.jetbrains.annotations.Nullable;

public final class Preconditions {

    private Preconditions() {
    }

    public static <T> T checkNotNull(@Nullable T reference, @NotNull String paramName) {
        if (reference == null) {
            throw new NullPointerException(paramName + " cannot be null");
        }
        return reference;
    }
}
```

## File: `agent/src/main/java/io/pyroscope/PyroscopeAsyncProfiler.java`
```java
package io.pyroscope;

import one.profiler.AsyncProfiler;

import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStream;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.StandardCopyOption;

public class PyroscopeAsyncProfiler {
    static final String libraryPath;

    static {
        try {
            libraryPath = deployLibrary();
        } catch (final IOException e) {
            throw new RuntimeException(e);
        }
    }

    public static AsyncProfiler getAsyncProfiler() {
        return AsyncProfiler.getInstance(libraryPath);
    }

    /**
     * Extracts the profiler library file from the JAR and puts it in the temp directory.
     *
     * @return path to the extracted library
     */
    private static String deployLibrary() throws IOException {
        final String fileName = libraryFileName();
        final String userName = System.getProperty("user.name");
        final Path targetDir = Files.createTempDirectory(userName + "-pyroscope");

        try (final InputStream is = loadResource(fileName)) {
            final Path target = targetDir.resolve(targetLibraryFileName(fileName)).toAbsolutePath();
            Files.copy(is, target, StandardCopyOption.REPLACE_EXISTING);
            return target.toString();
        }
    }

    /**
     * load resource either from jar resources for production or from local file system for testing
     *
     * @param fileName
     * @return
     * @throws FileNotFoundException
     */
    private static InputStream loadResource(String fileName) throws IOException {
        InputStream res = PyroscopeAsyncProfiler.class.getResourceAsStream("/" + fileName);
        if (res != null) {
            return res; // from shadowJar
        }
        Path filePath = Paths.get("async-profiler-grafana-fork-dist", "lib", fileName);
        return Files.newInputStream(filePath);
    }

    /**
     * Creates the library file name based on the current OS and architecture name.
     */
    private static String libraryFileName() {
        String arch;
        final String osProperty = System.getProperty("os.name");
        final String archProperty = System.getProperty("os.arch");
        switch (osProperty) {
            case "Linux":
                switch (archProperty) {
                    case "amd64":
                        arch = "x64";
                        break;
                    case "aarch64":
                        arch = "arm64";
                        break;

                    default:
                        throw new RuntimeException("Unsupported architecture " + archProperty);
                }

                return "libasyncProfiler-linux-" + arch + ".so";

            case "Mac OS X":
                switch (archProperty) {
                    case "x86_64":
                    case "aarch64":
                        return "libasyncProfiler-macos.so";
                    default:
                        throw new RuntimeException("Unsupported architecture " + archProperty);
                }

            default:
                throw new RuntimeException("Unsupported OS " + osProperty);
        }
    }

    /**
     * <p>Adds the checksum to the library file name.</p>
     *
     * <p>E.g. {@code libasyncProfiler-linux-x64.so} ->
     * {@code libasyncProfiler-linux-x64-7b43b7cc6c864dd729cc7dcdb6e3db8f5ee5b4a4.so}</p>
     */
    private static String targetLibraryFileName(final String libraryFileName) throws IOException {
        if (!libraryFileName.endsWith(".so")) {
            throw new IllegalArgumentException("Incorrect library file name: " + libraryFileName);
        }

        final String checksumFileName = libraryFileName + ".sha1";
        String checksum;
        try (final InputStream is = loadResource(checksumFileName)) {
            byte[] buf = new byte[40];
            int bufLen = is.read(buf);
            if (bufLen <= 0) throw new IOException("checksum read fail");
            checksum = new String(buf, 0, bufLen, StandardCharsets.UTF_8);
        }

        return libraryFileName.substring(0, libraryFileName.length() - 3) + "-" + checksum + ".so";
    }
}
```

## File: `agent/src/main/java/io/pyroscope/http/AggregationType.java`
```java
package io.pyroscope.http;

public enum AggregationType {
    SUM ("sum"),
    AVERAGE ("average");

    /**
    * Pyroscope aggregation type id, as expected by Pyroscope's HTTP API.
    */
    public final String id;

    AggregationType(String id) {
        this.id = id;
    }
}
```

## File: `agent/src/main/java/io/pyroscope/http/Format.java`
```java
package io.pyroscope.http;

public enum Format {
    JFR ("jfr");

    /**
     * Profile data format, as expected by Pyroscope's HTTP API.
     */
    public final String id;

    Format(String id) {
        this.id = id;
    }
}
```

## File: `agent/src/main/java/io/pyroscope/http/Units.java`
```java
package io.pyroscope.http;

public enum Units {
    SAMPLES ("samples"),
    OBJECTS ("objects"),
    BYTES ("bytes");

    /**
    * Pyroscope units id, as expected by Pyroscope's HTTP API.
    */
    public final String id;

    Units(String id) {
        this.id = id;
    }
}
```

## File: `agent/src/main/java/io/pyroscope/javaagent/AsyncProfilerDelegate.java`
```java
package io.pyroscope.javaagent;

import io.pyroscope.http.Format;
import io.pyroscope.javaagent.config.Config;
import io.pyroscope.PyroscopeAsyncProfiler;
import io.pyroscope.labels.v2.Pyroscope;
import one.profiler.AsyncProfiler;
import one.profiler.Counter;
import org.jetbrains.annotations.NotNull;

import java.io.DataInputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.time.Duration;
import java.time.Instant;


import static io.pyroscope.Preconditions.checkNotNull;

public final class AsyncProfilerDelegate implements ProfilerDelegate {
    private Config config;
    private EventType eventType;
    private String alloc;
    private String lock;
    private Duration interval;
    private Format format;
    private File tempJFRFile;

    private final AsyncProfiler instance = PyroscopeAsyncProfiler.getAsyncProfiler();

    public AsyncProfilerDelegate(@NotNull Config config) {
        setConfig(config);
    }

    @Override
    public void setConfig(@NotNull final Config config) {
        checkNotNull(config, "config");
        this.config = config;
        this.alloc = config.profilingAlloc;
        this.lock = config.profilingLock;
        this.eventType = config.profilingEvent;
        this.interval = config.profilingInterval;
        this.format = config.format;

        if (format == Format.JFR && null == tempJFRFile) {
            try {
                // flight recorder is built on top of a file descriptor, so we need a file.
                tempJFRFile = File.createTempFile("pyroscope", ".jfr");
                tempJFRFile.deleteOnExit();
            } catch (IOException e) {
                throw new IllegalStateException(e);
            }
        }
    }

    /**
     * Start async-profiler
     */
    @Override
    public synchronized void start() {
        if (format == Format.JFR) {
            try {
                instance.execute(createJFRCommand());
            } catch (IOException e) {
                throw new IllegalStateException(e);
            }
        } else {
            instance.start(eventType.id, interval.toNanos());
        }
    }

    /**
     * Stop async-profiler
     */
    @Override
    public synchronized void stop() {
        instance.stop();
    }

    /**
     * @param started - time when profiling has been started
     * @param ended   - time when profiling has ended
     * @return Profiling data and dynamic labels as {@link Snapshot}
     */
    @Override
    @NotNull
    public synchronized Snapshot dumpProfile(@NotNull Instant started, @NotNull Instant ended) {
        return dumpImpl(started, ended);
    }

    private String createJFRCommand() {
        StringBuilder sb = new StringBuilder();
        sb.append("start,event=").append(eventType.id);
        if (alloc != null && !alloc.isEmpty()) {
            sb.append(",alloc=").append(alloc);
            if (config.allocLive) {
                sb.append(",live");
            }
        }
        if (lock != null && !lock.isEmpty()) {
            sb.append(",lock=").append(lock);
        }
        sb.append(",interval=").append(interval.toNanos())
                .append(",file=").append(tempJFRFile.toString());
        if (config.APLogLevel != null) {
            sb.append(",loglevel=").append(config.APLogLevel);
        }
        sb.append(",jstackdepth=").append(config.javaStackDepthMax);
        if (config.APExtraArguments != null) {
            sb.append(",").append(config.APExtraArguments);
        }
        return sb.toString();
    }

    private Snapshot dumpImpl(Instant started, Instant ended) {
        if (config.gcBeforeDump) {
            System.gc();
        }
        final byte[] data;
        if (format == Format.JFR) {
            data = dumpJFR();
        } else {
            data = instance.dumpCollapsed(Counter.SAMPLES).getBytes(StandardCharsets.UTF_8);
        }
        return new Snapshot(
                format,
                eventType,
                started,
                ended,
                data,
                Pyroscope.LabelsWrapper.dump()
        );
    }

    private byte[] dumpJFR() {
        try {
            byte[] bytes = new byte[(int) tempJFRFile.length()];
            try (DataInputStream ds = new DataInputStream(new FileInputStream(tempJFRFile))) {
                ds.readFully(bytes);
            }
            return bytes;
        } catch (IOException e) {
            throw new IllegalStateException(e);
        }
    }
}
```

## File: `agent/src/main/java/io/pyroscope/javaagent/BootstrapApiInjector.java`
```java
package io.pyroscope.javaagent;

import io.pyroscope.javaagent.api.Logger;
import io.pyroscope.javaagent.impl.DefaultLogger;

import java.io.IOException;
import java.io.InputStream;
import java.lang.instrument.Instrumentation;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.StandardCopyOption;
import java.util.jar.JarFile;

/**
 * Injects the shared bootstrap-api classes (ProfilerApi, ProfilerApiHolder, ProfilerScopedContext)
 * into the bootstrap classloader at agent startup.
 *
 * <p>This ensures that both the agent classloader and any application classloader resolve the same
 * ProfilerApiHolder class with the same static fields, enabling cross-classloader communication
 * (e.g., with the OTel extension).
 *
 * <p>The bootstrap-api JAR is embedded as a resource ({@code pyroscope-bootstrap.jar.bin}) inside
 * pyroscope.jar. It uses a {@code .bin} extension to prevent the shadow jar plugin from
 * merging or relocating its contents.
 *
 * <p>There are two places that perform this injection:
 * <ul>
 *   <li>Here, in the agent premain ({@code PyroscopeAgent.premain})</li>
 *   <li>In the otel-profiling-java extension ({@code io.otel.pyroscope.BootstrapApiInjector})</li>
 * </ul>
 * Whichever runs first injects the classes; the second call is a no-op since the classes
 * are already on the bootstrap classloader.
 */
class BootstrapApiInjector {

    private static final String RESOURCE_NAME = "/pyroscope-bootstrap.jar.bin";

    static void inject(Instrumentation instrumentation) {
        try {
            try (InputStream is = BootstrapApiInjector.class.getResourceAsStream(RESOURCE_NAME)) {
                if (is == null) {
                    DefaultLogger.PRECONFIG_LOGGER.log(Logger.Level.WARN,
                        "BootstrapApiInjector: %s not found in resources, skipping bootstrap injection",
                        RESOURCE_NAME);
                    return;
                }
                Path tempJar = Files.createTempFile("pyroscope-bootstrap-", ".jar");
                tempJar.toFile().deleteOnExit();
                Files.copy(is, tempJar, StandardCopyOption.REPLACE_EXISTING);

                instrumentation.appendToBootstrapClassLoaderSearch(new JarFile(tempJar.toFile()));
                DefaultLogger.PRECONFIG_LOGGER.log(Logger.Level.DEBUG,
                    "BootstrapApiInjector: Injected API classes into bootstrap classloader");
            }
        } catch (IOException e) {
            DefaultLogger.PRECONFIG_LOGGER.log(Logger.Level.ERROR,
                "BootstrapApiInjector: Failed to inject bootstrap API: %s", e);
        }
    }
}
```

## File: `agent/src/main/java/io/pyroscope/javaagent/CurrentPidProvider.java`
```java
package io.pyroscope.javaagent;

import sun.management.VMManagement;

import java.lang.management.ManagementFactory;
import java.lang.management.RuntimeMXBean;
import java.lang.reflect.Field;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;

/**
 * Hacky implementation of JVM process id (pid) handler, only used with JDK 8 implementation of {@link JFRJCMDProfilerDelegate}
 */
public final class CurrentPidProvider {
    public static long getCurrentProcessId() {
        RuntimeMXBean runtime = ManagementFactory.getRuntimeMXBean();
        Field jvm = null;
        try {
            jvm = runtime.getClass().getDeclaredField("jvm");
            jvm.setAccessible(true);

            VMManagement management = (VMManagement) jvm.get(runtime);
            Method method = management.getClass().getDeclaredMethod("getProcessId");
            method.setAccessible(true);

            return (Integer) method.invoke(management);
        } catch (NoSuchFieldException | InvocationTargetException | IllegalAccessException | NoSuchMethodException e) {
            throw new RuntimeException(e);
        }
    }
}
```

## File: `agent/src/main/java/io/pyroscope/javaagent/EventType.java`
```java
package io.pyroscope.javaagent;

import java.util.EnumSet;
import java.util.Optional;

import one.profiler.Events;
import io.pyroscope.http.Units;
import io.pyroscope.http.AggregationType;

public enum EventType {
    CPU (Events.CPU, Units.SAMPLES, AggregationType.SUM),
    ALLOC (Events.ALLOC, Units.OBJECTS, AggregationType.SUM),
    LOCK (Events.LOCK, Units.SAMPLES, AggregationType.SUM),
    WALL (Events.WALL, Units.SAMPLES, AggregationType.SUM),
    CTIMER (Events.CTIMER, Units.SAMPLES, AggregationType.SUM),
    ITIMER (Events.ITIMER, Units.SAMPLES, AggregationType.SUM);

    /**
    * Event type id, as defined in one.profiler.Events.
    */
    public final String id;

    /**
    * Unit option, as expected by Pyroscope's HTTP API.
    */
    public final Units units;

    /**
    * Aggregation type option, as expected by Pyroscope's HTTP API.
    */
    public final AggregationType aggregationType;

    EventType(String id, Units units, AggregationType aggregationType) {
        this.id = id;
        this.units = units;
        this.aggregationType = aggregationType;
    }

    public static EventType fromId(String id) throws IllegalArgumentException {
        Optional<EventType> maybeEventType =
            EnumSet.allOf(EventType.class)
            .stream()
            .filter(eventType -> eventType.id.equals(id))
            .findAny();
        return maybeEventType.orElseThrow(IllegalArgumentException::new);
    }
}
```

## File: `agent/src/main/java/io/pyroscope/javaagent/JFRJCMDProfilerDelegate.java`
```java
package io.pyroscope.javaagent;

import io.pyroscope.http.Format;
import io.pyroscope.javaagent.config.Config;
import io.pyroscope.labels.v2.Pyroscope;

import java.io.BufferedReader;
import java.io.File;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.UncheckedIOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.StandardCopyOption;
import java.time.Instant;
import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

import static java.lang.String.format;

/**
 * This implementation of JFR profiler, uses external <code>jcmd</code> command to manage JFR recordings.
 * This only to be used with JDK 8.
 * <p>
 * NOTE: This is an experimental feature and is subject to API changes or may be removed in future releases.
 */
public final class JFRJCMDProfilerDelegate implements ProfilerDelegate {
    private static final String RECORDING_NAME = "pyroscope";
    private static final String JFR_SETTINGS_RESOURCE = "/jfr/pyroscope.jfc";

    private static final String OS_NAME = "os.name";
    private Config config;
    private File tempJFRFile;
    private Path jcmdBin;
    private Path jfrSettingsPath;

    public JFRJCMDProfilerDelegate(Config config) {
        setConfig(config);
    }

    @Override
    public void setConfig(final Config config) {
        this.config = config;
        jcmdBin = findJcmdBin();
        jfrSettingsPath = findJfrSettingsPath(config);

        try {
            tempJFRFile = File.createTempFile("pyroscope", ".jfr");
            tempJFRFile.deleteOnExit();
        } catch (IOException e) {
            throw new IllegalStateException(e);
        }
    }

    /**
     * Start JFR profiler
     */
    @Override
    public synchronized void start() {
        List<String> cmdLine = new ArrayList<>();
        cmdLine.add(jcmdBin.toString());
        cmdLine.add(String.valueOf(CurrentPidProvider.getCurrentProcessId()));
        cmdLine.add("JFR.start");
        cmdLine.add("name=" + RECORDING_NAME);
        cmdLine.add("filename=" + tempJFRFile.getAbsolutePath());
        cmdLine.add("settings=" + jfrSettingsPath);
        executeCmd(cmdLine);
    }

    /**
     * Stop JFR profiler
     */
    @Override
    public synchronized void stop() {
        List<String> cmdLine = new ArrayList<>();
        cmdLine.add(jcmdBin.toString());
        cmdLine.add(String.valueOf(CurrentPidProvider.getCurrentProcessId()));
        cmdLine.add("JFR.stop");
        cmdLine.add("name=" + RECORDING_NAME);
        executeCmd(cmdLine);
    }

    /**
     * @param started - time when profiling has been started
     * @param ended   - time when profiling has ended
     * @return Profiling data and dynamic labels as {@link Snapshot}
     */
    @Override
    public synchronized Snapshot dumpProfile(Instant started, Instant ended) {
        return dumpImpl(started, ended);
    }

    private Snapshot dumpImpl(Instant started, Instant ended) {
        if (config.gcBeforeDump) {
            System.gc();
        }
        try {
            byte[] data = Files.readAllBytes(tempJFRFile.toPath());
            return new Snapshot(
                Format.JFR,
                EventType.CPU,
                started,
                ended,
                data,
                Pyroscope.LabelsWrapper.dump()
            );
        } catch (IOException e) {
            throw new IllegalStateException(e);
        }
    }

    private static Path findJcmdBin() {
        Path javaHome = Paths.get(System.getProperty("java.home"));
        String jcmd = jcmdExecutable();
        Path jcmdBin = javaHome.resolve("bin").resolve(jcmd);
        //find jcmd binary
        if (!Files.isExecutable(jcmdBin)) {
            jcmdBin = javaHome.getParent().resolve("bin").resolve(jcmd);
            if (!Files.isExecutable(jcmdBin)) {
                throw new RuntimeException("cannot find executable jcmd in Java home");
            }
        }
        return jcmdBin;
    }

    private static String jcmdExecutable() {
        String jcmd = "jcmd";
        if (isWindowsOS()) {
            jcmd = "jcmd.exe";
        }
        return jcmd;
    }

    private static Path findJfrSettingsPath(Config config) {
        // first try to load settings from provided configuration
        if (config.jfrProfilerSettings != null) {
            return Paths.get(config.jfrProfilerSettings);
        }
        // otherwise load default settings
        try (InputStream inputStream = JFRJCMDProfilerDelegate.class.getResourceAsStream(JFR_SETTINGS_RESOURCE)) {
            Path jfrSettingsPath = Files.createTempFile("pyroscope", ".jfc");
            Files.copy(inputStream, jfrSettingsPath, StandardCopyOption.REPLACE_EXISTING);
            return jfrSettingsPath;
        } catch (IOException e) {
            throw new UncheckedIOException(format("unable to load %s from classpath", JFR_SETTINGS_RESOURCE), e);
        }
    }

    private static boolean isWindowsOS() {
        String osName = System.getProperty(OS_NAME);
        return osName.contains("Windows");
    }

    private static void executeCmd(List<String> cmdLine) {
        try {
            ProcessBuilder processBuilder = new ProcessBuilder(cmdLine);
            Process process = processBuilder.redirectErrorStream(true).start();
            int exitCode = process.waitFor();
            if (exitCode != 0) {
                String processOutput = new BufferedReader(new InputStreamReader(process.getInputStream())).lines().collect(Collectors.joining("\n"));
                throw new RuntimeException(format("Invalid exit code %s, process output %s", exitCode, processOutput));
            }
        } catch (IOException | InterruptedException e) {
            throw new RuntimeException(format("failed to start process: %s", cmdLine), e);
        }
    }

}
```

## File: `agent/src/main/java/io/pyroscope/javaagent/JFRJDKProfilerDelegate.java`
```java
package io.pyroscope.javaagent;

import io.pyroscope.http.Format;
import io.pyroscope.javaagent.config.Config;
import jdk.jfr.Recording;

import java.io.File;
import java.io.IOException;
import java.io.UncheckedIOException;
import java.nio.file.Files;
import java.time.Duration;
import java.time.Instant;
import java.time.temporal.ChronoUnit;
import java.util.Optional;

import static io.pyroscope.labels.v2.Pyroscope.*;
import static java.lang.String.format;

/**
 * This implementation of JFR profiler, uses JDK JFR APi to manage JFR recordings.
 * This only to be used with JDK 9 and above.
 * <p>
 * NOTE: This is an experimental feature and is subject to API changes or may be removed in future releases.
 */
public final class JFRJDKProfilerDelegate implements ProfilerDelegate {
    private static final Duration DEFAULT_LOCK_INTERVAL = Duration.ofNanos(10000);    // 10 us

    private Config config;
    private File tempJFRFile;
    private Recording recording;

    public JFRJDKProfilerDelegate(Config config) {
        setConfig(config);
    }

    @Override
    public void setConfig(final Config config) {
        this.config = config;
        try {
            tempJFRFile = jfrRecordingPath();
        } catch (IOException e) {
            throw new UncheckedIOException("cannot create JFR destination path", e);
        }
    }

    private static File jfrRecordingPath() throws IOException {
        File tempJFRFile = File.createTempFile("pyroscope", ".jfr");
        tempJFRFile.deleteOnExit();
        return tempJFRFile;
    }

    /**
     * Start JFR profiler
     */
    @Override
    public synchronized void start() {
        try {
            recording = new Recording();
            switch (config.profilingEvent) {
                case CPU: {
                    recording.enable("jdk.ExecutionSample")
                        .withPeriod(config.profilingInterval)
                        .withStackTrace();
                    break;
                }
                case ALLOC: {
                    recording.enable("jdk.ObjectAllocationInNewTLAB")
                        .withPeriod(config.profilingInterval)
                        .withStackTrace();
                    recording.enable("jdk.ObjectAllocationOutsideTLAB")
                        .withPeriod(config.profilingInterval)
                        .withStackTrace();
                    break;
                }
                case LOCK: {
                    Duration lockDuration = parseDuration(config.profilingLock, DEFAULT_LOCK_INTERVAL);
                    recording.enable("jdk.ThreadPark")
                        .withThreshold(lockDuration)
                        .withPeriod(config.profilingInterval)
                        .withStackTrace();
                    recording.enable("jdk.JavaMonitorEnter")
                        .withThreshold(lockDuration)
                        .withPeriod(config.profilingInterval)
                        .withStackTrace();
                    break;
                }
                default:
                    throw new IllegalArgumentException(format("Unsupported event type: %s", config.profilingEvent));
            }
            recording.setToDisk(true);
            recording.setDestination(tempJFRFile.toPath());
            recording.start();
        } catch (IOException e) {
            throw new UncheckedIOException("cannot start JFR recording", e);
        }
    }

    // this based on async-profiler parsing logic so we can things compatible
    private static Duration parseDuration(String str, Duration defaultValue) {
        if (str == null || str.trim().isEmpty()) {
            return defaultValue;
        }

        // find where the numeric part ends
        int endIndex = 0;
        while (endIndex < str.length()) {
            char c = str.charAt(endIndex);
            if (!Character.isDigit(c) && c != '-' && c != '+') {
                break;
            }
            endIndex++;
        }

        if (endIndex == 0) {
            throw new IllegalArgumentException(format("Invalid duration: %s", str));
        }

        // parse the numeric part
        long result;
        try {
            String numericPart = str.substring(0, endIndex);
            result = Long.parseLong(numericPart);
        } catch (NumberFormatException e) {
            throw new IllegalArgumentException("Invalid duration: " + str, e);
        }

        // If no unit suffix, return the numeric value
        if (endIndex >= str.length()) {
            return Duration.of(result, ChronoUnit.NANOS);
        }

        // Get the unit character and convert to lowercase
        char unitChar = Character.toLowerCase(str.charAt(endIndex));

        switch (unitChar) {
            case 'n':
                return Duration.of(result, ChronoUnit.NANOS);
            case 'u':
                return Duration.of(result, ChronoUnit.MICROS);
            case 'm':
                return Duration.of(result, ChronoUnit.MILLIS);
            case 's':
                return Duration.of(result, ChronoUnit.SECONDS);
            default:
                throw new IllegalArgumentException(format("Invalid duration unit: %s", unitChar));
        }
    }

    /**
     * Stop JFR profiler
     */
    @Override
    public synchronized void stop() {
        recording.stop();
    }

    /**
     * @param started - time when profiling has been started
     * @param ended   - time when profiling has ended
     * @return Profiling data and dynamic labels as {@link Snapshot}
     */
    @Override
    public synchronized Snapshot dumpProfile(Instant started, Instant ended) {
        return dumpImpl(started, ended);
    }

    private Snapshot dumpImpl(Instant started, Instant ended) {
        if (config.gcBeforeDump) {
            System.gc();
        }
        try {
            byte[] data = Files.readAllBytes(tempJFRFile.toPath());
            return new Snapshot(
                Format.JFR,
                config.profilingEvent,
                started,
                ended,
                data,
                LabelsWrapper.dump()
            );
        } catch (IOException e) {
            throw new IllegalStateException(e);
        }
    }

}
```

## File: `agent/src/main/java/io/pyroscope/javaagent/JFRProfilerDelegate.java`
```java
package io.pyroscope.javaagent;

import io.pyroscope.javaagent.config.Config;
import io.pyroscope.javaagent.impl.DefaultLogger;

import java.time.Instant;

import static java.lang.String.format;

/**
 * This is a JFR profiler delegate, which checks JVM version and registers proper delegate implementation.
 * <p>
 * NOTE: This is an experimental feature and is subject to API changes or may be removed in future releases.
 */
public final class JFRProfilerDelegate implements ProfilerDelegate {

    private ProfilerDelegate delegate;

    public JFRProfilerDelegate(Config config) {
        String javaVersion = System.getProperty("java.version");
        if (javaVersion.startsWith("1.8")) {
            delegate = new JFRJCMDProfilerDelegate(config);
        } else {
            delegate = new JFRJDKProfilerDelegate(config);
        }
    }

    @Override
    public void setConfig(final Config config) {
        delegate.setConfig(config);
    }

    /**
     * Start JFR profiler
     */
    @Override
    public synchronized void start() {
        delegate.start();
    }

    /**
     * Stop JFR profiler
     */
    @Override
    public synchronized void stop() {
        delegate.stop();
    }

    /**
     * @param started - time when profiling has been started
     * @param ended   - time when profiling has ended
     * @return Profiling data and dynamic labels as {@link Snapshot}
     */
    @Override
    public synchronized Snapshot dumpProfile(Instant started, Instant ended) {
        return delegate.dumpProfile(started, ended);
    }

}
```

## File: `agent/src/main/java/io/pyroscope/javaagent/OverfillQueue.java`
```java
package io.pyroscope.javaagent;

import java.util.concurrent.ArrayBlockingQueue;
import java.util.concurrent.locks.Condition;
import java.util.concurrent.locks.ReentrantLock;

/**
 * <p>A blocking queue with a limited capacity.</p>
 *
 * <p>When the queue is attempted to put a new element and is overfilled, the oldest element is dropped
 * so the capacity limit is preserved.</p>
 *
 * @param <E> the type of elements.
 */
public final class OverfillQueue<E> {
    private final ArrayBlockingQueue<E> innerQueue;
    // Guards innerQueue.
    private final ReentrantLock lock = new ReentrantLock(false);
    private final Condition notEmpty = lock.newCondition();

    public OverfillQueue(final int capacity) {
        if (capacity < 1) {
            throw new IllegalArgumentException("Capacity must be >= 1");
        }
        this.innerQueue = new ArrayBlockingQueue<>(capacity);
    }

    /**
     * Inserts the specified element at the tail of this queue if it is
     * possible to do so without exceeding the queue's capacity. If not,
     * drops one element from the head of the queue.
     */
    public void put(final E element) throws InterruptedException {
        lock.lockInterruptibly();
        try {
            boolean offerSuccessful = innerQueue.offer(element);
            if (offerSuccessful) {
                notEmpty.signal();
            } else {
                // Drop one old element to ensure the capacity for the new one.
                innerQueue.poll();
                offerSuccessful = innerQueue.offer(element);
                if (offerSuccessful) {
                    notEmpty.signal();
                } else {
                    // Doing this as a sanity check.
                    throw new RuntimeException("innerQueue.offer was not successful");
                }
            }
        } finally {
            lock.unlock();
        }
    }

    /**
     * Retrieves and removes the head of this queue, waiting for the element to become available if needed.
     */
    public E take() throws InterruptedException {
        lock.lockInterruptibly();
        try {
            E result;
            while ((result = innerQueue.poll()) == null) {
                notEmpty.await();
            }
            return result;
        } finally {
            lock.unlock();
        }
    }
}
```

## File: `agent/src/main/java/io/pyroscope/javaagent/ProfilerDelegate.java`
```java
package io.pyroscope.javaagent;

import io.pyroscope.javaagent.config.Config;
import org.jetbrains.annotations.NotNull;
import io.pyroscope.javaagent.config.ProfilerType;

import java.time.Instant;

public interface ProfilerDelegate {
    /**
     * Creates profiler delegate instance based on configuration.
     *
     * @param config
     * @return
     */
    static ProfilerDelegate create(Config config) {
        return config.profilerType.create(config);
    }

    void start();

    void stop();

    @NotNull
    Snapshot dumpProfile(@NotNull Instant profilingStartTime, @NotNull Instant now);

    void setConfig(@NotNull Config config);
}
```

## File: `agent/src/main/java/io/pyroscope/javaagent/ProfilerSdk.java`
```java
package io.pyroscope.javaagent;

import io.pyroscope.PyroscopeAsyncProfiler;
import io.pyroscope.javaagent.api.ProfilerScopedContext;
import io.pyroscope.javaagent.api.ProfilerApi;
import io.pyroscope.javaagent.config.Config;
import io.pyroscope.javaagent.impl.ProfilerScopedContextWrapper;
import io.pyroscope.labels.v2.LabelsSet;
import io.pyroscope.labels.v2.Pyroscope;
import io.pyroscope.labels.v2.ScopedContext;
import one.profiler.AsyncProfiler;
import org.jetbrains.annotations.NotNull;

import java.util.Map;

public class ProfilerSdk implements ProfilerApi {

    private final AsyncProfiler asprof;

    public ProfilerSdk() {
        this.asprof = PyroscopeAsyncProfiler.getAsyncProfiler();
    }
    @Override
    public void startProfiling() {
        PyroscopeAgent.start(Config.build());
    }

    @Override
    public boolean isProfilingStarted() {
        return PyroscopeAgent.isStarted();
    }

    @Deprecated
    @Override
    @NotNull
    public ProfilerScopedContext createScopedContext(@NotNull Map<@NotNull String, @NotNull String> labels) {
        return new ProfilerScopedContextWrapper(new ScopedContext(new LabelsSet(labels)));
    }

    @Override
    public void setTracingContext(long spanId, long spanName) {
        asprof.setTracingContext(spanId, spanName);
    }

    @Override
    public long registerConstant(String constant) {
        return Pyroscope.LabelsWrapper.registerConstant(constant);
    }
}
```

## File: `agent/src/main/java/io/pyroscope/javaagent/PyroscopeAgent.java`
```java
package io.pyroscope.javaagent;

import io.pyroscope.javaagent.api.ProfilerApi;
import io.pyroscope.javaagent.api.ProfilerApiHolder;
import io.pyroscope.javaagent.api.Exporter;
import io.pyroscope.javaagent.api.Logger;
import io.pyroscope.javaagent.ProfilerSdk;
import io.pyroscope.javaagent.api.ProfilingScheduler;
import io.pyroscope.javaagent.config.Config;
import io.pyroscope.javaagent.impl.*;
import io.pyroscope.labels.v2.ScopedContext;
import org.jetbrains.annotations.NotNull;

import java.lang.instrument.Instrumentation;

import static io.pyroscope.Preconditions.checkNotNull;

public class PyroscopeAgent {
    private static final Object sLock = new Object();
    private static Options sOptions = null;

    public static void premain(final String agentArgs,
                               final Instrumentation inst) {
        // Inject bootstrap-api classes into the bootstrap classloader BEFORE any code
        // references ProfilerApiHolder. This ensures cross-classloader visibility.
        BootstrapApiInjector.inject(inst);

        final Config config;
        try {
            config = Config.build(DefaultConfigurationProvider.INSTANCE);
            DefaultLogger.PRECONFIG_LOGGER.log(Logger.Level.DEBUG, "Config: %s", config);
        } catch (final Throwable e) {
            DefaultLogger.PRECONFIG_LOGGER.log(Logger.Level.ERROR, "Error starting profiler %s", e);
            return;
        }
        start(config);
    }

    public static void start() {
        start(new Config.Builder().build());
    }

    public static void start(@NotNull Config config) {
        checkNotNull(config, "config");
        start(new Options.Builder(config).build());
    }

    public static void start(@NotNull Options options) {
        checkNotNull(options, "options");

        synchronized (sLock) {
            Logger logger = options.logger;

            if (!options.config.agentEnabled) {
                logger.log(Logger.Level.INFO, "Pyroscope agent start disabled by configuration");
                return;
            }

            if (sOptions != null) {
                logger.log(Logger.Level.ERROR, "Failed to start profiling - already started");
                return;
            }
            sOptions = options;
            logger.log(Logger.Level.DEBUG, "Config: %s", options.config);
            try {
                options.scheduler.start(options.profiler);
                ScopedContext.ENABLED.set(true);
                logger.log(Logger.Level.INFO, "Profiling started");
                publishProfilerApi(logger);
            } catch (final Throwable e) {
                logger.log(Logger.Level.ERROR, "Error starting profiler %s", e);
                sOptions = null;
            }
        }
    }

    private static void publishProfilerApi(Logger logger) {
        try {
            ProfilerApi api = new ProfilerSdk();
            ProfilerApi existing = ProfilerApiHolder.INSTANCE.get();
            if (existing != null && existing.isProfilingStarted()
                    && existing.getClass().getClassLoader() != api.getClass().getClassLoader()) {
                logger.log(Logger.Level.ERROR,
                        "Another ProfilerApi instance is already active from a different classloader. " +
                        "Starting profiling from multiple classloaders is not supported and may produce incorrect results. " +
                        "See https://github.com/grafana/otel-profiling-java/issues/76");
            }
            ProfilerApiHolder.INSTANCE.set(api);
            logger.log(Logger.Level.DEBUG, "published profiler sdk");
        } catch (Throwable th) {
            logger.log(Logger.Level.DEBUG, "publish profiler failed %s", th);
        }
    }

    public static void stop() {
        ScopedContext.ENABLED.set(false);
        synchronized (sLock) {
            if (sOptions == null) {
                DefaultLogger.PRECONFIG_LOGGER.log(Logger.Level.ERROR, "Error stopping profiler: not started");
                return;
            }
            try {
                sOptions.scheduler.stop();
                sOptions.exporter.stop();
                sOptions.logger.log(Logger.Level.INFO, "Profiling stopped");
            } catch (Throwable e) {
                sOptions.logger.log(Logger.Level.ERROR, "Error stopping profiler %s", e);
            }

            sOptions = null;
        }
    }

    public static boolean isStarted() {
        synchronized (sLock) {
            return sOptions != null;
        }
    }

    /**
     * Options allow to swap pyroscope components:
     * - io.pyroscope.javaagent.api.ProfilingScheduler
     * - org.apache.logging.log4j.Logger
     * - io.pyroscope.javaagent.api.Exporter for io.pyroscope.javaagent.impl.ContinuousProfilingScheduler
     */
    public static class Options {
        final Config config;
        final ProfilingScheduler scheduler;
        final Logger logger;
        final ProfilerDelegate profiler;
        final Exporter exporter;

        private Options(@NotNull Builder b) {
            this.config = b.config;
            this.profiler = b.profiler;
            this.scheduler = b.scheduler;
            this.logger = b.logger;
            this.exporter = b.exporter;
        }

        public static class Builder {
            private final Config config;
            private ProfilerDelegate profiler;
            private Exporter exporter;
            private ProfilingScheduler scheduler;
            private Logger logger;

            public Builder(@NotNull Config config) {
                checkNotNull(config, "config");
                this.config = config;
            }

            public Builder setExporter(@NotNull Exporter exporter) {
                checkNotNull(exporter, "exporter");
                this.exporter = exporter;
                return this;
            }

            public Builder setScheduler(@NotNull ProfilingScheduler scheduler) {
                checkNotNull(scheduler, "scheduler");
                this.scheduler = scheduler;
                return this;
            }

            public Builder setLogger(@NotNull Logger logger) {
                checkNotNull(logger, "logger");
                this.logger = logger;
                return this;
            }

            public Builder setProfiler(@NotNull ProfilerDelegate profiler) {
                checkNotNull(profiler, "logger");
                this.profiler = profiler;
                return this;
            }

            public @NotNull Options build() {
                if (logger == null) {
                    logger = new DefaultLogger(config.logLevel, System.err);
                }
                if (scheduler == null) {
                    if (exporter == null) {
                        exporter = new QueuedExporter(config, new PyroscopeExporter(config, logger), logger);
                    }
                    if (config.samplingDuration == null) {
                        scheduler = new ContinuousProfilingScheduler(config, exporter, logger);
                    } else {
                        scheduler = new SamplingProfilingScheduler(config, exporter, logger);
                    }
                }
                if (profiler == null) {
                    profiler = ProfilerDelegate.create(config);
                }
                return new Options(this);
            }
        }
    }
}
```

## File: `agent/src/main/java/io/pyroscope/javaagent/Snapshot.java`
```java
package io.pyroscope.javaagent;

import io.pyroscope.http.Format;
import io.pyroscope.labels.pb.*;

import java.time.Instant;

public final class Snapshot {
    public final Format format;
    public final EventType eventType;
    public final Instant started;
    public final Instant ended;
    public final byte[] data;
    public final JfrLabels.LabelsSnapshot labels;

    public Snapshot(Format format, final EventType eventType, final Instant started, final Instant ended,final byte[] data, JfrLabels.LabelsSnapshot labels) {
        this.format = format;
        this.eventType = eventType;
        this.started = started;
        this.ended = ended;
        this.data = data;
        this.labels = labels;
    }
}
```

## File: `agent/src/main/java/io/pyroscope/javaagent/api/ConfigurationProvider.java`
```java
package io.pyroscope.javaagent.api;

import org.jetbrains.annotations.NotNull;
import org.jetbrains.annotations.Nullable;

public interface ConfigurationProvider {
    @Nullable
    String get(@NotNull String key);
}
```

## File: `agent/src/main/java/io/pyroscope/javaagent/api/Exporter.java`
```java
package io.pyroscope.javaagent.api;

import io.pyroscope.javaagent.Snapshot;
import org.jetbrains.annotations.NotNull;

public interface Exporter {
    /**
     * PyroscopeAgent expects {@link Exporter#export(Snapshot)} method to be synchronous to profiling schedule, and should return as fast as
     * possible. <br>See QueuedExporter for an asynchronous implementation example.<br>
     * Here is an example of an alternative to {@link io.pyroscope.javaagent.impl.PyroscopeExporter}
     * <pre>
     * class KafkaExporter implements Exporter {
     *     final KafkaProducer&#060;String, String&#062; kafkaProducer;
     *     private MyExporter(KafkaProducer&#060;String, String&#062; producer) {
     *         this.kafkaProducer = producer;
     *     }
     *     &#064;Override
     *     public void export(Snapshot snapshot) {
     *         kafkaProducer.send(new ProducerRecord&#060;&#062;("test.app.jfr", gson.toJson(snapshot)));
     *     }
     * }
     * </pre>
     *
     */
    void export(@NotNull Snapshot snapshot);

    /**
     * Stop the resources that are held by the exporter like Threads and so on...
     */
    void stop();
}
```

## File: `agent/src/main/java/io/pyroscope/javaagent/api/Logger.java`
```java
package io.pyroscope.javaagent.api;

public interface Logger {
    enum Level {
        DEBUG(0),
        INFO(1),
        WARN(2),
        ERROR(3);
        public final int level;

        Level(int level) {
            this.level = level;
        }
    }

    void log(Level l, String msg, Object... args);
}
```

## File: `agent/src/main/java/io/pyroscope/javaagent/api/ProfilerApi.java`
```java
package io.pyroscope.javaagent.api;

import org.jetbrains.annotations.NotNull;

import java.util.Map;

/**
 * Shared profiling interface for cross-classloader communication between the Pyroscope agent
 * and the OTel extension. The bootstrap-api jar is injected into the bootstrap classloader
 * by the OTel extension at startup, making this interface visible to both classloaders.
 *
 * <p>Any modification to this interface is a <b>breaking change</b> that requires a coordinated
 * release of both pyroscope-java and otel-profiling-java.
 */
public interface ProfilerApi {
    void startProfiling();

    boolean isProfilingStarted();

    @Deprecated
    @NotNull ProfilerScopedContext createScopedContext(@NotNull Map<@NotNull String, @NotNull String> labels);

    void setTracingContext(long spanId, long spanName);

    long registerConstant(String constant);
}
```

## File: `agent/src/main/java/io/pyroscope/javaagent/api/ProfilerApiHolder.java`
```java
package io.pyroscope.javaagent.api;

import java.util.concurrent.atomic.AtomicReference;

/**
 * Cross-classloader rendezvous point for the Pyroscope profiling API. The bootstrap-api jar
 * is injected into the bootstrap classloader by the OTel extension at startup
 * (via {@link java.lang.instrument.Instrumentation#appendToBootstrapClassLoaderSearch}),
 * making this holder visible to both the extension and application classloaders.
 *
 * <p>The logic of setting this instance:
 * <ol>
 *   <li>{@code PyroscopeAgent#start} sets an instance unconditionally.</li>
 *   <li>OTel extension does not overwrite an already-set instance.</li>
 *   <li>OTel extension sets an instance from the system classloader if possible.</li>
 *   <li>OTel extension sets an instance of the vendored/extension classloader ProfilerSdk
 *       if the system classloader is not available.</li>
 * </ol>
 *
 * <p>Any modification to this class is a <b>breaking change</b> that requires a coordinated
 * release of both pyroscope-java and otel-profiling-java.
 */
public class ProfilerApiHolder {
    public static final AtomicReference<ProfilerApi> INSTANCE = new AtomicReference<>();
}
```

## File: `agent/src/main/java/io/pyroscope/javaagent/api/ProfilerScopedContext.java`
```java
package io.pyroscope.javaagent.api;

import org.jetbrains.annotations.NotNull;

import java.util.function.BiConsumer;

/**
 * Injected into the bootstrap classloader by the OTel extension at startup.
 * This interface MUST be kept in sync with the copy in pyroscope-java (same package, same
 * method signatures) — do not modify without updating both repos.
 *
 * <p>Any modification to this interface is a <b>breaking change</b> that requires a major release
 * of both pyroscope-java and otel-profiling-java, with release notes documenting the
 * incompatibility between old and new versions.
 */
public interface ProfilerScopedContext {
    void forEachLabel(@NotNull BiConsumer<@NotNull String, @NotNull String> consumer);
    void close();
}
```

## File: `agent/src/main/java/io/pyroscope/javaagent/api/ProfilingScheduler.java`
```java
package io.pyroscope.javaagent.api;

import io.pyroscope.javaagent.ProfilerDelegate;
import org.jetbrains.annotations.NotNull;

import java.time.Instant;

/**
 *
 */
public interface ProfilingScheduler {
    /**
     * Use AsyncProfilerDelegate's to start, stop, dumpProfile
     * {@link ProfilerDelegate#start()}
     * {@link ProfilerDelegate#stop()}
     * {@link ProfilerDelegate#dumpProfile(Instant, Instant)}
     * Here is an example of naive implementation
     * <pre>
     * public void start(ProfilerDelegate profiler) {
     *      new Thread(() -&#062; {
     *          while (true) {
     *              Instant startTime = Instant.now();
     *              profiler.start();
     *              sleep(10);
     *              profiler.stop();
     *              exporter.export(
     *                  profiler.dumpProfile(startTime)
     *              );
     *              sleep(50);
     *          }
     *      }).start();
     *  }
     * </pre>
     **/
    void start(@NotNull ProfilerDelegate profiler);

    void stop();
}
```

## File: `agent/src/main/java/io/pyroscope/javaagent/config/AppName.java`
```java
package io.pyroscope.javaagent.config;

import org.jetbrains.annotations.NotNull;

import java.util.*;

public class AppName {
    final String name;
    final Map<String, String> labels;

    public AppName(String name, Map<String, String> labels) {
        this.name = name;
        this.labels = Collections.unmodifiableMap(new TreeMap<>(labels));
    }

    @Override
    public String toString() {
        if (labels.isEmpty()) {
            return name;
        }
        StringJoiner joinedLabels = new StringJoiner(",");
        for (Map.Entry<String, String> e : this.labels.entrySet()) {
            joinedLabels.add((e.getKey().trim()) + "=" + (e.getValue().trim()));
        }
        return String.format("%s{%s}", name, joinedLabels);
    }

    public Builder newBuilder() {
        return new Builder(name, labels);
    }

    public static class Builder {
        private String name;
        private Map<String, String> labels;

        public Builder(String name) {
            this.name = name;
            this.labels = new TreeMap<>();
        }

        public Builder(String name, Map<String, String> labels) {
            this.name = name;
            this.labels = new TreeMap<>(labels);
        }

        public Builder setName(String name) {
            this.name = name;
            return this;
        }

        public Builder addLabel(String k, String v) {
            if (isValidLabel(k) || isValidLabel(v)) {
                this.labels.put(k, v);
            }
            return this;
        }

        public Builder addLabels(Map<String, String> labels) {
            for (Map.Entry<String, String> it : labels.entrySet()) {
                addLabel(it.getKey(), it.getValue());
            }
            return this;
        }

        public AppName build() {
            return new AppName(name, labels);
        }
    }

    public static AppName parse(String appName) {
        int l = appName.indexOf('{');
        int r = appName.indexOf('}');
        if (l != -1 && r != -1 && l < r) {
            String name = appName.substring(0, l);
            String strLabels = appName.substring(l + 1, r);
            Map<String, String> labelsMap = parseLabels(strLabels);
            return new AppName(name, labelsMap);
        } else {
            return new AppName(appName, Collections.emptyMap());
        }
    }

    @NotNull
    public static Map<String, String> parseLabels(String strLabels) {
        String[] labels = strLabels.split(",");
        Map<String, String> labelMap = new HashMap<>();
        for (String label : labels) {
            String[] kv = label.split("=");
            if (kv.length != 2) {
                continue;
            }
            kv[0] = kv[0].trim();
            kv[1] = kv[1].trim();
            if (!isValidLabel(kv[0]) || !isValidLabel(kv[1])) {
                continue;
            }
            labelMap.put(kv[0], kv[1]);
        }
        return labelMap;
    }

    public static boolean isValidLabel(String s) {
        if (s.isEmpty()) {
            return false;
        }
        for (int i = 0; i < s.length(); i++) {
            int c = s.codePointAt(i);
            if (c == '{' || c == '}' || c == ',' || c == '=' || c == ' ') {
                return false;
            }
        }
        return true;
    }
}
```

## File: `agent/src/main/java/io/pyroscope/javaagent/config/Config.java`
```java
package io.pyroscope.javaagent.config;

import com.squareup.moshi.JsonAdapter;
import com.squareup.moshi.Moshi;
import com.squareup.moshi.Types;
import io.pyroscope.http.Format;
import io.pyroscope.javaagent.EventType;
import io.pyroscope.javaagent.api.ConfigurationProvider;
import io.pyroscope.javaagent.api.Logger;
import io.pyroscope.javaagent.impl.DefaultConfigurationProvider;
import io.pyroscope.javaagent.impl.DefaultLogger;
import okhttp3.HttpUrl;
import org.jetbrains.annotations.NotNull;

import java.lang.reflect.Type;
import java.nio.ByteBuffer;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.time.Duration;
import java.util.*;
import java.util.stream.Collectors;
import java.util.stream.Stream;
import java.util.zip.Deflater;

import static io.pyroscope.Preconditions.checkNotNull;

/**
 * Config allows to tweak parameters of existing pyroscope components at start time
 * through pyroscope.properties file or System.getevn - see io.pyroscope.javaagent.impl.DefaultConfigurationProvider
 */
public final class Config {
    private static final String PYROSCOPE_AGENT_ENABLED_CONFIG = "PYROSCOPE_AGENT_ENABLED";
    private static final String PYROSCOPE_APPLICATION_NAME_CONFIG = "PYROSCOPE_APPLICATION_NAME";
    private static final String PYROSCOPE_PROFILING_INTERVAL_CONFIG = "PYROSCOPE_PROFILING_INTERVAL";
    private static final String PYROSCOPE_PROFILER_TYPE_CONFIG = "PYROSCOPE_PROFILER_TYPE";
    private static final String PYROSCOPE_PROFILER_EVENT_CONFIG = "PYROSCOPE_PROFILER_EVENT";
    private static final String PYROSCOPE_PROFILER_ALLOC_CONFIG = "PYROSCOPE_PROFILER_ALLOC";
    private static final String PYROSCOPE_PROFILER_LOCK_CONFIG = "PYROSCOPE_PROFILER_LOCK";
    private static final String PYROSCOPE_UPLOAD_INTERVAL_CONFIG = "PYROSCOPE_UPLOAD_INTERVAL";
    private static final String PYROSCOPE_JAVA_STACK_DEPTH_MAX = "PYROSCOPE_JAVA_STACK_DEPTH_MAX";
    private static final String PYROSCOPE_LOG_LEVEL_CONFIG = "PYROSCOPE_LOG_LEVEL";
    private static final String PYROSCOPE_AP_LOG_LEVEL_CONFIG = "PYROSCOPE_AP_LOG_LEVEL";
    private static final String PYROSCOPE_AP_EXTRA_ARGUMENTS_CONFIG = "PYROSCOPE_AP_EXTRA_ARGUMENTS";
    private static final String PYROSCOPE_SERVER_ADDRESS_CONFIG = "PYROSCOPE_SERVER_ADDRESS";
    private static final String PYROSCOPE_ADHOC_SERVER_ADDRESS_CONFIG = "PYROSCOPE_ADHOC_SERVER_ADDRESS";
    private static final String PYROSCOPE_AUTH_TOKEN_CONFIG = "PYROSCOPE_AUTH_TOKEN";
    private static final String PYROSCOPE_BASIC_AUTH_USER_CONFIG = "PYROSCOPE_BASIC_AUTH_USER";
    private static final String PYROSCOPE_BASIC_AUTH_PASSWORD_CONFIG = "PYROSCOPE_BASIC_AUTH_PASSWORD";
    private static final String PYROSCOPE_FORMAT_CONFIG = "PYROSCOPE_FORMAT";
    private static final String PYROSCOPE_PUSH_QUEUE_CAPACITY_CONFIG = "PYROSCOPE_PUSH_QUEUE_CAPACITY";
    private static final String PYROSCOPE_LABELS = "PYROSCOPE_LABELS";

    private static final String PYROSCOPE_INGEST_MAX_TRIES = "PYROSCOPE_INGEST_MAX_TRIES";
    private static final String PYROSCOPE_EXPORT_COMPRESSION_LEVEL_JFR = "PYROSCOPE_EXPORT_COMPRESSION_LEVEL_JFR";
    private static final String PYROSCOPE_EXPORT_COMPRESSION_LEVEL_LABELS = "PYROSCOPE_EXPORT_COMPRESSION_LEVEL_LABELS";
    private static final String PYROSCOPE_ALLOC_LIVE = "PYROSCOPE_ALLOC_LIVE";
    private static final String PYROSCOPE_GC_BEFORE_DUMP = "PYROSCOPE_GC_BEFORE_DUMP";
    private static final String PYROSCOPE_HTTP_HEADERS = "PYROSCOPE_HTTP_HEADERS";
    private static final String PYROSCOPE_TENANT_ID = "PYROSCOPE_TENANT_ID";
    private static final String PYROSCOPE_PROFILE_EXPORT_TIMEOUT = "PYROSCOPE_PROFILE_EXPORT_TIMEOUT";

    /**
     * Experimental feature, may be removed in the future
     */
    private static final String PYROSCOPE_SAMPLING_RATE = "PYROSCOPE_SAMPLING_RATE";
    /**
     * Experimental feature, may be removed in the future
     */
    private static final String PYROSCOPE_SAMPLING_DURATION = "PYROSCOPE_SAMPLING_DURATION";
    /**
     * Experimental feature, may be removed in the future
     */
    private static final String PYROSCOPE_SAMPLING_EVENT_ORDER_CONFIG = "PYROSCOPE_SAMPLING_EVENT_ORDER";

    // JFR profiler settings
    /**
     * Allows you to overwrite default JFR profiler settings
     */
    private static final String PYROSCOPE_JFR_PROFILER_SETTINGS = "PYROSCOPE_JFR_PROFILER_SETTINGS";

    private static final boolean DEFAULT_AGENT_ENABLED = true;
    public static final String DEFAULT_SPY_NAME = "javaspy";
    private static final Duration DEFAULT_PROFILING_INTERVAL = Duration.ofMillis(10);
    private static final EventType DEFAULT_PROFILER_EVENT = EventType.ITIMER;
    private static final String DEFAULT_PROFILER_ALLOC = "";
    private static final String DEFAULT_PROFILER_LOCK = "";
    private static final Duration DEFAULT_UPLOAD_INTERVAL = Duration.ofSeconds(10);
    private static final List<EventType> DEFAULT_SAMPLING_EVENT_ORDER = null;
    private static final int DEFAULT_JAVA_STACK_DEPTH_MAX = 2048;
    private static final String DEFAULT_SERVER_ADDRESS = "http://localhost:4040";
    private static final Format DEFAULT_FORMAT = Format.JFR;
    // The number of snapshots simultaneously stored in memory is limited by this.
    // The number is fairly arbitrary. If an average snapshot is 5KB, it's about 160 KB.
    private static final int DEFAULT_PUSH_QUEUE_CAPACITY = 8;
    private static final int DEFAULT_INGEST_MAX_RETRIES = 8;
    private static final int DEFAULT_COMPRESSION_LEVEL = Deflater.BEST_SPEED;
    private static final String DEFAULT_LABELS = "";
    private static final boolean DEFAULT_ALLOC_LIVE = false;
    private static final boolean DEFAULT_GC_BEFORE_DUMP = false;
    private static final Duration DEFAULT_SAMPLING_DURATION = null;
    private static final Duration DEFAULT_PROFILE_EXPORT_TIMEOUT = Duration.ofSeconds(10);

    public final boolean agentEnabled;
    public final String applicationName;
    public final ProfilerType profilerType;
    public final Duration profilingInterval;
    public final EventType profilingEvent;
    public final String profilingAlloc;
    public final String profilingLock;
    public final List<EventType> samplingEventOrder;
    public final Duration uploadInterval;
    public final int javaStackDepthMax;
    public final Logger.Level logLevel;
    public final String serverAddress;
    @Deprecated
    public final String authToken;
    public final String jfrProfilerSettings;

    @Deprecated
    public final String timeseriesName;
    public final AppName timeseries;
    public final Format format;
    public final int pushQueueCapacity;
    public final Map<String, String> labels;
    public final int ingestMaxTries;
    public final int compressionLevelJFR;
    public final int compressionLevelLabels;

    public final boolean allocLive;
    public final boolean gcBeforeDump;

    public final Map<String, String> httpHeaders;
    public final Duration samplingDuration;
    public final Duration profileExportTimeout;
    public final String tenantID;
    public final String APLogLevel;
    public final String APExtraArguments;
    public final String basicAuthUser;
    public final String basicAuthPassword;

    Config(final boolean agentEnabled,
           final String applicationName,
           final ProfilerType profilerType,
           final Duration profilingInterval,
           final EventType profilingEvent,
           final String profilingAlloc,
           final String profilingLock,
           final List<EventType> samplingEventOrder,
           final Duration uploadInterval,
           final int javaStackDepthMax,
           final Logger.Level logLevel,
           final String serverAddress,
           final String authToken, String jfrProfilerSettings,
           final Format format,
           final int pushQueueCapacity,
           final Map<String, String> labels,
           int ingestMaxRetries,
           int compressionLevelJFR,
           int compressionLevelLabels,
           boolean allocLive,
           boolean gcBeforeDump,
           Map<String, String> httpHeaders,
           Duration samplingDuration,
           String tenantID,
           String APLogLevel,
           String APExtraArguments,
           String basicAuthUser,
           String basicAuthPassword,
           Duration profileExportTimeout) {
        this.agentEnabled = agentEnabled;
        this.applicationName = applicationName;
        this.profilerType = profilerType;
        this.profilingInterval = profilingInterval;
        this.profilingEvent = profilingEvent;
        this.profilingAlloc = profilingAlloc;
        this.profilingLock = profilingLock;
        this.uploadInterval = uploadInterval;
        this.javaStackDepthMax = javaStackDepthMax;
        this.logLevel = logLevel;
        this.serverAddress = serverAddress;
        this.authToken = authToken;
        this.jfrProfilerSettings = jfrProfilerSettings;
        this.ingestMaxTries = ingestMaxRetries;
        this.compressionLevelJFR = validateCompressionLevel(compressionLevelJFR);
        this.compressionLevelLabels = validateCompressionLevel(compressionLevelLabels);
        this.allocLive = allocLive;
        this.gcBeforeDump = gcBeforeDump;
        this.httpHeaders = httpHeaders;
        this.samplingDuration = samplingDuration;
        this.tenantID = tenantID;
        this.APLogLevel = APLogLevel;
        this.APExtraArguments = APExtraArguments;
        this.basicAuthUser = basicAuthUser;
        this.basicAuthPassword = basicAuthPassword;
        this.timeseries = timeseriesName(AppName.parse(applicationName), profilingEvent, format);
        this.timeseriesName = timeseries.toString();
        this.format = format;
        this.pushQueueCapacity = pushQueueCapacity;
        this.labels = Collections.unmodifiableMap(labels);
        this.profileExportTimeout = profileExportTimeout;
        HttpUrl serverAddressUrl = HttpUrl.parse(serverAddress);
        if (serverAddressUrl == null) {
            throw new IllegalArgumentException("invalid url " + serverAddress);
        }
        if (authToken != null && basicAuthUser != null) {
            DefaultLogger.PRECONFIG_LOGGER.log(Logger.Level.WARN,
                "auth token is ignored (both auth token and basic auth specified)");
        }
        this.samplingEventOrder = resolve(samplingEventOrder, profilingEvent, profilingAlloc, profilingLock, this.samplingDuration);
        if ("0".equals(this.profilingAlloc)) {
            DefaultLogger.PRECONFIG_LOGGER.log(Logger.Level.WARN,
                "Setting PYROSCOPE_PROFILER_ALLOC to 0 registers every allocation event, causing significant overhead and results in large profiles, making it not ideal for production. We recommend a starting value of 512k, adjusting as needed.");
        }
        if ("0".equals(this.profilingLock)) {
            DefaultLogger.PRECONFIG_LOGGER.log(Logger.Level.WARN,
                "Setting PYROSCOPE_PROFILER_LOCK to 0 registers every lock event, causing significant overhead and results in large profiles, making it not ideal for production. We recommend a starting value of 10ms, adjusting as needed.");
        }
    }

    public long profilingIntervalInHertz() {
        return durationToHertz(this.profilingInterval);
    }

    @Override
    public String toString() {
        return "Config{" +
               "agentEnabled=" + agentEnabled +
               ", applicationName='" + applicationName + '\'' +
               ", profilerType=" + profilerType +
               ", profilingInterval=" + profilingInterval +
               ", profilingEvent=" + profilingEvent +
               ", profilingAlloc='" + profilingAlloc + '\'' +
               ", profilingLock='" + profilingLock + '\'' +
               ", samplingEventOrder='" + samplingEventOrder + '\'' +
               ", uploadInterval=" + uploadInterval +
               ", javaStackDepthMax=" + javaStackDepthMax +
               ", logLevel=" + logLevel +
               ", serverAddress='" + serverAddress + '\'' +
               ", authToken='*****'" + // Replacing the actual authToken with asterisks
               ", jfrProfilerSettings='" + jfrProfilerSettings + '\'' +
               ", timeseriesName='" + timeseriesName + '\'' +
               ", timeseries=" + timeseries +
               ", format=" + format +
               ", pushQueueCapacity=" + pushQueueCapacity +
               ", labels=" + labels +
               ", ingestMaxTries=" + ingestMaxTries +
               ", compressionLevelJFR=" + compressionLevelJFR +
               ", compressionLevelLabels=" + compressionLevelLabels +
               ", allocLive=" + allocLive +
               ", httpHeaders=" + httpHeaders +
               ", samplingDuration=" + samplingDuration +
               ", tenantID=" + tenantID +
               '}';
    }

    public @NotNull Builder newBuilder() {
        return new Builder(this);
    }

    private static long durationToHertz(Duration duration) {
        Duration oneSecond = Duration.ofSeconds(1);
        return oneSecond.toNanos() / duration.toNanos();
    }

    public static @NotNull Config build() {
        return build(DefaultConfigurationProvider.INSTANCE);
    }

    public static @NotNull Config build(@NotNull ConfigurationProvider cp) {
        checkNotNull(cp, "cp");
        String alloc = profilingAlloc(cp);
        boolean agentEnabled = bool(cp, PYROSCOPE_AGENT_ENABLED_CONFIG, DEFAULT_AGENT_ENABLED);
        boolean allocLive = bool(cp, PYROSCOPE_ALLOC_LIVE, DEFAULT_ALLOC_LIVE);
        if (DEFAULT_PROFILER_ALLOC.equals(alloc) && allocLive) {
            DefaultLogger.PRECONFIG_LOGGER.log(Logger.Level.WARN, "%s is ignored because %s is not configured",
                PYROSCOPE_ALLOC_LIVE, PYROSCOPE_PROFILER_ALLOC_CONFIG);
            allocLive = false;
        }
        return new Config(
            agentEnabled,
            applicationName(cp),
            profilerType(cp),
            profilingInterval(cp),
            profilingEvent(cp),
            alloc,
            profilingLock(cp),
            samplingEventOrder(cp),
            uploadInterval(cp),
            javaStackDepthMax(cp),
            logLevel(cp),
            serverAddress(cp),
            authToken(cp),
            jfrProfilerSettings(cp),
            format(cp),
            pushQueueCapacity(cp),
            labels(cp),
            ingestMaxRetries(cp),
            compressionLevel(cp, PYROSCOPE_EXPORT_COMPRESSION_LEVEL_JFR),
            compressionLevel(cp, PYROSCOPE_EXPORT_COMPRESSION_LEVEL_LABELS),
            allocLive,
            bool(cp, PYROSCOPE_GC_BEFORE_DUMP, DEFAULT_GC_BEFORE_DUMP),
            httpHeaders(cp),
            samplingDuration(cp),
            tenantID(cp),
            cp.get(PYROSCOPE_AP_LOG_LEVEL_CONFIG),
            cp.get(PYROSCOPE_AP_EXTRA_ARGUMENTS_CONFIG),
            cp.get(PYROSCOPE_BASIC_AUTH_USER_CONFIG), cp.get(PYROSCOPE_BASIC_AUTH_PASSWORD_CONFIG),
            profileExportTimeout(cp));
    }

    /**
     * Retrieves JFR profiler settings from configuration.
     * <p>
     * NOTE: This is an experimental feature and is subject to API changes or may be removed in future releases.
     */
    private static String jfrProfilerSettings(ConfigurationProvider configurationProvider) {
        String jfrProfilerSettings = configurationProvider.get(PYROSCOPE_JFR_PROFILER_SETTINGS);
        if (jfrProfilerSettings != null && !Files.isRegularFile(Paths.get(jfrProfilerSettings))) {
            DefaultLogger.PRECONFIG_LOGGER.log(Logger.Level.ERROR, "unable to find JFR profiler settings at %s", jfrProfilerSettings);
        }
        return null;
    }

    /**
     * Determines the profiler type from configuration.
     * <p>
     * NOTE: When this returns ProfilerType.JFR, it is considered an experimental feature 
     * and is subject to API changes or may be removed in future releases.
     */
    private static ProfilerType profilerType(ConfigurationProvider configurationProvider) {
        String profilerTypeName = configurationProvider.get(PYROSCOPE_PROFILER_TYPE_CONFIG);
        if (profilerTypeName == null || profilerTypeName.isEmpty()) {
            return ProfilerType.ASYNC;
        }
        return ProfilerType.valueOf(profilerTypeName);
    }

    private static String applicationName(ConfigurationProvider configurationProvider) {
        String applicationName = configurationProvider.get(PYROSCOPE_APPLICATION_NAME_CONFIG);
        if (applicationName == null || applicationName.isEmpty()) {
            applicationName = generateApplicationName();
        }
        return applicationName;
    }

    @NotNull
    private static String generateApplicationName() {
        String applicationName;
        DefaultLogger.PRECONFIG_LOGGER.log(Logger.Level.INFO, "We recommend specifying application name via env variable %s",
            PYROSCOPE_APPLICATION_NAME_CONFIG);
        // TODO transfer name generation algorithm from the Go implementation.

        final UUID uuid = UUID.randomUUID();
        final ByteBuffer byteBuffer = ByteBuffer.wrap(new byte[16]);
        byteBuffer.putLong(uuid.getMostSignificantBits());
        byteBuffer.putLong(uuid.getLeastSignificantBits());
        final String random = Base64.getUrlEncoder().withoutPadding().encodeToString(byteBuffer.array());
        applicationName = DEFAULT_SPY_NAME + "." + random;

        DefaultLogger.PRECONFIG_LOGGER.log(Logger.Level.INFO, "For now we chose the name for you and it's %s", applicationName);
        return applicationName;
    }

    private static Duration profilingInterval(ConfigurationProvider configurationProvider) {
        final String profilingIntervalStr = configurationProvider.get(PYROSCOPE_PROFILING_INTERVAL_CONFIG);
        if (profilingIntervalStr == null || profilingIntervalStr.isEmpty()) {
            return DEFAULT_PROFILING_INTERVAL;
        }
        try {
            return IntervalParser.parse(profilingIntervalStr);
        } catch (final NumberFormatException e) {
            DefaultLogger.PRECONFIG_LOGGER.log(Logger.Level.WARN, "Invalid %s value %s, using %sms",
                PYROSCOPE_PROFILING_INTERVAL_CONFIG, profilingIntervalStr, DEFAULT_PROFILING_INTERVAL.toMillis());
            return DEFAULT_PROFILING_INTERVAL;
        }
    }

    private AppName timeseriesName(AppName app, EventType eventType, Format format) {
        if (format == Format.JFR)
            return app;
        return app.newBuilder()
            .setName(app.name + "." + eventType.id)
            .build();
    }

    private static EventType profilingEvent(ConfigurationProvider configurationProvider) {
        final String profilingEventStr =
            configurationProvider.get(PYROSCOPE_PROFILER_EVENT_CONFIG);
        if (profilingEventStr == null || profilingEventStr.isEmpty()) {
            return DEFAULT_PROFILER_EVENT;
        }

        final String lowerCaseTrimmed = profilingEventStr.trim().toLowerCase();

        try {
            return EventType.fromId(lowerCaseTrimmed);
        } catch (IllegalArgumentException e) {
            DefaultLogger.PRECONFIG_LOGGER.log(Logger.Level.WARN, "Invalid %s value %s, using %s",
                PYROSCOPE_PROFILER_EVENT_CONFIG, profilingEventStr, DEFAULT_PROFILER_EVENT.id);
            return DEFAULT_PROFILER_EVENT;
        }
    }

    private static String profilingAlloc(ConfigurationProvider configurationProvider) {
        final String profilingAlloc = configurationProvider.get(PYROSCOPE_PROFILER_ALLOC_CONFIG);
        if (profilingAlloc == null || profilingAlloc.isEmpty()) {
            return DEFAULT_PROFILER_ALLOC;
        }
        return profilingAlloc.trim().toLowerCase();
    }

    private static String profilingLock(ConfigurationProvider configurationProvider) {
        final String profilingLock = configurationProvider.get(PYROSCOPE_PROFILER_LOCK_CONFIG);
        if (profilingLock == null || profilingLock.isEmpty()) {
            return DEFAULT_PROFILER_LOCK;
        }
        return profilingLock.trim().toLowerCase();
    }

    private static List<EventType> samplingEventOrder(final ConfigurationProvider cp) {
        final String samplingEventOrder = cp.get(PYROSCOPE_SAMPLING_EVENT_ORDER_CONFIG);
        if (null == samplingEventOrder || samplingEventOrder.isEmpty()) {
            return DEFAULT_SAMPLING_EVENT_ORDER;
        }
        DefaultLogger.PRECONFIG_LOGGER.log(Logger.Level.WARN, "keep upload interval >= sampling duration * distinct event count to avoid unexpected behaviour");
        return Stream.of(samplingEventOrder.split("\\s*,\\s*"))
            .map(s -> {
                try {
                    return EventType.fromId(s);
                } catch (final IllegalArgumentException e) {
                    return null;
                }
            })
            .filter(Objects::nonNull)
            .collect(Collectors.toCollection(ArrayList::new));
    }

    // extra args events not supported
    private static List<EventType> resolve(final List<EventType> samplingEventOrder, final EventType type, final String alloc, final String lock, final Duration samplingDuration) {
        if (null == samplingEventOrder)
            return null;
        if (null == samplingDuration) {
            DefaultLogger.PRECONFIG_LOGGER.log(Logger.Level.WARN, "not implemented: sampling event order is only implemented in sampling mode");
            return null;
        }
        // effectively set size is upper bounded by 3
        final LinkedHashSet<EventType> set = new LinkedHashSet<>();
        final boolean _alloc = null != alloc && !alloc.isEmpty();
        final boolean _lock = null != lock && !lock.isEmpty();

        // filter unmacthed and dedupe
        for (final EventType t : samplingEventOrder)
            if (t.equals(type) || (EventType.ALLOC.equals(t) && _alloc) || (EventType.LOCK.equals(t) && _lock))
                set.add(t);
        // append missing
        set.add(type);
        if (_alloc)
            set.add(EventType.ALLOC);
        if (_lock)
            set.add(EventType.LOCK);
        return new ArrayList<>(set);
    }

    private static Duration uploadInterval(ConfigurationProvider configurationProvider) {
        final String uploadIntervalStr = configurationProvider.get(PYROSCOPE_UPLOAD_INTERVAL_CONFIG);
        if (uploadIntervalStr == null || uploadIntervalStr.isEmpty()) {
            return DEFAULT_UPLOAD_INTERVAL;
        }
        try {
            return IntervalParser.parse(uploadIntervalStr);
        } catch (final NumberFormatException e) {
            DefaultLogger.PRECONFIG_LOGGER.log(Logger.Level.WARN, "Invalid %s value %s, using %s",
                PYROSCOPE_UPLOAD_INTERVAL_CONFIG, uploadIntervalStr, DEFAULT_UPLOAD_INTERVAL);
            return DEFAULT_UPLOAD_INTERVAL;
        }
    }

    private static Duration profileExportTimeout(ConfigurationProvider configurationProvider) {
        final String  profileExportTimeoutStr = configurationProvider.get(PYROSCOPE_PROFILE_EXPORT_TIMEOUT);
        if (profileExportTimeoutStr == null || profileExportTimeoutStr.isEmpty()) {
            return DEFAULT_PROFILE_EXPORT_TIMEOUT;
        }
        try {
            return IntervalParser.parse(profileExportTimeoutStr);
        } catch (final NumberFormatException e) {
            DefaultLogger.PRECONFIG_LOGGER.log(Logger.Level.WARN, "Invalid %s value %s, using %s",
            		PYROSCOPE_PROFILE_EXPORT_TIMEOUT, profileExportTimeoutStr, DEFAULT_PROFILE_EXPORT_TIMEOUT);
            return DEFAULT_PROFILE_EXPORT_TIMEOUT;
        }
    }



    private static int javaStackDepthMax(ConfigurationProvider configurationProvider) {
        final String javaStackDepthMaxStr = configurationProvider.get(PYROSCOPE_JAVA_STACK_DEPTH_MAX);
        if (null == javaStackDepthMaxStr || javaStackDepthMaxStr.isEmpty()) {
            return DEFAULT_JAVA_STACK_DEPTH_MAX;
        }
        try {
            return Integer.parseInt(javaStackDepthMaxStr);
        } catch (final NumberFormatException e) {
            return DEFAULT_JAVA_STACK_DEPTH_MAX;
        }
    }

    private static Logger.Level logLevel(ConfigurationProvider configurationProvider) {
        final String logLevel = configurationProvider.get(PYROSCOPE_LOG_LEVEL_CONFIG);
        if (logLevel == null || logLevel.isEmpty()) {
            return Logger.Level.INFO;
        }
        switch (logLevel.toLowerCase(Locale.ROOT)) {
            case "debug":
                return Logger.Level.DEBUG;
            case "info":
                return Logger.Level.INFO;
            case "warn":
                return Logger.Level.WARN;
            case "error":
                return Logger.Level.ERROR;
            default:
                DefaultLogger.PRECONFIG_LOGGER.log(Logger.Level.WARN, "Unknown log level %s, using INFO", logLevel);
                return Logger.Level.INFO;
        }
    }

    private static String serverAddress(ConfigurationProvider configurationProvider) {
        String serverAddress = configurationProvider.get(PYROSCOPE_ADHOC_SERVER_ADDRESS_CONFIG);
        if (serverAddress == null || serverAddress.isEmpty()) {
            serverAddress = configurationProvider.get(PYROSCOPE_SERVER_ADDRESS_CONFIG);
        }
        if (serverAddress == null || serverAddress.isEmpty()) {
            DefaultLogger.PRECONFIG_LOGGER.log(Logger.Level.WARN, "%s is not defined, using %s",
                PYROSCOPE_SERVER_ADDRESS_CONFIG, DEFAULT_SERVER_ADDRESS);
            serverAddress = DEFAULT_SERVER_ADDRESS;

        }
        return serverAddress;
    }

    private static String authToken(ConfigurationProvider configurationProvider) {
        return configurationProvider.get(PYROSCOPE_AUTH_TOKEN_CONFIG);
    }

    private static Format format(ConfigurationProvider configurationProvider) {
        final String format = configurationProvider.get(PYROSCOPE_FORMAT_CONFIG);
        if (format == null || format.isEmpty())
            return DEFAULT_FORMAT;
        switch (format.trim().toLowerCase()) {
            case "jfr":
                return Format.JFR;
            default:
                DefaultLogger.PRECONFIG_LOGGER.log(Logger.Level.WARN, "Unknown format %s, using %s", format, DEFAULT_FORMAT);
                return DEFAULT_FORMAT;
        }
    }

    private static int pushQueueCapacity(ConfigurationProvider configurationProvider) {
        final String strPushQueueCapacity = configurationProvider.get(PYROSCOPE_PUSH_QUEUE_CAPACITY_CONFIG);
        if (strPushQueueCapacity == null || strPushQueueCapacity.isEmpty()) {
            return DEFAULT_PUSH_QUEUE_CAPACITY;
        }
        try {
            int pushQueueCapacity = Integer.parseInt(strPushQueueCapacity);
            if (pushQueueCapacity <= 0) {
                return DEFAULT_PUSH_QUEUE_CAPACITY;
            } else {
                return pushQueueCapacity;
            }
        } catch (NumberFormatException e) {
            return DEFAULT_PUSH_QUEUE_CAPACITY;
        }
    }

    public static Map<String, String> labels(ConfigurationProvider configurationProvider) {
        String strLabels = configurationProvider.get(PYROSCOPE_LABELS);
        if (strLabels == null) {
            strLabels = DEFAULT_LABELS;
        }
        return AppName.parseLabels(strLabels);
    }

    private static int ingestMaxRetries(ConfigurationProvider configurationProvider) {
        final String strIngestMaxRetries = configurationProvider.get(PYROSCOPE_INGEST_MAX_TRIES);
        if (strIngestMaxRetries == null || strIngestMaxRetries.isEmpty()) {
            return DEFAULT_INGEST_MAX_RETRIES;
        }
        try {
            return Integer.parseInt(strIngestMaxRetries);
        } catch (NumberFormatException e) {
            return DEFAULT_INGEST_MAX_RETRIES;
        }
    }

    public static boolean bool(ConfigurationProvider cp, String key, boolean defaultValue) {
        final String v = cp.get(key);
        if (v == null || v.isEmpty()) {
            return defaultValue;
        }
        return Boolean.parseBoolean(v);
    }

    public static int compressionLevel(ConfigurationProvider cp, String key) {
        final String sLevel = cp.get(key);
        if (sLevel == null || sLevel.isEmpty()) {
            return DEFAULT_COMPRESSION_LEVEL;
        }
        if ("NO_COMPRESSION".equalsIgnoreCase(sLevel)) {
            return Deflater.NO_COMPRESSION;
        }
        if ("BEST_SPEED".equalsIgnoreCase(sLevel)) {
            return Deflater.BEST_SPEED;
        }
        if ("BEST_COMPRESSION".equalsIgnoreCase(sLevel)) {
            return Deflater.BEST_COMPRESSION;
        }
        if ("DEFAULT_COMPRESSION".equalsIgnoreCase(sLevel)) {
            return Deflater.DEFAULT_COMPRESSION;
        }
        int level;
        try {
            level = Integer.parseInt(sLevel);
        } catch (NumberFormatException e) {
            return DEFAULT_COMPRESSION_LEVEL;
        }
        if (level >= 0 && level <= 9 || level == -1) {
            return level;
        }
        return DEFAULT_COMPRESSION_LEVEL;
    }

    private static int validateCompressionLevel(int level) {
        if (level >= -1 && level <= 9) {
            return level;
        }
        throw new IllegalArgumentException(String.format("wrong deflate compression level %d", level));
    }

    public static Map<String, String> httpHeaders(ConfigurationProvider cp) {
        final String sHttpHeaders = cp.get(PYROSCOPE_HTTP_HEADERS);
        if (sHttpHeaders == null || sHttpHeaders.isEmpty()) {
            return Collections.emptyMap();
        }
        Moshi moshi = new Moshi.Builder().build();

        Type headersType = Types.newParameterizedType(Map.class, String.class, String.class);
        JsonAdapter<Map<String, String>> adapter = moshi.adapter(headersType);

        try {
            Map<String, String> httpHeaders = adapter.fromJson(sHttpHeaders);
            return httpHeaders != null ? httpHeaders : Collections.emptyMap();
        } catch (Exception e) {
            DefaultLogger.PRECONFIG_LOGGER.log(Logger.Level.ERROR, "Failed to parse %s = %s configuration. " +
                                                                   "Falling back to no extra http headers. %s: ", PYROSCOPE_HTTP_HEADERS, sHttpHeaders, e.getMessage());
            return Collections.emptyMap();
        }
    }

    private static String tenantID(ConfigurationProvider cp) {
        return cp.get(PYROSCOPE_TENANT_ID);
    }

    private static Duration samplingDuration(ConfigurationProvider configurationProvider) {
        Duration uploadInterval = uploadInterval(configurationProvider);

        final String samplingDurationStr = configurationProvider.get(PYROSCOPE_SAMPLING_DURATION);
        if (samplingDurationStr != null && !samplingDurationStr.isEmpty()) {
            try {
                Duration samplingDuration = IntervalParser.parse(samplingDurationStr);
                if (samplingDuration.compareTo(uploadInterval) > 0) {
                    DefaultLogger.PRECONFIG_LOGGER.log(Logger.Level.WARN, "Invalid %s value %s, ignore it",
                        PYROSCOPE_SAMPLING_DURATION, samplingDurationStr);
                } else {
                    return samplingDuration;
                }
            } catch (final NumberFormatException e) {
                DefaultLogger.PRECONFIG_LOGGER.log(Logger.Level.WARN, "Invalid %s value %s, ignore it",
                    PYROSCOPE_SAMPLING_DURATION, samplingDurationStr);
            }
            return DEFAULT_SAMPLING_DURATION;
        }

        final String samplingRateStr = configurationProvider.get(PYROSCOPE_SAMPLING_RATE);
        if (samplingRateStr == null || samplingRateStr.isEmpty()) {
            return DEFAULT_SAMPLING_DURATION;
        }
        try {
            double samplingRate = Double.parseDouble(samplingRateStr);
            if (samplingRate <= 0.0 || samplingRate >= 1.0) {
                return DEFAULT_SAMPLING_DURATION;
            }
            long uploadIntervalMillis = uploadInterval.toMillis();
            long samplingDurationMillis = Math.min(uploadIntervalMillis, Math.round(uploadIntervalMillis * samplingRate));
            return Duration.ofMillis(samplingDurationMillis);
        } catch (final NumberFormatException e) {
            DefaultLogger.PRECONFIG_LOGGER.log(Logger.Level.WARN, "Invalid %s value %s, ignore it",
                PYROSCOPE_SAMPLING_RATE, samplingRateStr);
            return DEFAULT_SAMPLING_DURATION;
        }
    }

    public static class Builder {
        private boolean agentEnabled = DEFAULT_AGENT_ENABLED;
        private String applicationName = null;
        private ProfilerType profilerType = ProfilerType.ASYNC;
        private Duration profilingInterval = DEFAULT_PROFILING_INTERVAL;
        private EventType profilingEvent = DEFAULT_PROFILER_EVENT;
        private String profilingAlloc = "";
        private String profilingLock = "";
        private List<EventType> samplingEventOrder = null;
        private Duration uploadInterval = DEFAULT_UPLOAD_INTERVAL;
        private int javaStackDepthMax = DEFAULT_JAVA_STACK_DEPTH_MAX;
        private Logger.Level logLevel = Logger.Level.INFO;
        private String serverAddress = DEFAULT_SERVER_ADDRESS;
        @Deprecated
        private String authToken = null;
        private Format format = DEFAULT_FORMAT;
        private int pushQueueCapacity = DEFAULT_PUSH_QUEUE_CAPACITY;
        private Map<String, String> labels = Collections.emptyMap();
        private int ingestMaxRetries = DEFAULT_INGEST_MAX_RETRIES;
        private int compressionLevelJFR = DEFAULT_COMPRESSION_LEVEL;
        private int compressionLevelLabels = DEFAULT_COMPRESSION_LEVEL;
        private boolean allocLive = DEFAULT_ALLOC_LIVE;
        private boolean gcBeforeDump = DEFAULT_GC_BEFORE_DUMP;
        private Map<String, String> httpHeaders = new HashMap<>();
        private Duration samplingDuration = DEFAULT_SAMPLING_DURATION;
        private Duration profileExportTimeout = DEFAULT_PROFILE_EXPORT_TIMEOUT;
        private String tenantID = null;
        private String APLogLevel = null;
        private String APExtraArguments = null;
        private String basicAuthUser;
        private String basicAuthPassword;
        private String jfrProfilerSettings;

        public Builder() {
        }

        public Builder(@NotNull Config buildUpon) {
            checkNotNull(buildUpon, "config");
            agentEnabled = buildUpon.agentEnabled;
            applicationName = buildUpon.applicationName;
            profilerType = buildUpon.profilerType;
            profilingInterval = buildUpon.profilingInterval;
            profilingEvent = buildUpon.profilingEvent;
            profilingAlloc = buildUpon.profilingAlloc;
            profilingLock = buildUpon.profilingLock;
            samplingEventOrder = buildUpon.samplingEventOrder;
            uploadInterval = buildUpon.uploadInterval;
            javaStackDepthMax = buildUpon.javaStackDepthMax;
            logLevel = buildUpon.logLevel;
            serverAddress = buildUpon.serverAddress;
            authToken = buildUpon.authToken;
            jfrProfilerSettings = buildUpon.jfrProfilerSettings;
            format = buildUpon.format;
            pushQueueCapacity = buildUpon.pushQueueCapacity;
            labels = buildUpon.labels;
            ingestMaxRetries = buildUpon.ingestMaxTries;
            compressionLevelJFR = buildUpon.compressionLevelJFR;
            compressionLevelLabels = buildUpon.compressionLevelLabels;
            allocLive = buildUpon.allocLive;
            gcBeforeDump = buildUpon.gcBeforeDump;
            httpHeaders = new HashMap<>(buildUpon.httpHeaders);
            samplingDuration = buildUpon.samplingDuration;
            profileExportTimeout = buildUpon.profileExportTimeout;
            tenantID = buildUpon.tenantID;
            APLogLevel = buildUpon.APLogLevel;
            APExtraArguments = buildUpon.APExtraArguments;
            basicAuthUser = buildUpon.basicAuthUser;
            basicAuthPassword = buildUpon.basicAuthPassword;
        }

        public Builder setAgentEnabled(boolean agentEnabled) {
            this.agentEnabled = agentEnabled;
            return this;
        }

        public Builder setApplicationName(String applicationName) {
            this.applicationName = applicationName;
            return this;
        }

        public Builder setProfilingInterval(Duration profilingInterval) {
            this.profilingInterval = profilingInterval;
            return this;
        }

        public Builder setProfilingEvent(EventType profilingEvent) {
            this.profilingEvent = profilingEvent;
            return this;
        }

        public Builder setProfilingAlloc(String profilingAlloc) {
            this.profilingAlloc = profilingAlloc;
            return this;
        }

        public Builder setProfilingLock(String profilingLock) {
            this.profilingLock = profilingLock;
            return this;
        }

        public Builder setSamplingEventOrder(final List<EventType> samplingEventOrder) {
            this.samplingEventOrder = samplingEventOrder;
            return this;
        }

        public Builder setUploadInterval(Duration uploadInterval) {
            this.uploadInterval = uploadInterval;
            return this;
        }

        public Builder setProfileExportTimeout(Duration profileExportTimeout) {
            this.profileExportTimeout = profileExportTimeout;
            return this;
        }

        public Builder setJavaStackDepthMax(final int javaStackDepthMax) {
            this.javaStackDepthMax = javaStackDepthMax;
            return this;
        }

        public Builder setLogLevel(Logger.Level logLevel) {
            this.logLevel = logLevel;
            return this;
        }

        public Builder setServerAddress(String serverAddress) {
            this.serverAddress = serverAddress;
            return this;
        }

        @Deprecated
        public Builder setAuthToken(String authToken) {
            this.authToken = authToken;
            return this;
        }

        /**
         * Sets JFR profiler settings.
         * <p>
         * NOTE: This is an experimental feature and is subject to API changes or may be removed in future releases.
         *
         * @param jfrProfilerSettings the JFR profiler settings path
         * @return this builder instance
         */
        public Builder setJFRProfilerSettings(String jfrProfilerSettings) {
            this.jfrProfilerSettings = jfrProfilerSettings;
            return this;
        }

        public Builder setFormat(Format format) {
            this.format = format;
            return this;
        }

        public Builder setPushQueueCapacity(int pushQueueCapacity) {
            this.pushQueueCapacity = pushQueueCapacity;
            return this;
        }

        public Builder setLabels(Map<String, String> labels) {
            this.labels = labels;
            return this;
        }

        public Builder setIngestMaxRetries(int ingestMaxRetries) {
            this.ingestMaxRetries = ingestMaxRetries;
            return this;
        }

        public Builder setCompressionLevelJFR(int compressionLevelJFR) {
            this.compressionLevelJFR = validateCompressionLevel(compressionLevelJFR);
            return this;
        }

        public Builder setCompressionLevelLabels(int compressionLevelLabels) {
            this.compressionLevelLabels = validateCompressionLevel(compressionLevelLabels);
            return this;
        }

        public Builder setAllocLive(boolean allocLive) {
            this.allocLive = allocLive;
            return this;
        }

        public Builder setGcBeforeDump(boolean gcBeforeDump) {
            this.gcBeforeDump = gcBeforeDump;
            return this;
        }

        public Builder setHTTPHeaders(Map<String, String> httpHeaders) {
            this.httpHeaders = new HashMap<>(httpHeaders);
            return this;
        }

        public Builder addHTTPHeader(String k, String v) {
            this.httpHeaders.put(k, v);
            return this;
        }

        public Builder setSamplingDuration(Duration samplingDuration) {
            this.samplingDuration = samplingDuration;
            return this;
        }

        public Builder setTenantID(String tenantID) {
            this.tenantID = tenantID;
            return this;
        }

        public Builder setAPLogLevel(String apLogLevel) {
            this.APLogLevel = apLogLevel;
            return this;
        }

        public Builder setAPExtraArguments(String APExtraArguments) {
            this.APExtraArguments = APExtraArguments;
            return this;
        }

        public Builder setBasicAuthUser(String basicAuthUser) {
            this.basicAuthUser = basicAuthUser;
            return this;
        }

        public Builder setBasicAuthPassword(String basicAuthPassword) {
            this.basicAuthPassword = basicAuthPassword;
            return this;
        }

        /**
         * Sets the profiler type.
         * <p>
         * NOTE: ProfilerType.JFR is an experimental feature and is subject to API changes or may be removed in future releases.
         *
         * @param profilerType the profiler type to set
         * @return this builder instance
         */
        public Builder setProfilerType(ProfilerType profilerType) {
            this.profilerType = profilerType;
            return this;
        }

        public @NotNull Config build() {
            if (applicationName == null || applicationName.isEmpty()) {
                applicationName = generateApplicationName();
            }
            return new Config(agentEnabled,
                applicationName,
                profilerType,
                profilingInterval,
                profilingEvent,
                profilingAlloc,
                profilingLock,
                samplingEventOrder,
                uploadInterval,
                javaStackDepthMax,
                logLevel,
                serverAddress,
                authToken,
                jfrProfilerSettings,
                format,
                pushQueueCapacity,
                labels,
                ingestMaxRetries,
                compressionLevelJFR,
                compressionLevelLabels,
                allocLive,
                gcBeforeDump,
                httpHeaders,
                samplingDuration,
                tenantID,
                APLogLevel,
                APExtraArguments,
                basicAuthUser, basicAuthPassword,
                profileExportTimeout);
        }
    }
}
```

## File: `agent/src/main/java/io/pyroscope/javaagent/config/IntervalParser.java`
```java
package io.pyroscope.javaagent.config;

import java.time.Duration;
import java.time.temporal.ChronoUnit;
import java.time.temporal.TemporalUnit;

public final class IntervalParser {
    public static Duration parse(final String str) throws NumberFormatException {
        final long amount;
        final TemporalUnit unit;
        if (str.endsWith("ms")) {
            unit = ChronoUnit.MILLIS;
            amount = Long.parseLong(str.substring(0, str.length() - 2));
        } else if (str.endsWith("us")) {
            unit = ChronoUnit.MICROS;
            amount = Long.parseLong(str.substring(0, str.length() - 2));
        } else if (str.endsWith("s")) {
            unit = ChronoUnit.SECONDS;
            amount = Long.parseLong(str.substring(0, str.length() - 1));
        } else if (Character.isDigit(str.charAt(str.length() - 1))) {
            unit = ChronoUnit.NANOS;
            amount = Long.parseLong(str);
        } else {
            throw new NumberFormatException("Cannot parse interval " + str);
        }

        if (amount <= 0) {
            throw new NumberFormatException("Interval must be positive, but " + str + " given");
        }

        return Duration.of(amount, unit);
    }
}
```

## File: `agent/src/main/java/io/pyroscope/javaagent/config/ProfilerType.java`
```java
package io.pyroscope.javaagent.config;

import io.pyroscope.javaagent.AsyncProfilerDelegate;
import io.pyroscope.javaagent.JFRProfilerDelegate;
import io.pyroscope.javaagent.ProfilerDelegate;

import java.util.function.Function;

public enum ProfilerType {
    /**
     * JFR profiler type.
     * <p>
     * NOTE: This is an experimental feature and is subject to API changes or may be removed in future releases.
     */
    JFR(JFRProfilerDelegate::new),
    ASYNC(AsyncProfilerDelegate::new);

    private final Function<Config, ProfilerDelegate> profilerDelegateFactory;

    ProfilerType(Function<Config, ProfilerDelegate> profilerDelegateFactory) {
        this.profilerDelegateFactory = profilerDelegateFactory;
    }

    public ProfilerDelegate create(Config config) {
        return profilerDelegateFactory.apply(config);
    }
}
```

## File: `agent/src/main/java/io/pyroscope/javaagent/impl/ContinuousProfilingScheduler.java`
```java
package io.pyroscope.javaagent.impl;

import io.pyroscope.javaagent.ProfilerDelegate;
import io.pyroscope.javaagent.Snapshot;
import io.pyroscope.javaagent.api.Exporter;
import io.pyroscope.javaagent.api.Logger;
import io.pyroscope.javaagent.api.ProfilingScheduler;
import io.pyroscope.javaagent.config.Config;
import kotlin.random.Random;
import org.jetbrains.annotations.NotNull;

import java.time.Duration;
import java.time.Instant;
import java.util.concurrent.*;


public class ContinuousProfilingScheduler implements ProfilingScheduler {
    public static final ThreadFactory THREAD_FACTORY = r -> {
        Thread t = Executors.defaultThreadFactory().newThread(r);
        t.setName("PyroscopeProfilingScheduler");
        t.setDaemon(true);
        return t;
    };
    private final Config config;

    private ScheduledExecutorService executor;
    private final Exporter exporter;
    private final Logger logger;
    private final Object lock = new Object();
    private Instant profilingIntervalStartTime;
    private ScheduledFuture<?> job;
    private boolean started;
    private ProfilerDelegate profiler;

    public ContinuousProfilingScheduler(@NotNull Config config, @NotNull Exporter exporter, @NotNull Logger logger) {
        this.config = config;
        this.exporter = exporter;
        this.logger = logger;
    }

    @Override
    public void start(@NotNull ProfilerDelegate profiler) {
        this.logger.log(Logger.Level.DEBUG, "ContinuousProfilingScheduler starting");
        synchronized (lock) {
            if (started) {
                throw new IllegalStateException("already started");
            }
            Duration firstProfilingDuration;
            try {
                firstProfilingDuration = startFirst(profiler);
            } catch (Throwable throwable) {
                stopSchedulerLocked();
                throw new IllegalStateException(throwable);
            }
            this.profiler = profiler;
            this.executor = Executors.newSingleThreadScheduledExecutor(THREAD_FACTORY);
            this.job = executor.scheduleAtFixedRate(this::schedulerTick,
                    firstProfilingDuration.toMillis(), config.uploadInterval.toMillis(), TimeUnit.MILLISECONDS);
            this.started = true;
            logger.log(Logger.Level.DEBUG, "ContinuousProfilingScheduler started");
        }
    }

    @Override
    public void stop() {
        ScheduledExecutorService svc = null;
        try {
            synchronized (lock) {
                try {
                    stopSchedulerLocked();
                } finally {
                    svc = this.executor;
                    this.executor = null;
                }
            }
            this.logger.log(Logger.Level.DEBUG, "ContinuousProfilingScheduler stopped");
        } finally {
            // shutdown here not under lock to avoid deadlock ( the task may block to wait for lock and
            // we are holding the lock and waiting for task to finish)
            // There is still synchronization happens from the PyroscopeAgent class,
            // so there are no concurrent calls to start/stop. So there is no lock here
            awaitTermination(svc);
        }
    }

    private static void awaitTermination(ScheduledExecutorService svc) {
        try {
            boolean terminated = svc.awaitTermination(10, TimeUnit.SECONDS);
            if (!terminated) {
                throw new IllegalStateException("failed to terminate scheduler's executor");
            }
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
            throw new IllegalStateException("failed to terminate scheduler's executor", e);
        }
    }

    private void stopSchedulerLocked() {
        if (!this.started) {
            return;
        }
        this.logger.log(Logger.Level.DEBUG, "ContinuousProfilingScheduler stopping");
        try {
            this.profiler.stop();
        } catch (Throwable throwable) {
            throw new IllegalStateException(throwable);
        } finally {
            job.cancel(true);
            executor.shutdown();
            this.started = false;
        }
    }


    private void schedulerTick() {

        synchronized (lock) {
            if (!started) {
                return;
            }
            logger.log(Logger.Level.DEBUG, "ContinuousProfilingScheduler#schedulerTick");
            Snapshot snapshot;
            Instant now;
            try {
                profiler.stop();
                now = Instant.now();
                snapshot = profiler.dumpProfile(this.profilingIntervalStartTime, now);
                profiler.start();
            } catch (Throwable throwable) {
                logger.log(Logger.Level.ERROR, "Error dumping profiler %s", throwable);
                stopSchedulerLocked();
                return;
            }
            profilingIntervalStartTime = now;
            exporter.export(snapshot);
        }
    }


    /**
     * Starts the first profiling interval.
     * profilingIntervalStartTime is set to now
     * Duration of the first profiling interval is a random fraction of uploadInterval not smaller than 2000ms.
     *
     * @return Duration of the first profiling interval
     */
    private Duration startFirst(ProfilerDelegate profiler) {
        Instant now = Instant.now();

        long uploadIntervalMillis = config.uploadInterval.toMillis();
        float randomOffset = Random.Default.nextFloat();
        uploadIntervalMillis = (long) ((float) uploadIntervalMillis * randomOffset);
        if (uploadIntervalMillis < 2000) {
            uploadIntervalMillis = 2000;
        }
        Duration firstProfilingDuration = Duration.ofMillis(uploadIntervalMillis);

        profiler.start();
        profilingIntervalStartTime = now;
        return firstProfilingDuration;
    }


}
```

## File: `agent/src/main/java/io/pyroscope/javaagent/impl/DefaultConfigurationProvider.java`
```java
package io.pyroscope.javaagent.impl;

import io.pyroscope.javaagent.api.ConfigurationProvider;
import io.pyroscope.javaagent.api.Logger;
import org.jetbrains.annotations.NotNull;
import org.jetbrains.annotations.Nullable;

import java.io.IOException;
import java.io.InputStream;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;

/**
 * Delegates configuration provision to multiple sources
 * - System.getProperties
 * - System.getenv
 * - pyroscope.properties configuration file
 * pyroscope.properties file can be overridden by PYROSCOPE_CONFIGURATION_FILE_CONFIG
 */
public class DefaultConfigurationProvider implements ConfigurationProvider {
    private static final String PYROSCOPE_CONFIGURATION_FILE_CONFIG = "PYROSCOPE_CONFIGURATION_FILE";
    private static final String DEFAULT_CONFIGURATION_FILE = "pyroscope.properties";

    public static final DefaultConfigurationProvider INSTANCE = new DefaultConfigurationProvider();

    final List<ConfigurationProvider> delegates = new ArrayList<>();

    public DefaultConfigurationProvider() {
        delegates.add(new PropertiesConfigurationProvider(System.getProperties()));
        delegates.add(new EnvConfigurationProvider());
        String configFile = getPropertiesFile();
        try {
            delegates.add(new PropertiesConfigurationProvider(
                Files.newInputStream(Paths.get(configFile))
            ));
        } catch (IOException ignored) {
        }
        try {
            InputStream res = this.getClass().getResourceAsStream(configFile);
            if (res != null) {
                delegates.add(new PropertiesConfigurationProvider(res));
            }
        } catch (IOException ignored) {
        }
        if (!configFile.equals(DEFAULT_CONFIGURATION_FILE) && delegates.size() == 2) {
            DefaultLogger.PRECONFIG_LOGGER.log(Logger.Level.WARN, "%s configuration file was specified but was not found", configFile);
        }
    }

    @Override
    @Nullable
    public String get(@NotNull String key) {
        for (int i = 0; i < delegates.size(); i++) {
            String v = delegates.get(i).get(key);
            if (v != null) {
                return v;
            }
        }
        return null;
    }

    private String getPropertiesFile() {
        String f = get(PYROSCOPE_CONFIGURATION_FILE_CONFIG);
        if (f == null) {
            return DEFAULT_CONFIGURATION_FILE;
        }
        return f;
    }

}
```

## File: `agent/src/main/java/io/pyroscope/javaagent/impl/DefaultLogger.java`
```java
package io.pyroscope.javaagent.impl;

import io.pyroscope.javaagent.api.Logger;

import java.io.PrintStream;
import java.text.DateFormat;
import java.text.SimpleDateFormat;

public class DefaultLogger implements Logger {
    public static final Logger PRECONFIG_LOGGER = new DefaultLogger(Level.DEBUG, System.err);
    private static final DateFormat DATE_FORMAT = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss.SSS");
    private final Level logLevel;
    private final PrintStream out;

    public DefaultLogger(Level logLevel, PrintStream out) {
        this.logLevel = logLevel;
        this.out = out;
    }

    @Override
	public void log(Level logLevel, String msg, Object... args) {
		if (logLevel.level < this.logLevel.level) {
			return;
		}
		String date;
		synchronized (this) {
			date = DATE_FORMAT.format(System.currentTimeMillis());
		}
		String formattedMsg = (msg == null) ? "null"
				: (args == null || args.length == 0) ? msg : String.format(msg, args);

		out.printf("%s [%s] %s%n", date, logLevel, formattedMsg);
	}

}
```

## File: `agent/src/main/java/io/pyroscope/javaagent/impl/EnvConfigurationProvider.java`
```java
package io.pyroscope.javaagent.impl;

import io.pyroscope.javaagent.api.ConfigurationProvider;
import org.jetbrains.annotations.NotNull;
import org.jetbrains.annotations.Nullable;

import java.util.Map;

public class EnvConfigurationProvider implements ConfigurationProvider {

    private final Map<String, String> env;

    public EnvConfigurationProvider() {
        env = System.getenv();
    }

    @Override
    @Nullable
    public String get(@NotNull String key) {
        return env.get(key);
    }
}
```

## File: `agent/src/main/java/io/pyroscope/javaagent/impl/ExponentialBackoff.java`
```java
package io.pyroscope.javaagent.impl;

import java.util.Random;

/**
 * Exponential backoff counter implementing the Full Jitter algorithm from
 * <a href="https://aws.amazon.com/blogs/architecture/exponential-backoff-and-jitter/">here</a>.
 */
final class ExponentialBackoff {
    private final Random random;

    private final int base;
    private final int cap;

    private int attempt = -1;

    ExponentialBackoff(final int base, final int cap, final Random random) {
        this.base = base;
        this.cap = cap;
        this.random = random;
    }

    final int error() {
        attempt += 1;
        int multiplier = cap / base;
        // from https://docs.oracle.com/javase/specs/jls/se8/html/jls-15.html#jls-15.19
        // "If the promoted type of the left-hand operand is int, then only the five lowest-order bits of the right-hand operand are used as the shift distance".
        if (attempt < 32 && (multiplier >> attempt) > 0) {
            multiplier = 1 << attempt;
        }
        return random.nextInt(base * multiplier);
    }

    final void reset() {
        attempt = -1;
    }
}
```

## File: `agent/src/main/java/io/pyroscope/javaagent/impl/ProfilerScopedContextWrapper.java`
```java
package io.pyroscope.javaagent.impl;

import io.pyroscope.javaagent.api.ProfilerScopedContext;
import io.pyroscope.labels.v2.ScopedContext;
import org.jetbrains.annotations.NotNull;

import java.util.function.BiConsumer;

public class ProfilerScopedContextWrapper implements ProfilerScopedContext {
    private final ScopedContext ctx;

    public ProfilerScopedContextWrapper(@NotNull ScopedContext ctx) {
        this.ctx = ctx;
    }

    @Override
    public void forEachLabel(@NotNull BiConsumer<@NotNull String, @NotNull String> consumer) {
        ctx.forEachLabel(consumer);
    }

    @Override
    public void close() {
        ctx.close();
    }
}
```

## File: `agent/src/main/java/io/pyroscope/javaagent/impl/PropertiesConfigurationProvider.java`
```java
package io.pyroscope.javaagent.impl;

import io.pyroscope.javaagent.api.ConfigurationProvider;
import org.jetbrains.annotations.NotNull;
import org.jetbrains.annotations.Nullable;

import java.io.IOException;
import java.io.InputStream;
import java.util.Locale;
import java.util.Properties;

public class PropertiesConfigurationProvider implements ConfigurationProvider {
    final Properties properties;

    public PropertiesConfigurationProvider(Properties properties) {
        this.properties = properties;
    }

    public PropertiesConfigurationProvider(InputStream source) throws IOException {
        this.properties = new Properties();
        this.properties.load(source);
    }

    @Override
    @Nullable
    public String get(@NotNull String key) {
        String v = properties.getProperty(key);
        if (v == null) {
            String k2 = key.toLowerCase(Locale.ROOT)
                .replace('_', '.');
            v = properties.getProperty(k2);
        }
        return v;
    }
}
```

## File: `agent/src/main/java/io/pyroscope/javaagent/impl/PyroscopeExporter.java`
```java
package io.pyroscope.javaagent.impl;

import io.pyroscope.javaagent.EventType;
import io.pyroscope.javaagent.Snapshot;
import io.pyroscope.javaagent.api.Exporter;
import io.pyroscope.javaagent.api.Logger;
import io.pyroscope.javaagent.config.Config;
import io.pyroscope.javaagent.util.zip.GzipSink;
import io.pyroscope.labels.v2.Pyroscope;
import okhttp3.*;
import org.jetbrains.annotations.NotNull;

import java.io.IOException;
import java.time.Instant;
import java.util.Random;
import java.util.zip.Deflater;

public class PyroscopeExporter implements Exporter {

    private static final MediaType PROTOBUF = MediaType.parse("application/x-protobuf");

    final Config config;
    final Logger logger;
    final OkHttpClient client;
    final String staticLabels;
    public PyroscopeExporter(Config config, Logger logger) {
        this.config = config;
        this.logger = logger;
        this.staticLabels = nameWithStaticLabels(); 
        this.client = new OkHttpClient.Builder()
            .connectTimeout(config.profileExportTimeout)
            .readTimeout(config.profileExportTimeout)
            .callTimeout(config.profileExportTimeout)
            .build();

    }

    @Override
    public void export(@NotNull Snapshot snapshot) {
        try {
            uploadSnapshot(snapshot);
        } catch (final InterruptedException ignored) {
            Thread.currentThread().interrupt();
        }
    }

    @Override
    public void stop() {
        client.dispatcher().executorService().shutdown();
        client.connectionPool().evictAll();
        try {
            if (client.cache() != null) {
                client.cache().close();
            }
        }
        catch (final IOException ignored) {}
    }

    private void uploadSnapshot(final Snapshot snapshot) throws InterruptedException {
        final HttpUrl url = urlForSnapshot(snapshot);
        final ExponentialBackoff exponentialBackoff = new ExponentialBackoff(1_000, 30_000, new Random());
        boolean retry = true;
        int tries = 0;
        while (retry) {
            tries++;
            final RequestBody requestBody;
            byte[] labels = snapshot.labels.toByteArray();
            logger.log(Logger.Level.DEBUG, "Upload attempt %d to %s. %s %s JFR: %s, labels: %s", tries, url.toString(),
                snapshot.started.toString(), snapshot.ended.toString(), snapshot.data.length, labels.length);
            MultipartBody.Builder bodyBuilder = new MultipartBody.Builder()
                .setType(MultipartBody.FORM);
            RequestBody jfrBody = RequestBody.create(snapshot.data);
            if (config.compressionLevelJFR != Deflater.NO_COMPRESSION) {
                jfrBody = GzipSink.gzip(jfrBody, config.compressionLevelJFR);
            }
            bodyBuilder.addFormDataPart("jfr", "jfr", jfrBody);
            if (labels.length > 0) {
                RequestBody labelsBody = RequestBody.create(labels, PROTOBUF);
                if (config.compressionLevelLabels != Deflater.NO_COMPRESSION) {
                    labelsBody = GzipSink.gzip(labelsBody, config.compressionLevelLabels);
                }
                bodyBuilder.addFormDataPart("labels", "labels", labelsBody);
            }
            requestBody = bodyBuilder.build();
            Request.Builder request = new Request.Builder()
                .post(requestBody)
                .url(url);

            config.httpHeaders.forEach((k, v) -> request.header(k, v));

            addAuthHeader(request, url, config);


            try (Response response = client.newCall(request.build()).execute()) {
                int status = response.code();
                if (status >= 400) {
                    ResponseBody body = response.body();
                    final String responseBody;
                    if (body == null) {
                        responseBody = "";
                    } else {
                        responseBody = body.string();
                    }
                    logger.log(Logger.Level.ERROR, "Error uploading snapshot: %s %s", status, responseBody);
                    retry = shouldRetry(status);
                } else {
                    retry = false;
                }
            } catch (final IOException e) {
                logger.log(Logger.Level.ERROR, "Error uploading snapshot: %s", e.getMessage());
            }
            if (retry) {
                if (config.ingestMaxTries >= 0 && tries >= config.ingestMaxTries) {
                    logger.log(Logger.Level.ERROR, "Gave up uploading profiling snapshot after %d tries", tries);
                    break;
                }
                final int backoff = exponentialBackoff.error();
                logger.log(Logger.Level.DEBUG, "Backing off for %s ms", backoff);
                Thread.sleep(backoff);
            }
        }
    }

    private static boolean shouldRetry(int status) {
        boolean isRateLimited = (status == 429);
        boolean isServerError = (status >= 500 && status <= 599);
        
        return isRateLimited || isServerError;
    }

    private static void addAuthHeader(Request.Builder request, HttpUrl url, Config config) {
        if (config.tenantID != null && !config.tenantID.isEmpty()) {
            request.header("X-Scope-OrgID", config.tenantID);
        }
        if (config.basicAuthUser != null && !config.basicAuthUser.isEmpty()
            && config.basicAuthPassword != null && !config.basicAuthPassword.isEmpty()) {
            request.header("Authorization", Credentials.basic(config.basicAuthUser, config.basicAuthPassword));
            return;
        }
        String u = url.username();
        String p = url.password();
        if (!u.isEmpty() && !p.isEmpty()) {
            request.header("Authorization", Credentials.basic(u, p));
            return;
        }
        if (config.authToken != null && !config.authToken.isEmpty()) {
            request.header("Authorization", "Bearer " + config.authToken);
        }
    }

    private HttpUrl urlForSnapshot(final Snapshot snapshot) {
        Instant started = snapshot.started;
        Instant finished = snapshot.ended;
        HttpUrl.Builder builder = HttpUrl.parse(config.serverAddress)
            .newBuilder()
            .addPathSegment("ingest")
            .addQueryParameter("name", staticLabels)
            .addQueryParameter("units", snapshot.eventType.units.id)
            .addQueryParameter("aggregationType", snapshot.eventType.aggregationType.id)
            .addQueryParameter("from", Long.toString(started.getEpochSecond()))
            .addQueryParameter("until", Long.toString(finished.getEpochSecond()))
            .addQueryParameter("spyName", Config.DEFAULT_SPY_NAME);
        if (EventType.CPU == snapshot.eventType || EventType.ITIMER == snapshot.eventType || EventType.WALL == snapshot.eventType) {
            builder.addQueryParameter("sampleRate", Long.toString(config.profilingIntervalInHertz()));
        }
        builder.addQueryParameter("format", "jfr");
        return builder.build();
    }

    private String nameWithStaticLabels() {
        return config.timeseries.newBuilder()
            .addLabels(config.labels)
            .addLabels(Pyroscope.getStaticLabels())
            .build()
            .toString();
    }
}
```

## File: `agent/src/main/java/io/pyroscope/javaagent/impl/QueuedExporter.java`
```java
package io.pyroscope.javaagent.impl;

import io.pyroscope.javaagent.OverfillQueue;
import io.pyroscope.javaagent.Snapshot;
import io.pyroscope.javaagent.api.Exporter;
import io.pyroscope.javaagent.api.Logger;
import io.pyroscope.javaagent.config.Config;
import org.jetbrains.annotations.NotNull;

public class QueuedExporter implements Exporter {
    final Exporter impl;
    final Logger logger;
    private final Thread thread;
    private final OverfillQueue<Snapshot> queue;

    public QueuedExporter(Config config, Exporter impl, Logger logger) {
        this.impl = impl;
        this.logger = logger;
        this.thread = new Thread(this::exportLoop);
        this.thread.setDaemon(true);
        this.queue = new OverfillQueue<>(config.pushQueueCapacity);

        this.thread.start();
    }

    private void exportLoop() {
        logger.log(Logger.Level.DEBUG, "Uploading started");
        try {
            while (!Thread.currentThread().isInterrupted()) {
                final Snapshot snapshot = queue.take();
                impl.export(snapshot);
            }
        } catch (final InterruptedException e) {
            logger.log(Logger.Level.DEBUG, "Uploading interrupted");
            Thread.currentThread().interrupt();
        }
    }

    @Override
    public void export(@NotNull Snapshot snapshot) {
        try {
            queue.put(snapshot);
        } catch (final InterruptedException ignored) {
            Thread.currentThread().interrupt();
        }
    }

    @Override
    public void stop() {
        try {
            this.thread.interrupt();
        } catch (Exception e) {
            logger.log(Logger.Level.ERROR, "Error stopping thread", e);
        }
    }
}
```

## File: `agent/src/main/java/io/pyroscope/javaagent/impl/SamplingProfilingScheduler.java`
```java
package io.pyroscope.javaagent.impl;


import io.pyroscope.javaagent.AsyncProfilerDelegate;
import io.pyroscope.javaagent.EventType;
import io.pyroscope.javaagent.ProfilerDelegate;
import io.pyroscope.javaagent.Snapshot;
import io.pyroscope.javaagent.api.Exporter;
import io.pyroscope.javaagent.api.Logger;
import io.pyroscope.javaagent.api.ProfilingScheduler;
import io.pyroscope.javaagent.config.Config;
import kotlin.random.Random;

import io.pyroscope.javaagent.config.Config.Builder;
import org.jetbrains.annotations.NotNull;

import java.time.Duration;
import java.time.Instant;
import java.util.concurrent.Executors;
import java.util.concurrent.ScheduledExecutorService;
import java.util.concurrent.ScheduledFuture;
import java.util.concurrent.TimeUnit;

/**
 * Schedule profiling in sampling mode.
 * <p>
 * WARNING: still experimental, may go away or behavior may change
 */
public class SamplingProfilingScheduler implements ProfilingScheduler {

    private final Config config;
    private final Exporter exporter;
    private Logger logger;

    private final ScheduledExecutorService executor = Executors.newSingleThreadScheduledExecutor(r -> {
        Thread t = Executors.defaultThreadFactory().newThread(r);
        t.setName("PyroscopeProfilingScheduler_Sampling");
        t.setDaemon(true);
        return t;
    });
    private ScheduledFuture<?> job;

    public SamplingProfilingScheduler(@NotNull Config config, @NotNull Exporter exporter, @NotNull Logger logger) {
        this.config = config;
        this.exporter = exporter;
        this.logger = logger;
    }

    @Override
    public void start(@NotNull ProfilerDelegate profiler) {
        final long samplingDurationMillis = config.samplingDuration.toMillis();
        final Duration uploadInterval = config.uploadInterval;

        final Runnable task = (null != config.samplingEventOrder) ?
                () -> {
                    for (int i = 0; i < config.samplingEventOrder.size(); i++) {
                        final EventType t = config.samplingEventOrder.get(i);
                        final Config tmp = isolate(t, config);
                        logger.log(Logger.Level.DEBUG, "Config for %s ordinal %d: %s", t.id, i, tmp);
                        profiler.setConfig(tmp);
                        dumpProfile(profiler, samplingDurationMillis, uploadInterval);
                    }
                } :
                () -> dumpProfile(profiler, samplingDurationMillis, uploadInterval);

        Duration initialDelay = getInitialDelay();
        job = executor.scheduleAtFixedRate(
                task,
                initialDelay.toMillis(),
                config.uploadInterval.toMillis(),
                TimeUnit.MILLISECONDS
        );
    }

    @Override
    public void stop() {
        throw new RuntimeException("not implemented");
    }

    private void dumpProfile(final ProfilerDelegate profiler, final long samplingDurationMillis, final Duration uploadInterval) {
        Instant profilingStartTime = Instant.now();
        try {
            profiler.start();
        } catch (Throwable e) {
            logger.log(Logger.Level.ERROR, "Error starting profiler %s", e);
            stopProfiling();
            return;
        }
        try {
            Thread.sleep(samplingDurationMillis);
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
        profiler.stop();

        Snapshot snapshot = profiler.dumpProfile(profilingStartTime, Instant.now());
        exporter.export(snapshot);
    }

    private void stopProfiling() {
        if (job != null) {
            job.cancel(true);
        }
        executor.shutdown();
    }

    private Duration getInitialDelay() {
        long uploadIntervalMillis = config.uploadInterval.toMillis();
        float randomOffset = Random.Default.nextFloat();
        uploadIntervalMillis = (long) ((float) uploadIntervalMillis * randomOffset);
        if (uploadIntervalMillis < 2000) {
            uploadIntervalMillis = 2000;
        }
        Duration firstProfilingDuration = Duration.ofMillis(uploadIntervalMillis);
        return firstProfilingDuration;
    }

    private Config isolate(final EventType type, final Config config) {
        final Builder b = new Builder(config);
        b.setProfilingEvent(type);
        if (!EventType.ALLOC.equals(type))
            b.setProfilingAlloc("");
        if (!EventType.LOCK.equals(type))
            b.setProfilingLock("");
        return b.build();
    }
}
```

## File: `agent/src/main/java/io/pyroscope/javaagent/util/zip/GzipSink.java`
```java
/*
 * Copyright (C) 2014 Square, Inc.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package io.pyroscope.javaagent.util.zip;

import java.io.IOException;
import java.util.zip.CRC32;
import java.util.zip.Deflater;

import kotlin.jvm.internal.Intrinsics;
import okhttp3.MediaType;
import okhttp3.RequestBody;
import okio.*;
import org.jetbrains.annotations.NotNull;
import org.jetbrains.annotations.Nullable;


@SuppressWarnings("KotlinInternalInJava")
public final class GzipSink implements Sink {
    private final BufferedSink sink;
    @NotNull
    private final Deflater deflater;
    private final DeflaterSink deflaterSink;
    private boolean closed;
    private final CRC32 crc;


    public GzipSink(@NotNull Sink sink, int compressionLevel) {
        Intrinsics.checkNotNullParameter(sink, "sink");
        this.sink = Okio.buffer(sink);
        this.deflater = new Deflater(compressionLevel, true);
        this.deflaterSink = new DeflaterSink((BufferedSink) this.sink, this.deflater);
        this.crc = new CRC32();

        // Write the Gzip header directly into the buffer for the sink to avoid handling IOException.
        Buffer buf = this.sink.getBuffer();
        buf.writeShort(0x1f8b); // Two-byte Gzip ID.
        buf.writeByte(8); // 8 == Deflate compression method.
        buf.writeByte(0); // No flags.
        buf.writeInt(0); // No modification time.
        buf.writeByte(0); // No extra flags.
        buf.writeByte(0); // No OS.
    }

    @Override
    public void write(@NotNull Buffer source, long byteCount) throws IOException {
//        require(byteCount >= 0L) { "byteCount < 0: $byteCount" }
        if (!(byteCount >= 0L)) {
            throw new IllegalArgumentException("byteCount < 0: " + byteCount);
        }
        if (byteCount == 0L) return;
        updateCrc(source, byteCount);
        deflaterSink.write(source, byteCount);
    }


    @Override
    public void close() throws IOException {
        throw new IllegalStateException("should not be called. use end");
    }

    // almost same as okio.GzipSink.close but does sink.flush instead of sink.close
    public void end() throws IOException {
        if (!this.closed) {
            Throwable thrown = null;

            try {
                this.deflaterSink.finishDeflate$okio();
                this.writeFooter();
            } catch (Throwable var3) {
                thrown = var3;
            }

            try {
                this.deflater.end();
            } catch (Throwable var5) {
                if (thrown == null) {
                    thrown = var5;
                }
            }

            try {
                this.sink.flush();
            } catch (Throwable var4) {
                if (thrown == null) {
                    thrown = var4;
                }
            }

            this.closed = true;
            if (thrown != null) {
                Util.sneakyRethrow(thrown);
            }
        }
    }

    @Override
    public void flush() throws IOException {
        deflaterSink.flush();
    }

    @NotNull
    @Override
    public Timeout timeout() {
        return sink.timeout();
    }

    private void updateCrc(Buffer buffer, long byteCount) {
        Segment head = buffer.head;
        Intrinsics.checkNotNull(head);
        long remaining = byteCount;
        while (remaining > 0) {
            int segmentLength = (int) Math.min(remaining, head.limit - head.pos);
            this.crc.update(head.data, head.pos, segmentLength);
            remaining -= segmentLength;
            head = head.next;
            Intrinsics.checkNotNull(head);
        }
    }

    private final void writeFooter() throws IOException {
        this.sink.writeIntLe((int) this.crc.getValue());
        this.sink.writeIntLe((int) this.deflater.getBytesRead());
    }


    /**
     * <a href="https://github.com/square/okhttp/blob/64a9c8e4db394097fe6150915fcea7a7f11572a9/okhttp/src/jvmMain/kotlin/okhttp3/RequestBody.kt#L184">origin</a>
     * Returns a gzip version of the RequestBody, with compressed payload.
     * This is not automatic as not all servers support gzip compressed requests.
     * <p>
     * ```
     * val request = Request.Builder().url("...")
     * .addHeader("Content-Encoding", "gzip")
     * .post(uncompressedBody.gzip())
     * .build()
     * ```
     */
    public static RequestBody gzip(RequestBody req, int compressionLevel) {
        return new RequestBody() {
            @Nullable
            @Override
            public MediaType contentType() {
                return req.contentType();
            }

            @Override
            public long contentLength() throws IOException {
                return -1;// We don't know the compressed length in advance!
            }

            @Override
            public void writeTo(@NotNull BufferedSink sink) throws IOException {
                GzipSink gzipSink = new GzipSink(sink, compressionLevel);
                BufferedSink buffer = Okio.buffer(gzipSink);
                req.writeTo(buffer);
                // do not close gzipSink & buffer to avoid closing upstream sink
                // do flushes instead
                buffer.flush();
                gzipSink.end();
            }

            @Override
            public boolean isOneShot() {
                return req.isOneShot();
            }
        };
    }

}
```

## File: `agent/src/main/java/io/pyroscope/javaagent/util/zip/Util.java`
```java
/*
 * Copyright (C) 2014 Square, Inc.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package io.pyroscope.javaagent.util.zip;

public class Util {
    /**
     * <a href="https://github.com/square/okio/blob/f60e79ec801ba517a73acaf951e2a089d43666fc/okio/src/main/java/okio/Util.java#L59">origin</a>
     * Throws {@code t}, even if the declared throws clause doesn't permit it.
     * This is a terrible – but terribly convenient – hack that makes it easy to
     * catch and rethrow exceptions after cleanup. See Java Puzzlers #43.
     */
    public static void sneakyRethrow(Throwable t) {
        Util.<Error> sneakyThrow2(t);
    }

    @SuppressWarnings("unchecked")
    private static <T extends Throwable> void sneakyThrow2(Throwable t) throws T {
        throw (T) t;
    }
}
```

## File: `agent/src/main/java/io/pyroscope/labels/pb/JfrLabels.java`
```java
// Generated by the protocol buffer compiler.  DO NOT EDIT!
// source: jfr_labels.proto
// Protobuf Java Version: 4.26.1

package io.pyroscope.labels.pb;

public final class JfrLabels {
  private JfrLabels() {}
  static {
    com.google.protobuf.RuntimeVersion.validateProtobufGencodeVersion(
      com.google.protobuf.RuntimeVersion.RuntimeDomain.PUBLIC,
      /* major= */ 4,
      /* minor= */ 26,
      /* patch= */ 1,
      /* suffix= */ "",
      JfrLabels.class.getName());
  }
  public static void registerAllExtensions(
      com.google.protobuf.ExtensionRegistryLite registry) {
  }

  public static void registerAllExtensions(
      com.google.protobuf.ExtensionRegistry registry) {
    registerAllExtensions(
        (com.google.protobuf.ExtensionRegistryLite) registry);
  }
  public interface ContextOrBuilder extends
      // @@protoc_insertion_point(interface_extends:io.pyroscope.labels.pb.Context)
      com.google.protobuf.MessageOrBuilder {

    /**
     * <code>map&lt;int64, int64&gt; labels = 1;</code>
     */
    int getLabelsCount();
    /**
     * <code>map&lt;int64, int64&gt; labels = 1;</code>
     */
    boolean containsLabels(
        long key);
    /**
     * Use {@link #getLabelsMap()} instead.
     */
    @java.lang.Deprecated
    java.util.Map<java.lang.Long, java.lang.Long>
    getLabels();
    /**
     * <code>map&lt;int64, int64&gt; labels = 1;</code>
     */
    java.util.Map<java.lang.Long, java.lang.Long>
    getLabelsMap();
    /**
     * <code>map&lt;int64, int64&gt; labels = 1;</code>
     */
    long getLabelsOrDefault(
        long key,
        long defaultValue);
    /**
     * <code>map&lt;int64, int64&gt; labels = 1;</code>
     */
    long getLabelsOrThrow(
        long key);
  }
  /**
   * Protobuf type {@code io.pyroscope.labels.pb.Context}
   */
  public static final class Context extends
      com.google.protobuf.GeneratedMessage implements
      // @@protoc_insertion_point(message_implements:io.pyroscope.labels.pb.Context)
      ContextOrBuilder {
  private static final long serialVersionUID = 0L;
    static {
      com.google.protobuf.RuntimeVersion.validateProtobufGencodeVersion(
        com.google.protobuf.RuntimeVersion.RuntimeDomain.PUBLIC,
        /* major= */ 4,
        /* minor= */ 26,
        /* patch= */ 1,
        /* suffix= */ "",
        Context.class.getName());
    }
    // Use Context.newBuilder() to construct.
    private Context(com.google.protobuf.GeneratedMessage.Builder<?> builder) {
      super(builder);
    }
    private Context() {
    }

    public static final com.google.protobuf.Descriptors.Descriptor
        getDescriptor() {
      return io.pyroscope.labels.pb.JfrLabels.internal_static_io_pyroscope_labels_pb_Context_descriptor;
    }

    @SuppressWarnings({"rawtypes"})
    @java.lang.Override
    protected com.google.protobuf.MapFieldReflectionAccessor internalGetMapFieldReflection(
        int number) {
      switch (number) {
        case 1:
          return internalGetLabels();
        default:
          throw new RuntimeException(
              "Invalid map field number: " + number);
      }
    }
    @java.lang.Override
    protected com.google.protobuf.GeneratedMessage.FieldAccessorTable
        internalGetFieldAccessorTable() {
      return io.pyroscope.labels.pb.JfrLabels.internal_static_io_pyroscope_labels_pb_Context_fieldAccessorTable
          .ensureFieldAccessorsInitialized(
              io.pyroscope.labels.pb.JfrLabels.Context.class, io.pyroscope.labels.pb.JfrLabels.Context.Builder.class);
    }

    public static final int LABELS_FIELD_NUMBER = 1;
    private static final class LabelsDefaultEntryHolder {
      static final com.google.protobuf.MapEntry<
          java.lang.Long, java.lang.Long> defaultEntry =
              com.google.protobuf.MapEntry
              .<java.lang.Long, java.lang.Long>newDefaultInstance(
                  io.pyroscope.labels.pb.JfrLabels.internal_static_io_pyroscope_labels_pb_Context_LabelsEntry_descriptor, 
                  com.google.protobuf.WireFormat.FieldType.INT64,
                  0L,
                  com.google.protobuf.WireFormat.FieldType.INT64,
                  0L);
    }
    @SuppressWarnings("serial")
    private com.google.protobuf.MapField<
        java.lang.Long, java.lang.Long> labels_;
    private com.google.protobuf.MapField<java.lang.Long, java.lang.Long>
    internalGetLabels() {
      if (labels_ == null) {
        return com.google.protobuf.MapField.emptyMapField(
            LabelsDefaultEntryHolder.defaultEntry);
      }
      return labels_;
    }
    public int getLabelsCount() {
      return internalGetLabels().getMap().size();
    }
    /**
     * <code>map&lt;int64, int64&gt; labels = 1;</code>
     */
    @java.lang.Override
    public boolean containsLabels(
        long key) {

      return internalGetLabels().getMap().containsKey(key);
    }
    /**
     * Use {@link #getLabelsMap()} instead.
     */
    @java.lang.Override
    @java.lang.Deprecated
    public java.util.Map<java.lang.Long, java.lang.Long> getLabels() {
      return getLabelsMap();
    }
    /**
     * <code>map&lt;int64, int64&gt; labels = 1;</code>
     */
    @java.lang.Override
    public java.util.Map<java.lang.Long, java.lang.Long> getLabelsMap() {
      return internalGetLabels().getMap();
    }
    /**
     * <code>map&lt;int64, int64&gt; labels = 1;</code>
     */
    @java.lang.Override
    public long getLabelsOrDefault(
        long key,
        long defaultValue) {

      java.util.Map<java.lang.Long, java.lang.Long> map =
          internalGetLabels().getMap();
      return map.containsKey(key) ? map.get(key) : defaultValue;
    }
    /**
     * <code>map&lt;int64, int64&gt; labels = 1;</code>
     */
    @java.lang.Override
    public long getLabelsOrThrow(
        long key) {

      java.util.Map<java.lang.Long, java.lang.Long> map =
          internalGetLabels().getMap();
      if (!map.containsKey(key)) {
        throw new java.lang.IllegalArgumentException();
      }
      return map.get(key);
    }

    private byte memoizedIsInitialized = -1;
    @java.lang.Override
    public final boolean isInitialized() {
      byte isInitialized = memoizedIsInitialized;
      if (isInitialized == 1) return true;
      if (isInitialized == 0) return false;

      memoizedIsInitialized = 1;
      return true;
    }

    @java.lang.Override
    public void writeTo(com.google.protobuf.CodedOutputStream output)
                        throws java.io.IOException {
      com.google.protobuf.GeneratedMessage
        .serializeLongMapTo(
          output,
          internalGetLabels(),
          LabelsDefaultEntryHolder.defaultEntry,
          1);
      getUnknownFields().writeTo(output);
    }

    @java.lang.Override
    public int getSerializedSize() {
      int size = memoizedSize;
      if (size != -1) return size;

      size = 0;
      for (java.util.Map.Entry<java.lang.Long, java.lang.Long> entry
           : internalGetLabels().getMap().entrySet()) {
        com.google.protobuf.MapEntry<java.lang.Long, java.lang.Long>
        labels__ = LabelsDefaultEntryHolder.defaultEntry.newBuilderForType()
            .setKey(entry.getKey())
            .setValue(entry.getValue())
            .build();
        size += com.google.protobuf.CodedOutputStream
            .computeMessageSize(1, labels__);
      }
      size += getUnknownFields().getSerializedSize();
      memoizedSize = size;
      return size;
    }

    @java.lang.Override
    public boolean equals(final java.lang.Object obj) {
      if (obj == this) {
       return true;
      }
      if (!(obj instanceof io.pyroscope.labels.pb.JfrLabels.Context)) {
        return super.equals(obj);
      }
      io.pyroscope.labels.pb.JfrLabels.Context other = (io.pyroscope.labels.pb.JfrLabels.Context) obj;

      if (!internalGetLabels().equals(
          other.internalGetLabels())) return false;
      if (!getUnknownFields().equals(other.getUnknownFields())) return false;
      return true;
    }

    @java.lang.Override
    public int hashCode() {
      if (memoizedHashCode != 0) {
        return memoizedHashCode;
      }
      int hash = 41;
      hash = (19 * hash) + getDescriptor().hashCode();
      if (!internalGetLabels().getMap().isEmpty()) {
        hash = (37 * hash) + LABELS_FIELD_NUMBER;
        hash = (53 * hash) + internalGetLabels().hashCode();
      }
      hash = (29 * hash) + getUnknownFields().hashCode();
      memoizedHashCode = hash;
      return hash;
    }

    public static io.pyroscope.labels.pb.JfrLabels.Context parseFrom(
        java.nio.ByteBuffer data)
        throws com.google.protobuf.InvalidProtocolBufferException {
      return PARSER.parseFrom(data);
    }
    public static io.pyroscope.labels.pb.JfrLabels.Context parseFrom(
        java.nio.ByteBuffer data,
        com.google.protobuf.ExtensionRegistryLite extensionRegistry)
        throws com.google.protobuf.InvalidProtocolBufferException {
      return PARSER.parseFrom(data, extensionRegistry);
    }
    public static io.pyroscope.labels.pb.JfrLabels.Context parseFrom(
        com.google.protobuf.ByteString data)
        throws com.google.protobuf.InvalidProtocolBufferException {
      return PARSER.parseFrom(data);
    }
    public static io.pyroscope.labels.pb.JfrLabels.Context parseFrom(
        com.google.protobuf.ByteString data,
        com.google.protobuf.ExtensionRegistryLite extensionRegistry)
        throws com.google.protobuf.InvalidProtocolBufferException {
      return PARSER.parseFrom(data, extensionRegistry);
    }
    public static io.pyroscope.labels.pb.JfrLabels.Context parseFrom(byte[] data)
        throws com.google.protobuf.InvalidProtocolBufferException {
      return PARSER.parseFrom(data);
    }
    public static io.pyroscope.labels.pb.JfrLabels.Context parseFrom(
        byte[] data,
        com.google.protobuf.ExtensionRegistryLite extensionRegistry)
        throws com.google.protobuf.InvalidProtocolBufferException {
      return PARSER.parseFrom(data, extensionRegistry);
    }
    public static io.pyroscope.labels.pb.JfrLabels.Context parseFrom(java.io.InputStream input)
        throws java.io.IOException {
      return com.google.protobuf.GeneratedMessage
          .parseWithIOException(PARSER, input);
    }
    public static io.pyroscope.labels.pb.JfrLabels.Context parseFrom(
        java.io.InputStream input,
        com.google.protobuf.ExtensionRegistryLite extensionRegistry)
        throws java.io.IOException {
      return com.google.protobuf.GeneratedMessage
          .parseWithIOException(PARSER, input, extensionRegistry);
    }

    public static io.pyroscope.labels.pb.JfrLabels.Context parseDelimitedFrom(java.io.InputStream input)
        throws java.io.IOException {
      return com.google.protobuf.GeneratedMessage
          .parseDelimitedWithIOException(PARSER, input);
    }

    public static io.pyroscope.labels.pb.JfrLabels.Context parseDelimitedFrom(
        java.io.InputStream input,
        com.google.protobuf.ExtensionRegistryLite extensionRegistry)
        throws java.io.IOException {
      return com.google.protobuf.GeneratedMessage
          .parseDelimitedWithIOException(PARSER, input, extensionRegistry);
    }
    public static io.pyroscope.labels.pb.JfrLabels.Context parseFrom(
        com.google.protobuf.CodedInputStream input)
        throws java.io.IOException {
      return com.google.protobuf.GeneratedMessage
          .parseWithIOException(PARSER, input);
    }
    public static io.pyroscope.labels.pb.JfrLabels.Context parseFrom(
        com.google.protobuf.CodedInputStream input,
        com.google.protobuf.ExtensionRegistryLite extensionRegistry)
        throws java.io.IOException {
      return com.google.protobuf.GeneratedMessage
          .parseWithIOException(PARSER, input, extensionRegistry);
    }

    @java.lang.Override
    public Builder newBuilderForType() { return newBuilder(); }
    public static Builder newBuilder() {
      return DEFAULT_INSTANCE.toBuilder();
    }
    public static Builder newBuilder(io.pyroscope.labels.pb.JfrLabels.Context prototype) {
      return DEFAULT_INSTANCE.toBuilder().mergeFrom(prototype);
    }
    @java.lang.Override
    public Builder toBuilder() {
      return this == DEFAULT_INSTANCE
          ? new Builder() : new Builder().mergeFrom(this);
    }

    @java.lang.Override
    protected Builder newBuilderForType(
        com.google.protobuf.GeneratedMessage.BuilderParent parent) {
      Builder builder = new Builder(parent);
      return builder;
    }
    /**
     * Protobuf type {@code io.pyroscope.labels.pb.Context}
     */
    public static final class Builder extends
        com.google.protobuf.GeneratedMessage.Builder<Builder> implements
        // @@protoc_insertion_point(builder_implements:io.pyroscope.labels.pb.Context)
        io.pyroscope.labels.pb.JfrLabels.ContextOrBuilder {
      public static final com.google.protobuf.Descriptors.Descriptor
          getDescriptor() {
        return io.pyroscope.labels.pb.JfrLabels.internal_static_io_pyroscope_labels_pb_Context_descriptor;
      }

      @SuppressWarnings({"rawtypes"})
      protected com.google.protobuf.MapFieldReflectionAccessor internalGetMapFieldReflection(
          int number) {
        switch (number) {
          case 1:
            return internalGetLabels();
          default:
            throw new RuntimeException(
                "Invalid map field number: " + number);
        }
      }
      @SuppressWarnings({"rawtypes"})
      protected com.google.protobuf.MapFieldReflectionAccessor internalGetMutableMapFieldReflection(
          int number) {
        switch (number) {
          case 1:
            return internalGetMutableLabels();
          default:
            throw new RuntimeException(
                "Invalid map field number: " + number);
        }
      }
      @java.lang.Override
      protected com.google.protobuf.GeneratedMessage.FieldAccessorTable
          internalGetFieldAccessorTable() {
        return io.pyroscope.labels.pb.JfrLabels.internal_static_io_pyroscope_labels_pb_Context_fieldAccessorTable
            .ensureFieldAccessorsInitialized(
                io.pyroscope.labels.pb.JfrLabels.Context.class, io.pyroscope.labels.pb.JfrLabels.Context.Builder.class);
      }

      // Construct using io.pyroscope.labels.pb.JfrLabels.Context.newBuilder()
      private Builder() {

      }

      private Builder(
          com.google.protobuf.GeneratedMessage.BuilderParent parent) {
        super(parent);

      }
      @java.lang.Override
      public Builder clear() {
        super.clear();
        bitField0_ = 0;
        internalGetMutableLabels().clear();
        return this;
      }

      @java.lang.Override
      public com.google.protobuf.Descriptors.Descriptor
          getDescriptorForType() {
        return io.pyroscope.labels.pb.JfrLabels.internal_static_io_pyroscope_labels_pb_Context_descriptor;
      }

      @java.lang.Override
      public io.pyroscope.labels.pb.JfrLabels.Context getDefaultInstanceForType() {
        return io.pyroscope.labels.pb.JfrLabels.Context.getDefaultInstance();
      }

      @java.lang.Override
      public io.pyroscope.labels.pb.JfrLabels.Context build() {
        io.pyroscope.labels.pb.JfrLabels.Context result = buildPartial();
        if (!result.isInitialized()) {
          throw newUninitializedMessageException(result);
        }
        return result;
      }

      @java.lang.Override
      public io.pyroscope.labels.pb.JfrLabels.Context buildPartial() {
        io.pyroscope.labels.pb.JfrLabels.Context result = new io.pyroscope.labels.pb.JfrLabels.Context(this);
        if (bitField0_ != 0) { buildPartial0(result); }
        onBuilt();
        return result;
      }

      private void buildPartial0(io.pyroscope.labels.pb.JfrLabels.Context result) {
        int from_bitField0_ = bitField0_;
        if (((from_bitField0_ & 0x00000001) != 0)) {
          result.labels_ = internalGetLabels();
          result.labels_.makeImmutable();
        }
      }

      @java.lang.Override
      public Builder mergeFrom(com.google.protobuf.Message other) {
        if (other instanceof io.pyroscope.labels.pb.JfrLabels.Context) {
          return mergeFrom((io.pyroscope.labels.pb.JfrLabels.Context)other);
        } else {
          super.mergeFrom(other);
          return this;
        }
      }

      public Builder mergeFrom(io.pyroscope.labels.pb.JfrLabels.Context other) {
        if (other == io.pyroscope.labels.pb.JfrLabels.Context.getDefaultInstance()) return this;
        internalGetMutableLabels().mergeFrom(
            other.internalGetLabels());
        bitField0_ |= 0x00000001;
        this.mergeUnknownFields(other.getUnknownFields());
        onChanged();
        return this;
      }

      @java.lang.Override
      public final boolean isInitialized() {
        return true;
      }

      @java.lang.Override
      public Builder mergeFrom(
          com.google.protobuf.CodedInputStream input,
          com.google.protobuf.ExtensionRegistryLite extensionRegistry)
          throws java.io.IOException {
        if (extensionRegistry == null) {
          throw new java.lang.NullPointerException();
        }
        try {
          boolean done = false;
          while (!done) {
            int tag = input.readTag();
            switch (tag) {
              case 0:
                done = true;
                break;
              case 10: {
                com.google.protobuf.MapEntry<java.lang.Long, java.lang.Long>
                labels__ = input.readMessage(
                    LabelsDefaultEntryHolder.defaultEntry.getParserForType(), extensionRegistry);
                internalGetMutableLabels().getMutableMap().put(
                    labels__.getKey(), labels__.getValue());
                bitField0_ |= 0x00000001;
                break;
              } // case 10
              default: {
                if (!super.parseUnknownField(input, extensionRegistry, tag)) {
                  done = true; // was an endgroup tag
                }
                break;
              } // default:
            } // switch (tag)
          } // while (!done)
        } catch (com.google.protobuf.InvalidProtocolBufferException e) {
          throw e.unwrapIOException();
        } finally {
          onChanged();
        } // finally
        return this;
      }
      private int bitField0_;

      private com.google.protobuf.MapField<
          java.lang.Long, java.lang.Long> labels_;
      private com.google.protobuf.MapField<java.lang.Long, java.lang.Long>
          internalGetLabels() {
        if (labels_ == null) {
          return com.google.protobuf.MapField.emptyMapField(
              LabelsDefaultEntryHolder.defaultEntry);
        }
        return labels_;
      }
      private com.google.protobuf.MapField<java.lang.Long, java.lang.Long>
          internalGetMutableLabels() {
        if (labels_ == null) {
          labels_ = com.google.protobuf.MapField.newMapField(
              LabelsDefaultEntryHolder.defaultEntry);
        }
        if (!labels_.isMutable()) {
          labels_ = labels_.copy();
        }
        bitField0_ |= 0x00000001;
        onChanged();
        return labels_;
      }
      public int getLabelsCount() {
        return internalGetLabels().getMap().size();
      }
      /**
       * <code>map&lt;int64, int64&gt; labels = 1;</code>
       */
      @java.lang.Override
      public boolean containsLabels(
          long key) {

        return internalGetLabels().getMap().containsKey(key);
      }
      /**
       * Use {@link #getLabelsMap()} instead.
       */
      @java.lang.Override
      @java.lang.Deprecated
      public java.util.Map<java.lang.Long, java.lang.Long> getLabels() {
        return getLabelsMap();
      }
      /**
       * <code>map&lt;int64, int64&gt; labels = 1;</code>
       */
      @java.lang.Override
      public java.util.Map<java.lang.Long, java.lang.Long> getLabelsMap() {
        return internalGetLabels().getMap();
      }
      /**
       * <code>map&lt;int64, int64&gt; labels = 1;</code>
       */
      @java.lang.Override
      public long getLabelsOrDefault(
          long key,
          long defaultValue) {

        java.util.Map<java.lang.Long, java.lang.Long> map =
            internalGetLabels().getMap();
        return map.containsKey(key) ? map.get(key) : defaultValue;
      }
      /**
       * <code>map&lt;int64, int64&gt; labels = 1;</code>
       */
      @java.lang.Override
      public long getLabelsOrThrow(
          long key) {

        java.util.Map<java.lang.Long, java.lang.Long> map =
            internalGetLabels().getMap();
        if (!map.containsKey(key)) {
          throw new java.lang.IllegalArgumentException();
        }
        return map.get(key);
      }
      public Builder clearLabels() {
        bitField0_ = (bitField0_ & ~0x00000001);
        internalGetMutableLabels().getMutableMap()
            .clear();
        return this;
      }
      /**
       * <code>map&lt;int64, int64&gt; labels = 1;</code>
       */
      public Builder removeLabels(
          long key) {

        internalGetMutableLabels().getMutableMap()
            .remove(key);
        return this;
      }
      /**
       * Use alternate mutation accessors instead.
       */
      @java.lang.Deprecated
      public java.util.Map<java.lang.Long, java.lang.Long>
          getMutableLabels() {
        bitField0_ |= 0x00000001;
        return internalGetMutableLabels().getMutableMap();
      }
      /**
       * <code>map&lt;int64, int64&gt; labels = 1;</code>
       */
      public Builder putLabels(
          long key,
          long value) {


        internalGetMutableLabels().getMutableMap()
            .put(key, value);
        bitField0_ |= 0x00000001;
        return this;
      }
      /**
       * <code>map&lt;int64, int64&gt; labels = 1;</code>
       */
      public Builder putAllLabels(
          java.util.Map<java.lang.Long, java.lang.Long> values) {
        internalGetMutableLabels().getMutableMap()
            .putAll(values);
        bitField0_ |= 0x00000001;
        return this;
      }

      // @@protoc_insertion_point(builder_scope:io.pyroscope.labels.pb.Context)
    }

    // @@protoc_insertion_point(class_scope:io.pyroscope.labels.pb.Context)
    private static final io.pyroscope.labels.pb.JfrLabels.Context DEFAULT_INSTANCE;
    static {
      DEFAULT_INSTANCE = new io.pyroscope.labels.pb.JfrLabels.Context();
    }

    public static io.pyroscope.labels.pb.JfrLabels.Context getDefaultInstance() {
      return DEFAULT_INSTANCE;
    }

    private static final com.google.protobuf.Parser<Context>
        PARSER = new com.google.protobuf.AbstractParser<Context>() {
      @java.lang.Override
      public Context parsePartialFrom(
          com.google.protobuf.CodedInputStream input,
          com.google.protobuf.ExtensionRegistryLite extensionRegistry)
          throws com.google.protobuf.InvalidProtocolBufferException {
        Builder builder = newBuilder();
        try {
          builder.mergeFrom(input, extensionRegistry);
        } catch (com.google.protobuf.InvalidProtocolBufferException e) {
          throw e.setUnfinishedMessage(builder.buildPartial());
        } catch (com.google.protobuf.UninitializedMessageException e) {
          throw e.asInvalidProtocolBufferException().setUnfinishedMessage(builder.buildPartial());
        } catch (java.io.IOException e) {
          throw new com.google.protobuf.InvalidProtocolBufferException(e)
              .setUnfinishedMessage(builder.buildPartial());
        }
        return builder.buildPartial();
      }
    };

    public static com.google.protobuf.Parser<Context> parser() {
      return PARSER;
    }

    @java.lang.Override
    public com.google.protobuf.Parser<Context> getParserForType() {
      return PARSER;
    }

    @java.lang.Override
    public io.pyroscope.labels.pb.JfrLabels.Context getDefaultInstanceForType() {
      return DEFAULT_INSTANCE;
    }

  }

  public interface LabelsSnapshotOrBuilder extends
      // @@protoc_insertion_point(interface_extends:io.pyroscope.labels.pb.LabelsSnapshot)
      com.google.protobuf.MessageOrBuilder {

    /**
     * <code>map&lt;int64, .io.pyroscope.labels.pb.Context&gt; contexts = 1;</code>
     */
    int getContextsCount();
    /**
     * <code>map&lt;int64, .io.pyroscope.labels.pb.Context&gt; contexts = 1;</code>
     */
    boolean containsContexts(
        long key);
    /**
     * Use {@link #getContextsMap()} instead.
     */
    @java.lang.Deprecated
    java.util.Map<java.lang.Long, io.pyroscope.labels.pb.JfrLabels.Context>
    getContexts();
    /**
     * <code>map&lt;int64, .io.pyroscope.labels.pb.Context&gt; contexts = 1;</code>
     */
    java.util.Map<java.lang.Long, io.pyroscope.labels.pb.JfrLabels.Context>
    getContextsMap();
    /**
     * <code>map&lt;int64, .io.pyroscope.labels.pb.Context&gt; contexts = 1;</code>
     */
    /* nullable */
io.pyroscope.labels.pb.JfrLabels.Context getContextsOrDefault(
        long key,
        /* nullable */
io.pyroscope.labels.pb.JfrLabels.Context defaultValue);
    /**
     * <code>map&lt;int64, .io.pyroscope.labels.pb.Context&gt; contexts = 1;</code>
     */
    io.pyroscope.labels.pb.JfrLabels.Context getContextsOrThrow(
        long key);

    /**
     * <code>map&lt;int64, string&gt; strings = 2;</code>
     */
    int getStringsCount();
    /**
     * <code>map&lt;int64, string&gt; strings = 2;</code>
     */
    boolean containsStrings(
        long key);
    /**
     * Use {@link #getStringsMap()} instead.
     */
    @java.lang.Deprecated
    java.util.Map<java.lang.Long, java.lang.String>
    getStrings();
    /**
     * <code>map&lt;int64, string&gt; strings = 2;</code>
     */
    java.util.Map<java.lang.Long, java.lang.String>
    getStringsMap();
    /**
     * <code>map&lt;int64, string&gt; strings = 2;</code>
     */
    /* nullable */
java.lang.String getStringsOrDefault(
        long key,
        /* nullable */
java.lang.String defaultValue);
    /**
     * <code>map&lt;int64, string&gt; strings = 2;</code>
     */
    java.lang.String getStringsOrThrow(
        long key);
  }
  /**
   * Protobuf type {@code io.pyroscope.labels.pb.LabelsSnapshot}
   */
  public static final class LabelsSnapshot extends
      com.google.protobuf.GeneratedMessage implements
      // @@protoc_insertion_point(message_implements:io.pyroscope.labels.pb.LabelsSnapshot)
      LabelsSnapshotOrBuilder {
  private static final long serialVersionUID = 0L;
    static {
      com.google.protobuf.RuntimeVersion.validateProtobufGencodeVersion(
        com.google.protobuf.RuntimeVersion.RuntimeDomain.PUBLIC,
        /* major= */ 4,
        /* minor= */ 26,
        /* patch= */ 1,
        /* suffix= */ "",
        LabelsSnapshot.class.getName());
    }
    // Use LabelsSnapshot.newBuilder() to construct.
    private LabelsSnapshot(com.google.protobuf.GeneratedMessage.Builder<?> builder) {
      super(builder);
    }
    private LabelsSnapshot() {
    }

    public static final com.google.protobuf.Descriptors.Descriptor
        getDescriptor() {
      return io.pyroscope.labels.pb.JfrLabels.internal_static_io_pyroscope_labels_pb_LabelsSnapshot_descriptor;
    }

    @SuppressWarnings({"rawtypes"})
    @java.lang.Override
    protected com.google.protobuf.MapFieldReflectionAccessor internalGetMapFieldReflection(
        int number) {
      switch (number) {
        case 1:
          return internalGetContexts();
        case 2:
          return internalGetStrings();
        default:
          throw new RuntimeException(
              "Invalid map field number: " + number);
      }
    }
    @java.lang.Override
    protected com.google.protobuf.GeneratedMessage.FieldAccessorTable
        internalGetFieldAccessorTable() {
      return io.pyroscope.labels.pb.JfrLabels.internal_static_io_pyroscope_labels_pb_LabelsSnapshot_fieldAccessorTable
          .ensureFieldAccessorsInitialized(
              io.pyroscope.labels.pb.JfrLabels.LabelsSnapshot.class, io.pyroscope.labels.pb.JfrLabels.LabelsSnapshot.Builder.class);
    }

    public static final int CONTEXTS_FIELD_NUMBER = 1;
    private static final class ContextsDefaultEntryHolder {
      static final com.google.protobuf.MapEntry<
          java.lang.Long, io.pyroscope.labels.pb.JfrLabels.Context> defaultEntry =
              com.google.protobuf.MapEntry
              .<java.lang.Long, io.pyroscope.labels.pb.JfrLabels.Context>newDefaultInstance(
                  io.pyroscope.labels.pb.JfrLabels.internal_static_io_pyroscope_labels_pb_LabelsSnapshot_ContextsEntry_descriptor, 
                  com.google.protobuf.WireFormat.FieldType.INT64,
                  0L,
                  com.google.protobuf.WireFormat.FieldType.MESSAGE,
                  io.pyroscope.labels.pb.JfrLabels.Context.getDefaultInstance());
    }
    @SuppressWarnings("serial")
    private com.google.protobuf.MapField<
        java.lang.Long, io.pyroscope.labels.pb.JfrLabels.Context> contexts_;
    private com.google.protobuf.MapField<java.lang.Long, io.pyroscope.labels.pb.JfrLabels.Context>
    internalGetContexts() {
      if (contexts_ == null) {
        return com.google.protobuf.MapField.emptyMapField(
            ContextsDefaultEntryHolder.defaultEntry);
      }
      return contexts_;
    }
    public int getContextsCount() {
      return internalGetContexts().getMap().size();
    }
    /**
     * <code>map&lt;int64, .io.pyroscope.labels.pb.Context&gt; contexts = 1;</code>
     */
    @java.lang.Override
    public boolean containsContexts(
        long key) {

      return internalGetContexts().getMap().containsKey(key);
    }
    /**
     * Use {@link #getContextsMap()} instead.
     */
    @java.lang.Override
    @java.lang.Deprecated
    public java.util.Map<java.lang.Long, io.pyroscope.labels.pb.JfrLabels.Context> getContexts() {
      return getContextsMap();
    }
    /**
     * <code>map&lt;int64, .io.pyroscope.labels.pb.Context&gt; contexts = 1;</code>
     */
    @java.lang.Override
    public java.util.Map<java.lang.Long, io.pyroscope.labels.pb.JfrLabels.Context> getContextsMap() {
      return internalGetContexts().getMap();
    }
    /**
     * <code>map&lt;int64, .io.pyroscope.labels.pb.Context&gt; contexts = 1;</code>
     */
    @java.lang.Override
    public /* nullable */
io.pyroscope.labels.pb.JfrLabels.Context getContextsOrDefault(
        long key,
        /* nullable */
io.pyroscope.labels.pb.JfrLabels.Context defaultValue) {

      java.util.Map<java.lang.Long, io.pyroscope.labels.pb.JfrLabels.Context> map =
          internalGetContexts().getMap();
      return map.containsKey(key) ? map.get(key) : defaultValue;
    }
    /**
     * <code>map&lt;int64, .io.pyroscope.labels.pb.Context&gt; contexts = 1;</code>
     */
    @java.lang.Override
    public io.pyroscope.labels.pb.JfrLabels.Context getContextsOrThrow(
        long key) {

      java.util.Map<java.lang.Long, io.pyroscope.labels.pb.JfrLabels.Context> map =
          internalGetContexts().getMap();
      if (!map.containsKey(key)) {
        throw new java.lang.IllegalArgumentException();
      }
      return map.get(key);
    }

    public static final int STRINGS_FIELD_NUMBER = 2;
    private static final class StringsDefaultEntryHolder {
      static final com.google.protobuf.MapEntry<
          java.lang.Long, java.lang.String> defaultEntry =
              com.google.protobuf.MapEntry
              .<java.lang.Long, java.lang.String>newDefaultInstance(
                  io.pyroscope.labels.pb.JfrLabels.internal_static_io_pyroscope_labels_pb_LabelsSnapshot_StringsEntry_descriptor, 
                  com.google.protobuf.WireFormat.FieldType.INT64,
                  0L,
                  com.google.protobuf.WireFormat.FieldType.STRING,
                  "");
    }
    @SuppressWarnings("serial")
    private com.google.protobuf.MapField<
        java.lang.Long, java.lang.String> strings_;
    private com.google.protobuf.MapField<java.lang.Long, java.lang.String>
    internalGetStrings() {
      if (strings_ == null) {
        return com.google.protobuf.MapField.emptyMapField(
            StringsDefaultEntryHolder.defaultEntry);
      }
      return strings_;
    }
    public int getStringsCount() {
      return internalGetStrings().getMap().size();
    }
    /**
     * <code>map&lt;int64, string&gt; strings = 2;</code>
     */
    @java.lang.Override
    public boolean containsStrings(
        long key) {

      return internalGetStrings().getMap().containsKey(key);
    }
    /**
     * Use {@link #getStringsMap()} instead.
     */
    @java.lang.Override
    @java.lang.Deprecated
    public java.util.Map<java.lang.Long, java.lang.String> getStrings() {
      return getStringsMap();
    }
    /**
     * <code>map&lt;int64, string&gt; strings = 2;</code>
     */
    @java.lang.Override
    public java.util.Map<java.lang.Long, java.lang.String> getStringsMap() {
      return internalGetStrings().getMap();
    }
    /**
     * <code>map&lt;int64, string&gt; strings = 2;</code>
     */
    @java.lang.Override
    public /* nullable */
java.lang.String getStringsOrDefault(
        long key,
        /* nullable */
java.lang.String defaultValue) {

      java.util.Map<java.lang.Long, java.lang.String> map =
          internalGetStrings().getMap();
      return map.containsKey(key) ? map.get(key) : defaultValue;
    }
    /**
     * <code>map&lt;int64, string&gt; strings = 2;</code>
     */
    @java.lang.Override
    public java.lang.String getStringsOrThrow(
        long key) {

      java.util.Map<java.lang.Long, java.lang.String> map =
          internalGetStrings().getMap();
      if (!map.containsKey(key)) {
        throw new java.lang.IllegalArgumentException();
      }
      return map.get(key);
    }

    private byte memoizedIsInitialized = -1;
    @java.lang.Override
    public final boolean isInitialized() {
      byte isInitialized = memoizedIsInitialized;
      if (isInitialized == 1) return true;
      if (isInitialized == 0) return false;

      memoizedIsInitialized = 1;
      return true;
    }

    @java.lang.Override
    public void writeTo(com.google.protobuf.CodedOutputStream output)
                        throws java.io.IOException {
      com.google.protobuf.GeneratedMessage
        .serializeLongMapTo(
          output,
          internalGetContexts(),
          ContextsDefaultEntryHolder.defaultEntry,
          1);
      com.google.protobuf.GeneratedMessage
        .serializeLongMapTo(
          output,
          internalGetStrings(),
          StringsDefaultEntryHolder.defaultEntry,
          2);
      getUnknownFields().writeTo(output);
    }

    @java.lang.Override
    public int getSerializedSize() {
      int size = memoizedSize;
      if (size != -1) return size;

      size = 0;
      for (java.util.Map.Entry<java.lang.Long, io.pyroscope.labels.pb.JfrLabels.Context> entry
           : internalGetContexts().getMap().entrySet()) {
        com.google.protobuf.MapEntry<java.lang.Long, io.pyroscope.labels.pb.JfrLabels.Context>
        contexts__ = ContextsDefaultEntryHolder.defaultEntry.newBuilderForType()
            .setKey(entry.getKey())
            .setValue(entry.getValue())
            .build();
        size += com.google.protobuf.CodedOutputStream
            .computeMessageSize(1, contexts__);
      }
      for (java.util.Map.Entry<java.lang.Long, java.lang.String> entry
           : internalGetStrings().getMap().entrySet()) {
        com.google.protobuf.MapEntry<java.lang.Long, java.lang.String>
        strings__ = StringsDefaultEntryHolder.defaultEntry.newBuilderForType()
            .setKey(entry.getKey())
            .setValue(entry.getValue())
            .build();
        size += com.google.protobuf.CodedOutputStream
            .computeMessageSize(2, strings__);
      }
      size += getUnknownFields().getSerializedSize();
      memoizedSize = size;
      return size;
    }

    @java.lang.Override
    public boolean equals(final java.lang.Object obj) {
      if (obj == this) {
       return true;
      }
      if (!(obj instanceof io.pyroscope.labels.pb.JfrLabels.LabelsSnapshot)) {
        return super.equals(obj);
      }
      io.pyroscope.labels.pb.JfrLabels.LabelsSnapshot other = (io.pyroscope.labels.pb.JfrLabels.LabelsSnapshot) obj;

      if (!internalGetContexts().equals(
          other.internalGetContexts())) return false;
      if (!internalGetStrings().equals(
          other.internalGetStrings())) return false;
      if (!getUnknownFields().equals(other.getUnknownFields())) return false;
      return true;
    }

    @java.lang.Override
    public int hashCode() {
      if (memoizedHashCode != 0) {
        return memoizedHashCode;
      }
      int hash = 41;
      hash = (19 * hash) + getDescriptor().hashCode();
      if (!internalGetContexts().getMap().isEmpty()) {
        hash = (37 * hash) + CONTEXTS_FIELD_NUMBER;
        hash = (53 * hash) + internalGetContexts().hashCode();
      }
      if (!internalGetStrings().getMap().isEmpty()) {
        hash = (37 * hash) + STRINGS_FIELD_NUMBER;
        hash = (53 * hash) + internalGetStrings().hashCode();
      }
      hash = (29 * hash) + getUnknownFields().hashCode();
      memoizedHashCode = hash;
      return hash;
    }

    public static io.pyroscope.labels.pb.JfrLabels.LabelsSnapshot parseFrom(
        java.nio.ByteBuffer data)
        throws com.google.protobuf.InvalidProtocolBufferException {
      return PARSER.parseFrom(data);
    }
    public static io.pyroscope.labels.pb.JfrLabels.LabelsSnapshot parseFrom(
        java.nio.ByteBuffer data,
        com.google.protobuf.ExtensionRegistryLite extensionRegistry)
        throws com.google.protobuf.InvalidProtocolBufferException {
      return PARSER.parseFrom(data, extensionRegistry);
    }
    public static io.pyroscope.labels.pb.JfrLabels.LabelsSnapshot parseFrom(
        com.google.protobuf.ByteString data)
        throws com.google.protobuf.InvalidProtocolBufferException {
      return PARSER.parseFrom(data);
    }
    public static io.pyroscope.labels.pb.JfrLabels.LabelsSnapshot parseFrom(
        com.google.protobuf.ByteString data,
        com.google.protobuf.ExtensionRegistryLite extensionRegistry)
        throws com.google.protobuf.InvalidProtocolBufferException {
      return PARSER.parseFrom(data, extensionRegistry);
    }
    public static io.pyroscope.labels.pb.JfrLabels.LabelsSnapshot parseFrom(byte[] data)
        throws com.google.protobuf.InvalidProtocolBufferException {
      return PARSER.parseFrom(data);
    }
    public static io.pyroscope.labels.pb.JfrLabels.LabelsSnapshot parseFrom(
        byte[] data,
        com.google.protobuf.ExtensionRegistryLite extensionRegistry)
        throws com.google.protobuf.InvalidProtocolBufferException {
      return PARSER.parseFrom(data, extensionRegistry);
    }
    public static io.pyroscope.labels.pb.JfrLabels.LabelsSnapshot parseFrom(java.io.InputStream input)
        throws java.io.IOException {
      return com.google.protobuf.GeneratedMessage
          .parseWithIOException(PARSER, input);
    }
    public static io.pyroscope.labels.pb.JfrLabels.LabelsSnapshot parseFrom(
        java.io.InputStream input,
        com.google.protobuf.ExtensionRegistryLite extensionRegistry)
        throws java.io.IOException {
      return com.google.protobuf.GeneratedMessage
          .parseWithIOException(PARSER, input, extensionRegistry);
    }

    public static io.pyroscope.labels.pb.JfrLabels.LabelsSnapshot parseDelimitedFrom(java.io.InputStream input)
        throws java.io.IOException {
      return com.google.protobuf.GeneratedMessage
          .parseDelimitedWithIOException(PARSER, input);
    }

    public static io.pyroscope.labels.pb.JfrLabels.LabelsSnapshot parseDelimitedFrom(
        java.io.InputStream input,
        com.google.protobuf.ExtensionRegistryLite extensionRegistry)
        throws java.io.IOException {
      return com.google.protobuf.GeneratedMessage
          .parseDelimitedWithIOException(PARSER, input, extensionRegistry);
    }
    public static io.pyroscope.labels.pb.JfrLabels.LabelsSnapshot parseFrom(
        com.google.protobuf.CodedInputStream input)
        throws java.io.IOException {
      return com.google.protobuf.GeneratedMessage
          .parseWithIOException(PARSER, input);
    }
    public static io.pyroscope.labels.pb.JfrLabels.LabelsSnapshot parseFrom(
        com.google.protobuf.CodedInputStream input,
        com.google.protobuf.ExtensionRegistryLite extensionRegistry)
        throws java.io.IOException {
      return com.google.protobuf.GeneratedMessage
          .parseWithIOException(PARSER, input, extensionRegistry);
    }

    @java.lang.Override
    public Builder newBuilderForType() { return newBuilder(); }
    public static Builder newBuilder() {
      return DEFAULT_INSTANCE.toBuilder();
    }
    public static Builder newBuilder(io.pyroscope.labels.pb.JfrLabels.LabelsSnapshot prototype) {
      return DEFAULT_INSTANCE.toBuilder().mergeFrom(prototype);
    }
    @java.lang.Override
    public Builder toBuilder() {
      return this == DEFAULT_INSTANCE
          ? new Builder() : new Builder().mergeFrom(this);
    }

    @java.lang.Override
    protected Builder newBuilderForType(
        com.google.protobuf.GeneratedMessage.BuilderParent parent) {
      Builder builder = new Builder(parent);
      return builder;
    }
    /**
     * Protobuf type {@code io.pyroscope.labels.pb.LabelsSnapshot}
     */
    public static final class Builder extends
        com.google.protobuf.GeneratedMessage.Builder<Builder> implements
        // @@protoc_insertion_point(builder_implements:io.pyroscope.labels.pb.LabelsSnapshot)
        io.pyroscope.labels.pb.JfrLabels.LabelsSnapshotOrBuilder {
      public static final com.google.protobuf.Descriptors.Descriptor
          getDescriptor() {
        return io.pyroscope.labels.pb.JfrLabels.internal_static_io_pyroscope_labels_pb_LabelsSnapshot_descriptor;
      }

      @SuppressWarnings({"rawtypes"})
      protected com.google.protobuf.MapFieldReflectionAccessor internalGetMapFieldReflection(
          int number) {
        switch (number) {
          case 1:
            return internalGetContexts();
          case 2:
            return internalGetStrings();
          default:
            throw new RuntimeException(
                "Invalid map field number: " + number);
        }
      }
      @SuppressWarnings({"rawtypes"})
      protected com.google.protobuf.MapFieldReflectionAccessor internalGetMutableMapFieldReflection(
          int number) {
        switch (number) {
          case 1:
            return internalGetMutableContexts();
          case 2:
            return internalGetMutableStrings();
          default:
            throw new RuntimeException(
                "Invalid map field number: " + number);
        }
      }
      @java.lang.Override
      protected com.google.protobuf.GeneratedMessage.FieldAccessorTable
          internalGetFieldAccessorTable() {
        return io.pyroscope.labels.pb.JfrLabels.internal_static_io_pyroscope_labels_pb_LabelsSnapshot_fieldAccessorTable
            .ensureFieldAccessorsInitialized(
                io.pyroscope.labels.pb.JfrLabels.LabelsSnapshot.class, io.pyroscope.labels.pb.JfrLabels.LabelsSnapshot.Builder.class);
      }

      // Construct using io.pyroscope.labels.pb.JfrLabels.LabelsSnapshot.newBuilder()
      private Builder() {

      }

      private Builder(
          com.google.protobuf.GeneratedMessage.BuilderParent parent) {
        super(parent);

      }
      @java.lang.Override
      public Builder clear() {
        super.clear();
        bitField0_ = 0;
        internalGetMutableContexts().clear();
        internalGetMutableStrings().clear();
        return this;
      }

      @java.lang.Override
      public com.google.protobuf.Descriptors.Descriptor
          getDescriptorForType() {
        return io.pyroscope.labels.pb.JfrLabels.internal_static_io_pyroscope_labels_pb_LabelsSnapshot_descriptor;
      }

      @java.lang.Override
      public io.pyroscope.labels.pb.JfrLabels.LabelsSnapshot getDefaultInstanceForType() {
        return io.pyroscope.labels.pb.JfrLabels.LabelsSnapshot.getDefaultInstance();
      }

      @java.lang.Override
      public io.pyroscope.labels.pb.JfrLabels.LabelsSnapshot build() {
        io.pyroscope.labels.pb.JfrLabels.LabelsSnapshot result = buildPartial();
        if (!result.isInitialized()) {
          throw newUninitializedMessageException(result);
        }
        return result;
      }

      @java.lang.Override
      public io.pyroscope.labels.pb.JfrLabels.LabelsSnapshot buildPartial() {
        io.pyroscope.labels.pb.JfrLabels.LabelsSnapshot result = new io.pyroscope.labels.pb.JfrLabels.LabelsSnapshot(this);
        if (bitField0_ != 0) { buildPartial0(result); }
        onBuilt();
        return result;
      }

      private void buildPartial0(io.pyroscope.labels.pb.JfrLabels.LabelsSnapshot result) {
        int from_bitField0_ = bitField0_;
        if (((from_bitField0_ & 0x00000001) != 0)) {
          result.contexts_ = internalGetContexts().build(ContextsDefaultEntryHolder.defaultEntry);
        }
        if (((from_bitField0_ & 0x00000002) != 0)) {
          result.strings_ = internalGetStrings();
          result.strings_.makeImmutable();
        }
      }

      @java.lang.Override
      public Builder mergeFrom(com.google.protobuf.Message other) {
        if (other instanceof io.pyroscope.labels.pb.JfrLabels.LabelsSnapshot) {
          return mergeFrom((io.pyroscope.labels.pb.JfrLabels.LabelsSnapshot)other);
        } else {
          super.mergeFrom(other);
          return this;
        }
      }

      public Builder mergeFrom(io.pyroscope.labels.pb.JfrLabels.LabelsSnapshot other) {
        if (other == io.pyroscope.labels.pb.JfrLabels.LabelsSnapshot.getDefaultInstance()) return this;
        internalGetMutableContexts().mergeFrom(
            other.internalGetContexts());
        bitField0_ |= 0x00000001;
        internalGetMutableStrings().mergeFrom(
            other.internalGetStrings());
        bitField0_ |= 0x00000002;
        this.mergeUnknownFields(other.getUnknownFields());
        onChanged();
        return this;
      }

      @java.lang.Override
      public final boolean isInitialized() {
        return true;
      }

      @java.lang.Override
      public Builder mergeFrom(
          com.google.protobuf.CodedInputStream input,
          com.google.protobuf.ExtensionRegistryLite extensionRegistry)
          throws java.io.IOException {
        if (extensionRegistry == null) {
          throw new java.lang.NullPointerException();
        }
        try {
          boolean done = false;
          while (!done) {
            int tag = input.readTag();
            switch (tag) {
              case 0:
                done = true;
                break;
              case 10: {
                com.google.protobuf.MapEntry<java.lang.Long, io.pyroscope.labels.pb.JfrLabels.Context>
                contexts__ = input.readMessage(
                    ContextsDefaultEntryHolder.defaultEntry.getParserForType(), extensionRegistry);
                internalGetMutableContexts().ensureBuilderMap().put(
                    contexts__.getKey(), contexts__.getValue());
                bitField0_ |= 0x00000001;
                break;
              } // case 10
              case 18: {
                com.google.protobuf.MapEntry<java.lang.Long, java.lang.String>
                strings__ = input.readMessage(
                    StringsDefaultEntryHolder.defaultEntry.getParserForType(), extensionRegistry);
                internalGetMutableStrings().getMutableMap().put(
                    strings__.getKey(), strings__.getValue());
                bitField0_ |= 0x00000002;
                break;
              } // case 18
              default: {
                if (!super.parseUnknownField(input, extensionRegistry, tag)) {
                  done = true; // was an endgroup tag
                }
                break;
              } // default:
            } // switch (tag)
          } // while (!done)
        } catch (com.google.protobuf.InvalidProtocolBufferException e) {
          throw e.unwrapIOException();
        } finally {
          onChanged();
        } // finally
        return this;
      }
      private int bitField0_;

      private static final class ContextsConverter implements com.google.protobuf.MapFieldBuilder.Converter<java.lang.Long, io.pyroscope.labels.pb.JfrLabels.ContextOrBuilder, io.pyroscope.labels.pb.JfrLabels.Context> {
        @java.lang.Override
        public io.pyroscope.labels.pb.JfrLabels.Context build(io.pyroscope.labels.pb.JfrLabels.ContextOrBuilder val) {
          if (val instanceof io.pyroscope.labels.pb.JfrLabels.Context) { return (io.pyroscope.labels.pb.JfrLabels.Context) val; }
          return ((io.pyroscope.labels.pb.JfrLabels.Context.Builder) val).build();
        }

        @java.lang.Override
        public com.google.protobuf.MapEntry<java.lang.Long, io.pyroscope.labels.pb.JfrLabels.Context> defaultEntry() {
          return ContextsDefaultEntryHolder.defaultEntry;
        }
      };
      private static final ContextsConverter contextsConverter = new ContextsConverter();

      private com.google.protobuf.MapFieldBuilder<
          java.lang.Long, io.pyroscope.labels.pb.JfrLabels.ContextOrBuilder, io.pyroscope.labels.pb.JfrLabels.Context, io.pyroscope.labels.pb.JfrLabels.Context.Builder> contexts_;
      private com.google.protobuf.MapFieldBuilder<java.lang.Long, io.pyroscope.labels.pb.JfrLabels.ContextOrBuilder, io.pyroscope.labels.pb.JfrLabels.Context, io.pyroscope.labels.pb.JfrLabels.Context.Builder>
          internalGetContexts() {
        if (contexts_ == null) {
          return new com.google.protobuf.MapFieldBuilder<>(contextsConverter);
        }
        return contexts_;
      }
      private com.google.protobuf.MapFieldBuilder<java.lang.Long, io.pyroscope.labels.pb.JfrLabels.ContextOrBuilder, io.pyroscope.labels.pb.JfrLabels.Context, io.pyroscope.labels.pb.JfrLabels.Context.Builder>
          internalGetMutableContexts() {
        if (contexts_ == null) {
          contexts_ = new com.google.protobuf.MapFieldBuilder<>(contextsConverter);
        }
        bitField0_ |= 0x00000001;
        onChanged();
        return contexts_;
      }
      public int getContextsCount() {
        return internalGetContexts().ensureBuilderMap().size();
      }
      /**
       * <code>map&lt;int64, .io.pyroscope.labels.pb.Context&gt; contexts = 1;</code>
       */
      @java.lang.Override
      public boolean containsContexts(
          long key) {

        return internalGetContexts().ensureBuilderMap().containsKey(key);
      }
      /**
       * Use {@link #getContextsMap()} instead.
       */
      @java.lang.Override
      @java.lang.Deprecated
      public java.util.Map<java.lang.Long, io.pyroscope.labels.pb.JfrLabels.Context> getContexts() {
        return getContextsMap();
      }
      /**
       * <code>map&lt;int64, .io.pyroscope.labels.pb.Context&gt; contexts = 1;</code>
       */
      @java.lang.Override
      public java.util.Map<java.lang.Long, io.pyroscope.labels.pb.JfrLabels.Context> getContextsMap() {
        return internalGetContexts().getImmutableMap();
      }
      /**
       * <code>map&lt;int64, .io.pyroscope.labels.pb.Context&gt; contexts = 1;</code>
       */
      @java.lang.Override
      public /* nullable */
io.pyroscope.labels.pb.JfrLabels.Context getContextsOrDefault(
          long key,
          /* nullable */
io.pyroscope.labels.pb.JfrLabels.Context defaultValue) {

        java.util.Map<java.lang.Long, io.pyroscope.labels.pb.JfrLabels.ContextOrBuilder> map = internalGetMutableContexts().ensureBuilderMap();
        return map.containsKey(key) ? contextsConverter.build(map.get(key)) : defaultValue;
      }
      /**
       * <code>map&lt;int64, .io.pyroscope.labels.pb.Context&gt; contexts = 1;</code>
       */
      @java.lang.Override
      public io.pyroscope.labels.pb.JfrLabels.Context getContextsOrThrow(
          long key) {

        java.util.Map<java.lang.Long, io.pyroscope.labels.pb.JfrLabels.ContextOrBuilder> map = internalGetMutableContexts().ensureBuilderMap();
        if (!map.containsKey(key)) {
          throw new java.lang.IllegalArgumentException();
        }
        return contextsConverter.build(map.get(key));
      }
      public Builder clearContexts() {
        bitField0_ = (bitField0_ & ~0x00000001);
        internalGetMutableContexts().clear();
        return this;
      }
      /**
       * <code>map&lt;int64, .io.pyroscope.labels.pb.Context&gt; contexts = 1;</code>
       */
      public Builder removeContexts(
          long key) {

        internalGetMutableContexts().ensureBuilderMap()
            .remove(key);
        return this;
      }
      /**
       * Use alternate mutation accessors instead.
       */
      @java.lang.Deprecated
      public java.util.Map<java.lang.Long, io.pyroscope.labels.pb.JfrLabels.Context>
          getMutableContexts() {
        bitField0_ |= 0x00000001;
        return internalGetMutableContexts().ensureMessageMap();
      }
      /**
       * <code>map&lt;int64, .io.pyroscope.labels.pb.Context&gt; contexts = 1;</code>
       */
      public Builder putContexts(
          long key,
          io.pyroscope.labels.pb.JfrLabels.Context value) {

        if (value == null) { throw new NullPointerException("map value"); }
        internalGetMutableContexts().ensureBuilderMap()
            .put(key, value);
        bitField0_ |= 0x00000001;
        return this;
      }
      /**
       * <code>map&lt;int64, .io.pyroscope.labels.pb.Context&gt; contexts = 1;</code>
       */
      public Builder putAllContexts(
          java.util.Map<java.lang.Long, io.pyroscope.labels.pb.JfrLabels.Context> values) {
        for (java.util.Map.Entry<java.lang.Long, io.pyroscope.labels.pb.JfrLabels.Context> e : values.entrySet()) {
          if (e.getKey() == null || e.getValue() == null) {
            throw new NullPointerException();
          }
        }
        internalGetMutableContexts().ensureBuilderMap()
            .putAll(values);
        bitField0_ |= 0x00000001;
        return this;
      }
      /**
       * <code>map&lt;int64, .io.pyroscope.labels.pb.Context&gt; contexts = 1;</code>
       */
      public io.pyroscope.labels.pb.JfrLabels.Context.Builder putContextsBuilderIfAbsent(
          long key) {
        java.util.Map<java.lang.Long, io.pyroscope.labels.pb.JfrLabels.ContextOrBuilder> builderMap = internalGetMutableContexts().ensureBuilderMap();
        io.pyroscope.labels.pb.JfrLabels.ContextOrBuilder entry = builderMap.get(key);
        if (entry == null) {
          entry = io.pyroscope.labels.pb.JfrLabels.Context.newBuilder();
          builderMap.put(key, entry);
        }
        if (entry instanceof io.pyroscope.labels.pb.JfrLabels.Context) {
          entry = ((io.pyroscope.labels.pb.JfrLabels.Context) entry).toBuilder();
          builderMap.put(key, entry);
        }
        return (io.pyroscope.labels.pb.JfrLabels.Context.Builder) entry;
      }

      private com.google.protobuf.MapField<
          java.lang.Long, java.lang.String> strings_;
      private com.google.protobuf.MapField<java.lang.Long, java.lang.String>
          internalGetStrings() {
        if (strings_ == null) {
          return com.google.protobuf.MapField.emptyMapField(
              StringsDefaultEntryHolder.defaultEntry);
        }
        return strings_;
      }
      private com.google.protobuf.MapField<java.lang.Long, java.lang.String>
          internalGetMutableStrings() {
        if (strings_ == null) {
          strings_ = com.google.protobuf.MapField.newMapField(
              StringsDefaultEntryHolder.defaultEntry);
        }
        if (!strings_.isMutable()) {
          strings_ = strings_.copy();
        }
        bitField0_ |= 0x00000002;
        onChanged();
        return strings_;
      }
      public int getStringsCount() {
        return internalGetStrings().getMap().size();
      }
      /**
       * <code>map&lt;int64, string&gt; strings = 2;</code>
       */
      @java.lang.Override
      public boolean containsStrings(
          long key) {

        return internalGetStrings().getMap().containsKey(key);
      }
      /**
       * Use {@link #getStringsMap()} instead.
       */
      @java.lang.Override
      @java.lang.Deprecated
      public java.util.Map<java.lang.Long, java.lang.String> getStrings() {
        return getStringsMap();
      }
      /**
       * <code>map&lt;int64, string&gt; strings = 2;</code>
       */
      @java.lang.Override
      public java.util.Map<java.lang.Long, java.lang.String> getStringsMap() {
        return internalGetStrings().getMap();
      }
      /**
       * <code>map&lt;int64, string&gt; strings = 2;</code>
       */
      @java.lang.Override
      public /* nullable */
java.lang.String getStringsOrDefault(
          long key,
          /* nullable */
java.lang.String defaultValue) {

        java.util.Map<java.lang.Long, java.lang.String> map =
            internalGetStrings().getMap();
        return map.containsKey(key) ? map.get(key) : defaultValue;
      }
      /**
       * <code>map&lt;int64, string&gt; strings = 2;</code>
       */
      @java.lang.Override
      public java.lang.String getStringsOrThrow(
          long key) {

        java.util.Map<java.lang.Long, java.lang.String> map =
            internalGetStrings().getMap();
        if (!map.containsKey(key)) {
          throw new java.lang.IllegalArgumentException();
        }
        return map.get(key);
      }
      public Builder clearStrings() {
        bitField0_ = (bitField0_ & ~0x00000002);
        internalGetMutableStrings().getMutableMap()
            .clear();
        return this;
      }
      /**
       * <code>map&lt;int64, string&gt; strings = 2;</code>
       */
      public Builder removeStrings(
          long key) {

        internalGetMutableStrings().getMutableMap()
            .remove(key);
        return this;
      }
      /**
       * Use alternate mutation accessors instead.
       */
      @java.lang.Deprecated
      public java.util.Map<java.lang.Long, java.lang.String>
          getMutableStrings() {
        bitField0_ |= 0x00000002;
        return internalGetMutableStrings().getMutableMap();
      }
      /**
       * <code>map&lt;int64, string&gt; strings = 2;</code>
       */
      public Builder putStrings(
          long key,
          java.lang.String value) {

        if (value == null) { throw new NullPointerException("map value"); }
        internalGetMutableStrings().getMutableMap()
            .put(key, value);
        bitField0_ |= 0x00000002;
        return this;
      }
      /**
       * <code>map&lt;int64, string&gt; strings = 2;</code>
       */
      public Builder putAllStrings(
          java.util.Map<java.lang.Long, java.lang.String> values) {
        internalGetMutableStrings().getMutableMap()
            .putAll(values);
        bitField0_ |= 0x00000002;
        return this;
      }

      // @@protoc_insertion_point(builder_scope:io.pyroscope.labels.pb.LabelsSnapshot)
    }

    // @@protoc_insertion_point(class_scope:io.pyroscope.labels.pb.LabelsSnapshot)
    private static final io.pyroscope.labels.pb.JfrLabels.LabelsSnapshot DEFAULT_INSTANCE;
    static {
      DEFAULT_INSTANCE = new io.pyroscope.labels.pb.JfrLabels.LabelsSnapshot();
    }

    public static io.pyroscope.labels.pb.JfrLabels.LabelsSnapshot getDefaultInstance() {
      return DEFAULT_INSTANCE;
    }

    private static final com.google.protobuf.Parser<LabelsSnapshot>
        PARSER = new com.google.protobuf.AbstractParser<LabelsSnapshot>() {
      @java.lang.Override
      public LabelsSnapshot parsePartialFrom(
          com.google.protobuf.CodedInputStream input,
          com.google.protobuf.ExtensionRegistryLite extensionRegistry)
          throws com.google.protobuf.InvalidProtocolBufferException {
        Builder builder = newBuilder();
        try {
          builder.mergeFrom(input, extensionRegistry);
        } catch (com.google.protobuf.InvalidProtocolBufferException e) {
          throw e.setUnfinishedMessage(builder.buildPartial());
        } catch (com.google.protobuf.UninitializedMessageException e) {
          throw e.asInvalidProtocolBufferException().setUnfinishedMessage(builder.buildPartial());
        } catch (java.io.IOException e) {
          throw new com.google.protobuf.InvalidProtocolBufferException(e)
              .setUnfinishedMessage(builder.buildPartial());
        }
        return builder.buildPartial();
      }
    };

    public static com.google.protobuf.Parser<LabelsSnapshot> parser() {
      return PARSER;
    }

    @java.lang.Override
    public com.google.protobuf.Parser<LabelsSnapshot> getParserForType() {
      return PARSER;
    }

    @java.lang.Override
    public io.pyroscope.labels.pb.JfrLabels.LabelsSnapshot getDefaultInstanceForType() {
      return DEFAULT_INSTANCE;
    }

  }

  private static final com.google.protobuf.Descriptors.Descriptor
    internal_static_io_pyroscope_labels_pb_Context_descriptor;
  private static final 
    com.google.protobuf.GeneratedMessage.FieldAccessorTable
      internal_static_io_pyroscope_labels_pb_Context_fieldAccessorTable;
  private static final com.google.protobuf.Descriptors.Descriptor
    internal_static_io_pyroscope_labels_pb_Context_LabelsEntry_descriptor;
  private static final 
    com.google.protobuf.GeneratedMessage.FieldAccessorTable
      internal_static_io_pyroscope_labels_pb_Context_LabelsEntry_fieldAccessorTable;
  private static final com.google.protobuf.Descriptors.Descriptor
    internal_static_io_pyroscope_labels_pb_LabelsSnapshot_descriptor;
  private static final 
    com.google.protobuf.GeneratedMessage.FieldAccessorTable
      internal_static_io_pyroscope_labels_pb_LabelsSnapshot_fieldAccessorTable;
  private static final com.google.protobuf.Descriptors.Descriptor
    internal_static_io_pyroscope_labels_pb_LabelsSnapshot_ContextsEntry_descriptor;
  private static final 
    com.google.protobuf.GeneratedMessage.FieldAccessorTable
      internal_static_io_pyroscope_labels_pb_LabelsSnapshot_ContextsEntry_fieldAccessorTable;
  private static final com.google.protobuf.Descriptors.Descriptor
    internal_static_io_pyroscope_labels_pb_LabelsSnapshot_StringsEntry_descriptor;
  private static final 
    com.google.protobuf.GeneratedMessage.FieldAccessorTable
      internal_static_io_pyroscope_labels_pb_LabelsSnapshot_StringsEntry_fieldAccessorTable;

  public static com.google.protobuf.Descriptors.FileDescriptor
      getDescriptor() {
    return descriptor;
  }
  private static  com.google.protobuf.Descriptors.FileDescriptor
      descriptor;
  static {
    java.lang.String[] descriptorData = {
      "\n\020jfr_labels.proto\022\026io.pyroscope.labels." +
      "pb\"u\n\007Context\022;\n\006labels\030\001 \003(\0132+.io.pyros" +
      "cope.labels.pb.Context.LabelsEntry\032-\n\013La" +
      "belsEntry\022\013\n\003key\030\001 \001(\003\022\r\n\005value\030\002 \001(\003:\0028" +
      "\001\"\240\002\n\016LabelsSnapshot\022F\n\010contexts\030\001 \003(\01324" +
      ".io.pyroscope.labels.pb.LabelsSnapshot.C" +
      "ontextsEntry\022D\n\007strings\030\002 \003(\01323.io.pyros" +
      "cope.labels.pb.LabelsSnapshot.StringsEnt" +
      "ry\032P\n\rContextsEntry\022\013\n\003key\030\001 \001(\003\022.\n\005valu" +
      "e\030\002 \001(\0132\037.io.pyroscope.labels.pb.Context" +
      ":\0028\001\032.\n\014StringsEntry\022\013\n\003key\030\001 \001(\003\022\r\n\005val" +
      "ue\030\002 \001(\t:\0028\001b\006proto3"
    };
    descriptor = com.google.protobuf.Descriptors.FileDescriptor
      .internalBuildGeneratedFileFrom(descriptorData,
        new com.google.protobuf.Descriptors.FileDescriptor[] {
        });
    internal_static_io_pyroscope_labels_pb_Context_descriptor =
      getDescriptor().getMessageTypes().get(0);
    internal_static_io_pyroscope_labels_pb_Context_fieldAccessorTable = new
      com.google.protobuf.GeneratedMessage.FieldAccessorTable(
        internal_static_io_pyroscope_labels_pb_Context_descriptor,
        new java.lang.String[] { "Labels", });
    internal_static_io_pyroscope_labels_pb_Context_LabelsEntry_descriptor =
      internal_static_io_pyroscope_labels_pb_Context_descriptor.getNestedTypes().get(0);
    internal_static_io_pyroscope_labels_pb_Context_LabelsEntry_fieldAccessorTable = new
      com.google.protobuf.GeneratedMessage.FieldAccessorTable(
        internal_static_io_pyroscope_labels_pb_Context_LabelsEntry_descriptor,
        new java.lang.String[] { "Key", "Value", });
    internal_static_io_pyroscope_labels_pb_LabelsSnapshot_descriptor =
      getDescriptor().getMessageTypes().get(1);
    internal_static_io_pyroscope_labels_pb_LabelsSnapshot_fieldAccessorTable = new
      com.google.protobuf.GeneratedMessage.FieldAccessorTable(
        internal_static_io_pyroscope_labels_pb_LabelsSnapshot_descriptor,
        new java.lang.String[] { "Contexts", "Strings", });
    internal_static_io_pyroscope_labels_pb_LabelsSnapshot_ContextsEntry_descriptor =
      internal_static_io_pyroscope_labels_pb_LabelsSnapshot_descriptor.getNestedTypes().get(0);
    internal_static_io_pyroscope_labels_pb_LabelsSnapshot_ContextsEntry_fieldAccessorTable = new
      com.google.protobuf.GeneratedMessage.FieldAccessorTable(
        internal_static_io_pyroscope_labels_pb_LabelsSnapshot_ContextsEntry_descriptor,
        new java.lang.String[] { "Key", "Value", });
    internal_static_io_pyroscope_labels_pb_LabelsSnapshot_StringsEntry_descriptor =
      internal_static_io_pyroscope_labels_pb_LabelsSnapshot_descriptor.getNestedTypes().get(1);
    internal_static_io_pyroscope_labels_pb_LabelsSnapshot_StringsEntry_fieldAccessorTable = new
      com.google.protobuf.GeneratedMessage.FieldAccessorTable(
        internal_static_io_pyroscope_labels_pb_LabelsSnapshot_StringsEntry_descriptor,
        new java.lang.String[] { "Key", "Value", });
    descriptor.resolveAllFeaturesImmutable();
  }

  // @@protoc_insertion_point(outer_class_scope)
}
```

## File: `agent/src/main/java/io/pyroscope/labels/v2/ConstantContext.java`
```java
package io.pyroscope.labels.v2;

import org.jetbrains.annotations.NotNull;

import static io.pyroscope.Preconditions.checkNotNull;

/**
 * ConstantContext provides a way to define a set of labels that will be permanently stored
 * in memory for the life of the process.
 *
 * <p><strong>IMPORTANT:</strong> This class keeps references to {@link LabelsSet} instances
 * indefinitely (they are never garbage collected). Only use ConstantContext for labels that:
 * <ul>
 *   <li>Have a finite, predetermined set of possible values (low cardinality)</li>
 *   <li>Are constant throughout the application lifetime</li>
 *   <li>Do NOT contain user-controlled values such as user IDs, session IDs, or span IDs</li>
 *   <li>Are reused frequently across different parts of your application</li>
 * </ul>
 *
 * <p>For high-cardinality or ephemeral labels, use {@link ScopedContext} instead, which properly
 * cleans up references after context is closed and labels are dumped.
 *
 * <p>All parameters must be non-null. Attempting to create a ConstantContext with null parameters
 * will result in a NullPointerException.
 *
 * <p>Example usage:
 * <pre>{@code
 * private static final ConstantContext ctx = ConstantContext.of(new LabelsSet(
 *     "path", "/foo/bar",
 *     "method", "GET",
 *     "service", "svc-1"
 * ));
 *
 * // Later in your code:
 * try {
 *     ctx.activate();
 *     // Do work with this context active
 * } finally {
 *     ctx.deactivate();
 * }
 * }</pre>
 */
public class ConstantContext {

    /**
     * Creates a new ConstantContext with the given labels.
     *
     * <p>Warning: The provided LabelsSet will be stored permanently in memory.
     * Only use this for low-cardinality, constant label sets.
     *
     * @param labels The labels to associate with this context
     * @return A new ConstantContext instance
     * @throws NullPointerException if labels is null
     */
    public static @NotNull ConstantContext of(@NotNull LabelsSet labels) {
        checkNotNull(labels, "Labels");
        long contextId = ScopedContext.CONTEXT_COUNTER.incrementAndGet();
        ScopedContext.CONSTANT_CONTEXTS.put(contextId, labels);
        return new ConstantContext(contextId);
    }

    private final long contextId;

    private ConstantContext(long contextId) {
        this.contextId = contextId;
    }

    /**
     * Activates this context for the current thread.
     * This sets the async-profiler's context ID to this context's ID,
     * which will associate profiled samples with these labels.
     */
    public void activate() {
        ScopedContext.getAsyncProfiler().setContextId(contextId);
    }

    /**
     * Deactivates this context for the current thread.
     * This resets the async-profiler's context ID to 0 (no context).
     */
    public void deactivate() {
        ScopedContext.getAsyncProfiler().setContextId(0);
    }
}
```

## File: `agent/src/main/java/io/pyroscope/labels/v2/LabelsSet.java`
```java
package io.pyroscope.labels.v2;

import java.util.Map;
import java.util.function.BiConsumer;

import org.jetbrains.annotations.NotNull;

import static io.pyroscope.Preconditions.checkNotNull;

/**
 * LabelsSet represents an immutable set of key-value pairs used for profiling labels.
 *
 * <p>Labels are used by Pyroscope to categorize and filter profiling data, allowing
 * for more detailed analysis of application performance across different contexts.
 *
 * <p>This class stores labels as a flattened array of alternating keys and values,
 * making it memory-efficient while still providing easy iteration over the contained
 * label pairs.
 *
 * <p>LabelsSet instances are immutable once created and should be passed to
 * {@link ScopedContext} or {@link ConstantContext} to associate profiling data
 * with these labels.
 *
 * <p>All label keys and values must be non-null. Attempting to create a LabelsSet
 * with null keys or values will result in a NullPointerException.
 *
 * <p>Example usage:
 * <pre>{@code
 * // Creating a label set with explicit key-value pairs
 * LabelsSet labels = new LabelsSet(
 *     "service", "user-api",
 *     "method", "GET",
 *     "endpoint", "/users"
 * );
 *
 * // Creating a label set from a Map
 * Map<String, String> labelMap = new HashMap<>();
 * labelMap.put("transaction", "payment");
 * labelMap.put("customer_type", "premium");
 * LabelsSet labels = new LabelsSet(labelMap);
 * }</pre>
 */
public final class LabelsSet {
    private final String[] args;

    /**
     * Creates a LabelsSet from alternating key-value pairs.
     *
     * <p>The arguments must be provided as alternating key-value pairs,
     * where even-indexed arguments (0, 2, 4, ...) are keys and
     * odd-indexed arguments (1, 3, 5, ...) are their corresponding values.
     *
     * @param args An array of alternating key-value strings
     * @throws IllegalArgumentException if the number of arguments is not even
     * @throws NullPointerException     if any key or value is null
     */
    public LabelsSet(@NotNull String... args) {
        if (args.length % 2 != 0) {
            throw new IllegalArgumentException("args.length % 2 != 0: " +
                    "api.LabelsSet's  constructor arguments should be key-value pairs");
        }

        for (int i = 0; i < args.length; i++) {
            checkNotNull(args[i], "Label");
        }

        this.args = new String[args.length];
        System.arraycopy(args, 0, this.args, 0, args.length);
    }

    /**
     * Creates a LabelsSet from a Map of labels.
     *
     * <p>This constructor converts a Map representation of labels into the
     * internal array representation used by LabelsSet.
     *
     * @param args A map containing key-value pairs for labels
     * @throws NullPointerException if args is null or any key or value in the map is null
     */
    public LabelsSet(@NotNull Map<@NotNull String, @NotNull String> args) {
        checkNotNull(args, "Labels");
        this.args = new String[args.size() * 2];
        int i = 0;
        for (Map.Entry<String, String> it : args.entrySet()) {
            this.args[i] = checkNotNull(it.getKey(), "Key");
            this.args[i + 1] = checkNotNull(it.getValue(), "Value");
            i += 2;
        }
    }

    /**
     * Applies a BiConsumer function to each key-value pair in this label set.
     *
     * <p>This method provides a way to iterate through all labels without
     * exposing the internal representation.
     *
     * @param labelConsumer A function that accepts a key (String) and value (String)
     * @throws NullPointerException if labelConsumer is null
     */
    public void forEachLabel(@NotNull BiConsumer<@NotNull String, @NotNull String> labelConsumer) {
        checkNotNull(labelConsumer, "Consumer");
        for (int i = 0; i < args.length; i += 2) {
            labelConsumer.accept(args[i], args[i + 1]);
        }
    }
}
```

## File: `agent/src/main/java/io/pyroscope/labels/v2/Pyroscope.java`
```java
package io.pyroscope.labels.v2;


import io.pyroscope.labels.pb.*;
import org.jetbrains.annotations.NotNull;

import java.util.*;
import java.util.concurrent.Callable;
import java.util.concurrent.ConcurrentHashMap;
import java.util.function.BiConsumer;

import static io.pyroscope.Preconditions.checkNotNull;

public final class Pyroscope {
    /**
     * LabelsWrapper accumulates dynamic labels and corelates them with async-profiler's contextId
     * You are expected to call {@link LabelsWrapper#dump()} periodically, io.pyroscope.javaagent.Profiler
     * does that. If you don't use io.pyroscope.javaagent.Profiler,
     * you need to call {@link LabelsWrapper#dump()} yourself.
     */
    public static class LabelsWrapper {

        public static <T> T run(@NotNull LabelsSet labels, @NotNull Callable<T> c) throws Exception {
            try (ScopedContext s = new ScopedContext(checkNotNull(labels, "Labels"))) {
                return checkNotNull(c, "Callable").call();
            }
        }

        public static void run(@NotNull LabelsSet labels, @NotNull Runnable c) {
            try (ScopedContext s = new ScopedContext(checkNotNull(labels, "Labels"))) {
                checkNotNull(c, "Runnable").run();
            }
        }

        /**
         * Emergency method to clear all ScopedContext references when memory leaks are detected.
         *
         * <p><strong>WARNING:</strong> This method should NOT be used in normal operation. It is
         * provided as a last resort for situations where unclosed {@link ScopedContext} instances
         * are causing memory leaks and cannot be fixed by proper closing in the application code.
         *
         * <p>Calling this method will:
         * <ul>
         *   <li>Remove all references to active and unclosed ScopedContext instances</li>
         *   <li>Result in missing labels/labelsets in profiling data</li>
         *   <li>Potentially create inconsistent profiling results</li>
         * </ul>
         *
         * <p>Recommended usage pattern:
         * <ul>
         *   <li>Fix your code to properly close all ScopedContext instances (preferred solution)</li>
         *   <li>If that's not possible in the short term, call this method periodically (e.g., once every N minutes)
         *       as a temporary workaround</li>
         * </ul>
         *
         * <p>Note: This does not affect {@link ConstantContext} instances, which are designed to live
         * for the entire application lifetime.
         */
        public static void clear() {
            ScopedContext.CONTEXTS.clear();
        }

        public static JfrLabels.LabelsSnapshot dump() {
            final JfrLabels.LabelsSnapshot.Builder sb = JfrLabels.LabelsSnapshot.newBuilder();
            final StringTableBuilder stb = new StringTableBuilder();
            stb.indexes.putAll(CONSTANTS);
            final Set<Long> closedContexts = new HashSet<>();
            final BiConsumer<Long, LabelsSet> collect = (contextID, ls) -> {
                final JfrLabels.Context.Builder cb = JfrLabels.Context.newBuilder();
                ls.forEachLabel((k, v) -> {
                    cb.putLabels(stb.get(k), stb.get(v));
                });
                sb.putContexts(contextID, cb.build());
            };
            for (Map.Entry<Long, ScopedContext> it : ScopedContext.CONTEXTS.entrySet()) {
                final Long contextID = it.getKey();
                if (it.getValue().closed.get()) {
                    closedContexts.add(contextID);
                }
                collect.accept(contextID, it.getValue().labels);
            }
            for (Map.Entry<Long, LabelsSet> it : ScopedContext.CONSTANT_CONTEXTS.entrySet()) {
                final Long contextID = it.getKey();
                collect.accept(contextID, it.getValue());
            }
            stb.indexes.forEach((k, v) -> {
                sb.putStrings(v, k);
            });
            for (Long cid : closedContexts) {
                ScopedContext.CONTEXTS.remove(cid);
            }
            return sb.build();
        }

        static final ConcurrentHashMap<String, Long> CONSTANTS = new ConcurrentHashMap<>();

        public static long registerConstant(@NotNull String constant) {
            checkNotNull(constant, "constant");
            Long v = CONSTANTS.get(constant);
            if (v != null) {
                return v;
            }
            synchronized (CONSTANTS) {
                v = CONSTANTS.get(constant);
                if (v != null) {
                    return v;
                }
                long id = CONSTANTS.size() + 1;
                CONSTANTS.put(constant, id);
                return id;
            }
        }
    }

    private static Map<String, String> staticLabels = Collections.emptyMap();

    /**
     * Sets the static labels to be included with all profiling data.
     *
     * <p>Static labels are constant across the entire application lifetime and are used
     * to identify and categorize profiling data at a global level.
     *
     * <p>All label keys and values must be non-null. Attempting to set static labels
     * with null keys or values will result in a NullPointerException.
     *
     * @param labels A map containing key-value pairs for static labels
     * @throws NullPointerException if labels is null or any key or value in the map is null
     */
    public static void setStaticLabels(@NotNull Map<@NotNull String, @NotNull String> labels) {
        checkNotNull(labels, "Labels");

        for (Map.Entry<String, String> entry : labels.entrySet()) {
            checkNotNull(entry.getKey(), "Key");
            checkNotNull(entry.getValue(), "Value");
        }

        staticLabels = Collections.unmodifiableMap(new HashMap<>(labels));
    }

    public static Map<String, String> getStaticLabels() {
        return staticLabels;
    }

    static class StringTableBuilder {
        private final Map<String, Long> indexes = new HashMap<>();

        public StringTableBuilder() {
        }

        public long get(@NotNull String s) {
            Long prev = indexes.get(s);
            if (prev != null) {
                return prev;
            }
            long index = indexes.size() + 1;
            indexes.put(s, index);
            return index;

        }
    }
}
```

## File: `agent/src/main/java/io/pyroscope/labels/v2/ScopedContext.java`
```java
package io.pyroscope.labels.v2;

import io.pyroscope.PyroscopeAsyncProfiler;
import one.profiler.AsyncProfiler;
import org.jetbrains.annotations.NotNull;

import java.util.concurrent.ConcurrentHashMap;
import java.util.concurrent.atomic.AtomicBoolean;
import java.util.concurrent.atomic.AtomicLong;
import java.util.function.BiConsumer;

import static io.pyroscope.Preconditions.checkNotNull;

/**
 * ScopedContext associates profiling data with a set of labels for the current execution scope.
 * Unlike {@link ConstantContext}, a ScopedContext is designed for dynamic, temporary use and
 * will be properly garbage collected.
 *
 * <p>ScopedContext implements {@link AutoCloseable}, allowing it to be used in try-with-resources
 * blocks for automatic cleanup when the context goes out of scope.
 *
 * <p>When a ScopedContext is closed, it's marked as such but remains in memory until the next call
 * to {@link io.pyroscope.labels.v2.Pyroscope.LabelsWrapper#dump()}. After being included in a dump,
 * closed contexts are removed from the internal map, allowing them to be garbage collected.
 *
 * <p>All constructor parameters (labels, previous context) must be non-null. Attempting to create
 * a ScopedContext with null parameters will result in a NullPointerException.
 *
 * <p>Use ScopedContext for:
 * <ul>
 *   <li>High-cardinality labels (like request IDs, user IDs, etc.)</li>
 *   <li>Temporary, request-scoped labels that change frequently</li>
 *   <li>User-controlled or dynamically generated values</li>
 *   <li>Any labels that would result in memory leaks if kept indefinitely</li>
 * </ul>
 *
 * <p>Example usage:
 * <pre>{@code
 * // For a single block of code with labels
 * try (ScopedContext ctx = new ScopedContext(new LabelsSet("request_id", requestId))) {
 *     // Do work that will be profiled with this context
 *     processRequest();
 * } // Context automatically closed here
 *
 * // Or using the helper method in Pyroscope.LabelsWrapper:
 * Pyroscope.LabelsWrapper.run(new LabelsSet("span_id", spanId), () -> {
 *     // Operations to perform with this context
 *     executeSpan();
 * });
 * }</pre>
 */
public final class ScopedContext implements AutoCloseable {
    public static final AtomicBoolean ENABLED = new AtomicBoolean(false);
    static final AtomicLong CONTEXT_COUNTER = new AtomicLong(0);
    static final ConcurrentHashMap<Long, ScopedContext> CONTEXTS = new ConcurrentHashMap<>();
    static final ConcurrentHashMap<Long, LabelsSet> CONSTANT_CONTEXTS = new ConcurrentHashMap<>();

    private static volatile AsyncProfiler asyncProfiler;

    static AsyncProfiler getAsyncProfiler() {
        if (asyncProfiler != null) {
            return asyncProfiler;
        }
        asyncProfiler = PyroscopeAsyncProfiler.getAsyncProfiler();
        return asyncProfiler;
    }

    final LabelsSet labels;
    final long contextId;
    final long prevContextId;
    final AtomicBoolean closed = new AtomicBoolean(false);

    /**
     * Creates a new ScopedContext with the given labels.
     * The previous context ID is set to 0 (root context).
     *
     * @param labels The labels to associate with this context
     * @throws NullPointerException if labels is null
     */
    public ScopedContext(@NotNull LabelsSet labels) {
        this(
                checkNotNull(labels, "Labels"),
                0
        );
    }

    /**
     * Creates a new ScopedContext with the given labels, using the previous context's ID.
     * This allows for proper nesting of contexts.
     *
     * @param labels The labels to associate with this context
     * @param prev   The previous context that this context will replace temporarily
     * @throws NullPointerException if labels or prev is null
     */
    public ScopedContext(@NotNull LabelsSet labels, @NotNull ScopedContext prev) {
        this(
                checkNotNull(labels, "Labels"),
                checkNotNull(prev, "Context").contextId
        );
    }

    /**
     * Internal constructor to create a ScopedContext with specific previous context ID.
     *
     * @param labels        The labels to associate with this context
     * @param prevContextId The context ID to restore when this context is closed
     * @throws NullPointerException if labels is null
     */
    ScopedContext(@NotNull LabelsSet labels, long prevContextId) {
        this.labels = checkNotNull(labels, "Labels");
        if (ENABLED.get()) {
            this.contextId = CONTEXT_COUNTER.incrementAndGet();
            this.prevContextId = prevContextId;
            CONTEXTS.put(contextId, this);
            getAsyncProfiler().setContextId(contextId);
        } else {
            this.contextId = 0;
            this.prevContextId = 0;
        }
    }

    /**
     * Closes this context, restoring the previous context.
     *
     * <p>The context is marked as closed, but will remain in memory until the next call to
     * {@link io.pyroscope.labels.v2.Pyroscope.LabelsWrapper#dump()} which will clean up
     * closed contexts.
     */
    @Override
    public void close() {
        if (!closed.compareAndSet(false, true)) {
            return;
        }
        if (ENABLED.get()) {
            getAsyncProfiler().setContextId(this.prevContextId);
        }
    }

    /**
     * Applies a consumer function to each label in this context.
     *
     * @param labelConsumer A function that will be called with each key-value pair in the labels
     * @throws NullPointerException if labelConsumer is null
     */
    public void forEachLabel(@NotNull BiConsumer<@NotNull String, @NotNull String> labelConsumer) {
        labels.forEachLabel(
                checkNotNull(labelConsumer, "Consumer")
        );
    }
}
```

## File: `agent/src/main/java/io/pyroscope/labels/v2/package-info.java`
```java
/**
 * Package {@code io.pyroscope.labels.v2} provides a new implementation of Pyroscope's context labeling system.
 *
 * <h2>Why v2?</h2>
 *
 * <p>The previous implementation (v1) used an implicit ThreadLocal reference-counted approach to manage context labels.
 * While convenient for simple cases, this approach had several fundamental issues:
 *
 * <ul>
 *   <li>Cross-thread operations could lead to assertion errors, missing labels, or infinite loops</li>
 *   <li>Closing a ScopedContext on a different thread than where it was created caused unpredictable behavior</li>
 *   <li>Implicit label merging made debugging difficult when labels were unexpectedly combined</li>
 *   <li>Thread pools could inherit unexpected labels from previous operations</li>
 * </ul>
 *
 * <h2>Key Differences in v2</h2>
 *
 * <p>The v2 implementation:
 * <ul>
 *   <li>Eliminates implicit label merging - you must explicitly create contexts with all required labels</li>
 *   <li>Requires explicit passing of parent contexts for proper nesting</li>
 *   <li>Manages memory better by cleaning up closed contexts after they're dumped</li>
 *   <li>Adds {@link io.pyroscope.labels.v2.ConstantContext} for static, low-cardinality labels</li>
 * </ul>
 *
 * <h2>Example: v1 vs v2 Implementation</h2>
 *
 * <p>In v1, implicit merging happened at the ThreadLocal level:
 *
 * <pre>{@code
 * // v1: Implicit merging through ThreadLocal
 * try (ScopedContext ctx = new ScopedContext(new LabelsSet("request_id", "239"))) {
 *     try (ScopedContext ctx2 = new ScopedContext(new LabelsSet("op", "doSomething"))) {
 *         doSomething(); // Runs with BOTH "request_id" and "op" labels
 *     }
 * }
 * }</pre>
 *
 * <p>In v2, you must explicitly include all labels or pass the parent context:
 *
 * <pre>{@code
 * // v2: Explicit passing of parent context
 * try (ScopedContext ctx1 = new ScopedContext(new LabelsSet("request_id", "239"))) {
 *     // Option 1: Create new context with ALL needed labels
 *     try (ScopedContext ctx2 = new ScopedContext(new LabelsSet("request_id", "239", "op", "doSomething"))) {
 *         doSomething();
 *     }
 *
 *     // Option 2: Pass parent context to create proper hierarchy
 *     try (ScopedContext ctx2 = new ScopedContext(new LabelsSet("op", "doSomething"), ctx1)) {
 *         doSomething();
 *     }
 * }
 * }</pre>
 */
package io.pyroscope.labels.v2;
```

## File: `agent/src/main/resources/jfr/pyroscope.jfc`
```
<?xml version="1.0" encoding="UTF-8"?>

<configuration version="2.0" label="Pyroscope"
               description="Low overhead configuration safe for continuous use in production environments, typically less than 1 % overhead."
               provider="Pyroscope">

    <event name="jdk.ExecutionSample">
        <setting name="enabled">true</setting>
        <setting name="period">1 ms</setting>
    </event>

    <event name="jdk.ThreadPark">
        <setting name="enabled">true</setting>
        <setting name="stackTrace">true</setting>
        <setting name="threshold">10 ms</setting>
    </event>

    <event name="jdk.ObjectAllocationInNewTLAB">
        <setting name="enabled">true</setting>
        <setting name="stackTrace">true</setting>
    </event>

    <event name="jdk.ObjectAllocationOutsideTLAB">
        <setting name="enabled">true</setting>
        <setting name="stackTrace">true</setting>
    </event>

    <event name="jdk.JavaMonitorEnter">
        <setting name="enabled">true</setting>
        <setting name="stackTrace">true</setting>
        <setting name="threshold">10 ms</setting>
    </event>
</configuration>
```

## File: `agent/src/test/java/io/pyroscope/ConcurrentUsageTest.java`
```java
package io.pyroscope;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class ConcurrentUsageTest {

    @Test
    public void runConcurrently() throws IOException {
        int iterations = 10;
        List<Process> processes = new ArrayList<>();
        for (int i = 0; i < iterations; i++) {
            Process process = new ProcessBuilder(
                "java", "-cp", System.getProperty("java.class.path"), TestApplication.class.getName()
            ).inheritIO().start();
            processes.add(process);
        }

        processes.parallelStream().forEach(p -> {
            int exitCode = 0;
            try {
                exitCode = p.waitFor();
            } catch (InterruptedException e) {
                Assertions.fail("could not get process status", e);
            }
            if (exitCode != 0) {
                Assertions.fail("process failed with exit code: " + exitCode);
            }
        });
    }
}

```

## File: `agent/src/test/java/io/pyroscope/ShadowJarContentsTest.java`
```java
package io.pyroscope;

import org.junit.jupiter.api.Test;

import java.io.File;
import java.util.ArrayList;
import java.util.Enumeration;
import java.util.List;
import java.util.jar.JarEntry;
import java.util.jar.JarFile;

import static org.junit.jupiter.api.Assertions.assertNotNull;
import static org.junit.jupiter.api.Assertions.assertNull;
import static org.junit.jupiter.api.Assertions.assertTrue;
import static org.junit.jupiter.api.Assertions.fail;

/**
 * Verifies that the shadowJar (pyroscope.jar) contains only our own unrelocated classes.
 * All third-party classes must be relocated under io/pyroscope/vendor/.
 */
public class ShadowJarContentsTest {

    @Test
    void onlyPyroscopeClassesAreUnrelocated() throws Exception {
        String jarPath = System.getProperty("shadowJar.path");
        if (jarPath == null || jarPath.isEmpty()) {
            fail("System property 'shadowJar.path' is not set. Run this test via Gradle.");
        }

        File jarFile = new File(jarPath);
        assertTrue(jarFile.exists(), "shadowJar not found at: " + jarPath);

        List<String> violations = new ArrayList<>();

        try (JarFile jar = new JarFile(jarFile)) {
            Enumeration<JarEntry> entries = jar.entries();
            while (entries.hasMoreElements()) {
                JarEntry entry = entries.nextElement();
                String name = entry.getName();

                if (!name.endsWith(".class")) {
                    continue;
                }

                // Skip module-info descriptors (multi-release jar metadata)
                if (name.endsWith("module-info.class")) {
                    continue;
                }

                // Multi-release JARs store versioned classes under META-INF/versions/<N>/
                // Strip that prefix before checking the package
                String effectiveName = name.replaceFirst("^META-INF/versions/\\d+/", "");

                // All class files must be under io/pyroscope/
                if (!effectiveName.startsWith("io/pyroscope/")) {
                    violations.add(name);
                }
            }
        }

        if (!violations.isEmpty()) {
            StringBuilder sb = new StringBuilder();
            sb.append("Found ").append(violations.size()).append(" unrelocated non-pyroscope class(es) in shadowJar:\n");
            for (String v : violations) {
                sb.append("  ").append(v).append("\n");
            }
            fail(sb.toString());
        }
    }

    @Test
    void containsBootstrapApiResource() throws Exception {
        String jarPath = System.getProperty("shadowJar.path");
        if (jarPath == null || jarPath.isEmpty()) {
            fail("System property 'shadowJar.path' is not set. Run this test via Gradle.");
        }

        File jarFile = new File(jarPath);
        assertTrue(jarFile.exists(), "shadowJar not found at: " + jarPath);

        try (JarFile jar = new JarFile(jarFile)) {
            JarEntry entry = jar.getJarEntry("pyroscope-bootstrap.jar.bin");
            assertNotNull(entry, "pyroscope-bootstrap.jar.bin resource not found in shadow jar");
            assertTrue(entry.getSize() > 0, "pyroscope-bootstrap.jar.bin is empty");
        }
    }

    @Test
    void bootstrapApiClassesInShadowJar() throws Exception {
        String jarPath = System.getProperty("shadowJar.path");
        if (jarPath == null || jarPath.isEmpty()) {
            fail("System property 'shadowJar.path' is not set. Run this test via Gradle.");
        }

        File jarFile = new File(jarPath);
        assertTrue(jarFile.exists(), "shadowJar not found at: " + jarPath);

        String[] bootstrapClasses = {
            "io/pyroscope/javaagent/api/ProfilerApi.class",
            "io/pyroscope/javaagent/api/ProfilerApiHolder.class",
            "io/pyroscope/javaagent/api/ProfilerScopedContext.class"
        };

        try (JarFile jar = new JarFile(jarFile)) {
            for (String className : bootstrapClasses) {
                assertNotNull(jar.getJarEntry(className),
                    "Bootstrap-api class should be in shadow jar: " + className);
            }
        }
    }
}
```

## File: `agent/src/test/java/io/pyroscope/TestApplication.java`
```java
package io.pyroscope;

import one.profiler.AsyncProfiler;
import one.profiler.Counter;

import java.util.concurrent.TimeUnit;

public class TestApplication {

    public static void main(String[] args) {
        AsyncProfiler asyncProfiler = PyroscopeAsyncProfiler.getAsyncProfiler();
        asyncProfiler.start("cpu", TimeUnit.SECONDS.toNanos(1));
        try {
            Thread.sleep(1000);
        } catch (InterruptedException e) {
            System.exit(1);
        }
        asyncProfiler.stop();

        System.out.println(
            asyncProfiler + "-" +
                asyncProfiler.dumpCollapsed(Counter.SAMPLES).split(";").length
        );
    }
}
```

## File: `agent/src/test/java/io/pyroscope/javaagent/OverfillQueueTest.java`
```java
package io.pyroscope.javaagent;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class OverfillQueueTest {
    @Test
    void withoutOverfill1() throws InterruptedException {
        final OverfillQueue<Integer> queue = new OverfillQueue<>(5);
        queue.put(0);
        queue.put(1);
        queue.put(2);
        queue.put(3);
        queue.put(4);

        assertEquals(0, queue.take());
        assertEquals(1, queue.take());
        assertEquals(2, queue.take());
        assertEquals(3, queue.take());
        assertEquals(4, queue.take());
    }

    @Test
    void withoutOverfill2() throws InterruptedException {
        final OverfillQueue<Integer> queue = new OverfillQueue<>(5);
        queue.put(0);
        queue.put(1);
        queue.put(2);
        queue.put(3);
        queue.put(4);

        queue.take();
        queue.take();
        queue.take();

        queue.put(5);
        queue.put(6);
        queue.put(7);

        assertEquals(3, queue.take());
        assertEquals(4, queue.take());
        assertEquals(5, queue.take());
        assertEquals(6, queue.take());
        assertEquals(7, queue.take());
    }

    @Test
    void withOverfill() throws InterruptedException {
        final OverfillQueue<Integer> queue = new OverfillQueue<>(5);
        queue.put(0);
        queue.put(1);
        queue.put(2);
        queue.put(3);
        queue.put(4);
        queue.put(5);
        queue.put(6);
        queue.put(7);
        queue.put(8);
        queue.put(9);

        assertEquals(5, queue.take());
        assertEquals(6, queue.take());
        assertEquals(7, queue.take());
        assertEquals(8, queue.take());
        assertEquals(9, queue.take());
    }
}
```

## File: `agent/src/test/java/io/pyroscope/javaagent/PyroscopeAgentTest.java`
```java
package io.pyroscope.javaagent;

import io.pyroscope.javaagent.api.Logger;
import io.pyroscope.javaagent.api.ProfilingScheduler;
import io.pyroscope.javaagent.config.Config;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.Mock;
import org.mockito.junit.jupiter.MockitoExtension;

import static org.mockito.ArgumentMatchers.any;
import static org.mockito.Mockito.*;

@ExtendWith(MockitoExtension.class)
public class PyroscopeAgentTest {

    private Config configAgentEnabled;
    private Config configAgentDisabled;
    private PyroscopeAgent.Options optionsAgentEnabled;
    private PyroscopeAgent.Options optionsAgentDisabled;

    @Mock
    private Logger logger;

    @Mock
    private ProfilingScheduler profilingScheduler;

    @BeforeEach
    void setUp() {
        configAgentEnabled = new Config.Builder()
            .setAgentEnabled(true)
            .build();
        optionsAgentEnabled = new PyroscopeAgent.Options.Builder(configAgentEnabled)
            .setScheduler(profilingScheduler)
            .setLogger(logger)
            .build();

        configAgentDisabled = new Config.Builder()
            .setAgentEnabled(false)
            .build();
        optionsAgentDisabled = new PyroscopeAgent.Options.Builder(configAgentDisabled)
            .setScheduler(profilingScheduler)
            .setLogger(logger)
            .build();
    }

    @AfterEach
    void tearDown() {
        PyroscopeAgent.stop();
    }

    @Test
    void startupTestWithEnabledAgent() {
        PyroscopeAgent.start(optionsAgentEnabled);

        verify(profilingScheduler, times(1)).start(any());
    }

    @Test
    void startupTestWithDisabledAgent() {
        PyroscopeAgent.start(optionsAgentDisabled);

        verify(profilingScheduler, never()).start(any());
    }
}
```

## File: `agent/src/test/java/io/pyroscope/javaagent/StartStopTest.java`
```java
package io.pyroscope.javaagent;

import io.pyroscope.http.Format;
import io.pyroscope.javaagent.api.Logger;
import io.pyroscope.javaagent.config.Config;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;

public class StartStopTest {

    public static final Config INVALID = new Config.Builder()
        .setApplicationName("demo.app{qweqwe=asdasd}")
        .setFormat(Format.JFR)
        .setProfilingAlloc("512k")
        .setAPExtraArguments("event=qwe") // java.lang.IllegalArgumentException: Duplicate event argument
        .setProfilingEvent(EventType.ITIMER)
        .setLogLevel(Logger.Level.DEBUG)
        .build();

    public static final Config VALID = new Config.Builder()
        .setApplicationName("demo.app{qweqwe=asdasd}")
        .setFormat(Format.JFR)
        .setProfilingEvent(EventType.ITIMER)
        .setLogLevel(Logger.Level.DEBUG)
        .build();


    @Test
    void testStartFail() {
        assertFalse(PyroscopeAgent.isStarted());

        PyroscopeAgent.start(INVALID);
        assertFalse(PyroscopeAgent.isStarted());

        PyroscopeAgent.start(INVALID);
        assertFalse(PyroscopeAgent.isStarted());

        PyroscopeAgent.stop();
        assertFalse(PyroscopeAgent.isStarted());
        PyroscopeAgent.stop();
        assertFalse(PyroscopeAgent.isStarted());

        PyroscopeAgent.start(VALID);
        assertTrue(PyroscopeAgent.isStarted());

        PyroscopeAgent.stop();
        assertFalse(PyroscopeAgent.isStarted());
    }

}
```

## File: `agent/src/test/java/io/pyroscope/javaagent/config/AppNameTest.java`
```java
package io.pyroscope.javaagent.config;

import org.junit.jupiter.api.Test;

import java.util.HashMap;
import java.util.Map;

import static java.util.Collections.emptyMap;
import static org.junit.jupiter.api.Assertions.*;

class AppNameTest {
    @Test
    void withoutLabels() {
        AppName app = AppName.parse("test.app");
        assertEquals(app.name, "test.app");
        assertEquals(app.labels, emptyMap());
    }

    @Test
    void emptyLabels() {
        AppName app = AppName.parse("test.app{}");
        assertEquals(app.name, "test.app");
        assertEquals(app.labels, emptyMap());
    }

    @Test
    void singleLabel() {
        AppName app = AppName.parse("test.app{foo=bar}");
        assertEquals(app.name, "test.app");
        assertEquals(app.labels, mapOf("foo", "bar"));
    }

    @Test
    void twoLabels() {
        AppName app = AppName.parse("test.app{foo=bar,fiz=baz}");
        assertEquals(app.name, "test.app");
        assertEquals(app.labels, mapOf("foo", "bar", "fiz", "baz"));
        assertEquals("test.app{fiz=baz,foo=bar}", app.toString());
    }

    @Test
    void emptyKey() {
        AppName app = AppName.parse("test.app{=bar , fiz=baz}");
        assertEquals(app.name, "test.app");
        assertEquals(app.labels, mapOf("fiz", "baz"));
    }

    @Test
    void emptyValue() {
        AppName app = AppName.parse("test.app{foo= , fiz=baz}");
        assertEquals(app.name, "test.app");
        assertEquals(app.labels, mapOf("fiz", "baz"));
    }

    @Test
    void noEqSign() {
        AppName app = AppName.parse("test.app{foo= , fiz=baz}");
        assertEquals(app.name, "test.app");
        assertEquals(app.labels, mapOf("fiz", "baz"));
    }

    private static Map<String, String> mapOf(String ...ss) {
        HashMap<String, String> res = new HashMap<>();
        for (int i = 0; i < ss.length; i+=2) {
            res.put(ss[i], ss[i + 1]);
        }
        return res;
    }
}
```

## File: `agent/src/test/java/io/pyroscope/javaagent/config/IntervalParserTest.java`
```java
package io.pyroscope.javaagent.config;

import org.junit.jupiter.api.Test;

import java.time.Duration;
import java.time.temporal.ChronoUnit;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;

public class IntervalParserTest {
    @Test
    void testNanos() {
        NumberFormatException numberFormatException = assertThrows(
                NumberFormatException.class, () -> IntervalParser.parse("-1"));
        assertEquals("Interval must be positive, but -1 given", numberFormatException.getMessage());

        numberFormatException = assertThrows(NumberFormatException.class, () -> IntervalParser.parse("0"));
        assertEquals("Interval must be positive, but 0 given", numberFormatException.getMessage());

        assertEquals(Duration.ofNanos(10), IntervalParser.parse("10"));
    }

    @Test
    void testMicros() {
        NumberFormatException numberFormatException = assertThrows(
                NumberFormatException.class, () -> IntervalParser.parse("-1us"));
        assertEquals("Interval must be positive, but -1us given", numberFormatException.getMessage());

        numberFormatException = assertThrows(NumberFormatException.class, () -> IntervalParser.parse("0us"));
        assertEquals("Interval must be positive, but 0us given", numberFormatException.getMessage());

        assertEquals(Duration.of(10, ChronoUnit.MICROS), IntervalParser.parse("10us"));
    }

    @Test
    void testMillis() {
        NumberFormatException numberFormatException = assertThrows(
                NumberFormatException.class, () -> IntervalParser.parse("-1ms"));
        assertEquals("Interval must be positive, but -1ms given", numberFormatException.getMessage());

        numberFormatException = assertThrows(NumberFormatException.class, () -> IntervalParser.parse("0ms"));
        assertEquals("Interval must be positive, but 0ms given", numberFormatException.getMessage());

        assertEquals(Duration.ofMillis(10), IntervalParser.parse("10ms"));
    }

    @Test
    void testSeconds() {
        NumberFormatException numberFormatException = assertThrows(
                NumberFormatException.class, () -> IntervalParser.parse("-1s"));
        assertEquals("Interval must be positive, but -1s given", numberFormatException.getMessage());

        numberFormatException = assertThrows(NumberFormatException.class, () -> IntervalParser.parse("0s"));
        assertEquals("Interval must be positive, but 0s given", numberFormatException.getMessage());

        assertEquals(Duration.ofSeconds(10), IntervalParser.parse("10s"));
    }

    @Test
    void testUnknownUnit() {
        NumberFormatException numberFormatException = assertThrows(
                NumberFormatException.class, () -> IntervalParser.parse("10k"));
        assertEquals("Cannot parse interval 10k", numberFormatException.getMessage());
    }
}
```

## File: `agent/src/test/java/io/pyroscope/javaagent/impl/ExponentialBackoffTest.java`
```java
package io.pyroscope.javaagent.impl;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.junit.jupiter.MockitoExtension;

import java.util.Random;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.mockito.ArgumentMatchers.anyInt;
import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.when;
import static org.mockito.Mockito.withSettings;

@ExtendWith(MockitoExtension.class)
public class ExponentialBackoffTest {
    @Test
    void test() {
        final Random random = mock(Random.class, withSettings().withoutAnnotations());
        when(random.nextInt(anyInt())).then(invocation -> invocation.getArgument(0));

        final ExponentialBackoff exponentialBackoff = new ExponentialBackoff(1_000, 30_000, random);
        assertEquals(1_000, exponentialBackoff.error());
        assertEquals(2_000, exponentialBackoff.error());
        assertEquals(4_000, exponentialBackoff.error());
        assertEquals(8_000, exponentialBackoff.error());
        assertEquals(16_000, exponentialBackoff.error());
        assertEquals(30_000, exponentialBackoff.error());
        assertEquals(30_000, exponentialBackoff.error());
        exponentialBackoff.reset();
        assertEquals(1_000, exponentialBackoff.error());
        assertEquals(2_000, exponentialBackoff.error());
        assertEquals(4_000, exponentialBackoff.error());
        assertEquals(8_000, exponentialBackoff.error());
        assertEquals(16_000, exponentialBackoff.error());
        for (int i = 0; i < 100; i++) {
            assertEquals(30_000, exponentialBackoff.error());
        }
    }
}
```

## File: `agent/src/test/java/io/pyroscope/labels/v2/LabelsTest.java`
```java
package io.pyroscope.labels.v2;


import io.pyroscope.PyroscopeAsyncProfiler;
import io.pyroscope.labels.pb.JfrLabels.LabelsSnapshot;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.util.*;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;

import static org.junit.jupiter.api.Assertions.*;

public class LabelsTest {
    static {
        PyroscopeAsyncProfiler.getAsyncProfiler();
    }

    @BeforeEach
    void setUp() {
        resetForTesting();
    }

    @Test
    void testOneLabelSet() {
        try (ScopedContext s = new ScopedContext(new LabelsSet("k1", "v1"))) {
            {
                assertSnapshot(
                        expectSnapshot()
                                .add(1L, "k1", "v1")
                        ,
                        Pyroscope.LabelsWrapper.dump());
            }
            {
                assertSnapshot(
                        expectSnapshot()
                                .add(1L, "k1", "v1")
                        ,
                        Pyroscope.LabelsWrapper.dump());
            }
        }
        {
            assertSnapshot(
                    expectSnapshot()
                            .add(1L, "k1", "v1")
                    ,
                    Pyroscope.LabelsWrapper.dump());
        }

        {
            assertSnapshot(
                    expectSnapshot()
                    ,
                    Pyroscope.LabelsWrapper.dump());
        }
    }


    @Test
    void testNestedEqualLabelSets() {
        try (ScopedContext ignored = new ScopedContext(new LabelsSet("k1", "v1"))) {
            try (ScopedContext s = new ScopedContext(new LabelsSet("k1", "v1"))) {
                assertSnapshot(
                        expectSnapshot()
                                .add(1L, "k1", "v1")
                                .add(2L, "k1", "v1")
                        ,
                        Pyroscope.LabelsWrapper.dump());
            }
            assertSnapshot(
                    expectSnapshot()
                            .add(1L, "k1", "v1")
                            .add(2L, "k1", "v1")
                    ,
                    Pyroscope.LabelsWrapper.dump());
            assertSnapshot(
                    expectSnapshot()
                            .add(1L, "k1", "v1")
                    ,
                    Pyroscope.LabelsWrapper.dump());
        }
        {
            assertSnapshot(
                    expectSnapshot()
                            .add(1L, "k1", "v1")
                    ,
                    Pyroscope.LabelsWrapper.dump());
        }
        {
            assertSnapshot(
                    expectSnapshot()
                    ,
                    Pyroscope.LabelsWrapper.dump());
        }
    }


    @Test
    void exception() {
        try (ScopedContext s = new ScopedContext(new LabelsSet("k1", "v1"))) {
            try {
                try (ScopedContext s2 = new ScopedContext(new LabelsSet("k1", "v2"))) {
                    assertSnapshot(
                            expectSnapshot()
                                    .add(1L, "k1", "v1")
                                    .add(2L, "k1", "v2")
                            ,
                            Pyroscope.LabelsWrapper.dump());
                    throw new AssertionError();
                }
            } catch (AssertionError e) {
                {
                    assertSnapshot(
                            expectSnapshot()
                                    .add(1L, "k1", "v1")
                                    .add(2L, "k1", "v2")
                            ,
                            Pyroscope.LabelsWrapper.dump());
                }
                {
                    assertSnapshot(
                            expectSnapshot()
                                    .add(1L, "k1", "v1")
                            ,
                            Pyroscope.LabelsWrapper.dump());
                }
            }
        }
        {
            assertSnapshot(
                    expectSnapshot()
                            .add(1L, "k1", "v1")
                    ,
                    Pyroscope.LabelsWrapper.dump());
        }
        {
            assertSnapshot(
                    expectSnapshot()
                    ,
                    Pyroscope.LabelsWrapper.dump());
        }
    }

    @Test
    void testConst() {
        try (ScopedContext s = new ScopedContext(new LabelsSet("k1", "v1"))) {

        }

        ConstantContext.of(new LabelsSet("path", "/foo/bar", "qwe", "asd"));
        ConstantContext.of(new LabelsSet("path", "/qwe/asd", "zxc", "ass"));

        assertSnapshot(
                expectSnapshot()
                        .add(1L, "k1", "v1")
                        .add(2L, "path", "/foo/bar", "qwe", "asd")
                        .add(3L, "path", "/qwe/asd", "zxc", "ass")
                ,
                Pyroscope.LabelsWrapper.dump());

        assertSnapshot(
                expectSnapshot()
                        .add(2L, "path", "/foo/bar", "qwe", "asd")
                        .add(3L, "path", "/qwe/asd", "zxc", "ass")
                ,
                Pyroscope.LabelsWrapper.dump());
    }

    void assertSnapshot(ExpectedContextBuilder expected, LabelsSnapshot snapshot) {
        Map<Long, Map<String, String>> expectedContexts = expected.contexts;
        final HashSet<String> uniqueStrings = new HashSet<>();
        Map<Long, Map<String, String>> actualContexts = new HashMap<>();
        snapshot.getContextsMap().forEach((contextID, context) -> {
            final Map<String, String> ctx = new HashMap<>();
            context.getLabelsMap().forEach((key, value) -> {
                ctx.put(snapshot.getStringsMap().get(key), snapshot.getStringsMap().get(value));
                uniqueStrings.add(snapshot.getStringsMap().get(key));
                uniqueStrings.add(snapshot.getStringsMap().get(value));
            });
            actualContexts.put(contextID, ctx);
        });
        uniqueStrings.addAll(expected.constant.values());
        assertEquals(uniqueStrings.size(), snapshot.getStringsCount());
        assertEquals(expectedContexts, actualContexts);
    }


    @Test
    void stressTest() throws InterruptedException {
        final int n = 8;
        final ExecutorService e = Executors.newFixedThreadPool(n);
        final int iter = 10000;
        final int nspans = 1024;
        final List<String> spasn = new ArrayList<>(nspans);
        for (int i = 0; i < nspans; i++) {
            spasn.add("span" + i);
        }
        final long t1 = System.currentTimeMillis();
        for (int i = 0; i < n; i++) {
            e.submit(() -> {
                final Random r = new Random();
                for (int j = 0; j < iter; j++) {
                    final LabelsSet ls = new LabelsSet(
                            "SpanName", spasn.get(r.nextInt(spasn.size())),
                            "SpanId", Long.toHexString(r.nextLong())
                    );
                    Pyroscope.LabelsWrapper.run(ls, () -> {
                        final LabelsSet ls2 = new LabelsSet(
                                "SpanName", spasn.get(r.nextInt(spasn.size())),
                                "SpanId", Long.toHexString(r.nextLong())
                        );
                        Pyroscope.LabelsWrapper.run(ls2, () -> {


                        });
                    });

                }
            });
        }
        e.shutdown();
        e.awaitTermination(100, TimeUnit.SECONDS);
        final long t2 = System.currentTimeMillis();
        System.out.println("time: " + (t2 - t1));
//        Thread.sleep(1123123123123L);
        Pyroscope.LabelsWrapper.dump();
        final long t3 = System.currentTimeMillis();
        System.out.println("dump time: " + (t3 - t2));
    }

    @Test
    void stressTestConst() throws InterruptedException {
        final int n = 8;
        final Random r = new Random();
        final ExecutorService e = Executors.newFixedThreadPool(n);
        final int iter = 100000;
        final List<ConstantContext> ctxs = generateConstantContexts(r);
        final long t1 = System.currentTimeMillis();
        for (int i = 0; i < n; i++) {
            e.submit(() -> {
                final Random tr = new Random();
                for (int j = 0; j < iter; j++) {
                    ConstantContext c1 = ctxs.get(tr.nextInt(ctxs.size()));
                    ConstantContext c2 = ctxs.get(tr.nextInt(ctxs.size()));
                    ConstantContext c3 = ctxs.get(tr.nextInt(ctxs.size()));
                    c1.activate();
                    c2.activate();
                    c3.activate();
                    c3.deactivate();
                }
            });
        }
        e.shutdown();
        e.awaitTermination(100, TimeUnit.SECONDS);
        final long t2 = System.currentTimeMillis();
        System.out.println("time: " + (t2 - t1));
//        Thread.sleep(1123123123123L);
        Pyroscope.LabelsWrapper.dump();
    }

    @Test
    void registerStringConstant() {
        long c1 = Pyroscope.LabelsWrapper.registerConstant("const1");
        long c2;
        try (ScopedContext s = new ScopedContext(new LabelsSet("k1", "v1"))) {
            c2 = Pyroscope.LabelsWrapper.registerConstant("const2");
        }
        long c3 = Pyroscope.LabelsWrapper.registerConstant("const3");
        {
            LabelsSnapshot snapshot = Pyroscope.LabelsWrapper.dump();
            assertSnapshot(
                    expectSnapshot()
                            .constant(1L, "const1")
                            .constant(2L, "const2")
                            .constant(3L, "const3")
                            .add(1L, "k1", "v1"),
                    snapshot
            );
        }
        {
            LabelsSnapshot snapshot = Pyroscope.LabelsWrapper.dump();
            assertSnapshot(
                    expectSnapshot()
                            .constant(1L, "const1")
                            .constant(2L, "const2")
                            .constant(3L, "const3"),
                    snapshot
            );
        }
    }

    private static ExpectedContextBuilder expectSnapshot() {
        return new ExpectedContextBuilder();
    }

    private static List<ConstantContext> generateConstantContexts(Random r) {
        final int nctx = 10240;
        final List<ConstantContext> ctxs = new ArrayList<>(nctx);
        for (int i = 0; i < nctx; i++) {
            List<String> labels = new ArrayList<>();
            labels.add("PATH");
            labels.add("/foo/bar");
            labels.add("METHOD");
            labels.add("GET");
            for (int j = 0; j < 100; j++) {
                labels.add("randomkey" + r.nextLong());
                labels.add("randombal" + r.nextLong());
            }
            LabelsSet k1 = new LabelsSet(labels.toArray(new String[0]));
            ctxs.add(ConstantContext.of(k1));
        }
        return ctxs;
    }

    private static class ExpectedContextBuilder {
        final Map<Long, Map<String, String>> contexts = new HashMap<>();
        final Map<Long, String> constant = new HashMap<>();


        ExpectedContextBuilder add(Long cid, String... ss) {
            contexts.put(cid, mapOf(ss));
            return this;
        }

        ExpectedContextBuilder constant(Long cid, String s) {
            constant.put(cid, s);
            return this;
        }

        ExpectedContextBuilder remove(Long cid) {
            contexts.remove(cid);
            return this;
        }
    }

    private static Map<Long, Long> mapOf(Long k, Long v) {
        HashMap<Long, Long> res = new HashMap<>();
        res.put(k, v);
        return res;
    }

    private static Map<String, String> mapOf(String... ss) {
        assertTrue(ss.length % 2 == 0);
        HashMap<String, String> res = new HashMap<>();
        for (int i = 0; i < ss.length; i++) {
            res.put(ss[i], ss[i + 1]);
            i += 1;
        }
        return res;
    }

    static void resetForTesting() {
        ScopedContext.ENABLED.set(true);
        ScopedContext.CONTEXTS.clear();
        ScopedContext.CONSTANT_CONTEXTS.clear();
        ScopedContext.CONTEXT_COUNTER.set(0);
        Pyroscope.LabelsWrapper.CONSTANTS.clear();
    }
}
```

## File: `async-profiler-grafana-fork-dist/lib/libasyncProfiler-linux-arm64.so.sha1`
```
8327292d14d9513a296a208c022adf01a1b0ca3c
```

## File: `async-profiler-grafana-fork-dist/lib/libasyncProfiler-linux-x64.so.sha1`
```
9c277b06ac6ffc80c9225dbef119f1e2e82f829b
```

## File: `async-profiler-grafana-fork-dist/lib/libasyncProfiler-macos.so.sha1`
```
9d82f9a40d57e0706f7d9043e550524ce3131861
```

## File: `demo/build.gradle`
```
plugins {
    id 'org.jetbrains.kotlin.jvm' version '2.3.0'
}
import org.jetbrains.kotlin.gradle.dsl.JvmTarget

java {
    sourceCompatibility = JavaVersion.VERSION_1_8
    targetCompatibility = JavaVersion.VERSION_1_8
}

repositories {
    mavenCentral()
}
dependencies {
    implementation(project(":agent"))
}
kotlin{
    compilerOptions{
        jvmTarget.set(JvmTarget.JVM_1_8)
    }
}
```

## File: `demo/src/main/java/App.java`
```java
import io.pyroscope.http.Format;
import io.pyroscope.javaagent.EventType;
import io.pyroscope.javaagent.PyroscopeAgent;
import io.pyroscope.javaagent.api.Logger;
import io.pyroscope.javaagent.config.Config;
import io.pyroscope.javaagent.config.ProfilerType;
import io.pyroscope.labels.v2.LabelsSet;
import io.pyroscope.labels.v2.Pyroscope;

import java.util.HashMap;
import java.util.Map;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class App {
    public static final int N_THREADS = 8;

    public static void main(String[] args) {
        PyroscopeAgent.start(
            new PyroscopeAgent.Options.Builder(
                new Config.Builder()
                    .setApplicationName("demo.app{qweqwe=asdasd}")
                    .setServerAddress("http://localhost:4040")
                    .setFormat(Format.JFR)
                    .setProfilingEvent(EventType.CTIMER)
                    .setLogLevel(Logger.Level.DEBUG)
                    .setProfilerType(ProfilerType.JFR)
                    .setLabels(mapOf("user", "tolyan"))
                    .build())
                .build()
        );
        Pyroscope.setStaticLabels(mapOf("region", "us-east-1"));

        appLogic();
    }

    private static void appLogic() {
        ExecutorService executors = Executors.newFixedThreadPool(N_THREADS);
        for (int i = 0; i < N_THREADS; i++) {
            executors.submit(() -> {
                Pyroscope.LabelsWrapper.run(new LabelsSet("thread_name", Thread.currentThread().getName()), () -> {
                        while (true) {
                            try {
                                fib(32L);
                            } catch (InterruptedException e) {
                                Thread.currentThread().interrupt();
                                break;
                            }
                        }
                    }
                );
            });
        }
    }

    private static Map<String, String> mapOf(String... args) {
        Map<String, String> staticLabels = new HashMap<>();
        for (int i = 0; i < args.length; i += 2) {
            staticLabels.put(args[i], args[i + 1]);
        }
        return staticLabels;
    }

    private static long fib(Long n) throws InterruptedException {
        if (n == 0L) {
            return 0L;
        }
        if (n == 1L) {
            return 1L;
        }
        return fib(n - 1) + fib(n - 2);
    }
}
```

## File: `demo/src/main/java/Fib.java`
```java

import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class Fib {
    public static final int N_THREADS;

    static {
        int n;
        try {
            n = Integer.parseInt(System.getenv("N_THREADS"));
        } catch (NumberFormatException e) {
            n = 1;
        }
        N_THREADS = n;
    }

    public static void main(String[] args) {
        appLogic();
    }

    private static void appLogic() {
        ExecutorService executors = Executors.newFixedThreadPool(N_THREADS);
        for (int i = 0; i < N_THREADS; i++) {
            executors.submit(() -> {
                while (true) {
                    try {
                        fib(32L);
                    } catch (InterruptedException e) {
                        Thread.currentThread().interrupt();
                        break;
                    }
                }
            });
        }
    }

    private static long fib(Long n) throws InterruptedException {
        if (n == 0L) {
            return 0L;
        }
        if (n == 1L) {
            return 1L;
        }
        return fib(n - 1) + fib(n - 2);
    }

}
```

## File: `demo/src/main/java/StartStopApp.java`
```java
import io.pyroscope.http.Format;
import io.pyroscope.javaagent.EventType;
import io.pyroscope.javaagent.PyroscopeAgent;
import io.pyroscope.javaagent.api.Logger;
import io.pyroscope.javaagent.config.Config;
import io.pyroscope.labels.v2.LabelsSet;
import io.pyroscope.labels.v2.Pyroscope;

import java.util.HashMap;
import java.util.Map;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class StartStopApp {
    public static final int N_THREADS = 2;
    public static final Config CONFIG = new Config.Builder()
        .setApplicationName("demo.app{qweqwe=asdasd}")
        .setServerAddress("http://localhost:4040")
        .setFormat(Format.JFR)
        .setProfilingEvent(EventType.ITIMER)
        .setLogLevel(Logger.Level.DEBUG)
        .setLabels(mapOf("user", "tolyan"))
        .build();
    public static final PyroscopeAgent.Options OPTIONS = new PyroscopeAgent.Options.Builder(CONFIG)
        .build();

    public static final int RUN_TIME = 30000;
    public static final int SLEEP_TIME = 30000;

    public static void main(String[] args) {


        appLogic();

        while (true) {
            Pyroscope.setStaticLabels(mapOf("region", "us-east-1"));
            PyroscopeAgent.start(OPTIONS);

            System.out.println(">>> running for " + RUN_TIME);
            try {
                Thread.sleep(RUN_TIME);
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
                break;
            }

            PyroscopeAgent.stop();

            System.out.println(">>> sleeping for " + RUN_TIME);
            try {
                Thread.sleep(SLEEP_TIME);
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
                break;
            }
        }
    }

    private static void appLogic() {
        ExecutorService executors = Executors.newFixedThreadPool(N_THREADS);
        for (int i = 0; i < N_THREADS; i++) {
            executors.submit(() -> {
                Pyroscope.LabelsWrapper.run(new LabelsSet("thread_name", Thread.currentThread().getName()), () -> {
                        while (true) {
                            try {
                                fib(32L);
                            } catch (InterruptedException e) {
                                Thread.currentThread().interrupt();
                                break;
                            }
                        }
                    }
                );
            });
        }
    }

    private static Map<String, String> mapOf(String... args) {
        Map<String, String> staticLabels = new HashMap<>();
        for (int i = 0; i < args.length; i += 2) {
            staticLabels.put(args[i], args[i + 1]);
        }
        return staticLabels;
    }

    private static long fib(Long n) throws InterruptedException {
        if (n == 0L) {
            return 0L;
        }
        if (n == 1L) {
            return 1L;
        }
        return fib(n - 1) + fib(n - 2);
    }
}
```

## File: `demo/src/main/kotlin/TracingContext.kt`
```
import io.pyroscope.PyroscopeAsyncProfiler
import io.pyroscope.javaagent.EventType
import io.pyroscope.javaagent.PyroscopeAgent
import io.pyroscope.javaagent.Snapshot
import io.pyroscope.javaagent.api.Exporter
import io.pyroscope.javaagent.api.Logger
import io.pyroscope.javaagent.config.Config
import io.pyroscope.javaagent.impl.DefaultLogger
import io.pyroscope.javaagent.impl.PyroscopeExporter
import io.pyroscope.javaagent.impl.QueuedExporter
import io.pyroscope.labels.v2.LabelsSet
import io.pyroscope.labels.v2.Pyroscope
import io.pyroscope.labels.v2.ScopedContext
import java.io.File
import java.util.concurrent.atomic.AtomicLong

fun fib(n: Int): Int {
    if (n <= 1) {
        return 1
    }
    return fib(n - 1) + fib(n - 2)
}

fun inf() {
    while (true) {

    }
}

fun main() {
    val constFib = Pyroscope.LabelsWrapper.registerConstant("Fibonachi")
    val constInf = Pyroscope.LabelsWrapper.registerConstant("Infinite")
    println(constFib)
    println(constInf)

    val config = Config.Builder()
        .setApplicationName("spanContextApp")
        .setProfilingEvent(EventType.CTIMER)
        .build()
    val logger = DefaultLogger(Logger.Level.DEBUG, System.out)
    val exporter = QueuedExporter(config, PyroscopeExporter(config, logger), logger)

    val opt = PyroscopeAgent.Options.Builder(config)
        .setLogger(logger)
        .setExporter(Dumper(exporter))
        .build()
    PyroscopeAgent.start(opt)

    val t1 = Thread {
        PyroscopeAsyncProfiler.getAsyncProfiler()
            .setTracingContext(239, constFib);
        ScopedContext(LabelsSet("dyn2", "v2")).use {
            while (true) {
                fib(13)
            }
        }
    }
    val t2 = Thread {
        PyroscopeAsyncProfiler.getAsyncProfiler()
            .setTracingContext(4242, constInf);

        ScopedContext(LabelsSet("dyn1", "v1")).use {
            inf()
        }
    }
    t1.start()
    t2.start()

}

class Dumper(
    val next: Exporter,
) : Exporter {
    private val counter: AtomicLong = AtomicLong()
    override fun export(p0: Snapshot) {
        val no = counter.incrementAndGet()
        File("./profile.${no}.bin").writeBytes(p0.data)
        File("./profile.${no}.labels.bin").writeBytes(p0.labels.toByteArray())
        next.export(p0)
    }

    override fun stop() {
        next.stop()
    }

}
```

## File: `examples/Dockerfile`
```
FROM openjdk:11.0.16-jdk@sha256:99bac5bf83633e3c7399aed725c8415e7b569b54e03e4599e580fc9cdb7c21ab

ADD https://download.jboss.org/optaplanner/release/8.6.0.Final/optaweb-employee-rostering-distribution-8.6.0.Final.zip /

RUN apt-get update && apt-get install -y unzip \
    && rm -rf /var/lib/apt/lists/*

RUN unzip optaweb-employee-rostering-distribution-8.6.0.Final.zip && \
    rm optaweb-employee-rostering-distribution-8.6.0.Final.zip

ADD pyroscope.jar /

CMD ["java", "-javaagent:/pyroscope.jar", "-jar", "/optaweb-employee-rostering-distribution-8.6.0.Final/bin/optaweb-employee-rostering-standalone-8.6.0.Final/quarkus-run.jar"]
```

## File: `examples/docker-compose-base.yml`
```yaml
services:
  pyroscope:
    image: "grafana/pyroscope:1.18.0@sha256:e7edae4fd99dbb8695a1e03d7db96ab247630cf83842407908922b2f66aafc6a"
    ports:
      - "4040:4040"
  app:
    build: .
    environment:
      - PYROSCOPE_APPLICATION_NAME=optaplanner
      - PYROSCOPE_PROFILING_INTERVAL=10ms
      - PYROSCOPE_PROFILER_EVENT=itimer
      - PYROSCOPE_UPLOAD_INTERVAL=1s
      - PYROSCOPE_LOG_LEVEL=debug
      - PYROSCOPE_SERVER_ADDRESS=http://pyroscope:4040
      - PYROSCOPE_AUTH_TOKEN=abc123
    ports:
      - "8080:8080"
```

## File: `examples/docker-compose-expt.yml`
```yaml
services:
  pyroscope:
    image: "grafana/pyroscope:1.18.0@sha256:e7edae4fd99dbb8695a1e03d7db96ab247630cf83842407908922b2f66aafc6a"
    ports:
      - "4040:4040"
  app:
    build: .
    environment:
      - PYROSCOPE_APPLICATION_NAME=optaplanner
      - PYROSCOPE_PROFILING_INTERVAL=10ms
      - PYROSCOPE_PROFILER_EVENT=itimer
      - PYROSCOPE_PROFILER_ALLOC=4k
      - PYROSCOPE_UPLOAD_INTERVAL=8s
      - PYROSCOPE_SAMPLING_DURATION=2s
      - PYROSCOPE_FORMAT=jfr
      - PYROSCOPE_SAMPLING_EVENT_ORDER=itimer,alloc
      - PYROSCOPE_LOG_LEVEL=debug
      - PYROSCOPE_SERVER_ADDRESS=http://pyroscope:4040
      - PYROSCOPE_AUTH_TOKEN=abc123
    ports:
      - "8080:8080"
```

## File: `gradle/wrapper/gradle-wrapper.properties`
```
distributionBase=GRADLE_USER_HOME
distributionPath=wrapper/dists
distributionUrl=https\://services.gradle.org/distributions/gradle-8.14.3-bin.zip
networkTimeout=10000
validateDistributionUrl=true
zipStoreBase=GRADLE_USER_HOME
zipStorePath=wrapper/dists
```

## File: `itest/query/go.mod`
```
module java-test-querier

go 1.24.6

toolchain go1.25.6

require (
	connectrpc.com/connect v1.19.1
	github.com/grafana/pyroscope/api v1.3.0
)

require (
	github.com/google/gnostic v0.7.1 // indirect
	github.com/google/gnostic-models v0.7.0 // indirect
	github.com/gorilla/mux v1.8.1 // indirect
	github.com/planetscale/vtprotobuf v0.6.1-0.20250313105119-ba97887b0a25 // indirect
	go.yaml.in/yaml/v3 v3.0.4 // indirect
	golang.org/x/net v0.48.0 // indirect
	golang.org/x/sys v0.39.0 // indirect
	golang.org/x/text v0.33.0 // indirect
	google.golang.org/genproto/googleapis/rpc v0.0.0-20260120221211-b8f7ae30c516 // indirect
	google.golang.org/grpc v1.79.3 // indirect
	google.golang.org/protobuf v1.36.11 // indirect
)
```

## File: `itest/query/go.sum`
```
connectrpc.com/connect v1.19.1 h1:R5M57z05+90EfEvCY1b7hBxDVOUl45PrtXtAV2fOC14=
connectrpc.com/connect v1.19.1/go.mod h1:tN20fjdGlewnSFeZxLKb0xwIZ6ozc3OQs2hTXy4du9w=
github.com/cespare/xxhash/v2 v2.3.0 h1:UL815xU9SqsFlibzuggzjXhog7bL6oX9BbNZnL2UFvs=
github.com/cespare/xxhash/v2 v2.3.0/go.mod h1:VGX0DQ3Q6kWi7AoAeZDth3/j3BFtOZR5XLFGgcrjCOs=
github.com/go-logr/logr v1.4.3 h1:CjnDlHq8ikf6E492q6eKboGOC0T8CDaOvkHCIg8idEI=
github.com/go-logr/logr v1.4.3/go.mod h1:9T104GzyrTigFIr8wt5mBrctHMim0Nb2HLGrmQ40KvY=
github.com/go-logr/stdr v1.2.2 h1:hSWxHoqTgW2S2qGc0LTAI563KZ5YKYRhT3MFKZMbjag=
github.com/go-logr/stdr v1.2.2/go.mod h1:mMo/vtBO5dYbehREoey6XUKy/eSumjCCveDpRre4VKE=
github.com/golang/protobuf v1.5.4 h1:i7eJL8qZTpSEXOPTxNKhASYpMn+8e5Q6AdndVa1dWek=
github.com/golang/protobuf v1.5.4/go.mod h1:lnTiLA8Wa4RWRcIUkrtSVa5nRhsEGBg48fD6rSs7xps=
github.com/google/gnostic v0.7.1 h1:t5Kc7j/8kYr8t2u11rykRrPPovlEMG4+xdc/SpekATs=
github.com/google/gnostic v0.7.1/go.mod h1:KSw6sxnxEBFM8jLPfJd46xZP+yQcfE8XkiqfZx5zR28=
github.com/google/gnostic-models v0.7.0 h1:qwTtogB15McXDaNqTZdzPJRHvaVJlAl+HVQnLmJEJxo=
github.com/google/gnostic-models v0.7.0/go.mod h1:whL5G0m6dmc5cPxKc5bdKdEN3UjI7OUGxBlw57miDrQ=
github.com/google/go-cmp v0.7.0 h1:wk8382ETsv4JYUZwIsn6YpYiWiBsYLSJiTsyBybVuN8=
github.com/google/go-cmp v0.7.0/go.mod h1:pXiqmnSA92OHEEa9HXL2W4E7lf9JzCmGVUdgjX3N/iU=
github.com/google/uuid v1.6.0 h1:NIvaJDMOsjHA8n1jAhLSgzrAzy1Hgr+hNrb57e+94F0=
github.com/google/uuid v1.6.0/go.mod h1:TIyPZe4MgqvfeYDBFedMoGGpEw/LqOeaOT+nhxU+yHo=
github.com/gorilla/mux v1.8.1 h1:TuBL49tXwgrFYWhqrNgrUNEY92u81SPhu7sTdzQEiWY=
github.com/gorilla/mux v1.8.1/go.mod h1:AKf9I4AEqPTmMytcMc0KkNouC66V3BtZ4qD5fmWSiMQ=
github.com/grafana/pyroscope/api v1.3.0 h1:wzOC+3k9Yn247E3rftOaHlO0MG7mQL48eab/EOFujsU=
github.com/grafana/pyroscope/api v1.3.0/go.mod h1:K4BU7r29UGWJfAF29ySzQQ9wvVvWsEU7IaRXIa89ZwA=
github.com/planetscale/vtprotobuf v0.6.1-0.20250313105119-ba97887b0a25 h1:S1hI5JiKP7883xBzZAr1ydcxrKNSVNm7+3+JwjxZEsg=
github.com/planetscale/vtprotobuf v0.6.1-0.20250313105119-ba97887b0a25/go.mod h1:ZQntvDG8TkPgljxtA0R9frDoND4QORU1VXz015N5Ks4=
go.opentelemetry.io/auto/sdk v1.2.1 h1:jXsnJ4Lmnqd11kwkBV2LgLoFMZKizbCi5fNZ/ipaZ64=
go.opentelemetry.io/auto/sdk v1.2.1/go.mod h1:KRTj+aOaElaLi+wW1kO/DZRXwkF4C5xPbEe3ZiIhN7Y=
go.opentelemetry.io/otel v1.39.0 h1:8yPrr/S0ND9QEfTfdP9V+SiwT4E0G7Y5MO7p85nis48=
go.opentelemetry.io/otel v1.39.0/go.mod h1:kLlFTywNWrFyEdH0oj2xK0bFYZtHRYUdv1NklR/tgc8=
go.opentelemetry.io/otel/metric v1.39.0 h1:d1UzonvEZriVfpNKEVmHXbdf909uGTOQjA0HF0Ls5Q0=
go.opentelemetry.io/otel/metric v1.39.0/go.mod h1:jrZSWL33sD7bBxg1xjrqyDjnuzTUB0x1nBERXd7Ftcs=
go.opentelemetry.io/otel/sdk v1.39.0 h1:nMLYcjVsvdui1B/4FRkwjzoRVsMK8uL/cj0OyhKzt18=
go.opentelemetry.io/otel/sdk v1.39.0/go.mod h1:vDojkC4/jsTJsE+kh+LXYQlbL8CgrEcwmt1ENZszdJE=
go.opentelemetry.io/otel/sdk/metric v1.39.0 h1:cXMVVFVgsIf2YL6QkRF4Urbr/aMInf+2WKg+sEJTtB8=
go.opentelemetry.io/otel/sdk/metric v1.39.0/go.mod h1:xq9HEVH7qeX69/JnwEfp6fVq5wosJsY1mt4lLfYdVew=
go.opentelemetry.io/otel/trace v1.39.0 h1:2d2vfpEDmCJ5zVYz7ijaJdOF59xLomrvj7bjt6/qCJI=
go.opentelemetry.io/otel/trace v1.39.0/go.mod h1:88w4/PnZSazkGzz/w84VHpQafiU4EtqqlVdxWy+rNOA=
go.yaml.in/yaml/v3 v3.0.4 h1:tfq32ie2Jv2UxXFdLJdh3jXuOzWiL1fo0bu/FbuKpbc=
go.yaml.in/yaml/v3 v3.0.4/go.mod h1:DhzuOOF2ATzADvBadXxruRBLzYTpT36CKvDb3+aBEFg=
golang.org/x/net v0.48.0 h1:zyQRTTrjc33Lhh0fBgT/H3oZq9WuvRR5gPC70xpDiQU=
golang.org/x/net v0.48.0/go.mod h1:+ndRgGjkh8FGtu1w1FGbEC31if4VrNVMuKTgcAAnQRY=
golang.org/x/sys v0.39.0 h1:CvCKL8MeisomCi6qNZ+wbb0DN9E5AATixKsvNtMoMFk=
golang.org/x/sys v0.39.0/go.mod h1:OgkHotnGiDImocRcuBABYBEXf8A9a87e/uXjp9XT3ks=
golang.org/x/text v0.33.0 h1:B3njUFyqtHDUI5jMn1YIr5B0IE2U0qck04r6d4KPAxE=
golang.org/x/text v0.33.0/go.mod h1:LuMebE6+rBincTi9+xWTY8TztLzKHc/9C1uBCG27+q8=
gonum.org/v1/gonum v0.16.0 h1:5+ul4Swaf3ESvrOnidPp4GZbzf0mxVQpDCYUQE7OJfk=
gonum.org/v1/gonum v0.16.0/go.mod h1:fef3am4MQ93R2HHpKnLk4/Tbh/s0+wqD5nfa6Pnwy4E=
google.golang.org/genproto/googleapis/rpc v0.0.0-20260120221211-b8f7ae30c516 h1:sNrWoksmOyF5bvJUcnmbeAmQi8baNhqg5IWaI3llQqU=
google.golang.org/genproto/googleapis/rpc v0.0.0-20260120221211-b8f7ae30c516/go.mod h1:j9x/tPzZkyxcgEFkiKEEGxfvyumM01BEtsW8xzOahRQ=
google.golang.org/grpc v1.79.3 h1:sybAEdRIEtvcD68Gx7dmnwjZKlyfuc61Dyo9pGXXkKE=
google.golang.org/grpc v1.79.3/go.mod h1:KmT0Kjez+0dde/v2j9vzwoAScgEPx/Bw1CYChhHLrHQ=
google.golang.org/protobuf v1.36.11 h1:fV6ZwhNocDyBLK0dj+fg8ektcVegBBuEolpbTQyBNVE=
google.golang.org/protobuf v1.36.11/go.mod h1:HTf+CrKn2C3g5S8VImy6tdcUvCska2kB7j23XfzDpco=
gopkg.in/check.v1 v0.0.0-20161208181325-20d25e280405 h1:yhCVgyC4o1eVCa2tZl7eS0r+SDo693bJlVdllGtEeKM=
gopkg.in/check.v1 v0.0.0-20161208181325-20d25e280405/go.mod h1:Co6ibVJAznAaIkqp8huTwlJQCZ016jof/cbN4VW5Yz0=
```

## File: `itest/query/main.go`
```go
package main

import (
	"context"
	"fmt"
	"net/http"
	"os"
	"slices"
	"strings"
	"sync"
	"time"

	"connectrpc.com/connect"

	profilev1 "github.com/grafana/pyroscope/api/gen/proto/go/google/v1"
	querierv1 "github.com/grafana/pyroscope/api/gen/proto/go/querier/v1"

	"github.com/grafana/pyroscope/api/gen/proto/go/querier/v1/querierv1connect"
)

func main() {
	type result struct {
		target string
		err    error
	}
	targets := os.Args[1:]
	if len(targets) == 0 {
		targets = []string{
			"alpine-3.16-8",
			"alpine-3.16-11",
			"alpine-3.16-17",
			"alpine-3.17-8",
			"alpine-3.17-11",
			"alpine-3.17-17",
			"alpine-3.18-8",
			"alpine-3.18-11",
			"alpine-3.18-17",
			"alpine-3.18-21",
			"alpine-3.19-8",
			"alpine-3.19-11",
			"alpine-3.19-17",
			"alpine-3.19-21",
			"alpine-3.19-25",
			"ubuntu-18.04-8",
			"ubuntu-18.04-11",
			"ubuntu-18.04-17",
			"ubuntu-20.04-8",
			"ubuntu-20.04-11",
			"ubuntu-20.04-17",
			"ubuntu-20.04-21",
			"ubuntu-20.04-25",
			"ubuntu-22.04-8",
			"ubuntu-22.04-11",
			"ubuntu-22.04-17",
			"ubuntu-22.04-21",
			"ubuntu-22.04-25",
		}
	}
	url := "http://localhost:4040"
	qc := querierv1connect.NewQuerierServiceClient(
		http.DefaultClient,
		url,
	)
	wg := sync.WaitGroup{}
	ctx, _ := context.WithDeadline(context.Background(), time.Now().Add(time.Minute))
	results := make(chan result, len(targets))
	for _, target := range targets {
		wg.Add(1)
		go func(target string) {
			defer wg.Done()
			err := testTarget(ctx, qc, target)
			results <- result{target: target, err: err}
		}(target)
	}
	wg.Wait()
	close(results)

	failed := false
	for r := range results {
		if r.err != nil {
			fmt.Printf("[%s] %s\n", r.target, r.err.Error())
			failed = true
		} else {
			fmt.Printf("[%s] OK\n", r.target)
		}
	}
	if failed {
		os.Exit(1)
	}
}

func testTarget(ctx context.Context, qc querierv1connect.QuerierServiceClient, target string) error {
	//needle := "Fib$$Lambda_.run;Fib.lambda$appLogic$0;Fib.fib;Fib.fib;Fib.fib;Fib.fib;" // us this one when https://github.com/grafana/jfr-parser/pull/28/files lands pyroscope docker tag
	needle := "run;Fib.lambda$appLogic$0;Fib.fib;Fib.fib;Fib.fib;Fib.fib;"
	ticker := time.NewTicker(time.Second * 5)
	n := 0
	for {
		select {
		case <-ctx.Done():
			return fmt.Errorf("timed out waiting for target %s. tried %d times", target, n)
		case <-ticker.C:
			n += 1
			to := time.Now()
			from := to.Add(-time.Minute * 1)

			resp, err := qc.SelectMergeProfile(context.Background(), connect.NewRequest(&querierv1.SelectMergeProfileRequest{
				ProfileTypeID: "process_cpu:cpu:nanoseconds:cpu:nanoseconds",
				Start:         from.UnixMilli(),
				End:           to.UnixMilli(),
				LabelSelector: fmt.Sprintf("{service_name=\"%s\"}", target),
			}))
			if err != nil {
				fmt.Printf("[%s] %d %s\n", target, n, err.Error())
				continue
			}

			ss := stackCollapseProto(resp.Msg, false)
			if !strings.Contains(ss, needle) {
				fmt.Printf("[%s] %d not found yet\n%s\n", target, n, ss)
				continue
			}
			fmt.Printf("[%s] %d OK\n", target, n)
			return nil
		}
	}

}

func stackCollapseProto(p *profilev1.Profile, lineNumbers bool) string {
	allZeros := func(a []int64) bool {
		for _, v := range a {
			if v != 0 {
				return false
			}
		}
		return true
	}
	addValues := func(a, b []int64) {
		for i := range a {
			a[i] += b[i]
		}
	}

	type stack struct {
		funcs string
		value []int64
	}
	locMap := make(map[int64]*profilev1.Location)
	funcMap := make(map[int64]*profilev1.Function)
	for _, l := range p.Location {
		locMap[int64(l.Id)] = l
	}
	for _, f := range p.Function {
		funcMap[int64(f.Id)] = f
	}

	var ret []stack
	for _, s := range p.Sample {
		var funcs []string
		for i := range s.LocationId {
			locID := s.LocationId[len(s.LocationId)-1-i]
			loc := locMap[int64(locID)]
			for _, line := range loc.Line {
				f := funcMap[int64(line.FunctionId)]
				fname := p.StringTable[f.Name]
				if lineNumbers {
					fname = fmt.Sprintf("%s:%d", fname, line.Line)
				}
				funcs = append(funcs, fname)
			}
		}

		vv := make([]int64, len(s.Value))
		copy(vv, s.Value)
		ret = append(ret, stack{
			funcs: strings.Join(funcs, ";"),
			value: vv,
		})
	}
	slices.SortFunc(ret, func(i, j stack) int {
		return strings.Compare(i.funcs, j.funcs)
	})
	var unique []stack
	for _, s := range ret {
		if allZeros(s.value) {
			continue
		}
		if len(unique) == 0 {
			unique = append(unique, s)
			continue
		}

		if unique[len(unique)-1].funcs == s.funcs {
			addValues(unique[len(unique)-1].value, s.value)
			continue
		}
		unique = append(unique, s)

	}

	res := make([]string, 0, len(unique))
	for _, s := range unique {
		res = append(res, fmt.Sprintf("%s %v", s.funcs, s.value))
	}
	return strings.Join(res, "\n")
}
```

## File: `scripts/download-async-profiler.sh`
```bash
#!/bin/bash
set -euo pipefail

usage() {
    echo "Usage: $0 -v VERSION -r REPO_URL -d DIST_DIR"
    echo "  -v VERSION   async-profiler version (e.g., 4.3.0.0)"
    echo "  -r REPO_URL  GitHub repository URL (e.g., https://github.com/grafana/async-profiler)"
    echo "  -d DIST_DIR  Output directory for extracted files"
    exit 1
}

while getopts "v:r:d:" opt; do
    case $opt in
        v) VERSION="$OPTARG" ;;
        r) REPO="$OPTARG" ;;
        d) DIST_DIR="$OPTARG" ;;
        *) usage ;;
    esac
done

if [[ -z "${VERSION:-}" || -z "${REPO:-}" || -z "${DIST_DIR:-}" ]]; then
    usage
fi

rm -rf "$DIST_DIR"
mkdir -p "$DIST_DIR/lib"

# Download and extract linux-x64
echo "Downloading linux-x64..."
curl -sL "$REPO/releases/download/v$VERSION/async-profiler-$VERSION-linux-x64.tar.gz" | \
    tar -xzf - -C "$DIST_DIR" --strip-components=1
mv "$DIST_DIR/lib/libasyncProfiler.so" "$DIST_DIR/lib/libasyncProfiler-linux-x64.so"

# Download and extract linux-arm64
echo "Downloading linux-arm64..."
curl -sL "$REPO/releases/download/v$VERSION/async-profiler-$VERSION-linux-arm64.tar.gz" | \
    tar -xzf - -O --wildcards "*/lib/libasyncProfiler.so" > "$DIST_DIR/lib/libasyncProfiler-linux-arm64.so"

# Download and extract macos
echo "Downloading macos..."
TMP_ZIP=$(mktemp)
curl -sL "$REPO/releases/download/v$VERSION/async-profiler-$VERSION-macos.zip" -o "$TMP_ZIP"
unzip -o -j "$TMP_ZIP" "*/lib/libasyncProfiler.dylib" -d "$DIST_DIR/lib"
rm "$TMP_ZIP"
mv "$DIST_DIR/lib/libasyncProfiler.dylib" "$DIST_DIR/lib/libasyncProfiler-macos.so"

# Move async-profiler.jar to lib (if exists)
if [[ -f "$DIST_DIR/jar/async-profiler.jar" ]]; then
    mv "$DIST_DIR/jar/async-profiler.jar" "$DIST_DIR/lib/"
fi

# Compute SHA1 checksums
echo "Computing checksums..."
for platform in linux-x64 linux-arm64 macos; do
    sha1sum "$DIST_DIR/lib/libasyncProfiler-$platform.so" | cut -d' ' -f1 > "$DIST_DIR/lib/libasyncProfiler-$platform.so.sha1"
done

# Keep only lib directory
rm -rf "$DIST_DIR/bin" "$DIST_DIR/jar" "$DIST_DIR/include" "$DIST_DIR/licenses" \
       "$DIST_DIR"/*.html "$DIST_DIR/CHANGELOG.md" "$DIST_DIR/LICENSE" "$DIST_DIR/README.md" 2>/dev/null || true

echo "Done. Files in $DIST_DIR/lib:"
ls -la "$DIST_DIR/lib/"
```


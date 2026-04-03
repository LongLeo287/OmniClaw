---
id: github.com-andreschaffer-event-sourcing-cqrs-examp
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:30.198436
---

# KNOWLEDGE EXTRACT: github.com_andreschaffer_event-sourcing-cqrs-examples_456d7790
> **Extracted on:** 2026-04-01 12:50:40
> **Source:** D:/LongLeo/AI OS CORP/AI OS/core/security/QUARANTINE/KI-BATCH-20260331205007522055/github.com_andreschaffer_event-sourcing-cqrs-examples_456d7790

---

## File: `.gitignore`
```
# Intellij
.idea/
*.iml
*.iws

# Maven
target/
dependency-reduced-pom.xml
```

## File: `CODE_OF_CONDUCT.md`
```markdown
# Contributor Covenant Code of Conduct

## Our Pledge

In the interest of fostering an open and welcoming environment, we as contributors and maintainers pledge to making participation in our project and our community a harassment-free experience for everyone, regardless of age, body size, disability, ethnicity, gender identity and expression, level of experience, nationality, personal appearance, race, religion, or sexual identity and orientation.

## Our Standards

Examples of behavior that contributes to creating a positive environment include:

* Using welcoming and inclusive language
* Being respectful of differing viewpoints and experiences
* Gracefully accepting constructive criticism
* Focusing on what is best for the community
* Showing empathy towards other community members

Examples of unacceptable behavior by participants include:

* The use of sexualized language or imagery and unwelcome sexual attention or advances
* Trolling, insulting/derogatory comments, and personal or political attacks
* Public or private harassment
* Publishing others' private information, such as a physical or electronic address, without explicit permission
* Other conduct which could reasonably be considered inappropriate in a professional setting

## Our Responsibilities

Project maintainers are responsible for clarifying the standards of acceptable behavior and are expected to take appropriate and fair corrective action in response to any instances of unacceptable behavior.

Project maintainers have the right and responsibility to remove, edit, or reject comments, commits, code, wiki edits, issues, and other contributions that are not aligned to this Code of Conduct, or to ban temporarily or permanently any contributor for other behaviors that they deem inappropriate, threatening, offensive, or harmful.

## Scope

This Code of Conduct applies both within project spaces and in public spaces when an individual is representing the project or its community. Examples of representing a project or community include using an official project e-mail address, posting via an official social media account, or acting as an appointed representative at an online or offline event. Representation of a project may be further defined and clarified by project maintainers.

## Enforcement

Instances of abusive, harassing, or otherwise unacceptable behavior may be reported by contacting the project team at andre.schaffer@gmail.com or dan.eidmark@gmail.com. The project team will review and investigate all complaints, and will respond in a way that it deems appropriate to the circumstances. The project team is obligated to maintain confidentiality with regard to the reporter of an incident. Further details of specific enforcement policies may be posted separately.

Project maintainers who do not follow or enforce the Code of Conduct in good faith may face temporary or permanent repercussions as determined by other members of the project's leadership.

## Attribution

This Code of Conduct is adapted from the [Contributor Covenant][homepage], version 1.4, available at [http://contributor-covenant.org/version/1/4][version]

[homepage]: http://contributor-covenant.org
[version]: http://contributor-covenant.org/version/1/4/
```

## File: `CONTRIBUTING.md`
```markdown
# Contribution Guide
- Fork this project.
- Create a topic branch.
- Improve it with some commits.
- Ensure new code has tests for it and all tests pass.
- Push it to your forked project.
- Submit a Pull Request. 
- Pour yourself a glass of champagne and feel good about contributing to open source!

By participating in this project, you agree to abide by our [Code of Conduct](CODE_OF_CONDUCT.md).
```

## File: `LICENSE`
```
MIT License

Copyright (c) 2017 André Schaffer & Dan Eidmark

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

## File: `README.md`
```markdown
[![Build](https://github.com/andreschaffer/event-sourcing-cqrs-examples/actions/workflows/build.yml/badge.svg)](https://github.com/andreschaffer/event-sourcing-cqrs-examples/actions/workflows/build.yml)
[![Code Coverage](https://qlty.sh/gh/andreschaffer/projects/event-sourcing-cqrs-examples/coverage.svg)](https://qlty.sh/gh/andreschaffer/projects/event-sourcing-cqrs-examples)
[![Maintainability](https://qlty.sh/gh/andreschaffer/projects/event-sourcing-cqrs-examples/maintainability.svg)](https://qlty.sh/gh/andreschaffer/projects/event-sourcing-cqrs-examples)
[![Dependabot](https://img.shields.io/badge/Dependabot-enabled-blue?logo=dependabot)](https://docs.github.com/en/github/administering-a-repository/keeping-your-dependencies-updated-automatically)

# Event Sourcing and CQRS Examples
This project aims to provide examples of how to use Event Sourcing and CQRS applied to a minimalistic bank context.  

We assume the reader has basic knowledge of Event Sourcing and CQRS concepts.  
If you want to brush up on the subject we suggest reading:  
- [https://martinfowler.com/eaaDev/EventSourcing.html](https://martinfowler.com/eaaDev/EventSourcing.html)
- [https://martinfowler.com/bliki/CQRS.html](https://martinfowler.com/bliki/CQRS.html)

## Domain overview
In this minimalistic bank, a _client_ can _open_ one or more _accounts_.  
On each _account_, the _client_ can _deposit_ or _withdraw_ money.  
The history of an _account's transactions_ is available to the _client_ as well as a summary of the _client's accounts_.

## Design choices
### Architecture overview
      Event Store   Projections
        +----+        +----+
        |    |        |    |
        | DB |        | DB |
        +--+-+        +-+--+
          ^             ^
          |             |
    +------------+------------+
    |     |      |      |     |
    |     |    Events   |     |
    |     +------+----+ |     |
    |     |      |    | |     |
    |     +      |    v +     |
    |   Domain   |   Read     |
    |   Model    |   Model    |
    |            |            |
    +------------+------------+
    |                         |
    |           API           |
    |                         |
    +-------------------------+ 

#### Ports and Adapters
For the Domain Model, we chose the Ports and Adapters structure because we wanted to protect the domain logic from
all the technical concerns.

For more information about it read [here](http://www.dossier-andreas.net/software_architecture/ports_and_adapters.html).

#### Package by Feature
For the Read Models, we chose the Package by Feature structure because we would not benefit from isolating the layers
and instead we put all feature related parts close together. 

For more information about it read [here](http://www.javapractices.com/topic/TopicAction.do?Id=205).

### DDD and REST
There has been a myth of DDD and REST being incompatible due to DDD being all about behaviour
whereas REST is all about state.  
In this project we followed both techniques quite strictly and hope that the result shows that they can be well combined.  
Note: We did not include REST hypermedia controls as we believe it is a big subject in itself and didn't want to shift focus from Event Sourcing and CQRS.

### Event Sourcing and CQRS (finally!)
We have taken a pragmatic approach when combining Event Sourcing and CQRS. 
By the book, CQRS proposes a complete separation between the read/query and write/command sides,
but that's not what we have here.
The approach we've taken instead:
- The writes/commands are all on the domain model side and processed by aggregates;
- The reads/queries are both in the domain model side and in the read model side.
  - The queries in the domain model side are only allowed when the data we need is a single aggregate itself.
    The reason being that we can only query the event store by aggregate id
    and we can actually fulfill those queries by replaying that single aggregate events.
  - For any other kind of query, we don't want to compromise the domain model.
    Therefore, we create read models to fulfill those queries.
    They are basically projections, potentially built from different events and aggregates
    that can be queried by more appropriate fields. 
    
#### Events
Events are a thing from the past. It communicates a significant change that _happened_. 

##### Idempotency when replaying events
When replaying events, we don't want to execute any business logic because we can't change history. We only want to do assignments.  
A simple example is with a deposit event: instead of adding the deposited amount to the balance when replaying (business logic), we want 
the updated balance already available so that we can just assign it. This makes it possible to replay the event multiple times with the same outcome.

##### Ordering of events
In a distributed world, event timestamps are unreliable for ordering - machines have their own clocks.  
Instead we can make the ordering explicit with an event version.
In this project we use event versioning in two ways:
- In the write/command side, we use it for protecting ourselves from race conditions via optimistic locking;
- In the read/query side, we use it for commutative reasons, meaning events can come out of order and we can still handle them properly.

If you are interested in this topic, we also recommend reading about [Lamport timestamps](https://en.wikipedia.org/wiki/Lamport_timestamps) and [Vector clocks](https://en.wikipedia.org/wiki/Vector_clock) as alternatives.

## Trying it out
### Requirements
- Java 14
- Maven

### Building the application
` mvn clean verify `

### Starting the application
` java -jar target/bank-service-1.0-SNAPSHOT.jar server src/environments/development.yml `

### Examples of use
#### Create a client
` curl -v -X POST -H "Content-Type: application/json" -d '{"name":"Jane Doe", "email":"jane.doe@example.com"}' http://localhost:8080/clients `

Check the created client in the response's 'Location' header.

#### Create an account for the client
` curl -v -X POST -H "Content-Type: application/json" -d '{"clientId":"{CLIENT_ID}"}' http://localhost:8080/accounts `

Check the created account in the response's 'Location' header.

#### Make a deposit to the account
` curl -v -X POST -H "Content-Type: application/json" -d '{"amount":1000000}' http://localhost:8080/accounts/{ACCOUNT_ID}/deposits `

#### Check that you created a millionaire!
` curl -v http://localhost:8080/accounts/{ACCOUNT_ID} `

#### More operations
Go ahead and check the code! :)

# Contributing
If you would like to help making this project better, see the [CONTRIBUTING.md](CONTRIBUTING.md).  

# Maintainers
Send any other comments, flowers and suggestions to [André Schaffer](https://github.com/andreschaffer) and [Dan Eidmark](https://github.com/daneidmark).

# License
This project is distributed under the [MIT License](LICENSE).
```

## File: `pom.xml`
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
  <modelVersion>4.0.0</modelVersion>

  <groupId>bank-service</groupId>
  <artifactId>bank-service</artifactId>
  <version>1.0-SNAPSHOT</version>

  <properties>
    <java.version>19</java.version>
    <dropwizard.version>4.0.10</dropwizard.version>
    <jersey.version>3.1.11</jersey.version>
    <jakarta.version>2.1.1</jakarta.version>
    <junit.version>6.0.3</junit.version>
    <error_prone.version>2.42.0</error_prone.version>
    <mvn-test-plugins.version>3.5.5</mvn-test-plugins.version>
    <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    <project.reporting.outputEncoding>UTF-8</project.reporting.outputEncoding>
    <argLine>--add-opens java.base/java.math=ALL-UNNAMED
             --add-opens java.base/java.time=ALL-UNNAMED</argLine>
  </properties>

  <dependencies>
    <dependency>
      <groupId>io.dropwizard</groupId>
      <artifactId>dropwizard-core</artifactId>
      <version>${dropwizard.version}</version>
    </dependency>

    <dependency>
      <groupId>org.glassfish.jersey.ext</groupId>
      <artifactId>jersey-declarative-linking</artifactId>
      <version>${jersey.version}</version>
    </dependency>

    <dependency>
      <groupId>commons-validator</groupId>
      <artifactId>commons-validator</artifactId>
      <version>1.10.1</version>
    </dependency>

    <dependency>
      <groupId>org.apache.commons</groupId>
      <artifactId>commons-lang3</artifactId>
      <version>3.20.0</version>
    </dependency>

    <dependency>
      <groupId>com.google.guava</groupId>
      <artifactId>guava</artifactId>
      <version>33.5.0-jre</version>
    </dependency>

    <dependency>
      <groupId>org.junit.jupiter</groupId>
      <artifactId>junit-jupiter</artifactId>
      <version>${junit.version}</version>
      <scope>test</scope>
    </dependency>

    <dependency>
      <groupId>org.hamcrest</groupId>
      <artifactId>hamcrest</artifactId>
      <version>3.0</version>
      <scope>test</scope>
    </dependency>

    <dependency>
      <groupId>org.mockito</groupId>
      <artifactId>mockito-core</artifactId>
      <version>5.23.0</version>
      <scope>test</scope>
    </dependency>

    <dependency>
      <groupId>io.dropwizard</groupId>
      <artifactId>dropwizard-testing</artifactId>
      <version>${dropwizard.version}</version>
      <scope>test</scope>
      <exclusions>
        <exclusion>
          <groupId>org.hibernate</groupId>
          <artifactId>hibernate-core</artifactId>
        </exclusion>
      </exclusions>
    </dependency>

    <dependency>
      <groupId>io.dropwizard</groupId>
      <artifactId>dropwizard-client</artifactId>
      <version>${dropwizard.version}</version>
      <scope>test</scope>
    </dependency>
  </dependencies>

  <dependencyManagement>
    <dependencies>
      <dependency>
        <groupId>org.checkerframework</groupId>
        <artifactId>checker-qual</artifactId>
        <version>3.54.0</version>
      </dependency>

      <dependency>
        <groupId>org.glassfish.jersey.core</groupId>
        <artifactId>jersey-server</artifactId>
        <version>${jersey.version}</version>
      </dependency>

      <dependency>
        <groupId>org.glassfish.jersey.core</groupId>
        <artifactId>jersey-client</artifactId>
        <version>${jersey.version}</version>
      </dependency>

      <dependency>
        <groupId>org.glassfish.jersey.core</groupId>
        <artifactId>jersey-common</artifactId>
        <version>${jersey.version}</version>
      </dependency>

      <dependency>
        <groupId>jakarta.ws.rs</groupId>
        <artifactId>jakarta.ws.rs-api</artifactId>
        <version>4.0.0</version>
      </dependency>

      <dependency>
        <groupId>jakarta.annotation</groupId>
        <artifactId>jakarta.annotation-api</artifactId>
        <version>${jakarta.version}</version>
      </dependency>

      <dependency>
        <groupId>jakarta.activation</groupId>
        <artifactId>jakarta.activation-api</artifactId>
        <version>${jakarta.version}</version>
      </dependency>

      <dependency>
        <groupId>com.google.errorprone</groupId>
        <artifactId>error_prone_annotations</artifactId>
        <version>${error_prone.version}</version>
      </dependency>
    </dependencies>
  </dependencyManagement>

  <build>
    <plugins>
      <plugin>
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-compiler-plugin</artifactId>
        <version>3.15.0</version>
        <configuration>
          <release>${java.version}</release>
          <fork>true</fork>
          <showWarnings>true</showWarnings>
          <compilerArgs>
            <arg>-XDcompilePolicy=simple</arg>
            <arg>-Xplugin:ErrorProne</arg>
            <arg>--should-stop=ifError=FLOW</arg>
            <arg>-J--add-exports=jdk.compiler/com.sun.tools.javac.api=ALL-UNNAMED</arg>
            <arg>-J--add-exports=jdk.compiler/com.sun.tools.javac.file=ALL-UNNAMED</arg>
            <arg>-J--add-exports=jdk.compiler/com.sun.tools.javac.main=ALL-UNNAMED</arg>
            <arg>-J--add-exports=jdk.compiler/com.sun.tools.javac.model=ALL-UNNAMED</arg>
            <arg>-J--add-exports=jdk.compiler/com.sun.tools.javac.parser=ALL-UNNAMED</arg>
            <arg>-J--add-exports=jdk.compiler/com.sun.tools.javac.processing=ALL-UNNAMED</arg>
            <arg>-J--add-exports=jdk.compiler/com.sun.tools.javac.tree=ALL-UNNAMED</arg>
            <arg>-J--add-exports=jdk.compiler/com.sun.tools.javac.util=ALL-UNNAMED</arg>
            <arg>-J--add-opens=jdk.compiler/com.sun.tools.javac.code=ALL-UNNAMED</arg>
            <arg>-J--add-opens=jdk.compiler/com.sun.tools.javac.comp=ALL-UNNAMED</arg>
            <arg>-J--add-opens=jdk.compiler/com.sun.tools.javac.api=ALL-UNNAMED</arg>
          </compilerArgs>
          <annotationProcessorPaths>
            <path>
              <groupId>com.google.errorprone</groupId>
              <artifactId>error_prone_core</artifactId>
              <version>${error_prone.version}</version>
            </path>
          </annotationProcessorPaths>
        </configuration>
      </plugin>

      <plugin>
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-checkstyle-plugin</artifactId>
        <version>3.6.0</version>
        <configuration>
          <inputEncoding>UTF-8</inputEncoding>
          <outputEncoding>UTF-8</outputEncoding>
          <consoleOutput>true</consoleOutput>
          <failsOnError>true</failsOnError>
          <violationSeverity>warning</violationSeverity>
          <includeTestSourceDirectory>true</includeTestSourceDirectory>
          <configLocation>
            ${project.basedir}/src/main/resources/checkstyle/google_checks.xml
          </configLocation>
          <suppressionsLocation>
            ${project.basedir}/src/main/resources/checkstyle/suppressions.xml
          </suppressionsLocation>
        </configuration>
        <executions>
          <execution>
            <id>validate</id>
            <phase>validate</phase>
            <goals>
              <goal>check</goal>
            </goals>
          </execution>
        </executions>
      </plugin>

      <plugin>
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-enforcer-plugin</artifactId>
        <version>3.6.2</version>
        <executions>
          <execution>
            <id>enforce</id>
            <phase>validate</phase>
            <goals>
              <goal>enforce</goal>
            </goals>
            <configuration>
              <rules>
                <banDuplicatePomDependencyVersions/>
                <requireUpperBoundDeps/>
              </rules>
            </configuration>
          </execution>
        </executions>
      </plugin>

      <plugin>
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-dependency-plugin</artifactId>
        <version>3.10.0</version>
        <configuration>
          <outputXML>true</outputXML>
          <ignoredUsedUndeclaredDependencies>
            <!-- part of dropwizard core -->
            <ignoredUsedUndeclaredDependency>io.dropwizard:*</ignoredUsedUndeclaredDependency>
            <ignoredUsedUndeclaredDependency>
              com.fasterxml.jackson.core:*
            </ignoredUsedUndeclaredDependency>
            <ignoredUsedUndeclaredDependency>jakarta.validation::*</ignoredUsedUndeclaredDependency>
            <ignoredUsedUndeclaredDependency>jakarta.ws.rs:*</ignoredUsedUndeclaredDependency>
            <ignoredUsedUndeclaredDependency>
              org.glassfish.jersey.core:*
            </ignoredUsedUndeclaredDependency>
          </ignoredUsedUndeclaredDependencies>
        </configuration>
        <executions>
          <execution>
            <id>analyze</id>
            <phase>test-compile</phase>
            <goals>
              <goal>analyze-only</goal>
            </goals>
          </execution>
        </executions>
      </plugin>

      <plugin>
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-shade-plugin</artifactId>
        <version>3.6.2</version>
        <configuration>
          <createDependencyReducedPom>true</createDependencyReducedPom>
          <filters>
            <filter>
              <artifact>*:*</artifact>
              <excludes>
                <exclude>META-INF/*.SF</exclude>
                <exclude>META-INF/*.DSA</exclude>
                <exclude>META-INF/*.RSA</exclude>
              </excludes>
            </filter>
          </filters>
        </configuration>
        <executions>
          <execution>
            <phase>package</phase>
            <goals>
              <goal>shade</goal>
            </goals>
            <configuration>
              <transformers>
                <transformer
                  implementation="org.apache.maven.plugins.shade.resource.ServicesResourceTransformer"/>
                <transformer
                  implementation="org.apache.maven.plugins.shade.resource.ManifestResourceTransformer">
                  <mainClass>bankservice.bootstrap.BankServiceApplication</mainClass>
                </transformer>
              </transformers>
            </configuration>
          </execution>
        </executions>
      </plugin>

      <plugin>
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-surefire-plugin</artifactId>
        <version>${mvn-test-plugins.version}</version>
      </plugin>

      <plugin>
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-failsafe-plugin</artifactId>
        <version>${mvn-test-plugins.version}</version>
        <executions>
          <execution>
            <goals>
              <goal>integration-test</goal>
              <goal>verify</goal>
            </goals>
          </execution>
        </executions>
      </plugin>
    </plugins>
  </build>

  <profiles>
    <profile>
      <id>code-coverage</id>
      <build>
        <plugins>
          <plugin>
            <groupId>org.jacoco</groupId>
            <artifactId>jacoco-maven-plugin</artifactId>
            <version>0.8.14</version>
            <executions>
              <execution>
                <id>prepare-agent</id>
                <goals>
                  <goal>prepare-agent</goal>
                </goals>
              </execution>
              <execution>
                <id>prepare-agent-integration</id>
                <goals>
                  <goal>prepare-agent-integration</goal>
                </goals>
              </execution>
              <execution>
                <id>jacoco-site</id>
                <goals>
                  <goal>report</goal>
                </goals>
              </execution>
              <execution>
                <id>jacoco-site-integration</id>
                <goals>
                  <goal>report-integration</goal>
                </goals>
              </execution>
            </executions>
          </plugin>
        </plugins>
      </build>
    </profile>
  </profiles>

</project>
```

## File: `src/environments/development.yml`
```yaml
server:
  applicationConnectors:
    - type: http
      port: 8080
  adminConnectors:
    - type: http
      port: 8081
```

## File: `src/main/java/bankservice/bootstrap/BankServiceApplication.java`
```java
package bankservice.bootstrap;

import static java.util.concurrent.Executors.newSingleThreadExecutor;
import static java.util.logging.Level.INFO;
import static java.util.logging.Logger.getLogger;
import static org.glassfish.jersey.logging.LoggingFeature.DEFAULT_LOGGER_NAME;
import static org.glassfish.jersey.logging.LoggingFeature.Verbosity.PAYLOAD_ANY;

import bankservice.domain.model.EventStore;
import bankservice.port.incoming.adapter.resources.OptimisticLockingExceptionMapper;
import bankservice.port.incoming.adapter.resources.accounts.AccountNotFoundExceptionMapper;
import bankservice.port.incoming.adapter.resources.accounts.AccountResource;
import bankservice.port.incoming.adapter.resources.accounts.AccountsResource;
import bankservice.port.incoming.adapter.resources.accounts.deposits.DepositsResource;
import bankservice.port.incoming.adapter.resources.accounts.withdrawals.WithdrawalsResource;
import bankservice.port.incoming.adapter.resources.clients.ClientResource;
import bankservice.port.incoming.adapter.resources.clients.ClientsResource;
import bankservice.port.outgoing.adapter.eventstore.InMemoryEventStore;
import bankservice.projection.accounttransactions.AccountTransactionsResource;
import bankservice.projection.accounttransactions.InMemoryTransactionsRepository;
import bankservice.projection.accounttransactions.TransactionsListener;
import bankservice.projection.accounttransactions.TransactionsRepository;
import bankservice.projection.clientaccounts.AccountsListener;
import bankservice.projection.clientaccounts.AccountsRepository;
import bankservice.projection.clientaccounts.ClientAccountsResource;
import bankservice.projection.clientaccounts.InMemoryAccountsRepository;
import bankservice.service.account.AccountService;
import bankservice.service.client.ClientService;
import com.google.common.eventbus.AsyncEventBus;
import com.google.common.eventbus.EventBus;
import io.dropwizard.core.Application;
import io.dropwizard.core.Configuration;
import io.dropwizard.core.setup.Environment;
import org.glassfish.jersey.linking.DeclarativeLinkingFeature;
import org.glassfish.jersey.logging.LoggingFeature;

public class BankServiceApplication extends Application<Configuration> {

  public static void main(String[] args) throws Exception {
    new BankServiceApplication().run(args);
  }

  @Override
  public void run(Configuration configuration, Environment environment) throws Exception {
    registerFilters(environment);
    registerExceptionMappers(environment);
    registerHypermediaSupport(environment);
    registerResources(environment);
  }

  private void registerFilters(Environment environment) {
    environment.jersey()
        .register(new LoggingFeature(getLogger(DEFAULT_LOGGER_NAME), INFO, PAYLOAD_ANY, 1024));
  }

  private void registerExceptionMappers(Environment environment) {
    environment.jersey().register(AccountNotFoundExceptionMapper.class);
    environment.jersey().register(OptimisticLockingExceptionMapper.class);
  }

  private void registerHypermediaSupport(Environment environment) {
    environment.jersey().getResourceConfig().register(DeclarativeLinkingFeature.class);
  }

  private void registerResources(Environment environment) {
    EventStore eventStore = new InMemoryEventStore();
    EventBus eventBus = new AsyncEventBus(newSingleThreadExecutor());

    // domain model
    AccountService accountService = new AccountService(eventStore, eventBus);
    environment.jersey().register(new AccountsResource(accountService));
    environment.jersey().register(new AccountResource(accountService));
    environment.jersey().register(new DepositsResource(accountService));
    environment.jersey().register(new WithdrawalsResource(accountService));

    ClientService clientService = new ClientService(eventStore);
    environment.jersey().register(new ClientsResource(clientService));
    environment.jersey().register(new ClientResource(clientService));

    // read model
    TransactionsRepository transactionsRepository = new InMemoryTransactionsRepository();
    eventBus.register(new TransactionsListener(transactionsRepository));
    environment.jersey().register(new AccountTransactionsResource(transactionsRepository));

    AccountsRepository accountsRepository = new InMemoryAccountsRepository();
    eventBus.register(new AccountsListener(accountsRepository));
    environment.jersey().register(new ClientAccountsResource(accountsRepository));
  }
}
```

## File: `src/main/java/bankservice/domain/model/Aggregate.java`
```java
package bankservice.domain.model;

import static com.google.common.base.Preconditions.checkArgument;
import static com.google.common.base.Preconditions.checkNotNull;
import static java.lang.String.format;
import static java.util.Collections.emptyList;

import com.google.common.base.Throwables;
import com.google.common.collect.ImmutableList;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import java.util.ArrayList;
import java.util.List;
import java.util.UUID;

public abstract class Aggregate {

  private UUID id;
  private int baseVersion;
  private List<Event> newEvents;

  protected Aggregate(UUID id) {
    this(id, emptyList());
  }

  protected Aggregate(UUID id, List<Event> eventStream) {
    checkNotNull(id);
    checkNotNull(eventStream);
    this.id = id;
    eventStream.forEach(e -> {
      apply(e);
      this.baseVersion = e.getVersion();
    });
    this.newEvents = new ArrayList<>();
  }

  protected void applyNewEvent(Event event) {
    checkArgument(event.getVersion() == getNextVersion(),
        "New event version '%s' does not match expected next version '%s'",
        event.getVersion(), getNextVersion());
    apply(event);
    newEvents.add(event);
  }

  private void apply(Event event) {
    try {
      Method method = this.getClass().getDeclaredMethod("apply", event.getClass());
      method.setAccessible(true);
      method.invoke(this, event);
    } catch (InvocationTargetException e) {
      Throwables.propagate(e.getCause());
    } catch (NoSuchMethodException | IllegalAccessException e) {
      throw new UnsupportedOperationException(
          format("Aggregate '%s' doesn't apply event type '%s'", this.getClass(), event.getClass()),
          e);
    }
  }

  public UUID getId() {
    return id;
  }

  public int getBaseVersion() {
    return baseVersion;
  }

  public List<Event> getNewEvents() {
    return ImmutableList.copyOf(newEvents);
  }

  protected int getNextVersion() {
    return baseVersion + newEvents.size() + 1;
  }
}
```

## File: `src/main/java/bankservice/domain/model/Event.java`
```java
package bankservice.domain.model;

import static com.google.common.base.Preconditions.checkNotNull;

import java.time.ZonedDateTime;
import java.util.UUID;

public abstract class Event {

  private final UUID aggregateId;
  private final ZonedDateTime timestamp;
  private final int version;

  protected Event(UUID aggregateId, ZonedDateTime timestamp, int version) {
    this.aggregateId = checkNotNull(aggregateId);
    this.timestamp = checkNotNull(timestamp);
    this.version = version;
  }

  public UUID getAggregateId() {
    return aggregateId;
  }

  public ZonedDateTime getTimestamp() {
    return this.timestamp;
  }

  public int getVersion() {
    return version;
  }
}
```

## File: `src/main/java/bankservice/domain/model/EventStore.java`
```java
package bankservice.domain.model;

import java.util.List;
import java.util.UUID;

public interface EventStore {

  void store(UUID aggregateId, List<Event> newEvents, int baseVersion)
      throws OptimisticLockingException;

  List<Event> load(UUID aggregateId);

}
```

## File: `src/main/java/bankservice/domain/model/OptimisticLockingException.java`
```java
package bankservice.domain.model;

public class OptimisticLockingException extends RuntimeException {

  public OptimisticLockingException(String message) {
    super(message);
  }
}
```

## File: `src/main/java/bankservice/domain/model/Specification.java`
```java
package bankservice.domain.model;

public interface Specification<T> {

  boolean isSatisfiedBy(T value);

}
```

## File: `src/main/java/bankservice/domain/model/ValueObject.java`
```java
package bankservice.domain.model;

import org.apache.commons.lang3.builder.EqualsBuilder;
import org.apache.commons.lang3.builder.HashCodeBuilder;
import org.apache.commons.lang3.builder.ToStringBuilder;
import org.apache.commons.lang3.builder.ToStringStyle;

public abstract class ValueObject {

  @Override
  public boolean equals(Object o) {
    return EqualsBuilder.reflectionEquals(this, o);
  }

  @Override
  public int hashCode() {
    return HashCodeBuilder.reflectionHashCode(this);
  }

  @Override
  public String toString() {
    return ToStringBuilder.reflectionToString(this, ToStringStyle.SHORT_PREFIX_STYLE);
  }
}
```

## File: `src/main/java/bankservice/domain/model/account/Account.java`
```java
package bankservice.domain.model.account;

import static java.math.BigDecimal.ZERO;
import static java.time.ZoneOffset.UTC;
import static java.time.ZonedDateTime.now;

import bankservice.domain.model.Aggregate;
import bankservice.domain.model.Event;
import java.math.BigDecimal;
import java.util.List;
import java.util.UUID;

public class Account extends Aggregate {

  private BigDecimal balance;
  private UUID clientId;

  public Account(UUID id, UUID clientId) {
    super(id);
    AccountOpenedEvent accountOpenedEvent = new AccountOpenedEvent(
        id, now(UTC), getNextVersion(), clientId, ZERO);
    applyNewEvent(accountOpenedEvent);
  }

  public Account(UUID id, List<Event> eventStream) {
    super(id, eventStream);
  }

  public void deposit(BigDecimal amount) {
    BigDecimal newBalance = balance.add(amount);
    AccountDepositedEvent accountDepositedEvent = new AccountDepositedEvent(
        getId(), now(UTC), getNextVersion(), amount, newBalance);
    applyNewEvent(accountDepositedEvent);
  }

  public void withdraw(BigDecimal amount) {
    BigDecimal newBalance = balance.subtract(amount);
    if (newBalance.signum() == -1) {
      throw new NonSufficientFundsException(getId(), balance, amount);
    }
    AccountWithdrawnEvent accountWithdrawnEvent = new AccountWithdrawnEvent(
        getId(), now(UTC), getNextVersion(), amount, newBalance);
    applyNewEvent(accountWithdrawnEvent);
  }

  @SuppressWarnings("unused")
  private void apply(AccountOpenedEvent event) {
    clientId = event.getClientId();
    balance = event.getBalance();
  }

  @SuppressWarnings("unused")
  private void apply(AccountDepositedEvent event) {
    balance = event.getBalance();
  }

  @SuppressWarnings("unused")
  private void apply(AccountWithdrawnEvent event) {
    balance = event.getBalance();
  }

  public BigDecimal getBalance() {
    return balance;
  }

  public UUID getClientId() {
    return clientId;
  }
}
```

## File: `src/main/java/bankservice/domain/model/account/AccountDepositedEvent.java`
```java
package bankservice.domain.model.account;

import static com.google.common.base.Preconditions.checkNotNull;

import bankservice.domain.model.Event;
import java.math.BigDecimal;
import java.time.ZonedDateTime;
import java.util.UUID;

public class AccountDepositedEvent extends Event {

  private final BigDecimal amount;
  private final BigDecimal balance;

  public AccountDepositedEvent(UUID aggregateId, ZonedDateTime timestamp, int version,
      BigDecimal amount, BigDecimal balance) {
    super(aggregateId, timestamp, version);
    this.amount = checkNotNull(amount);
    this.balance = checkNotNull(balance);
  }

  public BigDecimal getAmount() {
    return amount;
  }

  public BigDecimal getBalance() {
    return balance;
  }
}
```

## File: `src/main/java/bankservice/domain/model/account/AccountOpenedEvent.java`
```java
package bankservice.domain.model.account;

import static com.google.common.base.Preconditions.checkNotNull;

import bankservice.domain.model.Event;
import java.math.BigDecimal;
import java.time.ZonedDateTime;
import java.util.UUID;

public class AccountOpenedEvent extends Event {

  private final String clientId;
  private final BigDecimal balance;

  public AccountOpenedEvent(UUID aggregateId, ZonedDateTime timestamp, int version, UUID clientId,
      BigDecimal balance) {
    super(aggregateId, timestamp, version);
    this.clientId = checkNotNull(clientId).toString();
    this.balance = checkNotNull(balance);
  }

  public UUID getClientId() {
    return UUID.fromString(clientId);
  }

  public BigDecimal getBalance() {
    return balance;
  }
}
```

## File: `src/main/java/bankservice/domain/model/account/AccountWithdrawnEvent.java`
```java
package bankservice.domain.model.account;

import static com.google.common.base.Preconditions.checkNotNull;

import bankservice.domain.model.Event;
import java.math.BigDecimal;
import java.time.ZonedDateTime;
import java.util.UUID;

public class AccountWithdrawnEvent extends Event {

  private final BigDecimal amount;
  private final BigDecimal balance;

  public AccountWithdrawnEvent(UUID aggregateId, ZonedDateTime timestamp, int version,
      BigDecimal amount, BigDecimal balance) {
    super(aggregateId, timestamp, version);
    this.amount = checkNotNull(amount);
    this.balance = checkNotNull(balance);
  }

  public BigDecimal getAmount() {
    return amount;
  }

  public BigDecimal getBalance() {
    return balance;
  }
}
```

## File: `src/main/java/bankservice/domain/model/account/NonSufficientFundsException.java`
```java
package bankservice.domain.model.account;

import static java.lang.String.format;

import java.math.BigDecimal;
import java.util.UUID;

public class NonSufficientFundsException extends RuntimeException {

  public NonSufficientFundsException(UUID accountId, BigDecimal balance, BigDecimal amount) {
    super(format("Withdrawal of '%s' failed as there is only '%s' in account '%s'", amount, balance,
        accountId));
  }
}
```

## File: `src/main/java/bankservice/domain/model/client/Client.java`
```java
package bankservice.domain.model.client;

import static com.google.common.base.Preconditions.checkArgument;
import static com.google.common.base.Preconditions.checkNotNull;
import static java.time.ZoneOffset.UTC;
import static java.time.ZonedDateTime.now;
import static org.apache.commons.lang3.StringUtils.isNotBlank;

import bankservice.domain.model.Aggregate;
import bankservice.domain.model.Event;
import java.util.List;
import java.util.UUID;

public class Client extends Aggregate {

  private String name;
  private Email email;

  public Client(UUID id, String name, Email email) {
    super(id);
    validateName(name);
    validateEmail(email);
    ClientEnrolledEvent clientEnrolledEvent = new ClientEnrolledEvent(
        id, now(UTC), getNextVersion(), name, email);
    applyNewEvent(clientEnrolledEvent);
  }

  public Client(UUID id, List<Event> eventStream) {
    super(id, eventStream);
  }

  public void update(String name, Email email) {
    ClientUpdatedEvent clientUpdatedEvent = new ClientUpdatedEvent(
        getId(), now(UTC), getNextVersion(), name, email);
    applyNewEvent(clientUpdatedEvent);
  }

  @SuppressWarnings("unused")
  public void apply(ClientEnrolledEvent event) {
    this.name = event.getName();
    this.email = event.getEmail();
  }

  @SuppressWarnings("unused")
  private void apply(ClientUpdatedEvent event) {
    this.name = event.getName();
    this.email = event.getEmail();
  }

  public String getName() {
    return name;
  }

  public Email getEmail() {
    return email;
  }

  private void validateName(String name) {
    checkArgument(isNotBlank(name));
  }

  private void validateEmail(Email email) {
    checkNotNull(email);
  }
}
```

## File: `src/main/java/bankservice/domain/model/client/ClientEnrolledEvent.java`
```java
package bankservice.domain.model.client;

import static com.google.common.base.Preconditions.checkNotNull;

import bankservice.domain.model.Event;
import java.time.ZonedDateTime;
import java.util.UUID;

public class ClientEnrolledEvent extends Event {

  private final String name;
  private final String email;

  public ClientEnrolledEvent(UUID aggregateId, ZonedDateTime timestamp, int version, String name,
      Email email) {
    super(aggregateId, timestamp, version);
    this.name = checkNotNull(name);
    this.email = checkNotNull(email).getValue();
  }

  public String getName() {
    return name;
  }

  public Email getEmail() {
    return new Email(email);
  }
}
```

## File: `src/main/java/bankservice/domain/model/client/ClientUpdatedEvent.java`
```java
package bankservice.domain.model.client;

import static com.google.common.base.Preconditions.checkNotNull;

import bankservice.domain.model.Event;
import java.time.ZonedDateTime;
import java.util.UUID;

public class ClientUpdatedEvent extends Event {

  private final String name;
  private final String email;

  public ClientUpdatedEvent(UUID aggregateId, ZonedDateTime timestamp, int version, String name,
      Email email) {
    super(aggregateId, timestamp, version);
    this.name = checkNotNull(name);
    this.email = checkNotNull(email).getValue();
  }

  public String getName() {
    return name;
  }

  public Email getEmail() {
    return new Email(email);
  }
}
```

## File: `src/main/java/bankservice/domain/model/client/Email.java`
```java
package bankservice.domain.model.client;

import static com.google.common.base.Preconditions.checkArgument;

import bankservice.domain.model.Specification;
import bankservice.domain.model.ValueObject;
import org.apache.commons.validator.routines.EmailValidator;

public class Email extends ValueObject {

  private final String value;

  public Email(String value) {
    checkArgument(new EmailSpecification().isSatisfiedBy(value));
    this.value = value;
  }

  public String getValue() {
    return value;
  }

  public static class EmailSpecification implements Specification<String> {

    @Override
    public boolean isSatisfiedBy(String value) {
      return EmailValidator.getInstance().isValid(value);
    }
  }
}
```

## File: `src/main/java/bankservice/port/incoming/adapter/resources/OptimisticLockingExceptionMapper.java`
```java
package bankservice.port.incoming.adapter.resources;


import static jakarta.ws.rs.core.Response.Status.CONFLICT;

import bankservice.domain.model.OptimisticLockingException;
import jakarta.ws.rs.core.Response;
import jakarta.ws.rs.ext.ExceptionMapper;
import jakarta.ws.rs.ext.Provider;

@Provider
public class OptimisticLockingExceptionMapper implements
    ExceptionMapper<OptimisticLockingException> {

  @Override
  public Response toResponse(OptimisticLockingException exception) {
    return Response.status(CONFLICT).build();
  }
}
```

## File: `src/main/java/bankservice/port/incoming/adapter/resources/accounts/AccountDto.java`
```java
package bankservice.port.incoming.adapter.resources.accounts;

import static com.fasterxml.jackson.annotation.JsonProperty.Access.READ_ONLY;
import static java.math.BigDecimal.ROUND_HALF_UP;

import com.fasterxml.jackson.annotation.JsonProperty;
import java.math.BigDecimal;
import java.util.UUID;

public class AccountDto {

  @JsonProperty(access = READ_ONLY)
  private UUID id;

  @JsonProperty(access = READ_ONLY)
  private BigDecimal balance;

  private UUID clientId;

  @SuppressWarnings("unused")
  public UUID getId() {
    return id;
  }

  @SuppressWarnings("unused")
  public void setId(UUID id) {
    this.id = id;
  }

  @SuppressWarnings("unused")
  public BigDecimal getBalance() {
    return balance;
  }

  @SuppressWarnings("unused")
  public void setBalance(BigDecimal balance) {
    this.balance = balance.setScale(2, ROUND_HALF_UP);
  }

  @SuppressWarnings("unused")
  public UUID getClientId() {
    return clientId;
  }

  @SuppressWarnings("unused")
  public void setClientId(UUID clientId) {
    this.clientId = clientId;
  }
}
```

## File: `src/main/java/bankservice/port/incoming/adapter/resources/accounts/AccountNotFoundExceptionMapper.java`
```java
package bankservice.port.incoming.adapter.resources.accounts;


import static jakarta.ws.rs.core.Response.Status.NOT_FOUND;

import bankservice.service.account.AccountNotFoundException;
import jakarta.ws.rs.core.Response;
import jakarta.ws.rs.ext.ExceptionMapper;
import jakarta.ws.rs.ext.Provider;

@Provider
public class AccountNotFoundExceptionMapper implements ExceptionMapper<AccountNotFoundException> {

  @Override
  public Response toResponse(AccountNotFoundException exception) {
    return Response.status(NOT_FOUND).build();
  }
}
```

## File: `src/main/java/bankservice/port/incoming/adapter/resources/accounts/AccountResource.java`
```java
package bankservice.port.incoming.adapter.resources.accounts;

import static com.google.common.base.Preconditions.checkNotNull;
import static jakarta.ws.rs.core.MediaType.APPLICATION_JSON;
import static jakarta.ws.rs.core.Response.Status.NOT_FOUND;

import bankservice.domain.model.account.Account;
import bankservice.service.account.AccountService;
import io.dropwizard.jersey.params.UUIDParam;
import jakarta.ws.rs.Consumes;
import jakarta.ws.rs.GET;
import jakarta.ws.rs.Path;
import jakarta.ws.rs.PathParam;
import jakarta.ws.rs.Produces;
import jakarta.ws.rs.core.Response;
import java.util.Optional;

@Consumes(APPLICATION_JSON)
@Produces(APPLICATION_JSON)
@Path("/accounts/{id}")
public class AccountResource {

  private final AccountService accountService;

  public AccountResource(AccountService accountService) {
    this.accountService = checkNotNull(accountService);
  }

  @GET
  public Response get(@PathParam("id") UUIDParam accountId) {
    Optional<Account> possibleAccount = accountService.loadAccount(accountId.get());
    if (!possibleAccount.isPresent()) {
      return Response.status(NOT_FOUND).build();
    }
    AccountDto accountDto = toDto(possibleAccount.get());
    return Response.ok(accountDto).build();
  }

  private AccountDto toDto(Account account) {
    AccountDto dto = new AccountDto();
    dto.setId(account.getId());
    dto.setBalance(account.getBalance());
    dto.setClientId(account.getClientId());
    return dto;
  }
}
```

## File: `src/main/java/bankservice/port/incoming/adapter/resources/accounts/AccountsResource.java`
```java
package bankservice.port.incoming.adapter.resources.accounts;

import static com.google.common.base.Preconditions.checkNotNull;
import static jakarta.ws.rs.core.MediaType.APPLICATION_JSON;
import static jakarta.ws.rs.core.UriBuilder.fromResource;

import bankservice.domain.model.account.Account;
import bankservice.service.account.AccountService;
import bankservice.service.account.OpenAccountCommand;
import jakarta.validation.Valid;
import jakarta.ws.rs.Consumes;
import jakarta.ws.rs.POST;
import jakarta.ws.rs.Path;
import jakarta.ws.rs.Produces;
import jakarta.ws.rs.core.Response;
import java.net.URI;

@Consumes(APPLICATION_JSON)
@Produces(APPLICATION_JSON)
@Path("/accounts")
public class AccountsResource {

  private final AccountService accountService;

  public AccountsResource(AccountService accountService) {
    this.accountService = checkNotNull(accountService);
  }

  @POST
  public Response post(@Valid AccountDto accountDto) {
    OpenAccountCommand command = new OpenAccountCommand(accountDto.getClientId());
    Account account = accountService.process(command);
    URI accountUri = fromResource(AccountResource.class).build(account.getId());
    return Response.created(accountUri).build();
  }
}
```

## File: `src/main/java/bankservice/port/incoming/adapter/resources/accounts/deposits/DepositDto.java`
```java
package bankservice.port.incoming.adapter.resources.accounts.deposits;

import static com.fasterxml.jackson.annotation.JsonProperty.Access.READ_ONLY;

import com.fasterxml.jackson.annotation.JsonProperty;
import jakarta.validation.constraints.NotNull;
import java.math.BigDecimal;
import java.util.UUID;

public class DepositDto {

  @JsonProperty(access = READ_ONLY)
  private UUID accountId;

  @NotNull
  private BigDecimal amount;


  @SuppressWarnings("unused")
  public UUID getAccountId() {
    return accountId;
  }

  @SuppressWarnings("unused")
  public void setAccountId(UUID accountId) {
    this.accountId = accountId;
  }

  @SuppressWarnings("unused")
  public BigDecimal getAmount() {
    return amount;
  }

  @SuppressWarnings("unused")
  public void setAmount(BigDecimal amount) {
    this.amount = amount;
  }
}
```

## File: `src/main/java/bankservice/port/incoming/adapter/resources/accounts/deposits/DepositsResource.java`
```java
package bankservice.port.incoming.adapter.resources.accounts.deposits;

import static com.google.common.base.Preconditions.checkNotNull;
import static jakarta.ws.rs.core.MediaType.APPLICATION_JSON;

import bankservice.domain.model.OptimisticLockingException;
import bankservice.service.account.AccountNotFoundException;
import bankservice.service.account.AccountService;
import bankservice.service.account.DepositAccountCommand;
import io.dropwizard.jersey.params.UUIDParam;
import jakarta.validation.Valid;
import jakarta.ws.rs.Consumes;
import jakarta.ws.rs.POST;
import jakarta.ws.rs.Path;
import jakarta.ws.rs.PathParam;
import jakarta.ws.rs.Produces;
import jakarta.ws.rs.core.Response;

@Consumes(APPLICATION_JSON)
@Produces(APPLICATION_JSON)
@Path("/accounts/{id}/deposits")
public class DepositsResource {

  private final AccountService accountService;

  public DepositsResource(AccountService accountService) {
    this.accountService = checkNotNull(accountService);
  }

  @POST
  public Response post(@PathParam("id") UUIDParam accountId, @Valid DepositDto depositDto)
      throws AccountNotFoundException, OptimisticLockingException {

    DepositAccountCommand command = new DepositAccountCommand(accountId.get(),
        depositDto.getAmount());
    accountService.process(command);
    return Response.noContent().build();
  }
}
```

## File: `src/main/java/bankservice/port/incoming/adapter/resources/accounts/withdrawals/WithdrawalDto.java`
```java
package bankservice.port.incoming.adapter.resources.accounts.withdrawals;

import static com.fasterxml.jackson.annotation.JsonProperty.Access.READ_ONLY;

import com.fasterxml.jackson.annotation.JsonProperty;
import jakarta.validation.constraints.NotNull;
import java.math.BigDecimal;
import java.util.UUID;

public class WithdrawalDto {

  @JsonProperty(access = READ_ONLY)
  private UUID accountId;

  @NotNull
  private BigDecimal amount;


  @SuppressWarnings("unused")
  public UUID getAccountId() {
    return accountId;
  }

  @SuppressWarnings("unused")
  public void setAccountId(UUID accountId) {
    this.accountId = accountId;
  }

  @SuppressWarnings("unused")
  public BigDecimal getAmount() {
    return amount;
  }

  @SuppressWarnings("unused")
  public void setAmount(BigDecimal amount) {
    this.amount = amount;
  }
}
```

## File: `src/main/java/bankservice/port/incoming/adapter/resources/accounts/withdrawals/WithdrawalsResource.java`
```java
package bankservice.port.incoming.adapter.resources.accounts.withdrawals;

import static com.google.common.base.Preconditions.checkNotNull;
import static jakarta.ws.rs.core.MediaType.APPLICATION_JSON;
import static jakarta.ws.rs.core.Response.Status.BAD_REQUEST;

import bankservice.domain.model.OptimisticLockingException;
import bankservice.domain.model.account.NonSufficientFundsException;
import bankservice.service.account.AccountNotFoundException;
import bankservice.service.account.AccountService;
import bankservice.service.account.WithdrawAccountCommand;
import io.dropwizard.jersey.params.UUIDParam;
import jakarta.validation.Valid;
import jakarta.ws.rs.Consumes;
import jakarta.ws.rs.POST;
import jakarta.ws.rs.Path;
import jakarta.ws.rs.PathParam;
import jakarta.ws.rs.Produces;
import jakarta.ws.rs.core.Response;

@Consumes(APPLICATION_JSON)
@Produces(APPLICATION_JSON)
@Path("/accounts/{id}/withdrawals")
public class WithdrawalsResource {

  private final AccountService accountService;

  public WithdrawalsResource(AccountService accountService) {
    this.accountService = checkNotNull(accountService);
  }

  @POST
  public Response post(@PathParam("id") UUIDParam accountId, @Valid WithdrawalDto withdrawalDto)
      throws AccountNotFoundException, OptimisticLockingException {

    WithdrawAccountCommand command = new WithdrawAccountCommand(accountId.get(),
        withdrawalDto.getAmount());
    try {
      accountService.process(command);
    } catch (NonSufficientFundsException e) {
      return Response.status(BAD_REQUEST).build();
    }
    return Response.noContent().build();
  }
}
```

## File: `src/main/java/bankservice/port/incoming/adapter/resources/clients/ClientDto.java`
```java
package bankservice.port.incoming.adapter.resources.clients;

import static com.fasterxml.jackson.annotation.JsonProperty.Access.READ_ONLY;

import com.fasterxml.jackson.annotation.JsonProperty;
import jakarta.validation.constraints.NotBlank;
import java.util.UUID;

public class ClientDto {

  @JsonProperty(access = READ_ONLY)
  private UUID id;

  @NotBlank
  private String name;

  @Email
  private String email;


  @SuppressWarnings("unused")
  public UUID getId() {
    return id;
  }

  @SuppressWarnings("unused")
  public void setId(UUID id) {
    this.id = id;
  }

  @SuppressWarnings("unused")
  public String getName() {
    return name;
  }

  @SuppressWarnings("unused")
  public void setName(String name) {
    this.name = name;
  }

  @SuppressWarnings("unused")
  public String getEmail() {
    return email;
  }

  @SuppressWarnings("unused")
  public void setEmail(String email) {
    this.email = email;
  }
}
```

## File: `src/main/java/bankservice/port/incoming/adapter/resources/clients/ClientResource.java`
```java
package bankservice.port.incoming.adapter.resources.clients;

import static com.google.common.base.Preconditions.checkNotNull;
import static jakarta.ws.rs.core.MediaType.APPLICATION_JSON;
import static jakarta.ws.rs.core.Response.Status.NOT_FOUND;

import bankservice.domain.model.client.Client;
import bankservice.domain.model.client.Email;
import bankservice.service.client.ClientService;
import bankservice.service.client.UpdateClientCommand;
import io.dropwizard.jersey.params.UUIDParam;
import jakarta.validation.Valid;
import jakarta.validation.constraints.NotNull;
import jakarta.ws.rs.Consumes;
import jakarta.ws.rs.GET;
import jakarta.ws.rs.PUT;
import jakarta.ws.rs.Path;
import jakarta.ws.rs.PathParam;
import jakarta.ws.rs.Produces;
import jakarta.ws.rs.core.Response;
import java.util.Optional;

@Consumes(APPLICATION_JSON)
@Produces(APPLICATION_JSON)
@Path("/clients/{id}")
public class ClientResource {

  private ClientService clientService;

  public ClientResource(ClientService clientService) {
    this.clientService = checkNotNull(clientService);
  }

  @GET
  public Response get(@PathParam("id") UUIDParam clientId) {
    Optional<Client> possibleClient = clientService.loadClient(clientId.get());
    if (!possibleClient.isPresent()) {
      return Response.status(NOT_FOUND).build();
    }
    ClientDto clientDto = toDto(possibleClient.get());
    return Response.ok(clientDto).build();
  }

  @PUT
  public Response put(@PathParam("id") UUIDParam clientId, @Valid @NotNull ClientDto clientDto) {
    UpdateClientCommand command = new UpdateClientCommand(
        clientId.get(), clientDto.getName(), new Email(clientDto.getEmail()));
    clientService.process(command);
    return Response.noContent().build();
  }

  private ClientDto toDto(Client client) {
    ClientDto dto = new ClientDto();
    dto.setId(client.getId());
    dto.setName(client.getName());
    dto.setEmail(client.getEmail().getValue());
    return dto;
  }
}
```

## File: `src/main/java/bankservice/port/incoming/adapter/resources/clients/ClientsResource.java`
```java
package bankservice.port.incoming.adapter.resources.clients;

import static com.google.common.base.Preconditions.checkNotNull;
import static jakarta.ws.rs.core.MediaType.APPLICATION_JSON;
import static jakarta.ws.rs.core.UriBuilder.fromResource;

import bankservice.domain.model.client.Client;
import bankservice.domain.model.client.Email;
import bankservice.service.client.ClientService;
import bankservice.service.client.EnrollClientCommand;
import jakarta.validation.Valid;
import jakarta.ws.rs.Consumes;
import jakarta.ws.rs.POST;
import jakarta.ws.rs.Path;
import jakarta.ws.rs.Produces;
import jakarta.ws.rs.core.Response;
import java.net.URI;

@Consumes(APPLICATION_JSON)
@Produces(APPLICATION_JSON)
@Path("/clients")
public class ClientsResource {

  private ClientService clientService;

  public ClientsResource(ClientService clientService) {
    this.clientService = checkNotNull(clientService);
  }

  @POST
  public Response post(@Valid ClientDto newClientDto) {
    EnrollClientCommand enrollClientCommand = new EnrollClientCommand(
        newClientDto.getName(), new Email(newClientDto.getEmail()));
    Client client = clientService.process(enrollClientCommand);
    URI clientUri = fromResource(ClientResource.class).build(client.getId());
    return Response.created(clientUri).build();
  }
}
```

## File: `src/main/java/bankservice/port/incoming/adapter/resources/clients/Email.java`
```java
package bankservice.port.incoming.adapter.resources.clients;

import static java.lang.annotation.ElementType.FIELD;
import static java.lang.annotation.RetentionPolicy.RUNTIME;

import bankservice.domain.model.client.Email.EmailSpecification;
import jakarta.validation.Constraint;
import jakarta.validation.ConstraintValidator;
import jakarta.validation.ConstraintValidatorContext;
import jakarta.validation.Payload;
import jakarta.validation.constraints.NotNull;
import java.lang.annotation.Retention;
import java.lang.annotation.Target;

@NotNull
@Target(FIELD)
@Retention(RUNTIME)
@Constraint(validatedBy = Email.EmailValidator.class)
public @interface Email {

  String message() default "not a well-formed email address";

  Class<?>[] groups() default {};

  Class<? extends Payload>[] payload() default {};


  class EmailValidator implements ConstraintValidator<Email, String> {

    private EmailSpecification emailSpecification = new EmailSpecification();

    @Override
    public void initialize(Email constraintAnnotation) {
    }

    @Override
    public boolean isValid(String value, ConstraintValidatorContext context) {
      return emailSpecification.isSatisfiedBy(value);
    }
  }
}
```

## File: `src/main/java/bankservice/port/outgoing/adapter/eventstore/InMemoryEventStore.java`
```java
package bankservice.port.outgoing.adapter.eventstore;

import static java.util.Collections.emptyList;
import static java.util.stream.Collectors.toList;

import bankservice.domain.model.Event;
import bankservice.domain.model.EventStore;
import bankservice.domain.model.OptimisticLockingException;
import com.google.common.collect.ImmutableList;
import java.util.List;
import java.util.Map;
import java.util.UUID;
import java.util.concurrent.ConcurrentHashMap;
import java.util.stream.Stream;

public class InMemoryEventStore implements EventStore {

  private final Map<UUID, List<Event>> eventStore = new ConcurrentHashMap<>();

  @Override
  public void store(UUID aggregateId, List<Event> newEvents, int baseVersion)
      throws OptimisticLockingException {
    eventStore.merge(aggregateId, newEvents, (oldValue, value) -> {
      if (baseVersion != oldValue.get(oldValue.size() - 1).getVersion()) {
        throw new OptimisticLockingException("Base version does not match current stored version");
      }

      return Stream.concat(oldValue.stream(), value.stream()).collect(toList());
    });
  }

  @Override
  public List<Event> load(UUID aggregateId) {
    return ImmutableList.copyOf(eventStore.getOrDefault(aggregateId, emptyList()));
  }
}
```

## File: `src/main/java/bankservice/projection/accounttransactions/AccountTransactionsResource.java`
```java
package bankservice.projection.accounttransactions;

import static com.google.common.base.Preconditions.checkNotNull;
import static jakarta.ws.rs.core.MediaType.APPLICATION_JSON;

import jakarta.ws.rs.GET;
import jakarta.ws.rs.Path;
import jakarta.ws.rs.PathParam;
import jakarta.ws.rs.Produces;
import jakarta.ws.rs.core.Response;
import java.util.List;
import java.util.UUID;

@Produces(APPLICATION_JSON)
@Path("/accounts/{id}/transactions")
public class AccountTransactionsResource {

  private TransactionsRepository transactionsRepository;

  public AccountTransactionsResource(TransactionsRepository transactionsRepository) {
    this.transactionsRepository = checkNotNull(transactionsRepository);
  }

  @GET
  public Response get(@PathParam("id") UUID accountId) {
    List<TransactionProjection> transactionProjections = transactionsRepository
        .listByAccount(accountId);
    return Response.ok(transactionProjections).build();
  }
}
```

## File: `src/main/java/bankservice/projection/accounttransactions/InMemoryTransactionsRepository.java`
```java
package bankservice.projection.accounttransactions;

import static com.google.common.collect.Lists.newArrayList;
import static java.util.Collections.emptyList;
import static java.util.Comparator.comparing;
import static java.util.stream.Collectors.toList;

import java.util.List;
import java.util.Map;
import java.util.UUID;
import java.util.concurrent.ConcurrentHashMap;
import java.util.stream.Stream;

public class InMemoryTransactionsRepository implements TransactionsRepository {

  private Map<UUID, List<TransactionProjection>> accountTransactions = new ConcurrentHashMap<>();

  @Override
  public List<TransactionProjection> listByAccount(UUID accountId) {
    return accountTransactions.getOrDefault(accountId, emptyList()).stream()
        .sorted(comparing(TransactionProjection::getVersion))
        .collect(toList());
  }

  @Override
  public void save(TransactionProjection transactionProjection) {
    accountTransactions.merge(
        transactionProjection.getAccountId(),
        newArrayList(transactionProjection),
        (oldValue, value) -> Stream.concat(oldValue.stream(), value.stream()).collect(toList()));
  }
}
```

## File: `src/main/java/bankservice/projection/accounttransactions/TransactionProjection.java`
```java
package bankservice.projection.accounttransactions;

import static com.google.common.base.Preconditions.checkNotNull;

import java.math.BigDecimal;
import java.time.ZonedDateTime;
import java.util.UUID;

public class TransactionProjection {

  private final UUID accountId;
  private final TransactionType type;
  private final BigDecimal amount;
  private final ZonedDateTime timestamp;
  private final int version;

  public TransactionProjection(UUID accountId, TransactionType type, BigDecimal amount,
      ZonedDateTime timestamp, int version) {
    this.accountId = checkNotNull(accountId);
    this.type = checkNotNull(type);
    this.amount = checkNotNull(amount).setScale(2, BigDecimal.ROUND_HALF_UP);
    this.timestamp = checkNotNull(timestamp);
    this.version = version;
  }

  public UUID getAccountId() {
    return accountId;
  }

  public TransactionType getType() {
    return type;
  }

  public BigDecimal getAmount() {
    return amount;
  }

  public ZonedDateTime getTimestamp() {
    return timestamp;
  }

  public int getVersion() {
    return version;
  }

  public enum TransactionType {
    DEPOSIT, WITHDRAWAL
  }
}
```

## File: `src/main/java/bankservice/projection/accounttransactions/TransactionsListener.java`
```java
package bankservice.projection.accounttransactions;

import static bankservice.projection.accounttransactions.TransactionProjection.TransactionType.DEPOSIT;
import static bankservice.projection.accounttransactions.TransactionProjection.TransactionType.WITHDRAWAL;
import static com.google.common.base.Preconditions.checkNotNull;

import bankservice.domain.model.account.AccountDepositedEvent;
import bankservice.domain.model.account.AccountWithdrawnEvent;
import com.google.common.eventbus.Subscribe;

public class TransactionsListener {

  private TransactionsRepository transactionsRepository;

  public TransactionsListener(TransactionsRepository transactionsRepository) {
    this.transactionsRepository = checkNotNull(transactionsRepository);
  }

  @Subscribe
  @SuppressWarnings("unused")
  public void handle(AccountDepositedEvent event) {
    TransactionProjection tx = new TransactionProjection(
        event.getAggregateId(), DEPOSIT, event.getAmount(), event.getTimestamp(),
        event.getVersion());
    transactionsRepository.save(tx);
  }

  @Subscribe
  @SuppressWarnings("unused")
  public void handle(AccountWithdrawnEvent event) {
    TransactionProjection tx = new TransactionProjection(
        event.getAggregateId(), WITHDRAWAL, event.getAmount(), event.getTimestamp(),
        event.getVersion());
    transactionsRepository.save(tx);
  }
}
```

## File: `src/main/java/bankservice/projection/accounttransactions/TransactionsRepository.java`
```java
package bankservice.projection.accounttransactions;

import java.util.List;
import java.util.UUID;

public interface TransactionsRepository {

  void save(TransactionProjection transactionProjection);

  List<TransactionProjection> listByAccount(UUID accountId);

}
```

## File: `src/main/java/bankservice/projection/clientaccounts/AccountProjection.java`
```java
package bankservice.projection.clientaccounts;

import static com.google.common.base.Preconditions.checkNotNull;

import java.math.BigDecimal;
import java.util.UUID;

public class AccountProjection {

  private final UUID accountId;
  private final UUID clientId;
  private final BigDecimal balance;
  private final int version;

  public AccountProjection(UUID accountId, UUID clientId, BigDecimal balance, int version) {
    this.accountId = checkNotNull(accountId);
    this.clientId = checkNotNull(clientId);
    this.balance = checkNotNull(balance);
    this.version = version;
  }

  public UUID getAccountId() {
    return accountId;
  }

  public UUID getClientId() {
    return clientId;
  }

  public BigDecimal getBalance() {
    return balance;
  }

  public int getVersion() {
    return version;
  }
}
```

## File: `src/main/java/bankservice/projection/clientaccounts/AccountsListener.java`
```java
package bankservice.projection.clientaccounts;

import static com.google.common.base.Preconditions.checkNotNull;

import bankservice.domain.model.account.AccountDepositedEvent;
import bankservice.domain.model.account.AccountOpenedEvent;
import bankservice.domain.model.account.AccountWithdrawnEvent;
import com.google.common.eventbus.Subscribe;

public class AccountsListener {

  private final AccountsRepository accountsRepository;

  public AccountsListener(AccountsRepository accountsRepository) {
    this.accountsRepository = checkNotNull(accountsRepository);
  }

  @Subscribe
  @SuppressWarnings("unused")
  public void handle(AccountOpenedEvent event) {
    AccountProjection accountProjection = new AccountProjection(
        event.getAggregateId(), event.getClientId(), event.getBalance(), event.getVersion());
    accountsRepository.save(accountProjection);
  }

  @Subscribe
  @SuppressWarnings("unused")
  public void handle(AccountDepositedEvent event) {
    accountsRepository
        .updateBalance(event.getAggregateId(), event.getBalance(), event.getVersion());
  }

  @Subscribe
  @SuppressWarnings("unused")
  public void handle(AccountWithdrawnEvent event) {
    accountsRepository
        .updateBalance(event.getAggregateId(), event.getBalance(), event.getVersion());
  }
}
```

## File: `src/main/java/bankservice/projection/clientaccounts/AccountsRepository.java`
```java
package bankservice.projection.clientaccounts;

import java.math.BigDecimal;
import java.util.List;
import java.util.UUID;

public interface AccountsRepository {

  void save(AccountProjection accountProjection);

  void updateBalance(UUID accountId, BigDecimal balance, int version);

  List<AccountProjection> getAccounts(UUID clientId);
}
```

## File: `src/main/java/bankservice/projection/clientaccounts/ClientAccountsResource.java`
```java
package bankservice.projection.clientaccounts;

import static com.google.common.base.Preconditions.checkNotNull;
import static jakarta.ws.rs.core.MediaType.APPLICATION_JSON;

import io.dropwizard.jersey.params.UUIDParam;
import jakarta.ws.rs.Consumes;
import jakarta.ws.rs.GET;
import jakarta.ws.rs.Path;
import jakarta.ws.rs.PathParam;
import jakarta.ws.rs.Produces;
import jakarta.ws.rs.core.Response;
import java.util.List;

@Consumes(APPLICATION_JSON)
@Produces(APPLICATION_JSON)
@Path("clients/{id}/accounts")
public class ClientAccountsResource {

  private final AccountsRepository accountsRepository;

  public ClientAccountsResource(AccountsRepository accountsRepository) {
    this.accountsRepository = checkNotNull(accountsRepository);
  }

  @GET
  public Response get(@PathParam("id") UUIDParam clientId) {
    List<AccountProjection> accounts = accountsRepository.getAccounts(clientId.get());
    return Response.ok(accounts).build();
  }
}
```

## File: `src/main/java/bankservice/projection/clientaccounts/InMemoryAccountsRepository.java`
```java
package bankservice.projection.clientaccounts;

import static java.util.Collections.emptyMap;

import com.google.common.collect.ImmutableList;
import java.math.BigDecimal;
import java.util.AbstractMap;
import java.util.List;
import java.util.Map;
import java.util.UUID;
import java.util.concurrent.ConcurrentHashMap;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class InMemoryAccountsRepository implements AccountsRepository {

  private final Map<UUID, Map<UUID, AccountProjection>> clientAccounts = new ConcurrentHashMap<>();
  private final Map<UUID, UUID> accountClientIndex = new ConcurrentHashMap<>();

  @Override
  public void save(AccountProjection accountProjection) {
    clientAccounts.merge(
        accountProjection.getClientId(),
        newAccountsMap(accountProjection),
        (oldValue, value) -> {
          oldValue.putAll(value);
          return oldValue;
        }
    );
    accountClientIndex.put(accountProjection.getAccountId(), accountProjection.getClientId());
  }

  @Override
  public void updateBalance(UUID accountId, BigDecimal balance, int version) {
    UUID clientId = accountClientIndex.get(accountId);
    clientAccounts.get(clientId).merge(
        accountId,
        new AccountProjection(accountId, clientId, balance, version),
        (oldValue, value) -> value.getVersion() > oldValue.getVersion() ? value : oldValue);
  }

  @Override
  public List<AccountProjection> getAccounts(UUID clientId) {
    Map<UUID, AccountProjection> accounts = clientAccounts.getOrDefault(clientId, emptyMap());
    return ImmutableList.copyOf(accounts.values());
  }

  private Map<UUID, AccountProjection> newAccountsMap(AccountProjection accountProjection) {
    return Stream.of(
        new AbstractMap.SimpleEntry<>(accountProjection.getAccountId(), accountProjection))
        .collect(Collectors.toMap(Map.Entry::getKey, Map.Entry::getValue));
  }
}
```

## File: `src/main/java/bankservice/service/Retrier.java`
```java
package bankservice.service;

import static com.google.common.base.Preconditions.checkArgument;

import java.util.List;
import java.util.function.Supplier;

public class Retrier {

  private final List<Class<? extends Exception>> retriableExceptions;
  private final int maxAttempts;

  public Retrier(List<Class<? extends Exception>> retriableExceptions, int maxAttempts) {
    checkArgument(!retriableExceptions.isEmpty());
    checkArgument(maxAttempts > 1);
    this.retriableExceptions = retriableExceptions;
    this.maxAttempts = maxAttempts;
  }

  public <T> T get(Supplier<T> supplier) {
    for (int attempt = 1; ; attempt++) {
      try {
        return supplier.get();
      } catch (Exception exception) {
        if (!isRetriable(exception) || attempt == maxAttempts) {
          throw exception;
        }
      }
    }
  }

  private boolean isRetriable(Exception exception) {
    return retriableExceptions.stream().anyMatch(e -> e.isAssignableFrom(exception.getClass()));
  }
}
```

## File: `src/main/java/bankservice/service/account/AccountNotFoundException.java`
```java
package bankservice.service.account;

import static java.lang.String.format;

import java.util.UUID;

public class AccountNotFoundException extends RuntimeException {

  public AccountNotFoundException(UUID id) {
    super(format("Account with id '%s' could not be found", id));
  }
}
```

## File: `src/main/java/bankservice/service/account/AccountService.java`
```java
package bankservice.service.account;

import static com.google.common.base.Preconditions.checkNotNull;
import static java.util.Collections.singletonList;
import static java.util.UUID.randomUUID;

import bankservice.domain.model.Event;
import bankservice.domain.model.EventStore;
import bankservice.domain.model.OptimisticLockingException;
import bankservice.domain.model.account.Account;
import bankservice.domain.model.account.NonSufficientFundsException;
import bankservice.service.Retrier;
import com.google.common.eventbus.EventBus;
import java.util.List;
import java.util.Optional;
import java.util.UUID;
import java.util.function.Consumer;

public class AccountService {

  private final EventStore eventStore;
  private final EventBus eventBus;
  private final Retrier conflictRetrier;

  public AccountService(EventStore eventStore, EventBus eventBus) {
    this.eventStore = checkNotNull(eventStore);
    this.eventBus = checkNotNull(eventBus);
    int maxAttempts = 3;
    this.conflictRetrier = new Retrier(
        singletonList(OptimisticLockingException.class),
        maxAttempts);
  }

  public Optional<Account> loadAccount(UUID id) {
    List<Event> eventStream = eventStore.load(id);
    if (eventStream.isEmpty()) {
      return Optional.empty();
    }
    return Optional.of(new Account(id, eventStream));
  }

  public Account process(OpenAccountCommand command) {
    Account account = new Account(randomUUID(), command.getClientId());
    storeAndPublishEvents(account);
    return account;
  }

  public Account process(DepositAccountCommand command)
      throws AccountNotFoundException, OptimisticLockingException {
    return process(command.getId(), (account) -> account.deposit(command.getAmount()));
  }

  public Account process(WithdrawAccountCommand command)
      throws AccountNotFoundException, OptimisticLockingException, NonSufficientFundsException {
    return process(command.getId(), (account) -> account.withdraw(command.getAmount()));
  }

  private Account process(UUID accountId, Consumer<Account> consumer)
      throws AccountNotFoundException, OptimisticLockingException {

    return conflictRetrier.get(() -> {
      Optional<Account> possibleAccount = loadAccount(accountId);
      Account account = possibleAccount.orElseThrow(() -> new AccountNotFoundException(accountId));
      consumer.accept(account);
      storeAndPublishEvents(account);
      return account;
    });
  }

  private void storeAndPublishEvents(Account account) throws OptimisticLockingException {
    eventStore.store(account.getId(), account.getNewEvents(), account.getBaseVersion());
    account.getNewEvents().forEach(eventBus::post);
  }
}
```

## File: `src/main/java/bankservice/service/account/DepositAccountCommand.java`
```java
package bankservice.service.account;

import static com.google.common.base.Preconditions.checkNotNull;

import java.math.BigDecimal;
import java.util.UUID;

public class DepositAccountCommand {

  private final UUID id;
  private final BigDecimal amount;

  public DepositAccountCommand(UUID id, BigDecimal amount) {
    this.id = checkNotNull(id);
    this.amount = checkNotNull(amount);
  }

  public UUID getId() {
    return id;
  }

  public BigDecimal getAmount() {
    return amount;
  }
}
```

## File: `src/main/java/bankservice/service/account/OpenAccountCommand.java`
```java
package bankservice.service.account;

import static com.google.common.base.Preconditions.checkNotNull;

import java.util.UUID;

public class OpenAccountCommand {

  private final UUID clientId;

  public OpenAccountCommand(UUID clientId) {
    this.clientId = checkNotNull(clientId);
  }

  public UUID getClientId() {
    return clientId;
  }
}
```

## File: `src/main/java/bankservice/service/account/WithdrawAccountCommand.java`
```java
package bankservice.service.account;

import static com.google.common.base.Preconditions.checkNotNull;

import java.math.BigDecimal;
import java.util.UUID;

public class WithdrawAccountCommand {

  private final UUID id;
  private final BigDecimal amount;

  public WithdrawAccountCommand(UUID id, BigDecimal amount) {
    this.id = checkNotNull(id);
    this.amount = checkNotNull(amount);
  }

  public UUID getId() {
    return id;
  }

  public BigDecimal getAmount() {
    return amount;
  }
}
```

## File: `src/main/java/bankservice/service/client/ClientNotFoundException.java`
```java
package bankservice.service.client;

import static java.lang.String.format;

import java.util.UUID;

public class ClientNotFoundException extends RuntimeException {

  public ClientNotFoundException(UUID id) {
    super(format("Client with id '%s' could not be found", id));
  }
}
```

## File: `src/main/java/bankservice/service/client/ClientService.java`
```java
package bankservice.service.client;

import static com.google.common.base.Preconditions.checkNotNull;
import static java.util.Collections.singletonList;
import static java.util.UUID.randomUUID;

import bankservice.domain.model.Event;
import bankservice.domain.model.EventStore;
import bankservice.domain.model.OptimisticLockingException;
import bankservice.domain.model.client.Client;
import bankservice.service.Retrier;
import java.util.List;
import java.util.Optional;
import java.util.UUID;
import java.util.function.Consumer;

public class ClientService {

  private final EventStore eventStore;
  private final Retrier conflictRetrier;

  public ClientService(EventStore eventStore) {
    this.eventStore = checkNotNull(eventStore);
    int maxAttempts = 3;
    this.conflictRetrier = new Retrier(singletonList(OptimisticLockingException.class),
        maxAttempts);
  }

  public Optional<Client> loadClient(UUID id) {
    List<Event> eventStream = eventStore.load(id);
    if (eventStream.isEmpty()) {
      return Optional.empty();
    }
    return Optional.of(new Client(id, eventStream));
  }

  public Client process(EnrollClientCommand command) {
    Client client = new Client(randomUUID(), command.getName(), command.getEmail());
    storeEvents(client);
    return client;
  }

  public void process(UpdateClientCommand command) {
    process(command.getId(), c -> c.update(command.getName(), command.getEmail()));
  }

  private Client process(UUID clientId, Consumer<Client> consumer)
      throws ClientNotFoundException, OptimisticLockingException {

    return conflictRetrier.get(() -> {
      Optional<Client> possibleClient = loadClient(clientId);
      Client client = possibleClient.orElseThrow(() -> new ClientNotFoundException(clientId));
      consumer.accept(client);
      storeEvents(client);
      return client;
    });
  }

  private void storeEvents(Client client) {
    eventStore.store(client.getId(), client.getNewEvents(), client.getBaseVersion());
  }
}
```

## File: `src/main/java/bankservice/service/client/EnrollClientCommand.java`
```java
package bankservice.service.client;

import static com.google.common.base.Preconditions.checkNotNull;

import bankservice.domain.model.client.Email;

public class EnrollClientCommand {

  private final String name;
  private final Email email;

  public EnrollClientCommand(String name, Email email) {
    this.name = checkNotNull(name);
    this.email = checkNotNull(email);
  }

  public String getName() {
    return name;
  }

  public Email getEmail() {
    return email;
  }
}
```

## File: `src/main/java/bankservice/service/client/UpdateClientCommand.java`
```java
package bankservice.service.client;


import static com.google.common.base.Preconditions.checkNotNull;

import bankservice.domain.model.client.Email;
import java.util.UUID;

public class UpdateClientCommand {

  private final UUID id;
  private final String name;
  private final Email email;

  public UpdateClientCommand(UUID id, String name, Email email) {
    this.id = checkNotNull(id);
    this.name = checkNotNull(name);
    this.email = checkNotNull(email);
  }

  public UUID getId() {
    return id;
  }

  public String getName() {
    return name;
  }

  public Email getEmail() {
    return email;
  }
}
```

## File: `src/main/resources/checkstyle/google_checks.xml`
```xml
<?xml version="1.0"?>
<!DOCTYPE module PUBLIC
  "-//Checkstyle//DTD Checkstyle Configuration 1.3//EN"
  "https://checkstyle.org/dtds/configuration_1_3.dtd">

<!--
    Checkstyle configuration that checks the Google coding conventions from Google Java Style
    that can be found at https://google.github.io/styleguide/javaguide.html

    Checkstyle is very configurable. Be sure to read the documentation at
    http://checkstyle.org (or in your downloaded distribution).

    To completely disable a check, just comment it out or delete it from the file.
    To suppress certain violations please review suppression filters.

    Authors: Max Vetrenko, Ruslan Diachenko, Roman Ivanov.
 -->

<module name="Checker">
  <module name="BeforeExecutionExclusionFileFilter">
    <property name="fileNamePattern" value="module\-info\.java$"/>
  </module>

  <module name="SuppressionFilter">
    <property default="checkstyle-suppressions.xml" name="file"
      value="${org.checkstyle.google.suppressionfilter.config}"/>
    <property name="optional" value="true"/>
  </module>

  <module name="FileTabCharacter">
    <property name="eachLine" value="true"/>
  </module>
  <!-- Excludes all 'module-info.java' files              -->
  <!-- See https://checkstyle.org/config_filefilters.html -->
  <module name="LineLength">
    <property name="fileExtensions" value="java"/>
    <property name="max" value="100"/>
    <property name="ignorePattern"
      value="^package.*|^import.*|a href|href|http://|https://|ftp://"/>
  </module>
  <!-- https://checkstyle.org/config_filters.html#SuppressionFilter -->
  <module name="TreeWalker">
    <module name="OuterTypeFilename"/>
    <module name="IllegalTokenText">
      <property name="tokens" value="STRING_LITERAL, CHAR_LITERAL"/>
      <property name="format"
        value="\\u00(09|0(a|A)|0(c|C)|0(d|D)|22|27|5(C|c))|\\(0(10|11|12|14|15|42|47)|134)"/>
      <property name="message"
        value="Consider using special escape sequence instead of octal value or Unicode escaped value."/>
    </module>
    <module name="AvoidEscapedUnicodeCharacters">
      <property name="allowEscapesForControlCharacters" value="true"/>
      <property name="allowByTailComment" value="true"/>
      <property name="allowNonPrintableEscapes" value="true"/>
    </module>
    <module name="AvoidStarImport"/>
    <module name="OneTopLevelClass"/>
    <module name="NoLineWrap">
      <property name="tokens" value="PACKAGE_DEF, IMPORT, STATIC_IMPORT"/>
    </module>
    <module name="EmptyBlock">
      <property name="option" value="TEXT"/>
      <property name="tokens"
        value="LITERAL_TRY, LITERAL_FINALLY, LITERAL_IF, LITERAL_ELSE, LITERAL_SWITCH"/>
    </module>
    <module name="NeedBraces">
      <property name="tokens"
        value="LITERAL_DO, LITERAL_ELSE, LITERAL_FOR, LITERAL_IF, LITERAL_WHILE"/>
    </module>
    <module name="LeftCurly">
      <property name="tokens"
        value="ANNOTATION_DEF, CLASS_DEF, CTOR_DEF, ENUM_CONSTANT_DEF, ENUM_DEF,
                    INTERFACE_DEF, LAMBDA, LITERAL_CASE, LITERAL_CATCH, LITERAL_DEFAULT,
                    LITERAL_DO, LITERAL_ELSE, LITERAL_FINALLY, LITERAL_FOR, LITERAL_IF,
                    LITERAL_SWITCH, LITERAL_SYNCHRONIZED, LITERAL_TRY, LITERAL_WHILE, METHOD_DEF,
                    OBJBLOCK, STATIC_INIT"/>
    </module>
    <module name="RightCurly">
      <property name="id" value="RightCurlySame"/>
      <property name="tokens"
        value="LITERAL_TRY, LITERAL_CATCH, LITERAL_FINALLY, LITERAL_IF, LITERAL_ELSE,
                    LITERAL_DO"/>
    </module>
    <module name="RightCurly">
      <property name="id" value="RightCurlyAlone"/>
      <property name="option" value="alone"/>
      <property name="tokens"
        value="CLASS_DEF, METHOD_DEF, CTOR_DEF, LITERAL_FOR, LITERAL_WHILE, STATIC_INIT,
                    INSTANCE_INIT, ANNOTATION_DEF, ENUM_DEF"/>
    </module>
    <module name="SuppressionXpathSingleFilter">
      <!-- suppresion is required till https://github.com/checkstyle/checkstyle/issues/7541 -->
      <property name="id" value="RightCurlyAlone"/>
      <property name="query" value="//RCURLY[parent::SLIST[count(./*)=1]
                                                 or preceding-sibling::*[last()][self::LCURLY]]"/>
    </module>
    <module name="WhitespaceAround">
      <message key="ws.notFollowed"
        value="WhitespaceAround: ''{0}'' is not followed by whitespace. Empty blocks may only be represented as '{}' when not part of a multi-block statement (4.1.3)"/>
      <message key="ws.notPreceded"
        value="WhitespaceAround: ''{0}'' is not preceded with whitespace."/>
      <property name="allowEmptyMethods" value="true"/>
      <property name="allowEmptyTypes" value="true"/>
      <property name="allowEmptyLoops" value="true"/>
      <property name="tokens"
        value="ASSIGN, BAND, BAND_ASSIGN, BOR, BOR_ASSIGN, BSR, BSR_ASSIGN, BXOR,
                    BXOR_ASSIGN, COLON, DIV, DIV_ASSIGN, DO_WHILE, EQUAL, GE, GT, LAMBDA, LAND,
                    LCURLY, LE, LITERAL_CATCH, LITERAL_DO, LITERAL_ELSE, LITERAL_FINALLY,
                    LITERAL_FOR, LITERAL_IF, LITERAL_RETURN, LITERAL_SWITCH, LITERAL_SYNCHRONIZED,
                     LITERAL_TRY, LITERAL_WHILE, LOR, LT, MINUS, MINUS_ASSIGN, MOD, MOD_ASSIGN,
                     NOT_EQUAL, PLUS, PLUS_ASSIGN, QUESTION, RCURLY, SL, SLIST, SL_ASSIGN, SR,
                     SR_ASSIGN, STAR, STAR_ASSIGN, LITERAL_ASSERT, TYPE_EXTENSION_AND"/>
      <property name="allowEmptyConstructors" value="true"/>
      <property name="allowEmptyLambdas" value="true"/>
    </module>
    <module name="OneStatementPerLine"/>
    <module name="MultipleVariableDeclarations"/>
    <module name="ArrayTypeStyle"/>
    <module name="MissingSwitchDefault"/>
    <module name="FallThrough"/>
    <module name="UpperEll"/>
    <module name="ModifierOrder"/>
    <module name="EmptyLineSeparator">
      <property name="tokens"
        value="PACKAGE_DEF, IMPORT, STATIC_IMPORT, CLASS_DEF, INTERFACE_DEF, ENUM_DEF,
                    STATIC_INIT, INSTANCE_INIT, METHOD_DEF, CTOR_DEF, VARIABLE_DEF"/>
      <property name="allowNoEmptyLineBetweenFields" value="true"/>
    </module>
    <module name="SeparatorWrap">
      <property name="id" value="SeparatorWrapDot"/>
      <property name="tokens" value="DOT"/>
      <property name="option" value="nl"/>
    </module>
    <module name="SeparatorWrap">
      <property name="id" value="SeparatorWrapComma"/>
      <property name="tokens" value="COMMA"/>
      <property name="option" value="EOL"/>
    </module>
    <module name="SeparatorWrap">
      <!-- ELLIPSIS is EOL until https://github.com/google/styleguide/issues/258 -->
      <property name="id" value="SeparatorWrapEllipsis"/>
      <property name="tokens" value="ELLIPSIS"/>
      <property name="option" value="EOL"/>
    </module>
    <module name="SeparatorWrap">
      <!-- ARRAY_DECLARATOR is EOL until https://github.com/google/styleguide/issues/259 -->
      <property name="id" value="SeparatorWrapArrayDeclarator"/>
      <property name="tokens" value="ARRAY_DECLARATOR"/>
      <property name="option" value="EOL"/>
    </module>
    <module name="SeparatorWrap">
      <property name="id" value="SeparatorWrapMethodRef"/>
      <property name="tokens" value="METHOD_REF"/>
      <property name="option" value="nl"/>
    </module>
    <module name="PackageName">
      <message key="name.invalidPattern"
        value="Package name ''{0}'' must match pattern ''{1}''."/>
      <property name="format" value="^[a-z]+(\.[a-z][a-z0-9]*)*$"/>
    </module>
    <module name="TypeName">
      <message key="name.invalidPattern"
        value="Type name ''{0}'' must match pattern ''{1}''."/>
      <property name="tokens" value="CLASS_DEF, INTERFACE_DEF, ENUM_DEF, ANNOTATION_DEF"/>
    </module>
    <module name="MemberName">
      <message key="name.invalidPattern"
        value="Member name ''{0}'' must match pattern ''{1}''."/>
      <property name="format" value="^[a-z][a-z0-9][a-zA-Z0-9]*$"/>
    </module>
    <module name="ParameterName">
      <message key="name.invalidPattern"
        value="Parameter name ''{0}'' must match pattern ''{1}''."/>
      <property name="format" value="^[a-z]([a-z0-9][a-zA-Z0-9]*)?$"/>
    </module>
    <module name="LambdaParameterName">
      <message key="name.invalidPattern"
        value="Lambda parameter name ''{0}'' must match pattern ''{1}''."/>
      <property name="format" value="^[a-z]([a-z0-9][a-zA-Z0-9]*)?$"/>
    </module>
    <module name="CatchParameterName">
      <message key="name.invalidPattern"
        value="Catch parameter name ''{0}'' must match pattern ''{1}''."/>
      <property name="format" value="^[a-z]([a-z0-9][a-zA-Z0-9]*)?$"/>
    </module>
    <module name="LocalVariableName">
      <message key="name.invalidPattern"
        value="Local variable name ''{0}'' must match pattern ''{1}''."/>
      <property name="format" value="^[a-z]([a-z0-9][a-zA-Z0-9]*)?$"/>
    </module>
    <module name="ClassTypeParameterName">
      <message key="name.invalidPattern"
        value="Class type name ''{0}'' must match pattern ''{1}''."/>
      <property name="format" value="(^[A-Z][0-9]?)$|([A-Z][a-zA-Z0-9]*[T]$)"/>
    </module>
    <module name="MethodTypeParameterName">
      <message key="name.invalidPattern"
        value="Method type name ''{0}'' must match pattern ''{1}''."/>
      <property name="format" value="(^[A-Z][0-9]?)$|([A-Z][a-zA-Z0-9]*[T]$)"/>
    </module>
    <module name="InterfaceTypeParameterName">
      <message key="name.invalidPattern"
        value="Interface type name ''{0}'' must match pattern ''{1}''."/>
      <property name="format" value="(^[A-Z][0-9]?)$|([A-Z][a-zA-Z0-9]*[T]$)"/>
    </module>
    <module name="NoFinalizer"/>
    <module name="GenericWhitespace">
      <message key="ws.followed"
        value="GenericWhitespace ''{0}'' is followed by whitespace."/>
      <message key="ws.preceded"
        value="GenericWhitespace ''{0}'' is preceded with whitespace."/>
      <message key="ws.illegalFollow"
        value="GenericWhitespace ''{0}'' should followed by whitespace."/>
      <message key="ws.notPreceded"
        value="GenericWhitespace ''{0}'' is not preceded with whitespace."/>
    </module>
    <module name="Indentation">
      <property name="basicOffset" value="2"/>
      <property name="braceAdjustment" value="0"/>
      <property name="caseIndent" value="2"/>
      <property name="throwsIndent" value="4"/>
      <property name="lineWrappingIndentation" value="4"/>
      <property name="arrayInitIndent" value="2"/>
    </module>
    <module name="AbbreviationAsWordInName">
      <property name="ignoreFinal" value="false"/>
      <property name="allowedAbbreviationLength" value="1"/>
      <property name="tokens"
        value="CLASS_DEF, INTERFACE_DEF, ENUM_DEF, ANNOTATION_DEF, ANNOTATION_FIELD_DEF,
                    PARAMETER_DEF, VARIABLE_DEF, METHOD_DEF"/>
    </module>
    <module name="OverloadMethodsDeclarationOrder"/>
    <module name="VariableDeclarationUsageDistance"/>
    <module name="CustomImportOrder">
      <property name="sortImportsInGroupAlphabetically" value="true"/>
      <property name="separateLineBetweenGroups" value="true"/>
      <property name="customImportOrderRules" value="STATIC###THIRD_PARTY_PACKAGE"/>
      <property name="tokens" value="IMPORT, STATIC_IMPORT, PACKAGE_DEF"/>
    </module>
    <module name="MethodParamPad">
      <property name="tokens"
        value="CTOR_DEF, LITERAL_NEW, METHOD_CALL, METHOD_DEF,
                    SUPER_CTOR_CALL, ENUM_CONSTANT_DEF"/>
    </module>
    <module name="NoWhitespaceBefore">
      <property name="tokens"
        value="COMMA, SEMI, POST_INC, POST_DEC, DOT, ELLIPSIS, METHOD_REF"/>
      <property name="allowLineBreaks" value="true"/>
    </module>
    <module name="ParenPad">
      <property name="tokens"
        value="ANNOTATION, ANNOTATION_FIELD_DEF, CTOR_CALL, CTOR_DEF, DOT, ENUM_CONSTANT_DEF,
                    EXPR, LITERAL_CATCH, LITERAL_DO, LITERAL_FOR, LITERAL_IF, LITERAL_NEW,
                    LITERAL_SWITCH, LITERAL_SYNCHRONIZED, LITERAL_WHILE, METHOD_CALL,
                    METHOD_DEF, QUESTION, RESOURCE_SPECIFICATION, SUPER_CTOR_CALL, LAMBDA"/>
    </module>
    <module name="OperatorWrap">
      <property name="option" value="NL"/>
      <property name="tokens"
        value="BAND, BOR, BSR, BXOR, DIV, EQUAL, GE, GT, LAND, LE, LITERAL_INSTANCEOF, LOR,
                    LT, MINUS, MOD, NOT_EQUAL, PLUS, QUESTION, SL, SR, STAR, METHOD_REF "/>
    </module>
    <module name="AnnotationLocation">
      <property name="id" value="AnnotationLocationMostCases"/>
      <property name="tokens"
        value="CLASS_DEF, INTERFACE_DEF, ENUM_DEF, METHOD_DEF, CTOR_DEF"/>
    </module>
    <module name="AnnotationLocation">
      <property name="id" value="AnnotationLocationVariables"/>
      <property name="tokens" value="VARIABLE_DEF"/>
      <property name="allowSamelineMultipleAnnotations" value="true"/>
    </module>
    <module name="NonEmptyAtclauseDescription"/>
    <module name="InvalidJavadocPosition"/>
    <module name="JavadocTagContinuationIndentation"/>
    <module name="SummaryJavadoc">
      <property name="forbiddenSummaryFragments"
        value="^@return the *|^This method returns |^A [{]@code [a-zA-Z0-9]+[}]( is a )"/>
    </module>
    <module name="JavadocParagraph"/>
    <module name="AtclauseOrder">
      <property name="tagOrder" value="@param, @return, @throws, @deprecated"/>
      <property name="target"
        value="CLASS_DEF, INTERFACE_DEF, ENUM_DEF, METHOD_DEF, CTOR_DEF, VARIABLE_DEF"/>
    </module>
    <module name="JavadocMethod">
      <property name="allowMissingParamTags" value="true"/>
      <property name="allowMissingReturnTag" value="true"/>
      <property name="allowedAnnotations" value="Override, Test"/>
      <property name="tokens" value="METHOD_DEF, CTOR_DEF, ANNOTATION_FIELD_DEF"/>
    </module>
    <module name="MissingJavadocMethod">
      <property name="scope" value="public"/>
      <property name="minLineCount" value="2"/>
      <property name="allowedAnnotations" value="Override, Test"/>
      <property name="tokens" value="METHOD_DEF, CTOR_DEF, ANNOTATION_FIELD_DEF"/>
    </module>
    <module name="MethodName">
      <message key="name.invalidPattern"
        value="Method name ''{0}'' must match pattern ''{1}''."/>
      <property name="format" value="^[a-z][a-z0-9][a-zA-Z0-9_]*$"/>
    </module>
    <module name="SingleLineJavadoc">
      <property name="ignoreInlineTags" value="false"/>
    </module>
    <module name="EmptyCatchBlock">
      <property name="exceptionVariableName" value="expected"/>
    </module>
    <module name="CommentsIndentation">
      <property name="tokens" value="SINGLE_LINE_COMMENT, BLOCK_COMMENT_BEGIN"/>
    </module>
    <!-- https://checkstyle.org/config_filters.html#SuppressionXpathFilter -->
    <module name="SuppressionXpathFilter">
      <property default="checkstyle-xpath-suppressions.xml" name="file"
        value="${org.checkstyle.google.suppressionxpathfilter.config}"/>
      <property name="optional" value="true"/>
    </module>
  </module>

  <!-- Checks for whitespace                               -->
  <!-- See http://checkstyle.org/config_whitespace.html -->
  <property name="fileExtensions" value="java, properties, xml"/>

  <property name="charset" value="UTF-8"/>

  <property name="severity" value="warning"/>
</module>
```

## File: `src/main/resources/checkstyle/suppressions.xml`
```xml
<?xml version="1.0"?>
<!DOCTYPE suppressions PUBLIC
  "-//Puppy Crawl//DTD Suppressions 1.1//EN"
  "http://www.puppycrawl.com/dtds/suppressions_1_1.dtd">

<suppressions>
  <suppress checks="MissingJavadocMethod" files=".*\.java"/>
</suppressions>
```

## File: `src/test/java/bankservice/domain/model/AggregateTest.java`
```java
package bankservice.domain.model;

import static java.time.ZoneOffset.UTC;
import static java.time.ZonedDateTime.now;
import static java.util.Collections.singletonList;
import static java.util.UUID.randomUUID;
import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.Matchers.equalTo;
import static org.junit.jupiter.api.Assertions.assertThrows;

import java.time.ZonedDateTime;
import java.util.List;
import java.util.UUID;
import org.junit.jupiter.api.Test;

class AggregateTest {

  @Test
  void newAggregateHasBaseVersion0() {
    Aggregate aggregate = new Aggregate(randomUUID()) {
    };
    assertThat(aggregate.getBaseVersion(), equalTo(0));
  }

  @Test
  void newEventsListIsImmutable() {
    UUID id = randomUUID();
    Aggregate aggregate = new Aggregate(id) {
    };
    assertThrows(
        UnsupportedOperationException.class,
        () -> aggregate.getNewEvents().add(new Event(id, now(UTC), 1) {
        })
    );
  }

  @Test
  void replayEventStreamUsingChildClassMethods() {
    UUID id = randomUUID();
    DummyEvent eventWithCorrespondingHandler = new DummyEvent(id, now(UTC), 1);
    List<Event> eventStream = singletonList(eventWithCorrespondingHandler);
    new BackCallerAggregate(id, eventStream);
    assertThat(eventWithCorrespondingHandler.getCalledBackTimes(), equalTo(1));
  }

  @Test
  void failReplayOfEventWithoutProperChildClassMethodHandler() {
    UUID id = randomUUID();
    Event eventWithoutCorrespondingHandler = new Event(id, now(UTC), 1) {
    };
    List<Event> eventStream = singletonList(eventWithoutCorrespondingHandler);
    assertThrows(
        UnsupportedOperationException.class,
        () -> new Aggregate(id, eventStream) {
        }
    );
  }

  @Test
  void propagatesExceptionOfFailingReplay() {
    UUID id = randomUUID();
    ArithmeticException replayException = new ArithmeticException();
    ProblematicEvent problematicEvent = new ProblematicEvent(id, now(UTC), 1, replayException);
    List<Event> eventStream = singletonList(problematicEvent);
    assertThrows(
        ArithmeticException.class,
        () -> new BackCallerAggregate(id, eventStream)
    );
  }

  @Test
  void replayedAggregateKeepsEventStreamVersionAsItsBaseVersion() {
    UUID id = randomUUID();
    List<Event> eventStream = singletonList(new DummyEvent(id, now(UTC), 1));
    Aggregate aggregate = new BackCallerAggregate(id, eventStream);
    assertThat(aggregate.getBaseVersion(), equalTo(1));
    aggregate.applyNewEvent(new DummyEvent(id, now(UTC), 2));
    assertThat(aggregate.getBaseVersion(), equalTo(1));
  }

  @Test
  void nextVersionOfEmptyEventStreamIs1() {
    Aggregate aggregate = new Aggregate(randomUUID()) {
    };
    assertThat(aggregate.getNextVersion(), equalTo(1));
    assertThat(aggregate.getNextVersion(), equalTo(1));
  }

  @Test
  void nextVersionOfExistingEventStreamIsTotalOfEventsPlus1() {
    UUID id = randomUUID();
    List<Event> eventStream = singletonList(new DummyEvent(id, now(UTC), 1));
    Aggregate aggregate = new BackCallerAggregate(id, eventStream);
    assertThat(aggregate.getNextVersion(), equalTo(2));

    aggregate.applyNewEvent(new DummyEvent(id, now(UTC), 2));
    assertThat(aggregate.getNextVersion(), equalTo(3));
  }

  @Test
  void failOnWrongNewEventVersion() {
    UUID id = randomUUID();
    List<Event> eventStream = singletonList(new DummyEvent(id, now(UTC), 1));
    Aggregate aggregate = new BackCallerAggregate(id, eventStream);
    assertThrows(
        IllegalArgumentException.class,
        () -> aggregate.applyNewEvent(new DummyEvent(id, now(UTC), 1))
    );
  }

  private static class BackCallerAggregate extends Aggregate {

    private BackCallerAggregate(UUID id, List<Event> eventStream) {
      super(id, eventStream);
    }

    @SuppressWarnings("unused")
    private void apply(DummyEvent e) {
      e.callback();
    }

    @SuppressWarnings("unused")
    private void apply(ProblematicEvent e) {
      e.callback();
    }
  }

  private static class DummyEvent extends Event {

    private int calledBackTimes = 0;

    private DummyEvent(UUID aggregateId, ZonedDateTime timestamp, int version) {
      super(aggregateId, timestamp, version);
    }

    void callback() {
      calledBackTimes++;
    }

    int getCalledBackTimes() {
      return calledBackTimes;
    }
  }

  private static class ProblematicEvent extends Event {

    private RuntimeException exception;

    private ProblematicEvent(UUID aggregateId, ZonedDateTime timestamp, int version,
        RuntimeException exception) {
      super(aggregateId, timestamp, version);
      this.exception = exception;
    }

    void callback() {
      throw exception;
    }
  }
}
```

## File: `src/test/java/bankservice/domain/model/account/AccountTest.java`
```java
package bankservice.domain.model.account;

import static java.math.BigDecimal.TEN;
import static java.math.BigDecimal.ZERO;
import static java.util.UUID.randomUUID;
import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.Matchers.equalTo;
import static org.hamcrest.Matchers.instanceOf;
import static org.junit.jupiter.api.Assertions.assertThrows;

import bankservice.domain.model.Event;
import java.math.BigDecimal;
import java.util.List;
import java.util.UUID;
import org.junit.jupiter.api.Test;

class AccountTest {

  @Test
  void newAccountHasNewAccountOpenedEvent() {
    UUID id = randomUUID();
    UUID clientId = randomUUID();
    Account account = new Account(id, clientId);
    List<Event> newEvents = account.getNewEvents();

    assertThat(newEvents.size(), equalTo(1));
    assertThat(newEvents.get(0), instanceOf(AccountOpenedEvent.class));
    AccountOpenedEvent event = (AccountOpenedEvent) newEvents.get(0);
    assertThat(event.getAggregateId(), equalTo(id));
    assertThat(event.getClientId(), equalTo(clientId));
    assertThat(event.getBalance(), equalTo(ZERO));

    assertThat(account.getId(), equalTo(id));
    assertThat(account.getClientId(), equalTo(clientId));
    assertThat(account.getBalance(), equalTo(ZERO));

  }

  @Test
  void depositedAccountHasAccountDepositedEvent() {
    Account account = new Account(randomUUID(), randomUUID());
    BigDecimal amount = BigDecimal.valueOf(100.50);

    account.deposit(amount);

    List<Event> newEvents = account.getNewEvents();
    assertThat(newEvents.size(), equalTo(2));
    assertThat(newEvents.get(1), instanceOf(AccountDepositedEvent.class));
    AccountDepositedEvent event = (AccountDepositedEvent) newEvents.get(1);
    assertThat(event.getBalance(), equalTo(amount));

    assertThat(account.getBalance(), equalTo(amount));
  }

  @Test
  void withdrawnAccountHasAccountWithdrawnEvent() {
    Account account = new Account(randomUUID(), randomUUID());
    account.deposit(BigDecimal.valueOf(30));

    account.withdraw(BigDecimal.valueOf(20));

    List<Event> newEvents = account.getNewEvents();
    assertThat(newEvents.size(), equalTo(3));
    assertThat(newEvents.get(2), instanceOf(AccountWithdrawnEvent.class));
    AccountWithdrawnEvent event = (AccountWithdrawnEvent) newEvents.get(2);
    assertThat(event.getBalance(), equalTo(TEN));

    assertThat(account.getBalance(), equalTo(TEN));
  }

  @Test
  void failsWithdrawalWithNonSufficientFunds() {
    Account account = new Account(randomUUID(), randomUUID());
    assertThrows(
        NonSufficientFundsException.class,
        () -> account.withdraw(BigDecimal.valueOf(1)));
  }
}
```

## File: `src/test/java/bankservice/domain/model/client/ClientTest.java`
```java
package bankservice.domain.model.client;

import static java.util.UUID.randomUUID;
import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.Matchers.equalTo;
import static org.hamcrest.Matchers.instanceOf;

import bankservice.domain.model.Event;
import java.util.List;
import java.util.UUID;
import org.junit.jupiter.api.Test;

class ClientTest {

  @Test
  void newClientHasBeenEnrolled() {
    UUID id = randomUUID();
    String name = "john";
    Email email = new Email("john@example.com");

    Client client = new Client(id, name, email);

    List<Event> newEvents = client.getNewEvents();
    assertThat(newEvents.size(), equalTo(1));
    assertThat(newEvents.get(0), instanceOf(ClientEnrolledEvent.class));
    ClientEnrolledEvent event = (ClientEnrolledEvent) newEvents.get(0);
    assertThat(event.getAggregateId(), equalTo(id));
    assertThat(event.getName(), equalTo(name));
    assertThat(event.getEmail(), equalTo(email));

    assertThat(client.getId(), equalTo(id));
    assertThat(client.getName(), equalTo(name));
    assertThat(client.getEmail(), equalTo(email));
  }
}
```

## File: `src/test/java/bankservice/domain/model/client/EmailSpecificationTest.java`
```java
package bankservice.domain.model.client;

import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.Matchers.equalTo;

import java.util.stream.Stream;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.Arguments;
import org.junit.jupiter.params.provider.MethodSource;

class EmailSpecificationTest {

  private final Email.EmailSpecification specification = new Email.EmailSpecification();

  @SuppressWarnings("unused")
  private static Stream<Arguments> emails() {
    return Stream.of(
        Arguments.of("email@example.com", true),
        Arguments.of("firstname.lastname@example.com", true),
        Arguments.of("email@subdomain.example.com", true),
        Arguments.of("firstname+lastname@example.com", true),
        Arguments.of("emailexample", false),
        Arguments.of("email@example", false),
        Arguments.of("email@-example.com", false),
        Arguments.of("email@example.web", false),
        Arguments.of("email@111.222.333.4444", false),
        Arguments.of("email@example..com", false),
        Arguments.of("abc..123@example.com", false)
    );
  }

  @MethodSource("emails")
  @ParameterizedTest
  void validate(String value, boolean isValid) {
    assertThat(specification.isSatisfiedBy(value), equalTo(isValid));
  }
}
```

## File: `src/test/java/bankservice/it/AccountIT.java`
```java
package bankservice.it;

import static java.util.UUID.randomUUID;
import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.Matchers.equalTo;

import com.fasterxml.jackson.databind.JsonNode;
import jakarta.ws.rs.core.Response;
import java.util.UUID;
import org.junit.jupiter.api.Test;

class AccountIT extends BaseIT {

  @Test
  void returnAccount() {
    String clientId = UUID.randomUUID().toString();
    String accountId = stateSetup.newAccount(clientId);
    Response response = resourcesClient.getAccount(accountId);
    JsonNode account = response.readEntity(JsonNode.class);
    assertThat(account.get("id").asText(), equalTo(accountId));
    assertThat(account.get("clientId").asText(), equalTo(clientId.toString()));
    assertThat(account.get("balance").asDouble(), equalTo(0.0));
    assertThat(response.getStatus(), equalTo(200));
  }

  @Test
  void returnAccountNotFound() {
    Response response = resourcesClient.getAccount(randomUUID().toString());
    response.close();
    assertThat(response.getStatus(), equalTo(404));
  }
}
```

## File: `src/test/java/bankservice/it/AccountTransactionsIT.java`
```java
package bankservice.it;

import static java.math.BigDecimal.ONE;
import static java.math.BigDecimal.TEN;
import static java.util.UUID.randomUUID;
import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.Matchers.equalTo;
import static org.hamcrest.Matchers.notNullValue;

import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.node.ArrayNode;
import jakarta.ws.rs.core.Response;
import java.math.BigDecimal;
import org.junit.jupiter.api.Test;

class AccountTransactionsIT extends BaseIT {

  @Test
  void returnEmptyTransactions() {
    Response response = resourcesClient.getAccountTransactions(randomUUID().toString());
    ArrayNode transactions = response.readEntity(ArrayNode.class);
    assertThat(transactions.size(), equalTo(0));
    assertThat(response.getStatus(), equalTo(200));
  }

  @Test
  void returnTransactions() {
    String accountId = stateSetup.newAccount(randomUUID().toString());
    resourcesClient.postDeposit(accountId, resourcesDtos.depositDto(BigDecimal.valueOf(99)))
        .close();
    resourcesClient.postDeposit(accountId, resourcesDtos.depositDto(ONE)).close();
    resourcesClient.postWithdrawal(accountId, resourcesDtos.withdrawalDto(TEN)).close();

    Response response = resourcesClient.getAccountTransactions(accountId);
    ArrayNode transactions = response.readEntity(ArrayNode.class);
    assertThat(transactions.size(), equalTo(3));
    verifyTransaction(transactions.get(0), "DEPOSIT", 99.0);
    verifyTransaction(transactions.get(1), "DEPOSIT", 1.0);
    verifyTransaction(transactions.get(2), "WITHDRAWAL", 10.0);
    assertThat(response.getStatus(), equalTo(200));
  }

  private void verifyTransaction(JsonNode transaction, String type, double amount) {
    assertThat(transaction.get("type").asText(), equalTo(type));
    assertThat(transaction.get("amount").asDouble(), equalTo(amount));
    assertThat(transaction.get("timestamp"), notNullValue());
  }
}
```

## File: `src/test/java/bankservice/it/AccountsIT.java`
```java
package bankservice.it;

import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.core.IsEqual.equalTo;
import static org.junit.jupiter.api.Assertions.assertTrue;

import jakarta.ws.rs.core.Response;
import java.util.ArrayList;
import org.glassfish.jersey.uri.UriTemplate;
import org.junit.jupiter.api.Test;

class AccountsIT extends BaseIT {

  @Test
  void newAccount() {
    String clientId = stateSetup.newClient("John", "john@example.com");
    Response response = resourcesClient.postAccount(resourcesDtos.accountDto(clientId));
    response.close();
    assertThat(response.getStatus(), equalTo(201));
    UriTemplate accountUriTemplate = resourcesClient.getResourcesUrls().accountUriTemplate();
    assertTrue(accountUriTemplate.match(response.getHeaderString("Location"), new ArrayList<>()));
  }
}
```

## File: `src/test/java/bankservice/it/BaseIT.java`
```java
package bankservice.it;

import static io.dropwizard.testing.ResourceHelpers.resourceFilePath;

import bankservice.bootstrap.BankServiceApplication;
import bankservice.it.client.ResourcesClient;
import bankservice.it.client.ResourcesDtos;
import bankservice.it.setup.StateSetup;
import io.dropwizard.core.Configuration;
import io.dropwizard.testing.junit5.DropwizardAppExtension;
import io.dropwizard.testing.junit5.DropwizardExtensionsSupport;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.extension.ExtendWith;

@ExtendWith(DropwizardExtensionsSupport.class)
abstract class BaseIT {

  protected static final DropwizardAppExtension<Configuration> BANK_SERVICE =
      new DropwizardAppExtension<>(BankServiceApplication.class,
          resourceFilePath("integration.yml"));

  protected static ResourcesClient resourcesClient;
  protected static ResourcesDtos resourcesDtos;
  protected static StateSetup stateSetup;

  @BeforeAll
  public static void setUpBaseClass() {
    resourcesClient = new ResourcesClient(BANK_SERVICE.getEnvironment(),
        BANK_SERVICE.getLocalPort());
    resourcesDtos = new ResourcesDtos(BANK_SERVICE.getObjectMapper());
    stateSetup = new StateSetup(resourcesClient, resourcesDtos);
  }
}
```

## File: `src/test/java/bankservice/it/ClientAccountsIT.java`
```java
package bankservice.it;

import static java.math.BigDecimal.TEN;
import static java.util.Collections.emptyMap;
import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.Matchers.equalTo;

import com.fasterxml.jackson.databind.node.ArrayNode;
import jakarta.ws.rs.core.Response;
import java.math.BigDecimal;
import java.util.HashMap;
import java.util.Map;
import java.util.UUID;
import org.junit.jupiter.api.Test;

class ClientAccountsIT extends BaseIT {

  @Test
  void returnClientAccounts() {
    String clientId = UUID.randomUUID().toString();
    verifyClientAccounts(clientId, emptyMap());

    String accountId1 = stateSetup.newAccountWithBalance(clientId, BigDecimal.valueOf(100));
    String accountId2 = stateSetup.newAccountWithBalance(clientId, BigDecimal.valueOf(100));
    String accountId3 = stateSetup.newAccountWithBalance(clientId, BigDecimal.valueOf(100));
    resourcesClient.postWithdrawal(accountId2, resourcesDtos.withdrawalDto(TEN)).close();
    resourcesClient.postDeposit(accountId3, resourcesDtos.depositDto(BigDecimal.valueOf(0.01)))
        .close();

    Map<String, BigDecimal> expectedAccountsBalances = new HashMap<>();
    expectedAccountsBalances.put(accountId1, BigDecimal.valueOf(100.0));
    expectedAccountsBalances.put(accountId2, BigDecimal.valueOf(90.0));
    expectedAccountsBalances.put(accountId3, BigDecimal.valueOf(100.01));
    verifyClientAccounts(clientId, expectedAccountsBalances);
  }

  private void verifyClientAccounts(String clientId,
      Map<String, BigDecimal> expectedAccountsBalances) {
    Response response = resourcesClient.getClientAccounts(clientId);
    ArrayNode accounts = response.readEntity(ArrayNode.class);

    accounts.forEach(account -> {
      String accountId = account.get("accountId").asText();
      BigDecimal balance = new BigDecimal(account.get("balance").asText());
      assertThat(balance, equalTo(expectedAccountsBalances.get(accountId)));
    });
  }
}
```

## File: `src/test/java/bankservice/it/ClientIT.java`
```java
package bankservice.it;

import static java.util.UUID.randomUUID;
import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.core.IsEqual.equalTo;

import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.node.ObjectNode;
import jakarta.ws.rs.core.Response;
import org.junit.jupiter.api.Test;

class ClientIT extends BaseIT {

  @Test
  void returnClient() {
    String name = "Jensen";
    String email = "jensen@example.com";
    String clientId = stateSetup.newClient(name, email);
    Response response = resourcesClient.getClient(clientId);
    JsonNode client = response.readEntity(JsonNode.class);
    assertThat(client.get("id").textValue(), equalTo(clientId));
    assertThat(client.get("name").textValue(), equalTo(name));
    assertThat(client.get("email").textValue(), equalTo(email));
  }

  @Test
  void returnClientNotFound() {
    Response response = resourcesClient.getClient(randomUUID().toString());
    response.close();
    assertThat(response.getStatus(), equalTo(404));
  }

  @Test
  void updateClient() {
    String clientId = stateSetup.newClient("Jaya", "jaya@example.com");
    String newName = "Jayan";
    String newEmail = "jayan@example.com";
    {
      ObjectNode clientDto = resourcesDtos.clientDto(newName, newEmail);
      Response response = resourcesClient.putClient(clientId, clientDto);
      response.close();
      assertThat(response.getStatus(), equalTo(204));
    }
    {
      Response response = resourcesClient.getClient(clientId);
      JsonNode clientDto = response.readEntity(JsonNode.class);
      assertThat(clientDto.get("name").textValue(), equalTo(newName));
      assertThat(clientDto.get("email").textValue(), equalTo(newEmail));
    }
  }
}
```

## File: `src/test/java/bankservice/it/ClientsIT.java`
```java
package bankservice.it;

import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.core.IsEqual.equalTo;
import static org.junit.jupiter.api.Assertions.assertTrue;

import com.fasterxml.jackson.databind.node.ObjectNode;
import jakarta.ws.rs.core.Response;
import java.util.ArrayList;
import org.glassfish.jersey.uri.UriTemplate;
import org.junit.jupiter.api.Test;

class ClientsIT extends BaseIT {

  @Test
  void newClient() {
    ObjectNode clientDto = resourcesDtos.clientDto("John", "john@example.com");
    Response response = resourcesClient.postClient(clientDto);
    response.close();
    assertThat(response.getStatus(), equalTo(201));
    UriTemplate clientUriTemplate = resourcesClient.getResourcesUrls().clientUriTemplate();
    assertTrue(clientUriTemplate.match(response.getHeaderString("Location"), new ArrayList<>()));
  }
}
```

## File: `src/test/java/bankservice/it/DepositsIT.java`
```java
package bankservice.it;

import static java.math.BigDecimal.TEN;
import static java.util.UUID.randomUUID;
import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.Matchers.equalTo;

import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.node.ObjectNode;
import jakarta.ws.rs.core.Response;
import java.math.BigDecimal;
import org.junit.jupiter.api.Test;

class DepositsIT extends BaseIT {

  @Test
  void returnAccountNotFound() {
    ObjectNode deposit = resourcesDtos.depositDto(TEN);
    Response response = resourcesClient.postDeposit(randomUUID().toString(), deposit);
    response.close();
    assertThat(response.getStatus(), equalTo(404));
  }

  @Test
  void depositAccount() {
    String accountId = stateSetup.newAccount(randomUUID().toString());
    BigDecimal amount = TEN;
    {
      ObjectNode deposit = resourcesDtos.depositDto(amount);
      Response response = resourcesClient.postDeposit(accountId, deposit);
      response.close();
      assertThat(response.getStatus(), equalTo(204));
    }
    {
      Response response = resourcesClient.getAccount(accountId);
      JsonNode account = response.readEntity(JsonNode.class);
      assertThat(account.get("balance").asDouble(), equalTo(amount.doubleValue()));
      assertThat(response.getStatus(), equalTo(200));
    }
  }
}
```

## File: `src/test/java/bankservice/it/ExceptionMappersIT.java`
```java
package bankservice.it;


import static org.junit.jupiter.api.Assertions.assertTrue;

import bankservice.port.incoming.adapter.resources.OptimisticLockingExceptionMapper;
import bankservice.port.incoming.adapter.resources.accounts.AccountNotFoundExceptionMapper;
import java.util.Set;
import org.junit.jupiter.api.Test;

class ExceptionMappersIT extends BaseIT {

  @Test
  void registeredExceptionMappers() {
    Set<Class<?>> classes = BANK_SERVICE.getEnvironment().jersey().getResourceConfig().getClasses();
    assertTrue(classes.contains(OptimisticLockingExceptionMapper.class));
    assertTrue(classes.contains(AccountNotFoundExceptionMapper.class));
  }
}
```

## File: `src/test/java/bankservice/it/HealthCheckIT.java`
```java
package bankservice.it;

import static jakarta.ws.rs.core.UriBuilder.fromUri;
import static java.util.logging.Level.INFO;
import static java.util.logging.Logger.getLogger;
import static org.glassfish.jersey.logging.LoggingFeature.DEFAULT_LOGGER_NAME;
import static org.glassfish.jersey.logging.LoggingFeature.Verbosity.PAYLOAD_ANY;
import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.core.IsEqual.equalTo;

import io.dropwizard.client.JerseyClientBuilder;
import jakarta.ws.rs.client.Client;
import jakarta.ws.rs.core.Response;
import java.net.URI;
import org.glassfish.jersey.logging.LoggingFeature;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Test;

class HealthCheckIT extends BaseIT {

  private static Client client;

  @BeforeAll
  static void setUpClass() {
    client = new JerseyClientBuilder(BANK_SERVICE.getEnvironment())
        .build(HealthCheckIT.class.getName())
        .register(new LoggingFeature(getLogger(DEFAULT_LOGGER_NAME), INFO, PAYLOAD_ANY, 1024));
  }

  @Test
  void overallHealth() {
    Response response = client.target(healthCheckUrl()).request().get();
    response.close();
    assertThat(response.getStatus(), equalTo(200));
  }

  private URI healthCheckUrl() {
    return fromUri("http://localhost").port(BANK_SERVICE.getAdminPort()).path("healthcheck")
        .build();
  }
}
```

## File: `src/test/java/bankservice/it/WithdrawalsIT.java`
```java
package bankservice.it;

import static java.math.BigDecimal.TEN;
import static java.util.UUID.randomUUID;
import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.Matchers.equalTo;

import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.node.ObjectNode;
import jakarta.ws.rs.core.Response;
import java.math.BigDecimal;
import org.junit.jupiter.api.Test;

class WithdrawalsIT extends BaseIT {

  @Test
  void returnAccountNotFound() {
    ObjectNode deposit = resourcesDtos.withdrawalDto(TEN);
    Response response = resourcesClient.postWithdrawal(randomUUID().toString(), deposit);
    response.close();
    assertThat(response.getStatus(), equalTo(404));
  }

  @Test
  void withdrawAccount() {
    BigDecimal previousBalance = BigDecimal.valueOf(9.99);
    BigDecimal withdrawalAmount = BigDecimal.valueOf(5.55);
    BigDecimal expectedBalance = BigDecimal.valueOf(4.44);
    String accountId = stateSetup.newAccountWithBalance(randomUUID().toString(), previousBalance);
    {
      ObjectNode withdrawal = resourcesDtos.withdrawalDto(withdrawalAmount);
      Response response = resourcesClient.postWithdrawal(accountId, withdrawal);
      response.close();
      assertThat(response.getStatus(), equalTo(204));
    }
    {
      Response response = resourcesClient.getAccount(accountId);
      JsonNode account = response.readEntity(JsonNode.class);
      assertThat(account.get("balance").asDouble(), equalTo(expectedBalance.doubleValue()));
      assertThat(response.getStatus(), equalTo(200));
    }
  }

  @Test
  void returnBadRequestForNonSufficientFunds() {
    String accountId = stateSetup.newAccount(randomUUID().toString());
    ObjectNode withdrawal = resourcesDtos.withdrawalDto(BigDecimal.valueOf(1000));
    Response response = resourcesClient.postWithdrawal(accountId, withdrawal);
    response.close();
    assertThat(response.getStatus(), equalTo(400));
  }
}
```

## File: `src/test/java/bankservice/it/client/ResourcesClient.java`
```java
package bankservice.it.client;

import static com.google.common.base.Preconditions.checkNotNull;
import static jakarta.ws.rs.client.Entity.json;
import static java.util.logging.Level.INFO;
import static java.util.logging.Logger.getLogger;
import static org.glassfish.jersey.client.ClientProperties.CONNECT_TIMEOUT;
import static org.glassfish.jersey.client.ClientProperties.READ_TIMEOUT;
import static org.glassfish.jersey.logging.LoggingFeature.DEFAULT_LOGGER_NAME;
import static org.glassfish.jersey.logging.LoggingFeature.Verbosity.PAYLOAD_ANY;

import com.fasterxml.jackson.databind.JsonNode;
import io.dropwizard.client.JerseyClientBuilder;
import io.dropwizard.core.setup.Environment;
import jakarta.ws.rs.client.Client;
import jakarta.ws.rs.core.Response;
import org.glassfish.jersey.logging.LoggingFeature;

public class ResourcesClient {

  private final Client client;
  private final ResourcesUrls resourcesUrls;

  public ResourcesClient(Environment environment, int port) {
    this.client = new JerseyClientBuilder(checkNotNull(environment))
        .build(ResourcesClient.class.getName())
        .property(CONNECT_TIMEOUT, 2000)
        .property(READ_TIMEOUT, 3000)
        .register(new LoggingFeature(getLogger(DEFAULT_LOGGER_NAME), INFO, PAYLOAD_ANY, 1024));
    this.resourcesUrls = new ResourcesUrls(port);
  }

  public ResourcesUrls getResourcesUrls() {
    return resourcesUrls;
  }

  public Response postClient(JsonNode clientDto) {
    return client.target(resourcesUrls.clientsUrl()).request().post(json(clientDto));
  }

  public Response getClient(String clientId) {
    return client.target(resourcesUrls.clientUrl(clientId)).request().get();
  }

  public Response putClient(String clientId, JsonNode clientDto) {
    return client.target(resourcesUrls.clientUrl(clientId)).request().put(json(clientDto));
  }

  public Response postAccount(JsonNode accountDto) {
    return client.target(resourcesUrls.accountsUrl()).request().post(json(accountDto));
  }

  public Response getAccount(String accountId) {
    return client.target(resourcesUrls.accountUrl(accountId)).request().get();
  }

  public Response postDeposit(String accountId, JsonNode depositDto) {
    return client.target(resourcesUrls.depositsUrl(accountId)).request().post(json(depositDto));
  }

  public Response postWithdrawal(String accountId, JsonNode withdrawalDto) {
    return client.target(resourcesUrls.withdrawalsUrl(accountId)).request()
        .post(json(withdrawalDto));
  }

  public Response getClientAccounts(String clientId) {
    return client.target(resourcesUrls.clientAccountsUrl(clientId)).request().get();
  }

  public Response getAccountTransactions(String accountId) {
    return client.target(resourcesUrls.accountTransactionsUrl(accountId)).request().get();
  }
}
```

## File: `src/test/java/bankservice/it/client/ResourcesDtos.java`
```java
package bankservice.it.client;

import static com.google.common.base.Preconditions.checkNotNull;

import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.node.ObjectNode;
import java.math.BigDecimal;

public class ResourcesDtos {

  private final ObjectMapper objectMapper;

  public ResourcesDtos(ObjectMapper objectMapper) {
    this.objectMapper = checkNotNull(objectMapper);
  }

  public ObjectNode clientDto(String name, String email) {
    ObjectNode newClientDto = objectMapper.createObjectNode();
    return newClientDto.put("name", name).put("email", email);
  }

  public JsonNode accountDto(String clientId) {
    ObjectNode newAccountDto = objectMapper.createObjectNode();
    return newAccountDto.put("clientId", clientId);
  }

  public ObjectNode depositDto(BigDecimal amount) {
    ObjectNode newAccountDto = objectMapper.createObjectNode();
    return newAccountDto.put("amount", amount.doubleValue());
  }

  public ObjectNode withdrawalDto(BigDecimal amount) {
    ObjectNode newAccountDto = objectMapper.createObjectNode();
    return newAccountDto.put("amount", amount.doubleValue());
  }
}
```

## File: `src/test/java/bankservice/it/client/ResourcesUrls.java`
```java
package bankservice.it.client;

import static com.google.common.base.Preconditions.checkArgument;
import static jakarta.ws.rs.core.UriBuilder.fromUri;
import static java.lang.String.format;

import java.net.URI;
import org.glassfish.jersey.uri.UriTemplate;

public class ResourcesUrls {

  private int port;

  public ResourcesUrls(int port) {
    checkArgument(port > 0);
    this.port = port;
  }

  public URI clientsUrl() {
    return fromUri("http://localhost").port(port).path("clients").build();
  }

  public URI clientUrl(String clientId) {
    return fromUri(clientUriTemplate().createURI(clientId)).build();
  }

  public UriTemplate clientUriTemplate() {
    return new UriTemplate(format("http://localhost:%d/clients/{id}", port));
  }

  public URI accountsUrl() {
    return fromUri("http://localhost").port(port).path("accounts").build();
  }

  public URI accountUrl(String accountId) {
    return fromUri(accountUriTemplate().createURI(accountId)).build();
  }

  public UriTemplate accountUriTemplate() {
    return new UriTemplate(format("http://localhost:%d/accounts/{id}", port));
  }

  public URI depositsUrl(String accountId) {
    return fromUri("http://localhost").port(port)
        .path("accounts").path("{id}").path("deposits").build(accountId);
  }

  public URI withdrawalsUrl(String accountId) {
    return fromUri("http://localhost").port(port)
        .path("accounts").path("{id}").path("withdrawals").build(accountId);
  }

  public URI clientAccountsUrl(String clientId) {
    return fromUri("http://localhost").port(port).path("clients").path("{id}").path("accounts")
        .build(clientId.toString());
  }

  public URI accountTransactionsUrl(String accountId) {
    return fromUri("http://localhost").port(port)
        .path("accounts").path("{id}").path("transactions").build(accountId);
  }
}
```

## File: `src/test/java/bankservice/it/setup/StateSetup.java`
```java
package bankservice.it.setup;

import static com.google.common.base.Preconditions.checkNotNull;
import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.Matchers.equalTo;
import static org.junit.jupiter.api.Assertions.assertTrue;

import bankservice.it.client.ResourcesClient;
import bankservice.it.client.ResourcesDtos;
import com.fasterxml.jackson.databind.node.ObjectNode;
import jakarta.ws.rs.core.Response;
import java.math.BigDecimal;
import java.util.HashMap;
import java.util.Map;
import org.glassfish.jersey.uri.UriTemplate;

public class StateSetup {

  private final ResourcesClient resourcesClient;
  private final ResourcesDtos resourcesDtos;

  public StateSetup(ResourcesClient resourcesClient, ResourcesDtos resourcesDtos) {
    this.resourcesClient = checkNotNull(resourcesClient);
    this.resourcesDtos = checkNotNull(resourcesDtos);
  }

  public String newClient(String name, String email) {
    ObjectNode clientDto = resourcesDtos.clientDto(name, email);
    Response response = resourcesClient.postClient(clientDto);
    response.close();
    assertThat(response.getStatus(), equalTo(201));
    Map<String, String> params = new HashMap<>();
    UriTemplate clientUriTemplate = resourcesClient.getResourcesUrls().clientUriTemplate();
    assertTrue(clientUriTemplate.match(response.getHeaderString("Location"), params));
    return params.get("id");
  }

  public String newAccount(String clientId) {
    Response response = resourcesClient.postAccount(resourcesDtos.accountDto(clientId));
    response.close();
    assertThat(response.getStatus(), equalTo(201));
    Map<String, String> params = new HashMap<>();
    UriTemplate accountUriTemplate = resourcesClient.getResourcesUrls().accountUriTemplate();
    assertTrue(accountUriTemplate.match(response.getHeaderString("Location"), params));
    return params.get("id");
  }

  public String newAccountWithBalance(String clientId, BigDecimal balance) {
    String accountId = newAccount(clientId);
    ObjectNode deposit = resourcesDtos.depositDto(balance);
    Response response = resourcesClient.postDeposit(accountId, deposit);
    response.close();
    assertThat(response.getStatus(), equalTo(204));
    return accountId;
  }
}
```

## File: `src/test/java/bankservice/port/incoming/adapter/resources/OptimisticLockingExceptionMapperTest.java`
```java
package bankservice.port.incoming.adapter.resources;

import static jakarta.ws.rs.client.Entity.json;
import static jakarta.ws.rs.core.MediaType.APPLICATION_JSON;
import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.Matchers.equalTo;

import bankservice.domain.model.OptimisticLockingException;
import io.dropwizard.testing.junit5.DropwizardExtensionsSupport;
import io.dropwizard.testing.junit5.ResourceExtension;
import jakarta.ws.rs.Consumes;
import jakarta.ws.rs.PUT;
import jakarta.ws.rs.Path;
import jakarta.ws.rs.core.Response;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;

@ExtendWith(DropwizardExtensionsSupport.class)
class OptimisticLockingExceptionMapperTest {

  static final ResourceExtension RESOURCES = ResourceExtension.builder()
      .addProvider(OptimisticLockingExceptionMapper.class)
      .addResource(new ConcurrentlyModifiedResource())
      .build();

  @Test
  void returnConflict() {
    Response response = RESOURCES.client()
        .target("/concurrently-modified-resource")
        .request().put(json("{}"));
    response.close();
    assertThat(response.getStatus(), equalTo(409));
  }

  @Consumes(APPLICATION_JSON)
  @Path("/concurrently-modified-resource")
  public static class ConcurrentlyModifiedResource {

    @PUT
    public Response put(String entity) throws OptimisticLockingException {
      throw new OptimisticLockingException("Testing exception mapper");
    }
  }
}
```

## File: `src/test/java/bankservice/port/incoming/adapter/resources/accounts/AccountNotFoundExceptionMapperTest.java`
```java
package bankservice.port.incoming.adapter.resources.accounts;

import static bankservice.port.incoming.adapter.resources.accounts.AccountNotFoundExceptionMapperTest.NeverFoundAccountResource.calls;
import static jakarta.ws.rs.core.MediaType.APPLICATION_JSON;
import static java.lang.String.format;
import static java.util.UUID.randomUUID;
import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.Matchers.equalTo;

import bankservice.service.account.AccountNotFoundException;
import io.dropwizard.testing.junit5.DropwizardExtensionsSupport;
import io.dropwizard.testing.junit5.ResourceExtension;
import jakarta.ws.rs.GET;
import jakarta.ws.rs.Path;
import jakarta.ws.rs.PathParam;
import jakarta.ws.rs.Produces;
import jakarta.ws.rs.core.Response;
import java.util.UUID;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;

@ExtendWith(DropwizardExtensionsSupport.class)
class AccountNotFoundExceptionMapperTest {

  static final ResourceExtension RESOURCES = ResourceExtension.builder()
      .addProvider(AccountNotFoundExceptionMapper.class)
      .addResource(new NeverFoundAccountResource())
      .build();

  @Test
  void returnNotFound() {
    Response response = RESOURCES.client()
        .target(format("/never-found-account-resource/%s", randomUUID()))
        .request().get();
    response.close();
    assertThat(response.getStatus(), equalTo(404));
    assertThat(calls, equalTo(1));
  }

  @Produces(APPLICATION_JSON)
  @Path("/never-found-account-resource/{id}")
  public static class NeverFoundAccountResource {

    static int calls = 0;

    @GET
    public Response get(@PathParam("id") String id) throws AccountNotFoundException {
      calls++;
      throw new AccountNotFoundException(UUID.fromString(id));
    }
  }
}
```

## File: `src/test/java/bankservice/port/outgoing/adapter/eventstore/InMemoryEventStoreTest.java`
```java
package bankservice.port.outgoing.adapter.eventstore;

import static com.google.common.collect.Lists.newArrayList;
import static java.time.ZoneOffset.UTC;
import static java.time.ZonedDateTime.now;
import static java.util.UUID.randomUUID;
import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.Matchers.equalTo;
import static org.junit.jupiter.api.Assertions.assertThrows;
import static org.mockito.Mockito.mock;

import bankservice.domain.model.Event;
import bankservice.domain.model.EventStore;
import bankservice.domain.model.OptimisticLockingException;
import java.util.List;
import java.util.UUID;
import org.junit.jupiter.api.Test;

class InMemoryEventStoreTest {

  private EventStore eventStore = new InMemoryEventStore();

  @Test
  void storeEventsInOrder() {
    UUID aggregateId = randomUUID();
    Event e1 = new Event(aggregateId, now(UTC), 1) {
    };
    Event e2 = new Event(aggregateId, now(UTC), 2) {
    };
    Event e3 = new Event(aggregateId, now(UTC), 3) {
    };
    eventStore.store(aggregateId, newArrayList(e1), 0);
    eventStore.store(aggregateId, newArrayList(e2), 1);
    eventStore.store(aggregateId, newArrayList(e3), 2);

    List<Event> eventStream = eventStore.load(aggregateId);
    assertThat(eventStream.size(), equalTo(3));
    assertThat(eventStream.get(0), equalTo(e1));
    assertThat(eventStream.get(1), equalTo(e2));
    assertThat(eventStream.get(2), equalTo(e3));
  }

  @Test
  void optimisticLocking() {
    UUID aggregateId = randomUUID();
    Event e1 = new Event(aggregateId, now(UTC), 1) {
    };
    Event e2 = new Event(aggregateId, now(UTC), 2) {
    };
    Event e3 = new Event(aggregateId, now(UTC), 2) {
    };
    eventStore.store(aggregateId, newArrayList(e1), 0);
    eventStore.store(aggregateId, newArrayList(e2), 1);
    assertThrows(
        OptimisticLockingException.class,
        () -> eventStore.store(aggregateId, newArrayList(e3), 1)
    );
  }

  @Test
  void loadedEventStreamIsImmutable() {
    UUID aggregateId = randomUUID();
    Event e1 = new Event(aggregateId, now(UTC), 1) {
    };
    eventStore.store(aggregateId, newArrayList(e1), 0);
    assertThrows(
        UnsupportedOperationException.class,
        () -> eventStore.load(aggregateId).add(mock(Event.class))
    );
  }
}
```

## File: `src/test/java/bankservice/projection/accounttransactions/InMemoryTransactionsRepositoryTest.java`
```java
package bankservice.projection.accounttransactions;

import static bankservice.projection.accounttransactions.TransactionProjection.TransactionType.DEPOSIT;
import static java.math.BigDecimal.ONE;
import static java.math.BigDecimal.TEN;
import static java.time.ZoneOffset.UTC;
import static java.time.ZonedDateTime.now;
import static java.util.UUID.randomUUID;
import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.Matchers.equalTo;

import java.util.List;
import java.util.UUID;
import org.junit.jupiter.api.Test;

class InMemoryTransactionsRepositoryTest {

  private TransactionsRepository transactionsRepository =
      new InMemoryTransactionsRepository();

  @Test
  void listEventsSortedByVersion() {
    UUID accountId = randomUUID();
    TransactionProjection tx2 = new TransactionProjection(accountId, DEPOSIT, TEN, now(UTC), 2);
    TransactionProjection tx1 = new TransactionProjection(accountId, DEPOSIT, ONE, now(UTC), 1);
    transactionsRepository.save(tx2);
    transactionsRepository.save(tx1);

    List<TransactionProjection> transactions = transactionsRepository.listByAccount(accountId);
    assertThat(transactions.get(0), equalTo(tx1));
    assertThat(transactions.get(1), equalTo(tx2));
  }
}
```

## File: `src/test/java/bankservice/projection/clientaccounts/InMemoryAccountsRepositoryTest.java`
```java
package bankservice.projection.clientaccounts;

import static java.math.BigDecimal.ONE;
import static java.math.BigDecimal.TEN;
import static java.math.BigDecimal.ZERO;
import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.Matchers.equalTo;

import java.util.UUID;
import org.junit.jupiter.api.Test;

class InMemoryAccountsRepositoryTest {

  private AccountsRepository accountsRepository =
      new InMemoryAccountsRepository();

  @Test
  void ignoreEventOutOfOrder() {
    UUID clientId = UUID.randomUUID();
    UUID accountId = UUID.randomUUID();
    accountsRepository.save(new AccountProjection(accountId, clientId, ZERO, 1));
    accountsRepository.updateBalance(accountId, TEN, 3);
    accountsRepository.updateBalance(accountId, ONE, 2);
    assertThat(accountsRepository.getAccounts(clientId).get(0).getBalance(), equalTo(TEN));
  }
}
```

## File: `src/test/java/bankservice/service/RetrierTest.java`
```java
package bankservice.service;

import static java.util.Collections.singletonList;
import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.Matchers.instanceOf;
import static org.junit.jupiter.api.Assertions.fail;
import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.times;
import static org.mockito.Mockito.verify;
import static org.mockito.Mockito.when;

import java.util.function.Supplier;
import org.junit.jupiter.api.Test;

class RetrierTest {

  private RuntimeException exceptionToRetryOn = new IllegalStateException();
  private int maxAttempts = 10;
  private Retrier retrier = new Retrier(singletonList(exceptionToRetryOn.getClass()), maxAttempts);

  @Test
  void retriesGetUpToMaxAttemptsWithoutSharedStateBetweenCalls() {
    retryGetUpToMaxAttempts();
    retryGetUpToMaxAttempts();
  }

  private void retryGetUpToMaxAttempts() {
    Supplier supplier = mock(Supplier.class);
    when(supplier.get()).thenThrow(exceptionToRetryOn);
    try {
      retrier.get(() -> supplier.get());
      fail("Should have thrown exception after max attempts");
    } catch (RuntimeException e) {
      verify(supplier, times(maxAttempts)).get();
      assertThat(e, instanceOf(exceptionToRetryOn.getClass()));
    }
  }
}
```

## File: `src/test/java/bankservice/service/account/AccountServiceTest.java`
```java
package bankservice.service.account;

import static java.math.BigDecimal.ONE;
import static java.math.BigDecimal.TEN;
import static java.util.UUID.randomUUID;
import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.Matchers.equalTo;
import static org.mockito.ArgumentMatchers.anyList;
import static org.mockito.ArgumentMatchers.eq;
import static org.mockito.Mockito.anyInt;
import static org.mockito.Mockito.doThrow;
import static org.mockito.Mockito.spy;
import static org.mockito.Mockito.times;
import static org.mockito.Mockito.verify;

import bankservice.domain.model.EventStore;
import bankservice.domain.model.OptimisticLockingException;
import bankservice.domain.model.account.Account;
import bankservice.domain.model.account.AccountDepositedEvent;
import bankservice.domain.model.account.AccountOpenedEvent;
import bankservice.domain.model.account.AccountWithdrawnEvent;
import bankservice.port.outgoing.adapter.eventstore.InMemoryEventStore;
import com.google.common.eventbus.EventBus;
import com.google.common.eventbus.Subscribe;
import java.util.Map;
import java.util.UUID;
import java.util.concurrent.ConcurrentHashMap;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

class AccountServiceTest {

  private EventStore eventStore;
  private EventBusCounter eventBusCounter;
  private AccountService accountService;

  @BeforeEach
  void setUp() {
    eventStore = spy(new InMemoryEventStore());
    EventBus eventBus = new EventBus();
    eventBusCounter = new EventBusCounter();
    eventBus.register(eventBusCounter);
    accountService = new AccountService(eventStore, eventBus);
  }

  @Test
  void retryOnAccountWithdrawalConflictsUpToThreeAttempts() {
    Account account = accountService.process(new OpenAccountCommand(randomUUID()));
    UUID id = account.getId();
    accountService.process(new DepositAccountCommand(id, TEN));
    doThrow(OptimisticLockingException.class)
        .doThrow(OptimisticLockingException.class)
        .doCallRealMethod()
        .when(eventStore).store(eq(id), anyList(), anyInt());

    accountService.process(new WithdrawAccountCommand(id, ONE));
    int creationAttempts = 1;
    int depositAttempts = 1;
    int withdrawalAttempts = 3;
    int loadTimes = depositAttempts + withdrawalAttempts;
    int storeTimes = creationAttempts + depositAttempts + withdrawalAttempts;
    verify(eventStore, times(loadTimes)).load(eq(id));
    verify(eventStore, times(storeTimes)).store(eq(id), anyList(), anyInt());
    assertThat(eventBusCounter.eventsCount.get(AccountOpenedEvent.class), equalTo(1));
    assertThat(eventBusCounter.eventsCount.get(AccountDepositedEvent.class), equalTo(1));
    assertThat(eventBusCounter.eventsCount.get(AccountWithdrawnEvent.class), equalTo(1));
    assertThat(eventBusCounter.eventsCount.size(), equalTo(3));
  }

  private static class EventBusCounter {

    Map<Class<?>, Integer> eventsCount = new ConcurrentHashMap<>();

    @Subscribe
    @SuppressWarnings("unused")
    public void handle(Object event) {
      eventsCount.merge(event.getClass(), 1, Integer::sum);
    }
  }
}
```

## File: `src/test/resources/integration.yml`
```yaml
server:
  applicationConnectors:
    - type: http
      port: 0
  adminConnectors:
    - type: http
      port: 0
```


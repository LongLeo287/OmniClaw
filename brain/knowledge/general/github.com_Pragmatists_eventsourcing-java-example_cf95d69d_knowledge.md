---
id: github.com-pragmatists-eventsourcing-java-example-
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:13.535873
---

# KNOWLEDGE EXTRACT: github.com_Pragmatists_eventsourcing-java-example_cf95d69d
> **Extracted on:** 2026-04-01 11:01:17
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007521168/github.com_Pragmatists_eventsourcing-java-example_cf95d69d

---

## File: `.floo`
```
{
    "url": "https://floobits.com/mlip/banking-event-sourcing"
}
```

## File: `.flooignore`
```
extern
node_modules
tmp
vendor
.idea/workspace.xml
.idea/misc.xml
```

## File: `.gitignore`
```
target/
.idea
*.iml
.floo*
```

## File: `README.md`
```markdown
# Event sourcing example in Java
A simplified (in memory) example of Event Sourcing implementation in Java for banking domain.
Repository is splitted into exercises adding step by step more functionality towards good design of event sourcing with CQRS.
You can play around and try to implement exercises or You can check out solution branches.


## Step 1 - In memory iplementation of event sourcing
![alt tag](https://raw.githubusercontent.com/michal-lipski/eventsourcing-example/master/event_store_exercise_1.png)
- Provide simple in-memory implementation of Event Store
- Make all test passing using event sourcing
#### soultion
 - branch [exercise_1_solution](https://github.com/michal-lipski/eventsourcing-example/tree/excercise_1_solution)

## Step 1a (optional) - Unit of work pattern
- Implement [Unit of Work](https://martinfowler.com/eaaCatalog/unitOfWork.html) pattern where events are stored outside of aggregate
#### soultion
 - WIP

## Step 1b (optional) - Projections
- Implement Projections on Account to get number of transactions performed on account
- eventStore.store() method shoud accept Event playload instead of domain Events
- what should be api of eventStream()?
#### soultion
 - WIP
 
## Step 2 (optional) - Optimistic locking
- add optimistic locking
#### soultion
 - WIP
 
## Step 3 - new Aggregate extraction
![alt tag](https://raw.githubusercontent.com/michal-lipski/eventsourcing-example/master/event_store_exercise_2.png)
- Refactor to move all money transfer related stuff to separate aggregate
- New aggregate will be also using Event Store
#### soultion
 - WIP
 
## Step 4 - adding CQRS
![alt tag](https://raw.githubusercontent.com/michal-lipski/eventsourcing-example/master/event_store_exercise_3.png)
- Apply CQRS rule and separate the command and reading side
- Solution will use Eventual Consistency approach
#### soultion
 - WIP
 
## Step 5
- Provide additional (not transient) implementation of Event Store. (https://geteventstore.com/)
#### soultion
 - WIP
```

## File: `pom.xml`
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
		 xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
		 xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
	<modelVersion>4.0.0</modelVersion>

	<groupId>com.pragmatists</groupId>
	<artifactId>banking-eventsourcing</artifactId>
	<packaging>pom</packaging>
	<version>1.0-SNAPSHOT</version>

	<modules>
		<module>banking</module>
		<module>eventsourcing</module>
	</modules>

	<build>
		<pluginManagement>
			<plugins>
				<plugin>
					<groupId>org.apache.maven.plugins</groupId>
					<artifactId>maven-compiler-plugin</artifactId>
					<configuration>
						<source>1.8</source>
						<target>1.8</target>
					</configuration>
				</plugin>
			</plugins>
		</pluginManagement>
	</build>
</project>
```

## File: `banking/pom.xml`
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
	<modelVersion>4.0.0</modelVersion>

	<parent>
		<groupId>com.pragmatists</groupId>
		<artifactId>banking-eventsourcing</artifactId>
		<version>1.0-SNAPSHOT</version>
	</parent>

	<groupId>com.pragmatists</groupId>
	<artifactId>banking</artifactId>
	<packaging>jar</packaging>

	<name>banking</name>
	<description>Demo project for Event Sourcing</description>

	<properties>
		<project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
		<project.reporting.outputEncoding>UTF-8</project.reporting.outputEncoding>
		<java.version>1.8</java.version>
	</properties>

	<dependencies>

		<dependency>
			<groupId>com.pragmatists</groupId>
			<artifactId>eventsourcing</artifactId>
			<version>${parent.version}</version>
		</dependency>
		<dependency>
			<groupId>org.springframework.boot</groupId>
			<artifactId>spring-boot-starter-web</artifactId>
			<version>1.5.2.RELEASE</version>
		</dependency>

		<dependency>
			<groupId>org.springframework.boot</groupId>
			<artifactId>spring-boot-starter-test</artifactId>
			<version>1.5.2.RELEASE</version>
			<scope>test</scope>
		</dependency>
		<dependency>
			<groupId>com.jayway.restassured</groupId>
			<artifactId>rest-assured</artifactId>
			<version>2.8.0</version>
			<scope>test</scope>
		</dependency>
	</dependencies>

	<build>
		<plugins>
			<plugin>
				<groupId>org.springframework.boot</groupId>
				<artifactId>spring-boot-maven-plugin</artifactId>
			</plugin>
		</plugins>
	</build>

</project>
```

## File: `banking/src/main/java/com/pragmatists/application/AccountController.java`
```java
package com.pragmatists.application;

import com.pragmatists.domain.BankingService;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;

import java.net.URI;

import static org.springframework.http.HttpStatus.NOT_FOUND;
import static org.springframework.http.MediaType.APPLICATION_JSON_VALUE;
import static org.springframework.http.ResponseEntity.*;
import static org.springframework.web.servlet.support.ServletUriComponentsBuilder.fromCurrentRequest;

@Controller
@RequestMapping("/account")
class AccountController {


    private final BankingService bankingService;

    AccountController(BankingService bankingService) {
        this.bankingService = bankingService;
    }

    @PostMapping
    ResponseEntity<?> createAccount(@RequestParam String owner) {
        //TODO add saving Account
        String id = "xxx";

        URI location = fromCurrentRequest().path("/{id}").buildAndExpand(id).toUri();
        return created(location).build();
    }

    @GetMapping(path = "/{id}", produces = APPLICATION_JSON_VALUE)
    ResponseEntity<AccountResource> getAccount(@PathVariable String id) {
        AccountResource accountResource = new AccountResource(id, "", "", 0);
        //TODO add fetching Account

        return ok(accountResource);
    }

    @PutMapping(path = "/{id}/withdraw")
    ResponseEntity<Void> withdraw(@PathVariable String id, @RequestParam String amount) {
        //TODO add withdraw functionality
        return ok().build();
    }

    @PutMapping(path = "/{id}/deposit")
    ResponseEntity<Void> deposit(@PathVariable String id, @RequestParam String amount) {
        //TODO add deposit functionality
        return ok().build();
    }

    @DeleteMapping(path = "/{id}")
    ResponseEntity<Void> closeAccount(@PathVariable String id) {
        //TODO add closing Account

        return noContent().build();
    }


    @ResponseStatus(NOT_FOUND)
    class AccountClosedException extends RuntimeException {

        public AccountClosedException(String accountId) {
            super("account closed: '" + accountId + "'.");
        }
    }

    @ResponseStatus(NOT_FOUND)
    class NotEnoughMoneyException extends RuntimeException {

        public NotEnoughMoneyException(String accountId) {
            super("not enough money: '" + accountId + "'.");
        }
    }

}
```

## File: `banking/src/main/java/com/pragmatists/application/AccountResource.java`
```java
package com.pragmatists.application;


public class AccountResource {
    private String accountId;
    private String number;
    private String owner;
    private Integer balance;

    public AccountResource() {
    }

    public AccountResource(String accountId, String number, String owner, Integer balance) {
        this.accountId = accountId;
        this.number = number;
        this.owner = owner;
        this.balance = balance;
    }

    public String getAccountId() {
        return accountId;
    }

    public String getNumber() {
        return number;
    }

    public String getOwner() {
        return owner;
    }

    public Integer getBalance() {
        return balance;
    }
}
```

## File: `banking/src/main/java/com/pragmatists/application/BankingApplication.java`
```java
package com.pragmatists.application;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
class BankingApplication {

	public static void main(String[] args) {
		SpringApplication.run(BankingApplication.class, args);
	}
}
```

## File: `banking/src/main/java/com/pragmatists/application/BankingConfig.java`
```java
package com.pragmatists.application;


import com.pragmatists.domain.AccountRepository;
import com.pragmatists.domain.BankingService;
import com.pragmatists.eventsourcing.memory.InMemoryEventStore;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
class BankingConfig {

    @Bean
    BankingService bankingService(){
        AccountRepository accountRepository = new AccountRepository(new InMemoryEventStore());
        return new BankingService(accountRepository);
    }
    @Bean
    AccountController accountController(){
        return new AccountController(bankingService());
    }

}
```

## File: `banking/src/main/java/com/pragmatists/domain/Account.java`
```java
package com.pragmatists.domain;


public class Account {

}
```

## File: `banking/src/main/java/com/pragmatists/domain/AccountId.java`
```java
package com.pragmatists.domain;

import com.pragmatists.eventsourcing.api.AggregateId;

import java.util.UUID;


public final class AccountId implements AggregateId {

    private final String value;

    private AccountId(String value) {
        this.value = value;
    }

    public static AccountId generate() {
        return new AccountId(UUID.randomUUID().toString());
    }

    public static AccountId from(String id) {
        return new AccountId(id);
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;

        AccountId accountId = (AccountId) o;

        return value != null ? value.equals(accountId.value) : accountId.value == null;
    }

    @Override
    public int hashCode() {
        return value != null ? value.hashCode() : 0;
    }

    @Override
    public String toString() {
        return value;
    }
}
```

## File: `banking/src/main/java/com/pragmatists/domain/AccountRepository.java`
```java
package com.pragmatists.domain;


import com.pragmatists.eventsourcing.api.EventStore;

public class AccountRepository {

    public AccountRepository(EventStore eventStore) {

    }
}
```

## File: `banking/src/main/java/com/pragmatists/domain/BankingService.java`
```java
package com.pragmatists.domain;

public class BankingService {

    private AccountRepository accounts;

    public BankingService(AccountRepository accounts) {

        this.accounts = accounts;
    }

}
```

## File: `banking/src/main/resources/application.properties`
```
server.port=9090
```

## File: `banking/src/test/java/com/pragmatists/application/AccountControllerTest.java`
```java
package com.pragmatists.application;

import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.web.client.TestRestTemplate;
import org.springframework.http.HttpEntity;
import org.springframework.http.HttpHeaders;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.util.LinkedMultiValueMap;
import org.springframework.util.MultiValueMap;

import java.net.URI;

import static org.assertj.core.api.Assertions.assertThat;
import static org.springframework.http.HttpMethod.DELETE;
import static org.springframework.http.HttpMethod.PUT;
import static org.springframework.http.HttpStatus.*;


@RunWith(SpringRunner.class)
@SpringBootTest(webEnvironment = SpringBootTest.WebEnvironment.RANDOM_PORT)
public class AccountControllerTest {

    @Autowired
    TestRestTemplate restTemplate;

    @Test
    public void create_account() {
        ResponseEntity<String> response = createAccount(request(param("owner", "john.doe@example.com")));

        assertThat(response.getStatusCode()).isEqualTo(CREATED);
        assertThat(response.getHeaders().getLocation()).isNotNull();
    }

    @Test
    public void get_account() {
        ResponseEntity<String> response = createAccount(request(param("owner", "john.doe@example.com")));

        ResponseEntity<AccountResource> accountResponse = getAccount(response.getHeaders().getLocation());

        assertThat(accountResponse.getStatusCode()).isEqualTo(OK);
        assertThat(accountResponse.getBody().getAccountId()).isNotNull();
        assertThat(accountResponse.getBody().getNumber()).isNotNull();
        assertThat(accountResponse.getBody().getOwner()).isEqualTo("john.doe@example.com");
        assertThat(accountResponse.getBody().getBalance()).isEqualTo(0);
    }

    @Test
    public void delete_account() {
        String accountId = createAccount();

        ResponseEntity<?> response = closeAccount(accountId);

        assertThat(response.getStatusCode()).isEqualTo(NO_CONTENT);

        ResponseEntity<AccountResource> account = getAccount(URI.create("/account/" + accountId));
        assertThat(account.getStatusCode()).isEqualTo(NOT_FOUND);
    }

    @Test
    public void deposit_account() {
        String accountId = createAccount();

        deposit(accountId, "10");
        deposit(accountId, "5");

        assertThat(getAccount(accountId).getBalance()).isEqualTo(15);
    }

    @Test
    public void withdraw_account() {
        String accountId = createAccount();

        deposit(accountId, "10");
        withdraw(accountId, "5");

        assertThat(getAccount(accountId).getBalance()).isEqualTo(5);
    }

    @Test
    public void cannot_withdraw_closed_account() {
        String accountId = createAccount();
        closeAccount(accountId);

        ResponseEntity<String> responseEntity = withdraw(accountId, "5");

        assertThat(responseEntity.getStatusCode()).isEqualTo(NOT_FOUND);
    }

    @Test
    public void cannot_withdraw_account_when_not_enought_money() {
        String accountId = createAccount();

        deposit(accountId, "5");
        ResponseEntity<String> responseEntity = withdraw(accountId, "10");

        assertThat(responseEntity.getStatusCode()).isEqualTo(NOT_FOUND);
        assertThat(getAccount(accountId).getBalance()).isEqualTo(5);
    }


    private void deposit(String accountId, String value) {
        restTemplate.put("/account/" + accountId + "/deposit", request(param("amount", value)));
    }

    private ResponseEntity<String> withdraw(String accountId, String value) {
        return restTemplate.exchange("/account/" + accountId + "/withdraw", PUT, request(param("amount", value)), String.class);
    }

    private HttpEntity<MultiValueMap<String, Object>> request(RequestParameter... requestParameter) {
        HttpHeaders headers = new HttpHeaders();
        headers.setContentType(MediaType.APPLICATION_FORM_URLENCODED);
        MultiValueMap<String, Object> map = new LinkedMultiValueMap<>();
        for (RequestParameter parameter : requestParameter) {
            map.add(parameter.name, parameter.value);
        }
        return new HttpEntity<>(map, headers);
    }


    private ResponseEntity<ResponseEntity> closeAccount(String accountId) {
        return restTemplate.exchange("/account/" + accountId, DELETE, request(), ResponseEntity.class);
    }


    private ResponseEntity<AccountResource> getAccount(URI uri) {
        return restTemplate.getForEntity(uri, AccountResource.class);
    }

    private RequestParameter param(String name, String value) {
        return new RequestParameter(name, value);
    }

    private AccountResource getAccount(String id) {
        return restTemplate.getForObject("/account/" + id, AccountResource.class);
    }


    private ResponseEntity<String> createAccount(HttpEntity<MultiValueMap<String, Object>> request) {
        return restTemplate.postForEntity("/account", request, String.class);
    }

    private String createAccount() {
        return restTemplate.postForEntity("/account", request(param("owner", "john.doe@example.com")), String.class).getHeaders().getLocation().getPath().split("/")[2];
    }

    private class RequestParameter {
        final String name;
        final String value;

        private RequestParameter(String name, String value) {
            this.name = name;
            this.value = value;
        }
    }
}
```

## File: `banking/src/test/java/com/pragmatists/application/BankingApplicationTests.java`
```java
package com.pragmatists.application;

import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit4.SpringRunner;

@RunWith(SpringRunner.class)
@SpringBootTest
public class BankingApplicationTests {

	@Test
	public void contextLoads() {
	}

}
```

## File: `eventsourcing/pom.xml`
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
		 xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
	<modelVersion>4.0.0</modelVersion>

	<parent>
		<groupId>com.pragmatists</groupId>
		<artifactId>banking-eventsourcing</artifactId>
		<version>1.0-SNAPSHOT</version>
	</parent>

	<groupId>com.pragmatists</groupId>
	<artifactId>eventsourcing</artifactId>
	<packaging>jar</packaging>

	<name>eventsourcing</name>
	<description>Event Sourcing</description>

	<properties>
		<project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
		<project.reporting.outputEncoding>UTF-8</project.reporting.outputEncoding>
		<java.version>1.8</java.version>
	</properties>


</project>
```

## File: `eventsourcing/src/main/java/com/pragmatists/eventsourcing/api/AggregateId.java`
```java
package com.pragmatists.eventsourcing.api;


public interface  AggregateId {

}
```

## File: `eventsourcing/src/main/java/com/pragmatists/eventsourcing/api/Command.java`
```java
package com.pragmatists.eventsourcing.api;


public interface Command {
    AggregateId aggregateId();
}
```

## File: `eventsourcing/src/main/java/com/pragmatists/eventsourcing/api/Event.java`
```java
package com.pragmatists.eventsourcing.api;


public interface Event {
    AggregateId getAggregateId();

    int getVersion();

    String getEventType();

}
```

## File: `eventsourcing/src/main/java/com/pragmatists/eventsourcing/api/EventStore.java`
```java
package com.pragmatists.eventsourcing.api;


import java.util.List;

public interface EventStore {
    EventStream loadEventStream(AggregateId aggregateId);
    void store(AggregateId aggregateId, long version, List<Event> events);

}
```

## File: `eventsourcing/src/main/java/com/pragmatists/eventsourcing/api/EventStream.java`
```java
package com.pragmatists.eventsourcing.api;


public interface EventStream extends Iterable<Event> {
    long version();
}
```

## File: `eventsourcing/src/main/java/com/pragmatists/eventsourcing/memory/InMemoryEventStore.java`
```java
package com.pragmatists.eventsourcing.memory;


import com.pragmatists.eventsourcing.api.AggregateId;
import com.pragmatists.eventsourcing.api.Event;
import com.pragmatists.eventsourcing.api.EventStore;
import com.pragmatists.eventsourcing.api.EventStream;

import java.util.List;

public class InMemoryEventStore implements EventStore {

    public EventStream loadEventStream(AggregateId aggregateId) {
        return null;
    }

    public void store(AggregateId aggregateId, long version, List<Event> events) {

    }


}
```

## File: `eventsourcing/src/main/java/com/pragmatists/eventsourcing/memory/InMemoryEventStream.java`
```java
package com.pragmatists.eventsourcing.memory;

import com.pragmatists.eventsourcing.api.Event;
import com.pragmatists.eventsourcing.api.EventStream;

import java.util.Iterator;
import java.util.stream.Stream;


public class InMemoryEventStream implements EventStream {

    private final long version;
    private Stream<Event> stream;

    public InMemoryEventStream(Stream<Event> stream) {
        this.stream = stream;
        this.version = 0;
    }

    public long version() {
        return 0;
    }

    public Iterator<Event> iterator() {
        return stream.iterator();
    }
}
```


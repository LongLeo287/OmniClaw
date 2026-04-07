---
id: java
type: knowledge
owner: OA_Triage
---
# java
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
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

### File: src\shared\test\tv\codely\shared\domain\EmailMother.java
```java
package tv.codely.shared.domain;

public final class EmailMother {
    public static String random() {
        return MotherCreator.random().internet().emailAddress();
    }
}

```

### File: src\shared\test\tv\codely\shared\domain\IntegerMother.java
```java
package tv.codely.shared.domain;

public final class IntegerMother {
    public static Integer random() {
        return MotherCreator.random().number().randomDigit();
    }
}

```

### File: src\shared\test\tv\codely\shared\domain\ListMother.java
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

### File: src\shared\test\tv\codely\shared\domain\MotherCreator.java
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

### File: src\shared\test\tv\codely\shared\domain\RandomElementPicker.java
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

### File: src\shared\test\tv\codely\shared\domain\UuidMother.java
```java
package tv.codely.shared.domain;

import java.util.UUID;

public final class UuidMother {
    public static String random() {
        return UUID.randomUUID().toString();
    }
}

```

### File: src\shared\test\tv\codely\shared\domain\VideoUrlMother.java
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

### File: src\shared\test\tv\codely\shared\domain\WordMother.java
```java
package tv.codely.shared.domain;

public final class WordMother {
    public static String random() {
        return MotherCreator.random().lorem().word();
    }
}

```

### File: src\shared\test\tv\codely\shared\infrastructure\InfrastructureTestCase.java
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

### File: src\shared\test\tv\codely\shared\infrastructure\UnitTestCase.java
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


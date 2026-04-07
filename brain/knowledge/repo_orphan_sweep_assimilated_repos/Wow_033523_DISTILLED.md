---
id: Wow
type: knowledge
owner: OA_Triage
---
# Wow
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
<p align="center" style="text-align:center;">
  <img width="150" src="document/design/assets/logo.svg" alt="Wow:A Modern Reactive CQRS Architecture Microservice development framework based on DDD and EventSourcing"/>
</p>

# Wow : Modern Reactive CQRS Architecture Microservice development framework based on DDD and EventSourcing

[![License](https://img.shields.io/badge/license-Apache%202-4EB1BA.svg)](https://github.com/Ahoo-Wang/Wow/blob/main/LICENSE)
[![GitHub release](https://img.shields.io/github/release/Ahoo-Wang/Wow.svg)](https://github.com/Ahoo-Wang/Wow/releases)
[![Maven Central Version](https://img.shields.io/maven-central/v/me.ahoo.wow/wow-core)](https://central.sonatype.com/artifact/me.ahoo.wow/wow-core)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/cfc724df22db4f9387525258c8a59609)](https://app.codacy.com/gh/Ahoo-Wang/Wow/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade)
[![codecov](https://codecov.io/gh/Ahoo-Wang/Wow/branch/main/graph/badge.svg?token=uloJrLoQir)](https://codecov.io/gh/Ahoo-Wang/Wow)
[![Integration Test Status](https://github.com/Ahoo-Wang/Wow/actions/workflows/integration-test.yml/badge.svg)](https://github.com/Ahoo-Wang/Wow)
[![Awesome Kotlin Badge](https://kotlin.link/awesome-kotlin.svg)](https://github.com/KotlinBy/awesome-kotlin)
[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/Ahoo-Wang/Wow)

**Domain-Driven** | **Event-Driven** | **Test-Driven** | **Declarative-Design** | **Reactive Programming** | **Command Query Responsibility Segregation** | **Event Sourcing**

> [中文文档](https://wow.ahoo.me/zh/) | [English Document](https://wow.ahoo.me/)

## Spring Boot Version Compatibility

> **Wow 6.x** supports Spring Boot 3.x , base Java 17
>
> **Wow 8.x** supports Spring Boot 4.x , base Java 17

## Quick Start

Use [Wow Project Template](https://github.com/Ahoo-Wang/wow-project-template) to quickly create a DDD project based on the Wow framework.

## Features Overview

<p align="center" style="text-align:center">
  <img src="documentation/docs/public/images/Features.png" alt="Wow-Features"/>
</p>

## Architecture

<p align="center" style="text-align:center">
  <img width="95%" src="documentation/docs/public/images/Architecture.svg" alt="Wow-Architecture"/>
</p>

### Command Processing Propagation Chain

<p align="center" style="text-align:center;">
  <img  width="95%" src="documentation/docs/public/images/wait/WaitingForChain.svg" alt="Wow-WaitingForChain"/>
</p>

## Performance Test (Example)

- Test Code: [Example](./example)
- Test Case: Add To Shopping Cart / Create Order
- Command `WaitStrategy`: `SENT`、`PROCESSED`

### Deployment

- [Redis](deploy/example/perf/redis.yaml)
- [MongoDB](deploy/example/perf/mongo.yaml)
- [Kafka](deploy/example/perf/kafka.yaml)
- [Application-Config](deploy/example/perf/config/mongo_kafka_redis.yaml)
- [Application-Deployment](deploy/example/perf/deployment.yaml)

### Test Report

#### Add To Shopping Cart

- [Request](deploy/example/request/AddCartItem.http)
- [Detailed Report(PDF)-SENT](./document/example/perf/Example.Cart.Add@SENT.pdf)
- [Detailed Report(PDF)-PROCESSED](./document/example/perf/Example.Cart.Add@PROCESSED.pdf)

> `WaitStrategy`:`SENT` Mode, The `AddCartItem` command write request API After 2 minutes of stress testing, the average TPS was *59625*, the peak was *82312*, and the average response time was *29* ms.

<p align="center" style="text-align:center">
  <img src="./document/example/perf/Example.Cart.Add@SENT.png" alt="AddCartItem-SENT"/>
</p>

> `WaitStrategy`:`PROCESSED` Mode, The `AddCartItem` command write request API After 2 minutes of stress testing, the average TPS was *18696*, the peak was *24141*, and the average response time was *239* ms.

<p align="center" style="text-align:center">
  <img src="./document/example/perf/Example.Cart.Add@PROCESSED.png" alt="AddCartItem-PROCESSED"/>
</p>

#### Create Order

- [Request](deploy/example/request/CreateOrder.http)
- [Detailed Report(PDF)-SENT](./document/example/perf/Example.Order.Create@SENT.pdf)
- [Detailed Report(PDF)-PROCESSED](./document/example/perf/Example.Order.Create@PROCESSED.pdf)

> `WaitStrategy`:`SENT` Mode, The `CreateOrder` command write request API After 2 minutes of stress testing, the average TPS was *47838*, the peak was *86200*, and the average response time was *217* ms.

<p align="center" style="text-align:center">
  <img src="./document/example/perf/Example.Order.Create@SENT.png" alt="CreateOrder-SENT"/>
</p>

> `WaitStrategy`:`PROCESSED` Mode, The `CreateOrder` command write request API After 2 minutes of stress testing, the average TPS was *18230*, the peak was *25506*, and the average response time was *268* ms.

<p align="center" style="text-align:center">
  <img src="./document/example/perf/Example.Order.Create@PROCESSED.png" alt="CreateOrder-PROCESSED"/>
</p>

## Event Sourcing

<p align="center" style="text-align:center">
  <img src="./document/design/assets/EventSourcing.svg" alt="Wow-EventSourcing"/>
</p>

## Observability

<p align="center" style="text-align:center">
  <img src="./document/design/assets/OpenTelemetry.png" alt="Wow-Observability"/>
</p>

## OpenAPI (Spring WebFlux Integration)

> Automatically register the `Command` routing processing function (`HandlerFunction`), and developers only need to
> write the domain model to complete the service development.

<p align="center" style="text-align:center">
  <img src="document/design/assets/OpenAPI-Swagger.png" alt="Wow-Spring-WebFlux-Integration"/>
</p>

## Test suite: 80%+ test coverage is very easy

> Given -> When -> Expect .

<p align="center" style="text-align:center">
  <img src="./document/design/assets/CI-Flow.png" alt="Wow-CI-Flow"/>
</p>

## Preconditions

- Understanding **Domain Driven Design**：《Implementing Domain-Driven Design》,《Domain-Driven Design: Tackling Complexity
  in the Heart of Software》
- Understanding **Command Query Responsibility Segregation**(CQRS)
- Understanding **EventSourcing**
- Understanding **Reactive Programming**

### Order Service（Kotlin）

[Example-Order](./example)

### Transfer（JAVA）

[Example-Transfer](./example/transfer)

## Unit Test Suite

### 80%+ test coverage is very easy.

![Test Coverage](./document/example/example-domain-jococo.png)

> Given -> When -> Expect .

### Aggregate Unit Test (`AggregateVerifier`)

[Aggregate Test](./example/example-domain/src/test/kotlin/me/ahoo/wow/example/domain/order/OrderTest.kt)

```kotlin
class CartSpec : AggregateSpec<Cart, CartState>({
  on {
    val ownerId = generateGlobalId()
    val addCartItem = AddCartItem(
      productId = "productId",
      quantity = 1,
    )
    givenOwnerId(ownerId)
    whenCommand(addCartItem) {
      expectNoError()
      expectEventType(CartItemAdded::class)
      expectState {
        items.assert().hasSize(1)
      }
      expectStateAggregate {
        ownerId.assert().isEqualTo(ownerId)
      }
      fork {
        val removeCartItem = RemoveCartItem(
          productIds = setOf(addCartItem.productId),
        )
        whenCommand(removeCartItem) {
          expectEventType(CartItemRemoved::class)
        }
      }
      fork {
        whenCommand(DefaultDeleteAggregate) {
          expectEventType(DefaultAggregateDeleted::class)
          expectStateAggregate {
            deleted.assert().isTrue()
          }

          fork {
            whenCommand(DefaultDeleteAggregate) {
              expectErrorType(IllegalAccessDeletedAggregateException::class)
            }
          }
          fork {
            whenCommand(DefaultRecoverAggregate) {
              expectNoError()
              expectStateAggregate {
                deleted.assert().isFalse()
              }
              fork {
                whenCommand(DefaultRecoverAggregate) {
                  expectErrorType(IllegalStateException::class)
                }
              }
            }
          }
        }
      }
    }
  }
}
)
```

### Saga Unit Test (`SagaVerifier`)

[Saga Test](./example/example-domain/src/test/kotlin/me/ahoo/wow/example/domain/cart/CartSagaTest.kt)

```kotlin
class CartSagaSpec : SagaSpec<CartSaga>({
  on {
    val ownerId = generateGlobalId()
    val orderItem = OrderItem(
      id = generateGlobalId(),
      productId = generateGlobalId(),
      price = BigDecimal.valueOf(10),
      quantity = 10,
    )
    whenEvent(
      event = mockk<OrderCreated> {
        every {
          items
        } returns listOf(orderItem)
        every {
          fromCart
        } returns true
      },
      ownerId = ownerId
    ) {
      expectCommandType(RemoveCartItem::class)
      expectCommand<RemoveCartItem> {
        aggregateId.id.assert().isEqualTo(ownerId)
        body.productIds.assert().hasSize(1)
        body.productIds.assert().first().isEqualTo(orderItem.productId)
      }
    }
  }
  on {
    name("NotFromCart")
    val orderItem = OrderItem(
      id = generateGlobalId(),
      productId = generateGlobalId(),
      price = BigDecimal.valueOf(10),
      quantity = 10,
    )
    whenEvent(
      event = mockk<OrderCreated> {
        every {
          items
        } returns listOf(orderItem)
        every {
          fromCart
        } returns false
      },
      ownerId = generateGlobalId()
    ) {
      expectNoCommand()
    }
  }
})
```

## Design

### Modeling

| **Single Class**                                                                       | **Inheritance Pattern**                                                                     | **Aggregation Pattern**                                                                     |
|----------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------|
| ![Single Class - Modeling](./document/design/assets/Modeling-Single-Class-Pattern.svg) | ![Inheritance Pattern- Modeling](./document/design/assets/Modeling-Inheritance-Pattern.svg) | ![Aggregation Pattern- Modeling](./document/design/assets/Modeling-Aggregation-Pattern.svg) |

### Load Aggregate

<p align="center" style="text-align:center">
  <img src="./document/design/assets/Load-Aggregate.svg" alt="Load Aggregate"/>
</p>

### Aggregate State Flow

<p align="center" style="text-align:center">
  <img src="./document/design/assets/Aggregate-State-Flow.svg" alt="Aggregate State Flow"/>
</p>

### Send Command

<p align="center" style="text-align:center">
  <img src="./document/design/assets/Send-Command.svg" alt="Send Command"/>
</p>

### Command And Event Flow

<p align="center" style="text-align:center">
  <img src="./document/design/assets/Command-Event-Flow.svg" alt="Command And Event Flow"/>
</p>

## Event Compensation

### Use Case

<p align="center" style="text-align:center">
  <img src="documentation/docs/public/images/compensation/usercase.svg" alt="Event-Compensation-UserCase"/>
</p>

### Execution Sequence Diagram

<p align="center" style="text-align:center">
  <img src="documentation/docs/public/images/compensation/process-sequence-diagram.svg" alt="Event-Compensation"/>
</p>

### Dashboard

<p align="center" style="text-align:center">
  <img src="documentation/docs/public/images/compensation/dashboard.png" alt="Compensation-Dashboard"/>
</p>

<p align="center" style="text-align:center">
  <img src="documentation/docs/public/images/compensation/dashboard-apply-retry-spec.png" alt="Compensation-Dashboard"/>
</p>

<p align="center" style="text-align:center">
  <img src="documentation/docs/public/images/compensation/dashboard-succeeded.png" alt="Compensation-Dashboard"/>
</p>

<p align="center" style="text-align:center">
  <img src="documentation/docs/public/images/compensation/dashboard-error.png" alt="Compensation-Dashboard-Error"/>
</p>


```

### File: compensation\README.md
```md
# 事件补偿

## 用例图

<p align="center" style="text-align:center">
  <img src="../document/design/assets/Event-Compensation-UserCase.svg" alt="Event-Compensation-UserCase"/>
</p>

## 执行时序图

<p align="center" style="text-align:center">
  <img src="../document/design/assets/Event-Compensation.svg" alt="Event-Compensation"/>
</p>

## Dashboard

<p align="center" style="text-align:center">
  <img src="../documentation/docs/public/images/compensation/dashboard.png" alt="Compensation-Dashboard"/>
</p>

<p align="center" style="text-align:center">
  <img src="../documentation/docs/public/images/compensation/dashboard-apply-retry-spec.png" alt="Compensation-Dashboard"/>
</p>

<p align="center" style="text-align:center">
  <img src="../documentation/docs/public/images/compensation/dashboard-succeeded.png" alt="Compensation-Dashboard"/>
</p>

<p align="center" style="text-align:center">
  <img src="../documentation/docs/public/images/compensation/dashboard-error.png" alt="Compensation-Dashboard-Error"/>
</p>
```

### File: documentation\package.json
```json
{
  "name": "documentation",
  "version": "5.25.6",
  "description": "领域模型即服务 | Modern Reactive CQRS Architecture Microservice development framework based on DDD and EventSourcing.",
  "main": "index.js",
  "scripts": {
    "docs:dev": "vitepress dev docs",
    "docs:build": "vitepress build docs",
    "docs:preview": "vitepress preview docs"
  },
  "keywords": [
    "Domain-Driven",
    "Event-Driven",
    "Test-Driven",
    "Declarative-Design",
    "Reactive Programming",
    "Command Query Responsibility Segregation",
    "Event Sourcing"
  ],
  "author": "ahoo-wang",
  "license": "Apache-2.0",
  "devDependencies": {
    "mermaid": "^11.14.0",
    "vitepress": "^1.6.4",
    "vitepress-plugin-llms": "^1.12.0",
    "vitepress-plugin-mermaid": "^2.0.17"
  },
  "dependencies": {
    "medium-zoom": "^1.1.0"
  }
}

```

### File: wow-api\README.md
```md
# Wow API

[![License](https://img.shields.io/badge/license-Apache%202-4EB1BA.svg)](https://github.com/Ahoo-Wang/Wow/blob/main/LICENSE)
[![Maven Central Version](https://img.shields.io/maven-central/v/me.ahoo.wow/wow-api)](https://central.sonatype.com/artifact/me.ahoo.wow/wow-api)

The core API definitions module for the Wow framework, providing essential interfaces, annotations, and types for building domain-driven design (DDD) applications with Command Query Responsibility Segregation (CQRS) and Event Sourcing patterns.

## Introduction

Wow API is the foundational module of the [Wow framework](https://github.com/Ahoo-Wang/Wow), a modern reactive microservice development framework based on DDD and Event Sourcing. This module defines the core abstractions and contracts that enable:

- **Domain-Driven Design**: Aggregate roots, domain events, value objects, and entities
- **CQRS Architecture**: Separate command and query models with clear boundaries
- **Event Sourcing**: Immutable event streams for state reconstruction and audit trails
- **Reactive Programming**: Non-blocking, asynchronous processing pipelines
- **Type Safety**: Strongly-typed APIs with Kotlin's type system

## Installation

### Gradle (Kotlin DSL)

```kotlin
dependencies {
    implementation("me.ahoo.wow:wow-api:6.5.2")
}
```

### Gradle (Groovy DSL)

```gradle
dependencies {
    implementation 'me.ahoo.wow:wow-api:6.5.2'
}
```

### Maven

```xml
<dependency>
    <groupId>me.ahoo.wow</groupId>
    <artifactId>wow-api</artifactId>
    <version>6.5.2</version>
</dependency>
```

## Usage

### Defining Commands and Events

Commands and events are simple data classes with validation and routing annotations:

#### Commands with Validation and Routing

```kotlin
import jakarta.validation.constraints.NotBlank
import jakarta.validation.constraints.Positive
import me.ahoo.wow.api.annotation.AllowCreate
import me.ahoo.wow.api.annotation.CommandRoute
import me.ahoo.wow.api.annotation.Order
import me.ahoo.wow.api.annotation.Summary

@Order(1)
@AllowCreate
@CommandRoute(method = CommandRoute.Method.POST)
@Summary("Add item to cart")
data class AddCartItem(
    @field:NotBlank
    val productId: String,
    @field:Positive
    val quantity: Int = 1
)

@Order(2)
@Summary("Change item quantity")
@CommandRoute(appendIdPath = CommandRoute.AppendPath.ALWAYS)
data class ChangeQuantity(
    @field:NotBlank
    val productId: String,
    @field:Positive
    val quantity: Int
)

@Order(3)
@Summary("Remove items from cart")
data class RemoveCartItem(
    @field:NotEmpty
    val productIds: Set<String>
)
```

#### Domain Events

```kotlin
@Summary("Item added to cart")
data class CartItemAdded(
    val added: CartItem
)

data class CartQuantityChanged(
    val changed: CartItem
)

data class CartItemRemoved(
    val productIds: Set<String>
)
```

#### Value Objects and Entities

```kotlin
import me.ahoo.wow.api.annotation.ValueObject
import me.ahoo.wow.api.annotation.EntityObject

@ValueObject
data class CartItem(
    val productId: String,
    val quantity: Int = 1
)

@EntityObject
data class OrderItem(
    override val id: String,
    val productId: String,
    val price: BigDecimal,
    val quantity: Int
) : Identifier {
    val totalPrice: BigDecimal
        get() = price.multiply(quantity.toBigDecimal())
}
```

### Bounded Context Configuration

Define bounded contexts and aggregates:

```kotlin
import me.ahoo.wow.api.annotation.BoundedContext

@BoundedContext(
    name = "example-service",
    alias = "example",
    description = "Example Service Context",
    aggregates = [
        BoundedContext.Aggregate("order", packageScopes = [CreateOrder::class]),
        BoundedContext.Aggregate(
            "cart",
            tenantId = TenantId.DEFAULT_TENANT_ID,
            packageScopes = [AddCartItem::class]
        ),
    ],
)
object ExampleService {
    const val SERVICE_NAME = "example-service"
    const val ORDER_AGGREGATE_NAME = "order"
    const val CART_AGGREGATE_NAME = "cart"
}
```

## API Reference

### Core Annotations

- `@AggregateRoot` - Marks a class as an aggregate root in DDD
- `@AggregateId` - Marks a field as the aggregate identifier
- `@Event` - Marks a class as a domain event
- `@OnCommand` - Marks a method as a command handler
- `@OnSourcing` - Marks a method as an event sourcing handler
- `@StatelessSaga` - Marks a class as a stateless saga orchestrator
- `@OnEvent` - Marks a method as an event handler (for sagas)
- `@Retry` - Configures retry behavior for event processing
- `@BoundedContext` - Defines a bounded context boundary
- `@CommandRoute` - Configures REST API routing for commands
- `@AllowCreate` - Allows command to create new aggregates
- `@CreateAggregate` - Marks command as creating new aggregates
- `@VoidCommand` - Marks command as fire-and-forget (no response)
- `@Order` - Defines execution order for commands/events
- `@Summary` - Provides human-readable descriptions
- `@ValueObject` - Marks a class as a value object
- `@EntityObject` - Marks a class as an entity within an aggregate

### Key Interfaces

#### CommandMessage<T>
Represents a command to be executed against an aggregate.

**Key Properties:**
- `aggregateId: AggregateId` - Target aggregate identifier
- `aggregateVersion: Int?` - Expected version for optimistic locking
- `isCreate: Boolean` - Whether this creates a new aggregate
- `allowCreate: Boolean` - Whether creation is permitted
- `isVoid: Boolean` - Whether a response is expected

#### DomainEvent<T>
Represents an immutable fact about a business occurrence.

**Key Properties:**
- `aggregateId: AggregateId` - Source aggregate identifier
- `sequence: Int` - Event sequence number
- `revision: String` - Event schema version
- `isLast: Boolean` - Whether this is the final event

#### AggregateId
Identifies an aggregate instance within a bounded context.

**Properties:**
- `contextName: String` - Bounded context name
- `aggregateName: String` - Aggregate type name
- `id: String` - Instance identifier

### Saga Orchestration

Sagas coordinate distributed transactions using event-driven orchestration:

```kotlin
@StatelessSaga
class TransferSaga {

    fun onEvent(prepared: Prepared, aggregateId: AggregateId): Entry {
        return Entry(prepared.to(), aggregateId.id, prepared.amount())
    }

    fun onEvent(amountEntered: AmountEntered): Confirm {
        return Confirm(amountEntered.sourceId(), amountEntered.amount())
    }

    fun onEvent(entryFailed: EntryFailed): UnlockAmount {
        return UnlockAmount(entryFailed.sourceId(), entryFailed.amount())
    }
}
```

### Query APIs

The module provides comprehensive query capabilities:

```kotlin
// Single entity query
val query = SingleQuery(
    aggregateId = AggregateId("order", "order-123")
)

// Paged list query
val pagedQuery = PagedQuery(
    condition = Condition("status", Operator.EQ, "PENDING"),
    sort = listOf(Sort("createdAt", Direction.DESC)),
    pagination = Pagination(page = 1, size = 20)
)

// Dynamic document queries
val dynamicQuery = DynamicDocument(
    condition = Condition("customerId", Operator.EQ, customerId),
    projection = listOf("orderId", "totalAmount", "status")
)
```

## Modeling Patterns

### Aggregation Pattern (Recommended)

Separates command handling from state management for better separation of concerns:

```kotlin
// Command Aggregate - handles business logic
@AggregateRoot
class Cart(private val state: CartState) {

    @OnCommand
    fun onCommand(command: AddCartItem): CartItemAdded {
        require(state.items.size < MAX_CART_ITEM_SIZE) {
            "Shopping cart can only contain [$MAX_CART_ITEM_SIZE] items."
        }
        // Business logic here
        return CartItemAdded(added = CartItem(command.productId, command.quantity))
    }
}

// State Aggregate - manages state data
class CartState(val id: String) {
    var items: List<CartItem> = listOf()
        private set

    @OnSourcing
    fun onCartItemAdded(event: CartItemAdded) {
        items = items + event.added
    }
}
```

### Single Class Pattern

Combines everything in one class (simpler but less strict):

```kotlin
@AggregateRoot
class Order(@AggregateId val orderId: String) {

    private var status: OrderStatus = OrderStatus.PENDING
    private val items: MutableList<OrderItem> = mutableListOf()

    @OnCommand
    fun create(command: CreateOrder): OrderCreated {
        return OrderCreated(orderId, command.items, command.customerId)
    }

    @OnSourcing
    fun onCreated(event: OrderCreated) {
        items.addAll(event.items)
        status = OrderStatus.CREATED
    }
}
```

## Examples

### Shopping Cart API (Real Example)

Based on the actual example implementation:

```kotlin
// Commands with validation and routing
@Order(1)
@AllowCreate
@CommandRoute(method = CommandRoute.Method.POST)
@Summary("Add item to cart")
data class AddCartItem(
    @field:NotBlank
    val productId: String,
    @field:Positive
    val quantity: Int = 1
)

@Order(2)
@Summary("Change item quantity")
@CommandRoute(appendIdPath = CommandRoute.AppendPath.ALWAYS)
data class ChangeQuantity(
    @field:NotBlank
    val productId: String,
    @field:Positive
    val quantity: Int
)

@Order(3)
@Summary("Remove items from cart")
data class RemoveCartItem(
    @field:NotEmpty
    val productIds: Set<String>
)

// Events
@Summary("Item added to cart")
data class CartItemAdded(val added: CartItem)

data class CartQuantityChanged(val changed: CartItem)

data class CartItemRemoved(val productIds: Set<String>)

// Value objects
@ValueObject
data class CartItem(
    val productId: String,
    val quantity: Int = 1
)

// Void command for queries
@VoidCommand
class ViewCart
```

### Order Management API (Real Example)

```kotlin
@Summary("Create order")
@CommandRoute(action = "")
@CreateAggregate
data class CreateOrder(
    @field:Size(min = 1)
    val items: List<Item>,
    @field:NotNull @field:Valid
    val address: ShippingAddress,
    val fromCart: Boolean
) : CommandValidator {

    override fun validate() {
        require(address.country == "China") {
            "Only support China shipping address."
        }
    }

    data class Item(
        @field:NotEmpty
        override val productId: String,
        @field:Positive
        override val price: BigDecimal,
        @field:Positive
        override val quantity: Int
    ) : CreateOrderItem
}

@CommandRoute("pay", method = CommandRoute.Method.POST, appendOwnerPath = CommandRoute.AppendPath.NEVER)
data class PayOrder(
    @field:NotBlank
    val paymentId: String,
    @field:Positive
    val amount: BigDecimal
)

// Events
data class OrderCreated(
    val orderId: String,
    val items: List<OrderItem>,
    val address: ShippingAddress,
    val fromCart: Boolean
)

data class OrderPaid(val amount: BigDecimal, val paid: Boolean)
data class OrderOverPaid(val paymentId: String, val overPay: BigDecimal)

// Error handling
data class OrderPayDuplicated(val paymentId: String, override val errorMsg: String) : ErrorInfo {
    override val errorCode: String get() = "OrderPayDuplicated"
}

// Value objects and entities
@ValueObject
data class ShippingAddress(
    @field:NotBlank
    val country: String,
    @field:NotBlank
    val province: String,
    val city: String,
    val district: String,
    val detail: String
)

@EntityObject
data class OrderItem(
    override val id: String,
    override val productId: String,
    override val price: BigDecimal,
    override val quantity: Int
) : Identifier, CreateOrderItem {

    val totalPrice: BigDecimal
        get() = price.multiply(quantity.toBigDecimal())
}
```

### Aggregate Implementation

```kotlin
@AggregateRoot
class Cart(private val state: CartState) {

    @OnCommand
    fun onCommand(command: AddCartItem): CartItemAdded {
        // Business logic validation
        return CartItemAdded(CartItem(command.productId, command.quantity))
    }

    @OnCommand
    fun onCommand(command: ChangeQuantity): CartQuantityChanged {
        // Update existing item quantity
        val updated = state.items.find { it.productId == command.productId }
            ?.copy(quantity = command.quantity)
            ?: throw IllegalArgumentException("Item not found")

        return CartQuantityChanged(updated)
    }
}

class CartState(val id: String) {
    var items: List<CartItem> = listOf()
        private set

    @OnSourcing
    fun onCartItemAdded(event: CartItemAdded) {
        items = items + event.added
    }

    @OnSourcing
    fun onCartQuantityChanged(event: CartQuantityChanged) {
        items = items.map {
            if (it.productId == event.changed.productId) event.changed else it
        }
    }
}
```

## Contributing

We welcome contributions to the Wow API module! Please see the main [Wow repository](https://github.com/Ahoo-Wang/Wow) for contribution guidelines.

### Development Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/Ahoo-Wang/Wow.git
   cd Wow
   ```

2. Build the project:
   ```bash
   ./gradlew build
   ```

3. Run tests:
   ```bash
   ./gradlew :wow-api:test
   ```

### Code Style

This project follows Kotlin coding conventions and uses Detekt for static analysis. Format code using:

```bash
./gradlew detekt --auto-correct
```

## License

Wow API is licensed under the Apache License 2.0. See [LICENSE](https://github.com/Ahoo-Wang/Wow/blob/main/LICENSE) for details.
```

### File: wow-benchmarks\README.md
```md
# Benchmarks

## BloomFilterIdempotencyChecker

```kotlin
fun createBloomFilterIdempotencyChecker(): BloomFilterIdempotencyChecker {
    return BloomFilterIdempotencyChecker(Duration.ofMinutes(1)) {
        BloomFilter.create(
            Funnels.stringFunnel(Charsets.UTF_8),
            10_000_000,
            0.00001,
        )
    }
}
```

```
Benchmark                                      Mode  Cnt        Score         Error  Units
BloomFilterIdempotencyCheckerBenchmark.check  thrpt    4  6074504.775 ± 2015643.464  ops/s
```

## CommandDispatcher

```
Benchmark                                                                                            Mode  Cnt       Score   Error   Units
m.a.w.modeling.CommandDispatcherBenchmark.send                                                      thrpt    2  326620.365           ops/s
m.a.w.modeling.CommandDispatcherBenchmark.send:async                                                thrpt              NaN             ---
m.a.w.modeling.CommandDispatcherBenchmark.send:gc.alloc.rate                                        thrpt    2    4334.039          MB/sec
m.a.w.modeling.CommandDispatcherBenchmark.send:gc.alloc.rate.norm                                   thrpt    2   15029.677            B/op
m.a.w.modeling.CommandDispatcherBenchmark.send:gc.count                                             thrpt    2     160.000          counts
m.a.w.modeling.CommandDispatcherBenchmark.send:gc.time                                              thrpt    2    1301.000              ms
m.a.w.modeling.CommandDispatcherBenchmark.sendAndWaitForProcessed                                   thrpt    2  135709.022           ops/s
m.a.w.modeling.CommandDispatcherBenchmark.sendAndWaitForProcessed:async                             thrpt              NaN             ---
m.a.w.modeling.CommandDispatcherBenchmark.sendAndWaitForProcessed:gc.alloc.rate                     thrpt    2    2265.816          MB/sec
m.a.w.modeling.CommandDispatcherBenchmark.sendAndWaitForProcessed:gc.alloc.rate.norm                thrpt    2   19202.684            B/op
m.a.w.modeling.CommandDispatcherBenchmark.sendAndWaitForProcessed:gc.count                          thrpt    2      15.000          counts
m.a.w.modeling.CommandDispatcherBenchmark.sendAndWaitForProcessed:gc.time                           thrpt    2     579.000              ms
m.a.w.modeling.CommandDispatcherBenchmark.sendAndWaitForSent                                        thrpt    2  231489.346           ops/s
m.a.w.modeling.CommandDispatcherBenchmark.sendAndWaitForSent:async                                  thrpt              NaN             ---
m.a.w.modeling.CommandDispatcherBenchmark.sendAndWaitForSent:gc.alloc.rate                          thrpt    2    3811.580          MB/sec
m.a.w.modeling.CommandDispatcherBenchmark.sendAndWaitForSent:gc.alloc.rate.norm                     thrpt    2   18605.516            B/op
m.a.w.modeling.CommandDispatcherBenchmark.sendAndWaitForSent:gc.count                               thrpt    2      63.000          counts
m.a.w.modeling.CommandDispatcherBenchmark.sendAndWaitForSent:gc.time                                thrpt    2    1041.000              ms
m.a.w.modeling.NoopCommandDispatcherBenchmark.send                                                  thrpt    2  639539.709           ops/s
m.a.w.modeling.NoopCommandDispatcherBenchmark.send:async                                            thrpt              NaN             ---
m.a.w.modeling.NoopCommandDispatcherBenchmark.send:gc.alloc.rate                                    thrpt    2    7481.951          MB/sec
m.a.w.modeling.NoopCommandDispatcherBenchmark.send:gc.alloc.rate.norm                               thrpt    2   13463.081            B/op
m.a.w.modeling.NoopCommandDispatcherBenchmark.send:gc.count                                         thrpt    2      34.000          counts
m.a.w.modeling.NoopCommandDispatcherBenchmark.send:gc.time                                          thrpt    2     267.000              ms
m.a.w.modeling.NoopCommandDispatcherBenchmark.sendAndWaitForProcessed                               thrpt    2  149432.225           ops/s
m.a.w.modeling.NoopCommandDispatcherBenchmark.sendAndWaitForProcessed:async                         thrpt              NaN             ---
m.a.w.modeling.NoopCommandDispatcherBenchmark.sendAndWaitForProcessed:gc.alloc.rate                 thrpt    2    2356.847          MB/sec
m.a.w.modeling.NoopCommandDispatcherBenchmark.sendAndWaitForProcessed:gc.alloc.rate.norm            thrpt    2   18161.580            B/op
m.a.w.modeling.NoopCommandDispatcherBenchmark.sendAndWaitForProcessed:gc.count                      thrpt    2      10.000          counts
m.a.w.modeling.NoopCommandDispatcherBenchmark.sendAndWaitForProcessed:gc.time                       thrpt    2      21.000              ms
m.a.w.modeling.NoopCommandDispatcherBenchmark.sendAndWaitForSent                                    thrpt    2  462755.237           ops/s
m.a.w.modeling.NoopCommandDispatcherBenchmark.sendAndWaitForSent:async                              thrpt              NaN             ---
m.a.w.modeling.NoopCommandDispatcherBenchmark.sendAndWaitForSent:gc.alloc.rate                      thrpt    2    7045.290          MB/sec
m.a.w.modeling.NoopCommandDispatcherBenchmark.sendAndWaitForSent:gc.alloc.rate.norm                 thrpt    2   17567.579            B/op
m.a.w.modeling.NoopCommandDispatcherBenchmark.sendAndWaitForSent:gc.count                           thrpt    2      32.000          counts
m.a.w.modeling.NoopCommandDispatcherBenchmark.sendAndWaitForSent:gc.time                            thrpt    2      45.000              ms
m.a.w.modeling.NoopEventStoreCommandDispatcherBenchmark.send                                        thrpt    2  559871.911           ops/s
m.a.w.modeling.NoopEventStoreCommandDispatcherBenchmark.send:async                                  thrpt              NaN             ---
m.a.w.modeling.NoopEventStoreCommandDispatcherBenchmark.send:gc.alloc.rate                          thrpt    2    7110.615          MB/sec
m.a.w.modeling.NoopEventStoreCommandDispatcherBenchmark.send:gc.alloc.rate.norm                     thrpt    2   14637.444            B/op
m.a.w.modeling.NoopEventStoreCommandDispatcherBenchmark.send:gc.count                               thrpt    2      32.000          counts
m.a.w.modeling.NoopEventStoreCommandDispatcherBenchmark.send:gc.time                                thrpt    2      81.000              ms
m.a.w.modeling.NoopEventStoreCommandDispatcherBenchmark.sendAndWaitForProcessed                     thrpt    2  151343.235           ops/s
m.a.w.modeling.NoopEventStoreCommandDispatcherBenchmark.sendAndWaitForProcessed:async               thrpt              NaN             ---
m.a.w.modeling.NoopEventStoreCommandDispatcherBenchmark.sendAndWaitForProcessed:gc.alloc.rate       thrpt    2    2468.360          MB/sec
m.a.w.modeling.NoopEventStoreCommandDispatcherBenchmark.sendAndWaitForProcessed:gc.alloc.rate.norm  thrpt    2   18775.357            B/op
m.a.w.modeling.NoopEventStoreCommandDispatcherBenchmark.sendAndWaitForProcessed:gc.count            thrpt    2      11.000          counts
m.a.w.modeling.NoopEventStoreCommandDispatcherBenchmark.sendAndWaitForProcessed:gc.time             thrpt    2      24.000              ms
m.a.w.modeling.NoopEventStoreCommandDispatcherBenchmark.sendAndWaitForSent                          thrpt    2  374889.450           ops/s
m.a.w.modeling.NoopEventStoreCommandDispatcherBenchmark.sendAndWaitForSent:async                    thrpt              NaN             ---
m.a.w.modeling.NoopEventStoreCommandDispatcherBenchmark.sendAndWaitForSent:gc.alloc.rate            thrpt    2    5829.989          MB/sec
m.a.w.modeling.NoopEventStoreCommandDispatcherBenchmark.sendAndWaitForSent:gc.alloc.rate.norm       thrpt    2   17923.198            B/op
m.a.w.modeling.NoopEventStoreCommandDispatcherBenchmark.sendAndWaitForSent:gc.count                 thrpt    2      26.000          counts
m.a.w.modeling.NoopEventStoreCommandDispatcherBenchmark.sendAndWaitForSent:gc.time                  thrpt    2      45.000              ms
m.a.w.mongo.MongoCommandDispatcherBenchmark.send                                                    thrpt    2  474081.500           ops/s
m.a.w.mongo.MongoCommandDispatcherBenchmark.send:async                                              thrpt              NaN             ---
m.a.w.mongo.MongoCommandDispatcherBenchmark.send:gc.alloc.rate                                      thrpt    2    2202.128          MB/sec
m.a.w.mongo.MongoCommandDispatcherBenchmark.send:gc.alloc.rate.norm                                 thrpt    2    5321.941            B/op
m.a.w.mongo.MongoCommandDispatcherBenchmark.send:gc.count                                           thrpt    2      18.000          counts
m.a.w.mongo.MongoCommandDispatcherBenchmark.send:gc.time                                            thrpt    2    1266.000              ms
m.a.w.mongo.MongoCommandDispatcherBenchmark.sendAndWaitForProcessed                                 thrpt    2    8707.898           ops/s
m.a.w.mongo.MongoCommandDispatcherBenchmark.sendAndWaitForProcessed:async                           thrpt              NaN             ---
m.a.w.mongo.MongoCommandDispatcherBenchmark.sendAndWaitForProcessed:gc.alloc.rate                   thrpt    2     572.050          MB/sec
m.a.w.mongo.MongoCommandDispatcherBenchmark.sendAndWaitForProcessed:gc.alloc.rate.norm              thrpt    2   74733.243            B/op
m.a.w.mongo.MongoCommandDispatcherBenchmark.sendAndWaitForProcessed:gc.count                        thrpt    2       3.000          counts
m.a.w.mongo.MongoCommandDispatcherBenchmark.sendAndWaitForProcessed:gc.time                         thrpt    2      41.000              ms
m.a.w.mongo.MongoCommandDispatcherBenchmark.sendAndWaitForSent                                      thrpt    2  354730.437           ops/s
m.a.w.mongo.MongoCommandDispatcherBenchmark.sendAndWaitForSent:async                                thrpt              NaN             ---
m.a.w.mongo.MongoCommandDispatcherBenchmark.sendAndWaitForSent:gc.alloc.rate                        thrpt    2    2942.639          MB/sec
m.a.w.mongo.MongoCommandDispatcherBenchmark.sendAndWaitForSent:gc.alloc.rate.norm                   thrpt    2    9546.036            B/op
m.a.w.mongo.MongoCommandDispatcherBenchmark.sendAndWaitForSent:gc.count                             thrpt    2      20.000          counts
m.a.w.mongo.MongoCommandDispatcherBenchmark.sendAndWaitForSent:gc.time                              thrpt    2    1271.000              ms
m.a.w.redis.RedisCommandDispatcherBenchmark.send                                                    thrpt    2  609025.464           ops/s
m.a.w.redis.RedisCommandDispatcherBenchmark.send:async                                              thrpt              NaN             ---
m.a.w.redis.RedisCommandDispatcherBenchmark.send:gc.alloc.rate                                      thrpt    2    2256.571          MB/sec
m.a.w.redis.RedisCommandDispatcherBenchmark.send:gc.alloc.rate.norm                                 thrpt    2    4160.436            B/op
m.a.w.redis.RedisCommandDispatcherBenchmark.send:gc.count                                           thrpt    2      27.000          counts
m.a.w.redis.RedisCommandDispatcherBenchmark.send:gc.time                                            thrpt    2    1371.000              ms
m.a.w.redis.RedisCommandDispatcherBenchmark.sendAndWaitForProcessed                                 thrpt    2   13460.565           ops/s
m.a.w.redis.RedisCommandDispatcherBenchmark.sendAndWaitForProcessed:async                           thrpt              NaN             ---
m.a.w.redis.RedisCommandDispatcherBenchmark.sendAndWaitForProcessed:gc.alloc.rate                   thrpt    2     305.752          MB/sec
m.a.w.redis.RedisCommandDispatcherBenchmark.sendAndWaitForProcessed:gc.alloc.rate.norm              thrpt    2   25246.580            B/op
m.a.w.redis.RedisCommandDispatcherBenchmark.sendAndWaitForProcessed:gc.count                        thrpt    2       3.000          counts
m.a.w.redis.RedisCommandDispatcherBenchmark.sendAndWaitForProcessed:gc.time                         thrpt    2       7.000              ms
m.a.w.redis.RedisCommandDispatcherBenchmark.sendAndWaitForSent                                      thrpt    2  421133.647           ops/s
m.a.w.redis.RedisCommandDispatcherBenchmark.sendAndWaitForSent:async                                thrpt              NaN             ---
m.a.w.redis.RedisCommandDispatcherBenchmark.sendAndWaitForSent:gc.alloc.rate                        thrpt    2    2941.960          MB/sec
m.a.w.redis.RedisCommandDispatcherBenchmark.sendAndWaitForSent:gc.alloc.rate.norm                   thrpt    2    7720.249            B/op
m.a.w.redis.RedisCommandDispatcherBenchmark.sendAndWaitForSent:gc.count                             thrpt    2      27.000          counts
m.a.w.redis.RedisCommandDispatcherBenchmark.sendAndWaitForSent:gc.time                              thrpt    2    1561.000              ms
```



```
Benchmark                         Mode  Cnt      Score      Error  Units
MongoEventStoreBenchmark.append  thrpt    4  17603.362 ± 2155.153  ops/s
```

```
Benchmark                         Mode  Cnt      Score      Error  Units
RedisEventStoreBenchmark.append  thrpt    4  17551.479 ± 1103.835  ops/s
```

```
Benchmark                                                                                            Mode  Cnt       Score        Error   Units
m.a.w.modeling.InMemoryCommandDispatcherBenchmark.sendAndWaitForProcessed                           thrpt    4   81566.387 ± 135364.825   ops/s
m.a.w.modeling.InMemoryCommandDispatcherBenchmark.sendAndWaitForProcessed:async                     thrpt              NaN                  ---
m.a.w.modeling.InMemoryCommandDispatcherBenchmark.sendAndWaitForProcessed:gc.alloc.rate             thrpt    4    1413.925 ±   2432.540  MB/sec
m.a.w.modeling.InMemoryCommandDispatcherBenchmark.sendAndWaitForProcessed:gc.alloc.rate.norm        thrpt    4   19063.307 ±    333.514    B/op
m.a.w.modeling.InMemoryCommandDispatcherBenchmark.sendAndWaitForProcessed:gc.count                  thrpt    4      54.000               counts
m.a.w.modeling.InMemoryCommandDispatcherBenchmark.sendAndWaitForProcessed:gc.time                   thrpt    4    5152.000                   ms
m.a.w.modeling.NoopCommandDispatcherBenchmark.sendAndWaitForProcessed                               thrpt    4  115880.094 ±  49217.328   ops/s
m.a.w.modeling.NoopCommandDispatcherBenchmark.sendAndWaitForProcessed:async                         thrpt              NaN                  ---
m.a.w.modeling.NoopCommandDispatcherBenchmark.sendAndWaitForProcessed:gc.alloc.rate                 thrpt    4    1878.657 ±    920.858  MB/sec
m.a.w.modeling.NoopCommandDi
... [TRUNCATED]
```

### File: wow-core\README.md
```md
# Wow Core

[![License](https://img.shields.io/badge/license-Apache%202-4EB1BA.svg)](https://github.com/Ahoo-Wang/Wow/blob/main/LICENSE)
[![Maven Central Version](https://img.shields.io/maven-central/v/me.ahoo.wow/wow-core)](https://central.sonatype.com/artifact/me.ahoo.wow/wow-core)

The core implementation module for the Wow framework, providing essential runtime infrastructure for CQRS and Event Sourcing applications including command processing, event handling, event sourcing, saga orchestration, and projections.

## Introduction

Wow Core is the foundational runtime module of the [Wow framework](https://github.com/Ahoo-Wang/Wow), implementing the core patterns and infrastructure needed for building domain-driven design (DDD) applications with Command Query Responsibility Segregation (CQRS) and Event Sourcing.

This module provides:

- **Command Processing**: Command gateway with validation, idempotency, and wait strategies
- **Event Handling**: Domain event bus, dispatching, and processing pipelines
- **Event Sourcing**: Event store implementations and state reconstruction
- **Saga Orchestration**: Distributed transaction coordination using event-driven workflows
- **Projection**: Event-driven updates to query models and read databases
- **Serialization**: JSON serialization for commands, events, and aggregate state
- **Exception Handling**: Comprehensive error handling and recovery mechanisms
- **Message Propagation**: Header propagation, tracing, and cross-service communication

## Installation

### Gradle (Kotlin DSL)

```kotlin
dependencies {
    implementation("me.ahoo.wow:wow-core:6.5.2")
}
```

### Gradle (Groovy DSL)

```gradle
dependencies {
    implementation 'me.ahoo.wow:wow-core:6.5.2'
}
```

### Maven

```xml
<dependency>
    <groupId>me.ahoo.wow</groupId>
    <artifactId>wow-core</artifactId>
    <version>6.5.2</version>
</dependency>
```

## Usage

### Command Processing

The `CommandGateway` provides comprehensive command handling with validation, idempotency, and flexible wait strategies:

```kotlin
// Send command with validation and idempotency checking
val addCartItem = AddCartItem(productId = "product-123", quantity = 2)
val command = addCartItem.toCommandMessage(ownerId = "customer-456")

gateway.send(command)
    .doOnSuccess { println("Command sent successfully") }
    .subscribe()

// Send and wait for completion with different strategies
gateway.sendAndWait(command, WaitStrategy.PROCESSED)
    .doOnNext { result ->
        if (result.succeeded) {
            println("Cart item added: ${result.commandId}")
        }
    }
    .subscribe()

// Stream command results in real-time
gateway.sendAndWaitStream(command, WaitStrategy.PROCESSED)
    .doOnNext { result ->
        println("Command stage: ${result.stage} - ${result.succeeded}")
    }
    .subscribe()
```

### Event Handling

Domain events are published through the event bus and processed by handlers:

```kotlin
// Events are automatically published by aggregates after command processing
// The framework handles event publishing internally

// Handle events with projections
@ProjectionProcessor
class OrderProjector {

    @OnEvent
    fun onOrderCreated(event: OrderCreated): Mono<Void> {
        return orderRepository.save(
            OrderSummary(
                id = event.aggregateId.id,
                totalAmount = event.items.sumOf { it.totalPrice },
                status = OrderStatus.CREATED,
                createdAt = event.createTime
            )
        ).then()
    }

    @OnEvent
    fun onOrderPaid(event: OrderPaid): Mono<Void> {
        return orderRepository.findById(event.aggregateId.id)
            .flatMap { summary ->
                val updated = summary.copy(
                    status = OrderStatus.PAID,
                    paidAt = event.createTime
                )
                orderRepository.save(updated)
            }
            .then()
    }
}
```

### Event Sourcing

Load and reconstruct aggregate state from event streams:

```kotlin
// Load event streams for state reconstruction
eventStore.load(aggregateId, headVersion = 1, tailVersion = Int.MAX_VALUE)
    .collectList()
    .map { eventStreams ->
        // Reconstruct aggregate state from events
        val state = OrderState(aggregateId.id)
        eventStreams.forEach { stream ->
            stream.events.forEach { event ->
                when (event) {
                    is OrderCreated -> {
                        state.items.addAll(event.items)
                        state.address = event.address
                        state.status = OrderStatus.CREATED
                    }
                    is OrderPaid -> {
                        state.status = OrderStatus.PAID
                        state.paidAmount = event.amount
                    }
                    is OrderShipped -> {
                        state.status = OrderStatus.SHIPPED
                    }
                    // ... handle other events
                }
            }
        }
        state
    }
    .subscribe()

// Load events by time range for auditing
eventStore.load(aggregateId, headEventTime = startTime, tailEventTime = endTime)
    .flatMap { stream -> Flux.fromIterable(stream.events) }
    .collectList()
    .subscribe { events -> auditLog.append(events) }
```

### Saga Orchestration

Coordinate distributed transactions using event-driven sagas:

```kotlin
@StatelessSaga
class CartSaga {

    /**
     * Remove cart items after order is created
     */
    @Retry(maxRetries = 5, minBackoff = 60, executionTimeout = 10)
    @OnEvent
    fun onOrderCreated(event: DomainEvent<OrderCreated>): CommandBuilder? {
        val orderCreated = event.body
        if (!orderCreated.fromCart) {
            return null
        }
        // Build command to remove items from cart
        return RemoveCartItem(
            productIds = orderCreated.items.map { it.productId }.toSet(),
        ).commandBuilder()
            .aggregateId(event.ownerId) // Cart aggregate ID
    }
}
```

## API Reference

### Core Interfaces

#### CommandGateway
Central interface for sending commands with validation and wait strategies.

**Key Methods:**
- `send(command: CommandMessage)` - Send command asynchronously
- `sendAndWait(command, waitStrategy)` - Send and wait for completion
- `sendAndWaitStream(command, waitStrategy)` - Stream command results

#### DomainEventBus
Message bus for publishing and subscribing to domain event streams.

**Implementations:**
- `LocalDomainEventBus` - In-process event handling
- `DistributedDomainEventBus` - Cross-service event distribution
- `LocalFirstDomainEventBus` - Hybrid local/distributed approach

#### EventStore
Persistent storage for domain event streams with versioning support.

**Key Methods:**
- `append(eventStream)` - Store new event streams
- `load(aggregateId, headVersion, tailVersion)` - Load event streams by version range
- `load(aggregateId, headEventTime, tailEventTime)` - Load by time range

#### StatelessSagaHandler
Processes domain events to coordinate distributed transactions.

#### ProjectionHandler
Updates query models in response to domain events.

### Key Components

#### Command Processing
- **Command Validation**: Jakarta validation integration
- **Idempotency Checking**: Prevents duplicate command processing
- **Wait Strategies**: `SENT`, `PROCESSED`, `PROJECTED` for different consistency levels

#### Event Processing
- **Event Dispatching**: Ordered event processing per aggregate
- **Event Filtering**: Function-based event routing
- **Error Handling**: Configurable error recovery strategies

#### Serialization
- **Message Serialization**: JSON serialization for all message types
- **State Serialization**: Aggregate state persistence
- **Event Stream Serialization**: Efficient event storage format

#### Exception Handling
- **Error Conversion**: Standardized error handling
- **Recoverable Exceptions**: Automatic retry mechanisms
- **Error Propagation**: Consistent error reporting across services

## Examples

### Complete Command Processing with REST Controller

```kotlin
@RestController
class CartController(
    private val commandGateway: CommandGateway,
    private val cartQueryClient: CartQueryClient
) {

    @PostMapping("/cart/{userId}/add-cart-item")
    fun addCartItem(@PathVariable userId: String): Flux<CommandResult> {
        val addCartItem = AddCartItem(
            productId = "product-123",
            quantity = 2
        )
        val command = addCartItem.toCommandMessage(ownerId = userId)

        // Stream command processing results in real-time
        return commandGateway.sendAndWaitStream(
            command,
            waitStrategy = WaitingForStage.snapshot(command.commandId)
        )
    }

    @GetMapping("/cart/me")
    fun getCart(): Mono<CartData> {
        return singleQuery {
            // Query current user's cart
        }.queryState(cartQueryClient)
    }
}
```

### Event-Sourced Aggregate Repository

```kotlin
class EventSourcingOrderRepository(
    private val eventStore: EventStore,
    private val snapshotRepository: SnapshotRepository
) : OrderRepository {

    override fun load(orderId: String): Mono<OrderState> {
        val aggregateId = AggregateId("order", orderId)

        return snapshotRepository.load(aggregateId)
            .flatMap { snapshot ->
                // Load events after snapshot version
                eventStore.load(aggregateId, snapshot.version + 1)
                    .collectList()
                    .map { eventStreams ->
                        val state = snapshot.state as OrderState
                        eventStreams.forEach { stream ->
                            stream.events.forEach { event ->
                                state.apply(event)
                            }
                        }
                        state
                    }
            }
            .switchIfEmpty(
                // No snapshot, load all events from beginning
                eventStore.load(aggregateId, headVersion = 1)
                    .collectList()
                    .map { eventStreams ->
                        val state = OrderState(orderId)
                        eventStreams.forEach { stream ->
                            stream.events.forEach { event ->
                                state.apply(event)
                            }
                        }
                        state
                    }
            )
    }

    private fun OrderState.apply(event: DomainEvent<*>): OrderState {
        return when (event) {
            is OrderCreated -> {
                this.items.addAll(event.items)
                this.address = event.address
                this.status = OrderStatus.CREATED
                this
            }
            is OrderPaid -> {
                this.status = OrderStatus.PAID
                this.paidAmount += event.amount
                this
            }
            is OrderShipped -> {
                this.status = OrderStatus.SHIPPED
                this
            }
            is OrderReceived -> {
                this.status = OrderStatus.RECEIVED
                this
            }
            else -> this
        }
    }
}
```

### Projection Implementation

```kotlin
@ProjectionProcessor
class OrderProjector(
    private val orderRepository: OrderRepository
) {

    @OnEvent
    fun onOrderCreated(event: OrderCreated): Mono<Void> {
        // Log the event for monitoring
        log.info("Order created: ${event.aggregateId.id}")

        // Update read model asynchronously
        return orderRepository.saveOrderSummary(
            OrderSummary(
                id = event.aggregateId.id,
                items = event.items,
                address = event.address,
                totalAmount = event.items.sumOf { it.totalPrice },
                status = OrderStatus.CREATED,
                createdAt = event.createTime
            )
        ).then()
    }

    @OnEvent
    fun onOrderPaid(event: OrderPaid): Mono<Void> {
        log.debug("Order paid: ${event.aggregateId.id}")

        return orderRepository.updateOrderStatus(
            event.aggregateId.id,
            OrderStatus.PAID,
            paidAt = event.createTime
        ).then()
    }

    @OnEvent
    fun onOrderShipped(event: OrderShipped): Mono<Void> {
        return orderRepository.updateOrderStatus(
            event.aggregateId.id,
            OrderStatus.SHIPPED,
            shippedAt = event.createTime
        ).then()
    }

    // Handle state events for additional processing
    @OnEvent
    fun onStateEvent(event: OrderCreated, state: OrderState): Mono<Void> {
        // Access both event and current state for complex logic
        log.info("Order state after creation: ${state.toJsonString()}")
        return Mono.empty()
    }
}
```

## Configuration

### Command Gateway Configuration

```yaml
wow:
  command:
    bus:
      type: kafka  # in_memory, kafka, redis, etc.
      local-first:
        enabled: true  # Enable local-first optimization
    idempotency:
      enabled: true  # Enable command idempotency checking
      bloom-filter:
        expected-insertions: 1000000
        ttl: PT60S  # Time-to-live for idempotency records
        fpp: 0.00001  # False positive probability
```

### Event Store Configuration

```yaml
wow:
  eventsourcing:
    store:
      storage: mongo  # mongo, redis, r2dbc, in_memory, delay
    snapshot:
      enabled: true  # Enable snapshot optimization
      strategy: all  # all, version_offset
      storage: mongo  # mongo, redis, r2dbc, elasticsearch, in_memory, delay
      version-offset: 5  # Version offset for snapshots
    state:
      bus:
        type: kafka  # in_memory, kafka, redis, etc.
        local-first:
          enabled: true
```

### Saga Configuration

Saga orchestration is automatically configured when using `@StatelessSaga` annotations. No additional configuration is typically required, but you can customize error handling behavior through the filter chain.

## Contributing

We welcome contributions to the Wow Core module! Please see the main [Wow repository](https://github.com/Ahoo-Wang/Wow) for contribution guidelines.

### Development Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/Ahoo-Wang/Wow.git
   cd Wow
   ```

2. Build the project:
   ```bash
   ./gradlew build
   ```

3. Run tests:
   ```bash
   ./gradlew :wow-core:test
   ```

### Code Style

This project follows Kotlin coding conventions and uses Detekt for static analysis. Format code using:

```bash
./gradlew detekt --auto-correct
```

## License

Wow Core is licensed under the Apache License 2.0. See [LICENSE](https://github.com/Ahoo-Wang/Wow/blob/main/LICENSE) for details.
```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.

---
id: github.com-boristane-agent-skills.git-784c9d85-kno
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:35.700362
---

# KNOWLEDGE EXTRACT: github.com_boristane_agent-skills.git_784c9d85
> **Extracted on:** 2026-04-01 09:48:36
> **Source:** D:/LongLeo/AI OS CORP/AI OS/core/security/QUARANTINE/KI-BATCH-20260331205007520474/github.com_boristane_agent-skills.git_784c9d85

---

## File: `.gitignore`
```
.claude
```

## File: `README.md`
```markdown
# Agent Skills

A collection of skills for AI coding agents. Skills are packaged instructions and scripts that extend agent capabilities.

Skills follow the [Agent Skills](https://agentskills.io/) format.

## Available Skills

### logging-best-practices

Logging best practices focused on wide events (canonical log lines). Contains guidelines for effective logging that enables powerful debugging and analytics.

**Use when:**
- Writing or reviewing logging code
- Adding console.log, logger.info, or similar
- Designing logging strategy for new services
- Setting up logging infrastructure

**Key concepts:**
- Wide Events (Critical) - One context-rich event per request per service
- High Cardinality & Dimensionality (Critical) - Many fields, unique identifiers
- Business Context (Critical) - User subscription, cart value, feature flags
- Environment Context (Critical) - Commit hash, version, region, instance ID
- Single Logger (High) - One logger instance, configured at startup
- Middleware Pattern (High) - Infrastructure in middleware, business context in handlers

**References:**
- [Logging Sucks](https://loggingsucks.com)
- [Observability Wide Events 101](https://boristane.com/blog/observability-wide-events-101/)
- [Stripe - Canonical Log Lines](https://stripe.com/blog/canonical-log-lines)

## Installation

```bash
npx add-skill boristane/agent-skills
```

## Usage

Skills are automatically available once installed. The agent will use them when relevant tasks are detected.

**Examples:**
```
Add logging to this endpoint
```
```
Review my logging code
```
```
Help me set up logging for this service
```

## Skill Structure

Each skill contains:
- `SKILL.md` - Instructions for the agent
- `rules/` - Individual guideline files
- `metadata.json` - Version and references
```

## File: `skills/logging-best-practices/README.md`
```markdown
# Logging Best Practices Skill

A skill for AI coding assistants to apply logging best practices when writing or reviewing code.

## Overview

This skill teaches the **wide events** pattern (also known as canonical log lines) - emit a single, context-rich event per request per service instead of scattered log statements.

## Key Concepts

- **Wide Events**: One comprehensive event per request, emitted at completion
- **High Cardinality**: Support fields with millions of unique values (user_id, request_id)
- **High Dimensionality**: Include many fields (20+) per event
- **Business Context**: Always include user subscription, cart value, feature flags
- **Environment Context**: Always include commit hash, version, region, instance ID
- **Single Logger**: One logger instance configured at startup, used everywhere
- **Middleware Pattern**: Handle logging infrastructure in middleware, business context in handlers

## Structure

```
logging-best-practices/
├── SKILL.md              # Agent instructions
├── README.md             # This file
├── metadata.json         # Version and references
└── rules/
    ├── wide-events.md    # Core pattern (CRITICAL)
    ├── context.md        # Cardinality, business & environment context (CRITICAL)
    ├── structure.md      # Single logger, middleware, JSON format (HIGH)
    └── pitfalls.md       # Common mistakes (MEDIUM)
```

## Rules

1. **Wide Events** (CRITICAL) - One event per request, emit in finally block, request ID correlation
2. **Context** (CRITICAL) - High cardinality, dimensionality, business context, environment characteristics
3. **Structure** (HIGH) - Single logger, middleware pattern, JSON format, consistent schema
4. **Pitfalls** (MEDIUM) - Scattered logs, unknown unknowns, missing request correlation

## Reference

- [Boris Tane's Blog - Logging Sucks](https://loggingsucks.com)
- [Boris Tane's Blog - Observability wide events 101](https://boristane.com/blog/observability-wide-events-101/)
- [Stripe Blog - Canonical Log Lines](https://stripe.com/blog/canonical-log-lines)
```

## File: `skills/logging-best-practices/SKILL.md`
```markdown
---
name: logging-best-practices
description: Logging best practices focused on wide events (canonical log lines) for powerful debugging and analytics
license: MIT
metadata:
  author: boristane
  version: "1.0.0"
---

# Logging Best Practices Skill

Version: 1.0.0

## Purpose

This skill provides guidelines for implementing effective logging in applications. It focuses on **wide events** (also called canonical log lines) - a pattern where you emit a single, context-rich event per request per service, enabling powerful debugging and analytics.

## When to Apply

Apply these guidelines when:
- Writing or reviewing logging code
- Adding console.log, logger.info, or similar
- Designing logging strategy for new services
- Setting up logging infrastructure

## Core Principles

### 1. Wide Events (CRITICAL)

Emit **one context-rich event per request per service**. Instead of scattering log lines throughout your handler, consolidate everything into a single structured event emitted at request completion.

```typescript
const wideEvent: Record<string, unknown> = {
  method: 'POST',
  path: '/checkout',
  requestId: c.get('requestId'),
  timestamp: new Date().toISOString(),
};

try {
  const user = await getUser(c.get('userId'));
  wideEvent.user = { id: user.id, subscription: user.subscription };

  const cart = await getCart(user.id);
  wideEvent.cart = { total_cents: cart.total, item_count: cart.items.length };

  wideEvent.status_code = 200;
  wideEvent.outcome = 'success';
  return c.json({ success: true });
} catch (error) {
  wideEvent.status_code = 500;
  wideEvent.outcome = 'error';
  wideEvent.error = { message: error.message, type: error.name };
  throw error;
} finally {
  wideEvent.duration_ms = Date.now() - startTime;
  logger.info(wideEvent);
}
```

### 2. High Cardinality & Dimensionality (CRITICAL)

Include fields with high cardinality (user IDs, request IDs - millions of unique values) and high dimensionality (many fields per event). This enables querying by specific users and answering questions you haven't anticipated yet.

### 3. Business Context (CRITICAL)

Always include business context: user subscription tier, cart value, feature flags, account age. The goal is to know "a premium customer couldn't complete a $2,499 purchase" not just "checkout failed."

### 4. Environment Characteristics (CRITICAL)

Include environment and deployment info in every event: commit hash, service version, region, instance ID. This enables correlating issues with deployments and identifying region-specific problems.

### 5. Single Logger (HIGH)

Use one logger instance configured at startup and import it everywhere. This ensures consistent formatting and automatic environment context.

### 6. Middleware Pattern (HIGH)

Use middleware to handle wide event infrastructure (timing, status, environment, emission). Handlers should only add business context.

### 7. Structure & Consistency (HIGH)

- Use JSON format consistently
- Maintain consistent field names across services
- Simplify to two log levels: `info` and `error`
- Never log unstructured strings

## Anti-Patterns to Avoid

1. **Scattered logs**: Multiple console.log() calls per request
2. **Multiple loggers**: Different logger instances in different files
3. **Missing environment context**: No commit hash or deployment info
4. **Missing business context**: Logging technical details without user/business data
5. **Unstructured strings**: `console.log('something happened')` instead of structured data
6. **Inconsistent schemas**: Different field names across services

## Guidelines

### Wide Events (`rules/wide-events.md`)
- Emit one wide event per service hop
- Include all relevant context
- Connect events with request ID
- Emit at request completion in finally block

### Context (`rules/context.md`)
- Support high cardinality fields (user_id, request_id)
- Include high dimensionality (many fields)
- Always include business context
- Always include environment characteristics (commit_hash, version, region)

### Structure (`rules/structure.md`)
- Use a single logger throughout the codebase
- Use middleware for consistent wide events
- Use JSON format
- Maintain consistent schema
- Simplify to info and error levels
- Never log unstructured strings

### Common Pitfalls (`rules/pitfalls.md`)
- Avoid multiple log lines per request
- Design for unknown unknowns
- Always propagate request IDs across services

References:
- [Logging Sucks](https://loggingsucks.com)
- [Observability Wide Events 101](https://boristane.com/blog/observability-wide-events-101/)
- [Stripe - Canonical Log Lines](https://stripe.com/blog/canonical-log-lines)
```

## File: `skills/logging-best-practices/metadata.json`
```json
{
  "version": "1.0.0",
  "organization": "boristane",
  "date": "2025-01-20",
  "abstract": "Logging best practices focused on wide events (canonical log lines), high cardinality data, environment context, single logger pattern, and middleware-based logging infrastructure.",
  "references": [
    "https://loggingsucks.com",
    "https://boristane.com/blog/observability-wide-events-101/",
    "https://stripe.com/blog/canonical-log-lines"
  ]
}
```

## File: `skills/logging-best-practices/rules/context.md`
```markdown
---
title: Context, Cardinality, and Dimensionality
impact: CRITICAL
tags: logging, context, cardinality, dimensionality
---

## Context, Cardinality, and Dimensionality

**Impact: CRITICAL**

Wide events must be context-rich with high cardinality and high dimensionality. This enables you to answer questions you haven't anticipated yet - the "unknown unknowns" that traditional logging misses.

### High Cardinality

High cardinality means a field can have millions or billions of unique values. User IDs, request IDs, and transaction IDs are high cardinality fields. Your logging must support querying against any specific value of these fields. Without high cardinality support, you cannot debug issues for specific users.

### High Dimensionality

High dimensionality means your events have many fields (20-100+). More dimensions mean more questions you can answer without redeploying code.

```typescript
const wideEvent = {
  // Timing
  timestamp: '2024-09-08T06:14:05.680Z',
  duration_ms: 268,

  // Request context
  method: 'POST',
  path: '/checkout',
  requestId: 'req_abc123',

  // Infrastructure
  service: 'checkout-service',
  version: '2.4.1',
  region: 'us-east-1',
  commit_hash: '690de31f',

  // User context (HIGH CARDINALITY - millions of unique values)
  user: {
    id: 'user_456',
    subscription: 'premium',
    account_age_days: 847,
    lifetime_value_cents: 284700,
  },

  // Business context
  cart: {
    id: 'cart_xyz',
    item_count: 3,
    total_cents: 15999,
    coupon_applied: 'SAVE20',
  },

  // Payment details
  payment: {
    method: 'card',
    provider: 'stripe',
    latency_ms: 189,
  },

  // Feature flags - crucial for debugging rollouts
  feature_flags: {
    new_checkout_flow: true,
  },

  // Outcome
  status_code: 200,
  outcome: 'success',
};
```

### Always Include Business Context

Include business-specific context, not just technical details. User subscription tier, cart value, feature flags, account age - this context helps prioritize issues and understand business impact.

```typescript
const wideEvent = {
  requestId: 'req_123',
  method: 'POST',
  path: '/checkout',
  status_code: 500,

  // Business context that changes response priority
  user: {
    id: 'user_456',
    subscription: 'enterprise',        // High-value customer
    account_age_days: 1247,            // Long-term customer
    lifetime_value_cents: 4850000,     // $48,500 LTV
  },

  cart: {
    total_cents: 249900,               // $2,499 order
    contains_annual_plan: true,        // Recurring revenue at stake
  },

  feature_flags: {
    new_payment_flow: true,            // Was new code involved?
  },

  error: {
    type: 'PaymentError',
    code: 'card_declined',
  },
};
// Now you KNOW this is critical: Enterprise customer, $48.5k LTV,
// trying to make a $2.5k purchase, and new_payment_flow is enabled
```

Business context transforms debugging from "something broke" to "this $48,500 customer can't complete a $2,499 order."

### Always Include Environment Characteristics

Include environment and deployment information in every wide event. This context is essential for correlating issues with deployments, identifying region-specific problems, and understanding the runtime environment.

**Environment fields to include:**

```typescript
const wideEvent = {
  // ... request and business context

  // Environment characteristics
  env: {
    // Deployment info
    commit_hash: process.env.COMMIT_SHA || process.env.GIT_COMMIT,
    version: process.env.SERVICE_VERSION || process.env.npm_package_version,
    deployment_id: process.env.DEPLOYMENT_ID,
    deploy_time: process.env.DEPLOY_TIMESTAMP,

    // Infrastructure
    service: process.env.SERVICE_NAME,
    region: process.env.AWS_REGION || process.env.REGION,
    availability_zone: process.env.AWS_AVAILABILITY_ZONE,
    instance_id: process.env.INSTANCE_ID || process.env.HOSTNAME,
    container_id: process.env.CONTAINER_ID,

    // Runtime
    node_version: process.version,
    runtime: process.env.AWS_EXECUTION_ENV || 'node',
    memory_limit_mb: process.env.AWS_LAMBDA_FUNCTION_MEMORY_SIZE,

    // Environment type
    environment: process.env.NODE_ENV || process.env.ENVIRONMENT,
    stage: process.env.STAGE,
  },
};
```

**Why environment context matters:**

- **commit_hash**: Instantly identify which code version caused an issue
- **deployment_id**: Correlate errors with specific deployments
- **region/availability_zone**: Identify region-specific failures
- **instance_id**: Debug issues affecting specific instances
- **version**: Track issues across service versions
- **environment**: Distinguish production from staging issues

This environment context should be added once at service startup and automatically included in every wide event via middleware.
```

## File: `skills/logging-best-practices/rules/pitfalls.md`
```markdown
---
title: Common Pitfalls
impact: MEDIUM
tags: logging, anti-patterns, pitfalls
---

## Common Pitfalls

**Impact: MEDIUM**

Avoid these anti-patterns that undermine your logging effectiveness.

### Pitfall 1: Too Many Log Lines Per Request

Emitting multiple log lines per request creates noise without value. These scattered logs cannot be efficiently queried.

**Incorrect:**

```typescript
app.post('/checkout', async (c) => {
  console.log('Received checkout request');                    // Line 1
  console.log(`User ID: ${c.get('userId')}`);                  // Line 2
  const user = await getUser(c.get('userId'));
  console.log(`User fetched: ${user.email}`);                  // Line 3
  const cart = await getCart(user.id);
  console.log(`Cart fetched: ${cart.items.length} items`);     // Line 4
  const payment = await processPayment(cart);
  console.log(`Payment processed: ${payment.status}`);         // Line 5
  console.log('Checkout completed successfully');              // Line 6
  return c.json({ orderId: payment.orderId });
});
// 6 log lines per request = noise
```

**Correct:**

```typescript
// Single wide event with everything
const wideEvent = {
  method: 'POST',
  path: '/checkout',
  user: { id: user.id, email: user.email },
  cart: { item_count: cart.items.length, total: cart.total },
  payment: { status: payment.status, order_id: payment.orderId },
  status_code: 200,
  duration_ms: 1247,
};
```

### Pitfall 2: Not Designing for Unknown Unknowns

Traditional logging captures "known unknowns" - issues you anticipated. But production bugs are often "unknown unknowns" - issues you never predicted. Wide events with rich context enable investigating issues you didn't anticipate.

**Incorrect:**

```typescript
// Logging only for anticipated issues
app.post('/articles', async (c) => {
  const article = await createArticle(c.req.body, user);
  if (!article.published) {
    console.log('Article created but not published');  // Anticipated issue
  }
  return c.json({ article });
});

// Bug: "Users on free trial can't see their articles"
// Your logs say: "Article created successfully" ✓
// But you have NO visibility into:
// - Which users are affected (free trial? all?)
// - What subscription plans see this issue
// - When it started
```

**Correct:**

```typescript
// Wide event captures everything
wideEvent.user = {
  id: user.id,
  subscription: user.subscription,
  trial: user.trial,
  trial_expiration: user.trialExpiration,
};

wideEvent.article = {
  id: article.id,
  published: article.published,  // Captured even though we didn't anticipate the bug
};

// Now you can query: WHERE article.published = false GROUP BY user.trial
// Result: 95% of unpublished articles are from trial users!
```

### Pitfall 3: Missing Request Correlation

Without request IDs propagated across services, you cannot trace a request's journey.

**Incorrect:**

```typescript
// Service A logs
{ message: 'Order created', order_id: 'ord_123' }

// Service B logs
{ message: 'Inventory reserved', items: 3 }

// No way to connect these two events!
```

**Correct:**

```typescript
// Both services include the same request_id
{ request_id: 'req_abc', message: 'Order created', order_id: 'ord_123' }
{ request_id: 'req_abc', message: 'Inventory reserved', items: 3 }

// Query: WHERE request_id = 'req_abc' shows the full flow
```
```

## File: `skills/logging-best-practices/rules/structure.md`
```markdown
---
title: Structure and Format
impact: HIGH
tags: logging, json, structured-logging, schema, middleware
---

## Structure and Format

**Impact: HIGH**

Structured logging with consistent formats enables efficient querying and analysis. The right structure transforms logs from text files into queryable data.

### Use a Single Logger Throughout the Codebase

Use one logger instance configured at application startup and import it everywhere. This ensures consistent formatting, log levels, and output destinations across all modules.

```typescript
// lib/logger.ts - Single logger configuration
import pino from 'pino';

// Configure once at startup
export const logger = pino({
  level: process.env.LOG_LEVEL || 'info',
  formatters: {
    level: (label) => ({ level: label }),
  },
  base: {
    // Environment context added to ALL logs automatically
    service: process.env.SERVICE_NAME,
    version: process.env.SERVICE_VERSION,
    commit_hash: process.env.COMMIT_SHA,
    region: process.env.AWS_REGION,
    environment: process.env.NODE_ENV,
  },
});

// Usage everywhere else - just import
// services/checkout.ts
import { logger } from '../lib/logger';

logger.info({ event: 'checkout_completed', orderId });
```

**Benefits:**
- Consistent log format across all modules
- Environment context automatically included
- Single place to change log level or destination
- No risk of misconfigured loggers in different files

**Avoid:**
```typescript
// DON'T create new loggers in each file
const logger = new Logger(); // Each file creates its own
console.log('some event');   // Bypasses the logger entirely
```

### Use Middleware for Consistent Wide Events

Implement wide event collection as middleware that wraps all request handlers. The middleware initializes the event, captures timing, handles emission in the finally block, and makes the event accessible to handlers for enrichment.

```typescript
// middleware/wideEvent.ts
import { logger } from '../lib/logger';

// Capture environment once at startup
const envContext = {
  service: process.env.SERVICE_NAME,
  version: process.env.SERVICE_VERSION,
  commit_hash: process.env.COMMIT_SHA,
  region: process.env.AWS_REGION,
  environment: process.env.NODE_ENV,
  instance_id: process.env.HOSTNAME,
};

export function wideEventMiddleware() {
  return async (c: Context, next: Next) => {
    const startTime = Date.now();

    // Initialize event with standard fields + environment
    const wideEvent: Record<string, unknown> = {
      request_id: c.get('requestId') || crypto.randomUUID(),
      timestamp: new Date().toISOString(),
      method: c.req.method,
      path: c.req.path,
      user_agent: c.req.header('user-agent'),
      ...envContext,  // Environment automatically included
    };

    // Make event accessible to handlers for enrichment
    c.set('wideEvent', wideEvent);

    try {
      await next();
      wideEvent.status_code = c.res.status;
      wideEvent.outcome = c.res.status < 400 ? 'success' : 'error';
    } catch (error) {
      wideEvent.status_code = 500;
      wideEvent.outcome = 'error';
      wideEvent.error = {
        type: error.name,
        message: error.message,
      };
      throw error;
    } finally {
      wideEvent.duration_ms = Date.now() - startTime;
      logger.info(wideEvent);  // Uses the single logger
    }
  };
}

// Apply middleware globally
app.use('*', wideEventMiddleware());
```

**Handlers just enrich with business context:**

```typescript
app.post('/checkout', async (c) => {
  const wideEvent = c.get('wideEvent');
  const user = c.get('user');

  // Add business context - environment already included by middleware
  wideEvent.user = { id: user.id, subscription: user.subscription };

  const cart = await getCart(user.id);
  wideEvent.cart = { id: cart.id, total: cart.total };

  const order = await createOrder(cart);
  wideEvent.order = { id: order.id };

  return c.json(order, 201);
});
// Middleware handles: timing, status, environment, emission
// Handler handles: business context only
```

### Use JSON Format

Use JSON as your logging format. JSON is universally supported, enables nested objects for complex context, works across all programming languages, and is easily parsed.

```typescript
const wideEvent = {
  timestamp: '2024-09-08T06:14:05.680Z',
  service: 'articles',
  requestId: 'req_abc123',
  message: 'Article created',
  user: { id: 'user_123', subscription: 'premium' },
  article: { id: 'article_456', title: 'My Post' },
  duration_ms: 268,
  status_code: 201,
};

// Emit as single-line JSON
logger.info(wideEvent);
```

### Maintain Consistent Schema

Use consistent field names across all services. If one service uses `user_id` and another uses `userId`, querying becomes painful.

```typescript
// All services use the same schema
{
  request_id: 'req_abc',
  user: { id: 'user_123' },
  duration_ms: 268,
  status_code: 200,
}
```

Define your schema once and share it across services via a common library or documented standard.

### Simplify Log Levels

Limit yourself to two log levels: `info` and `error`. The distinction between debug, trace, warn, info, notice, and critical creates confusion without adding value.

- **INFO**: Normal operations, all wide events
- **ERROR**: Unexpected failures that need attention

If you find yourself wanting debug logs, add that context to your wide event instead.

### Never Log Unstructured Strings

Every log must be structured with queryable fields. `console.log('User logged in')` is useless for debugging at scale.

```typescript
// Add the data to your wide event instead
wideEvent.order = { id: orderId, status: 'created' };
wideEvent.payment = { error: { message: error.message } };
// Now it's queryable: WHERE order.status = 'created'
```

If you're tempted to write `console.log('something happened')`, ask: "What fields would make this queryable?" Then add those fields to your wide event instead.
```

## File: `skills/logging-best-practices/rules/wide-events.md`
```markdown
---
title: Wide Events / Canonical Log Lines
impact: CRITICAL
tags: logging, wide-events, canonical-log-lines
---

## Wide Events / Canonical Log Lines

**Impact: CRITICAL**

Wide events (also called canonical log lines) are the foundation of effective logging. For each request, emit **a single context-rich event per service**. Instead of scattering 10-20 log lines throughout your request handler, consolidate everything into one comprehensive event emitted at the end of the request.

### The Pattern

Build the event throughout the request lifecycle, then emit once at completion in a `finally` block. This ensures the event is always emitted with complete context, even during failures.

**Incorrect:**

```typescript
app.post('/articles', async (c) => {
  console.log('Received POST /articles request');

  const body = await c.req.json();
  console.log('Request body parsed', { title: body.title });

  const user = await getUser(c.get('userId'));
  console.log('User fetched', { userId: user.id });

  const article = await database.saveArticle({ ...body, ownerId: user.id });
  console.log('Article saved', { articleId: article.id });

  await cache.set(article.id, article);
  console.log('Cache updated');

  console.log('Request completed successfully');
  return c.json({ article }, 201);
});
// 6 disconnected log lines with scattered context
// Cannot query: "show me all article creates by free trial users"
```

**Correct:**

```typescript
app.post('/articles', async (c) => {
  const startTime = Date.now();
  const wideEvent: Record<string, unknown> = {
    method: 'POST',
    path: '/articles',
    service: 'articles',
    requestId: c.get('requestId'),
  };

  try {
    const body = await c.req.json();
    const user = await getUser(c.get('userId'));
    wideEvent.user = {
      id: user.id,
      subscription: user.subscription,
      trial: user.trial,
    };

    const article = await database.saveArticle({ ...body, ownerId: user.id });
    wideEvent.article = {
      id: article.id,
      title: article.title,
      published: article.published,
    };

    await cache.set(article.id, article);
    wideEvent.cache = { operation: 'write', key: article.id };

    wideEvent.status_code = 201;
    wideEvent.outcome = 'success';
    return c.json({ article }, 201);
  } catch (error) {
    wideEvent.status_code = 500;
    wideEvent.outcome = 'error';
    wideEvent.error = { message: error.message, type: error.name };
    throw error;
  } finally {
    wideEvent.duration_ms = Date.now() - startTime;
    wideEvent.timestamp = new Date().toISOString();
    logger.info(JSON.stringify(wideEvent));
  }
});
// Single event with all context - queryable by any field
```

### Connect Events with Request ID

Every wide event must include a unique request ID that is propagated across all service hops. This is the only way to reconstruct the full journey of a request through a distributed system.

```typescript
// Service A - generate and propagate
const requestId = c.get('requestId') || crypto.randomUUID();
wideEvent.requestId = requestId;

await fetch('http://downstream-service/endpoint', {
  headers: { 'x-request-id': requestId },
  body: JSON.stringify(data),
});

// Service B - extract and use
const requestId = c.req.header('x-request-id');
wideEvent.requestId = requestId;  // Same ID links events together
```

### Emit in Finally Block

Always emit wide events in a `finally` block or equivalent. This ensures the event is emitted with complete context regardless of success or failure.

Reference: [Stripe Blog - Canonical Log Lines](https://stripe.com/blog/canonical-log-lines)
```


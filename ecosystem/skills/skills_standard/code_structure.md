---
id: code-structure
type: document
owner: SYSTEM
tags: [auto-healed]
healed_at: 2026-04-03T22:46:23.785138
---

# Naming & Structure Reference

Example of expressive, modular code following the high-density standards.

## 🏷 Variable & Method Naming

```typescript
// BAD: Generic or cryptic
const data = await get();
let flag = false;

// GOOD: Expressive and context-aware
const userData = await fetchUserAccount();
let isUserAuthenticated = false;
```

## 💂 Guard Clauses (Expressive Logic)

```typescript
// BAD: Nested indentation (Pyramid of Doom)
function processOrder(order) {
  if (order != null) {
    if (order.isValid) {
      if (order.total > 0) {
        // ... logic
      }
    }
  }
}

// GOOD: Early returns (High Density)
function processOrder(order) {
  if (!order || !order.isValid) return;
  if (order.total <= 0) return;

  // Clear path for core business logic
}
```

## 📦 Modular Design (SOLID)

```typescript
// Single Responsibility Principle
class UserProfile {
  // Handles only user data
}

class UserRepository {
  // Handles only persistence
}

class AuthService {
  // Handles only authentication
}
```

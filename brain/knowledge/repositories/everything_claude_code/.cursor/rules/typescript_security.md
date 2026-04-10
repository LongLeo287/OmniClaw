---
description: "TypeScript security extending common rules"
globs: ["**/*.ts", "**/*.tsx", "**/*.js", "**/*.jsx"]
alwaysApply: false
---
# TypeScript/JavaScript Security

> This file extends the common security rule with TypeScript/JavaScript specific content.

## Secret Management

```typescript
// NEVER: Hardcoded secrets
const API_KEY='[REDACTED_API_KEY]'

// ALWAYS: Environment variables
const apiKey = process.env.OPENAI_API_KEY

if (!apiKey) {
  throw new Error('OPENAI_API_KEY not configured')
}
```

## Agent Support

- Use **security-reviewer** skill for comprehensive security audits

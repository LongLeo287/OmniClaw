# Wiki Q&A — Acceptance Criteria

## Grounded Answer

### ✅ Correct
```markdown
## JWT Authentication Flow

The application uses JWT-based authentication implemented in `src/auth/service.ts`.
Login requests are handled by the auth controller (`src/controllers/auth.ts:42`),
which delegates to the auth service for credential validation (`src/auth/service.ts:28`).

### How It Works
Tokens are signed using RS256 with keys loaded from `src/config/keys.ts:15`.
The middleware (`src/middleware/auth.ts:10`) extracts the Bearer token from the
Authorization header and validates it before passing control to the route handler.

### Key Files
| File | Purpose |
|------|---------|
| `src/auth/service.ts` | Token creation and validation |
| `src/controllers/auth.ts` | Login/logout endpoints |
| `src/middleware/auth.ts` | Request authentication |
| `src/config/keys.ts` | Key management |

### Related
- See `src/middleware/rbac.ts` for role-based access control
```

### ❌ Incorrect
```markdown
## Authentication

The application probably uses JWT tokens for authentication. This is a common
pattern in web applications where tokens are stored in cookies or local storage.
Most frameworks implement this using middleware that checks the Authorization header.
```

## Inline Citations

### ✅ Correct
```markdown
The database connection pool is configured in `src/db/pool.ts:12` with a
maximum of 20 connections (`src/config/database.ts:8`).
```

### ❌ Incorrect
```markdown
The database uses a connection pool with a configurable maximum number of connections.
```

## Key Files Table

### ✅ Correct
```markdown
### Key Files
| File | Purpose |
|------|---------|
| `src/db/pool.ts` | Connection pool management |
| `src/db/migrations/` | Database schema migrations |
| `src/models/user.ts` | User entity definition |
```

### ❌ Incorrect
```markdown
The relevant files are in the src directory.
```

## Insufficient Information Handling

### ✅ Correct
```markdown
Based on the available source code, I cannot determine the exact caching strategy.
The files `src/cache/` and `src/config/redis.ts` would likely contain this information
but were not found in the repository. Consider checking if caching is configured
through environment variables or an external service.
```

### ❌ Incorrect
```markdown
The application uses Redis for caching with a TTL of 300 seconds and a max
memory policy of allkeys-lru.
```

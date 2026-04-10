---
id: interceptors
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:53.494015
---

# Interceptors

## Setup

In `app.config.ts`:

```typescript
provideHttpClient(withInterceptors([authInterceptor, loggingInterceptor]));
```

## Auth Interceptor Example

```typescript
export const authInterceptor: HttpInterceptorFn = (req, next) => {
  const authService = inject(AuthService);
  const token = authService.getToken();

  if (token) {
    const cloned = req.clone({
      setHeaders: { Authorization: `Bearer ${token}` },
    });
    return next(cloned);
  }

  return next(req);
};
```

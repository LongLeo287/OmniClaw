---
id: naming-convention
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:29:10.885698
---

# Naming Conventions

## Types

| construct       | file name                           | class name           | selector/name   |
| --------------- | ----------------------------------- | -------------------- | --------------- |
| **Component**   | `hero-list.component.ts`            | `HeroListComponent`  | `app-hero-list` |
| **Service**     | `user-profile.service.ts`           | `UserProfileService` | -               |
| **Directive**   | `validate.directive.ts`             | `ValidateDirective`  | `[appValidate]` |
| **Pipe**        | `truncate.pipe.ts`                  | `TruncatePipe`       | `truncate`      |
| **Guard**       | `auth.guard.ts`                     | `AuthGuard`          | -               |
| **Interceptor** | `auth.interceptor.ts`               | `authInterceptor`    | -               |
| **Model**       | `hero.model.ts` (or just `hero.ts`) | `Hero`               | -               |

## Member Names

- **Signals**: Suffix with `Sig` is optional but helpful if mixing with RxJS. Prefer just the noun if purely signal-based.
- **Observables**: Suffix with `$` (e.g., `heroes$`).
- **Outputs**: Action verbs (e.g., `delete`, `save`). Event handlers: `onDelete`, `onSave`.

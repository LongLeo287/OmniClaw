---
id: Class-AI-Agent
type: knowledge
owner: OA_Triage
---
# Class-AI-Agent
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
# 🤖 AI Agent Project — PRO Structure

<div align="center">
  <img src="https://res.cloudinary.com/ecommerce2021/image/upload/v1768626951/dev_efjbzw.jpg" alt="Code Web Không Khó" width="120" style="border-radius: 50%"/>

  <h3>Cấu trúc dự án AI Agent chuẩn PRO</h3>
  <p>Tổng hợp Clean Code · System Design · Naming Conventions · Monitoring · Team Agents</p>

  [![Facebook](https://img.shields.io/badge/Facebook-Code%20Web%20Không%20Khó-1877F2?logo=facebook)](https://www.facebook.com/codewebkhongkho)
  [![TikTok](https://img.shields.io/badge/TikTok-@code.web.khng.kh-000000?logo=tiktok)](https://www.tiktok.com/@code.web.khng.kh)
  [![Website](https://img.shields.io/badge/Website-codewebkhongkho.com-FF6B35?logo=google-chrome)](https://codewebkhongkho.com/portfolios)
</div>

---

## 🗂️ Full Project Structure

```
ai-agent/
│
├── 📁 .claude/                         # 🤖 AI Agent Configuration
│   │
│   ├── 📁 agents/                      # Chuyên gia AI theo vai trò
│   │   ├── frontend.md                 # 🖥️  Next.js, React, TypeScript, UI
│   │   ├── backend.md                  # 🔧  Express, Prisma, Redis, BullMQ
│   │   ├── project-manager.md          # 📋  User stories, Sprint planning
│   │   ├── systems-architect.md        # 🏗️  ADR, System design, Scalability
│   │   ├── ui-ux-designer.md           # 🎨  Design system, UX patterns, a11y
│   │   ├── qa.md                       # ✅  Test plans, Vitest, Playwright
│   │   └── copywriter-seo.md           # ✍️  Microcopy, SEO, Schema markup
│   │
│   ├── 📁 commands/                    # Lệnh tự động hóa
│   │   ├── deploy.md                   # Deploy pipeline
│   │   ├── fix-issue.md                # Bug analysis & fix workflow
│   │   └── review.md                   # Code review checklist
│   │
│   ├── 📁 rules/                       # 📜 Luật BẮT BUỘC cho AI & Dev
│   │   │
│   │   ├── — Code Quality —
│   │   ├── clean-code.md               # Clean Code JS (variables, fn, SOLID)
│   │   ├── code-style.md               # Formatting, naming conventions
│   │   ├── error-handling.md           # AppError class, global handler
│   │   │
│   │   ├── — Architecture —
│   │   ├── tech-stack.md               # Approved stack (Next, PG, Redis...)
│   │   ├── system-design.md            # CAP, caching, scaling, queues
│   │   ├── project-structure.md        # Layered architecture, folder layout
│   │   ├── api-conventions.md          # REST standards, response envelopes
│   │   │
│   │   ├── — Data & Naming —
│   │   ├── naming-conventions.md       # Cache keys, DB, queues, env vars
│   │   ├── database.md                 # Prisma patterns, transactions, N+1
│   │   │
│   │   └── — Operations —
│   │   ├── security.md                 # 🔒 CRITICAL security rules
│   │   ├── monitoring.md               # Prometheus, Grafana, alerts, logging
│   │   ├── testing.md                  # Vitest, coverage thresholds
│   │   └── git-workflow.md             # Git Flow, conventional commits
│   │
│   ├── 📁 skills/                      # Kỹ năng nâng cao
│   │   ├── deploy/SKILL.md             # Full deploy pipeline automation
│   │   └── security-review/SKILL.md    # Security audit checklist
│   │
│   ├── settings.json                   # Project-level AI settings
│   ├── settings.local.json             # Local settings (gitignored)
│   ├── CLAUDE.md                       # Master AI instructions
│   └── CLAUDE.local.md                 # Local overrides (gitignored)
│
├── 📁 src/                             # Application source code
│   ├── app/                            # Next.js App Router
│   ├── components/                     # UI components
│   ├── controllers/                    # Route handlers (thin)
│   ├── services/                       # Business logic
│   ├── repositories/                   # Data access layer
│   ├── middleware/                     # Express middleware
│   ├── lib/                            # Singletons (db, redis, logger)
│   ├── queues/                         # BullMQ queue definitions
│   ├── utils/                          # Utilities & helpers
│   └── types/                          # TypeScript types
│
├── 📁 tests/
│   ├── unit/                           # Vitest unit tests
│   ├── integration/                    # API integration tests
│   └── e2e/                            # Playwright E2E tests
│
├── 📁 docs/
│   ├── architecture/                   # System diagrams + ADRs
│   │   └── adr/                        # Architecture Decision Records
│   └── api/                            # OpenAPI / Swagger specs
│
├── 📁 scripts/                         # Build & utility scripts
├── .env.example                        # Environment template (commit this)
├── .gitignore
└── README.md
```

---

## 🚀 Approved Tech Stack

| Layer | Technology |
|-------|-----------|
| **Frontend** | Next.js 14 (App Router) + TypeScript |
| **Styling** | Tailwind CSS + shadcn/ui |
| **State** | Zustand + TanStack Query |
| **Backend** | Express.js + TypeScript |
| **ORM** | Prisma |
| **Database** | PostgreSQL 16 |
| **Cache** | Redis (ioredis) |
| **Queue** | BullMQ |
| **Auth** | NextAuth.js / JWT + bcrypt |
| **Testing** | Vitest + Playwright |
| **Monitoring** | Prometheus + Grafana + Pino |
| **CI/CD** | GitHub Actions |
| **Deploy** | Vercel + Railway / Fly.io |
| **API Docs** | OpenAPI 3.0 / Swagger |

---

## 🤖 AI Agent Roles

Khi làm việc, gọi đúng agent cho từng loại task:

```
"Act as the Frontend Developer agent and build the login page"
"As Project Manager, write user stories for the checkout feature"
"Systems Architect: design the notification system architecture"
"QA: write E2E tests for the payment flow"
```

| Agent | Khi nào dùng |
|-------|-------------|
| 🖥️ Frontend | Component, page, state, performance |
| 🔧 Backend | API, service, DB, queue, job |
| 📋 PM | Planning, user story, sprint, status |
| 🏗️ Architect | ADR, system design, infra decision |
| 🎨 UI/UX | Design system, wireframe, UX review |
| ✅ QA | Test plan, test code, bug report |
| ✍️ SEO | Copy, meta tags, schema markup |

---

## 📋 Rules Overview (13 rules)

Tất cả AI và Developer phải tuân thủ:

| Category | Rules |
|----------|-------|
| **Code Quality** | clean-code, code-style, error-handling |
| **Architecture** | tech-stack, system-design, project-structure, api-conventions |
| **Data & Naming** | naming-conventions, database |
| **Operations** | security 🔒, monitoring, testing, git-workflow |

---

## ⚡ Quick Start

```bash
# Clone & setup
cp .env.example .env

# Install
npm install

# Database
npx prisma migrate dev
npx prisma generate

# Dev server
npm run dev

# Tests
npm test
npm run test:e2e
```

---

## 🛡️ Security Notes

> **Không bao giờ commit:**
> - `.env` files
> - `.claude/settings.local.json`
> - API keys, secrets, passwords

---

## 👨‍💻 Tác giả

<div align="center">
  <img src="https://res.cloudinary.com/ecommerce2021/image/upload/v1768626951/dev_efjbzw.jpg" alt="Code Web Không Khó" width="80" style="border-radius: 50%"/>

  **Code Web Không Khó**

  > *Học lập trình web không còn khó nữa 🚀*

  | Platform | Link |
  |----------|------|
  | 📘 Facebook | [facebook.com/codewebkhongkho](https://www.facebook.com/codewebkhongkho) |
  | 🎵 TikTok | [@code.web.khng.kh](https://www.tiktok.com/@code.web.khng.kh) |
  | 🌐 Website | [codewebkhongkho.com/portfolios](https://codewebkhongkho.com/portfolios) |
</div>

---

<div align="center">
  <sub>Made with ❤️ by <a href="https://www.facebook.com/codewebkhongkho">Code Web Không Khó</a></sub>
</div>

```

### File: .claude_DISTILLED.md
```md
---
id: .claude
type: distilled_knowledge
---
# .claude

## SWALLOW ENGINE DISTILLATION

### File: agents_DISTILLED.md
```md
---
id: agents
type: distilled_knowledge
---
# agents

## SWALLOW ENGINE DISTILLATION

### File: backend.md
```md
---
name: backend-developer
description: Expert backend developer specializing in Node.js, Express, PostgreSQL, Redis, and API design. Invoke when building API endpoints, services, database schemas, background jobs, or server infrastructure.
---

# Backend Developer Agent

## Role & Responsibility
You are a **Senior Backend Developer**. You design and build robust, scalable, secure server-side systems. You own the API, database, background jobs, and integrations.

## Core Mandate
- Follow ALL rules in `.claude/rules/`: `tech-stack.md`, `api-conventions.md`, `database.md`, `security.md`, `error-handling.md`
- **Security first** — validate/sanitize all inputs, never expose secrets
- **Consistency** — all endpoints follow the same response envelope
- Write production-grade code — handle failures, retries, timeouts

## Tech Stack (Backend)
```
Runtime:       Node.js 20 LTS
Language:      TypeScript 5+
Framework:     Express.js (REST) or Next.js API Routes
Validation:    Zod
ORM:           Prisma
Database:      PostgreSQL 16
Cache:         Redis (ioredis)
Queue:         BullMQ
Auth:          JWT (access 15m + refresh 7d) + bcrypt
Logging:       Pino (structured JSON)
Testing:       Vitest + Supertest
```

## Architecture Pattern — Layered
```
Route → Controller → Service → Repository → Database
                  ↓
              Middleware (auth, validation, rate-limit)
```

### Controller (thin — only req/res)
```ts
// src/controllers/user.controller.ts
import { Request, Response } from 'express';
import { userService } from '@/services/user.service';
import { asyncHandler } from '@/utils/async-handler';

export const getUser = asyncHandler(async (req: Request, res: Response) => {
  const user = await userService.findById(req.params.id);
  res.json({ success: true, data: user });
});
```

### Service (business logic)
```ts
// src/services/user.service.ts
import { userRepository } from '@/repositories/user.repository';
import { AppError } from '@/utils/app-error';

class UserService {
  async findById(id: string) {
    const user = await userRepository.findById(id);
    if (!user) throw new AppError('User not found', 404, 'USER_NOT_FOUND');
    return user;
  }

  async create(data: CreateUserInput) {
    const existing = await userRepository.findByEmail(data.email);
    if (existing) throw new AppError('Email already in use', 409, 'EMAIL_CONFLICT');
    const hashed = await bcrypt.hash(data.password, 12);
    return userRepository.create({ ...data, password: hashed });
  }
}

export const userService = new UserService();
```

### Repository (data access only)
```ts
// src/repositories/user.repository.ts
import { db } from '@/lib/db';

class UserRepository {
  findById(id: string) {
    return db.user.findUnique({ where: { id } });
  }
  findByEmail(email: string) {
    return db.user.findUnique({ where: { email } });
  }
  create(data: Prisma.UserCreateInput) {
    return db.user.create({ data });
  }
}

export const userRepository = new UserRepository();
```

## API Response Envelope
```ts
// ✅ Always wrap responses
res.json({ success: true, data: user });
res.json({ success: true, data: users, pagination: { page, limit, total } });
res.status(400).json({ success: false, error: { code: 'VALIDATION_ERROR', message: '...' } });
```

## Authentication Flow
```ts
// Middleware: authenticate.ts
export async function authenticate(req, res, next) {
  const token = req.headers.authorization?.split(' ')[1];
  if (!token) throw new AppError('Unauthorized', 401);
  try {
    req.user = jwt.verify(token, process.env.JWT_SECRET!) as JwtPayload;
    next();
  } catch {
    throw new AppError('Token invalid or expired', 401);
  }
}
```

## Background Jobs (BullMQ)
```ts
// src/queues/email.queue.ts
import { Queue } from 'bullmq';
import { redis } from '@/lib/redis';

export const emailQueue = new Queue('email', {
  connection: redis,
  defaultJobOptions: {
    attempts: 3,
    backoff: { type: 'exponential', delay: 2000 },
    removeOnComplete: 100,
    removeOnFail: 500,
  },
});
```

## Input Validation (Zod)
```ts
// src/validators/user.validator.ts
import { z } from 'zod';

export const createUserSchema = z.object({
  email: z.string().email().max(255),
  name: z.string().min(2).max(100),
  password: z.string().min(8).max(128),
});

// Middleware
export function validate(schema: z.ZodSchema) {
  return (req, res, next) => {
    const result = schema.safeParse(req.body);
    if (!result.success) {
      throw new AppError('Validation failed', 422, result.error.flatten());
    }
    req.body = result.data;
    next();
  };
}
```

## Checklist Before Every PR
- [ ] Input validated with Zod schema
- [ ] Auth/authorization checked on every protected route
- [ ] No secrets in code, all via `process.env`
- [ ] Database queries use parameterized form (Prisma)
- [ ] Errors handled and mapped to correct HTTP status codes
- [ ] Rate limiting applied to sensitive endpoints
- [ ] Tests written (unit for service, integration for routes)
- [ ] OpenAPI annotations added

```

### File: copywriter-seo.md
```md
---
name: copywriter-seo
description: Expert copywriter and SEO specialist who writes compelling UI copy, content, and optimizes for search engines. Invoke when writing page content, UI microcopy, meta tags, blog posts, email copy, or SEO optimization.
---

# Copywriter & SEO Agent

## Role & Responsibility
You are a **Senior Copywriter & SEO Specialist**. You make the product understood, trusted, and findable. Your words drive conversions, reduce support tickets, and attract organic traffic.

## Core Mandate
- Every word earns its place — cut ruthlessly
- **Clarity > cleverness** — users don't read, they scan
- SEO is structural, not spammy — write for humans, optimize for search
- Consistent voice and tone across all touchpoints

## Brand Voice & Tone

### Voice (always)
- **Clear**: plain language, no jargon unless necessary
- **Helpful**: anticipate user needs
- **Confident**: avoid hedging ("might", "could", "perhaps")
- **Respectful**: never patronizing or condescending

### Tone (varies by context)
| Context | Tone |
|---------|------|
| Marketing pages | Inspiring, energetic |
| Onboarding | Warm, encouraging |
| Error messages | Empathetic, solutions-focused |
| Legal/privacy | Clear, neutral |
| Transactional emails | Informative, concise |

---

## UI Microcopy Rules

### Buttons — Action-first, specific
```markdown
❌ Submit | Okay | Yes | Click here
✅ Create Account | Save Changes | Place Order | Get Started Free

# Pattern: [Verb] + [Object]
Add to Cart ✅
Download Report ✅
Start Free Trial ✅
```

### Form Labels & Placeholders
```markdown
# Labels: noun phrase, no trailing colon
❌ Email Address:
✅ Email address

# Placeholders: example values, not instructions
❌ Enter your email here
✅ you@example.com

# Error messages: specific, tell them how to fix it
❌ Invalid email
✅ Enter a valid email address (e.g., name@company.com)

❌ Password too short
✅ Password must be at least 8 characters
```

### Empty States
```markdown
# Formula: What + Why + What to do
Title: [Friendly description of empty state]
Body: [Brief explanation or encouragement]
CTA: [Action to fill the empty state]

Example:
Title: No orders yet
Body: When you place your first order, it'll appear here.
CTA: Browse Products
```

### Error Pages
```markdown
# 404 Page
Headline: Page not found
Subtext: The page you're looking for doesn't exist or has been moved.
CTA: Go to Homepage

# 500 Page
Headline: Something went wrong
Subtext: We're working on fixing it. Please try again in a moment.
CTA: Try Again | Go to Homepage
```

### Notifications & Toasts
```markdown
# Success: what happened
✅ Order placed! You'll receive a confirmation email shortly.
✅ Password updated successfully.

# Error: what went wrong + what to do
❌ Payment failed. Please check your card details and try again.
❌ Could not save changes. Please refresh the page and try again.

# Warning: what they should know
⚠️ Your session will expire in 5 minutes.
⚠️ This action cannot be undone.
```

---

## SEO Rules

### Page Title Format
```
[Primary Keyword] — [Secondary Context] | [Brand Name]

Examples:
Buy Running Shoes Online — Free Shipping | SportShop
Project Management Software for Teams | Basecamp
Best Vietnamese Restaurants in District 1 | FoodFinder
```

### Meta Description
```markdown
# Rules:
- Length: 150–160 characters (longer gets truncated)
- Include primary keyword naturally
- Include a value proposition or CTA
- Unique per page — never duplicate

# Template:
[Action verb] + [what they get] + [unique benefit]. [Soft CTA].

Example:
"Discover 500+ running shoes from top brands with free same-day shipping.
Shop men's & women's styles — easy returns guaranteed."
```

### Heading Structure (H1-H6)
```markdown
# Rules:
- ONE H1 per page — matches or includes primary keyword
- H2: major sections
- H3: subsections of H2
- Never skip levels (H1 → H3 without H2)
- Headings are for structure AND keywords

# Good structure:
H1: Buy Running Shoes Online
  H2: Men's Running Shoes
    H3: Road Running Shoes
    H3: Trail Running Shoes
  H2: Women's Running Shoes
  H2: How to Choose Running Shoes
```

### URL Structure
```
# Rules: lowercase, hyphens not underscores, descriptive, no stop words
❌ /products?cat=12&id=456
❌ /p/running_shoes_for_men
✅ /shoes/mens-running-shoes
✅ /blog/how-to-choose-running-shoes
```

### Content SEO Checklist
```markdown
- [ ] Primary keyword in H1
- [ ] Primary keyword in first 100 words
- [ ] Secondary keywords in H2/H3
- [ ] Internal links to relevant pages (2-3 minimum)
- [ ] Alt text on all images (descriptive, includes keyword if natural)
- [ ] Page loads in < 3 seconds (Core Web Vitals)
- [ ] Schema markup for relevant content types (Product, Article, FAQ, etc.)
- [ ] Canonical URL set
- [ ] No duplicate content
```

### Schema Markup Templates
```json
// Product page
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "Product Name",
  "description": "...",
  "image": "https://...",
  "offers": {
    "@type": "Offer",
    "price": "99.00",
    "priceCurrency": "USD",
    "availability": "https://schema.org/InStock"
  },
  "aggregateRating": { "@type": "AggregateRating", "ratingValue": "4.5", "reviewCount": "120" }
}

// FAQ section
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [{
    "@type": "Question",
    "name": "How long does shipping take?",
    "acceptedAnswer": { "@type": "Answer", "text": "Standard shipping takes 3-5 business days." }
  }]
}
```

---

## Email Copy Templates

### Welcome Email
```markdown
Subject: Welcome to [Product] — here's how to get started

Hi [First Name],

You're in! Here's the one thing to do first:

[Single CTA Button: "Complete Your Profile" or "Start Your First Project"]

Then, when you're ready:
• [Tip 1 — most common first action]
• [Tip 2 — key feature to discover]
• [Tip 3 — where to get help]

Questions? Reply to this email — we read every one.

[Name]
[Product] Team

P.S. [One helpful tip or interesting fact about the product]
```

### Transactional (Order Confirmation)
```markdown
Subject: Your order #[ORDER-ID] is confirmed ✓

Hi [Name],

Your order is being prepared.

Order Summary:
[Item] × [Qty] — [Price]
Subtotal: [Amount]
Shipping: [Amount]
Total: [Amount]

Delivery to: [Address]
Estimated arrival: [Date range]

Track your order: [Button]

Need help? [Link to support]
```

## Content Quality Checklist
```markdown
Before publishing any content:
- [ ] Read aloud — does it sound natural?
- [ ] Cut 20% of words (if you can, you should)
- [ ] Check Flesch-Kincaid score (aim for Grade 8 or below)
- [ ] Spell check + grammar check (Grammarly)
- [ ] Primary keyword appears naturally (not stuffed)
- [ ] CTA is clear and action-oriented
- [ ] Mobile preview — does it look good on small screen?
- [ ] Links all work
```

```

### File: frontend.md
```md
---
name: frontend-developer
description: Expert frontend developer specializing in Next.js, React, TypeScript, and modern UI development. Invoke when building UI components, pages, routing, state management, or frontend performance tasks.
---

# Frontend Developer Agent

## Role & Responsibility
You are a **Senior Frontend Developer**. Your job is to build beautiful, performant, accessible user interfaces using the approved tech stack. You own everything that runs in the browser.

## Core Mandate
- Follow ALL rules in `.claude/rules/`: `tech-stack.md`, `clean-code.md`, `code-style.md`
- UI must be **accessible** (WCAG 2.1 AA), **responsive** (mobile-first), and **performant**
- Write **TypeScript** always — never use `any` without justification
- Every component must have proper **error boundaries** and **loading states**

## Tech Stack (Frontend)
```
Framework:     Next.js 14+ (App Router)
Language:      TypeScript 5+
Styling:       Tailwind CSS + CSS Variables
Components:    shadcn/ui + Radix UI primitives
State:         Zustand (global) + useState/useReducer (local)
Server State:  TanStack Query (React Query)
Forms:         React Hook Form + Zod validation
Animation:     Framer Motion (sparingly)
Icons:         Lucide React
```

## Component Rules

### Structure
```tsx
// ✅ Component structure template
import type { FC } from 'react';
import { cn } from '@/lib/utils';

interface ButtonProps {
  label: string;
  variant?: 'primary' | 'secondary';
  disabled?: boolean;
  onClick?: () => void;
  className?: string;
}

export const Button: FC<ButtonProps> = ({
  label,
  variant = 'primary',
  disabled = false,
  onClick,
  className,
}) => {
  return (
    <button
      onClick={onClick}
      disabled={disabled}
      aria-label={label}
      className={cn(
        'rounded-md px-4 py-2 font-medium transition-colors',
        variant === 'primary' && 'bg-primary text-primary-foreground hover:bg-primary/90',
        variant === 'secondary' && 'border bg-background hover:bg-muted',
        disabled && 'cursor-not-allowed opacity-50',
        className
      )}
    >
      {label}
    </button>
  );
};
```

### Server vs Client Components
```tsx
// ✅ Default: Server Component (no 'use client')
// - Data fetching, static/SEO content, layouts

// ✅ Client Component: only when needed
'use client';
// - useState, useEffect, event listeners
// - Browser APIs (localStorage, window)
// - Real-time updates
```

### Data Fetching (Next.js App Router)
```tsx
// ✅ Server Component: fetch directly
async function UserProfile({ userId }: { userId: string }) {
  const user = await db.user.findUnique({ where: { id: userId } });
  if (!user) notFound();
  return <ProfileCard user={user} />;
}

// ✅ Client Component: TanStack Query
const { data, isLoading, error } = useQuery({
  queryKey: ['user', userId],
  queryF
... [TRUNCATED]
```

### File: .claude\agents_DISTILLED.md
```md
---
id: agents
type: distilled_knowledge
---
# agents

## SWALLOW ENGINE DISTILLATION

### File: backend.md
```md
---
name: backend-developer
description: Expert backend developer specializing in Node.js, Express, PostgreSQL, Redis, and API design. Invoke when building API endpoints, services, database schemas, background jobs, or server infrastructure.
---

# Backend Developer Agent

## Role & Responsibility
You are a **Senior Backend Developer**. You design and build robust, scalable, secure server-side systems. You own the API, database, background jobs, and integrations.

## Core Mandate
- Follow ALL rules in `.claude/rules/`: `tech-stack.md`, `api-conventions.md`, `database.md`, `security.md`, `error-handling.md`
- **Security first** — validate/sanitize all inputs, never expose secrets
- **Consistency** — all endpoints follow the same response envelope
- Write production-grade code — handle failures, retries, timeouts

## Tech Stack (Backend)
```
Runtime:       Node.js 20 LTS
Language:      TypeScript 5+
Framework:     Express.js (REST) or Next.js API Routes
Validation:    Zod
ORM:           Prisma
Database:      PostgreSQL 16
Cache:         Redis (ioredis)
Queue:         BullMQ
Auth:          JWT (access 15m + refresh 7d) + bcrypt
Logging:       Pino (structured JSON)
Testing:       Vitest + Supertest
```

## Architecture Pattern — Layered
```
Route → Controller → Service → Repository → Database
                  ↓
              Middleware (auth, validation, rate-limit)
```

### Controller (thin — only req/res)
```ts
// src/controllers/user.controller.ts
import { Request, Response } from 'express';
import { userService } from '@/services/user.service';
import { asyncHandler } from '@/utils/async-handler';

export const getUser = asyncHandler(async (req: Request, res: Response) => {
  const user = await userService.findById(req.params.id);
  res.json({ success: true, data: user });
});
```

### Service (business logic)
```ts
// src/services/user.service.ts
import { userRepository } from '@/repositories/user.repository';
import { AppError } from '@/utils/app-error';

class UserService {
  async findById(id: string) {
    const user = await userRepository.findById(id);
    if (!user) throw new AppError('User not found', 404, 'USER_NOT_FOUND');
    return user;
  }

  async create(data: CreateUserInput) {
    const existing = await userRepository.findByEmail(data.email);
    if (existing) throw new AppError('Email already in use', 409, 'EMAIL_CONFLICT');
    const hashed = await bcrypt.hash(data.password, 12);
    return userRepository.create({ ...data, password: hashed });
  }
}

export const userService = new UserService();
```

### Repository (data access only)
```ts
// src/repositories/user.repository.ts
import { db } from '@/lib/db';

class UserRepository {
  findById(id: string) {
    return db.user.findUnique({ where: { id } });
  }
  findByEmail(email: string) {
    return db.user.findUnique({ where: { email } });
  }
  create(data: Prisma.UserCreateInput) {
    return db.user.create({ data });
  }
}

export const userRepository = new UserRepository();
```

## API Response Envelope
```ts
// ✅ Always wrap responses
res.json({ success: true, data: user });
res.json({ success: true, data: users, pagination: { page, limit, total } });
res.status(400).json({ success: false, error: { code: 'VALIDATION_ERROR', message: '...' } });
```

## Authentication Flow
```ts
// Middleware: authenticate.ts
export async function authenticate(req, res, next) {
  const token = req.headers.authorization?.split(' ')[1];
  if (!token) throw new AppError('Unauthorized', 401);
  try {
    req.user = jwt.verify(token, process.env.JWT_SECRET!) as JwtPayload;
    next();
  } catch {
    throw new AppError('Token invalid or expired', 401);
  }
}
```

## Background Jobs (BullMQ)
```ts
// src/queues/email.queue.ts
import { Queue } from 'bullmq';
import { redis } from '@/lib/redis';

export const emailQueue = new Queue('email', {
  connection: redis,
  defaultJobOptions: {
    attempts: 3,
    backoff: { type: 'exponential', delay: 2000 },
    removeOnComplete: 100,
    removeOnFail: 500,
  },
});
```

## Input Validation (Zod)
```ts
// src/validators/user.validator.ts
import { z } from 'zod';

export const createUserSchema = z.object({
  email: z.string().email().max(255),
  name: z.string().min(2).max(100),
  password: z.string().min(8).max(128),
});

// Middleware
export function validate(schema: z.ZodSchema) {
  return (req, res, next) => {
    const result = schema.safeParse(req.body);
    if (!result.success) {
      throw new AppError('Validation failed', 422, result.error.flatten());
    }
    req.body = result.data;
    next();
  };
}
```

## Checklist Before Every PR
- [ ] Input validated with Zod schema
- [ ] Auth/authorization checked on every protected route
- [ ] No secrets in code, all via `process.env`
- [ ] Database queries use parameterized form (Prisma)
- [ ] Errors handled and mapped to correct HTTP status codes
- [ ] Rate limiting applied to sensitive endpoints
- [ ] Tests written (unit for service, integration for routes)
- [ ] OpenAPI annotations added

```

### File: copywriter-seo.md
```md
---
name: copywriter-seo
description: Expert copywriter and SEO specialist who writes compelling UI copy, content, and optimizes for search engines. Invoke when writing page content, UI microcopy, meta tags, blog posts, email copy, or SEO optimization.
---

# Copywriter & SEO Agent

## Role & Responsibility
You are a **Senior Copywriter & SEO Specialist**. You make the product understood, trusted, and findable. Your words drive conversions, reduce support tickets, and attract organic traffic.

## Core Mandate
- Every word earns its place — cut ruthlessly
- **Clarity > cleverness** — users don't read, they scan
- SEO is structural, not spammy — write for humans, optimize for search
- Consistent voice and tone across all touchpoints

## Brand Voice & Tone

### Voice (always)
- **Clear**: plain language, no jargon unless necessary
- **Helpful**: anticipate user needs
- **Confident**: avoid hedging ("might", "could", "perhaps")
- **Respectful**: never patronizing or condescending

### Tone (varies by context)
| Context | Tone |
|---------|------|
| Marketing pages | Inspiring, energetic |
| Onboarding | Warm, encouraging |
| Error messages | Empathetic, solutions-focused |
| Legal/privacy | Clear, neutral |
| Transactional emails | Informative, concise |

---

## UI Microcopy Rules

### Buttons — Action-first, specific
```markdown
❌ Submit | Okay | Yes | Click here
✅ Create Account | Save Changes | Place Order | Get Started Free

# Pattern: [Verb] + [Object]
Add to Cart ✅
Download Report ✅
Start Free Trial ✅
```

### Form Labels & Placeholders
```markdown
# Labels: noun phrase, no trailing colon
❌ Email Address:
✅ Email address

# Placeholders: example values, not instructions
❌ Enter your email here
✅ you@example.com

# Error messages: specific, tell them how to fix it
❌ Invalid email
✅ Enter a valid email address (e.g., name@company.com)

❌ Password too short
✅ Password must be at least 8 characters
```

### Empty States
```markdown
# Formula: What + Why + What to do
Title: [Friendly description of empty state]
Body: [Brief explanation or encouragement]
CTA: [Action to fill the empty state]

Example:
Title: No orders yet
Body: When you place your first order, it'll appear here.
CTA: Browse Products
```

### Error Pages
```markdown
# 404 Page
Headline: Page not found
Subtext: The page you're looking for doesn't exist or has been moved.
CTA: Go to Homepage

# 500 Page
Headline: Something went wrong
Subtext: We're working on fixing it. Please try again in a moment.
CTA: Try Again | Go to Homepage
```

### Notifications & Toasts
```markdown
# Success: what happened
✅ Order placed! You'll receive a confirmation email shortly.
✅ Password updated successfully.

# Error: what went wrong + what to do
❌ Payment failed. Please check your card details and try again.
❌ Could not save changes. Please refresh the page and try again.

# Warning: what they should know
⚠️ Your session will expire in 5 minutes.
⚠️ This action cannot be undone.
```

---

## SEO Rules

### Page Title Format
```
[Primary Keyword] — [Secondary Context] | [Brand Name]

Examples:
Buy Running Shoes Online — Free Shipping | SportShop
Project Management Software for Teams | Basecamp
Best Vietnamese Restaurants in District 1 | FoodFinder
```

### Meta Description
```markdown
# Rules:
- Length: 150–160 characters (longer gets truncated)
- Include primary keyword naturally
- Include a value proposition or CTA
- Unique per page — never duplicate

# Template:
[Action verb] + [what they get] + [unique benefit]. [Soft CTA].

Example:
"Discover 500+ running shoes from top brands with free same-day shipping.
Shop men's & women's styles — easy returns guaranteed."
```

### Heading Structure (H1-H6)
```markdown
# Rules:
- ONE H1 per page — matches or includes primary keyword
- H2: major sections
- H3: subsections of H2
- Never skip levels (H1 → H3 without H2)
- Headings are for structure AND keywords

# Good structure:
H1: Buy Running Shoes Online
  H2: Men's Running Shoes
    H3: Road Running Shoes
    H3: Trail Running Shoes
  H2: Women's Running Shoes
  H2: How to Choose Running Shoes
```

### URL Structure
```
# Rules: lowercase, hyphens not underscores, descriptive, no stop words
❌ /products?cat=12&id=456
❌ /p/running_shoes_for_men
✅ /shoes/mens-running-shoes
✅ /blog/how-to-choose-running-shoes
```

### Content SEO Checklist
```markdown
- [ ] Primary keyword in H1
- [ ] Primary keyword in first 100 words
- [ ] Secondary keywords in H2/H3
- [ ] Internal links to relevant pages (2-3 minimum)
- [ ] Alt text on all images (descriptive, includes keyword if natural)
- [ ] Page loads in < 3 seconds (Core Web Vitals)
- [ ] Schema markup for relevant content types (Product, Article, FAQ, etc.)
- [ ] Canonical URL set
- [ ] No duplicate content
```

### Schema Markup Templates
```json
// Product page
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "Product Name",
  "description": "...",
  "image": "https://...",
  "offers": {
    "@type": "Offer",
    "price": "99.00",
    "priceCurrency": "USD",
    "availability": "https://schema.org/InStock"
  },
  "aggregateRating": { "@type": "AggregateRating", "ratingValue": "4.5", "reviewCount": "120" }
}

// FAQ section
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [{
    "@type": "Question",
    "name": "How long does shipping take?",
    "acceptedAnswer": { "@type": "Answer", "text": "Standard shipping takes 3-5 business days." }
  }]
}
```

---

## Email Copy Templates

### Welcome Email
```markdown
Subject: Welcome to [Product] — here's how to get started

Hi [First Name],

You're in! Here's the one thing to do first:

[Single CTA Button: "Complete Your Profile" or "Start Your First Project"]

Then, when you're ready:
• [Tip 1 — most common first action]
• [Tip 2 — key feature to discover]
• [Tip 3 — where to get help]

Questions? Reply to this email — we read every one.

[Name]
[Product] Team

P.S. [One helpful tip or interesting fact about the product]
```

### Transactional (Order Confirmation)
```markdown
Subject: Your order #[ORDER-ID] is confirmed ✓

Hi [Name],

Your order is being prepared.

Order Summary:
[Item] × [Qty] — [Price]
Subtotal: [Amount]
Shipping: [Amount]
Total: [Amount]

Delivery to: [Address]
Estimated arrival: [Date range]

Track your order: [Button]

Need help? [Link to support]
```

## Content Quality Checklist
```markdown
Before publishing any content:
- [ ] Read aloud — does it sound natural?
- [ ] Cut 20% of words (if you can, you should)
- [ ] Check Flesch-Kincaid score (aim for Grade 8 or below)
- [ ] Spell check + grammar check (Grammarly)
- [ ] Primary keyword appears naturally (not stuffed)
- [ ] CTA is clear and action-oriented
- [ ] Mobile preview — does it look good on small screen?
- [ ] Links all work
```

```

### File: frontend.md
```md
---
name: frontend-developer
description: Expert frontend developer specializing in Next.js, React, TypeScript, and modern UI development. Invoke when building UI components, pages, routing, state management, or frontend performance tasks.
---

# Frontend Developer Agent

## Role & Responsibility
You are a **Senior Frontend Developer**. Your job is to build beautiful, performant, accessible user interfaces using the approved tech stack. You own everything that runs in the browser.

## Core Mandate
- Follow ALL rules in `.claude/rules/`: `tech-stack.md`, `clean-code.md`, `code-style.md`
- UI must be **accessible** (WCAG 2.1 AA), **responsive** (mobile-first), and **performant**
- Write **TypeScript** always — never use `any` without justification
- Every component must have proper **error boundaries** and **loading states**

## Tech Stack (Frontend)
```
Framework:     Next.js 14+ (App Router)
Language:      TypeScript 5+
Styling:       Tailwind CSS + CSS Variables
Components:    shadcn/ui + Radix UI primitives
State:         Zustand (global) + useState/useReducer (local)
Server State:  TanStack Query (React Query)
Forms:         React Hook Form + Zod validation
Animation:     Framer Motion (sparingly)
Icons:         Lucide React
```

## Component Rules

### Structure
```tsx
// ✅ Component structure template
import type { FC } from 'react';
import { cn } from '@/lib/utils';

interface ButtonProps {
  label: string;
  variant?: 'primary' | 'secondary';
  disabled?: boolean;
  onClick?: () => void;
  className?: string;
}

export const Button: FC<ButtonProps> = ({
  label,
  variant = 'primary',
  disabled = false,
  onClick,
  className,
}) => {
  return (
    <button
      onClick={onClick}
      disabled={disabled}
      aria-label={label}
      className={cn(
        'rounded-md px-4 py-2 font-medium transition-colors',
        variant === 'primary' && 'bg-primary text-primary-foreground hover:bg-primary/90',
        variant === 'secondary' && 'border bg-background hover:bg-muted',
        disabled && 'cursor-not-allowed opacity-50',
        className
      )}
    >
      {label}
    </button>
  );
};
```

### Server vs Client Components
```tsx
// ✅ Default: Server Component (no 'use client')
// - Data fetching, static/SEO content, layouts

// ✅ Client Component: only when needed
'use client';
// - useState, useEffect, event listeners
// - Browser APIs (localStorage, window)
// - Real-time updates
```

### Data Fetching (Next.js App Router)
```tsx
// ✅ Server Component: fetch directly
async function UserProfile({ userId }: { userId: string }) {
  const user = await db.user.findUnique({ where: { id: userId } });
  if (!user) notFound();
  return <ProfileCard user={user} />;
}

// ✅ Client Component: TanStack Query
const { data, isLoading, error } = useQuery({
  queryKey: ['user', userId],
  queryFn: () => fetch(`/api/v1/users/${userId}`).then(r => r.json()),
  staleTime: 60_000,
});
```

### Forms with Validation
```tsx
... [TRUNCATED]
```

### File: .claude\CLAUDE.md
```md
# Claude AI Configuration

## Project Overview
This project uses Claude AI as an intelligent agent to assist with development tasks.

## Core Instructions
- Always follow the rules defined in `.claude/rules/`
- Use available commands from `.claude/commands/` for common tasks
- Leverage skills from `.claude/skills/` for specialized operations
- Coordinate with sub-agents in `.claude/agents/` for complex workflows

## Mandatory Rules
All rules in `.claude/rules/` are **mandatory** and must be followed at all times:

### Code Quality
- `clean-code.md` — Clean Code principles (variables, functions, SOLID, concurrency)
- `code-style.md` — Formatting and naming style guide
- `error-handling.md` — Error classes and global handler patterns

### Architecture & Design
- `tech-stack.md` — Approved technologies (Next.js, PG, Redis, Prisma, BullMQ, docs)
- `system-design.md` — System design patterns (CAP, caching, scaling, queues)
- `project-structure.md` — Folder organization and layered architecture
- `api-conventions.md` — REST API design standards

### Data & Naming
- `naming-conventions.md` — Cache keys, DB identifiers, queues, events, env vars
- `database.md` — Query patterns, transactions, migrations

### Operations
- `security.md` — Security requirements (CRITICAL — never violate)
- `monitoring.md` — Logging, metrics (Prometheus), Grafana dashboards, alerting
- `testing.md` — Test coverage standards and patterns
- `git-workflow.md` — Git branching strategy and commit format

## Available Commands
- `deploy` — Deploy the application
- `fix-issue` — Analyze and fix a reported issue
- `review` — Perform a code review

## Available Agents
Specialized sub-agents in `.claude/agents/`. Invoke the right agent for each task:

| Agent | File | When to Invoke |
|-------|------|---------------|
| 🖥️ Frontend Developer | `agents/frontend.md` | Components, pages, routing, state, performance |
| 🔧 Backend Developer | `agents/backend.md` | APIs, services, DB queries, background jobs |
| 📋 Project Manager | `agents/project-manager.md` | User stories, sprint planning, status reports |
| 🏗️ Systems Architect | `agents/systems-architect.md` | Architecture decisions, ADRs, system design, scalability |
| 🎨 UI/UX Designer | `agents/ui-ux-designer.md` | Design system, wireframes, UX patterns, accessibility |
| ✅ QA Engineer | `agents/qa.md` | Test plans, writing tests, bug reports, coverage |
| ✍️ Copywriter/SEO | `agents/copywriter-seo.md` | Page copy, microcopy, meta tags, SEO optimization |


## Agent Behavior
- Be proactive in identifying potential issues
- Always explain changes before making them
- Prefer incremental changes over large rewrites
- Test assumptions before acting

```

### File: .claude\commands_DISTILLED.md
```md
---
id: commands
type: distilled_knowledge
---
# commands

## SWALLOW ENGINE DISTILLATION

### File: deploy.md
```md
# Deploy Command

## Description
Deploy the application to the target environment.

## Usage
Tell Claude: "Run the deploy command" or "Deploy to [environment]"

## Steps

### 1. Pre-deploy Checklist
- [ ] All tests pass (`npm test`)
- [ ] No linting errors (`npm run lint`)
- [ ] Environment variables are configured
- [ ] Database migrations are ready

### 2. Build
```bash
npm run build
```

### 3. Deploy
```bash
# Development
npm run deploy:dev

# Production
npm run deploy:prod
```

### 4. Post-deploy Verification
- Check application health endpoint
- Verify logs for errors
- Run smoke tests

## Rollback
If deployment fails:
```bash
npm run rollback
```

```

### File: fix-issue.md
```md
# Fix Issue Command

## Description
Analyze and fix a reported bug or issue systematically.

## Usage
Tell Claude: "Fix issue: [describe the issue]" or "Fix bug in [file/module]"

## Process

### 1. Understand the Issue
- Read the error message or bug description carefully
- Identify the affected component(s)
- Reproduce the issue locally if possible

### 2. Root Cause Analysis
- Check recent git changes: `git log --oneline -20`
- Review affected files
- Look for related tests that may reveal expected behavior

### 3. Plan the Fix
- Identify the minimal change needed
- Consider side effects on other components
- Update or add tests to cover the fix

### 4. Implement
- Make the targeted fix
- Ensure code follows `.claude/rules/code-style.md`
- Handle errors per `.claude/rules/error-handling.md`

### 5. Verify
- Run relevant tests: `npm test -- --testPathPattern=[affected]`
- Run full test suite: `npm test`
- Check linting: `npm run lint`

### 6. Commit
Follow `.claude/rules/git-workflow.md`:
```
fix: [short description of the fix]

Closes #[issue-number]
```

```

### File: review.md
```md
# Review Command

## Description
Perform a thorough code review of specified files or a pull request.

## Usage
Tell Claude: "Review [file/PR/feature]" or "Do a code review of [changes]"

## Review Checklist

### Code Quality
- [ ] Code follows style guide (`.claude/rules/code-style.md`)
- [ ] No unnecessary complexity or duplication
- [ ] Functions are small and focused (single responsibility)
- [ ] Variable and function names are descriptive

### Security
- [ ] No hardcoded secrets or credentials
- [ ] Input validation is present
- [ ] Authentication/authorization checks in place
- [ ] See `.claude/rules/security.md` for full checklist

### Error Handling
- [ ] Errors are properly caught and handled
- [ ] Meaningful error messages
- [ ] No swallowed exceptions
- [ ] See `.claude/rules/error-handling.md`

### Testing
- [ ] Unit tests cover new logic
- [ ] Edge cases are tested
- [ ] Tests are readable and maintainable
- [ ] See `.claude/rules/testing.md`

### Database
- [ ] Queries are optimized (no N+1)
- [ ] Transactions used where appropriate
- [ ] See `.claude/rules/database.md`

### API
- [ ] Endpoints follow REST conventions
- [ ] Request/response schemas are documented
- [ ] See `.claude/rules/api-conventions.md`

## Output Format
Provide feedback as:
- 🔴 **Critical** — Must fix before merge
- 🟡 **Warning** — Should fix, potential issue
- 🟢 **Suggestion** — Nice to have improvement
- ✅ **Good** — Highlight what's done well

```


```

### File: .claude\rules_DISTILLED.md
```md
---
id: rules
type: distilled_knowledge
---
# rules

## SWALLOW ENGINE DISTILLATION

### File: api-conventions.md
```md
# API Conventions

## REST API Design Standards

### URL Structure
- Use **kebab-case** for URL paths: `/api/user-profiles`
- Use **plural nouns** for resource collections: `/api/users`, `/api/products`
- Nest related resources: `/api/users/:id/orders`
- API version prefix: `/api/v1/...`

### HTTP Methods
| Method | Usage |
|--------|-------|
| GET | Read resources (idempotent) |
| POST | Create new resource |
| PUT | Replace entire resource |
| PATCH | Partial update |
| DELETE | Remove resource |

### HTTP Status Codes
| Code | Meaning |
|------|---------|
| 200 | OK — Successful GET/PUT/PATCH |
| 201 | Created — Successful POST |
| 204 | No Content — Successful DELETE |
| 400 | Bad Request — Invalid input |
| 401 | Unauthorized — Not authenticated |
| 403 | Forbidden — No permission |
| 404 | Not Found |
| 409 | Conflict |
| 422 | Unprocessable Entity — Validation failed |
| 500 | Internal Server Error |

### Request/Response Format
```json
// Success response
{
  "success": true,
  "data": { ... },
  "message": "Optional message"
}

// Error response
{
  "success": false,
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Human readable message",
    "details": [ ... ]
  }
}

// Paginated list response
{
  "success": true,
  "data": [ ... ],
  "pagination": {
    "page": 1,
    "limit": 20,
    "total": 100,
    "totalPages": 5
  }
}
```

### Naming Conventions
- Request/response body fields: **camelCase**
- Query parameters: **camelCase**
- Always return consistent field names

### Filtering & Pagination
```
GET /api/users?page=1&limit=20&sortBy=createdAt&order=desc
GET /api/products?category=electronics&minPrice=100
```

### Documentation
- Every endpoint MUST have JSDoc/Swagger annotations
- Include request body schema, response schema, and error codes

```

### File: clean-code.md
```md
# Clean Code — JavaScript Rules
> Source: [clean-code-javascript](https://github.com/ryanmcdermott/clean-code-javascript) by Ryan McDermott

## 📦 Variables

### ✅ Use meaningful, pronounceable names
```js
// ❌ Bad
const yyyymmdstr = moment().format('YYYY/MM/DD');

// ✅ Good
const currentDate = moment().format('YYYY/MM/DD');
```

### ✅ Same vocabulary for same type
```js
// ❌ getUserInfo(), getClientData(), getCustomerRecord()
// ✅ getUser()
```

### ✅ Use searchable names (no magic numbers)
```js
// ❌ setTimeout(blastOff, 86400000);
const MILLISECONDS_PER_DAY = 60 * 60 * 24 * 1000;
setTimeout(blastOff, MILLISECONDS_PER_DAY); // ✅
```

### ✅ Use explanatory variables
```js
// ❌ Bad
saveCityZipCode(address.match(regex)[1], address.match(regex)[2]);

// ✅ Good
const [_, city, zipCode] = address.match(cityZipCodeRegex) || [];
saveCityZipCode(city, zipCode);
```

### ✅ Avoid mental mapping — be explicit
```js
// ❌ locations.forEach(l => { dispatch(l); });
// ✅ locations.forEach(location => { dispatch(location); });
```

### ✅ Don't add redundant context
```js
// ❌ const Car = { carMake, carModel, carColor }
// ✅ const Car = { make, model, color }
```

### ✅ Use default parameters
```js
// ❌ const name = name || 'Default';
// ✅ function create(name = 'Default') {}
```

---

## 🔧 Functions

### ✅ 2 arguments or fewer — use object destructuring for more
```js
// ❌ function createMenu(title, body, buttonText, cancellable) {}
// ✅ function createMenu({ title, body, buttonText, cancellable }) {}
```

### ✅ Functions should do ONE thing
```js
// ❌ emailClients() — fetches DB + checks active + sends email
// ✅ emailActiveClients() calls isActiveClient() separately
```

### ✅ Function names should say what they do
```js
// ❌ addToDate(date, 1)     → unclear what is added
// ✅ addMonthToDate(1, date) → crystal clear
```

### ✅ One level of abstraction per function
```js
// ❌ parseBetterJSAlternative() — tokenizes + parses + AST walks in one function
// ✅ parseBetterJSAlternative() → calls tokenize() → calls parse()
```

### ✅ Remove duplicate code — extract shared logic
### ✅ No flag parameters — split into separate functions
```js
// ❌ function createFile(name, isTemp) { if (isTemp) ... }
// ✅ function createFile(name) {}
//    function createTempFile(name) {}
```

### ✅ Avoid Side Effects
- Don't mutate global state
- Don't mutate function arguments (use copies)
```js
// ✅ Return new array instead of mutating
function addItemToCart(cart, item) {
  return [...cart, { item, date: Date.now() }];
}
```

### ✅ Favor functional programming
```js
// ❌ for loop with mutations
// ✅ filter(), map(), reduce()
const totalOutput = programmerOutput
  .filter(p => p.linesOfCode > 0)
  .reduce((acc, p) => acc + p.linesOfCode, 0);
```

### ✅ Encapsulate conditionals
```js
// ❌ if (fsm.state === 'fetching' && isEmpty(listNode)) {}
// ✅ if (shouldShowSpinner(fsmInstance, listNodeInstance)) {}
```

### ✅ Avoid negative conditionals
```js
// ❌ if (!isNotDOMNodePresent(node)) {}
// ✅ if (isDOMNodePresent(node)) {}
```

### ✅ Remove dead code immediately

---

## 🏛️ Classes

### ✅ Prefer ES6 classes
### ✅ Use method chaining (builder pattern)
```js
class QueryBuilder {
  select(fields) { this.fields = fields; return this; }
  from(table) { this.table = table; return this; }
  build() { return `SELECT ${this.fields} FROM ${this.table}`; }
}
new QueryBuilder().select('*').from('users').build();
```

### ✅ Prefer composition over inheritance
> "Favor has-a over is-a"

---

## 🧱 SOLID Principles

| Principle | Rule |
|-----------|------|
| **S** — Single Responsibility | One class = one job. Never combine unrelated concerns |
| **O** — Open/Closed | Open for extension, closed for modification |
| **L** — Liskov Substitution | Subclasses must be substitutable for their base class |
| **I** — Interface Segregation | Clients shouldn't depend on interfaces they don't use |
| **D** — Dependency Inversion | Depend on abstractions, not concretions |

```js
// ✅ D — Dependency Inversion
class InventoryService {
  constructor(inventoryRequester) { // inject the dependency
    this.inventoryRequester = inventoryRequester;
  }
  requestItems(customer) {
    return this.inventoryRequester.requestItem(customer.purchaseHistory);
  }
}
```

---

## ⚡ Concurrency

### ✅ Use Promises over callbacks
### ✅ Use async/await over Promises
```js
// ✅ Clearest form
async function getCleanCodeArticle() {
  try {
    const response = await request.get(cleanCodeUrl);
    await fs.writeFile('article.html', response);
  } catch (err) {
    console.error(err);
  }
}
```

---

## 🗒️ Comments

### ✅ Only comment business logic complexity
### ❌ Never leave commented-out code
### ❌ No journal comments (use git log instead)
### ❌ No positional markers (`/////`)
```js
// ✅ Good comment — explains WHY
// We retry 3x because OAuth2 tokens can have clock skew
const MAX_RETRIES = 3;
```

---

## 📐 Formatting

- Use consistent capitalization (camelCase for vars/fns, PascalCase for classes, UPPER_SNAKE for constants)
- Keep callers and callees close in the file
- Related code should appear together

```

### File: code-style.md
```md
# Code Style Guide

## General Principles
- **Clarity over cleverness** — Write code that is easy to read and understand
- **Consistency** — Follow existing patterns in the codebase
- **DRY** — Don't Repeat Yourself, but don't over-abstract

## JavaScript / TypeScript

### Formatting
- Indentation: **2 spaces** (no tabs)
- Max line length: **100 characters**
- Use **single quotes** for strings
- Always use **semicolons**
- Trailing commas in multi-line structures

### Naming
```js
// Variables and functions: camelCase
const userProfile = {};
function getUserById(id) {}

// Classes and interfaces: PascalCase
class UserService {}
interface UserRepository {}

// Constants: UPPER_SNAKE_CASE
const MAX_RETRY_COUNT = 3;
const API_BASE_URL = 'https://api.example.com';

// Files: kebab-case
// user-service.js, auth-middleware.js
```

### Functions
```js
// ✅ Good — Arrow functions for simple operations
const double = (x) => x * 2;

// ✅ Good — Named functions for complex logic
function processUserData(user) {
  // ...
}

// ❌ Avoid — Functions longer than 30 lines (extract helpers)
```

### Async/Await
```js
// ✅ Always use async/await over raw promises
async function fetchUser(id) {
  try {
    const user = await userRepository.findById(id);
    return user;
  } catch (error) {
    throw new AppError('User not found', 404);
  }
}

// ❌ Avoid promise chains
fetchUser(id).then(...).catch(...);
```

### Imports
```js
// Order: 1. Node built-ins, 2. External deps, 3. Internal modules
import path from 'path';
import express from 'express';
import { UserService } from './user-service.js';
```

## Comments
```js
// ✅ Explain WHY, not WHAT
// We retry 3 times because the external API has transient failures
const MAX_RETRIES = 3;

// ❌ Avoid obvious comments
// Set x to 5
const x = 5;
```

## File Organization
- One class/service per file
- Group related files in feature folders
- Index files for clean imports

```

### File: database.md
```md
doc# Database Rules

## General Rules
- **Never** write raw SQL strings directly in business logic
- Always use an ORM (Prisma/Sequelize/TypeORM) or query builder
- All database calls must be inside try/catch blocks
- Use **transactions** for multi-step operations

## Connection Management
```js
// ✅ Use connection pooling
const pool = new Pool({ max: 10, idleTimeoutMillis: 30000 });

// ❌ Never create a new connection per request
```

## Query Best Practices
```js
// ✅ Select only needed fields
const user = await db.user.findUnique({
  where: { id },
  select: { id: true, email: true, name: true }
});

// ❌ Avoid SELECT *
const user = await db.user.findUnique({ where: { id } });

// ✅ Use pagination for lists
const users = await db.user.findMany({
  take: limit,
  skip: (page - 1) * limit,
  orderBy: { createdAt: 'desc' }
});
```

## Transactions
```js
// ✅ Use transactions for atomic operations
await db.$transaction(async (tx) => {
  const order = await tx.order.create({ data: orderData });
  await tx.inventory.update({ where: { id: productId }, data: { stock: { decrement: 1 } } });
  return order;
});
```

## Migrations
- Always use migration files, never modify the database schema directly
- Migration files are version-controlled and immutable
- Run migrations in CI/CD before deploying

## Naming Conventions
- Tables: **snake_case** plural (`user_profiles`, `order_items`)
- Columns: **snake_case** (`created_at`, `user_id`)
- Indexes: `idx_[table]_[column]`
- Foreign keys: `fk_[table]_[referenced_table]`

## Security
- Never log query results containing sensitive data (passwords, tokens)
- Use parameterized queries — never string concatenation
- Apply row-level security where applicable

```

### File: error-handling.md
```md
# Error Handling

## Core Principles
- **Never swallow errors silently** — always log or rethrow
- Use a centralized error handler
- Return consistent error responses to the API
- Distinguish between operational errors (expected) and programmer errors (bugs)

## Custom Error Class
```js
// src/utils/app-error.js
class AppError extends Error {
  constructor(message, statusCode = 500, code = 'INTERNAL_ERROR') {
    super(message);
    this.name = 'AppError';
    this.statusCode = statusCode;
    this.code = code;
    this.isOperational = true;
    Error.captureStackTrace(this, this.constructor);
  }
}

export default AppError;
```

## Throwing Errors
```js
// ✅ Use AppError for known operational errors
if (!user) {
  throw new AppError('User not found', 404, 'USER_NOT_FOUND');
}

if (!hasPermission) {
  throw new AppError('Forbidden', 403, 'ACCESS_DENIED');
}
```

## Async Error Handling
```js
// ✅ Always wrap async route handlers
const asyncHandler = (fn) => (req, res, next) =>
  Promise.resolve(fn(req, res, next)).catch(next);

router.get('/users/:id', asyncHandler(async (req, res) => {
  const user = await userService.findById(req.params.id);
  res.json({ success: true, data: user });
}));
```

## Global Error Handler (Express)
```js
// middleware/error-handler.js
export function errorHandler(err, req, res, next) {
  const statusCode = err.statusCode || 500;
  const isOperational = err.isOperational || false;

  // Log all errors
  logger.error({ err, req: { method: req.method, url: req.url } });

  // Don't expose internal errors to clients
  if (!isOperational) {
    return res.status(500).json({
      success: false,
      error: { code: 'INTERNAL_ERROR', message: 'An unexpected error occurred' }
    });
  }

  res.status(statusCode).json({
    success: false,
    error: { code: err.code, message: err.message }
  });
}
```

## Validation Errors
```js
// Use a validation library (Zod/Joi/Yup) and throw structured errors
import { z } from 'zod';

const userSchema = z.object({
  email: z.string().email(),
  name: z.string().min(2)
});

function validateUser(data) {
  const result = userSchema.safeParse(data);
  if (!result.success) {
    throw new AppError('Validation failed', 422, 'VALIDATION_ERROR');
  }
  return result.data;
}
```

```

### File: git-workflow.md
```md
# Git Workflow

## Branch Strategy (Git Flow)

```
main          — Production-ready code only
develop       — Integration branch for features
feature/*     — New features
fix/*         — Bug fixes
hotfix/*      — Urgent production fixes
release/*     — Release preparation
```

## Branch Naming
```
feature/user-authentication
feature/payment-integration
fix/login-redirect-bug
fix/order-calculation-issue
hotfix/critical-security-patch
release/v1.2.0
```

## Commit Message Format (Conventional Commits)

```
<type>(<scope>): <short description>

[optional body]

[optional footer]
```

### Types
| Type | Usage |
|------|-------|
| `feat` | New feature |
| `fix` | Bug fix |
| `docs` | Documentation only |
| `style` | Formatting, no logic change |
| `refactor` | Code restructure, no feature/fix |
| `test` | Adding or fixing tests |
| `chore` | Build process, dependencies |
| `perf` | Performance improvement |

### Examples
```
feat(auth): add JWT refresh token support

fix(orders): correct total price calculation when discount applied

docs(api): add Swagger annotations to user endpoints

test(users): add unit tests for UserService.findById

chore: upgrade express to v5.0.0
```

## Pull Request Rules
- PRs must reference an issue: `Closes #123`
- Minimum 1 reviewer approval required
- All CI checks must pass
- No direct commits to `main` or `develop`
- PR title must follow conventional commit format

## Commit Best Practices
- Commit frequently with small, focused changes
- Each commit should be a single logical change
- Never commit: `.env` files, secrets, `node_modules`
- Always run tests before committing

## Tags & Releases
```bash
# Tag a release
git tag -a v1.2.0 -m "Release version 1.2.0"
git push origin v1.2.0
```

```

### File: monitoring.md
```md
# Monitoring & Observability

> Standards for logging, metrics, tracing, alertin
... [TRUNCATED]
```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.

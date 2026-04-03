---
id: github.com-analogjs-angular-skills-edc5c445-knowle
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:30.171747
---

# KNOWLEDGE EXTRACT: github.com_analogjs_angular-skills_edc5c445
> **Extracted on:** 2026-04-01 14:28:13
> **Source:** D:/LongLeo/AI OS CORP/AI OS/core/security/QUARANTINE/KI-BATCH-20260331205007523903/github.com_analogjs_angular-skills_edc5c445

---

## File: `LICENSE`
```
MIT License

Copyright (c) 2026 Brandon Roberts

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## File: `README.md`
```markdown
## **The Angular team has released an official skills package at [angular/skills](https://github.com/angular/skills). This repository is no longer actively maintained.**

## Skills Removal

If you have previously installed these skills, you can remove them before installing the official skills with the following command:

```sh
npx skills remove analogjs/angular-skills
```

## Resources

- [Angular Documentation](https://angular.dev)
- [Angular AI Documentation](https://angular.dev/ai)
- [Skills.sh](https://skills.sh)

## License

MIT
```

## File: `skills/angular-component/SKILL.md`
```markdown
---
name: angular-component
description: Create modern Angular standalone components following v20+ best practices. Use for building UI components with signal-based inputs/outputs, OnPush change detection, host bindings, content projection, and lifecycle hooks. Triggers on component creation, refactoring class-based inputs to signals, adding host bindings, or implementing accessible interactive components.
---

# Angular Component

Create standalone components for Angular v20+. Components are standalone by default—do NOT set `standalone: true`.

## Component Structure

```typescript
import { Component, ChangeDetectionStrategy, input, output, computed } from '@angular/core';

@Component({
  selector: 'app-user-card',
  changeDetection: ChangeDetectionStrategy.OnPush,
  host: {
    'class': 'user-card',
    '[class.active]': 'isActive()',
    '(click)': 'handleClick()',
  },
  template: `
    <img [src]="avatarUrl()" [alt]="name() + ' avatar'" />
    <h2>{{ name() }}</h2>
    @if (showEmail()) {
      <p>{{ email() }}</p>
    }
  `,
  styles: `
    :host { display: block; }
    :host.active { border: 2px solid blue; }
  `,
})
export class UserCard {
  // Required input
  name = input.required<string>();
  
  // Optional input with default
  email = input<string>('');
  showEmail = input(false);
  
  // Input with transform
  isActive = input(false, { transform: booleanAttribute });
  
  // Computed from inputs
  avatarUrl = computed(() => `https://api.example.com/avatar/${this.name()}`);
  
  // Output
  selected = output<string>();
  
  handleClick() {
    this.selected.emit(this.name());
  }
}
```

## Signal Inputs

```typescript
// Required - must be provided by parent
name = input.required<string>();

// Optional with default value
count = input(0);

// Optional without default (undefined allowed)
label = input<string>();

// With alias for template binding
size = input('medium', { alias: 'buttonSize' });

// With transform function
disabled = input(false, { transform: booleanAttribute });
value = input(0, { transform: numberAttribute });
```

## Signal Outputs

```typescript
import { output, outputFromObservable } from '@angular/core';

// Basic output
clicked = output<void>();
selected = output<Item>();

// With alias
valueChange = output<number>({ alias: 'change' });

// From Observable (for RxJS interop)
scroll$ = new Subject<number>();
scrolled = outputFromObservable(this.scroll$);

// Emit values
this.clicked.emit();
this.selected.emit(item);
```

## Host Bindings

Use the `host` object in `@Component`—do NOT use `@HostBinding` or `@HostListener` decorators.

```typescript
@Component({
  selector: 'app-button',
  host: {
    // Static attributes
    'role': 'button',
    
    // Dynamic class bindings
    '[class.primary]': 'variant() === "primary"',
    '[class.disabled]': 'disabled()',
    
    // Dynamic style bindings
    '[style.--btn-color]': 'color()',
    
    // Attribute bindings
    '[attr.aria-disabled]': 'disabled()',
    '[attr.tabindex]': 'disabled() ? -1 : 0',
    
    // Event listeners
    '(click)': 'onClick($event)',
    '(keydown.enter)': 'onClick($event)',
    '(keydown.space)': 'onClick($event)',
  },
  template: `<ng-content />`,
})
export class Button {
  variant = input<'primary' | 'secondary'>('primary');
  disabled = input(false, { transform: booleanAttribute });
  color = input('#007bff');
  
  clicked = output<void>();
  
  onClick(event: Event) {
    if (!this.disabled()) {
      this.clicked.emit();
    }
  }
}
```

## Content Projection

```typescript
@Component({
  selector: 'app-card',
  template: `
    <header>
      <ng-content select="[card-header]" />
    </header>
    <main>
      <ng-content />
    </main>
    <footer>
      <ng-content select="[card-footer]" />
    </footer>
  `,
})
export class Card {}

// Usage:
// <app-card>
//   <h2 card-header>Title</h2>
//   <p>Main content</p>
//   <button card-footer>Action</button>
// </app-card>
```

## Lifecycle Hooks

```typescript
import { OnDestroy, OnInit, afterNextRender, afterRender } from '@angular/core';

export class My implements OnInit, OnDestroy {
  constructor() {
    // For DOM manipulation after render (SSR-safe)
    afterNextRender(() => {
      // Runs once after first render
    });

    afterRender(() => {
      // Runs after every render
    });
  }

  ngOnInit() { /* Component initialized */ }
  ngOnDestroy() { /* Cleanup */ }
}
```

## Accessibility Requirements

Components MUST:
- Pass AXE accessibility checks
- Meet WCAG AA standards
- Include proper ARIA attributes for interactive elements
- Support keyboard navigation
- Maintain visible focus indicators

```typescript
@Component({
  selector: 'app-toggle',
  host: {
    'role': 'switch',
    '[attr.aria-checked]': 'checked()',
    '[attr.aria-label]': 'label()',
    'tabindex': '0',
    '(click)': 'toggle()',
    '(keydown.enter)': 'toggle()',
    '(keydown.space)': 'toggle(); $event.preventDefault()',
  },
  template: `<span class="toggle-track"><span class="toggle-thumb"></span></span>`,
})
export class Toggle {
  label = input.required<string>();
  checked = input(false, { transform: booleanAttribute });
  checkedChange = output<boolean>();
  
  toggle() {
    this.checkedChange.emit(!this.checked());
  }
}
```

## Template Syntax

Use native control flow—do NOT use `*ngIf`, `*ngFor`, `*ngSwitch`.

```html
<!-- Conditionals -->
@if (isLoading()) {
  <app-spinner />
} @else if (error()) {
  <app-error [message]="error()" />
} @else {
  <app-content [data]="data()" />
}

<!-- Loops -->
@for (item of items(); track item.id) {
  <app-item [item]="item" />
} @empty {
  <p>No items found</p>
}

<!-- Switch -->
@switch (status()) {
  @case ('pending') { <span>Pending</span> }
  @case ('active') { <span>Active</span> }
  @default { <span>Unknown</span> }
}
```

## Class and Style Bindings

Do NOT use `ngClass` or `ngStyle`. Use direct bindings:

```html
<!-- Class bindings -->
<div [class.active]="isActive()">Single class</div>
<div [class]="classString()">Class string</div>

<!-- Style bindings -->
<div [style.color]="textColor()">Styled text</div>
<div [style.width.px]="width()">With unit</div>
```

## Images

Use `NgOptimizedImage` for static images:

```typescript
import { NgOptimizedImage } from '@angular/common';

@Component({
  imports: [NgOptimizedImage],
  template: `
    <img ngSrc="/assets/hero.jpg" width="800" height="600" priority />
    <img [ngSrc]="imageUrl()" width="200" height="200" />
  `,
})
export class Hero {
  imageUrl = input.required<string>();
}
```

For detailed patterns, see [references/component-patterns.md](../../../vault/archives/archive_legacy/agents/plugins/ui-design/skills/web-component-design/references/component-patterns.md).
```

## File: `skills/angular-component/references/component-patterns.md`
```markdown
# Angular Component Patterns

## Table of Contents
- [Model Inputs (Two-Way Binding)](#model-inputs-two-way-binding)
- [View Queries](#view-queries)
- [Content Queries](#content-queries)
- [Dependency Injection in Components](#dependency-injection-in-components)
- [Component Communication Patterns](#component-communication-patterns)
- [Dynamic Components](#dynamic-components)

## Model Inputs (Two-Way Binding)

For two-way binding with `[(value)]` syntax:

```typescript
import { Component, model } from '@angular/core';

@Component({
  selector: 'app-slider',
  host: {
    '(input)': 'onInput($event)',
  },
  template: `
    <input 
      type="range" 
      [value]="value()" 
      [min]="min()" 
      [max]="max()" 
    />
    <span>{{ value() }}</span>
  `,
})
export class Slider {
  // Model creates both input and output
  value = model(0);
  min = input(0);
  max = input(100);
  
  onInput(event: Event) {
    const target = event.target as HTMLInputElement;
    this.value.set(Number(target.value));
  }
}

// Usage: <app-slider [(value)]="sliderValue" />
```

Required model:

```typescript
value = model.required<number>();
```

## View Queries

Query elements and components in the template:

```typescript
import { Component, viewChild, viewChildren, ElementRef } from '@angular/core';

@Component({
  selector: 'app-gallery',
  template: `
    <div #container class="gallery">
      @for (image of images(); track image.id) {
        <app-image-card [image]="image" />
      }
    </div>
  `,
})
export class Gallery {
  images = input.required<Image[]>();

  // Query single element
  container = viewChild.required<ElementRef<HTMLDivElement>>('container');

  // Query single component (optional)
  firstCard = viewChild(ImageCard);

  // Query all matching components
  allCards = viewChildren(ImageCard);
}
```

## Content Queries

Query projected content:

```typescript
import { Component, contentChild, contentChildren, effect, signal } from '@angular/core';

@Component({
  selector: 'app-tabs',
  template: `
    <div class="tab-headers">
      @for (tab of tabs(); track tab.label()) {
        <button
          [class.active]="tab === activeTab()"
          (click)="selectTab(tab)"
        >
          {{ tab.label() }}
        </button>
      }
    </div>
    <div class="tab-content">
      <ng-content />
    </div>
  `,
})
export class Tabs {
  // Query all projected Tab children
  tabs = contentChildren(Tab);

  // Query single projected element
  header = contentChild('tabHeader');

  activeTab = signal<Tab | undefined>(undefined);

  constructor() {
    // Set first tab as active when tabs are available
    effect(() => {
      const firstTab = this.tabs()[0];
      if (firstTab && !this.activeTab()) {
        this.activeTab.set(firstTab);
      }
    });
  }

  selectTab(tab: Tab) {
    this.activeTab.set(tab);
  }
}

@Component({
  selector: 'app-tab',
  template: `<ng-content />`,
  host: {
    '[class.active]': 'isActive()',
    '[style.display]': 'isActive() ? "block" : "none"',
  },
})
export class Tab {
  label = input.required<string>();
  isActive = input(false);
}
```

## Dependency Injection in Components

Use `inject()` function instead of constructor injection:

```typescript
import { Component, inject } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-dashboard',
  template: `...`,
})
export class Dashboard {
  private router = inject(Router);
  private userService = inject(User);
  private config = inject(APP_CONFIG);
  
  // Optional injection
  private analytics = inject(Analytics, { optional: true });
  
  // Self-only injection
  private localService = inject(Local, { self: true });
  
  navigateToProfile() {
    this.router.navigate(['/profile']);
  }
}
```

## Component Communication Patterns

### Parent to Child (Inputs)

```typescript
// Parent
@Component({
  template: `<app-child [data]="parentData()" [config]="config" />`,
})
export class Parent {
  parentData = signal({ name: 'Test' });
  config = { theme: 'dark' };
}

// Child
@Component({ selector: 'app-child' })
export class Child {
  data = input.required<Data>();
  config = input<Config>();
}
```

### Child to Parent (Outputs)

```typescript
// Child
@Component({
  selector: 'app-child',
  template: `<button (click)="save()">Save</button>`,
})
export class Child {
  saved = output<Data>();
  
  save() {
    this.saved.emit({ id: 1, name: 'Item' });
  }
}

// Parent
@Component({
  template: `<app-child (saved)="onSaved($event)" />`,
})
export class Parent {
  onSaved(data: Data) {
    console.log('Saved:', data);
  }
}
```

### Shared Service Pattern

```typescript
// Shared state service
@Injectable({ providedIn: 'root' })
export class Cart {
  private items = signal<CartItem[]>([]);
  
  readonly items$ = this.items.asReadonly();
  readonly total = computed(() => 
    this.items().reduce((sum, item) => sum + item.price, 0)
  );
  
  addItem(item: CartItem) {
    this.items.update(items => [...items, item]);
  }
  
  removeItem(id: string) {
    this.items.update(items => items.filter(i => i.id !== id));
  }
}

// Component A
@Component({ template: `<button (click)="add()">Add</button>` })
export class Product {
  private cart = inject(Cart);
  product = input.required<Product>();
  
  add() {
    this.cart.addItem({ ...this.product(), quantity: 1 });
  }
}

// Component B
@Component({ template: `<span>Total: {{ cart.total() }}</span>` })
export class CartSummary {
  cart = inject(Cart);
}
```

## Dynamic Components

Using `@defer` for lazy loading:

```typescript
@Component({
  template: `
    @defer (on viewport) {
      <app-heavy-chart [data]="chartData()" />
    } @placeholder {
      <div class="chart-placeholder">Loading chart...</div>
    } @loading (minimum 500ms) {
      <app-spinner />
    } @error {
      <p>Failed to load chart</p>
    }
  `,
})
export class Dashboard {
  chartData = input.required<ChartData>();
}
```

Defer triggers:
- `on viewport` - When element enters viewport
- `on idle` - When browser is idle
- `on interaction` - On user interaction (click, focus)
- `on hover` - On mouse hover
- `on immediate` - Immediately after non-deferred content
- `on timer(500ms)` - After specified delay
- `when condition` - When expression becomes true

```typescript
@Component({
  template: `
    @defer (on interaction; prefetch on idle) {
      <app-comments [postId]="postId()" />
    } @placeholder {
      <button>Load Comments</button>
    }
  `,
})
export class Post {
  postId = input.required<string>();
}
```

## Attribute Directives on Components

```typescript
@Directive({
  selector: '[appHighlight]',
  host: {
    '[style.backgroundColor]': 'color()',
  },
})
export class Highlight {
  color = input('yellow', { alias: 'appHighlight' });
}

// Usage on component
@Component({
  imports: [Highlight],
  template: `<app-card appHighlight="lightblue" />`,
})
export class Page {}
```

## Error Boundaries

```typescript
@Component({
  selector: 'app-error-boundary',
  template: `
    @if (hasError()) {
      <div class="error">
        <h3>Something went wrong</h3>
        <button (click)="retry()">Retry</button>
      </div>
    } @else {
      <ng-content />
    }
  `,
})
export class ErrorBoundary {
  hasError = signal(false);
  private errorHandler = inject(ErrorHandler);
  
  retry() {
    this.hasError.set(false);
  }
}
```
```

## File: `skills/angular-di/SKILL.md`
```markdown
---
name: angular-di
description: Implement dependency injection in Angular v20+ using inject(), injection tokens, and provider configuration. Use for service architecture, providing dependencies at different levels, creating injectable tokens, and managing singleton vs scoped services. Triggers on service creation, configuring providers, using injection tokens, or understanding DI hierarchy.
---

# Angular Dependency Injection

Configure and use dependency injection in Angular v20+ with `inject()` and providers.

## Basic Injection

### Using inject()

Prefer `inject()` over constructor injection:

```typescript
import { Component, inject } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { User } from './user.service';

@Component({
  selector: 'app-user-list',
  template: `...`,
})
export class UserList {
  // Inject dependencies
  private http = inject(HttpClient);
  private userService = inject(User);
  
  // Can use immediately
  users = this.userService.getUsers();
}
```

### Injectable Services

```typescript
import { Injectable, inject, signal } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root', // Singleton at root level
})
export class User {
  private http = inject(HttpClient);
  
  private users = signal<User[]>([]);
  readonly users$ = this.users.asReadonly();
  
  async loadUsers() {
    const users = await firstValueFrom(
      this.http.get<User[]>('/api/users')
    );
    this.users.set(users);
  }
}
```

## Provider Scopes

### Root Level (Singleton)

```typescript
// Recommended: providedIn
@Injectable({
  providedIn: 'root',
})
export class Auth {}

// Alternative: in app.config.ts
export const appConfig: ApplicationConfig = {
  providers: [
    Auth,
  ],
};
```

### Component Level (Instance per Component)

```typescript
@Component({
  selector: 'app-editor',
  providers: [EditorState], // New instance for each component
  template: `...`,
})
export class Editor {
  private editorState = inject(EditorState);
}
```

### Route Level

```typescript
export const routes: Routes = [
  {
    path: 'admin',
    providers: [Admin], // Shared within this route tree
    children: [
      { path: '', component: AdminDashboard },
      { path: 'users', component: AdminUsers },
    ],
  },
];
```

## Injection Tokens

### Creating Tokens

```typescript
import { InjectionToken } from '@angular/core';

// Simple value token
export const API_URL = new InjectionToken<string>('API_URL');

// Object token
export interface AppConfig {
  apiUrl: string;
  features: {
    darkMode: boolean;
    analytics: boolean;
  };
}

export const APP_CONFIG = new InjectionToken<AppConfig>('APP_CONFIG');

// Token with factory (self-providing)
export const WINDOW = new InjectionToken<Window>('Window', {
  providedIn: 'root',
  factory: () => window,
});

export const LOCAL_STORAGE = new InjectionToken<Storage>('LocalStorage', {
  providedIn: 'root',
  factory: () => localStorage,
});
```

### Providing Token Values

```typescript
// app.config.ts
export const appConfig: ApplicationConfig = {
  providers: [
    { provide: API_URL, useValue: 'https://api.example.com' },
    {
      provide: APP_CONFIG,
      useValue: {
        apiUrl: 'https://api.example.com',
        features: { darkMode: true, analytics: true },
      },
    },
  ],
};
```

### Injecting Tokens

```typescript
@Injectable({ providedIn: 'root' })
export class Api {
  private apiUrl = inject(API_URL);
  private config = inject(APP_CONFIG);
  private window = inject(WINDOW);
  
  getBaseUrl(): string {
    return this.apiUrl;
  }
}
```

## Provider Types

### useClass

```typescript
// Provide implementation
{ provide: Logger, useClass: ConsoleLogger }

// Conditional implementation
{
  provide: Logger,
  useClass: environment.production
    ? ProductionLogger
    : ConsoleLogger,
}
```

### useValue

```typescript
// Static values
{ provide: API_URL, useValue: 'https://api.example.com' }

// Configuration objects
{ provide: APP_CONFIG, useValue: { theme: 'dark', language: 'en' } }
```

### useFactory

```typescript
// Factory with dependencies
{
  provide: User,
  useFactory: (http: HttpClient, config: AppConfig) => {
    return new User(http, config.apiUrl);
  },
  deps: [HttpClient, APP_CONFIG],
}

// Async factory (not recommended - use provideAppInitializer)
{
  provide: CONFIG,
  useFactory: () => fetch('/config.json').then(r => r.json()),
}
```

### useExisting

```typescript
// Alias to existing provider
{ provide: AbstractLogger, useExisting: ConsoleLogger }

// Multiple tokens pointing to same instance
providers: [
  ConsoleLogger,
  { provide: Logger, useExisting: ConsoleLogger },
  { provide: ErrorLogger, useExisting: ConsoleLogger },
]
```

## Injection Options

### Optional Injection

```typescript
@Component({...})
export class My {
  // Returns null if not provided
  private analytics = inject(Analytics, { optional: true });
  
  trackEvent(name: string) {
    this.analytics?.track(name);
  }
}
```

### Self, SkipSelf, Host

```typescript
@Component({
  providers: [Local],
})
export class Parent {
  // Only look in this component's injector
  private local = inject(Local, { self: true });
}

@Component({...})
export class Child {
  // Skip this component, look in parent
  private parentService = inject(ParentSvc, { skipSelf: true });

  // Only look up to host component
  private hostService = inject(Host, { host: true });
}
```

## Multi Providers

Collect multiple values for same token:

```typescript
// Token for multiple validators
export const VALIDATORS = new InjectionToken<Validator[]>('Validators');

// Provide multiple values
providers: [
  { provide: VALIDATORS, useClass: RequiredValidator, multi: true },
  { provide: VALIDATORS, useClass: EmailValidator, multi: true },
  { provide: VALIDATORS, useClass: MinLengthValidator, multi: true },
]

// Inject as array
@Injectable()
export class Validation {
  private validators = inject(VALIDATORS); // Validator[]
  
  validate(value: string): ValidationError[] {
    return this.validators
      .map(v => v.validate(value))
      .filter(Boolean);
  }
}
```

### HTTP Interceptors (Multi Provider)

```typescript
// Interceptors use multi providers internally
export const appConfig: ApplicationConfig = {
  providers: [
    provideHttpClient(
      withInterceptors([
        authInterceptor,
        loggingInterceptor,
        errorInterceptor,
      ])
    ),
  ],
};
```

## App Initializers

Run async code before app starts using `provideAppInitializer`:

```typescript
import { provideAppInitializer, inject } from '@angular/core';

export const appConfig: ApplicationConfig = {
  providers: [
    Config,
    provideAppInitializer(() => {
      const configService = inject(Config);
      return configService.loadConfig();
    }),
  ],
};
```

### Multiple Initializers

```typescript
providers: [
  provideAppInitializer(() => {
    const config = inject(Config);
    return config.load();
  }),
  provideAppInitializer(() => {
    const auth = inject(Auth);
    return auth.checkSession();
  }),
]
```

## Environment Injector

Create injectors programmatically:

```typescript
import { createEnvironmentInjector, EnvironmentInjector, inject } from '@angular/core';

@Injectable({ providedIn: 'root' })
export class Plugin {
  private parentInjector = inject(EnvironmentInjector);
  
  loadPlugin(providers: Provider[]): EnvironmentInjector {
    return createEnvironmentInjector(providers, this.parentInjector);
  }
}
```

## runInInjectionContext

Run code with injection context:

```typescript
import { runInInjectionContext, EnvironmentInjector, inject } from '@angular/core';

@Injectable({ providedIn: 'root' })
export class Utility {
  private injector = inject(EnvironmentInjector);
  
  executeWithDI<T>(fn: () => T): T {
    return runInInjectionContext(this.injector, fn);
  }
}

// Usage
utilityService.executeWithDI(() => {
  const http = inject(HttpClient);
  // Use http...
});
```

For advanced patterns, see [references/di-patterns.md](di-patterns.md).
```

## File: `skills/angular-di/references/di-patterns.md`
```markdown
# Angular Dependency Injection Patterns

## Table of Contents
- [Service Patterns](#service-patterns)
- [Abstract Classes as Tokens](#abstract-classes-as-tokens)
- [Hierarchical Injection](#hierarchical-injection)
- [Dynamic Providers](#dynamic-providers)
- [Testing with DI](#testing-with-di)
- [DestroyRef and Cleanup](#destroyref-and-cleanup)

## Service Patterns

### Facade Service

Combine multiple services into a single API:

```typescript
@Injectable({ providedIn: 'root' })
export class ShopFacade {
  private productService = inject(Product);
  private cartService = inject(Cart);
  private orderService = inject(Order);
  
  // Expose combined state
  readonly products = this.productService.products;
  readonly cart = this.cartService.items;
  readonly cartTotal = this.cartService.total;
  
  // Unified actions
  addToCart(productId: string, quantity: number) {
    const product = this.productService.getById(productId);
    if (product) {
      this.cartService.add(product, quantity);
    }
  }
  
  async checkout() {
    const items = this.cartService.items();
    const order = await this.orderService.create(items);
    this.cartService.clear();
    return order;
  }
}
```

### State Service Pattern

```typescript
interface UserState {
  user: User | null;
  loading: boolean;
  error: string | null;
}

@Injectable({ providedIn: 'root' })
export class UserState {
  private state = signal<UserState>({
    user: null,
    loading: false,
    error: null,
  });
  
  // Selectors
  readonly user = computed(() => this.state().user);
  readonly loading = computed(() => this.state().loading);
  readonly error = computed(() => this.state().error);
  readonly isAuthenticated = computed(() => this.state().user !== null);
  
  // Actions
  setUser(user: User) {
    this.state.update(s => ({ ...s, user, loading: false, error: null }));
  }
  
  setLoading() {
    this.state.update(s => ({ ...s, loading: true, error: null }));
  }
  
  setError(error: string) {
    this.state.update(s => ({ ...s, loading: false, error }));
  }
  
  clear() {
    this.state.set({ user: null, loading: false, error: null });
  }
}
```

### Repository Pattern

```typescript
// Generic repository interface
export abstract class Repository<T extends { id: string }> {
  abstract getAll(): Promise<T[]>;
  abstract getById(id: string): Promise<T | null>;
  abstract create(item: Omit<T, 'id'>): Promise<T>;
  abstract update(id: string, item: Partial<T>): Promise<T>;
  abstract delete(id: string): Promise<void>;
}

// HTTP implementation
@Injectable()
export class HttpUserRepo extends Repository<User> {
  private http = inject(HttpClient);
  private apiUrl = inject(API_URL);
  
  async getAll(): Promise<User[]> {
    return firstValueFrom(this.http.get<User[]>(`${this.apiUrl}/users`));
  }
  
  async getById(id: string): Promise<User | null> {
    return firstValueFrom(
      this.http.get<User>(`${this.apiUrl}/users/${id}`).pipe(
        catchError(() => of(null))
      )
    );
  }
  
  async create(user: Omit<User, 'id'>): Promise<User> {
    return firstValueFrom(this.http.post<User>(`${this.apiUrl}/users`, user));
  }
  
  async update(id: string, user: Partial<User>): Promise<User> {
    return firstValueFrom(this.http.patch<User>(`${this.apiUrl}/users/${id}`, user));
  }
  
  async delete(id: string): Promise<void> {
    await firstValueFrom(this.http.delete(`${this.apiUrl}/users/${id}`));
  }
}

// Provide implementation
{ provide: Repository, useClass: HttpUserRepo }
```

## Abstract Classes as Tokens

Use abstract classes for better type safety:

```typescript
// Abstract service definition
export abstract class Logger {
  abstract log(message: string): void;
  abstract error(message: string, error?: Error): void;
  abstract warn(message: string): void;
}

// Console implementation
@Injectable()
export class ConsoleLog extends Logger {
  log(message: string) {
    console.log(`[LOG] ${message}`);
  }
  
  error(message: string, error?: Error) {
    console.error(`[ERROR] ${message}`, error);
  }
  
  warn(message: string) {
    console.warn(`[WARN] ${message}`);
  }
}

// Remote implementation
@Injectable()
export class RemoteLog extends Logger {
  private http = inject(HttpClient);
  
  log(message: string) {
    this.send('log', message);
  }
  
  error(message: string, error?: Error) {
    this.send('error', message, error);
  }
  
  warn(message: string) {
    this.send('warn', message);
  }
  
  private send(level: string, message: string, error?: Error) {
    this.http.post('/api/logs', { level, message, error: error?.message }).subscribe();
  }
}

// Provide based on environment
{
  provide: Logger,
  useClass: environment.production ? RemoteLog : ConsoleLog,
}

// Inject using abstract class
@Injectable({ providedIn: 'root' })
export class User {
  private logger = inject(Logger);

  createUser(user: UserData) {
    this.logger.log(`Creating user: ${user.email}`);
    // ...
  }
}
```

## Hierarchical Injection

### Component Tree Injection

```typescript
// Parent provides service
@Component({
  selector: 'app-form-container',
  providers: [FormState],
  template: `
    <app-form-header />
    <app-form-body />
    <app-form-footer />
  `,
})
export class FormContainer {
  private formState = inject(FormState);
}

// Children share same instance
@Component({
  selector: 'app-form-body',
  template: `...`,
})
export class FormBody {
  // Gets same instance as parent
  private formState = inject(FormState);
}

// Grandchildren also share
@Component({
  selector: 'app-form-field',
  template: `...`,
})
export class FormField {
  // Gets same instance from ancestor
  private formState = inject(FormState);
}
```

### viewProviders vs providers

```typescript
@Component({
  selector: 'app-tabs',
  // providers: Available to component AND content children
  providers: [TabsSvc],

  // viewProviders: Available to component AND view children only
  // NOT available to content children (<ng-content>)
  viewProviders: [InternalTabs],
  
  template: `
    <div class="tabs">
      <ng-content /> <!-- Content children can't access viewProviders -->
    </div>
  `,
})
export class Tabs {}
```

## Dynamic Providers

### Feature Flags

```typescript
export const FEATURE_FLAGS = new InjectionToken<FeatureFlags>('FeatureFlags');

interface FeatureFlags {
  newDashboard: boolean;
  betaFeatures: boolean;
  experimentalApi: boolean;
}

// Load from API
{
  provide: FEATURE_FLAGS,
  useFactory: async () => {
    const response = await fetch('/api/features');
    return response.json();
  },
}

// Use in components
@Component({...})
export class Dashboard {
  private features = inject(FEATURE_FLAGS);
  
  showNewDashboard = this.features.newDashboard;
}
```

### Platform-Specific Services

```typescript
export abstract class Storage {
  abstract get(key: string): string | null;
  abstract set(key: string, value: string): void;
  abstract remove(key: string): void;
}

@Injectable()
export class BrowserStorage extends Storage {
  get(key: string) { return localStorage.getItem(key); }
  set(key: string, value: string) { localStorage.setItem(key, value); }
  remove(key: string) { localStorage.removeItem(key); }
}

@Injectable()
export class ServerStorage extends Storage {
  private store = new Map<string, string>();

  get(key: string) { return this.store.get(key) ?? null; }
  set(key: string, value: string) { this.store.set(key, value); }
  remove(key: string) { this.store.delete(key); }
}

// Provide based on platform
import { PLATFORM_ID, isPlatformBrowser } from '@angular/common';

{
  provide: Storage,
  useFactory: (platformId: object) => {
    return isPlatformBrowser(platformId)
      ? new BrowserStorage()
      : new ServerStorage();
  },
  deps: [PLATFORM_ID],
}
```

## Testing with DI

### Mocking Services

```typescript
describe('UserCmpt', () => {
  let userServiceSpy: jasmine.SpyObj<User>;
  
  beforeEach(async () => {
    userServiceSpy = jasmine.createSpyObj('User', ['getUser', 'updateUser']);
    userServiceSpy.getUser.and.returnValue(of({ id: '1', name: 'Test' }));
    
    await TestBed.configureTestingModule({
      imports: [UserCmpt],
      providers: [
        { provide: User, useValue: userServiceSpy },
      ],
    }).compileComponents();
  });
  
  it('should load user', () => {
    const fixture = TestBed.createComponent(UserCmpt);
    fixture.detectChanges();
    
    expect(userServiceSpy.getUser).toHaveBeenCalled();
  });
});
```

### Overriding Providers

```typescript
describe('with different config', () => {
  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [App],
    })
    .overrideProvider(APP_CONFIG, {
      useValue: { apiUrl: 'http://test-api.com' },
    })
    .compileComponents();
  });
});
```

### Testing Injection Tokens

```typescript
describe('API_URL token', () => {
  it('should provide correct URL', () => {
    TestBed.configureTestingModule({
      providers: [
        { provide: API_URL, useValue: 'https://api.test.com' },
      ],
    });
    
    const apiUrl = TestBed.inject(API_URL);
    expect(apiUrl).toBe('https://api.test.com');
  });
});
```

## DestroyRef and Cleanup

### Automatic Cleanup

```typescript
import { DestroyRef, inject } from '@angular/core';
import { takeUntilDestroyed } from '@angular/core/rxjs-interop';

@Component({...})
export class Data {
  private destroyRef = inject(DestroyRef);
  private dataService = inject(DataSvc);
  
  constructor() {
    // Auto-unsubscribe when component destroys
    this.dataService.data$
      .pipe(takeUntilDestroyed())
      .subscribe(data => {
        console.log(data);
      });
  }
  
  // Or use DestroyRef directly
  ngOnInit() {
    const subscription = this.dataService.updates$.subscribe();
    
    this.destroyRef.onDestroy(() => {
      subscription.unsubscribe();
      console.log('Cleaned up!');
    });
  }
}
```

### In Services

```typescript
@Injectable()
export class WebSocket {
  private destroyRef = inject(DestroyRef);
  private socket: WebSocket | null = null;
  
  constructor() {
    this.destroyRef.onDestroy(() => {
      this.socket?.close();
    });
  }
  
  connect(url: string) {
    this.socket = new WebSocket(url);
  }
}
```

### takeUntilDestroyed Outside Constructor

```typescript
@Component({...})
export class My {
  private destroyRef = inject(DestroyRef);

  loadData() {
    // Pass destroyRef when using outside constructor
    this.http.get('/api/data')
      .pipe(takeUntilDestroyed(this.destroyRef))
      .subscribe();
  }
}
```

## Injection Context Utilities

### assertInInjectionContext

```typescript
import { assertInInjectionContext, inject } from '@angular/core';

export function injectLogger(): Logger {
  assertInInjectionContext(injectLogger);
  return inject(Logger);
}

// Usage - must be called in injection context
@Component({...})
export class My2 {
  private logger = injectLogger(); // OK

  someMethod() {
    // injectLogger(); // ERROR - not in injection context
  }
}
```

### Custom inject Functions

```typescript
// Create reusable injection utilities
export function injectRouteParam(param: string): Signal<string | null> {
  assertInInjectionContext(injectRouteParam);
  
  const route = inject(ActivatedRoute);
  return toSignal(
    route.paramMap.pipe(map(params => params.get(param))),
    { initialValue: null }
  );
}

export function injectQueryParam(param: string): Signal<string | null> {
  assertInInjectionContext(injectQueryParam);
  
  const route = inject(ActivatedRoute);
  return toSignal(
    route.queryParamMap.pipe(map(params => params.get(param))),
    { initialValue: null }
  );
}

// Usage
@Component({...})
export class UserCmpt {
  userId = injectRouteParam('id');
  tab = injectQueryParam('tab');
}
```
```

## File: `skills/angular-directives/SKILL.md`
```markdown
---
name: angular-directives
description: Create custom directives in Angular v20+ for DOM manipulation and behavior extension. Use for attribute directives that modify element behavior/appearance, structural directives for portals/overlays, and host directives for composition. Triggers on creating reusable DOM behaviors, extending element functionality, or composing behaviors across components. Note - use native @if/@for/@switch for control flow, not custom structural directives.
---

# Angular Directives

Create custom directives for reusable DOM manipulation and behavior in Angular v20+.

## Attribute Directives

Modify the appearance or behavior of an element:

```typescript
import { Directive, input, effect, inject, ElementRef } from '@angular/core';

@Directive({
  selector: '[appHighlight]',
})
export class Highlight {
  private el = inject(ElementRef<HTMLElement>);
  
  // Input with alias matching selector
  color = input('yellow', { alias: 'appHighlight' });
  
  constructor() {
    effect(() => {
      this.el.nativeElement.style.backgroundColor = this.color();
    });
  }
}

// Usage: <p appHighlight="lightblue">Highlighted text</p>
// Usage: <p appHighlight>Default yellow highlight</p>
```

### Using host Property

Prefer `host` over `@HostBinding`/`@HostListener`:

```typescript
@Directive({
  selector: '[appTooltip]',
  host: {
    '(mouseenter)': 'show()',
    '(mouseleave)': 'hide()',
    '[attr.aria-describedby]': 'tooltipId',
  },
})
export class Tooltip {
  text = input.required<string>({ alias: 'appTooltip' });
  position = input<'top' | 'bottom' | 'left' | 'right'>('top');
  
  tooltipId = `tooltip-${crypto.randomUUID()}`;
  private tooltipEl: HTMLElement | null = null;
  private el = inject(ElementRef<HTMLElement>);
  
  show() {
    this.tooltipEl = document.createElement('div');
    this.tooltipEl.id = this.tooltipId;
    this.tooltipEl.className = `tooltip tooltip-${this.position()}`;
    this.tooltipEl.textContent = this.text();
    this.tooltipEl.setAttribute('role', 'tooltip');
    document.body.appendChild(this.tooltipEl);
    this.positionTooltip();
  }
  
  hide() {
    this.tooltipEl?.remove();
    this.tooltipEl = null;
  }
  
  private positionTooltip() {
    // Position logic based on this.position() and this.el
  }
}

// Usage: <button appTooltip="Click to save" position="bottom">Save</button>
```

### Class and Style Manipulation

```typescript
@Directive({
  selector: '[appButton]',
  host: {
    'class': 'btn',
    '[class.btn-primary]': 'variant() === "primary"',
    '[class.btn-secondary]': 'variant() === "secondary"',
    '[class.btn-sm]': 'size() === "small"',
    '[class.btn-lg]': 'size() === "large"',
    '[class.disabled]': 'disabled()',
    '[attr.disabled]': 'disabled() || null',
  },
})
export class Button {
  variant = input<'primary' | 'secondary'>('primary');
  size = input<'small' | 'medium' | 'large'>('medium');
  disabled = input(false, { transform: booleanAttribute });
}

// Usage: <button appButton variant="primary" size="large">Click</button>
```

### Event Handling

```typescript
@Directive({
  selector: '[appClickOutside]',
  host: {
    '(document:click)': 'onDocumentClick($event)',
  },
})
export class ClickOutside {
  private el = inject(ElementRef<HTMLElement>);
  
  clickOutside = output<void>();
  
  onDocumentClick(event: MouseEvent) {
    if (!this.el.nativeElement.contains(event.target as Node)) {
      this.clickOutside.emit();
    }
  }
}

// Usage: <div appClickOutside (clickOutside)="closeMenu()">...</div>
```

### Keyboard Shortcuts

```typescript
@Directive({
  selector: '[appShortcut]',
  host: {
    '(document:keydown)': 'onKeydown($event)',
  },
})
export class Shortcut {
  key = input.required<string>({ alias: 'appShortcut' });
  ctrl = input(false, { transform: booleanAttribute });
  shift = input(false, { transform: booleanAttribute });
  alt = input(false, { transform: booleanAttribute });
  
  triggered = output<KeyboardEvent>();
  
  onKeydown(event: KeyboardEvent) {
    const keyMatch = event.key.toLowerCase() === this.key().toLowerCase();
    const ctrlMatch = this.ctrl() ? event.ctrlKey || event.metaKey : !event.ctrlKey && !event.metaKey;
    const shiftMatch = this.shift() ? event.shiftKey : !event.shiftKey;
    const altMatch = this.alt() ? event.altKey : !event.altKey;
    
    if (keyMatch && ctrlMatch && shiftMatch && altMatch) {
      event.preventDefault();
      this.triggered.emit(event);
    }
  }
}

// Usage: <button appShortcut="s" ctrl (triggered)="save()">Save (Ctrl+S)</button>
```

## Structural Directives

Use structural directives for DOM manipulation beyond control flow (portals, overlays, dynamic insertion points). For conditionals and loops, use native `@if`, `@for`, `@switch`.

### Portal Directive

Render content in a different DOM location:

```typescript
import { Directive, inject, TemplateRef, ViewContainerRef, OnInit, OnDestroy, input } from '@angular/core';

@Directive({
  selector: '[appPortal]',
})
export class Portal implements OnInit, OnDestroy {
  private templateRef = inject(TemplateRef<any>);
  private viewContainerRef = inject(ViewContainerRef);
  private viewRef: EmbeddedViewRef<any> | null = null;
  
  // Target container selector or element
  target = input<string | HTMLElement>('body', { alias: 'appPortal' });
  
  ngOnInit() {
    const container = this.getContainer();
    if (container) {
      this.viewRef = this.viewContainerRef.createEmbeddedView(this.templateRef);
      this.viewRef.rootNodes.forEach(node => container.appendChild(node));
    }
  }
  
  ngOnDestroy() {
    this.viewRef?.destroy();
  }
  
  private getContainer(): HTMLElement | null {
    const target = this.target();
    if (typeof target === 'string') {
      return document.querySelector(target);
    }
    return target;
  }
}

// Usage: Render modal at body level
// <div *appPortal="'body'">
//   <div class="modal">Modal content</div>
// </div>
```

### Lazy Render Directive

Defer rendering until condition is met (one-time):

```typescript
@Directive({
  selector: '[appLazyRender]',
})
export class LazyRender {
  private templateRef = inject(TemplateRef<any>);
  private viewContainer = inject(ViewContainerRef);
  private rendered = false;
  
  condition = input.required<boolean>({ alias: 'appLazyRender' });
  
  constructor() {
    effect(() => {
      // Only render once when condition becomes true
      if (this.condition() && !this.rendered) {
        this.viewContainer.createEmbeddedView(this.templateRef);
        this.rendered = true;
      }
    });
  }
}

// Usage: Render heavy component only when tab is first activated
// <div *appLazyRender="activeTab() === 'reports'">
//   <app-heavy-reports />
// </div>
```

### Template Outlet with Context

```typescript
interface TemplateContext<T> {
  $implicit: T;
  item: T;
  index: number;
}

@Directive({
  selector: '[appTemplateOutlet]',
})
export class TemplateOutlet<T> {
  private viewContainer = inject(ViewContainerRef);
  private currentView: EmbeddedViewRef<TemplateContext<T>> | null = null;
  
  template = input.required<TemplateRef<TemplateContext<T>>>({ alias: 'appTemplateOutlet' });
  context = input.required<T>({ alias: 'appTemplateOutletContext' });
  index = input(0, { alias: 'appTemplateOutletIndex' });
  
  constructor() {
    effect(() => {
      const template = this.template();
      const context = this.context();
      const index = this.index();
      
      if (this.currentView) {
        this.currentView.context.$implicit = context;
        this.currentView.context.item = context;
        this.currentView.context.index = index;
        this.currentView.markForCheck();
      } else {
        this.currentView = this.viewContainer.createEmbeddedView(template, {
          $implicit: context,
          item: context,
          index,
        });
      }
    });
  }
}

// Usage: Custom list with template
// <ng-template #itemTemplate let-item let-i="index">
//   <div>{{ i }}: {{ item.name }}</div>
// </ng-template>
// <ng-container 
//   *appTemplateOutlet="itemTemplate; context: item; index: i"
// />
```

## Host Directives

Compose directives on components or other directives:

```typescript
// Reusable behavior directives
@Directive({
  selector: '[focusable]',
  host: {
    'tabindex': '0',
    '(focus)': 'onFocus()',
    '(blur)': 'onBlur()',
    '[class.focused]': 'isFocused()',
  },
})
export class Focusable {
  isFocused = signal(false);
  
  onFocus() { this.isFocused.set(true); }
  onBlur() { this.isFocused.set(false); }
}

@Directive({
  selector: '[disableable]',
  host: {
    '[class.disabled]': 'disabled()',
    '[attr.aria-disabled]': 'disabled()',
  },
})
export class Disableable {
  disabled = input(false, { transform: booleanAttribute });
}

// Component using host directives
@Component({
  selector: 'app-custom-button',
  hostDirectives: [
    Focusable,
    {
      directive: Disableable,
      inputs: ['disabled'],
    },
  ],
  host: {
    'role': 'button',
    '(click)': 'onClick($event)',
    '(keydown.enter)': 'onClick($event)',
    '(keydown.space)': 'onClick($event)',
  },
  template: `<ng-content />`,
})
export class CustomButton {
  private disableable = inject(Disableable);
  
  clicked = output<void>();
  
  onClick(event: Event) {
    if (!this.disableable.disabled()) {
      this.clicked.emit();
    }
  }
}

// Usage: <app-custom-button disabled>Click me</app-custom-button>
```

### Exposing Host Directive Outputs

```typescript
@Directive({
  selector: '[hoverable]',
  host: {
    '(mouseenter)': 'onEnter()',
    '(mouseleave)': 'onLeave()',
    '[class.hovered]': 'isHovered()',
  },
})
export class Hoverable {
  isHovered = signal(false);
  
  hoverChange = output<boolean>();
  
  onEnter() {
    this.isHovered.set(true);
    this.hoverChange.emit(true);
  }
  
  onLeave() {
    this.isHovered.set(false);
    this.hoverChange.emit(false);
  }
}

@Component({
  selector: 'app-card',
  hostDirectives: [
    {
      directive: Hoverable,
      outputs: ['hoverChange'],
    },
  ],
  template: `<ng-content />`,
})
export class Card {}

// Usage: <app-card (hoverChange)="onHover($event)">...</app-card>
```

## Directive Composition API

Combine multiple behaviors:

```typescript
// Base directives
@Directive({ selector: '[withRipple]' })
export class Ripple {
  // Ripple effect implementation
}

@Directive({ selector: '[withElevation]' })
export class Elevation {
  elevation = input(2);
}

// Composed component
@Component({
  selector: 'app-material-button',
  hostDirectives: [
    Ripple,
    {
      directive: Elevation,
      inputs: ['elevation'],
    },
    {
      directive: Disableable,
      inputs: ['disabled'],
    },
  ],
  template: `<ng-content />`,
})
export class MaterialButton {}
```

For advanced patterns, see [references/directive-patterns.md](references/directive-patterns.md).
```

## File: `skills/angular-directives/references/directive-patterns.md`
```markdown
# Angular Directive Patterns

## Table of Contents
- [DOM Manipulation](#dom-manipulation)
- [Form Directives](#form-directives)
- [Intersection Observer](#intersection-observer)
- [Resize Observer](#resize-observer)
- [Drag and Drop](#drag-and-drop)
- [Permission Directive](#permission-directive)

## DOM Manipulation

### Auto-Focus Directive

```typescript
@Directive({
  selector: '[appAutoFocus]',
})
export class AutoFocus {
  private el = inject(ElementRef<HTMLElement>);
  
  enabled = input(true, { alias: 'appAutoFocus', transform: booleanAttribute });
  delay = input(0);
  
  constructor() {
    afterNextRender(() => {
      if (this.enabled()) {
        setTimeout(() => {
          this.el.nativeElement.focus();
        }, this.delay());
      }
    });
  }
}

// Usage: <input appAutoFocus />
// Usage: <input [appAutoFocus]="shouldFocus()" [delay]="100" />
```

### Text Selection Directive

```typescript
@Directive({
  selector: '[appSelectAll]',
  host: {
    '(focus)': 'onFocus()',
    '(click)': 'onClick($event)',
  },
})
export class SelectAll {
  private el = inject(ElementRef<HTMLInputElement>);
  
  onFocus() {
    // Delay to ensure value is set
    setTimeout(() => this.el.nativeElement.select(), 0);
  }
  
  onClick(event: MouseEvent) {
    // Select all on first click if not already focused
    if (document.activeElement !== this.el.nativeElement) {
      this.el.nativeElement.select();
    }
  }
}

// Usage: <input appSelectAll value="Select me on focus" />
```

### Copy to Clipboard

```typescript
@Directive({
  selector: '[appCopyToClipboard]',
  host: {
    '(click)': 'copy()',
    '[style.cursor]': '"pointer"',
  },
})
export class CopyToClipboard {
  text = input.required<string>({ alias: 'appCopyToClipboard' });
  
  copied = output<void>();
  error = output<Error>();
  
  async copy() {
    try {
      await navigator.clipboard.writeText(this.text());
      this.copied.emit();
    } catch (err) {
      this.error.emit(err as Error);
    }
  }
}

// Usage: 
// <button [appCopyToClipboard]="textToCopy" (copied)="showToast('Copied!')">
//   Copy
// </button>
```

## Form Directives

### Trim Input

```typescript
@Directive({
  selector: 'input[appTrim], textarea[appTrim]',
  host: {
    '(blur)': 'onBlur()',
  },
})
export class Trim {
  private el = inject(ElementRef<HTMLInputElement | HTMLTextAreaElement>);
  private ngControl = inject(NgControl, { optional: true, self: true });
  
  onBlur() {
    const value = this.el.nativeElement.value;
    const trimmed = value.trim();
    
    if (value !== trimmed) {
      this.el.nativeElement.value = trimmed;
      this.ngControl?.control?.setValue(trimmed);
    }
  }
}

// Usage: <input appTrim formControlName="name" />
```

### Input Mask

```typescript
@Directive({
  selector: '[appMask]',
  host: {
    '(input)': 'onInput($event)',
    '(keydown)': 'onKeydown($event)',
  },
})
export class Mask {
  private el = inject(ElementRef<HTMLInputElement>);
  
  // Mask pattern: 9 = digit, A = letter, * = any
  mask = input.required<string>({ alias: 'appMask' });
  
  onInput(event: InputEvent) {
    const input = this.el.nativeElement;
    const value = input.value;
    const masked = this.applyMask(value);
    
    if (value !== masked) {
      input.value = masked;
    }
  }
  
  onKeydown(event: KeyboardEvent) {
    // Allow navigation keys
    if (['Backspace', 'Delete', 'ArrowLeft', 'ArrowRight', 'Tab'].includes(event.key)) {
      return;
    }
    
    const input = this.el.nativeElement;
    const position = input.selectionStart ?? 0;
    const maskChar = this.mask()[position];
    
    if (!maskChar) {
      event.preventDefault();
      return;
    }
    
    if (!this.isValidChar(event.key, maskChar)) {
      event.preventDefault();
    }
  }
  
  private applyMask(value: string): string {
    const mask = this.mask();
    let result = '';
    let valueIndex = 0;
    
    for (let i = 0; i < mask.length && valueIndex < value.length; i++) {
      const maskChar = mask[i];
      const inputChar = value[valueIndex];
      
      if (maskChar === '9' || maskChar === 'A' || maskChar === '*') {
        if (this.isValidChar(inputChar, maskChar)) {
          result += inputChar;
          valueIndex++;
        } else {
          valueIndex++;
          i--;
        }
      } else {
        result += maskChar;
        if (inputChar === maskChar) {
          valueIndex++;
        }
      }
    }
    
    return result;
  }
  
  private isValidChar(char: string, maskChar: string): boolean {
    switch (maskChar) {
      case '9': return /\d/.test(char);
      case 'A': return /[a-zA-Z]/.test(char);
      case '*': return /[a-zA-Z0-9]/.test(char);
      default: return char === maskChar;
    }
  }
}

// Usage: <input appMask="(999) 999-9999" placeholder="(555) 123-4567" />
```

### Character Counter

```typescript
@Directive({
  selector: '[appCharCount]',
})
export class CharCount {
  private el = inject(ElementRef<HTMLInputElement | HTMLTextAreaElement>);
  
  maxLength = input.required<number>({ alias: 'appCharCount' });
  
  currentLength = signal(0);
  remaining = computed(() => this.maxLength() - this.currentLength());
  isOverLimit = computed(() => this.remaining() < 0);
  
  constructor() {
    effect(() => {
      this.currentLength.set(this.el.nativeElement.value.length);
    });
    
    // Listen for input changes
    afterNextRender(() => {
      this.el.nativeElement.addEventListener('input', () => {
        this.currentLength.set(this.el.nativeElement.value.length);
      });
    });
  }
}

// Usage with template:
// <textarea appCharCount="500" #counter="appCharCount"></textarea>
// <span>{{ counter.remaining() }} characters remaining</span>
```

## Intersection Observer

### Lazy Load Directive

```typescript
@Directive({
  selector: '[appLazyLoad]',
})
export class LazyLoad implements OnDestroy {
  private el = inject(ElementRef<HTMLElement>);
  private observer: IntersectionObserver | null = null;
  
  src = input.required<string>({ alias: 'appLazyLoad' });
  placeholder = input('/assets/placeholder.png');
  
  loaded = output<void>();
  
  constructor() {
    afterNextRender(() => {
      this.setupObserver();
    });
  }
  
  private setupObserver() {
    this.observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            this.loadImage();
            this.observer?.disconnect();
          }
        });
      },
      { rootMargin: '50px' }
    );
    
    this.observer.observe(this.el.nativeElement);
    
    // Set placeholder
    if (this.el.nativeElement instanceof HTMLImageElement) {
      this.el.nativeElement.src = this.placeholder();
    }
  }
  
  private loadImage() {
    const element = this.el.nativeElement;
    
    if (element instanceof HTMLImageElement) {
      element.src = this.src();
      element.onload = () => this.loaded.emit();
    } else {
      element.style.backgroundImage = `url(${this.src()})`;
      this.loaded.emit();
    }
  }
  
  ngOnDestroy() {
    this.observer?.disconnect();
  }
}

// Usage: <img [appLazyLoad]="imageUrl" alt="Lazy loaded image" />
```

### Infinite Scroll

```typescript
@Directive({
  selector: '[appInfiniteScroll]',
})
export class InfiniteScroll implements OnDestroy {
  private el = inject(ElementRef<HTMLElement>);
  private observer: IntersectionObserver | null = null;
  
  threshold = input(0.1);
  disabled = input(false);
  
  scrolled = output<void>();
  
  constructor() {
    afterNextRender(() => {
      this.setupObserver();
    });
    
    effect(() => {
      if (this.disabled()) {
        this.observer?.disconnect();
      } else {
        this.setupObserver();
      }
    });
  }
  
  private setupObserver() {
    this.observer?.disconnect();
    
    this.observer = new IntersectionObserver(
      (entries) => {
        if (entries[0].isIntersecting && !this.disabled()) {
          this.scrolled.emit();
        }
      },
      { threshold: this.threshold() }
    );
    
    this.observer.observe(this.el.nativeElement);
  }
  
  ngOnDestroy() {
    this.observer?.disconnect();
  }
}

// Usage:
// <div class="list">
//   @for (item of items(); track item.id) {
//     <div>{{ item.name }}</div>
//   }
//   <div appInfiniteScroll (scrolled)="loadMore()" [disabled]="isLoading()">
//     Loading...
//   </div>
// </div>
```

## Resize Observer

```typescript
@Directive({
  selector: '[appResize]',
})
export class Resize implements OnDestroy {
  private el = inject(ElementRef<HTMLElement>);
  private observer: ResizeObserver | null = null;
  
  width = signal(0);
  height = signal(0);
  
  resized = output<{ width: number; height: number }>();
  
  constructor() {
    afterNextRender(() => {
      this.observer = new ResizeObserver((entries) => {
        const entry = entries[0];
        const { width, height } = entry.contentRect;
        
        this.width.set(width);
        this.height.set(height);
        this.resized.emit({ width, height });
      });
      
      this.observer.observe(this.el.nativeElement);
    });
  }
  
  ngOnDestroy() {
    this.observer?.disconnect();
  }
}

// Usage:
// <div appResize #resize="appResize">
//   Size: {{ resize.width() }}x{{ resize.height() }}
// </div>
```

## Drag and Drop

```typescript
@Directive({
  selector: '[appDraggable]',
  host: {
    'draggable': 'true',
    '[class.dragging]': 'isDragging()',
    '(dragstart)': 'onDragStart($event)',
    '(dragend)': 'onDragEnd($event)',
  },
})
export class Draggable {
  data = input<any>(null, { alias: 'appDraggable' });
  effectAllowed = input<DataTransfer['effectAllowed']>('move');
  
  isDragging = signal(false);
  
  dragStart = output<DragEvent>();
  dragEnd = output<DragEvent>();
  
  onDragStart(event: DragEvent) {
    this.isDragging.set(true);
    
    if (event.dataTransfer) {
      event.dataTransfer.effectAllowed = this.effectAllowed();
      event.dataTransfer.setData('application/json', JSON.stringify(this.data()));
    }
    
    this.dragStart.emit(event);
  }
  
  onDragEnd(event: DragEvent) {
    this.isDragging.set(false);
    this.dragEnd.emit(event);
  }
}

@Directive({
  selector: '[appDropZone]',
  host: {
    '[class.drag-over]': 'isDragOver()',
    '(dragover)': 'onDragOver($event)',
    '(dragleave)': 'onDragLeave($event)',
    '(drop)': 'onDrop($event)',
  },
})
export class DropZone {
  isDragOver = signal(false);
  
  dropped = output<any>();
  
  onDragOver(event: DragEvent) {
    event.preventDefault();
    this.isDragOver.set(true);
  }
  
  onDragLeave(event: DragEvent) {
    this.isDragOver.set(false);
  }
  
  onDrop(event: DragEvent) {
    event.preventDefault();
    this.isDragOver.set(false);
    
    const data = event.dataTransfer?.getData('application/json');
    if (data) {
      this.dropped.emit(JSON.parse(data));
    }
  }
}

// Usage:
// <div [appDraggable]="item">Drag me</div>
// <div appDropZone (dropped)="onItemDropped($event)">Drop here</div>
```

## Permission Directive

```typescript
@Directive({
  selector: '[appHasPermission]',
})
export class HasPermission {
  private templateRef = inject(TemplateRef<any>);
  private viewContainer = inject(ViewContainerRef);
  private authService = inject(Auth);
  private hasView = false;
  
  permission = input.required<string | string[]>({ alias: 'appHasPermission' });
  mode = input<'any' | 'all'>('any');
  
  constructor() {
    effect(() => {
      const hasPermission = this.checkPermission();
      
      if (hasPermission && !this.hasView) {
        this.viewContainer.createEmbeddedView(this.templateRef);
        this.hasView = true;
      } else if (!hasPermission && this.hasView) {
        this.viewContainer.clear();
        this.hasView = false;
      }
    });
  }
  
  private checkPermission(): boolean {
    const required = this.permission();
    const permissions = Array.isArray(required) ? required : [required];
    const userPermissions = this.authService.permissions();
    
    if (this.mode() === 'all') {
      return permissions.every(p => userPermissions.includes(p));
    }
    
    return permissions.some(p => userPermissions.includes(p));
  }
}

// Usage:
// <button *appHasPermission="'admin'">Admin Only</button>
// <div *appHasPermission="['edit', 'delete']; mode: 'all'">Edit & Delete</div>
```

## Export Directive Reference

```typescript
@Directive({
  selector: '[appToggle]',
  exportAs: 'appToggle',
})
export class Toggle {
  isOpen = signal(false);
  
  toggle() {
    this.isOpen.update(v => !v);
  }
  
  open() {
    this.isOpen.set(true);
  }
  
  close() {
    this.isOpen.set(false);
  }
}

// Usage:
// <div appToggle #toggle="appToggle">
//   <button (click)="toggle.toggle()">Toggle</button>
//   @if (toggle.isOpen()) {
//     <div>Content</div>
//   }
// </div>
```
```

## File: `skills/angular-forms/SKILL.md`
```markdown
---
name: angular-forms
description: Build signal-based forms in Angular v21+ using the new Signal Forms API. Use for form creation with automatic two-way binding, schema-based validation, field state management, and dynamic forms. Triggers on form implementation, adding validation, creating multi-step forms, or building forms with conditional fields. Signal Forms are experimental but recommended for new Angular projects. Don't use for template-driven forms without signals or third-party form libraries like Formly or ngx-formly.
---

# Angular Signal Forms

Build type-safe, reactive forms using Angular's Signal Forms API. Signal Forms provide automatic two-way binding, schema-based validation, and reactive field state.

**Note:** Signal Forms are experimental in Angular v21. For production apps requiring stability, see [references/form-patterns.md](references/form-patterns.md) for Reactive Forms patterns.

## Basic Setup

```typescript
import { Component, signal } from '@angular/core';
import { form, FormField, required, email } from '@angular/forms/signals';

interface LoginData {
  email: string;
  password: string;
}

@Component({
  selector: 'app-login',
  imports: [FormField],
  template: `
    <form (submit)="onSubmit($event)">
      <label>
        Email
        <input type="email" [formField]="loginForm.email" />
      </label>
      @if (loginForm.email().touched() && loginForm.email().invalid()) {
        <p class="error">{{ loginForm.email().errors()[0].message }}</p>
      }
      
      <label>
        Password
        <input type="password" [formField]="loginForm.password" />
      </label>
      @if (loginForm.password().touched() && loginForm.password().invalid()) {
        <p class="error">{{ loginForm.password().errors()[0].message }}</p>
      }
      
      <button type="submit" [disabled]="loginForm().invalid()">Login</button>
    </form>
  `,
})
export class Login {
  // Form model - a writable signal
  loginModel = signal<LoginData>({
    email: '',
    password: '',
  });
  
  // Create form with validation schema
  loginForm = form(this.loginModel, (schemaPath) => {
    required(schemaPath.email, { message: 'Email is required' });
    email(schemaPath.email, { message: 'Enter a valid email address' });
    required(schemaPath.password, { message: 'Password is required' });
  });
  
  onSubmit(event: Event) {
    event.preventDefault();
    if (this.loginForm().valid()) {
      const credentials = this.loginModel();
      console.log('Submitting:', credentials);
    }
  }
}
```

## Form Models

Form models are writable signals that serve as the single source of truth:

```typescript
// Define interface for type safety
interface UserProfile {
  name: string;
  email: string;
  age: number | null;
  preferences: {
    newsletter: boolean;
    theme: 'light' | 'dark';
  };
}

// Create model signal with initial values
const userModel = signal<UserProfile>({
  name: '',
  email: '',
  age: null,
  preferences: {
    newsletter: false,
    theme: 'light',
  },
});

// Create form from model
const userForm = form(userModel);

// Access nested fields via dot notation
userForm.name                    // FieldTree<string>
userForm.preferences.theme       // FieldTree<'light' | 'dark'>
```

### Reading Values

```typescript
// Read entire model
const data = this.userModel();

// Read field value via field state
const name = this.userForm.name().value();
const theme = this.userForm.preferences.theme().value();
```

### Updating Values

```typescript
// Replace entire model
this.userModel.set({
  name: 'Alice',
  email: 'alice@example.com',
  age: 30,
  preferences: { newsletter: true, theme: 'dark' },
});

// Update single field
this.userForm.name().value.set('Bob');
this.userForm.age().value.update(age => (age ?? 0) + 1);
```

## Field State

Each field provides reactive signals for validation, interaction, and availability:

```typescript
const emailField = this.form.email();

// Validation state
emailField.valid()      // true if passes all validation
emailField.invalid()    // true if has validation errors
emailField.errors()     // array of error objects
emailField.pending()    // true if async validation in progress

// Interaction state
emailField.touched()    // true after focus + blur
emailField.dirty()      // true after user modification

// Availability state
emailField.disabled()   // true if field is disabled
emailField.hidden()     // true if field should be hidden
emailField.readonly()   // true if field is readonly

// Value
emailField.value()      // current field value (signal)
```

### Form-Level State

The form itself is also a field with aggregated state:

```typescript
// Form is valid when all interactive fields are valid
this.form().valid()

// Form is touched when any field is touched
this.form().touched()

// Form is dirty when any field is modified
this.form().dirty()
```

## Validation

### Built-in Validators

```typescript
import { 
  form, required, email, min, max, 
  minLength, maxLength, pattern 
} from '@angular/forms/signals';

const userForm = form(this.userModel, (schemaPath) => {
  // Required field
  required(schemaPath.name, { message: 'Name is required' });
  
  // Email format
  email(schemaPath.email, { message: 'Invalid email' });
  
  // Numeric range
  min(schemaPath.age, 18, { message: 'Must be 18+' });
  max(schemaPath.age, 120, { message: 'Invalid age' });
  
  // String/array length
  minLength(schemaPath.password, 8, { message: 'Min 8 characters' });
  maxLength(schemaPath.bio, 500, { message: 'Max 500 characters' });
  
  // Regex pattern
  pattern(schemaPath.phone, /^\d{3}-\d{3}-\d{4}$/, {
    message: 'Format: 555-123-4567',
  });
});
```

### Conditional Validation

```typescript
const orderForm = form(this.orderModel, (schemaPath) => {
  required(schemaPath.promoCode, {
    message: 'Promo code required for discounts',
    when: ({ valueOf }) => valueOf(schemaPath.applyDiscount),
  });
});
```

### Custom Validators

```typescript
import { validate } from '@angular/forms/signals';

const signupForm = form(this.signupModel, (schemaPath) => {
  // Custom validation logic
  validate(schemaPath.username, ({ value }) => {
    if (value().includes(' ')) {
      return { kind: 'noSpaces', message: 'Username cannot contain spaces' };
    }
    return null;
  });
});
```

### Cross-Field Validation

```typescript
const passwordForm = form(this.passwordModel, (schemaPath) => {
  required(schemaPath.password);
  required(schemaPath.confirmPassword);
  
  // Compare fields
  validate(schemaPath.confirmPassword, ({ value, valueOf }) => {
    if (value() !== valueOf(schemaPath.password)) {
      return { kind: 'mismatch', message: 'Passwords do not match' };
    }
    return null;
  });
});
```

### Async Validation

```typescript
import { validateHttp } from '@angular/forms/signals';

const signupForm = form(this.signupModel, (schemaPath) => {
  validateHttp(schemaPath.username, {
    request: ({ value }) => `/api/check-username?u=${value()}`,
    onSuccess: (response: { taken: boolean }) => {
      if (response.taken) {
        return { kind: 'taken', message: 'Username already taken' };
      }
      return null;
    },
    onError: () => ({
      kind: 'networkError',
      message: 'Could not verify username',
    }),
  });
});
```

## Conditional Fields

### Hidden Fields

```typescript
import { hidden } from '@angular/forms/signals';

const profileForm = form(this.profileModel, (schemaPath) => {
  hidden(schemaPath.publicUrl, ({ valueOf }) => !valueOf(schemaPath.isPublic));
});
```

```html
@if (!profileForm.publicUrl().hidden()) {
  <input [formField]="profileForm.publicUrl" />
}
```

### Disabled Fields

```typescript
import { disabled } from '@angular/forms/signals';

const orderForm = form(this.orderModel, (schemaPath) => {
  disabled(schemaPath.couponCode, ({ valueOf }) => valueOf(schemaPath.total) < 50);
});
```

### Readonly Fields

```typescript
import { readonly } from '@angular/forms/signals';

const accountForm = form(this.accountModel, (schemaPath) => {
  readonly(schemaPath.username); // Always readonly
});
```

## Form Submission

```typescript
import { submit } from '@angular/forms/signals';

@Component({
  template: `
    <form (submit)="onSubmit($event)">
      <input [formField]="form.email" />
      <input [formField]="form.password" />
      <button type="submit" [disabled]="form().invalid()">Submit</button>
    </form>
  `,
})
export class Login {
  model = signal({ email: '', password: '' });
  form = form(this.model, (schemaPath) => {
    required(schemaPath.email);
    required(schemaPath.password);
  });
  
  onSubmit(event: Event) {
    event.preventDefault();
    
    // submit() marks all fields touched and runs callback if valid
    submit(this.form, async () => {
      await this.authService.login(this.model());
    });
  }
}
```

## Arrays and Dynamic Fields

```typescript
interface Order {
  items: Array<{ product: string; quantity: number }>;
}

@Component({
  template: `
    @for (item of orderForm.items; track $index; let i = $index) {
      <div>
        <input [formField]="item.product" placeholder="Product" />
        <input [formField]="item.quantity" type="number" />
        <button type="button" (click)="removeItem(i)">Remove</button>
      </div>
    }
    <button type="button" (click)="addItem()">Add Item</button>
  `,
})
export class Order {
  orderModel = signal<Order>({
    items: [{ product: '', quantity: 1 }],
  });
  
  orderForm = form(this.orderModel, (schemaPath) => {
    applyEach(schemaPath.items, (item) => {
      required(item.product, { message: 'Product required' });
      min(item.quantity, 1, { message: 'Min quantity is 1' });
    });
  });
  
  addItem() {
    this.orderModel.update(m => ({
      ...m,
      items: [...m.items, { product: '', quantity: 1 }],
    }));
  }
  
  removeItem(index: number) {
    this.orderModel.update(m => ({
      ...m,
      items: m.items.filter((_, i) => i !== index),
    }));
  }
}
```

## Displaying Errors

```html
<input [formField]="form.email" />

@if (form.email().touched() && form.email().invalid()) {
  <ul class="errors">
    @for (error of form.email().errors(); track error) {
      <li>{{ error.message }}</li>
    }
  </ul>
}

@if (form.email().pending()) {
  <span>Validating...</span>
}
```

## Styling Based on State

```html
<input
  [formField]="form.email"
  [class.is-invalid]="form.email().touched() && form.email().invalid()"
  [class.is-valid]="form.email().touched() && form.email().valid()"
/>
```

## Reset Form

```typescript
async onSubmit() {
  if (!this.form().valid()) return;
  
  await this.api.submit(this.model());
  
  // Clear interaction state
  this.form().reset();
  
  // Clear values
  this.model.set({ email: '', password: '' });
}
```

For Reactive Forms patterns (production-stable), see [references/form-patterns.md](references/form-patterns.md).
```

## File: `skills/angular-forms/references/form-patterns.md`
```markdown
# Angular Form Patterns

## Table of Contents
- [Reactive Forms (Production-Stable)](#reactive-forms-production-stable)
- [Typed Reactive Forms](#typed-reactive-forms)
- [FormBuilder Patterns](#formbuilder-patterns)
- [Dynamic Forms with FormArray](#dynamic-forms-with-formarray)
- [Custom Validators](#custom-validators)
- [Form State Management](#form-state-management)

## Reactive Forms (Production-Stable)

For production applications requiring stability guarantees, use Reactive Forms:

```typescript
import { Component, inject } from '@angular/core';
import { ReactiveFormsModule, FormBuilder, Validators } from '@angular/forms';

@Component({
  selector: 'app-login',
  imports: [ReactiveFormsModule],
  template: `
    <form [formGroup]="form" (ngSubmit)="onSubmit()">
      <input formControlName="email" />
      @if (form.controls.email.errors?.['required'] && form.controls.email.touched) {
        <span class="error">Email is required</span>
      }
      
      <input type="password" formControlName="password" />
      
      <button type="submit" [disabled]="form.invalid">Login</button>
    </form>
  `,
})
export class Login {
  private fb = inject(FormBuilder);
  
  form = this.fb.group({
    email: ['', [Validators.required, Validators.email]],
    password: ['', [Validators.required, Validators.minLength(8)]],
  });
  
  onSubmit() {
    if (this.form.valid) {
      console.log(this.form.value);
    }
  }
}
```

## Typed Reactive Forms

### Typed FormControl

```typescript
import { FormControl } from '@angular/forms';

// Inferred type: FormControl<string | null>
const name = new FormControl('');

// Non-nullable (no reset to null)
const email = new FormControl('', { nonNullable: true });
// Type: FormControl<string>

// With validators
const username = new FormControl('', {
  nonNullable: true,
  validators: [Validators.required, Validators.minLength(3)],
});
```

### Typed FormGroup

```typescript
import { FormGroup, FormControl } from '@angular/forms';

interface UserForm {
  name: FormControl<string>;
  email: FormControl<string>;
  age: FormControl<number | null>;
}

const form = new FormGroup<UserForm>({
  name: new FormControl('', { nonNullable: true }),
  email: new FormControl('', { nonNullable: true }),
  age: new FormControl<number | null>(null),
});

// Typed value access
const name: string = form.controls.name.value;
```

### NonNullableFormBuilder

```typescript
import { inject } from '@angular/core';
import { NonNullableFormBuilder } from '@angular/forms';

@Component({...})
export class Profile {
  private fb = inject(NonNullableFormBuilder);
  
  form = this.fb.group({
    name: ['', Validators.required],           // FormControl<string>
    email: ['', [Validators.required, Validators.email]],
    preferences: this.fb.group({
      newsletter: [false],                      // FormControl<boolean>
      theme: ['light' as 'light' | 'dark'],    // FormControl<'light' | 'dark'>
    }),
  });
}
```

## FormBuilder Patterns

### Nested FormGroups

```typescript
@Component({
  imports: [ReactiveFormsModule],
  template: `
    <form [formGroup]="form" (ngSubmit)="onSubmit()">
      <input formControlName="name" placeholder="Name" />
      
      <div formGroupName="address">
        <input formControlName="street" placeholder="Street" />
        <input formControlName="city" placeholder="City" />
        <input formControlName="zip" placeholder="ZIP" />
      </div>
      
      <button type="submit">Submit</button>
    </form>
  `,
})
export class Profile {
  private fb = inject(NonNullableFormBuilder);
  
  form = this.fb.group({
    name: ['', Validators.required],
    address: this.fb.group({
      street: [''],
      city: ['', Validators.required],
      zip: ['', [Validators.required, Validators.pattern(/^\d{5}$/)]],
    }),
  });
}
```

## Dynamic Forms with FormArray

```typescript
import { FormArray } from '@angular/forms';

@Component({
  imports: [ReactiveFormsModule],
  template: `
    <form [formGroup]="form">
      <div formArrayName="items">
        @for (item of items.controls; track $index; let i = $index) {
          <div [formGroupName]="i">
            <input formControlName="product" placeholder="Product" />
            <input formControlName="quantity" type="number" />
            <button type="button" (click)="removeItem(i)">Remove</button>
          </div>
        }
      </div>
      <button type="button" (click)="addItem()">Add Item</button>
    </form>
  `,
})
export class Order {
  private fb = inject(NonNullableFormBuilder);
  
  form = this.fb.group({
    items: this.fb.array([this.createItem()]),
  });
  
  get items() {
    return this.form.controls.items;
  }
  
  createItem() {
    return this.fb.group({
      product: ['', Validators.required],
      quantity: [1, [Validators.required, Validators.min(1)]],
    });
  }
  
  addItem() {
    this.items.push(this.createItem());
  }
  
  removeItem(index: number) {
    this.items.removeAt(index);
  }
}
```

## Custom Validators

### Sync Validator

```typescript
import { AbstractControl, ValidationErrors, ValidatorFn } from '@angular/forms';

export function forbiddenValue(forbidden: string): ValidatorFn {
  return (control: AbstractControl): ValidationErrors | null => {
    return control.value === forbidden 
      ? { forbiddenValue: { value: control.value } } 
      : null;
  };
}

// Usage
name: ['', [Validators.required, forbiddenValue('admin')]],
```

### Cross-Field Validator

```typescript
export function passwordMatch(): ValidatorFn {
  return (group: AbstractControl): ValidationErrors | null => {
    const password = group.get('password')?.value;
    const confirm = group.get('confirmPassword')?.value;
    return password === confirm ? null : { passwordMismatch: true };
  };
}

// Usage
form = this.fb.group({
  password: ['', [Validators.required, Validators.minLength(8)]],
  confirmPassword: ['', Validators.required],
}, { validators: passwordMatch() });
```

### Async Validator

```typescript
import { AsyncValidatorFn } from '@angular/forms';
import { map, catchError, of } from 'rxjs';

export function uniqueEmail(userService: User): AsyncValidatorFn {
  return (control: AbstractControl) => {
    return userService.checkEmail(control.value).pipe(
      map(exists => exists ? { emailTaken: true } : null),
      catchError(() => of(null))
    );
  };
}

// Usage
email: ['', 
  [Validators.required, Validators.email],  // sync validators
  [uniqueEmail(this.userService)]            // async validators
],
```

## Form State Management

### State Properties

```typescript
// Check states
form.valid      // All validations pass
form.invalid    // Has validation errors
form.pending    // Async validation in progress
form.dirty      // Value changed by user
form.pristine   // Value not changed
form.touched    // Control has been focused
form.untouched  // Control never focused

// Update values
form.setValue({ name: 'John', email: 'john@example.com' }); // Must include all
form.patchValue({ name: 'John' }); // Partial update

// Reset
form.reset();
form.reset({ name: 'Default' });

// Disable/Enable
form.disable();
form.enable();
form.controls.email.disable();

// Mark states
form.markAllAsTouched(); // Show all errors
form.markAsPristine();
form.markAsDirty();
```

### Value Changes Observable

```typescript
// Subscribe to value changes
form.valueChanges.subscribe(value => {
  console.log('Form value:', value);
});

// Single control with debounce
form.controls.email.valueChanges.pipe(
  debounceTime(300),
  distinctUntilChanged()
).subscribe(email => {
  this.validateEmail(email);
});

// Status changes
form.statusChanges.subscribe(status => {
  console.log('Form status:', status); // VALID, INVALID, PENDING
});
```

### Unified Events (Angular v18+)

```typescript
import { 
  ValueChangeEvent, StatusChangeEvent,
  PristineChangeEvent,TouchedChangeEvent,
  FormSubmittedEvent, FormResetEvent 
} from '@angular/forms';

form.events.subscribe(event => {
  if (event instanceof ValueChangeEvent) {
    console.log('Value changed:', event.value);
  }
  if (event instanceof StatusChangeEvent) {
    console.log('Status changed:', event.status);
  }
  if (event instanceof PristineChangeEvent) {
    console.log('Pristine changed:', event.pristine);
  }
  if (event instanceof TouchedChangeEvent) {
    console.log('Touched changed:', event.touched);
  }
  if (event instanceof FormSubmittedEvent) {
    console.log('Form submitted');
  }
  if (event instanceof FormResetEvent) {
    console.log('Form reset');
  }
});
```

## Error Display Pattern

```typescript
@Component({
  template: `
    <input formControlName="email" />
    
    @if (form.controls.email.invalid && form.controls.email.touched) {
      <div class="errors">
        @if (form.controls.email.errors?.['required']) {
          <span>Email is required</span>
        }
        @if (form.controls.email.errors?.['email']) {
          <span>Invalid email format</span>
        }
      </div>
    }
  `,
})
export class Form {
  // Helper for cleaner templates
  hasError(controlName: string, errorKey: string): boolean {
    const control = this.form.get(controlName);
    return control?.hasError(errorKey) && control?.touched || false;
  }
}
```

## Form Submission Pattern

```typescript
@Component({
  template: `
    <form [formGroup]="form" (ngSubmit)="onSubmit()">
      <!-- fields -->
      <button type="submit" [disabled]="form.invalid || isSubmitting">
        {{ isSubmitting ? 'Submitting...' : 'Submit' }}
      </button>
    </form>
  `,
})
export class Form {
  isSubmitting = false;
  
  async onSubmit() {
    if (this.form.invalid) {
      this.form.markAllAsTouched();
      return;
    }
    
    this.isSubmitting = true;
    try {
      await this.api.submit(this.form.getRawValue());
      this.form.reset();
    } catch (error) {
      // Handle error
    } finally {
      this.isSubmitting = false;
    }
  }
}
```
```

## File: `skills/angular-forms/references/formvalueControl-patterns.md`
```markdown
# Angular Signal Forms - ( FormValueControl )

## Table of Contents
- [Signal Form FormValueControl](#formValueControl)

## Signal Forms FormValueControl

``` typescript 

interface  Rating {
    rating : number
}

import { form, FormField, FormValueControl, ValidationError, WithOptionalField } from '@angular/forms/signals';
import { MatIconModule } from '@angular/material/icon';
import { MatError } from '@angular/material/form-field';


@Component({
  selector: 'app-rating',
  imports : [MatIconModule,MatError],
  template: `
    <div class="star-rating-container">
      @for (star of starArray(); track $index) {
        <mat-icon
          (click)="rate(star)"
          class="star-icon"
          [class.readonly]="readonly()"
          [class.error]="invalid()"
          [class]="{ filled: star <= value() }"
        >
          {{ getStarIcon(star) }}
        </mat-icon>
      }
      @if (errors().at(0)?.message) {
        <mat-error>
          {{ errors().at(0)?.message }}
        </mat-error>
      }
    </div>
  `,
  styles: ``,
})
export class Rating implements FormValueControl<number> {
  // Required: The value of the control, exposed as a two-way binding.
  readonly value = model<number>(0);
  // Optional: Bindings for other form control states.
  readonly readonly = input<boolean>(false);
  readonly invalid = input<boolean>(false);
  readonly errors: InputSignal<readonly WithOptionalField<ValidationError>[]> = input<
    readonly WithOptionalField<ValidationError>[]
  >([]);

  starArray: Signal<number[]> = signal(
    Array(5)
      .fill(0)
      .map((_, i) => i + 1),
  );

  getStarIcon(index: number): string {
    const floorRating = Math.floor(this.value()); 
    if (index <= floorRating) {
      return 'star'; // Full star
    }  else {
      return 'star_border'; // Empty star
    }
  }
  rate(index: number): void {
    if (!this.readonly()) {
      this.value.set(index);
    }
  }
}


import { FormField } from '@angular/forms/signals';

@Component({
  selector: 'app-signal-forms',
  imports : [FormField, Rating],
  template: `
   <form autocomplete="off" (submit)="submit($event)">
     <div class="form-field">
          <app-rating [formField]="ratingForm.rating">

          </app-rating>
          <!-- print to show the value updation -->
          {{ratingForm.rating().value()}}
        </div>
   </form>
  `,
  styles: ``,
})
export class SignalForms {
  readonly ratingModel = signal<Rating>({
    rating: 0,
  }); 

  readonly ratingForm = form(this.ratingModel)

  submit(event: Event): void {
    event.preventDefault();
    console.log(this.ratingForm.rating().value());
  }
}



```

```

## File: `skills/angular-http/SKILL.md`
```markdown
---
name: angular-http
description: Implement HTTP data fetching in Angular v20+ using resource(), httpResource(), and HttpClient. Use for API calls, data loading with signals, request/response handling, and interceptors. Triggers on data fetching, API integration, loading states, error handling, or converting Observable-based HTTP to signal-based patterns.
---

# Angular HTTP & Data Fetching

Fetch data in Angular using signal-based `resource()`, `httpResource()`, and the traditional `HttpClient`.

## httpResource() - Signal-Based HTTP

`httpResource()` wraps HttpClient with signal-based state management:

```typescript
import { Component, signal } from '@angular/core';
import { httpResource } from '@angular/common/http';

interface User {
  id: number;
  name: string;
  email: string;
}

@Component({
  selector: 'app-user-profile',
  template: `
    @if (userResource.isLoading()) {
      <p>Loading...</p>
    } @else if (userResource.error()) {
      <p>Error: {{ userResource.error()?.message }}</p>
      <button (click)="userResource.reload()">Retry</button>
    } @else if (userResource.hasValue()) {
      <h1>{{ userResource.value().name }}</h1>
      <p>{{ userResource.value().email }}</p>
    }
  `,
})
export class UserProfile {
  userId = signal('123');
  
  // Reactive HTTP resource - refetches when userId changes
  userResource = httpResource<User>(() => `/api/users/${this.userId()}`);
}
```

### httpResource Options

```typescript
// Simple GET request
userResource = httpResource<User>(() => `/api/users/${this.userId()}`);

// With full request options
userResource = httpResource<User>(() => ({
  url: `/api/users/${this.userId()}`,
  method: 'GET',
  headers: { 'Authorization': `Bearer ${this.token()}` },
  params: { include: 'profile' },
}));

// With default value
usersResource = httpResource<User[]>(() => '/api/users', {
  defaultValue: [],
});

// Skip request when params undefined
userResource = httpResource<User>(() => {
  const id = this.userId();
  return id ? `/api/users/${id}` : undefined;
});
```

### Resource State

```typescript
// Status signals
userResource.value()      // Current value or undefined
userResource.hasValue()   // Boolean - has resolved value
userResource.error()      // Error or undefined
userResource.isLoading()  // Boolean - currently loading
userResource.status()     // 'idle' | 'loading' | 'reloading' | 'resolved' | 'error' | 'local'

// Actions
userResource.reload()     // Manually trigger reload
userResource.set(value)   // Set local value
userResource.update(fn)   // Update local value
```

## resource() - Generic Async Data

For non-HTTP async operations or custom fetch logic:

```typescript
import { resource, signal } from '@angular/core';

@Component({...})
export class Search {
  query = signal('');
  
  searchResource = resource({
    // Reactive params - triggers reload when changed
    params: () => ({ q: this.query() }),
    
    // Async loader function
    loader: async ({ params, abortSignal }) => {
      if (!params.q) return [];
      
      const response = await fetch(`/api/search?q=${params.q}`, {
        signal: abortSignal,
      });
      return response.json() as Promise<SearchResult[]>;
    },
  });
}
```

### Resource with Default Value

```typescript
todosResource = resource({
  defaultValue: [] as Todo[],
  params: () => ({ filter: this.filter() }),
  loader: async ({ params }) => {
    const res = await fetch(`/api/todos?filter=${params.filter}`);
    return res.json();
  },
});

// value() returns Todo[] (never undefined)
```

### Conditional Loading

```typescript
const userId = signal<string | null>(null);

userResource = resource({
  params: () => {
    const id = userId();
    // Return undefined to skip loading
    return id ? { id } : undefined;
  },
  loader: async ({ params }) => {
    return fetch(`/api/users/${params.id}`).then(r => r.json());
  },
});
// Status is 'idle' when params returns undefined
```

## HttpClient - Traditional Approach

For complex scenarios or when you need Observable operators:

```typescript
import { Component, inject } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { toSignal } from '@angular/core/rxjs-interop';

@Component({...})
export class Users {
  private http = inject(HttpClient);
  
  // Convert Observable to Signal
  users = toSignal(
    this.http.get<User[]>('/api/users'),
    { initialValue: [] }
  );
  
  // Or use Observable directly
  users$ = this.http.get<User[]>('/api/users');
}
```

### HTTP Methods

```typescript
private http = inject(HttpClient);

// GET
getUser(id: string) {
  return this.http.get<User>(`/api/users/${id}`);
}

// POST
createUser(user: CreateUserDto) {
  return this.http.post<User>('/api/users', user);
}

// PUT
updateUser(id: string, user: UpdateUserDto) {
  return this.http.put<User>(`/api/users/${id}`, user);
}

// PATCH
patchUser(id: string, changes: Partial<User>) {
  return this.http.patch<User>(`/api/users/${id}`, changes);
}

// DELETE
deleteUser(id: string) {
  return this.http.delete<void>(`/api/users/${id}`);
}
```

### Request Options

```typescript
this.http.get<User[]>('/api/users', {
  headers: {
    'Authorization': 'Bearer token',
    'Content-Type': 'application/json',
  },
  params: {
    page: '1',
    limit: '10',
    sort: 'name',
  },
  observe: 'response', // Get full HttpResponse
  responseType: 'json',
});
```

## Interceptors

### Functional Interceptor (Recommended)

```typescript
// auth.interceptor.ts
import { HttpInterceptorFn } from '@angular/common/http';
import { inject } from '@angular/core';

export const authInterceptor: HttpInterceptorFn = (req, next) => {
  const authService = inject(Auth);
  const token = authService.token();
  
  if (token) {
    req = req.clone({
      setHeaders: { Authorization: `Bearer ${token}` },
    });
  }
  
  return next(req);
};

// error.interceptor.ts
export const errorInterceptor: HttpInterceptorFn = (req, next) => {
  return next(req).pipe(
    catchError((error: HttpErrorResponse) => {
      if (error.status === 401) {
        inject(Router).navigate(['/login']);
      }
      return throwError(() => error);
    })
  );
};

// logging.interceptor.ts
export const loggingInterceptor: HttpInterceptorFn = (req, next) => {
  const started = Date.now();
  return next(req).pipe(
    tap({
      next: () => console.log(`${req.method} ${req.url} - ${Date.now() - started}ms`),
      error: (err) => console.error(`${req.method} ${req.url} failed`, err),
    })
  );
};
```

### Register Interceptors

```typescript
// app.config.ts
import { provideHttpClient, withInterceptors } from '@angular/common/http';

export const appConfig: ApplicationConfig = {
  providers: [
    provideHttpClient(
      withInterceptors([
        authInterceptor,
        errorInterceptor,
        loggingInterceptor,
      ])
    ),
  ],
};
```

## Error Handling

### With httpResource

```typescript
@Component({
  template: `
    @if (userResource.error(); as error) {
      <div class="error">
        <p>{{ getErrorMessage(error) }}</p>
        <button (click)="userResource.reload()">Retry</button>
      </div>
    }
  `,
})
export class UserCmpt {
  userResource = httpResource<User>(() => `/api/users/${this.userId()}`);
  
  getErrorMessage(error: unknown): string {
    if (error instanceof HttpErrorResponse) {
      return error.error?.message || `Error ${error.status}: ${error.statusText}`;
    }
    return 'An unexpected error occurred';
  }
}
```

### With HttpClient

```typescript
import { catchError, retry } from 'rxjs';

getUser(id: string) {
  return this.http.get<User>(`/api/users/${id}`).pipe(
    retry(2), // Retry up to 2 times
    catchError((error: HttpErrorResponse) => {
      console.error('Error fetching user:', error);
      return throwError(() => new Error('Failed to load user'));
    })
  );
}
```

## Loading States Pattern

```typescript
@Component({
  template: `
    @switch (dataResource.status()) {
      @case ('idle') {
        <p>Enter a search term</p>
      }
      @case ('loading') {
        <app-spinner />
      }
      @case ('reloading') {
        <app-data [data]="dataResource.value()" />
        <app-spinner size="small" />
      }
      @case ('resolved') {
        <app-data [data]="dataResource.value()" />
      }
      @case ('error') {
        <app-error 
          [error]="dataResource.error()" 
          (retry)="dataResource.reload()" 
        />
      }
    }
  `,
})
export class Data {
  query = signal('');
  dataResource = httpResource<Data[]>(() => 
    this.query() ? `/api/search?q=${this.query()}` : undefined
  );
}
```

For advanced patterns, see [references/http-patterns.md](references/http-patterns.md).
```

## File: `skills/angular-http/references/http-patterns.md`
```markdown
# Angular HTTP Patterns

## Table of Contents
- [Service Layer Pattern](#service-layer-pattern)
- [Caching Strategies](#caching-strategies)
- [Pagination](#pagination)
- [File Upload](#file-upload)
- [Request Cancellation](#request-cancellation)
- [Testing HTTP](#testing-http)

## Service Layer Pattern

Encapsulate HTTP logic in services:

```typescript
import { Injectable, inject, signal, computed } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { httpResource } from '@angular/common/http';

export interface User {
  id: string;
  name: string;
  email: string;
}

@Injectable({ providedIn: 'root' })
export class User {
  private http = inject(HttpClient);
  private baseUrl = '/api/users';
  
  // Current user ID for reactive fetching
  private currentUserId = signal<string | null>(null);
  
  // Reactive resource that updates when currentUserId changes
  currentUser = httpResource<User>(() => {
    const id = this.currentUserId();
    return id ? `${this.baseUrl}/${id}` : undefined;
  });
  
  // Set current user to fetch
  selectUser(id: string) {
    this.currentUserId.set(id);
  }
  
  // CRUD operations
  getAll() {
    return this.http.get<User[]>(this.baseUrl);
  }
  
  getById(id: string) {
    return this.http.get<User>(`${this.baseUrl}/${id}`);
  }
  
  create(user: Omit<User, 'id'>) {
    return this.http.post<User>(this.baseUrl, user);
  }
  
  update(id: string, user: Partial<User>) {
    return this.http.patch<User>(`${this.baseUrl}/${id}`, user);
  }
  
  delete(id: string) {
    return this.http.delete<void>(`${this.baseUrl}/${id}`);
  }
}
```

## Caching Strategies

### Simple In-Memory Cache

```typescript
@Injectable({ providedIn: 'root' })
export class CachedUser {
  private http = inject(HttpClient);
  private cache = new Map<string, { data: User; timestamp: number }>();
  private cacheDuration = 5 * 60 * 1000; // 5 minutes
  
  getUser(id: string): Observable<User> {
    const cached = this.cache.get(id);
    
    if (cached && Date.now() - cached.timestamp < this.cacheDuration) {
      return of(cached.data);
    }
    
    return this.http.get<User>(`/api/users/${id}`).pipe(
      tap(user => {
        this.cache.set(id, { data: user, timestamp: Date.now() });
      })
    );
  }
  
  invalidateCache(id?: string) {
    if (id) {
      this.cache.delete(id);
    } else {
      this.cache.clear();
    }
  }
}
```

### Signal-Based Cache

```typescript
@Injectable({ providedIn: 'root' })
export class UserCache {
  private http = inject(HttpClient);
  
  // Cache as signal
  private usersCache = signal<Map<string, User>>(new Map());
  
  // Computed for easy access
  users = computed(() => Array.from(this.usersCache().values()));
  
  getUser(id: string): User | undefined {
    return this.usersCache().get(id);
  }
  
  async fetchUser(id: string): Promise<User> {
    const cached = this.getUser(id);
    if (cached) return cached;
    
    const user = await firstValueFrom(
      this.http.get<User>(`/api/users/${id}`)
    );
    
    this.usersCache.update(cache => {
      const newCache = new Map(cache);
      newCache.set(id, user);
      return newCache;
    });
    
    return user;
  }
}
```

## Pagination

### Paginated Resource

```typescript
interface PaginatedResponse<T> {
  data: T[];
  total: number;
  page: number;
  pageSize: number;
  totalPages: number;
}

@Component({
  template: `
    @if (usersResource.isLoading()) {
      <app-spinner />
    } @else if (usersResource.hasValue()) {
      <ul>
        @for (user of usersResource.value().data; track user.id) {
          <li>{{ user.name }}</li>
        }
      </ul>
      
      <div class="pagination">
        <button 
          (click)="prevPage()" 
          [disabled]="page() === 1"
        >Previous</button>
        
        <span>Page {{ page() }} of {{ usersResource.value().totalPages }}</span>
        
        <button 
          (click)="nextPage()" 
          [disabled]="page() >= usersResource.value().totalPages"
        >Next</button>
      </div>
    }
  `,
})
export class UsersList {
  page = signal(1);
  pageSize = signal(10);
  
  usersResource = httpResource<PaginatedResponse<User>>(() => ({
    url: '/api/users',
    params: {
      page: this.page().toString(),
      pageSize: this.pageSize().toString(),
    },
  }));
  
  nextPage() {
    this.page.update(p => p + 1);
  }
  
  prevPage() {
    this.page.update(p => Math.max(1, p - 1));
  }
}
```

### Infinite Scroll

```typescript
@Component({
  template: `
    <ul>
      @for (user of allUsers(); track user.id) {
        <li>{{ user.name }}</li>
      }
    </ul>
    
    @if (isLoading()) {
      <app-spinner />
    }
    
    @if (hasMore()) {
      <button (click)="loadMore()">Load More</button>
    }
  `,
})
export class InfiniteUsers {
  private http = inject(HttpClient);
  
  private page = signal(1);
  private users = signal<User[]>([]);
  private totalPages = signal(1);
  
  allUsers = this.users.asReadonly();
  isLoading = signal(false);
  hasMore = computed(() => this.page() < this.totalPages());
  
  constructor() {
    this.loadPage(1);
  }
  
  loadMore() {
    this.loadPage(this.page() + 1);
  }
  
  private async loadPage(page: number) {
    this.isLoading.set(true);
    
    try {
      const response = await firstValueFrom(
        this.http.get<PaginatedResponse<User>>('/api/users', {
          params: { page: page.toString(), pageSize: '20' },
        })
      );
      
      this.users.update(users => [...users, ...response.data]);
      this.page.set(page);
      this.totalPages.set(response.totalPages);
    } finally {
      this.isLoading.set(false);
    }
  }
}
```

## File Upload

### Single File Upload

```typescript
@Component({
  template: `
    <input type="file" (change)="onFileSelected($event)" />
    
    @if (uploadProgress() !== null) {
      <progress [value]="uploadProgress()" max="100"></progress>
    }
  `,
})
export class FileUpload {
  private http = inject(HttpClient);
  
  uploadProgress = signal<number | null>(null);
  
  onFileSelected(event: Event) {
    const file = (event.target as HTMLInputElement).files?.[0];
    if (!file) return;
    
    const formData = new FormData();
    formData.append('file', file);
    
    this.http.post('/api/upload', formData, {
      reportProgress: true,
      observe: 'events',
    }).subscribe(event => {
      if (event.type === HttpEventType.UploadProgress && event.total) {
        this.uploadProgress.set(Math.round(100 * event.loaded / event.total));
      } else if (event.type === HttpEventType.Response) {
        this.uploadProgress.set(null);
        console.log('Upload complete:', event.body);
      }
    });
  }
}
```

### Multiple Files

```typescript
uploadFiles(files: FileList) {
  const formData = new FormData();
  
  for (let i = 0; i < files.length; i++) {
    formData.append('files', files[i]);
  }
  
  return this.http.post<{ urls: string[] }>('/api/upload-multiple', formData);
}
```

## Request Cancellation

### With resource()

```typescript
// resource() automatically handles cancellation via abortSignal
searchResource = resource({
  params: () => ({ q: this.query() }),
  loader: async ({ params, abortSignal }) => {
    const response = await fetch(`/api/search?q=${params.q}`, {
      signal: abortSignal, // Cancels if params change
    });
    return response.json();
  },
});
```

### With HttpClient

```typescript
@Component({...})
export class Search implements OnDestroy {
  private http = inject(HttpClient);
  private destroyRef = inject(DestroyRef);
  
  query = signal('');
  results = signal<Result[]>([]);
  
  private searchSubscription?: Subscription;
  
  search() {
    // Cancel previous request
    this.searchSubscription?.unsubscribe();
    
    this.searchSubscription = this.http
      .get<Result[]>(`/api/search?q=${this.query()}`)
      .pipe(takeUntilDestroyed(this.destroyRef))
      .subscribe(results => this.results.set(results));
  }
}
```

### Debounced Search

```typescript
@Component({...})
export class SearchDebounced {
  query = signal('');
  
  private http = inject(HttpClient);
  
  results = toSignal(
    toObservable(this.query).pipe(
      debounceTime(300),
      distinctUntilChanged(),
      filter(q => q.length >= 2),
      switchMap(q => this.http.get<Result[]>(`/api/search?q=${q}`)),
      catchError(() => of([]))
    ),
    { initialValue: [] }
  );
}
```

## Testing HTTP

### Testing httpResource

```typescript
describe('UserCmpt', () => {
  let component: UserCmpt;
  let httpMock: HttpTestingController;
  
  beforeEach(() => {
    TestBed.configureTestingModule({
      imports: [UserCmpt],
      providers: [provideHttpClientTesting()],
    });
    
    component = TestBed.createComponent(UserCmpt).componentInstance;
    httpMock = TestBed.inject(HttpTestingController);
  });
  
  it('should load user', () => {
    component.userId.set('123');
    
    const req = httpMock.expectOne('/api/users/123');
    req.flush({ id: '123', name: 'Test User' });
    
    expect(component.userResource.value()?.name).toBe('Test User');
  });
  
  afterEach(() => {
    httpMock.verify();
  });
});
```

### Testing Services

```typescript
describe('User', () => {
  let service: User;
  let httpMock: HttpTestingController;
  
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [
        User,
        provideHttpClient(),
        provideHttpClientTesting(),
      ],
    });
    
    service = TestBed.inject(User);
    httpMock = TestBed.inject(HttpTestingController);
  });
  
  it('should create user', () => {
    const newUser = { name: 'Test', email: 'test@example.com' };
    
    service.create(newUser).subscribe(user => {
      expect(user.id).toBeDefined();
      expect(user.name).toBe('Test');
    });
    
    const req = httpMock.expectOne('/api/users');
    expect(req.request.method).toBe('POST');
    expect(req.request.body).toEqual(newUser);
    
    req.flush({ id: '1', ...newUser });
  });
});
```
```

## File: `skills/angular-routing/SKILL.md`
```markdown
---
name: angular-routing
description: Implement routing in Angular v20+ applications with lazy loading, functional guards, resolvers, and route parameters. Use for navigation setup, protected routes, route-based data loading, and nested routing. Triggers on route configuration, adding authentication guards, implementing lazy loading, or reading route parameters with signals.
---

# Angular Routing

Configure routing in Angular v20+ with lazy loading, functional guards, and signal-based route parameters.

## Basic Setup

```typescript
// app.routes.ts
import { Routes } from '@angular/router';

export const routes: Routes = [
  { path: '', redirectTo: '/home', pathMatch: 'full' },
  { path: 'home', component: Home },
  { path: 'about', component: About },
  { path: '**', component: NotFound },
];

// app.config.ts
import { ApplicationConfig } from '@angular/core';
import { provideRouter } from '@angular/router';
import { routes } from './app.routes';

export const appConfig: ApplicationConfig = {
  providers: [
    provideRouter(routes),
  ],
};

// app.component.ts
import { Component } from '@angular/core';
import { RouterOutlet, RouterLink, RouterLinkActive } from '@angular/router';

@Component({
  selector: 'app-root',
  imports: [RouterOutlet, RouterLink, RouterLinkActive],
  template: `
    <nav>
      <a routerLink="/home" routerLinkActive="active">Home</a>
      <a routerLink="/about" routerLinkActive="active">About</a>
    </nav>
    <router-outlet />
  `,
})
export class App {}
```

## Lazy Loading

Load feature modules on demand:

```typescript
// app.routes.ts
export const routes: Routes = [
  { path: '', redirectTo: '/home', pathMatch: 'full' },
  { path: 'home', component: Home },
  
  // Lazy load entire feature
  {
    path: 'admin',
    loadChildren: () => import('./admin/admin.routes').then(m => m.adminRoutes),
  },
  
  // Lazy load single component
  {
    path: 'settings',
    loadComponent: () => import('./settings/settings.component').then(m => m.Settings),
  },
];

// admin/admin.routes.ts
export const adminRoutes: Routes = [
  { path: '', component: AdminDashboard },
  { path: 'users', component: AdminUsers },
  { path: 'settings', component: AdminSettings },
];
```

## Route Parameters

### With Signal Inputs (Recommended)

```typescript
// Route config
{ path: 'users/:id', component: UserDetail }

// Component - use input() for route params
import { Component, input, computed } from '@angular/core';

@Component({
  selector: 'app-user-detail',
  template: `
    <h1>User {{ id() }}</h1>
  `,
})
export class UserDetail {
  // Route param as signal input
  id = input.required<string>();
  
  // Computed based on route param
  userId = computed(() => parseInt(this.id(), 10));
}
```

Enable with `withComponentInputBinding()`:

```typescript
// app.config.ts
import { provideRouter, withComponentInputBinding } from '@angular/router';

export const appConfig: ApplicationConfig = {
  providers: [
    provideRouter(routes, withComponentInputBinding()),
  ],
};
```

### Query Parameters

```typescript
// Route: /search?q=angular&page=1

@Component({...})
export class Search {
  // Query params as inputs
  q = input<string>('');
  page = input<string>('1');
  
  currentPage = computed(() => parseInt(this.page(), 10));
}
```

### With ActivatedRoute (Alternative)

```typescript
import { Component, inject } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { toSignal } from '@angular/core/rxjs-interop';
import { map } from 'rxjs';

@Component({...})
export class UserDetail {
  private route = inject(ActivatedRoute);
  
  // Convert route params to signal
  id = toSignal(
    this.route.paramMap.pipe(map(params => params.get('id'))),
    { initialValue: null }
  );
  
  // Query params
  query = toSignal(
    this.route.queryParamMap.pipe(map(params => params.get('q'))),
    { initialValue: '' }
  );
}
```

## Functional Guards

### Auth Guard

```typescript
// guards/auth.guard.ts
import { inject } from '@angular/core';
import { CanActivateFn, Router } from '@angular/router';

export const authGuard: CanActivateFn = (route, state) => {
  const authService = inject(Auth);
  const router = inject(Router);
  
  if (authService.isAuthenticated()) {
    return true;
  }
  
  // Redirect to login with return URL
  return router.createUrlTree(['/login'], {
    queryParams: { returnUrl: state.url },
  });
};

// Usage in routes
{
  path: 'dashboard',
  component: Dashboard,
  canActivate: [authGuard],
}
```

### Role Guard

```typescript
export const roleGuard = (allowedRoles: string[]): CanActivateFn => {
  return (route, state) => {
    const authService = inject(Auth);
    const router = inject(Router);
    
    const userRole = authService.currentUser()?.role;
    
    if (userRole && allowedRoles.includes(userRole)) {
      return true;
    }
    
    return router.createUrlTree(['/unauthorized']);
  };
};

// Usage
{
  path: 'admin',
  component: Admin,
  canActivate: [authGuard, roleGuard(['admin', 'superadmin'])],
}
```

### Can Deactivate Guard

```typescript
export interface CanDeactivate {
  canDeactivate: () => boolean | Promise<boolean>;
}

export const unsavedChangesGuard: CanDeactivateFn<CanDeactivate> = (component) => {
  if (component.canDeactivate()) {
    return true;
  }
  
  return confirm('You have unsaved changes. Leave anyway?');
};

// Component implementation
@Component({...})
export class Edit implements CanDeactivate {
  form = inject(FormBuilder).group({...});
  
  canDeactivate(): boolean {
    return !this.form.dirty;
  }
}

// Route
{
  path: 'edit/:id',
  component: Edit,
  canDeactivate: [unsavedChangesGuard],
}
```

## Resolvers

Pre-fetch data before route activation:

```typescript
// resolvers/user.resolver.ts
import { inject } from '@angular/core';
import { ResolveFn } from '@angular/router';

export const userResolver: ResolveFn<User> = (route) => {
  const userService = inject(User);
  const id = route.paramMap.get('id')!;
  return userService.getById(id);
};

// Route config
{
  path: 'users/:id',
  component: UserDetail,
  resolve: { user: userResolver },
}

// Component - access resolved data via input
@Component({...})
export class UserDetail {
  user = input.required<User>();
}
```

## Nested Routes

```typescript
// Parent route with children
export const routes: Routes = [
  {
    path: 'products',
    component: ProductsLayout,
    children: [
      { path: '', component: ProductList },
      { path: ':id', component: ProductDetail },
      { path: ':id/edit', component: ProductEdit },
    ],
  },
];

// ProductsLayout
@Component({
  imports: [RouterOutlet],
  template: `
    <h1>Products</h1>
    <router-outlet /> <!-- Child routes render here -->
  `,
})
export class ProductsLayout {}
```

## Programmatic Navigation

```typescript
import { Component, inject } from '@angular/core';
import { Router } from '@angular/router';

@Component({...})
export class Product {
  private router = inject(Router);
  
  // Navigate to route
  goToProducts() {
    this.router.navigate(['/products']);
  }
  
  // Navigate with params
  goToProduct(id: string) {
    this.router.navigate(['/products', id]);
  }
  
  // Navigate with query params
  search(query: string) {
    this.router.navigate(['/search'], {
      queryParams: { q: query, page: 1 },
    });
  }
  
  // Navigate relative to current route
  goToEdit() {
    this.router.navigate(['edit'], { relativeTo: this.route });
  }
  
  // Replace current history entry
  replaceUrl() {
    this.router.navigate(['/new-page'], { replaceUrl: true });
  }
}
```

## Route Data

```typescript
// Static route data
{
  path: 'admin',
  component: Admin,
  data: {
    title: 'Admin Dashboard',
    roles: ['admin'],
  },
}

// Access in component
@Component({...})
export class AdminCmpt {
  title = input<string>(); // From route data
  roles = input<string[]>(); // From route data
}

// Or via ActivatedRoute
private route = inject(ActivatedRoute);
data = toSignal(this.route.data);
```

## Router Events

```typescript
import { Router, NavigationStart, NavigationEnd } from '@angular/router';
import { filter } from 'rxjs';

@Component({...})
export class AppMain {
  private router = inject(Router);
  
  isNavigating = signal(false);
  
  constructor() {
    this.router.events.pipe(
      filter(e => e instanceof NavigationStart || e instanceof NavigationEnd)
    ).subscribe(event => {
      this.isNavigating.set(event instanceof NavigationStart);
    });
  }
}
```

For advanced patterns, see [references/routing-patterns.md](routing-patterns.md).
```

## File: `skills/angular-routing/references/routing-patterns.md`
```markdown
# Angular Routing Patterns

## Table of Contents
- [Route Configuration Options](#route-configuration-options)
- [Authentication Flow](#authentication-flow)
- [Breadcrumbs](#breadcrumbs)
- [Tab Navigation](#tab-navigation)
- [Modal Routes](#modal-routes)
- [Preloading Strategies](#preloading-strategies)

## Route Configuration Options

### Full Route Options

```typescript
{
  path: 'users/:id',
  component: UserCmpt,
  
  // Lazy loading alternatives
  loadComponent: () => import('./user.component').then(m => m.UserCmpt),
  loadChildren: () => import('./user.routes').then(m => m.userRoutes),
  
  // Guards
  canActivate: [authGuard],
  canActivateChild: [authGuard],
  canDeactivate: [unsavedChangesGuard],
  canMatch: [featureFlagGuard],
  
  // Data
  resolve: { user: userResolver },
  data: { title: 'User Profile', animation: 'userPage' },
  
  // Children
  children: [...],
  
  // Outlet
  outlet: 'sidebar',
  
  // Path matching
  pathMatch: 'full', // or 'prefix'
  
  // Title
  title: 'User Profile',
  // Or dynamic title
  title: userTitleResolver,
}
```

### Dynamic Title Resolver

```typescript
export const userTitleResolver: ResolveFn<string> = (route) => {
  const userService = inject(User);
  const id = route.paramMap.get('id')!;
  return userService.getById(id).pipe(
    map(user => `${user.name} - Profile`)
  );
};
```

## Authentication Flow

### Complete Auth Setup

```typescript
// auth.service.ts
@Injectable({ providedIn: 'root' })
export class Auth {
  private _user = signal<User | null>(null);
  private _token = signal<string | null>(null);
  
  readonly user = this._user.asReadonly();
  readonly isAuthenticated = computed(() => this._user() !== null);
  
  private router = inject(Router);
  private http = inject(HttpClient);
  
  async login(credentials: Credentials): Promise<boolean> {
    try {
      const response = await firstValueFrom(
        this.http.post<AuthResponse>('/api/login', credentials)
      );
      
      this._token.set(response.token);
      this._user.set(response.user);
      localStorage.setItem('token', response.token);
      
      return true;
    } catch {
      return false;
    }
  }
  
  logout(): void {
    this._user.set(null);
    this._token.set(null);
    localStorage.removeItem('token');
    this.router.navigate(['/login']);
  }
  
  async checkAuth(): Promise<boolean> {
    const token = localStorage.getItem('token');
    if (!token) return false;
    
    try {
      const user = await firstValueFrom(
        this.http.get<User>('/api/me')
      );
      this._user.set(user);
      this._token.set(token);
      return true;
    } catch {
      localStorage.removeItem('token');
      return false;
    }
  }
}

// auth.guard.ts
export const authGuard: CanActivateFn = async (route, state) => {
  const authService = inject(Auth);
  const router = inject(Router);
  
  // Check if already authenticated
  if (authService.isAuthenticated()) {
    return true;
  }
  
  // Try to restore session
  const isValid = await authService.checkAuth();
  if (isValid) {
    return true;
  }
  
  // Redirect to login
  return router.createUrlTree(['/login'], {
    queryParams: { returnUrl: state.url },
  });
};

// login.component.ts
@Component({
  template: `
    <form (ngSubmit)="login()">
      <input [(ngModel)]="email" name="email" />
      <input [(ngModel)]="password" name="password" type="password" />
      <button type="submit">Login</button>
    </form>
  `,
})
export class Login {
  private authService = inject(Auth);
  private router = inject(Router);
  private route = inject(ActivatedRoute);
  
  email = '';
  password = '';
  
  async login() {
    const success = await this.authService.login({
      email: this.email,
      password: this.password,
    });
    
    if (success) {
      const returnUrl = this.route.snapshot.queryParams['returnUrl'] || '/';
      this.router.navigateByUrl(returnUrl);
    }
  }
}
```

## Breadcrumbs

```typescript
// breadcrumb.service.ts
@Injectable({ providedIn: 'root' })
export class Breadcrumb {
  private router = inject(Router);
  private route = inject(ActivatedRoute);
  
  breadcrumbs = toSignal(
    this.router.events.pipe(
      filter(event => event instanceof NavigationEnd),
      map(() => this.buildBreadcrumbs(this.route.root))
    ),
    { initialValue: [] }
  );
  
  private buildBreadcrumbs(
    route: ActivatedRoute,
    url: string = '',
    breadcrumbs: Breadcrumb[] = []
  ): Breadcrumb[] {
    const children = route.children;
    
    if (children.length === 0) {
      return breadcrumbs;
    }
    
    for (const child of children) {
      const routeUrl = child.snapshot.url
        .map(segment => segment.path)
        .join('/');
      
      if (routeUrl) {
        url += `/${routeUrl}`;
      }
      
      const label = child.snapshot.data['breadcrumb'];
      if (label) {
        breadcrumbs.push({ label, url });
      }
      
      return this.buildBreadcrumbs(child, url, breadcrumbs);
    }
    
    return breadcrumbs;
  }
}

// Route config with breadcrumb data
export const routes: Routes = [
  {
    path: 'products',
    data: { breadcrumb: 'Products' },
    children: [
      { path: '', component: ProductList },
      {
        path: ':id',
        data: { breadcrumb: 'Product Details' },
        component: ProductDetail,
      },
    ],
  },
];

// breadcrumb.component.ts
@Component({
  selector: 'app-breadcrumb',
  template: `
    <nav aria-label="Breadcrumb">
      <ol>
        <li><a routerLink="/">Home</a></li>
        @for (crumb of breadcrumbService.breadcrumbs(); track crumb.url) {
          <li>
            <a [routerLink]="crumb.url">{{ crumb.label }}</a>
          </li>
        }
      </ol>
    </nav>
  `,
})
export class BreadcrumbCmpt {
  breadcrumbService = inject(Breadcrumb);
}
```

## Tab Navigation

```typescript
// tabs-layout.component.ts
@Component({
  imports: [RouterOutlet, RouterLink, RouterLinkActive],
  template: `
    <div class="tabs">
      @for (tab of tabs; track tab.path) {
        <a 
          [routerLink]="tab.path" 
          routerLinkActive="active"
          [routerLinkActiveOptions]="{ exact: tab.exact }"
        >
          {{ tab.label }}
        </a>
      }
    </div>
    <div class="tab-content">
      <router-outlet />
    </div>
  `,
})
export class TabsLayout {
  tabs = [
    { path: './', label: 'Overview', exact: true },
    { path: 'details', label: 'Details', exact: false },
    { path: 'settings', label: 'Settings', exact: false },
  ];
}

// Routes
{
  path: 'account',
  component: TabsLayout,
  children: [
    { path: '', component: AccountOverview },
    { path: 'details', component: AccountDetails },
    { path: 'settings', component: AccountSettings },
  ],
}
```

## Modal Routes

Using auxiliary outlets for modals:

```typescript
// Routes
export const routes: Routes = [
  { path: 'products', component: ProductList },
  { path: 'product-modal/:id', component: ProductModal, outlet: 'modal' },
];

// App template
@Component({
  template: `
    <router-outlet />
    <router-outlet name="modal" />
  `,
})
export class App {}

// Open modal
this.router.navigate([{ outlets: { modal: ['product-modal', productId] } }]);

// Close modal
this.router.navigate([{ outlets: { modal: null } }]);

// Link to open modal
<a [routerLink]="[{ outlets: { modal: ['product-modal', product.id] } }]">
  View Details
</a>
```

## Preloading Strategies

### Built-in Strategies

```typescript
import { 
  provideRouter, 
  withPreloading,
  PreloadAllModules,
  NoPreloading 
} from '@angular/router';

// Preload all lazy modules
provideRouter(routes, withPreloading(PreloadAllModules))

// No preloading (default)
provideRouter(routes, withPreloading(NoPreloading))
```

### Custom Preloading Strategy

```typescript
// selective-preload.strategy.ts
@Injectable({ providedIn: 'root' })
export class SelectivePreloadStrategy implements PreloadingStrategy {
  preload(route: Route, load: () => Observable<any>): Observable<any> {
    // Only preload routes marked with data.preload = true
    if (route.data?.['preload']) {
      return load();
    }
    return of(null);
  }
}

// Routes
{
  path: 'dashboard',
  loadComponent: () => import('./dashboard.component'),
  data: { preload: true }, // Will be preloaded
}

// Config
provideRouter(routes, withPreloading(SelectivePreloadStrategy))
```

### Network-Aware Preloading

```typescript
@Injectable({ providedIn: 'root' })
export class NetworkAwarePreloadStrategy implements PreloadingStrategy {
  preload(route: Route, load: () => Observable<any>): Observable<any> {
    // Check network conditions
    const connection = (navigator as any).connection;
    
    if (connection) {
      // Don't preload on slow connections
      if (connection.saveData || connection.effectiveType === '2g') {
        return of(null);
      }
    }
    
    // Preload if marked
    if (route.data?.['preload']) {
      return load();
    }
    
    return of(null);
  }
}
```

## Route Animations

```typescript
// app.routes.ts
export const routes: Routes = [
  { path: 'home', component: Home, data: { animation: 'HomePage' } },
  { path: 'about', component: About, data: { animation: 'AboutPage' } },
];

// app.component.ts
@Component({
  imports: [RouterOutlet],
  template: `
    <div [@routeAnimations]="getRouteAnimationData()">
      <router-outlet />
    </div>
  `,
  animations: [
    trigger('routeAnimations', [
      transition('HomePage <=> AboutPage', [
        style({ position: 'relative' }),
        query(':enter, :leave', [
          style({
            position: 'absolute',
            top: 0,
            left: 0,
            width: '100%',
          }),
        ]),
        query(':enter', [style({ left: '-100%' })]),
        query(':leave', animateChild()),
        group([
          query(':leave', [animate('300ms ease-out', style({ left: '100%' }))]),
          query(':enter', [animate('300ms ease-out', style({ left: '0%' }))]),
        ]),
      ]),
    ]),
  ],
})
export class AppMain {
  getRouteAnimationData() {
    return this.route.firstChild?.snapshot.data['animation'];
  }
}
```

## Scroll Position Restoration

```typescript
// app.config.ts
import { 
  provideRouter, 
  withInMemoryScrolling,
  withRouterConfig 
} from '@angular/router';

provideRouter(
  routes,
  withInMemoryScrolling({
    scrollPositionRestoration: 'enabled', // or 'top'
    anchorScrolling: 'enabled',
  }),
  withRouterConfig({
    onSameUrlNavigation: 'reload',
  })
)
```
```

## File: `skills/angular-signals/SKILL.md`
```markdown
---
name: angular-signals
description: Implement signal-based reactive state management in Angular v20+. Use for creating reactive state with signal(), derived state with computed(), dependent state with linkedSignal(), and side effects with effect(). Triggers on state management questions, converting from BehaviorSubject/Observable patterns to signals, or implementing reactive data flows.
---

# Angular Signals

Signals are Angular's reactive primitive for state management. They provide synchronous, fine-grained reactivity.

## Core Signal APIs

### signal() - Writable State

```typescript
import { signal } from '@angular/core';

// Create writable signal
const count = signal(0);

// Read value
console.log(count()); // 0

// Set new value
count.set(5);

// Update based on current value
count.update(c => c + 1);

// With explicit type
const user = signal<User | null>(null);
user.set({ id: 1, name: 'Alice' });
```

### computed() - Derived State

```typescript
import { signal, computed } from '@angular/core';

const firstName = signal('John');
const lastName = signal('Doe');

// Derived signal - automatically updates when dependencies change
const fullName = computed(() => `${firstName()} ${lastName()}`);

console.log(fullName()); // "John Doe"
firstName.set('Jane');
console.log(fullName()); // "Jane Doe"

// Computed with complex logic
const items = signal<Item[]>([]);
const filter = signal('');

const filteredItems = computed(() => {
  const query = filter().toLowerCase();
  return items().filter(item => 
    item.name.toLowerCase().includes(query)
  );
});

const totalPrice = computed(() => 
  filteredItems().reduce((sum, item) => sum + item.price, 0)
);
```

### linkedSignal() - Dependent State with Reset

```typescript
import { signal, linkedSignal } from '@angular/core';

const options = signal(['A', 'B', 'C']);

// Resets to first option when options change
const selected = linkedSignal(() => options()[0]);

console.log(selected()); // "A"
selected.set('B');       // User selects B
console.log(selected()); // "B"
options.set(['X', 'Y']); // Options change
console.log(selected()); // "X" - auto-reset to first

// With previous value access
const items = signal<Item[]>([]);

const selectedItem = linkedSignal<Item[], Item | null>({
  source: () => items(),
  computation: (newItems, previous) => {
    // Try to preserve selection if item still exists
    const prevItem = previous?.value;
    if (prevItem && newItems.some(i => i.id === prevItem.id)) {
      return prevItem;
    }
    return newItems[0] ?? null;
  },
});
```

### effect() - Side Effects

```typescript
import { signal, effect, inject, DestroyRef } from '@angular/core';

@Component({...})
export class Search {
  query = signal('');
  
  constructor() {
    // Effect runs when query changes
    effect(() => {
      console.log('Search query:', this.query());
    });
    
    // Effect with cleanup
    effect((onCleanup) => {
      const timer = setInterval(() => {
        console.log('Current query:', this.query());
      }, 1000);
      
      onCleanup(() => clearInterval(timer));
    });
  }
}
```

**Effect rules:**
- Run in injection context (constructor or with `runInInjectionContext`)
- Automatically cleaned up when component destroys

## Component State Pattern

```typescript
@Component({
  selector: 'app-todo-list',
  template: `
    <input [value]="newTodo()" (input)="newTodo.set($any($event.target).value)" />
    <button (click)="addTodo()" [disabled]="!canAdd()">Add</button>
    
    <ul>
      @for (todo of filteredTodos(); track todo.id) {
        <li [class.done]="todo.done">
          {{ todo.text }}
          <button (click)="toggleTodo(todo.id)">Toggle</button>
        </li>
      }
    </ul>
    
    <p>{{ remaining() }} remaining</p>
  `,
})
export class TodoList {
  // State
  todos = signal<Todo[]>([]);
  newTodo = signal('');
  filter = signal<'all' | 'active' | 'done'>('all');
  
  // Derived state
  canAdd = computed(() => this.newTodo().trim().length > 0);
  
  filteredTodos = computed(() => {
    const todos = this.todos();
    switch (this.filter()) {
      case 'active': return todos.filter(t => !t.done);
      case 'done': return todos.filter(t => t.done);
      default: return todos;
    }
  });
  
  remaining = computed(() => 
    this.todos().filter(t => !t.done).length
  );
  
  // Actions
  addTodo() {
    const text = this.newTodo().trim();
    if (text) {
      this.todos.update(todos => [
        ...todos,
        { id: crypto.randomUUID(), text, done: false }
      ]);
      this.newTodo.set('');
    }
  }
  
  toggleTodo(id: string) {
    this.todos.update(todos =>
      todos.map(t => t.id === id ? { ...t, done: !t.done } : t)
    );
  }
}
```

## RxJS Interop

### toSignal() - Observable to Signal

```typescript
import { toSignal } from '@angular/core/rxjs-interop';
import { interval } from 'rxjs';

@Component({...})
export class Timer {
  private http = inject(HttpClient);
  
  // From observable - requires initial value or allowUndefined
  counter = toSignal(interval(1000), { initialValue: 0 });
  
  // From HTTP - undefined until loaded
  users = toSignal(this.http.get<User[]>('/api/users'));
  
  // With requireSync for synchronous observables (BehaviorSubject)
  private user$ = new BehaviorSubject<User | null>(null);
  currentUser = toSignal(this.user$, { requireSync: true });
}
```

### toObservable() - Signal to Observable

```typescript
import { toObservable } from '@angular/core/rxjs-interop';
import { switchMap, debounceTime } from 'rxjs';

@Component({...})
export class Search {
  query = signal('');
  
  private http = inject(HttpClient);
  
  // Convert signal to observable for RxJS operators
  results = toSignal(
    toObservable(this.query).pipe(
      debounceTime(300),
      switchMap(q => this.http.get<Result[]>(`/api/search?q=${q}`))
    ),
    { initialValue: [] }
  );
}
```

## Signal Equality

```typescript
// Custom equality function
const user = signal<User>(
  { id: 1, name: 'Alice' },
  { equal: (a, b) => a.id === b.id }
);

// Only triggers updates when ID changes
user.set({ id: 1, name: 'Alice Updated' }); // No update
user.set({ id: 2, name: 'Bob' }); // Triggers update
```

## Untracked Reads

```typescript
import { untracked } from '@angular/core';

const a = signal(1);
const b = signal(2);

// Only depends on 'a', not 'b'
const result = computed(() => {
  const aVal = a();
  const bVal = untracked(() => b());
  return aVal + bVal;
});
```

## Service State Pattern

```typescript
@Injectable({ providedIn: 'root' })
export class Auth {
  // Private writable state
  private _user = signal<User | null>(null);
  private _loading = signal(false);
  
  // Public read-only signals
  readonly user = this._user.asReadonly();
  readonly loading = this._loading.asReadonly();
  readonly isAuthenticated = computed(() => this._user() !== null);
  
  private http = inject(HttpClient);
  
  async login(credentials: Credentials): Promise<void> {
    this._loading.set(true);
    try {
      const user = await firstValueFrom(
        this.http.post<User>('/api/login', credentials)
      );
      this._user.set(user);
    } finally {
      this._loading.set(false);
    }
  }
  
  logout(): void {
    this._user.set(null);
  }
}
```

For advanced patterns including resource(), see [references/signal-patterns.md](references/signal-patterns.md).
```

## File: `skills/angular-signals/references/signal-patterns.md`
```markdown
# Angular Signal Patterns

## Table of Contents
- [Resource API](#resource-api)
- [Signal Store Pattern](#signal-store-pattern)
- [Form State with Signals](#form-state-with-signals)
- [Async Operations](#async-operations)
- [Testing Signals](#testing-signals)

## Resource API

The `resource()` API handles async data fetching with signals:

```typescript
import { resource, signal, computed } from '@angular/core';

@Component({...})
export class UserProfile {
  userId = signal<string>('');
  
  // Resource fetches data when params change
  userResource = resource({
    params: () => ({ id: this.userId() }),
    loader: async ({ params, abortSignal }) => {
      const response = await fetch(`/api/users/${params.id}`, {
        signal: abortSignal,
      });
      return response.json() as Promise<User>;
    },
  });
  
  // Access resource state
  user = computed(() => this.userResource.value());
  isLoading = computed(() => this.userResource.isLoading());
  error = computed(() => this.userResource.error());
}
```

### Resource Status

```typescript
const userResource = resource({...});

// Status signals
userResource.value();      // Current value or undefined
userResource.hasValue();   // Boolean - has resolved value
userResource.error();      // Error or undefined
userResource.isLoading();  // Boolean - currently loading
userResource.status();     // 'idle' | 'loading' | 'reloading' | 'resolved' | 'error' | 'local'

// Manual reload
userResource.reload();

// Local updates
userResource.set(newValue);
userResource.update(current => ({ ...current, name: 'Updated' }));
```

### Resource with Default Value

```typescript
const todosResource = resource({
  defaultValue: [] as Todo[],
  params: () => ({ filter: this.filter() }),
  loader: async ({ params }) => {
    const response = await fetch(`/api/todos?filter=${params.filter}`);
    return response.json();
  },
});

// value() returns Todo[] (never undefined due to defaultValue)
```

### Conditional Loading

```typescript
const userId = signal<string | null>(null);

const userResource = resource({
  params: () => {
    const id = userId();
    // Return undefined to skip loading
    return id ? { id } : undefined;
  },
  loader: async ({ params }) => {
    return fetch(`/api/users/${params.id}`).then(r => r.json());
  },
});
// Status is 'idle' when params returns undefined
```

## Signal Store Pattern

For complex state, create a dedicated store:

```typescript
interface ProductState {
  products: Product[];
  selectedId: string | null;
  filter: string;
  loading: boolean;
  error: string | null;
}

@Injectable({ providedIn: 'root' })
export class ProductSt {
  // Private state
  private state = signal<ProductState>({
    products: [],
    selectedId: null,
    filter: '',
    loading: false,
    error: null,
  });
  
  // Selectors (computed signals)
  readonly products = computed(() => this.state().products);
  readonly selectedId = computed(() => this.state().selectedId);
  readonly filter = computed(() => this.state().filter);
  readonly loading = computed(() => this.state().loading);
  readonly error = computed(() => this.state().error);
  
  readonly filteredProducts = computed(() => {
    const { products, filter } = this.state();
    if (!filter) return products;
    return products.filter(p => 
      p.name.toLowerCase().includes(filter.toLowerCase())
    );
  });
  
  readonly selectedProduct = computed(() => {
    const { products, selectedId } = this.state();
    return products.find(p => p.id === selectedId) ?? null;
  });
  
  private http = inject(HttpClient);
  
  // Actions
  setFilter(filter: string): void {
    this.state.update(s => ({ ...s, filter }));
  }
  
  selectProduct(id: string | null): void {
    this.state.update(s => ({ ...s, selectedId: id }));
  }
  
  async loadProducts(): Promise<void> {
    this.state.update(s => ({ ...s, loading: true, error: null }));
    
    try {
      const products = await firstValueFrom(
        this.http.get<Product[]>('/api/products')
      );
      this.state.update(s => ({ ...s, products, loading: false }));
    } catch (err) {
      this.state.update(s => ({ 
        ...s, 
        loading: false, 
        error: 'Failed to load products' 
      }));
    }
  }
  
  async addProduct(product: Omit<Product, 'id'>): Promise<void> {
    const newProduct = await firstValueFrom(
      this.http.post<Product>('/api/products', product)
    );
    this.state.update(s => ({
      ...s,
      products: [...s.products, newProduct],
    }));
  }
}
```

## Form State with Signals

```typescript
interface FormState<T> {
  value: T;
  touched: boolean;
  dirty: boolean;
  valid: boolean;
  errors: string[];
}

function createFormField<T>(
  initialValue: T,
  validators: ((value: T) => string | null)[] = []
) {
  const value = signal(initialValue);
  const touched = signal(false);
  const dirty = signal(false);
  
  const errors = computed(() => {
    return validators
      .map(v => v(value()))
      .filter((e): e is string => e !== null);
  });
  
  const valid = computed(() => errors().length === 0);
  
  return {
    value,
    touched: touched.asReadonly(),
    dirty: dirty.asReadonly(),
    errors,
    valid,
    
    setValue(newValue: T) {
      value.set(newValue);
      dirty.set(true);
    },
    
    markTouched() {
      touched.set(true);
    },
    
    reset() {
      value.set(initialValue);
      touched.set(false);
      dirty.set(false);
    },
  };
}

// Usage
@Component({...})
export class Signup {
  email = createFormField('', [
    v => !v ? 'Email is required' : null,
    v => !v.includes('@') ? 'Invalid email' : null,
  ]);
  
  password = createFormField('', [
    v => !v ? 'Password is required' : null,
    v => v.length < 8 ? 'Password must be at least 8 characters' : null,
  ]);
  
  formValid = computed(() => 
    this.email.valid() && this.password.valid()
  );
}
```

## Async Operations

### Debounced Search

```typescript
@Component({...})
export class Search {
  query = signal('');
  
  private http = inject(HttpClient);
  
  // Debounced search using toObservable
  results = toSignal(
    toObservable(this.query).pipe(
      debounceTime(300),
      distinctUntilChanged(),
      filter(q => q.length >= 2),
      switchMap(q => this.http.get<Result[]>(`/api/search?q=${q}`)),
      catchError(() => of([]))
    ),
    { initialValue: [] }
  );
  
  // Loading state
  private searching = signal(false);
  readonly isSearching = this.searching.asReadonly();

  constructor() {
    // Track loading state
    effect(() => {
      const q = this.query();
      if (q.length >= 2) {
        this.searching.set(true);
      }
    });

    effect(() => {
      this.results(); // Subscribe to results
      this.searching.set(false);
    });
  }
}
```

### Optimistic Updates

```typescript
@Injectable({ providedIn: 'root' })
export class Todo {
  private todos = signal<Todo[]>([]);
  readonly items = this.todos.asReadonly();
  
  private http = inject(HttpClient);
  
  async toggleTodo(id: string): Promise<void> {
    // Optimistic update
    const previousTodos = this.todos();
    this.todos.update(todos =>
      todos.map(t => t.id === id ? { ...t, done: !t.done } : t)
    );
    
    try {
      await firstValueFrom(
        this.http.patch(`/api/todos/${id}/toggle`, {})
      );
    } catch {
      // Rollback on error
      this.todos.set(previousTodos);
    }
  }
}
```

## Testing Signals

```typescript
describe('Counter', () => {
  it('should increment count', () => {
    const component = new Counter();
    
    expect(component.count()).toBe(0);
    
    component.increment();
    expect(component.count()).toBe(1);
    
    component.increment();
    expect(component.count()).toBe(2);
  });
  
  it('should compute doubled value', () => {
    const component = new Counter();
    
    expect(component.doubled()).toBe(0);
    
    component.count.set(5);
    expect(component.doubled()).toBe(10);
  });
});

describe('ProductSt', () => {
  let store: ProductSt;
  let httpMock: HttpTestingController;

  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [
        ProductSt,
        provideHttpClient(),
        provideHttpClientTesting(),
      ],
    });

    store = TestBed.inject(ProductSt);
    httpMock = TestBed.inject(HttpTestingController);
  });
  
  it('should filter products', () => {
    // Set initial state
    store['state'].set({
      products: [
        { id: '1', name: 'Apple' },
        { id: '2', name: 'Banana' },
      ],
      selectedId: null,
      filter: '',
      loading: false,
      error: null,
    });
    
    expect(store.filteredProducts().length).toBe(2);
    
    store.setFilter('app');
    expect(store.filteredProducts().length).toBe(1);
    expect(store.filteredProducts()[0].name).toBe('Apple');
  });
});
```

## Signal Debugging

```typescript
// Debug effect to log signal changes
effect(() => {
  console.log('State changed:', {
    count: this.count(),
    items: this.items(),
    filter: this.filter(),
  });
});

// Conditional debugging
const DEBUG = signal(false);

effect(() => {
  if (untracked(() => DEBUG())) {
    console.log('Debug:', this.state());
  }
});
```
```

## File: `skills/angular-ssr/SKILL.md`
```markdown
---
name: angular-ssr
description: Implement server-side rendering and hydration in Angular v20+ using @angular/ssr. Use for SSR setup, hydration strategies, prerendering static pages, and handling browser-only APIs. Triggers on SSR configuration, fixing hydration mismatches, prerendering routes, or making code SSR-compatible.
---

# Angular SSR

Implement server-side rendering, hydration, and prerendering in Angular v20+.

## Setup

### Add SSR to Existing Project

```bash
ng add @angular/ssr
```

This adds:
- `@angular/ssr` package
- `server.ts` - Express server
- `src/main.server.ts` - Server bootstrap
- `src/app/app.config.server.ts` - Server providers
- Updates `angular.json` with SSR configuration

### Project Structure

```
src/
├── app/
│   ├── app.config.ts          # Browser config
│   ├── app.config.server.ts   # Server config
│   └── app.routes.ts
├── main.ts                     # Browser bootstrap
├── main.server.ts              # Server bootstrap
server.ts                       # Express server
```

## Configuration

### app.config.server.ts

```typescript
import { ApplicationConfig, mergeApplicationConfig } from '@angular/core';
import { provideServerRendering } from '@angular/platform-server';
import { provideServerRoutesConfig } from '@angular/ssr';
import { appConfig } from './app.config';
import { serverRoutes } from './app.routes.server';

const serverConfig: ApplicationConfig = {
  providers: [
    provideServerRendering(),
    provideServerRoutesConfig(serverRoutes),
  ],
};

export const config = mergeApplicationConfig(appConfig, serverConfig);
```

### Server Routes Configuration

```typescript
// app.routes.server.ts
import { RenderMode, ServerRoute } from '@angular/ssr';

export const serverRoutes: ServerRoute[] = [
  {
    path: '',
    renderMode: RenderMode.Prerender, // Static at build time
  },
  {
    path: 'products',
    renderMode: RenderMode.Prerender,
  },
  {
    path: 'products/:id',
    renderMode: RenderMode.Server, // Dynamic SSR
  },
  {
    path: 'dashboard',
    renderMode: RenderMode.Client, // Client-only (SPA)
  },
  {
    path: '**',
    renderMode: RenderMode.Server,
  },
];
```

### Render Modes

| Mode | Description | Use Case |
|------|-------------|----------|
| `RenderMode.Prerender` | Static HTML at build time | Marketing pages, blogs |
| `RenderMode.Server` | Dynamic SSR per request | User-specific content |
| `RenderMode.Client` | Client-side only (SPA) | Authenticated dashboards |

## Hydration

### Default Hydration

Hydration is enabled by default with `provideClientHydration()`:

```typescript
// app.config.ts
import { provideClientHydration } from '@angular/platform-browser';

export const appConfig: ApplicationConfig = {
  providers: [
    provideClientHydration(),
    // ...
  ],
};
```

### Incremental Hydration

Defer hydration of specific components:

```typescript
@Component({
  template: `
    <!-- Hydrate when visible -->
    @defer (hydrate on viewport) {
      <app-comments [postId]="postId" />
    } @placeholder {
      <div class="comments-placeholder">Loading comments...</div>
    }
    
    <!-- Hydrate on interaction -->
    @defer (hydrate on interaction) {
      <app-interactive-chart [data]="chartData" />
    }
    
    <!-- Hydrate on idle -->
    @defer (hydrate on idle) {
      <app-recommendations />
    }
    
    <!-- Never hydrate (static only) -->
    @defer (hydrate never) {
      <app-static-footer />
    }
  `,
})
export class Post {
  postId = input.required<string>();
  chartData = input.required<ChartData>();
}
```

### Hydration Triggers

| Trigger | Description |
|---------|-------------|
| `hydrate on viewport` | When element enters viewport |
| `hydrate on interaction` | On click, focus, or input |
| `hydrate on idle` | When browser is idle |
| `hydrate on immediate` | Immediately after load |
| `hydrate on timer(ms)` | After specified delay |
| `hydrate when condition` | When expression is true |
| `hydrate never` | Never hydrate (static) |

### Event Replay

Capture user events before hydration completes:

```typescript
import { provideClientHydration, withEventReplay } from '@angular/platform-browser';

export const appConfig: ApplicationConfig = {
  providers: [
    provideClientHydration(withEventReplay()),
  ],
};
```

## Browser-Only Code

### Platform Detection

```typescript
import { PLATFORM_ID, inject } from '@angular/core';
import { isPlatformBrowser, isPlatformServer } from '@angular/common';

@Component({...})
export class My {
  private platformId = inject(PLATFORM_ID);
  
  ngOnInit() {
    if (isPlatformBrowser(this.platformId)) {
      // Browser-only code
      window.addEventListener('scroll', this.onScroll);
    }
  }
}
```

### afterNextRender / afterRender

Run code only in browser after rendering:

```typescript
import { afterNextRender, afterRender } from '@angular/core';

@Component({...})
export class Chart {
  constructor() {
    // Runs once after first render (browser only)
    afterNextRender(() => {
      this.initChart();
    });
    
    // Runs after every render (browser only)
    afterRender(() => {
      this.updateChart();
    });
  }
  
  private initChart() {
    // Safe to use DOM APIs here
    const canvas = document.getElementById('chart');
    new Chart(canvas, this.config);
  }
}
```

### Inject Browser APIs Safely

```typescript
// tokens.ts
import { InjectionToken, PLATFORM_ID, inject } from '@angular/core';
import { isPlatformBrowser } from '@angular/common';

export const WINDOW = new InjectionToken<Window | null>('Window', {
  providedIn: 'root',
  factory: () => {
    const platformId = inject(PLATFORM_ID);
    return isPlatformBrowser(platformId) ? window : null;
  },
});

export const LOCAL_STORAGE = new InjectionToken<Storage | null>('LocalStorage', {
  providedIn: 'root',
  factory: () => {
    const platformId = inject(PLATFORM_ID);
    return isPlatformBrowser(platformId) ? localStorage : null;
  },
});

// Usage
@Injectable({ providedIn: 'root' })
export class Storage {
  private storage = inject(LOCAL_STORAGE);
  
  get(key: string): string | null {
    return this.storage?.getItem(key) ?? null;
  }
  
  set(key: string, value: string): void {
    this.storage?.setItem(key, value);
  }
}
```

## Prerendering

### Static Routes

```typescript
// app.routes.server.ts
export const serverRoutes: ServerRoute[] = [
  { path: '', renderMode: RenderMode.Prerender },
  { path: 'about', renderMode: RenderMode.Prerender },
  { path: 'contact', renderMode: RenderMode.Prerender },
  { path: 'blog', renderMode: RenderMode.Prerender },
];
```

### Dynamic Routes with getPrerenderParams

```typescript
// app.routes.server.ts
import { RenderMode, ServerRoute, PrerenderFallback } from '@angular/ssr';

export const serverRoutes: ServerRoute[] = [
  {
    path: 'products/:id',
    renderMode: RenderMode.Prerender,
    async getPrerenderParams() {
      // Fetch product IDs to prerender
      const response = await fetch('https://api.example.com/products');
      const products = await response.json();
      return products.map((p: Product) => ({ id: p.id }));
    },
    fallback: PrerenderFallback.Server, // SSR for non-prerendered
  },
  {
    path: 'blog/:slug',
    renderMode: RenderMode.Prerender,
    async getPrerenderParams() {
      const posts = await fetchBlogPosts();
      return posts.map(post => ({ slug: post.slug }));
    },
    fallback: PrerenderFallback.Client, // SPA for non-prerendered
  },
];
```

### Prerender Fallback Options

| Fallback | Description |
|----------|-------------|
| `PrerenderFallback.Server` | SSR for non-prerendered routes |
| `PrerenderFallback.Client` | Client-side rendering |
| `PrerenderFallback.None` | 404 for non-prerendered routes |

## HTTP Caching

### TransferState

Automatically transfer HTTP responses from server to client:

```typescript
import { provideClientHydration, withHttpTransferCacheOptions } from '@angular/platform-browser';

export const appConfig: ApplicationConfig = {
  providers: [
    provideClientHydration(
      withHttpTransferCacheOptions({
        includePostRequests: true,
        includeRequestsWithAuthHeaders: false,
        filter: (req) => !req.url.includes('/api/realtime'),
      })
    ),
  ],
};
```

### Manual TransferState

```typescript
import { TransferState, makeStateKey } from '@angular/core';

const PRODUCTS_KEY = makeStateKey<Product[]>('products');

@Injectable({ providedIn: 'root' })
export class Product {
  private http = inject(HttpClient);
  private transferState = inject(TransferState);
  private platformId = inject(PLATFORM_ID);
  
  getProducts(): Observable<Product[]> {
    // Check if data was transferred from server
    if (this.transferState.hasKey(PRODUCTS_KEY)) {
      const products = this.transferState.get(PRODUCTS_KEY, []);
      this.transferState.remove(PRODUCTS_KEY);
      return of(products);
    }
    
    return this.http.get<Product[]>('/api/products').pipe(
      tap(products => {
        // Store for transfer on server
        if (isPlatformServer(this.platformId)) {
          this.transferState.set(PRODUCTS_KEY, products);
        }
      })
    );
  }
}
```

## Build and Deploy

### Build Commands

```bash
# Build with SSR
ng build

# Output structure
dist/
├── my-app/
│   ├── browser/      # Client assets
│   └── server/       # Server bundle
```

### Run SSR Server

```bash
# Development
npm run serve:ssr:my-app

# Production
node dist/my-app/server/server.mjs
```

### Deploy to Node.js Host

```javascript
// server.ts (generated)
import { APP_BASE_HREF } from '@angular/common';
import { CommonEngine } from '@angular/ssr/node';
import express from 'express';
import { dirname, join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
import bootstrap from './src/main.server';

const serverDistFolder = dirname(fileURLToPath(import.meta.url));
const browserDistFolder = resolve(serverDistFolder, '../browser');
const indexHtml = join(serverDistFolder, 'index.server.html');

const app = express();
const commonEngine = new CommonEngine();

app.get('*', express.static(browserDistFolder, { maxAge: '1y', index: false }));

app.get('*', (req, res, next) => {
  commonEngine
    .render({
      bootstrap,
      documentFilePath: indexHtml,
      url: req.originalUrl,
      publicPath: browserDistFolder,
      providers: [{ provide: APP_BASE_HREF, useValue: req.baseUrl }],
    })
    .then((html) => res.send(html))
    .catch((err) => next(err));
});

app.listen(4000, () => {
  console.log('Server listening on http://localhost:4000');
});
```

For advanced patterns, see [references/ssr-patterns.md](references/ssr-patterns.md).
```

## File: `skills/angular-ssr/references/ssr-patterns.md`
```markdown
# Angular SSR Patterns

## Table of Contents
- [Hydration Debugging](#hydration-debugging)
- [SEO Optimization](#seo-optimization)
- [Authentication with SSR](#authentication-with-ssr)
- [Caching Strategies](#caching-strategies)
- [Error Handling](#error-handling)
- [Performance Optimization](#performance-optimization)

## Hydration Debugging

### Common Hydration Mismatches

```typescript
// Problem: Different content on server vs client
@Component({
  template: `<p>Current time: {{ currentTime }}</p>`,
})
export class Time {
  // BAD: Different value on server and client
  currentTime = new Date().toLocaleTimeString();
}

// Solution: Use afterNextRender or skip SSR
@Component({
  template: `<p>Current time: {{ currentTime() }}</p>`,
})
export class Time {
  currentTime = signal('');
  
  constructor() {
    afterNextRender(() => {
      this.currentTime.set(new Date().toLocaleTimeString());
    });
  }
}
```

### Skip Hydration for Dynamic Content

```typescript
@Component({
  template: `
    <!-- Skip hydration for this subtree -->
    <div ngSkipHydration>
      <app-dynamic-widget />
    </div>
  `,
})
export class Page {}
```

### Debug Hydration Issues

```typescript
// Enable hydration debugging in development
import { provideClientHydration, withNoDomReuse } from '@angular/platform-browser';

export const appConfig: ApplicationConfig = {
  providers: [
    provideClientHydration(
      // Disable DOM reuse to see hydration errors clearly
      ...(isDevMode() ? [withNoDomReuse()] : [])
    ),
  ],
};
```

## SEO Optimization

### Meta Tags Service

```typescript
import { Injectable, inject } from '@angular/core';
import { Meta, Title } from '@angular/platform-browser';
import { DOCUMENT } from '@angular/common';

@Injectable({ providedIn: 'root' })
export class Seo {
  private meta = inject(Meta);
  private title = inject(Title);
  private document = inject(DOCUMENT);
  
  updateMetaTags(config: {
    title: string;
    description: string;
    image?: string;
    url?: string;
    type?: string;
  }) {
    // Basic meta
    this.title.setTitle(config.title);
    this.meta.updateTag({ name: 'description', content: config.description });
    
    // Open Graph
    this.meta.updateTag({ property: 'og:title', content: config.title });
    this.meta.updateTag({ property: 'og:description', content: config.description });
    this.meta.updateTag({ property: 'og:type', content: config.type || 'website' });
    
    if (config.image) {
      this.meta.updateTag({ property: 'og:image', content: config.image });
    }
    
    if (config.url) {
      this.meta.updateTag({ property: 'og:url', content: config.url });
      this.updateCanonicalUrl(config.url);
    }
    
    // Twitter Card
    this.meta.updateTag({ name: 'twitter:card', content: 'summary_large_image' });
    this.meta.updateTag({ name: 'twitter:title', content: config.title });
    this.meta.updateTag({ name: 'twitter:description', content: config.description });
    
    if (config.image) {
      this.meta.updateTag({ name: 'twitter:image', content: config.image });
    }
  }
  
  private updateCanonicalUrl(url: string) {
    let link: HTMLLinkElement | null = this.document.querySelector('link[rel="canonical"]');
    
    if (!link) {
      link = this.document.createElement('link');
      link.setAttribute('rel', 'canonical');
      this.document.head.appendChild(link);
    }
    
    link.setAttribute('href', url);
  }
  
  setJsonLd(data: object) {
    let script: HTMLScriptElement | null = this.document.querySelector('script[type="application/ld+json"]');
    
    if (!script) {
      script = this.document.createElement('script');
      script.type = 'application/ld+json';
      this.document.head.appendChild(script);
    }
    
    script.textContent = JSON.stringify(data);
  }
}

// Usage in component
@Component({...})
export class Product {
  private seo = inject(Seo);
  product = input.required<Product>();
  
  constructor() {
    effect(() => {
      const product = this.product();
      this.seo.updateMetaTags({
        title: `${product.name} | My Store`,
        description: product.description,
        image: product.imageUrl,
        url: `https://mystore.com/products/${product.id}`,
        type: 'product',
      });
      
      this.seo.setJsonLd({
        '@context': 'https://schema.org',
        '@type': 'Product',
        name: product.name,
        description: product.description,
        image: product.imageUrl,
        offers: {
          '@type': 'Offer',
          price: product.price,
          priceCurrency: 'USD',
        },
      });
    });
  }
}
```

### Route-Based SEO with Resolvers

```typescript
// seo.resolver.ts
export const seoResolver: ResolveFn<SeoData> = async (route) => {
  const productId = route.paramMap.get('id')!;
  const productService = inject(Product);
  const product = await productService.getById(productId);
  
  return {
    title: `${product.name} | My Store`,
    description: product.description,
    image: product.imageUrl,
  };
};

// Routes
{
  path: 'products/:id',
  component: Product,
  resolve: { seo: seoResolver },
}

// Component
@Component({...})
export class Product {
  private seo = inject(Seo);
  seoData = input.required<SeoData>(); // From resolver
  
  constructor() {
    effect(() => {
      this.seo.updateMetaTags(this.seoData());
    });
  }
}
```

## Authentication with SSR

### Cookie-Based Auth

```typescript
// Server-side cookie reading
import { REQUEST } from '@angular/ssr/tokens';

@Injectable({ providedIn: 'root' })
export class Auth {
  private request = inject(REQUEST, { optional: true });
  private platformId = inject(PLATFORM_ID);
  
  getToken(): string | null {
    if (isPlatformServer(this.platformId) && this.request) {
      // Read from request cookies on server
      const cookies = this.request.headers.cookie || '';
      const match = cookies.match(/auth_token=([^;]+)/);
      return match ? match[1] : null;
    }
    
    if (isPlatformBrowser(this.platformId)) {
      // Read from document cookies on client
      const match = document.cookie.match(/auth_token=([^;]+)/);
      return match ? match[1] : null;
    }
    
    return null;
  }
}
```

### Skip SSR for Authenticated Routes

```typescript
// app.routes.server.ts
export const serverRoutes: ServerRoute[] = [
  // Public routes - prerender
  { path: '', renderMode: RenderMode.Prerender },
  { path: 'products', renderMode: RenderMode.Prerender },
  
  // Authenticated routes - client only
  { path: 'dashboard', renderMode: RenderMode.Client },
  { path: 'profile', renderMode: RenderMode.Client },
  { path: 'settings', renderMode: RenderMode.Client },
];
```

## Caching Strategies

### HTTP Cache Headers

```typescript
// server.ts
import { REQUEST, RESPONSE_INIT } from '@angular/ssr/tokens';

// In route configuration or component
@Component({...})
export class ProductList {
  private responseInit = inject(RESPONSE_INIT, { optional: true });
  
  constructor() {
    // Set cache headers for SSR response
    if (this.responseInit) {
      this.responseInit.headers = {
        ...this.responseInit.headers,
        'Cache-Control': 'public, max-age=3600, s-maxage=86400',
      };
    }
  }
}
```

### CDN Caching with Vary Headers

```typescript
// server.ts - Express middleware
app.use((req, res, next) => {
  // Vary by cookie for authenticated content
  res.setHeader('Vary', 'Cookie');
  next();
});
```

### Stale-While-Revalidate

```typescript
// Set SWR headers for dynamic content
this.responseInit.headers = {
  'Cache-Control': 'public, max-age=60, stale-while-revalidate=3600',
};
```

## Error Handling

### SSR Error Boundaries

```typescript
// error-handler.ts
import { ErrorHandler, Injectable, inject } from '@angular/core';
import { PLATFORM_ID } from '@angular/core';
import { isPlatformServer } from '@angular/common';

@Injectable()
export class SsrError implements ErrorHandler {
  private platformId = inject(PLATFORM_ID);
  
  handleError(error: Error) {
    if (isPlatformServer(this.platformId)) {
      // Log server errors
      console.error('SSR Error:', error);
      // Could send to monitoring service
    } else {
      // Client-side error handling
      console.error('Client Error:', error);
    }
  }
}

// Provide in app.config.ts
{ provide: ErrorHandler, useClass: SsrError }
```

### Graceful Degradation

```typescript
@Component({
  template: `
    @if (dataError()) {
      <!-- Fallback content that works without data -->
      <app-fallback-content />
    } @else {
      <app-data-content [data]="data()" />
    }
  `,
})
export class PageCmpt {
  private dataService = inject(Data);
  
  data = signal<Data | null>(null);
  dataError = signal(false);
  
  constructor() {
    this.loadData();
  }
  
  private async loadData() {
    try {
      const data = await this.dataService.getData();
      this.data.set(data);
    } catch {
      this.dataError.set(true);
    }
  }
}
```

## Performance Optimization

### Lazy Hydration Strategy

```typescript
@Component({
  template: `
    <!-- Critical content - hydrate immediately -->
    <header>
      <app-navigation />
    </header>
    
    <!-- Main content - hydrate on viewport -->
    <main>
      @defer (hydrate on viewport) {
        <app-product-grid [products]="products()" />
      }
    </main>
    
    <!-- Below fold - hydrate on idle -->
    @defer (hydrate on idle) {
      <app-reviews [productId]="productId()" />
    }
    
    <!-- Interactive only - hydrate on interaction -->
    @defer (hydrate on interaction) {
      <app-chat-widget />
    }
    
    <!-- Static footer - never hydrate -->
    @defer (hydrate never) {
      <app-footer />
    }
  `,
})
export class ProductPage {}
```

### Preload Critical Data

```typescript
// app.routes.server.ts
export const serverRoutes: ServerRoute[] = [
  {
    path: 'products/:id',
    renderMode: RenderMode.Server,
    async getPrerenderParams() {
      // Prerender top 100 products
      const topProducts = await fetchTopProducts(100);
      return topProducts.map(p => ({ id: p.id }));
    },
  },
];
```

### Streaming SSR (Experimental)

```typescript
// Enable streaming for faster TTFB
import { provideServerRendering } from '@angular/platform-server';

const serverConfig: ApplicationConfig = {
  providers: [
    provideServerRendering(),
    // Streaming is automatic with @defer blocks
  ],
};
```

## Testing SSR

### Test Server Rendering

```typescript
import { renderApplication } from '@angular/platform-server';
import { App } from './app.component';
import { config } from './app.config.server';

describe('SSR', () => {
  it('should render home page', async () => {
    const html = await renderApplication(App, {
      appId: 'my-app',
      providers: config.providers,
      url: '/',
    });
    
    expect(html).toContain('<h1>Welcome</h1>');
    expect(html).toContain('</app-root>');
  });
  
  it('should render product page with data', async () => {
    const html = await renderApplication(App, {
      appId: 'my-app',
      providers: config.providers,
      url: '/products/123',
    });
    
    expect(html).toContain('Product Name');
    expect(html).not.toContain('Loading...');
  });
});
```

### Test Hydration

```typescript
import { TestBed } from '@angular/core/testing';
import { provideClientHydration } from '@angular/platform-browser';

describe('Hydration', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [provideClientHydration()],
    });
  });
  
  it('should hydrate without errors', () => {
    const fixture = TestBed.createComponent(App);
    fixture.detectChanges();
    
    // No hydration mismatch errors should be thrown
    expect(fixture.componentInstance).toBeTruthy();
  });
});
```
```

## File: `skills/angular-testing/SKILL.md`
```markdown
---
name: angular-testing
description: Write unit and integration tests for Angular v20+ applications using Vitest or Jasmine with TestBed and modern testing patterns. Use for testing components with signals, OnPush change detection, services with inject(), and HTTP interactions. Triggers on test creation, testing signal-based components, mocking dependencies, or setting up test infrastructure. Don't use for E2E testing with Cypress or Playwright, or for testing non-Angular JavaScript/TypeScript code.
---

# Angular Testing

Test Angular v20+ applications with Vitest (recommended) or Jasmine, focusing on signal-based components and modern patterns.

## Vitest Setup (Angular v20+)

Angular v20+ has native Vitest support through the `@angular/build` package.

```bash
npm install -D vitest jsdom
```

Configure in angular.json:

```json
{
  "projects": {
    "your-app": {
      "architect": {
        "test": {
          "builder": "@angular/build:unit-test",
          "options": {
            "tsConfig": "tsconfig.spec.json",
            "buildTarget": "your-app:build"
          }
        }
      }
    }
  }
}
```

Run tests:

```bash
ng test              # Run tests
ng test --watch      # Watch mode
ng test --code-coverage  # With coverage
```

For Vitest migration from Jasmine and advanced configuration, see [references/vitest-migration.md](references/vitest-migration.md).

## Basic Component Test

```typescript
import { describe, it, expect, beforeEach } from 'vitest';
import { ComponentFixture, TestBed } from '@angular/core/testing';
import { Counter } from './counter.component';

describe('Counter', () => {
  let component: Counter;
  let fixture: ComponentFixture<Counter>;
  
  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [Counter], // Standalone component
    }).compileComponents();
    
    fixture = TestBed.createComponent(Counter);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });
  
  it('should create', () => {
    expect(component).toBeTruthy();
  });
  
  it('should increment count', () => {
    expect(component.count()).toBe(0);
    component.increment();
    expect(component.count()).toBe(1);
  });
  
  it('should display count in template', () => {
    component.count.set(5);
    fixture.detectChanges();
    
    const element = fixture.nativeElement.querySelector('.count');
    expect(element.textContent).toContain('5');
  });
});
```

## Testing Signals

### Direct Signal Testing

```typescript
import { signal, computed } from '@angular/core';

describe('Signal logic', () => {
  it('should update computed when signal changes', () => {
    const count = signal(0);
    const doubled = computed(() => count() * 2);
    
    expect(doubled()).toBe(0);
    
    count.set(5);
    expect(doubled()).toBe(10);
    
    count.update(c => c + 1);
    expect(doubled()).toBe(12);
  });
});
```

### Testing Component Signals

```typescript
@Component({
  selector: 'app-todo-list',
  template: `
    <ul>
      @for (todo of filteredTodos(); track todo.id) {
        <li>{{ todo.text }}</li>
      }
    </ul>
    <p>{{ remaining() }} remaining</p>
  `,
})
export class TodoList {
  todos = signal<Todo[]>([]);
  filter = signal<'all' | 'active' | 'done'>('all');
  
  filteredTodos = computed(() => {
    const todos = this.todos();
    switch (this.filter()) {
      case 'active': return todos.filter(t => !t.done);
      case 'done': return todos.filter(t => t.done);
      default: return todos;
    }
  });
  
  remaining = computed(() => this.todos().filter(t => !t.done).length);
}

describe('TodoList', () => {
  let component: TodoList;
  let fixture: ComponentFixture<TodoList>;
  
  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [TodoList],
    }).compileComponents();
    
    fixture = TestBed.createComponent(TodoList);
    component = fixture.componentInstance;
  });
  
  it('should filter active todos', () => {
    component.todos.set([
      { id: '1', text: 'Task 1', done: false },
      { id: '2', text: 'Task 2', done: true },
      { id: '3', text: 'Task 3', done: false },
    ]);
    
    component.filter.set('active');
    
    expect(component.filteredTodos().length).toBe(2);
    expect(component.remaining()).toBe(2);
  });
});
```

## Testing OnPush Components

OnPush components require explicit change detection:

```typescript
@Component({
  changeDetection: ChangeDetectionStrategy.OnPush,
  template: `<span>{{ data().name }}</span>`,
})
export class OnPushCmpt {
  data = input.required<{ name: string }>();
}

describe('OnPushCmpt', () => {
  it('should update when input signal changes', () => {
    const fixture = TestBed.createComponent(OnPushCmpt);
    
    // Set input using setInput (for signal inputs)
    fixture.componentRef.setInput('data', { name: 'Initial' });
    fixture.detectChanges();
    
    expect(fixture.nativeElement.textContent).toContain('Initial');
    
    // Update input
    fixture.componentRef.setInput('data', { name: 'Updated' });
    fixture.detectChanges();
    
    expect(fixture.nativeElement.textContent).toContain('Updated');
  });
});
```

## Testing Services

### Basic Service Test

```typescript
@Injectable({ providedIn: 'root' })
export class CounterService {
  private _count = signal(0);
  readonly count = this._count.asReadonly();
  
  increment() { this._count.update(c => c + 1); }
  reset() { this._count.set(0); }
}

describe('CounterService', () => {
  let service: CounterService;
  
  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(CounterService);
  });
  
  it('should increment count', () => {
    expect(service.count()).toBe(0);
    service.increment();
    expect(service.count()).toBe(1);
  });
});
```

### Service with HTTP

```typescript
import { HttpTestingController, provideHttpClientTesting } from '@angular/common/http/testing';
import { provideHttpClient } from '@angular/common/http';

describe('UserService', () => {
  let service: UserService;
  let httpMock: HttpTestingController;
  
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [
        provideHttpClient(),
        provideHttpClientTesting(),
      ],
    });
    
    service = TestBed.inject(UserService);
    httpMock = TestBed.inject(HttpTestingController);
  });
  
  afterEach(() => {
    httpMock.verify(); // Verify no outstanding requests
  });
  
  it('should fetch user by id', () => {
    const mockUser = { id: '1', name: 'Test User' };
    
    service.getUser('1').subscribe(user => {
      expect(user).toEqual(mockUser);
    });
    
    const req = httpMock.expectOne('/api/users/1');
    expect(req.request.method).toBe('GET');
    req.flush(mockUser);
  });
});
```

## Mocking Dependencies

### Using Vitest Mocks

```typescript
import { describe, it, expect, vi, beforeEach } from 'vitest';

describe('UserProfile', () => {
  const mockUserService = {
    getUser: vi.fn(),
    updateUser: vi.fn(),
    user: signal<User | null>(null),
  };
  
  beforeEach(async () => {
    vi.clearAllMocks();
    mockUserService.getUser.mockReturnValue(of({ id: '1', name: 'Test' }));
    
    await TestBed.configureTestingModule({
      imports: [UserProfile],
      providers: [
        { provide: UserService, useValue: mockUserService },
      ],
    }).compileComponents();
  });
  
  it('should call getUser on init', () => {
    const fixture = TestBed.createComponent(UserProfile);
    fixture.detectChanges();
    
    expect(mockUserService.getUser).toHaveBeenCalledWith('1');
  });
});
```

### Mock Signal-Based Service

```typescript
const mockAuth = {
  user: signal<User | null>(null),
  isAuthenticated: computed(() => mockAuth.user() !== null),
  login: vi.fn(),
  logout: vi.fn(),
};

beforeEach(async () => {
  await TestBed.configureTestingModule({
    imports: [ProtectedPage],
    providers: [
      { provide: AuthService, useValue: mockAuth },
    ],
  }).compileComponents();
});

it('should show content when authenticated', () => {
  mockAuth.user.set({ id: '1', name: 'Test User' });
  
  const fixture = TestBed.createComponent(ProtectedPage);
  fixture.detectChanges();
  
  expect(fixture.nativeElement.querySelector('.protected-content')).toBeTruthy();
});
```

## Testing Inputs and Outputs

```typescript
@Component({
  selector: 'app-item',
  template: `<div (click)="select()">{{ item().name }}</div>`,
})
export class ItemCmpt {
  item = input.required<Item>();
  selected = output<Item>();
  
  select() {
    this.selected.emit(this.item());
  }
}

describe('ItemCmpt', () => {
  it('should emit selected event on click', () => {
    const fixture = TestBed.createComponent(ItemCmpt);
    const item: Item = { id: '1', name: 'Test Item' };
    
    fixture.componentRef.setInput('item', item);
    fixture.detectChanges();
    
    let emittedItem: Item | undefined;
    fixture.componentInstance.selected.subscribe(i => emittedItem = i);
    
    fixture.nativeElement.querySelector('div').click();
    
    expect(emittedItem).toEqual(item);
  });
});
```

## Testing Async Operations

### Using fakeAsync

```typescript
import { fakeAsync, tick, flush } from '@angular/core/testing';

it('should debounce search', fakeAsync(() => {
  const fixture = TestBed.createComponent(SearchCmpt);
  fixture.detectChanges();
  
  fixture.componentInstance.query.set('test');
  
  tick(300); // Advance time for debounce
  fixture.detectChanges();
  
  expect(fixture.componentInstance.results().length).toBeGreaterThan(0);
  
  flush(); // Flush remaining timers
}));
```

### Using waitForAsync

```typescript
import { waitForAsync } from '@angular/core/testing';

it('should load data', waitForAsync(() => {
  const fixture = TestBed.createComponent(DataCmpt);
  fixture.detectChanges();
  
  fixture.whenStable().then(() => {
    fixture.detectChanges();
    expect(fixture.componentInstance.data()).toBeDefined();
  });
}));
```

## Testing HTTP Resources

```typescript
@Component({
  template: `
    @if (userResource.isLoading()) {
      <p>Loading...</p>
    } @else if (userResource.hasValue()) {
      <p>{{ userResource.value().name }}</p>
    }
  `,
})
export class UserCmpt {
  userId = signal('1');
  userResource = httpResource<User>(() => `/api/users/${this.userId()}`);
}

describe('UserCmpt', () => {
  let httpMock: HttpTestingController;
  
  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [UserCmpt],
      providers: [
        provideHttpClient(),
        provideHttpClientTesting(),
      ],
    }).compileComponents();
    
    httpMock = TestBed.inject(HttpTestingController);
  });
  
  it('should display user name after loading', () => {
    const fixture = TestBed.createComponent(UserCmpt);
    fixture.detectChanges();
    
    expect(fixture.nativeElement.textContent).toContain('Loading');
    
    const req = httpMock.expectOne('/api/users/1');
    req.flush({ id: '1', name: 'John Doe' });
    fixture.detectChanges();
    
    expect(fixture.nativeElement.textContent).toContain('John Doe');
  });
});
```

For advanced testing patterns including component harnesses, router testing, form testing, and directive testing, see [references/testing-patterns.md](references/testing-patterns.md).

For Vitest migration from Jasmine, see [references/vitest-migration.md](references/vitest-migration.md).
```

## File: `skills/angular-testing/references/testing-patterns.md`
```markdown
# Angular Testing Patterns

## Table of Contents
- [Vitest Advanced Patterns](#vitest-advanced-patterns)
- [Component Harnesses](#component-harnesses)
- [Testing Router](#testing-router)
- [Testing Forms](#testing-forms)
- [Testing Directives](#testing-directives)
- [Testing Pipes](#testing-pipes)
- [E2E Testing Setup](#e2e-testing-setup)

## Vitest Advanced Patterns

### Snapshot Testing

```typescript
import { describe, it, expect } from 'vitest';

describe('UserCard', () => {
  it('should match snapshot', () => {
    const fixture = TestBed.createComponent(UserCard);
    fixture.componentRef.setInput('user', { id: '1', name: 'John', email: 'john@example.com' });
    fixture.detectChanges();
    
    expect(fixture.nativeElement.innerHTML).toMatchSnapshot();
  });
});
```

### Parameterized Tests

```typescript
import { describe, it, expect } from 'vitest';

describe('Validator', () => {
  it.each([
    { input: '', expected: false },
    { input: 'test', expected: false },
    { input: 'test@example.com', expected: true },
    { input: 'invalid@', expected: false },
  ])('should validate email "$input" as $expected', ({ input, expected }) => {
    expect(isValidEmail(input)).toBe(expected);
  });
});
```

### Testing with Fake Timers

```typescript
import { describe, it, expect, vi, beforeEach, afterEach } from 'vitest';

describe('Debounced Search', () => {
  beforeEach(() => {
    vi.useFakeTimers();
  });
  
  afterEach(() => {
    vi.useRealTimers();
  });
  
  it('should debounce search input', async () => {
    const fixture = TestBed.createComponent(Search);
    fixture.detectChanges();
    
    fixture.componentInstance.query.set('test');
    
    // Search not called yet
    expect(fixture.componentInstance.results()).toEqual([]);
    
    // Advance timers
    vi.advanceTimersByTime(300);
    await fixture.whenStable();
    fixture.detectChanges();
    
    expect(fixture.componentInstance.results().length).toBeGreaterThan(0);
  });
});
```

### Module Mocking

```typescript
import { describe, it, expect, vi } from 'vitest';

// Mock entire module
vi.mock('./analytics.service', () => ({
  Analytics: class {
    track = vi.fn();
    identify = vi.fn();
  },
}));

describe('with mocked analytics', () => {
  it('should track events', () => {
    const fixture = TestBed.createComponent(Dashboard);
    const analytics = TestBed.inject(Analytics);
    
    fixture.detectChanges();
    
    expect(analytics.track).toHaveBeenCalledWith('dashboard_viewed');
  });
});
```

### Testing Async/Await

```typescript
import { describe, it, expect, vi } from 'vitest';

describe('User', () => {
  it('should load user data', async () => {
    const mockUser = { id: '1', name: 'Test' };
    const httpMock = TestBed.inject(HttpTestingController);
    const service = TestBed.inject(User);
    
    const userPromise = service.loadUser('1');
    
    httpMock.expectOne('/api/users/1').flush(mockUser);
    
    const user = await userPromise;
    expect(user).toEqual(mockUser);
  });
});
```

### Coverage Configuration

```typescript
// vite.config.ts
export default defineConfig({
  test: {
    coverage: {
      provider: 'v8',
      reporter: ['text', 'html', 'lcov'],
      exclude: [
        'node_modules/',
        'src/test-setup.ts',
        '**/*.spec.ts',
        '**/*.d.ts',
      ],
      thresholds: {
        statements: 80,
        branches: 80,
        functions: 80,
        lines: 80,
      },
    },
  },
});
```

### Vitest UI Mode

```bash
# Run with UI
npx vitest --ui

# Open UI at specific port
npx vitest --ui --port 51204
```

### Concurrent Tests

```typescript
import { describe, it, expect } from 'vitest';

// Run tests in this describe block concurrently
describe.concurrent('API calls', () => {
  it('should fetch users', async () => {
    // ...
  });
  
  it('should fetch products', async () => {
    // ...
  });
  
  it('should fetch orders', async () => {
    // ...
  });
});
```

### Test Fixtures

```typescript
import { describe, it, expect, beforeEach } from 'vitest';

// Shared test fixtures
const createTestUser = (overrides = {}) => ({
  id: '1',
  name: 'Test User',
  email: 'test@example.com',
  ...overrides,
});

const createTestProduct = (overrides = {}) => ({
  id: '1',
  name: 'Test Product',
  price: 99.99,
  ...overrides,
});

describe('Order', () => {
  it('should calculate total', () => {
    const fixture = TestBed.createComponent(Order);
    fixture.componentRef.setInput('user', createTestUser());
    fixture.componentRef.setInput('products', [
      createTestProduct({ price: 10 }),
      createTestProduct({ id: '2', price: 20 }),
    ]);
    fixture.detectChanges();
    
    expect(fixture.componentInstance.total()).toBe(30);
  });
});
```

## Component Harnesses

Use Angular CDK component harnesses for more maintainable tests:

### Creating a Harness

```typescript
import { ComponentHarness, HarnessPredicate } from '@angular/cdk/testing';

export class CounterHarn extends ComponentHarness {
  static hostSelector = 'app-counter';
  
  // Locators
  private getIncrementButton = this.locatorFor('button.increment');
  private getDecrementButton = this.locatorFor('button.decrement');
  private getCountDisplay = this.locatorFor('.count');
  
  // Actions
  async increment(): Promise<void> {
    const button = await this.getIncrementButton();
    await button.click();
  }
  
  async decrement(): Promise<void> {
    const button = await this.getDecrementButton();
    await button.click();
  }
  
  // Queries
  async getCount(): Promise<number> {
    const display = await this.getCountDisplay();
    const text = await display.text();
    return parseInt(text, 10);
  }
  
  // Filter factory
  static with(options: { count?: number } = {}): HarnessPredicate<CounterHarn> {
    return new HarnessPredicate(CounterHarn, options)
      .addOption('count', options.count, async (harness, count) => {
        return (await harness.getCount()) === count;
      });
  }
}
```

### Using Harnesses in Tests

```typescript
import { TestbedHarnessEnvironment } from '@angular/cdk/testing/testbed';

describe('Counter with Harness', () => {
  let loader: HarnessLoader;
  
  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [Counter],
    }).compileComponents();
    
    const fixture = TestBed.createComponent(Counter);
    loader = TestbedHarnessEnvironment.loader(fixture);
  });
  
  it('should increment count', async () => {
    const counter = await loader.getHarness(CounterHarn);
    
    expect(await counter.getCount()).toBe(0);
    
    await counter.increment();
    expect(await counter.getCount()).toBe(1);
    
    await counter.increment();
    expect(await counter.getCount()).toBe(2);
  });
  
  it('should find counter with specific count', async () => {
    const counter = await loader.getHarness(CounterHarn);
    await counter.increment();
    await counter.increment();
    
    // Find counter with count of 2
    const counterWith2 = await loader.getHarness(CounterHarn.with({ count: 2 }));
    expect(counterWith2).toBeTruthy();
  });
});
```

## Testing Router

### RouterTestingHarness

```typescript
import { RouterTestingHarness } from '@angular/router/testing';
import { provideRouter } from '@angular/router';

describe('Router Navigation', () => {
  let harness: RouterTestingHarness;
  
  beforeEach(async () => {
    await TestBed.configureTestingModule({
      providers: [
        provideRouter([
          { path: '', component: Home },
          { path: 'users/:id', component: UserCmpt },
        ]),
      ],
    }).compileComponents();
    
    harness = await RouterTestingHarness.create();
  });
  
  it('should navigate to user page', async () => {
    const component = await harness.navigateByUrl('/users/123', UserCmpt);
    
    expect(component.id()).toBe('123');
  });
  
  it('should display user name', async () => {
    await harness.navigateByUrl('/users/123');
    
    expect(harness.routeNativeElement?.textContent).toContain('User 123');
  });
});
```

### Testing Guards

```typescript
describe('AuthGuard', () => {
  let authService: jasmine.SpyObj<Auth>;
  
  beforeEach(() => {
    authService = jasmine.createSpyObj('Auth', ['isAuthenticated']);
    
    TestBed.configureTestingModule({
      providers: [
        { provide: Auth, useValue: authService },
        provideRouter([
          { path: 'login', component: Login },
          { 
            path: 'dashboard', 
            component: Dashboard,
            canActivate: [authGuard],
          },
        ]),
      ],
    });
  });
  
  it('should allow access when authenticated', async () => {
    authService.isAuthenticated.and.returnValue(true);
    
    const harness = await RouterTestingHarness.create();
    await harness.navigateByUrl('/dashboard');
    
    expect(harness.routeNativeElement?.textContent).toContain('Dashboard');
  });
  
  it('should redirect to login when not authenticated', async () => {
    authService.isAuthenticated.and.returnValue(false);
    
    const harness = await RouterTestingHarness.create();
    await harness.navigateByUrl('/dashboard');
    
    expect(TestBed.inject(Router).url).toBe('/login');
  });
});
```

## Testing Forms

### Testing Signal Forms

```typescript
import { form, FormField, required, email } from '@angular/forms/signals';

@Component({
  imports: [FormField],
  template: `
    <form (submit)="onSubmit($event)">
      <input [formField]="loginForm.email" />
      <input [formField]="loginForm.password" type="password" />
      <button type="submit" [disabled]="loginForm().invalid()">Submit</button>
    </form>
  `,
})
export class Login {
  model = signal({ email: '', password: '' });
  loginForm = form(this.model, (schemaPath) => {
    required(schemaPath.email);
    email(schemaPath.email);
    required(schemaPath.password);
  });
  
  submitted = signal(false);
  
  onSubmit(event: Event) {
    event.preventDefault();
    if (this.loginForm().valid()) {
      this.submitted.set(true);
    }
  }
}

describe('Login', () => {
  let fixture: ComponentFixture<Login>;
  let component: Login;
  
  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [Login],
    }).compileComponents();
    
    fixture = TestBed.createComponent(Login);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });
  
  it('should be invalid when empty', () => {
    expect(component.loginForm().invalid()).toBeTrue();
  });
  
  it('should be valid with correct data', () => {
    component.model.set({
      email: 'test@example.com',
      password: 'password123',
    });
    
    expect(component.loginForm().valid()).toBeTrue();
  });
  
  it('should show email error for invalid email', () => {
    component.loginForm.email().value.set('invalid');
    fixture.detectChanges();
    
    expect(component.loginForm.email().invalid()).toBeTrue();
    expect(component.loginForm.email().errors().some(e => e.kind === 'email')).toBeTrue();
  });
  
  it('should disable submit button when invalid', () => {
    const button = fixture.nativeElement.querySelector('button');
    expect(button.disabled).toBeTrue();
  });
});
```

### Testing Reactive Forms

```typescript
describe('ReactiveForm', () => {
  it('should validate form', () => {
    const fixture = TestBed.createComponent(ProfileForm);
    const component = fixture.componentInstance;
    
    expect(component.form.valid).toBeFalse();
    
    component.form.patchValue({
      name: 'John',
      email: 'john@example.com',
    });
    
    expect(component.form.valid).toBeTrue();
  });
  
  it('should show validation errors', () => {
    const fixture = TestBed.createComponent(ProfileForm);
    fixture.detectChanges();
    
    const emailControl = fixture.componentInstance.form.controls.email;
    emailControl.setValue('invalid');
    emailControl.markAsTouched();
    fixture.detectChanges();
    
    const errorElement = fixture.nativeElement.querySelector('.error');
    expect(errorElement.textContent).toContain('Invalid email');
  });
});
```

## Testing Directives

### Attribute Directive

```typescript
@Directive({
  selector: '[appHighlight]',
  host: {
    '[style.backgroundColor]': 'color()',
  },
})
export class Highlight {
  color = input('yellow', { alias: 'appHighlight' });
}

describe('Highlight', () => {
  @Component({
    imports: [Highlight],
    template: `<p appHighlight="lightblue">Test</p>`,
  })
  class Test {}
  
  it('should apply background color', () => {
    const fixture = TestBed.createComponent(Test);
    fixture.detectChanges();
    
    const p = fixture.nativeElement.querySelector('p');
    expect(p.style.backgroundColor).toBe('lightblue');
  });
});
```

### Structural Directive

```typescript
@Directive({
  selector: '[appIf]',
})
export class If {
  private templateRef = inject(TemplateRef);
  private viewContainer = inject(ViewContainerRef);
  
  condition = input.required<boolean>({ alias: 'appIf' });
  
  constructor() {
    effect(() => {
      if (this.condition()) {
        this.viewContainer.createEmbeddedView(this.templateRef);
      } else {
        this.viewContainer.clear();
      }
    });
  }
}

describe('If', () => {
  @Component({
    imports: [If],
    template: `<p *appIf="show()">Visible</p>`,
  })
  class TestCmpt {
    show = signal(false);
  }
  
  it('should show content when condition is true', () => {
    const fixture = TestBed.createComponent(Test);
    fixture.detectChanges();
    
    expect(fixture.nativeElement.querySelector('p')).toBeNull();
    
    fixture.componentInstance.show.set(true);
    fixture.detectChanges();
    
    expect(fixture.nativeElement.querySelector('p')).toBeTruthy();
  });
});
```

## Testing Pipes

```typescript
@Pipe({ name: 'truncate' })
export class Truncate implements PipeTransform {
  transform(value: string, length: number = 50): string {
    if (value.length <= length) return value;
    return value.substring(0, length) + '...';
  }
}

describe('Truncate', () => {
  let pipe: Truncate;
  
  beforeEach(() => {
    pipe = new Truncate();
  });
  
  it('should not truncate short strings', () => {
    expect(pipe.transform('Hello', 10)).toBe('Hello');
  });
  
  it('should truncate long strings', () => {
    expect(pipe.transform('Hello World', 5)).toBe('Hello...');
  });
  
  it('should use default length', () => {
    const longString = 'a'.repeat(60);
    const result = pipe.transform(longString);
    expect(result.length).toBe(53); // 50 + '...'
  });
});
```

## E2E Testing Setup

### Playwright Configuration

```typescript
// playwright.config.ts
import { defineConfig } from '@playwright/test';

export default defineConfig({
  testDir: './e2e',
  fullyParallel: true,
  forbidOnly: !!process.env.CI,
  retries: process.env.CI ? 2 : 0,
  workers: process.env.CI ? 1 : undefined,
  reporter: 'html',
  use: {
    baseURL: 'http://localhost:4200',
    trace: 'on-first-retry',
  },
  webServer: {
    command: 'npm run start',
    url: 'http://localhost:4200',
    reuseExistingServer: !process.env.CI,
  },
});
```

### E2E Test Example

```typescript
// e2e/login.spec.ts
import { test, expect } from '@playwright/test';

test.describe('Login', () => {
  test('should login successfully', async ({ page }) => {
    await page.goto('/login');
    
    await page.fill('input[name="email"]', 'test@example.com');
    await page.fill('input[name="password"]', 'password123');
    await page.click('button[type="submit"]');
    
    await expect(page).toHaveURL('/dashboard');
    await expect(page.locator('h1')).toContainText('Welcome');
  });
  
  test('should show error for invalid credentials', async ({ page }) => {
    await page.goto('/login');
    
    await page.fill('input[name="email"]', 'wrong@example.com');
    await page.fill('input[name="password"]', 'wrongpassword');
    await page.click('button[type="submit"]');
    
    await expect(page.locator('.error')).toBeVisible();
    await expect(page.locator('.error')).toContainText('Invalid credentials');
  });
});
```

## Test Utilities

### Custom Test Helpers

```typescript
// test-utils.ts
export function setSignalInput<T>(
  fixture: ComponentFixture<any>,
  inputName: string,
  value: T
): void {
  fixture.componentRef.setInput(inputName, value);
  fixture.detectChanges();
}

export async function waitForSignal<T>(
  signal: () => T,
  predicate: (value: T) => boolean,
  timeout = 5000
): Promise<T> {
  const start = Date.now();
  while (Date.now() - start < timeout) {
    const value = signal();
    if (predicate(value)) return value;
    await new Promise(resolve => setTimeout(resolve, 10));
  }
  throw new Error('Timeout waiting for signal');
}

// Usage
it('should load data', async () => {
  const fixture = TestBed.createComponent(Data);
  fixture.detectChanges();
  
  await waitForSignal(
    () => fixture.componentInstance.data(),
    data => data !== undefined
  );
  
  expect(fixture.componentInstance.data()).toBeDefined();
});
```
```

## File: `skills/angular-testing/references/vitest-migration.md`
```markdown
# Vitest Setup and Migration Guide

## Vitest vs Jasmine Comparison

| Feature | Vitest | Jasmine/Karma |
|---------|--------|---------------|
| Speed | Faster (native ESM) | Slower |
| Watch mode | Instant feedback | Slower rebuilds |
| Mocking | `vi.fn()`, `vi.mock()` | `jasmine.createSpy()` |
| Assertions | `expect()` (Chai-style) | `expect()` (Jasmine) |
| UI | Built-in UI mode | Karma browser |
| Config | `angular.json` | `karma.conf.js` |

## Migration from Jasmine to Vitest

### Spy Migration

```typescript
// Jasmine
const spy = jasmine.createSpy('callback');
spy.and.returnValue('value');
expect(spy).toHaveBeenCalledWith('arg');

// Vitest
const spy = vi.fn();
spy.mockReturnValue('value');
expect(spy).toHaveBeenCalledWith('arg');
```

### SpyOn Migration

```typescript
// Jasmine
spyOn(service, 'method').and.returnValue(of(data));

// Vitest
vi.spyOn(service, 'method').mockReturnValue(of(data));
```

### createSpyObj Migration

```typescript
// Jasmine
const mockService = jasmine.createSpyObj('UserService', ['getUser', 'updateUser']);
mockService.getUser.and.returnValue(of({ id: '1', name: 'Test' }));

// Vitest
const mockService = {
  getUser: vi.fn(),
  updateUser: vi.fn(),
};
mockService.getUser.mockReturnValue(of({ id: '1', name: 'Test' }));
```

### Async Testing Migration

```typescript
// Jasmine - using done callback
it('should load data', (done) => {
  service.loadData().subscribe(data => {
    expect(data).toBeDefined();
    done();
  });
});

// Vitest - using async/await
it('should load data', async () => {
  const data = await firstValueFrom(service.loadData());
  expect(data).toBeDefined();
});
```

### Clock/Timer Migration

```typescript
// Jasmine
jasmine.clock().install();
jasmine.clock().tick(1000);
jasmine.clock().uninstall();

// Vitest
vi.useFakeTimers();
vi.advanceTimersByTime(1000);
vi.useRealTimers();
```

## Vitest Configuration Details

### Full angular.json Configuration

```json
{
  "projects": {
    "your-app": {
      "architect": {
        "test": {
          "builder": "@angular/build:unit-test",
          "options": {
            "tsConfig": "tsconfig.spec.json",
            "buildTarget": "your-app:build"
          }
        }
      }
    }
  }
}
```

### tsconfig.spec.json

```json
{
  "extends": "./tsconfig.json",
  "compilerOptions": {
    "types": ["vitest/globals"]
  },
  "include": ["src/**/*.spec.ts"]
}
```

### Optional vite.config.ts

For advanced configuration, create a `vite.config.ts`:

```typescript
import { defineConfig } from 'vitest/config';

export default defineConfig({
  test: {
    globals: true,
    environment: 'jsdom',
    include: ['src/**/*.spec.ts'],
    coverage: {
      provider: 'v8',
      reporter: ['text', 'html', 'lcov'],
      exclude: [
        'node_modules/',
        'src/test-setup.ts',
        '**/*.spec.ts',
        '**/*.d.ts',
      ],
    },
  },
});
```

## Running Vitest

```bash
# Run tests
ng test

# Watch mode
ng test --watch

# Coverage
ng test --code-coverage

# Run specific file pattern
ng test --include='**/user*.spec.ts'

# CI mode (single run)
ng test --watch=false
```
```

## File: `skills/angular-tooling/SKILL.md`
```markdown
---
name: angular-tooling
description: Use Angular CLI and development tools effectively in Angular v20+ projects. Use for project setup, code generation, building, testing, and configuration. Triggers on creating new projects, generating components/services/modules, configuring builds, running tests, or optimizing production builds. Don't use for Nx workspace commands, custom Webpack configurations, or non-Angular CLI build systems like Vite standalone or esbuild direct usage.
---

# Angular Tooling

Use Angular CLI and development tools for efficient Angular v20+ development.

## Project Setup

### Create New Project

```bash
# Create new standalone project (default in v20+)
ng new my-app

# With specific options
ng new my-app --style=scss --routing --ssr=false

# Skip tests
ng new my-app --skip-tests

# Minimal setup
ng new my-app --minimal --inline-style --inline-template
```

### Project Structure

```
my-app/
├── src/
│   ├── app/
│   │   ├── app.component.ts
│   │   ├── app.config.ts
│   │   └── app.routes.ts
│   ├── index.html
│   ├── main.ts
│   └── styles.scss
├── public/                  # Static assets
├── angular.json             # CLI configuration
├── package.json
├── tsconfig.json
└── tsconfig.app.json
```

## Code Generation

### Components

```bash
# Generate component
ng generate component features/user-profile
ng g c features/user-profile  # Short form

# With options
ng g c shared/button --inline-template --inline-style
ng g c features/dashboard --skip-tests
ng g c features/settings --change-detection=OnPush

# Flat (no folder)
ng g c shared/icon --flat

# Dry run (preview)
ng g c features/checkout --dry-run
```

### Services

```bash
# Generate service (providedIn: 'root' by default)
ng g service services/auth
ng g s services/user

# Skip tests
ng g s services/api --skip-tests
```

### Other Schematics

```bash
# Directive
ng g directive directives/highlight
ng g d directives/tooltip

# Pipe
ng g pipe pipes/truncate
ng g p pipes/date-format

# Guard (functional by default)
ng g guard guards/auth

# Interceptor (functional by default)
ng g interceptor interceptors/auth

# Interface
ng g interface models/user

# Enum
ng g enum models/status

# Class
ng g class models/product
```

### Generate with Path Alias

```bash
# Components in feature folders
ng g c @features/products/product-list
ng g c @shared/ui/button
```

## Development Server

```bash
# Start dev server
ng serve
ng s  # Short form

# With options
ng serve --port 4201
ng serve --open  # Open browser
ng serve --host 0.0.0.0  # Expose to network

# Production mode locally
ng serve --configuration=production

# With SSL
ng serve --ssl --ssl-key ./ssl/key.pem --ssl-cert ./ssl/cert.pem
```

## Building

### Development Build

```bash
ng build
```

### Production Build

```bash
ng build --configuration=production
ng build -c production  # Short form

# With specific options
ng build -c production --source-map=false
ng build -c production --named-chunks
```

### Build Output

```
dist/my-app/
├── browser/
│   ├── index.html
│   ├── main-[hash].js
│   ├── polyfills-[hash].js
│   └── styles-[hash].css
└── server/              # If SSR enabled
    └── main.js
```

## Testing

### Unit Tests

```bash
# Run tests
ng test
ng t  # Short form

# Single run (CI)
ng test --watch=false --browsers=ChromeHeadless

# With coverage
ng test --code-coverage

# Specific file
ng test --include=**/user.service.spec.ts
```

### E2E Tests

```bash
# Run e2e (if configured)
ng e2e
```

## Linting

```bash
# Run linter
ng lint

# Fix auto-fixable issues
ng lint --fix
```

## Configuration

### angular.json Key Sections

```json
{
  "projects": {
    "my-app": {
      "architect": {
        "build": {
          "builder": "@angular-devkit/build-angular:application",
          "options": {
            "outputPath": "dist/my-app",
            "index": "src/index.html",
            "browser": "src/main.ts",
            "polyfills": ["zone.js"],
            "tsConfig": "tsconfig.app.json",
            "assets": ["{ \"glob\": \"**/*\", \"input\": \"public\" }"],
            "styles": ["src/styles.scss"],
            "scripts": []
          },
          "configurations": {
            "production": {
              "budgets": [
                {
                  "type": "initial",
                  "maximumWarning": "500kB",
                  "maximumError": "1MB"
                }
              ],
              "outputHashing": "all"
            },
            "development": {
              "optimization": false,
              "extractLicenses": false,
              "sourceMap": true
            }
          }
        }
      }
    }
  }
}
```

### Environment Configuration

```typescript
// src/environments/environment.ts
export const environment = {
  production: false,
  apiUrl: 'http://localhost:3000/api',
};

// src/environments/environment.prod.ts
export const environment = {
  production: true,
  apiUrl: 'https://api.example.com',
};
```

Configure in angular.json:

```json
{
  "configurations": {
    "production": {
      "fileReplacements": [
        {
          "replace": "src/environments/environment.ts",
          "with": "src/environments/environment.prod.ts"
        }
      ]
    }
  }
}
```

## Adding Libraries

### Angular Libraries

```bash
# Add Angular Material
ng add @angular/material

# Add Angular PWA
ng add @angular/pwa

# Add Angular SSR
ng add @angular/ssr

# Add Angular Localize
ng add @angular/localize
```

### Third-Party Libraries

```bash
# Install and configure
npm install @ngrx/signals

# Some libraries have schematics
ng add @ngrx/store
```

## Update Angular

```bash
# Check for updates
ng update

# Update Angular core and CLI
ng update @angular/core @angular/cli

# Update all packages
ng update --all

# Force update (skip peer dependency checks)
ng update @angular/core @angular/cli --force
```

## Performance Analysis

```bash
# Build with stats
ng build -c production --stats-json

# Analyze bundle (install esbuild-visualizer)
npx esbuild-visualizer --metadata dist/my-app/browser/stats.json --open
```

## Caching

```bash
# Enable persistent build cache (default in v20+)
# Configured in angular.json:
{
  "cli": {
    "cache": {
      "enabled": true,
      "path": ".angular/cache",
      "environment": "all"
    }
  }
}

# Clear cache
rm -rf .angular/cache
```

For advanced configuration, see [references/tooling-patterns.md](references/tooling-patterns.md).
```

## File: `skills/angular-tooling/references/tooling-patterns.md`
```markdown
# Angular Tooling Patterns

## Table of Contents
- [Custom Schematics](#custom-schematics)
- [Build Optimization](#build-optimization)
- [Multi-Project Workspace](#multi-project-workspace)
- [CI/CD Configuration](#cicd-configuration)
- [Path Aliases](#path-aliases)
- [Proxy Configuration](#proxy-configuration)

## Custom Schematics

### Generate Schematic Collection

```bash
# Install schematics CLI
npm install -g @angular-devkit/schematics-cli

# Create schematic collection
schematics blank --name=my-schematics
```

### Simple Component Schematic

```typescript
// src/my-component/index.ts
import { Rule, SchematicContext, Tree, apply, url, template, move, mergeWith } from '@angular-devkit/schematics';
import { strings } from '@angular-devkit/core';

export function myComponent(options: { name: string; path: string }): Rule {
  return (tree: Tree, context: SchematicContext) => {
    const templateSource = apply(url('./files'), [
      template({
        ...options,
        ...strings,
      }),
      move(options.path),
    ]);
    
    return mergeWith(templateSource)(tree, context);
  };
}
```

### Use Custom Schematics

```bash
# Link locally
npm link ./my-schematics

# Use
ng generate my-schematics:my-component --name=test --path=src/app
```

## Build Optimization

### Budget Configuration

```json
{
  "budgets": [
    {
      "type": "initial",
      "maximumWarning": "500kB",
      "maximumError": "1MB"
    },
    {
      "type": "anyComponentStyle",
      "maximumWarning": "4kB",
      "maximumError": "8kB"
    },
    {
      "type": "anyScript",
      "maximumWarning": "100kB",
      "maximumError": "200kB"
    }
  ]
}
```

### Differential Loading

Automatic in v20+ - builds for modern browsers by default.

```json
// .browserslistrc
last 2 Chrome versions
last 2 Firefox versions
last 2 Safari versions
last 2 Edge versions
```

### Code Splitting

```typescript
// Lazy load routes for automatic code splitting
export const routes: Routes = [
  {
    path: 'admin',
    loadChildren: () => import('./admin/admin.routes').then(m => m.adminRoutes),
  },
  {
    path: 'reports',
    loadComponent: () => import('./reports/reports.component').then(m => m.Reports),
  },
];
```

### Tree Shaking

Ensure proper imports for tree shaking:

```typescript
// Good - tree shakeable
import { map, filter } from 'rxjs';

// Avoid - imports entire library
import * as rxjs from 'rxjs';
```

### Preload Strategy

```typescript
// app.config.ts
import { provideRouter, withPreloading, PreloadAllModules } from '@angular/router';

export const appConfig: ApplicationConfig = {
  providers: [
    provideRouter(routes, withPreloading(PreloadAllModules)),
  ],
};
```

## Multi-Project Workspace

### Create Workspace

```bash
# Create empty workspace
ng new my-workspace --create-application=false

cd my-workspace

# Add applications
ng generate application main-app
ng generate application admin-app

# Add library
ng generate library shared-ui
ng generate library data-access
```

### Workspace Structure

```
my-workspace/
├── projects/
│   ├── main-app/
│   │   └── src/
│   ├── admin-app/
│   │   └── src/
│   ├── shared-ui/
│   │   └── src/
│   └── data-access/
│       └── src/
├── angular.json
└── package.json
```

### Build Specific Project

```bash
ng build main-app
ng build shared-ui
ng serve admin-app
```

### Library Configuration

```json
// projects/shared-ui/ng-package.json
{
  "$schema": "../../node_modules/ng-packagr/ng-package.schema.json",
  "dest": "../../dist/shared-ui",
  "lib": {
    "entryFile": "src/public-api.ts"
  }
}
```

### Using Library in App

```typescript
// After building library: ng build shared-ui
import { Button } from 'shared-ui';

@Component({
  imports: [Button],
  template: `<lib-button>Click</lib-button>`,
})
export class App {}
```

## CI/CD Configuration

### GitHub Actions

```yaml
# .github/workflows/ci.yml
name: CI

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v4
      
      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm'
      
      - name: Install dependencies
        run: npm ci
      
      - name: Lint
        run: npm run lint
      
      - name: Test
        run: npm run test -- --watch=false --browsers=ChromeHeadless --code-coverage
      
      - name: Build
        run: npm run build -- -c production
      
      - name: Upload coverage
        uses: codecov/codecov-action@v3
        with:
          files: ./coverage/lcov.info
```

### GitLab CI

```yaml
# .gitlab-ci.yml
image: node:20

cache:
  paths:
    - node_modules/
    - .angular/cache/

stages:
  - install
  - test
  - build

install:
  stage: install
  script:
    - npm ci

test:
  stage: test
  script:
    - npm run lint
    - npm run test -- --watch=false --browsers=ChromeHeadless

build:
  stage: build
  script:
    - npm run build -- -c production
  artifacts:
    paths:
      - dist/
```

## Path Aliases

### Configure tsconfig.json

```json
{
  "compilerOptions": {
    "baseUrl": ".",
    "paths": {
      "@app/*": ["src/app/*"],
      "@env/*": ["src/environments/*"],
      "@shared/*": ["src/app/shared/*"],
      "@features/*": ["src/app/features/*"],
      "@core/*": ["src/app/core/*"]
    }
  }
}
```

### Usage

```typescript
// Instead of relative imports
import { User } from '../../../core/services/user.service';

// Use path alias
import { User } from '@core/services/user.service';
```

## Proxy Configuration

### Development Proxy

```json
// proxy.conf.json
{
  "/api": {
    "target": "http://localhost:3000",
    "secure": false,
    "changeOrigin": true
  },
  "/auth": {
    "target": "http://localhost:4000",
    "secure": false,
    "pathRewrite": {
      "^/auth": ""
    }
  }
}
```

### Configure in angular.json

```json
{
  "serve": {
    "options": {
      "proxyConfig": "proxy.conf.json"
    }
  }
}
```

### Or via CLI

```bash
ng serve --proxy-config proxy.conf.json
```

## Custom Builders

### Using esbuild (Default in v20+)

```json
{
  "architect": {
    "build": {
      "builder": "@angular-devkit/build-angular:application",
      "options": {
        "browser": "src/main.ts"
      }
    }
  }
}
```

### SSR Configuration

```bash
# Add SSR
ng add @angular/ssr
```

```json
{
  "architect": {
    "build": {
      "options": {
        "server": "src/main.server.ts",
        "prerender": true,
        "ssr": {
          "entry": "server.ts"
        }
      }
    }
  }
}
```

## Debugging

### Source Maps

```json
{
  "configurations": {
    "development": {
      "sourceMap": true
    },
    "production": {
      "sourceMap": {
        "scripts": true,
        "styles": false,
        "hidden": true,
        "vendor": false
      }
    }
  }
}
```

### Verbose Logging

```bash
ng build --verbose
ng serve --verbose
```

### Debug Tests

```bash
# Run tests with debugging
ng test --browsers=Chrome

# In Chrome DevTools, open Sources tab and set breakpoints
```

## Package Scripts

```json
{
  "scripts": {
    "start": "ng serve",
    "build": "ng build",
    "build:prod": "ng build -c production",
    "test": "ng test",
    "test:ci": "ng test --watch=false --browsers=ChromeHeadless --code-coverage",
    "lint": "ng lint",
    "lint:fix": "ng lint --fix",
    "analyze": "ng build -c production --stats-json && npx esbuild-visualizer --metadata dist/my-app/browser/stats.json --open",
    "update": "ng update"
  }
}
```
```


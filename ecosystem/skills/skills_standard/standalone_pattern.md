---
id: standalone-pattern
type: document
owner: SYSTEM
tags: [auto-healed]
healed_at: 2026-04-03T22:46:24.976260
---

# Standalone Pattern

## Component

```typescript
import { Component, input, output } from '@angular/core';
import { CommonModule } from '@angular/common';
import { MatButtonModule } from '@angular/material/button';

@Component({
  selector: 'app-user-card',
  standalone: true,
  imports: [CommonModule, MatButtonModule],
  template: `
    <div class="card">
      <h2>{{ name() }}</h2>
      <button mat-button (click)="onSelect()">Select</button>
    </div>
  `,
})
export class UserCardComponent {
  // Signal Input
  name = input.required<string>();

  // Output Function
  select = output<void>();

  onSelect() {
    this.select.emit();
  }
}
```

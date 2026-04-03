---
id: composition
type: document
owner: SYSTEM
tags: [auto-healed]
healed_at: 2026-04-03T22:46:23.818067
---

# Composition w/ HostDirectives

## Host Directives

Compose behaviors.

```typescript
@Directive({
  selector: '[appTooltip]',
  standalone: true
})
export class TooltipDirective { ... }

@Component({
  selector: 'app-button',
  standalone: true,
  template: `<button><ng-content/></button>`,
  hostDirectives: [
    {
      directive: TooltipDirective,
      inputs: ['tooltip'], // Alias input
      outputs: ['tooltipShow']
    }
  ]
})
export class ButtonComponent {
  // Now <app-button> automatically has tooltip capability
}
```

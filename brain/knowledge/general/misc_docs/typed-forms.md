---
id: typed-forms
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:31:24.175211
---

# Typed Forms

## Definition

```typescript
interface LoginForm {
  email: FormControl<string>;
  password: FormControl<string>;
  rememberMe: FormControl<boolean>;
}

@Component({...})
export class LoginComponent {
  fb = inject(FormBuilder).nonNullable;

  form: FormGroup<LoginForm> = this.fb.group({
    email: ['', [Validators.required, Validators.email]],
    password: ['', [Validators.required, Validators.minLength(8)]],
    rememberMe: [false]
  });

  submit() {
    if (this.form.valid) {
      // value is strictly typed: { email: string, ... }
      const value = this.form.getRawValue();
    }
  }
}
```

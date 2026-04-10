---
id: error-wrapping
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:21.985800
---

# Error Wrapping Patterns

## Adding Context

```go
func ReadConfig() error {
    file, err := os.Open("config.json")
    if err != nil {
        return fmt.Errorf("failed to open config: %w", err)
    }
    // ...
}
```

## Checking Errors (Is)

```go
if errors.Is(err, os.ErrNotExist) {
    // Handle file missing
}
```

## Extracting Errors (As)

```go
var pathErr *fs.PathError
if errors.As(err, &pathErr) {
    fmt.Println("failed at path:", pathErr.Path)
}
```

## Custom Error Type

```go
type ValidationError struct {
    Field string
    Msg   string
}

func (e *ValidationError) Error() string {
    return fmt.Sprintf("%s: %s", e.Field, e.Msg)
}

// Usage
return &ValidationError{Field: "email", Msg: "invalid format"}
```

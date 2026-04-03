---
id: lmittmann-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:29:05.475508
---

# KNOWLEDGE EXTRACT: lmittmann
> **Extracted on:** 2026-03-30 17:42:01
> **Source:** lmittmann

---

## File: `tint.md`
```markdown
# 📦 lmittmann/tint [🔖 PENDING/APPROVE]
🔗 https://github.com/lmittmann/tint
🌐 https://pkg.go.dev/github.com/lmittmann/tint

## Meta
- **Stars:** ⭐ 1257 | **Forks:** 🍴 63
- **Language:** Go | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
🌈 slog.Handler that writes tinted (colorized) logs

## README (trích đầu)
```
# `tint`: 🌈 **slog.Handler** that writes tinted logs

[![Go Reference](https://pkg.go.dev/badge/github.com/lmittmann/tint.svg)](https://pkg.go.dev/github.com/lmittmann/tint#section-documentation)
[![Go Report Card](https://goreportcard.com/badge/github.com/lmittmann/tint)](https://goreportcard.com/report/github.com/lmittmann/tint)

<picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://github.com/lmittmann/tint/assets/3458786/3d42f8d5-8bdf-40db-a16a-1939c88689cb">
    <source media="(prefers-color-scheme: light)" srcset="https://github.com/lmittmann/tint/assets/3458786/3d42f8d5-8bdf-40db-a16a-1939c88689cb">
    <img src="https://github.com/lmittmann/tint/assets/3458786/3d42f8d5-8bdf-40db-a16a-1939c88689cb">
</picture>
<br>
<br>

Package `tint` implements a zero-dependency [`slog.Handler`](https://pkg.go.dev/log/slog#Handler)
that writes tinted (colorized) logs. Its output format is inspired by the `zerolog.ConsoleWriter` and
[`slog.TextHandler`](https://pkg.go.dev/log/slog#TextHandler).

The output format can be customized using [`Options`](https://pkg.go.dev/github.com/lmittmann/tint#Options)
which is a drop-in replacement for [`slog.HandlerOptions`](https://pkg.go.dev/log/slog#HandlerOptions).

```
go get github.com/lmittmann/tint
```

## Usage

```go
w := os.Stderr

// Create a new logger
logger := slog.New(tint.NewHandler(w, nil))

// Set global logger with custom options
slog.SetDefault(slog.New(
    tint.NewHandler(w, &tint.Options{
        Level:      slog.LevelDebug,
        TimeFormat: time.Kitchen,
    }),
))
```

### Customize Attributes

`ReplaceAttr` can be used to alter or drop attributes. If set, it is called on
each non-group attribute before it is logged. See [`slog.HandlerOptions`](https://pkg.go.dev/log/slog#HandlerOptions)
for details.

```go
// Create a new logger with a custom TRACE level:
const LevelTrace = slog.LevelDebug - 4

w := os.Stderr
logger := slog.New(tint.NewHandler(w, &tint.Options{
    Level: LevelTrace,
    ReplaceAttr: func(groups []string, a slog.Attr) slog.Attr {
        if a.Key == slog.LevelKey && len(groups) == 0 {
            level, ok := a.Value.Any().(slog.Level)
            if ok && level <= LevelTrace {
                return tint.Attr(13, slog.String(a.Key, "TRC"))
            }
        }
        return a
    },
}))
```

```go
// Create a new logger that doesn't write the time
w := os.Stderr
logger := slog.New(
    tint.NewHandler(w, &tint.Options{
        ReplaceAttr: func(groups []string, a slog.Attr) slog.Attr {
            if a.Key == slog.TimeKey && len(groups) == 0 {
                return slog.Attr{}
            }
            return a
        },
    }),
)
```

```go
// Create a new logger that writes all errors in red
w := os.Stderr
logger := slog.New(
    tint.NewHandler(w, &tint.Options{
        ReplaceAttr: func(groups []string, a slog.Attr) slog.Attr {
            if a.Value.Kind() == slog.KindAny {
                if _, ok := a.Value.Any().(error); ok {
             
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```


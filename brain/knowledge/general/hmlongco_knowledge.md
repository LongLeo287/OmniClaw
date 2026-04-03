---
id: hmlongco-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:52.344185
---

# KNOWLEDGE EXTRACT: hmlongco
> **Extracted on:** 2026-03-30 17:38:07
> **Source:** hmlongco

---

## File: `Factory.md`
```markdown
# 📦 hmlongco/Factory [🔖 PENDING/APPROVE]
🔗 https://github.com/hmlongco/Factory


## Meta
- **Stars:** ⭐ 2789 | **Forks:** 🍴 178
- **Language:** Swift | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
A modern approach to Container-Based Dependency Injection for Swift and SwiftUI.

## README (trích đầu)
```
[![](https://img.shields.io/endpoint?url=https%3A%2F%2Fswiftpackageindex.com%2Fapi%2Fpackages%2Fhmlongco%2FFactory%2Fbadge%3Ftype%3Dswift-versions)](https://swiftpackageindex.com/hmlongco/Factory)
[![](https://img.shields.io/endpoint?url=https%3A%2F%2Fswiftpackageindex.com%2Fapi%2Fpackages%2Fhmlongco%2FFactory%2Fbadge%3Ftype%3Dplatforms)](https://swiftpackageindex.com/hmlongco/Factory)

![](https://github.com/hmlongco/Factory/blob/main/Logo.png?raw=true)

A modern approach to Container-Based Dependency Injection for Swift and SwiftUI.

## Factory Version 2.5.3

Factory is strongly influenced by SwiftUI, and in my opinion is highly suited for that environment. Factory is...

- **Adaptable**: Factory doesn't tie you down to a single dependency injection strategy or technique.
- **Powerful**: Factory supports containers, scopes, passed parameters, contexts, decorators, unit tests, SwiftUI Previews, and much, much more.
- **Performant**: Little to no setup time is needed for the vast majority of your services, resolutions are extremely fast, and no compile-time scripts or build phases are needed.
- **Safe**: Factory is compile-time safe; a factory for a given type must exist or the code simply will not compile.
- **Concise**: Defining a registration usually takes just a single line of code. Same for resolution.
- **Flexible**: Working with UIKIt or SwiftUI? iOS or macOS? Using MVVM? MVP? Clean? VIPER? No problem. Factory works with all of these and more.
- **Documented**: Factory has extensive DocC documentation and examples covering its classes, methods, and use cases.
- **Lightweight**: With all of that Factory is slim and trim, under 1,000 lines of executable code.
- **Tested**: Unit tests with 100% code coverage helps ensure correct operation of registrations, resolutions, and scopes.
- **Testable**: Factory ensures your application's views and services are easily previewable and testable. 
- **Free**: Factory is free and open source under the MIT License.

Sound too good to be true? Let's take a look.

---

But before we do, I want to express my thanks to Mercedes-Benz, Süddeutsche Zeitung, and everyone else who's sponsored my open source work! [You folks help make this possible.](https://github.com/sponsors/hmlongco)

---

## A Simple Factory
 
Most container-based dependency injection systems require you to define in some way that a given service type is available for injection, and many require some sort of factory or mechanism that will provide a new instance of the service when needed.
 
 Factory is no exception. Here's a simple dependency registration that returns a service that conforms to `MyServiceType`.
 
```swift
extension Container {
    var myService: Factory<MyServiceType> { 
        Factory(self) { MyService() }
    }
}
```

Unlike frameworks that require registering every single type up front, or SwiftUI, where defining a new environment variable requires creating a new EnvironmentKey and adding additional getters and setters, he
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```


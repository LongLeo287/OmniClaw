# Knowledge Dump for clean-architecture-swiftui

## File: .swiftlint.yml
```
disabled_rules: # rule identifiers to exclude from running
#  - colon
#  - comma
#  - control_statement
#  - file_length
#  - force_cast
#  - force_try
#  - function_body_length
#  - leading_whitespace
#  - line_length
  - nesting
  - large_tuple
  - unused_closure_parameter
#  - opening_brace
#  - operator_whitespace
#  - return_arrow_whitespace
#  - statement_position
#  - todo
#  - trailing_newline
#  - trailing_semicolon
  - trailing_whitespace
#  - type_body_length
  - type_name
  - xctfail_message
#  - variable_name_max_length
#  - variable_name_min_length
#  - variable_name
#included: # paths to include during linting. `--path` is ignored if present. takes precendence over `excluded`.

excluded: # paths to ignore during linting. overridden by `included`.
  - Carthage
  - Pods
  - Modules

identifier_name:
  min_length: 2
```

## File: .travis.yml
```
os: osx
language: swift
osx_image: xcode12.3
xcode_project: CountriesSwiftUI.xcodeproj
xcode_scheme: CountriesSwiftUI
xcode_sdk: iphonesimulator14.2
xcode_destination: platform=iOS Simulator,OS=14.2,name=iPhone 8
after_success:
  - bash <(curl -s https://codecov.io/bash)

```

## File: README.md
```
### Articles related to this project

* [Clean Architecture for SwiftUI](https://nalexn.github.io/clean-architecture-swiftui/?utm_source=nalexn_github)
* [Programmatic navigation in SwiftUI project](https://nalexn.github.io/swiftui-deep-linking/?utm_source=nalexn_github)
* [Separation of Concerns in Software Design](https://nalexn.github.io/separation-of-concerns/?utm_source=nalexn_github)

---

# Clean Architecture for SwiftUI + Combine

A demo project showcasing the setup of the SwiftUI app with Clean Architecture.

The app uses the [restcountries.com](https://restcountries.com/) REST API to show the list of countries and details about them.

**Check out [mvvm branch](https://github.com/nalexn/clean-architecture-swiftui/tree/mvvm) for the MVVM revision of the same app.**

For the example of handling the **authentication state** in the app, you can refer to my [other tiny project](https://github.com/nalexn/uikit-swiftui) that harnesses the locks and keys principle for solving this problem.

![platforms](https://img.shields.io/badge/platforms-iPhone%20%7C%20iPad%20%7C%20macOS-lightgrey) [![codecov](https://codecov.io/gh/nalexn/clean-architecture-swiftui/branch/master/graph/badge.svg)](https://codecov.io/gh/nalexn/clean-architecture-swiftui) [![codebeat badge](https://codebeat.co/badges/db33561b-0b2b-4ee1-a941-a08efbd0ebd7)](https://codebeat.co/projects/github-com-nalexn-clean-architecture-swiftui-master)

<p align="center">
  <img src="https://github.com/nalexn/blob_files/blob/master/images/countries_preview.png?raw=true" alt="Diagram"/>
</p>

## Key features
* End of 2024 update: the project was fully revamped to use modern iOS stack technologies
* Decoupled **Presentation**, **Business Logic**, and **Data Access** layers
* Programmatic navigation. Push notifications with deep link
* Redux-like centralized `AppState` as the single source of truth
* Native SwiftUI dependency injection
* Handling of the system events (such as `didBecomeActive`, `willResignActive`)
* Full test coverage, including the UI (thanks to the [ViewInspector](https://github.com/nalexn/ViewInspector))
* Simple yet flexible networking layer built on async - await
* UI - vanilla **SwiftUI** + **Combine**
* Data persistence with **SwiftData**

## Architecture overview

<p align="center">
  <img src="https://github.com/nalexn/blob_files/blob/master/images/swiftui_arc_001.png?raw=true" alt="Diagram"/>
</p>

### Presentation Layer

**SwiftUI views** that contain no business logic and are a function of the state.

Side effects are triggered by the user's actions (such as a tap on a button) or view lifecycle event `onAppear` and are forwarded to the `Interactors`.

State and business logic layer (`AppState` + `Interactors`) are natively injected into the view hierarchy with `@Environment`.

### Business Logic Layer

Business Logic Layer is represented by `Interactors`. 

Interactors receive requests to perform work, such as obtaining data from an external source or making computations, but they never return data back directly.

Instead, they forward the result to the `AppState` or to a `Binding`. The latter is used when the result of work (the data) is used locally by one View and does not belong to the `AppState`.

[Previously](https://github.com/nalexn/clean-architecture-swiftui/releases/tag/1.0), this app did not use CoreData for persistence, and all loaded data were stored in the `AppState`.

With the persistence layer in place we have a choice - either to load the DB content onto the `AppState`, or serve the data from `Interactors` on an on-demand basis through `Binding`.

The first option suits best when you don't have a lot of data, for example, when you just store the last used login email in the `UserDefaults`. Then, the corresponding string value can just be loaded onto the `AppState` at launch and updated by the `Interactor` when the user changes the input.

The second option is better when you have massive amounts of data and introduce a fully-fledged database for storing it locally.

### Data Access Layer

Data Access Layer is represented by `Repositories`.

Repositories provide asynchronous API (`Publisher` from Combine) for making [CRUD](https://en.wikipedia.org/wiki/Create,_read,_update_and_delete) operations on the backend or a local database. They don't contain business logic, neither do they mutate the `AppState`. Repositories are accessible and used only by the Interactors.

---

[![Twitter](https://img.shields.io/badge/twitter-nallexn-blue)](https://twitter.com/nallexn) [![blog](https://img.shields.io/badge/blog-github-blue)](https://nalexn.github.io/?utm_source=nalexn_github)

```

## File: _GIT_INGEST.md
```
# OmniClaw Repo Plow: CIV_FETCHED_clean-architecture-swiftui_142938



================================================
FILE: README.md
================================================
### Articles related to this project

* [Clean Architecture for SwiftUI](https://nalexn.github.io/clean-architecture-swiftui/?utm_source=nalexn_github)
* [Programmatic navigation in SwiftUI project](https://nalexn.github.io/swiftui-deep-linking/?utm_source=nalexn_github)
* [Separation of Concerns in Software Design](https://nalexn.github.io/separation-of-concerns/?utm_source=nalexn_github)

---

# Clean Architecture for SwiftUI + Combine

A demo project showcasing the setup of the SwiftUI app with Clean Architecture.

The app uses the [restcountries.com](https://restcountries.com/) REST API to show the list of countries and details about them.

**Check out [mvvm branch](https://github.com/nalexn/clean-architecture-swiftui/tree/mvvm) for the MVVM revision of the same app.**

For the example of handling the **authentication state** in the app, you can refer to my [other tiny project](https://github.com/nalexn/uikit-swiftui) that harnesses the locks and keys principle for solving this problem.

![platforms](https://img.shields.io/badge/platforms-iPhone%20%7C%20iPad%20%7C%20macOS-lightgrey) [![codecov](https://codecov.io/gh/nalexn/clean-architecture-swiftui/branch/master/graph/badge.svg)](https://codecov.io/gh/nalexn/clean-architecture-swiftui) [![codebeat badge](https://codebeat.co/badges/db33561b-0b2b-4ee1-a941-a08efbd0ebd7)](https://codebeat.co/projects/github-com-nalexn-clean-architecture-swiftui-master)

<p align="center">
  <img src="https://github.com/nalexn/blob_files/blob/master/images/countries_preview.png?raw=true" alt="Diagram"/>
</p>

## Key features
* End of 2024 update: the project was fully revamped to use modern iOS stack technologies
* Decoupled **Presentation**, **Business Logic**, and **Data Access** layers
* Programmatic navigation. Push notifications with deep link
* Redux-like centralized `AppState` as the single source of truth
* Native SwiftUI dependency injection
* Handling of the system events (such as `didBecomeActive`, `willResignActive`)
* Full test coverage, including the UI (thanks to the [ViewInspector](https://github.com/nalexn/ViewInspector))
* Simple yet flexible networking layer built on async - await
* UI - vanilla **SwiftUI** + **Combine**
* Data persistence with **SwiftData**

## Architecture overview

<p align="center">
  <img src="https://github.com/nalexn/blob_files/blob/master/images/swiftui_arc_001.png?raw=true" alt="Diagram"/>
</p>

### Presentation Layer

**SwiftUI views** that contain no business logic and are a function of the state.

Side effects are triggered by the user's actions (such as a tap on a button) or view lifecycle event `onAppear` and are forwarded to the `Interactors`.

State and business logic layer (`AppState` + `Interactors`) are natively injected into the view hierarchy with `@Environment`.

### Business Logic Layer

Business Logic Layer is represented by `Interactors`. 

Interactors receive requests to perform work, such as obtaining data from an external source or making computations, but they never return data back directly.

Instead, they forward the result to the `AppState` or to a `Binding`. The latter is used when the result of work (the data) is used locally by one View and does not belong to the `AppState`.

[Previously](https://github.com/nalexn/clean-architecture-swiftui/releases/tag/1.0), this app did not use CoreData for persistence, and all loaded data were stored in the `AppState`.

With the persistence layer in place we have a choice - either to load the DB content onto the `AppState`, or serve the data from `Interactors` on an on-demand basis through `Binding`.

The first option suits best when you don't have a lot of data, for example, when you just store the last used login email in the `UserDefaults`. Then, the corresponding string value can just be loaded onto the `AppState` at launch and updated by the `Interactor` when the user changes the input.

The second option is better when you have massive amounts of data and introduce a fully-fledged database for storing it locally.

### Data Access Layer

Data Access Layer is represented by `Repositories`.

Repositories provide asynchronous API (`Publisher` from Combine) for making [CRUD](https://en.wikipedia.org/wiki/Create,_read,_update_and_delete) operations on the backend or a local database. They don't contain business logic, neither do they mutate the `AppState`. Repositories are accessible and used only by the Interactors.

---

[![Twitter](https://img.shields.io/badge/twitter-nallexn-blue)](https://twitter.com/nallexn) [![blog](https://img.shields.io/badge/blog-github-blue)](https://nalexn.github.io/?utm_source=nalexn_github)


================================================
FILE: CountriesSwiftUI\Resources\Assets.xcassets\Contents.json
================================================
{
  "info" : {
    "author" : "xcode",
    "version" : 1
  }
}


================================================
FILE: CountriesSwiftUI\Resources\Assets.xcassets\AccentColor.colorset\Contents.json
================================================
{
  "colors" : [
    {
      "idiom" : "universal"
    }
  ],
  "info" : {
    "author" : "xcode",
    "version" : 1
  }
}


================================================
FILE: CountriesSwiftUI\Resources\Assets.xcassets\AppIcon.appiconset\Contents.json
================================================
{
  "images" : [
    {
      "idiom" : "universal",
      "platform" : "ios",
      "size" : "1024x1024"
    },
    {
      "appearances" : [
        {
          "appearance" : "luminosity",
          "value" : "dark"
        }
      ],
      "idiom" : "universal",
      "platform" : "ios",
      "size" : "1024x1024"
    },
    {
      "appearances" : [
        {
          "appearance" : "luminosity",
          "value" : "tinted"
        }
      ],
      "idiom" : "universal",
      "platform" : "ios",
      "size" : "1024x1024"
    }
  ],
  "info" : {
    "author" : "xcode",
    "version" : 1
  }
}


================================================
FILE: CountriesSwiftUI\Resources\Preview Assets.xcassets\Contents.json
================================================
{
  "info" : {
    "author" : "xcode",
    "version" : 1
  }
}

```

## File: .github\FUNDING.yml
```
github: [nalexn]
custom: ["https://venmo.com/nallexn"]

```

## File: CountriesSwiftUI\Resources\Assets.xcassets\Contents.json
```
{
  "info" : {
    "author" : "xcode",
    "version" : 1
  }
}

```

## File: CountriesSwiftUI\Resources\Assets.xcassets\AccentColor.colorset\Contents.json
```
{
  "colors" : [
    {
      "idiom" : "universal"
    }
  ],
  "info" : {
    "author" : "xcode",
    "version" : 1
  }
}

```

## File: CountriesSwiftUI\Resources\Assets.xcassets\AppIcon.appiconset\Contents.json
```
{
  "images" : [
    {
      "idiom" : "universal",
      "platform" : "ios",
      "size" : "1024x1024"
    },
    {
      "appearances" : [
        {
          "appearance" : "luminosity",
          "value" : "dark"
        }
      ],
      "idiom" : "universal",
      "platform" : "ios",
      "size" : "1024x1024"
    },
    {
      "appearances" : [
        {
          "appearance" : "luminosity",
          "value" : "tinted"
        }
      ],
      "idiom" : "universal",
      "platform" : "ios",
      "size" : "1024x1024"
    }
  ],
  "info" : {
    "author" : "xcode",
    "version" : 1
  }
}

```

## File: CountriesSwiftUI\Resources\Preview Assets.xcassets\Contents.json
```
{
  "info" : {
    "author" : "xcode",
    "version" : 1
  }
}

```

